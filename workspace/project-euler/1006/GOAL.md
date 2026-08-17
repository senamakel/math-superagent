# Goal

Find $\Psi(10^{18}) \bmod 101001001$ for Project Euler problem 1006.

## Precise statement

Let $S_0 = 0$, $S_1 = 01$, and for $n \ge 2$ let $S_n = S_{n-1}S_{n-2}$
(concatenation). So:

- $S_2 = 010$
- $S_3 = 01001$
- $S_4 = 01001010$

A **Fibonacci subword** of length $k$ is a contiguous substring of length $k$
(properly, a *factor*) of some $S_n$. A known fact: for each positive integer
$k$ there are exactly $k+1$ distinct Fibonacci subwords of length $k$.

Each distinct Fibonacci subword of length $k$ is interpreted as a decimal
number, ignoring leading zeros. $\Psi(k)$ is the sum of the squares of those
$k+1$ decimal numbers.

## Worked examples (oracle)

- $\Psi(3) = 20302$. The four length-3 subwords are $001,010,100,101$, giving
  $1^2 + 10^2 + 100^2 + 101^2 = 20302$.
- $\Psi(10) \equiv 10699667 \pmod{101001001}$.

## Completion criterion

Produce $A = \Psi(10^{18}) \bmod 101001001$, verified by the brute-force oracle
on every case it can reach (small $k$, and the two given examples), and by a
second independent route at full size where possible.

## Status: brute-force oracle complete (verified)

`code/brute.py` implements the naive oracle: it builds a long Fibonacci word,
collects all distinct length-$k$ factors, sums squares of the decimal ints.
Verified against the examples:

- length-3 subwords `001, 010, 100, 101`; Ψ(3) = 20302 ✓
- Ψ(10) mod 101001001 = 10699667 ✓
- factor counts exactly k+1 for k = 1..20, sets stable under extension ✓
- Ψ(1)..Ψ(20) values recorded in `code/out/PE1006-verification.md`

Surprise found: the suggested word-length bound (>= 2k) is NOT sufficient —
k = 15 needs length 35. brute.py uses >= 3k (safe for all k <= 30).

Not yet done: the efficient computation of Ψ(10^18) mod M at full size, and
its independent verification. Next step: derive the recurrence/structure
exploiting the k+1 Sturmian factors, with brute.py as the small-k oracle.
