# Exact maximal safe set of the halved |a-b| operator — excess coordinates

Approach: `research/approaches/excess-maximal-invariant-set.md`, first-step.
Tool: this run. All exact integer arithmetic, no floats. Capture:
`code/out/excess_maximal_set.captured.txt` (primary),
`excess_maximal_set_verify.captured.txt`, `excess_maximal_set_probe.captured.txt`,
`excess_maximal_set_prefix.captured.txt`, `excess_maximal_set_synthesis.captured.txt`.

## The object and the recursion

Halved coordinates: every interior entry of every row is even, so
`h_k(i) = A_k(i)/2` for `i ≥ 1` is well-defined and
`h_{k+1}(i) = |h_k(i) - h_k(i+1)|` (halving commutes with |·|). Safety
(`A_k(1) ∈ {0,2}`) is `h_k(1) ≤ 1`. The maximal safe set of width-K windows is
the exact backward-preimage fixed point (Blanchini/Rakovic–Kerrigan–Kouramas–
Mayne, specialised to the acyclic causal cone):

```
S_1 = { w : w_1 ≤ 1 }
S_K = { w ∈ [0..M]^K : w_1 ≤ 1 and H(w) ∈ S_{K-1} },  H(w)_i = |w_i - w_{i+1}|
```

`S_K` is the UNIQUE maximal set of width-K windows safe for K rows. Cost at
M=3, K≤10 is ≤ 4^10 = 1,048,576 states per backward pass — trivial.

## Step 1 — load and verify the halved first row

From `witnesses.json`: `A_1 = 1,2,2,4,2,4,2,4,6,2,6,4`.
Halved `h_1` (i≥1) = `(1,1,2,1,2,1,2,3,1,3,2)`.
Matches problem.md's A_1 halved to 9 entries exactly.
Reproduction check: `A_2 = |A_1(i)-A_1(i+1)| = 1,0,2,2,2,2,2,2,4,4,2`,
exact match to problem.md.

## Step 3 — S_K sizes and membership of the real window

| K | |S_K| | real h_1(1..K) ∈ S_K | decision by forward oracle |
|---|---|---|---|
| 1 | 2 | yes | yes |
| 2 | 5 | yes | yes |
| 3 | 16 | yes | yes |
| 4 | 58 | yes | yes |
| 5 | 222 | yes | yes |
| 6 | 869 | yes | yes |
| 7 | 3438 | yes | yes |
| 8 | 13672 | yes | yes |
| 9 | 54518 | yes | yes |
| 10 | 217706 | yes | yes |

Backward recursion EXACTLY equals the independent forward oracle at every K
(`excess_maximal_set_synthesis.captured.txt`, rule 9/11). The real prime window
is in `S_K` for all K — a maximal-set certificate, strictly stronger than
forward simulation of one trajectory, re-deriving the known depth safety.

## Step 4 — shape extraction: the negative stabilization result

A raw-coordinate box guess `{w_1 ≤ 1, w_2 ≤ 2}` is REFUTED by the forward
oracle: there exist safe-prefix windows (e.g. (0,0,0,0,0,2,2)) that are unsafe,
and width-5 windows with `w_2 = 2` that are unsafe.

An apparent excess-coordinate stabilization (|S_K| projected
= 1,2,6,18,54,… = 2·3^{K-2}, a "full product box" over attainable excess
vectors) is an **attainability artifact**: excess projection `t=max(0,w-1)`
collapses `w=0` and `w=1` both to `t=0`, discarding exactly the distinction
(the far-tail `2`s that propagate leftward and destabilise) that decides
safety. `isFullProductBox` only says every excess *pattern* occurs among *some*
safe window; it does NOT say safety is a function of the excess vector. The
forward oracle is the authoritative refuter.

**Negative bound (falsifier (b) tripped): NO fixed finite prefix decides S_K.**
For every prefix length J=1..9 there is a window whose safe J-prefix extends to
an UNSAFE window:

```
J=1: (0,)  -> (0,2)  unsafe
J=2: (0,0) -> (0,0,2)  unsafe
...
J=9: (0,...,0) -> (0,...,0,2)  unsafe
```

So the constraint family does NOT stabilise to a bounded-prefix / bounded-shape
invariant within K≤10. Density `|S_K|/4^K` falls monotonically toward ~0.2076
(K=10) and the ratio `|S_K|/|S_{K-1}|` rises toward 4, i.e. nearly all of the
box is excluded as K grows — safety depends on the whole (growing) window, not
on a bounded prefix. There is **no width-uniform finite-prefix invariant of
S_K** to synthesise from this computation.

## Step 5 — sanity checks

- backward recursion == forward oracle: EXACT at every K (checked
  `excess_maximal_set_synthesis.captured.txt` row A).
- A_2 reproduced from A_1 by H.
- A window with `w_1=2` is never safe (leading 2 at row 1); all 8 width-3
  windows with `w_2=3` and `w_1≤1` are forward-unsafe (`|w_1-3|≥2>1`).

## Honest verdict

The deliverable is the **exact maximal-set certificate** (real window ∈ S_K for
all K, and S_K is the full backward-preimage fixed point — no over/under
approximation), plus the **recorded negative bound**: no compact finite-prefix
invariant of this class exists at widths ≤ 10, so the synthesis half of the
approach does not yield the target parametric invariant `A_k(1)∈{0,2}` from
this exact enumeration. This is a falsifier-(b) result, not a proof.
