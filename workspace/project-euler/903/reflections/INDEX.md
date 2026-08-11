# Index — reflections

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `L0.0/1786462715957_01_learnings.md` | Attempt 1, judged unsolved, 1 learning(s). The entire attempt was delegated to a subagent whose invocation returned an HTTP 400 tool error, so nothing was executed — no program ran, no example was reproduced, and the effort ended before even the brute force existed. The concrete alternative: never gate all work behind an async subagent call that can fail silently; execute `/workspace/brute.py` directly in the main loop (and retry/fall back when a tool errors), so a provider error cannot masquerade as a dead end. A run with no executed program contradicts rule 1 regardless of how the failure is framed. |
| `L0.0/1786465799805_01_learnings.md` | Attempt 1, judged unsolved, 1 learning(s). The orchestrator again delegated the entire run to a single `goals` subagent whose invocation returned an HTTP 400 provider error, so no program ran and brute.py never existed — the same failure as attempt 1, so retrying against the same failing provider is the fix that will not work. The concrete alternative: don't route the whole run through one async subagent that can fail silently; execute /workspace/brute.py directly in the main loop (falling back to a different provider or running code inline on tool error), so a provider error cannot masquerade as a dead end and the worked examples actually get reproduced. |
| `L0.0/2_attempt_learnings.md` | _(undescribed)_ |
