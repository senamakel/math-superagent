# Pattern-finder report — round 3

## What changed since the last pass

Since pattern_finder_report2.md, the run produced one new artifact relevant to
*sequence* structure: `code/out/coclique-bound-verified.md` (the exact coclique
bound values 3, 22, 45, 15 for rook, 99, BvLS, and the (57,14,1,4) comparison).
That gave me the seed of a genuinely new family-level sequence the earlier
rounds had only ever looked at one member of. I computed the whole feasible
family, derived the closed form, and attacked it.

## Finding — Coclique bound for the family has an exact closed form (CHECKED, derived)

For the family `srg(v,k,1,2)`, `k = u²+u+2`, `v = 1+k²/2`, the negative
eigenvalue is `s = −(u+1)` (since `4k−7 = (2u+1)²`), and the Hoffman coclique
bound

```
alpha ≤ v·(−s)/(k−s)
```

evaluates **identically** (proved symbolically in sympy and checked over every
`u ∈ [1,200]` with zero mismatches) to

```
alpha = (u·k+2)/2 = (u³+u²+2u+2)/2,
```

always an integer because `u·k` is even. The five feasible values:

| u | k | v | s | bound | (u·k+2)/2 |
|---|---|---|---|---|---|
| 1 | 4 | 9 | −2 | 3 | 3 |
| 3 | 14 | 99 | −4 | **22** | 22 |
| 4 | 22 | 243 | −5 | 45 | 45 |
| 10 | 112 | 6273 | −11 | 561 | 561 |
| 31 | 994 | 494019 | −32 | 15408 | 15408 |

This is a derivation, not a fit: it follows by direct substitution into the
standard eigenvalue formulas. The closed form is genuinely new to the run —
the k14-l1-local thread recorded the raw 99 bound (22) but not the identity.

**Bearing.** The five feasible bounds are all **distinct** (3, 22, 45, 561,
15408). So the srg(99,14,1,2) coclique bound **22 is parameter-specific**:
a nonexistence argument exploiting the specific value 22 (a 22-coclique
forcing a 2-(22,K,2) design, the direct analogue of the Wilbrink–Brouwer
15-coclique→2-(15,5,4) argument that killed (57,14,1,4)) is **not** refuted on
arrival by the negative controls rook(3) (bound 3) and BvLS (bound 45), because
neither equals 22. This promotes the coclique-design branch of the k14-l1-local
thread to the sharpest 99-specific non-spectral lever the run holds.

It does **not** rule out 99 — the bound forces nothing by itself (the true
independence number could be anywhere ≤ 22). Its value is that 22 is the one
clean, exactly-derivable, 99-only number the run has for a coclique-design
contradiction.

## Sequences that showed no further structure (re-confirmed)

- Triangles `{6,231,891,117096,81842481}`, pentagons `{0,33264,384912,1669320576,96451036488576}`, outer blocks, distance-2 counts, eigenvalue multiplicities — all satisfy no low-order constant-coefficient linear recurrence; all are the quartic-in-`u` forms from `k = u²+u+2`, as prior rounds established.
- The coclique-bound sequence `{3,22,45,561,15408}` and the triangle-count sequence `{6,231,891,117096,81842481}` are **not in the OEIS** (both lookups miss) — recorded so nobody searches again.

## Recommendation

The coclique-design branch is the most promising inexhaustive structural route
now on the board: at equality (a true 22-coclique) a putative 99-graph would
carry a 2-(22,K,2) design; the Wilbrink–Brouwer template shows the counting
inequality (their Lemma 1) is what turns such a coclique into a contradiction
at (57,14,1,4). A next attack is to push that same inequality at 99 under the
7K₂ local structure and replication-7 partial STS, verifying each step as a
99-specific one that rook(3)(3) and BvLS(45) cannot reach — but that is a
phase-4 structural argument for the inventor/thread, not a sequence finding.
