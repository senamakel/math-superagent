<!-- source: https://arxiv.org/pdf/1908.03236 | converted from PDF -->

arXiv:1908.03236v2  [math.RA]  12 Aug 2019Gaussian Integers, Rings, Finite Fields,
and the Magic Square of Squares

O. M. Cain
onnomawcain@gmail.com

April 2019

Abstract. We show the 3 × 3 magic square of squares problem equivalent
to solving quartic polynomials with certain factorization constraints over an
abelian extension of the rationals. We analyze a particular case in which said
extension is assumed to be the Gaussian integers resulting a new search method.
Additionally, the magic square of squares is analyzed over ﬁnite ﬁelds and rings
of the form Z/nZ resulting in some conjectures enumerating the rings and ﬁnite
ﬁelds in which a magic square of squares can be constructed. Code is made
available.

1 Background

The construction of a 3 × 3 magic square of squares – sometimes called simply
the magic square of squares problem – is deﬁned to be 9 distinct squared integers
placed in a 3 × 3 grid, 


a2 b2 c2

d
2 e2 f 2

g2 h2 i2
 

 ,

such that the sums of the elements in each row, column, and the two main
diagonals sum to the same total. That is to say for some integer total T we
have a2 + b2 + c2 = d
2 + e2 + f 2 = g2 + h2 + i2 = T,

a2 + d
2 + g2 = b2 + e2 + h2 = c2 + f 2 + i2 = T,

and a2 + e2 + i2 = g2 + e2 + c2 = T.

In total there are eight sums to be satisﬁed. A lot has been written up on this
fabled object [1] but it is currently unknown if any solution exists. Some ’near
misses’ have been found such as the Parker Square [2],



292 12 472

412 372 12

232 412 292


 ,

1

in which seven of the eight sums add to 3051 but the eighth sums to 4107 ̸= 3051.
The Parker Square also unfortunately has two duplicate entries.
The problem has been shown related to congruent numbers, elliptic curves,
and right triangles with rational sides [3] (which isn’t terribly surprising since
each of those are tightly related to the others).

2 The Magic Hourglass of Squares

At simpler – and still unsolved – problem is whether there exists a magic hour-
glass of squares. That is, 7 squared integers,


a2 b2 c2

− e2 −
g2 h2 i2


 ,

satisfying a2 + e2 + i2 = b2 + e2 + h2 = c2 + e2 + g2 = T

and a2 + b2 + c2 = g2 + h2 + i2 = T

for some integer total T . There are two overlapping magic hourglasses of squares
in any magic square of squares. We will warm up by ﬁrst observing

Theorem 2.1: The total of any magic hourglass of squares T is 3 times the
central entry e2.

Proof: Observe by rearranging

3T = (a2 + e2 + i2) + (b2 + e2 + h2) + (c2 + e2 + g2)

= (a2 + b2 + c2) + (e2 + e2 + e2) + (g2 + h2 + i2) = 2T + 3e2.

The Theorem follows immediately man. □
Corollary 2.1: For any magic hourglass of squares, entries as given above, we
have a2 + i2 = b2 + h2 = c2 + g2 = 2e2.

Proof: From Theorem 2.1 we have a2 + e2 + i2 = 3e2 or equivalently a2 + i2 =
2e2. The same follows for the other two sums containing the central entry. □
Solutions to r2 + t2 = 2s2 over the integers have been known for a long time
[4]. Note this is equivalent to an arithmetic progression of 3 squares since
r2 − s2 = s2 − t2. Speciﬁcally

Theorem 2.2: For every integer solution to r2 + t2 = 2s2 there exist 3 in-
teger parameters m, n, and k such that

r = k(m2 + 2mn − n2), s = k(m2 + n2), t = k(m2 − 2mn − n2),

2

r2 − s2 = s2 − t2 = 4mn(m + n)(m − n)k2.

Proof: Left undone.

The converse of Theorem 2.2 is also true: any such m, n, and k solve r2 + t2 =
2s2.
The parameter k in is only a scaling factor. It is m and n which are really
“doing the work”. For example, we may pick m = 3 and n = 2 to obtain

172 − 132 = 132 − 72 = 120.

An existing guess-and-check method of hourglass searching makes use of this
fact [1]. The ‘guess’ is made by picking a number expressible as the sum of two
squares in at least 3 ways, say

1105 = 332 + 42 = 322 + 92 = 242 + 232,

and making use of Theorem 2.2 to generate the 3 sums of the hourglass which
include the central entry. In this case we get

3672 + 15192 = 13372 + 8092 = 10572 + 11512 = 2(11052)

and the corresponding hourglass


 3672 13372 11512

− 11052 −
10572 8092 15192




in which the 3 of the 5 sums have the same total. The top and bottom rows are
diﬀerent.

3 Factorization Over the Gaussian Integers

Theorem 2.2 has a nice reinterpretation as

Lemma 3.1: For every integer solution to r2 + t2 = 2s2 there exists a complex
number ω ∈ Z[i, √
k] such that k is an integer and

r = Re[ω2] + Im[ω2], s = ωω, t = Re[ω2] − Im[ω2],

r2 − s2 = s2 − t2 = Im[ω4], and rt = Re[ω4].

Proof: Choose ω = √
k(m+ ni). All but the last equation follow from Theorem
2.2. Noting that Re[xy] = Re[x]Re[y] − Im[x]Im[y], the last equation is derived
easily. □
To simplify notation, we let the function χ take a complex number ω to
(r, s, t) as deﬁned above. Meaning speciﬁcally χ(ω) = (Re[ω2]+Im[ω2], ωω, Re[ω2]−

3

Im[ω2])

Theorem 3.2: A magic hourglass of squares,


a2 b2 c2

− e2 −
g2 h2 i2


 ,

exists if and only if there exists α, β, γ ∈ K = Z[i, √
A, √
B, √
C] with A, B, and
C integers such that

α
4 + β4 + γ4 ∈ Z, α
2, β2, γ2 ∈ Z[i], αα = ββ = γγ,

(a, e, i) = χ(α), (b, e, h) = χ(β), (c, e, g) = χ(γ),

with α
4, β4, and γ4 distinct and strictly complex.

Proof: From Corollary 2.1 note that in any magic hourglass of squares (a2, e2, i2),
(b2, e2, h2), and (c2, e2, g2) each form an arithmetic progression. Applying Lemma
3.1 to each we have α, β, and γ parametrize the 3 progressions respectively –
in the same way that ω parametrized r2, s2, and t2. Note the equivalence of
αα, ββ, and γγ follows from the fact that the 3 progressions have the same
middle element.
By Theorem 2.2 and Lemma 3.1 we see that the sums a2 +e2 +i2, b2 +e2 +h2,
and c2 +e2 +g2 are all equal to 3e2 if and only if we have the former parametriza-
tion by α, β, and γ. Next we must show that a2 + b2 + c2 = 3e2 (the logic for
g2 + h2 + i2 is identical). Rearranging, we have

(a2 − e2) + (b2 − e2) + (c2 − e2) = 0.

By Lemma 3.1 again, we see this is equivalent to Im[α
4] + Im[β4] + Im[γ4] = 0.
Which in turn is equivalent to
 α
4 + β4 + γ4 ∈ Z.

The restriction α
4 ̸∈ Z ensures that a2, e2, and i2 are distinct (an analogous
statement can be said for β and γ). Restricting α
4, β4, and γ4 to be distinct
ensures that the remaining elements of the hourglass are distinct as well.
As for the reverse direction, it can be seen easily from Theorem 2.2 and
Lemma 3.1 that any choice of α, β, γ within the restrictions yields a valid magic
hourglass. □
Observation 3.1: The Galois group of K = Q(i, √
A, √
B, √
C) is a product
of cyclic groups of order 2 and is therefore abelian. It follows (we think?) that
K is a subring of the ring of integers of some cyclotomic ﬁeld extension of the
rationals. That sounds useful but we weren’t able to do anything with it.

4

Observation 3.2: For a full magic square – as opposed to a measly hourglass
– we obtain two inclusions

α
4 + β4 + γ4, α
4 + δ4 − γ4 ∈ Z

where χ(δ) = (d, e, f ) and obeys a similar set of restrictions.

4 Case K = Z[i]

The Gaussian integers Z[i] have unique factorization (see Theorem 6.6 in [6]).
Thus if we take α, β, γ ∈ Z[i] (meaning that the parameter k as it appears in
Lemma 3.1 is 1 for each of α, β, and γ) then by

αα = ββ = γγ (1)

from Theorem 3.2, we see that α, β, and γ have the same prime factorization
up to conjugation of factors. This allows for some interesting formulations such
as

Theorem 4.1: If there exists x, y, z ∈ Z[i] such that

Im[x
4y4z4] = −4Im[x
4]Im[y4]Im[z4]

and x
4, y4, and z4 are both strictly complex and not real multiples of each other
then there exists a magic hourglass of squares.

Proof: Choose α = xyz, β = xyz, and γ = xyz.

It follows immediately that αα = ββ = γγ and trivially that α
2, β2, γ2 ∈ Z[i].
To see that α
4 + β4 + γ4 is real we must ﬁrst note the identity

Im[XY Z] =

Re[X]Re[Y ]Im[Z] + Re[X]Im[Y ]Re[Z] + Im[X]Re[Y ]Re[Z] − Im[X]Im[Y ]Im[Z].

From this one derives

Im[x
4y4z4] + 4Im[x
4]Im[y4]Im[z4] = Im[x4y4z4] + Im[x
4y4z4] + Im[x
4y4z4]

= Im[α
4] + Im[β4] + Im[γ4]

to see that Im[α
4 + β4 + γ4] = 0.
To see that none of α
4, β4, or γ4 is real, suppose that one of them, say α
4,
is. Then necessarily Im[β4] = −Im[γ4]. Along with ββ = γγ, this implies that
γ4 = β4 or equivalently γ2 = ±β2. But if so then β2γ2 = ±x
4(yy)
2(zz)
2 is real
implying in turn that x
4 is real; a contradiction.
Lastly, to see that α
4, β4, and γ4 are distinct suppose that two are not, say
α
4 = β4. It follows that α
2 = ±β2 and therefore that x
2y2 = ±x
2y2. Scaling

5

both sides by x
2y2 we obtain |x|4y4 = ±x
4|y|4 which implies that x
4 and y4 are
real multiples of each other; a contradiction. □
It’s not clear whether the converse of Theorem 4.1 is true. But a slightly weaker
statement can be obtained replacing x
4, y4, and z4 with x
2, y2, and z2 respec-
tively.

Theorem 4.2: If there exists a magic hourglass of squares, then there exists
x, y, z ∈ Z such that
 Im[x
2y2z2] = −4Im[x
2]Im[y2]Im[z2]

and x
2, y2, and z2 are both strictly real and not real multiples of each other.

Proof: Left undone.

Observation 4.1: Theorem 4.1 can be used to search for magic hourglasses.
It’s known that for any Gaussian integer ω = m + ni the value Im[ω4] =
4mn(m + n)(m − n) is always divisible by 24 [4]. Thus 4Im[x
4]Im[y4]Im[z4]
is divisible by 4 · 243. One may then iterate over integers A and B assigning
xyz = 27A + 32B (which will necessarily satisfy the former divisibility con-
straint) and then check for each possible factorization, x, y, and z, whether the
constraint of Theorem 4.1 is also satisﬁed. It’s not clear if there’s a system-
atic way to choose integers A and B so that xyz is easy to factor or – perhaps
alternatively – has many factorizations.

5 The Smallest Non-Parker Finite Field

At this point we move on from the traditional magic square of squares problem.
Speciﬁcally, we will attempt to ﬁnd solutions over elements of ﬁnite ﬁelds instead
of over the integers. We call a ﬁnite ﬁeld – or ring in general – Parker if
no magic square of square can be formed; that is, if no nine distinct squared
elements can be found satisfying the constraints given in the Section 1. If a
traditional magic square of squares does not exist, then Z is Parker. It is hoped
that by enumerating which ﬁnite ﬁelds and rings are Parker, it may become
clear whether Z is Parker.
The ﬁeld F29, for example, is not Parker since

92 112 12

62 02 142

122 162 82

is a valid magic square of squares evaluated mod 29.
As a guiding inquiry, we ask what is the non-Parker ﬁnite ﬁeld of smallest
order? We have seen already that F29 is non-Parker, so there are only ﬁnitely
many ﬁelds left to check. Remember that for any prime, p, or prime power,

6

pr, there exists a ﬁnite ﬁeld – isomorphically unique – having that order (see
Theorem 15.7.3 in [7]).
The ﬁnite ﬁelds with orders less than 29 are

F2, F3, F4, F5, F7, F8, F9, F11, F13, F16, F17, F19, F23, F25, and F27.

One could quickly check which of these, if any, are Parker with symbolic compu-
tation. We will however proceed by whittling down this list, lemma by lemma,
in the hope of also getting a better sense of the structure of magic squares of
squares. If any reader would like a more rigorous treatement of the cases Fr
2
and Fr
3 than what we can oﬀer, they are referred to [10]. We start with

Lemma 5.1: All 3 × 3 magic squares over ﬁnite ﬁelds of even order have
duplicate entries.

Proof: All ﬁnite ﬁelds can be formed by taking a quotient of a polynomial
ring over a ﬁnite ﬁeld of prime order (see Theorem 15.7.3 of [2]). For example,

F9 ∼= F3[x]/(x
2 + 1).

This means every element of a ﬁeld of even order is a sum of distinct powers of
x. For example, the entries of F8 ∼= F2[x]/(x
3 + x + 1) are

0, 1, x, x + 1, x
2, x
2 + 1, x
2 + x, and x2 + x + 1.

Thus any magic square in F2k can be regarded as a linear combination of magic
squares (added element-wise) over F2 where each such square is scaled by a
power of x. A magic square over F16,

take 1 + x + x3 x + x2 1 + x
2 + x
3

x + x
2 0 x + x
2

1 + x
2 + x
3 x + x2 1 + x + x3 for example,

can be decomposed as an element-wise sum of 4 magic squares over F2,

1 0 1
0 0 0
1 0 1 + x · 1 1 0
1 0 1
0 1 1 + x
2 · 0 1 1
1 0 1
1 1 0 + x
3 · 1 0 1
0 0 0
1 0 1 .

Naturally, we proceed by analyzing magic squares in F2. There are 8:

0 0 0
0 0 0
0 0 0 , 1 1 0
1 0 1
0 1 1 , 0 1 1
1 0 1
1 1 0 , 1 0 1
0 0 0
1 0 1 ,

1 1 1
1 1 1
1 1 1 , 0 0 1
0 1 0
1 0 0 , 1 0 0
0 1 0
0 0 1 , and 0 1 0
1 1 1
0 1 0 .

7

To see that these are the only possible 8, we resort to a previously published
result [8] that any 3 × 3 magic square over the integers can be parametrized by
3 integers, A, B, and C, in the form

A −A A
−A 0 A
0 A −A + 0 −B B
B 0 −B
−B B 0 + C C C
C C C
C C C .

And now we arrive at the important bit. All 8 squares have the same entry
in the edge-middles and in opposite corners. Thus any magic square over a ﬁnite
ﬁeld of even order will have at most 4 distinct entries. □

Corollary 5.1: All ﬁnite ﬁelds of even order are Parker.
Proof: By Lemma 3.1 any 3×3 magic square over a ﬁnite ﬁeld has duplicate
entries. □

Okay. First lemma down. We’ve eliminated F2, F4, F8, and F16 from our
list of candidates leaving

F3, F5, F7, F9, F11, F13, F17, F19, F23, F25, and F27.

The smaller ﬁelds can be eliminated easily.

Lemma 5.2: A ﬁnite ﬁeld of odd order, q, has q+1
2 squares.
Proof: This follows easily from the fact that F×
q is cyclic (for proof of which,
we cite Artin [7] again; Theorem 15.7.3). □

Corollary 5.2: The ﬁelds F3, F5, F7, F9, F11, and F13 are Parker.
Proof: By Lemma 5.2, each of the ﬁelds in question have fewer than 9
distinct squares. Therefore no 3 × 3 magic square of distinct squares can be
formed. □

The remaining candidates are F17, F19, F23, F25, and F27. Tackling these re-
maining ﬁelds will require poking into their structure somewhat deeper (either
that or just performing a computation, but we decided not to take that route).

Lemma 5.3: Any non-Parker ﬁnite ﬁeld contains either 4 distinct solutions
to x
2 + y2 = 0 with x, y ̸= 0 or 4 distinct solutions to x
2 + y2 = 2 with
x
2, y2 ̸= 2.
Proof: By deﬁnition, a non-Parker ﬁeld contains at least one magic square
of distinct squares. We use the standard variables

a2 b2 c2

d
2 e2 f 2

g2 h2 i2 .

8

If e = 0 then there are 4 distinct solutions to x
2 + y2 = 0. If e is nonzero,
we use the fact that all elements in a ﬁeld have inverses (this is one of the
facts that deﬁnes what exactly a “ﬁeld” is). We scale our hypothetical magic
square by (e−1)
2 which produces another magic square of distinct squares. The
new square has a central entry of 1. Thus there are 4 distinct solutions to
x
2 + y2 = 2(12) = 2. □

Corollary 5.3: The ﬁelds F19, F23, and F27 are Parker.
Proof: Let’s count the solutions x
2 +y2 = 0, 2 in each of of the ﬁelds in ques-
tion. This took us roughly 10 minutes per ﬁeld to do by hand (and was, in fact,
further veriﬁed with computation [9]). There are no solutions to x
2 + y2 = 0.
The respective solutions to x
2 + y2 = 2 are

F19 : 22 + 62 = 42 + 92 = 2,

F23 : 02 + 52 = 32 + 42 = 62 + 92 = 2,

and F27 : (x)
2 + (x
2 + 2x)
2 = (x2 + 2)
2 + (x + 2)
2 = (x + 1)
2 + (x2 + x)
2 = 2

where x
3 = x + 2. None of the ﬁelds have 4 distinct solutions and are thus each
Parker by Lemma 5.3. □

We are left with F17 and F25 each having 4 distinct solutions to x
2 + y2 = 0.
But this doesn’t yet ensure F17 and F25 are non-Parker. We need one last
lemma.

Lemma 5.4: Magic squares of distinct squares over a ﬁnite ﬁeld with a central
entry of 0 are parametrized (up to scaling) by solutions to α
2 − β2 = β2 − γ2 = 1
(i.e. three consecutive squares) satisfying {α, β, γ} ∩ {0, 1, −1} = ∅.

Proof: Suppose we have a magic square of squares over a ﬁnite ﬁeld with
a central entry of 0, a2 b2 c2

d
2 0 −d
2

−c2 −b2 −a2 .

Again, we use the fact that all entries have inverses and scale the square by
(c−1)
2. With the right change of variables, we obtain

β2 −α
2 1
−γ2 0 γ2

−1 α
2 −β2 .

This square is manifestly magic if and only if

α
2 − β2 − 1 = β2 − γ2 − 1 = 0.

9

The lemma follows immediately. □

Corollary 5.4: The ﬁelds F17 and F25 are Parker.

Proof: Up to isomorphism, the squares of F17 and of F25 are

{0, 1, 2, 4, 8, 9, 13, 15, 16}

and {0, 1, 2, 3, 4, x + 1, x + 3, 2x + 1, 2x + 1, 3x + 1, 3x + 1, 4x + 1, 4x + 1}

respectively. They manifestly have no three consecutive squares (excluding 0
and ±1). Thus, by our Lemma 5.4, they are Parker. □
We’ve ﬁnished the whole list of candidates. The ﬁnal result of this section
can be stated.

Theorem 5.1: F29 is the non-Parker ﬁeld of smallest order.
Proof: All ﬁnite ﬁelds of smaller order are Parker by Corollaries 5.1, 5.2,
5.3, and 5.4. We see that F29 is non-Parker by the aforementioned construction.
□

6 Search Algorithm for Finite Fields

We did our best in the previous section to work by argumentation. In this sec-
tion we’ll switch to empirical results obtained via a computer algebra system
[9]. It will ﬁrst be addressed how to generate all magic squares over a given
ﬁeld. In pseudo-code:

Algorithm 6.1:
# Input: A ﬁnite ﬁeld, Fq.
# Output: Set of all tuples (a2, b2, ..., i2) forming magic squares over Fq
# up to scaling.
function msos ﬁeld(Fq):
SQUARES ← {x
2 : x
2 ∈ Fq}
MSOS ← {}
e ← 0 # ﬁrst case.
for {a2, i2} ⊂ SQUARES:
if a2 + i2 ̸= 2e2: continue
c2, g2 ← 1, −1
B ← 3e2 − a2 − c2

D ← 3e2 − a2 − g2

F ← 3e2 − c2 − i2

H ← 3e2 − g2 − i2

if {B, D, F, H} ̸⊂ SQUARES: continue
if |{a2, B, c2, D, e2, F, g2, H, i2}| ̸= 9: continue

10

MSOS ← MSOS ∪ {(a2, B, c2, D, e2, F, g2, H, i2)}
e ← 1 # second case.
SEQUENCES ← {}
for {a2, i2} ⊂ SQUARES:
if a2 + i2 ̸= 2e2: continue
for {c2, g2} ⊂ SEQUENCES:
B ← 3e2 − a2 − c2

D ← 3e2 − a2 − g2

F ← 3e2 − c2 − i2

H ← 3e2 − g2 − i2

if {B, D, F, H} ̸⊂ SQUARES: continue
if |{a2, B, c2, D, e2, F, g2, H, i2}| ̸= 9: continue
MSOS ← MSOS ∪ {(a2, B, c2, D, e2, F, g2, H, i2)}
SEQUENCES ← SEQUENCES ∪ {{a2, i2}}
return MSOS

Implementation in the SageMath language is available at [11].
The correctness of the code follows roughly from some observations made
while proving Lemmas 5.3 and 5.4. We neglect to give a rigorous proof, but will
content ourselves noting the following intuition.
Any magic square of squares over a ﬁnite ﬁeld may be scaled into one of two
forms according to whether the central entry is zero:

a2 b2 1
d
2 0 f 2

−1 h2 i2 or a2 b2 c2

d
2 1 f 2

g2 h2 i2 .

Observe that in the ﬁrst case, the square is determined by just a2 and, in the
second case, by a2 and c2. Both cases are labeled accordingly in the code.

7 Observations on Finite Fields

Algorithm 6.1 was implemented in a computer algebra system [9] (actually, it
was ﬁrst written in a computer algebra system and then turned into pseudo-
code, but whatever). Some results:

Observation 7.1: In addition to the Parker ﬁelds given in the previous section,
the only Parker ﬁelds of prime order, p, with p < 1000 are F31, F43, F47, and F67.

Corollary 7.1: The smallest non-Parker ﬁeld with order p ≡ 3 ( mod 4)
is F59 with the explicit construction

202 122 72

22 12 232

222 252 292 .

11

Conjecture 7.1: The only Parker ﬁelds of prime order are:

F2, F3, F5, F7, F11, F13, F17, F19, F23, F31, F43, F47, and F67.

Observation 7.2: The ﬁrst few ﬁnite ﬁelds of prime order with more magic
squares (up to scaling) than any smaller such ﬁnite ﬁeld are:

Field # of magic squares
up to scaling
F2 0
F29 2
F61 4
F89 5
F97 6
F109 9
F113 13
F137 18
F181 24
F193 28

Conjecture 7.2: The only Parker ﬁelds whose order is strictly a prime power
are F9, F25, F27, and F243.

Note that conjectures 7.1 and 7.2 taken together assert that exactly 17 ﬁnite
ﬁelds are Parker. We could only think to justify the claim with an argument
from probability – which more or less means we couldn’t justify the claim. For
what it’s worth, we point out that the 2 conjectures of this section agree, but
are not proven by Theorem 28 in [10] (a ﬁnite ﬁeld is “Parker” in Labruna’s
terminology if it contains a magic square of squares “of order 9”).

8 A Search Algorithm for Rings

In this section, we address which rings of the form Z/nZ admit a 3 × 3 magic
square of squares – that is, which such rings are not Parker.
Our ﬁrst objective will be modifying Algorithm 6.1 to work on rings. As we
did before, ﬁrst the algorithm pseudo-code will be given and then an explana-
tion.

Algorithm 8.1:
# Input: An integer, n.
# Output: Set of all tuples (a2, b2, ..., i2) forming magic squares over Z/nZ}
# up to scaling by (Z/nZ)
×.
function msos ring(n):
SQUARES ← {x
2 : x
2 ∈ Z/nZ}
MSOS ← {}
for m|n:
 12

e ← m # The overline, · , is used to denote a residue in Z/nZ.
SEQUENCES ← {}
for {a2, i2} ⊂ SQUARES:
if a2 + i2 ̸= 2e2: continue
for {c2, g2} ∈ SEQUENCES:
B ← 3e2 − a2 − c2

D ← 3e2 − a2 − g2

F ← 3e2 − c2 − i2

H ← 3e2 − g2 − i2

if {B, D, F, H} ̸⊂ SQUARES: continue
if |{a2, B, c2, D, e2, F, g2, H, i2}| ̸= 9: continue
MSOS ← MSOS ∪ {(a2, B, c2, D, e2, F, g2, H, i2)}
SEQUENCES ← SEQUENCES ∪ {{a2, i2}}
return MSOS

Implementation in the SageMath language is available at [11].
For ﬁelds, we reduced to the cases in which the central entry of the magic
square was either 0 or 1. A similar approach is taken for Z/nZ. Consider the
orbits formed under the multiplicative action of (Z/nZ)
×. There is one orbit
corresponding to each divisor of n. Thus any magic square of squares over Z/nZ
may be scaled such that e is the residue of some divisor of n.

9 Observations on Rings

The code from the previous section was again implemented in a computer alge-
bra system [9] resulting in

Observation 9.1: The smallest ring of the form Z/nZ which admits a magic
square of squares is Z/27Z.

Observation 9.2: The ﬁrst few rings of the form Z/nZ with more magic

13

squares (up to scaling by (Z/nZ)
×) than any smaller such ring are:

Ring # of magic squares
up to scaling
Z/27Z) 3
Z/29Z) 7
Z/37Z) 9
Z/53Z) 13
Z/54Z) 36
Z/58Z) 56
Z/74Z) 72
Z/101Z) 75
Z/106Z) 104
Z/122Z) 240
Z/162Z) 576
Z/202Z) 604
 Ring # of magic squares
up to scaling
Z/218Z) 680
Z/226Z) 832
Z/274Z) 1296
Z/314Z) 1304
Z/346Z) 2112
Z/362Z) 2262
Z/386Z) 2260
Z/394Z) 2420
Z/458Z) 2904
Z/466Z) 2972
Z/482Z) 3860
Z/486Z) 6120

Conjecture 9.2: If Z/nZ has more magic squares (up to scaling) than any
smaller such ring, then n = 2p for some prime, p ≡ 1( mod 4), with exactly 7
exceptions: n = 27, 29, 37, 53, 54, 101, and 162.

Observation 9.3: The only Parker Z/nZ for odd n in the range 100 < n < 1000
are n = 129, 141, 147, and 201.

Conjecture 9.3: Z/201Z is the largest Parker ring of the form Z/nZ where n
is odd.

Observation 9.4: The only Parker Z/nZ for n divisible by 4 in the range
1000 < n < 3000 are n = 1032, 1072, 1104, 1128, 1488, 1608, 2064, and 2256.
Interestingly, each of these integers is of the form 2a3bp with a prime p ≡
3 (mod 4).

1032 = 23 · 3 · 43, 1072 = 24 · 67, 1104 = 24 · 3 · 23, 1128 = 23 · 3 · 47,

1488 = 24 · 3 · 31, 1608 = 23 · 3 · 67, 2064 = 24 · 3 · 43, and 2256 = 24 · 3 · 47.

Further searches targeting integers of this form revealed only that Z/3216Z is
Parker (which indeed ﬁts the form: 3216 = 24 · 3 · 67). It is surprising though
that such large Parker rings exist.

Conjecture 9.4: Z/3216Z is the largest Parker ring of the form Z/nZ.

Note a proof of the existence of inﬁnitely many Parker rings of the form
Z/nZ would prove that no magic square of distinct squares exists over the inte-
gers. If, instead, such a square existed and N were its largest entry, then Z/nZ
would be non-Parker for n > N . And therefore only ﬁnitely many such rings
could be Parker.
 14

REFERENCES

[1] Christian Boyer, Magic Square of Squares,
http://www.multimagie.com/English/SquaresOfSquares.htm
[2] Matt Parker, The Parker Square, Numberphile,
[interview by Brady Haran],
https://www.youtube.com/watch?v=aOT bG-vWyg
[3] John P. Robertson, Magic Squares of Squares,
Mathematics Magazine, vol. 69, no. 4, 1996, pp. 289–293.
JSTOR, www.jstor.org/stable/2690537.
[4] MathWorld, Congruum Problem,
http://mathworld.wolfram.com/CongruumProblem.html
[5] Eknath Ghate, The Kronecker-Weber Theorem,
Summer School on Cyclotomic ﬁelds, Pune, June 7-30, 1999
[6] Keith Conrad, The Gaussian Integers,
https://kconrad.math.uconn.edu/blurbs/
[7] Artin, Algebra
[8] Math Pages, Magic Square of Squares,
https://www.mathpages.com/home/kmath417/kmath417.htm
[9] SageMath, the Sage Mathematics Software System (Version 8.4),
The Sage Developers, 2015, http://www.sagemath.org.
[10] Giancarlo Labruna, Magic Squares of Squares of Order Three Over
Finite Fields, https://digitalcommons.montclair.edu/etd/138/
[11] Code repository: https://github.com/onnomc/parker-ring-search

15
