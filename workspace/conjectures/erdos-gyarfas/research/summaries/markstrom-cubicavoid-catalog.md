# Markström — "Cubic graphs without given cycles" data catalog

Source: http://abel.math.umu.se/~klasm/Data/cubicavoid.html (live, fetched this run)
Full text: `research/sources/markstrom-cubicavoid-catalog.md`

## What it is

Klas Markström's data directory of cubic graphs avoiding specified cycle lengths,
generated exhaustively with a modified Gunnar Brinkmann `minibaum`. Every listed file
prefix `cubic_noX_Y_Z_..._nN.g6` contains **all 3-connected cubic graphs on N vertices
with no cycles of lengths X, Y, Z, ...**. No file for a given N means none exist.

## The run-relevant assertions (primary source)

1. **"I have looked for cubic graphs with no cycles of lengths 4, 8, 16. I have found no
   such graphs and have searched all N ≤ 52."** — i.e. no 3-connected cubic graph on
   n ≤ 52 vertices simultaneously avoids C4, C8, C16. (Exoo's G78 is the smallest known
   that does, and it is 3-connected cubic: 78 > 52, consistent.)
2. A search for smallest graphs with no cycles of lengths 4, 6, 8, 10, 12 to N ≤ 66:
   none found.
3. Links Exoo's CYCLES catalog for graphs avoiding other lengths, some now proven
   smallest by this exhaustive search.

## Caveat to record

This is the **3-connected** cubic exhaustion (per the page: "all 3-connected cubic
graphs"). The general cubic (or non-3-connected) case to n≤52 is NOT claimed here —
the general cubic C4/C8/C16-free exhaustion to n≤29 is Markström's other result, and the
general min-degree-3 case to n≤15 is Royle's. So the honest statement:
**no 3-connected cubic counterexample on n ≤ 52** (primary, this catalog), and
**no cubic counterexample on n ≤ 29** (Markström's paper), and **no general counterexample
on n ≤ 15** (Royle).

```claim
id: EG-markstrom-3conn-cubic-n52
statement: There is no 3-connected cubic graph on n ≤ 52 vertices with no cycle of length 4, 8, or 16; i.e. no 3-connected cubic counterexample to the Erdős–Gyárfás conjecture below 53 vertices (the conjecture's hypothesis class restricted to 3-connected cubic).
hypotheses: cubic and 3-connected, n ≤ 52, δ=3.
holds-here: yes — the strongest published exhaustion for this class.
status: computed and checked (Markström, exhaustive minibaum search; primary data catalog)
bearing: A would-be 3-connected cubic counterexample has at least 53 vertices; combined with Exoo's G78 (3-connected cubic, C4/C8/C16-free) the true minimum for this class lies in [53, 78].
anchor: research/sources/markstrom-cubicavoid-catalog.md
```