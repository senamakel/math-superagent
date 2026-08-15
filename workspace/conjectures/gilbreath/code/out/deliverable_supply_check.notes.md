# From-scratch independent check: P=3 closed form vs the per-residue-affine law

**Tool-builder verification, this run. From-scratch, no lib imports, exact integer
arithmetic, O(N^2) right-diagonal recurrence cross-checked against a literal
full-triangle builder (0 mismatches, n=2..40 for both P=3 and P=7).**

## Setup (canonical, matching claim `dyadic-oddfactor-affine-modulus-lifting`)

2-then-odds sequence `q_1=2, q_2=3`, gap after `q_m` (m>=2) is `2` if the
halved-gap bit `h[(m-2) mod P]` is 1 else `4`, with the **tail-1 word**
`h = [0]*(P-1)+[1]` of odd period `P`.  `nu2(n)` = # of 2s in the maximal
`{0,2}` **body** suffix of the right diagonal `delta(q_n)` (terminal entry
excluded).  For P=3 this is `h=[0,0,1]` (gaps 4,4,2 repeating: 2,3,7,11,13,17,...).

## Results (exact, n up to 2000)

### P=3 (word `[0,0,1]`)

1. **The literal closed form `nu2(n) = 2*floor((n-1)/3)` is REFUTED as a
   universal statement.**  It fails on 1332 of the tested n in [2,2000] — all
   of residue 1 and residue 2 (mod 3).  Examples: n=4 gives nu2=0 (not 2);
   n=5 gives nu2=3 (not 2); n=7 gives nu2=2 (not 4).  It holds (accidentally)
   only on residue 0 (mod 3).

2. **The claim's actual per-residue-affine law DOES hold** (this is the real
   statement in `dyadic-oddfactor-affine-modulus-lifting`):
   `nu2(n+3) - nu2(n) = c_r` is constant per residue, with `c_0=c_1=c_2=2`.
   The exact closed form (offsets constant from n=3): with `k = floor(n/3)`,
   `nu2(n)-2k` = {-2, -2, +1} for residues 0,1,2 respectively, i.e.
   `nu2(n) = 2*floor(n/3) + offset_r`, offset = (-2,-2,1).  So
   `nu2(n) ~~ (2/3) n`, min c_r = 2 >= 2, **positive linear supply** — the
   bearing of the claim (the odd-factor converse holds exactly-per-residue) is
   intact.  The slope 2/3 is exactly the `dyadic-oddfactor-infimum-bounded`
   figure for P=3.

### P=7 (Mersenne k=3, word `[0]*6+[1]`)

3. Per-residue-affine mod 7 with constants `c_r = [2,2,6,4,4,2,4]` and
   `sum_r c_r = 24 = 3^3 - 3` — EXACT match to the Mersenne closed form
   `sum c_r = 3^k - 3` (claim `mersenne-nu2-affine-selfsimilar-recursion` /
   the Mersenne row of the general claim).  min c_r = 2, all even.

## Conventions confirmed

- Right-diagonal recurrence indexing: the `e`-th yielded diagonal is over
  prefix length `e+1` (nu2(n) read at e = n-1).  This is the off-by-one that
  made an early draft disagree with the literal builder.
- Body convention for nu2 excludes the terminal entry.

## Source of truth for the verdict

`code/out/deliverable_supply_check.py` (+ `deliverable_supply_check.captured.txt`),
EXIT_CODE=0 (P=3 affinity + P=7 sum both pass).
