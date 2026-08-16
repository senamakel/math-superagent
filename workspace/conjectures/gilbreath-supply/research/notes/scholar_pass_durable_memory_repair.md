# Scholar pass: durable-memory repair + library coverage confirmation

Author: scholar. Date: this run.

## What this pass found

The reference library was **already comprehensively digested** by prior scholar
passes: every one of the ~30 sources in `research/sources/` has a bounded,
claim-block-carrying digest in `research/summaries/`, and the claim blocks are
re-derived into `research/CLAIMS.md` (63 claims), the ladders into `WEAKENED.md`,
approaches and their refutations into `APPROACHES.md`, and the open state into
`ROOT.md`/`FRONTIER.md`/`REQUESTS.md`. There was **no under-digested source**:
the `citations_w*` files are citation-graph leads (explicitly flagged "not read —
a lead, not evidence"), the `odlyzko_gilbreath` page is a leads list, and the
four `oeis_*` files are each marked "does not help SUPPLY". The wrong-arXiv
overwrites are recorded in `sources/DELETED_wrong_arxiv.md`.

## The defect found and fixed

`recall_memory` returned **404 "No data found in the system" 15 times** — the
Cognee durable memory was **empty**, so every source-backed finding lived only
in workspace files and would NOT survive across runs. `remember_memory` works
(stores return note IDs). This pass stored the load-bearing, verified,
source-backed findings into durable memory as ~20 notes. The recall-side 404 is
a backend issue outside this run's control; the *storage* side now exists so a
run with working recall can retrieve it.

## The load-bearing durable findings stored

- SUPPLY definition + linearisation ν₂ = wt(Φ_n h) and measured c≈0.49.
- Why the mod-4 switch-density reduction is a dead end (ABGS §9, Lau — parity
  barrier, L-function-inaccessible; equal-residue side (Shiu/Maynard/BFTB/
  Freiberg) is the wrong direction) — the entire justification for attacking the
  fold.
- The five closed doors and the unifying obstruction (no 'h is complicated'
  hypothesis works).
- PROVED: rank Φ_n = n−2, nullity 2, ker=span(even-alt,odd-alt), surjective,
  every image has 4 preimages, wt exactly Binomial(n−2,1/2) for uniform h.
- The Lucas-mixing weakest-input candidate (Pivato–Yassawi Thm 7.1) and its
  missing finite-prefix transfer — the single largest open technical tool.
- Measured (NOT proved) N=40000 second-moment / dip-sparsity / rising-tail-min
  picture, and the sharpest open problem (s2_N→0 or finite exceptional set).
- The canonical oracle guard values (ν₂(53)=18, ν₂(64)=27, ν₂(4000)=1975,
  μ_4000=0.497259) and the grounding resolution (floored range k∈[2,n−1]).
- Refutations: Walsh/subset-sum bound (Φ's geometry alone cannot force high
  weight — witnesses in its own admissible class), Kummer 2-adic valuation
  lift, Mahler contrapositive, entropy-neither-nor.
- The Walsh-side uncertainty bounds (Meshulam, Tao, Donoho–Stark) as DIRECTIONAL
  only; Bacher/LOS with holds-here and conjecture caveats; the ABGS-vs-LOS
  non-factual contradiction.

## What this pass added

Nothing new was *derived* — the prior passes had already closed the approaches
and settled the classes. The value of this pass was (a) verifying complete
coverage, (b) verifying the ABGS↔LOS contradiction and the Rampersad–Wiebe
overstatement correction are the only two flagged clashes, and (c) making the
findings durable so the run is no longer at risk of losing its library to an
empty memory store.
