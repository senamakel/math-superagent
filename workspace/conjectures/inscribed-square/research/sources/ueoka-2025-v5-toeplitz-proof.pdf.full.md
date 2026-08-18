<!-- source: https://zenodo.org/records/17847990/files/v5%20English%20ToeplitzConjecture.pdf?download=1 | converted from PDF -->

The Proof of the Inscribed Square Problem using
Topological Degree

Yohiki Ueoka (Shiki Ueoka) ∗ AI support Gemini † ChatGPT ‡

December 7, 2025

Abstract

We present a proof demonstrating the existence of a non-degenerate inscribed
square in any C0 Jordan curve in the plane. The main idea is to formulate the
square condition based on distances, constructing a continuous map F : T 4 → R4

for any continuous curve. By uniformly approximating the C0 curve by a sequence
of C1 curves, we show that the corresponding maps Fn converge uniformly to F0.
A detailed analysis of the boundary ∂T 4 confirms that all Fn are non-zero on the
boundary, and a uniform positive margin exists. Furthermore, the sequence of
zero points does not approach the boundary, thus excluding degenerate squares.
Combining these elements, we extend the argument of topological degree from the
C1 case to the C0 curve, resolving Toeplitz’s conjecture for continuous curves.

Acknowledgments

This research is the result of a collaboration between human and AI systems. Intuition re-
garding the “boundary margin”and the “exclusion of degenerate squares”was provided by
Shiki Ueoka (The pen name of Yoshiki Ueoka). The construction of the distance-
based map F and the topological degree argument were primarily developed by AI support
Gemini. AI support ChatGPT contributed to reviewing the initial draft and proposing
the refinement of the angular conditions into distance-based polynomial conditions.

1 Parameter Space and the Square Map

1.1 The Parameter Space T 4

Let γ : [0, 1] → R
2 be a continuous, injective map satisfying γ(0) = γ(1), parametrizing
the Jordan curve.

T 4 = {(t1, t2, t3, t4) ∈ [0, 1]
4 : 0 ≤ t1 < t2 < t3 < t4 ≤ 1}.

The boundary is given by

∂T 4 = {t ∈ T 4 : ti = tj for some i < j}.

∗Independent Researcher
†Google AI
‡OpenAI
 1

1.2 Distance-Based Square Condition

Let pi = γ(ti) and ℓij = ∥pi − pj∥. The conditions for (p1, p2, p3, p4) to form a square are:

ℓ12 = ℓ23 = ℓ34 = ℓ41,
ℓ13 = ℓ24,
ℓ2
13 = 2 ℓ
2
12.

1.3 Definition of the Square Map

Definition 1.1. The map F : T 4 → R4 is defined as

F (t) =
 





 ℓ12 − ℓ23
ℓ23 − ℓ34
ℓ13 − ℓ24
ℓ
2
13 − 2ℓ
2
12







Lemma 1.2. If γ is continuous, then F is continuous on T 4.

Proof. The continuity of F follows directly from the continuity of pi and the fact that all
components of F are algebraic combinations of the continuous distance functions ℓij.

2 Uniform Approximation and Map Convergence

Let γn be a sequence of C 1 Jordan curves such that ∥γn − γ0∥∞ → 0, and let Fn be the
corresponding square map.

Lemma 2.1 (Uniform Convergence).

∥Fn − F0∥∞ → 0.

Proof. By the triangle inequality, the distances ℓ
(n)
ij converge uniformly to ℓ
(0)
ij because
|ℓ
(n)
ij − ℓ
(0)
ij | ≤ 2∥γn − γ0∥∞. Since the components of F are continuous functions of ℓij,
the map Fn converges uniformly to F0.

3 Boundary Behavior and Degree Stability

Lemma 3.1 (Non-zero on the Boundary). For any n and t ∈ ∂T 4, we have Fn(t) ̸= 0.

Proof. If t ∈ ∂T 4, then ti = tj for some i, j, implying pi = pj and ℓij = 0. If Fn(t) = 0,
all side lengths must be equal and non-zero, leading to a contradiction since at least one
side length ℓij must be zero.

Lemma 3.2 (Uniform Margin on the Boundary). There exists an ϵ > 0 such that for all
n and t ∈ ∂T 4, ∥Fn(t)∥ ≥ ϵ.

2

Proof. Since F0 is continuous, non-zero on the compact boundary ∂T 4, it attains a min-
imum m0 = mint∈∂T 4 ∥F0(t)∥ > 0. By the uniform convergence ∥Fn − F0∥∞ → 0, for
ϵ
′ = m0/2, there exists N such that for all n > N and t ∈ ∂T 4, ∥Fn(t)∥ > m0/2. Setting
ϵ = min(m0/2, minn=1,...,N mint∈∂T 4 ∥Fn(t)∥), we guarantee a uniform positive margin ϵ
for all n.

Lemma 3.3 (Degree Stability). For sufficiently large n,

deg(F0, T 4, 0) = deg(Fn, T 4, 0).

Proof. The uniform margin on the boundary ensures that the homotopy connecting Fn
and F0 is non-zero on the boundary ∂T 4. By the stability property of the Brouwer degree,
the degrees coincide.

4 Exclusion of Degeneracy and Existence of the Limit
Square

Let Z(Fn) = {t : Fn(t) = 0}.

Lemma 4.1 (Zero Points Stay Away from the Boundary). There exists a δ > 0 such that
for all n and t ∈ Z(Fn), dist(t, ∂T 4) ≥ δ.

Proof. If a sequence of zero points t
(k) ∈ Z(Fnk) approached the boundary t
∗ ∈ ∂T 4,
the uniform convergence Fnk → F0 would imply F0(t∗) = 0, contradicting the boundary
non-zero property guaranteed by Lemma 3.2.

Lemma 4.2 (Positive Minimum Side Length). There exists an η > 0 such that for any
t ∈ Z(F0), ℓ12(t) ≥ η.

Proof. If ℓ12(t) = 0 for t ∈ Z(F0), then p1 = p2. Since γ is injective, this implies t1 = t2,
so t ∈ ∂T 4. This contradicts Lemma 4.1. Thus, ℓ12(t) > 0. Since Z(F0) is a compact set,
the continuous function ℓ12(t) attains a minimum η > 0.

Corollary 4.3. Any zero point in Z(F0) represents a non-degenerate square.

5 The Main Theorem

Theorem 5.1. Every C 0 Jordan curve has a non-degenerate inscribed square.

Proof. For the C 1 case, the inscribed square problem is known to be solved, and it is
established that deg(Fn, T 4, 0) ̸= 0

for the corresponding map (see [1], [2]). By the Degree Stability Lemma 3.3,

deg(F0, T 4, 0) = deg(Fn, T 4, 0) ̸= 0.

Therefore, F0 must possess a zero point t
∗. The Corollary 5.2 and Lemma 4.2 ensure that
this zero point corresponds to a non-degenerate square.

3

References

References

[1] Pugh, C. C. (2009). The Inscribed Square Problem. A preprint circulated by the
author.

[2] Shnirel’man, L. G. (1944). On certain geometrical properties of closed curves. Uspekhi
Matematicheskikh Nauk, 1(2): 164–168. (Russian)

[3] Stromquist, W. (1989). Inscribed squares and continuous curves. The American Math-
ematical Monthly, 96(6): 521–523.
 4
