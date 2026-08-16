# Index — code/lib

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

> **VERIFIED ES lower-bound construction: `es_construct.py` ONLY.** The three
> construction modules below ending in `.quarantined` are defective — do not
> import them, and do not build on them. A later agent must measure every
> argument against `es_construct.es_set` / `es_set_blocks`.

| File | Purpose |
| --- | --- |
| `cupcap.py` | Exact cup/cap predicates (is_cup, is_cap using Fraction slope comparisons, distinct-x required) and the G-cupcap characterization predicate exists_cupcap(X,n) — a k-cup plus (n+2−k)-cap sharing leftmost/rightmost points by x whose union is n points in convex position — plus convex_by_cupcap and the shared_extreme_nonconvex_pairs diagnostic. Validated against an independent Fraction reference on every subset of every tested set, and against the es_geom oracle on 624 sets / 1220 cases (see code/cupcap/verify.py and code/out/cupcap_verify.txt). |
| `es_construct.py` | **THE verified ES lower-bound construction.** `es_set(n)` / `es_set_blocks(n)` realize 2^{n-2} points in general position with no convex n-gon in exact rationals; verified by the exact oracle `es_geom` (largest convex subset = n−1 at n=4,5,6; no convex 7-gon at n=7) and independently by a from-scratch gift-wrapping hull (`code/out/verify_es_construct_indep.py`). This is the single construction every later argument is measured against. |
| `es_construction.py.quarantined` | **QUARANTINED — known-defective, do not import.** (renamed from `es_construction.py`). `es_lower_set` uses floating-point radial placement + integer rounding and fails general position at n≥5 (largestConvex 5 at n=5, 8 at n=6); `cups_caps_block` also violates its own cap/cup bounds. Superseded by `es_construct.py`. Kept on disk for the record of the failure. |
| `es_geom.py` | The exact planar-geometry oracle (checker): `orient`, `in_general_position`, `convex_hull`, `in_convex_position`, `largest_convex_subset`, `has_convex_k_subset`, and cup/cap spectra — exact integer/Fraction arithmetic, never floating point. Verified correct on hand-known sets in the checker-vs-construction disambiguation (`code/out/checker_vs_construction_resolution.md`). |
| `es_lower.py.quarantined` | **QUARANTINED — unverified, superseded, do not import.** (renamed from `es_lower.py`). Exact-rational recursive `g(a,b)` + parabola placement; never oracle-verified as a whole and superseded by `es_construct.py`. Kept on disk for the record of the failure. |
| `esz.py.quarantined` | **QUARANTINED — known-defective, do not import.** (renamed from `esz.py`). `es_set` (exact arc placement) leaks a convex n-gon: largestConvex 6 at n=5, 9 at n=6. Superseded by `es_construct.py`. Kept on disk for the record of the failure. |
