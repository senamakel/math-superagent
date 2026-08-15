<!-- source: http://emis.muni.cz/journals/PM/57f3/pm57f305.pdf | converted from PDF -->

PORTUGALIAE MATHEMATICA
Vol. 57 Fasc. 3 – 2000

A CELLULAR AUTOMATON ON A TORUS

C.I. Cobeli, M. Crˆas¸maru and A. Zaharescu

Abstract: In this paper we prove a conjecture of Brian Thwaites concerning the
evolution function of a certain cellular automaton on a torus.

In the seventies, when more and more people had access to personal comput-
ers, John Conway’s game of life became very popular. Since then, the study of
this type of game grew up into the theory of cellular automata. In [4] (see also
[1, page 311]) Brian Thwaites proposes a conjecture which leads to such a cellular
automaton.

Thwaites’s conjecture is: Given any ﬁnite sequence of rational numbers, take
the positive diﬀerences of successive members (including diﬀerencing the last
member with the ﬁrst); iteration of this operation eventually produces a set of
zeros if and only if the size of the set is a power of 2.

Our aim in this note is to prove that Thwaites conjecture holds true.
Let a0, ..., ad−1 be the given d rational numbers, which we may think as the
heights of d poles situated around a circle. These numbers are replaced at the
next step by d rational numbers given by the diﬀerence in heights of successive
poles, and then the process is repeated.
Being an iteration of the same operation, it resembles Conway’s life game.
For now the ﬁeld of play is a 1-dimensional torus and since, as we will see only
ﬁnitely many numbers which depend on the initial conﬁguration are involved, in
the long run, we will end up with a cycle. Finding the lengths of these cycles,
which depend mostly on d — the size of the torus —, is the interesting problem.
In other words, if d is a power of 2, Thwaites conjecture says that the length of
any cycle is equal to 1 (the shortest possible). We examine the lengths of the
cycles that occur and provide conditions on d which guarantee that these lengths
are small or long. A criterion which tests if a given integer is a period for this
evolution function is given in section 3.

Received : December 20, 1998; Revised : March 22, 1999.
AMS Subject Classiﬁcation: 11B85, 11A07.

312 C.I. COBELI, M. CR ˆAS¸MARU and A. ZAHARESCU

1 – Proof of Thwaites conjecture

We begin by making some notations which set the problem in a clearer frame-
work. Let a0, ..., ad−1 be the given rational numbers. For convenience, we unpack
this ordered set of numbers by associating to it the inﬁnite sequence (a0, a1, ...),
where the components are deﬁned by

ak = ak+d for k ≥ 0 .(1)

Let us denote by Qd and by Nd the set of all the sequences with rational and
natural components respectively, satisfying (1). The evolution function φ : Qd → Qd
is deﬁned by φ(a0, a1, ...) = (a′ , a′ , ...), where

a′ = |ak − ak+1| for k ≥ 0 .(2)
 With these notations, Thwaites conjecture says that for any sequence
(a0, a1, ...) ∈ Qd, φ(n)(a0, a1, ...) = (0, 0, ...) for all suﬃciently large n ∈ N iﬀ
d is a power of 2. (Here φ(n) is the repeated composition of n samples of φ.)
Let’s note that all the components of φ(n)(a0, a1, ...) are nonnegative if n ≥ 1
and by multiplying all the components of the initial sequence (a0, a1, ...) by the
least common multiple of their denominators, we may assume that the domain
of our evolution function is Nd.
Let M = max {a0, ..., ad−1}. By the deﬁnition of φ, it is easy to see that all
the components of φ(n)(a0, a1, ...) are integers belonging to [0, M ]. Because there
are only ﬁnitely many such periodic sequences in Nd, it follows that given any
initial conﬁguration (a0, a1, ...), the repeated application of the evolution function
will eventually produce a cycle of sequences which keep repeating.
The next lemma shows that after suﬃciently many steps we always end up
with sequences with components having at most 2 distinct values.

Lemma 1. Let d be a positive integer, (a0, a1, ...) a sequence of nonnegative
integers satisfying (1) and suppose the function φ is deﬁned as above. Then
there is a positive integer a such that for suﬃciently large n all the components
of φ(n)(a0, a1, ...) belong to {0, a}.

Proof: The proof is by (inverse) induction. Let us look at a portion of the
sequence of numbers we get at some step. We write them on a line as follows:

..., b, 0, ..., 0,
︸
 ︷︷ ︸
s zeros m, ..., m,
︸ ︷︷ ︸
u numbers
 0, ..., 0,
︸ ︷︷ ︸
t zeros c, ...(3)
 A CELLULAR AUTOMATON ON A TORUS 313

Here m is the maximum of all our numbers at this step, b and c are nonzero,
m > b, m > c, s ≥ 0, t ≥ 0, u ≥ 1 and the part of the sequence that begins and
ends with m contains only 0’s or m’s. Then, after at most s + u + t steps, the
maximum of the numbers that are produced out by this portion of the sequence
will be ≤ max {m − b, m − c} < m. Of course at a given step the sequence of
numbers we obtain might contain several subsequences of the form (3), but what
happens is that after at most d steps the maximum of the numbers at that step
will be strictly less than m. The lemma then follows by induction.

By multiplying all the components of the initial conﬁguration by a−1, where
a is given by Lemma 1, we may assume that after suﬃciently many steps all the
components of the sequences we obtain are 0 or 1. Then our operation (taking
the positive diﬀerences of successive members of the sequence) is nothing else
than addition in the group (Z/2Z, + ).

Now there is a transparent way to generalize the game by replacing Z/2Z by a
more general ﬁnite monoid and also by playing on a multidimensional ﬁeld. The
operation in this case is to take the sum (or product if the multiplicative notation
is used) of the closest neighbors. We only mention here that if we keep the same
group Z/2Z, but play on a multidimensional torus, then we eventually obtain a
sequence of zeros if and only if the size of one of the dimensions is a power of 2.
This can be showed by following the same lines of proof.

Returning to our problem, let us observe that by starting with an arbitrary
sequence of 0’s and 1’s, by applying repeatedly the evolution function, we obtain
the following table which is ﬁlled with the beginning of the sequences obtained
in the ﬁrst few iterations.

Step 1 2 3 · · ·
0. a0 a1 a2 · · ·
1. a0 + a1 a1 + a2 a2 + a3 · · ·
2. a0 + a2 a1 + a3 a2 + a4 · · ·
3. a0 + a1 + a2 + a3 a1 + a2 + a3 + a4 a2 + a3 + a4 + a5 · · ·
4. a0 + a4 a1 + a5 a2 + a6 · · ·
5. a0 + a1 + a4 + a5 a1 + a2 + a5 + a6 a2 + a3 + a6 + a7 · · ·
6. a0 + a2 + a4 + a6 a1 + a3 + a5 + a7 a2 + a4 + a6 + a8 · · ·
7. a0 + a1 + · · · + a7 a1 + a2 + · · · + a8 a2 + a3 + · · · + a9 · · ·
8. a0 + a8 a1 + a9 a2 + a10 · · ·
9. a0 + a1 + a8 + a9 a1 + a2 + a9 + a10 a2 + a3 + a10 + a11 · · ·
10. a0 + a2 + a8 + a10 a1 + a3 + a9 + a11 a2 + a4 + a10 + a12 · · ·
· · · · · · · · · · · · · · ·

314 C.I. COBELI, M. CR ˆAS¸MARU and A. ZAHARESCU

Now it is easy to see by induction that in the above table if d = 2m then the
d-th row (and consequently all that follow after it) contains only 0’s. Also, there
are sequences of 0’s and 1’s, namely those containing an odd number of 1’s, for
which on the (d−1)-th row all the numbers are equal to 1. Thus, if d is a power of
2 and we start with an arbitrary set of 0’s and 1’s, then the process will produce
0’s in d steps and only for particular ak’s in less then d steps.
The outcome in the case d ̸= 2m can be also deduced easily by induction.
Thus, if we start for example with the periodic sequence given by a0 = 1 and
ak = 0 for 1 ≤ k ≤ d − 1, then 1 will always be the ﬁrst number on the rows
representing the steps of order a power of 2. Therefore, if d is not a power of 2
then there are sequences which will never produce a set of 0’s.
We summarize our result in the following theorem which proves the Thwaites
conjecture.

Theorem 1. Let d be a positive integer and suppose the evolution function φ
is deﬁned as above. Then there is a rational number r > 0 such that the repeated
application of φ to any initial sequence of rational numbers (a0, a1, ...) satisfying
(1) will eventually produce a cycle of sequences with the property (1) with all
their components in {0, r}. Moreover, the cycle will contain only the sequence
(0, 0, ...) independently on the initial sequence if and only if d is a power of 2.

2 – The length of cycles

We assume in this section that the evolution function φ is deﬁned on Ud,
where Ud, is the set of all the sequences with components in {0, 1}, satisfying (1).
This is not restrictive as we saw above and also has the advantage that it makes
φ to be additive.
Theorem 1 shows that if d is a power of 2 then the length of any cycle is equal
to 1. Suppose from now on that d is not a power of 2. Write d = 2k r with k ≥ 0
and r odd, r > 1. Let s be the order of 2 modulo r. Thus 2s −1 ≡ 0 (mod r).
Let F = {0, 1} be the ﬁeld with 2 elements and let I be the ideal of F [X]
generated by X d −1. Map the sequence a = (a0, ..., ad−1) to the coset

ψ(a) = I +
 d−1∑

i=0 ai X i

in the ring F [X]/I. Then φ(a) = I + 0 if and only if a = 0. Moreover ψ(φ(a)) =
(1 + X) φ(a). It follows that we get a cycle of length n, starting with e0 =

A CELLULAR AUTOMATON ON A TORUS 315

(1, 0, ..., 0) precisely when n is the least positive integer for which

(1 + X)n+c ≡ (1 + X)c (mod X d −1)(4)

in F [X], for some positive integer c.
We now prove that n = 2k(2s − 1) is always a period (thus the length of a
cycle will be a divisor of this number). We have:

(1 + X)2k+s = 1 + X 2k+s

since we are working in characteristic 2. But

X 2k+s − X 2k = X 2k (X 2k(2s−1) − 1) ≡ 0 (mod X d −1)

since d divides 2k(2s − 1). Hence

(1 + X)2k+s ≡ 1 + X 2k = (1 + X)2k (mod X d −1)

and we see that (4) is satisﬁed with n = 2k(2s − 1) and c = 2k.
Let us assume now that d = r is a prime number and that s is even, s = 2 t
say. In this case we want to show that d(2t − 1) is a period. We have 2t ≡ −1
(mod d), so that 2t = d m − 1 for some integer m. Since X d − 1 is coprime to X
it will suﬃce to prove that

X d(1 + X)d(2t−1)+d ≡ X d(1 + X)d (mod X d −1) ,(5)

taking the integer c to be d. However

(1 + X)d(2t−1)+d = {(1 + X)2t}d = (1 + X 2t)d = (1 + X md−1)d

from which it follows that

X d(1 + X)d(2t−1)+d ≡ X d(1 + X md−1)d = (X + X md)d (mod X d −1) .

The congruence (5) then follows since we may replace every occurrence of X d by 1,
modulo X d −1. We have proved the following

Theorem 2.

(i) Let d = 2kr, r odd and let s be the order of 2 modulo r. Then 2k(2s− 1)
is a period.

(ii) If d is an odd prime and s is even, s = 2 t, then d(2t −1) is a period.

One can ask about short and long periods.

316 C.I. COBELI, M. CR ˆAS¸MARU and A. ZAHARESCU

Let us assume that d is a prime. Then the period provided by Theorem 2 has
length 2s −1 or d(2t −1). In both cases the length is a multiple of d.

Short periods :

If d is a Mersenne prime, i.e. a prime d of the form d = 2p − 1 the length
of the above period is d. In this case each such period will actually be a cycle.
One doesn’t know if there are inﬁnitely many such primes. The ﬁrst Mersenne
primes are 3, 7, 31, 127, ... . As examples, we show below the cycles produced by
the initial conﬁguration e0 when d = 3 and d = 7:

(1, 0, 0) → (1, 0, 1) → (1, 1, 0) → (0, 1, 1) → (1, 0, 1) → · · ·

and
 (1, 0, 0, 0, 0, 0, 0) → (1, 0, 0, 0, 0, 0, 1) → (1, 0, 0, 0, 0, 1, 0) →

→ (1, 0, 0, 0, 1, 1, 1) → (1, 0, 0, 1, 0, 0, 0) → (1, 0, 1, 1, 0, 0, 1) →

→ (1, 1, 0, 1, 0, 1, 0) → (0, 1, 1, 1, 1, 1, 1) → (1, 0, 0, 0, 0, 0, 1) → · · ·

respectively.

Long periods :

In case 2 is a primitive root modulo d, the period provided by Theorem 2 is as
large as d(2 d−1
2 −1). Artin’s conjecture, still unsolved, says that there are inﬁnitely
many such primes. The ﬁrst prime numbers which satisfy Artin’s conjecture are
3, 5, 11, 13, 19, 29, 37, 53, 59, 61, 67, 83, 101, ....
We give below the cycle obtained in case d = 5.

(1, 0, 0, 0, 0) → (1, 0, 0, 0, 1) → (1, 0, 0, 1, 0) → (1, 0, 1, 1, 1) →

→ (1, 1, 0, 0, 0) → (0, 1, 0, 0, 1) → (1, 1, 0, 1, 1) → (0, 1, 1, 0, 0) →

→ (1, 0, 1, 0, 0) → (1, 1, 1, 0, 1) → (0, 0, 1, 1, 0) → (0, 1, 0, 1, 0) →

→ (1, 1, 1, 1, 0) → (0, 0, 0, 1, 1) → (0, 0, 1, 0, 1) → (0, 1, 1, 1, 1) →

→ (1, 0, 0, 0, 1) → · · ·

In their papers on Artin’s conjecture Rajiv Gupta and M. Ram Murty [2] and
Heath-Brown [3] use results by Bombieri, Friedlander, Fouvry, Deshouillers and
Iwaniec to show that there are inﬁnitely many primes p for which all the prime
factors of p−1
2 are larger than p1/4,
This shows that there are primes p for which the lengths of our periods are

huge, more precisely they are larger than 2p1/4 .

A CELLULAR AUTOMATON ON A TORUS 317

The lengths of cycles obtained for all primes d ≤ 47 are given in the following
Table.
 d length of cycle s 2s − 1 d(2s/2 − 1)
3 3 2 3 3
5 15 = 5 · 3 4 15 15
7 7 3 7
11 341 = 11 · 31 10 341 · 3 341
13 819 = 13 · 63 12 819 · 5 819
17 255 = 17 · 15 8 255 255
19 9709 = 19 · 511 18 9709 · 33 9709
23 2047 = 23 · 89 11 2047
29 475107 = 29 · 16383 28 475107 · 5 · 113 475107
31 31 5 31
37 3233097 = 37 · 87381 36 3233097 · 3 · 5 · 13 · 109 3233097 · 3
41 41943 = 41 · 1023 20 41943 · 52 41943
43 5461 = 43 · 127 14 5461 · 3 5461
47 8388607 = 47 · 178481 23 8388607

3 – A more general evolution function

In this section we introduce a more general evolution function and give a
useful method to calculate its repeated composition by itself. Finally, we deduce
a criterion which discerns if a given integer is or is not the length of a cycle of
chains produced by our original evolution function.

Let d be a positive integer and S = {0, 1}d. We denote by ρ(x) the circular
rotation to the right of the vector x ∈ S (e.g. for d = 7, ρ(1, 1, 0, 1, 0, 0, 0) =
(0, 1, 1, 0, 1, 0, 0) ) and · : S ×S → S the xor function (which is the componentwise
addition mod 2).

Let a1, a2, ..., as be s positive integers and deﬁne the evolution function
φ : S → S by
 φ(x) = ρ(a1)(x) · · · ρ(as)(x) .

Note that for s = 2, a1 = 0 and a2 = 1 we get our previous evolution function.

The following lemma adds together some properties of these functions.

318 C.I. COBELI, M. CR ˆAS¸MARU and A. ZAHARESCU

Lemma 2. For any nonnegative integers k, m, n and any x, y ∈ S we have:

1. ρ(xy) = ρ(x) ρ(y) ,

2. φ(xy) = φ(x) φ(y) ,

3. φ(ρ(x)) = ρ(φ(x)) ,

4. φ(m)(xy) = φ(m)(x) φ(m)(y) ,

5. φ(m)(ρ(x)) = ρ(φ(m)(x)) ,

6. φ(m)(ρ(n)(x)) = ρ(n)(φ(m)( x)) ,

7. φ(2k)(x) = ρ(2ka1)(x) · · · ρ(2kas)(x) .

Proof: Everything follows easily by deﬁnitions and/or by induction.

As a consequence, we immediately obtain the following:

Corollary 1. Suppose d = 2k. Then, for any x ∈ S and n ≥ 1 we have that
φ(d+n−1)(x) = 0 if s is even and φ(nd)(x) = x if s is odd.

Remark. It is easy to see that properties 1–7 from Lemma 2 do not depend
essentially on S. Thus we may replace {0, 1} by a more general monoid (a nilpo-
tent one may be of particular interest), for which similar consequences still hold
true. Let k = 2l0 + 2l1 + · · · + 2lµ(6)e the representation in base 2 of the positive integer k and assume l0 < ... < lµ.
We denote rij ≡ 2liaj (mod d) , 0 ≤ rij ≤ d−1(7)

for 0 ≤ i ≤ µ and 1 ≤ j ≤ s.

The next proposition gives an algorithm for the calculation of φ(k)(x) in
Os(log k) steps.

Proposition 1. Let x ∈ S and

y0 = ρr01(x) · · · ρr0s(x) .

Deﬁne inductively yj = ρrj1(yj−1) · · · ρrjs(yj−1)

for 1 ≤ j ≤ µ. Then φ(k)(x) = yµ .

A CELLULAR AUTOMATON ON A TORUS 319

Proof: Let k = k1 + 2l0. Using Lemma 2 we have

φ(k)(x) = φ(k1+2l0 )(x) = φ(k1)(φ(2l0 )(x))

= φ(k1)(ρ(2l0 a1)(x) · · · ρ(2l0 as)(x))

= φ(k1)(ρ(r01)(x) · · · ρ(r0s)(x)) = φ(k1)(y0) .

Similarly, let k1 = k2 + 2l1. Then we have

φ(k1)(y0) = φ(k2+2l1 )(y0) = φ(k2)(φ(2l1 )(y0))

= φ(k2)(ρ(2l1 a1)(y0) · · · ρ(2l1 as)(y0))

= φ(k2)(ρ(r11)(y0) · · · ρ(r1s)(y0)) = φ(k2)(y1) .

It is clear now that the proposition follows by induction following the same pro-
cedure.

A direct way to calculate φ(k)(x) is given in the next theorem.

Theorem 3. For any positive integer k represented as in (6), we have

φ(k)(x) = ∏

1≤i1,...,iµ+1 ≤s ρ(r0 i1 +···+rµ iµ+1 )(x) .

Proof: The proof is by induction on µ.
If µ = 0, then k = 2l0 and by Lemma 2

φ(2l0 )(x) = ρ(2l0 a1)(x) · · · ρ(2l0 as)(x) = ρ(r01)(x) · · · ρ(r0s)(x) .

Suppose the statement is true for µ − 1. Let k1 = k − 2lµ. Then the represen-
tation of k1 in base 2 has µ digits and we can apply to it the induction hypothesis.
Thus, by Lemma 2 we have

φ(k)(x) = φ(2lµ +k1)(x) = φ(2lµ )(φ(k1)(x))

= φ(2lµ )( ∏

1≤i1,...,iµ ≤s ρ(r0 i1 +···+rµ−1 iµ )(x)
)
 .

By the deﬁnition of φ(x), (7) and Lemma 2 this is

320 C.I. COBELI, M. CR ˆAS¸MARU and A. ZAHARESCU

=
 s∏

j=1 ρ(2lµ aj )( ∏

1≤i1,...,iµ ≤s ρ(r0 i1 +···+rµ−1 iµ )(x)
)

=
 s∏

j=1 ρ(rµj )( ∏

1≤i1,...,iµ ≤s ρ(r0 i1 +···+rµ−1 iµ )(x)
)

= ∏

1≤i1,...,iµ+1 ≤s ρ(r0 i1 +···+rµ iµ+1 )(x) ,

which concludes the proof of the theorem.

Now we apply this result to the particular evolution function from the previous
sections. Thus, from now on we assume that s = 2, a1 = 0 and a2 = 1, that is
φ(x) = x ρ(x).

Corollary 2. Let k = 2l0 + 2l1 + · · · + 2lµ be the representation in base 2 of
the positive integer k, where l0 < · · · < lµ, and φ(x) = x ρ(x). Denote

Rk = {r : r ≡ 2li (mod d), 0 ≤ r ≤ d−1, for some 0 ≤ i ≤ µ} .

Then
 φ(k)(x) = x ∏

R⊂P(Rk)ρ
( ∑

r∈R r)
(x)

for any x ∈ S.

Proof: By Theorem 3

φ(k)(x) = ∏

1≤i1,...,iµ+1 ≤2ρ(r0 i1 +···+rµ iµ+1 )(x) .(8)

By (7) and our hypothesis rj1 = 0 and rj2 ≡ 2lj (mod d), 0 ≤ rj2 < d for 0 ≤ j ≤ µ.
The corollary then follows by isolating in (8) the term with i1 = ... = iµ+1 = 1,
that is ρ(0)(x) (= x) and using the fact that

ρ
(∑

r∈∅ r)
(x) = 0 .

From Corollary 2 we deduce a criterion for cycling. Thus, φ(k)(x) = x is
equivalent to
 ∏

R⊂P(Rk) ρ
( ∑

r∈R r)
(x) = 0 .(9)
 A CELLULAR AUTOMATON ON A TORUS 321

Starting with x = e0 = (1, 0, ..., 0), we get φ(e0) = e0 ρ(e0) = (1, 1, 0, ..., 0) = e1.
Then, by (9) and Lemma 2, we deduce

∏

R⊂P(Rk)ρ
( ∑

r∈R r)
(e0) · ∏

R⊂P(Rk)ρ
(1+ ∑

r∈R r)
(e0) = 0 ,

which can be written as

∏

R⊂P(Rk)ρ
( ∑

r∈R r)
(e0) = ∏

R⊂P(Rk)ρ
(
1+ ∑

r∈R r)
(e0)

or
 ∏

R⊂P(Rk)ρ
( ∑

r∈R r)
(e0) = ρ
( ∏

R⊂P(Rk)ρ
( ∑

r∈R r)
(e0)
)
 .(10)

For any m ∈ {1, ..., d} let

νk,d(m) = #{
R ⊂ Rk : ∑

r∈R r ≡ m (mod d)} .

Then (10) becomes
 d∏

m=1 ρ νk(m)(e0) = ρ( d∏

m=1 ρ νk(m)(e0)) .

Since the only invariants of ρ are (0, ..., 0) and (1, ..., 1) we obtain the following:

Corollary 3. A positive integer k is a period for φ(x) = x ρ(x) if and only
if the numbers νk,d(m), 1 ≤ m ≤ d have the same parity.

We checked the values of νk,d(m) with k being the length of the shortest cycle
for diﬀerent values of d and we found some interesting regularity properties. Thus,
νk,d(m) not only have the same parity but most of the time they are equal. Some
nontrivial examples are:

1. If d = 11 then k = 341 = 1010101012 ,
ν341,11(11) = 1 and ν341,11(m) = 3 for 1 ≤ m ≤ 10.

2. If d = 13 then k = 819 = 11001100112 ,
ν819,13(13) = 3 and ν819,13(m) = 5 for 1 ≤ m ≤ 12.

322 C.I. COBELI, M. CR ˆAS¸MARU and A. ZAHARESCU

3. If d = 19 then k = 9709 = 100101111011012 ,
ν9709,19(19) = 25 and ν9709,19(m) = 27 for 1 ≤ m ≤ 18.

4. If d = 29 then k = 475107 = 11100111111111000112 ,
ν475107,29(29) = 563 and ν475107,29(m) = 565 for 1 ≤ m ≤ 28.

5. If d = 37 then k = 3233097 = 1100010101010101001001 and

m 1 2 3 4 5 6 7 8 9 10
ν3233097,37(m) 23 27 25 23 27 29 25 23 27 29

m 11 12 13 14 15 16 17 18 19 20
ν3233097,37(m) 27 29 33 33 31 31 31 29 29 31

m 21 22 23 24 25 26 27 28 29 30
ν3233097,37(m) 31 31 33 33 29 27 29 27 23 25

m 31 32 33 34 35 36 37
ν3233097,37(m) 29 27 23 25 27 23 19

5′. If d = 37 and we take k′ to be deﬁned by k′ = 3233097 ∗ 3 = 9699291 =
1001001111111111110110112, then
ν9699291,37(37) = 7083 and ν9699291,37(m) = 7085 for 1 ≤ m ≤ 36.

6. If d = 41 then k = 41943 = 10100011110101112 ,
ν41943,41(41) = 23 and ν41943,41(m) = 25 for 1 ≤ m ≤ 40.

7. If d = 43 then k = 5461 = 10101010101012 ,
ν5461,43(43) = 1 and ν5461,43(m) = 3 for 1 ≤ m ≤ 42.

This leads us to make the following

Conjecture. Suppose d is a prime number, s is the order of 2 mod d, s is
even and k = d(2s/2 − 1). Then

νk,d(1) = νk,d(2) = · · · = νk,d(d−1) = νk,d(d) + 2 .

A CELLULAR AUTOMATON ON A TORUS 323

ACKNOWLEDGEMENT – We are very grateful to the referee for providing us with a
slightly diﬀerent approach, which we follow in the proof of Theorem 2, which is simpler
than our original approach and gives better results (precisely, it provides proofs for both
parts (i) and (ii) of Theorem 2, while in the original version of the paper we only proved
part (i) and proposed (ii) as a conjecture).

REFERENCES

[1] Campbell, J.P. – Reviews, Mathematics Magazine, 69(4) (October 1996), 311–313.
[2] Gupta, R. and Ram Murty, M. – A Remark on Artin’s conjecture, Invent. Math.,
78 (1984), 127–130.
[3] Heath-Brown, D.R. – Artin’s conjecture for primitive roots, Quart. J. Math.
Oxford, 37(2), (1986), 27–38.
[4] Thwaites, B. – Two conjectures or how to win £ 1100, Mathematical Gazette, 80
(March 1996), 35–36.
 Cristian Ioan Cobeli,
Mathematics Research Institute of the Romanian Academy,
P.O. Box 1-764, Bucharest, 70700 – ROMANIA
E-mail: ccobeli@stoilow.imar.ro

and

Marcel Crˆa¸smaru,
Vatra Dornei, 5975 – ROMANIA
E-mail: mi@assist.cccis.ro

and

Alexandru Zaharescu,
McGill University, Department of Mathematics and Statistics, Burnside Hall,
805 Sherbrooke Street West, Montreal, Quebec, Canada, H3A-2K6 – CANADA
and
Mathematics Research Institute of the Romanian Academy,
P.O. Box 1-764, Bucharest, 70700 – ROMANIA
E-mail: zaharesc@math.mcgill.ca
