#!/usr/bin/env python3
"""Generate local synthesized narration from the reviewable JSON script."""
from pathlib import Path
import concurrent.futures
import json
import subprocess

root=Path(__file__).resolve().parent
out=root/"audio"
out.mkdir(exist_ok=True)
segments=json.loads((root/"narration.json").read_text())

def render(segment):
    ident=segment["id"]
    script=out/f"{ident}.txt"
    audio=out/f"{ident}.aiff"
    script.write_text(segment["text"]+"\n")
    subprocess.run(["say","-v","Samantha","-r","155","-f",str(script),"-o",str(audio)],check=True,capture_output=True)
    duration=float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","default=noprint_wrappers=1:nokey=1",str(audio)],text=True))
    return {**segment,"audio":str(audio.relative_to(root)),"audio_seconds":duration}

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
    rendered=list(pool.map(render,segments))
(root/"audio-manifest.json").write_text(json.dumps(rendered,indent=2)+"\n")
for segment in rendered:
    print(segment["id"],"spoken",round(segment["audio_seconds"],2),"target",segment["target_seconds"])
