# Scholar — full-library assimilation pass (at end of attempt 2)

This pass re-read the entire reference library (all 49 source summaries plus the
claim ledger), not to acquire anything new but to verify that every source has
been digested into precise, claim-bearing notes, to fix stale lines, and to
consolidate durable findings. The library is **phase-1 complete** (ROOT.md and
LIBRARY-REPORT.md state this; this pass independently confirms the claim and
summary coverage). No new source acquisition was made and none is warranted.

## What I verified (survey, not re-derivation)

- All 49 summaries under `research/summaries/` are judged. The large majority
  carry a precise `claim` block with hypotheses, holds-here, status, bearing,
  and anchor. The claim ledger holds 104 claims, consistently cross-referenced
  to notes and captures.
- The two canonical controls are grounded and ORACLE-CHECKED: rook(3)=srg(9,4,1,2)
  and BvLS(243,22,1,2); `code/lib.srg.is_srg` verifies both by exact integer
  counting and rejects 14-regular circulant(99,{1..7}) on λ/μ mismatch.

## Corrections made this pass (all summary-level, no derived-file edits)

1. **Closed the 8 unfinished OEIS auto-digest placeholders.** Files
   `oeis_{a000201,a003106,a007494,a097008,a208970,a319859,a327265,a328594}.md`
   each carried a `> Filed by an OEIS lookup, not read` footer. Replaced each
   with a `catalogued, does not help` verdict and one-line reason. These are
   partition/necklace/Wythoff/aperiodic-word sequences unrelated to srg
   feasibility. The family's own vertex counts (9,99,243,6273,494019) are NOT a
   catalogued OEIS sequence (`research/notes/oeis-miss-family-vertex-counts.md`).
   (A218293/A219272 were already closed with the same verdict.)
2. **Makhnev summary: stale "PENDING" oracle line → PASSED.** The primary
   Russian full-text summary said the rook/BvLS condition-(*) check was "PENDING
   tool_builder/coder execution". It has been RUN: `code/out/makhnev-1988-condition-captured.txt`
   (wall 0.59s) shows rook(3) T=6 and BvLS T=891 both pass `is_srg`, both have
   n3=0, both satisfy condition (*) — claim `makhnev-condstar-gate-passed` is
   `checked`. Fixed in both the body and the claim-block status fields.
3. **Makhnev summary residual: Lou–Murin no longer "untraceable".** The note
   claimed the forbidden-9-vertex lead was "still untraceable"; it is in the
   library as the MIT PRIMES-USA 2014 paper
   (`research/summaries/lou-murin-srg991412-2014.md`). Corrected; flagged that
   whether it contains the exact "forbidden subgraph of order 9" claim Reimbayev
   cites is unverified.

## The one ledger-inconsistency I noted (not a contradiction in content)

Claim `5vertex-pq-inert-6vertex-live` is rendered in CLAIMS.md as `asserted`,
but its own claim block (in `research/approaches/pq-2-6-2-classification.md`)
says `status: sourced (primary proof in library; proofs read directly)` and the
fact is independently proved by Pech 2021 Thm 5.7 (full text held). The `asserted`
label is an artifact of the claim block living in an approach file rather than a
summary. Content is consistent; the label understates the evidence. Not worth a
re-file; flagged here so a future reader does not treat it as a true gap.

## Contradiction sweep

I searched every summary for `contradicts:` fields and read the ones that fired.
No genuine contradiction between sources, and none between a source and recalled
memory, exists in the library:
- Bagchi/BN1988 "μ=2 ⇒ grid" vs. BvLS existence: RESOLVED (the grid branch needs
  BOTH k<12λ(λ+3) AND k<(λ+1)(λ+2); k=22≥6 so BvLS falls in the second branch).
  Claim `c6-resolved-no-bite`, `bagchi-bvls-contradiction-resolved`.
- The (85,14,3,2) automorphism result (primes {2} only) vs. 99's {2,3} — not a
  contradiction, an illuminating divergence: the 85-graph is dead with a SMALLER
  group, so automorphism-group size is not the 99 obstruction.
- Wrong-download records (Bagchi, Behbahani–Lam 2011, Östergård–Soicher,
  Bondarenko–Radchenko) are each flagged with a correction note; none leaks
  wrong content into a claim.

## Durable source-backed findings stored this pass (remember_memory)

1. Makhnev 1988 Thm 2 conditional + controls-passed (n3=0 ⇒ no 99; both controls
   n3=0 and exist; 99 has n3≥1).
2. The n3 pivot: all 62 order-6 counts are (n,k)±c·n3; order-6 counting does NOT
   force n3≥1 at 99 (all admit n3=0, residue n3≡0 mod 3, [0,4158]); a forcing
   needs k=14 geometry, not counting.
3. Brouwer–Neumaier 1988 + Bagchi μ=2 dichotomy has no bite at 99; table marks
   (99,14,1) open.
4. The two k=14 nonexistence templates: (57,14,1,4) star-complement and
   (85,14,3,2) segment-enumeration — both confirm local-graph enumeration with a
   stated finite space is the live method; 99's 7K2 local graph is more rigid.
5. Automorphism constraints consolidated (|G| | 2·3³·7·11; primes {2,3}; 7||G|⇒Z7,
   2||G|⇒|G||6; no Z6,S3,Z9,E9; order-11 ruled out by Wilbrink).
6. Pech 2021 Thm 5.7 proves PQ point graphs satisfy the 5-vertex condition —
   INERT at 99; the live rung is the 6-vertex condition on Pech's 8 PQ types.
7. Super-simple 2-(22,4,2) EXISTS (CP-SAT OPTIMAL, 77-block certificate,
   independently verified) — closes the coclique-lift route as NON-OBSTRUCTIVE.
8. Control-checked negatives: five-member integrality list (corrects problem.md),
   outer-design recursion false on BvLS, n3-seed locally consistent at radius 1
   (earlier contradiction was a lib/localprop.py bug).

## What the run still lacks

- No **forcing** of n3≥1 (or n3=0) at 99 that survives the k=14-specific geometry
  requirement; the order-6 identities are n3-agnostic.
- Whether the 6-vertex condition holds for a proper PQ point graph (99) on Pech's
  8 types — the live differentiator the rank-3 controls pass trivially.
- Whether the (99,14,1,2) incidence 2-rank is computable/settled by an actual 99
  system (circular, per the incidence-prank determinism note); rank is NOT
  parameter-determined, so it could separate 99 from 243 in principle.
- The Z7-prescribed-automorphism sub-case is open: CP-SAT is inconclusive there
  (forced-structure-reduction preprint and this run's own automorphism ledger
  agree). Local-enumeration / orbit-matrix + eigenvalue interlacing is the
  suggested next instrument, not more of the same encoding.

## Verdict on the sources that do not help (and why)

- Brouwer–Haemers "Strongly Regular Graphs" chapter: paywalled preview, value
  duplicated; `brouwer-haemers-chapter-no-help`.
- Zehavi–Oliveira "Not Conway's 99-graph": solves a differently-worded variant,
  a boundary caution, not a route.
- Makhnev 2013 local-subgraphs: paywalled, body absent, statement unavailable.
- All 9 OEIS rows: unrelated or coincidental; closed with `does not help`.
- Behbahani–Lam–Östergård 2012 and KKO 2011 STS block-graph results: concern
  COMPLETE STSs, whose block-graph family (λ=(v+3)/2, μ=9) is disjoint from the
  λ=1, μ=2 partial-STS family; the transfer to a partial STS is not available.
- Citation-graph files: frontier leads, correctly not evidence; none names a
  theorem this run lacks.
