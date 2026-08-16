"""Extend survivor maxima and verify the max = period-12 hypothesis."""

def survivors(k):
    A = {0}
    cur = 1
    while cur < k:
        L = 2 * 3 ** (cur - 1)
        next_mod = 3 ** (cur + 1)
        g = pow(2, L, next_mod)
        p3k = 3 ** cur
        Anext = set()
        for r in A:
            base = pow(2, r, next_mod)
            gp = 1
            for j in range(3):
                v = (base * gp) % next_mod
                d = (v // p3k) % 3
                if d in (0, 1):
                    Anext.add(r + j * L)
                gp = gp * g % next_mod
        A = Anext
        cur += 1
    return sorted(A)

print("k period            max            period-max  (period-max==12?)")
for k in range(3, 18):
    S = survivors(k)
    period = 2 * 3 ** (k - 1)
    mx = max(S)
    print(f"{k:2d} {period:8d}  {mx:8d}  {period-mx:8d}   {period-mx==12}")
