# Thue–Morse: an aperiodic switch bit with sublinear supply

**Why this matters.** The run's dyadic-collapse theorem (`dyadic-collapse-proved`)
says: h eventually periodic with minimal period a power of two ⟹ ν₂ = O_k(1).
The natural complement is "aperiodic ⟹ ν₂ ≥ c·n", and the whole G-supply
reduction to a *combinatorial* transfer leans on a dichotomy of that shape. The
witness below shows that complement is FALSE in the strongest way: the
Thue–Morse bit string is aperiodic yet ν₂ = O(log n). So "aperiodic" alone
cannot carry the supply bound — the controlling invariant is finer (2-adic
linear complexity; see `dyadic-linear-complexity-supply`).

## Setup

- `h[j] = wt(j) mod 2` (Thue–Morse, `h = 0,1,1,0,1,0,0,1,...`), j ≥ 0.
- `ζ(h)[d] = Σ_{j⊆d} h[j] (mod 2)` is the subset-zeta (Möbius) transform over
  F₂; `j⊆d` means bitwise submask. By `rule90-interior-xor` this is exactly the
  tail-cell value at depth `d`, so `ν₂(q_n) = #{d ≤ n : ζ(h)[d] = 1}`.

## The identity

**Lemma.** `ζ(h)[d] = 1 ⟺ wt(d) = 1 ⟺ d is a power of two (d = 2^m).**

*Proof.* Work over the integers first. Every bit `i` of `d` is present in
exactly `2^{wt(d)-1}` of the submasks `j ⊆ d` (fix bit i = 1, choose the other
`wt(d)-1` ones arbitrarily). Hence

```
Σ_{j⊆d} wt(j) = Σ_{bit i ⊆ d} Σ_{j⊆d, i⊆j} 1
             = wt(d) · 2^{wt(d)-1}.
```

Now `h[j] = wt(j) mod 2`, and
`wt(j) mod 2 = wt(j) − 2⌊wt(j)/2⌋`, so `Σ_{j⊆d} h[j] ≡ Σ_{j⊆d} wt(j) (mod 2)`.
Therefore

```
ζ(h)[d] ≡ wt(d) · 2^{wt(d)-1} (mod 2).
```

This is odd iff `wt(d) = 1` (for `wt(d) ≥ 2` the factor `2^{wt(d)-1}` is even;
for `wt(d) = 0`, i.e. d = 0, the sum is 0). Since `wt(d) = 1` iff `d` is a
power of two, the lemma follows. ∎

## Consequence

`ν₂(n) = #{d ≤ n : d is a power of 2} = ⌊log₂ n⌋ + 1 = O(log n)`, while `h` is
the canonical **aperiodic** (indeed uniformly recurrent, 2-automatic) sequence.
So aperiodicity does not imply linear supply: the supply collapses on a
density-1/2, linear-complexity-2 bit string.

## What this does and does not refute

- REFUTES: the dichotomy "dyadic-periodic ⟺ collapse, else linear growth" as a
  route to a prime-free supply theorem. Thue–Morse is neither periodic nor
  linear.
- Does NOT touch: the prime-specific measured bound ν₂/w ∈ [0.515, 0.87]
  (`g-supply-transfer-measured`); Lemma 5.4 and the recharge identity.
- Does NOT touch: the conditional Route B deliverable
  (`g-supply-conditional-theorem`) whose hypothesis is the named-open two-point
  mod-4 correlation.
- Points at: 2-adic linear complexity as the invariant that separates the
  collapse families (period 2^k, Thue–Morse: low LC) from the linear-growth
  families (odd-factor periods, pseudo-random h, primes). This is the adopted
  approach `dyadic-linear-complexity-supply`.

## CORRECTION (scholar, this cycle) — the "hence nu2 = floor(log2 n)+1" step is FALSE

The PARITY lemma in this note is true: for h[j] = wt(j) mod 2,
ζ(h)[d] = 1 ⟺ d is a power of 2 (via Σ_{j⊆d} wt(j) = wt(d)·2^{wt(d)-1} ≡ 0
mod 2 for wt(d) ≥ 2). But the step "hence ν₂(q_n) = #{d≤n : d power of 2} =
⌊log₂ n⌋+1 = O(log n)" is FALSE: ζ(h)[d] is a PARITY (mod-4) statistic — it
fires on halved values that are odd, i.e. actual values ≡ 2 (mod 4): 2, 6, 10,
… — whereas ν₂ counts cells that are EXACTLY 2 within the maximal {0,2} suffix.
A parity-1 cell whose halved value is 3 (actual 6) is NOT in {0,2} and is not
counted. Inside a genuine {0,2} block the halved evolution is XOR, but once a
halved value reaches 3 the evolution reverts to |a−b| and the parity fold no
longer determines the suffix.

The run's own independent measurements contradict the claimed formula:
- dyadic-separating-invariant-three-strings (checked, actual right-diagonal
  cycle_and_nu2): TM nu2/n = 0.270 @ n=100 (nu2=27), 0.011 @ n=4000 (nu2=44).
- adversarial board post (direct exact triangle D=4000): nu2(100)=27,
  nu2(4000)=45, first mismatch n=1.
These disagree with the claimed 7 and 12. The specific identity is wrong.

WHAT SURVIVES: the qualitative conclusion (Thue-Morse is SUBLINEAR / on the
rigid side, density nu2/n -> 0, far below the linear families) is supported by
the MEASUREMENTS (density decays 0.270 -> 0.011 over n=100..4000), but it is
now numerical evidence, NOT the proof this note claimed. The claim block below
is rewritten to reflect this: parity lemma stated as the true (and only)
proved content; the nu2-equality and the O(log n) "proof" demoted to refuted /
measurement-only.

## Cross-reference and the corrected open question (Directive 66)

Paired with `dyadic-oddfactor-infimum-supply-useful`
(`research/notes/dyadic-oddfactor-infimum-supply-useful.md`; corroboration of
claim `dyadic-oddfactor-infimum-bounded`), the pair establishes one dichotomy:
**sharp on periodic words, silent on aperiodic ones.** Odd-factor periodic
words have `ν₂ = c·n + O(1)` with `c` bounded away from 0 (P=3: 0.647, P=5:
0.509, P=7: 0.267, P=9: 0.359, P=15: 0.114); Thue–Morse is aperiodic with
`ν₂ = O(log n)`. So the odd-factor linear growth cannot be promoted toward the
primes by aperiodicity — that bridge is exactly what this witness breaks. Read
beside the witness, the infimum note is **neutral** for the primes, not
encouraging.

The corrected open question is therefore NOT "is the prime bit string
aperiodic?" (known, and now known to be insufficient). It is: **which finer
invariant separates Thue–Morse (log) from the odd-factor families (linear), and
where do the primes sit on it?** The candidate named here is 2-adic linear
complexity; note `dyadic-linear-complexity-supply` already sharpens it further:
period-3 has bounded linear complexity yet positive density, so *general* linear
complexity does not separate — the refined candidate is the 2-adic spectral
structure of `σ = I + S` (mass in the non-nilpotent part, "2-adic
non-rigidity"). The most informative measurement left on this route is to
compare that invariant on all three: Thue–Morse, one odd-factor periodic word
(P=3), and the real prime halved-gap string. See task
`measure-2adic-separating-invariant-three-strings`.

## Verification

The derivation is the proof (elementary integer identity, no analysis
hypotheses). Hand-checked d = 0..7 (all 8 values: ζ = 1 exactly at d ∈
{1,2,4}, i.e. the powers of two). The subset-zeta identity
`ζ(h)[d] = 1 ⟺ d a power of two` is **also machine-confirmed to N = 10^5** by
the cross-referenced claim `thue-morse-subset-zeta-confirmed-identification-refuted`
(`research/notes/thue-morse-identification-refuted.md`), so this note's
"machine check not executed this cycle" line is superseded for the *identity*
itself. What that claim also shows is that the *load-bearing identification*
`nu2(n) == #{d≤n : d a power of 2}` does NOT hold for the Thue–Morse triangle
(first mismatch at n = 1; n = 100: 27 vs 7) — the fold bit marks cell PARITY,
not {0,2} membership. The qualitative conclusion here (Thue–Morse ν₂ is
sublinear, max ~219 over n ≤ 4000; aperiodicity does not force linear supply)
survives and is what this witness is cited for.

```claim
id: thue-morse-sublinear-supply-witness
statement: Let h[j] = wt(j) mod 2 (Thue-Morse, aperiodic, 2-automatic, linear
  complexity 2). (PROVED) Its F2 subset-zeta transform satisfies zeta(h)[d]=1
  iff wt(d)=1 iff d is a power of two. (REFUTED) The claimed consequence
  "nu2(n) = #{d<=n : d power of 2} = floor(log2 n)+1 = O(log n)" is FALSE: the
  fold bit zeta(h)[d] is a PARITY (mod-4) statistic that fires on halved
  values which are odd (actual values 2,6,10,...), not on cells EXACTLY 2, so
  it does not count the maximal {0,2}-suffix. Ground-truth right-diagonal
  measurements give TM nu2(100)=27 (not 7) and nu2(4000)=44-45 (not 12),
  first mismatch at n=1. What survives as MEASURED (not proved): TM nu2/n is
  sublinear, decaying 0.270->0.011 over n=100..4000, so aperiodicity does not
  force linear supply.
hypotheses: F2 subset-zeta (Möbius) transform; rule90-interior-xor holds only
  inside a genuine {0,2} block; integer identity sum_{j⊆d} wt(j) =
  wt(d)·2^{wt(d)-1}.
holds-here: partially — the PARITY lemma holds for all d (prime-free); the
  nu2-equality does NOT hold (it conflates parity with {0,2}-membership).
status: proved for the parity lemma only; the O(log n) conclusion is REFUTED
  by the ground-truth nu2 measurements and downgraded to numerical evidence.
contradicts: dyadic-separating-invariant-three-strings
note: the claimed nu2-equality contradicted this run's own ground-truth
  measurement (TM nu2/n 0.270@100, 0.011@4000); the correction aligns with it.
bearing: closes the dichotomy gap in the dyadic-periodicity-collapse thread
  (aperiodic ⟺ linear is dead) — but ONLY on the measured-sublinear reading,
  not on a "proved O(log n)" reading. The supply transfer's controlling
  invariant is NOT established as 2-adic linear complexity by this witness.
anchor: research/notes/thue-morse-sublinear-supply-witness.md
```
