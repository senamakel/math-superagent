# Keramatipour Paley(9)-pattern theorem — status note and verification harness

Source: `research/sources/keramatipour-sat-conway99-body.full.md` (Keramatipour,
MPhil thesis, Churchill College Cambridge, June 2023; arXiv:2604.23037v1 —
**unrefereed preprint**). Summary: `research/summaries/keramatipour-sat-conway99-body.md`.

This note records the precise status of the Paley(9)-pattern claims so a later
role does not take them as load-bearing without checking the right thing.

## What is already CHECKED (does not need redoing)

**Lemma 3.4.1 — the pattern is present in both controls.** Verified by exact
enumeration: `code/out/paley9_pattern_check_fixed.captured.txt` shows rook(3)
(9 configs, ALL Paley(9)) and BvLS (13365 configs, ALL Paley(9)). The earlier
`paley9_pattern_check.captured.txt` traceback (`matching has 11 edges, need 7`)
was a script bug, not a graph property — the fixed run supersedes it. Claim
`keramatipour-no-paley9-pattern-99`'s lemma half is thus established on both
positive controls.

## What is UNCHECKED (the 99-specific theorem, and it must not be treated as load-bearing)

**Theorem 3.4.2 — a putative srg(99,14,1,2) cannot follow the Paley(9) pattern.**
Status: **asserted-by-source, unverified**. The thesis proof is an informal
case analysis. Its contradiction is that two vertices v and v' end up sharing
three common neighbours (violating μ=2): v = (1,3,x') and (1,3,x) both adjacent
to {(1,3),(2,4,y),(2,4,y')}. The k=14 arithmetic enters where vertex 5 must
have two neighbours in N_{1,3}, and the forced triangle must be
{5,(1,3,x),(2,4,y)}.

The proof does NOT rule out rook(3)=Paley(9) directly (rook has the pattern and
k=4, where the "vertex 5 needs two neighbours in N_{1,3}" step is vacuous), so
it is not obviously refuted on the 9-control — but it is NOT verified either.

## What the local deduction steps need (hand to coder)

`code/out/paley9_pattern_deductions.py` is a **corroboration harness only**: it
checks that the pattern's local edge-deduction rules (the C4 among
(1,5),(1,6),(2,5),(2,6); the parallelism C4 among (1,3,5),(1,4,5),(1,3,6),(1,4,6))
are self-consistent and match rook(3)'s 2x2-block adjacency. Running it does
**not** verify Thm 3.4.2's full 99-vertex contradiction; the required full step
is verifying that u ∈ N_{2,4}, v ∈ N_{1,3} with the stated three-common-
neighbour clash actually arises under a complete forced configuration. That is
a finite SAT/CP-SAT question (the whole point of the run's sat_solver line),
not a deduction-rules check — and it is the step a negative-control audit must
attack: does the same case analysis, run verbatim at k=22 (BvLS, which HAS the
pattern) either produce no contradiction (consistent with BvLS existing) or
produce a contradiction only because k=14 is special? If it produces the SAME
contradiction at k=22, the theorem is refuted on arrival by the BvLS control
and must be dropped.

This is the cleanest single next check for the `triangle-graph` / Paley-9
thread, and it is the only candidate "99-specific forbidden local
configuration" the library holds whose 99-exclusion step is genuinely
unchecked.

## Why this matters for the run

The run's deliverable includes "forced/forbidden local configuration." Thm
3.4.2 is the only in-library claim of that shape. If verified it is a real
99-specific structural constraint; if it reproduces at k=22 it is a false
positive the run must not cite. Either outcome is worth recording; the current
state is a stated gap.
