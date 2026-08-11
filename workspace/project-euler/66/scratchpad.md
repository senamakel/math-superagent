# Scratchpad

Use this file for temporary calculations, partial derivations, and observations
that are not yet established well enough for `memory.md`.

## Phase 2 — hand traces (validation only, not proofs; no web verification available in this run)

### CF digits and periods (iteration of memory.md §2.4)

- D=2: (m,d,a) steps: (1,1,2) → L=1. CF [1; 2̄]. Convergents: p0/q0=1/1 (norm −1), p1/q1=3/2 (norm +1).
- D=3: (1,2,1), (1,1,2) → L=2. CF [1; 1̄,2]. p1/q1=2/1 (norm +1).
- D=5: (2,1,4) → L=1. CF [2; 4̄]. p1/q1=9/4 (norm +1).
- D=7: (2,3,1), (1,2,1), (1,3,1), (2,1,4) → L=4. CF [2; 1,1,1,4̄]. p: 2,3,5,8; q: 1,1,2,3; p3/q3=8/3 (norm 64−63=+1).
- D=13: (3,4,1), (1,3,1), (2,3,1), (1,4,1), (3,1,6) → L=5. CF [3; 1,1,1,1,6̄]. p: 3,4,7,11,18,119,137,256,393,649; q: 1,1,2,3,5,33,38,71,109,180. p4/q4=18/5 (norm −1); p9/q9=649/180 (norm +1) — matches oracle.
- D=7 identity check p_n² − D q_n² = (−1)^{n+1} d_{n+1}: n=0: 4−7=−3 = −d1=−3 ✓; n=1: 9−7=+2 = +d2 ✓; n=2: 25−28=−3 = −d3 ✓; n=3: 64−63=+1 = +d4 ✓. Also p_n q_{n−1} − p_{n−1} q_n = (−1)^{n−1} ✓.
- Degenerate-collapse observation (U1): D=7 with signed minimizer m=−2 at start would give (a',b',k')=(1,0,1) (trivial); nonneg minimizer m=1 gives the good chain below. Same phenomenon at D=67 (m=−8 vs classical m=7).

### Chakravala traces (rule: m ≥ 0, k | (a+bm), minimize |m²−D|; updates with |k|; final square if k=−1)

- D=2: (1,1,−1), m=1 → (3,2,1) ✓ oracle.
- D=3: (1,1,−2), m=1 → (2,1,1) ✓ oracle.
- D=5: (2,1,−1), m=2 → (9,4,1) ✓ oracle.
- D=6: (2,1,−2), m=2 → (5,2,1) ✓ oracle.
- D=7: (2,1,−3), m=1 → (3,1,2); (3,1,2), m=3 → (8,3,1) ✓ oracle.
- D=13: (3,1,−4), m=1 → (4,1,3); (4,1,3), m=2 → (7,2,−3); (7,2,−3), m=4 → (18,5,−1); k=−1 → square: (324+325, 2·18·5) = (649,180) ✓ oracle.
- D=67 (consistency check vs classical): (8,1,−3) m=7 → (41,5,6) → (90,11,−7) → (221,27,−2) → (1899,232,−7) → (3577,437,6) → (9053,1106,−3) → (48842,5967,1). Check 48842² − 67·5967² = 1 (hand multiplication; matches the classical published example).
