# Thread: mechanical-word / floor-sum route (directive 2), with slope correction

---
thread:
  question: Can Psi(k) for PE1006 be computed for k=10^18 in O(log) via the mechanical-word / geometrically weighted floor-sum, evaluated by the universal Euclidean (Chtholly / AtCoder floor_sum) algorithm?
  status: live
  rests-on:
    - claims/governing-sturmian
    - claims/governing-factor-complexity
    - claims/mechanical-word-digit-rule
    - claims/governing-universal-euclidean
  blocked-by: []
  next: slope correction already verified in-container at k=1..100 (exact rational
  arithmetic, research/notes/mechanical-slope-correction.md); proceed to implement
  the universal-Euclidean second-moment monoid and check it against brute on
  k=1..150 and Psi(10) mod M = 10699667 before running at 10^18.
---

# Thread: mechanical-word / floor-sum route (directive 2)

## Status update from the research digest

**Slope correction (discovered while reading Perrin–Restivo against directive 2).**
The problem's word S is the characteristic Sturmian word of slope α = 1/φ² ≈
0.382, NOT 1/φ ≈ 0.618 as directive 2's literal "slope a = F(n-1)/F(n)" reads.

- Perrin–Restivo Example 2: "The Fibonacci word is the characteristic word of
  slope α = 2/(3+√5)" = (3−√5)/2 = 1/φ².
- Berstel DLT'95 (Section 2): "The most famous characteristic word is the
  Fibonacci word f = abaababaabaab… Its slope is 1/τ²" (τ the golden ratio).
- Exact-arithmetic check at k=3 done by hand in this digest: slope α = 34/89
  (= F(n−2)/F(n)) with arc-midpoint intercepts reproduces {001,010,100,101} =
  the problem's factor set; slope 55/89 (= F(n−1)/F(n) ≈ 0.618) produces
  {010,011,101,110}, whose Ψ = 22522 ≠ 20302. So the directive's literal slope
  contradicts its own claimed verification at k=3; the corrected slope
  F(n−2)/F(n) → 1/φ² is the one that works.
- `code/out/check_slope.py` is written for tool_builder to confirm this
  mechanically over k=1..8 before the solver trusts the slope at 10^18.

**Convention trap (three sources).** Rabbit-sequence / "slope 1/φ" /
"cutting-line slope" statements (Sivasankar–Rama, MathWorld, Wikipedia's
Fibonacci-word page, Berstel Prop 2.3) all describe the digit-complement or
the line slope, not the problem's word. The factor sets are NOT invariant
under 0↔1 swap; any source string compared to the problem's factors must be
digit-matched to S.

## Directive 2 (primary, all k) — corrected

Model the k+1 distinct length-k Fibonacci subwords as a mechanical word of
rational slope a = F(n-2)/F(n) for F(n) >> k. Cut the unit circle at the k+1
points frac(-m·a), m = 0..k, take the midpoint x of each of the k+1 arcs;
digit_j(x) = floor(x + (j+1)a) − floor(x + j a). With v(x) = Σ_j digit_j·10^(k-1-j),
telescoping gives v(x) = floor(x+ka) − 10^(k-1)·floor(x) + 9·Σ_{j=1}^{k-1}
10^(k-1-j)·floor(x + j a). Psi(k) = Σ over the k+1 reps of v(x)² — the second
moment of a geometrically weighted floor sum, evaluated by the universal
Euclidean algorithm in O(log).

## Directive 1 (checkpoint at k = F_n − 1)

C(j,jp) = A(jp−j) = cyclic autocorrelation of standard word q_n, closed form
A(d) = max(0, m−t) + max(0, m−(N−t)), N = F_n, m = #ones(q_n), t = (d·m) mod N.
Same slope caution applies to the standard word's digit convention.

## What the sources now establish (see claim notes)

`governing-sturmian` (slope 1/φ², two anchors), `governing-factor-complexity`
(k+1, three anchors + brute oracle), `mechanical-word-digit-rule` (arc-midpoint
construction, source-backed + k=3 exact check), `governing-universal-euclidean`
(O(log) monoid, four anchors).

## Next step for tool_builder

run `python code/out/check_slope.py`; expected: slope 1/φ² and 34/89 match the
oracle at every k=1..8, slope 1/φ and 55/89 fail at k=3.