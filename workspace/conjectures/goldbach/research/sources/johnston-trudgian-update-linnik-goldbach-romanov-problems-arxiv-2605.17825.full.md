<!-- source: https://arxiv.org/pdf/2605.17825 | converted from PDF -->

An update on the Linnik–Goldbach problem

Daniel R. Johnston
Max Planck Institute for Mathematics, Bonn, Germany
johnston@mpim-bonn.mpg.de

Tim Trudgian
School of Science, UNSW Canberra, Australia
timothy.trudgian@unsw.edu.au

RHB at 50 proved that seven 2’s would do.
Twenty-five years later, we show six in this review.
We wish him to his century when proofs of 5 are due!

Abstract

We consider the Linnik–Goldbach problem of writing all large even integers as the sum
of two primes and a fixed number of powers of 2. We show that, under the generalised
Riemann hypothesis, one can use 6 powers of two. In addition, we discuss refinements to
the unconditional case and to the related problem of Romanov in expressing a positive
proportion of odd numbers as the sum of a prime and a power of 2.

1 Introduction

We refine the numerical bounds for the Linnik–Goldbach problem — a well-studied
problem in number theory. The main source of improvement arises from new bounds on
Goldbach representations due to Lichtman [15]. However, there are other minor optimisations
we employ. The goal of this paper is to both showcase these new bounds, and also survey the
most recent techniques for tackling the Linnik–Goldbach problem and the related problem of
Romanov. Throughout, p, possibly with a subscript (e.g. p1, p2, p3), is assumed to be prime.
Moreover, φ(·) denotes the Euler totient function and (a, b) stands for gcd(a, b).

DRJ and TT are supported by Australian Research Council Discovery Project DP240100186.
Key phrases: Linnik–Goldbach problem, Romanov problem, Goldbach’s conjecture, sieve methods
2020 MSC codes: 11N36, 11P32 (Primary) 11M26, 11P55 (Secondary)

1

arXiv:2605.17825v2  [math.NT]  22 Jul 2026

1.1 The Linnik–Goldbach problem

Linnik’s approximation of Goldbach’s conjecture asks for the smallest K ≥ 0 such that
every large even integer can be expressed as the sum of two primes and K powers of 2:

n = p1 + p2 + 2ν1 + · · · + 2
νK . (1)

Linnik [17] was the first to show that K exists; the first values of K were very large (see e.g.
[18]). However, after a series of improvements, Heath-Brown and Schlage-Puchta [11] were
able to obtain K = 7 assuming the generalised Riemann hypothesis (GRH). Unconditionally,
they were able to use some zero-density results by Heath-Brown [9] to show
1 that K = 13 is
admissible. Pintz and Ruzsa [26, 27] independently obtained the same result (K = 7) under
GRH and K = 8 unconditionally. We show it is now possible to obtain K = 6 under GRH.

Theorem 1. Assuming GRH, every sufficiently large even integer can be expressed as the
sum of two primes and K = 6 powers of 2.

The main estimate required to obtain Theorem 1 is an upper bound on Goldbach
representations due to Lichtman [15], which we detail in Sections 1.3 and 2. Later in Table 1,
we display the parameters required to achieve further improvements, both conditionally and
unconditionally. Notably, we fall just short of obtaining K = 7 unconditionally with our
setup. However, recently announced work of Maynard, Pandey and Radziwi l l on exponential
sums over primes should allow one to easily overcome this barrier and attain K = 7. We
discuss this further in Section 3.3. We also remark that K = 4 is possible upon assuming
the Elliott–Halberstam conjecture (see Conjecture 1 and Theorem 3).

1.2 The Romanov problem

A very closely related problem to the Linnik–Goldbach problem is the Romanov problem,
which concerns n that can be expressed as the sum of a prime and a power of 2:

n = p + 2
a.

In this context, we define
 d(N ) := |{n ≤ N : n = p + 2a}|
N

to be the density of such numbers less than N , and

d = lim inf
N →∞ d(N )

1Included in [11] is a note about unpublished work by Elsholtz, which shows that K = 12 is admissible.

2

be the lower density. The fact that d > 0 is due to Romanov [29], and an explicit value for
the lower bound for d is often referred to as Romanov’s constant. Currently, the best known
lower bound for d is d ≥ 0.10788. (2)

due to2 Elsholtz and Schlage-Puchta [3]. Given the improvement we attain in the Goldbach-
Linnik problem, it seems natural that an improvement should be possible in the Romanov
problem too. However, due to a technicality in Elsholtz and Schlage-Puchta’s argument, this
is actually not possible. Instead, we must revert to an older technique for bounding d due to
Pintz [24]. Here, Lichtman’s new bound for Goldbach representations leads to d ≥ 0.10695.
Although this improves upon Pintz’s original bound, it unfortunately falls short of beating
Elsholtz and Schlage-Puchta’s bound (2).
In any case, given the recent activity in improving bounds for Goldbach representations,
it seems that sharper bounds in the Romanov problem are within reach. For this reason,
in Section 4, we include additional discussion on the Romanov problem, and a table of
parameters required for further refinements.

1.3 Upper bounds for Goldbach representations

For an even number N > 2, let

G(N ) = #{(p1, p2) ∈ N2 : 2 < p1, p2 < N, p1 + p2 = N } (3)

denote the number of Goldbach representations of N . Bounds for G(N ) have historically
been linked to the Linnik–Goldbach and Romanov problems. We remark that Hardy and
Littlewood [8, Conjecture A] conjectured that

G(N ) ∼ 2C0N
(log N )2 ∏

p|N
p>2
 p − 1
p − 2 ,

where
 C0 = ∏

p>2
 (1 − 1
(p − 1)2
 ) = 0.66016 . . . (4)

is the twin-prime constant. Although a non-zero lower bound on G(N ) is out of reach, we
have upper bounds of the form

G(N ) ≤ (C ∗ + ε) C0N
(log N )2 ∏

p|N
 p − 1
p − 2 , (5)

2A slightly weaker bound is actually given in [3, Theorem 1]. However, upon repeating the relevant
computations we obtained the bound given in (2), which is also stated at the end of page 721 of [3].

3

with C ∗ ≥ 2 and ε > 0 arbitrarily small. The value C ∗ = 8 is commonly cited in the
literature, and readily follows from classical sieve methods and the Bombieri–Vinogradov
theorem (see [1, Theorem 2] and [10, Theorem 3.1]). Using carefully weighted sieves, the
value of C ∗ can be lowered, with Chen [2] proving C ∗ = 7.8342 in 1978, and Wu [30] proving
C ∗ = 7.8209 in 2004.
In recent years, there has been breakthrough work on variants of the Bombieri–
Vinogradov theorem, allowing for smaller admissible values of C ∗. The foundation was laid
down by Maynard [19, 20, 21] and enhanced by Lichtman [15, 16] and Pascadi [23]. Notably,
in [15] the value C ∗ = 6.7814 is attained, a significant improvement on previous work.

Proposition 1 ([15, Theorem 1.2]). The bound (5) holds with C ∗ = 6.7814.

We remark that in [23, p. 4], Pascadi suggests that with an extension of his techniques,
one should be able to reduce C ∗ further than the value given in Proposition 1.
For the purpose of proving Theorem 1, we actually need a slight variation of Proposition 1
(see Proposition 2). This is discussed in the next section.

2 Statement of sieve upper bound results

In this section, we detail Lichtman’s recent upper bound for Goldbach representations,
and also provide a variant of Proposition 1 for use in the Linnik–Goldbach problem. Here,
it is useful for the reader to have a basic understanding of sieve-theoretic arguments, which
are detailed in texts including [7, 6, 4].
In the standard approach for the Linnik–Goldbach problem, we require upper bounds for

R(N, h) := #{p1, p2 ≤ N : p1 − p2 = h}. (6)

In the following subsections, we first outline the standard argument to obtain bounds for
G(N ), then describe how in [15], Lichtman managed to obtain Proposition 1. Afterwards,
we discuss the very minor modification to obtain a bound for R(N, h) as opposed to G(N ).

2.1 Bounding G(N )

To bound G(N ), defined in (3), one may equivalently bound the number of primes in

A = A(N ) := {N − p : p ≤ N, (p, N ) = 1}. (7)

Via a standard sifting argument (see [7, Theorem 3.11]) an upper bound for G(N ) can be
found by approximating the size of the sets Ad := {a ∈ A : d | a}, where d is square-free
and coprime to N . In particular, one has

#Ad = π(N ; d, N ) + O(log N ), (8)

4

where π(N ; d, a) := #{p ≤ N : p ≡ a (mod d)} and the O(log N ) term in (8) comes from
considering the number of primes p with (p, N ) > 1. In turn, one is led to computing an
averaged form of the error
 E(N ; d, a) := π(N ; d, a) − π(N )
φ(d) ,

where π(N ) := π(N ; 1, 1). The classical approach (as employed in the proof of [7,
Theorem 3.11]) is to use the Bombieri–Vinogradov theorem, which states that for any ε > 0,
∑

d≤xθ−ε max
(a,d)=1 |E(x; d, a)| ≪ε,A x
(log x)A , (9)

with θ = 1/2. Here, θ is referred to as the level of distribution of primes: a central problem
in analytic number theory is to prove that higher values of θ are admissible. Essentially, the
higher the value of θ, the better sieve-theoretic estimates are possible, with θ = 1/2 readily
giving a constant of C ∗ = 8 in (5). The Elliott–Halberstam conjecture asserts that θ = 1 is
possible, which would lead to a constant of C ∗ = 4 in (5).

Conjecture 1 (Elliott–Halberstam). The bound (9) holds with θ = 1.

In practice, one does not require the full statement of the Bombieri–Vinogradov theorem.
The absolute values in (9) can be replaced by a suitable weight λ(d). Indeed, in [15,
Theorem 1.7], Lichtman shows that

sup
0<|a|<x1+ε
 ∑

d≤xθ−ε λ(d)E(x; d, a) ≪ε,A x
(log x)A , (10)

where θ = 153/256 ≈ 0.597 and λ(d) is triply well-factorable of level x
θ as defined in [15,
Definition 1.4]. Compared to previous work [20, 16], the main novelty of Lichtman’s result
is the uniformity in the residue a, which is required when bounding G(N ).
Unfortunately, the weights ̃λ(d) arising
3 in the linear sieve are not triply well-factorable
but merely “doubly” well-factorable. Because of this, Lichtman provides a technical result [15,
Proposition 6.6] which shows that one can get a level of distribution with the sieve weights
̃λ(d) that is at most θ = 153/256, but often lower depending on the divisor structure of the
moduli d under consideration. In any case, Lichtman goes beyond the level of distribution
offered by the Bombieri–Vinogradov theorem, and obtains C ∗ = 6.7814 in (5) using a
procedure of Wu [30] in [15, §7].

3In particular, the weights introduced by Iwaniec in [12].

5

2.2 Bounding R(N, h)

Compared to G(N ) (cf. (7)), to bound R(N, h) one considers the set

A
′ = A
′(N, h) := {p + h : p ≤ N, (p, h) = 1}

and via a sifting argument one is required to approximate

#A
′
d := #{a ∈ A′ : d | a} = π(N ; d, −h) + O(log h) (11)

with d square-free and (d, h) = 1. We note that the expressions (8) and (11) are identical
but with the residue class N replaced with −h. So, since the results in [15] (see (10)) are
uniform in the residue class, the argument required to bound R(N, h) is identical to that of
bounding G(N ). In particular, one obtains the following, which mirrors Proposition 1.

Proposition 2. Let ε > 0. Then, for all h < N ,

R(N, h) ≤ (C1 + ε) C0N
(log N )2 ∏

p|h
p>2
 p − 1
p − 2 (12)

with C1 = 6.7814 and C0 as in (4).

A key feature of Proposition 2 is the uniformity of h < N . If instead h < (log N )D for
some D > 0, then a “small residue” sieving argument could be used, leading to the lower
value of C1 = 6.458 as per [15, Theorem 1.1].
To conclude this section, we also make note of the improvement one gets upon assuming
the Elliott–Halberstam conjecture (Conjecture 1). In particular, for R(N, h) the situation is
exactly the same as the case of G(N ), whereby replacing the Bombieri–Vinogradov theorem
(level of distribution θ = 1/2) with the Elliott–Halberstam conjecture (level of distribution
θ = 1) gives C1 = 4.

Proposition 3. Assuming the Elliott–Halberstam conjecture, one may take C1 = 4 in (12).

3 The Linnik–Goldbach problem

In this section, we explore the modern framework of the Linnik–Goldbach problem, both
in the GRH and non-GRH cases, and prove Theorem 1. We include Table 1 to show what
further results are possible if C1 in (12) is lowered. Throughout, a basic understanding of
the circle method is assumed, such as that found in the introductory text [22].

6

3.1 The method of Pintz and Ruzsa

We begin by detailing the core argument of Pintz and Ruzsa [26, 27], which is the most
recent approach to the Linnik–Goldbach problem. The key result is Theorem 2, which allows
one to obtain a valid value for K in the Linnik–Goldbach problem, by inputting well-studied
number-theoretic constants. The overall method is very similar to previous approaches,
including that of Heath-Brown and Schlage-Puchta [11] and a subsequent refinement by
Platt and Trudgian [28]. However in [27], Pintz and Ruzsa make use of an “explicit formula”
of Pintz [25], which allows for great flexibility when applying the circle method.
In what follows, we set n = N to be a sufficiently large even number to be studied in
the context of the Linnik–Goldbach problem (see (1)) and L = [log N/ log 2]. In [27], a lower
order term is also included in the definition of L for technical purposes. However, we omit
this term as it has no impact on the final asymptotic result.
In the setup for the Linnik–Goldbach problem, one studies two representation functions

r′
k(n) = ∑

n=p+2ν1 +···+2νk log p (13)

and r′′
k(n) = ∑

n=p1+p2+2ν1 +···+2νk log p1 log p2,

where one wants to show r′′
k(N ) > 0. To do so, one uses L
1 and L
2 estimates for r′
k(n),
combined with Cauchy–Schwarz. The L
1 estimate is the following asymptotic.

Lemma 1 (cf. [5, Lemma 14]). For any fixed k ≥ 1, one has ∑

n≤N r′
k(n) ∼ N L
k.

Proof. Write ∑

n≤N r′
k(n) = ∑

p≤N f (N − p) log p

where f (x) is the number of k-tuples v1, . . . , vk with vi ≤ L and

2
v1 + · · · + 2
vk ≤ x.

Notably, ⌊ log(x/k)
log 2
 ⌋k ≤ f (x) ≤ (log x
log 2
 )k (14)

so that f (x) ∼ (log x/ log 2)
k. Now, let θ(x) = ∑

p≤x log p denote the Chebyshev weighted
prime-counting function. Since f is a non-negative increasing function,
∑

p≤N f (N − p) log p ≤ f (N )θ(N ) (15)

7

and ∑

p≤N f (N − p) log p ≥ ∑

p≤N −N/L f (N − p) log p ≥ θ(N − N/L)f (N/L). (16)

The result then follows by applying (14) and the prime number theorem to (15) and (16).

To obtain the L2 bound, Pintz and Ruzsa use a technical application of the circle method.
Before stating their bound, we define the number-theoretic constants involved.
To begin with, C0 is the constant (4), C1 is as in Proposition 2, and R0 is given by

R0 =
 ∞∑

d=1
 f (2d − 1)
ϵ(2d − 1) ,

where f (n) is the multiplicative function defined by

f (p
e) =
 {
0, p = 2 or e ≥ 2

(p − 2)−1, otherwise,

and where ϵ(d) is the multiplicative order of 2 mod d. Existing computations of R0 (see [28,
p. 55]) yield that 1.93642 < R0 < 1.93656. (17)

Pintz and Ruzsa then use a function A(k) related to representations of integers as the sum
and difference of powers of 2. Explicitly, A(k) is defined as

A(k) := lim
L→∞
 ( S(k, L)
2L2k − 1) ,

where

S(k, L) :=
 ∞∑

m=−∞
m̸=0
 rk,k(m)σ(m),

rk,k(m, L) := #{(a1, · · · , a2k) ∈ {0, . . . , L}
2k : m = 2a1 + · · · + 2
ak − 2ak+1 − · · · − 2
a2k}

and σ(m) := 2C0 ∏

p|m
p>2
 p − 1
p − 2 .

Khalfalah and Pintz proved several properties of A(k) in [13, Theorem 1]. They showed
that A(k) is decreasing with k and limk→∞ A(k) = 0. Moreover, A(k) > 2−2k−1 for all k ≥ 1,
and, in addition, the following explicit bounds hold ([13, Theorem 2])

0.27835 < A(1) < 0.27926, 0.05458 < A(2) < 0.05549,

8

0.012697 < A(3) < 0.013598, 0.003091 < A(4) < 0.003992.

For their application of the circle method, Pintz and Ruzsa use the standard definitions
of major and minor arcs. In particular, one lets P and Q be such that

2 ≤ P < Q = N
P

and the major (M) and minor (m) arcs be given by

M = ⋃

q≤P
 q⋃

a=1
(a,q)=1
 [ a
q − 1
qQ, a
q + 1
qQ
]

m = [1/Q, 1 + 1/Q] \ M.

From here, one then estimates (via Parseval’s identity)

∑

1≤n≤N(r′
k(n))
2 ≤ ∫ 1

0 |S(α)Gk(α)|2dα = ∫

M |S(α)G
k(α)|2dα + ∫

m |S(α)G
k(α)|2dα,

where S(α) = ∑

p≤N e(pα) log p and G(α) = ∑

1≤ν≤L e(2
να).

A key quantity is an acceptable choice of the “cut-offs” P and Q. Assuming GRH, Pintz
and Ruzsa take P = √N L−8 and Q = √N . This is sufficient to give an asymptotic for the
major arcs [26, Lemma 1] and a suitable minor arc estimate. Unconditionally, the work of
Pintz [25] allows one to take P as large as P = N 4/9−ε to give an asymptotic for the major
arcs. In general, it is preferable to take P as large as possible, so we will just set

P = √
N L−8 (assuming GRH),

P = N 4/9−ε (unconditionally)

with ε > 0 fixed. In [27], Pintz and Ruzsa set P ∈ [N 0.4, N 0.41] but there is no harm in
setting P to be larger here. Namely, for α ∈ m one just needs the minor arc estimate ([27,
Lemma 2])
 S(α) ≪ ( N
√P + N 4/5 + √N P ) L4 ≪ L
4N 4/5 (18)

to hold, which is valid for any P ∈ [N 0.4, N 0.6].
Next, we define the constant C ′
2, explicitly given as (see [27, Section 4])

C ′
2 = 1
2(C1 + ε − 2)R0C0 + (
1 − log P
log N
 ) log 2
2 . (19)

9

We note that the log P/ log N term in (19) is omitted in [27], but as remarked on [27, p. 578]
it may be incorporated for additional optimisation.
Finally, we introduce the parameter c1, given by (see [26, §7] and [27, §5])

c1 = 0.7163436 (assuming GRH),

c1 = 0.7894009 (unconditionally). (20)

To define c1 in a precise manner, suppose that, for some 0 < σ < 1, we have an estimate

S(α) ≪ N σ+ε (21)

for α ∈ m and some arbitrarily small ε > 0. Then c1 is any constant such that there exists a
set E with µ(E) = N 1−2σ for which

|G(x)| =
 ∣
∣
∣
∣
∣
L−1∑

j=0 e(2
jx)
∣
∣
∣
∣
∣ < c1L (22)

holds for all x ∈ [0, 1] \ E. Thus, unconditionally one computes c1 using σ = 4/5 by (18).
Then, under GRH, Pintz and Ruzsa use σ = 3/4, which follows from an exponential sum
estimate of Hardy and Littlewood [8, Lemma 9]. The actual computation to obtain the values
of c1 in (20) is nontrivial, and is explained in detail in [26, §4-7].
With all of the notation above, Pintz and Ruzsa obtain the following L
2 estimate.

Lemma 2 (See [26, Lemma 13] or [27, Lemma 9]). With A(k), C ′
2 and c1 as defined above,
one has, for ε > 0 and sufficiently large N ,
∑

n≤N(r′
k(n))
2 ≤ 2N L2k(1 + A(k) + C ′
2c2k−2
1 + ε).

Finally, from here, one then obtains the following result, which allows us to compute a
value of K in the Linnik–Goldbach problem.

Theorem 2 (Pintz–Ruzsa [26, 27]). Let K ≥ 2 and i, j ≥ 1 be such that K = i + j with
i = j or i = j + 1 depending on whether K is even or not. Then, using the notation above, if
√
A(i) + C ′
2c2i−2
1
 √
A(j) + C ′
2c2j−2
1 < 1, (23)

then every sufficiently large even number is the sum of two primes and K powers of 2.

Proof. To begin with, we note that by Lemma 1, the average value of r′
k(n) (with n odd) is
2N Lk. Therefore, the difference
 sk(n) := r′
k(n) − 2Lk

10

satisfies ∑

n≤N
2∤n
 sk(n) = o(N L
k).

The goal now is to establish, for every large even N , the positivity of

r′′
K(N ) = ∑

m+n=N
2∤m
2∤n
 r′
i(m)r′
j(n)

= ∑

m+n=N
2∤m
2∤n
 si(m)sj(n) + 2Lj ∑

m≤N
2∤m
 si(m) + 2Li ∑

n≤N
2∤n
 sj(n) + 4LK ∑

m+n=N
2∤m
2∤n
 1

= ∑

m+n=N
2∤m
2∤n
 si(m)sj(n) + 2LKN + o(N LK). (24)

To deal with the sum over si(m)sj(n), we apply Cauchy–Schwarz, giving

∑

m+n=N
2∤m
2∤n
 si(m)sj(n) ≤
 



 ∑

m≤N
2∤m
 si(m)
2





1/2 



∑

n≤N
2∤n
 sj(n)2





1/2
 . (25)

Now, by applying both the L1 bound (Lemma 1) and the L
2 bound (Lemma 2)
∑

m≤N
2∤m
 si(m)
2 = ∑

m≤N
2∤m
 (r′
i(m) − 2Li)2

= ∑

m≤N
2∤m
 r′
i(m)
2 − 4Li ∑

m≤N
2∤m
 r′
i(m) + 4L2i ∑

m≤N
2∤m
 1

≤ 2N L2i (
A(i) + C ′
2c2i−2
1 + ε) (26)

and analogously for the sum over sj(n)
2. Substituting (26) into (25) and then (24) completes
the proof.

3.2 Proof of Theorem 1

From Theorem 2 and Proposition 2, the proof of Theorem 1 readily follows.

Proof of Theorem 1. Setting K = 6 in Theorem 2, assuming GRH and setting C1 = 6.7814
(from Proposition 2) gives that the left-hand side of (23) is bounded above by

A(3) + C ′
2(0.7163436)
4 ≤ 0.865 < 1.

11

Table 1: The value of C1 required to solve the Linnik–Goldbach problem for K powers of 2,
as computed via Theorem 2.

K Assuming GRH C1 required K Assuming GRH C1 required
7 Yes 9.958 7 No 6.737
6 Yes 7.589 6 No 5.672
5 Yes 5.859 5 No 4.782
4 Yes 4.608 4 No 4.069
3 Yes 3.613 3 No 3.398
2 Yes 2.856 2 No 2.826

Given the recent breakthrough work of Lichtman [15] and Pascadi [23], it seems likely that
the value of C1 = 6.7814 (from Proposition 2) may be lowered further. In Table 1 we thereby
list the value of C1 required to get different values of K in the Linnik–Goldbach problem.
Notably, we are very close to obtaining K = 7 unconditionally. In the next subsection, we
detail how recently announced work should allow one to overcome this K = 7 barrier.
We also recall that assuming the Elliott–Halberstam conjecture (Conjecture 1) one may
take C1 = 4 (Proposition 3), giving the following result.

Theorem 3. Assume the Elliott–Halberstam conjecture. Then the Linnik–Goldbach problem
holds with K = 4.

3.3 Bounds on exponential sums over primes

Recall Vinogradov’s exponential sum bound over the minor arcs (equation (18)):

S(α) ≪ ( N
√
P + N 4/5 + √N P ) L4 ≪ L
4N 4/5.

Recently, Maynard, Pandey and Radziwi l l4 have announced an improvement to this classical
bound, obtaining a power saving on the critical N 4/5 term. In particular, they are able to
reduce this term to N 19/24+ε.
In our notational setup for the Linnik–Goldbach problem, this amounts to setting
σ = 19/24 in (21). Consequently, one can use a lower value (unconditionally) for c1 in
Theorem 2. To test this numerically, we used the existing code by Languasco5, first used
in [14], to compute a valid value for c1 in (22) with σ = 19/24. This gives the value of

c1 = 0.77779.

4See for example, Maynard’s abstract at the 2026 Probability in Number Theory workshop in Montreal.
5Available at codeocean.com/capsule/5525188/tree/v2.

12

Substituting this new value of c1 into Theorem 2 with K = 7 and C1 = 6.7814 (from
Proposition 2) yields √A(4) + C ′
2c6
1√
A(3) + C ′
2c4
1 ≤ 0.934,

thereby showing that every sufficiently large even number is the sum of two primes and 7
powers of 2. Given the preliminary nature of Maynard, Pandey and Radziwi l l’s work, we have
not listed this as a theorem. In any case, we even this small improvement to Vinogradov’s
bound (note 19/24 = 0.79166 . . .) has a sizeable impact on the Linnik–Goldbach problem.

4 Romanov’s constant

In this section we detail the impact of the constant C1 (in Proposition 2) on the value one
obtains for Romanov’s constant as defined in Section 1.2. We primarily discuss the classical
approach of Pintz [24], for which Lichtman’s new Goldbach bounds are valid. We also outline
the more recent method of Elsholtz and Schlage-Puchta [3], which currently gives the best
result of d ≥ 0.10788.

4.1 Pintz’s method

In [24], Pintz gives a method for computing values of Romanov’s constant. The method
is very similar to the original approach of Romanov, with several optimisations added.
First, let r(n) := #{(p, a) : n = p + 2
a} (27)

denote the number of representations of n as the sum of a prime and a power of two. Noting
that r(n) is an unweighted version of r′
k(n) from the Linnik–Goldbach problem (see (13)),
we attain L
1 and L2 estimates for r(n) which are very similar to those given for r′(n) in
Lemmas 1 and 2. In particular, Pintz gives [24, Proposition 2]

S1(N ) := ∑

n≤N r(n) ∼ N
log 2

and for sufficiently large N [24, Lemma 3’]

S2(N ) := ∑

n≤N r(n)2 ≤ ̃CN,

where ̃C = 1
log 2
 ( C0(C1 + ε)R0
log 2 + 1)

13

with C0 as in (4), C1 as in Proposition 2, R0 as in (17), and ε > 0 arbitrary. From here, one
can readily compute a lower bound for d via Cauchy–Schwarz. In particular, one has

S1(N )2 ≤
 



 ∑

n≤N
r(n)>0
 1





 S2(N ),

so that ∑

n≤N
r(n)>0
 1 ≥ N
̃C(log 2)2 ,

and thus d > 1/ ̃C(log 2)
2. However, since r(n) only takes integer values, Pintz is able to
refine the use of Cauchy–Schwarz via the following lemma.

Lemma 3 ([24, Lemma 4’]). Suppose that b(n) ∈ N ∪ {0} for each n ≤ N . Assume that

N∑

n=1 b(n) = M and
 N∑

n=1 b(n)
2 ≤ DM.

Then,
 #{n ≤ N : b(n) > 0} ≥ ⌈D⌉ + ⌊D⌋ − D
⌈D⌉⌊D⌋ M.

So, setting M = N/ log 2 and D = ̃C log 2 in Lemma 3, along with Lichtman’s value of
C1 = 6.7814, we obtain d ≥ 0.10695,

which is just short of Elsholtz and Schlage-Puchta’s bound d ≥ 0.10788. In Table 2, we give
lower bounds for d assuming different values of C1. Notably, we see that if C1 ≤ 6.71, then an
improvement to Elsholtz and Schlage-Puchta’s bound is attainable via this relatively simple
method of Pintz. In addition, one attains d ≥ 0.17277 under assumption of the Elliott–
Halberstam conjecture (via Proposition 3).

4.2 Elsholtz and Schlage-Puchta’s method

In [3] Elsholtz and Schlage-Puchta use a novel idea to bound d, which takes advantage of
the fact that r(n) (defined in (27)) has an irregular distribution, depending on the residue
class of n modulo a fixed integer ℓ. For example, modulo 3, it is much more likely that
p + 2
ν ≡ 0 mod 3. This is because both primes and powers of two are uniformly distributed
on the residue classes 1 and 2 (mod 3). Extending on from this simple example, Elsholtz and
Schlage-Puchta work with the much larger modulus ℓ = 224 − 1 for their computations.

14

Table 2: Lower bounds for d via Pintz’s method for hypothetical values for C1.

C1 Lower bound for d Notes
8 0.09163 Classical value of C1 from Bombieri–Vinogradov.
7.8209 0.09362 Implied by the work of Wu [30].
6.7814 0.10695 Lichtman’s value of C1.
6.71 0.10799 Beats Elsholtz and Schlage-Puchta’s record.
4 0.17277 Follows from the Elliott–Halberstam conjecture.
2 0.31098 Conjectural value for C1.

With this setup in mind, Elsholtz and Schlage-Puchta rely on an upper bound for

R(N, h, k, ℓ) := #{p1, p2 ≤ N : p2 ≡ k (mod ℓ), p1 − p2 = h},

which generalises R(N, h) defined in (6). This allows them to obtain L
1 and L
2 estimates for
the representation function

r(n, k, ℓ) := #{(p, a) : n = p + 2a and n ≡ k (ℓ)},

in an analogous way to Pintz’s moment estimates for r(n) = r(n, 1, 1). Consequently, they
compute the local densities

d(k, ℓ) := lim inf
N →∞ #{n ≤ N : r(n, k, ℓ) > 0}
N/ℓ .

via Cauchy–Schwarz, or more precisely, the refinement of Cauchy–Schwarz in Lemma 3.
Finally, a lower bound for d is computed via the identity

d =
 ∑

0≤k<ℓ d(k, ℓ)
ℓ .

Due to the highly skewed distribution of d(k, ℓ) as k varies, this method yields a modest
improvement over Pintz’s simpler approach.
In analogy with our refinement of the Goldbach–Linnik problem, the key question here
is whether Elsholtz and Schlage-Puchta’s bound on R(N, h, k, ℓ) can be improved with
Lichtman’s new sieve bounds. In [3], the bound

sup
k∈Z
(k,ℓ)=1 R(N, h, k, ℓ) ≤ (8 + ε) C0N
φ(ℓ)(log N )2 ∏

p|ℓh
p>2
 p − 1
p − 2 (28)

is given for any fixed ℓ ≥ 1 and all h < N . The leading constant of 8 here is obtained by
the Bombieri–Vinogradov theorem, by a similar argument to the classical bound for R(N, h)
discussed in Section 2. Details of this classical argument can be found in [7, Theorem 3.12].

15

It seems possible then, that one could use Lichtman’s theory in [15] to reduce the constant
8 to 6.7814, in analogy with Proposition 2. However, this is unfortunately not possible. To
see this, we note that to bound R(N, h, k, ℓ) one sifts the set

A
′(k, ℓ) = {p + h : p ≤ N, (p, hℓ) = 1, p ≡ k (mod ℓ)},

and so is led to estimate

#A
′(k, ℓ)d := #{n ∈ A′(k, ℓ) : d | n} = π(N ; dℓ, a) + O(log ℓh),

where a depends on h, k, ℓ and d obtained via the Chinese remainder theorem from solving
the congruences p ≡ −h (mod d) and p ≡ k (mod ℓ). Note that by contrast, one had to
study the fixed residue class −h mod d when bounding R(N, h) in Section 2.2.
Now, as discussed in Section 2, Lichtman’s work then allows one to bound the sum

sup
0<|a|<x1+ε
 ∑

d≤xθ−ε λ(d)E(x; dℓ, a), (29)

with E(x; dℓ, a) = π(x; dℓ, a) − π(x)/φ(dℓ). However, since a depends on d in this setting
bounding a sum of the form (29) is not sufficient. In particular, one would require the
supremum over a to appear inside the sum rather than outside the sum as in (29).
We conclude by remarking that although Lichtman’s theory is not able to improve (28),
standard sieve weighting procedures depending on the Bombieri–Vinogradov theorem can
be applied to the problem of bounding R(N, h, k, ℓ). So, as also mentioned by Elsholtz and
Schlage-Puchta [3, p. 716], one could apply Wu’s complicated sieve weighting procedure
in [30] to improve the 8 in (28) to 7.8209. This would give
6 d ≥ 0.11011. However, if one
could overcome the uniformity issue appearing in Lichtman’s result and reduce the constant
in (28) to 6.7814, then a significantly better bound of d ≥ 0.12532 would follow from Elsholtz
and Schlage-Puchta’s method.

Acknowledgements

We are grateful to Alex Pascadi and Roger Heath-Brown for enjoyable discussions on
this topic, as well as the referee for some remarks that helped to improve our exposition.
DRJ is grateful to the Max Planck Institute for Mathematics in Bonn for its hospitality and
financial support.

6Elsholtz and Schlage-Puchta refrain from listing this result as a theorem, due to the technical nature of
Wu’s argument, making it preferable for someone to carefully go through the sieve weighting argument to
verify that it extends to this mod ℓ setting.
 16

References

[1] Bombieri, E. and Davenport, H. (1966). Small differences between prime numbers. Proc.
Roy. Soc. Ser. A, 293(1432):1–18.

[2] Chen, J. R. (1978). On the Goldbach’s problem and the sieve methods. Sci. Sinica,
21(6):701–739.

[3] Elsholtz, C. and Schlage-Puchta, J.-C. (2018). On Romanov’s constant. Math. Z., 288(3-
4):713–724.

[4] Friedlander, J. B. and Iwaniec, H. (2010). Opera de Cribro. American Mathematical
Society, Providence RI.

[5] Gallagher P. X. (1975). Primes and powers of 2. Invent. Math., 2:125–142.

[6] Greaves, G. (2013). Sieves in Number Theory. Springer-Verlag, Berlin Heidelberg.

[7] Halberstam, H. and Richert, H. (1974). Sieve Methods. Academic Press, London.

[8] Hardy, G. H. and Littlewood, J. E. (1923). Some problems of “partitio numerorum”, III:
On the expression of a number as a sum of primes. Acta Math., 44(1):1–70.

[9] Heath-Brown, D. R. (1979). The density of zeros of Dirichlet’s L-functions. Canadian J.
Math., 31(2):231–240.

[10] Heath-Brown, D. R. (2002). Lectures on sieves. Available at arXiv:0209360.

[11] Heath-Brown, D. R. and Puchta, J.-C. (2002). Integers represented as a sum of primes
and powers of two. Asian J. Math., 6(3):535–565.

[12] Iwaniec, H. (1980). A new form of the error term in the linear sieve. Acta Arith.,
37:307–320.

[13] Khalfalah, A. and Pintz, J. (2006). On the representation of Goldbach numbers by a
bounded number of powers of two. In Elementare und analytische Zahlentheorie, pages
129–142. Schr. Wiss. Ges. Johann Wolfgang Goethe Univ. Frankfurt am Main.

[14] Languasco, A. and Zaccagnini, A. (2010). On a Diophantine problem with two primes
and s powers of two. Acta Arith., 145:193–208.

[15] Lichtman, J. D. (2023). Primes in arithmetic progressions to large moduli, and Goldbach
beyond the square-root barrier. Preprint available at arXiv:2309.08522.

[16] Lichtman, J. D. (2025). A modification of the linear sieve, and the count of twin primes.
Algebra Number Theory, 19(1):1–38.

[17] Linnik, Y. V. (1953). Addition of prime numbers with powers of one and the same
number (in Russian). Mat. Sbornik N.S., 74(32):3–60.

17

[18] Liu, J., Liu, M., and Wang, T. (1998). The number of powers of 2 in a representation
of large even integers II. Sci. China Ser. A, 41(12):1255–1271.

[19] Maynard, J. (2025a). Primes in Arithmetic Progressions to Large Moduli I: Fixed
Residue Classes. Mem. Amer. Math. Soc., 306(1542).

[20] Maynard, J. (2025b). Primes in Arithmetic Progressions to Large Moduli II: Well-
Factorable Estimates. Mem. Amer. Math. Soc., 306(1543).

[21] Maynard, J. (2025c). Primes in Arithmetic Progressions to Large Moduli III: Uniform
Residue Classes. Mem. Amer. Math. Soc., 306(1544).

[22] Murty, M. R. and Sinha, K. (2023). An Introduction to the Circle Method. American
Mathematical Society, Providence RI.

[23] Pascadi, A. (2025). On the exponents of distribution of primes and smooth numbers.
Preprint available at arXiv:2505.00653.

[24] Pintz, J. (2006). A note on Romanov’s constant. Acta Math. Hungar., 112(1-2):1–14.

[25] Pintz, J. (2023). A new explicit formula in the additive theory of primes with
applications I. The explicit formula for the Goldbach problem and the Generalized Twin
Prime Problem. Acta Arith., 210:53–94.

[26] Pintz, J. and Ruzsa, I. Z. (2003). On Linnik’s approximation to Goldbach’s problem I.
Acta Arith., 109(2):169–194.

[27] Pintz, J. and Ruzsa, I. Z. (2020). On Linnik’s approximation to Goldbach’s problem II.
Acta Math. Hungar., 161(2):569–582.

[28] Platt, D. J. and Trudgian, T. S. (2015). Linnik’s approximation to Goldbach’s
conjecture, and other problems. J. Number Theory, 153:54–62.

[29] Romanoff, N. P. (1934). ¨Uber einige S¨atze der additiven Zahlentheorie. Math. Ann.,
109(1):668–678.

[30] Wu, J. (2004). Chen’s double sieve, Goldbach’s conjecture and the twin prime problem.
Acta Arith., 114(3):215–273.
 18
