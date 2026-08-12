> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/broutin_marckert_colliding_bullets.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/1709.00789 | converted from PDF -->

## What is in it

- {(σ, τ ) ∈ Rπ(V, ∆) : |SV,∆(σ, τ )| = k}


## What it claims

Abstract
The ﬁnite colliding bullets problem is the following simple problem: consider a gun, whose
barrel remains in a ﬁxed direction; let (Vi)1≤i≤n be an i.i.d. family of random variables with
uniform distribution on [0, 1]; shoot n bullets one after another at times 1, 2, . . . , n, where
the ith bullet has speed Vi. When two bullets collide, they both annihilate. We give the
distribution of the number of surviving bullets, and in some generalisation of this model.
While the distribution is relatively simple (and we found a number of bold claims online),
our proof is surprisingly intricate and mixes combinatorial and geometric arguments; we
argue that any rigorous argument must very likely be rather elaborate.

1 Introduction

1.1 Motivation and models of interest

The colliding bullets problem may be stated as follows: a gun whose position and direction
remains ﬁxed shoots bullets, one every second. The speeds of the bullets are random, indepen-
dent and uniform in [0, 1]. Upon collision, they both annihilate without aﬀecting the others
speeds. The main questions of interest…

Th…

## Statements it makes

Theorem 1. We have, for any n ≥ 0,

Proposition 2. For Xn ∼ qn, we have the following convergence in distribution

Theorem 3. For any ℓ ∈ {5, 6, 7}, any n ≥ 0

Proposition 4. Let (Fn)n≥1 denote the sequence of sizes in the bullets ﬂock model, and let
(Dn)n≥1 denote the sequence of red distances to 0 in the two-step tree model. Then, with proba-
bility one,
(i) Fn = 0 inﬁnitely often, and
(ii) Dn → ∞; in particular, Dn = 0 only ﬁnitely often.

Lemma 7. Let (V, ∆) ∈ Gn. For any (σ, τ ) ∈ Sn × Sn−1, the set S(Vσ, ∆τ ) of indices of the
surviving bullets in the conﬁguration (σ, τ ) is fully determined by the map ΓV,∆(σ, τ, ·, ·, ·).

Lemma 8. The map Γ : (V, ∆) ↦→ ΓV,∆ is locally constant in Gn: for (V, ∆) ∈ Gn, there exists
an open neighborhood O of (V, ∆) in Rn × Rn−1 such that O ⊂ Gn, and

Lemma 12. For any (V, ∆) ∈ Gn, there exists an essentially generic parameter (V′, ∆′) ∈ Gn
such that the TCS of (V, ∆) and (V′, ∆
′) are identical, i.e., ΓV,∆ = ΓV′,∆′.

Lemma 13. Let n ≥ 2. Suppose that, the following two conditions hold:
(i) for every m < n, for every (Vm, ∆m−1) ∈ Gm, we have

Proposition 14. Suppose that, for every (Vn, ∆n−1) ∈ Gn we have Pff
Vn,∆n−1 = qn. Then:
(i) For any laws µ (without atom) and ν (atoms allowed, except at 0), we have

Lemma 15. The assumption (ii) of Lemma 13 holds: for every essentially generic parameter
(Vn, ∆n−1) in Gn, we have Pff
Vn,∆n−1 = Pff
V↓
n,∆n−1 .

Proposition 16. Let (V, ∆) be an honest simple singular parameter. Moreover, let π =
(min V, vℓ, vr, dℓ, dr) be a minimal critical pattern for (V, ∆). If the distribution of the number
of surviving bullets in (V−, ∆) and (V+, ∆) agree when we restrict the count to conﬁgurations
in Rπ, then the distribution is preserved over Sn × Sn−1.

Proposition 17. For any n ≥ 2, the properties P (1)
n , P (2)
n and P (3)
n all hold.

Lemma 18. Let n ≥ 2. If Pn holds, then P (3)
n+1 holds.

Lemma 19. Let n ≥ 2. If Pm holds for all m ≤ n, then P (1)
n+1 holds.

Lemma 20. Let n ≥ 2. If Pn holds, then P (2)
n+1 holds.

*[digest of a 86965 character source; every section, statement, and proof in full at `research/sources/broutin_marckert_colliding_bullets.full.md`]*
