# Check the M=N diagonal conjecture: #configs with max level M=N equals 3^(N-1).
# Tabulate (N, countMmaxN) and compare to 3^(N-1).
import collections, os

print("N | count(M=N) | 3^(N-1) | match")
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
            M = int(parts[1].strip())
            cnt[M] += 1
    got = cnt.get(N, 0)
    pred = 3**(N-1)
    print(f"{N:2d} | {got:8d} | {pred:8d} | {got==pred}")

# Also the near-diagonal M=N-1 column
print("\nN | count(M=N-1) | 3^(N-2)*? | ratio to diag")
for N in range(3, 13):
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
            M = int(parts[1].strip())
            cnt[M] += 1
    a = cnt.get(N-1, 0)
    d = cnt.get(N, 0)
    print(f"N={N}: M=N-1={a}, M=N={d}, ratio={a/d if d else float('nan'):.6f}")
