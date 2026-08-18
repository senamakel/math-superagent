"""Extract V(R_k) run values and run-gap (Sturmian) sequences to disk for
the sequence tools. V(R_k) computed by brute factor enumeration of the
distinct length-k factors of the Fibonacci word."""
from collections import Counter

def fib_word(min_len):
    a, b = '0', '01'
    while len(b) < min_len:
        a, b = b, b + a
    return b

def main():
    kmax = 400
    word = fib_word(4 * kmax + 8)
    L = len(word)
    VR = {}
    for k in range(1, kmax + 1):
        exts = {}
        for i in range(L - k):
            w = word[i:i + k]
            exts.setdefault(w, set()).add(word[i + k])
        factors = set(word[i:i + k] for i in range(L - k + 1))
        Rs = [w for w in factors if len(exts.get(w, set())) == 2]
        assert len(Rs) == 1, k
        VR[k] = int(Rs[0])
    # runs
    runs = []               # (start, end, value)
    prev, cstart = None, 1
    for k in range(1, kmax + 1):
        if VR[k] != prev:
            if prev is not None:
                runs.append((cstart, k - 1, prev))
            cstart = k
            prev = VR[k]
    runs.append((cstart, kmax, prev))
    runvals = [v for s, e, v in runs]
    starts = [s for s, e, v in runs]
    gaps = [starts[i + 1] - starts[i] for i in range(len(starts) - 1)]
    runlens = [e - s + 1 for s, e, v in runs]
    print("runs:", len(runs))
    print("run starts:", starts)
    print("run gaps:", gaps)
    print("run lengths:", runlens, "hist", Counter(runlens))
    print("run VALUES (first 60):", runvals[:60])
    with open("code/out/vr_runvals.txt", "w") as f:
        for v in runvals:
            f.write(str(v) + "\n")
    with open("code/out/vr_rungaps.txt", "w") as f:
        for g in gaps:
            f.write(str(g) + "\n")

if __name__ == "__main__":
    main()
