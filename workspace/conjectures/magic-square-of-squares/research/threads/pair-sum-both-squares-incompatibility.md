# Thread: pair-sum both-squares incompatibility

**Question.** For `q1, q2 ∈ Φ` with `q1 > q2` and `q1 + q2 < 1`, can
`1 − (q1+q2)` and `1 + (q1+q2)` be simultaneously rational squares?

**Status.** live — opened by directive 15; reframed by directive 19.

## Evidence

Complete censuses, each over its full outer index (exact integer arithmetic):

| M | \|Φ(M)\| | pairs (`q1>q2`, `q1+q2<1`) | `1−(q1+q2)` square | `1+(q1+q2)` square | BOTH |
| --- | --- | --- | --- | --- | --- |
| 100 | 2040 | 614,165 | 46 | 5 | 0 |
| 200 | 8156 | 9,856,010 | 132 | 24 | 0 |
| 400 | 32495 | 156,988,030 | 325 | 66 | 0 |
| 800 | 129870 | 2,509,516,913 | 718 | 150 | 0 |

The M=800 row is the **COMPLETE** census (parallel, 26 workers;
`code/out/side_census_M800_complete.captured.txt`);
`code/out/side_census_stages_M800.jsonl` checkpoint sums equal the printed
totals. The earlier "17.7% partial" M=800 numbers (6/11/0) are superseded —
they covered only the smallest 18% of the index and must never be quoted.

## The prior hypothesis is refuted

The docstring of `side_census.py` claimed "1+(q1+q2) is NEVER a rational
square." That is false — it happens 66 times at M=400. Do not use the docstring
hypothesis as a prefilter justification anywhere. The both=0 finding is what
survived.

## Why this is a GLOBAL statement, not a local one

Directive 19 confirms what `hilbert-symbol-of-two-squares-trivially-split`
already established: if 1−s = t² and 1+s = u² then t²+u² = 2, a conic everywhere
locally soluble, and Hasse-Minkowski gives nothing. The Hilbert symbols
(t², u²)_p = 1 at every prime. **No Q-level local or congruence obstruction can
explain both=0.** The earlier steer toward local obstructions was wrong; this
claim settles it. The both=0 finding is a GLOBAL statement.

## The concordant-forms elliptic-curve frame

`concordant-forms-iff-ell-torsion-order-2` gives the right language: the
condition "both 1−s and 1+s are rational squares" is equivalent to the elliptic
curve

> E_{M,N}: y² = x(x+M)(x+N)

having a rational point of order greater than 2 (finite or infinite), where
M, N derive from s = q1+q2.

**So the both=0 question becomes:** does Φ-membership of the summands force
E_{M,N} to have rank 0 or the wrong torsion, for every pair? This connects the
cheap pair-level observation to the workspace's standing blocker — uniform
boundedness of ranks — rather than being a separate lead.

## Next step: test on the witnesses

Take the 66 plus-witnesses and the 325 minus-witnesses from
`code/out/side_census.captured.txt`, form E_{M,N} for each, and compute rank
and torsion. If the minus-witnesses and plus-witnesses split cleanly by rank or
torsion, that is the mechanism behind both=0 and it is checkable now.

**Any lemma proposed from this must be run against these witnesses or it is
asserted, never checked.**

```claim
id: phi-pair-sides-both-square-zero-through-M800
statement: For every M in {100, 200, 400, 800} and every pair q1 > q2 from
  Phi(M) with q1 + q2 < 1 (614165, 9856010, 156988030 and 2509516913 pairs
  respectively), the quantity 1-(q1+q2) is a rational square exactly {46,
  132, 325, 718} times and 1+(q1+q2) exactly {5, 24, 66, 150} times, and no
  pair has both rational squares. The M=800 counts are a COMPLETE census
  over the full outer index (parallel, 26 workers; a prior partial capture
  that stopped at 18% of the index and reported 6/11/0 there is
  superseded). Each side condition alone is satisfiable at every M, so
  both=0 is not an artefact of either side being empty.
hypotheses: M <= 800; q1, q2 in Phi(M); q1 > q2; q1 + q2 < 1; exact integer
  arithmetic throughout; M=800 run checkpointed with sums equal to the
  printed result, example witnesses re-verified independently
holds-here: yes for M <= 800 only; a computation, not a theorem for all M
status: checked
bearing: the strongest unbroken side statement — the two square conditions
  1+s and 1-s are never simultaneously satisfied for a pair-sum s
  realisable from Phi — now stands over a complete 2.5e9-pair census. A
  proof of the incompatibility (s = 2t/(1+t^2) parametrisation of
  x^2+y^2=2 intersected with Phi-pair-sums) would be an impossibility lemma
  on pair sums; it would not forbid the known near-miss witnesses, which
  are not pair sums of Phi elements in (0,1) with both sides square.
anchor: code/out/side_census_M800_complete.captured.txt;
  code/out/side_census_stages_M800.jsonl;
  code/phi_triple_variety/side_census_par.py;
  code/out/side_census.captured.txt (M=400 serial)
source: operator-computation
```

```thread
question: For q1,q2 in Phi with q1>q2 and q1+q2<1, can 1-(q1+q2) and
  1+(q1+q2) be simultaneously rational squares? Complete censuses: M=100:
  46 minus / 5 plus; M=200: 132/24; M=400: 325/66; M=800 (COMPLETE over the
  whole outer index of 129870 values, 2509516913 pairs): 718 minus / 150
  plus, BOTH=0 at every size. This is a GLOBAL statement: no Q-level local
  or congruence obstruction can explain it. The concordant-forms dictionary
  (concordant-forms-iff-ell-torsion-order-2) reframes it as: does Phi-
  membership force E_{M,N}: y²=x(x+M)(x+N) to have rank 0 or wrong torsion,
  for every pair? This connects the cheap pair-level observation to the
  run's standing blocker — uniform boundedness of ranks.
status: live
rests-on: phi-universal-set, phi-pair-sides-both-square-zero-through-M800,
  concordant-forms-iff-ell-torsion-order-2,
  hilbert-symbol-of-two-squares-trivially-split
blocked-by: both=0 verified at M=100,200,400 and COMPLETE at M=800; the 150
  plus-witnesses and 718 minus-witnesses need their concordant curves; an
  incompatibility proof is still missing
next: form E_{M,N} for the 150 plus-witnesses and 718 minus-witnesses from
  side_census_M800_complete.captured.txt; compute rank+torsion for each;
  check whether the two sets split cleanly by rank or torsion; state any
  split found as a claim with the witnesses as falsifier
```