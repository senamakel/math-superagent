"""Verify ord_0(R_i) = n(n-i) for the weighted traceless-slice resultants.

f = x^n + sum_{j=2}^n a_j x^{n-j}  (monic, traceless a_1 = 0), weight w(a_j)=j.
R_i = Res_x(f, H_i(f)), H_i the Hasse derivative.
ord_0(R_i) = min weighted degree = exponent of t under the substitution
a_j -> t^j a_j (weighted grading equals the t-exponent).

Claim to verify:
  ord_0(R_i) = n(n-i)   for all n>=3, i in 1..n-1,
and the leading coefficient (coefficient of t^{n(n-i)}) is NONZERO,
so the order is exact, not merely >=.

Method A (direct): build the true R_i = Res_x(f, H_i) over QQ[a_2..a_n]
exactly, substitute a_j -> t^j a_j, and read off the lowest power of t.

Method B (structural root form, cheap, proves the exponent): under a_j->t^j a_j
the roots scale as beta_j -> t beta_j, and H_i(f)(x) = e_{n-i}(x-beta_1..x-beta_n).
Hence R_i(t) = prod_k H_i(F_t)(beta_k(t)) = t^{n(n-i)} * prod_k A_{i,k},
A_{i,k} = e_{n-i}((beta_k - beta_j)_{j != k}).  We verify prod_k A_{i,k} is not
identically zero as a polynomial in the beta's, so the order is exactly n(n-i).
"""
import sympy as sp

def hasse_derivative(coeffs, i):
    """Hasse derivative of f = sum_j a_j x^(n-j) (a_0=1), coeffs[i]=a_i (ascending)."""
    n = len(coeffs) - 1
    out = {}
    for j, c in enumerate(coeffs):
        deg = n - j
        if deg >= i:
            out[j] = sp.binomial(deg, i) * c
    return out

def order_in_t(poly, t):
    """Smallest exponent of t appearing in poly (as Poly in t), and its coeff."""
    P = sp.Poly(poly, t)
    if P.degree() < 0:  # zero poly -> infinite order
        return None, None
    terms = P.terms()  # list of (((exp,)), coeff)
    expm, coeff = terms[0]
    return expm[0], coeff

def method_A(n, name_map):
    x, t = sp.symbols('x t')
    a0 = sp.Integer(1)
    # ascending coeff list: a_0=1 (index n), a_1=0 (index n-1), a_2..a_n
    coeffs = [sp.Symbol('a%d' % j) if j >= 2 else (sp.Integer(1) if j == 0 else sp.Integer(0))
              for j in range(n + 1)]  # index j -> a_j
    f = sum(coeffs[j] * x ** (n - j) for j in range(n + 1))
    results = {}
    for i in range(1, n):
        hi = sum(hasse_derivative(coeffs, i)[j] * x ** (n - j - i)
                 for j in hasse_derivative(coeffs, i))
        R = sp.resultant(f, hi, x)
        Rt = R.subs({sp.Symbol('a%d' % j): sp.Symbol('a%d' % j) * t ** j
                     for j in range(2, n + 1)})
        Rt = sp.expand(Rt)
        e, c = order_in_t(Rt, t)
        results[i] = (e, c)
    return results

def method_B_nonzero(n):
    """Check prod_k e_{n-i}((beta_k-beta_j)_{j!=k}) is not identically zero,
    by evaluation at a random generic point (exact rational random)."""
    beta = [sp.symbols('b%d' % k) for k in range(n)]
    import random
    random.seed(12345 + n)
    # We evaluate at algebraically-independent-ish generic integer values to
    # test nonzero-ness of the polynomial (probabilistic but exact check).
    for i in range(1, n):
        m = n - i
        if m == 0:
            continue
        vals = {b: random.randint(1, 100) for b in beta}
        prod = sp.Integer(1)
        for k in range(n):
            others = [beta[k] - beta[j] for j in range(n) if j != k]
            if m == len(others) + 1:
                # impossible: need m <= n-1 always, m=n-i <= n-1 for i>=1
                pass
            e_val = sum(sp.prod([others[idx] for idx in sub])
                        for sub in sp.subsets(range(len(others)), m))
            prod *= sp.expand(e_val)
        pv = prod.subs(vals)
        if pv == 0:
            return False, i
    return True, None

if __name__ == '__main__':
    print("Method A (direct true resultants, exact over QQ[a_2..a_n]):")
    for n in [3, 4, 5]:
        res = method_A(n, None)
        ok = all(e == n * (n - i) for i, (e, c) in res.items()) \
             and all(c != 0 for i, (e, c) in res.items())
        print(f"  n={n}: ord_0(R_i)={ {i: e for i, (e, c) in res.items()} }, "
              f"target { {i: n*(n-i) for i in range(1, n)} }, "
              f"leading coeffs nonzero: "
              f"{ {i: (c != 0) for i, (e, c) in res.items()} }  -> {'OK' if ok else 'FAIL'}")
    print("Method B (structural root-form leading coefficient nonzero):")
    for n in [3, 4, 5, 6, 7, 8]:
        ok, badi = method_B_nonzero(n)
        msg = 'FAIL at i=%s' % badi if not ok else 'OK'
        print(f"  n={n}: prod_k A_k not identically zero -> {msg}")
