#!/usr/bin/env python3
"""End-of-erosion-run regeneration check over the depth-1000 record.

For each maximal pure-erosion run (consecutive b(k+1) == b(k)-1), the last
erosion step k -> k+1 is followed by a regeneration iff the erosion run is
followed by a regeneration.  Data (b) from blocks_depth1000.json (exact).

Also computes, over the live regime k=1..161 (intruder exists), the run
lengths distribution and the count of runs directly followed by a
regeneration event, to confirm "every genuine erosion run ends in a
regeneration" (est. from regeneration_data.md).
"""
import json


def main():
    rec = json.load(open("code/out/blocks_depth1000.json"))
    b = rec["b"]
    D = len(b)
    # 0-based diffs[i] = b[i+1] - b[i]
    diffs = [b[i + 1] - b[i] for i in range(D - 1)]

    # maximal erosion runs: start index i (transition k=i), length L
    runs = []
    i = 0
    while i < D - 1:
        if diffs[i] == -1:
            j = i
            while j < D - 1 and diffs[j] == -1:
                j += 1
            runs.append((i, j - i))   # transitions i..j-1 erosion
            i = j
        else:
            i += 1

    live = [(s, L) for (s, L) in runs if s + L < 161 + 1]  # fully inside k=1..161
    # A run of erosion transitions k_start..k_end corresponds to rows
    # k_start..k_end+1; it is followed by a regeneration if
    # diffs[k_end+1] >= 0 exists.
    followed_by_regen = []
    not_followed = []
    for (s, L) in live:
        e = s + L - 1
        if e + 1 < D - 1 and diffs[e + 1] >= 0:
            followed_by_regen.append((s + 1, L))  # 1-based start row
        else:
            not_followed.append((s + 1, L))
    print(f"live-regime erosion runs (k=1..161): {len(live)}")
    print(f"  directly followed by a regeneration: {len(followed_by_regen)}")
    print(f"  not: {len(not_followed)}")
    if not_followed:
        print("  first not-followed:", not_followed[:5])
    print("  length list:", sorted((L for _, L in live), reverse=True))

    # same for every erosion run in the entire record (tail included)
    all_runs = len(runs)
    tail_838 = [r for r in runs if r[1] >= 100]
    print(f"all erosion runs in record: {all_runs}; tail runs (len>=100): {tail_838}")


if __name__ == "__main__":
    main()