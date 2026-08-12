# Potočnik–Vidali, "Cubic vertex-transitive graphs of girth six"

**Source:** Primož Potočnik, Janoš Vidali, *Cubic vertex-transitive graphs of girth six*, Discrete Math. 345(3) (2022), art. 112734. arXiv:2005.01635v4 (open access, arXiv PDF/HTML). Full text on disk: `research/sources/potocnik-vidali-cubic-vertex-transitive-girth6-html.full.md`.

## Main theorem (classification)

Every finite simple **cubic vertex-transitive** graph of **girth 6**, with the single
exception of the **Desargues graph** (the generalised Petersen graph GP(10,3) on
20 vertices), is the skeleton of one of three constructions:

1. **a hexagonal tiling of the torus** (a vertex-transitive map on the torus of
   type {6,3} — all such tilings are vertex-transitive);
2. the **truncation of an arc-transitive triangulation of a closed hyperbolic
   surface** (type {3,ℓ} with ℓ ≥ 7); or
3. the **truncation of a 6-regular graph with respect to an arc-transitive
   dihedral scheme**.

The paper also refines this by a *signature* describing how girth-6 cycles are
distributed (face cycles vs non-face cycles). Cubic vertex-transitive graphs of
girth larger than 6 are discussed but not classified. (Erratum added two missing
signatures, (3,3,4) and (3,4,5), in Table 2.)

## Why it matters for the run

This is the structural classification that underlies any attack on the
**cubic-bipartite** and **cubic vertex-transitive** restrictions of the
Erdős–Gyárfás conjecture — exactly the classes the run's verified frontier and
the Gebendorfer girth-6 paper concern. It tells a future agent *what* the
candidate graphs are (toroidal hexagonal skeletons, hyperbolic-surface
truncations, dihedral-scheme truncations, plus the Desargues exception), so a
power-of-two-cycle check can be organised by family rather than by enumeration.
It also fixes the counting/structural reference: the small cubic vertex-transitive
girth-6 census (via Potočnik–Spiga–Verret) is the natural oracle set.

One caveat: this paper is **classification of structure**, not a statement about
cycles of powers of two. It gives the shapes; the power-of-two cycle question on
those shapes is separate and open (the run's cubic-bipartite Moore/Levi-graph
argument in `research/summaries/cubic-bipartite-60.md` is one route into it).

```claim
id: EG-potocnik-vidali-girth6-classification
statement: Every finite simple cubic vertex-transitive graph of girth 6, except the Desargues graph on 20 vertices, is the skeleton of a hexagonal torus tiling, of the truncation of an arc-transitive triangulation of a closed hyperbolic surface, or of the truncation of a 6-regular graph wrt an arc-transitive dihedral scheme.
hypotheses: finite simple cubic (3-regular) vertex-transitive graph with girth exactly 6.
holds-here: true — these are finite simple min-degree-3 graphs relevant to the cubic-bipartite / cubic vertex-transitive restrictions the run attacks.
status: asserted-by-source (peer-reviewed, Discrete Math 2022); classification theorem with full proof on disk.
bearing: fixes the structural census of the cubic-bipartite/vertex-transitive girth-6 classes so power-of-two-cycle questions can be organised by family rather than by enumeration; underpins the Gebendorfer girth-6 (and girth-12) threads.
anchor: research/summaries/potocnik-vidali-cubic-vertex-transitive-girth6-html.md
```
