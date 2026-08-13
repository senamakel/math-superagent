import sys

def good_low(k, x):
    for _ in range(k):
        if x % 3 == 2:
            return False
        x //= 3
    return True

def main(kmax):
    # Transition k-1 -> k: lifts of class c (mod M_{k-1}) are c + j*M_{k-1}, j=0,1,2,
    # M_{k-1} = 2*3^(k-2). The NEW digit introduced at level k is position k-1 of
    # 2^lift mod 3^k. Claim (proved by LTE + unit argument): it takes the values
    # {0,1,2} exactly once over j, so exactly two lifts survive.
    members = [n for n in range(2) if good_low(1, pow(2, n, 3))]
    mod_old = 2  # M_1 = 2*3^0
    jcounts = {0: 0, 1: 0, 2: 0}   # which lift j dies at each transition
    total_transitions = 0
    for k in range(2, kmax + 1):
        p3k = 3 ** k
        bad = []
        nxt = []
        for c in members:
            digs = []
            for j in (0, 1, 2):
                cand = c + j * mod_old
                r = pow(2, cand, p3k)
                d = (r // (3 ** (k - 1))) % 3   # position k-1 digit
                digs.append(d)
                if good_low(k, r):
                    nxt.append(cand)
            if sorted(digs) != [0, 1, 2]:
                bad.append((c, digs))
            else:
                total_transitions += 1
                jcounts[digs.index(2)] += 1
        if bad:
            print(f"k={k}: {len(bad)} classes with non-cycling digits, e.g. {bad[:3]}")
            return False
        members = nxt
        mod_old = 2 * 3 ** (k - 1)
    print(f"digit at position k-1 cycles through {{0,1,2}} over the 3 lifts, for ALL classes, k=2..{kmax}")
    print(f"transitions checked: {total_transitions}; dead lift j distribution: {jcounts}")
    return True

if __name__ == "__main__":
    kmax = int(sys.argv[1]) if len(sys.argv) > 1 else 14
    ok = main(kmax)
    sys.exit(0 if ok else 1)