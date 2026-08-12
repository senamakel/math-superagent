# Connectivity, girth, diameter: what the on-disk full texts say about a minimal counterexample

> Extraction by the librarian from the full texts of every EG source in this
> library (`research/sources/*.full.md` + `royle-2n-conjecture.md`,
> `markstrom-houseofgraphs-*.full.md`). **Bottom line: the sources contain no
> proved or asserted 2-connectivity, 3-connectivity, girth, or diameter
> statement about the *general* minimal counterexample.** Everything they
> say on these topics is listed below; everything else is gap.

## What IS in the sources — exact statements, with proved/asserted + anchor

### Connectivity-adjacent (all degree-structure, not connectivity)

1. **Lemma 0.1 (proved).** For a minimal counterexample $G$ (min order, then
   min size; $\delta(G)\ge 3$; no power-of-two cycle), **every proper
   subgraph $H\subsetneq G$ has $\delta(H)\le 2$**. Walk: if $H$ had
   $\delta\ge3$ it would be a smaller counterexample whose power-of-two
   cycle embeds in $G$.
   — Anchor: `research/sources/carr-real.full.md`, Lemma 0.1.
2. **Cor 0.1(1) (proved).** **Every vertex of $G$ is adjacent to a degree-3
   vertex** (cubic vertices form a dominating set). Walk: $G-v$ has
   $\delta\le2$; the only vertex that can drop below 3 after removing $v$ is
   a degree-3 neighbor of $v$.
   — Anchor: `carr-real.full.md`, Cor 0.1(1).
3. **Cor 0.1(2) (proved).** The **degree-$\ge4$ vertices form an independent
   set**. Walk: deleting the edge $uv$ between two degree-$\ge4$ vertices
   leaves $\delta\ge3$, contradicting Lemma 0.1.
   — Anchor: `carr-real.full.md`, Cor 0.1(2).
4. **Cor 0.2 (proved).** **Every *regular* minimal counterexample is cubic.**
   — Anchor: `carr-real.full.md`, Cor 0.2.
5. **Thm 0.1 (proved).** **At least $4/7$ of the vertices have degree exactly
   3.** — Anchor: `carr-real.full.md`, Thm 0.1.
6. **Markström dichotomy (proved argument, §4).** $G$ splits into an
   independent set $V_1$ of degree-$\ge4$ vertices and a nonempty set
   $V_2=V\setminus V_1$ of degree-3 vertices. Walk: if $d(u),d(v)\ge3$ and
   $uv\in E$ then $G-\{u,v\}$ is a smaller counterexample.
   — Anchor: `research/sources/markstrom-extremal-graphs.full.md`, §4; this
   is the source Carr credits.

### Connectivity of a minimal counterexample — NOT stated anywhere on disk

- **No** source in the library states that a minimal counterexample is
  2-connected, 3-connected, has no cut vertex, or has any separator/block/
  ear-decomposition property. Carr's paper never uses the words
  "connected", "cut", "separator", "block", or "ear"; Markström §4 does not
  either. The computational searches (Royle min-degree-3 to $n\le15$;
  Markström cubic to $n\le29$) make **no connectivity restriction** and find
  no counterexample, so they neither prove nor disprove any connectivity
  claim.
- **In fact there is a standing warning against assuming 2-connectedness**:
  Royle's own relaxation note (anchor:
  `research/sources/royle-2n-conjecture.md`) explicitly builds a
  **1-connected** construction — "a 1-connected counterexample can be
  constructed by using three copies of X joined to a single central vertex"
  (allowing at most one vertex of degree 2). So a would-be minimal
  counterexample cannot currently be assumed 2-connected on any source's
  authority. A **2-connectivity lemma would be genuinely new** if provable.

### Girth — NOT settled for a minimal counterexample

- **Triangles are compatible with the near-counterexample evidence.**
  The Markström graph (cubic, planar, 24 vertices, no $C_4$, no $C_8$,
  has a $C_{16}$; the closest known near-counterexample) **contains
  triangles** — it is built from $K_4$ by expanding vertices into
  triangles, so its girth is 3. Invariants served by HoG (anchor:
  `research/sources/markstrom-houseofgraphs-invariants.full.md`) show
  $girth=3$ (invariant value 3.0 twice — girth and girth-related entries).
  Anchor for the construction claim:
  `markstrom-extremal-graphs.full.md` §4: "the lower right of the four
  graphs can be constructed from $K_4$ be repeatedly expanding vertices
  into triangles".
- **No source asserts a minimal counterexample must be triangle-free, or
  must have any specific girth.** (The oracle script
  `code/verify_connectivity_claims.py` is written to re-confirm girth 3 on
  the HoG adjacency list, but has NOT been run — no executor here.)
- In the extremal family (Markström §3), the minimum-cycle-count graphs are
  built by vertex-into-triangle expansion and have girth 3; and the §2/§5
  sections' "girth" column refers to cubic graphs with *many* cycles, not
  to counterexamples. Do not import those girth numbers into the
  gap-note; they are about a different problem.

### Diameter

- **No statement in the library's EG sources about the diameter of a
  minimal counterexample.** The only diameter result is Carr's companion
  note (anchor: `research/sources/carr-diameter2.full.md`,
  arXiv:2508.19302, to appear BICA 109): **every graph with diameter 2 and
  minimum degree at least 3 contains a $C_4$ or a $C_8$** — that is a
  *restricted-class* proof (diameter 2 is a hypothesis, not a conclusion
  about counterexamples). It implies: a minimal counterexample cannot have
  diameter 2 (else it would contain a 4- or 8-cycle). **This corollary is
  a genuine consequence of the literature: a minimal counterexample has
  $\mathrm{diam}(G)\ge 3$.** It is not stated as such in any source; the
  librarian derives it (see "Derived, marked as such").

### Degree-3 structure — everything the sources say, all proved

- Cubic vertices form a **dominating set** (Cor 0.1(1)); in particular a
  degree-3 vertex has at least one degree-3 neighbor.
- Degree-3 vertices form a **nonempty** set $V_2$ (Markström dichotomy);
  the degree-$\ge4$ set $V_1$ is independent.
- At least **4/7** of vertices are degree 3 (Thm 0.1); counting: $4|V_1|\le
  3|V_3|$ over edges $V_3\text{--}V_1$.
- Every **regular** counterexample is **cubic** (Cor 0.2).
- No separator structure, no blocks, no ear decomposition, no "two
  degree-3 vertices cannot be separated by ..." statement anywhere.

## Derived (this run's own deductions, not in sources — labeled)

- **Corollary (derived, trivial but not written in sources): a minimal
  counterexample cannot have diameter 2.** Proof: Carr's theorem
  (arXiv:2508.19302) — every $\delta\ge3$ graph of diameter 2 contains a
  $C_4$ or $C_8$ — plus $C_4,C_8$ are powers of two. Combined with the
  domination result, the **cubic-vertex set is a diameter-3 dominating
  set in the weak sense that every vertex is at distance 1 from $V_3$**.
- **Also trivial (degree bookkeeping, not connectivity):** in each
  component of $G-v$, $v$ must have at least one neighbor; combined with
  $\delta(G)\ge3$ this gives no lower bound > 1 on component sizes, so it
  proves nothing about cut vertices. A 2-connectivity proof, if one
  exists, must use cycle-minimality, not degrees.

## What this means for the structural-lemma attempt

- A **provable 2-connectivity (or "'no cut vertex') lemma for minimal
  counterexamples would be genuinely new** — no source on disk asserts it,
  and the wider searches (arXiv + web, queries run:
  "Erdos-Gyarfas conjecture minimal counterexample 2-connected
  connectivity cut vertex", "...girth triangles", "survey minimal
  counterexample structure 2-connected", "cut vertex block girth
  triangle-free", PDF category) found no such published statement either.
- A **girth statement** (e.g. "a minimal counterexample contains a
  triangle") is likewise wide open; the near-counterexample family is
  triangle-rich, so no a priori reason to forbid triangles.
- **Watch-out / falsifier:** any 2-connectivity lemma is refuted
  dimension-wise by Royle's relaxation comment (1-connected
  constructions are *considered possible* in his note), so the lemma must
  explicitly handle why that degree-2 relaxation ("at most one vertex of
  degree 2") cannot be part of a *minimum-order* counterexample — i.e. why
  a cut-vertex counterexample would force a smaller one via its
  components. That is exactly the standard minimal-counterexample-cut
  argument, and it is **not** in any source here.

## Cross-reference

A prior novelty check (`research/summaries/novelty-check-connectivity-triangles.md`)
already established the literature absence for Q1 (connectivity) and Q2
(triangles/girth) with claims `EG-no-connectivity-result` and
`EG-no-triangle-statement`, plus `EG-exoo-G78-C16-free` (Exoo's G78, order 78,
is a cubic C4,C8-free graph with NO C16 — so the small-power-of-two-cycle
picture does NOT stabilize past n=24; don't import "C16 forced" as a girth-ish
fact) and `EG-no-triangle-exit-lemma`. This note is the per-source extraction
with quotes that the novelty check's claims rest on; do not delete either.
The only genuinely new item added here is the derived **diameter corollary**
(claim `EG-min-ce-diam-ge-3` below).

## Claim ledger

```claim
id: EG-min-ce-diam-ge-3
statement: A minimal counterexample G to the Erdős–Gyárfás conjecture has diameter at least 3.
hypotheses: G finite simple, δ(G)≥3, no power-of-two cycle, minimal (min order then min size).
holds-here: yes — this is exactly the structural object the run studies.
status: proved (derivation from Carr, arXiv:2508.19302: every δ≥3 graph of diameter 2 contains a C4 or a C8, which are powers of two; a counterexample cannot contain either).
bearing: any structural argument may assume diam(G) ≥ 3, i.e. some pair of vertices at distance ≥ 3; combined with cubic domination (Cor 0.1(1)) the cubic set is a dominating set but not a diameter-2 one.
anchor: research/summaries/connectivity-girth-minimal-ce.md (derived; not stated as such in any source)
```

- `research/sources/carr-real.full.md` (Lemma 0.1, Cor 0.1, Cor 0.2, Thm 0.1)
- `research/sources/markstrom-extremal-graphs.full.md` (§4 dichotomy; §4
  near-counterexample construction and "can be constructed from K4 by
  repeatedly expanding vertices into triangles")
- `research/sources/royle-2n-conjecture.md` (relaxation note: 1-connected
  construction)
- `research/sources/carr-diameter2.full.md` (diameter-2 ⇒ C4/C8; the only
  diameter statement in the library)
- `research/sources/markstrom-houseofgraphs-invariants.full.md` (Markström
  graph girth 3)
- `research/sources/markstrom-houseofgraphs-api.full.md` (adjacency list
  used by the oracle script)

## Not checked / left open

- The oracle script `code/verify_connectivity_claims.py` is written but
  **not executed** (librarian has no executor); the two-K4+bridge refutation
  and the Markström girth-3 check are elementary and should be run by the
  coder.
- No source establishes **3-connectivity**, **edge connectivity**, **blocks
  structure**, or **ear decompositions** for a minimal counterexample;
  these are all open for the structural-lemma attempt.