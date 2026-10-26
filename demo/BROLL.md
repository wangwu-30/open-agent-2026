# Demo B-roll assets

Seven 1920 × 1080 cards are in `broll/`. They distinguish the architecture from the two demonstrated sponsor bridges. The H-MEM cards use actual recorded command output saved in `evidence/`; they explicitly label the replay and identify omitted temporary-path / provenance fields.

Open `demo/broll/index.html` in a browser, or serve it locally:

```sh
python3 -m http.server 8766 --bind 127.0.0.1 --directory demo/broll
```

Then visit `http://127.0.0.1:8766/?page=1`. Arrow keys change cards, number keys 1–7 select a card, and F enters fullscreen. Card 5 is an optional introduction; the assembly script uses the actual Zetaris browser capture in its place.

The English narration is reviewable in `narration.json`. `generate-narration.py` uses the local macOS Samantha voice; the synthesized audio is in `audio/` and its duration manifest is `audio-manifest.json`. Rendered cards can be rebuilt using `render-broll.py` with Pillow and the macOS fonts referenced there.

After recording a safe Zetaris browser clip with the result visible for at least ten seconds:

```sh
python3 demo/assemble-demo.py --zetaris demo/zetaris-live.mp4
```

This produces `demo/hubcrew-demo.mp4` with 1080p, 30 fps, H.264, and AAC audio. Target length is 190 seconds (3:10). The seven segments are 15, 25, 22, 33, 40, 30, and 25 seconds. The Zetaris segment uses the first 40 seconds of the supplied capture, retaining the last frame if the capture is shorter. Ensure the selected capture begins with the relevant UI and includes the actual query result. The script validates total duration and a size below 200 MB, and saves `video-metadata.json`.

The final Zetaris clip was recorded as real browser screenshots sampled at 2 fps during manual query execution, then encoded at 30 fps. Its labels state `localhost:3000 · LIVE SQL · supplied samples · manual demo mapping` and disclose the sampling method. The displayed result data is unchanged. The local query completes at 14.381 seconds and its five result rows remain on screen for more than ten seconds.

No secrets, production memory, or private chat content were used in the B-roll. No unrecorded end-to-end integration is claimed.
