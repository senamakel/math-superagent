<!-- source: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v24i3p25/pdf/ | converted from PDF -->

Frankl’s Conjecture for subgroup lattices

Alireza Abdollahi∗

Department of Mathematics, University of Isfahan,
Isfahan, 81746-73441, Iran; and

School of Mathematics, Institute for Research in Fundamental Sciences (IPM),
P.O. Box 19395-5746, Tehran, Iran

a.abdollahi@math.ui.ac.ir
http://sci.ui.ac.ir/∼a.abdollahi

Russ Woodroofe

Department of Mathematics & Statistics,
Mississippi State University, MS 39762, USA; and

UP FAMNIT, University of Primorska,
Glagolja˘ska 8, 6000 Koper, Slovenia

russ.woodroofe@famnit.upr.si
http://osebje.famnit.upr.si/∼russ.woodroofe/
 Gjergji Zaimi

gjergjiz@gmail.com

Submitted: Jun 25, 2016; Accepted: Jul 25, 2017; Published: Aug 11, 2017
Mathematics Subject Classiﬁcations: 05D05, 06A07, 06C15, 20E15.

Abstract
We show that the subgroup lattice of any ﬁnite group satisﬁes Frankl’s Union-
Closed Conjecture. We show the same for all lattices with a modular coatom, a
family which includes all supersolvable and dually semimodular lattices. A common
technical result used to prove both may be of some independent interest.

1 Introduction

1.1 Frankl’s Conjecture

All groups and lattices considered in this paper will be ﬁnite. An element of a lattice is
a join-irreducible if it cannot be written as the join of strictly lesser elements. We will
examine the following conjecture, attributed to Frankl from 1979.

∗Supported in part by grant No. 95050219 from School of Mathematics, Institute for Research in
Fundamental Sciences (IPM), and by the Center of Excellence for Mathematics at the University of
Isfahan.

the electronic journal of combinatorics 24(3) (2017), #P3.25 1

Conjecture 1.1 (Frankl’s Union-Closed Conjecture). If L is a lattice with at least 2
elements, then there is a join-irreducible a with ∣
∣[a, ˆ1]
∣
∣ ⩽ 1
2 |L|.

There are a number of diﬀerent equivalent forms of this conjecture. The original form
that Frankl considered involved a related condition for families of sets that are closed
under intersection. The ﬁrst appearance in print was in the conference proceedings [26],
arising from its mention by Duﬀus in a problem session. Three forms of the problem
are given in [26]: a statement about families of sets closed under union, Frankl’s original
form, and the lattice statement as we have here. Conjecture 1.1 appears as a 5-diﬃculty
problem in [30], where it is called a “diabolical” problem. See [6] for further information
and history. The conjecture has been the subject of a Polymath project [4].
We will henceforth refer to Conjecture 1.1 as Frankl’s Conjecture. We will focus on the
lattice form. If we wish to refer to the join-irreducible a satisfying the required condition,
we will say that L satisﬁes Frankl’s Conjecture with a.
Frankl’s Conjecture, while open in general, is known to hold for many families of
lattices. Poonen in [24] proved and generalized remarks of Duﬀus from [26]: namely, that
the conjecture holds for distributive lattices, and for relatively complemented (including
geometric) lattices. Reinhold [25] showed the conjecture to hold for dually semimodular
lattices (see also [1, 29]). Whether the conjecture holds for semimodular lattices is in
general unknown, but Cz´edli and Schmidt in [10] veriﬁed it for semimodular lattices that
have a high ratio of elements to join-irreducibles. Joshi, Waphare, and Kavishwar have
recently in [14] shown the conjecture to hold for dismantlable lattices.
We remark that Blinovsky has an arXiv preprint which claims to settle the Frankl
Conjecture. However: his argument is diﬃcult to follow, and has gone through a large
number of arXiv versions in a short time. Moreover, he has also claimed to solve several
other diﬃcult conjectures in a short period, using the same technique. There does not
seem at this time to be a consensus that his proof is correct.

1.2 Subgroup lattices

Recall that for a group G, the subgroup lattice of G is the set L(G) of all subgroups of G,
ordered by inclusion.
Our ﬁrst main theorem veriﬁes that Frankl’s Conjecture holds for subgroup lattices.

Theorem 1.2. If G is a group and L(G) is the subgroup lattice of G, then L(G) satisﬁes
Conjecture 1.1.

Subgroup lattices of groups form a large family of lattices. Indeed, it is an important
open question (ﬁrst asked by P´alfy and Pudl´ak [22]) as to whether every ﬁnite lattice
occurs as an interval in the subgroup lattice of some ﬁnite group. Although most experts
on the topics appear to believe the answer to the P´alfy-Pudl´ak question to be negative,
progress has been somewhat limited. Indeed, the problem is diﬃcult [5] even for lattices
of height 2! See [2] and its references for further discussion of the P´alfy-Pudl´ak question
and attempts to disprove it.

the electronic journal of combinatorics 24(3) (2017), #P3.25 2

In light of the question of P´alfy and Pudl´ak, it would be highly interesting to settle
Frankl’s Conjecture in intervals of the form [H, G] of L(G). We cannot do this in general,
but give group-theoretic suﬃcient conditions. We will state these conditions carefully in
Corollary 1.5. We also verify that Frankl’s Conjecture holds for every interval in a solvable
group in Corollary 1.10.

1.3 Modular elements, subgroup lattices, and Frankl’s Conjecture

An essential tool in the proof of Theorem 1.2 also has applications to many other lattices.
For this reason, we give it in a quite general form.
An element m of a lattice L is left-modular if for every a < b in L, the expression
a ∨ m ∧ b can be written without parentheses. That is, if a ∨ (m ∧ b) = (a ∨ m) ∧ b for
every a < b. We show:

Theorem 1.3 (Main Technical Theorem). Let L be a lattice, let m ∈ L \ {ˆ1} be left-
modular, and let x, y ∈ L be (not necessarily distinct) join-irreducibles. If m ∨ x ∨ y = ˆ1,
then L satisﬁes Frankl’s Conjecture with either x or y.

It follows from the well-known Dedekind Identity (see Section 2.1 below) that any
normal subgroup N of G is left-modular in L(G). It is straightforward to see that a
subgroup X is a join-irreducible in L(G) if and only if X is cyclic of prime-power order.
Thus, we obtain the following as an easy consequence of Theorem 1.3.

Corollary 1.4. If G is a group with a normal subgroup N ▹ G, such that G/N is generated
by at most two elements of prime-power order, then L(G) satisﬁes Frankl’s Conjecture.

The proof of Theorem 1.2 will be obtained by combining Corollary 1.4 with results on
ﬁnite simple groups.
We similarly obtain a relative version for upper intervals in groups. The statement
is somewhat harder to work with, as we are not aware of any short description for join-
irreducibles in intervals of subgroup lattices.

Corollary 1.5. Let G be a group and H be a subgroup. If X and Y are join-irreducibles
of the interval [H, G], and N ▹ G is such that HN < G but HN ∨ X ∨ Y = G, then the
interval [H, G] satisﬁes Frankl’s Conjecture.

1.4 The Averaged Frankl’s Condition

A related question to Frankl’s Conjecture asks for which lattices the average size over a
join-irreducible element (other than ˆ0) is at most 1
2 |L|. We call this condition the Averaged
Frankl’s Condition. The Averaged Frankl’s Condition does not hold for all lattices, but
is known to hold for lattices with a large ratio of elements to join-irreducibles [9]. The
condition obviously holds for uncomplicated subgroup lattices such as L(Zpn) or L(Z
n
p ).
Indeed, our techniques allow us to show a stronger condition for a restrictive class of
groups.

the electronic journal of combinatorics 24(3) (2017), #P3.25 3

Proposition 1.6. If G is a supersolvable group in which all Sylow subgroups are elemen-
tary abelian, then G satisﬁes Frankl’s Conjecture with any join-irreducible X.

Supersolvable groups with elementary abelian subgroups are also known as complemented
groups, and were ﬁrst studied by Hall [12]. We don’t know whether the subgroup lattices
of arbitrary groups satisfy the Averaged Frankl’s Condition.

1.5 Other lattices

Left-modular elements also occur in lattices from elsewhere in combinatorics. A situation
that is both easy and useful is:

Corollary 1.7. If a lattice L has a left-modular coatom m, then L satisﬁes Frankl’s
Conjecture.

Proof. If ˆ1 is a join-irreducible, then the result is trivial. Otherwise, there is some join-
irreducible x such that m ∨ x = ˆ1, and we apply Theorem 1.3.

Remark 1.8. Shewale, Joshi, and Kharat prove [29, Theorem 2] that if every coatom of a
lattice L is left-modular, then L satisﬁes Frankl’s Conjecture. Indeed, a similar technique
is already applied by Reinhold in [25]. After submission of this paper, we learned that
the Shewale, Joshi, and Kharat go on to remark [29, Remark 2] that the same argument
yields (a more general result than) Corollary 1.7.
There has been much study of classes of lattices that have a left-modular coatom.
Dually semimodular lattices have every coatom left-modular, so we recovery the earlier-
mentioned result [25] that such lattices satisfy Frankl’s Conjecture. We also obtain the new
result that supersolvable and left-modular lattices (those with a maximal chain consisting
of left-modular elements) satisfy Frankl’s Conjecture. See e.g. [20] for background on
supersolvable lattices.
Still more generally, the comodernistic lattices recently examined by the second author
and Schweig [28] are those lattices with a left-modular coatom on every interval. This
class of lattices includes all supersolvable, left-modular, and dually semimodular lattices.
It also includes other large classes of examples, including subgroup lattices of solvable
groups and k-equal partition lattices.

Theorem 1.9. Comodernistic lattices (including supersolvable, left-modular, and dually
semimodular lattices) satisfy Frankl’s Conjecture.

Subgroup lattices of solvable groups are one family of examples of comodernistic lat-
tices [28, Theorem 1.7]. That is, every interval in the subgroup lattice of a solvable group
has a left-modular coatom. It follows immediately that:

Corollary 1.10. If G is a solvable group, then every interval in L(G) satisﬁes Frankl’s
Conjecture.

Since the ˆ0 element of any lattice is left-modular, Theorem 1.3 also yields the following:

Corollary 1.11. If L is a lattice such that ˆ1 = x ∨ y for join-irreducibles x, y, then L
satisﬁes Frankl’s Conjecture.

the electronic journal of combinatorics 24(3) (2017), #P3.25 4

1.6 Organization

In Section 2 we will discuss the group-theoretic aspects of the problem. We will complete
the proof of Corollary 1.4 and Theorem 1.2, pending only on the proof of Theorem 1.3.
In Section 3, we will prove Theorem 1.3 and generalizations, as well as Proposition 1.6.

Acknowledgements

We would like to thank the administrators and community of MathOverﬂow, which
brought us together to work on the problem [3]. We also thank Tobias Fritz and Marco
Pellegrini for carefully reading earlier drafts. Marco Pellegrini in particular provided us
with additional background on generation of Suzuki groups, including the useful reference
to [11]. We thank the anonymous referee for her/his thoughtful comments.

2 Groups, generation, and subgroup lattices

The main purpose of this section is to prove Theorem 1.2, as we do in Section 2.3. We
ﬁrst begin with some basic background on the combinatorics of subgroup lattices.

2.1 Modular elements in subgroup lattices

We ﬁrst recall the well-known Dedekind Identity (see [27, 1.3.14] or [13, Exercise 2.9]):

Lemma 2.1 (Dedekind Modular Identity). If H, K, N are subgroups of a group G such
that H ⩽ K, then H(N ∩ K) = HN ∩ K.

It is also well known that HN is a subgroup of G if and only if HN = N H = H ∨ N .
These conditions are obviously satisﬁed when N is a normal subgroup, and are sometimes
otherwise satisﬁed.
It is thus immediate from the Dedekind Identity that whenever HN is a subgroup, we
also have that N satisﬁes the modular relation with H and any K > H. In particular, we
recover our earlier claim that normal subgroups are left-modular in L(G).

2.2 Proof of Corollary 1.4

Corollary 1.4 follows from the left-modularity of a normal subgroup N , together with
another routine exercise: If x and y are elements of prime-power order in G/N , then
there are x, y ∈ G of prime-power order such that x = N x, y = N y [13, Exercise 3.12].
In particular, the modular subgroup N and the join-irreducibles ⟨x⟩ and ⟨y⟩ satisfy the
conditions of Theorem 1.3.
Corollary 1.5 follows by a similar argument.

the electronic journal of combinatorics 24(3) (2017), #P3.25 5

2.3 Proof of Theorem 1.2

In order to prove Theorem 1.2, we will need a result on ﬁnite simple groups. King recently
proved the following in [15].

Theorem 2.2 (Prime Generation Theorem [15]). If G is any nonabelian ﬁnite simple
group, then G is generated by an involution and an element of prime order.

We now complete the proof of Theorem 1.2. Whenever N is a maximal normal sub-
group of G, the quotient G/N is simple. Of course, abelian simple groups are generated by
a single element of prime order. Nonabelian simple groups are handled by Theorem 2.2.
Theorem 1.2 now follows from Corollary 1.4.

2.4 Overview of generation of simple groups by elements of prime order

The substantive work of King [15] in proving Theorem 2.2 builds on a large body of
preceding work. We will brieﬂy survey some history and mathematical details. We assume
basic knowledge of the Classiﬁcation of Finite Simple Groups in this discussion, but will
not assume any such elsewhere in the paper.

Deﬁnition 2.3. A group G is said to be (p, q)-generated if G is generated by an element
of order p and one of order q.

The case of (2, 3)-generation is particularly well-studied in the literature. Such groups
are exactly the quotients (having order at least 6) of the inﬁnite group P SL2(Z). There is
also a connection with automorphism groups of compact Riemann surfaces [8]. In addition
to the references below, see e.g. [23, 31] for more background on (2, 3)-generation.
The following has been known to hold for some time.

Proposition 2.4. With at most ﬁnitely many exceptions, every nonabelian ﬁnite simple
group is either (2, 3)- or (2, 5)-generated.

We summarize the history behind Proposition 2.4. The alternating group An was
shown to be (2, 3)-generated by Miller [21] for n ̸= 6, 7, 8; while A6, A7 and A8 are easily
seen to be (2, 5)-generated. Excluding the groups P Sp4(q), all but ﬁnitely many of the
classical groups are (2, 3)-generated by work of Liebeck and Shalev [16]. In the same
paper [16], the authors showed that, excluding ﬁnitely many exceptions, in characteristic
2 or 3 the groups P Sp4 are (2, 5)-generated. Cazzola and Di Martino in [7] showed
P Sp4 to be (2, 3)-generated in all other characteristics. L¨ubeck and Malle [17] (building
on earlier work by Malle [18, 19]) showed all simple exceptional groups excluding the
Suzuki groups to be (2, 3)-generated. Evans [11] showed the Suzuki groups to be (2, p)-
generated for any odd prime p dividing the group order, and in particular to be (2, 5)-
generated. Proposition 2.4 now follows by combining the results enumerated here with
the Classiﬁcation of Finite Simple Groups.
We caution that P SU3(3
2) is known not to be (2, 3)-generated [32], and since it has
order |P SU3(3
2)| = 2
5 · 3
3 · 7, the group is certainly not (2, 5)-generated either.
King’s proof of Theorem 2.2 proceeds by showing that every classical simple group G
is either (2, 3)-, (2, 5)-, or (2, r)-generated, where r is a so-called Zsigmondy prime for G.

the electronic journal of combinatorics 24(3) (2017), #P3.25 6

3 Proof of Theorem 1.3

Since m ̸= ˆ1, we see that x ∨ y ̸⩽ m. If x ⩽ m, then we may replace the triple m, x, y with
m, y, y while still meeting the conditions of the theorem. Thus, we may suppose without
loss of generality that neither x nor y is on the interval [ˆ0, m].
Suppose without loss of generality that [x, ˆ1] has at most as many elements as [y, ˆ1].
We will show that ∣
∣[x, ˆ1]
∣
∣ ⩽ 1
2 |L| by constructing an injection from [x, ˆ1] to its complement
in L.
We construct this injection in two stages. First, since ∣
∣[x, ˆ1]
∣
∣ ⩽ ∣
∣[y, ˆ1]
∣
∣, there is an
injection ϕ1 that maps
 ϕ1 : [x, ˆ1] \ [x ∨ y, ˆ1] → [y, ˆ1] \ [x ∨ y, ˆ1].

(We notice that if x = y, then x ∨ y = x = y, and this will cause no trouble in our
argument.) We then consider the map

ϕ2 : [x ∨ y, ˆ1] → [ˆ0, m]
α ↦→ m ∧ α.

As x ∨ y ∨ (m ∧ α) = (x ∨ y ∨ m) ∧ α = ˆ1 ∧ α = α by left-modularity, the map ϕ2 is an
injection. Since x ̸⩽ m, the image of ϕ2 is contained in the complement of [x, ˆ1].
The two maps ϕ1, ϕ2 have disjoint domains. Combining them yields the desired injec-
tion.

3.1 Generalizations

Examining our proof of Theorem 1.3, we observe that we do not use the full power of
left-modularity, but only that m satisﬁes the left-modular relation for any α > x ∨ y.
Thus, we have actually proved the following generalization:

Proposition 3.1. Let L be a lattice, and let x, y ∈ L be (not necessarily distinct) join-
irreducibles. If m ∈ L \ {ˆ1} satisﬁes (x ∨ y ∨ m) ∧ α = (x ∨ y) ∨ (m ∧ α) for any α > x ∨ y,
and m ∨ x ∨ y = ˆ1, then L satisﬁes Frankl’s Conjecture with either x or y.

While the statement of Proposition 3.1 appears notably more complicated than that
of Theorem 1.3, it yields a reasonably uncomplicated corollary for intervals in subgroup
lattices.

Corollary 3.2. Let G be a group, let H < G, and let X, Y be join-irreducibles of [H, G].
If there is a subgroup K with H < K < G such that K(X ∨ Y ) = G, then the interval
[H, G] satisﬁes Frankl’s Conjecture.

We in particular are now able to prove Proposition 1.6.

Proof (of Proposition 1.6). It follows by a theorem of Hall [12] that for every subgroup H
in G, there is some subgroup K such that KH = G and H ∩ K = 1. The result follows
by combining the theorem of Hall with Corollary 3.2.

the electronic journal of combinatorics 24(3) (2017), #P3.25 7

References

[1] Tetsuya Abe and Bumpei Nakano, Lower semimodular types of lattices: Frankl’s
conjecture holds for lower quasi-semimodular lattices, Graphs Combin. 16 (2000),
no. 1, 1–16.
[2] Michael Aschbacher, Overgroup lattices in ﬁnite groups of Lie type containing a
parabolic, J. Algebra 382 (2013), 71–99.
[3] Various authors, A group-theoretic perspective on Frankl’s union closed problem,
MathOverﬂow, http://mathoverflow.net/q/154025.
[4] , Polymath11 – FUNC, https://gowers.wordpress.com/2016/01/21/
frankls-union-closed-conjecture-a-possible-polymath-project/.
[5] Robert Baddeley and Andrea Lucchini, On representing ﬁnite lattices as intervals in
subgroup lattices of ﬁnite groups, J. Algebra 196 (1997), no. 1, 1–100.
[6] Henning Bruhn and Oliver Schaudt, The journey of the union-closed sets conjecture,
Graphs Combin. 31 (2015), no. 6, 2043–2074.
[7] M. Cazzola and L. Di Martino, (2, 3)-generation of PSp(4, q), q = pn, p ̸= 2, 3,
Results Math. 23 (1993), no. 3-4, 221–232.
[8] Marston Conder, Hurwitz groups: a brief survey, Bull. Amer. Math. Soc. (N.S.) 23
(1990), no. 2, 359–370.
[9] G´abor Cz´edli, On averaging Frankl’s conjecture for large union-closed-sets, J. Com-
bin. Theory Ser. A 116 (2009), no. 3, 724–729.
[10] G´abor Cz´edli and E. Tam´as Schmidt, Frankl’s conjecture for large semimodular and
planar semimodular lattices, Acta Univ. Palack. Olomuc. Fac. Rerum Natur. Math.
47 (2008), 47–53.
[11] Martin J. Evans, A note on two-generator groups, Rocky Mountain J. Math. 17
(1987), no. 4, 887–889.
[12] Philip Hall, Complemented groups, J. London Math. Soc. 12 (1937), 201–204.
[13] I. Martin Isaacs, Algebra: a graduate course, Graduate Studies in Mathematics, vol.
100, American Mathematical Society, Providence, RI, 2009.
[14] Vinayak Joshi, B. N. Waphare, and S. P. Kavishwar, A proof of Frankl’s union-
closed sets conjecture for dismantlable lattices, Algebra Universalis 76 (2016), no. 3,
351–354.
[15] Carlisle S. H. King, Generation of ﬁnite simple groups by an involution and an ele-
ment of prime order, J. Algebra 478 (2017), 153–173, arXiv:1603.04717.
[16] Martin W. Liebeck and Aner Shalev, Classical groups, probabilistic methods, and the
(2, 3)-generation problem, Ann. of Math. (2) 144 (1996), no. 1, 77–125.
[17] Frank L¨ubeck and Gunter Malle, (2, 3)-generation of exceptional groups, J. London
Math. Soc. (2) 59 (1999), no. 1, 109–122.
[18] Gunter Malle, Hurwitz groups and G2(q), Canad. Math. Bull. 33 (1990), no. 3, 349–
357.

the electronic journal of combinatorics 24(3) (2017), #P3.25 8

[19] , Small rank exceptional Hurwitz groups, Groups of Lie type and their geome-
tries (Como, 1993), London Math. Soc. Lecture Note Ser., vol. 207, Cambridge Univ.
Press, Cambridge, 1995, pp. 173–183.
[20] Peter McNamara and Hugh Thomas, Poset edge-labellings and left modularity, Euro-
pean Journal of Combinatorics 27 (2006), no. 1, 101–113, arXiv:math.CO/0211126.
[21] G. A. Miller, On the groups generated by two operators, Bull. Amer. Math. Soc. 7
(1901), no. 10, 424–426.
[22] P´eter P´al P´alfy and Pavel Pudl´ak, Congruence lattices of ﬁnite algebras and intervals
in subgroup lattices of ﬁnite groups, Algebra Universalis 11 (1980), no. 1, 22–27.
[23] Marco Antonio Pellegrini and Maria Clara Tamburini, Finite simple groups of low
rank: Hurwitz generation and (2, 3)-generation, Int. J. Group Theory 4 (2015), no. 3,
13–19.
[24] Bjorn Poonen, Union-closed families, J. Combin. Theory Ser. A 59 (1992), no. 2,
253–268.
[25] J¨urgen Reinhold, Frankl’s conjecture is true for lower semimodular lattices, Graphs
Combin. 16 (2000), no. 1, 115–116.
[26] Ivan Rival (ed.), Graphs and order, NATO Advanced Science Institutes Series C:
Mathematical and Physical Sciences, vol. 147, D. Reidel Publishing, Dordrecht, 1985,
[27] Derek J. S. Robinson, A course in the theory of groups, Graduate Texts in Mathe-
matics, vol. 80, Springer-Verlag, New York, 1996.
[28] Jay Schweig and Russ Woodroofe, A broad class of shellable lattices, Adv. Math. 313
(2017), 537–563, arXiv:1604.03115.
[29] R. S. Shewale, Vinayak Joshi, and V. S. Kharat, Frankl’s conjecture and the dual
covering property, Graphs Combin. 25 (2009), no. 1, 115–121.
[30] Richard P. Stanley, Enumerative combinatorics. Vol. 2, Cambridge Studies in Ad-
vanced Mathematics, vol. 62, Cambridge University Press, Cambridge, 1999.
[31] M. A. Vsemirnov, More classical groups which are not (2, 3)-generated, Arch. Math.
(Basel) 96 (2011), no. 2, 123–129.
[32] Ascher Wagner, The minimal number of involutions generating some ﬁnite three-
dimensional groups, Boll. Un. Mat. Ital. A (5) 15 (1978), no. 2, 431–439.

the electronic journal of combinatorics 24(3) (2017), #P3.25 9
