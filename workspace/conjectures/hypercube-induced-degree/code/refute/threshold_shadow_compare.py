"""Compare the true extremal value of |O_{<=d}(A)| against Hamming balls.

The lemma G-threshold-shadow says the extremal family for |O_{<=d}(A)| given
|A| = a is a Hamming ball in E (initial segment of simplicial/colex order).

We check this by brute force for small n: for each a, find the true max of
|O_{<=d}(A)| over all A subset E of size a, and compare against the Hamming
ball (in the FULL cube, ball of radius r centered at 0, cut down to E) of size
as close to a as possible. If some non-ball A beats every Hamming ball, the
lemma is refuted as stated.
"""
import itertools
from math import comb

def weight(x, n):
    return bin(x).count("1")

def build(n):
    E = [x for x in range(1 << n) if weight(x, n) % 2 == 0]
    O = [x for x in range(1 << n) if weight(x, n) % 2 == 1]
    neigh = {x: [x ^ (1 << i) for i in range(n)] for x in range(1 << n)}
    return E, O, neigh

def threshold_val(A_set, d, O, neigh):
    cnt = 0
    for x in O:
        k = sum(1 for u in neigh[x] if u in A_set)
        if k <= d:
            cnt += 1
    return cnt

def true_max(E, O, neigh, a, d):
    best = -1
    for subset in itertools.combinations(E, a):
        v = threshold_val(set(subset), d, O, neigh)
        if v > best:
            best = v
    return best

def hamming_ball_set(n, r, center=0):
    """Vertices within Hamming distance <= r of center (center given as int mask)."""
    return {x for x in range(1 << n) if weight(x ^ center, n) <= r}

def ball_value(n, E, O, neigh, d, r, center=0):
    A = hamming_ball_set(n, r, center) & set(E)
    return len(A), threshold_val(A, d, O, neigh)

def compare(n, d):
    E, O, neigh = build(n)
    results = []
    print(f"n={n} d={d}")
    for a in range(0, len(E) + 1):
        tmax = true_max(E, O, neigh, a, d)
        # try every ball (centered 0..2^n-1) and every radius
        ballbest = -1
        ballbest_desc = None
        for center in range(1 << n):
            for r in range(0, n + 1):
                A = hamming_ball_set(n, r, center) & set(E)
                if len(A) == a:
                    v = threshold_val(A, d, O, neigh)
                    if v > ballbest:
                        ballbest = v
                        ballbest_desc = (center, r)
        flag = ""
        if tmax > ballbest:
            flag = "  <-- TRUE MAX BEATS EVERY BALL  (REFUTES LEMMA)"
        results.append((a, tmax, ballbest, ballbest_desc, flag))
    for a, tmax, bb, desc, flag in results:
        print(f"  a={a:2d} true_max={tmax:2d} ball_best={bb:2d}{flag}")

if __name__ == "__main__":
    import sys
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    d = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    compare(n, d)
