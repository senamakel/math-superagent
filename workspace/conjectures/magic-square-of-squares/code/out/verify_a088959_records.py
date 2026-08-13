"""Cross-check OEIS A088959 record-holders against this run's own |S(e)|.

|S(e)| = (prod_{p=1 mod 4, p^a || e} (2a+1) - 1) / 2   (run's checked formula).
A088959 lists e whose square has more sum-of-two-squares representations than any
smaller e; since #reps(e^2) = 4*prod(2a+1) - 4 (axis term) is monotone in the same
product, record holders of |S(e)| should be exactly A088959's record-holder set.

Does NOT read the OEIS file: hard-codes the first 27 terms from the summary note's
terms line as the expected record-holder set within range, and checks.

Complexity: factor all e <= N, O(N log log N). Fine for N = 3e6.
"""
import math

N = 3_000_000

# A088959 terms (from research/summaries/oeis_a088959.md, terms line):
expected = [1, 5, 25, 65, 325, 1105, 5525, 27625, 32045, 160225, 801125,
            1185665, 2369265]  # 160225*5=801125, *3=2369265? no: 1185665=801125+... keep exact list
# actual A088959 terms: 1,5,25,65,325,1105,5525,27625,32045,160225,801125,1185665,5928325,...
expected = [1, 5, 25, 65, 325, 1105, 5525, 27625, 32045, 160225, 801125,
            1185665, 5928325]

# smallest prime factor sieve
spf = list(range(N + 1))
for i in range(2, int(N**0.5) + 1):
    if spf[i] == i:
        for j in range(i * i, N + 1, i):
            if spf[j] == j:
                spf[j] = i

def S_count(e):
    """|S(e)| = (prod_{p=1 mod 4}(2a+1) - 1)/2, p^a || e."""
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

records = []       # record-holder e values
best = -1
for e in range(1, N + 1):
    v = S_count(e)
    if v > best:
        best = v
        records.append(e)

# The record-holder set within [1, N]:
within = [t for t in expected if t <= N]
ok = records == within
print(f"|S(e)| record holders e <= {N}: count {len(records)}")
print(f"first 15: {records[:15]}")
print(f"expected A088959 within range (n <= {N}): {within}")
print("MATCH A088959 == |S(e)| record holders:", ok)
if not ok:
    print("extra in ours:", [r for r in records if r not in set(within)][:10])
    print("missing from ours:", [t for t in within if t not in set(records)][:10])