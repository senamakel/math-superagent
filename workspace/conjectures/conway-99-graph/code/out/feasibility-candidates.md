# Feasibility of candidate srg(v, k, 1, 2) members — exact check

Computed by the librarian (hand, exact integer arithmetic) on a cold run to
resolve a disagreement between two library sources. **Feasibility check only,
not an oracle verdict.** The canonical oracle lives in `code/lib`; the script
`code/out/feasibility.py` encodes the same arithmetic for the oracle team to
confirm.

## The two conditions every member must pass

For `srg(v, k, λ, μ)` with `λ = 1, μ = 2`:

1. **Counting**: `v = 1 + k + k(k−2)/2`  (from `k(k−λ−1) = (v−k−1)·μ`).
2. **Perfect square**: eigenvalue discriminant `Δ = (λ−μ)² + 4(k−μ) = 4k−7`
   must be a perfect square, else `r, s` are irrational — and a finite graph
   has algebraic-integer eigenvalues, so this is necessary.
3. **Multiplicity integrality**: the two non-k eigenvalues have multiplicities
   `m± = ½[(v−1) ∓ (2k − (v−1))/√Δ]`, and both must be nonnegative integers
   (they sum to `v−1` and are integers iff one is).

`problem.md`'s candidate list `k = 4, 8, 14, 22, 32, 44, …` checks condition 2
only. The literature's "only five possible members" list is
`(k,v) = (4,9), (14,99), (22,243), (112,6273), (994,494019)`. The difference is
condition 3, which kills `k = 8, 32, 44`.

## Exact hand arithmetic (all integers)

| k | v | Δ=4k−7 | √Δ | 2k−(v−1) | (2k−(v−1))/√Δ | m± integer? |
|---|---|---|---|---|---|---|
| 4  | 9   | 9   | 3  | 8−8=0      | 0/3 = 0     | YES (m=4,4) |
| 8  | 33  | 25  | 5  | 16−32=−16  | **−16/5 ✗** | **NO** |
| 14 | 99  | 49  | 7  | 28−98=−70  | −70/7 = −10 | YES (54,44) |
| 22 | 243 | 81  | 9  | 44−242=−198| −198/9=−22 | YES |
| 32 | 513 | 121 | 11 | 64−512=−448| **−448/11 ✗**| **NO** |
| 44 | 969 | 169 | 13 | 88−968=−880| **−880/13 ✗**| **NO** |
| 112| 6273| 441 | 21 | 224−6272=−6048| −6048/21=−288 | YES |
| 994| 494019| 3969| 63| 1988−494018=−492030| /63=−7810 | YES |

Every `k` with `Δ` a perfect square gives integral multiplicities **except**
`k = 8, 32, 44`. The survivors are exactly the literature's five:
`(4,9), (14,99), (22,243), (112,6273), (994,494019)`.

## Resolution

**`srg(33, 8, 1, 2)` is excluded by eigenvalue-multiplicity integrality** — the
−16/5 in the table is not an integer. This is the "nearest precedent"
mechanism `problem.md` asked for: the next member up from the rook's graph is
ruled out by the standard integrality condition, not by anything graph-specific.

**`problem.md`'s candidate list is wrong past `k = 22`**: it lists `32 → 513`
and `44 → 969` as candidates, but both fail multiplicity integrality. The
`4k−7` perfect-square condition alone admits them; the full feasibility
condition does not. **The literature's "five members" list wins.**

Both `v = 9` and `v = 243` survive every condition here, consistent with them
existing — confirming they cannot be touched by any integrality/feasibility
argument (as `problem.md` insists). Status: hand-derived exact arithmetic;
confirm with `feasibility.py` through the oracle before citing.
