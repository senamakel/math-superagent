"""Probe genuinely multi-term factored f=(x-r)^m*g, correct degrees (m+deg g=20)."""
from sympy import Poly, QQ, symbols, expand

x = symbols('x')
N = 20


def analyze(label, f):
    f = Poly(expand(f), x).set_domain(QQ)
    assert f.degree() == N and f.LC() == 1, (label, f.degree(), f.LC())
    coeffs = f.all_coeffs()
    nz = [i for i, c in enumerate(reversed(coeffs)) if c != 0]
    nz_under = [e for e in nz if e < 20]
    d = f
    share, fail = [], []
    for j in range(1, N):
        d = d.diff()
        (share if f.gcd(d).degree() > 0 else fail).append(j)
    return (label, len(share), share, nz_under)


cands = {
    # m + deg(g) = 20, g genuinely multi-term
    'x13*(x7-x-1)':       x**13 * (x**7 - x - 1),
    'x13*(x7-2x-1)':      x**13 * (x**7 - 2*x - 1),
    'x13*(x7-x2-x-1)':    x**13 * (x**7 - x**2 - x - 1),
    'x12*(x8-2x4-1)':     x**12 * (x**8 - 2*x**4 - 1),
    'x12*(x8-x4-1)':      x**12 * (x**8 - x**4 - 1),
    'x14*(x6-x3-1)':      x**14 * (x**6 - x**3 - 1),
    'x14*(x6-2x2-1)':     x**14 * (x**6 - 2*x**2 - 1),
    'x15*(x5-x2-1)':      x**15 * (x**5 - x**2 - 1),
    'x15*(x5-2x-1)':      x**15 * (x**5 - 2*x - 1),
    '(x-1)14*(x6-x3-1)':  (x - 1)**14 * (x**6 - x**3 - 1),
    '(x-1)13*(x7-x-1)':   (x - 1)**13 * (x**7 - x - 1),
    '(x-2)13*(x7-x-1)':   (x - 2)**13 * (x**7 - x - 1),
}


def main():
    for label, f in cands.items():
        try:
            s, score, share, nz = analyze(label, f)
        except Exception as e:
            print(f"{label:22s} ERR {e}")
            continue
        print(f"{label:22s} score={score:2d} shares={share}  nz=[{','.join(map(str,nz))}]")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
