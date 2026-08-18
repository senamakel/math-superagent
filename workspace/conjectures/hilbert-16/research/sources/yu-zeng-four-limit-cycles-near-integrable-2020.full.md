<!-- source: https://publish.uwo.ca/~pyu/pub/preprints/YZ_IJBC2020.pdf | converted from PDF -->

December 5, 2020 9:15 WSPC/S0218-1274 2050236

International Journal of Bifurcation and Chaos, Vol. 30, No. 15 (2020) 2050236 (11 pages)
c× World Scientiﬁc Publishing Company
DOI: 10.1142/S0218127420502363

Visualization of Four Limit Cycles in Near-Integrable
Quadratic Polynomial Systems*

Pei Yu† and Yanni Zeng‡

Department of Applied Mathematics, Western University,
London, Ontario, Canada N6A 5B7
†pyu@uwo.ca
‡yzeng243@uwo.ca

Received February 25, 2020; Revised May 3, 2020

It has been known for almost 40 years that general planar quadratic polynomial systems can
have four limit cycles. Recently, four limit cycles were also found in near-integrable quadratic
polynomial systems. To help more people to understand limit cycles theory, the visualization
of such four numerically simulated limit cycles in quadratic systems has attracted researchers’
attention. However, for near-integral systems, such visualization becomes much more diﬃcult
due to limitation on choosing parameter values. In this paper, we start from the simulation
of the well-known quadratic systems constructed around the end of 1979, then reconsider the
simulation of a recently published quadratic system which exhibits four big size limit cycles, and
ﬁnally provide a concrete near-integral quadratic polynomial system to show four normal size
limit cycles.

Keywords: Hilbert’s 16th problem; quadratic near-integrable system; limit cycle; Andronov–Hopf
bifurcation; Melnikov function; simulation.

1. Introduction

The well-known Hilbert’s 16th problem is remained
unsolved for more than one hundred years since
Hilbert [1902] proposed the 23 mathematical prob-
lems. A simpliﬁed version of the problem, based on
a general Li´enard equation, was chosen by Smale
[1998] as one of the 18 challenging mathematical
problems for the 21st century. Consider the follow-
ing planar system:

˙x = P (x, y), ˙y = Q(x, y), (1)

where the dot denotes diﬀerentiation with respect
to time t, P (x, y)and Q(x, y)are polynomials in x
and y. The second part of Hilbert’s 16th problem is
to ﬁnd the upper bound, called Hilbert number and
denoted by H(n), where n =max{deg P, deg Q},
 on the number of limit cycles that system (1) can
have. If the problem is restricted to the neighbor-
hood of isolated ﬁxed points, then the question
is reduced to studying degenerate Andronov–Hopf
bifurcations. In 1952, Bautin [1952] proved that
three small limit cycles exist around a ﬁne focus
or a center in quadratic systems. Almost 30 years
later, concrete examples were independently con-
structed by Shi [1979], and by Chen and Wang
[1979] to show the existence of four limit cycles in
quadratic, implying that H(2) ≥ 4. However, the
question whether H(2) = 4 is still open.
To reduce the diﬃculty in attacking the
Hilbert’s 16th problem, Arnold proposed a weak
version of the problem [Arnold, 1977], which trans-
forms the problem of determining the maximal
number of limit cycles (a geometric problem) to

∗The ﬁrst draft of this article has been posted on arXiv.org since February 25, 2020, No. 2002.09987v1.
†Author for correspondence
 2050236-1Int. J. Bifurcation Chaos 2020.30. Downloaded from www.worldscientific.comby CITY UNIVERSITY OF HONG KONG on 12/12/20. Re-use and distribution is strictly not permitted, except for Open Access articles.
December 5, 2020 9:15 WSPC/S0218-1274 2050236

P. Yu & Y. Zeng

ﬁnding the maximal number of isolated zeros of the
Abelian integral or Melnikov function (an algebraic
problem):

M (h)= ∮

H(x,y)=h Q(x, y)dx − P (x, y)dy, (2)

where H(x, y),P and Q are all real polynomials in x
and y with deg H = n+1, and max{deg P, deg Q}≤
n. The weak Hilbert’s 16th problem is closely
related to the maximal number of limit cycles in
the following near-Hamiltonian system [Han, 2006]:

˙x = ∂H(x, y)
∂y + εpn(x, y),

˙y = − ∂H(x, y)
∂x + εqn(x, y),
 (3)

where pn(x, y)and qn(x, y)are nth-degree polyno-
mials in x and y,and H(x, y) is a polynomial in x
and y with deg H = n +1, and 0 <ε ≪ 1 indicat-
ing the small perturbations εpn(x, y)and εqn(x, y)
on the system. When ε = 0, (3) is reduced to a
Hamiltonian system, and the ﬁrst-order (ε-order)
Melnikov function becomes

M (h)= ∮
H(x,y)=h qn(x, y)dx − pn(x, y)dy. (4)

In this paper, we focus on quadratic systems,
i.e. on the case n = 2 in (1), and pay particular
attention to the numerical realization of four limit
cycles which are visualizable. In general, a quadratic
system which has at least two singularities can be
writteninthe form of [Chen&Wang, 1979; Ye,
1982]
 ˙x = −y + lx2 + mxy + ny2,

˙y = x(1 + ax + by), (5)

which, under the assumption n ̸= 0, can be rescaled
to
 ˙x = −y + lx2 + mxy + y2,

˙y = x(1 + ax + by). (6)

System (6) is exactly the same as the system given
in [Yu & Han, 2012] under the transformation
(x, y) → (y, x):

˙x = y(1 + a1x + a2y),

˙y = −x + x2 + a3xy + a4y2. (7)

Note that system (6) has two singularities at (0, 0)
and (0, 1), while system (7) has two singularities at
(0, 0) and (1, 0).
 Recently, Kuznetsov et al. [2013] considered the
following quadratic system:

˙x = y + x
2 + xy,

˙y = a2x
2 + b2xy + c2y2 + α2x + β2y, (8)

and proved that the system has four limit cycles if
certain conditions on the parameters are satisﬁed.
In particular, they chose a set of parameter values
to show four big size limit cycles.
To consider perturbing an integrable system,
we need (0, 0) to be a center, for which it has the
classiﬁcations as follows. The origin of (7) is a cen-
ter if and only if one of the following conditions is
satisﬁed [Yu & Han, 2012],

QR
3 –Reversiblesystem: a3 = a2 =0;

QH
3 – Hamiltonian system: a3 = a1 +2a4 =0;

QLV
3 – Lokta–Volterra system:

a2 =1 + a4 =0; and

Q4 – Codimension-4 system: a3 − 5a2

= a1 − (5 + 3a4)= a4 +2(1 + a
2
2)=0.

In this paper, we will perturb the reversible system
to obtain the following perturbed one [Yu & Han,
2012]:

˙x = y(1 + a1x)+ εpn(x, y)

= y(1 + a1x)+ εa10x,

˙y = −x + x2 + a4y2 + εqn(x, y)

= −x + x2 + a4y2 + ε(b01y + b11xy),
 (9)

where a10,b01 and b11 are perturbation parameters.
Numerical simulation is a common powerful
approach in illustrating solution trajectories of
dynamical systems, in particular, for complex
behaviors such as limit cycles and chaotic oscil-
lations, which do not have analytical solution
formulas. Many studies have been focused on devel-
oping eﬃcient numerical approaches for dynamical
systems, for example, see [Johnson et al., 1997;
Johnson, 1998; Wischgoll & Scheuermann, 2001;
Kawai et al., 2007]. Although modern computers
allow us to perform simulations on complicated
nonlinear dynamical systems, it turns out that
the possibilities of naive approach, based on the
construction of trajectories by numerical integra-
tion of complex diﬀerential equations, are very

2050236-2Int. J. Bifurcation Chaos 2020.30. Downloaded from www.worldscientific.comby CITY UNIVERSITY OF HONG KONG on 12/12/20. Re-use and distribution is strictly not permitted, except for Open Access articles.
December 5, 2020 9:15 WSPC/S0218-1274 2050236

Visualization of Four Limit Cycles in Quadratic Systems

limited. Even for two-dimensional planar dynami-
cal systems, simulating three limit cycles bifurcat-
ing from a single Andronov–Hopf critical point is
not an easy task (e.g. see [Huang et al., 2019]).
Recently, visualization of simulating four limit
cycles in planar quadratic polynomial systems has
attracted researchers’ attention [Kuznetsov et al.,
2013; Leonov et al., 2013]. Such work not only pro-
vides a direct way of understanding complex theo-
retical results, but also promotes the development
on eﬃcient numerical integration methods.
In this paper, we consider bifurcation of limit
cycles in the quadratic systems (6), (8) and (9), and
show simulated visualizable four limit cycles. Since
the convergence for small limit cycles is extremely
slow, particularly for system (9), we apply the
Runge–Kutta (R–K) fourth-order method to sim-
ulate small limit cycles on a Desktop machine with
CPU@3.20 GHz, and use Matlab solver ODE23 to
simulate large limit cycles. For unstable limit cycles,
we use backward time (i.e. using negative time step)
and so the unstable limit cycles become “stable”. In
the next section, we consider the quadratic exam-
ples proposed by Shi [1979], and by Chen and Wang
[1979]. In Sec. 3, we reconsider the example con-
structed by Kuznetsov et al. [2013] to demonstrate
four big size limit cycles. Finally, we present a con-
crete near-integrable quadratic system [Yu & Han,
2012] to show four normal size limit cycles.

2. Four Limit Cycles Obtained in
[Shi, 1979; Chen & Wang, 1979]

In this section, we consider the two concrete
quadratic systems given by Shi [1979] and by Chen
 and Wang [1979]. The Shi example is given by the
following equations [Shi, 1979]:

˙x = λx − y − 10x
2 +(5+ δ)xy + y2,

˙y = x + x2 +(−25 + 8ϵ − 9δ)xy, (10)

where the parameter values chosen in [Shi, 1979] are

λ = −10
−250,ϵ = −10
−52,δ = −10
−13, (11)

for proving the existence of four limit cycles. The
example given by Chen and Wang in [1979] is
described as

˙x = −δ2x − y − 3x
2 +(1 − δ1)xy + y2,

˙y = x + 2
9 x2 − 3xy, (12)

where 0 <δ1,δ2 ≪ 1, but not speciﬁed.
Firstly it is noted that the two systems (10)
and (12) have the exact same structure of (6). Sec-
ondly it was proved that both systems have a big
stable limit cycle around the unstable focus (0, 1),
and three small limit cycles around the stable focus
(0, 0). The schematic diagrams showing the exis-
tence of limit cycles are depicted in Fig. 1.
Note that when λ = ϵ = δ = 0, the origin of
system (10) is a third-order ﬁne focus, while the
origin of system (12) is a second-order ﬁne focus
when δ1 = δ2 = 0. In [Shi, 1979] the author explic-
itly constructed four trapping regions [see Fig. 1(a)]
and applied Bendixson theory to prove the existence
of four limit cycles, one of them around (0, 1) and
three of them around (0, 0) which were obtained
by perturbing the third-order ﬁne focus using the
three parameters. On the other hand, Chen and
Wang [1979] constructed two trapping regions [see

(a) (b)

Fig. 1. Schematic diagrams showing the existence of limit cycles for (a) system (10) (see Fig. 1 in [Shi, 1979]); and (b) sys-
tem (12) (see Fig. 3 in [Chen & Wang, 1979]).
 2050236-3Int. J. Bifurcation Chaos 2020.30. Downloaded from www.worldscientific.comby CITY UNIVERSITY OF HONG KONG on 12/12/20. Re-use and distribution is strictly not permitted, except for Open Access articles.
December 5, 2020 9:15 WSPC/S0218-1274 2050236

P. Yu & Y. Zeng

Fig. 1(b)] and used Bendixson theory to prove the
existence of the big limit cycle around (0, 1) and a
small one around (0, 0). Then they showed further
perturbing the second-order ﬁne focus (0, 0) using
the parameters δ1 and δ2 to obtain two more small
limit cycles, but did not specify the values of δ1
and δ2. The stability of the four limit cycles is same
for both systems: The big one around the unsta-
ble focus (0, 1) is stable, and the outer most small
limit cycle around (0, 0) is unstable, the middle one
is stable and the inner most one is unstable. The
focus (0, 0) is stable. Figure 2 shows the simulation
of the big limit cycle for systems (10) and (12) when
λ = ϵ = δ = δ1 = δ2 = 0. Two initial points are cho-
sen for simulating the trajectories with one outside
the limit cycle (in blue color) and one inside the
limit cycle (in red color), both converging to the
stable limit cycle (in green color).
To simulate the small limit cycles, the param-
eter values used by Shi, given in (11), to prove the
existence of four limit cycles cannot be used for sim-
ulation since they are too small. When these param-
eters vanish, the focus values are

v0 = v1 = v2 =0,v3 = 35625
8 .

Since v3 is pretty large, we must choose the param-
eter values such that the three limit cycles are
very small. To achieve this, we choose the follow-
ing parameter values:

λ = − 2
108 ,ϵ = − 1
1000 ,δ = − 1
10 , (13)

which are much larger than that used by Shi given
in (11). With these parameter values, we apply the
Maple program [Yu, 1998] to obtain the following
 focus values:

v0 = − 1
108 ,v1 = 1
103 ,v2 = − 2079402109
112500000 ,

v3 = 59143866813736153313
16200000000000000 .

Then, the truncated normal form up to third-order
terms is given by

˙r = v0 + v1r2 + v2r4 + v4r6. (14)

Solving ˙r = 0 yields the approximation of the ampli-
tudes of the three small limit cycles as follows:

r1 ≈ 0.003636,r2 ≈ 0.006431,r3 ≈ 0.070769.

The simulation of the three small limit cycles is
shown in Fig. 3, obtained using the R–K fourth-
order method since Matlab solver ODE23 (or
ODE45) takes too much time to get convergence.
For a clear view, we only present the data of form-
ing the limit cycles, but for each of the limit cycles
we show two trajectories converging to the same
limit cycle, one from outside the limit cycle (in blue
color) and one from inside the limit cycle (in red
color). It can be seen from Fig. 3 that the analyti-
cal predictions agree very well with the simulations.
With the parameter values given in (13), the
simulated big limit cycle is obtained using Matlab
solver ODE23, as shown in Fig. 4(a). Comparing
this ﬁgure with Fig. 2(a) shows that small pertur-
bation parameter values can cause obvious change
on the size of the limit cycle.
Next, we consider the example proposed by
Chen and Wang [1979], given in (12). Setting δ1 =
δ2 = 0 yields the focus values v0 = v1 =0,v2 =
− 77
972 ≈−0.079218. Thus, we can choose δ1 and
δ2 to obtain two small limit cycles with the outer

(a) (b)

Fig. 2. Simulation of big limit cycle for (a) system (10) when λ = δ = ϵ = 0 with initial points (−18, 150) and (−5, 30); and

(b) system (12) when δ1 = δ2 = 0 with initial points (−1.5 × 10
11, 5 × 10
11)and (−10
11, 2 × 10
11).

2050236-4Int. J. Bifurcation Chaos 2020.30. Downloaded from www.worldscientific.comby CITY UNIVERSITY OF HONG KONG on 12/12/20. Re-use and distribution is strictly not permitted, except for Open Access articles.
December 5, 2020 9:15 WSPC/S0218-1274 2050236

Visualization of Four Limit Cycles in Quadratic Systems

(a) (b)

(c) (d)

Fig. 3. Simulation of third small limit cycles using the R–K fourth-order method for system (10) with λ = −2 × 10
−8,
ϵ = −0.001 and δ = −0.1: (a) the outer most limit cycle with time step Δt = −0.001, and initial points (0, −3) and (0, 0.006);
(b) the middle limit cycle with Δt =0.01, and initial points (0, 0.006) and (0, 0.004); (c) the inner most limit cycle with
Δt = −0.01, and initial points (0, 0.004), (0, 0.001); and (d) three small limit cycles with the stable one in red color and
unstable ones in blue color.
 (a) (b)

Fig. 4. Simulation of the stable big limit cycle using Matlab solver ODE23: (a) for system (10) taking λ = −2 × 10
−8,
ϵ = −0.001, δ = −0.1, with initial points (−18, 150) and (−5, 30); and (b) for system (10) taking δ1 =0.01, δ2 =0.00002,

with initial points (−0.6 × 10
11, 10
11)and (−0.3 × 10
11, 10
11).

2050236-5Int. J. Bifurcation Chaos 2020.30. Downloaded from www.worldscientific.comby CITY UNIVERSITY OF HONG KONG on 12/12/20. Re-use and distribution is strictly not permitted, except for Open Access articles.
December 5, 2020 9:15 WSPC/S0218-1274 2050236

P. Yu & Y. Zeng
 (a) (b)

(c) (d)

Fig. 5. Simulation of three small limit cycles using the R–K fourth-order method for system (12) with δ1 =0.01 and
δ2 =0.00002: (a) the outer most limit cycle with time step Δt = −0.001, and initial points (0, 0.22) and (0, 0.15); (b) the
middle limit cycle with Δt =0.001, and initial points (0, 0.15) and (0, 0.06); (c) the inner most limit cycle with Δt = −0.001,
and initial points (0, 0.06), (0, 0.01); and (d) three small limit cycles with the stable one in red color and unstable ones in blue
color.

one stable. Then by Bendixson theory, one more
small unstable limit cycle can be obtained, which
encloses the two small limit cycles. For this pur-
pose, we choose

δ1 =0.01,δ2 =0.00002, (15)

under which

v0 = −10
−5,v1 =0.0025,

v2 = − 172948799
2332800000 ≈−0.074138.

Then the truncated normal form ˙r = −10−5 +
0.0025r2 − 0.074138r4 gives the approximation of
the amplitudes of the two small limit cycles as
r1 =0.068102 and r2 =0.170538.
With the parameter values, the simulated big
limit cycle is obtained using Matlab solver ODE23,
as shown in Fig. 4(b). Comparing this ﬁgure with
Fig. 2(b) again shows that very small perturbation
parameter values can have great inﬂuence on the
size of the limit cycle. For this case, the limit cycle
 obtained with δ1 =0.01,δ2 =0.00002 is only about
1/3 of that obtained with δ1 = δ2 =0.
The simulated three small limit cycles are
shown in Fig. 5. Again for a clear view, for each of
the limit cycles we show two trajectories converging
to the same limit cycle, one from outside the limit
cycle (in blue color) and one from inside the limit
cycle (in red color). It can be seen from this ﬁgure
that the analytical predictions for the two smaller
limit cycles agree very well with the simulations.

3. Four Big Size Limit Cycles
Obtained in [Kuznetsov et al.,
2013]

In this section, we consider system (8). For this sys-
tem Kuznetsov et al. [2013] proved that it has four
limit cycles if the following conditions hold:

b2 ∈ (1, 3),c2 ∈ ( 1
3 , 1
),

2050236-6Int. J. Bifurcation Chaos 2020.30. Downloaded from www.worldscientific.comby CITY UNIVERSITY OF HONG KONG on 12/12/20. Re-use and distribution is strictly not permitted, except for Open Access articles.
December 5, 2020 9:15 WSPC/S0218-1274 2050236

Visualization of Four Limit Cycles in Quadratic Systems

(a) (b)

Fig. 6. Simulation of limit cycles using Matlab solver ODE23 for system (8) with the parameter values given in (17): (a) three
limit cycles around the unstable focus (0, 0); and (b) one big unstable limit cycle (in green color) around the stable focus
(−6.2596, 7.4498), with two trajectories starting from the initial points (−4500, 0) (in blue color) and (−2500, 0) (in red color).

4a2(c2 − 1) > (b2 − 1)
2,b2c2 > 1,

α2 ∈ ( a2(b2 +2)
b2c2 − 1 , a2(b2 +2)
b2c2 − 1 + δ),

β2 ∈ (0,ε), 0 <ε ≪ δ ≪ 1. (16)

The following parameter values:

a2 = −10,b2 =2.2,c2 =0.7,

α2 = −72.7778,β =0.0015, (17)

were chosen in [Kuznetsov et al., 2013] to obtain
four big size limit cycles. With the above parameter
values, system (8) has two ﬁxed points,

E0 =(0, 0) and E1 =(−6.2596, 7.4498).

We use the parameter values in (17) and apply Mat-
lab solver ODE23 to obtain the simulated three
limit cycles around E0 as showninFig. 6(a), and
one big unstable limit cycle around E1 as shown in
Fig. 6(b). Note that the three limit cycles shown in
Fig. 6(a) are those loops between diﬀerent colors.
The outside red trajectory converges to the outer
most limit cycle, while the blue trajectory “con-
verges” to the middle unstable limit cycle using
backward time integration, the green trajectory
converges to the inner most stable limit cycle, and
the inside red trajectory “converges” to the unsta-
ble focus E0 using backward time integration. In
Fig. 6(b), with backward time integration, two tra-
jectories “converge” to the unstable big limit cycle
(in green color), one from outside (in blue color)
and one from inside (in red color).
 4. Four Normal Size Limit Cycles
Obtained for the Near-Integrable
System (9)

Finally, we study the bifurcation of four limit cycles
in near-integrable system (9). This system has two
centers at (0, 0) and (0, 1) at ε =0. The Mel-
nikov function method has been used in [Yu & Han,
2012] to show that when a1 < −1, system (9) can
have small limit cycles bifurcating from the two cen-
ters (0, 0) and (1, 0) with distributions: (3, 0), (0, 3),
(2, 0), (0, 2) and (1, 1). The Melnikov functions
associated with the two centers are respectively
given by

M0(h, aij ,bij)

= μ00(h − h00)+ μ01(h − h00)
2

+ μ02(h − h00)
3 + μ03(h − h00)
4

+ O((h − h00)
5), for 0 <h − h00 ≪ 1,

M1(h, aij ,bij)

= μ10(h10 − h)+ μ11(h10 − h)
2

+ μ12(h10 − h)
3 + μ13(h10 − h)
4

+ O((h10 − h)
5), for 0 <h10 − h ≪ 1,
(18)

where

Lh : H(x, y)= h
 {∈ (h00, ∞), for 1 + a1x> 0,

∈ (−∞,h10), for 1 + a1x< 0,

2050236-7Int. J. Bifurcation Chaos 2020.30. Downloaded from www.worldscientific.comby CITY UNIVERSITY OF HONG KONG on 12/12/20. Re-use and distribution is strictly not permitted, except for Open Access articles.
December 5, 2020 9:15 WSPC/S0218-1274 2050236

P. Yu & Y. Zeng

h00 = H(0, 0)

= 1+ a1 − a4
2a4(a1 − a4)(a1 − 2a4) , for 1 + a1x> 0,

h10 = H(1, 0) = − (a1 +1)(a4 +1)
2a4(a1 − a4)(a1 − 2a4)

× (−1 − a1)
− 2a4
a1 , for 1 + a1x< 0, (19)

and the coeﬃcients μij,i =0, 1; j =0, 1, 2,... can
be obtained by using the Maple programs developed
in [Han et al., 2009]. It should be noted that all
the coeﬃcients μ1k,k =1, 2,... obtained in [Han
et al., 2009] should be multiplied by −1, since the
rotations along the loop H(x, y)= h on the right-
hand side and left-hand side of the line x = − 1
a1
have opposite directions. But this error does not
aﬀect the conclusion on the number of bifurcating
limit cycles.
Further, the following results were proved in
[Yu & Han, 2012]. For the case of bifurcation
of small limit cycles from the two centers (0, 0)
and (1, 0) with (3, 0)-distribution (resp., (0, 3)-
distribution) there exists at least one large limit
cycle near Lh for some h ∈ (−∞,h10) (respectively
for some h ∈ (h00, ∞)). For the case of limit cycles
with (2, 0)-distribution (resp., (0, 2)-distribution)
there exist at least two large limit cycles, one near
Lh1 for some h1 ∈ (−∞,h10)and onenear Lh2 for
some h2 ∈ (h00, ∞). There exist corresponding val-
ues of the parameters a1 and a4 for the existence of
four limit cycles.
Four cases were considered in [Yu & Han, 2012]
to yield four limit cycles, as described below.

(A) (3, 0)-distribution for small limit cycles plus a
(0, 1)-distribution of large limit cycle, resulting
in (3, 1)-distribution, with the parameter val-
ues given by

a1 = − 30
7 ,a4 = 1
3 (a1 − 5) − ε1,

b11 = (a1 +2a4)(1 + a4 − a1)
1+ a4 a10 − ε2,

b01 = −a10 − ε3,

where εk, k =1, 2, 3 are perturbation para-
meters.
(B) (0, 3)-distribution for small limit cycles plus a
(1, 0)-distribution of large limit cycle, result-
ing in a (1, 3)-distribution, with the parameter
values given by
 a1 = − 70
51 ,a4 = 1
3 (6a1 +5) − ε1,

b11 = (a1 +2a4)(2a1 − a4 +1)
(1 + a1)2(a1 − a4 +1) a10 − ε2,

b01 = −b11 + 2a4 − 1
1+ a1 a10 − ε3.

(C) (2, 0)-distribution for small limit cycles plus a
(1, 1)-distribution of large limit cycles, result-
ing in a (3, 1)-distribution, with the parameter
values given by

a1 = −4,a4 = − 18
5 − ε1,

b11 = 392
65 a10 − ε2,b01 = −a10 − ε3.

(D) (0, 2)-distribution for small limit cycles plus a
(1, 1)-distribution of large limit cycles, result-
ing in (1, 3)-distribution, with the parameter
values given by

a1 = − 4
3 ,a4 = − 6
5 − ε1,

b11 = 1176
65 a10 − ε2,b01 = − 513
65 a10 − ε3.

It should be pointed out that although the above
formulas were given in [Yu & Han, 2012] and the
existence of large limit cycles were proved using the
Melnikov function for each case, the three small
limit cycles were not explicitly shown but with a
proof on the existence of ﬁne focus with a schematic
plotting. In other words, the three perturbations
εk,k =1, 2, 3 were not deﬁnitely deﬁned to numer-
ically demonstrate the three small limit cycles.
We choose the formulas and parameter values
given in (A) for simulation. When εk =0,k =
1, 2, 3, the focus values associated with (0, 0) are

v0 = v1 = v2 =0,v3 = 347875
7260624 ≈ 0.047913.

Now we set

a10 =0.005,ε1 =0.1,ε2 =3 × 10
−5,ε3 =10
−8,

which results in

a1 = − 30
7 ,a4 = − 671
210 ,a10 = 1
200 ,

b01 = − 500001
100000000 ,b11 = 49182857
968100000 ,

2050236-8Int. J. Bifurcation Chaos 2020.30. Downloaded from www.worldscientific.comby CITY UNIVERSITY OF HONG KONG on 12/12/20. Re-use and distribution is strictly not permitted, except for Open Access articles.
December 5, 2020 9:15 WSPC/S0218-1274 2050236

Visualization of Four Limit Cycles in Quadratic Systems

Fig. 7. Simulated two trajectories for system (20), converg-
ing to the big stable limit cycle around the unstable focus
(1, 0), with the initial points (300, 0) (in red color) and (10, 0)
(in blue color).

and further taking ε = 1
100 we have system (12) in
the form of

˙x = y (1 − 30
7 x) + 1
100 × 1
200 x,

˙y = −x + x2 − 671
210 y2 + 1
100

× (− 500001
100000000 y + 49182857
968100000 xy)
.
 (20)
 Then, we apply the Maple program [Yu, 1998] to
obtain the following focus values:

v0 = − 1
200000000 ,v1 = 461
56000000 ,

v2 = − 36481804571
14817600000000 ,

v3 = 11326448548182069181
25092716544000000000 .

Then solving the truncated normal form (14) with
the above focus values we obtain the approximated
amplitudes of the three small limit cycles around
(0, 0):

r1 ≈ 0.026385,r2 ≈ 0.079134,r3 ≈ 0.140966.

However, unlike the three quadratic systems
considered in the previous two sections, the sim-
ulation for this near-integrable system is extremely
diﬃcult since the convergence speed is too slow.
We apply the R–K fourth-order method to simulate
the system and obtain the results shown in Figs. 7
and 8. Again, for each of the limit cycles we take two

(a) (b)

(c) (d)

Fig. 8. Simulation of the three small limit cycles for system (20): (a) two trajectories “converging” (backward time) to
the outer most unstable limit cycle, from the initial points (−0.35, 0) (in red color) and (−0.25, 0) (in blue color); (b) two
trajectories converging to the middle stable limit cycle, from the initial points (−0.25, 0) (in red color) and (−0.05, 0) (in
blue color); (c) two trajectories “converging” (backward time) to the inner most unstable limit cycle, from the initial points
(−0.05, 0) (in red color) and (−0.002, 0) (in blue color); and (d) three limit cycles with stable one in red color and unstable
ones in blue color.
 2050236-9Int. J. Bifurcation Chaos 2020.30. Downloaded from www.worldscientific.comby CITY UNIVERSITY OF HONG KONG on 12/12/20. Re-use and distribution is strictly not permitted, except for Open Access articles.
December 5, 2020 9:15 WSPC/S0218-1274 2050236

P. Yu & Y. Zeng
 Table 1. Simulation data for system (20).

Trajectories
Moving Towards Initial
Point Time
Step Number of
Interation CPU
Time

∞ −0.0001 10
8 2sec
(300, 0)
The large LC
(Stable) 0.0001 10
12 12 hr

(10, 0)(1, 0)
(Unstable) −0.0001 10
11 1.2 hr

∞ 0.0001 5×10
11 6hr

(−0.35, 0)The most outer LC
of the 3 small LCs
(Unstable) −0.001 10
12 12 hr

(−0.25, 0)ThemiddleLC
of the 3 small LCs
(Stable) 0.01 2×10
11 25 hr

(−0.05, 0)
The most inner LC
of the 3 small LCs
(Unstable) −0.02 8×10
12 100 hr

10
13 125 hr

(−0.002, 0)(0, 0)
(Stable) 0.02 7×10
12 87.5hr

initial points, one from outside and one from inside
the limit cycle. Also, we use the backward time in
integration scheme for unstable limit cycles. The
time step, the number of iterations and the CPU
time are given in Table 1. It should be noted that
the big stable limit cycle shown in Fig. 7 comes from
global bifurcation, rather than from Andronov–
Hopf bifurcation like the three small limit cycles,
which is usually called hidden attractor [Leonov &
Kuznetsov, 2013].

5. Conclusion

In this paper, we have considered the bifurcation
of limit cycles in planar quadratic systems and
numerically simulate four limit cycles which are
visualizable. After we study the two well-known
classical examples, and a recently published system,
we focus on near-integrable systems, and construct
a concrete example to show visualizable four limit
cycles.

Acknowledgments

This work was supported by the Natural Sci-
ences and Engineering Research Council of
 Canada (No. R2686A02). Useful discussions with
Drs. Mathieu Desroches, Jean-Pierre Franoise and
Junmin Yang are greatly appreciated.

References

Arnold, V. I. [1977] “Loss of stability of self-oscillations
close to resonance and versal deformations of equiv-
ariant vector ﬁelds,” Funct. Anal. Appl. 11, 85–92.
Bautin, N. N. [1952] “On the number of limit cycles
which appear with the variation of coeﬃcients from
an equilibrium position of focus or center type,” Mat.
Sbornik (N.S.) 30, 181–196.
Chen, L. S. & Wang, M. S. [1979] “The relative posi-
tion, and the number, of limit cycles of a quadratic
diﬀerential system,” Acta. Math. Sinica 22, 751–758.
Han, M. [2006] Bifurcation of Limit Cycles of Planar
Systems, Handbook of Diﬀerential Equations, Ordi-
nary Diﬀerential Equations, Vol. 3, eds. Canada, A.,
Drabek,P. & Fonda,A.(Elsevier).
Han, M., Yang, J. & Yu, P. [2009] “Hopf bifurcations for
near-Hamiltonian systems,” Int. J. Bifurcation and
Chaos 19, 4117–4130.
Hilbert, D. [1902] “Mathematical problems,” (M.
Newton, Transl.) Bull. Amer. Math. 8, 437–479.
Huang, J., Ruan, S., Yu, P. & Zhang, Y. [2019] “Bifur-
cation analysis of a mosquito population model with

2050236-10Int. J. Bifurcation Chaos 2020.30. Downloaded from www.worldscientific.comby CITY UNIVERSITY OF HONG KONG on 12/12/20. Re-use and distribution is strictly not permitted, except for Open Access articles.
December 5, 2020 9:15 WSPC/S0218-1274 2050236

Visualization of Four Limit Cycles in Quadratic Systems

a saturated release rate of sterile mosquitoes,” SIAM
J. Appl. Dyn. Syst. 18, 939–972.
Johnson, M. E., Jolly, M. S. & Kevrekidis, I. G. [1997]
“Two-dimensional invariant manifolds and global
bifurcations: Some approximation and visualization
studies,” Numer. Algorith. 14, 125–140.
Johnson, M. E. [1998] Computer-Assisted Studies and
Visualization of Nonlinear Phenomena: Two-Dimen-
sional Invariant Manifolds, Global Bifurcations, and
Robustness of Global Attractors, PhD thesis, Applied
and Computational Mathematics, Princeton Univer-
sity, USA.
Kawai, H., Kudo, H. & Takahashi, H. [2007] “Visualiza-
tion of a limit cycle orbit in a Taylor vortax ﬂow with
ashort annulus,” J. Chem.Eng.Japan 40, 944–950.
Kuznetsov, N. V., Kuznetsova, O. A. & Leronov, G. A.
[2013] “Visualization of four normal size limit cycles in
two-dimensional polynomial quadratic system,” Dif-
fer. Eqn. Dyn. Syst. 21, 29–34.
Leonov, G. A. & Kuznetsov, N. V. [2013] “Hidden attrac-
tors in dynamical systems. From hidden oscillations
in Hilbert–Kolmogorov, Aizerman, and Kalman prob-
lems to hidden chaotic attractor in Chua circuits,”
Int. J. Bifurcation and Chaos 23, 1330002-1–69.
 Leonov, G. A., Burova, I. G. & Aleksandrov, K. D. [2013]
“Visualization of four limit cycles of two-dimensional
quadratic systems in the parameter space,” Diﬀ.
Eqns. 49, 1675–1703.
Shi, S. [1979] “A concrete example of the existence of
four limit cycles for plane quadratic systems,” Sci.
Sinica 11, 1051–1056; [1979] (Chinese) 23, 153–158,
[1980] (English).
Smale, S. [1998] “Mathematical problems for the next
century,” The Math. Intell. 20, 7–15.
Wischgoll, T. & Scheuermann, G. [2001] “Detection and
visualization of closed streamlines in planar ﬂows,”
IEEE Trans. Visual. Comput. Graph. 7, 165–172.
Ye, Y. Q. [1982] “Some problems in the qualitative the-
ory of ordinary diﬀerential equations,” J. Diﬀ. Eqns.
46, 153–164.
Yu, P. [1998] “Computation of normal forms via a per-
turbation technique,” J. Sound and Vib. 211, 19–38.
Yu, P. & Han, M. [2012] “Four limit cycles from per-
turbing quadratic integrable systems by quadratic
polynomials,” Int. J. Bifurcation and Chaos 22,
1250254-1–28.

2050236-11Int. J. Bifurcation Chaos 2020.30. Downloaded from www.worldscientific.comby CITY UNIVERSITY OF HONG KONG on 12/12/20. Re-use and distribution is strictly not permitted, except for Open Access articles.
