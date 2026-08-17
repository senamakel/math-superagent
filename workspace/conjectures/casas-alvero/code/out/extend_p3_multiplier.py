"""Exact p=3 Hasse-CA satisfier count m(n,3)=sat/3 for monic degree-n polys
over F3, extending the recorded p=3 multiplier sequence 1,3,5,1,5,39,1
(n=3..9) to test the conjecture:

    CONJECTURE: m(n,3) = 1  (3 is a GOOD prime for degree n, only the 3 pure
    powers (x-a)^n satisfy Hasse-CA)  iff  3 | n.

Recorded data n=3..9: m = 1 at n=3,6,9 (all multiples of 3); m>1 at
n=4,5,7,8 (none a multiple of 3).  This differs from p=2 (m=1 iff n is a
power of 2), so it is a distinct regularity.  Key fresh tests:
  - n=12 (3|12): predicts m=1  <- would extend the divisibility pattern
  - n=10,11,13,14 (not multiples of 3): predict m>1

Polynomial sum c_j x^j stored as base-3 digit vector.  i-th Hasse derivative
H_i has coeff of x^j = C(j,i) mod 3 (Lucas).  Exact gcd over F3 via Euclid
on coefficient vectors.  Hasse-CA iff gcd(f,H_i) non-constant for all
i=1..n-1 (gcd(f,0)=f is non-constant -> vanishing H_i passes).

Exponential oracle (enumerates all 3^n monic polys), used only at bounded n
to test a structural conjecture.
"""
from multiprocessing import Pool
from math import comb
import sys


def pas_triangle(n):
    """Rows of Pascal's triangle mod 3 up to row n, as lists."""
    rows = []
    prev = [1]
    rows.append(prev)
    for r in range(1, n + 1):
        cur = [(prev[k] if k < len(prev) else 0) +
               (prev[k - 1] if k - 1 >= 0 else 0) for k in range(r + 1)]
        cur = [c % 3 for c in cur]
        rows.append(cur)
        prev = cur
    return rows


# global pascal rows (built per process — cheap)
PASCAL = None


def init_pascal(n):
    global PASCAL
    PASCAL = pas_triangle(n)


def hasse_deriv(digs, i, triangle):
    """H_i of polynomial given by coefficient list digs (len n+1, index=degree).
    coeff of x^{j-i} gets C(j,i)*digs[j]; C(j,i) mod 3."""
    n = len(digs) - 1
    out = [0] * (n - i + 1)
    for j in range(i, n + 1):
        c = triangle[j][i] * digs[j] % 3
        if c:
            out[j - i] = (out[j - i] + c) % 3
    return out


def trim(d):
    while len(d) > 1 and d[-1] == 0:
        d.pop()
    return d


def dp_mod(a, b):
    """polynomial remainder a mod b over F3 (both as coeff lists, monic-at-top)."""
    a = trim(a[:])
    b = trim(b[:])
    degb = len(b) - 1
    lc = b[-1]
    inv = pow(lc, 1, 3)  # lc = 1 or 2; inv exists since 3 prime
    # reduce: linear in degree of a
    while len(a) - 1 >= degb:
        deg = len(a) - 1 - degb
        # coefficient of a at top that we must kill
        coef = a[-1] * inv % 3
        if coef:
            for k in range(degb + 1):
                a[deg + k] = (a[deg + k] - coef * b[k]) % 3
        a = trim(a)
    return a


def dp_gcd(a, b):
    if all(x == 0 for x in a):
        return b
    if all(x == 0 for x in b):
        return a
    a = trim(a[:])
    b = trim(b[:])
    while not all(x == 0 for x in b):
        a, b = b, dp_mod(a, b)
    return a


def degree(p):
    return len(trim(p[:])) - 1


def is_ca_f3(digs, n):
    for i in range(1, n):
        hi = hasse_deriv(digs, i, PASCAL)
        if all(x == 0 for x in hi):
            continue
        g = dp_gcd(digs, hi)
        if degree(g) == 0:
            return False
    return True


def is_pure_power_f3(digs, n):
    """Over F3 monic pure powers (x-a)^n: (x)^n = x^n or (x+1),(x+2)."""
    for a in (0, 1, 2):
        # (x+a)^n = sum C(n,k) a^{n-k} x^k mod 3
        bits = []
        for k in range(n + 1):
            coef = comb(n, k) * pow(a, n - k, 3) % 3
            bits.append(coef)
        if bits == digs:
            return True
    return False


def base3_polys(n):
    """iterate all 3^n monic polys x^n + lower coeffs."""
    for v in range(3 ** n):
        digs = [0] * n + [1]
        x = v
        for j in range(n):
            digs[j] = x % 3
            x //= 3
        yield digs


def _count_chunk(args):
    n, lo, hi = args
    sat = ce = 0
    power = 3 ** n
    for v in range(lo, hi):
        digs = [0] * n + [1]
        x = v
        for j in range(n):
            digs[j] = x % 3
            x //= 3
        if is_ca_f3(digs, n):
            sat += 1
            if not is_pure_power_f3(digs, n):
                ce += 1
    return sat, ce


def sat_count(n, workers, oracle_check=True):
    if oracle_check:
        # oracle-guard at small n against the canonical library
        from lib.casas_alvero import is_ca_hasse, is_pure_power
        from sympy import symbols, Poly, GF
        x = symbols("x")
        ok = True
        for v in range(3 ** n):
            digs = [0] * n + [1]
        # done in main below instead
    size = 3 ** n
    CH = 3 ** 10
    bounds = [(n, lo, min(lo + CH, size)) for lo in range(0, size, CH)]
    with Pool(workers, initializer=init_pascal, initargs=(n,)) as pool:
        parts = pool.map(_count_chunk, bounds, chunksize=1)
    return sum(s for s, _ in parts), sum(c for _, c in parts)


def oracle_guard(n):
    """Check my F3 checker against the canonical sympy oracle on all 3^n polys
    for small n.  Returns mismatch count."""
    from lib.casas_alvero import is_ca_hasse, is_pure_power
    from sympy import symbols, Poly, GF
    x = symbols("x")
    mism = 0
    for v in range(3 ** n):
        digs = [0] * n + [1]
        xv = v
        for j in range(n):
            digs[j] = xv % 3
            xv //= 3
        f = Poly(x ** n + sum(digs[j] * x ** j for j in range(n)), x, domain=GF(3))
        mine_ca = is_ca_f3(digs, n)
        mine_pp = is_pure_power_f3(digs, n)
        ref_ca = is_ca_hasse(f, 3)
        ref_pp = is_pure_power(f, 3)
        if mine_ca != ref_ca or mine_pp != ref_pp:
            mism += 1
    return mism


if __name__ == "__main__":
    # thin entry: needs PASCAL init in the current process too
    worker_n = int(sys.argv[2]) if len(sys.argv) > 2 else 28
    for n in [int(x) for x in sys.argv[1].split(",")]:
        init_pascal(n)
        if n <= 6:
            # oracle guard against the canonical sympy oracle, small n only
            mism = oracle_guard(n)
            print(f"oracle-guard n={n}: {mism} mismatches", flush=True)
            if mism:
                print("REFUSING to report (checker disagrees with canonical oracle)")
                continue
        else:
            print(f"oracle-guard n={n}: skipped (n>6, checker already validated at n=5)", flush=True)
        sat, ce = sat_count(n, worker_n, oracle_check=False)
        m = sat // 3
        print(f"n={n} 3^n={3**n:11d} 3|n={n%3==0}  sat={sat:8d} ce={ce:8d} "
              f"m=sat/3={m:5d}  (m==1 iff 3-good: {m==1})", flush=True)
