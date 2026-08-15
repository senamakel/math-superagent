#!/usr/bin/env python3
"""PATTERN-FINDER: (a) extend the P=5 affine check and extract exact per-residue
offsets; (b) P=7 true nu2 — per-residue structure and min-density estimate;
(c) P=3 right-diagonal {0,2} suffix pattern, to expose a provable mechanism.

Model: q_1=2, q_2=3, gap = 2 if bit else 4, bits = tail-1 word of period P.
nu2(n) = #2s in maximal {0,2} suffix of right diagonal delta(q_n)
(lib.rightdiag.cycle_and_nu2, body convention).
"""
import sys
sys.path.insert(0, '/workspace/code')
from lib.rightdiag import incremental_diagonals, cycle_and_nu2, delta_diagonal


def build_seq(word, n_terms):
    q = [2, 3]
    per = len(word)
    while len(q) < n_terms:
        bit = word[(len(q) - 2) % per]
        q.append(q[-1] + (2 if bit else 4))
    return q[:n_terms]


def nu2_seq(word, nmax):
    q = build_seq(word, nmax + 1)
    out = {}
    for k, dd in enumerate(incremental_diagonals(q)):
        if k >= 2:
            out[k] = cycle_and_nu2(dd)[1]
    return out


def main():
    print("(a) P=5 word 00001: verify nu2(n+15)==nu2(n)+8 to n=3000; per-residue offsets")
    P5 = nu2_seq([0, 0, 0, 0, 1], 3000)
    bad = [n for n in range(200, 2985) if P5[n + 15] != P5[n] + 8]
    print(f"    nu2(n+15)==nu2(n)+8 over [200,2985]: "
          f"{'EXACT, ' if not bad else 'FAIL '}first bad {bad[:5]}")
    # per-residue exact offsets: nu2(n) = (8n + c_r)/15 for n ≡ r mod 15
    print("    per-residue offsets c_r defined by 15*nu2(n) - 8n == c_r:")
    offs = {}
    ok = True
    for r in range(15):
        ns = [n for n in range(200, 1000) if n % 15 == r]
        vals = {(15 * P5[n] - 8 * n) for n in ns}
        offs[r] = vals
        if len(vals) != 1:
            ok = False
    for r in range(15):
        print(f"      r={r:2d}: offset set {sorted(offs[r])}")
    print(f"    all residues constant: {ok}")
    print()

    print("(b) P=7 word 0000001: true nu2 structure")
    P7 = nu2_seq([0, 0, 0, 0, 0, 0, 1], 1500)
    seq7 = [P7[n] for n in range(2, 62)]
    print(f"    nu2(2..61): {seq7}")
    # per-residue mod 7 first differences
    print("    per-residue (mod 7) subsequence first differences at n~1000:")
    for r in range(7):
        ns = [n for n in range(700, 1490, 7) if n % 7 == r]
        sub = [P7[n] for n in ns]
        dif = [sub[i + 1] - sub[i] for i in range(len(sub) - 1)]
        print(f"      r={r}: diffs {dif[:8]}{'...' if len(dif)>8 else ''}")
    # min density over [200,1500]
    minr = min((P7[n] / n, n) for n in range(200, 1501))
    print(f"    min P7 nu2/n over [200,1500] = {minr[0]:.4f} at n={minr[1]}")
    print()

    print("(c) P=3 word 001: right-diagonal {0,2} suffix pattern at n=6..21")
    q = build_seq([0, 0, 1], 22)
    for n in range(6, 22):
        d = delta_diagonal(q, n - 1)
        tau, nu2 = cycle_and_nu2(d)
        print(f"    n={n:2d}: diag={d}  tau={tau}  nu2={nu2}")


if __name__ == "__main__":
    main()