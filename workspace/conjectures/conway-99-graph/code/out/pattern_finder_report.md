# Pattern-Finder report — exact structure in the computed data

I read the run's computed artifacts (derived-design sequences, feasibility tables,
hexagon/C6 counts, BvLS/rook oracle results) and ran the exact sequence tools.
Two findings are genuinely new and exact; one is a cross-check that promotes a
source-asserted claim to checked on both controls.

## Finding 1 — Integrality of the family = "a = √(4k−7) divides 63" (CHECKED)

The five feasible members `u ∈ {1,3,4,10,31}` (from `k = u²+u+2`) are not an
opaque index list — they are exactly the odd divisors of 63:

```
a = 2u+1 = √(4k−7) ∈ {3, 7, 9, 21, 63}  ⟺  a | 63  ⟺  u ∈ {1,3,4,10,31}
```

Derivation (exact, verified in sympy and by exhaustive scan):
- `v−1 = k²/2`, so the negative-eigenvalue multiplicity is integral iff
  `a | k(4−k)/2`.
- With `k=(a²+7)/4`, `k(4−k)/2 = (a²+7)(9−a²)/16`; since `a` is odd, `gcd(a,16)=1`,
  so this reduces mod `a` to `a | 7·9 = 63`.
- `passes(u)` iff `(2u+1) | 63` holds with **zero mismatches** over `u ∈ [1, 300000]`.

**Bearing.** It names the mechanism that kills `srg(33,8,1,2)` (a=5 ∤ 63) and why
it cannot touch 99 (a=7 | 63). 99 is the member with `a=7`. This sharpens claim
`srg33-mechanism-answers-request` and closes the "nearest precedent" dead end for
good: the obstruction is spectral integrality, which 9 and 243 both survive.

## Finding 2 — Hexagon identity n₁₂ = formula + n₃ holds with n₃ = 0 on both controls (CHECKED)

The Reimbayev identity `n₁₂ = (1/12)·n·k·(k−2)·(2k²−21k+53) + n₃` is verified
**exactly** on both existing graphs, with `n₃ = 0` confirmed by two independent
exact routes:

| graph | triangles | n₃ | formula | induced C6 (n₁₂) | n₁₂ − formula |
|---|---|---|---|---|---|
| rook(3) | 6 | 0 | 6 | 6 | 0 ✓ |
| BvLS(243) | 891 | 0 | 4,980,690 | 4,980,690 | 0 ✓ |

Cross-checks: `count_induced_C6` (lib.hexagons) validated against independent
brute force (rook=6, bare C6=1); triangle-pair join-edge enumeration gives n₃=0
directly; Makhnev condition (*) holds on both (0 violating triangle pairs).

**Bearing.** Both existing members attain the hexagon bound and satisfy n₃=0, so
n₃=0 is *family-realizable*. The hexagon count alone cannot separate 99. The
Makhnev/Reimbayev conditional "n₃=0 ⇒ no srg(99,14,1,2)" is asserted-by-source and
paywalled (unverified). The open lever is whether n₃ is *forced ≥ 1* in any
putative (99,14,1,2) by a counting argument — not the identity itself.

## Filled stub (directive)

`code/out/makhnev-1988-condition-captured.txt` is no longer "NOT YET RUN": it now
carries the real output for both controls (rook: 6 triangles all joined by 3 edges,
0 bad; BvLS: 891 triangles, 8910 joined by 3, 0 by 2; both satisfy (*)). Plus the
new hexagon capture `code/out/hexagon_identity_verified.captured.txt`.

## Sequences that showed NO further structure

The hexagon-count sequence `{6, 209286, 4980690, 146767540920, 79371206037594576}`,
triangle counts, distance-2/outer-block counts, and the multiplicity sequences all
fail low-order linear recurrences — they are governed by the closed forms in
`k = u²+u+2`, `v = 1+k²/2`, and the a|63 integrality, not by an independent law.

## Recommendation

The single most exploitable exact fact is Finding 1: a putative (99,14,1,2) is the
`a=7` member, and any nonexistence argument must be specific to a=7 — the a|63
spectral integrality is precisely what 9 (a=3) and 243 (a=9) survive. A natural next
attack, consistent with the geometry route, is whether the `a=7` arithmetic forces a
counting obstruction in the 84-point/140-block outer partial Steiner triple system
(Finding 2's n₃ lever), since n₃=0 is exactly the condition Makhnev's conditional
would plug into.
