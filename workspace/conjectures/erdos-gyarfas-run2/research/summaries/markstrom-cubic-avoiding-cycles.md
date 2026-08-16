# Markström — Cubic graphs without given cycles (complete search data)

Source: K. Markström, "Cubic graphs without given cycles",
http://abel.math.umu.se/~klasm/Data/cubicavoid.html (Graph6 data). Full text
held; [[markstrom-cubic-avoiding-cycles]].

## The data

- Files `cubic_noX_Y_Z_..._nN.g6` hold **all 3-connected cubic graphs on N
  vertices** avoiding cycles of lengths X,Y,Z,…, found by exhaustive search
  (modified minibaum generator; Fortran90 filter). A *complete* search up to
  the largest N listed for each combination; absence of a file for a given N
  means **no 3-connected cubic graph on that many vertices avoids the stated
  cycles**.
- **He looked for cubic graphs with no cycles of lengths 4, 8, 16: found NO
  such graphs (3-connected cubic) for all N searched.** Exoo found one (78
  vertices).
- He made a complete search for the smallest graphs with no cycles of lengths
  4, 6, 8, 10, 12.

## What it implies here

The complete search for 3-connected cubic graphs avoiding {4,8,16} found none
up to its bound — so, among 3-connected cubic graphs at least, avoiding all
three smallest 2-powers is impossible in the searched range, even though
avoiding {4,8} alone happens at 24 vertices (Markström) and avoiding
{4,8,16} *non-3-connected* happens at 78 (Exoo). This is the sharpest known
evidence that connectivity helps force short 2-powers, and it is the data the
oracle should reproduce (the exhaustive-isomorph-free cycle check over cubic
graphs). The .g6 files are machine-readable ground truth for validating a cycle
checker against.

```claim
id: markstrom-exhaustive-cubic-no-4816
statement: No 3-connected cubic graph avoiding cycles of lengths 4, 8, and 16 exists for all N up to Markström's search bound; the smallest known (non-3-connected) cubic graph avoiding {4,8,16} has 78 vertices (Exoo).
hypotheses: 3-connected cubic graphs, avoiding C4,C8,C16
holds-here: yes — near-miss/verification data
status: catalogued (exhaustive search, Graph6 data)
bearing: connectivity + cubic forces a short 2-power in the searched range; sharp data under the oracle
anchor: research/sources/markstrom-cubic-avoiding-cycles.full.md
```

## What it does not give

The exact largest N searched is not stated on this page (it links to the
paper); the strongest verified claim here is "complete up to the data files".
The non-3-connected case at 78 (Exoo) shows 3-connectivity is what makes the
difference, not mere cubicness.
