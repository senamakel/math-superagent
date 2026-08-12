"""Count genuine duplicates: values that are repunits of length >=3 in >=2
distinct bases, below a bound. Also count the raw (b,k) pairs and the dedup
correction = pairs - distinct.
"""
import sys

def pair_value(b, k):
    # (b^k - 1)//(b - 1)
    return (pow(b, k) - 1)//(b - 1)

def stats(N):
    vals = set()          # distinct strong repunits > 1
    pairs = 0
    b = 2
    while b*b + b + 1 < N:
        k = 3
        while True:
            v = pair_value(b, k)
            if v >= N:
                break
            pairs += 1
            if v in vals:
                dup_holder = v
            vals.add(v)
            k += 1
        b += 1
    return len(vals), pairs

if __name__ == "__main__":
    for p in range(1, 12):
        N = 10**p
        d, pr = stats(N)
        print(f"p={p:2d} N=10^{p:<2d} distinct={d:7d} pairs={pr:7d} correction={pr-d:5d}")
