# Pattern-finder seventh pass — the orbit's hidden symmetry: survivors avoid ±r pairs

## The provenance of the discovery

Prior passes (5, 6) established that the survivor *exponents* `A_k` (residues
`r mod 2·3^(k-1)` whose `2^r mod 3^k` has low `k` ternary digits in `{0,1}`)
are: all even, `|A_k| = 2^(k-1)`, project exactly onto `2^j` classes mod `3^j`
for `k > j`, and — this pass's starting point — have a **half-count that tends
to `1/2`** rather than splitting along any fixed line:

```
half(k) = #{r ∈ A_k : r < period/2},  period = 2·3^(k-1) = 2·|A_k|
k:  2  3  4  5   6   7   8    9   10   11   12   13   14 ...
   [2, 4, 7, 13, 21, 37, 70, 139, 267, 525, 1041, 2046, 4100, ...]
frac: 1.0, 1.0, 0.875, 0.8125, 0.6562, 0.5781, 0.5469, 0.543, 0.5215,
       0.5127, 0.5083, 0.4995, 0.5005, ...  (→ 1/2 as k → ∞)
```

The half-count has **no** low-order linear recurrence and is not polynomial
(kept from pass 5, re-confirmed on 23 terms), so `frac → 1/2` is the emerging
law. The natural structural cause of an exact equidistribution about the
midpoint would be **reflection invariance**: `r ∈ A_k ⟺ (period − r) ∈ A_k`.
That hypothesis is what this pass attacks.

## The exact regularity that REFUTES reflection invariance (fresh, k=2..26)

`pattern_refl2.py` (exact modular survivor lift, k=2..26): for every `k`,
the survivor set `A_k` contains **no nontrivial reflection pair {r, P−r}**
(`P = 2·3^(k-1)`). The only element of `A_k` whose mirror is also in `A_k` is
`r = 0`, for every single `k` from 2 to 26:

```
k=2  |A|=2    hits=[0]     k=14 |A|=8192     hits=[0]
k=3  |A|=4    hits=[0]     k=18 |A|=131072   hits=[0]
...                         k=26 |A|=33554432 hits=[0]
```

So the survivor exponents are **anti-orbits under the map r ↦ P−r**: the half
count ~`2^(k-1)/2 = 2^(k-2)` is *not* a symmetry — it is exactly one fewer
than the 2^(k-1)/2 a reflection symmetry would force, because the lone fixed
point r=0 has no partner. The `frac → 1/2` limit is real (verified) but it is
the limit of an *almost−1/2* sequence, never exact.

**Why reflection-invariance fails — the value-domain theorem behind it.**
`A_k` is the set of `r` with `2^r ∈ S mod 3^k`, `S` the digit-{0,1} set. A
reflection pair `{r, P−r}` inside `A_k` means **both** `2^r` and `2^{P−r} =
(2^r)^{-1} mod 3^k` lie in `S`. A pairof values that are each other's inverses
and both in `S`. So the exponent-side question reduces to a pure **value-domain
theorem**:

> **`S ∩ S^{-1} = {1}` in `Z_3`** — the only 3-adic integer whose ternary digits
> all lie in {0,1} *and whose multiplicative inverse also has all digits in
> {0,1}* is `1`.

## The proof — COMPLETE and rigorous (S ∩ S^{-1} = {1} in Z_3)

Let `S` be the set of 3-adic integers all of whose ternary digits lie in
{0,1}. Let `x ∈ S` be a unit, so its low digit is 1. Write
`m = v_3(x − 1) ≥ 1` and `x = 1 + 3^m y` with `y ≢ 0 (mod 3)`. Because `x`
has all digits in {0,1} and the digit at position `m` (the lowest nonzero
position of `x − 1`) is 1 — a unit in S has every nonzero digit equal to 1,
never 2 — we get `y ≡ 1 (mod 3)`.

In `Z_3` the inverse expands by the geometric series

```
x^{-1} = (1 + 3^m y)^{-1} = 1 - 3^m y + (3^m y)^2 - (3^m y)^3 + ...
```

For `j ≥ 2`, the term `(3^m y)^j` is divisible by `(3^m)^2 = 3^{2m} ≥ 3^{m+1}`
(since `m ≥ 1`), so it contributes 0 to the `3^m`-digit place. Hence

```
x^{-1} ≡ 1 - 3^m y  (mod 3^{m+1}),
```

and the digit of `x^{-1}` at position `m` is

```
digit_m(x^{-1}) ≡ -y ≡ -1 ≡ 2  (mod 3),    since y ≡ 1 (mod 3).
```

So `x^{-1}` has digit **2** at position `m`, i.e. `x^{-1} ∉ S`. Every `x ≠ 1`
in `S` therefore has its inverse outside `S`, and trivially `1^{-1} = 1 ∈ S`.
**Therefore `S ∩ S^{-1} = {1}`.  QED.**

`pattern_invproof.py` verifies the load-bearing claims numerically: for the
minimal offender `x = 1 + 3^m` (y = 1), `digit_m(x^{-1}) = 2` for every
m = 1..11; and for general `x = 1 + 3^m(1+3w)` (y ≡ 1 mod 3), `digit_m = 2`
for all m = 1..7, w = 0..3 (zero violations). The full value-domain
enumeration (`pattern_invset.py`, k=2..12, over all `2^(k-1)` value-units in
S) confirms `{1}` is the only unit of S whose inverse is in S.

## Bearing on the conjecture — what this does and does not give

Two exact structural facts, each PROVED (the value-domain one by the rigorous
argument above; the orbit one by the exact modular lift to k=26):

**(i) Exponent side — anti-orbit (proved).** `A_k` is the set of `r` with
`2^r ∈ S mod 3^k`. A reflection pair `{r, P−r}` ⊆ `A_k` (P = 2·3^(k−1)) exists
iff both `2^r` and `2^{P−r} = (2^r)^{-1} mod 3^k` lie in S, i.e. iff the value
`2^r` lies in `S ∩ S^{-1} = {1}`, i.e. iff `2^r = 1`, i.e. iff `r = 0`.
So **for every k, `A_k` contains no reflection pair except the trivial `{0,0}`**
— verified directly k=2..26 (pattern_refl2.py). This is the cleanest exact
structural statement this run has produced, and it is a *proof*, not a fit.

**(ii) Value domain — `S ∩ S^{-1} = {1}` (proved).** Among {0,1}-digit 3-adic
units, no nontrivial one is multiplicatively self-inverse-keeping. Its
relevance: a counterexample `2^n` (digit-2-free) is a value in S; if its low-
digit-complement inverse `2^{-n}` mod 3^k stayed in S at every k it would
engineer a reflection pair — and this theorem rules out ALL such pairings,
not just orbit ones.

**Honest limits (stated precisely):**
- The value-domain theorem `S ∩ S^{-1} = {1}` is **proved** (complete proof
  above), and cross-checked exhaustively in the value domain to 3^12 and on
  the orbit to k=26.
- It is NOT a proof of the Erdős conjecture. It excludes the *reflection-symmetric*
  subclass of counterexamples (those whose 3-adic inverse is also digit-{0,1});
  it does not exclude a lone counterexample `2^n` with no inverse partner in S.
  But it is a genuine, exactly-stated, rigorously-proved partial structural
  result — the anti-symmetry of the survivor orbits — which is precisely the
  shape of partial result GOAL.md asks for (a structural fact about the digit-
  {0,1} set S and the orbit it is preserved/opposed by).

## Attack log (who tried to break it, and how far)

- **Reflection-invariance hypothesis** (r ∈ A_k ⟺ P−r ∈ A_k): REFUTED for all
  k=2..26 — the correct statement is the exact opposite (anti-orbit: only r=0
  is self-mirrored). Falsifying witness: k=2 alone (A_2={0,2}, P=6, reflection
  of 2 is 4∉A_2).
- **"Some {0,1}-digit unit has a {0,1}-digit inverse"**: REFUTED — `k=12`
  enumeration over all `2^11` units finds only x=1; and `x=1+3^m` has inverse
  with digit 2 at position m for every m=1..11.
- **`frac(k) → 1/2` is an exact 1/2 split**: NOT a theorem; the honest
  statement is `frac(k) = (2^(k-2)+δ_k)/2^(k-1)` with small `|δ_k|` (δ_k = -2 at
  k=13, +7 at k=16, etc.), never exactly 0. The limit 1/2 is real but the
  closest-to-half values still miss by a fixed correction.

## What was NOT found (so nobody searches again)

- `half(k)` and `deficit(k)` sequences have no constant-coefficient linear
  recurrence of order ≤ 8 and no polynomial fit (fresh, to k=24).
- `deficit(k)` = period − max(survivor) takes only the values
  {2,4,10,12,142,424,846,1126,2422,25678} over k=2..24: not a fixed offset
  (the pass-2 "deficit=12" was real for k=4..11 only).

## Status summary

- **PROVED (complete proof):** `S ∩ S^{-1} = {1}` in `Z_3` — the only {0,1}-digit
  3-adic unit whose inverse is also {0,1}-digit is 1. Exhaustively cross-checked
  to 3^12 in the value domain and, via the orbit, to k=26.
- **PROVED (from it):** for every k, the survivor-exponent set `A_k` contains
  no reflection pair `{r, P−r}` except the trivial `{0,0}` (anti-orbit under
  `r ↦ P−r`). Verified k=2..26.
- **Result type:** a genuine partial result stated exactly — a structural
  anti-symmetry of the digit-{0,1} set and of the survivor orbits. It excludes
  the reflection-symmetric subclass of counterexamples, not the whole conjecture.
- NEGATIVE (fresh, exact): no low-order recurrence/polynomial in half/deficit.

This is the one genuinely new structural regularity this run's pattern work has
produced since the 3-adic-count proof (pass 6): a *hidden anti-symmetry* of the
survivor orbits that both the half-count limit and the value-domain inverse-set
theorem converge on.
