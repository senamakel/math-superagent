# Pattern-finder fourth pass — carry-count sequence on the ×2 transducer

Follow-on to `regularity_findings_3.md`. The live route (GOAL.md /
research/backward/erdos-via-symbolic-invariant.md) is a finite-transducer
statistic along the ×2 base-3 carry. This pass computed the natural first such
statistic — the **carry-count sequence** `c(n)` = number of base-3 carries when
doubling `2^n` to obtain `2^(n+1)` — which the run had not yet produced, and ran
the exact sequence tools on it. Also re-derived a proved equivalence.

## The fresh sequence and its (negative) structure

`c(n)` for n=0..120:
`0,2,0,3,3,2,2,5,0,5,3,6,7,3,3,11,5,9,4,10,6,10,11,8,4,6,5,10,10,10,12,...`

- `analyze_sequence`: differences never become constant → not a low-degree
  polynomial. Leading ratio fluctuates → not simple exponential.
- `find_linear_recurrence` (max order 12, 121 terms): **no constant-coefficient
  linear recurrence of order ≤ 12**.
- `oeis_lookup` on [0,2,0,3,3,2,2,5,0,5,3,6,7,3,3,11]: **not catalogued**.

So the carry statistic — like the digit counts c0,c1,c2 before it — has no
low-order linear/polynomial/OEIS structure. This is a genuine negative the
symbolic-invariant route must work around: the statistic cannot be proposed as
an exact low-order-recurrent threshold.

## The one exact result this pass establishes (PROVED)

**E — `c(n) = 0  ⟺  2^n` is digit-{0,1}-free (i.e. `digit_free(2^n)`).**

Proof (exact, not a fit): the base-3 digits of `2^(n+1)` are obtained by
doubling each digit of `2^n` with carries. At digit position i, an internal
carry-in is generated exactly when `2·d_i ∈ {4}` from `d_i = 2` (the only digit
with `2·d_i ≥ 3` among `{0,1,2}`), and with carry-in 0 so far every step the
future carry stays 0 iff no `d_i = 2` appears. A leading (length-growing) carry
would require a leading digit 2, impossible once all digits are in {0,1}
(leading digit of 2^n is always 1 for n ≥ 1; for n = 0 it is 1). Hence no base-3
carry occurs while doubling `2^n` iff every ternary digit of `2^n` lies in
{0,1}.

- Verified exactly: over n = 0..3000, `(c(n)==0) == digit_free(2^n)` with **zero
  mismatches**; digit-free n are exactly {0, 2, 8} in this range, each with
  c(n)=0.
- NOTE on value: this is a correct reformulation, but it is essentially the
  definition in carry language — it restates "no digit 2" as "no carry". It does
  not separate survivor paths from the tail beyond what `digit_free` itself does.
  Recorded as proved, but low-mileage: it re-encodes the same predicate.

(Reproduction check: survivor sets A_k recomputed here match the run exactly —
k=6 first=[0,2,8,20,24,26,56,62], k=8 first=[0,2,8,24,26,72,80,126], |A_k|=2^(k-1)
for k≤8; oracle_verify.captured.txt confirms |A_k|=2^(k-1) and finite_check
[1,1000]={2,8}. All consistent.)

```claim
id: carry-count-zero-iff-digitfree
statement: Let c(n) be the number of base-3 carries generated while doubling
  the ternary expansion of 2^n to obtain that of 2^(n+1). Then c(n) = 0 if and
  only if the base-3 expansion of 2^n avoids the digit 2 (i.e. digit_free(2^n)).
  Proof: doubling digit d produces a carry iff 2d >= 3, which among {0,1,2}
  happens exactly when d = 2; with carry-in 0 the future stays carry-free iff no
  d_i = 2 appears, and a leading (length-gaining) carry would need a leading
  digit 2, impossible once all digits are in {0,1} (the leading digit of 2^n is
  always 1 for n >= 1). So c(n)=0 iff every ternary digit of 2^n is in {0,1}.
hypotheses: n >= 0 a nonnegative integer.
holds-here: yes — exact for all n; verified (c(n)==0) == digit_free(2^n) for
  every n in [0,3000], zero mismatches; digit-free n in that range are exactly
  {0,2,8}.
status: proved (it is a carry-language restatement of the digit-2-free
  predicate; low independent value because it re-encodes the same condition).
bearing: gives the ×2 transducer one exact handle (no carry <-> no digit 2) but
  does not separate the survivor paths {0,2,8} from the tail beyond digit_free
  itself; recorded so nobody re-proposes "number of carries" as a new invariant.
anchor: code/out/regularity_findings_4.md
```

## What survives this pass / is closed

- PROVED (this pass): E — c(n)=0 ⟺ digit_free(2^n) (a reformulation, low value).
- CONFIRMED on fresh data: survivor sets, |A_k|=2^(k-1), c1-even.
- NEGATIVE (this pass): c(n) has no order-≤12 linear recurrence, no polynomial
  fit, not in OEIS. Recorded so nobody searches these again.

## Standing regularities (unchanged from prior passes, all exact)

- PROVED: c1(n) even for all n ≥ 1.
- PROVED (modular identity): c0 ≡ c2 + L(n) (mod 2), L = number of ternary digits.
- PROVED (bijection): |A_k| = 2^(k-1); sieve cannot close by counting.
- REFUTED: #{c0 odd} == #{c2 odd} (crossing, not a law); c0≡c2 mod 2; max-survivor
  deficit is not a fixed invariant; survivors fill every even 2-adic class.
- NEGATIVE: c0,c1,c2,c(n) each have no low-order linear recurrence / polynomial
  fit; none of them catalogued (carry-count newly so).
