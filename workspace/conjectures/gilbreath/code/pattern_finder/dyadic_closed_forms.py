#!/usr/bin/env python3
"""PATTERN-FINDER: exact closed forms for nu2(n) on periodic 2-then-odds words.

Model (locked to dyadic oracle): q_1=2, q_2=3, gap = 2 if bit else 4, bits =
periodic word repeated.  nu2(n) = #2s in maximal {0,2} suffix of right
diagonal delta(q_n) (body convention, lib.rightdiag.cycle_and_nu2).

Verified already (n=2..120):  P=3 word 001 -> nu2(n) = 2*floor((n-1)/3).

Here:
  (1) verify the P=3 closed form to nmax=2000 (big exact check);
  (2) extract nu2(n) for P=5 word 00001 and fit candidate rational-slope
      closed forms; report exact-match counts and first falsifier;
  (3) all 8 period-3 words: classify grow/collapse and give exact sequences.
Exact integer arithmetic; O(nmax^2) diffs, O(nmax) memory.
"""
import sys
sys.path.insert(0, '/workspace/code')
from lib.rightdiag import incremental_diagonals, cycle_and_nu2


def build_seq(word, n_terms):
    q = [2, 3]
    per = len(word)
    while len(q) < n_terms:
        bit = word[(len(q) - 2) % per]
        q.append(q[-1] + (2 if bit else 4))
    return q[:n_terms]


def nu2_seq(word, nmax):
    """nu2(n) for n=2..nmax, exact, one diagonal pass."""
    q = build_seq(word, nmax + 1)
    out = {}
    for k, dd in enumerate(incremental_diagonals(q)):
        if k >= 2:
            out[k] = cycle_and_nu2(dd)[1]
    return out


def check_form(word, nmax, form, desc):
    """form(n) candidate; report exact-match count and first bad."""
    vals = nu2_seq(word, nmax)
    bad = []
    for n in range(2, nmax + 1):
        if form(n) != vals[n]:
            bad.append((n, vals[n], form(n)))
            if len(bad) >= 4:
                break
    tot = nmax - 1
    ok = tot - len(bad)
    print(f"  {desc}: {ok}/{tot} exact  "
          + (f"first bad {bad}" if bad else "NO falsifier up to nmax"))
    return len(bad) == 0, vals


def main():
    print("=" * 66)
    print("(1) P=3 word 001: closed form nu2(n) = 2*floor((n-1)/3), n=2..2000")
    vals = nu2_seq([0, 0, 1], 2000)
    bad = [n for n in range(2, 2001) if vals[n] != 2 * ((n - 1) // 3)]
    print(f"    matches: {2000-1-len(bad)}/1999  first bad: {bad[:5]}")
    print()

    print("=" * 66)
    print("(2) P=5 word 00001: exact nu2(n) first 48 terms (n=2..49):")
    vals5 = nu2_seq([0, 0, 0, 0, 1], 49)
    seq5 = [vals5[n] for n in range(2, 50)]
    print("   ", seq5)
    print()
    # increments by 5
    print("    increments nu2(n)-nu2(n-5):")
    inc = [vals5[n] - vals5[n - 5] for n in range(7, 50)]
    print(f"    {inc}")
    print("    candidates:")
    # 8/15 slope: check nu2(n) = floor(8n/15) + offset patterns
    check_form([0, 0, 0, 0, 1], 300,
               lambda n: (8 * n) // 15, "floor(8n/15)")
    check_form([0, 0, 0, 0, 1], 300,
               lambda n: (8 * (n - 2)) // 15, "floor(8(n-2)/15)")
    check_form([0, 0, 0, 0, 1], 300,
               lambda n: (8 * n - 8) // 15, "floor((8n-8)/15)")
    print()

    print("=" * 66)
    print("(3) all 8 period-3 words: nu2 at n=120 and n=600 (grow vs collapse):")
    for bits in range(8):
        w = [(bits >> 2) & 1, (bits >> 1) & 1, bits & 1]
        v1 = nu2_seq(w, 121)
        v2 = nu2_seq(w, 601)
        a = v1[120]
        b = v2[600]
        tag = "COLLAPSE" if b < 15 else "GROW"
        print(f"    {''.join(map(str,w))}: nu2(120)={a:4d}  nu2(600)={b:4d}  {tag}")


if __name__ == "__main__":
    main()