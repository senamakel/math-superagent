"""Extract and print the (s(i), N(i)) interval data for every k, to look for
closed forms of the start sequence s(i) and length sequence N(i) in (k,i,alpha).
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
    for k in range(3, 34):
        d = data[str(k)]
        facs = d["factors"]
        n = k + 1
        starts, Ns = [], []
        for i in range(k):
            bits = [1 if f[i] == '1' else 0 for f in facs]
            s, L = circ_interval(bits)
            starts.append(s)
            Ns.append(L)
        print(f"k={k:2d} n={n:2d} | s: {starts}")
        print(f"           | N: {Ns}")


if __name__ == "__main__":
    main()
