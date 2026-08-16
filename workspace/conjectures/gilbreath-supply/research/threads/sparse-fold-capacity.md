# Sparse-input amplification of the fold — capacity curve and witness shape

Settled this run (exact, two independent oracle routes agree). Full detail and
numbers in `code/out/sparse_fold_capture.txt`, one-page summary in
`code/out/sparse_fold_capture.settles.md`, implementation in
`code/lib/sparse_fold.py`.

## Results (all measured / oracle-checked, none an infinite-n theorem)

1. **Sparsity never caps fold weight.** Cap(n,k) = max wt(Φ_n h) over
   k-sparse h equals n−2 or n−3 for **every** k in 1..n−1 (max possible n−2),
   exact brute force at n = 8,10,12, confirmed identically by a second route
   (explicit F₂ matrix matvec). Even a *single* 1 reaches full weight at the
   shared boundary index n−1. The general transfer "sparse h ⇒ wt(Φ_n h) = o(n)"
   (gap G-eq-sparse-fold-is-sublinear) is **false even at k = 1** — the known
   e_{n-1} per-window refutation is not an artifact of one position; the
   *maximum* over k-sparse strings is (n−2) for every k.

2. **Mechanism.** Boundary-spike concentration: every depth d reads the
   depth's own offset o = d (a submask of d), landing on the shared final index
   n−1, so one 1 there feeds all n−2 depths.

3. **Central hypothesis (can Φ do work switch-density can't see?):** Yes
   *infinitely often*. The density-0 powers-of-2 string has wt(Φ_n h)/n ~ 2/3
   along n = 2^k+1 (exact to 4096) while its mod-4 switch density is 0. But
   **every fixed sparse string has liminf ratio 0** (powers-of-2 fail at every
   exact 2^k, ratio → 0; squares lower-envelope min only 0.0739). Hence no
   fixed finite-prefix condition discharges G-weak-input-strictness — its
   witness must have support growing with n and must avoid the read-boundary
   drop. That is precisely the shape the refuter's fixed-1 bound already
   demanded (a witness cannot be a finite spike), now confirmed computationally
   over two infinite sparse families and generalised to "no fixed S works at
   all".

## Bearing

Sharpens the open sharpest question. The fold genuinely amplifies sparse inputs
infinitely often (so the switch-density form genuinely discards structure), but
SUPPLY needs the ratio bounded below for **all** large n, and every fixed
sparse string fails liminf. The live object is a *growing* sparse witness that
stays away from the read-boundary drop — or a proof that none can exist, which
would re-establish gap G-eq-sparse-fold-is-sublinear in the only form that
could matter for the equivalence (GOAL priority 3).

## Evidence / negative controls

- Two independent exact routes (SOS submask-product transform; explicit F₂
  matrix matvec via `lib.fold_matrix`) agree on every counted row.
- Negative control present: k = 0 and k = n (all-ones) give wt = 0 (kernel,
  closed door 1), so the enumeration is not vacuous.
- All numbers exact; only ratio columns are floats. No proof of any infinite-n
  statement is claimed.
