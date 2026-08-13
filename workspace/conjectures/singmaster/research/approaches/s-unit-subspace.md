```approach
idea: S-unit equations via the Schmidt Subspace Theorem — bound N(a) for each
  fixed a by noting that all representations (n,k) with C(n,k)=a give S-integers
  n that are solutions of the unit equation n(n-1)...(n-k+1) = a·k! over a
  common set of primes S. The Evertse–Schlickewei–Schmidt bound on the number of
  solutions to S-unit equations depends only on |S| and the number of terms,
  not on the magnitudes — giving a bound on N(a) that is independent of a, up to
  the dependence of |S| on a.

mechanism: [CORRECTED after grounding] The invented file's self-doubt about
  whether the factors are S-units is resolved AFFIRMATIVELY. From C(n,k)=a:
      n(n-1)...(n-k+1) = a·k!
  so every prime p dividing any factor (n-j), 0<=j<k, divides a·k!, hence
  p ∈ S := {primes | a} ∪ {primes <= k} ⊆ {primes | a} ∪ {primes <= log2 a}
  (last inclusion since C(n,k) >= C(2k,k) >= 2^k forces k <= log2(a) for any
  representation). Hence each factor n-j is an S-unit of this common S, and
  |S| <= omega(a) + pi(log2 a). The S-set construction is sound.

  The S-unit/Subspace machinery is real: Evertse 1984 (Invent. Math. 75,
  561-584) and van der Poorten–Schlickewei, with the quantitative form
  Schlickewei 1990 (J. reine angew. Math. 406, 109-120), the best count bound
  being Evertse's (2^35 n^2)^{n^3 s} for the S-unit equation a1 x1 + ... + an xn
  = 1 with |S| = s (as quoted in Mueller, BLMS 32 (2000), doi 10.1112/
  S002460939900675X); the uniform-in-rank refinement is Evertse–Schlickewei–
  Schmidt, Annals of Math. 155 (2002) 807-836 ("linear equations in variables
  which lie in a multiplicative group": number of non-degenerate solutions is
  bounded by a function of the dimension n and the rank r alone). The closest
  published equal-values application is Evertse–Győry–Shorey–Tijdeman 1987
  (Acta Arith. 48, 379-396, doi 10.4064/aa-48-4-379-396), which bounds equal
  values of binary forms by S-unit reduction with constants depending on the
  FORM.

  Why it still cannot give a uniform bound:
  (1) |S| = omega(a)+pi(log2 a) is UNBOUNDED in a (take a a primorial:
      omega(a) ~ log a / log log a), and every S-unit count bound grows
      (exponentially) with s=|S| and the rank r=|S|-1. So the route yields at
      best N(a) <= f(omega(a)+log2 a) with f exponential in its argument — an
      upper bound growing with a, NOT a constant; it does not even reproduce
      Singmaster's O(log a).
  (2) N(a) is a sum over ~log2 a columns: for each k the equation C(n,k)=a is a
      degree-k polynomial in n with <= k+1 integer roots, giving the trivial
      N(a) <= O((log2 a)^2); the S-unit structure does not couple the columns,
      and the ESS theorem counts solutions of ONE fixed equation (with a fixed
      coefficient tuple and fixed n), not a varying-k family.
  (3) The per-pair S-unit reduction of the equal-products equation is exactly
      the work already in this library: Saradha–Shorey–Tijdeman 1995 Thm 2
      (effective but non-uniform, constant depends on d1,d2,L/M — claim
      sst-effective-shared-factor) and Beukers–Shorey–Tijdeman 1999 Thm 1.1
      (ineffective via Siegel for gcd(m,n)=1 — claim
      bst-fixed-kl-ineffective-primary). The subspace theorem's counting bound
      is non-constructive (it gives finiteness/count without a usable
      enumeration or size bound), so it contains the same ineffectivity wall as
      Siegel/Faltings.
  No published application of the Subspace Theorem to bounding N(a) exists;
  several searches (S-unit + Singmaster, subspace theorem + equal binomial
  coefficients, equal products of consecutive integers + subspace theorem)
  surface only the equal-values-of-binary-forms work (EGST 1987) and the
  general S-unit machinery, none of which yields a uniform-in-a bound.

status: refuted
killed-by: |S| = omega(a)+pi(log2 a) is unbounded in a, so the S-unit count
  bound N(a) <= f(|S|) grows with a and is not a constant; the per-pair
  reduction duplicates SST 1995 Thm 2 / BST 1999 Thm 1.1 (sst-effective-shared-
  factor, bst-fixed-kl-ineffective-primary), which are already in the library
  and are non-uniform / ineffective; the ESS counting theorem concerns a single
  fixed equation and does not couple the ~log2 a columns that N(a) sums over.
precedent:
  https://doi.org/10.4007/annals.2002.155.807 (Evertse–Schlickewei–Schmidt,
    Annals 155 (2002) 807-836: bound on non-degenerate solutions of
    a1 x1 + ... + an xn = 1 in a rank-r multiplicative group, in terms of
    dimension and rank only)
  https://doi.org/10.1007/BF01388637 (Evertse 1984, Invent. Math. 75, 561-584:
    equations in S-units and Thue–Mahler)
  https://doi.org/10.1515/crll.1990.406.109 (Schlickewei 1990, J. reine angew.
    Math. 406, 109-120: explicit upper bound for the number of S-unit solutions)
  https://doi.org/10.1112/S002460939900675X (Mueller 2000, BLMS 32: states
    Evertse's best bound (2^35 n^2)^{n^3 s}, s=|S|; function-field S-units via
    the abc-theorem)
  https://doi.org/10.4064/aa-48-4-379-396 (Evertse–Győry–Shorey–Tijdeman 1987,
    Acta Arith. 48, 379-396: equal values of binary forms — the closest
    published equal-values application, per-form constants)
  claims: sst-effective-shared-factor, bst-fixed-kl-ineffective-primary,
    bst-fixed-kl-ineffective, bilu-tichy-method-ineffective-uniformity-wall
first-step: none — the mechanism is structurally sound but its output is a
  function of omega(a)+pi(log2 a), unbounded in a, so it is refuted as a route
  to the conjectured constant. It would also fail to reproduce the known
  O(log a) bound (f(|S|) is exponential in |S|, far larger than log a). Do not
  re-propose unless a way to bound s = omega(a)+pi(log2 a) uniformly is found —
  which is exactly the content of the conjecture.
```