# G-run-telescope machine-verified (claim `g-run-telescope-verified`)

```claim
id: g-run-telescope-verified
statement: >-
  For every d in [0, 2^14], the digital down-set ↓d = {o in [0,d] : o bitwise
  submask of d} is a disjoint union of maximal consecutive-integer runs, each of
  length exactly 2^g with g = nu2(d+1), in count exactly
  2^(popcount(d) - g), each of the form [m·2^g, (m+1)·2^g - 1]; and for any
  two-valued boundary r over {1,3} with h[j] = [r_{j+1} != r_j], for every run
  [u,v] of ↓d the telescoping identity XOR_{o in [u,v]} h[pos+o] =
  [r_{pos+u} != r_{pos+v+1}] holds. Machine-verified by brute submask
  enumeration (d = 0..2^14, every d, vs the closed-form partition), and by
  element-by-element XOR vs prefix-XOR, on the real prime-residue h (d<=2^10
  brute, 2^14 prefix) and 6 random-h controls — ALL PASSED.
hypotheses: >-
  h any {0,1} string over a two-valued boundary (prime case r = q_j mod 4);
  g = number of trailing 1-bits of d; d <= 2^14 = 16384; positions <= 101; 6
  random trials (default; --trials/--dmax-full adjustable).
holds-here: yes — this is the exact fold-cell reading (submask-XOR of the sliding window) that the adopted dyadic-gap-character-correlation reduction uses, on the real prime-residue string and random controls.
status: checked (verified numerically, exact arithmetic; not a proof of SUPPLY)
bearing: >-
  Grounds the G-run-telescope reduction step of the adopted approach
  dyadic-gap-character-correlation: the fold cell T(n,d) = XOR over submasks
  becomes XOR over O(2^(popcount-g)) run-endpoint character products, each an
  adjacent-residue mismatch. Also fulfils the verification contract of
  lib/submasks.py (downset_runs/trailing_ones/boundary_from_h were previously
  unverified). It is not the dyadic-gap-correlation bound itself and touches
  none of the five closed doors.
anchor: code/gfold/g_run_telescope_verify.py; code/out/g_run_telescope_verify.captured.txt
```

Executed this attempt: `code/gfold/g_run_telescope_verify.py` (already written
on disk, previously marked UNRUN at `code/out/commands.log:7139`), capture
`code/out/g_run_telescope_verify.captured.txt`. This is the adversarial
verification of the two structural facts the adopted approach
`dyadic-gap-character-correlation` rests on.

## C1 — down-set run structure (d = 0..16384, every d)

For g = ν₂(d+1) = number of trailing 1-bits of d, the digital down-set
↓d = {o ∈ [0,d] : o bitwise submask of d} partitions into maximal
consecutive-integer runs, each of length exactly 2^g, in count exactly
2^(popcount(d) − g), each a block [m·2^g, (m+1)·2^g − 1] for even m.
Checked by brute submask enumeration (`downset_brute`) vs the closed-form
`downset_runs` partition, plus the run-length/count/alignment asserts, for
**all 16385 values of d in [0, 2^14] — ALL PASSED**. (The earlier <1s timing
of this block was confirmed in isolation.)

## C2 — telescoping identity (real prime-residue h AND 6 random controls)

For any two-valued boundary r over {1,3} with h[j] = [r_{j+1} ≠ r_j], and any
run R = [u, v] of ↓d:
XOR_{o∈R} h[pos+o] = [r_{pos+u} ≠ r_{pos+v+1}].

- Real prime h (q_j mod 4), brute element-by-element XOR oracle:
  d = 0..1024 × 51 positions = **52275 (d,pos) pairs, PASSED**.
- Real prime h, prefix-XOR (associativity) full sweep:
  d = 0..16384 × 101 positions = **1654885 pairs, PASSED**.
- 6 random h controls (seed 12345), brute and prefix routes:
  **313650 + 9929310 pairs, PASSED**.

Both formulations agree with the down-set partition (fold over runs = brute
fold over the whole down-set).

## Negative control

The run-count assert uses `2^(popcount(d) − g)`; the brute `runs_of_set`
count against `len(fast)` — a wrong divisor in the formula would assert-fail
on the first d with popcount ≠ g. None did, over all 16385 d.

## What this settles

- The run-structure lemma (length 2^g, count 2^(popcount−g), block form)
  holds for every d ≤ 2^14 — the formula claimed in the approach and in
  `research/BACKWARD.md`/`BLUEPRINT.md` as `G-run-telescope`.
- The telescoping identity is exact on the real prime-residue string and on
  random strings, over the full d-range the fold uses (d ≤ 2^14 with
  positions up to 101, i.e. n up to ~2^14 + 100).
- `lib/submasks.py`'s contract ("each function is verified against brute
  enumeration in code/gfold/g_run_telescope_verify.py") is now actually
  fulfilled; the module's `downset_runs`/`trailing_ones`/`boundary_from_h`
  are load-bearing for the adopted character-correlation line and were
  previously unverified.

## Scope

- All checks are exact (set arithmetic, XOR, integer parity); no floats.
- Range: d ≤ 2^14 = 16384 for C1 and the prefix route; d ≤ 2^10 for the
  brute element oracle. positions ≤ 101; 6 random trials.
- Not a proof of SUPPLY and not a proof of the dyadic-gap-correlation
  bound; this grounds the reduction step only (evidence class: verified
  numerically, exact).
- The default run was changed from 30 to 6 random trials (30 × ~19 s ≈ 570 s
  over the 550 s tool budget); the identity is deterministic-algebraic, so
  one trial detects any systematic boundary bug; six is a full control set.
  `--trials` and `--dmax-full` are respected if a larger run is wanted.