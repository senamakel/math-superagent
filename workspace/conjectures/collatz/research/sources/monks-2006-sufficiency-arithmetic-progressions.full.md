<!-- source: https://monks.scranton.edu/files/pubs/SufficiencyRev4.pdf | converted from PDF -->

THE SUFFICIENCY OF ARITHMETIC PROGRESSIONS FOR THE 3x +1
CONJECTURE

KENNETH M. MONKS

Abstract. Deﬁne T : Z+ → Z+ by T (x)= (3x +1) /2 if x is odd and T (x)= x/2 if x is even.
The 3x +1 Conjecture states that the T -orbit of every positive integer contains 1. A set of positive
integers is said to be suﬃcient if the T -orbit of every positive integer intersects the T -orbit of an
element of that set. Thus to prove the 3x +1 Conjecture it suﬃces to prove it on some suﬃcient
set. Andaloro proved that the sets 1+2nN are suﬃcient for n ≤ 4 and asked if 1+ 2nN is also
suﬃcient for larger values of n. We answer this question in the aﬃrmative by proving the stronger
result that A + BN is suﬃcient for any nonnegative integers A and B with B 6=0, i.e. every
nonconstant arithmetic sequence forms a suﬃcient set. We then prove analagous results for the
Divergent Orbits Conjecture and Nontrivial Cycles Conjecture.

1. Introduction and Statement of Main Results

A dynamical system on a set X is obtained by iterating a map f : X → X.For any function
f : X → X and any x ∈ X,the f-orbit of x is the set ©
f k (x): k ∈ N
ª where f 0 is the identity map
and f k = f ◦ f k−1 for all positive integers k.If x, y∈ X whose f -orbits are not disjoint, we will say
that x and y merge or that x merges with y.Thus, x and y merge if and only if there exist some
nonnegative integers k and j such that f k (x)= f j (y) .The relation "merges with" is an equivalence
relation on X.Asubset S ⊆X is called suﬃcient for f on X if S meets every equivalence class, i.e.
if every element of X merges with some element of S.Since all of the elements in an equivalence class
merge, the long-term behavior of their orbits must be identical. Thus to determine the long-term
behavior of the orbits of the elements of X,itsuﬃces to determine the long-term behavior of the
orbits of the elements of some suﬃcient set S.
The famous 3x +1 Conjecture has been an open problem in dynamical systems theory for more
than 65 years (see [Lag],[Wir]). The conjecture states that the T -orbit of every positive integer
contains 1,where T is given by T (x)= x/2 if x is even and T (x)= (3x +1) /2 if x is odd. For any
positive integer x,if x merges with 1 then T k (x)= T j (1) for some nonnegative integers k and j.
Since T j (1) = 1 if j is even and T j (1) = 2 if j is odd, either T k (x)=1 or T k+1 (x)= 1.In either
case the T -orbit of x contains 1.Thus, the 3x +1 Conjecture is true if and only if every positive
integer merges with 1. Therefore, to prove the conjecture it suﬃces to prove it holds on some set
S that is suﬃcient for T on Z
+, since if every element of S merges with 1 then every positive integer
also merges with 1. For the remainder of the paper, the term "suﬃcient" with no qualiﬁcation will
mean "suﬃcient for T on Z
+".
Andaloro [And] proved that the set 1+ 16N is suﬃcient. As any superset of a suﬃcient set is
also suﬃcient, it follows that 1+2
nN is suﬃcient for n ≤ 4. In the same paper, Andaloro asks if
1+2
nN is suﬃcient for any or all n> 4.
All of the sets 1+2
nN are members of the more general family of sets of the form A + BN where
A and B are natural numbers and B 6=0. We will call any such set an arithmetic progression since

1991 Mathematics Subject Classiﬁcation. Primary 11B25, 11B83.
Key words and phrases. 3x +1 problem, Arithmetic sequences, Orbits.

1

2 KENNETH M . M ONKS

it is the set of terms in the nonconstant arithmetic sequence A, A+ B, A+2B, . . .. It is natural to
ask which of these sets are suﬃcient. We answer this question with our main result.

Theorem 1.1. Every arithmetic progression is suﬃcient.

We postpone the proof until Section 3.
There are only two ways that the T -orbit of a positive integer x can fail to contain 1.If x
has an unbounded T -orbit, we say the T -orbit of x is divergent. The well-known Divergent Orbits
Conjecture states that no positive integer has an unbounded T -orbit. Let S be a set of positive
integers with the following property: if no element of S has an unbounded orbit then the Divergent
Orbits Conjecture is true. We say such a set S is suﬃcient for the Divergent Orbits Conjecture.
If T k (x)= x for some k> 1,then wesay the T -orbit of x is a cycle. The second way the 3x +1
Conjecture could be false is if the T -orbit of some positive integer x is a cycle other than the trivial
cycle, {1,2}. The well-known Nontrivial Cycles Conjecture states that the only cycle of positive
integers is the trivial one.As with the previous conjecture, we say S is suﬃcient for the Nontrivial
Cycles Conjecture when S has the following property: if no element of S has an orbit that contains
a nontrivial cycle then the Nontrivial Cycles Conjecture is true.
Clearly the truth of these two conjectures would imply the 3x +1 Conjecture. Our result carries
over to these conjectures.

Corollary 1.2. Every arithmetic progression is suﬃcient for the Divergent Orbits Conjecture.

Corollary 1.3. Every arithmetic progression is suﬃcient for the Nontrivial Cycles Conjecture.

Thus to prove any of the three conjectures, the 3x+1 Conjecture, the Divergent Orbits Conjecture,
or the Nontrivial Cycles Conjecture, it suﬃces to show that it holds for the elements of some
arithmetic progression. Hence, studying the behavior of T on particular arithmetic sequences may
lead to a proof of the conjecture itself.
Though not directly applicable to the 3x +1 Conjecture itself, the arguments in this paper can be
used to show that every negative arithmetic progression (the negation of all terms in an arithmetic
progression) is suﬃcient for T on Z
−. Additionally, the union of an arithmetic progression, a
negative arithmetic progression, and {0} forms a suﬃcient set for T on Z.The proofs of these cases
are omitted, as they are identical to the proof of Theorem 1.1.
In the next section we provide previously known facts and notation used in our proofs.

2. Background Information and Notation

For convenience, we include here notation and results from Wirsching’s book [Wir] and other
sources that will be used in the proofs of our results.
For any a, b, c∈ Z,c >0, we will write a ≡
c b as an abbreviation for a = b (mod c).

Deﬁne the set of feasible vectors to be F = ∞S

k=0
N
k+1.Let s ∈ F.Then s =(s0,s1, ..., sk) for some

nonnegative integers k and s0,s1, ..., sk.The length of s,written l (s),is k.The norm of s,written

||s||,is l (s)+ l(s)P

i=0
si.

In our proof, it will be essential to consider the inverses of the piecewise components of T .The
even and odd components are denoted T0 (x)= x/2 and T1 (x)=(3x +1) /2 respectively, giving
T −1
0 (x)= 2x and T −1
1 (x)= 2 · 3
−1x − 3
−1 as functions on the rational numbers. For s ∈ F with
s =(s0,s1, ..., sk), Wirsching calls the function vs : Z
+ → Q given by

vs = T −s0
0 ◦ T −1
1 ◦ T −s1
0 ◦ T −1
1 ◦ ...◦ T −1
1 ◦ T −sk
0

SUFFICIENCY OF ARITHM ETIC PROGRESSIONS 3

a back-tracing function.If vs (x) ∈ Z
+ then we say s is an admissible vector for x.Deﬁne E (x)=
{s ∈ F : s is admissible for x}. Wirsching proves a lemma that justiﬁes calling vs the back-tracing
function.

Lemma 2.1. [Wir, Lemma 2.17] If s ∈ E (x) then T ||s|| (vs (x)) = x.

Wirsching also works out a convenient explicit formula for vs in terms of the entries of s.

Lemma 2.2. [Wir, Lemma 2.13] Let s ∈ F.Deﬁne

c (s)= 2
||s||

3l(s)

and
 r (s)=
 l(s)−1X

j=0 2
j+s0+s1+...+sj 3
−(j+1)

Then vs (x)= c (s) x − r (s) .

It is also useful to concatenate smaller vectors into larger vectors. Let s =(s0,s1,s2, ..., sk) and
t =(t0,t1,t2, ..., tm).Deﬁne s · t =(s0,s1,s2,..., sk−1,sk + t0,t1,t2, ..., tm).Then vs·t represents the
function that back-traces ﬁrst along t andthenalong s, as indicated by the following lemma.

Lemma 2.3. [Wir, Corollary 2.10] For any s, t∈ F,vs·t = vs ◦ vt.

In contrast to concatenation, it is also useful to back-trace through part of a longer back-tracing
vector. Deﬁne a terminal part of a vector s =(s0,s1,s2, ..., sk) to be any vector of the form
(sj,sj+1, ..., sk) for j ∈ {0,1,..., k}. Wirsching proves a lemma regarding these.

Lemma 2.4. [Wir, Lemma 2.16] Let s ∈ F.Let x ∈ Z
+.If s ∈ E (x) then for any terminal part t
of s, t∈ E (x) .

Additionally, a condition relating divisibility by 3 and back-tracing will be needed.

Lemma 2.5. [Wir, Lemma 3.4] Let x ∈ Z
+. Then x 6≡
3 0 if and only if there exists some s ∈ E (x)

with l (s) ≥1.

Notice that T0 and T1 are both nonconstant linear functions and therefore are bijections on R.
Thus, T0, T1, and their inverses generate a group of real-valued functions. This group is described
by Misiurewicz and Rodrigues [MR].

Lemma 2.6. [MR, Theorem 5.1] Let G be the group of real-valued functions generated by T0,T1,
T −1
0 ,and T −1
1 .Then

G = ½
h : h (x)= 2
n3
mx + k
2i3j for some n, m, k∈ Z and i, j∈ N
¾

Finally, the following number theoretic result follows from arguments given in [Ber].

Lemma 2.7. For every n ∈ N,for every odd τ ∈ N,and for every a ∈ Z,there exists an increasing

(possibly empty) sequence of natural numbers t1,t2, ..., th with th <n such that hP

i=1
2
tiτ i ≡
2n a.

4 KENNETH M . M ONKS

3. Proof

Much of the proof will consist of studying the actions of functions T0 and T1 on Z/bZ where b is
a positive integer relatively prime to 2 and 3.Let b be such an integer and let Zb = Z/bZ.Notice
that a function of the form

(3.1) h (x)= 2
n3
mx + k

induces a well-deﬁned permutation of Zb for any n, m, k∈ Z. For any such function h,deﬁne h to
be the corresponding permutation of Zb. We adopt the usual convention of using x to stand for
the congruence class of the integer x in expressions such as h (x). For example, T0 : Zb → Zb and
T1 : Zb → Zb are given by T0 (x)=2
−1x and T1 (x)= 2
−13x +2
−1 and both are in the form of
(3.1). Notice also that if h and g are two functions in the form of (3.1), then h ◦ g is also of the same
form, and h ◦ g = h ◦ g. We classify the group generated by these two permutations for a given b.

Lemma 3.1. Let b be a positive integer relatively prime to 2 and 3.Let Gb be the group of permu-
tations on Zb generated by T0 and T1.Then

Gb = ©
h : h (x)= 2
n3
mx + k for some n, m, k∈ Z
ª

Proof:
Deﬁne
 M = ©
h : h (x)= 2
n3
mx + k for some n, m, k∈ Z
ª

and let H ∈ M .Then H = h for some h such that h (x)= 2
n3
mx + k for some n, m, k∈ Z.By
Lemma 2.6 h is some composition of T0,T1,T
−1
0 ,and T −1
1 .Thus there exist e1,e2,..., eg ∈ Z such
that h = T eg
1 ◦ T eg−1
0 ◦ .. .◦ T e4
1 ◦ T e3
0 ◦ T e2
1 ◦ T e1
0 .
Since the set of permutations on Zb is a ﬁnite group, there exist σ0,σ1 ∈ Z
+ such that T0σ0 = T0
and T1σ1 = T1.Thus by increasing ei by a multiple of σ0 for odd i and increasing ei by a multiple
of σ1 for even i as necessary, we can create a sequence of positive integers e
0
1,e
0
2,.. .,e
0
g such that

h = T1e
0
g ◦ T0e
0
g−1 ◦ .. .◦ T1e
0
4 ◦ T0e
0
3 ◦ T1e
0
2 ◦ T0e
0
1. Therefore h ∈ Gb,so H ∈ Gb.Thus M ⊆Gb.
Conversely, since b is relatively prime to 2 and 3,both 2
−1 and 3
−1 are elements of Zb.Thus,
the generators T0 (x)= 2
−1x =2
−13
0x +0 and T1 (x)= 2
−13
1x +2
−1 are both elements of M .
Therefore ¡
T0 ◦ H¢ (x)= 2
n−13
mx +2
−1k and ¡
T1 ◦ H¢ (x)= 2
n−13
m+1x + ¡
2
−13k +2
−1¢
,which
are also both elements of M .Thus M contains the generators of Gb and is closed under composition
with respect to these generators. Hence Gb ⊆M , and we are done.
QED
We now present an outline of the proof. In order to prove that any arithmetic progression is
suﬃcient, we choose an arbitrary arithmetic progression A + BN and an arbitrary positive integer x
and show that x merges with an element a ∈ A + BN. Thisisdoneinthree steps. In the ﬁrst step
(Lemma 3.2), we ﬁnd a particular k such that we can back-trace from T k (x) to a.In the second
step (Lemma 3.6), we use T k (x) as a stepping-stone to show that x merges with a number z that
is congruent to 0 modulo 2
nb where B =2
n3mb and b is relatively prime to 2 and 3.For the third
and ﬁnal step (Lemma 3.8), we use z as the next stepping-stone to show that x merges with a.
To begin the ﬁrst step, we observe that in order to back-trace from a number with admissible
vectors of positive length it must not be divisible by 3 by Lemma 2.5.

Lemma 3.2. For every x ∈ Z
+,there exists k ∈ N such that T k (x) 6≡
3 0.

Proof:
Let x ∈ Z
+.If x 6≡
3 0, then we are done, since T 0 (x)= x.

SUFFICIENCY OF ARITHM ETIC PROGRESSIONS 5

Assume x ≡
3 0.Let k be one more than the exponent of the largest 2-power that divides x.

Clearly T k−1 (x)= 2i +1 for some i ∈ N.Thus

T k (x)= T ¡
T k−1 (x)¢

= T (2i +1)

= 3(2i +1)+1
2
=3i +2
6≡
3 0

QED
Thus any positive integer has an iterate that is not divisible by 3. We now present three technical
lemmas that will be used in step two. We start by reproving a stronger version of [Wir, Lemma 3.1].

Lemma 3.3. For any s ∈ F,there exists q0 ∈ N − 3N such that for any q ∈ Z
+,

s ∈ E (q) ⇔ q ≡
3l(s) q0

Proof:
Let s ∈ F.We have that s = ¡
s0,s1,... ,sl(s)¢ for some natural numbers s0,s1,... ,sl(s).Let
q ∈ Z
+.If l (s)= 0 then vs (q)= 2
s0q ∈ Z
+ so that s ∈ E (q).Thus the theorem is satisﬁed trivially
in this case.
Assume l (s) ≥1.There exists t ∈ N such that 2t ≡
3l(s) 1 since 2 is relatively prime to 3
l(s).Let

w =3
l(s)r (s).Bythe deﬁnition of r (s),wehave

w =3
l(s)l(s)−1X

j=0 2
j+s0+s1+...+sj 3
−(j+1)(3.2)
 =3
l(s)
 

2
l(s)−1+s0+s1+...+sl(s)−13
−l(s) +
 l(s)−2X

j=0 2
j+s0+s1+...+sj 3
−(j+1)




=2
l(s)−1+s0+s1+...+sl(s)−1 +3

l(s)−2X

j=0 2
j+s0+s1+...+sj 3
l(s)−j−2

which shows that w ∈ Z
+ and 3 - w.Deﬁne q0 = t
||s||w.Since 3 - t as well, q0 ∈ N − 3N. By Lemma
2.2, vs (q)= c (s) q − r (s)= 3
−l(s) ³
2
kskq − 3
l(s)r (s)´ =3
−l(s) ³2
kskq − w´

We have that
 s ∈ E (q) ⇔ vs (q) ∈ Z
+

⇔ 3
−l(s) ³
2
kskq − w´ ∈ Z
+

⇔ 3
l(s) | ³
2
kskq − w´

⇔ 2
kskq − w ≡
3l(s) 0

⇔ q ≡
3l(s) t
kskw

⇔ q ≡
3l(s) q0

6 KENNETH M . M ONKS

which completes the proof.
QED
The second technical lemma demonstrates that any feasible vector can be concatenated with a
vector of length zero to make it admissible for any given natural number relatively prime to 3.

Lemma 3.4. For any s ∈ F and any y ∈ N − 3N,there exists a natural number k such that
s · (k) ∈ E (y) .

Proof:
Let s ∈ F.Let y ∈ N − 3N. By Lemma 3.3, there exists q0 ∈ N − 3N such that for any
q ∈ Z
+,s∈ E (q) ⇔ q ≡
3l(s) q0.

Since 2 is a primitive root for 3
l(s) (c.f. [Hua]), we have that 2
ky ≡
3l(s) q0 for some k ∈ Z
+.Thus

s ∈ E ¡
2
ky¢
, so by Lemma 2.3 we have

vs·(k) (y)= ¡
vs ◦ v(k)¢ (y)= vs ¡
T −k
0 (y)¢ = vs ¡
2
ky¢ ∈ Z
+

Therefore s · (k) ∈ E (y).
QED
For the third technical lemma, again using vs (x)= c (s) x − r (s) as in Lemma 2.2, we prove two
facts about r (s). Namely, we show that any ﬁnite increasing sequence can appear in the exponents
of the 2-powers in the formula for r (s), and for a given positive integer b relatively prime to 2 and
3, all elements of Zb can be obtained as r (s) for some s.

Lemma 3.5. Let b be a positive integer relatively prime to 2 and 3.
(i) Let t1,t2, ..., td be a strictly increasing sequence of natural numbers. Then there exists some s ∈

F such that vs (x)= 2
||s||3
−dx − dP

i=1
2
ti3
−i.

(ii) Let n, m, k∈ Z.There exists an s ∈ F such that vs ∈ Gb is given by vs (x)= 2
n3
mx + k.

Furthermore, there exist increasing natural numbers u1,u2,... ,ud such that dP

i=1
2
ui3
−i ≡
b k.

Proof:

(i) Deﬁne s0 = t1 and si = ti+1 − ti − 1 for i ∈ {1,2, ..., d− 1}.The sum jP

i=0
si is a telescoping

sum, so by induction on j, jP

i=0
si = tj+1 − j for any j ∈ {0,1, ..., d− 1}.

Now take s =(s0,s1,..., sd−1,0).Then l (s)= d. By Lemma 2.2, we see that

vs (x) ≡
b 2
||s||3
−dx −
 d−1X

j=02

j+ j

i=0
si

3−(j+1)

=2
||s||3
−dx −
 d−1X

j=02
tj+13
−(j+1)

and we are done.
(ii) The function h (x)= 2
n3
mx − k is an element of Gb by Lemma 3.1. Since Gb is generated by
T0 and T1, h = T1eg ◦T0eg−1 ◦.. .◦T1e4 ◦T0e3 ◦T1e2 ◦T0e1 for some g, e1,e2,..., eg ∈ N.Let σ0 and σ1
be the orders of T0 and T1 respectively as in the proof of Lemma 3.1. By decreasing ei by a multiple
of σ0 for odd i and decreasing ei by a multiple of σ1 for even i as necessary, we can create a sequence

of nonpositive integers e
0
1,e
0
2,.. .,e
0
g such that h = T1e
0
g ◦ T0e
0
g−1 ◦ .. .◦ T1e
0
4 ◦ T0e
0
3 ◦ T1e
0
2 ◦ T0e
0
1.

SUFFICIENCY OF ARITHM ETIC PROGRESSIONS 7

Thus there exists an s ∈ F with vs = h,so vs (x)= 2
n3
mx − k.Since vs (x)= c (s) x − r (s),we
have

(3.3) r (s)= −vs (0) ≡
b −h (0) = k

Deﬁne uj =(j − 1) + s0 + s1 + ...+ sj−1
for j ∈ {1,... ,l(s)}.Clearly u1,u2, ..., ul(s)−1 is strictly increasing. Since Lemma 2.2 gives that

l(s)X

j=12
uj 3
−j =
 l(s)−1X

j=0 2
j+s0+s1+...+sj 3
−(j+1)

= r (s)
≡
b k

by (3.3).
QED
We now complete the second step in the proof of the main result.

Lemma 3.6. Let b be a positive integer relatively prime to 2 and 3 and let n ∈ N.For every x ∈ Z
+,
there exists z ∈ Z
+ such that z ≡
2nb 0 and z 6≡
3 0 and x merges with z.

Proof:
Let x ∈ Z
+. By Lemma 3.2, there exists y such that y 6≡
3 0 and x merges with y. We will produce

an s ∈ E (y) such that vs (y) ≡
2nb 0 and vs (y) 6≡
3 0.

We know that there exists an s1 ∈ F such that vs1 (x) ≡
b x +1 by part (ii) of Lemma 3.5.Thus

for any m ∈ N

(3.4) vm
s1 (x) ≡
b x + m

Lemma 3.4 allows us to choose n1 ∈ N such that (0,0) · s1 · s1 · ...· s1| {z }
b
 · (n1) ∈ E (y).Let s2 =

(0,0) · s1 · s1 · ...· s1| {z }
b
 · (n1).Since s2 is admissible for y, vt (y) ∈ Z
+ for any terminal part t of s2 by

Lemma 2.4. So v(n1) (y) ≡
b a for some a ∈ {0,1,2, ..., b− 1}.Deﬁne s3 = s1 · s1 · ...· s1| {z }
b−a
 · (n1).This

gives us
 vs3 (y)= vs1 · s1 · ...· s1| {z }

b−a
 ·(n1) (y)

= vb−a
s1 ¡
v(n1) (y)¢ by Lemma 2.3

≡
b vb−a
s1 (a)

≡
b a +(b − a) by (3.4)

≡
b 0

Deﬁne s4 =(0,0) ·s1 · s1 · .. .· s1| {z }
a . By Lemma 2.3,

vs4 (vs3 (y)) = vs4·s3 (y)= vs2 (y) ∈ N

8 KENNETH M . M ONKS

Thus s4 ∈ E (vs3 (y)).Since l (s4) is positive, vs3 (y) 6≡
3 0 by Lemma 2.5.

Deﬁne s =(n) · s3.Wehavethat

vs (y)= v(n)·s3 (y)= v(n) (vs3 (y)) = 2
nvs3 (y) ∈ N

Thus s ∈ E (y).Deﬁne z = vs (y).Since vs3 (y) 6≡
3 0,wehave 2
nvs3 (y) 6≡
3 0.Thus z 6≡
3 0.

Since vs3 (y) ≡
b 0,wehave 2
nvs3 (y) ≡
2nb 0.Thus z ≡
2nb 0.

Lemma 2.1 implies that y = T ||s|| (vs (y)),so y = T ||s|| (z).Thus y merges with z,and x merges
with y,so x merges with z.
QED
We now provide a technical lemma in preparation for the ﬁnal step.

Lemma 3.7. Let s ∈ F and let m, q0 ∈ N.Then there exists p0 ∈ N−3N such that for any p ∈ Z
+,if
p ≡
3l(s)+m p0 then s ∈ E (p) and vs (p) ≡
3m q0.

Proof:
Deﬁne w =3
l(s)r (s), as in Lemma 3.3. Again by equation (3.2), w ∈ Z
+ and 3 - w.
Since 2 is relatively prime to 3
l(s)+m,there exists some t ∈ Z
+ such that 2t ≡
3l(s)+m 1.Deﬁne

p0 = t
||s|| ¡
3
l(s)q0 + w¢.Noticethat 3 - p0 since 3 - t and 3 - w.Let p ∈ Z
+ and assume p ≡
3l(s)+m p0.

2
||s||p − w ≡
3l(s)+m 2
||s|| ³
t
||s|| ³
3
l(s)q0 + w´´ − w(3.5)
 ≡
3l(s)+m 2
||s||t
||s||3
l(s)q0 +2
||s||t
||s||w − w

≡
3l(s)+m 1
||s||3
l(s)q0 +1
||s||w − w

≡
3l(s)+m 3
l(s)q0

Thus 3
l(s) | 2
kskp − w,so 2
||s||p−w
3l(s) ∈ Z
+. FromLemma 2.2wehavethat vs (p)= 2
ksk

3l(s) p − r (s)=

2
kskp−w
3l(s) ,so vs (p) ∈ Z
+ and s ∈ E (p). Division of both sides and the modulus of (3.5) by 3
l(s) yields
that vs (p) ≡
3m q0.
QED
In the third and ﬁnal step we use z as our stepping-stone to show that any positive integer x can
merge with a,a number that is in whatever congruence class we desire.

Lemma 3.8. Let b be a positive integer relatively prime to 2 and 3 and let n, m∈ N.For every x ∈
Z
+ and for any a0,q0 ∈ N,there exists an a ∈ Z
+ such that a ≡
2nb a0 and a ≡
3m q0 and x merges with
a.

Proof:
Let x ∈ Z
+. By Lemma 3.6, there exists an z ∈ Z
+ such that z ≡
2nb 0 and z 6≡
3 0 and x merges

with z.Let a0,q0 ∈ N.We have a0 ≡
2nb a1 +2
na2 for some a1 ∈ {0,1,2, ...,2
n − 1} and a2 ∈

{0,1,2, ..., b− 1}.
We now show that there exists an odd natural number τ such that 3τ ≡
2nb 1.If n =0,wecan take

any natural number t with 3t ≡
b 1 and either set τ = t (in the case that t is odd) or τ = t + b (in the

case that t is even). Otherwise if n> 0 then any τ ∈ N such that 3τ ≡
2nb 1 satisﬁes 2
nb | (3τ − 1)

which implies that τ is odd.

SUFFICIENCY OF ARITHM ETIC PROGRESSIONS 9

There exists an increasing sequence of natural numbers t1,t2, ..., th1 with th1 <n such that
h1P

i=1
2
tiτ i ≡
2n −a1 by Lemma 2.7. By the deﬁnition of congruence, h1P

i=1
2
tiτ i = −a1 +2
ni1 for some

i1 ∈ Z. There exist increasing natural numbers u1,u2, ..., uh2 such that h2P

i=1
2
uiτ i ≡
b 3
h1 (−a2 − i1) by

part (ii) of Lemma 3.5. Therefore τ h1 h2P

i=1
2
uiτ i ≡
b (−a2 − i1),so by the deﬁnition of congruence,

τ h1 h2P

i=12
uiτ i = −a2 − i1 + bi2 for some i2 ∈ Z.Deﬁne

wi =
 ( ti if 1 ≤i ≤h1
n + ui−h1 if h1 +1 ≤i ≤h1 + h2

That is, wi is the i
th term of the sequence t1,t2,... ,th1,n+ u1,n+ u2, ..., n+ uh2.Since ti and ui
are increasing and th1 <n, the sequence w1,w2,.. .,wh1+h2 is also increasing. So

h1+h2X

i=1 2
wiτ i =
 h1X

i=12
wiτ i +
 h1+h2X

i=h1+1
2
wiτ i

=
 h1X

i=12
tiτ i +
 h2X

i=12
wi+h1 τ i+h1

=(−a1 +2
ni1)+ τ h1 h2X

i=12
n+uiτ i

= −a1 +2
ni1 +2
n Ã

τ h1 h2X

i=12
uiτ i!

= −a1 +2
ni1 +2
n (−a2 − i1 + bi2)

= −a1 − 2
na2 +2
nbi2
≡
2nb −a1 − 2
na2

≡
2nb −a0

Thus there exists an increasing sequence w1,w2,.. .,wh1+h2 such that h1+h2P

i=1 2
wiτ i ≡
2nb
 h1+h2P

i=1 2
wi3
−i ≡
2nb
−a0,sobypart (i) of Lemma 3.5 there exists an s1 ∈ F such that

(3.6) vs1 (x) ≡
2nb 2
||s1||3
−l(s1)x + a0

By Lemma 3.7 there exists p0 ∈ N − 3N such that for all p ∈ Z
+,if p ≡
3l(s1)+m p0 then s1 ∈ E (p)

and vs1 (p) ≡
3m q0.Since 2 is a primitive root for 3
l(s1)+m (c.f. [Hua]) and z is a unit mod 3
l(s1)+m,

there exists n2 ∈ Z
+ such that 2
n2z ≡
3l(s1)+m p0.Thus s1 ∈ E (2
n2z) and vs1 (2
n2z) ≡
3m q0.Deﬁne

s = s1 · (n2). By Lemma 2.3,

vs (z)= vs1·(n2) (z)= vs1 ¡
v(n2) (z)
¢ = vs1 (2
n2z)

Therefore s ∈ E (z) so vs (z) ∈ Z
+ and vs (z) ≡
3m q0.Deﬁning a = vs (z),wehave a ≡
3m q0.

10 KENNETH M . M ONKS

Note that 2
n2 z is divisible by 2
nb,since z is. Thus 2
n2z ≡
2nb 0,sothat

a = vs (z)

= vs1 (2
n2z)

≡
2nb vs1 (0)

≡
2nb a0 by (3.6)

By Lemma 2.1, T ksk (a)= z.Thus z merges with a,and x merges with z,so x merges with a.
QED
As thepreviouslemma showsthat any positive integer x merges with an integer a that can be
in any desired congruence classes modulo 2
nb and modulo 3
m, we are prepared to prove the main
result.
ProofofTheorem 1.1:
Let S be an arithmetic progression. Let x ∈ Z
+. Wehavethat S = A + BN for some nonnegative
integers A and B with B 6=0.There exists some k ∈ Z
+ such that kB > A.Wecan write
kB =2
n3
mb for some n,m ∈ Z
+ and b ∈ Z
+ relatively prime to 2 and 3. By Lemma 3.8, there
exists an a ∈ Z
+ such that a ≡
2nb A and a ≡
3m A and x merges with a.Thus a ≡
2nb3m A since 2
nb and

3
m are relatively prime and both divide a − A. Hence a = A + kBk1 for some k1 ∈ Z. However,
k1 > 0 since a is positive and kB > A.Thus k1 ∈ N and a ∈ S. Therefore every positive integer
merges with an element of S.So, S is a suﬃcient set.
QED
The proofs of the corollaries then easily follow from the main result.
ProofofCorollary 1.2:
Let S be an arithmetic progression and assume that for every a ∈ S, limj→∞ T j (a) 6= ∞.Let
x ∈ Z
+.Then x merges with a for some a ∈ S by Theorem 1.1. Since x and a merge, their orbits
are not disjoint, so T j1 (x)= T j2 (a) for some j1,j2 ∈ Z
+.Therefore for every j ∈ Z
+, T j1+j (x)=
T j2+j (a) .Thus limj→∞ T j (x) 6= ∞ as well.So no positive integer has a divergent orbit, and the
Divergent Orbits Conjecture holds. Thus S is suﬃcient for the Divergent Orbits Conjecture.
QED
ProofofCorollary 1.3:
Let S be an arithmetic progression and assume that no element of S has an orbit that contains a
nontrivial cycle. Let x ∈ Z
+. There exists some a ∈ S such that x merges with a by Theorem 1.1.
Assume the orbit of x contains a nontrivial cycle. Since x and a merge, their orbits are not disjoint,
so T j1 (x)= T j2 (a) for some j1,j2 ∈ Z
+. Therefore for every j ∈ Z
+, T j1+j (x)= T j2+j (a),so the
orbit of a contains a nontrivial cycle as well, contradicting the assumption. Thus no positive integer
has an orbit that contains a nontrivial cycle, and the Nontrivial Cycles Conjecture holds. Thus S
is suﬃcient for the Nontrivial Cycles Conjecture.
QED
 4. Acknowledgements

The author would like to thank Kenneth G. Monks for his advice, assistance, and support through-
out the course of this project. This project was funded by two summer research grants from the
University of Scranton.
 References

[And] Andaloro, P., On total stopping times under 3x +1 iteration, Fibonacci Quart. 38 (2000), no. 1, 73—78.
[Ber] Bernstein, D. J. ANon-Iterative 2-adic Statement of the 3x +1 Conjecture, Proc. Amer. Math. Soc. 121
(1994), 405-408.
 SUFFICIENCY OF ARITHM ETIC PROGRESSIONS 11

[Hua] Hua, Loo Keng, Introduction to Number Theory, Springer-Verlag, 1982, ISBN: 3-540-10818-1.
[Lag] Lagarias, J. C., The 3x +1 problem and its generalizations,Am. Math. Monthly 92 (1985), 3-23.
[MR] Misiurewicz, M. and Rodrigues, A., Real 3x +1, Proc. Amer. Math. Soc. 133 (2004) 1109-1118.
[Wir] Wirsching, G., The Dynamical System Generated by the 3n +1 Function, Lecture Notes in Math. 1681,
Springer-Verlag, 1998, ISBN: 3-540-63970-5.

Department of Mathematics, University of Scranton, Scranton, PA, 18510
E-mail address : monksk2@scranton.edu
