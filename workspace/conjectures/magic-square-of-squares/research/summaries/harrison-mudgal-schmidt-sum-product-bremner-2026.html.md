# Harrison, Mudgal & Schmidt, "Uniform sum-product phenomenon for algebraic groups and Bremner's conjecture", arXiv:2603.06483v1 (2026)

[[harrison-mudgal-schmidt-sum-product-bremner-2026.html.full]]
Full text: `research/sources/harrison-mudgal-schmidt-sum-product-bremner-2026.html.full.md` (32 pp, HTML conversion).
Authors: Joseph Harrison, Akshat Mudgal, Harry Schmidt (Warwick). v1, 6 Mar 2026.
Companion PDF-conversion summary: `research/summaries/harrison-mudgal-schmidt-sum-product-bremner-2026.md` (superseded digest).

## Theorem 1.1 — exact statement (verbatim content)

"There is an **effectively computable** constant C ≥ 1 with the following property. Let E be an elliptic curve in Weierstrass form y² = x³ + ax + b, a, b ∈ Q, and let r be the rank of E(Q). Let X = {x(P) : P ∈ E(Q)} and Y = {y(P) : P ∈ E(Q)}. Let A be either an arithmetic progression, a geometric progression or a set of the form {u², (u+d)², (u+2d)², …, (u+dl)²}, with u, d ∈ Q and l ∈ N. If A ⊆ X or A ⊆ Y, then |A| ≤ C^(1+r)."

Hypotheses: curve over **Q** in short Weierstrass form; r = rank E(Q); pattern entirely inside one coordinate set; C ≥ 1. The paper notes explicitly: "the constant C in Theorem 1.1 does not depend on a, b" — **C is absolute**, uniform over all E/Q (only r enters, in the exponent).

**(a) What C is a function of.** Per the statement: of nothing — an absolute effective constant. Per the proof chain (Theorem 1.1 ⇐ Corollary 2.2 in §7 ⇐ Theorem 2.1 ⇐ Theorem 4.2 + Prop 5.1 ⇐ Theorem 3.7 + Lemmas 4.1/4.4): a worked-out value would be a function of (i) the **David–Philippon uniform-Mordell–Lang constant** C(d, g) from [11, Théorème 1.13] (Theorem 3.7's first part "follows directly" from it — this is the input for the elliptic-curve case; d = degree of the subvariety in E^g), specialised to the correspondence 𝒞 = {(P, x(P))} ⊆ E × 𝔾_a (Example 3.5; 𝒞 is not a translate of a subgroup, else E would be isogenous to 𝔾_a, so Corollary 2.2's hypotheses hold); (ii) degree- and subgroup-count bounds from Bombieri–Zannier [2, Lemma 2] and the sub-Pfaffian complexity bound of Jones–Schmidt [27] ("an absolute (effectively computable) constant", used in Lemma 4.1); (iii) for the 𝔾_m half of Theorem 3.7 only: Laurent [29] + the Evertse–Schlickewei–Schmidt S-unit bound [18]. **No exact expression for C is stated anywhere in the paper.** The weak-PFR constants of Gowers–Green–Manners–Tao (Lemma 6.3: d ≤ C log(4K), |A′| ≥ |A|/K^(C′), C = 140, C′ = 110; propagated by Lemmas 6.2, 6.6) feed the sum-product theorems 1.3, 2.3, 1.8, 2.6 — **not** the §7 proof of Corollary 2.2/Theorem 1.1, which invokes only Theorem 2.1. The introduction sketches an alternative route through (1.9) and Proposition 5.1, but the formal §7 proof is PFR-free. (Correction to the prior summary: "C built from David–Philippon + PFR constants" is inaccurate for Theorem 1.1.)

**(b) Is any explicit value/formula given?** **No.** The paper's only explicit constants are in the PFR/structural lemmas (140, 110, 400, 100 in Lemmas 6.2–6.6) and cited external results (Cushman's 4/3+10/4407, CPS's 1/21). Theorem 1.1's C is asserted "effectively computable" and never exhibited, bounded, or sized — not even as a function of the ingredients. An explicit C would require re-deriving David–Philippon's Théorème 1.13 constant specialised to this correspondence, which the paper does not do.

**(c) Which ingredient dominates.** Structurally the David–Philippon uniform-ML constant for subvarieties of E^g is the dominant input (it is the only Diophantine-geometry input in the elliptic-curve case); the paper does not quantify any of the sizes. S-unit bounds concern the 𝔾_m case only. Nothing in the paper gives even an order of magnitude for C.

## Why it matters for the MSS run

- The MSS gives three points Pᵢ = 2Qᵢ ∈ E(Q) with x(Pᵢ) = a−b, a, a+b in AP (Robertson reduction, claim `robertson-elliptic-reduction`), so A = {a−b, a, a+b} ⊆ X — Theorem 1.1's **first** pattern class, length 3 ≤ C^(1+r). Note the centre line's entries r², e², s² (all squares in AP) are an AP of *values*; their square roots are never in AP jointly with r²+s²=2e², so the "consecutive squares" class does *not* apply. The doubled-point applicability is settled (claim `patterns-bremner-2026-no-mismatch-for-2E-Q`).
- The prior open question — could C^(1+r) < 3 ever be verified? — is **answered negatively by this paper as it stands**: no value, no formula, and the machinery (DP uniform ML) yields constants vastly larger than 3. The run's blocker is unchanged operationally: C is in-principle computable but uncomputed. Corollary 2.2 additionally bounds proper generalised APs of *any* rank k by D(d)^(1+r), which the thread notes covers the four-centre-AP configuration {u, v, u+v, u−v}.
- Theorem A.1 (Appendix A): for the AP/GP surfaces S_A, S_B attached to E^t × P, an effectively computable t exists with S_A(K) = S_B(K) = D(K) — a Zariski-closure consequence, not usable numerically.

```claim
id: hms-2026-bremner-effective-constant
statement: There is an effectively computable constant C >= 1, independent of the curve
  coefficients a, b (absolute over all E/Q), such that for any E/Q in Weierstrass form
  y^2 = x^3 + ax + b of rank r, any arithmetic progression, geometric progression, or set
  of consecutive squares contained in {x(P): P in E(Q)} or {y(P): P in E(Q)} has length
  <= C^(1+r). (Theorem 1.1.)
hypotheses: E/Q rank r; A an AP/GP/consecutive-squares set in Q with A subset X or A subset Y;
  C effectively computable, C >= 1, independent of a and b
holds-here: yes — the Robertson AP {a-b, a, a+b} of x(2Q_i) is an AP inside X, so a putative
  MSS must satisfy 3 <= C^(1+r(E_e)); the consecutive-squares class does NOT apply (square
  roots of an AP of squares are never in AP when r^2+s^2 = 2e^2)
status: proved (theorem stated and proved in the paper; statement verified in the full text v1;
  no explicit value or formula for C is given anywhere)
bearing: makes the Garcia-Fritz-Pasten AP-length constant effective in principle, resolving the
  ineffectiveness obstruction of uniform-height-bound-elliptic-ap; but since C is uncomputed and
  built from David-Philippon uniform Mordell-Lang constants, the inequality C^(1+r) < 3 cannot be
  evaluated and is not obtainable from the paper; the §7 proof of Theorem 1.1 does not use
  weak-PFR (140, 110), correcting the earlier note
answers: hms-constant-bound
anchor: research/summaries/harrison-mudgal-schmidt-sum-product-bremner-2026.html.md
```

## Plain-English verdict

**No concrete number can be extracted from this paper.** C^(1+r) < 3 would require C < 3 when r = 0 and C < 3^(1/2) ≈ 1.733 when r ≥ 1; the paper gives neither a value for C nor any bound on it, and its only route to an explicit C runs through David–Philippon's quantitative uniform Mordell–Lang, whose constants are known (from the DP07 literature, not stated in this paper) to be far beyond 3. The advance is real and theoretical: the uniform AP-length bound for elliptic curves is now stated with an *effectively computable* constant, so "decide whether C^(1+r) < 3" is a well-posed finite task rather than an open-ended one. But within the paper it stays unexecuted, and there is no prospect from HMS's Theorem 1.1 alone of a rank-bound R with C^(1+R) < 3. The uniform-height approach survives only as "an effective bound exists and is formally decidable"; the next lane (thread step 0) remains David–Philippon's actually-explicit constant, not this paper.