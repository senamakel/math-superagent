# Bilu–Tichy 2000 — The Diophantine equation f(x)=g(y) (PRIMARY, the classification paper)

Source: Y.F. Bilu, R.F. Tichy, "The Diophantine equation f(x)=g(y)", Acta
Arithmetica XCV.3 (2000) 261–288. Full text read:
`research/sources/bilu-tichy-2000-fxgy.full.md`.
URL: https://matwbn.icm.edu.pl/ksiazki/aa/aa95/aa9534.pdf

## What the paper establishes

**The explicit finiteness criterion for `f(x)=g(y)`** (f,g ∈ Q[x] nonconstant).

Theorem 1.1 (= Theorem 10.5 for K=Q, O_S=Z): the equation (1) has **infinitely
many rational solutions with a bounded denominator** iff
`f = φ∘f₁∘λ` and `g = φ∘g₁∘µ` for linear λ,µ, some φ ∈ Q[x], and a **standard
pair** `(f₁,g₁)` over Q such that `f₁(x)=g₁(y)` itself has infinitely many
bounded-denominator solutions.

**Five standard-pair kinds** (§1.1):
1. `(x^m, ax^r p(x)^m)` or switched, `0≤r<m, (r,m)=1` — infinite family
   `x = a^q t^r p(a^s t^m)`, `y = a^s t^m` with `qm−sr=1`.
2. `(x², (ax²+b)p(x)²)` — infinite for infinitely many a,b (via `u²=av²+b`).
3. `(D_m(x,a^n), D_n(x,a^m))`, gcd(m,n)=1 (Dickson) — infinite family
   `x=D_n(t,a), y=D_m(t,a)`, t ∈ Z.
4. `(a^{−m/2}D_m(x,a), −b^{−n/2}D_n(x,b))`, gcd(m,n)=2 — infinite for infinitely
   many a,b (via `a^{m/2}u²+bv²=4ab`).
5. `((ax²−1)³, 3x⁴−4x³)` — infinite for infinitely many a (via `3au²=v²+2`).

**Key consequences for this run:**
- For `gcd(deg f, deg g)=1`, φ is linear and only kinds 1 and 3 occur (Remark
  1.2(ii), reproducing Schinzel's criterion).
- If the leading coefficients `a_p, b_q` have `a_p/b_q` not a perfect `deg φ`-th
  power, then `deg φ = 1` (Remark 1.2(iii)); the example given is exactly
  `C(x,m) = y(y−1)…(y−n+1)` — the falling-factorial / binomial form — having
  finitely many solutions when m,n > 2. This is the immediate ancestor of the
  run's `bilu-tichy-method-ineffective-uniformity-wall` claim.
- The proof route (Section 1.4, Sections 4–10): exceptional factor (genus 0,
  ≤ 2 points at infinity) → Ritt's second theorem classification (Thm 6.1) for
  `gcd(m,n) ≤ 2` → Fried's reduction (Thm 8.1) + quadratic factors (Thm 8.2)
  → standard or "specific" pairs (Thm 9.3) → Siegel's theorem (Thm 10.1).
- Theorem 10.5 generalizes to S-integers of a number field; the "specific pair"
  case only occurs for K ≠ Q / O_S ≠ Z. **For K=Q, O_S=Z, only the five standard
  kinds occur.** This is the classification HPT 2022 (the run's HPT full text)
  applies to the binomial problem `C(x,k1)=C(y,k2)`.
- **The genus formula** (Prop 4.1): `2g−2 = Σ_γ (mn−Ω(γ)) − mn − gcd(m,n)`
  with `Ω(γ)=Σ(µᵢ,νⱼ)` over root-multiplicities of f−γ, g−γ. This is Fried's
  formula, the tool behind the run's closed-form genus computations and BST's
  classification — the run's `k2=2,3,4,5` closed forms are special cases.

## Bearing for this run

- **Primary source of the Bilu–Tichy classification** that the run's
  `bilu-tichy-grounding.md` and HPT 2022 rely on. It confirms that the HPT
  exceptional-pair classification for the binomial problem is the specialization
  (`r=0,c=0,d=1` arithmetic-progression products) of this five-kind list, and
  that **finiteness per fixed (k1,k2) is the Siegel-based content** — while the
  classification itself is a *criterion* ("infinite ⟺ standard pair"), it gives
  **no bound on the number of solutions** and is **ineffective** (Siegel's
  theorem, which it invokes, is ineffective).
- Therefore it **confirms, at the primary level, the run's**
  `bilu-tichy-method-ineffective-uniformity-wall`: the classification tells you
  *whether* a family is infinite (the exceptional pairs), but supplies no count
  computable in (k1,k2), and the effective routes (Baker-type) are per-curve.
- The binomial example in Remark 1.2(iii) (`C(x,m)=y(y−1)…(y−n+1)`, m,n>2,
  finitely many solutions) is a direct ancestor of the run's small-column curves
  and shows the classification was already aimed at binomial forms.
- The genus formula (Prop 4.1) is a checkable machine route for the run's genus
  closed forms (an independent verification of the Singular/Sage grid beyond
  BST 1999 Thm 2.2). Not yet run; recorded as an available check.

## Claim

```claim
id: bilu-tichy-classification-primary
statement: Bilu-Tichy 2000 (Acta Arith. 95, 261-288, Thm 1.1/10.5): f(x)=g(y)
  (f,g in Q[x]) has infinitely many rational solutions with bounded denominator
  iff f = phi∘f1∘lambda, g = phi∘g1∘mu with linear lambda,mu and (f1,g1) one of
  the five standard pairs over Q (first x^m vs ax^r p(x)^m; second x^2 vs
  (ax^2+b)p(x)^2; third Dickson pair (D_m(x,a^n),D_n(x,a^m)) with gcd(m,n)=1;
  fourth scaled Dickson pair with gcd(m,n)=2; fifth ((ax^2-1)^3, 3x^4-4x^3)).
  For K=Q with O_S=Z only these five kinds occur. The proof uses Siegel's theorem
  (ineffective) and gives no bound on the number of integral solutions. Genus
  formula Prop 4.1: 2g-2 = sum_gamma (mn - Omega(gamma)) - mn - gcd(m,n).
hypotheses: f,g nonconstant in Q[x]; the criteria quantify over rational
  solutions with a bounded denominator (for integral solutions, if f(x)-g(y) has
  no exceptional factor the number is finite via Siegel).
holds-here: yes — this is the primary classification behind HPT 2022's binomial
  application (C(x,k1)=C(y,k2) = the arithmetic-progression-products f with
  r=0,c=0,d=1); the infinite Singmaster family is the concrete standard-pair
  (first-kind-type / quadratic) example. The criterion is ineffective and gives
  no uniform-in-(k1,k2) count.
status: asserted-by-source (primary full text read; the five kinds and the two
  theorems quoted verbatim; not independently re-derived)
bearing: grounds the run's bilu-tichy approach file and the HPT application at
  the primary level; confirms the ineffective-uniformity wall; the genus formula
  is an available independent check for the run's genus grid.
anchor: research/sources/bilu-tichy-2000-fxgy.full.md
```