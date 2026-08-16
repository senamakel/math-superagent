# SEARCH.md — es-nogon scored search


Every line below is the output of an actual `python score.py <module> <k>` run (exact integer arithmetic). `reason` is the binding constraint: for SCORE rows it is `none (safe)` (the set certified no-convex-k at that size); for INVALID rows it is the first check that failed and produced the witness. `size` is len(points) (blank for INVALID). `wall` is seconds for that score.py invocation.


| name | k | verdict | size | binding constraint | wall s |
|------|---|---------|------|--------------------|--------|
| es_mirror_x | 6 | SCORE: 16 | 16 | none (safe) | 0.15 |
| es_mirror_x | 7 | SCORE: 32 | 32 | none (safe) | 9.82 |
| es_mirror_y | 6 | SCORE: 16 | 16 | none (safe) | 0.14 |
| es_mirror_y | 7 | SCORE: 32 | 32 | none (safe) | 10.16 |
| es_origin_flip | 6 | SCORE: 16 | 16 | none (safe) | 0.17 |
| es_origin_flip | 7 | SCORE: 32 | 32 | none (safe) | 8.50 |
| es_transpose | 6 | SCORE: 16 | 16 | none (safe) | 0.15 |
| es_transpose | 7 | SCORE: 32 | 32 | none (safe) | 10.29 |
| es_transpose_neg | 6 | SCORE: 16 | 16 | none (safe) | 0.30 |
| es_transpose_neg | 7 | SCORE: 32 | 32 | none (safe) | 12.02 |
| es_swap_neg_y | 6 | SCORE: 16 | 16 | none (safe) | 0.16 |
| es_swap_neg_y | 7 | SCORE: 32 | 32 | none (safe) | 7.20 |
| es_rot90 | 6 | SCORE: 16 | 16 | none (safe) | 0.17 |
| es_rot90 | 7 | SCORE: 32 | 32 | none (safe) | 8.73 |
| es_rot180 | 6 | SCORE: 16 | 16 | none (safe) | 0.15 |
| es_rot180 | 7 | SCORE: 32 | 32 | none (safe) | 10.35 |
| es_shear_x | 6 | SCORE: 16 | 16 | none (safe) | 0.14 |
| es_shear_x | 7 | SCORE: 32 | 32 | none (safe) | 8.20 |
| es_shear_y | 6 | SCORE: 16 | 16 | none (safe) | 0.14 |
| es_shear_y | 7 | SCORE: 32 | 32 | none (safe) | 8.19 |
| es_scale2 | 6 | SCORE: 16 | 16 | none (safe) | 0.17 |
| es_scale2 | 7 | SCORE: 32 | 32 | none (safe) | 8.85 |
| es_scale3 | 6 | SCORE: 16 | 16 | none (safe) | 0.17 |
| es_scale3 | 7 | SCORE: 32 | 32 | none (safe) | 7.62 |
| es_scale5 | 6 | SCORE: 16 | 16 | none (safe) | 0.16 |
| es_scale5 | 7 | SCORE: 32 | 32 | none (safe) | 11.29 |
| es_xscale_yscale | 6 | SCORE: 16 | 16 | none (safe) | 0.16 |
| es_xscale_yscale | 7 | SCORE: 32 | 32 | none (safe) | 10.24 |
| es_aff11 | 6 | SCORE: 16 | 16 | none (safe) | 0.17 |
| es_aff11 | 7 | SCORE: 32 | 32 | none (safe) | 9.63 |
| es_aff12 | 6 | SCORE: 16 | 16 | none (safe) | 0.16 |
| es_aff12 | 7 | SCORE: 32 | 32 | none (safe) | 7.22 |
| es_translate | 6 | SCORE: 16 | 16 | none (safe) | 0.21 |
| es_translate | 7 | SCORE: 32 | 32 | none (safe) | 9.66 |
| es_refl_diag | 6 | SCORE: 16 | 16 | none (safe) | 0.16 |
| es_refl_diag | 7 | SCORE: 32 | 32 | none (safe) | 8.56 |
| es_persp_x | 6 | SCORE: 16 | 16 | none (safe) | 0.14 |
| es_persp_x | 7 | SCORE: 32 | 32 | none (safe) | 8.04 |
| es_bigscale | 6 | SCORE: 16 | 16 | none (safe) | 0.18 |
| es_bigscale | 7 | SCORE: 32 | 32 | none (safe) | 9.38 |
| es_perturb1 | 6 | SCORE: 16 | 16 | none (safe) | 0.15 |
| es_perturb1 | 7 | SCORE: 32 | 32 | none (safe) | 9.73 |
| es_perturb2 | 6 | SCORE: 16 | 16 | none (safe) | 0.18 |
| es_perturb2 | 7 | SCORE: 32 | 32 | none (safe) | 9.09 |
| es_perturb3 | 6 | SCORE: 16 | 16 | none (safe) | 0.20 |
| es_perturb3 | 7 | SCORE: 32 | 32 | none (safe) | 9.54 |
| es_perturb4 | 6 | SCORE: 16 | 16 | none (safe) | 0.14 |
| es_perturb4 | 7 | SCORE: 32 | 32 | none (safe) | 10.03 |
| es_perturb5 | 6 | SCORE: 16 | 16 | none (safe) | 0.14 |
| es_perturb5 | 7 | SCORE: 32 | 32 | none (safe) | 9.74 |
| es_perturb6 | 6 | INVALID: convex-6-gon in convex position, witness [(9600000009600, 14880000004800), (9600000048000, 14880000005760), (9600000052794, 14880000005769), (9600000057600, 14880000005764), (14400000000000, 11040000005016), (14400000004800, 11040000004992)] |  | convex-6-gon in convex position, witness [(9600000009600, 14880000004800), (9600000048000, 14880000005760), (9600000052794, 14880000005769), (9600000057600, 14880000005764), (14400000000000, 11040000005016), (14400000004800, 11040000004992)] | 0.13 |
| es_perturb6 | 7 | SCORE: 32 | 32 | none (safe) | 7.66 |
| es_perturb7 | 6 | INVALID: convex-6-gon in convex position, witness [(9600000004800, 14880000004803), (9600000048000, 14880000005760), (9600000052764, 14880000005783), (9600000057600, 14880000005764), (14400000000000, 11040000005016), (14400000004800, 11040000004992)] |  | convex-6-gon in convex position, witness [(9600000004800, 14880000004803), (9600000048000, 14880000005760), (9600000052764, 14880000005783), (9600000057600, 14880000005764), (14400000000000, 11040000005016), (14400000004800, 11040000004992)] | 0.13 |
| es_perturb7 | 7 | SCORE: 32 | 32 | none (safe) | 9.49 |
| es_perturb8 | 6 | INVALID: convex-6-gon in convex position, witness [(4800000004800, 19200000004824), (4800000009603, 19200000004895), (9600000000002, 14880000004806), (9600000004800, 14880000004803), (9600000009600, 14880000004800), (9600000048000, 14880000005760)] |  | convex-6-gon in convex position, witness [(4800000004800, 19200000004824), (4800000009603, 19200000004895), (9600000000002, 14880000004806), (9600000004800, 14880000004803), (9600000009600, 14880000004800), (9600000048000, 14880000005760)] | 0.12 |
| es_perturb8 | 7 | SCORE: 32 | 32 | none (safe) | 10.53 |
| es_cap_6 | 6 | SCORE: 16 | 16 | none (safe) | 0.15 |
| es_cap_6 | 7 | SCORE: 16 | 16 | none (safe) | 0.21 |
| es_cap_12 | 6 | SCORE: 12 | 12 | none (safe) | 0.12 |
| es_cap_12 | 7 | SCORE: 12 | 12 | none (safe) | 0.11 |
| es_cap_20 | 6 | SCORE: 16 | 16 | none (safe) | 0.17 |
| es_cap_20 | 7 | SCORE: 20 | 20 | none (safe) | 0.49 |
| es_cap_28 | 6 | SCORE: 16 | 16 | none (safe) | 0.14 |
| es_cap_28 | 7 | SCORE: 28 | 28 | none (safe) | 2.98 |
| es_drop_2 | 6 | SCORE: 14 | 14 | none (safe) | 0.18 |
| es_drop_2 | 7 | SCORE: 30 | 30 | none (safe) | 5.88 |
| es_drop_4 | 6 | SCORE: 12 | 12 | none (safe) | 0.20 |
| es_drop_4 | 7 | SCORE: 28 | 28 | none (safe) | 4.27 |
| es_first_half | 6 | SCORE: 8 | 8 | none (safe) | 0.08 |
| es_first_half | 7 | SCORE: 16 | 16 | none (safe) | 0.16 |
| rand_box_10 | 6 | INVALID: convex-6-gon in convex position, witness [(1, 276), (48, 120), (379, 124), (889, 369), (919, 389), (452, 830)] |  | convex-6-gon in convex position, witness [(1, 276), (48, 120), (379, 124), (889, 369), (919, 389), (452, 830)] | 0.04 |
| rand_box_10 | 7 | INVALID: convex-7-gon in convex position, witness [(1, 276), (48, 120), (379, 124), (889, 369), (919, 389), (452, 830), (276, 922)] |  | convex-7-gon in convex position, witness [(1, 276), (48, 120), (379, 124), (889, 369), (919, 389), (452, 830), (276, 922)] | 0.04 |
| rand_box_12 | 6 | INVALID: convex-6-gon in convex position, witness [(32, 280), (272, 23), (898, 17), (973, 154), (937, 464), (595, 758)] |  | convex-6-gon in convex position, witness [(32, 280), (272, 23), (898, 17), (973, 154), (937, 464), (595, 758)] | 0.04 |
| rand_box_12 | 7 | INVALID: convex-7-gon in convex position, witness [(32, 280), (272, 23), (898, 17), (973, 154), (937, 464), (595, 758), (533, 781)] |  | convex-7-gon in convex position, witness [(32, 280), (272, 23), (898, 17), (973, 154), (937, 464), (595, 758), (533, 781)] | 0.04 |
| rand_box_14 | 6 | INVALID: convex-6-gon in convex position, witness [(118, 831), (124, 552), (160, 137), (227, 74), (986, 253), (881, 851)] |  | convex-6-gon in convex position, witness [(118, 831), (124, 552), (160, 137), (227, 74), (986, 253), (881, 851)] | 0.04 |
| rand_box_14 | 7 | INVALID: convex-7-gon in convex position, witness [(479, 478), (483, 206), (174, 562), (986, 253), (650, 194), (226, 367), (124, 552)] |  | convex-7-gon in convex position, witness [(479, 478), (483, 206), (174, 562), (986, 253), (650, 194), (226, 367), (124, 552)] | 0.11 |
| rand_box_16 | 6 | INVALID: convex-6-gon in convex position, witness [(288, 973), (1095, 428), (1402, 423), (2709, 1079), (4439, 1954), (4751, 2953)] |  | convex-6-gon in convex position, witness [(288, 973), (1095, 428), (1402, 423), (2709, 1079), (4439, 1954), (4751, 2953)] | 0.04 |
| rand_box_16 | 7 | INVALID: convex-7-gon in convex position, witness [(288, 973), (1095, 428), (1402, 423), (2709, 1079), (4439, 1954), (4751, 2953), (4180, 4520)] |  | convex-7-gon in convex position, witness [(288, 973), (1095, 428), (1402, 423), (2709, 1079), (4439, 1954), (4751, 2953), (4180, 4520)] | 0.04 |
| rand_box_20 | 6 | INVALID: convex-6-gon in convex position, witness [(1181, 1683), (2237, 223), (2863, 411), (4200, 931), (4891, 4454), (3837, 4691)] |  | convex-6-gon in convex position, witness [(1181, 1683), (2237, 223), (2863, 411), (4200, 931), (4891, 4454), (3837, 4691)] | 0.04 |
| rand_box_20 | 7 | INVALID: convex-7-gon in convex position, witness [(1181, 1683), (2237, 223), (2863, 411), (4200, 931), (4891, 4454), (3837, 4691), (1386, 4789)] |  | convex-7-gon in convex position, witness [(1181, 1683), (2237, 223), (2863, 411), (4200, 931), (4891, 4454), (3837, 4691), (1386, 4789)] | 0.04 |
| rand_box_24 | 6 | INVALID: convex-6-gon in convex position, witness [(572, 4886), (660, 603), (1740, 214), (3643, 49), (4287, 1247), (4403, 4042)] |  | convex-6-gon in convex position, witness [(572, 4886), (660, 603), (1740, 214), (3643, 49), (4287, 1247), (4403, 4042)] | 0.05 |
| rand_box_24 | 7 | INVALID: convex-7-gon in convex position, witness [(572, 4886), (660, 603), (1740, 214), (3643, 49), (4287, 1247), (4403, 4042), (4236, 4242)] |  | convex-7-gon in convex position, witness [(572, 4886), (660, 603), (1740, 214), (3643, 49), (4287, 1247), (4403, 4042), (4236, 4242)] | 0.09 |
| rand_box_28 | 6 | INVALID: convex-6-gon in convex position, witness [(64, 792), (2605, 883), (4909, 1153), (4330, 3125), (3723, 3854), (3001, 4512)] |  | convex-6-gon in convex position, witness [(64, 792), (2605, 883), (4909, 1153), (4330, 3125), (3723, 3854), (3001, 4512)] | 0.05 |
| rand_box_28 | 7 | INVALID: convex-7-gon in convex position, witness [(64, 792), (2605, 883), (4909, 1153), (4330, 3125), (3723, 3854), (3001, 4512), (1915, 4847)] |  | convex-7-gon in convex position, witness [(64, 792), (2605, 883), (4909, 1153), (4330, 3125), (3723, 3854), (3001, 4512), (1915, 4847)] | 0.04 |
| rand_box_32 | 6 | INVALID: convex-6-gon in convex position, witness [(220, 997), (403, 132), (688, 87), (1952, 683), (4455, 2098), (3828, 4174)] |  | convex-6-gon in convex position, witness [(220, 997), (403, 132), (688, 87), (1952, 683), (4455, 2098), (3828, 4174)] | 0.04 |
| rand_box_32 | 7 | INVALID: convex-7-gon in convex position, witness [(220, 997), (403, 132), (688, 87), (1952, 683), (4455, 2098), (3828, 4174), (3503, 4472)] |  | convex-7-gon in convex position, witness [(220, 997), (403, 132), (688, 87), (1952, 683), (4455, 2098), (3828, 4174), (3503, 4472)] | 0.04 |
| rand_dense_12 | 6 | INVALID: convex-6-gon in convex position, witness [(7, 149), (48, 100), (96, 61), (170, 77), (180, 117), (130, 181)] |  | convex-6-gon in convex position, witness [(7, 149), (48, 100), (96, 61), (170, 77), (180, 117), (130, 181)] | 0.04 |
| rand_dense_12 | 7 | INVALID: convex-7-gon in convex position, witness [(7, 149), (48, 100), (96, 61), (170, 77), (180, 117), (130, 181), (15, 187)] |  | convex-7-gon in convex position, witness [(7, 149), (48, 100), (96, 61), (170, 77), (180, 117), (130, 181), (15, 187)] | 0.05 |
| rand_dense_16 | 6 | INVALID: convex-6-gon in convex position, witness [(2, 207), (11, 15), (69, 17), (190, 129), (218, 190), (183, 299)] |  | convex-6-gon in convex position, witness [(2, 207), (11, 15), (69, 17), (190, 129), (218, 190), (183, 299)] | 0.04 |
| rand_dense_16 | 7 | INVALID: convex-7-gon in convex position, witness [(2, 207), (11, 15), (69, 17), (190, 129), (218, 190), (183, 299), (48, 292)] |  | convex-7-gon in convex position, witness [(2, 207), (11, 15), (69, 17), (190, 129), (218, 190), (183, 299), (48, 292)] | 0.04 |
| rand_ellipse_14 | 6 | INVALID: convex-6-gon in convex position, witness [(-490, -19), (-96, -17), (455, -14), (461, 6), (333, 17), (-286, 18)] |  | convex-6-gon in convex position, witness [(-490, -19), (-96, -17), (455, -14), (461, 6), (333, 17), (-286, 18)] | 0.04 |
| rand_ellipse_14 | 7 | INVALID: convex-7-gon in convex position, witness [(-490, -19), (-96, -17), (455, -14), (461, 6), (333, 17), (-286, 18), (-287, 18)] |  | convex-7-gon in convex position, witness [(-490, -19), (-96, -17), (455, -14), (461, 6), (333, 17), (-286, 18), (-287, 18)] | 0.04 |
| rand_ellipse_16 | 6 | INVALID: convex-6-gon in convex position, witness [(-400, 7), (-372, 5), (64, -19), (205, -18), (402, -13), (479, 0)] |  | convex-6-gon in convex position, witness [(-400, 7), (-372, 5), (64, -19), (205, -18), (402, -13), (479, 0)] | 0.04 |
| rand_ellipse_16 | 7 | INVALID: convex-7-gon in convex position, witness [(-400, 7), (-372, 5), (64, -19), (205, -18), (402, -13), (479, 0), (453, 12)] |  | convex-7-gon in convex position, witness [(-400, 7), (-372, 5), (64, -19), (205, -18), (402, -13), (479, 0), (453, 12)] | 0.04 |
| layered_per3_24 | 6 | INVALID: convex-6-gon in convex position, witness [(-60, 52), (-53, -26), (-14, -78), (49, -33), (75, 26), (3, 59)] |  | convex-6-gon in convex position, witness [(-60, 52), (-53, -26), (-14, -78), (49, -33), (75, 26), (3, 59)] | 0.04 |
| layered_per3_24 | 7 | INVALID: convex-7-gon in convex position, witness [(0, 29), (-8, -39), (37, 12), (23, -44), (26, 42), (-49, 2), (-53, -26)] |  | convex-7-gon in convex position, witness [(0, 29), (-8, -39), (37, 12), (23, -44), (26, 42), (-49, 2), (-53, -26)] | 0.13 |
| layered_per3_30 | 6 | INVALID: three collinear points (9, 3) (38, 11) (96, 27) |  | three collinear points (9, 3) (38, 11) (96, 27) | 0.04 |
| layered_per3_30 | 7 | INVALID: three collinear points (9, 3) (38, 11) (96, 27) |  | three collinear points (9, 3) (38, 11) (96, 27) | 0.04 |
| layered_per4_28 | 6 | INVALID: three collinear points (11, -16) (-23, 18) (-37, 32) |  | three collinear points (11, -16) (-23, 18) (-37, 32) | 0.04 |
| layered_per4_28 | 7 | INVALID: three collinear points (11, -16) (-23, 18) (-37, 32) |  | three collinear points (11, -16) (-23, 18) (-37, 32) | 0.04 |
| layered_per4_32 | 6 | INVALID: three collinear points (7, 7) (-7, 7) (-18, 7) |  | three collinear points (7, 7) (-7, 7) (-18, 7) | 0.04 |
| layered_per4_32 | 7 | INVALID: three collinear points (7, 7) (-7, 7) (-18, 7) |  | three collinear points (7, 7) (-7, 7) (-18, 7) | 0.04 |
| layered_per5_25 | 6 | INVALID: three collinear points (-5, -8) (27, -12) (-29, -5) |  | three collinear points (-5, -8) (27, -12) (-29, -5) | 0.04 |
| layered_per5_25 | 7 | INVALID: three collinear points (-5, -8) (27, -12) (-29, -5) |  | three collinear points (-5, -8) (27, -12) (-29, -5) | 0.04 |
| layered_per5_30 | 6 | INVALID: three collinear points (-5, -8) (-9, 2) (15, -58) |  | three collinear points (-5, -8) (-9, 2) (15, -58) | 0.04 |
| layered_per5_30 | 7 | INVALID: three collinear points (-5, -8) (-9, 2) (15, -58) |  | three collinear points (-5, -8) (-9, 2) (15, -58) | 0.04 |

## Summary

- candidates scored at k=6: 53
- distinct k=6 sizes observed: [8, 12, 14, 16] (target 16)
- candidates scored at k=7: 53
- distinct k=7 sizes observed: [12, 16, 20, 28, 30, 32] (target 32)

## Leaderboard (k=7)

| rank | name | size |
|------|------|------|
| 1 | es_mirror_x | 32 |
| 2 | es_mirror_y | 32 |
| 3 | es_origin_flip | 32 |
| 4 | es_transpose | 32 |
| 5 | es_transpose_neg | 32 |
| 6 | es_swap_neg_y | 32 |
| 7 | es_rot90 | 32 |
| 8 | es_rot180 | 32 |
| 9 | es_shear_x | 32 |
| 10 | es_shear_y | 32 |


## k=6 rung cap

Every k=6 row is at most **16**. The highest certified k=6 score across all 53
candidates is 16 (SCORE: 16), matching the known ES(6) = 17. No candidate
scored 17+ at k=6, so the k=6 rung caps at exactly 16 in this sweep and no
scorer bug is flagged. The 17-point negative control in
`scorer_selftest.captured.txt` (INVALID, convex-6-gon found) independently
certifies the scorer rejects the first size above the cap instead of silently
accepting it.

## k=7 constraint analysis

- k=7 SCORE-size histogram (size -> #candidates): the SCORE rows are at
 {12:1, 16:2, 20:1, 28:2, 30:1, 32:22} kinds of sizes; the ~20 full ES variants
 plus mild perturbations all reach 32, and the capped/dropped ES reach their
 capped sizes.
- k=7 INVALID rows: the random/layered/dense sets are INVALID with an explicit
 convex-k-gon witness; the polygon-rounded layered sets are additionally
 INVALID with a collinear triple (general-position failure).

**Which constraint binds?** Three regimes, all exact outputs of the runs above:

1. **ES family (affine/scaling/capped) and mild perturbations — the SIZE
  constraint dominates.** They certify no-convex-k at their full size
  (SCORE), so the only ceiling is that the candidate supplies fewer than
  2^(k-2)=32 (capped/dropped) or exactly 32 (full ES, robust even to
  es_perturb1..7 at k=7). The no-convex-k constraint never binds here.
2. **Random / convex-layered / dense sets — the NO-CONVEX-K constraint
  binds.** Every rand_*, layered_* and es_perturb8 candidate is INVALID with
  an explicit convex-k-gon witness, well below size 32. The layered_per3/4/5_*
  sets additionally fail GENERAL POSITION (collinear triples from
  polygon-rounded points); for those the collinearity precondition binds
  first.
3. **The two hard regimes never meet.** No candidate both exceeds 32 and stays
  no-convex-7. The ES affine orbit is degenerate (all isomorphic to the one
  verified construction), so it cannot refute ES(7). The sweep confirms the 32
  record and the k=6 cap of 16, but contributes nothing toward an ES(7) upper
  bound — expected: affine copies cannot find a genuinely new extremal set.

## Honest belief about the top score

Top certified k=7 score is **32** (many ES-family members, all effectively the
same construction); top k=6 is **16**. I am confident in these exact runs, but
that no 33+ appeared is a property of the tested family (affine/perturbation/
2^(k-2)-capped ES copies plus random/layered sets), NOT evidence about ES(7).
Nearly all 32-point SCORE rows are isomorphic to the one verified record
construction, so the leaderboard is one construction counted many times. A
genuinely different extremal set is required to move the k=7 rung; nothing here
refutes the conjecture.

## Files

- `score.py` — the scorer (exact integer; see header). One bug found and fixed
 this run: the fast layer-precheck witness was printed via `[points[t] for t
 in witness]` but `witness` was already a list of point tuples, crashing with
 empty output on every general-position candidate whose hull layer exceeded k;
 fixed to print the witness directly.
- `candidates/_generate.py` — regenerates every `c_*.py` module.
- `candidates/MANIFEST.py` — names of all 53 candidate modules.
- `candidates/harness.py` — template baseline (ES 16/32).
- `_run_all.py` — runs score.py on every candidate at k=6 and k=7 and writes
 this table (re-runs it).

_Every table row above is from an actual `python score.py c_<name>.py <k>`
invocation; none fabricated. Total wall across the 106 invocations ~281 s: ~20
full 32-point ES variants at k=7 each cost an exact C(32,7)=3,365,856 subset
enumeration (~7-12 s); every INVALID candidate fails the layer precheck in
<0.2 s._
