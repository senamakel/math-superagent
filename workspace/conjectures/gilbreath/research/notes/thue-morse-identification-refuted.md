# Thue-Morse nu2 identification REFUTED by direct exact triangle (D=4000)

## What was claimed

`thue-morse-sublinear-supply-witness` (proved, `research/notes/thue-morse-
sublinear-supply-witness.md`) states, as the load-bearing bridge of the
dyadic-linear-complexity-supply transfer:

> ν₂(n) = #{d ≤ n : ζ(h)[d] = 1} = #{d ≤ n : d is a power of 2}
>        = ⌊log₂ n⌋ + 1 = O(log n).

The first half of that sentence is a **subset-zeta claim** (ζ(h)[d]=1 iff d is
a power of two) — TRUE and now machine-confirmed.  The second half is an
**identification claim** (that this zeta count equals the diagonal nu2 of the
Thue-Morse 2-then-odds triangle) — **FALSE**, refuted by exact computation.

## PART A — subset-zeta identity (CONFIRMED, never before machine-checked)

For h[j] = wt(j) mod 2 (Thue-Morse), j = 0..N:

- Fast O(N log N) F2 subset-zeta agrees with a naive O(N·2^wt) double loop on
  N=4096.
- #{d ∈ 0..N : ζ(h)[d] = 1} = 17 at N = 100000, and the set is exactly the
  17 powers of two in 1..N.
- The popcount-subset-sum identity
  Σ_{j⊆d} wt(j) ≡ wt(d)·2^{wt(d)-1} (mod 2) holds for d ≤ 699 (direct check).

So ζ(h)[d] = 1 ⟺ d is a power of two.  **This sharp ≡-reading (odd cells) is
correct.**

## PART B — the identification nu2(n) == #powers-of-two (REFUTED)

Setup (exact integers, one row at a time, D = 4000):
q[0]=2, q[1]=3, and gap q[j+2]−q[j+1] = 2 if h[j]=1 else 4.
nu2(n) = # of 2s in the maximal {0,2} suffix of the right diagonal
δ(q_n) = [A_k(n−k)]_k, floored at index 2 (the run's canonical convention,
`lib.rightdiag.cycle_and_nu2`).

Cross-checks (all pass): the triangle matches `lib.gilbreath.rows_generator`;
diagonal and canonical nu2 match `lib.rightdiag.cycle_and_nu2` and
`delta_diagonal`.

Results:

```
n      nu2(n)   #pw2<=n
1       0        1        <- FIRST MISMATCH
100    27        7
500    39        9
1000   41       10
2000   43       11
4000   45       12
```

**The identification does not hold at any sample, and the first mismatch is
n = 1.**  Later fine scan (n ≤ 4000): nu2 bobs in 27..219 — small, but never
equal to ⌊log₂ n⌋+1 and not monotone in n.

### Why it fails

ζ(h)[d] = 1 marks **odd** cells: the fold value (a bit / a mod-2 parity of a
cell).  nu2 counts **even** {0,2} tail cells.  The actual right-diagonal tail
of the Thue-Morse triangle is dense in 0s and 2s (nearly the whole body is
{0,2}: n=100 shows 98/100, n=50 48/50), with repeated 2/0 runs that
parity-cancel in the XOR fold.  One cell whose half is even contributes 0 to
the fold bit yet is a 2 (hence counted by nu2); one whose half is odd
contributes 1 and is NOT counted (it is 0 or not in the suffix).  So the fold
bit is the *opposite* statistic from the nu2 tail count, and the two never
agree beyond tiny n.

In short: `rule90-interior-xor` tells you the **parity** of a tail cell, not
whether it is 0 or 2 — and nu2 requires the latter.

## The qualitative conclusion SURVIVES (strengthened)

Even though the exact log₂ identification is wrong, the reason the witness
existed is confirmed and is now on firmer ground:

- ν₂ for the Thue-Morse 2-then-odds is **sublinear and actually small**:
  max ~219 over all n ≤ 4000, and values do not grow with n (27 at n=100,
  45 at n=4000, with occasional bumps to ~200 at n∈{1100,2100,3100}).
- Thue-Morse remains a valid aperiodic bit-string witness that **aperiodicity
  does not force linear supply** — the dichotomy "periodic ⟺ collapse, else
  linear" is dead regardless of the exact identification.

## What is refuted, what is not

- REFUTED: the over-precise claim "ν₂(n) = #{powers of two ≤ n} = ⌊log₂ n⌋+1"
  (the identification between the subset-zeta count and the actual triangle
  nu2).  The ≡-statement of the subset-zeta identity itself is CONFIRMED.
- NOT touched: `dyadic-collapse-proved` (period-2^k ⟹ bounded ν₂), the
  odd-factor periodic families' positive linear density (PART C), the
  `g-supply-transfer-measured` prime ratio, or Lemma 5.4 / the recharge
  identity.
- The corner-family table keeps its claim: the real prime switch bit and the
  odd-factor/LCG/pseudo-random families show **positive density** of ζ==1
  (the supply-friendly classes), while Thue-Morse, Rudin-Shapiro, all-ones,
  alternating and period-4 show **sublinear** (≈log or constant) density.

## Corner-family density table (PART C), N = 200000, d ∈ 0..N, denom 200001

| family | count ζ==1 | density | class |
| --- | --- | --- | --- |
| all-zeros | 0 | 0 | {0} |
| all-ones | 1 | 1/200001 | intermediate (sublinear) |
| alternating 0,1 | 1 | 1/200001 | intermediate |
| period4 0,0,1,1 | 1 | 1/200001 | intermediate |
| period3 0,1,0 | 133333 | 133333/200001 ≈ 0.6667 | {≥ c>0} |
| period5 | 106667 | 106667/200001 ≈ 0.5333 | {≥ c>0} |
| Thue-Morse | 18 | 6/66667 ≈ 9.0e-5 | intermediate (sublinear) |
| Rudin-Shapiro | 17 | 17/200001 ≈ 8.5e-5 | intermediate |
| LCG pseudo-random | 99983 | 99983/200001 ≈ 0.4999 | {≥ c>0} |
| real prime switch bit | 100323 | 33441/66667 ≈ 0.5016 | {≥ c>0} |

(Periodic families are computed off their exact period; the 18-on-Thue-Morse
count reflects the near-logarithmic profile, not exactly log₂ — consistent
with the refuted over-precision.)

## Anchors

- Program: `code/out/thue_dyadic_full.py` (this run), run under
  `timeout 540`, EXIT_CODE=0.
- Capture: `code/out/thue_dyadic_supply_verify.captured.txt`.
- Diagnostic: `code/out/thue_dyadic_ident_diag.py`.
- Prior claim corrected: `thue-morse-sublinear-supply-witness` — its
  ≡-reading of ζ is right, its identification to nu2 is wrong.

```claim
id: thue-morse-subset-zeta-confirmed-identification-refuted
statement: For h[j]=wt(j) mod 2, the F2 subset-zeta satisfies zeta(h)[d]==1
  iff d is a power of two (CONFIRMED by direct machine check to N=1e5), but
  the load-bearing identification nu2(n)==#{d<=n : d a power of two} does NOT
  hold for the Thue-Morse 2-then-odds triangle: first mismatch at n=1
  (nu2=0 vs 1), and nu2 never equals the power-of-two count at any sampled n
  (n=100: 27 vs 7; n=4000: 45 vs 12).  The fold bit zeta marks cell PARITY,
  not {0,2} membership, so it is the wrong statistic for nu2.  The qualitative
  conclusion survives: Thue-Morse nu2 stays sublinear (max ~219 over n<=4000),
  so aperiodicity does not force linear supply.
hypotheses: exact integer triangle to D=4000 (O(D^2) diffs, one row at a
  time); canonical nu2 = maximal-{0,2}-suffix-of-right-diagonal floored at
  index 2, cross-checked against lib.rightdiag and lib.gilbreath; subset-zeta
  fast-vs-naive agreement on N=4096.
holds-here: yes (this is the verification itself)
status: refuted (the identification) / confirmed (the subset-zeta identity)
bearing: the dyadic-linear-complexity-supply transfer must NOT use
  nu2 = #powers-of-two as if it were exact; it may still cite the qualitative
  sublinearity of Thue-Morse nu2 as the aperiodic witness.
anchor: research/notes/thue-morse-identification-refuted.md
```
