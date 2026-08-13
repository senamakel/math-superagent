# Kummer–Lucas p-adic approach — refutation note

Candidate mechanism: for a fixed prime p, the number of (n,k) pairs sharing the same
`(v_p(C(n,k)), C(n,k) mod p)` is bounded "at most logarithmically"; intersecting over
enough primes would then bound the number of representations of one a.

## The core lemma is false — the p-adic equivalence classes are large

Kummer's theorem (1852): `v_p(C(n,k))` = number of carries when adding k + (n−k) in
base p. Lucas's theorem: `C(n,k) ≡ ∏_i C(n_i,k_i) (mod p)`.

For **p=2**, the class `(v_2 = 0, residue ≡ 1 (mod 2))` contains every coefficient of
row `n = 2^m − 1`:
- All entries of row `2^m−1` are odd → `v_2(C(2^m−1, k)) = 0` for all k (no carries when
  adding two numbers whose digitwise sum has no overlap, i.e. k + (n−k) = n = all-ones).
- Every odd binomial coefficient is ≡ 1 (mod 2).
So there are exactly `2^m` values of (n,k) = (2^m−1, k), k=0..2^m−1, in ONE
(v_2, residue) class.

Thus the class size for the "no carry, residue 1" class of p=2 is `2^m` at n=2^m−1 —
**exponential in the bit-length, not logarithmic**. The proposed engine has no truth to
build on. This is the Sierpinski-triangle/fractal phenomenon: positive-density sets of
C(n,k) share each p-adic class.

## Consequence for the approach

The constraint "all representations of one a must lie in the same p-adic class" is real
but too weak: each class contains exponentially many candidates, so intersecting a few
primes cannot drive the count to O(1). In fact every power p-adic class is infinite in
the triangle (rows 2^m−1 for p=2 and their analogues), so no finite intersection of
prime classes bounds N(a).

This matches the literature: p-adic methods (Barát JLMS distribution of C(n,k) mod
prime powers; Sun–Zhang density in Z_p) study equidistribution/density, and none yields
a level-set cardinality bound. Same structural wall as the algebraic-geometry route:
local (per-prime, per-class) information does not control how many globally-distinct
(n,k) land on a single integer value.

## Verdict

**refuted**. The explicit obstruction: `(n,k)=(2^m−1,k)` gives 2^m pairs in one class
for p=2 (and the general row n=(p-1)pm^a analogue for generic p), so the "logarithmic
class size" lemma is unconditionally false. Killing line: a fixed p-adic class has
infinitely many members, so per-prime constraints cannot bound N(a).

```claim
id: kummer-lucas-class-not-logarithmic
statement: For a fixed prime p the p-adic equivalence class (v_p(C(n,k)) fixed, C(n,k)
  mod p fixed) contains exponentially many pairs: for p=2, all C(2^m-1,k) (k=0..2^m-1)
  are odd ≡1 (mod 2) with v_2=0, giving 2^m members of one class at n=2^m-1. The
  kummer-lucas-p-adic lemma ("class size grows logarithmically") is therefore false.
hypotheses: p=2 (argument generalizes to any p via n=(p-1)p^a-1 / Lucas carries).
holds-here: n/a — this refutes the approach's proposed lemma.
status: proved (Kummer/Lucas + the explicit all-ones row); elementary, no source needed
  beyond the definition.
bearing: Kills the kummer-lucas-p-adic candidate: local p-adic classes are large/infinite,
  so per-prime constraints cannot bound N(a).
anchor: research/notes/kummer-lucas-grounding.md
```
