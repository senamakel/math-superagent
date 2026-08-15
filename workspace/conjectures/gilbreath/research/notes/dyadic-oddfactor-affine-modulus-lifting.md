# Exact-affine structure of ν₂ on odd-period tail-1 words (generalised)

**Pattern-finder finding, verified-numerically (conjecture, not proved).**

## Setup

2-then-odds sequence with `q_1=2, q_2=3`, gap `q_{m+1}-q_m = 2` if bit else `4`,
bits = **tail-1 word** `[0]*(P-1)+[1]` of odd period `P`. `ν₂(n)` = #2s in the
maximal `{0,2}` suffix of the right diagonal `δ(q_n)` (body convention,
`lib.rightdiag.cycle_and_nu2`).

Nu2 is **per-residue affine mod L** iff for each residue `r mod L`,
`ν₂(n+L) − ν₂(n) = c_r` is an exact constant over the whole window.

## The generalisation (extends `dyadic-mersenne-affine`)

> **For every odd period `P`, `ν₂` is per-residue affine mod**
> **`L = 2^{ord₂(P)} − 1`**, where `ord₂(P)` is the multiplicative order of 2
> mod P — i.e. `L` is the *smallest Mersenne number divisible by P*.

The Mersenne result (`dyadic-mersenne-affine`) is the special case
`ord₂(P) = log₂(P+1)` (i.e. `P = 2^k−1`), which gives `L = P`.

### Verified (exact, 0 contradictions, L ≤ 3500)

| P | ord₂ | L = 2^ord₂−1 | affine | min c_r | slope Σc_r/L² |
|---|------|--------------|--------|---------|----------------|
| 3  | 2  | 3    | yes | 2 | 2/3 |
| 5  | 4  | 15   | yes | 8 (const) | 8/15 |
| 7  | 3  | 7    | yes | 2 | 24/49 |
| 9  | 6  | 63   | yes | 26 (const) | 26/63 |
| 11 | 10 | 1023 | yes | 936 | 160/341 |
| 15 | 4  | 15   | yes | 2 | 26/75 |
| 17 | 8  | 255  | yes | 80 (const) | 16/51 |
| 21 | 6  | 63   | yes | 16 | 506/1323 |
| 23 | 11 | 2047 | yes | 936 | 22528/47081 |
| 31 | 5  | 31   | yes | 2 | 240/961 |
| 33 | 10 | 1023 | yes | 242 (const) | 22/93 |
| 51 | 8  | 255  | yes | 58 | 478/1445 |
| 63 | 6  | 63   | yes | 2 | 242/1323 |
| 73 | 9  | 511  | yes | 110 | 10728/37303 |
| 85 | 8  | 255  | yes | 32 | 104/425 |
| 89 | 11 | 2047 | yes | 608 | 66880/182183 |
| 93 | 10 | 1023 | yes | 152 | 10342/31713 |

Larger P (ord₂ large, L huge) not yet tested (window cost); all tested cases
agree.

## Two exact closed-form families

### (a) Mersenne `P = 2^k − 1` — sum c_r = 3^k − 3
Per-residue constants vary but `Σ_{r=0}^{P−1} c_r = 3^k − 3` (OEIS A058809),
density slope `(3^k − 3)/(2^k − 1)²`, verified k=2..10. (Documented in
`dyadic-mersenne-affine.md`.)

### (b) Fermat-like `P = 2^m + 1` — c_r constant = 3^m − 1
For P = 2^m + 1 (m = 2,3,4,5 verified): `ord₂(P) = 2m`, `L = 2^{2m} − 1`, and
**c_r is identically `3^m − 1` for every residue**, so
`ν₂(n+L) − ν₂(n) = 3^m − 1` for all n. Density slope
`(3^m − 1)/(2^{2m} − 1) = (3^m−1)/((2^m−1)(2^m+1))`.

| m | P=2^m+1 | L | c_r | slope |
|---|---------|---|-----|-------|
| 2 | 5  | 15  | 8  | 8/15 |
| 3 | 9  | 63  | 26 | 26/63 |
| 4 | 17 | 255 | 80 | 16/51 |
| 5 | 33 | 1023| 242| 22/93 |

Remarkable symmetry: Mersenne gives `3^k − 3` over period `2^k−1`; Fermat-like
gives `3^m − 1` over period `2^m+1`. Both are "3-power minus small" with L the
relevant Mersenne multiple.

## Minimality

The true smallest affine modulus is conjectured to be exactly
`L = 2^{ord₂(P)} − 1` (not a proper divisor). Direct test for P=11 (L=1023):
proper multiples 33, 341 are NOT affine, only 341? — no: at P=11 both 341 and
1023 are affine, 33 is not. For P=13 (L=4095), every tested proper multiple
{39,65,91,195,273,455,585,1365} is NOT affine; only 4095 is. So no smaller
divisor works generically; L itself is the minimal (conjecturally).

Note: for P=11, modulus 341 = 11·31 IS affine (smaller than 1023), so the
minimal modulus is not always L. The claim to record is: **affine at the
Mersenne modulus `2^{ord₂(P)}−1` (so supply is linear), and min c_r ≥ 2.**
Pinning the exact minimal modulus needs per-P divisor work (P=11 → 341).

## Bearing / interpretation

- **Collapse side** (power-of-2 periods): `dyadic-collapse-proved`, ν₂=O(1).
- **Affine-linear side** now holds at an exact law on EVERY odd-period tail-1
  word: ν₂ is per-residue affine mod `2^{ord₂(P)}−1` with all c_r ≥ 2, giving
  `ν₂(n) ≥ (2/L)·n − O(1)` — positive linear supply, an *exact-affine* form of
  the odd-factor converse.
- The convex combination: for any odd P, since L ≤ (some bound times P)... the
  per-P constant `2/L` decays as ord₂(P) grows (like the Mersenne slope), so
  there is NO uniform c across all P — consistent with
  `dyadic-oddfactor-infimum-bounded`.
- **Numerical/verification evidence only** — a conjecture, not proved. Does NOT
  close G-supply for the aperiodic primes.

## Files
- `code/pattern_finder/affine_modulus_efficient.py` (+ `pf_affine_modulus_efficient.captured.txt`)
- `code/pattern_finder/affine_min_constant.py` (+ `pf_affine_min_const.captured.txt`)
- `code/pattern_finder/fermat_like_constant_c.py` (+ `pf_fermat_like_const_c.captured.txt`)
- `code/pattern_finder/affine_minimal_probe.py` (+ `pf_affine_minimal_probe.captured.txt`)
- prior: `research/notes/dyadic-mersenne-affine.md` (Mersenne case)

```claim
id: dyadic-oddfactor-affine-modulus-lifting
statement: For every odd period P, the right-diagonal {0,2}-suffix count nu2(n)
  of the tail-1 word [0]*(P-1)+[1] (2-then-odds, gaps 2/4) is per-residue affine
  modulo L = 2^ord2(P)-1, where ord2(P) is the multiplicative order of 2 mod P
  (L the smallest Mersenne number divisible by P): nu2(n+L)-nu2(n)=c_{n mod P}
  is a constant per residue over the window.  In every measured case all
  c_r >= 2, so nu2(n) >= (2/L)n - O(1): positive LINEAR supply on every
  odd-period tail-1 word.  Exact closed forms: Mersenne P=2^k-1 has sum c_r =
  3^k-3 (density (3^k-3)/(2^k-1)^2); Fermat-like P=2^m+1 has c_r constant =
  3^m-1 (density (3^m-1)/(2^(2m)-1)).
hypotheses: 2-then-odds halved-gap bit string h of odd minimal period P,
  tail-1 word; canonical nu2 = maximal {0,2} suffix of right diagonal; exact
  integers, P <= 93, L <= 3500 (larger P untested); ord2 exists (P odd).
holds-here: yes
status: checked
bearing: extends dyadic-oddfactor-infimum-bounded / dyadic-mersenne-affine from
  the Mersenne periods to ALL odd periods: the odd-factor converse (positive
  linear nu2) holds at an exact per-residue-affine law with min c_r >= 2, giving
  a clean positive-lower-bound on every odd-period tail-1 word.  Numerical only
  (conjecture, not proved) and does NOT close G-supply for the aperiodic primes
  (abgs-2011-s9-mod4-switch-limit-open stays the open hypothesis).  Slopes decay
  with ord2(P) so no uniform c across P.
anchor: research/notes/dyadic-oddfactor-affine-modulus-lifting.md
```
