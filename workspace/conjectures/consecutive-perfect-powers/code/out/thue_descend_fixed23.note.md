# Exponent-2 case `x^2 - y^3 = 1` proved in full: descent + complete Thue resolution

Program: `code/refute/thue_descent_full.py` and `code/refute/thue_nf.gp`.
Output: `code/out/thue_descent_full.captured.txt`, `code/out/thue_gp.captured.txt`.

## Result (proved, rank-4 GOAL deliverable: an exponent-2 case proved in full)

> The only solution of `x^2 - y^3 = 1` in positive integers `x, y` is `(x, y) = (3, 2)`.

This is Lebesgue's 1850 theorem, re-derived here in-workspace by an explicit
descent whose final Thue equations are resolved completely by PARI's proven
`thue()` algorithm. Each descent step is exact symbolic algebra; no
enumeration, no floating point.

## Method

1. `y^3 = x^2 - 1 = (x-1)(x+1)`, `gcd(x-1, x+1) | 2`. (exact identity)
2. `x` even is impossible: then `x-1, x+1` are odd and coprime, both cubes
   `a^3 < b^3` with `b^3 - a^3 = 2`, but the minimum gap of two positive cubes
   is `2^3 - 1^3 = 7 > 2`. (one-line case split)
3. `x` odd, write `x = 2k+1`, `y = 2y'`:
   `(2k+1)^2 - 1 = 4k(k+1) = y^3 = 8 y'^3`, so `k(k+1) = 2 y'^3`.
   Since `gcd(k, k+1) = 1`, all of the 2-power of `2 y'^3` sits in the even one
   of `{k, k+1}`. Let `v = v_2(y')`; then `v_2(2y'^3) = 1 + 3v` (≡ 1 mod 3,
   **not** generally 1). So the even factor is `2^{1+3v}·(odd)^3 =
   2·(2^v·odd)^3`, i.e. the shape `{k, k+1} = {c^3, 2d^3}` holds with `d`
   absorbing the whole `2^v`:
   - Case A: `k = c^3`, `k+1 = 2d^3`  ⟹  `c^3 - 2d^3 = -1`
   - Case B: `k = 2d^3`, `k+1 = c^3`  ⟹  `c^3 - 2d^3 = +1`
   **Correction (adversarial review was right):** the earlier phrasing "the
   single factor 2 of `2 y'^3` goes wholly into the even one" is FALSE when
   `y'` is even — `2y'^3` carries `1+3v` powers of 2, not one. The stated
   justification is wrong, but the conclusion survives because the extra
   `2^{3v}` folds into `d^3`. The descent is intact; the sentence was not.
4. Resolve the two Thue equations `c^3 - 2d^3 = ±1` **completely** with PARI's
   `thue()` (a proven complete solver for degree-3 binary Thue equations):
   ```
   thue c^3-2d^3=1 : [[-1,-1], [1,0]]
   thue c^3-2d^3=-1: [[-1, 0], [1, 1]]
   ```
5. Map back and keep `x, y > 0`:
   - Case B `(c,d)=(1,0)`: `k=0`, `x=1`, `y=0` — excluded (y=0).
   - Case B `(c,d)=(-1,-1)`: `k=-2`, `x=-3` — excluded (x<0).
   - Case A `(c,d)=(-1,0)`: `k=-1`, `x=-1` — excluded (x<0).
   - Case A `(c,d)=(1,1)`: `k=1`, `x=3`, `y=2 c d = 2` — **the solution (3,2)**.
   - Cross-check `3^2 - 2^3 = 9 - 8 = 1` ✓.

## Completeness of the Thue step

The companion `thue_descent_full.py` enumerated units `±(1-ω)^n` (ω³=2) in the
bounded window `|n| ≤ 60` and found only `(c,d)=(1,0),(1,1)`. That window is
**not** a proof: the ω²-coefficient is not monotone in `n` (a recurrence scan
shows it changes sign and grows irregularly), so the window could in principle
miss solutions. The `-1`-class solutions `(c,d)=(-1,0),(-1,-1)` PARI finds are
indeed outside any non-negative unit window yet are valid complete solutions of
the Thue equations. They do not change the filtered answer (they give `x ≤ 0`),
but the honest completeness claim relies on **PARI `thue()`**, not the window.

Supporting PARI facts used: `Q(∛2)` has class number 1 and unit rank 1
(K = bnfinit(x^3-2), `K.no = 1`, `K.fu = [x-1]`), which underlies the exact
resolution.

## Cross-verification (independent route)

**Honesty correction (adversarial review).** The two .gp files
`thue_pair.gp` and `thue_nf.gp` both contain the *identical*
`thueinit(x^3-2); thue(T, ±1)` calls — one PARI proven `thue()` solver run
twice. They are **not** an independent route; completeness of the Thue step
rests on a single black box (PARI's proven complete degree-3 Thue solver).
The genuinely independent confirmations of the **answer** `(x,y)=(3,2)` are:
the exact integer oracle `solutions(N)`, the brute force in
`code/elementary/elementary_rungs.py` to `x=10^7`, and the previously-verified
`r-fixed-23` claim — all agree. So the *answer* is cross-verified by multiple
routes, but the *completeness of the Thue resolution* is not independently
confirmed, and the claim's `status: proved` rests on that single black box.
Do not copy the "two invocations of one solver = independent" pattern.

## Scope note

The claim `exp2-fixed23-proved-thue` fixes **q=3 only**. It does not close case
A (`x^2 - y^q = 1` for all odd primes q); ruling out q ≠ 3 remains open
(separate claims `exp2-descent-*` cover that, verified-numerically).

```claim
id: exp2-fixed23-proved-thue
statement: The only solution of x^2 - y^3 = 1 in positive integers x, y is
  (x,y) = (3,2).
hypotheses: x, y > 0 integers; descent k(k+1)=2 y'^3 with gcd(k,k+1)=1; the
  Thue equations c^3 - 2d^3 = +-1 resolved completely by PARI's proven thue()
  algorithm.
holds-here: TRUE — this is the exponent-2 case (q=3) that the reduction to odd
  primes relies on; it is the known solution's own case, never an over-elimination.
status: proved (descent exact; Thue resolution by proven complete algorithm;
  final filtering x,y>0 selects exactly (3,2)).
bearing: closes rank-4 GOAL item "exponent-2 cases proved in full"; the
  q-exponent of the known solution is 3, so proving x^2-y^3=1 does not
  eliminate the known solution — it is precisely it.
anchor: code/out/thue_descent_full.captured.txt, code/out/thue_gp.captured.txt
```
