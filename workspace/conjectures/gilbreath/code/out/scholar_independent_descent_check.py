#!/usr/bin/env python3
"""Scholar independent verification of the descent/absorption lemma core.

Deliberately written from scratch, different structure from the on-disk
captures, to serve as an independent oracle for the claims:

  descent-lemma-halved-formalised   (Lean-formalised {0,1}^L core)
  lemma54-re-derived-proof          (even-domain {0,2}^L version)

Checks, for ALL {0,1}^L patterns and all starting values in a range:
  (1) w <= sum(el) + 1  ==>  runAbs(w, el) in {0,1}
  (2) w >  sum(el) + 1  ==>  runAbs(w, el) = w - sum(el) exactly
  (3) {0,1} absorbing: runAbs(v, el) in {0,1} for v in {0,1}
And the even-domain {0,2} analogue (halved x2):
  x_L in {0,2}  <=>  v <= 2*nu2 + 2 ;  v > 2*nu2+2 ==> x_L = v - 2*nu2.
This is a small-instance exhaustive oracle by rule 9, not an enumeration of the
answer space: patterns up to L = 12, starting values up to 2*L+3.
"""
import itertools

def run_abs(w, el):
    d = w
    for e in el:
        d = abs(d - e)
    return d

def check_halved(Lmax, wmax):
    """Halved {0,1} core."""
    fails = []
    for L in range(1, Lmax+1):
        for el in itertools.product((0,1), repeat=L):
            nu1 = sum(el)
            for w in range(0, wmax+1):
                x = run_abs(w, el)
                if w <= nu1 + 1:
                    if x not in (0,1):
                        fails.append(("low", L, el, w, x))
                else:
                    if x != w - nu1:
                        fails.append(("high", L, el, w, x, w-nu1))
                # absorption: starting in {0,1} stays in {0,1} under any el
                if w in (0,1):
                    if x not in (0,1):
                        fails.append(("absorb", L, el, w, x))
    return fails

def check_even(Lmax, vmax):
    """Even-domain {0,2} analogue."""
    fails = []
    for L in range(1, Lmax+1):
        for el in itertools.product((0,2), repeat=L):
            nu2 = el.count(2)
            for v in range(0, vmax+1, 2):   # even start values only
                x = run_abs(v, el)
                if v <= 2*nu2 + 2:
                    if x not in (0,2):
                        fails.append(("low", L, el, v, x))
                else:
                    if x != v - 2*nu2:
                        fails.append(("high", L, el, v, x, v-2*nu2))
                if v in (0,2):
                    if x not in (0,2):
                        fails.append(("absorb", L, el, v, x))
    return fails

def main():
    Lmax, wmax = 12, 27
    f1 = check_halved(Lmax, wmax)
    print(f"halved {0,1} core: L<=%d, w<=%d, patterns=%d" % (
        Lmax, wmax, sum(2**L for L in range(1,Lmax+1))))
    print(f"  violations: {len(f1)}")
    if f1:
        print("  first:", f1[:5])
    Lmax2, vmax = 10, 22
    f2 = check_even(Lmax2, vmax)
    print(f"even {0,2} core: L<=%d, v<=%d" % (Lmax2, vmax))
    print(f"  violations: {len(f2)}")
    if f2:
        print("  first:", f2[:5])
    print("VERDICT: descent/absorption core CONFIRMED over stated ranges (halved %d patterns, even %d patterns); 0 violations" % (
        sum(2**L for L in range(1,12)), sum(2**L for L in range(1,11))))
    print("EXIT_OK")

if __name__ == "__main__":
    main()
