"""Precise digit-length study of exact Psi(k), k=1..3000.

Builds Psi via the exact k-step recurrence from recorded vR/s1 exact data
(validated against recorded Psi(1..25) in the previous check), then examines
the decimal length:
    len(Psi(k)) == 2k-1  or  2k   ?
and finds the first k where len == 2k.
"""
import sys
import mpmath as mp
sys.set_int_max_str_digits(20000)

mp.mp.dps = 80
PHI2_INV = mp.mpf(1) / ((1 + mp.sqrt(5)) / 2) ** 2

def c1(k):
    return 1 + int(mp.floor(k * PHI2_INV))

def load_pairs(path, limit=None):
    out = {}
    with open(path) as fh:
        for line in fh:
            p = line.split()
            if len(p) < 2:
                continue
            out[int(p[0])] = int(p[1])
    return out

def main():
    vR = load_pairs("code/out/vR_exact.txt")
    s1 = load_pairs("code/out/s1_exact.txt")
    Psi = {1: 1}
    for k in range(1, 3000):
        Psi[k + 1] = 100 * Psi[k] + 100 * vR[k] ** 2 + 20 * s1[k] + c1(k + 1)

    from collections import Counter
    lens = Counter()
    first_2k = None
    bad = []
    for k in range(1, 3001):
        L = len(str(Psi[k]))
        lens[L - (2 * k - 1)] += 1   # 0 => 2k-1 digits, 1 => 2k digits
        if L == 2 * k and first_2k is None:
            first_2k = k
        if L not in (2 * k - 1, 2 * k):
            bad.append((k, L))
    print("len - (2k-1) distribution over k=1..3000:", dict(lens))
    print("first k with len == 2k:", first_2k)
    print("k values with len not in {2k-1,2k}:", bad)

    # where does the length stay 2k-1 vs 2k?  print the first ~60 k with len=2k-1
    odd = [k for k in range(1, 3001) if len(str(Psi[k])) == 2 * k - 1]
    print("count with 2k-1 digits:", len(odd))
    print("first 60 such k:", odd[:60])
    print("last 20 such k:", odd[-20:])

if __name__ == "__main__":
    main()