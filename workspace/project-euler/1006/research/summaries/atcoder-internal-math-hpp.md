# AtCoder Library — atcoder/internal_math.hpp (v1.5.1) — summary

<!-- source: https://cdn.jsdelivr.net/gh/atcoder/ac-library@v1.5.1/atcoder/internal_math.hpp | converted from plain text -->

## What it is

The internal number-theory header of the AtCoder Library (ACL), fetched from the
jsDelivr mirror at tag `v1.5.1`. It backs `atcoder/math.hpp` (the `floor_sum`,
`pow_mod`, `inv_mod`, `crt` public API) with the actual arithmetic internals.

## What it contains, and what matters for PE1006

- `safe_mod(x, m)`: x mod m in [0, m-1], handling negatives. Used to reduce the
  `b` offset and `a` slope in `floor_sum` before the recursion.
- `barrett`: fast modular multiplication via Barrett reduction (im = ceil(2^64/m),
  high-word trick) — the fast modular path for the mod-M arithmetic the run does,
  though Python bigints do not need it.
- `pow_mod_constexpr`, `is_prime_constexpr` — constexpr modular pow/primality for
  compile-time use; not needed by the solver.
- `inv_gcd(a, b)`: returns (g, x) with a*x ≡ g (mod b). This is what the run's
  `inv_mod(10, M)` (10^{-1} mod 101001001) would be computed by; gcd(10, M)=1
  so the inverse exists.
- **`floor_sum_unsigned(n, m, a, b)`** — the actual O(log) recursion that
  `atcoder::floor_sum` delegates to: sum_{i=0}^{n-1} floor((a*i+b)/m) in
  O(log m) via the Euclidean (reciprocal) step. **This is the primitive the
  universal-Euclidean notes generalise** (geometric weights x^i * floor(...))
  and the base case of the run's floor-sum primitive.

## Relationship to PE1006

The run's solution needs sum_{i} 10^i (mod M) * floor((a*i+b)/c) — a
geometric-weight floor sum — evaluated by the O(log) universal-Euclidean
recursion. `math.hpp` gives the public `floor_sum`; `internal_math.hpp` gives
the recursion it rests on (`floor_sum_unsigned`), the modular-inverse used for
x = 10^{-1} mod M, and the Barrett fast-mul. Together the two headers anchor
the base primitive whose geometric-weight generalisation (fhq 6-component
monoid; OI-wiki merge/flip) the solution implements.

The full text is at `research/sources/atcoder-internal-math-hpp.full.md`. See
also `research/sources/atcoder-math-hpp-v151.full.md` (the public header) and
`research/sources/oi-wiki-universal-euclidean-floor-sum.full.md` +
`research/sources/universal-euclidean-geometric-weight-fhq.full.md` (the
geometric-weight generalisation).