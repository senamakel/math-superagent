# Working memory

## Problem

Project Euler 591. BQA_d(x,n) = quadratic integer a + b*sqrt(d) (integers a,b
with |a|,|b| <= n) closest to real x, minimizing |a + b sqrt(d) - x|.
I_d(a + b sqrt(d)) = a. Need sum of |I_d(BQA_d(pi, 10^13))| over all
non-square positive integers d < 100. This workspace task is only to build
the brute-force oracle and verify the given examples/claims, not to solve the
full problem.

## Established results

Verified brute-force oracle (brute.py), float sqrt — all reproduce statement:
- BQA_2(pi,10)     = a=6,  b=-2                (`6 - 2 sqrt(2)`)
- BQA_5(pi,100)    = a=-55, b=26               (`26 sqrt(5) - 55`)
- BQA_7(pi,10^6)   = a=560323, b=-211781
All three PASS.

Recorded medium-n brute-force results (float):
- d=2, n=10^7  -> a=691596,   b=-489030   err 3.17e-8
- d=2, n=10^8  -> a=32680452, b=-23108567 err 1.98e-9
- d=3, n=10^6  -> a=212673,   b=-122785   err 1.83e-9
(verified to hold the |a|<=n invariant; not otherwise cross-checked)

High-precision check (mpmath, 60 digits) of the d=2 n=10^13 candidate
a=-6188084046055, b=4375636191520:
|a + b sqrt(2) - pi| = 4.29e-15  < 1e-13  PASS
(Confirms the given I_2 = a = -6188084046055 claim.)
Upper-bound candidate in the statement double inequality
a=-1019836515172, b=721133315582: gap = 9.25e-14 < 1e-13 PASS.

NOTE: with plain double precision the 10^13 candidate computes as gap ~8.9e-6
because a,b ~1e13 exceed double's ~16-significant-digit resolution (~1e-4
absolute). Must use high-precision arithmetic for the big cases.

## Failed approaches / notes

- refresh_index tool has a path bug in this environment (prepends "workspace/"
  to an already-rooted path), fails for /workspace, /workspace/toolkits,
  /workspace/research. Worked around by editing INDEX.md directly.
- Double-precision float is NOT adequate for computing |a+b sqrt(d)-pi| when
  a,b are ~1e13 and the target gap is ~1e-13; use mpmath or exact integer
  arithmetic (isqrt-style) for any large-n verification.

## Open questions

- The medium-n brute-force records (d=2 n=1e7/1e8, d=3 n=1e6) have not been
  independently verified by a second route, and the d=2 n=1e8 float gap
  (~2e-9 reported) is at/near float resolution — float sqrt noise can distort
  both the error magnitude and (at n~1e8) possibly the winning (a,b). Recheck
  with high-precision arithmetic before relying on them. The three statement
  examples and the mpmath 1e13 claim are fully verified and are the trusted
  oracle.
