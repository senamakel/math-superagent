# Torquato, Zhang, De Courcy-Ireland — "Hidden multiscale order in the primes"

**Source:** arXiv:1804.06279 (full PDF). Published as J. Phys. A: Math. Theor. 52 (2019) 135002, doi 10.1088/1751-8121/ab0588.
**Full text:** `research/sources/torquato-zhang-decourcy-ireland-hidden-multiscale-order-primes.full.md`

## What this establishes (condensed, conditional on Hardy–Littlewood)

The paper studies the **pair correlations of the primes** in an interval
`M ≤ p ≤ M+L`, in the scaling `M→∞, L/M→β>0` (i.e. long intervals comparable
to their location, not the consecutive-prime or short-interval regime itself).

- **Prop 1 (the structure factor), conditional on the Hardy–Littlewood prime-pair
  conjecture:** the limiting structure factor `S(k)/ρ` of the primes in such an
  interval is a finite union of periodic components, so `S(k)` carries a **dense
  set of Dirac-delta peaks at rational values of `k/π`**. This is the exact
  fingerprint of an *effectively limit-periodic* point process (Bragg-like /
  quasicrystal-like pure-point diffraction).
- **Prop 2:** in the infinite-size limit the primes in these intervals form a
  **hyperuniform point process of class II** — density fluctuations at large
  scales are anomalously suppressed compared to a Poisson (uncorrelated) system.
- **Prop 3 (order metric):** the scalar order metric `τ` shows a **transition**:
  strong order when `L` is comparable to `M`, effectively uncorrelated
  (Poisson / Gallagher) behaviour when `L` is only logarithmic in `M`.
- Constructs an **algorithm to reconstruct primes in a dyadic interval** from the
  limit-periodic structure factor.

## Why this is in the library

The run's single open gap (REQUESTS.md, G-supply) is a **lower bound on the
two-point mod-4 correlation of consecutive primes** — the switch-bit frequency
`gap ≡ 2 (mod 4)` — which REQUESTS itself declares is a *named-open, intrinsically
two-point* problem, provably NOT a one-point statistic. This is a primary,
peer-reviewed-venue treatment of the **two-point (pair) structure of the primes
conditional on Hardy–Littlewood** — the same conjecture the run's conditional
Route B deliverable names as its hypothesis.

## What it does NOT settle (bounded claim)

- It does **not** prove any lower bound on consecutive-prime residue switches
  mod 4, and does not change the REQUESTS status of that gap (still open,
  conditional framing stands). The gap is named-open; nothing closes it.
- Its scaling regime (`L ~ M`, long intervals) is **different from** the
  consecutive-prime mod-4 regime the gap lives in. It corroborates the
  Hardy–Littlewood conditional framing of two-point prime structure at large
  scale; it is not a consecutive-gap mod-4 frequency theorem.
- Consequently it is corroborating *context* for the conditional Route B
  deliverable, not a route that closes the gap.

## Claim block

```claim
id: torquato-2019-hl-conditional-pair-structure
statement: Conditional on the Hardy–Littlewood prime-pair conjecture, the primes in an interval M≤p≤M+L with M→∞, L/M→β>0 form an effectively limit-periodic point configuration: the structure factor is a finite union of periodic components with a dense set of Dirac-delta peaks at rational k/π (Prop 1), the process is hyperuniform of class II (Prop 2), and the order metric τ shows a transition from ordered (L comparable to M) to uncorrelated/Poisson (L logarithmic in M) (Prop 3).
hypotheses: Hardy–Littlewood prime-pair conjecture; long-interval scaling L/M → β > 0; dyadic intervals for the reconstruction algorithm.
holds-here: partially — corroborates that the two-point structure of the primes is governed (conditionally) by Hardy–Littlewood at the large-scale limit, which is the same conjecture the run's conditional Route B deliverable rests on; but the paper's interval scaling is NOT the consecutive-prime mod-4 regime of the G-supply gap, so it does not close that gap or change its named-open status.
status: sourced (primary, arXiv v + J. Phys. A; conditional on HL — the conditional flag is the paper's own)
bearing: strengthens the honesty/framing of the conditional Route B deliverable (the two-point prime structure is exactly Hardy–Littlewood-driven); does NOT supply the unconditional or consecutive-gap mod-4 lower bound REQUESTS lists as the only unmet need.
anchor: research/sources/torquato-zhang-decourcy-ireland-hidden-multiscale-order-primes.full.md
```

## Statements / names to reuse

- Effectively limit-periodic; hyperuniformity class II; structure factor `S(k)`;
  scalar order metric `τ`; dyadic-interval reconstruction.
- Authors: Salvatore Torquato (Princeton, chemistry/physics), Ge Zhang,
  Matthew De Courcy-Ireland (Princeton math) — 2019.
- Related easier preprint (also by them): "Uncovering multiscale order in the
  prime numbers via scattering" (arXiv:1802.10498), which introduced the
  effectively-limit-periodic / hyperuniform primes concept. (Not yet in the
  library; the J. Phys. A paper is the fuller treatment.)
