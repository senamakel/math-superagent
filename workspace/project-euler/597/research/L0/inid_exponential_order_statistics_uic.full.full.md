<!-- source: http://homepages.math.uic.edu/~wangjing/stat416/orderstat-exp1.pdf | converted from PDF -->

11

Order Statistics from Independent
Exponential Random Variables and
the Sum of the Top Order Statistics

H. N. Nagaraja

The Ohio State University^ Columbus^ OH, USA

Abstract: Let X(i) < • • • < X(^) be the order statistics from n indepen-
dent nonidentically distributed exponential random variables. We investigate
the dependence structure of these order statistics, and provide a distributional
identity that facilitates their simulation and the study of their moment proper-
ties. Next, we consider the partial sum Ti — Yl^=i^i ^{j)'> 0 < i < n — 1. We
obtain an explicit expression for the cdf of T^, exploiting the memoryless prop-
erty of the exponential distribution. We do this for the identically distributed
case as well, and compare the properties of Ti under the two settings.

Keywords and phrases: Markov property, equal in distribution, simulation,
mixtures, selection differential

11,1 Introduction

Let Xi,. . .,Xn be independent nonidentically distributed (inid) random vari-
ables (rvs), where Xj is Exp(Aj), j — 1,... , n; that is, the pdf of Xj is given
by  /,•(x) = A,•e-^^^ x>0 ,

and the \j are possibly distinct. Let X(i) < • • • < X(^) be the order statis-
tics from this sample. We investigate their dependence structure and provide
a distributional identity that facilitates their simulation and investigation of
distributional and moment properties. This is done in Section 11.2.
The work in Section 11.3 is motivated by a personal communication from

173

174 H. N. Nagaraja

Dr. Yang-Seok Choi who was interested in the distribution of

n
Ti= Yl ^0) ' 0 < z < n - 1. (11.1)

There we obtain an expHcit expression for the cdf of T^. We also consider the
independent identically distributed (iid) case and relate Ti to a rv known as
selection differential in the genetics literature. We then compare the properties
of To under the iid and inid models.

11.2 Distributional Representations and
Basic Applications

We begin with a discussion of the stochastic structure of and distributional
representations for the vector of order statistics (^(i), • • •, ^(n))- When the Aj
are identical and equal to, say A, it is known that (see, e.g., David and Nagaraja,
2003, p. 18)

{X^i)J = h,^.^n)^ll^^ (11.2)

where the Zj are iid standard exponential (i.e., Exp(l)) rvs. This is known as
Renyi's representation [Renyi (1953)].
Let X = (-^(1)5 • • • 5 X{n)y aiid Z = (Zi,... , ZnY, and define a vector cxi =

(ai,. . .,a^,0,. . .,0)' where aj = l/{\{n — j + 1)}, I < i,j < n. Then, X(^) =
a/ Z and (11.2) can be expressed as

X = CZ, (11.3)

where C is the n x n matrix of constants whose ith row is a/. This relation is
helpful in simulating all or a subset of order statistics from a random sample of
size n from an Exp(A) parent.
When the Xj are not identical, representations for the exponential order
statistics do exist. Nevzorov (1984) shows that [see also Nevzorova and Nev-
zorov (1999)] the joint distribution of order statistics can be expressed as a
mixture distribution with n! components where the various component vectors
are chosen with probability pi of picking certain permutation of the Aj for or-
dering the observed rvs. To be precise, Nevzorov shows that the cdf of -^(i),
the ith component of X, can be expressed as a mixture cdf given by

n\
F(i){x) = Y.piFi{x), (11.4)

1=1

Exponential Order Statistics 175

where  _ ^1 ' ' ' ^n /-. 1 r\

{^d{l) H \- ^d{n)){^d{2) H \- ^d{n)) ' ' '^d{n)

and Fi is the cdf of the rv
 + '" + 7T ^ r, 1 < ^ < ^,
{^d{l) H ^ ^d{n)) {^d{i) H \- ^d(n)) '

and the mixture includes all n\ vectors corresponding to the n! permutations
(d(l),d(2),.. .,d(n)) of integers 1,2,.. .,n.
Tikhov (1991) gave another, simpler, form of the above representation by
introducing antiranks D(l),... , J9(n) defined by

{D{i) = m} = {X(i) = Xm}, 1 < i, m < n. (11.6)

With these random subscripts, one can write the distributional equality

d Zi Zj^
^ W = 7^ , , X ^ + ---+7 ^ . \ , v^l<^<^ ^ (11-7)

where the Zj are iid standard exponentials and are independent of the antirank
vector (£)(1),.. .,D(n)). The form in (11.3) also holds in this case, with a
modification that lets the elements of C to be rvs. Let us define a random
vector 8Li = (Ai,... , A^, 0,... , 0)', 1 < i < n, where

^j = i^DU) + • • • + AD(n))"\ 1 < i < n. (11.8)

Then the following distributional equality holds:

X-AZ, (11.9)

where A is an n x n random matrix whose zth row is a^'. The elements of A
are independent of the vector Z whose components themselves are iid standard
exponential rvs. The elements of A are functions of Ai,... , A^ that are de-
pendent and depend on the distribution of (Z)(l),..., D(n)), given by the pi in
(11.5).

11.2.1 Remark s

1. The joint distribution of {D{1),..., D(n)), given in (11.5), can be used
to simulate this vector. We now describe how it can be done easily and more
efficiently in a sequential manner. We start with D{1)] it is a discrete rv with
support no = {l,2,...,n } and P{D{1) = i) = Xi/ii^jeQo^j'l' ^^^^ ^(1) ^^

176 H. N. Nagaraja

selected from this distribution, D{2) is chosen from fii = {1,2,... , n} - {D{1)}
using the probabiUty distribution given by P{D{2) = i) = K/(^J^Q^ AJ). In
general, for 1 < fc < n — 1, after D{1),..., D{k) are chosen, D{k + 1) is chosen
from
 nk = {l,2,...,n}-{D{l),D{2),...,D{k)}

using the probabilities

P{D{k + l) = i)=.\J I > ^ AH , i G Ofc, 1 < A: < n - 1.

2. The representation in (11.9) can be used to simulate exponential order
statistics or functions of these order statistics. If the quantity of interest is a
function of the first i order statistics, one need to simulate only i^(l),... , D{i)
and these choices will determine the sum X]^=i+i ^D{k) ^^at is needed to eval-
uate the observed values of Aj,j < i. Also, we need to simulate only Z^, 1 <
k<i.

3. The representation for the cdf of X(^i) given in (11.4) and the distri-
butional identity for the rv X(^) given in (11.7) have different purposes and
applications. The former can be used to determine probabilities associated
with X(^) assuming that the explicit form for Fi is available, whereas the latter
gives a handy framework for simulation. There is a distinction between (11.4)

and an equality in distribution (=) relation obtained by replacing the cdfs with
the associated rvs in that equation. Tikhov's (1991, p. 630) interpretation of
Nevzorov's result makes this improper leap.

11.2.2 Applications

Moments

We can use the distributional equality in (11.7) to obtain expressions for the
moments of order statistics. Because
 i

Aj and Zj are independent, and the Zj are iid standard exponential, it follows
that

Exponential Order Statistics 177

and
 Far(X(,)) =  E{Xf^) - {E{X^,^)}' = ^  E{A]) + VariJ2 Aj ] ,

upon simplification. Further, for 1 <  i <  A; <  n,

i k

i / i ^  \

j=l \j= l l=i+l J

In the iid case, the A/s are all constants and Aj = l/{A(n — j +  1)}, and
the classical results follow immediately.

Spacings of order statistics

The relation in (11.7) can also be used to study the distributional representa-
tions for spacings. For example,

X(i) - X(i_i) = AiZi, 2<i<n,

and hence for 2 <  i <  n — 1,

Cot'(X(i) - X(i-i), X(i+i) - X(i)) =  Cov{AiZi, Ai+iZi-^i) = Cov{Ai, Ai^i).

In the iid case, it is wellknown that the spacings are independent and thus
are uncorrelated. It appears that the covariance is zero if and only if the A^ are
identical. Such a conjecture is also made in Khaledi and Kochar (2000) and a
proof is given of the claim for n =  3. (They actually prove a stronger result.)
The case where n >  3 appears to be open.

Other linear functions

For a vector (3 =  (/3i,.. -.(inY, one can simulate /3'X values as (3'AZ using
(11.9). For example, the Ti in (11.1) can be simulated as the sum

i n
Ti = {n-i)Y^ AjZj + Y,{n-j + l)AjZj. (11.11)

3=1 j=i+ l

178 H. N. Nagaraja

In the iid case, Ti is related to the selection differential^ given by

^^ = 1(1 E ^o)-H' (11-12)
y j=n-k+l j

where // and a are the mean and standard deviation of the parent population.
For the Exp(A) parent, both these moments are 1/A. The rv Djt is used to
measure the improvement due to selection where the top values in the sample
are selected and for small A: (= n — z), it provides a good test for checking for
outliers at the upper end of the sample.
Another linear function is the total time on test given by

and serves as the best estimator of 1/A based on type II right censored sample
in the iid case.

11.3 Sum of the Top Order Statistics

The following classical result (see, e.g., David and Nagaraja, 2003, pp. 137-138)
is helpful in our pursuit of the cdf of the sum Ti.

Lemma 11.3.1. Suppose Zrj r = 1,... , m, are independent standard exponen-
tial random variables and Cr 's are distinct positive numbers. Then

where
 ^r=i ^ ^^ / / r=i

and the probability is 1 if z < 0.

Now recall the representation (11.11) for Ti where the joint distribution of
the Aj is as described in Section 11.2 and the Zj are iid standard exponential
rvs.

Exponential Order Statistics 179

11.3.1 The IID case

When the Xi are identically distributed each being standard exponential, say,
Aj would be a  constant 1/cj where Cj = n — j + 1. In that case,

Ti = {n-i)J2(-]Zj + ^h  0<i<n-l , (11.13)

where Wi is the sum of (n—i) standard exponential rvs, and is a gamma(n —z, 1)
rv with pdf
 [n- I - 1)!

Thus, To is a  gamma(n, 1) rv. Also, because T^-i =  -^(n)?

P{Tn-i >t) = l-{l - e-*)^, t > 0.

For 0 <  i <  n  — 1, one can use Lemma 11.3.1 and conditioning argument
in the representation (11.13) to obtain an explicit expression for the survival
function of Ti as follows:

P{Ti>t) =  pl(n-i)Y,-Zj+Yi>t

• 1 ^j

rt / ^

* 1 /• *

j-= i yn  — i — ij ! JQ

n—i—1 jj .

A;!
fc=0

Here, Cj = n — j + 1,
 Cj+ i n - z

The Wj are obtained using Lemma 11.3.1, and have alternating signs. They are
given by
 _-p|-n-fc + l _ 1 n! (-1)^-^'
""'" H ^'- ^ ~n-j + i{n-i)\{j-1)1(1-jy:

180 K  N. Nagaraja

The pdf of Ti can be obtained by differentiating (11.14). Upon some simplifi-
cation the pdf can be expressed as

~( Q-fi I Q+i J [n-i-iy. Jo

or as
 frM - „(::;)i:(;:;)(-')--{-=^i^'}

(n ^r-^(^^») »""*"'*•

Nagaraja (1981) has obtained a similar expression for the pdf of Ti/{n — i) in his
study of the selection differential Dk in (11.12) arising from a random sample
from an exponential distribution. Prom Nagaraja (1982), one can obtain the
asymptotic distribution of Ti — {n — i) log(n) if n approaches infinity such that
fe = n  — i is held fixed. Becasue the exponential distribution is in the domain
of attraction of the Gumbel distribution, the cdf oiTi — k log(n) converges to
the following cdf for fc  > 2:

Andrews (1996) has studied the finite-sample moment and distributional
properties of the selection differential Dk for the exponential and uniform par-
ents. Prom his work, one can obtain explicit expressions for the first four mo-
ments of Ti =  {n — i){fi + aDn-i) in the iid case. He also discusses asymptotes
for the moments of Dk when k ^ np^ 0 < p < 1, and the rate of convergence of
the finite-sample moments.

11.3.2 The non-IID  case

Let us assume that the Xj are all distinct. As in the iid case, we dispose of the
special situations first. When i = 0,

n n n

j=l j=l j=l

Hence, Lemma 11.3.1 can be used directly to obtain an explicit expression for
P{To > t).
When i = n  — 1^ Ti = X(^) and hence

n
p{Tn-i > i)=1 - n (i - ^"^'0 • (11-1^)

Exponential Order Statistics  181

As we see below, for 1 < i < n — 1, the expression for P{Ti > t) is more
involved.
For a given j , 1 < j < n, let S{j) be a set with {i — 1) elements taken from
{1, 2,... , n} - {j}. There are {^Zl) different choices for S{j). For each such
choice, let S{j) = {1,2,... , n} - {j} - S{j).

Theorem 11.3.1. Let Ti he given by (11.1) with I < i < n - \. Then, for
t > 0; P{Ti > t) can be expressed as

j=^ S(j) kesij)

rt/{n-i) rt/{n-i)
/ 11 {^-e~ )^W\
meS{j)  Xj + E K- i'Ti- i)Xk

reS{j)  > dx

^ /•oo ( I
+ E ^i E / n (1 - ^''"'') ^^p {-(^^ + E ^r)x > dx,

(11.16)

where
 Wk{S{j)) =  Ui^kesij) (l Af j

PROOF . The joint pdf of ^(i),... , X(^) is the sum of n! terms where each term
has the form
 n

k=l
where (r(l),... , r{n)) is a permutation of (1,... , n). Then

P{T,>t) = Y.j - /o«,<^^-<..<oo i i A.we-*'»>-<ix». (1M7)
n! Xi_|-iH--"+Xn>t fc=l

We split and group the n! terms using the following procedure:

(a) We fix X(^) = X and its parameter Aj, j = 1,... , n.

(b) Given j , we fix the parameters associated with A'(i),..., X(i_iy There are

such distinct ways of choosing their parameters.

182 H, N. Nagaraja

(c) The remaining parameters associated with -^(i+i),. •., -^(n) can be ordered
in (n — i)! ways.

Let S^{j) be a typical (ordered) set in (b) and S^{j) be a typical ordered set in
(c). The expression for P{Ti > t) given in (11.17) above can be written as

i-i
'" roo I r p "_ ^
E E E / ^.--'^" / • • 7 n Mk)e-'^^'^^'dx,

/ ... / TT A (u\e~^''^^^^^dxh

J 0<X<Xi+i<...<Xn<OO 1 1 ^^«J Xj+iH \-Xn>t k=l-\-l  (11.18)

For every unordered set S{j) that leads to S'^(j),
E [i-l n V)e-^'-«^'=dx J

SOU); Sij) fixed

can be seen as
 P( max Xk<x)= Yl {I- e-^"^), x > 0. (11.19)

Further, in (11.18), for every unordered set S(j) that leads to S (j),

E {/•••Lx...<...<.„<o o n V)e->^('=)-dx, |

S^'CJ); 5(j ) fixed ^ Xi+i-^-'-{-Xn>t k=i-\-l )

can be expressed as

V " g-^ErG5(j)^ ^
5"(j);5(j)fixed

j- j 0<y...<-<y.<^ n A.(,)e-V^.-d,J, (11.20)
2/i+iH \-yn>t-{n-i)x k=i+l )

by taking y^ = x^ — x^ k = i + 1,.. .^n. The multiple integral in (11.20), when
summed over S (j) for a fixed S{j)^ represents

P(F(i) + .. . + F(^_i)>t-(n-i)x )

where y(i),... , F(^_^) are the sample order statistics generated from (n — i)
independent exponential rvs having exp(Ar.)distribution, r G S{j). Thus, the
above expression is nothing but

P {Eres(j)yr >t-in- i)x) = P (E,e50 ) tZr>t-[n- i)x) , (11.21)

Exponential Order Statistics 183

where the Zr are iid standard exponential rvs. Thus, in view of Lemma 11.3.1,
for a fixed x and S{j), the expression in (11.21) reduces to

reS(j)

if X < t/{n — i)^ where the Wr{S{j)) are as given in the theorem. The expression
in (11.21) is clearly 1 if x > t/{n — i).
Combining the above with (11.19) and (11.20), and recalling (11.18), we are
led to the expression for P{Ti > t) given in (11.16). •

Note s

1. The first summation in (11.16) above has n x {^ZD x (^ — 0 distinct
terms and the second summation has n x {^ZD terms.
2. The form given by (11.16) holds when i = n - 1 as well. In that case
S{j) has only one element, Wk{S{j)) = 1, and J2reS(j) ^r — (^ — '^)^k = 0 in the
above expression. However, the expression given by (11.12) is much easier to
work with.
3. If some of the A^-'s coincide, one could use limiting argument to obtain
the relevant expression for P{Ti > t). The extreme setup of this type is the iid
case.
4. The distribution of the random variable Ti is helpful in finding probabil-
ities of interest in the performance analysis of multiple antenna systems. See
for example, Choi et al. (2003). There, the inid case is of interest.

11.3.3 The IID case vs. the INID case

It would be interesting to study the changes in the distributional properties of
Ti as one moves from the iid case to the inid case. Of course, the additional
complications that arise in the expression for the cdf in the inid case are evident
in the above discussion. The question of interest could be in terms of stochastic
comparisons. For example, how do the cdf of Ti in the inid case compare with
the one in the iid case?
Proschan and Sethuraman (1976) obtained a majorization result for order
statistics from heterogeneous populations with proportional hazard functions.
They showed that if the vector A = (Ai,... , A^)' majorizes i/ = (z/i,..., Vn)'-> Xi
is exp(Ai), Yi is exp(^'i), and they are all mutually independent, then (-X'(i),...,
X(^)) is stochastically larger than (^(i),. • .,F(n))- Without loss of generality,
we can take Ai > • • • > A^^ and i^i > - - - > Vn-, then the first vector majorizes the
second if Yl)^i Aj > Zlj=:i ^j for 1 < i < n, and equality holds when i — n. This
means any monotonically increasing function of order statistics is stochastically
larger with parameter vector A than with i/, and in particular, this property

184 H. N. Nagaraja

holds for Ti. The iid case corresponds to the vector (A,..., A)' and is majorized
by any A with at least two distinct components. Thus, Ti will have a larger
mean under heterogeneity than under homogeneity when the sum of the hazard
rates remains the same. But, then one has to keep in mind that

E{Xi + • • • + Xn) = E{To) = Y (iid case)
A
n ^
= y ^ T- (inid case).
• 1 Ai

When ^ Ai = nA, from the '^arithmetic mean-harmonic mean inequality," it
is clear that the mean of the sample average (= TQ/U) in the iid case is itself
(much) smaller than its mean in the inid case. Thus, a similar result for Ti
when i > 0 is hardly surprising given that components of Ti tend to be those
Xj with larger means or smaller hazard rates.

References

1. Andrews, D. M. (1996). Moments of the selection differential from ex-
ponential and uniform parents. In Statistical Theory and Applications:
Papers in Honor of Herbert A, David (Eds. H. N. Nagaraja, P. K. Sen,
and D. F. Morrison), pp. 67-80, Springer-Verlag, New York.

2. Choi, Y.-S., Nagaraja, H. N., and Alamouti, S. M. (2003). Performance
analysis and comparisons of antenna and beam selection/combining
diversity. Submitted for publication.

3. David, H. A., and Nagaraja, H. N. (2003). Order Statistics, Third edition,
John Wiley & Sons, New York.

4. Khaledi, B.-E., and Kochar, S. (2000). Dependence among spacings.
Probability in the Engineering and Information Sciences, 14, 461-472.

5. Nagaraja, H. N. (1981). Some finite sample results for the selection dif-
ferential. Annals of the Institute of Statistical Mathematics, 33, 437-448.

6. Nagaraja, H. N. (1982). Some nondegenerate limit laws for the selection
differential. Annals of Statistics, 10, 1306-1310.

7. Nevzorov, V. B. (1984). Representations of order statistics, based on ex-
ponential variables with different scaling parameters, Zapiksi Nauchnykh
Seminarov Leningradskogo Otdeleniya Matematicheskogo Instituta imeni
V. A. Steklova Akademii Nauk SSSR (LOMI), 136, 162-164; English
translation (1986). Journal of Soviet Mathematics, 33, 797-798.

Exponential Order Statistics 185

8. Nevzorova, L., and Nevzorov, V. (1999). Ordered random variables, Acta
Applicandae Mathematicae^ 58, 217-229.

9. Proschan, F., and Sethuraman, J. (1976). Stochastic comparisons of order
statistics from heterogeneous populations, with applications in reliability.
Journal of Multivariate Analysis^ 6, 608-616.

10. Renyi, A. (1953). On the theory of order statistics. Acta Mathematica
Academiae Scientiarum Hungaricae^ 4, 191-231.

11. Tikhov, M. (1991). Reducing of test duration for censored samples, The-
ory of Probability and Applications^ 36, 604-607.
