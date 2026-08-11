# Count reachable configs at each N by max level M from the feature dumps.
# Format per line: level_hist a_k | M | dx dy dz  -- M = 2nd field after '|'
import collections, glob, os

for N in range(2, 13):
    path = f"/workspace/data/level_{N}.txt"
    if not os.path.exists(path):
        continue
    cnt = collections.Counter()
    total = 0
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            # e.g. "0 1 4 4 4 5 3 | 6 | 2 3 3"
            parts = line.split('|')
            M = int(parts[1].strip())
            cnt[M] += 1
            total += 1
    print(f"N={N}: total={total}  M-distribution:")
    ms = sorted(cnt)
    print("   ", ", ".join(f"{m}:{cnt[m]}" for m in ms))
