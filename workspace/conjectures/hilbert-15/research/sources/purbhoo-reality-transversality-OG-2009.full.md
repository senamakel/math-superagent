<!-- source: https://arxiv.org/pdf/0911.2039 | converted from PDF -->

arXiv:0911.2039v1  [math.AG]  11 Nov 2009
REALITY AND TRANSVERSALITY FOR SCHUBERT CALCULUS
IN OG(n, 2n+1)

KEVIN PURBHOO

Abstract. We prove an analogue of the Mukhin-Tarasov-Varchenko theorem (for-
merly the Shapiro-Shapiro conjecture) for the maximal type Bn orthogonal Grass-
mannian OG(n, 2n+1).

1. The Mukhin-Tarasov-Varchenko Theorem

For any non-negative integer k, let Ck[z] denote the (k+1)-dimensional complex
vector space of polynomials of degree at most k:

Ck[z] := {f (z) ∈ F[z] | deg f (z) ≤ k} .

Fix integers 0 ≤ d ≤ m, and consider the Grassmannian X = Gr(d, Cm−1[z]), the va-
riety of all d-dimensional linear subspaces of the m-dimensional vector space Cm−1[z].
A point x ∈ X is real if x is is spanned by polynomials in Rm−1[z]; a subset of S ⊂ X
is real if every point in S is real.
The Mukhin-Tarasov-Varchenko theorem (formerly the Shapiro-Shapiro conjec-
ture) asserts that any zero-dimensional intersection of Schubert varieties in X, relative
a special family of ﬂags in Cm−1[z], is transverse and real. This theorem is remarkable
for two immediate reasons: ﬁrst, it is a rare example of an algebraic geometry prob-
lem in which the solutions are always provably real; second, the usual arguments to
prove transversality involve Kleiman’s transversality theorem [5], which requires that
the Schubert varieties be deﬁned relative to generic ﬂags. We recall the most relevant
statements here, and refer the reader to the survey article [13] for a discussion of the
history, context, reformulations and applications of this theorem.
To begin, we deﬁne a full ﬂag in Cm−1[z], for each a ∈ CP1:

F•(a) : {0} ⊂ F1(a) ⊂ · · · ⊂ Fm−1(a) ⊂ Cm−1[z] .

If a ∈ C, Fi(a) := (z + a)m−iC[z] ∩ Cm−1[z]
is the set of polynomials in Cm−1[z] divisible by (z + a)m−i. For a = ∞, we set
Fi(∞) := Ci−1[z] = lima→∞ Fi(a). The ﬂag F•(a) is often described as the ﬂag
osculating the rational normal curve γ : CP1 → P(Cm−1[z]), γ(t) = (z + t)m−1, which
simply means that Fi(a) is the span of {γ(a), γ′(a), . . . , γ(i−1)(a)}.

Research partially supported by an NSERC discovery grant.
1

2 KEVIN PURBHOO

Let Λ = Λd,m be the set of all partitions λ : (λ1 ≥ · · · ≥ λd), where λ1 ≤ m − d and
λd ≥ 0. We say λ is a partition of k and write λ ⊢ k or |λ| = k if k = λ1 + · · · + λd.
For every λ ∈ Λ, the Schubert Variety in X relative to the ﬂag F•(a) is

Xλ(a) := {x ∈ X | dim (x ∩ Fn−d−λi+i(a)) ≥ i , for i = 1, . . . , d} .

The codimension of Xλ(a) in X is |λ|.

Theorem 1 (Mukhin-Tarasov-Varchenko [6, 7]). If a1, . . . as ∈ RP
1 are distinct real
points, and λ1, . . . λs ∈ Λ are partitions with |λ1| + · · · + |λs| = dim X, then the
intersection Xλ1(a1) ∩ · · · ∩ Xλs(as)

is ﬁnite, transverse, and real.

In [13], Sottile conjectured an analogue of Theorem 1 for OG(n, 2n+1), the maximal
orthogonal Grassmannian in type Bn. In Section 2 of this note, we give a proof of
this conjecture (our Theorem 3). We discuss some of its consequences in Section 3; in
particular, we note that Theorem 3 should yield a geometric proof of the Littlewood-
Richardson rule for OG(n, 2n+1).

2. The theorem for OG(n, 2n+1)

Fix a positive integer n, and consider the non-degenerate symmetric bilinear form
⟨·, ·⟩ on the (2n + 1)-dimensional vector space C2n[z] given by

〈 2n∑

k=0 ak zk
k! ,
 2n∑

ℓ=0 bℓ zℓ
ℓ! 〉 =
 2n∑

m=0
(−1)mamb2n−m .

Let Y = OG(n, C2n[z])) be the orthogonal Grassmannian in C2n[z], which is the
variety of all n-dimensional isotropic subspaces of C2n[z]. The dimension of Y is
n(n+1)
2 .
The deﬁnition of a Schubert variety in Y requires our reference ﬂags to be orthog-
onal. The bilinear form on C2n[z] has been chosen so that this is true for the ﬂags
F•(a).

Proposition 2. For a ∈ CP
1, then the ﬂag F•(a) is an orthogonal ﬂag; that is
Fi(a)⊥ = F2n+1−i(a), for i = 0, . . . , 2n + 1.

Proof. For a = 0, ∞, this is straightforward to verify. We deduce the result for all
other a by showing that ⟨f (z), g(z)⟩ = ⟨f (z + a), g(z + a)⟩.
To see this, note that ⟨ d
dz ( zk
k! ), zℓ
ℓ! ⟩ = −⟨ zk
k! , d
dz ( zℓ
ℓ! )⟩, so d
dz is a skew-symmetric oper-
ator on C2n[z]. It follows that exp(a d
dz ) is an orthogonal operator on C2n[z] and so
⟨f (z + a), g(z + a)⟩ = ⟨exp(a d
dz )f (z), exp(a d
dz )g(z)⟩ = ⟨f (z), g(z)⟩. □

REALITY AND TRANSVERSALITY FOR SCHUBERT CALCULUS IN OG(n, 2n+1) 3

The Schubert varieties in Y are indexed by the set Σ of all strict partitions σ :
(σ1 > σ2 > · · · > σk), with σ1 ≤ n, σk > 0, k ≤ n. For convenience, we put σj = 0
for j > k. We associate to σ a decreasing sequence of integers, σ1 > · · · > σn, such
that σi = σi if σi > 0, and {|σ1|, . . . , |σn|} = {1, . . . , n}. It is not hard to see that σi

is given explicitly by the formula

σi = σi − i + #{j ∈ N | j ≤ i < j + σj} .

For σ ∈ Σ, the Schubert variety in Y relative to the ﬂag F•(a) is deﬁned to be

Yσ(a) := {y ∈ Y | dim (y ∩ F1+n−σi(a)) ≥ i , for i = 1, . . . , n} .

The codimension of Yσ(a) in Y is |σ|. We refer the reader to [2, 12] for further details.

Theorem 3. If a1, . . . as ∈ RP
1 are distinct real points, and σ1, . . . σs ∈ Σ, with
|σ1| + · · · + |σs| = dim Y , then the intersection

Yσ1(a1) ∩ · · · ∩ Yσs(as)

is ﬁnite, transverse, and real.

Proof. Let X = Gr(n, C2n[z]), and let Λ = Λn,2n+1. We prove this result by viewing
Y as a subvariety of X, and the Schubert varieties Yσ as the intersections of Schubert
varieties in X with Y . Note that dim X = 2 dim Y = n(n + 1).
For a strict partition σ ∈ Σ, let

̃σi := σi + i = σi + #{j ∈ N | j ≤ i < j + σj} .

Observe that ̃σi − ̃σi+1 = σi − σi+1 − 1 ≥ 0, and ̃σ1 ≤ σ1 + 1 ≤ n + 1; hence we see
that ̃σ : (̃σ1 ≥ ̃σ2 ≥ · · · ≥ ̃σn)
is a partition in Λ.
It follows directly from the deﬁnitions of Schubert varieties in X and Y that

Xeσ(a) ∩ Y = Yσ(a) .

Moreover, we have,
 |̃σ| = |σ| + ∑

i≥1 #{j ∈ N | j ≤ i < j + σj}

= |σ| + ∑

j≥1 #{i ∈ N | j ≤ i < j + σj}

= |σ| + ∑

j≥1 σj = 2|σ| .

Thus, if |σ1| + · · · + |σs| = dim Y , then |̃σ1| + · · · + |̃σs| = 2 dim Y = dim X, and so
by Theorem 1 the intersection
 Xeσ1(a1) ∩ · · · ∩ Xeσs(as)

4 KEVIN PURBHOO

is ﬁnite, transverse, and real; in particular this intersection is a zero-dimensional
reduced scheme. It follows immediately that

Yσ1(a1) ∩ · · · ∩ Yσs(as) = Y ∩ Xeσ1(a1) ∩ · · · ∩ Xeσs(as)

is ﬁnite and real. To see that the intersection on the left hand side is also transverse,
note that it is proper, so it suﬃces to show that it is scheme-theoretically reduced.
But this is immediate from the fact that the right hand side is the intersection of Y
with a zero-dimensional reduced scheme. □

3. Consequences

Let 0 ≤ d ≤ m, X = Gr(d, Cm−1[z]), be as in Section 1. We can consider the
Wronskian of d polynomials f1(z), . . . , fd(z) ∈ Cm−1[z]:

Wrf1,...,fd(z) :=
 ∣
∣
∣
∣
∣
∣
∣
∣
∣
 f1(z) · · · fd(z)
f ′
1(z) · · · f ′
d(z)
. . .
f (d−1)
1 (z) · · · f (d−1)
d (z)
∣
∣
∣
∣
∣
∣
∣
∣
∣
 .

This is a polynomial of degree at most dim X = d(n − d). If f1, . . . , fd are linearly
dependent, the Wronskian is zero; otherwise up to a constant multiple, Wrf1,...,fd(z)
depends only on the linear span of f1(z), . . . , fd(z) in Cm−1[z]. Thus the Wronskian
gives us a well deﬁned morphism of schemes Wr : X → P(Cd(n−d)[z]), called the
Wronski map. This morphism is ﬂat and ﬁnite [1]. For x ∈ X we will write
Wr(x; z) for any representative of Wr(x) in Cd(n−d)[z].
The Wronski map has a deep connection to the Schubert varieties on X relative
to the ﬂags F•(a), a ∈ CP1. A proof of the following classical result may be found
in [1, 9, 13].

Theorem 4. The Wronksian Wr(x; z) is divisible by (z + a)k if and only if x ∈ Xλ(a)
for some partition λ ⊢ k. Also, x ∈ Xµ(∞) for some µ ⊢ ( dim X − deg Wr(x; z)).

For X = Gr(n, C2n[z]), and Y = OG(n, C2n[z]) we deduce the following analogue:

Theorem 5. If y ∈ Y then Wr(y; z) = P (y; z)2 for some polynomial P (y; z) ∈
Cn(n+1)/2[z]. P (y; z) is divisible by (z + a)k if and only if y ∈ Yσ(a) for some strict
partition σ ⊢ k in Σ. Also, y ∈ Yτ (∞) for some strict partition τ ⊢ ( dim Y −
deg P (y; z))
.

Proof. Let y ∈ Y , and let (z + a)ℓ be the largest power (z + a) that divides Wr(x; z).
By Theorem 4, there exists a partition λ ⊢ ℓ such that y ∈ Xλ(a). Since ℓ is maximal,
y is in the Schubert cell

X ◦
λ(a) := {
x ∈ X ∣
∣ dim (
x ∩ Fk(a)) ≥ i, n+1−λi+i ≤ k ≤ n+1−λi+1+i, 0 ≤ i ≤ n
}

= Xλ(a) \ ( ⋃

|µ|>|λ| Xµ(a)) .

REALITY AND TRANSVERSALITY FOR SCHUBERT CALCULUS IN OG(n, 2n+1) 5

(Here, by convention, λ0 = n + 1, λn+1 = 0.) The Schubert cells in Y are of the form

Y ◦
σ (a) := {
y ∈ Y ∣
∣ dim (
y ∩ Fk(a)) ≥ i, n+1−σi ≤ k ≤ n−σi+1, 0 ≤ i ≤ n
}

= Xeσ(a) ∩ Y

(Here, by convention, σ0 = n + 1, σn+1 = −n − 1.) Now, the intersection X ◦
λ(a) ∩ Y
is nonempty, since it contains y, and is therefore a Schubert cell in Y . It follows that
λ = ̃κ for some strict partition κ ∈ Σ. Thus ℓ = |λ| = 2|κ| is even, which proves that
Wr(y; z) = P (y; z)2 is a square.
We have shown that (z + a)|κ| is the largest power of (z + a) that divides P (y; z),
and y ∈ Y ◦
κ (a). If y ∈ Yσ(a) then we must have Yσ(a) ⊃ Yκ(a), which implies that
|σ| ≤ |κ|, and hence (z + a)k divides P (y; z). Conversely, for any k ≤ |κ| there
exists σ ⊢ k such that Yσ(a) ⊃ Yκ(a), and so y ∈ Yσ(a). This proves the second
assertion. The third is proved by the same argument, taking ℓ = dim Y − deg P (y; z)
and a = ∞. □

If we write P (y) for the class of P (y; z) in projective space P(Cn(n+1)/2[z]), then
y ↦→ P (y) deﬁnes a morphism of schemes P : Y → P(Cn(n+1)/2[z]).

Theorem 6. P is a ﬂat, ﬁnite morphism.

Proof. Let h(z) = (z + a1)k1 · · · (z + as)ks ∈ Cn(n+1)/2[z]. By Theorem 5,

P −1(h(z)) =
 s⋂

i=1
 ( ⋃

σi⊢ki Yσi(ai)) ,

which, by Theorem 3, is a ﬁnite set. Since P is a projective morphism, this implies
that that P is ﬂat and ﬁnite [4, Ch. III, Exer. 9.3(a)]. □

In [9] we showed that the properties of the Wronski map and Theorem 1 can be used
to give geometric interpretations and proofs of several combinatorial theorems in the
jeu-de-taquin theory, including the Littlewood-Richardson rule for Grassmannians in
type An. The map P and Theorem 3 are the appropriate analogues for OG(n, 2n+1).
With a few modiﬁcations, it should be possible to use the arguments in [9] to give
geometric proofs of the analogous results in the theory of shifted tableaux, as devel-
oped in [3, 8, 10, 11, 14], including the Littlewood-Richardson rule for OG(n, 2n+1).
The main ingredients required to adapt these proofs are Theorems 3, 5 and 6, and
the Gel’fand-Tsetlin toric degeneration of OG(n, 2n+1). The complete details should
be straightforward but somewhat lengthy, and we will not include them here.

References

[1] D. Eisenbud and J. Harris, Divisors on general curves and cuspidal rational curves, Invent.
Math., 74 (183), 371–418.
[2] Wm. Fulton and P. Pragacz, Schubert varieties and degeneracy loci, Lecture Notes in Mathe-
matics, vol. 1689, Springer-Verlag, Berlin, 1998.

6 KEVIN PURBHOO

[3] M. Haiman, Dual equivalence with applications, including a conjecture of Proctor, Discrete
Math. 99 (1992), 79–113.
[4] R. Hartshorne, Algebraic Geometry, Graduate Texts in Math. 52, Springer-Verlag, 1977.
[5] S. L. Kleiman, The transversality of a general translate, Compositio Math. 28 (1974), 287–297.
[6] E. Mukhin, V. Tarasov and A. Varchenko, The B. and M. Shapiro conjecture in real algebraic
geometry and the Bethe Ansatz, to appear in Ann. Math.
[7] E. Mukhin, V. Tarasov and A. Varchenko, Schubert calculus and representations of general
linear group, preprint, arXiv:0711.4079.
[8] P. Pragacz, Algebro-geometric applications of Schur S- and Q- polynomials, in Topics in invari-
ant theory, Seminaire d’Algebre Dubreil-Malliavin 1989–1990 (M.-P. Malliavin ed.), Springer
Lecture Notes in Math. 1478, 130–191, Springer, 1991.
[9] K. Purbhoo, Jeu de taquin and a monodromy problem for Wronksians of polynomials, preprint.
[10] B. E. Sagan, Shifted tableau, Schur Q-functions, and a conjecture of Stanley, J. Comb. Theory,
ser. A. 45 (1987), 62–03.
[11] J.R. Stembridge, Shifted tableaux and the projective representations of the symmetric group,
Adv. Math. 74 (1989), 87–134.
[12] F. Sottile, Pieri-type formulas for maximal isotropic Grassmannians via triple intersections,
Colloq. Math., 82 (1999), 49–63.
[13] F. Sottile, Frontiers of reality in Schubert calculus, preprint.
[14] D. Worley, A theory of shifted Young tableau, Ph. D. thesis, M.I.T., 1984, available at
http://hdl.handle.net/1721.1/15599.

Department of Combinatorics & Optimization, University of Waterloo, Waterloo,
ON, N2L 3G1, CANADA
E-mail address: kpurbhoo@math.uwaterloo.ca
URL: http://www.math.uwaterloo.ca/~kpurbhoo
