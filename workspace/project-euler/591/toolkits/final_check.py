"""Final independent checks on results_full.txt:
1. Re-sum S by hand from the file.
2. Verify each row: b <= floor(1e13/sqrt(d)), a == nint(pi - b*sqrt(d)) high precision.
3. Check d=2 oracle row.
4. Cross-check a few d against results_independent.txt when it appears.
"""
import math, mpmath as mp
mp.mp.dps = 80
pi = mp.mpf('3.1415926535897932384626433832795028841971693993751058209749445923')

res = {}
for line in open('/workspace/results_full.txt'):
    p = line.split()
    if p and p[0].isdigit():
        d = int(p[0]); b = int(p[1]); a = int(p[2]); absa = int(p[3])
        res[d] = (b, a, absa)

S = 0
fails = 0
for d in range(2, 100):
    if math.isqrt(d)**2 == d: continue
    b, a, absa = res[d]
    S += absa
    L = int(mp.floor(mp.mpf(10)**13 / mp.sqrt(d)))
    sd = mp.sqrt(d)
    expect_a = mp.nint(pi - b * sd)
    if b > L:
        fails += 1; print(f"FAIL b>L: d={d}")
    if int(expect_a) != a:
        fails += 1; print(f"FAIL a mismatch: d={d} got {a} expect {int(expect_a)}")
print("S re-summed:", S, " fails:", fails)

# d=2 oracle
b2,a2,_ = res[2]
print("d=2:", b2, a2, "expected b=4375636191520, a=-6188084046055:",
      b2==4375636191520 and a2==-6188084046055)

# cross-check against independent file if exists
import os
if os.path.exists('/workspace/results_independent.txt'):
    indep = {}
    for line in open('/workspace/results_independent.txt'):
        p = line.split()
        if p and p[0].isdigit():
            indep[int(p[0])] = (int(p[1]), int(p[2]), int(p[3]))
    mismatch = [d for d in res if d in indep and res[d] != indep[d]]
    print("independent file: rows match:", len(mismatch)==0, "mismatch d:", mismatch)
    if indep:
        print("independent S:", sum(v[2] for v in indep.values()))