# Confirm (A*di) % M == (-dv) mod M in each run, and test whether the
# consecutive run-value steps form a Euclidean descent related to A and M.
A = 1504170715041707
M = 4503599627370517
from math import gcd

# run boundaries from earlier analysis: (first_coin_value, last_coin_value, n_diff, run_value_step)
runs_val = [
    # (start_val, end_val, index_step, value_step_pos)
]
# from run output, using consecutive-run value differences at boundaries:
# coin16=15806432 ... we list runs as (coin#lo, coin#hi, idx_step, pos val step)
R = [
    (16,54, 283827021, 409165),
    (54,55, 11111552452, 151003),
    (55,57, 33050830335, 43844),
    (57,60, 209132707441, 4902),
    (60,94, 924571768317, 137),
    (94,97, 33075450951971, 30),
    (97,98, 164452682991538, 13),
    (98,102, 1051942428084853, 1),
]
for (lo,hi,di,dv) in R:
    lhs = (A*di) % M
    rhs = (M - dv) % M
    print(f"run {lo:3d}..{hi:3d}: (A*di)%M={lhs}  == (M-dv)%M ? {lhs==rhs}  dv={dv}")

# Euclidean descent of A and M: remainders
def euclid(x,y):
    steps=[]
    while y:
        q = x//y
        steps.append((x,y,q,x%y))
        x,y = y,x%y
    return steps
print("\nEuclidean steps (a,b,q,r0):")
for s in euclid(max(A,M), min(A,M)):
    print("  ", s)

# Reduced pair A/M in lowest terms
g = gcd(A,M)
print("\ngcd(A,M)=",g)
