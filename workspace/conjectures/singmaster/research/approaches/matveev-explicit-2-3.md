```approach
idea: Apply Matveev 2000 Theorem 2.3 (the rational/integer logarithmic case,
  K=Q, D=ρ=1) to the curve C(x,2)=C(y,3), computing the explicit constants
  numerically to obtain an effective bound on max(x,y) for this specific pair.
  This is the concrete per-pair deliverable that `effective-methods-wall`
  identified as the honest surviving task: an effective bound with a computed
  constant, stated with its k-dependence.

mechanism: C(x,2) = C(y,3) is a genus-1 elliptic curve. The standard approach
  (Stroeker–de Weger 1999, David's elliptic logarithms) gives an effective
  bound via the elliptic-logarithm method. But Matveev 2000 provides an
  alternative route through ordinary (non-elliptic) logarithms: the equation
  x(x-1)/2 = y(y-1)(y-2)/6 can be rewritten as 3x(x-1) = y(y-1)(y-2), which
  after completing the square in x gives (2x-1)^2 = 1 + (4/3) y(y-1)(y-2).
  This is NOT a pure elliptic-curve reduction — the cube on the RHS introduces
  algebraic numbers. Alternatively, the equal-products form
  6·x(x-1) = 2·y(y-1)(y-2) can be treated as a linear form in three logarithms
  of algebraic numbers by taking logs of both sides and using the fact that
  all factors are rational integers. Specifically, for a solution (x,y) with
  C(x,2)=C(y,3)=a, write a = 3x(x-1) = y(y-1)(y-2). Then for distinct primes
  p dividing the factors, we get a linear form in logarithms of primes.

  The Matveev 2000 route (Thm 2.3, K=Q):
  Let α₁,...,αₙ be positive rational numbers (the prime factors involved).
  Let b₁,...,bₙ be integers (the exponents). Then Λ = b₁ln α₁ + ... + bₙln αₙ.
  If Λ ≠ 0, then |Λ| > exp(−C(n)·D²·∏Aⱼ·log(2eB)) where
  C(n) = 112·2ⁿ(C₂ C′₀) with C₂,C′₀,C₁,D,Ω as defined in the theorem.
  For K=Q, D=ρ=1, and the 2ⁿ improvement of Thm 2.3 applies (no Kummer
  condition needed — the theorem is for prime factors, which are rational).

  The computation steps:
  1. Reduce C(x,2)=C(y,3) to a system of equations: 3x(x-1) = y(y-1)(y-2).
  2. Parametrise solutions where the RHS is large via the prime factorisation
     of the three consecutive integers y, y-1, y-2 (they are pairwise coprime
     or share only small gcds).
  3. Set up a linear form Λ in logarithms of the primes involved, using
     Baker's method: write the equation as a product identity and take logs.
  4. Apply Matveev 2000 Thm 2.3 to get a lower bound on |Λ|.
  5. Get an upper bound on |Λ| from the equation itself (standard, using that
     the three factors y, y-1, y-2 are close).
  6. Combine to get an absolute bound on y, then compute the bound numerically.

  The resulting bound will be enormous (like the Stroeker–de Weger M₀ ≈ 10⁴⁰)
  but it is EXPLICIT and COMPUTED — exactly the GOAL-eligible deliverable.

status: adopted
precedent:
  https://www.mathnet.ru/eng/im190 (Matveev 2000, Thm 2.3 for K=Q, held)
  https://www.ams.org/journals/mcom/1999-68-227/ (Stroeker–de Weger 1999, held:
    the elliptic-logarithm solution of (2,3); our Matveev computation is an
    independent verification route)
  effective-methods-wall (this run's grounded impossibility, which this
    computation confirms by exhibiting the constant's k-dependence)
claims: matveev-2000-explicit-constants-primary, deweger-smallk-effective
first-step: Factor the (2,3) equation: 6C(x,2) = 2C(y,3) ⇒ 3x(x-1) = y(y-1)(y-2).
  Parametrise: the three consecutive integers y-2, y-1, y are pairwise coprime
  up to gcd 1 or 2. Write y = a·u², y-1 = b·v² (or similar, depending on which
  factor carries which primes). Set up the linear form in three logarithms:
  ln y + ln(y-1) + ln(y-2) - ln 3 - ln x - ln(x-1) = 0.
  Actually better: use the known reduction of C(x,2)=C(y,3) to the elliptic
  curve Y²+Y=X³−9X+20 (Stroeker–de Weger Table 1). Then the Matveev computation
  is for the linear form in elliptic logarithms, BUT we want the ordinary-
  logarithm route. The simplest concrete target: take the equal-products form
  (2,3): 3·x(x-1) = y(y-1)(y-2). Let p₁,...,pᵣ be the prime factors of all
  six integers. Then taking logs gives a linear relation Σbᵢ ln pᵢ = 0 with
  the bᵢ being the net exponents. Apply Matveev Thm 2.3 with n = r (number of
  distinct primes). Compute Aⱼ = max{h(αⱼ), |ln αⱼ|} for each prime αⱼ = pⱼ
  (since primes are rational, h(pⱼ) = ln pⱼ). Compute B = max|bⱼ| (the
  maximum exponent). Evaluate the Matveev constants C₂, C′₀ numerically for
  n = r. Get the bound on max(x,y). This is a finite computation using the
  explicit constants from the held Matveev paper.
```