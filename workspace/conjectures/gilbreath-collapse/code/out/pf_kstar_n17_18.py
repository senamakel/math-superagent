"""Test the K*(n)=ceil(n/2) conjecture at its next two yet-unknown terms: n=17,18.
If K* deviates from ceil(n/2), the formula's falsifier is found."""
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
    return out

def fiber_witness(n, K, s2):
    fibers = defaultdict(list)
    for h in range(1 << n):
        fibers[tuple(pair_counts(h, n, K))].append(h)
    for hs in fibers.values():
        if len(hs) >= 2:
            base = s2[hs[0]]
            for h in hs[1:]:
                if s2[h] != base:
                    return (hs[0], h)
    return None

def main():
    for n in (17, 18):
        s2 = {h: S2(n, [(h >> i) & 1 for i in range(n)]) for h in range(1 << n)}
        target = (n + 1) // 2  # ceil(n/2)
        # check K=target-1 has a witness (so K* > target-1) and K=target has none
        w_below = fiber_witness(n, target - 1, s2)
        w_at = fiber_witness(n, target, s2)
        print(f"n={n}: ceil(n/2)={target}  witness at K={target-1}? {'YES' if w_below else 'no'}  "
              f"witness at K={target}? {'YES' if w_at else 'no'}  "
              f"=> K*(n)={('>' + str(target-1) if w_below else '?')} {('IS ' if (w_below and not w_at) else 'NOT ') + str(target)}")

if __name__ == "__main__":
    main()
