<!-- source: https://www.math.tugraz.at/~elsholtz/WWW/papers/papers03sumofk.pdf | converted from PDF -->

TRANSACTIONS OF THE
AMERICAN MATHEMATICAL SOCIETY
Volume 353, Number 8, Pages 3209–3227
S 0002-9947(01)02782-9
Article electronically published on April 12, 2001

SUMS OF k UNIT FRACTIONS

CHRISTIAN ELSHOLTZ

Abstract. Erd˝os and Straus conjectured that for any positive integer n ≥ 2
the equation 4
n = 1
x + 1
y + 1
z has a solution in positive integers x, y,and z.
Let m> k ≥ 3and

Em,k(N )= |{n ≤ N | m
n = 1
t1 + .. . + 1
tk has no solution with ti ∈ N}| .

We show that parametric solutions can be used to ﬁnd upper bounds on
Em,k(N ) where the number of parameters increases exponentially with k.This
enables us to prove

Em,k(N ) ≪ N exp (−cm,k(log N )
1− 1
2k−1−1 ) with cm,k > 0.

This improves upon earlier work by Viola (1973) and Shen (1986), and is an
“exponential generalization” of the work of Vaughan (1970), who considered
the case k =3.
 1. Introduction

In the theory of diophantine equations one often chooses the variables to be
coprime. For many equations, for example x
n +yn = zn, thisis no lossof generality.
For other equations, however, this may be a considerable loss of generality. In fact,
if the variables are chosen coprime in pairs then one makes use of k instead of
conceivably 2k − 1 independent parameters only.
The multiplicative structure amongst k integers can be expressed by means of
2k − 1 parameters. One parameter corresponds to each of the 2k − 1nonempty
subsets of the set of k integers.
If one deals with a diophantine equation in many variables which are highly
composite and have many nontrivial common divisors, then one ought to start oﬀ
from the most general starting point using all parameters.
In this paper we apply this idea to the diophantine equation
m
n = 1
t1 + 1
t2 + ... + 1
tk .(1.1)

One of the outstanding problems in the theory of unit fractions is the famous
Erd˝os-Straus conjecture on 4
n = 1
x + 1
y + 1
z and its generalizations.

Conjecture 1.1 (Erd˝os & Straus, 1948, [Erd50]). For all integers n ≥ 2, there ex-
ists a solution of the equation 4
n = 1
x + 1
y + 1
z in positive integers x, y and z.

Received by the editors May 23, 2000 and, in revised form, August 28, 2000.
2000 Mathematics Subject Classiﬁcation. Primary 11D68; Secondary 11D72, 11N36.
The research for this paper was supported by a Ph.D. grant from the German National Merit
Foundation.
 c⃝2001 American Mathematical Society

3209

3210 CHRISTIAN ELSHOLTZ

Conjecture 1.2 (Schinzel, [Sie56]). For all integers m ≥ 4 there exists Nm such
that for all integers n ≥ Nm there exists a solution of m
n = 1
x + 1
y + 1
z in positive
integers x, y and z.

It is not even known whether there is any m such that m
n canbewrittenas a
sum of k = m − 1 unit fractions if n ≥ Nm,k.Note that, for m ≤ k there are,
trivially, solutions of (1.1).
Partial answers to these conjectures concentrated on the exceptional set of de-
nominators, for ﬁxed m and k.Let Em,k(N ) denote the number of those integers
n ≤ N for which (1.1) has no solution in positive integers t1,t2,... ,tk.
Upper bounds on Em,k(N ) can be obtained by means of sieve methods, since
parametric solutions of equation (1.1) solve this equation for denominators n ly-
ing in certain residue classes. It can be expected to yield good upper bounds on
Em,k(N ), if the parametric solution uses many independent parameters.
The question of ﬁnding upper bounds on Em,k(N ) has attracted considerable
attention (see [Nak39], [Web70], [Vau70], [Vio73], [Li81], [Yan82], [She86], and
[AB98]; the strongest of these results are those of Vaughan and Shen). Previous
work started oﬀ from parametric solutions where the number of parameters grows
linearly with k. In this paper we shall show that the number of parameters that
can be used in the sieve process may increase exponentially with k.We prove the
following theorem:

Theorem 1.3. For any ﬁxed k ≥ 3 and m>k the following upper bound holds,
with a positive constant cm,k,

Em,k(N ) ≪ N

exp (
cm,k(log N )
1− 1
2k−1 −1 ) .

This improves upon the work of Viola (see [Vio73]) and Shen (see [She86]) who
proved an upper bound with the exponent 1 − 1
k−1 and 1 − 1
k , respectively, instead
of our new exponent 1 − 1
2k−1−1 .For k = 3, this result had been found before
by Vaughan, (see [Vau70]). Proofs of Vaughan’s result can also be found in the
books by Narkiewicz (see [Nar86]) and Schwarz (see [Sch74]). Our work can be
understood as an “exponential generalization” of the work of Vaughan. We use
2k−1 parameters, while Vaughan used 4 parameters for k =3.
Whereas this work concentrates on sums of a ﬁxed number of unit fractions there
has recently been considerable progress on questions involving an unlimited number
of unit fractions. For this I would like to refer the reader to the work of E. Croot
(see [Cro00]) and G. Martin (see [Mar99] and [Mar00]). A. Schinzel wrote a recent
survey on various aspects of unit fractions, (see [Scha] and [Sch00]).
I would like to express my gratitude to all of those who have contributed to
the research on this work. I am greatly indebted to D.R. Heath-Brown (Oxford),
who introduced me to the subject of the Erd˝os-Straus conjecture and the relevant
methods of elementary and analytic number theory. I would also like to express
my gratitude to W. Schwarz (Frankfurt), D. Laugwitz (Darmstadt), J. Br¨udern
(Stuttgart), A. Schinzel (Warsaw), C. List (Oxford), S. Daniel (Cardiﬀ), an anony-
mous referee, and many others, for useful suggestions.
This paper is part of the author’s Ph.D. thesis. An unabbreviated version can
be obtained from the author upon request.

SUMS OF k UNIT FRACTIONS 3211

2. Notation

It turned out to be suitable to denote the parameters by their rˆole. That is to
say, a parameter that occurs in the i1-th, i2-th, ... , ir-th fraction but not in the
other fractions will be denoted as xi1i2...ir .
It is convenient to have a common name for certain products of parameters.
The product of all parameters occurring in the i-th fraction is denoted by [i]. The
product of all parameters that occur in the i1-th, i2-th, ... , ir-th fraction will be
called
 [i1 ⊕ i2 ⊕ ... ⊕ ir].

Similarly, the product of all parameters that occur in the i1-th, i2-th, ... , ir-th
fraction, but not in the j1-th, j2-th, ... , js-th fraction will be denoted by

[i1 ⊕ i2 ⊕ ... ⊕ ir ⊖ j1 ⊖ j2 ⊖ ... ⊖ js].

The product [1 ⊕ 2], for example, has diﬀerent meanings for diﬀerent k:

k =2 : [1 ⊕ 2] = x12,
k =3 : [1 ⊕ 2] = x12x123,
k =4 : [1 ⊕ 2] = x12x123x124x1234,
k =5 : [1 ⊕ 2] = x12x123x124x125x1234x1235x1245x12345,

etc. While the length of the right hand side grows exponentially with k, the length
of the left hand side is as compact for large k as it is for small k.
To denote individual parameters, it is more convenient to refer to them by their
name xi1i2...ir . Nevertheless, it is important to keep in mind that any individual
parameter xi1i2...ir can also be expressed as

xi1i2...ir =[i1 ⊕ i2 ⊕ ... ⊕ ir ⊖ ir+1 ⊖ ir+2 ⊖ ... ⊖ ik],

where the i1,... ,ir,ir+1,ir+2,... ,ik are a permutation of {1, 2,... ,k}.
We often need to specify those parameters that occur in the second fraction. For
this purpose, we make the following convention: If xI is a parameter such that I is
a subset of {1, 2,... ,k},with2 ∈ I and |I|≥ 2, then we say that I is an admissible
index set or that xI is an admissible parameter. We introduce the abbreviation
K := 2k−1.
We also need a particular enumeration of the parameters xI .We denote the i-th
parameter by yi.Any such parameter yi (for i =1,... ,K − 1) is identical to some
xI for some admissible index set I. With each parameter yi we associate a suitable
constant ϑi, to be deﬁned later.

3. Survey of the Proof

The structure of the proofs of Vaughan, Viola, Shen, and myself is the same. I
will give a short survey of this proof, particularly in the case k =4, and compare
the new approach with previous work.

Step 1: Starting point. We explain the previous work in our new notation
which makes it easier to compare the various results. For k = 3, Vaughan used the
following starting point:

m
n = 1
x12x13x123 + 1
nx12x23x123 + 1
nx13x23x123 .

3212 CHRISTIAN ELSHOLTZ

For k = 4, we use the following starting point.

m
n = 1
x12x123x124x134x1234 + 1
nx12x23x24x123x124x234x1234

+ 1
nx23x123x134x234x1234 + 1
nx24x124x134x234x1234 .

(3.1)

More generally, we use all 2k−1 − 1 parameters occurring in the second fraction, and
x134...k, i.e. the only parameter not occurring in the second fraction. Note that this
is a slight simpliﬁcation of the most general starting point which would allow for
2k − 1 instead of 2k−1 parameters. The idea that in principle 2k − 1 parameters can
be used to decompose integers can be traced back to the work of Dedekind (see his
paper of 1897, [Ded31]), and S´os (see [Sos05] and [Sos06]). For prime denominator
n = p the number of parameters that could be used in principle is 2
k − k − 1, since
here there are restrictions on k of the parameters, (for details see [Els98]). It is
thus conceivable to prove a slightly better sieve bound, using the methods of this
paper.
Viola made use of k, and Shen made use of k + 1 parameters. Shen used one
parameter that occurs in all fractions and k parameters that occur in all but one
fraction. For k = 4, their approach starts with

Viola: m
n = 1
x123x124x134x1234 + 1
nx123x124x1234

+ 1
nx123x134x1234 + 1
nx124x134x1234 .

Shen: m
n = 1
x123x124x134x1234 + 1
nx123x124x234x1234

+ 1
nx123x134x234x1234 + 1
nx124x134x234x1234 .

From our starting point (3.1) we proceed to solve certain residue classes:

with x134 + x12x24x124 + x12x23x123 = rx23x24x234 (say)

we ﬁnd that n =(mx12x23x24x123x124x234x1234 − 1) r

− mx12x123x124x1234 (x12x23x123 + x12x24x124)

is soluble. We see that we can solve the equation for certain residue classes. This
means for all n in certain residue classes one can ﬁnd a solution.

Step 2: Uniqueness of the residue classes. In order to apply an upper bound
sieve we have to count the number of residue classes which can be treated as above.
We must ensure that each sifted class is counted at most once. We shall show that
suitable conditions on the size of the parameters and a square-free condition en-
tails that two distinct factorizations of x12x23x24x123x124x234x1234 lead to distinct
residue classes such that each counted class is counted at most once.

Step 3: Counting the number of eliminable residue classes. It turns out
that the number ω(q) of residue classes to be counted can be written as ω(q) ≈
d2k−1−1 ( q+1
m )
,where d2k−1−1 is the divisor function counting the number of ways

SUMS OF k UNIT FRACTIONS 3213

in whicha number canbe writtenasa productof2k−1 − 1 factors. We shall prove
that
 (log x)
2
k−1−2 ≪ ∑

q≤x
q prime
 ω(q)
q .

Step 4: The large sieve argument. A general large sieve device due to Vaughan
immediately implies the theorem.

4. The Starting Point

Our starting point is as follows:
m
p = 1
[
1 ⊕ 2]
x134...k + 1
p[2] + 1
p[2 ⊕ 3]
x134...k + ... + 1
p[
2 ⊕ k]x134...k .

This implies that

m[
2]
x134...k = p[
2 ⊖ 1] + x134...k + [
2 ⊖ 3] + ... + [2 ⊖ k]
.

The left hand side is divisible by [2 ⊖ 1] hence the right hand side must also be
divisible by [
2 ⊖ 1]
. So, for some positive integer r:
[
2 ⊖ 1]
r = x134...k + [
2 ⊖ 3] + ... + [2 ⊖ k]
.

We then divide by [
2 ⊖ 1] and get

m[2 ⊕ 1]
x134...k = p + r.

We re-substitute x134...k = [2 ⊖ 1]
r − [2 ⊖ 3] − ... − [
2 ⊖ k],and obtain

m[2 ⊕ 1]([2 ⊖ 1]
r − [
2 ⊖ 3] − ... − [2 ⊖ k]) = p + r.

Hence,
 p = (
m[2 ⊕ 1][
2 ⊖ 1] − 1) r − m[2 ⊕ 1]([2 ⊖ 3] + ... + [2 ⊖ k])

= (
m[2] − 1) r − m[
1 ⊕ 2]([2 ⊖ 3] + ... + [
2 ⊖ k]) .

In particular, we can solve the equation (1.1) for all integers n in the residue
class
 −m[
1 ⊕ 2]([2 ⊖ 3] + ... + [2 ⊖ k]) mod q = m[2] − 1.

5. Uniqueness of the Residue Classes

5.1. Introduction. In this section we shall show how to ensure that each elim-
inable residue class is counted not more than once. For this purpose we introduce
certain restrictions on the parameters. On the one hand, these restrictions are suf-
ﬁciently strong to ensure that each class we count is counted once. On the other
hand, they are suﬃciently weak to ensure that the number of counted classes is on
average of the same order as the number of those classes for which the equation is
generally soluble.
Following the ideas of Vaughan, Viola, and Shen, it seemed to be suitable to
restrict the size of the parameters, to take some of the parameters to be square-
free, and to omit small primes q. Using combinatorial ideas that go beyond the
work of Vaughan, Viola, and Shen, it turns out that these restrictions suﬃce to
ensure the uniqueness of the residue classes:

3214 CHRISTIAN ELSHOLTZ

Theorem 5.1 (Uniqueness of the residue class). Let q be prime with q> qm,k.
We use the enumeration of the parameters as speciﬁed in section 5.2.1 below. Let
the size of the parameters be restricted as follows: For the i-th parameter yi,we
have [2]
ϑi ≤ yi, where ϑi = 3
4i . Let [2]
x12x234...k be square-free. Suppose that we have
two factorizations of q+1
m with the above restrictions on the parameters.

q +1
m =[2] = x12x123 ··· =˜x12 ˜x123 ··· = ˜[2].

Suppose that the corresponding eliminable classes of these two factorizations are
congruent modulo q

[1 ⊕ 2]
(
[2 ⊖ 3] + ... +[2 ⊖ k]
) ≡ ˜[1 ⊕ 2]
( ˜[2 ⊖ 3] + ... + ˜[2 ⊖ k]
) mod q.

Then, for any pair (xI , ˜xI ) of corresponding parameters with an admissible index
set I, pairwise identity holds:
 xI =˜xI .

This means that the factorization of q+1
m with the above restrictions is unique.

The proof of this result requires several steps and lemmas.

Part 1. Firstly, we give the details of the suitable order of the parameters and the
restriction on the size of the parameters.

Part 2. Suppose that we have two factorisations of q+1
m =[2] = ˜[2].
Suppose that the eliminable classes

[1 ⊕ 2]
(
[2 ⊖ 3] + ... +[2 ⊖ k]
) and ˜[1 ⊕ 2]
( ˜[2 ⊖ 3] + ... + ˜[2 ⊖ k]
)

that correspond to the factorizations [2] = ˜[2] are congruent modulo q,where q is
prime. We will show that suitable restrictions on the size of the parameters ensure
that [1 ⊕ 2]
(
[2 ⊖ 3] + ... +[2 ⊖ k]
) = ˜[1 ⊕ 2]
( ˜[2 ⊖ 3] + ... + ˜[2 ⊖ k]
)
.

Part 3. Using the size of the parameters and omitting small primes, we shall
subsequently show that [1 ⊕ 2][2 ⊖ r]= ˜[1 ⊕ 2] ˜[2 ⊖ r]for r = k, k − 1, ··· , 3.

Part 4. Given the identity of a pair of ‘long’ products of corresponding parameters
(see part 3) our next step is to deduce the identity of suitable pairs of ‘shorter sub-
products’, and ﬁnally for all pairs of admissible parameters xI =˜xI .

5.2. The details. Since some of the details are somewhat involved we invite the
reader ﬁrst to work through the proof in the case k = 4. We give some details for
this case in section 5.3. Parts 1-3 closely follow the arguments of Viola. In part
4 however, we need to split long products into short ones, a problem that did not
occur in Viola’s or Shen’s presentation.

SUMS OF k UNIT FRACTIONS 3215

5.2.1. Part 1. We enumerate the K − 1 admissible parameters as follows: The ﬁrst
k − 1 parameters are

y1 = x12,y2 = x123,y3 = x1234,... ,yk−1 = x123...k.

Then we continue with yk = x124,... ,y2k−4 = x12k and y2k−3 = x1235,y2k−2 =
x1236,... ,y(k2−k−4)/2 = x12(k−1)k etc. up to

y2k−2−k+4 = x1234...(k−2)k,... ,y2k−2 = x124...(k−1)k.

Similarly, y2k−2+1 = x23,... ,y2k−2+k−2 = x2k,then x234,x235,... ,x2(k−1)k etc. up
to x234...(k−2)(k−1),... ,x24...(k−1)k, and ﬁnally yK−1 = x234...(k−2)(k−1)k.

Put ϑi = 3
4i . In particular, we ﬁnd that

[1 ⊕ 2] ≥ x12x123 ··· x123...k ≥ [2]
1− 1
4k−1 ,

[2 ⊕ k] ≥ x123...k =[2] 3
4k−1 ,

For r ≥ 3: [2 ⊖ r] ≥ x12x123 ··· x123...(r−1) ≥ [2]
1− 1
4r−2 ,

[2 ⊕ (r − 1)] ≥ x123...(r−1) ≥ [2] 3
4r−2 .

We also put an upper bound on the parameters

[2]
ϑi ≤ yi ≤ [2]
ϑi+η (i =2,... ,K − 1) with η = 1
K4K−1 .

Note that ∑K−1
i=2 (ϑi + η) < 1
4 . It is important that we do not impose such an upper
bound on the parameter y1 = x12.We observe that

[2 ⊖ 3] ≤ [2 ⊖ 4] ≤ ... ≤ [2 ⊖ k].

5.2.2. Part 2.

Lemma 5.2 (Compare [Vio73]). Suppose that we have two factorizations of q+1
m ,

q +1
m =[2] = ˜[2],

with the above restrictions on the parameters. Suppose that

[1 ⊕ 2]
(
[2 ⊖ 3] + ... +[2 ⊖ k]
) ≡ ˜[1 ⊕ 2]
( ˜[2 ⊖ 3] + ... + ˜[2 ⊖ k]
) mod q.(5.1)

We then have

[1 ⊕ 2]
([2 ⊖ 3] + ... +[2 ⊖ k]
) = ˜[1 ⊕ 2]
( ˜[2 ⊖ 3] + ... + ˜[2 ⊖ k]
)
.(5.2)

Proof. Note that ([2],q)=1.

[1 ⊕ 2]
(
[2 ⊖ 3] + ... +[2 ⊖ k]
) ≡ ˜[1 ⊕ 2]
( ˜[2 ⊖ 3] + ... + ˜[2 ⊖ k]
) mod q,
[2]
[2 ⊖ 1]
 ([2 ⊖ 3] + ... +[2 ⊖ k]
) ≡ [2]
˜[2 ⊖ 1]
 ( ˜[2 ⊖ 3] + ... + ˜[2 ⊖ k]
) mod q,

˜[2 ⊖ 1]
([2 ⊖ 3] + ... +[2 ⊖ k]
) ≡ [2 ⊖ 1]
( ˜[2 ⊖ 3] + ... + ˜[2 ⊖ k]
) mod q.

3216 CHRISTIAN ELSHOLTZ

Therefore

0 ≤ ˜[2 ⊖ 1]
(
[2 ⊖ 3] + ... +[2 ⊖ k]
) ≤ (k − 2) ˜[2 ⊖ 1][2 ⊖ k]

≤ (k − 2) [2] [2]
˜[1 ⊕ 2][2 ⊕ k]
≤ (k − 2)[2]
1− 2
4k−1 <m[2] − 1= q.

Analogously
 0 ≤ [2 ⊖ 1]
( ˜[2 ⊖ 3] + ... + ˜[2 ⊖ k]
) <q.

Therefore (5.1) implies that

˜[2 ⊖ 1]
([2 ⊖ 3] + ... +[2 ⊖ k]
) =[2 ⊖ 1]
( ˜[2 ⊖ 3] + ... + ˜[2 ⊖ k]
)
.

Hence the asserted identity (5.2) must also hold.

5.2.3. Part 3.

Lemma 5.3 (Compare [Vio73]). Suppose, as in the previous lemma, that we have
two factorizations of q+1
m =[2] =[˜2] with the restrictions on the parameters men-
tioned above. Let us further suppose that q> qm,k and that

[1 ⊕ 2]
([2 ⊖ 3] + ... +[2 ⊖ k]
) = ˜[1 ⊕ 2]
( ˜[2 ⊖ 3] + ... + ˜[2 ⊖ k]
)
.

Then
 [1 ⊕ 2][2 ⊖ r]= ˜[1 ⊕ 2] ˜[2 ⊖ r] for r =3, ··· ,k.

Proof. We ﬁrst prove [1 ⊕ 2][2 ⊖ r]= ˜[1 ⊕ 2] ˜[2 ⊖ r]for r = k and then, successively,
for r = k − 1,k − 2,... , 3. For r = k we have that

∣
∣
∣[1 ⊕ 2][2 ⊖ r] − ˜[1 ⊕ 2] ˜[2 ⊖ r]∣
∣
∣

= ∣
∣
∣ ˜[1 ⊕ 2]
( ˜[2 ⊖ 3] + ... + ˜[2 ⊖ r − 1]
) − [1 ⊕ 2]
(
[2 ⊖ 3] + ... +[2 ⊖ r − 1]
)∣
∣
∣ .

Suppose, for a contradiction, that [1 ⊕ 2][2 ⊖ r] ̸= ˜[1 ⊕ 2] ˜[2 ⊖ r]. The idea is to
deduce contradicting upper and lower bounds for

∣
∣
∣ ˜[2 ⊖ 1][2 ⊖ r] − [2 ⊖ 1] ˜[2 ⊖ r]∣
∣
∣.

SUMS OF k UNIT FRACTIONS 3217

The upper bound:
∣
∣
∣ ˜[2 ⊖ 1][2 ⊖ r] − [2 ⊖ 1] ˜[2 ⊖ r]∣
∣
∣

= [2 ⊖ 1] ˜[2 ⊖ 1]
[2]
 ∣
∣
∣[1 ⊕ 2][2 ⊖ r] − ˜[1 ⊕ 2] ˜[2 ⊖ r]∣
∣
∣

= [2 ⊖ 1] ˜[2 ⊖ 1]
[2]
 ∣
∣
∣ ˜[1 ⊕ 2]
( ˜[2 ⊖ 3] + ... + ˜[2 ⊖ (r − 1)]
)

−[1 ⊕ 2]
(
[2 ⊖ 3] + ... +[2 ⊖ (r − 1)]
)∣
∣
∣

= [2 ⊖ 1] ˜[2 ⊖ 1]
[2]
 ∣
∣
∣ [2]
˜[2 ⊖ 1]
 ( ˜[2 ⊖ 3] + ... + ˜[2 ⊖ (r − 1)]
)

− [2]
[2 ⊖ 1]
 ([2 ⊖ 3] + ... +[2 ⊖ (r − 1)]
)∣
∣
∣

= ∣
∣
∣[2 ⊖ 1]
( ˜[2 ⊖ 3] + ... + ˜[2 ⊖ (r − 1)]
)

− ˜[2 ⊖ 1]
([2 ⊖ 3] + ... +[2 ⊖ (r − 1)]
)∣
∣
∣

< max(
(r − 3)[2 ⊖ 1] ˜[2 ⊖ (r − 1)], (r − 3) ˜[2 ⊖ 1][2 ⊖ (r − 1)]
)

≤ (r − 3) max
( [2]
2

[1 ⊕ 2] ˜[2 ⊕ (r − 1)] , [2]
2

˜[1 ⊕ 2][2 ⊕ (r − 1)]
 )

≤ (r − 3)[2]
2−(1− 1
4k−1 )− 3
4r−2 .

The lower bound:∣
∣
∣ ˜[2 ⊖ 1] ˜[2 ⊕ r] − [2 ⊖ 1][2 ⊕ r]
∣
∣
∣ is an integer ≥ 0. By our assumption,

[1 ⊕ 2][2 ⊖ r] ̸= ˜[1 ⊕ 2] ˜[2 ⊖ r]

⇔ [2]
[2 ⊖ 1] [2]
[2 ⊕ r] ̸= [2]
˜[2 ⊖ 1]
 [2]
˜[2 ⊕ r]
⇒ ∣
∣ ˜[2 ⊖ 1] ˜[2 ⊕ r] − [2 ⊖ 1][2 ⊕ r]
∣
∣ ̸=0
Hence ∣
∣ ˜[2 ⊖ 1] ˜[2 ⊕ r] − [2 ⊖ 1][2 ⊕ r]
∣
∣ ≥ 1.

∣
∣
∣ ˜[2 ⊖ 1][2 ⊖ r] − [2 ⊖ 1] ˜[2 ⊖ r]∣
∣
∣ = [2]

[2 ⊕ r] ˜[2 ⊕ r]
 ∣
∣
∣ ˜[2 ⊖ 1] ˜[2 ⊕ r] − [2 ⊖ 1][2 ⊕ r]
∣
∣
∣

≥ [2]

[2 ⊕ r] ˜[2 ⊕ r] = [2 ⊖ r] ˜[2 ⊖ r]
[2]

≥ [2]
2(1− 1
4r−2 )−1.

Combining the lower and upper bound, yields

[2]
2(1− 1
4r−2 )−1 ≤ (r − 3)[2]
2−(1− 1
4k−1 )− 3
4r−2

which leads to [2] 3
4r−1 ≤ (r − 3).
Hence we ﬁnd for suﬃciently large q a contradiction for r = k and can inductively
assume that the lemma has been proven for k, ··· ,r+1. The same argument proves
the lemma for any r ≥ 3.

5.2.4. Part 4. It will be our aim now to split ‘long’ products like [1 ⊕ 2][2 ⊖ r]into
‘short’ ones such that we ﬁnally get the identity of the single parameters xI =˜xI .
In this part we also make use of a restriction on the multiplicative structure of [2].

3218 CHRISTIAN ELSHOLTZ

We assume that [2]
x12x234···k is square-free. In particular, we do not assume that x12
is square-free.
We know that
 [1 ⊕ 2][2 ⊖ 3] = ˜[1 ⊕ 2] ˜[2 ⊖ 3]
[1 ⊕ 2][2 ⊖ 4] = ˜[1 ⊕ 2] ˜[2 ⊖ 4]
... ... ...
[1 ⊕ 2][2 ⊖ k]= ˜[1 ⊕ 2] ˜[2 ⊖ k].

Multiplying these equations leads to

[1 ⊕ 2]
k−2[2 ⊖ 3][2 ⊖ 4] ... [2 ⊖ k]= ˜[1 ⊕ 2]
k−2 ˜[2 ⊖ 3] ˜[2 ⊖ 4] ... ˜[2 ⊖ k].

Writing this equation in terms of the single parameters, in decreasing order of their
exponents, leads to

(x12)
2k−4(x123x124 ...x12k)
2k−5(x1234x1235 ...x12(k−1)k)
2k−6 ... (x123...k)
k−2

× (x23x24 ...x2k)
k−3(x234x235 ...x2(k−1)k)
k−4 ... (x234...k)
0

=(˜x12)
2k−4(˜x123 ˜x124 ... ˜x12k)
2k−5(˜x1234 ˜x1235 ... ˜x12(k−1)k)
2k−6 ... (˜x123...k)
k−2

× (˜x23 ˜x24 ... ˜x2k)
k−3(˜x234 ˜x235 ... ˜x2(k−1)k)
k−4 ... (˜x234...k)
0.

Any divisor of the left hand side taken to the r-th (say) power must also be
taken to the r-th power on the right hand side. By the uniqueness of the prime
factorization and since [2]
x12x234...k and [2]
˜x12 ˜x234...k are square-free, we can see that

x12 =˜x12
x123x124 ... x12k =˜x123 ˜x124 ... ˜x12k
x1234x1235 ...x12(k−1)k =˜x1234 ˜x1235 ... ˜x12(k−1)k
... ... ...
x123...k =˜x123...k

and
 x23x24 ... x2k =˜x23 ˜x24 ... ˜x2k
x234x235 ...x2(k−1)k =˜x234 ˜x235 ... ˜x2(k−1)k
... ... ...
x234...k =˜x234...k.

One can ﬁrst prove the ﬁrst line. For the following lines we can use the principle:
Suppose that pra
1 prb
2 =˜pra
1 ˜prb
2,where the pri stand for any product of parameters
and where a ̸= b.Then gcd(pr1,pr2) = 1 and gcd( ˜pr1, ˜pr2) = 1 implies that
pr1 =˜pr1 and pr2 =˜pr2. The very last of these equations, x234...k =˜x234...k,
requires a further explanation. Let I run through the admissible index sets. We
know that [2] = ∏
I xI = ∏I ˜xI = ˜[2]. Hence the identity x234...k =˜x234...k follows,
since these are the only parameters that do not occur in any of the above equations.
Note that

x12(x123x124 ... x12k) ...x123...k =˜x12(˜x123 ˜x124 ... ˜x12k) ... ˜x123...k,

i.e. [1 ⊕ 2] = ˜[1 ⊕ 2].
(5.3)
 SUMS OF k UNIT FRACTIONS 3219

This implies
 [2 ⊖ a]= ˜[2 ⊖ a], (a =3,... ,k).

We now aim to prove that xI =˜xI , for any pair xI and ˜xI of corresponding
parameters with admissible index set I.Let J = {i1,i2, ··· ,ir}⊆ {3, 4,... ,k}.
We will show that x12J =˜x12J and x2J =˜x2J .
We can express the product x12J x2J as follows:

[2 ⊕ i1 ⊕ i2 ⊕ ... ⊕ ir ⊖ ir+1 ⊖ ... ⊖ ik−2].

Then consider the product
∏

b̸=i1,i2,... ,ir[2 ⊖ b]= [2 ⊖ 3][2 ⊖ 4][2 ⊖ 5] ... [2 ⊖ k]
[2 ⊖ i1][2 ⊖ i2] ... [2 ⊖ ir] = ∏

b̸=i1,i2,... ,ir
 ˜[2 ⊖ b].

The greatest exponent that occurs in this product is k − r − 2. The parameters
that occur with exponent k − r − 2are x12,x12i1i2...ir and x2i1i2...ir .We already
know that x12 =˜x12, and hence we can deduce that

x12i1i2...ir x2i1i2...ir =˜x12i1i2...ir ˜x2i1i2...ir .

This implies with (5.3) that

∏

3≤j1<j2<...<jr
˜x12j1j2...jr = ˜x12i1i2...ir ˜x2i1i2...ir
x2i1i2...ir
 ∏

3≤j1<j2<...<jr
x12j1j2...jr

x12i1i2...ir ,

˜x2i1i2...ir ∏

3≤j1<j2<...<jr ,
but not (j1=i1,... ,jr =ir )

x12j1j2...jr = x2i1i2...ir ∏

3≤j1<j2<...<jr ,
but not (j1=i1,... ,jr=ir )

˜x12j1j2...jr .

The square-free condition implies that

x2i1i2...ir =˜x2i1i2...ir .

It immediately follows that
 x12i1i2...ir =˜x12i1i2...ir .

5.3. The case k =4. In this section we give some further details for the case
k = 4, so that the reader can more easily work through the last section. We take
y1 = x12,y2 = x123,y3 = x1234,y4 = x124,y5 = x23,y6 = x24,y7 = x234.
[2] = x12x123x124x1234x23x24x234 and for example [2]
3/4 ≤ y1 ≤ [2]
3/4+1/(7·4
7).The
soluble residue class is x12x123x124x1234(x12x124x24 + x12x123x23) modulo m[2] − 1.
Suppose there are two factorizations of [2], namely

x12x123x124x1234x23x24x234 =˜x12 ˜x123 ˜x124 ˜x1234 ˜x23 ˜x24 ˜x234

and suppose that x123x124x1234x23x24 and ˜x123 ˜x124 ˜x1234 ˜x23 ˜x24 are square-free. We
know that
 x12x123x124x1234x12x123x23 =˜x12 ˜x123 ˜x124 ˜x1234 ˜x12 ˜x123 ˜x23,(5.4)
 x12x123x124x1234x12x124x24 =˜x12 ˜x123 ˜x124 ˜x1234 ˜x12 ˜x124 ˜x24.(5.5)

Multiplying both equations gives the equality

x
4
12x
3
123x
3
124x
2
1234x
1
23x
1
24x
0
234 =˜x
4
12 ˜x
3
123 ˜x
3
124 ˜x
2
1234 ˜x
1
23 ˜x
1
24 ˜x
0
234.

3220 CHRISTIAN ELSHOLTZ

The square-freeness implies that
 x12 =˜x12,

x123x124 =˜x123 ˜x124,
x1234 =˜x1234,

x23x24 = x123x124,
x234 =˜x234.

Combining this with (5.4) gives
 x23x123 =˜x23 ˜x123.

Combining this with x123x124 =˜x123 ˜x124 gives

x23 ˜x123 ˜x124 =˜x23 ˜x123x124.

Any factor in x23 must (because of the square-free condition) occur in ˜x23 and vice
versa. This implies x23 =˜x23. The arguments for the other parameters are similar.

6. The Number of Eliminable Classes

6.1. Lower bound estimate of ∑

q≤x ω(q). We now count the number ωm,k(q)of

residue classes modulo q for which we can solve the equation. As before, q denotes
a prime. In view of theorem 7.2, we aim to ﬁnd a lower bound on ∑

q≤x
 ωm,k(q)
q .

Let dK−1,[2](n):= ∑

y1y2...yK−1=n
yi≥[2]ϑi
 1and d
′
K−2,[2](n)= ∑

y2...yK−1=n
yi≥[2]ϑi
 1.

Note that
 dK−1,[2](n)= ∑

[2]ϑ1 ≤x12
x12|n
 d
′
K−2,[2]( n
x12 )

and that for [2] ≤ x
 d
′
K−2,[2](n) ≥ d
′
K−2,x(n).

By the above considerations concerning the ‘uniqueness of the residue class’, we
can eliminate the following number of residue classes modulo q:

ωm,k(q)=
 



 ∑

[2]ϑ1 ≤x12
x12| q+1
m
 µ
2 ( q+1
mx12
 ) d
′
K−2,[2] ( q+1
mx12
 ) if q ≡−1mod m and
q> qm,k,

0otherwise.

Theorem 6.1 (Compare [Vau70] for the case k =3). We have the following lower
bound: ∑

q≤x ωm,k(q) ≫m,k x(log x)
K−3.

By partial summation this implies the following corollary:

SUMS OF k UNIT FRACTIONS 3221

Corollary 6.2.
 ∑

q≤x
 ωm,k(q)
q ≫m,k (log x)
K−2.

Proof of the theorem.

∑

q+1
m ≤x ωm,k(q)= ∑

q+1
m =[2]≤x
 ∑

x12| q+1
m
[2]
3/4≤x12
 d
′
K−2,[2]
 ( q +1
mx12
 ) µ
2 ( q +1
mx12
 )

≥ ∑

x
2 < q+1
m ≤x
 ∑

x12| q+1
m
x3/4≤x12
 d
′
K−2,x
 ( q +1
mx12
 ) µ
2 ( q +1
mx12
 )

= ∑

x
2 < q+1
m ≤x
 ∑

r| q+1
m
r≤x1/4
 d
′
K−2,x(r)µ
2(r)

= ∑

r≤x1/4 µ
2(r)d
′
K−2,x(r) (π(x; mr, −1) − π( x
2 ; mr, −1)
)

≥ ∑

r≤x1/4 µ
2(r)d
′
K−2,x(r) ( li(x) − li( x
2 )
ϕ(mr)
 )

+ ∑

r≤x1/4 µ
2(r)d
′
K−2,x(r) ((π(x; mr, −1) − π( x
2 ; mr, −1)
) − ( li(x) − li( x
2 )
ϕ(mr)
 ))

≥ ∑

r≤x1/4 µ
2(r)d
′
K−2,x(r) ( li(x) − li( x
2 )
ϕ(mr)
 ) + R(x)(say)

≫ 1
m x
log x
 ∑

r≤x1/4
 µ
2(r)
ϕ(r) d
′
K−2,x(r)+ R(x)

≫ x
log x
 ∑

y2y2...yK−1≤x1/4

yi≥xϑi
 µ
2(y2 ... yK−1)
ϕ(y2 ...yK−1) + R(x)

≫ x
log x
 ∑

xϑi ≤yi≤xϑi+η
 µ
2(y2 ... yK−1)
ϕ(y2 ...yK−1) + R(x)

≫ x
log x (log x)K−2 + R(x) by theorem 6.4 below

≫ x(log x)
K−3 + R(x).

The error term is

R(x)= ∑

r≤x1/4 µ
2(r)d
′
K−2,x(r) ((
π(x; mr, −1) − π( x
2 ; mr, −1)
)−( li(x) − li( x
2 )
ϕ(mr)
 )) .

3222 CHRISTIAN ELSHOLTZ

For the estimate of the error term note that d
′
K−2,x(r) ≤ dK−2(r).

|R(x)|≤
 ∣
∣
∣
∣
∣
∣
 ∑

r≤x1/4
 µ
2(r)d
′
K−2,x(r)
√
ϕ(r)
 √
ϕ(mr) ((π(x; mr, −1) − π( x
2 ; mr, −1)
)

− ( li(x) − li( x
2 )
ϕ(mr)
 )) ∣
∣
∣
∣
∣
∣

by the Cauchy-Schwarz inequality

≪
 

 ∑

r≤x1/4
 µ
2(r)(dK−2(r))2

ϕ(r)
 



1/2

×



 ∑

r≤x1/4 ϕ(mr) ((π(x; mr,−1)−π( x
2 ; mr,−1)
)−( li(x)−li( x
2 )
ϕ(mr)
 ))2


1/2

by the Brun-Titchmarsh theorem:

ϕ(mr) ∣
∣
∣
∣(π(x; mr, −1) − π( x
2 ; mr, −1)
) − ( li(x) − li( x
2 )
ϕ(mr)
 )∣
∣
∣
∣ ≪ x
log x
and by lemma 6.3 below

≪ ((log x)(K−2)2)1/2 

 x
log x
 ∑

r≤x1/4
 ∣
∣
∣
∣(
π(x; mr, −1) − π( x
2 ; mr, −1)
)

− ( li(x) − li( x
2 )
ϕ(mr)
 )∣
∣
∣
∣
 


1/2

by the Bombieri-Vinogradov theorem for an arbitrary constant A,

≪ x
(log x)A for an arbitrary constant A.

Lemma 6.3 (This is lemma 4 of [Vio73]).

∑

n≤x µ
2(n) d
l
k(n)
ϕ(n) ≪ (log x)
kl .

6.2. An estimate on ∑

xαi ≤ni≤xβi
 µ
2(n1...ns)
n1...ns . Recall that in corollary 6.2 for estab-

lishing the lower bound of the main term, we have used

∑

xϑi ≤yi≤xϑi+η
 µ
2(y2 ...yK−1)
ϕ(y2 ... yK−1) ≫ (log x)
K−2.

This follows immediately from the following theorem:

SUMS OF k UNIT FRACTIONS 3223

Theorem 6.4. Let 0 <αi <βi < 1,for i =1, ··· ,s. Then the following inequality
holds: ∑

xαi ≤ni≤xβi
i=1,... ,s
 µ
2(n1n2 ...ns)
n1n2 ...ns ≫s (log x)
s s∏

i=1(βi − αi).

The proof below was suggested to me by Roger Heath-Brown. It simpliﬁed my
own proof considerably.
We put αmin =min
1≤i≤s αi.Let p stand for a prime and let w be an integer

parameter that may increase with x,whereas R is a ﬁxed positive integer. Let r
be an integer 0 <r ≤ R.Let also be 0 <αi <βi < 1, for i =1, ··· ,s.

Lemma 6.5. For x> 0 we have that
∑

1≤n≤x
 1
n =log x + γ + O ( 1
x1/4
 ) .

For x ≥ 1 this follows from ∑

1≤n≤x 1
n =log x+ γ + O ( 1
x ) . For x< 1 this follows
from | log x + γ| = Oε( 1
xε ) for any positive ε.
The easy proof of the following lemma is left to the reader.

Lemma 6.6. Suppose that (w, R)=1.
∑

xα<n≤xβ
w|n
n≡r modR
 1
n = (β − α)log x
wR + O ( 1
xα/4 w3/4
 ) .

If p2|n1 ··· ns,where p is a prime, then either for some nu we have that p2|nu or
for some nu and nv (with u ̸= v) wehavethat p|nu and p|nv. Thusit isenough
to consider the case that p2 divides a product of two of the parameters. Let ∑′

denote that the sum is taken over the nu and nv satisfying the following conditions.

x
αu <nu ≤ x
βu ,x
αv <nv ≤ x
βv ,nu ≡ ru mod R, nv ≡ rv mod R.

Lemma 6.7.

∑′

p2|nunv
 1
nunv = (
3 − 2
p
 ) (βu − αu)(βv − αv)
R2 p2 (log x)
2 + O ( log x
xmin(αu,αv )/4 p3/2
 ) .

Proof of the lemma.
∑′

p2|nunv
 1
nunv = ∑′

p2|nu
 1
nunv + ∑′

p2|nv
 1
nunv + ∑′

p|nu,p|nv
 1
nunv

− ∑′

p2|nu,p|nv
 1
nunv − ∑′

p|nu,p2|nv
 1
nunv

= S1 + S2 + S3 − S4 − S5 (say).

The lemma follows with

S1,2,3 = (βu − αu)(βv − αv)
p2 R2 (log x)
2 + O ( log x
xmin(αu,αv )/4 p3/2
 ) .

3224 CHRISTIAN ELSHOLTZ

S4,5 = (βu − αu)(βv − αv)
p3 R2 (log x)
2 + O ( log x
xmin(αu,αv)/4 p9/4
 ) .

Proposition 6.8. Let p denote a prime and suppose that (p, R)= 1.Then we
have that

∑

xαi <ni≤xβi
p
2|n1···ns
ni≡ri modR
 1
n1 ··· ns = 1
Rs
 ( s(s +1)
2p2 + Os( 1
p3 )
) ( s∏

i=1(βi − αi)

)
 (log x)
s

+Os
 ( (log x)
s−1

xαmin/4 p3/2
 ) .

Proof of the proposition. To prove the proposition one applies the above lemma to
all s cases with p2|nu and all s(s−1)
2 cases with p|nu,p|nv. This explains the s(s+1)
2p2
part. Other cases like p2|nu,p|nv give the Os( 1
p3 ) part. The other factors are of

the type ( (βi−αi)
R log x + O ( 1
xαi/4 )). Thus multiplying and collecting error terms
proves the proposition.

The proposition implies the following corollary:

Corollary 6.9. Let p denote a prime and suppose that (p, R)= 1. Then there
exists a constant Cs such that the following inequality holds:
∑

xαi <ni≤xβi
p
2|n1···ns
ni≡ri modR
 1
n1 ··· ns ≤ Cs
p2 Rs (log x)
s.

Proof of theorem 6.4. Let Qs denote a ﬁxed integer to be determined below.
If (n, ∏
p≤Qs p2)= 1, then n is trivially square-free with regard to primes p ≤ Qs.
For such n we see that µ
2(n) ≥ 1 − ∑p>Qs
p
2|n 1.

Let us choose R = ∏
p≤Qs p2. To ensure that n1n2 ··· ns is square-free with
regard to primes p ≤ Qs it is enough to choose ni ≡ 1mod R for all i =1, ··· ,s.
Hence
∑

xαi <ni≤xβi
ni≡1modR
 µ
2(n1 ··· ns)
n1 ··· ns ≥ ∑

xαi <ni≤xβi
ni≡1modR
 1
n1 ··· ns − ∑

p>Qs
p
2|n1···ns
 ∑

xαi <ni≤xβi
ni≡1modR
 1
n1 ··· ns

≥ 1
Rs
 s∏

i=1(βi − αi)(log x)
s + Os
 ( (log x)
s−1

xαmin/4
 )

− ∑

p>Qs
 1
p2 Cs
Rs
 s∏

i=1(βi − αi)(log x)
s + Os
 

 ∑

p>Qs
 1
p3/2 (log x)
s−1

xαmin/4
 



=
 

1 − Cs ∑

p>Qs
 1
p2
 

 1
Rs
 s∏

i=1(βi − αi)(log x)
s + Os
 ( (log x)
s−1

xαmin/4
 ) .

SUMS OF k UNIT FRACTIONS 3225

We now choose Qs suﬃciently large such that Cs ∑p>Qs 1
p2 < 1. The theorem
follows immediately.
 7. The Final Sieve Result

We will use Montgomery’s version of the large sieve.

Theorem 7.1 (see [Mon78]). Let P denote the set of primes. Let p be a prime. Let
A be a set of integers which avoids ω(p) residue classes modulo p.Here ω : P→ N
with 0 ≤ ω(p) ≤ p − 1.Let A(x) denote the counting function A(x)= ∑a≤x,a∈A 1.
Then the following upper bound on the counting function holds:

A(N ) ≤ 2N
L , where L = ∑

q≤N 1/2 µ
2(q) ∏

p|q
 ω(p)
p − ω(p) .

Vaughan generally proved a lower bound estimate for L, when a lower bound for
∑

p≤x
 ω(p)
p is known.

Theorem 7.2 (Vaughan, [Vau73]). Let α> 0,C1 > 0. If, for suﬃciently large x,
the inequality
 ∑

p≤x
 ω(p)
p >C1(log x)
α

holds, then there is a positive constant C(α, C1) such that

L> exp (C(α, C1)(log N )
 α
α+1 ) .

Hence corollary 6.2 and theorem 7.2 immediately yield the following sieve bound,
which proves our theorem 1.3:

Em,k(N ) ≤ 2N exp (−cm,k(log N )
1− 1
2k−1 −1 ) .

Remark 7.3. For k = 3 we have worked out the following slightly more explicit
version of Vaughan’s theorem:
We may observe, that for k = 3 it suﬃces to apply the Bombieri-Vinogradov
theorem with an exponent of A = 3
2 in the upper bound ≪ x
(log x)A .For A< 2 − ε it
can be shown that the ≪-constant is eﬀective, (see [Kar93], page 140). (Vaughan’s
approach was slightly diﬀerent and required an A> 2.) Moreover, it is possible to
compute admissible values of the constants cm,k.
An admissible value for cm,3 is

cm,3 = 3

e 2
3
 ( 1
8m
 ) 1
3 − ε, where ε> 0.

In the case of the Erd˝os-Straus conjecture with m = 4 we found that c4,3 =0.5645
is an admissible value, (see [Els96]). This result holds for N> Nm,where Nm is, in
principle, eﬀective. An entirely eﬀective but very weak upper bound was recently
proven, (see [AB98]).

3226 CHRISTIAN ELSHOLTZ

References

[AB98] M.H. Ahmadi and M.N. Bleicher. On the conjectures of Erd˝os and Straus, and Sierpinski
on Egyptian fractions. Int. J. Math. Stat. Sci., 7:169–185, 1998. See also Zentralblatt
990.17875. MR 99k:11049
[Cro00] E.S. Croot. Unit Fractions. PhD thesis, University of Georgia, Athens, 2000. The thesis
is based on three papers: 1) On some questions of Erd˝os and Graham about Egyptian
fractions, to appear in Mathematika, 2) On unit fractions with denominators in short
intervals, to appear in Acta Arithmetica, 3) On a coloring conjecture about unit fractions.
[Ded31] R. Dedekind. ¨Uber Zerlegungen von Zahlen durch ihren gr¨oßten gemeinsamen Teiler,
(Festschrift der Universit¨at Braunschweig, 1897) in Gesammelte mathematische Werke,
Band 2. Braunschweig: Friedr. Vieweg & Sohn A.-G., 1931.
[EG80] P. Erd˝os and R.L. Graham. Old and New Problems and Results in Combinatorial
Number Theory.Universit´edeGen`eve, 1980. Monographie No. 28 de L’Enseignement
Math´ematique. MR 82j:10001
[Els96] C. Elsholtz. The Erd˝os-Straus conjecture on 4
n = 1
x + 1
y + 1
z . Diploma thesis, Technische
Universit¨at Darmstadt, 1996.
[Els98] C. Elsholtz. Sums of k Unit Fractions. PhD thesis, Technische Universit¨at Darmstadt,
1998.
[Erd50] P. Erd˝os. Az 1
x1 + 1
x2 + .. . + 1
xn = a
b egyenlet eg´esz sz´am´u megold´asair´ol (On a Dio-
phantine equation). Mat. Lapok, 1:192–210, 1950. MR 13:208b
[Gra64] R.L. Graham. On ﬁnite sums of unit fractions. Proc. London Math. Soc. (3), 14:193–207,
1964. MR 28:3968
[Guy94] R.K. Guy. Unsolved Problems in Number Theory, second edition. Springer-Verlag, 1994.
MR 96e:11002
[Kar93] A.A. Karatsuba. BasicAnalyticNumberTheory. Springer Verlag, 1993. MR 94a:11001
[Li81] Delang Li. On the Equation 4
n = 1
x + 1
y + 1
z . J. Number Theory, 13:485–494, 1981.
See also Letter to the editor, J. Number Theory 15:282, 1982. MR 83e:10026; MR
84b:10024
[Mar00] G. Martin. Denser Egyptian fractions. Acta Arith. 95:231–260, 2000.
[Mar99] G. Martin. Dense Egyptian fractions. Trans. Amer. Math. Soc., 351:3641–3657, 1999.
MR 99m:11035
[Mon78] H.L. Montgomery. The analytic principle of the large sieve. Bull. Amer. Math. Soc.,
84:547–567, 1978. MR 57:5931
[Mor69] L.J. Mordell. Diophantine Equations,volume 30 of Pure and Applied Mathematics.Aca-
demic Press, 1969. MR 40:2600
[Nak39] M. Nakayama. On the Decomposition of a Rational Number into “Stammbr¨uche”.
Tˆohuku Math. J., 46:1–21, 1939. MR 1:134c
[Nar86] W. Narkiewicz. Classical Problems in Number Theory,volume 62 of Mathematical Mono-
graphs. PWN, 1986. MR 90e:11002
[San91] J.W. Sander. On 4
n = 1
x + 1
y + 1
z and Rosser’s sieve. Acta Arith., 59:183–204, 1991. MR
92j:11031
[San94] J.W. Sander. On 4
n = 1
x + 1
y + 1
z and Iwaniec’ Half Dimensional Sieve. J. Number Theory,
46:123–136, 1994. MR 95e:11044
[San97] J.W. Sander. Egyptian Fractions and the Erd˝os-Straus Conjecture. Nieuw Arch. Wisk.
(4), 15:43–50, 1997. MR 98d:11039
[Scha] A. Schinzel. Erd˝os’s work on ﬁnite sums of unit fractions. To appear in Paul Erd˝os and
his Mathematics, Proceedings of the Erd˝os conference (Budapest 1999), (Editors: G.
H´alasz, L. Lov´asz, M. Simonovits, V. S´os).
[Sch00] A. Schinzel. On sums of three unit fractions with polynomial denominators. Funct. Ap-
prox. Comment. Math. 28:187–194, 2000.
[Sch56] A. Schinzel. Sur quelques propri´et´es des nombres 3
n et 4
n ,o`u n est un nombre impair.
Mathesis, 65:219–222, 1956. MR 18:284a
[Sch74] W. Schwarz. Einf¨uhrung in die Siebmethoden der analytischen Zahlentheorie. Bibli-
ographisches Institut, Mannheim, 1974. MR 53:13147
[She86] Shen Zun. On the diophantine equation ∑k
i=0 1
xi = a
n . Chinese Ann. Math. Ser. B,
7:213–220, 1986. MR 87j:11026

SUMS OF k UNIT FRACTIONS 3227

[Sie56] W. Sierpi´nski. Sur les d´ecompositions de nombres rationnels en fractions primaires. Math-
esis, 65:16–32, 1956. MR 17:1185d
[Sos05] E. S´os. Die diophantische Gleichung 1
x = 1
x1 + 1
x2 + ... + 1
xn . Zeitschrift f¨ur mathema-
tischen und naturwissenschaftlichen Unterricht, 36:97–102, 1905.
[Sos06] E. S´os. Zwei diophantische Gleichungen. Zeitschrift f¨ur mathematischen und naturwis-
senschaftlichen Unterricht, 37:186–190, 1906.
[Vau70] R.C. Vaughan. On a problem of Erd˝os, Straus and Schinzel. Mathematika, 17:193–198,
1970. MR 44:6600
[Vau73] R.C. Vaughan. Some Applications of Montgomery’s Sieve. J. Number Theory, 5:64–79,
1973. MR 49:7222
[Vio73] C. Viola. On the diophantine equations ∏k
0 xi − ∑k
0 xi = n and ∑k
0 1
xi = a
n . Acta Arith.,
22:339–352, 1973. MR 48:234
[Web70] W.A. Webb. On 4
n = 1
x + 1
y + 1
z . Proc. Amer. Math. Soc., 25:578–584, 1970. MR 41:1639

[Yan82] Xun Qian Yang. A note on 4
n = 1
x + 1
y + 1
z . Proc. Amer. Math. Soc., 85:496–498, 1982.
MR 83j:10017

Institut f¨ur Mathematik, Technische Universit¨at Clausthal, Erzstrasse 1, D-38678
Clausthal-Zellerfeld, Germany
E-mail address: elsholtz@math.tu-clausthal.de
