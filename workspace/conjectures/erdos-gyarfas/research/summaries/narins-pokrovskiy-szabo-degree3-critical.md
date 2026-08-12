# Narins–Pokrovskiy–Szabó — Graphs without proper subgraphs of minimum degree 3 and short cycles

Source: https://discovery.ucl.ac.uk/id/eprint/10112658/1/CyclesPaper.pdf (author accepted manuscript)
Published: Combinatorica 37 (2017) 495–519; DOI 10.1007/s00493-015-3310-9
Full text: `research/sources/narins-pokrovskiy-szabo-degree3-critical-pdf.full.md`

## What it is

Studies **degree 3-critical graphs** (following Bollobás–Brightwell): graphs on `n`
vertices with `2n−2` edges and **no proper induced subgraph of minimum degree 3**.
This is exactly the class containing a minimal EG counterexample via Carr's Lemma 0.1
(every proper subgraph of a minimal counterexample has δ≤2; if δ(G)≥3 and no proper
subgraph has min-degree 3, then an `n`-vertex graph has at most `2n−2` edges, and for a
minimal counterexample the "induced" and "non-induced" readings both hold as in EFRS).

Establishes the **Erdős–Faudree–Gyárfás–Schelp (EFRS 1988) picture** and refutes its
central conjecture.

## Key established results

1. **The EFRS conjecture is false.** Constructs an infinite sequence of degree 3-critical
   graphs `G_n` with **no cycle of length 23** (Theorem 1.2). Method: for each even
   "1-3 tree" T (all leaf-leaf paths even length), graph `G(T)` (add two new vertices
   x,y; edge xy; every leaf joined to x and y) is degree 3-critical. Cycles of `G(T)`
   correspond to leaf-leaf path lengths of T, so avoiding one length in the tree avoids
   one cycle length in the graph.
2. **More generally**, degree 3-critical graphs with no cycle of length `2k+3` exist for
   every odd `k≥10` (i.e. missing odd cycles 23, 25, 27, ...), via 2k-avoiding sequences.
3. **Every degree 3-critical graph with n≥6 contains a C6** (Theorem 1.4/Prop 5.1),
   and contains cycles of lengths 3, 4, 5, and at least ⌊log₂n⌋ (Erdős et al.).
4. If the "induced" word is dropped (no proper *non-induced* subgraph of min degree 3),
   the graphs are **characterized** (Theorem 4.1: wheels and gluings of the H-graphs,
   which are **pancyclic**) — so in the strict non-induced class the conjecture holds in
   the strongest form.
5. The shortest cycle length not guaranteed in large degree 3-critical graphs is between
   **7 and 23** (odd cycles only can be avoided; whether even cycles can be avoided is
   open, Problem 6.1).

## Why this matters to the run

The minimal EG counterexample is degree 3-critical-like. This gives a **structural
warning**: degree-3-critical graphs do NOT force all short cycle lengths — in particular
they can miss cycles of length 23, 25, ... So a purely "degree-3-critical ⇒ many cycle
lengths" argument cannot prove EG by itself; the power-of-two obstruction is compatible
with the degree-3-critical class missing long odd cycles. Conversely, even cycle lengths
(4, 6, 8, ...) are much harder to avoid, and C4/C8/C16 avoidance (the run's regime) is a
stronger restriction than what this paper's constructions achieve (they avoid odd cycles,
not powers of two).

The `G(T)` construction (2 new vertices over a 1-3 tree) is a concrete counterexample
template the run should be aware of — but note it produces cycles of many powers-like
lengths from leaf-leaf paths, so it is not a power-of-two counterexample constructor.

## Status

Peer-reviewed (Combinatorica 2017), open-access author manuscript. Read in full here.
Claims below.

```claim
id: EG-degree3-critical-no-C23
statement: There is an infinite sequence of degree 3-critical graphs (n vertices, 2n−2 edges, no proper induced subgraph of minimum degree 3) with no cycle of length 23; more generally with no cycle of length 2k+3 for any k≥10.
hypotheses: degree 3-critical graphs; δ≥3 follows; the "no proper induced subgraph of min degree 3" reading matches EFRS and Carr's minimal-counterexample lemma.
holds-here: yes — the minimal EG counterexample lies in (a slight variant of) this class.
status: proved (Combinatorica 2017, Narins–Pokrovskiy–Szabó)
bearing: No proof can rest on "degree-3-critical ⇒ all short cycle lengths appear"; power-of-two cycles must come from a different structural fact. This is a warning that the run's structural arguments about a minimal counterexample must produce a specific forbidden length (4/8/16), not merely "many cycle lengths".
anchor: research/sources/narins-pokrovskiy-szabo-degree3-critical-pdf.full.md
```

```claim
id: EG-degree3critical-C6
statement: Every degree 3-critical graph on at least 6 vertices contains a C6.
hypotheses: degree-3-critical graph, n≥6.
holds-here: yes (the relevant class for a minimal counterexample).
status: proved (Combinatorica 2017)
bearing: A minimal EG counterexample, being near-degree-3-critical, contains a C6 — consistent with the run's picture (powers of two only excluded, other small cycles abundant).
anchor: research/sources/narins-pokrovskiy-szabo-degree3-critical-pdf.full.md
```
