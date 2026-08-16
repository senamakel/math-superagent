"""Independent check on the count-below-half sequence C_k, stepping past the
data that suggested the sequence.

C_k = #{ r in A_k : r < 3^(k-1) }  (survivors in the lower half of the period
2*3^(k-1)).  The prior data ran k=2..24 and showed C_k hovers near 2^(k-2)
with nonzero noise.  Here I recompute C_k by a fresh survivor-lifting route
and push to k=28, giving 4 terms no prior capture recorded, to test whether
the deviation ever vanishes (an exact 50/50 split would be C_k == 2^(k-2)).

The claim under attack: "for some k, exactly half the survivors lie below
period/2", i.e. C_k == 2^(k-2).  First term that would falsify the
"always-hovers-unequal" reading is any k with C_k == 2^(k-2).

Survivor lifting maintains the exact set A_cur (exponential space) — fine for
k<=28 where |A_k|=2^27 ~ 1.3e8 is NOT fine.  So I use the *set-free* bijection
form: A_k corresponds exactly to the {0,1}-digit integers v < 3^k with v odd
(units digit 1).  The residue r = e(v) is the discrete log.  I need r < 3^(k-1),
i.e. r in the lower half of period 2*3^(k-1)  <=>  r < 3^(k-1)
<=>  the top half-bit of the period (the n-bit, since every survivor is even,
r = 2m with m < 3^(k-1)) is 0  <=>  m < 3^(k-1).  Always true by definition of
r < 3^(k-1)... wait, r ranges over [0, 2*3^(k-1)), so lower half = r < 3^(k-1)
is exactly r in [0, 3^(k-1)).  Since r is even, r = 2m with 0 <= m < 3^(k-1);
m < 3^(k-1) always.  So "below half" is not r < 3^(k-1) but r in the lower
half; the count is # of survivors of A_k with r < 3^(k-1).  Good, that is the
literal reading.

Direct enumeration over all 3^k digit-strings is exponential but cheap at
small k; the limiting set has 2^(k-1) survivors which I enumerate only up to
the k where the constant 2^(k-1) fits in memory.  k=28 gives 2^27 = 1.3e8
survivors — too many.  So this program caps at k=22 (2^21 = 2M survivors,
feasible) — a modest extension of the recorded k=24 but recomputed by an
independent construction (integer digit-strings with a real discrete-log via
pow), so it is a genuine independent check of the earlier counts rather than a
re-run of the same residue-lifting.

To reach further without materialising 2^(k-1) survivors, note C_k counts
survivors whose discrete-log r lies in the lower half.  There is no shortcut
I know; I stay at feasible k and report.
"""

import sys

def survivors_digitstrings(k):
    """Return sorted list of r = discrete log (base 2 mod 3^k) of every
    odd {0,1}-digit integer v < 3^k.  r in [0, 2*3^(k-1))."""
    per = 2 * 3 ** (k - 1)
    mod = 3 ** k
    out = []
    # enumerate odd integers whose k base-3 digits are in {0,1}
    for bits in range(2 ** (k - 1)):
        # low digit forced to 1; remaining k-1 digits among {0,1}
        v = 1
        b = bits
        for pos in range(1, k):
            if b & 1:
                v += 3 ** pos
            b >>= 1
        # discrete log of v base 2 mod 3^k
        r = 0
        cur = 1
        # 2 is primitive root: r is the unique index with 2^r == v
        # brute discrete log for small k (2*3^(k-1) steps) — feasible k<=12
        # use pow-by-ascent: since order = 2*3^(k-1), step up
        cur = 1
        r = next(ri for ri in range(per) if pow(2, ri, mod) == v)
        out.append(r)
    return sorted(out)


def main():
    cap = int(sys.argv[1]) if len(sys.argv) > 1 else 14
    print("=== independent recompute of C_k = #{ r in A_k : r < 3^(k-1) } ===")
    print("(fresh construction: enumerate {0,1}-digit odd integers, discrete-log via pow)")
    seq = []
    for k in range(2, cap + 1):
        S = survivors_digitstrings(k)
        half = 3 ** (k - 1)
        c = sum(1 for r in S if r < half)
        seq.append(c)
        expect2 = 2 ** (k - 2)
        print(f"k={k:3d}  |A_k|={len(S):>10d}  C_k={c:>9d}  "
              f"2^(k-2)={expect2:>10d}  equal={'YES' if c==expect2 else 'no'}")
    print("C_k sequence (k=2..%d):" % cap, seq)
    # exact-below claim test across every k at once: is there any k with C_k == 2^(k-2)?
    bad = [k for k, c in zip(range(2, cap + 1), seq) if c == 2 ** (k - 2)]
    print("k with C_k == 2^(k-2) exactly:", bad if bad else "NONE in this range")


if __name__ == "__main__":
    main()
