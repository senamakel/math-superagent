# Thread: pair-sum both-squares incompatibility

**Question.** For `q1, q2 ∈ Φ` with `q1 > q2` and `q1 + q2 < 1`, can
`1 − (q1+q2)` and `1 + (q1+q2)` be simultaneously rational squares?
If not — if the two square conditions are provably incompatible — that
would be an impossibility lemma on **pairs**, which is cheaper than anything
on triples. A Φ-triple `q3 = q1 + q2 ∈ Φ` needs both `1 − q3` and `1 + q3`
to be rational squares (every member of Φ has that property), so proving
that no sum `s = q1+q2` of two Φ-values can have both `1 ± s` square would
rule out Φ-triples *without* testing membership of the sum.

**Status.** live — opened by directive 15.

**Evidence.** At M=400 (|Φ| = 32495, 156,988,030 pairs with `q1>q2` and
`q1+q2<1`):
- 1−(q1+q2) is a rational square: **325** times
- 1+(q1+q2) is a rational square: **66** times
- **BOTH**: **0** times

Neither condition is empty, so the both=0 is not an artefact of either being
rare. Every one of the 66 plus-witnesses inspected has 1−(q1+q2) a non-square,
and vice versa. Three witnesses were re-verified in exact Fraction arithmetic
with `in_phi` confirming both members lie in Φ:

| q1 | q2 |
| --- | --- |
| 1476984/9765625 | 1257456/21390625 |
| 2258256/17181025 | 6571656/193905625 |
| 10226040/65237929 | 70160160/534950641 |

**The prior hypothesis is refuted.** The docstring of `side_census.py` claimed
"1+(q1+q2) is NEVER a rational square." That is false — it happens 66 times
at M=400. Do not use the docstring hypothesis as a prefilter justification
anywhere. The both=0 finding is what survived and is the thing to work on.

**Why this is promising.** The condition "both 1−s and 1+s are rational
squares" is the classical **concordant-forms** shape: two numbers differing
by a rational square are simultaneously squares. Specifically, if 1−s = t²
and 1+s = u² with t,u ∈ Q, then t² + u² = 2, and the point (t,u) lies on
the circle x² + y² = 2. But s = q1+q2 is not an arbitrary rational — it is
a sum of two Φ-values, each itself of the form f(m,n) = sin(4 arctan(n/m)).
The question is whether this structure forces s into a form that is
incompatible with the concordant condition.

**Next steps.**
1. **Re-run side_census at larger M** (directive 15): `PYTHONPATH=code timeout
   540 python3 code/phi_triple_variety/side_census.py 800 500`. See if both=0
   survives. This is the immediate task in TASKS.md.
2. **Run the remaining six phi_triple_variety programs** — never been executed.
   The independent verifiers must agree with the side_census finding.
3. **Name the invariant.** If both=0 is provable, what invariant separates
   the 66 pairs where 1+s is square from the 325 where 1−s is square? A
   congruence obstruction modulo some modulus, or a descent on the elliptic
   curve `y² = (1−s)(1+s)` (which is an elliptic curve in the variable s)?
4. **Frame as a concordant-forms question.** The simultaneous conditions
   `1−s = t²`, `1+s = u²` are equivalent to the elliptic curve
   `E_s: v² = (1−s)(1+s)` having a rational point with v ≠ 0. The sum
   `s = q1+q2` is a rational with a specific structure (sum of two sin(4θ)
   values). Can the Mordell–Weil group of the associated curve be controlled?
5. **Correlate with the known 7-square witness.** Bremner's grid has
   `q_v + q_{u+v} > 1`, so the clip condition already kills it — but both=0
   is about sums < 1. Find or construct a pair with sum < 1 from the witness
   or from a known near-miss, and test whether both 1±s are square — the
   expected answer is no (both=0 survives), and a yes would refute the
   incompatibility.

```thread
question: For q1,q2 in Phi with q1>q2 and q1+q2<1, can 1-(q1+q2) and
  1+(q1+q2) be simultaneously rational squares? At M=400: 325 minus-square
  pairs, 66 plus-square pairs, and BOTH=0. If both=0 is provable, that is
  an impossibility lemma on pairs, which rules out Φ-triples without testing
  membership of the sum.
status: live
rests-on: phi-universal-set, phi-pair-sides-never-both-square,
  concordant-forms-iff-ell-torsion-order-2
blocked-by: both=0 only verified at M=400; need M=800 and then a proof
next: re-run side_census at M=800; run the six unrun phi_triple_variety
  programs; name the invariant separating the plus and minus pairs; frame
  as a concordant-forms question on the associated elliptic curve
```