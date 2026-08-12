<!-- source: https://arxiv.org/pdf/0811.0908 | converted from PDF -->

arXiv:0811.0908v2  [cond-mat.stat-mech]  7 Nov 2008
Statistical properties of the ﬁnal state in one-dimensional ballistic aggregation

Satya N. Majumdar
Laboratoire de Physique Th´eorique et de Mod`eles Statistiques (UMR 8626 du CNRS),
Universit´e Paris-Sud, Bˆatiment 100 91405 Orsay Cedex, France

Kirone Mallick
Institut de Physique Th´eorique Centre d’ ´Etudes de Saclay, 91191 Gif-sur-Yvette Cedex, France

Sanjib Sabhapandit
Raman Research Institute, Bangalore 560080, India
(Dated: November 2, 2018)

We investigate the long time behaviour of the one-dimensional ballistic aggregation model that
represents a sticky gas of N particles with random initial positions and velocities, moving determin-
istically, and forming aggregates when they collide. We obtain a closed formula for the stationary
measure of the system which allows us to analyze some remarkable features of the ﬁnal ‘fan’ state.
In particular, we identify universal properties which are independent of the initial position and
velocity distributions of the particles. We study cluster distributions and derive exact results for
extreme value statistics (because of correlations these distributions do not belong to the Gumbel-
Fr´echet-Weibull universality classes). We also derive the energy distribution in the ﬁnal state. This
model generates dynamically many diﬀerent scales and can be viewed as one of the simplest exactly
solvable model of N -body dissipative dynamics.

PACS numbers: 68.43.Jk, 02.50.-r, 05.40.-a, 47.70.Nd

I. INTRODUCTION

The ballistic aggregation model is one of the simplest interacting particles processes of non-equilibrium statistical
mechanics and as such has attracted a lot of attention in the past decades [1]. This model represents a gas of N
unit-mass particles forming clusters through perfectly inelastic adhesive collisions. The motion of a particle between
two collisions is deterministic and free (i.e. ballistic) and the total mass and momentum in a collision are conserved
whereas the kinetic energy is dissipated. The stochasticity in this model is due only to the initial conﬁguration
which consists of single particles randomly located with uncorrelated random velocities drawn from a continuous
distribution. This dissipative system, usually referred to as ballistic aggregation or sticky gas, appears as a minimal
model of cluster formation and provides a relevant statistical description of the merger of coherent structures such as
vortices, thermal plumes, ﬂowing granular media [2] or the accumulation of cosmic dust into planetoids. The ballistic
aggregation model also plays a role in the study of the large-scale structure of the universe because the motion of
self-gravitating matter in the expanding universe is similar to that of matter moving solely by inertia [3, 4]. Another
noteworthy feature of this model stems from its connection with the Burgers equation, an important toy model in
the study of turbulence: it can be shown that at very high Reynolds number, the solution of the Burgers equation
in the long time limit consists of a series of shocks which follow exactly the dynamics of the ballistic aggregation
model [5, 6, 7].
Ballistic aggregation exhibits at long time t a self-similar coarsening behaviour ﬁrst studied by Carnevale, Pomeau
and Young [1]. In one dimension, the coarsening regime occurs for intermediate times satisfying t ∼ N 3/2, N being
the total mass or equivalently the total number of initial particles in the system. For longer times, and in the absence
of any boundary, the system ultimately reaches a state where no more collisions are possible: the particles are grouped
into clusters of diﬀerent sizes (or masses) with velocities increasing from left to right. This ﬁnal ordered state will be
called the “fan” state. Once this state is reached, there is no further loss of energy and the system becomes stationary.
The aim of this paper is to investigate the properties of this fan state. We ﬁnd an exact analytic formula for
the joint probability distribution of the sizes and velocities of the clusters by mapping the ﬁnal state of the ballistic
aggregation model to the convex minorant of a one-dimensional random walk. From this invariant measure that fully
characterizes the set of all possible fan states, various statistical properties of the model in the long time limit will be
derived. In particular, we shall retrieve the known fact [10, 11, 12] that the probability of obtaining a fan state with
exactly k clusters is a purely combinatorial factor (which is universal in the sense that it does not depend upon the
initial velocity distribution of the particles). We shall prove that the cluster distribution in the fan state is identical
to the statistics of cycles in a random permutation of N objects [13, 14], both problems having a common underlying
combinatorial structure related to the convex minorant construction [15, 16]. This will allow us to characterize the
diﬀerent scales that are dynamically generated in the system: in the large N limit, the size of a typical cluster is of

2

order N/ ln N , the largest cluster contains a ﬁnite fraction of the total mass N and hence grows linearly with N , the
smallest cluster scales as ln N , and the rightmost cluster, which has the leading velocity, has a size of order √
N . We
shall also derive the (non-universal) joint distribution of mass and velocity of this ‘leader’ which is very diﬀerent from
the usual extreme-value distributions obtained for uncorrelated random variables. Finally, we shall show that the
energy remaining in the system after all collisions have ended is of the order ln N and shall calculate the distribution
of the scaling variable E/ ln N .
The paper is organized as follows. In Section-II we deﬁne the ballistic aggregation model and focus on its ﬁnal
fan state. In particular, we show how the statistical properties in the fan state are related to those of the convex
minorant of an associated one dimensional random walk problem. This mapping allows us to derive explicitly the
joint distribution of the cluster sizes and their velocities in the fan state which is one of the key results of this paper.
In Section-III we show how this joint distribution can be used to derive the cluster size distribution in the fan state
which turns out to be universal (with respect to the initial velocity distribution). This universal property is shown
to be related to the statistics of cycles lengths in a random permutation problem. In Section-IV, we further exploit
the joint distribution to compute exact asymptotic results for certain extreme variables in the fan state such as the
size and the velocity distribution of the rightmost (‘leader’) cluster. In Section-V, we derive the exact asymptotic
distribution of energy in the fan state. Finally we conclude in Section-VI with a summary and some open problems.

II. STATISTICAL DESCRIPTION OF THE STATIONARY STATE

A. Deﬁnition of the Model

The ballistic aggregation problem in one dimension is an elementary interactive particles process, the dynamics of
which is deﬁned as follows. At the initial time t = 0, we start with N particles randomly located on an inﬁnite line.
We label the particles as i = 1, 2, . . . , N according to the order of their initial positions from left to right (see Fig. 1
where we have taken N = 6). We denote by vi and mi, respectively, the initial velocity and the mass of the i-th
particle. For t > 0, each particle moves ballistically at constant speed. When two particles meet they coalesce and
form a single new particle whose mass is the sum of the initial masses and whose momentum is the sum of the initial
momenta. The only randomness in the model lies in the initial conditions, i.e. the initial positions and velocities
of each particle. We shall assume that the initial velocities {vi}’s are uncorrelated random variables, drawn from a
common continuous probability density function (PDF) φ(v). For simplicity, we assume that all the initial masses
are the same and take them to be unity. Once the initial conditions are given, the evolution of a given realization is
deterministic and fully determined by the mass and momentum conservation laws. The shocks being totally inelastic,
energy is dissipated at each collision.
At late times t ≫ O(1) (but before the system feels the ﬁniteness of the mass N ), the ballistic aggregation model
exhibits a coarsening regime where typical cluster size grows with time as a power law, as studied ﬁrst by Carnevale,
Pomeau and Young [1] using scaling arguments and numerical simulations. For example, in this regime, the average
size (or mass) of a particle-cluster grows as t2D/(2+D) and its velocity decreases as t−D/(2+D), D being the spatial
dimension. The global mass of the system being conserved, the total energy of the system decays as t−2D/(2+D). These
exponents derived in [1] turn out to be correct in one dimension where the problem is exactly solvable [4, 8, 9]. This,
however, turns out to be a bit fortuitous. In higher dimensions, the exponents predicted in [1] turn out to be incorrect
due to strong correlations between the velocities of the colliding clusters at late times [17]. In one dimension, it is
possible to calculate exactly (in one dimension) the mass distribution of the clusters [4, 8, 9] in the scaling limit when
N → ∞ (N being the total mass of the system) and t → ∞, keeping the ratio t/N 3/2 ﬁnite [4, 8, 9]. However, these
scaling results for the coarsening regime are valid only for intermediate times satisfying t ∼ N 3/2. When t ≫ N 3/2,
the system evolves into a stationary state in which no more collisions can occur: the particles are grouped in k disjoint
clusters of diﬀerent masses, where k itself is a stochastic variable. Each cluster moves at a constant velocity, and
the speed of a given cluster is larger than that of its left neighbour (if any) and less than that of its right neighbour
(if any). In this ultimate state the clusters keep on moving farther apart, i.e., they fan out from each other with
increasing time, thus justifying the name “fan” state (see Fig. 1). Once this fan state is reached, there is no further
collision and hence no further dissipation of energy.
In this work, we shall focus on the statistical description of the fan state of the random aggregation process. We
shall show that properties of the fan state related to the sizes of the clusters (regardless of their respective ordering and
their velocities) are universal as they do not depend on the PDF φ(v) from which the initial velocities of the particles
are drawn. The cluster statistics can in fact be mapped to the cycle length distribution in random permutations,
which are fundamental combinatorial objects. From this observation the distribution of the cluster masses and in
particular the typical mass of the largest and the smallest cluster can readily be calculated. When the distribution
of the velocities of the clusters is taken into account, universality with respect to φ(v) is lost. However, in the large

3

t=0

t
FAN  STATE ( long time limit )

m=1 m=1 m=2 m=2
m=2m=1 m=3

m=1 for all particles
 5 64321

FIG. 1: An example of a conﬁguration of 6 particles with identical initial mass mi = 1 and varying initial velocities, evolving
in the long time limit into the fan state: the velocities are now increasing from left to right and there are no more colllisions.

N limit, we will see that some universality is restored, thanks to the central limit theorem, in the size distribution of
the rightmost cluster (the leader) provided the second moment σ2 = ∫ ∞
−∞ v2 φ(v) dv is ﬁnite. Finally, we are also able
to calculate explicitly the energy distribution in the fan state, but only for the special case when φ(v) is Gaussian.

B. The Fan State as a Convex Minorant

The fan state of the random aggregation process can be determined geometrically from the initial conditions [11].
We now explain this graphical interpretation of the fan state as a convex minorant of a random walk. Recall that we
label the particles as i = 1, 2, . . . , N according to the order of their initial positions from left to right (see Fig. 1) and
that we denote by vi respectively the initial velocity of the i-th particle (all the initial masses being unity). For any
realization of the initial state {v1, v2, . . . , vN }, the ﬁnal state is uniquely determined i.e. the number of ﬁnal clusters,
their masses and their velocities are unique.
The initial state {v1, v2, . . . , vN } of the system is represented by a broken graph (P0, P1, . . . , PN ) (see Fig. 2) such
that:
(i) P0 = (0, 0) is the origin;
(ii) the coordinates of Pi are given recursively by Pi = Pi−1 + (1, vi) for 1 ≤ i ≤ N .
In other words, the speed vi of the i-th particle is represented by the slope of the line (Pi−1Pi). We also emphasize
that the horizontal coordinate of Pi does not correspond to the actual position of the i-th particle but only on its
label.
More generally, if we had started with particles having diﬀerent masses {m1, m2, . . . , mN } the coordinates of Pi
would be Pi = Pi−1 + mi(1, vi) [11]. In other words, the initial state is drawn as a random walk in the cumulative
momentum and cumulative mass space as shown in Figs. 2 and 3.
Suppose that the ﬁrst collision occurs between particles i and (i + 1) with velocities vi and vi+1 respectively.
These two particles can aggregate if vi > vi+1, which means that the slope of the (Pi−1Pi) is larger than the slope
of the (PiPi+1). Equivalently, this means that Pi is located above the segment (Pi−1Pi+1) i.e., locally, the graph
(Pi−1PiPi+1) has a negative curvature. After this collision, a cluster is formed with mass 2 and velocity (vi + vi+1)/2.
This cluster is represented by the vector (Pi−1Pi+1) (see Fig. 2) with coordinates (2, vi + vi+1). We note that the
slope of this vector again represents the velocity of the cluster. We now have a system of N − 1 ‘particles’, with N − 2
particles of mass 1 and one particle of mass 2. The state of this system is represented by a broken line in which the
angle (Pi−1PiPi+1) with downward curvature is replaced by its base (see Fig. 2). Similarly, the next collision is also
represented graphically by replacing another angle with downward curvature by its base (see Fig. 2) . This process
will continue iteratively and the particles will aggregate forming clusters till all angles with downward curvature have
been eliminated, i.e. all collisions have occurred. It follows that for any given initial state, the ﬁnal state is uniquely
given by the convex minorant of the corresponding random walk. Each line segment of the convex minorant represents
a cluster in the fan state, —the horizontal and the vertical components of the segment give respectively the mass and
the momentum of the cluster, i.e., the slope gives the velocity of the cluster. The geometry of the convex minorant

4

NEXT COLLISION FIRST COLLISION

Pi

Pi−1 Pi+1

P0
 PN

FIG. 2: Initial conﬁguration is represented by a graph (thin line) joining P0 to PN (we have taken mj = 1 ∀j). This graph can
be interpreted as a random walk in the cumulative momentum and cumulative mass space. After the ﬁrst collision the particles
i and i + 1 aggregate into one cluster: in the associated graph, the angle (Pi−1PiPi+1) is replaced by the segment (Pi−1Pi+1).

i∑

j=1 mjvj
 mjvj
 mj
 nℓuℓ
nℓ
 i∑

j=1 mj
0

FIG. 3: We draw the convex minorant of the graph representing the same initial conﬁguration as in Fig. 2. This convex
minorant represents the ﬁnal ‘fan’ state in which no more collisions can occur. Each straight segment of the convex minorant
corresponds to a cluster of nl particles with momentum nlul.

(including the number of segments which represents the number of ﬁnal clusters), however, diﬀers from one realization
of initial conditions to another. Various statistical properties of the ballistic aggregation in the fan state can be found
from the statistical properties of the underlying convex minorant.

C. The Invariant Measure in the Fan State

We now derive the joint probability distribution which describes the fan state. Let pN (k; {ni, ui}) denote the joint
PDF of having k clusters in the fan state of masses and velocities ni and ui respectively, with i = 1, 2, . . . , k. Note that
the various segments of the convex minorant (see Fig. 3) are correlated as their slopes must be increasingly ordered
from left to right, i.e., u1 < u2 < · · · < uk. Moreover, the total mass is conserved, ∑k
i=1 ni = N . Once these two
constraints are speciﬁed, the momentum of each ﬁnal cluster is essentially determined by the conservation law:

nℓuℓ =
 Nℓ∑

j=Nℓ−1+1 mjvj (1)

for the ℓ-th cluster with ℓ = 1, 2, . . . , k. We have deﬁned here the cumulated masses Nk = n1 + . . . + nk. The sum in
the above equation is thus restricted to the initial velocities of those particles which form the ℓ-th cluster. We also
recall that mj = 1 ∀j. However, most importantly, to form a speciﬁc (say ℓ-th) ﬁnal cluster (i.e., a line segment in the

5

underlying convex minorant) by aggregation of nℓ consecutive initial particles, the portion of the underlying random
walk of nℓ steps must be such that it originates from one end of the line segment of convex minorant and ﬁnishes at
its other end, while staying above the segment in the intermediate steps. Now, consider a random walk of nℓ steps
that starts from one end of a line segment and ﬁnishes at its other end, but is otherwise allowed to cross the segment
in the intermediate steps. For any realization of such a walk, given that there is one unique minimum with respect
to the segment, if we consider all the nℓ cyclic permutations of the steps, then out of nℓ diﬀerent realizations of the
walks there is one and only one arrangement where in the intermediate steps the walk stays above the segment. This
property is known as Raney’s lemma [18, 19]. (Here, the uniqueness of the arrangement is guaranteed by the fact
that the PDF φ(v) is continuous).
Thus, the probability that a random walk of nℓ steps that starts at one end of a line segment and ﬁnishes at its
other end while staying above the segment in-between equals 1/nℓ. Note that this probability is independent of the
slope uℓ of the segment as well as the PDF φ(v) of the jump-lengths. Finally, gathering all the above inputs together
we write
 pN (k; {ni, ui}) = δ
 (

N −
 k∑

i=1 ni
) k−1∏

i=1 θ(ui+1 − ui)

×
 k∏

ℓ=1
 1
nℓ
 〈
δ
 

uℓ − 1
nℓ
 Nℓ∑

j=Nℓ−1+1 vj



〉
 , (2)

where the angle brackets ⟨· · · ⟩ denote the averaging over the set of initial velocities {vi}. This key result provides a
full statistical description of the clusters sizes and velocities in the fan state. From this joint probability distribution,
all the statistical properties of the ﬁnal state can be derived.

III. UNIVERSAL STATISTICAL PROPERTIES OF CLUSTERS IN THE FAN STATE

In this section, we compute the distribution of the number and sizes of the clusters in the fan state: we will show
that this distribution, obtained by integrating out the velocities of the clusters from the joint probability distribution
given in Eq. (2), is universal with respect to the initial continuous PDF φ(v).

A. Statistics of the Total Number of Clusters in the Fan State

We ﬁrst calculate pN (k), the probability that the ﬁnal state contains k distinct clusters. The value of pN (k) is
obtained by summing Eq. (2) over all ni > 0’s and integrating it over ui’s, keeping k ﬁxed. Thus,

pN (k) = ∑

{ni}
 ∫ k∏

i=1 dui δ
 (

N −
 k∑

i=1 ni
) k−1∏

i=1 θ(ui+1 − ui)
 k∏

ℓ=1
 P(nℓ, uℓ)
nℓ . (3)

In this equation, we have used

P(nℓ, uℓ) =
 〈
δ
 

uℓ − 1
nℓ
 Nℓ∑

j=Nℓ−1+1 vj



〉
 = ∫ δ
 

uℓ − 1
nℓ
 Nℓ∑

j=Nℓ−1+1 vj



 Nℓ∏

j=Nℓ−1+1 φ(vj )dvj , (4)

where φ is the distribution of the initial velocities. We note that the function P(n, u) is normalized:

∫ +∞

−∞ duP(n, u) = 1 . (5)

To disentangle the constraints in Eq. (3), it is useful to consider the following generating function:

∑

N pN (k)zN = ∑

{ni}
 zni

ni
 ∫ k∏

i=1 dui
 k−1∏

i=1 θ(ui+1 − ui) P(ni, ui) = ∫ k∏

i=1 dui
 k−1∏

i=1 θ(ui+1 − ui) ρz(ui) (6)

6

with
 ρz(ui) = ∑

{ni}
 zni

ni P(ni, ui) . (7)

The integral on the right hand side (r.h.s) of Eq. (6) can be evaluated recursively and is found to be

∫ +∞

−∞ dukρz(uk) ∫ uk

−∞ duk−1ρz(uk−1) . . . ∫ u2

−∞ du1ρz(u1) = 1
k!
 ( ∫ +∞

−∞ dukρz(uk)
)k = 1
k!
 

∑

{ni}
 zni

ni
 


k
 , (8)

where the last equality is obtained by using the deﬁnition of ρz(u) in (7) and the normalization property in (5). Thus,
for any given value of k > 0, we have
 ∑

N pN (k)zN = 1
k!
 [
− ln(1 − z)
]k . (9)

After extracting the coeﬃcient of zN on the r.h.s of this equation, we conclude that

pN (k) = 1
k!
 ∞∑

{ni>1}
 [ k∏

i=1 ni
]−1
 δ
 (
N −
 k∑

i=1 ni
)
 . (10)

This formula can be expressed in terms of some classical combinatorial numbers as follows. It is convenient to
introduce a second auxiliary variable t and to calculate the generating function of Eq. (9) with respect to t:

∑

k
 ∑

N pN (k)zN tk = ∑

k
 1
k!
 [− ln(1 − z)
]ktk = (1 − z)
−t = 1 + tz + t(t + 1)
2! z2 + t(t + 1)(t + 2)
3! z3 + . . . (11)

Identifying the coeﬃcients of zN on both sides of this equation we obtain the identity:

∑

k pN (k)tk = t(t + 1)(t + 2) . . . (t + N − 1)
N ! . (12)

Using the classical formula
 t(t + 1)(t + 2) . . . (t + N − 1) =
 N∑

k=1 S1(N, k) tk , (13)

that deﬁnes the unsigned Stirling numbers of the ﬁrst kind [20], S1(N, k), we conclude that the probability of ﬁnding
k clusters in the fan state for a system starting with N distinct unit-mass particles is given by

pN (k) = = S1(N, k)
N ! , with k = 1, 2, . . . , N . (14)

We thus recover by a diﬀerent method the result of Ref. [11].
From Eq. (13), we observe that ∑N
k=1 S1(N, k) = N !. Thus, pN (k), and consequently the joint PDF given by
Eq. (2) are both clearly normalized as it must. Furthermore, using Eq. (12), one deduces that the mean number of
clusters is given by 1 + 1
2 + . . . + 1
N .
In fact, it is well known [20] that the unsigned Stirling numbers S1(N, k) enumerate the number of permutations of
N elements with k disjoint cycles exactly: thus, pN (k) is identical to the probability distribution of number of cycles
in random permutations with uniform measure. Many results have been derived concerning the statistics of random
permutations. For example, it has been shown in the context of permutation cycles [14] that for large N , pN (k) has
a Gaussian form around its mean ⟨k⟩ ∼ ln N , with a variance which is also of order ln N . Therefore, the typical mass
of a cluster is of order N/ ln N . Using this together with the t2/3 asymptotic growth of cluster sizes before the fan
state is reached, the characteristic time to reach this state is estimated to be tc ∼ (N/ ln N )
3/2.
 7

B. Distribution of Clusters Sizes including the Biggest and the Smallest

We now consider a more reﬁned observable. It may be tempting to calculate the cluster size distribution i.e. to
integrate out the velocities from Eq. (2) and determine the marginal PDF pN (k; {ni}). Unfortunately, this marginal
distribution is not universal: it depends on the choice of the initial PDF φ(v) (this fact can be veriﬁed by working
out explicit examples). However, if one considers the statistics of the clusters according to their sizes regardless of
their spatial ordering then the result is again φ(v)-independent.
More precisely, let cj for j = 1, 2, . . . , N denote the number of clusters of size j in the fan state. By mass
conservation, we have ∑
j jcj = N . Then, it can be shown that the joint probability, Pr{c1, c2, . . . , cN } is given by

Pr{c1, c2, . . . , cN } = δ(
N −
 N∑

j=1 jcj) N∏

j=1
 1
jcj cj! . (15)

The derivation of this formula from the invariant measure in the fan state, Eq. (2), is given in the Appendix A. This
expression is identical to the distribution of cycles in random permutations where cj’s are to be identiﬁed with the
number of cycles of length j [20].
The generating function associated with this probability distribution is deﬁned as follows:

GN (t1, . . . , tN ) = ∑

c1,...,cN Pr{c1, c2, . . . , cN }tc1
1 . . . tcN
N . (16)

This function GN can itself be embeded in a ’grand-canonical’ generating function given by

Γ(z, {tk}) = ∑

N GN (t1, . . . , tN )zN = exp ( ∞∑

k=1
 zktk
k
 ) , (17)

where the last equality is obtained by using Eq. (15). This expression embodies all the necessary information and will
be useful for further calculations.
For example, we can study the extreme cluster sizes. Let QN (L) be the probability that the largest cluster size
(mass) nmax ≤ L and RN (S) the probability that the smallest cluster size nmin ≥ S. It follows from these deﬁnitions
that the probability that the largest cluster is of size L is given by

Pr (nmax = L) = QN (L) − QN (L − 1) , (18)

and similarly
 Pr (nmin = S) = RN (S) − QN (S + 1) . (19)

Using Eq. (15) we ﬁnd

QN (L) = ∑

c1,...,cL Pr{c1, c2, . . . , cL, 0, . . . , 0} = GN (t1 = 1, . . . , tL = 1, 0, . . . , 0) , (20)

and similarly
 RN (S) = ∑

cS,...,cN Pr{0, . . . , 0, cS, . . . , cN } = GN (0, . . . , 0, tS = 1, . . . , tN = 1) . (21)

Using the grand-canonical generating function deﬁned in Eq. (17), we readily obtain

QL(z) = ∑

N QN (L)zN = exp
 ( L∑

n=1
 zn

n
 )
 and RL(z) ∑

N RN (S)zN = exp
 ( ∞∑

n=S
 zn

n
 )
 . (22)

The mean sizes of the largest and the smallest clusters in the fan state containing N particles are given by

⟨nmax⟩N = ∑

L L[QN (L) − QN (L − 1)] = ∑

L [1 − QN (L)] (23)

and ⟨nmin⟩N = ∑

S S[RN (S) − RN (S + 1)] = ∑

S RN (S) . (24)

8

For large N , the asymptotic behaviour of ⟨nmax⟩N and ⟨nmin⟩N can be obtained by analyzing the associated generating
functions in the z → 1 limit. For example, using Eqs. (22) we obtain

∑

N ⟨nmax⟩N zN = ∑

L
 { 1
1 − z − exp
 ( L∑

n=1
 zn

n
 ) } = 1
1 − z
 ∑

L
 {
1 − exp
 (

−
 ∞∑

n=L+1
 zn

n
 ) } . (25)

When z → 1, the sums on the right-hand sides can be transformed into integrals and the desired asymptotics are
obtained by extracting the leading singularity at z = 1. Thus, for large N , we obtain

⟨nmax⟩ ∼ λN with λ = ∫ ∞

0 exp (
−x − ∫ ∞

x
 e−y

y dy) dx = 0.6243299885 . . . (26)

This constant is known as the Golomb-Dickman Constant [21]. Similarly, We ﬁnd, ⟨nmin⟩ ∼ e−C ln N , where C =
0.57721566 . . . is Euler’s constant, and we again note that, ⟨nmin⟩ and ⟨nmax⟩ are identical to the mean lengths of
the shortest and the longest cycles, respectively, of random permutations and were already calculated in this context
[14, 22]. Recently, the same constants also appeared in the context of the statistics of longest and shortest lasting
records of independent and identically distributed random variables [23, 24]

IV. LEADER STATISTICS

In this section we compute the statistics of the size and the velocity of the ‘rightmost cluster’ in the fan state.
This rightmost cluster will be referred to as the ‘leader’ since it moves with the highest velocity. Let LN (n, v) denote
the joint PDF of the leader’s size n and velocity v in the fan state. To obtain this PDF, we start from the basic
microscopic joint PDF of all cluster sizes and their velocities in Eq. (2) and integrate out the sizes and velocities of
all clusters except the leader. As usual, it is convenient to consider the generating function which then reads

∑

N LN (n, v) zN = zn

n P(n, v)
 ∞∑

k=1
 ∫ [k−1∏

i=1 duiρz(ui)

]
 θ(v − uk−1)
 [
k−2∏

i=1 θ(ui+1 − ui)

]
 (27)

where ρz(u) and P(n, v) are deﬁned respectively in Eqs. (7) and (4). The (k − 1)-fold integral over the ui’s can be
recursively evaluated as in Eq. (8) and we get

∫ [k−1∏

i=1 duiρz(ui)

]
 θ(v − uk−1)
 [k−2∏

i=1 θ(ui+1 − ui)

]
 = 1
(k − 1)!
 ( ∫ v

−∞ ρz(u)du)k−1. (28)

Substituting this in Eq. (27) and summing over k we get a somewhat compact expression

∑

N LN (n, v) zN = zn

n P(n, v) exp [∫ v

−∞ ρz(u)du] . (29)

For the subsequent asymptotic analysis, it turns out to be convenient to rewrite the expression in Eq. (29) in a slightly
diﬀerent form. Using the deﬁnition of ρz(u) from Eq. (7) and the normalization in Eq. (5), it follows that

∫ v

−∞ ρz(u)du =
 ∞∑

k=1
 zk

k
 [1 − ∫ ∞

v P(k, u) du] = − ln(1 − z) − ∫ ∞

v ρz(u)du. (30)

Using this in Eq. (29) gives
 ∑

N LN (n, v) zN = zn

n(1 − z) P(n, v) exp [− ∫ ∞

v ρz(u)du] . (31)

From the joint PDF LN (n, v) of the leader’s size and velocity in Eq. (31) one can then obtain the marginals:
CN (n) = ∫ ∞
−∞ LN (n, v)dv for the size PDF and DN (v) = ∑∞
n=1 LN (n, v) for the velocity PDF of the leader. It is
evident from Eq. (31) that LN (n, v), for any ﬁnite N , depends explicitly on the initial velocity distribution φ(v)
since both P(n, v) as well as ρz(u) depends on φ(v). This is unlike the distribution of the cluster sizes as derived
in Section III which is completely universal, i.e., independent of φ(v) for any ﬁnite N . So, a natural question is: to

9

what extent the leader size and velocity distributions are universal, i.e., independent of the details of φ(v)? We will
see below that the universal property holds for the leader’s size distribution, but only in the large N limit and for
continuous and symmetric φ(v) with a ﬁnite variance σ2 = ∫ ∞
−∞ v2φ(v)dv. In that case, for large N , one can use
the central limit theorem and the limiting marginal size distribution CN (n) essentially becomes universal, though the
marginal velocity distribution DN (v) still remains nonuniversal even in the large N limit. A natural question is how
these results get modiﬁed when φ(v) is such that its variance σ2 is inﬁnite. A particular example of this class is the
Cauchy distribution for φ(v). We will show that the Cauchy case is exactly solvable and one can derive the size and
the velocity distribution of the leader explicitly. In subsections A and B below, we consider, for ﬁnite σ2, the limiting
size and the velocity distribution of the leader respectively. In subsection C, we derive the explicit distributions for
the Cauchy case.
 A. The Limiting Leader Size Distribution

In this subsection we compute the limiting size distribution CN (n) of the leader for large N . Integrating Eq. (31)
over v and writing z = e−s we get

∑

N Cn(n)e−sN = e−sn

n(1 − e−s)
 ∫ ∞

−∞ dvP(n, v) exp[−Y (s, v)] (32)

where
 Y (s, v) =
 ∞∑

k=1
 e−sk

k
 ∫ ∞

v du P(k, u) (33)

with P(k, u) deﬁned in Eq. (4). Now, for large N , we need to investigate the behavior of the r.h.s of Eq. (32) in the
limit s → 0. It is evident that to obtain a sensible limit of the r.h.s in Eq. (32) one needs to consider the scaling
limit s → 0 but n → ∞ keeping the product sn ﬁnite. In this scaling limit, it is not diﬃcult to see that the dominant
contribution to the sum Y (s, v) in Eq. (33) comes from those terms where the product sk is ﬁnite in the limit s → 0,
i.e., terms where k ∼ 1/s is large.
Now, for large k, it follows from the deﬁnition in Eq. (4) that for a symmetric φ(v) with zero mean and a ﬁnite
variance σ2 = ∫ ∞
−∞ v2φ(v)dv is ﬁnite, one can invoke the central limit theorem to assert that P(k, u) has a Gaussian
distribution, i.e.,
 P(k, u) ≈
 √ k
2πσ2 exp [
− ku2

2σ2
 ] . (34)

Substituting this result in Eq. (33) and replacing the resulting sum by an integral in the small s limit, we ﬁnd that
an appropriate scaling limit of Y (s, v) exists when s → 0, v → 0 keeping the ratio v/√
s ﬁxed. In this scaling limit,
we get
 Y (s, v) ≈ 1
2
 ∫ ∞

s
 dy
y e−y erfc ( v√
y

σ√2s
 ) (35)

The integral on the r.h.s of Eq. (35) can be done explicitly and one gets to leading order in small s

Y (s, v) ≈ − 1
2 (C + ln(s)) − ln [w + √
w2 + 1] (36)

where C = 0.57721566 . . . is the Euler’s constant and w = v
σ√2s is the scaling variable. Finally we substitute this
expression for Y (s, v) and the limiting Gaussian form of P(n, v) from Eq. (34) onto the r.h.s of Eq. (32), perform the
subsequent integration and ﬁnally arrive at the following expression in the scaling limit s → 0, n → ∞ but keeping
the product ns ﬁxed ∑

N Cn(n)e−sN ≈ 1
√n G(n s) (37)

where the scaling function G(x) is given by

G(x) = 2b
√
π e−x
√
x
 ∫ ∞

0 dy e−y2 √

1 + y2

x (38)

10

and
 b = eC/2 = 1.33456 . . . . (39)

We notice one remarkable fact: even though we needed to have σ2 ﬁnite in arriving at the result in Eq. (38), σ2 has
dropped out of the ﬁnal expression in Eq. (38). Thus for any ﬁnite σ2, the scaling function G(x) is universal and is
actually independent of the value of σ2.
From the expression in Eq. (38) it is easy to compute the moments of the leader size distribution for large N . For
example, to compute the k-th moment ⟨nk⟩N for large N , we multiply both sides of Eq. (38) by nk and sum over all
n. This gives,
 ∑

N ⟨nk⟩N e−sN ≈ 2b
√
π√
s
 ∑

n e−sn nk−1 ∫ ∞

0 dy e−y2 √
1 + y2/ns. (40)

We next make a change of variable y = √
sn u in the integral and carry out the sum over n. In the scaling limit, this
sum can be replaced by an integral which can be explicitly performed and we get for small s

∑

N ⟨nk⟩N e−sN ≈ 2bΓ(k + 1/2)
√
πsk+1/2
 ∫ ∞

0
 du
(1 + u2)k = b Γ(k − 1/2)Γ(k + 1/2)
Γ(k) s−(k+1/2). (41)

Note that this expression is strictly valid for k ≥ 1. For k = 0, one can show independently that ∑N CN (n)e−sN → 1/s
as s → 0 as expected since the PDF CN (n) is normalized to unity. Inverting the Laplace transform in Eq. (41),it
then follows that for large N , the k-th moment of the leader size behaves for k ≥ 1,

⟨nk⟩N ≈ Ak N k−1/2; where Ak = b Γ(k − 1/2)
Γ(k) . (42)

In particular the average leader size (k = 1) behaves for large N as

⟨n⟩N ≈ b √
π N 1/2 = (2.63533 . . .) N 1/2 (43)

From the expression for the moments in Eq. (41), it follows that for large N , the leader size distribution CN (n)
has the following scaling form
 CN (n) ≈ 1
N 3/2 W ( n
N
 ) (44)

where the scaling function W (x), for 0 ≤ x ≤ 1 is such that, for all k ≥ 1,
∫ 1

0 W (x) x
k dx = b Γ(k − 1/2)
Γ(k) (45)

Finally, one can analytically continue the Eq. (45) for noninteger k and then invert the equation to obtain the
following explicit expression of W (x) valid for 0 ≪ x ≤ 1

W (x) = b
√
π x
−3/2(1 − x)
−1/2 (46)

It is easy to verify that for all k ≥ 1, the above expression for W (x) does indeed satisfy Eq. (45). Note that the scaling
in Eq. (44) is valid only for 1 ≪ n ∼ N . In particular it does not hold when n ∼ O(1). This is also evident from the
explicit form of the scaling function W (x) in Eq. (46) which diverges as x
−3/2 as x → 0, making it non-normalizable.
Indeed, for small n, one has to keep the full expression of the generating function to recover the correct normalization.
Thus the main result of this subsection is the universal scaling form of the leader size distribution in Eqs. (44),
(45) and (46) valid for any continuous and symmetric φ(v) with a ﬁnite σ2 and remarkably it is independent of the
actual value of the σ2.
 B. The Limiting Leader Velocity Distribution

The marginal velocity PDF of the leader DN (v) can be obtained by summing Eq. (31) over n. This gives

∞∑

N =1 DN (v) zN = 1
1 − z ρz(v) exp [− ∫ ∞

v ρz(u)du] . (47)

11

A somewhat more convenient quantity is the cumulative velocity distribution of the leader, FN (v) = ∫ v
−∞ DN (v′) dv′.
One can easily derive its generating function by integrating Eq. (47)

∞∑

N =1 FN (v) zN = exp [
− ∫ ∞
v ρz(u)du] − (1 − z)
1 − z . (48)

Note that as v → ∞, the r.h.s of Eq. (48) becomes z/(1 − z). This is consistent with the l.h.s of Eq. (48) since
FN (v) → 1 as v → ∞ and thus the generating function in that limit is precisely z/(1 − z).
The result for the cumulative velocity distribution of the leader in Eq. (48) is exact for all N . We next address the
question of the limiting leader velocity distribution as N → ∞. For large N , one needs to investigate the r.h.s of Eq.
(48) in the limit z → 1. In that limit, the r.h.s scales as exp [− ∫ ∞
v ρ1(u)du] /(1 − z), provided the numerator is ﬁnite.
In such cases, it follows from Eq. (48) that FN (v) tends to a limiting N -independent distribution F∞(v) given by

F∞(v) = exp [− ∫ ∞

v ρ1(u) du] = exp
 [
−
 ∞∑

n=1
 1
n
 ∫ ∞

v P(n, u) du
]
 . (49)

Note that for some φ(v) this limiting distribution may not exist. In fact, we will see later that when φ(v) has the
Cauchy distribution, which is symmetric and continuous, there is no N -independent limiting distribution. It is evident
from Eq. (49) that, unlike the limiting leader size distribution, the limiting leader velocity distribution, whenever it
exists, is highly nonuniversal and depends explicitly on the initial velocity distribution φ(v).
To see how this limiting distribution in Eq. (49) looks like, we ﬁrst consider the Gaussian distribution, φ(v) =

exp(−v2/2σ2)/√
2πσ2. In this case, P(n, u) = √ n
2πσ2 exp [
− nu
2
2σ2 ] exactly for all u. Substituting on the r.h.s of Eq.
(49) and performing the integral one can express the limiting distribution F∞(v) as a function of the dimensionless
variable v/σ,
 F∞(v) = F (v/σ); where F (z) = exp
 [
− 1
2
 ∞∑

n=1
 1
n erfc (√ n
2 z)]
 . (50)

While we were unable to perform the sum exactly in Eq. (50), the function F (z) can be easily plotted using Mathe-
matica and is shown in Fig. (4). It is easy to show from Eq. (50) that the function F (z) has ﬁnite nonzero support
only for positive z. It is identically zero for all z ≤ 0. Furthermore, the asymptotics of F (z) as z → 0 and z → ∞
can also be derived. We ﬁnd
 F (z) ≈ √
2 z as z → 0 (51)

≈ 1 − 1
√
2π z e−z2/2 as z → ∞. (52)

The asymptotic behavior as z → ∞ is easy to derive, as in this limit the dominant contribution comes from the n = 1
term of the sum in Eq. (50). In contrast, the other limit z → 0 in Eq. (51) is more tricky to derive. We provide a
derivation in Appendix-B.
Let us make a couple of interesting observations on the general formula for the limiting velocity distribution in Eq.
(49) when it exists.

(i) For any continuous and symmetric initial velocity distribution φ(v) for which the limiting velocity distribution
F∞(v) exists, F∞(v) = 0 for any v ≤ 0. This follows from the fact for v = 0, by symmetry, ∫ ∞
0 P(n, u) du = 1/2.
Thus, the sum in Eq. (49) diverges for v = 0 and F∞(0) = 0. Since F∞(v) is a cumulative distribution, it is a
nondecreasing function of v. Hence it follows that if F∞(v = 0) = 0 then F∞(v) = 0 for all v ≤ 0. The implication of
this result is rather interesting. It implies that even though initial velocity distribution may be symmetric in v and
there may be a lot of particles initially with a negative velocity, the eventual velocity of the leader, i.e., the rightmost
cluster is always positive.

(ii) Note that the velocity of the leader is also the maximum of the ﬁnal velocities. Now if the collisions were elastic,
the particles would have merely interchanged the velocities in each collision (this is called the Jepsen gas), and in the
ﬁnal state the velocity of the leader would have been the maximum of all the initial velocities [26]. Therefore, in this
case the distribution of the leader velocity would have been given by the usual extreme value statistics of uncorrelated
random variables [27]. The velocity of the ﬁnal leader of elastic Jepsen gas scales as u ≈ aN w + bN for large N ,
and the limiting distribution of the scaled velocity w has only three possible forms depending on the tail of φ(v) [26].
However, the scaling parameters aN and bN depends on N as well as on the complete form of φ(v). For example,

12

−2 0 2 4
z=v/σ

0

0.2

0.4

0.6

0.8

1F(z)
FIG. 4: (Color online). The limiting cumulative velocity distribution F∞(v) = F (z = v/σ) plotted against z, for the Gaussian
distribution φ(v) = exp(−v2/2σ2)/
√2πσ2.

when φ(v) is Gaussian, aN = (2 ln N )
−1/2 and bN = (2 ln N )
1/2 − (2 ln N )
−1/2(ln ln N + ln 4π)/2. The limiting velocity
distribution is Gumbel in this case. Thus, unlike the elastic gas where the leader velocity increases with N , it follows
from Eq. (49) (when the limiting distribution exists) that in the sticky gas, the leader velocity remains of O(1) in the
large N limit. This is due to the strong correlations generated between the velocities of diﬀerent clusters in the fan
state. Thus Eq. (49) provides an exactly solvable case of extreme value statistics of correlated random variables.

C. Exact Leader Statistics for the Cauchy Distribution

In this subsection, we consider the special case of the symmetric Cauchy distribution for the initial velocity,

φ(v) = 1
π a
v2 + a2 . (53)

For this distribution, the mean is zero, but the second moment σ2 diverges. So, the results of the previous two
subsections, where it was assumed σ2 is ﬁnite, do not hold. However, the principal result in Eq. (31) is still valid and
we show here that the Cauchy distribution preents an excatly solvable case in the sense that the r.h.s of Eq. (31) can
be exactly evaluated in closed form.
The ﬁrst simpliﬁcation occurs when one calculates P(n, u) deﬁned in Eq. (4). Since the Cauchy distribution is
stable, it turns out (as can be easily proved) that

P(n, u) = φ(u) = 1
π a
u2 + a2 . (54)

Thus P(n, u) is completely independent of n. This particular feature of the Cauchy distribution was also used recently
to obtain excat results for the statistics of records in a sequence of random walk in presence of a drift [25]. Using this
independence on n, it then follows from the deﬁnition in Eq. (7) that

ρz(u) = − 1
π a
u2 + a2 ln(1 − z). (55)

One can then trivially do the integral
∫ ∞

v ρz(u) du = − [ 1
2 − 1
π arctan(v/a)
] ln(1 − z). (56)

13

Substituting these results in Eq. (31) gives the following exact expression

∞∑

N =1 LN (n, v) zN = 1
π a
v2 + a2 zn

n (1 − z)
−µ(v) where µ(v) = 1
2 + 1
π arctan(v/a). (57)

Comparing coeﬃcient of zN gives us the exact joint distribution of size and the velocity of the leader

LN (n, v) = 1
π a
v2 + a2 Γ(µ(v) + N − n)
n Γ(N − n + 1) Γ(µ(v)) . (58)

Marginal size distribution: To compute the marginal size distribution CN (n) = ∫ ∞
∞ LN (n, v) dv of the leader, it
is convenient to do the integration over v in Eq. (57). This gives the exact generating function

∞∑

N =1 CN (n) zN = − zn+1

n (1 − z) ln(1 − z) . (59)

From this generating function, it is easy to calculate the moments ⟨nk⟩N of the leader size for large N by investing
the singularity of the r.h.s in Eq. (59) near z = 1. Skipping the details, we ﬁnd that for large N and for k ≥ 1

⟨nk⟩N ≈ 1
k N k

ln(N ) . (60)

This result should be compared to the case in Eq. (42) where σ2 is ﬁnite. In particular, the average leader size grows
as ⟨n⟩N ≈ N/ln N , much faster than the N 1/2 growth for the case where σ2 is ﬁnite.

Marginal velocity distribution: Similarly, the marginal velocity PDF of the leader DN (v) = ∑n LN (n, v) can be
computed conveniently directly from Eq. (57). We get

∞∑

N =1 DN (v) zN = 1
π a
v2 + a2 [− ln(1 − z)] (1 − z)
−µ(v), (61)

from which one can compute the generating function for the cumulative velocity distribution FN (v) = ∫ v
−∞ DN (v′) dv′.
We get a nice compact expression
 ∞∑

N =1 FN (v) zN = (1 − z)
−µ(v) − 1. (62)

Comparing powers of zN gives a very simple but nontrivial distribution valid for all N ≥ 1

FN (v) = Γ(µ(v) + N )
Γ(N + 1) ; where µ(v) = 1
2 + 1
π arctan(v/a). (63)

Note that when v → ∞, µ(v) → 1 and when v → −∞, µ(v) → 0. Thus, in the limit v → ∞, FN (v) → 1 and
when v → −∞, FN (v) → 0 as expected. Also, for N = 1, we get F1(v) = µ(v) which is just the cumulative Cauchy
distribution. This is expected, because the velocity of a single particle remains unchanged as there is no collision.
We note from this exact velocity distribution in Eq. (63) that the distribution is N -dependent explicitly and does
not have any nontrivial N -independent limiting form as N → ∞, unlike in the previous subsection for the Gaussian
case. In fact, by ananlysing the singularity near z = 1 in Eq. (62), we see that for any ﬁxed v, as N → ∞, FN (v)
decays with N as a power law with an exponent that depends continuously on v

FN (v) ≈ 1
Γ(µ(v)) 1
N 1−µ(v) . (64)

Since the exponent 1 − µ(v) = 1/2 − arctan(v/a)/π decreases monotonically from 1 (as v → −∞) to zero (as v → ∞),
it follows that the distribution for smaller values of v tends to zero faster than the distribution for higher v. Thus the
marginal leader velocity distribution in the Cauchy case is very diﬀerent from that of its Gaussian counterpart.
 14

V. DISTRIBUTION OF THE TOTAL ENERGY IN THE FAN STATE

In this section we compute the distribution of the total energy of the clusters in the fan state. For simplicity, we
restrict ourselves to the initial Gaussian distribution of the velocities, φ(v) = exp(−v2/2)/√
2π where we have also
set σ2 = 1 without any loss of generality. Thus, initially, the total (kinetic) energy of the system, E0 = ∑N
i=1 v2
i /2, is
distributed according to the PDF
 PN (E0) = EN/2−1
0 e−E0

Γ(N/2) . (65)

Now, as the system evolves, it dissipates energy through collisions, and once the fan state is reached there is no more
energy loss. It is natural to ask how the PDF of the energy evolves with time from its initial form in Eq. (65), and
in particular how does this energy PDF look like in the ﬁnal fan state beyond which there is no more dissipation.
Let QN (E) denote the PDF of the total energy in the fan state, i.e.,

QN (E) =
 〈
δ
 (
E − 1
2
 k∑

i=1 ni u2
i
 )〉
 , (66)

where the angle brackets ⟨· · · ⟩ denote the average over the random variables k, {ni} and {ui}, whose joint PDF is
given by Eq. (2). It is convenient to consider the Laplace transform of the energy in Eq. (66)

∫ ∞

0 QN (E) e−αE dE =
 〈

exp
 [
− α
2
 k∑

i=1 ni u2
i
 ]〉
 . (67)

To evaulate this average using the measure in Eq. (2), we need to ﬁrst evaluate P(n, u) in Eq. (4). For Gaussian
φ(v), this is simple: P(n, u) = √ n
2π exp [
− n u
2
2 ] exactly for all n and u. We substitute this in the measure in

Eq. (2) and note that calculating the average in Eq. (67) just amounts to renormalizing the eﬀective P(n, u) →
√ n
2π exp [−(1 + α) n u
2
2 ]
. With this input, one can then carry out exactly the same procedure as in subsection III A
and one arrives at the ﬁnal result

∫ ∞

0 QN (E) e−αE dE =
 N∑

k=1(1 + α)
−k/2 [ S1(N, k)
N !
 ]

, (68)

where we recall S1(N, k)/N ! from Eq. (14). The inverse Laplace transform yields

QN (E) =
 N∑

k=1
[ Ek/2−1 e−E

Γ(k/2)
 ]
 ·
 [ S1(N, k)
N !
 ]
. (69)

Since in the ﬁnal state the number of clusters k is distributed according to pN (k) = S1(N, k)/N !, it is interesting to
note that, for a given number k of ﬁnal clusters, the distribution of the total energy is identical to that of k initial
particles.
Equation (69) provides an exact expression for QN (E), for all values of E and N . However, it is always desirable
to have an closed-form expression, even though its validity would require taking the limit of large N . To achieve this
goal, we ﬁrst express Eq. (68) in the following form by using the generating function given in Eq. (13):

∫ ∞

0 QN (E) e−αE dE = 1
N !
 Γ(
N + 1/√
1 + α
)

Γ(1/√
1 + α) . (70)

At this point, we make a short detour to compute the mean and variance of the ﬁnal total energy, as they are
readily available from the ﬁrst and second derivatives of Eq. (70) with respect to α at α = 0. We ﬁnd the mean as

⟨E⟩ = 1
2 HN (71)

15

where HN = ∑N
k=1 k−1 is the harmonic number, and asymptotically, HN ∼ ln N + C where C is the Euler’s constant.
The variance is
 ⟨E2⟩ − ⟨E⟩
2 = 3
4 HN − 1
4 HN,2 (72)

where HN,r = ∑N
k=1 k−r is generalized harmonic number. Note that HN = HN,1. The limiting value of HN,r as
N → ∞ is the Riemann zeta function H∞,r = ζ(r), and ζ(2) = π2/6.
We now return to Eq. (70), and proceed along the main course to obtain a closed-form expression of QN (E) for
large N . The inverse Laplace transform of Eq. (70) is formally given by the Bromwich integral

QN (E) = 1
2πi
 ∫ c+i∞

c−i∞ eS(α) dα, (73)

where
 S(α) = ln Γ(
N + 1/√
1 + α ) − ln
(
N !)

− ln Γ(
1/√
1 + α ) + αE. (74)

Now a saddle point approximation of the integral in Eq. (73) yields

QN (E) ≈ eS(α
∗)∕√
2π|S′′(α∗)| , (75)

in which α
∗ is determined implicitly in terms of E and N by the saddle point condition S′(α
∗) = 0. Enforcing this
condition to Eq. (74) gives the saddle point equation for α
∗ as

E = β3

2
 [
ψ(N + β) − ψ(β)
], (76)

where β = 1/√
1 + α∗ and ψ(x) = (d/dx) ln Γ(x) = Γ′(x)/Γ(x) is the digamma Function. As ψ(N + β) ∼ ln N ,
Eq. (76) suggests that when both E and N are large, the natural scaling variable is z = 2E/ ln N . In terms of this
scaling variable, for large N , from Eq. (76) we ﬁnd

β = z1/3 + z1/3

3 ln N ψ(z1/3) + O ( 1
[ln N ]2
 ) . (77)

Now, employing Stirling’s approximation (for large N ) in Eq. (74) and using Eq. (77), in terms of z we have

S(α
∗) = [ 3
2 z1/3 − z
2 − 1] ln N − ln Γ(z1/3) + O ( 1
ln N
 ) . (78)

Similarly, we ﬁnd
 S′′(α
∗) ∼ 3
4 z5/3 ln N. (79)

Therefore, substituting S and S′′ form Eq. (78) and Eq. (79) respectively, in Eq. (75), ﬁnally we obtain

QN
 ( z
2 ln N ) ≈ ( 3π
2 ln N )−1/2 e−h(z) ln N

z5/6 Γ(z1/3) , (80)

where the large deviation function h(z) is given by

h(z) = 1 + z
2 − 3
2 z1/3. (81)

The saddle-point approximation Eq. (80) is indeed a very good for large N , as we demonstrate in Fig. 5 by comparing
with the exact result Eq. (69) for N = 2000.
Near z = 1 we have h(1 + x) = x
2/6 + O(x
3). Therefore, from Eq. (80) we ﬁnd that QN (E) has a Gaussian form
close to the mean ⟨E⟩ ∼ (1/2) ln N , with a variance ⟨E2⟩ − ⟨E⟩
2 ∼ (3/4) ln N ; —we note that by taking the large N
limit in Eq. (71) and Eq. (72) respectively, we independently recover these mean and variance. However, far away
from the mean, the PDF is quite asymmetric as clearly seen in Fig. 5.
 16

0 1 2 3 4 5
 0.0

0.2

0.4

0.6

0.8

1.0

0 1 2 3 4 5
 0.00

0.05

0.10

0.15

0.20

E∕( 1
2 ln N)QN(E)
zh(z)
FIG. 5: (Color online). Main: Distribution of the total energy for N = 2000. The solid (red) line plots the saddle-point
approximation Eq. (80), and the dashed (blue) line plots the exact form Eq. (69), evaluated using Mathematica. Inset:
The solid (red) line plots the large deviation function Eq. (81), and the dashed (blue) line plots −(ln N )−1 ln QN ` z
2 ln N ´ −
(ln N )−1 lnˆ( 3π
2 ln N )1/2z5/6 Γ(z1/3)˜ as a function of z, using the exact form of QN (E) given in Eq. (69).

VI. SUMMARY AND CONCLUSION

In summary, we have studied analytically various statistical properties in the ﬁnal fan state of a one dimensional
sticky gas of N particles. The particles are initially distributed randomly in space, each with unit mass and with an
initial velocity drawn independently from an identical distribution φ(v). Each particle moves ballistically and when
two particles collide, they form a single cluster with the total mass and total momentum conserved in the collision
process. In the long time limit, the system reaches a fan state where the system consists of a ﬁnite number of clusters
with their velocities increasing from left to right and there is no further collision. We have shown that the sizes and the
number of clusters are distributed universally in the fan state, independent of φ(v) and this distribution is identical
to that of the cycles lengths in random permutation problem. We have also computed exactly the distribution of the
size and the velocity of the rightmost cluster (leader) moving with the largest velocity. Furthermore, the distribution
of the total energy in the fan state is also computed exactly for Gaussian φ(v). Our results provide an exactly solvable
case of a many-body system (of ﬁnite size N ) with dissipative dynamics and in particular, brings out the universal
features of the ﬁnal stationary state in an explicit way.
There are interesting open issues for further research. Here we have focused solely on the ﬁnal fan state. It would
be interesting to study the dynamics, i.e., the approach to this fan state and investigate to what extent the universal
features exist away from the fan state.
There are also immediate generalizations of the problem studied here that are open for future research. For example,
it would be interesting to know to what extent the universal features in the fan state remain valid for an inhomogeneous
sticky gas. The inhomogeneity can arise either from unequal initial masses or nonidentical velocity distributions in
the initial condition. For an inﬁnite system, i.e., with a ﬁnite density of initial particles, the ballistic aggregation
model with inhomogeneous initial condition has been studied [28]. It would be interesting to extend this study to the
case of a ﬁnite number N of particles.
Finally, it would be interesting to study this ﬁnite system of N particles when the collisions are inelastic, but not
necessarily sticky, i.e., with a nonzero coeﬃcient of restitution. This problem has been studied for an inﬁnite system
and many asymptotic properties such as the energy decay and the velocity distribution were found to be similar to
the sticky gas limit [29, 30]. It would be interesting to see to what extent the universal features in the stationary
state for ﬁnite N are retained when one introduces a nonzero coeﬃcient of restitution.

Acknowledgements: We thank D. Dhar for many stimulating discussions and for his early participation in this

17

work. We acknowledge useful discussions with A. Comtet, P. L. Krapivsky and Y. Peres. The support from grant
no. 3404-2 of “Indo-French Center for the Promotion of Advanced Research (IFCPAR/CEFIPRA)” is also gratefully
acknowledged.
 APPENDIX A: PROOF OF EQUATION (15)

In this Appendix, we derive the distribution of the cluster sizes (regardless of their positions) starting from joint
probability distribution of the cluster sizes and velocities given in Eq. (2). To calculate Pr{c1, c2, . . . , cN } from the
joint-PDF pN (k; {ni, ui}), we must: (i) integrate out the velocities, (ii) sum over all conﬁgurations with the same
cluster sizes (but placed in diﬀerent orders) (iii) change the variables from the list (n1, , . . . , nk) that represents the
sizes of the k consecutive clusters to the set {c1, . . . , cN } that encodes the number of clusters of a given size. We thus
have
 Pr{c1, c2, . . . , cN } = ∑

Permutations of
unequal size clusters
 pN (n1, . . . , nk) , (A1)

where the sum is restricted to permutations that exchange clusters having diﬀerent sizes i.e. permutations of the list
(n1, . . . , nk) that exchange ni’s having diﬀerent values. Using Eq. (3) and the fact that ∏k
i=1 nk = ∏N
j=1 jcj , we ﬁnd
that pN (n1, . . . , nk) is given by

pN (n1, . . . , nk) = δ (N − ∑N
j=1 jcj)

∏N
j=1 jcj
 ∫ k∏

ℓ=1 duℓ P(nℓ, uℓ)
 k−1∏

ℓ=1 θ(uℓ+1 − uℓ) . (A2)

From the deﬁnition of P(nℓ, uℓ) given in Eq. (4), the integral on the r.h.s of Eq. (A2) is found to be

∫ N∏

i=1 dvi φ(vi)
 k−1∏

ℓ=1 θ
 

 1
nℓ+1
 Nℓ+1∑

j=Nℓ+1 vj − 1
nℓ
 Nℓ∑

j=Nℓ−1+1 vj


 (A3)

where Nℓ = n1 + . . . + nℓ for ℓ = 1, . . . , k. The proof of Eq. (15) hence reduces to showing the following identity:

∑

Permutations of
unequal clusters
 ∫ N∏

i=1 dvi φ(vi)
 k−1∏

ℓ=1 θ
 

 1
nℓ+1
 Nℓ+1∑

j=Nℓ+1 vj − 1
nℓ
 Nℓ∑

j=Nℓ−1+1 vj


 = 1
c1! c2! . . . cN ! , (A4)

where we recall that c1 is equal to the total number of 1’s in the list (n1, . . . , nk), c2 is equal to the total number of
2’s in this list etc... This identity is proved by the following argument: consider a permutation that exchanges two
clusters of the same size p; then, by relabeling the vi (which are dummy variables) we observe that the integral on the
left hand side (l.h.s) of Eq. (A4) is invariant. There are cp! possible permutations of the cp clusters of size p. Thus
we have formally
 c1! c2! . . . cN ! ∑

Permutations of
unequal clusters
 = ∑

All Permutations . (A5)

If we have k distinct numbers u1 . . . uk there is only one permutation that orders them in increasing order. Therefore,
we have
 ∑

σ∈Σk
 k−1∏

ℓ=1 θ(uσ(ℓ+1) − uσ(ℓ)) = 1 , (A6)

where Σk is the symmetric group of k elements. After substituting this identity in Eq. (A5) and using the fact that
the PDF φ(vi) is normalized, Eq. (A4) is ﬁnally proved. We note that the method of proof used here is closely related
to the derivation by F. Spitzer of a generalization of the Sparre-Andersen theorem [15].
 18

APPENDIX B: LIMITING BEHAVIOR OF F (z) AS z → 0 IN EQ. (50)

Let us write F (z) in Eq. (50) as F (z) = exp[−S(z)] where the sum

S(z) =
 ∞∑

n=1
 1
2n erfc (√ n
2 z) . (B1)

We want to compute the behavior of S(z) as z → 0. We ﬁrst note the identity

∞∑

n=1
 1
2n exp(−n z2/2) = − 1
2 ln [1 − e−z2/2] . (B2)

Subtracting Eq. (B2) from Eq. (B1) gives

S(z) + 1
2 ln [1 − e−z2/2] =
 ∞∑

n=1
 1
2n
 [
erfc (√ n
2 z) − e−n z2/2] . (B3)

Now, let us deﬁne a new variable y = n z2/2. As n changes by 1, y changes by ∆y = z2/2. Now, in the limit z → 0,
this increment ∆y is very small. Thus, one can replace the sum over n on the r.h.s of Eq. (B3) by an integral over y
to leading order for small z, giving

S(z) + 1
2 ln [
1 − e−z2/2] ≈ I = 1
2
 ∫ ∞

0
 dy
y [erfc (
√y) − e−y] . (B4)

The integral I on the r.h.s is just a constant and can be evaluated by parts

I = − 1
2
 [∫ ∞

0 e−y ln(y) dy − 1
√π
 ∫ ∞

0
 ln(y)
√
y e−y dy] . (B5)

The two integrals on the r.h.s are elementary ones and can be easily evaluated to give ﬁnally, I = − ln(2). Substituting
this in Eq. (B3) and taking the z → 0 limit gives

S(z) → − ln(
√2 z), (B6)

implying as z → 0 to leading order
 F (z) = exp[−S(z)] → √
2 z. (B7)

[1] G. F. Carnevale, Y. Pomeau, and W. R. Young, Phys. Rev. Lett. 64, 2913 (1990).
[2] Granular Gases, edited by T. P¨oschel and S. Luding (Springer, Berlin, 2001); Granular Gas Dynamics, edited by T. P¨oschel
and N. Brilliantov (Springer, Berlin, 2003).
[3] S. F. Shandarin and Ya. B. Zeldovich, Rev. Mod. Phys. 61, 185 (1989).
[4] P. A. Martin, J. Piasecki, J. Stat. Phys, 76, 447 (1994); J. Stat. Phys, 84, 837 (1996).
[5] J. M. Burgers, The Nonlinear Diﬀusion Equation (Reidel, Dordrecht,1974).
[6] S. Kida, J. Fluid Mech. 93 part 2, 337 (1979).
[7] U. Frisch and J. Bec, “Burgulence”, in Les Houches 2000: New Trends in Turbulence, M. Lesieur ed., (Springer EDP-
Sciences).
[8] L. Frachebourg, Phys. Rev. Lett. 82, 1502 (1999).
[9] L. Frachebourg, P. A. Martin and J. Piasecki, Physica A 279, 69 (2000).
[10] K. Shida and T. Kawai, Physica A 162, 145 (1989).
[11] M. Sibuya, T. Kawai, and K. Shida, Physica A 167, 676 (1990).
[12] H. Hyuga, T. Kawai, K. Shida and S. Yamada, Physica A 241, 664 (1997).
[13] V. Goncharov, Sur la distribution des cycles dans les permutations, C.R. (Doklady) Acad. Sci. URSS (N.S) 35, 267 (1942).
[14] L.A. Shepp, S.P. Lloyd, Trans. Am. Math. Soc. 121, 340 (1966).
[15] F. Spitzer, Trans. Am. Math. Soc. 82, 323 (1956).
[16] J. M. Steele, J. Comput. Appl. Math. 142, 235 (2002).
 19

[17] E. Trizac and P. L. Krapivsky, Phys. Rev. Lett. 91, 218302 (2003).
[18] W. Feller, An Introduction to Probability Theory and Its Applications (Wiley, New York, 1971), Vol. II, 2nd ed.
[19] R. L. Graham, D. E. Knuth and O. Patashnik, Concrete Mathematics (Addison-Wesley, 2nd ed., 1994).
[20] J. Riordan, Introduction to Combinatorial Analysis (Dover, New York, 2002).
[21] S. R. Finch, Mathematical Constants, (Cambridge University Press, UK, 2003).
[22] R. Arratia, A. D. Barbour and S. Tavare, Notices of the AMS, 44, 903 (1997).
[23] S.N. Majumdar and R.M. Ziﬀ, Phys. Rev. Lett. 101, 050601 (2008).
[24] C. Godreche and J.M. Luck, arXiv: 0809.3377.
[25] P. Le Doussal and K.J. Wiese, arXiv: 0808.3217.
[26] I. Bena and S.N. Majumdar, Phys. Rev. E 75, 051103 (2007); S. Sabhapandit, I. Bena, and S.N. Majumdar, JSTAT
P05012 (2008).
[27] R.A. Fisher and L.H.C. Tippet, Proc. Cambridge Philos. Soc. 24, 180 (1928); E.J. Gumbel, Statistics of Extremes
(Columbia University Press, NY, 1958).
[28] L. Frachebourg, V. Jacquemet, and P. A. Martin, J. Stat. Phys. 105, 745 (2001).
[29] E. Ben-Naim, S.Y. Chen, G.D Doolen, and S. Redner, Phys. Rev. Lett. 83, 4069 (1999).
[30] M. Shinde, D. Das, and R. Rajesh, Phys. Rev. Lett. 99, 234505 (2007).
