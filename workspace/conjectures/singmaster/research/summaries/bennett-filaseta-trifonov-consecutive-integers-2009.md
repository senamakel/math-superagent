# Bennett–Filaseta–Trifonov 2009 — "On the factorization of consecutive integers"

<!-- source: https://personal.math.ubc.ca/~bennett/BFTpaper0207.pdf | full text: research/sources/bennett-filaseta-trifonov-consecutive-integers-2009.full.md -->

M. A. Bennett, M. Filaseta, O. Trifonov, "On the factorization of consecutive
integers", J. reine angew. Math. (Crelle) 629 (2009) 171–200. Author preprint
(Feb 2007) on disk, 2120 lines. The work is the modern sharpening of Sylvester's
theorem and of Ecklund–Eggleton–Erdős–Selfridge 1978 (both cited and surveyed
in the introduction).

## What it establishes

**Theorem 1.1 (on disk, verbatim above):** If k ∈ {5,7}, n ≥ 2k is an integer,
and C(n,k) = U·V with P(U) ≤ k and V coprime to k! (equivalently: U has only
primes ≤ k, V has only primes > k), then V > U, EXCEPT precisely for

    (n,k) ∈ {(10,5), (12,5), (21,7), (28,5), (30,7), (54,7)}.

Here P(m) is the greatest prime factor, P(±1)=1. So for k ∈ {5,7} the
EEES "small-prime part U < large-prime part V" conjecture is settled
completely, with six explicit exceptions. (EEES 1978 had left k ∈ {3,5,7}
ineffective; this proves the two cases k=5,7, and the k=3 case remains open.)

**Theorem 1.2 / Theorem 10.1:** For x positive outside {1,2,3,8}, k,l,y
nonnegative with x²+Dx = 2^k·3^l·y (D ≤ 100, D coprime to 6, y coprime to 6),
the Diophantine structure of x²+x-type equations — bounding representations of
products of consecutive pairs by fixed small primes. The method: hypergeometric
Padé approximation (Ridout/Mahler-type), fractional parts of powers, and the
careful two-consecutive-integers case analysis going back to Størmer 1897.

**Section 2 generalities:** p-adic/Archimedean approximation lemmas (Thms 2.1–2.4)
that produce the exceptional-pair finiteness and bound `y < x^(λ−ε)` in the
x²+Dx = 2^k 3^l y family with explicit λ(p,q).

## Bearing for this run

This is the **effective, explicit** modern form of the Sylvester–Schur engine the
`zsigmondy-primitive-prime` thread stands on. For the Fibonacci family and any
value a with a representation at k=5 or k=7 (n ≥ 2k), the large-prime part V of
that C(n,k) strictly dominates the small-prime part U except for six known
pairs. That is a *structural* constraint on which primes must appear in a — the
kind of fact a proof that each representation needs its own prime factor of a
would use. Caveat: the theorem constrains the *split* of one C(n,k); it does not
by itself separate two different representations of the same a (two reps can
share their large primes). The k=3 case (EEES's remaining ineffective case) is
still open — that is the honest gap if this thread wants k=3 coverage.

```claim
id: bft-2009-prime-split-k57
statement: Bennett-Filaseta-Trifonov 2009 (Thm 1.1): for k in {5,7}, n >= 2k,
  write C(n,k) = U·V with P(U) <= k and V coprime to k!. Then V > U except
  exactly for (n,k) in {(10,5),(12,5),(21,7),(28,5),(30,7),(54,7)}. This
  settles the EEES 1978 conjecture for k=5,7; k=3 remains the ineffective case.
hypotheses: k in {5,7}; n >= 2k; U composed of primes <= k, V of primes > k.
holds-here: yes — applies to any representation C(n,k)=a with k in {5,7},
  n >= 2k, except the six listed pairs (check each against the witness set and
  the Fibonacci family: e.g. C(15,5)=3003 has n=15 >= 2k=10, so U<V holds
  for it; C(14,6) is k=6, outside this theorem's scope).
status: sourced (author PDF on disk; Thm 1.1 quoted verbatim; the six exceptions
  are on disk)
bearing: effective explicit control of the small/large prime split for k=5,7; a
  concrete improvement over EEES 1978 for the zsigmondy/block threads; k=3 gap
  is the remaining open EEES case.
anchor: research/summaries/bennett-filaseta-trifonov-consecutive-integers-2009.md
```

```claim
id: bft-2009-x2dx-small-prime-reps
statement: Bennett-Filaseta-Trifonov 2009 (Thm 1.2/10.1): for x positive,
  x not in {1,2,3,8}, and D <= 100 coprime to 6, the equation
  x^2 + Dx = 2^k 3^l y (y coprime to 6, k,l >= 0) has its solutions bounded
  via hypergeometric Padé: y > x^(lambda−eps) for x large with explicit lambda.
hypotheses: D <= 100, D coprime to 6; y coprime to 6; x positive outside the
  four excluded values.
holds-here: adjacent — the k=2 column (triangular numbers C(x+1,2)) is the
  D=1 case x(x+1) = 2·y with y a binomial; the theorem's structure is the
  effective method the k=2 column would need. Not directly Singmaster — the
  binomial on both sides makes the small-prime set vary.
status: sourced (author PDF on disk; statements quoted in digest)
bearing: the effective Padé technique for products of two consecutive integers
  with restricted prime factors — a tool the k=2-column attack could reuse
  (Tian's conjecture line; also see Chan 2024 equal-products, held).
anchor: research/summaries/bennett-filaseta-trifonov-consecutive-integers-2009.md
```