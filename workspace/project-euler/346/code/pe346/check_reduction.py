"""Verify the structural reduction:
strong_sum(N) = 1 - 31 - 8191 + sum over all (b,k>=3) pairs of (b^k-1)/(b-1) < N

i.e. the dedup correction is exactly the two double-base repunits 31 and 8191.
Check the pair-sum equals strong_sum + 31 + 8191 - 1 at several N and at 10^12.
"""
def pair_sum(N):
    total = 0
    b = 2
    while b*b + b + 1 < N:
        k = 3
        while True:
            v = (pow(b, k) - 1)//(b - 1)
            if v >= N:
                break
            total += v
            k += 1
        b += 1
    return total

# known strong sums (incl. the value 1) from verified runs
known = {
    1000:   15864,
    10**4:  450740,
    10**6:  372810163,
    10**10: 339706288602849,
    10**12: 336108797689259276,
}
DUPS = [31, 8191]
for N, s in known.items():
    ps = pair_sum(N)
    predicted = 1 - sum(DUPS) + ps      # strong_sum = 1 - 31 - 8191 + pair_sum
    print(f"N={N:<13d} pair_sum={ps:<20d} predicted_strong={predicted:<22d} known={s}  match={predicted==s}")
