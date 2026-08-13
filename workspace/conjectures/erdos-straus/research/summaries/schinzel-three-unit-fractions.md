# Schinzel, "On sums of three unit fractions with polynomial denominators"

Source: https://projecteuclid.org/journalArticle/Download?urlid=10.7169%2Ffacm%2F1538186694
(Funct. Approx. Comment. Math. 28 (2000) 187–194; obtained via Project Euclid DOI
10.7169/facm/1538186694, the AMU-hosted PDF having failed to download).
Full text: `research/sources/schinzel-three-unit-fractions.full.md`

## What it establishes (sourced, primary)

Setting: polynomial identities of the form

```
m/(ax+b) = 1/F1(x) + 1/F2(x) + 1/F3(x)        (2)
```

with `a > 0`, `b` integer, `F_i ∈ Z[x]` with positive leading coefficients.
This is the standard shape of all "modular identity" families (set `n = ax+b`).

- **Theorem 1**: Let `a,b` be integers, `a > 0`, `(a,b) = 1`. If `b` is a
  **quadratic residue mod a**, then there are **no** polynomials `F1,F2,F3 ∈ Z[x]`
  with positive leading coefficients satisfying (2) with `m ≡ 0 mod 4`.
  The crucial case `m = 4` was quoted in Guy's book but the proof had never been
  published; Schinzel here gives the first published proof. The proof reduces to
  Yamamoto's Theorem 2 (Mem. Fac. Sci. Kyushu 19 (1965) 37–47) and a Kronecker/
  Jacobi-symbol evaluation, Lemma 2: `n² = 4(cs−b*)b*r − s` and `n²s =
  4(cs−b*)b*r − 1` have no positive-integer solutions.
- **Theorem 2**: Let `m,a,b` integers, `a > 0`, `m > 3b > 0`. There are **no**
  polynomials `F1,F2,F3 ∈ Z[x]` (positive leading coefficients) satisfying (2).
  It is conjecturally generalisable to `k` terms with `m > kb`.

## Consequence for this problem

This is the **precise statement of the obstruction** behind the six open classes.
For the class `n ≡ 1 (mod 840)`, write `n = 840k + 1`, i.e. `a = 840`, `b = 1`.
Since `1 = 1²` is a quadratic residue mod 840, **Theorem 1 says no polynomial
identity of the form `4/(840k+1) = 1/F1(k)+1/F2(k)+1/F3(k)` with `F_i ∈ Z[k]`
exists.** The same holds for each of the six residues `1, 121, 169, 289, 361,
529` — every one is a square mod 840 (also confirmed by Elsholtz–Tao Prop 1.6
via the vanishing of Type-I/II solutions at odd squares).

Hence any construction reaching `n ≡ 1 (mod 840)` must be of a shape **outside**
(2): a non-polynomial-identity construction, or rational functions whose
denominators are not in `Z[x]` with the stated conditions, or a finite-covering
argument that switches shape by sub-class (e.g. a sieve like Salez's, which
checks a set of residues modulo a huge modulus instead of one identity). This
is exactly the boundary Salez's "seven equations are complete for degree-1"
result also marks.

```claim
id: schinzel-thm1-polynomial-obstruction
answers: exact-statement-from-b7df
statement: If (a,b)=1 and b is a quadratic residue modulo a, then there are no polynomials F1,F2,F3 in Z[x] with positive leading coefficients satisfying 4/(ax+b) = 1/F1(x) + 1/F2(x) + 1/F3(x) (m ≡ 0 mod 4 case of Schinzel Theorem 1).
hypotheses: a>0, (a,b)=1, b a quadratic residue mod a, F_i in Z[x] with positive leading coefficients.
holds-here: true — with a=840, b=r for r in {1,121,169,289,361,529}, every r is a quadratic residue mod 840, so no such polynomial identity covers any open class.
status: sourced (Schinzel 2000, Theorem 1, first published proof; proof in full text; related to Yamamoto 1965).
bearing: THE precise obstruction. A single polynomial identity of the standard shape cannot cover n ≡ 1 (mod 840); a new family must leave the Z[x]-polynomial-identity form.
anchor: research/sources/schinzel-three-unit-fractions.full.md
```

```claim
id: schinzel-thm2-m-greater-3b
statement: If m > 3b > 0 and a > 0, there are no polynomials F1,F2,F3 in Z[x] with positive leading coefficients satisfying m/(ax+b) = 1/F1+1/F2+1/F3.
hypotheses: m,a,b integers, a>0, m>3b>0.
holds-here: false — this run's target is m=4 with b=1 (4 > 3), so Theorem 2 does not apply; Theorem 1 is the applicable obstruction.
status: sourced (Schinzel 2000, Theorem 2).
bearing: rules out one more naive shape (large-m identity families) but not the target shape.
anchor: research/sources/schinzel-three-unit-fractions.full.md
```