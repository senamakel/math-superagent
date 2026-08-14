from fractions import Fraction as F

for path in ("code/out/fit_edges.py",):
    pass

# data
n_seq = {1:7,2:26,3:70,4:155,5:301,6:532,7:876,8:1365,9:2035,10:2926}
e_seq = {1:11,2:69,3:240,4:628,5:1375,6:2659,7:4694,8:7730,9:12053,10:17985}

def polyfit(points, deg):
    # points: list of (k, y) with k integers 1..; interpolate polynomial in k
    # use Lagrange over distinct k values
    xs = [p[0] for p in points]; ys = [F(p[1]) for p in points]
    # build coefficients via solving; we use direct Lagrange evaluation at symbolic? instead do Newton
    # Newton forward differences using equally spaced k = start.. 
    # simply use sympy-free: interpolate by building Vandermonde and Gaussian elimination
    n = len(points)
    from fractions import Fraction
    # Vandermonde matrix in variable t = k (monomial basis)
    import itertools
    def solve(M, b):
        n = len(M)
        A = [row[:] for row in M]; bb = b[:]
        for col in range(n):
            piv = col
            while piv < n and A[piv][col] == 0: piv += 1
            A[col], A[piv] = A[piv], A[col]; bb[col], bb[piv] = bb[piv], bb[col]
            pv = A[col][col]
            for j in range(col, n): A[col][j] /= pv
            bb[col] /= pv
            for r in range(n):
                if r != col and A[r][col] != 0:
                    fct = A[r][col]
                    for j in range(col, n): A[r][j] -= fct*A[col][j]
                    bb[r] -= fct*bb[col]
        return bb
    M = []
    for x in xs:
        row = []
        pw = F(1)
        for d in range(n):
            row.append(pw); pw *= x
        M.append(row)
    coeffs = solve(M, ys[:])   # coeffs of monomial x^d
    return coeffs  # lowest degree first

def evalpoly(coeffs, x):
    x = F(x); s = F(0)
    for d,c in enumerate(coeffs):
        s += c * x**d
    return s

# n(k): confirm quartic fits k=1..10
c = polyfit([(k,n_seq[k]) for k in range(1,11)], 10)
cdeg4 = polyfit([(k,n_seq[k]) for k in range(1,6)], 6)
# check if degree-4 through k=1..5 predicts 6..10 exactly (only if coeffs above deg4 are zero)
print("n(k) monomial coeffs (degree 9 fit through k=1..10):")
print("  low->high:", [str(x) for x in c])
print("  high coeffs (k^5..k^9) all zero?", all(x==0 for x in c[5:]))

print()
print("quartic fit through k=1..5, test k=6..10:")
co4 = polyfit([(k,n_seq[k]) for k in range(1,6)], 6)
for k in range(1,11):
    pred = evalpoly(co4, k)
    print(f"  n({k}) pred={pred} actual={n_seq[k]} match={pred==n_seq[k]}")

print()
print("=== e(k) quartic-window fits ===")
for lo in range(1,5):
    for hi in range(lo+3, 11):
        pts = [(k,e_seq[k]) for k in range(lo,hi+1)]
        c4 = polyfit(pts, len(pts))
        # check degree <= 4 (coeffs above degree 4 zero) and extras
        over = [x for x in c4[5:]]
        if all(x==0 for x in over):
            # test on all
            ok_all = all(evalpoly(c4[:5], k)==e_seq[k] for k in range(1,11))
            print(f"  window k={lo}..{hi}: quartic exact on k=1..10? {ok_all}  coeffs={[str(x) for x in c4[:5]]}")
        else:
            pass

print()
print("=== e(k): compare fourth differences structure ===")
# is e(k)-3/2 k^4 ... let's test if e(k) satisfies 4th-diff=36 AFTER adjusting small k
# compute quartic with 4th diff 36: 36 = 24*a4 -> a4=3/2
# fit quartic to k=4..8 (the clean tail) and predict
for lo in (3,4):
    pts=[(k,e_seq[k]) for k in range(lo,lo+5)]
    c4=polyfit(pts,len(pts))
    ok=True
    for k in range(1,11):
        if evalpoly(c4[:5],k)!=e_seq[k]: ok=False
    print(f"  quartic through k={lo}..{lo+4} exact on k=1..10? {ok} coeffs={[str(x) for x in c4[:5]]}")
    # which k fail
    fails=[k for k in range(1,11) if evalpoly(c4[:5],k)!=e_seq[k]]
    print(f"    failing k: {fails}")
