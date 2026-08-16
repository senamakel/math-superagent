# Bensmail 2016 — On q-power cycles in cubic graphs (FULL TEXT NOW HELD)

Source: J. Bensmail, "On q-power cycles in cubic graphs", Discuss. Math.
Graph Theory 37(1):211–220 (2017), doi:10.7151/dmgt.1926. The **complete
paper** is at [[bensmail-q-power-construction.full]] (bibliotekanauki.pl PDF —
different from the mislabeled arXiv 1508.05567 file, which is unrelated and must
not be cited).

## What it establishes (with proofs — all constructions explicit)

A q-power cycle is a cycle of length q^k (k ≥ 1; the paper's notation; Erdős–
Gyárfás is q=2, and a simple graph's minimal q-power cycle consistent with
simplicity is 4 = 2^2, which is the k≥2 convention elsewhere).

Constructions, all starting from an **internally cubic tree** (all non-leaf
vertices degree 3, arbitrarily large) made cubic by attaching edge-gadgets
(replace an edge; ends degree-1) or vertex-gadgets (replace a degree-3 vertex;
three ends degree-2) so that the original tree's leaves remain articulation
vertices. Hence the only cycles lie in the gadgets, with controlled lengths.

- **q ≥ 6 (Thm 9):** edge-gadget with k ≥ 1 columns; cycles of H lie in
  {3,…,2k+2} ∪ {3k+9,…,14k+21}. Pick k so q ∈ {2k+4, 2k+5}; then no q-power
  cycle (q ∉ L and q² > 14k+21). Arbitrarily large **planar cubic** graphs.
- **q = 5 (Thm 14):** vertex-gadget with {t_i,t_j}-paths lengths in {6,7,8},
  G′ cycles in {2,5}; cycles of H in {3,4} ∪ {14,…,18} ∪ {35,…,45}. No 5-power
  cycle. Arbitrarily large planar cubic.
- **q = 4 (Thm 18):** edge-gadget; cycles of H in {3} ∪ {5,…,15}. No 4-power
  cycle. Side effect for q=2: this planar cubic family's 2-powers among
  {3}∪{5..15} are just 8=2³ (neither 4 nor 16), so its only 2-power cycle is
  length 8.
- **Section 4 (Fig 8):** constructions modified to give arbitrarily large
  planar cubic graphs whose all 2-power cycles are **4-cycles only** or
  **8-cycles only**. The note states these give 2-power cycles of length an
  odd power of 2 in the q=4 case.
- **q = 3 (Thm 22):** edge-gadget with cycles in {4,6,8}, {t1,t2}-paths in
  {13,…,25}; H cycles in {4,6,8} ∪ {13,…,25}. No 3-power cycle. Arbitrarily
  large planar cubic.
- **Section 4 / Figure 8:** constructions modified to give arbitrarily large
  planar cubic graphs whose all 2-power cycles are **4-cycles only** or
  **8-cycles only**. Explicitly asks whether, for larger 2^k > 8, there are
  infinite families of cubic graphs whose all 2-power cycles have length 2^k.

## What it implies here

This is the **strongest known near-counterexample behaviour**, now from the
full primary text (previously held only as abstract/secondary). Any structural
argument for the conjecture must survive: there are arbitrarily large cubic
(and planar cubic) graphs whose only 2-power cycle has length 4 or 8. So the
conjecture's content is precisely "at least one 2^k-cycle exists" — not "2-power
lengths are plentiful" — and a proof cannot use any unboundedness of 2-power
lengths in cubic graphs. It is fully consistent with the 32-vertex bound (these
graphs are large) and with Carr's predominantly-cubic picture (they are cubic).
The paper's closing question — for each 2^k > 8, are there infinite cubic
families whose only 2-power cycle is that length — is a live lead for what a
counterexample would have to look like.

```claim
id: bensmail-q-power
statement: For every q ≥ 3 there are arbitrarily large (planar) cubic graphs with no q-power cycle; for q = 2, arbitrarily large planar cubic graphs whose all 2-power cycles have length 4 only or 8 only.
hypotheses: cubic graphs, q ≥ 2
holds-here: yes for q=2 — the E-G near-misses live in the cubic (even planar) class
status: proved (full construction held)
bearing: any structural theorem must permit cubic graphs whose only 2-power cycles have length 4 or 8; proof cannot rely on unbounded 2-power lengths in cubic graphs
anchor: research/sources/bensmail-q-power-construction.full.md
answers: whether-large-cubic-can-limit-2power-lengths (yes)
```

```claim
id: bensmail-open-question
statement: Bensmail asks whether, for every 2^k > 8, there is an infinite family of cubic graphs whose all 2-power cycles have length exactly 2^k.
hypotheses: cubic graphs, 2^k > 8
holds-here: yes — the canonical shape a potential counterexample family would take
status: asserted (question, not result)
bearing: target for a structural impossibility: good evidence against this would be showing the only possible 2-power lengths in cubic graphs are 4 and 8
anchor: research/sources/bensmail-q-power-construction.full.md
```
