# OEIS A057447 — 3-Higgs primes (source digest)

> Source: https://oeis.org/A057447 · full page verbatim at `research/sources/oeis-a057447-3-higgs-primes.full.md` (never edited).

## Definition — OEIS name line, exact

> **A057447**: a(n+1) = next prime such that a(n+1)-1 | (a(1)...a(n))^3.

OFFSET 1,1. The page's Mathematica code seeds the product with `{2}` and appends the least prime `d` after the last term with `(d-1) | (product)^3`; so a(1) = 2 and each later term is the least prime p > a(n) whose predecessor p−1 divides the **cube** of the product of all earlier terms. This is the standard k-Higgs recursion with k = 3.

## DATA field — first 30 terms, exact transcription

> 2, 3, 5, 7, 11, 13, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 101, 107, 109, 127, 131, 139, 149

Terms 31–58 (the rest of the page's data field): 151, 157, 167, 173, 179, 181, 191, 197, 199, 211, 223, 229, 233, 251, 263, 269, 271, 277, 281, 283, 293, 311, 313, 317, 331, 347, 349, 359. The b-file (T. D. Noe) runs to n = 1000.

## Comments on the page, verbatim

- "No prime of the form a*b^k + 1, with a > 0, b > 1 and k > 3 (including those in A037896) belongs to the sequence." — Mauro Fiorentini, Aug 09 2023.

Meta: AUTHOR Robert G. Wilson v, Sep 25 2000; keyword `nonn`; crossrefs A007459 (2-Higgs primes), A037896, A057448.

## What this establishes for the run

- The 3-Higgs predicate to cross-check a recursive implementation against: generate primes in increasing order, keep p iff `(p-1) | (product of kept primes)^3`, start with 2 — exact integer arithmetic.
- Hand-check (this session, small-case oracle): the recursion yields a(1..7) = 2, 3, 5, 7, 11, 13, 19, and every skip in the page's data up to 359 is forced by the cube — 17 (16 ∤ P³, v2 short), 97, 103 (contains prime 17 ∤ P), 113, 137, 163 (3^4), 193 (2^6), 239 (prime 17), 241 (2^4), 257 (2^8), 337 (2^4), 353 (2^5). A further programmatic check against all 58 terms is prepared at `code/higgs/check_a057447.py` (not yet executed this run — the librarian has no shell).
- Bridge to the main problem: A002827's comment "The prime factors of a unitary perfect number are the Higgs primes (A057447)" — the five known unitary perfect numbers are exactly the run's witness set, so their prime divisors must all lie in this list (see the A002827 digest); and `H_even` is defined as even m for which every prime divisor of 2^m + 1 is 3-Higgs, so this list is the allowed-recruit catalogue for that branch.