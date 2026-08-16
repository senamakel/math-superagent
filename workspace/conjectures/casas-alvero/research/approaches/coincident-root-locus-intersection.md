# Intersection theory on the coincident-root-locus stratification (refuted)

```approach
idea: Bézout against the discriminant: deg_a R_i = 2n−i, so
       V(R_1,…,R_{n−1}) ⊂ A^{n−1} has Bézout degree ∏_{i=1}^{n−1}(2n−i) =
       (2n−1)!/n!, while CA says it is the single reduced point {(x−a)^n}.
       Decompose the excess degree over the coincident-root-locus strata X_λ of
       the discriminant, using Fulton's excess-intersection formula and the
       Chow classes of the X_λ.
mechanism: excess intersection over the discriminant stratification; the
       "residual off-Δ term" would be shown empty by a degree identity.
status: refuted
killed-by: (1) Factual premise false — R_i = Res(f, H_i f) = ∏_j H_i f(β_j)
       vanishes on a stratum X_λ only when λ has some part ≥ i+1 (a root of
       multiplicity m kills H_1,…,H_{m-1} there, not H_i for i ≥ m). So R_i does
       NOT vanish on all of Δ = ∪_{λ≠(n)} X_λ; e.g. n=4, f=(x−a)²(x−b)(x−c) has
       R_2 ≠ 0. (2) Deeper, the residual is tautological — a CA counterexample
       is squarefree with ≥5 distinct roots (Laterveer–Ounaïes), so counterexample
       components lie in X_{(1^n)}, OFF the discriminant; "residual off-Δ term
       empty" is literally "no counterexamples", not a reduction. The degree
       identity would require knowing the counterexample components to compute
       the residual. (3) What survives is the statement "multiplicity of the
       pure-power point alone equals ∏(2n−i)", which is exactly the complete-
       intersection / regular-sequence reformulation the run already adopts
       (ghosh-complete-intersection, schaub-spivakovsky bad-prime minors,
       arithmetic-jet-lift) — bookkeeping on the adopted line, not a new attack.
precedent: _unchecked_
charp-break: Chow classes / plethysm are char-0 Springer/S_n theory (stated, not
       the reason this died — the false premise and the tautological residual are
       char-0 obstructions).
```

## Why it closed

The excess-intersection framing looked like it would produce a finite degree
identity per `n`. It cannot:

1. **The stratification is wrong.** Each resultant `R_i` is the divisor where `f`
   shares a root with `H_i f`. That does not contain the full discriminant: a
   root of multiplicity `m` forces `R_i = 0` only for `i ≤ m−1`. The locus
   `V(R_1,…,R_{n−1})` is the CA scheme itself, not a scheme supported on `Δ`.
2. **The residual is the conjecture.** A hypothetical counterexample has
   `≥ 5` distinct roots (all multiplicity 1), so it lies in `X_{(1^n)}`, which
   is the *complement* of the discriminant. The "residual off-Δ term" is by
   definition the counterexample components. Showing it is empty is proving CA;
   the degree bookkeeping adds no inference, it only reformats the answer.
3. **The one non-tautological piece is already adopted.** The claim "the pure-
   power point absorbs the whole Bézout degree" is the regularity / complete-
   intersection statement `√(R_1,…,R_{n−1}) = (a_1,…,a_{n−1})` (Schaub–
   Spivakovsky) — the run's adopted arithmetic-jet-lift engine already computes
   exactly this as the minors `J_T` whose prime divisors are the bad primes.
   Excess intersection would be a *certificate format* for that computation, not
   a different route past its Gröbner/rank wall.
