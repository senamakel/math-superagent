#!/usr/bin/env python3
"""Hand-check the run structure of M_d △ M_d' for small n, to pin the exact
'order' claim of the squared-excess approach.

Facts to confirm:
 (F1) |M_d △ M_d'| is even and >= 2 for d != d' (meet formula).
 (F2) #runs(M_d △ M_d') can be 1 (single even-length run -> order 2), and when
      it is 1 the run length is EVEN and >= 2 (never length 1, never separation 1).
 (F3) every distance-2 pair (|M_d △ M_d'| = 2) has #runs = 2 (two non-adjacent
      singletons) -> order 4. No distance-2 pair is a consecutive doubleton.
 (F4) single-run separations (= run length) are all EVEN; separation 1 never
      occurs as a single run.  Two-singleton pairs have separation 2^a (Type B)
      or 2^a - 2^b (Type A).
"""
import itertools


def submasks(x):
    s = x
    while True:
        yield s
        if s == 0:
            break
        s = (s - 1) & x


def M(n, d):
    return sorted({n - 1 - d + o for o in submasks(d) if 0 <= n - 1 - d + o <= n - 1})


def runs_of(S):
    runs = []
    for x in S:
        if runs and x == runs[-1][1] + 1:
            runs[-1][1] = x
        else:
            runs.append([x, x])
    return runs


def symdiff(a, b):
    return sorted(set(a) ^ set(b))


def pc(x):
    return bin(x).count("1")


def meet_dist(n, d, dp):
    return 2**pc(d) + 2**pc(dp) - 2**(pc(d & dp) + 1)


f1_ok = True
f2_ok = True
f3_ok = True
f4_ok = True
single_run_seps = set()
two_run_seps = set()
examples = {"single_run": None, "adjacent_pair": None}

for n in range(3, 40):
    rows = {d: M(n, d) for d in range(2, n)}
    for d, dp in itertools.combinations(range(2, n), 2):
        S = symdiff(rows[d], rows[dp])
        sz = len(S)
        R = runs_of(S)
        nr = len(R)
        # F1: even and >= 2
        if sz < 2 or sz % 2 != 0:
            f1_ok = False
            print("F1 FAIL", n, d, dp, S)
        # check meet formula
        if sz != meet_dist(n, d, dp):
            print("meet formula FAIL", n, d, dp, sz, meet_dist(n, d, dp))
        # F2/F4: single run -> even length >= 2
        if nr == 1:
            L = R[0][1] - R[0][0] + 1
            single_run_seps.add(L)
            if L < 2 or L % 2 != 0:
                f2_ok = False
                print("F2 FAIL", n, d, dp, R)
            if examples["single_run"] is None and L == 4:
                examples["single_run"] = (n, d, dp, R)
        # F3: distance-2 pairs
        if sz == 2:
            if nr != 2:
                f3_ok = False
                print("F3 FAIL (distance-2 not two runs)", n, d, dp, R)
            if R[1][0] - R[0][1] == 1:
                # two adjacent singletons = would be a consecutive doubleton
                f3_ok = False
                print("F3 FAIL (adjacent singletons)", n, d, dp, R)
            else:
                two_run_seps.add(R[1][0] - R[0][0])
        # separation-1 single run would be length 1 -> impossible by F2, but check
        if nr == 1 and R[0][1] == R[0][0]:
            f4_ok = False
        if nr == 2 and R[1][0] - R[0][0] == 1 and R[1][0] - R[0][1] != 1:
            pass

print("F1 (|symdiff| even, >=2):", f1_ok)
print("F2 (single run -> even length >=2):", f2_ok)
print("F3 (distance-2 pairs all two runs, non-adjacent):", f3_ok)
print("F4 (no separation-1 single run):", f4_ok)
print("single-run separations seen:", sorted(single_run_seps))
print("two-singleton (A2) separations seen:", sorted(two_run_seps))
print("example single run (n,d,d',runs):", examples["single_run"])

# Exhibit the load-bearing example: single run of length 4 -> order-2 at sep 4
n, d, dp, R = examples["single_run"]
S = symdiff(M(n, d), M(n, dp))
print(f"\nExhibit: n={n} d={d} d'={dp}  M_d△M_d' = {S}  runs = {R}")
print(f"  -> eps_{d} eps_{dp} = chi(r_{R[0][0]}) chi(r_{R[0][1]+1})  [order 2, separation {R[0][1]-R[0][0]+1}]")
