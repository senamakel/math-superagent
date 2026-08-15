# Dyadic half-step fold: exact structural reason the combinatorial converse dies

Directive 68 item 3 / TASK B. The F2 transfer converse — "balanced AND anti-dyadic
h ⟹ ν₂ = wt(Phi h) ≥ c·m" — is machine-refuted by the **half-step string**
`h = 1^k 0^k` (m = 2k), which is balanced (wt h = m/2) and maximally anti-dyadic
(≥ m/2 from every 2^a-periodic string) while the fold collapses. This note states
the exact mechanism and the provable closed form.

## Conventions (locked)

n = m+2; fold matrix Phi_n has rows k = 2..n-2 (tail cells, k = 2..m), cols
j = 2..n-1 (m = n-2 row-1 halved gap bits), entry (k,j) =
[C(k-1, j-(n-k)) mod 2] if j in [n-k, n-1]. The fold of h at depth row k is the
mod-2 XOR over h[m-k..m-1] with Pascal-row-(k-1) mod-2 weights (Lucas: offset i
selected iff (i & (k-1)) == i).  ν₂ = wt(Phi h) = # tail rows whose fold = 1.

## Exact closed form (verified)

For `h = 1^k 0^k`, m = 2k, writing a depth row as K = k+1+δ (δ = 0..k-1; K ranges
2..m), the contributing h=1 positions are i = 0..δ (the window [m-K..m-1] =
[2k-(k+1+δ) .. 2k-1] = [k-1-δ .. 2k-1]; the h=1 positions that fall in the
window are exactly those with offset-from-right-edge i ≤ δ).  The exact value
is:

```
fold_bit(K) = #{ i ∈ [0, δ] : (i & (k+δ)) == i }  (mod 2)
```

verified for all k = 1..200 (full row set, 0 mismatches vs the direct matrix).

## Mechanisms

**Submask-count parity.** fold_bit(K) = |{i ≤ δ : i ⊆ (k+δ)}| mod 2.

**Power-of-two collapse (the provable fact).** For k = 2^a, δ ∈ [0, 2^a − 1]:
k+δ = 2^a + δ has bit a set; a submask i with bit a set would be ≥ 2^a > δ, so
only i ⊆ δ (low part) qualify, and i ⊆ δ forces i ≤ δ automatically. Hence the
count is the number of submasks of δ, which is 2^{popcount(δ)} — odd iff δ = 0.
So **for k a power of two, the fold fires exactly at δ = 0 (row K = k+1 = m/2+1),
i.e. wt(Phi h) = 1 exactly.** Machine-confirmed: wt=1 ⟺ k a power of 2 for all
k = 1..1024.

**Corollary (why the converse dies):** The half-step 1^{2^a} 0^{2^a} is the
probe's own survival type — balanced (exactly m/2 ones) and > 0.2m from every
periodic string (distance m/2, the probe's threshold) — yet wt(Phi h) = 1
(ratio 1/m = 1/2^{a+1} → 0), not ≥ c·m.  The claimed quantitative converse
"supra-dyadic ⟹ ν₂ linear" is FALSE as a universal statement; the only theorem
that survives is the power-of-2 collapse side (dyadic-collapse-proved).

## Part (a): wt(Phi h) not always 1

- Exactly 1 iff k a power of 2 (k = 2,4,8,16,32,64 in range; k = 2^a up to 1024
  verified).  Ratios 1/m = 1/2^{a+1} → 0.
- Always a power of two (verified k = 1..1024).
- Non-power-of-two deviations are powers of two: k=3→2, k=5→4, k=6→2, k=9→8,
  k=10→4, k=12→2, ... (divide accordingly; measured, not proved).

## Part (b): fold image is small and structured

For k a power of two the image is a single row: K = k+1 (the center depth,
m/2+1).  Generally the firing offsets δ are the subset of [0,k) with
#{i ⊆ (k+δ), i ≤ δ} odd — a sparse set whose offsets-from-center are
powers-of-2-separated (step divides a power of two); numerically the image is
tiny (|image| ≤ 2^{floor(log2 k)}) vs the m-1 scanned rows.

## Part (c): other block structures

Symmetric two-block `1^k 0^k` is the collapse witness.  Unequal halves
`1^k 0^{ak}` also give very small weights (1 for k power of 2 at a=2,3; e.g.
1^k0^2k m=4k → 1).  Four-block `1^k 0^k 1^k 0^k` re-collapses to wt 1 at
k power of 2 (m = 4k).  Cyclic rotation of the half-step does NOT collapse
(rotations destroy the clean window-BC structure: wt up to m/2), so the block
BOUNDARY at the quarter/center positions — not mere balance — is what kills the
fold weight.  (Computed, not proved.)

## What survives

- `dyadic-collapse-proved` (the power-of-2 collapse side) still holds.
- The half-step family is a family of balanced, anti-dyadic strings that
  OPTIMALLY collapse the fold — the sharpest counterexample to the converse.
- Not claimed here: a parity of wt for general k, or the full classification of
  which block boundaries fire.  Claimed: the power-of-2 theorem (closed form +
  submask-count proof) and the exact counterexample.

```claim
id: dyadic-halfstep-fold-power2-collapse
statement: For the F2 fold matrix Phi_n (rows k=2..n-2, cols j=2..n-1, entry
  C(k-1,j-(n-k)) mod 2, m = n-2), the half-step string h = 1^a 0^a (m = 2a)
  with a = 2^b a power of two has fold weight exactly wt(Phi h) = 1, and the
  fold fires exactly at the center depth row k = a+1 = m/2+1.  (Forward
  direction only: a power-of-two length forces the single-center collapse.)
hypotheses: h the halved-gap mod-4 switch bit over the fixed row-1 window
  [2,n-1]; F2; |a-b|/2 = (a/2) XOR (b/2) mod 2 (rule90-interior-xor, proved);
  the fold matrix convention of lib.rule90fold / kernel_characterize.
holds-here: yes — the half-step is the F2 transfer converse's own witness type
  (balanced, anti-dyadic), so this theorem pins the collapse mechanism exactly.
proof: write a depth row K = a+1+delta (delta = 0..a-1).  The contributing
  h=1 positions in the Pascal window [m-K..m-1] are exactly offsets i = 0..delta
  from the right edge, so the fold bit is #{i in [0,delta] : (i & (a+delta))==i}
  mod 2 (verified identical to the direct matrix for all a = 1..200, every row).
  For a = 2^b and delta in [0, 2^b - 1], a+delta = 2^b + delta; any submask i
  with bit b set is >= 2^b > delta, so only i subseteq delta (low part) qualify,
  and in that part i subseteq delta implies i <= delta.  Hence the count is the
  number of submasks of delta, 2^{popcount(delta)}, which is odd iff delta = 0.
  So the fold fires exactly at delta = 0 (row K = a+1), i.e. wt = 1.
status: proved (closed-form submask-count identity; the forward direction)
bearing: the exact structural reason the combinatorial F2 converse dies — the
  half-step is balanced AND maximally anti-dyadic yet collapses to fold weight 1
  at power-of-2 length; strengthens asserted claim spad-nondegenerate-linear-refuted
  by giving the collapse a closed-form mechanism.  Does not bear on the primes:
  nu2 >= c*n reverts to abgs-2011-s9-mod4-switch-limit-open.
anchor: research/notes/dyadic-halfstep-fold.md, code/dyadic/halfstep_depthbound.py,
  code/out/dyadic_halfstep_large_DEPTHBOUND.captured.txt
answers: spad-nondegenerate-linear-refuted
```

```claim
id: dyadic-halfstep-fold-classification-checked
statement: For the half-step string h = 1^a 0^a (m = 2a) over the F2 fold matrix
  Phi_n, wt(Phi h) = 1 iff a is a power of two, and wt(Phi h) is always a power
  of two (deviations are powers of two: a=3->2, 5->4, 6->2, 9->8, 10->4, 12->2).
hypotheses: same fold matrix, window and parity convention as
  dyadic-halfstep-fold-power2-collapse.
holds-here: yes — this is the converse/classification that would make the
  half-step's collapse exactly-when-power-of-two; it is what the proved forward
  claim alone does not deliver.
proof: none — machine-verified for all a = 1..1024 against the direct fold
  matrix; the deviations being powers of two is measured, not proved.
status: checked (numerical, a <= 1024)
bearing: the CONVERSE of the power-of-two collapse, NOT proved.  Together with
  dyadic-halfstep-fold-power2-collapse it shows the half-step reaches fold
  weight 1 precisely at power-of-two length, but "iff" and "always a power of
  two" are only machine-sealed to 1024 and must not be reported as proved.
anchor: research/notes/dyadic-halfstep-fold.md, code/dyadic/halfstep_depthbound.py,
  code/out/dyadic_halfstep_large_DEPTHBOUND.captured.txt
```

## Files

- `code/dyadic/halfstep_depthbound.py` — computes part (a)(b)(c), prints the
  depth bound m explicitly (Directive 67 rule 3), streams rows one at a time.
- `code/out/dyadic_halfstep_large_DEPTHBOUND.captured.txt` — its capturing run,
  EXIT_CODE=0.
- Original captures `dyadic_halfstep.captured.txt` and
  `dyadic_halfstep_large.captured.txt` NOT overwritten.
