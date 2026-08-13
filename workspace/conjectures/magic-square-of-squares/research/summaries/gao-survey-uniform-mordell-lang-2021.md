> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/gao-survey-uniform-mordell-lang-2021.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/2104.03431 | converted from PDF -->

## What is in it

- Σ > degL(C)
M(M−1)/2 degL(V )
(M−1)(M−2)/2 · degL(C)
M degL⊠M (Z) degL(V )
M−1,
- {Q ∈ Cs(Q) : ˆhL(Q − P ) ≤ c1 max{1, hMg ,M(s)}
} < c2,
- {
P − Ps ∈ (Cs − Ps)(Q) ∩ Γ : ˆhL(P − Ps) > c max{1, hMg ,M(s)}
} ≤ c
ρ


## What it claims

Abstract. This expository survey is based on my online talk at the ICCM 2020. It aims to
sketch key steps of the recent proof of the uniform Mordell–Lang conjecture for curves embedded
into Jacobians (a question of Mazur). The full version of this conjecture is proved by combining
Dimitrov–Gao–Habegger [DGH21] and K¨uhne [K¨uh21a]. We include in this survey a detailed
proof on how to combine these two results, which was implicitly done in [DGH20] but not
explicitly written in existing literature. At the end of the survey we state some future aspects.

Contents

1. Introduction 1
2. The Height Machine 6
3. Vojta’s method 8
4. Basic setup and Statement of the New Gap Principle 10
5. Betti map and Betti form 12
6. Non-degenerate subvarieties 15
7. The height inequality and its application 17
8. Equidistribution on non-degenerate subvarieties and its application 20
9. Proof of the New Gap Principle and proof of Uniform Mordell–Lang for curves 24
10. Further aspects 27
References 32

1. Introduction

Let F be a ﬁeld of characteristic 0. A smooth curve C deﬁned over F is a geometrically…

## Statements it makes

Theorem 1.1 (Dimitrov–Gao–Habegger + K¨uhne). Let g ≥ 2 be an integer. Then there exists
a constant c(g) ≥ 1 with the following property. Let C be a smooth curve of genus g deﬁned over
F , let P0 ∈ C(F ), and let Γ be a subgroup of Jac(C)(F ) of ﬁnite rank ρ. Then

Proposition 2.1. We have

Theorem 2.2. Let f : X //❴❴❴ Y be a generically ﬁnite rational map between projective vari-
eties. Let L be an ample line bundle on X and M be an ample line bundle on Y . Then

Proposition 2.3. We have, for all x ∈ A(Q),

Theorem 2.4. Assume L is ample. Then
(i) ˆhA,L(x) ≥ 0 for all x ∈ A(Q);
(ii) ˆhA,L(x) = 0 if and only if x ∈ A(Q)tor;
(iii) ˆhA,L extends R-linearly to a positive deﬁnite quadratic form A(Q) ⊗Q R → R, which by
abuse of notation is still denoted by ˆhA,L.

Theorem 2.5. There exists a constant c = c(A/S, L, M) > 0 such that

Theorem 3.1. Let g ≥ 2 and C be a smooth curve of genus at least 2 deﬁned over Q. Let
P0 ∈ C(Q), and j : C → Jac(C) be the Abel–Jacobi embedding via P0.
There exists a constant R = R(C, P0) > 0 such that the following properties hold true. Con-
sider all distinct points P, Q ∈ C(Q) such that |j(Q)| ≥ |j(P )| ≥ R and

Theorem 3.2. Let C ⊂ A be an irreducible closed subvariety that dominates S and such
that C → S is a ﬂat family of curves of genus at least 2. Then there exists a constant
c = c(π, L, M; C) ≥ 1 with the following property. Suppose s ∈ S(Q) and Γ is a subgroup
of As(Q) of ﬁnite rank ρ ≥ 0, then

Theorem 4.1 (Dimitrov–Gao–Habegger + K¨uhne). There exist positive constants c1, c2 de-
pending only on g (apart from L and M) with the following property. For each s ∈ Mg(Q) and
each P ∈ Cs(Q), we have

Proposition 5.2. The Betti map b∆ satisﬁes the following properties.
(i) For each t ∈ T2g, we have that b−1
∆ (t) is complex analytic.
(ii) For each s ∈ ∆, the restriction b∆|As is a group isomorphism.
(iii) The map (b∆, π) : A∆ → T2g × ∆ is a real analytic isomorphism.

Proposition 5.5. The cohomology class of the Betti form ω on Aan
g,D coincides with the ﬁrst
Chern class c1(Lg,D) of Lg,D.

Lemma 6.2. Let X and Y be irreducible subvarieties of A such that π|X and π|Y are both
dominant. Assume that X is non-degenerate. Then X ×S Y is a non-degenerate subvariety of
A ×S A.

Lemma 6.3. Assume π|X sm is smooth and x ∈ X sm(C) satisﬁes (ω|∧ dim X
X )x ̸= 0. Then we
have (ωM |∧ dim X [M ]
X [M ] )(x,...,x) ̸= 0.

Theorem 6.4. Let S → Mg be a generically ﬁnite morphism. Let DM be as from (4.3). Then
DM (C[M +1]
g ) ×Mg S is a non-degenerate subvariety of Jac(Cg/Mg)[M ] ×Mg S for M ≥ dim S + 1;

Theorem 6.4 is a particular case of the more general [Gao20a, Thm.10.1], which we state
now. We expect [Gao20a, Thm.10.1]…

The…


*[further statements in the full text]*

*[digest of a 111504 character source; every section, statement, and proof in full at `research/sources/gao-survey-uniform-mordell-lang-2021.full.md`]*
