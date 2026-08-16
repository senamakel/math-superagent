# Summary — Hidden multiscale order in the primes

Source: Torquato, Zhang, de Courcy-Ireland, *Hidden multiscale order in the primes*,
J. Phys. A: Math. Theor. 52 (2019) 135002, doi:10.1088/1751-8121/ab0588
(companion: *Uncovering multiscale order in the prime numbers via scattering*,
J. Stat. Mech. 2018). Full text: `[[torquato_hidden_multiscale_order_primes.full]]`.
Downloaded this run (librarian) from the FRONTIER's top-ranked prime-correlation tier.

## What this establishes

The pair correlations of the primes, studied through the **structure factor**
`S(k)` of primes in an interval `[M, M+L]` as `M → ∞` with `L/M → β > 0`.

**m = 2 case.** The two-point prime statistics (how often two primes differ by a
given shift `r`) are governed by the Hardy–Littlewood constant `S(H)` for
`H = {0, r}`: the count of `n` with `n`, `n+r` both prime is `∼ S({0,r})·X/(log X)²`.
The paper shows (conditionally on HL) that this pair statistic is exactly
captured by the structure-factor formula (Eq. 10), equivalent to HL's original
expression for `m=2`. Consequence: apparent "multiscale order" of the primes is
the limit-periodic / hyperuniform structure predicted by these HL constants —
they explain why the primes' density fluctuations are anomalously suppressed at
large scales relative to Poisson.

**Higher-order (m ≥ 2).** The m-tuple generalization — `# {n : n+h_1,…,n+h_m all
prime} ∼ S(H)·X/(log X)^m` with `S(H) = ∏_p (1 − ω(H;p)/p)/(1−1/p)^m` — is
flagged as the conjectural controlling input for order-m correlation. Only `m=1`
(prime number theorem) is proved; HL is used as the working framework for
`m ≥ 2` throughout, with Note on status: Maynard–Tao–Zhang/Polymath 8 give a
positive proportion of shifts, but not the exact constants.

## What it implies here

This is the same arithmetic input the reopened pass needs at order `K > 1`, but
delivered exactly where Lacasa left it conjectural:

- Lacasa (already digested) showed the **block frequencies** of gap residues are
  `Z`-normalised sums of HL constants `C(g₁,…,g_m)` and are NOT uniform for
  `m>1`. Torquato makes the companion point that these HL constants are also the
  correct pair (m=2) statistic of the primes themselves. Together they establish
  that **higher-order correlations of prime-gap residue sequences are
  conjecturally controlled by HL k-tuple constants**, while the order-1 (pair)
  frequency is open (Abgs §9). This is the candidate arithmetic input at
  order `K>1`.
- Neither paper reaches the fold `Φ` or `wt(Φ_n h)`. Both are properties of the
  prime gap / prime set alone. The fold's input `h[j]=((q_{j+1}−q_j)/2) mod 2`
  is a binary **projection** of the mod-6 gap residues, so the mod-6/
  mod-4 collapse caveat from the Lacasa digest applies unchanged: HL-controlled
  higher-order correlations of the *residue* sequence do not automatically
  survive projection to the *parity* bit the fold reads.

## What it does NOT settle

- No theorem for `m ≥ 2` (everything above `m=1` rests on the unproved HL
  conjecture). Do not present HL-control of order-K correlations as unconditional.
- Nothing about the fold matrix, `wt(Φ_n h)`, or `ν₂`.
- The "hidden order" is finite-interval / scale structure, distinct from the
  index-domain correlations the fold actually reads.

```claim
id: torquato-hl-k-tuple-controls-prime-correlations
statement: For the primes in an interval [M,M+L] with L/M → β > 0, the pair correlation g2(r) (m=2) is governed by the Hardy-Littlewood constant S({0,r}); equivalently # {n ≤ X : n, n+r prime} ∼ S({0,r})·X/(log X)², and this m=2 statistic is exactly captured by the structure-factor formula Eq. (10), equivalent to HL's original expression. For m ≥ 2, the m-tuple count # {n : n+h_1,...,n+h_m all prime} ∼ S(H)·X/(log X)^m, S(H)=∏_p(1−ω(H;p)/p)/(1−1/p)^m, is the conjectural controlling input for order-m correlation; only m=1 (PNT) is proved.
hypotheses: Hardy-Littlewood k-tuple conjecture (assumed for m ≥ 2); μ and S(H) as usual; intervals with L/M → β > 0.
holds-here: yes, in the sense it is the arithmetic-input side of the reopened question — it says order-m (m>1) correlations of the primes ARE conjecturally pinned by HL constants, in contrast to the order-1 pair frequency being open (Abgs §9). Whether it survives projection onto the gap-parity bit h the fold reads is NOT settled here and is the open transfer.
status: asserted (the m=2 equivalence is derived/-conditional on HL; there is no unconditional m≥2 theorem — the constants are the conjecture's content, not a proof).
bearing: supplies the companion arithmetic-input source for the reopened pass's K>1 territory: higher-order (m>1) correlations of prime gap residues/prime sets are HL-k-tuple-controlled (conjecturally), while the order-1 switch-density frequency is open. Combined with Lacasa's unconditional forbidden-gap-block enumeration, it frames the search for an input strictly weaker than pointwise mod-4 switch density that a K>1 fold functional could read.
anchor: torquato_hidden_multiscale_order_primes.full, §1 (structure factor, Eq. 10), §2 (HL representation, m=1..m≥2 status).
```

## Keyword map
Hardy-Littlewood k-tuple; structure factor; prime pair correlation; hyperuniformity; limit-periodic; multiscale order; order-m correlations.
