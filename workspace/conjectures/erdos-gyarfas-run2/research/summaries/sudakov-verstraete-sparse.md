# Sudakov & Verstraëte 2008 — no-2-power-cycle ⇒ sparse

Source: arXiv:0707.2117 "Cycle lengths in sparse graphs" (Benny Sudakov,
Jacques Verstraëte). Full text held as landing page/abstract only;
[[sudakov-verstraete-sparse.full]].

## What it establishes (abstract-level; second part is the E–G relevant one)

- First part (unrelated to E–G): for average degree d and girth g, |C(G)| =
  Ω(d^{⌊(g-1)/2⌋}); longest cycle has length Ω(d^{⌊(g-1)/2⌋}); verifies an
  Erdős conjecture; tight via Moore graphs.
- **Second part (E–G):** they prove a general theorem giving an upper bound on
  the average degree of an n-vertex graph with **no cycle of even length in a
  prescribed infinite sequence**. For the powers of two, the bound is
  **e^{O(log* n)}** on the average degree of a graph of order n with no
  cycle of length in the sequence (log* = iterated logarithm).

## What it implies here

This is the quantifier the obstruction rests on: a graph can avoid 2-power
cycles only if its average degree is ≤ e^{O(log* n)}. Average degree 3 is far
below that, so this theorem **does not** force a 2-power cycle at δ ≥ 3 — it
only says growth is extremely slow (at most iterated-logarithm-subexponential).
The conjecture asserts that degree 3 alone suffices, which is exactly the gap:
the theorem cannot distinguish δ ≤ 3 from the trivial sparse regime, and an
argument for the conjecture cannot come from average-degree growth alone. This
is the structural wall the run's approach must beat — the powers are too
sparse for any interval/average-degree theorem.

```claim
id: sv-sparse-without-2power
statement: An n-vertex graph with no cycle of length a power of two has average degree at most e^{O(log* n)}.
hypotheses: finite simple, no 2-power cycle, n vertices
holds-here: yes (applies, but the bound is subexponential-in-log* and does not rule out degree 3)
status: proved (in source)
bearing: pins the obstruction — average-degree methods cannot force the conjecture at δ ≥ 3
anchor: research/sources/sudakov-verstraete-sparse.full.md
answers: why-averagedegree-approaches-fail
```

```claim
id: sv-odd-cycle-lengths
statement: The number of odd cycle lengths in a graph of chromatic number d and girth g is Ω(d^{⌊(g-1)/2⌋}).
hypotheses: chromatic number d, girth g
holds-here: no (chromatic/girth conditions outside the counterexample frame)
status: proved
bearing: context only
anchor: research/sources/sudakov-verstraete-sparse.full.md
```
