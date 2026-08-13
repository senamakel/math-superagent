```approach
idea: Use the Aurifeuillean factorization 2^{2p}+1 = L_p·M_p together with
  quadratic reciprocity to prove that for all odd primes p in a specific
  congruence class, at least one prime divisor of L_p or M_p is ≡ 1 (mod 16),
  hence non-3-Higgs. This is an algebraic rather than analytic path to the
  divisor-level condition.
mechanism: The Aurifeuillean factors are L_p = 2^p − 2^{(p+1)/2} + 1 and
  M_p = 2^p + 2^{(p+1)/2} + 1. These satisfy M_p − L_p = 2^{(p+3)/2} and
  L_p·M_p = 2^{2p}+1. Rewriting: let x = 2^{(p+1)/2}; then L_p = x^2/2 − x + 1
  and M_p = x^2/2 + x + 1 (with x = 2^{(p+1)/2} ∈ Q(√2)). Equivalently,
  L_p and M_p are norms from Z[√−2] or related to the factorization of
  x^4 + 4 = (x^2 + 2x + 2)(x^2 − 2x + 2) when p ≡ 1 (mod 4) — the standard
  Aurifeuillean identity for 2^{4k+2}+1. For each residue class of p mod 16,
  the factors L_p, M_p have predictable quadratic character modulo small primes.
  The goal: find a modulus m (e.g., 16, 32, or a product of small primes) such
  that for all p in some congruence class, the Jacobi symbols force a prime
  divisor of L_p or M_p to be ≡ 1 (mod 16). This is the algebraic route to
  Conjecture 29's conclusion — using reciprocity on the specific quartic form
  rather than equidistribution of divisors. The mechanism is classical algebraic
  number theory: prime ideal factorization in the ring of integers of Q(ζ_8)
  or Q(√2, √−1) applied to the norm element 2^p ± 2^{(p+1)/2} + 1.
status: refuted
killed-by: Subsumed by the already-adopted biquadratic-character-divisors
  approach, which uses quartic (rather than quadratic) reciprocity in Z[i].
  Quadratic reciprocity (Legendre/Jacobi symbols) only controls the quadratic
  character mod small primes, which gives mod-8 or mod-16 constraints indirectly
  and at best a necessary condition. The v2(r−1) ≥ 4 condition — which is
  exactly "r is NOT 3-Higgs" — is a quartic condition: (2/r)_4 = 1 ⟺ r ≡ 1
  (mod 16) for r ≡ 1 (mod 8). Quadratic reciprocity cannot distinguish between
  r ≡ 1 (mod 8) and r ≡ 1 (mod 16); it can at best force r ≡ 1 (mod 8), which
  gives v2(r−1) ≥ 3 — still 3-Higgs. The biquadratic approach uses the richer
  structure of Z[i] where 2^{2p}+1 = (2^p+i)(2^p−i) factors, and quartic
  reciprocity directly computes (2/π)_4 for each Gaussian prime π, determining
  whether r ≡ 1 (mod 16). This approach would be a strict weakening of the
  adopted one, using a coarser invariant.
first-step: Derive the exact Aurifeuillean splitting for 2^{2p}+1 in terms of
  the residue class of p mod 8; compute L_p and M_p modulo 16 and modulo small
  primes for p ≡ 1,3,5,7 (mod 8); identify which residue classes give
  L_p ≡ 1 (mod 16) or M_p ≡ 1 (mod 16) unconditionally, or force a prime
  divisor ≡ 1 (mod 16) via Legendre-symbol constraints on the quartic form.
```