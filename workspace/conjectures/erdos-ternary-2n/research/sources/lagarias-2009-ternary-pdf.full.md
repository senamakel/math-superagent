<!-- source: https://arxiv.org/pdf/math/0512006v4 | converted from PDF -->

arXiv:math/0512006v4  [math.DS]  11 Jul 2008
Ternary Expansions of Powers of 2

Jeﬀrey C. Lagarias1

Dept. of Mathematics
University of Michigan
Ann Arbor, MI 48109-1109

(To Mel Nathanson on his 60-th birthday)

(July 11, 2008 )

ABSTRACT

P. Erd˝os asked how frequently does 2n have a ternary expansion that omits the digit 2. He
conjectured that this holds only for ﬁnitely many values of n. We generalize this question
to consider iterates of two discrete dynamical systems. The ﬁrst considers truncated ternary
expansions of real sequences xn(λ) = ⌊λ2n⌋, where λ > 0 is a real number, along with its
untruncated version, while the second considers 3-adic expansions of sequences yn(λ) = λ2n,
where λ is a 3-adic integer. We show in both cases that the set of initial values having inﬁnitely
many iterates that omit the digit 2 is small in a suitable sense. For each nonzero initial value
we obtain an asymptotic upper bound as k → ∞ on the the number of the ﬁrst k iterates
that omit the digit 2. We also study auxiliary problems concerning the Hausdorﬀ dimension
of intersections of multiplicative translates of 3-adic Cantor sets.

1. Introduction

P. Erd˝os [4] asked the question of when the ternary expansion of 2n omits the digit 2. This
happens for 20 = (1)3, 22 = 4 = (11)3 and 28 = 256 = (100111)3. He conjectured that it
does not happen for all n ≥ 9, and commented that: “As far as I can see, there is no method
at our disposal to attack this conjecture.” This question was initially studied by Gupta [12]
who found by a sieving procedure that there are no other solutions for n < 4374. In 1980
Narkiewicz [18] showed that the number

N1(X) := #{n ≤ X : the ternary expansion (2
n)3 omits the digit 2}.

has N1(X) ≤ 1.62X α0 with α0 = log3 2 ≈ 0.63092. The Erd˝os question remains open and has
appeared in several problem lists, e.g. Erd˝os and Graham [5] and Guy [13, Problem B33]. In
this paper we call the ”Conjecture of Erd˝os” the weaker assertion that there are only ﬁnitely
many exponents n such that the ternary expansion (2n)3 of 2n omits the digit 2.
This paper considers analogues of the conjecture of Erd˝os for iterates of two discrete dy-
namical systems, one acting on the real numbers and the other acting on the 3-adic integers,
with an additional degree of freedom given by a parameter λ specifying the initial condition. In

1MSC Classiﬁcation (2000): 11A63 (Primary), 11K16, 11K41, 26A18, 37A45 (Secondary)

both dynamical systems the parameter value λ = 1 recovers the original sequence {2n : n ≥ 0}
of Erd˝os as a forward orbit of the dynamics.
The ﬁrst dynamical system is y ↦→ 2y acting on the real numbers, which is a homeomor-
phism of R that is an expanding map. It produces a sequence of iterates yn = 2ny0 starting
from y0 = λ. The real dynamical system concerns the iterates yn. We also consider an asso-
ciated dynamical system which gives integers, by applying the ﬂoor operator, obtaining the
sequence xn = ⌊yn⌋; that is,
 xn = xn(λ) := ⌊λ2
n⌋, for n ≥ 0. (1.1)

We call this the truncated real dynamical system. Strictly speaking the truncated real dynam-
ical system has forward orbits involving two variables O+(λ) := {(yn(λ), xn(λ)) : n ≥ 0}, with
{yn(λ)} driving the dynamics. However the expanding nature of the map y ↦→ 2y implies that
the integer sequence {xn(λ) : n ≥ 0} contains enough information to uniquely determine the
initial condition λ of the iteration; here we consider the ternary expansions of the xn(λ).
The second dynamical system is y ↦→ 2y acting on the 3-adic integers Z3, which is a 3-
adic measure-preserving homeomorphism of Z3. It produces a sequence of iterates yn = 2ny0
starting from the initial condition y0 = λ. We write

yn = yn(λ) = λ2
n, for n ≥ 0, (1.2)

In this case we study membership of values yn(λ) in the subset Σ3,¯2 of all 3-adic integers whose
3-adic expansion omits the digit 2; this is the multiplicative translate 1
2 Σ3,¯1 of the 3-adic
analogue Σ3,¯1 of the classical ”middle-third” Cantor set.
In the real number case dynamical systems of a related nature have been studied by several
authors. Flatto, Lagarias and Pollington [8] introduced a parameter λ in similar questions
concering the fractional parts of the sequences {{λξn}}, for ﬁxed ξ > 1, with the aim of proving
results for the parameter value λ = 1 by proving universal results valid for all parameter values
λ > 0. Recently Dubickas and Novickas [3] considered the prime or compositeness properties of
integers occurring in truncated recurrence sequences, including ⌊λ2n⌋ as a particularly simple
case. Dubickas [2] further extends both these results to certain λ that are real algebraic
numbers.
The paper contains both results and conjectures;. We now state them in detail.

1.1. Truncated Real Dynamical System: Results

For the truncated real dynamical system xn = ⌊λ2n⌋, we show that there is a uniform asymp-
totic upper bound valid for all nonzero λ on the number of n ≤ X for which (⌊λ2n⌋)3 omits
the digit 2. Let (k)3 denote the ternary digit expansion of the integer k.

Theorem 1.1. For each λ > 0, the upper bound

Nλ(X) := #{n : 1 ≤ n ≤ X and (⌊λ2
n⌋)3 omits the digit 2} ≤ 25X 0.9725 (1.3)

holds for all all suﬃciently large X ≥ n0(λ).

In the complementary direction, the function Nλ(X) is not always bounded. The next result
shows there exist uncountably many λ > 0 such that the sequence xn(λ) contains inﬁnitely
many integers omitting the digit 2 in their ternary expansion.

2

Theorem 1.2. There exists an inﬁnite sequence S = {nk : k ≥ 1} satisfying n1 = 2 and

2 1
14 (nk−1+2k−7) ≤ nk ≤ 2
27(nk−1+2k+6), (1.4)

having the following property: The set of real numbers Σ(S) consisting of all λ > 0 for which
all the integers {xn(λ) := ⌊λ2n⌋ : n ∈ S} have ternary expansions omitting the digit 2 is an
uncountable set.

The set of exponents produced in this theorem forms a very thin inﬁnite set. One can show
that (1.4) implies that for X ≥ 2, its cardinality satisﬁes

#{nk : 1 ≤ nk ≤ X} ≥ log∗(X) − 4. (1.5)

in which log∗(X) denotes the number of iterations of the logarithm function starting at X
necessary to get a value of smaller than 1. Thus we obtain that for all λ ∈ Σ(S),

Nλ(X) ≥ log∗(X) − 4. (1.6)

We next consider properties of the set of λ that have inﬁnitely such integers. We deﬁne
the truncated real exceptional set ET (R+) by

ET (R+) := {λ > 0 : inﬁnitely many ternary expansions (⌊λ2
n⌋)3 omit the digit 2} (1.7)

We prove the following result.

Theorem 1.3. The truncated real exceptional set has Hausdorﬀ dimension

dimH(ET (R+)) = log3(2) = log 2
log 3 ≈ 0.63092.

It has nonzero log3(2)-dimensional Hausdorﬀ measure.

This result gives an indication why it may be a hard problem to tell whether there are
inﬁnitely many exceptional powers of 2 for any particular λ, such as λ = 1. Namely, it is likely
to be a hard problem to decide whether any particular real number belongs to this ”small”
exceptional set.

1.2. Real Dynamical System: Conjecture

Consider the real dynamical system y ↦→ 2y on R+. without truncation, having forward orbits
O+(λ) := {yn = λ2n : n ≥ 0}. We deﬁne the real exceptional set E(R+) by

E(R+) := {λ > 0 : inﬁnitely many ternary expansions (λ2
n)3 omit the digit 2}. (1.8)

This set is much more constrained than the truncated exceptional set ET (R+) discussed above.
As far as we know it could even be the empty set. The conjecture of Erd˝os is equivalent to the
assertion that 1 ̸∈ E(R+).
Concerning this exceptional set we make the following conjecture.

3

Conjecture A. The real exceptional set

E(R) := {λ ∈ R+ : inﬁnitely many ternary expansions (λ2
n)3 omit the digit 2}

has Hausdorﬀ dimension zero.

A stronger form of this conjecture would be that the exceptional set is countable; even
stronger would be the assertion that the real exceptional set is empty. Thus, for the moment,
there remains the possibility that the conjecture of Erd˝os might hold for all initial conditions
λ > 0, for the full ternary expansions (λ2n)3 as real numbers.
Note that if the real exceptional set is nonempty, it will necessarily be an inﬁnite set,
because it is forward invariant under multiplication by 2, i.e. 2E(R+) ⊂ E(R+). It is clearly
also forward invariant under multiplication by 3, i.e. 3E(R+) ⊂ E(R+). Thus it is forward
invariant under two commuting semigroup actions. But the real exceptional set is not known to
be a (topologically) closed set, so that results on Hausdorﬀ dimension on closed sets invariant
under commuting semigroup actions cannot be directly applied.

1.3. 3-Adic Dynamical System: Results

For a 3-adic integer λ = ∑∞
j=0 dj3j with each dj ∈ {0, 1, 2} we write (λ)3 = (· · · d2d1d0)3 for its
3-adic digital expansion. Our ﬁrst observation is an upper bound on the number of solutions
valid for all nonzero λ ∈ Z3, which extends the result of Narkiewicz [18] for λ = 1, using
essentially the same proof.

Theorem 1.4. For each nonzero λ ∈ Z3, the 3-adic integers, and each X ≥ 2,

˜Nλ(X) := #{n ≤ X : (λ2
n)3 ∈ Z3 omits the digit 2} ≤ 2X α0 , (1.9)

with α0 = log3 2 ≈ 0.63092.

We next study the 3-adic exceptional set

E(Z3) := {λ ∈ Z3 : inﬁnitely many 3-adic expansions λ2
n omit the digit 2}. (1.10)

This set seems hard to study directly, so as approximations to the 3-adic exceptional set, we
deﬁne for k ≥ 1 the sequence of sets

E (k)(Z3) := {λ ∈ Z3 : at least k values of λ2
n omit the digit 2}. (1.11)

These sets clearly form a nested family under inclusion,

E (1)(Z3) ⊃ E (2)(Z3) ⊃ E (3)(Z3) ⊃ · · · ,

and their intersection contains the exceptional set E(Z3). These sets are somewhat easier to
study.
We consider the problem of estimating the Hausdorﬀ dimension of the sets E (k)(Z3) (with
respect to the 3-adic metric) and show the following result.

Theorem 1.5. (1) The exceptional set E (1)(Z3)) has Hausdorﬀ dimension

dimH(E (1)(Z3)) = α0 ≈ 0.63092. (1.12)

4

(2) The exceptional set E (2)(Z3) has Hausdorﬀ dimension bounded by

1
2 log3(2) ≤ dimH(E (2)(Z3)) ≤ 1
2 . (1.13)

(3) The exceptional set E (3)(Z3) has positive Hausdorﬀ dimension bounded by

1
6 log3 2 ≤ dimH(E (3)(Z3)) ≤ dimH(E (2)(Z3)). (1.14)

This result is only a beginning of the study of dimH (E (k)) for general k. The (not necessarily
closed) set E (k)(Z3) is a countable union of closed sets C(2m1 , 2m2 , · · · , 2mk ) consisting of those
λ for which {λ2mj : 1 ≤ j ≤ k} all have 3-adic expansions that omit the digit 2. One can use
this to obtain upper and lower bounds on Hausdorﬀ dimension of these sets by analyzing the
Hausdorﬀ dimension of the individual sets C(2m1 , 2m2 , · · · , 2mk ). These sets are intersections of
multiplicative translates of the 3-adic Cantor set, which we discuss in the next subsection. In
Theorem 1.5 the upper bound in (2) is deduced using Theorem 1.6 below.
It is not clear whether dimH(E (k)(Z3)) > 0 for all k ≥ 1. Proving or disproving this
assertion already seems a subtle question.
Since E(Z3) ⊆ E (k)(Z3) for each k ≥ 1, any upper bound on the Hausdorﬀ dimension of
E (k)(Z3) gives an upper bound for the Hausdorﬀ dimension of the 3-adic exceptional set E(Z3).
Each condition λ2mj ∈ Σ3,¯2 imposes more constraints, apparantly lowering the Hausdorﬀ
dimension. This motivates the following conjecture concerning the 3-adic exceptional set E(Z3).

Conjecture B. The 3-adic exceptional set

E(Z3) := {λ ∈ Z3 : inﬁnitely many 3-adic expansions λ2
n omit the digit 2}

has Hausdorﬀ dimension zero.

As in the real dynamical system case, we do not know much about this exceptional set,
except that it contains 0. Again, the conjecture of Erd˝os is equivalent to the assertion that
1 ̸∈ E(Z3). The 3-adic exceptional set E(Z3) is forward invariant under multiplication by 2 and
multiplication by 3, but is not known to be a closed set.

1.4. Intersection of Multiplicative Translates of Cantor Sets: Results

The study of the exceptional sets E (k)(Z3) leads to auxiliary questions concerning the Hausdoﬀ
dimensions of intersections of multiplicative translates of the standard 3-adic Cantor set Σ3,¯2,
deﬁned by Σ3,¯2 := {λ ∈ Z3 : the 3-adic expansion (λ)3 omits the digit 2}. (1.15)

For integers 1 ≤ M1 < M2 < · · · < Mk we study the multiplicative intersection sets

C(M1, M2, · · · , Mk) := {λ ∈ Z3 : (Mjλ)3 omits the digit 2 for 1 ≤ j ≤ k}

=
 k⋃

j=1
 ( 1
Mj Σ3,¯2
) (1.16)

These sets are closed sets. The standard ”middle third” Cantor set

Σ3,¯1 := {λ ∈ Z3 : the 3-adic digit expansion (λ)3 omits the digit 1}. (1.17)

5

has Σ3,¯1 = 2Σ3,¯2, so that all results given below for Σ3¯2 convert to equivalent results for
multiplicative translates of Σ3,¯1.
Multiplicative intersection sets arise in studying sets E (k)(Z3), because they are given by
countable unions of such sets, namely

E (k)(Z3) = ⋃

0≤m1<m2<...<mk C(2
m1 , 2
m2 , · · · , 2
mk )

What can be said about the Hausdorﬀ dimension of sets C(M1, M2, ..., Mk)? This dimension
depends in a complicated manner on the 3-adic expansions of the Mi, and leads to various
problems which seem interesting in their own right.

Theorem 1.6. Let M be a positive integer which is not a power of 3. Let Σ3,¯2 be the ternary
Cantor set. Then the Hausdorﬀ dimension of C(1, M ) = Σ3,¯2 ∩ 1
M Σ3,¯2 satisﬁes

dimH(C(1, M )) ≤ 1
2 . (1.18)

We do not know if this bound is sharp. However it is possible to show that

dimH(C(1, 7)) = log3( 1 + √5
2 ) ≈ 0.438.

For lower bounds on the Hausdorﬀ dimension of such sets, we give the following suﬃcient
condition for positivity of the Hausdorﬀ dimension.

Theorem 1.7. Let 1 ≤ M1 < M2 < · · · < Mk be positive integers. Suppose there is a positive
integer N belonging to the 3-adic Cantor set Σ3,¯2 ∪ Z such that all the integers N Mi satisfy

N Mi ∈ Σ3,¯2 ∩ Z, 1 ≤ j ≤ k. (1.19)

Then
 dimH (C(M1, M2, ..., Mk)) ≥ log3(2)
⌈log3(N Mk)⌉ . (1.20)

This is proved by direct construction of a Cantor set of positive Hausdorﬀ dimension inside
C(M1, M2, ..., Mk).
This result gives a possible approach to obtaining a nonzero lower bound for dimH(E (k)(Z3))
for k = 4 or larger, if suitable Mi = 2ni can be found that fulﬁll its hypotheses. However it
can be shown that the suﬃcient condition of Theorem 1.7 is not necessary, e.g. N = 1 and
M1 = 1, M2 = 52 does not satisfy the hypothesis of this theorem, but C(1, 52) has positive
Hausdorﬀ dimension. Thus further strengthenings of this approach may be possible.
Determining the structure and Hausdorﬀ dimension of the sets C(M1, ..., Mk) leads to many
open problems.

Problem 1. Let

MC := {M ≥ 1 : there exist integersN1, N2 ∈ Σ3,¯2 with N1M = N2}.

Obtain upper and lower bounds for the number of integers 1 ≤ M ≤ X in MC.

6

Problem 2. Let MH := {M ≥ 1 : dimH(C(1, M ) > 0.}

Obtain upper and lower bounds for the number of integers 1 ≤ M ≤ X in MH.

These are diﬀerent problems, because it can be shown that the inclusion MC ⊂ MH is
strict.

1.5. Generalization of the Erd˝os Conjecture

We formulate the following strengthening of Erd˝os’s original question, by analogy with a con-
jecture of Furtstenberg [10, Conjecture 2’], which is reviewed in §5.

Conjecture E. Let p and q be multiplicatively independent positive integers, i.e. all {piqj :
i ≥ 0, j ≥ 0} are distinct. Then the base q expansions of the powers {(pn)q : n ≥ 1} have
the property that any given ﬁnite pattern P = a1a2 · · · ak of consecutive q-ary digits occurs in
(pn)q, for all suﬃciently large n ≥ n0(P ).

Conjecture E generalizes Erd˝os’s original problem, which is the special case p = 2, q = 3
with the single pattern P = 2. We note that Furstenberg’s original conjecture concerns d-ary
expansions of {(pn)d : n ≥ 1} with d = pq in which p and q are multiplicatively independent,
i.e. his conjecture would apply to the 6-adic expansion {(2n)6 : n ≥ 0}, rather than the 3-adic
expansion above.
This conjecture might more properly be formulated as a question, since we present no
signiﬁcant new evidence in its favor. However we think that any mechanism that forces a
single pattern to appear from some point on should apply to all patterns.

1.6. Summary

First, this paper places the original Erd˝os problem in a more general dynamical context.
The two dynamical generalizations seem to give restrictions on the original Erd˝os question
of roughly equal strength, as formulated in Theorems 1.1 and 1.4. That is, they each reduce
the number of candidate 1 ≤ n ≤ X to at most X c for some 0 < c < 1. What is interesting
is that these arguments use ”independent” information about the ternary expansions of 2n.
The method used for the real dynamical system estimates the omission of 2 in the log3 X most
signiﬁcant ternary digits of 2n, while for the 3-adic dynamical system the method estimates
the omission of 2 in the log3 X least signiﬁcant ternary digits of 2n. Heuristically, the most
signiﬁcant digits and least signiﬁcant digits seem uncorrelated; this is the ”independence”
referred to above. Furthermore, since the ternary expansion (2n)3 has about α0n ternary digits,
the vast number of digits in the middle of the expansion are not exploited in either method;
only a logarithmically small proportion of the available digits in the ternary expansion (2n)3
are considered in the two methods.
It seems a challenging problem to ﬁnd a method that eﬀectively combines the two ap-
proaches to ﬁnd better upper bounds on N1(X) than that given by Narkiewicz. Can one
obtain an upper bound of O(X β) for some β < log3 2 in this way? Can one show that the high
order digits and the low order digits in the ternary expansion (2n)3 are ”uncorrelated” in some
quantiﬁable way?
Second, we formulate Conjecture A and Conjecture B , asserting Hausdorﬀ dimension zero
of exceptional sets, which seem more approachable questions than the original question of

7

Erd˝os. A much harder question seems to be to resolve whether the exceptional sets E(R+) and
E(Z3) are countable or ﬁnite.
Third, our analysis leads to a variety of interesting auxiliary problems in combinatorial num-
ber theory. These concern the Hausdorﬀ dimension of intersections of multiplicative translates
of 3-adic Cantor sets. These Hausdorﬀ dimensions depend in an complicated arithmetic way
on the values of the integer multipliers. These sets seem worthy of further study.
Finally, we observe analogies with work of Furstenberg [9], [10] on actions of multiplicative
semigroups and intersections of Cantor sets. This resulted in formulating Conjecture E.

1.7. Contents and Notation

The contents of the rest of the paper are as follows. In §2 we prove results for the truncated
real dynamical system. In §3 we prove results for the 3-adic dynamical system. In §4 we
establish auxiliary results on the Hausdorﬀ dimensions of intersections of a ﬁnite number of
multiplicative translates (by positive integers) of the 3-adic Cantor set, and include several
examples. These results are used to complete the proofs of one result in §3. In §5 we discuss
work of Furstenberg. This includes a conjecure which motivates Conjecture E, and his for-
muation of a notion transversality of semigroup actions on a compact space and implications
for intersections of Cantor sets. In the concluding section §6 we describe history associated to
Erd˝os’s original question.

Notation. Let {{x}} := x − ⌊x⌋ = x (mod 1)

denote the fractional part of a real number x. Let

⟨⟨x⟩⟩ := {{x + 1/2}} − 1/2

denote the (signed) distance of x to the nearest integer.

Acknowledgments. I am grateful to A. Pollington, K. Soundararajan and H. Furstenberg
for helpful comments and references. I thank the reviewer for helpful comments and sugges-
tions. The author was supported by NSF grant DMS-0500555.

2. Real Dynamical System: Proofs

We consider the sequence of real numbers x∗
n := λ2n, and consider the associated integers

xn(λ) = ⌊x∗
n⌋.

On taking logarithms to base 3 we have

log3 x∗
n = log3 λ + n log3 2 = mn + wn,

in which mn = ⌊log3 x∗
n⌋ is the integer part and wn := log3 x∗
n (mod 1) is the fractional part,
with 0 ≤ wn < 1. Now the digits in the ternary expansion of xn(λ) are completely determined
by knowledge of the real number wn, since xn(λ) = 3mn 3wn, so they are the ﬁrst mn ternary
digits in the ternary expansion of 3wn, since multiplication by 3mn simply shifts ternary digits
to the left without changing them.
 8

On the other hand, the sequence of wn form an orbit under iteration of the map T : [0, 1] ↦→
[0, 1] given by T (w) = w + log3 2 (mod 1). (2.1)

on taking initial condition w0 = log3 λ, with wn+1 = T (wn). Since α0 = log3 2 is irrational,
the map T is an irrational rotation on the torus R/Z, which is known to be uniquely ergodic.
In particular, every forward orbit of iteration of T is uniformly distributed (mod 1), with the
convergence rate to uniform distribution determined by properties of the continued fraction
expansion of α0. We now examine the consequences of this property for the ternary expansions
of x∗
n.
First, the leading ternary digits of 3wn specify the position of wn in the interval [0, 1]
to a small subinterval. The property of omitting the digit 2 in a leading digit of a ternary
expansion of xn will prohibit wn from certain subintervals in [0, 1]; the allowed subintervals
will have small measure. Using the fact that the distribution of wn(mod 1) approaches the
uniform distribution fairly rapidly, one can show that most wn have some leading digit that
is a 2; Theorem 1.1 is deduced using this idea, where the number k of leading digits used will
depend on the interval [1, X] considered.
Second, one use a construction selecting a rapidly growing set of values of n = nk, chosen
using the continued fraction expansion of α0, in such a way as to permit each wnk to fall in a
”good” interval where the initial ternary digits for a large set of short intervals have xnk (λ)’s
with ternary expansions avoiding any 2’s. A recursive intervals construction, which modiﬁes λ
slightly at each stage while not disturbing the initial ternary digits already selected, produces
the sets in Theorem 1.2. Finally, we use a quantitative version of such an intervals construction
producing the set of Hausdorﬀ dimension α0 in Theorem 1.3.
We begin with two preliminary lemmas, the ﬁrst on the spacings of multiples of an irrational
number (modulo one) and the second on Diophantine approximation properties of α0 = log3 2.

Lemma 2.1. Let θ be irrational and consider the N + 1 numbers

{x + jθ (mod 1) : 0 ≤ j ≤ N },

viewed as subdividing the torus R/Z (the interval [0, 1] with endpoints identiﬁed) into N + 1
subintervals (”steps”).
(1) These subintervals take at most three distinct lengths. If three diﬀerent lengths occur,
say L1, L2, L3, then one of them is the sum of the other two, say L1 + L2 = L3.
(2) Let the continued fraction expansion of θ = [a0, a1, a2, · · ·], have partial quotients ai and
convergents pn
qn with denominators satisfying qn+1 = an+1qn + qn−1. Write uniquely

N = (j + 1)qn + qn−1 + k, 0 ≤ k ≤ qn − 1 (2.2)

with 0 ≤ j ≤ an+1 − 1. Then the subintervals have lengths

L1 = |⟨⟨qnθ⟩⟩|

L2 = |⟨⟨qn−1θ⟩⟩ + (j + 1)⟨⟨qnθ⟩⟩|

L3 = |⟨⟨qn−1θ⟩⟩ + j⟨⟨qnθ⟩⟩|

and occur with multiplicities jqn + qn−1 + k + 1, k + 1, and qn − (k + 1), respectively. Here
L3 = L1 + L2, and L1 < L2 if 0 ≤ j ≤ an+1 − 2, while L2 < L1 if j = an+1 − 1. The intervals
of size L3 do not occur if and only if k = qn − 1.
(3) For N = qn+1 − 1, there occur intervals of exactly two lengths L1, L2 as above, and
these lengths satisfy L2 < L1 < 2L2. (2.3)

9

Proof. (1), (2) These results have a long history, which is detailed in Slater [23]. In particular,
(2) implies (1) and the formulas in (2) appear in Slater [23, eqn. (33), p. 1120]. The ordering
of L1 and L2 follows from the fact that the ⟨⟨qnθ⟩⟩ alternate in sign with successive n.
(3) Let N = qn+1 − 1. If an ≥ 2 then the decomposition (2.2) is

N = (an+1 − 1)qn + qn−1 + (qn − 1)

with k = qn − 1 and j = an+1 − 1, Now (2) says there are steps of exactly two lengths L1 and
L2 given by
 L1 = |⟨⟨qnθ⟩⟩|

L2 = |⟨⟨qn−1θ⟩⟩ + (an+1 − 1)⟨⟨qnθ⟩⟩|

and L2 < L1. Next we have

⟨⟨qn+1θ⟩⟩ = ⟨⟨qn−1θ⟩⟩ + an+1⟨⟨qnθ⟩⟩ = (⟨⟨qn−1θ⟩⟩ + (an+1 − 1)⟨⟨qnθ⟩⟩) + (⟨⟨qnθ⟩⟩).

Since ⟨⟨qn+1θ⟩⟩ and ⟨⟨qnθ⟩⟩ have opposite signs, and

|⟨⟨qn+1θ⟩⟩| ≤ L2

we must have L2 < L1 = L2 + |⟨⟨qn+1θ⟩⟩| < 2L2.

(The fact that θ is irrational gives the strict inequality at the last step.)
There remains the case an+1 = 1. Now we ﬁnd that the decompostion (2.2) is

N = qn + qn−1 − 1 = anqn−1 + qn−2 + (qn−1 − 1),

with k = qn−1 − 1 and j = an−1 − 1. As before, there are intervals of exactly two lengths

L1 = |⟨⟨qn−1θ⟩⟩|

L2 = |⟨⟨qn−2θ⟩⟩ + (an − 1)⟨⟨qn−1θ⟩⟩|,

with L2 < L1. We deduce as in the case an+1 ≥ 2 that

L2 < L1 = L2 + |⟨⟨qnθ⟩⟩| < 2L2,

as required.

The point of Lemma 2.1 is that for the choice N = qn − 1 the points {x + jθ (mod 1) :
0 ≤ j ≤ N } are very close to uniformly spaced on the interval [0, 1]. The next result obtains
information on the convergent denominators qn for the irrational number α0.

Lemma 2.2. For the irrational number α0 = log3 2 the following hold.
(1) For all q ≥ 1, and all integer p there holds the Diophantine inequality

|α0 − p
q | ≥ 1
1200 1
qc0+1 . (2.4)

with c0 = 13.3.
(2) The denominators qn of the continued fraction convergents pn
qn of α0 satisfy

qn ≤ 1200(qn−1)
c0. (2.5)

10

Proof. (i) The existence of a bound of this general form, aside from the precise constants,
follows from A. Baker’s results on linear forms in logarithms [1, Theorem 3.1], applied to the
linear form Λ = k + q log 2 − p log 3, taking k = 0, noting that its height B := max{|p|, q} ≤ 2q.
The particular bound (2.4) is obtained from a result of Simons and de Weger [22, Lemma
12], who show that for k ≥ 1 and all integers l,

|(k + l) log 2 − k log 3| > exp(−13.3(0.46057))k−13.3 > 1
484 k−13.3.

Their result is proved using a transcendence result of G. Rhin [19, Proposition, p. 160] for
linear forms in two logarithms. We may suppose k < k + l < 1.6k, and obtain

| log3 2 − k
k + l | > 1
log 3 exp(−13.3(0.46057))(k + l)
−1k−13.3 ≥ 1
1200 (k + l)
−14.3,

which on taking p = k, q = k + l gives the needed bound.

(2) Since α0 lies in the interval between two successive continued fraction convergents pn−1
qn−1
and pn
qn , we obtain using (2.4) that

1
qnqn−1 = | pn
qn − pn−1
qn−1 | = |α0 − pn−1
qn−1 | + |α0 − pn
qn | ≥ 1
1200 1
(qn−1)c0+1

Multiplying by 1200qnqc0
n−1 gives (2.5).

Proof of Theorem 1.1. Let λ > 0. We study for 1 ≤ n ≤ X the ternary expansion of

xn = xn(λ) = ⌊λ2
n⌋.

We will study the ﬁrst k leading ternary digits of the {xn : 1 ≤ n ≤ X} where we choose k as
follows. If pj
qj are the convergents of the continued fraction expansion of α0 = log3 2, pick that
l such that ql−1 < X ≤ ql, and then choose k to be the number of ternary digits in ql−1, so
that 3k−1 < ql−1 ≤ 3k. Note that k = ⌈log3 ql−1⌉ ≤ ⌈log3 X⌉.
We now set wn := log3(λ2n)(mod 1), with 0 ≤ wn < 1, so that

wn = nα0 + log3 λ (mod 1). (2.6)

We now observe that where wn falls in the interval [0, 1) speciﬁes the ﬁrst k ternary digits in the
ternary expansion of ewn, with 1 ≤ ewn < 3, we can partition the interval [0, 1) into half-open
intervals corresponding to each such ternary expansion. Consider a ternary expansion

b = [b0b1 · · · bk−1]3, bi ∈ {0, 1, 2}, b0 ̸= 0,

of length k, noting there are 2 · 3k−1 such expansions. Set

β(b) =
 k−1∑

j=0
 bj
3j , (2.7)

which has 1 ≤ β(b) < 3 and associate the subinterval of [0, 1),

J(b) := [log3 β(b), log3(β(b) + 1
3k−1 )). (2.8)

11

These 2 · 3k−1 subintervals partition [0, 1), from J([10 · · · 0]3) = [log3(1), log3(1 + 1
3k−1 )) to
J([22 · · · 2]3) = [log3(3 − 1
3k−1 ), log3 3).
We claim that the following conditions (C1) and (C2) are equivalent for xn with 3m ≤ xn ≤
3m+1, with m ≥ k.
(C1) xn has ternary expansion having the k leading digits b = [b0b1 · · · bk−1]3, i.e xn =∑m
j=0 bj3m−j , for some (bk+1, ..., bm).
(C2) wn = log3 xn (mod 1) has wn ∈ J(b).
The claim follows because the deﬁnition of J(b) speciﬁes the k leading ternary digits of 3wn,
while xn = 3m3wn and the eﬀect of multiplying by 3m simply shifts all ternary digits m places
to the left without changing the leading digits.
Next we note that the intervals J(b) all have the same length to within a factor of 3,
namely 1
3k ≤ |J(b)| ≤ 1
3k−1 . (2.9)

This holds using
 |J(b)| = log(β(b) + 1
3k−1 ) − log(β(b)) = ∫ β(b)+ 1
3k−1

β(b)
 dx
x ,

and the bounds (2.9) follow since 1
3 ≤ 1
x ≤ 1.
Next we examine the wn in consecutive blocks of length N = ql−1 − 1, i.e the set {wn :
j(ql−1 − 1) ≤ n < (j + 1)(ql−1 − 1)}. By (2.6) we may apply Lemma 2.1(3) to this sequence of
numbers, to infer that the spacings between them are of two lengths L1 and L2 which satisfy
L2 < L1 < 2L2. In particular since 3k−1 ≤ ql−1 ≤ 3k these block sizes satisfy

1
2 · 3k ≤ 1
2(ql−1 − 1) ≤ L1 < L2 ≤ 2
ql−1 − 1 ≤ 2
3k−1 .

We conclude using (2.9) that at each subinterval J(b) contains at most six points wn from this
block. Thus at most six values of n in j(ql−1 − 1) ≤ n < (j + 1)(ql−1 − 1) give an xn having
given intial k-digit ternary expansion b = [b0b1 · · · bk1]3.
We know there are exactly 2k−1 values of b = [b0b1 · · · bk1]3 that omit the ternary digit 2,
so the above shows there are at most 6 · 2k−1 values of n in each such block giving an xn whose
initial k ternary digits avoid 2. There are ⌊ X
ql−1−1 ⌋ + 1 such blocks covering all 1 ≤ n ≤ X
hence we conclude there are at most

M := 6 · 2
k−1 ( X
ql−1 − 1 + 1
) ≤ 6 · 2
k−1 ( X
3k−1 + 1
)

≤ 6 (( 2
3 )
k−1X + 2
k−1) ≤ 12( 2
3 )
k−1X,

values of xn whose initial k ternary digits omit the digit 2. (In the last inequality we used
X ≥ ql−1 > 3k−1.
It remains to upper bound M as a function of X. Using Lemma 2.2(2) we have

X ≤ ql ≤ 1200(ql−1)
c0 ≤ 1200(3
k)
c0

with c0 = 13.3. We apply this bound to obtain

( 3
2 )
k = (3
c0k)log3(3/2)c−1
0 ≥ ( 1
1200 X)( 1−α0
c0 ) ,

12

Here 1
37 < (log3(3/2))c
−1
0 = 1−α0
c0 ≤ 1
36 , so we obtain

( 2
3 )
k ≤ (1200)
 1−α0
c0 X −( 1−α0
c0 )

Substituting this into the deﬁnition of M we obtain,

M ≤ 18( 2
3 )
kX ≤ 18 · (1200) 1
36 X 1− 1−α0
c0 ≤ 25X 36
37 ≤ 25X 0.9725.

and the result follows. .

Proof of Theorem 1.2. We will construct a rapidly increasing sequence of integers S0 =
{mk : k ≥ 1} having the form mk = l0 + l1 + ... + lk, (2.10)

such that there is an uncountable set of real numbers ˜Σ such that all the numbers λ ∈ Σ have
the property: for each k ≥ 1, the integer Mk := ⌊λ2mk ⌋ has a ternary expansion that omits the
digit 1. We now claim that all the integers Nk := ⌊λ2mk −1⌋ have ternary expansions (Nk)3 that
omit the digit 2. This holds because for each Nk either Mk = 2Nk or Mk = 2Nk + 1, but Mk
is necessarily an even integer since all its ternary digits are 0 or 2, so we must have Mk = 2Nk.
Thus Nk has only digits 0 and 1 in its ternary expansion, so we have for S = {mk − 1 : k ≥ 1}
that ˜Σ ⊂ Σ(S) := {λ : (⌊λ2
nk ⌋)3 omits the digit 2},

hence Σ(S) is an uncountable set.
We choose the lk recursively, taking l0 = m0 = 0 and lk to be the smallest integer satisfying
lk ≥ 2k and 0 < {{log3 2
lk }} = {{lkα0}} < 2
−mk−1−2k−4. (2.11)

Here mk = l0 + l1 + · · · + lk. We set

rk := ⌊lkα0⌋, α0 = log3 2.

The condition lk ≥ 2k ensures that rk ≥ k. Then we have

2
lk = 3
lkα0 = 3
rk+{{lkα0}} = 3
rk 3
{{lkα0}}.

Using ex ≤ 1 + 2x for 0 ≤ x ≤ 1 we have

3
{{lkα0}} = e
{{lkα0}} log 3 ≤ 1 + 2 log 3{{lkα0}} ≤ 1 + 2 log 3
2mk−1+2k+4 .

Thus we obtain

3
rk < 2
lk < 3
rk (1 + 2 ln 3
2mk−1+2k+4
 ) ≤ 3
rk (1 + 1
3(mk−1+2k+2)α0
 ) (2.12)

This says that the ternary expansion of 2lk has leading digit 1 followed by a string of at least
(mk−1 + 2k + 2)α0 zeros.
Given this choice of {lk : k ≥ 1}, we deﬁne the set Σ to consist of all real numbers

˜Σ := {λ :=
 ∞∑

k=0
 dk
2mk : λ is admissible} (2.13)

13

where λ is called admissible if, for all k ≥ 1 it has the two properties
(P1) The digit dk satisﬁes 0 ≤ dk ≤ 3
rk − 3
rk−k. (2.14)

(P2) Let λk := ∑k
j=0 dj
2
mj . Then the integer

Mk := λk2
mk (2.15)

has a ternary expansion (Mk)3 which omits the digit 1.

Claim 1. Any λ = ∑∞
j=0 dj
2
mj with all dk satisfying (P1) satisﬁes

1 ≤ λ < 2 (2.16)

and Mk = λk2
mk = ⌊λ2
mk ⌋, for all k ≥ 1. (2.17)

To prove the claim , we observe that (P1) gives

1 ≤ λ ≤ 1 +
 ∞∑

k=1
 1
2mk−1
 ( 3rk − 3rk−k

2lk
 )

≤ 1 +
 ∞∑

k=1
 1
2mk−1 (1 − 3
−k) < 2. (2.18)

Next, (P1) gives
 0 ≤ λ − λk =
 ∞∑

j=k+1
 dj
2mj = 1
2mk
 

 ∞∑

j=k+1
 dj
2mj −mk
 



≤ 1
2mk
 

 ∞∑

j=k+1
(1 − 1
3j ) 1
2mj−1−mk
 



≤ 1
2mk
 

 ∞∑

j=k+1
(1 − 1
3j ) 1
2(j−k−1)(2j)
 

 < 1
2mk ,

proving Claim 1.

Claim 2. For any choice of {dj : 1 ≤ j ≤ k − 1} that satisfy both (P1) and (P2), there are
at least 2rk − 2rk−k choices of dk that satisfy (P1) and (P2).

To prove this, ﬁrst note that

λk−12
mk = Mk−12
mk−mk−1 = Mk−12
lk = Mk−13
rk + Mk−1(2
lk − 3
rk ). (2.19)

We assert that 0 ≤ Mk−1(2
lk − 3
rk ) ≤ 3
rk−k. (2.20)

14

The left inequality is immediate, and using (2.18) we have Mk−1 ≤ λ2mk−1 ≤ 2mk−1+1, while
(2.12) gives
 Mk−1(2
lk − 3
rk ) ≤ 2
mk−1+1 (3
rk ln 3
2mk−1+2k+4
 )

≤ 3
rk 1
22k+3 ≤ 3
rk−k,

proving (2.20).
From (2.19) and (2.20) we see that the ternary expansion of λk−12mk repeats that of Mk−1
shifted rk positions to the left, then has a block of at least k zeros, and following this has the
ternary expansion of the integer Mk−1(2lk − 3rk ). It follows that choosing from the range of
values 0 ≤ dk ≤ 3rk − 3rk−k, and setting λk := ∑k
j−0 dj
2
mj , the integers

Mk := λk2
mk = λk−12
mk + dk (2.21)

can be selected to give all ternary integers which
(i) have the ternary expansion matching Mk−1 to the left of the rk-th position,
(ii) omit the digit 1, and
(iii) have at least one 2 and at least one 0 in positions between rk and rk − k;
call these allowable values. In these k + 1 positions the largest allowed value is 222 · · · 20 and
the smallest is 000 · · · 02. These produce exactly 2rk − 2rk−k such ternary integers Mk, con-
structed by choice of the same number of allowable values dk. This proves Claim 2.

Claim 3. The set ˜Σ contains uncountably many admissible λ, and each of them has the
property that every Mk = ⌊λ2
mk ⌋, k ≥ 1, (2.22)

has a ternary expansion (Mk)3 that omits the digit 1.

Indeed Claim 2 implies there are uncountably many such λ, since the construction has a
Cantor set form which gives an inﬁnite tree of values with branching at least two at every
node at every level k ≥ 2. The relation (2.22) holds by Claim 1, and these Mk have ternary
expansions omitting 2 by (P2). Thus Claim 3 follows.
It remains to verify the upper and lower bounds (1.4) on the growth rate of the sequence
mk. The size of mk is determined by the Diophantine condition on lk given by equation (2.11).
(The numbers lk grow so rapidly that the side condition lk ≥ 2k is automatically satisﬁed for
k ≥ 2.) Note that we cannot directly use Dirichlet’s box principle to get an upper bound for
the size of the minimal lk satisfying (2.11) because this is a one-sided approximation condition.
Instead we have that the minimal lk will be no larger than that even-numbered convergent q2l
of the continued fraction expansion of α0 satisfying

q2l−2 ≤ 2
mk−1+2k+4 < q2l.

Lemma 2.2 (2) gives the bound

q2l ≤ 1
C 2
0 (q2l−2)
2c1 = (1200)
2(q2l−2)
26.6 ≤ 2
27mk−1+54k+132. (2.23)

Since nk = mk − 1 we obtain

nk ≤ mk ≤ mk−1 + q2l ≤ mk−1 + 2
27mk−1+54k+132 ≤ 2
27(nk−1+2k+6),

15

which is the upper bound in (1.4).
Lemma 2.2 implies a lower bound on how small lk+1 can be to make (2.11) hold, namely
we must have (lk+1)
c0 ≥ 2
mk+2j−7, (2.24)

with c0 = 13.3, to avoid contradicting 2.2(1). This yields the lower bound in (1.4), which holds
for nk = mk − 1 produced in this construction.

Proof of Theorem 1.3. We consider the truncated exceptional set ET (R+) . We ﬁrst
establish the upper bound dimH (ET (R+)) ≤ α0. We have

ET (R+) =
 ∞⋃

M =2
 (
ET (R+) ∩ [ 1
M , M ]
) .

Since the Hausdorﬀ dimension of a countable union of sets is the supremum of the Hausdorﬀ
dimensions of the separate sets, it suﬃces to show that

dimH (ET (R+) ∩ [ 1
M , M ]) ≤ α0 = log3 2. (2.25)

To show this we ﬁnd suitable coverings of these sets. For each n ≥ 1 we have

ET (R+) ∩ [ 1
M , M ]) ⊂ Sn(M ) :=
 ∞⋃

j=N Σj([ 1
M , M ]) (2.26)

with Σj([ 1
M , M ]) := {λ : − 1
M ≤ λ ≤ M and (⌊λ2
j⌋)3 omits the digit 2}.

The set Sn(M ) thus encodes a ”tail event” that there are arbitrarily large j for which (⌊λ2j ⌋)3
that omit the digit 2. We will eventually let n → ∞ so we suppose that n ≥ log3 M + 2,
so that λ2j ≥ 1, for any j ≥ n. Now consider such j as ﬁxed, and note that ⌊λ2j ⌋ takes a
ﬁxed integer value on an interval of length 1
2j . Letting b = (⌊λ2j ⌋)3, we see that allowable
values of b satisfy 1 ≤ b ≤ M 2j. As λ varies over [ 1
M , M ] these integers vary over a subset
of [1, M 2j ] and of these, the number of such ternary expansions b that omit the digit 2 is at
most (counting integers over successive blocks [3k−1, 3k)),

1 + 2 + · · · + 2
⌈log3(2j M )⌉ ≤ 2
log2(2j M )+2

≤ 2
jα0+log3 M +2 ≤ 4M 2
jα0 .

Thus we obtain a collection

Ij(M ) := {Ij(b) : b gives an admissible interval for ⌊λ2
j⌋, 1
M ≤ λ ≤ M }.

of at most 4M 2jα0 intervals of length 1
3j , and these intervals cover the set Σj([ 1
M , M ]). Summing
over all j ≥ n we obtain an inﬁnite collection of intervals

I(n, M ) :=
 ∞⋃

j=n Ij(M ),

16

which cover the set ET (R+) ∩ [ 1
M , M ]) by (2.26), and every interval included has length at most
1
2n . Now ﬁx ǫ > 0 and observe that

∑

I∈I(n,M ) |I|
α0+ǫ =
 ∞∑

j=n
 

 ∑

I∈Ij(M )( 1
2j )
α0+ǫ




≤
 ∞∑

j=n 4M 2
jα0 ( 1
2j )
α0+ǫ

= 4M
 

 ∞∑

j=n 2
−jǫ


 = ( 4M
1 − 2−ǫ )2
−nǫ.

Letting n → ∞, the diameter of the covering I(n, M ) goes to zero, and the scaled length goes
to zero as well, which establishes

dimH
 (ET (R+) ∩ [ 1
M , M ]
) ≤ α0 + ǫ.

Now we can let ǫ → 0 to obtain (2.25), and the upper bound dimH(ET (R+)) ≤ α0 follows.
To establish the lower bound dimH (ET (R)) ≥ α0 is more diﬃcult, as it requires controlling
all coverings of the set. We will actually establish the stronger result that

measα0( ˜Σ) > 1
16 , (2.27)

where ˜Σ ⊂ [1, 2] is the set constructed in Theorem 1.2 in (2.13). The set ˜Σ had a construction
resembling a Cantor set, with two diﬀerences. The ﬁrst diﬀerence is that the dissection at each
layer k depended on the previous layers, and the second diﬀerence is that the layer at level k
involved denominators 2mk with
 mk = l0 + l1 + ... + lk,

with the lk growing extremely rapidly. We can however adapt an argument given in Falconer
[7, Example 2.7, p. 31] for the Cantor set to show (2.27).
We claim that ˜Σ has a representation as

˜Σ =
 ∞⋂

s=1 Xs, (2.28)

in which Xs consists of a union of a collection Js of disjoint intervals of size proportional to
3−s, and the sets are nested: · · · X3 ⊂ X2 ⊂ X1.

Here the intervals in Js will play the role of the Cantor set dissection into intervals at level s,
for each power of 3s.
We ﬁrst deﬁne the collection Js for those levels s = sk with

sj := ⌊mjα0⌋, (2.29)

which are directly given in the construction of Theorem 1.2. Then we show one can ﬁll in all
the intermediate layers sk ≤ s < sk+1.
 17

We have 3sk < 2mk < 3sk+1, and the set Jsk is the union of all closed intervals

Jsk := {
[ M
2mk , M + 1
2mk
 ] : M = λk2
mk with λk =
 k∑

j=0
 dj
2mj admissible.}

with admissibility in the construction in Theorem 1.2. Here we have

2
mk = 2
l1+...+lk = 3
l1α0+...+lkα0 = 3
r1+r2+...+rk · 3
{{l1α0}}+...+{{lkα0}} ≤ 2 · 3
r+1+...+rk,

using the fact that ∞∑

k=1{{lkα0}} ≤
 ∞∑

k=1 2
−mk−1−2k−2 ≤ 1
2 ,

using (2.11). This also establishes that

sk = r1 + r2 + ... + rk. (2.30)

Inside each interval at level s = sk−1 there ﬁt exactly 2rk − 2rk−k subintervals at ternary level
s = sk, each of length 2−mk , and we now know that 1
2 3−sk ≤ 2−mk ≤ 3−sk . This dissection
of an interval at ternary level sk−1 into subintervals at ternary level sk is exactly that of the
Cantor set, except that the two ends of the interval are trimmed oﬀ a small amount, to a
relative distance 3−k from each end of the interval.
We now ﬁll in the intermediate levels Xs for sk−1 < s < sk by gluing together all intervals
in Jsk that have matching initial ternary expansions [M ]3 of M = λk2mk , disregarding the last
sk −s ternary digits of [M ]3, and ﬁlling in the space between them. The resulting intervals of Js
all have size exactly 3sk−s2−mk (except possibly for two subintervals adjacent to the truncated
ends); their size lies between 1
2 3−s and 3−s. Also, the gaps between any two adjacent intervals
at ternary level s are of size at least as large as

Gs = 3
sk−s2
−mk ≥ 1
2 3
−s. (2.31)

This fact holds because this construction uses ternary integers omitting the digit 1; the set of
ternary integers omitting the digit 2 has some intervals of this kind that are adjacent, so the
gap size would be zero in that case.
The above construction deﬁnes the intervals in Js at level s for all s. This dissection
imitates the Cantor set in that each interval at level s, contains at most 2s′−s subintervals at
any deeper ternary level s′ ≥ s. It may contain fewer subintervals, due to the trimming at
ends of the subinterval, but it always contains at least 2s′−s−1 such subintervals.
The set ˜Σ is a compact set contained in the interval [1, 2]. To bound its α0-dimensional
Hausdorﬀ measure from below, we must show that in every covering {Ui} by closed intervals
there holds ∑

i |Ui|
α0 ≥ 1
16 . (2.32)

By enlarging the intervals slightly (by 1 + ǫ) and observing that their interiors give an open
cover of ˜Σ, we can extract a ﬁnite subcover. Since we can extract a ﬁnite subcover for any
ǫ > 0, it suﬃces to verify (2.32) holds for every ﬁnite cover {Ui} of ˜Σ by intervals.
Given an interval Ui in a covering, deﬁne s by

3
−s ≤ |Ui| < 3
−s+1. (2.33)

18

Then Ui can touch at most two subintervals at level s because all subintervals in Js are sepated
by gaps of size at least 1
2 3−s. If s′ ≥ s then Ui intersects at most 2 · 2s′−s subintervals at level
s′ − s; by (2.33) this number is bounded above by

2 · 2
s′−s ≤ 2
s′3
−α0s ≤ 2 · 2
s′(3
α0 |Ui|
α0 ) = 4 · 2
s′|Ui|
α0 ). (2.34)

Given a ﬁnite cover, choose s′ = sk large enough so that |Ui| ≥ 3−s′ for all i. Then the
collection {Ui} necessarily covers all subintervals at level s′ = sk. By construction Isk contains
at least k∏

i=1(2
ri − 2
ri−i) = 2
r1+...+rk n∏

i=1(1 − 2
−i) ≥ 1
4 2
sk (2.35)

intervals, since where ∏k
i=1(1 − 2−i) ≥ ∏∞
i=1(1 − 2−i) ≥ 1
4 . Now we count how many intervals
at level sk are covered. Since Ui intersects at most 4 · 2sk |Ui|α0 such intervals we must have

∑

i 4 · 2
sk |Ui|
α0 ≥ |Jsk | ≥ 1
4 2
−sk .

This yields ∑

i |Ui|
α0 ≥ 1
16 ,

which establishes (2.27).

Remark. More generally we may consider the real dynamical system y → βy, where β > 1,
and consider the truncated ternary expansions {(⌊λβn⌋)3 : n ≥ 0}. The methods above should
extend to those β such that α := log3 β satisﬁes a Diophantine condition

|α − p
q | ≥ c2 1
qc1+1 , for all p, q with q ≥ 1, (2.36)

for constants c1 > 1 and c2 > 0. The conclusions of the results require appropriate modiﬁcation,
with constants depending on the Diophantine condition.

3. 3-adic Integer Dynamical System: Proofs

We consider the 3-adic integers Z3 and write the 3-adic expansion of λ ∈ Z3 as

λ =
 ∞∑

j=0 dj3
j with each dj ∈ {0, 1, 2}. (3.1)

We write the 3-adic digit expansion as (λ)3 = (· · · d2d1d0)3.
This dynamical system consider the sequence of 3-adic integers, yn = λ2n, where λ is a
given nonzero 3-adic integer. Here yn form the forward orbit of the ﬁrst order linear recurrence
yn = 2yn−1, with initial condition y0 = λ. The map T : x → 2x is an automorphism of the
3-adic integers Z3, which leaves each of the sets Σj := 3jZ∗
3 for j ≥ 0 invariant. (Here Z∗
3 are
the 3-adic units.) These sets partition Z3 and this map acts ergodically on each component
Σj. We are interested in the possible ways that the orbit {yn : n ≥ 0} can intersect the set
Σ3,¯2 := {w : w = ∑∞
j=0 aj3j ∈ Z3, with each aj = 0 or 1}. We now upper bound the number
of n ≤ X that can fall in the set Σ3,¯2.
 19

Proof of Theorem 1.4. Let λ ∈ Z3 with λ ̸= 0. We study the set

˜Nλ(X) := #{1 ≤ n ≤ X : (λ2
n)3 omits the digit 2}. (3.2)

Write λ = 3jλ∗ with λ∗ ∈ Z×
3 := {λ ∈ Z3 : λ ̸≡ 0 (mod 3)}. Then we have ˜Nλ(X) = ˜Nλ∗ (X),
since multiplication by 3j simply shifts 3-adic digits to the left. Thus to prove the desired
inequality there is no loss of generality to require λ ̸= 0 (mod 3), by replacing λ with λ∗.
The proof is based on the fact that 2 is a primitive root (mod 3k) for each k ≥ 1. Thus,
for each k ≥ 1 {λ2
n (mod 3) : 1 ≤ n ≤ φ(3
k) = 2 · 3
k−1} (3.3)

runs over all 2 · 3k−1 invertible residue classes ( mod 3k). Of these, exactly 2k−1 residue classes
have a 3-adic expansion that omits the digit 2. Now, given X, pick that k such that

2 · 3
k−2 < X ≤ 2 · 3
k−1.

Then applying (3.3) over 1 ≤ n ≤ 2·3k−1 we have exactly 2k−1 values of n with (λ2n)3 omitting
the digit 2 in its ﬁrst k 3-adic digits (dk−1 · · · d1d0)3. Thus

˜Nλ(X) ≤ 2
k−1 = 2 · 2
k−2 = 2 · 3
α0(k−2)

= 2
1−α0 (
2 · 3
k−2)α0 ≤ 2X α0 ,

which is the desired upper bound.

The object of Theorem 1.5 is to establish upper bounds on the Hausdorﬀ dimension of the
3-adic exceptional set E(Z3) through upper bounds on various E (j)(Z3) which contain it.
We note that Hausdorﬀ dimension is a metric notion (cf. Rogers [20]), and its version for 3-
adic integers uses the 3-adic metric is quite similar to Hausdorﬀ dimension for real numbers on
the interval [0, 1]. In fact we have a continuous (and almost one-to-one) mapping ι : Z3 → [0, 1]
which sends a 3-adic number λ = (· · · d2d1d0)3 to the real number with ternary expansion
.d0d1d2 · · ·. One can show that this mapping preserves Hausdorﬀ dimension of sets, i.e a 3-adic
set X and its image ι(X) have the same Hausdorﬀ dimension. This holds because one can
expand each set in a 3-adic covering of a set X to a closed-open disk
B(m, 3j) = {x ∈ Z3 : x ≡ m (mod 3j)}, with at most a factor of 3 increase in diameter, and
similarly one can inﬂate any real covering to a covering with ternary intervals [ m
3j , m+1
3j ] with
at most a factor of 3 increase in diameter. But these special intervals are assigned the same
diameter under their respective metrics, and this can be used to show the Hausdorﬀ dimensions
of X and ι(X) coincide. In particular the standard 3-adic Cantor set Σ3,¯1 maps under ι to the
usual Cantor set in [0, 1] hence it has Hausdorﬀ dimension dH (Σ3,¯1) = log3(2) ≈ 0.63092. Now
Σ3,¯1 = 2Σ3,¯2) hence dimH (Σ3,¯2) = log3(2) as well.

Proof of Theorem 1.5. This proof assumes that Theorem 1.6 is proved in order to deduce
the upper bound in (2).

(1) We have
 E (1)(Z3) =
 ∞⋃

m=0 C(2
m),

with C(2m) := {λ : (λ2n)3 omits the digit 2}. Then

C(2
m) = 1
2m C(1) = 1
2m (Σ3,¯2) = 1
2m+1 (Σ3,¯1).

20

Each C(2m) is a linearly rescaled version of the Cantor set Σ3,¯1 so has Hausdorﬀ dimension
log3 2. Thus
 log3 2 = dimH (C(1)) ≤ dimH (E (1)(Z3)) ≤ sup
m≥0 dimH(C(2
m)) = log3 2,

as required.
(2) We have E (2)(Z3) = ⋃

0≤m1<m2 C(2
m1 , 2
m2 ).

with C(2m1 , 2m2 ) := {λ : (λ2mi)3 omits the digit 2}. Now

C(2
m1 , 2
m2 ) = 1
2m1 C(1, 2
m2−m1),

which gives dimH (C(2m1 , 2m2 )) = dimH(C(1, 2m2−m1)). Since m2−m1 ≥ 1, Theorem 1.6 applies
to give
 dimH (C(1, 2
m2−m1)) ≤ 1
2 , for all m2 > m1 ≥ 0.

This yields the upper bound

dimH(E (2)(Z3)) = sup
0≤m1<m2 dimH(C(2
m1 , 2
m2 )) ≤ 1
2 .

To establish the lower bound, we use the fact that 4 = (11)3. Then the set

ΣA := {λ = (· · · d2d1d0)3 : all blocks d2n+1d2n ∈ {00, 01} } ⊂ Σ3,¯2,

satisﬁes 4ΣA = {λ = (· · · d2d1d0)3 : all blocks d2n+1d2n ∈ {00, 11} } ⊂ Σ3,¯2,

which shows that ΣA ⊂ C(1, 4). Now ΣA is given by a Cantor set construction, which permits
its Hausdorﬀ dimension to be computed in a standard way. We obtain

dimH(E (2)(Z3)) ≥ dimH(C(1, 2
2)) ≥ dimH (ΣA) = log3(2)
log3(9) = 1
2 log3(2) ≈ 0.31596.

(3) We have E (2)(Z3) = ⋃

0≤m1<m2<m3 C(2
m1 , 2
m2 , 2
m3 ).

The upper bound dimH(E (3)(Z3) ≤ dimH(E (2)(Z3) is immediate. To establish the lower bound,
we use the facts that 4 = (11)3 and 256 = (100111)3. Then

ΣB := {λ = (· · · d2d1d0)3 : all d6n+5d6n+4d6n+3d6n+2d6n+1d6n ∈ {000000, 000001} } ⊂ Σ3,¯2.

has

4ΣB = {λ = (· · · d2d1d0)3 : all d6n+5d6n+4d6n+3d6n+2d6n+1d6n ∈ {000000, 000011} } ⊂ Σ3,¯2.

256ΣB = {λ = (· · · d2d1d0)3 : all d6n+5d6n+4d6n+3d6n+2d6n+1d6n ∈ {000000, 100111} } ⊂ Σ3,¯2.

Thus ΣB ⊂ C(1, 4, 256) ⊂ E (3)(Z3). Now ΣB has a Cantor set construction showing that

dimH(ΣB) = log3(2)
log3(36) = 1
6 log3(2) ≈ 0.10515,

which gives the asserted lower bound.
 21

Remark. The proof of Theorem 1.5 exploited the known solutions to Erd˝os’s problem. Con-
sequently this approach does not extend to give a nonzero lower bound for dimH (E (k)(Z3)),
for any k ≥ 4. Theorem 1.7 oﬀers more ﬂexibility in ﬁnding ternary expansion identities for
integers that could potentially yield nonzero lower bounds in these cases.

4. Intersections of Multiplicative Translates of the 3-Adic Cantor Set: Proofs

We study the 3-adic Cantor set Σ3,¯1, deﬁned by

Σ3,¯2 := {λ ∈ Z3 : the 3-adic digit expansion (λ)3 omits the digit 2}. (4.1)

For integers 1 ≤ M1 < M2 < · · · < Mk we deﬁne the intersection set

C(M1, M2, · · · , Mk) := {λ ∈ Z3 : (Miλ)3 omits the digit 2} (4.2)

=
 k⋂

i=1
 1
Mi Σ3,¯1 (4.3)

In §3 we used integers Mi = 2mi but here we allow arbitrary positive integers Mi. We study
C(1, M ) for general M and note ﬁrst that C(1, 3j M ) = C(1, M ).. Thus without loss of generality
we may reduce to the case gcd(M, 3) = 1. Another simple fact is the following.

Lemma 4.1. Let M be a positive integer.

(1) If M ≡ 2(mod 3) then C(1, M ) = {0}.

(2) If M ≡ 1(mod 3) then C(1, M ) is an inﬁnite set.

Proof. (1) Suppose M ≡ 2(mod 3). If C(1, M ) ̸= {0}, then it necessarily contains some λ
with λ ̸= 0(mod 3), since we may divide out any powers of 3, and multiplication by 3j simply
shifts digits to the left. Then λ ∈ Σ3,¯2 implies λ ≡ 1 (mod 3). Then M λ ≡ 2(mod 3) so
M λ ̸∈ Σ3,¯2, a contradicting membership in (1, M ). Hence no such λ exist, and C(1, M ) = {0}.
(2) Suppose M ≡ 1(mod 3). To show C(1, M ) is an inﬁnite set it suﬃces to exhibit one
nonzero element λ ∈ C∗(1, M ), because 3jλ ∈ C∗(1, M ) for all j ≥ 0. We may construct such an
element λ = (· · · d2d1d0)3 recursively, starting with the choice d0 = 1. Write M = ∑n
j=0 aj3j,
with a0 = 1. Let M λ = ∑∞
j=0 cj3j. Then the k-th digit satisﬁes

ck ≡ dk +
 

 n∑

j=1 ajdn−j


 + ek−1 (mod 3)

(with the convention d−1 = d−2 = · · · = d−n = 0), and with ek−1 encoding the ”carry digit” in-
formation, from the previous terms, which is completely determined by (d0, d1, ..., dk−1.) Since
we have two choices 0, 1 for dk, at least one of them will foce ck ̸= 2 (mod 3). Thus we can
recursively construct an admissible λ by induction on k. .

It is possible to make a detailed analysis of the structure of C(1, M ) with M ≡ 1 (mod 3),
and determine their Hausdorﬀ dimensions, which we consider elsewhere. One can show that
inﬁnite set C(1, M ) can be either countable or uncountable, e.g. C(1, 49) is countably inﬁnite,
while C(1, 7) is uncountable.
 22

Now we upper bound the Hausdorﬀ dimension of C(1, M ). For M = 3j, (j ≥ 0) we have
C(1, 3j ) = Σ3,¯2, whence dimH (C(1, 3j )) = log3(2) ≈ 0.63. The following result treats all other
M ≥ 1.

Proof of Theorem 1.6. We suppose that M > 1 is an integer that is not a power of 3,
i.e. its ternary expansion (M )3 contains at least two nonzero ternary digits. Our object is to
upper bound the Hausdorﬀ dimension of

C(1, M ) := Σ3,¯2 ∩ M Σ3,¯2,

by 1
2 . By the discussion above we may reduce to the case that gcd(M, 3) = 1, and by Lemma 4.1
we may suppose M ≡ 1 (mod 3), since the Hausdorﬀ dimension is 0 if M ≡ 2(mod 3). Thus
we can write
 (M )3 = b0 + bm3
m +
 n∑

j=m+1 bj3
j, bj ∈ {0, 1, 2}, with b0bm ̸= 0. (4.4)

and b0 = 1, where the m-th digit is the ﬁrst nonzero ternary digit after the 0-th digit.
We will study the minimal covers of C(1, M ) with 3-adic open sets of measure 3−r−1 that
specify the ﬁrst r + 1 digits of the 3-adic expansion of a number λ ∈ C(1, M ). These sets
are congruence classes ( mod 3r+1) and they have diameter 3−(r+1). We call a congruence class
λ (mod 3r+1) admissible if C∗(1, M ) contains at least one element in this congruence class.
Our object is to bound above the number of admissible congruence classes λ (mod 3r+1)
Set λ = ∑∞
j=0 dj3j ∈ Σ3,¯2, so that each dj = 0 or 1. Now deﬁne the digits aj by

M λ =
 ∞∑

j=0 aj3
j, aj ∈ {0, 1, 2}.

The condition that M λ ∈ Σ3,¯2 means each aj = 0 or 1 which imposes extra constraints on the
dj’s.

Claim 1. Suppose that (d0, d1, ..., d2lm+k−1) with 0 ≤ k < m of λ ∈ C(1, M ) are ﬁxed.
Then at least one of the following conditions holds:

(i) There is at most one admissible value for d2lm+k in λ (mod 32lm+k+1).

(ii) There are two admissible values for d2lm+k for λ (mod 32lm+k+1) and for any ﬁxed
choices of (d2lm+k+1, d2lm+k+2, ..., d(2l+1)m+k−1) at most three of the four possible values of
(d2lm+k, d(2l+1)m+k) give admissible sequences for λ (mod 3(2l+1)m+k).

To prove the claim, suppose that condition (i) doesn’t hold. We then examine the digit
a(2l+1)m+k using

M λ ≡ b0d(2l+1)m+k3
(2l+1)m+k + bmd(2l+m)+k3
(2l+1)m+k

+ M (

2lm+k−1∑

j=0 dj3
j) + b0d2lm+k3
2lm+k (mod 3
(2l+1)m+k+1). (4.5)

23

Deﬁne the digits rj by
 M (

2lm+k−1∑

j=0 dj3
j) =
 ∞∑

j=0 rj3
j, rj ∈ {0, 1, 2}.

We assert that (4.5) then gives the congruence

a(2l+1)m+k ≡ b0d(2l+1)m+k + bmd2lm+k + r(2l+l)m+k (mod 3). (4.6)

That is, we assert there cannot be any extra ”carry digit” from lower order terms that aﬀects
the (2l + 1)m + k-th 3-adic digit, coming from the addition of b0d2lm+k32m+k in (4.5). Namely,
the extra term b0d2lm+k3k, where d2lm+k = 0 or 1 contributes nothing if d2lm+k = 0, while
if d2lm+k = 1 By our assumption that (i) doesn’t hold, both values d2lm+k = 0, 1 occur for
admissible λ(mod 32lm+k) for these digits. Since b0 = 1 and the 3-adic digit of M λ in the
(2lm + k + 1)-st place is 0 or 1, this digit must have been 0 when d2lm+k = 0, and 1 when
d2lm+k = 1, so there can be no ”carry digit” in the addition of b0d2lm+k3k, as asserted.
Now consider the pairs (d2lm+k, d(2l+1)m+k). Of the four values (00), (01), (10), (11) that
these may take, the quantities b0d(2l+1)m+k +bmd2lm+k with b0 = 1 and bm = 1 or 2 will cover all
residue classes ( mod 3). In particular, at least one choice will result in a(2l+1)m+k ≡ 2 ( mod 3)
in (4.6), and so give a non-admissible set of digits (mod 3(2l+1)m+k). This proves (ii), and the
claim.

Claim 2. For M having the ternary expansion (4.4) and a given r ≥ 2m there are are at
most 3 1
2 r+2m admissible congruence classes in C(1, M ) (mod 3r).

To prove the claim, we group the 3-adic digits in pairs (d2jm+k, d(2j+1)m+k)), 0 ≤ k < m,
for all pairs with (2j + 1)m + k ≤ r. There are at most 2m − 1 unpaired digits. Claim 1
establishes that, conditional on the choice of all other allowed digits, there are at most three
permitted choices for the set of paired digits. For each unpaired digit there are at most two
choices for its value. Since the number of paired digits is at most 1
2 (r + 1) the total number of
admissible sequences (mod 3r+1) is at most 3 1
2 (r+1)22m−1, which implies Claim 2.

To conclude the proof, Claim 2 implies that we have a covering Ir of C(1, M ) with a set of
at most 3
( 1
2 r+2m sets, each of diameter 3−(r+1). For each ǫ > 0 this covering satisﬁes
∑

I∈Ir |I| 1
2 +ǫ ≤ 3
( 1
2 r+2m(3
−(r+1)) 1
2 +ǫ ≤ 3
−(r+1)ǫ.

Letting r → ∞, this bound implies dimH(C(1, M )) ≤ 1
2 + ǫ. Letting ǫ → 0 gives the result.

We do not know whether the bound in Theorem 1.5 is sharp. However it is possible to
show that C(1, 7) has dimH C(1, 7) = log3( 1+√5
2 ) ≈ 0.43.

Proof of Theorem 1.7. We suppose are given N a positive integer with N ∈ Σ3,¯2 ∫ Z and
1 ≤ M1 < M2 < · · · < Mk with all N Mi ∈ Σ3,¯2. Our object is to obtain an explicit nonzero
lower bound on the Hausdorﬀ dimension dimH(C(M1, M2, · · · , Mk)). We set n equal to the
number of ternary digits in N Mk, so that n = ⌈log3 N Mk⌉. Now we consider the set

ΣC := {λ = (· · · d2d1d0)3 : all blocks d(k+1)n−1 · · · dkn+1dkn ∈ {0
n, (N )3} } ⊂ Σ3,2.

24

Since each N Mj ∈ Σ3,¯2 is an integer with at most n ternary digits, we have

MjΣC := {λ = (· · · d2d1d0)3 : all blocks d(k+1)n−1 · · · dkn+1dkn ∈ {0
n, (N Mj)3} } ⊂ Σ3,¯2.

Thus ΣC ⊂ C(M1, M2, · · · , Mk). By inspection ΣC is a Cantor set which has Hausdorﬀ dimen-
sion
 dimH ΣC = log3(2)
log3(3n) = log3(2)
⌈log3(N Mk)⌉ ,

and the result follows. .

5. Furstenberg Conjecture and Transversality of Semigroup Actions

In 1970 Furstenberg [10, p. 43] formulated the following conjecture which is in the same
direction as Erd˝os’s question.

Conjecture 2
′. (Furstenberg) Suppose p and q are not powers of the same integer. Then the
expansions to the base B = pq of the powers {(pn)pq : n ≥ 1} have the property that any given
ﬁnite pattern of consecutive base B digits occurs in (pn)pq for all suﬃciently large n.

For example, for p = 2 and q = 3, this conjecture asserts that any given pattern of base B = 6
digits will occur as consecutive digits in the base 6 expansion of (2n)6, for all suﬃciently large
n. The restriction to products B = pq of two (or more) multiplicatively independent elements
was motivated by results in Furstenberg’s seminal work [9]. There he showed that for any
irrational number θ the set {pmqnθ(mod 1) : m, n ≥ 0} is dense on the torus R/Z. However it
is well known that there is an uncountable set of irrational numbers θ for which {pmθ : m ≥ 0}
is not dense on the torus.
Conjecture E in the introduction proposes nevertheless that Furstenberg’s conjecture con-
tinues to hold when the base B = q is a prime (in the special case p = 2, q = 3). More
generally one can ask whether Furstenberg’s conjecture might be valid more generally for base
B expansions for arbitrary B with gcd(B, p) = 1.
A main object of Furstenberg [10] was to introduce a notion of transversality of two semi-
groups of transformations S1 and S2 acting on a compact metric space X with respect to a
(suitable) dimension function dim(A) deﬁned on all closed sets A.

Deﬁnition 5.1. Two closed sets A and B in a compact metric space X are transverse (for a
given dimension function) if

dim(A ∩ B) ≤ max(dim(A) + dim(B) − dim(X), 0).

Deﬁnition 5.2. Two semigroups S1 and S2 acting on a compact metric space X are transverse
(for a given dimension function) if any closed S1-invariant set A and any closed S2-invariant
set B are themselves transverse, for that dimension function.

He obtained as an immediate consequence of this deﬁnition the following result concerning
simultaneous invariant sets ([10, p. 42]), which draws on earlier work ([9]).

25

Proposition 5.1. (Furstenberg) Suppose that S1 and S2 are transverse semigroups acting on
a compact metric space X, and that S1 has the additional property:

(*) If A is a closed S1-invariant set with dim(A) = dim(X), then A = X.

Then any proper closed subset of X invariant under both S1 and S2 has dim(A) = 0.

Furstenberg does not construct any transverse semigroups, but as evidence for their exis-
tence shows for the following pair of tranformation semigroups that their (nontrivial) simulta-
neously invariant closed sets satisfy this property ([10, Theorem 3]).

Proposition 5.2. (Furstenberg) Let Zr be the ring of r-adic integers, and suppose that r = pq
with p > 1 and q > 1 not both powers of the same integer. Deﬁne transformations Ds(x) = ⌊ x
s ⌋,
for s = p, q, and pq, and note that Dpq = DpDq = DqDp. Let Sp and Sq denote the semigroups
generated by Dp and Dq, respectively. If A is a simultaneously Sp and Sq invariant proper
closed subset of Zr, then A has Hausdorﬀ dimension zero.

The proof of this result draws on his earlier work ([9]). Furstenberg [10, p. 45] goes on to
conjecture that Sp and Sq are transverse semigroups acting on Zr.
Conjectures A and B in the introduction are partially motivated by Furstenberg’s frame-
work but fall outside it. One could approach Conjecture A by considering only the ternary
expansions of fractional parts {{λ2n}}, and thus iterating x → 2x on the compact space
X = R/Z. This deﬁnes a larger exceptional set E(R/Z), which contains E(R). Does E(R/Z)
have Hausdorﬀ dimension zero? This set includes all dyadic rationals (thus λ = 1), which is
a dense set in R/Z, so its closure is the whole space X, and is not covered by Furstenberg’s
results.
Furstenberg’s formulation does not apply to semigroups of transformations on the real
numbers because R is not compact. One may ask: Can Furstenberg’s framework be generalized
to apply to semigroups of operators acting on the real numbers, or the integers?

6. Concluding Remarks

We conclude by reviewing some history related to Erd˝os’s question. Erd˝os [4] raised his question
on ternary expansions of 2n in connection with his conjecture that the binomial coeﬃcient (2n
n )

is not squarefree for all n ≥ 5. This binomial coeﬃcient is divisible by 4 except for n = 2k, so
it is natural to examine when larger primes divide (2k+1
2k ). Here one has

3 does not divide (2k+1

2k
 ) ⇐⇒ The ternary expansion of 2
n omits the digit 2,

as follows from Lucas’s theorem (Lucas[16], see Graham et al. [14, Exercise 5.61]). This led
Erd˝os to raise his ternary expansion question, since a positive answer to it would establish his
binomial coeﬃcient conjecture.
As it turned out, Erd˝os’s binomial coeﬃcient conjecture was later resolved aﬃrmatively,
without answering the ternary expansion question. In 1985 Sarkozy [21] proved that (
2n
n )

is not squarefree for all suﬃciently large n. About 1995, Granville and Ramar´e [11] and,
independently, Velammal [24] proved it for all n ≥ 5.
The theme of this paper is that Erd˝os’s unconventional question retains interest for its own
sake, even though the problem that originally motivated its study has been solved.

26

References

[1] A. Baker, Transcendental Number Theory, Cambridge University Press: Cambridge 1975

[2] A. Dubickas, Arithmetical properties of powers of algebraic integers, Bull. Lond. Math.
Soc. 38 (2006), 70–80.

[3] A. Dubickas and A. Novikas, Integer parts of powers of rational numbers, Math. Z. 251
(2005), 635–648.

[4] P. Erd˝os, Some unconventional problems in number theory, Math. Mag. 52, No. 2 (1979),
67–70.

[5] P. Erd˝os and R. L. Graham, Old and New Problems and Results in Combinatorial Number
Theory, Monograph No. 28 de L’Enseign. Math., Univ. of Geneva 1980.

[6] K. Falconer, The geometry of fractal sets, Cambridge Tracts in Mathematics No. 85,
Cambridge Univ. Press: Cambridge 1985.

[7] K. Falconer, Fractal Geometry: Mathematical Foundations and Applications, John Wiley
& Sons: Chichester 1990.

[8] L. Flatto, J. C. Lagarias and A. Pollington, On the range of fractional parts {ξ( p
q )n}, Acta
Arith. 70 (1995), 125–147.

[9] H. Furstenberg, Disjointness in ergodic theory, minimal sets, and a problem in Diophantine
approximation, Math. Systems Theory 1 (1967) 1–49.

[10] H. Furstenberg, Intersections of Cantor sets and transversality of semigroups, in: Problems
in Analysis: (Symposium Salomon Bochner, Princeton Univ. 1969), pp. 41–59, Princeton
Univ. Press; Princeton 1970.

[11] A. Granville and O. Ramar´e, Explicit bounds on exponential sums and the scarcity of
sqarefree binomial coeﬃcients, Mathematika 43 (1996), 73–107.

[12] H. Gupta, Powers of 2 and sums of distinct powers of 3, Univ. Beograd Publ. Elecktrotehn.
Fak. Ser. Mat. Fiz. No. 602–633 (1978), 151–158. (MR 0580438)

[13] R. K. Guy, Unsolved Problems in Number Theory, Second Edition, Springer-Verlag: New
York 1994.

[14] R. L. Graham, D. Knuth and O. Patashnik, Concrete Mathematics, Second Edition.
Addison-Wesley: Reading, Mass. 1994.

[15] D. Lind and B. Marcus, An Introduction to Symbolic Dynamics and Coding, Cambridge
Univ. Press: Cambridge 1995.

[16] E. Lucas, Sur les congruences des nombres eul´eriens et des coeﬃcients diﬀ´erentials des
fonctions trigonom´etriques, suivant un module premier, Bull. Soc. Math. France 6 (1878),
49–54.

[17] R. D. Mauldin and S. C. Williams, Hausdorﬀ dimension in graph directed constructions,
Trans. Amer. Math. Soc. 309 (1988), 811–829.

27

[18] W. Narkiewicz, A note on a paper of H. Gupta concerning powers of 2 and 3, Univ. Beograd
Publ. Elecktrotehn. Fak. Ser. Mat. Fiz. No. 678–715 (1980), 173–174. (MR 0623247)

[19] G. Rhin, Approximants de Pad´e et mesures eﬀectives d’irrationalit´e, Progress in Mathe-
matics, 71 (1987), 155–164.

[20] C. A. Rogers, Hausdorﬀ Measures, Cambridge University Press: Cambridge 1970.
(Reprint: 1998).

[21] A. S´ark¨ozy, On divisors of binomial coeﬃcients I, J. Number Theory 20 (1985) , 70–80.

[22] J. Simons and B. M. M. de Weger, Theoretical and computational bounds for m-cycles of
the 3n + 1 problem, Acta Arith. 117 (2005), 51–70.

[23] N. E. Slater, Gaps and steps for the sequence nθ (mod 1), Math. Proc. Camb. Phil. Soc.
63 (1967), 1115–1123.

[24] G. Velammal, Is the binomial coeﬃcient (2n
n ) squarefree?, Hardy-Ramanujan J. 18 (1995),
23–45.

Jeﬀrey C. Lagarias
Dept. of Mathematics
The University of Michigan
Ann Arbor, MI 48109-1043
email: lagarias@umich.edu
 28
