# Scholar: A₂ = Θ((log n)²) confirmed exactly — reconciling the capture's log-log fit

The adopted route `downset-row-code-distance-closed-form` flagged (first-step
task 2, and the approach file lines 95-98) that the exact closed form
predicts `A_2 = Θ((log n)²)`, which is STRONGER than the capture's measured
"`A_2 = O(n^{0.48})`" log-log fit — and that the two "should be reconciled".
No note on disk records that reconciliation. This note supplies it, by hand,
matching the measured capture values exactly.

## The closed-form characterisation of distance-2 pairs

The distance formula (claim `downset-row-intersection-meet-formula`, proved)
gives `|M_d △ M_{d'}| = 2^{pc(d)} + 2^{pc(d')} − 2^{pc(d∧d')+1}`. To equal 2:

- **Type A — two distinct powers of two.** `pc(d)=pc(d')=1`, `d≠d'`, so
  `pc(d∧d')=0`; distance `= 2+2−2 = 2`. So every unordered pair of distinct
  powers of two in `[2, n−1]` is a distance-2 pair: `C(k,2)` of them, where
  `k = ⌊log₂(n−1)⌋` is the number of powers of two in the range.
- **Type B — a 2-bit number and one of its bits.** `d = 2^a+2^b` (a>b), and
  `d'` is either single bit `2^a` or `2^b` of `d`. Then `pc(d)=2`,
  `pc(d')=1`, `pc(d∧d')=1`, distance `= 2²+2¹−2^{1+1} = 2`. (The route doc
  only wrote `{2^a, 2^a+2^b}`, missing that the HIGHER single bit `2^b` is
  also a partner; both give distance 2 — the symmetric partner `d'=2^b` is the
  one the hand recount below needs and the one that makes the numbers match.)

No other combination gives distance 2 (all distances are even and ≥2; a
distance-2 term in the enumerator requires total `2^{pc}+2^{pc'}`
−`2^{pc(∧)+1}` = 2, and only the two cases above solve it). Hence exactly

```
A_2(n) = C(k,2) + #{ {2^a, 2^a+2^b}, {2^b, 2^a+2^b} : 2≤2^a+2^b≤n−1, a>b }   (unordered)
```

## Hand verification against the capture's measured values

Counting Type A + Type B unordered pairs (d,d'), d<d', d,d'∈[2,n−1]:

**n=16** (powers 2,4,8 → k=3):
Type A: C(3,2) = {2,4},{2,8},{4,8} = **3**.
Type B: pairs {2ᵃ,2ᵃ+2ᵇ},{2ᵇ,2ᵃ+2ᵇ}: {3,2},{5,4},{6,4},{6,2},{9,8},{10,8},{10,2},{12,8},{12,4} = **9**.
A_2 = 3+9 = **12**  →  measured 12 ✓

**n=24** (powers 2,4,8,16 → k=4):
Type A: C(4,2) = **6**.
Type B: {3,2},{5,4},{6,4},{6,2},{9,8},{10,8},{10,2},{12,8},{12,4},{17,16},{18,16},{18,2},{20,16},{20,4} = **14**.
A_2 = 6+14 = **20**  →  measured 20 ✓

**n=32** (powers 2,4,8,16 → k=4):
Type A: **6**.
Type B: previous 14 + {24,16},{24,8} = **16**.
A_2 = 6+16 = **22**  →  measured 22 ✓

All three match the exact capture values (`code/out/fold_second_moment_capture.txt`:
A_2 = 12@16, 20@24, 22@32) exactly. So the closed form and the measured A_2
agree on the nose.

## Closed-form coefficient and the extended verification to n = 4096

For `n = 2^m` the closed form is exactly `A_2(2^m) = (m−1)(3m−4)/2`. Counting
Type A + Type B combinatorially: `P1(m) = C(m−1,2)` distinct powers-of-two pairs
in `[2,2^m−1]` (powers `2^1..2^{m−1}`); `P2(m) = (m−1)²` Type-B pairs (for each
`a ∈ {1..m−1}`, the `m−1` choices of `b ≠ a` with `2^a+2^b ≤ 2^m−1`). Sum:
`(m−1)(m−2)/2 + (m−1)² = (m−1)(3m−4)/2`. This matches the executed brute-force
distance distribution at **every** recorded n = 16..4096:

| n = 2^m | m | C(m−1,2) | (m−1)² | closed form | brute (capture) |
|---|---|---|---|---|---|
| 16 | 4 | 3 | 9 | 12 | 12 |
| 32 | 5 | 6 | 16 | 22 | 22 |
| 64 | 6 | 10 | 25 | 35 | 35 |
| 128 | 7 | 15 | 36 | 51 | 51 |
| 256 | 8 | 21 | 49 | 70 | 70 |
| 512 | 9 | 28 | 64 | 92 | 92 |
| 1024 | 10 | 36 | 81 | 117 | 117 |
| 2048 | 11 | 45 | 100 | 145 | 145 |
| 4096 | 12 | 55 | 121 | 176 | 176 |

（The n=24 point, 20, is not in the powers-of-two table but is verified by the
hand count above.) The companion note `reconcile_a2_closed_form.md` records the
same extended verification; this is the canonical reconciliation.

## Why this is the right growth, and what the "O(n^0.48)" fit was

- **Type A contributes `C(k,2) = ⌊log₂(n−1)⌋²/2`.** Type B: for each 2-bit
  `d = 2^a+2^b ≤ n−1`, between 1 and 2 partners; the count is again
  `~ (log₂ n)²/2` (there are `k²/2` pairs with a>b, times ~one partner each
  once range effects are counted). So `A_2(n) = Θ((log n)²)` — exact.
- The capture's "log-log exponent 0.480 over n=16..4096" is a power-law fit of
  a `(log n)²` curve, which looks like a power law over a short span and
  decays monotonically as n grows (`A_2/n^0.48` keeps dropping; the exponent
  would drift to 0). The `A_2/n²` and `A_2/n` monotone decay in the capture
  are real and are exactly what `(log n)²` predicts. There is **no
  contradiction**: the fit was a normalization artifact, not a growth law.

## Consequence for condition (C)

`A_2 = Θ((log n)²)` is even better than the earlier `O(n^{0.48})` read for the
`F_n(z) = O(n)` geometry theorem: the distance distribution is concentrated at
sub-logarithmic-in-log scales, so the enumerator's off-diagonal bulk is killed
even faster. The geometry half (C) stands, and the arithmetic heart (A) —
`E[S(n)²] = O(n)` for the real prime h — remains the single open input.

```claim
id: a2-is-theta-log-squared-confirmed
statement: >
  The number of distance-2 row pairs of the SUPPLY fold, A_2(n), equals exactly
  C(k,2) plus the count of pairs {2^a,2^a+2^b} and {2^b,2^a+2^b} (a>b, both ≤
  n−1) with k=⌊log₂(n−1)⌋; this is Θ((log n)²). Hand-counted A_2 = 12, 20, 22
  at n=16, 24, 32; and the powers-of-two closed form A_2(2^m)=(m−1)(3m−4)/2
  matches the executed brute-force capture at every n=16..4096
  (12,22,35,51,70,92,117,145,176) identically.
hypotheses: none — pure combinatorics of the row set M_d={n−1−d+o:o⊆d}, d∈[2,n−1].
holds-here: yes
status: checked-by-hand against the executed exact capture (fold_second_moment_capture.txt);
  n=16,24,32 by brute-set hand count, n=16..4096 by the exact closed-form coefficient;
  the closed form follows from the proved distance formula
  (downset-row-intersection-meet-formula); a full all-pairs n=8..256 machine re-count is
  first-step task 2 of the adopted route (scripts on disk, not yet run in full)
bearing: reconciles the capture's "A_2=O(n^{0.48})" log-log fit with the route's
  predicted A_2=Θ((log n)²) — the fit was a power-law artifact, growth is
  quadratic-in-log, strengthening the F_n(z)=O(n) geometry theorem (C); A_2 reads
  the dyadic-lag autocorrelation of the switch sign u_j=chi(q_j)chi(q_{j+1}).
anchor: research/notes/a2_theta_log_squared.md
follows-from: downset-row-intersection-meet-formula
answers: fold-second-moment-condition-C (part: the A_2 reconciliation)
```
