"""Fresh sequence data for the pattern tools on the live (×2 transducer) route.

Produces, exactly:
  (a) survivor sets A_k (reproduce the run's numbers) by survivor lifting,
  (b) the carry-count sequence c(n): number of base-3 carries when doubling
      the ternary string of 2^n to obtain that of 2^(n+1),
  (c) c1,c2,c0 digit counts, for OEIS/recurrence probing in a later step.
Writes a single token stream to stdout.
"""

def to_base3_digits(m):
    if m == 0:
        return [0]
    d = []
    while m:
        d.append(m % 3)
        m //= 3
    return d

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

print("=== survivor sets A_k (compressed) ===")
for k in range(1, 9):
    S = survivors(k)
    print(f"k={k} |A|={len(S)} first={S[:8]} last={S[-3:]}")

print()
print("=== carry-count c(n) for n=0..120 ===")
car = []
for n in range(0, 121):
    digs = to_base3_digits(2 ** n)
    carry_in = 0
    cnt = 0
    for i in range(len(digs)):
        s = 2 * digs[i] + carry_in
        carry_in = s // 3
        if carry_in >= 1:
            cnt += 1
    # final carry may extend length
    if carry_in >= 1:
        cnt += 1  # the top carry-out (append) also counts as a carry event
    car.append(cnt)
print(car)

print()
print("=== c1,c2,c0 digit counts n=0..120 ===")
c1, c2, c0 = [], [], []
for n in range(0, 121):
    d = to_base3_digits(2 ** n)
    c1.append(sum(1 for x in d if x == 1))
    c2.append(sum(1 for x in d if x == 2))
    c0.append(sum(1 for x in d if x == 0))
print("c1:", c1)
print("c2:", c2)
print("c0:", c0)

print()
print("=== check c1 even for n=1..500 ===  ", end="")
ok = all(c1n % 2 == 0 for n, c1n in enumerate(c1) if n >= 1)
# extend a bit
for n in range(len(c1), 501):
    d = to_base3_digits(2 ** n)
    if sum(1 for x in d if x == 1) % 2:
        ok = False
print(ok)
