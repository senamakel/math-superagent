# Ghosh 2009 — new lower bounds for the size of a non-trivial loop

<!-- src: R. Ghosh, "New lower bounds for the size of a non-trivial loop in the Collatz 3x+1 and generalized px+q problem", arXiv:0907.3086v4 (math.GM, Aug 2009). Full text: research/sources/ghosh-2009-new-lower-bounds-nontrivial-loop.full.md -->

## What the source establishes

Elementary fractional-part analysis of the cycle identity. For a non-trivial loop of the accelerated map T with m odd members a_1,…,a_m and a_min the minimum, the identity 2^(S_m) = ∏_i (3 + 1/a_i) (same identity as Hercher's bridge) gives

    3^m < 2^(S_m) < (3 + 1/a_min)^m,  i.e.  m log₂3 < S_m < m log₂3 + m log₂(1 + 1/(3a_min)).

Since S_m is an integer, existence forces a dichotomy:

- **α-loops**: m log₂(1 + 1/(3a_min)) > 1, hence a_min < α(m) = 1/(3(2^(1/m) − 1)).
- **β-loops**: m log₂(1 + 1/(3a_min)) < 1, hence a_min < β(m) = 1/(3(2^((1−{m log₂3})/m) − 1)), where {·} is the fractional part.

**Lower bounds on m** (using Oliveira e Silva's verification 19×2^58): an α-loop needs m > 11,387,806,137,299,329,586 odd members; a β-loop needs m ≥ 6,586,818,670 odd members.

**Generalization** to px+q: α_m(p,q) = q/(p(2^(1/m)−1)), β_m(p,q) = q/(p(2^((1−{m log₂ p})/m)−1)).

## Relation to the library

The β-loop bound 6,586,818,670 **matches** the Eliahou odd-integer bound in `lagarias-W2` (6,586,818,670 odd integers) — an independent derivation of the same number, cross-checking both. The fractional-part machinery on m·log₂3 is the same Diophantine lever as `zudilin-mu-8616` and Eliahou's one-sided continued fractions. Caveat: the paper is math.GM (unrefereed preprint), 6 pages; the α/β dichotomy is elementary and appears sound, but the m-bounds are only as good as the verification bound used (19×2^58 is long superseded by Barina's 2^71, which would raise all three numbers).

## Claims

```claim
id: ghosh-alpha-beta-dichotomy
statement: Any non-trivial Collatz loop with m odd members and minimum a_min satisfies either a_min < α(m) = 1/(3(2^(1/m)−1)) (α-loop, when m log₂(1+1/(3a_min)) > 1) or a_min < β(m) = 1/(3(2^((1−{m log₂3})/m)−1)) (β-loop, when m log₂(1+1/(3a_min)) < 1) (Ghosh 2009, arXiv:0907.3086).
hypotheses: non-trivial loop of the accelerated map T with m odd members
holds-here: yes — elementary consequence of the cycle identity 2^S = ∏(3+1/a_i)
status: asserted (unrefereed preprint, elementary proof)
bearing: upper bound on the minimum element of a cycle of given shape — the "upper arm" of the minimum-element analysis; dual to G-min-element-lower
anchor: research/summaries/ghosh-2009-new-lower-bounds-nontrivial-loop.md
```

```claim
id: ghosh-beta-loop-bound
statement: A β-loop must contain at least 6,586,818,670 odd numbers; an α-loop at least 11,387,806,137,299,329,586 odd numbers, using the then-current verification 19×2^58 (Oliveira e Silva) (Ghosh 2009).
hypotheses: verification to 19×2^58 (long superseded by Barina's 2^71)
holds-here: numbers are history — the method survives, the inputs are stale
status: asserted (unrefereed preprint)
bearing: the β number cross-checks lagarias-W2's 6,586,818,670; re-running with Barina's 2^71 would give the current numbers
anchor: research/summaries/ghosh-2009-new-lower-bounds-nontrivial-loop.md
```

```claim
id: ghosh-pxq-generalization
statement: For the generalized px+q problem, the analogous dichotomy holds with α_m(p,q) = q/(p(2^(1/m)−1)) and β_m(p,q) = q/(p(2^((1−{m log₂ p})/m)−1)) (Ghosh 2009).
hypotheses: p, q odd positive
holds-here: context only (this run is on 3x+1)
status: asserted (unrefereed preprint)
bearing: the same fractional-part lever generalizes to the px+q family
anchor: research/summaries/ghosh-2009-new-lower-bounds-nontrivial-loop.md
```
