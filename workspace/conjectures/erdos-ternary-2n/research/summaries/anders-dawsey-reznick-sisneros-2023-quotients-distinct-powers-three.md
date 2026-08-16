# Anders, Dawsey, Reznick & Sisneros-Thiry, "Representations of integers as quotients of sums of distinct powers of three"

Source: arXiv:2308.07252 (Aug 2023). Full text: `research/sources/anders-dawsey-reznick-sisneros-2023-quotients-distinct-powers-three.full.md`.

## What it is

The paper studies the set `S(3;{0,1})` — integers that are **sums of distinct powers of 3** (equivalently, numbers whose base-3 expansion uses only digits 0 and 1) — and it asks which integers are **quotients** `m = p(3)/q(3)` of two such sums. This is the set `A/A` where `A = {sums of distinct powers of 3}`.

Erdős's conjecture is precisely the statement that the *only* powers of 2 in `S(3;{0,1})` are `{1, 4, 256}`. This paper is about quotients rather than membership, so it does **not** settle the conjecture, but it develops the exact transducer machinery the run's directed route (symbolic invariant / carry structure on the base-2→base-3 conversion) needs.

## The relevant machinery — multiplication transducers under digit restriction

The paper works with **multiplication transducers in base 3**: for a multiplier `m`, a finite automaton that reads a base-3 digit string (representing an input `r`) and writes the base-3 digits of `m·r`. To restrict to numbers whose **output** digits lie in `{0,1}`, one deletes the edges that write a forbidden digit (here the digit `2`). The resulting pruned transducer recognises exactly the inputs `r` such that `m·r ∈ S(3;{0,1})`.

The carry state encodes the excess that must be resolved. Because the digit `2` is forbidden in the output, the automaton must resolve each multiplication step's carry by either remaining in `{0,1}` or propagating a "step up" through a looped carry value. This is a concrete, finite-state model of the power-of-2-in-S problem: `2^n ∈ S(3;{0,1})` iff the base-3 transducer scaling by `2^n`... more precisely, one considers scaling `r` by `m`; the run's problem is the special case studying the orbit of `1` under repeated ×2.

## Concrete results carried

- **Theorem 1.2**: For any integer `r`, if `m ∈ A/A` (a quotient of two sums of distinct powers of 3), then `m ∈ I_r = (2/3·3^r, 3/2·3^r)` for some `r`. So every representable quotient lies in one of these intervals — a necessary condition, **not sufficient** (the paper exhibits small counterexamples e.g. 529, 592, 601, 616).
- **Lemma 2.1**: `(st)(x) ∈ P` (sums of distinct powers, i.e. 0/1 polynomials) iff the supports `Δ(s) ∩ Δ(t) = ∅` — the digit vectors are disjoint. This is a clean structural characterisation of when a product of {0,1}-polynomials stays {0,1}, directly relevant to whether products/powers stay in the digit-{0,1} set.
- **Lemma 2.2, 2.3, Theorem 2.4**: conditions for shifted combinations `p(x) = Σ x^{n_j} p_j(x)` to remain in `P`.
- **Theorems 2.5–2.6, 3.1–3.3**: complete classification results for specific small integers (100, 22, 34, 64) as quotients — establishing some are representable (100) and others not (22, 34), with "universal" vs "local" representation distinctions.

## Relevance to this run

This is the strongest held source on the **transducer / carry-structure** approach — the exact direction GOAL.md and the oracle point at ("a carry/transducer statistic on the base-2 → base-3 conversion"). The relevant transferable insights:

1. **The digit-`2` output restriction is naturally encoded by pruning a multiplication transducer and keeping only digit-{0,1} states.** The set of carry states that can "survive" scaling into `{0,1}` is a finite-state object one could analyse for an invariant.
2. **Lemma 2.1 (support-disjointness) is the clean algebraic fact** that a product of distinct-powers-of-3 sets stays in the set exactly when the supports do not overlap. Since `2^n` is built by repeated squaring/multiplication, any `2^n ∈ S` must pass through a chain of products whose supports are pairwise disjoint at every step — a strong structural restriction on a minimal counterexample.
3. It confirms that membership of powers of 2 in `S` is *not* treated anywhere in this paper (it is a quotient paper), so the conjecture remains open and this is background machinery, not a route to the answer.

## Status

Sourced (arXiv preprint 2023). The transducer/automatic-set, carry-state and support-disjointness facts are quotable; none of them settles Erdős's conjecture. Store the structural facts (esp. Lemma 2.1 and the pruned-transducer model) in Cognee as the run's main automatic-sequence handle on the {0,1}-digit set.

```claim
id: ANDERS-PRODUCT-SUPPORT-DISJOINTNESS
statement: (Lemma 2.1) For s(x), t(x) in P (0/1-coefficient polynomials, i.e.
  sums of distinct powers of 3, evaluated at x with constant term possibly 0),
  (st)(x) in P iff the supports Delta(s) and Delta(t) of the two digit vectors
  are disjoint.
hypotheses: s, t are sums of distinct powers of 3 (digits 0 or 1 in base 3).
holds-here: yes -- a product/sum of two distinct-powers-of-3 numbers stays in
  the {0,1}-digit set exactly when the ternary digit positions used do not
  overlap. Any 2^n in the {0,1}-digit set must arise from a chain of such
  products with disjoint supports.
status: asserted-by-source (paper proves it; proof not re-derived here)
bearing: structural handle on the {0,1}-digit Cantor set S. Restricts how a
  product can stay in S. Background for the transducer/carry route; does not
  settle the conjecture.
anchor: research/sources/anders-dawsey-reznick-sisneros-2023-quotients-distinct-powers-three.full.md
```

```claim
id: ANDERS-QUOTIENT-INTERVAL-CONDITION
statement: (Theorem 1.2) If m is a quotient p(3)/q(3) of two sums of distinct
  powers of 3 (m in A/A), then m lies in I_r = (2/3 * 3^r, 3/2 * 3^r) for some
  integer r. Necessary, not sufficient.
hypotheses: m in A/A (quotient of two {0,1}-digit sums of powers of 3).
holds-here: yes as a structural fact about A/A; A/A contains 2^n only if it is
  in such an interval. Not directly a constraint on the powers-of-2 membership
  question.
status: asserted-by-source
bearing: necessary-condition structure for the quotient set; background.
anchor: research/sources/anders-dawsey-reznick-sisneros-2023-quotients-distinct-powers-three.full.md
```

## Status

Sourced (arXiv preprint 2023).
