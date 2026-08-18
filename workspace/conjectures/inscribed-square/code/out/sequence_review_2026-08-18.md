# Sequence review (2026-08-18)

Executed `python code/extract_all_sequences.py`; this is the mechanical extraction output. Computation-bearing lists include polygon sizes `[8,12,16,20,24,32]`, doubled sizes `[4,8,12,16,20,24,32]`, sanity `[1,0,1]`, an all-zero broken-oracle artifact, and vertex output `[1,2,3,4,5,6,8]`.

Exact tool checks:
- `[8,12,16,20,24,32]`: differences `[4,4,4,4,8]`; every term divisible by 4; no constant-coefficient linear recurrence of order <=5.
- `[4,8,12,16,20,24,32]`: differences `[4,4,4,4,4,8]`; every term divisible by 4; no constant-coefficient recurrence of order <=6.
- OEIS lookup of the latter matched unrelated entries A376616, A034045, A160408, A180490, not a relevant geometric count.
- `[1,0,1]` has too few terms for a meaningful conjecture. The all-zero list is explicitly an oracle artifact. `[1,2,3,4,5,6,8]` was already identified as non-exact/conflicted with the boundary oracle.

Conclusion: no exploitable exact regularity. The divisibility-by-4 observation is tautological for polygon-size bookkeeping, not a conjecture about the square-peg problem. No larger run is warranted: it would only extend heterogeneous logs, not test a mathematical sequence. A putative continuation of the first-difference pattern would first be falsified at the next supplied polygon size if that size were 28 (but no such continuation is meaningful here).

## Pass 3 (same day, after further formalisation work)

Re-ran workspace-wide integer-list extraction restricted to files newer than this review's mtime. New files are Lean statements, kernel-verdict JSONs, claim notes, library reports, and config/.frontier.json. Integer lists in them are repeats of the sequences above (inside commands.log / out INDEX.md), plus one new 9-element list `[1,2,21,10,14,15,24,33,34]` in config/.frontier.json, which is a **bibliographic citation bracket** from the CDM paper introduction ("see for instance [1, 2, 21, 10, 14, 15, 24, 33, 34]"), not computed data — not a sequence, not analyzed.

Conclusion unchanged: no genuinely new computation-bearing integer sequence has landed since the 2nd pass; no exact exploitable regularity exists in the current artifacts. The only exact candidate sequence ([1,0,1]) is 3 terms; the 7-term sequence is rounded-rational and contradicts the exact boundary oracle; the rest are bookkeeping or artifacts. No larger run is warranted — extending them would mean inventing a computation the run never produced. Re-open only if a new oracle run produces exact counts (e.g., algebraic-exact inscribed-square counts over a family of curves).
