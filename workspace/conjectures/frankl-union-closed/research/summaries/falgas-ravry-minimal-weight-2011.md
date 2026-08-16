# Falgas-Ravry, "Minimal weight in union-closed families" — arXiv:1101.2589 (2011)

Full body: [[falgas-ravry-minimal-weight-2011.full]]

This paper is **about the minimal weight (total size) problem for separating
union-closed families**, not directly a new UC bound. It is the source ROOT.md
cites for the separating-families thread, so its actual content must be stated
exactly.

## What it establishes (verified in body)

- **Definitions.** A family `S` *separates* pair `(i,j)` if some `A∈S`
  contains exactly one of `i,j`; `S` is separating if it separates every pair.
  `w(S) = Σ_{A∈S}|A|` is the weight.
- **Reimer's Average Set Size Theorem** (stated, prior result): for union-closed
  `S`, `(1/|S|)Σ_{A∈S}|A| ≥ log₂|S|/2`, equality iff powerset. Equivalently
  `w(S) ≥ (|S|log₂|S|)/2`.
- **Theorem 3 (main structural result).** A separating union-closed `S` on
  `[n]` (elements by increasing degree) has `d_S(i) ≥ i−1` for all `i`.
  Hence `|S| ≥ n−1` and `w(S) ≥ C(n,2)`, equality iff `S` is the staircase
  `T_n = {{n},{n−1,n},…,{2,…,n}}` or `T_n ∪ {∅}`. This beats Reimer when
  `Ω > √(|S|log₂|S|)`.
- **Theorem 5 / Corollary 6.** Weight bounds and asymptotically sharp (to
  factor 2) lower bound on average degree of separating union-closed families:
  `(1/|Ω|)Σ d_S(x) ≥ (1/2)√(|S|log₂|S|) + O(1)`.
- A separating union-closed family's domain size satisfies
  `n−1 ≤ m ≤ 2^n` (satisfiable pairs), and a union-closed `S` of size `m` is
  at most `(m+1)`-separating.

## What this source does NOT contain, and the correct attribution

- **The "separating families with |F| ≤ 2m are UC" bound is NOT stated as a
  theorem in this paper.** It contains the *construction* (Theorem 1.2 in
  Maßberg's numbering = this paper's Lemma 2: the `A_i = [n]∖[i] ∪ X_i` sets)
  from which Maßberg (arXiv:1508.05718) derives the `≤2m ⟹ UC` corollary
  (Maßberg Lemma 1.3) and then improves to `2(m + m/(log₂m−log₂log₂m))`.
  So ROOT.md's "separating |F|≤2m, Falgas-Ravry arXiv:1101.2589, improved by
  Maßberg" is **correct in attribution** (Maßberg's ref [3] is exactly this
  weight paper), but the `2m` UC bound itself is a *corollary proved in
  Maßberg on top of Falgas-Ravry's construction*, not a statement of the weight
  paper. The same construction (Lemma 2 here) is Maßberg Theorem 1.2.
- This paper does not prove UC itself; the introduction only restates that UC
  holds for `|S| < 40` or `|V(S)| < 11` or `|S| > (5/8)2^|V(S)|` (citing
  others), and its own content is the minimal-weight problem.

## Hypotheses and holds-here

- `S` finite union-closed, separating on `[n]`. Theorems are for separating
  families. **Holds-here: yes** for the weight/degree claims (structural facts
  about separating union-closed families, usable as constraints).
- All results **proved in-paper** (no numerics).

## What it lets the run do

- The degree lower bound `d_S(i) ≥ i−1` for separating families is a concrete
  structural constraint: for every `i`-th element by degree, its abundance is
  at least `(i−1)/|S|`. This is a lower bound on individual-element abundance
  in separating families — a directly usable fact for the abundance-profile
  thread.
- **Warning for the library (attribution clarified).** ROOT.md's "separating
  |F|≤2m, Falgas-Ravry arXiv:1101.2589, improved by Maßberg" is **correct in
  attribution**: Maßberg's ref [3] is exactly this weight paper, and its
  Lemma-2 construction (Maßberg's Theorem 1.2) is what the `≤2m ⟹ UC`
  corollary is built on. The only refinement to note: the `≤2m ⟹ UC` bound
  itself is a corollary *proved in Maßberg*, not a theorem stated in the weight
  paper — so cite Maßberg (arXiv:1508.05718) for the bound and Falgas-Ravry for
  the underlying construction.

```claim
id: falgas-ravry-separating-degree
statement: A separating union-closed family S on [n] (elements ordered by
  increasing degree) has d_S(i) ≥ i−1 for all i, so |S|≥n−1 and w(S)≥C(n,2),
  equality iff the staircase T_n or T_n∪{∅}; average degree over Ω is
  ≥(1/2)√(|S|log₂|S|)+O(1), asymptotically sharp to factor 2.
hypotheses: S finite, union-closed, separating (point-separating on its domain)
holds-here: yes
status: proved
bearing: a structural lower bound on individual-element abundance in
  separating families, usable by the abundance-profile thread; also contains the
  A_i-set construction that is Maßberg's Theorem 1.2, on top of which Maßberg
  proves the '≤2m ⟹ UC' corollary and the pushed bound — so ROOT's attribution
  of the 2m separating bound to this file is right (Maßberg ref [3]), but the
  UC bound itself is proved in Maßberg, not here
anchor: research/sources/falgas-ravry-minimal-weight-2011.full.md, Thms 3,5, Cor 6
```
