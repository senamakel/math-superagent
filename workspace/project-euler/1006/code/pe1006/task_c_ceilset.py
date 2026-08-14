"""Characterize exactly which columns i get the +1 (ceil) count.

N(i;k) = (k+1 row-count) ones across column i. Verified: N in {L, L+1}, L=floor((k+1)a).
We now test the sharp hypothesis: the ceLD set {i : N(i;k)=L+1} equals the set
{ i : the i-th factor-window-start class } from the Sturmian structure, and
characterise it as a mechanical/Beatty set in i with period driven by the
Fibonacci/Zeckendorf data of k+1. We report the exact empirical function and
whether it matches all k<=40.
"""
import json, os
from mpmath import mp, mpf, sqrt, floor

mp.dps = 80
DATA = os.path.join(os.path.dirname(__file__), "..", "out", "factors_k40.json")
a = mpf(3) / 2 - sqrt(5) / 2


def load():
    return json.load(open(DATA))


def frac(x):
    return x - floor(x)


def main():
    data = load()
    ceilset = {}
    Lval = {}
    for k in range(1, 41):
        facs = data[str(k)]
        N = [sum(1 for f in facs if f[i] == '1') for i in range(k)]
        L = int(floor((k + 1) * a))
        Lval[k] = L
        assert all(n in (L, L + 1) for n in N), (k, N, L)
        ceilset[k] = set(i for i, n in enumerate(N) if n == L + 1)
        # verifies the earlier claim, print nothing heavy

    print("Verified: for all k<=40, N(i;k) in {floor((k+1)a), floor((k+1)a)+1}.")
    print("Now characterise ceil set = {i : N(i;k)=floor((k+1)a)+1}.\n")

    print("Test: ceilset(k) = { i : frac((k+1 - i)*a) >= 1 - a }  (a-shift class)\n")
    # candidate: the columns that are 'long' correspond to starts whose window
    # overruns; try a few thresholded mechanical forms.
    cand_forms = {
        "frac((k+1-i)*a)>=1-a": lambda k, i: frac((mpf(k + 1) - i) * a) >= 1 - a,
        "frac((i+1)*a)<a": lambda k, i: frac((i + 1) * a) < a,
        "frac(i*a)<a": lambda k, i: frac(i * a) < a,
        "frac((k-i)*a)<a": lambda k, i: frac((k - i) * a) < a,
        "floor((i+1)*a2)-floor(i*a2)==1 a2=1/a": lambda k, i: (lambda t=1/a: floor((i+1)*t)-floor(i*t)==1)(),
        "1 if frac((i+1)/phi)<1": lambda k, i: (lambda t=(mpf(5)**mpf(0.5)+1)/2: frac((i+1)*t) >= t-1)(),
    }
    for name, fn in cand_forms.items():
        bad = 0
        first = None
        for k in range(1, 41):
            pred = set(i for i in range(k) if fn(k, i))
            diff = pred ^ ceilset[k]
            if diff:
                bad += len(diff)
                if first is None:
                    first = (k, sorted(diff)[:6])
        print(f"  {name}: mismatched entries total = {bad}", "| first:", first if first else "NONE -> perfect match")

    # Print ceil sets compactly and look for the period/pattern
    print("\nCeil sets in k (i listed):")
    for k in range(1, 41):
        print(f"  k={k:2d} L={Lval[k]:2d} ceilset={sorted(ceilset[k])}")

    # Summary: what does the whole thing depend on? sum_i N(i;k) over i =
    # total ones across all factors. Print and note relation to floor((k+1)a)*(k) ...
    print("\nsum_i N(i;k) = total-#ones | k+1 rows each ~(k+1)a ones -> expect ~(k+1)*(k+1)a")
    for k in range(1, 41):
        facs = data[str(k)]
        N = [sum(1 for f in facs if f[i] == '1') for i in range(k)]
        print(f"  k={k:2d}: sum N = {sum(N)}", f"| size ceilset = {len(ceilset[k])}", f"| L*(k)+ceilset = {Lval[k]*k+len(ceilset[k])}")


if __name__ == "__main__":
    main()
