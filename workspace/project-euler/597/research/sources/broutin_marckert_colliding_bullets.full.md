<!-- source: https://arxiv.org/pdf/1709.00789 | converted from PDF -->

The combinatorics of the colliding bullets

Nicolas Broutin∗† Jean-Fran¸cois Marckert
‡†

February 6, 2020

Abstract
The ﬁnite colliding bullets problem is the following simple problem: consider a gun, whose
barrel remains in a ﬁxed direction; let (Vi)1≤i≤n be an i.i.d. family of random variables with
uniform distribution on [0, 1]; shoot n bullets one after another at times 1, 2, . . . , n, where
the ith bullet has speed Vi. When two bullets collide, they both annihilate. We give the
distribution of the number of surviving bullets, and in some generalisation of this model.
While the distribution is relatively simple (and we found a number of bold claims online),
our proof is surprisingly intricate and mixes combinatorial and geometric arguments; we
argue that any rigorous argument must very likely be rather elaborate.

1 Introduction

1.1 Motivation and models of interest

The colliding bullets problem may be stated as follows: a gun whose position and direction
remains ﬁxed shoots bullets, one every second. The speeds of the bullets are random, indepen-
dent and uniform in [0, 1]. Upon collision, they both annihilate without aﬀecting the others
speeds. The main questions of interest concern the distribution of the number of surviving bul-
lets: if we ﬁre n bullets, what is the probability that k bullets escape to inﬁnity? What is the
probability if we ﬁre an inﬁnite number of bullets?

The aim of this note is to solve the ﬁnite case, as well as some generalizations deﬁned here:

Model 1 – Colliding bullets with random speeds and unit delays: n bullets are ﬁred at
times 1, 2, · · · , n; the respective speeds of the bullet are i.i.d. random variables v1, · · · , vn taken
under a distribution µ with support in [0, +∞) having no atom. Denote by

Pru
n := P
ru
n,µ = (P ru
n (k), 0 ≤ k ≤ n) (1)

the distribution of the number of surviving bullets. ▹

Model 2 – Colliding bullets with random speeds and random delays: n bullets are
ﬁred; the respective speeds of the bullets are i.i.d. random variables v1, · · · , vn with common
distribution µ with support in [0, +∞) having no atom. The ith bullet is shot at time Tj =
∑j−1
k=1 ∆k where (∆1, · · · , ∆n−1), the inter-bullet delays, are i.i.d. positive random variables (and
independent of the speeds) taken under a distribution ν having no atom at 0. Denote by

P
rr
n := P
rr
n,µ,ν = (P rr
n (k), 0 ≤ k ≤ n) (2)

the distribution of the number of surviving bullets. ▹

∗Sorbonne Universit´e, Sorbonne Paris Cit´e, CNRS, Laboratoire de Probabilit´es Statistique et Mod´elisation,
LPSM, F-75005 Paris, France. Email: nicolas.broutin@upmc.fr
†Both authors are very grateful to the NYU-ECNU Institute of Mathematical Sciences at NYU Shanghai where
most of this work has been done.
‡CNRS, LaBRI, Universit´e Bordeaux
 1arXiv:1709.00789v3  [math.CO]  5 Feb 2020
Model 3 – Colliding bullets with fixed speeds, and fixed delays: Choose a vector of n
distinct speeds V := (V1, · · · , Vn) ∈ [0, +∞)n and n−1 inter-bullet delays ∆ := (∆1, · · · , ∆n−1),
some positive numbers. Let σ and τ be independent uniform random permutations on Sn and
Sn−1, respectively. The ith bullet has speed Vσi and is shot at time T τ
i = ∆τ1 + · · · + ∆τi−1
(so that T τ
1 = 0, and the increments of the sequence (T τ
i , 1 ≤ i ≤ n) are the ∆τj ). Assume
moreover that for any (σ, τ ), [(Vσi, 1 ≤ i ≤ n) , (T τ
i , 1 ≤ i ≤ n)] is generic in the following sense:
if we consider that collisions have no eﬀect, there are no pairs (σ, τ ), no times, at which three
bullets, are exactly at the same place (see formal Deﬁnition 5). Denote by

P
ff
n = Pff
V,∆ := (P ff
V,∆(k), 0 ≤ k ≤ n) (3)

the distribution of the number of surviving bullets. ▹

The version of the problem in Model 3 makes an important link with combinatorics that will
be crucial to our approach (see the remark following Theorem 1 for details).

Model 4 – Colliding bullets with fixed acceleration functions, and fixed delays:
Fix a continuous increasing function f : R+ → R+ such that f (0) = 0. Choose an impe-
tus vector of n distinct elements I := (I1, · · · , In) ∈ [0, +∞)n and n − 1 inter-bullet delays
∆ := (∆1, · · · , ∆n−1), some positive numbers. Let σ and τ be independent uniform random
permutations on Sn and Sn−1, respectively. For the same convention as in the previous model,
the ith bullet is shot at time T τ
i = ∆τ1 + · · · + ∆τi−1. The speed of the bullet is not constant (in
general): the distance between bullet i and the origin at time t ≥ T τ
i is

Dt(i) = f (Iσi(t − T τ
i )).

Hence, when it exists, the speed at time t of the ith shot bullet is Iσif ′(Iσi(t − T τ
i )) so that
for f (x) = x we recover the preceding bullet problem (for V = I). For f (x) = x2 we have
accelerating bullets with “constant” acceleration 2I 2
σi, for f (x) = √x the asymptotic speed is
zero, for f (x) = 1 − exp(−x) the bullets slow down and converge in time +∞ to 1. Assume
again genericity in the sense explained in the previous problem. Denote by

Pfaf
n = Pfaf,f
I,∆ := (P faf
I,∆(k), 0 ≤ k ≤ n) (4)

the distribution of the number of surviving bullets. ▹

1.2 Main results and discussion

For every n ≥ 0, let qn be the probability distribution that is uniquely characterized by the
following recurrence relation and initial conditions:

q1(1) = 1, q1(0) = 0, q0(0) = 1, (5)

and for N ≥ 2, for any 0 ≤ k ≤ N ,

qN (k) = 1
N qN −1(k − 1) + (
1 − 1
N
 ) qN −2(k) (6)

with qn(−1) = qn(k) = 0 if k > n ≥ 0. In other words, qN is the distribution of XN , where
(Xn, n ≥ 0) is a simple Markov chain with memory 2 deﬁned by X0 = 0, X1 = 1 and for n ≥ 2,

Xn (d)
= B1/n(1 + Xn−1) + (1 − B1/n)Xn−2 (7)

where (B1/n, n ≥ 1) is a sequence of independent Bernoulli random variables with respective
parameters 1/n, n ≥ 1.

We are now ready to state our main result:
 2

Theorem 1. We have, for any n ≥ 0,

Pru
n = Prr
n = Pff
n = Pfaf
n = qn.

Remark. (a) Theorem 1 in particular states that the distribution of the number of surviving
bullets is independent of (V, ∆), provided that the colliding bullets problem is well-deﬁned (the
probability of a triple collision is zero). One could wonder if this is just the consequence of a
much stronger result that would say that the law of the set of surviving bullets is independent of
(V, ∆). Exhaustive enumeration all the conﬁgurations for examples with few bullets show that
the stronger statement is false.
(b) As we already mentioned, our analysis will principally rely on the study of “the permu-
tation model” Pff
n for which the pair speeds-delays (V, ∆) is ﬁxed, but uniformly and indepen-
dently permuted. When (V, ∆) is ﬁxed (and generic), the distribution Pff
V,∆ has a combinatorial
ﬂavour: the probability that k bullets survive is proportional to the number of permutations (σ, τ )
for which this property holds. However, since the distribution of the “identities” of the surviving
bullets is not the same in general for two diﬀerent pairs (V′, ∆′) and (V, ∆), the proof of The-
orem 1 cannot rely only on the speciﬁcs of the permutations (σ, τ ) and must take into account
the pair speeds-delays. Our key result is the proof that the map (V, ∆) ↦→ Pff
V,∆ is constant in
the set of generic elements.
When one reduces a speed, for example V1, the distribution of the set of conﬁgurations dra-
matically changes, and some avalanches of consequences arise (this has somehow the ﬂavour
of the jeu de taquin used in the Robinston–Schensted correspondence). For some choices of
(σ, τ ), when one replaces V1 by V ′
1 = V1 − ε, a bullet A which was surviving now collides with
another one, say bullet B; bullet B which used to collide with bullet C, is now destroyed by
bullet D, etc... The paper is principally devoted to the recursive control of these avalanches of
combinatorial modiﬁcations that comes from the reduction of a speed.

The simple form of the recurrence relation for qn also allows us to derive asymptotics for the
number of surviving particles as n tends to inﬁnity. The proof relies on a connection between
qn and cycles in random permutations that we present in Section 1.4, and we shall present the
proof at that point. In the following N (0, 1) denotes a centered Gaussian random variable with
unit variance.

Proposition 2. For Xn ∼ qn, we have the following convergence in distribution

Xn − 1
2 log(n)
√ 1
2 log(n)
 (d)
−−−→
n→∞ N (0, 1).

1.3 Discussion

Our aim was initially to attack the inﬁnite version, which has been attributed to David
Wilson. One quickly realizes that estimates for the probability that all the bullets shot from
some time interval vanish (and of related events) should be rather useful when trying to cook up
a Borel–Cantelli type argument. This led us to investigate the ﬁnite version. In [10], the readers
where asked to compute numerically the probability that 20 bullets all annihilate when the speeds
are uniform. Apparently motivated by this question, the ﬁnite version of the colliding bullets
problem arose in a number of online forums (see [8, 9], for instance). There, the distribution of
the number of surviving bullets is claimed to be qn, and a number of people discuss justiﬁcations.
However, we were unable to understand the arguments that are claimed to be proofs; this led
us develop our own solution (which in the end, seems to be the only rigorous one; see later).
Our proof of Theorem 1 is rather involved, despite the simplicity of the form of the distri-
butions qn. Together with the fact that qn also appears in a number of simpler models that we

3

present in Section 1.4, this may lead the reader to think that there should exist a much shorter
and eﬃcient proof. It is possible. Nevertheless, here are some facts that explain why some of
the intricate considerations we go through here should be present in any proof:

• Biased permutations in conditional spaces. First, consider Model ru. With probability
1/n the slowest bullet is ﬁred last and, similarly, also with probability 1/n the fastest
is ﬁred the ﬁrst. If one or both of these events occur then the corresponding bullet(s)
survive(s). Furthermore, the delays between the remaining bullets are unchanged and all
equal to 1. So by exchangeability, the problem reduces to a problem of the same type,
and with smaller size. However, if none of these events occur, any decomposition appears
to be much more involved: for example, if it is ﬁred after i − 1 others, for some i < n,
the slowest bullet may survive or not. When one searches to condition on the survival
or destruction of the slowest bullet (or of any other bullet), one quickly realises that the
permutation of speeds of the remaining bullets is biased. In the case of eventual survival,
the bullets shot after it must collide pairwise, and their space-time diagram must not cross
that of the slowest bullet. This creates a bias that looks diﬃcult to handle.

• Non constant delays. Even worse, in the case of eventual collision, even if for some reason,
(a) the distribution of the speed that collides with it was known, and (b) no other collision
occurs ﬁrst, then after the collision, the delays between the bullets are no more constant;
even if we rewind time back to zero, one of the delays is now 3.

• Random delays? The previous considerations lead us to study Model rr, since in any
decomposition, the removal of any bullets, will make the delay between the bullets be-
come non constant. However, one also quickly realizes that the distribution of the delay
between shots has all the chances to be modiﬁed by the removal of two bullets; and the
exchangeability might be ruined.

• Fixed distinct delays must be permuted. Overall, one is led to consider a sequence of
arbitrary delays between the shots. But some computer experiments show that if we replace
the unit inter delays 1, · · · , 1 by some deterministic positive and distinct real numbers
δ1, · · · , δk−1, then the distribution of the number of surviving bullets when the bullet speeds
are uniformly permuted is not constant and depends on the vector (δi, 1 ≤ i ≤ k−1). What
appears to be true however (and this is veriﬁed by our analysis), is that if one permutes
both the bullet speeds and the delays, independently, then the distribution of the surviving
bullets appears to be the same and given again by qn. Hence, Model ff does not appear
only as a generalization of Model ru, but indeed, as a tool to analyze it.

Therefore, when studying the quenched Model ff, one of the important points is to guarantee
that at every level of the induction, the permutations of both the speeds and of the delays are
equally likely and independent, which takes us back to the ﬁrst point.
When discussing our ﬁndings with colleagues, we heard from Vladas Sidoravicius that Fedja
Nazarov had an unpublished proof of the fact that, for every n ≥ 1, one has q2n(0) = ∏n
i=1(1− 1
2i );
this is also stated in [4], but the proof is not reproduced there. So, to the best of our knowledge,
our proof of Theorem 1 is the ﬁrst rigorous treatment of the distribution of the number of
surviving bullets in the ﬁnite bullets colliding problem.

1.4 Simpler natural models following the same distribution

We present here three other models in which the probability distributions qn, n ≥ 1, play
a special role. We have found the ﬁrst two discussed in a forum about the bullet problem, but
we could not ﬁnd anything that could be considered remotely close to a proof that the colliding

4

bullets problem is indeed equivalent to these models: it seems that some of the users have noticed
that the distribution is the same, by a mixture of simulations, exhaustive enumeration, but also
what seems to be wrong proofs from the level of details that were provided. In any case, from
what we could see, it seems that none of the pitfalls that we have mentioned at the end of the
previous section has been dealt with correctly ([8],[9]).

Model 5 – Sorted bullet flock. Let µ be a probability distribution on (−∞, +∞) without
atoms; n bullets with i.i.d. speeds v1, · · · , vn with common distribution µ are ﬁred at times
1, · · · , n. At time 0, the set of living bullet is L0 = ∅. The ith bullet is ﬁred at time i and:

• if vi ≤ min(Li−1) then Li := Li−1 ∪ {vi};

• if vi > min(Li−1), Li = Li−1 \ {min(Li−1)}.

In other words, if bullet i is faster than one of the surviving bullets, it collides instantaneously
with the slowest, and both of them disappear. Otherwise bullet i is the slowest, and it is added
to the list of surviving bullets. Denote by P(5)
n the distribution of the number of bullets in the
ﬂock at time n. ▹

Model 6 – Odd cycles in random permutations. Let s be a permutation chosen uniformly
at random in the symmetric group on {1, · · · , n}, and let Zn be the number of cycles with odd
length in the cycle representation of s. Denote by P(6)
n the distribution of Zn. ▹

Finally, we introduce the following that ensures a monotone coupling of the marginals at
diﬀerent values of n (it is used in Proposition 4):

Model 7 – Two-step directed tree on N. Let (Bn, n ≥ 1) be a sequence of independent
Bernoulli random variables with parameters 1/n. For each n ≥ 1, if Bn = 1 add the red directed
edge (n, n − 1), and if Bn = 0, add the black directed edge (n, n − 2). Then, for each node of N,
there is a unique directed edge out, and as a consequence a unique directed path to the node 0,
which is the unique sink of the inﬁnite digraph. For n ≥ 1, let P(7)
n be the distribution of the
number of red edges on the unique path between n and 0. ▹

All three models above also follow the exact same distribution qn deﬁned on page 2:

Theorem 3. For any ℓ ∈ {5, 6, 7}, any n ≥ 0

P(ℓ)
n = qn.

The proofs of the three diﬀerent cases of Theorem 3 are all straightforward, and presented
in Section 5. This contrasts with all bullet-related models of Section 1.1 for which the proof is
fairly intricate.

1.5 Remarks about the case with inﬁnitely many bullets

Let µ be a probability distribution on [0, ∞). Let (Vi, i ≥ 0) be a sequence of i.i.d. speeds
with common distribution µ, and consider the corresponding colliding problem with inﬁnitely
many bullets: for each integer i ≥ 0 a bullet is ﬁred at time i, that has speed Vi. Let S∞ denote
the set of indices of the bullets that survive forever (provided it is well-deﬁned, see later on).
Consider now the sequence of colliding problems where only the ﬁrst n bullets are shot, with
speeds V1, V2, . . . , Vn; let Sn denote the collection of indices of the surviving bullets.
Theorem 1 implies that, as n → ∞, the number of surviving bullets |Sn| → ∞ in probability,
whatever the common distribution µ of the speeds, provided that it has no atom.
Of course, without any additional element, this does not rule out the possibility that |Sn|
may vanish inﬁnitely often. In other words, unsurprisingly, the knowledge of the marginal

5

Figure 1: A simulation of evolution of the number of surviving bullets (|Sj|, 1 ≤ j ≤ n) for n = 50000.

distributions (qn)n≥1 alone does not allow to conclude about the eventual survival of some
bullet.
Actually, among the models we have presented in Section 1.4, which all have qn as marginals,
some vanish inﬁnitely often, while others tend to inﬁnity almost surely:

Proposition 4. Let (Fn)n≥1 denote the sequence of sizes in the bullets ﬂock model, and let
(Dn)n≥1 denote the sequence of red distances to 0 in the two-step tree model. Then, with proba-
bility one,
(i) Fn = 0 inﬁnitely often, and
(ii) Dn → ∞; in particular, Dn = 0 only ﬁnitely often.

We do not know what happens for the original colliding bullets problem, but at the very
least, the sequence (|Sn|)n≥0 exhibits ﬂuctuations that are quite complex. In particular, the fact
that |Sn| = 0 does not imply that no bullet from the set {1, 2, . . . , n} survives forever! Indeed,
when bullet n + 1 is shot, there are three possibilities: it may

• be slow enough to avoid all the trajectories of the bullets in {1, 2, . . . , n}, in which case
there is one additional surviving bullet,

• hit one of the surviving bullets, which would cause the set of surviving bullets to lose one
of its elements,

• hit some bullet i ∈ {1, . . . , n} that, if not hit, would collide with one of the bullets in
{1, . . . , i − 1}, say bullet j; the ﬁrst eﬀect is to release bullet j, which may inductively give
rise to the same three possibilities.

This shows that, for any n ≥ 0, we have |Sn+1| − |Sn| ∈ {+1, −1}, but also that the ﬂuctuations
of the sequence (|Sn|)n≥0 are quite complex (see Figure 1 for a simulation), and that the set
Sn can dramatically change from one step to another. Even showing that if |Sn| = 0 inﬁnitely
often then every bullet is eventually destroyed does not seem straightforward. We will leave the
question hanging, since we are concerned here with the combinatorics case with only ﬁnitely
many bullets.
Let us just observe that when an inﬁnite number of bullets are shot, the events

{ bullet i survives } and { ∃ i, bullet i survives }

6

are measurable. Indeed, a bullet does not survive forever if it is hit before time m for some
m ∈ N; on the other hand, since the speeds are non-negative, the fact that bullet i ≤ m is hit
before time m only depends on the bullets shot before time m (see also Section 2.3).
Finally, let us mention that Dygert, Junge, Kinzel, Raymond, Slivken, and Zhu [4] have
recently proved that in the case where the law of the speeds has support a ﬁnite set in (0, ∞),
(1) if the ﬁrst bullet has the second fastest speed then it survives with positive probability (the
fastest speed would be obvious), and (2) if it has the slowest speed then it is eventually destroyed
with probability one. Sidoravicius and Tournier [14] also have related results. These two papers
also contain interesting discussions of the relevant connections with in probability and physics
literature. To the best of our knowledge, the results in [4] and [14] are the only non-trivial results
on the inﬁnite model that have been proved rigorously.

Remark. Let us mention that the colliding bullet problem has already appeared in the physics
literature under the name “ballistic annihilation”. There compared to the present model, the
roles of times and space are exchanged: one sees the bullets as the particles in some gas model;
the particles move with constant (random) speeds, initially from diﬀerent points in space, and
the main question is to infer the evolution in the density of particles as times evolves. For more
details, see for instance [1–3, 5, 6, 11–13, 15, 16].

1.6 Structure of the proof and plan of the paper

A moment thought suﬃces to see that among Models 1–3 of Section 1.1, Model 3 with the
ﬁxed parameter (V, ∆) is the most general; the two others are just annealed versions and the
corresponding distributions are obtained by integration. Model 4, with the ﬁxed acceleration
function, is actually more general but it may be reduced to Model 3 via coupling and a simple
transformation (see Proposition 14 for details). So from now on, we focus on Pff
V,∆.
Again, the naive induction – the one relying on the elimination of the slowest or fastest
bullet – fails in general as we have pointed out it Section 1.3 because one cannot guarantee
that a speciﬁc bullet collides. There is however a situation in which one can identify a bullet
that must either collide or survive: it is when the minimal speed is zero; indeed, in this case,
the bullet with minimal speed remains in the barrel so it does survive if it is shot last, and
does collide with the next one otherwise. As a consequence, if the minimal speed is null, then
there is a simple one-step reduction to cases with one or two bullets less. Unfortunately, this
trick only works once (at most one speed is zero). But one may try to show that lowering the
minimal speed does not alter the distribution of the number of surviving bullets, then one could
iteratively bring the minimal speed to zero and thus write down a complete recurrence relation.
We will show that one can indeed alter the parameter (V, ∆) without changing the distri-
bution of the number of surviving bullets; this will a posteriori justify writing Pff
n in place of
Pff
V,∆. Granted the independence of Pff
V,∆ from (V, ∆), it is fairly easy to rigorously devise a
recurrence relation for the distribution Pff
n and identify it as qn, thereby proving Theorem 1.
We carry on the details in Section 3.1.
The heart of the argument then consists in justifying the independence of Pff
V,∆ with respect
to (V, ∆). For many values of the parameter (V, ∆) that we call generic, one can indeed
slightly lower the minimal speed without aﬀecting the distribution of the number of surviving
bullets, for the simple reason that none of the conﬁgurations are aﬀected; this is formalized in
Lemma 8 and relies on a simple topological property. In general however, it is not possible
to take the minimal speed to zero without altering any of the conﬁgurations. While lowering
the minimal speed, one may encounter certain non-generic or singular values of the parameter
(V, ∆) for which there exist collisions involving more than two bullets. For such a value of
the parameter the colliding bullets problem is not well-deﬁned if we consider that bullets only
annihilate pairwise. These are values of the parameter at which (at least for some conﬁgurations)

7

the pairs of annihilating bullets are modiﬁed. Still, in some small neighborhoods of (V, ∆), the
distribution Pff
V,∆ is well-deﬁned and remains constant1; because there is no clear one-to-one
correspondence between the conﬁgurations of these neighborhoods, this invariance necessarily
involves a priori intricate averaging.
The whole argument then reduces to showing that the distribution Pff
V,∆ remains constant
when “crossing” the non-generic values of the parameter; this is the corner stone of the argument.
In order to prove this, we ﬁrst show that it is “essentially” suﬃcient to consider what happens at
the values of the parameter that involve at most triple collisions; these singular values are called
simple; the formal deﬁnition (Deﬁnition 10) is slightly more restrictive, but this is the idea, and
we do not want to blur the big picture at this point. This amounts to showing that it is possible
to slightly alter the parameter, without changing the distribution of surviving bullets, in such
a way that only simple singular points are encountered when eventually reducing the minimal
speed to zero (Lemma 12). In order to treat the eﬀect of “crossing” a simple singular value of
the parameter, we proceed by introducing two new combinatorial colliding bullets models with
general constraints and by comparing them through an induction argument in Section 4.
Turning the sketch we have just presented into a rigorous proof requires to set up a number
of geometric representations and formal deﬁnitions; these preliminary results are presented in
Section 2.

2 Notation, preliminaries and geometric considerations

2.1 The virtual space-time diagram

In this section, we ignore the eﬀects of collisions and consider trajectories and events that
are only virtual. From now on, for i ≥ 1, we denote by “bullet i”, the ith shot bullet, and we
assume that the n bullets are shot at some times t1 < · · · < tn with respective non-negative
speeds v1, · · · , vn. If it is in the air at time t ∈ R, bullet i lies at a distance to the starting point
x = 0 that is given by Yi(t) = vi(t − ti).

So, ignoring the collisions, each bullet has a virtual trajectory; for bullet i, it is given by the
half-line HL (vi, ti) := {(t, Yi(t)), t ≥ ti}. (8)

Two bullets i ̸= j may only collide at time (which may be positive or negative)

T (i, j) = viti − vjtj
vi − vj , (9)

the time at which the lines L (vi, ti) and L (vj, tj) supporting respectively HL (vi, ti) and HL (vj, tj)
intersect. We deﬁne the virtual collision time between bullet i and bullet j by

CT(i, j) = { T (i, j) if T (i, j) ≥ max{ti, tj},
+∞ if T (i, j) < max{ti, tj}. (10)

Even if we ask T (i, j) to be larger than max{ti, tj} to ensure that both i and j have been shot,
CT(i, j) is still virtual : indeed, (10) still ignores the remaining bullets. Even if T (i, j) < ∞
there is no guarantee that bullets i and j ever hit each other for one or both may have been
destroyed before time T (i, j). The collection of line segments {HL(vi, ti)}1≤i≤n is called the
virtual space-time diagram of the collision process (See Figure 2).

1To be precise: the set of generic points restricted to the neighborhood of a singular point is not connected,
but Pff
V,∆ is constant on every connected component, and the values all agree.

8

t1 t2 t3 t4 t5 t6 t7t1 t2 t3 t4 t5 t6 t7

Figure 2: On the left, some instance of a virtual space-time diagram for seven bullets; on the right,
the corresponding space-time diagram in solid lines (the virtual space-time diagram is still shown in light
dashed lines). The red disks represent the collisions; the collision times are then the ﬁrst coordinates of
the red disks. The 5th bullet survives.

2.2 Unambiguous colliding problems and generic parameters

For n ≥ 1, let Θn ⊂ Rn
+ × Rn−1
+ be the set of couples (Vn, ∆n−1) where Vn = (V1, . . . , Vn)
and ∆n−1 = (∆1, . . . , ∆n−1) for which 0 ≤ V1 < V2 < · · · < Vn and 0 < ∆1 ≤ ∆2 ≤ · · · ≤ ∆n−1.
The set Θn will be referred to as the parameter space and its elements (V, ∆) as parameters.
A pair (σ, τ ) ∈ Sn × Sn−1 of permutations of the speeds and inter-bullet delays is called a
conﬁguration. Fix a conﬁguration (σ, τ ). Consider
{ T τ
j = ∆τ1 + · · · + ∆τj−1, for 1 ≤ j ≤ n,
V σ
j = Vσj , for 1 ≤ j ≤ n.

and, for t ≥ T τ
j ,
 Yσ,τ
j (t) = V σ
j (t − T τ
j ) (11)

the virtual position of bullet j at any time t ≥ T τ
j . Let CT
σ,τ (i, j) be the virtual collision time
of bullets i and j in conﬁguration (σ, τ ); if CT
σ,τ (i, j) < ∞ then denote by

M V,∆
σ,τ (i, j) := HL (V σ
i , T τ
i ) ∩ HL (V σ
j , T τ
j ) (12)

the corresponding virtual collision point (in space-time) of bullets i and j in the conﬁguration
(σ, τ ); if CT
σ,τ (i, j) = ∞ then the half-lines do not intersect and we set M V,∆
σ,τ (i, j) = ∅. Here,
all the quantities are still virtual, since they are deﬁned independently from the action of the
other bullets.

Deﬁnition 5 (Generic parameter). We say that the parameter (V, ∆) ∈ Θn is generic if for
each ﬁxed conﬁguration (σ, τ ) ∈ Sn × Sn−1, and for any 1 ≤ i < j < k ≤ n, we have

HL (V σ
i , T τ
i ) ∩ HL (V σ
j , T τ
j ) ∩ HL (V σ
k , T τ
k ) = ∅. (13)

Let Gn denote the subset of Θn consisting of all generic parameters.

A parameter is generic if for every conﬁguration no three virtual trajectories ever intersect
at the same point. Note that being generic requires more than “no three bullets meet simul-
taneously at the same place”, since the constraints hold on virtual trajectories. The fact that
(V, ∆) is generic is a suﬃcient condition for the probability distribution Pff
V,∆ to be deﬁned
unambiguously.
 9

2.3 The set of surviving bullets and the space-time diagram

Fix (V, ∆) = (Vn, ∆n−1) ∈ Gn and a conﬁguration (σ, τ ). Then the collection of indices of
the bullets that indeed survive is determined by the following simple algorithm. For the sake of
readability, we now drop the references to (V, ∆) and (σ, τ ) and suppose that the bullets are
shot at times t1 < t2 < · · · < tn and have speeds v1, v2, . . . , vn.
For each time t ≥ 0, the algorithm computes the set St ⊂ {1, 2, . . . , n} of bullets that either
have not yet been shot, or that are still in the air at time t. Initially, we have S0 = {1, 2, . . . , n}.
Suppose that we have computed St for t ≤ T . If there is a collision between the bullets in ST at
some time t > T , then a collision occurs at time

T + = min{CT(i, j) : i, j ∈ ST }.

Depending on T +, proceed as follows:

• if T + = ∞ there is no collision after time T and therefore St = ST for all t ≥ T ;

• if T + < ∞, then T + = CT(i1, j1) > T for some pair (i1, j1) of elements of ST ; this pair
is not necessarily unique, but since the parameter is generic, every bullet is involved in at
most one colliding pair. Writing (iℓ, jℓ), 1 ≤ ℓ ≤ p for the pairs for which CT(iℓ, jℓ) = T +,
one then has ST + = ST \ {iℓ, jℓ : 1 ≤ ℓ ≤ p} and St = ST for all t ∈ [T, T +).

One can thus compute St for all t ≥ 0. Since St is eventually constant, the set of surviving bullets
is then S = limt→∞ St. The procedure actually computes the time of death ∂i of each bullet
i ∈ [n]. Instead of the completed half-line HL(vi, ti) one can then consider its true trajectory
HL(vi, ti) which is the line segment

HL(vi, ti) = {(t, Yi(t)) : t ∈ [ti, ∂i]}. (14)

The collection of trajectories {HL(vi, ti)}1≤i≤n is called the space-time diagram. See the simula-
tions in Fig. 3.

Remark. When it is clear from the context which speeds and shooting times we are talking
about, we sometimes refer to HL(vi, ti) and HL(vi, ti) as HLi and HLi.

2.4 The topological collision scheme

Fix (V, ∆) ∈ Gn, so that for any conﬁguration (σ, τ ) ∈ Sn ×Sn−1, the half-lines HL(V σ
i , T τ
i ),
1 ≤ i ≤ n, only intersect pairwise. Recall the deﬁnition of M V,∆
σ,τ (i, j) in (12) and recall that
L (V σ
k , T τ
k ) denotes the line which contains HL(V σ
k , T τ
k ).
Each line L(V σ
k , T τ
k ) splits R2 into two open half-spaces; since V σ
k ∈ [0, ∞), there is a natural
labelling each one of these half-spaces as above and below, depending on whether it contains
every point (0, y) or (0, −y) for all large enough y, respectively. Furthermore, since lines only
intersect pairwise, for any triple of distinct integers (i, j, k), the point M V,∆
σ,τ (i, j), when it exists,
lies either above or below the line L(V σ
k , T τ
k ).
In the following, we write

[ n
3
 ]• = { {(i, j, k) ∈ {1, · · · , n}3, i < j, j ̸= k, i ̸= k} if n ≥ 3
{(1, 2, ∗)} if n = 2 .

Deﬁnition 6 (Topological colliding scheme). Let (V, ∆) ∈ Gn. The topological colliding scheme
(TCS, for short) of (V, ∆) is the function ΓV,∆ deﬁned as follows.

10

Figure 3: Simulations of the space-time diagram in the colliding bullets problem with n bullets, shot
with unit delays, with independent uniform random speeds on [0, 1]. On the left-hand side picture n = 50,
on the right-hand side n = 5000.

(i) If n ≥ 3, then

ΓV,∆ : Sn × Sn−1 × [ n
3 ]• −→ {−1, 0, +1}n!×(n−1)!×(n
3)

(σ, τ, i, j, k) ↦−→
 



 0 if M V,∆
σ,τ (i, j) = ∅
+1 if M V,∆
σ,τ (i, j) is above L (V σ
k , T τ
k )
−1 if M V,∆
σ,τ (i, j) is below L (V σ
k , T τ
k ) ,
 (15)

(ii) If n = 2, then
 ΓV,∆(σ, τ, 1, 2, ∗) = { 0 if M V,∆
σ,τ (1, 2) = ∅
1 otherwise.

The topological colliding scheme is very similar to order types in geometry. Its importance
relies in the (obvious?) fact that for every conﬁguration, it determines indices of the surviving
bullets. This is straightforward from the following lemma.

Lemma 7. Let (V, ∆) ∈ Gn. For any (σ, τ ) ∈ Sn × Sn−1, the set S(Vσ, ∆τ ) of indices of the
surviving bullets in the conﬁguration (σ, τ ) is fully determined by the map ΓV,∆(σ, τ, ·, ·, ·).

Proof. We proceed by induction on the number of bullets n. If n ∈ {0, 1}, then there is
nothing to prove; if n = 2, for every permutations σ and τ , the point M V,∆
σ,τ (i, j) exists pre-
cisely if ΓV,∆(σ, τ, i, j, k) = 1, and hence the information is contained in the restricted map
ΓV,∆(σ, τ, ·, ·, ·) whether the two bullets do collide or not (∆ has no inﬂuence).
Suppose now that the property holds for up to n − 1 bullets, and any generic pair (V, ∆).
Fix a pair of permutations (σ, τ ) ∈ Sn × Sn−1. Observe ﬁrst that considering a subset of the
trajectories HLi, i ∈ [n], does correspond to looking at some TCS for a speed vector consisting
of the speeds of the selected bullets, and a delay vector containing aggregate delays; if (V, ∆)
is generic, so are any of the vectors obtained by taking subsets of the bullet trajectories. There
are two possibilities:

• if ΓV,∆(σ, τ, 1, ·, ·) = 0 then HL1 does not intersect any of other HLi. In this case 1 ∈ SVσ,∆τ
and the remaining surviving bullets are determined by the map induced by ΓV,∆(σ, τ, ·, ·, ·)
on the set [ B
3 ]• where B = {2, . . . , n}.
 11

• otherwise, there exists some j such that ΓV,∆(σ, τ, 1, j, ·) is not identically zero. Then, let
J ∈ {2, 3, . . . , n} be minimal such that ΓV,∆(σ, τ, 1, J, k) = 1, for all k ̸∈ {1, J} (so that
M V,∆
σ,τ (1, J) lies above all lines Li, i ∈ {2, . . . , n} \ {J}). By induction, we can determine
whether bullet J survives when removing bullets with indices in the set {1, J + 1, J +
2, . . . , n} by looking at the map ΓV,∆(σ, τ, ·, ·, ·) on the set [ B
3 ]• where now B = {2, . . . , J}.
With this information in hand:

– If bullet J does survive in this smaller colliding scheme, then bullets 1 and J do
collide in the original scheme. Additionally, bullets 2, 3, . . . , J − 1 all annihilate and
none of the trajectories genuinely crosses HLJ . Another induction yields the indices
of the surviving bullets lying in {J + 1, . . . , n} by looking at ΓV,∆(σ, τ, ·, ·, ·) on the
set [ B
3 ]• with B = {J + 1, . . . , n}.

– If bullet J does not survive, it collides with another one (whose index is given by the
induction); removing both, we can again use induction to determine the remaining
surviving bullets.

It follows that the set of indices of the surviving bullets S(Vσ, ∆
τ ) is a function of the map
ΓV,∆(σ, τ, ·, ·, ·).

The following simple observation will also be useful:

Lemma 8. The map Γ : (V, ∆) ↦→ ΓV,∆ is locally constant in Gn: for (V, ∆) ∈ Gn, there exists
an open neighborhood O of (V, ∆) in Rn × Rn−1 such that O ⊂ Gn, and

ΓV,∆ = ΓV′,∆′ for all (V′, ∆′) ∈ O. (16)

2.5 Singular parameters and critical patterns

A parameter (Vn, ∆n−1) in Θn \ Gn is called singular. The parameter (Vn, ∆n−1) is singular
if and only it contains a critical pattern, or critical bi-triangle in the following sense:

Deﬁnition 9 (Critical pattern). A critical pattern or critical bi-triangle with respect to some
parameter (V, ∆) is a tuple (vm, vℓ, vr, dℓ, dr) such that
(a) vm, vℓ and vr are three distinct speeds from V,
(b) dℓ and dr are the sums of components of ∆ over two disjoint sets of indices, and
(c) the three half-lines HL(vm, 0), HL(vℓ, dℓ), and HL(vr, dℓ + dr) are concurrent (see Figure 4).

Given (V, ∆), a conﬁguration (σ, τ ) is said to contain the critical pattern π = (vm, vl, vr, dl, dr)
if there exists (i, j, k) such that V σ
i = vm, V σ
j = vℓ, V σ
k = vr and furthermore





 T τ
j − T τ
i =
 j−1∑

p=i ∆τ
p = dℓ

T τ
k − T τ
j =
 k−1∑

p=j ∆τ
p = dr;

we let Cπ = Cπ(V, ∆) denote the set of conﬁgurations that contain π. For a given conﬁguration
(σ, τ ) ∈ Cπ containing a given critical pattern π = (vm, vℓ, vr, dℓ, dr), let ρπ ≥ 0 be such that
the common intersection point of HL(vm, 0), HL(vℓ, dℓ), and HL(vr, dℓ + dr) has coordinates
(t, ρπ), for some t ≥ 02. The pattern is called realized by (σ, τ ) if it is also contained in the

2So ρπ is the (spatial) distance from the origin at which the lines intersect; this is independent of the potential
time shift that the pattern may have in speciﬁc conﬁguration.

12

diagram involving the actual trajectories HL(V σ
i , T τ
i ); this means that for p ∈ {i, j, k}, the actual
trajectory HL(V σ
p , T τ
p ) contains the line segment HL(V σ
p , T τ
p ) ∩ [0, ∞) × [0, ρπ) (meaning that the
portions of the half-lines before the triple collision point are not intersected, see Figure 4); we let
Rπ = Rπ(V, ∆) be the set of conﬁgurations for which π is realized. Finally, we say that a critical
pattern π = (vm, vℓ, vr, dℓ, dr) is minimal if both dℓ and dr correspond to a single component of
∆ (meaning that the three bullets with speed vm, vr and vℓ are shot consecutively).
While a given speed v may be involved in multiple critical patterns, there may not be a single
conﬁguration that contains multiple critical patterns. For this reason, it is useful to keep track
of which conﬁgurations contain a given critical pattern: a pattern is called (σ, τ )-critical if it is
critical for (σ, τ ).

Deﬁnition 10 (Simple singular parameter). A singular parameter (Vn, ∆n−1) is called simple,
if for every conﬁguration (σ, τ ), every speed v of Vn is involved in at most one (σ, τ )-critical
pattern. In other words, for each (σ, τ ), each line HL(V σ
m, T τ
m) participates in at most one critical
bi-triangle; in particular, the collisions involve at most three bullets.

For a speed vector Vn = (V1, V2, . . . , Vn) ∈ Rn
+, let V↓
n be the vector (0, V2, . . . , Vn) where
the minimal speed has been put to zero.

Deﬁnition 11 (Essentially generic). A parameter (Vn, ∆n−1) ∈ Gn is called essentially generic
if, for any convex combination V′
n of Vn and V↓
n, that is V′
n = (λV1, V2, . . . , Vn) for some some
λ ∈ [0, 1], the parameter (V′
n, ∆n−1) is either generic or simple singular.

When (V, ∆) is essentially generic, every critical pattern with respect to a convex com-
bination (V′, ∆) of (V, ∆) and (V↓, ∆) must involve the minimal speed: it must be of the
form (min V′, vℓ, vr, dℓ, dr). The following crucial “density lemma” allows us to focus only on
essentially generic parameters:

Lemma 12. For any (V, ∆) ∈ Gn, there exists an essentially generic parameter (V′, ∆′) ∈ Gn
such that the TCS of (V, ∆) and (V′, ∆
′) are identical, i.e., ΓV,∆ = ΓV′,∆′.

Our proof of Lemma 12 is probabilistic; for the readers who might be averse to such an
existential proof, we mention that one could alternatively give an explicit and deterministic
construction of the parameter (V′, ∆′).

Proof. By Lemma 8, there exists a full-dimensional compact set J × K ⊂ Rn
+ × Rn−1
+ around
(V, ∆) in which the TCS is constant; in particular, J × K is included in Gn. We may, and will
from now on, assume that J is a rectangular box.
Furthermore, this implies that for any such point (V◦, ∆◦), lowering the minimal speed can
create at most triple-intersections in the virtual space-time diagram. In order to complete the
proof, it suﬃces to prove that there exists some point in J for which no two such triple collision
points are ever aligned with the point in space-time at which the bullet with the minimal speed
is shot, call it O = O(σ, τ ).
To do this, we show that if V′ denotes a point chosen proportionally to Lebesgue measure
on J, then (V′, ∆) has the desired property with probability one. To see this, ﬁx any (σ, τ ) and
consider the half-lines corresponding to the bullets with speeds V ′
2, V ′
3, . . . , V ′
n in this order. Note
that the speeds V ′
i , 2 ≤ i ≤ n are all uniform in some small interval. For any i ∈ {2, . . . , n − 1},
given the speeds V ′
2, . . . , V ′
i there are only a ﬁnite number of intersection points among the
corresponding lines. The rays originating from O intersect the half-lines HL(V σ
ℓ , T τ
ℓ ), 2 ≤ σℓ ≤ i
at ﬁnitely many points, therefore, the line HL(V σ
k , T τ
k ) with σ(k) = i + 1 contains none of these
with probability one. As a consequence, almost surely, no two intersections are aligned with
O = O(σ, τ ). Since the number of conﬁgurations is ﬁnite, this completes the proof.

13

dℓ dr dℓ dr dℓ dr

vm

vℓ vr

vm

vℓ vr
 vm

vℓ vr
Figure 4: In red a critical pattern or critical bi-triangle (vm, vℓ, vr, dℓ, dr) in diﬀerent conﬁgurations.
On the left, the critical pattern is realized: it is not intersected by any other trajectories. In the middle,
the critical pattern is not realized, for one of the three bullets is intersected before reaching the point of
the triple collision. On the right, the critical bi-triangle is realized, but not minimal.

3 Invariance with respect to generic parameters

3.1 Statement of the invariance and consequences

As we already mentioned earlier, our approach consists in an induction argument. In order
to better put the ﬁnger on what precisely is needed for the induction hypothesis, we state a
ﬁxed-n version of the invariance principle that is one of the keys to the induction step. Note
that the key assumption to guarantee that the law of the number of surviving bullets be qn
deﬁned in (5–6) is the “invariance principle” in (17).

Lemma 13. Let n ≥ 2. Suppose that, the following two conditions hold:
(i) for every m < n, for every (Vm, ∆m−1) ∈ Gm, we have

Pff
Vm,∆m−1 = qm ,

(ii) for every essentially generic parameter (Vn, ∆n−1) in Gn, we have

P
ff
Vn,∆n−1 = P
ff
V↓
n,∆n−1 . (17)

Then, for every (Vn, ∆n−1) ∈ Gn, we have

Pff
Vn,∆n−1 = qn .

Proof. By Lemma 12, it suﬃces to prove the claim for all essentially generic parameters. Suppose
that (i) and (ii) hold, and let (Vn, ∆n−1) ∈ Gn be essentially generic, so that (17) holds. We
look for a decomposition for the colliding bullet problem with (V↓
n, ∆n−1), when min V↓
n = 0.
Since σ is uniform in Sn, the element a such that σa = 1 is uniform in {1, · · · , n}; and the speed
of bullet a is then 0. It happens that:

(1) With probability 1
n , a = n. The last bullet has then speed 0 and all the others have a
positive speed, so the last bullet survives. On that event, the permutation σ′ of the n − 1
ﬁrst speeds is uniform on Sn−1 and the last delay ∆τ
n is uniform among all the delays (and
is independent from σ′). Thus, the number of bullets from this groups of n − 1 that survive
is distributed as a convex combination of the Pff
V−,∆−, where V− = (V2, V3, . . . , Vn) and

∆− ∈ Rn−2
+ is obtained from ∆n−1 by removing a uniform component. Clearly, any such
(V−, ∆
−) is generic; therefore, by induction, the convex combination is simply qn−1.

14

(2) With probability 1− 1
n , a ∈ {1, · · · , n−1}. The bullet with speed 0 is shot in position a. The
bullet that follows is shot at time T τ
a+1 and has positive speed V σ
a+1: it hits the zero-speed
bullet immediately at time T τ
a+1 (observe that in (9), when vi = 0, T (i, j) = tj). In other
words, the zero-speed bullet remains the barrel and is thus bound to get hit by the next
bullet for it has positive speed.

Observe now that, in the latter case (2) when a ∈ {1, 2, . . . , n − 1}:

(2.i) if a = n − 1, then the last two bullets collide regardless of the conﬁguration of the n − 2
ﬁrst bullets and of the delays between them. If one conditions on the speed V σ
n of the
last bullet, and on the delays (∆τ
n−2, ∆τ
n−1)immediately before and after the time when
bullet n − 1 is shot, then the remaining structure is entirely exchangeable, and therefore
satisﬁes the induction hypothesis.

(2.ii) if a = 1, the same property holds (and the proof follows the same lines).

(2.iii) if 1 < a < n − 1, we need to condition on (a, V σ
a+1, ∆τ
a−1, ∆τ
a, ∆τ
a+1). Removing bullets
a and a + 1, we obtain a conﬁguration with n − 2 remaining bullets where the delay
between bullet a − 1 and a + 2 is now the sum of three components ∆τ
a−1 + ∆τ
a + ∆τ
a+1 of
∆n−1. Besides this, and the fact that two speeds V σ
a and V σ
a+1 are ﬁxed, the rest of the
conﬁguration is perfectly exchangeable. Now, in this case, a is uniform in {2, . . . , n − 2},
and since the distribution of V σ
a+1 is uniform among the other speeds, integrating on the
distribution of a – still conditioning on the other variables – by the induction hypothesis
the distribution of the surviving bullets is given by qn−2. Since this is true conditionally
on (σa+1, τa−1, τa, τa+1) whatever these values are, the conclusion follows.

The above decomposition implies that, for any 0 ≤ k ≤ n, we have

Pff
Vn,∆n−1(k) = P
V↓
n,∆n−1 = 1
n qn−1(k − 1) + (1 − 1
n
 ) qn−2(k) ,

(with qm(−1) = 0 for every m) and it follows that Pff
Vn,∆n−1 = qn. Since (Vn, ∆n−1) was
arbitrary, this completes the proof.

Assuming Model 3 follows qn, the following proposition shows that Models 1, 2 and 4 of
Section 1.1 are also governed by qn.

Proposition 14. Suppose that, for every (Vn, ∆n−1) ∈ Gn we have Pff
Vn,∆n−1 = qn. Then:
(i) For any laws µ (without atom) and ν (atoms allowed, except at 0), we have

Pru
n,µ = Prr
n,µ,ν = qn.

(ii) For any continuous (strictly) increasing function f : R+ → R+ with f (0) = 0, and any
(Vn, ∆n−1) ∈ Gn, we have P
faf,f
Vn,∆n−1 = qn .

Proof. (i) Both Pru
n,µ and Prr
n,µ,ν are annealed versions of Pff
V,∆. For any ﬁxed vector ∆n−1
of non-zero real numbers, (Vn, ∆n−1) ∈ Gn almost surely if Vn is obtained by sorting n i.i.d.
copies of a random variable with law µ. Taking the vector ∆n−1 as 1 = (1, 1, . . . , 1), we obtain
immediately that Pru
n,µ = qn. Furthermore, since ν has no atom at zero, min ∆n−1 > 0 with
probability one when ∆n−1 consists of a family of n − 1 i.i.d. random variables with distribution
ν, and it follows that Prr
n,µ,ν = qn.
(ii) Let (Vn, ∆n−1) ∈ Gn. Fix any continuous and (strictly) increasing f : R+ → R+
with f (0) = 0. Then the map Φ : R2 → R2 deﬁned by Φ(x, y) = (x, f (y)) is a one-to-one
correspondence between the space-time diagrams of the model

Pff
Vn,∆n−1 and those of P
faf,f
Vn,∆n−1.

15

This one-to-one correspondence induces a one to one correspondence between the virtual collision
points in both models which preserves the lexicographical order ≤lex on the plane: (x1, y1) ≤lex
(x2, y2) ⇔ Φ(x1, y1) ≤lex Φ(x2, y2). It follows immediately Φ preserves the order of the collisions,
and thus, the number and identities of surviving bullets. The claim follows readily.

3.2 Crossing a single singular point

We now state the main element of our strategy:

Lemma 15. The assumption (ii) of Lemma 13 holds: for every essentially generic parameter
(Vn, ∆n−1) in Gn, we have Pff
Vn,∆n−1 = Pff
V↓
n,∆n−1 .

The proof of this lemma will be decomposed, but it will somehow last until the end of Section
4. The proof roughly consists in showing that, as we continuously lower the minimum speed of
an essentially generic parameter (V, ∆), the probability distribution Pff
V,∆ remains unchanged.
This is only partially true, since as we lower the minimum speed, we may encounter singular
parameters, for which the colliding bullet problem is not even well-deﬁned. Fix (V, ∆) an
essential generic parameter in Gn. For λ ∈ [0, 1], the parameter

(Vλ, ∆) := ((1 − λ)V + λV↓, ∆)

is either a generic or a simple singular parameter; furthermore, there are at most ﬁnitely many
values 0 < λ1 < λ2 < · · · < λk < 1 for which (Vλ, ∆) is singular. By Lemmas 7 and 8, the map

λ ↦→ Pff
Vλ,∆ (18)

is constant on each of the intervals [0, λ1), (λi, λi+1), 1 ≤ i < k and (λk, 1]. As a consequence,
proving that the hypothesis of Lemma 13 holds reduces to showing that, for 1 ≤ i ≤ k, the left
and right limits at λi agree. Note that, by construction, for every 1 ≤ i ≤ k, the parameter
(Vλi, ∆) is simple singular, and every critical pattern for (Vλi, ∆) involves the minimum speed
λiV1. In the following, we call such a singular parameter honest. This latter fact is crucial for
the arguments to come. In other words, up to a change of variables, one is lead to studying the
diﬀerence between Pff
V+,∆ and Pff
V−,∆ where (V, ∆) is an honest singular parameter, and

Pff
V+,∆ := lim
λ→0− Pff
Vλ,∆ and P
ff
V−,∆ := lim
λ→0+ Pff
Vλ,∆ .

In the following, we refer to this as “crossing the singular point (V, ∆)”. Since the permutations
(σ, τ ) are uniformly random, proving that the two laws Pff
V+,∆ and Pff
V−,∆ agree consists in
verifying that, for every k ≥ 0, the number of the conﬁgurations for which k bullets survive
agree for both parameters. In the following, we often refer to these two limit colliding bullets
problem as (V−, ∆) and (V+, ∆), and what we mean here is that the pair (V−, ∆), (V−, ∆)
refers to any choice of (V−λ, ∆), (Vλ, ∆) with λ > 0 small enough such that (V, ∆) is the only
singular parameter among (Vµ, ∆) with µ ∈ [−λ, λ], the actual choice being in fact irrelevant.
There are some natural classes of conﬁgurations for which the numbers “obviously” agree.
We now expose some of those classes in order to better focus the remainder of the proof to the
classes of conﬁgurations for which some genuine work is needed.

(i) Only critical configurations matter. In words: the contribution to Pff
V+,∆ and to
Pff
V−,∆ of the conﬁgurations which do not contain any critical pattern is the same. Formally,
we say that a conﬁguration (σ, τ ) is critical for (V, ∆) if there exists a (necessarily unique)
(σ, τ )-critical pattern with respect to (V, ∆). We denote by C(V, ∆) = ∪πCπ(V, ∆) the set
of conﬁgurations that are critical for (V, ∆). If (σ, τ ) ̸∈ C(V, ∆) then ΓV+,∆(σ, τ, ·, ·, ·) =
ΓV−,∆(σ, τ, ·, ·, ·). Therefore, for every k ≥ 0, the numbers of non-critical conﬁgurations in
which k bullets survive are identical for (V−, ∆) and (V+, ∆).

16

We now look further at the critical conﬁgurations in C(V, ∆). Recall the notion of a realized
critical pattern and of a minimal critical pattern deﬁned in Section 2.5.

(ii) Only configurations with realized critical patterns matter. In words: the
contribution to Pff
V+,∆ and to Pff
V−,∆ of the conﬁgurations without any realized critical pattern
is the same. Formally, consider π = (min V, vℓ, vr, dℓ, dr) a critical pattern for (V, ∆). Fix a
conﬁguration (σ, τ ) ∈ Cπ \ Rπ for which the pattern is not realized. Then, by deﬁnition, at
least one of the bullets with speeds min V, vℓ or vr does not survive until the time where the
triple-collision is supposed to occur. As a consequence, the space-time diagrams of (V−, ∆) and
(V+, ∆) corresponding to (σ, τ ) are identical, and therefore, the number of surviving bullets is
the same in both situations. It follows that it suﬃces to consider the conﬁgurations (σ, τ ) ∈ ∪πRπ
in which the critical pattern is realized.

(iii) It suffices to consider minimal critical patterns. In words: the contribution to
Pff
V+,∆ and to Pff
V−,∆ of the conﬁgurations with a realized critical pattern which is not minimal
in the sense that it is not formed by three consecutive bullets can be reduced to a similar
structure on a bullet problem with less than n bullets, and can thus be treated by induction.
Formally, let π = (min V, vℓ, vr, dℓ, dr) be a critical pattern that is not minimal, that is at least
one of dℓ or dr is the sum of more than one component of ∆. Consider now Rπ, and suppose
that it is not empty (this requires, for instance, that both dℓ and dr are sums of an odd number
of elementary delays to ensure that the bullets shot “within the critical bi-triangle” pairwise
annihilate).
Fix (σ, τ ) ∈ Rπ. Let T τ
i , T τ
j and T τ
k , with 1 ≤ i < j < k ≤ n denote respectively the
times at which the bullets with speeds V1 = min V, vℓ and vr are shot. The conﬁguration
(σ, τ ) may be decomposed into two parts: an “outer” conﬁguration of speeds and delays on
[0, T τ
i ] ∪ [T τ
k , T τ
n ] and another “inner” conﬁguration of speeds and delays on [T τ
i , T τ
k ]. Of course,
these conﬁgurations are constrained by durations of the intervals, and the fact that both the
bullets shot from [0, T τ
i ) ∪ (T τ
k , T τ
n ] and from (T τ
i , T τ
k ) \ {T τ
j } should avoid the trajectories of the
bullets with speeds V1, vℓ and vr before the triple-collision.
We can decompose the conﬁguration (σ, τ ) as follows:

• outer conﬁguration: Let I := {σp : T τ
p < T τ
i or T τ
p > T τ
k } and J := {τp : p < i or p ≥ k}.
Then, |I| = i + n − k − 1 and |J | = i − 1 + n − k. Let V• denote the increasing reordering
of {Vp : p ∈ I} ∪ {V1, vℓ, vr}, and ∆
• the increasing reordering of {∆p : p ∈ J } ∪ {dℓ, dr}.
Then, (V•, ∆•) ∈ Θn+i−k+2.

• inner conﬁguration: Let V◦ and ∆◦ be the increasing reorderings of {Vp : p ̸∈ I} and
{∆p : p ̸∈ J }, respectively. Then (V◦, ∆◦) ∈ Θk+1−i.

The conﬁguration (σ, τ ) then corresponds to a pair of conﬁgurations, say (σ•, τ •) and (σ◦, τ ◦)
for (V•, ∆
•) and (V◦, ∆◦), respectively. Both (σ•, τ •) and (σ◦, τ ◦) contain the critical pattern
π, and it is realized; furthermore, π is minimally critical for (V•, ∆
•). We emphasize the fact
that, while a given conﬁguration gives rise to a single pair of parameters (V•, ∆•), (V◦, ∆◦), in
general, there may be more than one pair of parameters when one considers all the conﬁgurations
(σ, τ ) ∈ Rπ(V, ∆).
The fact that π is realized yields a kind of decoupling between the conﬁgurations (σ•, τ •) and
(σ◦, τ ◦): given any achievable pair of parameters (V•, ∆
•), (V◦, ∆
◦), and all the conﬁgurations
(σ•, τ •) for which π is realized, every conﬁguration of (σ◦, τ ◦) for which π is also realized is
compatible with (σ•, τ •). Therefore, the number of conﬁgurations (σ, τ ) for which π is realized
and the decomposition in pair of parameters is (V•, ∆
•), (V◦, ∆
◦) is the product #{(σ•, τ •) ∈
Rπ} × #{(σ◦, τ ◦) ∈ Rπ}. Furthermore, since the only bullets that may survive are those with

17

speed in V•, we have the reﬁned relation:

#{(σ, τ ) ∈ Rπ(V, ∆) : |SV,∆(σ, τ )| = k}

= ∑ #{(σ•, τ •) ∈ Rπ(V•, ∆
•) : |SV•,∆•(σ•, τ •)| = k} × #{(σ◦, τ ◦) ∈ Rπ(V◦, ∆◦)} ,

where the sum in the right-hand side extends over achievable pairs of parameters (V•, ∆
•),
(V◦, ∆◦). In other words, if we proceed by induction on n, the fact that the numbers of
conﬁgurations where some non-minimal critical pattern is realized agree is a direct consequence
of the fact that the numbers agree for all minimal critical patterns in a colliding bullets problem
of smaller size.

We can now state the result of the arguments above:

Proposition 16. Let (V, ∆) be an honest simple singular parameter. Moreover, let π =
(min V, vℓ, vr, dℓ, dr) be a minimal critical pattern for (V, ∆). If the distribution of the number
of surviving bullets in (V−, ∆) and (V+, ∆) agree when we restrict the count to conﬁgurations
in Rπ, then the distribution is preserved over Sn × Sn−1.

3.3 On the need for keeping track of constraints

The arguments of the previous section, summarized in Proposition 16, imply that we may
focus on honest simple singular parameters, and on conﬁgurations in which a minimal critical
pattern is realized. The minimality of the pattern and the fact that the minimal speed min V
is involved in the pattern imply that the constraints that π be realized in (σ, τ ) reduces to the
fact that no bullet hits the critical bitriangle from the right.
Now, a glance at Figure 5 suﬃces to note that, for a conﬁguration in Rπ, the sole eﬀect of
passing from V+ to V− is to release the line with speed vr, and replace the collision between
the bullets with speeds vℓ and vr by the collision between the bullets with speeds min V and
vℓ. Furthermore, in view of Fig. 5, for the conﬁgurations containing the minimal and realized
bi-triangle π, the two colliding bullets – those with speeds vℓ and vr before slowing down in
(V+, ∆) and those with speeds min V and vℓ in (V−, ∆) – do not contribute to the number of
surviving bullets. In spite of this, we cannot just suppress them:

• it would modify the colliding problem. For example, consider the case of V+.
Since the bullets with speeds vℓ and vr collide, the delays dℓ and dr merge. If we were to
remove the bullets with speeds vℓ and vr, there would be no bullet shot at time dℓ + dr
after the bullet min V. This would imply that the delay between the bullet with minimal
speed and the next one (if any), is the sum of three elementary intervals.

• Constraints persist. More importantly, the removal in the space-time diagram of the
bullets with speeds vℓ and vr does not remove the constraints they were holding: we
restricted ourselves to conﬁgurations where the critical pattern is realized; this restriction
a priori imposes restrictions on the conﬁgurations that may be obtained when removing
the bullets with speeds vℓ and vr.

For all the above reasons, we are led to consider more general models that allow to keep
track of the constraints imposed by the assumptions along the course of the induction argument.
This is developed in the next section, where we also complete the proof of Theorem 1.

4 Counting conﬁgurations with general restrictions

4.1 Two combinatorial models with constraints

The considerations of the previous section motivate the introduction of two colliding bullets
models with restrictions, which generalize the initial colliding bullets problem. It is the relation-

18

Figure 5: The evolution of the space-time diagram when crossing a singular parameter (V, ∆) for a
conﬁguration where the critical pattern is realized: The eﬀect of reducing the speed of the bullet forming
the left-side of the bi-triangle till it crosses the singular value of the parameter is to switch the pair of
bullets colliding in the vicinity of the triple point, and hence to also switch the bullet that survives.

ship between these two models that allows to compare the distributions Pff
V+,∆ and Pff
V−,∆ of
the number of surviving bullets when crossing a minimal singular parameter. Both models are
very similar to the initial colliding bullets problem, except that: there are a distinguished delay
∆⋆, a distinguished speed Vr and a distance s which, together with the minimal speed Vmin enter
into play to constrain the set of conﬁgurations that are allowed.
The vectors of speeds and delays are now denoted by Vn = (V1, · · · , Vn−2, Vmin, Vr) and
∆n−1 = (∆1, · · · , ∆n−2, ∆⋆), respectively3; we also enforce that Vmin is the minimal speed of
Vn. Hence, a conﬁguration is now a pair of permutations (σ, τ ) ∈ Sn−2 × Sn−1. Given the
permutation τ ∈ Sn−1 of the delays, we deﬁne a sequence of times (T τ
i )1≤i≤n, by

T τ
i = ∆τ1 + · · · + ∆τi−1, (19)

where for convenience we have written ∆n−1 := ∆⋆. Two of these times are distinguished and
correspond to the beginning and to the end of the interval corresponding to the distinguished
delay ∆⋆; we denote them by T τ
l and T τ
r, with the constraint that T τ
r − T τ
l = ∆⋆. The n − 2
remaining non-distinguished times are distinct and come with a natural ordering, and we denote
them by T τ
i , 1 ≤ i ≤ n − 2.
The speeds are then assigned to the times as follows: the speeds Vmin and Vr are assigned to
the distinguished times T τ
l and T τ
r in this order. The permutation σ ∈ Sn−2 then determines to
which non-distinguished time is assigned each one of the n − 2 non-distinguished speeds. We let

H = H(Vn, ∆n−1) (20)

denote the distance between the horizontal axis and the point HL(Vmin, 0) ∩ HL(Vr, ∆⋆), which
exists and lies above the axis since Vmin < Vr (see as Figure 6.)
The two new models, which, in passing, are combinatorial models, are parametrized by
(Vn, ∆n−1) ∈ Gn, a real number s ∈ [0, H], and a set A which will take in the sequel one of the
three values: {0}, Z+ or Z+ \ {0}. In both models, there is a special segment

S := HL(Vr, T τ
r) ⋂ [0, ∞) × [0, s].

3For the sake of simplicity, V is not a sorted vector anymore.

19

∆⋆ ∆⋆

H(V, ∆)

S S

Figure 6: The same conﬁguration is represented for the two constrained models (Models 8 and 9). In
red, the only lines corresponding to the distinguished speeds, forming what we will refer to as the special
triangle; in blue the special segment S used to restrict the conﬁgurations that are involved. The left side
of the special triangle is denoted by LS, and the right side by RS.

The restriction will come from the number of bullets whose true trajectory hits the segment S
in the space-time diagram. In both models, there is only one bullet that is shot from one of the
extremities of the distinguished interval corresponding to ∆⋆, and the name of the model refers
to whether it is shot from the left or the right end point. We phrase the models combinatorially,
but one should keep in mind that since we will counting conﬁgurations, there is an underlying
uniform measure on the (σ, τ ) ∈ Sn−2 × Sn−1.

Model 8 – Left model with restriction LR(Vn, ∆n−1, s, ·, ·). For (σ, τ ) ∈ Sn−2 × Sn−1:
• Shoot the bullet with speed Vσj at time T τ
j for 1 ≤ j ≤ n − 2; this gives rise to the virtual
trajectories HL(V σ
j , T τ
j ), 1 ≤ j ≤ n − 2.
• Shoot the bullet with minimal speed Vmin at time T τ
l; this corresponds to the virtual trajectory
HL(Vmin, T τ
l).
• No bullet is shot at time T τ
r.

For k ≥ 0, we denote by LR(Vn, ∆n−1, s, A, k) the set of conﬁgurations (σ, τ ) such that in the
(true) space-time diagram of the n − 1 bullets, the number of bullets whose true trajectory
crosses the segment S belongs to A, and k bullets eventually survive. ▹

Model 9 – Right model with restriction RR(Vn, ∆n−1, s, ·, ·). For (σ, τ ) ∈ Sn−2 × Sn−1:
• Shoot the bullet with speed Vσj at time T τ
j for j from 1 to n − 2; this gives rise to the virtual
trajectories HL(V σ
j , T τ
j ), 1 ≤ j ≤ n − 2.
• No bullet is shot at time T τ
l.
• Shoot the bullet with speed Vr at time T τ
r; this corresponds to the virtual trajectory HL(Vr, T τ
r).

For k ≥ 0, Denote by RR(Vn, ∆n−1, s, A, k) the set of conﬁgurations (σ, τ ) such that in the
(true) space-time diagram, the number of bullets that cross the segment S belongs to A, and k
bullets survive. (By convention, the bullet with speed Vr does not cross S.) ▹

The relationship between the two models when s = H and A = {0} is precisely the one
between the two versions of the original colliding bullet problem taken at two diﬀerent parameters
in the vicinity of a singular parameter: the consequence of a modiﬁcation of the minimal speed
is that the bullet which survives the “near triple collision” switches from the one with speed

20

Vmin to the one with speed Vr (or vice versa). (Compare Figures 5 and 6.) The other values for
s and A are used for the proof.
Let n ≥ 2 be a natural number and consider the three following properties; recall the sequence
of probability distributions qn deﬁned in (5) and (6).

P (1)
n : { for any generic parameter (Vn, ∆n−1) ∈ Gn we have Pff
Vn,∆n−1 = qn }

P (2)
n :
 



 for the set A being either {0}, Z+, or Z+ \ {0} we have
for all (Vn, ∆n−1) ∈ Gn, for all s ≤ H(Vn, ∆n−1), and for all k ≥ 0
|LR(Vn, ∆n−1, s, A, k)| = |RR(Vn, ∆n−1, s, A, k)|
 




P (3)
n :
 



 there exists a map gn : Z+ → Z+ such that
for any (Vn, ∆n−1) ∈ Gn and for all k ≥ 0 we have
|LR(Vn, ∆n−1, 0, {0}, k)| = |RR(Vn, ∆n−1, 0, {0}, k)| = gn(k)
 


 .

Remark. (i) In view of Proposition 14, the part that is currently missing to complete the proof
of Theorem 1 is precisely the fact that P (1)
n holds for every n.
(ii) We emphasize the fact that, in P (2)
n , it is not true that the two cardinalities

|LR(Vn, ∆n−1, s, A, k)| and |RR(Vn, ∆n−1, s, A, k)|

are independent of (Vn, ∆n−1) ∈ Gn.

Proposition 17. For any n ≥ 2, the properties P (1)
n , P (2)
n and P (3)
n all hold.

We will prove Proposition 17 by induction. We could not ﬁnd a argument that would proceed
by proving P (1)
n , P (2)
n and P (3)
n each separately, and it seems that one has to treat the bundle

Pn = { all three properties P (1)
n , P (2)
n and P (3)
n hold } (21)

in a single induction argument. This is the main reason why the following proof is slightly
intricate.
First, one easily veriﬁes that P1 and P2 both hold: this can be checked by inspecting the
cases: 0 or 1 bullet is ﬁred in all these models, except in P (1)
2 ; this latter case with two bullets is
simple enough to be checked easily. Now, the induction step necessary to prove Proposition 17
follows directly from Lemmas 18, 19 and 20 below:

Lemma 18. Let n ≥ 2. If Pn holds, then P (3)
n+1 holds.

Lemma 19. Let n ≥ 2. If Pm holds for all m ≤ n, then P (1)
n+1 holds.

Lemma 20. Let n ≥ 2. If Pn holds, then P (2)
n+1 holds.

Observe that Lemma 19 is what makes the link between the original bullet colliding problem
and the models with constraints described above precise. The proofs of these three Lemmas are
presented in the next Sections..

4.2 Proof of Lemma 19

Since Pm holds for m ≤ n, by Lemma 13, it suﬃces to prove that (17) holds for all
(Vn+1, ∆n) ∈ Gn+1 that is essentially generic. Then, by the arguments in Section 3.2 this reduces
to comparing the law of the number of surviving bullets for (V⋆
n+1+, ∆n) and (V⋆
n+1−, ∆n),
where (V⋆
n+1, ∆n) is a simple singular parameter Θn+1.

21

LS
 RS

γ S
 LS
 RS

γ S
 γ′

Figure 7: Illustration for the proof of Lemma 20: Either γ touches LS or it is intersected before by
some other line. (The lines γ and γ′ have been chosen with negative slopes only for the sake of clarity of
the representation.)

By Proposition 16, in order to compare (V⋆
n+1+, ∆n) and (V⋆
n+1−, ∆n) it suﬃces to consider
conﬁgurations for which there is some minimal critical pattern with respect to (V⋆
n+1, ∆n) that
is realised and involves the minimum speed.
There is a unique critical pattern for (V⋆
n+1, ∆n) and it is of the form π = (V1, Vℓ, Vr, dℓ, dr)
where both dℓ and dr are components of ∆n. For any conﬁguration (σ, τ ) where π is realized,

• in (V⋆
n+1+, ∆n) the bullets with speeds Vℓ and Vr collide;

• in (V⋆
n+1−, ∆n) the bullets with speeds V1 = min V⋆
n+1 and Vℓ collide.

Note that in both models, Vℓ does not play a role after the triple-collision, and it will be
suppressed from the parameter in the following. More precisely, writing ∆⋆ = dℓ + dr, and
reorganizing the components of the parameter into

V′
n = (V2, . . . , Vn−1, V1, Vr) ∈ Rn
+ where the speed Vℓ has been removed,
∆
′
n−1 = (∆1, . . . , ∆n, ∆⋆) ∈ Rn−1
+ since dℓ and dr have been merged into ∆⋆

we are precisely led to proving that
∣
∣LR (V′
n, ∆
′
n−1, s, {0}, k)∣
∣ = ∣
∣RR (V′
n, ∆′
n−1, s, {0}, k)∣
∣ for all k ≥ 0, (22)

for s = H(Vn, ∆n−1). Since we assumed P (2)
n , (22) holds and, in turn,

Pff
V⋆
n+1+,∆n = Pff
V⋆
n+1−,∆n ,

which completes the proof.

4.3 Proof of Lemma 20

First note that it suﬃces to establish the formula for A = Z+ and for Z+ \ {0} since one can
then recover the case A = {0} by a simple diﬀerence. Suppose that Pm hold for all m ≤ n and
ﬁx (Vn+1, ∆n) ∈ Gn+1.

The case A = Z+. In this case, there is no constraint on the number of trajectories intersecting
the special segment S. As a consequence, the previous arguments (that say that the case A = Z+
is equivalent to the case s = 0) show that P (3)
n+1 implies the desired property, and Lemma 18

proves that Pn implies P (3)
n+1 (and is proved independently of the current lemma later on).

The case A = Z+ \ {0}. In each of the conﬁgurations involved, some of the HLi hit the segment
S from the right. Consider those for which the lowest intersection point in S with these half
lines is reached by a given half line γ. Now, denote by RS and LS the right and left sides of the

22

triangle formed by the line segments with speed Vmin and Vr. There are two cases (represented
in Figure 7) depending on whether γ is intersected by some other half-line before reaching LS
or not:

(a) if γ touches RS and LS without being intersected : in this case, we prove directly (without
the induction hypothesis) that, for all k ≥ 0, we actually have equality of the two sets

LR(Vn+1, ∆n, s, Z+ \ {0}, k, γ) = RR(Vn+1, ∆n, s, Z+ \ {0}, k, γ) , (23)

where we added the entry γ to LR and RR to denote the set of conﬁgurations corresponding
to this situation. For any conﬁguration (σ, τ ) ∈ LR(Vn, ∆n−1, s, Z+ \ {0}, k, γ), it is clear
that (σ, τ ) ∈ ∪ℓ≥0RR(Vn, ∆n−1, s, Z+ \ {0}, ℓ), the only thing to prove is that taking (σ, τ )
as a conﬁguration of RR, there are precisely k surviving bullets. To see this, observe ﬁrst
that the line γ touches RS and LS without being hit in the LR model, and hits RS in the
RR model. Consider the triangle T formed by the horizontal line, the direction γ and LS.
Now, the bullet whose trajectory follows γ (see Figure 8):

• hits the bullet with minimum speed whose trajectory follows LS in LR, and

• hits the bullet with speed Vr whose trajectory follows RS in RR.

Therefore, in each case, the two corresponding bullets collide. Now, the rest of the con-
ﬁguration is unaﬀected by any of the collisions, because everything in both cases, happens
inside the triangle T , which is not intersected in both models. As a consequence, if there
are k surviving bullets in LR, there are also k surviving bullets in RR. One easily sees that
the argument actually proves the equality of the two sets in (23)4.

LS
 RS

γ S
 LS
 RS

γ S

LS
 RS

γ S

LR

RR

Figure 8: An illustration for the proof of Lemma 20 (a): A conﬁguration where the line γ is not
intersected before hitting LS: on the right we show the corresponding space-time diagrams in Models 8
and 9 where a bullet is shot along LS or RS, respectively. It is important to note that except inside the
blue shaded triangle, the two space-time diagrams are identical; as a consequence, the induction hypothesis
is not necessary in this case.

4We note here that we do not need to assume that the line γ is the line that immediately come after RS.
There may well be some bullets whose (real) trajectories are trapped in the triangle formed by RS and γ; these
are precisely the same in LR and RR because of our assumption that γ is the lowest line hitting RS.

23

(b) if γ touches RS and is intersected by some half line, say γ′ before touching LS: in this case,
we need the induction hypothesis to prove that, for all k ≥ 0,
∣
∣LR(Vn, ∆n−1, s, Z+ \ {0}, k, γ, γ′)
∣
∣ = ∣
∣RR(Vn, ∆n−1, s, Z+ \ {0}, k, γ, γ′)
∣
∣ , (24)

where we added the entries γ and γ′ to LR and to RR to denote the set of conﬁgurations corre-
sponding to this situation. Any conﬁguration (σ, τ ) in ∪k≥0LR(Vn, ∆n−1, s, Z+\{0}, k, γ, γ′)
is also a conﬁguration of ∪k≥0RR(Vn, ∆n−1, s, Z+ \{0}, k, γ, γ′), and reciprocally. Fix a con-
ﬁguration, that can be seen in both models. By assumption, we suppose that the half-lines
γ and γ′ intersect at some point p, before reaching LS (see Figure 9). Note that, in this
conﬁguration, any portion of the space-time diagram that is shot between LS and γ, or
between γ and γ′ must remain trapped between LS and γ, and γ and γ′, respectively (see
the two coloured regions in Figure 9); this must be the case both in LR and RR. As a
consequence, none of the corresponding bullets may survive in any of the two models; for
this reason, we can ignore them, and we now suppose that no bullet is shot between LS and
γ or γ and γ′. Now,

• in LR, the two bullets whose trajectory follow γ and γ′ indeed collide at the point p.
The rest of the space-time diagram is a set of half-lines that does not intersect γ′ before
the point p. The rest of the conﬁguration is just constrained not to hit the portion
of γ′ before p, that we call S′. There are k surviving bullets precisely if this smaller
conﬁguration lies in LR(V′
n−1, ∆
′
n−2, s′, S′, {0}, k), where V′
n−1, ∆
′
n−2 are obtained by
removing the necessary speeds, and merging the delays between LS and γ′, and s′

denotes the second coordinate of p.

• in RR, the bullet following γ collides with the one following RS. The rest of the
conﬁguration has the same constraint that the line segment S′ of γ′ before the point
p is not intersected by any real trajectory. As a consequence, there are k surviving
bullets precisely if that smaller conﬁguration lies in RR(V′
n−1, ∆
′
n−2, s′, {0}, k), where
it is important to note that V′
n−1, ∆
′
n−2 and s′ are the same as above.

Next observe that there is a one-to-one map between the conﬁgurations of n + 1 lines and
the ones with n − 1 lines5. It follows by the induction hypothesis that for each k, the sets
LR(V′
n−1, ∆n−2, s′, {0}, k) and RR(V′
n−1, ∆n−2, s′, {0}, k) have the same cardinalities, and
as a consequence, that (24) holds for all k.

4.4 Proof of Lemma 18

As before, the general idea consists in proving that we can modify the parameters (Vn, ∆n−1),
making sure that we modify the statistics in either LR or RR, until we arrive to a situation where
we can without a doubt assert that these statistics are equal. In the previous proofs, the crucial
modiﬁcation consisted in decreasing the speed of the slowest bullet. Here, we rely on a diﬀerent
modiﬁcation for the following reasons:

• Although the models LR and RR seem to be images of one another under some natural
symmetry, it is not the case. In particular, the fact that the slowest speed is the one that
lies to the left of the special interval of length ∆⋆ ruins the nice symmetries; for instance,
no bullet may hit the slowest bullet from the left while it is certainly possible that a bullet
hits the one shot right after ∆⋆ from the right.

5because we removed the “trapped” portions; otherwise it would be many-to-one, but the counting would still
work since the constraints on the “trap” are the same in both models.

24

LS
 RS

γ S
 γ′ LS S′
RS′

LS
 RS

γ S
 γ′ LS S′
RS′

LR

RR new RR

new LR

Figure 9: An illustration for the proof of Lemma 20 (b): The space-time diagrams in Models 8 and 9 of
a single conﬁguration where γ is hit by some line γ′ before hitting LS (the one from Figure 7). One can
transform the conﬁguration into one for new matching LR and RR problems, where the critical pattern is
modiﬁed. The new critical bi-triangle is shown shaded in red. The instance is of smaller size, and allows
to use the induction hypothesis.

• More importantly, recall that we said that the distribution of the number of surviving
bullets does not in general remain the same if the permutations σ and τ of the speeds and
delays are not independent. Here, the fact that the slowest speed is shot right before the
interval of length ∆⋆ creates a dependence which makes diﬃcult to reduce the question
to the initial colliding bullet problem where the intervals and speeds are all permuted
independently.

Observe that
 LR(Vn, ∆n−1, 0, {0}, k) and RR(Vn, ∆n−1, 0, {0}, k)

are sets of conﬁgurations in a model where n − 1 bullets are ﬁred, but since the special segment
S has length zero (and no bullet with speed 0, for the case when min Vn = 0 can be treated
directly), there are no restriction of any kind. In fact, we will prove a bit more than what is
needed: we will prove that the equality of the statistics holds even if the speed Vmin attached
to the left of the special interval ∆⋆ is any ﬁxed speed (minimal or not). In other words, we do
not assume that Vmin is the minimal speed anymore in this section, but keep the name because
the order of the speeds in Vn has been deﬁned with this name (Vmin has been placed in second to
last position).
Since the permutations (σ, τ ) we consider let attached ∆⋆ and Vmin (or ∆⋆ and Vr), the
statistics LR(Vn, ∆n−1, 0, {0}, ·) (resp. RR(Vn, ∆n−1, 0, {0}, ·)) are only clearly given by qn−1
when ∆⋆ = 0, since this case corresponds exactly to Pff
Vn−1,∆n−2 where ∆n−2 is obtained from
∆n−1 by removing ∆⋆ and Vn−1 is obtained from Vn by suppressing Vr (resp. Vmin).
The idea of the proof is similar to that of Lemma 4.3, but rather than decreasing the minimal
speed, we decrease the length ∆⋆. Proceeding in this way addresses the two issues mentioned
above: it does act symmetrically on LR and RR and, eventually, when ∆⋆ = 0, the dependence
between the permutations of the speeds and delays vanish. In the following, we consider only
one of the problems LR or RR: it important to understand that we do not compare directly LR

25

and RR which seems diﬃcult; we proceed by justifying that we can reduce ∆⋆, without changing
the statistics, until it reaches zero, at which point, LR and RR are identiﬁed.
The core of the argument still relies on the kind of decompositions and reductions of the
conﬁgurations that we have already treated in detail earlier and which should be familiar to the
reader by now. So, since we have mentioned the main diﬃculty and the diﬀerences with the
previous arguments, we allow ourselves to be quicker and only sketch the argument.
When decreasing ∆⋆ at the same time in LR and RR, if the TCS is not modiﬁed, then the
statistics are not modiﬁed. So we focus on the situations when the TCS does change: there
exists conﬁgurations (σ, τ ) for which one line from either side (before or after ∆⋆) crosses the
intersection of two lines originating from the other side. Only the conﬁgurations for which such
a situation occurs need to be considered; furthermore, only the conﬁguration for which the
crossing indeed modiﬁes the set of surviving bullets (at least locally) matter. This allows for
the deﬁnition of notion of critical pattern or bi-triangle similar to the one is Section 2.5 (see
Figure 10). As before, an induction argument allows to suppose that the critical pattern is
minimal. Altogether, we are led to the situations described in Figure 10. Putting everything
together, crossing a critical point of ∆⋆ reduces to verifying that the statistics of LR and RR are
identical for a problem of smaller size, and thus the induction hypothesis applies.

∆
? ↓∆
? ↓∆
?∆
?∆
?∆
?
∆
?
new LRnew RR
 Figure 10: An illustration for the proof of Lemma 18: The typical eﬀect of diminishing the value of ∆⋆:
one reaches a critical value for which there is a critical pattern involving three lines. The red lines are
there to help comparing the statistics before and after the ‘crossing’ of this critical value, which reduces
to comparing the statistics of a couple of models LR / RR involving a smaller number of bullets.

5 Remaining proofs

5.1 Proof of Theorem 3

(i) Bullet Flock. Observe that the eventual number of surviving bullets only depends on the
order of the speeds, not on their speciﬁc values. It does not depend either on the interbullet
delays since the collisions are instantaneous. Assume that the bullet with minimal speed is shot
at time i and that its speed is vi. Being the slowest, it does not inﬂuence any of the bullets shot
at times 1, 2, . . . , i − 1. Furthermore, it will be hit by the next bullet i + 1, except of course

26

if there is no such bullet that is, if i = n which happens with probability 1/n. Of course, the
behaviour of the bullets shot from time i + 2 is not inﬂuenced. Removing the bullets i, and i + 1
when the latter exists leaves the system in an exchangeable situation again, with n − 1 or n − 2
bullets. The result follows readily from the recursive deﬁnition of qn.

(ii) Odd cycles in permutations. We proceed again by induction on n. Consider the element
with label 1 and the cycle C containing it. A straightforward computation shows that the length
|C| of C is 1 with probability 1/n (in which case, 1 is a ﬁxed point). If |C| > 1, then let b be the
image of 1 in the permutation (the number just after it around C). By symmetry, b is uniform
in {2, · · · , n}. Let also c be the image of b, and z the preimage of 1. Note that we might have
c = 1 and z = b if |C| = 2, or z = c if |C| = 3. Consider now the cycle structure obtained as
follows:

• suppress the elements 1 and b from this cycle representation;

• if z ̸= b, modify its image in the permutation so its new image is c.

A simple combinatorial argument shows that the remaining structure is the cycle representation
of a permutation that is uniformly distributed in the symmetric group on S′ = {1, 2, · · · , n} \
{1, b}: indeed, from a given permutation on S′ with cyclic representation (C′
1, · · · , C′
ℓ) all the
potential initial permutations can be obtained by

• either adding the cycle (1, b) on its own,

• or inserting the linked pair 1, b to the right of any element in one of the cycles C′
j; the
number of choices for the location of this insertion equals ∑
j |C′
j| = n − 2, and thus does
not depend on (C′
1, . . . , C′
ℓ).

This previous decomposition immediately yields the recurrence relation that deﬁnes qn.

(iii) Two-step directed tree. In this case, the claim is straightforward since for every n, the
distance to 0 clearly satisﬁes the recurrence relation (7) by construction.

5.2 Proof of Proposition 2

The limit distribution for a random variable Xn under qn follows from the combinatorial
decomposition. Recall that, by Theorem 3, Xn is distributed as the number of cycles of odd
length in a uniformly random permutation of length n. Since a permutation is a set of cycles,
classical combinatorial decomposition [7] yields that the bivariate generating function counting
permutations where the cycles are marked by u and size by z is

P (z, u) = ∑

n≥0
 ∑

k≥1 pn,ku
k zn

n! = exp(−u log(1 − z)),

where pn,k is the number of size n permutations with k cycles multiplied by n!. Here, we want
the simple modiﬁcation P ◦(z, u) of P (z, u) where u only marks the cycles of odd length, and we
let P (z, u) be the corresponding generating function. We ﬁnd

P ◦(z, u) = exp (
u
[ − log(1 − z) + 1
2 log(1 − z2)] − 1
2 log(1 − z2)
)

= (1 + z)(u−1)/2 · (1 − z)−(1+u)/2.

The only two potential singularities are z = ±1, and as a function of z, the generating function
P ◦(z, u) is clearly analytic in the following disk with two dents:

D := {z ∈ C : |z| ≤ 2, arg(z − 1) > π/12, arg(1 − z) > π/12}.

27

If u = 1, then P ◦(z, 1) = 1/(1 − z) and there is a unique singularity at 1; otherwise, for any
u in a complex punctured neighborhood U of 1, P (z, u) has two singularities at z ∈ {+1, −1}.
In this case, the domain D is what is referred in [7] as a ∆-domain and the singularity analysis
transfer theorem implies that, as n → ∞, the main contribution comes from z = 1 (the other
one has a lower order polynomial growth in n) and we have

[zn]P ◦(z, u) = 1
n!
 ∑

k≥1 p◦
n,ku
k ∼ 2(u−1)/2

Γ( 1+u
2 ) n(u−1)/2.

We shall need a uniform estimate for u ∈ U , and we must look into the contribution of (1 +
z)(u−1)/2 more carefully: standard binomial expansion yields the exact formula

[zn](1 + z)
(u−1)/2 = Γ( 1−u
2 + n)
Γ( 1−u
2 )Γ(n) .

For any ϵ > 0, choosing U to be the punctured ball of radius 2ϵ around 1, it follows that,
uniformly in U , as n → ∞,

∣
∣
∣[zn](1 + z)(u−1)/2∣
∣
∣ ≤ Γ(n + ϵ)
Γ(ϵ)Γ(n + 1) ∼ nϵ−1

Γ(ϵ) .

Standard manipulations then imply that the probability generating function fn(u) = E[uXn]
satisﬁes, again uniformly in U provided that ϵ ∈ (0, 1),

fn(u) = [zn]P ◦(z, u)
[zn]P ◦(z, 1) ∼ 2(u−1)/2

Γ( 1+u
2 ) e 1
2 (u−1) log n.

The quasi-powers theorem (Theorem IX.8 of Flajolet and Sedgewick [7]) immediately yields that
EXn ∼ 1
2 log n, Var(Xn) ∼ 1
2 log n and the claimed Gaussian limit distribution for Xn.

5.3 Proof of Proposition 4

(i) Let Tx denote the time (number of bullets to shoot) to destroy the slowest bullet in the
ﬂock given that it has a given speed x ∈ [0, 1]. Considering the speed of the bullet that is ﬁrst
shot yields the following integral equation for Tx:

E(Tx) = 1 + x (E(TU x) + E(Tx)) , (25)

where U is an random variable uniform on [0, 1]. This is a simple diﬀerential equation, and one
obtains, with the condition that T0 = 1 almost surely,

E(Tx) = 1/(1 − x)
2.

This shows in particular that for every x, Tx is almost surely ﬁnite, and in turn, that the time
to destroy any ﬁnite number of bullets is also ﬁnite. This ensures that Fn = 0 inﬁnitely often.
(ii) For the case of the distances in the two-step tree, one easily veriﬁes that the two sub-
sequences (D2k)k≥1 and (D2k+1)k≥0 are non-decreasing. The convergence in probability thus
implies almost sure convergence, and in turn the fact that there exists a (random) integer n0
such that Dn ≥ 1 for all n ≥ n0, which proves the claim.

28

References

[1] V. Belitsky and P.A. Ferrari. Ballistic annihilation and deterministic surface growth. Journal of
Statistical Physics, 80:517–543, 1995.
[2] E. Ben-Naim and S. Redner. Decay kinetics of ballistic annihilation. Physical Review Letters, 70:
1890–1893, 1993.
[3] M. Droz, P.-A. Rey, L. Frachebourg, and J. Piasecki. Ballistic annihilation kinetics for a multivelocity
one-dimensional ideal gas. Physical Review E, 51:5541–5548, 1995.
[4] B. Dygert, M. Junge, C. Kinzel, A. Raymond, E. Slivken, and J. Zhu. The bullet problem with
discrete speeds. arxiv:1610.00282 [math.PR], 2016.
[5] Y. Elskens and H. Frisch. Annihilation kinetics in the one-dimensional ideal gas. Physical Review
A, 31:3812–3816, 1985.
[6] A. Ermakov, B. T´oth, and W. Werner. On some annihilating and coalescing systems. Journal of
Statistical Physics, 91:845–870, 1998.
[7] Ph. Flajolet and R. Sedgewick. Analytic Combinatorics. Cambridge University Press, New York,
NY, USA, 1 edition, 2009. ISBN 0521898064, 9780521898065.
[8] Forumers. https://math.stackexchange.com/questions/1526292/colliding-bullets, .
[9] Forumers. https://www.reddit.com/r/mathriddles/comments/3sa4ci/colliding_bullets, .
[10] M. Kleber and D. Wilson. “Ponder This” IBM research challenge. URL https://www.research.
ibm.com/haifa/ponderthis/challenges/May2014.html.
[11] P. L. Krapivsky and Cl´ement Sire. Ballistic annihilation with continuous isotropic initial velocity
distribution. Physical Review Letters, 86(12):2494–2497, Mar 2001. ISSN 1079-7114. doi: 10.1103/
physrevlett.86.2494. URL http://dx.doi.org/10.1103/PhysRevLett.86.2494.
[12] P.L. Krapivsky, S. Redner, and F. Leyvraz. Ballistic annihilation kinetics: The case of discrete
velocity distributions. Physical Review E, 51:3977–3987, 1995.
[13] J. Piasecki. Ballistic annihilation in a one-dimensional ﬂuid. Physical Review E, 51:5535–5540, 1995.
[14] V. Sidoravicius and L. Tournier. Note on a one-dimensional system of annihilating particles.
arXiv:1610.05955 [math.PR], 2016.
[15] E. Trizac. Scaling in ballistic annihilation kinetics. Journal of Physics: Condensed Matter, 14:
2159–2166, 2002.
[16] Emmanuel Trizac. Kinetics and scaling in ballistic annihilation. Physical Review Letters, 88(16), Apr
2002. ISSN 1079-7114. doi: 10.1103/physrevlett.88.160601. URL http://dx.doi.org/10.1103/
PhysRevLett.88.160601.
 29
