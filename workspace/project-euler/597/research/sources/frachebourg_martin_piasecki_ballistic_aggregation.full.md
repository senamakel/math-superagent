<!-- source: https://arxiv.org/pdf/cond-mat/9911346 | converted from PDF -->

arXiv:cond-mat/9911346v1  [cond-mat.stat-mech]  22 Nov 1999
Ballistic aggregation: a solvable model of irreversible many particles dynamics

L. Frachebourg∗ and Ph. A. Martin
Institut de Physique Th´eorique
Ecole Polytechnique F´ed´erale de Lausanne
CH-1015 Lausanne, Switzerland

J. Piasecki
Institute of Theoretical Physics
University of Warsaw
00 681 Warsaw, Poland
(May 11, 2018)

The adhesive dynamics of a one-dimensional aggregating gas of point particles is rigorously de-
scribed. The inﬁnite hierarchy of kinetic equations for the distributions of clusters of nearest neigh-
bours is shown to be equivalent to a system of two coupled equations for a large class of initial
conditions. The solution to these nonlinear equations is found by a direct construction of the rele-
vant probability distributions in the limit of a continuous initial mass distribution. We show that
those limiting distributions are identical to those of the statistics of shocks in the Burgers turbulence.
The analysis relies on a mapping on a Brownian motion problem with parabolic constraints.

I. INTRODUCTION

Rigorous solutions of the many-body dynamics are extremely rare. The present paper yields up such a precious
case, reviewing parts of the existing works and completing the research which has been carried out in recent years.
The system under study is a one-dimensional gas of point particles forming aggregates through perfectly inelastic,
adhesive collisions. The motion between collisions being free, the process is called ballistic aggregation. This dynam-
ics is deterministic, randomness occurs only through the distribution of initial datas. In the context of statistical
mechanics, the model was introduced and studied numerically in [1] and further investigated analytically in [2], [3]
and [4]. However in the context of ﬂuid dynamics, it has been recognized much earlier (see e.g. [5], [6]) that the
evolution of shocks in the inviscid limit of the (decaying) one-dimensional Burgers equation obeys the laws of ballis-
tic aggregation. Moreover when the initial particle velocities are Gaussian and independent (equivalently when the
initial Burgers ﬁeld is a white noise) both models are isomorphic to a problem of Brownian motion under parabolic
constraints. The latter problem has eventually received a solution in closed analytical form [4], [7] which enables to
predict the exact distribution of shocks in the decaying Burgers turbulence, and correspondingly the distribution of
masses and velocities of the aggregating particles. These close connections between problems of diﬀerent origins is
an attractive feature of ballistic aggregation. The purpose of this work is to establish precisely the above mentioned
relations and to give an exact and fairly complete description of ballistic aggregation.
There are essentially two approaches. The ﬁrst one consists in writing the dynamical hierarchy of equations coupling
the many-particle distribution functions using the tools of kinetic theory, and hopefully solving these equations. The
second route is by explicitly constructing the dynamics from suitably chosen initial conditions: the construction should
of course yield a solution of the kinetic equations. Both approaches are discussed here and both will make the link
with the dynamics of Burgers shock waves manifest.
After recalling the way in which one can describe the state of an inﬁnite gas (Section II), we present in Section
III the derivation of the inﬁnite hierarchy of kinetic equations coupling the time evolution of distributions of many-
particle clusters of nearest neighbours. The derived hierarchy, after integration over momenta of the aggregates, turns
out to be identical to the hierarchy found in the study of the Burgers turbulence [6].
In Section IV an original result is derived. The inﬁnite dynamical hierarchy is shown to be compatible with the
factorization of the many-body distributions into products of two-particle conditional distributions and the one-
particle density. Such a factorization is propagated by the ballistic aggregation. This yields an exact closure of the
hierarchy and permits to reduce it to a system of two coupled equations (Section V) which allow self-similar solutions
(Section VI).

∗supported by the Swiss National Foundation for Scientiﬁc Research.

1

The Section VII is devoted to an explicit construction of the particle distributions. The construction, which has
already been presented in [3], uses a simple initial condition which enables to reformulate the problem within the
theory of Brownian motion. To establish the relation with shock wave dynamics at this level, one must envisage the
delicate question of the continuum limit. Indeed the Burgers velocity ﬁeld takes values in the continuum, whereas
masses of aggregates, resulting of sums of elementary initial masses, have discrete values. A strict isomorphism will
only be obtained in the continuum limit of the aggregation process letting the distribution of initial masses tend to
a continuous and uniform mass density. In terms of Brownian motion this leads to the subtle problem of controlling
the cumulated eﬀect of Brownian excursions in inﬁnitely many small time intervals. This problem is addressed and
extensively discussed in Section VIII: in the continuum limit the particle distributions become identical to those of the
shocks in Burgers dynamics so that all the results of [7] immediately apply. All distributions of order three and more
factorize in the way described in Section IV, so giving a complete statistical description of the aggregation process.
In Section IX the exact predictions for the mass and velocity distributions are compared to existing bounds as well as
to the ﬁndings of previously formulated approximate theories. In particular signiﬁcant discrepancies with mean ﬁeld
theory appear in the domains of large and small masses. The asymptotic form of the two-particle correlation function
at large distance displays the range of spatial correlations induced by the aggregation process: one ﬁnds a very rapid
decay of such correlations. In the last section, we brieﬂy indicate by which mechanisms our explicit solution veriﬁes
the closed dynamical equation derived in Section IV (and hence the whole hierarchy), thus completing our analysis
of the model.
 II. STATES OF THE AGGREGATING GAS

At any time t > 0, the system is composed of point particles moving in R1. The state of a given particle is entirely
characterized by specifying its position X, its momentum P , and its mass M .
Consider a closed space interval [L1, L2] , where L1 < L2. We denote by

µk(1, 2, . . . , k; t|L1, L2) (1)

the probability density for ﬁnding precisely k particles within the interval [L1, L2] at time t, occupying the sequence
of states
 j ≡ (Xj, Pj , Mj), j = 1, 2, . . . , k (2)

ordered in space according to the inequalities

L1 < X1 < X2 < . . . < Xk < L2 (3)

The set of densities µk(1, 2, . . . , k; t|L1, L2), k = 0, 1, 2, . . ., deﬁned for arbitrary intervals [L1, L2], provides a complete
statistical description of the state of the inﬁnite volume of the gas. Summing up the probability weights for all possible
events within [L1, L2] one gets the normalization condition

µ0(t|L1, L2) +
 ∞∑

k=1
 ∫ d1 ∫ d2. . . ∫ dk θ(X1 − L1) θ(L2 − Xk)

×
 k∏

j=2 θ(Xj − Xj−1)µk(1, 2, . . . , k; t|L1, L2) = 1 (4)

where ∫ dj ≡ ∫ +∞

−∞ dXj
 ∫ +∞

−∞ dPj
 ∫ +∞

0 dMj , (5)

and θ(X) is the unit Heaviside step function.
Knowing the probability densities µk(1, 2, . . . , k; t|L1, L2) one can evaluate the densities µk(1, 2, . . . , k; t) of the
nearest neighbours conﬁgurations by letting the extremities of the interval [L1, L2] approach the positions of the ﬁrst
and the last particle, respectively

µk(1, 2, . . . , k; t) ≡ lim
L1→X1 lim
L2→Xk µk(1, 2, . . . , k; t|L1, L2) (6)

2

In particular, µ1(1; t) represents simply the number density of particles at time t in the one-particle state 1 ≡
(X1, P1, M1).
An alternative way of describing the state of an inﬁnite system consists in determining the complete set of reduced
distributions ρk(1, 2, . . . , k; t), representing the number density of ordered k-particle states (1, 2, . . . , k). The diﬀerence
with respect to the densities µk(1, 2, . . . , k; t) comes from the fact that the k particles need not represent the set of
nearest neighbours. Although in evaluating ρk(1, 2, . . . , k; t) the inequalities

X1 < X2 < . . . < Xk (7)

are still supposed to hold, one has to consider all conﬁgurations of the system compatible with the condition that the
states (1, 2, . . . , k) are occupied at time t, with an arbitrary number of particles between pairs (j, j+1), j = 1, . . . , k−1.
Clearly, there is then no diﬀerence at the level of the one-particle densities, and, as it has already been mentioned,
the equality
 ρ1(1; t) = µ1(1; t) (8)

holds.
For the two-particle reduced density ρ2(1, 2; t), the corresponding formula reads

ρ2(1, 2; t) = µ2(1, 2; t) +
 ∞∑

r=1
 ∫ d1′ ∫ d2′ . . . ∫ dr′ θ(X ′
1 − X1)θ(X2 − X ′
r)

×
 r−1∏

j=1 θ(X ′
j+1 − X ′
j) µ2+r(1, 1′, 2′, . . . , r′, 2; t) (9)

The possibility of the presence of r particles (r = 0, 1, 2, . . .) between the two particles at X1 and at X2, has been
taken into account in (9). By deﬁnition (6) the density µ2+r(1, 1′, 2′, . . . , r′, 2; t) vanishes outside the region X1 <
X ′
1 < . . . < X ′
r < X2, reﬂecting the linear ordering of the particles.
In a similar way (i.e. by considering all possible intermediate states) one can express ρk(1, 2, . . . , k; t) in terms of the
densities of nearest neighbours µk+r(1, 2, . . . , k + r; t), r = 0, 1, 2, . . ., for arbitrary k = 3, 4, . . .. The general relations
between both types of description of the states of an inﬁnite system are discussed in Ruelle’s book [8].

III. EVOLUTION OF THE DISTRIBUTION OF NEAREST NEIGHBOURS

Our main object here is the study of the dynamics of aggregation. The point masses forming the system move
freely between collisions. When two of them collide, they instantaneously merge forming a new particle whose mass is
equal to the sum of their masses. As the momentum is also conserved, the aggregate continues the motion along the
center of mass trajectory of the pair it has been formed from. Hence, the microscopic dynamics consists of periods of
a free motion separated by perfectly inelastic (sticky or adhesive) binary collisions.
Suppose that at some moment two particles occupy the states a = (Xa, Pa, Ma) and b = (Xb, Pb, Mb), with Xa < Xb.
The notation (a + b) will be used to denote the state corresponding to the center of mass motion of such an ordered
pair. Hence
 (a + b) ≡ ( MaXa + MbXb
Ma + Mb , Pa + Pb, Ma + Mb
) (10)

We shall restrict our analysis to spatially homogeneous systems. The one-particle density does not depend in this
case on the position variable
 µ1(1; t) = µ1(P1, M1; t) (11)

Therefore, the changes of µ1(1; t) in the course of time are exclusively due to collisions. Clearly, in one dimension
only the nearest neighbours can collide. The rate of collisions between adjacent particles j and (j + 1) is proportional
to the density of the nearest neighbours µ2(j, j + 1; t). It can be written as

C(j, j + 1)µ2(j, j + 1; t) (12)

where the collision factor
 3

C(j, j + 1) ≡ ( Pj
Mj − Pj+1
Mj+1
 ) θ ( Pj
Mj − Pj+1
Mj+1
 ) δ(Xj+1 − Xj − 0+) (13)

chooses (with the help of the Dirac δ-distribution) only the precollisional conﬁgurations. As the motion between
collisions is free, the rate (12) is proportional to the relative velocity of the colliding pair (the θ-factor in C(j, j + 1)
assures the mutual approach of the particles).
In order to evaluate the time derivative of the one-particle density (11) let us consider ﬁrst the events which lead
to the creation of the state 1 by adhesive collisions. Their rate of occurrence is given by
∫ d1′ ∫ d2′ C(1′, 2′)δ[1 − (1′ + 2′)]µ(1′, 2′; t) (14)

Here the distribution

δ[1 − (1′ + 2′)] = δ [X1 − M ′
1X ′
1 + M ′
2X ′
2
M ′
1 + M ′
2
 ] δ[P1 − (P ′
1 + P ′
2)]δ[M1 − (M ′
1 + M ′
2)] (15)

picks out only those collisions which create the aggregate in the state 1.
Consider now the events leading to the destruction of state 1. When the precollisional state of one of the particles
is 1, the collision removes this state from the system. The rate of such annihilating events is given by
∫ d1′C(1′, 1)µ2(1′, 1; t) + ∫ d1′C(1, 1′)µ2(1, 1′; t) (16)

Combining the gain term (14) and the loss terms (16), we arrive at the equation

∂
∂t µ1(1; t) = ∫ d1′ ∫ d2′C(1′, 2′)δ[1 − (1′ + 2′)]µ2(1′, 2′; t)

− ∫ d1′C(1′, 1)µ2(1′, 1; t) − ∫ d1′C(1, 1′)µ2(1, 1′; t) (17)

In a similar way one can derive the evolution equation for the two-particle distribution of the nearest neighbours.
It reads [ ∂
∂t + L12 + C(1, 2)
] µ2(1, 2; t) =
∫ d1′ ∫ d2′C(1′, 2′){δ[1 − (1′ + 2′)]µ3(1′, 2′, 2; t) + δ[2 − (1′ + 2′)]µ3(1, 1′, 2′; t)}

− ∫ d1′C(1′, 1)µ3(1′, 1, 2; t) − ∫ d1′C(2, 1′)µ3(1, 2, 1′; t) (18)

where
 L12 = P1
M1
 ∂
∂X1 + P2
M2
 ∂
∂X2 (19)

is the generator of free streaming. On the left hand side there appears the loss term C(1, 2)µ2(1, 2; t) describing the
destroying eﬀect of a possible merging of the pair (1, 2). The right hand side takes into account the processes of
creation of aggregates in the states 1 or 2 (the ﬁrst two terms). Finally, the last two terms represent the destruction
of the two-particle state (1, 2) by collisions with the left nearest neighbour of particle 1, and with the right nearest
neighbour of particle 2, respectively. Equation (18) relates the rate of change of µ2(1, 2; t) to the three-particle density
µ3(1, 2, 3; t).
Denoting by L1...k the k-particle generator of free streaming

L1...k =
 k∑

j=1
 Pj
Mj
 ∂
∂Xj (20)

we write the general k-th equation of the inﬁnite hierarchy (k = 1, 2, . . .) in the form

4



 ∂
∂t + L1...k +
 k−1∑

j=1 C(j, j + 1)



 µk(1, 2, . . . , k; t) =

k∑

j=1
 ∫ d1′ ∫ d2′C(1′, 2′)δ[j − (1′ + 2′)]µk+1(1, . . . , j − 1, 1′, 2′, j + 1, . . . , k; t)

− ∫ d1′C(1′, 1)µk+1(1′, 1, 2, . . . , k; t) − ∫ d1′C(k, 1′)µk+1(1, 2, . . . , k, 1′; t). (21)

The fact that µk(1, . . . , j, j + 1, . . . , k; t) is the density of a sequence of k nearest neighbours imposes a restrictive
condition on its support. Indeed, tracing backward in time the free trajectory of particle j to the moment t = 0, we
ﬁnd the position of the center of mass of the part of the initial system it has been formed from. So, if we denote by
ρ the constant mass density at t = 0, the point

X right
j (−t) = Xj − Pj
Mj t + Mj
2ρ ≡ Xj − Y −
j (22)

has the meaning of the right extremity of the initial mass region which produced the mass Mj through adhesive
collisions. This right extremity must coincide with the left extremity

X left
j+1(−t) = Xj+1 − Pj+1
Mj+1 t − Mj+1
2ρ ≡ Xj+1 − Y +
j+1 (23)

of the region which produced the mass Mj+1. Otherwise, the pair (j, j + 1) would not represent nearest neighbours.
In (22) and (23) we have introduced the notation

Y ±
j = Pj
Mj t ± Mj
2ρ . (24)

We thus conclude that the density µk(1, . . . , k; t) contains necessarily the singular factor

k−1∏

j=1 δ [Xj+1 − Xj − Y +
j+1 + Y −
j ] (25)

This conclusion implies important consequences for collisional conﬁgurations where Xj+1 = Xj +0+. The distribution
(25) imposes then the condition
 Y +
j+1 = Y −
j (26)

Hence, in the hierarchy equations (21) one can replace the collision terms C(j, j + 1) (see (13)) by

Mj + Mj+1
2ρt δ(Xj+1 − Xj − 0+) (27)

With the use of (27), one ﬁnds, after integrating over all momenta, the inﬁnite hierarchy for the distribution of masses
and distances between the particles which has already been derived in the study of the Burgers model of turbulence
[9]. Our independent reasoning based on the microscopic laws of the aggregation process conﬁrms the existence of a
one-to-one correspondence between the two problems.
It is quite remarkable that the inﬁnite set of equations (21) can be rigorously reduced to a system of two coupled
nonlinear equations under a simple assumption, which can be shown to be satisﬁed for a large class of initial conditions.
This important fact, derived in the next section, has not been noticed in [9]. The authors restricted their analysis
therein to the ﬁrst equation of the hierarchy, supplemented with an integral relation obtained by integrating equation
(18) over both momenta and masses. In the search for self-similar solutions, they assumed a speciﬁc form of two-particle
correlations, which eventually led them to an erroneous conclusion that the masses were exponentially distributed
. The exponential distribution has been eighteen years later conjectured again in [1], and shown to follow from
the hierarchy equations (21) within the weak mean-ﬁeld approximation [2]. It turned out that a rigorous analysis
invalidated these approximate results (see [4] and section IX).

5

IV. REDUCTION OF THE HIERARCHY

A fundamental role in further considerations will be played by the conditional probability density

µ(2|1; t) = µ2(1, 2; t)
µ1(1; t) (28)

for ﬁnding the right nearest neighbour of a particle supposed to occupy the state 1, in the state 2 at time t. The
normalization ∫ d2 µ(2|1; t) = 1 (29)

expresses the fact that in a homogeneous system the right nearest neighbour does exist in some state with certainty.
The singular factor
 δ [X2 − X1 − Y +
2 + Y −
1 ] (30)

present in µ2(1, 2; t) (see (25)), and thus also in µ(2|1; t), involves the combination Y −
1 = tP1/M1 − M1/2ρ of mass and
momentum of particle 1. This combination appears in formula (22) for the position of point X right
j (−t), separating
from the right hand side the masses which contributed to the formation of particle j from the rest of the system.
The reduction of the dynamical hierarchy (21) presented in this section is possible if µ(2|1; t) depends on P1 and
M1 exclusively via the eﬀective variable Y −
1 . The following structure of the conditional probability density will be
thus assumed
 µ(2|1; t) = δ [X2 − X1 − Y +
2 + Y −
1 ] ¯µ(M2, P2, Y −
1 ; t) (31)

In fact, it will be shown by construction in Section VII that for a large class of initial conditions the above hypothesis
is veriﬁed.
The presence of factor (25) in µk(1, . . . , k; t) clearly indicates the existence of correlations between the states of the
nearest neighbours. Let us suppose that only two-particle correlations exist, so that

µk(1, 2, . . . , k; t) = µ1(1; t)
 j=k−1∏

j=1 µ(j + 1|j; t) (32)

We shall prove now that the above factorization is compatible with the dynamics of the system, and that the factorized
densities (32) yield a solution to the hierarchy equations (21), provided µ1(1; t) and µ(2|1; t) satisfy the system of
coupled equations

∂
∂t µ1(1; t) = ∫ d1′ ∫ d2′C(1′, 2′)δ[1 − (1′ + 2′)]µ1(1′; t)µ(2′|1′; t)

− ∫ d1′C(1′, 1)µ1(1′; t)µ(1|1′; t) − ∫ d1′C(1, 1′)µ1(1; t)µ(1′|1; t) (33)

[ ∂
∂t + L12 + C(1, 2)
] µ(2|1; t) = ∫ d1′ ∫ d2′C(1′, 2′)δ[2 − (1′ + 2′)]µ(1′|1; t)µ(2′|1′; t)

+ {∫ d1′C(1, 1′)µ(1′|1; t) − ∫ d1′C(2, 1′)µ(1′|2; t)
} µ(2|1; t) (34)

Equation (33) is just the ﬁrst equation of the hierarchy (17) in which µ2(1, 2; t) has been replaced by µ1(1; t)µ(2|1; t).
Let us consider the general equation (21) for k ≥ 2. Upon inserting the factorized form (32) of the densities µk and
µk+1 we get (with the use of the ﬁrst equation (33)) the following relation

µ1(1; t)
 

 ∂
∂t + L1...k +
 k−1∑

j=1 C(j, j + 1)



 k−1∏

r=1 µ(r + 1|r; t) =

6

∫ d1′ ∫ d2′C(1′, 2′)δ[1 − (1′ + 2′)]µ2(1′, 2′; t)[µ(2|2′; t) − µ(2|1; t)]
 j=k−1∏

j=2 µ(j + 1|j; t)

+µ1(1; t)
 k∑

j=2
 ∫ d1′ ∫ d2′C(1′, 2′)δ[j − (1′ + 2′)]
 j−2∏

r=1 µ(r + 1|r; t)

×µ(1′|j − 1; t)µ(2′|1′; t)µ(j + 1|2′; t)
 k−1∏

s=j+1 µ(s + 1|s; t)

+µ1(1; t) [∫ d1′C(1, 1′)µ(1′|1; t) − ∫ d1′C(k, 1′)µ(1′|k; t)
] k−1∏

j=1 µ(j + 1|j; t). (35)

The ﬁrst term on the right hand side vanishes. Indeed, equation (26) implies the equality

− P1
M1 t + M1
2ρ = − P ′
1 + P ′
2
M ′
1 + M ′
2 t + M ′
1 + M ′
2
2ρ = − P ′
2
M ′
2 t + M ′
2
2ρ (36)

So, taking into account the supposed structure (31) of conditional densities, we can replace µ(2|2′; t) in (35) by
µ(2|1; t). Using exactly the same reasoning one can show that in the remaining gain terms in (35), involving the
creation of particles j = 2, 3, . . . , k through aggregation of 1′ and 2′, the density µ(j + 1|2′; t) equals µ(j + 1|j; t). This
permits to rewrite the hierarchy equation (35) in the following form


 ∂
∂t + L1...k +
 k−1∑

j=1 C(j, j + 1)



 k−1∏

j=1 µ(j + 1|j; t) =

k∑

j=2
 ∫ d1′ ∫ d2′C(1′, 2′)δ[j − (1′ + 2′)]
 j−2∏

r=1 µ(r + 1|r; t)µ(1′|j − 1; t)µ(2′|1′; t)
 k−1∏

s=j µ(s + 1|s; t)

+ [∫ d1′C(1, 1′)µ(1′|1; t) − ∫ d1′C(k, 1′)µ(1′|k; t)
] k−1∏

j=1 µ(j + 1|j; t) (37)

The last term in (37) can be conveniently rewritten as

k∑

j=2
 [∫ d1′C(j − 1, 1′)µ(1′|j − 1; t) − ∫ d1′C(j, 1′)µ(1′|j; t)
] k−1∏

r=1 µ(r + 1|r; t) (38)

A straightforward calculation shows then that equation (35) is satisﬁed (for any k ≥ 1) if the conditional probability
density µ is a solution of equation (34).
We have thus proved that solving the system of coupled equations (33) and (34), one obtains the solution of the
inﬁnite hierarchy (21) in the factorized form (32). This remarkable reduction of the dynamical hierarchy to a closed
system of two equations does not involve any approximation, provided µ(2|1; t) has the structure (31). The adhesive
collisions do correlate the motion of the nearest neighbours (the mean ﬁeld approach is ruled out), but no three- or
more-particle correlations are created in the course of time. The same kind of situation has been already discovered
in the case of ballistic annihilation [10].

V. EVOLUTION OF REDUCED DENSITIES

The factorized form (32) of distributions µk implies the analogous factorization of the reduced densities

ρ(1, . . . , k; t) = ρ1(1; t)
 j=k−1∏

j=1 ρ(j + 1|j; t) (39)

where ρ(2|1; t) is the conditional density
 7

ρ(2|1; t) ≡ ρ(X21, P2, M2|0, P1, M1; t) = ρ2(1, 2; t)
ρ1(1; t) (40)

From the closed system of equations (33), (34) for the nearest neighbour distributions one can derive the corresponding
set of dynamical equations for the densities ρ1 = µ1 and ρ(2|1; t). First of all let us notice that the relation (9) implies
the equality
 ρ2(X1, P1, M1, X1+, P2, M2; t) = µ2(X1, P1, M1, X1+, P2, M2; t) (41)

Hence, equation (33) preserves its form

∂
∂t ρ1(1; t) = ∫ d1′ ∫ d2′C(1′, 2′)δ[1 − (1′ + 2′)]ρ1(1′; t)ρ(2′|1′; t)

− ∫ d1′C(1′, 1)ρ1(1′; t)ρ(1|1′; t) − ∫ d1′C(1, 1′)ρ1(1; t)ρ(1′|1; t) (42)

In order to derive the closed evolution equation for ρ(2|1; t) one has to use the formula

ρ(2|1; t) = µ(2|1; t) +
 ∞∑

r=1
 ∫ d1′ ∫ d2′ . . . ∫ dr′ θ(X ′
1 − X1)θ(X2 − X ′
r)

×
 r−1∏

j=1 θ(X ′
j+1 − X ′
j) µ(1′|1; t)µ(2′|1′; t) · · · µ(r′|r′ − 1; t)µ(2|r′; t) (43)

(see (9) and (32)). Using then repeatedly equation (34) one arrives at the equation
[ ∂
∂t + L12 + C(1, 2)
] ρ(2|1; t) = ∫ d1′ ∫ d2′C(1′, 2′)δ[2 − (1′ + 2′)]ρ(1′|1; t)ρ(2′|1′; t)

+ ∫ d1′C(1, 1′)ρ(1′|1; t)[ρ(2|1; t) − ρ(2|1′; t)]

− ∫ d1′{C(1′, 2)ρ(1′|1; t)ρ(2|1′; t) + C(2, 1′)ρ(1′|2; t)ρ(2|1; t)} (44)

Equations (42) and (44) form a closed system which suﬃces to determine the reduced densities of any order owing to
the relation (39).
 VI. SELF-SIMILAR SOLUTIONS

It seems interesting to check whether the aggregation dynamics is compatible with self-similar solutions. In other
words, whether the evolution of the merging masses can be entirely reduced to rescaling of densities of a given shape
(this idea has been followed in the study of the Burgers model of turbulence [9]). In order to investigate this question
we insert into equations (33), (34) the assumed scaling formulas

µ1(P1, M1; t) = tγ1 µ1 (
P1t1−2α, M1t−α; 1) (45)

µ(X21, P2, M2|0, P1, M1; t) = tγ2 µ(X21t−α, P2t1−2α, M2t−α|0, P1t1−2α, M1t−α; 1) (46)

where X21 = X2 − X1 and where we have used the fact that the three variables

X21, P
M t, M
2ρ (47)

have the same dimension and must thus scale in the same way.
As the mass is conserved, the integral
∫ +∞

−∞ dP ∫ ∞

0 dM M tγ1 ν(P t1−2α, M tα) (48)

8

representing the total mass density does not depend on time. This implies the relation

γ1 = 1 − 4α. (49)

On the other hand, the normalization condition (29) leads to

γ2 = 1 − 4α. (50)

It can be checked by a straightforward calculation that the distributions µ1(1; t) and µ(2|1; t) of the form (45) and
(46), respectively, with the exponents (α, γ1, γ2) satisfying equations (49) and (50), lead to a consistent closed system
of equations for the self-similar distributions µ1(P ′, M ′; 1) and µ(2′|1′; 1) when put into the reduced hierarchy (33),
(34). It follows that the dynamics does not suﬃce to ﬁx completely the values of the exponents. They can thus
depend on the nature of the initial condition of the system.

VII. A STATISTICAL MECHANICAL MODEL

In this section, we give a microscopic description of the dynamics of ballistic aggregation from the view-point of
statistical mechanics by recalling the model introduced in [1] and [3].
One considers the aggregation process developing from a simple initial condition. At t = 0, all the particles
have the same mass m and are located on the sites Xj = ja of an inﬁnite regular lattice with lattice constant a
(j = 0, ±1, ±2, ...). The mass density ρ = m/a. It is assumed that the initial momenta are uncorrelated, with a
distribution corresponding to thermal equilibrium at inverse temperature β:

ϕm(p) = ( β
2πm
 )1/2 exp (
− βp2

2m
 ) (51)

As it has already been explained in Section III, the dynamics of the sticky gas has the remarkable property that any
mass aggregate is found on the trajectory of the center of mass of the initial cluster it has been formed from. In
particular, the state of an aggregate Mj = njm at time t > 0 determines uniquely the set of nj consecutive initial
masses which constitute it: they are located at t = 0 within the interval [
Xj − Y +
j + a/2, Xj − Y −
j − a/2] (see also
Eqs.(22),(23)). This property permits to write explicitly the kinematical constraints that select the subset of initial
phase space conﬁgurations leading to the occurrence of a speciﬁc sequence of aggregate states j = (Xj, Pj, Mj), j =
1, . . . , k, within [L1, L2] at time t > 0. The distributions µk(1, 2, . . . , k; t |L1, L2) are then obtained by averaging these
constraints over the initial state.
The origin of the constraints is two-fold. One class of them ensures that the nj initial particles located in the interval
[Xj −Y +
j +a/2, Xj −Y −
j −a/2] do merge and form the jth aggregate before time t. A necessary and suﬃcient condition
here is that the trajectories of the centers of mass of all the pairs of subclusters of consecutive initial particles, which
form a partition of the initial nj-particle cluster, cross before time t. After averaging, this leads to functions denoted
by Im(Mj, Pj; t) which are the probability densities for the formation of masses Mj = njm, with momenta Pj from
the corresponding sets of nj initial neighbouring masses.
The second class of constraints guarantees that no particles other than the k speciﬁed aggregates are found within
[L1, L2] at time t. The particles initially located in (−∞, ja] will be found to the left of L1 if the positions of all
the centers of mass of clusters of consecutive initial masses located in [(j − i)a, ja], i = 1, 2, . . . stay smaller than L1
up to time t. After averaging, this will be expressed by a function Jm(Y ; t), where Jm(−L1 + (j + 1/2)a; t) (resp.
Jm(L2 − (j + 1/2)a; t) is the probability for ﬁnding the particles initially located in (−∞, ja] (resp. [(j + 1)a, ∞)) in
(−∞, L1] (resp. in [L2, ∞)). In particular, in terms of function Jm deﬁned in this way the probability µ0,m(t|L1, L2)
of ﬁnding the interval [L1, L2] void of particles is given by

µ0,m(t|L1, L2) = ∑

j Jm (−L1 + (j + 1/2)a; t) Jm (L2 − (j + 1/2)a; t) (52)

The probability density µ1,m (6) reads 1

1We add the index m to keep in mind the discrete nature of the initial state.

9

µ1,m(1; t) =
 ∞∑

n1=1 δ(M1−n1m) ∑

j δ (X1 − Y +
1 − (j + 1/2)a)

×Im(M1, P1; t)Jm (
−Y +
1 ; t) Jm (
Y −
1 ; t) (53)

where the summation involving δ-functions is a manifestation of the discreteness of the initial masses and the lattice
positions. The function Im in (53) ensures that the particles initially located in [X1 − Y +
1 + a/2, X1 − Y −
1 − a/2] have
met to form the aggregate, while the functions Jm ensure that all the particles initially located on the left of X1 − Y +
1
(resp. on the right of X1 − Y +
1 ) are at time t on the left (resp. on the right) of X1.
The probability density µ2,m (6) is given by

µ2,m(1, 2; t) = θ(X2 − X1)
 ∞∑

n1=1 δ(M1 − n1m)
 ∞∑

n2=1 δ(M2 − n2m)

× ∑

j δ (
X1 − Y +
1 − (j + 1/2)a) δ (
X2 − X1 + Y −
1 − Y +
2 )

×Im(M1, P1; t)Im(M2, P2; t)Jm (
−Y +
1 ; t) Jm (
Y −
2 ; t) . (54)

In this expression the ni and j summations involving δ-functions reﬂect again the discreteness of the initial conditions.
The additional δ−function obtained here by construction reﬂects the fact that the aggregates are nearest neighbours
and imposes precisely the condition (31) under which the hierarchy could be reduced. Once again, functions Im
stand for the formation of aggregates 1 and 2, while functions Jm ensure that particles initially located on the left of
X1 − Y +
1 (resp. on the right of X2 − Y −
2 ) stay at time t on the left of X1 (resp. on the right of X2).
The higher order distributions µk,m can be constructed along the same lines. They verify the factorization (32)

µk,m(1, . . . , k; t) = µ1,m(1; t)
 k−1∏

j=1 µm(j + 1|j; t) (55)

with the conditional probability µm(2|1; t), derived from (53) and (54), of the form

µm(2|1; t) = µ2,m(1, 2; t)
µ1,m(1; t)

= θ(X2 − X1)
 ∞∑

n2=1 δ(M2 − n2m)δ (
X2 − X1 + Y −
1 − Y +
2 ) Im(M2, P2; t) Jm (
Y −
2 ; t)

Jm (
Y −
1 ; t) (56)

Note that this conditional probability has the structure (31).
To have the model in an explicit form, it remains to give the formulae that express functions Im and Jm in
terms of the constraints: the details of the calculation can be found in [3]. The important point is that, due to the
uncorrelated Gaussian initial velocity distribution, the whole aggregation dynamics can be mapped on the following
equivalent Brownian motion problem:
Let P (τ ) be a Brownian path starting from the origin, P (0) = 0. Then, for M = nm,

Im(M, P ; t) = E(0,0){P (rm) ≥ rm[(M − rm)/2ρt + P/M ], r = 1, . . . , n − 1|P (nm) = P } (57)

is the conditional measure of such paths constrained to be above the parabolic barrier rm[(M − rm)/2ρt + P/M ] at
discrete ”times” τr = rm, r = 1, . . . , n − 1 and to end in P at ”time” nm, see Fig.1.

10
 M
 I (M,P;t)
m
 τ

P (τ)

P

FIG. 1. Brownian interpretation of the function Im(M, P ; t). The Brownian motion starts at P (0) = 0, ends at P (M ) = P
while overpassing the points P (rm) ≥ rm(2ρQ+ − rm)/2ρt, (r = 1, . . . , n − 1) with Q+ = P t/M + M/2ρ.

Likewise
 Jm(Y ; t) = E(0,0){P (rm) ≥ rm(2ρY − rm)/2ρt, r = 1, 2, . . .} (58)

is the measure of the paths that remain above the barrier rm(Y − rm)/2ρt for all discrete times τr = rm, r = 1, . . .;
see Fig.2. We recall that the dynamics is deterministic, and randomness enters only through the initial velocity
distribution: P (τ ) is a process in momentum space, as a function of the mass of aggregates.

P J (Y;t)
m
 τ

(τ)

FIG. 2. Brownian interpretation of the function Jm(Y ; t). The Brownian motion starts at P (0) = 0 and overpasses the
points P (rm) ≥ rm(2ρY − rm)/2ρt, (r = 1, 2, . . .).

A simple and immediate consequence are the scaling properties of functions Im and Jm with respect to time. Owing
to the fact that the scaled Brownian motion (ρt)
α/2P (τ (ρt)
−α) is equivalent in probability to P (τ ), the functions Im
and Jm obey the scaling relations with α = 2/3

Im(M, P ; t) = (ρt)
−1/3Im′ (M ′, P ′; 1) ≡ (ρt)
−1/3Im′ (M ′, P ′)
Jm(Y ; t) = Jm′ (Y ′; 1) ≡ Jm′ (Y ′) (59)

with
 m′ = m(ρt)
−2/3, P ′ = P (ρt)
−1/3, M ′ = nm′ = M (ρt)
−2/3, Y ′ = (ρt)
−2/3ρY (60)

The construction (53)-(58) yields in principle a solution to the dynamical hierarchy that has the factorization property:
µ1,m(1; t) and µm(2|1; t) have to verify the coupled equations (33)-(34), adapted to the case of discrete masses. We
shall not proceed to this veriﬁcation now, but rather simplify ﬁrst the discussion by taking the continuum limit of our
statistical mechanical model.
 11

The continuum limit amounts to let m → 0 and a → 0 while keeping the initial mass density ρ = m/a and time
ﬁxed. Because of (59) one can alternatively ﬁx the scaled momentum P ′ and the scaled mass M ′ and look for the
large time asymptotics t → ∞. In the ﬁrst view, one looks for the formation of masses of order 1 at a given time
arising from an initial inﬁnitesimal dust. In the second view one looks for the formation of masses of size ∼ mt2/3,
t → ∞, while keeping the discrete initial condition. These two views are equivalent. The interesting point is that
in the continuum limit the Brownian expressions (57) and (58) can be computed in a closed analytical form, thus
providing an explicit complete statistical description of the aggregation process. Moreover this description exactly
coincides with that of the statistics of shocks in the inviscid limit of the Burgers equation with white noise initial
data.
To conclude one can check that the factorization property (55) persists for a wider class of initial conditions,
for instance allowing any uncorrelated initial velocity distribution, and an arbitrary (non random) choice of initial
positions and masses.
 VIII. THE CONTINUUM LIMIT

In this section, we determine the continuum limits (m → 0 with ρ = m/a ﬁxed) of the one- and two-point probability
densities
 lim
m→0 µ1,m(1; t) = µ1(1; t)

lim
m→0 µ2,m(1, 2; t) = µ2(1, 2; t). (61)

Owing to the scaling relations (59) it is suﬃcient to calculate functions µ1(1; t) and µ2(1, 2; t) for t = 1 and
2 ρ = 1.
From now on we drop the time parameter from the notation setting simply µ1,m(1; t) = µ1,m(1), µ2,m(1, 2; t) =
µ2,m(1, 2), and so on. Later in this section we will comment on the way to recover the time variable in the continuum
limit of these densities.
Let us ﬁrst introduce the transition probability density kernel

Km,ν(M1, P1, M2, P2) = E(M1,P1){P (rm) ≥ fν(rm), r = n1 + 1, . . . , n2 − 1|P (M2) = P2} (62)

for the Brownian motion P (τ ) to start at P (M1) = P1, and end at P (M2) = P2 with M1 = n1m and M2 = n2m,
while overpassing the points fν(rm), r = n1 + 1, . . . , n2 − 1, where fν(τ ) is the parabola

fν(τ ) = ντ − τ 2

2 . (63)

According to deﬁnitions (57) and (58), the functions Im and Jm appearing in the one- and two-point densities can be
expressed in terms of the transition kernel (62) as

Im(M, P ) = Km,Y + (0, 0, M, P ) (64)

and
 Jm(Y ) = lim
M→∞
 ∫ ∞

fY (M) dP Km,Y (0, 0, M, P ). (65)

In (62), Brownian paths are allowed to make excursions through holes of width m separating the discrete points
rm. In the continuum limit m → 0, the weight of such excursions becomes vanishingly small and the paths become
constrained to overpass the continuous barrier fν(τ ), M1 ≤ τ ≤ M2. Thus for P1 > fν(M1) and P2 > fν(M2)

Km,ν(M1, P1, M2, P2) = Kν(M1, P1, M2, P2) + Rm,ν(M1, P1, M2, P2) (66)

where limm→0 Rm,ν(M1, P1, M2, P2) = 0, and

Kν(M1, P1, M2, P2) = E(M1,P1){P (τ ) > fν(τ ), M1 ≤ τ ≤ M2|P (M2) = P2} (67)

2In [3] the density was set equal to 1/2.
 12

is the transition kernel for a Brownian motion with a continuous parabolic barrier. It satisﬁes the diﬀusion equation

∂
∂M2 Kν(M1, P1, M2, P2) = 1
2β ∂2

∂P2 Kν(M1, P1, M2, P2) (68)

with Kν(M, P1, M, P2) = δ(P1 − P2), and the Dirichlet conditions on the barrier: Kν(M1, P1, M2, P2) = 0 when
P1 = fν(M1) or P2 = fν(M2).
Our object now is to express the distributions of aggregates in the continuum limit in terms of the kernel (67), which
can be explicitly computed (Section II of [7]). However, in the continuum limit of Im and Jm the starting point (0, 0)
of the Brownian motion lies on the parabola (63) where Kν(0, 0, M, P ) = 0. Thus the determination of the densities
µ1(1) and µ2(1, 2) requires the evaluation of the leading term in the asymptotic expansion of Km,ν(0, 0, M, P ) as
m → 0. This is not an elementary task since it involves the control of the cumulated eﬀect of Brownian excursions in
small intervals ((r − 1)m, rm), r = 1, 2, . . . in the neighbourhood of the origin. The result is given in the following
proposition

Proposition
lim
m→0 Km,ν(0, 0, M, P )
√
m = 1
√
2β ∂
∂P0 Kν(M0, P0, M, P )
∣
∣
∣
∣(M0,P0)=(0,0) , M > 0, P ≥ fν(M ) (69)

With this result the continuum limits m → 0 of functions Im and Jm, as expressed in (64) and (65), with ﬁxed
initial mass density ρ = m/a, read

lim
m→0 Im(M, P )
m = 1
2β ∂2

∂P1∂P2 KY + (0, P1, M, P2)
∣
∣
∣
∣P1=0,P2=P ≡ I(M, P ) (70)

and
 lim
m→0 Jm(Y )
√m = lim
M→∞ 1
√
2β
 ∫ ∞

fY (M) dP ∂
∂P1 KY (0, P1, M, P )
∣
∣
∣
∣
P1=0 ≡ J(Y ). (71)

In obtaining (70) we have taken into account that in (64), in addition to (0, 0), the paths have a second contact point
with the parabola at (M, P ).
Then, using equations (53),(54), the continuum limits of the one- and two-point probability densities can be readily
found. One multiplies and divides (53) by m2 and takes (70) and (71) into account. Then, m → 0 playing the role of
an inﬁnitesimal, the discrete sums go to the corresponding integrals, which can be evaluated owing to the δ-functions,
yielding eventually the formula
 µ1(1) = I(M1, P1)J (
−Y +
1 ) J (
Y −
1 ) (72)

and, in the same way

µ2(1, 2) = θ(X2 − X1)δ (
X2 − X1 + Y −
1 − Y +
2 ) I(P1, M1)I(P2, M2)J (
−Y +
1 ) J (
Y −
2 ) . (73)

The time and the initial density dependence can always be reintroduced in the continuum limit. Indeed, through
Eqs.(59) and (70),(71) we get the scaling properties of functions I and J

J(Y ; t) = (ρt)
−1/3J(Y ′), I(M, P ; t) = (ρt)
−1I(M ′, P ′) (74)

with the scaling functions J(Y ) and I(M, P ) deﬁned above. This implies the scaling behavior of the densities in the
continuum limit of the form

lim
m→0 µk,m(1, . . . , k; t) = µk(1, . . . , k; t) = ρk(ρt)
−5k/3µk(1′, . . . , k′) (75)

with
 j′ ≡ (X ′
j, P ′
j , M ′
j) = ( ρXj
(ρt)2/3 , Pj
(ρt)1/3 , Mj
(ρt)2/3
 ) . (76)

13

The scaling functions µ1(1) and µ2(1, 2) are given by (72) and (73) and, for higher orders, the scaling functions are
given by
 µk(1, . . . , k) = µ1(1)
 k−1∏

j=1
 µ2(j, j + 1)
µ1(j) . (77)

From Eq.(52), we ﬁnd that the probability density to ﬁnd an interval [0, x) void of aggregates scales in the continuum
limit as
 µ0(x; t) = µ0(x
′) (78)

with x
′ = ρx(ρt)
−2/3 and
 µ0(x) = ∫ dyJ(y)J(x − y). (79)

Since the functions I(M, P ) and J(Y ) have been explicitly computed in [7], the results (72,73) and (77) give a complete
solution of the ballistic aggregation model in a closed analytical form. We postpone the discussion of this solution to
the next section and devote the rest of the present section to the proof of (69).

Proof of the proposition
The strategy to prove Eq.(69) is to bound the transition kernel (62) while linearizing the constraints imposed on
the ﬁrst k = M0/m points, 0 < M0 < M .
We have (
ν − M0
2
 ) τ ≤ fν(τ ) ≤ ντ, 0 ≤ τ ≤ M0 (80)

Let us introduce the kernel

K l
m,ν(0, 0, M0, P0) = E(0,0){P (rm) ≥ νrm, r = 1, . . . , k − 1|P (M0) = P0} (81)

for paths starting at (0, 0), ending at (M0, P0), while overcoming the linearly distributed sequence of discrete points
νrm, r = 1, . . . , k − 1. Clearly (see Fig. 3)

K l
m,ν(0, 0, M0, P0) ≤ Km,ν(0, 0, M0, P0) ≤ K l
m,ν−M0/2(0, 0, M0, P0). (82)

τ

P
 m MM 0

0P
 ν

(τ)P
 FIG. 3. Illustration of the “linearized” bounds used to in (83).

14

Using the Markov property of the Brownian motion, one infers from (82) the bounds for the kernel Km,ν(0, 0, M, P )
for M > M0 > 0
 K (<)
m,ν(0, 0, M, P ) ≤ Km,ν(0, 0, M, P ) ≤ K (>)
m,ν(0, 0, M, P ) (83)

with
 K (<)
m,ν(0, 0, M, P ) = ∫ dP0 K l
m,ν(0, 0, M0, P0)Km,ν(M0, P0, M, P ) (84)

and
 K (>)
m,ν(0, 0, M, P ) = ∫ dP0 K l
m,ν−M0/2(0, 0, M0, P0)Km,ν(M0, P0, M, P ). (85)

We shall calculate these bounds by ﬁrst letting m → 0 and then M0 → 0. They will be shown to coincide in this limit.
It is convenient to relate the transition kernel K l
m,ν (81) for the Brownian process with discrete linear barrier
P (rm) ≥ νrm, r = 1, . . . , k − 1 to that of a dimensionless Brownian process q(τ ) with covariance equal to 1, the paths
constrained to be positive at integer times, and with the corresponding transition kernel

Gk(q) = E(0,0) {q(n) ≥ 0, n = 1, . . . k − 1|q(k) = q} . (86)

For this later process, we deﬁne the average ⟨f (q)⟩k = ∫ dq Gk(q)f (q). The moments 〈
qj〉
k , j = 0, 1, 2, . . . will be for
us of particular interest.
The relation between the two processes is given by removing a linear drift

q(τ ) =
 √ β
2m (P (τ ) − ντ ) (87)

which leads to the relation

K l
m,ν(0, 0, M0, P0) = exp ( βν2M0
2
 ) √ β
2m Gk
 (√ β
2m (P0 − νM0)

)
 , k = M0
m . (88)

When this is inserted into (84), one obtains

K (<)
m,ν(0, 0, M, P ) = exp (
− βν2M0
2
 )

× ∫ dq Gk(q)e−ν(2mβ)1/2qKm,ν
 (
M0, νM0 + √ 2m
β q, M, P ) . (89)

Then, we take the following steps. First, for M0 > 0 we can replace in (89) the kernel Km,ν for the discrete parabolic
barrier by its continuous limit (66). Next, we expand the integrand up to second order in the variable √
mq. This
gives
 K (<)
m,ν(0, 0, M, P ) = e−βν2M0/2[ ⟨1⟩k Kν(M0, νM0, M, P )

+√
m ⟨q⟩k
 (
−ν√
2βKν(M0, νM0, M, P ) + √ 2
β ∂
∂P0 Kν(M0, P0, M, P )|P0=νM0
 )]

+ 〈
q2〉

k O(m) + ⟨1⟩k o(m). (90)

Recalling that k = M0/m, we have to evaluate the ﬁrst moments 〈
qj〉

k of the distribution Gk(q) for large k. This is
done in appendix A with the help of the Sparre-Andersen theorem together with a Tauberian theorem. One gets

⟨1⟩k ∼
 √ M0
πm , ⟨q⟩k ∼ 1
2 , 〈q2〉

k ∼ √ m
πM0 , m → 0. (91)

Hence
 15

lim
m→0 K (<)
m,ν(0, 0, M, P )
√m = e−βν2M0/2 [ Kν(M0, νM0, M, P )
√
πM0

+ 1
2
 (
−ν√
2βKν(M0, νM0, M, P ) + √ 2
β ∂
∂P0 Kν(M0, P0, M, P )|P0=νM0
 )] + O(
√M0) (92)

Finally, since Kν(M0, P0, M, P ) is diﬀerentiable with respect to P0 and vanishes at P0 = 0, one has
Kν(M0, νM0, M, P ) = O(M0), M0 → 0, so that

lim
M0→0 lim
m→0 K (<)
m,ν(0, 0, M, P )
√m = 1
√2β ∂
∂P0 Kν(M0, P0, M, P )
∣
∣
∣
∣
(M0,P0)=(0,0) . (93)

The upper bound K (>)
m,ν(0, 0, M, P ) is treated in the same way and attains the same limit, thus leading to the result
Eq.(69) of the proposition.
The analysis performed in [3] was based on the lower bound

Km,ν(0, 0, M, P )
√m > 1
√
2πβ ∂
∂P0 Kν(M0, P0, M, P )
∣
∣
∣
∣
(M0,P0)=(0,0) (94)

obtained by retaining the eﬀects of Brownian excursions only in the ﬁrst interval (0, m) at the origin. The result
obtained therein diﬀers from the exact limit (69) by a factor 1/√
π. In fact, the limit (69) involves contributions of
inﬁnitely many intervals, which can be summed up by applying the Sparre-Andersen theorem.

IX. EXPLICIT SOLUTION

The function I(M, P ) (70), explicitly computed in [7], has the form

I(M, P ) = 2b3 exp (−b3 [ P 2

M + M 3

12
 ]) I(M ), (95)

where we set b = (β/2)
1/3 and
 I(M ) = ∑

k≥1 e−bωkM . (96)

The function J(Y ) (71) reads
 J(Y ) = √
be−b
3Y 3/3J (Y ) (97)

with
 J (Y ) = 1
2iπ
 ∫ +i∞

−i∞ dw ebY w

Ai(w) . (98)

In (96) and (98), Ai(w) is the Airy function [11], solving the diﬀerential equation

f ′′(w) − wf (w) = 0, (99)

Ai(w) is analytic in the complex w plane, and has an inﬁnite countable set of zeros −ωk on the negative real axis,
0 < ω1 < ω2 < · · ·. The asymptotic behavior of these functions has been derived in [7]

I(µ) ∼ 1
√
4πb3µ3 , µ → 0; I(µ) ∼ exp(−ω1bµ), µ → ∞ (100)

and
 J (u) ∼ e−buω1

Ai′(−ω1) , u → ∞; J (u) ∼ −2bu exp ( b3u3

3
 ) , u → −∞. (101)

16

In fact, these results, which have been announced in [4], were derived in details in the related framework of the
Burgers turbulence [7] . The solutions of the one-dimensional Burgers equation with a white-noise initial condition,
develop, in the limit of vanishing viscosity, a train of shock waves. In Burgers theory, a shock located at X is
characterized by two parameters µ and η, and can be identiﬁed with a particle of mass M = µ at point X with
momentum 3 P = −η. Then it turns out that dynamics of shocks is completely equivalent to ballistic aggregation
subject to mass and momentum conservation [9], [5]. Moreover, the white noise covariance is D/2 = 1/(2β) and the
mass density ρ corresponds to a length scale in the Burgers equation. In this section, we recast the results of [7] in
the language of ballistic aggregation of interest here 4.
We consider ﬁrst the probability density (79) of ﬁnding an interval [0, x) void of particles

µ0(x) = ∫ ∞

−∞ dy J(y)J(x − y)

= √ π
bx exp (
− b3x
3

12
 ) 1
(2π i)2
 ∫ +i∞

−i∞ dw1
 ∫ +i∞

−i∞ dw2 exp ( bx
2 (w1 + w2) + (w1−w2)2

4bx )

Ai(w1)Ai(w2) (102)

which is plotted on Fig. 4. We have limx→0 µ0(x) = 1, and asymptotically for x → ∞

µ0(x) = √ π
bx
 exp (
− b
3x3
12 − bω1x
)

[Ai′(−ω1)
]2
 (
1 + O ( 1
x
 )) . (103)

0.0 1.0 2.0 3.0
x

0.0

0.2

0.4

0.6

0.8

1.0µ0(x)
FIG. 4. The probability density µ0(x) to ﬁnd no aggregates in an interval [0, x], for the parameters t = 1, ρ = 1 and β = 2
(a = 1 in Eq.(102)).

The one point probability density (72) reads

3In Burgers language, one speaks of the shock strength µ/t and shock wavelength ν = µ/2 − tη/µ
4In the present paper, the Brownian motion P (τ ) and the parabolic constraints fν (τ ) have the sign opposite to the corre-
sponding objects in [7], namely −ψ(y) and −sν(y). By invariance of Brownian motion under space reﬂexion, the functions I
and J are the same in both papers, provided that M and P correspond to µ and −η in the notation of [7].

17

µ1(P, M ) = I(M, P )J (
− P
M − M
2
 ) J ( P
M − M
2
 )

= 2b4J ( P
M − M
2
 ) I(M )J (
− P
M − M
2
 ) (104)

where I and J are given by Eqs.(96,98). Integration over the momentum space yields the mass density distribution

µ1(M ) = 2b3M I(M )H(M ) (105)

with
 H(M ) = 1
2iπ
 ∫ +i∞

−i∞ dw e−bMw

Ai2(w) (106)

whose asymptotic behavior reads

H(µ) ∼ 1, µ → 0; H(µ) ∼ √
πb3µ3 exp (
− b3µ3

12
 ) , µ → ∞. (107)

The shape of the mass density distribution (105) is plotted on Fig. 5.

0.0 1.0 2.0 3.0 4.0
M

0.0

1.0

2.0µ1(M)
FIG. 5. The mass density µ1(M ) for the parameters t = 1, ρ = 1 and β = 2 (a = 1 in Eq.(105)).

Its asymptotic behavior can be computed from (100) and (107) yielding the formulae

µ1(M ) =
 √ b3

πM + O(M 1/2), M → 0 (108)

and
 µ1(M ) ∼ 2√
πb9/2M 5/2 exp (
− b3M 3

12 − ω1bM ) , M → ∞. (109)

The exact scaling function obtained here is quite diﬀerent from a simple exponential exp(−M ) suggested on the basis
of numerical simulations in [1]. For example, one notices that small masses (M ≪ t2/3) are much more likely to be
present in the system than suggested in [1], while large masses (M ≫ t2/3) have a much smaller chance to be present.

18

Let us remark that the exponential form has been also found in [9] and [2] by solving the dynamical equations in a
mean-ﬁeld-like approximation scheme. In the framework of Burgers turbulence, more reﬁned numerical simulations
were performed by Kida [6] where the small mass behavior of the scaling function compatible with Eq.(108) has been
found. Moreover, our result (108) is compatible with the rigorous upper and lower bounds derived in [12]. The large
mass behavior Eq.(109) ﬁts into rigorous bounds of the type exp(−CM 3) found in [13] and [3].
The density of particles of velocity V = P/M , given by

µ1(V ) = ∫ ∞

0 dM M I(M )J (V − M/2)J (−V − M/2) (110)

is plotted on Fig.6.
 -3.0 -2.0 -1.0 0.0 1.0 2.0 3.0
V

0.0

0.5

1.0

1.5µ1(V)
FIG. 6. The velocity probability density µ1(V ) for the parameters t = 1, ρ = 1 and β = 2 (a = 1 in Eq.(110)).

From (110) and the asymptotic behavior (100), (101) of I and J, one can derive the bound

µ1(V ) ≤ C|V | exp (
− b3|V |3

3 − b|V |ω1
) , |V | → ∞. (111)

This shows that the large velocity behavior cannot be Gaussian and thus invalidates the numerically based hypothesis
of Kida [6].
The density of nearest neighbours (73) has the form

µ2(1, 2) = 4b7θ(X)δ (
X + Y −
1 − Y +
2 )

× exp (
− b3

3
 (
(Y −
1 )
3 + (Y +
2 )
3)
) I(M1)I(M2)J (
−Y +
1 ) J (
Y −
2 ) (112)

with X = X2 − X1. Expression (112) permits to compute the collision frequency between the particles deﬁned by

ν2(M1, M2; t) = ∫ ∞

−∞ dP1
 ∫ ∞

−∞ dP2
 ∣
∣
∣
∣ P1
M1 − P2
M2
 ∣
∣
∣
∣ µ2(0, P1, M1, 0+, P2, M2; t). (113)

First, we notice that relation (75) implies the scaling

ν2(M1, M2; t) = ρ2

(ρt)3 ν2(M ′
1, M ′
2) (114)

19

with
 ν2(M1, M2) = ∫ ∞

−∞ dP1
 ∫ ∞

−∞ dP2
 ∣
∣
∣
∣ P1
M1 − P2
M2
 ∣
∣
∣
∣ µ2(1, 2) (115)

This last integral, upon inserting formula (112), gives

ν2(M1, M2) = 2b6M1M2(M1 + M2)I(M1)I(M2)H(M1 + M2) (116)

with H given by Eq.(106). Clearly, the collision frequency does not factorize into a product of a function of M1 and
a function of M2. This fact invalidates the weak mean-ﬁeld hypothesis whose consequences where analysed in [2].

The two-point distribution function

The scaling form ρ2(1, 2) = ρ1ρ2(2|1) of the two-point reduced number density of aggregates enables to study the
long distance correlations in the system. The calculation requires the summation over all possible conﬁgurations of
aggregated masses in between the particles 1 and 2 (formula (43)). In principle, this summation can be be performed
as follows. Because of translation invariance, the conditional probability µ(2|1)

µ(X2, P2, M2|X1, P1, M1) = (P1, M1|T (X2 − X1)|P2, M2) (117)

can be considered as the kernel of an integral operator T (X) acting in the mass and momentum space. Then the
series (43) can be summed up by applying the Laplace transformation. Setting

˜T (s) = ∫ ∞

0 dXe−XsT (X)

˜ρ2(s, P1, M1, P2, M2) = ∫ ∞

0 dXe−Xsρ2(0, P1, M1, X, P2, M2) (118)

one ﬁnds by the convolution theorem

˜ρ2(s, P1, M1, P2, M2) = ρ1(P1, M1)
 ∞∑

r=1(P1, M1| ˜T r(s)|P2, M2)

= ρ1(P1, M1)(P1, M1| ˜T (s)(I − ˜T (s))
−1|P2, M2) (119)

Inverting the operator I − ˜T (s) and then performing the inverse Laplace transformation are not easy operations here.
So, we shall proceed in a diﬀerent way. In the context of the Burgers equation, ρ2(1, 2) corresponds to the joint density
to ﬁnd two shocks at distance |X2 − X1|. This density, in the Brownian interpretation, is the measure of paths that
have contact points with two parabolas: one centered at X1 another at X2. Summing over all such paths amounts to
sum over intermediate sequences of neighbouring aggregates in the particle language. We refer to [7] for details. One
ﬁnds the following form of the two-point density

ρ2(1, 2) = J (
−Y +
1 ) I(M1, P1) [δ (
X + Y −
1 − Y +
2 )

+θ (
X + Y −
1 − Y +
2 ) H (
X, Y −
1 , Y +
2 )] I(M2, P2)J (
Y −
2 ) (120)

The δ−function term corresponds to the case when 1 and 2 are the nearest neighbours, whereas the function
H (X, Y1, Y2) embodies precisely the sum over all conﬁgurations of intermediate particles. The function H will not be
reproduced here. The important fact is that its large distance asymptotic behaviour can be calculated leading to the
folowing cluster property of the two-point function [7]

ρ2(M1, P1, M2, P2, X) − ρ1(M1, P1)ρ1(P2, M2) ∼ −b11/2 32√
π
X 5/2 exp (
− b3X 3

12 − bω1X)

× exp (
−bω1(Y −
1 − Y +
2 )
) J (
−Y +
1 ) I(M1)I(M2)J (
Y −
2 ) , X → ∞. (121)

We see that although the particles in the initial state are not correlated and the motion between collisions is free, the
aggregation process induces dynamic correlations in the course of time. However, these correlations have a very short
range since they stay dominated by the rapidly decaying cubic exponential factor exp(−b3X 3/12).

20

X. RIGOROUS SOLUTION OF THE DYNAMIC HIERARCHY

We have shown in Section IV how the inﬁnite hierarchy (21) describing the aggregation process could be reduced
to a system of two coupled equations (33), (34), satisﬁed by the one-particle density µ1(1; t), and the conditional
probability density µ(2|1; t). It is the right moment now to show that the constructed densities (72), (73) provide a
rigorous solution to the aggregation dynamics.
In (72) and (73) the densities µ1(1; t) and µ(2|1; t) are expressed in terms of the probability weights I(M, P ) and
J(Y ) (to recover the time variable t the scaling relations (74) have to be used). In order to evaluate the rate of
change of the state of the aggregating gas it is thus suﬃcient to calculate the time derivative of functions I(M, P ; t),
J(−Y +; t) and J(Y −; t), where Y ± = tP/M ± M/2ρ. A straightforward calculation can be performed starting from
the deﬁning formulae (57), (58), whose explicit form can be found in [3]. Technically it is simple but lengthy, so we
shall not reproduce it here. Taking then the continuum limit one ﬁnds the following system of equations

∂
∂t I(M, P ; t) = ∫ dM1
 ∫ dP1
 ∫ dM2
 ∫ dP2
 ( P1
M1 − P2
M2
 ) δ(M − M1 − M2)δ(P − P1 − P2)

×δ [( P1
M1 − P2
M2
 ) − M
2ρ
 ] I(M1, P1; t)I(M2, P2; t) (122)

∂
∂t J ( P
M t − M
2ρ ; t) = − ∫ dM1
 ∫ dP1
 ( P
M − P1
M1
 ) δ [( P
M − P1
M1
 ) t − M + M1
2ρ
 ]

×I(P1, M1; t)J ( P1
M1 t − M1
2ρ ; t) (123)

A somehow laborious but straightforward analysis permits to check that the above system of equations, when
combined with the relations (72), (73), implies the fundamental dynamic equations (33), (34). As one could expect
from the interpretation of functions I and J given in Section VII, the time derivative of I(M, P ; t) is positive and
produces gain terms in the kinetic equation (33), whereas the negative time derivatives of factors J(Y +; t) and J(Y −; t)
generate loss terms.
 XI. CONCLUDING COMMENTS

The hierarchy equations (21) describe the aggregation dynamics in a one-dimensional gas for arbitrary initial
conditions. We considered here in detail the case where statistical correlations existed only between the states of
the nearest neighbours. Under the precise condition (31), the evolution preserved this property, and the state of the
system remained entirely characterized by the number density of aggregates and by the conditional distribution of
nearest neighbours. This permitted to reduce the hierarchy to two coupled equations.
Rather than solving the obtained system of equations we determined the relevant distributions on the basis of their
deﬁnitions, and only a posteriori we could verify that they satisﬁed the dynamical laws. So, ﬁnding a systematic way
of solving the system (33), (34) remains an open problem.
When discussing the continuum limit we started from a very simple discrete initial condition, where no correlations
were present at all. In the course of time, the system turned out to build up correlations by its internal dynamics,
but only between the pairs of nearest neighbours. It is thus tempting to conjecture that the factorized form (32) of
the many particle densities represents the asymptotic long time structure of the system for general initial conditions,
as only the nearest neighbours get correlated by the process of aggregation. Let us recall that the correlations are
rapidly decaying with the distance (see (121).
A comment concerning the continuum limit seems also quite important. It has been noted at the end of Section VII
that introduction of properly scaled variables permitted to interpret the continuum limit as a long time limit. One
can thus expect that the dynamical properties derived here are quite universal, and do not depend on our particularly
simple choice of the initial distribution. In particular, it would be interesting to clarify how large is the class of initial
states which leads for long times to the mass density distribution plotted in Fig.(5).
Let us ﬁnally notice, that the dynamical scaling of the mass distribution predicted on the basis of intuitive arguments
in [1] agrees with the rigorous scaling relations (59). The prediction of the Brownian motion exponent α = 2/3 in [1]
seems independent of the initial condition, whereas we derived it starting from a particular state. It would be thus
interesting to clarify to what extent this type of scaling is universal. Indeed, our analysis showed that the aggregation
dynamics was in principle compatible with other values of α, not necessarily equal to 2/3.

21

ACKNOWLEDGMENTS

J. Piasecki acknowledges the hospitality at the Institute of Theoretical Physics of the Ecole Polytechnique F´ed´erale
de Lausanne, and the ﬁnancial support by the KBN (Committee for Scientiﬁc Research, Poland), grant 2 P03B 127
16.
 APPENDIX A:

The moments of the distribution Gk (86) can be obtained from its generating function γ(s, ξ)

∞∑

k=1 sk 〈
qj〉
k = (−i)
j ∂jγ(s, ξ)
∂ξj
 ∣
∣
∣
∣
ξ=0 (A1)

with
 γ(s, ξ) = 1 +
 ∞∑

k=1 sk ∫ ∞

0 dq eiξqGk(q) (A2)

This generating function can be computed by applying the Sparre-Andersen theorem to the process with independent
increments governed by the Gaussian distribution (π)
−1/2 exp(−q2) (section XVIII.3 of [14])

γ(s, ξ) = exp
 [ ∞∑

k=1
 sk

k
 ∫ ∞

0 dq eiξq e−q2/k
√πk
 ]
 . (A3)

Using (A3) we ﬁnd
 ∞∑

k=1 sk ⟨1⟩k = γ(s, 0) = exp
 ( ∞∑

k=1
 sk

2k
 )
 = 1
√
1 − s (A4)

and thus
 ⟨1⟩k = Γ(k + 1/2)
√
πΓ(k + 1) ∼ 1
√
πk , k → ∞. (A5)

For the ﬁrst and second moments we ﬁnd

∞∑

k=1 sk ⟨q⟩k = −i ∂γ(s, ξ)
∂ξ
 ∣
∣
∣
∣ξ=0 = 1
√
1 − s
 ∞∑

k=1
 sk

2√
πk (A6)

and
 ∞∑

k=1 sk 〈
q2〉
k = − ∂2γ(s, ξ)
∂ξ2
 ∣
∣
∣
∣ξ=0 = 1
4√
1 − s
 

 1
1 − s +
 ( ∞∑

k=1
 sk
√πk
 )2

 . (A7)

To proceed, we need the following Tauberian theorem (Theorem 5, section XIII.5 in [14]):
Let ck ≥ 0 be a monotonic sequence and suppose that the series ∑∞
k=1 cksk converges for 0 ≤ s < 1. Then, if L
varies slowly at inﬁnity 5 and α ≥ 0, each of the two relations

∞∑

k=1 cksk ∼ 1
(1 − s)α L ( 1
1 − s
 ) , s → 1 (A8)

5L varies slowly at inﬁnity if limt→∞ L(tx)/L(t) = 1 for all x, a condition which is veriﬁed in the subsequent applications
where L is a constant.
 22

ck ∼ 1
Γ(α) kα−1L(k), k → ∞ (A9)

implies the other.
From (A6), we have
 ∞∑

k=1 sk ⟨q⟩k ∼ 1
2(1 − s) , s → 1 (A10)

and thus
 ⟨q⟩k ∼ 1
2 , k → ∞. (A11)

For the second moment we ﬁnd
 ∞∑

k=1 sk 〈
q2〉

k ∼ 1
2(1 − s)3/2 , s → 1 (A12)

leading to
 〈
q2〉

k ∼
 √
k
√π , k → ∞. (A13)

To control the remainder in (90) by a limited Taylor expansion up to second order in q we use the fact that Gk(q)

is non negative and that the second q-derivative of e−ν√
2mβqKm,ν(M0, νM0 + √ 2m
β q, M, P ) has a q-integrable bound

for M > 0 uniform when m and M0 are in a neighbourhood of zero (irrespective of the sign of ν). This is indeed the
case because one can check that Kν(M0, P0, M, P ) as well as its ﬁrst and second P0-derivative obey Gaussian bounds
of the form C1 exp(−C2P 2
0 ) with C1 and C2 independent of m and M0, M0 < M

[1] G. F. Carnevale, Y. Pomeau and W. R. Young, Phys. Rev. Lett. 64, 2913 (1990).
[2] J. Piasecki, Physica A 190, 95 (1992).
[3] Ph. A. Martin and J. Piasecki, J. Stat. Phys. 76, 447 (1994).
[4] L. Frachebourg, Phys. Rev. Lett. 82, 1502 (1999).
[5] J. M. Burgers, The nonlinear diﬀusion equation, Reidel, Dordrecht (1974).
[6] S. Kida, J. Fluid Mech. 93, 337 (1979).
[7] L. Frachebourg and Ph. A. Martin, Submitted to J. Fluid Mech. (1999).
[8] D. Ruelle, Statistical Mechanics, ch.7, W.A. Benjamin, Inc., New York (1969).
[9] T. Tatsumi and S. Kida, J. Fluid Mech. 55, 659 (1972).
[10] J. Piasecki, Phys. Rev. E 51, 5535 (1995).
[11] M. Abramowitz and I. A. Stegun, Handbook of Mathematical Functions, Dover, New-York (1965).
[12] M. Avellaneda and W. E, Comm. Math. Phys. 172, 13 (1995).
[13] M. Avellaneda, Comm. Math. Phys. 169, 45 (1995).
[14] W. Feller, An Introduction to Probability Theory and its Applications, Vol II, Wiley and Sons, New York, (1971).

23
