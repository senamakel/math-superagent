<!-- source: https://math.mit.edu/~poonen/papers/errata.pdf | converted from PDF -->

REMARKS AND ERRATA

For the book Rational points on varieties, see this separate list.

1. Errors that have not been fixed

Genus-two curves with 22 torsion points.

• The displayed definition of the function f is not the right one for its intended purpose. To
test whether the point (u, v) is torsion, one needs to express the vector of integrals along
γu as a linear combination of both the vector of integrals along Xt(R) and the vector
of integrals along an 1-cycle representing an independent complex-conjugation-invariant
class in H1(X(C), Q), and to define f (t, u) as that pair of coefficients. Probably this new
f still has a 2-dimensional image, but this has not yet been checked, so the proof as it
stands is incomplete.

Lattices in Tate modules.

• The proof of Theorem 1.2(d) claims that V ∩ TW spans TW as a W -module. This is
easy to prove if k = Fp, but it is not clear whether it is true over larger perfect fields
of characteristic p. Therefore in Theorem 1.2(d) one should assume k = Fp, and in
Corollary 1.3 one should assume k = Fp or change “W -basis of M∗(X)” to “K-basis of
M∗(X) ⊗ Q”. (Thanks to Remy van Dobben de Bruyn for noticing the gap.) Also, one
should assume u ∈ End X, not just End
◦ X, for Theorem 1.2(b,d).

2. Significant errors that were fixed

The classification of preperiodic points of quadratic polynomials over Q: a refined
conjecture.

• The proof of Proposition 1 in Section 4 contains an error: the point (2, √
33) is not on C!
Instead (−2, √
33) is; apparently a sign got dropped halfway through the computation.
To complete the 2-descent correctly one must use also the 2-adic information. The end
result of the computation is the same as before, so the main results of the paper still hold.
(Thanks to Ken Kramer for noticing the error.)
• There is typo in the third displayed equation on page 22: The first line should read

(µ, t) ↦→ ( t + µ2 + 3
2(µ − 1)2 , −3µ
3 + µt + t − 5µ
2 + 9µ + 1
2(µ − 1)3
 ) ,

which includes a missing +t in the numerator of the y-coordinate. (Thanks to John Doyle
for noticing this.)

Date: August 14, 2025. 1

The conjugate dimension of algebraic numbers.
• The data in Table 2 was mostly taken from a table in the cited article by Feit. We had
corrected the first row of that table, but Gaël Rémond pointed out to us that Feit’s table
has at least one other omission: for (n, ℓ) = (6, 4), the order of ST8 ≀S3 is 5308416, which
is 9/5 times the general formula ℓ
nn! = 2949120. Thus (6, 4) should be added to the list
of exceptions in our Theorem 15. This is now corrected in the online version, but not in
the printed version.

The moduli space of commutative algebras of finite rank.
• The proof of Lemma 11.1 relies on an invalid argument from [KP70], so the proofs of the
upper bounds in Theorem 11.2 and 11.3 are not complete. The theorems are nevertheless
true: they are proved (with improved error terms) in [BM21]. (Thanks to Simon R.
Blackburn and K. Robin McLean for pointing out the error.)

Isomorphism types of commutative algebras of finite rank over an algebraically
closed field.
• In Case 4b in characteristic 2, the printed version is missing one of the two isomorphism
types.
• Marco Pellegrini and Chiara Tamburini pointed out some redundant entries in Table 1
of the printed version; these arose from an incorrect classification of symmetric bilinear
forms in characteristic 2.
• Richard Rimanyi observed that in Table 1, in the last three of the four entries with
⃗d = (3, 1, 1), the ideal generator z4 is redundant.
All these have been corrected in the online version.

Bertini irreducibility theorems over finite fields.
• Jiayu Zhao pointed out a minor error in one proof in the printed version. It has been
corrected in the online version. The issue was that in the proof of Lemma 5.1 we were
implicitly using Lemma 3.6 of the online version without first reducing to the case of a
normal variety. So we added Lemma 3.6, and rewrote the proof of Lemma 5.1 to work
with the smooth loci (and we also modified Lemma 5.2 slightly).

Statistics of K-groups modulo p for the ring of integers of a varying quadratic
number field.
• In the printed version, the proof of Lemma 2.3 is not correct, because the Hochschild–Serre
spectral sequence requires OF ′[1/p] to be étale over OF [1/p], and it is not necessarily so.
(Thanks to Craig Westerland and David DeMark for pointing this out.) Nevertheless the
statement is true, since one can use Gysin sequences to reduce to the étale case.

3. Typos and minor misstatements

Union-closed families.
• p. 256, Theorem 1, in condition 2: Change F ⊎ G = G to F ⊎ G ⊆ G. A similar change
should be made to the beginning of lines −5 and −3 on p. 257, and to the beginning of
line 6 on p. 260. (Thanks to Theresa Vaughan.)
2

Computational aspects of curves of genus ≥ 2.
• In the printed version, “positive integer g” should be changed to “g ≥ 2” in the statement
of the Shafarevich conjecture in Section 11. The statement “For each number field K
and set of places S, there are at most finitely many genus 1 curves over K with good
reduction outside S” implies that the Shafarevich–Tate group of every elliptic curve over
a number field is finite. The latter is not yet proved.

The number of intersection points made by the diagonals of a regular polygon.
• The published version contains a typo introduced while converting a formula to TEX: in
Theorem 1, the 232 in the formula for I(n) should be 262, as the routines in ngon.m give.
(Thanks to Steve Sommars for noticing this.)

The Cassels–Tate pairing on polarized abelian varieties.
• In the printed version, Section 2 suggests that the maximal divisible subgroup Mdiv of
an abelian group M equals the set of m ∈ M such that for all n ≥ 1 there exists x ∈ M
such that nx = m. This is false in general (the latter set can be larger), but it is true
if the p-torsion subgroup M [p] is finite for each prime p. The latter condition holds for
each group in the paper for which the notation Mdiv is used, so the rest of the paper is
unaffected. (Thanks to Hendrik Lenstra for noticing the error.)

Mordell-Lang plus Bogomolov.
• In the printed version, Remark 1 following Proposition 5 should be replaced by the
following, because heights associated to effective divisors are not guaranteed to be bounded
below for points on the divisor itself. (Thanks to Najmuddin Fakhruddin for noticing
this.)
“Condition (∗) is satisfied for (U, f ) if there exists an integral projective variety V
containing U as an open dense subset, and an ample line bundle L on V such that f
extends to a morphism ¯f : V → V and a height associated to N := ¯f ∗L ⊗ L ⊗−q in
(Pic V ) ⊗ Q is bounded below for some 1 < q ∈ Q. The condition on N is satisfied, for
instance, if N is the pullback of an ample sheaf under some morphism of varieties.”
In the application to semiabelian varieties, one can then take ¯f = [m] for some m ≥ 2,
q = m, and N = L ⊗(m2−m)
1 . The results of the paper still hold.

Algebraic families of nonzero elements of Shafarevich-Tate groups.
• Section 2.6 implicitly assumes that A is principally polarized, which is the case in the
application. If A is a general abelian variety, Y should be a torsor of ˆA, and it is ˆA that
should be identified with Pic
0
X/k. (Thanks to my co-author for noticing this.)

Squarefree values of multivariable polynomials. The following changes should be made
to the printed version:
• In Theorem 3.2 and Lemma 6.2 the condition “xn appears in f (x)” should be strengthened
to “xn appears in each irreducible factor of f (x)”.
• The statement of Theorem 8.1 is OK, but some changes are needed in the proof, since
one cannot ensure that t will be among the tiα at the end. One should remark that in
the generalization of Lemma 7.2 it suffices to have ti/tj /∈ K p for some i, j, and then only
allow subsets {iα1, . . . , iαr} for which the corresponding tiα satisfy this condition on ratios:
this can be done provided deg D is sufficiently large.
3

The William Lowell Putnam Mathematical Competition 1986–2000: problems,
solutions, and commentary.
• The “Related question” on page 68 is wrong. Condition (b) should be replaced by the
hypothesis that all rows and columns of M have the same sum.

Orbits of automorphism groups of fields. In the printed version:
• In the proof of Lemma 1.6, the statement Md = cMd holds but does not follow from the
previous lines of the proof. It was used in the last sentence to show that multiplication-
by-c maps Md isomorphically to cM . Luckily, the latter also follows from Md = cM and
cM = c2M and the fact that cM is torsion-free. (Thanks to E. Mehmet Kiral for noticing
the gap.)
• The first paragraph of the proof of Lemma 2.8 should read as follows:
Since M − N generates M as a module, the sequence (f mM )m≥1 also contains
only finitely many sets. But this sequence is decreasing, so f mM = f m+1M for
some m.
Thanks to P. K. Sharma for noticing the error.

Twists of X(7) and primitive solutions to x2 + y3 = z7.
• In the printed version, in the proof of Lemma 4.6, “twist by 1/3” should be “twist by
−1/3”.

Unramified covers of Galois covers of low genus curves.
• In Remark 1.2 of the printed version, it should be assumed that Y has genus at least 2.
(Thanks to Amador Martin-Pizarro for noticing this.)

Smooth hypersurface sections containing a given subscheme over a finite field.
• The variable b should be c in a few places in the printed version: in “For d ≥ b” in the
proof of Lemma 2.1, and in the statement and proof of Lemma 3.2.

The set of nonsquares in a number field is diophantine.
• In the printed version, the equation at the end of the proof of Corollary 1.2 should be
An+1 = A1 ∪ {t2 : t ∈ An and − t ∈ An}. (Thanks to Jean-Louis Colliot-Thélène for
noticing this.)

Random maximal isotropic subspaces and Selmer groups.
• In the printed version, in the proof of Proposition 2.6(a), “codimension 1 subspaces of W ”
should be “codimension 1 subspaces of W not containing v”. The same extra condition
should be imposed on W1.
• The observation that a Selmer group could be an intersection of maximal isotropic
subspaces in a finite dimensional space (Remark 4.15) appeared earlier in a more limited
context, but with a similar proof. Namely, for elliptic curves E over a number field k with
E[2] ⊂ E(k), the 2-Selmer group Sel2 E was shown to be an intersection of two subspaces
of a finite-dimensional F2-vector space that were maximal isotropic with respect to a
symmetric bilinear pairing (slightly weaker than being maximal isotropic with respect to a
quadratic form): in [CTSSD98], see Proposition 1.2.1 in conjunction with Proposition 1.1.1
and the remark following it. 4

• Warning: The references to “PR11” are to the arXiv version http://arxiv.org/pdf/
1104.2105v1.pdf, not to the published version [PR11].

Average rank of elliptic curves. The following corrections should be made in the printed
version:
• The construction in [BS15, second half of §4.1] of a positive-density family of elliptic
curves in which the root number is equidistributed is actually taken from [Won01, p. 25
and §9], so the latter should have been credited.
• In the first paragraph of §4.2, S(Qp)min should be S(Zp)min. (Thanks to Ruthi Hortsch
for noticing this.)
• In Lemma 4.3, it is necessary to add the hypothesis that f is locally solvable. (Thanks to
Jack Thorne for noticing this.)

Characterizing integers among rational numbers with a universal-existential
formula.
• In the printed version, the third sentence of the second paragraph of the proof of Lemma
2.3 should say “Then Uq = {2x : x ∈ Fq, y ∈ F×
q , and x2 − cy2 = 1}.”
• In the last sentence of the same paragraph, although X has arithmetic genus 1, it may be
singular, so “genus 1” should say “genus ≤ 1”. In any case, X is X ′ − S for some smooth
projective curve X ′ of genus ≤ 1 and finite subscheme S having ≤ 12 geometric points,
so the proof still goes through.
(Thanks to Dion Leijnse for pointing out the errors.)

The moduli space of commutative algebras of finite rank.
• In the printed version, in Remark 6.9, Sn−1 should be replaced by gSng−1, where g is an
element of GLn(Z) that maps ˜Asplit to a based algebra consisting of Asplit with a basis
whose first element is 1. (Thanks to Andrew O’Desky for the correction.)

Using elliptic curves of rank one towards the undecidability of Hilbert’s tenth
problem over rings of algebraic integers.
• In the proof of Lemma 12, in the definition of S, the points P0, P ′, P ′ should be P0, P, P ′.

4. Remarks

Maximally complete fields.
• Irving Kaplansky told me that the residue field part of his “Hypothesis A,” namely the
condition that every polynomial of the form

a0xpn + a1xpn−1 + · · · + an−1xp + anx + an+1

with each ai in the residue field k have a root in k, was shown by Whaples to be equivalent
to the condition that k have no extensions of degree divisible by p. See the “Afterthought”
to “Maximal Fields with Valuations” in [Kap95].
• Laurent Moret-Bailly points out that the argument in Section 4 can be used to construct a
p-adic Mal’cev–Neumann field even if R is not perfect, because there is still a Cohen ring
(complete discrete valuation ring with the prime number p as uniformizer) with residue
field R. 5

The Cassels–Tate pairing on polarized abelian varieties.
• Let X be a smooth projective geometrically integral surface over a finite field of character-
istic p, and let ℓ be a prime not equal to p. The question of Tate in Section 11, whether
a certain antisymmetric pairing on Br(X)nd(ℓ) is always alternating, is now known to
have a positive answer, thanks to Tony Feng [Fen20]. This implies the earlier theorem of
[LLR05] that Br(X) is of square order if it is finite, or even if Br(X)(ℓ) is finite for any
prime ℓ.

Undecidability in number theory.
• The 2008 article mentioned that finding a solution in integers to x3 + y3 + z3 = 33 is an
unsolved problem. Eleven years later, in March 2019, Andrew Booker found the solution

(8866128975287528)
3 + (−8778405442862239)
3 + (−2736111468807040)
3 = 33.

As of December 5, 2020, the smallest positive integer for which it is not known whether it
is a sum of three cubes is 114.

Néron–Severi groups under specialization.
• Here is a more detailed explanation of why the homomorphism Pic X → Pic XK in (3.4)
is an isomorphism. (This came out of a discussion with Kęstutis Česnavičius.)
First, X is smooth over a regular local ring R, so X and XK are regular. This means
that Pic X and Pic XK can be understood as Weil divisor class groups.
Let X → Y → Spec R be the Stein factorization of X → Spec R. Then Y is finite over
Spec R, and Y is the normalization of Spec R in X [SP, Tag 03H0], so Y is a semilocal
Dedekind scheme.
Since X → Spec R is smooth, the special fiber Xk is a disjoint union of irreducible
divisors D of X. Any such D maps to some point y of Y lying above the closed point
of Spec R. Since Y is a semilocal Dedekind ring, y is a principal divisor on Y . Let F be
the fiber of X → Y above y, so F is a principal divisor on X. Now F is contained in
Xk, and F is connected (by definition of Stein factorization), and F contains a connected
component D of Xk (even scheme-theoretically, since Xk is reduced), so F = D. Thus D
is principal. The kernel of Pic X → Pic XK is spanned by the classes of such divisors D,
so Pic X → Pic XK is injective.
It is also surjective, since if E is an irreducible divisor on XK, its Zariski closure in X
is an irreducible divisor of X whose class maps to the class of E.

Modeling the distribution of ranks, Selmer groups, and Shafarevich–Tate groups
of elliptic curves.
• Corollary 1.2 of [GGGR19] proves our Conjecture 6.9.

References

[BS15] Manjul Bhargava and Arul Shankar, Ternary cubic forms having bounded invariants, and the
existence of a positive proportion of elliptic curves having rank 0, Ann. of Math. (2) 181 (2015),
no. 2, 587–621, DOI 10.4007/annals.2015.181.2.4. MR3275847
[BM21] Simon R. Blackburn and K. Robin McLean, Enumerating finite rings, July 28, 2021. Preprint,
arXiv:2107.13215v1 . 6

[CTSSD98] J.-L. Colliot-Thélène, A. N. Skorobogatov, and Peter Swinnerton-Dyer, Hasse principle for pencils
of curves of genus one whose Jacobians have rational 2-division points, Invent. Math. 134 (1998),
no. 3, 579–650, DOI 10.1007/s002220050274. MR1660925 (99k:11095)
[Fen20] Tony Feng, Étale Steenrod operations and the Artin-Tate pairing, Compos. Math. 156 (2020),
no. 7, 1476–1515, DOI 10.1112/s0010437x20007216. MR4122428
[GGGR19] Florence Gillibert, Jean Gillibert, Pierre Gillibert, and Gabriele Ranieri, Selmer groups are
intersection of two direct summands of the adelic cohomology, Bull. Lond. Math. Soc. 51 (2019),
no. 5, 776–786, DOI 10.1112/blms.12274. MR4022425
[Kap95] Irving Kaplansky, Selected papers and other writings, Springer-Verlag, New York, 1995. With an
introduction by Hyman Bass. MR1340874 (97a:01074)
[KP70] Robert L. Kruse and David T. Price, Enumerating finite rings, J. London Math. Soc. (2) 2
(1970), 149–159. MR0251079 (40 #4310)
[LLR05] Qing Liu, Dino Lorenzini, and Michel Raynaud, On the Brauer group of a surface, Invent. Math.
159 (2005), no. 3, 673–676. MR2125738
[PR11] Bjorn Poonen and Eric Rains, Self cup products and the theta characteristic torsor, Math. Res.
Lett. 18 (2011), no. 6, 1305–1318, DOI 10.4310/MRL.2011.v18.n6.a18. MR2915483
[SP] The Stacks Project authors, Stacks project, May 18, 2020. Available at http://stacks.math.
columbia.edu .
[Won01] Siman Wong, On the density of elliptic curves, Compositio Math. 127 (2001), no. 1, 23–54, DOI
10.1023/A:1017514507447. MR1832985 (2002d:11066)

7
