<!-- source: https://arxiv.org/pdf/2510.22786 | converted from PDF -->

ESSENTIAL DIMENSION RELATIVE TO BRANCHED COVERS OF
DEGREE AT MOST N

BENSON FARB AND JESSE WOLFSON

Abstract. We prove for various finite groups G and integers n ≥ 1 that there are families
of equations with Galois group G that cannot be simplified to a one-parameter family even
after adjoining a root of a polynomial of degree at most n. In more geometric language,
there are G-varieties X with the following property: for any G-equivariant branched cover
̃X → X of degree ≤ n, there is no dominant rational G-map ̃X 99K C to any G-curve C.
The method of proof is new, and applies in cases where previous methods do not.

1. Introduction

Let k be a perfect field. A G-variety over k is a k-variety X equipped with a faithful action
of a finite group G on X by birational automorphisms. A G-compression is a dominant
rational map f : X 99K Y

of G-varieties; equivalently, the G-action on X is the pullback via f of the G-action on Y .
In classical language, a G-compression is a simplification of equations via a rational change
of variables.

Example 1.1 (Kummer’s theorem). Suppose that char(k) ∤ n and that k contains a
primitive nth root of unity ζ ∈ k. Then every Z/nZ-variety compresses to P1 with its
standard Z/nZ-action z ↦→ ζ · z. In Galois-theoretic terms, every cyclic extension of a
function field of k-varieties is given by “adjoining an nth root”.

In contrast, Felix Klein proved that if char(k) = 0 then there is an A5-action on P2 that
cannot be compressed to any A5-action on a 1-dimensional variety. To state this result in
modern terms we need the following definition of Buhler-Reichstein [BR97].

Definition 1.2 (Essential dimension). Let k be a field. The essential dimension over
k of a faithful G-variety X, denoted edk(X 99K X/G) or edk(X), is the smallest d ≥ 1 so
that there is a G-compression X 99K Y over k to a d-dimensional faithful G-variety Y .

Kummer’s theorem gives edk(X) = 1 for every Z/nZ-variety X over k with a primitive
nth root of unity; Klein’s theorem gives edk(P2 → P2/A5) = 2.
1 In contrast to his incom-
pressibility result for A5, Klein proved that every A5 extension of function fields is indeed
icosahedral after adjoining a square root. In more geometric language:

The authors are partially supported by NSF grants DMS- 2203355(BF), and DMS-1944862 and DMS-
2506184 (JW).
1This holds for any field k not containing F4, cf. [Led07, Proposition 5] and [CHKZ08, Theorem 1.6].
1arXiv:2510.22786v1  [math.AG]  26 Oct 2025
2 BENSON FARB AND JESSE WOLFSON

Theorem 1.3 (Klein’s Normalformsatz). Let k be a field of characteristic 0 with √
5 ∈
k. Let X be any A5-variety over k. Then X has an A5-equivariant branched cover
2 ̃X 99K X
of degree at most 2 such that there is an A5-compression

̃X 99K P1.

Klein’s Normalformsatz is an example of a general classical problem, studied by Hamilton
[Ha1836], Sylvester-Hammond [SH1887, p.1] and many others, which asks: can one reduce
the number of variables in a system of polynomials by adjoining the solutions of a lower
degree polynomial? In more geometric language 3:

Problem 1.4 (Hamilton [Ha1836]). Let k be a field. Compute, for a given faithful G-
variety X and n ≥ 1,

(1.1) edk(X; ≤ n) := min{dim(Y ) : ∃ ̃X ≤n
99K X and ∃ G-compression ̃X 99K Y }

where the min ranges over all faithful G-varieties ̃X and Y over k and all branched covers
̃X 99K X of degree at most n. Further, for a given finite group G, compute

(1.2) edk(G; ≤ n) := sup edk(X; ≤ n)

where the supremum is taken over all faithful G-varieties X. 4

Remark 1.5.

(1) The assumption that the G-actions are faithful is critical. Without this, there is
always the trivial map to a point (with constant G-action).
(2) In classical language, the G-variety X encodes the problem of solving for x ∈ X
such that f (x) = y for given y, where f : X → X/G = Y is the quotient. In this
language, Problem 1.4 asks how simply an equation with Galois group G can be
solved using elimination theory and an accessory algebraic function of degree at
most n.

One reason for Klein’s and others’ interest in Problem 1.4 is that many of the known
solutions to classical equations, for example those involving modular functions and those
in enumerative geometry, are of this form; namely, where one can reduce the number of
variables by adjoining the roots of a polynomial of lower degree. See [FW19] and [FKW23]
for many examples. Klein’s theorems mentioned above can be written as:

edk(A5) = 2 but edk(A5; ≤ 2) = 1

for any k with char(k) = 0 and with √
5 ∈ k.

While the literature of the last 200 years contains upper bounds for edC(G; ≤ n), n ≥ 2
for many examples, lower bounds are lacking, even in the simplest cases. For example,

2By a degree n branched cover we mean a generically n-to-1, dominant rational map ˜X 99K X.
3We leave it to the reader to write down the equivalent Galois-theoretic formulation.
4It is known that edk(G; ≤ n) = edk(V ; ≤ n) for any faithful linear G-variety V (e.g. [FKW23, Example
4.6 and Lemma 4.9]).

ESSENTIAL DIMENSION RELATIVE TO BRANCHED COVERS OF DEGREE AT MOST N 3

Klein proved that any PSL2(F7)-variety X has an at-most 4-sheeted branched cover ̃X that
compresses to the Klein quartic curve, so that

edC(PSL2(F7); ≤ 4) = 1.

Can one do better, replacing n = 4 by n = 2 or n = 3? Corollary 1.7 below implies that the
answer is “no” for n = 2; that is, edC(PSL2(F7); ≤ 2) > 1. The case n = 3 remains open.

Results. The main technical result of this paper is the following. Its proof exploits the
classical geometry of G-curves (see below).

Theorem 1.6 (Main Theorem). Let k be a perfect field. Let n ≥ 2. Let G be a finite
group such that:

(1) G has no proper subgroup of index at most n (in particular |G| > n),
(2) G contains a subgroup M with |M | > n that acts faithfully on P1 over k, and
(3) G does not act nontrivially on a smooth curve of genus g ≤ (n − 1)2.

Then edk(G; ≤ n) > 1.

Theorem 1.6 is applicable because its three hypotheses are easy to check in examples.
Over C, we can apply it to give the following.

Corollary 1.7 (Sample results).

(1) Let G be any non-abelian simple finite group except A5. Then

edC(G; ≤ 2) > 1.

(2) edC(A7; ≤ 6) > 1.

(3) Let p ≥ 7 be prime, and let n ≤ min{p − 1, 1 + ⌊√
1 + p(p2−1)
168 ⌋} (note that for
p > 163 this min equals p − 1). Then

edC(PSL2(Fp); ≤ n) > 1.

Remarks 1.8.

(1) Item 1 shows that Klein’s Normalformsatz (Theorem 1.3) is exceptional among finite
simple groups.
(2) In the spirit of Hilbert’s 13th problem, Item 2 shows that the general degree 7
polynomial cannot be reduced to a 1-variable algebraic function even after allowing
an accessory sextic.
(3) Item 3 shows that for each n ≥ 1 the theory of edC(−; ≤ n) is nontrivial.
(4) A finite group G is the Galois group of a family of polynomials of degree µ(G), where
µ(G) denotes the order of the smallest permutation representation. A sharpened
version of Problem 1.4 asks for lower bounds on edk(G, ≤ µ(G) − 1).5 Item 2 of
Corollary 1.7 addresses this sharp version of Problem 1.4 over C for A7. Similarly,
for p > 11, Galois showed that µ(PSL2(Fp)) = p + 1. Thus, for p > 163, the n in
Item 3 is only off by 1 from the natural choice of n = p.

5e.g. for G = An, this sharpened version asks how much we can simplify the general degree n polynomial
using only the solution of a single polynomial of lower degree.

4 BENSON FARB AND JESSE WOLFSON

Remark 1.9 (Previous methods). All work up to this point has given lower bounds only
for the version of Problem 1.4 where for a given prime p, any degree prime to p branched
cover ̃X → X is allowed; this is called the “essential dimension at p” and is denoted
by ed(X; p). See, e.g. [BR99, RY00, KM08, Rei10, FKW21, BF24, FKW23, FKW24]. These
methods applied to ed(G; ≤ n) give exactly the following:

(1.3) edk(G; ≤ n) ≥ max{{edk(G; p)}p>n, {edk(P ; ≤ n)}P ⊂G p-Sylow, p≤n}.

Classical questions about the complexity of solving polynomials, e.g. Problem 1.4, impose
a different set of requirements on the collection of branched covers allowed. To tackle these
it is necessary to move beyond what essential dimension at p can give.
As an example, we claim that for k = C, G = A7 and n = 6 the inequality (1.3) is strict,
and so does not suffice to prove Corollary 1.7 (2), since the right-hand side of (1.3) equals
1 in this case. To prove this claim, first note that

|A7| = 3 · 4 · 5 · 6 · 7

implies that edC(A7; p) ≤ 1 for p ≥ 5. For p = 2, 3, the p-Sylow of A7 is isomorphic to
Z/pZ × Z/pZ, and since 6 = 2 · 3, we can kill off a Z/pZ factor in both cases by adjoining
a 6th root. Kummer’s theorem implies that the right-hand side of (1.3) for A7 and n = 6
equals 1, as claimed. Similar arguments show that the special cases of Corollary 1.7

edC(PSL2(F7); ≤ 2) > 1, edC(PSL2(F11); ≤ 3) > 1, and edC(PSL2(F13; ≤ 4) > 1

give further examples where the inequality (1.3) is strict.

The outline of the proof of Theorem 1.6 proceeds as follows. We assume the theorem is
false, and from this we construct a single G curve C to which every G-variety compresses
after taking a degree ≤ n cover. We then construct a G-curve to violate this. The key
invariant we use to prove certain curves cannot compress to others is the gonality of a
curve.

Acknowledgements. It is a pleasure to thank Mark Kisin for many comments, questions
and discussions which helped sharpen and improve this paper. We thank Curt McMullen
and Zinovy Reichstein for helpful comments on a draft.

2. Rational functions on curves

We work throughout over a perfect field k. Our main tool is Castelnuovo’s inequality
(see [Sti09, Theorem 3.11.3] and also [Acc70, Proposition 1] for k = C).

Theorem 2.1 (Castelnuovo’s Inequality). Let C be an irreducible algebraic curve over a
perfect field k. Let fi : C → Di be rational maps of curves of degree ni ≥ 1 for i = 1, 2.
Assume that the map (f1, f2) : C → D1 × D2 is birational onto its image. Then

g(C) ≤ n1g(D1) + n2g(D2) + (n1 − 1)(n2 − 1).

We need a slightly more general form of [Sti09, Corollary 3.11.4]; presumably the following
lemma was known to Riemann.

ESSENTIAL DIMENSION RELATIVE TO BRANCHED COVERS OF DEGREE AT MOST N 5

Lemma 2.2. Let C be an algebraic curve of genus g(C) over a perfect field k. Let j ≥ 1 and
let fi : C → P1 (so fi ∈ k(C)) have degree n ≥ 1 for i = 1, . . . , j. If k(f1, . . . , fj) = k(C),
then
 g(C) ≤ (n − 1)2.

We remark that k(f1, . . . , fj) is the function field of the curve that is the image of the map
C → P1
1 × · · · × P1
j under the map z ↦→ (f1(z), . . . , fj(z)).

Proof. We prove this by induction on j. The case j = 2 is exactly the “Riemann Inequality”,
stated as [Sti09, Corollary 3.11.4]. For the induction step, let F ′ = k(f1, . . . , fj−1) ⊂ k(C).
Denote by g(F ′) the genus of the smooth projective curve with function field F ′. Let
n/m = [k(C) : F ′]. Then [F ′ : k(fi)] = m for all i = 1, . . . , j − 1, and by the inductive
hypothesis,
 g(F ′) ≤ (m − 1)
2.

By Castelnuovo’s Inequality [Sti09, Theorem 3.11.3],

g(C) ≤ n
m g(F ′) + ( n
m − 1)(n − 1)

≤ n
m (m − 1)2 + ( n
m − 1)(n − 1)

= n2

m − 3n + nm + 1

=: hn(m).

Because m | n, it suffices to prove that hn(m) ≤ (n−1)2 for all m ∈ [1, n]. For this, consider
the function hn(t) = n2
t − 3n + nt + 1 as an analytic function of t on the positive real line.
For t = 1, n, we have
 hn(1) = hn(n) = n
2 − 2n + 1 = (n − 1)
2.

Taking the derivative in t, we see that h′
n(t) = n − ( n
t )2, and thus hn(t) has a unique critical
point in the positive reals at t = √n ∈ [1, n]. Therefore, the maximum of hn(t) for t ∈ [1, n]
occurs at t = √n or at one of the endpoints t = 1, n. But for n > 1:

hn(√n) = 2n
√n − 3n + 1

= (2
√
n − 1)n − 2n + 1

≤ n
2 − 2n + 1

= hn(1) = hn(n) = (n − 1)
2.

We conclude that hn(t) ≤ (n − 1)2 for all t ∈ [1, n] and thus conclude the inductive step as
claimed. □

Corollary 2.3. Let G be a finite group. Assume that |G| ∤ n and that G does not act
nontrivially on an algebraic curve of genus at most (n − 1)2. Then no faithful irreducible
G-curve C admits a degree n rational function.

6 BENSON FARB AND JESSE WOLFSON

Proof. Let C be a faithful G curve. Suppose the contrary, i.e. there exists a degree n map
f : C → P1. For g ∈ G, let fg : C → P1 denote the map x ↦→ f (gx). Let

F = k({fg}g∈G) ⊂ k(C)

denote the compositum. By construction, the field F is G-invariant. By Lemma 2.2,
g(F ) ≤ (n − 1)2. Therefore, our assumption on G implies that F ⊂ k(C)G, i.e. G fixes all
the elements of F , and thus F = k ({fg}g∈G) = k(f ). But then,

n = [k(C) : k(f )] = [k(C) : k(C)G][k(C)
G : k(f )]

= |G|[k(C)
G : k(f )]

which contradicts our assumption that |G| ∤ n. □

We close this section with two additional lemmas. First, a standard exercise with the
field norm shows the following.

Lemma 2.4. Let C be an irreducible curve. Suppose there exists a dominant map H → C
and a degree n rational function h : H → P1. Then C has a degree n rational function
f : C → P1.

Proof. Let h : H → P1 be a degree n map. Let Nk(H)/k(C) : k(H)× → k(C)× denote the
field norm. Then f := Nk(H)/k(C)(h) ∈ k(C) is degree n. □

3. Induced Actions on Unions of Rational Curves

As above, we work over a perfect field k. Our main invariant for showing edk(−; ≤ n) > 1
comes from studying actions on unions of rational curves induced from a finite subgroup of
PSL2(k). We can now state and prove our key lemma.

Lemma 3.1. Let G be a finite group. Let k be a perfect field. Suppose that:

(1) edk(G; ≤ n) = 1,
(2) G has no proper subgroup of index at most n, and
(3) G contains a subgroup M ⊂ G such that M ↪→ PSL2(k) and |M | > n.

Then there exists a smooth, irreducible, projective faithful G-curve ˜C with a degree m ra-
tional function f : ̃C → P1 for some m ≤ n.

Proof. We work throughout in the birational category, i.e. the category of varieties and
rational maps.
Let V be a faithful representation of G, viewed as a linear variety. By assumption,
there exists a branched cover π : E 99K V /G, of degree ≤ n such that π∗(V → V /G)
arises (rationally) by pullback from a G-cover of smooth projective curves ˜C → C. Extend
the inclusion of function fields κ(V /G) → κ(E) to an inclusion of separably closed fields
¯κ(V /G) → ¯κ(E), and consider the maps

Gal(¯κ(E)/κ(E)) → Gal(¯κ(V /G) → κ(V /G)) → G.

corresponding to V → V /G. The second map is surjective, and the image of the composite
map has index ≤ n, as π has degree ≤ n. By our assumption on G, we conclude that the

ESSENTIAL DIMENSION RELATIVE TO BRANCHED COVERS OF DEGREE AT MOST N 7

composite map is surjective, and hence π∗(V ) → E is an irreducible G-cover. In particular,
˜C is irreducible.
Next we remark that since V → V /G is G-versal, it is M -versal. Indeed, if X is any M -
variety, one may apply G-versality to (X × G)/M. Thus there is a rational, M -equivariant
map P1 → V, corresponding to Y := P1/M → V /G. Let YE = π∗(Y ), let κ(YE) ⊃ κ(Y ),
be the function field at some generic point of YE, and let ¯κ(YE) be a separable closure of
κ(YE). Consider the composite

Gal(¯κ(YE)/κ(YE)) → Gal(¯κ(YE)/κ(Y )) → M.

The second map is surjective, and the image of the composite has index ≤ n. In particular,
this image is non-trivial, as |M | > n. Hence the composite map

YE → E → C

is non-constant, and so the corresponding M -equivariant map ˜YE : π∗(P1) → ˜C is noncon-
stant. As ˜YE → P1 has degree ≤ n, we conclude by Lemma 2.4, that ̃C admits a map
h : ̃C → P1 of degree ≤ n. □

4. Finishing the proofs of Theorem 1.6 and Corollary 1.7

We now complete the proofs of the theorems stated in the introduction.

Proof of Theorem 1.6. Let n ≥ 1. Let G be a finite group satisfying the assumptions of
the theorem. Suppose to the contrary that edk(G; ≤ n) = 1. By Lemma 3.1, there exists
a smooth, irreducible projective curve ̃C with a faithful G-action and a degree m rational
function for some m ≤ n. By Corollary 2.3, this implies that G acts nontrivially on a curve
of genus at most (m − 1)2 ≤ (n − 1)2. But this contradicts Assumption (3) of the theorem.
Thus edk(G; ≤ n) > 1. □

There are infinitely many examples of (k, G, n) to which Theorem 1.6 applies: e.g. for
k = C, G simple, and for

(4.1) n ≤ min{d(G), max{m | Cm+1 ⊂ G, 1 + √1 + |G|/84}}

where d(G) denotes the size of the smallest permutation representation of G. For the
finite groups G of classical type, a complete list of d(G) is given in [Coo78, Table 1]. For
every finite simple group G the number d(G) can be extracted from the classification of
finite simple groups (e.g. see the Atlas [CCN+85] for the sporadic simple groups), and by
Cauchy’s Lemma, one can replace the max over cyclic subgroups in (4.1) by p − 1 for p
the largest prime dividing |G|. As the labeling implies, Corollary 1.7 gives a set of such
examples.

Proof of Corollary 1.7. We start with statement 1. Let G be a non-abelian finite simple
group not isomorphic to A5. As every index 2 subgroup is normal, G has no proper subgroup
of index 2. Further, there exists an odd prime p such that p | |G|, and thus by Cauchy’s
lemma, a cyclic subgroup Cp ⊂ G of order greater than 2. By Theorem 1.6, it suffices to
prove that G does not act on an elliptic or rational curve over C. Because the hyperelliptic
involution is unique and central in the automorphism group of a hyperelliptic curve [FK92,

8 BENSON FARB AND JESSE WOLFSON

Ch. III, Corollaries 2, 3, p. 108], we see that every group acting faithfully on a rational,
elliptic or hyperelliptic curve is a subquotient of a C2-central extension

1 → C2 → G → ¯G → 1

with ¯G ⊂ PGL2(C). Combining Theorem 1.6 with Klein’s [Kl1884] classification of finite
M¨obius groups, we obtain statement 1.
For statement 2, note that A7 has no subgroup of index less than 7, and there exists a
C7 ⊂ A7 (pick a 7-cycle). The argument above combines with the Hurwitz bound to show
that A7 does not act nontrivially on any curve of genus less than 31. But 31 > (6−1)2 = 25,
so the statement follows from Theorem 1.6.
For the final statement 3, as observed above, for p ≥ 7 the group PSL2(Fp) is simple and
does not act on a rational or elliptic curve. Therefore, by the Hurwitz bound, PSL2(Fp)
does not act on a curve of genus less than | PSL2(Fp)|/84 + 1. It remains to verify the
first two assumptions of Theorem 1.6. For p = 7, 11, PSL2(Fp) has no subgroup of index

less than p, and the upper bound on n above is equal to 1 + ⌊
√
1 + p(p2−1)
168 < p − 1.
For p > 11, Galois showed that PSL2(Fp) has no subgroup of index less than p + 1 (cf.
[Coo78, p. 213]). In all cases, we see that PSL2(Fp) satisfies the first assumption in the
statement of Theorem 1.6. For the second assumption, note that for all p > 2, we have
| PSL2(Fp)| = p(p2−1)
2 . By Cauchy’s Lemma, Cp ⊂ PSL2(Fp). In each case, we conclude by
Theorem 1.6 that edC(PSL2(Fp); ≤ n) > 1. □

References

[Acc70] R. Accola, Strongly branched coverings of closed Riemann surfaces, Proc. Amer. Math. Soc. 26
(1970), 315–322.
[BF24] Patrick Brosnan and Najmudden Fakrhuddin, Fixed points in toroidal compactifications of
Shimura varieties and essential dimension of congruence covers, J. Alg. Geom. 33 (2024), no. 2,
295–346.
[BR97] J. Buhler and Z. Reichstein, On the essential dimension of a finite group, Compositio Math. 106
(1997), no. 2, 159–179.
[BR99] Joe Buhler and Zinovy Reichstein, On Tschirnhaus transformations, Topics in number theory
(University Park, PA, 1997) 467 (1999), no. 2, 127–142.
[CCN
+85] J.H. Conway, R.T. Curtis, S.P. Norton, R.A. Parker, and R.A. Wilson, Atlas of Finite Groups -
Maximal Subgroups and Ordinary Characters for Simple Groups, Clarendon Press, Oxford, 1985.
[CGR06] V. Chernousov, P. Gille, and Z. Reichstein, Resolving G-torsors by abelian base extensions, J.
Algebra 296 (2006), 561–581.
[CHKZ08] H. Chu, S.-J. Hu, M.-C. Kang, and J. Zhang, Groups with essential dimension one, Asian J.
Math. 12 (2008), no. 2, 177-192.
[Coo78] B. Cooperstein, Minimal degree for a permutation representation of a classical group, Israel J.
Math. 30 (1978), 213–235.
[FW19] B. Farb and J. Wolfson, Resolvent degree, Hilbert’s 13th Problem and Geometry, L’Enseignement
Math. 65 (2019), no. 3, 303–376.
[FKW21] B. Farb, M. Kisin, and J. Wolfson, The essential dimension of congruence covers, Compos. Math.
157 (2021), no. 11, 2407-2432.
[FKW23] , Modular functions and resolvent problems (with an appendix by Nate Harman), Math.
Ann. 386 (2023), 113–150.
[FKW24] , Essential dimension via prismatic cohomology), Duke Math. J. 173 (2024), 3059–3106.

ESSENTIAL DIMENSION RELATIVE TO BRANCHED COVERS OF DEGREE AT MOST N 9

[FK92] H. Farkas and I. Kra, Riemann Surfaces, Springer, 1992.
[Ha1836] W.R. Hamilton, Inquiry into the validity of a method recently proposed by George B. Jerrard,
esq., for transforming and resolving equations of elevated degrees, Report of the Sixth Meeting of
the British Association for the Advancement of Science (Bristol) (1836), 295-–348.
[Ish92] N. Ishii, Coverings over d-gonal curves, Tsukuba J. Math. 16 (1992), no. 1, 173–189.
[Ish95] , Remarks on d-gonal curves, Tsukuba J. Math. 19 (1995), no. 2, 329–345.
[KM08] N. Karpenko and A. Merkurjev, Essential dimension of finite p-groups, Invent. Math. 172 (2008),
491–508.
[Kl1884] F. Klein, Vorlesungen ¨uber das Ikosaeder und die Aufl¨osung der Gleichungen vom f¨unften Grade
(Lectures on the Icosahedron and the Solution of the Equation of the Fifth Degree), Leipzig,
T¨ubner, 1884.
[Kl1879] , Ueber die Aufl¨osung gewisser Gleichungen vom siebenten und achten Grade, Math. Ann.
15 (1879), 252-282.
[Led07] A. Ledet, Finite groups of essential dimension one, J. Alg. 311 (2007), 31-37.
[Rei10] Z. Reichstein, Essential dimension, Proceedings of the International Congress of Mathematicians
II (2010), 162-188.
[RY00] Z. Reichstein and B. Youssin, Essential dimensions of algebraic groups and a resolution theorem
for G-varieties, Canad. J. Math. 52 (2000), no. 5, 1018–1056. With an appendix by J´anos Koll´ar
and Endre Szab´o.
[Sti09] H. Stichtenoth, Algebraic Function Fields and Codes, Springer, 2009.
[SH1887] J.J. Sylvester and J. Hammond, On Hamilton’s Numbers, Phil. Trans. R. Soc. London A 178
(1887), 285–312.

Department of Mathematics, University of Chicago
Email address: farb@math.uchicago.edu

Department of Mathematics, University of California-Irvine
Email address: wolfson@uci.edu
