#!/usr/bin/env python3
"""Exact final-boundary verification for the closed route orbit-matrix-g99-detached.

The m=33 fixed-point-free order-3 orbit-matrix CP-SAT encoder on srg(99,14,1,2)
(presolving/fixing phase) made exactly two logged progress heartbeats before
the run's natural 3000s termination. This program, in exact rational arithmetic
(Fraction, no floats for the integer arithmetic), extrapolates the presolve
fixing rate to the full 41,745-variable space and states honestly what the run
did and did not establish.

Data source: code/out/orbit_z3_enc_g99_plain_detached.captured.txt
Heartbeat points (var counts are "unfixed remaining" out of 41745):
    t1 =  694.32 s  -> var 41730/41745  => 15 variables fixed so far
    t2 = 1889.85 s  -> var 41712/41745  => 33 variables fixed so far

Program computes:
  1. Delta_vars = 33 - 15 = 18 vars over Delta_t = 1889.85 - 694.32 = 1195.53 s;
     seconds-per-variable from those two points; extrapolation to all 41,745
     variables; expressed in days. Checks against the boundary note's stated
     'one per ~66 s, ~32 days for presolve'.
  2. The rate FROM THE START (15 vars in 694.32 s alone) and the rate from the
     two points together, and explains why extrapolation to full presolve is a
     LOWER bound on total wall-clock (fixing slows as presolve progresses, and
     the INFEASIBLE search space the solver would have to exhaust after
     presolve is far larger than the fixed variables).
  3. Honest verdict: no INFEASIBLE reached => no order-3 automorphism excluded;
     the Z3 case remains open.

Every intermediate value is printed; seconds use Fraction; the integer parts are
exact. The only decimal shown is a clearly-labelled 2-decimal ESTIMATE.
"""

from fractions import Fraction

# --- Input heartbeat points (exact, from the rejected/progress capture) ---
TOTAL_VARS = 41745
CONSTRAINTS = 57165

# point 1
t1_s = Fraction(69432, 100)        # 694.32 s exactly
var1   = 41730
# point 2
t2_s  = Fraction(188985, 100)      # 1889.85 s exactly
var2   = 41712

# "variables fixed" = how far the unfixed counter has dropped below the total
fixed1 = TOTAL_VARS - var1          # 15
fixed2 = TOTAL_VARS - var2          # 33

def secs(frac):
    """2-decimal float ESTIMATE of a Fraction number of seconds."""
    return round(float(frac), 2)

def days_frac(sec_frac):
    """Convert seconds (Fraction) into days (Fraction), 86400 s/day."""
    return sec_frac / Fraction(86400)

def days_est(sec_frac):
    return round(float(days_frac(sec_frac)), 2)

print("=" * 78)
print("ORBIT-MATRIX-g99-DETACHED  --  EXACT FINAL-BOUNDARY PRESOLVE VERIFICATION")
print("=" * 78)
print(f"Total variables         : {TOTAL_VARS}")
print(f"Total constraints       : {CONSTRAINTS}")
print()

print("HEARTBEAT POINTS (from orbit_z3_enc_g99_plain_detached.captured.txt)")
print(f"  point 1: t = {t1_s} s = {secs(t1_s)} s   var {var1}/{TOTAL_VARS}  => {fixed1} vars fixed")
print(f"  point 2: t = {t2_s} s = {secs(t2_s)} s   var {var2}/{TOTAL_VARS}  => {fixed2} vars fixed")
print()

# --- 1. Two-point rate and extrapolation --------------------------------
print("STEP 1 -- TWO-POINT RATE AND EXTRAPOLATION TO ALL %d VARIABLES" % TOTAL_VARS)
print("-" * 78)
Delta_vars = fixed2 - fixed1
Delta_t    = t2_s - t1_s
print(f"  Delta_vars = fixed2 - fixed1 = {fixed2} - {fixed1} = {Delta_vars} variables")
print(f"  Delta_t    = t2 - t1 = {t2_s} - {t1_s} = {Delta_t} s "
      f"(estimate {secs(Delta_t)} s)")

secs_per_var = Delta_t / Delta_vars
print(f"  seconds per variable (two-point) = Delta_t / Delta_vars")
print(f"        = {Delta_t} / {Delta_vars} = {secs_per_var} s  "
      f"(estimate {secs(secs_per_var)} s)")
print(f"  Stated boundary note: 'one per ~66 s'")

extrap_total_s = secs_per_var * TOTAL_VARS
print(f"  extrapolated presolve wall = secs_per_var * {TOTAL_VARS}")
print(f"        = {secs_per_var} * {TOTAL_VARS} = {extrap_total_s} s")
extrap_days = days_frac(extrap_total_s)
print(f"        in days = {extrap_total_s} s / 86400 = {extrap_days} days "
      f"(estimate {days_est(extrap_total_s)} days)")
print(f"  Stated boundary note: '~32 days for presolve'")
print()

# --- 2. Rate from the start vs two-point -------------------------------
print("STEP 2 -- RATE FROM THE START vs TWO-POINT RATE")
print("-" * 78)
spv_start = t1_s / fixed1
print(f"  rate from start: {fixed1} vars in {t1_s} s")
print(f"        seconds per variable = {t1_s} / {fixed1} = {spv_start} s "
      f"(estimate {secs(spv_start)} s)")
overall_spv = t2_s / fixed2
print(f"  rate over both points: {fixed2} vars in {t2_s} s")
print(f"        seconds per variable = {t2_s} / {fixed2} = {overall_spv} s "
      f"(estimate {secs(overall_spv)} s)")

# Minimal completion time if the cluster of points so far held forever
min_complete_s = secs_per_var * TOTAL_VARS   # same as extrapolation above
print()
print("  WHY the extrapolation is a LOWER BOUND on total wall-clock:")
print("   (a) fixing SLOWS as presolve progresses: early fixes are cheap")
print("       (Probe/MaxClique/PresolveToFixPoint), later ones need the full")
print("       propagation lag; the 18-var two-point slope (%.2f s/var)" % secs(secs_per_var))
print("       is already slower than the start-to-15 rate (%.2f s/var)."
      % secs(spv_start))
print("   (b) presolve fixing is the ONLY progress; after presolve finishes,")
print("       the search proper (branch-and-bound over the INFEASIBLE space)")
print("       has to exhaust a space far larger than the %d fixed variables,"
      % TOTAL_VARS)
print("       by many orders of magnitude.")
print()

# --- 3. Honest verdict --------------------------------------------------
print("STEP 3 -- HONEST VERDICT")
print("-" * 78)
print("  Boundary reached: UNKNOWN/TIMEOUT at 3000.4s wall; last #Model bound")
print("  2974.64s, var 41675/41745, constraints 56987/57165; 0 gap_integral,")
print("  5039266 conflicts, 8049382 branches (no feasible point found).")
print()
print("  No INFEASIBLE was reached within the 3000s budget.")
print("  => NO order-3 fixed-point-free automorphism is EXCLUDED by this run.")
print("  The run is INCONCLUSIVE / TIMEOUT and proves nothing either way.")
print("  The Z3 (order-3) case REMAINS OPEN.")
print()
print("=" * 78)
print("Summary of exact values")
print("=" * 78)
print(f"  Delta_vars                      = {Delta_vars}")
print(f"  Delta_t                         = {Delta_t} s")
print(f"  seconds per variable (2-point)  = {secs_per_var} s  (est {secs(secs_per_var)})")
print(f"  extrapolated presolve           = {extrap_total_s} s  (est {secs(extrap_total_s)})")
print(f"                                  = {extrap_days} days (est {days_est(extrap_total_s)})")
print(f"  start-to-15 s/v                 = {spv_start} s  (est {secs(spv_start)})")
print(f"  overall-to-33 s/v               = {overall_spv} s  (est {secs(overall_spv)})")
print()
print("VERDICT: no INFEASIBLE reached => no order-3 automorphism excluded;")
print("         the Z3 case remains open.")
