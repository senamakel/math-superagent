# Lemke Oliver & Soundararajan 2016 — "Unexpected biases in the distribution of consecutive primes"

**Full text:** `research/sources/lemke-oliver-soundararajan-2016-unexpected-biases-consecutive-primes.full.md`
**Source:** R. J. Lemke Oliver, K. Soundararajan, *Proc. Natl. Acad. Sci. USA* 113(31) (2016) E4446–E4454, doi 10.1073/pnas.1605366113, arXiv:1603.03720 (PMC free full text).

## What it establishes

The primes are equidistributed among reduced residue classes mod q, but **pairs of consecutive primes (mod q) are not** — the incidence of the four (for q=3,4,6) or φ(q)² pattern-pairs is wildly non-uniform. This is the **two-point consecutive-prime residue statistic**, exactly the object the run's adopted `chebyshev-bias-granville-nu2-supply` approach identifies as the atomic input to Granville's ν₂ supply.

**Main Conjecture.** With π(x;q,a) = #{p_n ≤ x : p_{n+i-1} ≡ a_i (mod q), 1≤i≤r} for a pattern a = (a_1,…,a_r),

> π(x;q,a) = li(x)/φ(q)^r · ( 1 + c_1(q;a)·loglog x/log x + c_2(q;a)·1/log x + O((log x)^{-7/4}) )

where **c_1(q;a) = φ(q)/2 · ( (r−1)/φ(q) − #{1≤i<r : a_i ≡ a_{i+1} (mod q)} )** — the dominant bias term is governed by the *number of adjacent coordinates of a that repeat*. The c_2 term is given explicitly (eq. 2.23); for r=3+ it is a sum of pair terms.

**The two load-bearing consequences for this run:**

1. **The atomic bit is two-point, and its leading order is n/2.** For q=4, reduced residues are {1,3}, and the bit `[p_{n+1} ≢ p_n (mod 4)]` = `[gap ≡ 2 mod 4]` is the switch to a *distinct* pair (1,3) or (3,1). The equidistribution of single primes mod 4 over a full block × a secondary-bias term gives, to first order, ν₂ = #switches = n/2 (two of the four equiprobable pairs switch). Section 5 eq. [5.1] specialises the Main Conjecture to q=3,4:
   > π(x;q,a) = li(x)/4 · ( 1 ± (1/2log x)·log(2π log x / q) ) + O(x/(log x)^{11/4}),
   with the **minus sign for the repeating class a_1≡a_2 (mod q), plus for distinct** — i.e. the distinct (a,−a) pairs are *more* frequent than the repeating (a,a), so the switch count is even slightly pushed above n/2 at finite x.

2. **Conjecture 1.2 (robust bias).** For q=3 or 4 and a = ±1,
   > π(x;q,(a,−a)) > π(x;q,(a,a)) for all x ≥ 5, and
   > π(x;q,(a,−a)) − π(x;q,(a,a)) = x/(4(log x)²)·log(2π q log x) + O(x/(log x)^{11/4}).
   The "product of two consecutive primes prefers to be a quadratic nonresidue." This is the *sign* of the second-order bias — the honest quantity is a fluctuation bound, never a one-sided assertion (the bias oscillates, Littlewood-type; see Conjecture 1.5 symmetry π(x;q,a) = π(x;q,(−a_r,…,−a_1)) + O(x^{1/2+ε})).

## The connection to the ν₂ reduction (why the run holds this)

Granville's Lemma 5.4 feeds GC's supply side from ν₂ = #{c_s=2}, and the atomic bit that sets each c_s is the consecutive-prime mod-4 switch. Route B's whole remaining step is the *linear lower bound* ν₂ ≥ c·n. **This source supplies the two-point framework that makes ν₂ = n/2 the leading term** — so ν₂ ≥ c·n for any c<1/2 is the honest quantity the reduction consumes, and the factor-26 margin over n^0.525 (measured ν₂/n ≈ 0.49–0.52 at n=3999) is the right scale. The *bias* (second-order, ~x/(log x)²) is what wins the ordering at finite x and is bounded by this source, not asserted as unconditional. **Status: this is a sourced conjecture (Hardy–Littlewood / prime k-tuple level), not a theorem** — the leading term n/2 itself rests on the two-point k-tuple prediction (PNT-in-AP supplies only the one-point r=1 case; the run's `g-supply-two-point-crux-settled` note corrects the earlier "leading term unconditional" phrasing), and the bias is conjectural. So `ν₂ = n/2 + O(bias)` is k-tuple-conditional throughout.

## What it does NOT do

- It is not a proof of the mod-4 pair equidistribution (that is conjectural); it explains *why* the data deviate, at Hardy–Littlewood level.
- It says nothing about the iterated-difference operator itself — it only characterises the residue-pair input that feeds ν₂.
- It is PRIME-SPECIFIC (two-point); it cannot support a general 2-then-odds class theorem (Eppstein 2011 defeats any bounded-gap class; Colonna's delete-5 gives a concrete g=4 left-edge failure).

**Claim:** `los-2016-consecutive-pair-mod4-bias` — the consecutive-prime residue-pair distribution is biased with leading term n/2 and a second-order bias toward distinct pairs (Conjectures 1.1, 1.2, Main Conjecture); the switch count #{p_{n+1}≢p_n (mod 4)} = #{gap ≡ 2 mod 4} = ν₂ is a two-point statistic with value n/2 to first order.
**Bearing:** feeds the adopted `chebyshev-bias-granville-nu2-supply` approach — supplies the two-point characterisation that makes ν₂ ≈ n/2, leaving the honest deliverable as a fluctuation bound / Hardy–Littlewood-conditional linear bound.

```claim
id: los-2016-consecutive-pair-mod4-bias
statement: (Lemke Oliver & Soundararajan 2016, PNAS 113:31 E4446–E4454) The consecutive-prime residue-pair distribution mod q is biased. Main Conjecture: pi(x;q,a) = li(x)/phi(q)^r (1 + c1(q;a)·loglog x/log x + c2(q;a)/log x + O((log x)^{-7/4})), with c1(q;a) = phi(q)/2 ((r-1)/phi(q) - #{1<=i<r : a_i == a_{i+1} mod q}). At q=4 (eq 5.1) each of the four residue pairs is li(x)/4 (1 ± (1/2log x)·log(2pi log x/q)), MINUS for repeating (a,a), PLUS for distinct (a,-a). Hence the atomic bit feeding Granville's nu2, bit_n = [p_{n+1} not≡ p_n mod 4] = [gap_n ≡ 2 mod 4] = c_s = 2, is a TWO-POINT statistic equal to n/2 to first order, pushed slightly ABOVE n/2 at finite x by the bias. Conj 1.2: pi(x;q,(a,-a)) > pi(x;q,(a,a)) for q=3,4 and all x>=5. Conj 1.5 symmetry pi(x;q,a) = pi(x;q,(-a_r,...,-a_1)) + O(x^{1/2+eps}).
hypotheses: primes; consecutive-prime residue patterns mod q; the ENTIRE Main Conjecture (leading term included) rests on the prime k-tuple / Hardy-Littlewood conjecture. PNT-in-AP supplies ONLY the one-point r=1 case; the two-point r=2 leading term li(x)/phi(q)^2 is exactly the k-tuple prediction and is CONJECTURAL, not unconditional. CORRECTED 2026 (g-supply-two-point-crux-settled.md) — the earlier "main term unconditional from PNT-in-AP" phrasing was an overstatement.
holds-here: yes — the mod-4 consecutive-prime residue switch IS the nu2 supply input of the adopted chebyshev-bias-granville-nu2-supply approach.
status: asserted (sourced conjecture at prime k-tuple / Hardy-Littlewood level; the leading term n/2 is k-tuple-conditional, the bias is conjectural, neither is a theorem)
bearing: supplies the two-point mod-4 framework that makes nu2 = n/2 + O(bias) the leading term, so nu2 >= c·n for c < 1/2 is the right demand (factor ~26 margin over n^0.525); the honest deliverable is a fluctuation bound (bias oscillates Littlewood-type), never a one-sided bias assertion. PRIME-SPECIFIC two-point; cannot support a general 2-then-odds class theorem (Eppstein/Colonna defeats).
anchor: research/sources/lemke-oliver-soundararajan-2016-unexpected-biases-consecutive-primes.full.md
```
