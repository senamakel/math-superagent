# Scholar digest — pass 5: independent arithmetic re-verification and durable-memory repopulation

Cognee recall is down session-wide (404 NoDataError on every `recall_memory` /
`recall_scratch`), but `remember_memory` writes land (they return note IDs).
Prior passes (digest passes 1–4, consolidation pass 4) documented the same
outage and deliberately stopped retrying recall. This pass therefore verifies
against the on-disk captures and full texts, and re-stored the verified,
source-backed findings durably.

## What this pass independently re-verified (by hand, not a fresh run)

I have no execution tool this session, so I independently re-derived the
eigenvalue-multiplicity formula and checked it against every capture row,
rather than re-running programs.

For srg(v,k,λ,μ), eigenvalues k,r,s with roots of x²−(λ−μ)x−(k−μ), Δ=(λ−μ)²+4(k−μ),
multiplicities f=(v−1+g)/... :
g = ½[(v−1) − (2k+(v−1)(λ−μ))/√Δ], f = (v−1) − g.
For (λ,μ)=(1,2), Δ = 4k−7.

Checked against `code/out/check_srg33_12_1_6.captured.txt`:
- (33,12,1,6): Δ=49, 2k+(v−1)(λ−μ)=24+32·(−5)=−136, not ÷7 → **INFEASIBLE** [the Makhnev forced subobject]. ✓
- (27,10,1,5): g=6, f=20, feasible (Thm 1 exception). ✓
- (99,14,1,2): 2k+(v−1)(λ−μ)=28+98·(−1)=−70, ÷7=−10; g=½[98−10]=44, f=54. ✓ matches Brouwer 3^54,−4^44.
- (243,22,1,2): g=110, f=132. ✓
- (33,8,1,2): −16 not ÷5 → INFEASIBLE. ✓

All rows of the integrality table reproduce by my own derivation, confirming
the five-member family (9,4),(99,14),(243,22),(6273,112),(494019,994), the
divisor-63 characterization (2u+1 | 63), and 33/513/969's spectral exclusion.

Also re-checked the n3/Makhnev captures (`makhnev-1988-condition-captured.txt`:
condition (*) = n3=0 holds on BOTH controls, rook T=6 {3:6}, bvls T=891
{0:133650,1:240570,3:8910}; both mu=2≤3 so absorbed by Thm 1's mu≤3 branch).
The capture self-consistency is exact.

## Durable memory repopulated (remember_memory, all verified/source-backed)

Stored (note IDs in the write receipts): the five-member family + 33's
integrality exclusion; the Makhnev 1988 Thm 2 n3=0 conditional + the shorter
integrality proof of the 99-case (srg(33,12,1,6) infeasible); the order-6
counting result (n3 NOT arithmetically forced, 1≤n3≤4158 sharp bounds); the
n3=0 finding across the four classical λ=1 SRGs + absence of a μ=2 n3≥1
control; the forced-structure reduction to the 12-regular/84-vertex outer
graph (+ the preprint's 68%/69.43% circulant scores and undecided Z_7 case);
the resolved Bagchi/BN1988 μ=2 dichotomy; the local-consistency result (seed
extends at radius 1, stable radius-6 fixpoint, no local obstruction at any
radius); the automorphism bounds; the C3 triangle-graph controls; the
G-reduce non-recursion negative; the not-vertex-transitive result; the
localprop false-positive retraction; and the local-enumeration templates.

## Contradictions / corrections surfaced (all already on disk, confirmed)

- problem.md's candidate list (33, 513, 969) is wrong — all excluded by
  multiplicity integrality; five-member list won.
- Bagchi/BN1988 μ=2 "grid or k≥48" naive reading contradicted the existing
  BvLS; resolved by restoring the k<(λ+1)(λ+2)=6 second branch.
- The earlier n3_local_propagation "CONTRADICTION" was a localprop.py
  soundness bug (a-v=0 AND b-v=0 instead of NOT(a-v AND b-v)); capture is
  SUPERSEDED, seed is locally consistent.

## Sources that do not help (maintained)

`brouwer-haemers-srg-chapter` (paywalled, nothing beyond definition),
`makhnev-2013-local-subgraphs-srg-99` (paywalled, body absent),
`vanlint-brouwer-srg-partial-geometries-1984` (garbled OCR),
`zehavi-oliveira-not-conway-99` (solves a variant), `bagchi-mu2-correct`
(wrong download), `keramatipour-sat-conway99` (no reportable boundary),
duplicate landing pages (index.full, cesarz-woldar-arxiv dup, makhnev-1988-lambda1).

## What the run still lacks

1. Existence of srg(99,14,1,2) — open (Brouwer `?`, no 9/243-surviving claim).
2. Proving n3≥1 at 99 — would settle via Makhnev; the seed extends locally,
   so the open question is at what radius (if any) it stops — bounded
   enumeration on one more shell (task `radius-one-more-shell-enumeration`),
   NOT CP-SAT.
3. Whether G is trivial — the only surviving automorphism uncertainty.
4. Shpectorov–Zhao (85,14,3,2) is un-refereed and its enumeration not
   re-verified here; transfer to λ=1 untested.
5. **Durable-memory recall is down this session** — Cognee writes land but
   every recall returns 404. This means cross-run memory is not currently
   readable by agents, even though the writes persist. Worth confirming the
   backend before a future run depends on recall.
