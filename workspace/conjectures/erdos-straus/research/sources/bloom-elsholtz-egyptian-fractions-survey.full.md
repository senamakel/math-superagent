<!-- source: https://arxiv.org/pdf/2210.04496v1 | converted from PDF -->

arXiv:2210.04496v1  [math.NT]  10 Oct 2022
Thomas F. Bloom
Mathematical Institute
University of Oxford
Woodstock Road
Oxford OX2 6GG, UK
bloom@maths.ox.ac.uk
 Christian Elsholtz
Institut f¨ur Analysis und Zahlentheorie
Technische Universit¨at Graz
Kopernikusgasse 24/II
A-8010 Graz, Austria
elsholtz@math.tugraz.at

Egyptian Fractions

1. Introduction
Scribes of Ancient Egypt had an un-
usual method of writing fractions:
they were always1 expressed as a sum
of distinct unit fractions 1/xi – for
example, 2
15 would instead be written
as 1
10 + 1
30 . The Papyrus Rhind [32],
written over 3500 years ago, contains
a table showing how to do this for the
most frequently used fractions 2/n.
It is unclear precisely why the Egyp-
tians wrote fractions in this form,
which seems quite complicated for us,
but the study of the equation

(1) m
n = 1
x1 + · · · + 1
xk

with m, n, x1, . . . , xk positive inte-
gers, where in some cases k is con-
sidered as ﬁxed and in other cases
k may vary, has been very fruit-
ful from a modern number theoretic
point of view. Equations with in-
teger or rational variables are called
“Diophantine equations”. Another
example of a Diophantine equation
is the Pythagorean triple x
2 + y2 =
z2, whose history goes back to Baby-
lonian clay tablets, and is given a
parametric solution in Euclid’s “El-
ements”.
The study of solutions to (1), so-
called ‘Egyptian fractions’, has an im-
portant caveat when compared to the
 study of general Diophantine equa-
tions: we usually limit our atten-
tion to those solutions with x1 <
x2 < · · · < xk – in particular, we
do not allow equality between the xi,
and always count solutions as ordered
tuples. For the study of Egyptian
fractions this is no loss of general-
ity: it has been observed by Take-
nouchi [42] that a fraction which can
be written as a sum of k unit frac-
tions with repeated fractions can also
be written as a sum of k unit frac-
tions with distinct fractions. To see
this, one can replace any multiple
occurrence of some xi by means of
the two formulae below, depending
on whether xi is odd or even: 1
2t +
1
2t = 1
t+1 + 1
t(t+1) and 1
2t+1 + 1
2t+1 =

1
t+1 + 1
(t+1)(2t+1) . Note that the sum
of the denominators increases by this
replacement. One possibly has to re-
peat this, but as the sum of the de-
nominators increases, and as there is
only a bounded number of ways to
write a fraction as a sum of k unit
fractions (as we will show in Sec-
tion 5), this is a bounded process
which eventually stops with k distinct
unit fractions.
There are some even easier obser-
vations about Egyptian fractions:

a) A fraction m/n which has a
solution of (1) with ﬁxed k
 also has a solution with every
k′ ≥ k.
b) If m/n has a solution of the
form (1) with ﬁxed k, then
m
nt also has such a solution.
When m and k are ﬁxed one
therefore often concentrates
on prime values n.

The most basic question concern-
ing Egyptian fractions is, given some
rational m
n ∈ (0, 1], does (1) always
have a solution (for some k ≥ 1)? The
answer is yes, and in fact a greedy al-
gorithm can be used to construct a
solution: let x1 ≥ 1 be the smallest
positive integer such that 1
x1 ≤ m
n .

It follows that m
n − 1
x1 = m′
n′ < 1
x1
where m′ = mx1 − n < m. While
m′
n′ > 0 we may repeat this process,
and since the numerator decreases at
each stage this must terminate with
a solution to (1). In particular, this
greedy algorithm shows that m
n can
always be written as the sum of at
most m distinct unit fractions.
For example, when applied to 4/17
this algorithm produces the represen-
tation
4
17 = 1
5 + 1
29 + 1
1233 + 1
3039345.

The solution found by the greedy al-
gorithm is not necessarily the sim-
plest one, in either the sizes of the
denominators or the number of sum-
mands. For example, 4/17 may also

1With the exceptions of 2/3 and 3/4. 1

be written as
4
17 = 1
6 + 1
17 + 1
102 .

The greedy approach is one of a
variety of diﬀerent algorithms for pro-
ducing a solution to (1), each with its
own advantages and disadvantages.
For a survey on the rich literature
concerning algorithmic aspects we re-
fer the reader to [18].
In this survey we will consider
more theoretical questions, and focus
on a number of aspects that have re-
ceived considerable interest over the
last decades. We have endeavoured to
give, where possible, some indication
of the ideas and methods used, and
hence have sacriﬁced some breadth
for depth. The topics considered here
do not cover the full range of results
and open problems in this fascinat-
ing area, and the reader is encouraged
to explore further in the surveys of
Erd˝os and Graham [20, 21], the open
problems collection of Guy [22, Sec-
tion D11], and the survey of Schinzel
[37].

2. The Erd˝os-Straus conjecture
The greedy algorithm guarantees that
m
n can always be written as the sum
of at most m distinct unit fractions.
As the example for 4/17 above shows,
however, this is not necessarily opti-
mal, and one can ask, for any fraction
m
n , what is the minimal k such that
(1) has a solution.

2.1. Sums of two unit fractions.
One certainly needs at least two unit
fractions to represent 2
n (when n is
odd), and it is easy to check that one
needs at least three unit fractions to
represent 3
p , where p is a prime such
that p ≡ 1 mod 3.
In general, Stewart [41] has shown
that a reduced fraction m
n is a sum of
two unit fractions if and only if there
are two coprime divisors n1, n2 of n
such that m divides n1 + n2.
In particular, when applied to m =
4, this implies that 4
n is the sum of
two unit fractions for almost all n:
Stewart’s criterion implies that if 4
n is
 not the sum of two unit fractions then
all prime factors of n are 1 mod 4, and
the number of such integers n ≤ N
is asymptotically c N√
log N = o(N ), for
some constant c > 0. In fact, for ev-
ery m a similar but more complicated
analysis shows that the number of in-
tegers n ≤ N such that m
n is not the
sum of two unit fractions is asymptot-
ically cm N (log log N )βm
(log N )αm = O( N√
log N ),
for some constants cm, αm, βm – see
[11] for details.
In particular, once we have ﬁxed
m, asymptotically almost all fractions
with numerator m are the sum of
two unit fractions. The fact that we
have ﬁxed the numerator is vital here:
for any ﬁxed k ≥ 1 the set of ra-
tionals which can be expressed as as
sum of k unit fractions is nowhere
dense [40], except at 0, so the picture
changes considerably when not ﬁxing
the value m.

2.2. Sums of three unit fractions.
When m ≤ 3, the greedy algorithm
produces a solution to (1) with k ≤
3. When m = 4 the greedy algo-
rithm may require four unit fractions,
as we have seen above. It is be-
lieved, however, that for all n ≥ 1
this can be improved, and 4
n can be
written as the sum of three unit frac-
tions. This is perhaps the most noto-
rious open problem concerning Egyp-
tian fractions.

Conjecture 1 (Erd˝os-Straus 1950).
For every n ≥ 2 there exist positive
integers x, y, z such that

(2) 4
n = 1
x + 1
y + 1
z .

This conjecture appeared in a 1950
paper of Erd˝os [19], attributed to
himself and Ernst G. Straus. It is un-
known when the conjecture was orig-
inally made. Another reference is in
a paper of Obl´ath [31], submitted in
1948, who mentions it as a conjecture
of Erd˝os2, and solved it for small inte-
gers. When the second author asked
Erd˝os in 1996 how he came up with
the conjecture the answer was that
this is the ﬁrst interesting case.
 Although m = 4 is the ﬁrst non-
trivial case, it is believed that a simi-
lar phenomenon holds for any m ≥ 4
(excluding ﬁnitely many exceptions).
The analogous conjecture with nu-
merator 5 is due to Sierpi´nski [40],
and the general form was conjectured
by Schinzel (also in [40]).

Conjecture 2 (Schinzel 1956). For
every m ≥ 4 there exists a number
Nm such that, for every n ≥ Nm,
there exist positive integers x, y, z
such that
 m
n = 1
x + 1
y + 1
z .

We note that if (2) is soluble for n
it is trivially also soluble for all mul-
tiples of n. In particular, in exploring
the Erd˝os-Straus conjecture it suﬃces
to concentrate on prime values of n.
The Erd˝os-Straus conjecture has
been computationally veriﬁed up to
1017 [34]. It is possible to prove
the Erd˝os-Straus conjecture for many
congruence classes via elementary
means.
The key observation is that, for
any m ≡ 3 (mod 4), if there are inte-
gers a, c, d such that 4acd−1 = m and
n ≡ −a/c (mod m), then (2) is solv-
able. Indeed, if cn + a = (4acd − 1)b,
then dividing by abcdn shows that

4
n = 1
abd + 1
acdn + 1
bcdn .

This observation allows one to verify
the Erd˝os-Straus conjecture for many
congruence classes immediately. For
example, modulo 47 we could take
(a, c, d) = (1, 6, 2), so that any n ≡
−8 (mod 47) satisﬁes the conjecture,
and in fact we can write 4/47k − 8 as

1
(6k−1)2 + 1
12(47k−8) + 1
(6k−1)12(47k−8) .

We could instead take (a, c, d) =
(1, 2, 6), thereby verifying the con-
jecture for n ≡ −24 (mod 47), or
(a, c, d) = (2, 3, 2), verifying the con-
jecture for n ≡ −32 (mod 47), and
so on. Varying over all 18 ways of
writing 12 = acd we ﬁnd 13 dis-
tinct congruence classes modulo 47

2Some webpages, such as Wikipedia, and a paper by Graham [21] seem to suggest that Obl´ath made this conjecture independently. This
is not the case, as Obl´ath’s paper clearly attributes it to Erd˝os.

for which the Erd˝os-Straus conjec-
ture is true. In general, the num-
ber of such ‘solved’ congruence classes
modulo 4t − 1 essentially depends on
d3(t), the number of ways to write
t as a product of three positive in-
tegers, which on average grows like
≈ (log t)
2.
Using similar reasoning, one
can quickly show that modulo
840 only the congruence classes
1, 49, 121, 169, 289, 361 (all squares!)
are not generally solved (for details
see [28]), and modulo 120120 there is
corresponding work by Terzi [43].
If we take a = c = 1 then the above
shows that modulo all integers of the
shape 4d − 1 the congruence class −1
is soluble. Any simple sieve approach
(such as Brun’s sieve) can then be
used to prove that almost all integers
n ≤ N satisfy the Erd˝os-Straus con-
jecture.
A much more sophisticated ver-
sion by Vaughan [44] combines the
above remark that the number of
soluble congruence classes modulo
primes is described by the divi-
sor function d3 with the large sieve
and proves that there are at most
N exp(−c(log N )
2/3) exceptions n ∈
[1, N ], for some absolute constant c >
0. (To estimate the number of solu-
ble congruence classes correctly, one
needs both the Bombieri-Vinogradov
and the Brun-Titchmarsh theorem,
which guarantee that on average
prime numbers are relatively well dis-
tributed in congruence classes.)
Arguing heuristically, the number
of soluble congruence classes is so
large that all suﬃciently large inte-
gers should be covered by at least
one, giving a compelling heuristic ar-
gument that the Erd˝os-Straus conjec-
ture holds, at least for all suﬃciently
large n. More precisely, one could ar-
gue as follows: since the average value
of d3(m) is ≈ (log m)
2, for any prime
p ≤ N congruent to −1 (mod 4) we
expect to ﬁnd on average ≈ (log p)
2

many congruence classes modulo p
for which the Erd˝os-Straus conjecture
holds. Therefore, assuming indepen-
dence between these classes for dis-
tinct primes, the ‘probability’ that
 any n fails the Erd˝os-Straus conjec-
ture is, using standard prime number
estimates,

≪ ∏

p≤n
p≡−1 (mod 4)
 (
1 − d3((p + 1)/4)
p
 )

≈ e−Ω((log n)2).

(Here we use the Vinogradov nota-
tion f ≪ g to mean f = O(g).)
Since ∑
n≥1 e−c(log n)2 converges, this
probabilistic heuristic suggests there
are at most ﬁnitely many excep-
tions to the Erd˝os-Straus conjecture.
(Indeed, since this converges very
rapidly, and the conjecture has al-
ready been conﬁrmed up to 1017, this
strongly suggests the conjecture holds
for all n.)
Some congruence classes are easier
than others for the Erd˝os-Straus con-
jecture. For example, for n ≡ 3 mod
4 the fraction 4
n can even be repre-
sented by 2 unit fractions, 4
4t+3 =
1
t+1 + 1
(t+1)(4t+3) , and for n ≡ 5 mod 8
it can be represented by three unit
fractions 4
8t+5 = 1
2(t+1) + 1
(t+1)(8t+5) +

1
2(t+1)(8t+5) . It can be shown, how-
ever, that there are some congruence
classes for which there is no such ex-
plicit formula. For example, Schinzel
[38] proved this is the case for all qua-
dratic residue congruence classes. In
particular, there is no such formula
for n = 4t + 1.
Although there are some congru-
ence classes for which we cannot
solve the Erd˝os-Straus conjecture in
such an explicit fashion, there are
some congruence classes (as discussed
above) for which we are able to eas-
ily verify the conjecture. To establish
the conjecture for all primes p (and
hence all integers n) it therefore suf-
ﬁces to show that these ‘good’ con-
gruence classes cover all primes. (For
example, although 61 is of the form
4t + 1, for which we have no general
solution, it is also of the form 7t − 2,
for which we have the general solu-
tion 4
7t−2 = 1
2t + 1
2(7t−2) + 1
t(7t−2) .)
This is a classical observation. It is
less widely known that in fact this
 covering property is equivalent to the
Erd˝os-Straus conjecture.

Theorem 1. The Erd˝os-Straus con-
jecture is equivalent to the statement
that all primes are in at least one of
the following congruence classes:

−a/c (mod 4acd − 1)

for some a, c, d ≥ 1, or

− 4c2d + 1
k (mod 4cd)

for some c, d, k ≥ 1 with k | 4c2d + 1.

(Similar statements can be found
in Nakayama [29], Rosati [33], and
Mordell [28].)

Proof. We ﬁrst show that the cov-
ering statement is suﬃcient for the
Erd˝os-Straus conjecture to hold. The
case p ≡ −a/c (mod 4acd − 1) has
already been discussed above. If k |
4c2d + 1 and p ≡ − 4c2d+1
k (mod 4cd)
then there exists a ≥ 1 such that
p = 4acd− 4c2d+1
k . Therefore kp+1 =
4cd(ak − c) and an elementary re-
arrangement shows that

4
p = 1
ad(ak − c) + 1
acd + 1
(ak − c)cdp .

Thus the Erd˝os-Straus conjecture
holds for all primes p (and hence for
all integers n) if these congruence
classes cover all primes.
We now argue that the cover-
ing statement is necessary. Suppose
then that the Erd˝os-Straus conjecture
holds, let p be some prime, and let
4
p = 1
x + 1
y + 1
z with x ≤ y ≤ z, so
that 4xyz = p(xy + yz + xz). Note
that x < p, and hence p ∤ x. In
fact one can show via an elementary
argument, considering greatest com-
mon divisors, that there must exist
integers a, b, c, d ≥ 1 such that either

(1) x = abd, y = acdp, and z =
bcdp, or
(2) x = abd, y = acd, and z =
bcdp.

In the ﬁrst case we have 4abcdp2 =
p(ap + cp2 + bp) whence 4abcd = a +
b + cp and so p ≡ −a/c (mod 4acd −
1), and in the second case we have
4abcdp = p(a + cp + bp), whence

4abcd = a + (b + c)p. In particular
a divides b + c, say b + c = ak, and so

kp + 1 = 4cd(ak − c) = 4akcd − 4c2d

whence k | 4c2d + 1 and p ≡ − 4c2d+1
k
(mod 4cd). Thus p belongs to at least
one of the required congruence classes
as claimed. □

Recently Bright and Loughran [5]
have studied the Erd˝os-Straus con-
jecture using tools from modern al-
gebraic geometry, in particular show-
ing that there is no Brauer-Manin ob-
struction to the existence of solutions
to (2).

2.3. Counting solutions. For any
existence problem there is a corre-
sponding counting problem. Let f (n)
count how many representations 4
n
has as the sum of three distinct
unit fractions, so that the Erd˝os-
Straus conjecture is the statement
that f (n) > 0 for n ≥ 2 (and is equiv-
alent to the statement that f (p) > 0
for all primes p ≥ 2).
Elsholtz and Tao [17] have shown
that ∑

p≤N f (p) = N (log N )
2+o(1),

where the sum is over the primes
p ∈ [1, N ]. As the number of such
primes is asymptotically N
log N , one
can deduce that, on average, f (p) =
(log p)
3+o(1). Elsholtz and Planitzer
[15] proved that for almost all inte-
gers n ≤ N

f (n) ≥ (log n)
log 6+o(1).

(Note that log 6 ≈ 1.79.) More-
over for inﬁnitely many n the number
of solutions is much larger, namely
f (n) ≥ exp((log 6+o(1) log n
log log n ). This
is larger than one might expect at
ﬁrst sight, and improves upon results
of Elsholtz and Tao [17]. The cru-
cial idea is to study those n consisting
of many small primes, where one can
choose many divisors d of n such that
4
n − 1
d still has very many solutions as
a sum of two unit fractions.
A corresponding bound is also
known even when we restrict to
primes: all reduced congruence
classes e (mod f ) contain primes
 that have many solutions, at least
exp(cf log p
log log p ) for some constant cf >
0. Furthermore, Elsholtz and Tao
[17] established the pointwise upper
bound f (p) ≤ p 3
5 +o(1) for primes.
This was generalized by Elsholtz and
Planitzer [15] to composite denomi-
nators: f (n) ≤ n 3
5 +o(1). It seems
possible that a much better bound of
Oε(nε) holds.

3. Bounding the number of frac-
tions required
As we have already observed, the
greedy algorithm implies that any
m
n ∈ (0, 1) is the sum of at most m
distinct unit fractions, and Schinzel’s
conjecture implies that in fact three
unit fractions suﬃce, assuming n is
suﬃciently large compared to m.
What if m is large compared to n?
The number of fractions required may
grow with n: for example, an Egyp-
tian fraction decomposition of n−1
n re-
quires Ω(log log n) distinct unit frac-
tions. (This follows from the bounds
given in Section 5.) The greedy al-
gorithm shows that n − 1 unit frac-
tions always suﬃce, but much better
bounds are known.
The proofs of all reasonable upper
bounds follow a similar scheme. Sup-
pose we have an increasing sequence
N1 < N2 < · · · of positive integers
such that any 1 < n < Nk is the sum
of at most F (Nk−1) distinct divisors
of Nk, for some increasing function F .
The relevance of such a sequence, as
we will now show, is that it implies
that any m
n ∈ (0, 1) can be written
as the sum of at most 2F (n) distinct
unit fractions.
To see this, given m
n ∈ (0, 1) choose
k such that Nk−1 < n ≤ Nk, and let
ℓ < Nk be such that ℓ
Nk ≤ m
n < ℓ+1
Nk ,
whence 0 ≤ mNk − nℓ < n ≤ Nk.
Writing both mNk − nℓ and ℓ as the
sum of at most F (Nk−1) ≤ F (n) dis-
tinct divisors of Nk and using the
identity

m
n = mNk − nℓ
nNk + ℓ
Nk
 we obtain m
n as the sum of at
most 2F (n) distinct unit fractions as
claimed.
A trivial example of such a se-
quence is to take Nk = 2k, which
allows for F (n) = O(log n) (already
a vast improvement over the O(n)
delivered by the greedy algorithm).
Erd˝os [19] observed that a more ef-
ﬁcient choice is to take Nk to be the
product of the ﬁrst k primes, which
allows for F (n) = O(log n/ log log n)
instead. The best-known construc-
tion to date is due to Vose [46], who
constructed an explicit sequence Nk
with F (n) = O(
√log n), yielding the
following result.

Theorem 2 (Vose [46]). Any frac-
tion m
n ∈ (0, 1) can be written as the
sum of O(
√log n) many distinct unit
fractions.

Erd˝os [19] conjectured that in fact
any m
n ∈ (0, 1) can be written as
the sum of O(log log n) many distinct
unit fractions, which would be the
best possible as the example of n−1
n
shows.

4. Parametric solutions of m
n = 1
x1 +
· · · + 1
xk
Let Em,k(N ) count those n ≤ N such
that m
n is not the sum of k unit frac-
tions. As mentioned in section 2,
Vaughan [44] showed that E4,3(N ) ≤
N exp(−c(log N )
2/3), for some posi-
tive c. This has been generalised by
Elsholtz.

Theorem 3 (Elsholtz [10]). Let m >
k ≥ 3 be positive integers. Then

Em,k(N ) ≤ N exp(−cm,k(log N )
1− 1
2k−1 −1 )

for some absolute constant cm,k > 0.

Note that m = 4 and k = 3 recov-
ers Vaughan’s bound. Viola [45] pre-
viously established a similar bound
with 1
2k−1−1 replaced by 1
k−1 , which
Shen [39] had improved to 1
k .
A key idea in the proof of Theo-
rem 3, and a useful tool in general
for studying Egyptian fractions, is the
realisation that solutions to the equa-
tion m
n = 1
x1 + · · · + 1
xk can naturally
be described by 2k − 1 variables. The

earliest reference containing this idea,
which we are aware of, is Dedekind
[9]. A detailed explanation of the gen-
eral case is in [11], and shorter expla-
nations are in [10, 17, 16].
For concreteness, we will explain
the idea ﬁrst when k = 3, and then
when k = 4. Suppose that m
n = 1
x1 +
1
x2 + 1
x3 . Let t123 = gcd(x1, x2, x3),
t12 = gcd(x1, x2)/t123, and similarly
for t13 and t23. Note that t12, t13, t23
are all coprime in pairs. It is ele-
mentary to check that t12t13t123 di-
vides x1, whence we can write x1 =
t1t12t13t123, and similarly for x2 and
x3. It follows from the deﬁnition
that t1, t2, t3 are also all coprime in
pairs, and also that gcd(t1, t23) =
gcd(t2, t13) = gcd(t3, t12) = 1.
Furthermore, if we write m
n as

1
t1t12t13t123 + 1
t2t12t23t123 + 1
t3t13t23t123
and multiply by common denomina-
tors we obtain

mt1t2t3t12t13t23t123

= n (t1t2t12 + t1t3t13 + t2t3t23)

and hence (assuming that
gcd(m, n) = 1) each ti divides n.
In particular, when n is prime, this
leaves only the possibilities that the
ti are 1 or p. In other words, when
n is prime, one has 7 − 3 = 4 free
parameters.
To further illustrate the idea, we
now examine the case k = 4. Ev-
ery quadruple of four positive integers
(x1, x2, x3, x4) can be written as

x1 = t1t12t13t14t123t124t134t1234
x2 = t2t12t23t24t123t124t234t1234
x3 = t3t13t23t34t123t134t234t1234
x4 = t4t14t24t34t124t134t234t1234,

where

t1234 = gcd(x1, x2, x3, x4),

t123 = gcd(x1, x2, x3)/t1234
(and similarly for other three indices),
t12 = gcd(x1, x2)/(t1234t123t124), and
so on. Crucially, any pair tI , tJ with
I ̸⊆ J and J ̸⊆ I, for example
t123, t124 or t1, t23, must be coprime.
Given a solution to m
n = 1
x1 + 1
x2 + 1
x3 +
1
x4 , multiplying by the common de-
nominator as above, we see that when
 n = p is prime, each ti must be a di-
visor of p. In particular, the family
of solutions is naturally described by
24 − 1 − 4 = 11 free parameters. In
general, with the sum of k unit frac-
tions we have 2k − k − 1 free param-
eters.
We may now attempt a generali-
sation of Vaughan’s argument, ﬁnd-
ing a large collection of congruence
classes that attempt to cover most
n ≤ N . Crucially, the number of
degrees of freedom when constructing
these congruence classes grows expo-
nentially in k, leading ultimately (af-
ter a great deal of technical diﬃculty
and further sieve estimates) to The-
orem 3. (For comparison, Viola [45]
and Shen [39] used k and k + 1 free
parameters respectively, resulting in
their weaker bounds.)
For example, when k = 4, one can
now solve the classes

(mt12t23t24t123t124t234t1234 − 1) r

−mt12t123t124t1234(t12t23t123+t12t24t124).
For comparison, in the case k = 4 Vi-
ola made use of the fact that one can
solve the classes

(mt123t124t1234 − 1) r − (t123 + t124),

and Shen used

(mt123t124t234t1234 − 1) r

−mt123t124t1234(t123 + t124).
When k = 3 the number of soluble
congruence classes was described by
the d3 function; now when k = 4 it
is described by the d7 function. That
is, modulo q ≡ −1 mod m we obtain a
soluble congruence class for each way
of splitting q+1
m into a product of 7
factors.
There is a complication when k >
3 (resulting in the ﬁnal bound of The-
orem 3 containing a 2k−1 − 1 where
one might expect 2k −k−2), since the
soluble congruence classes are now
described by sums of products, rather
than a single product as in Vaughan’s
argument. In particular it is much
more diﬃcult to prove that diﬀerent
congruence classes thus obtained are
actually distinct.
The reader may wonder if such
parametric solutions could be used
 more generally in the study of Dio-
phantine equations. The answer is
yes, in principle, but in practice this
general approach often simpliﬁes to a
much easier one, as one can see with
the Fermat equation x
n + yn = zn.
Here one quickly sees that nothing is
gained, as the variables can be as-
sumed to be coprime.

5. Counting solutions to 1 = 1
x1 +
· · · + 1
xr
We now turn our attention from the
study of (1) for ﬁxed small k and
varying m/n, and consider the oppos-
ing situation in which we ﬁx m/n = 1
and study the solutions to

(3) 1 = 1
x1 + · · · + 1
xk
as k varies. An easy inductive argu-
ment shows that the number of so-
lutions to (3) for ﬁxed k ≥ 1 is ﬁ-
nite. We now present an elementary
argument which gives an explicit up-
per bound as follows (for more details
and slight improvements see [35]).
Fix some solution to (3), ordered
so that x1 ≤ · · · ≤ xk. For 0 ≤ m < k
deﬁne ym ∈ Q by

(4) 1 − ∑

1≤i≤m
 1
xi = 1
ym ,

so that y0 = 1 and yk−1 = xk, and for
1 ≤ m < k − 1 we have ym < xm+1.
By deﬁnition, 1
ym+1 = 1
ym − 1
xm+1 ,
whence ym+1 ≤ ym(ym+1) for all 0 ≤
m < k − 1. In particular, if (ui)i≥1 is
the sequence deﬁned by u1 = 1 and
ui+1 = ui(ui + 1), then ym ≤ um+1
for 0 ≤ m < k. Since the left-hand
side of (4) is at most k/xm+1 we de-
duce that, for all 1 ≤ i ≤ k, we
have xi ≤ kui. The sequence u2
−n
n is
strictly increasing and tends to c0 =
limn→∞ u2
−n
n = 1.26408 · · · , the so-
called Vardi constant, and hence xi ≤
kc2
i
0 . It follows immediately that the
number of solutions to (3) is at most

kk · c2
k−1
0 = c2
k(1+o(1))
0 .

In particular, this grows doubly ex-
ponentially with k. It is surprisingly
diﬃcult to come up with considerably
better upper bounds. Small improve-
ments are possible, by estimating the

number of the ﬁrst k − 2, k − 3 or
k − 4 values of xi trivially as above,
but using non-trivial upper bounds
for the number of ways of writing a
ﬁxed fraction as a sum of 2, 3 or 4
unit fractions, respectively. The best
upper bound currently known is still
doubly exponential in k, and is due
to Elsholtz and Planitzer [16]. They
show (using k−4 and 4 fractions) that
the number of solutions to (3) is at
most
 c2
k( 1
5 +o(1))
0 .

Although the upper bounds are all
doubly exponential in k, it was an
open problem for some time whether
this was the true order of magni-
tude of the number of solutions to
(3). That the number of solutions
is indeed increasing with (essentially)
doubly exponential growth was shown
by Konyagin [25], who proved that
the number of solutions to (3) is at
least
 2c k
log k

for some constant c > 0. We will
now sketch a variant of Konyagin’s
construction, which yields this lower
bound for an increasing sequence of
k, even if we further ask that all de-
nominators are odd. For full details
see [12, 25].
We make crucial use of fractions
of the shape 1
2n−1 with highly com-
posite n. The important feature of
these fractions is that the denomina-
tor 2n − 1 has many divisors, and for
every divisor m | 2n − 1 there is a
decomposition of 1/2n − 1 as

1
2n − 1 + m + 1
2n − 1 + (2n − 1)2/m .

This means that if we can ﬁnd at least
one representation of 1 as the sum of
k − 1 distinct unit fractions, one of
which is 1
2n−1 , then there are at least
d(2n −1)−2k many ways to write 1 as
the sum of k distinct unit fractions.
(Here the −2k is to avoid counting
representations with repeated denom-
inators.) We can write 1/2n − 1 as
both 1
22n − 1 + ( 1
22n + 1
22n(22n −1) + 1
2n +1
 )
 and 1
2n+1 − 1 +

( 1
(2n −1)(2n+1 −1) + 1
2n+1 + 1
2n+1(2n+1 −1)
 )
.
We may use these identities to ﬁnd
a solution to (3) containing 1
2n−1 for
any n with k = O(log n). To do
so one writes the number n in bi-
nary and applies a combination of
the two identities, to increase the
exponent by one, or double it, re-
spectively. For example the number
29 = 16 + 8 + 4 + 1 = 111012 can be
reached from 1 as follows (in binary):
0, 1, 10, 11, 110, 111, 1110, 11100, 11101.
Thus, one can construct a decomposi-
tion of 1 into unit fractions including
1
2n−1 with k = O(log n) fractions.
We have therefore shown the exis-
tence of ≫ d(2n − 1) many solutions
to (3) in k = O(log n) many variables.
If n is the product of the ﬁrst r primes
then r ∼ log n/ log log n ≈ k/ log k
and it can be shown (see [12, Lemma
2.1]) that 2n − 1 has many prime fac-
tors: ω(2n − 1) ≥ 2r − 6. It fol-
lows that d(2n − 1) ≥ 2ω(2
n−1) ≥
22
r−6. Combining these observations

we have found ≥ 2c k
log k many distinct
solutions to (3) with k variables as re-
quired.

6. Solutions to 1 = 1
x1 +· · ·+ 1
xk with
restricted denominators
We now turn our attention from
counting to an existence problem:
what restrictions can we impose on
the denominators in (3) while still be-
ing guaranteed of ﬁnding a solution?

6.1. Restrictions on the sizes of
the denominators. The ﬁrst natu-
ral question is: does there exist a so-
lution to (3) such that the denomina-
tors are all large? Or all small? There
are various ways to make this ques-
tion precise. Henceforth we ﬁx some
k ≥ 1 and order a solution to (3) as
x1 < · · · < xk.
We may ﬁrst ask: how small
can the largest denominator xk be?
Erd˝os observed that since 1 ≥∑0≤j<k 1
xk−j ∼ log( xk
xk−k ), we must
have xk ≥ (1+ 1
e−1 +o(1))k, and asked
whether this was best possible. This
was proved by Martin.
 Theorem 4 (Martin [27]). For any
k ≥ 1 there is a solution to (3) such
that

1 < x1 < · · · < xk ≤ ( e
e−1 +ok→∞(1))k.

We now ask, on the other hand:
how large can the smallest denomina-
tor x1 be? By a similar argument to
the above, we must have x1 ≤ ( 1
e−1 +
o(1))k, and Erd˝os asked whether this
was best possible. This was proved,
at least for inﬁnitely many k, by
Croot. In fact, Croot proves the fol-
lowing stronger result.

Theorem 5 (Croot [7]). For any
N > 1 there exists some k ≥ 1 and
a solution to (3) such that

N < x1 < · · · < xk ≤ (e+oN →∞(1))N.

Notice that since the sum of all re-
ciprocals in (N, (e + o(1))N ) is 1 +
o(1), we must have k = (e − 1 +
o(1))N . It immediately follows that
there are inﬁnitely many k and an ac-
companying solution to (3) with x1 ≥
( 1
e−1 + o(1))k, as required. (Note also
that Croot’s result implies Martin’s
for inﬁnitely many k.) Both Croot’s
and Martin’s results are more general
than we have stated here, concerning
decompositions of arbitrary rationals,
and we refer to [27, 7] for more details.

6.2. Restrictions to arbitrary
sets. Of course, one may impose
many more restrictions on the de-
nominators than simple size bounds.
Finding a solution to (3) is a challenge
even when the restrictions are very
mild: for example, it is a non-trivial
task to manually ﬁnd a representa-
tion of 1 as the sum of distinct unit
fractions with all denominators odd
(and > 1).
There is one trivial obstruction
that prevents a solution to (3) within
small sets: certainly no solution
can exist with denominators in A if∑n∈A 1
n < 1. Thus, for example, the
set of integers in the interval [N, 2N ]
contains no solution to (3), no mat-
ter how large N is. On the other
hand, Theorem 5 shows that, for in-
tervals, this trivial obstruction is the
only one, and that the set of integers

in [N, (e + o(1))N ] must contain a so-
lution for all large N .
If we consider restricting the de-
nominators to some (inﬁnite) arith-
metic progression, there are no longer
any obvious obstructions. Indeed,
we may ﬁnd a solution to (3) within
any inﬁnite arithmetic progression, as
shown by van Albada and van Lint
[1]. Taken together, these positive re-
sults about ﬁnding solutions to (3) in
short intervals and arbitrary congru-
ence classes can be seen as showing
that there are no ‘local’ obstructions
to the existence of a solution to (3).
It is therefore natural to conjec-
ture, as Erd˝os and Graham did in
[20], that the equation (3) enjoys a
Ramsey-type property: whenever the
integers are ﬁnitely coloured, there
exists a monochromatic solution to
(3). This was proved by Croot.

Theorem 6 (Croot [8]). For any
r ≥ 1, if the integers are arbitrar-
ily coloured with r many colours, then
there must be a monochromatic so-
lution to 1 = 1
x1 + · · · + 1
xk with
1 < x1 < · · · < xk.

In fact, Croot proves a strong
quantitative version: there exists a
constant C > 1 such that, for any
r ≥ 1, if the integers in [2, Cr] are
coloured with r many colours then
there must exist a monochromatic so-
lution to (3). This exponential be-
haviour is the best possible, since us-
ing a greedy approach one can r-
colour the integers in [2, e(1+o(1))r)
so that the sum of all reciprocals in
each colour class will be less than
one, and hence certainly there can
be no solution to (3). It is an inter-
esting and open problem to improve
the value of Croot’s constant C. (In
[8] Croot shows that C = e167000 is
suﬃcient for large r.) For r = 2
colours a Ph.D. thesis by Andreas
Hipler [23] proves that the interval
[2, 208] has this property, and that
208 is sharp. The proof involved non-
trivial computer calculations, as one
has to study many distinct colourings
 of certain crucial integers in this in-
terval. If we colour the integers in r
many colours then at least one colour
class has upper density3 ≥ 1/r. The
following result, which was also con-
jectured by Erd˝os and Graham (for
example in [21]), is therefore a natu-
ral strengthening of Croot’s colouring
result.

Theorem 7 (Bloom 2021+ [4]4).
Any subset of the integers with posi-
tive upper density contains a solution
to 1 = 1
x1 + · · · + 1
xk with 1 < x1 <
· · · < xk.

The proof of Theorem 7 extends
the method used by Croot to prove
Theorem 6: a variant of the Hardy-
Littlewood circle method, combined
with an ingenious elementary com-
binatorial argument. Croot actually
proves a density result for suﬃciently
‘smooth’ integers: in particular, that
any positive density set of integers
A, satisfying the additional constraint
that all prime factors of n ∈ A are
≤ n 1
4 −o(1), contains a solution to (3).
This immediately implies Theorem 6,
since any r-colouring of all integers
must also r-colour all such smooth in-
tegers.
This is not suﬃcient for an unre-
stricted density result since, for ex-
ample, the set of all n with a prime
divisor > n1/2 has positive density.
The chief novelty of [4] is that it
improves the technical strength of
Croot’s argument so that the smooth-
ness threshold of 1
4 − o(1) is raised to
1 − o(1). This suﬃces to prove an un-
restricted density result, since almost
all integers n have no prime factors
> n1−o(1).

6.3. A sketch of Croot’s method.
We now present a sketch of Croot’s
method and the proofs of Theorems 6
and 7. The actual proofs are quite
technical, and the interested reader is
referred to [8] and [4] for full details.
Suppose we are given some ﬁnite
set of integers A such that
(1) A ⊆ [N, O(N )],
 (2) A is ‘N θ-smooth’, in the
sense that all prime factors of
n ∈ A satisfy p ≤ N θ, and
(3) |A| ≫ N .

Our goal is to ﬁnd some S ⊆ A
such that ∑
n∈S 1
n = 1. We begin
by noting that, combining properties
(1) and (3) (with appropriate choices
of constants), we may assume that∑n∈A 1
n ∈ (2 − o(1), 2) (after possi-
bly discarding some elements of A).
Since we then have ∑n∈S 1
n < 2 for
all S ⊆ A, it suﬃces to ﬁnd some
non-empty S ⊆ A with ∑n∈S 1
n ∈ Z.
This trivial recasting has the advan-
tage that it naturally leads to the
possibility of using exponential sums.
In fact, if we let P = lcm(A), then
a simple exercise using orthogonality
shows that the number of S ⊆ A with∑
n∈S 1
n ∈ Z is exactly equal to

(5) 1
P
 ∑

− P
2 <r≤ P
2
 ∏

n∈A(1 + e(r/n)),

where e(x) = e2πix. It suﬃces there-
fore to prove that (5) is ≥ 2.
The r = 0 summand contributes
exactly 2|A|/P , and elementary num-
ber theory shows that the N θ-
smoothness assumption implies P =
eO(N θ ), which is 2o(|A|) provided θ ≤
1 − o(1). This ‘main term’ there-
fore contributes 2(1−o(1))|A|, which is
much larger than we require. The
contribution from other small r, those
with 0 < |r| ≤ N/4, say, is
harder to calculate exactly, but an
elementary calculation shows that
the sign of ℜ ∏
n∈A(1 + e(r/n)) is
cos(πr ∑
n∈A 1
n ) ∏
n∈A cos(πr/n). In
particular, since ∑n∈A 1
n ∈ (2 −
o(1), 2), the contribution to (5) from
all r with 0 < |r| ≤ N/4 is non-
negative, and hence can be discarded
in our quest for a lower bound.
In particular, to show that (5) is
≥ 2 as required, it suﬃces to show
that whenever N/4 < |r| ≤ P/2, we
have

(6)
 ∣
∣
∣
∣
∣
 ∏

n∈A
(1 + e(r/n))

∣
∣
∣
∣
∣ = o(2|A|/P ).

3We recall that the upper density of A ⊂ N is deﬁned as lim supN→∞ |A∩[1,N]|
N .
4The proof of Theorem 7 has now been formally computer-veriﬁed, using the Lean proof assisant, by Bloom and Mehta. The formal
version of the proof can be accessed at https://github.com/b-mehta/unit-fractions.

If r ̸∈ [−N/8, N/8] (mod n), then,
writing rn ∈ [−n/2, n/2] for the in-
teger such that r ≡ rn (mod n), we
have e(r/n) = e(rn/n) = e(ξ) for
some ξ ∈ (c, 1/2) (with c > 0 some
absolute constant), and hence |1 +
e(r/n)| ≤ 2/c′ for some other abso-
lute constant c′ > 1. Since P ≤
eO(N θ), to prove (6) it therefore suf-
ﬁces to ﬁnd ≫ N θ many n ∈ A such
that r ̸∈ [−N/8, N/8] (mod n).
We may equivalently phrase this
as saying that, if I is the interval of
width N/4 centred at r, then there
are ≫ N θ many n ∈ A that do not
divide any x ∈ I.
At this point we have left any men-
tion of exponential sums (and indeed
of unit fractions) far behind: Croot’s
method transforms the problem into
a purely combinatorial question con-
cerning the interaction between inter-
vals and multiples of elements in A.
Finding a satisfactory answer to this
question is a subtle and diﬃcult af-
fair, however. The overall idea is that
if there is some interval I which fails
the requisite property, then one can
construct an integer x ∈ I with ‘too
many’ divisors.
To explain this combinatorial pro-
cedure, we introduce a new ‘measure’
of sets of integers (depending on the
ﬁxed set A),

µ(X) = 1
log log N
 ∑

p∈PA∩X
 1
p ,

where Pn is the set of primes divid-
ing n, and PX = ∪n∈X Pn. It is also
convenient to introduce the notation
Aq = {n ∈ A : q | n}, for any integer
q ≥ 1. The three crucial facts about
this measure µ are that

(1) for any X, µ(X) ≤ 1 + o(1),
(2) for any x and q, if

|{n ∈ Aq : n | x}| ≥ (N/q)(log N )
−o(1),

then µ(Px) ≥ e−1 − o(1), and
(3) if 0 < |x1 − x2| ≪ N then

µ(Px1 ∪Px2) = µ(Px1)+µ(Px2)+o(1).

Suppose now that there exists
some interval I of width N/4 such
that all but o(N θ) many n ∈ A di-
vide some x(n) ∈ I. We will argue
 that there must exist some x ∈ I di-
visible by all primes in PA, and hence
divisible by P = lcm(A), which is
an immediate contradiction if, as in
our application, I is an interval of
width N/4 centred at some r with
N/4 < |r| ≤ P/2.
Let p ∈ PA, and consider Ap
– heuristically, we expect |Ap| ≈
|A|/p ≫ N/p, which we will assume
henceforth. In particular, provided
N/p ≫ N θ, for almost all n ∈ Ap
there exists some x(n) ∈ I divisi-
ble by n. In fact, after some divisor
sleight of hand, one can ensure that
there is some xp ∈ I which equals
x(n) for ≫ |Ap|(log N )
−o(1) many
n ∈ Ap. Therefore, by property (2) of
µ above, we have µ(Pxp) ≥ e−1−o(1).
Therefore all p ∈ PA have an as-
sociated xp ∈ I such that Pxp has
µ-weight at least e−1 > 1/3. Com-
bining properties (1) and (3) of µ it
follows that there cannot be three dis-
tinct such xp ∈ I. If all xp are in fact
identical, then we have found some
x ∈ I divisible by all p ∈ P, and
hence by P as required (we are assum-
ing for simplicity that P is squarefree
here). The only remaining possibility
is that all xp are one of two distinct
x, y ∈ I. In this case, we may ﬁnd
some large subset A
′ ⊆ A, such that
all n ∈ A
′ divide one of either x or
y, and we perform a similar iteration
with A
′ replacing A.
The above analysis succeeds pro-
vided N/p ≫ N θ for all primes p ∈
PA. Since the N θ-smooth hypothe-
sis implies p ≤ N θ, this in turn is
guaranteed provided θ < 1/2, and
hence we have proved (6). Therefore,
assuming a smoothness threshold of
N 1/2−o(1), we have found some S ⊆ A
with ∑n∈S 1
n = 1, and obtain Croot’s
smooth density result. (Croot works
with θ < 1/4 rather than < 1/2 to
ease some of the many technical diﬃ-
culties we have ignored in this sketch,
but in principle his method works up
to any θ < 1/2.)
To prove an unrestricted density
result such as Theorem 7, we need
to raise this smoothness threshold to
θ = 1 − o(1). The key idea of [4]
 is to give up on the strong pointwise
bound (6), and instead only aim to
prove an averaged version, which suf-
ﬁces for our purposes. We note that
in fact the above combinatorial argu-
ment shows that, for any interval I of
width O(N ), there exists some x ∈ I
divisible by every p ∈ PA with the
property that all but o(N/p) many
n ∈ Ap divide some x ∈ I. If there
are many such p, then the ensuing
bound on |∏n∈A(1 + e(r/n))| is quite
weak (particularly when some of the
primes can be as large as N 1−o(1)),
but on the other hand, there are not
many possible values of r for which
this can occur, since such r must
be O(N )-close to a ﬁxed multiple of
many primes simultaneously. On the
other hand, if there are few such p,
then we cannot restrict r, but can re-
cover a pointwise bound comparable
to (6) in strength. Trading oﬀ the
two gains, we are able to establish a
version of (6) that holds on average,
which is suﬃcient.

7. Applications
We conclude by mentioning some
intriguing applications of Egyptian
fractions to other areas of pure math-
ematics.

7.1. Finite group theory. One
simple yet surprising application is
within ﬁnite group theory. It is nat-
ural to ask what limits the number
of conjugacy classes imposes on the
underlying group. By considering
Egyptian fractions, Landau showed
that there are only ﬁnitely many
possibilities.

Theorem 8 (Landau [26]). For any
k ≥ 1 there are only ﬁnitely many ﬁ-
nite groups with exactly k conjugacy
classes.

This is an elementary consequence
of the bounds of Section 5 on the
size of the denominators of solutions
to (3). It suﬃces to show that, if
G has exactly k conjugacy classes,
then |G| ≪k 1. Suppose that G has
conjugacy classes of sizes m1, . . . , mk.
Since these partition G, it follows that
|G| = m1 + · · · + mk. On the other

hand, each mi is a divisor of |G|, and
hence, dividing by |G|, we have

1 = 1
|G|/m1 + · · · + 1
|G|/mk .

It follows that, by the upper bound
proved in Section 5, we haveG|/mi ≤ kc2
k
0 for all 1 ≤ i ≤ k. Fur-
thermore, since the identity is only
conjugate to itself, for some i we have
mi = 1. It follows that |G| ≤ kc2
k
0
as required. (Note that this explicit
bound implies, for example, that any
ﬁnite group G has ≫ log log|G| many
distinct conjugacy classes.)
Landau’s lower bound estimate has
been strengthened and extended in a
number of ways; see, for example, [3]
for extensions and references.

7.2. Polytopes. A more recent con-
nection is to discrete geometry. Re-
call that a polytope in Rd is the con-
vex hull of some ﬁnite set of points in
Z
d. We say that P is
• integer-free if there are no
points in Z
d in the interior of
P ,
• weakly maximal if it is
integer-free and there is no
integer-free polytope that
strictly contains P , and
• strongly maximal if it is
integer-free and there is no
integer-free, closed, convex,
d-dimensional, set of any sort
that strictly contains P .
 It is not obvious whether there
can exist integer-free polytopes that
are weakly maximal yet not strongly
maximal. Indeed, there do not exist
such polytopes in dimensions ≤ 3. It
was shown in [30] that there do exist
such polytopes in all dimensions ≥ 4.
Recently, Averkov has shown that in
fact there must exist many such poly-
topes, by establishing a close link be-
tween counting polytopes which are
weakly, not strongly, maximal, and
Egyptian fraction decompositions of
(3).

Theorem 9 (Averkov [2]). Let d ≥
6. Up to aﬃne equivalence, the num-
ber of weakly maximal integer-free
polytopes in Rd that are not strongly
maximal is at least the number of so-
lutions to (3) with k = d−5 variables.

In particular, using Konyagin’s
lower bound, we deduce that there are
at least 2cd/ log d many weakly maxi-
mal polytopes that are not strongly
maximal (for some constant c > 0).

7.3. Huﬀman codes. The study of
solutions to (3) when the denomina-
tors xi are (not necessarily distinct)
powers of a ﬁxed integer t has a close
connection to coding theory. For our
purposes, a k-code in an alphabet of
size t is simply a set of k distinct
{0, . . . , t − 1}-strings. For many prac-
tical applications, it is preferred that
the code be preﬁx-free, that is, no
 string appears as an initial segment
of any other (in particular this allows
for instant decoding). The Kraft-
McMillan inequality states that if a
preﬁx-free k-code has string lengths
l1, . . . , lk then ∑ 1

tli ≤ 1.
Preﬁx-free codes with the aver-
age word length as small as possi-
ble, also known as compact Huﬀman
codes, therefore have string lengths
that satisfy ∑ 1
tli = 1. In fact,
given any solution to this equation,
a corresponding compact Huﬀman
code can be produced. For exam-
ple, there are three essentially dis-
tinct ways (with the word lengths
li ordered by size) of writing 1 as a
sum of ﬁve reciprocal powers of 2:
1 = 1
2 + 1
4 + 1
8 + 1
16 + 1
16 = 1
2 + 1
8 +
1
8 + 1
8 + 1
8 = 1
4 + 1
4 + 1
4 + 1
8 + 1
8 . These
correspond to the compact Huﬀ-
man codes {0, 10, 110, 1110, 1111},
{0, 100, 101, 110, 111}, and
{00, 01, 10, 110, 111}. This corre-
spondence shows that the number
of compact Huﬀman codes is (up to
equivalence) the number of solutions
to ∑ 1
tli = 1. This is also equivalent
to counting other natural combina-
torial objects, such as the number of
nonequivalent canonical rooted trees,
or the number of bounded degree se-
quences. For more information we
refer to [14, 13].

References
[1] P. J. van Albada and J. H. van Lint,
Reciprocal bases for the integers, Amer.
Math. Monthly, 70 (1963), 170–174.
[2] G. Averkov, Diﬀerence Between Fam-
ilies of Weakly and Strongly Max-
imal Integral Lattice-Free Polytopes,
in Interactions with Lattice Polytopes
(Springer, ILP 2017) Vol. 386., pages
1–10
[3] A. Beltr´an, M. J. Felipe, and C. Mel-
chor, Landau’s theorem on conjugacy
classes for normal subgroups, Interna-
tional Journal of Algebra and Compu-
tation 26 (2016), 1453-1466.
[4] T. F. Bloom, On a density conjecture
about unit fractions, arXiv:2112.03726
(2021).
[5] M. Bright and D. Loughran, Brauer-
Manin obstruction for Erd˝os-Straus
 surfaces. Bull. Lond. Math. Soc. 52
(2020), no. 4, 746–761.
[6] T. D. Browning and C. Elsholtz. The
number of representations of rationals
as a sum of unit fractions. Illinois J.
Math. 55 (2011), no. 2, 685–696.
[7] E. S. Croot, On unit fractions with
denominators in short intervals, Acta
Arith. 99 (2001), no. 2, 99–114.
[8] E. S. Croot, On a coloring conjecture
about unit fractions. Ann. of Math. (2)
157 (2003), 545-556.
[9] R. Dedekind. Gesammelte mathema-
tische Werke, Band 2, Hrsg. v.
Robert Fricke, Emmy Noether u.
Oeystein Ore., ¨Uber Zerlegungen von
Zahlen durch ihren gr¨oßten gemein-
samen Teiler, (Festschrift der Uni-
versit¨at Braunschweig, 1897). Braun-
schweig: Friedr. Vieweg & Sohn A.-G.,
1931.
 [10] C. Elsholtz, Sums of k unit fractions,
Trans. Amer. Math. Soc. 353 (2001),
3209-3227.
[11] C. Elsholtz, Sums of k unit frac-
tions, Ph.D. Thesis (Darmstadt), 1998.
Shaker Verlag, Aachen.
[12] C. Elsholtz, Egyptian fractions with
odd denominators, Q. J. Math. 67
(2016), no. 3, 425-430.
[13] C. Elsholtz, C. Heuberger, and
D. Krenn, Algorithmic counting of
nonequivalent compact Huﬀman codes,
https://arxiv.org/abs/1901.11343.
[14] C. Elsholtz, C. Heuberger, and H.
Prodinger. The number of Huﬀman
codes, compact trees, and sums of unit
fractions. IEEE Trans. Inform. Theory
59 (2013), no. 2, 1065–1075.
[15] C. Elsholtz and S. Planitzer, The num-
ber of solutions of the Erd˝os-Straus
Equation and sums of k unit fractions,

Proc. R. Soc. Edinb. A: Math. 150(3)
(2020), 1401-1427.
[16] C. Elsholtz and S. Planitzer, Sums
of four and more unit fractions and
approximate parametrizations, Bull.
Lond. Math. Soc. 53 (3), 2021, 695-709.
[17] C. Elsholtz and T. Tao. Counting the
number of solutions to the Erd˝os-Straus
equation on unit fractions, J. Aust.
Math. Soc. 94 (2013), no. 1, 50-105.
[18] D. Eppstein, Ten algorithms for Egyp-
tian fractions, Mathematica in Educa-
tion and Research 4(2) (1995), 5-15.
[19] P. Erd˝os, Az 1/x1 + 1/x2 + . . . +
1/xn = a/b egyenlet eg´esz sz´am´u
megold´asair´ol, Mat. Lapok 1 (1950),
192-210.
[20] P. Erd˝os and R. L. Graham, Old and
new problems and results in combi-
natorial number theory, Monographies
de L’Enseignement Math´ematique, 28.
Universit´e de Gen`eve, Geneva, 1980.
[21] R.L. Graham, Paul Erd˝os and Egyp-
tian fractions, in Erd¨os centennial, 289-
309, Bolyai Soc. Math. Stud., 25, J´anos
Bolyai Math. Soc., Budapest, 2013.
[22] R. K. Guy, Unsolved Problems in Num-
ber Theory, Springer, Third Edition,
2004.
[23] Andreas Hipler, Zu Modulspannweiten
und zu einem Problem von Erd˝os und
Graham, Ph.D. Thesis, 2002, Univer-
sity of Mainz.
[24] O. T. Izhboldin and L. D. Kurlyand-
chik, Unit fractions, Proc. St. Peters-
burg Math. Soc., 111 (1995) 193-200.
 [25] S. V. Konyagin, Double Exponential
Lower Bound for the Number of Repre-
sentations of Unity by Egyptian Frac-
tions, Math. Notes 95 (2014), no. 1-2,
277-281.
[26] E. Landau, ¨Uber die Klassenzahl der
bin¨aren quadratischen Formen von neg-
ativer Diskriminante, Math. Ann. 56
(1903), 671-676.
[27] G. Martin, Denser Egyptian fractions,
Acta Arith. 95 (2000), no. 3, 231–260.
[28] L. J. Mordell, Diophantine Equations,
volume 30 of Pure and Applied Mathe-
matics. Academic Press, 1969.
[29] M. Nakayama, On the Decompo-
sition of a Rational Number into
“Stammbr¨uche”, Tohuko J. Math. 46
(1939), 1-21.
[30] B. Nill and G. M. Ziegler, Projecting
lattice polytopes without interior lat-
tice points, Math. Oper. Res. 36 (2011),
no. 3, 462–467.
[31] M.R. Obl´ath, Sur l’ ´equation diophanti-
enne 4/n = 1/x1 + 1/x2 + 1/x3, Math-
esis 59 (1950), 308-316.
[32] The Papyrus Rhind, approximately
1650–1550 BCE, written by the scribe
by Ahmes.
[33] L. A. Rosati, Sull’equazione diofantea
4
n = 1
x1 + 1
x2 + 1
x3 , Bollettino della
Unione Matematica Italiana (3), 9: 59-
64 (1954).
[34] S. Salez, The Erd˝os-Straus conjecture:
New modular equations and checking
up to N = 1017, arXiv:1406.6307.
[35] C. S´andor, On the number of so-
lutions of the Diophantine equation∑n
i=1 1
xi = 1, Period. Math. Hungar.
47 (2003), no. 1-2, 215-219.
 [36] A. Schinzel, Sur quelques propri´et´es des
nombres 3/n et 4/n, o`u n est un nombre
impair. Mathesis 65 (1956), 219-222.
[37] A. Schinzel, Erd˝os’s work on ﬁnite sums
of unit fractions, in Paul Erd˝os and his
mathematics, I (Budapest, 1999), 629-
636, Bolyai Soc. Math. Stud., 11, J´anos
Bolyai Math. Soc., Budapest, 2002.
[38] A. Schinzel, On sums of three unit
fractions with polynomial denomina-
tors. Funct. Approx. Comment. Math.
28 (2000), 187-194.
[39] Z. Shen, On the Diophantine equation
∑k
i=0 1/xi = a/n, Chinese Ann. Math.
Ser. B 7 (1986), 2, 213-220.
[40] W. Sierpi´nski, Sur les d´ecompositions
de nombres rationnels en fractions pri-
maires, Mathesis 65 (1956), 16-32.
[41] B. M. Stewart, Theory of numbers,
(second edition). The Macmillan Com-
pany, New York; Collier Macmillan
Ltd., London 1964.
[42] T. Takenouchi, On an indetermi-
nate equation, Proc. Phys.-Math. Soc.
Japan (3), 3 (1921) 78-92.
[43] D.G. Terzi, On a conjecture by Erd˝os-
Straus, Nordisk Tidskr. Informations-
Behandling (BIT) 11 (1971), 212-216.
[44] R. Vaughan, On a problem of Erd˝os,
Straus and Schinzel, Mathematika 17
(1970), 193-198.
[45] C. Viola, On the diophantine equations
Πk
0 xi−∑k
0 xi = n and ∑k
0 1/xi = a/n,
Acta Arith. 22 (1972/73) 339-352.
[46] M. D. Vose, Egyptian fractions, Bull.
London Math. Soc. 17 (1985), no. 1,
21–24.
