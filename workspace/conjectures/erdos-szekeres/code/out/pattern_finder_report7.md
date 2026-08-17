# Pattern-finder round 7 — NOTHING FURTHER (except one derived sequence already filed)

## What changed since the last look, and what did not

I re-surveyed the result files newer than pattern-finder round 6:

- `triple_inter.captured.txt` — single-n=7 fact: the even/odd 16–16 block
  bipartition IS a triple half-plane-intersection (min k=3), NOT a single side
  (k=1) nor a double-wedge intersection (k=2). One number, already recorded as
  done in the tasks ledger. No sequence.
- `evenodd_cutfamily.captured.txt` — same single-n=7 verdict (min k=3), counting-cut
  corroboration. No sequence.
- `wedge_sidepair.captured2.txt` / `.captured.txt` — n=7 only: 27 valid side-pair
  splits, 2454 distinct size-16 bipartitions, 1/27 wedge-consistent at the witness
  apex. Single n; recorded done.
- `wedge_evenodd_alln.captured.txt` — per-n (n=5,6,7) even/odd rows: sides
  False/False/False, double-wedge True/True/False. The 3-term "sequence" is a
  trivial categorical threshold decay already described in CONTEXT.md.
- `layer_extremality.captured.txt` — per-n onion-layer Conjecture C PASS/FAIL
  (FAIL n=4, PASS n=5,6,7). Binary, no exploitable numeric sequence.
- `factorization_survival.captured.txt` / `factorization_staircase_n7.captured.txt` —
  placement-property verdicts on the per-block goodness factorization (holds arc
  + staircase, FAILS scrambled-y). Already closed in tasks as a placement property.
- `maxconvex_structure.captured.txt` — per-pattern multiplicity table; its closed
  form (realized-pattern bijection, triangular classes, corner-pairs/six-FULL,
  goodness factorization) is already fully tabulated across pattern-finder
  rounds 3–6 and the claim files; no new regularity emerged.

None of these carries a new integer sequence beyond what rounds 1–6 recorded.

## The one legitimately new item, filed separately

The **non-convex-4-subset counts** NNC(N) = C(N,4) − convex4(N) of es_construct,
derived from ALREADY-CAPTURED convex-4 rows (32, 701, 12740, 213190 for n=5..8;
OEIS miss; not polynomial) plus the covering-ratio test at N=2^{n−2}
(NNC·C(N−4,n−4)/C(N,n) = 2.29, 5.78, 12.40, 23.49 — holds with increasing slack).
See `code/out/nnc_from_captured_claim.md`. This is the exact first-step quantity
of the open queued task `con4-supersat-nnc-count`, which is why it is recorded
despite the general es_construct-count prohibition (directive 22): it feeds a
live open task rather than extending the template's spectrum.

## Verdict

For all other captured data, the results have not changed since the last
pattern-finder pass and hold too few per-n terms to assert any exact sequence
beyond what is already recorded. Per the brief, **NOTHING FURTHER** — I am not
extending any es_construct spectrum (directive 22), and I did not compute a
second family's values because the Karolyi–Toth twin is not realized on disk and
the Aichholzer fetch is still queued.
