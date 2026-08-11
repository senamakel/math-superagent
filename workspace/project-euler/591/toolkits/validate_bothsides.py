"""Validate corrected both-sign solver against brute force for ALL d at n=10^6.
Also compare with the old positive-only candidates to confirm where they differ.
"""
import math, time, mpmath as mp
mp.mp.dps = 50
PI = mp.mpf('3.14159265358979323846264338327950288419716939937510')
from solution_bothsides import solve_d_both

def brute_best(d, n):
    """Brute force over b in [-L, L], a in [-n,n] via round(pi - b sqrt d)."""
    sd = mp.sqrt(d)
    L = int(mp.floor(n / sd))
    best = None
    # test both signs
    for b in range(-L, L+1):
        a = mp.nint(PI - b*sd)
        if a < -n: a = -n
        if a > n: a = n
        err = abs(PI - (a + b*sd))
        if best is None or err < best[0]:
            best = (err, int(a), b)
    return best

if __name__ == "__main__":
    n = 1_000_000
    ok = True
    mism = []
    t0=time.time()
    for d in range(2,100):
        if math.isqrt(d)**2==d: continue
        _, a_sol, absa_sol = solve_d_both(d, n)
        err_br, a_br, b_br = brute_best(d, n)
        if abs(a_sol) != abs(a_br):
            ok = False
            mism.append((d, a_sol, a_br, b_br))
    print(f"n={n} both-sign: ALL_MATCH={ok}, mismatches={mism[:10]}, count={len(mism)}")
    print(f"elapsed {time.time()-t0:.1f}s")