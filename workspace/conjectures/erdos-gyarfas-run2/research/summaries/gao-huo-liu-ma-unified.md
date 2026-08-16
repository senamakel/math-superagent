# Gao, Huo, Liu & Ma 2019 — unified cycle-length conjectures

Source: arXiv:1904.08126 "A unified proof of conjectures on cycle lengths in
graphs". Full text held as landing page / abstract only;
[[gao-huo-liu-ma-unified.full]].

## What it establishes

Unified tight minimum-degree results for paths between two endpoints whose
lengths form a long AP of difference 1 or 2, yielding exact cycle-length
results:
1. δ ≥ k+1 ⇒ cycles of all even lengths mod k; 2-connected non-bipartite ⇒
   cycles of all lengths mod k (Thomassen's conjecture).
2. k-connected ⇒ cycle of length 0 mod k (Dean's conjecture).
3. 3-connected non-bipartite δ ≥ k+1 ⇒ k cycles of consecutive lengths.
4. χ ≥ k+2 ⇒ k cycles of consecutive lengths.

## For this problem

This is the *contrast class* the obstruction section of problem.md points at:
interval/modular results are plentiful and sharp, but none prescribes a
specific power of two. The sparse-powers gap (needing a range of length > 2^k
to be forced to contain one) is exactly why these theorems, however sharp, do
not touch E–G. Recording this here is how the run keeps the obstruction in
view: the machinery that works for intervals/moduli is precisely the machinery
that cannot reach a prescribed sparse length.

```claim
id: ghlu-ma-interval-results
statement: Sharp min-degree/connectivity conditions force long arithmetic progressions or congruence classes of cycle lengths, but none prescribes a specific power of two.
hypotheses: various (min-degree, connectivity, chromatic number)
holds-here: yes as statements, but they do not force a prescribed 2^k (sparse)
status: asserted (abstract)
bearing: names the standard machinery and why it cannot reach E-G's prescribed sparse length
anchor: research/sources/gao-huo-liu-ma-unified.full.md
answers: why-intervalmodulo-tools-fail-here
```
