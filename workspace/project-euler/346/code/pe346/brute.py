"""Brute-force strong repunits below N.

A repunit in base b (b>1) of length k is (b^k - 1)/(b - 1) = 1 + b + ... + b^{k-1}.
Every positive integer n>1 is a repunit of length 2 in base n-1 ("11"). So a
number n>1 is STRONG (repunit in >=2 bases) iff it is a repunit of length k>=3
in some base b>1.  The number 1 counts trivially (repunit length 1 in any base).

So enumerate every distinct r = (b^k-1)/(b-1) for k>=3, b>=2, r <= N, plus 1.
"""

def strong_repunits(N):
    s = set()
    if N >= 1:
        s.add(1)
    b = 2
    import math
    while True:
        # length-3 value = b^2 + b + 1 ; need it <= N
        if b*b + b + 1 > N:
            break
        # k = 3, 4, ...
        val = b*b + b + 1  # k=3
        pw = b*b*b       # b^k
        k = 3
        while val <= N:
            s.add(val)
            # next k: multiply by b and add 1 * b^{k}? recompute cleanly
            pw *= b
            k += 1
            val = (pw - 1)//(b - 1)
        b += 1
    return sorted(s)

def main():
    for N, wantlist, wantsum in [
        (50, [1,7,13,15,21,31,40,43], None),
        (1000, None, 15864),
    ]:
        sr = strong_repunits(N)
        print("N =", N)
        print("  strong repunits:", sr)
        print("  count:", len(sr), " sum:", sum(sr))
        if wantlist:
            print("  matches example list:", sr == wantlist)
        if wantsum:
            print("  sum matches example:", sum(sr) == wantsum)

if __name__ == "__main__":
    main()
