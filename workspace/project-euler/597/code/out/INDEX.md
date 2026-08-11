# Index — code/out

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `exact_p3_extra.json` | Output of code/exact_p3_extra.py: exact rational p(3,L) for the 16 extra integer L values (120,...,5000), plus ncells from the exact arrangement enumeration. Cross-validated two independent enumerators + MC; anchors reproduced exactly before these were computed. |
| `exact_pn.json` | Output of code/arrangement_pn.py: exact rational p(n,L) values (and their floats, and the cell counts) for n=3 and n=4 across a range of integer L, including the anchor checks p(3,160)=56/135 and p(4,400)=0.5107843137. The exact reference values produced by the arrangement solver. |
