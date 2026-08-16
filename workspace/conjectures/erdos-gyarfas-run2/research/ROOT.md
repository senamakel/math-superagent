# ROOT — what the literature actually establishes

This is the primary-source synthesis of the Erdős–Gyárfás conjecture
(problem.md). Every claim here traces to a full text in `research/sources/`
(28 primary full texts) or, where a proof is genuinely unobtainable (conference
proceedings, paywalled originals), to its sourced statement in
`research/summaries/`. **Nothing here is assertion from memory** — each row names
its source. Where a claim is asserted-by-source rather than proved, that is
stated. The detailed claim blocks with hypotheses and falsifiers live in
`research/CLAIMS.md`; this is the map, not the ledger.

**Conjecture (Erdős–Gyárfás, 1995; first in print Erdős 1997).** Every finite
simple graph with δ(G) ≥ 3 contains a cycle of length a power of two (2^k, k ≥ 2).

---

## 1. The obstruction — why an interval/congruence method cannot work

The single difficulty that has kept the conjecture open is **prescribed-sparse
length**. The literature's generic cycle-length machinery delivers cycles at
*some* length in a range or residue class, never at a fixed sparse value:

- **Liu & Ma**, "Cycle lengths and minimum degree of graphs" (JCTB 134:36–75,
  2019; full text held): Thms 1.1–1.13 all produce blocks of consecutive or
  residue-termed cycle lengths. At δ = 3 the strongest consequence is a pair of
  cycles differing by 2 (Bondy–Vince), never an 8/16/32. *Primary-text
  confirmation of the obstruction.*
- **Bondy & Vince** (JGT 1998; full text held): ≤ 2 vertices of degree < 3 ⟹
  two cycles differing by 1 or 2; the interval length ~2 ≪ the 2^k gap between
  powers of two.
- **Gao–Huo–Liu–Ma** (arXiv:1904.08126; full text held): unified proof that
  cycles of all lengths mod k and consecutive-length cycles are forced — but
  again residue classes, never a prescribed power of two.
- **Sudakov–Verstraëte** (Combinatorica 28:357–372, 2008; held): a graph with no
  2-power cycle on n vertices has average degree ≤ e^{O(log* n)}. The only
  genuinely 2-power-specific density result, but it runs on **average degree ≫ 3**,
  so it cannot touch δ ≥ 3.
- **Liu–Montgomery** (arXiv:2107.06583; held, + Montgomery survey 2025): huge
  average degree forces all even cycle lengths in a vast interval, hence a power
  of two. This **disproves Erdős's stronger claim** that a fixed degree-3 graph
  could avoid all 2-powers, but again needs average degree far above 3.

**Consequence:** any successful approach must produce a cycle at a *prescribed*
power of two, not at "some length in [a,b]" — an interval result only helps if
b > 2a. The only results that live at δ ≥ 3 AND hit prescribed sparse lengths
are the restricted-class structural proofs (§3) and the counterexample-shape
structure (§2) — that is where the run must work.

---

## 2. Structure of a minimal counterexample

What a minimal (vertex-then-edge) counterexample must look like, if one exists.
This is the strongest structural handle at δ ≥ 3.

- **Markström 2004** (full text held): any minimal counterexample contains an
  **independent set of degree-≥4 vertices** and a **nonempty set of degree-3
  vertices**; hence any *regular* minimal counterexample is **cubic**. The
  degree-≥4 set being independent is what makes every vertex of degree ≥ 4 have
  all neighbours of lower degree.
- **Carr 2026** (arXiv:2605.22844, full proof held): (Cor 0.1) every vertex of a
  minimal counterexample is **adjacent to a degree-3 vertex** (cubic vertices
  dominate); (Thm) the degree-≥4 vertices are independent and **(4/7)** of all
  vertices have degree exactly 3. So a minimal counterexample is *predominantly
  cubic*.
- **Verified strengthening (this run, derived, not yet formally checked):** a
  forum argument (erdosproblems #64 discussion, `notes/verify-2-3-degree-fraction.md`)
  pushes Carr's 4/7 to **> 2/3** (|V3| ≥ 2|V≥4| + 1, strictly more than 2/3 of
  vertices of degree 3), step-by-step against Carr's held lemmas. Status:
  `derived` — a deduction resting on Carr's proved results, not yet Lean-checked.
- **Degree-3-critical frame.** A vertex-minimal counterexample is
  *induced-degree-3-critical*: no proper induced subgraph of min degree ≥ 3,
  with exactly 2n − 2 edges (EFGS 1988, full text held). This is why the
  degree-3-critical class is the spine of the counterexample question.
  - EFGS 1988 (held): min-degree-3-critical graphs have C3 and C4, a cycle of
    length Ω(log n), and arbitrarily high girth constructions.
  - DCG / Combinatorica 2026 (held): every n-vertex degree-3-critical graph has
    **Ω(log n) distinct cycle lengths**; the 1–3 tree constructions show this is
    tight up to a constant. **Ω(log n) distinct lengths does NOT force a power of
    two** (e.g. 3,5,7,9,…), so this is a constraint on the spine, not a proof step.
  - **Narins–Pokrovskiy–Szabó, Combinatorica 37:495–519 / arXiv:1408.5289
    (held, full text):** the 1–3-tree construction G(T), with the dictionary
    (cycles of G(T)) ↔ (leaf-to-leaf paths of T). Disproves the EFGS conjecture
    (there are degree-3-critical graphs with no 23-cycle); Thm 1.3: even 1–3
    trees force leaf-leaf lengths 0,2,...,18, and an infinite family misses
    length 20.

**The picture a minimal counterexample must fit:** predominantly cubic (> 4/7,
and per the derived strengthening > 2/3, of vertices degree 3), degree-≥4 set
independent and dominated by cubic vertices, induced-degree-3-critical with 2n−2
edges. This is the state of the art; the live thread is whether this structure
is *rigid enough* to force a 2-power cycle on degree counts alone
(`threads/near-cubic-degree-spine.md`).

---

## 3. Restricted classes already settled (exact hypotheses and conclusions)

1. **3-connected cubic planar graphs** (Heckman–Krakovski 2013, full proof
   held): every such graph contains a 2^m-cycle with 2 ≤ m ≤ 7 (length in
   {4,8,...,128}); discharging method, computer-assisted in parts. [Result 4 on
   the problem's value scale — a real class settled.]
2. **Planar claw-free graphs** (Daniel–Shauger 2001): contain a 2-power cycle.
   *Statement-only* — conference proceedings, full proof unobtainable; sourced
   from West's page, Wikipedia, ERGOS problems page. [Sourced statement.]
3. **K_{1,m}-free graphs** (Shauger 1998): a K_{1,m}-free graph with δ ≥ m+1 or
   Δ ≥ 2m−1 contains a 2-power cycle. *Statement-only* (conference proceedings,
   Congr. Numer. 171:61–65). [Sourced statement.]
4. **P8-free graphs** (Gao–Shan 2022, held): δ ≥ 3 and P8-free ⟹ contains a 4- or
   8-cycle.
5. **P10-free graphs** (Hu–Shen 2024, held): δ ≥ 3 and P10-free ⟹ contains a 4-
   or 8-cycle.
6. **P13-free graphs** (Hegde–Sandeep–Shashank 2024, held): δ ≥ 3 and P13-free ⟹
   contains a 2-power cycle; also P12-free ⟹ 4- or 8-cycle. Computer-assisted
   backtracking verification.
7. **Claw-free / almost-claw-free** (NEHB14, Couch–Daniel–Wright; held): every
   claw-free δ ≥ 3 graph has a cycle of length 2^k **or 3·2^k** (Theorem 1, full
   proof held); cubic claw-free counterexample must have ≥ 114 vertices
   (Theorem 9). The 3·2^k weakening is real but not yet a power of two.
8. **Cayley graphs** on quaternion, dihedral, semidihedral, and order-p^3 groups
   (Ghaffari–Mostaghim 2017, held): 2-power cycles present.
9. **Petersen-family and small cases**: verified by enumeration below.

---

## 4. Current computational verification bound (the oracle anchor)

- **Royle & Markström**: any counterexample (any δ ≥ 3) has **≥ 17 vertices**;
  any **cubic** counterexample has **≥ 30 vertices** (Markström 2004, held).
- **Markström 2004** (held): four cubic graphs on 24 vertices containing **no
  4- or 8-cycle** (one planar); **all contain a 16-cycle**. These are the
  closest near-misses known — they do **not** disprove the conjecture.
- **Exoo** (held): explicit constructions — a 78-vertex graph with no {4,8,16},
  a 540-vertex graph with no {4,8,16,32}, a 32-vertex graph with no {4,8,32}.
  These are counterexamples to *forbidden subsets* of the 2-powers, not to the
  conjecture, but they pin the lengths a cubic/near-cubic graph can target.
- **Balaji 2026 (SAT-Modulo-Symmetries, Zenodo)** — asserted-by-source, no full
  certificate on disk: every min-degree-3 graph on **≤ 30 vertices** has a 4-, 8-,
  or 16-cycle, so any counterexample has **≥ 31 vertices** (general and cubic).
  Status: this is the newest bound but is held only from landing page + GitHub
  README (no formal certificate); the run's own oracle should reproduce at least
  ≤ 16-vertex (or ≤ 19) agreement before trusting numbers past the Markström
  level.
- **Bipartite cubic ≥ 60 vertices** (Balaji, held): no bipartite cubic
  counterexample below 60 vertices.

**The run's oracle** (`code/lib/erdos_gyarfas.py` and peers, validated to ≤ 16
vertices in `code/out/oracle_validation.md`) reproduces the settled rungs: every
δ ≥ 3 graph on ≤ 12 vertices has a 4- or 8-cycle; on ≤ 16 vertices has a 4-, 8-,
or 16-cycle (`R-delta3-n16-three-targets`, settled). The verification bound the
run can trust as its own is the ≤ 16-vertex level until it independently
reproduces more.

---

## 5. A note on the run's standing

The conjecture is **open**. No counterexample exists and no proof exists. The
strongest 2-power-specific known results (Sudakov–Verstraëte, Liu–Montgomery)
need average degree ≫ 3; the only δ ≥ 3 machinery is the counterexample structure
(§2) and the settled classes (§3). The run's own settled rungs (≤ 12 and ≤ 16
vertex verification) are genuine but modest; the live frontier is §2's
near-cubic degree structure and whether it is rigid enough to force a 2-power
cycle.

## 6. Everything older / adjacent in the library

Full-text holdings and their one-line content: see `notes/library-holdings.md`.
Digests per source: `summaries/`. Adjacent machinery held but not load-bearing for
the obstruction: Verstraëte 2005 unavoidable-cycle-lengths (avg degree ≥ 10 ⟹
density-zero cycle-length set with O(n^0.99)); Lyngsie–Merker 2021 (3-connected
cubic graphs realise all residues mod odd k) — both congruence-class, neither a
prescribed power of two.
