# de Bruijn & Erdős (1951) — A Colour Problem for Infinite Graphs and a Problem in the Theory of Relations

**Source URL:** https://doi.org/10.1016/s1385-7258(51)50053-7
(Erdős archive copy: https://www.renyi.hu/~p_erdos/1951-01.pdf — unreachable from this run)
Full text: `research/sources/de-bruijn-erdos-1951.full.md` (bibliographic record; original text could not be fetched).

**Citation:** N. G. de Bruijn and P. Erdős, *A colour problem for infinite graphs and a problem in the theory of relations*, Indagationes Mathematicae (Proceedings) **54** (1951), 371–373.

## Exact result statement

**De Bruijn–Erdős compactness theorem for graph colouring.** For every graph `G`
(finite or infinite),

```
χ(G) = sup { χ(H) : H a finite subgraph of G }.
```

Equivalent form (the finite-subgraph reduction): if every finite subgraph of `G`
is `k`-colourable for some positive integer `k`, then `G` itself is
`k`-colourable. Contrapositive used below: if `χ(G) > k` — in particular if
`χ(G)` is infinite — then some **finite** subgraph has chromatic number `> k`.

## Hypotheses

- `G` is an arbitrary (simple) graph; the vertex set may be infinite, even
  uncountable.
- `k` is a positive integer. (The theorem is about ordinary, finite chromatic
  number; uncountable-chromatic analogues need stronger assumptions and are a
  separate, harder subject — see the Komjáth survey.)
- The proof is a compactness argument and needs a choice principle — equivalent
  in strength to the Boolean prime ideal theorem (or Tychonoff's theorem for
  compact Hausdorff spaces). For **countable** graphs the argument goes through
  without any choice via König's lemma. One does **not** need full ZFC choice.
- It is not a theorem of ZF alone for uncountable graphs; there are
  ZF-models where it fails.

## The Hadwiger–Nelson reduction (why this run cares)

Let `G` be the unit-distance graph on all of `R²`: vertices are points, `x ~ y`
iff `|x − y| = 1` exactly. By the theorem, `χ(G) = sup χ(H)` over finite
subgraphs `H`, so:

- **raising the lower bound** `4 → 5` is exactly the task of finding a **finite**
  unit-distance graph that is not `4`-colourable — a finite object, nothing
  infinite to reason about;
- **proving an upper bound** `χ(G) ≤ c` is exactly `4 ≤ χ(H) ≤ c` for every
  finite subgraph (matching the known `7`-colour hexagonal covering).

This is the single structural fact that makes the whole infinite problem a
finite-combinatorial search. It is a cited, standard theorem; the statement is
corroborated by the original-paper record, Péter Komjáth's survey *The chromatic
number of infinite graphs* (Discrete Math 2010, DOI 10.1016/j.disc.2010.11.004),
Lambie-Hanson & Rinot (2017), and the Chen–Chvátal survey (2007).

## Second part of the paper ("a problem in the theory of relations")

The 1951 paper's title advertises a second, relational problem. The paper stated
a theorem on colouring the points of the plane so that points at any of a set of
specified mutual distances are differently coloured — the direct ancestor of the
Hadwiger–Nelson question (there the context is colouring under a family of
forbidden distances). This run could not fetch the full text to quote it
verbatim (see gap); the graph-colouring compactness theorem is the part that is
universally cited and used.

## Status

- **Sourced, standard theorem** (compactness/choice content). The exact
  statement, hypotheses, and choice-principle dependence are corroborated by
  multiple independent indexing records and surveys.
- **Unverified locally:** the verbatim 1951 text and the precise wording of the
  "theory of relations" half were not retrievable (reported in FRONTIER.md.)
- **Application verified:** this run's own exact-arithmetic oracle uses the
  reduction in the simplest case — a single finite `7`-vertex graph of chromatic
  number `4` — as its calibration target (see `code/brute.py`).
