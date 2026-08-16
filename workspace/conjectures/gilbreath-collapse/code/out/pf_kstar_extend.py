"""Extend the independent K*(n) verification to n=16 and emit the K* sequence."""
from collections import defaultdict
from lib.collapse import S2

def pair_counts(hbits, n, K):
    out = []
    for k in range(1, K + 1):
        nk = n - k
        for a in (0, 1):
            for b in (0, 1):
                c = 0
                for i in range(nk):
                    if ((hbits >> i) & 1) == a and ((hbits >> (i + k)) & 1) == b:
                        c += 1
                out.append(c)
    return tuple(out)

def fiber_witness(n, K, s2):
    fibers = defaultdict(list)
    for h in range(1 << n):
        fibers[pair_counts(h, n, K)].append(h)
    for hs in fibers.values():
        if len(hs) >= 2:
            base = s2[hs[0]]
            for h in hs[1:]:
                if s2[h] != base:
                    return (hs[0], h)
    return None

def main():
    kstar = {}
    for n in range(3, 17):
        s2 = {h: S2(n, [(h >> i) & 1 for i in range(n)]) for h in range(1 << n)}
        ks = None
        for K in range(1, n):
            if fiber_witness(n, K, s2) is None:
                ks = K
                break
        kstar[n] = ks
    seq = [kstar[n] for n in range(3, 17)]
    print("K*(n) for n=3..16:", seq)
    print("K* - ceil(n/2):", [kstar[n] - ((n + 1) // 2) for n in range(3, 17)])
    print("K* - floor(n/2):", [kstar[n] - (n // 2) for n in range(3, 17)])
    # slope check on the tail
    import statistics
    xs = list(range(6, 17))
    ys = [kstar[n] for n in xs]
    n_ = len(xs)
    mx = sum(xs)/n_; my = sum(ys)/n_
    slope = sum((x-mx)*(y-my) for x,y in zip(xs,ys))/sum((x-mx)**2 for x in xs)
    print(f"linear-least-squares slope of K* over n=6..16: {slope:.4f}  (n/2 => ~0.5)")

if __name__ == "__main__":
    main()
