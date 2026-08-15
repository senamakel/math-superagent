# Prime switch bit: quantitative distance to nearest 2^k-periodic string (DPC-prime-antidyadic, measured)

This attempt executed the "first move" that the DPC-prime-antidyadic gap note
drafted but had not run: the Hamming distance of the real prime mod-4 switch
bit from the nearest power-of-two-periodic binary string.

Complementarity: `close-spad-prime-anti-dyadic` already **proved** non-eventual
periodicity of the switch bit (claim `spad-prime-anti-dyadic-proved`,
periodicity-violation witnesses). This note measures a **different, stronger
quantity** — how *close* the switch bit comes to a periodic string, which the
proved statement's "not eventually periodic" does not quantify.

## The quantity

Switch bit `h[j] = ((p_{j+2} − p_{j+1})/2) mod 2` over the fixed ancestor
window `j ∈ [2, n−1]` (`h[j]=1 ⟺ gap ≡ 2 mod 4`). For each `k = 0..6` (period
`p = 2^k`), compute the Hamming distance from `h|[2,n-1]` to the **nearest**
p-periodic binary string, over window length `n−2`.

Nearest distance is **exact**, not a heuristic: it decouples per residue class
mod p, `dist = Σ_r min(#0 in class r, #1 in class r)` (per-class majority). The
program proves this in-comment and verifies it against a brute-force oracle for
k=0..2 (all match exactly).

## The result (EXIT 0, exact integers, capture below)

| n    | dist/n to nearest 2^k-periodic, k=0..6 | w/(n-2) (switch density) |
|------|------------------------------------------|--------------------------|
| 10^4   | 0.414                                   | 0.586                    |
| 10^5   | 0.426                                   | 0.574                    |
| 10^6   | 0.437                                   | 0.563                    |

Sanity: worked rows `A_1,A_2,A_3` from problem.md reproduce exactly (PASS).

## Reading

- dist/n stays ~0.41–0.44 at every k and every prefix to 10^6 — it never
  collapses toward 0. So the prime switch bit is **quantitatively** far from
  every power-of-two-periodic string: strong measured confirmation of the
  DPC-prime-antidyadic content.
- **Crucial nuance:** dist/n equals the zero-fraction ≈ 1 − w/(n−2). The
  nearest periodic string is essentially the **constant all-ones** (k=0) string;
  letting the period grow (per-residue majority freedom over k=1..6) buys almost
  nothing. So the anti-dyadicity is almost entirely the switch-density bias
  (majority-1), not subtle period-correlation structure.
- Therefore this confirms non-periodicity but does **not** separate the prime
  bit from a constant, and does **not** close G-supply. `ν₂ ≥ c·n` for the
  primes stays the named-open arithmetic hypothesis
  `abgs-2011-s9-mod4-switch-limit-open`.

## Files

- Program: `code/out/prime_antidyadic_distance.py`
- Capture: `code/out/prime_antidyadic_distance.captured.txt`
- Run: `timeout 540 python3 code/out/prime_antidyadic_distance.py 2>&1 | tee code/out/prime_antidyadic_distance.captured.txt; echo EXIT_CODE=$?` → EXIT_CODE=0, 0.6s.

This is a prime measurement, numerical to 10^6, not a proof. Board lesson
posted (adversarial).
