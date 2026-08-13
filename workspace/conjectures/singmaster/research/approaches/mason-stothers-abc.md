```approach
idea: Polynomial abc theorem (Mason-Stothers) applied to the binomial-coefficient
  identity as a functional equation. For the equal-products equation
  F(x) = G(y) with F(x) = C(x,k1) and G(y) = C(y,k2), consider the polynomial
  identity F(T) - G(T) = 0. When k1 ≠ k2, this has only finitely many solutions
  by the Mason-Stothers theorem on polynomial equations A+B=C with gcd(A,B,C)=1.
  The theorem gives a degree bound: max(deg A, deg B, deg C) ≤ N₀(ABC) - 1
  where N₀ is the number of distinct roots. This translates to a bound on the
  common solutions of F(x) = G(y) when x and y are interpreted as independent
  variables of a polynomial identity. The geometric content: if F(x) = G(y) has
  "too many" integer solutions, then F and G must share a compositional factor
  (the Bilu-Tichy exceptional pairs), and for the non-exceptional pairs the
  abc theorem forces the degree — hence k1,k2 — to be bounded.

mechanism: The Mason-Stothers theorem (1983; also Stothers 1981, Silverman 1984)
  states: If A,B,C ∈ ℂ[t] are relatively prime polynomials, not all constant,
  with A+B+C = 0, then max(deg A, deg B, deg C) ≤ N₀(ABC) - 1, where N₀(P)
  is the number of distinct roots of P.

  Apply this to the binomial equation. For C(x,k1) = C(y,k2), let:
    A(T) = (T)_{k1} · k2! = T(T-1)...(T-k1+1) · k2!
    B(T) = -(T)_{k2} · k1! = -T(T-1)...(T-k2+1) · k1!
    C(T) = A(T) + B(T)
  Then A(x)+B(y) = 0, but x and y are different variables. The Mason-Stothers
  theorem applies to a polynomial identity in ONE variable.

  The one-variable reformulation: if the equation C(x,k1) = C(y,k2) has
  infinitely many integer solutions (x,y), then by Siegel's theorem on curves,
  the curve must have genus 0 or 1, AND there must be a rational parametrization.
  In that case, there's a rational function φ(T) and integers a,b such that
  x = φ(T) + a, y = φ(T) + b on a dense set of T values, giving C(φ(T)+a, k1) =
  C(φ(T)+b, k2) as an identity in T. Apply Mason-Stothers to this identity to
  bound the degree of φ and hence k1,k2.

  This is essentially re-deriving the Bilu-Tichy classification via the abc
  theorem for polynomials. Zannier (1993, 2009) has shown that the polynomial
  abc theorem can replace Siegel's theorem in classifying polynomial pairs
  F(x)=G(y) with infinitely many integral points. The advantage: Mason-Stothers
  is elementary and gives EXPLICIT degree bounds, unlike Siegel's theorem.

  The concrete new claim: for non-exceptional pairs (k1,k2), the number of
  integer solutions to C(x,k1)=C(y,k2) is bounded by an explicit function of
  k1,k2. Combined with the genus result that all but (2,3),(2,4) have genus ≥2
  (Faltings gives finiteness but not a bound), the Mason-Stothers approach
  could give an EFFECTIVE bound per pair — not uniform, but computable.

  Actually, the deeper use: apply Mason-Stothers NOT to the equal-products
  equation but to the factorization of C(x,k) itself. C(x,k) = (x)_k/k! can
  be written as a product of k linear factors over ℂ. If C(x,k1)=C(y,k2)=a,
  then (x)_{k1}·k2! = (y)_{k2}·k1! = a·k1!k2!. So both sides factor completely
  into linear terms. Write each factorization and compare. The distinct roots of
  the combined product are at most k1 + k2 + (number of prime factors of a).

  The speculative leap: if a has r representations with column indices
  k_1,...,k_r, then for each pair of representations we have:
    (x_i)_{k_i}·k_j! = (x_j)_{k_j}·k_i!
  Taking the product over all pairs and applying Mason-Stothers-like degree
  comparisons might force r to be bounded in terms of the number of distinct
  linear factors involved — which is at most something like (max k_i)·r + ω(a).

status: proposed (speculative)
first-step: Verify that the Mason-Stothers theorem applies to the one-variable
  reduction of C(x,k1)=C(y,k2). Specifically: write the algebraic curve
  X(k1,k2): C(x,k1) = C(y,k2) as a polynomial equation in variables u=x,
  v=y. Compute its genus using the run's established formula
  g = ((k1-1)(k2-1)+1-gcd(k1,k2))/2. For genus 0 cases, find the rational
  parametrization and verify that Mason-Stothers bounds the degree. For
  genus ≥2, the Faltings finiteness is known (but ineffective); the question is
  whether Mason-Stothers can be applied to the function-field version
  (interpreting (x,y) as elements of the function field of the curve) to get
  an effective bound on the number of integral points. Check Zannier's "Some
  applications of Diophantine approximation to the study of polynomial
  equations" and the literature on effective Mordell via abc.
```
