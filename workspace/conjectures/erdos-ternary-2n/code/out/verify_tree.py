import sys

def good_low(k, x):
    for _ in range(k):
        if x % 3 == 2:
            return False
        x //= 3
    return True

def main(kmax):
    # (a) order of 2 mod 3^k must be exactly 2*3^(k-1)
    for k in range(1, kmax+1):
        m = 3 ** k
        ord_ok = pow(2, 2 * 3 ** (k-1), m) == 1
        if k > 1:
            ord_ok &= pow(2, 3 ** (k-1), m) != 1  # not a divisor
            ord_ok &= pow(2, 2 * 3 ** (k-2), m) != 1
        assert ord_ok, f"order wrong at k={k}"
    print(f"order of 2 mod 3^k = 2*3^(k-1) confirmed for k=1..{kmax}")

    # (b) per-class child counts at every level == 2
    members = [n for n in range(2) if good_low(1, pow(2, n, 3))]
    mod_old = 2
    for k in range(2, kmax+1):
        child_counts = []
        nxt = []
        for c in members:
            cnt = 0
            for t in (0, 1, 2):
                cand = c + t * mod_old
                if good_low(k, pow(2, cand, 3 ** k)):
                    cnt += 1
                    nxt.append(cand)
            child_counts.append(cnt)
        bad = [i for i, cnt in enumerate(child_counts) if cnt != 2]
        if bad:
            print(f"k={k}: classes with !=2 children: {bad[:10]} count={len(bad)}")
            return
        members = nxt
        mod_old = 2 * 3 ** (k-1)
    print(f"every survivor class has exactly 2 surviving children, through k={kmax}")

    # (c) first-death level D(n) for n < 2*3^(k-1); histogram
    K = kmax - 2  # keep range modest
    if K >= 4:
        M = 2 * 3 ** (K - 1)
        hist = {}
        for n in range(M):
            d = None
            for k in range(1, K+1):
                if not good_low(k, pow(2, n, 3 ** k)):
                    d = k
                    break
            if d is None:
                d = -1  # survives every level in range (=> in {0,2,8} or others)
            hist[d] = hist.get(d, 0) + 1
        print(f"D(n) histogram for n < {M}: "+ ", ".join(f"D={d}:{c}" for d, c in sorted(hist.items())))

if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 14)