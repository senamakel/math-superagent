<!-- source: https://arxiv.org/pdf/2312.04430 | converted from PDF -->

arXiv:2312.04430v1  [math.AG]  7 Dec 2023
A Summary of Known Bounds on the Essential Dimension and
Resolvent Degree of Finite Groups

Alexander J. Sutherland

As of December 8, 2023

Abstract

We summarize what is currently known about ed(G) and RD(G) for ﬁnite groups G over C (i.e.
in characteristic 0). In Appendix A, we also give an argument which improves the known bound on
RD(PSL(2, F11)).

Contents

1 Introduction 1

2 Upper Bounds on RD(G) 2

3 Lower Bounds on ed(G) 3

4 Summary and Tables 4

A The Case of PSL(2, F11) 5

1 Introduction

The art of solving polynomials has a long and storied history. These investigations have led to a spectrum
of modern frameworks to classify the complexity of phenomena in algebra and geometry; the ends of this
spectrum are essential dimension and resolvent degree.
Using Galois theory, we can reformulate the classical problem

“Determine a simplest formula for the general degree n polynomial.”;

into
 “Determine ed(Sn) and RD(Sn), the essential dimension and resolvent degree of Sn.”;

where Sn denotes the symmetric group on n letters.
Essential dimension and resolvent degree are not deﬁned only for the symmetric group, but for all ﬁnite
groups. Note that for any ﬁnite group G, [FW2019, Lemma 3.2] yields

RD(G) ≤ ed(G) < ∞.

Consequently, we are naturally led to the following question.

Question 1.1 (Main Question). For which ﬁnite groups does RD(G) = ed(G) and for which ﬁnite groups is
RD(G) < ed(G)?

In this short note, we will address what is currently known about Question 1.1. In Section 2, we discuss
the ﬁnite groups G with explicit upper bounds on RD(G) in the literature. In Section 3, we discuss what is
known about ed(G) for the groups given in Section 1. In Section 4, we summarize the answers to Question
1.1. Note that we will not give proofs of the results, but we will indicate where these results can be found.

1

Additional Context For those interested in the history leading to resolvent degree, we refer the reader to
[Sut2022, Chapter 1]. For those interested in a larger-scale perspective on essential dimension and resolvent
degree, we refer the reader to the survey of Reichstein [Rei2021].
For the expert reader, we note that essential dimension and resolvent degree can be (and often are)
considered over arbitrary base ﬁelds and for arbitrary algebraic groups; see [ER2023], for example, where the
essential dimension of the symmetric groups is considered in prime characteristic. However, we restrict our
attention here to the classical case where our base ﬁeld is C and G is a ﬁnite group.

Acknowledgements I would like to thank Daniel Litt for recently asking what is known about Question
1.1, which prompted this expository note. I would like to thank Jesse Wolfson for several helpful comments
on a draft, including providing information on several relevant references.

2 Upper Bounds on RD(G)

For a ﬁnite group G with simple factors G1, . . . , Gs, [FW2019, Theorem 3.3] yields that

RD(G) ≤ max {RD(G1), . . . , RD(Gs)} .

Consequently, the literature has focused on RD(G) when G is a ﬁnite simple group. More speciﬁcally,
there are non-trivial upper bounds on RD(G) in the literature for a ﬁnite simple group G in the following
cases:

1. G is a cyclic group of prime order;

2. G is an alternating group (An, n ≥ 5);

3. G is a simple factor of a Weyl group of type E6, E7, or E8;

4. G = PSL(2, F7) or PSL(2, F11); or

5. G is a sporadic group.

Let us now consider each case individually.

Case 1: It is immediate that RD(G) = 1; it is also a special case of [FW2019, Corollary 3.4]. Indeed,
RD(A) = 1 for any ﬁnite abelian group A.

Case 2: Before stating known bounds, we note that RD(Sn) = RD(An), whereas ed (An) ̸= ed(Sn); we
will say more in Section 3. Bring showed that RD(An) ≤ n − 4 for n ≥ 5 in [Bri1786]. Segre gave a complete
proof that RD(An) ≤ n − 5 for n ≥ 9 in [Seg1945], building upon the work of Hilbert [Hil1927]. Indeed,
all of our bounds come in the form RD(An) ≤ n − m for n greater than some threshold determined by m.
For most values of m ≥ 6, the bounds are given by G(m) in [Sut2021]; see Theorems 3.7, 3.10, and 3.27, or
Appendices 5.1 and 5.2 for a summary. For m ∈ [13, 17] ∪ [22, 25], improvements to G(m) are established in
[HS2023, Theorem 1.1].

Case 3: We denote the simple factors of W (E6), W (E7), and W (E8) by W (E6)
+, W (E7)
+, W (E8)
+,
respectively, and note that in each case RD (W (En)) = RD (W (En)
+). In [FW2019], Theorem 8.2 establishes
RD (W (E6)
+) ≤ 3. In [Rei2022], Proposition 15.1 establishes RD (W (E7)
+) ≤ 4 and RD (W (E8)
+) ≤ 5.

Case 4: The group PSL(2, F7) was investigated classically by Fricke, Klein, and Gordan. We refer the
reader to [FKW2022, Proposition 4.2.4], which establishes that RD(PSL(2, F7)) = 1. Using modern language,
[Kle1879] establishes that RD(PSL(2, F11)) ≤ 3. We will say more in Appendix A, where we outline a proof
that RD(PSL(2, F11)) ≤ 2.
 2

Case 5: The resolvent degree of the sporadic groups was recently investigated by the author in joint work
with G´omez-Gonz´ales and Wolfson. Corollary 4.9 of [GGSW2023] gives the following bounds:

RD(J2) ≤ 5, RD(M24) ≤ 18, RD(He) ≤ 48, RD(Fi23) ≤ 776,
RD(M11) ≤ 6, RD(HS) ≤ 18, RD(J1) ≤ 51, RD(Fi24’) ≤ 779,

RD(M12) ≤ 7, RD(McL) ≤ 19, RD(Fi22) ≤ 74, RD(J4) ≤ 1328,
RD(M22) ≤ 8, RD(Co3) ≤ 20, RD(HN) ≤ 129, RD(Ly) ≤ 2475,

RD(Suz) ≤ 10, RD(Co2) ≤ 20, RD(Th) ≤ 244, RD(B) ≤ 4365,
RD(J3) ≤ 16, RD(Co1) ≤ 21, RD(O’N) ≤ 338, RD(M) ≤ 196874.

RD(M23) ≤ 17, RD(Ru) ≤ 26.

3 Lower Bounds on ed(G)

Let us again address the ﬁve cases outlined in Section 2, where non-trivial upper bounds on RD(G) are
known. The author is not aware of any lower bounds on the essential dimension of the sporadic groups, so
we omit Case 5 here.

Case 1: We follow [BR1997, Section 6.1] and recall that the rank of a ﬁnite abelian group A is the minimal
number of elements that generate A; equivalently, it is the largest r such that (Z/pZ)
r embeds into G for
some prime p. Theorem 6.1 of [BR1997] then yields that

ed(A) = rank(A).

Consequently, when G ∼= Z/pZ, we see that ed(G) = 1.

Case 2: We will discuss both the alternating groups An and the symmetric groups Sn. It was known
classically, e.g. by Felix Klein, that

ed(A2) = ed(A3) = 1, ed(A4) = ed(A5) = 2, ed(A6) = 3.

In [BR1997], Theorem 6.7 further establishes that

1. ed(An+4) ≥ ed(An) + 2 for n ≥ 4,

2. ed(An) ≥ 2⌊ n
4 ⌋ for n ≥ 4.

We now turn to the case of the symmetric groups. Again, it was known classically that

ed(S2) = ed(S3) = 2, ed(S4) = ed(S5) = 2.

Theorem 6.5 of [BR1997] additionally establishes

1. ed(S6) = 3,

2. ed(Sn) ≤ n − 3 for any n ≥ 5,

3. ed(Sn+2) ≥ ed(Sn) + 1 for any n ≥ 1,

4. ed(Sn) ≥ ⌊ n
2 ⌋ for any n ≥ 1.

In [Dun2010], Duncan showed that ed(A7) = ed(S7) = 4 and thus

ed(Sn) ≥ ⌊ n + 1
2
 ⌋ , for n ≥ 7.

As is noted in [ER2023, Section 1], “the exact value of ed(Sn) is open for every n ≥ 8, though it is widely
believed that ed(Sn) should be n − 3 for every n ≥ 5.”

3

Case 3: Duncan classiﬁes the ﬁnite groups of essential dimension 2 in [Dun2013, Theorem 1.1] and, notably,
ed(PSL(2, F7)) = 2. Proposition 4 of [Bea2014] gives the following list of possible ﬁnite simple groups of
essential dimension 3: they are A6 and PSL (2, F11). More speciﬁcally, we know ed(A6) = 3 (as covered
above) and ed(PSL(2, F11)) = 3 or 4.

Case 4: The essential dimension (and essential p-dimension, which we do not discuss here) of ﬁnite pseudo-
relection groups is determined in in [DR2014, Theorem 1.3]. Notably, they establish that ed(W (E6)) = 4,
ed(W (E7) = 7, and ed(W (E8)) = 8. The ﬁrst equality is given explicitly in Theorem 1.3; the second is given
in Remark 7.2; and the third from Example 1.2, as ed(W (E8)) = dim(V ) = a(2).

4 Summary and Tables

We now summarize the numerical results stated above in tables for Cases 1, 2, 3, and 4.

Case 1: Given that the essential dimension of an arbitrary abelian group A is the essential dimension of a
elementary p-subgroup of maximal rank, we focus on the cases of cyclic p-groups and elementary p-groups.

A RD(A) ed(A)
Z/pZ 1 1

(Z/pZ)r 1 r

Note that ed ((Z/pZ)
r) − RD ((Z/pZ)
r) = r − 1, so we can ﬁnd groups where the gap between essential
dimension and resolvent degree is arbitrarily large.

Case 2: We record the relevant values for An and Sn, up to n = 22.

n RD(An) = RD(Sn) ed(An) ed(Sn), known ed(Sn), conjectured
2 1 1 1 N/A
3 1 1 1 N/A
4 1 2 2 N/A
5 1 2 2 N/A
6 ≤ 2 3 3 N/A
7 ≤ 3 4 4 N/A
8 ≤ 4 ≥ 4 ≥ 4 5
9 ≤ 4 ≥ 4 ≥ 4 6
10 ≤ 5 ≥ 4 ≥ 5 7
11 ≤ 6 ≥ 4 ≥ 5 8
12 ≤ 7 ≥ 6 ≥ 6 9
13 ≤ 8 ≥ 6 ≥ 6 10
14 ≤ 9 ≥ 6 ≥ 7 11
15 ≤ 10 ≥ 6 ≥ 7 12
16 ≤ 11 ≥ 8 ≥ 8 13
17 ≤ 12 ≥ 8 ≥ 8 14
18 ≤ 13 ≥ 8 ≥ 9 15
19 ≤ 14 ≥ 8 ≥ 9 16
20 ≤ 15 ≥ 10 ≥ 10 17
21 ≤ 15 ≥ 10 ≥ 10 18
22 ≤ 16 ≥ 10 ≥ 11 19

If true, the conjecture that ed(Sn) = n − 3 for n ≥ 5 would yield that

• ed(Sn) − RD(Sn) ≥ 1 for n ≥ 5,

• ed(Sn) − RD(Sn) ≥ 2 for n ≥ 9,
 4

• ed(Sn) − RD(Sn) ≥ 3 for n ≥ 21,

and so on. In fact, given this conjecture, work as old as [Ham1836] implies that

lim
n!∞ (ed(Sn) − RD(Sn)) = ∞.

For modern references which improve upon Hamilton’s results, see [Wol2021, Theorem 1.1] or [Sut2021,
Theorem 1.3].

Case 3: For PSL(2, F7) and PSL(2, F11), we have the following:

G RD(G) ed(G)
PSL(2, F7) 1 2
PSL(2, F11) ≤ 2 3 or 4

Case 4: For the Weyl groups W (E6), W (E7), and W (E8), we note the following bounds:

G RD(G) ed(G)

W (E6) ≤ 3 4

W (E7) ≤ 4 7

W (E8) ≤ 5 8
 .

A The Case of PSL(2, F11)

In [Kle1879], Klein investigates PSL(2, F11). To do so, Klein considers the four-dimensional projective repre-
sentation P4 of PSL(2, F11) and constructs invariants of degrees 3 (∇), 5 (H), and 11 (C). Using the modern
computer algebra system GAP, one can directly compute the Molien series for the linear representation A5 as
the following rational expression:

1 − z2 + z7 + z8 − z11 + z14 + z15 − z20 + z22

(1 − z11) (1 − z6) (1 − z5) (1 − z3) (1 − z2) .

The series expansion of the Molien series begins:

1 + z3 + z5 + 2z6 + z7 + 2z8 + 3z9 + 3z10 + 4z11 + 6z12 + · · · .

Note that V(∇) ⊆ P4 is a cubic hypersurface in P4 and thus we know classically that it has dense solvable
points. This is enough to establish the Klein’s claim that

RD(PSL(2, F11)) ≤ dim (V(∇)) = 3.

We additionally outline a quick proof of an improved bound. Before we begin, we refer the reader to
[Sut2021, Section 2] for more on polar cones and [GGSW2023, Example 2.16] for more on the notation K (d).

Proof. For every K-point P ∈ K(V(∇)), the polar cone C(V(∇); P ) has

deg(C(V(∇); P )) = 6,

codim(C(V(∇); P )) ≥ 1.

Thus, P lies on a line of V(∇) over K (2), as RD(A6) = RD(S6) ≤ 2. For any such line Λ, we see that
V(∇) ∩ Λ ⊆ V(∇, H) and deg (V(H) ∩ Λ) = 3. Since RD(A3) = RD(S3) = 1 ≤ 2, V(∇, H) also has dense
K (2)-points and we see that
 RD(PSL(2, F11)) ≤ max {2, dim(V(∇, H))} = 2,

if the action of PSL (2, F11) is generically free. Since deg (V(∇, H)) = 10, we see that V(∇, H) has at most
10 irreducible components. Since PSL(2, F11) would act on the irreducible components transitively and the
smallest permuation representation of PSL(2, F11) is on 11 points, we see that V(∇, H) is irreducible and
thus [GGSW2023, Lemma 2.12] yields that the action of PSL(2, F11) on V(∇, H) is generically free.

5

References

[Bea2014] A. Beauville, Finite simple groups of small essential dimension, Trends in contemporary mathe-
matics, Springer INdAM Ser., 8:221-228, 2014.

[Bri1786] Bring, E. Meletemata quædam Mathematica circa Transformationem Æquationum Algebraicarum
(“Some Selected Mathematics on the Transformation of Algebraic Equations”). Lund, 1786.

[BR1997] J. Buhler and Z. Reichstein, On the essential dimension of a ﬁnite group, Compositio Math.,
106(2):159-179, 1997.

[Dun2010] A. Duncan, Essential dimensions of A7 and S7, Math. Res. Lett., 17(2):263-266, 2010.

[Dun2013] A. Duncan, Finite Groups of Essential Dimension 2, Comment. Math. Helv., 88:555-585, 2013.

[DR2014] A. Duncan and Z. Reichstein, Pseudo-reﬂection groups and essential dimension, Lon. Math. Soc.,
II., 90(3):879-902, 2014.

[ER2023] O. Edens and Z. Reichstein, Essential Dimension of Symmetric Groups in Prime Characteristic,
to appear in C. R. Math. Acad. Sci. Paris, 2023.

[FKW2022] B. Farb, M. Kisin, and J. Wolfson, Modular functions and resolvent problems, with an appendix
by Nate Harman, Math. Ann., 2022.

[FW2019] B. Farb, and J. Wolfson, Resolvent degree, Hilbert’s 13th problem and geometry, Enseign. Math.,
65(3-4):303-376, 2019.

[GGSW2023] C. G´omez-Gonz´ales, A. Sutherland, and J. Wolfson, Generalized Versality, Special Points, and
Resolvent Degree for the Sporadic Groups, 2023, arXiv:2310.09375.

[Ham1836] W. Hamilton, Inquiry into the validity of a method recently proposed by George B. Jerrard, esq.,
for transforming and resolving equations of elevated degrees. Report of the Sixth Meeting of the British
Association for the Advancement of Science, 295-348, 1836.

[HS2023] C. Heberle and A. Sutherland, Upper bounds on resolvent degree via Sylvester’s obliteration algo-
rithm, New York J. Math., 29:107-146, 2023.

[Hil1927] D. Hilbert, ¨Uber die Gleichung neunten Grades, Math. Ann., 97(1):243-250, 1927.

[Kle1879] F. Klein, Ueber die Transformation elfter Ordnung der elliptischen Functionen, Math. Ann., 15:533-
555, 1879.

[Kle1884] F. Klein, Vorlesungen ¨uber das Ikosaeder und die Auﬂ¨osung der Gleichungen vom f¨unften Grade,
Teubner, Leipzig, 1884

[Mor1956] G.G. Morrice, English translation: Lectures on the icosahedron and solution of equations of the
ﬁfth degree, 2nd and rev. edition, Dover Pub., New York, NY, 1956.

[Rei2021] Z. Reichstein, From Hilbert’s 13th problem to essential dimension and back, Eur. Math. Soc. Mag.,
122:4-15, 2021.

[Rei2022] Z. Reichstein, Hilbert’s 13th Problem for Algebraic Groups, to appear in Enseign. Math.

[Seg1945] B. Segre, The Algebraic Equations of Degree 5, 9, 157..., and the Arithmetic Upon an Algebraic
Variety, Ann. of Math., 46(2):287-301, 1945.

[Sut2021] A. Sutherland, Upper Bounds on Resolvent Degree and Its Growth Rate, 2021, arXiv:2107:.08139.

[Sut2022] A. Sutherland, Upper Bounds on the Resolvent Degree of General Polynomials and the Families of
Alternating and Symmetric Groups, UC Irvine. ProQuest ID: Sutherland uci 0030D 17672. Merritt ID:
ark:/13030/m5c321dc. Retrieved from https://escholarship.org/uc/item/7vp7k5zm.

[Wol2021] J. Wolfson, Tschirnhaus transformations after Hilbert, Enseign. Math., 66(3):489-540, 2021.

6
