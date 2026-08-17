# Index — code/lean

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `extremal_split_stability_G_cupcap.lean` | Decomposition of node extremal-split-stability/G-cupcap (the ES 1935 cup-cap characterization of convex position). Proves the (⇐) direction (cupcap_gives_convex) for real — kernel-checked, axioms only propext/Classical.choice/Quot.sound — via the arithmetic spine union_card_shared_two ( |
| `extremal_split_stability_G_split_consistent.lean` | Decomposition of node extremal-split-stability/G-split-consistent: ES 1960 es_construct template admits a line splitting it into two (n-1)-avoiding halves of 2^{n-3} (split counts 4/2/0 at n=5/6/7). Kernel-checked spine: esConstructSize_eq (block sum of C(n-2,i) = 2^{n-2}, via Nat.sum_range_choose), split_total_from_halves (two 2^{n-3} halves give total 2^{n-2}), and combining_consistency (if a valid split exists then N=2^{n-2}, tying the split to the construction's size) — all no-sorry, only propext/Classical.choice/Quot.sound. Three declared sorry gaps: es_construct_n5_four_splits, es_construct_n6_two_splits, es_construct_n7_no_split — the concrete 4/2/0 split-count computations over the verified es_construct coordinates (already exact in Python, code/out/gsplit_phase2.captured.txt), each with a next move. The n=7 zero is the refusal that refutes the G-split lemma on this template. |
| `g_cupcap_verified.lean` | Lean decomposition of node g-cupcap-verified (ES 1935 cup/cap characterization of convex position). Replaces the old Cited axiom with a declared sorry leaf convex_gives_geometry (the ES 1935 upper/lower boundary-chain decomposition). Proved for real on the kernel: union_card_shared_two ( |
| `gsplit_enum_completeness_and_n7_zero.lean` | Decomposition of node gsplit-enum-completeness-and-n7-zero: P1 (an N-point general-position set has exactly N(N-1) open-halfplane sides, realized by the rotating directed-line construction) and P2 (es_construct split counts 4/2/0 at n=5,6,7). Kernel-checked: parabola count at N=3,4 (by decide, no axioms), the combining spine p1_combining, and the cyclic-interval arithmetic core. 7 declared sorry gaps: allSides_card_parabola, sides_of_parabola_are_cyclic_intervals, cyclic_intervals_card_eq_N_mul, rotating_line_realises_all_sides, and the three es_construct split count theorems. Each gap is a fenced gap block with id/lemma/status/next. |
| `probe_n5.lean` | _(undescribed)_ |
| `probe_n5b.lean` | _(undescribed)_ |
| `probe_n5c.lean` | _(undescribed)_ |
| `probe_n5d.lean` | _(undescribed)_ |
| `probe_n5e.lean` | _(undescribed)_ |
| `probe_n5f.lean` | _(undescribed)_ |
| `probe_n5g.lean` | _(undescribed)_ |
| `probe_n5h.lean` | _(undescribed)_ |
| `probe_n6.lean` | _(undescribed)_ |
