"""PE1006: noise-vs-structure probe on the residue sequence
Psi(k) mod 101001001 for k=1..400.

- adjacent differences mod M: sample, and histogram of leading hex digit
- autocorrelation r(h) for h = 1..40  (sample autocorrelation, mean-subtracted)
- are the residues "flat"?  chi-squared of the leading digit distribution
  against uniform, on the actual M-residues
- first-digit leading-nonzero count structure seen in extract_subseqs
"""

import math

M = 101001001


def read_res(path):
    return [int(line.split()[1]) for line in open(path)]


def main():
    r = read_res('code/out/psi_residues.txt')
    n = len(r)
    print(f"n={n}")

    # sample autocorrelation, lags 1..40
    mean = sum(r) / n
    var = sum((x - mean) ** 2 for x in r) / n
    print(f"mean={mean:.2f}  var={var:.2f}  M/2={M/2:.1f}")
    print("autocorrelation:")
    out = []
    for h in range(1, 41):
        num = sum((r[i] - mean) * (r[i + h] - mean) for i in range(n - h))
        den = (n - h) * var
        out.append(num / den)
        if h in (1, 2, 3, 5, 8, 13, 21, 34):
            print(f"  h={h:3d}  r(h)={num / den:+.4f}")
    big = [abs(x) for x in out]
    print(f"max |r(h)| over h=1..40 = {max(big):.4f} (at h={big.index(max(big))+1})")
    # expected std for white noise ~ 1/sqrt(n)
    print(f"1/sqrt(n) = {1/math.sqrt(n):.4f}")

    # chi-squared of leading digit (0..9) against uniform
    from collections import Counter
    lead = Counter(str(x)[0] for x in r)
    print("leading-digit counts:", dict(sorted(lead.items())))
    exp = n / 10
    chi2 = sum((lead.get(str(d), 0) - exp) ** 2 / exp for d in range(10))
    print(f"chi2 (9 dof) = {chi2:.2f};  critical ~16.9 at 5%")

    # gaps between equal residues mod M: are collisions happening?
    # (with 400 draws from ~1e8, birthday gives ~0.8 expected collisions)
    from collections import defaultdict
    pos = defaultdict(list)
    for i, x in enumerate(r, 1):
        pos[x].append(i)
    coll = {x: p for x, p in pos.items() if len(p) > 1}
    print(f"repeated residues: {len(coll)} (expect ~{n * n / (2 * M):.2f})")
    for x, p in list(coll.items())[:5]:
        print(f"  {x}: positions {p}")


if __name__ == '__main__':
    main()