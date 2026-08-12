# Index — code/connectivity

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `verify_connectivity.py` | Glues Markström/Petersen lobes at a single cut vertex (all-single-edge k=3) and asserts the glued cycle set equals the union of the lobe cycle sets, machine-verifying the (a)/(c)/(e) ingredients of the cut-vertex structure lemma; also refutes "δ≥3⇒2-connected" via two K4s+bridge and validates the Markström edge list against graph6. Ran cleanly after fixing oracle unpack (`mine,_`→`_,mine`); output in code/out/connectivity/verify_connectivity.log — union claim holds for both lobes. |
