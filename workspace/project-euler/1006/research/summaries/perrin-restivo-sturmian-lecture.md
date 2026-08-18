# Perrin & Restivo — A note on Sturmian words (TCS 429 (2012) 243–250)

<!-- source: https://hal.science/hal-00828351v1/file/noteSturmianWords.pdf | read 2026-08-19 -->

Full text: `research/sources/perrin-restivo-sturmian-lecture.full.md`

## What it establishes

A paper on generating the set of factors of a Sturmian word in lexicographic order (via the Burrows–Wheeler connection). Alphabet {a,b}. **The Fibonacci word appears as the running example, with slope α = 2/(3+√5) = [0;2,1,1,…] and convergents 1/2, 1/3, 2/5, 3/8, 5/13…** (this is PE1006's S_∞ under a↔b).

**Theorem 2 (consecutive factors).** Two words u,v of F of the same length are consecutive in the lexicographic order iff u = r·a·b·s and v = r·b·a·s, or u = r·a and v = r·b. (The prefix r is the "principal prefix", always right-special.)

**Proposition 2.** The first and last elements of F∩Aⁿ have the form a·s and b·s.

**Proposition 3 (right border).** Ordering F∩Aⁿ lexicographically as (u₀,…,uₙ) and writing the last letters a₀a₁…aₙ, this "right border" word is conjugate to a word in a∗b∗. Equivalently (with the matrix M whose rows are the factors), each column of M is conjugate to a word in a∗b∗.

**Theorem 3.** T(w) = b^p a^q (p,q coprime) iff w is a conjugate of a standard word — the Burrows–Wheeler connection; for the Fibonacci word w = abaababa, T(w) = b³a⁵.

**The factor set at Fibonacci lengths (the section after Theorem 3, matching Wen–Wen).** For m = |sₙ| (a Fibonacci length, sₙ the standard/Fibonacci word), F∩Aᵐ is the union of the set X of **conjugates of sₙ** and the **singular factor** of length m; the singular factor is always the first or last element of F∩Aᵐ, and is of the form wₙ = x·sₙ·y⁻¹ = x·pₙ·x with pₙ palindromic. Example 10 (length 8): factors = conjugates of abaababa plus the singular factor babaabab.

**§5 — the exact integer algorithm for the characteristic word.** Given coprime u>v: `Characteristic(u,v,n)` with d←v; for i=1..n: if d+v < u then d←d+v, s[i]←a else d←d+v−u, s[i]←b. For a continued-fraction approximation v/u of α and n ≤ u−2, this returns the length-n prefix of the characteristic word — a Christoffel word when n = u−1. Example 11 runs it for (13,5,11) on the Fibonacci slope. **This is precisely the integer mechanical construction the run's solver implements** (slope 1/φ², exact rational approximant, floor-difference digits).

## Why it matters for PE1006

- **Theorem 2 + Proposition 3 give the lexicographic skeleton of the k+1 factors**: consecutive factors differ by an ab→ba swap at a right-special prefix; the right-border/column structure says the last-letter sequence is a∗b∗-conjugate. This is exactly the kind of structural constraint the run's Ψ-sum could exploit to order the k+1 factors and their decimal values.
- The singular-factor statement (conjugates + one singular word at Fibonacci lengths) is an independent statement of the Wen–Wen structure, in the standard-word convention.
- The Characteristic(u,v,n) integer algorithm is the exact primitive the run's mechanical construction (`mechanical-word-digit-rule`) uses, source-pinned with correctness conditions (n ≤ u−2, v/u a continued-fraction approximant).

## What it does NOT establish

- No Ψ(k), no decimal weighting, no floor-sum evaluation, no O(log) method. The generation algorithm is O(n²) to list all factors (fine for small k, not the full-size route).

## Claims anchored here

Corroborates `governing-sturmian` (slope 1/φ², convergents), `mechanical-word-digit-rule` (integer Characteristic algorithm + correctness condition n ≤ u−2), `unique-right-special-sturmian-sourced` (principal prefix always right-special), `sivasankar-rama-position-theorem`/Wen–Wen (conjugates + singular factor at Fibonacci lengths).
