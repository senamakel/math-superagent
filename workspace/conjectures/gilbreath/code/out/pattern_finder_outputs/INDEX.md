# Index — code/out/pattern_finder_outputs

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `b.txt` | Block length b_k (leading {0,2} count), k=1..1000; tail k>=162 is the finite-width artifact b = W−k−1. Canonical copy (was duplicated in code/pattern_finder/). |
| `b_genuine.txt` | Same b-series, k=1..161 only (real dynamics). Canonical copy. |
| `b_genuine2.txt` | Identical copy of b_genuine.txt (diff-clean). |
| `bits.txt` | s/2 = A_k(1)/2 ∈ {0,1}, k=1..1000. |
| `c.txt` | Intruder c_k = first value past the block, k=1..161; identical to intruder.txt. |
| `diffs.txt` | b_{k+1} − b_k for k=1..160 (genuine transitions). |
| `e_bits.txt` | Halved block edge (e_k/2), k=1..161, from boundary_state.py. |
| `giants_6e8.json` | _(undescribed)_ |
| `i_bits.txt` | Halved next-to-edge entry (i_k/2), k=1..161, from boundary_state.py. |
| `intruder.txt` | First value past the block, k=1..161; None → empty line. |
| `jumps.txt` | Jump sizes b_{k+1} − b_k at regeneration rows (b_{k+1} ≥ b_k), k=1..161. |
| `minima_b.txt` | Values of b at strict local minima, genuine regime. |
| `minima_rows.txt` | Row indices k (1-based) of those strict local minima. |
| `regen_rows.txt` | Row indices k (1-based) with b_{k+1} ≥ b_k, k=1..161. |
| `s.txt` | Second entry A_k(1) ∈ {0,2}, k=1..1000. |
| `s_bits.txt` | Halved second entry s/2, from boundary_state.py. |
| `s_runs0.txt` | Run lengths of consecutive s=0 values (k=1..1000). |
| `s_runs2.txt` | Run lengths of consecutive s=2 values (k=1..1000). |
| `t_bits.txt` | Halved A_k(2)/2, k=1..161, from boundary_state.py. |
| `w_bits.txt` | Halved third-from-edge block entry (w_k/2), k=1..161, from boundary_state.py. |
| `wider_giants.json` | Giant-jump data at a wider sieve (from the wider_giants_*.py family): W, depth, kstar, giant rows, inter-giant gaps, landing blocks, giant jumps, pre-jump blocks, landing floorings, and gap/(j+1) ratios — the wider-sieve confirmation of the genuine-giants characterization. |
ate.py. |
| `w_bits.txt` | Halved third-from-edge block entry (w_k/2), k=1..161, from boundary_state.py. |
| `wider_giants.json` | _(undescribed)_ |
