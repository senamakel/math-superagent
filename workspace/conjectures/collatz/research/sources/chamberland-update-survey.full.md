<!-- source: https://www.math.grinnell.edu/~chamberl/papers/3x_survey_eng.pdf | converted from PDF -->

An Update on the 3x+1 Problem

Marc Chamberland

Department of Mathematics and Computer Science

Grinnell College, Grinnell, IA, 50112, U.S.A.

E-mail: chamberl@math.grinnell.edu

Contents

1 Introduction 2

2 Numerical Investigations and Stopping Time 3

2.1 Stopping Time . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4

2.2 Total Stopping Time . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7

2.3 The Collatz Graph and Predecessor Sets . . . . . . . . . . . . . . . . . . . . . . 9

3 Representations of Iterates of a 3x + 1 Map 12

4 Reduction to Residue Classes and Other Sets 13

5 Cycles 15

6 Extending T to Larger Spaces 17

6.1 The Integers ZZ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17

6.2 Rational Numbers with Odd Denominators . . . . . . . . . . . . . . . . . . . . 18

6.3 The Ring of 2-adic Integers ZZ2 . . . . . . . . . . . . . . . . . . . . . . . . . . . 18

6.4 The Gaussian Integers and ZZ2[i] . . . . . . . . . . . . . . . . . . . . . . . . . . 20

6.5 The Real Line lR . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20

6.6 The Complex Plane lC . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23

7 Generalizations of 3x + 1 Dynamics 23

8 Miscellaneous 25

AMS subject classiﬁcation : 11B83.

Key Words. 3x + 1 problem, Collatz conjecture.

Running title: 3x + 1 survey.
 1
 2

1 Introduction

The 3x+1 Problem is perhaps today’s most enigmatic unsolved mathematical

problem: it can be explained to child who has learned how to divide by 2

and multiply by 3, yet there are relatively few strong results toward solving it.

Paul Erd¨os was correct when he stated, “Mathematics is not ready for such

problems.”

The problem is also referred to as the 3n + 1 problem and is associated with

the names of Collatz, Hasse, Kakutani, Ulam, Syracuse, and Thwaites. It may

be stated in a variety of ways. Deﬁning the Collatz function as

C(x) =
  3x + 1 x ≡ 1 (mod 2)

x

2 x ≡ 0 (mod 2),

the conjecture states that for each m ∈ ZZ+, there is a k ∈ ZZ+ such that

C (k)(m) = 1, that is, any positive integer will eventually iterate to 1. Note that

an odd number m iterates to 3m + 1 which then iterates to (3m + 1)/2. One

may therefore “compress” the dynamics by considering the map

T (x) =
 
 3x+1

2 x ≡ 1 (mod 2)

x
2 x ≡ 0 (mod 2).

The map T is usually favored in the literature.

To a much lesser extent some authors work with the most dynamically

streamlined 3x + 1 function, F : ZZ+dd → ZZ+dd, deﬁned by

F (x) = 3x + 1

2m(3x+1)

where m(x) equals the number of factors of 2 contained in 3x+1. While working

with F allows one to work only on the odd positive integers, the variability of

m seems to prohibit any substantial analysis.

This survey reﬂects the author’s view of how work on this problem can

be structured. I owe a huge debt to Jeﬀ Lagarias and G¨unther Wirsching for

the important work they have done in bringing this problem forward. The

paper of Lagarias[45](1985) thoroughly catalogued earlier results, made copious
 3

connections, and developed many new lines of attack; it has justly become the

classical reference for this problem. Wirsching’s book [87](1998) begins with

a strong survey, followed by several chapters of his own noteworthy analysis.

Lagarias has also maintained an annotated bibliography [48](1998) of work on

this problem, another valuable resource. This current survey would have been

much more diﬃcult to write in the absence of these signiﬁcant contributions.

This survey is not meant to be exhaustive, but rather is complementary to

the work of Lagarias and Wirsching. Where I believed there was signiﬁcant new

work in a given area, I included earlier contributions for the sake of completeness.

Some areas which have not seen recent development, such as the interesting

work connected to functional equations, cellular automata, and the origin of

the problem, have not been mentioned; the reader may consult Wirsching’s

book [87](1998).

2 Numerical Investigations and Stopping Time

The structure of the positive integers forces any orbit of T to iterate to one of

the following:

1. the trivial cycle {1, 2}

2. a non-trivial cycle

3. inﬁnity (the orbit is divergent)

The 3x + 1 Problem claims that option 1 occurs in all cases. Oliveira e

Silva[61, 62](1999,2000) proved that this holds for all numbers n < 100 × 250 ≈

1.12 × 1017. This was accomplished with two 133MHz and two 266MHz DEC

Alpha computers and using 14.4 CPU years. This computation ended in April

2000. Roosendaal[65](2003) claims to have improved this to n = 195 × 250 ≈

2.19 × 1017. His calculations continue, with the aid of many others in this

distributed-computer project.

The record for proving the non-existence of non-trivial cycles is that any

such cycle must have length no less than 272,500,658. This was derived with
 4

the help of numerical results like those in the last paragraph coupled with the

theory of continued fractions – see a section 5 for more on cycles.

There is a natural algorithm for checking that all numbers up to some N

iterate to one. First, check that every positive integer up to N − 1 iterates to

one, then consider the iterates of N . Once the iterates go below N , you are

done. For this reason, one considers the so-called stopping time of n, that is,

the number of steps needed to iterate below n :

σ(n) = inf{k : T (k)(n) < n}.

Related to this is the total stopping time, the number of steps needed to iterate

to 1:
 σ∞(n) = inf{k : T (k)(n) = 1}.

One considers the height of n, namely, the highest point to which n iterates:

h(n) = sup{T (k)(n) : k ∈ ZZ+}.

Note that if n is in a divergent trajectory, then σ∞(n) = h(n) = ∞. These

functions may be surprisingly large even for small values of n. For example,

σ(27) = 59, σ∞(27) = 111, h(27) = 9232.

The orbit of 27 is depicted in Figure 1.

Roosendaal[65](2003) has computed various “records” for these functions1.

Various results about consecutive numbers with the same height are catalogued

by Wirsching[87, pp.21–22](1998).

2.1 Stopping Time

The natural algorithm mentioned earlier can be rephrased: the 3x + 1 problem

is true if and only if every positive integer has a ﬁnite stopping time. Terras[77,

1Roosdendaal has diﬀerent names for these functions, and he applies them to the map

C(x).
 5

0

1000

2000

3000

4000
 0 10 20 30 40 50 60 70

Figure 1: Orbit starting at 27.
 6

78](1976,1979) has proven that the set of positive integers with ﬁnite stopping

time has density one. Speciﬁcally, he showed that the limit

F (k) := lim
m→∞ 1
m |{n ≤ m : σ(n) ≤ k}|

exists for each k ∈ ZZ+ and limk→∞ F (k) = 1. A shorter proof was provided

by Everett[31](1977). Lagarias[45](1985) proved a result regarding the speed of

convergence:
 F (k) ≥ 1 − 2−ηk

for all k ∈ ZZ+, where η = 1 − H(θ), H(x) = −x log(x) − (1 − x) log(1 − x) and

θ = (log2 3)−1. He uses this to constrain any possible divergent orbits:

∣{n ∈ ZZ+ : n ≤ x, σ(n) = ∞}∣ ≤ c1x1−η

for some positive constant c1. This implies that any divergent trajectory cannot

diverge too slowly. Along these lines, Garcia and Tal[33](1999) have recently

proven that the density of any divergent orbit is zero. This result holds for more

general sets and more general maps.

Along diﬀerent lines, Venturini[81](1989) showed that for every ρ > 0, the set

{n ∈ ZZ+ : T (k)(n) < ρn for some k} has density one. Allouche[1](1979) showed

that {n ∈ ZZ+ : T (k)(n) < nc for some k} has density one for c > 3/2 − log2 3 ≈

0.869. This was improved by Korec[39](1994) who obtained the same result

with c > log4 3 ≈ 0.7924.

Not surprisingly, results of a probabilistic nature abound concerning these

3x + 1 functions. An assumption often made is that after many iterations, the

next iterate has an equal chance of being either even or odd. Wagon[84](1985)

argues that the average stopping time for odd n (with the function C(x)) ap-

proaches a constant, speciﬁcally, the number

∞∑

i=1[1 + 2i + i log2 3] ci

2[i log2 3] ≈ 9.477955

where ci is the number of sequences containing 3/2 and 1/2 with exactly i 3/2’s

such that the product of the whole sequence is less than 1, but the product
 7

of any initial sequence is greater than 1. Note that this formula bypasses the

pesky “+1”, perhaps justiﬁed asymptotically. This seems to be borne out in

Wagon’s numerical testing of stopping times for odd numbers up to n = 109,

which matches well with the approximation given above.

2.2 Total Stopping Time

Results regarding the total stopping time are also plenteous. Applegate and

Lagarias[9](2002) make use of two new auxiliary functions: the stopping time

ratio
 γ(n) := σ∞(n)
log n ,

and the ones-ratio ρ(n) for convergent sequences, deﬁned as the ratio of the

number of odd terms in the ﬁrst σ∞(n) iterates divided by σ∞(n). It is easy

to see that γ(n) ≥ 1/ log 2 for all n, with equality only when n = 2k. Stronger

inequalities are
 γ(n) ≥ 1
log 2 − ρ(n) log 3

for any convergent trajectory, while if ρ(n) ≤ 0.61, then for any positive ϵ,

γ(n) ≤ 1
log 2 − ρ(n) log 3 + ϵ

for all suﬃciently large n. If one assumes that the ones-ratio equals 1/2 (which is

equivalent to the equal probability of encountering an even or an odd after many

iterates), we have that the average value of γ(n) is 2/ log(4/3) ≈ 6.95212, as

has been observed by Shanks[69](1965), Crandall[26](1978), Lagarias[45](1985),

Rawsthorne[64](1985), Lagarias and Weiss[47](1992), and Borovkov and Pfeifer[15](2000).

Experimental evidence supports this observation. Compare this with the upper

bounds suggested by the stochastic models of Lagarias and Weiss[47](1992):

lim sup
n→∞ γ(n) ≈ 41.677647.

Applegate and Lagarias[9](2002) note from records of Roosendaal[65](2003)

what is apparently the largest known value of γ:

n = 7, 219, 136, 416, 377, 236, 271, 195
 8

produces σ∞(n) = 1848 and γ(n) ≈ 36.7169. Applegate and Lagarias seek a

lower bound for γ which holds inﬁnitely often. Using the well-known fact that

T (k)(2k − 1) = 3k − 1 (see, for example, Kuttler[44](1994)), they note that

γ(2k − 1) ≥ log 2 + log 3
(log 2)2 ≈ 3.729.

They go on to show that there are inﬁnitely many converging n whose ones-ratio

is at least 14/29, hence giving the lower bound

γ(n) ≥ 29
29 log 2 − 14 log 3 ≈ 6.14316

for inﬁnitely many n. Though the proof involves an extensive computational

search on the Collatz tree to depth 60, the authors note with surprise that the

probabilistic average of γ(n) – approximately 6.95212 – was not attained.

Roosendaal[65](2003) deﬁnes a function which he calls the residue of a num-

ber x ∈ ZZ+, denoted Res(x). Suppose x is a convergent C-trajectory with E

even terms and O odd terms before reaching one. Then the residue is deﬁned

as
 Res(x) := 2E

x3O .

Roosendall notes that Res(993) = 1.253142 . . ., and that this is the highest

residue attained for all x < 232. He conjectures that this holds for all x ∈ ZZ+.

Zarnowski[89](2001) recasts the 3x + 1 problem as one with Markov chains.

Let g be the slightly altered function

g(x) =
 
 3x+1

2 x ≡ 1 (mod 2), x > 1

x
2 x ≡ 0 (mod 2)

1 x = 1,

en the column vector whose nth entry is one and all other entries zero, and the

transition matrix P be deﬁned by

Pij =
  1 if g(i) = j,

0 otherwise.

This gives a correspondence between g(k)(n) and eT P k, and the 3x + 1 Problem

is true if
 lim
k→∞ P k = [1 0 0 · · ·],
 9

128

64

32

16

8

4

2

1
 10

5

20

40
 3

6

12

13

26
85

42

21

84
 Figure 2: The Collatz graph.

where 1 and 0 represent constant column vectors. Zarnowski goes on to show

that the structure of a certain generalized inverse X of I − P encodes the total

stopping times of ZZ+.

For pictorial representations of stopping times for an extension of T , see

Dumont and Reiter[29].

2.3 The Collatz Graph and Predecessor Sets

The topic of stopping times is intricately linked with the Collatz tree or Collatz

graph, the directed graph whose vertices are predecessors of one via the map T .

It is depicted in Figure 2.3.

The structure of the Collatz graph has attracted some attention. Andaloro[4](2002)

studied results about the connectedness of subsets of the Collatz graph. Urvoy[79](2000)
 10

proved that the Collatz graph is non-regular, in the sense that it does not have

a decidable monadic second order theory; this is related to the work of Conway

mentioned in Section 4.

Instead of analyzing how fast iterates approach one, one may consider the

set of numbers which approach a given number a, that is, the predecessor set of

a:
 PT (a) := {b ∈ ZZ+ : T (k)(b) = a for some k ∈ ZZ+}

Since such sets are obviously inﬁnitely large, one may measure those terms in

the predecessor set not exceeding a given bound x, that is,

Za(x) := |{n ∈ PT (a) : n ≤ x}|.

The size of Za(x) was ﬁrst studied by Crandall[26](1979), who proved the exis-

tence of some c > 0 such that

Z1(x) > xc, x suﬃciently large.

Wirsching[87, p.4](1998) notes that this result extends to Za(x) for all a ̸≡

0 mod 3. Using the tree-search method of Crandall, Sander[67](1990) gave a spe-

ciﬁc lower bound, c = 0.25, and Applegate and Lagarias[6](1995) extended this

to c = 0.643. Using functional diﬀerence inequalities, Krasikov[41](1989) intro-

duced a diﬀerent approach and obtained c = 3/7 ≈ 0.42857. Wirsching[85](1993)

used the same approach to obtain c = 0.48. Applegate and Lagarias[7](1995)

superseded these results with Z1(x) > x0.81, for suﬃciently large x, by enhanc-

ing Krasikov’s approach with nonlinear programming. Recently, Krasikov and

Lagarias[42](2002) streamlined this approach to obtain

Z1(x) > x0.84, x suﬃciently large.

Wirsching[87](1998) has pushed these types of results in a diﬀerent direction.

On a seemingly diﬀerent course, for j, k ∈ ZZ+ let Rj,k denote the set of all sums

of the form
 2α0 + 2α1 3 + 2α232 + · · · + 2αj 3j
 11

where j + k ≥ α0 > · · · > αj ≥ 0. The size of Rj,k satisﬁes

|Rj,k| =
  j + k + 1

j + 1
  .

To maximize the size, one has |Rj−1,j | = (2j
j ). Wirsching posed the following

“covering conjecture”: there is a constant K > 0 such that for every j, l ∈ ZZ+

we have the implication

|Rj−1,j | ≥ K ·2·3l−1 =⇒ Rj−1,j covers the prime residue classes to modulus 3l.

This conjecture implies a stronger version of the earlier inequalities:

lim inf
x→∞
 (
 inf
a̸≡0 mod 3
 Za(ax)

xδ
 )
 > 0 for any δ ∈ (0, 1).

Wirsching argues that, intuitively, the sums of mixed powers can be seen as

accumulated non-linearities occuring when iterating the map T .

A large part of Wirsching’s book [87](1998) concerns a ﬁner study of the

predecessor sets using the functions

el(k, a) = |{b ∈ ZZ+ : T (k+l)(b) = a, k even iterates, l odd iterates}|.

Deﬁning the nth estimating series as

sn(a) :=
 ∞∑

l=1 el (n + ⌊l log2(3/2)⌋, a) ,

Wirsching proves the implication

lim inf
n→∞ sn(a)
βn > 0 =⇒ Za(x) ≥ C ( x
a
 )log2 β for some constant C > 0 and large x.

Since el(k, a) depends on a only through its residue class to modulo 3l, Wirsching

considers the functions el(k, ·) whose domain is ZZ3, the group of 3-adic integers.

Since el(k, a) = 0 whenever l ≥ 1 and 3|a, the set {el(k, ·) : l ≥ 1, k ≥ 0} is

a family of functions on the compact topological group ZZ∗ of invertible 3-adic

integers. This application of 3-adic integers to the 3x + 1 Problem was ﬁrst

seen in Wirsching[86](1994), and similar analysis was also done by Applegate
 12

and Lagarias[8](1995). The functions el(k, ·) are integrable with respect to ZZ∗’s

unique normalized Haar measure, yielding the 3-adic average

¯el(k) := ∫
ZZ∗ el(k, a)da = 1

2 · 3l−1
  k + l

l
  .

Several results follow with this approach, including

lim inf
n→∞ 1

2n
 ∫
ZZ∗ sn(a)da > 0,

implying that every predecessor set PT (a) with a ̸≡ 0 mod 3 has positive

density.

3 Representations of Iterates of a 3x + 1 Map

The oft-cited result in this area is due to B¨ohm and Sontacchi[14](1978): the

3x + 1 problem is equivalent to showing that each n ∈ ZZ+ may be written as

n = 1

3m
 (

2vm −
 m−1∑

k=0 3m−k−12vk )

where m ∈ ZZ+ and 0 ≤ v0 < v1 < · · · vm are integers. Similar results were

obtained by Amig´o[2, Prop.4.2](2001).

Sinai[70](2003) studies the function F on the set ⊓ deﬁned as

⊓ = {1} ∪ ⊓+ ∪ ⊓−, ⊓±1 = 6ZZ
+ ± 1.

Let k1, k2, . . . , km ∈ ZZ+ and ϵ = ±1. Then the set of x ∈ ⊓ϵ to which one can

apply F (k1)F (k2) · · · F (km) is an arithmetic progression

σ(k1,k2,...,km,ϵ) = {6 · (2k1+k2+···+km + qm) + ϵ}

for some qm such that 1 ≤ qm ≤ 2k1+k2+···+km . Moreover,

F (k1)F (k2) · · · F (km)(σ(k1,k2,...,km,ϵ)) = {6 · (3mp + r) + δ}

for some r and δ satisfying 1 ≤ r ≤ 3m, δ = ±1. Results in this spirit may

be found in Andrei et al.[5](2000) and Kuttler[44](1994). Sinai uses this result
 13

to obtain some distributional information regarding trajectories of F . Let 1 ≤

m ≤ M , x0 ∈ ⊓ and

ω ( m
M
 ) = log(F (m)(x0)) − log(x0) + m(2 log 2 − log 3)
√M .

If 0 ≤ t ≤ 1, then ω(t) behaves like a Wiener trajectory.

Related to these results is the connection made in Blecksmith et al.[13](1998)

between the 3x+1 problem and 3-smooth representations of numbers. A number

n ∈ ZZ+ has a 3-smooth representation if and only if there exist integers {ai}

and {bi} such that

n =
 k∑

i=1 2ai3bi, a1 > a2 > · · · > ak ≥ 0, 0 ≤ b1 < b2 < · · · < bk.

Note the similarity with the terms considered by Wirsching in the last section.

These numbers were studied at least as early as Ramanujan. A 3-smooth rep-

resentation of n is special of level k if

n = 3k + 3k−12a1 + · · · + 3 · 2ak−1 + 2ak

in which every power of 3 appears up to 3k. For a ﬁxed k, each n has at most

one such representation – see Lagarias[46](1990), who credits the proof to Don

Coppersmith. Blecksmith et al. then oﬀer the reader to prove that m ∈ ZZ+

iterates to 1 under C if and only if there are integers e and f such that the

positive integer n = 2e − 3f m has a special 3-smooth representation of level

k = f − 1. The choice of e and f is not unique, if it exists.

4 Reduction to Residue Classes and Other Sets

Once one is convinced that the 3x + 1 problem is true, a natural approach is

to ﬁnd subsets S ⊂ ZZ+ such that proving the conjecture on S implies it is true

on ZZ+. It is obvious this holds if S = {x : x ≡ 3 mod 4} since numbers in

the other residue classes decrease after one or two iterations. Puddu[63](1986)

and Cadogan[19](1984) showed that this works if S = {x : x ≡ 1 mod 4}.

The work of B¨ohm and Sontacchi[14](1978) implies that m odd T -iterates of x
 14

2

1

0 0
 1

2

Figure 3: Dynamics of Integers (a) mod 3 and (b) mod 4.

equals (3/2)m(x + 1) − 1, hence odds must eventually become even. Coupling

this with the dynamics of integers in ZZ4 (see Figure 3b) implies both S = {x :

x ≡ 1 mod 4} and S = {x : x ≡ 2 mod 4} are suﬃcient. Similarly, Figure

3a indicates S = {x : x ≡ 1 mod 3} or S = {x : x ≡ 2 mod 3} suﬃce.

Andaloro[3](2000) has improved these to S = {x : x ≡ 1 mod 16}. All of these

sets have an easily computed positive density, the lowest being Andaloro’s set

S at 1/16. Korec and Znam[40](1987) signiﬁcantly improve this by showing the

suﬃciency of the set S = {x : x ≡ a mod pn} where p is an odd prime, a is a

primitive root mod p2, p ̸ |a, and n ∈ ZZ+. This set has density p−n which can be

made arbitrarily small. In a similar vein, Yang[88](1998) proved the suﬃciency

of the set {n : n ≡ 3 + 10
3 (4k − 1) mod 22k+2}

for any ﬁxed k ∈ ZZ+. Korec and Znam also claim to have a suﬃcient set with

density zero, but details were not provided. To this end, a recent result of

Monks[57](2002) is noteworthy. The last section showed how diﬃcult it is to

ﬁnd a usable closed form expression for T (k)(x). If the “+1” was omitted from

the iterations, this would yield T (k)(x) = 3mx/2k, where m is the number of

odd terms in the ﬁrst k iterations of x. Monks[57](2002) has proven that there

are inﬁnitely many “linear versions” of the 3x + 1 problem. An example given
 15

is the map
 R(n) =
 
 1

11 n if 11|n

136
15 n if 15|n and N OT A

5
17 n if 17|n and N OT A

4
5 n if 5|n and N OT A

26
21 n if 21|n and N OT A

7
13 n if 13|n and N OT A

1
7 n if 7|n and N OT A

33
4 n if 4|n and N OT A

5
2 n if 2|n and N OT A

7n otherwise

where N OT A means “none of the above” conditions hold. Monks shows the

3x + 1 problem is true if and only if for every positive integer n the R-orbit of 2n

contains 2. The proof uses Conway’s Fractran language[25](1987) which Conway

used [24](1972) to prove the existence of a similar map whose long-term behavior

on the integers was algorithmically undecidable. Connecting this material back

to suﬃcient sets, one notes that the density of the set {2n : n ∈ ZZ+} is zero

(albeit, one has a much more complicated map).

5 Cycles

Studying the structure of any possible cycles of T has received much attention.

Letting Ω be a cycle of T , and Ωodd, Ωeven denote the odd and even terms

in Ω, one may rearrange the equation
∑

x∈Ω x = ∑

x∈Ω T (x)

to obtain ∑

x∈Ωeven x = ∑

x∈Ωodd x + |Ωodd| .

This was noted by Chamberland[21](1999) and Monks[57](2002).

Using modular arithmetic, Figure 3 indicates the dynamics of integers under

T both in ZZ3 and ZZ4. Since no cycles may have all of its elements of the form
 16

0 mod 3, 0 mod 4, or 3 mod 4, the ﬁgures imply that no integer cycles (except

{0}) have elements of the form form 0 mod 3. Also, the number of terms in

a cycle congruent to 1 mod 4 equals the number congruent to 2 mod 4. This

analysis was presented by Chamberland[21](1999).

An early cycles result concerns a special class of T -cycles called circuits. A

circuit is a cycle which may be written as k odd elements followed by l even

elements. Davison[27](1976) showed that there is a one-to-one correspondence

between circuits and solutions (k, l, h) in positive integers such that

(2k+l − 3k)h = 2l − 1. (1)

It was later shown using continued fractions and transcendental number theory

(see Steiner[71](1977), Rozier[66](1990)) that equation (1) has only the solution

(1, 1, 1). This implies that {1, 2} is the only circuit.

For general cycles of T , B¨ohm and Sontacchi[14](1978) showed that x ∈ ZZ+

is in an n-cycle of T if and only if there are integers 0 ≤ v0 ≤ v1 ≤ · · · ≤ vm = n

such that
 x = 1
2n − 3m
 m−1∑=0 3m−k2vk

A similar result is derived by B. Seifert[68](1988).

Eliahou[30](1993) has given some strong results concerning any non-trivial

cycle Ω of T . Letting Ω0 denote the odd terms in Ω, he showed

log2
 (3 + 1

M
 ) ≤ |Ω|
|Ωo| ≤ log2
 (3 + 1
m
 ) (2)

where m and M are the smallest and largest terms in Ω. Note that for “large”

cycles this implies |Ω|
|Ω0| ≈ log2 3.

Eliahou uses this in conjunction with the Diophantine approximation of log2 3

and the numerical bound m > 240 to show that

|Ω| = 301994a + 17087915b + 85137581c

where a, b, c are nonnegative integers, b ≥ 1 and ac = 0. Similar results were

found by Chisala[22](1994) and Halbeisen and Hungerb¨uhler[35](1997). This
 17

approach was pushed the farthest by Tempkin and Arteaga[75](1997). They

tighten the relations in (2) and use a better lower bound on m to obtain

|Ω| = 187363077a + 272500658b + 357638239c

where a, b, c are nonnegative integers, b ≥ 1 and ac = 0.

It is not apparent how the even-odd dissection of a cycle used in these results

may be extended to a ﬁner dissection of the terms in a cycle, say, mod 4. Related

to this, Brox[17](2000) has proven that there are ﬁnitely many cycles such that

σ1 < 2 log(σ1 + σ3)

where σi equals the number of terms in a cycle congruent to i mod 4.

6 Extending T to Larger Spaces

A common problem-solving technique is to imbed a problem into a larger class

of problems and use techniques appropriate to that new space. Much work has

been done along these lines for the 3x + 1 problem. The subsequent subsections

detail work done in increasingly larger spaces.

6.1 The Integers ZZ

The ﬁrst natural extension of T is to all of ZZ. The deﬁnition of T suﬃces to

cover this case. One soon ﬁnds three new cycles: {0}, {−5, −7, −10}, and the

long cycle
{−17, −25, −37, −55, −82, −41, −61, −91, −136, −68, −34}.

These new cycles could also be obtained (without minus signs) if one considered

the map deﬁne T ′(n) = −T (−n), which corresponds to the “3x − 1” problem.

It is conjectured that these cycles are all the cycles of T on ZZ. This problem

was considered by Seifert[68](1988).
 18

6.2 Rational Numbers with Odd Denominators

Just as the study of the “3x-1” problem of the last subsection is equivalent to

the 3x + 1 problem on ZZ−, Lagarias[46](1990) has extended the 3x + 1 to the

rationals by considering the class of maps

Tk(x) =
 
 3x+k

2 x ≡ 1 (mod 2)

x
2 x ≡ 0 (mod 2)

positive k ≡ ±1 mod 6 with (x, k) = 1. He has shown that cycles for Tk

correspond to rational cycles x/k for the 3x + 1 function T . Lagarias proves

there are integer cycles of Tk for inﬁnitely many k (with estimates on the number

of cycles and bounds on their lengths) and conjectures that there are integer

cycles for all k. Halbeisen and Hungerb¨uhler[35](1997) derived similar bounds

as Eliahou[30](1993) on cycle lengths for rational cycles.

6.3 The Ring of 2-adic Integers ZZ2

The next extension is to the ring ZZ2 of 2-adic integers consisting of inﬁnite

binary sequences of the form

a = a0 + a12 + a222 + · · · =
 ∞∑

j=0 aj2j

where aj ∈ {0, 1} for all non-negative integers j. Congruence is deﬁned by

a ≡ a0 mod 2.

Chisala[22](1994) extends C to ZZ2 but then restricts his attention to the

rationals. He derives interesting restrictions on rational cycles, for example, if

m is the least element of a positive rational cycle, then

m > 2
 ⌈m log2 3⌉
m − 3.

A more developed extension of T , initiated by Lagarias[45](1985), deﬁnes

T : ZZ2 → ZZ2, T (a) :=
  a/2 if a ≡ 0 mod 2

(3a + 1)/2 if a ≡ 1 mod 2
 19

It has been shown (see Mathews and Watts[52](1984) and M¨uller[59](1991))

that the extended T is surjective, not injective, inﬁnitely many times diﬀer-

entiable, not analytic, measure-preserving with respect to the Haar measure,

and strongly mixing. Similar results concerning iterates of T may be found in

Lagarias[45](1985), M¨uller[59](1991),[60](1994) and Terras[77](1976). Deﬁning

the shift map σ : ZZ2 → ZZ2 as

σ(x) =
 
 x−1

2 x ≡ 1 (mod 2)

x
2 x ≡ 0 (mod 2) ,

Lagarias[45](1985) proved that T is conjugate to σ via the parity vector map

Φ−1 : ZZ2 → ZZ2 deﬁned by

Φ−1(x) =
 ∞∑

k=0 2k (T k(x) mod 2),

that is, Φ ◦ T ◦ Φ−1 = σ. Bernstein[11](1994) gives an explicit formula for the

inverse conjugacy Φ, namely

Φ(2d0 + 2d1 + 2d2 + · · ·) = − 1
3 2d0 − 1
9 2d1 − 1
27 2d2 − · · ·

where 0 ≤ d0 < d1 < d2 < . . .. He also shows that the 3x + 1 problem is

equivalent to having ZZ
+ ⊂ Φ ( 1
3 ZZ). Letting Qodd denote the set of rationals

whose reduced form has an odd denominator, Bernstein and Lagarias[12](1996)

proved that the 3x + 1 problem has no divergent orbits if Φ−1(Qodd) ⊂ (Qodd).

Recent developments along these lines have been made by Monks and Yazinski[58](2002).

Since Hedlund[36](1969) proved that the automorphism group of σ is simply

Aut(σ) = {id, V }, where id is the identity map and V (x) = −1 − x, Monks and

Yazinski deﬁne a function Ω as

Ω = Φ ◦ V ◦ Φ−1.

We then have that Ω is the unique nontrivial autoconjugacy of the 3x+1 map, i.e.

Ω ◦ T = T ◦ Ω and Ω2 = id. Coupled with the results of Bernstein and Lagarias,

the authors show that three statements are equivalent: Φ−1(Qodd) ⊂ (Qodd),

Ω(Qodd) ⊂ (Qodd), and no rational 2-adic integer has a divergent T -trajectory.
 20

Monks and Yazinski also extend the results of Eliahou[30](1993) and Lagarias[45](1985)

concerning the density of “odd” points in an orbit. Let κn(x) denote the num-

ber of ones in the ﬁrst n-digits of the parity vector x. If x ∈ Qodd eventually

enters an n-periodic orbit, then

ln(2)
ln(3 + 1/m) ≤ lim
n→∞ κn(x)
n ≤ ln(2)
ln(3 + 1/M )

where m, M are the least and greatest cyclic elements in the eventual cycle. If

x ∈ Qodd diverges, then ln(2)
ln(3) ≤ lim inf
n→∞ κn(x)
n .

Monks and Yazinski deﬁne another extension of T , namely ξ : ZZ2 → ZZ2 as

ξ(x) =
  Ω(x) x ≡ 1 (mod 2)

x

2 x ≡ 0 (mod 2)

and prove that the 3x + 1 problem is equivalent to having the number one in

the ξ-orbit of every positive.

6.4 The Gaussian Integers and ZZ2[i]

Joseph[38](1998) extends T further to Z2[i], deﬁning ˜T as

˜T (α) =
 
 α/2, if α ∈ [0]

(3α + 1)/2, if α ∈ [1]

(3α + i)/2, if α ∈ [i]

(3α + 1 + i)/2, if α ∈ [1 + i]

where [x] denotes the equivalence class of x in ZZ2[i]/2ZZ2[i]. Joseph shows that

˜T is not conjugate to T × T via a ZZ2-module isomorphism, but is topologically

conjugate to T × T . Arguing akin to results of the last subsection, Joseph shows

that ˜T is chaotic (in the sense of Devaney). Kucinski[43](2000) studies cycles

of Joseph’s extension ˜T restricted to the Gaussian integers ZZ[i].

6.5 The Real Line lR

A further extension of T to the real line lR is interesting in that it allows

tools from the study of iterating continuous maps. In an unpublished paper,
 21

Tempkin[76](1993) studies what is geometrically the simplest such extension:

the straight-line extension to the Collatz function C:

L(x) =
  C(x), x ∈ ZZ

C(⌊x⌋) + (x − ⌊x⌋)(C(⌈x⌉) − C(⌊x⌋)), x ̸∈ ZZ

=
  −(5n − 2)x + n(10n − 3), x ∈ [2n − 1, 2n]

(5n + 4)x − n(10n + 7), x ∈ [2n, 2n + 1] .

Tempkin proves that on each interval [n, n+1], n ∈ ZZ+, L has periodic points of

every possible period. Capitalizing on the fact that iterates of piecewise linear

functions are piecewise linear, he also shows that every eventually periodic point

of L is rational, every rational is either eventually periodic or divergent, and

rationals of the form k/5 with k ̸≡ 0 mod 5 are divergent.

Tempkin also mentions a smooth extension to C, namely

E(x) := 7x + 2

4 + 5x + 2
4 cos(π(x + 1))

but conducts no speciﬁc analysis with it. Chamberland[20](1996) studies a

similar extension to T :

f (x) := x
2 cos2 ( πx
2
 ) + 3x + 1
2 sin2 ( πx
2
 )

= x + 1
4 − 2x + 1
4 cos(πx).

Chamberland shows that any cycle on ZZ+ must be locally attractive. By also

showing that the Schwarzian derivative of f is negative on lR+, this implies the

long-term dynamics of almost all points coincides with the long-term dynamics

of the critical points. One quickly ﬁnds that there are two attracting cycles,

A1 := {1, 2}, A2 := {1.192531907 . . ., 2.138656335 . . .}.

Chamberland conjectures that these are the only two attractive cycles of f

on lR+. This is equivalent to the 3x + 1 problem. It is also shown that a

monitonically increasing divergent orbit exists. Chamberland compactiﬁes the

map via the homeomorphism σ(x) = 1/x on [µ1, ∞) (µ1 is the ﬁrst positive
 22

Figure 4: Julia set of Chamberland’s map extended to the complex plane

ﬁxed point of the map f ), yielding a dynamically equivalent map h deﬁned on

[0, µ1] as
 h(x) =
 
 4x

4+x−(2+x) cos(πx) , x ∈ (0, µ1]

0, x = 0 .

Lastly, Chamberland makes statements regarding any general extension of f :

it must have 3-cycle, a homoclinic orbit (snap-back repeller), and a monoton-

ically increasing divergent trajectory. To illustrate how chaos ﬁgures into this

extension, Ken Monks replaced x with z in Chamberland’s map and numerically

generated the ﬁlled-in Julia set. A portion of the set is indicated in Figure 4.

In a more recent paper, Dumont and Reiter[28](2003) produce similar results

for the real extension

f (x) := 1
2
 (3sin
2(πx/2)x + sin2(πx/2)) .

The authors have produced several other extensions, as well as ﬁgures repre-

senting stopping times; see Dumont and Reiter[29](2001).

Borovkov and Pfeifer[15](2000) also show that any continuous extension of T

has periodic orbits of every period by arguing that the map is turbulent: there

exist compact intervals A1 and A2 such that A1 ∪ A2 = f (A1) ∩ f (A2).
 23

6.6 The Complex Plane lC

Letherman, Schleicher and Wood[50](1999) oﬀer the next reﬁnement of this

approach: they extend T to the complex plane with

f (z) := z
2 + 1
2 (1 − cos(πz)) (z + 1
2
 )+ 1
π
 ( 1
2 − cos(πz)) sin(πz)+h(z) sin
2(πz).

Note that the ﬁrst two terms (with z replaced by x) match Chamberland’s

extension. The clear dynamic advantage of this new function is that the set of

critical points on the real line is exactly ZZ. They improve Chamberland’s result

by showing that on [n, n + 1], with n ∈ ZZ+, there is a Cantor set of points that

diverge monotonically. On the complex plane, Letherman et al. use techniques

of complex dynamics to derive results about Fatou components. In particular,

they show that no integer is in a Baker domain (domain at inﬁnity). One

concludes then that any integer either belongs to a super-attracting periodic

orbit or a wandering domain.

7 Generalizations of 3x + 1 Dynamics

There have been many investigations of maps which have similar dynamics to

T but are not extensions of T . Here one is usually changing the function, as

opposed to last section where the space was extended.

Belaga and Mignotte[10](1998) considered the “3x+d” problem, and conjec-

ture that for any odd d ≥ −1 and not divisible by three, all integer orbits enter

a ﬁnite set (hence every orbit is eventually periodic). Note that the “3x − 1”

problem is equivalent to the 3x + 1 problem on the negative integers, considered

in the previous section.

Another obvious generalization is the class of “qx + 1” problems. Steiner[72,

73](1981) extended his cycle results and showed that for q = 5, there is only

one non-trivial circuit (13 → 208 → 13), while q = 7 has no non-trivial circuits.

Franco and Pomerance[32](1995) showed that if q is a Wieferich number2, then

some x ∈ ZZ+ never iterates to one. Crandall[26](1978) conjectured that this is

2An odd integer q is called a Wieferich number if 2l(q) ≡ 1 mod q2, where l(q) is the order
 24

true for any odd q ≥ 5. Wirsching[87](1998) oﬀers a heuristic argument using

p-adic averages that for q ≥ 5, the qx + 1 problem admits either a divergent

trajectory or inﬁnitely-many diﬀerent periodic orbits.

Mignosi[55](1995) looked at a related generalization, namely

Tβ(n) =
  ⌈βn⌉ n ≡ 1 (mod 2)

x

2 n ≡ 0 (mod 2)

for any β > 1 and r ∈ lR. The case β = 3/2 is equivalent to T . Mignosi

conjectures that for any β > 1, there are ﬁnitely many periodic orbits. This is

proven for β = √
2 and a hueristic argument is made that this conjecture holds

for almost all β ∈ (1, 2). Brocco[16](1995) modiﬁes the map to

Tα,r(n) =
  ⌈αn + r⌉ n ≡ 1 (mod 2)

x

2 n ≡ 0 (mod 2)

for 1 < α < 2. He shows for his map that the Mignosi’s conjecture is false if the

interval ((r − 1)/(α − 1), r/(α − 1)) contains an odd integer and α is a Salem

number or a PV number3 .

Matthews and Watts[52, 53](1984,1985) deal with multiple-branched maps

of the form
 T (x) := mix − ri
d , if x ≡ i mod d

where d ≥ 2 is an integer, m0, m1, . . . , md−1 are non-zero integers, and r0, r1, rd−1 ∈

ZZ such that ri ≡ imi mod d. They mirror their earlier results (seen in the

last section) by extending this map to the ring of d-adic integers and show it

is measure-preserving with respect to the Haar measure. Information about

divergent trajectories may be found in Leigh[49](1986) and Buttsworth and

Matthews[18](1990). Ergodic properties of these maps has been studied by

Venturini[80, 82, 83](1982,1992,1997). An encapsulating result of [83](1997)

of 2 in the multiplicative group (ZZ/qZZ). Wiefereich numbers have density one in the odd

numbers.
3A Salem number is a real algebraic number greater than 1 all of whose conjugates z satisfy

|z| ≤ 1, with at least one conjugate satisfying |z| = 1. A Pisot-Vijayaraghavan (PV) number

is a real algebraic number greater than 1 all of whose conjugates z satisfy |z| < 1.
 25

essentially claims that the condition |m0m1 · · · md−1| < 1 gives “converging”

behavior, while divergent orbits may occur if |m0m1 · · · md−1| > 1. A special

class of these maps – known as Hasse functions, which are “closer” to the 3x + 1

map T – have been studied by Allouche[1](1979), Heppner[37](1978), Garcia

and Tal[33](1999) and M¨oller[56](1978), with similar results. A recent survey

of these generalized mappings – with many examples – has been written by

Matthews[54](2002).

Seemingly farther removed from the 3x + 1 problem are results due to

Stolarsky[74](1998) who completely solves a problem of “similar appearance.”

First, recall Beatty’s Theorem which states that if α, β > 1 are irrational and

satisfy 1/α + 1/β = 1, then the sets

A = {⌊nα⌋ : n ∈ ZZ+}, B = {⌊nβ⌋ : n ∈ ZZ+}

form a partition of ZZ+. If α = φ := (1 + √5)/2, we have β = φ2 = (3 + √
5)/2.

Stolarsky considers the map

f (m) =
  ⌈⌈ m

φ2 ⌉φ2⌉ + 1, m ∈ A

⌈ m
φ2 ⌉, m ∈ B .

He proves that f admits a unique periodic orbit, namely {3, 7}. Deﬁning b(n) =

⌊nβ⌋, the set {b(k)(3) : k ∈ ZZ+} – which has density zero – characterizes the

eventually periodic points. All other positive integers have divergent orbits.

The symbolic dynamics are simple: any trajectory has an itinerary of either

Bl(AB)∞ or Bl(AB)kA∞ for some integers k, l ≥ 0.

8 Miscellaneous

Margenstern and Matiyasevich[51](1999) have encoded the 3x + 1 problem as a

logical problem using one universal quantiﬁer and several existential quantiﬁers.

Speciﬁcally, they showed that T (m)(2a) = b for some m ∈ ZZ+ if and only if there

exist w, p, r, s ∈ ZZ+ such that a, b ≤ w and
 4(w + 1)(p + r) + 1

p + r
 
  pw

s
 
  rw

t
  ×
 26

 2w + 1

w
 
  2s + 2t + r + b((4w + 3)(p + r) + 1)

3a + (4w + 4)(3t + 2r + s)
  ×

 p + r

p
 
  3a + (4w + 4)(3t + 2r + s)

2s + 2t + r + b((4w + 3)(p + r) + 1)
  ≡ 1 mod 2.

Gluck and Taylor[34](2002) have studied another “global statistic” besides

the total stopping time function σ∞(n). If σ∞(a1) = p under the map C, the

authors deﬁne a function4 A as

A(a1) = a1a2 + a2a3 + · · · + apa1

a2 + a2 + · · · + a2 .

where a2, a3, . . . , ap are the consecutive C-iterates of a1. For any odd m > 3,

they show that 9

13 < A(m) < 5
7 .

Moreover, these bounds are sharp since

lim
n→∞ A ( 4n − 1
3
 ) = 9
13

and
 lim
k→∞ A
 ( 2k(23k−1 + 1)
3k
 )
 = 5
7 .

Gluck and Taylor also produce a normalized histogram of A for values between

220 and 220+20001, and its randomized counterpart. These two histograms bear

a resemblance, hinting at the stochastic/probabilistic approach to this problem.

Acknowledgement: The author is grateful to Jeﬀ Lagarias and Ken Monks

for sharing some the most recent developments on this problem, and to Ken

Monks and Toni Guillamon i Grabolosa for many helpful suggestions.

References

[1] J.-P. Allouche. Sur la conjecture de “Syracuse-Kakutani-Collatz”. S´eminaire de Th´eorie

des Nombres, 1978–1979, Exp. No. 9, 15 pp., CNRS, Talence, 1979.

4Gluck and Taylor used the symbol C for their new function; to avoid confusion with the

Collatz function C, I am using the symbol A.
 27

[2] J.M. Amigo. Accelerated Collatz Dynamics. Centre de Recerca Matem`atica preprint,

no. 474, July 2001.

[3] P. Andaloro. On total stopping times under 3x + 1 iteration. Fibonacci Quarterly, 38,

(2000), 73–78.

[4] P. Andaloro. The 3x + 1 problem and directed graphs. Fibonacci Quarterly, 40(1),

(2002), 43–54.

[5] S. Andrei, M. Kudlek and R.S. Niculescu. Some Results on the Collatz Problem. Acta

Informatica , 37(2), (2000), 145–160.

[6] D. Applegate and J. Lagarias. Density Bounds for the 3x + 1 Problem. I. Tree-search

method. Mathematics of Computation, 64, (1995), 411–426.

[7] D. Applegate and J. Lagarias. Density Bounds for the 3x + 1 Problem. II. Krasikov-

Inequalities. Mathematics of Computation, 64, (1995), 427–438.

[8] D. Applegate and J. Lagarias. The Distribution of 3x + 1 Trees. Experimental Mathe-

matics, 4(3), (1995), 193–209.

[9] D. Applegate and J. Lagarias. Lower Bounds for the Total Stopping Time of 3x + 1

Iterates. Mathematics of Computation, 72(242), (2002), 1035–1049.

[10] E. Belaga and M. Mignotte. Embedding the 3x + 1 Conjecture in a 3x + d Context.

Experimental Mathematics, 7(2), (1998), 145–151.

[11] D. Bernstein. A Non-iterative 2-adic Statement of the 3N + 1 Conjecture . Proceedings

of the American Mathematical Society, 121, (1994), 405–408.

[12] D. Bernstein and J. Lagarias. The 3x + 1 Conjugacy Map. Canadian Journal of

Mathematics, 48, (1996), 1154–169.

[13] R. Blecksmith, M. McCallum and J. Selfridge. 3-Smooth Representations of Integers.

American Mathematical Monthly, 105(6), (1998), 529–543.

[14] C. B¨ohm and G. Sontacchi. On the Existence of Cycles of given Length in Integer

Sequences like xn+1 = xn/2 if xn even, and xn+1 = 3xn + 1 otherwise. Atti della

Accademia Nazionale dei Lincei. Rendiconti. Classe di Scienze Fisiche, Matematiche e

Naturali. Serie VIII , 64, (1978), 260–264.

[15] K. Borovkov and D. Pfeifer. Estimates for the Syracuse Problem via a Probabilistic

Model. Theory Probab. Appl., 45, (2000), 300–310.
 28

[16] S. Brocco. A note on Mignosi’s generalization of the (3X + 1)-problem. Journal of

Number Theory, 52(2), (1995), 173–178.

[17] T. Brox. Collatz Cycles with Few Descents. Acta Arithmetica, 92(2), (2000), 181–188.

[18] R. Buttsworth and K. Matthews. On some Markov matrices arising from the generalized

Collatz mapping . Acta Arithmetica, 55(1), (1990), 43–57.

[19] C. Cadogan. A Note on the 3x + 1 Problem. Caribbean Journal of Mathematics, 3,

(1984), 67–72.

[20] M. Chamberland. A Continuous Extension of the 3x + 1 Problem to the Real Line.

Dynamics of Continuous, Discrete and Impulsive Systems, 2, (1996), 495–509.

[21] M. Chamberland. Announced at the “Roundatable Discussion”, International Confer-

ence on the Collatz Problem and Related Topics, August 5-6, 1999, Katholische Univer-

sit¨at Eichst¨att, Germany .

[22] B. Chisala. Cycles in Collatz Sequences. Publicationes Mathematicae Debrecen, 45,

(1994), 35–39.

[23] K. Conrow. http : //www − personal.ksu.edu/~ kconrow/gentrees.html.

[24] J. Conway. Unpredictable Iterations. Proceedings of the Number Theory Conference

(University of Colorado, Boulder), (1972), 49–52.

[25] J. Conway. FRACTRAN: A Simple Universal Programming Language for Arithmetic.

Open Problems in Communication and Computation (Ed. T.M. Cover and B. Gopinath),

Springer, New York, (1987), 4–26.

[26] R.E. Crandall. On the “3x + 1” Problem. Mathematics of Computation, 32, (1978),

1281–1292.

[27] J. Davison. Some Comments on an Iteration Problem. Proceedings of the Sixth

Manitoba Conference on Numerical Mathematics , (1976), 155–159.

[28] J. Dumont and C. Reiter. Real Dynamics Of A 3-Power Extension Of The 3x + 1

Function. Dynamics of Continuous, Discrete and Impulsive Systems, (2003), to appear.

[29] J. Dumont and C. Reiter. Visualizing Generalized 3x+1 Function Dynamics. Computers

& Graphics, 25(5), (2001), 883–898.

[30] S. Eliahou. The 3x + 1 Problem: New Lower Bounds on Nontrivial Cycle Lengths.

Discrete Mathematics, 118, (1993), 45–56.
 29

[31] C.J. Everett. Iteration of the Number-Theoretic Function f (2n) = n, f (2n+1) = 3n+2.

Advances in Mathematics, 25, (1977), 42–45.

[32] Z. Franco and C. Pomerance. On a Conjecture of Crandall concerning the qx + 1

Problem. Mathematics of Computation, 64(211), (1995), 1333–1336.

[33] M. Garcia and F. Tal. A Note on the Generalized 3n + 1 Problem. Acta Arithmetica,

90(3), (1999), 245–250.

[34] D. Gluck and B. Taylor. A New Statistic for the 3x + 1 Problem. Proceedings of the

American Mathematical Society, 130(5), (2002), 1293–1301.

[35] L. Halbeisen and N. Hungerb¨uhler. Optimal Bounds for the Length of Rational Collatz

Cycles. Acta Arithmetica, 78(3), (1997), 227–239.

[36] G. Hedlund. Endomorphisms and Automorphisms of the Shift Dynamical System.

Mathematical Systems Theory, 3, (1969), 320–375.

[37] E. Heppner. Eine Bemerkung zum Hasse-Syracuse Algorithmus. Archiv der Mathe-

matik, 31(3), (1978), 317–320.

[38] J. Joseph. A Chaotic Extension of the 3x + 1 Function to Z2[i]. Fibonacci Quarterly,

36(4), (1998), 309–316.

[39] I. Korec. A Density Estimate for the 3x + 1 Problem. Mathematica Slovaca, 44(1),

(1994), 85–89.

[40] I. Korec and ˇS. Zn´am. A Note on the 3x+1 Problem. American Mathematical Monthly,

94, (1987), 771–772.

[41] I. Krasikov. How many numbers satisfy the 3X + 1 conjecture? International Journal

of Mathematics and Mathematical Sciences , 12, (1989), 791–796.

[42] I. Krasikov and J. Lagarias. Bounds for the 3x+1 Problem using Diﬀerence Inequalities.

arXiv:math.NT/0205002 v1, April 30, 2002.

[43] G. Kucinski. Cycles of the 3x + 1 Map on the Gaussian Integers. Preprint dated May,

2000.

[44] J. Kuttler. On the 3x + 1 Problem. Advances in Applied Mathematics, 15, (1994),

183–185.

[45] J. Lagarias. The 3x + 1 Problem and its Generalizations. American Mathematical

Monthly, 92, (1985), 1–23. Available online at www.cecm.sfu.ca/organics/papers.
 30

[46] J. Lagarias. The Set of Rational Cycles for the 3x + 1 Problem. Acta Arithmetica, 56,

(1990), 33–53.

[47] J. Lagarias and A. Weiss. The 3x + 1 Problem; Two Stochastic Models. Annals of

Applied Probability, 2, (1992), 229–261.

[48] J. Lagarias. 3x + 1 Problem Annotated Bibliography.

http://www.research.att.com/ ˜ jcl/doc/3x+1bib.ps, July 26, 1998.

[49] G.M. Leigh. A Markov process underlying the generalized Syracuse algorithm. Acta

Arithmetica, 46(2), (1986), 125–143.

[50] S. Letherman, D. Schleicher, and R. Wood. The 3n + 1-Problem and Holomorphic

Dynamics. Experimental Mathematics, 8(3), (1999), 241–251.

[51] M. Margenstern and Y. Matiyasevich. A binomial representation of the 3x + 1 problem.

Acta Arithmetica, 91(4), (1999), 367–378.

[52] K. Matthews and A.M. Watts. A Generalization of Hasse’s Generalization of the Syra-

cuse Algorithm. Acta Arithmetica, 43(2), (1984), 167–175.

[53] K. Matthews and A.M. Watts. A Markov Approach to the generalized Syracuse Algo-

rithm. Acta Arithmetica, 45(1), (1985), 29–42.

[54] K. Matthews. http : //www.maths.uq.edu.au/~ krm, August 15, 2002.

[55] F. Mignosi. On a generalization of the 3x + 1 problem. Journal of Number Theory,

55(1), (1995), 28–45.

[56] H. M¨oller. ¨Uber Hasses Verallgemeinerung des Syracuse-Algorithmus (Kakutanis Prob-

lem). Acta Arithmetica, 34(3), (1978), 219–226.

[57] K. Monks. 3x + 1 Minus the +. Discrete Mathematics and Theoretical Computer

Science, 5(1), (2002), 47–54.

[58] K. Monks and J. Yazinski. The Autoconjugacy of the 3x + 1 Function. Discrete

Mathematics, to appear.

[59] H. M¨uller. Das ‘3n + 1’ Problem. Mitteilungen der Mathematischen Gesellschaft in

Hamburg, 12, (1991), 231–251.

[60] H. M¨uller. ¨Uber eine Klasse 2-adischer Funktionen im Zusammenhang mit dem ‘3x + 1’-

Problem. Abhandlungen aus dem Mathematischen Seminar der Universit¨at Hamburg ,

64, (1994), 293–302.
 31

[61] T. Oliveira e Silva. Maximum excursion and stopping time record-holders for the 3x + 1

problem: computational results. Mathematics of Computation, 68(225), (1999), 371–384.

[62] T. Oliveira e Silva. http : //www.ieeta.pt/~ tos/3x + 1.html.

[63] S. Puddu. The Syracuse Problem (spanish). Notas de la Sociedad de Matemtica de

Chile , 5, (1986), 199-200.

[64] D. Rawsthorne. Imitation of an Iteration. Mathematics Magazine, 58, (1985), 172–176.

[65] E. Roosendaal. http : //personal.computrain.nl/eric/wondrous/ .

[66] O. Rozier. D´emonstration de l’absense de cycles d’une certain forme pour le Probl`eme

de Syracuse. Singularit´e, 1, (1990), 9–12.

[67] J. Sander. On the (3N + 1)-Conjecture. Acta Arithmetica, 55, (1990), 241–248.

[68] B. Seifert. On the Arithmetic of Cycles for the Collatz-Hasse (‘Syracuse’) Problem.

Discrete Mathematics, 68, (1988), 293–298.

[69] D. Shanks. Comments on Problem 63-13. SIAM Review, 7, (1965), 284–286.

[70] Y. Sinai. Statistical (3x+1) - Problem. Communications on Pure and Applied Mathe-

matics, 56(7), (2003), 1016–1028.

[71] R. Steiner. A Theorem on the Syracuse Problem. Proceedings of the Seventh Manitoba

Conference on Numerical Mathematics and Computing , (1977), 553–559.

[72] R. Steiner. On the “QX + 1 problem”, Q odd. Fibonacci Quarterly, 19(3), (1981),

285–288.

[73] R. Steiner. On the “QX + 1 problem”, Q odd. II. Fibonacci Quarterly, 19(4), (1981),

293–296.

[74] K. Stolarsky. A Prelude to the 3x + 1 Problem. Journal of Diﬀerence Equations and

Applications, 4, (1998), 451–461.

[75] J. Tempkin and S. Arteaga. Inequalities Involving the Period of a Nontrivial Cycle of

the 3n + 1 Problem. Draft of Circa October 3, 1997.

[76] J. Tempkin. Some Properties of Continuous Extensions of the Collatz Function. Draft

of Circa October 5, 1993.

[77] R. Terras. A Stopping Time Problem on the Positive Integers. Acta Arithmetica, 30,

(1976), 241–252.
 32

[78] R. Terras. On the Existence of a Density. Acta Arithmetica, 35, (1979), 101–102.

[79] T. Urvoy. Regularity of congruential graphs. Mathematical foundations of computer

science 2000 (Bratislava), 680–689, Lecture Notes in Computer Science, 1893, Springer,

Berlin, (2000), see also http : //www.irisa.fr/galion/turvoy/ .

[80] G. Venturini. Behavior of the iterations of some numerical functions. (Italian). Is-

tituto Lombardo. Accademia di Scienze e Lettere. Rendiconti. Scienze Matematiche e

Applicazioni. A , 116, (1982), 115–130.

[81] G. Venturini. On the 3x + 1 problem. Advances in Applied Mathematics, 10(3), (1989),

344–347.

[82] G. Venturini. Iterates of number-theoretic functions with periodic rational coeﬃcients

(generalization of the 3x + 1 problem). Studies in Applied Mathematics, 86(3), (1992),

185–218.

[83] G. Venturini. On a generalization of the 3x + 1 problem. Advances in Applied Mathe-

matics, 19(3), (1997), 295–305.

[84] S. Wagon. The Collatz Problem. Mathematical Intelligencer, 7(1), (1985), 72–76.

[85] G. Wirsching. An Improved Estimate concerning 3n + 1 Predecessor Sets. Acta Arith-

metica, 63, (1993), 205–210.

[86] G. Wirsching. A Markov Chain underlying the Backward Syracuse Algorithm. Revue

Roumaine de Math´ematiques Pures et Appliqu´ees, 39, (1994), 915–926.

[87] G. Wirsching. The Dynamical System Generated by the 3n + 1 Function. Springer,

Heidelberg, (1998)

[88] Z.H. Yang. An Equivalent Set for the 3x + 1 Conjecture. Journal of South China Normal

University, Natural Science Edition, no.2, (1998), 66–68.

[89] R. Zarnowski. Generalized Inverses and the Total Stopping Times of Collatz Sequences.

Linear and Multilinear Algebra, 49(2), (2001), 115–130.
