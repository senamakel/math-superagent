# Which regularity most likely yields an O(log) derivation

## The best handle: Wythoff-block structure of the right-special factor

The single most promising regularity for turning Psi(k) at k = 10^18 into an
O(log) evaluation is the **right-extension recurrence combined with the
Wythoff run structure of V(R_k)**:

    Psi(k+1) = 100·Psi(k) + 100·V(R_k)^2 + 20·S1(k) + J(k)
    J(k)     = 1 + floor((k+1)/phi^2)     (c1(k+1))

which is exact (direct proof from Sturmian right-extension structure) and
mod-M exact through k=400.  The remaining objects are V(R_k) and S1(k).
But V(R_k) is **constant on runs starting at the upper-Wythoff numbers
s_j = floor(j·phi^2)** (verified exact to k=3000), and within a run
R_k = '0'^d + R_{s_j} is just left zero-padding.  That means the correction
terms do not need one value per k: they collapse to one value per Wythoff
block, and there are only ~(log k) Fibonacci-sized blocks up to k (about 87
blocks at 10^18, matching the operator directive's "87 blocks").  This is
exactly the block-renormalisation that makes the naive per-k recurrence
O(log).

## Why the other regularities do not close it

- **No scalar recurrence survives mod M** — confirmed by the exact tools:
  Psi(k) mod M has no constant-coefficient linear recurrence (order ≤ 12),
  is noise-flat, and is not catalogued in OEIS.  No polynomial/linear closed
  form exists.
- **The autocorrelation/lag-sum collapse (directive 1)** holds only at
  k = F_n − 1, not at general k (Toeplitz defect bounded by 1 but nonzero).
- **Psi(k) itself** is not in OEIS (a miss was recorded), so no off-the-shelf
  closed form exists.

## The route the block structure feeds into

The committed O(log) method is the universal-Euclidean geometrically-weighted
floor-sum monoid (code/lib/ueuclid.py): Psi is the second moment of a
geometrically weighted floor sum over the k+1 arc representatives.  The
Wythoff block structure is exactly the way to accelerate the S1(k) and V(R_k)
correction terms (and the operator's prefix-window partial-sum V) inside the
monoid — carry the (v, sum v^2, sum v, 1) state through a constant-size
transfer matrix, collapse by Fibonacci/Wythoff block renormalisation.  The
two handles that matter are therefore (a) the mechanical floor-sum second
moment and (b) the Wythoff column structure of the right-special factor.

Files: research/notes/pattern-hunt-pe1006-cycle4.md (catalogue),
code/pattern_hunt/*.py (verifiers), code/out/r_runs_wythoff.txt (exact to k=3000).
