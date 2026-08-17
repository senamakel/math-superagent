# SMQH inner-12 configurations — closed dead end, not a live gap

**Finding (verified against primary artifacts, this cycle).** The standing
"open gap" of the library — the explicit inner-12 configurations behind the
SMQH 32-point no-7-gon result — is a **dead end**: the data was never published.

## What the SMQH paper asserts

Subercaseaux, Mackey, Qian, Heule, "Automated Symmetric Constructions in Discrete
Geometry" (arXiv:2506.00224): the 4-fold-symmetric 32-point no-7-gon SAT formula
has exactly 310,187,713 non-isomorphic satisfying assignments (~1 CPU-year of
enumeration); all share one of **6 non-realizable inner-12 configurations**; hence
no realizable 4-fold-symmetric 32-point no-7-gon set exists. The paper gives
neither coordinates nor orientation tables for the 6 configurations.

## Why it closes (not just "unfound")

1. The paper explicitly states the result without publishing the 6 configurations.
2. The GitHub repository `bsubercaseaux/automatic-symmetries` (full recursive tree
   fetched and held at `research/sources/smqh-repo-tree.full.md`) contains only:
   - `encoders/erdos_szekeres.py` (held), `encoders/everywhere_unbalanced*.py`
   - `experiments/16-6-4sym.sh`, `experiments/16-6-5sym.sh` (the 16-point 6-gon experiments)
   - `realizations/helpers/16-6-4fold-*.txt`, `16-6-5fold-sym.txt`
   - scripts, formulas/, orientations/, solutions/ (all empty `.gitkeep`)
   There is **no inner-12 data, no 32-point no-7-gon data file** anywhere in the tree.

## Consequence

The claim `smqh-no-realizable-4fold-32-no7gon` (that all 310M solutions share 6
non-realizable inner-12 configs) rests on the paper's assertion alone. It cannot
be turned into a concrete forbidden local structure / exact restricted class from
public artifacts; any such extraction would require re-running the full ~1
CPU-year SAT enumeration with the decoder, which is out of scope and not
reproducible here.

**Do not re-search for this data.** This close is a result: the six inner-12
configurations are not available and were never published as data.
