<!-- source: https://www.numdam.org/item/10.1051/ita:2005038.pdf | converted from PDF -->

RAIRO-Inf. Theor. Appl. 40 (2006) 15-27

DOI: 10.1051/ita:2005038

ON CHRISTOFFEL CLASSES

Jean-Pierre Borel 1 ,∗ and Christophe Reutenauer 2 ,∗∗

Abstract. We characterize conjugation classes of Christoﬀel words
(equivalently of standard words) by the number of factors. We give
several geometric proofs of classical results on these words and sturmian
words.

Mathematics Subject Classiﬁcation. 68R15.

1. Introduction

Sturmian sequences have a long history, through the work of Bernoulli in the
18th century, of Smith, Christoﬀel and Markoﬀ in the 19th century, Morse and
Hedlund in the 20th century and the explosion of researches at the end of it. See the
books by Allouche and Shallit [1] and Berstel and S´e´ebold [3]. They are related to
continued fractions, discrete geometry, symbolic dynamics, formal languages and
combinatorics on words.
Christoﬀel words are a ﬁnitary version of Sturmian sequences, related to con-
tinued fractions of rational numbers. They are a variant of the so called standard
words [3], which appear in Christoﬀel’s article [6].
The present article, besides some new results, rests on two principles: ﬁrst,
most of the theory of Sturmian sequences may be done on its ﬁnitary counterpart,
the theory of Christoﬀel words and their conjugates; secondly, most of the proofs
use only elementary arguments of planar geometry, in the spirit of [4]. We shall
illustrate here the second principle (for the ﬁrst, it should be done elsewhere). This
is done for some already known results in the Appendix. We also give some new
results: in particular, the conjugation classes of Christoﬀel words (equivalently

Keywords and phrases. Words, Christoﬀel, sturmian, conjugation, geometric.

1 LACO, UMR CNRS 6090, 123 avenue Albert Thomas, 87060 Limoges Cedex, France;
borel@unilim.fr
* Partially supported by R·egion Limousin.
2 Universit´eduQu´ebec `aMontr´eal; D´epartement de math´ematiques; Case postale 8888,
succursale Centre-Ville, Montr´eal (Qu´ebec) H3C 3P8, Canada; christo@math.uqam.ca
** Partially supported by NSERC and CRC (Canada). c⃝ EDP Sciences 2005

Article published by EDP Sciences and available at  http://www.edpsciences.org/ita or http://dx.doi.org/10.1051/ita:2005038

16 J.-P. BOREL AND C. REUTENAUER

(0, 0)
 (7, 3)

Figure 1. The lower Christoﬀel word aaabaabaab of slope 3
7 ·

of standard words) are characterized by the number of factors, see Theorem 4.1,
which is a ﬁnitary version of a well-known result of Morse-Hedlund on Sturmian
sequences.
Furthermore, Theorem 5.1 gives the exact position of the k +1 factors of
length k. This result has as consequence that in a Sturmian sequence, the k+1 fac-
tors of length k appear in some window of length 2k (it could not be shorter).
This article also sheds some light onto the circular structure of Christoﬀel words,
which justiﬁes the title. For related work on conjugacy and Sturmian sequences,
see the interesting word of Chuan [7–10].
The authors want to thank Val´erie Berth´e, Fran¸cois Bergeron and Jean Berstel
for useful discussions on this subject and Aldo de Luca for useful mail exchange.
And the two referees for useful suggestions and corrections.

2. Christoffel words

Aword w on a two-letter alphabet is called a lower Christoﬀel word if it is
obtained by discretizing a segment in the plane, as in Figure 1.
Formally, the deﬁnition goes as follows: each word w on an ordered two-letter
alphabet {a, b} deﬁnes naturally a continuous (even piecewise linear) path in the
plane, from the origin to some point (p, q) ∈ N2; letter a corresponds to a segment
[(i, j), (i+1,j)], letter b to a segment [(i, j), (i, j +1)]; thus p (resp. q)is the number
of a′s (resp. b′s)in w.
Now let (p, q) ∈ N2 with gcd(p, q) = 1. Consider a word w whose a–degree is p
and whose b–degree is q.We say that w is a lower Christoﬀel word if the path of w
is under the segment [(0, 0), (p, q)], and if both delimit a polygon with no integral
interior point. We say that w is the lower Christoﬀel word of slope q
p .Observe
that w is of length p + q.
One deﬁnes similarly upper Christoﬀel words.A Christoﬀel word is by deﬁnition
a lower or an upper Christoﬀel word. Note that a single letter is by deﬁnition also
a Christoﬀel word, but we disregard in the sequel this trivial case.
Note that if w, w′ are the lower and upper Christoﬀel words associated to (p, q),
then w′ =˜w (the reversal of w); moreover, w = amb, w′ = bma, where m is
the word that encodes the sequence of vertical and horizontal intersections of the

ON CHRISTOFFEL CLASSES 17

Figure 2. m = aabaabaa.

a
 b
a

b
 b

a a

Figure 3. The circular word (aaababb).

segment with the axes of the integer lattice; in particular, by symmetry, m is a
palindrome. See Figure 2.
Let us call cutting word aword m that is obtained in this way. In other words,
m is a cutting word (on the alphabet {a, b}) if and only if amb (or equivalently
bma) is a Christoﬀel word. These words have been studied extensively; they are
called central in [3], and the notation PER is used by A. de Luca for the set they
form. See [2] for other discretization procedures for segments.

3. Pirillo’s theorem

Recall that two words u, v are conjugate if for some words f, g, one has u =
fg, v = gf . Conjugation is an equivalence relation. An equivalence class is called
a conjugation class,or a circular word. The conjugation class of w is denoted (w).
See Figure 3.

Theorem 3.1. Aword m on the two-letter alphabet {a, b} is a cutting word if and
only if amb and bma are conjugate.

Remark. Pirillo’s statement in [15, 16] is the following: a word m is a palin-
drome preﬁx of some standard Sturmian sequence if and only if mab and mba are
conjugate.

18 J.-P. BOREL AND C. REUTENAUER

This statement is equivalent to the theorem; indeed, it follows from the general
theory of Sturmian words (see [3]) that m is a palindrome preﬁx of a standard
Sturmian sequence if and only if amb and bma are Christoﬀel words. Moreover, it
is easy to see that: mab and mba conjugate ⇔ amb and bma conjugate.
The fact that the lower and upper Christoﬀel words of the same slope are
conjugate (which is the direct part of Pirillo’s theorem) was already known by H.
Cohn [11] (Lem. 6.1); see also [12] proof of Proposition 10.

4. Characterization of Christoffel classes

Aword v is a factor of a word w if for some words p, q, one has w = pvq.A
word v is called factor of a circular word (w)if v is a factor of some conjugate
of w;notethat v may be factor of (w) without being factor of w, e.g. aa is factor
of (aba), but not of aba.

Theorem 4.1. Let w be a word of length n ≥ 2. The following statements are
equivalent.
(i) w is conjugate to a Christoﬀel word.
(ii) For k =0,... ,n − 1, (w) has k +1 factors of length k.
(iii) (w) has n − 1 factors of length n − 2 and w is primitive.

We call Christoﬀel class the conjugation class of a Christoﬀel word. Recall that a
word is primitive if it is not a power of some other word; equivalently, the associate
circular word is not ﬁxed by any nontrivial rotation.
We shall use the following lemma, which is a ﬁnitary version of a well-known
result for (inﬁnite) sequences.

Lemma 4.1. Let w be awordof length n. The following statements are equivalent:
(i) w is primitive;
(ii) for k =0,...,n − 1, (w) has at least k + 1 factors of length k.

We prove this lemma, since we could not ﬁnd a reference for it, although the
technique is classical.

Proof. If w is not primitive, then w = up,p ≥ 2. Then k = |u| <n,and (w)
has ≤ k factors of length k.
For the converse, denote by ak the number of factors of length k of (w). Then
1= a0 ≤ a1 ≤ ... ≤ an since each factor of length i − 1 has a right extension into a
factor of length i,if i ≤ n. Suppose that ak ≤ k for some k ∈{0,... ,n − 1}.Then
for some l ≤ k, one has al−1 = al ≤ l. Consider the factor graph of order l − 1
of (w), whose vertices are the factors of length l − 1of(w), with an edge u a
−→ v,
if ua is a factor of length l of (w), a a letter, and if ua = bv for some letter b.By
hypothesis, each factor of length l − 1 has a unique right extension into a factor of
length l. Hence each vertex has exactly one outgoing edge. Hence, each strongly
connected component of the graph is a simple closed path. Since the sequence
w∞ = ww ...w ... is the sequence of the labels of the edges of some inﬁnite path

ON CHRISTOFFEL CLASSES 19

w.w=a a b a a b a a b a b. a a b a a b a a b a b

Figure 4. The 4 factors of length 3.

in the graph, we see that w∞ has a period not greater than the number of vertices,
that is, hence w∞ has a period ≤ k. Hence w is not primitive. □

Proofofthe theorem.
(i) ⇒ (ii) This will be proved independently in the next section.
(ii) ⇒ (iii) Is clear, by the lemma.
(iii) ⇒ (i) By the lemma, (w) has at least n factors of length n − 1; but it cannot
have more, so that (w) has exactly n factors of length n − 1.
Now, the circular word (w)has n occurrences of factors of length n−2; moreover,
there are n − 1 distinct such factors. We deduce that (w) has exactly one factor
of length n − 2 that appears twice (call it m), and the others appear only once.
Since (w)has n factors of length n − 1, each factor of length n − 2has aunique
right (resp. left) extension into a factor of length n − 1 except one, which has
two extensions and which we denote by r (resp. l). Necessarily, r (resp. l)must
appear twice. Hence l = m = r.
Since m appears exactly twice and since length of w =length of m +2, we
have (w)= (amb)= (cmd); by the property of double extension, we deduce that
b ̸= d, a ̸= c; by counting letters, we see that {a, b} = {c, d}, hence a = d, b = c
and a ̸= b.Thus (amb)=(bma),amb and bma are conjugate and we conclude
using Pirillo’s theorem. □

5. Factors of a Christoffel class

We want to prove the following result.

Theorem 5.1. Let w be a Christoﬀel word of length n and k ∈{0, 1 ... ,
n − 1}.Let p (resp. s) the preﬁx (resp. suﬃx) of length k of w.Then (w)
has k +1 distinct factors of length k and they coincide with the k +1 factors of sp,
which are all distinct.

Note that sp is of length 2k and that a word of length 2k has k +1 factors of
length k, when they are counted with multiplicities; here, they are all distinct.
As an example, take w = aabaabaabab and k = 3. See Figure 4.

Proofofthe theorem.
1. Let C denote the set of conjugates of w.Fix k as in the Theorem. Note
that the set of factors of length k of (w), or equivalently of ww,is equal
to the set of preﬁxes of length k of the conjugates of w.
Deﬁne Ck to be the set of conjugates of w whose ﬁrst letter is a letter in s
(s is deﬁned in the statement), together with w itself; in other words, the

20 J.-P. BOREL AND C. REUTENAUER

(7, 3)

(0, 0)
 D

Figure 5. The 10 conjugates of x
3yx
2yx
2y.

elements of Ck are the preﬁxes of length n of s2w, for some factorization
s = s1s2. Clearly, |Ck| = k +1, since w is primitive.
We shall show that the set of preﬁxes of length k of the words in C is
equal to the set of preﬁxes of length k of the words in Ck, and that the
latter are distinct. This will prove the theorem.
2. To this end, we deﬁne a mapping ϕ : C\w → C\w′ (w′ is the greatest
conjugate in the lexicographic order of w), such that: if w2 = ϕ(w1)
and p1,p2 are the preﬁxes of length k of w1,w2,then (∗)either p1 = p2
or p1 >p2 in lexicographical order; moreover, (∗∗) the latter case occurs
if and only if w1 ∈ Ck.
This will prove 1.
3. It will turn out from the deﬁnition of ϕ that: w2 = ϕ(w1) ⇒
w1 = myxn, w2 = mxyn; this will prove (∗). Moreover, |m| <k ⇔
w1 ∈ Ck; this will prove (∗∗). Note that we use here the alphabet {x, y},
referring to the coordinates in the x, y-plane, see below.
4. We use the geometric realization of words in order to deﬁne ϕ.
We identify a primitive word w with the bi-inﬁnite sequence (we shall
say “sequence”) ··· w.w ··· w ··· ∈ {x, y}Z, where the dot indicates the
position of the zero. The latter sequence will be identiﬁed with the cor-
responding bi-inﬁnite path in the x, y-plane, together with some integer
point on this path, which serves to identify the origin of the path and dis-
tinguish between conjugates of w. All the conjugates of w give the same
bi-inﬁnite path, but with diﬀerent origins. See Figure 5, where the origins
are the fat points.
5. Now, consider all the points (np, nq) ∈ Z (here (p, q)= (7, 3)).
They are all on line D and the path goes vertically towards these points,
and leaves them horizontally (see Fig. 5); this corresponds to the factor

ON CHRISTOFFEL CLASSES 21

(0, 0)
 D D’

(p, q)

Figure 6. Geometric deﬁnition of the mapping ϕ.

yx in ...www ... We replace these yx by xy and change correspondingly
the path. See Figure 6.

The new path is identical to the previous one, after a translation, which amounts
to replace line D by line D′, which passes through the points of the ancient path
closest to D, but not on D.
Changing the path, but keeping the same fat points, we obtain the mapping
ϕ : C\w → C\w′, since we identify conjugates with fat points. It is readily veriﬁed
that ϕ satisﬁes 3. □

The proof shows also the following result.

Corollary 5.1. Let w be a lower Christoﬀel word and w = w1 <w2 < ... < wn
be its conjugates ordered lexicographically. Then w1 = xmy, wn = ymx and for
each i =1,... ,n − 1, one has for some words u, v, wi = uxyv, wi+1 = uyxv.

We may illustrate the corollary by writing a matrix with w = w1 in the ﬁrst row,
w2 in the second etc. Then each line diﬀers from the next only by one factor xy
which is replaced by yx. See Figure 7, where dots indicate the replacement.
Note that this matrix, for general words w, appears in the so called
Burrows-Wheeler transformation. It allows to S. Mantaci, A. Restivo, M. Sciortino
to prove that a word w is in a Christoﬀel class if and only if the last column of
this matrix is formed by y′s, followed by x
′s, see [14].
On this matrix, the mapping ϕ of the proof of Theroem 5.1 appears as scanning
through the rows: ϕ of a conjugate of w is the conjugate in the row above it. Note
that in the example of Figure 7, if we take k =4, the set C4 of the proof of
Theorem 5.1 is

C4 = {yx
2yx
3yx
2,x
2yx
3yx
2y, xyx
3yx
2yx, yx
3yx
2yx
2,x
3yx
2yx
2y};

22 J.-P. BOREL AND C. REUTENAUER

x xx y x x y xx y
x x y xxx y x x y
x x y xx y xxx y
x xy x x y x xy x
x y xxx y x x y x
x yx x y x x x yx
x yx x yx x yx x
y xxx y x x y xx
y xx y xxx y x x
y xx y x x y xxx

Figure 7. Matrix of conjugates.

x

0
7

4

1
 8
 5 2
 9
6

3

y

x

x
y
 x x
 y
 x

x

Figure 8. Cayley graph of a Z/10Z with generator 3.

the factors of length 4 of ww are the preﬁxes of length 4 of the words in C4,that
is yx
2y, x
2yx, xyx
2,yx
3,x
3y.
A closer look at this matrix shows that it has a cyclic structure, and also many
symmetries. This may be deduced from the following construction of Christoﬀel
words, which appears already in Christoﬀel’s article [6] (see also the equivalent
formulation by ﬁnite interval rotations [14] p. 244). We give the construction on
an example, for the Christoﬀel word w = x
3yx
2yx
2y.
The graph of Figure 8 is the Cayley graph of Z/10Z: its vertices are 0, 1,... , 9,
and the edges correspond to the generator 3 of Z/10Z, which is the number of y′s
in the Christoﬀel word w. Each vertex of the graph corresponds to a conjugate
(equivalently, a nontrivial suﬃx) of w, and the numbering of the vertex corresponds
to the distance to the line D of the corresponding integer point in Figure 9.
The word w is recovered by putting x on an edge i → j if i< j,and y otherwise,
and reading the edges, beginning form the vertex 0.
The following consequence of the theorem was indicated to us by Val´erie Berth.
Let α be irrational > 0 and consider the line y = αx. We obtain a bi-inﬁnite

ON CHRISTOFFEL CLASSES 23

03 69
2 5 8

1 4 7

Figure 9. Distances to the segment.

sequence s by discretizing from below this line. It is a consequence of the general
theory of Sturmian sequences that s has k + 1 factors of length k for any k ∈ N.
If we write s = ... a−2a−1a1a2a3 ..., where the origin is between a−1 and a1, then:
these k +1 factors are exactly the k +1 factors of a−k ...a−2a−1a1a2 ... ak,which
are distinct.
Indeed, let t be the cutting sequence corresponding to the line y = αx. Then,
denoting by ˜t the reversal of t,we have s = ˜tyxt. Now, for each palindrome word
m which is a preﬁx of t, w = xm y is a lower Christoﬀel word (see [5] Th. 4.1,
[3] Cor. 2.2.29); and there are arbitrary long such words, so we may assume that
|w| >k.Then m is a suﬃx of ˜t and my x m is a factor of s = ˜ty x t,and the yx
factors match. Since ww = xm y xm y and |w| >k, the theorem implies the
above assertion.
We also obtain the following corollary, since Sturmian sequences of the same
slope have the same factors.

Corollary 5.2. For each Sturmian sequence and each nonnegative integer k,some
factor of length 2k of the sequence contains the k +1 factors of length k of the
sequence.

Remark. Another proof of Corollary 5.2 using the Rauzy graph (see [3]) is easily
obtained.

6. Appendix: Some geometrical proofs of known results

a) We ﬁrst prove the direct part of Pirillo’s theorem: if w, w′ are the lower
and upper Christoﬀel word of the same slope, then they are conjugate.
It is easy to verify the following fact: if l, l′ are two parallel lines, as in the
leftmost part of Figure 10, then there exists at most one discrete path, with steps
as the ones in Section 2, between them: indeed, then the three other conﬁgurations
cannot occur (each square in Fig. 10 is a unit square and the fat points are integer
points).
Now consider the Christoﬀel word w of slope q
p ; we construct the segment
(0, 0), (2p, 2q), seeFigure11. Let A, B be the points on the path that are the
furthest from this segment. Then AB is parallel to the segment. By the previous
fact, the path from A to B is necessarily the one encoded by the upper Christoﬀel
word w′. Hence w′ is a factor of ww, which implies that w, w′ are conjugate.

24 J.-P. BOREL AND C. REUTENAUER

A

Figure 10. The ﬁrst conﬁguration forbids the others.

(7, 4)

(0, 0)
 (14, 8)

A
 B

Figure 11. Conjugation of the upper and lower Christoﬀel words.

b) With the same geometric argument, we obtain a little bit more. Recall
from [4] the standard factorization of a lower Christoﬀel word w:it is the factor-
ization w = uv corresponding to cutting the path from (0, 0) to (p, q) at the closest
integer point A
′ to the segment [(0, 0), (p, q)]; see Figure 12. The two words u, v
are necessarily lower Christoﬀel words.
Likewise, the upper Christoﬀel word w′ has a standard factorization which
corresponds to the closest point A
′′ in his path; by symmetry, since w′ =˜w (the
reversal of w), its standard factorization is w′ =˜v ˜u.We have ˜v = ynx, ˜u = ymx
where m, n are palindromes, since ˜v, ˜u are upper Christoﬀel words.
We have also a factorization w = fg corresponding to the furthest point A.Now
this point is necessarily the southeast corner of the unit square whose northwest
corner is A
′′.Thus we see that f, g and ˜v, ˜u are almost equal: f = xnx, g = ymy.
Thus v = x˜ny = xny, u = xmy. Hence we obtain

Proposition 6.1. The lower and upper Christoﬀel words w, w′ are conjugate by
palindromes. More precisely w = xmx yny, w′ = yny xmx, where the standard
factorization of w is w = xmy · xny and m, n are palindromes.

ON CHRISTOFFEL CLASSES 25

(7, 4)

(0, 0)
 ′′A
 A

′A

Figure 12. x
2y · x
2yx
2yxy.

A B C

DD’

Figure 13. Two symmetries imply a translation.

Remark. These results could be obtained as a consequence of the de Luca-Mignosi
characterization of standard words (a word mxy is standard ⇔ xmy is a Christoﬀel
word), see [13]. They show indeed that a word w is standard if and only if, for
some palindromes m, n, r one has w = mxy = nr.

c) We prove now geometrically the well-known fact that if w = xuy is a
Christoﬀel word of slope q/p, with p, q relatively prime, then u has the two periods
s, t with s + t = p + q and sp, tq ≡ 1mod.(p + q) (see [3, 13] Prop. 2.2.12). Note
that s, t are necessarily relatively prime.
We use Figure 12 and the notations of Part b above. We have w = xuy =
xmy xny, hence u = myx n, which shows that u has the palindrome preﬁx m and
the palindrome suﬃx n.Now, u is palindrome, and if a palindrome of length k
has a preﬁx (or suﬃx) of length l,then it has the period k − l; this is because the
product of two axial symmetries is a translation, see Figure 13: D is the bisector
of segment AC,and D′ that of AB. The product of the symmetry by D′ followed
by that of D maps B onto C,and A onto A + −−→
BC; hence it is the translation with
respect vector −−→
BC.
Thus u has the periods which are the sums t and s of the coordinates of the
points A
′ and A
′′ in Figure 12. Let (x
′,y′), (x
′′,y′′) be these coordinates. Then the
parallelogram constructed on these points has no interior integer points. Hence its

area is one, that is, x
′ y′

x
′′ y′′ =1. Moreover, p = x
′ + x
′′,q = y′ + y′′.Thus we

conclude in view of the following lemma.

26 J.-P. BOREL AND C. REUTENAUER

′ = ′′Ax y(, )

(, )′′ ′′ = ′′xy A M

Figure 14. Parallelogram.

Lemma 6.1. Let (x
′,y′), (x
′′,y′′) ∈ N2 be as in Figure 14 and suppose the parallel-
ogram 0A
′MA
′′ does not contain any integer interior point. Then (x
′ +y′)(y′ +y′′)
and (x
′′ + y′′)(x
′ + x
′′) are both congruent to 1 mod.(x
′ + y′ + x
′′ + y′′).

Proof. The area of a parallelogram with integer vertices, and no integer interior

point, is 1. Thus, we have 1 = x
′ y′

x
′′ y′′ = x
′y′′ − x
′′y′.Thus x
′y′′ =1 + x
′′y′

and (x
′ + y′)(y′ + y′′)= x
′y′ + x
′y′′ + y′2 + y′y′′ = x
′y′ +1+ x
′′y′ + y′2 + y′y′′ =
1+(x
′ + x
′′ + y′ + y′′)y′, which proves the ﬁrst congurence. The second is obtained
similarly. □

d) The proof in c). shows also the following fact: if the Christoﬀel word w
is of slope q
p ,gcd(p, q)= 1, and if w = uv is its standard factorization, then
|u| = t, |v| = s with sp, tq ≡ 1mod.(p + q).

References

[1] J.-P. Allouche and J. Shallit, Automatic sequences. Cambridge (2003).
[2] J. Berstel, Trac·e de droites, fractions continues et morphismes it·er·es,in M. Lothaire,Mots,
m´elanges oﬀerts M.-P. Schtzenberger, Herm`es, Paris (1990) 298–309.
[3] J. Berstel and P. S´e´ebold, Sturmian words, in M. Lothaire, Algebraic Combinatorics on
Words, Cambridge University Press (2002) 45–110.
[4] J.-P. Borel and F. Laubie, Quelques mots sur la droite projective r´eelle. J. Th·eorie des
Nombres de Bordeaux 5 (1993) 23–51.
[5] J. Berstel and A. de Luca, Sturmian words, Lyndon words and trees. Theor. Comput. Sci.
178 (1997) 171–2003.
[6] E.B. Christoﬀel, Observatio arithmetica. Annali di Matematica 6 (1875) 148–152.
[7] W.-F. Chuan, α-words and factors of characteristic sequences. Discrete Math. 177 (1997)
33–50.
[8] W.-F. Chuan, Characterizations of α-words, moments, and determinants. Fibonacci Quart.
41 (2003) 194–208.
[9] W.-F. Chuan, Moments of conjugacy classes of binary words. Theor. Comput. Sci. 310
(2004) 273–285.
[10] W.-F. Chuan, Factors of characteristic words of irrational numbers.Preprint.

ON CHRISTOFFEL CLASSES 27

[11] H. Cohn, Markoﬀ forms and primitive words. Math. Ann. 196 (1972) 8–22.
[12] A. de Luca, Sturmian words: structure, combinatorics, and their arithmetics. Theor. Com-
put. Sci. 183 (1997) 45–82.
[13] A. de Luca and F. Mignosi, On some combinatorial properties of Sturmian words. Theor.
Compt. Sci. 136 (1994) 361–385.
[14] S. Mantaci, A. Restivo and M. Sciortino, Burrows-Wheeler transform and Sturmian words.
Inform. Proc. Lett. 86 (2003) 241–246.
[15] G. Pirillo, A new characteristic property of the palindrome preﬁxes of a standard sturmian
word. S·em. Lothar. Combin. 43 (1999) 1–3.
[16] G. Pirillo, A curious characteristic property of standard Sturmian word, in Algebraic Com-
binatorics, Computer Science, edited by H. Crapo and D. Senato. Springer (2001) 541–546.

Communicated by J. Brestel.
Received June, 2004. Accepted December, 2004.

To access this journal online:
www.edpsciences.org
