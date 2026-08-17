"""Probe closed forms for the circular-interval starts s(i) and lengths N(i).

Prior data suggests s(i) might be an arithmetic progression mod n and N(i)
takes values in {m, m+1} with m=floor((k+1)*a).  Test:
  (A) is s(i+1)-s(i) constant mod n?
  (B) is s(i) = round(i*step) or floor(i*step+s0) for some step?
  (C) m = floor((k+1)*a), N(i) in {m,m+1}?
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
STRUCT = os.path.join(HERE, "..", "out", "structure.json")


def load():
    return json.load(open(STRUCT))


def circ_interval(bits):
    n = len(bits)
    ones = [j for j, b in enumerate(bits) if b == 1]
    if not ones:
        return None, 0
    if len(ones) == n:
        return 0, n
    z0 = next(j for j, b in enumerate(bits) if b == 0)
    start = None
    L = 0
    j = (z0 + 1) % n
    seen = 0
    while seen < n:
        if bits[j] == 1:
            if start is None:
                start = j
            L += 1
        else:
            if start is not None:
                break
        seen += 1
        j = (j + 1) % n
    return start, L


def main():
    data = load()
    print("k n | N(i) set | consecutive s-diffs mod n (unique) | s(0)")
    for k in range(3, 61):
        facs = data[str(k)]
        n = k + 1
        starts, Ns = [], []
        for i in range(k):
            bits = [1 if f[i] == '1' else 0 for f in facs]
            s, L = circ_interval(bits)
            starts.append(s)
            Ns.append(L)
        diffs = set((starts[i + 1] - starts[i]) % n for i in range(k - 1))
        print(f"{k:2d} {n:2d} | {sorted(set(Ns))} | {sorted(diffs)} | {starts[0]}")


if __name__ == "__main__":
    main()
