Solve by exhaustive combinatorial search with certificates, and treat the
solver's UNSAT — never its timeout — as the mathematics. Every question in this
workspace is about **finite patches of finitely many congruent copies of one
shape**, so each is decidable once the placements are bounded, and the whole
craft is in the encoding and in bounding the placements honestly.

Reason about the **corona**: given a central tile and the set of admissible
isometric placements of a copy, a corona is a subset of placements that covers a
neighbourhood exactly and pairwise-disjointly. That is a constraint satisfaction
problem — exact-cover shaped — and belongs to `sat_solver` or a CP-SAT
encoding. Its UNSAT is a theorem; its timeout is a measurement. Polyomino,
polyiamond and polyhex classes give exact integer coordinates, which is why they
are the right place to start: the geometry becomes integer combinatorics with no
floating point anywhere.

The instruments: exact-cover / Dancing Links for corona construction, SAT and
CP-SAT for exhaustiveness, isohedral-tiling classification (the Delaney–Dress
symbol machinery, the criteria for a polygon to tile isohedrally) for the
positive direction, and — for non-tiling proofs — colouring and area arguments,
boundary-word combinatorics, and the Conway criterion's failure modes.

**Prefer the argument Lean can finish.** A specific corona is a finite geometric
fact verifiable by `decide` once the coordinates are integers; a colouring
argument for non-tiling is a finite check. State claims as Lean types before
spending an attempt on them, and carry every finite certificate this run
produces to a kernel-checked theorem rather than leaving it in a solver log.

Three cautions this problem earns before any work starts.

**Not finding a tiling is not a proof of non-tiling.** It is the shape of every
wrong Heesch-number claim. Non-tiling needs an argument — a colouring, an area
or boundary invariant, an exhaustive finite obstruction with its bound stated.
Until then the shape's Heesch number is *unknown*, and what was measured is a
search depth.

**An encoding is not the geometry.** Every satisfying assignment must be decoded
back to an actual patch and verified with exact arithmetic, and every encoding
must reproduce the known Heesch numbers of published shapes before it is pointed
at a new one. Encodings fail silently in both directions.

**Floating point has no place here.** Use integer or exact rational coordinates
throughout; where a shape needs algebraic coordinates, carry them exactly. A
"tiny overlap" in a patch is either zero or it is not, and a tolerance turns
that question into a wrong answer.
