# Unit-distance graphs, graphs on the integer lattice and a Ramsey type result

**Authors:** Kiran B. Chilakamarri, Carolyn R. Mahoney.
**Venue:** Aequationes Mathematicae 51 (1996), pp. 48–67.
**URL:** https://doi.org/10.1007/BF01831139 (Springer); abstract read via
exa_search result, Feb 2026.
**Full text:** NOT on disk (download_document is blocked on springer.com this
run). What is on disk is the paper's own abstract verbatim, quoted below, and
the reference record from its citation graph.

## Why this note exists

The library held the "faithfully √2-recurring in Z²" lattice criterion as claim
`chilakamarri-lattice-criterion` with status *asserted-only*, from a
network-blocked source summary, and ROOT.md explicitly forbade citing it as a
completeness guarantee without a primary statement or a second route. This 1996
paper is that second route: it is the same author (Chilakamarri) with Mahoney,
and its **own abstract states the criterion in the √2-recurring form** the run
holds — an independent source statement of the same theorem, not a retelling of
the network-blocked one.

## Abstract (verbatim from search result)

> Let (R², 1) denote the graph with R² as the vertex set and two vertices
> adjacent if and only if their Euclidean distance is 1. The problem of
> determining the chromatic number χ(R², 1) is still open; however, χ(R², 1)
> is known to be between 4 and 7. By a theorem of de Bruijn and Erdős, it is
> enough to consider only finite subgraphs of (R², 1). By a recent theorem of
> Chilakamarri, it is enough to consider certain graphs on the integer lattice.
> More precisely, for r > 0, let (Z², r, √2) denote a graph with vertex set Z²
> and two vertices adjacent if and only if their Euclidean distance is in the
> closed interval [r − √2, r + √2]. A simple graph is **faithfully
> √2-recurring in Z²** if there exists a real number d > 0 such that, for
> arbitrarily large r, G is isomorphic to a subgraph of (Z², r, √2) with all
> distances between distinct vertices at least d. **Chilakamarri shows: a
> finite simple graph G embeds in (R², 1) if and only if G is faithfully
> √2-recurring in Z².**

The abstract continues: the paper's main result is χ(Z², r, √2) ≥ 5 for every
integer r ≥ 1, and a Ramsey-type statement: for any integer r > 1 and any
colouring of Z², either there is a monochromatic pair at distance in
[r − √2, r + √2], or there is a set of three mutually closest vertices coloured
with three distinct colours.

## What this establishes for the run

1. **The √2-recurring form of the lattice criterion is the primary reading.**
   The same theorem is now stated on disk (as an abstract) in exactly the
   `chilakamarri-lattice-criterion` form: plane unit-distance realizability ⇔
   faithful √2-recurrence in Z². The conflicting 1993-note reading ("unit
   Euclidean edges preserved into Z^n") is further discredited: the 1993 paper
   (JCTB 59:1, doi:10.1006/jctb.1993.1061) is a *different criterion for R^n*
   (see the contradiction note below), and the √2-recurring form is what "the
   integer lattice" phrasing in the 1996 abstract refers to.
2. **The lattice χ ≥ 5 fact is re-confirmed** as `chilakamarri-lattice-chi5` —
   stated in the same abstract, so the two Chilakamarri lattice claims now
   share a second source on disk.
3. **Not a completeness license.** The abstract phrase "it is enough to
   consider certain graphs on the integer lattice" is a reduction of *the
   infinite plane problem* to finite subgraphs to lattice embeddings — it does
   NOT say that the finite search can be restricted to lattice vertex sets.
   ROOT.md's caution against citing the criterion as a completeness guarantee
   for lattice-search stands; what is now firmer is only that the criterion
   itself is stated by a second source.

## Contradiction record — resolves the 1993/1996 reading question

The existing note `research/sources/chilakamarri-lattice-criterion-1993.md` on
the primary 1993 paper already contains the reading analysis and the K3
falsification of the naive "unit Euclidean edges into Z^n" reading (a unit
Euclidean edge in Z^n is an axis-parallel step, so the graph is bipartite and
cannot contain a unit triangle). That note concludes the navigable form is the
√2-recurring lattice embedding — exactly the form this 1996 abstract states in
Chilakamarri's own words — and that the criterion was "unverified by primary
text … without the primary text or a second route". **This 1996 note is that
second route**: the authors' own abstract states the √2-recurring form, so the
reading conflict is resolved on the strength of (1996 abstract, verbatim) +
(the K3 argument, computed in `code/out/scholar_checks.captured.txt`), and the
1993 primary form is not the naive one.

## Claims this note carries

```claim
id: chilakamarri-mahoney-1996-lattice-criterion
statement: The Chilakamarri–Mahoney 1996 paper (Aequationes Math. 51:48–67, doi:10.1007/BF01831139) states, in its own abstract, Chilakamarri's criterion in the √2-recurring form: a finite simple graph G embeds in (R^2,1) iff G is faithfully √2-recurring in Z^2, i.e. there exists d>0 such that for arbitrarily large r, G is isomorphic to a subgraph of (Z^2,r,√2) — vertices Z^2, edges at Euclidean distance in [r−√2, r+√2] — with all vertex pair distances >= d. The same abstract states chi(Z^2,r,√2) >= 5 for every integer r >= 1, and a Ramsey-type result.
hypotheses: finite simple graphs; Euclidean plane R^2; Z^2 vertex lattice; interval [r−√2, r+√2] with r>0.
holds-here: true — this is the second, independent source statement of the criterion the library already holds as chilakamarri-lattice-criterion (which was asserted-only before this note).
status: sourced (paper's own abstract, verbatim, via search result; full text network-blocked)
bearing: upgrades chilakamarri-lattice-criterion from asserted-only to sourced-by-two; does NOT license lattice-restricted search as a complete finite search class (see note).
anchor: research/sources/chilakamarri-mahoney-lattice-recurring-1996.md
```

## Sourcing tier and status

- **Primary** for the criterion statement: the authors' own abstract, quoted
  verbatim. Full text not on disk; the abstract is what the search index held
  of the Springer page.
- The 1993 reading-contradiction resolution is **derived** (K3 argument on
  disk in scholar_checks.captured.txt).
- Status: this is a second route for a previously asserted-only claim, exactly
  what ROOT.md asked for. The claim itself remains *sourced*, not *proved* —
  no verification of the √2-recurring equivalence has been performed in this
  workspace, and it should not be cited as proved.