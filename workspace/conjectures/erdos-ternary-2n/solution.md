# Erdős ternary conjecture: partial result — the modular sieve cannot close (proved)

## The theorem (this run's deliverable)

Let

```
A_k = { r mod 2·3^(k-1) : the low k ternary digits of 2^r mod 3^k all lie in {0,1} }
```

be the residue-class sieve set. Then

```
|A_k| = 2^(k-1)   for every k ≥ 1,
```

with a bijection between the survivor classes of `A_k` and the digit patterns
(length-k strings, low digit 1, other k−1 digits in {0,1}).

**Consequence (negative result about the method, proved):** the count doubles at
every level and never reaches zero, so the modular sieve *never empties*. No
obstruction modulo any finite power of 3 can prove the Erdős conjecture — i.e.
"`2^n mod 3^k` forces a digit 2" is false for every finite k. A proof of the
conjecture must come from structure the sieve cannot see (the middle/high-digit
coupling), not from a decaying survivor count. The density
`|A_k|/(2·3^(k-1)) = (1/2)(2/3)^(k-1) → 0` while the count grows; these are not
in tension, and the count-growth is exactly why the sieve cannot close.

## Why it is true (the proof)

1. **2 is a primitive root mod 3^k** for every k: its multiplicative order is
   `φ(3^k) = 2·3^(k-1)` (verified exactly for k=1..40 by order reduction; this
   is a standard LTE consequence, LAG-1/SAYE-2).
2. Hence `Φ_k : r ↦ 2^r mod 3^k` maps `Z/(2·3^(k-1))Z` bijectively onto the unit
   group `(Z/3^k)^×`.
3. A unit's low ternary digit is 1 (never 0). So the digit-free patterns among
   the units are exactly: low digit 1, other k−1 digits in {0,1} — that is
   `2^(k-1)` patterns. Each is hit by a unique exponent. Hence `|A_k| = 2^(k-1)`.
4. Each length-k pattern extends to a length-(k+1) pattern in exactly two ways
   (append 0 or 1), both units, both hit by a unique exponent — so the extension
   map `A_{k+1} → A_k` is exactly **2-to-1** and surjective.

The lifting mechanism was independently corroborated: `2^(2·3^(k-2)) ≡ 1 + 3^(k-1)
(mod 3^k)` with quotient c = 1 exactly for k=2..40 (verified by the program), so
each class's three lifts shift only the top digit by {0,1,2} mod 3 and exactly
one of the three dies.

## Numerical verification (all exact, exit 0; `code/out/prove_count_doubles.captured.txt`)

Fresh program `code/out/prove_count_doubles.py`, six sections, all PASS:

| # | Check | Range | Result |
|---|---|---|---|
| 1 | `digit_free`: 1,4,256 digit-free (1_3, 11_3, 100111_3); 32=1012_3, 64=2101_3 contain 2 | — | PASS |
| 2 | order of 2 mod 3^k = 2·3^(k-1) | k=1..40 | PASS |
| 3 | `|A_k|` by DIRECT sieve = 2^(k-1) | k=1..12 | PASS |
| 4 | each class lifts to exactly 2 of 3; total 2^k | k=1..11 | PASS |
| 5 | LTE: v_3(2^(2·3^(k-2))−1) = k−1, c=1 | k=2..40 | PASS |
| 6 | witnesses n=0,2,8 digit-free at every level | k=1..40 | PASS |

The three falsification witnesses `n = 0, 2, 8` (2^0=1_3, 2^2=11_3, 2^8=100111_3)
are digit-free and survive in `A_k` at every level; nothing in this result
forbids them, so it is not overreach.

This matches Narkiewicz's `N(x) ≤ 1.62·x^(log_3 2)` bound (LAG-1/STOLL-1): the
survivor count grows like `2^(k-1)`, never decays.

## Evidence classes

- **`|A_k| = 2^(k-1)` for all k: proved** (bijection argument, steps 1–4; the
  count), and **verified** exactly by the program to k=40 (order), k=12 (direct
  sieve), k=11 (lifting).
- **LTE quotient c=1: verified** k=2..40 (computed); the general c≢0 mod 3 is the
  standard LTE statement.
- **The sieve cannot close at any finite 3-adic precision: proved** (consequence
  of the count theorem).

## What the sieve cannot see — the frontier

- The orbit `{2^n : n ∈ Z}` is **dense** in `(Z_3)^×` (4 generates 1+3Z_3; 2≡−1
  mod 3 gives both cosets). The conjecture is exactly: the dense orbit meets the
  3-adic Cantor set `Σ_{0,1}` (all digits in {0,1}) at only {1,4,256}.
- Dimitrov–Howe (proved, DH-1): any counterexample beyond {0,2,8} has **≥26 ones**
  in its ternary expansion. So the residual open case is "≥26 ones and zero 2s".
- The low-digit no-2 sieve provably survives everything, so ruling out ≥26-ones-
  and-no-2s requires coupling the top (real, ~log_3 X) and bottom (3-adic)
  digits — the middle-digit structure neither controls alone. Combining the two
  is open (LAG-4).

## Files

- `code/out/prove_count_doubles.py` and `.captured.txt` — the verification program and its output.
- `research/APPROACHES.md` — why the pure sieve, the naive count, and the density/digit heuristics cannot close.
- `research/FRONTIER.md` — the exact open case and what would settle it.
- `research/threads/lifting-proof.md`, `research/threads/sieve-dynamics.md` — the proofs.
