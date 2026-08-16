#!/usr/bin/env python3
"""Independent refutation checks by direct computation.

(1) Soundness of the mod-9 filter: every root in the A038206 b-file
    (and hence every S-number) must be == 0 or 1 (mod 9).  If any b-file root
    has a different residue, the filter is unsound and the classification
    'every S-root m satisfies m == 0 or 1 (mod 9)' is FALSE.

(2) Independent recomputation of T(10^12) from the b-file roots, checking the
    verification route does not contain an off-by-one or transcription error.

(3) The mod-9 invariant on the actual worked example set, plus a scan of ALL
    roots m in [2,10^6] using the exact recursion, to check no root with
    residue 2..8 passes the S-test (numerical soundness check of the filter
    at full scale, independent of the catalogue).
"""
import math

roots = []
with open("code/out/roots408.txt") as f:
    for line in f:
        line = line.strip()
        if line:
            roots.append(int(line))

print("loaded", len(roots), "roots")

# (1) mod-9 classification check on the b-file roots
bad = [(m, m % 9) for m in roots[2:] if m % 9 not in (0, 1)]
print("=== (1) mod-9 filter soundness on b-file roots (excluding 0,1 sentinels) ===")
print("roots with residue not in {0,1}:", bad if bad else "NONE -> filter sound on b-file")

# (2) independent T(10^12) recomputation
t12 = sum(m * m for m in roots if 2 <= m <= 10**6)
print("=== (2) T(10^12) from b-file roots, m in [2,10^6] ===")
print("T(10^12) =", t12)
print("matches claimed 128088830547982:", t12 == 128088830547982)

# (3) full-scale numerical soundness of the filter via the exact recursion
def is_s_root(m):
    s = str(m * m)
    n = len(s)
    memo = {}
    def expr(i):
        if i in memo:
            return memo[i]
        res = set()
        val = 0
        for j in range(i, n):
            val = val * 10 + int(s[j])
            if j == n - 1:
                res.add(val)
            else:
                for sub in expr(j + 1):
                    res.add(val + sub)
        memo[i] = res
        return res
    val = 0
    for j in range(0, n - 1):
        val = val * 10 + int(s[j])
        if (m - val) in expr(j + 1):
            return True
    return False

print("=== (3) full-scale mod-9 filter soundness, m in [2,10^6] ===")
bad_full = []
count_badres_sroots = 0
# scan a full decade grid fast: actually scan ALL roots 2..10^6
for m in range(2, 10**6 + 1):
    if is_s_root(m):
        if m % 9 not in (0, 1):
            count_badres_sroots += 1
            if len(bad_full) < 10:
                bad_full.append(m)
print("S-roots with residue NOT in {0,1}: count =", count_badres_sroots)
print("examples:", bad_full if bad_full else "NONE")
print("RESULT:", "FILTER SOUND" if count_badres_sroots == 0 else "FILTER UNSOUND!")
