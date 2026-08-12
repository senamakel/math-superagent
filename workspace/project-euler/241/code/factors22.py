"""Factor all 22 hemiperfect n <= 1e18 and group per k, to expose the
prime-power skeleton that the denominator-cancellation search exploits."""
from collections import defaultdict

TERMS = [2, 24, 4320, 4680, 26208, 8910720, 17428320, 20427264, 91963648,
         197064960, 8583644160, 10200236032, 21857648640, 57575890944,
         57629644800, 206166804480, 17116004505600, 1416963251404800,
         15338300494970880, 75462255348480000, 88898072401645056,
         301183421949935616]

def factorize(n):
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f

def sigmaf(f):
    s = 1
    for p, e in f.items():
        s *= (p ** (e + 1) - 1) // (p - 1)
    return s

perk = defaultdict(list)
for n in TERMS:
    f = factorize(n)
    k = (2 * sigmaf(f) // n - 1) // 2
    perk[k].append((n, f))

for k in sorted(perk):
    print(f"=== k={k}  (abundancy {2*k+1}/2) ===")
    for n, f in perk[k]:
        fac = " * ".join(f"{p}^{e}" if e > 1 else str(p) for p, e in sorted(f.items()))
        print(f"  {n:>21} = {fac}")

# per-k: which primes appear at all? (the 'skeleton')
print()
for k in sorted(perk):
    allp = set()
    for n, f in perk[k]:
        allp.update(f.keys())
    print(f"k={k}: primes used across all terms: {sorted(allp)}")