"""PE1006: Psi(F_m) from the Christoffel/Sturmian base-word construction.

Structural fact (established, verified k=2..55 against structure.json): at
Fibonacci index k=F_m, the k+1 length-k factors of the Fibonacci word are
exactly the k distinct circular rotations of ONE Christoffel word ("base"),
plus ONE singular factor.

The base Christoffel word has slope alpha = 1/phi^2 = (3-sqrt5)/2, length k,
and F_{m-2} ones.  We build it *exactly* as a mechanical word with the exact
rational slope p/k where p = F_{m-2} ones:

    lower(n) = floor((n+1)*p/k) - floor(n*p/k)
    upper(n) = ceil ((n+1)*p/k) - ceil (n*p/k)

The two mechanical words differ at the first character only; the base is the
one containing exactly p ones, the singular is the other.  This reproduces the
whole factor set, hence Psi(F_m) = sum over the k rotations of val^2 plus the
singular val^2, where val = decimal value of the 0/1 string (leading zeros
ignored).

Rotation values are advanced incrementally to keep generation O(k):

    R_{i+1} = 10*R_i - b[i]*(10^k - 1)

with b[i] the digit leaving the front, so all k rotation values cost O(k) big
integer operations rather than O(k^2).

Exact integer arithmetic throughout.
"""
import math
import os
import sys
import time

MOD = 101001001


def fib_nums(n):
    """First n Fibonacci numbers F_0..F_{n-1} (F_0=0,F_1=1)."""
    F = [0, 1]
    while len(F) < n:
        F.append(F[-1] + F[-2])
    return F


def mech_words(k, p):
    """Lower and upper mechanical words of slope p/k, length k (strings).

    Exact integer arithmetic: floor((n+1)*p/k) - floor(n*p/k).
    """
    lo = []
    up = []
    # precompute floors of (n)*p/k for n = 0..k
    # f(n) = floor(n*p/k); g(n) = ceil(n*p/k) = (n*p + k-1)//k
    fl = [0] * (k + 1)
    ce = [0] * (k + 1)
    for n in range(k + 1):
        num = n * p
        fl[n] = num // k
        ce[n] = (num + k - 1) // k
    lo = [str(fl[n + 1] - fl[n]) for n in range(k)]
    up = [str(ce[n + 1] - ce[n]) for n in range(k)]
    return "".join(lo), "".join(up)


def base_and_singular(k, p):
    """Return (base, singular): the two mechanical words, base has p ones."""
    lo, up = mech_words(k, p)
    if lo.count("1") == p:
        return lo, up
    return up, lo


def rotations_and_singular(base, singular):
    """Sum of squares of val(rotation) over all k rotations plus singular."""
    k = len(base)
    b = [int(c) for c in base]
    # P10 = 10^k - 1
    P10 = 10 ** k - 1
    R = int(base)                 # decimal value of base (leading zeros ignored by int)
    total = 0
    ten_k = 10 ** k
    for i in range(k):
        total += R * R
        # rotate left by one: front digit b[i] leaves
        R = 10 * R - b[i] * (ten_k - 1)
    total += int(singular) ** 2
    return total


def build_psi_fibonacci(mmax, fibs):
    """Psi(F_m), exact and mod, for m=3..mmax (k from 2 upward)."""
    out = []
    for m in range(3, mmax + 1):
        k = fibs[m]
        p = fibs[m - 2]           # number of ones in base
        t0 = time.time()
        base, singular = base_and_singular(k, p)
        psi = rotations_and_singular(base, singular)
        dt = time.time() - t0
        out.append((m, k, psi, psi % MOD, dt))
        print(f"m={m:3d} k=F_m={k:>12d} Psi mod={psi % MOD:>10d} "
              f"exact digits={len(str(psi))}  time={dt:.2f}s", flush=True)
    return out


def verify_against_oracle():
    """Check built Psi against code/out/psi_data_1_150.txt for Fibonacci ks."""
    data_file = os.path.join(os.path.dirname(__file__), "..", "out",
                             "psi_data_1_150.txt")
    oracle = {}
    with open(data_file) as f:
        for line in f:
            parts = line.split()
            if len(parts) == 3 and parts[0].isdigit():
                oracle[int(parts[0])] = int(parts[2])
    fibs = fib_nums(50)
    ks = [2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    print("Verification against oracle psi_data_1_150.txt")
    print("=" * 72)
    all_ok = True
    for k in ks:
        m = fibs.index(k)
        base, singular = base_and_singular(k, fibs[m - 2])
        psi = rotations_and_singular(base, singular)
        ok = (k in oracle) and (psi == oracle[k])
        all_ok = all_ok and ok
        print(f"k={k:4d} (m={m}) built Psi={'MATCH' if ok else 'MISMATCH'}  "
              f"base ones={base.count('1')} base={base[:24]}{'...' if len(base)>24 else ''}")
    print("=" * 72)
    print("ALL VERIFIED:", all_ok)
    return all_ok


if __name__ == "__main__":
    # Phase 1: verify against the oracle
    verified = verify_against_oracle()

    # Phase 2: extend Psi(F_m) exactly as far as feasible
    mmax = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    fibs = fib_nums(mmax + 2)
    print()
    print(f"Extending exact Psi(F_m) up to m={mmax}")
    print("=" * 72)
    rows = build_psi_fibonacci(mmax, fibs)
    print()
    print("Summary Psi(F_m) mod 101001001:")
    for m, k, psi, r, dt in rows:
        print(f"  m={m:3d}  k=F_m={k:>12d}  Psi mod 101001001 = {r}")
