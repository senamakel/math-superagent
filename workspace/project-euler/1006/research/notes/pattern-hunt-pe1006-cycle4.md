# PE1006 pattern-hunt, cycle 4 — OEIS catalogue of the structural handles

This cycle's contribution: run the sequence tools and OEIS lookups on the
structural sequences the run had already extracted, and independently
re-verify the load-bearing regularities with fresh brute enumeration.
All statements below are conjectures (computationally verified exactly over
the stated ranges), except the right-extension recurrence which has a direct
proof from the definition.

## Confirmed this cycle (fresh brute enumeration, exact)

Ran `code/pattern_hunt/pattern_verify_runs.py`, `pattern_verify_full.py`,
`check_c1_weight.py`, `check_run_density.py`, `extract_vr_runs.py`.

1. **Right-extension recurrence** (verified again independently):
   every length-k factor set has exactly ONE right-special factor R_k (both
   '0' and '1' extend), and
       Psi(k+1) = 100·Psi(k) + 100·V(R_k)^2 + 20·S1(k) + J(k)
   holds EXACTLY k=1..24 (vs psi_exact.txt), and mod M = 101001001 for
   k=1..199 (fresh brute S1/J), and exact k=1..149 + mod M k=1..400 in
   cycle 3.  J(k) = #{factors with '1' extension} = c1(k+1).
   This is the one load-bearing regularity with a direct proof.

2. **c1(k) = # lead-`1` length-k factors = 1 + floor(k/φ²)** — verified
   fresh k=1..100.  OEIS **A189663** (partial sums of A189661).

3. **Weight distribution** of the k+1 factors is exactly
   {floor(k/φ²), ceil(k/φ²)} (Sturmian balance) — verified fresh k=1..100.

4. **V(R_k) is constant exactly on runs starting at the upper Wythoff
   numbers s_j = floor(j·φ²) = A001950**, verified to j=1146 (k=3000), run
   lengths in {1,2,3}, and R_k = `'0'*(k−s_j) + R_{s_j}` (zero-padding)
   within a run.  NEW this cycle: the run-START GAPS form a Sturmian word in
   {2,3} whose sequence is exactly OEIS **A076662** (the (2,3) Fibonacci
   string) = **A282162** = A001468-difference word.  Density of gap-3 ≈ 1/φ,
   gap-2 ≈ 1/φ² (measured 0.6144/0.3791 at k=400, consistent).

5. **Lmin(k) = k + NextFib(k) − 1** (OEIS **A344953**), verified to
   k = 6764 by three independent programs.

## OEIS catalogue (recorded, so nobody re-searches)

- exact Psi(1..6) — NOT in OEIS (no catalogued closed form).
- residue Psi(k) mod M — no constant-coefficient linear recurrence (order
  ≤ 12), noise-flat; NOT in OEIS.
- V(R_k) run-start gaps — **A076662** / **A282162** (Fibonacci/Wythoff word).
- V(R_k) run START positions s_j — **A001950** (upper Wythoff), i.e.
  s_j = floor(j·φ²).
- c1(k) = 1+floor(k/φ²) — **A189663**.
- Lmin(k) = k+NextFib(k)−1 — **A344953**.
- ndef(k) (Toeplitz-defect count) — NOT in OEIS (miss recorded earlier).

## What the regularities reduce the work to

Every scalar regularity dies mod M (no linear recurrence survives), so no
closed form of Psi(k) mod M exists at polynomial-in-k coefficients.  The O(log)
method must therefore evaluate, using the Sturmian mechanical construction:
- the lead-split by weight / lead letter (dimension 2, from c1),
- the right-special factor V(R_k) and its run structure (A001950 positions),
- the geometrically weighted floor-sum second moment (S2) via the universal
  Euclidean monoid (code/lib/ueuclid.py), which is the committed route.
The Wythoff run structure of V(R_k) (constant on floor(j·φ²) blocks) is the
handle that lets S1(k) and V(R_k) be evaluated in O(log) blocks rather than
one step per k — exactly the "87 Fibonacci blocks at 10^18" of the
operator's position/column-dedup directive.

## Files

- code/pattern_hunt/pattern_verify_runs.py  — Part1 recurrence k=1..24,
  Part2 run structure k=1..150 (brute).
- code/pattern_hunt/pattern_verify_full.py  — recurrence mod M k=1..199,
  c1=1+floor, run lengths (brute).
- code/pattern_hunt/check_c1_weight.py      — c1, weight-dist, c0 k=1..100.
- code/pattern_hunt/check_run_density.py    — gap densities vs 1/φ, 1/φ².
- code/pattern_hunt/extract_vr_runs.py      — V(R_k) run starts/gaps/values,
  writes code/out/vr_runvals.txt, vr_rungaps.txt.
- code/out/r_runs_wythoff.txt               — cycle-3 exact verification to
  k=3000 (run starts = A001950, zero-padding, J, Psi recurrence).
