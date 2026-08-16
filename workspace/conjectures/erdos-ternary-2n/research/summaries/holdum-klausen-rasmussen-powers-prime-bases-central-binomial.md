# Holdum, Klausen & Rasmussen, "Powers in prime bases and a problem on central binomial coefficients"

Source: INTEGERS 15 (2015), Paper A43. Full text: `research/sources/holdum-klausen-rasmussen-powers-prime-bases-central-binomial.full.md`.

## The carry reformulation of Erdős's conjecture

**Kummer's theorem:** `v_p(binomial(2n,n))` = number of carries when `n` is added to itself in base `p`.

For `n = 2^k` and `p = 3`: adding `2^k` to itself in base 3 has **no carries** exactly when the base-3 expansion of `2^k` has no digit `2` (each column digit is 0+0, 1+1; no 2+something from a carry-in). Therefore:

> Erdős's ternary conjecture ⟺ `v_3(binomial(2^(k+1), 2^k)) = 0` for no `k > 8` (equivalently `binomial(2^(k+1),2^k)` not divisible by 4 or 9 for `k > 8`, up to the 2-part).

**Conjecture 1.1:** `binomial(2n,n)` is divisible by 4 or 9 for every `n > 4` except `n = 64` and `n = 256`.

**Theorem 1.2 (verified):** the above holds for every `n` with `4 < n ≤ 2^10^13` except `n = 64, 256`. This is a **distinct verified computational bound** (`n ≤ 2^(10^13)`, a different and in the n-exponent large bound) reaching further in the exponent than Saye's trailing-digit range in a complementary sense.

## What it gives the run

1. A **symbolic-invariant reformulation**: the invariant is "number of carries when `2^k` is added to itself in base 3". Preserved/controlled by the carry structure; zero carries ⟺ digit-2-free.
2. Their `S^a_p(n)` counting function bounds how many base-p digits exceed p/2; they improve Narkiewicz-type bounds and Kennedy–Cooper results in special cases.
3. Non-Wieferich base idea: if p is not a Wieferich prime base α, a digit-pattern system occurs on every digit — relevant to whether the middle digits are reachable.

## Claims

```claim
id: KUMMER-CARRY-REFORMULATION
statement: Erdős's ternary conjecture ⟺ v_3(binomial(2^(n+1), 2^n)) = 0 never
  holds for n > 8, i.e. for no k > 8 is binomial(2^k, 2^(k-1)) free of the
  factors 4 and 9. The invariant is the number of carries when 2^n is added to
  itself in base 3: zero carries ⟺ (2^n)_3 has no digit 2.
hypotheses: n a positive integer; via Kummer's theorem v_p(binomial(2m,m)) =
  number of carries adding m to itself in base p (here p=3).
holds-here: yes — exact reformulation, not an approximation.
status: proved (Kummer's theorem is exact; the reformulation is immediate)
bearing: reframes the goal as a carry-statistic on the base-3 self-sum of powers
  of 2 — a symbolic-invariant shape. HKR also bound S^a_p(n), the count of base-p
  digits exceeding p/2 (improving Narkiewicz-type bounds in special cases).
anchor: research/summaries/holdum-klausen-rasmussen-powers-prime-bases-central-binomial.md
```

## Status

Sourced, peer-reviewed (INTEGERS). Theorem 1.2 is a verified computation (n ≤ 2^10^13, a distinct, complementary bound) — evidence for a bounded instance, not a proof.
