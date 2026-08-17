"""Analyze state sequences for recurrences and structure.

State file psi_state_1_200.txt has: k, S_mod, N1, N0, P1_mod, vR_mod.
We look for:
  1. A closed constant-order vector/linear recurrence among the states.
  2. The N1 structure (its diffs).
  3. Whether A(i,j) (pairwise position correlation) is Toeplitz.
"""
import os, json
HERE = os.path.dirname(os.path.abspath(__file__))
PARENT = os.path.dirname(HERE)

def load_state():
    data = {}
    with open(os.path.join(HERE, "psi_state_1_200.txt")) as f:
        f.readline()
        for line in f:
            p = line.strip().split(",")
            k = int(p[0])
            data[k] = dict(S_mod=int(p[1]), N1=int(p[2]), N0=int(p[3]),
                           P1_mod=int(p[4]), vR_mod=int(p[5]))
    return data

def main():
    st = load_state()
    ks = sorted(st)
    print("N1 diffs (k->k+1), up to k=199:")
    diffs = []
    for k in ks[:-1]:
        diffs.append(st[k+1]["N1"] - st[k]["N1"])
    print("".join("1" if d else "." for d in diffs))
    print("count of +1s:", sum(diffs), "out of", len(diffs))
    # density
    print("density:", sum(diffs)/len(diffs))
    # where +1, gaps
    positions = [i+1 for i,d in enumerate(diffs) if d]
    gaps = [positions[i+1]-positions[i] for i in range(len(positions)-1)]
    from collections import Counter
    print("positions:", positions[:40])
    print("gaps:", gaps[:40], Counter(gaps))

if __name__ == "__main__":
    main()
