# Thread: pair-sum both-squares incompatibility

**Question.** For `q1, q2 ∈ Φ` with `q1 > q2` and `q1 + q2 < 1`, can
`1 − (q1+q2)` and `1 + (q1+q2)` be simultaneously rational squares?

**Status.** live — opened by directive 15; reframed by directive 19.

## Evidence

At M=400 (|Φ| = 32495, 156,988,030 pairs with `q1>q2` and `q1+q2<1`):
- 1−(q1+q2) is a rational square: **325** times
- 1+(q1+q2) is a rational square: **66** times
- **BOTH**: **0** times

At M=800 (|Φ| = 129870, budget-exhausted at i=22988/129870 = 17.7%):
- 1−(q1+q2) a rational square: 6 (partial — 17.7% of index; NOT comparable to M=400's 325)
- 1+(q1+q2) a rational square: 11 (partial; NOT comparable)
- **BOTH**: 0

Neither condition is empty, so both=0 is not an artefact of either being rare.
The partial M=800 numbers must never be quoted as a decline from M=400 — they
cover only 17.7% of the index. Operator is running a longer-budget M=800 on the
host.

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