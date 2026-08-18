# PE1006: Psi(k) ≡ c1(k) (mod 100) — verified regularity

## Statement

For every k ≥ 1,

    Psi(k) ≡ 1 + ⌊k/φ²⌋  (mod 100),

where φ = (1+√5)/2, c1(k) = 1+⌊k/φ²⌋ = A189663 is the number of distinct
length-k Fibonacci subwords starting with '1', and Psi(k) is the PE1006 sum of
squares of the decimal values of the k+1 distinct length-k subwords (leading
zeros ignored).

## Proof (from established, verified recurrence)

1. **'11' is not a factor of the Fibonacci word.** (Verified in a length-17711
   prefix; this is the standard characterisation: the word is 01001010... with
   every 1 followed by 0.) Hence every factor w of length k with w·'1' still a
   factor must end in '0', so its decimal value V(w) ≡ 0 (mod 10).
2. Therefore S1(k) := Σ_{w·'1' ∈ F_{k+1}} V(w) ≡ 0 (mod 10).
3. The exact right-extension recurrence (established in pattern-hunt cycles
   3–4 with a direct proof, verified exactly k=1..3000):
       Psi(k+1) = 100·Psi(k) + 100·V(R_k)² + 20·S1(k) + J(k),
       J(k) = c1(k+1).
   Modulo 100: 100·Psi(k) ≡ 0, 100·V(R_k)² ≡ 0, and 20·S1(k) ≡ 0 since
   S1(k) ≡ 0 (mod 10).  So Psi(k+1) ≡ J(k) = c1(k+1) (mod 100).
4. Base: Psi(1) = 1 = c1(1).  Induction gives Psi(k) ≡ c1(k) (mod 100) for
   all k.

## Verification (all exact)

- Exact Ψ from the validated recurrence pipeline (recorded vR/s1, reproducing
  recorded exact Ψ(1..25)): k = 1..3000 all satisfy Ψ(k) mod 100 = c1(k) mod 100.
- Recorded residues mod M = 101001001 (k=1..400) agree with the identity
  (the modulus M ≡ 1 mod 100 doesn't disturb mod-100, verified by the exact
  values).
- Independent mechanical construction (mech_psi) at fresh k = 3001, 3005,
  3010, 3020, 3036, 3050, 3090, 3200, 3500, 4000: all pass.
- Falsification boundary: mod 1000 FAILS from k=2 (S1 is not generally
  0 mod 50 and V(R_k) not generally 0 mod 10), so mod 100 is exactly the
  strength of this argument.

## Consequence for the target

The last two digits of Ψ(10^18) are

    c1(10^18) mod 100 = 52,

computed exactly: c1(10^18) = 1 + ⌊10^18/φ²⌋ = 381966011250105152
(integer-sqrt of 5·10^36 with parity-aware floor, cross-checked at 60-digit
mpmath). Any O(log) evaluator returning Ψ(10^18) mod 101001001 must be ≡ 52
mod 100.

## Files

- code/pattern_hunt/verify_psi_mod100_c1.py — the verification program.
- code/pattern_hunt/check_psi_leading_digits.py, check_psi_digitlen.py,
  check_leading_block_c1.py — refuted digit-length/leading-block conjectures.