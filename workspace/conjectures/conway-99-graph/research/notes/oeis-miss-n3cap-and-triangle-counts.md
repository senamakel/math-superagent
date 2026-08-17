# OEIS lookup: the n3-cap and triangle-count catalogue sequences are not catalogued

Two catalogue sequences of the srg(v,k,1,2) family were looked up in OEIS
(round 26 pattern-finder) and returned **no match**:

- n3 capacity (tightest nonnegative cap on n3 over the 62 Reimbayev order-6
  formulas), over the five feasible members:
  `[0, 4158, 26730, 19320840, 121781611728]`.
- triangle counts (number of 3-cliques), over the five feasible members:
  `[6, 231, 891, 117096, 81842481]`.

Both are the u-quartics over the a = 2u+1 | 63 index set
(u ∈ {1,3,4,10,31}) already closed in the run's catalogue. No OEIS match means
no external closed form will surface; the closed forms are the run's own
(see `code/out/n3_cap_closed_form.captured.txt` and the family-count
catalogue). This is distinct from the already-recorded vertex-count miss
(`oeis-miss-family-vertex-counts.md`, `[9,99,243,6273,494019]`).

Recorded so nobody looks these two sequences up again.
