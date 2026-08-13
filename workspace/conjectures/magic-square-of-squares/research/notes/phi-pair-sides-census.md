# Phi pair-side census claims — mirrored from code/out/

The claims below are computed facts from this run's own exact programs.
The evidence is in `code/out/`; this note exists because `research/CLAIMS.md`
is derived from notes under `research/` and claim blocks in `code/out/` alone
are invisible to it. Do not duplicate the prose — the note carries the claim,
the capture carries the evidence.

## M=800 complete census

```claim
id: phi-pair-sides-both-square-zero-through-M800
statement: For every M in {100, 200, 400, 800} and every pair q1 > q2 from
  Phi(M) with q1 + q2 < 1 (614165, 9856010, 156988030 and 2509516913 pairs
  respectively), the quantity 1-(q1+q2) is a rational square exactly {46,
  132, 325, 718} times and 1+(q1+q2) exactly {5, 24, 66, 150} times, and no
  pair has both rational squares. The M=800 count is a COMPLETE census over
  the full outer index (a prior partial capture that stopped at 18% of the
  index and reported 6/11/0 there is superseded).
hypotheses: M <= 800; q1, q2 in Phi(M); q1 > q2; q1 + q2 < 1; exact integer
  arithmetic throughout; M=800 run parallel over 26 workers, checkpoint sums
  equal the printed result, example witnesses re-verified independently
holds-here: yes for M <= 800 only; a computation, not a theorem for all M
status: checked
bearing: extends phi-pair-sides-never-both-square to a complete 2.5e9-pair
  census and **supersedes** it — the M=400 claim (156988030 pairs, 325 minus,
  66 plus) is a complete census at that size and is not wrong, but the M=800
  census is the current ceiling and the one every future claim must be checked
  against. A completed census is a different object from a partial sweep and
  must not be filed beside one.
anchor: code/out/side_census_result.md;
  code/out/side_census_M800_complete.captured.txt;
  code/out/side_census_stages_M800.jsonl;
  code/phi_triple_variety/side_census_par.py;
  code/out/side_census.captured.txt (M=400 serial)
source: operator-computation
```

## M=400 census (superseded by M=800 but independently established)

```claim
id: phi-pair-sides-never-both-square
statement: For all pairs q1 > q2 drawn from Phi(M) with q1 + q2 < 1 and
  M = 400 (32495 values of Phi, 156988030 pairs), the quantity 1-(q1+q2) is a
  rational square for exactly 325 pairs and 1+(q1+q2) is a rational square for
  exactly 66 pairs, and there is no pair for which both are rational squares.
  This also refutes the hypothesis recorded in the docstring of
  code/phi_triple_variety/side_census.py, that 1+(q1+q2) is never a rational
  square: it is a rational square 66 times, and three witnesses were verified
  independently in exact Fraction arithmetic with in_phi confirming both
  members lie in Phi.
hypotheses: M = 400; q1, q2 in Phi(M); q1 > q2; q1 + q2 < 1; exact integer
  arithmetic throughout, no floating point
holds-here: yes for the stated range only. This is a computation at M = 400 and
  is not a theorem for all M. The refutation of the docstring hypothesis is
  unconditional, since a counterexample settles it
status: checked
bearing: kills the side_census docstring hypothesis outright, so nothing may be
  built on 1+(q1+q2) being non-square. Replaces it with a sharper and so far
  unbroken statement, that the two square conditions are never simultaneously
  satisfied, which if proved would be an impossibility lemma on pair sums
  rather than on triples. Superseded in range by phi-pair-sides-both-square-zero-through-M800
anchor: code/out/side_census_result.md;
  code/out/side_census.captured.txt;
  code/phi_triple_variety/side_census.py
source: operator-computation
```