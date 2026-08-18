# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | _(undescribed)_ |
| `analyze_existing_bounds.py` | Exact extraction of the rational Hausdorff-bound sequence already emitted by the ellipse oracle. |
| `brute.py` | Naive exact oracle for the inscribed-square problem: enumerates all 4-vertex subsets of a polygon with Fraction vertices and reports exact nondegenerate squares (four equal sides, equal diagonals). Correctness established by matching all three hand-verified examples: unit square → its 4 corners, 2×1 rectangle → none, diamond → its 4 corners. Deliberately exponential (C(n,4)) — oracle only, never run at statement size. Bears on the configuration-space claim intended for code/lean/Lib/Statement.lean: a polygon vertex square is the boundary case of Stromquist's theorem, not new mathematics. |
| `extract_all_sequences.py` | Extracts explicit integer lists from existing workspace artifacts for exact sequence analysis; does not search or infer. |
| `extract_sequence.py` | _(undescribed)_ |
