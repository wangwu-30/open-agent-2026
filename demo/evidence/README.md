# Recorded H-MEM evidence

Recorded at 2026-10-27 01:24:28 北京时间.

The CLI ran the official Meterless H-MEM reference installed at `sponsors/hmem-notebook/vendor/hmem`. A new isolated temporary state directory was used. `remember` finished before `ask` was launched in a separate process. Both commands exited with code 0. No credentials or production data were used.

- `hmem-1-remember.txt`: actual stdout from the write command.
- `hmem-2-ask.txt`: actual stdout from the new-process retrieval command, including memory ID and provenance.
- `hmem-recorded-output.json`: command arguments, exit codes, stdout and stderr.

The B-roll labels these as recorded terminal output. It omits the temporary state path from the displayed startup line and shows a provenance excerpt; full outputs remain here. The retrieval reference uses hash vectors and retrieval-only mode, as documented in the bridge README. This recording does not demonstrate automatic end-to-end integration between HubCards, G1, H-MEM and Zetaris.
