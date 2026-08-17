"""PE1006 pattern hunt, cycle 3: three exact extensions.

(1) Right-extension recurrence, verified mod M for k = 1..400:
        Psi(k+1) = 100*Psi(k) + 100*V(R_k)^2 + 20*S1(k) + J(k)   (mod M)
    where R_k is the unique right-special length-k factor (extends both ways),
    J(k) = #{ (w, b='1') : w in F_k, w+b in F_{k+1} }, S1(k) = sum V(w) over
    those pairs.  Also checks J(k) == # length-(k+1) factors ending in '1'
    == c1(k+1) (lead-1 count, known closed form 1 + floor((k+1)/phi^2)).

(2) Pair-correlation matrix: C(i,j) = #{ w in F_k : w_i = w_j = '1' } for
    selected k (general and Fibonacci-adjacent).  Reports how far C is from
    Toeplitz: d(i,j) = C(i,j) - C(i-1,j-1) for i,j >= 2, counting nonzero
    entries and their max |d|, and whether the nonzero corrections are
    confined to a band near the boundary.

(3) Writes code/out/ext_recurrence.txt extended to k=400 (mod M values of
    V(R_k), J(k), S1(k)), and code/out/extrecur_res.txt for tool analysis.
"""
M = 101001001


def fib_prefix(L):
    a, b = '0', '01'
    while len(b) < L:
        a, b = b, b + a
    return b


def main():
    kmax = 400
    W = fib_prefix(4 * kmax + 10)
    L = len(W)
    # all factor sets: store as sets of int bitmasks (bit 0 = rightmost letter)
    # plus their decimal values mod M.
    # F[k] = set of bitmask ints
    F = {}
    for k in range(1, kmax + 2):
        F[k] = set()
        for i in range(L - k + 1):
            F[k].add(int(W[i:i + k], 2))
    # precompute pow10 mod M
    pow10 = [1] * (kmax + 2)
    for t in range(1, kmax + 2):
        pow10[t] = pow10[t - 1] * 10 % M

    def value_mod(bitmask, k):
        """Decimal value of the length-k binary string given as bitmask,
        mod M.  bit t (0 = rightmost) contributes 10^t."""
        v = 0
        while bitmask:
            lb = bitmask & -bitmask
            t = lb.bit_length() - 1
            v = (v + pow10[t]) % M
            bitmask ^= lb
        return v

    # extensions
    rows = []
    ok_recur = True
    ok_j = True
    Pk = None
    Tk = None
    for k in range(1, kmax + 1):
        Fk, Fk1 = F[k], F[k + 1]
        ext1 = []  # list of (w_bitmask, value_mod) for right extension '1'
        J = 0
        S1 = 0
        special = None
        for w in Fk:
            e0 = (w << 1) in Fk1       # w + '0'
            e1 = ((w << 1) | 1) in Fk1 # w + '1'
            ne = e0 + e1
            assert ne >= 1
            if ne == 2:
                assert special is None
                special = w
            if e1:
                J += 1
                vm = value_mod(w, k)
                S1 = (S1 + vm) % M
        assert special is not None, k
        vR = value_mod(special, k)
        # recurrence check vs Psi mod M
        if Pk is None:
            # base k=1: compute Psi(1) from F[1]
            Pk = sum(value_mod(w, 1) ** 2 for w in F[1]) % M
            Tk = sum(value_mod(w, 1) for w in F[1]) % M
        Pk1 = (100 * Pk + 100 * vR * vR + 20 * S1 + J) % M
        Pbrute = sum(value_mod(w, k + 1) ** 2 for w in Fk1) % M
        ok_recur &= (Pk1 == Pbrute)
        # J(k) == # length-(k+1) factors ending in '1' == c1(k+1)
        P1 = sum(1 for w in Fk1 if w & 1) % M
        ok_j &= (J == P1)
        rows.append((k, vR, J, P1, S1))
        Pk, Tk = Pk1, None  # T not needed further

    with open('code/out/extrecur_res.txt', 'w') as fh:
        for k, vR, J, P1, S1 in rows:
            fh.write(f"{k} {vR} {J} {S1}\n")
    # c1 check: J(k) == c1(k+1) using the file's lead-1 counts
    c1 = [int(l.split()[1]) for l in open('code/out/c1_terms.txt')]
    ok_c1 = all(rows[k - 1][2] == c1[k] for k in range(1, 400))
    print(f"right-extension recurrence (mod M), k=1..{kmax}: {ok_recur}")
    print(f"J(k) == # length-(k+1) factors ending in '1': {ok_j}")
    print(f"J(k) == c1(k+1) (lead-1 count, closed form 1+floor((k+1)/phi^2)): {ok_c1}")

    # (2) pair-correlation matrix structure for selected k
    print()
    print("== pair-correlation Toeplitz failure ==")
    for k in (6, 8, 10, 12, 13, 16, 20, 21):
        Fk = F[k]
        # C(i,j), 1-indexed positions; store as dict
        C = {}
        for w in Fk:
            ones = [t for t in range(k) if (w >> t) & 1]
            for a in ones:
                for b in ones:
                    key = (a + 1, b + 1)
                    C[key] = C.get(key, 0) + 1
        # Toeplitz failure count: d(i,j) = C(i,j)-C(i-1,j-1) for 2<=i,j<=k
        nz = 0
        maxd = 0
        maxd_where = None
        for i in range(2, k + 1):
            for j in range(2, k + 1):
                d = C.get((i, j), 0) - C.get((i - 1, j - 1), 0)
                if d:
                    nz += 1
                    if abs(d) > maxd:
                        maxd = abs(d)
                        maxd_where = (i, j, d)
        tot = (k - 1) * (k - 1)
        # distance of failing cells from the boundary: min(i-1, j-1, k-i, k-j)
        min_dist_fail = None
        for i in range(2, k + 1):
            for j in range(2, k + 1):
                d = C.get((i, j), 0) - C.get((i - 1, j - 1), 0)
                if d:
                    md = min(i - 1, j - 1, k - i, k - j)
                    min_dist_fail = md if min_dist_fail is None else min(min_dist_fail, md)
        print(f"  k={k:3d}: nonzero Toeplitz defects {nz:4d}/{tot:4d} "
              f"max|d|={maxd}{(' at ' + str(maxd_where)) if maxd_where else ''} "
              f"nearest-to-boundary defect at distance {min_dist_fail}")
    print()
    print("rows written to code/out/extrecur_res.txt (k, V(R_k) mod M, J(k), S1(k) mod M)")


if __name__ == '__main__':
    main()