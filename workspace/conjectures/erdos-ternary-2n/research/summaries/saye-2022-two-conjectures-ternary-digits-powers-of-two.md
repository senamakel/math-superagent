# Saye, "On two conjectures concerning the ternary digits of powers of two"

Source: arXiv:2202.13256 (2022), J. Integer Sequences 25 (2022). Full text: `research/sources/saye-2022-two-conjectures-ternary-digits-powers-of-two.full.md` (also .pdf.full).

## What it establishes (verified range)

**Erdős conjecture verification:** no `2^n` with `n ≤ 2·3^45 ≈ 5.9×10^21` has a digit-2-free ternary expansion except `n = 0, 2, 8`.
**Sloane conjecture (digit 0):** for `n > 15`, `2^n` always contains a ternary 0, verified over the same range.

Also: the digit-1 question is essentially equivalent to Erdős's (exceptions −2^1, 2^3, 2^9).

## The method — a recursive construction of `2^n` with prescribed trailing ternary digits

This is the direct instrument the run's sieve can learn from. Key lemma:

**Lemma 1.** For positive integer k, define `u_k := 2·3^(k-1)`.
- (i) `u_k` is the smallest positive integer with `2^(u_k) ≡ 1 (mod 3^k)`.
- (ii) if `2^i ≡ 2^j (mod 3^k)` then `i ≡ j (mod u_k)`.
- (iii) the (k+1)-st ternary digit of `2^(i·u_k + j)` relates to the (k+1)-st digit of `2^j` by `d_{k+1}(2^(i·u_k+j)) ≡ d_{k+1}(2^j) + i·d_1(2^j) (mod 3)`.

This is precisely the statement that the multiplicative order of 2 mod `3^k` is `u_k = 2·3^(k-1)`, and the digit-lifting recursion behind the sieve. It constructs, for each k, an index `u_k` and coefficients so that `2^(u_k)` has controlled trailing digits; the recursive Algorithm 1 generates `Θ(2^K)` powers of two with prescribed trailing (0/1)-patterns.

Complexity note: `Θ(2^K)` work vs the `Θ(3^K)` of a naive sweep — this is why the trailing-digit sieve can reach `k=45` here while a scan of all `n` cannot.

## Relevance

- The 3-adic order fact `ord_{3^k}(2) = 2·3^(k-1)` is confirmed and used structurally.
- The recursive trailing-digit construction is the practical engine for the run's sieve instrument — but it also shows the sieve alone cannot close (it only controls trailing digits), matching GOAL.md's warning.
- `A_k` survivors are exactly the `{0,1}` trailing-digit residues; Saye's Lemma 1(iii) is the lift step the run must reproduce to re-derive `|A_k|`.

## Status

Sourced, peer-reviewed (JIS). Verification is numerical (exact integer arithmetic on residues) over a stated finite bound — not a proof of the conjecture. Bound stated precisely: `n ≤ 2·3^45`.
