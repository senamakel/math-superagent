<!-- source: https://arxiv.org/pdf/2406.09364 | converted from PDF -->

arXiv:2406.09364v2  [math.NT]  4 Sep 2024
ON THE EXISTENCE OF MAGIC SQUARES OF POWERS

NICK ROME AND SHUNTARO YAMAGISHI

Abstract. For any d ⩾ 2, we prove that there exists an integer n0(d) such that there
exists an n × n magic square of d
th powers for all n ⩾ n0(d). In particular, we establish the
existence of an n × n magic square of squares for all n ⩾ 4, which settles a conjecture of
V´arilly-Alvarado.
All previous approaches had been based on constructive methods and the existence of
n × n magic squares of d
th powers had only been known for sparse values of n. We prove our
result by the Hardy-Littlewood circle method, which in this setting essentially reduces the
problem to ﬁnding a suﬃcient number of disjoint linearly independent subsets of the columns
of the coeﬃcient matrix of the equations deﬁning magic squares. We prove an optimal (up
to a constant) lower bound for this quantity.

1. Introduction

Let n ⩾ 1 be an integer. A magic square is an n × n grid of distinct positive integers whose
columns, rows, and two major diagonals all sum to the same number. The number to which
all rows, columns and diagonals sum is known as the square’s magic constant.
Magic squares have a long and rich history. Legend has it that the earliest recorded
3 × 3 magic square was ﬁrst observed by Emperor Yu on the shell of a sacred turtle, which
emerged from the waters of the Lo River [Cam60, pp.118]. Since then magic squares have
appeared in various cultures, and have been an object of curiosity in art, philosophy, religion
and mathematics. The study of magic squares with additional structure is a topic that has
garnered great interest in both recreational and research mathematics.
The ﬁrst 4 × 4 magic square of squares (Figure 1) was constructed by Euler, in a letter sent
to Lagrange in 1770. Though Euler did not provide any explanation of how he constructed
the square, he presented his method to the St. Petersburg Academy of Sciences the same
year; the construction is based on the observation that the product of two sums of four
squares can itself be expressed as a sum of four squares. This idea was used in 1754 by Euler
to make partial progress, which led Lagrange, in the same year as the letter, to the ﬁrst
complete proof of the four square theorem: every positive integer is the sum of at most four
squares [Boy05, VA21].
 682 292 412 372

172 312 792 322

592 282 232 612

112 772 82 492

Figure 1. Euler’s 4 × 4 magic square of squares with magic constant 8515.

The search for a 3 × 3 magic square of squares was popularized by Martin Gardner in
1996 oﬀering a $100 prize to the ﬁrst person to construct such a square, though the problem
1

2 NICK ROME AND SHUNTARO YAMAGISHI

had already been posed by Edouard Lucas in 1876 and Martin LaBar in 1984 [Boy05, VA21].
Despite the great interest and eﬀorts, the prize remains unclaimed (as do the e100 and bottle
of champagne oﬀered by Boyer [Boy] for the same problem). However, there are number of
results making progress on this problem, for which a comprehensive list can be found in [Boy].
A 3 × 3 magic square of squares gives rise to a rational point with nonzero coordinates on a
surface cut out by 6 quadrics in the space P8. A deep conjecture of Lang predicts that this
surface contains only ﬁnitely many curves of genus 0 or 1, and that outside of these curves
it has only ﬁnitely many rational points. The method of [BTVA22] establishes that indeed
this surface contains only ﬁnitely many curves of genus 0 or 1. In fact, we know the surface
contains curves of genus 0 or 1 which do not correspond to magic squares (for instance, lines
parametrising repeated entries). Therefore, it seems plausible that perhaps there are no 3 × 3
magic squares of squares, or that they are remarkably rare.
An n × n magic square of squares corresponds to a rational point on a variety cut out by
2n quadrics in the space Pn2−1. In contrast to the n = 3 case, it is quite reasonable from a
geometric point of view that these spaces would carry many rational points for n ⩾ 5 [VA21].
This line of logic has led V´arilly-Alvarado to make the following conjecture.

Conjecture 1.1 ([VA21, Conjecture 4.3]). There is a positive integer n0(2) such that for
every integer n ⩾ n0(2), there exists an n × n magic square of squares.

In the light of Euler’s example above, V´arilly-Alvarado further suggested that the conjec-
ture holds with n0(2) = 4. We establish that this is indeed the case.

Theorem 1.2. For every integer n ⩾ 4, there exists an n × n magic square of squares.

In fact, we also establish a generalisation of the conjecture for higher powers.

Theorem 1.3. Let d ⩾ 3. There is a positive integer n0(d) such that for every integer
n ⩾ n0(d), there exists an n × n magic square of dth powers.

The novel feature of our work, in comparison to prior work on magic squares in the liter-
ature, is that we are applying the Hardy-Littlewood circle method to a problem, for which
all previous results had been based on constructive methods (see Remark 1.4 regarding the
independent work by Flores [Flo]). In particular, our result is non-constructive. We believe
this is the ﬁrst1 instance, in the literature, of the circle method being applied to study magic
squares. Prior to our result, the existence of n × n magic squares of dth powers was only
known for sparse values of n when d ⩾ 4 (for n = qd with q ⩾ 2 and additionally for small
values of n when 4 ⩽ d ⩽ 7), and the existence was also known for n in certain congruence
classes when d ∈ {2, 3}, while we establish the result for all n ⩾ n0(d). We present a more
detailed account of the progress on this topic in Section 1.1.
As it can be seen from the proof, the statement of Theorem 1.3 in fact holds with

n0(d) =
 {
4 min{2d, d(d + 1)} + 20 if 3 ⩽ d ⩽ 4,
4⌈d(log d + 4.20032)⌉ + 20 if d ⩾ 5. (1.1)

It is worth mentioning that the smallest known example of magic squares of dth powers was
of size 2d for d ⩾ 8; therefore, we improve on the smallest size of magic squares of dth powers
known to exist from 2d to n0(d) as in (1.1) for d ⩾ 9.

1Here we only mean in terms of magic squares with our deﬁnition. In a broader sense, as explained in
Remark 1.4, it is second to Flores’ paper which appeared on the arXiv on 12/6/2024 while our original version
on 13/6/2024.
 ON THE EXISTENCE OF MAGIC SQUARES OF POWERS 3

The main challenge in applying the circle method to the equations deﬁning magic squares
is that they deﬁne a variety which is “too singular” for the method to be directly applicable;
this is explained in Section 1.2. Though we can not apply the results for systems of general
homogeneous forms by Birch [Bir62] and Rydin Myerson [RM18], we can apply the version
available for systems of diagonal forms by Br¨udern and Cook [BC92]. However, this result
requires certain “partitionability” of the coeﬃcient matrix, which amounts to ﬁnding a suﬃ-
cient number of disjoint linearly independent subsets of the columns of the coeﬃcient matrix;
establishing this is the main technical challenge of the paper. We prove an optimal (up to a
constant) lower bound for this quantity in Theorem 2.2. In this context, the circle method
allow us to transform the problem of considerable complexity of ﬁnding magic squares of dth

powers to a theoretically and computationally simpler problem of ﬁnding disjoint linearly
independent subsets of the columns of the coeﬃcient matrix. We expect that this lower
bound will be particularly useful for studying other variants of magic squares. We believe
that our Theorems 1.2 and 1.3 are a signiﬁcant step towards the complete classiﬁcation of
the existence of n × n magic squares of dth powers.

1.1. Progress on magic squares of powers. An n × n magic square is a d-multimagic
square if it remains a magic square when all the entries are raised to the i
th power for every
i = 2, . . . , d. It is called a normal d-multimagic square if it is a d-multimagic square with
entries consisting of the numbers 1 up to d2. Clearly a normal d-multimagic square provides
an example of a magic square of dth powers. The ﬁrst published 2-multimagic squares,
which were of sizes 8 × 8 and 9 × 9, were obtained by Pfeﬀermann in 1890. The ﬁrst 3-
multimagic square was obtained in 1905 by Tarry. In fact, Tarry was the ﬁrst to devise a
systematic method of constructing 2-mulitmagic and 3-multumagic squares [Kee11]. Prior
to our Theorem 1.3, all known examples of magic squares of dth powers for d ⩾ 8 in fact
came from multimagic squares. For 2-multimagic squares it was proved by Chen, Li, Pan
and Xu [PLCX21] that there exists a 2m × 2m normal 2-multimagic squares for all m ⩾ 4.
There is also a result by Hu, Meng, Pan, Su and Xiong [HMP
+23] which establishes the
existence of 16m × 16m normal 3-multimagic squares for all m ⩾ 1. We refer the reader
to the introductions of [PLCX21], [HMP
+23] and [HP24] for more detailed history on the
progress regarding normal 2 and 3-multimagic squares. The most general result regarding
multimagic squares is given by Derksen, Eggermont and van der Essen [DEvdE07] who have
proved that there exist n × n normal d-multimagic squares for any n = qd with q ⩾ 2. There
is also a comprehensive list of various magic squares recorded by Boyer [Boy] which includes
the following:
• n × n magic squares of squares for 4 ⩽ n ⩽ 7.
• n × n 2-multimagic squares for 8 ⩽ n ⩽ 64.
• number of magic squares of dth powers for 2 ⩽ d ⩽ 7.
Thus we see that our Theorems 1.2 and 1.3 are the ﬁrst result of this type and of diﬀerent
nature compared to all the previous results on magic squares in the literature.

Remark 1.4. It is important to mention the very nice work by Flores [Flo] here. It was
completely unknown to us that he was simultaneously working on an adjacent problem until
his preprint appeared on the arXiv on 12/6/2024 which prompted us to post our original
version on 13/6/2024. Flores established the existence of n × n “non-trivial” d-multimagic
squares for all n ⩾ 2d(d + 1) + 1 also using the circle method. Strictly speaking, however, his
non-trivial multimagic square is not a magic square in the sense of Conjecture 1.1, because

4 NICK ROME AND SHUNTARO YAMAGISHI

it allows repeated entries; this is an important distinction for us, because for example 3 × 3
magic squares of squares with repeated entries are known to exist while the big open problem
is regarding the existence of one without. Though it is not dealt with in his paper, there is
no doubt that Flores’ work can be adapted to deal with multimagic squares without repeated
entries as well.

1.2. Application of the Hardy-Littlewood circle method. Let us label the entries of
the n × n magic square of dth powers as follows:

x
d
1,1 . . . x
d
1,n
. . .

x
d
n,1 . . . x
d
n,n
 .

Let µ be a positive integer. The system of equations deﬁning the n × n magic square of dth

powers with magic constant µ is equivalent to

x
d
1,1 + · · · + x
d
1,n = µ (1.2)
.
x
d
n,1 + · · · + x
d
n,n = µ

x
d
1,1 + · · · + x
d
n,1 = µ
.
x
d
1,n−1 + · · · + x
d
n,n−1 = µ

x
d
1,1 + · · · + x
d
n,n = µ

x
d
1,n + · · · + x
d
n,1 = µ,

which we denote by F0(x0) = µ. A priori the system of equations deﬁning the n × n magic
square of dth powers with magic constant µ requires 2n + 2 equations; however, it can be
veriﬁed that there is one degree of redundancy (the 2n − 1 equations corresponding to n rows
and n − 1 columns imply the equation corresponding to the remaining column). Therefore,
this is a system of equations deﬁned by R0 = 2n + 1 degree d homogeneous polynomials in
N0 = n
2 variables. Since the number of variables N0 grows quadratically with R0, it may
seem reasonable at ﬁrst to expect that the known results regarding the Hardy-Littlewood
circle method readily apply to this system. As it turns out, the system (1.2) is “too singular”
for this to be the case.
A seminal result by Birch [Bir62] establishes the existence of a non-trivial integral solution
to a general system of equations F1(x) = · · · = FR(x) = 0 deﬁned by R homogeneous
polynomials of degree d in N variables. For d = 2, this was greatly improved by Rydin
Myerson [RM18]. An important quantity in these results is the dimension of the singular
locus of the pencil σR(F) = max
β∈RR dim{x ∈ AN : β.∇F(x) = 0},

where F = (F1, . . . , FR). The required bound for σR(F) is N > σR(F)+(d−1)2d−1R(R+1) for
Birch’s result to be applicable, while N > σR(F) + 8R for Rydin Myerson’s result. However,
it can be veriﬁed that
 σR(F0) ⩾ n
2 − n = N0 − R0 − 1

2 ,

ON THE EXISTENCE OF MAGIC SQUARES OF POWERS 5

which is far too large to make use of either of the mentioned results. Both of these results
are for general systems of homogeneous polynomials; however, the system (1.2) consists only
of diagonal polynomials and there are results in this direction as well. Let us now suppose
that F1, . . . , FR are diagonal polynomials. The system of diagonal equations F1(x) = · · · =
FR(x) = 0 was ﬁrst studied by Davenport and Lewis [DL69, Lemma 32]; their result required

N ⩾
 {
⌊9R2d log(3Rd)⌋ if d is odd,
⌊48R2d3 log(3Rd2)⌋ if d ⩾ 4 is even,

to establish the existence of a non-trivial integral solution. Since N0 = (R0 − 1)2/4, we
can not hope to directly apply this result to (1.2). By incorporating the breakthrough on
Waring’s problem by Vaughan [Vau89], Br¨udern and Cook [BC92] improved the number of
variables required to be N ⩾ 2dR(log d + O(log log d)).
We remark that both of these results require a suitable “rank condition” on the coeﬃcient
matrix. Since the time of these two papers, there has been great progress regarding War-
ing’s problem (for example, by Wooley [Woo92], [Woo95] and more recently by Wooley and
Br¨udern [BW23]) and also the resolution of Vinogradov’s mean value theorem (see the work
by Bourgain, Demeter and Guth [BDG16], and by Wooley [Woo16, Woo19]). By incorporat-
ing these recent developments, the required number of variables may be further improved.
Though this technical procedure is mostly standard, we present the details in our separate
paper [RY] and the result applied to the system (1.2) is summarised in Theorem 2.2.

Acknowledgements. NR was supported by FWF project ESP 441-NBL while SY by a
FWF grant (DOI 10.55776/P32428). The authors are grateful to Tim Browning for his
constant encouragement and enthusiasm, J¨org Br¨udern for very helpful discussion regarding
his paper [BC92] and Diyuan Wu for turning the proof of Theorem 2.4 in the original version
into an algorithm and running the computation for us, for which the results are available
in the appendix of the original version. They would also like to thank Christian Boyer for
maintaining his website [Boy] which contains a comprehensive list of various magic squares
discovered, Brady Haran and Tony V´arilly-Alvarado for their public engagement activity of
mathematics and magic squares of squares
2, and all the magic squares enthusiasts who have
contributed to [Boy] which made this paper possible. Finally, the authors would like to thank
Daniel Flores for his work [Flo] which inspired them to optimise the proof of Theorem 2.4
and Trevor Wooley for very helpful discussion regarding recent developments in Waring’s
problem and his comments on the original version of this paper.

Notation. We make use of the standard abbreviations e(z) = e
2πiz and eq(z) = e 2πiz
q . Given
a vector a = (a1, . . . , aR) ∈ Z
R, by 1 ⩽ a ⩽ q we mean 1 ⩽ ai ⩽ q for each 1 ⩽ i ⩽ R.

2. Magic squares of powers

Let µ be a positive integer. Let M0 be the coeﬃcient matrix of the system (1.2), which is
given by (5.1). We deﬁne

I = {0} ∪ {(i1, j1; i2, j2) : (i1, j1) ̸= (i2, j2), 1 ⩽ i1, j1, i2, j2 ⩽ n}.

2A YouTube video “Magic Squares of Squares (are PROBABLY impossible)” of the Num-
berphile channel by Brady Haran, in which Tony V´arilly-Alvarado appears as a guest speaker:
https://www.youtube.com/watch?v=Kdsj84UdeYg.

6 NICK ROME AND SHUNTARO YAMAGISHI

For each σ = (i1, j1; i2, j2) ∈ I \ {0}, we denote xσ to be x0 with xi2,j2 removed and
Fσ(xσ) = µ the system of equations obtained by substituting xi2,j2 = xi1,j1 into F0(x0) = µ.
We then denote by Mσ the coeﬃcient matrix of this system, which is obtained from M0 by
adding the ((i2 − 1)n + j2)-th column to the ((i1 − 1)n + j1)-th column and then deleting the
((i2 − 1)n + j2)-th column (here ((i − 1)n + j)-th column corresponds to the xi,j variable).
For σ ∈ I , B ⊆ N and X ⩾ 1, we introduce the following counting function

Nσ(B; X, µ) = #{xσ ∈ (B ∩ [1, X])n2−ǫ(σ) : Fσ(xσ) = µ},

where
 ǫ(σ) =
 {
0 if σ = 0,
1 if σ ∈ I \ {0}.

Then the number of magic squares, whose entries are restricted to B, with magic constant
µ is given by
 N(B; X, µ) = N0(B; X, µ) + O
 

 ∑

σ∈I \{0} Nσ(B; X, µ)


 . (2.1)

In this expression, the sum in the O-term is the contribution from squares whose entries are
not distinct. We estimate these counting functions using the Hardy-Littlewood circle method
for B = N and
 A (X, X η) = {x ∈ [1, X] ∩ N : prime p|x implies p ⩽ X η}

for suﬃciently small η > 0. The optimal lower bound for n0(d) in Theorem 1.3 will come
from using smooth numbers for most choices of d, while for d ∈ {2, 3, 4} it will come from
the natural numbers instead.

Deﬁnition 2.1. Let σ ∈ I . We deﬁne Ψ(Mσ) to be the largest integer T such that there
exists {D1, . . . , DT },
where each Di is a linearly independent set of 2n + 1 columns of Mσ and Di ∩ Dj ̸= ∅ if
i ̸= j. We let Tσ be a non-negative integer such that

Ψ(Mσ) ⩾ Tσ.

By applying the circle method to the system of diagonal equations (1.2), we obtain the
following as a direct consequence of [RY, Theorems 1.4 and 1.5]. Here, we present a simpliﬁed
version of the result (see [RY, Tables 1 and 2] for more accurate values and also [RY, Remark
2.3]).

Theorem 2.2. Let B = N or A (X, X η) with η > 0 suﬃciently small. Suppose

min
σ∈I Tσ ⩾
 {
min{2d, d(d + 1)} + 1 if 2 ⩽ d ⩽ 4 and B = N,
⌈d(log d + 4.20032)⌉ + 1 if d ⩾ 5 and B = A (X, X η).

Then there exists λ > 0 such that

N0(B; X, µ) = CBSIX n2−(2n+1)d + O(X n2−(2n+1)d(log X)−λ),

where
 CB =
 {1 if B = N,
c(η) if B = A (X, X η),

ON THE EXISTENCE OF MAGIC SQUARES OF POWERS 7

c(η) > 0 is a constant depending only on η, the singular series S and the singular integral I
are deﬁned in (3.1) and (3.3), respectively. Furthermore,

max
σ∈I \{0} Nσ(B; X, µ) ≪ X n2−(2n+1)d−1.

The next step is to establish lower bounds for S and I which are independent of X. We
present the details of the following proposition in Section 3.

Proposition 2.3. Given any X ⩾ 1 suﬃciently large, there exists µ = µ(X) ∈ N such that

SI > cn,d,

where cn,d > 0 is a constant depending only on n and d.

Finally, in order to establish the existence of magic squares of dth powers with magic
constant µ, it remains to establish a lower bound for Tσ. The following is the main technical
result of the paper, which we prove through Sections 4–6.

Theorem 2.4. Let n ⩾ 8. Then T0 ⩾ ⌊ n
4
 ⌋ − 1.

By combining these results collected in this section, we obtain Theorem 1.3 as an immediate
consequence.

Proof of Theorem 1.3. It follows from Theorem 2.4 that

min
σ∈I \{0} Tσ ⩾ T0 − 2 ⩾ ⌊n
4
 ⌋ − 3.

Therefore, by combining this estimate, Theorem 2.2 and Proposition 2.3 with (2.1), we obtain
that Theorem 1.3 holds with

n0(d) =
 {
4 min{2d, d(d + 1)} + 20 if 2 ⩽ d ⩽ 4,
4⌈d(log d + 4.20032)⌉ + 20 if d ⩾ 5. (2.2)

□

In order to establish Theorem 1.2 we need to deal with smaller values of n.

Proof of Theorem 1.2. It follows from the proof of Theorem 1.3 above that there exists an
n × n magic square of squares as soon as n ⩾ 36. Since the statement is already known for
4 ⩽ n ⩽ 64, in fact explicit examples have been discovered and listed in [Boy], this completes
the proof. □

3. Singular series and singular integral: Proof of Proposition 2.3

We let Col(M0) denote the set of columns of M0. Let JacF0 denote the Jacobian matrix
of F0 and F = R or Qp for any prime p. A crucial fact we make use of in this section is that
given any z ∈ F \ {0}, we have
 JacF0(z, . . . , z) = dzd−1M0,

which in particular is of full rank. Therefore, if F0(z, . . . , z) = µ, then it is in fact a non-
singular solution.
Let S(q, a) = ∑

1⩽x⩽q eq(ax
d).

8 NICK ROME AND SHUNTARO YAMAGISHI

We deﬁne the singular series
 S =
 ∞∑

q=1 A(q), (3.1)

where
 A(q) = q−n2 ∑

1⩽a⩽q
gcd(q,a)=1
 ∏

c∈Col(M0) S(q, a.c) · eq
 (
−µ
 2n+1∑

i=1 ai
)
 .

We have the following lemma regarding S which is [RY, Lemmas 4.1 and 4.2].

Lemma 3.1. Suppose
 T0 > d(2n + 2)
2n + 1 .

Then
 A(q) ≪ q−(2n+1)( T0
d −1), (3.2)

where the implicit constant is independent of µ, and the series (2.3) converges absolutely. In
fact,
 S = ∏

p prime χ(p),

where
 χ(p) = 1 +
 ∞∑

k=1 A(pk).

We establish the desired lower bound for S for special values of µ.

Lemma 3.2. Let µ = npd
0, where p0 is a prime number suﬃciently large with respect to n
and d. Then S0 > cn,d, where cn,d > 0 is a constant depending only on n and d.

Proof. An application of (3.2) yields

|χ(p) − 1| ≪
 ∞∑

k=1 p−k(2n+1)( T0
d −1) ≪ p−(2n+1)( T0
d −1).

Therefore, there exists P > 0 such that∏

p>P χ(p) > 1
2 .

We remark that P is independent of µ. The standard argument shows that

χ(p) = lim
m→∞ νµ(pm)
pm(n2−2n−1) ,

where νµ(pm) is the number of solutions to the congruence F0(x0) ≡ µ (mod pm). Since
µ = npd
0 with prime p0 suﬃciently large and p0 is invertible modulo p for p ⩽ P , it follows
that νµ(pm) = νn(pm).

ON THE EXISTENCE OF MAGIC SQUARES OF POWERS 9

We know that x0 = (1, . . . , 1) ∈ Z
n2
p is a non-singular solution to the system of equations
F0(x0) = n. Thus it follows from Hensel’s lemma that

χ(p) = lim
m→∞ νµ(pm)
pm(n2−2n−1) = lim
m→∞ λn(pm)
pm(n2−2n−1) > 0

for p ⩽ P . Therefore, we obtain
 S > 1
2
 ∏

p⩽P χ(p) ≫ 1,

where the implicit constant is independent of µ. □

Let
 I(β) = ∫ 1

0 e(βξd)dξ.

We deﬁne the singular integral

I = ∫

R2n+1
 ∏

c∈Col(M0) I(γ.c) · e
 (
− µ
X d
 2n+1∑

i=1 γi
)
 dγ. (3.3)

We have the following lemma regarding I which is [RY, Lemmas 4.3]

Lemma 3.3. Suppose T0 > d. Then the integral (3.3) converges absolutely.

We establish the desired lower bound for I for special values of µ.

Lemma 3.4. Let ε0 > 0 be suﬃciently small. Suppose µ = nζ dX d with ζ ∈ [ε0, 1 − ε0]. Then
I > cn,d,ε0, where cn,d,ε0 > 0 is a constant depending only on n, d and ε0.

Proof. It follows by the standard argument as in [Sch82] that

I = lim
L→∞
 ∫

[0,1]n2
 2n+1∏

i=1 ΦL(F0,i(x0) − µX −d)dx0,

where
 ΦL(η) =
 {
L(1 − L|η|) if |η| ⩽ L
−1,
0 otherwise.

Furthermore, since µX −d = nζ d with ζ ∈ [ε0, 1 − ε0], we see that x0 = (ζ, . . . , ζ) is a non-
singular solution to the system of equations F0(x0) = µ. It then follows by an application
of the implicit function theorem as in [Sch82, Lemma 2] that I > 0. In particular, since
ζ ∈ [ε0, 1 − ε0], the lower bound is independent of µ. □

Let ε0 > 0 be suﬃciently small. By the prime number theorem, for any X suﬃciently large
there exists a prime p0 satisfying
 ε0X < p0 < (1 − ε0)X.

Then for µ = npd
0 we see that Lemmas 3.2 and 3.4 hold, from which Proposition 2.3 follows.

10 NICK ROME AND SHUNTARO YAMAGISHI

4. Linear equations

In this section, we record a simple result regarding certain systems of linear equations
which we will need in the following Section 6.1. Let 1 ⩽ i1 < m < m + 1 < i2 ⩽ n. We
denote by Ln(i1; m; i2) the system of 2n linear equations

xi + yi = 0 (1 ⩽ i ⩽ n)
xi+1 + yi = 0 (i ̸= i1 − 1, i1, i2 − 1, i2, m)
xi2 + yi1−1 = 0
xi2+1 + yi1 = 0
xi1 + yi2−1 = 0
xi1+1 + yi2 = 0
ym = 0,

where xn+1 is identiﬁed as x1.

Lemma 4.1. Suppose 1 < i1 < m < m + 1 < i2 < n. Then

{(x, y) ∈ R2n : (x, y) satisﬁes Ln(i1; m; i2)} = {0}.

Proof. Consider the system of equations Ln(i1; m; i2). By substituting ym = 0 into the
equation xm + ym = 0 and following through with the consequences, we obtain

xi = yi = 0 (i ∈ [i1 + 1, m]).

We can then deduce that
 0 = xi1+1 = yi2 = xi2 = yi1−1 = xi1−1,

which further implies that xi = yi = 0 (i ∈ [1, i1 − 1]).

Therefore, the system becomes

xi1 + yi1 = 0 xi2+1 + yi1 = 0
xm+1 + ym+1 = 0 xm+2 + ym+1 = 0
.
xi2−2 + yi2−2 = 0 xi2−1 + yi2−2 = 0
xi2−1 + yi2−1 = 0 xi1 + yi2−1 = 0
xi + yi = 0 xi+1 + yi = 0 (i ∈ [i2 + 1, n]).

By substituting x1 = 0, we obtain

xi = yi = 0 (i ∈ [i2 + 1, n]).

which further implies that 0 = xi2+1 = yi1 = xi1 = yi2−1.

Finally, by substituting yi2−1 = 0 into the remaining system, we see that

xi = yi = 0 (i ∈ [m + 1, i2 − 1])

as desired. □

ON THE EXISTENCE OF MAGIC SQUARES OF POWERS 11

5. Preliminaries

Let In denote the n × n identity matrix and deﬁne ̃In to be the (n − 1) × n matrix obtained
by removing the last row from In. Then the (2n + 1) × n
2 coeﬃcient matrix of the system
(1.2) is
 M0 =
 


















1 1 · · · 1
0 0 · · · 0
. . . .
0 0 · · · 0





 




0 0 · · · 0
1 1 · · · 1
. . . .
0 0 · · · 0




 · · ·
 




0 0 · · · 0
0 0 · · · 0
. . . .
1 1 · · · 1






̃In ̃In · · · ̃In[
1 0 · · · 0
0 0 · · · 1
] [0 1 · · · 0 0
0 0 · · · 1 0
] · · · [0 0 · · · 1
1 0 · · · 0
]
 











 . (5.1)

We shall denote by ci,j the ((i − 1)n + j)-th column of M0, for each 1 ⩽ i, j ⩽ n. The ﬁrst
subscript i will always satisfy 1 ⩽ i ⩽ n, but for the second subscript j, to simplify our
exposition, we will consider it modulo n, that is

ci,j+mn = ci,j,

for any 1 ⩽ j ⩽ n and m ∈ Z.

Deﬁnition 5.1. We shall refer to the set {ci,1, . . . , ci,n} as the i-th block for each 1 ⩽ i ⩽ n.

Given B ⊆ Col(M0), we deﬁne

B[i] = {1 ⩽ j ⩽ n : ci,j ∈ B} (5.2)

for each 1 ⩽ i ⩽ n.
Let S = S1 ∪ S2,
where S1 = {c1,1, c2,2, . . . , cn−1,n−1, cn,n}
and S2 = {c1,n, c2,n−1, . . . , cn−1,2, cn,1} \ S1.
The columns in S1 are precisely the ones with 1 in the 2n-th entry and S2 the ones with 1
in the (2n + 1)-th entry that are not contained in S1. We remark that

#S2 =
 {n if n is even,
n − 1 if n is odd.

Let us deﬁne
 ǫ(n) =
 {
1 if n is even,
0 if n is odd, (5.3)

and
 N = n − 1 + ǫ(n)

2 − 2. (5.4)

For each 0 ⩽ ℓ ⩽ N, we deﬁne

̃Bℓ = {c1,1+2ℓ, c2,2+2ℓ, . . . , cn,n+2ℓ} ⋃ ({c1,1+(2ℓ+1), c2,2+(2ℓ+1), . . . , cn,n+(2ℓ+1)} \ {cn−2ℓ−1,n}) .

12 NICK ROME AND SHUNTARO YAMAGISHI

This set contains precisely one column of the form c∗,n, which is cn−2ℓ,n, a column whose
entries between (n + 1)-th and (2n − 1)-th position are all 0. We will use these sets ̃Bℓ to
construct the collection of pairwise disjoint sets of 2n + 1 linearly independent columns of M
necessary to complete the proof of Theorem 2.4.
By (5.4) it follows that ̃Bℓ ∩ ̃Bℓ′ = ∅ (0 ⩽ ℓ < ℓ′ ⩽ N). (5.5)

Lemma 5.2. Given any 1 ⩽ ℓ ⩽ N, we have

̃Bℓ ∩ S = {
c n+1−ǫ(n)
2 −ℓ, n+1−ǫ(n)
2 +ǫ(n)+ℓ, cn−ℓ,ℓ+1} .

Proof. Since S1 ⊆ ̃B0, it follows from (5.5) that
̃Bℓ ∩ S1 = ∅.

Therefore, if ̃Bℓ ∩ S ̸= ∅, then there exist ǫ ∈ {0, 1} and 1 ⩽ i, j ⩽ n such that

(i, i + 2ℓ + ǫ + m(i, ℓ, ǫ)n) = (j, n + 1 − j),

where
 m(i, ℓ, ǫ) =
 {0 if 1 ⩽ i + 2ℓ + ǫ ⩽ n,
−1 if n < i + 2ℓ + ǫ ⩽ 2n.

It follows that i = j and
 j + 2ℓ + ǫ + m(j, ℓ, ǫ)n = n + 1 − j,

or equivalently
 j = n + 1 − ǫ
2 − ℓ − m(j, ℓ, ǫ)n
2 .

Suppose m(j, ℓ, ǫ) = 0. Then it must be that ǫ = 1 if n is even and 0 if n is odd. Thus we
see that c n+1−ǫ(n)
2 −ℓ, n+1−ǫ(n)
2 +ǫ(n)+ℓ ∈ ̃Bℓ ∩ S ;

here we note that 1 ⩽ n+1−ǫ(n)
2 + ǫ(n) + ℓ ⩽ n.
On the other hand, suppose m(j, ℓ, ǫ) = −1. Then

j = n + 1 − ǫ
2 − ℓ.

In particular, it must be that ǫ = 1. Thus we see that

cn−ℓ,ℓ+1 ∈ ̃Bℓ ∩ S .

Finally, we have c n+1−ǫ(n)
2 −ℓ, n+1−ǫ(n)
2 +ǫ(n)+ℓ ̸= cn−ℓ,ℓ+1, since

1 ⩽ n + 1 − ǫ(n)
2 − ℓ ⩽ n
2 − ℓ < n − ℓ.
 □

As a consequence of this lemma, there are precisely two columns in ̃Bℓ whose last two
entries are not 0. In the next section, we replace these two columns from ̃Bℓ with appropriate
columns whose last two entries are 0 such that the resulting set is linearly independent.
Finally, we complete the sets by adding two columns whose last two entries are not 0 which
preserve the linear independence.

ON THE EXISTENCE OF MAGIC SQUARES OF POWERS 13

6. Proof of Theorem 2.4

Let n ⩾ 8 and 1 ⩽ ℓ ⩽ N, where N is deﬁned in (5.4). Our goal is to replace the two
columns in ̃Bℓ from Lemma 5.2 in a suitable manner so that all columns have 0 for the last
two entries. Let us denote

i1(ℓ) = n + 1 − ǫ(n)
2 − ℓ and i2(ℓ) = n − ℓ,

where ǫ(n) is deﬁned in (5.3). Then the two columns we need to replace are

c n+1−ǫ(n)
2 −ℓ, n+1−ǫ(n)
2 +ǫ(n)+ℓ = ci1(ℓ),i1(ℓ)+2ℓ+ǫ(n) and cn−ℓ,ℓ+1 = ci2(ℓ),i2(ℓ)+2ℓ+1.

We shall modify ̃Bℓ as follows

Bℓ = ̃Bℓ \ (
{ci1(ℓ),i1(ℓ)+2ℓ, ci1(ℓ),i1(ℓ)+2ℓ+1} ⋃
{ci2(ℓ),i2(ℓ)+2ℓ, ci2(ℓ),i2(ℓ)+2ℓ+1})

⋃{ci1(ℓ),i2(ℓ)+2ℓ, ci1(ℓ),i2(ℓ)+2ℓ+1} ⋃
{ci2(ℓ),i1(ℓ)+2ℓ, ci2(ℓ),i1(ℓ)+2ℓ+1},

that is we ﬁrst remove the two columns in ̃Bℓ from the i1(ℓ)-th and i2(ℓ)-th block and then
add back in two columns from each of these blocks with switched positions. We remark that
we know there are two columns in ̃Bℓ from the i1(ℓ)-th and i2(ℓ)-th block, because

1 < i1(ℓ) < n − 2ℓ − 1 < n − 2ℓ < i2(ℓ) < n. (6.1)

It is clear that given 1 ⩽ ℓ < ℓ′ ⩽ N we have

{i1(ℓ), i2(ℓ)} ∩ {i1(ℓ′), i2(ℓ′)} = ∅. (6.2)

Therefore, the two blocks of ̃Bℓ which get modiﬁed to construct Bℓ are unique to ℓ. Let us
also recall the notation (5.2) and record the relations

Bℓ[i1(ℓ)] = {i2(ℓ) + 2ℓ, i2(ℓ) + 2ℓ + 1} and Bℓ[i2(ℓ)] = {i1(ℓ) + 2ℓ, i1(ℓ) + 2ℓ + 1} (6.3)

for each 1 ⩽ ℓ ⩽ N.

Lemma 6.1. Given 1 ⩽ ℓ ⩽ N such that

ℓ ̸=
 {
⌊n/4⌋ if n is even,
⌊n/4⌋, ⌊n/4⌋ + 1 if n is odd,

we have {ci1(ℓ),i2(ℓ)+2ℓ, ci1(ℓ),i2(ℓ)+2ℓ+1} ⋂ S = ∅

and {ci2(ℓ),i1(ℓ)+2ℓ, ci2(ℓ),i1(ℓ)+2ℓ+1} ⋂ S = ∅.

In particular, every column of Bℓ has 0 for the last two entries.

Proof. Let ǫ ∈ {0, 1}. Since it can be veriﬁed that

i1(ℓ) + i2(ℓ) + 2ℓ + ǫ ≡ n + 1 − ǫ(n)
2 + ǫ ̸≡ n + 1 (mod n)

and
 ±(i1(ℓ) − i2(ℓ)) ≡ ±n + 1 − ǫ(n)
2 ̸≡ 2ℓ + ǫ (mod n),

the result follows. □

14 NICK ROME AND SHUNTARO YAMAGISHI

Let Z ⊆ {1, . . . , N} be a set with the following property: given any m, ℓ ∈ Z , we have

n + 1 − ǫ(n)
2 ̸≡ 2(m − ℓ) + δ (mod n) (6.4)

for any δ ∈ {−1, 0, 1}.
Let us deﬁne R = ⋃

ℓ∈Z ̃Bℓ.

Lemma 6.2. Given ℓ ∈ Z , we have

Bℓ[i1(ℓ)] ∩ R[i1(ℓ)] = ∅

and Bℓ[i2(ℓ)] ∩ R[i2(ℓ)] = ∅.

Proof. First we recall the relations (6.3). Let us suppose

{i2(ℓ) + 2ℓ, i2(ℓ) + 2ℓ + 1} ⋂ R[i1(ℓ)] ̸= ∅.

Then there exists m ∈ Z such that

i2(ℓ) + 2ℓ + ǫ ≡ i1(ℓ) + 2m + ǫ
′ (mod n)

for some ǫ, ǫ
′ ∈ {0, 1}. Since the congruence is equivalent to

n + 1 − ǫ(n)
2 ≡ 2(ℓ − m) + ǫ − ǫ
′ (mod n),

we reach contradiction by the deﬁnition of Z .
Similarly, let us suppose

{i1(ℓ) + 2ℓ, i1(ℓ) + 2ℓ + 1} ⋂ R[i2(ℓ)] ̸= ∅.

Then there exists m ∈ Z such that

i1(ℓ) + 2ℓ + ǫ ≡ i2(ℓ) + 2m + ǫ
′ (mod n)

for some ǫ, ǫ
′ ∈ {0, 1}. From this congruence, we may reach contradiction in the same way
as above. □

Lemma 6.3. We have Bℓ ∩ Bℓ′ = ∅
for any distinct ℓ, ℓ′ ∈ Z .

Proof. Let Z = #Z and denote Z = {ℓ1, . . . , ℓZ}.
We shall prove by induction that

Bℓi ⋂ (
Bℓ1 ∪ · · · ∪ Bℓi−1 ∪ ̃Bℓi+1 ∪ · · · ∪ ̃BℓZ ) = ∅

for each 1 ⩽ i ⩽ Z. The base case i = 1 follows easily from (5.5) and Lemma 6.2. Let us
suppose the statement holds for all values greater than or equal to 1 and less than i, for some
1 < i ⩽ Z. Let i + 1 < j ⩽ Z. Then it follows from (5.5) and Lemma 6.2 that

Bℓi+1 ∩ ̃Bℓj = (
Bℓi+1 \ ̃Bℓi+1) ∩ ̃Bℓj ⊆ (Bℓi+1 \ ̃Bℓi+1) ∩ R = ∅.

ON THE EXISTENCE OF MAGIC SQUARES OF POWERS 15

Therefore, it remains to prove
 Bℓi+1 ⋂ (Bℓ1 ∪ · · · ∪ Bℓi) = ∅.

Since it follows from the inductive hypothesis that
̃Bℓi+1 ∩ Bℓs = ∅ (1 ⩽ s ⩽ i),

it suﬃces to prove (Bℓi+1 \ ̃Bℓi+1) ∩ Bℓs = ∅ (1 ⩽ s ⩽ i),

which in turn follows from

Bℓi+1[i1(ℓi+1)] ∩ Bℓs[i1(ℓi+1)] = ∅ and Bℓi+1[i2(ℓi+1)] ∩ Bℓs[i2(ℓi+1)] = ∅ (6.5)

for all 1 ⩽ s ⩽ i. Since the i1(ℓi+1)-th and i2(ℓi+1)-th block of ̃Bℓs do not get modiﬁed to
construct Bℓs, which follows from (6.2), we obtain

Bℓs[i1(ℓi+1)] = ̃Bℓs[i1(ℓi+1)] ⊆ R[i1(ℓi+1)]

and Bℓs[i2(ℓi+1)] = ̃Bℓs[i2(ℓi+1)] ⊆ R[i2(ℓi+1)]
for all 1 ⩽ s ⩽ i. Therefore, (6.5) and consequently the result follow from Lemma 6.2. □

Finally, we prove that Bℓ is a linearly independent set.

Lemma 6.4. Given ℓ ∈ Z \ {⌊n/4⌋, ⌊n/4⌋ + 1}, we have

dim SpanRBℓ = 2n − 1.

Proof. Suppose we have the following linear combination of columns in Bℓ:

0 = ∑

1⩽i⩽n
i̸=i1(ℓ),i2(ℓ)

(xici,i+2ℓ + yici,i+2ℓ+1) (6.6)

+xi1(ℓ)ci1(ℓ),i2(ℓ)+2ℓ + yi1(ℓ)ci1(ℓ),i2(ℓ)+2ℓ+1
+xi2(ℓ)ci2(ℓ),i1(ℓ)+2ℓ + yi2(ℓ)ci2(ℓ),i1(ℓ)+2ℓ+1,

with yn−2ℓ−1 = 0 (because we have (6.1) and cn−2ℓ−1,n /∈ Bℓ). Our goal is to show xi = yi = 0
for all 1 ⩽ i ⩽ n. Let us recall that cn−2ℓ,n ∈ Bℓ whose entries between (n + 1)-th and
(2n − 1)-th positions are all 0. Furthermore, this is the only column in Bℓ of the form c∗,n,
which follows from the deﬁnition of Bℓ and (6.1). By the deﬁnition of ci,j, the vector equation
(6.6) is equivalent to the following system of linear equations

xi + yi = 0 (1 ⩽ i ⩽ n)
xi+1 + yi = 0 (i ̸= i1(ℓ) − 1, i1(ℓ), i2(ℓ) − 1, i2(ℓ), n − 2ℓ − 1)
xi2(ℓ) + yi1(ℓ)−1 = 0
xi2(ℓ)+1 + yi1(ℓ) = 0
xi1(ℓ) + yi2(ℓ)−1 = 0
xi1(ℓ)+1 + yi2(ℓ) = 0
yn−2ℓ−1 = 0.

It is clear that this system of equations is precisely L(i1(ℓ); n − 2ℓ − 1; i2(ℓ)). Therefore, the
result follows from Lemma 4.1 since we have (6.1). □

16 NICK ROME AND SHUNTARO YAMAGISHI

6.1. Final bound for T0. Let us set

Z = {
1, . . . , ⌊n
4
 ⌋ − 1} .

Then we have
 |2(m − ℓ) + δ| ⩽ 2 ⌊n
4
 ⌋ − 3 ⩽ n − 6
2
for any m, ℓ ∈ Z and δ ∈ {−1, 0, 1}, which implies that Z satisﬁes (6.4). Since every column
in Bℓ has 0 for the last two entries, we obtain the following as an immediate consequence.

Corollary 6.5. Let ℓ ∈ Z and (a, b) ∈ S1 × S2. Then Bℓ ∪ {a, b} is a linearly independent
set.

Since #S1, #S2 ⩾ n − 1 ⩾ |Z | = ⌊n
4
 ⌋ − 1,

and Bℓ are pairwise disjoint, we easily obtain ⌊n/4⌋ − 1 pairwise disjoint sets of the form

Dℓ = Bℓ ∪ {aℓ, bℓ},

where (aℓ, bℓ) ∈ S1 × S2. Thus we have established

T0 ⩾ ⌊ n
4
 ⌋ − 1,

where T0 is from the statement of the theorem.

References

[BC92] J. Br¨udern and R. J. Cook, On simultaneous diagonal equations and inequalities. Acta Arith. 62
(1992), no. 2, 125–149.
[BDG16] J. Bourgain, C. Demeter, and L. Guth, Proof of the main conjecture in Vinogradov’s mean value
theorem for degrees higher than three. Ann. of Math. (2) 184 (2016), no. 2, 633–682.
[Bir62] B. J. Birch, Forms in many variables. Proc. Roy. Soc. London Ser. A 265 (1961/62), 245–263.
[Boy] C. Boyer, The multimagic squares site, http://www.multimagie.com.
[Boy05] , Some notes on the magic squares of squares problem. Math. Intelligencer 27 (2005),
no. 2, 52–64.
[BTVA22] N. Bruin, J. Thomas, and A. V´arilly-Alvarado, Explicit computation of symmetric diﬀerentials
and its application to quasihyperbolicity. Algebra Number Theory 16 (2022), no. 6, 1377–1405.
[BW23] J. Br¨udern and T. D. Wooley, On Waring’s problem for larger powers. J. Reine Angew. Math.
805 (2023), 115–142.
[Cam60] S. Cammann, The evolution of magic squares in China. Journal of the American Oriental Society
80 (1960), no. 2, 116–124.
[DEvdE07] H. Derksen, C. Eggermont, and A. van den Essen, Multimagic squares. Amer. Math. Monthly
114 (2007), no. 8, 703–713.
[DL69] H. Davenport and D. J. Lewis, Simultaneous equations of additive type. Philos. Trans. Roy. Soc.
London Ser. A 264 (1969), 557–595.
[Flo] D. Flores, A circle method approach to k-multimagic squares. arXiv:2406.08161.
[HMP+23] C. Hu, J. Meng, F. Pan, M. Su, and S. Xiong, On the existence of a normal trimagic square of
order 16 n. Journal of Mathematics 2023 (2023), 1–9.
[HP24] C. Hu and F. Pan, New inﬁnite classes for normal trimagic squares of even orders using row–square
magic rectangles. Mathematics 12 (2024), no. 8.
[Kee11] A.D. Keedwell, Gaston Tarry and multimagic squares. The Mathematical Gazette 95 (2011),
no. 534, 454–468.
[PLCX21] F. Pan, W. Li, G. Chen, and B. Xin, A complete solution to the existence of normal bimagic
squares of even order. Discrete Math. 344 (2021), no. 4, Paper No. 112292, 9.

ON THE EXISTENCE OF MAGIC SQUARES OF POWERS 17

[RM18] S. L. Rydin Myerson, Quadratic forms and systems of forms in many variables. Invent. Math.
213 (2018), no. 1, 205–235.
[RY] N. Rome and S. Yamagishi, Integral solutions to systems of diagonal equations. arXiv:2406.09256.
[Sch82] W. M. Schmidt, Simultaneous rational zeros of quadratic forms, Seminar on Number Theory,
Paris 1980-81, Progr. Math., vol. 22, Birkh¨auser, Boston, MA, 1982, pp. 281–307.
[VA21] A. V´arilly-Alvarado, The geometric disposition of Diophantine equations. Notices Amer. Math.
Soc. 68 (2021), no. 8, 1291–1300.
[Vau89] R. C. Vaughan, A new iterative method in Waring’s problem. Acta Math. 162 (1989), 1–71.
[Woo92] T. D. Wooley, Large improvements in Waring’s problem. Ann. of Math. (2) 135 (1992), no. 1,
131–164.
[Woo95] , New estimates for smooth Weyl sums. J. London Math. Soc. (2) 51 (1995), no. 1, 1–13.
[Woo16] , The cubic case of the main conjecture in Vinogradov’s mean value theorem. Adv. Math
294 (2016), 532–561.
[Woo19] , Nested eﬃcient congruencing and relatives of Vinogradov’s mean value theorem. Proc.
London Math. Soc. (3) 118 (2019), no. 4, 942–1016.
Email address: rome@tugraz.at

TU Graz, Institute of Analysis and Number Theory, Kopernikusgasse 24/II, 8010 Graz,
Austria.

Email address: shuntaro.yamagishi@ist.ac.at

IST Austria, Am Campus 1, 3400 Klosterneuburg, Austria.
