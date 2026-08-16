"""Extend the run's computed data for pattern analysis.

(a) c2 parity pattern over a large range (c1 even was proved; is there any
    exact statement about c2 or c0 parity?).
(b) Survivor exponent sets A_k to larger k, dumped as residues, with
    structural statistics: max survivor, whether witnesses 0,2,8 survive,
    closure structure, the multiset of low-k digit patterns.
(c) Check the digit-free n set in a reported range reproduces {0,2,8}.
"""

def base3_digits_lsb(m):
    d = []
    while m > 0:
        d.append(m % 3)
        m //= 3
    return d

# (a) parity patterns of c0, c1, c2 for n in [1, N]
def parity_data(N):
    c1odd = []
    c2odd = []
    c0odd = []
    for n in range(1, N + 1):
        d = base3_digits_lsb(2 ** n)
        c0 = sum(1 for x in d if x == 0)
        c1 = sum(1 for x in d if x == 1)
        c2 = sum(1 for x in d if x == 2)
        if c0 % 2: c0odd.append(n)
        if c1 % 2: c1odd.append(n)
        if c2 % 2: c2odd.append(n)
    return c0odd, c1odd, c2odd

N = 400
c0odd, c1odd, c2odd = parity_data(N)
print("c0 odd at n:", c0odd[:40], "count:", len(c0odd))
print("c1 odd at n:", c1odd[:10], "count:", len(c1odd), "(proved empty)")
print("c2 odd at n count:", len(c2odd), "first:", c2odd[:60])

# (b) survivors to k=12 using exact survivor lifting
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

print()
for k in range(1, 13):
    S = survivors(k)
    period = 2 * len(S)
    wits = [None if 0 not in S else 0]
    # witnesses 0,2,8 present?
    present = [x for x in (0, 2, 8) if x % period in S]
    print(f"k={k}: |A_k|={len(S)} max={max(S)} witnesses-present={present}")
