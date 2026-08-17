---
thread:
  question: Can Psi(k) for PE1006 be computed for k=10^18 in O(log) via the mechanical-word / geometrically weighted floor-sum, evaluated by the universal Euclidean (Chtholly / AtCoder floor_sum) algorithm?
  status: live
  rests-on: []
  blocked-by: []
  next: reproduce code/brute.py oracle (Psi(3)=20302, Psi(10)=10699667 mod M), then reproduce directive-2 mechanical-word construction against brute on k=1..150 before trusting it at 10^18.
---

# Thread: mechanical-word / floor-sum route (directive 2)

The two steering directives in `config/directives.jsonl` both claim outside-container
verification against a brute oracle. Neither has any in-container reproduction yet.
Directive 2 is the stronger form intended for the final solution; directive 1
(pair-correlation at k = F_n - 1) is a checkpoint and a second verification route.

## Directive 2 (primary, all k)

Model the k+1 distinct length-k Fibonacci subwords as a mechanical word: rational
slope a = F(n-1)/F(n) for F(n) >> k, cut the unit circle at the k+1 points
frac(-m*a), m = 0..k, take arc midpoint x of each arc, digit_j(x) =
floor(x + (j+1)a) - floor(x + j a). With v(x) = sum_j digit_j * 10^(k-1-j),
telescoping gives v(x) = floor(x+ka) - 10^(k-1) floor(x) +
9 * sum_{j=1}^{k-1} 10^(k-1-j) floor(x + j a). Psi(k) is the second moment of this
geometrically weighted floor sum over the k+1 representatives. Primitive: universal
Euclidean algorithm (monoid generalisation of AtCoder floor_sum, aka Chtholly),
carrying (count, sum x^j, sum x^j floor, sum x^j floor^2) mod M with
x = 10^-1 mod M, O(log) per evaluation. M = 101001001; 10 invertible since gcd = 1.

## Directive 1 (checkpoint at k = F_n - 1)

C(j,jp) = A(jp-j) = cyclic autocorrelation of standard word q_n, closed form
A(d) = max(0, m - t) + max(0, m - (N - t)), N = F_n, m = #ones(q_n), t = (d*m) mod N.

## Status

Nothing reproduced in-container. The immediate gate (per the run plan step 1) is a
naive brute program matching Psi(3) and Psi(10) before any derived method is trusted.
