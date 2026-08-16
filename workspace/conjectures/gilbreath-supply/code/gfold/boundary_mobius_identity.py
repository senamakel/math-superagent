#!/usr/bin/env python3
"""Test the boundary-Moebius reformulation of the SUPPLY fold.

Conjectured clean identity (to verify before adopting anything):

  h = boundary(r) over F2, i.e. h[j] = r[j+1] XOR r[j]  (r = "potential")
  fold cell:  T(n,d) = XOR_{o submask of d} h[n-1-d+o]

Claim: T(n,d) = b_d XOR b_{d-1},  where b_e = XOR_{o submask of e} r[n-1-e+o]
are the Moebius (submask-XOR) coefficients of the reversed r-window.
Equivalently wt(Phi_n h) = #{d in [2,n-1] : b_d != b_{d-1}} = variation of the
Moebius profile of r.

We brute-force all quantities with exact F2 arithmetic and report matches.
"""


def submasks(x):
    s = x
    while True:
        yield s
        if s == 0:
            break
        s = (s - 1) & x


def boundary_from_h(h):
    r = [0] * (len(h) + 1)
    r[0] = 1
    for j, b in enumerate(h):
        r[j + 1] = r[j] ^ b
    return r


def fold_cells(h, n):
    """T(n,d) for d = 0..n-1 (exact F2 submask-XOR)."""
    return [sum(h[n - 1 - d + o] for o in submasks(d)) % 2 for d in range(n)]


def mobius_r(r, n):
    """b_e = XOR_{o submask of e} r[n-1-e+o] for e = 0..n-1."""
    return [sum(r[n - 1 - e + o] for o in submasks(e)) % 2 for e in range(n)]


def check(h, n, name):
    r = boundary_from_h(h)
    T = fold_cells(h, n)
    b = mobius_r(r, n)
    # claim: T[d] == b[d] XOR b[d-1] for d >= 1 (b[-1] treated as 0)
    ok = True
    for d in range(1, n):
        lhs = T[d]
        rhs = b[d] ^ b[d - 1]
        if lhs != rhs:
            ok = False
            print(f"  [{name}] MISMATCH d={d}: T={lhs} vs b[d]^b[d-1]={rhs}")
    # also check the reverse boundary convention: T[d] == b[d]^b[d+1] ?
    ok2 = True
    for d in range(0, n - 1):
        lhs = T[d]
        rhs = b[d] ^ b[d + 1]
        if lhs != rhs:
            ok2 = False
    print(f"[{name}] n={n}  T[d]=b[d]^b[d-1]: {'OK' if ok else 'FAIL'}, "
          f"T[d]=b[d]^b[d+1]: {'OK' if ok2 else 'FAIL'}")
    return ok, ok2


def primes_upto_index(n):
    ps = []
    cand = 2
    while len(ps) < n:
        okp = True
        for p in ps:
            if p * p > cand:
                break
            if cand % p == 0:
                okp = False
                break
        if okp:
            ps.append(cand)
        cand += 1
    return ps


def prime_h(n):
    ps = primes_upto_index(n)
    return [((ps[j + 1] - ps[j]) // 2) % 2 for j in range(n - 1)]


def main():
    # small all-ones / alternating / Thue-Morse / random controls
    for n in [4, 5, 8, 13, 21]:
        h_ones = [1] * (n - 1)
        h_alt = [(j % 2) for j in range(n - 1)]
        h_tm = [(bin(j).count('1') % 2) for j in range(n - 1)]
        check(h_ones, n, "all-ones")
        check(h_alt, n, "alternating")
        check(h_tm, n, "Thue-Morse")
        # random controls
        import random
        random.seed(12345)
        for t in range(3):
            h_rnd = [random.randint(0, 1) for _ in range(n - 1)]
            check(h_rnd, n, f"random{t}")
    # real prime h for a few n
    for n in [8, 13, 21, 34]:
        check(prime_h(n), n, "prime-h")


if __name__ == "__main__":
    main()
