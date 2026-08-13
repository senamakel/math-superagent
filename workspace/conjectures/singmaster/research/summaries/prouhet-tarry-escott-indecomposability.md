# Hajdu–Papp–Tijdeman 2022 — PTE, indecomposability, and binomial-coefficient Diophantine equations

Source: L. Hajdu, Á. Papp, R. Tijdeman, "The Prouhet–Tarry–Escott problem,
indecomposability of polynomials and Diophantine equations", Ramanujan J. 58 (2022)
1075–1093. Full text: `research/sources/prouhet-tarry-escott-indecomposability.full.md`.

This is the **Bilu–Tichy grounding source** for the run's binomial-equation approach
(motivated by Benne de Weger's question on equal/differing binomial coefficients).

## What it establishes

- **Theorem 2.1 (PTE structure).** For `n > 2r^{3/2}+5r+8`, any partition of
  `{1,…,n}` into `A_0` (|A_0|=r) and equal-size sets `A_i` whose first `k−1`
  symmetric polynomials agree must have `k=2`, and the `A_i` are symmetric about
  the mean of the remaining set. Corollary 3.1: the only `k>2` solution to
  Problem 1 is `n=7` (sets `{2,3,7}` and `{1,5,6}`).

- **Theorem 2.2 (PTE ⇔ decomposability).** Such a partition exists iff
  `f_A(x)=∏_{a∈A}(x−a)` is decomposable over Q; the decomposition is explicit.

- **Corollary 2.1 (binomial case).** `f_{A,c,d}(x)=∏_{a∈A}(x−c−ad)` is decomposable
  over Q iff `n−r` is even and `A` is symmetric about its mean; the only (up to
  equivalence) decomposition is then the quadratic one.

- **Theorem 2.3 (classifies infinite families — INEFFECTIVE).** `f_{A,c,d}(x)=P(y)`,
  deg P≥2, has finitely many integer solutions unless (i) `P(y)=f_{A,c,d}(T(y))` for
  a non-constant rational T, or (ii) `P(y)=φ*(Q(y))` with Q having at most two roots
  of odd multiplicity. **Acknowledged ineffective** ("This result, similarly to the
  above mentioned ones, is ineffective").

- **Theorem 2.4 (EFFECTIVE, different equation).** `f_{A,c,d}(x)=ay^ℓ+b` with ℓ
  unknown ≥2 has all `x,y,ℓ` effectively bounded by a constant depending on the data.
  Proof uses Schinzel–Tijdeman (ℓ<C₁ via linear forms in logs), Brindza, and Lemma 5.4
  (Bilu–Tichy criterion: `f(x)=g(y)` infinite bounded-denominator solutions iff
  `f=φ∘F∘λ`, `g=φ∘G∘κ` with (F,G) a standard pair).

## What follows for this run

- The binomial collision `C(x,k1)=C(y,k2)` is the `r=0, c=0, d=1` special case of
  `f_{A,c,d}(x)=P(y)` (binomial polynomials have roots an arithmetic progression).
  So **the Bilu–Tichy classification has been applied to this exact problem** and
  determines which `(k1,k2)` are exceptional.
- Theorem 2.3's finiteness is **ineffective** — it gives "finitely many" with no count
  computable in `(k1,k2)`. The effective result (Thm 2.4) is for **shifted power
  values**, not equal binomials. So this route yields per-pair finiteness only, the
  same ineffectivity wall as Faltings/Siegel — **not a uniform bound on N(a)**.
- The surviving grounded kernel is the **classification of exceptional pairs**: the
  infinite Singmaster Fibonacci family `C(n+1,k+1)=C(n,k+2)` is the concrete
  exceptional example (its common factor comes from the Pell/quadratic structure).

Evidence class: sourced (full text read). Records the named obstruction that refutes
`bilu-tichy-classification` as a route to uniformity.

Claim block: `hpt-bilu-tichy-exceptional-classification` and
`bilu-tichy-method-ineffective-uniformity-wall` are held in
`research/notes/bilu-tichy-grounding.md` (the approach-level note).
