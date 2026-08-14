"""Extend the order-family test to d=41..75 and quantify the d=75 'fit'.

For a length-n sequence BM always returns order <= n/2 (here 75). Order 75 with
n=150 uses all 150 points (75 equations, 75 unknowns) and is therefore the
degenerate ceiling that fits ANY data. This script:
  (a) tests d=41..75 for consistency of a rational-coefficient recurrence over
      several primes (so we know whether any nondegenerate order fits);
  (b) for the consistent orders, reconstructs coefficients and reports whether
      they are small rationals or noise-sized.
"""
import os, random
from math import isqrt, gcd

from lib.recurrences import berlekamp_massey, verify_recurrence, rational_reconstruct

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
DATA = os.path.join(OUT_DIR, "psi_data_1_150.txt")
PRIMES = [1000003, 1000000007, 998244353, 2147483647]


def load_psi(path):
    psi = {}
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                k = int(line.split(":")[0].strip())
            except (ValueError, IndexError):
                continue
            parts = line.split(":")
            if len(parts) < 4:
                continue
            try:
                psi[k] = int(parts[-1].strip())
            except ValueError:
                continue
    return psi


def rank_mod(M, p):
    M = [list(r) for r in M]
    nrows, ncols = len(M), len(M[0]) if M else 0
    pivot_row = 0
    for col in range(ncols):
        sel = None
        for r in range(pivot_row, nrows):
            if M[r][col] % p != 0:
                sel = r
                break
        if sel is None:
            continue
        M[pivot_row], M[sel] = M[sel], M[pivot_row]
        inv = pow(M[pivot_row][col], p - 2, p)
        for c in range(col, ncols):
            M[pivot_row][c] = M[pivot_row][c] * inv % p
        for r in range(nrows):
            if r != pivot_row and M[r][col] % p != 0:
                f = M[r][col] % p
                for c in range(col, ncols):
                    M[r][c] = (M[r][c] - f * M[pivot_row][c]) % p
        pivot_row += 1
        if pivot_row == nrows:
            break
    return pivot_row


def consistent_mod(A, b, p):
    rows = [list(r) for r in A]
    aug = [rows[i] + [b[i] % p] for i in range(len(rows))]
    return rank_mod(rows, p) == rank_mod(aug, p)


def solve_mod(A, b, p, d):
    rows = [list(map(lambda x: x % p, r)) for r in A]
    bcol = [x % p for x in b]
    M = [rows[i] + [bcol[i]] for i in range(len(rows))]
    nrows, ncols = len(M), d + 1
    pivot_row = 0
    pivot_col = []
    for col in range(d):
        sel = None
        for r in range(pivot_row, nrows):
            if M[r][col] % p != 0:
                sel = r
                break
        if sel is None:
            continue
        M[pivot_row], M[sel] = M[sel], M[pivot_row]
        inv = pow(M[pivot_row][col], p - 2, p)
        for c in range(col, ncols):
            M[pivot_row][c] = M[pivot_row][c] * inv % p
        for r in range(nrows):
            if r != pivot_row and M[r][col] % p != 0:
                f = M[r][col] % p
                for c in range(col, ncols):
                    M[r][c] = (M[r][c] - f * M[pivot_row][c]) % p
        pivot_col.append(col)
        pivot_row += 1
    for r in range(nrows):
        allzero = all(M[r][c] % p == 0 for c in range(d))
        if allzero and M[r][d] % p != 0:
            return None
    sol = [0] * d
    for pi, col in enumerate(pivot_col):
        sol[col] = M[pi][d] % p
    return sol


def main():
    psi = load_psi(DATA)
    seq = [psi[k] for k in sorted(psi)]
    n = len(seq)
    print(f"Loaded {n} terms; BM order = {berlekamp_massey([x%PRIMES[1] for x in seq], PRIMES[1])[0]} (= n/2, degenerate ceiling)")

    # sanity: any length-n sequence has order <= n/2. Confirm by fitting d=n//2.
    # Check consistency for d=41..75 over all primes
    print("\nConsistency of rational-coefficient recurrence, d=41..75:")
    consistent_orders = []
    for d in range(41, 76):
        A = [[seq[k - 1 - j] for j in range(d)] for k in range(d, n)]
        b = [seq[k] for k in range(d, n)]
        inc = [p for p in PRIMES if not consistent_mod(A, b, p)]
        if not inc:
            consistent_orders.append(d)
            print(f"  d={d}: CONSISTENT over all primes")
        else:
            print(f"  d={d}: inconsistent mod {inc[:2]}...")
    print("consistent orders:", consistent_orders)

    # For each consistent order, reconstruct on largest prime and measure coefficient size
    print("\nCoefficient reconstruction for consistent orders (largest prime):")
    for d in consistent_orders:
        A = [[seq[k - 1 - j] for j in range(d)] for k in range(d, n)]
        b = [seq[k] for k in range(d, n)]
        p = PRIMES[-1]
        sol = solve_mod(A, b, p, d)
        if sol is None:
            print(f"  d={d}: singular solve mod p, skip")
            continue
        from fractions import Fraction
        max_den = 1
        recon_ok = True
        for c in sol:
            rc = rational_reconstruct(c, p)
            if rc is None:
                recon_ok = False
                break
            max_den = max(max_den, abs(rc[1]))
        # verify exactly with reconstructed fractions
        fracs = []
        allok = recon_ok
        if recon_ok:
            for c in sol:
                rc = rational_reconstruct(c, p)
                fracs.append(Fraction(*rc))
            for k in range(d, n):
                total = sum(fracs[j] * seq[k - 1 - j] for j in range(d))
                if total != seq[k]:
                    allok = False
                    break
        print(f"  d={d}: reconstruct_ok={recon_ok}, max_denominator={max_den}, exact_fit={allok}")

if __name__ == "__main__":
    main()
