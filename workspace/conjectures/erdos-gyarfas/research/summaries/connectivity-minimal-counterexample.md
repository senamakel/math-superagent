# Connectivity (2-connectedness / cut vertex) of an Erdős–Gyárfás minimal counterexample

> Question: does the literature state or prove ANY connectivity property
> (especially 2-connectivity, or absence of a cut vertex) for a minimal
> counterexample to the Erdős–Gyárfás conjecture (min order+size, δ≥3, no
> cycle of length a power of two)? Is a proof of 2-connectivity genuinely new,
> and what is the countervailing evidence (1-connected near-counterexamples)?

**Verdict up front: NO. No paper states, proves, or asserts any 2-connectivity,
3-connectivity, cut-vertex, blocks, edge-connectivity, or ear-decomposition
property of a minimal counterexample. A proof of 2-connectivity (equivalently
"no cut vertex") would be genuinely new.** This is established by full-text
reading of every EG source in this library plus multiple fresh literature
searches, and it is consistent with a standing 1-connected warning in Royle's
own relaxation note. Full detail lives in the companion librarian digestion at
`research/summaries/connectivity-girth-minimal-ce.md` (source-by-source quote
extraction) and `research/summaries/novelty-check-connectivity-triangles.md`
(claims ledger `EG-no-connectivity-result`).

---

## 1. Complete answer: no connectivity statement is proved or asserted

### Primary sources read in full (all in `research/sources/`)

1. **Avery Carr, *Every Minimal Counterexample to the Erdős–Gyárfás Conjecture
   is Predominantly Cubic***, arXiv:2605.22844 [math.CO], 13 May 2026.
   URLs: https://arxiv.org/abs/2605.22844 · https://doi.org/10.48550/arxiv.2605.22844
   Full text read (`carr-real.full.md`). The paper's *entire* content is:
   - Lemma 0.1 (proved): every proper subgraph H⊊G has δ(H)≤2.
   - Cor 0.1(1) (proved): every vertex adjacent to a degree-3 vertex (cubic
     vertices dominate).
   - Cor 0.1(2) (proved): vertices of degree ≥4 form an independent set.
   - Cor 0.2 (proved): every regular minimal counterexample is cubic.
   - Thm 0.1 (proved): ≥4/7 of the vertices have degree exactly 3.
   **The words "connected", "cut", "separator", "block", "ear", and
   "component" appear NOWHERE in the paper.** No connectivity claim exists.

2. **Klas Markström, *Extremal graphs for some problems on cycles in graphs***,
   Congressus Numerantium 171 (2004) 177–188.
   URL: http://abel.math.umu.se/~klasm/Uppsatser/cycex.pdf (also the §4 table
   quoted in ROOT/`markstrom-extremal-graphs.full.md`).
   §4 (the only section bearing on EG) gives the degree dichotomy: an edge-
   and vertex-minimal counterexample G has an independent set V1 of degree-≥4
   vertices and a nonempty set V2 of degree-3 vertices (he calls V1 the
   independent set: if d(u),d(v)≥3 and uv∈E then G−{u,v} would be a smaller
   counterexample). **No connectivity language anywhere in §4**; the
   connectivity words in the paper appear only in §3 and §5, which are about a
   *different* problem (fk(n) = min cycles in k-connected cubic graphs, and
   non-Hamiltonian 3-connected cubic graphs). No statement is made that a
   minimal counterexample is 2-connected, 3-connected, or cut-vertex-free.

3. **Gordon Royle, "The 2^n conjecture"** (original), archived:
   https://web.archive.org/web/2020/http://www.cs.uwa.edu.au/~gordon/remote/erdosconj.html
   (full text in `research/sources/royle-2n-conjecture.md`). Royle reports his
   min-degree-3 makeg search to n≤15 with **no connectivity restriction**, and
   a relaxation note (quoted verbatim in §3 below).

4. **Hegde, Sandeep & Shashank, *Erdős–Gyárfás conjecture on graphs without
   long induced paths***, arXiv:2410.22842 (v2 11 Feb 2025).
   https://doi.org/10.48550/arxiv.2410.22842. Full text read
   (`hegde-real.full.md`). Their "minimal counterexample" is defined as a
   counterexample with no proper *induced* subgraph counterexample (a different,
   weaker sense than Carr/Markström's min-order+min-size), used only to drive
   their backtracking correctness lemma. **No connectivity statement**;
   connectivity is never constrained or claimed anywhere.

5. **Avery Carr, *Cycles of Length 4 or 8 in Graphs with Diameter 2 and Minimum
   Degree at Least 3***, arXiv:2508.19302 (v4 30 Jan 2026), to appear BICA 109.
   https://arxiv.org/abs/2508.19302. Full text read (HTML abstract page;
   `carr-diameter2.full.md`). A restricted-class result (diameter-2 hypothesis),
   **not** a connectivity statement. Its usable corollary (derived here, not in
   the source): a minimal counterexample has diameter ≥ 3 — see claim
   `EG-min-ce-diam-ge-3`. Diameter ≠ connectivity; nothing about cut vertices.

6. **arXiv:2608.02675**, *A 60-Vertex Lower Bound for Cubic Bipartite
   Counterexamples to the Erdős–Gyárfás Conjecture* (v1 2 Aug 2026), newly
   downloaded this run (`cubic-bipartite-60.full.md` + digest). Proves every
   simple cubic bipartite graph on ≤58 vertices has a C4, C8, or C16, hence any
   cubic bipartite counterexample has ≥60 vertices. **Contains no connectivity
   statement about a minimal counterexample** — it is a computation for the
   bipartite class (Levi-graph / symmetric v3-configuration reduction).

### Secondary / class sources (no general connectivity claim either)

- Heckman–Krakovski, EJC 20(2) #P7 (2013) — proves EG for **3-connected cubic
  planar** graphs (a *class* whose hypothesis includes 3-connectivity; it is a
  hypothesis of the settled class, not a conclusion about minimal
  counterexamples). DOI https://doi.org/10.37236/3252.
- Exoo, arXiv:1403.5636 — G420 is 3-connected cubic planar, G78 cubic, both
  C4/C8/C16-free. Connectivity appears only as a description of these concrete
  examples, not as a statement about minimal counterexamples.
- Wikipedia / UCSD Erdős page / MathWorld / Erdős problems site #64 / Pirzada–
  Shah–Baskoro (EJGTA 2022) / Bensmail (DMGT 2016) / Gao–Shan / Hu–Shen /
  Nowbandegani et al. — all surveyed; **none** states a connectivity property of
  a minimal counterexample. They discuss verification bounds (≥17 total, ≥30
  cubic), settled classes, and extremal examples.

### Searches run (fresh, multiple angles)

The arXiv/PDF search terms covered minimal-counterexample 2-connectedness,
cut-vertex/separable/block structure, and 1-connected constructions. Results:
the only "minimal counterexample must be 3-connected" theorem found anywhere is
for a **different** conjecture — the Small Oriented Cycle Double Cover (SOCDC)
conjecture (Bagheri–Omoomi, arXiv:1207.5122) — and even that is conditional on
the CDC conjecture. **Nothing analogous exists for Erdős–Gyárfás.** The term
"Erdős–Gyárfás" plus any of "cut vertex", "2-connected", "blocks", "separable",
"1-connected" returns no paper stating such a property of an EG minimal
counterexample.

---

## 2. Exact citation of the one countervailing fact (the 1-connected warning)

Royle's own relaxation note is the only source that touches connectivity of
counterexamples at all, and it explicitly entertains **1-connected**
constructions. Verbatim from the archived page:

> "In addition to this it is clear that the condition minimum degree three can
> be relaxed to allow at most one vertex of minimum degree two, because then a
> **1-connected counterexample can be constructed by using three copies of X
> joined to a single central vertex**."

Source: Royle, "The 2^n conjecture"
(https://web.archive.org/web/2020/http://www.cs.uwa.edu.au/~gordon/remote/erdosconj.html).

**Why this does NOT refute a 2-connectivity lemma.** Royle's construction
relaxes the degree condition to *allow at most one vertex of degree 2*. A graph
built of three min-degree-3 lobes identified at one central vertex has, at the
identification point, something with degree equal to the number of lobes (≥3 in
degree, or a degree-2 if "one vertex of degree two" is used) — but more
importantly it is **not** a δ≥3 graph in the sense required of a counterexample
to the *conjecture*: either the central articulation is fine (degree ≥3) but
then "three copies joined at a central vertex" produces exactly the kind of
cut-vertex graph whose components are themselves min-degree-3, so such a graph
cannot be *minimal* (a smallest counterexample would live inside one lobe —
this is precisely the standard minimal-counterexample-at-a-cut-vertex
argument). Royle's note is about **extending the exclusion count** by relaxing
the *search's* degree condition to catch one-more graph; it does **not** exhibit
a δ≥3 1-connected graph with no power-of-two cycle. So the 1-connected warning
is a warning that a naive "take three counterexamples and glue" does not work,
not evidence against 2-connectivity.

**This is exactly the argument a would-be 2-connectivity lemma must formalize:**
show that a cut vertex v forces a smaller counterexample among the components
of G−v (since each component, together with v and enough edges to keep δ≥3,
either contains a power-of-two cycle or is a smaller counterexample). That
argument **is not in any source here**, and Royle's note does not preclude it.

---

## 3. Net finding and what it means for the structural-lemma attempt

- **(1) Exact-citation answer:** there is **no** paper that asserts or proves a
  connectivity/cut-vertex statement about an EG minimal counterexample.
  Quoting the strongest structural sources: Carr arXiv:2605.22844 (Lemma 0.1 +
  Cor 0.1 + Cor 0.2 + Thm 0.1, all degree-only), Markström §4 (degree
  dichotomy), Royle (search + 1-connected relaxation note), Hegde et al.
  (P13-free backtracking). None uses the words connected/cut/separator/block/ear
  about a minimal counterexample.
- **(2) Genuinely-new answer:** YES. A proof that a minimal counterexample is
  2-connected (no cut vertex) — or any ≥2-edge-connected / block statement —
  would be genuinely new. There is no prior art to beat.
- **Countervailing facts to attack against (so the lemma is tested):**
  - Royle's 1-connected construction (quoted above) — must be shown not to give
    a *minimal* δ≥3 counterexample via the cut-vertex-reduces argument.
  - No result forces 2-connectivity; the degree-4+ independent-set and ≥4/7-
    cubic structure are compatible with, but do not prove, 2-connectivity.
  - The Markström 24-graph and all C4/C8-free cubic near-examples are 2-connected
    (indeed the planar one is 3-connected), so 2-connectivity is *consistent*
    with every known near-counterexample — no known near-counterexample
    threatens it, but none proves it either.

## Claims ledger (managed here; the canonical copy is in CLAIMS.md via the
novelty-check note — claim `EG-no-connectivity-result`):

```claim
id: EG-no-connectivity-result
statement: No paper states or proves that a minimal counterexample to the Erdős–Gyárfás conjecture is 2-connected or 3-connected, or any connectivity result about such graphs. Carr (arXiv:2605.22844) contains only δ(H)≤2 for proper subgraphs, cubic domination, degree-≥4 independence, regular⇒cubic, and ≥4/7 cubic. Markström §4 contains only the degree dichotomy. Royle's page explicitly constructs a 1-connected near-counterexample (three min-degree-3 lobes joined to a central vertex, relaxing min-degree to "at most one vertex of degree 2"), so 2-connectivity is not derivable from any source and a proof would be genuinely new.
hypotheses: G a minimal counterexample (min order, min size, δ≥3, no power-of-two cycle).
holds-here: yes — this run studies exactly such G and must not assume 2-connectivity without proof.
status: literature absence established by full-text reading of Carr, Markström §4, Royle page, Hegde et al., Carr diameter-2, and the new cubic-bipartite paper, plus fresh multi-angle searches; Royle's 1-connected construction is in the primary source verbatim.
bearing: Any claim that a minimal counterexample is 2-connected (no cut vertex) is this run's own and must be stated as such; a cut vertex is not excluded by any published result, and the lemma must handle Royle's 1-connected relaxation by a cut-vertex-minimality argument that is absent from the literature.
anchor: research/summaries/connectivity-minimal-counterexample.md (this note); quoted evidence in research/summaries/connectivity-girth-minimal-ce.md and research/summaries/novelty-check-connectivity-triangles.md
```

## Sources used / rejected

- **Used (in library, full text read):** Carr arXiv:2605.22844
  (https://arxiv.org/abs/2605.22844); Markström Cong. Numer. 171 (2004)
  (http://abel.math.umu.se/~klasm/Uppsatser/cycex.pdf); Royle archived page
  (https://web.archive.org/web/2020/http://www.cs.uwa.edu.au/~gordon/remote/erdosconj.html);
  Hegde et al. arXiv:2410.22842 (https://arxiv.org/abs/2410.22842); Carr
  arXiv:2508.19302 (https://arxiv.org/abs/2508.19302); Heckman–Krakovski DOI
  https://doi.org/10.37236/3252; Exoo arXiv:1403.5636.
- **Newly downloaded this run:** arXiv:2608.02675 cubic-bipartite bound
  (https://arxiv.org/html/2608.02675v1) — checked, **no connectivity claim**;
  kept as the current best bipartite bound (≥60), not as a connectivity source.
- **Rejected as non-evidence for connectivity:** Bagheri–Omoomi arXiv:1207.5122
  (SOCDC minimal counterexample is 3-connected — a different conjecture, and
  conditional on CDC; **not transferable** to EG); the SOCDC-style result is the
  closest literature analogue found and confirms 2-connectivity-lemma work in
  the EG setting is open. Lo–Wu–Xie arXiv:2008.09001 and Yin–Wu-type
  2-connected-subgraph bounds concern unrelated connectivity guarantees and were
  not used. Further searched and found to contain no connectivity statement:
  Bensmail DMGT 2016, Pirzada et al. EJGTA 2022, Gao–Shan 2022, Hu–Shen 2024,
  Nowbandegani et al., Wikipedia, UCSD/MathWorld/Erdős-problems pages.
