<!-- source: https://arxiv.org/pdf/2009.01114 | converted from PDF -->

arXiv:2009.01114v4  [math.NT]  20 Oct 2020
On the Erd˝os-Sloane and Shifted Sloane
Persistence Problems

Gabriel Bonuccelli
Lucas Colucci
Edson de Faria

Instituto de Matem´atica e Estat´ıstica
Universidade de S˜ao Paulo
S˜ao Paulo
Brazil
{gabrielbhl,lcolucci,edson}@ime.usp.br

Abstract

In this paper, we investigate two variations on the so-called persistence problem
of Sloane: the shifted version, which was introduced by Wagstaﬀ; and the nonzero
version, proposed by Erd˝os. We explore connections between these problems and a
recent conjecture of de Faria and Tresser regarding equidistribution of the digits of
some integer sequences and a natural generalization of it.

1 Introduction

In 1973, Sloane [9] proposed the following question: given a positive integer n, multiply all
its digits together to get a new number, and keep repeating this operation until a single-digit
number is obtained. The number of operations needed is called the persistence of n. Is it
true that there is an absolute constant C(b) (depending solely on the base b in which the
numbers are written) such that the persistence of every positive integer is bounded by C(b)?
Despite many computational searches, heuristic arguments and related conjectures in favor
of a positive answer, no proof or disproof of this conjecture has been found so far.
Many variants of Sloane’s problem have been considered as well. The famous book of
Guy [5] mentions that Erd˝os introduced the version of the Sloane problem wherein only the

This work has been supported by “Projeto Tem´atico Dinˆamica em Baixas Dimens˜oes” FAPESP Grant
2016/25053-8
 1

nonzero digits of a number are multiplied in each iteration, which we call the Erd˝os-Sloane
problem. Another variant was raised by Diamond and Reidpath [3], where instead of the
usual base b, numbers are taken to the so-called factorial base. Less related variations include
the additive persistence (when the digits are summed up instead of multiplied) [7] or versions
where even more general functions of the digits are considered [1, 6].
In this paper, we will be concerned with the Erd˝os-Sloane version and with the shifted
Sloane problem, introduced by Wagstaﬀ [10], which consists in shifting all the digits of the
number by a ﬁxed positive integer before multiplying them.

2 Deﬁnitions and notation

For integers t ≥ 0 and b ≥ 2, the t-shifted Sloane map in base b is the map St,b that takes
a nonnegative integer n = ∑k
i=0 dib
i (as usual, 0 ≤ di ≤ k − 1 for all i and dk > 0) to the
integer St,b(n) = ∏k
i=0(di + t). This function was introduced (in the special case b = 10) by
Wagstaﬀ [10], motivated by a question of Erd˝os and Kiss. Note that t = 0 corresponds to
the map that we iterate in the original persistence problem. Furthermore, the Erd˝os-Sloane
map in base b, denoted by S∗
b , is the map that sends n = ∑k
i=0 dib
i to S∗
b (n) = ∏

0≤i≤k,di̸=0 di.
The set of nonnegative integers is denoted by N. We use the notation f k(n) to denote the
k-th iterate of a map f on the point n, i.e., f 0(n) = n and f k(n) = f (f k−1(n)) for every
k ≥ 1, and we let Per(f ) denote the set of periodic points of f . Finally, for 0 ≤ d ≤ b − 1
and an integer n, we let #d(n)b denote the number of digits d in the expansion of n in base
b (e.g., #2(10010)3 = 1, since 10010 = 102013), and #(n)b denote the number of digits of the
base-b expansion of n. The subscripts b will be omitted when clear from the context.
We are interested in the dynamics of St,b and S∗
b . Contrarily to the original problem
(t = 0) and to S∗
b , for t ≥ 1 it is not even clear that every n reaches a ﬁxed point or a cycle
of St,b. If it does, the smallest number of iterations to reach it will be called, as usual, the
persistence of n, and it will be denoted, respectively, by νt,b(n) and ν∗
b (n) (we set those values
to ∞ in case the corresponding sequence of iterates diverges). Even the basic question of
whether νt,b(n) is ﬁnite for every n is not so readily answered for many values of t and b,
and it is open for most of them. On the other hand, it is easy to see that Sb,b(n) > n holds
for every b and n, so νt,b(n) = ∞ for every n whenever t ≥ b. Thus, from now on, we will
assume that t ≤ b − 1 unless stated otherwise.

3 Questions

For every b ≥ 2 and 0 ≤ t ≤ b−1, one deﬁnes the t-shifted Sloane problem in base b as in the
previous section. We will refer to this problem as the (t, b) problem for short. Furthermore,
for every b ≥ 2, we may consider the Erd˝os-Sloane problem in base b, and, similarly, we will
refer to this problem as the (∗, b) problem.
 2

For each of the (t, b) and (∗, b) problems, there are diﬀerent questions one may ask about
the corresponding iterating map f = St,b (or f = S∗
b ).

1. The most basic question is the following: let Af denote the set of nonnegative integers
n such that the sequence of iterates (f k(n))k≥0 stabilizes (i.e., reaches either a cycle
or a ﬁxed point of f ). What can be said about Af ? It is trivial that Af = N in the
original problem (t = 0) and in the Erd˝os-Sloane problem. We will prove (Theorem
7) that Af = N for t = 1 and b ≥ 2 as well (extending a result of Wagstaﬀ [10]).
Furthermore, we will prove that some natural conjectures on the equidistribution of
digits of some sequences imply that Af = N for some pairs (t, b) and that N − Af
contains all suﬃciently large integers for other pairs (t, b), but our results do not cover
all the range of (t, b) (Theorems 15, 17, 19, 20 and 23).

2. In case Af = N, i.e., every n ∈ N stabilizes under iteration by f , is there a universal
constant that bounds the persistence of all numbers, that is, is there C such that
νt,b(n) ≤ C (or ν∗
b (n) ≤ C) for every n ∈ N? Note that the positive answer to the
question for t = 0 is the original Sloane conjecture. Perhaps surprisingly, we prove
that the equidistribution conjectures imply a negative answer for t = 1 and for the
Erd˝os-Sloane problem, which shows a pronounced diﬀerence in the behaviors of the
(0, b) problem and the (1, b) and (∗, b) problems (Theorems 5, 6, 10 and 13).

3. Still assuming Af = N, we know that every integer n reaches either a ﬁxed point or
a cycle of f . What are the cycles and the ﬁxed points of f ? Besides the trivial cases
(0, b) and (∗, b), we are able to describe them precisely in the case t = 1 for any b ≥ 3
(Theorem 7).

4. Finally, the most detailed question we deal with is the following: for a cycle (or ﬁxed
point) C of f , which integers n tend to an element of C under iteration by f ? That is,
what are the backward orbits of each cycle C? We can answer this question precisely
only in the case t = 1 and b = 3 (Theorem 8).

4 Equidistribution of digits in products of primes

If an integer n contains a digit zero in its base-b expansion, then S0,b(n) = 0; otherwise, it is a
product of positive digits in base b, i.e., the integers from 1 to b − 1. This simple fact implies
that almost all integers have persistence equal to one, in the sense that the number of integers
up to N having this property is asymptotically equal to N when N → ∞. Furthermore,
it implies that, when considering the dynamics of S0,b (or S∗
b ), it is frequently enough to
deal with products of integers less than b, i.e., products of power of primes smaller than b.
Similarly, for St,b, it is enough to consider products of integers between t and t + b − 1. Based
on strong computational evidence and heuristic models, de Faria and Tresser [2] proposed
a conjecture that states, in particular, that some sequences of this kind of numbers have a
very regular asymptotic distribution of digits. Before stating their conjecture, we introduce

3

one more deﬁnition: given ε > 0, a number n, and a base b, we say that the digits of n are
ε-equidistributed (in base b) if, for every digit d ∈ {0, . . . , b − 1}, we have | #d(n)b
#(n)b − 1
b | < ε.

Conjecture 1 (de Faria, Tresser [2]). Given an integer q > 1, a ﬁnite set of primes F that
does not contain all the primes dividing q, and a positive integer a, let (Ni)i≥0 be a sequence
of integers such that N0 = a and, for every k ≥ 0, Nk+1 = Nk · pk, where pk ∈ F . Then the
digits {0, . . . , q − 1} are asymptotically equidistributed when n → ∞ in the base-q expansion
of the Ni. That is, given ε > 0, there is n0 such that Nn is ε-equidistributed in base q for
every n ≥ n0.

This form of the conjecture stems from an earlier one that arose in discussions between
C. Tresser and G. Hentchel [2, p. 381].

Remark 2. The full version of Conjecture 1 also states that the equidistribution holds for
blocks of consecutive digits of any length l > 0, i.e., given a block of l digits, its proportion
in the base-q expansion of the numbers in the sequences (Ni)i≥0 is asymptotically equal to
1
ql .

Remark 3. Although Conjecture 1 seems very natural, even its simplest instances are not
known to be true. For instance, it is not known whether the sequence (2n)n≥0 is asymptoti-
cally equidistributed in base 3. Indeed, even the old conjecture of Erd˝os [4] that states that
all but ﬁnitely many terms of this sequence contain a digit two in its ternary expansion is
still open.

Although Conjecture 1 is enough to prove results in base 3 (and, in some cases, base 4),
for larger bases one needs a uniform, or “multidimensional” generalized version, which we
now state.

Conjecture 4 (Uniform generalization of Conjecture 1). Let q > 1 be an integer, F =
{p1, . . . , pk} be a ﬁnite set of primes that does not contain all the primes dividing q, and
a be a positive integer. Then, for every ε > 0, there exists N such that a ∏k
i=1 pαi
i is
ε-equidistributed in base q whenever αi ≥ N for some i ∈ {1, . . . , k}.

5 Main results

5.1 Erd˝os-Sloane problem

First, we consider the Erd˝os-Sloane version. It is trivial that the only periodic points of the
Erd˝os-Sloane map in base b are the ﬁxed points 1, 2, . . . , b − 1. As for the persistence of
a number, we prove that Conjectures 1 and 4 imply that the analog of Sloane’s conjecture
does not hold in this context.

Theorem 5. Conjecture 1 implies that for both S∗
3 and S∗
4, there are integers with arbitrarily
large persistence. Moreover, Conjecture 4 implies the same result for S∗
b , for every b ≥ 5.

4

Proof. We divide the proof into three cases: b = 3, b = 4 and b ≥ 5.

(i) Base 3

Let f denote S∗
3 for ease of notation. Taking q = 3, F = {2} and a = 1 in Conjecture
1, we get the following statement: for every ε > 0, there is N such that the proportion
of digits d (d = 0, 1, 2) in 2n is in (1/3 − ε, 1/3 + ε) whenever n ≥ N.

Take ε = 1/6. There is N such that the proportion of digits d (d = 0, 1, 2) in 2n is in
(1/6, 1/2) whenever n ≥ N. Take m such that m(1/6)t−1(log3 2)t−1 ≥ max{N, 3} and
consider the integer n = 2m. We claim that ν∗
3 (n) ≥ t.

As m = m(1/6)0(log3 2)0 ≥ max{N, 3}, we know that 2m has at least 1/6 of its
digits equal to 2. Thus, f (m) = 2m1, where m1 ≥ (1/6) log3 2m = m(1/6) log3 2.
As m(1/6) log3 2 ≥ max{N, 3}, we know that the persistence of m is at least two
and that 2m1 has at least 1/6 of its digits equal to 2. Thus, f (f (2m)) = f (2m1) =
2m2, where m2 ≥ 2m(1/6)2(log3 2)2. Inductively, we get that f t−1(2m) = 2mt−1, where
mt−1 ≥ 2m(1/6)t−1(log3 2)t−1 ≥ 3: indeed, if f i(2m) = 2mi with mi ≥ m(1/6)i(log3 2)i,
we have that f i(2m) is ε-equidistributed, since m(1/6)i(log3 2)i ≥ N, and then at
least 1/6 of its digits are equal to 2. This implies that f i+1(2m) = 2mi+1, where
mi+1 ≥ (1/6) log3 f i(2m) ≥ m(1/6)i+1(log3 2)i+1, and completes the induction. Hence,
f t−1(2m) ≥ 2m(1/6)t−1(log3 2)t−1 ≥ 3, which means that n = 2m has persistence at least t.

(ii) Base 4

In this case, we apply Conjecture 1 twice, with q = 4, F = 3, a = 1; and q = 4, F = 3,
a = 2, respectively, to get that for every ε > 0 there is N such that 3m and 2 · 3m are
ε-equidistributed whenever m ≥ N. Noting that, for every a and b, we have f (2a · 3b)
is either equal to f (3b) or f (2 · 3b) and applying the same argument as in item (i) with
ε = 1/8, one can show that ν∗
4 (3m) ≥ t if m(1/8)t−1(log3 4)t−1 ≥ max{N, 4}.

(iii) Larger bases

For b ≥ 5, let F be the set of primes smaller than b and Fr = F − {r}. We apply
Conjecture 4 for each prime divisor r of b and each proper divisor d of b, with Fr being
the set of primes considered, q = b and a = d. Note that, by Bertrand’s postulate
(which states that, for every n > 1, there is a prime p such that n < p < 2n), there
is some prime q such that (b − 1)/2 < q < b, which means that q does not divide
b. Taking the maximum of the N given in each application of the conjecture with a
ﬁxed ε > 0, we get the following statement: for every ε > 0, there is N such that
d ∏

pi∈Fr pαi
i is ε-equidistributed whenever αi ≥ N for some i ∈ {1, . . . , k}, where d is a
proper divisor of b and r is a prime divisor of b. Moreover, note that, for every n, one
has f (bn) = f (n), since the expansion of bn and n in base b diﬀer only by one digit 0.

We claim that ν ∗b (n) ≥ t, where n = (∏

pi∈F,pi∤b pi)m and m satisﬁes the inequality
m(1/(2b))t−1(logb 2)t−1 ≥ max{N, b}, where N is the integer given by the applications
of Conjecture 4 as above with ε = 1/(2b). As m ≥ N, n is ε-equidistributed, whence,

5

using a rough bound (∏

pi∈F,pi∤b pi)m ≥ 2m, we have f (n) = ∏

pi≤b prime pβi
i , with βi ≥
(1/b−ε)#(n)b ≥ (1/(2b))(logb 2)m. The fact that f (ba) = f (a) for every a implies that
f (f (n)) = f (d ∏

pi∈Fr pαi
i ) for some proper divisor d of b and some prime r dividing
b. As αi ≥ βi for every pi that does not divide b (because no power of pi can be
factored out into powers or divisors of b), we have αi ≥ (1/(2b))(logb 2)m ≥ N for some
i ∈ {1, . . . , k}. Then, the number d ∏

1≤i≤k pαi
i is ε-equidistributed, and hence we have

f (f (n)) = ∏

pi≤b prime pβ′
i
i with β′
i ≥ (1/(2b))#(d ∏

1≤i≤k pαi
i )b ≥ (1/(2b))(logb 2)αi ≥
(1/(2b))2(logb 2)2 · m for every i, and the argument can be repeated. Inductively, the
exponents of the pi in f t−1(n) are at least (1/(2b))t−1(logb 2)t−1 · m. In particular,
f t−1(n) ≥ 2(1/(2b))t−1(logb 2)t−1·m ≥ 2b ≥ b
2. By the choice of m, this number is at least b,
so n has persistence at least t.

In other words, assuming Conjectures 1 and 4, Theorem 5 states that lim supn→∞ ν∗
b (n) =
∞ for every b ≥ 3. Our next result gives an estimate on this number which is sharp up to a
constant factor.

Theorem 6. For each base b ≥ 3, we have

lim sup
n→∞ ν∗
b (n)
log log n ≤ 1
log (α−1) , (1)

where α = logb (b − 1). Moreover, if Conjecture 4 holds, then we have

lim sup
n→∞ ν∗
b (n)
log log n ≥ 1
log (β−1) , (2)

where β = logb 2
2b .

Proof. For ease of notation, let us denote by f the Erd˝os-Sloane map S∗
b in base b. The
proof is naturally divided into two parts.

(i) Upper bound. Given n > b, let us denote by kj (j = 0, 1, . . .) the number of digits of
f j(n) in base b. Note that kj ≤ 1 + logb f j(n) for all j. Since each digit in the base-b
expansion of f j(n) is at most b − 1, we have f j+1(n) ≤ (b − 1)kj . Therefore, for all
j ≥ 0 we get kj+1 ≤ 1 + kj logb (b − 1) = 1 + αkj.

By induction, it follows that for all j ≥ 1 we have

kj ≤ αjk0 + (1 + α + α2 + · · · + αj−1) < αjk0 + 1
1 − α . (3)

6

Since α < 1, the ﬁrst term in the right-hand side of (3) goes to zero as j → ∞. Thus,
let j0 be the smallest natural number such that αj0k0 < 1. An easy calculation shows
that
 j0 = ⌈ logb k0
logb (α−1)
⌉ ,

and since k0 ≤ 1 + logb n ≤ 2 logb n when n ≥ b, it follows that

j0 ≤ logb logb n
logb (α−1) + (
1 + logb 2
logb (α−1)
 ) .

But now note that kj0 ≤ D, where D = 1 + ⌈(1 + α)−1⌉. Hence, deﬁning

M = max {
ν∗
b (m) : m has at most D digits in base b
} < ∞,

we see that ν∗
b (f j0(n)) ≤ M. Since we clearly have ν∗
b (n) = j0 + ν∗
b (f j0(n)), it follows
that
 ν∗
b (n) ≤ logb logb n
logb (α−1) + (1 + M + logb 2
logb (α−1)
 )

= log logb n
log (α−1) + (
1 + M + logb 2
logb (α−1)
) .

Dividing both sides of this inequality by log log n and taking the lim sup as n → ∞,
we get (1) as desired.

(ii) Lower bound. Here we shall use one of the ideas used in the proof of Theorem 5. For

each natural number t, let us consider nt = (∏

pi prime,pi<b,pi∤b pi)mt, where mt is the
smallest positive integer such that

mt
 ( 1
2b
)t−1 (logb 2)t−1 ≥ C = max{b, N},

and where N is given by Conjecture 4 taking ε = 1
2b. As we saw in the proof of

Theorem 5, we have ν∗
b (nt) ≥ t. Now, by the very deﬁnition of mt, we know that

(mt − 1) ( 1
2b
)t−1 (logb 2)t−1 < C.

Taking logarithms (to base b) on both sides of this inequality and solving for t, we get

t > logb (mt − 1)
logb (β−1) + 1 − logb C
logb (β−1) ,

7

where β = logb 2
2b . Note that logb (mt − 1) > logb mt−logb 2 (because mt > 2). Moreover,
again from the deﬁnition of mt, we have

logb mt = logb logb nt − logb logb
 

 ∏

1≤i≤k pi


 .

Putting all these facts together, we deduce that

ν∗
b (nt) > logb logb nt
logb (β−1) + K

= log logb nt
log (β−1) + K, (4)

where K is a constant, namely

K = 1 − 1
logb (β−1) logb
 


2C logb
 

 ∏

1≤i≤k pi







 .

Thus, the inequalities in (4) divided by log log nt, letting t → ∞, imply that

lim sup
t→∞ ν∗
b (nt)
log log nt ≥ 1
log (β−1) ,

and this obviously implies (2).

5.2 1-shifted problem

In this section, we generalize a result of Wagstaﬀ [10] for base 10, showing that for any base
b, every positive integer n reaches reach a ﬁxed point or a cycle under iteration by S1,b.

Theorem 7. Let b ≥ 2. Then, for every positive integer n, the iterates of S1,b starting at n
reach one of the following cycles:

(102), if b = 2;
(2, . . . , b − 1, 10b) or (1(b − 2)b), if b ≥ 3.

Proof. For ease of notation, let f denote S1,b in this proof. First of all, notice that the
theorem is trivial for b = 2, since in this case f (n) is a power of 2 for every n, and then
f 2(n) = 102, which is the only ﬁxed point of f . From this point on, we assume that b ≥ 3.

8

Assume ﬁrst that n is of the form db
k −1, where 2 ≤ d ≤ b (i.e., all the digits of n, possibly
with the exception of the leading digit, are equal to b − 1; the leading digit of n is d − 1; and
n has exactly k digits). In this case, f (n) = db
k−1 = n + 1, and 2 ≤ f (f (n)) ≤ b = 10b, so
this number belongs to the cycle (2, 3, . . . , 10b).
If n is not of the form above, let n = (dkdk−1 . . . d0)b be the representation of n in base
b, and let j be the biggest index i such that i < k and di < b − 1. We can bound f (n) from
above by (dk +1)(dj +1)b
k−1, which can be written as dkb
k +djb
k−1 +b
k−1(1+dk(dj −(b−1))).
On the other hand, we have that n = ∑k
i=0 dib
i ≥ dkb
k + djb
k+1. If the term b
k−1(1 +
dk(dj − (b − 1))) is negative, we have f (n) < n. As dj ≤ b − 2, this term is nonnegative only
if dj = b − 2 and dk = 1. In this case, the bound for f (n) becomes equal to db
k + (b − 2)b
k−1.
Furthermore, if j < k − 1, then the lower bound on n can be strengthened to n ≥ b
k + (b −
1)b
k+1 + (b − 2)b
j and hence f (n) < n. So we must have j = k − 1 to have f (n) ≥ n. Also,
if any digit of n other than dk and dk−1 is not zero, we have n > db
k + (b − 2)b
k−1 ≥ f (n).
Therefore, f (n) < n unless n is of the form 1(b − 2)000 . . . 0b = b
k + (b − 2)b
k−1. In this
case, f (n) = 2(b − 1), which implies that f (n) < n unless k = 1, which corresponds to the
ﬁxed point n = 1(b − 2)b. This proves that f either reaches the ﬁxed point 1(b − 2)b or keeps
decreasing until it enters the cycle (2, 3, . . . , 102).

In the case b = 3, we are able to tell which integers reach the ﬁxed point and which
integers reach the cycle. Namely, we have the following result.

Theorem 8. For every n ≥ 1, the sequence (Sk
1,3(n))k≥1 reaches the cycle (2, 103) if and only
if either n or 2#1(n)3 lacks the digit 1 in its ternary expansion; otherwise, it reaches (113).

Proof. Once more, let f denote S1,3. The result is clear for n ∈ {1, 2, 103, 113}. Let n ≥ 123.
Notice that f (n) = 2#1(n)3#2(n), so f (n) ends in #2(n) zeros in base 3, and hence f (f (n)) =
f (2#1(n)).
If #1(n) = 0, then f (f (n)) = f (1) = 2. Also, if #1(2#1(n)) = 0, then f 3(n) =
f (f (2#1(n))) = f (2#1(2#1(n))) = f (1) = 2.
On the other hand, assume that both #1(n) and #1(2#1(n)) are positive. We will prove
by induction on n (over those values such that #1(n) > 0 and 2#1(n) > 0) that, in this case,
(f k(n))k≥1 reaches the cycle (113).
The result if trivial if n ≤ 113. If n > 113, then f (f (n)) = f (2#1(n))). As 2#1(n) < n, we
can use the induction hypothesis to prove that n reaches (113) if we have #1(2#1(n)) > 0 and
#1(2#1(2#1(n))) > 0. The ﬁrst inequality is just part of the condition on n; the second comes
from the fact that #1(2#1(n)) is even (an even number must have an even number of digits
1 in its ternary expansion), and hence 2#1(2#1(n)) is a power of four, and so it ends with a
digit 1.

Remark 9. By Conjecture 1, the number of n such that #1(2n)3 = 0 is ﬁnite. A result
of Narkiewicz [8] says that the number of n up to N with this property is bounded by

9

1.62N log3 2, so in particular their density in the set of positive integers is zero (this fact also
follows from a more general result of de Faria and Tresser [2, Corollary 3.7]).

As for the persistence, similarly as in Theorem 5, we prove that Conjectures 1 and 4
imply that there are integers of arbitrarily large persistence for S1,b.

Theorem 10. Conjecture 1 implies that there are integers of arbitrarily large persistence
for the 1-shifted problem in base 3 and 4, and Conjecture 4 implies the same result for bases
greater than 4.

Proof. We split the proof into three cases:

(i) Base 3

Put f = S1,3. Conjecture 1 implies the following: for every ε > 0, there exists N such
that 2m is ε-equidistributed whenever m ≥ N. To construct a number of persistence
greater than t, notice that, if a number a has exactly x digits 1 in its ternary expansion,
then f 2(a) = f (2x). Take ε = 1/6 and let N be the integer given by Conjecture 1 for
this value of ε. Let m be such that m(1/6)t−1(log3 2)t−1 ≥ max{N, 3}.

We claim that the number n = 2m has persistence larger than t. Let us denote, for
i ≥ 1 by ai and bi, respectively, the numbers deﬁned inductively in the following way:
2m has a1 digits 1 and b1 digits 2 in its ternary expansion, and f (2ai) = 2ai+1 · 3bi+1 for
every i ≥ 1. As m ≥ N, 2m is ε-equidistributed, so we have a1 ≥ (1/6)(log3 2)m. This
implies that f 2(2m) = f (2a1 · 3b1) = f (2a1) = 2a2 · 3b2. As a1 ≥ (1/6) log3 2 · m ≥ N, the
number 2a1 is ε-equidistributed, and this in turn implies that a2 ≥ (1/6) log3(2) · a1 ≥
(1/6)2(log3 2)2m. Inductively, we have that f t−1(2m) = 2at−1 · 3bt−1 where at−1 ≥
(1/6)t−1(log3 2)t−1m ≥ 3, which implies that n = 2m has persistence at least t, since
Theorem 7 shows that the elements of the cycle and the ﬁxed point of f have at most
two digits.

(ii) Base 4

We consider the number n = 3m, where m(1/8)t−1(log4 3)t−1 ≥ max{M, 4}, where M
is the maximum of the N obtained applying Conjecture 1 with (q, F, a) = (4, {3}, 1)
and (q, F, a) = (4, {3}, 2), in both cases with ε = 1/8, and the proof of item (i) applies.

(iii) Larger bases

Finally, for b ≥ 5, let F be the set of primes smaller than b and Fr = F − {r}. We
apply Conjecture 4 for each prime divisor r of b and each proper divisor d of b, with Fr
being the set of primes considered, q = b and a = d. Note that, by Bertrand’s postulate
(which states that, for every n > 1, there is a prime p such that n < p < 2n), there is
some prime s such that (b − 1)/2 < s < b. In particular, s does not divide b (so that
Fr is nonempty for every prime r dividing b). Taking the maximum of the N given in
each application of the conjecture with a ﬁxed ε > 0, we get the following statement:
for every ε > 0, there is N such that d ∏

pi∈Fr pαi
i is ε-equidistributed whenever αi ≥ N

10

for some i ∈ {1, . . . , k}, where d is a proper divisor of b and r is a prime divisor of b.
Moreover, note that, for every n, one has f (bn) = f (n), since the expansion of bn and
n in base b diﬀer only by one digit 0.

We claim that ν1,b(n) ≥ t, where n = (∏

pi∈F,pi∤b pi)m and m satisﬁes the inequality
m(1/(2b))t−1(logb 2)t−1 ≥ max{N, b}, where N is the integer given by the applications
of Conjecture 4 as above with ε = 1/(2b). As m ≥ N, n is ε-equidistributed, whence,
using a rough bound (∏

pi∈F,pi∤b pi)m ≥ 2m, we have f (n) = ∏

pi≤b prime pβi
i , with βi ≥
(1/b−ε)#(n)b ≥ (1/(2b))(logb 2)m. The fact that f (ba) = f (a) for every a implies that
f (f (n)) = f (d ∏

pi∈Fr pαi
i ) for some proper divisor d of b and some prime r dividing
b. As αi = βi for every pi that does not divide b (because no power of pi can be
factored out into powers or divisors of b), we have αi ≥ (1/(2b))(logb 2)m ≥ N for some
i ∈ {1, . . . , k}. Then, the number d ∏

1≤i≤k pαi
i is ε-equidistributed, and hence we have

f (f (n)) = ∏

pi≤b prime pβ′
i
i with β′
i ≥ (1/(2b))#(d ∏

1≤i≤k pαi
i )b ≥ (1/(2b))(logb 2)αi ≥
(1/(2b))2(logb 2)2 · m for every i, and the argument can be repeated. Inductively, the
exponents of the pi in f t−1(n) are at least (1/(2b))t−1(logb 2)t−1 · m. In particular,
f t−1(n) ≥ 2(1/(2b))t−1(logb 2)t−1·m ≥ 2b ≥ b
2. Again, as the elements of the cycle and the
ﬁxed point of f have at most two digits, this implies that n has persistence at least t.

An alternative proof of Theorem 10 in the case b = 3 would be to ﬁnd an inﬁnite
sequence (an)n≥0 such that 2an has an−1 digits 1 in base 3 for every n ≥ 1. In this case,
the integer 2an would have persistence equal to n plus the persistence of 2a0. The existence
of such a sequence is a straightforward consequence of Conjecture 1, but we conjecture it
independently, as it may be much simpler to prove than the full statement of the original
conjecture. A computational search shows that the initial terms of such a sequence could be

2, 4, 8, 24, 96, 350, 1580, 7520, 35600, 168980,

since 2168980 has 35600 digits 1, 235600 has 7520 digits 1, and so on, and 22 is a ﬁxed point
of S1,3. In fact, there is some computational evidence in favor of the following stronger
conjecture, which assures that one can ﬁnd such a sequence starting from any suﬃciently
large even number:

Conjecture 11. There is N such that, for every n > N, there is m such that 22m has exactly
2n digits 1 in base 3.

Remark 12. Conjecture 11 is equivalent to the assertion that the subsequence of terms of
even order of A036461 contains all suﬃciently large even numbers.

Just as we did for the Erd˝os-Sloane persistence, we can estimate the maximal growth of
ν1,b(n) as a function of n from above (unconditionally) and from below (using Conjecture 4
as in Theorem 10). More precisely, we have the result stated below. In its proof, we shall use
the following evident fact. If F is any ﬁnite non-empty set and φ : F → F is a self-map, then

11

every x ∈ F is eventually mapped to a (ﬁxed or) periodic point under φ, and the number of
iterates that it takes for x to reach the periodic cycle is obviously bounded by the cardinality
of F .

Theorem 13. For each base b ≥ 3, we have

lim sup
n→∞ ν1,b(n)
log log n ≤ 2
log (α−1) , (5)

where α = logb (b − 1). Moreover, if Conjecture 4 holds, then we have

lim sup
n→∞ ν1,b(n)
log log n ≥ 1
log (β−1) , (6)

where β = logb 2
2b .

Proof. Let us write f = S1,b in this proof. We treat the upper and lower estimates separately.

(i) Upper bound. Given n > b, write n = (d1d2 · · · dk)b (where k ≤ 1 + logb n; note that
this notation diﬀers from the one in section 2) and let ℓ ≤ k be the number of digits di
that are equal to b − 1. Then f (n) = b
ℓ · P , where P = ∏

di≤b−2(1 + di). This in turn
implies that f 2(n) = f (P ). But the number of digits of P in base b is at most

1 + logb P = 1 + ∑

di≤b−2 logb (1 + di) ≤ 1 + (k − ℓ)α ≤ 1 + kα,

where α = logb (b − 1) < 1. Hence we have

f 2(n) = f (P ) ≤ b
1+kα ≤ b
1+(1+logb n)α = b
1+αn
α.

By induction, it follows that

f 2j ≤ (b
1+α)1+α+α2+···+αj−1 n
αj < b
(1+α)/(1−α)n
αj , ∀j ≥ 1.

Let j0 be the smallest natural number such that n
αj0 < 2, i.e.,

j0 = ⌈log log n − log log 2
log (α−1)
 ⌉ . (7)

Then we have f 2j0(n) ∈ A = {1, 2, . . . , M}, where M = ⌈
2b
(1+α)/(1−α)⌉
. We claim that

A is f 2-invariant, i.e., f 2(A) ⊆ A. Indeed, if a ∈ A then

f 2(a) ≤ b
1+αa
α ≤ b
1+αM α ≤ b
1+α (2b
(1+α)/(1−α))α = 2αb
(1+α)/(1−α) < M,

12

and so f 2(a) ∈ A as claimed. But now, by the simple remark preceding the statement of
this theorem, every a ∈ A is eventually periodic, and if m ∈ N is the smallest number
such that f 2m(a) ∈ Per(f 2) ⊆ Per(f ), then m ≤ |A| = M. Summarizing, we have
proved that, starting from n > b: (i) after 2j0 iterates under f , we reach some a0 ∈ A;
(ii) after j1 ≤ 2M further iterates, we reach a periodic cycle, i.e., f j1(a0) ∈ Per(f ).
Therefore we have ν1,b(n) ≤ 2j0 + 2M, and from (7) we deduce that

ν1,b(n) ≤ 2 (log log n − log log 2
log (α−1)
 ) + 2(M + 1).

This shows that
 lim sup
n→∞ ν1,b(n)
log log n ≤ 2
log (α−1) .

and this is precisely (5).

(ii) Lower bound. Here we proceed just as in the proof of the lower bound in Theorem 10.

Once again, for each natural number t we consider nt = (∏

pi prime,pi<b,pi∤b pi)mt, where
mt is the smallest positive integer such that

mt
 ( 1
2b
)t−1 (logb 2)t−1 ≥ C = max{b, N},

and where N is given by Conjecture 4 taking ε = 1
2b. Then, as we saw in the proof of
Theorem 10, the 1-shifted persistence of nt is at least t, and the same computations
performed in the proof of Theorem 6 yield

ν1,b(nt) ≥ t > logb logb nt
logb (β−1) + K = log logb nt
log (β−1) + K, (8)

for some constant K. Dividing the resulting inequality in (8) by log log nt and letting
t → ∞, we arrive at (6) as desired.

5.3 2-shifted problem

In this section, we show that Conjectures 1 and 4 imply that every integer reaches a cycle
or a ﬁxed point under iteration by S2,b. Before stating the result precisely, we start with a
lemma.

Lemma 14. Let b ≥ 5 be a positive integer. Then

1. (b + 1)!
 logb (b+1)
b < b;
 13

2. (b + 1)logb(b−1) < b;

3. (b + 1)2 logb(b−2)+logb(b+1) < b
3.

Proof. Taking logarithms and rearranging terms, the ﬁrst inequality is equivalent to

b(log b)2 − log(b + 1)! · log(b + 1) > 0. (9)

We will use the following well-known upper bound for n!, valid for all positive integers n:

n! ≤ e (n
e
 )n √n.

Applying this bound to the left-hand side of inequality (9), we get

b(log b)2 − log(b + 1)! · log(b + 1)

≥ b(log b)2 − (b + 1)(log(b + 1))2 + b log(b + 1) − (log(b + 1))2

2 .

By the mean value theorem, b(log b)2 − (b + 1)(log(b + 1))2 = −g′(c) for some c ∈ (b, b + 1),
where g(x) = x(log x)2. As g′(x) = (log x)2 + 2 log x is increasing, we get that b(log b)2 −
(b + 1)(log(b + 1))2 ≥ −(log(b + 1))2 − 2 log(b + 1). This implies that

b(log b)2 − log(b + 1)! · log(b + 1) ≥ b log(b + 1) − 3(log(b + 1))2

2 − 2 log(b + 1).

Let h(b) = b log(b + 1) − 3(log(b+1))2

2 − 2(log(b + 1)). It is readily checked that h(5) > 0.
Moreover, h
′(b) = (b−2)(log(b+1)+1)
b+1 > 0 for every b > 2. This implies that h(b) > 0 for all
b ≥ 5 and concludes the proof of the ﬁrst item.
The inequality of the second item is equivalent, taking logarithms and rearranging terms,
to log(b − 1)
log b < log b
log(b + 1) . (10)

Inequality (10) is a straightforward consequence of the fact that f (x) = log x
log(x+1) is increasing

for x > 1, which follows immediately from f ′(x) = (x+1) log(x+1)−x log x
x(x+1)(log(x+1))2 .
Finally, the third inequality is equivalent to

log(b + 1)(2 log(b − 2) + log(b + 1)) < 3(log b)2. (11)

This can be proved using that log is a concave function and applying Jensen’s inequality to
2 log(b − 2) + log(b + 1):
 2 log(b − 2) + log(b + 1) < 3 log(b − 1).

The left-hand side of (11) is, then, smaller than 3 log(b−1) log(b+ 1). Inequality (10) implies
that this is less than 3(log b)2 and concludes the proof.

14

Theorem 15. Conjecture 1 (resp., Conjecture 4) implies that for every n ≥ 1, the iterates
of S2,3(n) (resp., S2,b(n), for b ≥ 4) reach a cycle or a ﬁxed point.

Proof. We will prove the result for b = 3, b = 4 and b ≥ 5 separately. In any case, to
show that the sequence of iterates starting at any positive integer stabilizes, we will prove
the following stronger statement: there exist integers N0 and k and a constant 0 < cb < 1
(which depends only on b) such that, for every n ≥ N0, Sj
2,b(n) ≤ n
cb (or, equivalently,
Sj
2,b(n) ≤ C · n
c′
b for some constant C independent of n and 0 < c′
b < 1) for some 1 ≤ j ≤ k.
In the cases b = 3, b = 4 and b ≥ 5, we will prove this statement with k = 4, k = 3 and
k = 2, respectively.

(i) Base 3

First, put f = S2,3 to simplify the notation. We will use the following instance of
Conjecture 1, which corresponds to q = 3, F = {2} and a = 1: for every ε > 0, there
exists N such that 2t is ε-equidistributed in base 3 whenever t ≥ N.

Let a0, b0, c0 denote, respectively, #0(n), #1(n), #2(n); and, for k ≥ 1, let ak, bk, ck de-
note, respectively, #0(2bk−2+ak−1+2ck−1), #1(2bk−2+ak−1+2ck−1), #2(2bk−2+ak−1+2ck−1), where
we put b−1 = 0. With this notation, we have

f k(n) = 2bk−2+ak−1+2ck−1 · 3bk−1

for every k ≥ 1.

Let us write α = log3 2 ≈ 0.631. Moreover, ﬁx ε = 0.001 and write δ = 1/3 − ε. Let N
be such that 2t is ε-equidistributed in base 3 for every t ≥ N.

For any integer n, we have f (n) = 2a0+2c0 · 3b0 and f 2(n) = 2b0f (2a0+2c0).

Let n ≥ 33M be an integer, where M ≥ N/(δα)2. We know that a0 + b0 + c0 ≥ log3 n ≥
3M. This implies that either b0 ≥ 2M or a0 + c0 ≥ M.

Suppose ﬁrst that a0 + c0 < M. Then b0 ≥ 2M, and using the trivial bound f (m) ≤
4log3 m+1, which holds for every m since each of the at most log3 m + 1 digits of m is
mapped to a factor 2, 3 or 4 in f (m), we get, using that 3a0+b0+c0−1 ≤ n ≤ 3a0+b0+c0,
that
 f 2(n)
n ≤ 2b0f (2a0+2c0)
3a0+b0+c0−1

≤ 2b0 · 4log3(2a0+2c0 )+1

3a0+b0+c0−1

= c · 3(α−1)b0+(2α2−1)a0+(4α2−1)c0

≤ c · (
3b0)α−1+(4α2−1)/2

15

≤ c · ( n
3M
 )α−1+(4α2−1)/2 ,

for some positive constant c, since 1 − 2α2, 1 − α > 0 and 1 − 4α2 < 0. As α − 1 +
(4α2 − 1)/2 < 0, this concludes the proof in this case.

From now on, we may assume that a0 + c0 ≥ M. As M ≥ N/(δα)2 ≥ N, we know
that 2a0+2c0 is ε-equidistributed, i.e., a1, b1, c1 belong to ((1/3 − ε)α(a0 + 2c0), (1/3 +
ε)α(a0 + 2c0)). In particular, writing β for 1/3 + ε, we have that a1, b1, c1 are bounded
from above by βα(a0 + 2c0).

As f 2(n) = 2b0+a1+2c1 · 3b1, we have f 3(n) = 2b1f (2b0+a1+2c1). As a1 ≥ δα(a0 + 2c0) ≥
δαM ≥ N, the number 2b0+a1+2c1 is ε-equidistributed, i.e., the quantities a2, b2, c2
belong to the interval ((1/3 − ε)α(b0 + a1 + 2c1), (1/3 + ε)α(b0 + a1 + 2c1)), and hence
are bounded from above by

βα(b0 + a1 + 2c1) ≤ βα(b0 + 3βα(a0 + 2c0))
= 3β2α2(a0 + 2c0) + βαb0.

On the other hand, the numbers a2, b2, c2 are greater than δα(b0 + a1 + 2c1) > δ2α2(a0 +
2c0) ≥ N, so 2a2+2c2+b1 is ε-equidistributed. This implies that

a3, b3, c3 ≤ βα(b1 + a2 + 2c2)
≤ βα(βα(a0 + 2c0) + 9β2α2(a0 + 2c0) + 3βαb0)
= β2α2(1 + 9βα)(a0 + 2c0) + 3β2α2b0.

Together, these estimates imply that

α(b2 + a3 + 2c3) + b3 ≤ α(3β2α2(a0 + 2c0) + βαb0)+
(3α + 1)(β2α2(1 + 9βα)(a0 + 2c0) + 3β2α2b0)
= β2α2(3α + (3α + 1)(1 + 9βα))(a0 + 2c0) + βα2(1 + 3(3α + 1)β)b0.

Finally, this bound implies that

f 4(n)
n = 2b2+a3+2c3 · 3b3

3a0+b0+c0−1

≤ 3 · 3α(b2+a3+2c3)+b3

3a0+b0+c0

≤ 3 · 3β2α2(3α+(3α+1)(1+9βα))(a0 +2c0)+βα2(1+3(3α+1)β)b0

3a0+b0+c0

= 3 · 3(β2α2(3α+(3α+1)(1+9βα))−1)a0 +(βα2(1+3(3α+1)β)−1)b0 +(2β2α2(3α+(3α+1)(1+9βα))−1)c0 .

This gives the result, since β2α2(3α+(3α+1)(1+9βα)) < 1
2 and βα2(1+3(3α+1)β) < 1.

16

(ii) Base 4

We now consider base 4. As usual, put f = S2,4 to ease the notation. We will prove the
following: for every suﬃciently large integer n, one of the numbers f (n), f 2(n), f 3(n)
is at most cn
cb for some c > 0 and 0 < cb < 1. We will apply Conjecture 4 twice, with
q = 4, F = {3, 5}, a = 1 and q = 4, F = {3, 5}, a = 2 to get the following statement:
for every ε > 0, there is N such that 3x · 5y and 2 · 3x · 5y are ε-equidistributed whenever
x ≥ N or y ≥ N.

For any integer n, if we put a0 = #0(n), b0 = #1(n), c0 = #2(n) and d0 = #3(n), we
have f (n) = 4⌊a0/2⌋+c0 · 2a′
0 · 3b0 · 5d0 and f 2(n) = 2⌊a0/2⌋+c0 · f (2a0′ · 3b0 · 5d0), where x
′

denotes the remainder of the integer x modulo 2.

Let ε = 0.001 and let n ≥ 44M be an integer, where M ≥ N/(2(1/4 − ε) log4 3). We
know that a0 + b0 + c0 + d0 ≥ log4 n ≥ 4M. This implies that either b0 ≥ M, or d0 ≥ M,
or a0 + c0 ≥ 2M.

Suppose ﬁrst that b0 < M and d0 < M. Then a0 + c0 ≥ 2M, and using the trivial
bound f (m) ≤ 5log4 m+1, which holds for every m since each of the at most log4 m + 1
digits of m is mapped to a factor 2, 3, 4, or 5 in f (m), we get that

f 2(n)
n ≤ 2⌊a0/2⌋+c0 · f (2a′
0 · 3b0 · 5d0)
4a0+b0+c0+d0−1

≤ 4 · 2a0/2+c0 · 5log4(2·3b0 ·5d0 )+1

4a0+b0+c0+d0

= c · 4−3a0/4−c0/2+(log4 5 log4 3−1)b0+((log4 5)2−1)d0

≤ c(M) · (4a0+c0)−1/2

≤ c(M) · ( n
42M
 )−1/2 ,

where c(M) is some constant dependent on M only. This proves the claim in the ﬁrst
case.

From now on, we assume that b0 ≥ M or d0 ≥ M. As M ≥ N/(2(1/4 − ε) log4 3) ≥ N,
we know that 2a′
0 · 3b0 · 5d0 is ε-equidistributed, i.e., #d(2a′
0 · 3b0 · 5d0) belongs to the
interval ((1/4 − ε) log4(2a′
0 · 3b0 · 5d0), (1/4 + ε) log4(2a′
0 · 3b0 · 5d0)), for d = 0, 1, 2, 3.
Put a1 = #0(2a′
0 · 3b0 · 5d0), b1 = #1(2a′
0 · 3b0 · 5d0), c1 = #2(2a′
0 · 3b0 · 5d0), and
d1 = #3(2a′
0 · 3b0 · 5d0). In particular, a1, b1, c1 and d1 are bounded from above by
(1/4 + ε) log4(2a′
0 · 3b0 · 5d0) ≤ (1/4 + 2ε) log4(3b0 · 5d0) ≤ βα(b0 + d0) for M large enough
(namely, for (1/4 + ε) log4(2 · 3M · 5M ) ≤ (1/4 + 2ε) log4(3M · 5M ) to hold), writing β
for 1/4 + 2ε and α for log4 5.

We have
 f 2(n) = 2⌊a0/2⌋+c0 · f (2a′
0 · 3b0 · 5d0) = 2⌊a0/2⌋+c0+a1+2c1 · 3b1 · 5d1,

17

and then

f 3(n) = f (2⌊a0/2⌋+c0+a1+2c1 ·3b1 ·5d1) = 2⌊(⌊a0/2⌋+c0+a1+2c1)/2⌋f (2(⌊a0/2⌋+c0+a1+2c1)′ ·3b1 ·5d1).

Putting a2 = #0(2(⌊a0/2⌋+c0+a1+2c1)′ · 3b1 · 5d1), b2 = #1(2(⌊a0/2⌋+c0+a1+2c1)′ · 3b1 · 5d1),
c2 = #2(2(⌊a0/2⌋+c0+a1+2c1)′ · 3b1 · 5d1), and d2 = #3(2(⌊a0/2⌋+c0+a1+2c1)′ · 3b1 · 5d1), we have

f 3(n) ≤ 2a0/4+c0/2+a1/2+c1+a2+2c2 · 3b2 · 5d2. (12)

As b1 ≥ (1/4 − ε) log4(2a′
0 · 3b0 · 5d0) ≥ (1/4 − ε) log4(3b0 · 5d0) ≥ 2M(1/4 − ε) log4 3 ≥ N,
the number 2(⌊a0/2⌋+c0+a1+2c1)′ · 3b1 · 5d1 is ε-equidistributed, i.e., a2, b2, c2 and d2 belong
to ((1/4 − ε) log4(2(⌊a0/2⌋+c+a1+2c1)′ · 3b1 · 5d1), (1/4 + ε) log4(2(⌊a0/2⌋+c+a1+2c1)′ · 3b1 · 5d1)).

This implies that a2, b2, c2 and d2 can be bounded from above by the following expres-
sion: (1/4 + ε) log4(2(⌊a0/2⌋+c0+a1+2c1)′ · 3b1 · 5d1) ≤ (1/4 + 2ε)α(b1 + d1) ≤ 2β2α2(b0 + d0).
Plugging these estimates for a1, . . . , d1, a2, . . . , d2 in (12), we get that

f 3(n)
n ≤ 4a0/8+c0/4+(3/4αβ+3α2β2+4α3β2)(b0+d0)

4a0+b0+c0+d0−1

= 4 · 4−7a0/8−3c0/4+(3/4αβ+3α2β2+4α3β2−1)(b0+d0)

≤ 4 · n
θ,

for some 0 < θ < 1 since 3αβ/4 + 3α2β2 + 4α3β2 < 1.

(iii) Larger bases

Finally, we prove the result for b ≥ 5. Let f denote S2,b. We will prove that either
f (n) ≤ c · n
cb or f 2(n) ≤ c · n
cb if n is large enough, for some c > 0 and 0 < cb < 1.

We start applying Conjecture 4 a few times: for every prime p dividing b and for every
proper divisor d of b (i.e., a divisor which is less than b, including 1), we apply it for
q = b, a = d, Fp = {r prime : r ≤ b+1, r ̸= p}. Taking the maximum of the N obtained
by each application of the conjecture, we get the following statement: for every ε > 0,
there is N such that, for every proper divisor d of b and every prime divisor p of b, the
number d ∏

qi∈Fp qai
i is ε-equidistributed if any of the ai is at least N.

Let ε > 0 be such that (b + 1)!(logb(b+1))(1/b+ε) < b. Such an ε exists by the ﬁrst item of
Lemma 14 and by the fact that limε→0+(b+1)!
ε logb(b+1) = 1. Moreover, let n ≥ b
4M , with
M ≥ N, where N is as in the paragraph above. For i ∈ {0, . . . , b − 1}, let ni denote the
number of digits i in the base-b expansion of n. We know that ∑b−1
i=0 ni ≥ logb n ≥ 4M.

By the deﬁnition of f , we have f (n) = ∏b−1
i=0(i + 2)ni. We may rewrite this number as
b
t · d · ∏

qi∈Fp qαi
i , where t ≥ 0 is an integer, d is a proper divisor of b and p is a prime
divisor of b. In particular, we have f (f (n)) = 2tf (d · ∏

qi∈Fp qαi
i ). Note that we have
t ≥ nb−2, since all the nb−2 powers of b are factored out to the term b
t.

18

Suppose ﬁrst that nb−1 ≥ M or nb−3 ≥ M. Then, the number d · ∏
qi∈Fp qαi
i is ε-
equidistributed, since no prime factor from b + 1 or b − 1 is factored out in b
t or d
in the product b
t · d · ∏

qi∈Fp qαi
i , as b is coprime with b − 1 and b + 1, and hence
αi ≥ max{nb−3, nb−1} ≥ M for some i. The number of occurrences of every digit from
0 to b − 1 in f (n) belongs, then, to the interval ((1/b − ε) logb(d · ∏

qi∈Fp qαi
i ), (1/b +
ε) logb(d · ∏
qi∈Fp qαi
i )). This implies that

f 2(n) ≤ 2t · (2 · · · (b + 1))(1/b+ε) logb(d·∏qi∈Fp qαi
i )

= 2t · (b + 1)!
(1/b+ε) logb( 1
bt ∏b−1
i=0 (i+2)ni )

= ( 2
(b + 1)!(1/b+ε)
 )t · (b + 1)!
(1/b+ε) ∑b−1
i=0 ni logb(i+2)

≤ 1 · (b + 1)!
(1/b+ε) logb(b+1) ∑b−1
i=0 ni

≤ b
cb ∑b−1
i=0 ni

= c · n
cb

for some c > 0, 0 < cb < 1, where the last inequality comes from the choice of ε.

Suppose now, on the other hand, that nb−1 < M and nb−3 < M. First, if nb−2 < M,
as M ≤ logb(n)/4 and ∑b−1
i=0 ni ≤ logb n, we have ∑b−4
i=0 ni ≥ logb(n)/4. Then,

f (n)
n = ∏b−1
i=0 (i + 2)ni

b
∑n−1
i=0 −1

≤ b · ( b − 1
b
 )∑b−3
i=0 ni (b + 1
b
 )nb−1

≤ b ·
 ( b
2 − 1
b2
 )logb(n)/4

= b · n
logb
( b2−1
b2
 )/4,

as desired, since logb ( b2−1
b2 ) < 0.

Finally, if nb−1, nb−3 < M ≤ logb(n)/4 and nb−2 ≤ M, then, applying the trivial bound
f (m) ≤ (b + 1)1+logb m and noting that t ≥ nb−2 and ∑n−4
i=0 ni + nb−2 ≥ logb(n)/2, we
get
 f 2(n)
n ≤ 2t · f (d · ∏

qi∈Fp qαi
i )

b
∑b−1
i=0 ni−1

≤ 2t · (b + 1)1+logb(d·∏qi∈Fp qαi
i )

b
∑b−1
i=0 ni−1
 19

= 2t · (b + 1)1+logb((
∏b−1
i=0 (i+2)ni )/bt)

b
∑b−1
i=0 ni−1

≤ b(b + 1) · ( 2
b + 1
 )t ·
 ( (b + 1)logb(b−2)

b
 )∑b−4
i=0 ni · ( b + 1
b
 )nb−2

·
 ( (b + 1)logb(b−1)

b
 )nb−3 ·
 ((b + 1)logb(b+1)

b
 )nb−1

≤ b(b + 1) · ( 2
b
 )nb−2 ·
 ((b + 1)logb(b−2)

b
 )∑b−4
i=0 ni ·
 ( (b + 1)logb(b−1)

b
 )nb−3

·
 ( (b + 1)logb(b+1)

b
 )nb−1 .

By the second item of Lemma 14, (b+1)logb(b−1)

b < 1. This inequality, together with the
simple fact that (b + 1)logb(b−2) ≥ 2 for b ≥ 4, implies

f 2(n)
n ≤ b(b + 1) ·
 ( (b + 1)logb(b−2)

b
 )nb−2+∑b−4
i=0 ni ·
 ((b + 1)logb(b+1)

b
 )nb−1

≤ b(b + 1)
 ((b + 1)2 logb(b−2)+logb(b+1)

b3
 )logb(n)/4 ,

where we used that nb−2+∑b−4
i=0 ≥ logb(n)/2 and nb−1 ≤ logb(n)/4 in the last inequality.
This completes the proof, since, by the third item of Lemma 14, the expression raised
to logb n in the last line above is smaller than 1, whence f 2(n)
n is bounded by b(b + 1) · n
γ

for some γ < 0.

Remark 16. The proof of Theorem 15 gives that S2,b(n) ≤ n
γ for some γ < 1 if n is large
enough. As in Theorem 13, this implies that the persistence of every number n under S2,b
is at most c log log n for some constant c. It is not hard to see that, as before, there is some
sequence of integers for which this is sharp up to a constant factor (i.e., there exists an
increasing sequence (nk)k≥1 of integers such that the persistence of nk is at least c′ log log nk
for some c′ > 0 and every k).

5.4 The (4, 5) problem diverges

Using a proof similar to the proof of Theorem 15, one can show that the sequence of iterates
of both S3,4 and S3,5 starting from every integer stabilizes (indeed, one can again prove that,

20

in case f = S3,4 or f = S3,5, for every suﬃciently large n, f j(n) ≤ n for some j ∈ {1, 2, 3, 4}).
On the other hand, our next result shows that, assuming Conjecture 4, S4,5 is the smallest
instance where the opposite behavior occurs, namely the sequence of iterates starting from
every suﬃciently large integer diverges.

Theorem 17. Conjecture 4 implies the following: there is an integer n0 such that, for every
n ≥ n0, the sequence of iterates (Sk
4,5(n))k≥0 diverges to inﬁnity.

Proof. Put f = S4,5. We will prove the following statement which obviously implies the
theorem: there is n0 such that, for every n ≥ n0, f 5(n) > n.
We apply Conjecture 4 for q = 5, a = 1 and F = {2, 3, 7} to get the following statement:
for every ε > 0, there is N such that 2x · 3y · 7z is ε-equidistributed whenever one of x, y, z
is at least N. In particular, the number 4x · 6y · 7z · 8w is equidistributed whenever one of x,
y, z and w is at least N.
Take ε = 0.001, put δ = 1/5 − ε and let n ≥ 54M +M 2, with Mδ3(log5 4)3 ≥ N, where N
is the integer given by the application of Conjecture 4 as in the paragraph above with this
value of ε; and M is large enough as for the last inequality in (13) to hold.
Let a0, . . . , e0 denote, respectively, #0(n), . . . , #4(n); and, for k ≥ 1, let ak, . . . , ek denote,
respectively, #0(4bk−2+ak−1 · 6ck−1 · 7dk−1 · 8ek−1), . . . , #4(4bk−2+ak−1 · 6ck−1 · 7dk−1 · 8ek−1), where
we put b−1 = 0. With this notation, we have

f k(n) = 4bk−2+ak−1 · 5bk−1 · 6ck−1 · 7dk−1 · 8ek−1

for every k ≥ 1.
Assume ﬁrst that one of a0, c0, d0, e0 is at least M. As M ≥ N/δ3(log5 4)3 > N, this
implies that 4a0 · 6c0 · 7d0 · 8e0 is ε-equidistributed. In particular, we have

a1, . . . , e1 ≥ δ log5(4a0 · 6c0 · 7d0 · 8e0)
= δ(a0 log5 4 + c0 log5 6 + d0 log5 7 + e0 log5 8).

In turn, as a1, . . . , e1 ≥ δ(a0 + c0 + d0 + e0) log5 4 > N, this implies that 4b0+a1 · 6c1 · 7d1 · 8e1
is ε-equidistributed, so

a2, . . . , e2 ≥ δ log5(4b0+a1 · 6c1 · 7d1 · 8e1)
= δ((b0 + a1) log5 4 + c1 log5 6 + d1 log5 7 + e1 log5 8)
= δ log5 4 · b0 + δ2 log5 1344(a0 log5 4 + c0 log5 6 + d0 log5 7 + e0 log5 8).

As the choice of M guarantees that the a2, . . . , e2 and a3, . . . , b3 are greater than N, the
same reasoning can be applied two more times to get that

a3, . . . , e3 ≥ δ log5(4b1+a2 · 6c2 · 7d2 · 8e2)
= δ((b1 + a2) log5 4 + c2 log5 6 + d2 log5 7 + e2 log5 8)
≥ δ2 log5 1344 log5 4 · b0
 21

+ δ2(log5 4 + δ(log5 1344)2)(a0 log5 4 + c0 log5 6 + d0 log5 7 + e0 log5 8)

and
 a4, . . . , e4 ≥ δ log5(4b2+a3 · 6c3 · 7d3 · 8e3)
= δ((b2 + a3) log5 4 + c3 log5 6 + d3 log5 7 + e3 log5 8)
≥ δ2((log5 4)2 + δ log5 4(log5 1344)2)b0
+ δ3 log5 1344(2 log5 4 + δ(log5 1344)2)·
· (a0 log5 4 + c0 log5 6 + d0 log5 7 + e0 log5 8).

Finally, this implies that

f 5(n)
n > 4b3+a4 · 5b4 · 6c4 · 7d4 · 8e4

5a0+b0+c0+d0+e0

≥
 ( 4δ2 log5 4(log5 4+δ(log5 1344)2) · 6720δ3 log5 4 log5 1344(2 log5 4+δ(log5 1344)2)

5
 )a0+c0+d0+e0 ·

·
 ( 4δ2 log5 1344 log5 4 · 6720δ2 log5 4(log5 4+δ(log5 1344)2)

5
 )b0

> 1,

as a straightforward computation shows that each of the expressions inside the parenthesis
are greater than 1 (indeed, the ﬁrst and the second expression are greater than 1.14 and
1.06, respectively).
Suppose now, on the other hand, that each of a0, c0, d0, e0 is less than M. This implies
that b0 > M 2 > N, which in turn implies that 4b0+a1 · 6c1 · 7d1 · 8e1 is ε-equidistributed. Hence,
we have a2, · · · , e2 ≥ δ log5(4b0+a1 · 6c1 · 7d2 · 8e1) ≥ (δ log5 4)b0 > N. Again, this implies
that 4b1+a2 · 6c2 · 7d2 · 8e2 is ε-equidistributed and a3, . . . , e3 ≥ δ log5(4b1+a2 · 6c2 · 7d2 · 8e2) ≥
δ2 log5 4 log5 1344 · b0 > N. Finally, this implies that a4, . . . , e4 ≥ δ log5(4b2+a3 · 6c3 · 7d3 · 8e3) ≥
δ2 log5 4(log5 4 + δ(log5 1344)2)b0, and then

f 5(n)
n > 4b3+a4 · 5b4 · 6c4 · 7d4 · 8e4

5a0+b0+c0+d0+e0

>
 ( 4δ2 log5 4 log5 1344 · 6720δ2 log5 4(log5 4+δ(log5 1344)2)

5
 )b0 · ( 1
5
)4M

≥
 ( 4δ2 log5 4 log5 1344 · 6720δ2 log5 4(log5 4+δ(log5 1344)2)

5
 )M 2
 · (1
5
 )4M

> 1, (13)

for large M, as the expression being raised to M 2 is greater than 1 (approximately 1.06).

22

5.5 Larger t and b

In this section, we consider the behavior of the t-shifted problem in base b when t is bounded
by a function of b. As one would expect, the equidistribution conjectures imply that, if b is
very large compared to t, then the sequence of iterates starting from any integer stabilizes
in the t-shifted problem in base b. One the other hand, if t is very close to b, then almost no
sequence stabilizes. Our next results give some estimates on the ranges of t and b (both for
small and large b) where each of those behaviors appear. Again, we start with a technical
lemma.

Lemma 18. Let t and b be positive integers such that b ≥ 5 and t ≤ b/4. Then

(i) b
logb(t)−1 · (b+t−1)logb(b+t−1)

b < 1;

(ii) ( (b+t−1)!
(t−1)! ) 1
b logb(b+t−1) < b.

Proof. (i) The inequality is equivalent, applying logarithms, to

log b · log t + (log(b + t − 1))2 < 2(log b)2. (14)

The left-hand side of (14) is increasing with t, so bounded from above by log b·log(b/4)+
(log(5b/4))2. Expanding this expression, we get

2(log b)2 + log(25/64) log b + (log(5/4))2,

which is smaller than 2(log b)2 whenever b ≥ e
− log(5/4)2/ log(25/64) ≈ 1.05.

(ii) The inequality is equivalent, taking logarithms twice, to

log log(b + t − 1) + log log ( (b + t − 1)!
(t − 1)!
 ) < log b + 2 log log b. (15)

By the inequality of arithmetic and geometric means, we have that

(b + t − 1)!
(t − 1)! = t(t + 1) · · · (b + t − 1)

≤ (t + (t + 1) + · · · + (b + t − 1)
b
 )b

= (b + 2t − 1
2
 )b

< (3b
4
 )b ,

as t ≤ b/4.
 23

We also have b + t − 1 < 5b/4. Plugging these two estimates on the left-hand side of
(15) and using that log log x is a concave and increasing function on its domain, we get
that

log log(b + t − 1) + log log ( (b + t − 1)!
(t − 1)!
 ) < log log(5b/4) + log log(3b/4)b

= log b + log log(5b/4) + log log(3b/4)

< log b + 2 log log ( 5b/4 + 3b/4
2
 )

= log b + 2 log log b.

Theorem 19. Conjecture 4 implies the following: for every prime number b ≥ 5 and t ≤ b/4,
the sequence of iterates (Sk
t,b(n))k≥1 stabilizes for every positive integer n.

Proof. The proof follows the ideas of the proof of Theorem 15. Let t and b be integers
such that 3 ≤ t ≤ b/4 (the cases t = 1 and t = 2 were covered by Theorems 7 and
15, respectively). Again, we will prove that, for every suﬃciently large integer n, either
f (n) ≤ n
cb or f 2(n) ≤ n
cb, where f = St,b and 0 < cb < 1.
We apply Conjecture 4 with q = b, a = 1, F = {p prime : p ≤ b + t − 1, p ̸= b} to get the
following statement: for every ε > 0, there is N such that the number ∏

pi prime:pi≤b+t−1,pi̸=b pai
i
is ε-equidistributed if any of the ai is at least N. Taking the maximum of the N obtained
by each application of the conjecture, we get the following statement: for every ε > 0, there
is N such that, for every proper divisor d of b and every prime divisor p of b, the number
d ∏

qi prime,qi≤b+t−1,qi̸=p qai
i is ε-equidistributed if any of the ai is at least N.
Let ε > 0 be so small as to satisfy

1
b · ((b + t − 1)!
(t − 1)!
 )( 1
b +ε) logb(b+t−1) < 1,

which is possible by the second item of Lemma 18. Moreover, let n ≥ b
2(b−1)M , with M ≥ N,
where N is as in the paragraph above. For i ∈ {0, . . . , b − 1}, let ni denote the number of
digits i in the base-b expansion of n. We know that ∑b−1
i=0 ni ≥ logb n ≥ 2(b − 1)M. This
implies that either ni ≥ M for some i ̸= b − t or nb−t ≥ (b − 1)M.
By the deﬁnition of f , we have f (n) = ∏b−1
i=0 (i + t)ni, where ni is the number of digits i
of n in base b. Note that ∏b−1
i=0 (i + t)ni = b
nb−t · ∏b−1
i=0,i̸=b−t(i + t)ni, and that b does not divide
the second product. Then, we have f 2(n) = t
nb−t · f (∏b−1
i=0,i̸=b−t(i + t)ni)
Suppose ﬁrst that ni ≥ M for some i ̸= b−t. This implies that the number ∏b−1
i=0,i̸=b−t(i+
t)ni is ε-equidistributed, i.e., the number of occurrences of every digit from 0 to b − 1 belongs
to the interval ((1/b − ε) logb(∏b−1
i=0,i̸=b−t(i + t)ni), (1/b + ε) logb(∏b−1
i=0,i̸=b−t(i + t)ni)). Hence,

as n ≥ b
∑b−1
i=0 ni−1, it follows that

f 2(n)
n ≤ 1
n · t
nb−t · (t · · · (t + b − 1))( 1
b +ε) logb(
∏b−1
i=0,i̸=b−t(i+t)ni )

24

= 1
n · b
nb−t logb t · ((b + t − 1)!
(t − 1)!
 )( 1
b +ε) ∑b−1
i=0,i̸=b−t ni(logb(i+t))

≤ 1
n · b
nb−t logb t
 


((b + t − 1)!
(t − 1)!
 )( 1
b +ε) logb(b+t−1)



∑b−1
i=0,i̸=b−t ni

≤ b · (b
logb t−1)nb−t 

1
b · ((b + t − 1)!
(t − 1)!
 )( 1
b +ε) logb(b+t−1)


∑b−1
i=0,i̸=b−t ni
 . (16)

The choice of ε implies that the expression inside the second parenthesis in the last line
of (16) is b
γ for some γ < 0, which completes the proof of this case, as logb(t) − 1 < 0 and
then (16) is bounded from above by b · b
γ′ ∑b−1
i=0 ni ≤ b · n
γ′ for some γ′ < 0.
Suppose now, on the other hand, that ni < M for every i ̸= b − t. This implies, as∑b−1
i=0 ni ≥ 2(b − 1)M, that nb−t ≥ (b − 1)M ≥ ∑b−1
i=0,i̸=b−t ni, and hence nb−t ≥ logb(n)/2 ≥
∑b−1
i=0,i̸=b−t ni. Applying a trivial bound f (m) ≤ (b + t − 1)1+logb m, we get that

f 2(n)
n = 1
n · t
nb−tf
 


 b−1∏

i=0,i̸=b−t(i + t)ni




≤ 1
n · b
nb−t logb t · (b + t − 1)1+∑b−1
i=0 logb(i+t)ni

≤ 2b
2 · b
(logb t−1)nb−t ·
 ( (b + t − 1)logb(b+t−1)

b
 )∑b−1
i=0,i̸=b−t ni

≤ 2b
2 ·
 (
b
logb(t)−1 · (b + t − 1)logb(b+t−1)

b
 )logb(n)/2

= 2b
2 · n
γ,

where, by the ﬁrst item of Lemma 18, b
logb(t)−1 · (b+t−1)
logb(b+t−1)

b < 1, whence γ < 0. This
concludes the proof.

The estimates in the proof of Theorem 19 can be applied asymptotically in b (instead
of for every b ≥ 4) using Stirling’s formula (instead of a precise inequality for every n) to
improve the constant 1/4 in to approximately 0.316 for large b. Namely, the following result,
whose proof is very similar to the proof of Theorem 19 and will be omitted, holds:

Theorem 20. Conjecture 4 implies the following: let c0 be the solution of 2 log(1 + c) +
c log(1 + 1/c) = 1 in the interval (0, 1) (c0 ≈ 0.315999). Then, for every c ≤ c0, there is
b0 with the following property: for every prime number b ≥ b0 and t ≤ cb, the sequence of
iterates (Sk
t,b(n))k≥1 stabilizes for every positive integer n.

25

Remark 21. What we stated in Remark 16 holds for Theorems 19 and 20 as well, i.e.,
the persistence is bounded by c log log n for every n and some c, and there is an increasing
sequence of integers (nk)k≥1 with persistence at least c′ log log nk for some c′ > 0 and every k.

On the other end of the spectrum, we have a divergence result, which we state now, after
a technical lemma.

Lemma 22. Let c0 be the solution 2 log c + log(c + 1) + c log(1 + 1/c) = 1 in the interval
(0, 1) (c0 ≈ 0.865722). Then, for every c > c0, there is b0 with the following property: Let
t and b be integers, with b ≥ b0 and t ≥ cb. If we put δ = 1/b − 1/b
2, then the following
inequalities hold:

(i) ( (t−1+b)!
(t−1)! )δ logb t > b;

(ii) t
δ logb t · ( (t−1+b)!
(t−1)! )(b−2)δ2(logb t)2 > b.

Proof. We will prove that the logarithm to base b of the two expressions on the left-hand
sides of i) and ii) are greater than 1 for large b. For that purpose, we use the following
logarithmic form of the well-known Stirling approximation:

log n! = n log n − n + O(log n).

(i) We have
logb
 ((t − 1 + b)!
(t − 1)!
 )δ logb t =

= δ log t
(log b)2 · (
(t − 1 + b) log(t − 1 + b) − (t − 1) log(t − 1)

− b + O(log b))

= δ log t
(log b)2 · (b log(t − 1 + b) + (t − 1) log(1 + b/(t − 1))

− b + O(log b))

≥ δ log cb
(log b)2 · (b log((c + 1)b) + cb log(1 + 1/c) − b + O(log b))

≥ δb
 (
1 + log c + log(c + 1) + c log(1 + 1/c) − 1
log b + O ( 1
b log b
))

≥ 1 + log c + log(c + 1) + c log(1 + 1/c) − 1
log b + O (1
b
 ) ,

since δb = 1 − 1/b. This expression is greater than 1 for large b as we have log c +
log(c + 1) + c log(1 + 1/c) − 1 > log c0 + log(c0 + 1) + c0 log(1 + 1/c0) − 1 > 2 log c0 +
log(c0 + 1) + c0 log(1 + 1/c0) − 1 = 0.
 26

(ii) We apply the bound obtained in the ﬁrst part of the proof to get

logb
 (
t
δ logb t · ( (t − 1 + b)!
(t − 1)!
 )(b−2)δ2(logb t)2)

= δ ( log t
log b
 )2 + (b − 2)δ log t
log b logb
 ((t − 1 + b)!
(t − 1)!
 )δ logb t

≥ ( 1
b − 1
b2
 ) (
1 + log c
log b
 )2 + (
1 − 2
b
 ) (1 + 1
b
 ) (1 + log c
log b
 ) ·

·
 (
1 + log c + log(c + 1) + c log(1 + 1/c) − 1
log b + O (1
b
 ))

= 1 + 2 log c + log(c + 1) + c log(1 + 1/c) − 1
log b + O ( 1
b
 ) ,

which is greater than 1 for large b since 2 log c + log(c + 1) + c log(1 + 1/c) − 1 >
2 log c0 + log(c0 + 1) + c0 log(1 + 1/c0) − 1 = 0.

Theorem 23. Conjecture 4 implies the following: let c0 be the solution 2 log c + log(c + 1) +
c log(1 + 1/c) = 1 in the interval (0, 1) (c0 ≈ 0.865722). Then, for every c > c0, there is b0
with the following property: for every prime number b ≥ b0 and positive integer t ≥ cb, the
sequence of iterates (Sk
t,b(n))k≥1 diverges for every suﬃciently large integer n.

Proof. Fix c > c0. Let b0 be the integer given by Lemma 22 for this c, and let t, b be integers
such that t ≥ cb and b ≥ b0.
We apply Conjecture 4 with q = b, a = 1, F = {p prime : p ≤ b + t − 1, p ̸= b} to get the
following statement: for every ε > 0, there is N such that the number ∏

pi prime:pi≤b+t−1,pi̸=b pai
i
is ε-equidistributed if any of the ai is at least N.
Put f = St,b. We can write f (n) = ∏b−1
i=0 (i + t)ni = b
nb−t · ∏b−1
i=0,i̸=b−t(i + t)ni. As b
is a prime number, b ∤ ∏b−1
i=0,i̸=b−t(i + t)ni, and then f 2(n) = t
nb−t · f (∏b−1
i=0,i̸=b−t(i + t)ni).
Let n
′
i denote the number of digits i in ∏b−1
i=0,i̸=b−t(i + t)ni. Then we may rewrite f 2(n) =
t
nb−t · ∏b−1
i=0 (i + t)n′
i = b
n′
b−t · t
nb−t · ∏b−1
i=0,i̸=b−t(i + t)n′
i.
Let ε = 1/b
2 and put δ = 1/b − ε. Let M ≥ N/(δ logb 2), where N is the integer given by
the application of Conjecture 4 as above with ε = 1/b
2, and M is large enough as to satisfy
that (17) is greater than 1. Let n ≥ b
(b−1)M +M 2 be an integer. We will prove that f 3(n) > n,
which implies that the sequence of iterates of f starting from any integer at least b
(b−1)M +M 2

diverges.
Either ni ≥ M for some i ̸= b − t or nb−t ≥ M 2 ≥ M ≥ N. In the ﬁrst case, this implies
that n
′
i ≥ δ logb(∏b−1
i=0,i̸=b−t(i + t)ni) ≥ (δ logb 2) ∑b−1
i=0,i̸=b−t ni ≥ (δ logb 2)M ≥ N. In any case,
the number t
nb−t ·∏

i=0,i̸=b−t(i+t)n′
i is ε-equidistributed. This means that every digit from 0 to

27

b − 1 appears at least δ logb(t
nb−t · ∏

i=0,i̸=b−t(i + t)n′
i) = δ(nb−t logb t + ∑b−1
i=0,i=b−t n
′
i logb(i + t))
times in this number, and hence

f 3(n) = f (
b
n′
b−t · t
nb−t ·
 b−1∏

i=0,i̸=b−t
(i + t)n′
i)

= t
n′
b−t · f (
t
nb−t ·
 b−1∏

i=0,i̸=b−t
(i + t)n′
i)

≥ t
n′
b−t(t(t + 1) . . . (b + t − 1))δ(nb−t logb t+∑b−1
i=0,i̸=b−t n′
i logb(i+t))

≥ t
n′
b−t · ((t − 1 + b)!
(t − 1)!
 )δ(nb−t+∑b−1
i=0,i̸=b−t n′
i) logb t . (16)

Suppose ﬁrst that ni ≥ M for some i ̸= b−t. Then ∏b−1
i=0,i̸=b−t(i+t)ni is ε-equidistributed,
which implies that n
′
i ≥ δ logb(∏b−1
i=0,i̸=b−t(i + t)ni) ≥ δ logb t ∑b−1
i=0,i̸=b−t ni for every 1 ≤ i ≤
b − 1. In this case, bound (16) implies, together with Lemma 22, that

f 3(n) ≥
 (
t
δ logb t · ( (t − 1 + b)!
(t − 1)!
 )(b−2)δ2(logb t)2)∑b−1
i=0,i̸=b−t ni · ((t − 1 + b)!
(t − 1)!
 )(δ logb t)nb−t

> b
∑b−1
i=0,i̸=b−t ni+nb−t

≥ n.

Finally, if ni < M for every i ̸= b − t, then nb−t ≥ M 2. Moreover, we have n
′
i ≤
logb(∏b−1
i=0,i̸=b−t(i + t)ni) < b logb(2b)M for every 0 ≤ i ≤ b − 1, and then, using (16), we get
that
 f 3(n)
n ≥ 1
n · t
n′
b−t · ( (t − 1 + b)!
(t − 1)!
 )δ(nb−t+∑b−1
i=0,i̸=b−t n′
i) logb t

≥ 1
n · ((t − 1 + b)!
(t − 1)!
 )(δ logb t)nb−t

>
 ( 1
b · ((t − 1 + b)!
(t − 1)!
 )δ logb t)nb−t · b
− ∑b−1
i=0,i̸=b−t ni

≥
 ( 1
b · ((t − 1 + b)!
(t − 1)!
 )δ logb t)M 2
 · b
−bM (17)

> 1,

if M is large enough (since, by Lemma 22, the base of M 2 in the last line of (17) is greater
than 1). This concludes the proof.
 28

Remark 24. As we saw before (in Theorems 19 and 20), if one applies bounds for n! that
hold for every n instead of the asymptotic Stirling formula, it is possible to get a result of the
following form, with c being a constant greater than c0 in Theorem 23: let b ≥ 7 be a prime
and t ≥ cb. Conjecture 4 implies that, for every suﬃciently large integer n, the sequence of
iterates (Sk
t,b(n))k≥1 diverges to inﬁnity.

6 Concluding remarks

As we made clear from the beginning, most of the main results in the present paper (Theo-
rems 5, 10, 15, 17, 19 and 23) are conditional on the validity of Conjecture 1 or 4. There is
ample experimental evidence in favor of Conjecture 1, and further support would be provided
if one could prove our main results unconditionally. Conversely, of course, if any one of these
unconditional statements were proved to be false, then Conjecture 1 (or 4) would have to be
false. However, given the computational evidence and robust heuristics available [2], we feel
conﬁdent that Conjectures 1 and 4 must be true.

7 Acknowledgments

We wish to thank the referee for several remarks and suggestions that led to a considerable
improvement of our exposition.

References

[1] A. F. Beardon, Sums of squares of digits, Math. Gaz. 82 (1998), 379–388.

[2] E. de Faria and C. Tresser, On Sloane’s persistence problem, Exp. Math. 23 (2014),
363–382.

[3] M. R. Diamond and D. D. Reidpath, A counterexample to conjectures by Sloane and
Erd˝os concerning the persistence of numbers, J. Recreat. Math. 29 (1998), 89–92.

[4] P. Erd˝os, Some unconventional problems in number theory, Math. Mag. 52 (1979),
67–70.

[5] R. K. Guy, Unsolved Problems in Number Theory, Vol. 1, Springer Science & Business
Media, 2013.

[6] A. M. Herzberg and M. R. Murty, Some remarks on iterated maps of natural numbers,
Resonance 19 (2014), 1038–1046.

[7] H. J. Hinden, The additive persistence of a number, J. Recreat. Math. 7 (1974), 134–135.

29

[8] W. Narkiewicz, A note on a paper of H. Gupta concerning powers of two and three,
Publikacije Elektrotehniˇckog fakulteta. Serija Matematika i ﬁzika 678/715 (1980), 173–
174.

[9] N. J. A. Sloane, The persistence of a number, J. Recreat. Math. 6 (1973), 97–98.

[10] S. S. Wagstaﬀ, Iterating the product of shifted digits, Fibonacci Quart. 19 (1981), 340–
347.

2010 Mathematics Subject Classiﬁcation: Primary 11A63; Secondary 11A67.
Keywords: persistence of a number, Sloane’s conjecture, products of digits, shifted Sloane
problem, equidistribution of digits.

(Concerned with sequences A036461, A335808, A335824, and A031346. )

Return to Journal of Integer Sequences home page.

30
