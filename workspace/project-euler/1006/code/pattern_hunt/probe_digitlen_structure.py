"""Digit-length structure of exact Psi(k), k=1..3000: full distribution."""
import sys
from math import isqrt

sys.set_int_max_str_digits(20000)


def c1(k):
    N = isqrt(5 * k * k)
    t = 3 * k - N
    if t % 2 == 1:
        return 1 + (t - 1) // 2
    return 1 + (t // 2 - 1)


def load_pairs(path):
    out = {}
    with open(path) as fh:
        for line in fh:
            p = line.split()
            if len(p) >= 2:
                out[int(p[0])] = int(p[1])
    return out


def main():
    vR = load_pairs("code/out/vR_exact.txt")
    s1 = load_pairs("code/out/s1_exact.txt")
    Psi = {1: 1}
    for k in range(1, 3000):
        Psi[k + 1] = 100 * Psi[k] + 100 * vR[k] ** 2 + 20 * s1[k] + c1(k + 1)

    from collections import Counter
    lens = Counter()
    for k in range(1, 3001):
        lens[len(str(Psi[k])) - (2 * k - 1)] += 1
    print("distribution of len(Psi(k))-(2k-1), k=1..3000:", dict(lens))

    # run structure of len==2k-1 positions and of len==2k+1 positions
    cls = {k: len(str(Psi[k])) - (2 * k - 1) for k in range(1, 3001)}
    runs = []
    for k in range(1, 3001):
        if cls[k] != 0:
            if runs and runs[-1][1] == k - 1 and runs[-1][0] == cls[k]:
                runs[-1][1] = k
            else:
                runs.append([cls[k], k, k])
        else:
            if runs and runs[-1][0] == 0 and runs[-1][1] == k - 1:
                runs[-1][1] = k
            else:
                runs.append([0, k, k])
    print("runs of the class value len-(2k-1) == 0 (first 30, then all non-trivial):")
    zero_runs = [(a, b) for c, a, b in runs if c == 0]
    print("  count of k with len==2k-1:", len(zero_runs))
    print("  first 40 positions:", [k for k in range(1, 3001) if cls[k] == 0][:40])
    print("  last 20 positions:", [k for k in range(1, 3001) if cls[k] == 0][-20:])
    neg = [k for k in range(1, 3001) if cls[k] < 0]
    pos2 = [k for k in range(1, 3001) if cls[k] >= 2]
    print("  k with len < 2k-1:", neg[:20], ".. count", len(neg))
    print("  k with len >= 2k+1:", pos2[:20], ".. count", len(pos2))

    # correlation with c1's digit length: does len(Psi(k)) == 2k-1 iff
    # Psi(k) has leading block that fits in fewer digits?  test:
    # len(Psi(k)) == len(c1) + something?  print k, len, class at boundaries
    print("\nsample around transitions:")
    for k in [22, 23, 24, 25, 255, 256, 257, 258, 259, 260, 377, 609, 610, 987, 1597, 2584]:
        print(f"  k={k:5d} len={len(str(Psi[k])):5d} 2k-1={2*k-1:5d} 2k={2*k:5d} class={cls[k]:+d} c1={c1(k)}")


if __name__ == "__main__":
    main()