#!/usr/bin/env python3
"""Measure the enclosure-width barrier for certifying inf_P g/Eh >= 1 near Yu's
minimizer (a1=a2=a, b1=a, b2=1, a≈0.3300622, value 1.00000889 at t=0.38234,
alpha=0.035).  A cell containing the minimizer certifies lo>=1 only when its
rigorous enclosure width is < the margin (~8.9e-6).  We report, for a nested
sequence of cell widths around the minimizer, the enclosure LOWER bound.

This diagnoses whether STEP 1's B&B can ever certify in 10s."""
import mpmath as mp
from inner_inf_scorer import ratio_iv, Iv

mp.mp.dps = 40


def lo_for_width(a, w):
    """enclosure lower bound of g/Eh over the box [a-w,a+w] in a1,a2,b1 and
    [1-w, 1] in b2 (b2 capped at its upper boundary 1; a single symmetric
    narrow box around the minimizer)."""
    al, ah = a - w, a + w
    r, eh, ok = ratio_iv(Iv(al, ah), Iv(al, ah), Iv(al, ah), Iv(max(0.0, 1 - w), 1),
                         0.38234, 0.035)
    return r.a if ok == 1 else None


a = 0.3300622
print(f"minimizer a={a}, true value 1.00000889, margin above 1 = {1.00000889-1:.3e}")
for w in [1e-2, 1e-3, 1e-4, 1e-5, 1e-6]:
    lo = lo_for_width(a, w)
    print(f"  box width {w:8.0e}: enclosure LOWER bound = "
          f"{mp.nstr(lo, 10) if lo is not None else 'n/a (infeasible)'}"
          f"  {'>= 1' if lo is not None and lo >= 1 else ''}")
