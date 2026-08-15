# Scholar report — what the new library material establishes for this run

This run's task: read what the research agent added to `research/`, record what
each source actually establishes and what it implies here, store durable
verified findings, flag contradictions, and say which sources do not help.

The library is **large, mature, and already well-digested** by the prior
`scholar-digest.md`. My job was to (a) verify the newest material independently,
(b) hunt for contradictions, and (c) confirm the strongest claims against
captured machine output. The net result: the library is coherent, the
size-bound deliverable through N=11 is real and machine-checked, and I found and
fixed **one genuine internal contradiction** (below).

## The one contradiction found and fixed

**Mycielski edge-count transition: `4e+v` vs `3e+v`.**
The `research/summaries/oeis-mycielski-catalogue-check.md` claim block and the
earlier digest stated the transition as `(v,e) -> (2v+1, 4e+v)`, while citing
the values M(C5)=11v/**20e**, M²(C5)=23v/**71e**, M³=47v/**236e**. Arithmetic
falsifies the `4e+v` form immediately: `4·5+5=25 ≠ 20`, `4·20+11=91 ≠ 71`.
The correct canonical (no-mirror) Mycielski transition is `(2v+1, 3e+v)`, which
reproduces 20, 71, 236 exactly.

Independent confirmation from the run's own captured output:
- `code/out/diag_mycielski.captured.txt`: C5=(5,5,chi3), M=(11,20,chi4),
  M²=(23,71,chi5).
- `code/out/verify_mycielski_k23_notes.md`: "the `4e+v` total in
  `diag_mycielski.py`'s comment is misleading; its code computes the `3e+v`
  canonical form; the counts 20 and 71 only match the canonical form."
- `code/out/verify_mycielski_both_variants.captured.txt`:
  variant A (no-mirror, the run's kernel): 5,20,71,236 ✓; variant B (mirror):
  5,25,111,467 — exactly `4e+v`.

So `4e+v` is the **mirror variant** the run explicitly does not use. I corrected
the oeis-note (3e+v) and left a note in the digest. The OEIS catalogue is
correct (A083329 vertices, A122695 edges); only the transition in the note was
wrong. CLAIMS.md re-derives automatically.

## What the newest sources establish (with implications)

**Graph-product tier — negative control for the construction engine.** The run's
core open question (can combining 4-colourable unit-distance graphs force
chi>4?) sits in graph-product chromatic theory. The primary tier:
- El-Zahar–Sauer 1985: tensor product of two 4-chromatic graphs has chi=4.
- Tardif 2001: chi(G×H) ≥ (1/2)·min{chi_f(G),chi_f(H)}.
- Duffus–Sands–Woodrow 1985: Cartesian max≤chi(□)≤product; tensor ≤ min.
**Implication:** generic product/combination of 4-colourable graphs stays at
chi≤4, so any chi>4 unit-distance construction must get its rigidity from
*geometry* (Minkowski-sum/rotation coincidences), not generic product structure.
Consistent with the measured Moser+Moser=4. All asserted-by-source; the
unit-distance analogue is the run's own open computation.

**Lovász neighborhood-complex theorem (Lovász 1978).** χ(G) ≥ conn(N(G)) + 3, so
conn(N(G)) ≥ 2 would certify chi≥5. The `neighborhood-complex-topological`
approach is **refuted** as a 5-certifier (hard homotopy-triviality; value capped
at chi=3 on the triangular lattice), but the theorem is a real, correctly-stated
source. Bearing: a cheap negative filter only.

**Hoffman eigenvalue bound.** χ ≥ 1 − λmax/λmin, general graphs, polynomial.
This is the cheap warm-up/filter of the adopted `lovasz-theta-vector-chromatic`
route: RHS>4 on a constructed UDG would certify chi≥5 polynomially. The value on
Moser / Moser+Moser / any Minkowski sum is a **computation, not a lookup** —
still open (REQUESTS row).

**Citation-graph notes (Braun–Vega 2020; Homma–Maehara 1990; Roth 1981; de
Bruijn–Erdős 1951 cited-by).** These are bibliographic/cited-by lookups, not
read full texts; each carries a claim block flagged `asserted` (abstract only).
- Braun–Vega: Hajós-type constructions + S¹-wedge summands in neighborhood
  complexes. Only corroborates the two already-refuted abstract-graph
  approaches; no geometric/constructive leverage. **Does not help forward.**
- Homma–Maehara 1990: companion of Maehara 1991; the key caution is part (iii) —
  algebraicity of coordinates is necessary but **not sufficient** for low
  chromatic number. Consistent with the exact-arithmetic discipline.
- Roth 1981: bibliographic only (framework rigidity); already captured by
  `maehara`/`kempe-universality`. **Does not help.**
- de Bruijn–Erdős 1951 cited-by: no statements, only citation rows; nothing to
  digest. **Does not help.**

**OEIS Mycielski catalogue (A083329 vertices, A122695 edges).** Confirms the
run's verified construction values (5/5, 11/20, 23/71) under the corrected
`3e+v` transition. Status `catalogued` — good evidence the values are right, no
evidence about why; the reproduction script exists.

## Strongest verified result (re-confirmed, already on disk)

**Every unit-distance graph in R² on at most 11 vertices is 4-colourable; every
5-chromatic unit-distance graph has at least 12 vertices.** Three machine-checked
steps (`code/out/census-kernel-n11-result.md`): sharp-critical-degree
(5-critical subgraph, min-degree≥4), sharp-nbhd-local (K4-free, K2,3-free,
nbhd-maxdeg≤2, exact symbolic certificate), sharp-kernel-4color-n11 (228 kernel
members all 4-colourable, exhaustive over 28 residues of `nauty-geng 11 -d4`).
**This is the reachable GOAL.md deliverable at its best verified extent.** It
survived all refutation attempts on disk (TPTP false-positive; Mycielski kernel
counterexample fails K2,3-freeness).

## The dead-end that matters most

**The Mycielski family cannot supply the needed base graph.** M^k(C5) contains a
K2,3 (vertices 0,2 share {1,6,12}) for every k≥2, and every UDG is K2,3-free.
So M^k(C5) is not unit-distance realizable for k≥2 — a pure geometric
disqualification, no colouring oracle needed. This **closes a whole construction
direction** that other sources gesture at (Mycielski raises chi), and it is why
the forced-pair crux (`G-forced-pair-exists`) still needs a *richer rigid
4-chromatic UDG*, not the abstract Mycielski cores.

## What the run still lacks (gaps, unchanged)

- The general chromatic effect of **spindling** (REQUESTS OPEN).
- Whether **Minkowski sums of 4-colourable UDGs can ever raise chi above 4**
  (the computation).
- Pushing the size-bound census past N=11 (N=12 is a scaling question).
- The exact 7-colour hex-tiling margin (to derive, not fetch).
- Hoffman ϑ(Ḡ)/Hoffman eigenvalue value on constructed UDGs (a computation).

## Sources that do not help

- Braun–Vega 2020, Roth 1981, de Bruijn–Erdős cited-by list — bibliographic /
  already-covered / refuted-direction corroboration. Do not re-read.
- Kempe universality (technique only, no chromatic statement), totally-unfaithful
  UDGs (opposite direction), Szemerédi–Trotter incidence/extremal (bounds
  counts, not chromatic numbers; steer toward algebraic constructions only).

## Verification status of what I added

- The Mycielski `3e+v` correction: verified against three captured outputs
  (`diag_mycielski`, `verify_mycielski_k23_notes`, `verify_mycielski_both_variants`).
- Size-bound N=11: re-confirmed from captured outputs on disk (not re-derived
  here; already `checked`).
- All new sourced claims recorded `asserted-by-source`; none machine-checked by
  me. Durable findings stored in Cognee via `remember_memory`.
