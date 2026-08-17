# OEIS lookup: the distance-2 and replication family sequences are not catalogued

Two further family sequences of the srg(v,k,1,2) catalogue were looked up in
OEIS (pattern-finder round 29, over the five feasible members
u ∈ {1,3,4,10,31}, k = u²+u+2) and returned **no match**:

- distance-2 vertex counts (k(k−2)/2): `[4, 84, 220, 6160, 493024]`
  (k = 4, 14, 22, 112, 994).
- outer-design replication (k−4)/2: `[0, 5, 9, 54, 495]`.

Both are closed-form quartics/linear-in-k values over the a = 2u+1 | 63 index
set, already catalogued in `code/out/derived_design_sequences.py` (captured as
`derived_design_sequences.captured.txt`, described in `code/out/INDEX.md`).
No OEIS match means no external closed form will surface; the closed forms are
the family's own. Recorded so nobody looks these two up again.

Distinct from the three misses already recorded:
- `oeis-miss-family-vertex-counts.md` (v ∈ {9, 99, 243, 6273, 494019}),
- `oeis-miss-n3cap-and-triangle-counts.md` ([0, 4158, 26730, 19320840,
  121781611728] and [6, 231, 891, 117096, 81842481]),
- `oeis-miss-paley-pattern-config-counts.md` ([1, 21, 55, 1540, 123256]).

Also confirmed this round: the pentagon sequence
[0, 33264, 384912, 1669320576, 96451036488576] and the outer-block counts
[0, 140, 660, 110880, 81348960] are the same closed-form class — analysed and
found (as expected) to fit no low-order constant-coefficient recurrence or
low-degree polynomial over the 5 evaluated points, because they are
higher-degree polynomials in u (degree 8 and 6 respectively) sampled at five
index points. Nothing here separates 99 from its controls 9 and 243; every
value is determined by the parameters alone.

Per the operator's closing directive this is the last family-sequence
computation: eleven routes are closed, solution.md is consolidated, and the
remaining 99-specific lever is the global n₃≥1 closure (structural, not
sequence-tool).