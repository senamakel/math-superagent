# Index — code/boundary_edge

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `boundary_edge_analysis.py` | Live-regime (k=1..161) boundary-edge analysis. Method: regenerates real prime Gilbreath rows 1..162 with numpy int64 (sieve 2e7, 1,270,607 primes; two passes of 162 abs-diff steps each), then (b) identifies erosion runs from the established regeneration criterion, (c) compares the Rule-90/Pascal-mod-2 boundary-edge prediction XOR_{j<=d, C(d,j) odd} h[b_K-d+j] against real rows at every depth of every run (edge + whole interior slice), (d) reports stall statistics. Correctness: reproduces A1=[1,2,2,4,2,4,2,4,6,2], A2=[1,0,2,2,2,2,2,2,4], A3=[1,2,0,0,0,0,0,2]; b/s/intruder k=1..162 equal code/out/blocks_depth1000.json; first-40 b/s equal code/out/witnesses.json; regen criterion 0 failures; run lengths equal depth-1000 live record [1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,4,4,4,5,7,8,12,12,13]. Formula validity was independently established in code/out/check_edge_zero_run.py (exhaustive over all 2^n bit strings, n<=18). O(162 x 1.27e6) per pass, ~100 MB peak; exits nonzero on any oracle failure. |
