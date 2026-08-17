# Goal

PE1006: Ψ(10^18) mod 101001001, where Ψ(k) = sum of squares of the k+1
distinct length-k Fibonacci subwords read as decimal integers (leading zeros
ignored).

Brute oracle verified (Ψ(k) exact k=1..150; Ψ(3)=20302, Ψ(10) mod 101001001
= 10699667). No constant-coefficient C-finite recurrence for Ψ(k)
(Berlekamp–Massey saturates at n/2). The risen-sea route: change the ground —
map the two periodic structures Ψ is built from, and reduce 10^18 via
exponent-orders rather than a Psi-period.

## Status of the three structural tasks (this run)

- TASK A (DONE, verified two ways): M=101001001 is PRIME. ord_10(M)=50500500
  (=(M-1)/2); Pisano period pi(M)=101001000 (=M-1). M-1=2^3·3·5^3·131·257.
- TASK B (DONE, negative result explained): r(k)=Psi(k) mod M has NO constant
  period <= 75 over k=1..150; the small-period reduction route is structurally
  impossible (ord_10(M)=50500500 >> 150 points means no power of 10 repeats in
  range). Reduction of 10^18 must be per-exponent mod ord_10(M), not a
  Psi-period.
- TASK C (DONE): factor table k=1..12 exact; N(i;k) balanced in i (two
  consecutive values), constant F_{m-2} at k=F_m-1; candidate
  N=floor((k-i)a+const) FALSIFIED; exact ones-total T(k)=(k+1)·floor(ka)+r_k.

## Open / remaining

Computing Ψ(10^18) mod M itself. Blocked on collapsing the double sum over the
balanced two-value column structure (polysmall in log k) — the factor-sum
expressed via ord_10/pi exponent reduction. Not a completion yet.

## Completion criteria

Three printed + saved reports (done: code/out/mod_A.txt, mod_B.txt,
mod_C.txt plus _struct/_ones and mod_report.md), all exact, structural
conclusions stated. Full Ψ(10^18) value remains open (posted to board).
