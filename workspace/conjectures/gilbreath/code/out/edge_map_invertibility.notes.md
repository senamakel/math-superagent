# Sharpened edge-zero-run lemma: the block interior cannot suppress the edge 2 for its whole erosion life

`code/out/check_edge_zero_run.py` existed with no captured output and checked a
**vacuous** statement: the halved-edge sequence `e_0..e_{n-1}` of a `{0,2}`
block under pure erosion has only `n` entries, so "worst zero-run ≤ 2n" is
trivial, and the only pattern achieving a run of length `n` is the all-zero
block. This note records the sharpened, non-vacuous statement and its proof.

## Setup and notation (all exact integer arithmetic, no floats)

Take a leading `{0,2}` block of unhalved length `n` in row `A_k`, i.e. halved
bit string `h[0..n-1]` with `A_k[1+j] = 2·h[j]`, and suppose the block is
**left alone to erode** (no `(2,4)`-regeneration event fires between rows —
equivalently, the intruder is never `4` while the edge is `2`, or the rows are
read between events). By the proved Rule-90 interior identification
(`rule90-interior-xor`; `research/notes/block_lemma.md`), the halved entry at
the block-edge position after `d` erosion rows (`d = 0..n-1`, block length
then `n-d`) is

    e_d = XOR over j=0..d of [C(d,j) mod 2] · h[(n-1-d)+j],

the Pascal-mod-2 (Rule 90) convolution. `e_d = 0` means the edge reads `0`
after `d` erosion rows, during which **no `(2,4)`-regeneration is possible even
if the intruder is 4** (boundary pair `(0,4)` gives `|0-4| = 4`, erosion
continues — the step law `b_{k+1} ≥ b_k ⟺ (edge,intruder)=(2,4)`).

## Claim: edge-map invertibility bounds structural regeneration-blocking

`edge-interior-invertibility-sharpened`

- **statement:** Over F₂, the halved-edge map `h ↦ e = (e_0..e_{n-1})` is
  linear with matrix `M_n[d][c] = C(d, c-(n-1-d)) mod 2` for
  `n-1-d ≤ c ≤ n-1`, else `0`; in reversed column order `c' = n-1-c` this
  matrix is **unitriangular** (diagonal `C(d,0) = 1`, zeros above), hence
  invertible. Therefore `e = 0 ⟺ h = 0`: **every nonzero `{0,2}` block shows
  edge value 2 at least once during its `n` erosion reads** — the block's own
  interior pattern cannot hold the edge at 0 for the block's whole erosion
  life. Equivalently the longest consecutive run of edge-0 rows is `≤ n-1`
  for every nonzero block (the vacuous `≤ 2n` is replaced by the sharp `≤ n-1`).
- **worst case (sharp):** the bound `n-1` is attained for exactly two patterns
  at each `n` (verified exhaustively): the edge sequences `e = [0^{n-1}, 1]`
  (edge 0 while the block has length ≥ 2, edge 2 only at the final length-1
  read — the pattern `h = [1,0,...,0]`, i.e. unhalved block `[2,0,0,...,0]`)
  and the mirror `e = [1, 0^{n-1}]`.
- **hypotheses:** erosion-only dynamics between reads (no regeneration event
  fires within the stretch); block interior `{0,2}`-valued (true by closure).
- **holds-here:** yes — the real rows' block interiors are exactly this
  object between regeneration events, by the proved Rule-90 interior
  identification and `{0,2}` closure; the lemma is about the operator on
  arbitrary blocks, so it transfers.
- **status: proved** (matrix linear-algebra argument; the determinant-free
  unitriangular argument needs only `C(d,0) = 1`, `C(d,j) mod 2` facts) and
  **machine-checked** on every nonzero block for `n = 1..18` (262,143
  patterns × 3 independent routes agree) and on the unitriangular structure
  for `n = 3..1024`.
- **bearing:** regeneration timing. The step law says an event needs
  `(edge, intruder) = (2,4)`. This lemma is the interior half of the timing:
  the edge *can* be 2 (indeed must be, at least once per block life; worst
  case only at the final length-1 read). It does **not** prove regeneration
  recurs — the intruder-4 timing is the other half, untouched. It refutes the
  structural fear that a bad interior pattern could keep the edge at 0 for
  the whole possible lifetime of a `{0,2}` block.

## Machine checks (three independent routes, all exact)

1. **R1 — Pascal convolution:** `e_d = XOR of C(d,j) mod 2 times h[n-1-d+j]`,
   `comb(d,j) % 2` (math.comb).
2. **R2 — literal dynamics:** build row `[1] + [2·h_i]`, apply `|a-b|`
   erosion `d` times, read the halved edge each step.
3. **R3 — matrix:** multiply `M_n · h` over F₂.

All three routes agree on every one of the 262,143 nonzero patterns
(`n ≤ 18`); worst zero-run for nonzero blocks is exactly `n-1` for every
`n = 2..18`; the two achievers at each `n` are reproduced by
back-substituting the unitriangular system. Unitriangularity: zero violations
for `n = 3..1024`.

## Files

- `code/out/check_edge_zero_run.py` — the original vacuous checker
  (all-pattern `≤ 2n`), executed this cycle: `code/out/check_edge_zero_run.captured.txt`.
- `code/out/check_edge_zero_run_nonzero.py` — first sharpening: nonzero
  blocks only, two routes; captured `code/out/check_edge_zero_run_nonzero.captured.txt`.
- `code/out/edge_map_invertibility.py` — the full proof-check: unitriangular
  structure to n=1024, three routes to n=18, worst-case achievers; captured
  `code/out/edge_map_invertibility.captured.txt` (EXIT_CODE=0).
- Also executed this cycle (written, never run): `code/out/check_A089582_crosscheck.py`
  (run's own generator reproduces OEIS A089582's 105 second-entry terms
  exactly — upgrades claim `oeis-A089582-second-entry-catalogue` from
  "read from a catalogue" to "reproduced by the run's oracle") and
  `code/out/verify_rule90_against_sources.py` (the `|a-b|/2 = (a/2) XOR (b/2)`
  identification re-derived without reading the sources, over `2^8` patterns).