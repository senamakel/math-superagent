# OEIS A351927 — 0-avoidance in trailing ternary digits of powers of 2

**Source:** `https://oeis.org/A351927` (OEIS sequence record, author Robert Saye, Feb 25 2022). Full text mirrored at `research/sources/oeis-A351927-no-0-trailing.md`.

## Definition
`a(n)` = smallest positive integer k such that 2^k has no digit 0 in the last n digits of its ternary expansion. Equivalently the least k whose last n low ternary digits are all in {1,2}.

## Terms (n = 1..47)
2, 1, 2, 4, 10, 15, 15, 15, 15, 15, 50, 50, 101, 101, 101, 101, 143, 143, 143, 143, 143, 143, 143, 143, 143, 1916, 1916, 1916, 1916, 1916, 1916, 82286, 1134022, 1639828, 3483159, 3483159, 3483159, 3917963, 3917963, 3917963, 4729774, 4729774, 9827775, 9827775, 43622201, 43622201, 43622201

## Relation to the run
- This is the Sloane persistence problem's sequence: Sloane (1973) conjectured every 2^n with n > 15 has a 0 somewhere in its ternary expansion (A102483, A346497). The values are dramatically larger than A351928 (0-avoidance is much rarer than 2-avoidance): already a(32) = 82286, a(34) ≥ 10^6.
- The asymmetry: the run's sieve for the **Erdős** conjecture is 2-avoidance (A351928, |A_k| = 2^{k-1}); the **Sloane** conjecture is 0-avoidance (A351927). Saye's paper (arXiv:2202.13256) verifies both to n ≤ 2·3^45.
- The astronomical minimal survivors in A351927 reflect that a(n) here is the minimum over a sub-sieve where the "all digits in {1,2}" condition is genuinely rare — contrast with 2-avoidance where low digit is forced to 1 and the count is exactly 2^{k-1}.

## Claims
```claim
id: OEIS-927
statement: The least k with 2^k avoiding digit 0 in its last n ternary digits is A351927: 2,1,2,4,10,15,15,15,15,15,50,50,101,...,43622201 (n ≤ 47); the values grow far faster than the 2-avoidance sequence A351928, consistent with Sloane's 0-avoidance conjecture (only 2^{0..4}, 2^{15} among powers have no 0, per Saye).
hypotheses: n ≥ 1; powers of 2 with ≥ n ternary digits.
holds-here: yes — the complementary digit-omission sequence to the run's.
status: checked (OEIS catalogue record)
bearing: quantifies the Sloane side for comparison; the Erdős side's survivors are far denser, which is exactly why the sieve on the Erdős side never empties.
anchor: research/sources/oeis-A351927-no-0-trailing.md
```