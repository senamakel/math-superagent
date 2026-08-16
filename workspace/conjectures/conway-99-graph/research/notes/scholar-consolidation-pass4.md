# Scholar consolidation — pass 4: provenance, where-else, and the shape of the live attack

Three prior scholar passes have digested the library thoroughly (passes 1–3 in
`scholar-digest-pass.md`, `-pass-2.md`, `-pass-3.md`; the claims ledger in
`research/CLAIMS.md` is full and well-formed). Recall (Cognee) is down across
every attempt this session (404 NoDataError, reported identically by every
prior pass), so this pass verifies against the on-disk full texts rather than
recall, and does **not** retry Cognee.

This pass answers the direction's specific questions, verifies the two flags
it raised, and locates where each source sits. It adds no new source (the
library is CLOSED per ROOT.md).

## 1. Where the Berlekamp–van Lint–Seidel graph lives in provenance

`srg(243,22,1,2)` is primary-established by Berlekamp–van Lint–Seidel 1973 and
van Lint's 1975 survey (five-member list, `research/sources/van-lint-perfect-codes-survey-1975.full.md`,
claim `five-member-list-vanlint1975`). Its construction is fully explicit:
the coset graph of the perfect ternary Golay code — a 5×11 parity-check H,
243 cosets in F₃¹¹, adjacent iff syndromes differ by a unit column, spectrum
22¹·4¹³²·(−5)¹¹⁰, vertex- and edge-transitive (claim `wikipedia-bvls-construction`).

**Why this answers the direction's provenance concern:** the run's oracle
`lib.srg.bvls_graph()` reconstructs this graph from the explicit H, and an
independent Cayley-graph build on Z₃⁵ cross-verifies it
(`code/out/check_bvls_cayley.py`). So using BvLS as a control does **not**
depend on the classification of SRGs or any search outcome — it is built from
the code and verified exact. The direction's worry ("would a counterexample
need the classification?") is answered: BvLS is a *constructed, verified*
witness independent of any classification theorem. Its existence is a
constructed fact, not an assumption.

## 2. The automorphism-order-9 concern — resolved, and the "nine origins" framing corrected

The direction worried that "nine origins for automorphism-group sizes ring
false" and that a group of order 9 having one subgroup of each order argued
for "many 9-cycles." The library's actual claims are **stronger and cleaner**
than any "nine origins" framing, and the order-9 case is explicitly handled:

- Behbahani–Lam 2011 (orbit-matrix, computer-assisted): prime divisors of
  |Aut Γ| ⊆ {2,3}; every order-3 automorphism is fixed-point-free (Thm 4.14 of
  Behbahani 2009 PhD thesis is the primary statement).
- Crnković–Maksimović 2020 (full PDF §7 in library, orbit-matrix with stated
  exhaustive search space): **no** automorphism group Z₆, S₃, Z₉, or E₉.
  For Z₉/E₉ the unique orbit distribution is (0,0,11) with a single orbit
  matrix (diagonal 4, off-diagonal 1); it refines to no Z₃ ≺ group /
  yields no SRG. Net: |Aut Γ| = 2^a·3^b with b ∈ {0,1}. (claim `aut-cm-2020`,
  full mechanism in `research/summaries/crnkovic-maksimovic-full-pdf.md`.)
- Cesarz–Woldar 2025: if 7|G| then G≅Z₇; if 2|G| then |G||6; no order-14
  automorphism (claim `aut-cw-2025`, computer-free in published form; arXiv
  Frob(21) elimination computer-assisted — flagged).

So the "nine origins" framing is not the library's claim; there is no
order-9 (Z₉) or E₉ group, and the surviving candidate groups are at most
Z₂, Z₃, Z₆, S₃, Z₇ (all modulo the divisibility bound). Whether G is trivial
is the one open automorphism question.

## 3. Where-else and what's-there: the settled neighbouring objects (the direction's request)

The family srg(v,k,1,2) has exactly five feasible members
(claim `integrality-five-members`, checked), and the constrained-neighbour
distribution is now mapped:

| parameters | existence | why / status | relation to 99 |
|---|---|---|---|
| (9,4,1,2) rook's / Paley(9) | EXISTS (checked) | 3×3 lattice; spectrum 1⁴·−2⁴; n3=0 | positive control; local 3K₂ degenerate |
| (33,8,1,2) | does NOT exist (checked) | eigenvalue-multiplicity integrality (2k−(v−1)=−16 ∤ 5) | spectral mechanism cannot transfer |
| (99,14,1,2) | OPEN (catalogued `?`) | the problem | — |
| (243,22,1,2) BvLS | EXISTS (checked) | coset graph of ternary Golay code; 4¹³²·−5¹¹⁰; n3=0 | positive control; k=22, vertex-transitive |
| (6273,112,1,2) | open (integrality passes) | later member | out of reach |
| (494019,994,1,2) | open (integrality passes) | later member | out of reach |

**Constrained λ=1 / k=14 precedents** (the "where-else what's-there" the
direction asks for — the closest settled objects and their mechanisms):

- `srg(57,14,1,4)` does not exist (Wilbrink–Brouwer 1978/1983, primary in
  library). **Same local 7K₂ windmill geometry as 99**, only μ differs (4 vs 2).
  Proof machinery: Lemma-1 counting inequality + coclique bound (equality ⇒
  2-(v,K,μ) design). Transferable to 99: local structure and both lemmas hold
  verbatim; the 99 coclique value is the specific number 22 (claim
  `coclique-bound-closed-form`, checked).
- `srg(85,14,3,2)` does not exist (Shpectorov–Zhao 2025, arXiv preprint, NOT
  peer-reviewed, `shpectorov-zhao-85-nonexists-template` marked
  **unchecked/asserted**). Method: local subgraph cubic on 14 vertices → 478
  segments in 4 types → exhaustive local case analysis against λ=3, μ=2 and a
  34-dim Euclidean representation. This is the *closest successful
  local-configuration-enumeration template* to 99, but λ differs (3 vs 1), so
  the local graph is 14-vertex cubic (39 good graphs) rather than the rigid
  7K₂ of the λ=1 case.
- `srg(19,6,1,2)` does not exist, by a spectrum-free local argument
  (Reimbayev, claim `reimbayev-19612-combinatorial-proof`, asserted).

## 4. What the sources establish that bears most on the live attack

The **n₃-pivot** is the run's single most load-bearing live line, and it is now
source-grounded end to end:
- Makhnev 1988 Thm 2 (primary Russian full text in library, claim
  `makhnev1988-condstar-theorems`, status **sourced**): under condition (*)
  [= n₃=0], no srg(99,14,1,2) exists. The mechanism builds an intermediate
  srg(33,12,1,6) from a triangle's closure (39 points) and its 60 exterior
  points, which is μ=6>3, contradicting Thm 1. Both controls rook(3) and BvLS
  satisfy (*) with n₃=0, so the n₃≥1 case (not excluded by the theorem) is the
  only escape — and neither control then refutes it (both are n₃=0).
- Reimbayev's hexagon lower bound (claim `reimbayev-hexagon-bound-n3-pivot`):
  the bound is attained iff n₃=0; both controls attain it (checked, exact C₆
  counts: rook=6, BvLS=4,980,690 = closed form). **So n₃=0 is family-realizable**,
  and the pure hexagon count cannot distinguish 99. This is the trap the run
  already named: 243 attains the bound, so the equality branch predicates
  nothing contradictory.
- Order-6 counting does NOT force n₃≥1 at 99 (claim `order6-n3-not-forced`,
  checked): all 62 order-6 counts admit n₃=0.
- The n₃ seed (two disjoint triangles joined by exactly 2 edges) is **locally
  consistent at radius 1** (claim `n3-seed-locally-consistent-radius1`,
  checked): the earlier "CONTRADICTION" was a soundness bug in
  `code/lib/localprop.py`, now superseded. There is no local obstruction at
  this radius; the next question is at what radius (if any) the seed stops
  extending.

## Sources that do not help, and why (maintained, from passes 1–3)

- `brouwer-haemers-srg-chapter.md` — paywalled landing page only; nothing
  beyond the standard definition.
- `makhnev-2013-local-subgraphs-srg-99.md` — paywalled, body absent.
- `vanlint-brouwer-srg-partial-geometries-1984` — garbled OCR, do not cite.
- `zehavi-oliveira-not-conway-99.md` — solves a *variant*, not the problem.
- `keramatipour-sat-conway99.md` — no reportable boundary; confirms
  enumeration is the wrong method.
- `bagchi-mu2-correct.md` — wrong paper (pre-Lie); correct Bagchi content
  resolved in `research/notes/bagchi-mu2-dichotomy-resolution.md`.
- `index.full.md` (under sources/) and `cesarz-woldar-automorph-conway99.md`,
  `makhnev-1988-lambda1.md` — duplicate landing pages of real content held
  elsewhere.

## Contradictions / corrections recorded

- **Bagchi / BN1988 μ≤2 dichotomy** (the one live contradiction, now resolved):
  the grid conclusion needs BOTH k < 12λ(λ+3) AND k < (λ+1)(λ+2)=6; k=14 fails
  the second branch, as does k=22 for BvLS. `bagchi-bvls-contradiction-pending`
  is superseded by `c6-resolved-no-bite` and `bagchi-bvls-contradiction-resolved`.
  No actual contradiction with the existing BvLS graph.
- **problem.md's candidate list (33, 513, 969)** is wrong; the five-member list
  won (claim `integrality-five-members`, checked).
- **Cesarz–Woldar computer-assistance status** differs between arXiv (Frob(21)
  elimination computer-assisted) and published version (reports computer-free);
  flagged in claim `aut-cw-2025`.

## Gaps that remain genuinely open (for the run, unchanged and live)

1. **Existence of srg(99,14,1,2)** — open; no 9/243-surviving nonexistence
   claim exists (Brouwer marks `?`).
2. **Proving n₃≥1 at 99** — would defeat the Makhnev route; the seed extends
   locally at radius 1, so the open question is at what radius it stops
   (task `radius-one-more-shell-enumeration`, paused by directive 16 until
   solution.md is written).
3. **Whether G is trivial** — the only surviving automorphism uncertainty.
4. **Shpectorov–Zhao (85,14,3,2)** — the closest k=14 template, but an
   un-refereed preprint whose enumeration the run has not re-verified; its
   transfer to λ=1 is untested.
5. **Behbahani–Lam–Östergård 2012** full text paywalled; two 4-vertex SRG
   families' spectra unknown (relevant to the triangle geometry).

## Durable findings to store (see remember_memory calls)

The source-backed, verified claims below (all in CLAIMS.md, several
`checked`) are the ones worth re-storing given the recall outage: the five
member family and 33's spectral exclusion; the two positive controls and
their constructions; the automorphism bounds (with the Z₉/E₉ exclusion and
the Cesarz–Woldar computer-assistance flag); the Makhnev n₃=0 conditional
and the fact that n₃=0 is family-realizable (both controls attain it); the
coclique bound value 22 at 99 with its closed form; the Bagchi/BN1988
dichotomy resolution; and the fact that the n₃ seed is locally consistent at
radius 1 (the earlier contradiction was an engine bug).
