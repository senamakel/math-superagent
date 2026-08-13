# Approaches opened, and what closed each

A log of strategies this run considered, why each was tried, and the obstruction
that stopped it. The purpose is to stop the next attempt walking into a dead end
a second time.

## 1. Pure modular sieve (count-decay)

**Status: closed — provably cannot work.**

Attempt: show there exists a finite k where `|A_k| = 0`, i.e. that no residue
class `n mod 2·3^(k-1)` keeps the low k ternary digits of `2^n` in `{0,1}`.

**Obstruction (proved, not just computed):** 2 is a primitive root mod `3^k`
(order `2·3^(k-1)` — LAG-1, SAYE-2), so `Phi_k : n ↦ 2^n mod 3^k` is a bijection
onto the unit group `(Z/3^k)^×`. The attainable digit patterns are exactly those
with low digit 1 and the other k−1 digits in `{0,1}`: `2^(k-1)` of them. Hence
`|A_k| = 2^(k-1)` exactly for **every** k. The count doubles at every level; it
never decays, let alone reaches 0. Verified numerically to k=40 (program
`prove_count_doubles.py`, all sections PASS).

**Consequence (the run's main negative result):** no obstruction modulo any
finite power of 3 can prove the Erdős ternary conjecture. The kill for `n > 8`
must come from structure the sieve cannot see.

## 2. Naive count estimate

`|A_k| ≈ 2·3^(k-1)·(2/3)^k ≈ 2^k/3` predicts the sieve *grows*. This is exactly
right and is realized: `|A_k| = 2^(k-1)`. The estimate is not "wrong"; it was
never a death certificate, just an indication that counting cannot close the
sieve. Not an approach — a diagnosis.

## 3. Density / i.i.d.-digits heuristics

The density of integers whose ternary expansion avoids 2 tends to 0, and
independent-uniform digits give `(2/3)^k`. Both are **true and irrelevant**: they
concern all integers or a random model, and the sequence `2^n` is thin and
deterministic. Recorded as heuristics, never proofs (GOAL.md).

## 4. LTE lifting (the operator's sketch)

Adding `j·2·3^(k-2)` to the exponent multiplies `2^r` by `(2^(2·3^(k-2)))^j`.
The program verified `v_3(2^(2·3^(k-2)) − 1) = k−1` for k=2..40 with quotient
**c = 1 exactly** (never 2, never 0 mod 3). So `2^(2·3^(k-2)) ≡ 1 + 3^(k-1)
(mod 3^k)`. The three lifts shift only the top digit, giving `{d, d+1, d+2}` mod
3, exactly one of which is 2 → exactly two survive. This is consistent with and
corroborates the bijection proof; the bijection proof is preferred because it
avoids a carry analysis entirely.

**Status:** corroborated numerically; unconditional proof is the bijection
argument (SIEVE-EXACT), which does not depend on the LTE quotient.
