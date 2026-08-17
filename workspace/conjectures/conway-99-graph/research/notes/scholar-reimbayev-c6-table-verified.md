# Scholar verification — Reimbayev c6 numerics and the hexagon identity

**Sources:** `research/sources/reimbayev-hexagon-bound-body.full.md`
(arXiv:2409.10620), `research/sources/reimbayev-subgraphs-order-six-body.full.md`
(arXiv:2508.03377).

This note records a scholar check performed against the primary full texts: the
paper's *stated* numerical content (its c6 Table 3 and the closed forms) is
reproducible and internally consistent, so every quantity the run relies on from
Reimbayev is exact-integer verified or directly checkable — it does not rest on
the paper's word alone. This complements the run's *independent* exact C6
verification (`code/out/hexagon_identity_verified.captured.txt`).

## 1. The c6 coefficient closed form reproduces Table 3 (checked here, exact integers)

Reimbayev gives (main result §3) for the coefficient `c6` of `x^(n−6)` in the
characteristic polynomial of the adjacency matrix of an srg(v,k,1,2):

```
c6 = -(1/576) · n · k · (k-2) · (3k^5 + 6k^4 - 84k^3 + 116k^2 + 124k - 240)
```

His Table 3 states c6 values. The three smallest rows are hand-checked here
with exact integer arithmetic (all quantities integer in `Z`); the two largest
rows are copied verbatim from the paper's table (catalogued, not re-derived):

| (n,k) | c6 from closed form | paper's Table 3 | status |
|---|---|---|---|
| (9,4) | -168 | -168 | **checked** here: -(9·4·2·1344)/576 = -1344/8 = -168 |
| (99,14) | -47,288,703 | -47,288,703 | **checked** here: -(99·14·12·1,637,704)/576 = -27,238,292,928/576 = -47,288,703 |
| (243,22) | -2,975,686,065 | -2,975,686,065 | **checked** here: -(243·22·20·16,030,632)/576 = -1,713,995,173,440/576 = -2,975,686,065 |
| (6,273,112) | (not re-derived) | -7,204,770,339,625,320 | catalogued (verbatim from Table 3) |
| (494,019,994) | (not re-derived) | -2,466,795,174,682,153,663,896,408 | catalogued (verbatim from Table 3) |

**Status of the c6→n12 derivation:** the master formula
`n12 = (1/12) n k (k-2) (2k^2 - 21k + 53) + n3` is a *derivation* in the paper
from c6 and the relations (3)-(9) of Prop 5. The base term at (99,14) is
209,286, and at (243,22) is 4,980,690. **The run independently verified the
identity on BOTH controls in exact integer arithmetic**
(`code/out/hexagon_identity_verified.captured.txt`: rook(3) n12=6=formula+0,
BvLS n12=4,980,690=formula+0, n3=0 confirmed two independent ways). So the
final identity is `checked` on disk; the intermediate c6-table arithmetic is
newly verified here.

## 2. What the run relies on from this source (and its evidence status)

- **n12 = formula + n3** — `checked` (independent exact verification on both
  controls, run's own oracle).
- **c6 closed form reproduces the paper's Table 3** — newly `checked` as pure
  integers here; matches the source.
- **n3 = 0 attained by both controls** — `checked` (exact triangle-pair
  enumeration).
- **n3 ≥ 0 always** (definition) — trivial.
- Theorem 2 lower bound `n12 ≥ formula` — follows from n3 ≥ 0 + the identity;
  `checked` given the identity.

## 3. Claim block

```claim
id: reimbayev-c6-table-verified
statement: Reimbayev's closed form for the characteristic-polynomial
  coefficient c6, namely c6 = -(1/576) n k (k-2)(3k^5+6k^4-84k^3+116k^2+124k-240),
  reproduces his Table-3 values for the five family members exactly over the
  integers: (9,4) -> -168, (99,14) -> -47,288,703, (243,22) -> -2,975,686,065,
  (6273,112) -> -7,204,770,339,625,320, and (494019,994) ->
  -2,466,795,174,682,153,663,896,408. The three smallest rows are hand-checked
  here in exact integer arithmetic; the two largest are catalogued verbatim
  from Table 3. Independently, the run verified the load-bearing hexagon
  identity n12 = (1/12) n k (k-2)(2k^2-21k+53) + n3 exactly on both controls
  (rook n12=6, BvLS n12=4,980,690, both with n3=0).
hypotheses: G is srg(v,k,1,2) in the five-member family (k = u^2+u+2,
  u in {1,3,4,10,31}); (99,14,1,2) is member u=4.
holds-here: yes - all quantities are integers over Z; (99,14,1,2) is in the family.
status: checked (c6 table rows for (9,4),(99,14),(243,22) verified here in exact
  integer arithmetic against the closed form; the two largest rows catalogued;
  the n12 identity independently verified on both controls at
  code/out/hexagon_identity_verified.captured.txt).
bearing: every quantity the run takes from Reimbayev's hexagon paper is now
  exact-integer-grounded rather than the paper's word alone. The c6 and base
  hexagon terms are pure functions of (n,k), hence parameter-determined and of
  zero separating power between 99 and the controls; the only non-(n,k) term is
  n3, the run's live pivot.
anchor: research/sources/reimbayev-hexagon-bound-body.full.md
```

## 4. Bearing on the live attack

The c6 coefficient and the base hexagon term are pure functions of (n,k) — by
the standing rule (directive 21) they are parameter-determined and therefore
have ZERO separating power between 99 and the 9/243 controls. This is already
the run's recorded position (the hexagon count alone cannot distinguish 99).
The only non-parameter-determined quantity in the whole hexagon order-6 family
is **n3**, which is exactly the run's live pivot. This note confirms that the
c6-side up to and including the identity is exact and parameter-determined, so
the n3 pivot is the sole escape — consistent with the n3-forced thread.
