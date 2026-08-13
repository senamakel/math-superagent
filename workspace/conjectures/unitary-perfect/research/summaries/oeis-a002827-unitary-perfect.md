# OEIS A002827 — unitary perfect numbers (source digest)

> Source: https://oeis.org/A002827 · full page verbatim at `research/sources/oeis-a002827-unitary-perfect.full.md` (never edited).

## Name — OEIS name line, exact

> **A002827**: Unitary perfect numbers: numbers k such that usigma(k) - k = k. (Formerly M4268 N1783)

OFFSET 1,1. "d is a unitary divisor of k if gcd(d,k/d)=1; usigma(k) is their sum (A034448)."

## DATA field — all five terms, exact transcription

> 6, 60, 90, 87360, 146361946186458562560000

These are exactly the run's five-witness oracle set in `GOAL.md`. "It is not known if a(6) exists." — N. J. A. Sloane, Jul 27 2015.

## EXAMPLE field — factorizations, exact transcription

- 6 = 2 * 3.
- 60 = 2^2 * 3 * 5.
- 90 = 2 * 3^2 * 5.
- 87360 = 2^6 * 3 * 5 * 7 * 13.
- 146361946186458562560000 = 2^18 * 3 * 5^4 * 7 * 11 * 13 * 19 * 37 * 79 * 109 * 157 * 313.
- "Unitary divisors of 60 are 1, 4, 3, 5, 12, 20, 15, 60, with sum 120 = 2*60."

The fifth factorization carries the `5^4` repeated kernel and ω = 12 — the sharp part of the witness set an impossibility lemma must not kill.

## Comments relevant to this run, verbatim

- "The prime factors of a unitary perfect number are the Higgs primes (A057447)." — Paul Muljadi, Oct 10 2005.
- "Frei proved that if there is a unitary perfect number that is not divisible by 3, then it is divisible by 2^m with m >= 144, it has at least 144 distinct odd prime factors, and it is larger than 10^440." — Amiram Eldar, Mar 05 2019.
- "All unitary perfect numbers are even (for a proof see the LeanGenius link)." — Peter Luschny, Jun 05 2026.
- Zumkeller-subsequence conjecture (A083207), "Verified for all present terms." — Ivan N. Ianakiev, Jan 20 2020.

## Formula — verbatim

> If m is a term and omega(m) = A001221(m) = k, then m < 2^(2^k) (Goto, 2007). — Amiram Eldar, Jun 06 2020

## What this establishes for the run

- Independent confirmation of the five witnesses, with the factorization of the fifth given explicitly (hand-check this session: the EXAMPLE prime powers multiply to 146,361,946,186,458,562,560,000, and `sigma_star`-style unitary-sigma identity holds for all five — machine re-check prepared at `code/higgs/check_a057447.py`).
- Transcription check of Muljadi's Higgs comment: every prime divisor of each of the five terms — {2,3}, {2,3,5}, {2,3,5}, {2,3,5,7,13}, and {2,3,5,7,11,13,19,37,79,109,157,313} — appears among the first 58 terms of A057447 (the 3-Higgs prime list).
- References: Guy UPNT B3; Frei 1978; Goto 2007 (m < 2^(2^k)); Subbarao–Cook–Newberry–Weber 1972; Wall 1975/1987; Wikipedia; Erdős problem #1052 page.