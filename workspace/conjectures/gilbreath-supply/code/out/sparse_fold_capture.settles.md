EXECUTED RESULT THIS RUN: sparse-input amplification of the SUPPLY fold
========================================================================
Runner writes to code/out/sparse_fold_capture.txt (full detail).

WHAT WAS RUN
  New library module code/lib/sparse_fold.py + drivers. Exact arithmetic,
  two independent oracle routes (SOS submask-product transform AND the explicit
  F2 matrix matvec) agree on every row counted.
  - Capacity curve Cap(n,k)=max wt(Phi_n h) over k-sparse h, n=8,10,12 (brute).
  - Single-1 fold weight by position, n=8,10,12.
  - Fixed infinite sparse string (density 0) fold-weight ratio, n=256..4096.

WHAT IT SETTLES
  1. Sparsity never caps the fold's image weight. Cap(n,k) = n-2 or n-3 for
     EVERY k in 1..n-1 (max possible is n-2). Even a single 1 reaches full
     weight when placed at the shared boundary index n-1. The general transfer
     'sparse h => wt(Phi_n h) = o(n)' (gap G-eq-sparse-fold-is-sublinear) is
     FALSE even at k=1. Confirms and extends the known e_{n-1} refutation.
  2. The mechanism is boundary-spike concentration: every depth reads the
     depth's own offset o=d (a submask of d), which lands on the shared final
     index n-1, so one boundary 1 feeds all n-2 depths.
  3. Central hypothesis (GOAL.md: can Phi do work switch-density cannot see?):
     YES infinitely often -- the density-0 powers-of-2 support string has
     wt/n ~ 2/3 along n = 2^k+1 (tested to 4096) while its mod-4 switch density
     is 0. BUT every FIXED sparse string has liminf ratio 0 (powers-of-2 fail
     at every exact 2^k; squares have lower-envelope min only 0.0739). So no
     fixed finite-prefix condition discharges G-weak-input-strictness; a
     witness must have support growing with n and avoid the read-boundary
     drop -- a strictly finer object than any fixed S.

EVIDENCE CLASS
  Exact / oracle-checked computation (two routes agree). NOT a proof of any
  infinite-n statement. Refines existing refutations and pins the witness shape
  for the live gap. Negative control present (k=0 and k=n give 0 = kernel).

STATUS, HONESTLY
  This is a sharpening of the structural picture, not a proof of SUPPLY. It
  moves the open question from 'can a sparse input be amplified' (already
  known refuted for the general transfer) to 'must a growing witness avoid the
  boundary drop', which is a precise, attackable shape.
