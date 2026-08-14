# Directives

What an operator asked this run to do, and what the run did about it. Written by the runtime; edit the queue, not this file.

## 1 — from steer

download_document cannot reach publisher or preprint hosts on this run: the network boundary permits only the search and data APIs, so arxiv.org, doi.org, sciencedirect.com and springer.com will fail every time regardless of the URL. Stop retrying them. Use read_sources and deep_research instead, which fetch server-side and return the text. This is a property of the run's environment, not of the sources, and it is not a finding about the mathematics.

I read the workspace first. The directive is an environment fact, not a research finding, so I carried it into the three places that decide what roles do with it:

- **`TASKS.md`** — replaced the placeholder with the full phase order from the run directive, and wrote the fetch rule into phase 1: use `read_sources`/`deep_research` for the blocked hosts, do not retry `download_document` on arxiv.org/doi.org/sciencedirect.com/springer.com, and do not file it as a mathematical finding.
- **`CONTEXT.md`** — added a short **Environment** section so every role is told the host restriction on every call; it stays well inside budget.
- **`prompts/librarian.md`** — folded the host warning into the "failed download" guidance, keeping the original "try another source, record what failed" advice.

I made no other changes: the directive names no research gap (so no `request_research`), starts no direction of attack (no new thread), and abandons none. `research/ROOT.md` already notes the sources were obtained via `read_sources`, so the plan on disk is consistent with the directive.

## 2 — from steer

Stop gathering. You have 14 sources and a 97-line ROOT.md, and CONTEXT.md's Established section is still the empty placeholder with zero claim blocks filed - you have read everything and concluded nothing, which is the one failure phase 1 exists to prevent. Phase 1 is over as of now; further sources only against a stated gap in research/REQUESTS.md. Do three things in order. First, have scholar convert what is already in research/sources into fenced claim blocks with hypotheses, evidence class and falsifier, and write the corresponding beliefs into CONTEXT.md's Established section. Second, EXECUTE code/brute.py - it has never been run and there is no captured output anywhere in code/out - and calibrate it against the 7-vertex graph exactly as GOAL.md requires: all 11 edges certified unit in exact arithmetic, 4-colourable SAT, 3-colourable UNSAT, with the real output captured to code/out. Third, only then measure anything new with it. A checker nobody has run is not an oracle, and a source nobody has extracted is not a library.

Done. I rewrote `TASKS.md` so the order is now: (1) scholar writes the claim beliefs from `research/CLAIMS.md` into CONTEXT.md's **Established** section, (2) run `code/brute.py` under `timeout 540` with output teed to `code/out/brute.captured.txt` and confirm the 7-vertex calibration from that capture, (3) only then measure anything new. I opened `research/threads/oracle-calibration.md` for that calibration and amended CONTEXT.md with a short **State** section telling every role that phase 1 is closed and the oracle is not yet accepted.

One correction to the directive's premise, handled rather than ignored: the workspace shows a prior `timeout 120` run in `code/out/commands.log` and a "verbatim" output block in `code/out/oracle_calibration.md`, so "never been run" is not literally true — but that block's edge-list format does not match `brute.py`'s actual print format, so no trustworthy GOAL-conformant capture exists. I therefore recorded the directive's substance (produce and verify the capture before trusting the oracle) and left the existing `G-oracle-calibrated` claim flagged as not accepted.
