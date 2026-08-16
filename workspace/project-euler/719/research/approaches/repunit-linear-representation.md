# Repunit-weighted Diophantine representation of the witness

## The idea in one line

Eliminate the concatenation variable and write the S-condition as a single
repunit-weighted representation problem: enumerate the *witnessing split*
(b₁,…,b_k) directly, and recover the root m by solving a quadratic.

## Mathematics

Let m² have D digits, and let a witness split m² = b₁|b₂|…|b_k place block bᵢ
starting at decimal position Lᵢ (counting from the right, so L₁ > L₂ > … > L_k = 0).
Concatenation gives

  m² = Σᵢ bᵢ · 10^{Lᵢ},

and the S-condition is Σᵢ bᵢ = m. Subtract the second from the first:

  m² − m = Σᵢ bᵢ (10^{Lᵢ} − 1) = 9 · Σᵢ bᵢ R_{Lᵢ},

where R_L = (10^L − 1)/9 is the **repunit** 111…1 (L ones). Equivalently

  m(m−1)/9 = Σᵢ bᵢ R_{Lᵢ},   with 0 ≤ bᵢ ≤ 10^{lᵢ}−1,  lᵢ = block length of bᵢ.

This is the full statement of the Butler–Graham–Stong "partition and sum"
structure (arXiv:1501.04067) — the mod-9 invariant m ≡ m² (mod 9) is only its
mod-9 shadow. The two-block case collapses the sum to one term and recovers the
classical Kaprekar/torn-number congruence 10^l − 1 | m(m−1) (Iannucci,
Dudeney). For k ≥ 2 blocks the witness becomes a representation of the
triangular-type integer m(m−1)/9 as a repunit-weighted sum with digit-length
bounds on the coefficients.

## Why it is a different line of attack

The adopted method keeps m as the free variable and *tests* whether a split
exists (digit-partition recursion over m = 2..10⁶). This proposal flips the
object: make the split (bᵢ, Lᵢ) the free variable and recover m. The two-block
analogue shows the power of the flip — the split-parametrisation turns a scan
into a divisor enumeration (unitary divisors of 10^n − 1). If the k-block
equation has an analogous parametrisation (or a small generating set of
"primitive" repunit representations), the witness space may be far smaller than
the root space, and T(N) becomes a sum over witnesses instead of a scan over
roots. This is a number-theory reformulation, not a search over candidate
answers: its cost would grow with the number of witnesses, not with isqrt(N).

## What is speculation vs established

- Established: the identity m² − m = Σ bᵢ(10^{Lᵢ}−1) and the two-block limit
  (Iannucci unitary-divisor parametrisation) — claims `iannucci-kaprekar-divisor-formula`,
  `dudeney-torn-number-two-block`, `partition-sum-invariant-mod9` in this run's library.
- Speculation: that the k-block repunit equation admits a compact
  parametrisation or primitive-generator structure comparable to the two-block
  divisor correspondence. No such result is in the library yet (the recorded
  literature gap says the general multi-block class has no published treatment,
  so this is a fresh question to put to research).

## Cost

If a witness-level parametrisation exists, the cost scales with the number of
witnesses (for N = 10¹² that is ≤ 408 roots × their few witnesses, essentially
constant), not with isqrt(N) = 10⁶. If it does not exist, this approach closes
with a recorded reason, which is itself a result.

## Research verdict (researcher, sourced)

The repunit identity m(m−1)/9 = Σ bᵢ R_{Lᵢ} (Lᵢ = number of digits strictly to the
right of block bᵢ) is **correct and already partly in this library**: it is the
full Butler–Graham–Stong partition-and-sum structure, and the two-block limit
is exactly the Kaprekar/torn-number congruence `(10^L − 1) | m(m−1)` with the
Iannucci unitary-divisor parametrisation of `10^n − 1`. That part is grounded.

The **open claim is the payoff**: whether the k-block (k ≥ 3) equation has a
compact parametrisation or primitive generating set that turns the scan into a
witness enumeration. I searched several phrasings (generalised Kaprekar numbers,
split-and-sum to square root, multi-block, repunit representation of
triangular-type integers m(m−1)/9) and found **no published treatment** of the
k ≥ 3 block case and no counterexample either — the recorded literature gap for
the multi-block S-number class holds. So the mechanism is established, the win is
unproven in both directions. Not refuted. Worth pursuing only as a fresh
research question, not as a settled method. The one near-hit — Pandichelvi &
Umamaheswari, "Exposure Of Positive Integer Solutions to an Equation Comprising
Kaprekar Numbers" (IJARSET 2024, https://doi.org/10.22214/ijraset.2024.63251) —
invents solution families for x₁+…+x_m = k for *constituent Kaprekar numbers* and
does not give an enumeration or a closed form; it confirms no structural
parametrisation is available for the general class.

```claim
id: repunit-witness-identity
statement: Let m² have D decimal digits and let m² = b₁|b₂|…|b_k be a split into k ≥ 2 contiguous blocks, where block bᵢ has lᵢ ≥ 1 digits and its least significant digit sits at decimal position Lᵢ (so L₁ > … > L_k = 0, and D−1 = L₁). If the blocks sum to m (the S-condition), then concatenation and block-sum give m² − m = Σᵢ bᵢ(10^{Lᵢ} − 1) = 9 Σᵢ bᵢ R_{Lᵢ}, i.e. m(m−1)/9 = Σᵢ bᵢ R_{Lᵢ} with R_L = (10^L−1)/9 the repunit and 0 ≤ bᵢ ≤ 10^{lᵢ}−1. For k = 2 this collapses to (10^{L₁}−1) | m(m−1), the Kaprekar/torn-number congruence.
hypotheses: base 10, contiguous blocks read left to right; Lᵢ measured from the right with L_k = 0.
holds-here: yes
status: checked (verified by hand on the statement's witnesses 82²=6724, 91²=8281, 99²=9801; two-block limit matches claims `iannucci-kaprekar-divisor-formula`, `dudeney-torn-number-two-block`)
bearing: The mod-9 invariant `partition-sum-invariant-mod9` is exactly the mod-9 shadow of this identity (9 | m(m−1)). It fully characterises the two-block case and is the natural frame in which to ask whether the k-block case admits a parametrisation — which the literature has not answered.
anchor: research/approaches/repunit-linear-representation.md
```

```approach
idea: Invert the witness: m(m−1)/9 = Σ bᵢ R_{Lᵢ} (repunit-weighted block sum), enumerate the split (bᵢ, Lᵢ) as the free object and recover the root m by solving a quadratic — the k-block generalisation of the two-block Kaprekar congruence 10^l−1 | m(m−1).
mechanism: Butler–Graham–Stong partition-and-sum structure (arXiv:1501.04067); repunits R_L; the two-block limit is the Iannucci unitary-divisor parametrisation of 10^n−1. Flipping the free variable from root to witness is exactly what made the two-block case a divisor enumeration instead of a scan.
status: adopted (mechanism established; sharpened into the cyclotomic-basis synthesis — see first-step)
precedent: |
  - Identity verified by hand (exact arithmetic) on the statement's witnesses:
    82²=6724=6|72|4 → m(m−1)/9 = 738 = 6·R₃ + 72·R₁ + 0·R₀; also on 91²=8281 and 99²=9801.
  - Two-block collapse → (10^L−1) | m(m−1), the classical Kaprekar/torn-number congruence:
    claim ids `iannucci-kaprekar-divisor-formula`, `dudeney-torn-number-two-block`,
    `kaprekar-two-block-subcase` in this library.
  - Mod-9 shadow: claim `partition-sum-invariant-mod9`, sourced to Butler, Graham, Stong,
    "Partition and sum is fast", arXiv:1501.04067 (https://arxiv.org/html/1501.04067v1).
  - No k-block (k≥3) analogue of the unitary-divisor parametrisation found in the
    literature: searches for "generalised Kaprekar number 3+ parts wanting square root
    digital sum" return only the two-block theory, the Kaprekar *constant/transformation*
    dynamics (a different object — rearrange-and-subtract, not split-and-sum), and
    divisor-partition numbers (Zumkeller/k-layered, not digit partitions). The general
    multi-block class exists only as OEIS A104113/A038206 (Branicky's digit-partition
    recursion). No source parametrises it, and no source proves it cannot be parametrised.
first-step: (adopted synthesis) Expand each term in the cyclotomic basis — 10^{Lᵢ}−1 = Σ_{d | Lᵢ} Φ_d(10) — so the witness equation becomes m(m−1) = Σ_d c_d Φ_d(10) with c_d = Σ_{i : d | Lᵢ} bᵢ. For k=2 this collapses to c_d = b₁ for every d | L, so m(m−1) = b₁(10^L−1), recovering Iannucci's unitary-divisor correspondence exactly; for k ≥ 3 the coefficient vector (c_d) is the genuinely new free object. Tool_builder's first concrete move: for each length composition with k ≥ 3, enumerate the reachable coefficient vectors (c_d) subject to 0 ≤ bᵢ ≤ 10^{lᵢ}−1 and concatenation consistency bᵢ = ⌊m²/10^{Lᵢ}⌋ mod 10^{lᵢ}; use the cyclotomic gcd structure gcd(Φ_a(10), Φ_b(10)) as the divisibility lever on m(m−1); and measure the witness-space size against the 406 known roots ≤ 10⁶ (b-file oracle). If the witness space is ≪ 10⁶, T(N) becomes a sum over witnesses; if not, close with the measured ratio recorded.
killed-by:
```
