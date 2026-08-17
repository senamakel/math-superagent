# AtCoder Library — internal_math.hpp (`floor_sum_unsigned`, `inv_gcd`, Barrett)

Source: https://cdn.jsdelivr.net/gh/atcoder/ac-library@v1.5.1/atcoder/internal_math.hpp — [[atcoder-internal-math-hpp.full]]

## What this source establishes

The unsigned core of the AtCoder `floor_sum`, plus the modular primitives:

- `floor_sum_unsigned(n, m, a, b)` = Σ_{i=0}^{n−1} ⌊(ai+b)/m⌋ mod 2^64, via the
  recursion: if a ≥ m, strip a/m (ans += n(n−1)/2·(a/m)); if b ≥ m, strip b/m
  (ans += n·(b/m)); then y_max = a·n + b, if y_max < m break, else
  (n, b, m, a) ← (y_max/m, y_max mod m, a, m) — the axis-flip Euclidean step.
  This is exactly the unweighted (x=1) special case of the universal-Euclidean
  monoid (fhq/OI-wiki/LOJ138).
- `inv_gcd(a, b)` — extended Euclidean, returns (g, x) with x·a ≡ g (mod b):
  the primitive for 10^{−1} mod M.
- `safe_mod`, `barrett` (fast modular multiplication), `pow_mod_constexpr`,
  `is_prime_constexpr` (Miller–Rabin with bases 2,7,61 — valid for n < 2^32):
  M = 101001001 < 2^32 so `is_prime` could verify primality, but the run does
  not need primality — only gcd(10, M)=1, which `inv_gcd` itself confirms.

## What it implies for PE1006

1. Verbatim confirmation that the Euclidean floor-sum recursion is exact and
   O(log), and that it is the x=1 case of the monoid the run must build. Any
   monoid implementation should reproduce `floor_sum`'s values when weights
   are all 1 — a cheap correctness gate before geometric weights.
2. `inv_gcd(10, M)` returns g=1 (gcd(10, M)=1), so 10^{−1} mod M exists — the
   geometric base. (Confirmed independently: M is odd and not ≡0 mod 5.)

## Claims anchored here

Corroborates `governing-universal-euclidean` (recursion; modular primitives).

## What it does NOT establish

- No geometric weights, no moments. The weighted/moment monoid is the fhq/
  LOJ138 tier.