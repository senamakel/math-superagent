# Verify column conjectures for N(N,M) = Q_k(N)*3^(2M-N-1), k=N-M, Q_k poly deg k.
import collections, os
from sympy import Rational

T = {}
for N in range(2, 13):
    path = f"/workspace/data/level_{N}.txt"
    if not os.path.exists(path):
        continue
    cnt = collections.Counter()
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split('|')
            cnt[int(parts[1].strip())] += 1
    T[N] = cnt

print("Test N(N,M) == Q_k(N)*3^(2M-N-1). We compute v*3^(N-2M+1) and check it's a polynomial in N of degree k.")
for k in [0, 1, 2, 3]:
    print(f"\n== offset k={k} (M=N-k) ==")
    data = []
    for N in sorted(T):
        v = T[N].get(N-k)
        if v is not None:
            # v = Q_k(N)*3^(2M-N-1) = Q_k(N)*3^(2(N-k)-N-1)=Q_k(N)*3^(N-2k-1)
            q = Rational(v, 3**(N-2*k-1)) if N-2*k-1 >= 0 else None
            data.append((N, v, q))
    for N, v, q in data:
        print(f"  N={N}: v={v}, Q_k={q}")
    # finite diffs of Q_k column
    qs = [q for _,_,q in data]
    diff = list(qs)
    for d in range(1, 5):
        diff = [b-a for a,b in zip(diff, diff[1:])]
        print(f"    diff order {d}: all_equal={len(set(diff))<=1}")
        if len(set(diff))<=1:
            print(f"      => Q_{k} polynomial degree {d} over these points")
            break
