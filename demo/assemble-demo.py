#!/usr/bin/env python3
"""Assemble the seven-scene 190-second demo around an actual Zetaris capture.

Usage: python3 demo/assemble-demo.py --zetaris demo/zetaris-live.mp4
Requires ffmpeg, ffprobe, generated broll PNGs, and audio-manifest.json.
The Zetaris capture must already be checked for passwords/private data.
"""
from pathlib import Path
import argparse
import json
import subprocess

parser=argparse.ArgumentParser()
parser.add_argument("--zetaris",required=True,type=Path)
parser.add_argument("--hmem-remember",type=Path)
parser.add_argument("--hmem-ask",type=Path)
parser.add_argument("--output",type=Path)
args=parser.parse_args()
root=Path(__file__).resolve().parent
capture=args.zetaris.resolve()
assert capture.is_file(),f"Missing real Zetaris capture: {capture}"
segments=json.loads((root/"audio-manifest.json").read_text())
out=root/"segments"
out.mkdir(exist_ok=True)

for segment in segments:
    ident=segment["id"]
    duration=segment["target_seconds"]
    assert segment["audio_seconds"] <= duration, f"Narration too long: {ident}"
    target=out/f"{ident}.mp4"
    custom_capture=args.hmem_remember if ident=="03-hmem-remember" else args.hmem_ask if ident=="04-hmem-ask" else None
    source=custom_capture.resolve() if custom_capture else root/segment["image"] if segment["image"] else capture
    is_still=bool(segment["image"] and not custom_capture)
    command=["ffmpeg","-hide_banner","-loglevel","error","-y"]
    if is_still:
        command += ["-loop","1","-framerate","30"]
    command += ["-i",str(source),"-i",str(root/segment["audio"])]
    filters=f"scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,setsar=1,fps=30,tpad=stop_mode=clone:stop_duration={duration}"
    if ident=="05-zetaris":
        command += ["-loop","1","-framerate","30","-i",str(root/"broll/zetaris-overlay.png"),"-filter_complex",f"[0:v]{filters}[base];[base][2:v]overlay=0:0[vout]","-map","[vout]"]
    else:
        command += ["-vf",filters,"-map","0:v:0"]
    command += ["-map","1:a:0","-af","apad","-t",str(duration),"-c:v","libx264","-preset","veryfast","-tune","stillimage","-crf","22","-pix_fmt","yuv420p","-r","30","-g","60","-c:a","aac","-b:a","128k","-ar","48000","-ac","2","-movflags","+faststart",str(target)]
    print("Rendering",ident,flush=True)
    subprocess.run(command,check=True)

concat=out/"concat.txt"
concat.write_text("".join(f"file '{s['id']}.mp4'\n" for s in segments))
video=args.output.resolve() if args.output else root/"hubcrew-demo.mp4"
subprocess.run(["ffmpeg","-hide_banner","-loglevel","error","-y","-f","concat","-safe","0","-i",str(concat),"-c","copy","-movflags","+faststart",str(video)],check=True)
probe=json.loads(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration,size:stream=codec_type,codec_name,width,height,r_frame_rate,sample_rate,channels","-of","json",str(video)],text=True))
(root/"video-metadata.json").write_text(json.dumps(probe,indent=2)+"\n")
assert 150 <= float(probe["format"]["duration"]) <= 220
assert int(probe["format"]["size"]) < 200_000_000
print(json.dumps(probe,indent=2))
