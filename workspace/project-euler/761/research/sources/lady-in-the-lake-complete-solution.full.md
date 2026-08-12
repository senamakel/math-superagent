<!-- source: https://arxiv.org/pdf/2401.14994 | converted from PDF -->

arXiv:2401.14994v1  [math.OC]  26 Jan 2024
Complete Solution of the Lady in the Lake Scenario∗

Alexander Von Moll Meir Pachter

December 2023

Abstract

In the Lady in the Lake scenario, a mobile agent, L, is pitted against
an agent, M , who is constrained to move along the perimeter of a
circle. L is assumed to begin inside the circle and wishes to escape
to the perimeter with some ﬁnite angular separation from M at the
perimeter. This scenario has, in the past, been formulated as a zero-
sum diﬀerential game wherein L seeks to maximize terminal separation
and M seeks to minimize it. Its solution is well-known. However, there
is a large portion of the state space for which the canonical solution
does not yield a unique equilibrium strategy. This paper provides such
a unique strategy by solving an auxiliary zero-sum diﬀerential game.
In the auxiliary diﬀerential game, L seeks to reach a point opposite
of M at a radius for which their maximum angular speeds are equal
(i.e., the antipodal point). L wishes to minimize the time to reach this
point while M wishes to maximize it. The solution of the auxiliary
diﬀerential game is comprised of a Focal Line, a Universal Line, and
their tributaries. The Focal Line tributaries’ equilibrium strategy for
L is semi-analytic, while the Universal Line tributaries’ equilibrium
strategy is obtained in closed form.

1 Introduction

The Lady in the Lake scenario involves a mobile agent, the Lady, denoted
L, swimming in a circular lake and another agent, the Man (or Monster),
denoted M , whose motion is constrained to the perimeter of the lake. L
seeks to reach the perimeter with maximum angular separation from M
while the latter seeks to minimize the angular separation. L’s swimming
speed is less than M ’s running speed (otherwise the solution is relatively
trivial), however, upon reaching the shore, L can run faster than M .
The scenario ﬁrst appeared in a column in Scientiﬁc American by Martin
Gardner in 1965. This original problem description was later collected in a

∗This paper is based on work performed at the Air Force Research Laboratory (AFRL)
Control Science Center. DISTRIBUTION STATEMENT A. Approved for public release.
Distribution is unlimited. AFRL-2024-0127; Cleared 09 JAN 2024.

1

book [1] and was also posted in a collection of Gardner’s writings [2]. Later,
the scenario was formulated as a zero-sum diﬀerential game and solved as
an example in [3]. Again, the scenario was included as an example in Ba¸sar
and Olsder’s book [4] and an analytical solution was provided therein. Ac-
cording to [4] the scenario also appeared in the Russian translation of Isaacs’
book [5]. Then the scenario was revisited in [6], although, instead of anal-
ysis and geometry, numerical methods were used to approximate a solution
(presumably because an analytical solution already existed for comparison
purposes). These numerical methods were based upon viscosity solutions of
the Hamilton-Jacobi-Isaacs (HJI) partial diﬀerential equation.
More recently, the Lady in the Lake scenario has been reintroduced, in
much the same way as the original, in the magazine Quanta as a mathemat-
ical puzzle [7], [8]. However, in its new incarnation, a twist has been added:
in [7, Puzzle 2] the reader is asked to determine (essentially) the equilibrium
escape time which L seeks to minimize and M seeks to maximize when L
starts in the center of the lake. The readers’ and author’s solutions account
for the possibility of M changing direction in order to foil L’s strategy in an
eﬀort to drive at the true equilibrium solution. However, a full diﬀerential
game treatment of this problem (as well as the more general scenario of any
starting position for L) has not yet been presented and is out of the scope
of the current paper. Nonetheless, [9] analyzed an easier variant of this
problem for which L begins outside the lake and seeks to enter in minimum
time subject to keeping θ, the angle between L and M , non-zero. There
are also several papers on the topic of evading a ﬁnite-range Turret whose
solutions resemble the original Lady in the Lake solution with a few added
subsolutions [10]–[12].
Although the solution to the original Lady in the Lake scenario have
been well-established, several open questions remain (and were mentioned
in [4]). These questions have to do with a particular point in the lake
from which L can guarantee its minimum terminal angular separation. This
point is opposite of M at a radius from the lake’s center for which L and
M ’s maximum angular speeds are equal, henceforth, the antipodal point, or
E. If L were to start under the equilibrium trajectory emanating from E
she’d do best by ﬁrst reaching E and subsequently exiting the lake along
the associated equilibrium trajectory. Therefore, the following questions was
raised:

If L starts at the lake center and knows M ’s current action, show
that L will reach the antipodal point, E. [p. 394, 4, paraphrased]

Some natural extensions to this question then include:

1. How long will it take for L to reach E (i.e., what is the equilibrium,
min max time)?
 2

2. What if L starts from general position (i.e., not just starting at the
center of the lake)?

This paper answers all of these questions, eﬀectively completing the solution
of the Lady in the Lake diﬀerential game by providing a unique strategy
for the players in a large region of the state space for which the canonical
strategy is undeﬁned.
A recent work [13] has sought to address very similar questions. There,
the focus is on ﬁnding the minimum time trajectory for L in the region of the
state space where she has angular speed advantage over M (which is only
a subset of the region for which the canonical strategy for the min max ter-
minal angle game is non-unique/undeﬁned). Ultimately, the authors specify
a nonlinear program which utilizes a general numerical optimization solver
to obtain minimum time trajectory resulting in L maneuvering to E. This
paper builds upon that work by providing a solution which is closed-form
for part of the state space and semi-analytic in the other part.
Following in the footsteps of [3]–[5], the methodology used within this
paper is based upon diﬀerential game theory. In general, obtaining solutions
to diﬀerential games is a diﬃcult endeavour as it involves solving the HJI, a
technique which suﬀers from the curse of dimensionality [14]. For example,
the Homicidal Chauﬀeur Diﬀerential Game (HCDG) has only two states
and two parameters and yet its solution (or, at least, the bulk of it) was the
subject of a PhD dissertation [15] and a multitude of follow-on publications.
This is, in part, due to the abundance and variety of singularities present
in its solution [4]. Fortunately, the Lady in the Lake diﬀerential game has
two states and only one parameter (in its most reduced formulation) and
its solution is far simpler than that of the HCDG. As will be shown, the
solution, presented here, concerning the min max time to reach the point E
contains some singularities of its own. In particular, the solution contains
a Focal Line (FL) – a line which is, itself, an equilibrium trajectory that
has tributary equilibrium trajectories that enter tangentially (c.f., e.g., [16],
[17]). Additionally, the solution also contains a Universal Line (UL) – a line
which, like the FL, is an equilibrium trajectory, but its tributaries do not
enter tangentially. The UL was introduced in the seminal work by Isaacs [5].
The remainder of this paper is summarized as follows. Section 2 contains
a rederivation of the classical Lady in the Lake results. Section 3 presents
all of the new results for the min max time to reach E diﬀerential game. It’s
broken down into a subsection on the FL and its tributaries, Section 3.1, a
subsection on the UL and its tributaries, Section 3.2, and a summary of the
complete solution. Lastly, the paper is concluded in Section 4. Regarding
notation, many symbols are reused in each section and subsection but are
typically deﬁned in a speciﬁc way for that context. For example, the symbol
H is used to denote the Hamiltonian which is deﬁned diﬀerently in the
classical formulation than it is in the min max time formulation.

3

2 The Classical Lady in the Lake Scenario [4]

In this section, the solution given by Ba¸sar and Olsder in [4] is rederived in
detail for the sake of completeness. Consider the state space region

R = {(r, θ) | 0 ≤ r ≤ 1, 0 ≤ θ ≤ π}

where µ < 1 is the speed of L. Without loss of generality, the angular
position of L w.r.t. M is assumed to be in the range θ ∈ [0, π]. The relative
dynamics are
 ˙r = µ cos ψ, r(0) = r0, (1)

˙θ = µ
r sin ψ − ω, θ(0) = θ0, 0 ≤ t ≤ tf , (2)

where (r0, θ0) ∈ R, ψ ∈ [−π, π], and ω ∈ [−1, 1] (all without loss of gener-
ality). The radius of the lake is set to 1 (again, without loss of generality)1.
The cost/payoﬀ functional is

J (r, θ, ψ(·), ω(·)) = Φ (rf , θf ) = θf , (3)

which L wishes to maximize and M wishes to minimize. The terminal
surface is given by φ(r, θ) = r − 1 = 0 (4)

The Value function, if it exists, gives the equilibrium cost/payoﬀ of the
diﬀerential game
 V (r, θ) = max
ψ(·) min
ω(·) θf = min
ω(·) max
ψ(·) θf . (5)

We begin by forming the Hamiltonian

H = λrµ cos ψ + λθ ( µ
r sin ψ − ω) , (6)

where λr and λθ are state adjoint variables. The equilibrium state adjoint
dynamics are given by [18]

˙λr = − ∂H
∂r = λθ µ
r2 sin ψ (7)

˙λθ = 0. (8)

The last equality implies that λθ(t) = λθ∀t ∈ [0, tf ], i.e., that λθ is constant
along the entire equilibrium trajectory. At termination, the state adjoint

1This reduction of the parameter space to just the ratio of agent speeds, µ, can be
accomplished through a scaling of space and time.

4

variables must satisfy [18]

λrf = ∂Φ
∂rf + ν ∂φ
∂rf = ν (9)

λθ = λθf = ∂Φ
∂θf + ν ∂φ
∂θf = 1, (10)

where ν is an additional adjoint variable. The equilibrium heading for L
must maximize the Hamiltonian, which implies

cos ψ∗ = λr√λ2
r + 1
r2 , sin ψ∗ = 1

r√
λ2
r + 1
r2 . (11)

Meanwhile, the equilibrium control for M must minimize the Hamiltonian,
which implies ω∗ = 1. (12)

At termination, the Hamiltonian must satisfy

Hf = − ∂Φ
∂tf − ν ∂φ
∂tf = 0. (13)

Furthermore, since the system is time-autonomous and ∂H
∂t = 0 we have
H = 0∀t.
Evaluating (6) at ﬁnal time and substituting in the equilibrium controls,
(11) and (12), and solving for ν gives

ν = √ 1
µ2 − 1. (14)

Note that ν must be positive in order for ˙rf to be positive, which is necessary
for L to exit the lake. Repeating this step for general time gives

λr = √ 1
µ2 − 1
r2 . (15)

Again, the negative case of the square root can be ruled out since heading
towards the center of the lake is never advantageous along the equilibrium
trajectory. Substituting (15) into (11) gives

cos ψ∗ =
 √
1 − µ2

r2 , sin ψ∗ = µ
r . (16)

Since sin ψ∗ = µ
r , it must be the case that r ≥ µ. That is, the equilibrium
control strategy for L is only deﬁned when r ≥ µ. As noted in [4], L’s
strategy corresponds to heading away from the tangent of the circle of radius
µ and results in a straight line in the non-rotating Cartesian coordinate
system.
 5

Substituting the equilibrium control strategies, (12) and (16), into the
dynamics, (1) and (2), and dividing gives

dθ
dr = − 1
µ
 √
1 − µ2

r2
∫ θf

θ0 dθ = − 1
µ
 ∫ rf

r0
 √
1 − µ2

r2 dr

θf − θ0 = − 1
µ
 [√r2
f − µ2 − µ cos−1 ( µ
rf
 ) − √r2
0 − µ2 + µ cos−1 ( µ
r0
 )] .

(17)

By setting rf = 1 in the above, the Value function is given by

V (r, θ) = θ − √ 1
µ2 − 1 + cos−1 µ +
 √ r2

µ2 − 1 − cos−1 ( µ
r
 ) . (18)

Deﬁne θT = V (µ, π), i.e.,

θT = π − √ 1
µ2 − 1 + cos−1 µ (19)

Note that L can only escape from the point E = (µ, π) if θT > 0 which
implies that µ > µcrit ≈ 0.21723. For the remainder of the paper it is
assumed that L’s speed is above this critical value.
Now, deﬁne the equilibrium trajectory which departs from E and exits
the lake as B. Based on (17) and (19), then,

B(r) = π −
 √ r2

µ2 − 1 + cos−1 ( µ
r
 ) , r ∈ [µ, 1] . (20)

If the state is such that θ < B(r) then θf < θT from (17) and (19). Therefore,
it would be better for L to navigate to the point E and depart along B in
order to achieve θf = θT . Fig. 1 shows the equilibrium trajectories for the
classical solution. Note the large blank area of the state space for which
no unique equilibrium trajectory exists and L is prescribed to swim to the
point E and subsequently take the B trajectory.
The curve B is a barrier surface (in the language of Isaacs [5]). That is,
neither agent can steer the state of the system towards or across the surface
on their opponent’s respective side. For example, if the state (r, θ), is below
B, then L cannot force the state onto B (hence why she is prescribed to
swim to E ﬁrst). Let −→n be a vector that is normal (pointing up and to the
right) to the curve B, −→n = [− dθ
dr 1
]⊤ . (21)

6

0.0 0.2 0.4 0.6 0.8 1.0
0

1

2

3 E
 rθ
r = µ
θ = θT
B
Classical Solution

Figure 1: Equilibrium ﬂowﬁeld for the classical Lady in the Lake diﬀerential game
for µ = 0.3.

A barrier curve is characterized by

min
ω max
ψ
 {
−→n · [ ˙r ˙θ]⊤} = 0. (22)

Expanding this condition gives

min
ω max
ψ − dθ
dr µ cos ψ + µ
r sin ψ − ω = 0,

which implies that the minimizing and maximizing controls are, respectively,
ω = 1 and
 cos ψ =
 dθ
dr√( dθ
dr )2 + 1
r2 , sin ψ = 1

r√( dθ
dr )2 + 1
r2 .

Taking the derivative of (20) and substituting into the above expressions
shows that (22) is indeed satisﬁed. Furthermore, the condition holds for
any curve that is an additive constant w.r.t. B, hence why there is no hope
in L being able to reach B from below.

3 Min-Max Time to Reach the Antipodal Point

In this section, we wish to obtain unique trajectories in the region of the
state space below the barrier, B, that are optimal in some sense. Speciﬁcally,

7

we aim to populate this region with trajectories which reach the point E =
(µ, π) such that the time spent getting there is in equilibrium w.r.t. the two
agents’ control strategies.

3.1 Focal Line

Proposition 1. There is a Focal Line (FL) given by

F = {(r, θ) | 0 < r ≤ µ, θ = π} , (23)

wherein L’s equilibrium control keeps the state of the state of the system on
the line θ = π (i.e., she chooses the heading, ψ, s.t. ˙θ = 0):

sin ψF L = r
µ , (24)

and M ’s equilibrium control is
 ωF L = 1. (25)

Proof. Since r < µ, L needs to increase r → µ. The goal of L is to reach the
point E = (µ, π). Any deviation of θ from π will need to be recovered at some
point along the trajectory in order to end up at E. Also L’s relative control
authority over the θ state is decreasing as she increases r. Thus any deviation
would be best dealt with earlier in the trajectory rather than later. Taking
this argument to the extreme: it is best for L to keep θ = π along the entire
trajectory. Regarding M ’s control, he has some informational advantage in
that, technically, L must know his instantaneous control input in order for
her to implement her singular control. However, if, for example, M were
to switch many times (thereby forcing L to have to guess and possibly be
wrong many times) L could instead choose sin ψ = 0 and head directly
to E, arriving in a shorter time. In other words, M ’s eﬀorts to exploit
his informational advantage are, themselves, easily exploitable. Hence, M
should adopt either ω = 1 or ω = −1 while on the FL, and thus the former
is taken without loss of generality.

Remark 1. The proposed control for L along the FL also keeps the state of
the system on the FL itself, which, of course, is one of the properties which
makes this surface a FL. The other property is that trajectories entering the
FL do so tangentially; this property will be proven later.

Substituting the FL controls, (24) and (25), into the dynamics, (1), gives

˙r = µ
√
1 − r2

µ2

= √µ2 − r2.

8

This expression can be used to obtain the amount of time spent on the FL
until the point (r, θ) = (µ, π) is reached as follows.

˙r = dr
dt = √µ2 − r2

dr
√µ2 − r2 = dt

dr

µ√1 − r2
µ2 = dt

Let x ≡ r
µ , and thus, µdx = dr:
 dx
√1 − x2 = dt

Finally, this equation can be integrated; on the LHS the integration bounds
are x = s
µ to 1 (which corresponds to r starting at s and going to µ), and
the RHS just becomes the time spent on the FL, ts:
∫ 1

s/µ
 dx
√1 − x2 = ∫ ts

0 dt = ts

=⇒ sin−1 (x)∣
∣1
s/µ = ts

π
2 − sin
−1 ( s
µ
 ) = ts

With the time spent on the FL in hand, the next step is to characterize
the FL tributaries, which are those equilibrium trajectories that merge onto
the FL. In order to do so, the game is reformulated as a game which begins
from a general initial condition and ends on the FL.

3.1.1 Equilibrium Heading for FL Tributaries

The terminal manifold is

M = {(r, θ) | 0 < r ≤ µ, θ = π} . (26)

M is also the zero-level set of the function

φ(r, θ) = θ − π. (27)

For the remainder of the paper, s is used to denote the value of r wherein
the state enters the FL. Thus, for the analysis concerning FL tributaries

9

rf = s and θf = π The terminal cost is the time for L to proceed along the
line θ = π from r = s to r = µ:

Φ(s) = π
2 − sin−1 ( s
µ
 ) . (28)

The performance functional is the total time taken by L to reach the point
E ≡ (µ, π) (by way of reaching (r, θ) = (s, π) ﬁrst)

J(ψ(·)) = Φ(s) + ∫ tf

0 1 dt, (29)

which L wishes to minimize. The Hamiltonian of the system is

H = λrµ cos ψ + λθ ( µ
r sin ψ − ω) + 1, (30)

where λr and λθ are adjoint variables associated with the r and θ states,
respectively. The value of the Hamiltonian at terminal time is given by [18]

Hf = − ∂Φ
∂t − ν ∂φ
∂t = 0. (31)

Since ∂H
∂t = 0 and the system’s dynamics are time-autonomous we have
dH
dt = 0 and thus H (t) = 0∀t ∈ [0, tf ]. The value of the adjoint variables
at terminal time are given by [18]

λrf = ∂Φ
∂s + ν ∂φ
∂s = −1
√µ2 − r2
f (32)

λθf = ∂Φ
∂θf + ν ∂φ
∂θf = ν, (33)

where ν is an additional adjoint variable. The optimal adjoint dynamics are
given by [18]
 ˙λr = − ∂H
∂r = −λθ µ
r2 sin ψ∗ (34)

˙λθ = − ∂H
∂θ = 0. (35)

Since ˙λθ = 0 we have that λθ = ν ∀t ∈ [0, tf ].
The equilibrium action for L is one that minimizes the Hamiltonian, ψ∗ =
arg minψ H , and therefore the vector [cos ψ∗ sin ψ∗] should be antiparallel
with the vector [
λr ν
r ]

cos ψ∗ = −λr√λ2
r + ν2
r2 , sin ψ∗ = −ν

r√
λ2
r + ν2
r2 (36)

10

Similarly, the equilibrium action for M is one that maximizes the Hamilto-
nian, ω∗ = arg maxω H , hence,

ω∗ = − sign ν. (37)

Assuming ω > 0, substituting the equilibrium controls into the Hamiltonian,
(30), gives
 H ∗ = −µ
√
λ2
r + ν2

r2 − ν + 1 = 0

=⇒
 √
λ2
r + ν2

r2 = 1 − ν
µ . (38)

Substituting the terminal value of λr, (32), and the terminal value of r (i.e.,
s) into the above and solving for ν gives

ν = −s2

µ2 − s2 , (39)

which is negative since s < µ along the FL. Substitution into (37) conﬁrms
that, indeed, ω is positive.
Substituting (36) and (39) into (30), evaluating at a general time, and
solving for λr gives
 λr = ± 1
µ2 − s2
 √
µ2 − s4

r2 . (40)

From (32) it’s clear that, at terminal time, λr < 0 which from (36) and (1)
implies that ˙rf > 0. Also, (40) shows that λr = 0 when r = s2
µ . Therefore, it
must be the case that λr (and, consequently, ˙r) changes sign once the system

passes through r = r2
f
µ since sign( ˙λr) = − sign(sin ψ∗) = −1 from (34), (36)
and (39).

Lemma 1. The equilibrium heading for L along FL tributaries is given by

cos ψ∗ = ±
√

1 − s4

µ2r2 , sin ψ∗ = s2

µr . (41)

Proof. Substitution of (38) and (39) into (36) gives the above expressions.

Lemma 2. The equilibrium control for M along FL tributaries is given by

ω∗ = 1. (42)

Proof. The result follows directly from (37) and (39).

Lemma 3. The equilibrium FL tributary trajectory is a straight line in the
global Cartesian frame.
 11

Proof. The proof follows the same steps as the proof for Lemma 2 in [9] and
is thus omitted for brevity.

Lemma 4. The FL tributaries enter the FL tangentially.

Proof. Evaluating ˙θ from (2) at terminal time (i.e., r = s) and substituting
in the equilibrium controls, (41) and (42), gives

˙θ∗
f = µ
s
 ( s2

µs
 ) − 1 = 0.

The FL, itself, is a line of constant θ, hence the result holds.

3.1.2 Equilibrium Flowﬁeld

Now, the equilibrium heading for L can be substituted into ˙r, (1), to obtain
˙r∗. However, the sign of cos ψ∗ is not known directly except at ﬁnal time
(wherein cos ψ∗, ˙r > 0). Therefore, it is useful to consider the retrograde
equation for r (denoted with a circle instead of a dot, i.e., ˚r = − ˙r) in order
for the initial condition to be fully speciﬁed:

˚r∗ = ± µ
r
 √
r2 − s4

µ2 , r(0) = s, ˚r∗(0) < 0. (43)

As mentioned previously, the sign of ˚r∗ is governed by the sign of λr which
starts (in retrograde time) negative and becomes positive if r reaches the
value s2
µ . Let the retrograde time be denoted by τ such that τ = 0 corre-
sponds to t = tf . Rewriting the above expression,

dr
dτ = ± µ
r
 √
r2 − s4

µ2 (44)

∫ r

s
 r
√
r2 − s4
µ2 dr = ± ∫ τ

0 µ dτ (45)

√
r2 − s4

µ2
 ∣
∣
∣
∣
∣
r

s = ±µτ (46)

√
r2 − s4

µ2 −
 √
s2 − s4

µ2 = ±µτ (47)

=⇒ r(τ ) = √
s2 − 2τ s√µ2 − s2 + µ2τ 2 (48)

Deﬁne the time when r = s2
µ (i.e., when λr and ˚r change sign) as ¯τ ; this

time is obtained by solving for τ in the negative version of (47) with r = s2
µ :

¯τ = s
µ
 √
1 − s2

µ2 . (49)

12

Note that this time also corresponds to the time at which L is is closest to
the center of the lake along the FL trajectory, i.e., minτ r(τ ) = r(¯τ ).
Similarly, for θ, after substituting (41) and (42) into (2) and changing
to retrograde time we have

˚θ∗ = 1 − s2

r2 , θ(0) = π. (50)

Rewriting the above expression and substituting in r(τ ) from (48),

dθ
dτ = 1 − s2

s2 − 2τ s√µ2 − s2 + µ2τ 2 (51)

∫ θ

π dθ = ∫ τ

0 dτ − s2 ∫ τ

0
 1

s2 − 2sτ √µ2 − s2 + µ2τ 2 dτ (52)

θ − π = τ − tan−1 ( µ2

s2 τ −
 √ µ2

s2 − 1

)
 − tan−1 (√ µ2

s2 − 1

)
 . (53)

The following is stated in order to summarize the results of this section.

Lemma 5. The equilibrium ﬂowﬁeld for FL tributaries, parameterized by
the entry point on the FL, s, is given by

r(τ ; s) = √s2 − 2τ s√µ2 − s2 + µ2τ 2,

θ(τ ; s) = π + τ − tan−1 ( µ2

s2 τ −
 √ µ2

s2 − 1

)
 − tan−1 (√ µ2

s2 − 1
)
 . (54)

3.1.3 Computation of the FL Entry Point

The equilibrium ﬂowﬁeld expressions derived in the previous section are
useful for ﬁlling a region of the state space with equilibrium trajectories by
computing (r(τ ), θ(τ )) starting from points along the FL. However, starting
(in forward time) from a general position (r, θ), the equilibrium heading of L
is unknown as it depends on s. This section describes the process by which
s may be computed.
There are two possible cases depending on L’s initial condition: 1) L’s
equilibrium heading has some component of towards the center of the lake
and 2) L’s equilibrium heading has a component of velocity away from the
center of the lake until she reaches the FL. Consider Case 1. Let the time
of arrival of L to the entry point of the FL, (s, π) be

tL(s) = 1
µ
 (√

r2 − s4

µ2 +
 √
s2 − s4

µ2
 )
 , (55)

which is derived based on the fact that L’s trajectory is a straight line in

the Cartesian frame (per Lemma 3) and is tangent to a circle of radius r2
f
µ .

13

M ’s time of arrival to the position that is antipodal to L is given by the
sum of angles traversed

tM (s) = θ + cos−1 ( s2

µr
 ) + cos−1 ( s
µ
 ) − π. (56)

Deﬁne the function δ(s) = tL(s)−tM (s) which is the diﬀerence of the agents’
respective times of arrival. The equilibrium entry point onto the FL is thus
the smallest possible root of this function, i.e.,

s∗ = min s s.t. δ(s) = 0, s ∈ (0, µ] . (57)

The solution may be obtained numerically as the above expression does not
admit a closed-form solution.
Case 2 is similar to Case 1 but with tL and tM given, respectively, by

tL(s) = 1
µ
 (√
s2 − s4

µ2 −
 √
r2 − s4

µ2
 )
 , (58)

tM (s) = θ − cos−1 ( s2

µr
 ) + cos−1 ( s
µ
 ) − π. (59)

In lieu of a more sophisticated method with which to determine whether the
initial condition, (r, θ), is in Case 1 or Case 2, the former should be assumed
ﬁrst. If no solution to (57) can be found, then Case 2 should be assumed.

3.2 Universal Line

Proposition 2. There is a Universal Line (UL) given by

U = {(r, θ) | 0 ≤ r ≤ 1, θ = 0} , (60)

wherein L’s equilibrium control strategy is to head directly to the center of
the lake and M does not move, i.e.,

cos ψU L = −1, ωU L = 0. (61)

Proof. When θ = 0, M has no incentive to move the state of the system
to some non-zero θ since doing so increases L’s angular separation (which
is, ultimately, the thing that M seeks to reduce). If L had an angular
component of velocity then θ would immediately become non-zero. When
θ = 0, the easiest way for L to drive θ → π is to pass through the origin.

Just as in the section on obtaining equilibrium controls for FL tributaries,
the game is reformulated as a game which begins from a general initial
condition and ends on the UL.
 14

3.2.1 Equilibrium Heading for UL Tributaries

The terminal manifold is the set of states where θ = 0, i.e.,

M = {(r, θ) | 0 < r ≤ 1, θ = 0} , (62)

which is also the zero-level set of the function

φ(r, θ) = θ. (63)

The terminal cost is the time for L to reach the origin along the UL under
the proposed UL strategy, (61):

Φ(rf , θf ) = rf
µ . (64)

In principle, one may consider the total time to ﬁnish out the original game
by adding in the time spent along the FL, starting from (0, π) and going to
(µ, π), however that is not necessary as that time will be the same for all
UL tributaries. The performance functional is the sum of the time taken to
reach the UL and then reach the origin (i.e., (29)). The Hamiltonian is the
same as in (30). Similarly as before, the equilibrium Hamiltonian is zero for
all time, and the equilibrium heading is given by (36) resulting in (38). The
terminal adjoint values are

λrf = ∂Φ
∂rf + ν ∂φ
∂rf = 1
µ (65)

λθf = ∂Φ
∂θf + ν ∂φ
∂θf = ν. (66)

Evaluating (38) at ﬁnal time results in
√ 1
µ2 + ν2

r2
f = 1 − ν
µ . (67)

Solving this expression, algebraically, for ν yields ν = 2r2
f
r2
f −µ2 which goes to

inﬁnity as rf → µ; additionally the sign of ν changes depending on whether
rf ≷ µ. Fortunately, the solution ν = 0 is valid for all rf , µ ∈ [0, 1].

Lemma 6. The equilibrium heading for L along UL tributaries is given by

cos ψ = −1. (68)

Proof. The result follows from the preceding analysis. Ultimately, L must
end at the center of the lake and thus the θ state bears no importance while
L is en route. Therefore, the fastest way for L to reach the center of the
lake is a straight line path, which is achieved with ψ = π.

Note that, since ν = 0, M ’s control disappears from the Hamiltonian
in (30) and therefore every value ω ∈ [−1, 1] is equally optimal.

15

3.2.2 Equilibrium Flowﬁeld

In contrast to the FL tributaries, the ﬂowﬁeld for the UL tributaries is
simple. Since M ’s equilibrium control is undeﬁned on the UL tributaries,
we adopt a value of ω∗ = 1.

Lemma 7. The equilibrium ﬂowﬁeld for UL tributaries is given by

r(τ ) = µτ, r(0) ∈ [0, 1)

θ(τ ) = τ, θ(0) = 0. (69)

A direct result of Lemma 7 is that UL tributaries only exist when θ ≤ r
µ .
The interpretation is that UL tributaries exist when M is close enough to L
so as to be able to close their angular separation prior to the latter reaching
the center of the lake.

3.3 Full Solution

The following result pieces together the two types of trajectories covered in
the previous section.

Lemma 8. The line segment

P = {
(r, θ) | 0 ≤ r ≤ 1, θ = r
µ
 } (70)

partitions the state space into two regions: one where FL tributaries exist
and are optimal and one where UL tributaries exist and are optimal. That
is, the two regions are mutually exclusive.

Proof. It was shown previously, in Lemma 7, that UL tributaries exist below
P. The remainder of the proof focuses on showing that FL tributaries exist
above P, that is, for θ > µ
r . Consider the FL tributary for which rf → 0;
this is the most limiting case for FL tributaries as the other endpoint of F
(where r = µ) corresponds to already being at the desired point (i.e., the
trajectory is the single point (r, θ) = (µ, π)). From (43) and (50) we have

lim
rf →0˚r∗∣
∣
∣
r>0 = + µ
r
 √

r2 − 04

µ = µ

lim
rf →0 ˚θ∗∣
∣
∣
r>0 = 1 − 02

r2 = 1

These retrograde dynamics result in a line that is parallel to the partition P
and lies arbitrarily close to it since 0 < rf ≪ 1. Two remaining properties
are needed in order for the result to hold: 1) that the FL tributaries do not
cross one another (and thus no FL tributary crosses below P as a result of
the above analysis), and 2) that the FL tributaries ﬁll the region of the state
space above P. Both of these properties will be veriﬁed, graphically, with
an example.
 16

Based on all of the preceding results of this section, the following theorem
summarizes the solution of the min-max time game.

Theorem 1. The solution to the zero-sum diﬀerential game of time to reach
the antipodal point E is given by the following equilibrium control strategies
and associated Value function.

(cos ψ∗, sin ψ∗) =
 




(√1 − r2
µ2 , r
µ ) if θ = π,

(−1, 0) if θ ≤ r
µ ,
(
±
√
1 − r4
f
µ2r2 , r2
f
µr
 )
 otherwise.
 (71)

ω∗ =
 




1 if θ > r
µ
0 if θ = 0
undef. otherwise,
 (72)

t∗
f =
 



 π
2 − sin−1 ( r
µ ) if θ = π,

π
2 + r
µ if θ ≤ r
µ ,

π
2 − sin−1 ( s
µ ) + tL(s), otherwise,
 (73)

where s is the solution of (57) and tL(s) is given by (55) or (58) depending
on which case applies to the current state as described in Section 3.1.3. Note
that the corresponding case determines the sign of cos ψ∗ as well.

Remark 2. One may verify that the equilibrium control strategies satisfy the
Hamilton-Jacobi-Isaacs (HJI) equation everywhere via direct substitution.
However, this is true by construction since, in this case, the Hamiltonian is
equivalent to the HJI and the control strategies are derived directly from
the former.

Fig. 2 shows the relative state space ﬁlled with equilibrium trajectories.
Solutions to the classical game (i.e., the min-max angular separation when
L reaches r = 1) exist above the barrier, B. It is assumed that L would
utilize the classical strategy to exit the lake, otherwise, she should swim to
E as quickly as possible and then exit the lake along the barrier, B.

4 Conclusion

Although the classical Lady in the Lake scenario has been solved for quite
some time, the question of what, speciﬁcally, to do “under” the barrier curve
was open. This paper has addressed that question by providing the min max
time and associated equilibrium strategies for L to reach the antipodal point.
Subsequent to reaching the antipodal point, L then continues on to reach the
shore and obtain the equilibrium terminal angular separation. Traditional

17

0.0 0.2 0.4 0.6 0.8 1.0
0

1

2

3 E
 rθ
r = µ
θ = θT
B
FL
UL
Tributary Partition
Classical Solution

Figure 2: Equilibrium trajectories of the complete Lady in the Lake game with
µ = 0.3.
 s2
µ
 µ 1

L0
 Lf

r
 s M0

Mf
 (a) Case 1
 s2
µ
 µ 1
L0
 Lf

s M0

Mf

(b) Case 2

Figure 3: Focal Line trajectories starting from the tributaries in the non-rotating
Cartesian coordinate system. In (a), L initially heads towards the tangent of the
circle of radius s
2
µ (Case 1), while in (b) L only heads away from the tangent (Case
2). Open markers indicate initial positions, triangles designate positions at the
moment the FL is reached, and closed markers indicate terminal positions.

18

diﬀerential game theory methods have been used to obtain the solution of the
min max time to reach the antipodal point game. Interestingly, its solution is
made up of two singular surfaces and their tributaries. The approach taken
in this paper will serve as a stepping stone to address the more diﬃcult game
of min max time to escape (i.e., similar to the problem posed in [7]).

References

[1] M. Gardner, “Mathematical carnival - from penny puzzles, card shuf-
ﬂes and tricks of lightning calculators to roller coaster rides into the
fourth dimension,” 1975.

[2] M. Gardner, “Lady in lake (1965),” in Martin Gardner Papers (SC0647),
D. Hartwig and J. Johnson, Eds., box 15, folder 11, Stanford, Cali-
fornia: Dept. of Special Collections and University Archives, Stanford
University Libraries, 2008.

[3] J. V. Breakwell, “Lecture notes,” in Diﬀerential Games and Applica-
tions, P. Hagedorn, H. W. Knobloch, and G. J. Olsder, Eds., Berlin,
Heidelberg: Springer Berlin Heidelberg, 1977, pp. 70–95, isbn: 978-3-
540-37179-3.

[4] T. Ba¸sar and G. J. Olsder, “Chapter 8: Pursuit-evasion games,” in
Dynamic Noncooperative Game Theory, ser. Mathematics in Science
and Engineering, vol. 160, London: Elsevier, Jan. 1, 1982, pp. 344–398.
doi: 10.1016/S0076-5392(08)62960-4.

[5] R. Isaacs, Diﬀerential Games: A Mathematical Theory with Applica-
tions to Optimization, Control and Warfare. New York: Wiley, Jan. 1,
1965, isbn: 9780486406824.

[6] M. Falcone, “Numerical methods for diﬀerential games based on par-
tial diﬀerential equations,” International Game Theory Review, vol. 08,
pp. 231–272, 02 Jun. 1, 2006. doi: 10.1142/S0219198906000886.

[7] P. Mutalik, “Can math help you escape a hungry bear?” Quanta Mag-
azine, Jun. 2021.

[8] P. Mutalik, “Math can, in theory, help you escape a hungry bear,”
Quanta Magazine, Aug. 2021.

[9] A. Von Moll, M. Pachter, D. Shishika, and Z. Fuchs, “Circular tar-
get defense diﬀerential games,” Transactions on Automatic Control,
vol. 68, pp. 4065–4078, 7 Oct. 5, 2022. doi: 10.1109/TAC.2022.3203357.

[10] M. Ivanov and E. Maslov, “A problem of avoidance of a rotating seg-
ment,” Computers & Mathematics with Applications, vol. 26, no. 6,
pp. 67–75, 1993. doi: 10.1016/0898-1221(93)90118-F.

19

[11] A. A. Galyaev and E. P. Maslov, “Evading a rotating detection zone on
a plane,” en, Journal of Computer and Systems Sciences International,
vol. 52, pp. 377–385, 3 May 2013. doi: 10.1134/s1064230713030076.

[12] A. Von Moll, Z. Fuchs, D. Shishika, D. Maity, M. Dorothy, and M.
Pachter, “Turret escape diﬀerential game,” Journal of Dynamics and
Games, Sep. 1, 2023, Presented at the 19th ISDG. doi: 10.3934/jdg.2023012.

[13] Y. Wang, “Solving the lady in the lake problem and its fastest optimal
strategy,” Bachelor’s Thesis, Pennsylvania State University, 2022.

[14] P. Bernhard, “Pursuit-evasion games and zero-sum two-person diﬀer-
ential games,” in Encyclopaedia of Systems and Control, J. Bailleul
and T. Samad, Eds. Springer, Jan. 1, 2014, pp. 1103–1109.

[15] A. W. Merz, “The homicidal chauﬀeur - a diﬀerential game,” Ph.D.
dissertation, Stanford, Jan. 1, 1971.

[16] A. Melikyan and P. Bernhard, “Geometry of optimal paths around
focal singular surfaces in diﬀerential games,” Applied Mathematics and
Optimization, vol. 52, no. 1, pp. 23–37, Jun. 2005, issn: 1432-0606. doi:
10.1007/s00245-004-0816-8.

[17] J. V. Breakwell and P. Bernhard, “A simple game with a singular focal
line,” en, Journal of Optimization Theory and Applications, vol. 64,
pp. 419–428, 2 Feb. 1990. doi: 10.1007/bf00939457.

[18] A. E. Bryson and Y.-C. Ho, Applied Optimal Control: Optimization,
Estimation and Control. New York, USA: Taylor and Francis Group,
1975. doi: 10.1201/9781315137667.

20
