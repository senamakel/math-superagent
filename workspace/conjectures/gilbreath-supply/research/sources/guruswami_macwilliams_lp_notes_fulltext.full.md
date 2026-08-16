<!-- source: https://www.cs.cmu.edu/~venkatg/teaching/codingtheory/notes/notes5a.pdf | converted from PDF -->

Introduction to Coding Theory CMU: Spring 2010

Notes 5.1: Fourier Transform, MacWillams identities, and LP bound

February 2010

Lecturer: Venkatesan Guruswami Scribe: Venkat Guruswami & Srivatsan Narayanan

We will discuss the last and most sophisticated of our (upper) bounds on rate of codes with
certain relative distance, namely the ﬁrst linear programming bound or the ﬁrst JPL bound due
to McEliece, Rodemich, Rumsey, and Welch, 1977 (henceforth, MRRW). This bound is the best
known asymptotic upper bound on the rate of a binary code for a signiﬁcant range of relative
distances (which is roughly δ ∈ (0.273, 1/2)). We will present a complete and self-contained proof
of the this bound. A variant called the second JPL bound gives the best known upper bound for
the remainder of the range, and we will mention this bound (without proof) at the end.

The linear programming bound is so-called because it is based on Delsarte’s linear programming
approach which shows that the distance distribution of a binary code satisﬁes a family of linear
constraints whose coeﬃcients are the evaluations of a certain family of orthogonal polynomials (in
this case, the Krawtchouk polynomials). The optimum (maximum) of this linear program gives an
upper bound on A(n, d). MRRW constructed good feasible solutions to the dual of linear program
using tools from the theory of orthogonal polynomials, and their value gave an upper bound on
A(n, d) by weak duality.

In these notes, we will use Fourier analysis of functions deﬁned on the hypercube to derive a
relationship between the weight distribution of a linear code and its dual, called the MacWilliams
identiﬁes. These give the linear constraints of the above-mentioned linear program.

Instead of the using the linear program or its dual and the theory of orthogonal polynomials (and
speciﬁcally properties of Krawtchouk polynomials), in the second part of these notes, we will give
a self-contained proof of the ﬁrst linear programming bound for binary linear codes using a Fourier
analytic approach. This is based on the methods of Friedman and Tillich, which was later extended
also to general codes by Navon and Samorodnitsky, that shows that the dual of a linear code of
large distance must have small “essential covering radius” (which means that Hamming balls of
small radii around the dual codewords will cover a large fraction of the Hamming space {0, 1}n).
This shows that the dual must have large size, and therefore the code itself cannot be too large.
The method can be extended to non-linear codes, but we will be content with deriving the linear
programming bound for (binary) linear codes.

1 Fourier analysis over the Boolean hypercube

Let Fn be set of all real-valued functions over the boolean hypercube, i.e., Fn = {f : {0, 1}n → R}.
Then the following characterization is straightforward.

Exercise 1 Show that Fn forms a vector space with dimension 2n. In fact, show that {eα : α ∈

1

{0, 1}n} forms a basis for Fn, where eα : {0, 1}n → R is deﬁned by:

eα(x) = δxα =
 {
1, ifx = α
0, otherwise

In fact, the above exercise views a function f ∈ Fn as simply a vector of dimension 2n, indexed by
the ”coordinates” α ∈ {0, 1}n. This motivates us to deﬁne an inner product on Fn:

Deﬁnition 1 For f, g ∈ Fn, deﬁne the inner product between f and g to be:

⟨f, g⟩ = 1
2n ∑

x f (x)g(x) = Ex [f (x)g(x)]

(This is just the standard inner product for vectors over reals, but suitably normalized.)

Now, we will deﬁne another basis for Fn, called the Fourier basis. This needs the following simple
lemma.

Lemma 2 For every binary linear code C ⊆ {0, 1}n,

∑

c∈C(−1)
α·c =
 {
|C|, if α ∈ C⊥,
0, otherwise.

where · denotes the dot product modulo 2.

Proof: If α ∈ C⊥, then the claim is obvious. Suppose that α ̸∈ C⊥. Then, there exists a c0 ∈ C
such that α · c0 = 1. Now, for each c ∈ C,

(−1)
α·c + (−1)
α·(c+c0) = (−1)
α·c (1 + (−1)
α·c0) = 0 (1)

Summing Equation 1 for all c ∈ C, we get:

0 = ∑

c∈C
 ((−1)
α·c + (−1)
α·(c+c0)) = ∑

c∈C(−1)
α·c + ∑

c∈C(−1)
α·(c+c0) = 2 ∑

c∈C(−1)
α·c,

giving the claim. □

Corollary 3 We have
 ∑

c∈{0,1}n(−1)
α·c =
 {
2n, if α = 0,
0, otherwise.

Proof: In Lemma 2, take C to be the whole vector space {0, 1}n, so that C⊥ = {0}. □

2

Remark 4 In this lecture, the notation 0 is typically overloaded to mean either a single alphabet
symbol, or the zero vector (0n) of the vector space. However, the right deﬁnition should be clear
from the context.

For each α ∈ {0, 1}n, deﬁne χα : {0, 1}n → R by χα(x) = (−1)α·x (where · refers to the inner
product between vectors, taken modulo 2). The function χα is often called a character function.
We show that the set of all character functions also forms an orthonormal basis for Fn.

Lemma 5 ⟨χα, χβ⟩ = δαβ

Proof:
 ⟨χα, χβ⟩ = Ex [(−1)
α·x(−1)
β·x] = 1
2n ∑

x (−1)
(α−β)·x =
 {
1, if α − β = 0,
0, otherwise

using Corollary 3. The claim follows from the deﬁnition of δαβ. □

Corollary 6 Let B be the set of character functions, i.e., B = {χα : α ∈ {0, 1}n}. Then, B is an
orthonormal basis for Fn, called its Fourier basis.

Proof: From Lemma 5, it follows that B is a linearly independent set. Also the cardinality of
B is 2n, which equals the dimension of the whole space Fn. Therefore, B must be a basis. The
orthonormality of B is directly implied again by Lemma 5. □

By the deﬁnition of a basis, any function f ∈ Fn can be expressed uniquely as a linear combination
of the character functions. That is, there exist ˆf (α) ∈ R such that

f = ∑

α ˆf (α)χα .

(We use the notation ˆf (α), instead of the conventional cα to remind us that the coeﬃcients depend
on f .) Note that this is equivalent to saying

f (x) = ∑

α ˆf (α)χα(x)

for all x ∈ {0, 1}n.

The following are some immediate consequences of this fact.

Lemma 7 Let f, g ∈ Fn. Then the following hold.

1. ⟨f, χα⟩ = ˆf (α)

2. (Parseval’s identity) ⟨f, g⟩ = ∑
α ˆf (α)ˆg(α)

3. ˆf (0) = Exf (x)
 3

Proof: Each of the above claims can be shown by a straightforward calculation.

1. ⟨f, χα⟩ = ⟨∑
β ˆf (β)χβ, χα⟩ = ∑
β ˆf (β)⟨χβ, χα⟩ = ∑
β ˆf (β)δαβ = ˆf (α)

2. ⟨f, g⟩ = ⟨f, ∑
α ˆg(α)χα⟩ = ∑
α ˆg(α)⟨f, χα⟩ = ∑
α ˆf (α)ˆg(α)

3. ˆf (0) = ⟨f, χ0⟩ = Ex [f (x)(−1)0·x] = Exf (x)

□

2 Dual codes, Fourier analysis, and MacWilliams identities

Let us introduce the following notation: for any S ⊆ {0, 1}n, deﬁne 1S : {0, 1}n → R, called the
characteristic function of S, by
 1S(x) =
 {
1, if x ∈ S,
0, otherwise.

We will now show that Fourier transform of the characteristic function of a code is essentially the
same (up to a constant scaling factor) as the characteristic function of its dual. This is useful
because the Fourier transform can be viewed as a notion of duality for functions. Fortunately,
there is a natural correspondence between the two notions (dual codes and Fourier transforms).

Lemma 8 For any linear code C ⊆ {0, 1}n,

̂1C = |C|
2n 1C⊥

Proof: For every α ∈ {0, 1}n,

̂1C(α) = ⟨1C, χα⟩ = 1
2n ∑

x 1C(x)χα(x) = 1
2n ∑

x∈C(−1)
α·x =
 { 1
2n |C|, if α ∈ C⊥,
0, otherwise

using Lemma 2. Therefore, ̂1C(α) = |C|
2n 1C⊥(α),

for all α ∈ {0, 1}n, giving the claim. □

Deﬁnition 9 For any S ⊆ {0, 1}n, let

W S
i = #{x ∈ S : wt(x) = i},

that is, W S
i denotes the number of points in S of weight i. Further, by weight distribution of S, we
denote the (n + 1)-tuple W S = ⟨W S
0 , W S
1 , . . . , W S
n ⟩.

4

Now, our goal is to relate the “weight distribution” of a code C to that of its dual C⊥. Let
ℓ ∈ {0, 1, . . . , n}. Then,
 W C⊥
ℓ = ∑

α:wt(α)=ℓ 1C⊥(α)

= 2n

|C|
 ∑

α:wt(α)=ℓ ̂1C(α)

= 2n

|C|
 ∑

α:wt(α)=ℓ Ex [1C(x)(−1)
α·x]

= 2n

|C| Ex
 

 ∑

α:wt(α)=ℓ 1C(x)(−1)
α·x




= 2n

|C| Ex
 

1C(x) ∑

α:wt(α)=ℓ
(−1)
α·x




For completeness, we calculate the sum ∑
α:wt(α)=ℓ(−1)α·x in the following lemma. The exact sum
is not of any signiﬁcance for our purposes in this course. We will however use the fact that this
sum depends only on the weight of x.

Lemma 10 For any x ∈ {0, 1}n with wt(x) = i,

∑

α:wt(α)=ℓ
(−1)
α·x =
 ℓ∑

j=0(−1)
j(i
j
)(
n − i
ℓ − j
) .

The latter quantity will be denoted as Kℓ(i) — the value of the Krawtchouk polynomial at i.

Proof: Notice that summation is taken over all α of a given weight ℓ. So, by symmetry, it depends
only the number of 1’s in x, and not on their positions. Hence, without any loss in generality, assume
that x = 1i0n−i. A vector α of weight ℓ must have j 1’s in the ﬁrst i positions, and ℓ − j in the
last n − i positions, for some j ∈ {0, 1, . . . , ℓ}, and in this case (−1)x·α = (−1)j. The number of α’s
satisfying this condition for any particular j ∈ {0, 1, . . . , ℓ} equals (i
j)(n−i
ℓ−j). The claim thus follows.
□

Remark 11 (Krawtchouk polynomial) The quantity ∑ℓ
j=0(−1)j(i
j)(n−i
ℓ−j), denoted Kℓ(i), can
be regarded as the evaluation of a polynomial Kℓ at wt(x) = i. Kℓ is usually called the ℓth

Krawtchouk polynomial and is deﬁned as

Kℓ(X) =
 ℓ∑

j=0(−1)
j(
X
j
 )(
n − X
ℓ − j
 ) .

(The function Kℓ also depends on n, but we supress this dependence for notational convenience.)
Note that Kℓ is a polynomial of degree ℓ and K0(X) = 1 and K1(X) = n − 2X, etc.

5

Now, we will complete the calculation of W C⊥
ℓ .

W C⊥
ℓ = 2n

|C| 1
2n ∑

x
 

1C(x) ∑

α:wt(α)=ℓ
(−1)
α·x




= 1
|C|
 ∑

x 1C(x)Kℓ(wt(x))

= 1
|C|
 ∑

x∈C Kℓ(wt(x))

= 1
|C|
 n∑

i=0
 ∑

x∈C,wt(x)=i Kℓ(i)

giving
 W C⊥
ℓ = 1
|C|
 n∑

i=0 W C
i Kℓ(i) (2)

for every ℓ = 0, 1, 2, . . . , n.

Equation 2, called the MacWilliams identity, tells us that the weight distribution of the dual code
C⊥ is completely determined once we are given the weight distribution of the code C.

Remark 12 We can write the MacWilliams identitities (2) equivalently as:

W C⊥
ℓ = Ex∈C [Kℓ(wt(x))] ,

or as a functional equation
 n∑

ℓ=0 W C⊥
ℓ zℓ = 1
|C|
 n∑

i=0 W C
i (1 − z)
i(1 + z)
n−i .

Exercise 2 Extend the MacWilliams identities to linear codes over any ﬁnite ﬁeld Fq. Speciﬁcally,
if C is a q-ary linear code of block length n, and as before W C
i (resp. W C⊥
i ) denote the number of
codewords of C (resp. C⊥) of Hamming weight i, then

W C⊥
ℓ = 1
|C|
 n∑

i=0 W C
i K(q)
ℓ (i)

where the q-ary Krawtchouk polynomial is deﬁned as

K(q)
ℓ (X) =
 ℓ∑

j=0(−1)
j(q − 1)
ℓ−j(
X
j
 )(n − X
ℓ − j
 ) .

[[ Hint: When the ﬁeld size q equals a prime p, replace (−1)x·y in the proof for the binary case
by ζ x·y
p where ζp = e2πi/p is a primitive p’th root of unity and x · y is, as usual, computed over the
underlying ﬁeld Fq.
 6

When q = pt for a prime p, the role of (−1)x·y can be played by ζ Tr(x·y)
p where Tr is the trace map
from Fq to Fp = {0, 1, 2 . . . , p − 1}: Tr(z) = z + zp + · · · + zpt−1. ]]

Exercise 3 Using the above, compute the weight distribution of the [qm−1, qm−1−m, 3]q Hamming
code.

3 A linear program bounding A(n, d)

In this section, we will use the MacWilliams identity to derive a linear program that bounds the
size of every code with a given minimum distance d, and thus bounds A(n, d). (Recall that A(n, d)
is the maximum size of any binary code with block length n and minimum distance d.)

For the moment, we will focus on linear codes C. Consider the linear program:

Maximize
 n∑

i=0 Ai

s.t. A0 = 1

Ai ≥ 0, i = 1, . . . , n

Ai = 0, i = 1, . . . , d − 1
n∑

i=0 Kℓ(i)Ai ≥ 0, ℓ = 1, . . . , n

We claim that for any linear code C of distance at least d, the assignment Ai = W C
i is a feasible
solution. Indeed, the ﬁrst two constraints are satisﬁed trivially. The constraint Ai = 0 for 1 ≤ i < d
enforces that the minimum distance of the code (that is, the minimum Hamming weight of any
nonzero code word) is at least d. The last set of constraints follow from the MacWilliams identities
for any ℓ ∈ {1, 2, . . . , n}, n∑

i=0 W C
i Kℓ(i) = W C⊥
ℓ ≥ 0

For this assignment, the objective function takes the value

n∑

i=0 W C
i = |C|

Therefore, the optimum of the linear program upper bounds the size of any linear code C of distance
at least d.

Now, we consider general codes C, and prove that they satisfy the same bound. Without loss of
generality, assume that 0n ∈ C. Deﬁne:

AC
i = #{(x, y) ∈ C2 | ∆(x, y) = i}
|C|

7

We claim that AC
i is a feasible solution to the linear program. The ﬁrst three sets of constraints are
trivially satisﬁed as before, whereas the last set of constraints can be veriﬁed in a straightforward
manner:
 n∑

i=0 AC
i Kℓ(i) = 1
|C|
 n∑

i=0
 ∑

(x,y)∈C2:∆(x,y)=i Kℓ(i)

= 1
|C|
 n∑

i=0
 

 ∑

(x,y)∈C2:∆(x,y)=i
 

 ∑

z:wt(z)=ℓ(−1)
(x−y)·z








= 1
|C|
 ∑

(x,y)∈C2
 

 ∑

z:wt(z)=ℓ
(−1)
(x−y)·z




= 1
|C|
 ∑

z:wt(z)=ℓ
 

 ∑

(x,y)∈C2(−1)
x·z(−1)
y·z




= 1
|C|
 ∑

z:wt(z)=ℓ
 (∑

x∈C(−1)
x·z) 

∑

y∈C(−1)
y·z




= 1
|C|
 ∑

z:wt(z)=ℓ
 (∑

x∈C(−1)
x·z)2

≥ 0

The value of the objective function is:

n∑

i=0 A
C
i = 1
|C|
 n∑

i=0
 

 ∑

(x,y)∈C2:∆(x,y)=i 1


 = 1
|C|
 ∑

(x,y)∈C2 1 = |C|

Therefore, the optimum value of the linear program upper bounds the size of any code with mini-
mum distance at least d.

3.1 Dual program and the MRRW bound

Consider the dual program for the above linear program. The dual program has variables β1, β2, . . . , βn
(where βi ≥ 0). Deﬁne β(X) to be the polynomial

β(X) = 1 +
 n∑

ℓ=0 βℓKℓ(X) .

Then the dual program is given by:

Minimize β(0)

s.t. βi ≥ 0, i = 1, 2, . . . , n

β(j) ≤ 0, j = d, . . . , n

8

By the weak duality theorem, the value of any feasible solution to the dual program upper bounds
the optimum value of the linear program, and hence also upper bounds A(n, d). Hence, in order to
upper bound the size of the code, it suﬃces to exhibit a dual feasible solution with a small objective
function. This was, in fact, the approach followed by MRRW, leading to the ﬁrst linear program-
ming bound. However, this involves studying several properties of Krawtchouk polynomials. In the
second installment of these notes, we will prove the same bound by following a diﬀerent approach
based on Fourier analysis.
 9
