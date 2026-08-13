# Archimedean Baker bound via the sum-of-reciprocals identity

```approach
idea: Transform the product identity Π(1+1/p_i^{e_i}) = 2^{a+1}/(2^a+1) into
  a sum-of-reciprocals Diophantine approximation: Σ 1/p_i^{e_i} + higher-order
  terms = log 2 + O(2^{-a}). The sum Σ 1/p_i^{e_i} is a rational number with
  denominator dividing the odd part m. The approximation error ~2^{-a} is
  extraordinarily small relative to the size of the denominators involved.
  Apply Baker's theorem on linear forms in (real, Archimedean) logarithms
  to bound m from below in terms of a, then combine with the 2-adic budget
  ω ≤ a+1 and m's multiplicative structure to force a contradiction unless
  a is bounded — yielding finiteness by Subbarao–Warren's theorem for fixed ω.

mechanism: Start from the exact balance:

    Π_{i=1}^ω (1 + 1/p_i^{e_i}) = 2^{a+1}/(2^a+1) = 2 · (1 - 1/(2^a+1))

  Take natural logarithms (real, Archimedean):

    Σ log(1 + 1/p_i^{e_i}) = log 2 + log(1 - 1/(2^a+1))

  Expand: log(1+x) = x - x^2/2 + x^3/3 - ... for |x| < 1:

    Σ [1/p_i^{e_i} - 1/(2p_i^{2e_i}) + 1/(3p_i^{3e_i}) - ...] = log 2 + ε

  where ε = log(1 - 1/(2^a+1)) = -1/(2^a+1) + O(4^{-a}).

  Rearranging, the rational sum S = Σ 1/p_i^{e_i} satisfies:

    |S - log 2| ≤ Σ 1/(2p_i^{2e_i}) + |ε| < Σ 1/(2·3^{2e_i}) + 2^{-a}

  For p_i ≥ 3 and e_i ≥ 1, Σ 1/(2p_i^{2e_i}) ≤ ω/(2·9). With ω ≤ a+1,
  this is at most (a+1)/18. But the key is that |S - log 2| is O(2^{-a})
  for large a, which is exponentially small.

  Now S = A/B where B | m = Π p_i^{e_i}. All p_i are 3-Higgs primes (for a
  sixth example), and m is Higgs-cubefree in the sense that each prime
  appears with exponent at most 3 (Graham + Maciejewski). So B is a product
  of 3-Higgs primes with exponents at most 3ω.

  Apply Baker's theorem (Baker–Wüstholz 1993, or Matveev 2000 for explicit
  constants): for rational numbers α_i = 1/p_i^{e_i} and α_0 = log 2,
  the linear form Λ = Σ α_i log 1 - log 2 (with log 1 = 0, so Λ = -log 2 +
  Σ 1/p_i^{e_i} + remainder) satisfies:

    |Λ| > exp(-C(ω) · Π log H(α_i))

  where H(α_i) is the height of each rational. Since Λ ~ 2^{-a}, we get:

    2^{-a} > exp(-C(ω) · Σ log p_i^{e_i}) = exp(-C(ω) · log m)

  so a < C(ω) · log m, i.e., m > exp(a/C(ω)).

  But m is built from at most ω primes, each ≤ something. If we can also
  bound m from above in terms of a (from the structure of 3-Higgs primes),
  we obtain a contradiction for large a.

  The upper bound: if all p_i are 3-Higgs, then each p_i lies in the thin
  set P_3, and m = Π p_i^{e_i} with e_i ≤ 3. From Ford's bound on P_3,
  the k-th 3-Higgs prime p_k satisfies p_k ≥ something like k^{1+δ}.
  With ω ≤ a+1, we get log m ≤ 3·ω·log(p_ω). If p_ω grows at least like
  ω(log ω), then log m ≤ 3ω(log ω + O(1)) ≤ 3(a+1)(log(a+1) + O(1)).

  Combining with the lower bound m > exp(a/C) gives:

    exp(a/C) < exp(3(a+1) log(a+1))

  i.e., a/C < 3(a+1) log(a+1), which holds for all a. So there is no
  contradiction — the bounds are on the same scale.

  **The sharper version**: instead of Baker in the real setting, use Baker
  on the *rational approximation* S = A/B ≈ log 2 directly. Then:

    |A/B - log 2| > B^{-C}

  for some effective C (this is weaker than the full Baker bound but
  sufficient for Diophantine approximation). With |A/B - log 2| ~ 2^{-a},
  we get 2^{-a} > B^{-C}, i.e., B > 2^{a/C}. Since B | m, m > 2^{a/C}.

  Meanwhile, B divides m, and m's log is at most Σ e_i log p_i ≤ 3 ω log
  p_max. If p_max (the largest odd prime in the UP) is bounded by something
  like 2^{O(a)} (from the growth of the 3-Higgs primes at index ω ≤ a+1),
  then this approach does not close on its own.

  **The key refinement**: use the fact that the approximation is not just
  to log 2 but to a specific rational 2^{a+1}/(2^a+1), whose product
  structure is fully known. The linear form

    Λ = Σ log(p_i^{e_i} + 1) + log(2^a+1) - (a+1)log 2 - Σ log p_i^{e_i}

  is exactly zero (this is the balance). Applying Baker to this homogeneous
  linear form in logarithms of integers gives:

    0 = |Λ| > exp(-C(ω+2) · Π log H_j)

  which is impossible UNLESS one of the integer arguments is 1 (i.e., some
  factor is trivial). Since all arguments are ≥ 3 (p_i^{e_i} ≥ 3, p_i^{e_i}+1 ≥ 4,
  2^a+1 ≥ 3), Baker's theorem says |Λ| > exp(-C · (log 3)^{ω+2}), which
  contradicts Λ = 0. This is **exactly** the standard Baker-style proof that
  certain exponential Diophantine equations have finitely many solutions —
  but here the equation is multiplicative, and Baker's theorem in the form
  above applies to LINEAR forms Σ α_i log β_i = 0, not to the product form
  directly.

  **This is why the approach needs the reformulation as an additive
  Diophantine approximation**: the multiplicative balance becomes an
  additive approximation after taking logarithms, and the error term is
  controlled by 2^{-a}. This distinguishes it from both the algebraic
  (quartic reciprocity) and combinatorial (Pratt-tree) approaches.

status: proposed
first-step: (1) Write the exact additive form: expand log Π(1+1/p_i^{e_i}) =
  log(2^{a+1}/(2^a+1)) as Σ log(1+1/p_i^{e_i}) = log 2 + log(1-1/(2^a+1)),
  then expand each log(1+x) to get S = Σ 1/p_i^{e_i} with explicit error
  bounds in terms of p_i and e_i. (2) Compute S exactly for the five known
  UPNs and verify that the error matches the predicted O(2^{-a}) bound.
  (3) Apply Matveev's explicit Baker bound (2000, Izv. Math.) to the linear
  form Λ = log 2 - S, using the heights H(p_i^{e_i}) = p_i^{e_i} and the
  bound on ω, to obtain an explicit inequality relating a and m, and determine
  whether this forces a < some absolute bound.
```