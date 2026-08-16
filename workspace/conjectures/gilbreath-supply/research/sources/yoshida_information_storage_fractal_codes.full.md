<!-- source: https://arxiv.org/pdf/1111.3275 | converted from PDF -->

MIT-CTP 4326

Information storage capacity of discrete spin systems

Beni Yoshida

Center for Theoretical Physics, Massachusetts Institute of Technology, Cambridge, Massachusetts 02139, USA and

Institute for Quantum Information and Matter, California Institute of Technology, Pasadena, California 91125, USA

(Dated: November 27, 2024)

Understanding the limits imposed on information storage capacity of physical systems is a problem

of fundamental and practical importance which bridges physics and information science. There is

a well-known upper bound on the amount of information that can be stored reliably in a given

volume of discrete spin systems which are supported by gapped local Hamiltonians. However, all

the previously known systems were far below this theoretical bound, and it remained open whether

there exists a gapped spin system that saturates this bound. Here, we present a construction

of spin systems which saturate this theoretical limit asymptotically by borrowing an idea from

fractal properties arising in the Sierpinski triangle. Our construction provides not only the best

classical error-correcting code which is physically realizable as the energy ground space of gapped

frustration-free Hamiltonians, but also a new research avenue for correlated spin phases with fractal

spin conﬁgurations.

I. INTRODUCTION AND SUMMARY OF RESULTS

Understanding the limits imposed on information storage capacity of physical systems is a problem of fundamental
and practical importance which bridges physics and information science [1]. This problem has been addressed for
continuum systems by Bekenstein [2]. He showed that it is not possible to store an inﬁnite amount of information on
a ﬁnite system and derived the well-celebrated bound on the number of logical bits that can be stored inside a ﬁnite
region:
 S ≤ 2πkBLE
ℏc (1)

where S is the amount of information stored, L is the linear length of the region, and E is the total energy. While
the Bekenstein bound itself can be derived from simple quantum mechanical calculations, the most beautiful outcome
concerning the Bekenstein bound is that black holes saturate this theoretical limit, giving rise to the area law of
black hole entropies [3]. This is essentially due to the observation that an object with a large amount of information
(entropy) tends to have high energy, and will eventually turn into a black hole once its energy exceeds a critical value.
This surprising connection between information theory and black hole physics is at the heart of the thermodynamic
treatment of black holes and the holographic principle [4].
Recently, a similar question on information storage capacity for discrete spin systems on a lattice has been addressed.
Consider discrete spin systems deﬁned on a D-dimensional lattice which is governed by a local gapped Hamiltonian
where D is the spatial dimension. To be concrete, we consider commuting frustration-free Hamiltonians with local
interaction terms, which are referred to as local codes. Now, we think of encoding bits of information into degenerate
gapped ground states of local codes. Then, the following bound is known to hold [5]:

kd1/D ≤ O(n) (2)

where k is the number of encoded logical bits, d is the code distance, and n is the total number of spins when the
energy ground space of a local Hamiltonian is viewed as the codeword space of an error-correcting code. A proportional
factor on the right-hand side of the bound depends on the range of interaction terms. Note that the code distance d is
a quantitative measure of the reliability of encoded bits against errors. Thus, the bound above reveals a fundamental
tradeoﬀ between the amount of encoded information k and the reliability of encoding d.arXiv:1111.3275v3  [cs.IT]  24 Dec 2012
2

1 1 0 0 0

1 0
1 0
1 0
1 1
0 1
0
0
0 0
1 0
1 0
0 1
0 1
1 1

0 0 1
 repetition code

theoretical limitcode distance
number of logical bits

d
 k

a b

spins

local interactions

FIG. 1: (a) Storage of information in discrete spin systems via local interactions. (b) A theoretical upper bound on information

storage capacity for D = 2. The graph is shown in a logarithmic scale. The dotted line represents a family of repetition codes.

Motivated by a tremendous success of the Bekenstein bound and its signiﬁcant impact on black hole physics, one
may be naturally led to an analogous question on information storage capacity of discrete spin systems, concerning
local codes which saturate the local code bound. This is a problem of practical importance since, in principle, such a
local code would be the best error-correcting code that is physically realizable with frustration-free local Hamiltonians.
This problem may also be of fundamental importance since such a local code may be viewed as an analog of a black hole
for discrete spin systems in some appropriate interpretation which is yet to be discovered, and may be useful in further
establishing the connection between continuum and discrete descriptions of space-time and quantum gravity [6, 7].
Finally, such a local code may be a candidate model of novel spin phases with exotic correlations which are beyond
descriptions of known eﬀective theories with mass gap, such as topological ﬁeld theory.
However, ﬁnding a local code which saturates the bound turned out to be a challenging problem. In particular,
previously found local codes were far below the bound as seen in Fig. 1(b). To gain some insights on the problem,
let us look at a prototypical example of local codes on a two-dimensional lattice (D = 2). A repetition code encodes
0 and 1 into repetitions of zeros and ones; 000 · · · and 111 · · · , and can be physically realized as a local code through
local ferromagnetic interactions. Since it encodes a single bit of information, it has k = 1. A repetition code is
known to be robust against errors since the originally encoded bit of information can be faithfully recovered provided
that the number of damaged spins is less than n
2 . A natural measure of the reliability of encoding is the number of
diﬀerent spin values in two codewords, which is called the Hamming distance in the coding theory language. Since
all the spin values of codewords are diﬀerent in a repetition code, the Hamming distance between codewords is n,
and the code distance is d = n. Now, let us analyze coding properties of a repetition code in terms of the local code
bound. For D = 2, the local code bound is k√d ≤ O(n), and the repetition code is far below the theoretical limit.
One may modify a repetition code by splitting the entire lattice into smaller subparts and using them as individual
repetition codes. However, such a construction gives a family of local codes with kd = n as shown with a dotted line
in Fig. 1(b), which is still below the bound. There had been no local code with provably better coding properties
than a family of repetition codes. Also, it should be noted that commercial memory devices, such as hard disc drives
(HDD), are constructed with ferromagnetic materials which are physical realizations of repetition codes.

Main result: In this paper, we present a construction of local codes, called fractal codes, which saturate the
theoretical limit asymptotically:
 k ∼ O(LD−1), d ∼ O(L
D−ϵ)

for D ≥ 2 where ϵ is an arbitrary small positive number, L is the linear length of the lattice and n = O(L
D).
 3

Fractal geometry as a code: Our construction borrows an idea from the Sierpinski triangle, a well-known
example of fractal geometries. The Sierpinski triangle has self-similar properties where the same patterns appear
repeatedly at diﬀerent length scales (Fig. 2a). This peculiar geometric nature of the triangle is reﬂected in its non-
integer dimensionality where the number of ﬁlled elements L
log 3/ log 2 grows as if the spatial dimension is log 3
log 2 ∼ 1.585.
While the Sierpinski triangle had been long thought to be a mathematical object, it turned out that the triangle is
physically realizable. Fig 2(a) shows a physical realization of the Sierpinski triangle on a square lattice via three-body
interactions where each term is minimized when local constraints c = a + b (mod 2) on three neighboring spins are
satisﬁed [8]. It has been pointed out that such a fractal system, generated by cellular automaton, may be useful as
an error-correcting code with an eﬃcient decoder [9]. Recently, its coding properties have been predicted as [5]:

k ∼ O(L), d ∼ O(L
 log 3
log 2 )

based on numerical simulations along with analytical arguments for inﬁnite lattices.

FIG. 2: Fractal codes. (a) The Sierpinski triangle and its physical realization on a square lattice (p = 2). Filled elements are

mapped to 1s while unﬁlled elements are mapped to 0s. Interaction terms are three-body. (b) A generalization of the Sierpinski

triangle (p = 3). Black elements are mapped to 1s, grey elements are mapped to 2s, and unﬁlled elements are mapped to 0s.

Despite a remarkable idea of constructing a local code based on Sierpinski triangle, previous works have two serious
drawbacks. First, this fractal code is still far below the theoretical limit as seen in Fig. 1(b). Second, in order to prove
the prediction of d ∼ O(L
 log 3
log 2 ), one needs to analyze Hamming distances between all the 2
L ground states and ﬁnd
the minimal Hamming distance, which is a formidable challenge both from analytical and computational perspectives.
We start by presenting the resolution of the ﬁrst challenge. Our construction of fractal codes utilizes a generalization
of Sierpinski triangle with higher-dimensional spins. To begin with, let us discuss fractal properties of Sierpinski
triangle with three-dimensional spins where possible spin values are 0, 1, 2 as shown in Fig. 2(b). The number of
non-zero spins in this generalized Sierpinski triangle is L
 log 6
log 3 , and its fractal dimension is log 6
log 3 ∼ 1.631, which is larger
than log 3
log 2 ∼ 1.585. Then, one may naturally expect that this generalization gives a fractal code with k ∼ O(L) and

d ∼ O(L
 log 6
log 3 ) where k is the number of encodable three-dimensional logical spins.
 4

The key observation here is that the fractal dimension of Sierpinski triangle grows as the inner dimension of spins
increases. In particular, at the limit where p goes to inﬁnity, we notice

D(2)
p = log( p(p+1)
2 )
log p → 2 for p → ∞. (3)

Therefore, by taking suﬃciently large p, one can construct a fractal code with k(p) ∼ O(L) and d ≥ O(L
2−ϵ) for an
arbitrary small ϵ > 0 where k(p) is the number of encodable p-dimensional spins. This family of fractal codes based
on generalized Sierpinski triangle will saturate the bound in Eq. (2) asymptotically. While our construction of fractal
codes uses p-dimensional spins with p > 2, one can simulate these fractal codes through two-dimensional spins.
Then, what about the bound on higher-dimensional systems with D > 2 ? Fortunately, there exist higher-
dimensional generalizations of Sierpinski triangle constructed on a D-dimensional hypercubic lattice (see [10] for
example). For D-dimensional Sierpinski triangle with p-dimensional spins, its fractal dimension is given by

D(D)
p = log ( p(p + 1) · · · (p + D − 1)
D!
 ) / log(p) (4)

which approaches to D as p goes to inﬁnity: D(D)
p → D for p → ∞. A fractal code based on D-dimensional Sierpinski
triangle has k(p) ∼ O(LD−1) and d ∼ O(L
D(D)
p ), and one can construct fractal codes which saturate the bound
asymptotically in any spatial dimension.

Main theorem: Discussion above is valid only if the assumption that the fractal dimension of the code distance
is equal to the fractal dimension of Sierpinski triangle is true:

Theorem 1 (Fractal dimension of code distance). In fractal codes, the fractal dimension of the code distance d is
equal to the fractal dimension of the Sierpinski triangle:

k ∼ O(L
D−1) d ∼ O(LD(D)
p ) (5)

where D(D)
p is the fractal dimension of D-dimensional Sierpinski triangle constructed with p-dimensional spins, and
k is the number of encodable logical p-dimensional spins.

The rest of the paper is dedicated to the proof of this theorem. A precise deﬁnition of fractal codes is presented
in subsequent sections, and a deﬁnition of local codes is presented in appendix A along with a brief introduction to
theory of error-correcting codes and a derivation of the local code bound.
In deriving the local code bound, only the locality of interaction terms on a discretized space is assumed. It
is interesting to observe that, from such a simple assumption, an area law naturally arises in fractal codes; the
number of encoded bits k is area-like with k ∼ O(LD−1), while the code distance d is asymptotically volume-like
with d ∼ O(L
D−ϵ). It is also interesting to note that, the area-law arising in fractal codes can be derived from
purely classical calculations while derivations of black hole area-law and entanglement entropy area-law both require
quantum mechanics. Indeed, fractal codes can be represented as a spin network state [6]. In a very broad and
expanded sense, fractal codes, and other physical realizations of cellular automaton, are black-hole like since their
inner states are completely determined by the degree of freedom at the surface. However, a connection between
fractal codes and black holes has not been established, with further work needed.

Comments: The paper is organized as follows. In section II, we discuss two-dimensional cases. In section III, we
discuss three-dimensional cases. In section IV, we sketch the proof for D > 3. In section V, we list possible future
problems and give some discussion. The paper is written in a self-consistent way, and most of non-trivial mathematical
proofs are presented in appendix B, so we hope that the main discussion is accessible to readers both in coding theory
and physics community. The main technical result of this paper is lemma 2 concerning the weights of raw vectors of
the Sierpinski triangle, which may be of interest by its own.
 5

II. TWO-DIMENSIONAL FRACTAL CODE

In this section, we introduce fractal codes on a two-dimensional lattice and show the asymptotic saturation of the
local code bound for D = 2. Theoretical tools to compute the code distance of fractal codes are also developed.

A. Basic properties of the Sierpinski triangle

We begin by recalling basic properties of the Sierpinski triangle [10]. The Sierpinski triangle arises by considering
the Pascal triangle, a triangular array of the binomial coeﬃcients, represented modulo p (see Fig. 3(a)). For our
purpose, it is convenient to represent the Sierpinski triangle as a matrix (Fig. 3(b)-(e)). Consider an L × L matrix B
where L = p
m with arbitrary prime p and positive integer m. Entries of B are denoted as B(t)r which corresponds
to an entry at t-th raw and r-th column of the matrix for t, r = 0, · · · , L − 1. Note that t and r run from 0 to L − 1,
instead of running from 1 to L in our notation. Then, the Sierpinski triangle arises by taking the following entries:

B(t)r = tCr (mod p) (6)

where tCr = 0 for r > t. We call B the Pascal matrix due to its resemblance to the Pascal triangle.
Entries B(t)r obey the following constraint:

B(t + 1)r+1 = B(t)r + B(t)r+1 (mod p) (7)

where periodic boundary conditions are set for r, meaning that B(t)L = B(t)0. The entire system can be viewed as
a “computational machine” which computes a vector B(t) = (B(t)0, B(t)1, · · · , B(t)L−1) at time t for a given initial
condition B(0) = (1, 0, · · · , 0) after the “time-evolution” according to Eq. (7). In this light, the Sierpinski triangle
can be viewed as a history of time-evolution of one-dimensional cellular automaton embedded in a two-dimensional
space.

Fractal dimensions: Fractal dimensions of the Sierpinski triangle can be computed by counting the number of
non-zero entries in B. For this purpose, it is useful to represent t and r in p-adic forms:

r = (rm, rm−1, · · · , r1)p, r =
 m∑

m′=1 p
m′−1rm′

t = (tm, tm−1, · · · , t1)p, t =
 m∑

m′=1 p
m′−1tm′

where rj and tj are positive integers with 0 ≤ rj, tj ≤ p − 1. Then, entries B(t)r can be calculated by the following
lemma:

Lemma 1. One has
 tCr =
 m∏

m′=1 tm′ Crm′ (mod p), (8)

and
 tCr ̸= 0 (mod p) iﬀ tm′ ≥ rm′ for all m
′. (9)

The proof of the lemma is straightforward. As a direct consequence of the lemma, one can compute the fractal
dimensions of the Sierpinski triangle:
 6

FIG. 3: (a) The Pascal triangle and the Sierpinski triangle. (b)-(e) The Pascal matrices. (b) p = 2 and m = 3. (c) p = 3 and

m = 2. (d) p = 5. (e) p = 7 and m = 1.

Corollary 1 (Fractal dimension). Let W (B) denote the number of non-zero entries in B. Then, one has

W (B) = ( p(p + 1)
2
 )m = L
D(2)
p (10)

where L = p
m, and the fractal dimension of the Pascal matrix B is given by

D(2)
p = log ( p(p + 1)
2
 ) / log p. (11)

Proof. The number of non-zero entries in B is equal to the number of pairs of t and r such that

tm′ ≥ rm′ for all m
′

from lemma 1. There are p(p+1)
2 possible pairs of (tm′, rm′) satisfying tm′ ≥ rm′ for each m
′. Therefore, in total, there

are W (B) = ( p(p+1)
2 )m non-zero entries.

Some examples of the Sierpinski triangle and its fractal dimensions are shown in Fig. 4.

Self-similarity: The Pascal matrices B have fractal properties with self-similar structures. In particular, as shown
in Fig. 5(a), similar patterns appear repeatedly at various length scales. Self-similarity of the Sierpinski triangle is
summarized as follows:
 7

FIG. 4: Examples of fractal dimensions for p = 2, 3, 5.

Fact 1 (Self-similarity). We denote the Pascal matrix deﬁned for L = p
m as B
(m). Then, one has

B
(1) =
 






 0C0, 0C1, · · · , 0Cp−1

1C0, 1C1, · · · , 1Cp−1
... ... ... . . .

p−1C0, p−1C1, · · · , p−1Cp−1






 (12)

and
 B
(m) =
 






 0C0 · B
(m−1), 0C1 · B
(m−1), · · · , 0Cp−1 · B
(m−1)

1C0 · B
(m−1), 1C1 · B
(m−1), · · · , 1Cp−1 · B
(m−1)

... ... ... . . .

p−1C0 · B
(m−1), p−1C1 · B
(m−1), · · · , p−1Cp−1 · B
(m−1)






 . (13)

Therefore, small Pascal matrices B
(m−1) appear repeatedly as submatrices of the original Pascal matrix B
(m).
Fact 1 can be proven easily by lemma 1. It is worth looking at an example for p = 2:

B
(1) =
 [
1, 0
1, 1
]
 , B
(m) =
 [
B
(m−1), 0
B
(m−1), B
(m−1)
]
 (14)

where 0 represents a 2m−1 × 2
m−1 zero matrix. An example for p = 3 is shown in Fig. 5.

B. Deﬁnition of fractal codes

Next, we give a precise deﬁnition of fractal codes in two-dimensional systems. Consider a two-dimensional square
lattice with n = L × 2L spins where spins are p-dimensional and spin values are 0, · · · , p − 1. We assume that p is
a prime number, and L = p
m with arbitrary positive integer m. Each spin is labeled by “time” t and “position” r
where t = 0, · · · , L − 1 and r = 0, · · · , 2L − 1. We set periodic boundary conditions along the time axis, and set open
boundary conditions along the position axis (see Fig. 6).
The admissible spin conﬁgurations of fractal codes obeys the following local constraint:

x(t + 1)r = x(t)r−1 + x(t)r (mod p) 0 ≤ t ≤ L − 2 (15)

8

FIG. 5: (a) An example of a self-similar property for p = 3. B(1) appears repeatedly as submatrices of B(2). (b) Self-similar

properties at diﬀerent length scales.

FIG. 6: The construction of fractal codes. The example above shows the case with p = 2 and L = 8 (m = 3). Periodic

boundary conditions are set along the time axis. Admissible spin conﬁgurations of a fractal code appear as ground states of a

three-body Hamiltonian. The ﬁrst raw at t = 0 is called an initial condition. Eight spins on the right hand side of the initial

condition are zero due to boundary terms.

where x(t)r = 0, · · · , p − 1 represents the spin value at (t, r). Notice that such spin conﬁgurations can be physically
realized as ground states of the following three-body local Hamiltonian:

Hf ractal = ∑

t,r Π(t)r, Π(t)r = x(t + 1)r − x(t)r−1 − x(t)r (mod p) (16)

with a ﬁnite energy gap. There are p2L admissible spin conﬁgurations which can be uniquely speciﬁed by the “initial
condition” x(0) = (x(0)0, · · · , x(0)2L−1) for t = 0 on the ﬁrst raw of a lattice (see Fig. 6). The original Sierpinski
triangle arises by taking x(0) = (1, 0, · · · , 0).
 9

Now, we construct the fractal codes based on admissible spin conﬁgurations obeying Eq. (15). Here, we further
limit our considerations to spin conﬁgurations which satisfy the following initial condition:

x(0)r = 0 for r ≥ L. (17)

This constraint may be physically realized by setting additional terms on the boundary of the lattice:

Hboundary = ∑

r≥L x(0)r. (18)

We denote a space of spin conﬁgurations speciﬁed by Eq. (15) and Eq. (17) as C(2)
p , and call it the codeword space of
a fractal code. Coding properties of fractal codes are summarized in the following theorem.

Theorem 2 (Two-dimensional fractal code). For the codeword space C(2)
p speciﬁed by Eq. (15) and Eq. (17), let k
be the number of encodable p-dimensional spins and d be the code distance of the code (i.e. the minimal Hamming
distance among all the possible spin conﬁgurations). Then, we have

k = L, d = L
D(2)
p . (19)

where
 D(2)
p = log ( p(p + 1)
2
 ) / log(p). (20)

Here, we notice that D(2)
p increases as p increases. In particular, since D(2)
p → 2 for p → ∞, we can construct a
code which asymptotically saturates the bound k√d ≤ O(n) in Eq. (2).

C. Principal vectors

Finally, we give the proof of theorem 2 by developing a theoretical tool which is useful in computing the code
distance of fractal codes.

Principal vectors: Let us consider the Pascal matrix B. We denote entries of the t-th row in B as B(t) where

B(t) = (B(t)0, · · · , B(t)L−1)

and call them principal vectors. For example, with m = 2 and p = 2, we have the following principal vectors:

B(0) = (1, 0, 0, 0)

B(1) = (1, 1, 0, 0)

B(2) = (1, 0, 1, 0)

B(3) = (1, 1, 1, 1).

See examples in Fig. 3.
Note that principal vectors B(t) are all independent. In particular, for an arbitrary vector v = (v0, v1, · · · , vL−1)
with vj = 0, · · · , p − 1, one can decompose v uniquely by using principal vectors:

v =
 L−1∑

t=0 c(t)B(t) (mod p) (21)

where c(t) = 0, · · · , p − 1. The following lemma is particularly useful in lower bounding the weight of v:
 10

Lemma 2 (Inequality on principal vectors). Consider the following linear combination of principal vectors:

v =
 L−1∑

t=0 c(t)B(t)

and denote the smallest positive integer t such that c(t) ̸= 0 as tmin. Then, one has

W (v) ≥ W (B(tmin)) (22)

where W (v) represents the number of non-zero entries in v.

Below, we give an intuition on the proof for p = 2 with an example. Consider the case with p = 2 and L = 8. One
may easily see that the lemma holds for the following vectors:

B(2) = (1, 0, 1, 0, 0, 0, 0, 0), B(5) = (1, 1, 0, 0, 1, 1, 0, 0)

B(2) + B(5) = (0, 1, 1, 0, 1, 1, 0, 0)

since W (B(2) + B(5)) ≥ W (B(2)). An important observation is that the ﬁrst four entries and the last four en-
tries of B(5) are exactly the same; (1, 1, 0, 0)(1, 1, 0, 0), while B(2) have non-zero entries only on the ﬁrst four;
(1, 0, 1, 0)(0, 0, 0, 0). Then, even if some entries of B(2) were cancelled by adding B(5) on the ﬁrst four entries, these
eliminated entries would be recovered on the last four entries as a result of adding B(5). By generalizing this obser-
vation, one notices that adding B(t) (t ≥ 4) to v does not decrease the weight of v if the last four entries of v are all
zero, since B(t) has the same entries for the ﬁrst and last four entries. Note that such v can be written as a linear
combination of B(0), B(1), B(2), B(3). In fact, one can show that adding B(t) to v such that t > tmin never decreases
the weight: W (v + B(t)) ≥ W (v) by a similar reasoning along with self-similar properties of the Sierpinski triangle.
Therefore, one obtains W (v) ≥ W (B(tmin)) for p = 2.
It is worth looking at another example for p = 3 and m = 2:

B(2) = (1, 2, 1, 0, 0, 0, 0, 0, 0), B(5) = (1, 2, 1, 1, 2, 1, 0, 0, 0), B(7) = (1, 1, 0, 2, 2, 0, 1, 1, 0)

B(2) + B(5) + B(7) = (0, 2, 2, 0, 1, 1, 1, 1, 0).

Then, we notice
 W (B(2) + B(5) + B(7)) ≥ W (B(2))

and the lemma holds. The proof for p > 2 is non-trivial, and is presented in appendix B 1.

Principal vectors for fractal codes: Note that the Sierpinski triangle B and principal vectors B(t) appear when
one chooses the following initial condition in fractal codes:

x(0) = (1, 0, 0, · · · )

where the entire spin conﬁguration may be represented as an L × 2L matrix:

[
B, 0] =
 






 B(0), ⃗0
B(1), ⃗0
... ...
B(L − 1), ⃗0









where 0 represents an L × L zero matrix and ⃗0 represents an L-component zero vector.
 11

While the fractal codes are deﬁned as an L × 2L matrix for t = 0, · · · , L − 1, one may naturally generalize the
deﬁnition of fractal codes for t = 0, · · · , 2L − 1 as a 2L × 2L matrix. Then, the spin conﬁguration generated from
x(0) = (1, 0, 0, · · · ) can be expressed as the following 2L × 2L matrix:

[B, 0
B, B

]
 =
 












 B(0), ⃗0
... ...
B(L − 1), ⃗0
B(0), B(0)
... ...
B(L − 1), B(L − 1)













 (23)

where the (t + L)-th raws are given by (B(t), B(t)) due to Fact. 1. For a later purpose, it is convenient to redeﬁne
principal vectors as 2L-component vectors instead of L-component vectors:

B(t) ← (B(t),⃗0)

B(t + L) ← (B(t), B(t)) (24)

for t = 0, · · · , L − 1, obtaining a complete set of 2L principal vectors. Note that these redeﬁned principal vectors are
all independent, and still obey lemma 2.

Time evolution: We have analyzed a spin conﬁguration arising from an initial condition x(0) = (1, 0, 0, 0, · · · ).
Redeﬁned 2L-component principal vectors can be used for decomposing arbitrary initial conditions in fractal codes:

x(0) =
 2L−1∑

t=0 c(t)B(t) (mod p). (25)

Recall that x(0)r = 0 for r ≥ L due to the boundary condition in Eq. (17), and thus, c(t) = 0 for t ≥ L. Then, the
initial condition can be decomposed as follows

x(0) =
 L−1∑

t=0 c(t)B(t) (mod p) (26)

by using B(t) with t = 0, · · · , L − 1 only. Therefore, the t-th raw x(t) can be represented as follows

x(t) =
 L−1∑

τ =0 c(τ )B(τ + t) (mod p) (27)

since the time evolution rule of fractal codes is linear.

Code distances: Finally, we prove theorem 2. In order to show d = L
D(2)
p , one needs to prove that the minimal
Hamming distance between all the pairs of codewords is equal to L
D(2)
p . This problem can be simpliﬁed further since
fractal codes are linear. Let us represent the spin conﬁguration generated from an initial condition v as V(v). Then,
the Hamming weight between two spin conﬁgurations V(v) and V(v′) is given by

W (V(v) + V(v′)) = W (V(v + v′)) (28)

where v + v′ is computed modulo p. Since fractal codes are linear:

V(v), V(v′) ∈ C(2)
p → V(v + v′) ∈ C(2)
p (29)

12

where C(2)
p is the codeword space, one only needs to prove

d ≡ min
v̸=⃗0 W (V(v)) = L
D(2)
p (30)

by ﬁnding a spin conﬁguration V(v) with the lowest weight.
The weight of a spin conﬁguration V (x(0)) generated from an initial condition x(0) is given by

W (V(x(0))) =
 L−1∑

t=0 W (x(t)).

We denote the smallest t such that c(t) ̸= 0 as tmin. Then, due to lemma 2, we have

W (x(t)) ≥ W (B(tmin + t)),

which leads to
 L−1∑

t=0 W (x(t)) ≥
 L−1∑

t=0 (B(tmin + t)).

Since W (B(t + L)) = 2W (B(t)) for t ≥ L due to the self-similarity, we have

L−1∑

t=0 (B(tmin + t)) ≥
 L−1∑

t=0 (B(t)) = L
D(2)
p .

The bound is tight for x(0) = (1, 0, · · · ). This completes the proof of theorem 2.

Comments: The reason why we limit our considerations to spin conﬁgurations obeying the boundary term Eq. (17)
comes from a certain technical diﬃculty. For p = 2 and an initial condition (x(0)0, · · · , x(0)2L−1) = (1, · · · , 1), the
resulting spin conﬁgurations are (x(t)0, · · · , x(t)2L−1) = (0, · · · , 0) for t > 0 which would lead to d = 2L. To avoid
this diﬃculty, we need Eq. (17). This issue is closely related to the irreversibility of cellular automaton.

III. THREE-DIMENSIONAL FRACTAL CODE

The construction of two-dimensional fractal codes can be generalized to higher-dimensional systems (D > 2)
straightforwardly. In this section, we introduce the three-dimensional version of fractal codes and show the asymptotic
saturation of the local code bound for D = 3.

A. Basic properties of the three-dimensional Sierpinski triangle

We begin by recalling basic properties of the three-dimensional Sierpinski triangle. It is convenient to represent
the Sierpinski triangle as an L × L × L tensor with L = p
m, denoted by B (see Fig. 7). Entries of B are denoted as
B(t)r(1),r(2) for t, r(1), r(2) = 0, · · · , L − 1. Then, the Sierpinski triangle arises by taking the following entries:

B(t)r(1),r(2) = tCr(1) · t−r(1)Cr(2) = t!
r(1)!r(2)!(t − r(1) − r(2))! (mod p). (31)

Note that entries B(t)r(1),r(2) obey the following constraint:

B(t + 1)r(1),r(2) = B(t)r(1),r(2) + B(t)r(1)−1,r(2) + B(t)r(1),r(2)−1 (mod p) (32)

13

FIG. 7: Three-dimensional Sierpinski triangle. The example above shows the case with p = 2 and m = 2.

where we set periodic boundary conditions for r(1) and r(2). We call B the Pascal tensor.
By denoting the t-th layer of B as B(0, t), the Pascal tensor B can be represented as follows:

B =
 






 B(0, 0)
B(0, 1)
...
B(0, L − 1)







 . (33)

For example, with p = 2 and m = 2, one has
 B =
 







B(0, 0)
B(0, 1)
B(0, 2)
B(0, 3)








where
 B(0, 0) =
 







1, 0, 0, 0
0, 0, 0, 0
0, 0, 0, 0
0, 0, 0, 0







 B(0, 1) =
 







1, 1, 0, 0
1, 0, 0, 0
0, 0, 0, 0
0, 0, 0, 0








B(0, 2) =
 







1, 0, 1, 0
0, 0, 0, 0
1, 0, 0, 0
0, 0, 0, 0






 B(0, 3) =
 







1, 1, 1, 1
1, 0, 1, 0
1, 1, 0, 0
1, 0, 0, 0







 .
 14

One can view B as a history of time-evolution of an initial condition

B(0, 0) =
 







1, 0, · · · , 0
0, 0, · · · , 0
... ... . . . 0
0, 0, 0, 0









according to the update rule in Eq. (32):

B(0, 0) → B(0, 1) → · · · → B(0, L − 1). (34)

Fractal dimensions: To compute fractal dimensions of the Sierpinski triangle, we represent t, r(1) and r(2) in
p-adic forms:
 r(1) = (r(1)
m r(1)
m−1 · · · r(1)
1 )p, r = ∑

m′=1 p
m′−1rm′

r(2) = (r(2)
m r(2)
m−1 · · · r(2)
1 )p, r = ∑

m′=1 p
m′−1rm′

t = (tmtm−1 · · · t1)p, t = ∑

m′=1 pm
′−1tm′.

From lemma 1, entries B(t)r(1),r(2) can be expressed as follows:

B(t)r(1),r(2) =
 m∏

m′=1 tm′ C
r(1)
m′ · tm′ −r(1)
m′ C
r(2)
m′ (mod p). (35)

Then, one has
 B(t)r(1),r(2) ̸= 0 (mod p) iﬀ tm′ ≥ r(1)
m′ and tm′ − r(1)
m′ ≥ r(2)
m′ for all m
′. (36)

There are only p(p + 1)(p + 2)/6 possible combinations of (tm′, r(1)
m′ , r(2)
m′ ) satisfying the above condition for each m
′.
Therefore, fractal dimensions of three-dimensional Sierpinski triangle are given as follows:

Corollary 2 (Fractal dimension). Let W (B) denote the number of non-zero entries in B. Then, one has

W (B) = ( p(p + 1)(p + 2)
6
 )m = L
D(3)
p (37)

where the fractal dimension of the Pascal matrix B is given by

D(3)
p = log ( p(p + 1)(p + 2)
6
 ) / log p. (38)

B. Deﬁnition of three-dimensional fractal codes

Next, we give a precise deﬁnition of three-dimensional fractal codes. We consider a three-dimensional cubic lattice
with n = L × 2L × 2L spins where spins are p-dimensional and L = p
m. Each spin is labeled by “time” t and two
“positions” r(1) and r(2) with t = 0, · · · , L − 1 and r(1), r(2) = 0, · · · , 2L − 1. We set periodic boundary conditions on
all the surfaces which are parallel to the time axis. The admissible spin conﬁgurations obey the following constraint:

x(t + 1)r(1),r(2) = x(t)r(1)−1,r(2) + x(t)r(1),r(2)−1 + x(t)r(1),r(2) (mod p) (39)

where x(t)r(1),r(2) = 0, · · · , p − 1 represents the spin value at (t, r(1), r(2)). Spin conﬁgurations may be uniquely
speciﬁed by “initial conditions” x(0) with x(0)r(1),r(2) = 0, · · · , p − 1, which may be considered as 2L × 2L matrices.

15

We further limit ourselves to spin conﬁgurations which satisfy the following initial condition:

x(0)r(1),r(2) = 0 for r(1) + r(2) ≥ L, (40)

and denote a space of spin conﬁgurations speciﬁed by this condition as C (3)
p . Our main result is summarized in the
following theorem:

Theorem 3 (Three-dimensional fractal code). For the codeword space C (3)
p , let k be the number of encodable p-
dimensional spins and d be the code distance of the code. Then, we have

k = L(L + 1)
2 , d = L
D(3)
p (41)

where
 D(3)
p = log ( p(p + 1)(p + 2)
6
 ) / log(p). (42)

When D = 3, the fractal dimension goes to three: D(3)
p → 3 for p → ∞. Therefore, the code saturates the bound
kd1/3 ≤ O(n) in Eq. (2) for D = 3 asymptotically.

C. Principal matrix

Finally, we give the proof of theorem 3. A key idea is to generalize the notion of principal vectors and introduce
principal matrices which will be useful in decomposing spin conﬁgurations on each layer. An inequality for principal
vectors in lemma 2 is also generalized to an inequality for principal matrices.

Principal vectors: Recall that we represented the Pascal tensor B in terms of its t-th layers B(0, t):

B =
 







B(0, 0)
B(0, 1)
...
B(0, t)






 .

Matrices B(0, t) are closely related to principal vectors B(t). To see this point, we further expand matrices B(0, t) as
follows:
 B(0, t) =
 






 B(0, t)0
B(0, t)1
...
B(0, t)L−1






 (43)

where B(0, t)j are L-component vectors with

B(0, t)j = (B(0, t)0,j, B(0, t)1,j, · · · , B(0, t)L−1,j). (44)

For example, when p = 2 and m = 2, we have
 B(0, 3) =
 







1, 1, 1, 1
1, 0, 1, 0
1, 1, 0, 0
1, 0, 0, 0







 ,
 16

and
 B(0, 3)0 = (1, 1, 1, 1), B(0, 3)1 = (1, 0, 1, 0)

B(0, 3)2 = (1, 1, 0, 0), B(0, 3)3 = (1, 0, 0, 0).

Therefore, one may represent B(0, 3) as follows:
 B(0, 3) =
 







B(3)
B(2)
B(1)
B(0)









where B(0), B(1), B(2) and B(3) are principal vectors. Similarly, one has

B(0, 2) =
 







1, 0, 1, 0
0, 0, 0, 0
1, 0, 0, 0
0, 0, 0, 0







 =
 







B(2)
0
B(0)
0
 





 .

As examples above show, matrices B(0, t) can be represented in terms of principal vectors B(t):

Lemma 3 (Principal matrix). The t-th layer matrix B(0, t) can be represented as

B(0, t) =
 






 B(t)0 · B(t)
B(t)1 · B(t − 1)
...
B(t)L−1 · B(t − L + 1)






 (45)

As an example, let us represent B(0, 6) for p = 2 and m = 3 (see Fig. 8):

B(6) = (1, 0, 1, 0, 1, 0, 1, 0), B(0, 6) = (B(6),⃗0, B(4),⃗0, B(2),⃗0, B(0),⃗0)T

where ⃗0 represents vectors with zero entries. Similarly, we can represent B(0, 7) for p = 3 and m = 2 as follows:

B(7) = (1, 1, 0, 2, 2, 0, 1, 1, 0)

B(0, 7) = (B(7), B(6),⃗0, 2B(4), 2B(3),⃗0, B(1), B(0),⃗0)T .

It is worth representing all the matrices B(0, t) at once as in Fig. 8(b). In B(0, t), principal vectors B(0), · · · , B(t)
are distributed with weights corresponding to a principal vector B(t).

Principal matrix: So far, we have analyzed the spin conﬁguration generated by the following initial condition:

B(0, 0) ≡
 







B(0)
0
0
0
 





 . (46)

Here, we consider spin conﬁgurations generated by other initial conditions:

B(a, 0) ≡
 







B(a)
0
0
0
 





 (for a = 0, · · · , L − 1), (47)

and denote the t-th layer of the spin conﬁguration generated by B(a, 0) as B(a, t). We call B(a, t) principal matrices.
One may represent principal matrices B(a, t) explicitly as follows:
 17

FIG. 8: (a) Shorthand notations of B(0, 6) for p = 2 and m = 3, and B(0, 7) for p = 3 and m = 2. (b) Principle matrices and

principal vectors.

Lemma 4 (Principal matrix). A principal matrix B(a, t) can be represented as

B(a, t) =
 






 B(t)0 · B(t + a)
B(t)1 · B(t + a − 1)
...
B(t)L−1 · B(t + a − L + 1)






 (48)

where B(τ + L) = 2B(τ ) for 0 ≤ τ < L.
 18

Below, we show some examples. For p = 2 and m = 2, we have:

B(0, 0) =
 







B(0)
0
0
0
 





 , B(0, 1) =
 







B(1)
B(0)
0
0
 





 , B(0, 2) =
 







B(2)
0
B(0)
0
 





 , B(0, 3) =
 







B(3)
B(2)
B(1)
B(0)









B(1, 0) =
 







B(1)
0
0
0
 





 , B(1, 1) =
 







B(2)
B(1)
0
0
 





 , B(1, 2) =
 







B(3)
0
B(1)
0
 





 , B(1, 3) =
 






 0
B(3)
B(2)
B(1)









B(2, 0) =
 







B(2)
0
0
0
 





 , B(2, 1) =
 







B(3)
B(2)
0
0
 





 , B(2, 2) =
 






 0
0
B(2)
0
 





 , B(2, 3) =
 






 0
0
B(3)
B(2)









B(3, 0) =
 







B(3)
0
0
0
 





 , B(3, 1) =
 






 0
B(3)
0
0
 





 , B(3, 2) =
 






 0
0
B(3)
0
 





 , B(3, 3) =
 






 0
0
0
B(3)







 .

For p = 3 and m = 1, we have

B(0, 0) =
 




B(0)
0
0
 


 , B(0, 1) =
 




B(1)
B(0)
0
 


 , B(0, 2) =
 



 B(2)
2B(1)
B(0)
 




B(1, 0) =
 




B(1)
0
0
 


 , B(1, 1) =
 




B(2)
B(1)
0
 


 , B(1, 2) =
 




2B(0)
2B(2)
B(1)
 




B(2, 0) =
 




B(2)
0
0
 


 , B(2, 1) =
 




2B(0)
B(2)
0
 


 , B(2, 2) =
 




2B(1)
B(0)
B(2)
 


 .

Inequality for principal matrix: One can see that principal matrices B(a, t) are all independent, and an arbitrary
L × L matrix can be decomposed uniquely by B(a, t):

v = ∑

a,t c(a, t)B(a, t). (49)

Here, we deﬁne the following sets:

R0(v) = {(a, t) : c(a, t) ̸= 0}

R1(v) = {(a, t) ∈ R0 : a + t ≤ a
′ + t
′ for all (a
′, t
′) ∈ R0}

R2(v) = {(a, t) ∈ R1 : t ≤ t′ for all (a
′, t
′) ∈ R1}.
 (50)

Note that R2 ⊆ R1 ⊆ R0, and there is only one element in R2. Examples of R0, R1 and R2 are shown in Fig. 9.
Then, for the weight of the initial condition, we have the following inequality:
 19

FIG. 9: Examples of R0, R1 and R2. R0 is a set of all shaded sites. R1 is a set of sites with minimal a + t. R2 is a subset of

R1 with minimal t.

Lemma 5 (Inequality on principal matrices). For a matrix

v = ∑

a,t c(a, t)B(a, t) (51)

where c(a, t) = 0 for all (a, t) with a + t ≥ L, let (a
′, t
′) ∈ R2(v). Then, we have

W (v) ≥ W (B(0, t
′)) . (52)

As an example, let us consider the following linear decomposition:

v = B(2, 3) + B(5, 3) + B(1, 4) + B(0, 8).

Then, we have
 R = {(2, 3), (5, 3), (1, 4), (0, 8)}, R1 = {(2, 3), (1, 4)}, R2 = {(2, 3)}

and
 W (v) ≥ W (B(0, 3)).

The proof of lemma 5 is given in appendix B 2.

Code distance: Finally, we prove theorem 3. One can naturally extend the deﬁnition of principal matrices B(a, t)
for 2L × 2L matrices by considering L × 2L × 2L fractal codes. Then, lemma 5 holds for redeﬁned principal matrices
after changing L → 2L. Since the initial condition x(0) obeys Eq. (40), one can decompose it as follows:

x(0) = ∑

a+t≤L c(a, t)B(a, t), (53)

20

and its time-evolution is given by
 x(t) = ∑

a+τ ≤L c(a, τ )B(a, τ + t).

Let (a
′, t
′) = R2(x(0)). Then, from lemma 5, one has

W (x(t)) ≥ W (B(0, t
′ + t)).

Therefore, one has
 L−1∑

t=0 W (x(t)) ≥
 L−1∑

t=0 W (B(0, t + t
′)) ≥
 L−1∑

t=0 W (B(0, t)) = LD(3)
p

which completes the proof.
 IV. HIGHER-DIMENSIONAL FRACTAL CODE

Finally, we brieﬂy discuss the D-dimensional fractal codes for D > 3. We consider a D-dimensional hypercubic
lattice with n = L × · · · × L spins with L = pm. Each spin is labeled by “time” t and “positions” r(1), · · · , r(D−1),
and we set periodic boundary conditions on all the D − 1-dimensional surfaces which are parallel to the time axis.
The admissible spin conﬁgurations of the lattice obey the following constraint:

x(t + 1)r = x(t)r +
 D−1∑

j=1 x(t)r−ej (mod p) 0 ≤ t ≤ L − 2 (54)

where r = (r(1), · · · , r(D−1)), and ej is a unit vector in the r(j) direction. In addition, we limit ourselves to spin
conﬁgurations which satisfy the following initial condition:

x(0)r = 0 for
 D−1∑

j=1 r(j) ≥ L, (55)

and denote a space of spin conﬁgurations speciﬁed by the condition above as C (D)
p . Then, we have the following
theorem.

Theorem 4 (Higher-dimensional fractal code). For the codeword space C (D)
p , let k be the number of encodable spins
and d be the code distance of the code. Then, we have

k = L(L + 1) · · · (L + D − 2)
(D − 1)! , d = LD(D)
p (56)

where
 D(D)
p = log ( p(p + 1) · · · (p + D − 1)
D!
 ) / log(p). (57)

The fractal dimension D(D)
p goes to D: D(D)
p → D for p → ∞. Therefore, the code saturates the bound kd
1/D ≤
O(n) in Eq. (2) asymptotically for arbitrary D.
Here, we give a sketch of the proof since it is complicated, but straightforward to obtain the proof. Recall that we
have deﬁned two-dimensional principal matrices from one-dimensional principal vectors. We deﬁne (D−1)-dimensional

21

principal tensors recursively from (D − 2)-dimensional principal tensors. In particular, a (D − 1)-dimensional principal
tensor B(r, t) with (D − 2)-dimensional vector r is deﬁned as the time evolution of B(r, 0):

B(r, 0) =
 







B(r)
0
...
0
 





 (58)

where B(r) is a (D − 2)-dimensional principal tensor.
With these independent (D − 1)-dimensional principal tensors B(r, t), one can decompose an arbitrary (D − 1)-
dimensional tensor uniquely. One can obtain the following inequality to bound the weight of (D − 1)-dimensional
tensors:

Lemma 6. For
 v = ∑

r,t c(r, t)B(r, t) where c(r, t) = 0 for all t +
 D−2∑

j=1 rj ≥ L, (59)

we deﬁne the following sets with RD−1 ⊆ · · · ⊆ R1 ⊆ R0:

R0 = {
(r1, · · · , rD−1) : c(r1, · · · , rD−1) ̸= 0
}

Ra = {
(r1, · · · , rD−1) ∈ Ra−1 :
 D−1∑

j=a rj ≤
 D−1∑

j=a r′
j for all (r′
1, · · · , r′
D−1) ∈ Ra−1}
. (60)

Then, for (r′
1, · · · , r′
D−1) ∈ RD−1, one has
 W (v) ≥ W (B(0, r′
D−1)) (61)

This bound can be proven recursively by using lemma 5. As a result of this bound, one can easily obtain a lower
bound for the weight of arbitrary spin conﬁgurations arising in D-dimensional fractal codes.

V. DISCUSSION AND OPEN QUESTIONS

In this paper, we have presented fractal codes which asymptotically saturates the local code bound. There are a
number of interesting open questions and future problems, and this section is devoted to discussions and speculations
on them.
 A. Open questions on local codes

An immediate question is whether a local code which “tightly” saturates the bound may exist or not. While our
discussion was limited to local codes based on the Sierpinski triangle, there are other interesting local codes with
various fractal spin conﬁgurations. Time evolutions of arbitrary cellular automaton, based on local update rules, can
be physically realized as local codes, and lead to fractal spin conﬁgurations when update rules are linear [10]. The
main technical ﬁnding in this paper is that the code distance d of the Sierpinski-type fractal code grows with fractal
dimensions of the Sierpinski triangle. Whether code distances of generalized fractal codes grow with fractal dimensions
of original fractal geometries or not may be an interesting open problem. For instance, the following update rule

x(t + 1)r = x(t)r−1 + x(t)r + x(t)r+1 (mod 2) (62)

22

leads to a fractal geometry with a fractal dimension log 1+√5
log 2 . Then a naturally arising question is whether d ∼

O(L
 log 1+
√5
log 2 ) or not. Another important question concerns the necessity of boundary terms for local codes generated by
reversible cellular automaton. Finally, one may also consider local codes generated by non-linear cellular automaton.
For instance, Wolfram’s rule 30 cellular automaton is known to generate pseudo-random spin conﬁgurations [10]
which may achieve d ∼ O(L
2). Also, such a model may be interesting as a toy model of spin glasses without quenched
disorder.
While our discussion in this paper is limited to classical error-correcting codes, a similar question for quantum error-
correcting codes is also of practical and fundamental importance in quantum information processing. The “quantum”
information storage capacity for local quantum codes was found in [5]:

kd 2
D−1 ≤ O(n) (63)

where d is the “quantum” code distance. For D = 2, the Toric code is known to saturate the bound, while the problem
of ﬁnding a capacity saturating code for D = 3 is currently open. Recently, there have been signiﬁcant progresses in
systematically studying coding properties of local quantum codes with translation symmetries [11–16]. In particular, a
three-dimensional local quantum code with anti-commuting pairs of fractal-like logical operators has been found [14].
A general framework to extend “classical” fractal codes to “quantum” fractal codes has been recently obtained along
with theoretical tools to compute their code distances [17].

B. Physical implementation

Before discussing the feasibility of physically implementing fractal codes, we need to brieﬂy discuss how bits of
information are stored in memory devices that are currently used. First of all, in order to store bits of information
securely, one needs to create some stable physical entities with multiple degrees of freedom. Such physical systems may
viewed as stable “spins” whose sizes are often much larger than sizes of actual single spins or quanta. For instance, in
hard disk drives, ferromagnetic materials, physical realizations of repetition codes via local Hamiltonians, are used as
stable spins. (Encoding bits of information into actual single spins is technically challenging, and only experimental
demonstrations in highly controlled systems are available at this moment). Based on these stable spins, one further
encodes bits of information using error-correcting codes by considering stable spins as basic building blocks. These
error-correcting codes, used for further encoding bits of information into stable spins, are not necessary supported by
local interaction terms since stable spins do not need to be protected by Hamiltonians. For such error-correcting codes
without locality, the ultimate bound on information storage capacity is the well-celebrated Shannon bound. It is well
known that some error-correcting codes saturate the Shannon bound while admitting eﬃcient decoding of encoded
information. Conventional theory of error-correcting codes focuses on the art of encoding based on stable qubits. On
the other hand, a problem of ﬁnding good local codes focuses on creating stable spins via local Hamiltonians, with
a hope of creating stable spins which are more beneﬁcial than ferromagnets, and does not focus on encoding bits of
information based on stable spins.
The biggest obstacle in physically implementing fractal codes is that it involves three-body interactions which may
not exist naturally in physical systems. Yet, one may be able to ﬁnd two-body classical Hamiltonian which leads to
the same codeword space as fractal codes via simple magnetic interactions. Another possible approach may be to
simulate three-body terms through two-body terms perturbatively [18] or non-perturbatively [19] by using quantum
Hamiltonians. Finally, it may be possible that Hamiltonians of fractal codes appear as eﬀective Hamiltonians of some
known interacting spin systems.
Encoding and decoding bits of information in an eﬃcient and physically implementable way is also an important
problem from a practical viewpoint. From coding theory perspective, practical encoding and decoding algorithm may

23

exist for local codes since local codes can be viewed as low-density parity-check codes (LDPCs) [20]. A particularly
interesting approach, motivated by physical arguments, is the so-called renormalization group (RG) decoding algo-
rithm [21]. These algorithms, however, require some “computations” to write and read out bits of information. This
is in a strong contrast with the fact that, for a ferromagnet, one can easily write and read a single bit of information
just by adding external magnetic ﬁelds and by measuring the total magnetization, without any computations. One
needs to ﬁnd encoding and decoding algorithm for fractal codes which are physically motivated and are implementable
without any non-local computations.
 C. As a many-body spin system

Studies on physical properties of fractal codes may also be of fundamental interest in condensed matter physics
community. Searching for novel local codes is fundamentally akin to searching for novel quantum phases as local codes
can be viewed as representatives of quantum phases with mass gap [12]. Most of conventional many-body spin systems,
such as a ferromagnet, are known to have continuous scale symmetries where ground states look exactly the same even
after changing the length scale of the system. This observation led to the development of the renormalization group
theory for classifying quantum phases arising in many-body systems. In this light, fractal codes are unconventional
since their ground states do not have continuous scale symmetries, but have only discrete scale symmetries where
ground states of fractal codes with p-dimensional spins look the same only under the scale transformations by powers
of p. Clearly, systems with discrete scale symmetries are beyond descriptions of topological ﬁeld theory, and searches
for their eﬀective theories may be an interesting future problem. Many-body physics with discrete scale symmetries
is a largely uncharted research area except some pioneering works [22, 23].
While our discussion was limited to the ground state properties of fractal codes, properties of quasi-particle excita-
tions in fractal codes are also interesting. It should be noted that thermal relaxation dynamics of a fractal code with
p = 2 was studied in [8] more than a decade ago where a fractal spin model was originally proposed as a toy model
which may exhibit spin-glass like relaxation dynamics even without quenched disorder. In particular, it was shown
that diﬀerent ground states of fractal spin systems are separated by energy barriers which grow logarithmically with
respect to the system size.
 D. Information storage capacity in other physical systems

Another intriguing question concerns a connection between the Bekenstein bound and the local code bound. The
Bekenstein bound is a quantum mechanical bound on the degree of freedom on a ﬁnite physical space, resulting from
the uncertainty principle. When the Bekenstein bound is applied to systems with gravity, one can derive the area
law for black hole entropies by requiring that the size of an object does not exceed the Schwarzschild radius and can
ﬁnd that entropies are upper bounded roughly by A/ℓ2
p where A is the surface are of an object and ℓp is the Planck
length. This observation led to the holographic principle of black holes which essentially states that physical states
of black holes can be determined completely by the surface of black holes.
As for the local code bound, it is interesting to observe that an area law naturally arises in fractal codes; the
number of encoded bits k is area-like with k ∼ O(LD−1), while the code distance d is asymptotically volume-like
with d ∼ O(L
D−ϵ). In deriving the local code bound, only the locality of interaction terms on a discretized space
is assumed. It is interesting to note that, the area-law arising in fractal codes can be derived from purely classical
calculations while derivations of black hole area-law and entanglement entropy area-law both crucially require quantum
mechanics. A construction of fractal codes is, in some sense, rooted on the holographic principle where ground states
can be uniquely speciﬁed by spin values on the surface. However, a connection between fractal codes and black holes

24

has not been established.
In the present paper, our discussion has been constrained to the following three conditions; a) static Hamiltonian,
b) local interactions, and c) being frustration-free. There are a large number of pioneering works that addressed a
similar question without above three constraints. A problem of encoding bits of information into dynamically evolving
systems has been actively addressed in studies of neural networks. For instance, the Hopﬁeld model of neural network,
based on the Hebb rule, is capable of reliably storing a large amount of information which easily breaks the local
code bound if non-local couplings are allowed. In [24], G´acs presented a model of one-dimensional locally coupled
dynamical spin systems that is capable of storing one bit per site, and is still robust against small, but ﬁnite amount
of noises. This remarkable result by G´acs implies that dynamical systems are more powerful than static systems in
terms of information storage capacity. While we have limited our considerations only to frustration-free spin systems,
there are a large number of interesting frustrated spin systems including spin glasses and anti-ferromagnets which
may be useful in storing bits of information. Relations between spin glass systems and classical error-correcting codes
have been actively investigated where some classes of spin glasses with non-local couplings are known to saturate the
Shannon bound asymptotically [25].
 Acknowledgments

I thank Eddie Farhi and Peter Shor for support at MIT. I thank Sergey Bravyi, Patrick Hayden, Masahito Ueda and
John Preskill for comments and discussion. This work is supported in part by DOE Grant No. DE-FG02-05ER41360
and by Nakajima Foundation.
 Appendix A: Review of coding theory

We give a brief review of theory of classical error-correcting codes in the context of spin physics. We also give a
derivation of the local code bound, following [5]. A precise deﬁnition of frustration-free classical local Hamiltonians
is also given here.

Local code: Consider a D-dimensional hyper-cubic lattice of L × · · · × L spins whose spin values are 0 or 1. A
classical local Hamiltonian H can be written in the following form

H =
 m∑

a=1 Πa (A1)

where interaction terms Πa are supported locally inside some ﬁnite regions of ω × · · · × ω spins. Here, ω is referred
to as a range of interactions.
A Hamiltonian is said to be frustration-free when a energy ground state can be obtained by minimizing each
interaction term Πa independently. Without loss of generality, we assume that the smallest value of Πa is zero for all
a; Πa ≥ 0. Then, a ground state s of a frustration-free Hamiltonian H satisﬁes

Πa(s) = 0, for all a. (A2)

We call such classical frustration-free Hamiltonians local codes. Ground states of local codes can be viewed as binary
strings, and form the codeword space (the ground space) C:

C = {s : Πa(s) = 0, ∀a}. (A3)

The number of encoded logical bits is k = log2 dim C, and there are 2k degenerate ground states in a local code.
 25

Code distance: Let us estimate how reliably bits of information can be stored in the presence of errors. Suppose
one encodes bits of information into a ground state s0. Then, consider an error which ﬂips some spins, giving rise to
a spin conﬁguration denoted by serror ̸= s0. If the number of ﬂipped spins is small, serror will be still close to the
original ground state s0, so one may be able to recover the encoded information. If the number of ﬂipped spins is large,
serror may be closer to other ground states sj (j ̸= 0), so one may not be able to recover the encoded information.
Based on this observation, it is convenient to introduce the Hamming distance between two binary strings s and s′

which is the number of diﬀerent spin values in s and s
′, corresponding to the weight of s + s
′ (mod 2). The Hamming
distance is the number of spin ﬂips necessary to change from s to s
′, and the code distance d is deﬁned as the minimal
Hamming distance between all the possible pairs of ground states:

d = min w(s + s
′), ∀s, s
′ ∈ C (A4)

where s ̸= s
′.

Singleton bound: To derive the local code bound, it is convenient to recall a certain fundamental upper bound
on classical error-correcting codes, called the Singleton bound:

n − d + 1 ≥ k. (A5)

We emphasize that this bound holds without assuming the geometric locality of Πa (i.e. for an arbitrary interaction
range ω). The Singleton bound can be proven by considering a bi-partition of the entire system into A and B where
B consists of d − 1 spins and A consists of n − d + 1 spins. Suppose that there exist two ground states s and s
′ whose
spin values inside A are exactly the same: s|A = s
′|A. If s and s
′ are diﬀerent ground states, one can obtain s
′ from s
just by ﬂipping spins only inside B. But this contradicts with the fact that the code distance is d while the number
of spins inside B is d − 1. So, s and s
′ must be the same ground state. This implies that, if s ̸= s
′, their spin values
in A must be diﬀerent: s|A ̸= s
′|A. Therefore, the number of logical bits k is upper bounded by the number of spins
in A, which is n − d + 1.

Local code bound: One can extend the Singleton bound for local codes by imposing geometric locality on
interaction terms Πa. The key idea in proving the Singleton bound is to remove a region B whose volume is smaller
than d, and upper-bound the number of logical bits k by the number of spins in A. To prove the local code bound,
we think of a bi-partition into A and B where B consists of hyper-cubic blocks B = B1 · · · Bm whose sizes are smaller
than d and their separation is at least ω so that interaction terms Πa may overlap with at most one block at the same
time. We think of two ground states s and s
′ such that s|A = s
′|A. Then, one can obtain s
′ from s by ﬂipping spins
inside B = B1 · · · Bm where we denote sets of spins inside Bj which are to be ﬂipped by Ej ⊆ Bj. Let us consider a
ground state s1 which can be obtained from s by ﬂipping spins in E1. Then, due to the locality of interaction terms
Πa, s1 is also a ground state. Since the size of B1 is smaller than d, E1 must be a null set. Similarly, one has Ej = 0
for all j and thus, s = s′. This implies that if s ̸= s
′, their spin values in A must be diﬀerent: s|A ̸= s
′|A, and one has

vA ≥ k (A6)

where vA is the number of spins in A.
One needs to ﬁnd an upper bound on vA by removing as many blocks Bj as possible while keeping the separations
between blocks Bj to be at least ω. Let us think of cubic regions Bj whose linear length is of order ℓ ≡ d
1/D. Then,
the number of blocks which can removed is of order ( L
ω + ℓ
 )D . (A7)

26

Therefore, vA is upper bounded roughly by
 vA ≤ L
D − ℓ
D · ( L
ω + ℓ
 )D . (A8)

This leads to
 n ≥ k (ω + ℓ)
D

(ℓ + ω)D − ℓD , ℓ = d1/D. (A9)

This leads to the local code bound kd1/D ≤ O(n).

Appendix B: Proofs of some lemmas

In this appendix, we give proofs of some lemmas used in the main discussion.

1. Proof of lemma 2

The proof of lemma 2 consists of several steps.

Inverse matrices: We begin by ﬁnding the inverse matrix B
−1 of the Pascal matrix B:

Lemma 7. The inverse matrix is given by:

B−1(t)r = B(L − 1 − r)L−1−t (B1)

where B−1(t)r represents an entry of B
−1 at (t, r). In particular, its entries are given by

B−1(t)r = L−1−rCL−1−t = (−1)
t+r tCr = (−1)t+rB(t)r. (B2)

Examples of inverse matrices are shown in Fig. 10.

Proof. Since B−1(t)r = B(L − 1 − r)L−1−t, we have

B−1(t)r = L−1−rCL−1−t = (pm − t) · · · (pm − 1 − r)
(t − r)!

= (−t)(−t + 1) · · · (−1 − r)
(t − r)!

= (−1)t−r(r + 1) · · · (t − 1)t
(t − r)!

= (−1)t+rt!
r!(t − r)!

= (−1)
t+r tCr

for t ≥ r where all the calculations are carried out modulo p. It is straightforward to see that B · B
−1 = I with some
calculations.

The following lemma is useful in ﬁnding the power B
c of the Pascal matrix B:

Lemma 8. A matrix B
c is generated by the following modiﬁed rule

x(t + 1)r = x(t)r−1 + cx(t)r (mod p) 0 ≤ t ≤ L − 2 (B3)

with an initial condition x(0) = (1, 0, · · · ).
 27

FIG. 10: Examples of the Pascal matrices and its inverse matrices. Only the shaded regions with t + r = odd may have diﬀerent

entries in B and B
−1. The inverse matrices can be obtained by reﬂecting the original matrices along the arrows shown above.

(a) p = 3 and m = 2. (b) p = 7 and m = 1.

By modifying the local rule for spin conﬁgurations, one can obtain powers of the Pascal matrix. An example is
shown in Fig. 11. Here, we notice that B
p = I since the update rule is reduced to

x(t + 1)r = x(t)r−1 (mod p) 0 ≤ t ≤ L − 2. (B4)

Also, we notice that B
p−1 = B
−1 from B
p = I.

FIG. 11: Examples of powers of the Pascal matrix B for p = 5.

Proof. For simplicity of discussion, we only prove the lemma for B
2. Since

B(t)r = B(t − 1)r + B(t − 1)r−1,
 28

we have
 B2(t)r = ∑

a B(t)aB(a)r

= ∑

a (B(t − 1)a + B(t − 1)a−1)B(a)r

= B2(t − 1)r + ∑

a B(t − 1)a−1B(a)r

= B2(t − 1)r + ∑

a B(t − 1)aB(a + 1)r

= B2(t − 1)r + ∑

a (B(t − 1)aB(a)r + B(a)r−1)

= B2(t − 1)r + B2(t − 1)r + B2(t − 1)r−1 = 2B2(t − 1)r + B2(t − 1)r−1

where B(t)a = 0 for t < 0, and B(t)a = B(t)a+L if a < 0. Then, we notice that entries of B
2 obeys the rule in
Eq. (39) for c = 2. Therefore, B
2 can be generated from the rule for c = 2. A similar discussion leads to the proof for
an arbitrary c.

Submatrices of the Pascal matrix: The the Pascal matrix B is invertible since principal vectors B(t) are
pairwise independent. Similar properties holds for submatrices of B. We denote the Pascal matrix B for m = 1 as
B
(1):
 B
(1) =
 






 0C0, 0C1, 0C2, · · · 0Cp−1

1C0, 1C1, 1C2, · · · 1Cp−1
... ... ... ... ...

p−1C0, p−1C1, p−1C2, · · · p−1Cp−1






 (mod p) (B5)

which is a p × p matrix. Then, for submatrices of B
(1), we have the following lemma:

Lemma 9. Consider the following submatrix of B
(1):

A =
 






x0C0, x0C1, x0 C2, · · · x0 Ca

x1C0, x1C1, x1 C2, · · · x1Ca
... ... ... ... ...

xa C0, xa C1, xa C2, · · · xa Ca






 (B6)

where a < p and 0 ≤ x0 < x1 < · · · < xa < p. Then, A always has an inverse matrix A−1. Similarly, consider the
following submatrix of B
(1):
 A’ =
 







p−a−1Cy0 , p−a−1Cy1, p−a−1Cy2 , · · · p−a−1Cya
... ... ... ... ...

p−2Cy0 , p−2Cy1, p−2Cy2 , · · · p−2Cya

p−1Cy0 , p−1Cy1, p−1Cy2 , · · · p−1Cya
 





 (B7)

where 0 ≤ y0 < y1 < · · · < ya < p. Then, A’ always has an inverse matrix (A’)
−1.

The construction of A goes as follows. First, we choose an p × a submatrix from B
(1) on the left hand side of
B
(1) (a < p). Then, we pick up a raws to create an a × a matrix A. Similarly, to construct A’, we choose an a × p
submatrix on the bottom of B
(1), and pick up a columns to create an a × a matrix A’. Examples of such constructions
of submatrices are shown in Fig. 12.
 29

FIG. 12: Submatrices for p = 7.

It is worth looking at examples. Consider the case where p = 5. Then, we have

B
(1) =
 









1, 0, 0, 0, 0
1, 1, 0, 0, 0
1, 2, 1, 0, 0
1, 3, 3, 1, 0
1, 4, 1, 4, 1










 . (B8)

For a = 2 and x0 = 2, x1 = 3 and x2 = 4, we have

A =
 




1, 2, 1
1, 3, 3
1, 4, 1




 . (B9)

Since three vectors (1, 2, 1), (1, 3, 3) and (1, 4, 1) are independent (mod 5), A is invertible. For a = 2 and y0 = 1,
y1 = 2 and y2 = 3, we have
 A’ =
 




2, 1, 0
3, 3, 1
4, 1, 4




 (B10)

which is also invertible.

Proof. For simplicity of discussion, we present a proof only for A. First, recall that the Vandermonde matrix M has
the following well-known property:

M =
 







1, x0, x2
0, · · · , xa
0
1, x1, x2
1, · · · , xa
1
... ... . . . ...
1, xa, x2
a, · · · , xa
a






 , det(M) = ∏

0≤i<j≤a(xj − xi). (B11)

Therefore, the following vectors are independent when xi ̸= xj for all i and j:

(1, 1, · · · , 1), (x0, x1, · · · , xa) · · · (xa
0, x
a
1, · · · , x
a
a). (B12)

Now, let us consider the Vandermonde matrix modulo p. When 0 ≤ x0 < x1 < · · · < xa < p, the vectors above are
independent modulo p since the determinant of M computed modulo p is nonzero. Notice that our goal to prove that
the following vectors are independent modulo p:

(x0 C0, x1 C0, · · · , xa C0), (x0C1, x1C1, · · · , xa C1) · · · (x0Ca, x1Ca, · · · , xa Ca). (B13)

30

This is immediate since vectors in Eq. (B13) can be created by adding vectors in Eq. (B12). Therefore, A is invertible.
A similar proof works for A’ by using lemma 7.

Proof of lemma 2: Finally, we prove lemma 2. Due to the self-similar structures of the Pascal matrix B, it is
suﬃcient to prove the lemma for m = 1. Consider a decomposition

v = ∑

t c(t)B(t)

where tmin is the minimal integer such that c(t) ̸= 0. Then, the goal is to prove

W (v) ≥ W (B(tmin)).

We list all the integers r such that
 B(tmin)r ̸= 0 and vr = 0

and denote them as r1, · · · , ra. Then, the number of non-zero entries of vr for r ≤ tmin is W (B(tmin)) − a. Next, we
list all the integers r such that
 B(tmin)r = 0 and vr = 0

and denote them as r′
1, · · · , r′
b. Then, the number of non-zero entries of vr for tmin < r is (p − 1 − tmin) − b. Then,
we have
 W (v) = W (B(tmin)) − a + (p − 1 − tmin) − b

from a simple counting argument. Therefore, it suﬃces to prove that a + b ≤ p − 1 − tmin.
We next consider constrains on coeﬃcients c(t):

vr =
 p−1∑

t=0 c(t)B(t)r = 0 for r = r1, · · · , ra, r′
1, · · · , r′
b.

Recall that tmin is the minimal t such that c(t) ̸= 0 and c(t) = 0 for t < tmin. Then, the above constraints can be
concisely represented as follows:
 (A’)T ·
 






 c(tmin)
c(tmin + 1)
...
c(p − 1)
 





 = 0

where
 A’ =
 






 B(tmin)r1, · · · , B(tmin)ra , B(tmin)r′
1, · · · , B(tmin)r′
b
B(tmin + 1)r1, · · · , B(tmin + 1)ra , B(tmin + 1)r′
1 , · · · , B(tmin + 1)r′
b
... ... ... ... ... ...
B(p − 1)r1, · · · , B(p − 1)ra , B(p − 1)r′
1 , · · · , B(p − 1)r′
b
 





 .

Here, A’ is a (p − tmin) × (a + b) matrix. Notice that the rank of A’ is p − tmin when a + b ≥ p − tmin due to lemma 9.
In such cases, we have c(t) = 0 for all t which leads to a contradiction. Therefore, a + b < p − tmin. This leads to
W (v) ≥ W (Bmin), and completes the proof of lemma 2.
 31

2. Proof of lemma 5

Lemma 5 is an inequality concerning the weights of principal matrices. We begin by proving the following lemma.

Lemma 10. Consider a matrix
 v = ∑

a,t c(a, t)B(a, t) (B14)

where (c, t) = 0 for a + t ≥ L. Let v∗ be
 v∗ = ∑

(a,t)∈R1(v) c(a, t)B(a, t). (B15)

Then, one has
 W (v) ≥ W (v∗). (B16)

Proof. We decompose v as follows:

v = ∑

a+t=0 c(a, t)B(a, t) + ∑

a+t=1 c(a, t)B(a, t) + ∑

a+t=2 c(a, t)B(a, t) + · · · . (B17)

In particular, we set
 v = ∑

δ v(δ), v(δ) = ∑

a+t=δ c(a, t)B(a, t). (B18)

For simplicity of discussion, we consider the case where

v = v(δ) + v(δ+1).

v(δ) can be represented as follows:
 v(δ+1) =
 












 d(δ) · B(δ)
d(δ − 1) · B(δ − 1)
...
d(0) · B(0)
0
...
 













where d(0), · · · , d(δ) are some integers, and v(δ+1) can be represented as follows:

v(δ+1) =
 













d
′(δ + 1) · B(δ + 1)
d′(δ) · B(δ)
...
d
′(0) · B(0)
0
...
 












 32

where d
′(0), · · · , d
′(δ + 1) are some integers. Then, we have

v(δ) + v(δ+1) =
 
















d′(δ + 1) · B(δ + 1) + d(δ) · B(δ)
d′(δ) · B(δ) + d(δ − 1) · B(δ − 1)
...
d′(1) · B(1) + d(0) · B(0)
d
′(0) · B(0)
0
...
 
















Then, due to lemma 2, we have
 W (v) ≥ W (v(δ)).

The discussion above can be easily extended to general cases. This completes the proof.

Next, it is convenient to consider the transposes of principal matrices. Let us begin with an example for p = 2 and
m = 2:
 B(1, 1) =
 







B(2)
B(1)
0
0
 





 =
 







1, 0, 1, 0
1, 1, 0, 0
0, 0, 0, 0
0, 0, 0, 0







 .

Then, its transpose is
 B(1, 1)
T =
 







1, 1, 0, 0
0, 1, 0, 0
1, 0, 0, 0
0, 0, 0, 0







 =
 






 B(1)
B(0) + B(1)
B(0)
0
 





 .

Here, we apply lemma 10 to the transpose B(1, 1)T :

B(1, 1)T = (B(1, 1)
T )
(1) + (B(1, 1)T )
(2)

where
 (B(1, 1)T )
(1) =
 







B(1)
B(0)
0
0
 





 , (B(1, 1)T )
(2) =
 






 0
B(1)
B(0)
0
 





 .

Then, one has
 W (B(1, 1)) ≥ W ((B(1, 1)
T )
(1)).

By noticing
 (B(1, 1)T )
(1) = B(0, 1) =
 







B(1)
B(0)
0
0
 





 ,
 33

one has
 W (B(1, 1)) ≥ W (B(0, 1)).

As the example above shows, by considering the transpose of principal matrices, one can further lower bound on
the weight of principal matrices. For this purpose, the following lemma is particularly useful.

Lemma 11. Consider a transpose B(a, t)T of a principal matrix with a + t < L. For a decomposition of B(a, t)T in
terms of principal matrices:
 B(a, t)
T = ∑

a′,t′ c(a
′, t
′)B(a′, t, ), (B19)

one has
 R1(B(a, t)
T ) = {(0, t)}. (B20)

The proof of the lemma 11 is immediate by noticing the following fact:

Fact 2. The principal matrices B(0, t) are symmetric under the transpose:

B(0, t)T = B(0, t). (B21)

The principal matrix B(a, t) for a ̸= 0 is given by

B(a, t) = ∑

x T x−1
r(1) (B(a)x · B(0, t)), (B22)

and its transpose is given by
 B(a, t)
T = ∑

y T y−1
r(2) (B(a)x · B(0, t)), (B23)

We ﬁnally prove lemma 2. For a decomposition

v = ∑

a,t c(a, t)B(a, t),

from lemma 10, one has
 W (v) ≥ W (v∗).

Here, we consider the transpose of v∗. Then, for (a
′, t
′) ∈ R2(v), from lemma 11, one has

R1((v∗)
T ) = (0, t
′).

Therefore, we have
 W (v) ≥ W (v∗) = W ((v∗)
T ) ≥ W (B(0, t
′)).

This completes the proof.

[1] R. Landauer, Nature 335, 779 (1988).

[2] J. D. Bekenstein, Phys. Rev. D 23, 287 (1981).
 34

[3] S. Hawking, Commun. Math. Phys. 43, 199 (1975).

[4] L. Susskind, J. Math. Phys. 36, 6377 (1995).

[5] S. Bravyi, D. Poulin, and B. Terhal, Phys. Rev. Lett. 104, 050503 (2010).

[6] R. Penrose, in Quantum Theory and Beyond (Cambridge Univertity Press, 1971).

[7] C. Rovelli and L. Smolin, Phys. Rev. D 52, 5743 (1995).

[8] M. E. J. Newman and C. Moore, Phys. Rev. E 60, 5068 (1999).

[9] D. R. Chowdhury, S. Basu, I. S. Gupta, and P. P. Chaudhuri, IEEE Transactions on Computers 43, 759 (1994).

[10] S. Wolfram, A new kind of science (Wolfram Media Inc. Champaign., 2002).

[11] B. Yoshida and I. L. Chuang, Phys. Rev. A 81, 052302 (2010).

[12] B. Yoshida, Ann. Phys. 326, 15 (2011).

[13] B. Yoshida, Ann. Phys. 326, 2566 (2011).

[14] J. Haah, Phys. Rev. A 83, 042330 (2011).

[15] H. Bombin, arXiv:1107.2707.

[16] I. H. Kim, arXiv:1202.0052.

[17] B. Yoshida, in preparation.

[18] S. P. Jordan and E. Farhi, Phys. Rev. A 77, 062329 (2008).

[19] S. A. Ocko and B. Yoshida, Phys. Rev. Lett. 107, 250502 (2011).

[20] R. Gallager, IRE Trans. Inform. Theory 8, 21 (1962).

[21] G. Duclos-Cianci and D. Poulin, Phys. Rev. Lett. 104, 050504 (2010).

[22] V. Eﬁmov, Physics Letters B 33, 563 (1970).

[23] K. G. Wilson, Phys. Rev. D 3, 1818 (1971).

[24] P. G´acs, J. Stat. Phys. 103, 45 (2001).

[25] N. Sourlas, Nature 339, 693 (1989).
