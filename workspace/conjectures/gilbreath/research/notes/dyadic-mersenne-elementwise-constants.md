# Elementwise structure of the Mersenne per-residue constants

**Pattern-finder finding — verified-numerically (conjecture, not proved).**
Refines `research/notes/dyadic-oddfactor-affine-modulus-lifting.md` from the
aggregate `sum c_r = 3^k - 3` to the *elementwise* shape of the per-residue
constants.

## Setup (same as the documented note)

2-then-odds sequence, gap = 2 if bit else 4, bits = **tail-1 word**
`[0]*(P-1)+[1]` of Mersenne period `P = 2^k - 1`. `nu2(n)` = #2s in the
maximal `{0,2}` suffix of the right diagonal `delta(q_n)` (body convention,
`lib.rightdiag.cycle_and_nu2`).

`nu2` is **per-residue affine mod P**: for each residue r mod P,
`nu2(n+P) - nu2(n) = c_r` constant. Define the half-constant array
`R_k[r] = c_r / 2`.

## Elementwise structural facts (all exact, k=2..10)

1. **`c_r` is always even** and `R_k[r] = c_r/2` takes only values in
   `{1, 2, 4, ..., 2^{k-2}}` plus the single Mersenne value `2^{k-1}-1`.
2. **The Mersenne value sits at r=1**: `R_k[1] = 2^{k-1} - 1` — the only
   non-power-of-2 value.
3. **All other entries are powers of 2.**
4. **Ones** (`R_k[r]=1`) sit exactly at `r = 0` and `r = 2^k - 2^j` for
   `j = 1..k-1` (i.e. `r = 2^k - 1 - (2^j - 1)`), plus the degenerate k=2
   seed where all three entries are 1.
5. **`sum_r c_r = 3^k - 3`** (OEIS A058809), density slope
   `(3^k-3)/(2^k-1)^2`. Confirmed independently to k=10.

**Fragility consequence (Directive 72):** the density slope
`(3^k-3)/(2^k-1)^2` decays like `(3/4)^k` — numerator `~3^k`, denominator
`~(2^k)^2 = 4^k` — so the per-period supply density tends to **0** as the
Mersenne period `P = 2^k-1` grows. Even the linear odd-factor families weaken
with growing period; this is the sharpest version of the fragility this run
keeps finding.

Verified by two independent routes (the original captures plus a fresh
recomputation in `code/pattern_finder/mersenne_*_final.py`).

## The recursion (self-similar interleave)

`R_{k+1}` is built from `R_k` by the block/interleave structure observed in
`code/pattern_finder/mersenne_block_recursion.py`: its even-index entries
`R_{k+1}[2r]` recover `R_k`, its odd-index entries are a transformed copy.
Combined with `S_{k+1} = 3 S_k + 3` for the running sum (so
`S_k = (3^k-3)/2`), this is the route to a potential induction proof of
`sum c_r = 3^k - 3` — but only conditional on the affine law, which is itself
unproved.

## Status and bearing

**Numerical/verification evidence only** — a conjecture, not a proof. The
whole per-residue-affine law (`dyadic-oddfactor-affine-modulus-lifting`) is
verified but unproved, so this elementwise refinement inherits that status. It
does NOT close G-supply for the aperiodic primes. It is a genuine partial
structural result on the *periodic* odd-factor family: the Mersenne case has a
fully explicit elementwise law for its supply constants, worth deriving.

## Files
- `code/pattern_finder/mersenne_elementwise_final.py` (+ capture)
- `code/pattern_finder/mersenne_ones_final.py`, `mersenne_block_recursion.py`,
  `mersenne_confirb_highk.py`, `find_recursion.py`, `align_recursion.py`
- all exact-integer; N up to 14000, k up to 10, O(k·N) per-recomputation.

```claim
id: mersenne-elementwise-supply-constants
statement: For the Mersenne tail-1 word P=2^k-1 (2-then-odds, gaps 2/4), the
  per-residue affine constants c_r of nu2 (across residues r mod P) satisfy:
  all c_r even; c_r/2 is a power of 2 except at r=1 where c_1/2 = 2^{k-1}-1;
  the value 1 occurs exactly at r=0 and r=2^k-2^j (j=1..k-1); and
  sum_{r} c_r = 3^k - 3 (density (3^k-3)/(2^k-1)^2).
hypotheses: per-residue affine law (verified, unproved); canonical nu2; exact
  integers, k=2..10.
holds-here: yes
status: checked
bearing: gives the exact elementwise shape of the Mersenne supply constants,
  turning the documented sum identity into a recursive array structure with a
  route to an induction proof conditional on the affine law. Still conjectured,
  does not close G-supply for the aperiodic primes.
```

## Files that verify it
- `code/pattern_finder/mersenne_elementwise_final.py`
- `code/pattern_finder/mersenne_ones_final.py`
- `code/pattern_finder/mersenne_confirm_highk.py`
- `code/pattern_finder/find_recursion.py`
