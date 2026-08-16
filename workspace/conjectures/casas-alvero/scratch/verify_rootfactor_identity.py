import sympy as sp

x, t, y = sp.symbols('x t y')
for n in [4, 5]:
    bs = sp.symbols('b1:%d' % (n + 1))
    f = sp.prod(x - b for b in bs)
    ft = sp.expand(f.subs(x, x + t))
    ok_h = True
    for i in range(n):
        hi = sp.Poly(ft, t).nth(i)          # H_i(f), the t^i coefficient
        esym = sp.Poly(sp.expand(sp.prod((x - b) + y for b in bs)), y).nth(i)  # e_{n-i}
        ok_h &= sp.simplify(sp.expand(hi - esym)) == 0
    ok_r = True
    for i in range(1, n):
        hi = sp.Poly(ft, t).nth(i)
        res = sp.resultant(f, hi, x)
        prod = sp.prod(hi.subs(x, b) for b in bs)
        ok_r &= sp.simplify(sp.expand(res - prod)) == 0
    print("n=%d  Hasse=e_sym: %s   Res=prod: %s" % (n, ok_h, ok_r))
