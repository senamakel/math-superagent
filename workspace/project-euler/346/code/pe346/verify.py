"""Independent verification of PE346 answer at N = 10^12.

Different structure: iterate over length k (>=3) explicitly with a growing
'current' value per base tracked in a list, then dedup. No pw arithmetic.
This gives an independent route to the same set.
"""
def strong_repunits(N):
    s = set()
    if N >= 1:
        s.add(1)
    b = 2
    while b*b + b + 1 <= N:
        val = b*b + b + 1    # length 3
        while val <= N:
            s.add(val)
            val = val*b + 1  # next length: 111..1 in base b
        b += 1
    return s

if __name__ == "__main__":
    for N in (10**3, 10**6, 10**9, 10**12):
        s = strong_repunits(N)
        print(N, len(s), sum(s))
