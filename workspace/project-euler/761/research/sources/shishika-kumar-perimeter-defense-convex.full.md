<!-- source: https://arxiv.org/pdf/1909.03989 | converted from PDF -->

Perimeter-defense Game on Arbitrary Convex Shapes

Daigo Shishika a, Vijay Kumar b

aDepartment of Mechanical Engineering, George Mason University, USA.

bGRASP Lab, University of Pennsylvania, USA.

Abstract

This paper studies a variant of multi-player reach-avoid game played between intruders and defenders. The intruder team
tries to score by sending as many intruders as possible to the target area, while the defender team tries to minimize this score
by intercepting them. Speciﬁcally, we consider the case where the defenders are constrained to move on the perimeter of the
target area. Since it is challenging to directly solve the multi-player game due to the high dimensionality of the joint state
space, we leverage the solutions to smaller scale problems. First, we solve the one vs. one game, for which existing works
either rely on numerical approaches or make simplifying assumptions (e.g., circular perimeter, or equal speed). This paper
accommodates target areas with any arbitrary convex shapes and provides analytical solution which lends itself to a useful
geometric interpretation. We also provide a detailed discussion on the optimality of the derived strategies. Secondly, we solve
the two vs. one game to introduce a cooperative pincer maneuver, where a pair of defenders team up to capture an intruder
that cannot be captured by either one of the defender individually. Finally, we introduce how the aforementioned building
blocks are used in three diﬀerent assignment-based defense strategies.

Key words: Pursuit evasion game, Reach avoid game, Cooperative control

1 Introduction

Maintaining perimeter surveillance and security is a
complex problem given that it has become practical to
deploy autonomous agents in large numbers. Various
approaches to counter intrusions by unmanned vehicles
have been studied including patrolling strategy [34], in-
trusion detection based on behavior rules [31], and GPS
spooﬁng to manipulate the behavior of the agents [23].

When evasive targets need to be detected, intercepted,
or surrounded, the scenarios are often formulated as
pursuit-evasion games (PEGs) [8,17,43]. If it is formu-
lated as a game of kind, we ask which initial conﬁgura-
tion leads to capture (or evasion), and what pursuit (or
evasive) strategy guarantees that. If it is formulated as a
game of degree, we ﬁnd the optimal strategy for a given
objective function, e.g., time to capture.

The game becomes more complex when the evader has
another objective, such as to reach a target. A version

⋆ We gratefully acknowledge the support of ARL grant
ARL DCIST CRA W911NF-17-2-0181. Corresponding au-
thor: D. Shishika.
Email addresses: dshishik@gmu.edu (Daigo Shishika),
kumar@seas.upenn.edu (Vijay Kumar).
 of this problem is called the target-attacker-defender
(TAD) game [15,26,36]. In a TAD game the attacker aims
to capture the target while avoiding being captured by
the defender, and the defender tries to defend the target
by intercepting the attacker. In [26] the defender could
save the target by reaching it before the attacker, which
led to a rendezvous type strategy.

Another formulation focuses on the case where the tar-
get is a region in the game space and is no longer treated
as an agent. The two-player version of the game (one de-
fender vs. one attacker) was ﬁrst introduced by Isaacs
as the target-defense game [22]. This game is also called
the reach-avoid game [11,50,51], and it has been stud-
ied in many diﬀerent variants including multi-player sce-
nario [6,20,47,48,49] and coast-line guarding or boarder
defense [16,19,44].

This paper considers the perimeter defense game, which
is a variant of the reach-avoid game played between in-
truders and defenders [39,41]. The intruder team tries
to score by sending as many intruders as possible to the
target area, while the defender team tries to minimize
this score by intercepting them. A speciﬁc assumption
made in this paper is that the defenders are constrained
to move on the perimeter. Such assumption is motivated
by the scenarios where the target region acts as an ob-arXiv:1909.03989v3  [eess.SY]  1 May 2021
stacle that the defenders cannot move through ( e.g., de-
fending a perimeter of a building using ground vehicles).

Various solution methods have been proposed to solve
the PEGs introduced thus far. In general the approaches
can be divided into two types: the diﬀerential game for-
mulation and the explicit policy method [26]. The former
obtains the strategies and the winning regions by solv-
ing a Hamilton-Jacobi-Issacs (HJI) partial diﬀerential
equation (PDE), while the latter analyzes the outcome
of the game by prescribing a strategy to the players.

The diﬀerential game formulation has been successfully
utilized for relatively simple problems that allow analyt-
ical solution to the HJI PDEs [3,22,29] and other prob-
lems with low dimensional state space for which the HJI
PDEs can be numerically solved [6,12]. The strength of
this approach is that the optimality of the derived strate-
gies are ensured by construction. The down side is the
curse of dimensionality, which makes the HJI PDEs in-
tractable for problems with large state space. There are
several papers on computing approximate optimal so-
lutions for pursuit-evasion games that also bypass the
computational intractability of solving HJI equations ex-
plicitly [27,28,42].

The explicit policy method is widely used for multi-
player PEGs that require scalability in the number of
agents. For scenarios involving multiple pursuers, spe-
ciﬁc control strategies have been proposed with the anal-
yses on their performance guarantees. Approaches based
on Voronoi tessellation and area minimization can be
found in various works [21,35,52]. A variant of such work
proposes a so called relay pursuit to improve the overall
eﬃciency by selecting one pursuer to actively go after
the evader [2], and it has been applied to a more com-
plex scenario [38]. A behavior called the cyclic pursuit
uses a chain of pursuers to encircle a target [4,24]. For
a non-adversarial scenario where there is no evasive ma-
neuver, the problem is formulated as the vehicle-routing
problem [1]. Evasive maneuvers have also been consider
in the scenario with one pursuer and multiple evaders
[14,37].

The problem becomes more challenging when there are
multiple pursuers and multiple evaders. The underly-
ing question is “which pursuer should go after which
evader?” In [35], a Voronoi-tessellation based approach
was used to directly obtain the desired direction of mo-
tion. In [30], a task allocation approach was proposed,
where the solution to the multiple pursuers vs. one
evader problem was used to assign a unique pursuer
for each evader so that capture in minimum time is
guaranteed.

Speciﬁcally for the reach-avoid game played between
multiple defenders and multiple attackers, [6] approxi-
mated the multi-player game as a combination of two-
player games. In contrast to a more conventional PEG
 that considers the time of capture, we must consider
whether the given pursuer can capture the attacker be-
fore it reaches the target. To obtain this feasibility (cap-
turability) information, the solutions to the two player
games (strategies and winning regions) were obtained by
numerically solving the associated HJI PDE [6,7]. As an
advantage of using a numerical approach, the authors
were able to handle complex environments with obsta-
cles. These solutions were used to formulate the design
of defense policy as an assignment problem.

Following the approach taken in [6,7], this paper starts
by identifying the solution to the two-player game: the
game played between one defender and one intruder. Al-
though the two-player game has been solved either nu-
merically [6,7], or under restricted assumptions (circu-
lar perimeter or equal speed) [39], we analytically solve
the problem for arbitrary convex shapes. This is enabled
due to the constraint that the defender moves on the
perimeter.

Our analytical solution has several advantages over the
numerical one. First, it lends itself to convenient geomet-
ric interpretations such as approach angle. In addition,
while the numerical approach requires us to compute the
solution oﬄine and store the data (i.e., a look up table
that gives control inputs from the current positions), an-
alytical approach eﬃciently computes the control input
online, and thus requires much less memory.

In addition, the derived solution exhibits an interest-
ing contrast to the solutions based on dominance region,
which was used in the original work by Isaacs [22] and
also in [32]. The intruder-dominated region contains all
the points that the intruder can reach ﬁrst regardless of
the defender’s strategy [32]. One can conclude that the
intruder can successfully reach the target/perimeter if
the intruder-dominated region intersects the target re-
gion. However, our analysis shows that such condition
is only suﬃcient and not necessary in the perimeter de-
fense game.

We also extend the existing assignment method by incor-
porating a cooperative defense performed by two defend-
ers. To this end, we analytically solve the game played
between two defenders and one intruder. Then the so-
lution to this two vs. one game is incorporated in the
extended assignment policy.

The main contributions of the paper are (i) the solution
to the one vs. one game; (ii) the solution to the two vs.
one game that shows the beneﬁt of defender cooperation;
and (iii) the analysis on the optimality of the derived
strategies. These results are essential building blocks to
solve the game played between multiple defenders and
multiple intruders [41]. Finally, we also present and dis-
cuss three diﬀerent assignment-based defense policies
that utilize the aforementioned results.

2

In our previous work [39] the perimeter-defense game
was solved on a circular perimeter with a formulation
that is not extensible to general shapes. This paper uses
a formulation that can treat any convex shapes including
the circular perimeter. While the extension to polygonal
perimeter was discussed in [39], the result was limited to
the case where the defender and the intruder have the
same speed limits, which allowed us to simplify the anal-
ysis. This paper ﬁlls the existing gap by accommodating
a more general case where the defender has any speed
that is equal or higher than the intruder. Finally, the
discussion of the payoﬀ functions, for which the derived
strategies are optimal, has not been published before.

The paper is organized as follows. Section 2 formulates
the problem. Section 3 solves the game played by one
defender and one intruder. Section 4 introduces the co-
operative aspect by solving the game played by two de-
fender and one intruder. Section 5 proposes the defender
team strategy using the results of one vs. one and two
vs. one games. Section 6 presents the numerical results.

2 Problem formulation

This section formulates the reach-avoid game for de-
fenders constrained on a perimeter. The target T ⊂ R2
is assumed to be a convex region on a plane, and its
perimeter is given by an arc-length parameterized curve
γ : [0, L) → ∂T , where L denotes the perimeter length. 1

We use s ∈ [0, L) to denote the arc-length position on
the curve measured in counter-clockwise (ccw) direction.
The tangent vector of the curve at s is denoted by

T (s) ≜ dγ(s)
ds .

For any two points/vectors in R2 we denote the relative
vectors using xa )b ≜ xb − xa,

and the unit vectors using ˆx = x
∥x∥ . The arc-length from
point sa to sb on the curve in ccw direction is denoted by

sa )b ≜ (sb − sa) mod L,

for example, sa )b + sb )a = L. The segment starting
from sa and ending at sb in ccw direction is denoted by
[sa, sb] ≜ {sx | sa )x ≤ sa )b}. We use (sa, sb) when the
endpoints are not included.

A set of ND defenders {Di}ND
i=1 are constrained to move

1 In case the target is concave, the results of this paper can
be applied by taking the convex hull of the original region and
by deploying defenders to protect this virtual target region.
 on the perimeter. 2 The position of the ith defender is
described by sDi or xDi = γ(sDi ). The defender’s con-
trol input is the signed speed: ˙sDi = ωDi or ˙xDi =
ωDiT (sDi) with the constraint |ωDi| ≤ 1.

A set of NA intruders {Aj}
NA
j=1 have ﬁrst-order integrator
dynamics in R2. The control inputs are the velocities;
˙xAi = uAi with the constraint ∥uAi∥ ≤ ν. It is assumed
that the defender is at least as fast as the intruder: 3

ν ∈ (0, 1]. (1)

This is a generalization of the case with ν = 1 studied
in [39] and removes some simpliﬁcations (see Sec. 3.4).

We assume that each player has access to the current
state and the speed ratio ν. However, the players do not
know the instantaneous control action of the opponent.

In a microscopic view, an intruder Ai scores if it reaches
the target (xAi ∈ ∂T ) without being captured by the
defenders. We use zero distance to deﬁne capture: i.e.,
∥xA − xD∥ = 0, however, the extension to the case with
non-zero capture radius is also straightforward [40]. The
defender moves on the perimeter to either intercept the
intruder or prevent it from scoring indeﬁnitely.

As the building blocks to analyze the multi-player game,
we solve the game played by one defender and one in-
truder, and also by two defenders and one intruder.

Problem 1: Find the barrier surface [22] that divides
the state space into intruder-winning and defender-
winning conﬁgurations. In each region, what are the
strategies to be used by the players?

In a macroscopic view, let Q ∈ N denote the number of
intruders that reach the perimeter. The intruder team
maximizes Q while the defender team minimizes it.

Problem 2: Given an initial conﬁguration of the game
and the speed ratio ν, what are the upper and lower
bounds on the score Q, and what are the associated team
strategies to ensure that bound?

We address these problems in the following sections.

2 This assumption is motivated by various scenarios, for
example, in which ground defenders are deployed to protect
a building that they cannot move through.
3 The case with faster intruders (i.e., ν > 1) requires a
separate treatment and is a subject of ongoing work. It is
easy to see that if ν > 1, and also if the capture is deﬁned
by zero distance, then the intruder can always win.

3

(a) (b)

stan,L

<latexit sha1_base64="29xqLyCFYAvt0SjQIZLKFWWzMEk=">AAACYnicbVDLahRBFK1pX7F9ZcxSF42D4EKG7iSgqxBw48JFBCcJTLfDrerbSZF6NFW3NUPR/+E2+Sv3fojVM7MwiRcKDueee+pweKukpzz/PUru3X/w8NHW4/TJ02fPX2yPXx572zmBM2GVdaccPCppcEaSFJ62DkFzhSf84tOwP/mBzktrvtGyxUrDmZGNFECR+u4XJeElBQLz/ku/2J7k03w12V1QbMCEbeZoMR4dlLUVnUZDQoH38yJvqQrgSAqFfVp2HlsQF3CG8wgNaPRVWMXus7eRqbPGuvgMZSv234sA2vul5lGpgc797d1A/m8376j5WAVp2o7QiPVHTacystnQQVZLh4LUMgIQTsasmTgHB4JiU2la1tiUugnl4Mybfk1wH0puVT0ksqpPb6YRIlbgo9TgT2G1BlOHsuPg+nlRRWRqdGtRdIlsmBR99IiNF7f7vQuOd6fF3nT36/7kcH/T/RZ7xd6wd6xgH9gh+8yO2IwJ5tgvdsWuR3+SNBknO2tpMtrc7LAbk7z+C5xgubE=</latexit> stan,R

<latexit sha1_base64="t+6Sp39lTtd4k5NAYLKghNDaNe8=">AAACYnicbVDLbtRAEJw1r2BeWXKEg8UKiQNa2UkkOEWRuHAMiE0irc2qZ9xORpmHNdOGrEb+D67wV9zzIRnv7oEktDRSqbq6plS8VdJTnv8dJffuP3j4aOtx+uTps+cvtscvj73tnMCZsMq6Uw4elTQ4I0kKT1uHoLnCE37xadif/EDnpTXfaNlipeHMyEYKoEh994uS8JICgXn/tV9sT/JpvprsLig2YMI2c7QYjw7K2opOoyGhwPt5kbdUBXAkhcI+LTuPLYgLOMN5hAY0+iqsYvfZ28jUWWNdfIayFfvvRQDt/VLzqNRA5/72biD/t5t31HysgjRtR2jE+qOmUxnZbOggq6VDQWoZAQgnY9ZMnIMDQbGpNC1rbErdhHJw5k2/JrgPJbeqHhJZ1ac30wgRK/BRavCnsFqDqUPZcXD9vKgiMjW6tSi6RDZMij56xMaL2/3eBce702Jvuvtlf3K4v+l+i71ib9g7VrAP7JB9ZkdsxgRz7Bf7zf6MrpI0GSc7a2ky2tzssBuTvL4GqAy5tw==</latexit>

s

<latexit sha1_base64="pTczvFf49Vo7OGJkmhEQPIcz9Ug=">AAACVXicbVDLSsNAFJ3EqjU+WnXpJlgEVyXRgq5EcOOyglWhCWVmcqOD8wgzE6WEfIFb/TbxYwQnbRe+Lgwczj333jOHFJwZG0Ufnr/UWl5Zba8F6xubW53u9s6NUaWmMKKKK31HsAHOJIwssxzuCg1YEA635PGi6d8+gTZMyWs7LSAV+F6ynFFsHXVlJt1e1I9mFf4F8QL00KKGk23vLMkULQVISzk2ZhxHhU0rrC2jHOogKQ0UmD7iexg7KLEAk1Yzp3V44JgszJV2T9pwxn6fqLAwZiqIUwpsH8zvXkP+1xuXNj9NKyaL0oKk80N5yUOrwubbYcY0UMunDmCqmfMa0gesMbUunCBIMsgTkVdJs5nk9ZwgpkqI4lnjSPE6+OmGUheBcVIJz1QJgWVWJSXBuh7HqUMyAz0XuS2OrXpx7Xa4xOPf+f4FN0f9+Lh/dDXonQ8W2bfRHtpHhyhGJ+gcXaIhGiGKAL2gV/TmvXuffstfmUt9bzGzi36U3/kCnPK0+w==</latexit>
  (s)

<latexit sha1_base64="9zT+sTfhXRYjv1HNmCOrPQIpBpg=">AAACW3icbVDLSsNAFJ3GV41vxZWbYBF0U5Iq6EoENy4r2Ac0QWYmN3boPMLMRCkhH+FWv8yF/+Kk7cLXhYHDuefee+aQnDNjw/Cj4S0tr6yuNdf9jc2t7Z3dvf2+UYWm0KOKKz0k2ABnEnqWWQ7DXAMWhMOATG7r/uAZtGFKPthpDonAT5JljGLrqEGcj9mpOXvcbYXtcFbBXxAtQAstqvu417iOU0ULAdJSjo0ZRWFukxJryyiHyo8LAzmmE/wEIwclFmCScua3Ck4ckwaZ0u5JG8zY7xMlFsZMBXFKge3Y/O7V5H+9UWGzq6RkMi8sSDo/lBU8sCqoPx+kTAO1fOoAppo5rwEdY42pdRH5fpxCFousjOvNJKvmBDFlTBRPa0eKV/5PN5S6CIyTSnihSggs0zIuCNbVKEockinouchtcWzZiiq3wyUe/c73L+h32tF5u3N/0brpLLJvoiN0jE5RhC7RDbpDXdRDFE3QK3pD741Pb8nzvc251GssZg7Qj/IOvwAe0bYk</latexit>
 stan,L

<latexit sha1_base64="29xqLyCFYAvt0SjQIZLKFWWzMEk=">AAACYnicbVDLahRBFK1pX7F9ZcxSF42D4EKG7iSgqxBw48JFBCcJTLfDrerbSZF6NFW3NUPR/+E2+Sv3fojVM7MwiRcKDueee+pweKukpzz/PUru3X/w8NHW4/TJ02fPX2yPXx572zmBM2GVdaccPCppcEaSFJ62DkFzhSf84tOwP/mBzktrvtGyxUrDmZGNFECR+u4XJeElBQLz/ku/2J7k03w12V1QbMCEbeZoMR4dlLUVnUZDQoH38yJvqQrgSAqFfVp2HlsQF3CG8wgNaPRVWMXus7eRqbPGuvgMZSv234sA2vul5lGpgc797d1A/m8376j5WAVp2o7QiPVHTacystnQQVZLh4LUMgIQTsasmTgHB4JiU2la1tiUugnl4Mybfk1wH0puVT0ksqpPb6YRIlbgo9TgT2G1BlOHsuPg+nlRRWRqdGtRdIlsmBR99IiNF7f7vQuOd6fF3nT36/7kcH/T/RZ7xd6wd6xgH9gh+8yO2IwJ5tgvdsWuR3+SNBknO2tpMtrc7LAbk7z+C5xgubE=</latexit> stan,R

<latexit sha1_base64="t+6Sp39lTtd4k5NAYLKghNDaNe8=">AAACYnicbVDLbtRAEJw1r2BeWXKEg8UKiQNa2UkkOEWRuHAMiE0irc2qZ9xORpmHNdOGrEb+D67wV9zzIRnv7oEktDRSqbq6plS8VdJTnv8dJffuP3j4aOtx+uTps+cvtscvj73tnMCZsMq6Uw4elTQ4I0kKT1uHoLnCE37xadif/EDnpTXfaNlipeHMyEYKoEh994uS8JICgXn/tV9sT/JpvprsLig2YMI2c7QYjw7K2opOoyGhwPt5kbdUBXAkhcI+LTuPLYgLOMN5hAY0+iqsYvfZ28jUWWNdfIayFfvvRQDt/VLzqNRA5/72biD/t5t31HysgjRtR2jE+qOmUxnZbOggq6VDQWoZAQgnY9ZMnIMDQbGpNC1rbErdhHJw5k2/JrgPJbeqHhJZ1ac30wgRK/BRavCnsFqDqUPZcXD9vKgiMjW6tSi6RDZMij56xMaL2/3eBce702Jvuvtlf3K4v+l+i71ib9g7VrAP7JB9ZkdsxgRz7Bf7zf6MrpI0GSc7a2ky2tzssBuTvL4GqAy5tw==</latexit>

  (s)

<latexit sha1_base64="Trp52W2jSXX4Q93EVZ+QEHZFpR8=">AAACXXicdVBNT9tAEN2Y0lKXQoBDD1xWjSrRQyPbsQi9VEhcOAapAarYRbvrMVmxH9buulVk+Vf02v4wTvwV1iSVmqodaaWnN29m3j5aCW5dFN33go1nm89fbL0MX22/3tnt7+1fWl0bBlOmhTbXlFgQXMHUcSfgujJAJBVwRe/Ouv7VNzCWa/XZLSrIJblVvOSMOE99yao5//rhyL6/6Q+i4ceT4yQ9xtEwisZxEncgGaejFMee6WqAVjW52et9ygrNagnKMUGsncVR5fKGGMeZgDbMagsVYXfkFmYeKiLB5s2T4xa/80yBS238Uw4/sX9ONERau5DUKyVxc/t3ryP/1ZvVrjzJG66q2oFiy0NlLbDTuPs+LrgB5sTCA8IM914xmxNDmPMhhWFWQJnJssm6zbRslwS1TUa1KDpHWrThuhvGfATWSxV8Z1pKooomqykx7SzOPVIFmKXIb/FsM4hbv8Mn/jtW/H9wmQzj0TC5SAen6Sr7LXSI3qIjFKMxOkXnaIKmiCGJfqCf6FfvIdgMtoOdpTTorWYO0FoFbx4B+XO3Bw==</latexit>

 +(s)

<latexit sha1_base64="FGONRddiNBDUtEJmpvmNbTUpg80=">AAACXXicbVDLSsNAFJ1G6yO+deHCTbAIilASFXQlghuXCtZWmlhmJjd2cB5hZqKUkK9wqx/myl9x0nbh68LA4dxz7z1zSM6ZsWH40fBmZptz8wuL/tLyyura+sbmnVGFptChiivdI9gAZxI6llkOvVwDFoRDlzxd1v3uM2jDlLy1oxwSgR8lyxjF1lH3cT5kD4f75mCw3grb4biCvyCaghaa1vVgo3Eep4oWAqSlHBvTj8LcJiXWllEOlR8XBnJMn/Aj9B2UWIBJyrHjKthzTBpkSrsnbTBmv0+UWBgzEsQpBbZD87tXk//1+oXNzpKSybywIOnkUFbwwKqg/n6QMg3U8pEDmGrmvAZ0iDWm1oXk+3EKWSyyMq43k6yaEMSUMVE8rR0pXvk/3VDqIjBOKuGFKiGwTMu4IFhX/ShxSKagJyK3xbFlK6rcDpd49Dvfv+DuqB0dt49uTloXJ9PsF9AO2kX7KEKn6AJdoWvUQRQJ9Ire0Hvj02t6y97qROo1pjNb6Ed52195YrbD</latexit>

s

<latexit sha1_base64="pTczvFf49Vo7OGJkmhEQPIcz9Ug=">AAACVXicbVDLSsNAFJ3EqjU+WnXpJlgEVyXRgq5EcOOyglWhCWVmcqOD8wgzE6WEfIFb/TbxYwQnbRe+Lgwczj333jOHFJwZG0Ufnr/UWl5Zba8F6xubW53u9s6NUaWmMKKKK31HsAHOJIwssxzuCg1YEA635PGi6d8+gTZMyWs7LSAV+F6ynFFsHXVlJt1e1I9mFf4F8QL00KKGk23vLMkULQVISzk2ZhxHhU0rrC2jHOogKQ0UmD7iexg7KLEAk1Yzp3V44JgszJV2T9pwxn6fqLAwZiqIUwpsH8zvXkP+1xuXNj9NKyaL0oKk80N5yUOrwubbYcY0UMunDmCqmfMa0gesMbUunCBIMsgTkVdJs5nk9ZwgpkqI4lnjSPE6+OmGUheBcVIJz1QJgWVWJSXBuh7HqUMyAz0XuS2OrXpx7Xa4xOPf+f4FN0f9+Lh/dDXonQ8W2bfRHtpHhyhGJ+gcXaIhGiGKAL2gV/TmvXuffstfmUt9bzGzi36U3/kCnPK0+w==</latexit>

xA

<latexit sha1_base64="IpvmRP4uopQgWGE/lBrOcRl9Mho=">AAACbXicbVHLbtQwFPWEQssU6AOxoqosRghWo2SK1C6L2HQ5SEyn0iQa2Tc3rTV+RLYDjKJ8RLfwZXwFv1BnkgVtuZKlo3OPr4/P5aUUzsfxn0H0ZOvps+2d58PdFy9f7e0fHF46U1nAGRhp7BVnDqXQOPPCS7wqLTLFJc756kvbn39H64TR3/y6xEyxay0KAcwHap6qgv5cfl7uj+JxvCn6GCQ9GJG+psuDwTTNDVQKtQfJnFskcemzmlkvQGIzTCuHJYMVu8ZFgJopdFm98dvQ94HJaWFsONrTDfvvjZop59aKB6Vi/sY97LXk/3qLyhdnWS10WXnU0D1UVJJ6Q9vP01xYBC/XATCwInilcMMsAx8iGg7THIuQSJ22k3nRdAR3dcqNzFtHRvakgk4FLDD3/QGEUFzQafwBRimm8zqtOLPNIskC0jnaThTmBrYeJU2YEXaQPEz8MbicjJOT8eTrp9H5pN/GDnlL3pGPJCGn5JxckCmZESArckt+kd+Dv9Gb6Cg67qTRoL/zmtyr6MMdvyG9hQ==</latexit> xA

<latexit sha1_base64="IpvmRP4uopQgWGE/lBrOcRl9Mho=">AAACbXicbVHLbtQwFPWEQssU6AOxoqosRghWo2SK1C6L2HQ5SEyn0iQa2Tc3rTV+RLYDjKJ8RLfwZXwFv1BnkgVtuZKlo3OPr4/P5aUUzsfxn0H0ZOvps+2d58PdFy9f7e0fHF46U1nAGRhp7BVnDqXQOPPCS7wqLTLFJc756kvbn39H64TR3/y6xEyxay0KAcwHap6qgv5cfl7uj+JxvCn6GCQ9GJG+psuDwTTNDVQKtQfJnFskcemzmlkvQGIzTCuHJYMVu8ZFgJopdFm98dvQ94HJaWFsONrTDfvvjZop59aKB6Vi/sY97LXk/3qLyhdnWS10WXnU0D1UVJJ6Q9vP01xYBC/XATCwInilcMMsAx8iGg7THIuQSJ22k3nRdAR3dcqNzFtHRvakgk4FLDD3/QGEUFzQafwBRimm8zqtOLPNIskC0jnaThTmBrYeJU2YEXaQPEz8MbicjJOT8eTrp9H5pN/GDnlL3pGPJCGn5JxckCmZESArckt+kd+Dv9Gb6Cg67qTRoL/zmtyr6MMdvyG9hQ==</latexit>

Fig. 1. Illustration of the tangent points and the approach
angle. The segment Sd is indicated with the solid line. (a)
A continuously diﬀerentiable perimeter. (b) A polygonal
perimeter.

3 One vs. One Game

This section solves the game played between one de-
fender and one intruder. The states of the system are
[sD, xA] and the dynamics are [ ˙sD, ˙xA] = [ωD, uA].
The terminal surface corresponding to intruder’s win is
{[sD, xA] | xA ∈ T and ∥xA − γsD∥ > 0}. The terminal
condition for defender’s win is discussed later in Sec. 3.2.

We ﬁrst introduce some relevant geometries, and then
solve the game of kind to ﬁnd the barrier surface [22]
that divides the game space into the intruder-winning
and the defender-winning regions. We also discuss the
objective functions for which the derived strategies are
also optimal in the game of degree.

3.1 Geometries

Let stan,R and stan,L denote the points where the tan-
gent lines from xA touch the perimeter (see Fig. 1a).
Considering the directions from the perspective of a de-
fender facing outward from the perimeter, the subscript

R corresponds to the “right” or clockwise (cw) direction
of motion, and L corresponds to the “left” or counter-
clockwise (ccw). We use

Sd(xA) ≜ [stan,R, stan,L]

to denote all the points on the perimeter that the in-
truder can reach by a straight-line path. Note that these
geometries are independent of the defender position.

For a given point sB ∈ Sd and sD /∈ Sd consider the
following quantity 4 :

JL(sB; sD, xA) ≜ sD )B − ∥γ(sB) − xA∥
ν . (2)

4 The restriction sD /∈ Sd will be removed after Remark 1.
 The ﬁrst term is the ccw distance from the defender to
sB, and ∥γ(sB)−xA∥ is the distance from the intruder to
sB. Hence, recalling that the defender and the intruder
has the speed 1 and ν respectively, JL describes how
much longer it takes for the defender to reach sB than
it takes for the intruder, when the defender moves ccw
and the intruder moves on a straight line path towards
sB. The subscript L is used to highlight that we assume
the engagement in the “left” or ccw direction.

Suppose the game starts at t = 0 and the intruder
reaches sB at time tF before the defender does. Then
sD )B(tF ) = sD )B(0) − tF ωD ≥ sD )B(0) − tF =
sD )B(0) − ∥γ(sB )−xA(0)∥
ν . Therefore, a positive JL(sB)
can also be interpreted as the expected arc-length dis-
tance between the intruder and the defender when the
intruder reaches sB. To focus on the geometry, we defer
the question of defender’s optimal direction of motion,
and whether the intruder should employ a straight line
path or not, to the later sections (e.g., Remark 3).

Restricting ourselves to straight line paths for now, the
intruder maximizes JL by ﬁnding the optimal breaching
point sB. The derivative is given by

dJL
dsB = d
dsB (sB − sD) − 1
ν d
dγ ∥γ − xA∥ · dγ(sB)
dsB

= 1 − 1
ν γ(sB) − xA
∥γ(sB) − xA∥ · T (sB),

where the dot product in the second term is related to
the approach angle deﬁned in the following:

Deﬁnition 1 Suppose the intruder position xA is given.
Then for s ∈ Sd, we deﬁne the approach angle to be

φ(s) ≜ cos−1 ( γ(s) − xA
∥γ(s) − xA∥ · T (s)) ∈ [0, π]. (3)

For a perimeter with discontinuous tangent vector (e.g.,
polygonal perimeter), we use φ−(s) and φ+(s) to denote
the approach angles before and after the discontinuity (in
ccw direction).

Note that φ is non-increasing in ccw direction due to the
convexity of T , 5 and for a continuously diﬀerentiable
perimeter, we always have φ(stan,R) = π and φ(stan,L) =
0 (see Fig. 1b).

Using the approach angle, the derivative is described as:

dJL
dsB = 1 − cos φ(sB)
ν ,

5 One can easily verify this by observing that T (s) and
γ(s) − xA rotate in ccw and cw direction respectively for
increasing s ∈ Sd.

4

which gives the following result:

dJL
dsB =
 



 positive if φ(sB) > φ
∗
L
0 if φ(sB) = φ∗
L
negative otherwise,
 (4)

where φ∗
L = cos
−1(ν). (5)

This result provides the critical breaching point that
maximizes JL as follows:

Deﬁnition 2 We deﬁne left breaching point sL(xA) ∈
Sd to be the point that maximizes JL. For a contin-
uously diﬀerentiable γ(s), it is the unique solution of
φ(s) = φ∗
L, i.e.,

sL(xA) = φ−1 (cos−1 ν) . (6)

For a perimeter with discontinuous tangent vector (e.g.,
polygonal perimeter), sL(xA) is a unique point that sat-
isﬁes either of the following conditions:

{ φ(s) = φ∗
L (sL is on a continuous part),

φ(s)+ < φ
∗
L < φ
−(s) (sL is on a vertex). (7)

Due to the monotonicity of φ(s) on a convex perimeter,
sL is always unique, and it can be found by a simple
search on a one-dimensional space. Note also that sL is
obtained analytically for some special cases discussed in
Sec. 3.4.

Remark 1 (Limiting cases) If ν = 1, then we always
have sL = stan,L, because φ∗
L = 0 and φ(stan,L) = 0.
When ν → 0 the optimal approach angle becomes φ∗
L →
π
2 , in which case sL is equivalent to the closest point on
the perimeter from xA.

Now we consider all defender locations by removing the
restriction sD ∈ Sd. With this extension, the left breach-
ing point sL does not maximize JL if sD ∈ [stan,R, sL],
however, we will show in Sec. 3.2 that sL and its coun-
terpart sR are the only points necessary in deﬁning the
optimal strategies.

For given positions sD and xA, we deﬁne the following
function that gives the critical value of JL:

J ∗
L(sD, xA) ≜ JL(sL) = sD )L − ∥γ(sL) − xA∥
ν . (8)

Figure 2a shows the level sets of J ∗
L for a speciﬁc value
of sD. The discontinuity corresponds to the manifold
where sL(xA) = sD.-0.4-0.3-0.2

-0.1-0.10
0

00.1
0.10.10.20.2
0.30.3
0.3

0.4
 0.4

0.50.50.60.60.70.8
-0.4
-0.3-0.2-0.2-0.1
-0.10
0

0 0.10.1
0.20.20.30.30.30.4
0.40.5
0.50.60.7
(a) (b)
 sD

<latexit sha1_base64="tTezqmZtKKITVaIF0fosg6hpYc4=">AAACWXicbVDLSsQwFE3ra6xvXbopDoKroR0FXYmgC5cKjgrTMiTprQbzKEmqDKHf4FY/TfwZ05lZ+LoQOJx77r0nh1ScGZskH0E4N7+wuNRZjlZW19Y3Nre2b42qNYUBVVzpe4INcCZhYJnlcF9pwIJwuCNP523/7hm0YUre2HEFucAPkpWMYuupgRm5i2a02U16yaTivyCdgS6a1dVoKzjNCkVrAdJSjo0Zpkllc4e1ZZRDE2W1gQrTJ/wAQw8lFmByN3HbxPueKeJSaf+kjSfs9wmHhTFjQbxSYPtofvda8r/esLblSe6YrGoLkk4PlTWPrYrbr8cF00AtH3uAqWbea0wfscbU+oCiKCugzETpsnYzKZspQYzLiOJF60jxJvrphlIfgfFSCS9UCYFl4bKaYN0M09wjWYCeivwWz7pu2vgdPvH0d75/wW2/lx72+tdH3bP+LPsO2kV76ACl6BidoUt0hQaIIoZe0Rt6Dz7DIOyE0VQaBrOZHfSjwp0vLxi1vQ==</latexit>sD

<latexit sha1_base64="tTezqmZtKKITVaIF0fosg6hpYc4=">AAACWXicbVDLSsQwFE3ra6xvXbopDoKroR0FXYmgC5cKjgrTMiTprQbzKEmqDKHf4FY/TfwZ05lZ+LoQOJx77r0nh1ScGZskH0E4N7+wuNRZjlZW19Y3Nre2b42qNYUBVVzpe4INcCZhYJnlcF9pwIJwuCNP523/7hm0YUre2HEFucAPkpWMYuupgRm5i2a02U16yaTivyCdgS6a1dVoKzjNCkVrAdJSjo0Zpkllc4e1ZZRDE2W1gQrTJ/wAQw8lFmByN3HbxPueKeJSaf+kjSfs9wmHhTFjQbxSYPtofvda8r/esLblSe6YrGoLkk4PlTWPrYrbr8cF00AtH3uAqWbea0wfscbU+oCiKCugzETpsnYzKZspQYzLiOJF60jxJvrphlIfgfFSCS9UCYFl4bKaYN0M09wjWYCeivwWz7pu2vgdPvH0d75/wW2/lx72+tdH3bP+LPsO2kV76ACl6BidoUt0hQaIIoZe0Rt6Dz7DIOyE0VQaBrOZHfSjwp0vLxi1vQ==</latexit>
 Fig. 2. Level sets of J ∗
L(sD, xA) (left) and J ∗
R(sD, xA) (right)
for a speciﬁc value of sD (ν = 0.9).

For a similar analysis on the cw motion of the defender,
consider the following function:

JR(sB; sD, xA) = sB )D − ∥xA − γ(sB)∥
ν , (9)

where the arc-length computation is now sB )D. With
the same process, we deﬁne the right breaching point, sR,
to be the solution to

φ(sR) = φ∗
R = π − cos−1(ν). (10)

We deﬁne a function for the critical value as

J ∗
R(sD, xA) ≜ JR(sR) = sR )D − ∥xA − γ(sR)∥
ν . (11)

Next we use the two functions J ∗
L and J ∗
R to divide the
game space into “right side” and “left side” with respect
to the position of the defender. Let s
op
D be the farthest
(opposite) point from the defender on the perimeter. The
partitioning will be given by the singular surface deﬁned
in the following:

Deﬁnition 3 Consider the surfaces deﬁned by

Γ(sD) = {xA | J ∗
L(xA, sD) = J ∗
R(xA, sD)}. (12)

The one extending from sD is called the aﬀerent sur-
face, Γaﬀ, and the other extending from s
op
D is called the
dispersal surface, Γdis (see Fig. 3a) [22].

The singular surfaces are deﬁned in the three-dimensional
state space, but for convenience, we look at the “two-
dimensional slice” by considering a speciﬁc value of sD.
The singular surfaces divide the entire game space into
two regions. We deﬁne them as the left region, ΩL(sD),
and the right region, ΩR(sD) (see Fig. 3a). As one can
see from the deﬁnition, there will be two equally good
strategies when the states are on the singular surface.

5
 -0.4-0.3-0.2-0.2
-0.2-0.1-0.1
-0.1

-0.1
 00
00
00.1
0.10.1
0.10.10.2
0.20.20.30.30.4afferentdispersal
R 1L

<latexit sha1_base64="g67ae3wGgD+8L76zcml6gCIfiWo=">AAACZXicbVDLahRBFK1pX7E1ZqLixoWNg+Bq6E4CZiUBNy5cRHGSwHQ73Lp9OylSj6aqOjIU/SVu9aP8An/D6plZmMQDBYdzz711OLyVwvk8/z1K7ty9d//B1sP00ePtJzvj3acnznQWaYZGGnvGwZEUmmZeeElnrSVQXNIpv/wwzE+vyDph9Fe/bKlScK5FIxB8lBbjnVKBv0CQ4Uu/+PStWIwn+TRfIbtNig2ZsA2OF7uj92VtsFOkPUpwbl7kra8CWC9QUp+WnaMW8BLOaR6pBkWuCqvkffYmKnXWGBuf9tlK/XcjgHJuqXh0Djndzdkg/m8273xzWAWh286TxvVHTSczb7KhhqwWltDLZSSAVsSsGV6ABfSxrDQta2pK1YRVO7zp1wJ3oeRG1kMiI/v0ehrEWIGLVk3f0SgFug5lx8H286KKTNdk16Z4JaphUvTxRmy8uNnvbXKyNy32p3ufDyZHB5vut9hL9pq9ZQV7x47YR3bMZgxZx36wn+zX6E+ynTxPXqytyWiz84xdQ/LqL3HhugA=</latexit>

R2L

<latexit sha1_base64="JOSQGMa3Y5CjGha/ipgQwAy4f3I=">AAACZXicbVDLahRBFK1pX7E1ZqLixoWNg+Bq6J4EdCUBNy5cRHGSwHQ73Lp9OylSj6aqWhmK/hK3+lF+gb9h9cwsTOKBgsO55946HN5K4Xye/x4lt27fuXtv53764OHuo73x/uMTZzqLNEcjjT3j4EgKTXMvvKSz1hIoLumUX74f5qffyDph9Be/aqlScK5FIxB8lJbjvVKBv0CQ4XO//Ph1thxP8mm+RnaTFFsyYVscL/dH78raYKdIe5Tg3KLIW18FsF6gpD4tO0ct4CWc0yJSDYpcFdbJ++xVVOqsMTY+7bO1+u9GAOXcSvHoHHK667NB/N9s0fnmbRWEbjtPGjcfNZ3MvMmGGrJaWEIvV5EAWhGzZngBFtDHstK0rKkpVRPW7fCm3wjchZIbWQ+JjOzTq2kQYwUuWjV9R6MU6DqUHQfbL4oqMl2T3ZjilaiGSdHHG7Hx4nq/N8nJbFocTGefDidHh9vud9hz9pK9ZgV7w47YB3bM5gxZx36wn+zX6E+ymzxNnm2syWi784RdQfLiL3PSugE=</latexit>

R 3L

<latexit sha1_base64="SD0ST2LvYDylLUvyNhvxKRTeIFI=">AAACZXicbVDLahRBFK3p+IitMZMoblzYOAiuhu4koCsJuHHhIoqTBKbb4dbt20mRejRV1cpQ9Je41Y/yC/wNq2dmYRIPFBzOPffW4fBWCufz/Pco2bpz99797Qfpw0c7j3fHe/unznQWaYZGGnvOwZEUmmZeeEnnrSVQXNIZv3o/zM++kXXC6C9+2VKl4EKLRiD4KC3Gu6UCf4kgw+d+8fHr4WI8yaf5CtltUmzIhG1wstgbvStrg50i7VGCc/Mib30VwHqBkvq07By1gFdwQfNINShyVVgl77NXUamzxtj4tM9W6r8bAZRzS8Wjc8jpbs4G8X+zeeebt1UQuu08aVx/1HQy8yYbashqYQm9XEYCaEXMmuElWEAfy0rTsqamVE1YtcObfi1wF0puZD0kMrJPr6dBjBW4aNX0HY1SoOtQdhxsPy+qyHRNdm2KV6IaJkUfb8TGi5v93ianB9PicHrw6WhyfLTpfps9Zy/Za1awN+yYfWAnbMaQdewH+8l+jf4kO8nT5Nnamow2O0/YNSQv/gJ1w7oC</latexit>
 sop
D

<latexit sha1_base64="OEvd3JZ+yUZTJd7g+pluG2p58ew=">AAACZXicbVBNSxxBFOwdEzWTqKuGXHLIkCWQ0zKzCnoSIR5yNJBVYWeydPe80cb+GLrfqEszv8Rr8qPyC/wb9uzuIWoeNBT16lUXxWopHKbp31608ur16tr6m/jtu43Nrf72zpkzjeUw5kYae8GoAyk0jFGghIvaAlVMwjm7/tbtz2/AOmH0T5zVUCh6qUUlOMVATftbbupP2l85wh16U7fT/iAdpvNJXoJsCQZkOafT7d5RXhreKNDIJXVukqU1Fp5aFFxCG+eNg5rya3oJkwA1VeAKP0/eJl8CUyaVseFpTObsvxeeKudmigWlonjlnu868n+7SYPVYeGFrhsEzRcfVY1M0CRdDUkpLHCUswAotyJkTfgVtZRjKCuO8xKqXFU+75xZ1S4I5nzOjCy7REa28dM0nIcKXJBquOVGKapLnzeM2naSFQHpEuxCFFwC6wdZGzxC49nzfl+Cs9Ew2xuOfuwPjkfL7tfJR/KZfCUZOSDH5Ds5JWPCSUPuyW/yp/cQbUTvow8LadRb3uySJxN9egS8i7qo</latexit>
 s D

<latexit sha1_base64="tTezqmZtKKITVaIF0fosg6hpYc4=">AAACWXicbVDLSsQwFE3ra6xvXbopDoKroR0FXYmgC5cKjgrTMiTprQbzKEmqDKHf4FY/TfwZ05lZ+LoQOJx77r0nh1ScGZskH0E4N7+wuNRZjlZW19Y3Nre2b42qNYUBVVzpe4INcCZhYJnlcF9pwIJwuCNP523/7hm0YUre2HEFucAPkpWMYuupgRm5i2a02U16yaTivyCdgS6a1dVoKzjNCkVrAdJSjo0Zpkllc4e1ZZRDE2W1gQrTJ/wAQw8lFmByN3HbxPueKeJSaf+kjSfs9wmHhTFjQbxSYPtofvda8r/esLblSe6YrGoLkk4PlTWPrYrbr8cF00AtH3uAqWbea0wfscbU+oCiKCugzETpsnYzKZspQYzLiOJF60jxJvrphlIfgfFSCS9UCYFl4bKaYN0M09wjWYCeivwWz7pu2vgdPvH0d75/wW2/lx72+tdH3bP+LPsO2kV76ACl6BidoUt0hQaIIoZe0Rt6Dz7DIOyE0VQaBrOZHfSjwp0vLxi1vQ==</latexit>

(a) (b)

sop
D

<latexit sha1_base64="OEvd3JZ+yUZTJd7g+pluG2p58ew=">AAACZXicbVBNSxxBFOwdEzWTqKuGXHLIkCWQ0zKzCnoSIR5yNJBVYWeydPe80cb+GLrfqEszv8Rr8qPyC/wb9uzuIWoeNBT16lUXxWopHKbp31608ur16tr6m/jtu43Nrf72zpkzjeUw5kYae8GoAyk0jFGghIvaAlVMwjm7/tbtz2/AOmH0T5zVUCh6qUUlOMVATftbbupP2l85wh16U7fT/iAdpvNJXoJsCQZkOafT7d5RXhreKNDIJXVukqU1Fp5aFFxCG+eNg5rya3oJkwA1VeAKP0/eJl8CUyaVseFpTObsvxeeKudmigWlonjlnu868n+7SYPVYeGFrhsEzRcfVY1M0CRdDUkpLHCUswAotyJkTfgVtZRjKCuO8xKqXFU+75xZ1S4I5nzOjCy7REa28dM0nIcKXJBquOVGKapLnzeM2naSFQHpEuxCFFwC6wdZGzxC49nzfl+Cs9Ew2xuOfuwPjkfL7tfJR/KZfCUZOSDH5Ds5JWPCSUPuyW/yp/cQbUTvow8LadRb3uySJxN9egS8i7qo</latexit>
 s D

<latexit sha1_base64="tTezqmZtKKITVaIF0fosg6hpYc4=">AAACWXicbVDLSsQwFE3ra6xvXbopDoKroR0FXYmgC5cKjgrTMiTprQbzKEmqDKHf4FY/TfwZ05lZ+LoQOJx77r0nh1ScGZskH0E4N7+wuNRZjlZW19Y3Nre2b42qNYUBVVzpe4INcCZhYJnlcF9pwIJwuCNP523/7hm0YUre2HEFucAPkpWMYuupgRm5i2a02U16yaTivyCdgS6a1dVoKzjNCkVrAdJSjo0Zpkllc4e1ZZRDE2W1gQrTJ/wAQw8lFmByN3HbxPueKeJSaf+kjSfs9wmHhTFjQbxSYPtofvda8r/esLblSe6YrGoLkk4PlTWPrYrbr8cF00AtH3uAqWbea0wfscbU+oCiKCugzETpsnYzKZspQYzLiOJF60jxJvrphlIfgfFSCS9UCYFl4bKaYN0M09wjWYCeivwWz7pu2vgdPvH0d75/wW2/lx72+tdH3bP+LPsO2kV76ACl6BidoUt0hQaIIoZe0Rt6Dz7DIOyE0VQaBrOZHfSjwp0vLxi1vQ==</latexit>

⌦R

<latexit sha1_base64="l9yzHLfaqOUlWD7XGSAjLmhE/ss=">AAACjXicfZHbahRBEIZ7J1HjeMjp0pshiyAiy0xU9EIkEEFvQhJxk4XtZanuqZk06cPQ3SMuw75EbuOL+Tb27M5CDmJBw89Xf1HVVaySwvk0/dOL1tYfPHy08Th+8vTZ882t7Z0zZ2rLcciNNHbEwKEUGodeeImjyiIoJvGcXR62+fOfaJ0w+oefVThRUGpRCA4+oBE9VljC9Pt0q58O0kUk90XWiT7p4mS63TM0N7xWqD2X4Nw4Sys/acB6wSXOY1o7rIBfQonjIDUodJNmMfA8eRlInhTGhqd9sqA3KxpQzs0UC04F/sLdzbXwX7lx7YuPk0boqvao+bJRUcvEm6T9fZILi9zLWRDArQizJvwCLHAfdhTHMc2xoMw1lBmZtxMYOV9CVTS07ceKFWAdYCvAl4BDW/MFw1osHgVwXKEFb+zrhoItFfyahzWV9E2r/mcUemUMKg4nyu4e5L442x9kbwf7p+/6B5+7Y22QF2SPvCIZ+UAOyDdyQoaEE0muyDX5HW1G76NPUeeNel3NLrkV0de/pdjJqg==</latexit>

! L

<latexit sha1_base64="HmqOKoVrkRLi9M+g1egsdG7aWhU=">AAACjXicfZHbahRBEIZ7J1HjeMjBS2+GLIKILDNR0QuRQAS9SEgCbrKwvSzVPTWTJn0YunvEZdiXyK2+mG9jz+4s5CApaPj56i+quopVUjifpn970dr6g4ePNh7HT54+e765tb1z5kxtOQ65kcaOGDiUQuPQCy9xVFkExSSes8uDNn/+E60TRv/wswonCkotCsHBBzSixwpLmB5Ot/rpIF1EcldkneiTLk6m2z1Dc8NrhdpzCc6Ns7TykwasF1ziPKa1wwr4JZQ4DlKDQjdpFgPPk1eB5ElhbHjaJwt6vaIB5dxMseBU4C/c7VwL/5cb1774NGmErmqPmi8bFbVMvEna3ye5sMi9nAUB3Iowa8IvwAL3YUdxHNMcC8pcQ5mReTuBkfMlVEVD236sWAHWAbYCfAk4tDVfMazF4lEAxxVa8Ma+aSjYUsGveVhTSd+26j6j0CtjUHE4UXb7IHfF2d4gezfYO33f3//SHWuDvCS75DXJyEeyT76TEzIknEhyRX6TP9Fm9CH6HHXeqNfVvCA3Ivr2D5kMyaQ=</latexit>
 Fig. 3. Singular surfaces for ν = 0.9. (a) Left region (cyan)
and right region (magenta). The left region is further parti-
tioned into three regions. (b) Level sets of V .

However, we will later show that such non-uniqueness
does not prevent us from identifying the barrier.

Let SL = [sD, s
op
D ] and SR = [s
op
D , sD] denote the seg-
ments of the perimeter to the left and right of the de-
fender. Whether the intruder is in the left region or not
can be tested using the location of the breaching points
(sL and sR), and the relation between the values J ∗
L and
J ∗
R. If xA ∈ ΩL(sD), then xA is in one of the following
three regions (see Fig. 3a):

R
1
L = {xA | sL ∈ SL, sR ∈ SR, J ∗
L > J ∗
R}
R
2
L = {xA | sL ∈ SL, sR /∈ SR} (13)
R
3
L = {xA | sL /∈ SL, sR /∈ SR, J ∗
L < J ∗
R}.

If the states [sD, xA] satisfy none of the above three
conditions, and if J ∗
L ̸= J ∗
R, then we have xA ∈ ΩR(sD).

Finally, we merge the two objective functions as follows:

V (xA, sD) =
 { J ∗
L(xA, sD) if xA ∈ ΩL(sD)

J ∗
R(xA, sD) otherwise. (14)

Fig. 3b shows the level sets of V (sD, xA). 6 We later
show in Sec. 3.3 that this is the value of the game for
some payoﬀ functions.

We close this section by providing an algorithm to com-
pute sL for general ν ∈ (0, 1). Note that in the special
case where ν = 1 or ν → 0, sL is immediately obtained
as discussed in Remark 1.

The condition in line 4 is only necessary for perimeters
that are non-diﬀerentiable. It is suﬃcient to visit non-
diﬀerentiable vertices in the interval Sd, and test the
condition (7). When there is no such critical point, then

6 The evolution of these level sets with the defender position
is illustrated in: https://youtu.be/h0_VqJbNsQc
 Algorithm 1 Finding left breaching point sL
1: Input: xA, γ, and ν
2: Compute tangent points stan,L and stan,R
3: Sd ← [stan,R, stan,L]
4: if ∃ a vertex s ∈ Sd s.t. (7) is true then
5: sL ← s
6: else
7: sL ← arg mins∈Sd |φ(s) − cos−1(ν)|
8: end if
9: Return: sL

sD

<latexit sha1_base64="zSSEBSZjzf1Hl5UEsFWMYk+VfmQ=">AAACV3icbVDLSsNAFJ3EV42vVpdugkVwVZIq6EoEXbhUtCo0ocxMburgPMLMRCkhn+BWv82v0Unbha8LA4dzz733zCEFZ8ZG0YfnLywuLa+0VoO19Y3NrXZn+86oUlMYUMWVfiDYAGcSBpZZDg+FBiwIh3vydN70759BG6bkrZ0UkAo8lixnFFtH3ZjRxajdjXrRtMK/IJ6DLprX1ajjnSaZoqUAaSnHxgzjqLBphbVllEMdJKWBAtMnPIahgxILMGk19VqH+47Jwlxp96QNp+z3iQoLYyaCOKXA9tH87jXkf71hafOTtGKyKC1IOjuUlzy0Kmw+HmZMA7V84gCmmjmvIX3EGlPr4gmCJIM8EXmVNJtJXs8IYqqEKJ41jhSvg59uKHURGCeV8EKVEFhmVVISrOthnDokM9Azkdvi2Kob126HSzz+ne9fcNfvxYe9/vVR96w/z76FdtEeOkAxOkZn6BJdoQGiaIxe0Rt69z68T3/Zb82kvjef2UE/yu98ASTStbA=</latexit>
 y A

<latexit sha1_base64="1g5CCiDD6iohBraxbImQcXQCXMo=">AAACV3icbVDLSsNAFJ3EV42vVpdugkVwVZIq6EoUNy4VrQpNKDOTmzo4jzAzUUrIJ7jVb/NrdNJ24evCwOHcc+89c0jBmbFR9OH5C4tLyyut1WBtfWNzq93ZvjOq1BQGVHGlHwg2wJmEgWWWw0OhAQvC4Z48XTT9+2fQhil5aycFpAKPJcsZxdZRN5PR+ajdjXrRtMK/IJ6DLprX1ajjnSaZoqUAaSnHxgzjqLBphbVllEMdJKWBAtMnPIahgxILMGk19VqH+47Jwlxp96QNp+z3iQoLYyaCOKXA9tH87jXkf71hafOTtGKyKC1IOjuUlzy0Kmw+HmZMA7V84gCmmjmvIX3EGlPr4gmCJIM8EXmVNJtJXs8IYqqEKJ41jhSvg59uKHURGCeV8EKVEFhmVVISrOthnDokM9Azkdvi2Kob126HSzz+ne9fcNfvxYe9/vVR96w/z76FdtEeOkAxOkZn6BJdoQGiaIxe0Rt69z68T3/Zb82kvjef2UE/yu98ASqxtbM=</latexit> x A

<latexit sha1_base64="iEZrvIH/R9/WZskWyOVDWpwB2As=">AAACV3icbVDLTsMwEHTCq4Rn4cglokLiVCUFCU4IxIUjCApITVTZzqZY+BHZDlBF+QSu8G18DThtD7xWsjSand0dDyk4MzaKPjx/bn5hcam1HKysrq1vbLa3bo0qNYU+VVzpe4INcCahb5nlcF9owIJwuCOP503/7gm0YUre2HEBqcAjyXJGsXXU9cvwbLjZibrRpMK/IJ6BDprV5bDtnSSZoqUAaSnHxgziqLBphbVllEMdJKWBAtNHPIKBgxILMGk18VqHe47Jwlxp96QNJ+z3iQoLY8aCOKXA9sH87jXkf71BafPjtGKyKC1IOj2Ulzy0Kmw+HmZMA7V87ACmmjmvIX3AGlPr4gmCJIM8EXmVNJtJXk8JYqqEKJ41jhSvg59uKHURGCeV8EyVEFhmVVISrOtBnDokM9BTkdvi2KoT126HSzz+ne9fcNvrxgfd3tVh57Q3y76FdtAu2kcxOkKn6AJdoj6iaIRe0Rt69z68T3/Rb02lvjeb2UY/ym9/ASi+tbI=</latexit>
 Fig. 4. The barrier surface (depicted in red). The green
cylinder depicts the perimeter shape extruded vertically. In-
truder winning region is the interior of the barrier surface.

the optimization in line 7 is performed. The simplest way
to perform this optimization is to discretize the interval
Sd into a ﬁnite set of points and evaluate the right-hand
side, which is practically ﬁne since the complexity of
the search grows only linearly with the resolution. To
improve the eﬃciency, one can also use, for example, the
bisection method [9].

The right breaching point sR can be computed in a sim-
ilar way. Once these breaching points are found, J ∗
L and
J ∗
R are immediately obtained using (2) and (9).

3.2 Winning Regions

This section proves that the barrier for the game of kind
is given by the zero level set of V deﬁned in (14). Fig. 4
depicts the surface V (sD, xA) = 0 in the three dimen-
sional state space. For convenience, we perform our anal-
ysis using the two-dimensional slice at sD corresponding
to the location of the defender. We deﬁne the intruder
winning region as

RA(sD) = {xA | V (sD, xA) > 0}. (15)

We ﬁrst show that the intruder can guarantee its victory
if it starts inside RA.

Lemma 1 If the initial conﬁguration is such that xA ∈
RA(sD) (i.e., V > 0), then regardless of the defender

6
! =0 . 4

<latexit sha1_base64="XHeVuyXW2Jx9cofiz+ds9Vpihn8=">AAACW3icbVDLSsNAFJ3Gd3y1iis3wSK4KokWdaMIblwqWCs0QWYmN+3QeYSZiVJCPsKtfpkL/8VJ24WvCwOHc8+998whOWfGhuFHw1tYXFpeWV3z1zc2t7abrZ0HowpNoUcVV/qRYAOcSehZZjk85hqwIBz6ZHxd9/vPoA1T8t5OckgEHkqWMYqto/qxLC7CTvep2Q474bSCvyCagzaa1+1Tq3EZp4oWAqSlHBsziMLcJiXWllEOlR8XBnJMx3gIAwclFmCScuq3Cg4dkwaZ0u5JG0zZ7xMlFsZMBHFKge3I/O7V5H+9QWGz86RkMi8sSDo7lBU8sCqoPx+kTAO1fOIAppo5rwEdYY2pdRH5fpxCFousjOvNJKtmBDFlTBRPa0eKV/5PN5S6CIyTSnihSggs0zIuCNbVIEockinomchtcWzZjiq3wyUe/c73L3g47kQnneO7bvvqdJ79KtpHB+gIRegMXaEbdIt6iKIxekVv6L3x6S14vrcxk3qN+cwu+lHe3hd+RLXV</latexit> ! =0 . 8

<latexit sha1_base64="m3OTAVTamP8GttMnb0YDay46C/4=">AAACXHicbVDLSsQwFM3U8VXfCm7cBAfB1dCqqBtFcONSwdGBaZEkvdVgHiVJlaH0J9zqj7nxW0xnZuGoFwKHc8+99+TQQnDrouizFcy0Z+fmFxbDpeWV1bX1jc07q0vDoMe00KZPiQXBFfQcdwL6hQEiqYB7+nzZ9O9fwFiu1a0bFpBK8qh4zhlxnuonqjyLuqf4Yb0TdaNR4b8gnoAOmtT1w0brPMk0KyUoxwSxdhBHhUsrYhxnAuowKS0UhD2TRxh4qIgEm1YjwzXe80yGc238Uw6P2J8TFZHWDiX1Sknck/3da8j/eoPS5adpxVVROlBsfCgvBXYaN7/HGTfAnBh6QJjh3itmT8QQ5nxGYZhkkCcyr5JmM83rMUFtlVAtssaRFnU47YYxH4H1UgWvTEtJVFYlJSWmHsSpRyoDMxb5LZ6tOnHtd/jE49/5/gV3B934sHtwc9S5OJ5kv4B20C7aRzE6QRfoCl2jHmJIoDf0jj5aX0E7WApWxtKgNZnZQlMVbH8D65e2Aw==</latexit> ! =1

<latexit sha1_base64="yw+UdTEHH0yDzf/mrbFKYWGlUxs=">AAACWXicbVDLSsNAFJ3EV42vVpdugkVwVRIVdaMU3LhUsFpoQpmZ3OjgPMLMRCkh3+BWP038GSdtF74uDBzOPffeM4cUnBkbRR+ev7C4tLzSWg3W1jc2t9qd7TujSk1hQBVXekiwAc4kDCyzHIaFBiwIh3vydNn0759BG6bkrZ0UkAr8IFnOKLaOGiSyPI/H7W7Ui6YV/gXxHHTRvK7HHe8iyRQtBUhLOTZmFEeFTSusLaMc6iApDRSYPuEHGDkosQCTVlO3dbjvmCzMlXZP2nDKfp+osDBmIohTCmwfze9eQ/7XG5U2P0srJovSgqSzQ3nJQ6vC5uthxjRQyycOYKqZ8xrSR6wxtS6gIEgyyBORV0mzmeT1jCCmSojiWeNI8Tr46YZSF4FxUgkvVAmBZVYlJcG6HsWpQzIDPRO5LY6tunHtdrjE49/5/gV3h734qHd4c9ztn8yzb6FdtIcOUIxOUR9doWs0QBQx9Ire0Lv36Xt+yw9mUt+bz+ygH+XvfAFzqrVg</latexit>

Fig. 5. Intruder-winning region under the constraint sL ∈ SL
(cyan) and sR ∈ SR (magenta), for varied intruder speed ν.
The dotted lines illustrate the corresponding intruder paths.

(a) (b)

sL

<latexit sha1_base64="syJd+KcAgYWuV4GDUjsN5+o+FqQ=">AAACV3icbVDLSsNAFJ3EV42vVpdugkVwVZIq6EoENy5cKFoVmlBmJjd1cB5hZqKUkE9wq9/m1+ik7cLXhYHDuefee+aQgjNjo+jD8xcWl5ZXWqvB2vrG5la7s31nVKkpDKjiSj8QbIAzCQPLLIeHQgMWhMM9eTpv+vfPoA1T8tZOCkgFHkuWM4qto27M6HLU7ka9aFrhXxDPQRfN62rU8U6TTNFSgLSUY2OGcVTYtMLaMsqhDpLSQIHpEx7D0EGJBZi0mnqtw33HZGGutHvShlP2+0SFhTETQZxSYPtofvca8r/esLT5SVoxWZQWJJ0dykseWhU2Hw8zpoFaPnEAU82c15A+Yo2pdfEEQZJBnoi8SprNJK9nBDFVQhTPGkeK18FPN5S6CIyTSnihSggssyopCdb1ME4dkhnomchtcWzVjWu3wyUe/873L7jr9+LDXv/6qHvWn2ffQrtoDx2gGB2jM3SBrtAAUTRGr+gNvXsf3qe/7LdmUt+bz+ygH+V3vgA0WrW4</latexit>
 sR

<latexit sha1_base64="LyT1fUnDsYzpZoKTieX4+Xe94Nk=">AAACV3icbVDLSsNAFJ3EV42vVpdugkVwVZIq6EoENy59VYUmlJnJTR2cR5iZKCXkE9zqt/k1Omm78HVh4HDuufeeOaTgzNgo+vD8hcWl5ZXWarC2vrG51e5s3xlVagoDqrjSDwQb4EzCwDLL4aHQgAXhcE+ezpv+/TNow5S8tZMCUoHHkuWMYuuoGzO6HrW7US+aVvgXxHPQRfO6HHW80yRTtBQgLeXYmGEcFTatsLaMcqiDpDRQYPqExzB0UGIBJq2mXutw3zFZmCvtnrThlP0+UWFhzEQQpxTYPprfvYb8rzcsbX6SVkwWpQVJZ4fykodWhc3Hw4xpoJZPHMBUM+c1pI9YY2pdPEGQZJAnIq+SZjPJ6xlBTJUQxbPGkeJ18NMNpS4C46QSXqgSAsusSkqCdT2MU4dkBnomclscW3Xj2u1wice/8/0L7vq9+LDXvzrqnvXn2bfQLtpDByhGx+gMXaBLNEAUjdErekPv3of36S/7rZnU9+YzO+hH+Z0vQAC1vg==</latexit> sL

<latexit sha1_base64="syJd+KcAgYWuV4GDUjsN5+o+FqQ=">AAACV3icbVDLSsNAFJ3EV42vVpdugkVwVZIq6EoENy5cKFoVmlBmJjd1cB5hZqKUkE9wq9/m1+ik7cLXhYHDuefee+aQgjNjo+jD8xcWl5ZXWqvB2vrG5la7s31nVKkpDKjiSj8QbIAzCQPLLIeHQgMWhMM9eTpv+vfPoA1T8tZOCkgFHkuWM4qto27M6HLU7ka9aFrhXxDPQRfN62rU8U6TTNFSgLSUY2OGcVTYtMLaMsqhDpLSQIHpEx7D0EGJBZi0mnqtw33HZGGutHvShlP2+0SFhTETQZxSYPtofvca8r/esLT5SVoxWZQWJJ0dykseWhU2Hw8zpoFaPnEAU82c15A+Yo2pdfEEQZJBnoi8SprNJK9nBDFVQhTPGkeK18FPN5S6CIyTSnihSggssyopCdb1ME4dkhnomchtcWzVjWu3wyUe/873L7jr9+LDXv/6qHvWn2ffQrtoDx2gGB2jM3SBrtAAUTRGr+gNvXsf3qe/7LdmUt+bz+ygH+V3vgA0WrW4</latexit>

Fig. 6. Engagement when the game starts in a conﬁguration
with sL /∈ SL and sR /∈ SR. (a) Defender takes a suboptimal
strategy aiming at sL. (b) Intruder enters ΩR and switches
its heading to sR.

strategy, the intruder guarantees its win using the follow-
ing feedback strategy:

u
∗
A =
 { ν ˆxA )L if xA ∈ ΩL(sD)

ν ˆxA )R otherwise, (16)

where ˆxA )L = γ(sL)−xA
∥γ(sL)−xA∥ , and ˆxA )R = γ(sR)−xA
∥γ(sR)−xA∥ . 7

PROOF. Suppose xA ∈ ΩL(sD) without the loss of
generality. We consider two cases: (i) sL ∈ [sD, s
op
D ], and
(ii) sL ∈ [s
op
D , sD]. In either case, we know that the in-
truder reaches sL ﬁrst if the defender moves ccw, because
J ∗
L = V > 0.

In the ﬁrst case when sL ∈ [sD, s
op
D ], it is clear that the
cw motion by the defender takes longer time to reach
sL than the ccw motion since sL )D > sD )L. Therefore,
the intruder can reach sL ﬁrst regardless of the defender
strategy. The set of all intruder positions corresponding
to the ﬁrst case is shown as the shaded (cyan) region in
Fig. 5.

The second case where sL ∈ [s
op
D , sD] (corresponding
to the white region in Fig. 5) is more subtle since the

7 For conciseness, we take the convention that the intruder
treats the singular surface as part of ΩR. On the singular
surface, the two actions in (16) are equally good, and this
choice is inconsequential towards the outcome of the game.
 defender may be tempted to move cw to reach sL before
the intruder does (e.g., see Fig. 6a). Suppose the defender
takes this strategy: ωD = −1 (cw motion). Then J ∗
L
increases because sD )L in (8) increases. Now, there exists
a time t1 when xA(t1) ∈ Γdis(sD(t1)), at which point we
have

V (t1) = J ∗
L(t1) = J ∗
R(t1) > J ∗
L(t0) = V (t0) > 0. (17)

If the defender continues in cw direction, the intruder
enters ΩR, and the strategy (16) switches the breaching
point to sR. 8 The intruder will reach sR ﬁrst because
J ∗
R(t1) > 0 (Fig. 6b). If the defender goes back to ccw
motion, the intruder stays in ΩL and continues towards
sL. The intruder will reach sL ﬁrst because J ∗
L(t1) > 0.

Therefore, no matter what decision the defender makes
at this point in time, V (sD, xA) stays positive through-
out the rest of the game, and the intruder never leaves
RA(sD) until it reaches the perimeter. Note that, for the
defender, this conﬁguration at t1 is strictly “worse” than
the initial one in the sense that V is now strictly larger
than what it was at t0.

Also note if xA ∈ Γdis, and if the defender continues to
switch its heading (according to ωD = −1 if xA ∈ ΩL,
and ωD = 1 otherwise, which is the opposite of (18)),
there will be a “chatter” due to inﬁnitely frequent switch-
ing in the heading. 9 The intruder will oscillate about
Γdis, and since it always has a velocity component to-
wards the perimeter (due to its convexity), the intruder
slide along Γdis to approach the perimeter and eventually
reach s
op
D . Notice that the defender gains no advantage
in the azimuthal proximity to the intruder, and thus a
rational defender will in fact never use such a strategy. ■

Remark 2 (Dominance region) For the conﬁgura-
tion in Fig. 6a, the analysis based on the dominance
region [32] will not conclude that the intruder can win
the game, because sL is not in the intruder-dominated
region; i.e., the defender has a way to reach sL before the
intruder. Nevertheless, we have shown that the intruder
can win the game by employing a feedback strategy (16).

The result mentioned in Remark 2 is a consequence of
the following points: (i) the perimeter acts as an obstacle,
and (ii) the defender is protecting a region (and not a
single point). Rather than moving towards the optimal
breaching point in the shortest path, the defender must
maneuver so that it does not generate a breaching point
that is “worse” (corresponding to a higher V ), as was
illustrated in Fig. 6. This is why the defender must travel

8 The simulation video at https://youtu.be/h0_VqJbNsQc
illustrates the engagement.
9 Such phenomena often arise in diﬀerential games [45,33].
The solution to a diﬀerential equation with discontinuous
right-hand side (due to chattering) can be provided in the
sense of Filippov [10].

7

a distance longer than L/2 (half of the perimeter length)
when the intruder is in the unshaded region in Fig. 5.

Remark 3 (Straight line path) Consider the case
xA ∈ ΩL. Noting that sL remains constant if uA =
ν ˆxA )L, and that sL is independent of sD, the strategy
in (16) clearly results in a straight line path towards sL.
Even if the defender behaves suboptimally, as exempliﬁed
in Fig. 6, the intruder’s path will still remain piece-wise
linear. This observation combined with the results of
Sec. 3.3 justiﬁes the restriction of the intruder strategy
to a set of straight-line paths.

Lemma 1 only gives a suﬃcient condition for the intruder
to win. To prove that it is also a necessary condition,
we show that the defender wins if the game starts in a
conﬁguration xA /∈ RA(sD).

Recall that the defender wins the game by either inter-
cepting the intruder or preventing it from reaching the
perimeter indeﬁnitely. Related to the latter scenario, we
show that the defender is able to stabilize the system
around the conﬁguration xA ∈ Γaﬀ(sD). 10

Lemma 2 When xA(t0) ∈ Γaﬀ(sD(t0)), then for any
intruder control strategy, the defender can maintain the
condition xA(t) ∈ Γaﬀ(sD(t)) for all t > t0 using the
following control:

ω∗
D(sD, xA) =
 { 1 if xA ∈ ΩL(sD)

−1 otherwise. (18)

PROOF. In the neighborhood of the surface Γaﬀ(sD),
consider the error function e = J ∗
L − J ∗
R. Noting that
e > 0 if xA ∈ ΩL(sD), and e < 0 otherwise, we can
rewrite the control as ω∗
D = sgn(e). (Note, this ex-
pression of control is only valid in the neighborhood of
xA ∈ Γaﬀ(sD).) The time derivative of the squared error
is given by d
dt e2 = 2e( ˙J ∗
L − ˙J ∗
R), where ˙J ∗
L is

dJ ∗
L
dt = ˙sL − ˙sD − ˆxA )L
ν · ( ˙sLT (sL) − uA)

= ˙sL
 (
1 − cos φ(sL)
ν
 ) + ˆxA )L
ν · uA − ωD

= ˆxA )L
ν · uA − ωD. (19)

From the second to the third line, we used the fact that
˙sL (1 − cos φ(sL)
ν ) = 0, which we prove in the following.
Observe that a small displacement in xA moves sL if it
is on a continuously diﬀerentiable part of the perimeter,
but sL will remain stationary if it is on a vertex (see (7)).

10 This stabilization is also demonstrated in the simulation
video available at https://youtu.be/h0_VqJbNsQc
 When sL is on a continuously diﬀerentiable part, we have
φ(sL) = φ∗
L = cos−1 ν, which gives 1 − cos φ(sL)
ν = 0.
When sL is on a vertex and not moving, we have ˙sL = 0.

With a similar computation on ˙J ∗
R, the time derivative
of the squared error is

ν
2 d
dt e2 = e (ˆxA )L · uA − νω∗
D − (ˆxA )R · uA + νω∗
D))

= e ((ˆxA )L − ˆxA )R) · uA − 2νω∗
D)

Recalling that ˆxA )L and ˆxA )R are unit vectors, no-
tice that ∥ˆxA )L − ˆxA )R∥ ≤ 2, and the equality holds
when ˆxA )L = −ˆxA )R, which can be true only when
xA is on the perimeter. Therefore, we have the bound
| (ˆxA )L − ˆxA )R) · uA| < 2ν, which gives

ν
2 d
dt e2 = |e|sgn(e) ((ˆxA )L − ˆxA )R) · uA − 2νsgn(e))

< −|e| (−2νsgn(e) + 2ν)
≤ 0.

Therefore, the error is stabilized around 0, implying that
J ∗
L = J ∗
R, i.e., xA ∈ Γaﬀ(sD). ■

Since the aﬀerent surface extends from the defender’s
position, the lemma shows that the intruder can only
reach the perimeter by passing through the defender po-
sition: i.e., it cannot reach the perimeter without getting
captured. Therefore, we extend the deﬁnition of capture
from xA = γ(sD) to the condition xA ∈ Γaﬀ(sD), and
use it as part of the terminal condition. Note that the
former condition is contained in the latter.

Lemma 3 Let RD(sD) denote the complement of
RA(sD). If the initial condition is xA ∈ RD(sD), i.e.,
xA /∈ RA(sD), then regardless of the intruder strategy,
the defender wins the game of kind using ω∗
D in (18):
i.e., the defender either captures the intruder or prevents
it from scoring indeﬁnitely.

PROOF. Suppose the intruder never enters the win-
ning region RA. Then, since RA contains the entire
perimeter other than a single point sD (defender posi-
tion), the only entry point to the perimeter is now sD.
However, entering the perimeter from sD means capture.
Therefore, for the intruder to win the game, it is neces-
sary to enter RA. The question is: can the intruder start
outside of RA and enter it?

Crossing the boundary ∂RA and entering RA requires
V (sD, xA) to increase from negative to positive. How-
ever, this is impossible when xA ∈ ΩL(sD) because

˙V = ˙J ∗
L = 1
ν ˆxA )L · uA − ω∗
D ≤ 0. (20)

8

We similarly have ˙V ≤ 0 for xA ∈ ΩR(sD). Therefore,
V (sD, xA) is non increasing, and so the intruder cannot
enter the region V > V (t0), implying that it cannot
enter RA. ■

The results of this section is summarized in the following
theorem:

Theorem 1 The zero level set of V (sD, xA) deﬁned in
(14) gives the barrier of the game of kind.

The result directly follows from Lemmas 1, 2 and 3.

We also provide the intruder and defender strategies in
the algorithm form. The key step for both strategies is to
determine whether the intruder is in the left region ΩL or
in the right region ΩR. Importantly, this question can be
answered without explicitly calculating the boundaries
of the regions:

Algorithm 2 Determining region (1 vs. 1)
1: Input: sD, xA, γ, and ν
2: Compute sL and sR using Alg. 1
3: J ∗
L ← JL(sL; sD, xA) using (2)
4: J ∗
R ← JR(sR; sD, xA) using (9)
5: if any of the conditions in (14) is true then
6: is in Left ← T rue
7: else
8: is in Left ← F alse
9: end if
10: Return: is in Left

Given the information is in Left, we can immediately
calculate the control input:

Algorithm 3 Intruder control (1 vs. 1)
1: Input: sD, xA, γ, and ν
2: Compute sL and sR using Alg. 1
3: Determine the region (i.e., is in left) using Alg. 2
4: if is in left = T rue then
5: u∗
A ← ν ˆxA/L
6: else
7: u∗
A ← ν ˆxA/R
8: end if
9: Return: u
∗
A

Algorithm 4 Defender control (1 vs. 1)
1: Input: sD, xA, γ, and ν
2: Determine the region (i.e., is in left) using Alg. 2
3: if is in left = T rue then
4: ω∗
D ← 1
5: else
6: ω∗
D ← −1
7: end if
8: Return: ω∗
D
 3.3 Optimality of the Strategies

This section discusses how the strategy set (ω∗
D, u
∗
A) de-
ﬁned in (18) and (16) forms an equilibrium also in the
game of degree for some objective functions. We visit
intruder-winning and defender-winning conﬁgurations
separately.

Suppose the initial conﬁguration is xA ∈ RA(sD). Then
consider the following objective function:

P1(ωD, uA) = min{sD )B(tF ), sB )D(tF )}, (21)

where tF is the time the intruder breaches the perimeter
at point sB. This quantity P1 describes the safe distance
at the time of breaching which the intruder maximizes
and the defender minimizes. The min operator is used
to account for both ccw and cw measure of the distance.

Theorem 2 If the initial conﬁguration satisﬁes xA ∈
RA(sD), and if the players use P1 in (21) as the objective
function, then u
∗
A in (16) and ω∗
D in (18) form an equi-
librium, and the value of the game is V (sD, xA) in (14):

V = min
ωD max
uA P1(ωD, uA) = max
uA min
ωD P1(ωD, uA).

PROOF. Suppose xA ∈ ΩL without the loss of gener-
ality. Along the terminal surface {[sD, xA] | xA ∈ ∂T },
we have xA = γ(sB) where sB ∈ SL from the sup-
position. We also have V = J ∗
L(sD, xA) = sD )B since
the term ∥γ(sL) − xA∥ in (2) is 0. Noting that sD )B =
min{sD )B, sB )D} for sB ∈ SL, we have P1 = J ∗
L along
the terminal surface. Therefore, maximizing or minimiz-
ing P1 is equivalent to maximizing or minimizing J ∗
L(tF )
on the terminal surface. Recalling the time derivative in
(19), we have

1 = arg min
ωD max
uA ˙J ∗
L(ωD, uA)

ν ˆxA )L = arg max
uA min
ωD ˙J ∗
L(ωD, uA)

and

min
ωD max
uA ˙J ∗
L(ωD, uA) = max
uA min
ωD ˙J ∗
L(ωD, uA)

= ˙J ∗
L(1, ν ˆxA )L) = 0. (22)

The above results prove the theorem. ■

Remark 4 A similar result will be obtained for any ob-
jective function that is an increasing function of P1. For
example, let α : [0, L/2) → [0, ∞) be a strictly increasing
function. Then P ′ ≜ α(P1) is a valid objective function
that has u
∗
A in (16) and ω∗
D in (18) as the equilibrium
strategies. The value of the game is then V ′ = α(V ). The
proof relies on the fact that P1 = V along the terminal

9

surface and ˙V = 0 everywhere under the optimal strate-
gies.

Remark 5 If the intruder’s objective is to quickly reach
the perimeter, e.g., P ′ = −(tF − t0), then the optimal
intrusion strategy will be diﬀerent. In this case, the in-
truder will move straight towards the closest point on the
perimeter whenever it avoids capture. Otherwise, it will
choose the breaching point so that P1 = ε, instead of
maximizing the safe distance.

Remark 6 The shortest path towards any sB /∈ Sd con-
sists of a straight line towards the tangent point and the
path along the perimeter, which is equivalent to breach-
ing the perimeter at the tangent point. Therefore, it is
reasonable for the intruder to choose sB ∈ Sd.

In the defender winning scenario, we can consider the
following quantity which describes the distance of the
intruder from the barrier:

dbar = min
x∈RA(sD) ∥x − xA∥. (23)

This quantity can be interpreted as a buﬀer / margin
from the intruder winning conﬁguration. The defender
will want to maximize this buﬀer, whereas the intruder
can minimize dbar hoping that any “mistake” in de-
fender’s behavior will let it penetrate the barrier and
enter RA(sD).

Let the terminal payoﬀ function to be the negative of
the distance from the barrier when the capture occurs
at time tF :

P2(ωD, uA) ≜ −dbar(tF ) < 0. (24)

Note that capture is deﬁned by xA ∈ Γaﬀ(sD) (see the
paragraph before Lemma 3). The defender tries to min-
imize P2, while the intruder tries to maximize it.

Theorem 3 If the initial conﬁguration is xA /∈ RA(sD),
and if the players use P2 in (24) as the objective function,
then u
∗
A in (16) and ω∗
D in (18) form equilibrium strate-
gies, and the value of the game is V (sD, xA) in (14):

V = min
ωD max
uA P2(ωD, uA) = max
uA min
ωD P2(ωD, uA).

PROOF. Following the proof of Theorem 2, it is suﬃ-
cient to show the following identity:

−dbar(sD, xA) =
 { νJ ∗
L(sD, xA) if xA ∈ ΩL(sD)

νJ ∗
R(sD, xA) otherwise. (25)

In the following we prove the case with xA ∈ ΩL(sD).

x !

<latexit sha1_base64="lEqjW4mBdOGyfP8IR0M/J3nJskg=">AAACW3icbVDLSsQwFM3Ud30rrtwEB0FcDK0KuhLBjUsFxxGmVZL0VsPkUZJUHUo/wq1+mQv/xXRmFr4uBA7nnnvvyaGF4NZF0UcrmJqemZ2bXwgXl5ZXVtfWN26sLg2DLtNCm1tKLAiuoOu4E3BbGCCSCujRwXnT7z2BsVyrazcsIJXkQfGcM+I81Utkjl/u9u/X2lEnGhX+C+IJaKNJXd6vt06TTLNSgnJMEGv7cVS4tCLGcSagDpPSQkHYgDxA30NFJNi0Gvmt8a5nMpxr459yeMR+n6iItHYoqVdK4h7t715D/tfrly4/SSuuitKBYuNDeSmw07j5PM64AebE0APCDPdeMXskhjDnIwrDJIPcJ1IlzWaa12OC2iqhWmSNIy3q8KcbxnwE1ksVPDMtJVFZlZSUmLofpx6pDMxY5Ld4tmrHtd/hE49/5/sX3Bx04sPOwdVR++xokv082kY7aA/F6BidoQt0ibqIoQF6RW/ovfUZTAVhsDSWBq3JzCb6UcHWF/wDthQ=</latexit>

! R T

<latexit sha1_base64="n4gb7k6pGiG53Fcu7vwDt55l9gY=">AAACYHicbVBNTxsxFHQWaMMCDWlvcLGIkLgQ7YZIcKqQeumRVoREilfI9r4FC3+sbG9RtNq/0Wv7t7j2l9Sb5MDXkyyN5s0bj4aVUjifJE+daGNz68PH7na8s7v3qbff/3zjTGU5TLiRxs4YdSCFhokXXsKstEAVkzBlD9/a/fQXWCeMvvaLEjJF77QoBKc+UOSUqAL/xIQ5fH27P0iGyXLwW5CuwQCt5+q23/lKcsMrBdpzSZ2bp0nps5paL7iEJiaVg5LyB3oH8wA1VeCyehm6wceByXFhbHja4yX7/KKmyrmFYkGpqL93r3ct+d5uXvniIquFLisPmq8+KiqJvcFtAzgXFriXiwAotyJkxfyeWsp96CmOSQ5FaKUmrTMrmhXBXE2YkXmbyMgmfpmG81CBC1INj9woRXVek4pR28zTLCCdg12Jgktg60HaBI/QePq637fgZjRMz4ajH+PB5XjdfRcdoiN0glJ0ji7Rd3SFJoijEv1Gf9Dfzr+oG/Wi/koaddY3X9CLiQ7+Azgtt4o=</latexit>
 B

<latexit sha1_base64="vcuwUHqLJxSHoYR14j6nMT0BbgI=">AAACWXicbVDLSsQwFE3ra6xvZ+kmOAiuhlYFXYnoxuUIjgrTIkl6q8E8SpIqQ+k3uNVPE3/GdGYWvi4EDueee+/JoaXg1sXxRxDOzS8sLnWWo5XVtfWNza3tG6srw2DItNDmjhILgisYOu4E3JUGiKQCbunTRdu/fQZjuVbXblxCJsmD4gVnxHlqmMoCn99v9uJ+PCn8FyQz0EOzGtxvBadprlklQTkmiLWjJC5dVhPjOBPQRGlloSTsiTzAyENFJNisnrht8J5nclxo459yeMJ+n6iJtHYsqVdK4h7t715L/tcbVa44yWquysqBYtNDRSWw07j9Os65AebE2APCDPdeMXskhjDnA4qiNIfC51Gn7WZaNFOC2jqlWuStIy2a6KcbxnwE1ksVvDAtJVF5nVaUmGaUZB6pHMxU5Ld4tu4ljd/hE09+5/sX3Bz0k8P+wdVR7+xoln0H7aBdtI8SdIzO0CUaoCFiiKNX9Ibeg88wCDthNJWGwWymi35U2P0CPHa1Qg==</latexit>

sL

<latexit sha1_base64="ITghNTxkKBW//y8XWLJ/TE/YIZc=">AAACWXicbVDLSsQwFE3ra6xvXbopDoKroR0FXYngxoULBUeFaRmS9FaDeZQkVYbQb3Crnyb+jOnMLHxdCBzOPffek0MqzoxNko8gnJtfWFzqLEcrq2vrG5tb27dG1ZrCgCqu9D3BBjiTMLDMcrivNGBBONyRp/O2f/cM2jAlb+y4glzgB8lKRrH11MCM3GUz2uwmvWRS8V+QzkAXzepqtBWcZoWitQBpKcfGDNOksrnD2jLKoYmy2kCF6RN+gKGHEgswuZu4beJ9zxRxqbR/0sYT9vuEw8KYsSBeKbB9NL97Lflfb1jb8iR3TFa1BUmnh8qax1bF7dfjgmmglo89wFQz7zWmj1hjan1AUZQVUGaidFm7mZTNlCDGZUTxonWkeBP9dEOpj8B4qYQXqoTAsnBZTbBuhmnukSxAT0V+i2ddN238Dp94+jvfv+C230sPe/3ro+5Zf5Z9B+2iPXSAUnSMztAFukIDRBFDr+gNvQefYRB2wmgqDYPZzA76UeHOFz6otcU=</latexit>
 s D

<latexit sha1_base64="tTezqmZtKKITVaIF0fosg6hpYc4=">AAACWXicbVDLSsQwFE3ra6xvXbopDoKroR0FXYmgC5cKjgrTMiTprQbzKEmqDKHf4FY/TfwZ05lZ+LoQOJx77r0nh1ScGZskH0E4N7+wuNRZjlZW19Y3Nre2b42qNYUBVVzpe4INcCZhYJnlcF9pwIJwuCNP523/7hm0YUre2HEFucAPkpWMYuupgRm5i2a02U16yaTivyCdgS6a1dVoKzjNCkVrAdJSjo0Zpkllc4e1ZZRDE2W1gQrTJ/wAQw8lFmByN3HbxPueKeJSaf+kjSfs9wmHhTFjQbxSYPtofvda8r/esLblSe6YrGoLkk4PlTWPrYrbr8cF00AtH3uAqWbea0wfscbU+oCiKCugzETpsnYzKZspQYzLiOJF60jxJvrphlIfgfFSCS9UCYFl4bKaYN0M09wjWYCeivwWz7pu2vgdPvH0d75/wW2/lx72+tdH3bP+LPsO2kV76ACl6BidoUt0hQaIIoZe0Rt6Dz7DIOyE0VQaBrOZHfSjwp0vLxi1vQ==</latexit>

(a) (b)

! ⌦
L

<latexit sha1_base64="w3tOQ8ncHw1ZtYK3O+2CLlm953M=">AAACqnicZZFLb9QwEMe9KY8SXm05colYVUIIrZItEj1W6qUHDgWx20XrsLIdZ9eqH5E9KURRvgEnrvDF+DY4j0VlO5Klv38zY8+DFlI4iOM/o2Dv3v0HD/cfhY+fPH32/ODwaO5MaRmfMSONXVDiuBSaz0CA5IvCcqKo5Ff0+rz1X91w64TRn6EqeKrIWotcMAIeLXCxEV/frD6sDsbxJO4suiuSQYzRYJerw9EPnBlWKq6BSeLcMokLSGtiQTDJmxCXjheEXZM1X3qpieIurbuCm+jYkyzKjfVHQ9TR2xk1Uc5VivpIRWDjdn0t/Oc7vu1sUQHq+04BkJ+mtdBFCVyz/v+8lBGYqB1KlAnLGcjKC8Ks8C1EbEMsYeBHF2LNvzGjFNFZjbWxqlkmaY0lzwHLObcwTrAV6w1g296aMAxxxnNMXY2pkVnbiZFND1Ve47ZImm8BHQDdAtYDRrY5mX8oE66QpHJQddPtAm0f6Avy+0t2t3VXzKeT5GQy/fhufDYdNrmPXqJX6DVK0Ht0hi7QJZohhiT6iX6h38Hb4FPwJVj2ocFoyHmB/rMg+wv3vtZ4</latexit>

T

<latexit sha1_base64="XauzakTpg3ueEvTLpMaaM5CawmA=">AAACp3icZZFLb9QwEMe94VXCq4Ujl4hVJbiskrYSHCtx4UaRutuV1lFlO5Ndq35E9gSIov0GSFzho/FtcB6LynYkS3//ZsaeB6+U9JimfybRvfsPHj46eBw/efrs+YvDo5cLb2snYC6ssm7JmQclDcxRooJl5YBpruCK33zs/FdfwXlpzSU2FeSarY0spWAY0Jxyn1xeH07TWdpbcldko5iS0S6ujyY/aGFFrcGgUMz7VZZWmLfMoRQKtjGtPVRM3LA1rII0TIPP277abXIcSJGU1oVjMOnp7YyWae8bzUOkZrjx+74O/vMd33Z2qEL9fa8ALD/krTRVjWDE8H9ZqwRt0k0kKaQDgaoJggknQwuJ2DDHBIa5xdTAN2G1ZqZoqbFOb1dZ3lIFJVK1AIfTjDq53iB13W0bxzEtoAyDbSm3qug6sWo7QF22tCuSlzvAR8B3QAxAsF1OER4qpK8Uazw2/XT7QDcEhoLC/rL9bd0Vi5NZdjo7+XI2PT8bN3lAXpM35C3JyHtyTj6RCzIngkjyk/wiv6N30edoES2H0Ggy5rwi/1nE/gLgmtUx</latexit>
 d bar

<latexit sha1_base64="Sx4/t67606HQTB445blGCrOiZCk=">AAACrnicZZFLb9QwEMe94dESXi0cuUSsKnFaJQsSHCv1wrFI7LbSOlrZzmTXqh+RPQuNonwDzlzha/FtcB6LynYkS3//ZsaeB6+U9JimfybRg4ePHh8dP4mfPnv+4uXJ6aultzsnYCGssu6aMw9KGligRAXXlQOmuYIrfnPR+a++gfPSmq9YV5BrtjGylIJhQLRYU4RbbDhz7fpkms7S3pL7IhvFlIx2uT6d/KCFFTsNBoVi3q+ytMK8YQ6lUNDGdOehYuKGbWAVpGEafN70RbfJWSBFUloXjsGkp3czGqa9rzUPkZrh1h/6OvjPd3bX2aEK9e1BAVh+yhtpqh2CEcP/5U4laJNuMEkhHQhUdRBMOBlaSMSWOSYwjC+mBr4LqzUzRUONdbpdZXlDFZRI1RIcTjPq5GaL1HW3No5jWkBJuW8ot6roOrGqHaAuG9oVycs94CPgeyAGINg+pwgPFdJXitUe6366faAbAkNBYX/Z4bbui+V8lr2fzb98mJ7Px00ekzfkLXlHMvKRnJPP5JIsiCAV+Ul+kd9RGi2jPFoPodFkzHlN/rNo+xevNdjh</latexit>
! RA

<latexit sha1_base64="GhyGstqBGwviq0d3+oAxBmZpS7g=">AAACrnicZZFLb9QwEMe94VXCq4Ujl4hVJU6rZKkExyIuPRbEbiuto5XtOLtW/ZI9AaIo34Bzr+3X4tvgPBaV7UiW/v7Nw+MZaqXwkKZ/JtGDh48ePzl4Gj97/uLlq8Oj10tvKsf4ghlp3CUlnkuh+QIESH5pHSeKSn5Br750/osf3Hlh9HeoLc8V2WhRCkYgIIwtcSCITL6tP68Pp+ks7S25L7JRTNFo5+ujyW9cGFYproFJ4v0qSy3kTVeSSd7GuPLcEnZFNnwVpCaK+7zpm26T40CKpDQuHA1JT+9mNER5XysaIhWBrd/3dfCf7/ius0MW1K+9BqD8lDdC2wq4ZsP7ZSUTMEk3mKQQjjOQdRCEORG+kLAtcYRBGF+MNf/JjFJEFw3Wxql2leUNlrwELJfcwTTDTmy2gF13a+M4xgUvMfUNpkYW3U+MbAeoygZ3TdJyB+gI6A6wATCyyylCoUJ4K0ntoe6n2we6ITA0FPaX7W/rvljOZ9mH2fzryfR0Pm7yAL1F79B7lKGP6BSdoXO0QAxZdI1u0G2URssoj9ZDaDQZc96g/yza/gUVSNgr</latexit>
 ⌫sD )L

<latexit sha1_base64="xu2OKoqPYs74J+r6eUH6IueX7xk=">AAADZXicZVLLbtNAFJ0mPIqhtAXEAhZYRJXYNIrdSLCsBAsWLIpE2kqZKBqPrxMr87BmxjTWaCS+hi38Dl/AbzATu6hpr2TpzLnnXt9XVrFSm9Hoz06vf+/+g4e7j6LHT/ae7h8cPjvXslYUJlQyqS4zooGVAiamNAwuKwWEZwwustXH4L/4DkqXUnwzTQUzThaiLEpKjKfmB6+wqGM9t5+wVzV6KZUhSsmr+IubHwxGw9HG4rsg6cAAdXY2P+yd4FzSmoMwlBGtp8moMjNLlCkpAxfhWkNF6IosYOqhIBz0zG6acPGRZ/K4kMp/wsQb9maEJVzrhmdeyYlZ6tu+QP73Hd10BqoyfH2rAFN8mNlSVLUBQdv/FzWLjYzDoOK8VEANazwgVJW+hZguiSLU+HFGWMAVlZwTkVsspOJumswsZlAYzM5BmUGCVblYGqzCy0VRhHMocKYtziTLQyeSuZbkhcWhyKy4JrKOyK4J2hKUXMfkPlFe6oqRRptmM92NULVCX1C0XeT2fkO505OwnVYOzOJlJtcWq5rB1KfmsK4UDrsIWKQpNrA24Z0eD9PKNwaMrGd2kDg7HFfGOcxXoMTxmNddqjBRr7cTZ/05NM5yZ4XDbe92nDhvkT+z5PZR3QXn6TA5GaZfx4PTtDu4XfQavUXvUILeo1P0GZ2hCaLoB/qJfqHfvb/9vf6L/stW2tvpYp6jLeu/+QeJzSBK</latexit>
 d bar

<latexit sha1_base64="Sx4/t67606HQTB445blGCrOiZCk=">AAACrnicZZFLb9QwEMe94dESXi0cuUSsKnFaJQsSHCv1wrFI7LbSOlrZzmTXqh+RPQuNonwDzlzha/FtcB6LynYkS3//ZsaeB6+U9JimfybRg4ePHh8dP4mfPnv+4uXJ6aultzsnYCGssu6aMw9KGligRAXXlQOmuYIrfnPR+a++gfPSmq9YV5BrtjGylIJhQLRYU4RbbDhz7fpkms7S3pL7IhvFlIx2uT6d/KCFFTsNBoVi3q+ytMK8YQ6lUNDGdOehYuKGbWAVpGEafN70RbfJWSBFUloXjsGkp3czGqa9rzUPkZrh1h/6OvjPd3bX2aEK9e1BAVh+yhtpqh2CEcP/5U4laJNuMEkhHQhUdRBMOBlaSMSWOSYwjC+mBr4LqzUzRUONdbpdZXlDFZRI1RIcTjPq5GaL1HW3No5jWkBJuW8ot6roOrGqHaAuG9oVycs94CPgeyAGINg+pwgPFdJXitUe6366faAbAkNBYX/Z4bbui+V8lr2fzb98mJ7Px00ekzfkLXlHMvKRnJPP5JIsiCAV+Ul+kd9RGi2jPFoPodFkzHlN/rNo+xevNdjh</latexit>

sL

<latexit sha1_base64="ITghNTxkKBW//y8XWLJ/TE/YIZc=">AAACWXicbVDLSsQwFE3ra6xvXbopDoKroR0FXYngxoULBUeFaRmS9FaDeZQkVYbQb3Crnyb+jOnMLHxdCBzOPffek0MqzoxNko8gnJtfWFzqLEcrq2vrG5tb27dG1ZrCgCqu9D3BBjiTMLDMcrivNGBBONyRp/O2f/cM2jAlb+y4glzgB8lKRrH11MCM3GUz2uwmvWRS8V+QzkAXzepqtBWcZoWitQBpKcfGDNOksrnD2jLKoYmy2kCF6RN+gKGHEgswuZu4beJ9zxRxqbR/0sYT9vuEw8KYsSBeKbB9NL97Lflfb1jb8iR3TFa1BUmnh8qax1bF7dfjgmmglo89wFQz7zWmj1hjan1AUZQVUGaidFm7mZTNlCDGZUTxonWkeBP9dEOpj8B4qYQXqoTAsnBZTbBuhmnukSxAT0V+i2ddN238Dp94+jvfv+C230sPe/3ro+5Zf5Z9B+2iPXSAUnSMztAFukIDRBFDr+gNvQefYRB2wmgqDYPZzA76UeHOFz6otcU=</latexit>
 xA

<latexit sha1_base64="0MevKHPToqz5EqMkiqgEke4O+do=">AAADUHicZVLLjtMwFPW0PIbwmoElm4hqJDZTNWklWA5iw3KQaDtSHVWOczON6kdkO0wjyx/BFv6KHX/CDuymRTOdK0U5Pvf4+r7ymlXajEa/j3r9Bw8fPT5+Ej199vzFy5PTVzMtG0VhSiWT6ionGlglYGoqw+CqVkB4zmCerz8F//wbKF1J8dW0NWScXIuqrCgxnppjXsab5cflyWA0HG0tvg+SHRignV0uT3tjXEjacBCGMqL1IhnVJrNEmYoycBFuNNSErsk1LDwUhIPO7DZfF595pohLqfwnTLxlb9+whGvd8twrOTErfegL5H/f2W1noGrDNwcJmPJDZitRNwYE7d4vGxYbGYeexEWlgBrWekCoqnwJMV0RRajxnYuwgBsqOSeisFhIxd0iySxmUBrMZqDMIMGqul4ZrMLJRVGECyhxri3OJStCJZK5juSlxSHJvNwT+Y7I9wTtCEr2dwofqKh0zUirTbvt7laoOqFPKLqbpB94q1dSGaKUvAnpLsZhOp0cmMWrXG4sVg2DhQ/NYVMrHGYRsEhTbGBjwjk9H6a1LwwY2WR2kDg7nNTGOczXoMT5hDe7UKGjXm+nzvp1aJ3lzgqHu9rtJHHeIr9myeFS3QezdJiMh+mXyeAi3S3cMXqD3qJ3KEHv0QX6jC7RFFG0Rt/RD/Sz96v3p/e3f9RJe7s/eo3uWD/6B9tHGWo=</latexit>

s D

<latexit sha1_base64="tTezqmZtKKITVaIF0fosg6hpYc4=">AAACWXicbVDLSsQwFE3ra6xvXbopDoKroR0FXYmgC5cKjgrTMiTprQbzKEmqDKHf4FY/TfwZ05lZ+LoQOJx77r0nh1ScGZskH0E4N7+wuNRZjlZW19Y3Nre2b42qNYUBVVzpe4INcCZhYJnlcF9pwIJwuCNP523/7hm0YUre2HEFucAPkpWMYuupgRm5i2a02U16yaTivyCdgS6a1dVoKzjNCkVrAdJSjo0Zpkllc4e1ZZRDE2W1gQrTJ/wAQw8lFmByN3HbxPueKeJSaf+kjSfs9wmHhTFjQbxSYPtofvda8r/esLblSe6YrGoLkk4PlTWPrYrbr8cF00AtH3uAqWbea0wfscbU+oCiKCugzETpsnYzKZspQYzLiOJF60jxJvrphlIfgfFSCS9UCYFl4bKaYN0M09wjWYCeivwWz7pu2vgdPvH0d75/wW2/lx72+tdH3bP+LPsO2kV76ACl6BidoUt0hQaIIoZe0Rt6Dz7DIOyE0VQaBrOZHfSjwp0vLxi1vQ==</latexit>

! RA

<latexit sha1_base64="GhyGstqBGwviq0d3+oAxBmZpS7g=">AAACrnicZZFLb9QwEMe94VXCq4Ujl4hVJU6rZKkExyIuPRbEbiuto5XtOLtW/ZI9AaIo34Bzr+3X4tvgPBaV7UiW/v7Nw+MZaqXwkKZ/JtGDh48ePzl4Gj97/uLlq8Oj10tvKsf4ghlp3CUlnkuh+QIESH5pHSeKSn5Br750/osf3Hlh9HeoLc8V2WhRCkYgIIwtcSCITL6tP68Pp+ks7S25L7JRTNFo5+ujyW9cGFYproFJ4v0qSy3kTVeSSd7GuPLcEnZFNnwVpCaK+7zpm26T40CKpDQuHA1JT+9mNER5XysaIhWBrd/3dfCf7/ius0MW1K+9BqD8lDdC2wq4ZsP7ZSUTMEk3mKQQjjOQdRCEORG+kLAtcYRBGF+MNf/JjFJEFw3Wxql2leUNlrwELJfcwTTDTmy2gF13a+M4xgUvMfUNpkYW3U+MbAeoygZ3TdJyB+gI6A6wATCyyylCoUJ4K0ntoe6n2we6ITA0FPaX7W/rvljOZ9mH2fzryfR0Pm7yAL1F79B7lKGP6BSdoXO0QAxZdI1u0G2URssoj9ZDaDQZc96g/yza/gUVSNgr</latexit>

xA

<latexit sha1_base64="0MevKHPToqz5EqMkiqgEke4O+do=">AAADUHicZVLLjtMwFPW0PIbwmoElm4hqJDZTNWklWA5iw3KQaDtSHVWOczON6kdkO0wjyx/BFv6KHX/CDuymRTOdK0U5Pvf4+r7ymlXajEa/j3r9Bw8fPT5+Ej199vzFy5PTVzMtG0VhSiWT6ionGlglYGoqw+CqVkB4zmCerz8F//wbKF1J8dW0NWScXIuqrCgxnppjXsab5cflyWA0HG0tvg+SHRignV0uT3tjXEjacBCGMqL1IhnVJrNEmYoycBFuNNSErsk1LDwUhIPO7DZfF595pohLqfwnTLxlb9+whGvd8twrOTErfegL5H/f2W1noGrDNwcJmPJDZitRNwYE7d4vGxYbGYeexEWlgBrWekCoqnwJMV0RRajxnYuwgBsqOSeisFhIxd0iySxmUBrMZqDMIMGqul4ZrMLJRVGECyhxri3OJStCJZK5juSlxSHJvNwT+Y7I9wTtCEr2dwofqKh0zUirTbvt7laoOqFPKLqbpB94q1dSGaKUvAnpLsZhOp0cmMWrXG4sVg2DhQ/NYVMrHGYRsEhTbGBjwjk9H6a1LwwY2WR2kDg7nNTGOczXoMT5hDe7UKGjXm+nzvp1aJ3lzgqHu9rtJHHeIr9myeFS3QezdJiMh+mXyeAi3S3cMXqD3qJ3KEHv0QX6jC7RFFG0Rt/RD/Sz96v3p/e3f9RJe7s/eo3uWD/6B9tHGWo=</latexit>

RT 0

<latexit sha1_base64="a/OREX6OQAV3sPzB1ttyc7HPRTI=">AAACkXicfZHdahRBEIV7x6jJ+JPEXOamcRFFZJmJAfVuUS8CIZhINglsL6G6p2bTpH+G7h5xGfY1vNXX8m3SszsLmogFDYevTtHFKV4p6UOW/e4l99buP3i4vpE+evzk6ebW9rMzb2sncCSssu6Cg0clDY6CDAovKoegucJzfv2p7Z9/Q+elNadhVuFEw9TIUgoIETGmS/qVMu7p6cvLrX42yBZF74q8E33S1fHlds+ywopaowlCgffjPKvCpAEXpFA4T1ntsQJxDVMcR2lAo580i6Xn9EUkBS2ti88EuqB/TjSgvZ9pHp0awpW/3Wvhv3rjOpTvJ400VR3QiOVHZa1osLRNgBbSoQhqFgUIJ+OuVFyBAxFiTmmasgLLmEjDuFVFu4FV8yXUZcPa/3i5ArwDfAXEEghoZz5jjMXhUQRfKnQQrHvdMHBTDd/nMaYpe9Oq/xmlWRmjSuOJ8tsHuSvO9gb528HeyX5/uN8da53skufkFcnJOzIkB+SYjIggFflBfpJfyU7yIRkmH5fWpNfN7JC/Kjm8AYXwyl8=</latexit>
 Fig. 7. Proof of the identity dbar = −νJ ∗
L.

We ﬁrst show that the point x
∗, which is the point in
RA that is closest from xA, lies on the straight line from
xA to γ(sL) (see Fig. 7). It suﬃces to show that xA )L is
perpendicular to the tangent of the barrier ∂RA at x∗,
denoted by B.

We can treat sL as a parameter to express a point, xbar,
on the left barrier ∂RA as follows:

xbar(sL) = γ(sL) − νsD )LRT (sL),

where R ∈ R2×2 denotes the matrix for ccw rotation by
φ∗
L. The tangent is obtained by

B ≜ dxbar
dsL = T − νRT − νsD )LRT ′,

where T ′ = dT (sL)
dsL denotes the normal vector of γ. The
inner product with ˆxA )L gives

B · ˆxA )L = T · ˆxA )L − νRT · ˆxA )L − νsD )LRT ′ · ˆxA )L
= cos(φ∗
L) − ν(ˆxA )L · ˆxA )L) − 0
= 0,

where from the ﬁrst to second line we used RT = ˆxA )L
and RT ′ · ˆxA )L = 0.

Now, the distance between xA and x∗ is

dbar = ∥xA )L∥ − νsD )L = −νJ ∗
L.

The case with xA ∈ ΩR can be shown similarly. ■

Unlike the intruder strategy, it is easy to see that the
defender strategy will stay the same even if the objective
is chosen to be the minimum time capture.

3.4 Special Cases

This section discusses how the results provided in the
preceding sections accommodate the two special cases
considered in [39]: circular perimeter, and equal speed.

10
(a)
 D

r

<latexit sha1_base64="nN/PHWuXGKQNotyTsdfhJZyDhCA=">AAAB+nicbVDLSgMxFM34rOOr6tJNsAiuykwRdFlw47IF+4DOUDLpnTY0yQxJRihjv8Ct/oA7cevPuPdDzLSz0NYDFw7n3Jvce6KUM20878vZ2Nza3tmt7Ln7B4dHx9WT065OMkWhQxOeqH5ENHAmoWOY4dBPFRARcehF07vC7z2C0iyRD2aWQijIWLKYUWKs1FbDas2rewvgdeKXpIZKtIbV72CU0EyANJQTrQe+l5owJ8owymHuBpmGlNApGcPAUkkE6DBfLDrHl1YZ4ThRtqTBC/X3RE6E1jMR2U5BzESveoX4nzfITHwb5kymmQFJlx/FGccmwcXVeMQUUMNnlhCqmN0V0wlRhBqbjesGI4gDEedB8XIUz10bi78awjrpNuq+V/fb17Vmowyogs7RBbpCPrpBTXSPWqiDKAL0jF7Qq/PkvDnvzseydcMpZ87QHzifPy6ak+Y=</latexit>
 D

! A

<latexit sha1_base64="FecSmqLTbluc/L3NBkAj/eGKbJk=">AAACqHicZZFLb9QwEMe9KdASXi0cuUSsKiEOq2SLBMciLhwXid0tWkcr23F2Tf2I7EkhivINOHBtv1m/Dc5jUdmOZOnv38zY86CFFA7i+HYUHDx4+Ojw6HH45Omz5y+OT14unCkt43NmpLEXlDguheZzECD5RWE5UVTyJb383PqXV9w6YfQ3qAqeKrLRIheMgEcLXDix/rQ+HseTuLPovkgGMUaDzdYno984M6xUXAOTxLlVEheQ1sSCYJI3IS4dLwi7JBu+8lITxV1ad+U20aknWZQb64+GqKN3M2qinKsU9ZGKwNbt+1r4z3d619miAtSvvQIg/5jWQhclcM36//NSRmCidiRRJixnICsvCLPCtxCxLbGEgR9ciDX/yYxSRGc11saqZpWkNZY8BywX3MI4wVZstoBte2vCMMQZzzF1NaZGZm0nRjY9VHmN2yJpvgN0AHQHWA8Y2eVk/qFMuEKSykHVTbcLtH2gL8jvL9nf1n2xmE6Ss8n06/vx+XTY5BF6jd6gtyhBH9A5+oJmaI4Y+oH+oGt0E7wLZsEy+N6HBqMh5xX6zwL6F3Zc1dw=</latexit>
 R
 <latexit sha1_base64="Rijjt9tGQbn+xBj/sukGMgEMGqk=">AAACo3icZZFLa9wwEMe17it1X0l67MV0WehpsbeF9hjopdBLErKbwMoEWR7viuhhpHFbY/wJ2mPz4fptKj+2pJsBwV+/mZHmkZVSOIzjP5PgwcNHj58cPA2fPX/x8tXh0fHKmcpyWHIjjb3KmAMpNCxRoISr0gJTmYTL7OZz57/8BtYJoy+wLiFVbKNFIThDj87Orw+n8TzuLbovklFMyWin10eTXzQ3vFKgkUvm3DqJS0wbZlFwCW1IKwcl4zdsA2svNVPg0qavtI1mnuRRYaw/GqOe3s1omHKuVpmPVAy3bt/XwX++2V1nh0pUP/YKwOJT2ghdVgiaD/8XlYzQRN00olxY4ChrLxi3wrcQ8S2zjKOfWUg1fOdGKabzhmpjVbtO0oZKKJDKFVicJtSKzRap7W5tGIY0h4JmrqGZkXnXiZHtAFXR0K7IrNiBbATZDvABcLbLyf1DuXClZLXDup9uH2iHQF+Q31+yv637YrWYJ+/ni7MP05PFuMkD8oa8Je9IQj6SE/KFnJIl4QTIT/Kb3Aaz4GtwHlwMocFkzHlN/rMg/QtMQtO0</latexit>
 

<latexit sha1_base64="6JYNjMJyhI+bdXOf9gcW6nKCwNU=">AAACqHicZZFLj9MwEMfd8NglvHbhyCWiWglxqJKCBMeVuHAsEm0X1dHKdiatWT8ie8ISRf0GHLjCN+Pb4CQtWrojWfr7NzP2PHilpMc0/TOK7ty9d//o+EH88NHjJ09PTp8tvK2dgLmwyroLzjwoaWCOEhVcVA6Y5gqW/OpD519+A+elNZ+xqSDXbG1kKQXDgBYUN4Ds8mScTtLektsi24kx2dns8nT0gxZW1BoMCsW8X2VphXnLHEqhYBvT2kPFxBVbwypIwzT4vO3L3SZngRRJaV04BpOe3sxomfa+0TxEaoYbf+jr4D/f2U1nhyrU3w8KwPJ93kpT1QhGDP+XtUrQJt1IkkI6EKiaIJhwMrSQiA1zTGAYXEwNXAurNTNFS411ervK8pYqKJGqBTgcZ9TJ9Qap627bOI5pASXlvqXcqqLrxKrtAHXZ0q5IXu4B3wG+B2IAgu1zivBQIX2lWOOx6afbB7ohMBQU9pcdbuu2WEwn2ZvJ9NPb8fl0t8lj8oK8JK9IRt6Rc/KRzMicCPKV/CS/yO/odTSLltGXITQa7XKek/8s4n8B1K7WBg==</latexit>
 ! R

<latexit sha1_base64="0POYid9V6qXhTfokTyo/EVNhOOI=">AAACp3icZZFLj9MwEMfd8FrCaxeOXCKqleBSNQUJjitx4caCaLdSHa1sZ9Ja60dkT4AoyjdA4gofjW+D8yhauiNZ+vs3M/Y8eKmkx/n8zyS6dfvO3XtH9+MHDx89fnJ88nTlbeUELIVV1q0586CkgSVKVLAuHTDNFVzwq/ed/+IrOC+t+YJ1CZlmWyMLKRgGtKSmSj5fHk/ns3lvyU2RjmJKRju/PJn8oLkVlQaDQjHvN+m8xKxhDqVQ0Ma08lAyccW2sAnSMA0+a/pq2+Q0kDwprAvHYNLT6xkN097XmodIzXDnD30d/Oc7ve7sUIn6+0EBWLzLGmnKCsGI4f+iUgnapJtIkksHAlUdBBNOhhYSsWOOCQxzi6mBb8JqzUzeUGOdbjdp1lAFBVK1AofTlDq53SF13a2N45jmUFDuG8qtyrtOrGoHqIuGdkXyYg/4CPgeiAEIts/Jw0O59KVitce6n24f6IbAUFDYX3q4rZtitZilr2eLT2+mZ4txk0fkOXlBXpKUvCVn5AM5J0siiCQ/yS/yO3oVfYxW0XoIjSZjzjPyn0XsL/sc1Ts=</latexit>

! !

<latexit sha1_base64="0oyU3cKDigsima7N0qc1YsS9h94=">AAACqHicZZFLj9MwEMfd8FrCaxeOXCKqldAeqqQgwXElLhyLRNtFdVjZjtOa9Uv2BIiifAMOXOGb8W1wHkVLdyRLf/9mxp4HtVJ4SNM/k+jW7Tt37x3djx88fPT4yfHJ05U3lWN8yYw07oISz6XQfAkCJL+wjhNFJV/Tq3edf/2VOy+M/gi15bkiWy1KwQgEtMJ2Jz6fXR5P01naW3JTZKOYotEWlyeTH7gwrFJcA5PE+02WWsgb4kAwydsYV55bwq7Ilm+C1ERxnzd9uW1yGkiRlMaFoyHp6fWMhijva0VDpCKw84e+Dv7znV53dsiC+n5QAJRv80ZoWwHXbPi/rGQCJulGkhTCcQayDoIwJ0ILCdsRRxiEwcVY82/MKEV00WBtnGo3Wd5gyUvAcsUdTDPsxHYH2HW3No5jXPASU99gamTRdWJkO0BVNrgrkpZ7QEdA94ANgJF9ThEeKoS3ktQe6n66faAbAkNBYX/Z4bZuitV8lr2azT+8np7Px00eoefoBXqJMvQGnaP3aIGWiKEv6Cf6hX5HZ9EiWkefhtBoMuY8Q/9ZRP8CJ53VuQ==</latexit>
 ⌦

<latexit sha1_base64="NKoEaCUi1pafGN9ZdCgaGImyG+A=">AAACqHicdZFLbxMxEMed5VWWVwtHLhZRJcQh2k2gTW+VuHAMEkmK4lVle72JqR8re7YQrfYbcOAK34xvg3c3QaUSI1n6+zcz9jxYqaSHJPk9iO7cvXf/wcHD+NHjJ0+fHR49X3hbOS7m3CrrLhj1Qkkj5iBBiYvSCaqZEkt29b71L6+F89KaT7AtRabp2shCcgoBLQhV5YZeHg6T0cnZeJK8w8koCTadBpEmZ5PJCU47kiRDtLPZ5dHgO8ktr7QwwBX1fpUmJWQ1dSC5Ek1MKi9Kyq/oWqyCNFQLn9VduQ0+DiTHhXXhGMAdvZlRU+39VrMQqSls/G1fC//6jm86W1SC/narACimWS1NWYEwvP+/qBQGi9uR4Fw6wUFtg6DcydAC5hvqKIcwuJgY8ZVbranJa2Ks080qzWqiRAFELYSDYUqcXG+AuPbWxHFMclEQ5mvCrMrbTqxqeqiLmrRFsmIP2A6wPeA94HSfk4eHculLRbcett10u0DXB4aCwv72S8L/F4vxKJ2Mxh/fDs/Hu00eoJfoFXqNUnSKztEHNENzxNEX9AP9RL+iN9EsWkaf+9BosMt5gf6xiP0BOcbWNQ==</latexit>

x A

<latexit sha1_base64="IpvmRP4uopQgWGE/lBrOcRl9Mho=">AAACbXicbVHLbtQwFPWEQssU6AOxoqosRghWo2SK1C6L2HQ5SEyn0iQa2Tc3rTV+RLYDjKJ8RLfwZXwFv1BnkgVtuZKlo3OPr4/P5aUUzsfxn0H0ZOvps+2d58PdFy9f7e0fHF46U1nAGRhp7BVnDqXQOPPCS7wqLTLFJc756kvbn39H64TR3/y6xEyxay0KAcwHap6qgv5cfl7uj+JxvCn6GCQ9GJG+psuDwTTNDVQKtQfJnFskcemzmlkvQGIzTCuHJYMVu8ZFgJopdFm98dvQ94HJaWFsONrTDfvvjZop59aKB6Vi/sY97LXk/3qLyhdnWS10WXnU0D1UVJJ6Q9vP01xYBC/XATCwInilcMMsAx8iGg7THIuQSJ22k3nRdAR3dcqNzFtHRvakgk4FLDD3/QGEUFzQafwBRimm8zqtOLPNIskC0jnaThTmBrYeJU2YEXaQPEz8MbicjJOT8eTrp9H5pN/GDnlL3pGPJCGn5JxckCmZESArckt+kd+Dv9Gb6Cg67qTRoL/zmtyr6MMdvyG9hQ==</latexit>x A

<latexit sha1_base64="IpvmRP4uopQgWGE/lBrOcRl9Mho=">AAACbXicbVHLbtQwFPWEQssU6AOxoqosRghWo2SK1C6L2HQ5SEyn0iQa2Tc3rTV+RLYDjKJ8RLfwZXwFv1BnkgVtuZKlo3OPr4/P5aUUzsfxn0H0ZOvps+2d58PdFy9f7e0fHF46U1nAGRhp7BVnDqXQOPPCS7wqLTLFJc756kvbn39H64TR3/y6xEyxay0KAcwHap6qgv5cfl7uj+JxvCn6GCQ9GJG+psuDwTTNDVQKtQfJnFskcemzmlkvQGIzTCuHJYMVu8ZFgJopdFm98dvQ94HJaWFsONrTDfvvjZop59aKB6Vi/sY97LXk/3qLyhdnWS10WXnU0D1UVJJ6Q9vP01xYBC/XATCwInilcMMsAx8iGg7THIuQSJ22k3nRdAR3dcqNzFtHRvakgk4FLDD3/QGEUFzQafwBRimm8zqtOLPNIskC0jnaThTmBrYeJU2YEXaQPEz8MbicjJOT8eTrp9H5pN/GDnlL3pGPJCGn5JxckCmZESArckt+kd+Dv9Gb6Cg67qTRoL/zmtyr6MMdvyG9hQ==</latexit>
 (b)

Fig. 8. Circular perimeter case. (a) States [r, θ] and the in-
truder’s heading angle ψA. (b) Computation of the approach
angle φ∗.

When the perimeter is a circle with radius R, the sym-
metry allows us to reduce the state space to [r, θ], where
r is the intruder’s radial distance from the perimeter,
and θ ∈ [−π, π] is the relative polar angle between the
defender and the intruder with respect to the center of
the circle.

Whether the intruder is in the left region or the right
region is determined by the sign of θ: xA ∈ ΩL(sD) if
θ > 0, and xA ∈ ΩR(sD) if θ < 0. The singular surfaces
correspond to the lines θ = 0 and θ = ±π. The intruder
control is parameterized by its speed vA and the heading
ψA as shown in Fig. 8a.

Theorem 4 (from [39]) For a circular perimeter, the
optimal strategies are

ω∗
D = sgn(θ), and (26)

(v∗
A, ψ∗
A) = (ν, sgn(θ) sin
−1 ( νR
R + r
 )) , (27)

and the value of the game is

V (r, θ; ν) = |θ| − F (r) + F (0), (28)

where

F (r) =
 √( R + r
νR
 )2 − 1 − cos−1 ( νR
R + r
 ) . (29)

The sign function accommodates the switching between
the left and the right regions.

The intrusion strategy allows further geometric inter-
pretation: the optimal path of the intruder is to move
towards the tangent point of the circle with radius νR
(see Fig. 8b) [39]. To verify this result with the strategy
 given in (16), we compute the approach angle as follows.
The angle α in Fig. 8b is α = sin
−1 ( νR
R ) = sin
−1(ν).
The approach angle is φ∗ = π − π
2 − α = π
2 − sin
−1(ν),
which gives the relation φ∗ = cos
−1(ν). Recalling the re-
sults in (4), the circular case matches with our analysis
in this paper.

The other special case is when the speed ratio is ν =
1. Notice that the objective function now has the form
J ∗
L = sD )L − ∥xA )L∥, in which case the level set V = 0
is generated by the locus of intruder positions where
∥xA )L∥ = sD )L (and similarly for the right breaching
points). In addition, recalling Remark 1, the optimal
breaching points are sL = stan,L and sR = stan,R. These
properties are suﬃcient to see that the barrier ∂RA is
given by a curve called the involute — a locus of the tip
of a taut string unwound from the geometry. The left and
the right part of the barrier corresponds to unwinding
the string in ccw and cw directions.

4 Two vs. One Game

The next building block is the game played between two
defenders (Di, Dj) and one intruder. The states of the
system are now [sDi, sDj , xA]. We follow the same struc-
ture as the previous section and discuss both the game
of kind and the game of degree.

4.1 Geometries

A naive extension of the one vs. one game will conclude
that the intruder will win if it is in the winning region
against both defenders Di and Dj, i.e., if xA is in

RI ≜ {x | V (sDi, x) > 0 and V (sDj , x) > 0}. (30)

The subscript I is used to reﬂect the fact that the games
against Di and Dj are independently considered. How-
ever, in reality, the optimal intrusion strategy and the
winning regions cannot be obtained by treating Di and
Dj separately, since the intruder must avoid both Di
and Dj simultaneously.

Observe that now the game space is divided into two
parts by Γaﬀ(sDi) and Γaﬀ(sDj ) (see Fig. 9a). We showed
in Sec. 3.2 that the intruder cannot win if it reaches
the aﬀerent surface, so xA ∈ Γaﬀ(sDi) ∪ Γaﬀ(sDj ) is a
part of the terminal condition. Since xA cannot cross
these surfaces, we focus our attention on the part of the
game space that contains the intruder (shaded region
in Fig. 9a) and ignore the other. Without the loss of
generality, we deﬁne Di to be the one on the cw side and
Dj to be the one on ccw side (Fig. 9a).

The opposite point s
op
D was important in the one vs. one
game because it was the farthest point from a single de-

11

irrelevant  region
 R i

<latexit sha1_base64="PxwyXJw/IC8OCdDfOInLcNouEFA=">AAACr3icZZFLb9QwEMe94VXCqy1HLhGrSpxWSUGix0pcemwrdrfSOiy24+xa9SPYE2hk5Rtw50o/Ft8GJ5tFZTuSpb9/M2PPg1ZSOEjTP6PowcNHj5/sPY2fPX/x8tX+weHMmdoyPmVGGntFieNSaD4FAZJfVZYTRSWf0+tPnX/+nVsnjP4MTcVzRVZalIIRCCjHisCaEekv26VY7o/TSdpbcl9kgxijwc6XB6OfuDCsVlwDk8S5RZZWkHtiQTDJ2xjXjleEXZMVXwSpieIu933VbXIUSJGUxoajIenp3QxPlHONoiGyq9Lt+jr4z3d019mhCtTNTgFQnuRe6KoGrtnm/7KWCZikm0xSCMsZyCYIwqwILSRsTSxhEOYXY81/MKMU0YXH2ljVLrLcY8lLwHLGLYwzbMVqDdh2tzaOY1zwElPnMTWy6Doxst1AVfp+8rTcAjoAugXMb3czkCI8VAhXSdI4aPrp9oF2ExgKCvvLdrd1X8yOJ9n7yfHFh/HpybDJPfQGvUXvUIY+olN0hs7RFDH0Df1Cv9FtlEXz6Ev0dRMajYac1+g/i8RfVsTZKA==</latexit>

R j

<latexit sha1_base64="RHQ6Tx3Yr3vsXfEbfIP9m1NWN5o=">AAACr3icZZFLb9QwEMe94VXCq4Ujl4hVJU6rpFSix0pceiwVu1tpHRbbcXZN/Qj2BIisfIPeuZaPxbfByWZR2Y5k6e/fzNjzoJUUDtL0zyi6d//Bw0d7j+MnT589f7F/8HLmTG0ZnzIjjb2kxHEpNJ+CAMkvK8uJopLP6dWHzj//zq0TRn+CpuK5IistSsEIBJRjRWDNiPQX7fLrcn+cTtLekrsiG8QYDXa+PBhd48KwWnENTBLnFllaQe6JBcEkb2NcO14RdkVWfBGkJoq73PdVt8lhIEVSGhuOhqSntzM8Uc41iobIrkq36+vgP9/hbWeHKlA/dwqA8iT3Qlc1cM02/5e1TMAk3WSSQljOQDZBEGZFaCFha2IJgzC/GGv+gxmliC481saqdpHlHkteApYzbmGcYStWa8C2u7VxHOOCl5g6j6mRRdeJke0GqtL3k6flFtAB0C1gfrubgRThoUK4SpLGQdNPtw+0m8BQUNhftrutu2J2NMneTY4+Ho9PT4ZN7qHX6A16izL0Hp2iM3SOpoihb+gXukG/oyyaR5+jL5vQaDTkvEL/WST+AlkD2Sk=</latexit>

R mid

<latexit sha1_base64="mjNP20PQha8S8e12Kn/tDNbMZvA=">AAACunicZZHNbtQwEMe94aMlfG1B4sIlYlWJ0yppkeiBQyUuHAtit5XW0cp2nF1r/RHZE9rI5A14Cq7wQrwNTjaLynYkS//8ZhzPzJ9WUjhI0z+j6N79Bw8PDh/Fj588ffZ8fPRi7kxtGZ8xI429osRxKTSfgQDJryrLiaKSX9LNxy5/+Y1bJ4z+Ck3Fc0VWWpSCEQhoOX6FFYE1I9J/aZcY+A14JYp2OZ6k07SP5K7IBjFBQ1wsj0Y/cGFYrbgGJolziyytIPfEgmCStzGuHa8I25AVXwSpieIu9/0AbXIcSJGUxoajIenp7RueKOcaRUNl167bz3XwX+74drJDFaibvQagPMu90FUNXLPt+2UtEzBJt6SkEJYzkE0QhFkRRkjYmljCIKwyxppfM6MU0YXH2ljVLrLcY8lLwHLOLUwybMVqDdh2X20cx7jgJabOY2pk0U1iZLuFqvS9BbTcAToAugPM70waSBF+VAhXSdI4aPrt9oV2WxgaCv5l+27dFfOTaXY6Pfn8bnJ+Njh5iF6jN+gtytB7dI4+oQs0Qwx9Rz/RL/Q7+hDRSESbbWk0Gu68RP9FBH8BQ9zdnQ==</latexit>
s mid

<latexit sha1_base64="3BNA7rIIGTYzJ7vqpyxGExlezeg=">AAACrnicZZFLa9wwEMe17iOp+0raYy+mS6CnxU4DzTGQS48pdDeBlVkkebwrooeRZtsY42/Qc6/t1+q3qfzYkm4GBH/9ZkaaB6+U9JimfybRo8dPnh4cPoufv3j56vXR8ZuFt1snYC6ssu6GMw9KGpijRAU3lQOmuYJrfnvZ+a+/gfPSmq9YV5BrtjaylIJhQNSvKMIdNloW7epoms7S3pKHIhvFlIx2tTqe/KCFFVsNBoVi3i+ztMK8YQ6lUNDGdOuhYuKWrWEZpGEafN70RbfJSSBFUloXjsGkp/czGqa9rzUPkZrhxu/7OvjPd3Lf2aEK9d1eAVie54001RbBiOH/cqsStEk3mKSQDgSqOggmnAwtJGLDHBMYxhdTA9+F1ZqZoqHGOt0us7yhCkqkagEOpxl1cr1B6rpbG8cxLaCk3DeUW1V0nVjVDlCXDe2K5OUO8BHwHRADEGyXU4SHCukrxWqPdT/dPtANgaGgsL9sf1sPxeJ0ln2cnX45m16cj5s8JO/Ie/KBZOQTuSCfyRWZE0Eq8pP8Ir+jNFpEebQaQqPJmPOW/GfR5i/et9j7</latexit>
 A1

A2
 sD i

<latexit sha1_base64="C92ZrnvK68y4cZfJiWB3G2bYWR4=">AAACqXicZZFLa9wwEMe1Ttuk7itJj72YLoFCYbHTQHMMNIceE+g+6MoskizvitXDSOO2xvgb9JJr+8n6bSo/tqSbAcFfv5mR5kELKRzE8Z9RcPDo8ZPDo6fhs+cvXr46PjmdOVNaxqfMSGMXlDguheZTECD5orCcKCr5nG4/tf75N26dMPoLVAVPFVlrkQtGwKO5W9XXK9GsjsfxJO4seiiSQYzRYDerk9FPnBlWKq6BSeLcMokLSGtiQTDJmxCXjheEbcmaL73URHGX1l29TXTmSRblxvqjIero/YyaKOcqRX2kIrBx+74W/vOd3Xe2qAD1Y68AyC/TWuiiBK5Z/39eyghM1M4kyoTlDGTlBWFW+BYitiGWMPCTC7Hm35lRiuisxtpY1SyTtMaS54DljFsYJ9iK9QawbW9NGIY44zmmrsbUyKztxMimhyqvcVskzXeADoDuAOsBI7uczD+UCVdIUjmouul2gbYP9AX5/SX723ooZueT5MPk/PZifHUxbPIIvUFv0TuUoI/oCn1GN2iKGNqiO/QL/Q7eB7fBIvjahwajIec1+s8C9hfd9tZ2</latexit>

s D j

<latexit sha1_base64="EYozLpmqzcM+Qg/XBipVqpLKL2g=">AAACqXicZZFLa9wwEMe17it1X0l77MV0CRQKi50E2mOgOfSYQPdBV2aRZHlXXT2MNG5rjL9BLr0mn6zfpvJjS7oZEPz1mxlpHrSQwkEc/xkFDx4+evzk4Gn47PmLl68Oj17PnCkt41NmpLELShyXQvMpCJB8UVhOFJV8TrefW//8B7dOGP0VqoKniqy1yAUj4NHcreqL1fdmdTiOJ3Fn0X2RDGKMBrtcHY2ucWZYqbgGJolzyyQuIK2JBcEkb0JcOl4QtiVrvvRSE8VdWnf1NtGxJ1mUG+uPhqijdzNqopyrFPWRisDG7fta+M93fNfZogLUr70CIP+U1kIXJXDN+v/zUkZgonYmUSYsZyArLwizwrcQsQ2xhIGfXIg1/8mMUkRnNdbGqmaZpDWWPAcsZ9zCOMFWrDeAbXtrwjDEGc8xdTWmRmZtJ0Y2PVR5jdsiab4DdAB0B1gPGNnlZP6hTLhCkspB1U23C7R9oC/I7y/Z39Z9MTuZJKeTk6uz8fnZsMkD9Ba9Q+9Rgj6ic/QFXaIpYmiLfqMbdBt8CK6CRfCtDw1GQ84b9J8F7C/gNtZ3</latexit>

smid

<latexit sha1_base64="iwJ5R2AmAFfcAuhVYy+DMcZ4Eeg=">AAACrnicZZFLa9wwEMe17iOp+0raYy+mS6CnxU4D6TGQS48pdDeBlVkkebwrooeRZtsY42/Qc6/t1+q3qfzYkm4GBH/9ZkaaB6+U9JimfybRo8dPnh4cPoufv3j56vXR8ZuFt1snYC6ssu6GMw9KGpijRAU3lQOmuYJrfnvZ+a+/gfPSmq9YV5BrtjaylIJhQNSvKMIdNloW7epoms7S3pKHIhvFlIx2tTqe/KCFFVsNBoVi3i+ztMK8YQ6lUNDGdOuhYuKWrWEZpGEafN70RbfJSSBFUloXjsGkp/czGqa9rzUPkZrhxu/7OvjPd3Lf2aEK9d1eAVh+yhtpqi2CEcP/5VYlaJNuMEkhHQhUdRBMOBlaSMSGOSYwjC+mBr4LqzUzRUONdbpdZnlDFZRI1QIcTjPq5HqD1HW3No5jWkBJuW8ot6roOrGqHaAuG9oVycsd4CPgOyAGINgupwgPFdJXitUe6366faAbAkNBYX/Z/rYeisXpLPs4O/1yNr04Gzd5SN6R9+QDycg5uSCfyRWZE0Eq8pP8Ir+jNFpEebQaQqPJmPOW/GfR5i/dg9j3</latexit>

(a) (b)

! a ! ( s D i )

<latexit sha1_base64="owd8s3qh9prcvb0lq1LEoQ+lFVc=">AAACrHicfZHdahQxFMez41cdP7rVS28Gl0IVWWaqYC8LFvRGrNBtC5thOJM52YYmkyHJSJcwT+DTeKtP4tuY2Z2F2ooHQv78zjmc5H/KRgrr0vT3KLpz9979B1sP40ePnzzdHu88O7W6NQxnTEttzkuwKEWNMyecxPPGIKhS4ll5+aHPn31DY4WuT9yywVzBohZcMHABFeNdWmpZ2aUKF/0ISkFBHV45D5x3e7bwR4XoXhXjSTpNV5HcFtkgJmSI42JnpGmlWauwdkyCtfMsbVzuwTjBJHYxbS02wC5hgfMga1Boc7/6T5fsBlIlXJtwapes6PUOD8r2Tw6VCtyFvZnr4b9y89bxg9yLumkd1mw9iLcycTrpzUkqYZA5uQwCmBHhrQm7AAPMBQvjOKYVclpaf820bg0V97SfV/INKAdQbgBbAwZ9zxEGWwx+DuBLgwacNq89BbNQcNUFmxb0Ta/+VyjqTWFQcVhRdnMht8Xp/jR7O93/+m5yeDAsa4u8IC/JHsnIe3JIPpFjMiOMfCc/yE/yK5pGJ9E8ytel0WjoeU7+ioj/AVZP1p8=</latexit>

! a ) ( s D j )

<latexit sha1_base64="JrLCdfbnjkyurnwG93SDlPU6aD4=">AAACrHicfZHdatRAFMdn41eNX1u99Ca4FKrIklTBXhYs6I1YodsWdkI4mZzZjp2PMDORLiFP4NN4q0/i2zjZzUJtxQPD/Pmdczgz/1PWUjifpr9H0a3bd+7e27ofP3j46PGT8fbTE2cay3DGjDT2rASHUmiceeElntUWQZUST8uL933+9BtaJ4w+9ssacwULLbhg4AMqxju0NLJySxUu+gGUgoJ6vPQtcN7tuqI9LL52L4vxJJ2mq0huimwQEzLEUbE9MrQyrFGoPZPg3DxLa5+3YL1gEruYNg5rYBewwHmQGhS6vF39p0t2AqkSbmw42icrerWjBeX6J4dKBf7cXc/18F+5eeP5ft4KXTceNVsP4o1MvEl6c5JKWGReLoMAZkV4a8LOwQLzwcI4jmmFnJauvWJat4aKt7SfV/INKAdQbgBbAwZ9zyEGWyx+CuBzjRa8sa9aCnah4LILNi3o6179r1DoTWFQcVhRdn0hN8XJ3jR7M9378nZysD8sa4s8Jy/ILsnIO3JAPpIjMiOMfCc/yE/yK5pGx9E8ytel0WjoeUb+ioj/AVhz1qA=</latexit>
 sD j

<latexit sha1_base64="ErWcZBBW2w5di+CNXXOae+d5PKs=">AAACjHicfZFtS9xAEMf3YmttrNaHl30Teggi5UisUKEIgiJ9U2qh5wmX45jdTM719iHsbopHyIfwrf1k/TZu7nLQaunAwp/f/IeZnaGF4NbF8e9OsPLi5eqrtdfh+puNzbdb2ztXVpeGYZ9poc01BYuCK+w77gReFwZBUoEDOj1r8oOfaCzX6oebFTiSMFE85wycRwM7rs7Ht/V4qxv34nlEz0XSii5p43K83dFpplkpUTkmwNphEhduVIFxnAmsw7S0WACbwgSHXiqQaEfVfN462vMki3Jt/FMumtM/KyqQ1s4k9U4J7sY+zTXwX7lh6fLjUcVVUTpUbNEoL0XkdNR8Psq4QebEzAtghvtZI3YDBpjzKwrDMM0wT6mtUqpF1kygRb2AMq/Sph/Nl4C2gC4BWwAGTc05+rUY/OrBtwINOG0OqhTMRMJd7dc0ST806n9GrpZGr0J/ouTpQZ6Lq8Ne8rF3+P2oe3rcHmuNvCPvyT5JyCdySr6QS9InjEzJPXkgv4LN4Cj4HJwsrEGnrdklf0Vw8Qg6Ysl7</latexit>
 sDi

<latexit sha1_base64="8UuBJruOmilwF8iVDTmgQQfu22U=">AAACjHicfZFtSxtBEMc319ra0/pQX/bN0SCIlHCnQgUpCJXSN0ULjRFyIczuzSVL9uHY3ZOG4z5E3+on89t0L7mA1dKBhT+/+Q8zO0MLwa2L44dO8OLl2qvX62/Cjc23W9s7u++urS4Nwz7TQpsbChYFV9h33Am8KQyCpAIHdPalyQ9u0Viu1U83L3AkYaJ4zhk4jwZ2XF2MeT3e6ca9eBHRc5G0okvauBrvdnSaaVZKVI4JsHaYxIUbVWAcZwLrMC0tFsBmMMGhlwok2lG1mLeO9j3Jolwb/5SLFvRxRQXS2rmk3inBTe3TXAP/lRuWLj8dVVwVpUPFlo3yUkROR83no4wbZE7MvQBmuJ81YlMwwJxfURiGaYZ5Sm2VUi2yZgIt6iWUeZU2/Wi+ArQFdAXYEjBoai7Qr8Xgdw8uCzTgtDmsUjATCb9qv6ZJ+rFR/zNytTJ6FfoTJU8P8lxcH/WS497Rj5Pu+Wl7rHXynnwgByQhn8g5+UauSJ8wMiO/yR25D7aCk+As+Ly0Bp22Zo/8FcHXPzg/yXo=</latexit>

Fig. 9. Regions in the two vs. one game. (a) Game space
divided by the two aﬀerent surfaces. (b) Further division
into three regions based on the location of the left and right
breaching points.

fender. The analogy in the two vs. one game is the mid-
point, smid, between the two defenders, which achieves
the maximum distance from the nearest defender.

In deriving the intruder strategy, we consider the follow-
ing quantity:

Jij = min{sDi )B, sB )Dj } − 1
ν ∥γ(sB) − xA∥, (31)

where the subscript ij denotes the indices of the de-
fenders. The interpretation is similar to JL and JR in
Sec. 3. It is the expected safe distance assuming that (i)
Di moves ccw, (ii) Dj moves cw, and (iii) the intruder
moves on a straight line path towards some breaching
point sB ∈ [sDi, sDj ].

For this function, we can consider three cases depending
on where sB lies in:

Jij =
 



 JL(sB; sDi, xA) if sB ∈ [sDismid)

JR(sB; sDj , xA) if sB ∈ (smidsDj ]

Jmid(sDi, sDj , xA) otherwise: i.e., sB = smid,

(32)

where

Jmid ≜ 1
2 sDi )Dj − 1
ν ∥γ(smid) − xA∥ (33)

describes how much longer it takes for the defenders to
reach smid than it does for the intruder. The division
described above is possible because only Di’s position is
active in the calculation of Jij when the breaching point
is in [sDi, smid), and similarly only Dj’s position matters
when sB ∈ (smid, sDj ].

Following the above decomposition, the game space that
contains the intruder can be further divided into three

-0.2

-0.2-0.2
-0.1-0.1
-0.1
-0.1-0.1-0.100
00000.1
 0.1

0.10.1
0.2
 0.3

sD i

<latexit sha1_base64="PcJMuoqBqtoWl152IbP6BLtEXtQ=">AAACbXicbZHNatwwEMe1btqmm34kLT0lBNOltKfF3gaSYyA99LiFbjawNos0Hidi9WEkuWERfohemyfLU+QVKq99aD4GBH9+89doNMMqwa1LkttB9Gzr+YuX26+GO6/fvH23u/f+3OraAM5AC20uGLUouMKZ407gRWWQSiZwzlZnbX7+G43lWv1y6wpzSS8VLzlQF9DcLv33JW+Wu6NknGwifizSXoxIH9Pl3mCaFRpqicqBoNYu0qRyuafGcRDYDLPaYkVhRS9xEaSiEm3uN/028edAirjUJhzl4g39/4an0tq1ZMEpqbuyD3MtfCq3qF15knuuqtqhgu6hshax03H7+bjgBsGJdRAUDA+9xnBFDQUXRjQcZgWWmSx91lZmZdMBZn3GtCjajrTooYTOBTSQ+/0BhKHY4FN4DVpKqgqf1YyaZpHmQakCTWcKdQP1o7QJNcIO0ocTfyzOJ+P023jy82h0Oum3sU32ySfylaTkmJySH2RKZgTIivwhf8nN4C76GB1Eh501GvR3PpB7EX35B59ZvfQ=</latexit>
s D j

<latexit sha1_base64="+ThZJtGTqC4BOQipD+1AWclGq2A=">AAACbXicbZHbatwwEIa17indHpI05KqhmC6lvVrsbaG5DCQXudxCNxtYm0UajxN1dTCS3LIIP0Ru2yfLU+QVIq990RwGBD/f/BqNZlgluHVJcj2Injx99vzF1svhq9dv3m7v7L47s7o2gDPQQptzRi0KrnDmuBN4Xhmkkgmcs9Vxm5//RmO5Vj/dusJc0gvFSw7UBTS3S3+y/NUsd0bJONlE/FCkvRiRPqbL3cE0KzTUEpUDQa1dpEnlck+N4yCwGWa1xYrCil7gIkhFJdrcb/pt4k+BFHGpTTjKxRv6/w1PpbVryYJTUndp7+da+FhuUbvyMPdcVbVDBd1DZS1ip+P283HBDYIT6yAoGB56jeGSGgoujGg4zAosM1n6rK3MyqYDzPqMaVG0HWnRQwmdC2ggd/sDCEOxwafwD2gpqSp8VjNqmkWaB6UKNJ0p1A3Uj9Im1Ag7SO9P/KE4m4zTr+PJj2+jo0m/jS3ynnwkX0hKvpMjckqmZEaArMgV+Uv+DW6i/egg+tBZo0F/Z4/ciejzLaFdvfU=</latexit>
 s mid

<latexit sha1_base64="LUV39H4AE+4AopqecTBnzoRYUxc=">AAACcnicbVHLahwxENSOncTZPPy6xZdxlkAOYZlZB5KjIZcc15C1DathkXp6bGE9BkljexHzG746v5X/yAdEszuH+NEgKKqrW0U1r6VwPsv+DJKNzRcvX229Hr55++799s7u3qkzjQWcgZHGnnPmUAqNMy+8xPPaIlNc4hm/+tH1z67ROmH0L7+ssVDsQotKAPORom5BPd76oETZLnZG2ThbVfoU5D0Ykb6mi93BlJYGGoXag2TOzfOs9kVg1guQ2A5p47BmcMUucB6hZgpdEVam2/RTZMq0MjY+7dMV+/9EYMq5peJRqZi/dI97Hflcb9746nsRhK4bjxrWH1WNTL1JuwTSUlgEL5cRMLAiek3hklkGPuY0HNISK6qqQLvNvGrXBHeBciPLzpGRPalgrQIWmYf+AGIoLuo03oBRiuky0IYz287zIiJdol2L4t7IhlHexh3xBvnjxJ+C08k4PxpPTr6Ojif9NbbIAflIPpOcfCPH5CeZkhkBUpM7ck9+D/4mH5LDpD9dMuhn9smDSr78AxM2wHU=</latexit>
 sD i

<latexit sha1_base64="PcJMuoqBqtoWl152IbP6BLtEXtQ=">AAACbXicbZHNatwwEMe1btqmm34kLT0lBNOltKfF3gaSYyA99LiFbjawNos0Hidi9WEkuWERfohemyfLU+QVKq99aD4GBH9+89doNMMqwa1LkttB9Gzr+YuX26+GO6/fvH23u/f+3OraAM5AC20uGLUouMKZ407gRWWQSiZwzlZnbX7+G43lWv1y6wpzSS8VLzlQF9DcLv33JW+Wu6NknGwifizSXoxIH9Pl3mCaFRpqicqBoNYu0qRyuafGcRDYDLPaYkVhRS9xEaSiEm3uN/028edAirjUJhzl4g39/4an0tq1ZMEpqbuyD3MtfCq3qF15knuuqtqhgu6hshax03H7+bjgBsGJdRAUDA+9xnBFDQUXRjQcZgWWmSx91lZmZdMBZn3GtCjajrTooYTOBTSQ+/0BhKHY4FN4DVpKqgqf1YyaZpHmQakCTWcKdQP1o7QJNcIO0ocTfyzOJ+P023jy82h0Oum3sU32ySfylaTkmJySH2RKZgTIivwhf8nN4C76GB1Eh501GvR3PpB7EX35B59ZvfQ=</latexit>
s D j

<latexit sha1_base64="+ThZJtGTqC4BOQipD+1AWclGq2A=">AAACbXicbZHbatwwEIa17indHpI05KqhmC6lvVrsbaG5DCQXudxCNxtYm0UajxN1dTCS3LIIP0Ru2yfLU+QVIq990RwGBD/f/BqNZlgluHVJcj2Injx99vzF1svhq9dv3m7v7L47s7o2gDPQQptzRi0KrnDmuBN4Xhmkkgmcs9Vxm5//RmO5Vj/dusJc0gvFSw7UBTS3S3+y/NUsd0bJONlE/FCkvRiRPqbL3cE0KzTUEpUDQa1dpEnlck+N4yCwGWa1xYrCil7gIkhFJdrcb/pt4k+BFHGpTTjKxRv6/w1PpbVryYJTUndp7+da+FhuUbvyMPdcVbVDBd1DZS1ip+P283HBDYIT6yAoGB56jeGSGgoujGg4zAosM1n6rK3MyqYDzPqMaVG0HWnRQwmdC2ggd/sDCEOxwafwD2gpqSp8VjNqmkWaB6UKNJ0p1A3Uj9Im1Ag7SO9P/KE4m4zTr+PJj2+jo0m/jS3ynnwkX0hKvpMjckqmZEaArMgV+Uv+DW6i/egg+tBZo0F/Z4/ciejzLaFdvfU=</latexit>
 s mid

<latexit sha1_base64="LUV39H4AE+4AopqecTBnzoRYUxc=">AAACcnicbVHLahwxENSOncTZPPy6xZdxlkAOYZlZB5KjIZcc15C1DathkXp6bGE9BkljexHzG746v5X/yAdEszuH+NEgKKqrW0U1r6VwPsv+DJKNzRcvX229Hr55++799s7u3qkzjQWcgZHGnnPmUAqNMy+8xPPaIlNc4hm/+tH1z67ROmH0L7+ssVDsQotKAPORom5BPd76oETZLnZG2ThbVfoU5D0Ykb6mi93BlJYGGoXag2TOzfOs9kVg1guQ2A5p47BmcMUucB6hZgpdEVam2/RTZMq0MjY+7dMV+/9EYMq5peJRqZi/dI97Hflcb9746nsRhK4bjxrWH1WNTL1JuwTSUlgEL5cRMLAiek3hklkGPuY0HNISK6qqQLvNvGrXBHeBciPLzpGRPalgrQIWmYf+AGIoLuo03oBRiuky0IYz287zIiJdol2L4t7IhlHexh3xBvnjxJ+C08k4PxpPTr6Ojif9NbbIAflIPpOcfCPH5CeZkhkBUpM7ck9+D/4mH5LDpD9dMuhn9smDSr78AxM2wHU=</latexit>

c = !2 sD i ⌦D j

<latexit sha1_base64="Q1/7zOAe2cKhMnpXB7uy4ErE5xs=">AAAD93icjVJNbxMxEHUbPsry0RSOXCyiSFwaZbeR4IJUCQ4ci0TaSuso8nq9yVLbu7K9bSLLv4AfwQ1x7bX8Ev4N42xUkRQkLO1q9s288Zu3k9WiNHY4/LWz27l3/8HDvUfR4ydPn+13D56fmqrRjI9ZJSp9nlHDRan42JZW8PNacyozwc+yi/chf3bJtSkr9dkuaz6RdKbKomTUAjTt9hl+h0mhKXNENd4lnlDNBFczO3cfpqWH1xc/7faGg+Hq4LtBvA56aH1Opge7NySvWCO5skxQY9J4WNuJo9qW0N1HpDG8puyCzngKoaKSm4lbzeNxH5AcF5WGR1m8Qv9kOCqNWcoMKiW1c7OdC+Dfcmlji7cTV6q6sVyx9qKiEdhWOJiD81JzZsUSAsp0CVoxm1Mwx4KFUURyXhBZOBI6Z4Vvgcw4klUiD4oqsQYla6sYBWRTH2NgioE6xa9YJSVVuSNNRrVP4wlEKue6LYK+gLpe7KFHH8N/XJp5pS3Vurra5G/mQqf0KBi+EqG5cP0IY0zmWbVwRDeCpyQvJV/UmgSPQ6yShFi+sOE7ORwktSVApItJEOAGo9p633aRF1yrw5Fs1v2Ci0ByY+/gXy+9k94pT1pD3AjkhwE251WlveTMpwlonFMYFXxdeD+Fy7aG6SV+yyyQdctd0f6LdbvXK6L5FyeKYNvj7d2+G5wmg/hokHwa9Y6T9d7voZfoFXqNYvQGHaOP6ASNEUNf0TW6QT87y863zvfOj7Z0d2fNeYE2Tuf6N8E+WKM=</latexit>

(a) (b)

Fig. 10. (a) Level set of Vij. (b) Geometric construction of
the zero level set of Vij.

regions (see Fig. 9b):

Ri = {xA | sL ∈ [sDismid)},
Rj = {xA | sR ∈ (smidsDj ]}, and (34)
Rmid = {xA | sL /∈ [sDismid), sR /∈ (smidsDj ]}.

If xA ∈ Ri(sDi, sDj ), the intruder can move towards sL
to play optimally against Di without considering Dj,
since sDj will not be active in Jij. Similarly when xA ∈
Rj(sDi, sDj ), the intruder can ignore Di and choose sR
to play optimally against Dj. However, when xA ∈ Rmid,
the intruder cannot simply choose one defender to play
against because the optimal behavior against Di makes
Dj to be the active defender and vice versa. A good
compromise in this case is to approach smid.

Now we have a candidate intrusion strategy:

u
∗
A = ν ˆxA )opt, (35)

where ˆxA )opt = γ(sopt)−xA
∥γ(sopt)−xA∥ , and the optimal breaching
point is deﬁned by

sopt(xA, sD1, sD2 ) =
 



 sL if xA ∈ Ri(sDi, sDj )

sR if xA ∈ Rj(sDi, sDj )

smid otherwise.
 (36)

The associated value (to be proved in Theorem 6) is
given as follows:

Vij =
 



 J ∗
L(sDi, xA) if xA ∈ Ri(sDi, sDj )

J ∗
R(sDj , xA) if xA ∈ Rj(sDi, sDj )

Jmid(sDi, sDj , xA) otherwise,
 (37)

where the regions are deﬁned in (34). Fig. 10a shows the
level sets of Vij(sDi , sDj , xA). Each level set is a combi-
nation of three curves: the two level sets from the one
vs. one games and a circle centered at smid. Speciﬁcally,

12

the zero level set {xA | Vij(sDi, sDj , xA) = 0} is a com-
bination of the two barriers, and a circle with radius

c = 1
2 νsDi )Dj , (38)

as shown in Fig. 10b.

4.2 Winning Regions

Analogous to the two-player game, we deﬁne the intruder
winning region to be the superlevel set of Vij as follows:

RC(sDi, sDj ) ≜ {xA | Vij(sDi, sDj , xA) > 0}. (39)

The subscript C is used to highlight the cooperative na-
ture of the associated defense strategy. The following
lemma gives a suﬃcient condition for intruder’s victory:

Lemma 4 If the initial conﬁguration satisﬁes xA(t0) ∈
RC(sDi(t0), sDj (t0)), then regardless of the defender’s
strategy, the intruder wins the game of kind using u
∗
A
deﬁned in (35).

PROOF. If the intruder starts in Ri ∩RC, then it wins
against Di by approaching sL since J ∗
L(sDi, xA) > 0.
In this case, although sL is suboptimal against Dj, the
intruder still wins because sL )Dj (t0) > sDi )L(t0): Dj is
farther from sL than Di. With the same argument, the
intruder wins if it starts in Rj ∩ RC. Finally, if xA ∈
Rmid∩RC, then the intruder can reach smid before either
of the defenders because Jmid > 0. ■

Observe that the intruder-winning region RC is smaller
than RI derived from the one vs. one game analysis.
The gap is generated by the cooperation between the
defenders.

Deﬁnition 4 The paired-defense region is deﬁned
by:

Rpair(sDi, sDj ) = RI (sDi, sDj ) − RC(sDi, sDj ). (40)

The cooperation arises in the form of “pincer move-
ment,” which is a tactic where the two defenders ap-
proach the intruder from both cw and ccw sides at the
same time. In our problem the corresponding control in-
put is [ωDi, ωDj ] = [1, −1]. By considering this defender
strategy, the next lemma shows that xA ∈ RC is also a
necessary condition for the intruder to win the game of
kind:

Lemma 5 If the initial conﬁguration satisﬁes xA ∈
Rpair(sDi, sDj ), and if the defender pair uses a pin-
cer movement, [ωDi, ωDj ] = [1, −1], then either
xA ∈ RD(sDi) or xA ∈ RD(sDj ) occurs before the in-
truder reaches the perimeter: i.e., the defender pair wins.

(a) (b)

smid

<latexit sha1_base64="yiGJlWEHqvceadyFLFqYbMfY5QM=">AAACYHicbVDLThsxFHWGPtLpAwK7djNqVKmraCYg0VWFxKZLkBpAikeR7bkDFn6M7DvQyJrfYAu/1W2/pJ4kiwK9kqWjc889Pjq8UdJjnv8eJFsvXr56PXyTvn33/sP2zmj3zNvWCZgJq6y74MyDkgZmKFHBReOAaa7gnF8f9/vzG3BeWvMTlw2Uml0aWUvBMFLULyjCLwxaVt1iZ5xP8tVkz0GxAWOymZPFaPCdVla0GgwKxbyfF3mDZWAOpVDQpbT10DBxzS5hHqFhGnwZVqG77Etkqqy2Lj6D2Yr99yIw7f1S86jUDK/8011P/m83b7H+VgZpmhbBiPVHdasytFnfQFZJBwLVMgImnIxZM3HFHBMYe0pTWkFNdR1o78zrbk1wHyi3quoTWdWlj9MIESvwUWrgVlitmakCbTlz3bwoIzIVuLUoukQ2jIsuesTGi6f9Pgdn00mxP5meHoyPppvuh+QT+Uy+koIckiPyg5yQGRGkIXfknjwM/iTDZDsZraXJYHOzRx5N8vEvTGG5Gg==</latexit> smid

<latexit sha1_base64="yiGJlWEHqvceadyFLFqYbMfY5QM=">AAACYHicbVDLThsxFHWGPtLpAwK7djNqVKmraCYg0VWFxKZLkBpAikeR7bkDFn6M7DvQyJrfYAu/1W2/pJ4kiwK9kqWjc889Pjq8UdJjnv8eJFsvXr56PXyTvn33/sP2zmj3zNvWCZgJq6y74MyDkgZmKFHBReOAaa7gnF8f9/vzG3BeWvMTlw2Uml0aWUvBMFLULyjCLwxaVt1iZ5xP8tVkz0GxAWOymZPFaPCdVla0GgwKxbyfF3mDZWAOpVDQpbT10DBxzS5hHqFhGnwZVqG77Etkqqy2Lj6D2Yr99yIw7f1S86jUDK/8011P/m83b7H+VgZpmhbBiPVHdasytFnfQFZJBwLVMgImnIxZM3HFHBMYe0pTWkFNdR1o78zrbk1wHyi3quoTWdWlj9MIESvwUWrgVlitmakCbTlz3bwoIzIVuLUoukQ2jIsuesTGi6f9Pgdn00mxP5meHoyPppvuh+QT+Uy+koIckiPyg5yQGRGkIXfknjwM/iTDZDsZraXJYHOzRx5N8vEvTGG5Gg==</latexit>
D i

<latexit sha1_base64="yMNgyq5uhHVvkqbBirUz5s/Q0mU=">AAACV3icbVDLSsNAFJ3EV42vVpdugkVwVZIq6EoEXbhUtCo0ocxMburgPMLMRCkhn+BWv82v0Unbha8LA4dzz733zCEFZ8ZG0YfnLywuLa+0VoO19Y3NrXZn+86oUlMYUMWVfiDYAGcSBpZZDg+FBiwIh3vydN70759BG6bkrZ0UkAo8lixnFFtH3VyM2KjdjXrRtMK/IJ6DLprX1ajjnSaZoqUAaSnHxgzjqLBphbVllEMdJKWBAtMnPIahgxILMGk19VqH+47Jwlxp96QNp+z3iQoLYyaCOKXA9tH87jXkf71hafOTtGKyKC1IOjuUlzy0Kmw+HmZMA7V84gCmmjmvIX3EGlPr4gmCJIM8EXmVNJtJXs8IYqqEKJ41jhSvg59uKHURGCeV8EKVEFhmVVISrOthnDokM9Azkdvi2Kob126HSzz+ne9fcNfvxYe9/vVR96w/z76FdtEeOkAxOkZn6BJdoQGiaIxe0Rt69z68T3/Zb82kvjef2UE/yu98AREKtaY=</latexit>D j

<latexit sha1_base64="PbgBVH/SChjLr5cmtcd2bg21614=">AAACV3icbVDLSsNAFJ3EV43P6tJNsAiuSlIFXYmgC5eKVoUmlJnJTR2dR5iZKCXkE9zqt/k1Omm78HVh4HDuufeeOaTgzNgo+vD8ufmFxaXWcrCyura+sdneujWq1BT6VHGl7wk2wJmEvmWWw32hAQvC4Y48nTX9u2fQhil5Y8cFpAKPJMsZxdZR1+fDx+FmJ+pGkwr/gngGOmhWl8O2d5JkipYCpKUcGzOIo8KmFdaWUQ51kJQGCkyf8AgGDkoswKTVxGsd7jkmC3Ol3ZM2nLDfJyosjBkL4pQC2wfzu9eQ//UGpc2P04rJorQg6fRQXvLQqrD5eJgxDdTysQOYaua8hvQBa0ytiycIkgzyRORV0mwmeT0liKkSonjWOFK8Dn66odRFYJxUwgtVQmCZVUlJsK4HceqQzEBPRW6LY6tOXLsdLvH4d75/wW2vGx90e1eHndPeLPsW2kG7aB/F6Aidogt0ifqIohF6RW/o3fvwPv1FvzWV+t5sZhv9KL/9BRL7tac=</latexit>
 R pair

<latexit sha1_base64="6LwTjItBv3fg+4Jde8zHJxNmehg=">AAACenicbVFNa9tAEF2rX6n75aTHXkRMoaVgJCfQHgO99OiWOgl4hRmNRsmS/RC7qzZm0V/ptf1L/S89dGXr0CQdWHi8eTP7eFM2UjifZb9Hyb37Dx4+2ns8fvL02fMXk/2DU2dai7REI409L8GRFJqWXnhJ540lUKWks/LqY98/+0bWCaO/+k1DhYILLWqB4CO1nhxwheFLt+aern1oQNhuPZlms2xb6V2QD2DKhlqs90cLXhlsFWmPEpxb5VnjiwDWC5TUjXnrqAG8ggtaRahBkSvC1nyXvo5MldbGxqd9umX/nQignNuoMioV+Et3u9eT/+utWl9/KILQTetJ4+6jupWpN2mfRFoJS+jlJgJAK6LXFC/BAvqY13jMK6q5qgPvN5d1tyNKF3hpZNU7MnIgY4RbFUJkbvpDjKG4qNP0HY1SoKvA2xJst8qLiHRFdieKeyMbpnkXd8Qb5LcTvwtO57P8aDb/fDw9mQ/X2GOv2CF7w3L2np2wT2zBlgzZNfvBfrJfoz/JYfI2ebeTJqNh5iW7UcnxX5CDw1c=</latexit>
 R C

<latexit sha1_base64="x+OrE7sFBFOYIz+gCkhR+nwexXI=">AAACd3icbVHLbtswEKTVRxI3bZzm2EOFGg1yMiS3QHsMkEuPTlAnAUzBIFerhAgfAkk1NQh9Sa/tR/VTegtl65BHFyAwmJ1dDmZ5LYXzWfZ3kDx7/uLl1vbO8NXu6zd7o/235840FnAORhp7yZlDKTTOvfASL2uLTHGJF/zmpOtf/EDrhNHf/arGQrErLSoBzEdqOdqjCsJZu6Qef/pw0i5H42ySrSt9CvIejElfs+X+YEZLA41C7UEy5xZ5VvsiMOsFSGyHtHFYM7hhV7iIUDOFrghr5236MTJlWhkbn/bpmr0/EZhybqV4VCrmr93jXkf+r7dofPW1CELXjUcNm4+qRqbepF0MaSksgperCBhYEb2mcM0sAx/DGg5piRVVVaDdZl61G4K7QLmRZefIyJ6M+a1VwCLz0B9ADMVFncZbMEoxXQbacGbbRV5EpEu0G1HcG9kwztu4I94gf5z4U3A+neSfJtPTz+PjaX+NbfKOfCBHJCdfyDH5RmZkToA05Bf5Tf4M/iXvk8PkaCNNBv3MAXlQSX4HNQTB0A==</latexit>

x A

<latexit sha1_base64="IpvmRP4uopQgWGE/lBrOcRl9Mho=">AAACbXicbVHLbtQwFPWEQssU6AOxoqosRghWo2SK1C6L2HQ5SEyn0iQa2Tc3rTV+RLYDjKJ8RLfwZXwFv1BnkgVtuZKlo3OPr4/P5aUUzsfxn0H0ZOvps+2d58PdFy9f7e0fHF46U1nAGRhp7BVnDqXQOPPCS7wqLTLFJc756kvbn39H64TR3/y6xEyxay0KAcwHap6qgv5cfl7uj+JxvCn6GCQ9GJG+psuDwTTNDVQKtQfJnFskcemzmlkvQGIzTCuHJYMVu8ZFgJopdFm98dvQ94HJaWFsONrTDfvvjZop59aKB6Vi/sY97LXk/3qLyhdnWS10WXnU0D1UVJJ6Q9vP01xYBC/XATCwInilcMMsAx8iGg7THIuQSJ22k3nRdAR3dcqNzFtHRvakgk4FLDD3/QGEUFzQafwBRimm8zqtOLPNIskC0jnaThTmBrYeJU2YEXaQPEz8MbicjJOT8eTrp9H5pN/GDnlL3pGPJCGn5JxckCmZESArckt+kd+Dv9Gb6Cg67qTRoL/zmtyr6MMdvyG9hQ==</latexit>
 D i

<latexit sha1_base64="yMNgyq5uhHVvkqbBirUz5s/Q0mU=">AAACV3icbVDLSsNAFJ3EV42vVpdugkVwVZIq6EoEXbhUtCo0ocxMburgPMLMRCkhn+BWv82v0Unbha8LA4dzz733zCEFZ8ZG0YfnLywuLa+0VoO19Y3NrXZn+86oUlMYUMWVfiDYAGcSBpZZDg+FBiwIh3vydN70759BG6bkrZ0UkAo8lixnFFtH3VyM2KjdjXrRtMK/IJ6DLprX1ajjnSaZoqUAaSnHxgzjqLBphbVllEMdJKWBAtMnPIahgxILMGk19VqH+47Jwlxp96QNp+z3iQoLYyaCOKXA9tH87jXkf71hafOTtGKyKC1IOjuUlzy0Kmw+HmZMA7V84gCmmjmvIX3EGlPr4gmCJIM8EXmVNJtJXs8IYqqEKJ41jhSvg59uKHURGCeV8EKVEFhmVVISrOthnDokM9Azkdvi2Kob126HSzz+ne9fcNfvxYe9/vVR96w/z76FdtEeOkAxOkZn6BJdoQGiaIxe0Rt69z68T3/Zb82kvjef2UE/yu98AREKtaY=</latexit>
D j

<latexit sha1_base64="PbgBVH/SChjLr5cmtcd2bg21614=">AAACV3icbVDLSsNAFJ3EV43P6tJNsAiuSlIFXYmgC5eKVoUmlJnJTR2dR5iZKCXkE9zqt/k1Omm78HVh4HDuufeeOaTgzNgo+vD8ufmFxaXWcrCyura+sdneujWq1BT6VHGl7wk2wJmEvmWWw32hAQvC4Y48nTX9u2fQhil5Y8cFpAKPJMsZxdZR1+fDx+FmJ+pGkwr/gngGOmhWl8O2d5JkipYCpKUcGzOIo8KmFdaWUQ51kJQGCkyf8AgGDkoswKTVxGsd7jkmC3Ol3ZM2nLDfJyosjBkL4pQC2wfzu9eQ//UGpc2P04rJorQg6fRQXvLQqrD5eJgxDdTysQOYaua8hvQBa0ytiycIkgzyRORV0mwmeT0liKkSonjWOFK8Dn66odRFYJxUwgtVQmCZVUlJsK4HceqQzEBPRW6LY6tOXLsdLvH4d75/wW2vGx90e1eHndPeLPsW2kG7aB/F6Aidogt0ifqIohF6RW/o3fvwPv1FvzWV+t5sZhv9KL/9BRL7tac=</latexit>

R I

<latexit sha1_base64="HgZNozuxle54FjSBJH978d1SuQM=">AAACbXicbZHPbtQwEMa9gdKyFNpScQIhi1VVTqtki0SPlXqB24LYbqVNtLInk9Za/4lsB7SK8hC9wpP1KXiFOpscaMtIlj795vN4PMNLKZyP49tB9OTp1rPtnefDF7svX+3tH7y+cKaygDMw0thLzhxKoXHmhZd4WVpkikuc89V5m5//ROuE0T/8usRMsSstCgHMBzRPFdDvy6/L/VE8jjdBH4ukFyPSx3R5MJimuYFKofYgmXOLJC59VjPrBUhshmnlsGSwYle4CFIzhS6rN/029CiQnBbGhqM93dB/b9RMObdWPDgV89fuYa6F/8stKl+cZrXQZeVRQ/dQUUnqDW0/T3NhEbxcB8HAitArhWtmGfgwouEwzbFIVVGnbWVeNB3grk65kXnbkZE9VNC5gAVyvz+AMBQXfBp/gVGK6bxOK85ss0iyoHSOtjOFuoHWo6QJNcIOkocTfywuJuPkZDz59ml0Num3sUPekg/kI0nIZ3JGvpApmREgK3JDfpM/g7/Rm+hd9L6zRoP+ziG5F9HxHXxmvWQ=</latexit>
 Fig. 11. Paired-defense region. (a) Intruder starts in Rpair.
Neither Di nor Dj has a guarantee to win from the one vs. one
game analysis because xA ∈ RI . (b) Pincer maneuver by the
defender pair pushes the intruder out from Rpair, while also
preventing it to enter RC . At this time, Dj can guarantee
its victory using one vs. one strategy since xA ∈ RD(i).

PROOF. Observe that Rpair shrinks as the two defend-
ers get closer, and it disappears when the two meet at
the midpoint. Hence, the intruder will exit Rpair in ﬁ-
nite time. There are only three ways to exit Rpair: enter
RD(sDi), enter RD(sDj ), or enter RC(sDi, sDj ). How-
ever, the intruder cannot enter RC because its speed ν
cannot exceed the rate at which the radius of the circle
decreases: ˙c = 1
2 ν d
dt sDi )Dj = 1
2 ν(−1 − 1) = −ν. There-
fore, xA enters either RD(sDi) or RD(sDj ). ■

Recalling that xA ∈ RD(sDi) ∪ RD(sDj ) trivially leads
to capture based on the solution to the one vs. one game,
the only region that the intruder can guarantee its vic-
tory is RC(sDi, sDj ).

Theorem 5 The zero level set of Vij deﬁned in (37)
gives the barrier of the game of kind played between two
defenders and one intruder.

The result directly follows from Lemmas 2, 5 and 4.

Remark 7 The two vs. one scenarios have also been
studied in related but diﬀerent problems. Cooperative
capture in pursuit-evasion games have been studied in
[29,13,18]. There are also works that consider two vs.
one cooperation in border-defense type scenarios [16,48].

4.3 Optimality of the Strategies

Consider the intruder winning conﬁguration. The payoﬀ
function in (21) can be modiﬁed to

P1(ωDi, ωDj , uA) = min{sDi )B(tF ), sB )Dj (tF )}, (41)

which describes the safe distance at the time of breach-
ing.

13

Theorem 6 If the initial conﬁguration is xA ∈
RC(sDi, sDj ), and if the players use P1 in (41) as the
objective function, then u
∗
A in (35), (36) and the pincer
maneuver [ωDi, ωDj ] = [1, −1] form equilibrium strate-
gies, and the value of the game is Vij in (37).

PROOF. Similar to the proof of Theorem 2, we can
see that P1 = Vij along the terminal surface. Therefore,
the increase (resp. reduction) in P1 is equivalent to the
increase (resp. reduction) in Vij(tF ). To prove the opti-
mality, we will show that

˙Vij(ω∗
D, uA) ≤ ˙Vij(ω∗
D, u
∗
A) = 0 ≤ ˙Vij(ωD, u
∗
A), (42)

where ωD = [ωDi, ωDj ], and ω∗
D = [1, −1]. The above
inequality indicates that any unilateral change in the
strategy will result in a suboptimal performance.

Recall that Vij = J ∗
L when xA ∈ Ri. In this case, the
inequality is shown using the time derivative ˙J ∗
L in the
proof of Theorem 2. The case with xA ∈ Rj is simi-
larly straightforward. However, the case xA ∈ Rmid has
not been considered yet. For example, can the defend-
ers move in the same direction ω∗
D = [1, 1] to move smid
away from the intruder? We will investigate this using
the time derivative ˙Vij = ˙Jmid:

˙Jmid = 1
2 (ωDj − ωDi) − ˆxA )mid
ν · ( ˙smidT (smid) − uA)

= 1
2 ((1 − β)ωDj − (1 + β)ωDi) + 1
ν ˆxA )mid · uA,

where we used ˙smid = 1
2 (ωDj + ωDi) and deﬁned

β ≜ ˆxA )mid · T (smid)
ν = cos φ(smid)
ν .

From the conditions on sL and sR (see (34)), the ap-
proach angle at smid satisﬁes φ∗
L ≤ φ(smid) ≤ φ∗
R when
xA ∈ Rmid. Hence, we have | cos φ(smid)| < ν, or equiv-
alently, |β| < 1 when xA ∈ Rmid. Therefore, both 1 − β
and 1 + β are positive, and we have

[1, −1] = arg min
ωD max
uA ˙J ∗
mid(ωD, uA),

ν ˆxA )mid = arg max
uA min
ωD ˙J ∗
mid(ωD, uA),

and minωD maxuA ˙J ∗
L(ωD, uA) = 0, which completes
the proof. ■

For the defender winning conﬁguration, we use the same
payoﬀ P2 in (24), with a modiﬁcation on dbar as follows:

dbar = min
x∈RC ∥x − xA∥. (43)
 Theorem 7 If the initial conﬁguration is xA /∈
RC(sDi, sDj ), and if the players use P2 in (24) as the
objective function, then u
∗
A in (35) and the pincer ma-
neuver [ωDi, ωDj ] = [1, −1] form equilibrium strategies,
and the value of the game is Vij in (37).

PROOF. Similar to the proof of Theorem 3, it suﬃces
to show that −dbar = νVij, since we already have the
result (42). The identity for the case with xA ∈ Ri or
xA ∈ Rj is already proved in Theorem 3. When xA ∈
Rmid, it is easy to get the result B · xA )mid = 0 recalling
that the barrier ∂RC in this portion is a circle whose
center is at smid. ■

The optimal behavior of the defender at sDi against an
intruder at xA may be diﬀerent based on the existence
of the third player sDj . In a one vs. one game Di must
decide between cw and ccw motion based on the location
of xA with respect to the dispersal surface Γdis(sDi),
and it is possible that the cw motion is optimal. On the
other hand, in a two vs. one game Di (deﬁned as the one
on cw side) should always move ccw.

As was done for the one vs. one game, we provide al-
gorithms to obtain key quantities necessary to compute
the strategies. First, recall that a defender pair divides
the game space into two parts (Fig. 9a). Given a pair of
defenders sD1 and sD2, we must ﬁrst determine which
acts as the cw-side defender (Di) and which acts as the
ccw-side defender (Dj).

Algorithm 5 Relevant region (2 vs. 1)
1: Input: sD1, sD2, xA, γ, and ν
2: Compute is in left1 with sD1 using Alg. 2
3: Compute is in left2 with sD2 using Alg. 2
4: if sD1 )D2 < L
2 then
5: is in D1D2 ← is in left1 and ∼is in left2
6: else
7: is in D1D2 ← is in left1 or ∼is in left2
8: end if
9: Return: is in D1D2
Note: ∼ is a negation operator

If is in D1D2= T rue, then the defender at sD1 takes
the role of Di as described in this section, but it will act
as Dj otherwise.

The defender strategy is presented in Alg. 7. If one de-
fender can guarantee capture, then the behavior of the
other defender is inconsequential. Therefore, we assign
no action to that defender in this paper. If a single de-
fender cannot guarantee capture, i.e., xA /∈ RD(sDi) ∪
RD(sDj ), then the defenders perform pincer movement.

Finally, note that the attacker’s current region identiﬁed
with (34), together with the quantities sL, sR and smid
are suﬃcient to ﬁnd Vij in (37)

14

Algorithm 6 Intruder Control (2 vs. 1)
1: Input: sD1, sD2, xA, γ, and ν
2: Compute sL and sR using Alg. 2
3: Compute is in D1D2 using Alg. 5
4: if is in D1D2 = T rue then
5: sDi ← sD1 and sDj ← sD2
6: else
7: sDi ← sD2 and sDj ← sD1
8: end if
9: Determine the region using (34)
10: if xA ∈ Ri then
11: u
∗
A = ν ˆxA )L
12: else if xA ∈ Rj then
13: u
∗
A = ν ˆxA )R
14: else
15: u
∗
A = ν ˆxA )mid
16: end if
17: Return: u∗
A

Algorithm 7 Defender Control (2 vs. 1)
1: Input: sD1, sD2, xA, γ, and ν
2: if xA ∈ RD(sD1) then
3: ωD1 ← strategy from Alg. 4
4: ωD2 ← 0
5: else if xA ∈ RD(sD2) then
6: ωD1 ← 0
7: ωD2 ← strategy from Alg. 4
8: else
9: Compute sL and sR using Alg. 2
10: Compute is in D1D2 using Alg. 5
11: if is in D1D2 = T rue then
12: [ωD1 , ωD2 ] ← [1, −1]
13: else
14: [ωD1 , ωD2 ] ← [−1, 1]
15: end if
16: end if
17: Return: [ωD1 , ωD2 ]

Remark 8 (Computation) Importantly, the calcula-
tion of the optimal strategies and the value (for both one
vs. one and two vs. one) do not require any explicit com-
putation of the surfaces nor the regions. A numerical
search is performed only in the ﬁrst step when ﬁnding the
breaching points, which is also simple due to the mono-
tonicity of the approach angle φ(s). Also note that nu-
merical methods proposed in [6,7] requires us to solve the
HJI PDE oﬄine and store the solution (i.e., control in-
puts corresponding to all possible states), so the players
can use this ‘lookup table’ in the run time. Our method
requires less memory because control inputs are computed
online.

5 Multiplayer Game

This section discusses assignment-based defense policies
when there are multiple players on both teams. These
multi-agent policies rely on the barriers or the winning
regions derived in the previous sections.

We ﬁrst review the assignment method (MM defense)
 proposed by Chen et al. [6,5] that only considers one
vs. one defense. We then propose an extension (MIS de-
fense) that directly incorporates cooperative two vs. one
defense, which was ﬁrst introduced in the conference ver-
sion of this paper [39]. We also brieﬂy introduce a co-
operative defense strategy (LGR defense) that has the
strongest theoretical guarantees, which is presented in
our separate publication [41]. Finally, we provide a dis-
cussion on the strengths and weaknesses of each policy.

The bounds QM M , QM IS and QLG that will be intro-
duced in this section provide solution to Prob. 2 posed
in Sec. 2.

5.1 Maximum Matching (MM) defense

For a given initial conﬁguration {xAi}
NA
i=1 and {sDj }ND
j=1,
the defender-winning regions can be used to determine
a set of intruders that each defender can win against: Dj
can be assigned to Ai if xAi /∈ RA(sDj ), or equivalently,
xA ∈ RD(sDj ). Again, the defender wins by either cap-
turing the intruder or delaying its intrusion indeﬁnitely
(see Sec. 3.2).

One can generate a bipartite graph with intruders and
defenders as two sets of nodes. Edges will be drawn from
each defender to all the intruders that it can capture.
Matching in graph theory refers to ﬁnding a set of edges
with no shared nodes. Here, this restriction corresponds
to the assumption that Dj can only play an optimal
two-player game against at most one intruder at a time.
Maximum-cardinality matching (MM) algorithms (see
references in [6]) give such an edge set with maximum
cardinality.

The edge set is used to assign at most one unique de-
fender to each intruder. If Dj is assigned to Ai, then Dj
selects its strategy to be optimal against Ai. The cardi-
nality of the edge set, N cap
MM, tells us that at least N cap
MM
intruders will be captured. The upper bound on the in-
truder score is then given by

Q ≤ QMM = NA − N cap
MM. (44)

This method assumes that all defenders play indepen-
dent games and ignores any cooperation with the team-
mates.

5.2 Maximum Independent Set (MIS) defense

Now we allow a defender pair to be assigned to a single
intruder. Let D(i,j) denote a pair (Di, Dj). The match-
ing algorithm needs to be modiﬁed to avoid conﬂicts. For
example, Di and a pair D(i,j) cannot be treated as in-
dependent nodes and be assigned to distinct intruders,
because Di may not be able to move optimally against
two intruders simultaneously. We pose the assignment

15

D1
 A1
A4
A3
A2
D2
D3

D3,5
D4,5
 1
 2
 3

45 6
7
 8
 9
 1 2 3
45
 67

8
9
 D1
 A1
A4
A3
A2D2
D3

D3,5
D4,5
 1
3
6
9

(b) (c) (d)

A1
 A2 A3
 A4

D1
D2
D3
 D4 D5
 A1
 A2 A3
A4

D1
D2D3
 D4 D5

possible assignment
MIS assignment

(a) (e)

Fig. 12. (a) Example with 5 defenders and 4 intruders. (b)
Each node on the left represents a defender or a pair of de-
fenders, and nodes on the right represent intruders. Edges are
drawn when the defender or defender pair can win against
the intruder. (c) Edges in (b) become nodes in the new graph.
A maximum independent set is highlighted in red. (d) An as-
signment (not necessarily unique) that defends against max-
imum number of intruders. (e) Assignment described in the
original game space.

problem into a maximum independent set (MIS) prob-
lem [25] as described in the following:

1) Construct a bipartite graph with two sets of nodes
VD = {Di}
ND
i=1 ∪ {D(i,j)}i̸=j and VA = {Ai}
NA
i=1. The
node set VD now includes all possible defender pairs.
2) For each Di, draw edges to all intruders, Ak, such that
xAk ∈ RD(sDi).
3) For each pair D(i,j), draw edges to all Ak such that
xAk ∈ Rpair(sDi, sDj ) (see Fig. 11). Note that we ex-
clude the intruders that are independently capturable
by either Di or Dj.

Figure 12a depicts a particular initial condition, and
Fig. 12b shows the bipartite graph (nodes with no edges
are omitted).

4) The edges in the graph are enumerated and be-
come the nodes in the new graph representation (see
Fig. 12c).
5) Draw an edge between two nodes (in the new graph)
whenever they share the same defender or intruder.
6) Find MIS, i.e., the largest subset of nodes with no
direct connection.

Figures 12d-e illustrate the resultant assignments that
give N cap
MIS = 4 and Q ≤ QMIS = NA − N cap
MIS = 0. Note
 that the maximum-matching assignment only guaran-
tees Q ≤ QMM = 1 in this example.

Since the MIS formulation considers paired defense in
addition to all the individual defenses, it gives equal or
tighter upper bound for any initial conﬁguration: i.e.,

Q ≤ QM IS ≤ QM M . (45)

The above result is also straightforward noting that bi-
partite matching problem can be encoded as a special
case of the independent set problem [25].

The downside of the above formulation is the fact that
MIS cannot be found eﬃciently [25]. While approxima-
tion methods to solve MIS exist (e.g., [46]), they poten-
tially make the inequality (45) to no longer hold, which
takes away the whole purpose of using the MIS strategy.
A computationally eﬃcient team policy that preserves
the eﬀectiveness of the cooperative defense is presented
next.

5.3 Local Game Region (LGR) defense

We ﬁnally present an approach that gives us the
strongest theoretical guarantees. The full detail of this
policy is presented in our separate publication [41], and
therefore we only provide a high-level idea here.

The core concept we use for this strategy is called the
Local Game Region (LGR), which is deﬁned by the in-
truder winning region in the two vs. one game, with an
addition of a degenerate case where the two defenders
are identical. There are ND C2 ×2 = ND(ND −1) ordered
pairs and ND degenerate cases resulting in N 2
D regions
in total. We use k ∈ 1, ..., N 2
D to denote the indices of
the regions.

For each LGR, We can deﬁne an intruder and a defender
subteams by collecting all intruders and defenders in the
region. Let nk
A and n
k
D denote the number of agents in the
kth intruder and defender subteams. Then we can deﬁne
the numerical advantage held by the intruder subteam
as follows: qk = max{nk
A − nk
D, 0}. (46)

We call this number the local game score. The signiﬁ-
cance of this quantity is that we can prove that the in-
truder subteam can guarantee to score at least qk points
by approaching near the mid point between the defender
pair that deﬁnes this kth LGR [41].

Now considering the overall game, the intruders can
maximize their score by selecting the optimal decompo-
sition into subteams, i.e., a selection of a set of LGRs.
We show in [41] that this team selection can be cast as

16

the following optimization problem:

QLG = max
G
 ∑

k∈G qk, (47)

where G denotes a set of disjoint LGRs, that does not
share any area.

Conveniently, the optimal disjoint set G
∗ and the value
QLG can be obtained in O(N 4
D) time by recognizing (47)
as an instance of the maximum weight independent set
problem on a circular arc graph [39]. For applications
where it is critical to avoid any intrusion, it is easy to
test whether the intruders can guarantee a score of at
least one: QLG > 0 ⇔ ∃ qk > 0.

By dividing the agents into subteams according to G
∗,
and by each subteam playing the two vs. one game
against the corresponding defender pair, the intruder
team guarantees the following (see Theorem 1 in [41]):

Q ≥ QLG. (48)

Note that such team strategy for the intruder and the
score lower bound are not given by either MM or MIS
analyses. Note also that this score lower bound is inde-
pendent of the defender strategy.

For the defender team strategy we also use the “inde-
pendent” intruder winning region, RI , deﬁned in (30).
We deﬁne an extended version of the local game score:

ˆqk = qk + ˆnk
A, (49)

where ˆnk
A denotes the number of intruders in the corre-
sponding paired-defense region Rpair.

The LGR defense policy developed in [41] takes the fol-
lowing steps:

1) Remove/ignore QLG uncapturable intruders from the
game, so that the defenders can play a virtual game
with QLG = 0 (i.e., qk = 0, ∀ k). Identiﬁcation of these
intruders is presented as Alg. 2 in [41].
2) For each region with ˆqk ≥ 1, assign corresponding
defender pair to one of the intruders in Rpair. A greedy
algorithm for this two vs. one assignments is presented
as Alg. 3 in [41].
3) Perform Maximum Matching to assign one vs. one de-
fense for the remaining intruders and defenders (Alg. 4
in [41]).

We show in [41] that the above procedure has polynomial
time complexity. In addition, we show that if ˆqk ≤ 1, ∀k
after the removal of uncapturable intruders in the ﬁrst
step, then the LGR defense policy guarantees the fol-
lowing (Theorem 3 in [41]):

Q ≤ QLG. (50)
 Together with the previous lower bound provided by the
intruder team, this result proves the optimality of this
defense policy in a sense that it constitutes a saddle-
point equilibrium.

As long as the intruder team sticks to their equilibrium
strategy, the defender team cannot reduce the score by
deviating from LGR defense policy. This optimality in-
directly proves the following result:

Q ≤ QLG ≤ QM IS ≤ QM M . (51)

We can in fact construct a case where QLG < QM IS as
discussed in the simulation section.

5.4 Discussions

We discuss the strengths and weaknesses of the three
approaches introduced in this section: MM, MIS, and
LGR defense policies.

The MM assignment has the best computational eﬃ-
ciency, and it is also the simplest approach to use. 11
The only necessary information from the agent-level
game is the pair-wise win/loss information for all
defender-intruder pairs. This simplicity allows us to
use the MM assignment even when the defenders have
diﬀerent speed limits or even diﬀerent dynamics, since
the analysis comes down to the individual performance.
Therefore the MM approach is also the most extensible
one as well. All of the above strengths come at the cost
of suboptimal defender behavior, due to the absence of
cooperative two vs. one defense.

The MIS assignment improves the score bound at the
cost of computational complexity. It is still simple to set
up and extensible since we are only augmenting the one
vs. one results with additional two vs. one results and
posing it as an existing combinatorial optimization prob-
lem. Again, the biggest drawback is the computational
complexity, which makes this approach suitable only for
small problems.

The LGR approach has two main strengths. First, the
LGR defense policy gives the tightest score bound, as de-
scribed in (51), and it actually constitutes a Nash equi-
librium [41]. The second strength of the LGR analysis is
that it also provides a lower bound on the score: QLG.
This is in contrast to MM or MIS approaches that only
provide score upper bounds. The intruder team strat-
egy as well as the score lower bound given by the LGR
analysis are useful tools in assessing the performance of
defense systems.

11 Note that we solely account for the multi-agent assignment
aspect and not the individual winning regions here.

17

Even with these strengths, the LGR algorithm is
tractable in a sense that the complexity grows polyno-
mially with the number of agents. The numerical com-
parison of the score bounds QM M and QLG is presented
in [41]. Also, the time complexity of all three approaches
are provided in the Appendix of [41]. The down side of
the LGR approach lies in a relatively sophisticated for-
mulation related to the subteam deﬁnitions. In addition,
the current theory only accommodates defender teams
with homogeneous speed limits, and the extension to
higher-order dynamics will be non-trivial.

In summary, the MM defense strategy should be con-
sidered when simplicity and extensibility are important.
The LGR defense strategy should be used when optimal-
ity is important. Finally, if the intruder team strategy
and/or score lower bound are useful, the LGR analysis
provides these information.

6 Simulation Examples

This section demonstrates the theoretical results
through numerical examples. All the examples use
the perimeter shape parameterized as follows: [x, y] =
[a cos θ, b sin θ], where [a, b] = [5, 2], [2, 2], [2, 3] and [5, 3]
for the polar angles θ ∈ [0, π
2 ], θ ∈ [ π
2 , π], θ ∈ [π, 3π
2 ],
and θ ∈ [ 3π
2 , 2π]. Note however that such parameteriza-
tion is not necessary to apply the results of this paper.
The perimeter curve maybe given as a series of sample
points, or as a set of vertices of a polygon. The number
of those data points linearly aﬀect the overall compu-
tational complexity through the search for the breach
point.

6.1 One vs. One Game

We verify the results in Sec. 3 by testing both opti-
mal and suboptimal intrusion strategies. We select the
speed ratio to be ν = 0.8 and start the game in the
intruder-winning conﬁguration. Fig. 13a shows the sim-
ulation snapshots when the intruder takes the optimal
strategy, whereas Fig. 13b and c show the cases when the
intruder behaves suboptimally. The computation time
of the strategies was 0.2 ms for an implementation in
Matlab running on a laptop with a Core i7-7820HQ pro-
cessor with 16 GB of memory.

By inspecting the right most column, we can compare
the performance in terms of two metrics. First, the dis-
tance between the defender and the intruder at this time
is the safe distance considered in Sec. 3.3. We can see
that the intruder achieves the largest safe distance with
the optimal strategy in Fig. 13a.

Next, notice the diﬀerence in the time the intruder
reaches the perimeter. By sacriﬁcing the safe distance,
the closest-point strategy in Fig. 13b shows an improved

t = 1 t = 200 t = 434

t = 1 t = 200 t = 385

t = 1 t = 200 t = 634

(a) optimal breaching point

(b) closest point

(c) tangent point

Fig. 13. Simulation snapshots of one vs. one game with
ν = 0.8. (a) Intruder behavior using the correct speed ratio.
(b) Intruder behavior using ν = 0.01. (c) Intruder behavior
using ν = 1.

performance in terms of the arrival time. This strategy
also has the property of being open-loop type, since the
closest point on the perimeter is completely independent
of the defender’s position or its behavior. However, note
that this strategy does not always guarantee intruder’s
win even if the game starts in the intruder winning con-
ﬁguration. Speciﬁcally, when the intruder starts on the
barrier, only the optimal strategy guarantees its win.

The tangent-point strategy in Fig. 13c shows the oppo-
site eﬀect in the time of arrival. By sacriﬁcing the safe
distance, this strategy delays the time the game ends,
which may become relevant in a multi-player game where
it tries to keep the defender away from other intruders.
The result of this example highlights the fact that the
optimal strategy will be diﬀerent if the intruder’s objec-
tive is to delay the capture as much as possible.

We omit the demonstration of the suboptimal defender
strategy since it is already shown clearly with Fig. 6 in
Sec. 3.2.

6.2 Multiplayer Game

The example provided in Sec. 5 (Fig. 12a) showed a triv-
ial case in which the MIS defense outperforms MM de-
fense, i.e., a case where QMIS < QMM. Here, we show

18
(a) (b) (c) (d)

1

2

3
 1

2

3
 t = 1
 1
2

3
 1

2

3
 t = 105
 1
23
 1

2

3
 t = 153
 12
3
 2

3
 t = 284

Fig. 14. Simulation snapshots of MM defense.

1

2

3
 1

2

3
 t = 1
 1
2
3
 1

2

3
 t = 105
 123
 1

2

3
 t = 200
 1
3
 2

3
 t = 285

(a) (b) (c) (d)

Fig. 15. Simulation snapshots of MIS defense.

an example where the two strategies initially have the
same guarantee QMM = QMIS, but only MIS actually
performs better than the initially provided bound.

Simulation snapshots of a three vs. three scenario are
shown in Fig. 14 and 15 for MM defense and MIS defense
respectively. 12 The small yellow stars indicate each in-
truder’s breaching point, the dash-dotted lines indicate
the one vs. one assignments, and the solid blue lines in-
dicate the two vs. one assignments.

The intruders are performing independently greedy be-
havior: i.e., there is no team coordination. 13 Each in-
truder ﬁnds the closest pair of defenders that contains
itself in the “relevant region”, deﬁned by the area be-
tween the two aﬀerent surfaces (see Fig. 9a). Then the
intruder plays the two vs. one game against the pair. For
example, in Fig. 14a both A1 and A2 are located in the
relevant region against the pair (D1, D2), and therefore
move towards the mid point between the two defenders.

12 Also see https://youtu.be/h0_VqJbNsQc for the ani-
mated version.
13 See [39] for a coordinated team strategy of the intruders.
 Once the intruder converges on the aﬀerent surface of
a defender, the relevant region may start switching fre-
quently. For example, at time t = 105, the intruder A2 is
already on the aﬀerent surface of defender D2. Depend-
ing on the side of a small deviation, the relevant pair
for A2 switches between (D1, D2) and (D2, D3). Such
switching causes the intruder to follow a zigzag path to-
wards defender D2. To avoid such degenerate behavior,
we add a small bias towards ccw direction when the in-
truder selects the pair, which is why A2 selects the pair
(D2, D3). The kink in the path of A3 (see Fig. 14d), is
generated due to the switching from the midpoint be-
tween (D2, D3) to the one between (D3, D1).

The MM assignment shown in Fig. 14, has two valid
edges giving N cap
A = 2 and QMM = NA−N cap
A = 1. Since
this MM assignment does not specify any behavior to
the unassigned defenders, we also consider a secondary
matching between the unassigned intruders and defend-
ers. Defender D1 gets this secondary assignment towards
A1, which is why D1 moves ccw. As the QMM from the
MM analysis expected, A1 scores a point (Fig. 14d).

The MIS assignment shown in Fig. 15 also has N cap
A = 2
at the beginning, only guaranteeing Q ≤ QMIS = 1. For

19

this small problem, the computation time of the MIS
defense strategy was 5 ms. The pair (D1, D2) initially
plays the two vs. one game against A1. However, at time
t = 105, the intruder A1 moves into RD(D2), which frees
D1 from the two vs. one game and allows it to perform
a one vs. one game against A2. At this point, the score
upperbound has changed to QMIS = 0, and the defender
team guarantees that no intruder scores.

Although the score bound provided by QMIS is tighter
than QMM (see Sec. 5), this example highlights that it
may still not be the smallest upper bound. Speciﬁcally,
the MIS analysis could not predict the outcome Q = 0
from the initial conﬁguration. We also note that the MIS
assignment is non-unique; in fact, it could have selected
the same edge set as the MM assignment in this ex-
ample, because they both have the same cardinality. In
other words, the two assignments are equally good in the
instantaneous analysis. However, only the assignment
shown in Fig. 15 leads to the capture of all intruders.

If we use the LGR defense strategy, we have qk = 0 for
all the regions, and thus we have QLG = 0. This im-
plies that all intruders will be captured. The assignment
will be the same as the one in Fig. 15. However, what is
important is that the LGR strategy always makes this
“correct” decision. This is one of the reasons behind the
performance gap between MIS and LGR defense strate-
gies. In addition, unlike the MIS defense strategy, LGR
analysis could predict Q = 0 from the initial conﬁgura-
tion, showing that it is a more accurate estimate of the
game outcome.

7 Conclusion

We study a variant of the reach-avoid game with the
defenders constrained to move on the perimeter of the
target region. The intruders try to score by breaching
the perimeter while the defender team tries to mini-
mize the score by intercepting them. The one vs. one
game is solved analytically for arbitrary convex shapes,
which provides the intruder’s optimal breaching point
and the defender’s optimal direction of motion. The de-
rived strategies are at an equilibrium in terms of the
safe distance (in the attacker-winning scenario) and the
largest margin (in the defender-winning scenario). The
two vs. one game is also solved analytically, and it high-
lights the beneﬁt of cooperation among the defenders.
Speciﬁcally, two defenders can team up to perform a
pincer maneuver to reduce the intruder-winning region.
Finally, we introduce and discuss various team defense
strategies that leverage the results from one vs. one and
two vs. one games.

Acknowledgements

We gratefully acknowledge useful discussions with Chris
Kroninger, Ken Hayashima, and Alexander Von Moll.
 References

[1] Pushkarini Agharkar and Francesco Bullo. Vehicle routing
algorithms to intercept escaping targets. Proc. Amer. Control
Conf. (ACC), pages 952–957, 2014.

[2] Efstathios Bakolas and Panagiotis Tsiotras. Relay pursuit
of a maneuvering target using dynamic Voronoi diagrams.
Automatica, 48(9):2213–2220, 2012.

[3] Tamer Basar and Geert Jan Olsder. Dynamic Noncooperative
Game Theory, 2nd Edition. Society for Industrial and
Applied Mathematics, 2011.

[4] Shaunak D. Bopardikar, Francesco Bullo, and Jo˜ao P.
Hespanha. A cooperative homicidal chauﬀeur game.
Automatica, 45(7):1771–1777, 2009.

[5] Mo Chen, Zhengyuan Zhou, and Claire J. Tomlin. A path
defense approach to the multiplayer reach-avoid game. IEEE
Conf. Decis. Control (CDC), pages 2420–2426, 2014.

[6] Mo Chen, Zhengyuan Zhou, and Claire J. Tomlin.
Multiplayer reach-avoid games via low dimensional solutions
and maximum matching. Proc. Amer. Control Conf. (ACC),
pages 1444–1449, 2014.

[7] Mo Chen, Zhengyuan Zhou, and Claire J. Tomlin.
Multiplayer reach-avoid games via pairwise outcomes. IEEE
Trans. Autom. Control, 62(3):1451–1457, mar 2017.

[8] Timothy H Chung and Geoﬀrey A Hollinger. Search and
pursuit-evasion in mobile robotics. Auton. Robot., 31(4):299–
316, 2011.

[9] George Corliss. Which root does the bisection algorithm
ﬁnd? Siam Review, 19(2):325–327, 1977.

[10] Aleksei Fedorovich Filippov. Diﬀerential equations with
discontinuous righthand sides: control systems, volume 18.
Springer Science & Business Media, 2013.

[11] Jaime F. Fisac, Mo Chen, Claire J. Tomlin, and S. Shankar
Sastry. Reach-avoid problems with time-varying dynamics,
targets and constraints. Proc. 18th Int. Conf. Hybrid Sys.
Comp. Control (ACM), pages 11–20, 2015.

[12] Jaime F. Fisac and S. Shankar Sastry. The pursuit-
evasion-defense diﬀerential game in dynamic constrained
environments. IEEE Conf. Decis. Control (CDC), pages
4549–4556, 2015.

[13] M Foley and W Schmitendorf. A class of diﬀerential games
with two pursuers versus one evader. IEEE Trans. Autom.
Control, 19(3):239–243, 1974.

[14] Zachariah E. Fuchs, Pramod P. Khargonekar, and Johnny
Evers. Cooperative defense within a single-pursuer, two-
evader pursuit evasion diﬀerential game. IEEE Conf. Decis.
Control (CDC), pages 3091–3097, 2010.

[15] Eloy Garcia, David W. Casbeer, Khanh Pham, and Meir
Pachter. Cooperative aircraft defense from an attacking
missile. J. Guid. Control Dyn, 38(8):1510–1520, 2015.

[16] Eloy Garcia, David W Casbeer, Alexander Von Moll, and
Meir Pachter. Cooperative two-pursuer one-evader blocking
diﬀerential game. In Proc. Amer. Control Conf. (ACC),
pages 2702–2709. IEEE, 2019.

[17] Eloy Garcia, David W Casbeer, Alexander Von Moll, and
Meir Pachter. Multiple pursuer multiple evader diﬀerential
games. IEEE Trans. Autom. Control, 2020.

[18] Eloy Garcia, Zachariah E. Fuchs, Dejan Milutinovic,
David W. Casbeer, and Meir Pachter. A Geometric Approach
for the Cooperative Two-Pursuer One-Evader Diﬀerential
Game. IFAC-PapersOnLine, 50(1):15209–15214, 2017.

20

[19] Eloy Garcia, Alexander Von Moll, David W Casbeer, and
Meir Pachter. Strategies for defending a coastline against
multiple attackers. In IEEE Conf. Decis. Control (CDC),
pages 7319–7324, 2019.

[20] Haomiao Huang, Jerry Ding, Wei Zhang, and Claire J.
Tomlin. A diﬀerential game approach to planning in
adversarial scenarios: A case study on capture-the-ﬂag. IEEE
Int. Conf. Rob. Autom. (ICRA), pages 1451–1456, 2011.

[21] Haomiao Huang, Wei Zhang, Jerry Ding, Duˇsan M.
Stipanovi´c, and Claire J. Tomlin. Guaranteed decentralized
pursuit-evasion in the plane with multiple pursuers. IEEE
Conf. Decis. Control (CDC), pages 4835–4840, 2011.

[22] Rufus Isaacs. Diﬀerential games: A mathematical theory with
applications to warfare and pursuit, control and optimization.
Courier Corporation, 1999.

[23] Andrew J. Kerns, Daniel P. Shepard, Jahshan A. Bhatti, and
Todd E. Humphreys. Unmanned aircraft capture and control
via GPS spooﬁng. J. Field Rob., 31(4):617–636, 2014.

[24] Tae Hyoung Kim and Toshiharu Sugie. Cooperative control
for target-capturing task based on a cyclic pursuit strategy.
Automatica, 43(8):1426–1431, 2007.

[25] Jon Kleinberg and Eva Tardos. Algorithm design. Addison
Wesley, 2006.

[26] Li Liang, Fang Deng, Zhihong Peng, Xinxing Li, and
Wenzhong Zha. A diﬀerential game for cooperative target
defense. Automatica, 102:58–71, 2019.

[27] Shih-Yuan Liu, Zhengyuan Zhou, Claire Tomlin, and J Karl
Hedrick. Evasion of a team of dubins vehicles from a hidden
pursuer. In IEEE Int. Conf. Rob. Autom. (ICRA), pages
6771–6776, 2014.

[28] Shih-Yuan Liu, Zhengyuan Zhou, Claire Tomlin, and Karl
Hedrick. Evasion as a team against a faster pursuer. In IEEE
Proc. Amer. Control Conf. (ACC), pages 5368–5373, 2013.

[29] Venkata Ramana Makkapati, Wei Sun, and Panagiotis
Tsiotras. Optimal Evading Strategies for Two-Pursuer/One-
Evader Problems. J. Guid. Control Dyn, 41(4):851–862, 2018.

[30] Venkata Ramana Makkapati and Panagiotis Tsiotras.
Optimal Evading Strategies and Task Allocation in Multi-
player Pursuit–Evasion Problems. Dynamic Games and
Applications, pages 1–20, 2019.

[31] Robert Mitchell and Ing Ray Chen. Adaptive intrusion
detection of malicious unmanned air vehicles using behavior
rule speciﬁcations. IEEE Trans. Syst. Man Cybern.: Syst.,
44(5):593–604, 2014.

[32] Dave W. Oyler, Pierre T. Kabamba, and Anouck R.
Girard. Pursuit-evasion games in the presence of obstacles.
Automatica, 65:1–11, 2016.

[33] Meir Pachter, Alexander Von Moll, Eloy Garcia, David W
Casbeer, and Dejan Milutinovi´c. Singular trajectories in
the two pursuer one evader diﬀerential game. In 2019
International Conference on Unmanned Aircraft Systems
(ICUAS), pages 1153–1160. IEEE, 2019.

[34] Fabio Pasqualetti, Antonio Franchi, and Francesco Bullo.
On cooperative patrolling: Optimal trajectories, complexity
analysis, and approximation algorithms. IEEE Trans. Rob.,
28(3):592–606, 2012.

[35] Alyssa Pierson, Zijian Wang, and Mac Schwager. Intercepting
rogue robots: An algorithm for capturing multiple evaders
with multiple pursuers. IEEE Rob. Autom. Lett., 2(2):530–
537, 2017.

[36] Sergey Rubinsky and Shaul Gutman. Three-Player Pursuit
and Evasion Conﬂict. J. Guid. Control Dyn, 37(1):98–110,
2014.
 [37] William L. Scott and Naomi E. Leonard. Optimal evasive
strategies for multiple interacting agents with motion
constraints. Automatica, 94:26–34, 2018.

[38] Jhanani Selvakumar and Efstathios Bakolas. Feedback
strategies for a reach-avoid game with a single evader and
multiple pursuers. IEEE Trans. Cybern., PP:1–12, 2019.

[39] Daigo Shishika and Vijay Kumar. Local-game decomposition
for multiplayer perimeter-defense problem. In IEEE Conf.
Decis. Control (CDC), pages 2093–2100, 2018.

[40] Daigo Shishika, James Paulos, Michael R Dorothy, M Ani
Hsieh, and Vijay Kumar. Team composition for perimeter
defense with patrollers and defenders. In IEEE Conf. Decis.
Control (CDC), pages 7325–7332, 2019.

[41] Daigo Shishika, James Paulos, and Vijay Kumar.
Cooperative team strategies for multi-player perimeter-
defense games. IEEE Rob. Autom. Lett., 5(2):2738–2745,
2020.

[42] Ryo Takei, Richard Tsai, Zhengyuan Zhou, and Yanina
Landa. An eﬃcient algorithm for a visibility-based
surveillance-evasion game. Comm. in Math. Sci., 12(7):1303–
1327, 2014.

[43] Alexander Von Moll, David Casbeer, Eloy Garcia, Dejan
Milutinovi´c, and Meir Pachter. The multi-pursuer single-
evader game. J. Intel. Rob. Syst., 96(2):193–207, 2019.

[44] Alexander Von Moll, Eloy Garcia, David Casbeer, M Suresh,
and Sufal Chandra Swar. Multiple-pursuer, single-evader
border defense diﬀerential game. J. Aero. Info. Syst., pages
1–10, 2019.

[45] Alexander Von Moll, Meir Pachter, Eloy Garcia, David
Casbeer, and Dejan Milutinovi´c. Robust policies for a
multiple-pursuer single-evader diﬀerential game. Dynamic
Games and Applications, 10(1):202–221, 2020.

[46] Rui Yan, Xiaoming Duan, Zongying Shi, Yisheng Zhong,
and Francesco Bullo. Maximum-matching capture strategies
for 3d heterogeneous multiplayer reach-avoid games. arXiv
preprint arXiv:1909.11881, 2019.

[47] Rui Yan, Zongying Shi, and Yisheng Zhong. Escape-avoid
games with multiple defenders along a ﬁxed circular orbit.
In 13th IEEE Int. Conf. Control & Autom. (ICCA), pages
958–963. IEEE, 2017.

[48] Rui Yan, Zongying Shi, and Yisheng Zhong. Reach-avoid
games with two defenders and one attacker: An analytical
approach. IEEE Trans. Cybern., 49(3):1035–1046, 2018.

[49] Rui Yan, Zongying Shi, and Yisheng Zhong. Task assignment
for multiplayer reach–avoid games in convex domains via
analytical barriers. IEEE Trans. Rob., 36(1):107–124, 2019.

[50] Zhengyuan Zhou, Jerry Ding, Haomiao Huang, Ryo Takei,
and Claire Tomlin. Eﬃcient path planning algorithms in
reach-avoid problems. Automatica, 89:28–36, 2018.

[51] Zhengyuan Zhou, Ryo Takei, Haomiao Huang, and Claire J
Tomlin. A general, open-loop formulation for reach-avoid
games. In IEEE Conf. Decis. Control (CDC), pages 6501–
6506, 2012.

[52] Zhengyuan Zhou, Wei Zhang, Jerry Ding, Haomiao Huang,
Duˇsan M. Stipanovi´c, and Claire J. Tomlin. Cooperative
pursuit with Voronoi partitions. Automatica, 72:64–72, 2016.

21
