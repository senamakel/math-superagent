"""Extend survivor-tree sequences to k=24 and report exact terms.

Sequences (survivor set A_k = {r mod 2*3^(k-1): low k ternary digits of
2^r mod 3^k avoid 2}):
  size(k)     = |A_k| = 2^(k-1)          (proved)
  half(k)     = #{r in A_k : r < 2*3^(k-1)/2}
  maxk(k)     = max A_k
  deficit(k)  = period(k) - max A_k,  period = 2*3^(k-1)
  frac(k)     = half(k)/2^(k-1)           (share below halfway)
Exact modular survivor lift, never materialises 2^n.
"""
def survivor_sets(K):
    sets = {1: {0}}
    A = {0}
    cur = 1
    while cur < K:
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
        sets[cur] = A
    return sets

K = 24
sets = survivor_sets(K)

size = [len(sets[k]) for k in range(1, K+1)]
half = [sum(1 for r in sets[k] if r < 2*3**(k-1)//2) for k in range(1, K+1)]
maxk = [max(sets[k]) for k in range(1, K+1)]
deficit = [2*3**(k-1) - max(sets[k]) for k in range(1, K+1)]
frac  = [half[k-1] / size[k-1] for k in range(1, K+1)]

print("size      :", size)
print("half      :", half[1:])          # k=2..24
print("maxk      :", maxk)
print("deficit   :", deficit)
print("half-2^(k-2) k=2..24:", [half[k-1]-2**(k-2) for k in range(2,K+1)])
print("frac k=2..24     :", [round(f,4) for f in frac[1:]])
# is maxk ever the global max of the period's even tail?
print("deficit == 12 count:", sum(1 for d in deficit if d==12))
print("deficit distinct values:", sorted(set(deficit)))
