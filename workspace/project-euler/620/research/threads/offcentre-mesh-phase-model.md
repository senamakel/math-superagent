```thread
question: >
  Which crossings of f(d)=Q_p−Q_q on (DL,DU) correspond to physically
  distinct, admissible gear arrangements, and which are spurious — so that
  g(c,s,p,q) correctly counts the PE620 arrangements?
status: open — but the on-disk 213-vs-205 discrepancy is now diagnosed as an
  artifact of the grid-scan, not (yet) a model defect; main blocker moved to
  running scholar_verify.py and computing a verified G(500)
rests-on:
  - tangency_enum_oracle_match
  - g20_overcount_by_eight
  - n_t_model_oracle_summary (added this review)
blocked-by:
  - scholar has no execution tool; the fresh verification script
    code/pattern/scholar_verify.py is written but not run
next:
  - Run code/pattern/scholar_verify.py; record output beside
    research/notes/n-t-model-on-disk-state.md
  - Retire the count_formula_test2.txt (2^17/1e-4) and levels.txt all-zero
    rows as grid/evaluator artifacts, or find the real defect if the run shows
    scan 6 at higher grids too
  - Verify G(500) by two independent routes (code/solution.py comment says
    1470337306; independent_verify.py Route B claims it; neither has an output
    file on disk)
  - Prove identity n_p+n_q = c+s and monotonicity of n_p (approach first-step 1)
  - Exact endpoint floors (approach first-step 2-3)
```

# Off-centre mesh phase model — admissibility fix, now with artifact audit

Current state after this review's audit of `code/out/`:

**Two families of "the same" model-file agree** — `n_integer_model.txt`,
`closedform_probe.txt`, `count_formula_test.txt`, `mpmath_table.txt`, `seq_G.txt`,
`G_sequence.txt` all give g(16,5,5,6)=9, G(16)=9, G(20)=205, and
`count_formula_test.txt` reports **0 mismatches across 372 tuples (s+p+q≤30)**,
G(30)=4538, using the n_t formula `[(c−t)β+(s+t)μ]/π`.

**Two files in the same folder disagree** — `count_formula_test2.txt` reports 6
for the g(16,5,5,6) scan (2^17 grid, tol 1e-4, p-only) with 2369 mismatches vs
formula over 2600 tuples, and `levels.txt` reports all-zero g rows (kmin..kmax =
1..0, nlo=nhi=0) for the SAME tuples that closedform_probe gives 9–12.

The earlier diagnosis (`g20_overcount_by_eight`, fast_g.py's mpmath
monotone-crossing form → G(20)=213) is one MORE value for the same tuple
family. So the on-disk record literally contains 9, 6, 0 and 213 for nearby
computations of the same model; only the 9-family matches the oracle.
`levels.txt`'s pattern (every row kmin=1, kmax=0, nlo=nhi=0.00000) is a
diagnostic bug (endpoint evaluator returning 0, likely because the code ran on
a tuple subset where the model's d-interval was mis-built), and
`count_formula_test2.py`'s scan is a p-only condition at low grid — both are
candidate artifacts, but that is a hypothesis until scholar_verify.py runs and
shows the scan value converging to 9 as the grid refines.

The claim `g20_overcount_by_eight` should therefore not be treated as the
settled truth about the n_t model until the 9-family, the 213 (fast_g.py), and
the 6 (count_formula_test2) are reconciled by one executable on one machine. If
fast_g.py is genuinely using a different admissibility/convention, its 213 may
be the spurious one; the thread should not "fix admissibility" to get from 213
to 205 until the 9-family's 205 is reproduced by the same code path.

## Current concrete state

- The residue form / sign convention is settled by the oracle (only
  (σ,η,θ)=(−1,−1,−1) gives 9 in tangency_enum.py; the n_t formula is that same
  signed-sum family).
- `fast_g.py` gives 213 for G(20) (claim `g20_overcount_by_eight`), the
  formula family gives 205; the grid scan at small grids gives less (6).
- No bound-independent G(500) output file exists on disk: `code/solution.py`
  and `independent_verify.py` mention 1470337306 only in comments/docstrings;
  no `code/out/G500*.txt` exists.

## What is NOT wrong (per the earlier note, still standing)

- The sign convention (all eight variants tested; only (−1,−1,−1) gives 9).
- n_p monotonicity on (d_min, d_max) — checked per case in fast_g.py and
  implicitly by count_formula_test's 0 mismatches.
- The DL/DU bounds and the residue formula.
- The identity n_p + n_q = c+s (mpmath-60, incl. at non-valid d).

## What the literature says about the off-centre congruence (still load-bearing)

Kurasov 2020 (gear eccentric systems, full text on disk): off-centre assembly
is NOT the coaxial (Z1+Z3)/k = C; it is a per-satellite-pair signed sum of
(central-angle × tooth-count) = integer × π, plus a separate diameter/location
closure — the W/n_t family at source level. Zhao–Li 2018 (duplex idler,
internal-mesh sign −) and Segade-Robleda 2012 (four-gear pitch-difference)
corroborate the signed-sum structure. Coaxial baseline (Guo 5.21, design
guides) is the d→0 limit. Sign caveat: Kurasov eq. (7) is OCR-garbled; signs
are pinned by the oracle rather than by the PDF.