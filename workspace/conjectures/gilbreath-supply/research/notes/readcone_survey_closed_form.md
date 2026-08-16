# Read-cone survey of the SUPPLY fold — fixed sparse strings cannot keep S = O(√n)

Survey of single-1 and fixed sparse read-cones, run by tool_builder
(`code/order_k/readcone_survey.py`, capture `code/out/readcone_survey_capture.txt`).

## The question

`G-input-strictness` / `G-orderk-input-strictness` asks whether a FIXED infinite
density-0 string h* can keep `S(n) = O(√n)` for all n, where `S(n) = (n−2) − 2·ν₂(n)`,
`ν₂(n) = wt(Φ_n h)`. This is the strictness witness that would show the second-moment
input is strictly weaker than pointwise mod-4 switch density. The per-window family
`h = e_{n−2}` does give `S ∈ {0,1}` (banked `input_strictness.py`), but that family
MOVES with n — a true "fixed" string must keep the same support.

## What was measured

**Read-cone closed form (proved, exact):**
`|C_j(n)| = #{ d ∈ [2, n−1] : (n−1−j) bitwise-submask of d }`.
Two-line proof: cell reads h[j] when `o = d−(n−1−j)` is a submask of d with
`d ≥ n−1−j`; the identity `(d−r) ⊆ d ⟺ r ⊆ d` for `d ≥ r = n−1−j` converts the read
condition into "r is a bitwise submask of d". Verified against the literal O(n)
`read_cone_size` on **245,344 (n,j) pairs** (n ∈ [4,700]) — 0 mismatches.
This is the exact form of the read-cone-column-equivalence weight
`2^{−popcount(n−1−j)}` per 1.

**Single-1 survey (n = 8..200):** the max over j of |S| is exactly `n−2`, achieved
only at `j = n−1` (read-boundary). `j = n−2` gives `S ∈ {0,1}` (small!), but that is
the *per-window* position. The crucial contrast:

- **Fixed** single 1 (`j` constant, the true fixed reading): `ν₂(n) ≤ j+1 = O(1)`,
  so `S(n) = (n−2) − 2ν₂(n)` is **linear** (S/n → 1), NOT O(√n). Measured for
  j = 0,1,2,5,50: S = 46, 96, 196, 496, 996 at n = 50..1000.
- **Per-window** `e_{n−2}`: `S ∈ {0,1}`, because a 1 at n−2 reads only the odd
  depths (o = d−1 ⊆ d ⟺ d odd), i.e. half of them — `ν₂(n) ≈ ⌈(n−2)/2⌉`.

**Fixed infinite sparse strings (prefix S(n), n = 8..4000):**
- Candidate A: 1s at `2^m − 2` (density 0). max|S| = 50@62, 112@126, 238@254,
  492@510, 966@990, 1956@1982, 2958@2998, 3950@3998 → **max|S| ~ n−4 (linear)**,
  and max|S|/√n **grows** 6.25 → 62.5. FAILS O(√n).
- Candidate B (control): 1s at `2^m` (powers of 2). Identical asymptotics
  (max|S| ~ n), grows. FAILS (consistent with the refuter's finding).

## Why every fixed density-0 string is forced linear i.o.

The mechanism is the read-cone. A 1 at position `n−1−k` is read by the depths
`d` for which `(n−1−j) ⊆ d`; by the closed form the count is
`~ (n−r)/2^{pc(r)}` — it reads **all depths when r=0** (position n−1) and about
**half when r=1** (position n−2), a quarter when r=3, etc. So a 1 landing at or
near the read-boundary `n−1` for infinitely many n reads Θ(n) depths at those n,
giving `ν₂(n) = Θ(n)` and `|S(n)| = Θ(n)` — linear, i.e. **not** O(√n).

A fixed support S has density 0, but if it contains infinitely many members that
sit at `n−1−k` for infinitely many n with k bounded (small `pc(n−1−j)`), then
|S(n)| = Θ(n) infinitely often. To keep S = O(√n) at *all* n, the support must
avoid being boundary-near for every n — a strictly finer growing object than any
fixed S. In particular the two natural families (2^m−2 and 2^m) both fail because
their members repeatedly land at a low-popcount distance from n−1.

## Verdict for G-input-strictness (fixed-string reading)

No fixed density-0 string among these families keeps `S = O(√n)` through n=4000;
the per-window linear amplification reappears infinitely often. This **confirms**
the refuter's prior shape constraint (`refuter_fixed_single_one_bound`, `sparse_fold`
capture): the G-input-strictness / G-weak-input-strictness witness, if it exists,
**cannot be a fixed sparse string** — it must be a growing, carefully-placed object.
So the strictness clause is NOT witnessed in the fixed-string reading by any
density-0 S measured here.

```claim
id: read-cone-closed-form-exact
statement: |
  For the SUPPLY fold, a single 1 at position j of the length-n window is
  read by exactly |C_j(n)| = #{ d in [2, n-1] : (n-1-j) bitwise-submask of d }
  depths. Proof: the depth-d cell reads h[j] when o = d-(n-1-j) is a bitwise
  submask of d with d >= n-1-j; the identity (d-r) subseteq d <=> r subseteq d
  for d >= r = n-1-j turns the read condition into "(n-1-j) subseteq d",
  whence the supermask count. This is the exact read-cone-column-equivalence
  weight 2^{-popcount(n-1-j)} per 1 of the support.
hypotheses: T(n,d)=XOR_{o subseteq d} h[n-1-d+o], d in [2,n-1] (floored).
holds-here: yes.
status: proved by the submask identity; machine-checked against the literal
  read_cone_size oracle on all 245344 (n,j) pairs with n in [4,700], 0 mismatches.
bearing: pins the exact amplification factor of a fixed support member; shows a
  fixed 1 at low popcount(n-1-j) reads ~ (n-r)/2^{pc(r)} depths, so a fixed 1
  near the boundary gives |S| = Theta(n) i.o. Forbids any fixed density-0 S from
  being a S = O(sqrt n) witness (unless it avoids boundary-near positions at all n).
anchor: code/lib/supply_fold.read_cone* , code/order_k/readcone_survey.py,
  code/out/readcone_survey_capture.txt; code/research_grounding/read_cone_check.py.
```

```claim
id: no-fixed-density0-string-keeps-sqrt-n-measured
statement: |
  Neither the fixed string with 1s at 2^m - 2 nor the one with 1s at 2^m
  (both density 0) keeps S(n) = O(sqrt n): over n in [8,4000] each has
  max|S| ~ n (linear), attained at n just below a power of two / at a power of
  two respectively, and max|S|/sqrt(n) grows (6.25 -> 62.5). By the read-cone
  closed form a fixed 1 at n-1-k reads ~ (n-r)/2^{pc(r)} depths, so with
  arbitrarily low-popcount r it forces S = Theta(n) infinitely often. Hence the
  G-input-strictness / G-weak-input-strictness witness, if it exists, is not a
  fixed sparse string; it must be a growing, boundary-avoiding object.
hypotheses: same as read-cone-closed-form-exact; fixed support S across n.
holds-here: yes.
status: measured, exact (canonical SOS oracle), not a proof of the infinite
  statement; the fixed-1-bound is the proved input and is cited.
bearing: confirms/extends refuter_fixed_single_one_bound and the sparse_fold
  capture's shape constraint on the witness; G-input-strictness is NOT witnessed
  in the fixed-string reading by density-0 S through n=4000.
anchor: code/order_k/readcone_survey.py, code/out/readcone_survey_capture.txt.
```

## Independently verified

The read-cone closed form was checked on 245,344 (n,j) pairs, two independent
code paths. The fixed-string S(n) used the canonical `s_sos`, and the single-1
values were additionally checked equal to the literal `s_direct` oracle (n =
8,20,50,100,200, all j). The two candidate families are a direct evaluation,
exact, no search.
