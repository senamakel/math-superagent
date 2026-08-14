"""Search for a low-order constant-coefficient linear recurrence for Psi(k)
that reproduces all 150 exact terms.

BM on 150 points saturates at order 75 = n/2, the degenerate ceiling. This
script instead tests, for each order d in 1..D_MAX, whether RATIONAL
coefficients c_0..c_{d-1} exist with
    a[k] = c_0 a[k-1] + ... + c_{d-1} a[k-d]   (k = d..149, 0-indexed)
holding EXACTLY for all 150 terms. Consistency is decided by rank over several
large primes (consistent over Q => consistent mod p for all but finitely many p),
and any candidate is reconstructed over Q and verified on the exact integers.
"""
import os

from lib.recurrences import berlekamp_massey, verify_recurrence, rational_reconstruct

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
DATA = os.path.join(OUT_DIR, "psi_data_1_150.txt")

PRIMES = [1000003, 1000000007, 998244353, 1000003]
PRIMES = [1000003, 1000000007, 998244353, 2147483647]

D_MAX = 40


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
                val = int(parts[-1].strip())
            except ValueError:
                continue
            psi[k] = val
    return psi


def mat_rank_mod(A, b, p):
    """Rank of A and of augmented [A|b] mod p by Gaussian elimination."""
    rows = [list(map(lambda x: x % p, r)) for r in A]
    bcol = [x % p for x in b]
    aug = [rows[i] + [bcol[i]] for i in range(len(rows))]
    # rank of A
    rA = rank_mod(rows, p)
    rAug = rank_mod(aug, p)
    return rA, rAug


def rank_mod(M, p):
    M = [list(r) for r in M]
    if not M:
        return 0
    nrows = len(M)
    ncols = len(M[0])
    pivot_row = 0
    for col in range(ncols):
        # find pivot
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
                factor = M[r][col] % p
                for c in range(col, ncols):
                    M[r][c] = (M[r][c] - factor * M[pivot_row][c]) % p
        pivot_row += 1
        if pivot_row == nrows:
            break
    return pivot_row


def consistent_mod(A, b, p):
    rA, rAug = mat_rank_mod(A, b, p)
    return rA == rAug, rA, rAug


def solve_mod(A, b, p, d):
    """Solve A x = b mod p (square-ish), return one solution or None if singular
    inconsistent. Uses the reduced row echelon of the augmented matrix, choosing
    a particular solution (free vars = 0)."""
    rows = [list(map(lambda x: x % p, r)) for r in A]
    bcol = [x % p for x in b]
    aug = [rows[i] + [bcol[i]] for i in range(len(rows))]
    M = [list(r) for r in aug]
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
                factor = M[r][col] % p
                for c in range(col, ncols):
                    M[r][c] = (M[r][c] - factor * M[pivot_row][c]) % p
        pivot_col.append(col)
        pivot_row += 1
    # check inconsistent rows: all coefficients 0 but b != 0
    for r in range(nrows):
        allzero = all(M[r][c] % p == 0 for c in range(d))
        if allzero and M[r][d] % p != 0:
            return None  # inconsistent
    # particular solution: free vars = 0
    sol = [0] * d
    for pi, col in enumerate(pivot_col):
        sol[col] = M[pi][d] % p
    return sol


def main():
    psi = load_psi(DATA)
    seq = [psi[k] for k in sorted(psi)]
    n = len(seq)
    print(f"Loaded {n} terms.")

    # --- BM reference ---
    print("\nBM orders:")
    for p in PRIMES[:3]:
        L, C = berlekamp_massey([x % p for x in seq], p)
        print(f"  prime {p}: order {L}")

    # --- For each order d, test consistency over all primes ---
    print(f"\nOrder search d=1..{D_MAX}: existence of rational-coefficient recurrence")
    inc_primes = {}  # d -> [primes where inconsistent]
    cons_primes = {}
    for d in range(1, D_MAX + 1):
        # build A, b: rows k=d..n-1 (0-indexed), A[k-d] = [a_{k-1},...,a_{k-d}], b=a_k
        A = []
        b = []
        for k in range(d, n):
            A.append([seq[k - 1 - j] for j in range(d)])
            b.append(seq[k])
        inc = []
        cons = []
        for p in PRIMES:
            ok, rA, rAug = consistent_mod(A, b, p)
            if ok:
                cons.append(p)
            else:
                inc.append((p, rA, rAug))
        if inc:
            print(f"  d={d}: inconsistent mod {[ (p, 'rankA',rA,'rankAug',rAug) for (p,rA,rAug) in inc]}")
            inc_primes[d] = inc
        else:
            print(f"  d={d}: CONSISTENT mod {cons}")
            cons_primes[d] = cons

    # --- For consistent orders, reconstruct and verify exactly ---
    for d in cons_primes:
        A = []
        b = []
        for k in range(d, n):
            A.append([seq[k - 1 - j] for j in range(d)])
            b.append(seq[k])
        # reconstruct rational coefficients using the largest prime
        p = PRIMES[-1]
        sol = solve_mod(A, b, p, d)
        if sol is None:
            print(f"  d={d}: singular/inconsistent solve on prime {p}, skipping")
            continue
        from fractions import Fraction
        coeffs_frac = []
        all_recon = True
        for c in sol:
            rc = rational_reconstruct(c, p)
            if rc is None:
                all_recon = False
                break
            coeffs_frac.append(Fraction(*rc))
        if not all_recon:
            print(f"  d={d}: coefficients not reconstructible as small rationals over p={p}; verifying via cross-prime only not exact")
            continue
        # verify exactly
        n_frac = [Fraction(x, 1) for x in seq]
        ok = True
        first_bad = None
        for k in range(d, n):
            total = sum(coeffs_frac[j] * n_frac[k - 1 - j] for j in range(d))
            if total != n_frac[k]:
                ok = False
                first_bad = k
                break
        print(f"  d={d}: exact verification of all {n-d} tail terms: {ok} (first_bad={first_bad})")
        if ok:
            print(f"  >>> FOUND exact rational recurrence of order {d}:")
            for j, c in enumerate(coeffs_frac):
                print(f"      c_{j} = {c}")

    # --- Report overall finding ---
    print("\n=== SUMMARY ===")
    print(f"BM order on 150 terms: 75 (== n/2, the degenerate ceiling for a length-n sequence).")
    if cons_primes:
        print(f"Orders d with a consistent rational-coefficient system over all primes: {sorted(cons_primes)}")
    else:
        print(f"No order d in 1..{D_MAX} gives a consistent system over all tested primes.")


if __name__ == "__main__":
    main()
