# Pattern-finder deliverable: the prime fold weight is √n-scaled subgaussian white noise

All numerics below are **exact** over `n = 3..40000` from the canonical
`code/out/nu2_primes_xor_40000.json` (guards ν₂(53)=18, ν₂(64)=27,
ν₂(4000)=1975, ν₂(40000)=20081 all pass). Every statement is a **measured
conjecture** over that finite range, never a proof.

## Setup (exact identities)
- h = prime gap-parity string, h[j] = [q_{j+1} ≠ q_j mod 4].
- Fold cell T(n,d) = XOR over submasks o⊆d of h[n−1−d+o].
- ν₂(n) = #{ d ∈ [2,n−1] : T(n,d)=1 } = wt(Φ_n h).
- S(n) = Σ_{d=2}^{n−1} (−1)^{T(n,d)} = (n−2) − 2ν₂(n). Hence exactly
  `ν₂(n)/n = 1/2 − 1/n − S(n)/(2n)`.
- Z(n) = S(n)/√n (normalized fluctuation).

## The finding: Z(n) is mean-zero white noise with E[Z²]=1 and subgaussian tail

| object | value over n=3..40000 | random-walk prediction | white-noise √n prediction |
|---|---|---|---|
| E[Z(n)²] | 0.999 | growing | 1 |
| kurtosis E[Z⁴]/(E[Z²])² | 2.95 | — | 3 (Gaussian) |
| P(\|Z\|>4) | 0 / 39998 | — | ~e^{-8}≈0.0003 |
| corr(S(n),S(n+1)) | 0.0002 | **≈1** | ≈0 |
| corr(S(n),S(n+k)) k=1..6 | all \|r\|<0.005 | ≈1 | 0 |
| corr(Z(n),Z(n+1)) | −0.008 | — | 0 |
| increment AC1 of dS | **−0.5009** | ~0 | **−1/2** |
| Var(dS)/n | →2.0 | — | 2 |
| mean S²/n (prefix) | 0.999 | growing | 1 |
| max\|S\| / √n | 3.815 @27624 | unbounded | ~4 |
| max\|S\| | 712 @36972 | ~√n | ~c√n |

## Why the two earlier "contradictions" reconcile

The run had reported S as (i) E[S²]≈n (random-walk-like variance) yet (ii)
structureless with no dyadic self-sim. The decisive test here settles it:
`corr(S(n), S(n+1)) = 0.0002 ≈ 0`, which a random walk would never give
(corr≈1). The truth is `S(n) = √n · Z(n)` with Z **white**: Var(S)~n but
consecutive S are uncorrelated because Z is. That simultaneously gives
- `corr(S(n),S(n+k)) ≈ 0` (because Z is white), and
- `AC1(dS) = −1/2` (the exact white-noise signature), and
- `Var(dS)/n → 2 = Var(Z(n+1))+Var(Z(n))`, and
- `E[S²]/n → E[Z²] = 1`.

The model `ν₂(n)/n = 1/2 − 1/n − Z(n)/(2√n)` with Z subgaussian white
reproduces ν₂(40000)/40000: measured 0.502025, predicted 0.50202.

## Bearing on SUPPLY (why this is the right structure)

- SUPPLY asks for ν₂(n) ≥ c·n. The identity gives ν₂(n)/n = 1/2 − Z/(2√n) − 1/n.
  So **ν₂/n → 1/2 regardless**, at rate 1/2√n. A violation ν₂/n < c needs
  Z(n) > 2(1/2−c)√n, i.e. an excursion of Z beyond a growing threshold.
- `E[Z²]=1` (the second-moment plateau) is exactly the input from which
  **density-1 SUPPLY** follows by Chebyshev: for any δ>0, the set
  {n : |S(n)| ≥ 2δ·n} has density ≤ 1/(4δ²n} → 0, so ν₂/n ≥ 1/2−δ−o(1) on a
  density-1 set.
- **Subgaussian tail upgrades density-1 to finiteness of every exceptional
  set:** P(|Z|>x) ≤ C e^{−cx²} with E[Z²]=1 would give
  Σ_n P(|Z(n)| > 2(1/2−c)√n) < ∞, i.e. {ν₂/n < c} finite for every fixed c<1/2.
  Measured: {ν₂/n<0.48} has last member n=5655; {ν₂/n<0.49} last 27624; tail
  min ν₂/n over [30000,40000] = 0.4901.

## What is NOT established
- `E[S(n)²] ≤ C·n` is **proved for uniform-random h** (rank fact, Φ_n surjective
  ⇒ wt exactly Binomial(n−2,1/2), Var=(n−2)/4) — a settled class — but for the
  real prime h it is **open**, and this white-noise model is that same second-
  moment content, read as a measured conjecture. The open arithmetic input is
  unchanged: prove E[S(n)²] = O(n) for the prime gap-parity string, or a
  subgaussian/ exponential-tail bound on Z.
- This touches none of the five closed doors: it is a measurement of the prime
  input, not a "complexity of h" hypothesis; the paradoxes it resolves
  (whiteness vs. variance growth) are about the statistic S, not about forcing
  φ-large weight from h.

## Falsifier / attack
The conjecture to break: that Z(n) has a uniform subgaussian/exponential tail
(equivalently E[S²]=O(n) with exponential concentration). The smallest thing
that would falsify finiteness of exceptional sets is a single large n with
ν₂(n)/n < 0.48 (equivalently S(n) > 0.04n). None exists through n=40000
(largest ν₂/n<0.48 is at n=5655). A counterexample family would be a
prime-realizable h injecting dyadic-period structure — the only class known
(sublinear Thue–Morse, closed door 4) to break the plateau.

## The one thing this note left implicit, now stated (directive 31)

**`E[S(n)²] = O(n)` alone gives density-1 SUPPLY, not pointwise SUPPLY.**
By Chebyshev, `P(|S(n)| ≥ δn) ≤ E[S²]/(δ²n²) = O(1/n)`, so the exceptional
set `{n : |S(n)| ≥ δn}` has zero Cesàro density — hence `ν₂/n ≥ 1/2 − δ` on a
density-1 set. The density-0 exceptional set may still be infinite, so this is
**not** pointwise SUPPLY. Pointwise SUPPLY (finitely many exceptions, `ν₂/n ≥ c`
for *all* large n and every `c < 1/2`) needs the stronger uniform
subgaussian/exponential tail on `Z(n)`, which by Borel–Cantelli
(`Σ_n P(|Z(n)| > δ√n) < ∞`) makes every exceptional set `{ν₂/n < c}` *finite*.
These are two different results and must never be conflated.

```claim
id: prime-E-S2-On-sharp-conjecture
statement: For the prime gap-parity string h, E[S(n)²] = O(n) with
  S(n) = (n−2) − 2ν₂(n) the signed excess — equivalently a uniform
  subgaussian or exponential tail on the normalized fluctuation
  Z(n) = S(n)/√n. The two sides are NOT equal in strength: E[S(n)²]=O(n)
  alone gives density-1 SUPPLY (ν₂/n → 1/2 on a density-1 set via
  Chebyshev), NOT pointwise SUPPLY; the stronger subgaussian/exponential
  tail gives Σ_n P(|Z(n)|>δ√n) < ∞, hence every exceptional set
  {ν₂/n < c}, c<1/2, is finite — full pointwise SUPPLY.
hypotheses: prime gap-parity string h[j]=[q_{j+1}≠q_j mod 4]; checked
  ceiling N=40000; canonical oracle guards ν₂(53)=18, ν₂(64)=27,
  ν₂(4000)=1975, ν₂(40000)=20081; convention d∈[2,n−1].
holds-here: prime side — measured-not-proved (E[Z²]=0.999, kurtosis 2.95,
  P(|Z|>4)=0 over n=3..40000); uniform side — proved for all n
  (rank Φ_n=n−2 ⇒ wt(Φ_n h) exactly Binomial(n−2,1/2) ⇒ E[S²]=n−2
  exactly, so E[S²]=O(n)).
status: measured-not-proved (prime h, n≤40000); proved (uniform h, all n)
bearing: this is the SAME second-moment content as the open arithmetic
  input (A) E[S(n)²]=O(n) — the geometry side F_n(z)=O(n) is already
  proved (fold-distance-enumerator-On), so (A) is the single remaining
  open input; restating it as a subgaussian tail on Z does not weaken it.
  Falsifier: a single n with ν₂(n)/n < 0.48 (i.e. S(n) > 0.04n − 2); none
  exists through n=40000, largest ν₂/n<0.48 at n=5655. A counterexample
  family would be a prime-realizable h injecting dyadic-period structure
  (the only known class to break the plateau — sublinear Thue–Morse,
  closed door 4).
anchor: code/out/pattern_normalized_white_noise.md;
  research/claims_normalized_white_noise.md
```
