<!-- source: https://arxiv.org/pdf/2604.04850 | converted from PDF -->

A NOTE ON BREMNER’S CONJECTURE AND UNIFORMITY

NATALIA GARCIA-FRITZ AND HECTOR PASTEN

Abstract. In 1998, Bremner conjectured that elliptic curves over the rationals having long se-
quences of distinct rational points whose x-coordinates are in arithmetic progression, have large
rank. This was proved some years ago in a strong form as a consequence of previous work by the
authors, by a combination of Nevanlinna theory and the uniform Mordell–Lang theorem of Gao–
Ge–K¨uhne. Thus, if the ranks of elliptic curves over the rationals are uniformly bounded, then so
are the lengths of the aforementioned arithmetic progressions. In this note we give a much more
direct proof of this last statement, using the height-uniform Mordell theorem of Dimitrov–Gao–
Habegger. The method is flexible and we give a new application of these ideas to x-coordinates
in finitely generated multiplicative groups and geometric progressions; connections to a possible
semiabelian uniform Mordell–Lang are also discussed.

1. Introduction

1.1. Bremner’s rank conjecture. For an elliptic curve E over Q, an arithmetic progression
of length M is a sequence of points P1, ..., PM in E(Q) whose x-coordinates with respect to one
(equivalently, all) Weierstrass equation y2 = f (x) with f cubic, form a non-trivial arithmetic
progression in Q.
In [2] Bremner conjectured that elliptic curves over Q with long arithmetic progressions have
large rank. To be accurate, Bremner says:
It seems that points of an arithmetic progression have the tendency to be linearly independent in
the group of rational points (...)
As explained in [2], this conjecture is in part motivated by [4] which studies arithmetic progres-
sions on rank one elliptic curves in quadratic twist families. There is a large body of work studying
arithmetic progressions on elliptic curves —both experimental and theoretical— and we refer to
[14] for a literature review.
Bremner’s rank conjecture was already proved as a consequence of our previous work [14] via
a combination of Nevanlinna theory and an application of the uniform Mordell–Lang theorem of
Gao–Ge–K¨uhne [16] (see Section 1.5 for details).
Our aim here is twofold. We give an alternative and very short proof of a (conditional) unifor-
mity consequence of Bremner’s conjecture, and we discuss a new uniformity phenomenon involving
multiplicative groups and x-coordinates of rational points in elliptic curves. Both topics follow
similar ideas, where the main point is an auxiliary curve of genus 2 with split Jacobian.

1.2. Bremner’s uniformity question. In the same paper [2], even before discussing ranks, Brem-
ner explicitly asked the following:

Question 1.1 (Bremner’s uniformity question). Can there exist arbitrarily large arithmetic pro-
gressions on elliptic curves (over Q)?

Date: May 19, 2026.
2020 Mathematics Subject Classification. Primary: 11G05; Secondary: 11B25, 14G05.
Key words and phrases. Bremner’s conjecture, elliptic curves, arithmetic progressions, multiplicative groups, ranks,
uniformity.
N.G.-F. was supported by ANID Fondecyt Regular grant 1251300 from Chile. H.P. was supported by ANID
Fondecyt Regular grant 1230507 from Chile. 1arXiv:2604.04850v2  [math.NT]  18 May 2026
Regarding uniform boundedness of arithmetic progressions on Mordell elliptic curves y2 = x3 +k,
this particular family has attracted special attention under the name of Mohanty’s conjecture and
we refer the reader to [13] and the references therein for further discussion.
The following immediate consequence of Theorem 1.8 can be regarded as a conditional answer
to Question 1.1 and, in fact, it was consequences of this kind that served as a key motivation in
our work [14].

Theorem 1.2. If the ranks of elliptic curves over Q are uniformly bounded, then so are the lengths
of arithmetic progressions on elliptic curves over Q.

We refer the reader to [21] for a detailed study of the question of uniform boundedness of ranks
of elliptic curves, especially over Q.
In Section 3 we present a simple and short proof of Theorem 1.2 that avoids the heavy machinery
of Nevanlinna theory that we used in [14] and which “only” uses the height-uniform Mordell theorem
of Dimitrov–Gao–Habegger [9]. Key to our argument is the use of genus 2 curves with split Jacobian.
The result also holds over number fields, but the question of uniform boundedness of ranks in
more generality than Q seems more dubious, so we keep the discussion over Q (which, by the way,
is the original setting discussed by Bremner [2]).

1.3. Another uniformity result. Bremner’s uniformity question relates the group structure of
an elliptic curve to the additive structure of the affine line. A natural problem is to use the x-
coordinate map to relate the group structure in the elliptic curve to finitely generated multiplicative
groups on Gm. Using the same method of constructing genus 2 curves with split Jacobian as in our
new proof of Theorem 1.2, we prove a result that hints at a new uniformity question:

Theorem 1.3. If the ranks of elliptic curves over Q are uniformly bounded, then there is a constant
κ > 1 with the following property:
Let E be an elliptic curve over Q given by a Weierstrass equation y2 = f (x) such that f (0) ̸= 0
and denote by x : E → P1 the x-coordinate map. Let Γ be a finitely generated multiplicative subgroup
of Q× and let ρ be its rank. Then
 # (x(E(Q)) ∩ Γ) ≤ κ · 2
ρ.

A special case is that of geometric progressions. The study of consecutive terms of a geometric
progression appearing as x-coordinates of rational points of an elliptic curve has captured some
attention and we refer the reader to [3, 8, 15, 17] and the references therein. As a corollary of
the previous result, we note that uniform boundedness can be expected even if the terms of the
geometric progression are not consecutive.

Corollary 1.4. If the ranks of elliptic curves over Q are uniformly bounded, then there is a uniform
bound B such that the following holds:
Let E be an elliptic curve over Q given by a Weierstrass equation y2 = f (x) such that f (0) ̸= 0
and denote by x : E → P1 the x-coordinate map. If a, ab, ab2, ... is a geometric progression in Q×

with b ̸= ±1, then there are at most B rational points of E with x-coordinate in this geometric
progression.

Indeed, one takes Γ = ⟨a, b⟩; note that at most two rational points have the same x-coordinate.
The proof of Theorem 1.3 is similar to that of Theorem 1.2 and is given in Section 4.

1.4. Rank-dependent bound for multiplicative groups. Given the recent developments on
the height-uniform Mordell Conjecture (see Section 2) and, more generally, the height-uniform
Mordell–Lang Conjecture [16] it is reasonable to expect that a similar result for curves in semia-
belian varieties is within reach (see also the comments in Section 1.3 of [16] concerning semiabelian
2

varieties). Let us state here the simplest case concerning a semiabelian variety that is not a torus
or an abelian variety:

Conjecture 1.5 (Height-uniform Mordell–Lang for a semiabelian case). Let d ≥ 1 be an integer.
There is a constant c(d) > 1 depending only on d such that the following holds:
Consider the semiabelian surface A = E × Gm where E is an elliptic curve over Q. Let C ⊆ A
be an irreducible curve defined over Q that is generically finite of degree ≤ d over E and over Gm
under the coordinate projections A → E and A → Gm. Let G ⊆ A(Q) be a finitely generated group
of rank r. Then #(C ∩ G) ≤ c(d)1+r.

This statement is closely related to our discussion.

Theorem 1.6. Assume Conjecture 1.5. There is a constant K > 1 such that the following holds:
Let E be an elliptic curve over Q of rank r given by a Weierstrass equation y2 = f (x) and denote
by x : E → P1 the x-coordinate map. Let Γ be a finitely generated multiplicative subgroup of Q×

and let ρ be its rank. Then # (x(E(Q)) ∩ Γ) ≤ Kρ+r+1.

In fact, one uses Conjecture 1.5 by choosing C ⊆ E × Gm as the graph of the x-coordinate
rational map x : E 99K Gm. Then one takes d = 2 and G = E(Q) × Γ. Of course there is nothing
special about the x-coordinate map and a similar result (with other choices of d) holds for any
non-constant map E → P1.
For geometric progressions one gets a rank-dependent bound for the total number of terms
coming from rational points of the elliptic curve, not only consecutive terms (again, at most two
rational points have the same x-coordinate).

Corollary 1.7 (Rank-dependent bound for geometric progressions). Assume Conjecture 1.5. There
is a constant K > 1 such that the following holds:
Let E be an elliptic curve over Q of rank r given by a Weierstrass equation y2 = f (x) and denote
by x : E → P1 the x-coordinate map. If a, ab, ab2, ... is a geometric progression in Q× with b ̸= ±1,
then there are at most Kr+1 rational points of E with x-coordinate in this geometric progression.

1.5. About the proof of Bremner’s conjecture. Bremner’s conjecture was proved some years
ago. It is an immediate consequence of our previous work [14] in the following strong form:

Theorem 1.8 (Strong form of Bremner’s conjecture). There is an absolute constant C > 1 such
that if E is an elliptic curve over Q with rank r, then all arithmetic progressions on E have length
bounded by Cr+1.

More precisely, in 2019 we proved this result with C replaced by a quantity C0(jE) that only
depends on the j-invariant jE of E, which was strong enough to prove Bremner’s conjecture over
twist families, see [14]. The core of the proof is a technical Nevanlinna-theoretical argument that
reduced the problem to a suitable version of the Mordell–Lang conjecture for surfaces contained in
abelian varieties. At the time, only R´emond’s quantitative version of Mordell–Lang was available
[22, 23], whose constants depended on the Faltings height of the abelian variety. But the situation
improved in 2021 when Gao–Ge–K¨uhne [16] removed the dependence on the height and, in our
setting, this resulted in removing the dependence on jE (for the interested reader: this change
must be made in the first paragraph after the proof of Lemma 6.5 in [14] when one introduces the
constant c(En, Ln); everything else in the proof of Theorem 6.1 is the same and the statement gets
upgraded accordingly). This is mentioned, for instance, in [7].
It should be noted that this state of affairs is not unique to our theorem: it is well-known to
experts that most —if not all!— applications of R´emond’s bound became height-uniform thanks
3

to the Gao–Ge–K¨uhne theorem. In fact, after our proof of Bremner’s conjecture in [14], the idea
of studying additive patterns in the x-coordinates of rational points of elliptic curves via the Gao–
Ge–K¨uhne theorem was further developed by Caro and the first author of this note in [6].
We remark that another proof of Theorem 1.8 was recently claimed in the preprint [7], although
it assumes a certain height conjecture of Lang, so at present, that proof currently applies only to
certain restricted families of elliptic curves. Yet another new (unconditional) proof of Bremner’s
conjecture in the form of Theorem 1.8 was very recently claimed in the preprint [17] using different
techniques. Both arguments are independent of our original proof of Theorem 1.8 and they have
their own features.
Finally, we mention two technical points for experts: our Theorem 1.8 holds over any number field
(not just Q), and one can replace the x-coordinate map in the definition of arithmetic progression
by other rational functions (for instance, y-coordinates) leading to the same kind of result. This is
in fact the way we run the argument in Theorem 6.1 of [14].

2. Height-uniform Mordell

In 1922, Mordell [19] proposed his celebrated conjecture on rational points of curves:

Conjecture 2.1 (Mordell). Let k be a number field and X a smooth projective curve of genus
g ≥ 2 defined over k. Then the set of rational points X(k) is finite.

This conjecture was proved by Faltings in his spectacular work [10]. A second proof with com-
pletely different ideas was produced by Vojta in [24]. While Vojta’s initial argument was highly
sophisticated and used Arakelov geometry, Bombieri [1] translated it into classical diophantine
approximation terms that were later further developed by Faltings to solve the Mordell–Lang con-
jecture [11, 12].
At the core of Vojta’s proof there is a gap phenomenon first discovered by Mumford [20]. From
this gap phenomenon it was possible to extract a bound for the number of rational points. In a
remarkably explicit work, R´emond [22, 23] succeeded in finding such bounds in the more general
context of the Mordell–Lang conjecture. For curves (i.e. in the context of Mordell’s conjecture),
R´emond’s bound crucially depended on
• The genus of the curve
• The Mordell–Weil rank of the Jacobian, and
• The Faltings height of the Jacobian.
Conjecturally, there was room for improvement. For instance, Caporaso–Harris–Mazur [5] showed
that the Bombieri–Lang conjecture in all dimensions implies that for any integer g ≥ 2 and number
field k, there is a bound B(g, k) depending only on g and k such that every smooth projective curve
X of genus g defined over k satisfies
 #X(k) ≤ B(g, k).

A somewhat milder problem was asked by Mazur [18]: Is there a bound for #X(k) which is
independent of the Faltings height of the Jacobian (although it could still depend on the Mordell–
Weil rank)?
In 2020, Dimitrov–Gao–Habegger [9] finally answered Mazur’s question by proving the following
remarkable height-uniform upper bound:

Theorem 2.2 (Height-uniform Mordell). Let g ≥ 2 and d ≥ 1 be integers. There is a constant
c = c(g, d) depending only on g and d such that if X is a smooth projective curve of genus g defined
over a number field k of degree d over Q, then

#X(k) ≤ c1+ρ

where ρ is the Mordell–Weil rank of the Jacobian of X over k.
4

After the Dimitrov–Gao–Habegger paper, there have been several extensions and, most recently,
a completely explicit height-uniform upper bound has been obtained in [25].

3. Bremner’s uniformity question

Proof of Theorem 1.2. Let E be an elliptic curve over Q with Weierstrass equation y2 = f (x) where
f ∈ Q[x] is a monic cubic polynomial. Consider an arithmetic progression on E of length M ≥ 4.
Then E contains an arithmetic progression of length N = M − 3 whose first term is not a 2-torsion
point of E. Let b, a + b, 2a + b, ..., (N − 1)a + b
be the x-coordinates of this arithmetic progression and note that f (b) ̸= 0. Consider the equation

s
2 = f (at2 + b).

The hexic polynomial f (at2 + b) has no repeated roots because f is separable, a ̸= 0, and f (b) ̸= 0.
So, the previous equation defines a hyperelliptic curve X of genus 2. This curve comes with some
rational points: at least those with t coordinates

t = −n, ..., −1, 0, 1, 2, ..., n

where n = ⌊
√N − 1⌋. This produces at least 2n + 1 different rational points in X, that is,

2n + 1 ≤ #X(Q).

The substitution y = s, x = at
2 + b
defines a non-constant map π : X → E.
The Jacobian J of X is an abelian surface because X has genus 2, and the above map exhibits
E as an isogeny factor of J over Q. Therefore J splits as J ∼ E × E′ up to isogeny over Q where
E′ is another elliptic curve (which in general is not isogenous to E).
If the ranks of elliptic curves over Q are bounded by a constant R, then

rank J(Q) = rank E(Q) + rank E′(Q) ≤ 2R.

The Dimitrov–Gao–Habegger theorem (Theorem 2.2) provides an absolute constant c > 1 (in
particular, independent of E and X) such that

#X(Q) ≤ c
1+rank J(Q) ≤ c
1+2R.

This gives 2⌊√M − 4⌋ + 1 = 2n + 1 ≤ c1+2R, which shows that M is uniformly bounded (assuming
the existence of the uniform rank bound R). □

4. Finitely generated multiplicative groups

Proof of Theorem 1.3. This is very similar to the argument in the previous section. We assume
that the ranks of elliptic curves over Q are bounded by some R.
Let E and f (x) be as in the statement. For every a ∈ Q× the equation y2 = f (at2) defines a
genus 2 hyperelliptic curve Xa over Q because f is separable and f (0) ̸= 0. Its Jacobian Ja splits
over Q as Ja ∼ E × Ea for some elliptic curve Ea depending on the choice of a. This splitting
comes from the map Xa → E defined by (t, y) ↦→ (at2, y).
Theorem 2.2 gives an absolute constant c > 1 (in particular, independent of E and a) such that

#Xa(Q) ≤ c1+rank Ja(Q) ≤ c
1+2R.

Let a vary over a set of representatives of Γ/Γ2; this is at most 2ρ+1 choices of a ∈ Q×. Each
γ ∈ x(E(Q)) ∩ Γ gives a rational point in some Xa; namely, choose a as the representative of
[γ] ∈ Γ/Γ2. The result follows with κ = 2c1+2R. □
5

5. Acknowledgments

N.G.-F. was supported by ANID Fondecyt Regular grant 1251300 from Chile. H.P. was supported
by ANID Fondecyt Regular grant 1230507 from Chile. We thank Yuri Bilu for a comment on a
previous version that helped us to pay more attention to the split Jacobian point of view.

References

[1] E. Bombieri, The Mordell conjecture revisited. Annali della Scuola Normale Superiore di Pisa-Classe di Scienze,
1990, vol. 17, no 4, p. 615-640.
[2] A. Bremner, On arithmetic progressions on elliptic curves. Experimental Mathematics, 1999, vol. 8, no 4, p.
409-413.
[3] A. Bremner, M. Ulas, Rational points in geometric progressions on certain hyperelliptic curves. Publ. Math.
Debrecen 82.3–4 (2013): 669-683.
[4] A. Bremner, J. Silverman, N. Tzanakis, Integral points in arithmetic progression on y2 = x(x2 − n2). Journal of
Number Theory, (2000) 80(2), 187-208.
[5] L. Caporaso, J. Harris, B. Mazur, Uniformity of rational points. J. Amer. Math. Soc. 10 (1997), no. 1, 1-35.
[6] J. Caro, N. Garcia-Fritz, Linear x-coordinate relations of triples on elliptic curves. Journal of Number Theory
271 (2025): 109-121.
[7] S. Choi, Additive rigidity for x-coordinates of rational points on elliptic curves. Preprint (2026) (formerly: Elliptic
curves and rational points in arithmetic progression, 2025). arXiv:2510.03828
[8] A. Ciss, D. Moody, Geometric progressions on elliptic curves. Glasnik matematicki 52.1 (2017): 1-10.
[9] V. Dimitrov, Z. Gao, P. Habegger, Uniformity in Mordell-Lang for curves. Ann. of Math. (2) 194 (2021), no. 1,
237-298.
[10] G. Faltings, Endlichkeitss¨atze f¨ur abelsche Variet¨aten ¨uber Zahlk¨orpern. (German) [Finiteness theorems for
abelian varieties over number fields] Invent. Math. 73 (1983), no. 3, 349-366.
[11] G. Faltings, Diophantine approximation on abelian varieties. Annals of Mathematics, 133 (1991), 549-576.
[12] G. Faltings, The general case of S. Lang’s conjecture. Barsotti Symposium in Algebraic Geometry (Abano Terme,
1991). Perspect. Math. 15. Academic Press. San Diego. 1994. p. 175-182
[13] N. Garcia-Fritz, Quadratic sequences of powers and Mohanty’s conjecture. International Journal of Number
Theory 14.02 (2018), 479-507.
[14] N. Garcia-Fritz, H. Pasten, Elliptic curves with long arithmetic progressions have large rank. Int. Math. Res.
Not. IMRN 2021, no. 10, 7394-7432.
[15] N. Garcia-Fritz, H. Pasten, Patterns on elliptic curves beyond Bremner’s conjecture. Preprint (2026)
arXiv:2605.14962
[16] Z. Gao, T. Ge, L. K¨uhne, The Uniform Mordell-Lang Conjecture. (2021) to appear in Publ. math. IHES.
[17] J. Harrison, A. Mudgal, H. Schmidt, Uniform sum-product phenomenon for algebraic groups and Bremner’s
conjecture. Preprint (2026) arXiv:2603.06483
[18] B. Mazur, Abelian varieties and the Mordell-Lang conjecture. In: Model Theory, Algebra, and Geometry, Math.
Sci. Res. Inst. Publ. 39, Cambridge Univ. Press, Cambridge, 2000, pp. 199-227.
[19] L. Mordell, On the rational solutions of the indeterminate equations of the third and fourth degrees. Proc. Cam-
bridge Philos. Soc. 21 (1922/23), 179-192.
[20] D. Mumford, A remark on Mordell’s conjecture. Amer. J. Math. 87 (1965), 1007-1016.
[21] J. Park, B. Poonen, J. Voight, M. Wood, A heuristic for boundedness of ranks of elliptic curves. J. Eur. Math.
Soc. (JEMS) 21 (2019), no. 9, 2859-2903.
[22] G. R´emond, D´ecompte dans une conjecture de Lang. Inventiones Mathematicae, (2000) 142 (3), 513-545.
[23] G. R´emond, Sur les sous-vari´et´es des tores. Compositio Mathematica 134.3 (2002) 337-366.
[24] P. Vojta, Siegel’s theorem in the compact case. Annals of Mathematics, 1991, p. 509-548.
[25] J. Yu, X. Yuan, S. Zhou, Quantitativity on the number of rational points in the Mordell conjecture. Preprint
(2026) arXiv:2602.01820

Departamento de Matem´aticas, Pontificia Universidad Cat´olica de Chile. Facultad de Matem´aticas,
4860 Av. Vicu˜na Mackenna, Macul, RM, Chile
Email address, N. Garcia-Fritz: natalia.garcia@uc.cl

Departamento de Matem´aticas, Pontificia Universidad Cat´olica de Chile. Facultad de Matem´aticas,
4860 Av. Vicu˜na Mackenna, Macul, RM, Chile
Email address, H. Pasten: hector.pasten@uc.cl
 6
