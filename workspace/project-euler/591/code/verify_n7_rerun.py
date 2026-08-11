"""Independent re-run verification: solver at n=1e7 vs brute force at n=1e7.

Reads the freshly produced /workspace/results_brute_n7.txt (rows: d b a |a| err),
calls solution_bothsides.solve_d_both(d, 10**7) for the same 16 d, and compares
the (b, a) pairs exactly. Reports per-d PASS/FAIL.

The built-in comparison inside brute_n7.py compares against the n=1e13 solver
file (results_full_bothsides.txt) and is EXPECTED to mismatch, since the optimal
(a,b) changes with n. This script performs the correct apples-to-apples check:
solver and brute at the SAME n=10^7.
"""
import sys
sys.path.insert(0, '/workspace')
from solution_bothsides import solve_d_both

DS = [2, 13, 14, 15, 18, 19, 21, 22, 27, 29, 41, 42, 52, 59, 80, 98]
N = 10**7

def load_brute(path='/workspace/results_brute_n7.txt'):
    res = {}
    for line in open(path):
        p = line.split()
        if not p:
            continue
        res[int(p[0])] = (int(p[1]), int(p[2]))  # d -> (b, a)
    return res

def main():
    brute = load_brute()
    ok = True
    print(f"{'d':>3} {'brute_b':>13} {'solver_b':>13} {'brute_a':>13} {'solver_a':>13}  VERDICT")
    for d in DS:
        b_s, a_s, absa_s = solve_d_both(d, N)
        b_b, a_b = brute[d]
        match = (b_s == b_b) and (a_s == a_b)
        ok = ok and match
        print(f"{d:3d} {b_b:13d} {b_s:13d} {a_b:13d} {a_s:13d}  "
              f"{'PASS' if match else 'FAIL'}")
    print(f"\nALL 16 d: {'PASS' if ok else 'FAIL'}")

if __name__ == '__main__':
    main()
