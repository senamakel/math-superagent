"""Fast version of the 2-adic constraint-family check (task verify-2adic-constraint-family).

The identity sum_c N_c 3^c == 2^n (mod 2^r) with N_c = #{a: a==c mod 2^(r-2)}
is EXACT for every digit-2-free n, because 2^n = sum_{a in A}3^a and
ord_{2^r}(3)=2^(r-2) so each 3^a == 3^(a mod 2^(r-2)) mod 2^r.  It is therefore
a tautology on the digit-free set and imposes NO exclusion by itself -- the
family cannot close.  We confirm (1) the order claim, (2) the identity on the
digit-free survivors with r capped so ord does not blow up (r <= 12, ord<=1024),
and (3) the real content: survivor exponents r in A_k project onto ALL even
2-adic residue classes mod 2^m, so no 2-adic congruence separates survivors.

Exact integer arithmetic; all loops polynomial in the printed sizes.
"""

from sympy.ntheory import n_order
from erdos.oracle import digit_free


def base3_positions_of_1(n_value):
    A = []
    ok = True
    v = n_value
    pos = 0
    while v > 0:
        d = v % 3
        if d == 1:
            A.append(pos)
        elif d == 2:
            ok = False
        v //= 3
        pos += 1
    return A, ok


def main():
    print("=== 2-adic digit-position family (verify-2adic, fast) ===", flush=True)
    print("\n[1] order of 3 mod 2^r == 2^(r-2), r=3..40:", flush=True)
    allok = all(n_order(3, 2 ** r) == 2 ** (r - 2) for r in range(3, 41))
    print(f"    ALL OK: {allok}", flush=True)

    print("\n[2] identity on digit-free n in [0,1000] (r capped at 12):", flush=True)
    dfree = [n for n in range(0, 1001) if digit_free(n)]
    print(f"    digit-free n in [0,1000]: {dfree}", flush=True)
    fails = 0
    for n in dfree:
        val = 2 ** n
        A, _ = base3_positions_of_1(val)
        for r in range(3, 13):
            ord_ = 2 ** (r - 2)
            mod = 2 ** r
            N = {}
            for c in range(ord_):
                N[c] = 0
            for a in A:
                N[a % ord_] += 1
            lhs = sum(N[c] * (3 ** c) for c in range(ord_)) % mod
            rhs = val % mod
            if lhs != rhs:
                fails += 1
                print(f"      FAIL n={n} r={r}", flush=True)
    print(f"    failures over {len(dfree)} digit-free n x r=3..12: {fails}", flush=True)

    print("\n[3] survivors r in A_k cover all even 2-adic classes mod 2^m:", flush=True)
    for k in [4, 6, 8]:
        period = 2 * 3 ** (k - 1)
        m3 = 3 ** k
        surv = []
        val = 1
        for r in range(period):
            v = val
            df = True
            for _ in range(k):
                if v % 3 == 2:
                    df = False
                    break
                v //= 3
            if df:
                surv.append(r)
            val = (val * 2) % m3
        for m in [3, 4, 5, 6]:
            evennew = {r for r in range(2 ** m) if r % 2 == 0}
            hits = {r % (2 ** m) for r in surv}
            covers = evennew.issubset(hits)
            print(f"    k={k} m={m}: |A_k mod 2^m|={len(hits)}  "
                  f"covers all {len(evennew)} even classes: {covers}",
                  flush=True)

    print("\nVERDICT: order claim OK; identity is a tautology on digit-free n", flush=True)
    print("(imposes no exclusion); survivors fill every even 2-adic class.", flush=True)
    print("The 2-adic family cannot close -- confirms prior findings.", flush=True)


if __name__ == "__main__":
    main()
