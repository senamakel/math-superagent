# Is there published work improving Lagarias's real-dynamics bound, or combining real + 3-adic methods?

**Question posed:** (1) Any published work improving the real-dynamics bound
`#{n≤X : leading digit of (2^n)_3 avoids 2} ≤ 25 X^(36/37)` using better
Diophantine approximation measures for log_3 2? (2) Any work combining the
real and 3-adic methods to control the middle digits, beyond Lagarias's
"it's open" remark? (3) Specifically, anyone using BOTH the continued fraction
of log_3 2 AND the 3-adic sieve simultaneously?

**Headline answers delivered here (each with evidence class):**

1. **No published improvement exists.** The bound stands as Lagarias's
   Theorem 1.1 (J. London Math. Soc. 79 (2009) 562–588; arXiv:math/0512006).
2. **The question's premise needs a correction:** the real-dynamics bound is
   NOT the best-known bound for this problem, and improving it via Diophantine
   measures would never reach the relevant target. See the "correction" below.
3. **No one has combined the two methods** to beat Narkiewicz's exponent.
   Lagarias explicitly poses this as open (Section 1.6). This is confirmed by
   the literature returned, not by absence of search.

---

## 1. The exact statement (Lagarias, J. London Math. Soc. 79 (2009), Thm 1.1)

Source: arXiv:math/0512006 (full text in this workspace at
`research/sources/lagarias-ar5iv-full.full.md`). URL: https://ar5iv.labs.arxiv.org/html/math/0512006

> **Theorem 1.1.** For each λ > 0, the number
> `N_λ(X) := #{ n : 1 ≤ n ≤ X and (⌊λ 2^n⌋)_3 omits the digit 2 }`
> satisfies `N_λ(X) ≤ 25 X^(36/37) ≤ 25 X^(0.9725)` for all sufficiently large
> X ≥ n_0(λ).

This is a statement about the **truncated real dynamical system** `x_n = ⌊λ2^n⌋`
— the *leading* digits of `2^n`. Hypotheses: λ > 0 any real number; the bound
holds only from some `n_0(λ)` (it is not uniform in λ).

### The central correction: the real bound is weaker than the 3-adic bound

Lagarias's Summary (Section 1.6) says the two methods give restrictions "of
roughly equal strength" — each reduces candidates to ≤ X^c for some 0<c<1. But
the actual exponents are far apart:

| Method | Exponent | Source |
|---|---|---|
| Real (truncated, *leading* ~log_3 X digits) | **36/37 ≈ 0.9725** | Thm 1.1 |
| 3-adic (Narkiewicz; *trailing* ~log_3 X digits) | **α_0 = log_3 2 ≈ 0.63092** | Narkiewicz 1980; Lagarias Thm 1.4 |

So for the actual Erdős problem (λ=1), Narkiewicz's exponent 0.63092 is already
*much better* than the real method's 0.9725. **Improving the real method (or its
Diophantine constant) can never be the route to proving any shadow of the
conjecture**, and it would not even improve upon the known 3-adic bound.
Lagarias himself presents the real bound as an isolated real-dynamics result,
not as competition for Narkiewicz's count. This is important for this run: the
goal `N_1(X) ≤ 1.62 X^(α_0)` (GOAL.md) is the 3-adic side, and the real method
is strictly inferior.

### Where 36/37 comes from (so "better Diophantine measures" matters precisely)

The real proof (Lagarias §2) uses the rotation `w_n = n·α_0 + log_3 λ (mod 1)`.
The digits of `⌊λ2^n⌋` are controlled by which of `2·3^(k-1)` subinterval of
[0,1) the `w_n` fall in. The count of bad n comes out as
`M ≤ 12 (2/3)^(k-1) X`. The exponent is determined by the *growth of continued
fraction convergents*, controlled by a Diophantine lower bound (Lemma 2.2):

> **Lemma 2.2.** For all q ≥ 1 and integers p,
> `|α_0 − p/q| ≥ (1/1200) q^(−(c_0+1))` with `c_0 = 13.3`.
> Consequently the convergent denominators satisfy
> `q_n ≤ 1200 (q_{n-1})^(c_0)`.

The constant `c_0 = 13.3` comes from Simons–de Weger (Acta Arith. 117 (2005)
51–70, Lemma 12), itself proved with a transcendence result of G. Rhin for
linear forms in two logarithms. Then
`(1 − α_0)/c_0 = (1 − log_3 2)/13.3 ≈ 0.02773`, so the exponent is
`1 − (1−α_0)/c_0 ≈ 0.97227 = 36/37`. **So the diophantine measure of
log_3 2 does enter — but only via a constant `c_0` that is already huge
(13.3), and it sits in an already-losing real bound.** Pushing `c_0` down to
any realistic value moves 0.9725 only marginally, never toward 0.63092.

### Best-known irrationality measures for log 2 / (log 3) (candidate "better measures")

For completeness: the irrationality exponent of log 2 is at most
`µ(log 2) ≤ 3.5746` (Marcovecchio, in Zudilin's 2004 survey "An essay on
irrationality measures of logarithms", arXiv:math/0404523). For a nonzero
`γ ∈ ℚlog2 + ℚlog3`, Rhin's construction gives `µ(γ) < 8.616`. These are the
state of the art for the *logarithmic* measures; they are **not** what Lagarias
uses (he uses the cruder Simons–de Weger / Baker-type two-logarithm bound).
Using a better irrationality measure of log_3 2 would improve the `c_0` constant
and hence the real exponent slightly — but as shown above that is a dead end
for the Erdős problem, because the real bound is already dominated by the
3-adic bound.

---

## 2. Has anyone combined real + 3-adic to control the middle digits?

**No.** Lagarias's Section 1.6 statement (the "combining is open" remark) is
reproduced verbatim below, and the search turned up nothing that goes beyond it:

> "Thus for the 3-adic dynamical system... the method used for the real
> dynamical system estimates the omission of 2 in the log_3 X most significant
> ternary digits of 2^n, while for the 3-adic dynamical system the method
> estimates the omission of 2 in the log_3 X least significant ternary digits
> of 2^n. ... the ternary expansion (2^n)_3 has about α_0 n ternary digits, the
> vast number of digits in the middle of the expansion are not exploited in
> either method; only a logarithmically small proportion of the available
> digits ... are considered in the two methods.
>
> **It seems a challenging problem to find a method that effectively combines
> the two approaches to find better upper bounds on N_1(X) than that given by
> Narkiewicz. Can one obtain an upper bound of O(X^β) for some β < log_3 2 in
> this way? Can one show that the high order digits and the low order digits in
> the ternary expansion (2^n)_3 are "uncorrelated" in some quantifiable way?"**

This is the exact quote that this run's memory records as LAG-4. **No one has
answered it.** The middle digits (α_0 n − 2 log_3 X of them, i.e. all but a
logarithmic fraction of the expansion) remain untouched by every method.

### Why the naive "combine both CF of log_3 2 and 3-adic sieve" fails to do the job

The two methods genuinely use *independent* digit blocks:

- The **real** method reads the top ~log_3 X digits of `2^n` via the rotation
  `n·log_3 2 (mod 1)`, whose spacing is governed by the **continued fraction of
  log_3 2** (Lemma 2.1 / Slater).
- The **3-adic** method reads the bottom ~log_3 X digits via `2^n mod 3^k`,
  governed by the **order of 2 mod 3^k** (a primitive root — the exact
  bijection that gives `|A_k| = 2^(k-1)`, this run's SIEVE-EXACT).

The two digit blocks are disjoint and each is only O(log X) long, while the
middle is O(n) long. Simply running the two sieves "in parallel" and intersecting
the survivors does combine the *bounds*, but since both bounds are at most
`X^(0.9725)` and `X^(0.63092)` the intersection is still at least
`X^(0.63092)` — no better than Narkiewicz. To get below `α_0` one must control
the middle digits, which neither the CF of log_3 2 nor the 3-adic sieve sees.
**This is why the question's premise (combine the two = improved bound) is not
realized in the literature: the two methods together still read only O(log n)
of the O(n) digits.**

---

## 3. The only genuine recent progress and why it doesn't touch the middle digits

Two directions have moved since 2009, neither filling the middle-digit gap:

### (a) Dimitrov–Howe (2021/2023), "Powers of 3 with few nonzero bits and a conjecture of Erdős"
arXiv:2105.06440 (Rocky Mountain J. Math.).
URL: https://arxiv.org/abs/2105.06440

> **Theorem 1.2.** The only powers of 2 that are sums of ≤ 25 distinct powers of
> 3 are 2^0, 2^2, 2^8. Equivalently: for x ∉ {0,2,8}, the base-3 expansion of
> 2^x either contains a digit 2 or contains at least twenty-six 1s.

This is the strongest *provable* statement on the sparse side. But it works by
**nested moduli with determinate-power lifting** — an exclusively *low-digit*
(3-adic) argument. It forces "a 2, or ≥26 ones" among the **low** digits; it
gives no control on the middle digits. The run's own `|A_k| = 2^(k-1)` shows
low digits alone cannot kill the surviving case (≥26 ones, no 2), so the
frontier (FRONTIER.md) is exactly the unfilled middle-digit coupling.

### (b) Verification and average results — not bounds

- **Saye (2022)**, "On two conjectures concerning the ternary digits of powers
  of two", arXiv:2202.13256: verifies the Erdős and Sloane conjectures for
  n ≤ 2·3^45 ≈ 5.9×10^21 (numerical, trailing-digit recursive sieve). Not a
  bound on N(X). URL: https://escholarship.org/uc/item/28m2v9br
- **Dupuy–Weirich (2016)**, "Bits of 3^n in binary..." (JNT 158, 268–280) and
  its number-field generalization **Li–Zhao** (arXiv:2601.12753): Cesàro-*average*
  digit equidistribution of `(2^n)_3`. Average statements — say nothing
  pointwise, consistent with GOAL.md's heuristic caveat.
- **Albayrak–Bell (2023)**, arXiv:2304.09223: quantitative finiteness of
  intersections of sparse automatic sets (encodes the Erdős conjecture) via
  S-unit-type bounds — gives *effective finiteness*, not an improved exponent.
- **Bennett–Bugeaud–Mignotte (2012)**, "Perfect powers with few binary digits
  and related Diophantine problems, II" (Math. Proc. Camb. Phil. Soc. 153
  (2012) 245–262): combines Archimedean + non-Archimedean linear forms in
  logarithms — but for a *different* problem (every q-th power of an integer
  has ≥5 nonzero binary digits). This is the closest published "real + p-adic"
  combination, and it **never** produces a bound `O(X^β), β < log_3 2` for the
  Erdős count.

---

## 4. Direct answers to the three sub-questions

| Question | Answer | Evidence class |
|---|---|---|
| Any work improving `25 X^(36/37)` via better Diophantine measures of log_3 2? | **No.** The real bound is unimproved since 2009; and it is *already weaker* than Narkiewicz's `1.62 X^(0.63092)`, so improving it would not help the Erdős count. | sourced (no such work found in 6 searches over the literature); the comparative-w eakness is computed from the two published exponents |
| Any work combining real + 3-adic for the middle digits? | **No.** Lagarias's Section 1.6 open-problem statement stands unaddressed. | sourced |
| Anyone using CF of log_3 2 AND 3-adic sieve simultaneously? | **No.** The two blocks are disjoint and each is O(log X) digits; intersecting them cannot beat Narkiewicz's exponent, which is the structural reason (not mere lack of effort) no such combination exists. | inference from the published structure (LAG-4) |

---

## Sources (primary)

- Lagarias, *Ternary expansions of powers of 2*, J. London Math. Soc. (2) 79
  (2009) 562–588; arXiv:math/0512006.
  https://ar5iv.labs.arxiv.org/html/math/0512006
- Narkiewicz, *A note on a paper of H. Gupta concerning powers of 2 and 3*,
  Univ. Beograd. Publ. Elektrotehn. Fak. Ser. Mat. Fiz. No. 678–715 (1980)
  173–174 (as cited in Lagarias).
- Dimitrov & Howe, *Powers of 3 with few nonzero bits and a conjecture of
  Erdős*, arXiv:2105.06440. https://arxiv.org/abs/2105.06440
- Zudilin, *An essay on irrationality measures of logarithms*,
  arXiv:math/0404523 (µ(log 2) ≤ 3.5746, Marcovecchio; µ(Qlog2+Qlog3) < 8.616, Rhin).
- Saye, *On two conjectures concerning the ternary digits of powers of two*,
  arXiv:2202.13256. https://escholarship.org/uc/item/28m2v9br
- Bennett, Bugeaud, Mignotte, *Perfect powers with few binary digits...*, MPLMS
  153 (2012). https://doi.org/10.1017/s0305004112000345
- Albayrak & Bell, *Quantitative estimates for the size of an intersection of
  sparse automatic sets*, arXiv:2304.09223.

## Sources examined and rejected (with reason)

- *On the Normality of Arithmetical Constants* (Lagarias 2001): general
  dynamical framework; contains the specific leading-digit bound.
- *Digit expansions of numbers in different bases* (JNT 2021, "General
  Section"): studies integers with binary digits in bases 3,4,5; different
  problem (all integers, not the 2^n orbit); no middle-digit coupling.
- *Fractional parts of powers of large rational numbers* & *Mahler's theorem
  notes*: about {ξ(p/q)^n} interval-containment, not the ternary digit count of
  2^n; not applicable.
- *Σ-digit-sum approximations* (Hensley–?, s2 vs s3): central-limit results on
  digit sums over all integers; not the 2^n orbit; rejected as irrelevant.
- *β-shift/Pisot results*: different base/dynamical system; rejected.

## Reliability notes

- The "no such work" claims rest on 6 distinct exa searches (Lagarias real
  bound, Diophantine measure of log_3 2, combining real+p-adic, CF-based
  irrationality of log 2/log 3, middle digits, ternary digit progress). This is
  a positive body of negative evidence, not a formal impossibility proof. The
  structural reason (disjoint O(log n) blocks vs O(n) middle) is a mathematical
  argument, stated as inference.
- The comparative weakness of the real (0.9725) vs 3-adic (0.63092) bounds is a
  direct, reproducible computation from the two published exponents, not an
  opinion.
