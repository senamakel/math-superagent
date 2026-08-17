# Scholar — order-7 Reimbayev verified in code + durable findings stored to disk

Cognee is down for the whole run (8 `remember_memory` failures, degraded health
report; recall is non-functional per directive 20). Every durable finding that
would have gone to Cognee is recorded here instead, on disk, where the run can
reach it. Nothing durable is lost; it lives in this note and in the claim blocks
that derive into `research/CLAIMS.md`.

## 1. Order-7 Reimbayev counting: promoted from asserted to checked

The newest acquisition (Reimbayev arXiv:2511.06572, order-7 Hamiltonian
subgraphs of srg(n,k,1,2)) landed as `asserted`/hand-verified while Cognee was
down. This pass re-derived its arithmetic in exact integer arithmetic at the
target (99,14,1,2) and at the five family members. The transcription in
`research/notes/librarian-order7-acquisition.md` matches the source full text
verbatim (read at
`research/sources/reimbayev-hamiltonian-order7-srg-l1-mu2.full.md` lines 140-175).

**Verified at (99,14,1,2), n3=0, h11=0 (exact integers):**

| h_i | value |
|-----|-------|
| h0 (heptagons) | 17,463,600/14 = **1,247,400** (=(1/14)·99·14·12·10·105) |
| h1 | (1/2)·16632·110 = **914,760** |
| h2 | 99·14·12·10·6 = **997,920** |
| h3,h4,h6,h9 | 99·14·12·10 = **166,320** each |
| h5,h7 | **83,160** each |
| h8 | **332,640** |
| h12,h17 | (1/4)·99·14·12 = **4,158** each |
| h10,h11,h13,h14,h15,h16,h18 | **0** |

All nonnegative integers; the bound `4·n3 >= h11 >= 2·n3` holds as 0=0=0. The
heptagon upper bound p7 = 1,247,400 is parameter-determined (same value at n3=0
as at the two controls), so **order-7 counting does not force n3>=1 at 99**,
and the p7 bound gives zero separating power between 99 and the n3=0 controls
(9, 243).

**This is the checked statement of claim `reimbayev-order7-counts-two-free-vars`.**
It upgrades a source-backed conclusion from `asserted` to `checked` (exact
integer arithmetic, verified here), while the paper's own derivations from
Figure-1 recoverability remain `asserted` (they are the source's, not re-derived).
The claim block itself lives in (and derives from) the authoritative acquisition
note `research/notes/librarian-order7-acquisition.md`; it now carries
`status: checked` there. This note records the verification and the durable
findings.

**Bearing (unchanged, now checked):** the counting-identity route is closed
through order 7. Free-variable count grows (order-6: one; order-7: two: n3 and
h11). G-n3-positive (forcing n3>=1 at 99) can only be closed by a **global
forced-count obstruction** (line/point-replication ledger), not by any order-<=7
subgraph-count identity. Both controls satisfy n3=0 and exist, so an n3>=1
argument is NOT refutable by them.

## 2. Durable findings stored to disk (Cognee unavailable)

Each is source-backed and most are `checked` in CLAIMS.md. Recorded here so the
next reader that would call recall_memory finds them on disk:

- **Order-7 counting is n3/h11-agnostic (above).** Closes the counting route
  through order 7. (Reimbayev 2511.06572, checked this pass.)
- **Makhnev 1988 Thm 2 conditional:** under n3=0, no srg(99,14,1,2); so any
  putative 99-graph has n3>=1. Mechanism re-derived: forced srg(33,12,1,6)
  subobject, parameter-infeasible by multiplicity integrality (g numerator
  -136 not divisible by sqrt(Delta)=7). Both controls satisfy n3=0 and exist.
  (sourced + re-derived, claim `makhnev99-shorter-proof-integrality`.)
- **n3 pivot:** the 62 order-6 Reimbayev counts and the order-7 counts are all
  (n,k)±c·n3 (resp. + h11); none forces n3>=1; residue n3≡0 (mod 3), admissible
  interval [0,4158] at k=14. (checked, claims `order6-n3-not-forced`,
  `n3-99-forced-at-least-3`.)
- **Five-member family, checked:** exactly (9,4),(99,14),(243,22),(6273,112),
  (494019,994); k=u^2+u+2 with 2u+1 | 63, u in {1,3,4,10,31}. CORRECTS
  problem.md's candidate list (33/513/969 die on multiplicity integrality).
  (claim `integrality-five-members`, checked.)
- **Two positive controls:** rook(3)=srg(9,4,1,2), bvls_graph()=srg(243,22,1,2),
  both oracle-verified (code/out/oracle-selfcheck.md). Every nonexistence
  argument must fail on both. (claims `c4`, `c5`, checked.)
- **Automorphism bounds:** |G| divides 2·3^3·7·11 (Makhnev-Minakova 2004);
  primes subset {2,3} (Behbahani-Lam 2011); 7||G| => Z7, 2||G| => |G||6
  (Cesarz-Woldar 2025, computer-free); no Z6,S3,Z9,E9 (Crnkovic-Maksimovic 2020).
  Triviality of the group is the one open automorphism question. (claims `c3`,
  `aut-aut-orders-consolidated`, asserted-by-source.)
- **Bagchi/BN1988 mu=2 dichotomy does not bite at 99:** needs BOTH k<12λ(λ+3)
  AND k<(λ+1)(λ+2)=6; k=14,22 both fail the second branch. (claimed
  `c6-resolved-no-bite`, `bagchi-bvls-contradiction-resolved`, sourced+reasoned.)
- **Nitpicky but load-bearing:** n3 seed (two disjoint triangles joined by
  exactly 2 edges) is locally consistent at radius 1; earlier CONTRADICTION was
  a lib/localprop.py soundness bug, not an obstruction. (claim
  `n3-seed-locally-consistent-radius1`, checked.)
- **Six-vertex condition is the live differentiator** (Pech 2021 Thm 5.7 proves
  PQ point graphs satisfy the 5-vertex condition — INERT at 99; the 6-vertex
  condition on Pech's 8 PQ types is live). (claim `5vertex-pq-inert-6vertex-live`.)

## 3. Sources that do not help (maintained verdict, unchanged from passes 1-4)

- `brouwer-haemers-srg-chapter.md` — paywalled preview; nothing beyond the SRG
  definition, all already held.
- `makhnev-2013-local-subgraphs-srg-99.md` — paywalled, body absent.
- `zehavi-oliveira-not-conway-99.md` — solves a *different* variant, not the
  problem; a boundary caution, not a route.
- `keramatipour-sat-conway99.md` — reports only SAT's incapability; no
  search-space size, symmetry reduction, or wall-clock; confirms enumeration is
  the wrong method, adds no reportable boundary.
- `bagchi-mu2-correct.md` — WRONG download (pre-Lie paper); do not use. Correct
  Bagchi content resolved in `research/notes/bagchi-mu2-dichotomy-resolution.md`.
- `index.full.md` (sources/), `cesarz-woldar-automorph-conway99.md`,
  `makhnev-1988-lambda1.md` — duplicate landing pages of real content held
  elsewhere.
- All 9 OEIS rows — unrelated/coincidental sequences; `does not help`.
- Behbahani-Lam-Ostergard 2012 and KKO 2011 — concern COMPLETE STSs (block-graph
  family lambda=(v+3)/2, mu=9); the transfer to a partial STS is NOT available.

## 4. Contradictions

No genuine contradiction between sources exists in the library, and none with
recalled memory. The one apparent one — Bagchi/BN1988 "mu=2 => grid or k>=48"
vs the existing BvLS (243,22,1,2) — is RESOLVED (the grid branch needs both
bounds; k=22 >= 6 falls in the escape branch). problem.md's candidate list is
wrong (five-member list won, checked). Cesarz-Woldar's computer-assistance
status differs between arXiv (Frob(21) elimination computer-assisted) and
published (computer-free) — flagged, not a content contradiction.

## 5. What the run still lacks

- A proof forcing n3>=1 (or n3=0) at 99 that is k=14-specific geometry, not a
  counting identity (counting is now closed through order 7).
- Whether the 6-vertex condition holds for a proper PQ point graph (99) on
  Pech's 8 types.
- Whether the (99,14,1,2) incidence p-rank/S-N-F is computable and whether it
  separates 99 from 243 (rank is NOT parameter-determined -- live, task
  `incidence-prank-parameter-determinism`).
- Whether G is trivial (the one open automorphism question).
- A completed exhaustive sub-search with a stated exhaustiveness argument and
  wall-clock boundary inside the triangle geometry.
