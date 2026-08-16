# NEHB14 — The Erdős–Gyárfás conjecture in claw-free graphs (full proof held)

Source: Salehi Nowbandegani, Esfandiari, Shirdareh Haghighi, Bibak, "On the
Erdős–Gyárfás conjecture in claw-free graphs", arXiv:1109.5398v3 (7 Feb 2013);
pub. Discuss. Math. Graph Theory (2013), doi:10.7151/dmgt.1732.
Full text: `research/sources/nehb14-clawfree-3-2k.full.md`.

Answers Hobbs's question whether the Erdős–Gyárfás conjecture holds in
claw-free graphs. This was previously held only as an abstract/landing summary;
the full proof text is now in the library and the statements below were checked
against it.

## What it proves

- **Theorem 1.** Every claw-free graph with δ ≥ 3 has a cycle of length 2^k or
  3·2^k for some positive integer k. (The 3·2^k weakening — not yet the full
  conjecture, but a long way toward it in the claw-free class.) Proof route:
  δ≥3 with no C4 ⟹ an n-hole (Lemma 2); in 4-regular claw-free C4-free every
  edge is uniquely triangulated (Prop 3); Lemma 4 controls the triangles on a
  smallest hole.
- Claw-free δ ≥ 4 with no C4: structural results on non-cut vertices lying on
  cycles (Theorem 5).
- **Cubic claw-free case.** Prop 6: correspondence G ↔ Ĝ between simple cubic
  graphs and simple cubic claw-free graphs without C4 (G is the line graph of Ĝ
  after expanding triangles — actually the reverse construction; Ĝ has |V|/3
  vertices). Corollary 7: if Ĝ has a cycle of length in {2,3,4,6,7,8} then the
  conjecture holds for G.
- **Theorem 9.** Any counterexample to the Erdős–Gyárfás conjecture in cubic
  claw-free graphs has **at least 114 vertices**. Proof: BFS levels from a
  vertex of Ĝ; L1 independent, L2 induces ≤1 edge, etc.; an easy counting gives
  Ĝ ≥ 38 vertices, so G = 3·38 ≥ 114.

```claim
id: nehb14-clawfree-3-2k
statement: Every claw-free graph with δ ≥ 3 has a cycle of length 2^k or 3·2^k; every cubic claw-free counterexample to E–G has ≥ 114 vertices.
hypotheses: claw-free, δ ≥ 3 (general); cubic claw-free (114 bound)
holds-here: yes — settled restricted class, and the nearest-confirmed class on the "2-power or 3·2-power" ladder
status: sourced, proof held in full text
bearing: the 3·2^k gap is the closest settled rung to a prescribed sparse set; the 114 bound is a lower-bound data point for cubic claw-free counterexamples
anchor: research/sources/nehb14-clawfree-3-2k.full.md
```

## For this problem

The 3·2^k weakening is strictly weaker than the target 2^k, but it is the
nearest settled class to the pattern "a prescribed sparse set of lengths" — the
run's own (weakened) problems (WEAKENED.md) sit on this ladder. The 114-vertex
bound for cubic claw-free counterexamples is a strong lower bound for that
subclass, far beyond the general 32.

Quotes the Erdős–Gyárfás original negative belief verbatim (line 52): "we are
convinced now that this is false and no doubt there are graphs for every r every
vertex of which has degree ≥ r and which contain no cycle of length 2^k, but we
never found a counterexample even for r = 3" — CONFIRMS the negative-belief
passage elsewhere attributed to them. Also independently cites the Shauger
K1,m and Daniel–Shauger planar-claw-free results.
