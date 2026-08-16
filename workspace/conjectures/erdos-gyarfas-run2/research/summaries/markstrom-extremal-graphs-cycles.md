# Markström 2004 — Extremal graphs for some problems on cycles

Source: Klas Markström, "Extremal graphs for some problems on cycles in
graphs" (Umeå; PDF cycex.pdf, ~2004). Full text held: [[markstrom-extremal-graphs-cycles.full]].

## Erdős–Gyárfás content (Section 4)

Statement of the conjecture (1995), with Erdős's $100 proof / $50
counterexample prize, attributed.

**The minimal-counterexample structure** (the observation used by Carr):
> "Assume that G is a, edge and vertex, minimal counterexample ... If d(u) ≥ 3
> and d(v) ≥ 3 then {u, v} can not be an edge; if it was then G \ {u, v} would
> be a counterexample with fewer edges than G. Thus a counterexample must
> consist of an independent set V1 of vertices of degree at least 4, and a
> nonempty set V2 = V \ V1 of vertices of degree 3."

So: deg-≥4 vertices form an independent set; all other vertices have degree
exactly 3. This is **proved here**, not merely asserted.

**Verification bounds (computed, this paper):**
- Royle (attributed): all relevant graphs on < 16 vertices have a power-of-2
  cycle → any counterexample ≥ 16 (the "17" in Wikipedia comes from
  counting convention "at least 17 vertices"). Primary statement: Royle
  "generated all relevant graphs on less than 16 vertices and found no
  counterexamples."
- Markström: all cubic graphs on < 29 vertices (V1 = ∅ case) checked for
  cycles of length 4, 8, 16 → no counterexample. Any **cubic** counterexample
  ≥ 29 vertices.
- **Smallest cubic graphs with no C4 and no C8: exactly 4 graphs on 24
  vertices** (Table 3 context). The counts: n=24:4, n=26:23, n=28:251 cubic
  graphs without C4 and C8. Each 24-vertex example contains a 16-cycle (so is
  *not* a counterexample). One of the four is planar.

**Attribution:** "Apart from Shauger's results on claw-free graphs [Sha98,
DS01] there seems to be very little published on this conjecture." (Note this
predates Liu–Montgomery, Sudakov–Verstraëte, the P_k-free results.)

## What it implies here

- The independent-set degree structure is *proved* (status: proved, vs Carr's
  abstract which restates it). This is the anchor the run can cite.
- Verification of the oracle: this run's checker must reproduce that the four
  24-vertex cubic graphs have no C4/C8 but do have a 16-cycle, and that every
  cubic graph < 29 has a 4/8/16-cycle. The Balaji SAT work pushes the general
  bound to 32; both should agree with a correct oracle.
- The four 24-vertex near-misses are the sharpest "local" obstruction data — a
  structural theorem must sit alongside graphs that avoid C4 and C8 but carry
  a C16.

```claim
id: ce-verification-royle-16
statement: Every graph with δ ≥ 3 on < 16 vertices has a cycle of length a power of two (Royle's search); any counterexample has ≥ 16 vertices.
hypotheses: finite simple, δ ≥ 3
holds-here: yes; superseded upward by Balaji (32)
status: catalogued (computer search, attributed to Royle)
bearing: oracle target / lower anchor; Wikipedia's "17" wording
anchor: research/sources/markstrom-extremal-graphs-cycles.full.md
```

```claim
id: ce-cubic-verification-29
statement: Every cubic graph on < 29 vertices has a C4, C8, or C16; any cubic counterexample has ≥ 29 vertices.
hypotheses: cubic, finite simple
holds-here: yes; superseded by Balaji (32)
status: catalogued (exhaustive search via minibaum, checked by program)
bearing: oracle target for the cubic class
anchor: research/sources/markstrom-extremal-graphs-cycles.full.md
```

```claim
id: markstrom-24-vertex-near-misses
statement: There are exactly 4 cubic graphs on 24 vertices with no C4 and no C8; each contains a 16-cycle; one is planar. Counts: n=24:4, n=26:23, n=28:251.
hypotheses: cubic, n ∈ {24,26,28}
holds-here: yes
status: catalogued (computer search)
bearing: oracle regression target; near-counterexample family a candidate the structural picture must survive
anchor: research/sources/markstrom-extremal-graphs-cycles.full.md
```

```claim
id: ce-principality-carr
statement: At least 4/7 of the vertices of a minimal counterexample have degree 3 (Carr refinement of Markström's structure).
hypotheses: minimal counterexample
holds-here: yes
status: asserted (abstract; proof body not held)
follows-from: ce-deg-structure
anchor: research/summaries/carr-predominantly-cubic.md
```
