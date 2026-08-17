# AtCoder Library — `floor_sum` (official spec and source)

Spec source: https://atcoder.github.io/ac-library/production/document_en/math.html ([[atcoder-math-floor_sum-doc]])
Source code: https://cdn.jsdelivr.net/gh/atcoder/ac-library@v1.5.1/atcoder/math.hpp ([[atcoder-math-hpp-v151]])

## What these establish

**Spec (official).**
- `floor_sum(ll n, ll m, ll a, ll b)` returns Σ_{i=0}^{n−1} ⌊(a·i+b)/m⌋.
  Constraints: 0 ≤ n < 2^32, 1 ≤ m < 2^32. Complexity **O(log m)**.
- `pow_mod(x, n, m)` = x^n mod m, O(log n); `inv_mod(x, m)` with gcd(x,m)=1,
  O(log m) — the two modular primitives the run needs (10^{-1} mod M, and
  powers of 10^{-1} in the geometric monoid).
- `crt(r, m)` solves a modular system — not needed for PE1006.

**Source.** The verbatim `math.hpp` shows `floor_sum` reduces negative a,b via
`safe_mod` and calls `internal::floor_sum_unsigned` — the unsigned-signature
Euclidean loop that the universal-Euclidean monoid generalises. It confirms the
standard recursion's *existence and exactness* for the plain (unweighted) case.

## What it implies for PE1006

1. The bare `floor_sum` is **O(log m) but unweighted**: it cannot handle the
   geometric weights 10ⁱ in Ψ's telescoped form. So the AtCoder primitive alone
   is insufficient; the run needs the universal-Euclidean monoid (fhq/OI-wiki/
   LOJ138), of which AtCoder's floor_sum is the x=1 special case. Using
   `floor_sum` here would require summing k terms — infeasible at k=10^18.
2. `inv_mod` gives x = 10^{-1} mod M (M = 101001001, gcd(10,M)=1), the base of
   the geometric weights; `pow_mod` computes x^j and 10^{k−1−j} mod M.
3. Verbatim source is a reference implementation to test the monoid against
   (with x=1 weights the monoid should reproduce floor_sum's answers).

## Claims anchored here

`governing-universal-euclidean` (floor_sum as the x=1 special case; inv_mod /
pow_mod as the modular primitives).

## What it does NOT establish

- No geometric-weight form; no moment closure. The O(log m) claim is for the
  un-weighted sum only.
- No Sturmian-word content.