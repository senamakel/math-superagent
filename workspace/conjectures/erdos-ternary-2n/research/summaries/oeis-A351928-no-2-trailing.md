# OEIS A351928 — 2-avoidance in trailing ternary digits of powers of 2

**Source:** `https://oeis.org/A351928` (OEIS sequence record, author Robert Saye, Feb 25 2022). Also mirrored at `research/sources/oeis-A351928-no-2-trailing.md` (full text) and `research/summaries/oeis-A351928-no-2-trailing.md`.

## Definition
`a(n)` = smallest positive integer k such that 2^k has no digit 2 in the last n digits of its ternary (base-3) expansion.

That is: `a(n) = min{ k ≥ 1 : (2^k) mod 3^n has all n low ternary digits in {0,1} }` with the additional constraint 2^k ≥ 3^{n-1} (the powers must actually have ≥ n ternary digits).

## Terms (n = 1..43)
2, 2, 6, 8, 8, 8, 20, 24, 24, 24, 72, 186, 186, 332, 332, 1134, 1134, 1134, 1134, 1134, 1134, 25458, 25458, 25458, 25458, 25458, 25458, 159140, 249968, 249968, 249968, 249968, 249968, 249968, 249968, 249968, 9076914, 9076914, 9076914, 9076914, 9076914, 9076914, 90062678

## Relation to the run
- `a(n)` is the **minimum** exponent surviving the level-n 2-avoidance sieve. The run's `A_k` contains the residues `r mod 2·3^{k-1}` that survive; `a(k)` is the minimal positive representative of the smallest surviving class (up to the extra `2^k ≥ 3^{n-1}` floor). So `a(k) ∈ A_k` for the chosen representative, and `a(k) → ∞` exactly if the *minimum* surviving exponent grows — which is a different statement from `|A_k|` (which is 2^{k-1}, growing).
- The sequence is consistent with Saye's Θ(2^K) recursion and with the run's sieve; the **structure `a(k) ∈ A_k` with |A_k| = 2^{k-1}** means the minimum grows only when the particular "first" path dies, not because the count shrinks.
- Cross-references: A351927 (0-avoidance), A102483, A346497; Erdős (1979) is the origin of the conjecture.

## Claims
```claim
id: OEIS-928
statement: The least k with 2^k avoiding digit 2 in its last n ternary digits is A351928: 2,2,6,8,8,8,20,24,24,24,72,186,186,332,332,1134,...; in particular it is not monotone in n but is nondecreasing, and matches the run's sieve: a(n) is the minimum surviving exponent at level n (up to the ≥ n digits requirement).
hypotheses: n ≥ 1, powers of 2 required to have ≥ n ternary digits.
holds-here: yes — the sequence is exactly the "first survivor" of the 2-avoidance sieve for the Erdős conjecture.
status: checked (OEIS catalogue record; the values for n ≤ 43 are listed and consistent with Saye's recursion)
bearing: fixes the minimal-survivor values as a catalogue fact; a(n) = 8 at level 4 already, and it stays small (≤ 24) until level 11 — consistent with the witnesses 0,2,8 having their powers' low digits avoiding 2.
anchor: research/sources/oeis-A351928-no-2-trailing.md
```