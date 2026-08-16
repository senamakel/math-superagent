#!/usr/bin/env python3
"""Test the 'suspicious partial family' of consecutive S-root pairs flagged in
seq_decades.txt: are (10^k - 10^j, 10^k - 10^j + 1) provably BOTH S-roots for
all k (j fixed in 1..k-1)? The notes called these 'a suspicious partial family'
but never verified whether they are a genuine exact regularity.

We test up to the full b-file (3200 roots, max ~1.03e9): for fixed j, do ALL
of 10^k - 10^j and 10^k - 10^j + 1 (k = j+1 .. K) appear as S-roots?  If yes
through the whole catalogue, it is a real exact family (conjecture, first
falsifier = the first k that fails, if any).  Also re-derive the splits that
witness 10^k-10^j being an S-root, to see the mechanism."""
import re

B_FILE = "research/sources/oeis_a038206_b.full.md"
def load_roots(path):
    roots = []
    with open(path) as f:
        for line in f:
            m = re.match(r"\s*(\d+)\s+(\d+)\s*$", line)
            if m:
                roots.append(int(m.group(2)))
    return roots

R = load_roots(B_FILE)
S = set(R)
MAXR = max(R)
print(f"Loaded {len(R)} roots, max = {MAXR}")

# partition witness: can m^2 split into >=2 blocks summing to m?
def is_s(m):
    s = str(m*m)
    from functools import lru_cache
    @lru_cache(maxsize=None)
    def expr(target, i):
        if target < 0: return False
        rest = s[i:]
        if target == int(rest): return True
        for j in range(i+1, len(s)):
            if expr(target - int(s[i:j]), j): return True
        return False
    for j in range(1, len(s)):
        if expr(m - int(s[:j]), j): return True
    return False

print("\nConsecutive-pair family test: is BOTH 10^k-10^j and +1 an S-root?")
print(f"{'j':>2} | families 10^k-10^j (k=..)          | +1                      | both through max")
for j in range(1, 7):
    lo_ok, hi_ok = True, True
    first_fail_lo = first_fail_hi = None
    cnt = 0
    k = j+1
    while True:
        vlo = 10**k - 10**j
        vhi = vlo + 1
        if vhi > MAXR: break
        cnt += 1
        if vlo not in S and first_fail_lo is None:
            first_fail_lo = (k, vlo)
            lo_ok = False
        if vhi not in S and first_fail_hi is None:
            first_fail_hi = (k, vhi)
            hi_ok = False
        k += 1
    status = "BOTH-all" if (lo_ok and hi_ok) else \
             ("hi-fails" if not hi_ok else ("lo-fails" if not lo_ok else "?"))
    print(f"{j:>2} | checked {cnt:<3} values to max      | firstfail_lo={first_fail_lo} | firstfail_hi={first_fail_hi} | {status}")

# mechanism: show the actual split for a few of these roots
print("\nWitness splits for small members:")
for (m,) in [(990,), (9990,), (9900,), (9990,), (99000,), (99001,), (9999,), (99990,)]:
    s = str(m*m)
    # find a 2-block or 3-block split summing to m
    hit = None
    for cut in range(1, len(s)):
        a = int(s[:cut]); b = int(s[cut:])
        if a + b == m:
            hit = (s[:cut], s[cut:]); break
    print(f"  m={m} m^2={s} isS={is_s(m)} 2-block={hit}")
