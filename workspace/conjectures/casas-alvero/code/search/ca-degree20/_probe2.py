"""Probe genuinely multi-term factored f=(x-r)^m*g and evens, avoiding binomials."""
from sympy import Poly, QQ, symbols, factor, expand

x = symbols('x')
N = 20


def analyze(label, f):
    f = Poly(expand(f), x).set_domain(QQ)
    assert f.degree() == N and f.LC() == 1
    coeffs = f.all_coeffs()
    nz = [i for i, c in enumerate(reversed(coeffs)) if c != 0]
    nz_under = [e for e in nz if e < 20]
    d = f
    share, fail = [], []
    for j in range(1, N):
        d = d.diff()
        (share if f.gcd(d).degree() > 0 else fail).append(j)
    return (label, len(share), share, fail, nz_under)


cands = {
    # factored f = (x-r)^m g with g genuinely multi-term (NOT x^k - c)
    'fc_x13_g(x3-x-1)':      x**13 * (x**3 - x - 1),
    'fc_x13_g(x3-2x-1)':     x**13 * (x**3 - 2*x - 1),
    'fc_x13_g(x4-x3-x2-x-1)': x**13 * (x**4 - x**3 - x**2 - x - 1),
    'fc_x12_g(x4+2x3+3x2+4x+5)': x**12 * (x**4 + 2*x**3 + 3*x**2 + 4*x + 5),
    'fc_x14_g(x2-3x+1)':     x**14 * (x**2 - 3*x + 1),
    'fc_x15_g(x2-x-1)':      x**15 * (x**2 - x - 1),
    'fc_x10_g(x5-x4-x3-x2-x-1)': x**10 * (x**5 - x**4 - x**3 - x**2 - x - 1),
    # shifted versions (root not at 0)
    'fc_r1^14_g(x2-3x+1)':   (x - 1)**14 * (x**2 - 3*x + 1),
    'fc_r1^13_g(x3-x-1)':    (x - 1)**13 * (x**3 - x - 1),
    # even-symmetric multi-term (not a pure power at 0)
    'even_x12(x2-1)^4':      x**12 * (x**2 - 1)**4,
    'even_x10(x^2-1)(x^2-4)^4': x**10 * (x**2 - 1) * (x**2 - 4)**4,
    # palindromic / self-reciprocal degree 20
    'pal_recip_20':          x**20 + x**19 + x**18 + x**17 + x**16 + x**15 + x**14
                             + x**13 + x**12 + x**11 + x**10 + x**9 + x**8 + x**7
                             + x**6 + x**5 + x**4 + x**3 + x**2 + x + 1,  # = (x^21-1)/(x-1)? deg 20 all coeff 1
}


def main():
    rows = []
    for label, f in cands.items():
        try:
            rows.append(analyze(label, f))
        except Exception as e:
            rows.append((label, 'ERR', str(e), None, None))
    for label, score, share, fail, nz in rows:
        if score == 'ERR':
            print(f"{label:28s} ERR {fail}")
            continue
        nzstr = ",".join(map(str, nz))
        print(f"{label:28s} score={score:2d} shares={share}  nz_under20=[{nzstr}]")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
