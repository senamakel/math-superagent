"""Task B: eventual periodicity of r(k) = Psi(k) mod M.

Loads exact Psi(1..150), computes r(k)=Psi(k) mod M, and searches for a
period T with a preperiod: glue(n+k) == glue(n+k+T) for all k beyond some
point. Reports the smallest preperiod and period found empirically on k<=150.

Exact integer arithmetic throughout.
"""
import os

MOD = 101001001
DATA = os.path.join(os.path.dirname(__file__), "..", "out", "psi_data_1_150.txt")


def load_psi(path):
    psi = {}
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or ":" not in line:
                continue
            parts = line.split(":")
            try:
                k = int(parts[0].strip())
            except ValueError:
                continue
            # value is the last colon field
            val = parts[-1].strip()
            psi[k] = int(val)
    return psi


def find_eventual_period(arr, max_period=1000):
    """Smallest (preperiod, period) such that arr[i]==arr[i+period] for all
    i >= preperiod AND all in-range indices agree. We search preperiod from 0
    upward and period from 1 upward; return first that satisfies for all
    available indices (a necessary condition given finite data)."""
    n = len(arr)
    for pre in range(0, n):
        for T in range(1, max_period + 1):
            ok = True
            for i in range(pre, n - T):
                if arr[i] != arr[i + T]:
                    ok = False
                    break
            if ok:
                return pre, T
    return None


def main():
    psi = load_psi(DATA)
    ks = sorted(psi)
    seq = [psi[k] for k in ks]
    r = [x % MOD for x in seq]
    print("Loaded Psi(k) for k =", ks[0], "..", ks[-1], "count =", len(ks))
    print(f"r(k) = Psi(k) mod {MOD}")
    print("r(1..40) =", r[:40])
    print()
    print("k=10 check: r(10) =", r[9], "(expect 10699667)")

    print("\n--- searching for pure periodicity (preperiod 0) ---")
    # Try preperiod 0: is r purely periodic with some T?
    n = len(r)
    found_pure = None
    for T in range(1, n // 2 + 1):
        if all(r[i] == r[i + T] for i in range(n - T)):
            found_pure = T
            break
    print("pure period T (preperiod 0):", found_pure)

    print("\n--- searching for eventual periodicity ---")
    res = find_eventual_period(r, max_period=3000)
    print("eventual (preperiod, period):", res)

    print("\n--- print r(k) table k=1..150 to eyeball ---")
    for i in range(0, 150, 10):
        print("k=", i + 1, "..", i + 10, ":", r[i:i + 10])


if __name__ == "__main__":
    main()
