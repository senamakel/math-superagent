# Frontier: where new work must start

What is left open after this run's established results, stated precisely enough
that the next attempt can aim at it rather than re-derive.

## The run's main negative result (proved)

**No obstruction modulo any finite power of 3 can prove the Erdős ternary
conjecture.** Reason: `|A_k| = 2^(k-1)` exactly for every k (bijection proof,
verified to k=40), so the modular sieve never empties — the count doubles at
every level. Pattern-level survivors form a full infinite binary tree (each
`{0,1}`-string of length k with low digit 1 is realised by a unique exponent).
This matches Narkiewicz's bound `N(x) ≤ 1.62 x^(log_3 2)` (LAG-1 / STOLL-1): the
count-of-survivors grows, it never decays.

So a proof of the conjecture **cannot** be "the sieve kills the residue class of
n": every class with digit-free pattern survives. It must be that no *actual
digit-free exponent string* (a path consistent across all k that is a genuine
`2^n`) exists beyond n=8.

## What the sieve cannot see (the honest reformulation)

The orbit `{2^n : n ∈ Z}` is dense in `(Z_3)^×` (ord(4 mod 3^k) = 3^(k-1) by LTE,
2 ≡ −1 mod 3 gives both cosets — DENSE-ORBIT). The conjecture is:

> the dense orbit `{2^n}` meets the 3-adic Cantor set `Σ_{0,1} ∩ (Z_3)^×`
> (elements with all digits in {0,1}) at exactly the three integer points
> 1, 4, 256.

Closure/dimension arguments cannot decide orbit visits (closure is everything).
Only the arithmetic of the map `n ↦ 2^n` can.

## The actual frontier (Dimitrov–Howe, DH-1, proved)

For `x ∉ {0,2,8}`, the ternary expansion of `2^x` contains a digit 2 **or** at
least 26 digits equal to 1. Equivalently: the only powers of 2 that are sums of
≤25 distinct powers of 3 are {1, 4, 256}.

**Therefore any counterexample to Erdős is `2^x` with ≥26 ones and zero 2s.**
The residual open case is exactly that. Improving the 26 (handling ≥26 distinct
powers of 3) is the concrete unproved step; DH-1's method (nested moduli with
determinate-power lifting, Lemmas 3.1 / Table 3) is the template.

## The gap DH-1 leaves open, precisely

- DH-1 controls the **low** (3-adic) digit side: it forces a 2 or many 1s among
  the low digits. The run's `|A_k| = 2^(k-1)` shows the low-digit no-2 sieve
  survives everything, so low digits alone cannot kill the case ≥26 ones & no 2.
- What is missing is the **coupling of the top (real, ~log_3 X) digits to the
  bottom (3-adic, ~log_3 X) digits** — the middle digits that neither the real
  truncated method nor the 3-adic method exploit. LAG-4 states combining them is
  open. A counterexample with ≥26 ones and no 2s must be ruled out by this
  middle-digit coupling, which the sieve provably does not capture.

## Concrete partial targets ranked

1. **Formalise SIEVE-EXACT** (`|A_k| = 2^(k-1)` + bijection + 2-to-1 extension)
   in Lean — kills the count picture permanently, cheap, done-by-bijection.
2. **Reproduce the DH-1 bound (26) directly** from the archive's stated method,
   as an independent recomputation, so the frontier number is independently held.
3. **Improve DH-1's 26** for the restricted shape (no 2s) — e.g. rule out ≥26
   ones with no 2s for small x-sizes by nested-modulus lifting; any increase in
   the ones-threshold is the named unproved step.
