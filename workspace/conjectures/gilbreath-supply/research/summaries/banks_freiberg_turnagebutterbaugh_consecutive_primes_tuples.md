# Banks–Freiberg–Turnage-Butterbaugh — Consecutive primes in tuples

<!-- source: https://arxiv.org/pdf/1311.7003 | Acta Arith. 167 (2015) 261–266 -->

## What it establishes

Deduces from Maynard–Tao that an admissible `k`-tuple of linear forms
`{gn + hj}` contains **at least m consecutive primes** infinitely often, once
`k` is large enough in terms of `m`.

Its three concrete consequences:

- **Corollary 1 (Erdős–Turán).** For every `m ≥ 2` there are infinitely many
  runs of `m` consecutive prime gaps that are strictly increasing, and
  infinitely many strictly decreasing.
- **Corollary 2.** Infinitely many runs with each gap dividing the next (and
  the reverse).
- **Corollary 3 (congruence-class strings, with density).** For coprime `a, D ≥ 3`,
  for every `m ≥ 2` there are infinitely many `r` with
  `pr+1 ≡ ... ≡ pr+m ≡ a (mod D)` and `pr+m − pr ≤ D · C_m`, `C_m` depending only on `m`.

## Why it concerns SUPPLY

Corollary 3 is a *bounded-gap converged-string* strengthening of the
Shiu/Maynard equal-residue rungs: not only do long strings of congruent primes
exist (Shiu, Maynard), they can be chosen with **uniformly bounded gap**
`≤ D·C_m`. For fixed `D` (say 4) this makes `h` constant over a bounded-length
window — so runs of equal `h` are not just positive-density (Maynard) but occur
in tight clumps of bounded span.

Same caveat as Maynard: this is the *equal-residue* direction. It reinforces
closed door #2 — arbitrarily long (indeed positive-density, now bounded-gap)
constant runs in `h` — and therefore that no "no long constant runs" hypothesis
can prove SUPPLY. It does not bear on the switch direction.

The Erdős–Turán gap-monotonicity results are context for the structure of
`h`: with bounded monotone gaps, `h[j]` (gap-parity mod 2) takes frequent and
uncontrolled values — another facet of why the fold `Φ` is doing genuinely
interesting work rather than reading a simple `h`.

## Hypotheses that hold here

- Admissibility: for `{gj + hj}` with `(g, product) = 1` and `g` the admissible
  shift, holds. Uniform over `D` up to constants.
- Unconditional (Maynard–Tao sieve, Bombieri–Vinogradov).

```claim
id: bftb-bounded-gap-equal-residue-strings
statement: For coprime integers a and D >= 3, for every m >= 2 there are infinitely many r with p_{r+1} == ... == p_{r+m} == a (mod D) and p_{r+m} - p_r <= D·C_m, where C_m is a constant depending only on m. (Consequence of Maynard-Tao, via BFTB Theorem 1; deduced from an admissible k-tuple of linear forms with k >= k_m.)
hypotheses: gcd(a,D)=1, D >= 3, m >= 2, k >= k_m (Maynard-Tao admissible k-tuple); unconditional via Bombieri-Vinogradov.
holds-here: yes — for D=4 this makes the prime gap-parity string h constant (equal-residue -> gap divisible by 4 -> h = 0) over bounded-length windows of span <= 4·C_m, infinitely often.
status: proved (corollary of proved Maynard-Tao; the deduction chain Theorem 1 -> Corollary 3 is given in the paper)
bearing: Strengthens closed door 2 ("no long constant runs"): not only do arbitrarily long constant runs in h exist (Shiu), they occur with uniformly bounded gap. Refutes any "no long constant runs" or "h varies enough" hypothesis outright. Equal-residue side only — does not touch the switch direction, which is the live barrier.
anchor: research/sources/banks_freiberg_turnagebutterbaugh_consecutive_primes_tuples.full.md Theorem 1 & Corollary 3 (lines 40-60, 150-160)
follows-from: maynard-positive-density-congruent-strings
contradicts: <none>
answers: <none>
```

## Full text

`research/sources/banks_freiberg_turnagebutterbaugh_consecutive_primes_tuples.full.md`
