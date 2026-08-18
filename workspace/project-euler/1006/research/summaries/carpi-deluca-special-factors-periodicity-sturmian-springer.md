# Carpi & de Luca — Special factors, periodicity, and an application to Sturmian words (Acta Informatica 36 (2000) 983–1006)

<!-- source: https://doi.org/10.1007/pl00013299 | 2026-08-19. STATUS: on-disk "full text" is the Springer *landing page* (abstract + paywall), not the paper body. The statements below are from the abstract; proof-level detail is NOT on disk. -->

Full text: `research/sources/carpi-deluca-special-factors-periodicity-sturmian-springer.full.md` (landing page only)

## What it establishes (per the abstract)

**Main theorem (finite words).** Let w be a finite word and n the least non-negative integer such that w has no right-special factor of length n and its right factor of length n is unrepeated. Then if all factors of another word v up to length n+1 are also factors of w, v itself is a factor of w.

**Infinite case.** A similar result for ultimately periodic infinite words, giving "uniqueness conditions" for ultimately periodic words.

**Sturmian application.** An upper bound for the rational exponents of factors of uniformly recurrent non-periodic infinite words, and a general formula for the **critical exponent** of a power-free Sturmian word; in particular the critical exponent is effectively computable for any Sturmian sequence whose slope has a periodic continued-fraction development. (This is the source of the Carpi–de Luca critical-exponent formula ind(u) = sup_n (2 + a_{n+1} + (q_{n−1}−2)/q_n) that Cassaigne Theorem 2.1 cites.)

## Why it matters for PE1006

- The critical-exponent formula for Sturmian words is what Cassaigne Theorem 2.1 uses to compute ind(f) = Φ+2 (see the Cassaigne digest). It bounds the repetition structure of the Fibonacci word's factors — background, not the Ψ sum.
- The special-factor machinery (right-special factors, unrepeated right factors) underlies the run's unique-right-special-factor axis (`fibonacci-unique-special-factor-reverse`, the R_k hinge of the extension recurrence), but this particular paper's theorems are about periodicity/critical exponents, not the factor-sum the run needs.

## What it does NOT establish

- No Ψ(k), no decimal weighting, no floor-sum, no O(log) method.
- The on-disk file is only the Springer landing page; the full paper is paywalled. Do not cite proof-level claims from this file.

## Status honesty

Landing page only. Not on the run's critical path. Corroborates `governing-factor-complexity` / `unique-right-special-sturmian-sourced` indirectly via the special-factor framework.

## Claims anchored here

None new. Background.
