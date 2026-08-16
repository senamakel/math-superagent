# Saye, "On two conjectures concerning the ternary digits of powers of two"

Source: arXiv:2202.13256 (2022), J. Integer Sequences 25 (2022), Article 22.3.4. Full text: `[[saye-2022-two-conjectures-ternary-digits-powers-of-two.full]]` (URL: https://cs.uwaterloo.ca/journals/JIS/VOL25/Saye/saye3.pdf; also arXiv abs).

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

## Claims

```claim
id: SAYE-VERIFICATION-BOUND
statement: No 2^n with n <= 2·3^45 ≈ 5.9×10^21 has a digit-2-free ternary
  expansion except 2^0, 2^2, 2^8 (Sloane digit-0 conjecture likewise verified,
  exceptions {2^0,2^1,2^2,2^3,2^4,2^15}; digit-1 question equivalent to Erdős's).
hypotheses: n <= 2·3^45; max recursion depth K = 46, Θ(2^K) constructed powers.
holds-here: yes.
status: verified-numerically over the stated finite bound (NOT a proof; exact
  integer residue arithmetic, no floats)
bearing: the current verification bound. Any counterexample must have
  n > 2·3^45. This run's own sieve should reproduce a smaller bound and keep its
  own bound separate from this literature claim.
anchor: research/sources/saye-2022-two-conjectures-ternary-digits-powers-of-two.full.md
```

```claim
id: SAYE-ORDER-AND-LIFT
statement: Lemma 1: u_k := 2·3^(k-1) is the smallest positive integer with
  2^u_k ≡ 1 (mod 3^k) (= φ(3^k)); if 2^i ≡ 2^j (mod 3^k) then i ≡ j (mod u_k);
  and d_{k+1}(2^(i·u_k+j)) ≡ d_{k+1}(2^j) + i·d_1(2^j) (mod 3).
hypotheses: k, i, j positive integers.
holds-here: yes — the multiplicative-order and digit-lift facts underpinning the
  sieve and |A_k| = 2^(k-1).
status: proved (elementary, self-contained proof in Saye §5, verified here)
bearing: the recursive trailing-digit construction runs in Θ(2^K) vs Θ(3^K)
  naive; this is the engine by which the sieve reaches k=45. It also shows the
  sieve only controls trailing digits — cannot close.
anchor: research/sources/saye-2022-two-conjectures-ternary-digits-powers-of-two.full.md
```

## Status

Sourced, peer-reviewed (JIS). Verification is numerical over a stated finite bound — not a proof.
