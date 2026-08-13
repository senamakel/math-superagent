# Index — code/lib

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `esc_residues.py` | Exact mod-840 coverage facts: per-family residue counts of the five Mordell identities, the six open classes {1,121,169,289,361,529}, their square status mod 840 and ≡1 mod 24 status, smallest uncovered prime (1009). Run as `timeout 540 python3 -m lib.esc_residues` for the report. |
