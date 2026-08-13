import sys

def good_low(k, x):
    for _ in range(k):
        d = x % 3
        if d == 2:
            return False
        x //= 3
    return True

def lift_up_to(kmax, return_sets=False):
    members = [n for n in range(2) if good_low(1, pow(2, n, 3))]
    sets = [sorted(members)]
    counts = [len(members)]
    mod_old = 2
    for k in range(2, kmax + 1):
        nxt = []
        for n in members:
            for cand in (n, n + mod_old, n + 2 * mod_old):
                if good_low(k, pow(2, cand, 3 ** k)):
                    nxt.append(cand)
        members = nxt
        counts.append(len(members))
        sets.append(sorted(members))
        mod_old = 2 * (3 ** (k - 1))
    if return_sets:
        return counts, sets
    return counts, members

if __name__ == "__main__":
    kmax = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    counts, sets = lift_up_to(kmax, return_sets=True)
    for i, c in enumerate(counts, start=1):
        print(f"k={i:2d}  |A_k|={c:8d}  A_k={sets[i-1] if i<=8 else ''}")
