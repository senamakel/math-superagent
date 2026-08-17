# Ecklund–Eggleton–Erdős–Selfridge 1978 — "On the prime factorization of binomial coefficients"

<!-- source: https://doi.org/10.1017/s1446788700011770 | full text: research/sources/ecklund-eggleton-erdos-selfridge-prime-factorization-1978.full.md -->

Earl F. Ecklund Jr, Roger B. Eggleton, Paul Erdős, J. L. Selfridge, "On the
prime factorization of binomial coefficients", J. Austral. Math. Soc. (Series A)
26(3) (1978) 257–269.

**Hold status: PARTIAL.** The file on disk is the Cambridge Core landing page:
abstract, author affiliations, and full reference list. The paper body and the
explicit lists of the 12/19 exceptional cases are paywalled (Cambridge Core
"Save PDF" only). What is on disk is therefore the *statement* of the theorems
and the complete bibliography — which is itself load-bearing, since it is the
canonical citation chain for the Sylvester–Schur line this run's block-approach
threads stand on.

## What it states (abstract, on disk verbatim)

For positive integers n and k with n ≥ 2k, write

  C(n,k) = u·v,  every prime factor of u is < k,  every prime factor of v is ≥ k.

It is shown that u < v holds with just 12 exceptions, which are determined.
If the partition is U·V with primes of U ≤ k and primes of V > k, then U < V
holds with at most finitely many exceptions, 19 of which are determined;
conjectured that there are no others. Building on Størmer's finiteness result
for runs of consecutive integers with no prime factor > k, and on
Sylvester/Schur/Erdős.

## Reference chain it exposes (the bibliography on disk)

- Sylvester 1892, "On arithmetical series", Messenger Math. 21, 1–19, 87–120.
- Schur 1929, "Einige Sätze über Primzahlen ...", S.B. Deutsch. Akad. Wiss.
  Berlin 23, 1–24.
- Erdős 1934, "A theorem of Sylvester and Schur", J. London Math. Soc. 9,
  282–288.
- Størmer 1897, "Quelques théorèmes sur l'équation de Pell x²−Dy² = ±1 ...",
  Videnskabs-Selskabets Skrifter, Christiania 2, 48 pp.
- Lehmer 1964, "On a problem of Størmer", Illinois J. Math. 8, 57–79.
- Mahler 1961, Lectures on Diophantine Approximations I (Notre Dame), Thm (5,II)
  p. 159 — identified in the paper as "the most accessible reference" for the
  Størmer finiteness route.
- Ecklund–Eggleton 1972, "Prime factors of consecutive integers", AMM 79,
  1082–1089.
- Erdős–Graham 1976, "On the prime factors of C(n,k)", Fibonacci Quart. 14,
  348–352.

Cited by: Guy UPNT (D14 and related), Filaseta 1996, Bennett–Filaseta–Trifonov
2009 (Crelle 629 — the modern sharpening of Sylvester's theorem, sought
separately), Filaseta–Kidd–Trifonov 2012.

## Bearing for this run

The theorem is a *global* structural fact about where the prime factors of
C(n,k) sit relative to k: for n ≥ 2k the "small-prime part" (primes < k) is
almost always beaten by the "large-prime part" (primes ≥ k), with only 12
exceptions. That is exactly the kind of constraint an argument bounding the
number of representations of a fixed a must use: every representation C(n,k)=a
with n ≥ 2k and k ≥ 2 contributes a large prime factor (Sylvester/Laishram–
Shorey gives one > k; this theorem controls the *split* of the whole
factorisation). The 12 exceptions are the only obstacle to a clean
"each rep with n ≥ 2k has its large-prime part > small-prime part" statement;
they are not on disk (paywalled), so do not cite their values. The 1993
Erdős–Lacampagne–Selfridge sequel ("Estimates of the least prime factor of a
binomial coefficient", Math. Comp. 61, 215–224, DOI 10.1090/s0025-5718-1993-1199990-6)
is the direction that bounds the least prime factor; that PDF exceeded this
run's 5 MB download cap and is recorded separately.

```claim
id: ees-1978-small-large-prime-split
statement: For positive integers n,k with n >= 2k, writing C(n,k) = u·v with all
  primes of u < k and all primes of v >= k, one has u < v with just 12
  determined exceptions; with primes of U <= k and of V > k the inequality
  U < V holds with at most finitely many exceptions, 19 determined, conjectured
  complete.
hypotheses: n >= 2k; the two partitions as stated (strict vs non-strict k).
holds-here: relevant to the zsigmondy / consecutive-block threads: every
  representation C(n,k) = a with n >= 2k, k >= 2 has its >=k-prime part larger
  than its <k-prime part outside a finite explicitly-known exception list.
status: asserted-by-source (abstract on disk; the argument and the 12/19
  exception lists are paywalled and NOT on disk — do not cite the exception
  values)
bearing: structural control of the prime split of C(n,k) relative to k; the
  engine behind Sylvester-type bounds the run's block approaches use. The 12
  exceptions being off-disk is the gap; BFT 2009 sharpens further.
anchor: research/summaries/ecklund-eggleton-erdos-selfridge-prime-factorization-1978.md
```