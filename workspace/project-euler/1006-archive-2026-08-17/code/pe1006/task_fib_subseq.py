"""Fibonacci-indexed subsequence A_m = Psi(F_m) mod M, M = 101001001.

Extracts from code/out/psi_data_1_150.txt the values of Psi(k) at the
Fibonacci indices k = F_m for m = 1..11 (k = 1,2,3,5,8,13,21,34,55,89,144),
reduces each mod M, and then, exactly over the field F_M (M prime, established
as Task A):

  (a) tests whether A satisfies a homogeneous constant-coefficient linear
      recurrence of order L in 1..8 (rank-consistency test mod M, and a
      Berlekamp-Massey minimal-order read),
  (b) computes consecutive multiplicative ratios A_{m+1} * A_m^{-1} mod M,
  (c) tests whether an AFFINE (non-homogeneous, constant offset) recurrence
      A_m = c_0 A_{m-1} + ... + c_{L-1} A_{m-L} + d fits.

All arithmetic is exact integer mod M (M prime, so F_M is a field). No floats
for answers.
"""
import os

M = 101001001

DATA = os.path.join(os.path.dirname(__file__), "..", "out", "psi_data_1_150.txt")
DATA = os.path.normpath(os.path.join(os.getcwd(), "code/out/psi_data_1_150.txt"))

FIB_K = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]  # k = F_m, m = 1..11


def ext_gcd(a, b):
    if b == 0:
        return (a, 1, 0)
    g, x, y = ext_gcd(b, a % b)
    return (g, y, x - (a // b) * y)


def inv(a):
    g, x, _ = ext_gcd(a % M, M)
    assert g == 1
    return x % M


def gauss_rank(rows):
    """Rank of `rows` (list of lists of ints, mod M) over F_M via elimination.
    rows are already augmented by caller if wanted; rank here is over the
    matrix of coefficients (leading part). Returns rank."""
    m = len(rows)
    if m == 0:
        return 0
    n = len(rows[0])
    A = [[v % M for v in r] for r in rows]
    rank = 0
    col = 0
    piv = [None] * n
    for col in range(n):
        pivot_row = None
        for r in range(rank, m):
            if A[r][col] % M != 0:
                pivot_row = r
                break
        if pivot_row is None:
            continue
        A[rank], A[pivot_row] = A[pivot_row], A[rank]
        pv = A[rank][col]
        pv_inv = inv(pv)
        for c in range(col, n):
            A[rank][c] = (A[rank][c] * pv_inv) % M
        for r in range(m):
            if r != rank and A[r][col] % M != 0:
                f = A[r][col] % M
                for c in range(col, n):
                    A[r][c] = (A[r][c] - f * A[rank][c]) % M
        piv[col] = rank
        rank += 1
        if rank == m:
            break
    return rank


def has_recurrence(A, L, affine=False, full_rows=None):
    """Test if A satisfies order-L recurrence (optionally affine) mod M, using
    all available consecutive windows. Returns (ok, solution or None)."""
    n = len(A)
    if L >= n:
        return (True, [0] * L)  # vacuous, too few points to pin coefficients
    # rows: for each j in [L, n-1], eq: sum_i c_i A[j-1-i] (+ d) = A[j]
    rows = []
    for j in range(L, n):
        row = [A[j - 1 - i] for i in range(L)]
        if affine:
            row.append(1)
        row.append(A[j])
        rows.append(row)
    aug_rank = gauss_rank(rows)
    hon_rank = gauss_rank([r[:-1] for r in rows])
    ok = (aug_rank == hon_rank)
    if not ok:
        return (False, None)
    # free variables exist if rank < colcount; find a basic solution
    # Build reduced solution (set free vars to 0) via back-substitution.
    sol = solve_basic(rows, L + (1 if affine else 0))
    return (True, sol)


def solve_basic(rows, ncols):
    """Return one solution to the linear system `rows` (each length ncols+1,
    last entry = rhs) over F_M, setting free variables to 0."""
    A = [[v % M for v in r] for r in rows]
    m = len(A)
    col = 0
    # forward eliminate to reduced form
    rank = 0
    for col in range(ncols):
        pivot_row = None
        for r in range(rank, m):
            if A[r][col] % M != 0:
                pivot_row = r
                break
        if pivot_row is None:
            continue
        A[rank], A[pivot_row] = A[pivot_row], A[rank]
        pv = A[rank][col]
        pvi = inv(pv)
        for c in range(col, ncols + 1):
            A[rank][c] = (A[rank][c] * pvi) % M
        for r in range(m):
            if r != rank and A[r][col] % M != 0:
                f = A[r][col] % M
                for c in range(col, ncols + 1):
                    A[r][c] = (A[r][c] - f * A[rank][c]) % M
        rank += 1
        if rank == m:
            break
    # pivot columns
    pivot_cols = []
    used = set()
    for r in range(rank):
        pc = None
        for c in range(ncols):
            if A[r][c] % M != 0:
                pc = c
                break
        pivot_cols.append(pc)
        used.add(pc)
    free = [c for c in range(ncols) if c not in used]
    sol = [0] * ncols
    for fv in free:
        sol[fv] = 0
    for r in range(rank - 1, -1, -1):
        pc = pivot_cols[r]
        val = A[r][ncols]
        for c in range(pc + 1, ncols):
            if A[r][c] % M != 0:
                val = (val - A[r][c] * sol[c]) % M
        sol[pc] = val % M
    return sol


def verify(A, coefs, order, affine=False):
    """Exact mod-M check that the order-`order` recurrence (with constant
    offset `d` last in coefs when affine) reproduces every term.

    coefs has `order` coefficients (c_0..c_{order-1}); when affine it carries
    one trailing entry d. `order` is the recurrence order = number of c's.
    """
    d = coefs[-1] if affine else 0
    L = order
    for j in range(L, len(A)):
        total = (d if affine else 0)
        for i in range(L):
            total = (total + coefs[i] * A[j - 1 - i]) % M
        if total != A[j] % M:
            return (False, j)
    return (True, None)


def load_psi():
    psi = {}
    with open(DATA) as f:
        for line in f:
            line = line.strip()
            if not line or ":" not in line:
                continue
            try:
                k_str, rest = line.split(":", 1)
                k = int(k_str.strip())
            except ValueError:
                continue
            parts = rest.split()
            # the Psi value is the last integer token on the line
            val = None
            for tok in parts:
                try:
                    val = int(tok)
                except ValueError:
                    val = None
            if val is not None:
                psi[k] = val
    return psi


def main():
    psi = load_psi()
    missing = [k for k in FIB_K if k not in psi]
    if missing:
        raise SystemExit("missing Psi values for k in %r" % missing)

    A = [psi[k] % M for k in FIB_K]

    print("=" * 72)
    print("A_m = Psi(F_m) mod M,  M = 101001001,  m = 1..11 (k = F_m)")
    print("=" * 72)
    print(" m   k=F_m   Psi(k) mod M")
    for i, k in enumerate(FIB_K):
        print(" %2d   %3d    %d" % (i + 1, k, A[i]))
    print()

    given = [1, 101, 20302, 2250400, 65706380, 60501668, 67421978,
             5792364, 65085883, 67821910, 53692412]
    match = (A == given)
    print("Matches the supplied values [1,101,20302,2250400,65706380,60501668,"
          "67421978,5792364,65085883,67821910,53692412]:", match)
    if not match:
        for i, (a, g) in enumerate(zip(A, given)):
            if a != g:
                print("  mismatch at m=%d: computed %d vs given %d" % (i + 1, a, g))
    print()

    # ---------- (a) homogeneous constant-coefficient recurrence, order 1..8
    print("(a) Homogeneous constant-coefficient linear recurrence, order L=1..8, over F_M")
    print("    (exact rank-consistency of the full consecutive system)")
    for L in range(1, 9):
        if L >= len(A):
            print("   L=%d: no data (need >%d points); vacuous" % (L, L))
            continue
        ok, sol = has_recurrence(A, L, affine=False)
        if ok:
            # reconfirm by direct verification
            vok, bad = verify(A, sol, L)
            genuine = (len(A) - L) > L
            status = "FITS (verified)"
            if not vok:
                status = "fits system but FAILS verify (solver bug)"
            elif not genuine:
                status = "FITS but VACUOUS (underdetermined: eqns<=unknowns; any sequence fits)"
            else:
                status = "NO genuine fit would report FITS here"
            print("   L=%d: %s   coefs=%s" % (L, status, [int(c) for c in sol]))
        else:
            print("   L=%d: no constant-coefficient order-%d recurrence (system inconsistent)" % (L, L))
    print()

    print("   NOTE: n=%d points. A homogeneous order-L recurrence is a GENUINE" % len(A))
    print("   constraint only when the defining system is overdetermined:")
    print("   (n-L) > L  <=>  L <= %d. Orders 6,7,8 are underdetermined -> vacuous" % ((len(A) - 1) // 2))
    print()

    # Berlekamp-Massey minimal order over F_M (uses our lib implementation)
    from lib.recurrences import berlekamp_massey, verify_recurrence
    order, coefs = berlekamp_massey(A, M)
    vok, bad = verify_recurrence(A, coefs, p=M)
    print("   Berlekamp-Massey over F_M: minimal order = %d, verifies all %d points: %s"
          % (order, len(A), vok))
    print("   (recurrence: A[m] = " + " + ".join(
        "%d*A[m-%d]" % (coefs[i], i + 1) for i in range(len(coefs))) + " mod M)")
    print()

    # ---------- (b) ratios A_{m+1}/A_m mod M
    print("(b) Consecutive multiplicative ratios A_{m+1} * inv(A_m) mod M")
    print("    (an element of F_M; exact)")
    for i in range(len(A) - 1):
        if A[i] % M == 0:
            print("   m=%d->%d: A_m = 0 mod M, ratio undefined (A_m not invertible)" % (i + 1, i + 2))
        else:
            r = (A[i + 1] * inv(A[i])) % M
            print("   m=%d->%d: A_{m+1}/A_m = %d" % (i + 1, i + 2, r))
    print()

    # ---------- (c) affine (non-homogeneous) recurrence
    print("(c) Affine recurrence A_m = c_0 A_{m-1}+...+c_{L-1}A_{m-L}+d, order L=1..8")
    for L in range(1, 9):
        if L >= len(A):
            continue
        ok, sol = has_recurrence(A, L, affine=True)
        if ok:
            vok, bad = verify(A, sol, L, affine=True)
            d = sol[-1]
            genuine = (len(A) - L) > (L + 1)
            if not vok:
                status = "fits system but FAILS verify (solver bug)"
            elif not genuine:
                status = "FITS but VACUOUS (underdetermined: eqns<=unknowns)"
            else:
                status = "FITS (verified, genuine order-%d affine recurrence)" % L
            print("   L=%d: %s  coefs=%s  d=%d" % (L, status, [int(c) for c in sol[:-1]], int(d)))
        else:
            print("   L=%d: no affine order-%d recurrence (system inconsistent)" % (L, L))
    print()

    print("   NOTE: n=%d points. An affine order-L recurrence is GENUINE only when" % len(A))
    print("   (n-L) > (L+1)  <=>  L <= %d. Orders >=%d are not genuine constraints." % ((len(A) - 2) // 2, (len(A) - 1) // 2 + 1))
    print()

    # A pure geometric check: is A_{m+1} a constant multiple of A_m for all m?
    const = None
    all_const = True
    for i in range(len(A) - 1):
        if A[i] == 0:
            all_const = False
            break
        r = (A[i + 1] * inv(A[i])) % M
        if const is None:
            const = r
        elif r != const:
            all_const = False
            break
    print("   Geometric? A_{m+1}=q*A_m for a constant q mod M:", all_const)


if __name__ == "__main__":
    main()
