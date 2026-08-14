# A Characterization in Z^n of Finite Unit-Distance Graphs in R^n — Chilakamarri 1993

**Source:** doi:10.1006/jctb.1993.1061
**Author:** Kiran B. Chilakamarri, J. Combin. Theory Ser. B 59 (1993) 156–160
**Full text:** not on disk; read via read_sources.

## What this establishes — the primary statement of the lattice criterion

This is the **original 1993 paper** (the 1996 Aequationes paper and the
Chilakamarri–Mahoney 1995 companion are retellings/developments). The theorem:

> A finite graph G is realizable as a unit-distance graph in R^n if and only if
> there exists a mapping f : V(G) → Z^n such that for every edge {u,v} ∈ E(G),
> the Euclidean distance between f(u) and f(v) equals 1 (non-edges
> unconstrained).

i.e. unit-distance realizability in R^n is equivalent to an **integer-lattice
embedding** that preserves unit distances along the edges. The proof is an
algebraic/coordinate-scaling construction. The paper's references ground it in
the Minkowski geometry of numbers and Hadwiger–Klee plane geometry.

## Why it matters here

This upgrades the library's `chilakamarri-lattice-criterion` claim to its
primary source, and it is the exact statement the run can build on: **every**
plane unit-distance graph has an integer-lattice-coordinate embedding realising
its edges. Combined with the 1996 refinement (faithfully √2-recurring, with the
scale d) this gives the lattice a complete search class — point sets can be
searched over Z² with exact arithmetic, never over the continuum with floats.

## Scholar correction — the unit-edge-into-Z^n reading is falsified by K3

The reading recorded above — "edges {u,v} embed to lattice points of Z^n at
Euclidean distance exactly 1" — is **forced to fail** by a computation this
run did not need to run: a unit Euclidean edge in Z^n is an axis-parallel
grid step (step components must lie in {0,±1} with exactly one nonzero), so
the unit-distance graph of Z^n under this reading is bipartite and cannot
contain K3; yet K3 (unit triangle) is a unit-distance graph in R^2. Hence the
stated criterion, taken literally, is false. The falsifier is elementary and
exact (norms of nonzero integer vectors).

The navigable conclusion: the 1993 paper's true statement is not the trivial
bipartite reading above — most likely a scaled / √2-recurring lattice
embedding (as the 1996 note `chilakamarri-unit-distance-lattice.md` records),
which is the form ROOT.md and the durable memory rely on. That form is
**unverified by primary text** (full text network-blocked; the criterion
claim is `held: yes, status: asserted`). The lattice-criterion claim must not
be upgraded past "asserted by source" without the primary text or a second
route, and no construction should be claimed as complete *because of* it.

## Note on download

Full text blocked at network layer. Content from read_sources summary of the
paper itself. Status: **sourced via read_sources (primary paper); full text not
on disk.**