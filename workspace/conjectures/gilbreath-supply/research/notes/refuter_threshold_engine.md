# Refuter — attack on the parity-control engine of the two open threshold lemmas

## Target

`G-threshold-parity-control` (BACKWARD.md / the shared engine of
`G-threshold-asymptotic-zero` and `G-threshold-concentration`, which are the
named gap between PASS3's "threshold -> 0" measurement and a theorem):

> For X ~ Hypergeometric(n, m, w), w = floor(theta n):
>   |E[(-1)^X]|  <=  max_j P[X=j]  <=  C / sqrt(1 + theta(1-theta)m(1-m/n)).

The whole asymptotic conclusion of PASS3 (w*(n) ~ n^0.555 -> sublinear-ish,
"tends to 0") stands or falls on this bound being TRUE. If either inequality
were false, both open lemmas collapse and PASS3's sublinear-threshold claim
loses its engine.

## What the engine actually says, in exact integers

E[(-1)^X] = sum_j (-1)^j P[X=j], P[X=j] = C(w,j)C(n-w,m-j)/C(n,m).
Scaling by C(n,m): the comparison |E[(-1)^X]| <= max_j P[X=j] is equivalent to

    | sum_j (-1)^j C(w,j) C(n-w,m-j) |  <=  max_j C(w,j) C(n-w,m-j).

## First inequality: |E[(-1)^X]| <= max_j P[X=j]

The hypergeometric pmf is **log-concave** (consecutive-ratio
P(j+1)/P(j) = [(w-j)(m-j)]/[(j+1)(n-w-m+j+1)] is decreasing in j), hence
**unimodal**: a_0 <= ... <= a_k >= ... >= a_n for the mode k. For any unimodal
nonnegative sequence, |sum_j (-1)^j a_j| <= a_k = max_j a_j — the classical
"alternating sum of a unimodal sequence is bounded by its maximum term"
(split at the mode; the increasing and decreasing sides each telescope to
things bounded by the mode).

### Hand checks (exact integers)

- n=2, m=1, w=1: A = C(1,1)C(1,0) - C(1,0)C(1,1) = 1 - 1 = 0, M = 1. |0|<=1. [equality corner]
- n=6, m=3, w=2 (the stated corner): A = 4 - 12 + 4 = -4, M = 12. |A|/C(6,3) = 4/20 = 0.2, maxatom = 12/20 = 0.6. The note's own number: |E|=0.2 <= 0.6. And C bound: Var X = 3*(2/6)(4/6)(3/5)=0.4, so C >= |E|·sqrt(1+Var) = 0.2·1.183 = 0.2366. The note's C>=0.26 is a safe over-estimate. MATCHES.
- Symmetric peak stripe: n=10,m=5,w=5 -> A=0; n=12,m=6,w=6 -> A=0 (all symmetric give exactly 0). Trivially <=.
- Deterministic corners m=n (A = (-1)^w·C(n,n), |A|=C(n,n)=M equality); m=n-1 gives |A|=|C(n-w,1)-C(w,1)·...| <= max, verified by the closed form |1-2w/n| <= max(w,n-w)/n.
- Flat-plateau worst case of the unimodal bound: |sum| equals the max exactly (e.g. 5 equal atoms), never exceeds.

Every hand case in the regimes the lemmas actually use satisfied |A| <= M.

## Second inequality: max_j P[X=j] <= C/sqrt(1+Var-ish)

For a log-concave pmf the mode atom is the max, and the standard local bound
max_j P[X=j] = O(1/sqrt(1+Var X)) holds (a squared-mass / concentration
argument: the mode atom controls a window of unit mass around it, and
sqrt(1+Var) bounds how far it can concentrate). For hypergeometric,
Var X = m(w/n)(1-w/n)(n-m)/(n-1) ~ theta(1-theta)m(1-m/n), matching the
claimed denominator. Standard and TRUE.

## Verdict on the engine

The engine lemma is **TRUE** (classical unimodal alternating-sum bound + the
standard log-concave mode bound). No violation found in any hand case,
including the note's own corner. This is NOT a refutation; it does however
discharge the risk that the two open lemmas rest on a false inequality. They
are open only through the (true) pair-counting in G-threshold-concentration,
which conclusion-pass3 already flags as the single open step.

## A sanity check on asymptotic-zero's scaling (hand)

Sum over popcount groups: group k has C(L,k) cells (L = floor(log2 n)),
m_d = 2^k, bound |K_w(m)/C(n,w)| <= C/sqrt(1+theta(1-theta)2^k).
Term ~ C(L,k)·2^{-k/2}. Maximizing the exponent
H(alpha) - (alpha/2)ln2 (alpha=k/L) gives max at alpha≈0.414 with value
n^{0.772}: so the biased-cell sum is n^{0.772}/1 = O(n^{0.772}) = o(n), and
dividing by n gives n^{-0.228} -> 0. Matches "tends to 0" as sublinear.
(Slightly SHARPER than the note's n^{3/4} = n^{0.75} figure; same conclusion.)

## Independent fold checks re-derived by hand

- Exact mean formula E[nu2/n] = (1/2n) sum_d (1 - K_w(2^pc(d);n)/C(n,w)) is
  correct: parity over a fixed m-set among weight-w strings
  #{odd} = (C(n,w)-K_w(m;n))/2. Reproduced the n=8 threshold: w=2 gives mean
  0.321<0.40, w=3 gives 0.446>=0.40 -> w*(8)=3, theta=0.375. MATCHES the
  measured column.
- n=4 C1 sensitivity (foundation of the whole K>1 reopening): h=0010 and
  h'=0100 have identical 2-gram histograms {00:1,01:1,10:1} but nu2 = 1 vs 2.
  Confirms K*(4) >= 2 and that S^2 is not determined by C_1. MATCHES banked
  K*(4)=2.

## The one genuinely live open surface

A real discrepancy exists between PASS3's settled figure and the workspace's
own imported data:
- PASS3 / CONCLUSION-PASS2: K*(n) = floor(n/2), explicitly "n=7 -> 3 not 4".
- research/witness-hunt-n20-imported.txt (still on disk) and the weakened
  target R-budget-n32: K*(7) = 4 = ceil(7/2).

For even n, floor = ceil so this is invisible; it bites only at ODD n (7,9,11,
13,15,17,19), exactly where PASS3 claims a correction. This is a
definition-dependence (directive 40 flagged three readings diverging past
n=8). It should be settled with the canonical oracle before being cited, but
it does not touch the threshold conclusion.

## Bottom line

No counterexample found. Every small, checkable, pure-Boolean or elementary
commitment I could hand-verify is correct, including the shared engine of the
two open lemmas. The honest positive outcome of this refutation attempt is a
*bounded* statement: the engine is sound on everything checkable, so the two
open lemmas are open only through the true pair-count, not through a false
bound. The refuter method's own oracle (find_counterexample on a small TPTP
collapse claim) is documented in code/refute/.
