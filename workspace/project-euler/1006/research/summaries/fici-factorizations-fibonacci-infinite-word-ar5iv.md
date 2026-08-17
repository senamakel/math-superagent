# Fici — *Factorizations of the Fibonacci Infinite Word* (J. Integer Seq. 18 (2015) 15.9.3; arXiv:1508.06754)

Source: https://ar5iv.labs.arxiv.org/html/1508.06754
(full text: [[fici-factorizations-fibonacci-infinite-word-ar5iv.full]])

## What this source establishes

A survey-note deriving, in sequence from elementary Fibonacci-number facts,
the various factorizations of the infinite Fibonacci word that use Fibonacci
words and related families (co-Fibonacci, singular, Christoffel words), plus
new ones. Only §1–2 are needed for this run.

**Section 1 (Preliminaries) — the characterization of the word itself.**
- Zeckendorf: every positive integer is a unique sum of non-consecutive
  Fibonacci numbers F_n, n > 1 (Theorem 1; Lekkerkerker/Ostrowski history).
- **The n-th digit of the Fibonacci infinite word f is the rightmost bit of
  the Zeckendorf representation of n** — i.e. f(n) = parity of the Zeckendorf
  digits. f = f(0)f(1)f(2)… = 0100101001001010010… (the problem's S_n limit).
- The finite words f_n = f(0)f(1)…f(F_n−1) (length F_n) satisfy
  **f_n = f_{n−1} f_{n−2}** (eq. (2)) — *exactly* the problem's S_n recurrence.
- Central words p_n (palindromic prefixes): p_n from f_n by removing the last
  two letters; f_{2n+1} = p_{2n+1}01, f_{2n+2} = p_{2n+2}10 (eq. (4)).

**Section 2 (Fibonacci and co-Fibonacci words).**
- Proposition 1: f = 0 · ∏_{n≥1} f_n = 0·1·0·01·010·01001·01001010… (a
  factorization of the infinite word by the finite Fibonacci words).
- The co-Fibonacci words f̃_n = E(f_n) (0↔1 swap), and the relationships used to
  show p_n central/Christoffel structure.

## What it implies for PE1006

1. **New equivalent digit characterization**: position-n digit of the word is
   determined by the Zeckendorf representation of n. This directly anchors the
   Ostrowski/Zeckendorf side — the numeration system underlying directive 1's
   O(log) lag-sum recursion and the factor-location results (Chuan–Ho use the
   same Zeckendorf technology).
2. The finite words f_n ARE the problem's S_n (same recurrence, same initial
   words up to the stated indexing), so the "first 1652 subwords" / position
   theorems transfer with no convention change — unlike the Sivasankar–Rama
   rabbit complement.
3. Proposition 1's factorization and the central-word equations give an
   alternative route to the first-occurrence positions of length-k factors
   (the k+1 factors' starting positions), corroborating the position theorem.

## Claims anchored here

`fibonacci-zeckendorf-parity-characterization`
(research/notes/sourced-claims-least-periods-standard-factors.md).

## What it does NOT establish

- Nothing about reading factors as decimals or summing squares.
- Nothing about mechanical words / floor sums / universal-Euclidean evaluation.
- The factorizations are structural; they do not by themselves evaluate Ψ(k)
  at k = 10^18.