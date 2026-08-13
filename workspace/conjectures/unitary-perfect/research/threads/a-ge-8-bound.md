```thread
question: Does the combined bound a ≥ 8 survive independent verification, and can the equality case a = 8 be eliminated?
status: open
rests-on: unitary-perfect-2-adic-budget, unitary-perfect-lower-bound-on-a, heven-two-mod-four
blocked-by: none yet
next:
  1. Independent verification: recompute a, ω(odd) from brute.py oracle for all five; confirm Wall 1988 theorem from the scanned PDF is stated for new examples
  2. Kill a = 8: Maciejewski Proposition 5 says H_even ⊆ {m ≡ 2 (mod 4)}. The paper's reduction maps a UPN's seed exponent a into H_even, so a ≡ 2 (mod 4). But a = 8 ≡ 0 (mod 4) — verify this is a valid elimination (check the reduction step: does a ∈ H_even follow, or something weaker?). If confirmed, the effective lower bound becomes a ≥ 10, not a ≥ 8
  3. Also check: 257 = 2^8+1 = F_3. v_2(257-1) = 8 > 3, so if the 3-Higgs exponent cap on p-1 applies, 257 is not 3-Higgs — another route to kill a = 8, but needs checking which exact constraint applies to the seed factor's prime divisors
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