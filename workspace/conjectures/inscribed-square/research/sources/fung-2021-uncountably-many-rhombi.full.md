<!-- source: https://ar5iv.labs.arxiv.org/html/2010.05101 | converted from HTML -->

[2010.05101] Every Jordan curve inscribes uncountably many rhombi

# Every Jordan curve inscribes uncountably many rhombi

Antony T.H. Fung

Date: August 7, 2026

###### Abstract.

We prove that every Jordan curve in ℝ 2 \mathbb{R}^{2} inscribes uncountably many rhombi. No regularity condition is assumed on the Jordan curve.

## 1. Introduction

The inscribed square problem is a famous open problem due to Otto Toeplitz in 1911 [7], which asks whether all Jordan curves in ℝ 2 \mathbb{R}^{2} inscribe a square. By “inscribe”, it means that all four vertices lie on the curve. There are lots of results for the case when the Jordan curve is “nice” [2] [3] [4] [6]. However, other than Vaughan’s result stating that every Jordan curve in ℝ 2 \mathbb{R}^{2} inscribes a rectangle (see [5]), little progress has been done on the general case.

One of the earliest results was Arnold Emch’s work [1]. In 1916, he proved that all piecewise analytic Jordan curves in ℝ 2 \mathbb{R}^{2} with only finitely many “bad” points inscribe a square. Emch’s approach was that given a direction τ \tau, construct the set of medians M τ M_{\tau}, defined as (roughly speaking) the set of midpoints of pairs of points on the curve that lie on the same line going in direction τ \tau. When the Jordan curve is nice enough, M τ M_{\tau} is a nice path. Now consider an orthogonal direction σ \sigma and similarly construct M σ M_{\sigma}. The paths M τ M_{\tau} and M σ M_{\sigma} must intersect, and their intersections correspond to quadrilaterals with diagonals perpendicularly bisecting each other, i.e. rhombi. Then by rotating and using the intermediate value theorem, he showed that at some direction, one of those rhombi is a square.

In this paper, we will follow a similar approach to show the existence of rhombi. However, without assuming analyticity, M τ M_{\tau} may not necessarily be a path. To get around this, we will define a new class of object called a pseudopath that has properties similar to a path. Then we will show that M τ M_{\tau} is a pseudopath, and use those properties of pseudopath to proceed the argument.

In this paper, we prove the following:

###### Theorem 1.1.

Let γ: S 1 → ℝ 2 \gamma:S^{1}\rightarrow\mathbb{R}^{2} be a Jordan curve. Then there exists an open interval of angles such that there exists inscribed rhombi of all these angles. Furthermore, if γ \gamma does not contain a special corner, then there exists inscribed rhombi of all angles.

In this section, we will define what is a rhombus of an angle and what is a special corner. In this paper, an inscribed rhombus is a set of 4 distinct points in i ​ m ​ ( γ) im(\gamma) such that those 4 points are the vertices of a rhombus in ℝ 2 \mathbb{R}^{2}.

A corollary of Theorem 1.1 is that every Jordan curve in ℝ 2 \mathbb{R}^{2} inscribes uncountably many rhombi.

###### Definition 1.2 (line of angle θ \theta).

A line of angle θ \theta means a line in the form x ​ sin ⁡ θ − y ​ cos ⁡ θ = x\sin\theta-y\cos\theta= constant. i.e. a line making angle θ \theta with the x x -axis in an anti-clockwise manner.

###### Definition 1.3 (special corner of angle θ \theta).

Let γ: S 1 → ℝ 2 \gamma:S^{1}\rightarrow\mathbb{R}^{2} be a Jordan curve. A special corner of γ \gamma of angle θ \theta is a point p ∈ i ​ m ​ ( γ) p\in im(\gamma) such that both the line of angle θ \theta through p p and the line of angle θ + π 2 \theta+\dfrac{\pi}{2} through p p only intersect i ​ m ​ ( γ) im(\gamma) at p p.

[image: [Uncaptioned image]]

Figure 1: p p is a special corner of angle θ \theta

###### Definition 1.4 (special corner).

Let γ: S 1 → ℝ 2 \gamma:S^{1}\rightarrow\mathbb{R}^{2} be a Jordan curve. A point p p is a special corner of γ \gamma if it is a special corner of γ \gamma of at least one angle θ \theta.

Intuitively, a special corner is a point on i ​ m ​ ( γ) im(\gamma) such that translating to the origin and rotating, the entire curve lies within a single quadrant.

###### Definition 1.5 (rhombus of angle θ \theta).

We say that a rhombus in ℝ 2 \mathbb{R}^{2} is a rhombus of angle θ \theta if the two diagonals are lines with angles θ \theta and θ + π 2 \theta+\dfrac{\pi}{2} respectively.

Clearly, “rhombus of angle θ \theta ” and “rhombus of angle θ + π 2 \theta+\frac{\pi}{2} ” are the same concept.

Now we can state Theorem 1.1 again in a more precise manner. We divide it into three separate statements.

###### Proposition 1.6.

Let γ: S 1 → ℝ 2 \gamma:S^{1}\rightarrow\mathbb{R}^{2} be a Jordan curve and θ ∈ ℝ \theta\in\mathbb{R}. If there is no special corner of angle θ \theta, then there exists an inscribed rhombus of angle θ \theta.

In particular, this implies that Jordan curves with no special corners have inscribed rhombi of all angles, and hence satisfying Theorem 1.1.

###### Proposition 1.7.

Let γ: S 1 → ℝ 2 \gamma:S^{1}\rightarrow\mathbb{R}^{2} be a Jordan curve with exactly one special corner. Then ∃ θ 0 \exists\theta_{0} and ϵ > 0 \epsilon>0 such that ∀ θ ∈ ( θ 0 − ϵ, θ 0 + ϵ) \forall\theta\in(\theta_{0}-\epsilon,\theta_{0}+\epsilon), there is no special corner of angle θ \theta.

Together with Proposition 1.6, this implies that Jordan curves with exactly one special corner satisfy Theorem 1.1.

###### Proposition 1.8.

Let γ: S 1 → ℝ 2 \gamma:S^{1}\rightarrow\mathbb{R}^{2} be a Jordan curve with at least two special corners. Let p p and q q be distinct special corners of γ \gamma, and suppose that the line passing through p p and q q is a line of angle θ 0 \theta_{0} for some θ 0 \theta_{0}. Then ∃ ϵ > 0 \exists\epsilon>0 such that ∀ θ ∈ ( θ 0 − ϵ, θ 0 + ϵ) \forall\theta\in(\theta_{0}-\epsilon,\theta_{0}+\epsilon), there exists an inscribed rhombus of angle θ \theta.

This implies that Jordan curves with at least two special corners satisfy Theorem 1.1.

Together, Propositions 1.6, 1.7, 1.8 imply Theorem 1.1.

We will quickly prove Proposition 1.7 first. Then in Section 2 we will develop some machinery in point-set topology to prove Proposition 1.6. In Section 3 we will prove Proposition 1.6. In Section 4 we will refine the arguments used in Section 3 to prove Proposition 1.8, and hence completing the proof of Theorem 1.1.

###### Proof of Proposition 1.7.

Suppose p p is the unique special corner of a Jordan curve γ: S 1 → ℝ 2 \gamma:S^{1}\rightarrow\mathbb{R}^{2}. Let q 1, q 2 q_{1},q_{2} be two other points in i ​ m ​ ( γ) im(\gamma) such that p, q 1, q 2 p,q_{1},q_{2} are not collinear. Let q q be the mid-point of q 1 q_{1} and q 2 q_{2}. For each θ \theta, let l θ l_{\theta} be the line of angle θ \theta through p p. Let θ 0 \theta_{0} be such that l θ 0 l_{\theta_{0}} passes through q q. Let ϵ = m ​ i ​ n ​ ( ∠ ​ q 2 ​ p ​ q, ∠ ​ q ​ p ​ q 1) \epsilon=min(\angle q_{2}pq,\angle qpq_{1}). Then ∀ θ ∈ ( θ 0 − ϵ, θ 0 + ϵ) \forall\theta\in(\theta_{0}-\epsilon,\theta_{0}+\epsilon), q 1 q_{1} and q 2 q_{2} are on opposite sides of the l θ l_{\theta}. Since i ​ m ​ ( γ) \ { p } im(\gamma)\backslash\{p\} is path-connected, i ​ m ​ ( γ) im(\gamma) must intersect l θ l_{\theta} at a point other than p p, and hence p p is not a special corner of angle θ \theta. Since p p is the unique special corner of γ \gamma, there is no special corners of angle θ \theta.

[image: [Uncaptioned image]]

Figure 2: Proof of Proposition 1.7

∎

## 2. Some point-set topology

We begin with our key concept.

###### Definition 2.1 (pseudopath).

Let X X be a topological space, and p, q ∈ X p,q\in X. A pseudopath between p p and q q is a compact set C ⊆ X C\subseteq X such that p, q ∈ C p,q\in C and ∀ \forall open set U U containing C C, ∃ \exists a path γ \gamma from p p to q q satisfying i ​ m ​ ( γ) ⊆ U im(\gamma)\subseteq U.

Intuitively, a pseudopath is a compact set that is arbitrarily close to containing a path. We note some properties of pseudopaths.

First of all, clearly the image of a path is a pseudopath. So pseudopath is a generalization of path. Another straightforward property of pseudopath is that the image of a pseudopath is a pseudopath:

###### Lemma 2.2.

Let f: X → Y f:X\rightarrow Y be a continuous function between topological spaces. If C C be a pseudopath between the points p, q ∈ X p,q\in X, then f ⁡ ( C) f(C) is a pseudopath between f ⁡ ( p), f ⁡ ( q) f(p),f(q).

###### Proof.

Since C is compact, f ⁡ ( C) f(C) is also compact. Since p, q ∈ C p,q\in C, f ⁡ ( p) f(p) and f ⁡ ( q) f(q) must be in f ⁡ ( C) f(C). Suppose U U is open in Y Y and contains f ⁡ ( C) f(C). Then f − 1 ​ ( U) f^{-1}(U) is open in X X and contains C C, and hence contains the image of a path γ \gamma from p p to q q. Then f ∘ γ f\circ\gamma is our desired path from f ⁡ ( p) f(p) to f ⁡ ( q) f(q) with image lying within U U. ∎

Now we prove the most crucial property of pseudopath in this paper.

###### Lemma 2.3.

Let A, B, C, D A,B,C,D be 4 distinct points on ∂ 𝔻 2 = S 1 \partial\mathbb{D}^{2}=S^{1} labeled in that order (i.e. A, C A,C lie in different path components in ∂ 𝔻 2 \ { B, D } \partial\mathbb{D}^{2}\backslash\{B,D\}). Let K K be a compact set in 𝔻 2 \mathbb{D}^{2} that intersects ∂ 𝔻 2 \partial\mathbb{D}^{2} at B B and D D, and only at B B and D D. If A, C A,C lie in different path components in 𝔻 2 \ K \mathbb{D}^{2}\backslash K, then K K is a pseudopath in 𝔻 2 \mathbb{D}^{2} between B B and D D.

[image: [Uncaptioned image]]

Figure 3: An example of Lemma 2.3

Note that K K does not necessarily contain the image of a path from B B to D D. For example, if we consider the example given in Figure 3 where K K is a set that looks like the graph of y = sin ⁡ ( 1 x) y=\sin(\frac{1}{x}), x ≠ 0 x\neq 0, with the hole at x = 0 x=0 being filled. It does not contain the image of a path going from B B to D D. That is precisely the reason why we have to deal with pseudopaths instead of just paths.

The key to proving Lemma 2.3 is Alexander duality, which requires local contractibility. Regarding the comment above on the example given in Figure 3, the graph of y = sin ⁡ ( 1 x) y=\sin(\frac{1}{x}) is not locally contractible at 0 0, which prevents us from using Alexander duality directly. Our strategy of proving Lemma 2.3 is that we first construct a locally contractible set, and then we apply Alexander duality.

Now we prove Lemma 2.3.

###### Proof.

We want to show that K K is a pseudopath in 𝔻 2 \mathbb{D}^{2} between B B and D D. Let U U be an arbitrary open set in 𝔻 2 \mathbb{D}^{2} containing K K. As U U is arbitrary, it suffices to show that inside U U, there exists a path going from B B to D D.

Embed 𝔻 2 \mathbb{D}^{2} in ℝ 2 \mathbb{R}^{2} in a standard way and give 𝔻 2 \mathbb{D}^{2} the Euclidean metric inherited from ℝ 2 \mathbb{R}^{2}. Now we can treat 𝔻 2 \mathbb{D}^{2} as a metric space. Consider small open balls around B B and D D that are contained in U U. Call them B ϵ B ​ ( B) B_{\epsilon_{B}}(B) and B ϵ D ​ ( D) B_{\epsilon_{D}}(D). Choose ϵ B \epsilon_{B} and ϵ D \epsilon_{D} to be small enough such that the closed balls B ϵ B ¯ ​ ( B) \overline{B_{\epsilon_{B}}}(B) and B ϵ D ¯ ​ ( D) \overline{B_{\epsilon_{D}}}(D) are contained in U \ { A, C } U\backslash\{A,C\}. Around each point in k ∈ K \ { B, D } k\in K\backslash\{B,D\}, consider an open ball B ϵ k ​ ( k) B_{\epsilon_{k}}(k) contained within U U. Choose ϵ k \epsilon_{k} to be small enough such that the closed ball B ϵ k ¯ ​ ( k) \overline{B_{\epsilon_{k}}}(k) is contained in U \ ∂ 𝔻 2 U\backslash\partial\mathbb{D}^{2}.

The open balls B ϵ B ​ ( B) B_{\epsilon_{B}}(B), B ϵ D ​ ( D) B_{\epsilon_{D}}(D), and those B ϵ k ​ ( k) B_{\epsilon_{k}}(k) ’s together form an open cover of K K. By compactness, there exists a subcover that contains only finitely many B ϵ k ​ ( k) B_{\epsilon_{k}}(k) ’s. Let X X be the union of B ϵ B ¯ ​ ( B) \overline{B_{\epsilon_{B}}}(B) and B ϵ D ¯ ​ ( D) \overline{B_{\epsilon_{D}}}(D) and all those B ϵ k ¯ ​ ( k) \overline{B_{\epsilon_{k}}}(k) ’s for each B ϵ k ​ ( k) B_{\epsilon_{k}}(k) in the subcover. Since X X is a union of finitely many closed balls, it must be locally contractible (which is required for using Alexander duality), and 𝔻 2 \ X \mathbb{D}^{2}\backslash X has finitely many path components. Let n n be the number of path components in 𝔻 2 \ X \mathbb{D}^{2}\backslash X. Also, by construction, K ⊆ X ⊆ U \ { A, C } K\subseteq X\subseteq U\backslash\{A,C\}, and ∂ 𝔻 2 \ X \partial\mathbb{D}^{2}\backslash X has exactly 2 path components, one containing A A and one containing C C (because B ϵ B ¯ ​ ( B) \overline{B_{\epsilon_{B}}}(B) and B ϵ D ¯ ​ ( D) \overline{B_{\epsilon_{D}}}(D) are the only closed balls used that can intersect ∂ 𝔻 2 \partial\mathbb{D}^{2}).

Let I I be an arc of a very big circle in ℝ 2 \mathbb{R}^{2} that connects B B and D D. Choose I I be the arc that only intersects 𝔻 2 \mathbb{D}^{2} at B B and D D.

[image: [Uncaptioned image]]

Figure 4: X X and I I. X X is a finite union of closed balls that covers K K.

Here, we view S 2 S^{2} as the one point compactification of ℝ 2 \mathbb{R}^{2}.

Inside S 2 \ X S^{2}\backslash X, A A and C C are in the same path component, and the path components of A A and C C in 𝔻 2 \ X \mathbb{D}^{2}\backslash X are the only ones that merged when embedded in S 2 \ X S^{2}\backslash X because there are only 2 path components in ∂ 𝔻 2 \partial\mathbb{D}^{2}. Hence, H 0 ​ ( S 2 \ X) = ℤ n − 1 H_{0}(S^{2}\backslash X)=\mathbb{Z}^{n-1}. Note that ℤ \mathbb{Z} coefficients are implicit. By Alexander duality and universal coefficient theorem, H 1 ​ ( X) = ℤ n − 2 H_{1}(X)=\mathbb{Z}^{n-2}.

Now we consider X ∪ I X\cup I. In S 2 \ ( i ​ n ​ t ​ ( 𝔻 2) ∪ I) S^{2}\backslash(int(\mathbb{D}^{2})\cup I), I I separates A A and C C into different path components. Note that S 2 \ ( X ∪ I) S^{2}\backslash(X\cup I) is the union of the two closed subspaces S 2 \ ( i ​ n ​ t ​ ( 𝔻 2) ∪ I) S^{2}\backslash(int(\mathbb{D}^{2})\cup I) and 𝔻 2 \ X \mathbb{D}^{2}\backslash X, and the two closed subspaces intersect at ∂ 𝔻 2 \ X \partial\mathbb{D}^{2}\backslash X. ∂ 𝔻 2 \ X \partial\mathbb{D}^{2}\backslash X has only 2 path components, the one with A A and the one with C C. Hence, all the path components in 𝔻 2 \ X \mathbb{D}^{2}\backslash X except for the two containing A A or C C remain being separate path components in S 2 \ ( X ∪ I) S^{2}\backslash(X\cup I). Those two path components containing A A or C C also remain separate because they are separate in S 2 \ ( i ​ n ​ t ​ ( 𝔻 2) ∪ I) S^{2}\backslash(int(\mathbb{D}^{2})\cup I). Hence, H 0 ​ ( S 2 \ ( X ∪ I)) = ℤ n H_{0}(S^{2}\backslash(X\cup I))=\mathbb{Z}^{n}. By Alexander duality and universal coefficient theorem, H 1 ​ ( X ∪ I) = ℤ n − 1 H_{1}(X\cup I)=\mathbb{Z}^{n-1}. Therefore, H 1 ​ ( X) ≇ H 1 ​ ( X ∪ I) H_{1}(X)\not\cong H_{1}(X\cup I).

Now we consider the Mayer-Vietoris sequence
⋯ → H 1 ​ ( { B, D }) → H 1 ​ ( X) ⊕ H 1 ​ ( I) → H 1 ​ ( X ∪ I) → H 0 ​ ( { B, D }) → H 0 ​ ( X) ⊕ H 0 ​ ( I) → ⋯ \cdots\rightarrow H_{1}(\{B,D\})\rightarrow H_{1}(X)\oplus H_{1}(I)\rightarrow H_{1}(X\cup I)\rightarrow H_{0}(\{B,D\})\rightarrow H_{0}(X)\oplus H_{0}(I)\rightarrow\cdots

Note that H 1 ​ ( { B, D }) H_{1}(\{B,D\}) and H 1 ​ ( I) H_{1}(I) are 0 0, and H 1 ​ ( X) ≇ H 1 ​ ( X ∪ I) H_{1}(X)\not\cong H_{1}(X\cup I). So, the map H 1 ​ ( X ∪ I) → H 0 ​ ( { B, D }) H_{1}(X\cup I)\rightarrow H_{0}(\{B,D\}) is not the zero map, and hence the map H 0 ​ ( { B, D }) → H 0 ​ ( X) ⊕ H 0 ​ ( I) H_{0}(\{B,D\})\rightarrow H_{0}(X)\oplus H_{0}(I) cannot be injective. Therefore, under the map H 0 ​ ( { B, D }) → H 0 ​ ( I) H_{0}(\{B,D\})\rightarrow H_{0}(I) induced by inclusion, [B] [B] and [D] [D] must be mapped to the same path component in X X, and hence there exists a path within X X that goes from B B to D D.

As X ⊆ U X\subseteq U, the proof of Lemma 2.3 is completed. ∎

We prove one more property of pseudopaths before we go back to proving our theorem about Jordan curves.

###### Lemma 2.4.

Let A, B, C, D A,B,C,D be 4 distinct points on ∂ 𝔻 2 = S 1 \partial\mathbb{D}^{2}=S^{1} labeled in that order (i.e. A, C A,C lie in different path components in ∂ 𝔻 2 \ { B, D } \partial\mathbb{D}^{2}\backslash\{B,D\}). Let K K be a pseudopath in 𝔻 2 \mathbb{D}^{2} between A, C A,C, and L L be a pseudopath in 𝔻 2 \mathbb{D}^{2} between B, D B,D. Then K ∩ L ≠ ∅ K\cap L\neq\varnothing.

###### Proof.

We proceed by contradiction. Assume that K ∩ L = ∅ K\cap L=\varnothing. As K K and L L are compact sets in a Hausdorff space, there exists open sets U U, V V such that K ⊆ U K\subseteq U and L ⊆ V L\subseteq V and U ∩ V = ∅ U\cap V=\varnothing. So, by the definition of pseudopath, there exists a path from A A to C C and a path from B B to D D that do not intersect each other, which is impossible. ∎

## 3. Proof of Proposition 1.6

This section is entirely devoted to the proof of Proposition 1.6.

We fix a Jordan curve γ: S 1 → ℝ 2 \gamma:S^{1}\rightarrow\mathbb{R}^{2}, and suppose θ \theta is an angle with no special corners.

Note that we will not use the fact that θ \theta is an angle with no special corners until the end of this section. Claim 3.3 and everything before holds for all θ \theta, not just for those without special corners.

Consider the function ( x, y) ↦ x ​ sin ⁡ θ − y ​ cos ⁡ θ (x,y)\mapsto x\sin\theta-y\cos\theta on i ​ m ​ ( γ) im(\gamma). As i ​ m ​ ( γ) im(\gamma) is compact, the function has a maximum and a minimum. Let M θ M_{\theta} be the maximum and m θ m_{\theta} be the minimum. Let μ θ:= M θ + m θ 2 \mu_{\theta}:=\dfrac{M_{\theta}+m_{\theta}}{2}.

Note that the line x ​ sin ⁡ θ − y ​ cos ⁡ θ = M θ x\sin\theta-y\cos\theta=M_{\theta} can be parametrized as { x = t ​ cos ⁡ θ + M θ ​ sin ⁡ θ y = t ​ sin ⁡ θ − M θ ​ cos ⁡ θ \begin{cases}x=t\cos\theta+M_{\theta}\sin\theta\\ y=t\sin\theta-M_{\theta}\cos\theta\end{cases}. Among all the points that are both in im ⁡ ( γ) \operatorname{im}(\gamma) and on the line x ​ sin ⁡ θ − y ​ cos ⁡ θ = M θ x\sin\theta-y\cos\theta=M_{\theta}, let M ​ M θ MM_{\theta} be the point that attains the maximal t t under this parametrization ( M ​ M θ MM_{\theta} exists by compactness). Similarly define m ​ M θ mM_{\theta} to be the one with minimal t t.

(Note that M ​ M θ MM_{\theta} and m ​ M θ mM_{\theta} may not necessarily be distinct)

Similarly, define M ​ m θ Mm_{\theta} and m ​ m θ mm_{\theta} using the line x ​ sin ⁡ θ − y ​ cos ⁡ θ = m θ x\sin\theta-y\cos\theta=m_{\theta}, and define M ​ μ θ M\mu_{\theta} and m ​ μ θ m\mu_{\theta} using the line x ​ sin ⁡ θ − y ​ cos ⁡ θ = μ θ x\sin\theta-y\cos\theta=\mu_{\theta}. Let t θ m ​ i ​ n t^{min}_{\theta} be the t t value that realizes m ​ μ θ m\mu_{\theta} under that parametrization, and let t θ m ​ a ​ x t^{max}_{\theta} be the t t value that realizes M ​ μ θ M\mu_{\theta} under that parametrization. Let A θ A_{\theta} be the mid-point of M ​ m θ Mm_{\theta} and m ​ m θ mm_{\theta}, and B θ B_{\theta} be the mid-point of M ​ M θ MM_{\theta} and m ​ M θ mM_{\theta}.

[image: [Uncaptioned image]]

Figure 5: Constructions of m ​ m θ mm_{\theta}, M ​ m θ Mm_{\theta}, m ​ M θ mM_{\theta}, M ​ M θ MM_{\theta}, m ​ μ θ m\mu_{\theta}, M ​ μ θ M\mu_{\theta}, A θ A_{\theta}, B θ B_{\theta}

Along the Jordan curve γ \gamma, there are two arcs from m ​ m θ mm_{\theta} to m ​ M θ mM_{\theta}, one containing m ​ μ θ m\mu_{\theta} and one doesn’t. Let γ θ \gamma_{\theta} be the arc containing m ​ μ θ m\mu_{\theta}, parametrized with γ θ ​ ( 0) = m ​ m θ \gamma_{\theta}(0)=mm_{\theta} and γ θ ​ ( 1) = m ​ M θ \gamma_{\theta}(1)=mM_{\theta}, and γ θ: [0, 1] → ℝ 2 \gamma_{\theta}:[0,1]\rightarrow\mathbb{R}^{2} being injective. Let γ θ o \gamma^{o}_{\theta} be the arc not containing m ​ μ θ m\mu_{\theta}, parametrized with γ θ o ​ ( 0) = m ​ m θ \gamma^{o}_{\theta}(0)=mm_{\theta} and γ θ o ​ ( 1) = m ​ M θ \gamma^{o}_{\theta}(1)=mM_{\theta}.

Similarly, let Γ θ \Gamma_{\theta} be the arc along γ \gamma from M ​ m θ Mm_{\theta} to M ​ M θ MM_{\theta} that passes through M ​ μ θ M\mu_{\theta}, parametrized with Γ θ ​ ( 0) = M ​ m θ \Gamma_{\theta}(0)=Mm_{\theta} and Γ θ ​ ( 1) = M ​ M θ \Gamma_{\theta}(1)=MM_{\theta}, and Γ θ: [0, 1] → ℝ 2 \Gamma_{\theta}:[0,1]\rightarrow\mathbb{R}^{2} being injective.

Now we prove some properties of γ θ \gamma_{\theta} and Γ θ \Gamma_{\theta}.

###### Claim 3.1.

The following 4 statements are all true:

1. (1)

i ​ m ​ ( γ θ) im(\gamma_{\theta}) and the line x ​ sin ⁡ θ − y ​ cos ⁡ θ = m θ x\sin\theta-y\cos\theta=m_{\theta} only intersect at m ​ m θ mm_{\theta}

2. (2)

i ​ m ​ ( γ θ) im(\gamma_{\theta}) and the line x ​ sin ⁡ θ − y ​ cos ⁡ θ = M θ x\sin\theta-y\cos\theta=M_{\theta} only intersect at m ​ M θ mM_{\theta}

3. (3)

i ​ m ​ ( Γ θ) im(\Gamma_{\theta}) and the line x ​ sin ⁡ θ − y ​ cos ⁡ θ = m θ x\sin\theta-y\cos\theta=m_{\theta} only intersect at M ​ m θ Mm_{\theta}

4. (4)

i ​ m ​ ( Γ θ) im(\Gamma_{\theta}) and the line x ​ sin ⁡ θ − y ​ cos ⁡ θ = M θ x\sin\theta-y\cos\theta=M_{\theta} only intersect at M ​ M θ MM_{\theta}

###### Proof.

By symmetry, we only have to prove (1). We will prove it by contradiction.

Suppose there is a point p ​ m θ ∈ i ​ m ​ ( γ θ) pm_{\theta}\in im(\gamma_{\theta}) lying on the line x ​ sin ⁡ θ − y ​ cos ⁡ θ = m θ x\sin\theta-y\cos\theta=m_{\theta} with p ​ m θ ≠ m ​ m θ pm_{\theta}\neq mm_{\theta}. Both p ​ m θ pm_{\theta} and m ​ μ θ m\mu_{\theta} are in i ​ m ​ ( γ θ) im(\gamma_{\theta}), so we can let γ θ | [a, b] \gamma_{\theta}|_{[a,b]} to be a path either going from p ​ m θ pm_{\theta} to m ​ μ θ m\mu_{\theta} or going from m ​ μ θ m\mu_{\theta} to p ​ m θ pm_{\theta}, for some 0 < a < b < 1 0<a<b<1.

Since γ \gamma is a Jordan curve, it cannot self-intersect. So i ​ m ​ ( γ θ o) ∩ i ​ m ​ ( γ θ | [a, b]) = ∅ im(\gamma^{o}_{\theta})\cap im(\gamma_{\theta}|_{[a,b]})=\varnothing. By the definition of M θ M_{\theta} and m θ m_{\theta}, i ​ m ​ ( γ θ o) im(\gamma^{o}_{\theta}) has to lie within the stripe S θ:= { ( x, y) ∣ m θ ≤ x ​ sin ⁡ θ − y ​ cos ⁡ θ ≤ M θ } S_{\theta}:=\{(x,y)\mid m_{\theta}\leq x\sin\theta-y\cos\theta\leq M_{\theta}\}. Also, by the definition of m ​ μ θ m\mu_{\theta}, i ​ m ​ ( γ θ o) im(\gamma^{o}_{\theta}) cannot intersect the ray L θ:= { ( t ​ cos ⁡ θ + μ θ ​ sin ⁡ θ, t ​ sin ⁡ θ − μ θ ​ cos ⁡ θ) ∣ t ≤ t θ m ​ i ​ n } L_{\theta}:=\{(t\cos\theta+\mu_{\theta}\sin\theta,t\sin\theta-\mu_{\theta}\cos\theta)\mid t\leq t^{min}_{\theta}\}.

So i ​ m ​ ( γ θ o) ⊆ S θ \ ( i ​ m ​ ( γ θ | [a, b]) ∪ L θ) im(\gamma^{o}_{\theta})\subseteq S_{\theta}\backslash(im(\gamma_{\theta}|_{[a,b]})\cup L_{\theta}). However, in S θ S_{\theta}, i ​ m ​ ( γ θ | [a, b]) ∪ L θ im(\gamma_{\theta}|_{[a,b]})\cup L_{\theta} separates m ​ m θ mm_{\theta} and m ​ M θ mM_{\theta} into two different path components. So we have arrived a contradiction.

[image: [Uncaptioned image]]

Figure 6: Proof of Claim 3.1

∎

###### Claim 3.2.

i ​ m ​ ( γ θ | ( 0, 1)) ∩ i ​ m ​ ( Γ θ | ( 0, 1)) = ∅ im(\gamma_{\theta}|_{(0,1)})\cap im(\Gamma_{\theta}|_{(0,1)})=\varnothing (i.e. γ θ \gamma_{\theta} and Γ θ \Gamma_{\theta} don’t intersect, except possibly at the endpoints)

###### Proof.

Case 1: If M ​ M θ ≠ m ​ M θ MM_{\theta}\neq mM_{\theta} and M ​ m θ ≠ m ​ m θ Mm_{\theta}\neq mm_{\theta}, then by Claim 3.1, M ​ M θ, M ​ m θ ∉ i ​ m ​ γ θ MM_{\theta},Mm_{\theta}\notin im{\gamma_{\theta}} and m ​ M θ, m ​ m θ ∉ i ​ m ​ Γ θ mM_{\theta},mm_{\theta}\notin im{\Gamma_{\theta}}. So this is the only possible configuration:

[image: [Uncaptioned image]]

Figure 7: Proof of Claim 3.2 Case 1 (up to homeomorphism)

Case 2: If M ​ M θ = m ​ M θ MM_{\theta}=mM_{\theta} and M ​ m θ ≠ m ​ m θ Mm_{\theta}\neq mm_{\theta}, then by Claim 3.1, M ​ m θ ∉ i ​ m ​ γ θ Mm_{\theta}\notin im{\gamma_{\theta}} and m ​ m θ ∉ i ​ m ​ Γ θ mm_{\theta}\notin im{\Gamma_{\theta}}. So this is the only possible configuration:

[image: [Uncaptioned image]]

Figure 8: Proof of Claim 3.2 Case 2 (up to homeomorphism)

Case 3: If M ​ M θ ≠ m ​ M θ MM_{\theta}\neq mM_{\theta} and M ​ m θ = m ​ m θ Mm_{\theta}=mm_{\theta}, then the proof is similar to Case 2.

Case 4: If M ​ M θ = m ​ M θ MM_{\theta}=mM_{\theta} and M ​ m θ = m ​ m θ Mm_{\theta}=mm_{\theta}, then what we need to prove is proving that i ​ m ​ ( γ θ) ≠ i ​ m ​ ( Γ θ) im(\gamma_{\theta})\neq im(\Gamma_{\theta}). It suffices to show that M ​ μ θ ∉ i ​ m ​ ( γ θ) M\mu_{\theta}\notin im(\gamma_{\theta}). We will prove it by contradiction, in a similar fashion as the proof of Claim 3.1.

Suppose M ​ μ θ ∈ i ​ m ​ ( γ θ) M\mu_{\theta}\in im(\gamma_{\theta}). Then we let γ θ | [a, b] \gamma_{\theta}|_{[a,b]} to be a path either going from M ​ μ θ M\mu_{\theta} to m ​ μ θ m\mu_{\theta} or going from m ​ μ θ m\mu_{\theta} to M ​ μ θ M\mu_{\theta}, for some 0 < a < b < 1 0<a<b<1. Let

 | L θ:= { ( t ​ cos ⁡ θ + μ θ ​ sin ⁡ θ, t ​ sin ⁡ θ − μ θ ​ cos ⁡ θ) ∣ t ≤ t θ m ​ i ​ n } L_{\theta}:=\{(t\cos\theta+\mu_{\theta}\sin\theta,t\sin\theta-\mu_{\theta}\cos\theta)\mid t\leq t^{min}_{\theta}\} |  |

 | U θ:= { ( t ​ cos ⁡ θ + μ θ ​ sin ⁡ θ, t ​ sin ⁡ θ − μ θ ​ cos ⁡ θ) ∣ t ≥ t θ m ​ a ​ x } U_{\theta}:=\{(t\cos\theta+\mu_{\theta}\sin\theta,t\sin\theta-\mu_{\theta}\cos\theta)\mid t\geq t^{max}_{\theta}\} |  |

Since γ \gamma is a Jordan curve, i ​ m ​ ( γ θ o) ∩ i ​ m ​ ( γ θ | [a, b]) = ∅ im(\gamma^{o}_{\theta})\cap im(\gamma_{\theta}|_{[a,b]})=\varnothing. By the definition of M θ M_{\theta} and m θ m_{\theta}, i ​ m ​ ( γ θ o) im(\gamma^{o}_{\theta}) has to lie within the stripe S θ:= { ( x, y) ∣ m θ ≤ x ​ sin ⁡ θ − y ​ cos ⁡ θ ≤ M θ } S_{\theta}:=\{(x,y)\mid m_{\theta}\leq x\sin\theta-y\cos\theta\leq M_{\theta}\}. Also, by the definition of m ​ μ θ m\mu_{\theta} and M ​ μ θ M\mu_{\theta}, i ​ m ​ ( γ θ o) im(\gamma^{o}_{\theta}) cannot intersect L θ ∪ U θ L_{\theta}\cup U_{\theta}.

So, i ​ m ​ ( γ θ o) ⊆ S θ \ ( i ​ m ​ ( γ θ | [a, b]) ∪ L θ ∪ U θ) im(\gamma^{o}_{\theta})\subseteq S_{\theta}\backslash(im(\gamma_{\theta}|_{[a,b]})\cup L_{\theta}\cup U_{\theta}). However, in S θ S_{\theta}, i ​ m ​ ( γ θ | [a, b]) ∪ L θ ∪ U θ im(\gamma_{\theta}|_{[a,b]})\cup L_{\theta}\cup U_{\theta} separates m ​ m θ mm_{\theta} and m ​ M θ mM_{\theta} into two different path components. So we have arrived a contradiction.

[image: [Uncaptioned image]]

Figure 9: Proof of Claim 3.2 Case 4

∎

We have finished proving Claim 3.1 and Claim 3.2, which are properties of γ θ \gamma_{\theta} and Γ θ \Gamma_{\theta}. Now we define the median of the angle θ \theta, denoted as ℳ θ \mathcal{M}_{\theta}:

ℳ θ:= { mid-point of p 1 and p 2 ∣ p 1 ∈ i m ( γ θ), p 2 ∈ i m ( Γ θ), p 1 and p 2 lie on the same \mathcal{M}_{\theta}:=\{\text{mid-point of }p_{1}\text{ and }p_{2}\mid p_{1}\in im(\gamma_{\theta}),\ p_{2}\in im(\Gamma_{\theta}),\ p_{1}\text{ and }p_{2}\text{ lie on the same}
line of angle θ } \text{ line of angle }\theta\}

Remark: We call it “median” here because the construction is similar to Emch’s construction of medians in his paper about inscribed rhombi in piecewise analytic Jordan curves [1]. The only difference is that analyticity is not assumed here.

We will now prove that ℳ θ \mathcal{M}_{\theta} is a pseudopath from A θ A_{\theta} to B θ B_{\theta}. When we were defining the concept of pseudopaths, we worked inside a topological space. Therefore, we will first construct a topological space R ​ e ​ c θ Rec_{\theta} for us to work in.

Consider S θ:= { ( x, y) ∣ m θ ≤ x ​ sin ⁡ θ − y ​ cos ⁡ θ ≤ M θ } S_{\theta}:=\{(x,y)\mid m_{\theta}\leq x\sin\theta-y\cos\theta\leq M_{\theta}\}. For all constructions so far, we do the same construction for every angle, not just θ \theta.

Let R ​ e ​ c θ:= S θ ∩ S θ + π 2 Rec_{\theta}:=S_{\theta}\cap S_{\theta+\frac{\pi}{2}}. Clearly, R ​ e ​ c θ = R ​ e ​ c θ + π 2 Rec_{\theta}=Rec_{\theta+\frac{\pi}{2}}.

[image: [Uncaptioned image]]

Figure 10: R ​ e ​ c θ Rec_{\theta}

###### Claim 3.3.

In R ​ e ​ c θ Rec_{\theta}, ℳ θ \mathcal{M}_{\theta} is a pseudopath between A θ A_{\theta} and B θ B_{\theta}.

###### Proof.

Let π θ: ℝ 2 → ℝ \pi_{\theta}:\mathbb{R}^{2}\rightarrow\mathbb{R} be the projection ( x, y) → x ​ sin ⁡ θ − y ​ cos ⁡ θ (x,y)\rightarrow x\sin\theta-y\cos\theta.
Let f θ: [0, 1] 2 → ℝ f_{\theta}:[0,1]^{2}\rightarrow\mathbb{R} be the function ( r 1, r 2) → π θ ∘ γ θ ​ ( r 1) − π θ ∘ Γ θ ​ ( r 2) (r_{1},r_{2})\rightarrow\pi_{\theta}\circ\gamma_{\theta}(r_{1})-\pi_{\theta}\circ\Gamma_{\theta}(r_{2}).
Let g θ: [0, 1] 2 → ℝ 2 g_{\theta}:[0,1]^{2}\rightarrow\mathbb{R}^{2} be the function ( r 1, r 2) → mid-point of ​ γ θ ​ ( r 1) ​ and ​ Γ θ ​ ( r 2) (r_{1},r_{2})\rightarrow\text{mid-point of }\gamma_{\theta}(r_{1})\text{ and }\Gamma_{\theta}(r_{2}).
Clearly, π θ, f θ, g θ \pi_{\theta},f_{\theta},g_{\theta} are continuous as functions between topological spaces. Also, by definition, ℳ θ = g θ ​ ( f θ − 1 ​ ( 0)) \mathcal{M}_{\theta}=g_{\theta}(f_{\theta}^{-1}(0)).

Suppose α \alpha is a path in [0, 1] 2 [0,1]^{2} going from ( 0, 1) (0,1) to ( 1, 0) (1,0). Then f θ ∘ α f_{\theta}\circ\alpha is a path in ℝ \mathbb{R} going from a negative number to a positive number, hence must passes through 0 0. So i ​ m ​ ( α) ∩ f θ − 1 ​ ( 0) ≠ ∅ im(\alpha)\cap f_{\theta}^{-1}(0)\neq\varnothing.

As α \alpha is arbitrary, ( 0, 1) (0,1) and ( 1, 0) (1,0) are in different path components in [0, 1] 2 \ f θ − 1 ​ ( 0) [0,1]^{2}\backslash f_{\theta}^{-1}(0). By claim 3.1, f θ − 1 ​ ( 0) f_{\theta}^{-1}(0) only intersects ∂ [0, 1] 2 \partial[0,1]^{2} at ( 0, 0) (0,0) and ( 1, 1) (1,1). Also, f θ − 1 ​ ( 0) f_{\theta}^{-1}(0) is compact in [0, 1] 2 [0,1]^{2} because { 0 } \{0\} is closed in ℝ \mathbb{R} and [0, 1] 2 [0,1]^{2} itself is compact. So, by Lemma 2.3, f θ − 1 ​ ( 0) f_{\theta}^{-1}(0) is a pseudopath from ( 0, 0) (0,0) to ( 1, 1) (1,1). Then by Lemma 2.2, ℳ θ = g θ ​ ( f θ − 1 ​ ( 0)) \mathcal{M}_{\theta}=g_{\theta}(f_{\theta}^{-1}(0)) is a pseudopath between A θ A_{\theta} and B θ B_{\theta}. ∎

Now we will complete the proof of Proposition 1.6, which is the aim of Section 3. When γ \gamma has no special corners of angle θ \theta, A θ A_{\theta}, A θ + π 2 A_{\theta+\frac{\pi}{2}}, B θ B_{\theta}, B θ + π 2 B_{\theta+\frac{\pi}{2}} are all distinct. By Claim 3.3, ℳ θ \mathcal{M}_{\theta} is a pseudopath between A θ A_{\theta} and B θ B_{\theta}, and ℳ θ + π 2 \mathcal{M}_{\theta+\frac{\pi}{2}} is a pseudopath between A θ + π 2 A_{\theta+\frac{\pi}{2}} and B θ + π 2 B_{\theta+\frac{\pi}{2}}. By Lemma 2.4, ℳ θ ∩ ℳ θ + π 2 ≠ ∅ \mathcal{M}_{\theta}\cap\mathcal{M}_{\theta+\frac{\pi}{2}}\neq\varnothing.

By Claim 3.1 and Claim 3.2, ℳ θ \mathcal{M}_{\theta} only intersects ∂ R ​ e ​ c θ \partial Rec_{\theta} at A θ A_{\theta} and B θ B_{\theta}, and ℳ θ + π 2 \mathcal{M}_{\theta+\frac{\pi}{2}} only intersects ∂ R ​ e ​ c θ \partial Rec_{\theta} at A θ + π 2 A_{\theta}+\frac{\pi}{2} and B θ + π 2 B_{\theta}+\frac{\pi}{2}.

Hence, ℳ θ ∩ ℳ θ + π 2 ⊆ i ​ n ​ t ​ ( R ​ e ​ c θ) \mathcal{M}_{\theta}\cap\mathcal{M}_{\theta+\frac{\pi}{2}}\subseteq int(Rec_{\theta}). So, by Claim 3.2 and the definition of ℳ θ \mathcal{M}_{\theta} and ℳ θ + π 2 \mathcal{M}_{\theta+\frac{\pi}{2}}, intersection points of ℳ θ \mathcal{M}_{\theta} and ℳ θ + π 2 \mathcal{M}_{\theta+\frac{\pi}{2}} correspond to inscribed quadrilaterals with diagonals being lines of angle θ \theta and angle θ + π 2 \theta+\frac{\pi}{2}, i.e. inscribed rhombi of angle θ \theta. Since ℳ θ ∩ ℳ θ + π 2 ≠ ∅ \mathcal{M}_{\theta}\cap\mathcal{M}_{\theta+\frac{\pi}{2}}\neq\varnothing, there exists an inscribed rhombus of angle θ \theta.

## 4. Proof of Proposition 1.8

This section is entirely devoted to the proof of Proposition 1.8.

Let γ \gamma be a Jordan curve in ℝ 2 \mathbb{R}^{2} with at least two special corners. Let p, q p,q be distinct special corners of γ \gamma. Without loss of generality, using suitable rotations and translations, we can let p p be the origin of ℝ 2 \mathbb{R}^{2} and let q q be lying in the positive x x -axis. What we need to prove is that ∃ ϵ > 0 \exists\epsilon>0 ∀ θ ∈ ( − ϵ, ϵ) \forall\theta\in(-\epsilon,\epsilon) ∃ \exists an inscribed rhombus of angle θ \theta. By symmetry, we can replace ( − ϵ, ϵ) (-\epsilon,\epsilon) by [0, ϵ) [0,\epsilon).

Let p p be a special corner of angle θ p \theta_{p}, where θ p ∈ [0, π 2) \theta_{p}\in[0,\frac{\pi}{2}). Actually, θ p \theta_{p} cannot be 0 0 because q q is in i ​ m ​ ( γ) im(\gamma).
(Note that the choice of θ p \theta_{p} may not necessarily be unique)

Similarly, let q q be a special corner of angle θ q \theta_{q}, with q ∈ ( 0, π 2) q\in(0,\frac{\pi}{2}). Then i ​ m ​ ( γ) im(\gamma) is inside the following region, touching the boundary only at p p and q q:

[image: [Uncaptioned image]]

Figure 11: A region where i ​ m ​ ( γ) im(\gamma) must lie within

It is impossible for all points on a Jordan curve to be collinear. So, A 0 A_{0} and B 0 B_{0} cannot both lie on the x x -axis. Without loss of generality (by reflecting along the x x -axis if necessary), let A 0 A_{0} be lying strictly above the x x -axis. Let ϵ A \epsilon_{A} be the angle ∠ ​ q ​ p ​ A 0 \angle qpA_{0}. i.e. the line going through the origin and A 0 A_{0} has angle ϵ A ∈ ( 0, θ p) \epsilon_{A}\in(0,\theta_{p}). Let ϵ B \epsilon_{B} be the angle ∠ ​ B 0 ​ q ​ p \angle B_{0}qp. i.e. the line going through B 0 B_{0} and q q has angle ϵ B ∈ [0, θ q) \epsilon_{B}\in[0,\theta_{q}).

Now we will split it into two cases. Case 1 is when ϵ B > 0 \epsilon_{B}>0, i.e. parts of the Jordan curve lies below the x x -axis. Case 2 is when ϵ B = 0 \epsilon_{B}=0, i.e. the entire Jordan curve lies on or above the x x -axis.

Case 1: When ϵ B > 0 \epsilon_{B}>0.
Let ϵ:= m ​ i ​ n ​ ( ϵ A, ϵ B) \epsilon:=min(\epsilon_{A},\epsilon_{B}). Then ∀ θ ∈ [0, ϵ) \forall\theta\in[0,\epsilon), A θ + π 2 = p A_{\theta+\frac{\pi}{2}}=p (because θ < θ p \theta<\theta_{p}) and B θ + π 2 = q B_{\theta+\frac{\pi}{2}}=q (because θ < θ q \theta<\theta_{q}). Also, A θ A_{\theta} is strictly above the line y = x ​ tan ⁡ θ y=x\tan\theta (because θ < ϵ A \theta<\epsilon_{A}) and B θ B_{\theta} is strictly below the line of angle θ \theta passing through q q (because θ < ϵ B \theta<\epsilon_{B}). So, A θ + π 2 A_{\theta+\frac{\pi}{2}}, B θ + π 2 = q B_{\theta+\frac{\pi}{2}}=q, A θ A_{\theta}, B θ B_{\theta} are all distinct, and the argument in Section 3 still goes through. Hence, there exists an inscribed rhombus of angle θ \theta.

[image: [Uncaptioned image]]

Figure 12: When B θ B_{\theta} is strictly below the x x -axis

Case 2: When ϵ B = 0 \epsilon_{B}=0.

Recall that Γ π 2: [0, 1] → ℝ 2 \Gamma_{\frac{\pi}{2}}:[0,1]\rightarrow\mathbb{R}^{2} is a path from p = M ​ m π 2 p=Mm_{\frac{\pi}{2}} to q = M ​ M π 2 q=MM_{\frac{\pi}{2}}. Γ π 2 \Gamma_{\frac{\pi}{2}} is the path “above” and γ π 2 \gamma_{\frac{\pi}{2}} is the path “below”. (precise definition is in Section 3)

Let w w be the x x -coordinate of q q (the width of R ​ e ​ c 0 Rec_{0}), and h h be the y y -coordinate of A 0 A_{0} (the height of R ​ e ​ c 0 Rec_{0}).
Let ϵ l:= m ​ i ​ n ​ { x ​ -coordinate of ​ Γ π 2 ​ ( r) ∣ r ∈ [Γ π 2 − 1 ​ ( M ​ m ϵ A), 1] } \epsilon_{l}:=min\{x\text{-coordinate of }\Gamma_{\frac{\pi}{2}}(r)\mid r\in[\Gamma_{\frac{\pi}{2}}^{-1}(Mm_{\epsilon_{A}}),1]\}.
Let ϵ r:= m ​ i ​ n ​ { w − ( x ​ -coordinate of ​ Γ π 2 ​ ( r)) ∣ r ∈ [0, Γ π 2 − 1 ​ ( m ​ m 0)] } \epsilon_{r}:=min\{w-(x\text{-coordinate of }\Gamma_{\frac{\pi}{2}}(r))\mid r\in[0,\Gamma_{\frac{\pi}{2}}^{-1}(mm_{0})]\}.

Note that ϵ l \epsilon_{l} and ϵ r \epsilon_{r} exist because of compactness.

[image: [Uncaptioned image]]

Figure 13: Definition of ϵ l \epsilon_{l} and ϵ r \epsilon_{r}

Let ϵ y:= m ​ i ​ n ​ { y ∣ ( x, y) ∈ i ​ m ​ ( Γ π 2) ​ and ​ ϵ l 8 ≤ x ≤ w − ϵ r 8 } \epsilon_{y}:=min\{y\mid(x,y)\in im(\Gamma_{\frac{\pi}{2}})\text{ and }\frac{\epsilon_{l}}{8}\leq x\leq w-\frac{\epsilon_{r}}{8}\}. Note that ϵ y > 0 \epsilon_{y}>0 because i ​ m ​ ( Γ π 2) im(\Gamma_{\frac{\pi}{2}}) only intersects the x x -axis at p p and q q.

[image: [Uncaptioned image]]

Figure 14: Definition of ϵ y \epsilon_{y}

We pick ϵ > 0 \epsilon>0 small enough such that

 | tan ⁡ ϵ < ϵ l 8 ​ h, ϵ r 8 ​ h, ϵ y 2 ​ w \tan\epsilon<\frac{\epsilon_{l}}{8h},\frac{\epsilon_{r}}{8h},\frac{\epsilon_{y}}{2w} |  |

and

 | ϵ < ϵ A, θ p, θ q \epsilon<\epsilon_{A},\theta_{p},\theta_{q} |  |

We want to show that ∀ θ ∈ [0, ϵ) \forall\theta\in[0,\epsilon), there exists an inscribed rhombus of angle θ \theta. We first work on the θ = 0 \theta=0 case.

The point A 0 A_{0} is strictly above the x x -axis. Also, A π 2 = p = ( 0, 0) A_{\frac{\pi}{2}}=p=(0,0), B 0 = ( w 2, 0) B_{0}=(\frac{w}{2},0), and B π 2 = q = ( w, 0) B_{\frac{\pi}{2}}=q=(w,0). Those 4 points are distinct, and hence the argument from Section 3 still goes through, and hence an inscribed rhombus of angle 0 0 exists.

We proceed with the 0 < θ < ϵ 0<\theta<\epsilon case.

Let R R be the region { ( x, y) ∣ ϵ l 4 ≤ x ≤ w − ϵ r 4 ​ and ​ m θ ≤ x ​ sin ⁡ θ − y ​ cos ⁡ θ ≤ 0 } \{(x,y)\mid\frac{\epsilon_{l}}{4}\leq x\leq w-\frac{\epsilon_{r}}{4}\text{ and }m_{\theta}\leq x\sin\theta-y\cos\theta\leq 0\} Note that ∂ R \partial R is a parallelogram with two sides being vertical and two sides being line segments of angle θ \theta.

[image: [Uncaptioned image]]

Figure 15: The region R R

We use a similar argument as the one used in Section 3. But instead of applying Lemma 2.4 to R ​ e ​ c θ Rec_{\theta}, we will apply it to R R.

###### Claim 4.1.

If 0 ≤ θ 1 < θ 2 < π 2 0\leq\theta_{1}<\theta_{2}<\frac{\pi}{2}, then

 | Γ π 2 − 1 ​ ( m ​ m θ 2) ≤ Γ π 2 − 1 ​ ( M ​ m θ 2) ≤ Γ π 2 − 1 ​ ( m ​ m θ 1) ≤ Γ π 2 − 1 ​ ( M ​ m θ 1) \Gamma_{\frac{\pi}{2}}^{-1}(mm_{\theta_{2}})\leq\Gamma_{\frac{\pi}{2}}^{-1}(Mm_{\theta_{2}})\leq\Gamma_{\frac{\pi}{2}}^{-1}(mm_{\theta_{1}})\leq\Gamma_{\frac{\pi}{2}}^{-1}(Mm_{\theta_{1}}) |  |

###### Proof.

We first prove that Γ π 2 − 1 ​ ( m ​ m θ 2) ≤ Γ π 2 − 1 ​ ( M ​ m θ 2) \Gamma_{\frac{\pi}{2}}^{-1}(mm_{\theta_{2}})\leq\Gamma_{\frac{\pi}{2}}^{-1}(Mm_{\theta_{2}}). We will prove it by contradiction.

Suppose Γ π 2 − 1 ​ ( m ​ m θ 2) > Γ π 2 − 1 ​ ( M ​ m θ 2) \Gamma_{\frac{\pi}{2}}^{-1}(mm_{\theta_{2}})>\Gamma_{\frac{\pi}{2}}^{-1}(Mm_{\theta_{2}}).
Let T θ 2:= { ( x, y) ∣ 0 ≤ x ≤ w and y ≥ 0 and x sin θ 2 − y cos θ 2 ≥ m θ 2 } T_{\theta_{2}}:=\{(x,y)\mid 0\leq x\leq w\text{ and }y\geq 0\text{ and }x\sin\theta_{2}-y\cos\theta_{2}\geq m_{\theta_{2}}\}.
Then Γ π 2 | [0, Γ π 2 − 1 ​ ( M ​ m θ 2)] \Gamma_{\frac{\pi}{2}}|_{[0,\Gamma_{\frac{\pi}{2}}^{-1}(Mm_{\theta_{2}})]} is a path in T θ 2 ≅ 𝔻 2 T_{\theta_{2}}\cong\mathbb{D}^{2} going from p p to M ​ m θ 2 Mm_{\theta_{2}}, and Γ π 2 | [Γ π 2 − 1 ​ ( m ​ m θ 2), 1] \Gamma_{\frac{\pi}{2}}|_{[\Gamma_{\frac{\pi}{2}}^{-1}(mm_{\theta_{2}}),1]} is a path in T θ 2 T_{\theta_{2}} going from m ​ m θ 2 mm_{\theta_{2}} to q q. However, Γ π 2 | [0, Γ π 2 − 1 ​ ( M ​ m θ 2)] \Gamma_{\frac{\pi}{2}}|_{[0,\Gamma_{\frac{\pi}{2}}^{-1}(Mm_{\theta_{2}})]} and Γ π 2 | [Γ π 2 − 1 ​ ( m ​ m θ 2), 1] \Gamma_{\frac{\pi}{2}}|_{[\Gamma_{\frac{\pi}{2}}^{-1}(mm_{\theta_{2}}),1]} do not intersect, which is impossible.

[image: [Uncaptioned image]]

Figure 16: T θ 2 T_{\theta_{2}}

Therefore, we must have Γ π 2 − 1 ​ ( m ​ m θ 2) ≤ Γ π 2 − 1 ​ ( M ​ m θ 2) \Gamma_{\frac{\pi}{2}}^{-1}(mm_{\theta_{2}})\leq\Gamma_{\frac{\pi}{2}}^{-1}(Mm_{\theta_{2}}).

Similarly, we have Γ π 2 − 1 ​ ( m ​ m θ 1) ≤ Γ π 2 − 1 ​ ( M ​ m θ 1) \Gamma_{\frac{\pi}{2}}^{-1}(mm_{\theta_{1}})\leq\Gamma_{\frac{\pi}{2}}^{-1}(Mm_{\theta_{1}}), and we also have Γ π 2 − 1 ​ ( M ​ m θ 2) ≤ Γ π 2 − 1 ​ ( m ​ m θ 1) \Gamma_{\frac{\pi}{2}}^{-1}(Mm_{\theta_{2}})\leq\Gamma_{\frac{\pi}{2}}^{-1}(mm_{\theta_{1}}) by considering the diagram below.

[image: [Uncaptioned image]]

Figure 17: m ​ m θ 1 mm_{\theta_{1}} and M ​ m θ 2 Mm_{\theta_{2}}

∎

###### Claim 4.2.

All points in { ( x, y) ∈ ℳ θ + π 2 ∣ ϵ l 4 ≤ x ≤ w − ϵ r 4 } \{(x,y)\in\mathcal{M}_{\theta+\frac{\pi}{2}}\mid\frac{\epsilon_{l}}{4}\leq x\leq w-\frac{\epsilon_{r}}{4}\} lie strictly above the line y = x ​ tan ⁡ θ y=x\tan\theta.

###### Proof.

Let ( x, y) ∈ { ( x, y) ∈ ℳ θ + π 2 ∣ ϵ l 4 ≤ x ≤ w − ϵ r 4 } (x,y)\in\{(x,y)\in\mathcal{M}_{\theta+\frac{\pi}{2}}\mid\frac{\epsilon_{l}}{4}\leq x\leq w-\frac{\epsilon_{r}}{4}\}. We want to show that y > x ​ tan ⁡ θ y>x\tan\theta. Since ( x, y) ∈ ℳ θ + π 2 (x,y)\in\mathcal{M}_{\theta+\frac{\pi}{2}}, we have x = x 1 + x 2 2 x=\frac{x_{1}+x_{2}}{2} and y = y 1 + y 2 2 y=\frac{y_{1}+y_{2}}{2} for some ( x 1, y 1) ∈ i ​ m ​ ( γ θ + π 2) (x_{1},y_{1})\in im(\gamma_{\theta+\frac{\pi}{2}}) and ( x 2, y 2) ∈ i ​ m ​ ( Γ θ + π 2) (x_{2},y_{2})\in im(\Gamma_{\theta+\frac{\pi}{2}}), with ( x 1, y 1), ( x, y), ( x 2, y 2) (x_{1},y_{1}),(x,y),(x_{2},y_{2}) lying on a line of angle θ + π 2 \theta+\frac{\pi}{2}. Then we have

 | | x 2 − x | = | y 2 − y | | tan ⁡ ( θ + π 2) | = | y 2 − y 0 | ​ tan ⁡ θ |x_{2}-x|=\dfrac{|y_{2}-y|}{|\tan(\theta+\frac{\pi}{2})|}=|y_{2}-y_{0}|\tan\theta |  |

By the definition of h h, we must have | y 2 − y | ≤ h |y_{2}-y|\leq h. So we have

 | | x 2 − x | ≤ h ​ tan ⁡ θ < h ​ tan ⁡ ϵ < m ​ i ​ n ​ ( ϵ l 8, ϵ r 8) |x_{2}-x|\leq h\tan\theta<h\tan\epsilon<min(\dfrac{\epsilon_{l}}{8},\dfrac{\epsilon_{r}}{8}) |  |

(the last inequality comes from the definition of ϵ \epsilon)

Since ϵ l 4 ≤ x ≤ w − ϵ r 4 \frac{\epsilon_{l}}{4}\leq x\leq w-\frac{\epsilon_{r}}{4} and | x 2 − x | < m ​ i ​ n ​ ( ϵ l 8, ϵ r 8) |x_{2}-x|<min(\dfrac{\epsilon_{l}}{8},\dfrac{\epsilon_{r}}{8}), we must have ϵ l 8 ≤ x 2 ≤ w − ϵ r 8 \frac{\epsilon_{l}}{8}\leq x_{2}\leq w-\frac{\epsilon_{r}}{8}. Hence, by the definition of ϵ y \epsilon_{y}, we must have y 2 ≥ ϵ y y_{2}\geq\epsilon_{y}. So we have

 | y = y 1 + y 2 2 ≥ y 2 2 ≥ ϵ y 2 > w ​ tan ⁡ ϵ ≥ x ​ tan ⁡ θ y=\frac{y_{1}+y_{2}}{2}\geq\frac{y_{2}}{2}\geq\frac{\epsilon_{y}}{2}>w\tan\epsilon\geq x\tan\theta |  |

∎

Intuitively, Claim 4.2 states that the pseudopath ℳ θ + π 2 \mathcal{M}_{\theta+\frac{\pi}{2}} has to pass through the region R R. We make it precise in the next claim.

Let Z S ​ W:= ( ϵ l 4, ϵ l 4 ​ tan ⁡ θ) Z_{SW}:=(\frac{\epsilon_{l}}{4},\frac{\epsilon_{l}}{4}\tan\theta), Z S ​ E:= ( w − ϵ l 4, ( w − ϵ l 4) ​ tan ⁡ θ) Z_{SE}:=(w-\frac{\epsilon_{l}}{4},(w-\frac{\epsilon_{l}}{4})\tan\theta) be the two bottom corners of R R. Let Z W:= { ( ϵ l 4, y) ∣ m θ ≤ ϵ l 4 ​ sin ⁡ θ − y ​ cos ⁡ θ ≤ 0 } Z_{W}:=\{(\frac{\epsilon_{l}}{4},y)\mid m_{\theta}\leq\frac{\epsilon_{l}}{4}\sin\theta-y\cos\theta\leq 0\} be the left vertical edge of R R, and let Z E:= { ( w − ϵ r 4, y) ∣ m θ ≤ ( w − ϵ r 4) ​ sin ⁡ θ − y ​ cos ⁡ θ ≤ 0 } Z_{E}:=\{(w-\frac{\epsilon_{r}}{4},y)\mid m_{\theta}\leq(w-\frac{\epsilon_{r}}{4})\sin\theta-y\cos\theta\leq 0\} be the right vertical edge of R R.

[image: [Uncaptioned image]]

Figure 18: The shaded region is R R. Showing Z S ​ W Z_{SW}, Z S ​ E Z_{SE}, Z W Z_{W}, Z E Z_{E}.

Let ℳ θ + π 2 R:= Z W ∪ Z E ∪ { ( x, y) ∈ ℳ θ + π 2 ∣ ϵ l 4 ≤ x ≤ w − ϵ r 4 } \mathcal{M}_{\theta+\frac{\pi}{2}}^{R}:=Z_{W}\cup Z_{E}\cup\{(x,y)\in\mathcal{M}_{\theta+\frac{\pi}{2}}\mid\frac{\epsilon_{l}}{4}\leq x\leq w-\frac{\epsilon_{r}}{4}\}. By Claim 4.2, we know that ℳ θ + π 2 R ⊆ R \mathcal{M}_{\theta+\frac{\pi}{2}}^{R}\subseteq R.

###### Claim 4.3.

In R R, ℳ θ + π 2 R \mathcal{M}_{\theta+\frac{\pi}{2}}^{R} is a pseudopath between Z S ​ W Z_{SW} and Z S ​ E Z_{SE}.

###### Proof.

Let U U be an open set in R R and ℳ θ + π 2 R ⊆ U \mathcal{M}_{\theta+\frac{\pi}{2}}^{R}\subseteq U. We want to show that there exists a path inside U U going from Z S ​ W Z_{SW} to Z S ​ E Z_{SE}. Since U U is open in R R, U = U ′ ∩ R U=U^{{}^{\prime}}\cap R for some U ′ U^{{}^{\prime}} open in R ​ e ​ c θ Rec_{\theta}.

Let U ′′:= U ′ \ { ( x, y) ∣ ϵ l 4 ≤ x ≤ w − ϵ r 4 and y ≤ x tan θ } U^{{}^{\prime\prime}}:=U^{{}^{\prime}}\backslash\{(x,y)\mid\frac{\epsilon_{l}}{4}\leq x\leq w-\frac{\epsilon_{r}}{4}\text{ and }y\leq x\tan\theta\}. Then U ′′ U^{{}^{\prime\prime}} is still open, and ( ℳ θ + π 2 R \ { Z S ​ W, Z S ​ E }) ⊆ U ′′ (\mathcal{M}_{\theta+\frac{\pi}{2}}^{R}\backslash\{Z_{SW},Z_{SE}\})\subseteq U^{{}^{\prime\prime}}. By Claim 4.2, the set { ( x, y) ∣ ϵ l 4 ≤ x ≤ w − ϵ r 4 ​ and ​ y ≤ x ​ tan ⁡ θ } \{(x,y)\mid\frac{\epsilon_{l}}{4}\leq x\leq w-\frac{\epsilon_{r}}{4}\text{ and }y\leq x\tan\theta\} we removed does not contain any points from ℳ θ + π 2 \mathcal{M}_{\theta+\frac{\pi}{2}}.

Let U ′ ′ ′:= U ′′ ∪ { ( x, y) ∈ R e c θ ∣ x < ϵ l 4 or w − ϵ r 4 < x } U^{{}^{\prime\prime\prime}}:=U^{{}^{\prime\prime}}\cup\{(x,y)\in Rec_{\theta}\mid x<\frac{\epsilon_{l}}{4}\text{ or }w-\frac{\epsilon_{r}}{4}<x\}. Then U ′ ′ ′ U^{{}^{\prime\prime\prime}} is an open set, and we have ℳ θ + π 2 ⊆ U ′ ′ ′ \mathcal{M}_{\theta+\frac{\pi}{2}}\subseteq U^{{}^{\prime\prime\prime}}. Also, by construction, we have ( U \ { Z S ​ W, Z S ​ E }) ⊆ U ′ ′ ′ (U\backslash\{Z_{SW},Z_{SE}\})\subseteq U^{{}^{\prime\prime\prime}}. By Claim 3.3, there exists a path α: [0, 1] → U ′ ′ ′ \alpha:[0,1]\rightarrow U^{{}^{\prime\prime\prime}} going from p p to q q. Since U ′ ′ ′ U^{{}^{\prime\prime\prime}} does not contain any points from { ( x, y) ∣ ϵ l 4 ≤ x ≤ w − ϵ r 4 ​ and ​ y ≤ x ​ tan ⁡ θ } \{(x,y)\mid\frac{\epsilon_{l}}{4}\leq x\leq w-\frac{\epsilon_{r}}{4}\text{ and }y\leq x\tan\theta\}, α \alpha must intersect Z W Z_{W} and Z E Z_{E}.

Let a 0:= m ​ a ​ x ​ { t ∈ [0, 1] ∣ α ⁡ ( t) ∈ Z W } a_{0}:=max\{t\in[0,1]\mid\alpha(t)\in Z_{W}\} and a 1:= m ​ i ​ n ​ { t ∈ [a 0, 1] ∣ α ⁡ ( t) ∈ Z E } a_{1}:=min\{t\in[a_{0},1]\mid\alpha(t)\in Z_{E}\}. Then α | [a 0, a 1] \alpha|_{[a_{0},a_{1}]} is a path in R R going from α ⁡ ( a 0) \alpha(a_{0}) to α ⁡ ( a 1) \alpha(a_{1}). Concatenating α | [a 0, a 1] \alpha|_{[a_{0},a_{1}]} with a path inside Z W Z_{W} going from Z S ​ W Z_{SW} to α ⁡ ( a 0) \alpha(a_{0}) and a path inside Z E Z_{E} going from α ⁡ ( a 1) \alpha(a_{1}) to Z S ​ E Z_{SE}, we get a path inside U U going from Z S ​ W Z_{SW} to Z S ​ E Z_{SE}.

[image: [Uncaptioned image]]

Figure 19: Construction of a path inside U U going from Z S ​ W Z_{SW} to Z S ​ E Z_{SE}

∎

We have finished proving Claim 4.3, which is an analogue of Claim 3.3 for ℳ θ + π 2 \mathcal{M}_{\theta+\frac{\pi}{2}} in R R. Now we work on an analogue of Claim 3.3 for ℳ θ \mathcal{M}_{\theta} in R R.

Let L L be the line segment { ( x, y) ∣ 0 ≤ x ≤ w ​ and ​ y = x ​ tan ⁡ θ } \{(x,y)\mid 0\leq x\leq w\text{ and }y=x\tan\theta\}.
Let L l L_{l} be the line segment { ( x, y) ∈ L ∣ x ≤ ϵ l 8 } \{(x,y)\in L\mid x\leq\frac{\epsilon_{l}}{8}\}, and L r L_{r} be the line segment { ( x, y) ∈ L ∣ w − ϵ r 8 ≤ x } \{(x,y)\in L\mid w-\frac{\epsilon_{r}}{8}\leq x\}.

Consider the set of points S:= { ( x, y) ∈ i ​ m ​ ( Γ π 2) ∣ ϵ l 8 ≤ x ≤ w − ϵ r 8 } S:=\{(x,y)\in im(\Gamma_{\frac{\pi}{2}})\mid\frac{\epsilon_{l}}{8}\leq x\leq w-\frac{\epsilon_{r}}{8}\}. By the definition of ϵ y \epsilon_{y}, whenever ( x, y) ∈ S (x,y)\in S, we have must have

 | y ≥ ϵ y > 2 ​ w ​ tan ⁡ ϵ > w ​ tan ⁡ ϵ > x ​ tan ⁡ θ y\geq\epsilon_{y}>2w\tan\epsilon>w\tan\epsilon>x\tan\theta |  |

So all points in S S lie strictly above L.

Let t l:= m ​ a ​ x ​ { t ∈ [0, 1] ∣ Γ π 2 ​ ( t) ∈ L l } t_{l}:=max\{t\in[0,1]\mid\Gamma_{\frac{\pi}{2}}(t)\in L_{l}\}. Note that t l t_{l} exists because of compactness and the fact that p ∈ L l p\in L_{l}. Let t r:= m ​ i ​ n ​ { t ∈ [t l, 1] ∣ Γ π 2 ​ ( t) ∈ L r } t_{r}:=min\{t\in[t_{l},1]\mid\Gamma_{\frac{\pi}{2}}(t)\in L_{r}\}. Note that t r t_{r} exists because q q is below L L and all points in S S are above L L. By construction, all points in i ​ m ​ ( Γ π 2 | ( t l, t r)) im(\Gamma_{\frac{\pi}{2}}|_{(t_{l},t_{r})}) lie strictly above L L.

Let γ ¯ \overline{\gamma} be a Jordan curve formed by concatenating Γ π 2 | [t l, t r] \Gamma_{\frac{\pi}{2}}|_{[t_{l},t_{r}]} with a path in L L going from Γ π 2 ​ ( t r) \Gamma_{\frac{\pi}{2}}(t_{r}) to Γ π 2 ​ ( t l) \Gamma_{\frac{\pi}{2}}(t_{l}).

[image: [Uncaptioned image]]

Figure 20: Construction of γ ¯ \overline{\gamma}

For every mathematical object we have constructed from γ \gamma, we add a bar on top to denote the same object constructed from γ ¯ \overline{\gamma} instead of γ \gamma.

Note that M θ ¯ = 0 \overline{M_{\theta}}=0 because i ​ m ​ ( γ ¯) im(\overline{\gamma}) does not go below L L. So, m ​ M θ ¯ = Γ π 2 ​ ( t l) \overline{mM_{\theta}}=\Gamma_{\frac{\pi}{2}}(t_{l}) and M ​ M θ ¯ = Γ π 2 ​ ( t r) \overline{MM_{\theta}}=\Gamma_{\frac{\pi}{2}}(t_{r}). Now we consider m ​ m θ ¯ \overline{mm_{\theta}} and M ​ m θ ¯ \overline{Mm_{\theta}}. Since the x x -coordinate of Γ π 2 ​ ( t l) \Gamma_{\frac{\pi}{2}}(t_{l}) is less than ϵ l \epsilon_{l} and the x x -coordinate of Γ π 2 ​ ( t r) \Gamma_{\frac{\pi}{2}}(t_{r}) is larger than ϵ r \epsilon_{r}, by the definition of ϵ l \epsilon_{l} and ϵ r \epsilon_{r}, we must have t l < Γ π 2 − 1 ​ ( M ​ m ϵ A) t_{l}<\Gamma_{\frac{\pi}{2}}^{-1}(Mm_{\epsilon_{A}}) and Γ π 2 − 1 ​ ( m ​ m 0) < t r \Gamma_{\frac{\pi}{2}}^{-1}(mm_{0})<t_{r}.

By Claim 4.1, we have

 | Γ π 2 − 1 ​ ( M ​ m ϵ A) ≤ Γ π 2 − 1 ​ ( m ​ m θ) ≤ Γ π 2 − 1 ​ ( M ​ m θ) ≤ Γ π 2 − 1 ​ ( m ​ m 0) \Gamma_{\frac{\pi}{2}}^{-1}(Mm_{\epsilon_{A}})\leq\Gamma_{\frac{\pi}{2}}^{-1}(mm_{\theta})\leq\Gamma_{\frac{\pi}{2}}^{-1}(Mm_{\theta})\leq\Gamma_{\frac{\pi}{2}}^{-1}(mm_{0}) |  |

Hence, we have t l < Γ π 2 − 1 ​ ( m ​ m θ) ≤ Γ π 2 − 1 ​ ( M ​ m θ) < t r t_{l}<\Gamma_{\frac{\pi}{2}}^{-1}(mm_{\theta})\leq\Gamma_{\frac{\pi}{2}}^{-1}(Mm_{\theta})<t_{r}. So, m ​ m θ mm_{\theta} and M ​ m θ Mm_{\theta} are in i ​ m ​ ( γ ¯) im(\overline{\gamma}), and hence m ​ m θ ¯ = m ​ m θ \overline{mm_{\theta}}=mm_{\theta} and M ​ m θ ¯ = M ​ m θ \overline{Mm_{\theta}}=Mm_{\theta}. Therefore, A θ ¯ = A θ \overline{A_{\theta}}=A_{\theta}.

Let Z S:= B θ ¯ = Z_{S}:=\overline{B_{\theta}}= mid-point of Γ π 2 ​ ( t l) \Gamma_{\frac{\pi}{2}}(t_{l}) and Γ π 2 ​ ( t r) \Gamma_{\frac{\pi}{2}}(t_{r}), and let Z N:= A θ ¯ = A θ Z_{N}:=\overline{A_{\theta}}=A_{\theta}. By Claim 3.3, in R ​ e ​ c θ ¯ \overline{Rec_{\theta}}, ℳ θ ¯ \overline{\mathcal{M}_{\theta}} is a pseudopath between Z S Z_{S} and Z N Z_{N}.

[image: [Uncaptioned image]]

Figure 21: The shaded region is R R. Showing Z S ​ W Z_{SW}, Z S ​ E Z_{SE}, Z N Z_{N}, Z S Z_{S}.

###### Claim 4.4.

All points in ℳ θ ¯ \overline{\mathcal{M}_{\theta}} have x x -coordinate strictly between ϵ l 4 \frac{\epsilon_{l}}{4} and w − ϵ r 4 w-\frac{\epsilon_{r}}{4}.

###### Proof.

Recall that by Claim 4.1, we have

 | Γ π 2 − 1 ​ ( M ​ m ϵ A) ≤ Γ π 2 − 1 ​ ( m ​ m θ) ≤ Γ π 2 − 1 ​ ( M ​ m θ) ≤ Γ π 2 − 1 ​ ( m ​ m 0) \Gamma_{\frac{\pi}{2}}^{-1}(Mm_{\epsilon_{A}})\leq\Gamma_{\frac{\pi}{2}}^{-1}(mm_{\theta})\leq\Gamma_{\frac{\pi}{2}}^{-1}(Mm_{\theta})\leq\Gamma_{\frac{\pi}{2}}^{-1}(mm_{0}) |  |

So, we have

 | i ​ m ​ ( γ θ ¯) = i ​ m ​ ( Γ π 2 | [t l, Γ π 2 − 1 ​ ( m ​ m θ ¯)]) = i ​ m ​ ( Γ π 2 | [t l, Γ π 2 − 1 ​ ( m ​ m θ)]) ⊆ i ​ m ​ ( Γ π 2 | [0, Γ π 2 − 1 ​ ( m ​ m 0)]) im(\overline{\gamma_{\theta}})=im(\Gamma_{\frac{\pi}{2}}|_{[t_{l},\Gamma_{\frac{\pi}{2}}^{-1}(\overline{mm_{\theta}})]})=im(\Gamma_{\frac{\pi}{2}}|_{[t_{l},\Gamma_{\frac{\pi}{2}}^{-1}(mm_{\theta})]})\subseteq im(\Gamma_{\frac{\pi}{2}}|_{[0,\Gamma_{\frac{\pi}{2}}^{-1}(mm_{0})]}) |  |

So, using the definition of ϵ r \epsilon_{r}, we know that all points in i ​ m ​ ( γ θ ¯) im(\overline{\gamma_{\theta}}) have x x -coordinate less than or equal to w − ϵ r w-\epsilon_{r}. Hence, by the definition of ℳ θ ¯ \overline{\mathcal{M}_{\theta}}, all points in ℳ θ ¯ \overline{\mathcal{M}_{\theta}} have x x -coordinate less than or equal to ( w − ϵ r) + w 2 = w − ϵ r 2 < w − ϵ r 4 \frac{(w-\epsilon_{r})+w}{2}=w-\frac{\epsilon_{r}}{2}<w-\frac{\epsilon_{r}}{4}.

Similarly,

 | i m ( Γ θ ¯) = i m ( Γ π 2 | [Γ π 2 − 1 ( [M ​ m θ ¯), t r]) = i m ( Γ π 2 | [Γ π 2 − 1 ( [M m θ), t r]) ⊆ i m ( Γ π 2 | [Γ π 2 − 1 ​ ( M ​ m ϵ A), 1]) im(\overline{\Gamma_{\theta}})=im(\Gamma_{\frac{\pi}{2}}|_{[\Gamma_{\frac{\pi}{2}}^{-1}([\overline{Mm_{\theta}}),t_{r}]})=im(\Gamma_{\frac{\pi}{2}}|_{[\Gamma_{\frac{\pi}{2}}^{-1}([Mm_{\theta}),t_{r}]})\subseteq im(\Gamma_{\frac{\pi}{2}}|_{[\Gamma_{\frac{\pi}{2}}^{-1}(Mm_{\epsilon_{A}}),1]}) |  |

Hence, all points in i ​ m ​ ( Γ θ ¯) im(\overline{\Gamma_{\theta}}) have x x -coordinate greater than or equal to ϵ l \epsilon_{l}, and hence all points in ℳ θ ¯ \overline{\mathcal{M}_{\theta}} have x x -coordinate greater than or equal to ϵ l + 0 2 = ϵ l 2 > ϵ l 4 \frac{\epsilon_{l}+0}{2}=\frac{\epsilon_{l}}{2}>\frac{\epsilon_{l}}{4}. ∎

We have proved Claim 4.4. We now complete the remaining of the proof of Proposition 1.8.

Lemma 3.3 and Claim 4.4 imply that in R R, ℳ θ ¯ \overline{\mathcal{M}_{\theta}} is a pseudopath between Z N Z_{N} and Z S Z_{S}. Together with Claim 4.3 and Lemma 2.4, we know that ℳ θ ¯ \overline{\mathcal{M}_{\theta}} and ℳ θ + π 2 R \mathcal{M}_{\theta+\frac{\pi}{2}}^{R} must intersect inside R R.

By Claim 4.4, ℳ θ ¯ \overline{\mathcal{M}_{\theta}} does not touch Z W Z_{W} nor Z E Z_{E}. Hence, ℳ θ ¯ \overline{\mathcal{M}_{\theta}} and ℳ θ + π 2 \mathcal{M}_{\theta+\frac{\pi}{2}} must intersect inside R R. By Claim 4.2, ℳ θ + π 2 \mathcal{M}_{\theta+\frac{\pi}{2}} does not touch the bottom edge of R R. Note that ℳ θ + π 2 \mathcal{M}_{\theta+\frac{\pi}{2}} also does not touch the top edge of R R because each point in ℳ θ + π 2 \mathcal{M}_{\theta+\frac{\pi}{2}} is the mid-point of a point in Γ θ + π 2 \Gamma_{\theta+\frac{\pi}{2}} (which cannot be above the top edge of R R because of the definition of m θ m_{\theta}) and a point in γ θ + π 2 \gamma_{\theta+\frac{\pi}{2}} (which is strictly below the top edge of R R). Hence, ℳ θ ¯ \overline{\mathcal{M}_{\theta}} and ℳ θ + π 2 \mathcal{M}_{\theta+\frac{\pi}{2}} must intersect inside the interior of R R. Let Z Z be such an intersection.

The point Z Z corresponds to a rhombus with diagonals being a line of angle θ \theta and a line of angle θ + π 2 \theta+\frac{\pi}{2}. The two vertices that correspond to the diagonal of angle θ \theta lie in i ​ m ​ ( γ ¯) im(\overline{\gamma}), and they are distinct because Z Z does not lie in the top edge of R R. In fact, those two vertices lie in i ​ m ​ ( γ) im(\gamma) because Z Z does not lie in L L. The two vertices that correspond to the diagonal of angle θ + π 2 \theta+\frac{\pi}{2} lie in i ​ m ​ ( γ) im(\gamma), and they are distinct because p, q ∉ R p,q\notin R.

Hence, Z Z corresponds to an inscribed rhombus of γ \gamma of angle θ \theta.

## 5. Discussion

We offer some speculation on how one may use the ideas of this paper towards the original inscribed square problem. One possibility would be to prove that an inscribed rhombus of angle θ \theta always exist even for those θ \theta having special corners and not covered in Proposition 1.8. The existence of such a rhombus seems intuitive by looking at how the pseudopaths ℳ θ \mathcal{M}_{\theta} and ℳ θ + π 2 \mathcal{M}_{\theta+\frac{\pi}{2}} behave near the special points when γ \gamma is nice enough, or by intuitively thinking about “areas enclosed” by those pseudopaths when they don’t form “loops”. Note that we have not defined those concepts in quotation marks for pseudopaths. Intuition comes from treating them as paths.

At the same time, we may try to prove some continuity statements on those rhombi when θ \theta varies. If both are being proven, then we may try to apply some intermediate value theorem arguments like what Arnold Emch did with nice analytic Jordan curves [1].

## References

- [1] Arnold Emch, *On some properties of the medians of closed continuous curves formed by analytic arcs*, American Journal of Mathematics 38 (1916), no. 1, 6–18.
- [2] J. E. Greene and A. Lobb, *The rectangular peg problem*, arxiv:2005.09193 (2020).
- [3] Cole Hugelmeyer, *Every smooth jordan curve has an inscribed rectangle with aspect ratio equal to 3 \sqrt{3}*, arxiv:1803.07417 (2018).
- [4] Benjamin Matschke, *A survey on the square peg problem*, Notices of the American Mathematical Society 61 (2014), 346.
- [5] Mark D. Meyerson, *Balancing acts*, Topology Proceedings 6 (1981), no. 1, 59–75.
- [6] Terence Tao, *An integration approach to the Toeplitz square peg problem*, Forum Math. Sigma 5 (2017), Paper No. e30, 63.
- [7] Otto Toeplitz, *Ueber einige aufgaben der analysis situs*, Verhandlungen der Schweizerischen Naturforschenden Gesellschaft 4 (1911), 197.

[◄][1][image: ar5iv homepage] [2]
[Feeling lucky?][3] [4]
[Conversion report][5]
[Report an issue][6]
[View original on arXiv][7] [►][8]


## Links

[1]: /html/2010.05100
[2]: /
[3]: /feeling_lucky
[4]: /land_of_honey_and_milk
[5]: /log/2010.05101
[6]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+2010.05101
[7]: https://arxiv.org/pdf/2010.05101
[8]: /html/2010.05102
