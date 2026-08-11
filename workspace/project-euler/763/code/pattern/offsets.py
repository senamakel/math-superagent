# Extract N(N,M) table and examine fixed-offset diagonals M-N = k.
# Look for pattern N(N, N+k) = poly(N) * 3^(N-1) or similar.
import collections, os

# read table
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

print("Offsets k=M-N: value N(N, N+k) divided by 3^(N-1)")
offsets = {}
for N, cnt in T.items():
    for M, v in cnt.items():
        k = M - N
        offsets.setdefault(k, []).append((N, v))

for k in sorted(offsets):
    print(f"\n-- offset k={k} --")
    for N, v in offsets[k]:
        # ratio to 3^(N-1)
        r = v / (3.0**(N-1))
        print(f"  N={N}: v={v:8d}  v/3^(N-1)={r:.6f}")
