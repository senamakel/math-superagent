# Thread: directive-9 contiguous-window prefix-sum route (avoids the O(k)-intercept obstruction)

---
thread:
  question: Can Psi(k) for PE1006 be computed in O(log) as the partial sum of v_r^2 over a contiguous prefix range of windows of the doubled standard word q_n q_n — avoiding the O(k)-intercept obstruction of psi-to-ueuclid-reduction.md — collapsed by a constant-size transfer matrix over the pair (y_r, y_(r+k)) with Fibonacci-block renormalisation (~87 blocks at 10^18)?
  status: live
  rests-on: governing-sturmian (standard words / mechanical), governing-factor-complexity (k+1 distinct factors), mechanical-word-digit-rule, governing-universal-euclidean
  blocked-by: none
  next: Directive 11: primitive verified on current code — do NOT rebuild it; run its own __main__ once and capture; then acceptance 4, anchors, then 10^18 under two approximants. Full detail below.
---

## What the directive asserts (steer, NOT established — check before building)

The O(k)-intercept obstruction in `research/notes/psi-to-ueuclid-reduction.md`
is avoidable. Verified outside the container at k = 3,5,6,8,10,13,17,21,26,34,
40,55,70,100,144,200 and for EVERY level n with F_n > k, not just the minimal
one.

- **Claim 1** — the k+1 DISTINCT length-k factors are exactly the k+1
  CONTIGUOUS windows at positions r = F_n-k-1 .. F_n-1 of the doubled standard
  word q_n q_n. As sets they are equal, every time. So Psi(k) = sum over that
  contiguous window range of v_r^2 — no multiplicity, no de-dup, no sum over l
  with O(k) intercepts. Sample at k=3: the five windows of q_4 q_4 = 0100101001
  are 010,100,001,010,101, the last four are the four distinct factors, and
  10000+1+100+10201 = 20302.
- **Claim 2** — Psi(k) = (full cyclic sum over all F_n windows) - (sum over
  the FIRST F_n-k-1 windows).
- **Claim 3** — the full cyclic sum equals sum_{j,jp} A(jp-j) 10^(2k-2-j-jp)
  with A the cyclic autocorrelation of q_n, for ANY k < F_n. Directive 1's
  identity was never restricted to k = F_n - 1 as a statement about the CYCLIC
  sum; the restriction was only ever about the cyclic sum equalling Psi. It
  does not, in general, and claim 2 is exactly the correction term.

## The remaining object

The partial sum of v_r^2 over a prefix range of windows. Use
v_(r+1) = 10 v_r - y_r 10^k + y_(r+k) with y the Fibonacci word; carry the
state (v, sum v^2, sum v, 1) as a constant-size transfer matrix whose step
depends on the pair (y_r, y_(r+k)), and collapse the product over the range by
Fibonacci-block renormalisation — about 87 blocks at 10^18.

## Dead-end record

The joint-monoid double-sum formulation in `psi-to-ueuclid-reduction.md` fights
an O(k) distinct-intercept obstruction (one intercept per l); that route is
what this directive replaces.
