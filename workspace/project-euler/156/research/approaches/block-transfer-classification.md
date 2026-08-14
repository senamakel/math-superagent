# Approach — general-m residue identity and the unique self-similarity scale (base b)

```approach
idea: The solution set of f(n,d)=n is classified by the general-m residue
identity f_d(k·b^m + x) − f_d(x) = k·m·b^{m−1} (k<d, 0≤x<b^m). At m=b the
increment equals the translation, so x ↦ k·b^m + x is a bijection of the
solution set; this is the UNIQUE scale with that property, and it gives s(d)
as a closed-form sum over one seed block.
mechanism: (base b) f_d(k·b^m+x) − f_d(x) = k·m·b^{m−1}. The translate
k·b^m+x is a fixed point exactly when f_d(x) = x + k·b^{m−1}(b−m), so for a
fixed point x this holds iff b = m (k≥1). Hence in base 10, m=10 is the one
scale where blocks transfer: f_d(x)=x ⟺ f_d(k·10^10+x)=k·10^10+x for
k≤d−1. With the bound n ≤ d·10^10 (Khovanova–Marton Prop 9.1), the full
solution set is ∪_{k=0}^{d−1} (k·10^10 + S_0(d)), and
s(d) = d·Σ_{x∈S_0(d)} x + (d(d−1)/2)·10^10·|S_0(d)|,  S_0(d)={x<10^10:f(x,d)=x}.
The whole computation collapses to enumerating the small seed set S_0(d)
inside [0,10^10) (≈86k f-evaluations total) plus this closed-form sum.
status: adopted
precedent: grounded — the m=10, k=1 shift is K&M arXiv:2305.10357 §4 / AMM
132(8) 2025 §4 (verbatim: "f_d(x+10^10)=f_d(x)+10^10"); the general-m
identity, the closed-form s(d) formula, and the uniqueness of m=b are NOT in
K&M or any source found (novelty-check note on disk). No closed form for
S_0(d) exists; it remains an enumerated object in all sources.
first-step: implement `code/block_transfer.py` that (a) enumerates S_0(d) for
d=1..9 by the existing jump iterator restricted to [0,10^10), (b) rebuilds
each full solution set as ∪_k (k·10^10 + S_0(d)), (c) computes s(d) by the
closed form, and (d) verifies bijection + s(d) against the 9 files
code/out/solutions-d*.txt and the total 21295121502550 already on disk.
```

## The theorem

**Residue identity (general m, base b).** For 1 ≤ d ≤ b−1, 1 ≤ k ≤ d−1,
m ≥ 1, and every 0 ≤ x < b^m:

    f_d(k·b^m + x) − f_d(x) = k·m·b^{m−1}.

*Proof.* f_d(N) = Σ_{j≤N} c_d(j), c_d(j) = # of digit-d in j. For
N = k·b^m + x with 0 ≤ x < b^m, every j in [k·b^m, k·b^m+x] writes as the
single digit k followed by the m digits of j−k·b^m (x padded to m digits).
Since 1 ≤ k ≤ d−1 < d, the high digit k ≠ d contributes c_d(k)=0; the m low
positions run through 0..x and, as d ≥ 1 so leading zeros carry no d,
contribute f_d(x). Hence f_d(k·b^m+x) = f_d(k·b^m−1) + f_d(x).

Now [0, k·b^m−1] is the union over high digits h ∈ {0,…,k−1} of m low digits
running 0..b^m−1. The high position never equals d (d ≥ k > h); each low
position, over each full cycle of b^m values repeated k times, contains d
exactly b^{m−1} times per repetition, so k·b^{m−1} times. Over m positions:
k·m·b^{m−1}. ∎

**Uniqueness of the self-similarity scale.** The residue identity gives

    f_d(k·b^m + x) = f_d(x) + k·m·b^{m−1}.

For a fixed point x (f_d(x)=x) the translate k·b^m+x is a fixed point iff
x + k·m·b^{m−1} = k·b^m + x, i.e. m = b (k ≥ 1). So **m = b is the only
scale at which solution sets transfer by translation**; in base 10 that scale
is 10. This is the structural reason the number 10 (= base) appears in the
problem's block decomposition, and it proves K&M's "periodicity modulo 10¹⁰"
as a corollary (their k=1, m=10 special case, stated there in words).

**Closed form (base 10, m = 10).** For 0 ≤ x < 10^10 and 1 ≤ k ≤ d−1:

    f_d(k·10^10 + x) = f_d(x) + k·10^10,  so  f_d(x)=x ⟺ f_d(k·10^10+x)=k·10^10+x.

With S_0(d) = {x < 10^10 : f_d(x)=x} and the bound n ≤ d·10^10, the solution
set is the disjoint union ∪_{k=0}^{d−1} (k·10^10 + S_0(d)), and

    s(d) = d·Σ_{x∈S_0(d)} x + (d(d−1)/2)·10^10·|S_0(d)|.

**Controlled break at k = d.** Here c_d(d)=1, so the same computation gives
f_d(d·10^10+x) = f_d(x) + d·10^10 + x + 1 > d·10^10+x: no solution has
n ≥ d·10^10 (the sampled "break" in code/pattern_residue_exact.py).

## Verification against the run's own data

The classification is visible in and checked against the complete solution
files code/out/solutions-d*.txt (661 solutions, produced independently by the
jump iterator). Seed sizes |S_0(d)| and totals:

| d | \|S_0(d)\| | blocks | total | s(d) |
| --- | --- | --- | --- | --- |
| 1 | 84 | 1 | 84 | 22786974071 |
| 2 | 7 | 2 | 14 | 73737982962 |
| 3 | 12 | 3 | 36 | 372647999625 |
| 4 | 12 | 4 | 48 | 741999999540 |
| 5 | 1 | 5 | 5 | 100000000000 |
| 6 | 12 | 6 | 72 | 2434703999430 |
| 7 | 7 | 7 | 49 | 1876917059570 |
| 8 | 43 | 8 | 344 | 15312327487352 |
| 9 | 1 | 9 | 9 | 360000000000 |

Closed-form check: d=2, ΣS_0 = 1868991481 → s(2)=2·1868991481+10^10·7 =
73737982962 ✓; d=7, ΣS_0 = 58131008510 → s(7)=7·58131008510+21·10^10·7 =
1876917059570 ✓. Grand total = 21295121502550, matching code/solution.py.

## What is new vs. what is K&M's

- **K&M (arXiv:2305.10357 §4, AMM 2025 §4), priority theirs:** the m=10, k=1
  shift identity, membership equivalence, equal block counts, and (with their
  Prop 9.1) the d-block decomposition.
- **New here (not in K&M, not found in any searched source):** (1) the
  general-m base-b residue identity k·m·b^{m−1}; (2) the uniqueness of the
  scale m=b; (3) the closed-form sum s(d) = d·ΣS_0 + (d(d−1)/2)·10^10·|S_0|;
  (4) the verified seed sizes [84,7,12,12,1,12,7,43,1] and ΣS_0 data.
- **Open in all sources:** S_0(d) has no closed form and is still enumerated;
  the seeds are a finite irreducible object (the jump iterator finds them all
  in ≈86k f-evaluations). See
  research/notes/novelty-check-block-transfer-classification.md.
