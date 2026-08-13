import sys
sys.setrecursionlimit(10000)

def good_low(k, x):
    for _ in range(k):
        d = x % 3
        if d == 2:
            return False
        x //= 3
    return True

def sieve_full(k):
    mod_n = 2 * (3 ** (k - 1))
    return [n for n in range(mod_n) if good_low(k, pow(2, n, 3 ** k))]

def lift_up_to(kmax):
    # A_1
    members = [n for n in range(2) if good_low(1, pow(2, n, 3))]
    counts = [len(members)]
    mod_old = 2  # 2*3^0
    for k in range(2, kmax + 1):
        mod_new = 2 * (3 ** (k - 1))
        nxt = []
        for n in members:
            for cand in (n, n + mod_old):
                if good_low(k, pow(2, cand, 3 ** k)):
                    nxt.append(cand)
        members = nxt
        counts.append(len(members))
        mod_old = mod_new
    return counts, members

if __name__ == "__main__":
    # verify lifting == full for small k
    for k in range(1, 9):
        mem_k, _ = lift_up_to(k)
        full = len(sieve_full(k))
        assert mem_k[-1] == full, (k, mem_k[-1], full)
    print("lifting matches full sieve for k=1..8")

    kmax = int(sys.argv[1]) if len(sys.argv) > 1 else 26
    counts, members = lift_up_to(kmax)
    for i, c in enumerate(counts, start=1):
        print(f"k={i:2d}  |A_k|={c}")
