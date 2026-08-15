# Rubinstein & Sarnak 1994, "Chebyshev's Bias"

**Full text (primary, clean & readable):** `research/sources/rubinstein-sarnak-1994-chebyshev-bias-full.full.md`
**Source:** M. Rubinstein, P. Sarnak, *Experimental Mathematics* 3(3) (1994) 173–197.
Primary PDF from Project Euclid: https://projecteuclid.org/download/pdf_1/euclid.em/1048515870
(There is also a garbage scanned copy `rubinstein-sarnak-1994-chebyshev-bias.full.md` — do not read; superseded by the Project Euclid copy.)
**Secondary transcript (mod-4 race, clean):** `research/summaries/rubinstein-sarnak-mod4-race-ubc-notes.md`.

## What it establishes

The canonical treatment of **Chebyshev's bias** — the observed predominance of
primes congruent to 3 mod 4 over 1 mod 4. This is the named analytic-number-
theory machinery the adopted Route B approach
(`research/approaches/chebyshev-bias-granville-nu2-supply.md`) needs for the
fluctuation side of the ν₂ supply statistic.

**Precise statements (all under hypotheses):**

- **Limiting distribution (Theorem 1.1, GRH).** With
  `E_{q;a1..ar}(x) = (log x)/√x · (φ(q)π(x;q,aj) − π(x))`, under the Generalized
  Riemann Hypothesis the vector-valued function has a limiting distribution
  μ_{q;a1..ar} on R^r.
- **Explicit Fourier transform (under GRH + GSH, eq. 1.2):**
  `^μ(ξ) = exp(i Σ_j c(q,aj) ξ_j) · Π_{χ≠0} Π_{γ>0} J0( 2|Σ_j χ(aj)ξ_j| / √(1/4+γ²) )`,
  with `c(q,a) = −1 + Σ_{b≡a} b/q` the bias-shifting constant and `J0` the Bessel
  function. The **exponential factor exp(i Σ c(q,aj)ξ_j) is the source of the
  Chebyshev bias** — it shifts the mean, breaking the symmetry that would give
  equal 1/r! densities.
- **The mod-4 value.** For q=4, residues 3 vs 1:
  `δ(P_{4;3,1}) = 0.9959...` and for q=3, `δ(P_{3;2,1}) = 0.9990...` — the
  logarithmic density of the set where primes ≡3 mod 4 lead primes ≡1 mod 4 is
  0.9959 (Section 4 numerical computations, 4-digit accuracy, error < 2.5e-6).
  This is a strong *bias toward 3 mod 4*, but it is **conditional** (GRH + GSH).
- **Oscillation (Littlewood-type).** Even under GRH+GSH there are infinitely
  many x with P4;1,3 *and* infinitely many with P4;3,1 — the bias oscillates,
  so **no one-sided unconditional statement holds**. The numerical value 0.9959
  is a logarithmic *density/probability*, not a permanent inequality.
- **Bias dissolves as q→∞ (Theorem 1.5/1.6):** `max_a |δ(P_{q;a1..ar}) − 1/r!| → 0`
  as q→∞, and a central limit theorem holds.

## Bearing on this problem

The adopted Route B approach needs a **fluctuation bound**, not a one-sided bias
assertion, for the two-point mod-4 switch statistic
`bit_n = [p_{n+1} ≢ p_n (mod 4)]`. This paper delivers the correct lens: the
second-order term δ − 1/r! is governed by the exponential bias-shift factor and
**oscillates (Littlewood-type)**, so any honest supply-side statement must be a
fluctuation bound at the GRH/LI level, never an unconditional one-sided density
claim. Together with Lemke-Oliver–Soundararajan (2016, 2017) it fixes the
"two-point at Hardy–Littlewood level, fluctuation not bias" half of the approach.

**Not a proof of Gilbreath's conjecture.** It is a result about primes in
arithmetic progressions; it bears on the ν₂ supply statistic only through the
mod-4 residue distribution of consecutive primes.

## Verification

Statement checked against the clean Project Euclid full text
([[rubinstein-sarnak-1994-chebyshev-bias-full.full]]): Section 4 lists
δ(P4;N,R) = 0.9959..., the Abstract and intro state the bias + Littlewood
oscillation, and eq. 1.2/3.3 give the Fourier transform with the bias-shift
factor. Value confirmed by the UBC secondary note. Status: **sourced**
(primary text read; the 0.9959 figure is a computed numerical value quoted from
the source, not re-derived here).

```claim
id: rubinstein-sarnak-fluctuation-not-bias-verified
statement: Rubinstein–Sarnak 1994 (Exp. Math 3(3):173–197, primary text verified): under GRH the prime-race vector E_{q;a1..ar} has a limiting distribution (Thm 1.1); under GRH+GSH the explicit Fourier transform is exp(iΣ_j c(q,a_j)ξ_j)·Π_{χ≠χ0,γ>0}J0(2|Σ_j χ(a_j)ξ_j|/√(1/4+γ²)) (eq 1.2/3.3), with the exponential bias-shift factor — c(q,a)=−1+Σ_{b≡a mod q} b/q — the source of the Chebyshev bias. Numerically δ(P_{4;3,1})=0.9959, δ(P_{3;2,1})=0.9990 (logarithmic density, bias toward 3 mod 4). But Littlewood 1914: both P_{4;1,3} and P_{4;3,1} extend to infinity (sign oscillates; Leech 1957 first member of P_{4;1,3}=26861), so NO one-sided unconditional bias holds; bias dissolves as q→∞ (Thm 1.5) with CLT (Thm 1.6). Confirms the approach-file claim `rubinstein-sarnak-fluctuation-not-bias` from the primary text.
hypotheses: GRH + GSH for the explicit formula/value; primes, not a general 2-then-odds class
holds-here: yes (supplies the fluctuation-not-bias lens for the two-point mod-4 switch statistic bit_n=[p_{n+1}≢p_n mod 4] feeding Granville's ν₂; but the race bias is a one-point PNT-in-AP object, so it alone does not give the fixed-q=4 two-point switch count)
status: proved (conditional on GRH/GSH; verified verbatim in primary full text)
bearing: Route B supply side. The honest deliverable is a FLUCTUATION bound at GRH/LI + Hardy–Littlewood/Dedekind-sum level, never an unconditional one-sided density. Confirms ν₂ is two-point, NOT a one-point PNT-in-AP statistic; neither this nor LOS-2017 proves the open lower bound ν₂ ≥ n^{0.525+δ}.
anchor: research/sources/rubinstein-sarnak-1994-chebyshev-bias-full.full.md
answers: what-named-machinery-supplies-nu2
```
