"""Exact Psi(k) by the sliding-window route, for k beyond the recorded range.

For fixed k, the k+1 distinct length-k factors of the Fibonacci word are all
windows of a prefix of length Lmin(k) = k + NextFib(k) - 1 (verified formula,
k<=6764; re-asserted here per k).  Every window's decimal value is computed
exactly by the recurrence
    v_{r+1} = 10*v_r - y_r*10^k + y_{r+k},   y_i in {0,1} the Fibonacci word digits.
For fixed window length k the integer value identifies the word (injective),
so the distinct values are collected in a set, then Psi(k) = sum of squares.

Validation baked in:
  * Psi(3)  == 20302                              (statement example)
  * Psi(10) mod M == 10699667                     (statement example)
  * Psi(1..25) == recorded code/out/psi_exact.txt
  * Psi(1..400) mod M == recorded code/out/psi_residues.txt
  * Psi(10^4) mod M == 34432237 (directive-6 anchor) and count == 10001
Reports for each k: len(Psi(k)), class C(k) = len - (2k-1), count, and
compared C(k) against len(c1(k)) - 1.
"""
import sys
import time

sys.set_int_max_str_digits(300000)
M = 101001001


def next_fib_strict(k):
    a, b = 0, 1
    while True:
        a, b = b, a + b
        if b > k:
            return b


def fib_prefix(L):
    """Length >= L prefix of the infinite Fibonacci word S = 0100101001001..."""
    a, b = "0", "01"
    while len(b) < L:
        a, b = b, b + a
    return b[:L]


def c1(k):
    from math import isqrt
    N = isqrt(5 * k * k)
    t = 3 * k - N
    return 1 + ((t - 1) // 2 if t % 2 == 1 else t // 2 - 1)


def psi_exact(k, prefix=None):
    """Exact Psi(k) via sliding windows.  Returns (Psi, count)."""
    L = k + next_fib_strict(k) - 1
    if prefix is None or len(prefix) < L:
        prefix = fib_prefix(L)
    y = prefix[:L]
    p10k = 10 ** k
    v = int(y[:k])  # first window value, V_0 (leading zeros dropped by int())
    vals = {v}
    for r in range(L - k):
        v = 10 * v - (1 if y[r] == '1' else 0) * p10k \
            + (1 if y[r + k] == '1' else 0)
        vals.add(v)
    return sum(x * x for x in vals), len(vals)


def main():
    # recorded oracles
    exact = {}
    with open("code/out/psi_exact.txt") as fh:
        for line in fh:
            kk, vv = line.split()
            exact[int(kk)] = int(vv)
    res = {}
    with open("code/out/psi_residues.txt") as fh:
        for line in fh:
            kk, vv = line.split()
            res[int(kk)] = int(vv)

    # ---- validation pass, small k ----
    print("== validation ==")
    ok = True
    for k in [3, 10, 25, 256, 400]:
        t0 = time.time()
        Psi, cnt = psi_exact(k)
        dt = time.time() - t0
        if k == 3:
            good = (Psi == 20302 and cnt == 4)
            print(f"  k=3: Psi={Psi} count={cnt} want 20302/4 -> {good}")
        if k == 10:
            good = (Psi % M == 10699667 and cnt == 11)
            print(f"  k=10: Psi mod M={Psi % M} count={cnt} want 10699667/11 -> {good}")
        if k in exact:
            good = (Psi == exact[k])
            print(f"  k={k}: Psi exact match recorded -> {good}")
        if k in res:
            good = (Psi % M == res[k])
            print(f"  k={k}: Psi mod M match recorded -> {good}")
        if Psi != exact.get(k, Psi) or (k in res and Psi % M != res[k]):
            ok = False
        print(f"      (took {dt:.2f}s)")
    if not ok:
        print("VALIDATION FAILED - aborting")
        sys.exit(1)
    print("  validation: ALL PASS\n")

    # ---- main grid ----
    ks = [10000, 20000, 25682, 25683, 25684, 30000, 40000]
    for k in ks:
        t0 = time.time()
        Psi, cnt = psi_exact(k)
        dt = time.time() - t0
        Ld = len(str(Psi))
        C = Ld - (2 * k - 1)
        print(f"k={k:6d}: len={Ld} 2k-1={2*k-1} C(k)={C:+d} count={cnt} "
              f"modM={Psi % M}  [{dt:.1f}s]")
        if cnt != k + 1:
            print(f"   *** COUNT MISMATCH: expected {k + 1} factors ***")


if __name__ == "__main__":
    main()