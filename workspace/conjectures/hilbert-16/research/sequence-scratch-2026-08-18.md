# Sequence scratch (2026-08-18)

Exact rerun of `sequence_extract_rerun.py` and `sequence_deeper_audit.py` produced `a=[4,30,97,236,485,890,1505]` for d=4..16 and complement `c=[7,10,16,23,31,40,50]` with h=d-2. The conjectured c=(h^2+14h+8)/8 holds exactly for h=4,6,...,14, but fails at h=2 (actual 7 vs predicted 5); h=2 is outside the originally observed range. No constant-coefficient recurrence order <=4 fits either 7-term sequence. Exact next extrapolation predicts at h=16/d=18: c=61 and a=2392, but this is not computed and would be the first postulated falsifier. Treat as conjecture only.

`note_scratch` was unavailable because the memory service timed out.
