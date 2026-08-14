import os

# Recompute solutions from the result files and check structure
base = "/workspace/code/out"
per_digit_sums = {1:22786974071,2:73737982962,3:372647999625,4:741999999540,
                  5:100000000000,6:2434703999430,7:1876917059570,
                  8:15312327487352,9:360000000000}
grand_total = 21295121502550

all_sols = {}
for d in range(1,10):
    sols = [int(x) for x in open(f"{base}/solutions-d{d}.txt").read().split()
            if x.strip().isdigit() or (x.strip().lstrip('-').isdigit())]
    all_sols[d] = sols
    # verify sorted
    assert sols == sorted(sols), f"d={d} not sorted"

# 1) Does the run's file sum equal the per-digit sum s(d)?
print("=== 1) file sum vs per-digit s(d) ===")
for d in range(1,10):
    s = sum(all_sols[d])
    ok = s == per_digit_sums[d]
    print(f"d={d}: n_sol={len(all_sols[d])} sum={s} match_s(d)={ok}")
print("sum of all file sums =", sum(sum(all_sols[d]) for d in range(1,10)),
      " grand_total =", grand_total)

# 2) universal 10^10 solution? and k*10^10 membership per digit
print("\n=== 2) k*10^10 in solutions, k=0..8 ===")
for d in range(1,10):
    S = set(all_sols[d])
    present = [k for k in range(9) if k*10**10 in S]
    print(f"d={d}: k*10^10 present for k in {present}")

# 3) Is 10^10 a solution for EVERY d? (from data)
print("\n10^10 in every d's solutions:", all(10**10 in set(all_sols[d]) for d in range(1,10)))

# 4) d=5 and d=9 exactly k*10^10?
print("d=5 == [k*10^10 k=0..4]:",
      all_sols[5] == [k*10**10 for k in range(5)])
print("d=9 == [k*10^10 k=0..8]:",
      all_sols[9] == [k*10**10 for k in range(9)])
