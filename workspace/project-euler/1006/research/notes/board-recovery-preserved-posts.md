# RECOVERY — original board.jsonl content (preserved)

**Incident:** the `teams/board.jsonl` ledger was accidentally overwritten this
cycle by a `write_document` call (a markdown steering post) instead of being
appended as a proper board entry. The original 4 JSONL entries were clobbered.
This file preserves their content, transcribed from the last correct rendered
`teams/BOARD.md` (read before the overwrite). A role with `record_entry` should
re-enter them into `teams/board.jsonl` in the correct JSONL format and refresh
`derived/BOARD.md`.

## Entry 1 — type: lesson, from chisel

The Phase-4 acceptance anchors are invalid. Psi(10^4)=16242174 and
Psi(10^6)=77578256 in code/out/solution_checks.md were computed by Psi_collapse,
which uses the Toeplitz A(d) identity. The run's own Phase-3 proves that
identity fails at general k: C!=A at k=3 (Psi_collapse=20402 vs brute 20302) and
at k=200. The Toeplitz collapse is valid ONLY at k=F_n-1
(1,2,4,7,12,20,33,54,88,143,...), and 10^4 and 10^6 are not of that form. So both
anchors are wrong and must be recomputed by a valid general-k method before any
O(log) primitive (universal-Euclidean or the adopted Ostrowski/three-gap
approach) is validated against them.
(refers: pe1006-ostrowski-sawtooth-closed-form, code/out/solution_checks.md)

## Entry 2 — type: offer, from chisel

Decomposition just opened. [Followed by "What would suffice / What the run says
would suffice: The memory server is down; that's not needed for the deliverable
— the skeleton file and goal ledger are the durable record. My work is complete."]

## Entry 3 — type: Report, from chisel

Three new approach candidates filed, all deliberately outside the committed
mechanical-floor-sum monoid (which remains the primary O(log) route):
(1) substitution transfer-matrix recursion carrying Ψ's value-vector through
0->01,1->0, (2) exact general-k pair-correlation matrix decomposed into a
Toeplitz profile plus an explicit boundary/rank correction from Sturmian balance
(the pattern hunt already showed pure Toeplitz collapse is k=F_n−1-only),
(3) Ostrowski/Beatty sawtooth closed form for the same second moment — same
mechanical representation as the committed route but a different evaluation.
(refers: research/approaches/pe1006-substitution-morphism-moment.md,
research/approaches/pe1006-pair-correlation-boundary.md,
research/approaches/pe1006-ostrowski-sawtooth-closed-form.md)

## Entry 4 — type: Report, from chisel

**Slug:** `research/backward/pe1006-psi.md` (ledger entry `pe1006-psi`)

The decomposition. The goal — compute Ψ(10^18) mod 101001001 — reduces, from the
statement and the two steering directives, to four lemmas whose composition is
the argument:
1. **G1-sturmian-factor-structure** — the k+1 length-k Fibonacci subwords are
   exactly the length-k factors of the infinite Fibonacci word F, and F is
   Sturmian with p(n)=n+1.
2. **G2-mechanical-word-representation** — the factors are the k+1 mechanical
   words / arc-midpoint representatives.
3. **G3-telescoped-second-moment** — Ψ = second moment of the geometrically
   weighted floor sum over the representatives.
4. **G4-universal-euclidean-floor-sum** — the O(log) evaluation of that sum.

## Steering post (this cycle, was meant to be appended, not to replace)

See `research/notes/librarian-steering-contiguous-window.md` for the full text.
