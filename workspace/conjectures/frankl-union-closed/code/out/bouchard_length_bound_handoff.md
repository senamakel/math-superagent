# Handoff — run the Bouchard length-bound oracle check (coder)

Run: `python3 code/out/bouchard_length_bound_check.py` (capture to
`code/out/bouchard_length_bound_check.captured.txt`, 3-line header: what ran,
oracle fn lib.uc.decide_union_closed, range n=1..4 exhaustive).

What it settles: Bouchard (arXiv:2511.10608) Theorem 1 under the CORRECTED
definition of ell = (max inclusion-chain size) − 1 (a gloss in the old summary
claimed "size of largest member set", which fails on the equality family — see
`code/out/bouchard_length_bound_finding.md`).

Expected: under the chain reading, 0 bound-violations and 0 equality-iff
violations for n=1..4; under the wrong largest-member reading, violations
appear (confirming the correction). Do not drift the claim to "proved" — the
exhaustive pass for n≤4 is evidence; the theorem is proved from the source's
own induction. If all four n pass cleanly, an entry may promote
`bouchard-upper-bound-length` to status `checked` for n≤4.
