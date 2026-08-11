# Closed forms for A_n, B_n — derivation (this run, 18 Sep 2025)

This file records the derivation of exact closed forms for A_n and B_n in

    f_n(k) = #{(pi,i) : 0 <= i < n!, (pi^i)(k) < (pi^i)(0)} = A_n + (k-1) B_n

(the gap function whose values the whole PE 903 reduction needs), and the
efficient O(n) modular evaluation of Q(n) mod p for n = 10^6.

## 1. Symbol definitions

- pi, sigma, tau: permutations of {0,...,n-1} in one-line notation; pi^i the
  i-th iterate, pi^0 = identity.
- rank: 1-based lexicographic position (factoradic: rank(tau) = 1 +
  sum_{j=0}^{n-2} a_j(tau)*(n-1-j)! with a_j(tau) = #{m>j : tau(m) < tau(j)}).
- ord(pi) = lcm of its cycle lengths; <pi> = {pi^t : t in Z_ord}.
- f_n(k) = #{(pi,i) : 0<=i<n!, (pi^i)(k) < (pi^i)(0)}.
- Established (verified n=2..11, all gaps): f_n(k) = A_n + (k-1) B_n,
  A_n = f_n(1), B_n = f_n(2)-f_n(1).
- Established central reduction (verify_red.py, exact for n=2..8; Q(10) mod p
  = 468421536 reproduced):
      Q(n) = (n!)^2 + A_n (n! - 1) + (B_n / 2) * T(n),
      T(n) = sum_{m=1}^{n-1} m (m-1) m!.

## 2. The sigma-measure decomposition (eliminates the cyclic subgroup sum)

For each pi the map i -> pi^i visits each element of <pi> exactly n!/ord(pi)
times (ord(pi) | lcm(1..n) | n!).  Hence for any statistic g:

    sum_{i=0}^{n!-1} g(pi^i) = (n!/ord(pi)) * sum_{sigma in <pi>} g(sigma).

Define the (not normalized) measure on S_n:
    N(sigma) = #{ (pi,i) : 0 <= i < n!, pi^i = sigma }
             = sum_{pi : sigma in <pi>} n!/ord(pi).
Then sum_sigma N(sigma) = (n!)^2 and, for our statistic:

    f_n(k) = sum_pi (n!/ord pi) * #{sigma in <pi> : sigma(k) < sigma(0)}
           = sum_sigma N(sigma) * [sigma(k) < sigma(0)].

KEY FACT: N(sigma) is a class function of sigma (if sigma' = rho sigma rho^{-1}
then the preimages pi' = rho pi rho^{-1} are in bijection and ord is preserved).
So with mu(sigma) = N(sigma)/(n!)^2 a probability measure on S_n:

    f_n(k)/(n!)^2 = E_mu[ [sigma(k) < sigma(0)] ].

## 3. Campion-Loth et al Lemma 4.7 (arXiv:2301.00898) — per-class affine form

For a conjugacy class C_lambda of cycle type lambda with a_1 = #fixed points,
a_2 = #2-cycles, for any pair i < j:

    Pr_{sigma in C_lambda}[ sigma(i) > sigma(j) ] =
        1/2  +  a_2/(n(n-1))  -  a_1(a_1-1)/(2 n (n-1))
             +  (j-i-1) * [ n - n a_1 - a_1 + a_1^2 - 2 a_2 ]
                          / [ n (n-1) (n-2) ].

(Exact finite-n statement; needs n >= 3 for the last denominator.  This is the
source that will be verified directly by enumeration in
closedform_exact.py before anything is built on it.)

With i=0, j=k: [sigma(k) < sigma(0)] = [sigma(0) > sigma(k)], so

    f_n(k)/(n!)^2 = E_mu[ Pr_lambda[I_{0,k}] ]
        = 1/2 + E_mu[a_2]/(n(n-1)) - E_mu[a_1(a_1-1)]/(2 n (n-1))
          + (k-1) * [ n - (n+1) E_mu[a_1] + E_mu[a_1^2] - 2 E_mu[a_2] ]
                   / [ n (n-1) (n-2) ]

by linearity — this PROVES f_n is affine in k (hence the observed
arithmetic property) and reduces everything to three mu-moments.

## 4. The three exact mu-moments (proved combinatorially)

(mu-normalization: E_mu[g] = sum_sigma N(sigma) g(sigma) / (n!)^2.)

(a) E_mu[a_1] = H_n = sum_{m=1}^n 1/m.
    Proof: sum_{sigma} N(sigma) a_1(sigma)
        = sum_pi (n!/ord pi) sum_{i mod ord} #{x : pi^i(x)=x}
        = sum_pi (n!/ord pi) sum_x ord(pi)/L_x(pi)      (L_x = cycle length of x)
        = sum_pi n! * (#cycles of pi)  =  n! * n! * E_uniform[#cycles]
        = (n!)^2 H_n.

(b) E_mu[a_2] = (1/4) H_{floor(n/2)}.
    Proof: a_2(pi^i) counts 2-cycles of pi^i.  A cycle of even length L of pi
    splits into 2-cycles under pi^i iff gcd(L,i) = L/2, which holds for exactly
    ord(pi)/L values of i mod ord(pi), contributing L/2 two-cycles each.  So
        sum_{i mod ord} a_2(pi^i) = sum_{even cycles C} (ord/L_C)(L_C/2)
                                  = (ord/2) * (#even cycles of pi).
    Therefore E_mu[a_2] = (1/2) E_uniform[#even cycles]
        = (1/2) sum_{m=1}^{floor(n/2)} 1/(2m)  =  (1/4) H_{floor(n/2)}.

(c) E_mu[a_1^2] = n + S(n),  S(n) = sum_{a=1}^{n-1} sum_{b=1}^{n-a} 1/lcm(a,b).
    Proof sketch: a_1(pi^i)^2 = sum_{x,y} [pi^i(x)=x][pi^i(y)=y].
    For x = y: ord/L_x; for x,y in one cycle of length L: ord/L; for x,y in
    different cycles of lengths L_x, L_y: ord/lcm(L_x,L_y).  Summing over i:
        sum_i a_1(pi^i)^2 = ord * [ sum_C |C| + sum_{(x,y) ordered, diff cycles}
                                                        1/lcm(L_x,L_y) ]
        = ord * [ n + sum_{(x,y) diff} 1/lcm ].
    For a fixed ordered pair (x,y), #{pi : x in a-cycle, y in b-cycle,
    different} = (n-2)! for each (a,b) with a+b <= n, hence
        E_mu[a_1^2] = n + sum_{a+b<=n} 1/lcm(a,b).

SAFETY: all three identities are cross-checked in closedform_exact.py by direct
orbit summation over all pi for n = 3..9 (exact Fractions), and the composite
f_n(k) rows are compared with the oracle-verified rows in out/extend_f.json.

## 5. Closed-form summary

For n >= 3 (n = 2 special: A_2 = 1, B_2 = 0):

    E1 := H_n
    E2 := (1/4) * H_{floor(n/2)}
    E11 := n + S(n),   S(n) = sum_{a+b<=n} 1/lcm(a,b)

    A_n/(n!)^2 = 1/2 + E2/(n(n-1)) - (E11 - E1)/(2 n (n-1))
    B_n/(n!)^2 = [ n - (n+1) E1 + E11 - 2 E2 ] / (n (n-1) (n-2))

## 6. Efficient evaluation of S(n) (the only non-trivial sum)

Use the standard 1/lcm(a,b) = gcd(a,b)/(ab) and gcd(a,b) = sum_{d|a, d|b} phi(d):

    S(n) = sum_{a+b<=n} gcd(a,b)/(ab)
         = sum_{d=1}^{floor(n/2)} phi(d)/d^2 * T(floor(n/d)),
    T(m) = sum_{a=1}^{m-1} sum_{b=1}^{m-a} 1/(ab)
         = 2 * sum_{s=2}^{m} H_{s-1}/s      (since 1/(a(s-a)) = (1/s)(1/a + 1/(s-a)))

T is computed for all m by the O(n) recurrence T(m) = T(m-1) + 2 H_{m-1}/m.
phi by a linear sieve up to n/2.  Total: O(n) time, O(n) space; at n = 10^6
this is trivial, and all denominators are < p so every fraction is invertible
mod p = 10^9+7.

FINAL FORMULA (mod p, all divisions via modular inverse; n = 10^6 < p):

    Q(n) = (n!)^2 + A_n (n! - 1) + (B_n/2) T(n)   mod p.

## 7. Program list and check matrix (built and run by tool_builder)

1. closedform_exact.py — exact Fraction implementation:
   - verify Lemma 4.7 formula by direct per-class enumeration for n=4,5,6,7
     (all classes, all gaps k): formula == counted probability;
   - verify the three mu-moments by direct orbit summation n=3..9;
   - rows f_n(k) from the closed forms == out/extend_f.json exactly for
     n=2..11 (big-int equality, all gaps);
   - Q(n) from the closed-form A_n, B_n == known Q values (2..8 brute),
     Q(9), Q(10), Q(11) from the verified reduction applied to extend_f rows;
   - Q(10) mod p == 468421536 (statement oracle).
2. solution103.py — modular implementation:
   - linear inverse sieve inv[1..n], H[1..n], phi[1..n/2], T recurrence;
   - S(n) mod p via the phi-decomposition;
   - A, B mod p from the closed forms; n!, T(n) in the loop; Q(n) mod p;
   - self-test n=2..11 (mod p) against the exact values; Q(10) oracle;
   - cross-checks: S direct O(n^2) pair-sum vs phi-method mod p at
     n = 10^4 and n = 5*10^4; exact-rational phi-evaluation vs modular at
     n = 2000 and n = 5000; second accumulation route
     Q = (n!)^2 + sum_{w=1}^{n-1} w! (w A + w(w-1) B/2) mod p at n = 10^6
     must agree with the telescoped route;
   - final: print Q(10^6) mod (10^9+7).

Nothing here is a search over the answer space: every formula is exact and
each program is a direct transcription of the identities above, validated
against every brute-force oracle the workspace possesses.