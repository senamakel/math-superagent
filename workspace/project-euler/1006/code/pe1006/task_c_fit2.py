"""Fit N(i;k) = number of length-k factors with a 1 at position i, testing the
task-suggested closed form N(i;k) = floor((k - i)*a + const) and variants,
finding which const matches ALL k<=40 (and how close each gets).

a = (3-sqrt5)/2 = 1/phi^2. We test const in a fine grid around a and related
candidates, plus forms floor((k+1-i)*a + c), floor(k*a - i*a + c), etc.
"""
import json, os
from mpmath import mp, mpf, sqrt, floor

mp.dps = 60
DATA = os.path.join(os.path.dirname(__file__), "..", "out", "factors_k40.json")
ALPHA = mpf(3) / 2 - sqrt(5) / 2


def load():
    return json.load(open(DATA))


def N_table(data):
    N = {}
    for k in range(1, 41):
        facs = data[str(k)]
        N[k] = [sum(1 for f in facs if f[i] == '1') for i in range(k)]
    return N


def check(form, N):
    """form(i, k) -> predicted N. Return number of mismatched (i,k)."""
    bad = 0
    for k in range(1, 41):
        for i in range(k):
            p = form(i, k)
            if p != N[k][i]:
                bad += 1
    return bad


def main():
    data = load()
    N = N_table(data)

    print("Testing N(i;k) = floor((k - i)*a + const)  over a fine const grid:")
    best = None
    c = mpf('-0.5')
    step = mpf('0.001')
    while c <= mpf('1.5'):
        bad = check(lambda i, k, c=c: int(floor((k - i) * ALPHA + c)), N)
        if best is None or bad < best[0]:
            best = (bad, c)
        c += step
    print("  best (bad, const):", best, " (bad=0 means perfect match)")

    print("\nTesting N(i;k) = floor((k+1 - i)*a + const):")
    best2 = None
    c = mpf('-0.5')
    while c <= mpf('1.5'):
        bad = check(lambda i, k, c=c: int(floor((mpf(k + 1) - i) * ALPHA + c)), N)
        if best2 is None or bad < best2[0]:
            best2 = (bad, c)
        c += step
    print("  best (bad, const):", best2)

    print("\nTesting N(i;k) = floor((k - i)*a) + delta(i) where delta counts something:")
    # From the data, N(i;k) = floor((k+1)*a) + e(i), e in {0,1}. Test
    # N(i;k) = floor((k+1 - i)*a) :  how many match?
    bad3 = check(lambda i, k: int(floor((mpf(k + 1) - i) * ALPHA)), N)
    print("  N=floor((k+1-i)*a) mismatches:", bad3)
    bad4 = check(lambda i, k: int(floor((k - i) * ALPHA + ALPHA)), N)
    print("  N=floor((k-i)*a + a) mismatches:", bad4)
    bad5 = check(lambda i, k: int(floor((mpf(k) - i) * ALPHA)), N)
    print("  N=floor((k-i)*a) mismatches:", bad5)

    print("\nDetailed per-k check of N(i;k)=" + "floor((k+1-i)*a)+e(i) e in{0,1} (must hold):")
    ok = True
    for k in range(1, 41):
        for i in range(k):
            lo = int(floor((mpf(k + 1) - i) * ALPHA))
            if N[k][i] not in (lo, lo + 1):
                ok = False
                print(f"  fails k={k} i={i}: N={N[k][i]} lo={lo}")
    print("  N(i;k) in {floor((k+1-i)*a), +1}:", ok)


if __name__ == "__main__":
    main()
