# Madaras & Tamášová — Minimal unavoidable sets of cycles in plane graphs

Source: T. Madaras, M. Tamášová, "Minimal unavoidable sets of cycles in plane graphs",
Opuscula Math. 38 (2018) 859–878. doi:10.7494/opmath.2018.38.6.859.
Full text: `research/sources/madaras-tamasova-minimal-unavoidable-sets.full.md`
(28 KB converted, 27 KB source).

## What it establishes

Introduces **minimal unavoidable set of cycles**: a set S of cycles is unavoidable
for a graph family G if every G ∈ G contains a cycle from S, and *minimal*
unavoidable if no proper S′ ⊂ S is unavoidable (i.e. for each proper subset there is
an *infinite* subfamily of G avoiding it).

This is a precise frame for the Erdős–Gyárfás conjecture: the conjecture asserts
that S = {2^k : k ≥ 2} is *unavoidable* in the family of graphs of minimum degree
≥ 3, though it is open whether it is even *minimal* unavoidable (an infinite
counterexample-avoiding-a-proper-subset construction is unknown). The paper quotes
Bensmail's q-power results as negative evidence for minimality for q ≥ 3.

## The results (all in plane graphs, δ ≥ 3, family G3)

The paper's concrete theorems are about *short* cycle sets, not powers of two:

- Theorem 3.1: S_{3,4,11} is minimal unavoidable in G3.
- Theorem 3.4: S_{3,4,6,8} and S_{3,4,8,9} are minimal unavoidable in G3.
- Theorem 3.5: S_{3,4,7,9} is minimal unavoidable in G3.
- Theorem 3.6: S_{3,5,6,7} is minimal unavoidable in G3.

The interesting one for E–G is Theorem 3.4's S_{3,4,6,8}: the set {8} appearing
inside a *minimal* unavoidable set in plane graphs is the only direct contact with
powers of two. Many of these minimal sets form a discharging/algebraic obstruction
on the face structure of plane graphs.

## Why it matters for this run

- Reframes E–G as a *minimal unavoidability* statement, which sharpens what a
  counterexample would have to be and connects to the discharging machinery
  (Heckman–Krakovski) already held.
- The discharging charge-transfer rules (Props 3.2, 3.3) are the standard planar
  toolkit; the results apply to plane graphs, not the general δ≥3 class the
  conjecture concerns, so this is adjacent machinery, not a partial result on E–G
  itself.
- Confirms from a peer-reviewed source that {2^k} unavoidability is not known to
  be minimal, and that the min-degree-3 plane-graph case is genuinely the hard
  general case.

## Claim block

```claim
id: madaras-minimal-unavoidable
statement: In the family of plane graphs with minimum degree at least 3, the sets {3,4,11}, {3,4,6,8}, {3,4,8,9}, {3,4,7,9}, {3,5,6,7} are each minimal unavoidable sets of cycles; in particular the face {8} appears in a minimal unavoidable set. Whether {2^k:k≥2} is minimal unavoidable in the family of graphs of minimum degree ≥3 is left open.
hypotheses: connected planar graphs (plane graphs), minimum degree at least 3, no loops/multiedges
holds-here: adjacent machinery — plane graphs, not the general δ≥3 class; the E-G set {2^k} not proven (un)minimal
status: sourced (peer-reviewed, Opuscula Math. 38 (2018))
bearing: reframes E-G as minimal-unavoidability; links to discharging method; {8} in a minimal unavoidable plane set
anchor: research/sources/madaras-tamasova-minimal-unavoidable-sets.full.md
```
