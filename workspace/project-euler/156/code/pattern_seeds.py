"""Extract block-0 seed sequences B_d for each digit and verify structural
claims exactly over the run's solution files.

Loads code/out/solutions-d*.txt (produced by code/solution.py and
cross-verified by code/verify.py).  For each d:

  1. B_d := solutions in [0, 10^10).  All exact from the files.
  2. Verify the block decomposition: the full solution set equals
     {k*10^10 + s : k=0..d-1, s in B_d} (the run's proven identity
     f_d(k*10^10+x) - f_d(x) = k*10^10, k <= d-1).
  3. NEW: verify the 5*10^8-scale translation for d in {1,2,3,4}:
     for every s in B_d with s in [5*10^8, 6*10^8), s - 5*10^8 is in B_d
     and has s' < 10^8; and no other B_d element lies in [5e8, 6e8).
     The supporting arithmetic fact f(5*10^8, d) = 5*10^8 is checked via
     lib.digits.f_place_value, plus a random-sample check of the
     translation identity f(5e8+x,d) - f(x,d) = 5e8 for x < 10^8.
  4. Run-length structure: maximal runs of consecutive integers inside B_d,
     printed as (start, length).  Within a run, every number past the first
     must contain exactly one copy of digit d (definition-level fact:
     g(n)=f(n,d)-n changes by c_d(n+1)-1 at step n+1).
"""
import sys, os, random, itertools
sys.path.insert(0, "/workspace/code")
from lib.digits import f_place_value

BASE = "/workspace/code/out"
sols = {}
for d in range(1, 10):
    sols[d] = [int(x) for x in open(f"{BASE}/solutions-d{d}.txt").read().split()]

print("== block decomposition: full set == {k*10^10 + s : k in 0..d-1, s in B_d} ==")
seeds = {}
for d in range(1, 10):
    Bd = [n for n in sols[d] if n < 10**10]
    seeds[d] = Bd
    rebuilt = sorted(k * 10**10 + s for k in range(d) for s in Bd)
    ok = (rebuilt == sols[d])
    print(f"  d={d}: |B_d|={len(Bd):>3}  |sols|={len(sols[d]):>3}  blocks={list(range(d))}  exact={ok}")
    assert ok, f"d={d} block decomposition FAILED"

print("\n== 5*10^8 translation, d in 1..4 ==")
for d in range(1, 5):
    f5e8 = f_place_value(5 * 10**8, d)
    # theorem precondition
    assert f5e8 == 5 * 10**8, (d, f5e8)
    # data consequence: B_d ∩ [5e8, 6e8) == {5e8 + s : s in B_d, s < 10^8}
    upper = sorted(s for s in seeds[d] if 5 * 10**8 <= s < 6 * 10**8)
    shift = sorted(5 * 10**8 + s for s in seeds[d] if s < 10**8)
    match = (upper == shift)
    print(f"  d={d}: f(5e8,{d})={f5e8} (={5*10**8} required)  "
          f"B_d∩[5e8,6e8)=[5e8+s : s<1e8] exactly: {match}  "
          f"({len(shift)} shifted terms)")
    assert match, d
# random-sample check of the translation identity itself for d=1..4
random.seed(20240601)
bad = 0
for d in range(1, 5):
    for _ in range(20000):
        x = random.randrange(0, 10**8)
        n = 5 * 10**8 + x
        if f_place_value(n, d) - f_place_value(x, d) != 5 * 10**8:
            bad += 1
print(f"  identity f(5e8+x,d)-f(x,d)=5e8, random x<1e8, d=1..4: 80000 checks, failures={bad}")

print("\n== run lengths inside B_d ==")
for d in range(1, 10):
    Bd = seeds[d]
    runs = []
    i = 0
    while i < len(Bd):
        j = i
        while j + 1 < len(Bd) and Bd[j + 1] == Bd[j] + 1:
            j += 1
        runs.append((Bd[i], j - i + 1))
        i = j + 1
    lengths = [L for _, L in runs]
    print(f"  d={d}: runs={lengths}   (starts {[s for s,_ in runs]})")

print("\n== within-run condition: each number past the run start has exactly one d ==")
allok = True
probs = []
for d in range(1, 10):
    Bd = seeds[d]
    i = 0
    while i < len(Bd):
        j = i
        while j + 1 < len(Bd) and Bd[j + 1] == Bd[j] + 1:
            j += 1
        if j > i:  # run of length >= 2
            for n in Bd[i + 1:j + 1]:
                if str(n).count(str(d)) != 1:
                    allok = False
                    probs.append((d, n))
        i = j + 1
print(f"  holds for every element of every run (run length >= 2): {allok}"
      + (f"  violations: {probs[:5]}" if not allok else ""))

print("\n== seed sets (ordered, one per line for the sequence tools) ==")
for d in range(1, 10):
    print(f"B_{d} ({len(seeds[d])} terms): {seeds[d]}")