#!/usr/bin/env python3
"""Final exact closure of the orbit-matrix programme's boundary (route 11).

One self-contained script, exact rational arithmetic only (Fraction), that
reproduces the reported boundary of the order-3 orbit-matrix CP-SAT run on the
putative srg(99,14,1,2) and states the honest verdict that closes route 11.

Data source
-----------
research/notes/orbit-order3-infeasibility-boundary.md and
code/out/orbit_z3_enc_g99_plain_detached.captured.txt.

The m=33 fixed-point-free order-3 orbit matrix was 41,745 variables /
57,165 constraints. The live heartbeat gave two progress points before the
run's 3000s termination:

    t1 = 694.32 s  -> var 41730/41745  => 15 variables fixed
    t2 = 1889.85 s -> var 41712/41745  => 33 variables fixed

This program does three exact steps:

  1. Two-point rate: 18 variables in 1195.53 s, seconds-per-variable =
     1195.53/18 s = 39851/600 s ~= 66.42 s, extrapolated to all 41,745
     variables and expressed in days (~32).
  2. Orbit-count comparison, from the group action alone (no graph data): a
     fixed-point-free order-3 automorphism on 99 points has 99/3 = 33
     point-orbits; an order-2 automorphism on 99 points with f fixed points
     has (99+f)/2 point-orbits, which is >= 50 for every odd f in {1,...,99}
     (order-2 on an odd point set forces f >= 1 and f odd). Enumerate f over
     the odd values 1..99 and print the orbit counts, all >= 50 > 33. Hence
     the order-2 orbit matrix has strictly more point-orbits than order-3's
     33, i.e. a strictly larger model: the directive's "strictly worse" claim.
  3. One-line honest verdict: the route is closed by computational
     infeasibility (measured ~1 var/66 s, ~32 days presolve for 41,745 vars),
     NOT by mathematics; no order-3 or order-2 automorphism exclusion is
     established; the Aut reduction to {Z2, Z3} and the openness of the
     automorphism group stand untouched.

No floats anywhere in the arithmetic; the only decimals shown are clearly
labelled 2-decimal ESTIMATES of exact Fractions.
"""

from fractions import Fraction

TOTAL_VARS = 41745
CONSTRAINTS = 57165
N = 99  # number of points in a putative srg(99,14,1,2)

# --- Heartbeat points, exact -------------------------------------------------
t1_s  = Fraction(69432, 100)          # 694.32 s exactly
var1  = 41730
t2_s  = Fraction(188985, 100)         # 1889.85 s exactly
var2  = 41712

fixed1 = TOTAL_VARS - var1            # 15
fixed2 = TOTAL_VARS - var2            # 33

def secs(frac):
    """2-decimal float ESTIMATE of a Fraction number of seconds."""
    return round(float(frac), 2)

def days_frac(sec_frac):
    return sec_frac / Fraction(86400)

print("=" * 78)
print("ROUTE 11  --  ORBIT-MATRIX PROGRAMME  --  FINAL BOUNDARY CLOSURE")
print("=" * 78)
print(f"Model size at m=33        : {TOTAL_VARS} variables, {CONSTRAINTS} constraints")
print()

# --- (1) heartbeat reproduction + exact two-point rate -----------------------
print("STEP 1 -- HEARTBEAT REPRODUCTION AND EXACT PRESOLVE RATE")
print("-" * 78)
print(f"Heartbeat point 1 : t = {t1_s} s (~{secs(t1_s)} s)  var {var1}/{TOTAL_VARS} "
      f"=> {fixed1} variables fixed")
print(f"Heartbeat point 2 : t = {t2_s} s (~{secs(t2_s)} s)  var {var2}/{TOTAL_VARS} "
      f"=> {fixed2} variables fixed")
print()

Delta_vars = fixed2 - fixed1
Delta_t    = t2_s - t1_s
secs_per_var = Delta_t / Delta_vars
extrap_total_s = secs_per_var * TOTAL_VARS
extrap_days = days_frac(extrap_total_s)

print(f"Delta_vars = {fixed2} - {fixed1} = {Delta_vars} variables")
print(f"Delta_t    = {t2_s} - {t1_s} = {Delta_t} s  (~{secs(Delta_t)} s)")
print(f"rate = Delta_t / Delta_vars = {Delta_t} / {Delta_vars}")
print(f"     = {secs_per_var} s per variable  (~{secs(secs_per_var)} s)")
print(f"  (boundary note: 'one per ~66 s')")
print()
print(f"presolve-only extrapolation to all {TOTAL_VARS} variables:")
print(f"  = {secs_per_var} * {TOTAL_VARS} = {extrap_total_s} s")
print(f"  in days = {extrap_total_s} / 86400 = {extrap_days} days  "
      f"(~{round(float(extrap_days), 2)} days)")
print(f"  (boundary note: '~32 days for presolve')")
print()

# --- (2) orbit-count comparison, pure group action, no graph data -----------
print("STEP 2 -- ORBIT-COUNT ARGUMENT: ORDER-2 MODEL STRICTLY WORSE")
print("-" * 78)
print(f"Points N = {N}.")
print("A fixed-point-free order-3 automorphism on N points:")
orbits3 = N // 3
print(f"  point-orbits = N/3 = {N}/{3} = {orbits3}")
print()
print("An order-2 automorphism on N points with f fixed points (f odd, f>=1):")
print(f"  point-orbits = (N+f)/2 = ({N}+f)/2, which is >= ({N}+1)/2 = {(N+1)//2}")
print("  for every f >= 1 (order-2 on an odd point set fixes >= 1 point, and")
print("  an involution fixes an odd number of points).")
print()

odd_f = [f for f in range(1, N + 1) if f % 2 == 1]
all_ge_50 = True
lines = []
for f in odd_f:
    oc = Fraction((N + f), 2)
    if oc < Fraction(50):
        all_ge_50 = False
    lines.append(f"  f = {f:3d}  ->  (N+f)/2 = {oc}")
print("Enumerating f over all odd values 1..99 (each line = orbit count):")
for line in lines:
    print(line)
print()
min_orbit2 = Fraction((N + 1), 2)
print(f"Minimum order-2 point-orbits (at f = 1) = (N+1)/2 = {min_orbit2} >= 50.")
print(f"All {len(odd_f)} odd values give orbit counts >= 50: {all_ge_50}.")
print(f"Every order-2 orbit count is >= 50 while order-3 has exactly {orbits3}.")
print(f"  {min_orbit2} > {orbits3}  => strictly more point-orbits for order-2.")
print("More point-orbits => a strictly larger orbit-matrix model => the")
print("order-2 case is strictly worse than the order-3 case that already")
print("fails to presolve at ~32 days. This is argued from the group action")
print("alone; no graph data is used.")
print()

# --- (3) one-line honest verdict ---------------------------------------------
print("STEP 3 -- ONE-LINE HONEST VERDICT")
print("-" * 78)
print("Route 11 is closed by computational infeasibility (measured ~1 var/66 s, "
      "~32 days of presolve for 41,745 variables), NOT by mathematics: no "
      "order-3 or order-2 automorphism exclusion is established, so the "
      "published Aut reduction to {Z2, Z3} and the openness of the "
      "automorphism group stand untouched.")
print()
print("=" * 78)
print("Summary of exact values")
print("=" * 78)
print(f"  Delta_vars                     = {Delta_vars}")
print(f"  Delta_t                        = {Delta_t} s  (~{secs(Delta_t)} s)")
print(f"  seconds per variable (2-point) = {secs_per_var} s  (~{secs(secs_per_var)} s)")
print(f"  extrapolated presolve wall     = {extrap_total_s} s")
print(f"                                  = {extrap_days} days  (~{round(float(extrap_days), 2)} days)")
print(f"  order-3 point-orbits           = {orbits3}")
print(f"  order-2 point-orbit range      = [{min_orbit2}, {Fraction((N + N),2)}]  (all >= 50)")
print()
print("VERDICT: closed by computational infeasibility, NOT by mathematics;")
print("         no order-3 or order-2 exclusion; Aut reduction and openness stand.")
