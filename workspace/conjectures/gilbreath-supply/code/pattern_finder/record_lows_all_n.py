#!/usr/bin/env python3
"""Complete record-low analysis of nu2(n)/n over ALL n in [2, 40000] (earlier
runs only looked at n >= 50), plus block minima from n=2 (not from 2^5).

The global minimum over [2,40000] is potentially below the quoted 0.3396
(which was over [50,4000] in problem.md). Establish exactly; also record the
upward-closing statement: does the running minimum ever improve after 53?
"""
import json

data = json.load(open('/workspace/code/out/nu2_primes_xor_40000.json'))
assert data[53] == 18 and data[64] == 27 and data[4000] == 1975 and data[40000] == 20081
N = 40000

def nu2(n):
    return data[n]

def S(n):
    return (n - 2) - 2 * nu2(n)

# running minimum over n = 4..40000 (n=2,3 have empty depth range [2,n-1],
# so nu2(2)=nu2(3)=0 trivially and would dominate the record analysis;
# the problem's "sufficiently large n" regime starts where the range is nonempty)
records = []   # (n, nu2(n)/n as Fraction, nu2(n))
cur_num, cur_den = nu2(4), 4
for n in range(4, N + 1):
    num, den = nu2(n), n
    if num * cur_den < cur_num * den:
        records.append((n, num, den, num / den))
        cur_num, cur_den = num, den

print(f"== record lows of nu2(n)/n over [4,{N}] ==")
print(f"count: {len(records)}")
for (n, num, den, v) in records:
    print(f"  n={n:6d}  nu2={num:5d}  nu2/n={num}/{den}={v:.6f}  S(n)={S(n):6d}")
print(f"global min over [4,{N}]: nu2({records[-1][0]})/{records[-1][0]} = {cur_num}/{cur_den}")
print("note: problem.md quoted min 0.3396 over [50,4000]; the TRUE global min over [4,40000] "
      "is at n=%d with %.6f" % (records[-1][0], cur_num / cur_den))

# after the last record, never improves again?
last_n = records[-1][0]
improved_after = any(nu2(n) * cur_den < cur_num * n for n in range(last_n + 1, N + 1))
print(f"running min ever improves after n={last_n}? {improved_after}")

# per-doubling block minima from n=2
print("\n== per-doubling block minima from n=2 ==")
for k in range(1, 16):
    lo, hi = 1 << k, min((1 << (k + 1)) - 1, N)
    if lo > N:
        break
    best_n, bn, bd = lo, nu2(lo), lo
    for n in range(lo, hi + 1):
        if nu2(n) * bd < bn * n:
            best_n, bn, bd = n, nu2(n), n
    print(f"  [2^{k:2d},2^{k+1})", f" min={bn}/{bd}={bn/bd:.6f} at n={best_n}")

# exact size of exceptional sets at several c (from n=2)
print("\n== exact {n in [2,40000] : nu2(n)/n < c} sizes ==")
from fractions import Fraction
for cval in [0.30, 0.35, 0.40, 0.42, 0.45, 0.46, 0.47, 0.48, 0.485, 0.49]:
    cf = Fraction(cval).limit_denominator(100000)
    members = [n for n in range(2, N + 1) if Fraction(nu2(n), n) < cf]
    print(f"  c={cval}: size={len(members):5d} max={max(members) if members else '-'}")
    if cval == 0.40:
        print("    members:", members)