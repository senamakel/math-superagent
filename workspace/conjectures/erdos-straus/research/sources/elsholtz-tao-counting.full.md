<!-- source: https://terrytao.files.wordpress.com/2011/07/egyptian-count13.pdf | converted from PDF -->

COUNTING THE NUMBER OF SOLUTIONS TO THE ERD ˝OS-STRAUS
EQUATION ON UNIT FRACTIONS

CHRISTIAN ELSHOLTZ AND TERENCE TAO

Abstract. For any positive integer n, let f (n) denote the number of solutions to the Diophantine
equation 4
n = 1
x + 1
y + 1
z with x, y, z positive integers. The Erd˝os-Straus conjecture asserts that
f (n) > 0 for every n ⩾ 2. To solve this conjecture, it suﬃces without loss of generality to consider
the case when n is a prime p. In this paper we consider the question of bounding the sum ∑p<N f (p)
asymptotically as N → ∞, where p ranges over primes. Our main result establishes the asymptotic
upper and lower bounds
 N log2 N ≪ ∑

p⩽N f (p) ≪ N log2 N log log N.

In particular, f (p) = Oδ(log3 p log log p) for a subset of primes of density δ arbitrarily close to 1. Also,
for a subset of the primes with density 1 the following lower bound holds: f (p) ≫ (log p)0.549. These
upper and lower bounds show that a typical prime has a small number of solutions to the Erd˝os-
Straus Diophantine equation; small, when compared with other additive problems, like Waring’s
problem. We establish several more results on f and related quantities, for instance the bound

f (p) ≪ p 3
5 +O( 1
log log p ) for all primes p. Eventually we prove lower bounds for the number fm,k(n) of
solutions of m
n = 1
t1 + · · · + 1
tk , ∑

n⩽N fm,k(n) ≫m,k N (log N )2
k−1−1

and a related result for primes.
 1. Introduction

For any natural number
1 n ∈ N, let f (n) denote the number of solutions (x, y, z) ∈ N3 to the
Diophantine equation

(1.1) 4
n = 1
x + 1
y + 1
z

(we do not assume x, y, z to be distinct or in increasing order). Thus for instance

f (1) = 0, f (2) = 3, f (3) = 12, f (4) = 10, f (5) = 12, f (6) = 39, f (7) = 36, f (8) = 46, . . .

We plot the values of f (n) for n ⩽ 1000, and separately restricting to primes p ⩽ 1000.
From these graphs one might be tempted to draw conclusions, such as “f (n) ≫ n inﬁnitely often”,
that we will refute in our investigations below.
The Erd¨os-Straus conjecture (see e.g. [20]) asserts that f (n) > 0 for all n ⩾ 2; it remains unresolved,
although there are a number of partial results. The earliest references to this conjecture are papers by
Erd˝os [14] and Obl´ath [44], and we draw attention to the fact that the latter paper was submitted in
1948.
Most subsequent approaches list parametric solutions, which solve the conjecture for n lying in
certain residue classes. These soluble classes are either used for analytic approaches via a sieve method,
or for computational veriﬁcations. For instance, it was shown by Vaughan [73] that the number of

1991 Mathematics Subject Classiﬁcation. 11D68, 11N37 secondary: 11D72, 11N56.
1In this paper we consider the natural numbers N = {1, 2, . . .} as starting from 1.

1

2 CHRISTIAN ELSHOLTZ AND TERENCE TAO

200 400 600 800 1000

5000

10 000

15 000

20 000

25 000

30 000
 Figure 1. The value f (n) for all n ⩽ 1000.

200 400 600 800 1000

200

400

600

800

1000
 Figure 2. The value f (p) for all primes p ⩽ 1000.

n < N for which f (n) = 0 is at most N exp(−c log2/3 N ) for some absolute constant c > 0 and all
suﬃciently large N . (Compare also [43, 75, 34, 80] for some weaker results).
The conjecture was veriﬁed for all n ⩽ 1014 in [70]. We list a more complete history of these
computations, but there may be many further unpublished computations as well.

5000 ⩽ 1950 Straus, see [14]
8000 1962 Bernstein [6]
20000 ⩽ 1969 Shapiro, see [39]
106128 1948/9 Oblath [44]
141648 1954 Rosati [52]
107 1964 Yamomoto [79]
1.1 × 107 1976 Jollensten [30]
108 1971 Terzi
1 [72]
109 1994 Elsholtz & Roth
2

1010 1995 Elsholtz & Roth
2

1.6 × 1011 1996 Elsholtz & Roth
2

1010 1999 Kotsireas [31]
1014 1999 Swett [70]

COUNTING THE NUMBER OF SOLUTIONS TO THE ERD ˝OS-STRAUS EQUATION ON UNIT FRACTIONS 3

Most of these previous approaches concentrated on the question whether f (n) > 0 or not. In this
paper we will instead study the average growth or extremal values of f (n).
Since we clearly have f (nm) ⩾ f (n) for any n, m ∈ N, we see that to prove the Erd¨os-Straus
conjecture it suﬃces to do so when n is equal to a prime p.
In this paper we investigate the average behaviour of f (p) for p a prime. More precisely, we consider
the asymptotic behaviour of the sum X

p⩽N f (p)

where N is a large parameter, and p ranges over all primes less than N . As we are only interested in
asymptotics, we may ignore the case p = 2, and focus on the odd primes p.
Let us call a solution (x, y, z) to (1.1) a Type I solution if n divides x but is coprime to y, z, and
a Type II solution if n divides y, z but is coprime to x. Let fI(n), fII(n) denote the number of Type I
and Type II solutions respectively. By permuting the x, y, z we clearly have

(1.2) f (n) ⩾ 3fI(n) + 3fII(n)

for all n > 1. Conversely, when p is an odd prime, it is clear from considering the denominators in the
Diophantine equation

(1.3) 4
p = 1
x + 1
y + 1
z

that at least one of x, y, z must be divisible by p; also, it is not possible for all three of x, y, z to be
divisible by p as this forces the right-hand side of (1.3) to be at most 3
p . We thus have

(1.4) f (p) = 3fI(p) + 3fII(p)

for all odd primes p. Thus, to understand the asymptotics of P
 p⩽N f (p), it suﬃces to understand the
asymptotics of P
 p⩽N fI(p) and P
 p⩽N fII(p). As we shall see, Type II solutions are somewhat easier
to understand than Type I solutions, but we will nevertheless be able to control both types of solutions
in a reasonably satisfactory manner.
We can now state our ﬁrst main theorem2.

Theorem 1.1 (Average value of fI, fII). For all suﬃciently large N , one has the bounds

N log3 N ≪ X

n⩽N fI(n) ≪ N log3 N

N log3 N ≪ X

n⩽N fII(n) ≪ N log3 N

N log2 N ≪ X

p⩽N fI(p) ≪ N log2 N log log N

N log2 N ≪ X

p⩽N fII(p) ≪ N log2 N.

1It appears that Terzi’s set of soluble residue classes is correct, but that the set of checked primes in these classes is
incomplete. Another reference to a calculation up to 108 due to N. Franceschine III (1978) (see [20, 16] and frequently re-
stated elsewhere) only mentions Terzi’s calculation, but is not an independent veriﬁcation. We are grateful to I. Kotsireas
for conﬁrming this.
2unpublished
2In a previous version of this manuscript, the weaker bound ∑p⩽N fII(p) ≪ N log2 N log log N was claimed.
As pointed out subsequently by Jia [29], the argument in that previous version in fact only gave ∑p⩽N fII(p) ≪
N log2 N log log2 N , but can be repaired to give the originally claimed bound ∑
p⩽N fII(n) ≪ N log2 N log log N . These
bounds are of course superceded by the results in Theorem 1.1.

4 CHRISTIAN ELSHOLTZ AND TERENCE TAO

Here, we use the usual asymptotic notation X ≪ Y or X = O(Y ) to denote the estimate |X| ⩽ CY
for an absolute constant C, and use subscripts if we wish to allow dependencies in the implied constant
C, thus for instance X ≪ε Y or X = Oε(Y ) denotes the estimate |X| ⩽ CεY for some Cε that can
depend on ε.
As a corollary of this and (1.4), we see that

N log2 N ≪ X

p⩽N f (p) ≪ N log2 N log log N.

From this, the prime number theorem, and Markov’s inequality, we see that for any ε > 0, we can ﬁnd
a subset of A primes of relative lower density at least 1 − ε, thus

(1.5) lim inf
N →∞ |{p ∈ A : p ⩽ N }|
|{p : p ⩽ N }| ⩾ 1 − ε,

such that f (p) = Oε(log3 p log log p) for all p ∈ A. Informally, a typical prime has only O(log3 p log log p)
solutions to the Diophantine equation (1.3); or alternatively, for any function ξ(p) of p that goes to
inﬁnity as p → ∞, one has O(ξ(p) log3 p log log p) for all p in a subset of the primes of relative density
1. This provides an explanation as to why analytic methods (such as the circle method) appear to be
insuﬃcient to resolve the Erd˝os-Straus conjecture, as such methods usually only give non-trivial lower
bounds on the number of solutions to a Diophantine equation in the case when the number of such
solutions grows polynomially with the height parameter N .
The double logarithmic factor log log N in the above arguments arises from technical limitations to
our method (and speciﬁcally, in the ineﬃcient nature of the Brun-Titchmarsh inequality (A.10) when
applied to very short progressions), and we conjecture that it should be eliminated.

Remark 1.2. In view of these results, one can naively model f (p) as a Poisson process with intensity
at least ≫ log3 p. Using this probabilistic model as a heuristic, one expects any given prime to have a
“probability” 1 − O(exp(−c log3 p)) of having at least one solution, which by the Borel-Cantelli lemma
suggests that the Erd¨os-Straus conjecture is true for all but ﬁnitely many p. Of course, this is only a
heuristic and does not constitute a rigorous argument. (However, one can view the results in [73], [12],
based on the large sieve, as a rigorous analogue of this type of reasoning.)

Remark 1.3. From Theorem 1.1 we have the lower bound P
 n⩽N f (n) ≫ N log3 N . In fact one has
the stronger bound P
 n⩽N f (n) ≫ N log6 N (Heath-Brown, private communication) using the methods
from [23]; see Remark 2.9 for further discussion.

To prove Theorem 1.1, we ﬁrst use some solvability criteria for Type I and Type II solutions to
obtain more tractable expressions for fI(p) and fII(p). As we shall see, fI(p) is essentially (up to a
factor of two) the number of quadruples (a, c, d, f ) ∈ N4 with 4acd = p + f , f dividing 4a
2d + 1, and
acd ⩽ 3p
4 , while fII(p) is essentially the number of quadruples (a, c, d, e) ∈ N4 with 4acde = p + 4a
2d + e
and acde ⩽ 3
2 p. (We will systematically review the various known representations of Type I and Type
II solutions in Section 2.) This, combined with standard tools from analytic number theory such as the
Brun-Titchmarsh inequality and the Bombieri-Vinogradov inequality, already gives most of Theorem
1.1. The most diﬃcult bound is the upper bounds on fI, which eventually require an upper bound for
expressions of the form X

a⩽A
 X

b⩽B τ (kab2 + 1)

for various A, B, k, where τ (n) := P
 d|n 1 is the number of divisors of n, and d|n denotes the assertion
that d divides n. By using an argument of Erd˝os [15], we obtain the following bound on this quantity:

Proposition 1.4 (Average value of τ (kab2 + 1)). For any A, B > 1, and any positive integer k ≪
(AB)
O(1), one has X

a⩽A
 X

b⩽B τ (kab2 + 1) ≪ AB log(A + B) log(1 + k).

COUNTING THE NUMBER OF SOLUTIONS TO THE ERD ˝OS-STRAUS EQUATION ON UNIT FRACTIONS 5

Remark 1.5. Using the heuristic that τ (n) ∼ log n on the average (see (A.5)), one expects the true
bound here to be O(AB log(A + B)). The log(1 + k) loss can be reduced (for some ranges of A, B, k, at
least) by using more tools (such as the Polya-Vinogradov inequality), but this slightly ineﬃcient bound
will be suﬃcient for our applications.

We prove Proposition 1.4 (as well as some variants of this estimate) in Section 7. Our main tool is
a more quantitative version of a classical bound of Erd˝os [15] on the sum P
 n⩽N τ (P (n)) for various
polynomials P , which may be of independent interest; see Theorem 7.1.
We also collect a number of auxiliary results concerning the quantities fi(n), some of which were in
previous literature. Firstly, we have a vanishing property at odd squares:

Proposition 1.6 (Vanishing). For any odd perfect square n, we have fI(n) = fII(n) = 0.

This observation essentially dates back to Schinzel (see [20][39], [59]) and Yamomoto (see [79]) and
is an easy application of quadratic reciprocity (A.7): for the convenience of the reader, we give the
proof in Section 4. A variant of this proposition was also established in [5]. Note that this does not
disprove the Erd¨os-Straus conjecture, since the inequality (1.2) does not hold with equality on perfect
squares; but it does indicate a key diﬃculty in attacking this conjecture, in that when showing that
fI(p) or fII(p) is non-zero, one can only use methods that must necessarily fail when p is replaced by an
odd square such as p
2, which already rules out many strategies (e.g. a ﬁnite set of covering congruence
strategies, or the circle method).
Next, we establish some upper bounds on fI(n), fII(n) for ﬁxed n:

Proposition 1.7 (Upper bounds). For any n ∈ N, one has

fI(n) ≪ n 3
5 +O( 1
log log n )

and fII(n) ≪ n 2
5 +O( 1
log log n ).
In particular, from this and (1.4) one can conclude that for any prime p one has

f (p) ≪ p 3
5 +O( 1
log log p ).

This should be compared with the recent result in [7], which gives the bound f (n) ≪ε n2/3+ε for all n
and all ε > 0. For composite n the treatment of parameters dividing n appears to be more complicated
and here we concentrate on those two cases that are motivated by the Erd˝os-Straus equation for prime
denominator.
We prove this proposition in Section 3.
The main tools here are the multiple representations of Type I and Type II solutions available (see
Section 2) and the divisor bound (A.6). The values of f (n) appear to ﬂuctuate in some respects as the
values of the divisor function, but behave much more regular on average. Moreover, in view of Theorem
1.1, one might also expect to have f (n) ≪ε nε for any ε > 0, but such logarithmic-type bounds on
solutions to Diophantine equations seem diﬃcult to obtain in general (Proposition 1.7 appears to be
the limit of what one can obtain purely from the divisor bound (A.6) alone).
In the reverse direction, we have the following lower bounds on f (n) for various sets of n:

Theorem 1.8 (Lower bounds). For inﬁnitely many n, one has

f (n) ⩾ exp((log 3 + o(1)) log n
log log n ),

where o(1) denotes a quantity that goes to zero as n → ∞.
For any function ξ(n) going to +∞ as n → ∞, one has

f (n) ⩾ exp   log 3
2 log log n − O(ξ(n)
p log log n)
  ≫ (log n)
0.549

for all n in a subset A of natural numbers of density 1 (thus |A∩{1,...,N }|
N → 1 as N → ∞).

6 CHRISTIAN ELSHOLTZ AND TERENCE TAO

Finally, one has
 f (p) ⩾ exp   ( log 3
2 − o(1)) log log p  ≫ (log p)0.549

for all primes p in a subset B of primes of relative density 1 (thus |{p∈B:p⩽N }|
|{p:p⩽N }| → 1 as N → ∞).

As the proof shows the ﬁrst two lower bounds are already valid for sums of two unit fractions. The
result directly follow from the growth of certain divisor functions. An even better model for f (n) is a
suitable superposition of several divisor functions. The proof will be in Section 6.
Finally, we consider (following [39], [59]) the question of ﬁnding polynomial solutions to (1.1).
Let us call a primitive
3 residue class n = r mod q solvable by polynomials if there exist polynomials
P1(n), P2(n), P3(n) which take positive integer values for all suﬃciently large n in this residue class (so
in particular, the coeﬃcients of P1, P2, P3 are rational), and such that

4
n = 1
P1(n) + 1
P2(n) + 1
P3(n)

for all n. By Dirichlet’s theorem
4, the primitive residue class r mod q contains arbitrarily large primes
p. For each large prime p in this class, we either have one or two of the P1(p), P2(p), P3(p) divisible by
p, as observed previously. For p large enough, note that Pi(p) can only be divisible by p if there is no
constant term in Pi. We thus conclude that either one or two of the Pi(n) have no constant term, but
not all three. Let us call the congruence Type I solvable if one can take exactly one of P1, P2, P3 to
have no constant term, and Type II solvable if exactly two have no constant term. Thus every solvable
primitive residue class r mod q is either Type I or Type II solvable.
It is well-known (see [39]) that any primitive residue class n = r mod 840 is solvable by polynomials
unless r is a perfect square. On the other hand, it is also known (see [39], [59]) that a primitive
congruence class n = r mod q which is a perfect square, cannot be solved by polynomials (this also
follows from Proposition 1.6). The next proposition classiﬁes all solvable primitive congruences.

Proposition 1.9 (Solvable congruences). Let q mod r be a primitive residue class. If this class is
Type I solvable by polynomials, then all suﬃciently large primes in this class belong to one of the
following sets:
• {n = −f mod 4ad}, where a, d, f ∈ N are such that f |4a2d + 1. [43]
• {n = −f mod 4ac} ∩ {n = − c
a mod f }, where a, c, f ∈ N are such that (4ac, f ) = 1.
• {n = −f mod 4cd} ∩ {n2 = −4c
2d mod f }, where c, d, f ∈ N are such that (4cd, f ) = 1.
• {n = − 1
e mod 4ab}, where a, b, e ∈ N are such that e|a + b and (e, 4ab) = 1. [1], [52]
Conversely, any residue class in one of the above four sets is solvable by polynomials.
Similarly, q mod r is Type II solvable by polynomials if and only if it is a subset of one of the
following residue classes:
• −e mod 4ab, where a, b, e ∈ N are such that e|a + b and (e, 4ab) = 1. [1]
• −4a
2d mod f , where a, d, f ∈ N are such that 4ad|f + 1. [73], [52]
• −4a
2d − e mod 4ade, where a, d, e ∈ N are such that (4ad, e) = 1. [43]

As indicated by the citations, many of these residue classes were observed to be solvable by poly-
nomials in previous literature, but some of the conditions listed here appear to be new, and they form
the complete list of all such classes. We prove Proposition 1.9 in Section 10.

3A residue class r mod q is primitive if r is coprime to q. One could also consider non-primitive congruences, but
these congruences only contain ﬁnitely many primes and are thus of less interest to solving the Erd¨os-Straus conjecture
(and if the Erd¨os-Straus conjecture held for a common factor of r and q, then the residue class r mod q would trivially
be solvable by polynomials.
4One does not need the full strength of Dirichlet’s theorem for this analysis, as it would suﬃce to work with almost
primes p that are coprime to all small natural numbers. Alternatively, one could argue using the proﬁnite (Furstenberg)
topology on the natural numbers, but we will not adopt this viewpoint here.

COUNTING THE NUMBER OF SOLUTIONS TO THE ERD ˝OS-STRAUS EQUATION ON UNIT FRACTIONS 7

Remark 1.10. The results in this paper would also extend (with minor changes) to the more general
situation in which the numerator 4 in (1.3) is replaced by some other ﬁxed positive integer, a situation
considered ﬁrst by Sierpi´nski and Schinzel (see e.g. [65, 73, 45, 46, 68]).

We will not detail all of these extensions here but in Section 11 we extend our study of the average
number of solutions to the more general question on sums of k unit fractions

(1.6) m
n = 1
t1 + 1
t2 + · · · + 1
tk .

If m > k ⩾ 3, and the ti are positive integers, then it is an open problem if for each suﬃciently large n
there is at least one solution. The Erd˝os-Straus conjecture with m = 4, k = 3, discussed above, is the
most prominent case. If m and k are ﬁxed, one can again establish sets of residue classes, such that
1.6 is generally soluble if n is in any of these residue classes.
The problem of classifying solutions of 1.6 has been studied by Rav [51], S´os [67] and Elsholtz [12].
Moreover Viola [74], Shen [63] and Elsholtz [13] have used a suitable subset of these solutions to give
(for ﬁxed m > k ⩾ 3) quantitive bounds on the number of those integers n ⩽ N , for which 1.6 does
not have any solution.
We will focus on the case5 Type II solutions, in which6 t2, . . . , tk are divisible by n. For given m, k, n,
let fm,k,II(n) denote the number of Type II solutions. Our main result regarding this quantity is the
following lower bound on this quantity:

Theorem 1.11. Let m > k ⩾ 3 be ﬁxed. Then, for N suﬃciently large, one has

(1.7) X

n⩽N fm,k,II(n) ≫m,k N (log N )
2
k−1−1

and

(1.8) X

p⩽N fm,k,II(p) ≫m,k N (log N )2
k−1−2

log log N .

Our emphasis here is on the exponential growth of the exponent. In particular, as k increases by
one, the average number of solutions is roughly squared. The denominator of log log N is present for
technical reasons (due to use of the crude lower bound (A.11) on the Euler totient function), and it is
likely that it could be eliminated (much as it is in the m = 4, k = 3 case) with additional eﬀort.

Remark 1.12. If we let fm,k(n) be the total number of solutions to (1.6) (not just Type II solutions),
then we of course obtain as a corollary that
X

n⩽N fm,k(n) ≫k N (log N )
2
k−1−1.

We do not expect the power of the logarithm to be sharp in this case (cf. Remark 2.9). For instance,
in [26] it is shown that X

n⩽N fm,2(n) =   1
φ(m) + o(1)
  N log2 N

for any ﬁxed m.

5The classiﬁcation of solutions that we give below also works for other divisibility patterns, but Type II solutions are
the easiest to count, and so we shall restrict our attention to this case.
6Strictly speaking, the deﬁnition of a Type II solution here is slightly diﬀerent from that discussed previously, because
we do not require that t1 is coprime to n. However, this coprimality automatic when n is prime (otherwise the right-hand
side of (1.6) would only be at most k/n). For composite n, it is possible to insert this condition and still obtain the lower
bound (1.7), but this would complicate the argument slightly and we have chosen not to do so here.

8 CHRISTIAN ELSHOLTZ AND TERENCE TAO

Note that the equation (1.6) can be rewritten as

1
mt1 + · · · + 1
mtk + 1
−n = 0,

which is primitive when n is prime. As a consequence, we obtain a lower bound for the number of
integer points on the (generalised) Cayley surface:

Corollary 1.13. Let k ⩾ 3. The number of integer points of the following generalization of Cayley’s
cubic surface,
 0 =
 kX
 i=0
 1
ti ,

with ti non-zero integers with mini |ti| ⩽ N , is ≫k N (log N )
2
k−1−2/ log log N .

Again, the double logarithmic factor should be removable with some additional eﬀort, although the
exponent 2k−1 − 2 is not expected to be sharp, and should be improvable also.
Part of the ﬁrst author’s work on ths project was supported by the German National Merit Foun-
dation. The second author is supported by a grant from the MacArthur Foundation, by NSF grant
DMS-0649473, and by the NSF Waterman award. The authors thank Nicolas Templier for many help-
ful comments and references. The ﬁrst author is very grateful to Roger Heath-Brown for very generous
advice on the subject (dating back as far as 1994). Both authors are particularly indebted to him
for several remarks (including Remark 2.9), and also for contributing some of the key arguments here
(such as the lower bound on P
 n⩽N fII(n) and P
 p⩽N fII(p)) which have been reproduced here with
permission. The ﬁrst author also wishes to thank Tim Browning, Ernie Croot and Arnd Roth for
discussions on the subject.

2. Representation of Type I and Type II solutions

We now discuss the representation of Type I and Type II solutions. There are many such represen-
tations in the literature (see e.g. [1], [5], [6], [43], [51], [52], [73], [76]); we will remark how each of these
representations can be viewed as a form of the one given here after using describing a certain algebraic
variety in coordinates.
For any non-zero complex number n, consider the algebraic surface

Sn := {(x, y, z) ∈ C3 : 4xyz = nyz + nxz + nxy} ⊂ C3.

Of course, when n is a natural number, f (n) is nothing more than the number of N-points (x, y, z) ∈
Sn ∩ N3 on this surface.
It is somewhat inconvenient to count N-points on Sn directly, due to the fact that x, y, z are likely to
share many common factors. To eliminate these common factors, it is convenient to lift Sn to higher-
dimensional varieties ΣI
n, ΣII
n (and more speciﬁcally, a three-dimensional variety in C6), which are
adapted to parameterising Type I and Type II solutions respectively. This will replace the three original
coordinates x, y, z by six coordinates a, b, c, d, e, f , any three of which can be used to parameterise ΣI
n.
or Σ
II
n . This multiplicity of parameterisations will be useful for many of the applications in this paper;
rather than pick one parameterisation in advance, it is convenient to be able to pick and choose between
them, depending on the situation.

COUNTING THE NUMBER OF SOLUTIONS TO THE ERD ˝OS-STRAUS EQUATION ON UNIT FRACTIONS 9

We begin with the description of Type I solutions. More precisely, we deﬁne ΣI
n to be the set of all
sextuples (a, b, c, d, e, f ) ∈ C6 which are non-zero and obey the constraints7

4abd = ne + 1(2.1)
 ce = a + b(2.2)
 4abcd = na + nb + c(2.3)
 4acde = ne + 4a
2d + 1(2.4)
 4bcde = ne + 4b
2d + 1(2.5)
 4acd = n + f(2.6)
 ef = 4a2d + 1(2.7)
 bf = na + c(2.8)
 n2 + 4c2d = f (4bcd − n).(2.9)

This is an algebraic set that can be parameterised by ﬁxing three of the six coordinates a, b, c, d, e, f and
solving for the other three coordinates. For instance, using the coordinates a, c, d, one easily veriﬁes
that
 ΣI
n =   (a, na + c
4acd − n , c, d, 4a2d + 1
4acd − n , 4acd − n) : a, c, d ∈ C3; 4acd ̸= n 

and similarly for the other   6
3  −1 = 14 choices of three coordinates; we omit the elementary but tedious
computations
8. Thus we see that Σ
I
n is a three-dimensional algebraic variety. From (2.3) we see that
the map πI
n : (a, b, c, d, e, f ) ↦→ (abdn, acd, bcd)
maps ΣI
n to Sn. After quotienting out by the dilation symmetry

(2.10) (a, b, c, d, e, f ) ↦→ (λa, λb, λc, λ−2d, e, f )

of ΣI
n, this map is injective.
If n is a natural number, then πI
n clearly maps N-points of ΣI
n to N-points of Sn, and if c is coprime
to n, gives a Type I solution (note that abd is automatically coprime to n, thanks to (2.1)). In the
converse direction, all Type I solutions arise in this manner:

Proposition 2.1 (Description of Type I solutions). Let n ∈ N, and let (x, y, z) be a Type I solution.
Then there exists a unique (a, b, c, d, e, f ) ∈ N6 ∩ ΣI
n with abcd coprime to n and a, b, c having no
common factor, such that πI
n(a, b, c, d, e, f ) = (x, y, z).

Proof. The uniqueness follows since πI
n is injective after quotienting out by dilations. To show existence,
we factor x = ndx′, y = dy′, z = dz′, where x′, y′, z′ are coprime, then after multiplying (1.1) by ndx′y′z′

we have

(2.11) 4dx
′y′z′ = y′z′ + nx′y′ + nx′z′.

As y′, z′ are coprime to n, we conclude that x′ divides y′z′, y′ divides x′z′, and z′ divides x′y′. Splitting
into prime factors, we conclude that

(2.12) x′ = ab, y′ = ac, z′ = bc

for some natural numbers a, b, c; since x′, y′, z′ have no common factor, a, b, c have no common factor
also. As y, z were coprime to n, abcd is coprime to n also.

7There are multiple redundancies in these constraints; to take just one example, (2.9) follows from (2.3) and (2.6).
One could in fact specify ΣI
n using just three of these nine constraints if desired. However, this redundancy will be useful
in the sequel, as we will be taking full advantage of all nine of these identities.
8In a few cases, for instance when using c, d, e as coordinates, one may need to solve some quadratic equations to
obtain the remaining variables, so that one may have two points in ΣI
n, rather than one, associated to each triple of
coordinates.

10 CHRISTIAN ELSHOLTZ AND TERENCE TAO

Substituting (2.12) into (2.11) we obtain (2.3), which in particular implies (as c is coprime to n)
that c divides a + b. If we then set e := a+b
c and f := 4acd − n = na+c
b , then e, f are natural
numbers, and we obtain the other identities (2.1)-(2.9) by routine algebra. By construction we have
πI
n(a, b, c, d, e, f ) = (x, y, z), and the claim follows. □

In particular, for ﬁxed n, a Type I solution exists if and only if there is an N-point (a, b, c, d, e, f ) of
ΣI
n with abcd coprime to n (the requirement that a, b, c have no common factor can be removed using
the symmetry (2.10)). By parameterising Σ
I
n using three or four of the six coordinates, we recover
some of the known characterisations of Type I solvability:

Proposition 2.2. Let n be a natural number. Then the following are equivalent:

• There exists a Type I solution (x, y, z).
• There exists a, b, e ∈ N with e|a + b and 4ab|ne + 1. [1]
• There exists a, b, c, d ∈ N such that 4abcd = na + nb + c with c coprime to n. [6]
• There exist a, c, d, e ∈ N such that ne + 1 = 4ad(ce − a) with c coprime to n. [52, 39]
• There exist a, c, d, f ∈ N such that n = 4acd − f and f |4a
2d + 1, with c coprime to n. [43]
• There exist b, c, d, e with ne = (4bcde − 1) − 4b2d and c coprime to n. [5]

The proof of this proposition is routine and is omitted.

Remark 2.3. Type I solutions (x, y, z) have the obvious reﬂection symmetry (x, y, z) ↦→ (x, z, y). With
(2.6) and (2.9) the corresponding symmetry for ΣI
n is given by

(a, b, c, d, e, f ) ↦→   b, a, c, d, e, n2 + 4c2d
f
   .

We will typically only use the ΣI
n parameterisation when y ⩽ z (or equivalently when a ⩽ b), in order
to keep the sizes of various parameters small.

Remark 2.4. If we consider N-points (a, b, c, d, e, f ) of ΣI
n with a = 1, they can be explicitly parame-
terised as   1, ce − 1, c, ef − 1
4 , e, f  

where e, f are natural numbers with ef = 1 mod 4 and n = cef − c − f . This shows that any n of
the form cef − c − f with ef = 1 mod 4 solves the Erd˝os-Straus conjecture, an observation made in
[5]. However, this is a relatively small set of solutions (corresponding to roughly log2 n solutions for a
given n on average, rather than log3 n), due to the restriction a = 1. Nevertheless, in [5] it was veriﬁed
that all primes p = 1 mod 4 with p ⩽ 10
10 were representable in this form.

Now we turn to Type II solutions. Here, we replace Σ
I
n by the variety ΣII
n , as deﬁned the set of all
sextuples (a, b, c, d, e, f ) ∈ C6 which are non-zero and obey the constraints

4abd = n + e(2.13)
 ce = a + b(2.14)
 4abcd = a + b + nc(2.15)
 4acde = n + 4a2d + e(2.16)
 4bcde = n + 4b2d + e(2.17)
 4acd = f + 1(2.18)
 ef = n + 4a2d(2.19)
 bf = nc + a(2.20)
 4c2dn + 1 = f (4bcd − 1).(2.21)

COUNTING THE NUMBER OF SOLUTIONS TO THE ERD ˝OS-STRAUS EQUATION ON UNIT FRACTIONS 11

This is a very similar variety to ΣI
n; indeed the non-isotropic dilation

(a, b, c, d, e, f ) ↦→ (a, b, c/n2, dn, n2e, f /n)

is a bijection from ΣI
n to ΣII
n . Thus, as with ΣI
n, Σ
II
n is a three-dimensional algebraic variety in C6

which can be parameterised by any three of the six coordinates in (a, b, c, d, e, f ). As before, many of
the constraints can be viewed as redundant; for instance, (2.21) is a consequence of (2.15) and (2.18).
Note that Σ
II
n enjoys the same dilation symmetry (2.10) as ΣI
n, and also has the reﬂection symmetry
(using (2.18) and (2.21))
 (a, b, c, d, e, f ) ↦→   b, a, c, d, e, 4c
2dn + 1
f
   .

Analogously to πI
n, we have the map πII
n : Σ
II
n → Sn given by

(2.22) πII
n : (a, b, c, d, e, f ) ↦→ (abd, acdn, bcdn)

which is injective up to the dilation symmetry (2.10) and which, when n is a natural number, maps
N-points of ΣII
n to N-points of Sn, and when abd is coprime to n, gives Type II solutions. (Note that
this latter condition is automatic when n is prime, since x, y, z cannot all be divisible by n.)
We have an analogue of Proposition 2.1:

Proposition 2.5 (Description of Type II solutions). Let n ∈ N, and let (x, y, z) be a Type II solution.
Then there exists a unique (a, b, c, d, e, f ) ∈ N6 ∩ΣII
n with abd coprime to n and a, b, c having no common
factor, such that πI
n(a, b, c, d, e, f ) = (x, y, z).

Proof. Uniqueness follows from injectivity modulo dilations of πII
n as before. To show existence, we
factor x = dx
′, y = ndy′, z = ndz′, where x′, y′, z′ are coprime, then after multiplying (1.1) by ndx′y′z′

we have

(2.23) 4dx
′y′z′ = ny′z′ + x′y′ + x′z′.

As x′ are coprime to n, we conclude that x′ divides y′z′, y′ divides x′z′, and z′ divides x′y′. Splitting
into prime factors, we again obtain the representation (2.12) for some natural numbers a, b, c; since
x′, y′, z′ have no common factor, a, b, c have no common factor also. As x was coprime to n, abd is
coprime to n also.
Substituting (2.12) into (2.23) we obtain (2.15), which in particular implies that c divides a + b.
If we then set e := a+b
c and f := 4acd − 1, then e, f are natural numbers, and we obtain the other
identities (2.13)-(2.21) by routine algebra. By construction we have πII
n (a, b, c, d, e, f ) = (x, y, z), and
the claim follows. □

Again, we can recover some known characterisations of Type II solvability:

Proposition 2.6. Let n be a natural number. Then the following are equivalent:

• There exists a Type II solution (x, y, z).
• There exists a, b, e ∈ N with e|a + b and 4ab|n + e, and n+e
4 coprime to n. [1]
• There exists a, b, c, d ∈ N such that 4abcd = a + b + nc with abd coprime to n. [6, 39]
• There exists a, b, d ∈ N with 4abd − 1|b + nc with abd coprime to n. [73]
• There exist a, c, d, e ∈ N such that n = (4acd − 1)e − 4a2d with n+e
4 coprime to n. [52]
• There exist a, c, d, f ∈ N such that n = 4ad(ce − a) − e = e(4acd − 1) − 4a2d with ad(ce − a)
coprime to n. [43]

Next, we record some bounds on the order of magnitude of the parameters a, b, c, d, e, f assuming
that y ⩽ z.

12 CHRISTIAN ELSHOLTZ AND TERENCE TAO

Lemma 2.7. Let n ∈ N, and suppose that (x, y, z) = πI(a, b, c, d, e, f ) is a Type I solution such that
y ⩽ z. Then
 a ⩽ b
1
4 n < acd ⩽ 3
4 n

b < ce ⩽ 2b

an ⩽ bf ⩽ 5
3 an.

If instead (x, y, z) = πI(a, b, c, d, e, f ) is a Type II solution such that y ⩽ z, then

a ⩽ b
1
4 n < acde ⩽ n

b < ce ⩽ 2b

3acd ⩽ f < 4acd

Informally, the above lemma asserts that the magnitudes of the quantities (a, b, c, d, e, f ) are con-
trolled entirely by the parameters (a, c, d, f ) (in the Type I case) and (a, c, d, e) (in the Type II case),
with the bounds acd ∼ n, f ≪ n in the Type I case and acde ∼ n in the Type II case. The constants
in the bounds here could be improved slightly, but such improvements will not be of importance in our
applications.

Proof. First suppose we have a Type I solution. As y ⩽ z, we have a ⩽ b. From (2.2) we then have
b < ce ⩽ 2b, and thus from (2.8) we have

an ⩽ bf ⩽ an + 2
ef bf.

Now, from (2.7), ef = 1 mod 4. If e = f = 1, then from (2.2) and (2.8) we would have b = na + c =
na + a + b, which is absurd, thus ef ⩾ 5. This gives bf ⩽ 5
3 an as claimed. From (2.8) this implies that
c ⩽ 2an
3 , which in particular implies that bcd < abdn and so y ⩽ z < x. From (1.1) we conclude that

4
3n ⩽ 1
x < 4
n
which gives the bound 1
4 n < acd ⩽ 3
4 n as claimed.
Now suppose we have a Type II solution. Again a ⩽ b and b < ce ⩽ 2b. From (2.15) we have

nc < 4abcd ⩽ nc + 2abcd

and thus n
4 < abd ⩽ n
2 , which by the ce bound gives n
4 < acde ⩽ n. Since f = 4acd − 1, we have
3acd ⩽ f < 4acd, and the claim follows. □

Remark 2.8. From the above bounds one can also easily deduce the following observation: if 4
p =
1
x + 1
y + 1
z , then the largest denominator max(x, y, z) is always divisible by p. (This observation also
appears in [12].)

Remark 2.9. Propositions 2.1, 2.5 can be viewed as a special case of the classiﬁcation by Heath-Brown
[23] of primitive integer points (x1, x2, x3, x4) ∈ (Z\{0})
4 on Cayley’s surface
  (x1, x2, x3, x4) : 1
x1 + 1
x2 + 1
x3 + 1
x4 = 0
  ,

where by “primitive” we mean that x1, x2, x3, x4 have no common factor. Note that if n, x, y, z solve
(1.1), then (−n, 4x, 4y, 4z) is an integer point on this surface, which will be primitive when n is prime.
In [23, Lemma 1] it is shown that such integer points (x1, x2, x3, x4) take the form

xi = ϵyjykylzijzikzil

COUNTING THE NUMBER OF SOLUTIONS TO THE ERD ˝OS-STRAUS EQUATION ON UNIT FRACTIONS 13

for {i, j, k, l} = {1, 2, 3, 4}, where ϵ ∈ {−1, +1} is a sign, and the yi, zij are non-zero integers obeying
the coprimality constraints (yi, yj) = (zij, zkl) = (yi, zij) = 1

for {i, j, k, l} = {1, 2, 3, 4}, and obeying the equation
X

{i,j,k,l}={1,2,3,4} yizjkzklzlj = 0.

Conversely, any ϵ, yi, zij obeying the above conditions induces a primitive integer point on Cayley’s
surface. The Type I (resp. Type II) solutions correspond, roughly speaking, to the cases when one of
the z1i (resp. one of the yi) in the factorisation

n = x1 = ϵy2y3y4z12z13z14

are equal to ±n. The yi, zij coordinates are closely related to the (a, b, c, d, e, f ) coordinates used in this
section; in [23] it is observed that the variety parameterised by these coordinates can be viewed as the
universal torsor [9] of Cayley’s surface.
In [23] it was shown that the number of integer points (x1, x2, x3, x4) on Cayley’s surface of max-
imal height max(|x1|, . . . , |x4|) bounded by N was comparable to N log6 N . This is not quite the situ-
ation considered in our paper; a solution to (1.1) with n ⩽ N induces an integer point (x1, x2, x3, x4)
whose minimal height min(|x1|, . . . , |x4|) is bounded by N . Nevertheless, the results in [23] can be
easily modiﬁed (by minor adjustments to account for the restriction that three of the xi are positive,
and restricting n to be a multiple of 4 to eliminate divisibility constraints) to give a lower boundP
 n⩽N f (n) ≫ N log6 N for the number of such points, though it is not immediately obvious whether
this lower bound can be matched by a corresponding upper bound. Nevertheless, we see that there are
several logarithmic factors separating the general solution count from the Type I and Type II solution
count; in particular, for generic n, the majority of solutions to (1.1) will neither be Type I nor Type II.

We close this section with a small remark about solutions to the equation
m
p = 1
x + 1
y + 1
z

for m > 3 and p coprime to m, namely that none of the denominators can be divisible by p2. (We will
not use this fact though in the rest of the paper.)

Proposition 2.10. Let m
p = 1
x + 1
y + 1
z where m > 3, p is a prime not dividing m, and x, y, z are
natural numbers. Then none of x, y, z are divisible by p.

Note that there are a small number of counterexamples to this proposition for m ⩽ 3, such as
3
2 = 1
1 + 1
4 + 1
4 .

Proof. We may assume that (x, y, z) is either a Type I or Type II solution (replacing 4 by m as
needed). In the Type I case (x, y, z) = (abdp, acd, bcd), the claim is already clear since abcd is known
to be coprime to p. In the Type II case (x, y, z) = (abd, acdp, bcdp) it is known that abd is coprime to
p, so the only remaining task is to establish that c is coprime to p also.
Suppose c is not coprime to p; then y, z are both divisible by p
2. In particular
1
y + 1
z ⩽ 2
p2

and hence m
p > 1
x ⩾ m
p − 2
p2 .

Taking reciprocals, we conclude that
 p < mx ⩽ p(1 − 2
mp )−1.

14 CHRISTIAN ELSHOLTZ AND TERENCE TAO

Bounding (1 − ε)
−1 < 1 + 2ε when 0 < ε < 1/2, we conclude that

p < mx < p + 4
m .

But if m > 4, this forces mx to be a non-integer, a contradiction. □

3. Upper bounds for fi(n)

We may now prove Proposition 1.7.
We begin with the bound for fI(n). By symmetry we may restrict attention to Type I solutions
(x, y, z) for which y ⩽ z. By Proposition 2.1 and Lemma 2.7, these solutions arise from sextuples
(a, b, c, d, e, f ) ∈ N6 ∩ ΣI
n obeying the Type I bounds in Lemma 2.7. In particular we see that

e · f · (cd)2 · ac = (acd)2( ce
b )( bf
a ) ≪ n3,

and so by the pigeonhole principle, at least one of e, f, cd, ac is O(n3/5).
Suppose ﬁrst that e ≪ n3/5. For ﬁxed e, we see from (2.1) and the divisor bound (A.6) that there
are nO( 1
log log n ) choices for a, b, d, giving a net total of n3/5+O( 1
log log n ) points in Σ
I
n in this case.
Similarly, if f ≪ n3/5, (2.7) and the divisor bound gives nO( 1
log log n ) choices for a, d for each f , giving
n3/5+O( 1
log log n ) solutions. If cd ≪ n3/5, one uses (2.9) and the divisor bound to get nO( 1
log log n ) choices
for b, f, c, d for each choice of cd, and if ak ≪ n3/5, then (2.8) and the divisor bound gives nO( 1
log log n )

choices for a, b, c, f for each ﬁxed ak. Putting all this together (and recalling that any three coordinates
in ΣI
n determine the other three) we obtain the ﬁrst part of Proposition 1.7.
Now we prove the bound for fII(n), which is similar. Again we may restrict attention to sextuples
(a, b, c, d, e, f ) ∈ N6 ∩ ΣII
n obeying the Type II bounds in Lemma 2.7. In particular we have

e2 · (ad) · (ac) · (cd) = (acde)
2 ⩽ n2

and so at least one of e, ad, ac, cd is O(n2/5).
If e ≪ n2/5, we use (2.13) and the divisor bound to get nO( 1
log log n ) choices for a, b, d for each e. If
ad ≪ n2/5, we use (2.19) and the divisor bound to get nO( 1
log log n ) choices for a, d, e, f for each ﬁxed
ad. If ac ≪ n2/5, we use (2.20) to get n
O( 1
log log n ) choices for a, c, b, f for each ﬁxed ac. If cd ≪ n
2/5,
we use (2.21) and the divisor bound to get nO( 1
log log n ) choices for b, c, d, f for each ﬁxed cd. Putting all
this together we obtain the second part of Proposition 1.7.

Remark 3.1. This argument, together with the fact that a large number n can be factorised in expected
O(no(1)) time (using, say, the quadratic sieve [49]), gives an algorithm to ﬁnd all Type I solutions for
a given n in expected time O(n3/5+o(1)), and a algorithm to ﬁnd all the Type II solutions in expected
run time O(n2/5+o(1)).
 4. Insolvability for odd squares

We now prove Proposition 1.6. Suppose for contradiction that n is an odd perfect square (in
particular, n = 1 mod 8) with a Type I solution. Then by Proposition 2.1, we can ﬁnd an N-point
(a, b, c, d, e, f ) in Σ
I
n.
Let q be the largest odd factor of ab. From (2.1) we have ne + 1 = 0 mod q. Since n is a perfect
square, we conclude that   e
q
   =   −1
q
   = (−1)(q−1)/4

thanks to (A.8). Since n = 1 mod 8, we see from (2.1) that e = 3 mod 4. By quadratic reciprocity
(A.7) we thus have   q
e
   = 1.

COUNTING THE NUMBER OF SOLUTIONS TO THE ERD ˝OS-STRAUS EQUATION ON UNIT FRACTIONS 15

On the other hand, from (2.2) we see that ab = −a
2 mod e, and thus
  ab
e
   =   −1
e
   = −1

by (A.8). This forces ab ̸= q, and so (by deﬁnition of q) ab is even. By (2.1), this forces e = 7 mod 8,
which by (A.9) implies that   2
e   = 1 and thus   q
e   =   ab
e   , a contradiction.
The proof in the Type II case is almost identical, using (2.13), (2.14) in place of (2.1), (2.2); we
omit the details.
 5. Lower bounds I

Now we prove the lower bounds in Theorem 1.1.
We begin with the lower bound

(5.1) X

n⩽N fII(n) ≫ N log3 N.

Suppose a, c, d, e are natural numbers with d square-free, e coprime to ad, e > a, and acde ⩽ N/4.
Then the quantity

(5.2) n := 4acde − e − 4a
2d

is a natural number of size at most N , and (a, ce − a, c, d, e, 4acd − 1) is an N-point of Σ
II
n . Applying
πII
n , we obtain a solution (x, y, z) = (a(ce − a)d, acdn, (ce − a)cdn)
to (1.1). We claim that this is a Type II solution, or equivalently that a(ce − a)d is coprime to n. As
e is coprime to ad, we see from (5.2) that n is coprime to ade, so it suﬃces to show that n is coprime
to b := ce − a. But if q is a common factor of both n and b, then from the identity (2.20) (with
f = 4acd − 1) we see that q is also a common factor of a, a contradiction. Thus we have obtained
a Type II solution. Also, as d is square-free, any two quadruples (a, c, d, e) will generate diﬀerent
solutions
9, as the associated sextuples (a, ce − a, c, d, e, 4acd − 1) cannot be related to each other by the
dilation (2.10). Thus, it will suﬃce to show that there are ≫ N log3 N quadruples (a, c, d, e) ∈ N with
d square-free, e coprime to ad, e > a, and acde ⩽ N/4. Restricting a, c, d to be at most N 0.1 (say), we
see that the number of possible choices of e is ≫ N
acd φ(ad)
ad , where φ is the Euler totient function. It
thus suﬃces to show that X

a,c,d⩽N 0.1 µ
2(d) φ(ad)
ad 1
adc ≫ log3 N,

where µ is the M¨obius function (so µ
2(d) = 1 exactly when d is square-free). Using the elementary
estimate φ(ad) ⩾ φ(a)φ(d) and factorising, we see that it suﬃces to show that

(5.3) X

d⩽N 0.1
 µ(d)2φ(d)
d2 ≫ log N.

But this follows from Lemma A.1.
Now we prove the lower bound X

n⩽N fI(n) ≫ N log3 N,

which follows by a similar method.

9Note the slight diﬀerence between the approach here and the approach given by Proposition 2.5, in that we use a
squarefree hypothesis on d to force the injectivity of the parameterisation, whereas in Proposition 2.5 it is the coprimality
of the a, b, c that is the primary source of injectivity. The reason for this change is that squarefree-ness is an easier
constraint to deal with than coprimality for the purposes of obtaining asymptotics. However, this trick is only available
for lower bounds and not for upper bounds, as not all Type II solutions can be associated with a squarefree d. We will
generalise this trick to sums of more than three fractions in Section 11 below.

16 CHRISTIAN ELSHOLTZ AND TERENCE TAO

Suppose a, c, d, f are natural numbers with d square-free, f dividing 4a
2d + 1 and coprime to c,
d ⩾ f , and acd ⩽ N/4. Then the quantity

(5.4) n := 4acd − f

is a natural number which is at most N , and (a, b, c, d, 4a2d+1
f , f ) is an N-point of Σ
I
n, where

b := c 4a
2d + 1
f − e = na + c
f .

Applying πI
n, this gives a solution
 (x, y, z) = (abdn, acd, bcd)

to (1.1), and as before the square-free nature of d ensures that each quadruple (a, c, d, f ) gives a diﬀerent
solution. We claim that this is a Type I solution, i.e. that abcd is coprime to n. As f divides 4a2d + 1,
f and with (5.4) also n is coprime to ad. As f and c are coprime by assumption, n is coprime to acd
by (5.4). As b = (na + c)/f , we conclude that n is also coprime to b.
Thus it will suﬃce to show that there are ≫ N log3 N quadruples (a, c, d, f ) ∈ N4 with f coprime
to 2ac, and d square-free with f dividing 4a
2d + 1, d ⩾ f , and acd ⩽ N/4.
We restrict a, c, f to be at most N 0.1. If f is coprime to 2ac, then there is a unique primitive residue
class of f such that 4a
2d + 1 is a multiple of f for all d in this class. Also, there are ≫ N
acf elements
d of this residue class with d ⩾ f and acd ⩽ N/4; a standard sieving argument shows that a positive
proportion of these elements are square-free. Thus, we have a lower bound of
X

a,c,f ⩽N 0.1:(f,2ac)=1
 N
acf

for the number of quadruples. Restricting f to be odd and then using the crude sieve

(5.5) 1(f,2ac)=1 ⩾ 1 − X
 p 1p|f 1p|a − X
 p 1p|f 1p|c

where p ranges over odd primes, one easily veriﬁes that the above expression is ≫ N log3 N , and the
claim follows.
Now we establish the lower bound X

p⩽N fII(p) ≫ N log2 N.

We will repeat the proof of (5.1), but because we are now counting primes instead of natural numbers
we will need to invoke the Bombieri-Vinogradov inequality at a key juncture.
Suppose a, c, d, e are natural numbers with d square-free, a, c, d ⩽ N 0.1, and e between N 0.6 and
N/4acd with

(5.6) p := 4acde − e − 4a
2d

prime. Then p is at most N and at least N 0.6, and in particular is automatically coprime to ade (and
thus ce − a, by previous arguments). Thus, as before, each such (a, c, d, e) gives a Type II solution for
a prime p ⩽ N , with diﬀerent quadruples giving diﬀerent solutions. Thus it suﬃces to show that there
are ≫ N log2 N quadruples (a, c, d, e) with the above properties.
Fix a, c, d. As e ranges from N 0.6 to N/4acd, the expression (5.6) traces out a primitive residue
class modulo 4acd − 1, omitting at most O(N 0.6) members of this class that are less than N . Thus,
the number of primes of the form (5.6) for ﬁxed acd is

π(N ; 4acd − 1, −4a
2d) − O(N 0.6),

COUNTING THE NUMBER OF SOLUTIONS TO THE ERD ˝OS-STRAUS EQUATION ON UNIT FRACTIONS 17

where π(N ; q, t) denotes the number of primes p < N that are congruent to t mod q. We replace
π(N ; 4acd − 1, −4a2d) by a good approximation, and bound the error. If we set

D(N ; q) := max
(a,q)=1
      π(N ; q, a) − li(N )
φ(q)
     

(as in (A.13)), where li(x) := R x
0 dt
log t is the logarithmic integral, the number of primes of the form (5.6)
for ﬁxed acd is at least li(N )
φ(4acd − 1) − D(N ; 4acd − 1) − O(N 0.6)

The overall contribution of those acd combinations referring to the O(N 0.6) error term is at most
O((N 0.1)3N 0.6) = o(N log2 N ), while li(N ) is comparable to N/ log N , so it will suﬃce to show the
lower bound

(5.7) X

a,c,d⩽N 0.1
 µ
2(d)
φ(4acd − 1) ≫ log3 N

and the upper bound

(5.8) X

a,c,d⩽N 0.1 D(N ; 4acd − 1) = o(N log2 N ).

We ﬁrst prove (5.7). Using the trivial bound φ(4acd − 1) ⩽ 4acd, it suﬃces to show that
X

a,c,d⩽N 0.1
 µ
2(d)
acd ≫ log3 N

which upon factorising reduces to showing
X

d⩽N 0.1
 µ
2(d)
d ≫ log N.

But this follows from Lemma A.1.
Now we show (5.8). Writing q := 4acd−1, we can upper bound the left-hand side of (5.8) somewhat
crudely by X

q⩽N 0.3 D(N ; q)τ (q + 1)2.

From divisor moment estimates (see (A.4)) we have
X

q⩽N 0.3
 τ (q + 1)4

q ≪ logO(1) N ;

hence by Cauchy-Schwarz, we may bound the preceding quantity by

≪ logO(1) N
 0

@ X

q⩽N 0.3 qD(N ; q)
2
1

A
 1/2
 .

Using the trivial bound D(N ; q) ≪ N/q, we bound this in turn by

≪ N 1/2 logO(1) N
 0

@ X

q⩽N 0.3 D(N ; q)

1

A
 1/2
 .

But from the Bombieri-Vinogradov inequality (A.14), we have
X

q⩽N 0.3 D(N ; q) ≪A N log−A N

for any A > 0, and the claim (5.8) follows.

18 CHRISTIAN ELSHOLTZ AND TERENCE TAO

Finally, we establish the lower bound
X

p⩽N fI(p) ≫ N log2 N.

Unsurprisingly, we will repeat many of the arguments from preceding cases. Suppose a, c, d, f are
natural numbers with a, c, f ⩽ N 0.1 with (a, c) = (2ac, f ) = 1, N 0.6 ⩽ d ⩽ N/4ac, such that f divides
4a2d + 1, and the quantity

(5.9) p := 4acd − f

is prime. Then p is at most N and is at least N 0.4, and in particular is coprime to a, c, f ; from (5.9) it
is coprime to d also. This thus yields a Type I solution for p; by the coprimality of a, c, these solutions
are all distinct as no two of the associated sextuples (a, b, c, d, 4a2d+1
f , f ) can be related by (2.10). Thus
it suﬃces to show that there are ≫ N log2 N quadruples (a, c, d, f ) with the above properties.
For ﬁxed a, c, f , the parameter d traverses a primitive congruence class modulo f , and p = 4acd − f
traverses a primitive congruence class modulo 4acf , that omits at most O(N 0.6) of the elements of this
class that are less than N . By (A.13), the total number of d that thus give a prime p for ﬁxed acf is
at least li(N )
φ(4acf ) − D(N ; 4acf ) − O(N 0.6)

and so by arguing as before it suﬃces to show the bounds
X

a,c,f ⩽N 0.1 1(a,c)=(2ac,f )=1 1
φ(4acf ) ≫ log3 N

and X

a,c,f ⩽N 0.1 D(N ; 4acf ) = o(N log2 N ).

But this is proven by a simple modiﬁcation of the arguments used to establish (5.8), (5.7) (the con-
straints (a, c) = (2ac, f ) = 1 being easily handled by an elementary sieve such as (5.5)). This concludes
all the lower bounds for Theorem 1.1.
 6. Lower bounds II

Here we prove Theorem 1.8.

Proof. For any natural numbers m, n, let g2(m, n) denote the number of solutions (x, y) ∈ N2 to the
Diophantine equation m
n = 1
x + 1
y . Since

1
x + 1
y = 1
x + 1
2y + 1
2y

we conclude the crude bound f (n) ⩾ g2(4, n) for any n.
In [7, Theorem 1] it was shown that g2(m, n) ≫ 3
s whenever n is the product of s distinct primes
congruent to −1 mod m. Since g2(kn) ⩾ g2(n) for any k, we conclude that

(6.1) f (n) ⩾ g2(4, n) ⩾ 3
w4(n)

2
for all n, where wm(n) is the number of distinct prime factors of n that are congruent to −1 mod m.
Now we prove the ﬁrst part of the theorem. Let s be a large number, and let n be the product of
the ﬁrst s primes equal to −1 mod 4, then from the prime number theorem in arithmetic progressions
we have log n = (1 + o(1))s log s, and thus s = (1 + o(1)) log n
log log n . From (6.1) we then have

f (n) ≫ exp   log 3(1 + o(1)) log n
log log n
   .

Letting s → ∞ we obtain the claim.

COUNTING THE NUMBER OF SOLUTIONS TO THE ERD ˝OS-STRAUS EQUATION ON UNIT FRACTIONS 19

For the second part of the theorem, we use the Tur´an-Kubilius inequality (Lemma A.2) to the
additive function w4. This inequality gives that
X

n⩽N |w4(n) − 1
2 log log N |2 ≪ N log log N.

From this and Chebyshev’s inequality (see also [71, p. 307]), we see that

w4(n) ⩾ 1
2 log log n + O(ξ(n)
p log log n)

for all n in a density 1 subset of N. The claim then follows from (6.1).
Now we turn to the third part of the theorem. We ﬁrst deal with the case when p = 4t − 1 is prime,
then 4
p = 4
p + 1 + 1
t(4t − 1)
which in particular implies that f (p) ⩾ g2(4, p + 1)
and thus f (p) ≫ 3
w4(p+1).
By Lemma A.3 we know that

(6.2) w4(p + 1) ⩾   1
2 − o(1)
  log log p

a set of primes of relative prime density 1.
It remains to deal with those primes p congruent to 1 mod 4. Writing
4
p = 1
(p + 3)/4 + 3
p(p + 3)/4
we see that f (p) ⩾ g2(3, p(p + 3)/4) ≫ 3
w3((p+3)/4) ≫ 3
w3(p+3).
It thus suﬃces to show that
 w3(p + 3) ⩾   1
2 − o(1)
  log log p

for all p in a set of primes of relative density 1. But this can be established by the same techniques
used to establish (6.2). □

7. Sums of divisor functions

Let P : Z → Z be a polynomial with integer coeﬃcients, which for simplicity we will assume to be
non-negative, and consider the sum X

n⩽N τ (P (n)).

In [15], Erd˝os established the bounds

(7.1) N log N ≪P X

n⩽N τ (P (n)) ≪P N log N

for all N > 1 and for P irreducible; note that the implied constants here can depend on both the degree
and the coeﬃcients of P . This is of course consistent with the heuristic τ (n) ∼ log n “on average”. Of
course, the irreducibility hypothesis is necessary as otherwise P (n) would be expected to have many
more divisors.
In this section we establish a reﬁnement of the Erd˝os upper bound that gives a more precise
description of the dependence of the implied constant on P (and with irreducibility replaced by a much
weaker hypothesis), which may be of some independent interest:

20 CHRISTIAN ELSHOLTZ AND TERENCE TAO

Theorem 7.1 (Erd˝os-type bound). Let N > 1, let P be a polynomial with degree D and coeﬃcients
being non-negative integers of magnitude at most N l. For any natural number m, let ρ(m) be the
number of roots of P mod m in Z/mZ, and suppose one has the bound

(7.2) ρ(pj) ⩽ C

for all primes p and all j ⩾ 1. Then

N X

m⩽N
 ρ(m)
m ≪ X

n⩽N τ (P (n)) ≪D,l,C N X

m⩽N
 ρ(m)
m .

Remark 7.2. For any ﬁxed P , one has (7.2) for some C = CP (by many applications
10 of Hensel’s
lemma, and treating the case of small p separately), and when P is irreducible one can use tools such
as Landau’s prime ideal theorem to show that P
 m⩽N ρ(m)
m ≪P log N (indeed, much more precise
asymptotics are available here). Thus we see that Erd˝os’ original result (7.1) is a corollary of Theo-
rem 7.1. For special types of P (e.g. linear or quadratic polynomials), more precise asymptotics onP
 n⩽N τ (P (n)) are known (see e.g. [17], [18] for the linear case, and [25], [61], [36], [37], [38] for the
quadratic case), but the methods used are less elementary (e.g. Kloosterman sum bounds in the linear
case, and class ﬁeld theory in the quadratic case), and do not cover all ranges of coeﬃcients of P for
the applications to the Erd¨os-Straus conjecture.

Proof. Our argument will be based on the methods in [15]. In this proof all implied constants will be
allowed to depend on D, l and C.
We begin with the lower bound, which is very easy. Clearly

(7.3) τ (P (n)) ⩾ X

m⩽N :m|P (n) 1

and thus X

n⩽N τ (P (n)) ⩾ X

m⩽N
 X

n⩽N :m|P (n) 1.

The expression P (n) mod m is periodic in n with period m, and thus for m ⩽ N one has

(7.4) N ρ(m)
m ≪ X

n⩽N :m|P (n) 1 ≪ N ρ(m)
m

which gives the lower bound on P
 n⩽N τ (P (n)).
Now we turn to the upper bound, which is more diﬃcult. We ﬁrst establish a preliminary bound

(7.5) X

n⩽N τ (P (n))
2 ≪ N logO(1) N

using an argument of Landreau [33]. Let n ⩽ N . By the coeﬃcient bounds on P we have

(7.6) P (n) ≪ N O(1).

Using the main lemma from [33], we conclude that

τ (P (n))2 ≪ X

m⩽N :m|P (n) τ (m)
O(1)

10See [69] for more precise bounds on C in terms of quantities such as the discriminant ∆(P ) of P ; bounds of this
type go back to Nagell [40] and Ore [48] (see also [58], [27]). One should in fact be able to establish a version of Theorem
7.1 in which the implied constant depends explicitly on the ∆(P ) rather than on C by using the estimates of Henriot
[24] (which build upon earlier work of Barban-Vehov [2], Daniel [10], Shiu [64], Nair [41], and Nair-Tenenbaum [42]), but
we will not do so here, as we will need to apply this bound in a situation in which the discriminant may be large, but
for which the bound C in (7.2) can still be taken to be small.

COUNTING THE NUMBER OF SOLUTIONS TO THE ERD ˝OS-STRAUS EQUATION ON UNIT FRACTIONS 21

and thus X

n⩽N τ (P (n))2 ≪ X

m⩽N τ (m)
O(1) X

n⩽N :m|P (n) 1.

Using (7.2), we may crudely bound P
 n⩽N :m|P (n) 1 ⩽ τ (m)
O(1), thus
X

n⩽N τ (P (n))2 ≪ X

m⩽N τ (m)O(1)

and the claim then follows from Lemma A.1.
In view of (7.5) and the Cauchy-Schwarz inequality, we may discard from the n summation any
subset of {1, . . . , N } of cardinality at most N log−C′ N for suﬃciently large C ′. We will take advantage
of this freedom in the sequel.
Suppose for the moment that we could reverse (7.3) and obtain the bound

(7.7) τ (P (n)) ≪ X

m⩽N :m|P (n) 1.

Combining this with (7.4), we would obtain
X

n⩽N τ (P (n)) ≪ X

m⩽N
 X

n⩽N :m|P (n) 1

≪ X

m⩽N
 N
m ρ(m)

which would give the theorem. Unfortunately, while (7.7) is certainly true when P (n) ⩽ N 2, it can fail
for larger values of P (n), and from the coeﬃcient bounds on P we only have the weaker upper bound
(7.6).
Nevertheless, as observed by Erd˝os, we have the following substitute for (7.7):

Lemma 7.3. Let C ′ be a ﬁxed constant. For all but at most O(N log−C′ N ) values of n in the range
1 ⩽ n ⩽ N , either (7.7) holds, or one has

τ (P (n)) ≪ O(1)
r X

m∈Sr:m|P (n) 1

for some 2 ⩽ r ≪ (log log N )
2, where Sr is the set of all m with the following properties:
• m lies between N 1/4 and N .
• m is N 1/r-smooth (i.e. m is divisible by any prime larger than N 1/r).
• m has at most (log log N )2 prime factors.
• m is not divisible by any prime power p
k with p ⩽ N 1/2, k > 1, and pk ⩾ N 1/8(log log N )2.

The point here is that the exponential loss in the O(1)r factor will be more than compensated for by
the N 1/r-smooth requirement, which as we shall see gains a factor of r−cr for some absolute constant
c > 0.

Proof. The claim follows from (7.7) when P (n) ⩽ N 2, so we may assume that P (n) > N 2.
We factorise P (n) as P (n) = p1 . . . pJ
where the primes p1 ⩽ . . . ⩽ pJ are arranged in non-decreasing order. Let 0 ⩽ j < J be the largest
integer such that p1 . . . pj ⩽ N . If j = 0 then all prime factors of P (n) are greater than N , and thus
by (7.6) we have J = O(1) and thus τ (P (n)) = O(1), which makes the claim (7.7) trivial. Thus we
may assume that j ⩾ 1.
Suppose ﬁrst that all the primes pj+1, . . . , pJ have size at least N 1/2. Then from (7.6) we in fact
have J = j + O(1), and so τ (P (n)) ≪ τ (p1 . . . pj).

22 CHRISTIAN ELSHOLTZ AND TERENCE TAO

Note that every factor of p1 . . . pj divides P (n) and is at most N , which gives (7.7). Thus we may
assume that pj+1, in particular, is less than N 1/2, which forces

(7.8) N 1/2 < p1 . . . pj ⩽ N

and pj < N 1/2.
Following [15], we eliminate some small exceptional sets of natural numbers n. First we consider
those n for which P (n) has at least (log log N )
2 distinct prime factors. For such P (n), one has τ (P (n)) ⩾
2
(log log N )
2, which is asymptotically larger than any given power of log N ; thus by (7.5), the set of such
n has size at most O(N log−C′ N ) and can be discarded.
Next, we consider those n for which P (n) is divisible by a prime power pk with p ⩽ N 1/2, k > 1,
and pk ⩾ N 1/8(log log N )
2. By reducing k if necessary we may assume that p
k ⩽ N . For each p and k,
there are at most O( N
pk ρ(p
k)) = O( N
pk ) numbers n with P (n) divisible by pk, thanks to (7.2); thus the
total number of such n is bounded by

≪ N X

p⩽N 1/2
 X

j⩾2:pj ⩾N 1/8(log log N )2
 1
pj

which can easily be computed to be O(N log−C′ N ). Thus we may discard all n of this type.
After removing all such n, we must have pj > N 1/8(log log N )2. Indeed, after eliminating the ex-
ceptional n as above, p1 . . . pj is the product of at most (log log N )
2 prime powers, each of which is
bounded by N 1/8(log log N )
2 , or is a single prime larger than N 1/8(log log N )
2 . The former possibility thus
contributes at most N 1/8 to the ﬁnal product p1 . . . pj; from (7.8) we conclude that the latter possibility
must occur at least once, and the claim follows.
Let r be the positive integer such that

N 1/(r+1) < pj ⩽ N 1/r,

then 2 ⩽ r ≪ (log log N )
2. The primes pj+1, . . . , pJ have size at least N 1/(r+1), so by (7.6) we have
J = j + O(r), which implies that
 τ (P (n)) ≪ O(1)
rτ (p1 . . . pj).

As p1 . . . pj is at least N 1/2, we have

τ (p1 . . . pj) ⩽ 2 X

m|p1...pj ;m⩾N 1/4 1.

Note that all m in the above summand lie in Sr and divide P (n). The claim follows. □

Invoking the above lemma, it remains to bound

X

m⩽N
 X

n⩽N :m|P (n) 1 +
 O((log log N )2)X
r=2 O(1)
r X

m∈Sr
 X

n⩽N :m|P (n) 1.

by O(N P
 n⩽N P (m)
m ). The ﬁrst term was already shown to be acceptable by (7.4). For the second
sum, we also apply (7.4) and bound it by

(7.9) ≪ N
 O((log log N )
2)X
r=2 O(1)
r X

m∈Sr
 ρ(m)
m .

To estimate this expression, let r, m be as in the above summation, and factor m into primes. As in
the proof of Lemma 7.3, the contribution to m coming from primes less than N 1/8(log log N )
2 is at most
N 1/8, and the primes larger than N 1/8(log log N )2 that divide m are distinct. Hence, by the pigeonhole
principle (as in [15]), there exists t ⩾ 1 with r2
t ≪ (log log N )
2 such that the N 1/r-smooth number
m has at least ⌊ rt
100 ⌋ distinct prime factors between N 1/2
t+1r and N 1/2
tr, and can thus be factored as

COUNTING THE NUMBER OF SOLUTIONS TO THE ERD ˝OS-STRAUS EQUATION ON UNIT FRACTIONS 23

m = q1 . . . q⌊ rt
100 ⌋u where q1 < . . . < q⌊ rt
100 ⌋ are primes between N 1/2t+1r and N 1/2tr, and u is an integer
of size at most N . From the Chinese remainder theorem and (7.2) we have the crude bound

ρ(m) ≪ O(1)
rtρ(u)

and thus
 X

m∈Sr
 ρ(m)
m ≪
 ∞X
t=1 O(1)
rt 1
⌊ rt
100 ⌋!
 0

@ X

N 1/2t+1r⩽p⩽N 1/2tr
 1
p
 1

A
 ⌊ rt
100 ⌋ X

u⩽N
 ρ(u)
u .

By the standard asymptotic P
 p<x 1
p = log log x + O(1), we have
X

N 1/2t+1r⩽p⩽N 1/2tr
 1
p = O(1);

putting this all together, we can bound (7.9) by

≪
   ∞X
r=2
 ∞X
t=1
 O(1)
rt

⌊ rt
100 ⌋!
 ! X

m⩽N
 ρ(m)
m

and the claim follows. □

We isolate a simple special case of Theorem 7.1, when the polynomial P is linear:

Corollary 7.4. If a, b, N are natural numbers with a, b ≪ N O(1), then
X

n⩽N τ (an + b) ≪ τ ((a, b))N log N

where (a, b) is the greatest common divisor of a and b.

Proof. By the elementary inequality τ (nm) ⩽ τ (n)τ (m) we may factor out (a, b) and assume without
loss of generality that a, b are coprime.
We apply Theorem 7.1 with P (n) := an + b. From the coprimality of a, b and elementary modular
arithmetic, we see that ρ(m) ⩽ 1 for all m, and the claim follows. □

We may now prove Proposition 1.4 from the introduction.

Proof of Proposition 1.4. We divide into two cases, depending on whether A ⩾ B or A ⩽ B.
First suppose that A ⩾ B. From Corollary 7.4 we have
X

a⩽A τ (kab2 + 1) ≪ A X

m⩽A
 1
m ≪ A log A,

for each ﬁxed b ⩽ B, and the claim follows on summing in B. (Note that this argument in fact works
whenever A ⩾ Bε for any ﬁxed ε > 0.)
Now suppose that A ⩽ B. For each ﬁxed a ∈ A, we apply Theorem 7.1 to the polynomial Pka(b) :=
kab2 + 1. To do this we ﬁrst must obtain a bound on ρka(pj), where ρka(m) is the number of solutions
b mod m to kab2 + 1 = 0 mod m. Clearly ρka(m) vanishes whenever m is not coprime to ka, so it
suﬃces to consider ρka(pj) when p does not divide ka. Then Pka is quadratic, and a simple application
of Hensel’s lemma reveals that ρka(pj) ⩽ 2 for all prime powers pj (the case p = 2, as usual, has to be
treated separately). We may therefore apply Theorem 7.1 and conclude that
X

b⩽B τ (kab2 + 1) ≪ B X

m⩽B
 ρka(m)
m .

It thus suﬃces to show that

(7.10) X

a⩽A
 X

m⩽B
 ρka(m)
m ≪ A log B log(1 + k).

24 CHRISTIAN ELSHOLTZ AND TERENCE TAO

To control ρka(m), the obvious tool to use here is the quadratic reciprocity law (A.7). To apply this
law, it is of course convenient to ﬁrst reduce to the case when a and m are odd. If m = 2
jm′ for some
odd m
′, then ρka(m) ≪ ρka(m
′), and from this it is easy to see that the bound (7.10) follows from the
same bound with m restricted to be odd. Similarly, by splitting a = 2
la
′ and absorbing the 2l factor
into k (and dividing A by 2
l to compensate), we may assume without loss of generality that a is odd.
As previously observed, ρka(m) vanishes unless ka and m are coprime, so we may also restrict to
the case (ka, m) = 1, where (n, m) denotes the greatest common divisor of n, m. If p is an odd prime
not dividing ka, then from elementary manipulation and Hensel’s lemma we see that

ρka(p
j) = ρka(p) ⩽ 1 +   −ka
p
   ,

and thus for odd m coprime to ka we have

ρka(m) ⩽ Y

p|m
   1 +   −ka
p
    .

For odd m, not necessarily coprime to ka, we thus have

ρka(m) ⩽ Y

p|m;(p,2ka)=1
   1 +   −ka
p
    .

using the multiplicativity properties of the Jacobi symbol, one has

1 +   −ka
p
   ⩽ X

j:pj |m
   −ka
pj
  

whenever p|m and (p, 2ka) = 1, and thus

ρka(m) ⩽ Y

p|m;(p,2ka)=1
 X

j:pj |m
   −ka
pj
   .

The right-hand side can be expanded as X

q|m;(q,2ka)=1
   −ka
q
   .

We can thus bound the left-hand side of (7.10) by
X

q⩽B:(q,2k)=1
 X

a⩽A;(a,2q)=1
   −ka
q
   X

m⩽B;q|m
 1
m .

The ﬁnal sum is of course log B
q
q + O( 1
q ). The contribution of the error term is bounded by

O( X

q⩽B
 X

a⩽A
 1
q ) = O(A log B)

which is acceptable, so it suﬃces to show that

(7.11)
       
 X

q⩽B:(q,2k)=1
 X

a⩽A;(a,2q)=1
   −ka
q
   log B
q
q
        ≪ A log B log(1 + k).

We ﬁrst dispose of an easy contribution, when q is less than A. The expression a ↦→   −ka
q   1(a,2q)=1 is

periodic with period 2q and sums to zero (being essentially a quadratic character on Z/2qZ), and so11

11One could obtain better estimates and deal with somewhat larger q here by using tools such as the Polya-Vinogradov
inequality, but we will not need to do so here. Similarly for the treatment of the regime A ⩽ q ⩽ kA.

COUNTING THE NUMBER OF SOLUTIONS TO THE ERD ˝OS-STRAUS EQUATION ON UNIT FRACTIONS 25

in this case we have X

a⩽A;(a,2q)=1
   −ka
q
   = O(q).

Thus the contribution of this case is bounded by

O
 0

@ X

q⩽A q log B
q
q
 1

A = O(A log B)

which is acceptable.
Next, we deal with the contribution when q is between A and kA. Here we crudely bound the
Jacobi symbol in magnitude by 1 and obtain a bound of

O( X

A⩽q⩽kA
 X

a⩽A
 log B
q ) = O(A log B log(1 + k))

which is acceptable.
Finally, we deal with the case when q exceeds kA. We write k = 2mk′ where k′ is odd, then from
quadratic reciprocity (A.7) (and (A.8), (A.9)) we have
  −ka
q
   = c(q)   q
k′a
  

where c(q) := (−1)(q−1)/2+m(q2−1)/8 is periodic with period 8. We can thus rewrite this contribution
to (7.11) as       
 X

a⩽A;(a,2)=1
 X

kA⩽q⩽B:(q,2ak)=1 c(q)   q
k′a
   log B
q
q
        .

For any ﬁxed a in the above sum, the expression q ↦→ c(q)   q
k′a   1(q,2ak)=1 is periodic with period
8k′a = O(kA), is bounded in magnitude by 1 and has mean zero. A summation by parts then gives
      
 X

kA⩽q⩽B:(q,2ak)=1 c(q)   q
k′a
   log B
q
q
        ≪ log B

and so on summing in A we see that this contribution is acceptable. This concludes the proof of the
proposition. □

We now record some variants of Proposition 1.4 that will also be useful in our applications.

Proposition 7.5 (Average value of τ3(ab + 1)). For any A, B > 1, one has

(7.12) X

a⩽A
 X

b⩽B τ3(ab + 1) ≪ AB log2(A + B).

Proof. By symmetry we may assume that A ⩽ B, so that ab ≪ B2 for all a ⩽ A and b ⩽ B. For any
n, τ3 is the number of ways to represent n as the product n = d1d2d3 of three terms. One of these
terms must be at most n1/3, and so
 τ3(n) ≪ X

d|n:d⩽n1/3 τ ( n
d ).

We can thus bound the left-hand side of (7.12) by

≪ X

d≪B2/3
 X

a⩽A
 X

b⩽B:d|ab+1 τ ( ab + 1
d ).

26 CHRISTIAN ELSHOLTZ AND TERENCE TAO

Note that for ﬁxed a, d, the constraint d|ab + 1 is only possible if a is coprime to d, and restricts b to
some primitive residue class q mod d for some q = qa,d between 1 and d. Writing b = cd + q, we can
thus bound the above expression by
≪ X

d≪B2/3
 X

a⩽A
 X

c≪B/d τ (ac + r)

where r = ra,d := aq+1
d . Note that r is clearly coprime to a. Thus by Corollary 7.4, we may bound the
preceding expression by
 ≪ X

d≪B2/3
 X

a⩽A
 B
d log B

which is O(AB log2 B). The claim follows. □

Proposition 7.6 (Average value of τ (ab + cd)). For any A, B, C, D > 1, one has

(7.13) X

a⩽A,b⩽B,c⩽C,d⩽D:(a,b,c,d)=1 τ (ab + cd) ≪ ABCD log(A + B + C + D).

Proof. By symmetry we may assume that A, B, C ⩽ D. Then for ﬁxed a, b, c coprime, we have
X

d⩽D τ (abcd) ≪ D log D

by Corollary 7.4, and the claim follows by summing in a, b, c, d. □

Remark 7.7. Informally, one can view the above propositions as asserting that the heuristics τ (n) ≪
log n, τ3(n) ≪ log2 n are valid on average (in a ﬁrst moment sense) on the range of various polynomial
forms in several variables.

8. Upper bound for P
 n⩽N fI(n) and P
 p⩽N fI(p)

Now that we have established Proposition 1.4, we can obtain upper bounds on sums of fI.
We begin with the bound X

n⩽N fI(n) ≪ N log3 N.

By Proposition 2.1 and symmetry followed by Lemma 2.7, it suﬃces to show that there are at most
O(N log3 N ) septuples (a, b, c, d, e, f, n) ∈ N7 obeying (2.1)-(2.9) and the Type I estimates from Lemma
2.7. In particular, acd ≪ N , f is a factor of 4a
2d + 1, and n = 4acd − f . As a, c, d, f determine the
remaining components of the septuple, we may thus bound the number of such septuples as
X

a,c,d:acd≪N τ (4a
2d + 1).

Dividing a, c, d into dyadic blocks (A/2 ⩽ a ⩽ A, etc.) and applying Proposition 1.4 (with k = 4) to
each block, we obtain the desired bound O(N log3 N ).
Now we establish the bound X

p⩽N fI(p) ≪ N log2 N log log N.

As before, it suﬃces to count quadruples (a, c, d, f ) with acd ≪ N , and f a factor of 4a
2d + 1; but now
we can restrict p = 4acd − f to be prime. Also, from Proposition 2.1 we may assume that p is coprime
to acd (and hence to 4acd, if we discard the prime p = 2).
Thus we may assume without loss of generality that −f mod 4ad is a primitive residue class. From
the Brun-Titchmarsh inequality (A.10), we conclude that for each ﬁxed a, d, f , there are O( N
φ(4ad) log(N/4ad) )
primes p in this residue class that are less than N if ad ⩽ N/100 (say); if instead ad > N/100, then

COUNTING THE NUMBER OF SOLUTIONS TO THE ERD ˝OS-STRAUS EQUATION ON UNIT FRACTIONS 27

we of course only have O(1) = O( N
φ(4ad) ) primes in this class. Thus, in any event, we can bound the
number of such primes as O( N
φ(4ad) log(2+N/ad) ). We therefore have the bound

(8.1) X

p⩽N fI(p) ≪ X

a,d:ad≪N τ (4a
2d + 1) N
φ(4ad) log(2 + N/ad) .

By dyadic decomposition (and bounding φ(4ad) ⩾ φ(ad)), it thus suﬃces to show that

(8.2) X

a,d:N/2⩽ad⩽N
 τ (4a
2d + 1)
φ(ad) ≪ log2 N.

Indeed, assuming this bound for all N , we can bound the right-hand side of (8.1) by

O(log N )X
j=1
 N log2 N
j ≪ N log2 N log log N

and the claim follows.
To prove (8.2), we would like to again apply Proposition 1.4, but we must ﬁrst deal with the φ(ad)
denominator. From (A.12) one has 1
φ(ad) ≪ 1
ad
 X
 s|a
 X
 t|d
 1
st .

Writing a = sa
′, d = td
′, we may thus bound the left-hand side of (8.2) by

≪ 1
N
 X

s,t:st⩽N
 1
st
 X

a′,d′:a′d′⩽N/st τ (4s
2t(a′)
2d′ + 1).

Applying Proposition 1.4 to the inner sum (decomposed into dyadic blocks, and setting k = 4s
2t), we
see that X

a′,d′:a′d′⩽N/st τ (4s
2t(a
′)
2d
′ + 1) ≪ N
st log2 N
st log(1 + s
2t).

Inserting this bound and summing in s, t we obtain the claim.

9. Upper bound for P n⩽N fII(n) and P p⩽N fII(p)

Now we prove the upper bound X

n⩽N fII(n) ≪ N log3 N.

By Proposition 2.5 followed by Lemma 2.7 (and symmetry), it suﬃces to show that there are at most
O(N log3 N ) N-points (a, b, c, d, e, f ) that lie in ΣII
n for some n ⩽ N , which also obeys the Type II
bound acde ⩽ N in Lemma 2.7.
Observe from (2.13)-(2.21) that a, c, d, e determine the other variables b, f, n. Thus, it suﬃces to
show that there are ≪ N log3 N quadruples (a, b, d, e) ∈ N4 with acde ⩽ N . But this follows from
(A.2) with k = 4.
Finally, we prove the upper bound X

p⩽N fII(p) ≪ N log2 N.

By dyadic decomposition, it suﬃces to show that

(9.1) X

N/2⩽p⩽N fII(p) ≪ N log2 N.

As before, we can bound the left-hand side (up to constants) by the number of quadruples (a, c, d, e) ∈
N4 with acde ≪ N . However, by (2.16), we may also add the restriction that 4acde−4a
2d−e is a prime

28 CHRISTIAN ELSHOLTZ AND TERENCE TAO

between N/2 and N . Also, if we set b := ce − a, then by Lemma 2.7 we may also add the restrictions
a ⩽ b and b ⩾ ce/2, and from Proposition 2.5 we can also require that a, b be coprime. Since

(ade)(acd)(ab)
1/2 ≪ (ade)(acd)b

≪ (ade)(acd)(ce)

= (acde)2

≪ N 2

we see that one of the quantities ade, acd, ab must be at most ≪ N 4/5 (cf. Section 3). As we shall
soon see, the ability to take one of these quantities to be signiﬁcantly less than N allows us to avoid
the ineﬃciencies in the Brun-Titchmarsh inequality (A.10) that led to a double logarithmic loss in the
Type I case. (Unfortunately, it does not seem that a similar trick is available in the Type II case.)
Let us ﬁrst consider those quadruples with ade ≪ N 4/5, which is the easiest case. For ﬁxed a, d, e,
4acde − 4a
2d − e traverses (a possibly non-primitive) residue class modulo 4ade. As ade ≪ N 4/5, there
are no primes in this class that are at least N/2 if the class is not primitive. If it is primitive, we may
apply the Brun-Titchmarsh inequality (A.10) to bound the number of primes between N/2 and N in
this class by ≪ N
φ(4ade) log(N ) , noting that log(N/4ade) is comparable to log N . Thus, we can bound
this contribution to the left-hand side of (9.1) by

≪ N
log N
 X

a,d,e:ade≪N 4/5
 1
φ(4acd) ;

setting m := ade and bounding φ(4ade) ⩾ φ(ade), we can bound this in turn by

≪ N
log N
 X

m≪N 4/5
 τ3(m)
φ(m)

where τ3(m) := P
 a,d,e:ade=m 1. Applying Lemma A.1, we have

(9.2) X

m≪N 4/5
 τ3(m)
φ(m) ≪ log3 N,

and so this contribution is acceptable.
Now we consider the case acd ≪ N 4/5. Here, we rewrite 4acde−4a
2d−e as (4acd−1)e−4a2d, which
then traverses a (possibly non-primitive) residue class modulo 4acd−1. Applying the Brun-Titchmarsh
inequality as before, we may bound this contribution by

≪ N
log N
 X

a,c,d:acd≪N 4/5
 1
φ(4acd − 1)

and hence (setting m := 4acd − 1) by

≪ N
log N
 X

m≪N 4/5
 τ3(m + 1)
φ(m) ,

so that it suﬃces to establish the bound

(9.3) X

m≪N 4/5
 τ3(m + 1)
φ(m) ≪ log3 N.

This is superﬁcially similar to (9.2), but this time the summand is not multiplicative in m, and we can
no longer directly apply Lemma A.1. To deal with this, we apply (A.12) and bound (9.3) by

≪ X

m≪N 4/5
 X
d|m
 τ3(m + 1)
dm ;

COUNTING THE NUMBER OF SOLUTIONS TO THE ERD ˝OS-STRAUS EQUATION ON UNIT FRACTIONS 29

writing m = dn, we can rearrange this as

≪ X

d≪N 4/5
 1
d2 X

n≪N 4/5/d
 τ3(dn + 1)
n .

Applying dyadic decomposition of the d, n variables and using Proposition 7.5, we obtain (9.3) as
required.
Finally, we consider the case ab ≪ N 4/5. Here, we rewrite 4acde − 4a
2d − e as 4abd − e, and note
that e divides a + b = ce. If we ﬁx a, b, there are thus at most τ (a + b) choices for e (which also ﬁxes
c), and once one ﬁxes such a choice, 4abd − e traverses a (possibly non-primitive) residue class modulo
4ab. Applying the Brun-Titchmarsh inequality again, we may bound this contribution by

≪ N
log N
 X

a,b:ab≪N 4/5;(a,b)=1
 τ (a + b)
φ(4ab) .

Bounding φ(4ab) ⩾ φ(ab) and using (A.12), we can bound this by

≪ N
log N
 X

a,b:ab≪N 4/5;(a,b)=1
 X
 k|a
 X
 l|b
 τ (a + b)
abkl .

Writing a = km, b = ln, we may bound this by

≪ N
log N
 X

k,l,m,n:klmn≪N 4/5;(k,l,m,n)=1
 1
k2l2mn τ (km + ln).

Dyadically decomposing in k, l, m, n and using Proposition 7.6, we see that this contribution is also
O(N log2 N ). The proof of (9.1) (and thus Theorem 1.1) is now complete.

10. Solutions by polynomials

We now prove Proposition 1.9. We ﬁrst verify that each of the sets is solvable by polynomials (which
of course implies that any residue class contained in such classes are also solvable by polynomials). We
ﬁrst do this for the Type I sets. In view of the πI
n map (which clearly preserves polynomiality), it will
suﬃce to ﬁnd polynomials a = a(n), . . . , f = f (n) of n that take values in N for suﬃciently large n in
these sets, and such that (a(n), . . . , f (n)) ∈ ΣI
n for all n. This is achieved as follows:
• If n = −f mod 4ad, where a, d, f ∈ N are such that f |4a
2d + 1, then we take

(a, b, c, d, e, f ) :=   a, n + f
4ad e − a, n + f
4ad , d, e, 4a2d + 1
e
   .

• If n = −f mod 4ac and n = − c
a mod f , where a, c, f ∈ N are such that (4ac, f ) = 1, then
we take
 (a, b, c, d, e, f ) :=   a, na + c
f , c, n + f
4ac , na + af + c
f c , f   ;

note from the hypotheses that na + af + c is divisible by the coprime moduli f and c, and is
thus also divisible by f c.
• If n = −f mod 4cd and n2 = −4c
2d mod f , where c, d, f, q ∈ N are such that (4cd, f ) = 1,
then we take

(a, b, c, d, e, f ) :=   n + f
4cd , n2 + 4c2d + nf
4cdf , c, d, (n + f )
2 + 4c
2d
4c2df , f   ;

note from the hypotheses that (n + f )
2 + 4c
2d is divisible by the coprime moduli 4c2d and f ,
and is thus also divisible by 4c
2df .
• If n = − 1
e mod 4ab, where a, b, e ∈ N are such that e|a + b and (e, 4ab) = 1, then we take

(a, b, c, d, e, f ) :=   a, b, a + b
e , ne + 1
4ab , e, 4a a + b
e ne + 1
4ab − n 

30 CHRISTIAN ELSHOLTZ AND TERENCE TAO

One easily veriﬁes in each of these cases that one has an N-point of Σ
I
n for n large enough.
Now we turn to the Type II case. We use the same arguments as before, but using Σ
II
n in place of
ΣI
n of course:
• If n = −e mod 4ab, where a, b, e ∈ N are such that e|a + b and (e, 4ab) = 1, then we take

(a, b, c, d, e, f ) :=   a, b, a + b
e , n + e
4ab , e, a + b
e n + e
b − 1  .

• If n = −4a
2d mod f , where a, d, f ∈ N are such that 4ad|f + 1, then we take

(a, b, c, d, e, f ) :=   a, f + 1
4ad n + 4a
2d
f − a, f + 1
4ad , d, n + 4a
2d
f , f   .

• If n = −4a
2d − e mod 4ade, where a, d, e ∈ N are such that (4ad, e) = 1, then we take

(a, b, c, d, e, f ) :=   a, n + e
4ad , n + 4a
2d + e
4ade , d, e, n + 4a
2d
e
   .

Again, one easily veriﬁes in each of these cases that one has an N-point of Σ
II
n for n large enough.
Now we establish the converse claim. Suppose ﬁrst that we have a primitive residue class q mod r
that can be Type I solved by polynomials, and is maximal with respect to this property, then we have
4
p = 1
x + 1
y + 1
z

for all suﬃciently large primes p in this class, where x = x(p), y = y(p), z = z(p) are polynomials of p
that take natural number values for all large p in this class. For all suﬃciently large p, we either have
y(p) ⩽ z(p) for all p, or y(p) ⩾ z(p) for all p; by symmetry we may assume the latter.
Applying Proposition 2.1, we see that

(x, y, z) = (abdp, acd, bcd)

for some N-point (a, . . . , f ) = (a(p), . . . , f (p)) in ΣI
p with a(p), b(p), c(p) having no common factor. In
particular, d = d(p) is the least common multiple of x(p), y(p), z(p). Applying the Euclidean algorithm
to the polynomials x(p), y(p), z(p), we conclude that for suﬃciently large p in the primitive residue class,
d is also a polynomial in p, which divides the polynomials x, y, z. Dividing out by d and repeating these
arguments, we conclude that a = a(p), b = b(p), and c = c(p) are also polynomials in p for suﬃciently
large p in the primitive residue class. Applying the identities (2.1)-(2.9) we also see that e = e(p) and
f = f (p) are polynomials in p for suﬃciently large p.
From Lemma 2.7 we have a(p)c(p)d(p) = O(p) and f (p) = O(p) for all p, which implies that at
least two of the polynomials a(p), c(p), d(p) must be constant in p, and that f (p) has degree at most 1
in p. We now divide into several cases.
First suppose that a, d are independent of p. By (2.7) this forces e, f to be independent of p as well,
and f divides 4a
2d + 1. By (2.6) we have
 p = −f mod 4ad

for all suﬃciently large primes p = q mod r and thus (by Dirichlet’s theorem on primes12 in arithmetic
progressions) the primitive residue class q mod r is contained in the residue class −f mod 4ad, and
the claim follows in this case.
Now suppose that a, c are independent of p, and f has degree 0 (i.e. is also independent of p). Then
from (2.6) we have p = −f mod 4ac, and from (2.8) we have p = − c
a mod f ; since p is a large prime
this also forces (4ac, f ) = 1, and the claim follows.
Now suppose that a, c are independent of p, and f has degree p (and thus grows linearly in p). By
Lemma 2.7, b, e are then bounded and thus constant in p. From (2.2) we have e|a + b, and from (2.1)

12As noted in the introduction, one could avoid the use of Dirichlet’s theorem, and work instead with almost primes
or the proﬁnite topology instead.

COUNTING THE NUMBER OF SOLUTIONS TO THE ERD ˝OS-STRAUS EQUATION ON UNIT FRACTIONS 31

we have p = − 1
e mod 4ab. As p is an arbitrarily large prime, this forces (4ab, e) = 1, and the claim
follows.
Next, suppose that c, d are independent of p, and f has degree 0. Then from (2.6) one has p = −f
mod 4cd, which in particular forces (4cd, f ) = 1. From (2.9) one has p
2 = −4c2d mod f , and the
claim follows.
Finally, suppose that c, d are independent of p, and f has degree 1. By (2.9), f (p) divides p
2 + 4c2d
for all large primes p in the primitive residue class. Applying the Euclidean algorithm, we conclude
that f in fact divides p
2 + 4c
2d as a polynomial in p. But as c, d are positive, p
2 + 4c
2d is irreducible
over the reals, a contradiction. This concludes the treatment of the Type I case.
We now turn to the Type II case. Let q mod r be a residue class that is Type II solvable by
polynomials. Arguing as in the Type I case, we obtain a N-point (a, . . . , f ) = (a(p), . . . , f (p)) in Σ
II
p for
all suﬃciently large primes p in this class, and obeying the bounds in Lemma 2.7, with a(p), . . . , f (p)
all depending in a polynomial fashion on p.
From Lemma 2.7 we have a(p)c(p)d(p)e(p) = O(p), and so three of these polynomials a(p), c(p), d(p), e(p)
must be independent of p.
Suppose ﬁrst that a, c, e are independent of p. By (2.2), b is independent of p also, and e|a + b. By
(2.13), p = −e mod 4ab, and thus (e, 4ab) = 1, and the claim then follows from Dirichlet’s theorem.
Now suppose that a, c, d are independent of p. By (2.18), f is independent of p also, and 4ad|f + 1.
From (2.19) one has p = −4a
2d mod f , and the claim follows.
Next, suppose a, d, e are independent of p. By (2.16) one has p = −4a
2d − e mod 4ade, which
implies (4ad, e) = 1, and the claim follows.
Finally, suppose c, d, e are independent of p. By (2.14) this forces a, b to be bounded, and hence
also independent of p; and so this case is subsumed by the preceding cases.

11. Lower bounds III

11.1. Generation of solutions. We begin the proof of Theorem 1.11; the method of proof will be
a generalisation of that in Section 5. For the rest of this section, m and k are ﬁxed, and all implied
constants in asymptotic notation are allowed to depend on m, k. We assume that N is suﬃciently large
depending on m, k.
In the m = 4, k = 3 case, Type II solutions were generated by the ansatz

(t1, t2, t3) = (abd, acdn, bcdn)

for various quadruples (a, b, c, d) (or equivalently, quadruples (a, c, d, e), setting b := ce − a); see (2.22).
We will use a generalisation of this ansatz for higher k; for instance, when k = 4 we will construct
solutions of the form

(t1, t2, t3, t4) = (bx12x123x124x1234, x12x23x24x123x124x234x1234n, bx23x123x234x1234n, bx24x124x234x1234n)

for various octuples (b, x12, x23, x24, x123, x124, x234, x1234), or equivalently, using octuples

(x12, x23, x24, x123, x124, x234, x1234, e),

and setting b = ex23x24x234 − x12x24x124 − x12x23x123.

More generally, we will generate Type II solutions via the following lemma.

Lemma 11.2 (Generation of Type II solutions). Let P denote the set 2k−1 − 1-element set

P := {I ⊂ {1, . . . , k} : 2 ∈ I; I ̸= {2}}.

Let (xI )I∈P be a tuple of natural numbers, and let e be another natural number, obeying the inequalities

1
2m N ⩽ e Y

I∈P xI ⩽ 1
m N(11.1)

32 CHRISTIAN ELSHOLTZ AND TERENCE TAO

and

(11.2) 1 < xI ⩽ N 1/2
k+2

whenever I ∈ P. Suppose also that the quantity

(11.3) w := Y

I∈P:I̸={1,2} xI

is square-free. Set
 b := e Y

I∈P:1̸∈I xI −
 kX
j=3
 Y

I∈P:j̸∈I xI(11.4)
 t1 := b Y

I∈P:1∈I xI(11.5)
 n := mt1 − e(11.6)
 t2 := n Y

I∈P xI(11.7)

and

(11.8) tj := bn Y

I∈P:j∈I xI .

Then n is a natural number with n ⩽ N , and (t1, . . . , tk) is a Type II solution for this value of n.
Furthermore, each choice of (xI )I∈P and e generates a distinct Type II solution.

Remark 11.3. In the m = 4, k = 3 case, the parameters xI are related to the coordinates (a, b, c, d, e, f )
appearing in Proposition 2.5 by the formula

(a, b, c, d, e, f ) = (x12, b, x23, x123, e, 4x12x23x123 − 1);

however, the constraint that a, b, c have no common factor and abd is coprime to n has been replaced by
the slightly diﬀerent criterion that d is squarefree, which turns out to be more convenient for obtaining
lower bounds (note that the same trick was also used to prove (5.1)). Parameterisations of this type
have appeared numerous times in the previous literature (see [19, 22, 54, 12], or indeed Propositions
2.1, 2.5), though because most of these parameterisations were focused on dealing with all solutions
of a given type, as opposed to an easily countable subset of solutions, there were more parameters xI
(indexed by all non-empty subsets of {1, . . . , k}, not just the ones in P), and there were some coprimality
conditions on the xI rather than square-free conditions.

Proof. Let the notation be as in the lemma. Then from (11.2) one has

kX
j=3
 Y

I∈P:j̸∈I xI ⩽ (k − 2)N 2
k−2/2
k+2 ≪ N 1/16

while since Y

I∈P xI ≪ N 2
k−1/2
k+2 ≪ N 1/8

we see from (11.1) that e ≫ N 7/8.

From (11.4) we then have that
 1
2 e Y

I∈P:1̸∈I xI ⩽ b ⩽ e Y

I∈P:1̸∈I xI

COUNTING THE NUMBER OF SOLUTIONS TO THE ERD ˝OS-STRAUS EQUATION ON UNIT FRACTIONS 33

and thus by (11.5) 1
2 e Y

I∈P xI ⩽ t1 ⩽ e Y

I∈P xI

and thus by (11.6) (noting that m ⩾ 4)

1
4 me Y

I∈P xI ⩽ n ⩽ me Y

I∈P xI .

These bounds ensure that b, n, t1, . . . , tk are natural numbers with n ⩽ N , and with with t2, . . . , tk
divisible by n. Dividing (11.4) by bn Q
 I∈P xI and using (11.5), (11.7), (11.8), we conclude that

1
t2 = e
nt1 −
 kX
j=3
 1
tj ;

applying (11.6) one concludes that (t1, . . . , tk) is a Type II solution.
It remains to demonstrate that each choice of (xI )I∈P and e generates a distinct Type II solution,
or equivalently that the Type II solution (t1, . . . , tk) uniquely determines (xI )I∈P and e. To do this,
ﬁrst observe from (1.6) that (t1, . . . , tk) determines n, and from (11.6) we see that e is determined also.
Next, observe from (11.5), (11.7), (11.8) that for any 3 ⩽ j ⩽ k, one has

(11.9) t2tj
n2t1 =
 0

@ Y

I∈P:j∈I;1̸∈I xI
 1

A
 2 0

@ Y

I∈P:j∈I XOR 1̸∈I xI
 1

A

where XOR denotes the exclusive or operator; in particular, the left-hand side is necessarily a natural
number. Note that all the factors xI appearing on the right-hand side are components of the square-free
quantity w given by (11.3). We conclude that (
Q
 I∈P:j∈I;1̸∈I xI )
2 is the largest perfect square dividing
t2tj
n2t1 . We conclude that the Type II solution (t1, . . . , tk) determines all the products

(11.10) Y

I∈P:j∈I;1̸∈I xI

for 3 ⩽ j ⩽ k. Note (from the square-free nature of w) that the xI with 1 ̸∈ I are all coprime.
Taking the greatest common divisor of the (11.10) for all 3 ⩽ j ⩽ k, we see that the Type II solution
determines x{2,3,...,k}. Dividing this quantity out from all the expressions (11.10), and then taking the
greatest common divisor of the resulting quotients for 4 ⩽ j ⩽ k, one recovers x{2,4,...,k}; a similar
argument gives xI for any I ∈ P with 1 ̸∈ I of cardinality k − 3. Dividing out these quantities and
taking greatest common divisors again, one can then recover xI for any I ∈ P with 1 ̸∈ I of cardinality
k − 4; continuing in this fashion we can recover all the xI with I ∈ P and 1 ̸∈ I.
Returning to (11.9), we can then recover the products Q
 I∈P:1,j∈I xI for all 3 ⩽ j ⩽ k. Taking
greatest common divisors iteratively as before, we can then recover all the xI with I ∈ P and 1 ∈ I,
thus reconstructing all of the data (xI )I∈P and e, as claimed. □

In view of this above lemma, we see that to prove (1.7), it suﬃces to show that the number of tuples
((xI )I∈P , e) obeying the hypotheses of the lemma is ≫ N (log N )
2k−1−1.
Observe that if we ﬁx xI with I ∈ P obeying (11.2) and with the quantity w deﬁned by (11.3), then
there are
 ≫ N
Q
 I∈P xI
choices of e that obey (11.1). Thus, noting that µ
2(w) ⩾ µ
2(
Q
 I∈P xI ), the number of tuples obeying
the hypotheses of the lemma is

(11.11) ≫ N X
 ∗
 µ
2(
Q
 I∈P xI )
Q
 I∈P xI ,

34 CHRISTIAN ELSHOLTZ AND TERENCE TAO

where the sum P
 ∗ ranges over all choices of (xI )I∈P obeying the bounds (11.2). To estimate (11.11),
we make use of [13, Theorem 6.4], which we restate as a lemma:

Lemma 11.4. Let l ⩾ 1, and for each 1 ⩽ i ⩽ l, let αi < βi be positive real numbers. Then

(11.12) X

N αi ⩽ni⩽N βi for all 1⩽i⩽l
 µ
2(n1 · · · nl)
n1 · · · nl ≫l (log N )l lY

i=1
(βi − αi),

for N suﬃciently large depending on l and the α1, . . . , αl, β1, . . . , βl.

From this lemma (and noting that there are 2k−1 − 1 parameters xI in the sum P
 ∗) we see that

(11.13) X
 ∗
 µ
2(Q
 I∈P xI )
Q
 I∈P xI ≫ log2
k−1−1 N ;

inserting this into (11.11) we obtain the claim.
Now we prove (1.8). As in Section 5, the arguments are similar to those used to prove (1.7), but
with the additional input of the Bombieri-Vinogradov inequality.

As in the proof of (1.7), it suﬃces to obtain a lower bound (in this case, ≫ N (log N )2k−1 −2

log log N ) on the
number of tuples ((xI )I∈P , e), but now with the additional constraint that the quantity

p := mt1 − e = mb Y

I∈P:1∈I xI − e

is prime.
Suppose we ﬁx (xI )I∈P obeying (11.2) with w squarefree. We may write

p = qe + r

where

(11.14) q := m Y

I∈P xI − 1

and
 r := −m Y

I∈P:1∈I xI
 kX
j=3
 Y

I∈P:j̸∈I xI .

Thus as e varies in the range given by (11.1), qe + r traces out an arithmetic progression of spacing q
whose convex hull contains [0.6N, 0.9N ] (say). Thus, every prime p in this interval [0.6N, 0.9N ] that
is congruent to r mod q will provide an e that will give a Type II solution with n = p prime, and
diﬀerent choices of (xI )I∈P and p will give diﬀerent Type II solutions.
For ﬁxed (xI )I∈P , if r is coprime to q, then we see from (A.13) (and estimating li(x) = (1+o(1)) x
log x )
that the number of such p is at least

⩾ c N
log N φ(q) − D(0.6N ; q) − D(0.9N ; q)

for some absolute constant c > 0. It thus suﬃces to show that

(11.15) X
 ∗ µ
2(w)1(r,q)=1 N
log N φ(q) ≫ N (log N )
2k−1−2

log log N

and

(11.16) X
 ∗ D(cN ; q) = o
   N (log N )2
k−1−2

log log N
 !

for c = 0.6, 0.9.

COUNTING THE NUMBER OF SOLUTIONS TO THE ERD ˝OS-STRAUS EQUATION ON UNIT FRACTIONS 35

We ﬁrst show (11.15). Since li(N/100) is comparable to N/ log N , and φ(q) ⩽ q ≪ w, we may
simplify (11.15) as

(11.17) X
 ∗
 µ
2(w)
Q
 I∈P xI 1(r,q)=1 ≫ (log N )
2k−1−1

log log N .

The expression on the left-hand side is similar to (11.11), but now one also has the additional constraint
1(r,q)=1. To deal with this constraint, we restrict the ranges of the xI parameters somewhat to perform
an averaging in the x{1,2} parameter (taking advantage of the fact that this parameter does not appear
in the µ
2(w) term). More precisely, we restrict to the ranges where

(11.18) xI ⩽ N 1/2
100k

(say) for I ̸= {1, 2}, and

(11.19) x{1,2} ⩽ N 1/2
k+2 .

We now analyse the constraint that r and q are coprime. We can factor

r = −mx2
{1,2}s

where
 s :=
 0

@ Y

I∈P:1∈I;I̸={1,2} xI
 1

A kX
j=3
 Y

I∈P:j̸∈I;I̸={1,2} xI ;

the point is that s does not depend on x{1,2}. Since q + 1 is divisible by mx{1,2}, we see that mx2
{1,2}
is coprime to q, and thus (q, r) = 1 iﬀ (q, s) = 1. We can write q = ux{1,2} − 1, where u :=
m Q
 I∈P:I̸={1,2} xI , and so (q, r) = 1 iﬀ (ux{1,2} − 1, s) = 1.
We may replace s here by the largest square-free factor s
′ of s. If we then factor s
′ = vy, where
v := (s
′, u) and y := s
′/v, then ux{1,2} − 1 is already coprime to v, and so we conclude that (q, r) = 1
iﬀ (ux{1,2} − 1, y) = 1.
Fix xI for I ̸= {1, 2}. By construction, u and y are coprime, and so the constraint (ux{1,2}−1, y) = 1
restricts x{1,2} to φ(y) distinct residue classes modulo y. Since

y ⩽ s ≪ N 1/2
90k

(say) thanks to (11.18), we conclude that
X

x{1,2}⩽N 1/2k+2
 1(q,r)=1
x{1,2} ≫ φ(y)
y log N.

Using the crude bound
13 (A.11), we may lower bound φ(y)
y ≫ 1
log log N . We may thus lower bound the
left-hand side of (11.17) by log N
log log N
 X
 ∗∗
 µ
2(w)
w ,

where P
 ∗∗ sums over all xI for I ̸= {1, 2} obeying (11.18). But by Lemma 11.4 we have

X
 ∗∗
 µ
2(w)
w ≫ (log N )2
k−1−2,

and the claim (11.17) follows.

13It is quite likely that by a ﬁner analysis of the generic divisibility properties of y, one can remove this double
logarithmic loss, but we will not attempt to do so here.

36 CHRISTIAN ELSHOLTZ AND TERENCE TAO

Finally, we show (11.16). Observe that each q can be represented in the form (11.14) in at most
τ2k−1−1(q + 1) diﬀerent ways; also, from (11.2) we have q ≪ N 2
k−1/2
k+2 = N 1/8. We may thus bound
the left-hand side of (11.16) by X

q≪N 1/8 D(cN ; q)τ2k−1−1(q + 1).

From the Bombieri-Vinogradov inequality (A.14) and the trivial bound D(cN ; q) ≪ N/q one has
X

q≪N 1/8 qD(cN ; q)
2 ≪A N log−A N

for any A > 0, while from Lemma A.1 (and shifting q by 1) one has
X

q≪N 1/8
 τ2k−1−1(q + 1)2

q ≪ logO(1) N.

The claim then follows from the Cauchy-Schwarz inequality (taking A large enough). The proof of
Theorem 1.11 is now complete.

Appendix A. Some results from number theory

In this section we record some well-known facts from number theory that we will need throughout
the paper. We begin with a crude estimate for averages of multiplicative functions.
Now we record some asymptotic formulae for the divisor function τ . From the Dirichlet hyperbola
method we have the asymptotic

(A.1) X

n⩽N τ (n) = N log N + O(N )

(see e.g. [28, §1.5]). More generally, we have

(A.2) X

n⩽N τk(n) = N logk−1 N + Ok(N logk−2 N )

for all k ⩾ 1, where τk(n) := P
 d1,...,dk:d1...dk=n 1. Indeed, the left-hand side of (A.2) can be rearranged
as X

d1⩽N
 X

d2⩽N/d1 . . . X

dk⩽N/d1...dk−1 1

and the claim follows by evaluating each of the summations in turn.
We can perturb this asymptotic:

Lemma A.1 (Crude bounds on sums of multiplicative functions). Let f (n) be a multiplicative function
obeying the bounds
 f (p) = m + O( 1
p )

for all primes p and some integer m ⩾ 1, and

|f (p
j)| ≪ jO(1)

for all primes p and j > 1. Then one has
X

n⩽N f (n) ≪m N logm−1 N

for N suﬃciently large depending on m; from this and summation by parts we have in particular that
X

n⩽N
 f (n)
n ≪m logm N

COUNTING THE NUMBER OF SOLUTIONS TO THE ERD ˝OS-STRAUS EQUATION ON UNIT FRACTIONS 37

If f is non-negative, we also have the corresponding lower bound
X

n⩽N f (n) ≫m N logm−1 N

and hence X

n⩽N
 f (n)
n ≫m logm N

One can of course get much better estimates by contour integration methods (and these estimates
also follow without much diﬃculty from the more general results in [21]), but the above crude bounds
will suﬃce for our purposes.

Proof. We allow all implied constants to depend on m. By M¨obius inversion, we can write

f (n) = X
 d|n τm(d)g( n
d )

where g is a multiplicative function obeying the bounds

g(p) = O( 1
p )

and |g(pj)| ≪ jO(1)

for all j > 1. In particular, the Euler product

∞X

n=1
 |g(n)|
n = Y
 p
 0

@ 1 + |g(p)|
p +
 ∞X
j=2
 |g(p
j)|
pj
 1

A = Y
 p
   1 + O   1
p2
   

is absolutely convergent.
We may therefore write P
 n⩽N f (n) as

(A.3) X

k⩽N g(k) X

d⩽N/k τm(d).

Applying (A.2), we conclude
 | X

n⩽N f (n)| ≪ X

k⩽N
 |g(k)|
k N logm−1 N

and the upper bound follows from the absolute convergence of P ∞
n=1 |g(n)|
n .
Now we establish the lower bound. By zeroing out f at various small primes p (and all their
multiples), we may assume that f (p
j) = g(pj) = 0 for all p ⩽ w for any ﬁxed threshold w. By making
w large enough, we may ensure that
 1 −
 ∞X

n=2
 |g(n)|
n > 0.

If we then insert the bound (A.2) into (A.3) we obtain the claim. □

As a typical application of Lemma A.1 we have

(A.4) X

n⩽N τ k(n) ≪k N log2k−1 N

for any N > 1 and k ⩾ 1, (see also [35]).
To study some more detailed distribution of divisors and prime divisors we recall the Tur´an-Kubilius
inequality for additive functions. A function w is called additive, if w(n1n2) = w(n1)+w(n2), whenever
gcd(n1, n2) = 1.

38 CHRISTIAN ELSHOLTZ AND TERENCE TAO

Lemma A.2 (Tur´an-Kubilius inequality (see [60], page 20)). Let w : N → R denote an arithmetic
function which is additive (thus w(nm) = w(n) + w(m) whenever n, m are coprime). Let A(N ) =
P
 pk⩽N w(pk)
pk and D2(N ) = P
 pk⩽N |w(pk)|
2

pk . For every N ⩾ 2 and for any additive function w the
following inequality holds: X

n⩽N |w(n) − A(N )|
2 ⩽ 30N D2(N ).

(Here P
 pk denotes the sum over all prime powers.)

Example. Let ω(n) denote the number of distinct prime factors of n, then A(N ) = P
 pk⩽N ω(pk)
pk =

log log N + O(1) and D2(N ) = P pk⩽N ω(pk)
2

pk = A(N ) = log log N + O(1). The Tur´an-Kubilius
inequailty then gives X

n⩽N |ω(n) − log log N |2 ⩽ 30N log log N + O(N ).

In particular, if ξ(n) → ∞ as n → ∞, then one has |ω(n) − log log n| ⩽ ξ(n)√log log n for all n in a set
of integers of density 1. For more details see [71].
From (A.1) one might guess the heuristic

(A.5) τ (n) ≈ log n

on average. But it follows from the Tur´an-Kubilius inequality that for “typical” n, the number of
divsors is about 2
log log n = (log n)
log 2, which is considerably smaller, and that a small number of
integers with an exceptionally large number of divisors heavily inﬂuences this average. The inﬂuence
of these integers with a very large number of divsiors dominates even more for higher moments. The
extremal cases heuristically consist of many small prime factors, and the following “divisor bound”
holds

(A.6) τ (n) ⩽ 2(1+o(1)) log n
log log n = O(n 1
log log n )

for any n ⩾ 1; see [50].
The Tur´an-Kubilius type inequalities have been studied for shifted primes as well. We make use of
the following result of Barban, (see Elliott [11], Theorem 12.10).

Lemma A.3. A function w : N → R+ is said to be strongly additive if it is additive and w(p
k) = w(p)
holds, for every prime power pk, k ⩾ 1. Let w denote a real nonnegative strongly additive function.
Deﬁne S(N ) = P
 p⩽N w(p)
p−1 and Λ(N ) = maxp⩽N w(p). Suppose that Λ(N ) = o(S(N )), as N → ∞.
Then for any ﬁxed ε > 0, the prime density

νN (p; |w(p + 1) − S(N )| > εS(N )) → 0 as N → ∞.

The same holds for other shifts p + a, where a ̸= 0.

The function ω(n) is strongly additive. This lemma implies that for primes with relative prime
density 1, p + 1 contains about 1
2 log log p primes of the form 1 mod 4. To see this one chooses w(p) = 1
if p ≡ 1 mod 4, and 0 otherwise. In this example one has S(N ) ∼ 1
2 log log N and Λ(N ) = 1.
We recall the quadratic reciprocity law

(A.7)   m
n
     n
m
   = (−1)
(n−1)(m−1)/4

for all odd m, n, where   m
n   is the Jacobi symbol, as well as the companion laws

(A.8)   −1
n
   = (−1)(n−1)/4

and

(A.9)   2
n
   = (−1)(n2−1)/8

COUNTING THE NUMBER OF SOLUTIONS TO THE ERD ˝OS-STRAUS EQUATION ON UNIT FRACTIONS 39

for odd n.
For any primitive residue class a mod q and any N > 0, let π(N ; q, a) denote the number of primes
p < N that are congruent to a mod q. We recall the Brun-Titchmarsh inequality (see e.g. [28, Theorem
6.6])

(A.10) π(N ; q, a) ≪ N
φ(q) log N
q

for any such class with N ⩾ q. This bound suﬃces for upper bound estimates on primes in residue
classes. Due to the q in the denominator of log( N
q ), it will only be eﬃcient to apply this inequality
when q is much smaller than N , e.g. q ⩽ N c for some c < 1.
The Euler totient function φ(q) in the denominator is also inconvenient; it would be preferable if
one could replace it with q. Unfortunately, this is not possible; the best bound on 1
φ(q) in terms of q
that one has in general is

(A.11) 1
φ(q) ≪ log log q
q

(see e.g. [53]). Using this bound would simplify our arguments, but one would lose an additional factor
of log log N or so in the ﬁnal estimates. To avoid this loss, we observe the related estimate

(A.12) 1
φ(q) ≪ 1
q
 X
 d|q
 1
d .

Indeed, we have q
φ(q) = Y
 p|q
 p
p − 1

= Y
 p|q (1 + 1
p )(1 + O( 1
p2 ))

≪ Y
 p|q (1 + 1
p )

⩽ X
 d|q
 1
d ,

and (A.12) follows. (One could restrict d to be square-free here if desired, but we will not need to do
so in this paper.)
The Brun-Titchmarsh inequality only gives upper bounds for the number of primes in an arithmetic
progression. To get lower bounds, we let D(N ; q) denote the quantity

(A.13) D(N ; q) := max
(a,q)=1
      π(N ; q, a) − li(N )
φ(q)
      .

where li(x) := R x
0 dt
log t is the logarithmic integral. The Bombieri-Vinogradov inequality (see e.g. [28,
Theorem 17.1]) implies in particular 14 that

(A.14) X

q⩽N θ D(N ; q) ≪θ,A N log−A N

for all 0 < θ < 1/2 and A > 0. Informally, this gives lower bounds on π(N ; q, a) on the average for
q much smaller than N 1/2.

14The inequality is usually phrased using the summatory von Mangoldt function ψ(N ; q, a) = ∑n⩽N ;n=a mod q Λ(n).
A summation by parts converts it to an estimate using the prime counting function, see [8] for details.

40 CHRISTIAN ELSHOLTZ AND TERENCE TAO

References

[1] A. Aigner, Br¨uche als Summe von Stammbr¨uchen, J. Reine Angew. Math. 214/215 (1964), 174-179.
[2] M. B. Barban, P. P. Vehov, Summation of multiplicative functions of polynomials, Mat. Zametki 5 (1969), 669680.
[3] P. Bartoˇs. K Rieˇsitel’nosti Diofantickej Rovnice ∑n
j=1 1
xj = a
b . ˇCasopis pro pˇestov´an´ı matematiky, 98 (1973), 261–
264.
[4] P. Bartoˇs and K. Pehatzov´a-Boˇsank´a. K Rieˇseniu Diofantickej Rovnice 1
x + 1
y + 1
z = a
b . ˇCasopis pro pˇestov´an´ı
matematiky, 96 (1971), 294–299.
[5] M. Bello-Hernandez, M. Benito, E. Fern´andez, On egyptian fractions, preprint, arXiv:1010.2035
[6] L. Bernstein, Zur L¨osung der diophantischen Gleichung m
n , insbesondere im Fall m = 4, J. Reine Angew. Math.
211, 1962, 1-10.
[7] T. Browning, C. Elsholtz, The number of representations of rationals as a sum of unit fractions, to appear in Illinois
Journal of Mathematics.
[8] J. Br¨udern. Einf¨uhrung in die analytische Zahlentheorie. Springer, Berlin, Heidelberg, 1995.
[9] J-L. Colliot-Th´eel`ene, J-J. Sansuc, Torseurs sous des groupes de type multiplicatif; applications ´a l’´etude des points
rationnels de certaines vari´et´es alg´ebriques, C. R. Acad. Sci. Paris S´er. A-B 282 (1976), no. 18, Aii, A1113–A1116.
[10] S. Daniel, Uniform bounds for short sums of certain arithmetic functions of polynomial arguments, Unpublished
manuscript.
[11] P. D. T. A. Elliott, Probabilistic number theory. II. Central limit theorems. Grundlehren der Mathematischen
Wissenschaften, 240. Springer-Verlag, Berlin-New York, 1980.
[12] C. Elsholtz, Sums of k unit fractions, PhD thesis, Technische Universit¨at Darmstadt, 1998.
[13] C. Elsholtz, Sums of k unit fractions Trans. Amer. Math. Soc. 353 (2001), 3209–3227.
[14] P. Erd˝os. Az 1
x1 + 1
x2 + . . . + 1
xn = a
b egyenlet eg´esz sz´am´u megold´asair´ol, Matematiki Lapok 1 (1950), 192–210.
[15] P. Erd˝os, On the sum ∑x
k=1 f (k)), J. London Math. Soc. 27 (1952), 7-15.
[16] P. Erd˝os, P.; R.L. Graham, Old and new problems and results in combinatorial number theory. Monographies de
L’Enseignement Math´ematique, 28. L’Enseignement Mathmatique, Geneva, 1980. 128 pp.
[17] ´E. Fouvry, Sur le probl´eme des diviseurs de Titchmarsh, J. Reine Angew. Math. 357 (1985), 51-76.
[18] ´E. Fouvry, H. Iwaniec, The divisor function over arithmetic progressions, With an appendix by Nicholas Katz. Acta
Arith. 61 (1992), no. 3, 271-287.
[19] H. Gupta, Selected topics in number theory. Abacus Press, Tunbridge Wells, 1980. 394 pp.
[20] R. Guy, Unsolved Problems in Number Theory, 2nd ed. New York: Springer-Verlag, pp. 158-166, 1994.
[21] H. Halberstam, H.-E. Richert, On a result of R. R. Hall. J. Number Theory 11 (1979), no. 1, 76-89.
[22] R.R. Hall, Sets of Multiples, Cambridge University Press, Cambridge, 1996.
[23] D. R. Heath-Brown, The density of rational points on Cayley’s cubic surface, Proceedings of the Session in Analytic
Number Theory and Diophantine Equations, 33 pp., Bonner Math. Schriften, 360, Univ. Bonn, Bonn, 2003
[24] K. Henriot, Nair-Tenenbaum bounds uniform with respect to the discriminant, arXiv:1102.1643
[25] C. Hooley, On the number of divisors of quadratic polynomials, Acta Math. 110 (1963), 97–114.
[26] J. Huang, R. C. Vaughan, Mean value theorems for binary Egyptian fractions, J. Number Theory 131 (2011),
1641–1656
[27] M. N. Huxley, A note on polynomial congruences, Recent Progress in Analytic Number Theory, Vol. I (H. Halberstam
and C. Hooley, eds.), Academic Press, London, 1981, pp. 193-196.
[28] H. Iwaniec, E. Kowalski, Analytic number theory. American Mathematical Society Colloquium Publications, 53.
American Mathematical Society, Providence, RI, 2004.
[29] C. Jia, A Note on Terence Tao’s Paper “On the Number of Solutions to 4/p = 1/n1 + 1/n2 + 1/n3”, preprint.
[30] R.W. Jollenstein. A note on the Egyptian problem,Congressus Numerantium, 17, Utilitas Math., Winnipeg, Man.
In Proceedings of the Seventh Southeastern Conference on Combinatorics, Graph Theory, and Computing, 351–364,
Louisiana State Univ., Baton Rouge, La., 1976.
[31] I. Kotsireas, The Erd˝os-Straus conjecture on Egyptian fractions, Paul Erd˝os and his mathematics (Budapest, 1999),
140–144, J´anos Bolyai Math. Soc., Budapest, 1999.
[32] N. V. Kuznecov, The Petersson conjecture for cusp forms of weight zero and the Linnik conjecture. Sums of
Kloosterman sums, Mat. Sb. (N.S.) 111(153) (1980), no. 3, 334-383, 479.
[33] B. Landreau, A new proof of a theorem of van der Corput, Bull. London Math. Soc. 21 (1989), no. 4, 366-368.
[34] Delang Li. On the Equation 4
n = 1
x + 1
y + 1
z . Journal of Number Theory 13 (1981), 485–494, 1981.
[35] C. Mardjanichvili, Estimation d’une somme arithmetique. Comptes Rendus (Doklady) de l’Acad´emie des Sciences
de l’URSS 22 (1939), 387–389.
[36] J. McKee, On the average number of divisors of quadratic polynomials, Math. Proc. Cambridge Philos. Soc. 117
(1995), no. 3, 389-392.
[37] J. McKee, A note on the number of divisors of quadratic polynomials. Sieve methods, exponential sums, and their
applications in number theory (Cardiﬀ, 1995), 275–281, London Math. Soc. Lecture Note Ser., 237, Cambridge Univ.
Press, Cambridge, 1997.

COUNTING THE NUMBER OF SOLUTIONS TO THE ERD ˝OS-STRAUS EQUATION ON UNIT FRACTIONS 41

[38] J. McKee, The average number of divisors of an irreducible quadratic polynomial, Math. Proc. Cambridge Philos.
Soc. 126 (1999), no. 1, 17–22.
[39] L.J. Mordell, Diophantine Equations, volume 30 of Pure and Applied Mathematics. Academic Press, 1969.
[40] T. Nagell, G´en´eralisation d’un the´or`eme de Tchebicheﬀ, J. Math. 8 (1921), 343–356.
[41] M. Nair, Multiplicative functions of polynomial values in short intervals, Acta Arith. 62 (1992), no. 3, 257269.
[42] M. Nair, G. Tenenbaum, Short sums of certain arithmetic functions, Acta Math. 180 (1998), 119-144.
[43] M. Nakayama, On the decomposition of a rational number into “Stammbr¨uche.”, Tˆohoku Math. J. 46, (1939). 1-21.
[44] M.R. Obl´ath. Sur l’ ´equation diophantienne 4
n = 1
x1 + 1
x2 + 1
x3 . Mathesis 59 (1950), 308–316.

[45] G. Palam`a. Su di una congettura di Sierpi´nski relativa alla possibilit`a in numeri naturali della 5
n = 1
x1 + 1
x2 + 1
x3 .
Bollettino della Unione Matematica Italiana (3), 13 (1958), 65–72.
[46] G. Palam`a. Su di una congettura di Schinzel. Bollettino della Unione Matematica Italiana (3), 14 (1959), 82–94.
[47] C.P. Popovici. On the diophantine equation a
b = 1
x1 + 1
x2 + 1
x3 . Analele Universit˘atii Bucures. ti. Seria S. tiint.ele
Naturii. Matematic˘a-Fizik˘a 10 (1961), 29–44, 1961.
[48] O. Ore, Anzahl der Wurzeln h¨oherer Kongruenzen, Norsk Matematisk Tidsskrift, 3 Aagang, Kristiana (1921),
343–356.
[49] C. Pomerance, Analysis and Comparison of Some Integer Factoring Algorithms, in Computational Methods in
Number Theory, Part I, H.W. Lenstra, Jr. and R. Tijdeman, eds., Math. Centre Tract 154, Amsterdam, 1982, pp
89–139.
[50] S. Ramanujan, Highly composite numbers, Proc. London Math. Soc. 14 (1915), 347-409.
[51] Y. Rav, On the representation of rational numbers as a sum of a ﬁxed number of unit fractions, J. Reine Angew.
Math. 222 1966 207–213.
[52] L. Rosati, Sull’equazione diofantea 4/n = 1/x1 + 1/x2 + 1/x3, Boll. Un. Mat. Ital. (3) 9, (1954). 59-63.
[53] J. Rosser, L. Schoenfeld, Approximate formulas for some functions of prime numbers, Illinois J. Math. 6 (1962)
64-94.
[54] I.Z. Ruzsa, On an additive property of squares and primes, Acta Arithmetica 49 (1988), 281–289.
[55] J.W. Sander. On 4
n = 1
x + 1
y + 1
z and Rosser’s sieve. Acta Arithmetica 59 (1991), 183–204.

[56] J.W. Sander. On 4
n = 1
x + 1
y + 1
z and Iwaniec’ Half Dimensional Sieve. Journal of Number Theory 46 (1994), 123–136.
[57] J.W. Sander. Egyptian Fractions and the Erd˝os-Straus Conjecture. Nieuw Archief voor Wiskunde (4) 15 (1997),43–
50.
[58] G. S´andor, ¨Uber die Anzahl der L¨osungen einer Kongruenz, Acta. Math. 87 (1952), 13–17.
[59] A. Schinzel, On sums of three unit fractions with polynomial denominators, Funct. Approx. Comment. Math.
28:187–194, 2000.
[60] W. Schwarz, J. Spilker, Arithmetical functions. London Mathematical Society Lecture Note Series, 184. Cambridge
University Press, Cambridge, 1994.
[61] E.J. Scourﬁeld, The divisors of a quadratic polynomial, Proc. Glasgow Math. Assoc. 5 (1961) 8–20.
[62] A. Selberg, Harmonic analysis and discontinuous groups in weakly symmetric Riemannian spaces with applications
to Dirichlet series, J. Indian Math. Soc. (N.S.) 20 (1956), 47–87.
[63] Shen Zun, On the diophantine equation ∑k
i=0 1
xi = a
n , Chinese Ann. Math. Ser. B, 7 (1986), 213–220.
[64] P. Shiu, A Brun-Titchmarsh theorem for multiplicative functions, J. Reine Angew. Math. 313 (1980), 161–170.
[65] W. Sierpi´nski, Sur les d´ecompositions de nombres rationnels en fractions primaires, Mathesis 65 (1956), 16–32, MR
17#1185d.
[66] W. Sierpi´nski. On the Decomposition of Rational Numbers into Unit Fractions (Polish). P´anstwowe Wydawnictwo
Naukowe, Warsaw, 1957.
[67] E. S´os. Die diophantische Gleichung 1
x = 1
x1 + 1
x2 + . . . + 1
xn . Zeitschrift f¨ur mathematischen und naturwis-
senschaftlichen Unterricht, 36:97–102, 1905.
[68] B.M. Stewart. Theory of Numbers. 2nd ed. New York: The Macmillan Company; London: Collier-Macmillan, 1964.
[69] C. L. Stewart, On the number of solutions of polynomial congruences and Thue equations, J. Amer. Math. Soc. 4
(1991), no. 4, 793–835.
[70] A. Swett, http://math.uindy.edu/swett/esc.htm accessed on 27 July 2011.
[71] G. Tenenbaum, Introduction to analytic and probabilistic number theory. Cambridge Studies in Advanced Mathe-
matics, 46. Cambridge University Press, Cambridge, 1995.
[72] D.G. Terzi. On a conjecture by Erd˝os-Straus. Nordisk Tidskr. Informations-Behandling (BIT) 11 (1971), 212–216.
[73] R. Vaughan, On a problem of Erd˝os, Straus and Schinzel, Mathematika 17, 1970 193–198.
[74] C. Viola, On the diophantine equations ∏k
0 xi − ∑k
0 xi = n and ∑k
0 1
xi = a
n , Acta Arith. 22 1973, 339–352.
[75] W. Webb, On 4/n = 1/x + 1/y + 1/z, Proc. Amer. Math. Soc. 25 (1970), 578–584.
[76] W. Webb, On a theorem of Rav concerning Egyptian fractions, Canad. Math. Bull. 18 (1975), no. 1, 155156.
[77] W. Webb, On the Diophantine equation k
n = a1
x1 + a2
x2 + a3
x3 , ˇCasopis pro pˇestov´ani matematiy, roˇc. 101 (1976),
360–365.
[78] A. Wintner, Eratosthenian Averages. Waverly Press, Baltimore, Md., 1943. v+81 pp.

42 CHRISTIAN ELSHOLTZ AND TERENCE TAO

[79] K. Yamamoto, On the Diophantine Equation 4
n = 1
x + 1
y + 1
z , Mem Fac. Sci. Kyushu Univ. Ser. A, V. 19, No. 1,
1965, 37–47.
[80] Xun Qian Yang. A note on 4
n = 1
x + 1
y + 1
z . Proceedings of the American Mathematical Society, 85 (1982), 496–498.

Institut f¨ur Mathematik A, Steyrergasse 30/II, Technische Universit¨at Graz, A-8010 Graz, Austria
E-mail address: elsholtz@math.tugraz.at

Department of Mathematics, UCLA, Los Angeles CA 90095-1555
E-mail address: tao@math.ucla.edu
