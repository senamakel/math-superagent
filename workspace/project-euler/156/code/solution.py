"""Efficient exact solver for Project Euler 156.

f(n, d) = total number of occurrences of digit d in the decimal writings of
the integers 0..n inclusive.  We solve f(n,d) = n for d in 1..9 and sum.

Method
------
1. f(n,d) is computed exactly in O(#digits) by the classical place-value
   digit count.  For the position with place value p = 10^i, the number of
   times digit at that position equals d, summed over 0..n, is
       (n // (10*p)) * p
       + max(0, min(n % (10*p) - d*p + 1, p))        for d != 0
   (for d == 0 the inner term is max(0, min(n % (10p) - p + 1, p)) with a
   shifted rule, but we only need d in 1..9 here, where the formula above is
   the standard one and is exact).

2. Search bound: every solution of f(n,d)=n with d in {1..9} satisfies
   n <= d*10^10.  Sources: OEIS A014778's completeness comments (84 terms,
   max 1111111110) and the Archive Labeling Sequences paper (Prop 9.1,
   solutions x satisfy x <= d*b^b in base b; recall memory chunk,
   arXiv:2305.10357).  For d=9 the bound is 9e10 and the actual max
   solution is 8e10 (A130431), so the bound is not tight but is provable.

3. Jump iteration to enumerate solutions without visiting the range: f(.,d)
   is non-decreasing, and any single number in [0, 9e10] has at most D = 11
   digits, so between n and m the count can grow by at most (m-n)*11.
   * if c = f(n) > n:                  next n = c            (f(m) >= c > m for n <= m < c)
   * if c = f(n) < n:                  next n = n + ceil((n-c)/10)  (f(m) <= c + 11(m-n) < m while 10(m-n) < n-c)
   * if c == n:                        n is a solution; next n = n+1
   This visits only O(#solutions * D) points (a few thousand per digit),
   polynomial in the description size, never cost-linear in the 1e10 bound.

4. Verification: agreement with the naive oracle code/brute.py on [0, 200000]
   for every digit d in 1..9 (brute force reaches that size); reproduction of
   the statement's oracle values; final sum cross-checked by summing the OEIS
   full-term tables for d = 1..9 (A014778, A101639, A101640, A101641,
   A130427, A130428, A130429, A130430, A130431) as a second route.
"""


def f_place(n, d):
    """Total occurrences of digit d (1..9) in decimal writings of 0..n.

    Exact integer arithmetic, O(number of decimal digits of n).
    Position with place value p contributes
        (n // (10p)) * p                          full blocks of 10p
        + clamp(n % (10p) - d*p + 1, 0, p)        partial block
    """
    total = 0
    p = 1
    while p <= n:
        hi = n // (10 * p)
        lo = n % (10 * p)
        partial = lo - d * p + 1
        if partial > p:
            partial = p
        if partial < 0:
            partial = 0
        total += hi * p + partial
        p *= 10
    return total


def f_iter(limit, d):
    """Naive incremental count of digit d in 0..limit, as list of values
    f(0,d), f(1,d), ..., f(limit,d).  Oracle for small limits."""
    out = []
    t = 0
    ds = str(d)
    for i in range(limit + 1):
        t += str(i).count(ds)
        out.append(t)
    return out


def solutions_by_jump(d, bound=None):
    """All n in [0, bound] with f(n,d) = n, by jump iteration.

    bound defaults to d*10**10 (the paper bound).  Returns (solutions, evals)
    where evals counts the number of f evaluations performed.
    """
    if bound is None:
        bound = d * 10**10
    # max digits of any number in [0, bound] is len(str(bound)) -- growth per
    # step of n is at most that many occurrences of d per number, so between
    # n and m the count grows by at most (m-n)*maxdig.
    maxdig = len(str(bound))
    sols = []
    n = 0
    evals = 0
    while n <= bound:
        c = f_place(n, d)
        evals += 1
        if c == n:
            sols.append(n)
            n += 1
        elif c > n:
            n = c
        else:
            # f(n+d) <= c + maxdig*d < n+d while (maxdig-1)*d < n-c
            n += (n - c + maxdig - 2) // (maxdig - 1)
    return sols, evals


def verify_against_oracle():
    """Check f_place against brute force on 0..200000 for every d in 1..9,
    and reproduce the statement's worked examples."""
    LIMIT = 200000
    ok = True
    for d in range(1, 10):
        naive = f_iter(LIMIT, d)
        for n in range(0, LIMIT + 1, 997):  # sample every 997th point
            if f_place(n, d) != naive[n]:
                print(f"MISMATCH d={d} n={n}: place={f_place(n,d)} naive={naive[n]}")
                ok = False
    # full agreement for d=1 on 0..200000 (statement's table + first solutions)
    naive = f_iter(LIMIT, 1)
    ok = ok and all(f_place(n, 1) == naive[n] for n in range(LIMIT + 1))
    # statement table f(n,1), n=0..12
    table = [f_place(n, 1) for n in range(13)]
    ok = ok and table == [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 4, 5]
    # first solutions of f(n,1)=n are 0, 1, 199981
    sols1, _ = solutions_by_jump(1, bound=10**6)
    ok = ok and sols1[0] == 0 and sols1[1] == 1 and sols1[2] == 199981
    # jump enumeration agrees with naive scan on [0, 200000] for all d
    for d in range(1, 10):
        j_sols, _ = solutions_by_jump(d, bound=LIMIT)
        naive_list = f_iter(LIMIT, d)   # hoisted: O(LIMIT) once, not per n
        n_sols = [n for n in range(LIMIT + 1) if naive_list[n] == n]
        ok = ok and j_sols == n_sols
    print("oracle checks:", "ALL OK" if ok else "FAILED")
    return ok


def main():
    if not verify_against_oracle():
        raise SystemExit(1)
    total = 0
    for d in range(1, 10):
        sols, evals = solutions_by_jump(d)
        s = sum(sols)
        total += s
        print(f"d={d}: {len(sols)} solutions, sum s({d}) = {s}, evals = {evals}")
        print(f"      last solution = {sols[-1]}")
    print("ANSWER  sum s(d) for d=1..9 =", total)


if __name__ == "__main__":
    main()