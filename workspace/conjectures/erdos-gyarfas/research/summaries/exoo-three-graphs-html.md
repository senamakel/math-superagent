> Summary — replaces the digest. Full text: [[exoo-three-graphs-html.full]] (G. Exoo, "Three Graphs and the Erdős-Gyárfás Conjecture", arXiv:1403.5636v1, 22 Mar 2014).

## What the source establishes

Three cubic constructions around the Erdős–Gyárfás conjecture:

1. **G420** — a 3-connected cubic planar graph of order 420 (each vertex of the
   buckyball C60 replaced by the 7-vertex graph H7), with **no cycles of length
   4, 8, or 16**. This shows the exponent m in Heckman–Krakovski's theorem
   (every 3-connected cubic planar graph has a 2^m-cycle, m ≤ 7) cannot be as
   small as 4; it must be at least 5.

2. **G78** — a cubic graph of order 78 (Petersen graph with one vertex replaced
   by a triangle and the other 11 vertices by copies of H7), with **no cycles
   of length 4, 8, or 16**. Appears to be the smallest known such graph
   (unpublished lower bound 54 by Markström).

3. A cubic graph of order 450 (Tutte–Coxeter with each vertex replaced by H15)
   with **no 2^m-cycles for m ≤ 5** (no C4, C8, C16, C32).

Also defines the extremal function f(k) = smallest cubic graph with no
2^m-cycles for m ≤ k, and records:
- f(2) = 10 (three cubic graphs of order 10 with no C4, including the Petersen graph);
- f(3) = 24 (Markström: four graphs, all with C16);
- 54 ≤ f(4) ≤ 78;
- f(5) ≤ 450.
- Cites Markström's result that the four 24-vertex C4,C8-free cubic graphs all contain a C16.

## Implication for this run

**The claim "every C4- and C8-free cubic graph on ≥24 vertices contains a C16"
is FALSE.** G78 (order 78) is a cubic graph with no C4, no C8, and no C16;
G420 is 3-connected cubic planar of order 420 with no C4, C8, or C16. The only
valid scoped statement is Markström's n=24 result (all four 24-vertex C4,C8-free
cubic graphs contain a C16), plus the fact that no cubic counterexample exists
below n=29 (Markström's exhaustive search). G420 also refutes any hope of
"C16 forced" in planar cubic 3-connected graphs: the obstruction can move to
C32 at order 420 (and C60 buckyball-based constructions show planarity does not
force short power-of-two cycles).

```claim
id: EG-exoo-G78-C16-free
statement: It is FALSE that every C4- and C8-free cubic graph on ≥24 vertices contains a C16. Exoo (arXiv:1403.5636) constructs G78, a cubic graph of order 78 with no 4-, 8-, or 16-cycles, and G420, a 3-connected cubic planar graph of order 420 with no C4, C8, or C16. Markström's "all four 24-vertex C4,C8-free cubic graphs contain a C16" holds only at n=24.
hypotheses: cubic, C4-free, C8-free, n≥24.
holds-here: yes — refutes the run's candidate claim; a verification extending "C16 present" beyond n=24 is impossible in this generality.
status: proved by explicit construction in Exoo arXiv:1403.5636.
bearing: claims about C16 in such graphs must be scoped to n=24; the obstruction can move to C32 at order 450.
anchor: research/summaries/exoo-three-graphs-html.md
```