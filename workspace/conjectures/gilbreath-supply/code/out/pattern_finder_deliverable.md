# Pattern-finder deliverable: the fold-excess fluctuation is white, the collapse witnesses are random walks

**Role:** pattern-recognition specialist.

**Finding (exact over computed ranges, a conjecture to derive, not a proof):**
the operative statistic that separates the density-1-SUPPLY inputs from the
collapse witnesses is **corr(S(n), S(n+1))** (equivalently the vanishing of all
higher-lag increment autocorrelation), NOT the lag-1 increment autocorrelation
ACF1(D), which is −1/2 for the good and the bad alike.

## Setup (all exact integer / ratio arithmetic)

```
S(n) = (n−2) − 2·ν₂(n)      (signed excess of the floored submask fold)
D(n) = S(n+1) − S(n)          (its increment)
```

Data: `code/out/nu2_primes_xor_40000.json` (index `d[n]=ν₂(n)`, guards
ν₂(53)=18, ν₂(64)=27, ν₂(4000)=1975 reproduced); iid/single-1 via exact SOS
fold (`lib.supply_fold.s_sos`).

## The discriminator, measured

| input | corr(S(n),S(n+1)) | ACF1(D) | Σ\|ACF(D;k)\| k≥2 | var(S)/var(D) | grade |
| --- | --- | --- | --- | --- | --- |
| **primes** | **−0.053** | −0.501 | **0.08** | 0.500 | **good** (white; var=O(n)) |
| **iid p=0.5** | **0.018** | −0.476 | **0.15** | 0.512 | **good** |
| **single-1 (near kernel)** | **0.956** | −0.500 | **3.0** | **158** | **collapses** (\|S\|~1.3n) |

The sharp facts:

1. **corr(S(n),S(n+1)) ≈ 0 for the good inputs, ≈ 1 for the bad.** The primes
   (−0.053) and iid (0.018) are *not random walks*: successive values of S are
   essentially uncorrelated, so S fluctuates at the √n scale. The near-kernel
   single-1 input has corr = 0.956 — it *is* a near-perfect random walk, so |S|
   grows linearly and var(S) explodes. (This is the sharp form of the prior
   claim `g-normalized-fold-weight-white-noise`, which recorded corr(S(n),
   S(n+1))=0.0002 for the primes.)

2. **ACF1(D) = −1/2 does NOT discriminate.** It is −0.500 for the single-1
   near-kernel input too — fold-generic. My first framing ("ACF1=−1/2 is the
   structure") was wrong, and this is the correction. The discriminator is the
   *vanishing of all higher-lag* increment autocorrelation: Σ\|ACF(D;k≥2)\| =
   0.08 (primes) vs 3.0 (single-1), which is what makes corr(S(n),S(n+1))≈0
   instead of ≈1.

3. **var(S) = O(n) ⟺ white increments.** A random walk gives var(S)≈N·var(D);
   white increments with lag-1 anticorrelation −1/2 cancel to var(S)≈var(D)/2.
   Measured: var(S)/var(D) = 0.500 (primes, converging to 1/2 from below:
   0.477@2000 → 0.500@40000) vs 158 (single-1).

## Why this is the honest boundary of the run's attack

- This is a **measured characterization** of which inputs satisfy density-1
  SUPPLY's second-moment input: the input's fold-excess S must be a non-random
  walk (corr(S,S⁺¹)≈0, white increments). The primes have it; every collapse
  witness (single-1, alternating, Thue-Morse) is a random walk.
- It does **not** reopen any closed door, and it is **not** a hypothesis that
  "h is complicated enough": the single-1 input is maximally simple and
  collapses, while iid (rich) is good — the structure being named is a property
  of the *output* S, not a complexity-of-input claim. It is precisely the
  statistic `E[S²]=O(n)` (density-1 SUPPLY) whose mechanism is now visible.
- The unconditional constant for the real primes — proving corr(S(n),S(n+1))→0
  (increments white) from an arithmetic input on h — **remains open and is
  unchanged**. This finding names the precise quantity to prove, not a proof of
  it.

## Status

- **Exact** over the terms supplied (n ≤ 40000 primes; iid/single-1 at
  n ≤ 3000).
- **A conjecture to derive**: whether the primes' increments stay white and
  corr(S(n),S(n+1))→0 as n→∞ is an arithmetic statement about the prime
  gap-parity string h, not established.
- The separation (good ≈ white, bad ≈ random walk) is robust across the
  computed ranges and independent of the exact constants.
