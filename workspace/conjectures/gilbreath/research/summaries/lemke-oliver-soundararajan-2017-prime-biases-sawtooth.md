# Lemke Oliver & Soundararajan 2017 — "The distribution of consecutive prime biases and sums of sawtooth random variables"

**Full text:** `research/sources/lemke-oliver-soundararajan-2017-prime-biases-sawtooth.full.md`
**Source:** arXiv:1709.06168 [math.NT], 2017 (companion to their PNAS 2016 paper). Converted from the arXiv PDF.

## What it establishes

The rigorous back half of the Lemke-Oliver–Soundararajan programme on
**biases in patterns of consecutive primes (mod q)** — the exact object the
adopted Route B approach (`chebyshev-bias-granville-nu2-supply`) needs for the
**two-point** ν₂ supply statistic.

**Setup.** For q≥3 and a residue-pattern a=(a1..ar), define
`π(x; q, a) = #{p_n ≤ x : p_{n+i−1} ≡ a_i (mod q)}`. The 2016 PNAS paper
conjectured the pattern frequencies; here they study the **secondary
(fluctuation) term** that distinguishes patterns with equal dominant term.

**Main theorems (all about the *limiting distribution of the secondary term*, i.e. the fluctuation):**

- **Theorem 1.1.** As q→∞ the distribution of `C(k)` (the secondary term for the
  pair/correlation statistics) tends to a continuous probability distribution,
  **symmetric around 0**: there is a continuous Φ_C with Φ_C(−x)+Φ_C(x)=1 such that
  `(1/q) #{k (mod q) : C(k) ≤ (e^γ/2) x} = Φ_C(x) + o(1)` uniformly on x∈[−X,X].
  **Symmetric around 0 ⟹ the fluctuation is centred, oscillatory — no one-sided bias.**
- **Theorem 1.2.** The same for `π̂(t)` (residue-attainability statistic).
- **Theorem 1.3.** The same symmetric-limiting-distribution result for the
  remainder term R(x) in the asymptotics of the mean of Euler's φ-function:
  `(1/y) meas{u ≤ y : R̃(u) ≤ (3e^γ/π²)x} = Φ_R(x)+o(1)` with Φ_R(−x)+Φ_R(x)=1.
- **Connection.** The secondary bias term is tied to the **Fourier transform of
  classical Dedekind sums** and to the **error term in Σ_{n≤x} φ(n)**.

## Bearing on this problem

Three load-bearing facts for Route B's supply-side ν₂ statistic
(`bit_n = [p_{n+1} ≢ p_n (mod 4)]` is a **two-point** consecutive-prime
mod-4 switch):

1. **The fluctuation is symmetric about 0** (Theorems 1.1–1.3): the honest
   statement about consecutive-prime pattern biases is a **fluctuation bound**,
   never a one-sided unconditional density. This directly instantiates the
   Chebyshev-bias/Littlewood caution the approach file flags.
2. The relevant scale is **Hardy–Littlewood / Lemke-Oliver–Soundararajan level**
   (secondary terms governed by Dedekind sums), confirming the approach's
   conclusion that ν₂ is **two-point, not one-point** — PNT-in-AP / GRH for
   Dirichlet L-functions does not by itself deliver ν₂ > n^β.
3. It gives the named mathematics (symmetric limiting distribution of the
   secondary term = the fluctuation law) that a conditional supply-side theorem
   of the form "IF ν₂ ≥ n^{0.525+δ} (which is about consecutive-prime mod-4
   switches) THEN GC via Lemma 5.4" would invoke.

**Not a proof of Gilbreath, and not a proof of the ν₂ lower bound itself** — it
establishes the *distributional law* of the fluctuation, not a lower bound for
consecutive-prime mod-4 switches. The ν₂ ≥ n^{0.525+δ} statement remains open.

**Caveat on bearing (a subtlety the abstract omits).** Theorems 1.1–1.3 are
**q → ∞** statements: they describe the limiting distribution of the secondary
term over all large (prime) moduli q and, inside each, over the residue index k
(mod q). The ν₂ supply statistic for Route B is a **fixed q = 4** statement —
the count of consecutive-prime pairs whose gap is ≡ 2 (mod 4) among the first n
pairs. So LOS-2017 is an *indirect analog* (same fluctuation-cannot-be-one-sided
lesson), not the sharp q=4 result. It rules out deriving ν₂ > n^β from any
one-sided bias assertion; it does not by itself deliver the fixed-q=4 switch
count. What would (were a fixed-q statement wanted) is a direct correlation
bound on gap ≡ 2 (mod 4) at Hardy–Littlewood level.

## Verification

Theorems 1.1–1.3 (statement of each, the C(k) = −C(−k) oddness, the
symmetric-about-0 Φ_C, Φ_s, Φ_R, the Dedekind-sum Fourier connection and the
φ-mean error-term link) verified verbatim in the converted full text
[[lemke-oliver-soundararajan-2017-prime-biases-sawtooth.full]]. Status:
**sourced**; not re-derived here.

```claim
id: los2017-secondary-term-symmetric
statement: Lemke Oliver & Soundararajan 2017 (arXiv:1709.06168): for the consecutive-prime mod-q pattern bias, the secondary coefficient C(k)=(1/φ(q))Σ_{χ≠χ0}χ(k)L(0,χ)L(1,χ)A_{q,χ} is odd (C(k)=−C(−k)) and, for q prime, its distribution over k mod q tends as q→∞ to a continuous distribution symmetric about 0: (1/q)#{k: C(k)≤(e^γ/2)x}=Φ_C(x)+o(1), Φ_C(−x)+Φ_C(x)=1 (Thm 1.1); the same holds for the Dedekind-sum Fourier transform πiŝ_q(t) (Thm 1.2) and the φ(n) mean-value remainder (Thm 1.3). So the secondary/fluctuation term of consecutive-prime pattern biases is centred and oscillatory, not one-sided.
hypotheses: q prime (for the theorem scope; the paper confines to prime q); the c2 coefficient recovers the pattern bias off-diagonal term; these are q→∞ large-modulus distributional statements.
holds-here: partially — the one-sided-bias-is-impossible lesson transfers to the fixed q=4 gap≡2(mod4) switch count feeding ν₂, but the theorems themselves are large-q and do not give the fixed-q=4 switch count.
status: proved (theorems proved in the paper, full text read)
bearing: Rule B supply side: supports the conclusion that the honest ν₂ deliverable is a fluctuation bound at GRH/LI + Hardy–Littlewood/Dedekind-sum level, never a one-sided unconditional density; does NOT prove ν₂ ≥ n^{0.525+δ}, which remains open.
anchor: research/sources/lemke-oliver-soundararajan-2017-prime-biases-sawtooth.full.md
answers: what-named-machinery-supplies-nu2
```
