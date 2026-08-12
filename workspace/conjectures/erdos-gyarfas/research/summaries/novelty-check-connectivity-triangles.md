# Novelty check: connectivity, triangles, C16-forcing, and verification-bound wording

Question asked of the literature: (1) any proved connectivity statement about a
minimal counterexample? (2) any published statement about triangles/girth in a
minimal counterexample? (3) is it known that every C4- and C8-free cubic graph
on ≥24 vertices contains a C16, and is the n=30+ count known? Is there a
published "triangle-exit lemma"? (4) exact wording of Royle's and Markström's
verification bounds with primary sources.

Verdict up front: **Q1 no (no connectivity result), Q2 no (nothing published on
triangles/girth beyond the trivial), Q3 the "every C4,C8-free cubic graph has a
C16" statement is FALSE as a general claim (Exoo G78, order 78, is a
counterexample), Q4 the primary sources say n≤15 general / n≤29 cubic; the
"17/30" figures are secondary.**

---

## Q1 — Connectivity of a minimal counterexample

**Nothing published. Neither Carr (arXiv:2605.22844v1, 13 May 2026) nor
Markström (Cong. Numer. 171 (2004) 177–188, §4) proves or states 2- or
3-connectivity.** The full text of Carr (in library, `carr-real.full.md`) gives:

- Lemma 0.1: every proper subgraph H ⊊ G has δ(H) ≤ 2.
- Cor 0.1(1): cubic vertices dominate (every vertex adjacent to a degree-3 vertex).
- Cor 0.1(2): the degree-≥4 vertices form an independent set.
- Cor 0.2: a regular minimal counterexample is cubic.
- Thm 0.1: ≥4/7 of the vertices have degree 3.

No connectivity statement appears in Carr's text; in particular nothing says
2-connected. **In fact the natural 2-connectivity conjecture is suspect**:
Royle's own page (archived, in library as `royle-2n-conjecture.md`) explicitly
builds a **1-connected** near-counterexample by joining three min-degree-3
lobes to a single central vertex, while relaxing the degree condition to
"at most one vertex of degree 2". So a would-be minimal counterexample must not
be assumed 2-connected on any source's word.

**arXiv/DOI citations:**
- Carr, *Every Minimal Counterexample to the Erdős–Gyárfás Conjecture is
  Predominantly Cubic*, arXiv:2605.22844 [math.CO], 13 May 2026.
- Markström, *Extremal graphs for some problems on cycles in graphs*,
  Congressus Numerantium 171 (2004) 177–188.
- Royle, "The 2^n conjecture" page
  (`https://web.archive.org/web/2020/http://www.cs.uwa.edu.au/~gordon/remote/erdosconj.html`).

---

## Q2 — Triangles / girth in a minimal counterexample

**Nothing published.** No source in the searched literature (Carr, Markström,
Royle, Hackman–Krakovski, Gao–Shan, Hu–Shen, Hegde–Sandeep–Shashank,
Nowbandegani–Esfandiari–Shirdareh–Bibak, Exoo, Bensmail, Pirzada–Shah–Baskoro,
UCSD Erdős page, MathWorld) states any of:
- girth of a minimal counterexample,
- that triangles must exist,
- structure of triangles and their neighborhoods in a minimal counterexample.

The only near-touches found:
- **Nowbandegani, Esfandiari, Shirdareh Haghighi, Bibak**, *On the Erdős–
  Gyárfás conjecture in claw-free graphs*, Discuss. Math. Graph Theory 34
  (2014) 635–640, arXiv:1109.5398, **Lemma 2.2 / §3** (see Q4 below) analyze
  the structure of triangles in *cubic claw-free C4-free graphs* — the deleted
  neighbours are distinct and the graph is vertex-disjoint triangles joined by
  a perfect matching. This is a special class, not a minimal counterexample,
  and the "exits distinct" content is already there in the claw-free setting
  (not under the name "triangle-exit lemma").
- **Heckman–Krakovski** (EJC 20(2) #P7, 2013) use triangles as a discharging
  tool in 3-connected cubic *planar* graphs; the Markström 24-vertex planar
  graph has girth 3 (contains cycles of length 3; MathWorld states it contains
  cycles of lengths 3, 5, 6, 7, and 9–24, and no 4 or 8).

**Conclusion: any claim about triangles in a minimal counterexample (e.g.,
"every triangle of cubic vertices ...") is this run's own, and should be
flagged as such in claims and reports, not attributed to the literature.**

Also relevant: **Heckman–Krakovski's theorem** (proved) is that every
*3-connected cubic planar* graph contains a 2^m-cycle with m ≤ 7, so the
*planar 3-connected* case is a settled class, but that is a class result, not a
statement about general minimal counterexamples.

---

## Q3 — "Every C4- and C8-free cubic graph on ≥24 vertices contains a C16"

**FALSE as a general statement, and known false in print.** The decisive source:

- **Geoffrey Exoo**, *Three Graphs and the Erdős–Gyárfás Conjecture*,
  arXiv:1403.5636 [math.CO], 22 Mar 2014.

Exoo constructs:
- **G420**, a 3-connected cubic planar graph of order 420 with **no C4, C8, or
  C16**, and
- **G78**, a cubic graph of order 78 with **no C4, C8, or C16** (built from the
  Petersen graph by replacing 11 of 12 vertices with copies of H7, and one
  vertex with a triangle).

So there are C4,C8-free cubic graphs on 24 (all four have a C16 — Markström's
Table 3), but also on 78 with no C16. Markström's "all four are C4,C8-free
cubic graphs on 24 vertices containing a C16" is a statement about *the
24-vertex* case only; it does **not** generalize to all n ≥ 24.

**Published count of cubic C4,C8-free graphs at n=30+:** not found. The only
published table is Markström's **Table 3**:

| n  | count |
|----|-------|
| 24 | 4     |
| 26 | 23    |
| 28 | 251   |

No source in the searched literature gives counts at n=30, 32, 34. Exoo gives
f(2)=10, f(3)=24, 54 ≤ f(4) ≤ 78, f(5) ≤ 450 (the smallest cubic graphs with no
2^m-cycles for m ≤ k), where f(4) straddles 78. An OEIS lookup (4, 23, 251)
found no catalogued sequence for "cubic graphs with no C4 and no C8." So: **with
the literature alone, nothing is known past n=28 cubic C4,C8-free counts, and
the C16-conclusion is false as a universal; the run's claim "every C4,C8-free
cubic graph on n≥24 has a C16" must be restricted to n=24 (Markström) or
proved.**

---

## Q4 — Triangle-exit lemma

**No published "triangle-exit lemma" exists under that or any equivalent
name.** The hypothesis "in a C4-free graph, the exits of a triangle of cubic
vertices are distinct, independent, and not adjacent to the other triangle
vertices" is not proved or stated as a lemma in any source located.

The closest published content is in **Nowbandegani–Esfandiari–Shirdareh–
Bibak**, DMGT 34 (2014) 635–640, §3 (arXiv:1109.5398v3, in library):
> "Suppose that G is a cubic claw-free graph that does not contain C4 ... Since
> G is claw-free, so we can assume that xy ∈ E(G). Thus xz, yz ∉ E(G); otherwise
> a C4 appears. Let x1 and y1 be respectively the other neighbours of x and y.
> Easily we see that x1 ≠ y1. Therefore, for every vertex there exists a unique
> triangle containing it, such that the other neighbours of its vertices are
> distinct."

This gives "the other neighbors of the triangle vertices are distinct" for the
**claw-free cubic C4-free** class. It does not state independence of the exits,
does not state non-adjacency of an exit to the other two triangle vertices, and
is not about minimal counterexamples. So the lemma as the run wants to use it
is **novel in the general (non-claw-free) setting**, though the distinctness
part is folklore in the claw-free cubic case.

---

## Q — Exact wording of the verification bounds (primary sources)

**Royle (primary, in library as `royle-2n-conjecture.md`, archived).** Exact
wording from the original page:

> "I have checked this conjecture for graphs on up to 15 vertices. Brendan
> McKay's graph generating program makeg was altered to only construct graphs X
> with the following properties:
> - Minimum degree of X is three.
> - No edges join two vertices of degree greater than three.
> - There are no 4-cycles in X
>
> The graphs so constructed are then examined for 8-cycles."
> (and a relaxation note: "the condition minimum degree three can be relaxed to
> allow at most one vertex of minimum degree two, because then a 1-connected
> counterexample can be constructed by using three copies of X joined to a
> single central vertex.")

**Markström (primary, in library as `markstrom-extremal-graphs.full.md`,
Cong. Numer. 171 (2004) 177–188).** §4 exact wording:

> "Using this observation Gordon Royle [Roy] used a modified version of Brendan
> McKay's graph generator makeg [McK] to generate graphs without C4's and the
> described degree structure. Royle generated all relevant graphs on less than
> 16 vertices and found no counterexamples. In order to extend this search
> further we choose to look at graphs with V1 = ∅, i.e cubic graphs. We used
> Gunnar Brinkman's cubic graph generator minibaum [Bri96] to generate all cubic
> graphs on less than 29 vertices and a simple fortran program to check for the
> existence of cycles of length 4,8 and 16. No counterexamples to the conjecture
> was found."

And Table 3: "The number of cubic graphs with no C4 and C8": 24→4, 26→23,
28→251; remark that the lower-right of the four 24-vertex graphs (the planar
one) "can be constructed from K4 be repeatedly expanding vertices into
triangles."

**The "17 total / 30 cubic" wording:** appears in secondary sources — the UCSD
Erdős page, MathWorld, Hegde–Sandeep–Shashank (arXiv:2410.22842, "a
counterexample has at least 17 vertices, a cubic counterexample has at least 30
vertices [10]"), Pirzada–Shah–Baskoro (EJGTA 10(1) 2022). The exact provenance
of the "17" (vs. Royle's own "15") is not documented in the primary sources;
"30" = Markström's n≤29 cubic search pushed one step. The run's record should
keep 15/29 as raw and 17/30 as the published consolidated figures.

---

## What this means for the run's claims

1. **Do not claim** "a minimal counterexample is 2-connected" without proof or
   a new source. Royle's own 1-connected construction shows why it is not
   derivable.
2. **Triangle claims are this run's own.** If the run proves a triangle-exit
   lemma, it is a new lemma in the general case (distinctness is known only in
   the claw-free cubic case).
3. **The C16-conclusion must be scoped to n=24** (or proved). Exoo's G78 refutes
   the general "every C4,C8-free cubic graph on ≥24 vertices has a C16".
4. **The verification-bound wording** should quote Royle "on up to 15 vertices"
   and Markström "on less than 29 vertices", and the 17/30 as the secondary
   consolidated figures.

## Claim ledger

```claim
id: EG-no-connectivity-result
statement: No paper states or proves that a minimal counterexample to the Erdős–Gyárfás conjecture is 2-connected or 3-connected, or any connectivity result about such graphs. Carr (arXiv:2605.22844) contains only δ(H)≤2 for proper subgraphs, cubic domination, degree-≥4 independence, regular⇒cubic, ≥4/7 cubic. Royle's own page explicitly constructs a 1-connected near-counterexample (three min-degree-3 lobes joined to a central vertex, relaxing min-degree to "at most one vertex of degree 2"), so 2-connectivity is not even plausibly derivable.
hypotheses: G a minimal counterexample (min order, min size, δ≥3, no power-of-two cycle).
holds-here: yes — this run studies exactly such G and must not assume 2-connectivity without proof.
status: literature absence established by full-text reading of Carr, Markström §4, Royle page, and searches; Royle's 1-connected construction is in the primary source.
bearing: Any claim "a minimal counterexample is 2-connected" is this run's own and must be stated as such; a cut-vertex is not excluded by any published result.
anchor: research/summaries/novelty-check-connectivity-triangles.md
```

```claim
id: EG-no-triangle-statement
statement: No published source states anything about triangles or girth in a minimal counterexample (girth, existence of triangles, or structure of triangles and their neighborhoods). The only triangle-structure result in the EG literature concerns the special class of cubic claw-free C4-free graphs (Nowbandegani–Esfandiari–Shirdareh–Bibak, DMGT 34 (2014) 635–640): each vertex lies in a unique triangle, the other neighbours of the triangle's vertices are distinct, and the graph is vertex-disjoint triangles joined by a perfect matching.
hypotheses: G a minimal counterexample; (class result) G cubic, claw-free, C4-free.
holds-here: yes — the claw-free result is about a different class; nothing transfers to a general minimal counterexample.
status: literature absence established by full-text reading and multiple searches; claw-free triangle structure is proved in DMGT 34 (2014).
bearing: Any triangle-based lemma about minimal counterexamples (e.g., "every triangle of cubic vertices...") is this run's own contribution and must be flagged as such.
anchor: research/summaries/novelty-check-connectivity-triangles.md
```

```claim
id: EG-exoo-G78-C16-free
statement: It is FALSE that every C4- and C8-free cubic graph on ≥24 vertices contains a C16. Exoo (arXiv:1403.5636) constructs G78, a cubic graph of order 78 with no 4-, 8-, or 16-cycles (from the Petersen graph by replacing 11 of 12 vertices with copies of H7 and one vertex with a triangle), and G420, a 3-connected cubic planar graph of order 420 with no C4, C8, or C16. Markström's "all four 24-vertex C4,C8-free cubic graphs contain a C16" holds only at n=24.
hypotheses: cubic, C4-free, C8-free, n≥24.
holds-here: yes — refutes the run's candidate claim; a verification extending "C16 present" beyond n=24 is impossible in this generality.
status: proved by explicit construction in Exoo arXiv:1403.5636 (read in full).
bearing: The claim "every C4,C8-free cubic graph on n≥24 vertices has a C16" must not be stated; the correct scoped statement is Markström's n=24 result plus the fact that C4,C8-free cubics at 26/28 vertices (counts 23, 251) all have a C16 (Markström found no counterexample cubic on n<29).
anchor: research/summaries/novelty-check-connectivity-triangles.md
```

```claim
id: EG-no-triangle-exit-lemma
statement: No published "triangle-exit lemma" (in a C4-free graph, the exits of a triangle of cubic vertices are distinct, independent, and not adjacent to the other triangle vertices) exists in the EG literature or elsewhere located. The closest published content is Nowbandegani–Esfandiari–Shirdareh–Bibak (DMGT 34 (2014) 635–640, §3) in the cubic claw-free C4-free class: "the other neighbours of its vertices are distinct" for the unique triangle containing each vertex. Independence of exits and non-adjacency of an exit to the other two triangle vertices are not stated anywhere found.
hypotheses: G cubic, C4-free; (closest result) G additionally claw-free.
holds-here: yes — the closest result needs claw-free, which a minimal counterexample is not known to be.
status: distinct-exits proved in the claw-free cubic case (DMGT 34 (2014)); the general lemma is absent from the literature — this run's candidate lemma is novel in the general setting.
bearing: The triangle-exit lemma is a new contribution if the run proves it without claw-freeness; it must be labelled as such.
anchor: research/summaries/novelty-check-connectivity-triangles.md
```

```claim
id: EG-verification-wording-primary
statement: Primary-source wording of the verification bounds: Royle (archived "2^n conjecture" page) "checked this conjecture for graphs on up to 15 vertices" with makeg modified for (i) min degree 3, (ii) no edge between two degree->3 vertices, (iii) no 4-cycles, then examined for 8-cycles. Markström (Cong. Numer. 171 (2004) 177–188, §4): "Royle generated all relevant graphs on less than 16 vertices and found no counterexamples"; Markström "generate[d] all cubic graphs on less than 29 vertices and a simple fortran program to check for the existence of cycles of length 4,8 and 16. No counterexamples to the conjecture was found." Table 3: cubic graphs with no C4 and C8: 24→4, 26→23, 28→251. The "≥17 total / ≥30 cubic" figures are secondary (UCSD Erdős page, MathWorld, Hegde et al. arXiv:2410.22842, Pirzada et al. EJGTA 2022); exact provenance of "17" is undocumented in the primary sources.
hypotheses: finite simple δ≥3 graphs (cubic case all degrees 3), n≤15 general / n≤29 cubic.
holds-here: yes — these are the run's oracle range.
status: primary texts read in full and quoted verbatim.
bearing: Any report of the verification bound must quote Royle n≤15 and Markström n≤29 cubic as raw, and 17/30 as the consolidated published figures.
anchor: research/summaries/novelty-check-connectivity-triangles.md
```

## Sources used (all in library or fetched this run)

- Carr arXiv:2605.22844 (full text read).
- Markström Cong. Numer. 171 (2004) 177–188 (full text read).
- Royle "The 2^n conjecture" (archived page, full text read).
- Exoo arXiv:1403.5636 (HTML full text read).
- Nowbandegani–Esfandiari–Shirdareh–Bibak arXiv:1109.5398v3 / DMGT 34 (2014)
  635–640 (full text read).
- Heckman–Krakovski EJC 20(2) #P7 (2013) (abstract + search snippets).
- Gao–Shan arXiv:2109.01277 (full text read; contains the induced-cycle lemma
  "if δ≥3 and no C4 then there is an induced Ck, k≥5" used for the P8 argument).
- Hu–Shen arXiv:2308.05675 (abstract + snippets).
- Hegde–Sandeep–Shashank arXiv:2410.22842 (full text read).
- UCSD Erdős problems page (fetched via search; text captured).
- MathWorld "Markström Graph" (read).
- Pirzada–Shah–Baskoro EJGTA 2022 (abstract + snippets).