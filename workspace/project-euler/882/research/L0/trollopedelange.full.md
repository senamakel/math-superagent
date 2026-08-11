<!-- source: https://emis.muni.cz/journals/INTEGERS/papers/l54/l54.pdf | converted from PDF -->

#A54 INTEGERS 11 (2011)

DIGITAL SUMS AND FUNCTIONAL EQUATIONS

Roland Girgensohn
1

Zentrum Mathematik, Technische Universit¨at M¨unchen, Germany

Received: 8/30/10, Revised: 6/14/11, Accepted: 8/22/11, Published: 9/19/11

Abstract
Let S(n) denote the total number of digits ‘1’ in the binary expansions of the integers
between 1 and n − 1. The Trollope-Delange formula is a classical result which
provides an explicit representation for S(n) in terms of the continuous, nowhere
diﬀerentiable Takagi function. Recently, connections have been established between
digital sums such as S(n) and certain functional equations associated with the
Takagi function and its relatives. In the present paper we explore such a connection
to derive a new, simple proof for the Trollope-Delange formula as well as for some
of its generalizations involving power and exponential sums.

1. Introduction

Let S(n) denote the total number of digits ‘1’ in the binary expansions of the
integers between 1 and n − 1. Since that is roughly half the number of all of those
digits, it is not far-fetched that S(n) must be of the order S(n) = 1
2 n log2 n +
O(n). Interestingly, it turns out that the capital-O term in this expansion can be
given explicitly as n times a continuous, 1-periodic function of log2 n. This was
ﬁrst proved by J.R. Trollope in [19]; subsequently, in [4], H. Delange gave a very
short and direct proof of this representation. The continuous function appearing in
their representation is a slight modiﬁcation of the well-known continuous, nowhere
diﬀerentiable Takagi function, investigated by T. Takagi already in 1903 [18] and
often presented as one of the simplest examples of a nowhere diﬀerentiable function.
The Trollope-Delange formula has been investigated and generalized intensively
in the intervening years. Bases other than 2 have been examined, the occurrence
of subblocks other than the digit ‘1’ has been counted, and other modiﬁcations
have been applied to these quantities. Always it turned out that a representation of
Trollope-Delange type of the quantity in question could be given, often with explicit
continuous functions. Some references to such work are given below.

1Postal address: Kepserstr. 5, 85356 Freising, Germany

INTEGERS: 11 (2011) 2

The purpose of the present note is to give a new and simple proof of the Trollope-
Delange formula and then to turn this proof into a method by applying it to some
other variations and generalizations of these sums. The method proceeds by extract-
ing functional equations from the digital sum sequences such as S(n), identifying
their solutions and then using this process to prove a formula of Trollope-Delange
type in just a few lines.
To ﬁx notation, let
 j = ∑

i≥0 ai(j) 2
i with ai(j) ∈ {0, 1} (1)

be the binary expansion of j ∈ N0, let

s(j) = ∑

i≥0 ai(j) (2)

be the number of digits ‘1’ in the binary expansion of j, and let

S(n) =
 n−1∑

j=0 s(j), (3)

S(n; t) =
 n−1∑

j=0 exp(t · s(j)) for t ∈ R and (4)

Sk(n) =
 n−1∑

j=0 s(j)
k for k ∈ N (5)

denote the digital sum in question as well as its so-called exponential and power
sums. Then the Trollope-Delange formula for S(n) is

1
n S(n) = 1
2 log2 n + 1
2 ̃F (log2 n) (6)

where the 1-periodic function ̃F is given by

̃F (u) = 1 − u − 2
1−u T ( 1
21−u
 ) for 0 ≤ u ≤ 1. (7)

Here, T is the Takagi function

T (x) =
 ∞∑

n=0
 1
2n d(2
nx) with d(x) = dist(x, Z) and x ∈ R. (8)

While this is the “direct” deﬁnition of the Takagi function, T can just as well be
deﬁned “indirectly” on [0, 1] as the only continuous solution of the system of two
functional equations

f ( x
2
 ) = 1
2 f (x) + x
2 , f ( x + 1
2
 ) = 1
2 f (x) + 1 − x
2 for x ∈ [0, 1]. (9)

INTEGERS: 11 (2011) 3

The system (9) is a speciﬁc example of the type of functional equations which, as
mentioned above, appear in the digital sum sequences and can therefore be used to
prove the Trollope-Delange formula. Thus, we will in Section 2 of this note review
some basic properties of these functional equations, before we use them in Section 3
to give a simple proof of the Trollope-Delange formula. This proof establishes and
then exploits a series of simple identities for the sequence S(n) which will turn out to
be equivalent to the functional equations (9). In Section 4 we use similar methods to
derive a representation for S(n; t) in an analogous manner. The representation itself
is known; its derivation is new. In Section 5 we note that S(n; t) is the exponential
generating function for the quantities Sk(n), so that generating function techniques
can be used to extract information about the Sk(n) from the representation for
S(n; t). Finally, in Section 6, we will use the same techniques to derive analogous
formulas for the number of zeros in the binary expansions of the integers. The
continuous functions appearing in all of these representations will always be given
as solutions of functional equations of the same type as (9); this representation
is explicit in the sense that these solutions can be computed explicitly from the
functional equations.
All of these digital sums have been considered before, and representations for
them have been given. Beyond the classical papers by Trollope and Delange, some
newer examples are [3], [5], [13], [14], [11], [9] and [10]. In [9], the idea to use
functional equations of type (9) to treat the digital sums is put forward, and in
[10], this idea is explored to the fullest. The present paper has the same focus and
scope as [10]; the methods however are diﬀerent. In [10] as in all of the previous
work, the functions appearing in the representations are taken as a given, and the
representations are then proved from properties of these functions. Here, we go the
other way round: we start with the sequences themselves, discover the functional
equations within these sequences and then identify the functions from the functional
equations. This is therefore a direct way of deriving Trollope-Delange type formulas.

2. Functional Equations

Before proving representations for the digital sums, some basic facts about the
functional equations used in the representations must be recounted.
Let g0, g1 : [0, 1] → R be given perturbation functions, and let |a0| , |a1| < 1. We
consider the system of two functional equations on [0, 1],

f ( x
2
 ) = a0f (x) + g0(x), (10)

f ( x + 1
2
 ) = a1f (x) + g1(x), (11)

where f is an unknown function satisfying these equations for all x ∈ [0, 1].

INTEGERS: 11 (2011) 4

It is clear that if such a function f exists, then it must satisfy f (0) = g0(0)/(1−a0)
(put x = 0 into (10)) and f (1) = g1(1)/(1 − a1) (put x = 1 into (11)). Moreover,
by putting x = 1 into (10) and x = 0 into (11), it follows that f ( 1
2 ) must equal the
two expressions
 a0 g1(1)
1 − a1 + g0(1) = a1 g0(0)
1 − a0 + g1(0). (12)

This is only possible if the two expressions are equal themselves. Thus, (12) is a
nessecary condition for the existence of a solution f .
It is also suﬃcient. Assume that g0, g1 are continuous and that (12) holds. Then
it can be proved as an easy application of Banach’s ﬁxed point theorem that there
exists a unique continuous solution f of (10),(11) on [0, 1]. (The earliest proof of
this was given in much more generality by M.F. Barnsley in connection with his
fractal interpolation functions, [2].)
If (12) holds, then any solution f is uniquely determined on the dyadic rationals
i/2
n, n ∈ N0, i = 0, . . . , 2
n. In fact, we have already seen above that (10),(11) ﬁx
the values f (0), f (1) and f ( 1
2 )
. This process can be continued. If, for n ∈ N, the
values f ( 2i+1
2n ) (i = 0, . . . , 2
n−1 − 1) are already known, then the values f ( 2i+1
2n+1 )

can be computed from (10), and the values f ( 2i+1+2
n
2n+1 ) can be computed from (11).
This covers all the dyadic rationals, and since they are dense in [0, 1], the functional
equations in this sense allow the explicit computation of their continuous solution.
These functional equations have been discussed in a diﬀerent context in [6],[7].
They were used there to characterize classes of nowhere diﬀerentiable functions as
solutions of these functional equations, and then to prove the non-diﬀerentiability
of the solutions directly from the functional equations. This applies to a large
variety of nowhere diﬀerentiable functions which previously had been investigated
separately; among them are the Takagi functions as well as the famous Weierstraß
functions C(x) = ∑∞
n=0 a
n cos(2
n · 2πx), which satisfy (10), (11) with a0, a1 = a,
g0(x) = cos(πx), g1(x) = − cos(πx).

3. The Trollope-Delange Formula

First, we need a simple lemma which connects functions deﬁned on the integers
with functions deﬁned on the dyadic rationals. As a basic notation for the rest of
this note, set p(n) = 2
[log2 n] for n ∈ N (13)

where [u] is the largest integer less than or equal to u. In other words, p(n) is the
largest power of 2 less than or equal to n. We always have

p(n) ≤ n < 2p(n). (14)

INTEGERS: 11 (2011) 5

The identities
 p(2n) = 2p(n), (15)

p(n + p(n)) = 2p(n), (16)

p(n + 2p(n)) = 2p(n) (17)

are simple but will be important throughout the rest of this note.

Lemma 1. Let G : N → R be a function on the integers. For n ∈ N, set

x := n − p(n)
p(n) ∈ [0, 1) and F (x) = F ( n − p(n)
p(n)
 ) := G(n). (18)

Then F is a well-deﬁned function on the dyadic rationals in [0, 1) if and only if
G(2n) = G(n) for all n ∈ N.

Proof. Note that when n ranges through all integers, then n−p(n)
p(n) ranges through
all dyadic rationals in [0, 1). Every dyadic rational is hit inﬁnitely often. Thus,
F is well-deﬁned if and only if G(n1) = G(n2) for all n1, n2 ∈ N with n1−p(n1)
p(n1) =

n2−p(n2)
p(n2) .
This last equality implies p (n2) n1 = p (n1) n2. Thus n1 and n2 can only diﬀer by
a factor which is a power of 2. The reverse is also true, so that n1−p(n1)
p(n1) = n2−p(n2)
p(n2)
if and only if n1 = 2
ℓn2 with an ℓ ∈ Z.
Thus, F is well deﬁned if and only if G(n1) = G(n2) for all n1, n2 ∈ N whose
quotient is an integer power of 2. This condition in turn holds if and only if G(n) =
G(2n) for all n ∈ N. !

The Trollope-Delange formula can now be proved as a consequence of a series of
simple identities. First, let p be a power of 2 and note that

s(2j) = s(j) and s(2j + 1) = s(j) + 1 for all j = 0, 1, . . . , (19)

s(j + p) = s(j) + 1 for j = 0, 1, . . . , p − 1, and (20)

s(j + p) = s(j) for j = p, p + 1, . . . , 2p − 1. (21)

Next, note that these identities imply, for all n ∈ N,

S(2n) = 2S(n) + n, (22)

S(n + p(n)) = S(n) + S(p(n)) + p(n) and (23)

S(n + 2p(n)) = S(n) + S(2p(n)) + n. (24)

To derive (22), split the sum for S(2n) into two parts, summing over the even and
the odd integers, and use (19). To derive (23), split the sum for S(n+p(n)) into three
parts starting at 0, p(n) and 2p(n), identify the second part as S(2p(n)) − S(p(n))

INTEGERS: 11 (2011) 6

and use (20) on the third part. To derive (24), split the sum for S(n + 2p(n)) into
two parts starting at 0 and 2p(n), and use (20) (with 2p(n) instead of p) on the
second part.
Now set
 G(n) := 1
p(n)
 (
S(n) − n
p(n) S(p(n))
) . (25)

Then, using formulas (15)–(17) and (22)–(24), it is easy to compute

G(2n) = G(n), (26)

G(n + p(n)) = 1
2 G(n) − n − p(n)
4p(n) and (27)

G(n + 2p(n)) = 1
2 G(n) + n
4p(n) . (28)

If we set x = x(n) := n−p(n)
p(n) , then, using (16) and (17),

x(n)
2 = n − p(n)
2p(n) = n + p(n) − p(n + p(n))
p(n + p(n)) = x(n + p(n)) and (29)

x(n) + 1
2 = n
2p(n) = n + 2p(n) − p(n + 2p(n))
p(n + 2p(n)) = x(n + 2p(n)). (30)

Moreover, by Lemma 1 the function F given by F (x) = F ( n−p(n)
p(n) ) := G(n) is
well-deﬁned on the dyadic rationals in [0, 1) and by (27),(28) satisﬁes

F ( x
2
 ) = G(n + p(n)) = 1
2 G(n) − n − p(n)
4p(n) = 1
2 F (x) − x
4 and (31)

F ( x + 1
2
 ) = G(n + 2p(n)) = 1
2 G(n) + n
4p(n) = 1
2 F (x) + x + 1
4 . (32)

This means that F satisﬁes the system (10),(11) with a0 = a1 = 1
2 , g0(x) = − x
4
and g1(x) = x+1
4 . Since condition (12) is satisﬁed (with F (0) = 0, F (1) = 1 and
F ( 1
2 ) = 1
4 ), it follows that F is the restriction to the dyadic rationals of a continuous
function on [0, 1] (also denoted by F ), which is a solution of (10),(11) on [0, 1].
By solving (25) for S(n), we get a representation for S(n) involving G(n) and
S(p(n)). The latter quantity can be given explicitly: Since p(n) is a power of 2, the
binary expansion of the p(n) numbers between 0 and p(n) − 1 can be thought of as
being ‘0’-‘1’-strings, each of length log2 p(n) and precisely half of whose digits are
‘1’s. Therefore S(p(n)) = 1
2 p(n) log2 p(n). (33)

From this we get the representation

S(n) = n
p(n) S(p(n)) + p(n)G(n) = n log2 p(n)
2 + p(n) F ( n − p(n)
p(n)
 ) , (34)

INTEGERS: 11 (2011) 7

and this (via p(n) = n/(x + 1)) is equivalent to

1
n S(n) = log2 n
2 − log2(x + 1)
2 + 1
x + 1 F (x) where x = n − p(n)
p(n) (35)

and where F is the countinuous function on [0, 1] which is given by the system
(31),(32). This is the Trollope-Delange formula.
It is, however, given in a form slightly diﬀerent from (6),(7). The equivalence of
the two forms can be seen quickly by noting that

F (x) = x − 1
2 T (x) = x + 1
2 − T ( x + 1
2
 ) . (36)

The ﬁrst equality in (36) follows because F (x) and x − 1
2 T (x) satisfy the same
system of type (10),(11), and the second equality follows by applying the second
equation of (9). Now set u equal to the fractional part of log2 n, i.e., u := {log2 n},
and note that x = 2
u − 1 (resp. u = log2(x + 1)) to arrive at (6),(7).
The core of the proof of the Trollope-Delange formula presented here consists
of deriving identities for S(n + p(n)) and S(n + 2p(n)), (23) and (24). With these
two identities (and the value S(1) = 1), the whole sequence S(n) is determined
without it ever being necessary to compute a single value of s(n). The Trollope-
Delange formula follows because (23) and (24) determine the sequence S(n) in the
same way as the functional equations (10) and (11) allow the computation of their
continuous solution; both perspectives are in fact equivalent by (29) and (30). This
also explains the approximation process which is visible in Figure 1 of [5].
Of course, identities for S(2n) and S(2n+1) would similarly determine the whole
sequence S(n). An identity for S(2n) is given above in (22), and for S(2n + 1) it
can be proved in a similar fashion that

S(2n + 1) = 2S(n) + n + s(n). (37)

This means that although (22) and (37) also determine the whole sequence S(n),
they only do so after computing the values s(n). In this sense, (23) and (24) are
“simpler” or “more natural” than (22) and (37).
Also, note that the proof presented here does not require any advance knowledge
of the main term log2 n
2 . This term (in the form log2 p(n)
2 ) arises in the computations
in a natural way, where it comes from the term S(p(n)). One might say that the
values S(p), where p is a power of 2, act as “stepping stones” for the complete
sequence S(n). We will see such a behavior again for the other types of digital sums
considered below.

INTEGERS: 11 (2011) 8

4. Exponential Sums

An explicit formula for the exponential sums S(n; t) has been derived in [14] and
(by diﬀerent methods) in [10]; in our notation it is given in formula (50), below.
This representation involves the so-called de Rham (sometimes Lebesgue) singular
function La(x). It can be deﬁned as the continuous solution of the system

f ( x
2
 ) = a f (x) and f ( x + 1
2
 ) = (1 − a) f (x) + a (38)

on [0, 1] for ﬁxed a ∈ (0, 1). This function was ﬁrst constructed by R. Salem in [16]
as a simple example of a singular function (it is strictly monotone and for a ̸= 1
2 has
derivative 0 almost everywhere). In [15], G. de Rham used the functional equations
(38) to characterize La(x) and to prove its singularity.
The goal now is to give another proof of the representation from [14] and [10],
using the method developed in the previous section, i.e., by deriving analogs for
the formulas (23)–(35). In particular, we do not have to know in advance that the
function La(x) will appear in the representation.
We get, using (19)–(21) in the same way as before,

S(2n; t) = (
e
t + 1
) S(n; t), (39)

S(n + p(n); t) = S(n; t) + e
t S(p(n); t) and (40)

S(n + 2p(n); t) = e
t S(n; t) + S(2p(n); t). (41)

Now set
 G(n; t) := S(n; t)
S(p(n); t) . (42)

Then it follows that
 G(2n; t) = G(n; t), (43)

G(n + p(n); t) = 1
et + 1 G(n; t) + e
t

et + 1 and (44)

G(n + 2p(n); t) = e
t

et + 1 G(n; t) + 1. (45)

Thus the function x ↦→ F (x; t) given by F (x; t) = F ( n−p(n)
p(n) ; t
) := G(n; t) is
well-deﬁned on the dyadic rationals in [0, 1) and by (44),(45) satisﬁes

F ( x
2 ; t
) = 1
et + 1 F (x; t) + e
t

et + 1 and (46)

F ( x + 1
2 ; t
) = e
t

et + 1 F (x; t) + 1. (47)

INTEGERS: 11 (2011) 9

Since e
t > 0, we have 1
et+1 < 1 and e
t
et+1 < 1. Moreover, condition (12) is
satisﬁed with
 F (0; t) = 1, F (1; t) = e
t + 1 and F ( 1
2 ; t
) = 2e
t + 1
et + 1 . (48)

Therefore F (x, t) is a continuous function in x.
Again, S(p(n); t) can be computed explicitly; the easiest way would be to iterate
formula (39) to get S(p(n); t) = (e
t + 1)
log2 p(n). (49)

Altogether, we get

S(n; t) = (e
t + 1)
log2 p(n) · F ( n − p(n)
p(n) ; t
) = (e
t + 1)
log2 n · (e
t + 1)
− log2(x+1)F (x; t)

(50)
where x = n−p(n)
p(n) . If we let

̃F (x; t) := (e
t + 1)
− log2(x+1)F (x; t), (51)

then ̃F satisﬁes ̃F (0; t) = ̃F (1; t) = 1 for every t ∈ R, so that for every t, ̃F (·; t) can
be continued to a continuous, 1-periodic function on R. Thus (50) is the exponential
analog of the Trollope-Delange formula.
Now, the function F (x; t) appearing in (50) is just a rescaled and re-parametrized
version of de Rham’s singular function La(x). Explicitly, we have

F (x; t) = 1 + e
t L 1
1+et (x), (52)

because both sides of this identity satisfy the same functional equations of
type (10),(11).

5. Power Sums

Now set S0(n) := n and consider the power sums Sk(n). The ﬁrst explicit represen-
tation for Sk(n) was given by J. Coquet in [3]. He proved that there exist 1-periodic
functions Gk,ℓ such that

1
n Sk(n) = ( log2 n
2
 )k +
 k−1∑

ℓ=0(log2 n)
ℓGk,ℓ(log2 n) (53)

holds; he also found certain recurrence relations between the functions Gk,ℓ. In [13],
a more explicit representation for the functions Gk,ℓ was given and their continuity
was proved. In [10], a still more explicit representation for the Gk,ℓ was given.

INTEGERS: 11 (2011) 10

The basic building block in the latter two papers is de Rham’s function La(x);
the functions Gk,ℓ are then given as certain combinations of the partial derivatives
(with respect to a) of La(x). These partial derivatives appear in the representations
because
 Sk(n) = ∂k

∂tk S(n; t)
∣
∣
∣
∣
t=0 , (54)

and S(n; t) is related to La(x) via F (x; t) and (52). This fact is noted and made
good use of in [14] and [10].
In the present note, we will also use (54) as a starting point, but we will then
follow a line of argument diﬀerent from that given in [14] and [10]. It will lead us to
a representation which is diﬀerent from (although of course equivalent to) Coquet’s
(53) in that it uses diﬀerent, maybe slightly simpler, building blocks. These building
blocks appear in the course of the argument in a natural way; prior knowledge of
them is not necessary.
This argument uses the method of (exponential) generating functions. In fact,
(54) directly translates into
 S(n; t) =
 ∞∑

k=0
 Sk(n)
k! t
k, (55)

so that all information about Sk(n) is already contained in S(n; t) and can be
extracted by expanding the result (50) of the previous section into a power series
and comparing coeﬃcients. Note that for every n ∈ N the sum (55) has an inﬁnite
radius of convergence, because Sk(n) ≤ n
k+1.
Before beginning with the actual argument, we need a few preparations. In
general, if c = (ck) is an arbitrary sequence, then its exponential generating function
is
 C(t) =
 ∞∑

k=0
 ck
k! t
k. (56)

For later reference, note the formula for the Cauchy product of exponential gener-
ating functions: If C1 and C2 are the exponential generating functions of (c1,k) and
(c2,k), then the exponential generating function of C1 · C2 is

C1(t) · C2(t) =
 ∞∑

k=0
 c3,k
k! t
k where c3,k =
 k∑

ν=0
 (k
ν
)
c1,ν c2,k−ν. (57)

To ﬁnish the preparations, set the auxiliary function D(t) (which appears in (50))
equal to
 D(t) := 1
1 + et (58)

INTEGERS: 11 (2011) 11

and expand D(t)
−u into an exponential series,

D(t)
−u = (1 + e
t)
u =
 ∞∑

k=0
 d(k; u)
k! t
k (59)

where
 d(k; u) = ∂k

∂tk (1 + e
t)
u∣
∣
∣
∣
t=0 (60)

and with radius of convergence at least π. From (60) we get the recursion

d(0; u) = 2
u and d(k + 1; u) = u d(k; u) − u d(k; u − 1), (61)

so that (inductively) d(k; u) = 2
u−k qk(u) where qk is a polynomial of degree k and
leading coeﬃcient 1, satisfying the recursion

q0(u) = 1 and qk+1(u) = u (2qk(u) − qk(u − 1)) for k ≥ 0. (62)

We will also need the particular values dk := d(k; −1); since

D(t)
1 = 1
1 + et = 1
2
 (
1 − tanh ( t
2
 )) , (63)

they have the explicit representation

dk = − 2
k+1 − 1
k + 1 Bk+1, (64)

where the numbers Bk are the Bernoulli numbers.
Now the result (50) of the previous section reads,

S(n; t) = D(t)
− log2 p(n) · F (x; t) = D(t)
− log2 n · D(t)
log2(x+1)F (x; t) (65)

where, by (46),(47), the function F (x; t) satisﬁes, for every t, the system of func-
tional equations

F ( x
2 ; t
) = D(t)F (x; t)+1−D(t) and F ( x + 1
2 ; t
) = (1−D(t))F (x; t)+1. (66)

Note here that if x ∈ [0, 1) is a dyadic rational, then by induction F (x; t) is a
polynomial in D(t), so that the series for F (x; t) has radius of convergence at least π.
Moreover, it follows from results in [8] that for every x ∈ [0, 1], F (x; t) is analytic
around t = 0.
Thus writing
 F (x; t) =
 ∞∑

k=0
 Fk(x)
k! t
k, (67)

INTEGERS: 11 (2011) 12

(66) implies by (57) that, for k ≥ 0, Fk(x) is a solution of

Fk ( x
2
 ) = 1
2 Fk(x) + δk,0 − dk +
 k−1∑

ν=0
 (k
ν
)
dk−ν Fν(x), (68)

Fk
 ( x + 1
2
 ) = 1
2 Fk(x) + δk,0 −
 k−1∑

ν=0
 (k
ν
)
dk−ν Fν(x). (69)

Here, δk,ℓ is the Kronecker symbol which equals 1 if k = ℓ and 0 otherwise.
This is a recursive deﬁnition of the functions Fk: If the solutions Fν of the
functional equations are known for ν = 0, . . . , k − 1, then these solutions enter the
functional equations for Fk as perturbation functions. Also, the solution for k = 0
is F0(x) = x + 1. It can be seen recursively that condition (12) is satisﬁed (with,
for k ≥ 1, Fk(0) = 0, Fk(1) = 1 and Fk( 1
2 ) = −dk), so that each Fk is a continuous
function on [0, 1]. At the end of this section, we will say more about these functions.
Now, Sk(n) can be given explicitly in terms of the continuous functions Fk and
the polynomials qk. One just has to convert (65) via (57) into its exponential series
and compare coeﬃcients on both sides.
Writing
 D(t)
log2(x+1)F (x; t) =
 ∞∑

k=0
 fk(x)
k! t
k, (70)

we have
 fk(x) = 1
x + 1
 k∑

µ=0
 (k
µ

)
2
−µqµ(− log2(x + 1)) · Fk−µ(x). (71)

Note here that the function t ↦→ D(t)
log2(x+1)F (x; t) is, for x = 0 and x = 1,
identical to 1 (use (48) and (58)). Therefore, fk(0) = fk(1) = δk,0 for all k, and the
continuous function fk can be continuously extended to a 1-periodic function on R.
Next from (65) we get, expanding D(t)
− log2 n · D(t)
log2(x+1)F (x; t) via (57),

Sk(n) =
 k∑

ν=0
 (k
ν
)
n 2
−ν qν(log2 n) · fk−ν(x). (72)

Note here that, if the right-hand side of (72) is sorted by powers of log2 n, then each
of these powers gets a factor which is a linear combination of the functions fk, i.e.,
a continuous function in x which can be continued 1-periodically to a continuous
function on R.
Now putting everything together, we get the following analog of the Trollope-
Delange formula for power sums.

Theorem 2. Fix k ≥ 0. Then for every n ≥ 0 the identity

1
n Sk(n) = 1
x + 1
 ∑

ν+µ+λ=k
 k!
ν! µ! λ! 2
−ν−µ qν(log2 n) qµ(− log2(x + 1)) Fλ(x) (73)

INTEGERS: 11 (2011) 13

holds, where x = n−p(n)
p(n) , where the polynomials qk are given by the recursion (62),
and where the functions Fk are the uniquely determined continuous solutions on
[0, 1] of the (recursive) system (68),(69).
In this representation, every power of log2 n is multiplied by some continuous
function in x which can be extended to a continuous, 1-periodic function on R. The

main term is ( log2 n
2 )k.

For k = 0, we get S0(n) = n; for k = 1, we recover the original Trollope-Delange
formula in the form (35). For k = 2, we get

1
n S2(n) = 1
4 (log2 n)
2 + ( 1
4 − 1
2 log2(x + 1) + 1
x + 1 F1(x)
) log2 n

+ 1
4 log2(x + 1)
2 − 1
4 log2(x + 1) − log2(x + 1)
x + 1 F1(x) + 1
x + 1 F2(x).

(74)

The functions Fk are interesting; Figures 1–2 show F1–F4. Of course, F1 is just
the function F appearing in the original Trollope-Delange formula; it is therefore
a relation of the Takagi function T . In fact, all of the functions Fk are linear
combinations of certain functions Tk investigated in [17], [1] and [10]. These are the
partial derivatives of the de Rham function,

Tk(x) = ∂k

∂ak La(x)
∣
∣
∣
∣
a= 1
2 , (75)

that is,
 La(x) =
 ∞∑

k=0
 Tk(x)
k!
 (
a − 1
2
 )k . (76)

It was proved in [1] that the continuous functions Tk are nowhere diﬀerentiable;
pictures of T1–T4 (resp. rescaled versions thereof) can also be found in [17] and [1].
Note that T0(x) = x and T1(x) = 2T (x) where T is the Takagi function. An
alternative recursive deﬁnition of the functions Tk by way of functional equations
of type (10),(11) is also given in [1] (in a diﬀerent but equivalent form) and [10],
namely, for k ≥ 1 and x ∈ [0, 1],

Tk ( x
2
 ) = 1
2 Tk(x) + kTk−1(x) and (77)

Tk
 ( x + 1
2
 ) = 1
2 Tk(x) + δk,1 − kTk−1(x). (78)

Since F (x; t) and La(x) are related by (52), we can set a = 1
1+et and then expand
both sides of (52) into a power series around t = 0. Comparing coeﬃcients, we ﬁnd

INTEGERS: 11 (2011) 14

that Fk is a linear combination of T0, . . . , Tk, namely

Fk(x) =
 k∑

m=0
 rk,m
m! Tm(x) for k ≥ 1, (79)

where the coeﬃcients rk,m come from the power series

e
t ( 1
1 + et − 1
2
 )m =
 ∞∑

k=0
 rk,m
k! t
k. (80)

From this, an explicit representation for the rk,m can be worked out, namely

rk,m = (
− 1
2
 )m k∑

ν=0
 (k
ν
) 1
2ν
 m∑

µ=0
 (
m
µ
 )
qν(−µ) (−1)
µ . (81)

Alternatively, the rk,m can also be computed recursively, as again follows from (80):

rk,0 = 1 for k ≥ 0, r0,1 = 0 and rk,1 = −dk − 1
2 for k ≥ 1 and (82)

rk,m =
 k−1∑

ν=m−1
 (k
ν
)
rν,m−1dk−ν for m ≥ 2. (83)

Explicitly, we have

F1(x) = T0(x) − 1
4 T1(x), F2(x) = T0(x) − 1
2 T1(x) + 1
16 T2(x), (84)

F3(x) = T0(x) − 5
8 T1(x) + 3
16 T2(x) − 1
64 T3(x), (85)

and so on.

6. The Number of Zeros

For comparison with the results in the previous section, we now give analogous
representations for the exponential and power sums of the number of digits ‘0’ in
the binary expansions of the integers. Since the computations run along the same
lines as those in the previous sections, they will be omitted here.
Denote
 s
(0)(j) :=
 log2 p(j)∑

i=0 δai(j),0 for j ≥ 1 and s
(0)(0) := −1, (86)

S(0)(n; t) =
 n−1∑

j=0 exp(t · s
(0)(j)) for t ∈ R and (87)

S(0)
k (n) =
 n−1∑

j=0 s
(0)(j)
k for k ∈ N. (88)

INTEGERS: 11 (2011) 15

Setting s
(0)(0) = −1 in (86) has the eﬀect of simplifying the formulas greatly.
(For example, in our notation, the analog of formula (39) is again, S(0)(2n; t) =
(e
t + 1) S(0)(n; t), while, without that normalization, we would get an extra sum-
mand of 1 − e
t.) Note, however, that this leads to values which may take some
getting used to, such as

S(0)
1 (1) = −1, S(0)
1 (2) = −1, S(0)
1 (3) = 0, S(0)
1 (4) = 0, (89)

and so on.
Deﬁne the function F (0)(x; t) as the continuous solution of the system

F (0) ( x
2 ; t
) = (1 − D(t)) F (0)(x; t) + D(t) and (90)

F (0) ( x + 1
2 ; t
) = D(t) F (0)(x; t) + e
t. (91)

This function is continuous in x since condition (12) is satisﬁed with

F (0)(0; t) = 1, F (0)(1; t) = e
t + 1 and F (0) ( 1
2 ; t
) = e
2t + e
t + 1
et + 1 . (92)

It is in fact just a rescaled and re-parametrized version of the function F (x; t) =:
F (1)(x; t) from Section 4:

F (0)(x; t) = e
2t F (1)(x; −t) + 1 − e
2t. (93)

Now the Trollope-Delange formula for S(0)(n; t) is

S(0)(n; t) = e
−tD(t)
− log2 p(n) · F (0)(x; t) = e
−tD(t)
− log2 n · D(t)
log2(x+1) · F (0)(x; t)
(94)
with x = n−p(n)
p(n) .

For the power sums, deﬁne for k ≥ 0 the function F (0)
k (x) as the continuous
solution of
 F (0)
k ( x
2
 ) = 1
2 F (0)
k (x) + dk −
 k−1∑

ν=0
 (k
ν
)
dk−ν F (0)
ν (x), (95)

F (0)
k
 ( x + 1
2
 ) = 1
2 F (0)
k (x) + 1 +
 k−1∑

ν=0
 (k
ν
)
dk−ν F (0)
ν (x). (96)

Again, for k = 0 the solution is F (0)
0 (x) = x + 1, and for k ≥ 1 we get F (0)
k (0) = 0,
F (0)
k (1) = 1 and F (0)
k ( 1
2 ) = 1 + dk. Condition (12) is satisﬁed, so that all of these
functions are continuous.
Now deﬁne a sequence (q(0)
k ) of polynomials of degree k and with leading coeﬃ-
cient 1 by

q(0)
0 (u) = 1 and q(0)
k+1(u) = 2 (u − 1) q(0)
k (u) − u q(0)
k (u − 1) for k ≥ 0. (97)

INTEGERS: 11 (2011) 16

If we write q(1)
k (u) := qk(u) for the polynomials from the previous section, then we
get the following Trollope-Delange analog for the power sums of the zero-counting
function:

1
n S(0)
k (n) = 1
x + 1
 ∑

ν+µ+λ=k
 k!
ν! µ! λ! 2
−ν−µ q(0)
ν (log2 n) q(1)
µ (− log2(x + 1)) F (0)
λ (x)

(98)
where x = n−p(n)
p(n) .
In particular, for k = 1, we get

1
n S(0)
1 (n) = 1
2 log2 n − 1 − 1
2 log2(x + 1) + F (0)
1 (x)
x + 1 , (99)

which is also, in a slightly diﬀerent form, one of the results in [9]. Note that

F (0)
1 (x) = x + 1
2 T (x), (100)

because both sides of the equality are continuous functions which satisfy the same
system of functional equations.
For k = 2, we get

1
n S(0)
2 (n) = 1
4 (log2 n)
2 +
 (

− 3
4 − 1
2 log2(x + 1) + F (0)
1 (x)
x + 1
 )
 log2 n + 1
4 log2(x + 1)
2

+ 1 + 3
4 log2(x + 1) − (log2(x + 1) + 2)
x + 1 F (0)
1 (x) + 1
x + 1 F (0)
2 (x).
 (101)

Some papers dealing with the number of occurrences of “words” (‘0’-‘1’-strings
longer than just one letter) in the binary expansions of the integers distinguish
between the number of occurrences “with overhang” and those “without overhang”.
Examples are [5], [12] or [11]. The quantity S(0)(n; t) computed in this section would
correspond to the formulas “without overhang”. The corresponding quantity “with
overhang” could be deﬁned as

s
(0)
n (j) :=
 log2 p(n)∑

i=0 δai(j),0 for j ≥ 0, n ≥ 1, (102)

̃S(0)(n; t) :=
 n−1∑

j=0 exp(t · s
(0)
n (j)) for t ∈ R, n ≥ 1. (103)

It is, however, easy to see that

̃S(0)(n; t) = S(0)(n; t) + (
e
t + e
−t) (
1 + e
t)log2 p(n) , (104)

so that there is no real diﬀerence between the two quantities in this case.

INTEGERS: 11 (2011) 17

References

[1] Allaart, P.C., Kawamura, K.: Extreme values of some continuous nowhere diﬀerentiable
functions, Math. Proc. Camb. Philos. Soc. 140 (2006), 269–295.

[2] Barnsley, M.F.: Fractal functions and interpolation, Constr. Approx. 2 (1986), 303–329.

[3] Coquet, J.: Power sums of digital sums, J. Number Theory 22 (1986), 161–176.

[4] Delange, H.: Sur la fonction sommatoire de la fonction “somme des chiﬀres,” Enseign. Math.
(2) 21 (1975), 31–47.

[5] Flajolet, P., Grabner, P., Kirschenhofer, P., Prodinger, H., Tichy, R.F.: Mellin transforms
and asymptotics: digital sums, Theoret. Comput. Sci. 123 (1994), 291–314.

[6] Girgensohn, R.: Functional equations and nowhere diﬀerentiable functions, Aeq. Math. 46
(1993), 243–256.

[7] Girgensohn, R.: Nowhere diﬀerentiable solutions of a system of functional equations, Aeq.
Math. 47 (1994), 89–99.

[8] Hata, M., Yamaguti, M.: The Takagi function and its generalization, Japan J. Appl. Math. 1
(1984), 183–199.

[9] Kr¨uppel, M.: Takagi’s continuous nowhere diﬀerentiable function and binary digital sums,
Rostock. Math. Kolloq. 63 (2008), 37–54.

[10] Kr¨uppel, M.: De Rham’s singular function, its partial derivatives with respect to the param-
eter and binary digital sums, Rostock. Math. Kolloq. 64 (2009), 57–74.

[11] Kobayashi, Z., Kuzumaki, T., Okada, T., Sekiguchi, T., Shiota, Y.: A probability measure
which has Markov property, Acta Math. Hungar. 121 (2008), 45–71.

[12] Muramoto, K., Okada, T., Sekiguchi, T., Shiota, Y.: An explicit formula of subblock occur-
rences for the p-adic expansion, Interdisciplinary Information Science 8 (2002), 115–121.

[13] Okada, T., Sekiguchi, T., Shiota, Y.: Applications of binomial measures to power sums of
digital sums, J. Number Theory 52 (1995), 256–266.

[14] Okada, T., Sekiguchi, T., Shiota, Y.: An explicit formula of the exponential sums of digital
sums, Japan J. Indust. Appl. Math. 12 (1995), 425–438.

[15] de Rham, G.: Sur certaines ´equations fonctionelles, ´Ecole Polytechnique de l’Universit´e de
Lausanne, Ouvrage publi´e `a l’occasion de son centenaire (1953), 95–97.

[16] Salem, R.: On some singular monotonic functions which are strictly increasing, Trans. Amer.
Math. Soc. 53 (1943), 427–439.

[17] Sekiguchi, T., Shiota, Y.: A generalization of Hata-Yamaguti’s results on the Takagi function,
Japan J. Indust. Appl. Math. 8 (1991), 203–219.

[18] Takagi, T.: A simple example of the continuous function without derivative, Proc. Phys.
Math. Soc. Japan 1 (1903), 176–177.

[19] Trollope, E.: An explicit expression for binary digital sums, Math. Mag. 41 (1968), 21–25.

INTEGERS: 11 (2011) 18

Figure 1: The functions F1 (left) and F2 (right).

Figure 2: The functions F3 (left) and F4 (right).
