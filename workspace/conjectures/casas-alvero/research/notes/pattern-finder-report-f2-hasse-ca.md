# Pattern-finder report — F2 Hasse-CA structural regularities

## The finding that survives attack: a PROVED theorem

**Two-monomial law (char 2, Hasse derivatives).** For `g(x) = x^n + x^a` over
`F_2`, with `0 < a < n`:

> `g` satisfies Hasse-Casas-Alvero  ⇔  `C(n,a)` is odd  ⇔  `(a & n) == a`
>                                      ⇔  `a` is a subset-sum of the set bits of `n`.

**Proof** (three cases, one derivative decides):

- Write `g = x^a (x^{n-a} + 1)`.  Hasse derivative `H_i(x^j) = C(j,i)x^{j-i}`
  (no `i!` factor), so `H_i(g) = C(n,i)x^{n-i} + C(a,i)x^{a-i}` over `F_2`.
- `i < a`: both exponents `> 0`, so `H_i(g)` has no constant term → `x | H_i(g)`
  → `gcd(g, H_i)` contains `x`.  Passes.
- `i > a`: `C(a,i) = 0`, so `H_i(g) = C(n,i)x^{n-i}` is an `x`-power → `gcd`
  contains `x`.  Passes.
- `i = a`: `H_a(g) = C(n,a)x^{n-a} + 1`.
  `gcd(x^a, H_a) = 1` (constant term `1`); and `gcd(x^{n-a}+1, C(n,a)x^{n-a}+1)`
  is non-constant **iff** `C(n,a)` is odd.  So Hasse-CA holds iff `C(n,a)` odd.

Lucas's theorem: `C(n,a)` odd iff every set bit of `a` is a set bit of `n` —
i.e. `(a & n) == a`, i.e. `a` is a subset-sum of `n`'s set bits.  ∎

## Consequences (theorems now, not fits)

1. **Support-2 counterexample law.** The support-2 F2 Hasse-CA
   counterexamples of degree `n` are exactly
   `{ x^n + x^a : 0 < a < n, (a & n) == a }`, and their count is
   `2^popcount(n) − 2`.  (None is a pure power: the only degree-`n` pure powers
   over `F_2` are `x^n` and `(x+1)^n`, and `x^n+x^a` matches neither for
   `0<a<n`.)  This was previously a calibrated fit; it is now a theorem for all
   `n`.

2. **Failing-index rigidity.** When a two-monomial `x^n+x^a` fails Hasse-CA, it
   fails at derivative `i = a` and only there (proved by the `i<a`/`i>a` cases;
   no dependence on either exponent beyond which monomial is which).

## What the sequence tools establish over the terms supplied

- The raw multiplier sequence `m(n,2) = sat(n,2)/2` over `n = 3..24`:
  `[2,1,2,2,8,1,2,2,8,2,8,8,457,1,2,2,8,2,8,8,466,2]` is **irregular**: not a
  low-degree polynomial (differences never become constant within 12 levels),
  **no constant-coefficient linear recurrence of order ≤ 8**, and **no OEIS
  match**.  This is expected: the value is governed by popcount structure, not
  by `n` linearly, so no `n`-indexed closed form exists.

- The **pc-class structure** (the run's own grouping) is where order lives:
  pc=2 ↔ m=2 constant, pc=3 ↔ m=8 constant (each across all recorded degrees),
  pc=4 ↔ m varies (457 / 466 / 418) — the variation is entirely in the large
  supports, while support-2 (=14) and support-4 (=106) are rigid within pc=4.

## Attack on my own method (the falsification test)

The two-monomial law was originally only verified over the suggesting range
(`n ≤ 28`, exhaustion-bound).  I extended it **exactly to `n = 3..64`** — 2015
candidate polynomials, **0 mismatches** — using a different method that tests
only the `2^pc − 2` candidates per `n` instead of all `2^n` monic polynomials.
This reaches popcount classes 5 and 6 (`n = 31, 47, 55, 59, 61, 63, 62, …`),
which exhaustive enumeration could never reach.  A clean-convention recheck
(S1/S2/S3: law holds; failing index `== a`; no `i != a` ever fails) confirms all
three over the same range.  The first falsifying term would be any `(n,a)` with
`(a&n)==a` that fails Hasse-CA, or any `(a&n)!=a` that passes; none exists in
`3..64`.  The proof above shows **none can exist for any `n`** — this is why I
report it as a theorem, not a conjecture.

**What would refute the theorem:** a single `(n,a)` violating
`HasseCA(x^n+x^a) ⇔ (a&n)==a`.  The three-case argument rules this out
unconditionally; the computation searched `3..64` and found none.

## Conjectures still open (not proved)

1. **pc=3 full-profile rigidity** `{2:6, 4:5, 6:3}` holds across many degrees
   (verified n=7,11,13,19,21,22,25,26,28) but the 5 support-4 and 3 support-6
   forms do not yet have a closed structural derivation.  Enumeration shows the
   `x^a(x+1)^{n-a}` family accounts for the 6 support-2 (proved above) but not
   the 4- and 6-support counterexamples.
2. **Submask/`x^u(x+1)^v`-product forms** for the higher-support F2
   counterexamples: the factorization of pc=3 counterexamples (all divisible by
   `x` and `(x+1)`) suggests a product-of-linears structure worth a derivation,
   but it is not yet proved.

## Compute log

- `code/out/twoterm_submask_wide.py` — law, n=3..64, 2015 candidates, 0
  mismatches (exit 0).
- `code/out/twoterm_structure.py` — failing index always `== a` (exit 0).
- `code/out/twoterm_sharp2.py` — S1/S2/S3 clean-convention check, all HOLDS
  (exit 0).
- Raw multiplier irregularity: `analyze_sequence` (no polynomial to 12 diff
  levels), `find_linear_recurrence` (none ≤ order 8), `oeis_lookup` (no match).
- Full write-up of the theorem: `research/notes/two-monomial-f2-hasse-ca-proved.md`.

All arithmetic exact (bit-parallel Euclid/Hasse on F2, no floats).
