```thread
question: Does the combined bound a ≥ 8 survive independent verification, and can the equality case a = 8 be eliminated?
status: closed — equality case eliminated for 2 ≤ a ≤ 28 by budget-equality-case-impossible
resolution: The equality case ω(odd) = a + 1 is impossible for every a in [2,28] by an extremal-product bound (claim budget-equality-case-impossible, filed in this workspace). In particular a = 8 is dead: 257 = 2^8+1 is prime and forced as a component, and the maximum possible Π(1+1/q) over nine components all 1 mod 4 falls short of the required T(8) = 512/257 by 0.297 in exact arithmetic. The bound is attained with equality at a = 1 (n = 90, the one known number in the equality case). Undecided for a ≥ 29. The result was adopted from operator computation; independent verification is now the top TASKS.md item.
rests-on: unitary-perfect-2-adic-budget, unitary-perfect-lower-bound-on-a, budget-equality-case-impossible
blocked-by: none
next: independent verification (see TASKS.md item 1); the next structural step is whether the inequality case ω(odd) ≤ a can be sharpened, or whether a ≥ 29 can be pushed.
closed-by: directive
```

## What is claimed

Wall (1988) proves `ω(odd) ≥ 9` for any unitary perfect number other than the five known. The budget corollary `ω(odd) ≤ a + 1`, proved in this workspace, gives `a ≥ ω(odd) − 1 ≥ 8`. So `2^8 = 256` divides any sixth UPN.

The directive names this as a free result already written up at `research/notes/lower-bound-on-a.md` with capture `code/out/wall1988_budget_lower_bound.captured.txt`. It says: verify independently, then push the equality case.

## The equality case a = 8

If `a = 8`, the budget identity forces `ω(odd) = 9` with all nine odd components `≡ 1 (mod 4)`. The seed is `2^8 + 1 = 257`, a Fermat prime `F_3`.

Two routes to kill it (need to check which is valid):

**Route A — H_even congruence.** Maciejewski Proposition 5: `H_even ⊆ {m ≡ 2 (mod 4)}`. If the paper's Subbarao-Warren reduction forces `a ∈ H_even` (and not some weaker condition), then `a = 8 ≡ 0 (mod 4)` is eliminated. The next viable value is `a = 10`.

**Route B — 3-Higgs exponent cap.** 257 is prime. `257 − 1 = 256 = 2^8`. The 3-Higgs condition requires every prime `q | (p − 1)` to have `v_q(p − 1) ≤ 3`. Here `v_2(256) = 8 > 3`, so 257 is not 3-Higgs. If the seed factor's prime divisors must be 3-Higgs (the paper's H definition), `a = 8` is eliminated.

The two routes may be equivalent — need to verify from the paper.