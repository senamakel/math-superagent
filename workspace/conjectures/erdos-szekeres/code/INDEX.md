# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | _(undescribed)_ |
| `brute.py` | Naive exact-arithmetic oracle for the ES convex-position problem: general_position, convex_position (hull test), largest_convex_subset (brute 2^N), and cup/cap spectrum, all on exact Fractions via 3x3 determinants. Exists to pin down the definitions and be the ground truth every faster method is checked against. Validated on hand-known sets (square->4, triangle+interior->3) and on the verified es_construct ES construction (maxConvex==n-1 at n=4,5,6; no convex n-gon at 2^{n-2} points). Capture: code/out/brute_oracle.captured.txt. |
| `checker_disambiguation.py` | Step (1) of the steering directive: tests lib.es_geom's exact oracle alone on 11 point sets whose largest-convex-subset answer is known by hand (circles k=4..16, parabolas/cups, triangle+interior=3, square=4, tri+outside=4). All PASS, exonerating the checker. The failure is in the constructions, not the oracle. |
| `debug_esz.py` | _(undescribed)_ |
| `es_oracle_demo.py` | _(undescribed)_ |
| `oracle_selfcheck.py` | _(undescribed)_ |
| `verify_oracle.py` | _(undescribed)_ |
