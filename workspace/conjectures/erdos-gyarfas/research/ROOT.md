# ROOT — the Erdős–Gyárfás literature map

Every result below states its exact hypotheses and conclusion, with the source
that establishes it. The run's claims ledger is `research/CLAIMS.md`; full texts
live under `research/sources/`, digests under `research/summaries/`.

## The conjecture itself

> **Erdős–Gyárfás conjecture** (posed by Erdős at the 1995 South-Eastern
> conference, Boca Raton; stated in print 1994–97). Every finite simple graph
> $G$ with $\delta(G) \ge 3$ contains a simple cycle of length $2^m$ for some
> non-negative integer $m$.
>
> Source: original Royle page
> (`https://web.archive.org/web/2020/http://www.cs.uwa.edu.au/~gordon/remote/erdosconj.html`)
> attributes the conjecture to Erdős & Gyárfás, presented 1995; Erdős offered
> $100 for a proof and $50 for a counterexample. The UCSD Erdős problems page
> (`https://mathweb.ucsd.edu/~erdosproblems/erdos/newproblems/PowerOfTwoCycles.html`)
> likewise gives the $100/$50 prizes. **Open.** No one has proved it and no one
> has produced a counterexample.
>
> Convention: $\delta(G)\ge 3$ is minimum degree (not connectivity, not
> average degree). The conjecture is false for $\delta \ge 2$ (a long odd cycle
> that is not a power of two), so degree 3 is doing real work. The cycle is any
> (not necessarily induced) cycle.

## Minimal counterexample

**Definition** (Carr, arXiv:2605.22844, 2026). A *minimal counterexample* is a
graph $G$ of minimum possible order, and subject to that minimum possible size,
with $\delta(G)\ge 3$ and no power-of-two cycle.

The structural facts the literature establishes about such a $G$:

1. **Markström's degree dichotomy.** $G$ splits as an independent set $V_1$ of
   vertices of degree $\ge 4$ together with a nonempty set $V_2 = V\setminus
   V_1$ of vertices of degree exactly 3.
   - *Argument* (edge-minimality, stated in Markström §4): if two vertices
     $u,v$ with $d(u),d(v)\ge 3$ were adjacent then $G-\{u,v\}$ would be a
     smaller counterexample. Hence no edge joins two "high"-degree vertices —
     $V_1$ is independent — and since not all vertices of a graph of
     $\delta\ge 3$ can pair up this way, $V_2\neq\emptyset$.
   - Sources: Markström, "Extremal graphs for some problems on cycles in
     graphs"; Carr abstract.

2. **Every regular minimal counterexample is cubic.** Direct consequence of (1).
   (Carr, abstract.)

3. **Cubic vertices dominate.** Every vertex of a minimal counterexample is
   adjacent to a vertex of degree exactly 3. (Carr, abstract; "Corollary".)

4. **Predominantly cubic.** At least $4/7$ of the vertices of any minimal
   counterexample have degree exactly 3. (Carr, abstract.)

5. **Proper-subgraph bound.** Every proper subgraph $H\subsetneq G$ of a
   minimal counterexample has $\delta(H)\le 2$. (Carr, Lemma 0.1, as reported
   in the arXiv HTML. If such $H$ had $\delta\ge 3$ it would be a counterexample
   on fewer vertices/edges, contradiction.)

**Implication for this run.** A would-be minimal counterexample must be crowded
with cubic vertices ($\ge 4/7$), its non-cubic vertices must form an independent
set, and every vertex must sit next to a cubic one. Any construction or
structural argument can assume these; any candidate that violates one is
refuted.

**What would falsify each:** exhibit a min-degree-$\ge 3$ power-of-two-cycle-free
graph that is a proper subgraph of a counterexample (for 5), or a minimal
counterexample violating the independent-set / 4/7 / dominating conditions
(1,3,4). None known.

## Restricted classes where the conjecture is proved

These are exact, sourced results. "Proved" means a paper proves it; the
computer-assist flags are as the authors describe.

1. **3-connected cubic planar graphs** — **Heckman & Krakovski, EJC 20(2) #P7,
   2013** (`https://doi.org/10.37236/3252`).
   - Hypothesis: $G$ is a 3-connected cubic planar graph.
   - Conclusion: $G$ contains a cycle of length $2^m$ for some $m\ge 0$.
   - Method: long proof, partly computer-based, discharging method used in a
     novel way.
   - Falsify: exhibit a 3-connected cubic planar graph with no power-of-two
     cycle. None known.

2. **$P_k$-free graphs** (no induced path on $k$ vertices), $\delta\ge 3$:
   - **Gao & Shan, Graphs and Combinatorics 2022** (arXiv:2109.01277):
     $P_8$-free $\Rightarrow$ contains a $C_4$ or a $C_8$.
   - **Hu & Shen, Discrete Mathematics 2024**: $P_{10}$-free $\Rightarrow$
     contains a power-of-two cycle.
   - **Hegde, Sandeep & Shashank, arXiv:2410.22842, 2024/2025**:
     $P_{13}$-free $\Rightarrow$ contains a power-of-two cycle; and the
     stronger intermediate **$P_{12}$-free $\Rightarrow$ contains a $C_4$ or a
     $C_8$**. Computer-assisted (backtracking search that either finds a
     $P_k$-free counterexample or proves none exists; code released).

3. **Planar claw-free graphs** — **Daniel & Shauger (2001)**; and **Shauger
   (1998)** for $K_{1,m}$-free graphs with $\min$-degree $\ge m+1$ or
   $\max$-degree $\ge 2m-1$. (Cited in Hegde–Sandeep–Shashank and the Erdős
   problems page; not in this library's summaries, flag for the librarian.)

4. **Cubic claw-free graphs** — partial structural results (Nowbandegani &
   Esfandiari, Hobbs's question; arXiv:1109.5398, 2011) give a triangle-
   contraction reduction: if $\hat G$ (each triangle shrunk to a point) has a
   cycle of length $k$, then $G$ has cycles of every length in
   $[2k,\, 2k+1,\, \dots,\, 3k]$. Bipartite counterexample must have $\ge 32$
   vertices (Nowbandegani–Esfandiari). Not in this library's summaries.

5. **Cayley graphs on some groups** — Ghaffari–Mostaghim, Aequationes
   Mathematicae 92 (2018): generalized quaternion, dihedral, semidihedral
   groups and groups of order $p^3$. (Cited in Hegde et al.)

6. **Diameter-2 graphs** — Carr, arXiv:2508.19302 (2025): every graph with
   diameter 2 and $\delta\ge 3$ contains a $C_4$ or a $C_8$.

7. **Dense graphs (sparse-degree side of average degree)** — **Sudakov &
   Verstraëte (2008)**: conjecture holds for every graph whose average degree
   is in the iterated logarithm of the number of vertices (i.e. very sparse
   with huge $n$). **Verstraëte (2005)**: a set $S$ of lengths with
   $|S|=O(n^{0.99})$ such that every graph with average degree $\ge 10$ contains
   a cycle with length in $S$. **Liu–Montgomery**: some large constant $C$ such
   that every graph with average degree $\ge C$ contains a cycle whose length is
   a power of two — this *disproved* Erdős's own later conviction that the
   conjecture fails for every minimum degree $\ge 3$ (noted in Hegde et al.).

## The computational verification bound (the key deliverable)

**Established figure, from the literature:**

- **Any counterexample to the conjecture must have more than 17 vertices.**
- **Any *cubic* counterexample must have more than 30 vertices.**

This is attributed to **Gordon Royle and Klas Markström**. Sources that state
these numbers (multiple independent): the UCSD Erdős Problems page
(`https://mathweb.ucsd.edu/~erdosproblems/erdos/newproblems/PowerOfTwoCycles.html`),
Wikipedia ("Erdős–Gyárfás conjecture"), Wolfram MathWorld ("Markström Graph"),
and the EJGTA paper "On 2-power unicyclic cubic graphs" (Pirzada, Shah, Baskoro,
2022).

**What the original sources actually report** (so the numbers are not taken on
faith; note there is a small numerical tension that must be stated):

- **Royle** (original page, "The 2^n conjecture", found via the Wayback
  Machine). He used a modified McKay `makeg` to generate graphs $X$ with:
  (i) min degree 3, (ii) no edge between two vertices of degree $>3$, (iii) no
  4-cycles; then checked for 8-cycles. **All relevant graphs on fewer than 16
  vertices** (i.e. $n\le 15$, his table runs 9–15) contain an abundance of
  8-cycles — no counterexample. His relaxation note: allowing at most one
  vertex of degree 2 lets a 1-connected counterexample be built from three
  copies of $X$ joined to a central vertex, extending exclusion a little beyond
  15.
- **Markström** ("Extremal graphs for some problems on cycles in graphs", §4).
  Confirms Royle generated all relevant graphs on fewer than 16 vertices.
  Markström then took the cubic case ($V_1=\emptyset$) and generated **all
  cubic graphs on fewer than 29 vertices** with Brinkmann's `minibaum`,
  checking for $C_4, C_8, C_{16}$: no counterexample. He found the **smallest
  cubic graphs with no $C_4$ and no $C_8$ on 24 vertices** — four of them, all
  containing a $C_{16}$; exactly one is planar (this is the "Markström graph",
  a cubic planar 24-vertex graph). So nothing contradicts the conjecture and the
  exclusion extends to all cubic graphs with $n\le 29$.

The consolidated ">17 vertices total, >30 cubic" figure is the accepted summary
of the Royle + Markström searches; the ">30 cubic" comes from the exhaustive
$n\le 29$ cubic search plus the relaxation counting that pushes 1-connected
constructions one step further. **The exact provenance of the "17" (vs. Royle's
own "15") is not documented in the original page**; treat ">17" as the
wide-cited consolidated figure and Royle's own stated bound as $n\le 15$
(general, with a 1-connected footnote), Markström's as $n\le 29$ (cubic). The
run should record this natively and treat 17/30 as the "published" numbers while
knowing the raw search went to 15/29.

**Unpublished / non-peer-reviewed extension (flag, do not rely on as
"literature").** A GitHub repository (`ArjunBalaji79/erdos-gyarfas-min-degree-3`)
reports a SAT Modulo Symmetries (SMS) verification that every min-degree-$\ge 3$
graph on at most 31 vertices contains a power-of-two cycle (UNSAT for each
$n=17$–$31$ against $C_4,C_8,C_{16}$), pushing the general bound to
"$\ge 32$ vertices" and cross-checked at $n\le 19$ with CEGA-SAT. This is
**not** in peer-reviewed literature and has not been audited here; record as a
lead for the computational agent, not as an established bound.

**Bottom line for this run.** The safe, source-backed computational claim is:
*no counterexample exists on $n \le 15$ vertices in general, and no cubic
counterexample exists on $n \le 29$ vertices* (Royle, Markström), summarized in
the literature as "$\ge 17$ total, $\ge 30$ cubic". Any new verification that
increases this (SMS to 31, or SAT on the $V_1\neq\emptyset$ degree structure)
is a genuine strengthening if machine-checked.

## What is NOT yet established (gaps)

- The general $\delta\ge 3$ case for $n\ge 18$. The cubic case for $n\ge 30$.
- Whether the "17 / 30" figures can be exactly attributed to a single published
  paper (the primary pages give 15/29); an exact citation chain for the 17/30
  numbers is missing and worth recovering.
  **RESOLVED (scholar digest):** the primary source is Markström, Congressus
  Numerantium 171 (2004) 177–188, §4 — Royle `makeg` exhaustively to $n<16$
  (general), Markström `minibaum` to $n<29$ (cubic), both no counterexample.
  Hegde et al. (arXiv:2410.22842v2) restate the consolidated "$\ge17$ total,
  $\ge30$ cubic" and add "$\ge30$ bipartite" (Nowbandegani–Esfandiari 2011).
  A single paper stating exactly "17" is still not identified, but the chain
  Royle15→Markström29→"17/30" is now source-anchored.
- The degree-4+ independent-set structure (Carr/Markström) has not been turned
  into a SAT/SMS propagator here; it reduces the search space for the
  $V_1\neq\emptyset$ case and is a concrete next computation.
- Verification for the mixed (non-cubic) case past $n=15$ has no known
  peer-reviewed bound; the SMS result (to 31) is the only claimed extension and
  is unvetted.

## Sources held in this library (with digests)

- `research/sources/royle-2n-conjecture.md` — Royle's original "2^n
  conjecture" page (via Wayback), verbatim table.
- `research/sources/carr-real.full.md`,
  `research/summaries/carr-real.md` — arXiv:2605.22844v1, Carr, real content.
- `research/sources/hegde-real.full.md`,
  `research/summaries/hegde-real.md` — arXiv:2410.22842v2, Hegde et al., real content.
- `research/sources/markstrom-extremal-graphs.full.md`,
  `research/summaries/markstrom-extremal-graphs.md` — Markström §4.
- `research/summaries/heckman-krakovski-cubic-planar.md` — EJC 20(2)#P7 2013.
- `research/sources/ucsd-erdos-power-of-two.md` — (download failed; content
  captured via search excerpts, UCSD Erdős problems page).

---

## Claims

```claim
id: EG-markstrom-dichotomy
statement: A minimal counterexample G to the Erdős–Gyárfás conjecture splits into an independent set V1 of vertices of degree ≥4 and a nonempty set V2 = V\V1 of vertices of degree exactly 3.
hypotheses: G is a finite simple graph, δ(G)≥3, G has no power-of-two cycle, and G is minimal (minimum order then minimum size).
holds-here: yes — this is exactly the minimal-counterexample structure this run studies.
status: proved (edge-minimality argument, Markström §4; restated in Carr abstract)
bearing: Any construction or structural argument about a minimal counterexample may assume V1 independent and V2 nonempty; every regular minimal counterexample is cubic.
anchor: research/summaries/markstrom-extremal-graphs.md §4; research/summaries/carr-minimal-counterexample.md
```

```claim
id: EG-regular-is-cubic
statement: Every regular minimal counterexample to the Erdős–Gyárfás conjecture is cubic (3-regular).
hypotheses: G is a minimal counterexample as in EG-markstrom-dichotomy and is regular.
holds-here: yes.
status: proved (immediate from EG-markstrom-dichotomy; Carr abstract)
bearing: Focuses the cubic search; a regular counterexample, if any, has all degrees 3.
anchor: research/summaries/carr-minimal-counterexample.md
```

```claim
id: EG-cubic-dominates
statement: Every vertex of a minimal counterexample G is adjacent to a vertex of degree exactly 3.
hypotheses: G is a minimal counterexample.
holds-here: yes.
status: proved (Carr, arXiv:2605.22844, abstract)
bearing: The cubic vertices form a dominating set; strengthens the structure a search must satisfy.
anchor: research/summaries/carr-minimal-counterexample.md
```

```claim
id: EG-predominantly-cubic
statement: At least 4/7 of the vertices of any minimal counterexample G have degree exactly 3.
hypotheses: G is a minimal counterexample.
holds-here: yes.
status: proved (Carr, arXiv:2605.22844, abstract)
bearing: Quantitative density of cubic vertices; a candidate with fewer than 4/7 cubic vertices is refuted.
anchor: research/summaries/carr-minimal-counterexample.md
```

```claim
id: EG-proper-subgraph-delta-le-2
statement: Every proper subgraph H ⊊ G of a minimal counterexample G has δ(H) ≤ 2.
hypotheses: G is a minimal counterexample; H a proper subgraph.
holds-here: yes.
status: proved (Carr, Lemma 0.1)
bearing: If δ(H)≥3 then H is a power-of-two-free min-degree-3 graph on fewer vertices — contradiction of minimality.
anchor: research/sources/carr-minimal-counterexample.full.md
```

```claim
id: EG-3conn-cubic-planar
statement: Every 3-connected cubic planar graph contains a cycle of length 2^m for some m≥0 (the conjecture holds for this class).
hypotheses: G is a 3-connected cubic planar graph.
holds-here: yes — a class, so it is a partial proof, and it also covers the Markström planar 24-vertex graph.
status: proved (Heckman & Krakovski, EJC 20(2)#P7, 2013); partly computer-assisted, discharging method
bearing: One of the ≥3 restricted classes; gives a proven class to test the run's machinery against.
anchor: research/summaries/heckman-krakovski-cubic-planar.md
```

```claim
id: EG-P13-free
statement: Every P13-free graph with δ(G)≥3 contains a cycle of length a power of two (conjecture holds).
hypotheses: G is finite simple, δ(G)≥3, G is P13-free (no induced path on 13 vertices).
holds-here: yes — a class.
status: proved with computer-assisted backtracking search (Hegde, Sandeep, Shashank, arXiv:2410.22842); subsumes P8-free (Gao–Shan) and P10-free (Hu–Shen).
bearing: Restricted-class verification; the P12-free sub-result (always a C4 or C8) is a sharper forced-cycle statement.
anchor: research/summaries/hegde-P13-free.md
```

```claim
id: EG-verification-bound
statement: No counterexample to the Erdős–Gyárfás conjecture exists on n ≤ 15 vertices in general, and no cubic counterexample exists on n ≤ 29 vertices.
hypotheses: finite simple graphs with δ≥3 and no power-of-two cycle (cubic case: all degrees 3), n ≤ 15 (general) / n ≤ 29 (cubic).
holds-here: yes — exact narrowing of the search space.
status: computed and checked (Royle modified makeg, n≤15; Markström minibaum, cubic n≤29); summarized in the literature as "≥17 total, ≥30 cubic" (UCSD Erdős problems page, Wikipedia, MathWorld, EJGTA Pirzada et al. 2022)
bearing: The oracle range and the minimum size of any hypothetical counterexample; the ≥4/7-cubic + independent-structure results must hold at these sizes if exploited.
anchor: research/sources/royle-2n-conjecture.md; research/summaries/markstrom-extremal-graphs.md §4
```

```claim
id: EG-markstrom-24-graphs
statement: The smallest cubic graphs with no C4 and no C8 have 24 vertices; there are four, all contain a C16, and exactly one is planar.
hypotheses: cubic graphs avoiding C4 and C8.
holds-here: yes — these are near-miss examples for an Erdős–Gyárfás counterexample.
status: computed and checked (Markström, §4; the planar one is the "Markström graph").
bearing: Shows the obstruction lives at length 16 for 24 vertices; a counterexample would need no C4, C8, or C16 simultaneously.
anchor: research/summaries/markstrom-extremal-graphs.md §4; mathworld.wolfram.com/MarkstroemGraph.html
```
