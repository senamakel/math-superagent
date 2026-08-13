"""EXECUTE THIS to independently reproduce the A088959/A088111 record-holder check.

Hand-checked by scholar 2026-08-13 for the first 9 terms (0,1,2,4,7,13,22,31,40),
verifying A088959 record-holders = argmax of |S(e)| = (prod_{p=1 mod 4}(2a+1)-1)/2:
e: 1 5 25 65 325 1105 5525 27625 32045
factor: - 5 5^2 5.13 5^2.13 5.13.17 5^2.13.17 5^3.13.17 5.13.17.29
|S(e)|: 0 1 2 4 7 13 22 31 40   (next 4k+1 prime multiplies in)

Run with:  python3 code/out/verify_a088959_records.py
Cost: spf sieve to 3e6, O(N log log N). Prints MATCH.
"""
import sys

N = int(sys.argv[1]) if len(sys.argv) > 1 else 3_000_000
expected_raw = "1,5,25,65,325,1105,5525,27625,32045,160225,801125,1185665,5928325,29641625,48612265,243061325,1215306625,2576450045"
expected = [int(t) for t in expected_raw.split(",") if int(t) <= N]

spf = list(range(N + 1))
for i in range(2, int(N**0.5) + 1):
    if spf[i] == i:
        for j in range(i * i, N + 1, i):
            if spf[j] == j:
                spf[j] = i

def S_count(e):
    prod = 1
    x = e
    while x > 1:
        p = spf[x]
        a = 0
        while x % p == 0:
            x //= p
            a += 1
        if p % 4 == 1:
            prod *= (2 * a + 1)
    return (prod - 1) // 2

records, best = [], -1
for e in range(1, N + 1):
    v = S_count(e)
    if v > best:
        best = v
        records.append(e)

ok = records == expected
print(f"|S(e)| records e<={N}: first 12 {records[:12]}")
print(f"expected A088959 within range: {expected}")
print("MATCH:", ok)
if not ok:
    print("extra:", set(records) - set(expected))
    print("missing:", set(expected) - set(records))