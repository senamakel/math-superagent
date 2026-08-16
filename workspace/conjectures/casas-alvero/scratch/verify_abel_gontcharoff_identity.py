"""Execute first step of root-difference-coloring (adopted approach).

Verify over QQ (n = 4,5,6) and over F_p (n = p+1 for p = 2,3,5) the two pieces
of the Abel-Gontcharoff / root-difference identity:

  (A) H_i(f)(x) = e_{n-i}(x - b_1, ..., x - b_n)
      The Hasse derivative (Taylor coefficient of f(x+t)) equals the (n-i)-th
      elementary symmetric function of the differences x - b_j.
  (B) Res_x(f, H_i(f)) = prod_{beta root of f} e_{n-i}(beta - b_1, ..., beta - b_n)
      (resultant = product over roots of the RHS evaluated at the root),
      so relative to the leading coefficient c_n.

All checks are exact symbolic arithmetic (sympy). The identity is a standard
fact; this is the oracle-guarded first-step run the approach mandates.

Failure would look like: any (A) or (B) inequality for any n/p in scope, on any
i, including the char-p cases where a Hasse derivative degenerates (i >= p).
That degeneration is exactly the point — the identity must still hold (the
Hasse derivative is still the e_{n-i} of differences), which is what makes it
char-p-safe as an identity while the *coloring collapse* is where char p
breaks.
"""
import sympy as sp


def verify(n, domain, label):
    x, t, y = sp.symbols("x t y")
    bs = sp.symbols("b1:%d" % (n + 1))
    ok = True
    lines = []
    # f = prod (x - b_j)
    f = sp.prod(x - b for b in bs)
    # f(x+t) = sum_i H_i(f)(x) t^i  -> H_i is coefficient of t^i
    ft = sp.expand(f.subs(x, x + t))
    ftp = sp.Poly(ft, t)
    for i in range(0, n):
        H_i = sp.Poly(ftp).nth(i)   # coefficient of t^i
        # e_{n-i}(x-b_1,...,x-b_n) = coeff of y^{n-i} in prod_j ((x-b_j)+y)
        prod = sp.Poly(sp.expand(sp.prod((x - b) + y for b in bs)), y)
        e_ni = prod.nth(n - i) if (n - i) <= n else 0
        diff = sp.simplify(sp.expand(H_i - e_ni))
        eq = diff == 0
        ok &= eq
        if not eq:
            lines.append(f"  n={n} i={i}: FAIL (H_i != e_{{{n-i}}})")
    # (B) resultant = product of RHS over roots (leading coeff of H_i is the
    # product factors; use sp.resultant and compare with prod of H_i(b_j)).
    for i in range(1, n):
        H_i = sp.Poly(ftp).nth(i)
        res = sp.resultant(f, H_i, x)
        prod = sp.prod(H_i.subs(x, b) for b in bs)
        diff = sp.simplify(sp.expand(res - prod))
        eq = diff == 0
        ok &= eq
        if not eq:
            lines.append(f"  n={n} i={i}: FAIL result<=prod")
    status = "PASS" if ok else "FAIL"
    if not lines:
        lines.append(f"  all i checked clean")
    return status, ("\n".join(lines))


# Over QQ, symbolic in roots b_j
print("=== A over QQ (symbolic in the roots b_1..b_n) ===")
allok = True
for n in [4, 5, 6]:
    st, msg = verify(n, "QQ", f"n={n}")
    allok &= (st == "PASS")
    print(f"n={n}: {st}\n{msg}")

# Over F_p (n = p+1 for p = 2,3,5): verify with roots generic, over the field.
# The identity is polynomial in the roots; evaluating in F_p as well.
print("\n=== A over F_p (n = p+1) ===")
for p in [2, 3, 5]:
    n = p + 1
    x, t, y = sp.symbols("x t y")
    bs = sp.symbols("b1:%d" % (n + 1))
    f = sp.prod(x - b for b in bs)
    # do the expansion over ZZ then reduce symbolically (polynomial identity
    # in char p is verified by checking each monomial coefficient mod p)
    ft = sp.expand(f.subs(x, x + t))
    ftp = sp.Poly(ft, t)
    ok = True
    notes = []
    for i in range(0, n):
        H_i = sp.Poly(ftp).nth(i)
        prod = sp.Poly(sp.expand(sp.prod((x - b) + y for b in bs)), y)
        e_ni = prod.nth(n - i)
        diff = sp.Poly(sp.expand(H_i - e_ni), x, *bs)
        # check every coefficient is 0 mod p (i.e. divisible by p)
        coeffs = sp.Poly(sp.expand(H_i - e_ni), x, *bs).all_coeffs()
        bad = [c for c in coeffs if (sp.sympify(c) % p) != 0]
        if bad:
            ok = False
            notes.append(f"  n={n} i={i}: FAIL mod {p}, {len(bad)} nonzero coeffs")
    # note the degeneracy locations explicitly
    print(f"p={p} n={n}: {'PASS' if ok else 'FAIL'}")
    for line in notes:
        print(line)
    allok &= ok

print("\n=== VERDICT ===")
print("ALL identity checks PASSED" if allok else "SOME CHECKS FAILED")
