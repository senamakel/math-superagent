# Index — code/scholar

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `cell_degree_check.py` | Independent mechanical confirmation that the fold cell degree is 2^popcount(d) (not popcount(d)); enumerate |
| `downset_verify.py` | Independent exact brute-submask verification of claim downset-row-intersection-meet-formula (meet + intersection-size + symdiff-size for fold rows M_d, n=4..199) with a random negative control; hand to coder/tool_builder as the machine route. |
| `lacasa_parity_projection_check.py` | Confirms (A) abstract mod-6-to-parity projection surjectivity for all m and (B) all binary blocks present in the real prime parity string at small order — the confirmation (not the evidence) for claim lacasa-mod6-forbidden-blocks-parity-invisible. |
| `lacasa_projection_check.py` | SUPERSEDED stub pointing to projection_erasure_check.py + lacasa_parity_projection_check.py; contains no load-bearing code. |
| `mr_gap_correlation_probe.py` | Empirical probe of whether the Mauduit–Rivat digit-sum statistic correlates with the gap-parity string h the SUPPLY fold reads (P(h=1 |
| `projection_erasure_check.py` | Consolidated numerical corroboration for two proved parity-projection conclusions: (A) the Lacasa mod-6 forbidden-block erasure (every F₂^m parity string realizable by an admissible 6-block — confirms lacasa-mod6-forbidden-blocks-parity-invisible) and (B) the NEW LOS orientation-merge (the mod-4 switch bit merges (1,3)/(3,1), so the odd C(k)=-C(-k) secondary bias is invisible to h — claim los-secondary-bias-orientation-invisible-to-fold). |
| `verify_intersection_formula.py` | _(undescribed)_ |
