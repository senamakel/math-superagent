# Berthé–Holton–Zamboni — Initial powers of Sturmian sequences

**Source:** V. Berthé, C. Holton, L. Q. Zamboni, *Initial powers of Sturmian
sequences*, Acta Arith. 122 (2006); full text from the author's IRIF page at
`research/sources/berthe-holton-zamboni-initial-powers-sturmian.full.md`
(2016 lines).

## What it establishes

- **ice(ω)** — the *initial critical exponent* of a Sturmian sequence ω = limsup
  of the largest p such that u^p is a prefix of ω for arbitrarily long prefixes u.
  An explicit formula for ice(ω) in terms of the S-adic representation of ω
  (Ostrowski numeration): ω = T^{c1}∘τ0^{a1}∘T^{c2}∘τ1^{a2}∘…, (a_k) the partial
  quotients of the slope, (c_k) the Ostrowski digits of the intercept; the
  characteristic (standard) sequence is exactly the one with c_k = 0 for all k.
- **Theorem 1.1**: there is a Sturmian sequence of slope α with ice = 2 iff each
  pair (s,t), s>1, occurs as (a_k, a_{k+1}) or (1,1,t) as (a_k,a_{k+1},a_{k+2})
  only finitely often.
- **Theorem 1.2**: for the characteristic Sturmian sequence ω of slope α,
  ind*(α) = 1 + ice(ω), where ind* is the limit superior of maximal powers of
  length-n factors (the *index*).
- **Prop 2.1**: in a minimal shift, max over ω of ice(ω) = ind*(X); if X is
  infinite and minimal, some ω has ice(ω) ≤ 1 + θ = (3+√5)/2.
- The Fibonacci shift example (slope 2/(1+√5) — the run's 1/φ² slope): its
  characteristic sequence begins in no power ≥ (3+√5)/2 ≈ 2.618, while every
  non-characteristic sequence in the shift begins in arbitrarily long blocks
  repeated ≥ 3 times.

## Why it matters here

Cross-checks the already-held critical-exponent numbers: for the Fibonacci word,
ice = 1+φ (Mousavi–Schaeffer–Shallit Thm 3.25) and ind* = 2+φ (Thm 3.24),
consistent with Thm 1.2 (ind* = 1+ice). The S-adic/Ostrowski expansion is the
same numeration the run's Ostrowski-prefix axis uses. It is **not** the Ψ
observable: prefix powers are about repetitions at the start of the word, not
about the length-k factor set or its decimal second moment. Background
corroboration, no new engine for G4.

```claim
id: berthe-holton-zamboni-initial-critical-exponent
statement: For the characteristic Sturmian sequence omega of slope alpha,
ind*(alpha) = 1 + ice(omega) (Thm 1.2), where ice is the initial critical
exponent (limsup of prefix powers) and ind* the index (limsup of factor
powers); for the Fibonacci word (slope 1/phi^2) ice = 1+phi and ind* = 2+phi.
hypotheses: omega a Sturmian sequence of irrational slope alpha; characteristic
= standard = intercept 0.
holds-here: yes — PE1006's word is the characteristic Sturmian word of slope
1/phi^2; the ice/ind* values match the held Mousavi-Schaeffer-Shallit Thm
3.24/3.25 numbers (2+phi and 1+phi).
status: asserted (survey-level statement of the paper's main results)
bearing: Cross-check only; corroborates the critical-exponent facts already
claimed and the Ostrowski-numeration framework. Does not bear on the decimal
second moment Psi(k).
anchor: research/sources/berthe-holton-zamboni-initial-powers-sturmian.full.md
(Theorem 1.1 p.2, Theorem 1.2 p.3, Prop 2.1 p.5, Fibonacci example p.1-2)
```

## Boundaries

- The ice formula is stated in the S-adic representation; the full derivation
  (§3–§5) is a long case analysis. Not needed for PE1006.
- Slope convention: density of the symbol 1; the paper's "Fibonacci shift of
  slope 2/(1+√5)" matches the run's 1/φ² slope (2/(3+√5) = 1/φ² ≈ 0.382; note
  2/(1+√5) = 1/φ ≈ 0.618 is the *complement* — the example in the paper's
  introduction uses 2/(1+√5), so the ice/ind* values transfer to the
  complement word, whose factor set is the digit-complement of PE1006's).
