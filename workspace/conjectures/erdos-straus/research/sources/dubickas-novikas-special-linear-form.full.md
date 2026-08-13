<!-- source: https://epublications.vu.lt/object/elaba:2089125/2089125.pdf | converted from PDF -->

VILNIUS UNIVERSITY

AIVARAS NOVIKAS

COMPOSITE NUMBERS IN THE SEQUENCES OF INTEGERS

Doctoral dissertation

Physical sciences, mathematics (01P)

Vilnius, 2012

The scientiﬁc work was carried out in 2008–2012 at Vilnius University.

Scientiﬁc supervisor:

prof. habil. dr. Art¯uras Dubickas (Vilnius University, physical sciences, mathe-

matics – 01P)

Scientiﬁc adviser:

prof. dr. Ram¯unas Garunkˇstis (Vilnius University, physical sciences, mathematics

– 01P)
 VILNIAUS UNIVERSITETAS

AIVARAS NOVIKAS

SUD ˙ETINIAI SKAI ˇCIAI SVEIKU¸ JU¸ SKAI ˇCIU¸ SEKOSE

Daktaro disertacija

Fiziniai mokslai, matematika (01P)

Vilnius, 2012 metai

Disertacija rengta 2008–2012 metais Vilniaus universitete.

Mokslinis vadovas:

prof. habil. dr. Art¯uras Dubickas (Vilniaus universitetas, ﬁziniai mokslai, mate-

matika – 01P)

Konsultantas:

prof. dr. Ram¯unas Garunkˇstis (Vilniaus universitetas, ﬁziniai mokslai, matema-

tika – 01P)
 Contents

Notation 6

Introduction 7

Actuality 7

Aims and problems 8

Methods 9

Novelty and approbation 9

Principal publications 9

Other publications 10

Acknowledgments 10

Review and main results 11

1. Integer parts of powers of rational numbers 24

1.1. Preliminary considerations 26

1.2. Two lemmas: the periodicity of the sequences of operations 28

1.3. Proof of Theorem 1.1: easy cases 29

1.4. The case a = 5/4 30

1.5. The case a = 5 and Proposition 1.2 37

1.6. Composite numbers in the sequences of shifted integer parts 38

2. Binary linear recurrence sequences 41

2.1. Several exceptional cases 44

2.2. The case |b| ⩾ 2 46

2.3. Divisibility sequences, covering systems and the case |b| = 1 51

3. Egyptian fractions and numbers expressible by a special

linear form 57

3.1. Proofs 61

Conclusions 64

References 66

5

Notation

N the set of all positive integers

Z the set of all integers

Q the set of all rational numbers

R the set of all real numbers

C the set of all complex numbers

[x] an integer part of x

{x} a fractional part of x

N
2 the set of all non-zero perfect squares

Fq the Galois ﬁeld of order q
( a
p ) the Jacobi symbol

K(α) the algebraic extension of the ﬁeld K

6

Introduction

The topics examined in this thesis were the subject of my research as a PhD

student at the Faculty of Mathematics and Informatics of Vilnius University. The

presented investigation concerns the existence of composite numbers in some spe-

cial sequences, such as the sequence of integer parts of powers of a ﬁxed number

and a linear recurrence sequence consisting of integer numbers.

Actuality. In number theory, the distinction between prime and composite num-

bers plays a crucial role. It was understood already in antiquity and the distinc-

tion grew in importance with number theory evolving as a separate large branch of

mathematics in the new times. Prime and composite numbers were examined in

the context of divisibility properties of integers (e.g., by Euclid in his ”Elements”

and much later by Fermat, Euler, etc.)

At the same time the interest of mathematicians shifted to examination of

integer numbers of special form and determining whether they can be prime or

composite. Fermat’s conjecture that all numbers of the form 2
2n +1 are prime was

soon disproved by Euler. However, many problems of this kind are very diﬃcult

and even remain unsolved to this day due to ”irregular” pattern of the prime and

composite numbers in the sequence of positive integers (e.g., the four Landau’s

problems). As such, they occupy a deserved position in contemporary number

theory.

In this thesis we search for composite numbers in the sequence of integer parts of

powers of a ﬁxed number. Although questions related to these sequences and also

to the similar sequences of fractional parts have been studied by many scientists

some important problems remain out of reach: e.g., the distribution of fractional

parts in even the seemingly most simple cases and existence of inﬁnitely many

prime numbers in the sequences of integer parts. The question of distribution of

the fractional parts is, on the one hand, related to the behaviour of the integer

parts, and, on the other hand, (in the case of the integer powers of the number

3/2) to such famous subjects as Waring’s problem.

7

The actuality of particular problems is further discussed in detail in the section

”Review and main results”.

Aims and problems. The most general aim of this thesis is to determine the

existence and properties of composite numbers in some special sequences of inte-

gers, also to construct sequences of some special form consisting of only composite

numbers. To be precise, the following questions are considered:

• For which rational numbers a > 1 and real numbers ξ > 0, does the

sequence
 [ξan], n = 1, 2, . . . ,

of integer parts contain inﬁnitely many composite numbers?

• If the sequence
 [ξan], n = 1, 2, . . . ,

contains inﬁnitely many composite numbers, then is it possible to indicate

a ﬁnite set of prime numbers at least one of which divides inﬁnitely many

of those composite numbers?

• For which ”shifted” sequences

[ξan + ν], n = 1, 2, . . . ,

where ν ∈ R, can the ﬁrst two questions be answered? Can one indi-

cate iniﬁnitely many values of ν for which such a sequence would contain

inﬁnitely many composite numbers for some certain a and any ξ > 0?

• For which binary linear recurrence equations

xn+1 = axn + bxn−1,

where a, b ∈ Z, does there exist a corresponding binary linear recurrence

sequence of integers whose two initial terms are positive and relatively

prime and which consists of only composite numbers (the absolute values

of the terms being taken)?

• Let t be a ﬁxed positive integer. Which numbers belong to the set E(t) =

{n ∈ N : n = tM − d}, where M is a positive multiple of the product and

d is a positive divisor of the sum of two positive integers a and b?

8

Methods. A variety of methods is applied in this thesis. In Section 1 we improve

the achievements of Forman and Shapiro [14] not only reducing the length of their

proofs, but also producing a series of new results, based on the examination of

the behaviour and mutual relations between fractional parts of powers of rational

numbers as well as their integer parts and avoiding initial assumption of the ”proof

by contradiction” method. This allows us to prove the most diﬃcult case of the

main Theorem 1.1 in Section 1.4 by using established divisibility properties of the

terms of the sequence to determine combinatorial properties of the sequences of

operations, interpreted as formal sequences of symbols. In Section 2 we apply

the concept of covering systems introduced by Erd˝os to the linear recurrence

sequences consisting of integer terms. In Section 3 we examine a special linear

form whose relation to the Egyptian fractions and some minor facts about it

established by us allows us to state a conjecture, which is tested by computer

calculations. Throughout the thesis such classical number theory subjects as

Chinese remainder theorem, Dirichlet’s theorem on arithmetical progressions and

Jacobi symbol are also occasionally used. See the introductory parts of Sections

1, 2 and 3 for more details.

Novelty and approbation. All research represented in this thesis is original.

The main results have been published in the refereed journals (see ”Principal

publications”). They were also presented at the international conference ”27th

Journ´ees Arithm´etiques” (Vilnius, Lithuania, 2011), at the Conference of Lithua-

nian Mathematical Society and the seminar of the Department of Probability

Theory and Number Theory of the Faculty of Mathematics and Informatics of

Vilnius University.

Principal publications. The main results of the thesis are published in the

following papers:

• A. Dubickas and A. Novikas, Integer parts of powers of rational num-

bers, Math. Zeitschrift, 251 (2005), 635–648.

9

• A. Dubickas, A. Novikas and J. ˇSiurys, A binary linear recurrence

sequence of composite numbers, J. Number Theory, 130 (8) (2010), 1737–

1749.

• A. Dubickas and A. Novikas, On integers expressible by some special

linear form, Acta Math. Univ. Comen., New Ser., 9 p. (to appear).

Other publications. Preprints and conference abstracts:

• Integer parts of powers of rational numbers, Preprint 2004–44, Vilnius

University, Faculty of Mathematics and Informatics 2004, 14 p. (with

A. Dubickas)

• A binary linear recurrence sequence of composite numbers, 27th Journ´ees

Arithm´etiques, Vilnius, Lithuania, June 27 – July 1, 2010: Abstracts,

http://atlas-conferences.com/c/b/b/v/22.htm (with J. ˇSiurys)

• Some remarks on the composition of competition problems, The 9th In-

ternational conference ”Teaching mathematics: retrospective and perspec-

tives”, Vilnius, Lithuania, May 16 – May 17, 2008: Abstracts

Acknowledgments. I would like to express my sincere gratitude to my super-

visor Professor Art¯uras Dubickas. I am highly indebted to him for his valuable

guidance, encouragement and advice.

I am also very thankful to my school teacher Antanas Sk¯upas and my university

teacher Hamletas Markˇsaitis, whose enthusiastic instruction and friendly attitude

was very inspiring and contributed much to my involvement in mathematical

research.

Finally, I would like to thank everyone, whose constant support, fruitful colla-

boration or mere joyful moments of life accompanied me through the mathematical

journey, notably Romualdas Kaˇsuba, as well as Juozas Maˇcys, Paulius ˇSarka,

Paulius Drungilas, Jonas Jankauskas, Jonas ˇSiurys and my other colleagues and

co-workers at the Department of Probability Theory and Number Theory and the

Department of Methodics of Mathematics and Informatics of the Faculty where

this PhD thesis was written.
 10

Review and main results. We start with some basic deﬁnitions. For any real

number x, the biggest integer not exceeding x we will call an integer part of x and

denote it by [x]. The number {x} = x − [x] is called a fractional part of x. We

deﬁne a prime number as a positive integer which has exactly two distinct positive

integer divisors and a composite number as a positive integer which has at least

three distinct positive integer divisors (i.e., it is not a prime number and is not

equal to 1). Denote by Z, N, Q, R, C the sets of all integers, positive integers,

rational numbers, real numbers and complex numbers, respectively.

Below, we present the research and our results related to

• the composite numbers in the sequences of integer parts of powers of ra-

tional numbers,

• the composite numbers in the binary linear recurrence sequences,

• the Egyptian fractions.

Integer parts of powers of rational numbers

There are many unsolved problems concerning the distribution of the fractional

parts of powers of a rational number a > 1. The sequence {an}, n = 1, 2, . . . ,

and, more generally, the sequence {ξan}, n = 1, 2, . . . , where ξ is a ﬁxed positive

number, was studied by Vijayaraghavan [34]. He proved the following:

The set of limit points of the sequence {(p/q)n}, n = 1, 2, . . . , where p > q > 1

are integers satisfying gcd(p, q) = 1, is inﬁnite.

The generalization of this proposition was proved by Pisot [27] (and later by

Dubickas, in a diﬀerent way [11]). Before stating it we recall what is a Pisot-

Vijayaraghavan number (or a PV number). Firstly, a number α ∈ C is called an

algebraic integer if it is a root of an irreducible monic polynomial with integer

coeﬃcients. Other roots of that polynomial are called conjugates of α. The

number α ∈ C is called a Pisot-Vijayaraghavan number if it is a real algebraic

integer greater than 1 such that all its conjugates are smaller than 1 in absolute

value. Now we proceed with the generalized statement:

Let α > 1 be an algebraic number and let ξ > 0 be a real number. Then the set

{ξαn}, n ∈ N, has only ﬁnitely many limit points if and only if α is a PV-number

and ξ ∈ Q(α).
 11

Despite these results, it remains unproved that the sequence {(3/2)
n}, n =

1, 2, . . . , has inﬁnitely many limit points in [0, 1/2) or in [1/2, 1]. Flatto, Lagarias

and Pollington [13] have made a step towards (see also [5] for other achievements

in this direction) by proving the inequality

lim sup
n→∞ {(3/2)
n} − lim inf
n→∞ {(3/2)
n} ⩾ 1/3.

It would suﬃce to prove that lim supn→∞ {(3/2)
n} − lim inf n→∞ {(3/2)
n} > 1/2.

Let us consider a more general case of the sequence {(ξ/2)an}, n ∈ N, where ξ > 0

and a ∈ Q, a > 1, are some ﬁxed numbers. Clearly, if one could prove that the

distance between the largest limit point of {(ξ/2)a
n}, n ∈ N, and the smallest one

is greater than 1/2, then the smallest limit point is smaller than 1/2. This would

imply that there are inﬁnitely many even numbers among [ξan], n ∈ N, which is

the matter of our direct concern in this thesis. However, it is only known [13]

that this distance is ⩾ 1/b, where b is the numerator of a = b/c ∈ Q, b > c > 1,

(b, c) = 1, which, although being a remarkable result itself, cannot be used to

achieve our aims.

Hence, the question of distribution in even the simplest case of a = 3/2 is far

from being understood; its importance is usually motivated by a remarkable con-

nection between the distribution of {(3/2)
n}, n = 1, 2, . . . , and Waring’s problem.

(See, for instance, [33].) Essentially, Waring’s problem has been solved by Hilbert

who proved the following:

Every positive integer is the sum of a ﬁxed number g(n) of nth powers of non-

negative integers, where n is any given positive integer and g(n) depends only on

n.
 However, the question of expressing the smallest possible g(n) by a formula

depends on the properties of {(3/2)
n} which still remain to be determined.

Some metrical results on the distribution of the fractional parts are well-known.

Koksma [21] proved that

The sequence {ξan}, n = 1, 2, . . . , where ξ > 0, is uniformly distributed in [0, 1]

for almost all a > 1.

This implies that, for almost all a > 1, [an] are composite for inﬁnitely many n

(see [14]). Baker and Harman [2] obtained other metrical results in this direction.

Unfortunately, it is impossible to apply these results to rational numbers, because

12

the set of rational numbers is of measure zero. To indicate certain values of a for

which [an] are composite for inﬁnitely many n also presents a challenge.

In [22] Mahler asked the following question:

Is there a positive number α such that the numbers {α(3/2)
n}, n ∈ N, are all

smaller than 1/2?

This question is equivalent to another one: is there a positive number ξ(= 2α)

such that the numbers [ξ(3/2)
n], n ∈ N, are all even? Mahler’s question remains

unsolved. Our Theorem 1.1 shows that, for every ξ > 0, the set [ξ(3/2)n], n ∈ N,

contains inﬁnitely many elements divisible by one of the numbers 2, 5, 7, 11.

There is not too much information about a > 1 for which [an] is prime for

inﬁnitely many integers n. See, for instance, [1], [2], [23], [37] for some existence

results in this direction. In [2] Baker and Harman prove that

The sequence [an], n = 1, 2, . . . , contains inﬁnitely many primes for almost all

a > 1.

However, no certain value of a is indicated by them. Mills [23] proved the

existence of such a number A that an integer part [A
3n] is prime for any n ∈ N.

According to a conjecture of Whiteman (see Problem E19 in [17]) the sequence

[an], n = 1, 2, . . . , where a > 1 is a rational noninteger number, contains inﬁnitely

many primes. However, no results are known to conﬁrm this statement.

We are interested in a problem for which the cases a = 3/2 and a = 4/3 were

successfully treated more than forty years ago by Forman and Shapiro [14], but

no progress has been made since then for a long time. This at ﬁrst glance simple

problem can be stated as follows: prove that for every rational a > 1 the sequence

of integer parts [an] contains inﬁnitely many composite numbers. (This problem

is trivial for integer a.)

Very few explicit irrational a > 1 producing inﬁnitely many composite numbers

are known. Cass [7] proved that

The set [an], n ∈ N, contains inﬁnitely many composite numbers if a > 1 is a

unit in a real quadratic number ﬁeld.

(By a unit in a real quadratic number ﬁeld we mean a invertible element in the

ring of algebraic integers of the real algebraic extension of Q of the second order.)

This result was extended by Dubickas [8] to all Pisot-Vijayaraghavan and Salem

numbers a :
 13

The set [an], n ∈ N, contains inﬁnitely many composite numbers if a > 1 is a

Pisot-Vijayaraghavan or a Salem number.

(Every real quadratic unit is a Pisot number of degree 2. See also [10] for a

generalization. By a Salem number we mean a real algebraic integer greater than

1 such that all its conjugates are not greater than 1 in absolute value and at least

one of them is equal to 1 in absolute value.) Some explicit transcendental a > 1

for which [an] are composite inﬁnitely often were constructed in [1].

As for the rational numbers, our result below concerning composite numbers in

the case of a = 2 has been recently improved by Dubickas [9]:

For any real numbers ξ ̸= 0 and ν, the sequence of integer parts [ξ2
n + ν], n =

1, 2, ..., contains inﬁnitely many composite numbers. Moreover, if the number ξ is

irrational, then the above sequence contains inﬁnitely many elements divisible by

2 or 3.

We are able to extend the result of [14]. We begin with our main theorem.

Set P(2) = {2}, P(3) = P(4) = {2, 3}, P(6) = P(4/3) = {2, 3, 5}, P(3/2) =

{2, 5, 7, 11}, P(5/4) = {2, 3, 7, 11, 13}.

Theorem 1.1. Let ξ > 0 be a real number and let a ∈ {2, 3, 4, 6, 3/2, 4/3, 5/4}.

Then the set [ξan], n ∈ N, contains inﬁnitely many elements divisible by at least

one number of the set P(a).

In the above mentioned paper [14] Forman and Shapiro proved that the sets

[(3/2)
n] and [(4/3)n], n ∈ N, contain inﬁnitely many composite numbers. Their

proof extends without change to [ξ(3/2)
n] and [ξ(4/3)
n] with arbitrary ξ > 0.

However, we will give a proof for a = 4/3 once again, because (after a small

preparation) we will be able to do this in just few lines in contrast to eight lemmas

used in [14]. This will serve as a warm-up for the proof of a corresponding result

for a = 5/4. The proof of Theorem 1.1 for a = 3/2 is given by combining our

Lemma 1.7 with the main result of [14].

A valuable diﬀerence between our approach and that of [14] is that we are seek-

ing a contradiction with Lemma 1.7 below which is obtained using fractional parts

rather than a similar lemma for the integer parts of powers as in [14]. The main

advantage in doing this is that we are able to describe some explicit (unavoidable)

ﬁnite sets for possible divisors. (We show, however, that such unavoidable sets do

not exist for some rational a; see the Proposition below.)

14

Note that the number a = 5 is missing in Theorem 1.1. The only reason for

this is that, for a = 5, such universal explicit (unavoidable) set for divisors of the

elements of the set [ξ5
n], n ∈ N, cannot be given. In fact, it cannot be given for

any number a = 4k + 1, where k ∈ N.

Proposition 1.2. Let a be a positive integer of the form 4k + 1, where k ∈ N,

and let P be an arbitrary ﬁnite set of prime numbers. Then there exists ξ > 0

such that every integer part [ξan], n = 1, 2, . . . , is relatively prime with every

prime number of the set P.

We prove Proposition 1.2 in Section 1.4. However, in the same section we prove

that the set [ξ5
n], n ∈ N, contains inﬁnitely many composite numbers since a

universal set of divisors does not work only for special values of ξ, which we are

able to deal with separately. The fact is a direct consequence of the following

theorem.

Theorem 1.3. Let ξ > 0 be a real number. If ξ ̸= (4k + 3)/(2 · 5
r), where

k, r are nonnegative integers, then the set [ξ5
n], n ∈ N, contains inﬁnitely many

elements divisible by 2, 3 or 5. If ξ = (4k + 3)/(2 · 5
r), where (4k + 3, 5
r) = 1, then

the set [ξ5
n], n ∈ N, contains inﬁnitely many elements divisible by 10k + 7.

It remains unproved that the integer parts [ξan], n = 1, 2, . . . , where ξ is an

arbitrary positive number and a ⩾ 7 is an integer, are composite for inﬁnitely

many n ∈ N. Also, Theorem 1.1 has not been extended to any rational noninteger

number other than 3/2, 4/3, 5/4 even for ξ = 1, although at ﬁrst glance the case

a = 6/5 may seem simpler than the case a = 5/4. However, by slightly changing

the problem, we can include some new rational numbers.

Theorem 1.4. Let ξ > 0 be a real number. Then each of the sets [ξ(5/2)
n] − 1

and [ξ(6/5)
n] − 1, where n ∈ N, contains inﬁnitely many elements divisible by at

least one number of the set {2, 3, 5}.

The proof for [ξ(5/2)
n] − 1 presented in Section 1.6 can be applied without

changes to all the sets of numbers the form [ξ(5/2)
n] − 1 + 30k, n ∈ N, where k is

any ﬁxed integer.
 15

One can also consider the nearest integers to powers instead of integer parts.

We deﬁne the nearest integer to z as [z +1/2]. Some new numbers can be obtained

again.

Theorem 1.5. Let ξ > 0 be a real number. Then

(i) the set [ξ7
n + 1/2], n ∈ N, contains inﬁnitely many composite numbers,

(ii) the set [ξ(5/3)n + 1/2], n ∈ N, contains inﬁnitely many elements divisible by

2 or 3,

(iii) the set [ξ(7/5)n + 1/2], n ∈ N, contains inﬁnitely many elements divisible by

at least one of the numbers 2, 3, 5, 11.

Note that no deﬁnite divisors are indicated for the set [ξ7
n + 1/2], n ∈ N. This

case is diﬀerent from all the other cases for the reason that it is not covered by

Lemma 1.2 which holds only for non-integer rational numbers (as in the case

a = 5) and, in contrast to the case a = 5, integer parts are used to ﬁnish the

proof instead of fractional parts (which are instrumental in excluding most of the

values of ξ in the proof of Theorem 1.3).

In Section 1.1 we deﬁne the sequences of operations which describe the be-

haviour of the sequences of integer parts, but which can also be viewed as inﬁnite

words, i.e. formal sequences of symbols belonging to some set, called an alphabet.

We will study the patterns which could and could not occur in these words and

the possible periodicity of these sequences of symbols, as well.

Binary linear recurrence sequences

A sequence of real numbers xn, n = 1, 2, . . . , is called a linear recurrence se-

quence if its terms satisfy the recurrence

xn+d = a1xn+d−1 + a2xn+d−2 + · · · + adxn, n = 1, 2, 3, . . . ,

for some ﬁxed numbers d ∈ N and a1, a2, . . . , ad ∈ R. The number d is called an

order of the linear recurrence sequence under the natural assumption that ad ̸= 0.

Our results concern the order 2 (or binary) linear recurrence sequences consist-

ing of integers. The best-known example of a binary linear recurrence sequence

is the Fibonacci sequence, given by F1 = F2 = 1 and the recurrence relation

Fn+1 = Fn + Fn−1 for n ⩾ 2.
 16

The question of determining prime and composite numbers in a linear recurrence

sequence is an old one. For instance, it is not known if there are inﬁnitely many

primes in the Fibonacci sequence.

The main motivation of our research is a result of Graham [15] who found two

relatively prime positive integers x1, x2 such that the sequence

xn+1 = xn + xn−1,

n = 2, 3, 4, . . . , contains only composite numbers, i.e., xn is composite for each

n ∈ N. Graham’s pair (x1, x2) was

(331635635998274737472200656430763, 1510028911088401971189590305498785).

Knuth [20] found the smaller pair

(x1, x2) = (62638280004239857, 49463435743205655).

Wilf [36] slightly reﬁned Knuth’s computation and found the pair

(x1, x2) = (20615674205555510, 3794765361567513).

This was further reduced by Nicol [26] to

(x1, x2) = (407389224418, 76343678551).

Currently, the ”smallest” known such pair (in the sense that x1 +x2 is the smallest

positive integer or max(x1, x2) is the smallest positive integer) is due to Vsemirnov

[35]
 (x1, x2) = (106276436867, 35256392432).

We prove the generalized result of this kind for every binary linear recurrence

sequence except two cases for which the impossibility to obtain such result will

be proved by a short argument. To be precise, we prove the following:

Theorem 2.1. Let (a, b) ∈ Z
2 and let (xn)∞
n=1 be a sequence given by some

initial values x1, x2 and the binary linear recurrence

xn+1 = axn + bxn−1

for n = 2, 3, 4, . . . . Suppose that b ̸= 0 and (a, b) ̸= (2, −1), (−2, −1). Then there

exist two relatively prime positive integers x1, x2 such that |xn| is a composite

integer for each n ∈ N.
 17

The exclusion of the two cases is explained in Section 2.1: the required pair of

initial values does not exist, i.e. the sequence (|xn|)∞
n=1, where x1, x2 are composite

and gcd(x1, x2) = 1, always contains inﬁnitely many prime numbers. The proof (as

well as a part of the proof of Theorem 2.1) uses Dirichlet’s theorem on arithmetic

progressions: an arithmetic progression whose initial term and common diﬀerence

are coprime integers contains inﬁnitely many prime numbers (we take absolute

values of the terms).

Theorem 2.1 has been formulated and proved for non-degenerate sequences in

[30], preceeded by a weaker result in that direction [19]. (Binary linear recurrence

sequence given by the recurrence equation xn+1 = axn + bxn−1 is called degenerate

if either a = 0 or the roots α and β of the characteristic equation x2 − ax − b = 0

satisfy α/β = u, where u is some root of unity.) We present a full, independent

and much more self-contained proof.

Like Graham [15], we shall use the concepts of divisibility sequences and covering

systems, as well as his idea of ﬁnding an appropriate covering system for |b| = 1

and Vsemirnov’s pair (7) in order to treat some special cases with |b| = 1, in our

proof.

Definition 2.2. A sequence of rational integers (vn)∞
n=1 is called a divisibility

sequence if vr divides vs whenever r divides s.

The Fibonacci sequence is a divisibility sequence. A more general example of a

divisibility sequence is called the Lucas sequence of the ﬁrst kind. Assume that the

roots α, β of the (characteristic) equation x2 − ax − b = 0, where a, b ∈ Z, b ̸= 0,

are distinct α ̸= β. Then
 un := αn − βn

α − β ∈ Z,

n = 1, 2, 3, . . . , is a divisibility sequence. Indeed, if r divides s then, setting

l := s/r ∈ N, we see that

us
ur = αrl − βrl

αr − βr = αr(l−1) + αr(l−2)βr + · · · + βr(l−1)

is a symmetric function in α, β. Hence us/ur ∈ Z, giving ur|us. If (xn)
∞
n=1 is a

sequence given by the linear recurrence xn+1 = axn + bxn−1 then one can consider

a corresponding divisibility sequence, by selecting u1 := 1, u2 := a. This sequence

is the Lucas sequence of the ﬁrst kind.
 18

Definition 2.3. A collection of residue classes

ri (mod mi) := {ri + mik | k ∈ Z},

where mi ∈ N, ri ∈ Z, 0 ⩽ ri < mi, and i = 1, . . . , t, is called a covering system

if every integer n ∈ Z belongs to at least one residue class ri (mod mi), where

1 ⩽ i ⩽ t.

For example, 0 (mod 2), 1 (mod 2) is a covering system. A more interesting

example, used in our proof, is this covering system:

0 (mod 2), 0 (mod 3), 3 (mod 4), 5 (mod 8), 5 (mod 12), 1 (mod 24).

It would be of interest to extend Theorem 2.1 to linear recurrence sequences of

order d, where d ⩾ 3. For which (a1, . . . , ad) ∈ Z
d, where ad ̸= 0, one can choose

d integers x1, . . . , xd satisfying gcd(x1, . . . , xd) = 1 such that the sequence

xn+d = a1xn+d−1 + a2xn+d−2 + · · · + adxn, n = 1, 2, 3, . . . ,

contains only composite numbers, i.e., |xn| is a composite integer for each n ⩾ 1?

It seems likely that the complete answer to this question is out of reach. Firstly,

for most linear recurrences of order d, there are no divisibility sequences satisfying

them. See, e.g., Theorem IV in the paper of Hall [18] for one of the ﬁrst results

of this kind for d = 3 :

There is no regular divisibility (linear recurrence) sequence whose characteristic

polynomial is an irreducible (in the ring of rational polynomials) cubic whose last

two coeﬃcients are relatively prime. (Here, divisibility sequence is called regular

if its ﬁrst term equals 0.)

So, using our methods, one will not be able to deal with the cases of regular

divisibility sequences, where, e.g., ai ∈ {−1, 0, 1} for each i = 1, . . . , d and the

characteristic polynomial of the linear recurrence is irreducible. Secondly, and

more importantly, there are no methods that would allow us to show that the

cases, where the characteristic polynomial

xd − a1xd−1 − a2xd−2 − · · · − ad

is (x + 1)
d or (x − 1)
d, are exceptional. Already for d = 3 and, say, (a1, a2, a3) =

(3, −3, 1) one gets a problem on prime values of a quadratic polynomial Z ↦→ Z

at nonnegative integer points which is completely out of reach.

19

Recently, the case xn+3 = xn+2 + xn+1 + xn, n = 1, 2, 3, . . . , has been treated

successfully in [31].

Egyptian fractions and numbers expressible by some special

linear form

Let t be a ﬁxed positive integer. We consider the set of positive integers

E(t) := {n : n = tM − d},

where M is a positive multiple of the product and d is a positive divisor of the

sum of two positive integers, namely,

ab|M and d|(a + b)

for some a, b ∈ N. Evidently,

E(t
′) ⊆ E(t) whenever t|t
′.

It is easy to see that
 E(1) = E(2) = N.

Indeed, suppose ﬁrst that t = 1. Then, for each n ∈ N selecting a = 2n + 1, b = 1,

M = ab = 2n + 1 and d = (a + b)/2 = n + 1, we ﬁnd that

n = 2n + 1 − (n + 1) = M − d,

giving E(1) = N. In case t = 2, for each n ∈ N we may choose a = n + 1, b = 1,

M = ab = n + 1 and d = a + b = n + 2. Then 2M − d = 2(n + 1) − (n + 2) = n,

so that E(2) = N.

Apart form the cases t = 1 and 2 the situation with t ⩾ 3 is not clear. In

this context, the sets E(4) and E(5) are of special interest, because an integer n

belongs to the set E(t) if and only if

n = tM − d = tuab − (a + b)/v

with some a, b, u, v ∈ N. Therefore, n ∈ E(t) yields the representation

t
n = 1
x + 1
y + 1
z

with positive integers
 x := uab, y := uvna, z := uvnb.

20

Thus, this leads us to the subject of Egyptian fractions (the sums of distinct

unit fractions) and the related famous conjectures. If n ∈ E(t) then the fraction

t/n is expressible by the sum of three unit fractions (i.e., three inverted positive

integers). In particular, if every prime number p belongs to the set E(4) then

the Erd˝os-Straus conjecture (asserting that for each integer n ⩾ 2 the fraction

4/n is expressible by the sum 1/x + 1/y + 1/z with x, y, z ∈ N) is true, whereas

if every prime number p belongs to E(5) then the corresponding conjecture of

Sierpi´nski (asserting that for each n ⩾ 4 the fraction 5/n is expressible by the

sum 1/x + 1/y + 1/z) is true [29]. In this context the most general Schinzel’s

conjecture asserts that the fraction t/n for each n ⩾ n(t) is expressible by the

sum 1/x + 1/y + 1/z. This clearly holds for t ⩽ 3 but is open for each ﬁxed t ⩾ 4.

Conjecture 3.5 given below implies that there is an integer C(t) such that each

prime number p > C(t) belongs to E(t). This would imply Schinzel’s conjecture

as well.

Yamamoto [38], [39] and Mordell [25] observed that it is suﬃcient to prove

the Erd˝os-Straus conjecture for those prime numbers p which modulo 840 are

1, 121, 169, 289, 361, or 529. Vaughan [32] showed that the Erd˝os-Straus conjec-

ture is true for almost all positive integers n. See also the list of references in

section D11 of [17] for the literature concerning the conjectures of Erd˝os-Straus,

Sierpi´nski and Schinzel on Egyptian fractions. More references on the Erd˝os-

Straus (including recent ones) can be found in a paper of Elsholtz and Tao [12]

on the average number of solutions of the equation 4/p = 1/x + 1/y + 1/z

with prime numbers p. At the computational side the calculations of Swett

http://math.uindy.edu/swett/esc.htm show that the Erd˝os-Straus conjecture

holds for integers n up to 10
14.

We observe that

Theorem 3.1. The set E(4) does not contain perfect squares and the numbers

288, 336, 4545.

Suppose k2 ∈ E(4), i.e., there exist u, v, a, b ∈ N such that

v(4uab − k2) = a + b.

To show that k2 /∈ E(4) we shall use the fact, which was proved in [28], that

Lemma 3.2. The equation above has no solutions in positive integers u, v, a, b, k.

21

Lemma 3.2 implies that −d is a quadratic nonresidue modulo 4ab if d|(a + b).

Note that the set of divisors of a + b, when a < b both run through the set

{1, 2, . . . , n}, contains the set {1, 2, . . . , 2n − 1}. Thus, by Lemma 3.2, we ﬁnd

that

Corollary 3.3. For each positive integer n the 2n − 1 consecutive integers

4n! − 2n + 1, 4n! − 2n + 2, . . . , 4n! − 1

are quadratic nonresidues modulo 4n!.

Corollary 3.3 gives the example of at least (2 − ε) log m/ log log m consecutive

quadratic nonresidues modulo m = 4n!. In this direction, the most interesting

problem is to determine how many consecutive quadratic residues and consecutive

quadratic nonresidues modulo m may occur for prime numbers m. See, e.g., [6],

[16], where it is shown that we have at least c1 log m log log log m consecutive

quadratic residues modulo m for inﬁnitely many primes m, and [24], where the

factor log log log m is replaced by log log m under assumption of the generalized

Riemann hypothesis.

A set of positive integers which is a subset of ∪
∞
q=0E(4q + 3) was recently con-

sidered in [3]. For M = ab and d = a + b, where a, b are positive integers and

b ≡ 3 (mod 4), put
 E∗(t) := {n : n = tab − a − b}.

Evidently, E∗(t) ⊆ E(t). In [3] it was shown that the set E := ∪
∞
q=0E∗(4q + 3)

does not contain perfect squares and that all prime numbers of the form 4s + 1

less than 10
10 belong to E.

As we already observed, the sets N\E(1) and N\E(2) are empty. By Lemma 3.2

the equation v(4uab − k2) = a + b has no solutions in positive integers u, v, a, b, k.

In particular, if t is a positive integer divisible by 4 and s ∈ N is such that

4s|t then the equation vs(4(t/4s)uab − k2) = a + b has no solutions in positive

integers u, v, a, b, k. The latter is equivalent to the equation v(tuab − sk2) = a + b.

Consequently, we obtain that

Corollary 3.4. The set E(t), where 4|t, does not contain the numbers of the

form sk2, where s ∈ N satisﬁes 4s|t and k ∈ N.

22

In particular, this implies that the set N\E(t) is inﬁnite when 4|t. We conjecture

that all other sets, namely, N \ E(t) with t ∈ N which is not a multiple of 4 are

ﬁnite. More precisely, we conjecture that

Conjecture 3.5. There exists an integer C(t) ∈ N ∪ {0} such that the set

E(t) contains all integers greater than or equal to C(t) + 1 if 4 does not divide t

and all integers greater than or equal to C(t) + 1 except for sk2, where 4s|t and

k ∈ N, if 4|t.

We have C(1) = C(2) = 0. It is known that the total number of representations

of t/n by the sum 1/x + 1/y + 1/z does not exceed c(ε)(n/t)
2/3n
ε, where ε > 0

(see [4]). We know that if n ∈ E(t) then t/n is expressible by the sum of three

unit fractions, so this bound also holds for the number of representations of n in

the form tM − d. On the other hand, by the result of Vaughan [32], almost all

positive integers are expressible by the sum of three unit fractions. It is easy to

see that for each ﬁxed integer t ⩾ 3 almost all positive integers belong to the set

E(t).

In fact, one can easily show a much stronger statement:

Proposition 3.6. For any integer t ⩾ 3 almost all positive integers can be

written in the form pa − 1 with some prime number p ≡ −1 (mod t) and some

a ∈ N.

If n ∈ N can be written in this way then

n = pa − 1 = (p + 1)a − a − 1 = tM − d ∈ E(t)

with b = 1, d = a + 1 and M = (p + 1)a/t. By the above, it suﬃces to show

that the density of positive integers n that have no prime divisors of the form

p ≡ −1 (mod t) is zero. This can be easily done by a standard sieve argument

(see Section 3.1).
 23

1. Integer parts of powers of rational numbers

Let a > 1 be a rational number. In this section we will consider composite

numbers in the sequence
 [an], n = 1, 2, . . . ,

where the brackets denote an integer part of the number (i.e. [an] is the biggest

number that does not exceed an). We are interested in a problem for which the

cases a = 3/2 and a = 4/3 were successfully treated forty-ﬁve years ago by Forman

and Shapiro [14], but no progress had been made for a long time. This at ﬁrst

glance simple problem can be stated as follows: prove that for every rational a > 1

the sequence of integer parts [an] contains inﬁnitely many composite numbers.

(This problem is trivial for integer a.)

The nature of the methods applied allows us to obtain the results for some

sequences of a more general kind. Together with any sequence [a
n], n = 1, 2, . . . ,

all sequences of the form [ξan], n = 1, 2, . . . , where ξ is any real positive number,

are covered by the statements below (note that now the problem is not trivial

even for integer values of a). The sequences of shifted powers of rational numbers

[ξan + ν], n = 1, 2, . . . , are also considered.

We begin with our main theorem. Set P(2) = {2}, P(3) = P(4) = {2, 3},

P(6) = P(4/3) = {2, 3, 5}, P(3/2) = {2, 5, 7, 11}, P(5/4) = {2, 3, 7, 11, 13}.

Theorem 1.1. Let ξ > 0 be a real number and let a ∈ {2, 3, 4, 6, 3/2, 4/3, 5/4}.

Then the set [ξan], n ∈ N, contains inﬁnitely many elements divisible by at least

one number of the set P(a).

In the above mentioned paper [14] Forman and Shapiro proved that the sets

[(3/2)
n] and [(4/3)n], n ∈ N, contain inﬁnitely many composite numbers. Their

proof extends without change to [ξ(3/2)
n] and [ξ(4/3)
n] with arbitrary ξ > 0.

However, we will give a proof for a = 4/3 once again, because (after a small

preparation) we will be able to do this in just few lines in contrast to eight lemmas

used in [14]. This will serve as a warm-up for the proof of a corresponding result

for a = 5/4. The proof of Theorem 1.1 for a = 3/2 is given by combining our

Lemma 1.7 with the main result of [14].

24

A valuable diﬀerence between our approach and that of [14] is that we are seek-

ing a contradiction with Lemma 1.7 below which is obtained using fractional parts

rather than a similar lemma for the integer parts of powers as in [14]. The main

advantage in doing this is that we are able to describe some explicit (unavoidable)

ﬁnite sets for possible divisors. (We show, however, that such unavoidable sets do

not exist for some rational a; see the Proposition below.)

Note that the number a = 5 is missing in Theorem 1.1. The only reason for

this is that, for a = 5, such universal explicit (unavoidable) set for divisors of the

elements of the set [ξ5
n], n ∈ N, cannot be given. In fact, it cannot be given for

any number a = 4k + 1, where k ∈ N.

Proposition 1.2. Let a be a positive integer of the form 4k + 1, where k ∈ N,

and let P be an arbitrary ﬁnite set of prime numbers. Then there exists ξ > 0

such that every integer part [ξan], n = 1, 2, . . . , is relatively prime with every

prime number of the set P.

We prove Proposition 1.2 in Section 1.4. However, in the same section we prove

that the set [ξ5
n], n ∈ N, contains inﬁnitely many composite numbers since a

universal set of divisors does not work only for special values of ξ, which we are

able to deal with separately. The fact is a direct consequence of the following

theorem.

Theorem 1.3. Let ξ > 0 be a real number. If ξ ̸= (4k + 3)/(2 · 5
r), where

k, r are nonnegative integers, then the set [ξ5
n], n ∈ N, contains inﬁnitely many

elements divisible by 2, 3 or 5. If ξ = (4k + 3)/(2 · 5
r), where (4k + 3, 5
r) = 1, then

the set [ξ5
n], n ∈ N, contains inﬁnitely many elements divisible by 10k + 7.

It remains unproved that the integer parts [ξan], n = 1, 2, . . . , where ξ is an

arbitrary positive number and a ⩾ 7 is an integer, are composite for inﬁnitely

many n ∈ N. Also, Theorem 1.1 has not been extended to any rational noninteger

number other than 3/2, 4/3, 5/4 even for ξ = 1, although at ﬁrst glance the case

a = 6/5 may seem simpler than the case a = 5/4. However, by slightly changing

the problem, we can include some new rational numbers.

Theorem 1.4. Let ξ > 0 be a real number. Then each of the sets [ξ(5/2)n] − 1

and [ξ(6/5)
n] − 1, where n ∈ N, contains inﬁnitely many elements divisible by at

least one number of the set {2, 3, 5}.
 25

The proof for [ξ(5/2)
n] − 1 presented in Section 1.6 can be applied without

changes to all the sets of numbers the form [ξ(5/2)
n] − 1 + 30k, n ∈ N, where k is

any ﬁxed integer.

One can also consider the nearest integers to powers instead of integer parts.

We deﬁne the nearest integer to z as [z +1/2]. Some new numbers can be obtained

again.

Theorem 1.5. Let ξ > 0 be a real number. Then

(i) the set [ξ7
n + 1/2], n ∈ N, contains inﬁnitely many composite numbers,

(ii) the set [ξ(5/3)n + 1/2], n ∈ N, contains inﬁnitely many elements divisible by

2 or 3,

(iii) the set [ξ(7/5)n + 1/2], n ∈ N, contains inﬁnitely many elements divisible by

at least one of the numbers 2, 3, 5, 11.

Note that no deﬁnite divisors are indicated for the set [ξ7
n + 1/2], n ∈ N. This

case is diﬀerent from all the other cases for the reason that it is not covered by

Lemma 1.2 which holds only for non-integer rational numbers (as in the case

a = 5) and, in contrast to the case a = 5, integer parts are used to ﬁnish the proof

instead of fractional parts (which are instrumental in exluding most of the values

of ξ in the proof of Theorem 1.3).

In Section 1.1 we deﬁne the sequences of operations which describe the be-

haviour of the sequences of integer parts, but which can also be viewed as inﬁnite

words, i.e. formal sequences of symbols belonging to some set, called an alphabet.

We will study the patterns which could and could not occur in these words and

the possible periodicity of these sequences of symbols, as well.

Proofs

1.1. Preliminary considerations.

Write a = b/c, where b > c ⩾ 1 are relatively prime integers. (Note that a

is allowed to be an integer.) Setting xn = [ξan + ν] and yn = {ξan + ν}, we

obtain the equality a(xn + yn − ν) = xn+1 + yn+1 − ν. Consequently, cxn+1 =

bxn + byn − cyn+1 + (c − b)ν, so sn = byn − cyn+1 + (c − b)ν is an integer. It follows

26

that
 xn+1 = (bxn + sn)/c, yn+1 = (byn + (c − b)ν − sn)/c.

Furthermore, since 0 ⩽ yn, yn+1 < 1, we deduce that −c + (c − b)ν < sn <

b + (c − b)ν. Let throughout S(a, ν) be the set of integers which belong to (−c +

(c − b)ν, b + (c − b)ν). Of course, sn ∈ S(a, ν) can take only ﬁnitely many values

|S(a, ν)|.

Let P be a ﬁnite set of prime numbers . Assume that the numbers xn = [ξan+ν]

are not divisible by a prime p ∈ P for every suﬃciently large n. We know that

sn ∈ S(a, ν) for every n ∈ N. If p|bc, then p|b or p|c. Such p cannot divide sn for n

suﬃciently large, since otherwise xn+1 or xn is divisible by p. We will thus be able

to exclude all numbers divisible by such primes from the set S(a, ν). Furthermore,

the prime 2 lying in all sets P(a), by an easy parity argument, allows to exclude

all odd numbers from S(a, ν) in case if b and c are both odd.

Throughout we will use the following notation. Instead of s1, s2, s3, . . . we will

consider the sequence of operations denoted by A, B, . . . corresponding to every

s ∈ S(a, ν). If, say A corresponds to s, this means that A maps the integer x to

the integer (bx + s)/c (which corresponds to [ξan + ν] → [ξan+1 + ν]) and the

fractional part y (of ξan + ν) to (by − s + (c − b)ν)/c (which is the fractional part

of ξan+1 + ν).

All this gives certain restrictions on the sequence of operations containing A’s,

B’s etc. In particular, for every ﬁxed prime p, every operation is a permutation of

residues modulo p. (We will only use the primes 3, 5, 7, 11, 13 in all our arguments

below.) For instance, if say we seek for a contradiction modulo 7, then 2A1

means that A maps the number of the form 7v + 2, v ∈ N, to the number of the

form 7v′ + 1, v′ ∈ N, in the corresponding sequence of integer parts. In a more

compact form we will write this in, say, the form A = (12)(643|(5). This means

that the only possible transformations modulo 7 are 1A2, 2A1, 6A4, 4A3 and 5A5,

whereas 3 maps to 0, i.e. the next integer part is divisible by 7, a contradiction.

If, e.g., B = (123)(4|(56), these two successive operations will ‘multiply’ as two

permutations, namely, AB = (413|(2)(56|. Also, AA = A
2 = (1)(2)(63|(4|(5).

A pattern AB . . . A is said to be impossible if AB . . . A = (1|(2|(3|(4|(5|(6|; this

means that one of the corresponding integer parts, but not necessarily the last one,

is divisible by 7. Because of this notation, it is convenient to write the residues 10

27

modulo 11 and 10,11,12 modulo 13 as a single digit numbers. Throughout we will

use the notation 10 = α, 11 = β and 12 = γ. Note that A
∞ means the periodic

sequence AAAAA . . . . (Similarly, (AB)
∞ means ABABAB . . . .)

1.2. Two lemmas: the periodicity of the sequences of operations.

Lemma 1.6. Suppose that ξ > 0 and ν are real numbers. If a > 1 is a rational

noninteger number, then the sequence {ξan + ν}, n = 1, 2, . . . , is not periodic.

Proof of Lemma 1.6: Indeed, if the the sequence is periodic, then for inﬁnitely

many m ∈ N we have the equality {ξan + ν} = {ξan+m + ν}, where n is ﬁxed.

This implies that ξ(an+m − an) = ξan(am − 1) is an integer. This can only happen

if ξ is a rational number. Writing a = b/c, where b > c > 1 are relatively prime

integers, and multiplying the above number by cn and by the denominator of ξ,

we obtain that there is a ﬁxed positive integer g such that g(bm − cm)/c
m is an

integer. For m suﬃciently large, this can only happen if bm − cm is divisible by c,

which is impossible. This proves the lemma. □

Lemma 1.7. Suppose that a > 1 is a rational noninteger number. Then the

sequence s1, s2, s3, . . . is not periodic.

Proof of Lemma 1.7: Assume it is periodic, of period ℓ. Then the sequence

((c−b)ν −sn)/c, n = 1, 2, . . . , is periodic too. So there is a positive integer n, and,

for every j = 0, 1, . . . , ℓ − 1, there are two real numbers ζ = ζ(j) > 1 and ω = ω(j)

such that yn+j+tℓ = ζyn+j+(t−1)ℓ + ω for every t ∈ N. Fix j. Each fractional part in

the subsequence yn+j+tℓ, t = 1, 2, . . . , is obtained from the preceding one by the

formula y → ζy + ω. For z = y + ω/(ζ − 1) this transformation can be written

as z → ζz. We claim that yn+j = −ω/(ζ − 1). Indeed, if yn+j > −ω/(ζ − 1)

then yn+j+tℓ + ω/(ζ − 1) → ∞ as t → ∞. This is impossible, because every

fractional part is bounded above by 1. Similarly, if yn+j < −ω/(ζ − 1) then

yn+j+tℓ + ω/(ζ − 1) → −∞ as t → ∞, which is also impossible. By the recurrent

formula, it follows that yn+j+tℓ = −ω/(ζ − 1) = −ω(j)/(ζ(j) − 1) for every t ∈ N.

The same is true for every j in the range 0 ⩽ j ⩽ ℓ − 1. Hence the sequence

28

yn, yn+1, yn+2, . . . is purely periodic with period at most ℓ. This plainly implies

that y1, y2, y3, . . . is periodic, contrary to Lemma 1. □

The key diﬀerence between Lemma 1.7 and a respective result in [14] is that

we claim that the sequence is not periodic without assumption that the sequence

of integer parts contains only ﬁnitely many composite numbers. Note that the

sequence can be periodic for integer a. For instance, we can take ξ = 1/2 and

a = 5. Then s1 = s2 = s3 = · · · = 2.

Hence, we obtain an important conclusion by Lemma 1.7 without making the

above mentioned assumption: periodic sequences of operations (as deﬁned in Sec-

tion 1.1) for noninteger a cannot occur.

1.3. Proof of Theorem 1.1: easy cases.

Here we will prove Theorem 1.1 in all cases except the case a = 5/4.

For a = 2, the binary expansion of the number ξ contains inﬁnitely many zeros.

So the set [ξ2
n], n ∈ N, contains inﬁnitely many even numbers.

For a = 3, we have S(3, 0) = {0, 1, 2}. Thus xn+1 = 3xn + sn with sn ∈ {0, 1, 2}.

Since 3 and 1 are both odd, the sequence xn, n = 1, 2, . . . , contains inﬁnitely

many even numbers or inﬁnitely many numbers divisible by 3, unless sn = 2 for

all large n. Assume that it is so. But then yn+1 = 3yn − 2 for all suﬃciently large

n. This implies that yn → −∞ as n → ∞, a contradiction.

For a = 4, S(4, 0) = {0, 1, 2, 3}. We either have inﬁnitely many even integer

parts or there are just two possibilities xn+1 = 4xn + 1 and xn+1 = 4xn + 3

starting with certain n. Assume that m is so large that xm, xm+1, . . . are not

divisible by 3. Then, by a simple argument modulo 3, we see that the possibility

xn+1 = 4xn + 1 cannot occur more than once. It follows that xn+1 = 4xn + 3 for all

suﬃciently large n. Then yn+1 = 4yn − 3 for all large n, so yn → −∞ as n → ∞,

a contradiction.

For a = 6, S(6, 0) = {0, 1, 2, 3, 4, 5}. Now, either we have inﬁnitely many integer

parts divisible by 2 or 3 or there are just two possibilities xn+1 = 6xn + 1 and

xn+1 = 6xn+5 starting with certain n. Assume that m is so large that xm, xm+1, . . .

are not divisible by 5. Then, by a simple argument modulo 5, we see that the

29

possibility xn+1 = 6xn + 1 cannot occur more than three times. It follows that

xn+1 = 6xn + 5 for all suﬃciently large n. Then yn+1 = 6yn − 5 for all large n, so

yn → −∞ as n → ∞, a contradiction.

For a = 4/3, S(4/3, 0) = {−2, −1, 0, 1, 2, 3}. Again, either there are inﬁnitely

many integer parts divisible by 2 or 3 or only two possibilities can occur 3xn+1 =

4xn−1 (type A) and 3xn+1 = 4xn+1 (type B) starting with certain n. Assume that

there are only ﬁnitely many integer parts divisible by 5. Of course, A = (1)(324|

and B = (231|(4) modulo 5. Since the sequence of A’s and B’s is not periodic, the

pattern AB occurs inﬁnitely often. More precisely, since AB = (1|(3)(24|, this

pattern can only be 3AB3 or 2AB4. The second case is impossible, because we

then must have B∞, which is periodic, contrary to Lemma 1.7. Similarly, 3AB21

leads to A
∞, a contradiction again. So we can only have 3ABA2. In order to avoid

1 and 4 in the sequence of residues modulo 5, we must have (AB)
∞ which is also

periodic, a contradiction.

For a = 3/2, S(3/2) = {−1, 0, 1, 2}. Now, either there are inﬁnitely many

even integer parts or there are two possibilities 2xn+1 = 3xn − 1 (type A) and

2xn+1 = 3xn + 1 (type B) starting with certain n. The arguments modulo 5, 7, 11

of Forman and Shapiro [14] show however that this sequence must be periodic,

unless there are inﬁnitely many integer parts divisible by 5, 7 or 11. This proves

the result, by Lemma 1.7. The fact that they only consider the case ξ = 1 is not

essential. We will not repeat their argument, although it can also be made much

shorter than in [14].

1.4. The case a = 5/4.

Consider the case a = 5/4. Then S(5/4, 0) = {−3, −2, −1, 0, 1, 2, 3, 4}. At the

expense of the prime 2, we can exclude −2, 0, 2, 4. The four remaining cases cor-

respond to the recurrences 4xn+1 = 5xn + sn and yn+1 = (5yn − sn)/4. They are

sn = −1 (type A), sn = 3 (type B), sn = 1 (type C) and sn = −3 (type D).

Note that the operation A can only occur if yn ∈ [0, 3/5). On applying it, the

fractional part yn+1 will be in the interval [1/4, 1). So A acts on fractional parts

as [0, 3/5) → [1/4, 1). Similarly, B : [3/5, 1) → [0, 1/2), C : [1/5, 1) → [0, 1) and

30

D : [0, 1/5) → [3/4, 1). We will write this in the form as below, where x, y refer

to integer and fractional parts, respectively:

A : x → (5x − 1)/4, y → (5y + 1)/4, [0, 3/5) → [1/4, 1);

B : x → (5x + 3)/4, y → (5y − 3)/4, [3/5, 1) → [0, 1/2);

C : x → (5x + 1)/4, y → (5y − 1)/4, [1/5, 1) → [0, 1);

D : x → (5x − 3)/4, y → (5y + 3)/4, [0, 1/5) → [3/4, 1).

In order to avoid confusion we must say that the composition of operations

in the proof of Lemma 1.8 below is very unusual for a reader with an algebraic

background. The composition of operations, say, BC is read from left to right

giving BC : y → (25y − 19)/16. This of course contradicts to the usual rule of

composition from right to left. However, in all our arguments following Lemma

1.8 we always use A, B, C and D, ﬁrstly, as elements of an inﬁnite sequence and,

secondly, as a kind of permutations. In both cases, it is much more convenient to

write (and read), say, BC from left to right.

Lemma 1.8. The patterns AD, DA, D2, B2, BC kB, where k ∈ N, BC 4,

(DB)
2D, BDCBDC uBD, u ∈ {0, 1, 2, 3}, (BD)
3, (DB)
2CD, (DB)
2C 2DBC vD,

v ∈ {0, 1}, cannot occur.

Proof of Lemma 1.8: The result is evident for AD, DA, D2 = DD and B2 =

BB from fractional parts. Also, BC : y → (25y − 19)/16 which is smaller than

3/8. Since C maps every y to a smaller number, we deduce that BC k maps y to a

number smaller than 3/8 for every k ∈ N. Hence BC kB cannot occur. Similarly,

C 4 : y → (625y − 369)/256, so C 4 can only be applied to y ⩾ 369/625 > 1/2.

Hence BC 4 cannot occur. Also, (DB)2 : y → (625y + 123)/256 which is greater

than 1/5, so (DB)
2D cannot occur.

Since BD : y → (25y − 3)/16, it can only be applied if 3/5 ⩽ y < 19/25. But

BDCBD : y → (3125y − 967)/1024 which is greater than or equal to 227/256 =

0.88671 . . . . On applying C at most three times to this number we will get a

number greater than 0.77 > 0.76 = 19/25, so the pattern BDCBDC uBD, where

0 ⩽ u ⩽ 3, cannot occur. Note that (BD)
2 : y → (625y − 123)/256. For y ⩾ 3/5,

this is greater than or equal to 63/64 > 19/25, so (BD)
2 cannot be followed by

one more BD, i. e. (BD)3 cannot occur.

31

Similarly, (DB)
2C : y → (3125y + 359)/1024 which is greater than 0.35 > 1/5,

so (DB)
2CD is impossible. Furthermore, this implies that (DB)2C 2 maps every

y to a number y′ > 3/16. But DB maps y′ to (25y′ + 3)/16 which is greater than

0.48, since y′ > 3/16. Thus (DB)2C 2DBC v, v ∈ {0, 1}, is greater than 0.35 and

cannot be followed by D. □

Lemma 1.9. Suppose that the set of integer parts contains only ﬁnitely many

elements divisible by 2 and 3. Then there are only ﬁnitely many A’s. Furthermore,

starting from some place, the sequence of operations is either BDC k1BDC k2 . . .

or DBC k1DBC k2 . . . , where k1, k2, · · · ⩾ 0.

Proof of Lemma 1.9: Note ﬁrst that the patterns AC, CA, ABA, ABDC,

CBC, CDC cannot occur. Indeed, modulo 3 we have A = (1)(2|, B = (12),

C = (1|(2), D = (12). This implies the above claim. We will frequently use it

without referring to it. Sometimes we will combine it with Lemma 3 which gives

other restrictions on patterns.

Assume that there are inﬁnitely many A’s. Then, since the sequence is not

periodic and since the patterns AC, CA, AD and DA cannot occur, every pattern

A
k, k ∈ N, can only occur between two B’s. Similarly, since BC kB is impossible,

every pattern C k can only occur between B and D, giving BC kD, D and B,

giving DC kB, or D and D, giving DC kD. Fix a fragment BAkB. Let’s forget for

a moment about A’s and C’s and consider the remaining subsequence of B’s and

D’s (to the right of the ﬁxed fragment BAkB which can only be 2BAkB2). Next

operation in this subsequence should be D, because neither B2 nor ABA can occur,

so the next operation cannot be B. Furthermore, this D should be of the form

2D1. Now, the next operation in the subsequence should be B. Indeed, assume

that it is D. Since the pattern D2 is impossible, these two D’s should be separated

by C k, k ∈ N. Since CDC cannot occur, we must have the pattern ABDC kD, but

its subpattern ABDC cannot occur, a contradiction. Furthermore, this B must

be of the form 1B2. Since BC kB, where k ⩾ 0, is impossible, after D, B it should

be 2D1 again, etc. We thus deduce that the subsequence is D, B, D, B, D, B, . . . .

These can only be separated by C k, so there are no more A’s, as claimed.

If there are only ﬁnitely many C’s in the original sequence, we have (DB)
∞,

a contradiction. Assume that the ﬁrst occurrence of C’s is between D and B, i.

32

e. there is a pattern DC kB with k > 0. Modulo 3 we must have 1DC kB1. This

cannot be followed by C, so it must be followed by D and gives 1DC kBD2. This

is clearly followed by C k1B, where k1 ⩾ 0, and gives 1DC kBDC k1B1. Further,

we must have D, then C k2BD, etc. Hence the sequence from certain place is

BDC k1BDC k2 . . . , k1, k2, · · · ⩾ 0. The argument when the ﬁrst occurrence of C’s is

between B and D is precisely the same and gives the sequence DBC k1DBC k2 . . . ,

where k1, k2, · · · ⩾ 0. □

Lemma 1.10. Suppose that the set of integer parts contains only ﬁnitely many

elements divisible by 2, 3, 7, 11 and 13. Then the sequence BDC k1BDC k2 . . . is

impossible.

Proof of Lemma 1.10: Modulo 7 we have B = (63125|(4), C = (21534|(6),

D = (14652|(3). Hence BD = (1|(2)(346)(5|.

We claim that there are inﬁnitely many patterns 4BD6. There are four possible

cases 3BD4, 6BD3, 2BD2 and 4BD6. In the ﬁrst case, we cannot have C next,

so we must have 4BD6 straight after 3BD4. In the second case, 6BD3, we have

next either 3BD4 (i.e. we are back to the ﬁrst case), or 3C4 which can only be

followed by 4BD6. Finally, in the third case, 2BD2, since the sequence is not

(BD)
∞, we must have some C’s later on. So next there is 2(BD)u2C v, where

u ⩾ 0 and v ∈ {1, 2, 3, 4}, which ends with 1, 5, 3, 4, respectively, and then BD

again. But BD cannot begin with 1 or 5. So we either immediately get 4BD6

or we are back to the case 3BD4, which is already considered. This proves our

claim.

Each pattern 4BD6 is either followed immediately by 6BD3 or it is followed by

6C kBD3. We thus have 4BDC kBD3, where k ⩾ 0. If next we would have 3BD4

then this should be followed again by BD. But by Lemma 1.8 (BD)
3 cannot occur,

so BD cannot be repeated more than twice, a contradiction. Thus we have the

pattern 4BDC kBDC4 which must be followed by 4BD6, etc. Hence our sequence

is formed by the patterns BDCBD which are separated by C ui, where ui ⩾ 0. So

the sequence is
 BDCBDC u1BDCBDC u2 . . . .

Furthermore, Lemma 1.8 implies that each ui is greater than or equal to 4.

33

The number 10 modulo 11 occurs as one of the residues. Recall that through-

out 10 will be denoted by α. We have that the operations B : x → 4x − 2,

C : x → 4x + 3 and D : x → 4x + 2 modulo 11, hence B = (9126|(3α574)(8),

C = (17965)(3482|(α), D = (16478)(2α95|(3). Consequently, BDCBDC 4 =

(25|(79|(81|(3|(4|(6|(α|. Thus BDCBDC ui can only end with one of the num-

bers 1, 7, 9, 6, 5. However the next block BDCBDC ui+1 can only begin with 7.

Thus each of the blocks BDCBDC ui is of the form 7BDCBDC ui7. This only

happens if each ui is of the form 8 + 5vi, where vi is a nonnegative integer. Fur-

thermore, there exist positive vi, for otherwise we have (BDCBDC 8)∞. Hence

ui ⩾ 13 for some i.

We have no other choice modulo 13, but to continue with our curious notation

10 = α, 11 = β and 12 = γ. Now, B : x → −2x + 4, C : x → −2x + 10,

D : x → −2x + 9. Hence B = (49γ6573β812|(α), C = (α3426β18795|(γ), D =

(941786α25γβ|(3). Thus BDCBD = (1|(2|(953|(8β6αγ|(74|. It follows that the

block BDCBDC ui with ui ⩾ 13 can only be of the form αBDCBDC uiγ, because

γC uiγ is the only possibility if ui ⩾ 11. However, the next block BDCBDC ui+1

cannot begin with γ, since the pattern BDCBD cannot begin with γ, a contra-

diction. □

Lemma 1.11. Suppose that the set of integer parts contains only ﬁnitely many

elements divisible by 2, 3, 7, 11 and 13. Then the sequence DBC k1DBC k2 . . . is

impossible.

Proof of Lemma 1.11: We will ﬁrst argue modulo 7 and claim that there

are inﬁnitely many patterns 3DB1. Since DB = (143)(5)(2|(6|, other possibilities

are 4DB3, 1DB4 and 5DB5. Recall that C = (21534|(6). The ﬁrst possibility,

4DB3, leads to 3DB1 next or we must have 4DBC4. So the only alternative to

4DB3 to occur is (DBC)
∞, a contradiction with Lemma 1.7. The pattern 1DB4

leads to 4DB3, so to the case which we just considered. After repeating 5DB5

at most twice (Lemma 1.8), we should apply either C or C 2 and then DB again

(modulo 7). This gives, respectively, 3DB1 (as required) or 4DB3 (which is the

ﬁrst possibility). The claim is proved.

If 3DB1 is followed by DB again, we cannot have further DB, by Lemma 1.8,

so it must be followed by C. But (DB)2C cannot begin with 3, a contradiction.

34

Hence 3DB1 must be followed by C, i. e. we have inﬁnitely many patterns

3DBC5. What can happen between two successive 3DBC5? Assume that the next

operation after the ﬁrst 3DBC5 is C. Then either 3DBC 23 is followed by 3DBC5

or we have 3DBC 3DB3 and then further (CDB)k until the second 3DBC5. Both

cases can be written as DBC 2(CDB)
u, where u ⩾ 0. Alternatively, assume that

after the ﬁrst 3DBC5 is DB. The whole pattern is 3DBCDB5. We can have at

most one DB until the next C, so the pattern can be written as 3DBC(DB)
vC3,

where v ∈ {1, 2}. We will show that the case v = 2 is impossible. Indeed, by

Lemma 1.8, (DB)
2C should be followed by C which gives 3DBC(DB)
2C 24. This

must be followed by 4DB3 (modulo 7), so we get (DB)2C 2DB3. Further, by

Lemma 1.8, this cannot be followed by DB or by CDB. So it must be followed

by C 2, which is impossible modulo 7. Hence v = 1, i. e. we have 3(DBC)23. The

second 3DBC5 begins either immediately or after inserting (CDB)
k, k ∈ N. We

conclude that the whole sequence consists of just two type blocks DBC 2(CDB)
u

and (DBC)2(CDB)
k, where k, u ⩾ 0.

We now show that k and u can only take two values 0 and 1. Set E = (DBC)
2,

F = (DBC)
2(CDB)k, G = DBC 2, H = DBC 2(CDB)u, where k, u ∈ N. Note

that the same letter F (and H) can denote diﬀerent patterns. Modulo 11, we have

E = (371|(68|(α2|(9)(4|(5|, G = (427|(3α968|(1|(5|, CDB = (α185|(9342|(7)(6|.

(Here, we use the expressions for B, C, D from Lemma 1.10.) Assume that there

is F with k ⩾ 2. By Lemma 1.8, (DB)2CD is impossible, so F cannot be followed

by another F (which can be diﬀerent from the ﬁrst F ) or E. Thus it must be

followed by G or H. Note that F with k ⩾ 2 can end up only with the residues

7, 5, 4, 2. So F H can end up only with 7. F G can end up only with 2 or 7. In case

it ends up with 2, F G must be followed by G or H which ends by 7. With 7 can

only begin E or F ; this ends with 1, 8 or 5. But neither of E, F, G, H begins with

1, 8 or 5, a contradiction. Similarly, assume that there is an H with u ⩾ 2. By

Lemma 1.8, the patterns HE and HF cannot occur. H with u ⩾ 2 can end with

7, 8, 5, 4, 2. This shows that HH, where both H can be diﬀerent, can only end

with 7, whereas HG can end with 2 or 7. In case it is 2, HG should be followed

by G or H. This ends up with 7 and we get a contradiction as above. Hence

k = u = 1 and F, H are uniquely determined. Thus the sequence can contain

35

only four possible patterns E = (DBC)
2, F = (DBC)
2CDB, G = DBC 2 and

H = DBC 2CDB = DBC 3DB.

Our next claim is that only the patterns of the form GH and G
2EkF, where k ⩾

0, can occur. We will still argue modulo 11. Recall that E = (371|(68|(α2|(9)(4|(5|,

G = (427|(3α968|(1|(5|, F = ECDB = (9378|(65|(1|(2|(4|(α|, and H = GCDB =

(27|(4|(α31|(9|(65|(8|. None of the operations E, F, G, H begins with 1, 5, 8, so

they cannot end with 1, 5, 8. With 7 can begin only E and F, but they end with

1 and 8, respectively. This is impossible, so no operation can begin or end with

1, 5, 7, 8. All remaining possibilities are αE2, 9E9, 4G2, 3Gα, αG9, 9G6, 9F 3,

αH3. None of these begins with 2 or 6, so αE2, 4G2, 9G6 cannot occur. Remaining

are 9E9, 3Gα, αG9, 9F 3, αH3. It is easily seen that F and H must be followed by

3Gα, so we have inﬁnitely many 3Gα, unless the sequence is E∞. What can happen

between two consecutive 3Gα’s? If 3Gα is followed by αH3, we immediately get

the fragment GH, because the next 3Gα should follow. Otherwise, we have 3G
29.

If the next is 9F 3, we have 3G
2F 3 and the fragment is ﬁnished. The alternative

is that we have several E’s (which are all of the form 9E9 inserted between G
2

and F ). So another possible fragment is G
2EkF, where k ⩾ 0.

We now derived that the sequence contains just two possible fragments GH and

G
2EkF. A contradiction will be obtained modulo 13. By a simple computation

using the expressions for A, B, C, D from the previous lemma, we have modulo 13

G = DBC 2 = (125)(7)(64β|(38|(γ9|(α|,

H = DBC 3DB = (γ679|(431α|(5)(2|(8|(β|,

E = (DBC)
2 = (16)(34)(γ8|(25|(9β|(7|(α|,

F = (DBC)
2CDB = (937|(γ1|(65|(42|(8|(α|(β|.

Clearly, G
2 = (152)(7)(6β|(3|(4|(8|(9|(α|(β|(γ|. In case if the sequence is not

(GH)
∞, we must have inﬁnitely many fragments of the form G
2EkF (with may

be diﬀerent k ⩾ 0). But G
2 can end only with 1, 2, 5, 7, β, so G
2Ek can end with

1, 2, 5, 7, β, 6. Among these numbers, F can only begin with 6 thus giving 5 at the

end of each fragment G
2EkF. If we have at least one fragment GH after certain

G
2EkF, then it must be 5GHα. However G cannot begin with α, a contradiction.

So we only have the fragments of the form G
2EkF with may be diﬀerent k, but

each ending (and so beginning) with 5. So we have 5G
22. This cannot be followed

36

neither by F nor by E2, so it must be followed by E and then by F which is

impossible modulo 13, a contradiction. This completes the proof of Lemma 6 □

By Lemma 1.9 there are no other possibilities for the sequence of operations

under the conditions of Theorem 1.1 except the two eliminated by Lemma 1.10

and Lemma 1.11. This implies that Theorem 1.1 is correct for a = 5/4, as well as

in all other cases explored in Section 1.3.

1.5. The case a = 5 and Proposition 1.2.

Proof of Proposition 1.2: Let P be the product of all odd primes of P, and

let δ = 1 if P is of the form 4v + 3, v ⩾ 0, and δ = 3 if P is of the form 4v + 1,

v ⩾ 0. Put ξ = δP/2. Then [ξan] = (δP a
n − 1)/2 is odd, so there are no numbers

among integer parts divisible by 2. Also, if p is an odd prime which belongs to P,

then (δP an − 1)/2 is not divisible by p. □

Proof of Theorem 1.3: We have xn+1 = 5xn + sn with sn ∈ S(5, 0) =

{0, 1, 2, 3, 4}. Assume that the sequence of integer parts contains only ﬁnitely

many elements divisible by 2 and 5. Then, starting with some n, there are two

possibilities xn+1 = 5xn + 2 (type A) and xn+1 = 5xn + 4 (type B). Suppose

that there are also only ﬁnitely many elements divisible by 3. But A = (1)(2| and

B = (1|(2) modulo 3, so the patterns AB and BA cannot occur. Thus we have

either A∞ or B∞. In the second case, yn+1 = 5yn − 4, hence yn → −∞ as n → ∞,

a contradiction. So we must have A
∞, i. e. xn+1 = 5xn + 2 and yn+1 = 5yn − 2

for all suﬃciently large n. In case if there is no n for which yn = 1/2, we obtain a

simple contradiction using fractional parts as in Lemma 1.7 and getting yn → ∞

or yn → −∞ as n → ∞. So yu = 1/2 for some u ∈ N. Setting q = xu, we

deduce that ξ5
u = q + 1/2. Hence either we have inﬁnitely many integer parts

[ξ5
n] divisible by at least one number of the set {2, 3, 5} or ξ = (q + 1/2)5
−u.

Let us choose the smallest nonnegative integers t and r for which we can write

ξ = (2q + 1)/(2 · 5
u) = (2t + 1)/(2 · 5
r). Then

xn+r = [(t + 1/2)5
n] = t5
n + (5n − 1)/2.

37

If t is even, then the numbers t5
n + (5
n − 1)/2, n = 1, 2, 3, . . . , are all even. Hence

the sequence [ξ5
n], n = 1, 2, . . . , contains inﬁnitely many even numbers, but this

is already covered by the previous case, because 2 ∈ {2, 3, 5}. So assume without

loss of generality that t is odd: t = 2k + 1, where k ⩾ 0. Then ξ = (4k + 3)/(2 · 5
r),

where (4k + 3, 5
r) = 1.

We need to show that the sequence of integer parts (2k + 1)5n + (5n − 1)/2,

n = 0, 1, 2, . . . , contains inﬁnitely many elements divisible by 10k + 7. Let us take

n of the form 1 + ϕ(10k + 7)ℓ, where ϕ is Euler’s function and ℓ ∈ N. Then

(2k + 1)5n + (5n − 1)/2 = (10k + 7)5ϕ(10k+7)ℓ + (5ϕ(10k+7)ℓ − 1)/2

is divisible by 10k+7, by Euler’s theorem, because (5, 10k+7) = 1. This completes

the proof of Theorem 1.3. □

1.6. Composite numbers in the sequences of shifted integer parts.

Proof of Theorem 1.4: For xn = [ξ(5/2)
n − 1], S(5/2, −1) = {2, 3, 4, 5, 6, 7}.

So we either have inﬁnitely many shifted integer parts xn divisible by 2 or 5 or

two types of linear recurrences 2xn+1 = 5xn + 3 (type A) and 2xn+1 = 5xn + 7

(type B). Modulo 3, we have A = (1)(2) and B = (21|. Hence, if only ﬁnitely

many elements are divisible by 3, we cannot have more than one operation B

which must be followed by A∞, a contradiction with Lemma 2. (Note that the

same proof applies without change to every set of the form [ξ(5/2)
n] − 1 + 30k,

where k is a ﬁxed integer and where n runs over every positive integer.)

Similarly, for xn = [ξ(6/5)n − 1], S(6/5, −1) = {−3, −2, −1, 0, 1, 2, 3, 4, 5, 6}.

All numbers in this set, except for −1 and 1, are divisible by 2, 3 or 5. This,

assuming that there are only ﬁnitely many shifted integer parts divisible by 2, 3, 5,

leaves just two possibilities. The corresponding formulas for fractional parts are

yn+1 = (6yn + 2)/5 and yn+1 = 6yn/5. For n suﬃciently large, yn > 0, since we

must have at least once the ﬁrst operation. (Otherwise this contradicts to Lemma

2.) But, as in both cases yn+1 ⩾ 6yn/5, we deduce that yn → ∞, a contradiction.

□

Proof of Theorem 1.5: For 7, we have S(7, 1/2) = {−3, −2, −1, 0, 1, 2, 3}.

Assume that we have only ﬁnitely many shifted integer parts xn divisible by 2

38

and 7. Then, starting with certain n, we must have xn+1 = 7xn − 2 (operation

A) or xn+1 = 7xn + 2 (operation B). Modulo 3 we have A = (12| and B = (21|,

so either there are inﬁnitely many integer parts divisible by 3 or, starting with

some place, we have (AB)∞. (There is no contradiction with Lemma 1.7, because

for a = 7 it cannot be applied.) However, this means that there is an inﬁnite

subsequence of primes deﬁned by the recurrent formula xn+2 = 7(7xn − 2) + 2 =

49xn − 12. Take one of these xn = p > 7. Take q such that 4q + 1 is divisible

by p. Then, since −12 ≡ 48q (mod p), we get xm+2 + q ≡ 49(xm + q) (mod p)

for every m = n, n + 2, n + 4, . . . . Choosing e ∈ N such that p|(49
e − 1) and

multiplying the ﬁrst e congruences we get xn+2e + q ≡ (xn + q) (mod p), hence

xn+2e − xn = xn+2e − p is divisible by p. So xn+2e > p is divisible by p and thus

cannot be prime, a contradiction. This proves part (i).

For 5/3, we have S(5/3, 1/2) = {−3, −2, −1, 0, 1, 2, 3}. Assume that there are

only ﬁnitely many shifted integer parts divisible by 2 and 3. This leaves us two

options −2 and 2 with two respective operations for fractional parts A : y →

(5y + 1)/3 (which maps [0, 2/5) to [1/3, 1)) and B : y → (5y − 3)/3 (which maps

[3/5, 1) to [0, 2/3)). If the sequence is not A
∞, B∞ or (AB)
∞ ((BA)
∞ is the same),

then we must have either A2 or B2. Since A
2 : y → (25y + 8)/9 which is greater

than or equal to 8/9, A2 must be followed by B2. Similarly, B2 : y → (25y − 24)/9

which is smaller than 1/9, so B2 should be followed by A
2. We thus have (A
2B2)
∞,

a contradiction with Lemma 1.7, which completes the proof of (ii).

Finally, S(7/5, 1/2) = {−5, −4, −3, −2, −1, 0, 1, 2, 3, 4, 5}. At the expense of

prime numbers 2, 5 we can exclude all numbers from S(7/5, 1/2) except for −4,

−2, 2, 4. The four remaining possibilities are

A : x → (7x − 4)/5, y → (7y + 3)/5, [0, 2/7) → [3/5, 1);

B : x → (7x − 2)/5, y → (7y + 1)/5, [0, 4/7) → [1/5, 1);

C : x → (7x + 2)/5, y → (7y − 3)/5, [3/7, 1) → [0, 4/5);

D : x → (7x + 4)/5, y → (7y − 5)/5, [5/7, 1) → [0, 2/5).

Modulo 3 we have A = C = (1|(2) and B = D = (1)(2|. The sequence thus

contains either the operations A and C only or the operations B and D only.

(Otherwise there are inﬁnitely many shifted integer parts divisible by 3.) We will

consider the A, C case. Assume without loss of generality that the sequence is

39

not C ∞. We then have inﬁnite number of A’s. Each A should be followed by a

pattern of C’s. But C 4 : y → (2401y − 2664)/625, so it cannot occur. We thus

can have the patterns AC, AC 2 and AC 3 only. Note that AC : y → (49y + 6)/25,

AC 2 : y → f (y) = (343y − 33)/125, AC 3 : y → g(y) = (2401y − 606)/625.

Since the functions (49y + 6)/25 and f (y) at 6/25 are greater than 2/7, each

AC should be followed by AC 3. By Lemma 1.7, the sequence is not (AC 2)
∞, so

this implies that there are inﬁnitely many patterns AC 3. We claim that only the

patterns AC 3AC and AC 3AC 2AC can occur. Indeed, since g(2/7) = 16/125 and

g(16/125) < 0, AC 3 cannot be followed by AC 3, so it must be followed either

by AC or by AC 2. In the ﬁrst case we have AC 3 next after the pattern AC 3AC.

In the second case, AC 3AC 2, since f (16/125) < 0.09 < 16/125 we cannot have

AC 3 next. Also, since f (0.09) < 0, we cannot have AC 2 next, so AC 3AC 2 must

be followed by AC which is always followed by AC 3. This proves that only the

patterns U = AC 3AC 2AC and V = AC 3AC can occur.

We will now seek for a contradiction modulo 11. Assume that there are only

ﬁnitely many elements divisible by 11. A acts as x → 8 − 3x and C acts as

x → 7 − 3x. This gives A = (86154793α|(2) and C = (785392146|(α). Thus

U = (18|(24|(76|(9)(3|(5|(α| and V = (1)(24α|(93|(78|(5|(6|. By Lemma 1.7, the

sequence is not U ∞ or V ∞, so there are inﬁnitely many patterns V U. But V U can

only be of the form 1V U 8. This leads to a contradiction, because U and V cannot

begin with 8, so neither V U 2 nor V U V can occur.

Finally, note that on replacing each pair xn, yn by −xn, 1 − yn, D becomes A

and B becomes C. The endpoints of the intervals will be the only diﬀerence: e. g.,

instead of [0, 2/7) the respective interval will be (0, 2/7]. This makes no diﬀerence

in our argument, so we do not need to repeat it in the case when B and D are

the only operations which occur. The proof of Theorem 1.5 is now completed. □

40

2. Binary linear recurrence sequences

Here, in Section 2, we will examine the occurrence of composite numbers in the

sequences of integers of another kind.

A sequence of real numbers xn, n = 1, 2, . . . , is called a linear recurrence se-

quence if it’s terms satisfy the recurrence

xn+d = a1xn+d−1 + a2xn+d−2 + · · · + adxn, n = 1, 2, 3, . . . ,

for some ﬁxed numbers d ∈ N and a1, a2, . . . , ad ∈ R. The number d is called an

order of the linear recurrence sequence under the natural assumption that ad ̸= 0.

Our results concern the order 2 (or binary) linear recurrence sequences consist-

ing of integers. The best-known example of a binary linear recurrence sequence

is the Fibonacci sequence, given by F1 = F2 = 1 and the recurrence relation

Fn+1 = Fn + Fn−1 for n ⩾ 2. Graham [15] found two relatively prime positive

integers x1, x2 such that the sequence

xn+1 = xn + xn−1,

n = 2, 3, 4, . . . , contains only composite numbers, i.e., xn is composite for each

n ∈ N. We will prove the generalized result of this kind for every binary linear

recurrence sequence except two cases for which the impossibility to obtain such

result will be proved by a short argument. To be precise, we prove the following:

Theorem 2.1. Let (a, b) ∈ Z
2 and let (xn)
∞
n=1 be a sequence given by some

initial values x1, x2 and the binary linear recurrence

xn+1 = axn + bxn−1 (1)

for n = 2, 3, 4, . . . . Suppose that b ̸= 0 and (a, b) ̸= (2, −1), (−2, −1). Then there

exist two relatively prime positive integers x1, x2 such that |xn| is a composite

integer for each n ∈ N.

The exclusion of the two cases is explained in Section 2.1: the required pair of

initial values does not exist, i.e. the sequence (|xn|)∞
n=1, where x1, x2 are composite

and gcd(x1, x2) = 1, always contains inﬁnitely many prime numbers. The proof (as

well as a part of the proof of Theorem 2.1) uses Dirichlet’s theorem on arithmetic

progressions: an arithmetic progression whose initial term and common diﬀerence

41

are coprime integers contains inﬁnitely many prime numbers (we take absolute

values of the terms).

In the proof of Theorem 2.1 we will use a well-known fact that the terms of linear

recurrence sequence can be expressed by the roots of the characteristic equation.

In our notation the characteristic equation is

x2 − ax − b = 0. (2)

Let α := (a + √
D)/2 and β := (a − √D)/2, where √D is deﬁned as i
√−D for

D < 0, be two roots of the characteristic equation, i.e., x2−ax−b = (x−α)(x−β),

and let discriminant of that equation be

D := (α − β)
2 = a2 + 4b. (3)

By (2) and (3), we have α − β = √D, αβ = −b and α + β = a. It is easily seen

that, for each n ∈ N, the nth term of the sequence (xn)
∞
n=1 deﬁned in (1) is given

by
 xn = −x1β + x2
α − β αn−1 + x1α − x2
α − β βn−1 (4)

provided that α ̸= β, i.e., D ̸= 0. Indeed, (4) is correct for n = 1 and 2. Since

αn−1 and βn−1 satisfy the recurrence (1), so does the right side of the equality (4)

for n = 2, 3, . . . . Hence, both sequences, deﬁned by the two sides of the equality

(4), are given by the same two initial values and the same recurrence. Therefore,

they coincide.

Similarly, for α = β, i.e., D = 0 we have

xn = (2x1 − x2α−1 + n(x2α−1 − x1))αn−1 (5)

for each n ∈ N.

We deal with the cases |b| > 1 and |b| = 1 separately.

In the ﬁrst case deal with in Section 2.2 the following observation is useful.

Let b divide x2. If xn+1 = axn + bxn−1, n = 2, 3, 4, . . . , then b divides xk, for

k = 2, 3, 4, . . . . If |xk| > b, we have that |xk| is composite. In case |b| ⩾ 2 we shall

take x2 divisible by |b|. The main diﬃculty is to show that x1 can be chosen so that

xn ̸= 0, b, −b for each n ⩾ 3, so that |xn| is composite. To see that the condition

|xk| > b holds is not very diﬃcult if the roots of the characteristic equation are

real. However, for negative discriminant the argument is more sophisticated.

42

The second case dealt with in Section 2.3 will require the use of divisibility

sequences and covering systems.

Definition 2.2. A sequence of rational integers (vn)
∞
n=1 is called a divisibility

sequence if vr divides vs whenever r divides s.

The Fibonacci sequence is a divisibility sequence. A more general example of a

divisibility sequence is called the Lucas sequence of the ﬁrst kind. Assume that

the roots α, β of the characteristic equation (2) are distinct α ̸= β. Then

un := αn − βn

α − β ∈ Z, (6)

n = 1, 2, 3, . . . , is a divisibility sequence. Indeed, if r divides s then, setting

l := s/r ∈ N, we see that

us
ur = αrl − βrl

αr − βr = αr(l−1) + αr(l−2)βr + · · · + βr(l−1)

is a symmetric function in α, β. Hence us/ur ∈ Z, giving ur|us. If (xn)
∞
n=1 is a

sequence given by the linear recurrence (1) then one can consider a corresponding

divisibility sequence, by selecting u1 := 1, u2 := a. This sequence is the Lucas

sequence of the ﬁrst kind.

From (1) and (6) one can calculate the terms of the Lucas sequence as follows:

u3 = au2 + bu1 = a2 + b,

u4 = au3 + bu2 = a(a2 + b) + ba = a(a2 + 2b),

u6 = u3(α3 + β3) = u3((α + β)3 − 3αβ(α + β)) = a(a2 + b)(a2 + 3b),

u12 = u6(α6+β6) = u6((α3+β3)
2−2(αβ)3) = a(a2+b)(a
2+2b)(a2+3b)(a4+4a2b+b2).

To obtain the last equality we used the identity

(a(a2 + 3b))
2 + 2b3 = (a2 + 2b)(a4 + 4a2b + b2).

Definition 2.3. A collection of residue classes

ri (mod mi) := {ri + mik | k ∈ Z},

where mi ∈ N, ri ∈ Z, 0 ⩽ ri < mi, and i = 1, . . . , t, is called a covering system

if every integer n ∈ Z belongs to at least one residue class ri (mod mi), where

1 ⩽ i ⩽ t.
 43

For example, 0 (mod 2), 1 (mod 2) is a covering system. A more interesting

example, used in our proof, is this covering system:

0 (mod 2), 0 (mod 3), 3 (mod 4), 5 (mod 8), 5 (mod 12), 1 (mod 24).

At the end of our proof we also consider the question of choosing the required

pair of the smallest possible initial values x1, x2 ofr some certain recurrence se-

quences. The pair (x1, x2) found by Graham in [15] for the case (a, b) = (1, 1)

later has been reduced from

(331635635998274737472200656430763, 1510028911088401971189590305498785)

to
 (x1, x2) = (106276436867, 35256392432). (7)

We too indicate the pairs of initial values smaller than those given by our general

method for certain sequences.

Proof of Theorem 2.1

2.1. Several exceptional cases.

In this section we prove that Theorem 2.1 does not hold for (a, b) = (±2, −1).

Then we start the proof of Theorem 2.1 with three special cases: (i) D = 0; (ii)

a = 0; (iii) b = −1, |a| ⩽ 2.

Let (a, b) = (±2, −1). It is easy to see that in this case the sequence (|xn|)∞
n=1,

where x1, x2 are composite and gcd(x1, x2) = 1, contains inﬁnitely many prime

numbers. Indeed, by (5),

xn = (2x1 − x2ε + n(x2ε − x1))εn−1

for each n ⩾ 1 and ε = ±1. Since x1 and x2 are relatively prime positive compos-

ite integers, we must have u := 2x1 − x2ε ̸= 0 and v := x2ε − x1 ̸= 0. Moreover,

gcd(x1, x2) = 1 implies gcd(u, v) = 1. So, by Dirichlet’s theorem on prime num-

bers in arithmetic progressions, we conclude that |xn| = |vn+u| is a prime number

for inﬁnitely many n ∈ N. This not only completes the proof of Theorem 2.1 in

the case D = 0, but also shows that the condition (a, b) ̸= (±2, −1) is necessary.

Case (i). Since D = a2 + 4b = 0, the solution of the linear recurrence (2.1) is

44

given by (5). Note that a = 2α and b = −α2. So α is a nonzero integer. We shall

split the proof into two cases |α| ⩾ 2 and |α| = 1.

In the ﬁrst case, |α| ⩾ 2, let us take two distinct primes p, q satisfying p, q > |α|

and select x1 := p2, x2 := |α|q2. Then x1, x2 are composite and gcd(x1, x2) = 1.

Furthermore, writing |α| = αε, where ε = ±1, by (5), we obtain

xn = (2p2 − q2ε + n(q2ε − p2))αn−1

for each n ⩾ 1. Clearly, |xn| is divisible by |α2| = |b| ⩾ 4 for n ⩾ 3, so |xn| is

composite for each n ∈ N, unless

2p2 − q2ε + n(q2ε − p2) = 0

for some n. But this equality cannot hold for n ∈ N. Indeed, if ε = −1, then

n = 2p2 + q2

p2 + q2 = 1 + p2

p2 + q2

is greater than 1 and smaller than 2, a contradiction. If ε = 1, then (n − 1)q2 =

(n − 2)p2 implies n − 1 = ℓp
2 and n − 2 = ℓq2 with ℓ ∈ Z. Hence 1 = (n − 1) −

(n − 2) = ℓ(p2 − q2), which is impossible, because p, q|α| ⩾ 2 yields |p2 − q2| ⩾

|5
2 − 3
2| = 16 > 1. Suppose next that α = ±1. Then b = −α2 = −1 and a = ±2.

This case is not allowed by the condition of the theorem.

Case (ii). For a = 0, we have xn+1 = bxn−1 for n ⩾ 2. Let p, q > |b| be

two distinct primes. Selecting x1 := p2 and x2 := q2, we have gcd(x1, x2) = 1.

Furthermore, x2k−1 = p2bk−1 and x2k = q2bk−1 for each k ⩾ 1, so |xn| is composite

for every n ∈ N.

Case (iii). The cases (a, b) = (±2, −1) and (a, b) = (0, −1) are already covered

by Case (i) and Case (ii), respectively. If (a, b) = (−1, −1) the recurrence sequence

xn+1 = −xn − xn−1 satisfying the condition of the theorem is, for example, the

following periodic sequence:

9, 16, −25, 9, 16, −25, 9, 16, −25, . . . .

For (a, b) = (1, −1), we have the recurrence xn+1 = xn − xn−1. Now, the periodic

sequence
 16, 25, 9, −16, −25, −9, 16, 25, 9, −16, −25, −9, . . .

satisﬁes the conditions of the theorem.
 45

2.2. The case |b| ⩾ 2.

In this Section we prove the lemmas below and, afterwards, Theorem 2.1 in the

case |b| ⩾ 2.

Lemma 2.4. Let d and ℓ be two positive integers. Then there is a positive

integer c and three distinct odd prime numbers p, q, r such that pqr divides d + c2

and gcd(pqr, ℓc) = 1.

Proof of Lemma 2.4: Given h ∈ Z and a prime number p, let ( h
p ) be the

Legendre symbol. Take three distinct prime numbers p, q, r greater than max(d, ℓ)

such that ( −d
p
 ) = ( −d
q
 ) = (−d
r
 ) = 1.

(For example, one can take the prime numbers p, q, r in the arithmetic progression

4kd + 1, k = 1, 2, . . . .) Then there are three positive integers c1, c2, c3 such that

c2
1 ≡ −d (mod p), c
2
2 ≡ −d (mod q), c
2
3 ≡ −d (mod r). By the Chinese remainder

theorem, there is a positive integer c such that c ≡ c1 (mod p), c ≡ c2 (mod q),

c ≡ c3 (mod r). Then c2 ≡ −d (mod pqr). This proves that pqr divides d + c2.

Since p, q, r > ℓ, none of the primes p, q, r divides ℓ. Assume that p|c. Then

p|(d + c2) implies p|d, which is impossible, because p > d. By the same argument,

q and r do not divide c. This completes the proof of gcd(pqr, ℓc) = 1. □

Lemma 2.5. Let ui, vi, i = 1, 2, . . . , p − 1, and s be the elements of the ﬁeld

Fp, where p is a prime number. Assume that for each i at least one of ui, vi is

nonzero. Then there exist u, v ∈ Fp such that at least one of u, v is nonzero and

uui + vvi ̸= s for each i = 1, . . . , p − 1.

Proof of Lemma 2.5: Fix an index i in the range 1 ⩽ i ⩽ p − 1. We claim that

there are exactly p pairs (u, v) ∈ F2
p for which

uui + vvi = s. (8)

Indeed, if ui = 0, then vi ̸= 0 and (u, sv∗
i ), where u ∈ Fp and v∗
i is the inverse

element of vi in Fp, are the solutions of (8). By the same argument, (8) has p

solutions if vi = 0. Finally, if ui ̸= 0 and vi ̸= 0, then we can take any u ∈ Fp and

the linear equation (8) has a unique solution in v. This proves the claim.

46

As i runs through 1, . . . , p − 1, we have p − 1 equations (8) which all together

have at most p(p − 1) distinct solutions (u, v) ∈ F2
p. But F2
p consists of the pair

(0, 0) and p2 − 1 pairs (u, v) with at least one u, v nonzero. Since p2 − 1 > p(p − 1),

there exists a pair (u, v) ∈ F2
p as required, namely, u ̸= 0 or v ̸= 0 and uui +vvi ̸= s

for each i = 1, . . . , p − 1. □

Lemma 2.6. Let c > 0, D < 0 and a be three integers. Suppose that p is an odd

prime number which divides −D + c2 but does not divide c. Then the sequence of

rational integers
 sn := (a + √D)
n − (a − √
D)
n

2
√D , (9)

n = 1, 2, 3, . . . , is purely periodic modulo p with period p − 1. Also, no two con-

secutive elements of the sequence (sn)
∞
n=1 can be zeros modulo p.

Proof of Lemma 2.6: By (9), we have

sn =
 [(n−1)/2]∑

k=0
 ( n
2k + 1
)
an−2k−1Dk,

where 00 is deﬁned as 1. Since D ≡ c2 (mod p) and

[(n−1)/2]∑

k=0
 ( n
2k + 1
)
an−2k−1c2k = (a + c)
n − (a − c)n

2c ,

we ﬁnd that
 sn ≡ (a + c)
n − (a − c)
n

2c (mod p). (10)

Since p and 2c are relatively prime, it remains to show that, for each n ⩾ 1, we

have
 (a + c)
n+p−1 − (a − c)
n+p−1 ≡ (a + c)
n − (a − c)
n (mod p).

Indeed, by Fermat’s little theorem, p divides both the numbers (a + c)
n+p−1 − (a +

c)
n = (a + c)
n((a + c)p−1 − 1) and (a − c)
n+p−1 − (a − c)
n, so p also divides their

diﬀerence. This proves the periodicity.

For the second statement of the lemma, assume that sn ≡ 0 (mod p) and

sn+1 ≡ 0 (mod p) for some n ∈ N. Then, by (10), (a + c)n ≡ (a − c)n (mod p)

and (a + c)
n+1 ≡ (a − c)
n+1 (mod p). If a ≡ c (mod p) then a ≡ −c (mod p),

so p divides 2c, which is not the case by the condition of the lemma. Similarly, a

and −c modulo p are distinct. Hence, from

(a − c)n+1 ≡ (a + c)
n+1 ≡ (a + c)
n(a + c) ≡ (a − c)
n(a + c) (mod p),

47

we ﬁnd that a + c ≡ a − c (mod p). Once again this yields p|2c, a contradiction.

□
 Lemma 2.7. Let (xn)
∞
n=1 be a sequence of integers given by (1), D = a2 +4b ̸= 0,

b ̸= 0, and let δ be a ﬁxed real number. Then xn+1 = δb for some n ⩾ 2 if and

only if
 x1 sn−1
2n−2 + x2
b sn
2n−1 = δ,

where sn is given by (9).

Proof of Lemma 2.7: The roots α and β of the characteristic equation (2) are

distinct, so, by (4) and α − β = √
D, we have

xn+1√D = (−x1β + x2)αn + (x1α − x2)βn (11)

for each n ⩾ 0. Since 2α = a + √D and 2β = a − √D, using (9), we ﬁnd that

αn − βn = 2
1−n√
Dsn. Since αβ = −b, equality (11) yields

xn+1√
D = x2(αn − βn) − x1αβ(αn−1 − βn−1) = x22
1−nsn√D + x1b2
2−nsn−1√D.

Hence xn+1 = x1b2
2−nsn−1 + x22
1−nsn, because D ̸= 0. It follows that equality

xn+1 = δb is equivalent to
 δ = x1 sn−1
2n−2 + x2
b sn
2n−1 ,

as claimed. □

Lemma 2.8. Let (xn)∞
n=1 be a sequence of integers given by (1), where a ̸= 0 and

D > 0. Then, for each K > 0 and each x1, there is a constant λ(K, α, β, x1) > 0

such that by selecting the two ﬁrst terms of the sequence (1) as x1 and x2 >

λ(K, α, β, x1) we have |xn| > K for each n ⩾ 2.

Proof of Lemma 2.8: Since D > 0 and a = α + β ̸= 0, we have |α| ̸= |β|.

Suppose that |α| > |β|. (The proof in the case |α| < |β| is the same.) From

αβ = −b, we obtain |α| > √
|b| ⩾ 1. Hence, by (11), using several times the

triangle inequality, for n ⩾ 1, we obtain

|xn+1|
√D ⩾ |(−x1β+x2)αn|−|(x1α−x2)βn| = |bx1+x2α||α|
n−1−|−bx1−x2β||β|
n−1

⩾ (|bx1 + x2α| − |bx1 + x2β|)|α|
n−1 ⩾ (|bx1 + x2α| − |bx1 + x2β|)|α|
n−1

⩾ (|x2α| − |bx1| − |bx1| − |x2||β|)|α|
n−1 = (|x2|(|α| − |β|) − 2|bx1|)|α|
n−1.

48

Since |α|
n−1 ⩾ 1 for n ⩾ 1, the last expression is greater than K√D provided

that |x2|(|α| − |β|) > 2|bx1| + K√D. So the lemma holds with

λ(K, α, β, x1) := 2|bx1| + K√
D
|α| − |β| (12)

when |α| > |β|. Evidently, the constants b, D appearing in the right hand side of

(12) depend on α, β too, because b = −αβ and D = a2 + 4b = (α − β)
2, by (2),

(3). □

Lemma 2.9. Let a1 ⩾ 0 and b1, b2 ⩾ 1 be integers such that no prime number p

divides the three numbers a1, b1, b2. Then, for each K > 0, there exists an integer

k1K such that b1k1 + a1 is a composite integer relatively prime to b2.

Proof of Lemma 2.9: The lemma is trivial if a1 = 0. Assume that a1 ⩾ 1.

Set t := gcd(b1, a1). By the condition of the lemma, t is relatively prime to b2.

By Dirichlet’s theorem about prime numbers in arithmetic progressions, there

is a t1 ∈ N such that (b1/t)t1 + a1/t is a prime number greater than b2. Then

b1t1 + a1 = t((b1/t)t1 + a1/t) is relatively prime to b2. This implies that, for any

s ∈ N, the number
 b1b2s + b1t1 + a1 = b1(b2s + t1) + a1

is relatively prime to b2. Of course, there are inﬁnitely many s ∈ N for which the

number b1b2s + b1t1 + a1 is composite. It remains to take one of those s ∈ N for

which k1 := b2s + t1 > K. □

We begin the proof of the theorem for |b| ⩾ 2 from the more diﬃcult case when

the discriminant D = a2 +4b is negative. Let us apply Lemma 2.4 to d := −D and

ℓ := |b|. Then, by Lemma 2.4, there exist a positive integer c and three distinct

odd primes p, q, r such that pqr divides −D + c2 and

gcd(pqr, |b|c) = 1. (13)

Our aim is to choose two composite relatively prime positive integers x1, x2 so that

|b| divides x2 and xn+1 /∈ {0, b, −b} for each n ⩾ 2. Then |x1| = x1 and |x2| = x2

are composite. Also, using (1), by induction on n we see that |b| divides xn+1 for

each n ⩾ 1. Since xn /∈ {0, b, −b} for n ⩾ 3 and |b| divides xn for n ⩾ 2, we must

have |xn| > |b| for each n ⩾ 3. Hence |xn| is a composite integer for every n ⩾ 3

too.
 49

For a contradiction, assume that, for some n ⩾ 1, xn+2 = δb with δ ∈ {0, 1, −1}.

Then, by Lemma 2.7, we have

x1 sn
2n−1 + x′
2 sn+1
2n = δ, (14)

where x′
2 := x2/b and n ∈ N. Firstly, let us choose x1, x
′
2 modulo p so that

2x1sn + x′
2sn+1 ̸= 0, n ∈ N. (15)

This is possible by combining Lemma 2.6 with Lemma 2.5. Indeed, by Lemma 2.6,

the sequence sn (mod p), n = 1, 2, 3, . . . , is purely periodic with period p − 1. So,

by Lemma 2.5 applied to the pairs (2s1, s2), (2s2, s3), . . . , (2sp−1, sp) ∈ F2
p and

s = 0, we conclude that there are x1, x
′
2 ∈ Fp, not both zeros in Fp, such that (15)

holds.

Next, we shall choose x1, x
′
2 ∈ Fq so that

2x1sn + x′
2sn+1 ̸= 2
n, n ∈ N, (16)

in Fq. As above, by Lemma 2.6, the sequence sn2
1−n (mod q), n = 1, 2, 3, . . . ,

where 2
1−n is the inverse of 2n−1 in Fq, is purely periodic with period q − 1. By

Lemma 2.5 applied to the pairs (s1, 2
−1s2), (s22
−1, s32
−2), . . . , (sq−12
−(q−2), sq2
−(q−1)) ∈

F2
q and s = 1, we conclude that there are x1, x
′
2 ∈ Fq, not both zeros, such that

(16) holds. By the same argument, there are x1, x
′
2 ∈ Fr, not both zeros, such

that
 2x1sn + x′
2sn+1 ̸= −2
n, n ∈ N, (17)

in Fr.

By the Chinese remainder theorem, combining (15), (16), (17), we see that

there exist two congruence classes a1 (mod pqr) and a2 (mod pqr) such that for

any integers x1 and x′
2 that belong to the ﬁrst and the second class, respectively,

equality (14) does not hold for n ∈ N. Furthermore, by Lemma 2.5, each prime

number p, q, r divides at most one of the integers a1, a2. It remains to select k1, k2 ∈

Z so that x1 = pqrk1+a1 and x2 = bx′
2 = b(pqrk2+a2) are two composite relatively

prime positive integers. Take k2 ∈ Z such that |pqrk2 + a2| > 1, bk2 > 0. Then

x2 > 0 is a composite number. Furthermore, no prime number divides the three

numbers pqr, a1 and x2, because the primes p, q, r do not divide |b|, by (13), and

if, say, p|a1 then p does not divide pqrk2 + a2. Hence, by Lemma 2.9 applied to

the triplet b1 := pqr, a1, b2 := x2, we may select k1 ∈ N so that x1 = pqrk1 + a1

50

is a composite integer relatively prime to x2. This proves the theorem for |b| ⩾ 2,

D < 0.

The case when D = a
2 + 4b > 0 is easier. As above, we need to choose two

composite relatively prime positive integers x1, x2 such that |b| divides x2 and

show that this choice leads to xn+1 /∈ {0, b, −b} for each n ⩾ 2. If |α| = |β|, then

α = −β, so a = α + β = 0. This case is already settled in Section 2. Assume next

that |α| ̸= |β|. Take x1 := p2 and x2 := b2q, where p, q > |b| are prime numbers

and q is so large that b2q is greater than the constant λ(|b|, α, β, p
2) given in

(12). Then, by Lemma 2.8, |xn+1| > |b| for n ⩾ 2. This completes the proof of

Theorem 2.1 in case |b| ⩾ 2.

2.3. Divisibility sequences, covering systems and the case |b| = 1.

In this Section we use divisibility sequences and covering systems to prove the

lemmas below and, afterwards, Theorem 2.1 in the case |b| = 1.

Lemma 2.10. If b = −1 and |a| ⩾ 4 then there exist ﬁve distinct prime numbers

pi, i = 1, . . . , 5, such that p1|u2, p2|u3, p3|u4, p4|u6 and p5|u12.

Proof of Lemma 2.10: Let p1 be any prime divisor of u2 = a, and let p2 ̸= 2 be

any prime divisor of u3 = a2 − 1 = (a − 1)(a + 1). Such p2 exists, because |a| ⩾ 4.

Clearly, p2 ̸= p1. Since a2 − 2 is either 2 or 3 modulo 4, it is not divisible by 4. So

a2 − 2 must have an odd prime divisor p3. Clearly, p3 ̸= p1. Furthermore, p3 ̸= p2,

because gcd(a2 − 1, a
2 − 2) = 1. We select this p3 as a divisor of u4. Observing

that 9 does not divide a2 − 3, we get that there is prime number p4 ̸= 3 that

divides a2 − 3. Since gcd(a, a
2 − 3) is either 1 or 3, this yields p4 ̸= p1. Also, since

gcd(a2 − 1, a
2 − 3) is either 1 or 2, we may have p4 = p2 only if p2 = 2, which is not

the case. So p4 ̸= p2. The fact that p4 ̸= p3 follows from gcd(a2 − 2, a
2 − 3) = 1.

We select this p4 as a divisor of u6.

It remains to show that there is a prime divisor p5 of a4 − 4a2 + 1 distinct from

pi, i = 1, . . . , 4. Note that a4 − 4a2 + 1 is not zero modulo 4 and modulo 3. Hence

there is a prime number p5 ̸= 2, 3 that divides a4 − 4a2 + 1 ⩾ 4
4 − 4
3 + 1 = 193.

Evidently, p5 ̸= p1. Writing

a4 − 4a2 + 1 = (a2 − 1)(a2 − 3) − 2

51

and using p5 ̸= 2, we may conclude that p5 ̸= p2, p4. Similarly, from a4 − 4a2 + 1 =

(a2 − 2)2 − 3 and p5 ̸= 3, we see that p5 ̸= p3. □

One can easily check that Lemma 2.10 does not hold for |a| = 3. The next

lemma is very similar to that above.

Lemma 2.11. If b = 1 and |a| ⩾ 2 then there exist ﬁve distinct prime numbers

pi, i = 1, . . . , 5, such that p1|u2, p2|u3, p3|u4, p4|u6 and p5|u12.

Proof of Lemma 2.11: Take any prime divisor p1 of u2 = a. Let p2 ̸= 2 be any

prime divisor of u3 = a2 + 1. Such p2 exists, because a2 + 1 is not divisible by 4.

Evidently, p2 ̸= p1. Similarly, let p3 ̸= 2 be any prime divisor of a2 + 2. Clearly,

p3 ̸= p2. Since gcd(a, a
2 + 2) is either 1 or 2, p3 = p1 only if they both are equal

to 2, which is not the case. So we may select this p3 as a divisor of u4. Observing

next that 9 does not divide a2 + 3, we deduce that there is prime number p4 ̸= 3

that divides a2 + 3. Since gcd(a, a
2 + 3) is either 1 or 3, this yields p4 ̸= p1. Also,

since gcd(a2 + 1, a
2 + 3) is either 1 or 2, we may have p4 = p2 only if p2 = 2,

which is not the case. Hence p4 ̸= p2. As above, the fact that p4 ̸= p3 follows from

gcd(a2 + 2, a
2 + 3) = 1. We select this p4 as a divisor of u6.

It remains to show that there is a prime divisor p5 of a
4 + 4a2 + 1 which is

distinct from pi, i = 1, . . . , 4. Note that a4 + 4a2 + 1 > 6 is not zero modulo 4 and

modulo 9. Hence there is a prime p5 ̸= 2, 3 that divides a4 + 4a2 + 1. Evidently,

p5 ̸= p1. Writing
 a4 + 4a2 + 1 = (a2 + 1)(a2 + 3) − 2

and using p5 ̸= 2, we may conclude that p5 ̸= p2, p4. Finally, from a4 + 4a2 + 1 =

(a2 + 2)2 − 3 and p5 ̸= 3, it follows that p5 ̸= p3. □

To illustrate Lemma 2.11, let us take (a, b) = (±2, 1). Then u2 = ±2, u3 = 5,

u4 = ±2
2 · 3, u6 = ±2 · 5 · 7 and u12 = ±2
2 · 3
2 · 5 · 7 · 11. Hence Lemma 2.11 holds

with p1 = 2, p2 = 5, p3 = 3, p4 = 7, p5 = 11.

The next lemma uses the concept of covering systems introduced by Erd˝os. In

the proof of the theorem for |b| = 1 we shall use the following well-known covering

system

0 (mod 2), 0 (mod 3), 1 (mod 4), 5 (mod 6), 7 (mod 12). (18)

Lemma 2.12. Let ri (mod mi), i = 1, . . . , t, be a covering system, and let

(un)∞
n=1 be a divisibility sequence given by u1 := 1, u2 := a and un+1 = aun + bun−1

52

for n = 2, 3, . . . , where a ∈ Z, b = ±1 and D = a2 + 4b > 0. Suppose that there

exist t distinct prime numbers p1, . . . , pt such that pi|umi for each i = 1, . . . , t.

Then there are two relatively prime composite positive integers x1, x2 such that

each |xn|, n ∈ N, where xn is a sequence deﬁned in (1), is a composite number.

Proof of Lemma 2.12: By the Chinese remainder theorem, there exist s, l ∈ Z

satisfying
 s ≡ umi−ri (mod pi),

l ≡ umi−ri+1 (mod pi)

for i = 1, . . . , t. Note that two consecutive terms of the sequence (un)
∞
n=1 cannot

be divisible by the same prime number p. Indeed, if p|un and p|un+1 then using

b = ±1 from un+1 = aun + bun−1 we ﬁnd that p|un−1. By the same argument,

p|un−2 and so on. Hence p|u1, a contradiction.

So, for every x1 in the residue class s (mod P ), where P = p1 . . . pt, and for every

x2 in the residue class l (mod P ), we have x1 ≡ umi−ri (mod pi) and x2 ≡ umi−ri+1

(mod pi) for i = 1, . . . , t. By induction on n, this implies

xn+1 ≡ umi−ri+n (mod pi) (19)

for each n ⩾ 0 and each i = 1, . . . , t. Since ri (mod mi), i = 1, . . . , t, is a covering

system, every non-negative integer n belongs to certain residue class ri (mod mi),

where i is some of the numbers 1, . . . , t. Fix one of those i and write n = ri + kmi,

where k ⩾ 0. Note that pi|umi(k+1), because pi|umi and umi|umi(k+1). Thus (19)

yields
 xn+1 ≡ umi(k+1) (mod pi) ≡ 0 (mod pi),

giving pi|xn+1.

It remains to choose two composite relatively prime positive integers x1 ≡ s

(mod P ) and x2 ≡ l (mod P ) so that |xn| > max(p1, . . . , pt) for every n ∈ N.

Then each |xn| is divisible by some pi and greater than pi, so it is a composite

number. To do this let us choose a composite integer x1 > max(p1, . . . , pt) sat-

isfying x1 ≡ s (mod P ). Then we can select x2 ≡ l (mod P ) as required, by

Lemma 2.8 and Lemma 2.9, where a1 := l, b1 := P, b2 := x1, because no prime

number p1, . . . , pt divides both s and l. □

53

Now, we shall prove the theorem for |b| = 1. Suppose ﬁrst that b = −1 and

|a| ⩾ 4. Then, by Lemma 2.10, there are ﬁve distinct primes p1, . . . , p5 dividing

u2, u3, u4, u6, u12, respectively. Since D = a2 − 4 > 0, the theorem follows from

Lemma 2.12 applied to the covering system (18). Similarly, if b = 1 and |a| ⩾ 2

we also have D = a2 + 4b = a2 + 4 > 0, so the theorem follows by Lemmas 2.11

and 2.12.

Recall that the cases b = −1, |a| ⩽ 2 and b = 1, a = 0 have been considered

in Section 2. In Section 1 we already described the literature concerning the case

(a, b) = (1, 1). So three cases that remain to be considered are (a, b) = (−1, 1),

(a, b) = (−3, −1), (a, b) = (3, −1).

We begin with the case (a, b) = (−1, 1). Vsemirnov’s pair (7) of two composite

relatively prime integers

V1 := 106276436867, V2 := 35256392432

shows that the numbers

Vn = Vn−1 + Vn−2 = Fn−1V2 + Fn−2V1, n ⩾ 2, (20)

are all composite. Here, Fn is the nth Fibonacci number, F0 := 0. For the

sequence xn+1 = −xn + xn−1, we clearly have

xn = (−1)
nFn−1x2 + (−1)
n−1Fn−2x1, n ⩾ 3. (21)

Selecting x1 := −V2 + V1 = 71020044435 and x2 := V1 = 106276436867, one can

easily check that x1 and x2 are relatively prime composite integers. Moreover, by

(20) and (21),

xn = (−1)
nFn−1V1 + (−1)
n−1Fn−2(−V2 + V1) = (−1)
nFn−2V2 + (−1)nFn−3V1

= (−1)n(Fn−2V2 + Fn−3V1) = (−1)
nVn−1

for n ⩾ 3. Thus |xn| = Vn−1 is also composite integer for each n ⩾ 3.

For (a, b) = (−3, −1), we use the covering system

1 (mod 2), 1 (mod 3), 0 (mod 4), 6 (mod 8), 6 (mod 12), 2 (mod 24).

The divisibility sequence (un)∞
n=1 is given by u1 := 1, u2 := −3 and un+1 = −3un −

un−1, n = 2, 3, . . . . We select the following primes dividing u2, u3, u4, u8, u12, u24,

54

respectively: 3, 2, 7, 47, 23, 1103. By the method described in Lemma 2.12, we

calculated the pair
 (x1, x2) = (13271293, 219498)

satisfying the conditions of the theorem.

For (a, b) = (3, −1), we use the covering system

0 (mod 2), 0 (mod 3), 3 (mod 4), 5 (mod 8), 5 (mod 12), 1 (mod 24).

As above, the primes dividing u2, u3, u4, u8, u12, u24 are 3, 2, 7, 47, 23, 1103, respec-

tively. This time, using the method described in Lemma 2.12, we found the pair

(x1, x2) = (7373556, 2006357)

satisfying the conditions of the theorem. The proof of Theorem 2.1 is thus com-

pleted. □

Below, we shall ﬁnd smaller solutions for (a, b) = (±3, −1). Instead of using

Lemma 2.12, we may directly search for a pair of relatively prime positive integers

x1, x2 such that each of the ﬁrst 24 elements of the sequence (1) is divisible by at

least one of the primes 3, 2, 7, 47, 23, 1103. Then we may choose a covering system

ri (mod mi), where m1 = 2, m2 = 3, m3 = 4, m4 = 8, m5 = 12, m6 = 24, and

i = 1, . . . , 6, such that, for each n in the range 0 ⩽ n ⩽ 23 and each i in the range

1 ⩽ i ⩽ 6, n + 1 ≡ ri (mod mi) implies pi|xn+1. This would be enough for pi|xn+1

to hold for any n + 1, n ⩾ 0, belonging to the residue class ri (mod mi). Using

this direct method, we found smaller pairs (x1, x2) producing sequences consisting

of composite numbers.

For (a, b) = (−3, −1), by selecting the residues of the covering system as

(r1, r2, r3, r4, r5, r6) = (1, 1, 0, 2, 6, 14)

and searching over x1 divisible by 7 and x2 divisible by 2 and 3, we found the pair

(x1, x2) = (35, 3294).

One can easily check that

1 (mod 2), 1 (mod 3), 0 (mod 4), 2 (mod 8), 6 (mod 12), 14 (mod 24)

is indeed a covering system. Also, if n+1, where n ⩾ 0, belongs to the residue class

ri (mod mi) we use the fact that pi|xn+1. This explains why we take x1 divisible

55

by 7 and x2 divisible by 6. It is clear that gcd(x1, x2) = gcd(35, 3294) = 1. Also,

|xn| > max(p1, . . . , p6) = 1103 for n ⩾ 2, so |xn| is composite for each n ∈ N.

Selecting (r1, r2, r3, r4, r5, r6) = (0, 0, 1, 7, 7, 11), we found the symmetric pair

(x1, x2) = (3294, 35). Similarly, taking (r1, r2, r3, r4, r5, r6) = (0, 2, 1, 3, 3, 7), we

established that
 (x1, x2) = (2367, 3031)

is also such a pair. Note that 3294 + 35 < 2367 + 3031. On the other hand,

max(3294, 35) > max(2367, 3031). In the same way, using (r1, r2, r3, r4, r5, r6) =

(1, 2, 0, 6, 10, 18), we found the symmetric pair (x1, x2) = (3031, 2367).

For (a, b) = (3, −1), selecting (r1, r2, r3, r4, r5, r6) = (0, 2, 1, 3, 7, 15), we found

the pair
 (x1, x2) = (3399, 35).

Choosing the residues (r1, r2, r3, r4, r5, r6) = (1, 2, 0, 6, 6, 10), we arrived to the

symmetric pair (x1, x2) = (35, 3399).
 56

3. Egyptian fractions and numbers expressible by a

special linear form

Let t be a ﬁxed positive integer. In this Section we consider the set of positive

integers
 E(t) := {n ∈ N : n = tM − d},

where M is a positive multiple of the product and d is a positive divisor of the

sum of two positive integers, namely,

ab|M and d|(a + b)

for some a, b ∈ N. Evidently,

E(t
′) ⊆ E(t) whenever t|t
′.

It is easy to see that
 E(1) = E(2) = N. (22)

Indeed, suppose ﬁrst that t = 1. Then, for each n ∈ N selecting a = 2n + 1, b = 1,

M = ab = 2n + 1 and d = (a + b)/2 = n + 1, we ﬁnd that

n = 2n + 1 − (n + 1) = M − d,

giving E(1) = N. In case t = 2, for each n ∈ N we may choose a = n + 1, b = 1,

M = ab = n + 1 and d = a + b = n + 2. Then 2M − d = 2(n + 1) − (n + 2) = n,

so that E(2) = N.

Apart from (22) the situation with t ⩾ 3 is not clear. In this context, the sets

E(4) and E(5) are of special interest, because an integer n belongs to the set E(t)

if and only if
 n = tM − d = tuab − (a + b)/v

with some a, b, u, v ∈ N. Therefore, n ∈ E(t) yields the representation

t
n = 1
x + 1
y + 1
z

with positive integers
 x := uab, y := uvna, z := uvnb.

57

Thus this leads us to the subject of Egyptian fractions (the sums of distinct

unit fractions) and the related famous conjectures. If n ∈ E(t) then t/n is ex-

pressible as the sum of three unit fractions. In particular, if every prime number p

belongs to the set E(4) then the Erd˝os-Straus conjecture (asserting that for each

integer n ⩾ 2 the fraction 4/n is expressible by the sum 1/x + 1/y + 1/z with

x, y, z ∈ N) is true, whereas if every prime number p belongs to E(5) then the

corresponding conjecture of Sierpi´nski (asserting that for each n ⩾ 4 the fraction

5/n is expressible by the sum 1/x + 1/y + 1/z) is true [29]. In this context the

most general Schinzel’s conjecture asserts that the fraction t/n for each n ⩾ n(t)

is expressible by the sum 1/x + 1/y + 1/z. This clearly holds for t ⩽ 3 but is

open for each ﬁxed t ⩾ 4. Conjecture 3.5 below implies that there is an integer

C(t) such that each prime number p > C(t) belongs to E(t). This would imply

Schinzel’s conjecture as well.

In this note we observe that

Theorem 3.1. The set E(4) does not contain perfect squares and the numbers

288, 336, 4545.

Suppose k2 ∈ E(4), i.e., there exist u, v, a, b ∈ N such that

v(4uab − k2) = a + b. (23)

To show that k2 /∈ E(4) we shall use the fact that

Lemma 3.2. The equation (23) has no solutions in positive integers u, v, a, b, k.

Lemma 3.2 implies that −d is a quadratic nonresidue modulo 4ab if d|(a + b).

Indeed, if the number −d were a quadratic residue modulo 4ab then selecting the

positive integer v := (a + b)/d we see that the equation k2 = −d + 4uab with some

u ∈ N has a solution k ∈ N, which is impossible in view of Lemma 3.2. Note that

the set of divisors of a + b, when a < b both run through the set {1, 2, . . . , n},

contains the set {1, 2, . . . , 2n − 1}. Thus, by Lemma 3.2, we ﬁnd that

Corollary 3.3. For each positive integer n the 2n − 1 consecutive integers

4n! − 2n + 1, 4n! − 2n + 2, . . . , 4n! − 1

are quadratic nonresidues modulo 4n!.
 58

Corollary 3.3 gives the example of at least (2 − ε) log m/ log log m consecutive

quadratic nonresidues modulo m = 4n! (by using Stirling’s approximation n! ∼
√2πn nn
en ).

As we already observed in (22), the sets N \ E(1) and N \ E(2) are empty. By

Lemma 3.2 the equation v(4uab − k2) = a + b has no solutions in positive integers

u, v, a, b, k. In particular, if t is a positive integer divisible by 4 and s ∈ N is such

that 4s|t then the equation vs(4(t/4s)uab−k2) = a+b has no solutions in positive

integers u, v, a, b, k. The latter is equivalent to the equation v(tuab − sk2) = a + b.

Consequently, we obtain that

Corollary 3.4. The set E(t), where 4|t, does not contain the numbers of the

form sk2, where s ∈ N satisﬁes 4s|t and k ∈ N.

In particular, this implies that the set N\E(t) is inﬁnite when 4|t. We conjecture

that all other sets, namely, N \ E(t) with t ∈ N which is not a multiple of 4 are

ﬁnite. More precisely, we conjecture that

Conjecture 3.5. There exists an integer C(t) ∈ N ∪ {0} such that the set

E(t) contains all integers greater than or equal to C(t) + 1 if 4 does not divide t

and all integers greater than or equal to C(t) + 1 except for sk2, where 4s|t and

k ∈ N, if 4|t.

By (22), we have C(1) = C(2) = 0. It is known that the total number of

representations of t/n by the sum 1/x + 1/y + 1/z does not exceed c(ε)(n/t)
2/3n
ε,

where ε > 0 (see [4]). We know that if n ∈ E(t) then t/n is expressible by the sum

of three unit fractions, so this bound also holds for the number of representations

of n in the form tM − d. On the other hand, by the result of Vaughan [32], almost

all positive integers are expressible by the sum of three unit fractions. It is easy

to see that for each ﬁxed integer t ⩾ 3 almost all positive integers belong to the

set E(t).

In fact, one can easily show a much stronger statement:

Proposition 3.6. For any integer t ⩾ 3 almost all positive integers can be

written in the form pa − 1 with some prime number p ≡ −1 (mod t) and some

a ∈ N.
 59

If n ∈ N can be written in this way then

n = pa − 1 = (p + 1)a − a − 1 = tM − d ∈ E(t)

with b = 1, d = a + 1 and M = (p + 1)a/t. By the above, it suﬃces to show

that the density of positive integers n that have no prime divisors of the form

p ≡ −1 (mod t) is zero. This can be easily done by a standard sieve argument

(see Section 3.1).

In the proof of Theorem 3.1 we describe an algorithm how to check if any

particular number belongs to the set E(t) or not and present the corresponding

Maple program. We applied this algorithm to make also other calculations with

C++ (with a better performance than that of Maple) below.

Coming back to Conjecture 3.5, by calculation with C++, in the range [1, 2·10
9]

we found only three exceptional integers 6, 36, 3600 which do not belong to the

set E(3). So we conjecture that

E(3) = N \ {6, 36, 3600} and C(3) = 3600.

For t = 4 we have
 288, 336, 4545, N
2 ∈ N \ E(4),

and we conjecture that C(4) = 4545.

There are much more integers which do not lie in E(5). In the range [1, 2 · 10
9]

there are 48 such integers:

1, 2, 5, 6, 10, 12, 20, 21, 30, 32, 45, 46, 50, 60, 92, 102, 105, 126, 141, 182, 192,

210, 282, 320, 330, 366, 406, 600, 650, 726, 732, 842, 846, 920, 992, 1020, 1446,

1452, 1905, 1920, 2100, 2250, 2262, 3962, 7320, 9050, 11520, 40500.

We conjecture that this list is full, i.e., C(5) = 40500. The list of integers in

[1, 2 · 10
9] which do not lie in E(6) contains 108 numbers, the largest one being

684450. We are more cautious to claim that C(6) = 684450, since this number is

quite large compared to the computation bound 2 · 10
9. Here is a result of our

calculations with C++ for 3 ⩽ t ⩽ 9.
 60

t computation bound number of exceptions largest exception

3 2 · 10
9 3 3600

4 2 · 10
9 3 4545

5 2 · 10
9 48 40500

6 2 · 10
9 108 684450

7 10
9 270 9673776

8 10
9 335 3701376

9 10
9 932 18481050

In the above table, for t = 4 all squares k2 are excluded, whereas for t = 8 all

squares k2 and all numbers of the form 2k2 are excluded (see Corollary 3.4 and

Conjecture 3.5).

3.1. Proofs.

Proof of Lemma 3.2: Lemma 3.2 was apparently ﬁrst proved by Yamamoto

[39]. See also Lemma 2 in [28] and Proposition 1.6 in [12]. Here is a short proof.

Since a = vd − b, equality (23) yields

k2 = 4u(vd − b)b − d = (4buv − 1)d − 4b2u.

So if (23) has a solution in positive integers then the Jacobi symbol ( −4b2u
4buv−1) =
( k2
4buv−1) must be equal to 1. Indeed, since −4b2u and 4buv − 1 are relatively

prime, we have ( −4b2u
4buv−1) ̸= 0 and so ( k2
4buv−1) = 1. We will show, however, that

it is equal to −1. Indeed, writing u = 2ru0, where r ⩾ 0 is an integer and u0 ⩾ 1

is an odd integer and using ( −1
4buv−1) = −1 and also ( 2
4buv−1) = 1 in case u is even,

i.e., r ⩾ 1, we ﬁnd that
( −4b2u
4buv − 1
) = ( −2
r+2b2u0
4buv − 1
 ) = − ( 2
ru0
4buv − 1
) = − ( u0
4buv − 1
 ) .

Further, by the quadratic reciprocity law, in view of u0|u we conclude that

− ( u0
4buv − 1
 ) = −(−1)
(u0−1)/2 ( 4buv − 1
u0
 ) = −(−1)(u0−1)/2 ( −1
u0
 ) = −1.

□

Proof of Theorem 3.1: Lemma 3.2 implies that k2 /∈ E(4). To complete the

proof of Theorem 3.1 we need to show that 288, 336, 4545 /∈ E(4).

61

The case n = 288 can be easily checked ‘by hand’. Observe that 288 = 4M − d

implies that d = 4s and M = (288 + 4s)/4 = 72 + s. Furthermore, from

72 + s = M ⩾ ab ⩾ a + b − 1 ⩾ d − 1 = 4s − 1

we ﬁnd that 1 ⩽ s ⩽ 24. So for each s = 1, 2, . . . , 24 it remains to check that

there are no positive integers a, b for which 4s|(a + b) and ab|(72 + s).

Note ﬁrst that for s ⩾ 11 we must have a + b = 4s and ab = 72 + s. Indeed, if

a + b > 4s then a + b ⩾ 8s and so

72 + s = M ⩾ ab ⩾ a + b − 1 ⩾ 8s − 1,

which is impossible, because s ⩾ 11. If ab < 72 + s then 2ab ⩽ 72 + s, so that

72+s ⩾ 2ab ⩾ 2(a+b−1) ⩾ 2(d−1) = 2(4s−1) = 8s−2, which is a contradiction

again. However, from a + b = 4s and ab = 72 + s it follows that

(4s)2 − 4(72 + s) = 4(4s2 − s − 72)

is a perfect square. So 4s2 − s − 72 must be a perfect square. It remains to

check the values of s between 11 and 24 which modulo 4 are 0 or 3, namely,

s = 11, 12, 15, 16, 19, 20, 23, 24. For none of these values 4s2 − s − 72 is a perfect

square.

The values of s between 1 and 10 can also be excluded, because there are no

a, b, with ab|(72 + s), for which 4s divides a + b; see the table below.

s 1 2 3 4 5 6 7 8 9 10

4s 4 8 12 16 20 24 28 32 36 40

72 + s 73 2 · 37 3 · 5
2 2
2 · 19 7 · 11 2 · 3 · 13 79 2
4 · 5 3
4 2 · 41

To complete the proof of the theorem observe that if n = tM − d then

n ⩾ tab − a − b ⩾ ta
2 − 2a

in case a ⩽ b. Hence (at − 1)
2 ⩽ nt + 1 and b ⩽ (a + n)/(ta − 1). Therefore, all

values from 1 to 10000 which do not belong to E(4) can be found with Maple as

follows.

For every particular value of n from 1 to 10000 we check all the pairs (a, b)

which satisfy the above inequalities for the existence of an appropriate value of d,

i.e., for the divisibility of a + b by some positive integer of the form d = tuab − n.

However, d ⩽ a + b ⩽ tab which means that there is only one possible such integer

62

d. Take a unique integer in the interval [1, tab] which equals −n modulo tab. It can

be expressed as tab − n (mod tab), as in the Maple code describing our algorithm

below.

t := 4: k := 0:

for n from 1 to 10000 do s := true;

for a from 1 by 1 while (s and (at − 1)2 ⩽ tn + 1) do B := (a + n)/(ta − 1);

for b from a by 1 while (s and b ⩽ B) do

if a + b (mod (tab − n (mod tab))) = 0 then s := f alse

end; end; end;

if s then k := k + 1;

print(n);

end; end:

print(k):

As a result (in less than three seconds) we got that only 100 perfect squares

and three exceptional numbers 288, 336, 4545 less than 10000 do not lie in E(4).

This completes the proof of Theorem 3.1. □

Proof of Proposition 3.6: Let p1 < p2 < p3 < . . . denote consecutive primes

in the arithmetic progression kt − 1, k = 1, 2, 3, . . . . By Dirichlet’s theorem,

the sum ∑∞
j=1 1/pj diverges. Thus for each ε > 0 we can pick s ∈ N for which
∏s
j=1(1 − 1/pj) < ε/2. Further, for each N ⩾ P := p1p2 . . . ps select a unique

k ∈ N for which kP ⩽ N < (k + 1)P . The number of positive integers n ⩽ N

without prime divisors in the set {p1, . . . , ps} does not exceed the number of such

positive integers in the interval [1, (k +1)P ]. The latter, by the inclusion-exclusion

principle, is equal to

(k + 1)P
 s∏

j=1
 (
1 − 1
pj
 ) ⩽ (k + 1)P ε
2 ⩽ (1 + 1/k)N ε
2 ⩽ 2N ε
2 = N ε.

This implies the claim. □
 63

Conclusions

Throughout this thesis, we have established the following results corresponding

to the raised questions (see the subsection ”Aims and problems”):

• The sequence
 [ξan], n = 1, 2, . . . ,

contains inﬁnitely many composite numbers for any ξ > 0 and any a ∈

{2, 3, 4, 5, 6, 3/2, 4/3, 5/4}.

• There exist ﬁnite sets of prime numbers of which at least one divides

inﬁnitely many numbers in the sequence

[ξan], n = 1, 2, . . . ,

for a ∈ {2, 3, 4, 6, 3/2, 4/3, 5/4}, and these sets do not depend on the num-

ber ξ > 0. For example, for a = 5/4, such a set is P(5/4) = {2, 3, 7, 11, 13}.

For a = 5, there are such sets corresponding to any particular ξ > 0. How-

ever, one such ﬁnite set for all ξ > 0 does not exist in this case.

• The sequence
 [ξan + ν], n = 1, 2, . . . ,

contains inﬁnitely many composite numbers for any ξ > 0 and any a ∈

{7, 5/3, 7/5} if ν = 1/2. The same holds for ν = −1, any ξ > 0 and

a = 6/5. The sequence [ξ(5/2)n − 1 + 30k], n = 1, 2, . . . , contains inﬁnitely

many composite numbers for any ξ > 0 and any integer k . The sets of

prime divisors are explicitly indicated, except for the case a = 7.

• For every binary linear recurrence equation

xn+1 = axn + bxn−1,

where a, b ∈ Z, (a, b) ̸= (±2, −1), there exists a corresponding binary

linear recurrence sequence of integers whose two initial terms are positive

and relatively prime and which consists of only composite numbers (the

64

absolute values of the terms are taken). For (a, b) = (±2, −1) such a

sequence does not exist.

• Almost all positive integers belong to each of the sets E(t) (and E(1) =

E(2) = N). The set E(t), where 4|t, does not contain the numbers of the

form sk2, where s ∈ N satisﬁes 4s|t and k ∈ N.

65

References

[1] G. Alkauskas and A. Dubickas, Prime and composite numbers as integer parts of

powers, Acta Math. Hungar., 105 (2004), 249–256.

[2] R.C. Baker and G. Harman, Primes of the form [c
p], Math. Zeitschrift, 221 (1996),

73–81.

[3] M. Bello-Hern´andez, M. Benito and E. Fern´andez, On Egyptian fractions,

preprint at arXiv:1010.2035v1, 2010.

[4] T.D. Browning and C. Elsholtz, The number of representations of rationals as a sum

of unit fractions, Illinois J. Math. (to appear).

[5] Y. Bugeaud, Linear mod one transformations and the distribution of fractional parts

{ξ(p/q)
n}, Acta Arith. 114 (2004), 301–311.

[6] D.A. Buell and R.H. Hudson, On runs of consecutive quadratic residues and quadratic

nonresidues, BIT 24 (1984), 243–247.

[7] D. Cass, Integer parts of powers of quadratic units, Proc. Amer. Math. Soc., 101 (1987),

610–612.

[8] A. Dubickas, Integer parts of powers of Pisot and Salem numbers, Archiv der Math., 79

(2002), 252–257.

[9] A. Dubickas, Prime and composite integers close to powers of a number, Monatsh. Math.,

156 (3) (2009), 271–284.

[10] A. Dubickas, Sequences with inﬁnitely many composite numbers, Analytic and Proba-

bilistic Methods in Number Theory, Palanga, 2001 (eds. A. Dubickas, A. Laurinˇcikas and

E. Manstaviˇcius), TEV, Vilnius (2002), 57–60.

[11] A. Dubickas, There are inﬁnitely many limit points of the fractional parts of powers,

Proc. Indian Acad. of Sciences (Math. Sc.), 115 (4) (2005), 391–397.

[12] C. Elsholtz and T. Tao, Counting the number of solutions to the Erd˝os-Straus equation

on unit fractions, preprint at arXiv:1107.1010v3, 2011.

[13] L. Flatto, J.C. Lagarias, A.D. Pollington, On the range of fractional parts

{ξ(p/q)
n}, Acta Arith., 70 (1995), 125–147.

[14] W. Forman and H.N. Shapiro, An arithmetic property of certain rational powers,

Comm. Pure Appl. Math., 20 (1967), 561–573.

[15] R.L. Graham, A Fibonacci-like sequence of composite numbers, Math. Mag., 37 (1964),

322–324.

[16] S.W. Graham and C.J. Ringrose, Lower bounds for least quadratic non-residues, in:

Analytic number theory, Proc. Conf. in Honor of Paul T. Bateman, Urbana, IL, USA,

1989, Prog Math. 85, 1990, pp.269–309.

[17] R.K. Guy, Unsolved problems in number theory, 3rd. ed, Springer, New-York, 2004.

[18] M. Hall, Divisibility sequences of third order, American J. Math., 58 (1936), 577–584.

66

[19] A.S. Izotov, Second-order linear recurrences of composite numbers, Fibonacci Quart. 40

(3) (2002), 266–268.

[20] D.E. Knuth, A Fibonacci-like sequence of composite numbers, Math. Mag., 63 (1990),

21–25.

[21] J.F. Koksma, Ein mengen-theoretischer Satz ¨uber Gleichverteilung modulo eins, Compo-

sitio Math., 2 (1935), 250–258.

[22] K. Mahler, An unsolved problem on the powers of 3/2, J. Austral. Math. Soc., 8 (1968),

313–321.

[23] H.W. Mills, A prime representing function, Bull. Amer. Math. Soc., 53 (1947), 604.

[24] H.L. Montgomery, Topics in multiplicative number theory, Lecture Notes in Mathe-

matics 227, Springer, New York, 1971.

[25] L.J. Mordell, Diophantine equations, Academic Press, London, New-York, 1969.

[26] J.W. Nicol, A Fibonacci-like sequence of composite numbers, Electronic J. Combin., 6

(1999), #R44, 6 p.

[27] C. Pisot, R´epartition (mod 1) des puissances successives des nombres r`eels, Comment.

Math. Helv., 19 (1946) 153–160.

[28] A. Schinzel, On sums of three unit fractions with polynomial denominators, Funct. Ap-

prox. Comment. Math. 28 (2000), 187–194.

[29] W. Sierpi´nski, Sur les d´ecompositions de nombres rationale en fractions primaires, Math-

esis 65 (1956), 16–32.

[30] L. Somer, Second-order linear recurrences of composite numbers, Fibonacci Quart. 44

(4) (2006), 358–361.

[31] J. ˇSiurys, A tribonacci-like sequence of composite numbers, Fibonacci Quart. 49 (4)

(2011), 298–302.

[32] R.C. Vaughan, On a problem of Erd˝os, Straus and Schinzel, Mathematika 65 (1970),

193–198.

[33] R.C. Vaughan, T.D. Wooley, Waring’s problem: a survey, Number theory for the

millennium, III (Urbana, IL, 2000), A. K. Peters, Natick, MA (2002), 301–340.

[34] T. Vijayaraghavan, On the fractional parts of the powers of a number, J. London Math.

Soc., 15 (1940), 159–160.

[35] M. Vsemirnov, A new Fibonacci-like sequence of composite numbers, Journal of Integer

Sequences, 7 (2004), Article 04.3.7, 3 p.

[36] H.S. Wilf, Letters to the editor, Math. Mag., 63 (1990), 284.

[37] E.M. Wright, A prime representing function, Amer. Math. Monthly, 58 (1951), 616–

618.

[38] K. Yamamoto, On a conjecture of Erd˝os, Mem. Fac. Sci. Kyuchu Univ. Ser. A 18 (1964),

166–167.

[39] K. Yamamoto, On the Diophantine equation 4
n = 1
x + 1
y + 1
z , Mem. Fac. Sci. Kyuchu

Univ. Ser. A 19 (1965), 37–47.
 67
