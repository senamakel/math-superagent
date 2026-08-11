> **Excerpt only — read this first.** The complete text is one level down at `research/L0/inid_exponential_order_statistics_uic.full.full.md`; open that only when this file does not answer the question, because it is large. Replace this excerpt with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

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


*[excerpt ends; 15094 characters not shown — see `research/L0/inid_exponential_order_statistics_uic.full.full.md`]*
