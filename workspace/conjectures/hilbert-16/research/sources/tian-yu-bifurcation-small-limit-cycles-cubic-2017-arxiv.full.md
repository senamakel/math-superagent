<!-- source: https://arxiv.org/pdf/1708.07864 | converted from PDF -->

arXiv:1708.07864v1  [math.DS]  25 Aug 2017
Bifurcation of small limit cycles
in cubic integrable systems using higher-order analysis

Yun Tian
a, Pei Yu
b,1

aDepartment of Mathematics, Shanghai Normal University, Shanghai, 200234, P. R.
China
bDepartment of Applied Mathematics, Western University, London, Ontario, Canada
N6A 5B7

Abstract

In this paper, we present a method of higher-order analysis on bifurcation of
small limit cycles around an elementary center of integrable systems under
perturbations. This method is equivalent to higher-order Melinikov function
approach used for studying bifurcation of limit cycles around a center but
simpler. Attention is focused on planar cubic polynomial systems and partic-
ularly it is shown that the system studied by H. ˙Zo l¸adek in the article Eleven
small limit cycles in a cubic vector ﬁeld (Nonlinearity 8, 843–860, 1995) can
indeed have eleven limit cycles under perturbations at least up to 7th order.
Moreover, the pattern of numbers of limit cycles produced near the center
is discussed up to 39th-order perturbations, and no more than eleven limit
cycles are found.

Keywords: Bifurcation of limit cycles; Higher-order analysis; Darboux
integral; Focus value.

2000 MSC: 34C07, 34C23

1. Introduction

Bifurcation theory of limit cycles is important for both theoretical devel-
opment of qualitative analysis and applications in solving real problems. It
is closely related to the well-known Hilbert’s 16th problem [2], whose second
part asks for the upper bound, called Hilbert number H(n), on the number

1Corresponding author.
E-mail addresses: ytian22@shnu.edu.cn (Y. Tian), pyu@uwo.ca (P. Yu)

of limit cycles that the following system,

dx
dt = Pn(x, y), dy
dt = Qn(x, y), (1)

can have, where Pn(x, y) and Qn(x, y) represent n
th-degree polynomials in x
and y. This problem has motivated many mathematicians and researchers in
other disciplines to develop mathematical theories and methodologies in the
areas of diﬀerential equations and dynamical systems. However, this problem
has not been completely solved even for quadratic systems since Hilbert pro-
posed the problem in the Second Congress of World Mathematicians in 1900.
The maximal number of limit cycles obtained for some quadratic systems is
4 [3, 4]. However, whether H(2) = 4 is still open. For cubic polynomial
systems, many results have been obtained on the lower bound of the number
of limit cycles. So far, the best result for cubic systems is H(3) ≥ 13 [5, 6].
Note that the 13 limit cycles obtained in [5, 6] are distributed around several
singular points.
When the problem is restricted to consider the maximum number of small-
amplitude limit cycles, denoted by M(n), bifurcating from a focus or a center
in system (1), one of the best-known results is M(2) = 3, which was obtained
by Bautin in 1952 [10]. For n = 3, a number of results in this research
direction have been obtained. So far the best result for the number of small
limit cycles around a focus is 9 [11, 12, 13], and that around a center is
12 [14].
One of powerful tools used for analyzing local bifurcation of limit cycles
around a focus or a center is normal form theory (e.g., see [15, 16, 17, 18]).
Suppose system (1) has an elementary focus or an elementary center at the
origin. With the computation methods using computer algebra systems (e.g.,
see [9, 19, 20, 21, 22]), we obtain the normal form expressed in polar coordi-
nates as dr
dt = r (v0 + v1 r2 + v2 r4 + · · · + vk r2k + · · · ),
dθ
dt = ωc + τ0 + τ1 r2 + τ2 r4 + · · · + τk r2k + · · · , (2)

where r and θ represent the amplitude and phase of motion, respectively.
vk (k = 0, 1, 2, · · · ) is called the kth-order focus value. v0 and τ0 are obtained
from linear analysis. The ﬁrst equation of (2) can be used for studying
bifurcation and stability of limit cycles, while the second equation can be used
to determine the frequency of the bifurcating periodic motion. Moreover, the
coeﬃcients τj can be used to determine the order or critical periods of a center
(when vj = 0, j ≥ 0).
 2

A particular attention has been paid to near-integrable polynomial sys-
tems, described in the form of

dx
dt = M −1(x, y, µ)Hy(x, y, µ) + ε p(x, y, ε, δ),
dy
dt = −M −1(x, y, µ)Hx(x, y, µ) + ε q(x, y, ε, δ), (3)

where 0 < ε ≪ 1, µ and δ are vector parameters; H(x, y, µ) is an analytic
function in x, y and µ; p(x, y, ε, δ) and q(x, y, ε, δ) are polynomials in x and y,
and analytic in δ and ε. M(x, y, µ) is an integrating factor of the unperturbed
system (3)|ε=0.
Suppose the unperturbed system (3)|ε=0 has an elementary center. Then,
considering limit cycles bifurcation in system (3) around the center, we may
use the normal form theory to obtain the ﬁrst equation of (2) as follows:

dr
dt = r [
v0(ε) + v1(ε)r2 + v2(ε)r4 + · · · + vi(ε)r2i + · · · ] , (4)

where
 vi(ε) =
 ∞∑

k=1 εkVik, i = 0, 1, 2, . . . ,

in which Vik denotes the ith εk-order focus value, and will be used throughout
this paper. Note that vi(ε) = O(ε) since the unperturbed system (3)|ε=0 is
an integrable system. Further, because system (3) is analytic in ε, we can
rearrange the terms in (4), and obtain

dr
dt = V1(r) ε + V2(r) ε2 + · · · + Vk(r) εk + · · · , (5)

where
 Vk(r) =
 ∞∑

i=0 Vik r2i+1, k = 1, 2, . . . . (6)

Similarly, for the normal form of system (3) we have the θ diﬀerential
equation, given by dθ
dt = T0(r) + O(ε),

with T0(0) ̸= 0, and thus

dr
dθ = V1(r) ε + V2(r) ε2 + · · · + Vk(r) εk + · · ·
T0(r) + O(ε) . (7)

3

Assume the solution r(θ, ρ, ε) of (7), satisfying the initial condition r(0, ρ, ε) =
ρ, is given in the form of

r(θ, ρ, ε) = r0(θ, ρ) + r1(θ, ρ)ε + r2(θ, ρ)ε2 + · · · + rk(θ, ρ)εk + · · · ,

with 0 < ρ ≪ 1. Then, r0(0, ρ) = ρ and rk(0, ρ) = 0, for k ≥ 1.
If there exists a positive integer K such that Vk(r) ≡ 0, 1 ≤ k < K, and
VK(r) ̸≡ 0, then it follows from (7) that

r0(θ, ρ) = ρ, rk(θ, ρ) = 0, 1 ≤ k < K, and rK(θ, ρ) = VK(ρ)
T0(ρ) θ.

Thus, the displacement function d(ρ) of system (7) can be written as

d(ρ) = r(2π, ρ, ε) − ρ = 2π VK(ρ)
T0(ρ) εK + O(εK+1). (8)

Therefore, if we want to determine the number of small-amplitude limit cycles
bifurcating from the center in system (3), we only need to study the number
of isolated zeros of VK(ρ) for 0 < ρ ≪ 1, and have to obtain the expression
of the ﬁrst non-zero coeﬃcient VK(r) in (5) by computing ViK, for i ≥ 0.
The above discussions show that the basic idea of using focus values is ac-
tually the same as that of the Melnikov function method. Using H(x, y) = h
to parameterize the section (i.e. the Poincar´e map), we obtain the displace-
ment function of (3), given by

d(h) = M1(h)ε + M2(h)ε2 + · · · + Mk(h)εk + · · · , (9)

where
 M1(h) =
∮
H(x,y,µ)=h
M(x, y, µ)[
q(x, y, 0, δ) dx − p(x, y, 0, δ) dy]
, (10)

evaluated along closed orbits H(x, y, µ) = h for h ∈ (h1, h2). Then, we
can study the ﬁrst non-zero Melnikov function Mk(h) in (9) to determine
the number of limit cycles in system (3). In the following, we remark on
the comparison of the Melnikov function method and the method of normal
forms (or focus values).

Remark 1. (1) Let H = h, 0 < h−h1 ≪ 1 deﬁne closed orbits around the
center of system (5)|ε=0. It is easy to see that for any integer K ≥ 1,
equation (8) holds if and only if Mk(h) ≡ 0, 1 ≤ k < K and MK(h) ̸≡ 0
in (9). Moreover, VK(ρ) for 0 < ρ ≪ 1 and MK(h) for 0 < h − h1 ≪ 1
have the same maximum number of isolated zeros.

4

(2) As we can see, Vk(r) can be obtained by the computation of normal
forms or focus values.
(3) In particular, when the original system is not a Hamiltonian system but
an integrable system, then even computing the coeﬃcients of the ﬁrst-
order Melnikov function is much more involved than the computation
of using the method of normal forms.
(4) However, the method of normal forms (or focus values) is restricted to
Hopf and generalized Hopf bifurcations, while the Melnikov function
method can also be applied to study bifurcation of limit cycles from
homoclinic/heteroclinic loops or any closed orbits.

When we apply the method of normal form computation, some unneces-
sary perturbation parameters are involved in the computation of high-order
focus values, which could be extremely computation demanding (in both
time and memory), and makes it much more diﬃcult to solve the problem.
Meanwhile, before we use the ﬁrst non-zero coeﬃcient VK(r) in (5) to ﬁnd
limit cycles, we need to prove Vk(r) ≡ 0, 1 ≤ k < K. The unnecessary
parameters involved could greatly increase the diﬃculty of proving that.
In this paper, without loss of limit cycles, we introduce a linear trans-
formation to eliminate unnecessary parameters from system (3). With less
parameters in (3), we can use the approximation of ﬁrst integrals to prove
Vk(r) ≡ 0. The idea will be illuminated in Section 2.
We will apply our method to study the bifurcation of small-amplitude
limit cycles in the system

dx
dt = a + 5
2 x + xy + x
3 +
 n∑

k=1 εkpk(x, y),

dy
dt = −2ax + 2y − 3x
2 + 4y2 − ax
3 + 6x
2y +
 n∑

k=1 εkqk(x, y), (11)

where

pk(x, y) = a00k +
 3∑

i+j=1 aijk x
iyj, qk(x, y) = b00k +
 3∑

i+j=1 bijk x
iyj, (12)

in which aijk and bijk are εkth-order coeﬃcients (parameters). The unper-
turbed system (11)|ε=0 has a rational Darboux integral [23],

H0 = f 5
1
f 4
2 = (x
4 + 4x
2 + 4y)5

(x5 + 5x3 + 5xy + 5x/2 + a)4 , (13)

5

with the integrating factor M = 20f 4
1 f −5
2 . It can be shown that for a < −25/4,
system (11)|ε=0 has a center at E0 = (− a
2 , − a2+2
4 ). The system (11)|ε=0 was
proposed in [23], and it was claimed that this system could have 11 limit
cycles around the center by studying the second-order Melnikov function.
Later, Yu and Han applied the normal form computation method and got
only 9 limit cycles around E0 [24] by analyzing the ε- and ε2-order focus
values. Recently, it has been shown [25] that errors are made in [23] for
choosing 12 integrals as the basis of the linear space of corresponding Mel-
nikov functions of system (11)|ε=0. In fact, among the 12 chosen integrals,
two of them can be expressed as linear combinations of the other ten inte-
grals, and therefore only 9 limit cycles can exist, agreeing with that shown
in [24].
The rest of the paper is organized as follows. In the next section, we
consider system (3), and construct a transformation to reduce the number of
perturbation parameters, which greatly simpliﬁes the analysis in the follow-
ing section. Section 3 is devoted to the computation of higher εk-order focus
values and the existence of 11 limit cycles in system (11), which needs com-
puting at least ε7-order focus values. Finally, conclusion is drawn in Section
4.

2. Preliminaries

The method of focus values (or normal forms) is one of important and
powerful tools for the study of small-amplitude limit cycles generated from
Hopf bifurcation. In general, a suﬃcient number of focus values would be
needed if one wants to ﬁnd more small-amplitude limit cycles. One main
challenge is that the computation of focus values becomes more and more
diﬃcult as the order of focus values goes up. That is why computer algebra
systems such as Maple and Mathematica have been used for computing the
focus values to improve the computational eﬃciency (e.g. see [21, 22]). An-
other approach is to eliminate certain parameters from the system, which is
the method we shall develop here for near-integrable systems.
In most studies of near-integrable systems, full perturbations like those
polynomials p(x, y, ε, δ) and q(x, y, ε, δ) given in system (3) are considered.
The parameter vector δ usually represents the coeﬃcients in p and q. When
normal forms are used to study small limit cycles, it is easy to get and solve
the focus values of ε order (coeﬃcients in V1(r)), because they are linear
functions of the system parameters, namely the coeﬃcients in p(x, y, 0, δ)
and q(x, y, 0, δ). For the εk-order focus values (coeﬃcients in Vk(r)), more

6

parameters would be involved in the computation. One can observe that
some parameters are not necessary for obtaining the maximum number of
limit cycles, and they only increase the diﬃculty in ﬁnding limit cycles.
When the ﬁrst n functions Vk(r) in (5), 1 ≤ k ≤ n are applied to studying
bifurcation of limit cycles, in order to remove unnecessary parameters without
reducing the number of limit cycles, we may use the following transformation:




 x → x + e1(ε)x + e2(ε)y + e3(ε),
y → y + e4(ε)x + e5(ε)y + e6(ε),
t → t + e7(ε)t,
µ → µ + e8(ε),
 (14)

where ei(ε) = ei1ε + ei2ε2 + · · · + einεn, i = 1, · · · , 8.

Note that (14)|ε=0 is an identity map. Thus, (14) keeps the unperturbed
system of (3) unchanged. Furthermore, the new system obtained by using
(14) can be still written in the same form of (3). So we only need to ﬁnd
proper ei(ε)’s to get simpler perturbation functions without loss of generality.
To illustrate how to obtain ei(ε), we take system (11) as an example.
The coeﬃcients aijk and bijk in (11) are the parameters. Substituting the
transformation (14) into system (11) yields

dx
dt = a + 5
2 x + xy + x
3 +
 n∑

k=1 εk ˜pk(x, y) + o(εn),

dy
dt = −2ax + 2y − 3x
2 + 4y2 − ax
3 + 6x
2y +
 n∑

k=1 εk ˜qk(x, y) + o(εn), (15)

where

˜pk(x, y) = ˜a00k +
 3∑

i+j=1 ˜aijk x
iyj, ˜qk(x, y) = ˜b00k +
 3∑

i+j=1 ˜bijk x
iyj. (16)

Obviously, the coeﬃcients ˜aijk and ˜bijk in (16) are linear in emk, m =
1, . . . , 8. Let Ek = (e1k, e2k, · · · , e8k)T . For any 1 ≤ k ≤ n, ˜aijk and ˜bijk can
be written in the form of

˜aijk = AijEk + ηijk, ˜bijk = BijEk + ζijk,

where Aij and Bij are 1 × 8 matrices, and ηijk and ζijk, given by

ηijk = ηijk(E1, · · · , Ek−1, aml1, · · · , amlk, bml1, · · · , bmlk),
ζijk = ζijk(E1, · · · , Ek−1, aml1, · · · , amlk, bml1, · · · , bmlk), (17)

7

are polynomials in eml, 1 ≤ l ≤ k − 1, and the coeﬃcients in the perturbation
functions (12).
Note that Aij and Bij are not dependent on k. We hope that we can
ﬁnd some proper values for eik to make some of the coeﬃcients ˜aijk and ˜bijk
vanish or satisfy some conditions, so that the computation of the focus values
would become easier. For instance, we can choose for 1 ≤ k ≤ n,

˜a10k = ˜a01k = ˜a20k = ˜a11k = ˜a02k = ˜a30k = 0,

and ˜apk ≜ ˜pk(− a
2 , − a2+4
4 ) = 0, ˜aqk ≜ ˜qk(− a
2 , − a2+4
4 ) = 0. (18)

The last two equations in (18) keep the equilibrium of system (11) in a
neighborhood of E0 with radius o(εn). A direct computation yields

˜a10k = 2ae2k + e6k + 5
2e7k + η10k, ˜a01k = 1
2 e2k + e3k + η01k,
˜a20k = 3e2k + 3e3k + e4k + η20k, ˜a11k = e5k + e7k + η11k,
˜a02k = −3e2k + η02k, ˜a30k = 2e1k + ae1k + e7k + η30k,

˜apk = − 1
4 a(4 + a
2)e1k − 1
8 (4 + a
2)(2 + a
2)e2k + 1
4(4 + a
2)e3k
+ 1
4a
2e4k + 1
8a(2 + a
2)e5k − 1
2ae6k + e8k + ˜ηk,

˜aqk = − 1
8 a
2(16 + 3a
2)e1k − 1
16 a(16 + 3a
2)(2 + a
2)e2k
+ 1
4a(16 + 3a
2)e3k + 1
4a(4 + a
2)e4k + 1
8(4 + a
2)(2 + a
2)e5k

− 1
4 (4 + a
2)e6k + 1
8a(a
2 + 8)e8k + ˜ζk,
 (19)

where ˜ηk and ˜ζk are also functions in ηijl and ζijl with 1 ≤ l ≤ k − 1,
respectively.
Because

det [∂(˜a10k, ˜a01k, ˜a20k, ˜a11k, ˜a02k, ˜a30k, ˜apk, ˜aqk)
∂(e1k, e2k, e3k, e4k, e5k, e6k, e7k, e8k)
 ] = 3
4 (32 − a
4) < 0

for a < −2−5/4, we can solve (19) for emk to obtain

emk = emk(η10k, η01k, η20k, η11k, η02k, η30k, ˜ηk, ˜ζk), 1 ≤ m ≤ 8,

which can be rewritten by using (17) as

emk = ˜emk(E1, · · · , Ek−1, aij1, · · · , aijk, bij1, · · · , bijk).

Note that em1 only depends on aij1 and bij1. Therefore, for all 1 ≤ m ≤ 8,
1 ≤ k ≤ n, emk can be expressed as a polynomial in aijl and bijl, 1 ≤ l ≤ k.
In other words, (18) has solutions for all 1 ≤ k ≤ n.

8

Thus, without loss of generality, we assume that (12) takes the following
form,
 pk(x, y) = a00k + a21kx
2y + a12kxy2 + a03ky3,
qk(x, y) = b00k + b10kx + b01ky + b20kx
2 + b11kxy + b02ky2

+b30kx
3 + b21kx
2y + b12kxy2 + b03ky3, (20)

with

a00k = 1
64(a
2 + 2)[
(a
2 + 2)2 a03k + 2a(a
2 + 2) a12k + 4a
2a21k]
,

b00k = 1
64{
8a
3b30k +16a(2b10k −ab20k)+4(a
2+2)(4b01k −2ab11k +a
2b21k)

− (a
2 + 2)2[
4b02k − 2ab12k − (a
2 + 2)b03k]}
. (21)
As mentioned in Section 1, to ﬁnd limit cycles around E0 in system (11),
we apply normal form theory to compute the focus values and then solve the
multivariate polynomial equations based on the focus values. Particularly,
we have
 b01k = 1
16[4a(2b11k − ab21k) − (a
2 + 2)2(a12k + 3b03k)

+ 4(a
2 + 2)(2b02k − aa21k − ab12k)]
, (22)

solved from the zeroth-order focus value V0k = 0, where

V0k = 1
32{
16 b01k − 4a(2b11k − ab21k) + (a
2 + 2)2(a12k + 3b03k)

− 4(a
2 + 2)(2b02k − aa21k − ab12k)]. (23)

Higher-order focus values are relatively complex, and we shall study them in
Section 3.
When we want to use focus values ViK in VK(r), i = 0, 1, 2, · · · , to study
limit cycles, we ﬁrst need to show Vk(r) ≡ 0, 1 ≤ k < K, or dr
dt = O(εK) in
(5). In order to prove this, we use the approximation of ﬁrst integrals, and
claim that if there exists an analytic function HK(x, y, ε) such that

(M −1Hy + εp) ∂HK
∂x + (−M −1Hx + εq) ∂HK
∂y = O(εK), (24)

then dr
dt = O(εK). This claim can be easily proved by using the closed contour
HK = h as the parameter to express the displacement function.
Usually, like that considered in [14, 24] the method of focus values is
used only to prove how many limit cycles around the equilibrium point that

9

system (3) can have. Combining it with the approximation of ﬁrst integrals,
we can obtain the maximal number of small limit cycles for parameters in
a neighborhood of critical conditions. Furthermore, if the focus values are
linear functions in parameters, we have a global result as follows.

Theorem 1 (Theorem 2.4.3 in [1]). Consider system (5) and assume Vk(r) ≡
0, 1 ≤ k < K. Suppose that for an integer m ≥ 1, each ViK, 0 ≤ i < m is
linear in δ, and further the following two conditions hold:

(i) rank
[ ∂(V0K ,··· ,Vm−1,K )
∂(δ1,··· ,δm) ] = m,

(ii) VK(r) ≡ 0, if ViK = 0, i = 0, 1, · · · , m − 1.

Then, for any given N > 0, there exist ε0 > 0 and a neighborhood V of
the origin such that system (3) has at most m − 1 limit cycles in V for
0 < |ε| < ε0, |δ| ≤ N. Moreover, m − 1 limit cycles can appear in an
arbitrary neighborhood of the origin for some values of (ε, δ).

The above theorem can be proved following the proof given in [1] with a
minor modiﬁcation. So the proof is omitted here.

3. Higher-order analysis leading to 11 limit cycles in system (11)

In this section, we focus on system (11) and show that it can have 11
limit cycles by using perturbations at least up to 7th order. In the following,
we will use the transformed system (11) with the simpliﬁed perturbations
given in (19) for the analysis.
In order to compute the focus values of this system, we ﬁrst shift the
equilibrium of system (11), (x, y) = (− a
2 + o(εn), − a2+2
4 + o(εn)) to the origin
and then use a computer algebra system and software package (e.g., the
Maple program in [19]) to obtain the focus values in terms of the parameters
a, aijk and bijk. We shall give detailed analysis for the ﬁrst few lower-order
focus values, and then summarize the results obtained from higher-order
analysis.
For convenience, deﬁne the vectors:

W 8
k = (V1k, V2k, · · · , V8k),
W 9
k = (V1k, V2k, · · · , V9k),
W 10
k = (V1k, V2k, · · · , V10k),

S8
k = (b10k, b20k, b11k, b02k, b30k, b21k, b12k, b03k)
,
S9
k = (b10k, b20k, b11k, b02k, b30k, b21k, b12k, b03k, a03k)
,
S10
k = (b10k, b20k, b11k, b02k, b30k, b21k, b12k, b03k, a03k, a12(3m)),
 (25)

10

where in S10
k , k = 7m for Case (A) and k = 13m for Case (B) (m ≥ 1, integer)
to be considered in Sections 3.4 and 3.5; and the determinants:

det8
k = det[ ∂W 8
k
∂S8
k
 ]
, det9
k = det[ ∂W 9
k
∂S9
k
 ]
, det10
k = det[ ∂W 10
k
∂S10
k
 ]
; (26)

and the functions:

F1 = − 373423834799904305184768
5 a36(a4−32)8 ,

F2 = 3013505105717894236809449177088
5 a45(a4−32)9 ,

F3 = − 57397219210893210316046010501071634432
a55(a4−32)10 ,

F4 = − 279638476916415193342384256641414767487418
a66(a4−32)11 ,

G1 = − 258237837
32 a9(a4−32) ,

G2 = 23476167
64 a11(a4−32)2 (57697a
4 − 35728a
2 − 88704),

G3 = − 23476167
1024 a13(a4−32)3 (2304313595a
8−1702233920a
6−11829269248a
4

− 39211065344a
2 + 8642101248),

G4 = − 75246080
a10(a4−32) ,

G5 = 9405760
3 a12(a4−32)2 (75767a
4 − 46944a
2 − 96768),

G6 = − 180880
3 a14(a4−32)3 (11681524055a
8 − 8555309984a
6 − 56944147200a
4

− 204210659328a
2 + 30640177152),

G7 = 2006968901247765
2883584 a11(a4−32) ,

G8 = − 154382223172905
2883584 a13(a4−32)2 (48667a
4 − 30160a
2 − 52416),

G9 = 66163809931245
46137344 a15(a4−32)3 (6314158847a
8 − 4591849024a
6

− 29599122432a
4 − 112639700992a
2 + 11915624448), (27)
Note that Fi ̸= 0, i = 1, 2, 3, and Gi ̸= 0, i = 1, 2, . . . , 9, since a
4 −32 > 0 for
a < −2−5/4.

3.1. ε- and ε2-order analysis
The ε-order focus values V11, V21, · · · , V111 are obtained by using the al-
gorithm and Maple program developed in [19]. Their expressions are lengthy,

11

and here we only present the ﬁrst one for brevity,

V11 = − 1
64a(a4−32) {
6912b101 − 5760a b201
+16(a
4 − 36a
2 + 40) b111 + 48a(a
4 + 36a
2 + 160) b021
+3456a
2 b301 − 24a(a
4 − 12a
2 + 40) b211
−16(3a
6 + 68a
4 + 300a
2 + 20) b121
−24a(3a
6 + 65a
4 + 300a
2 + 224) b031
+27(a
2 + 2)(7a
6 + 82a
4 + 320a
2 + 128) a031
+8a(24a
6 + 223a
4 + 1140a
2 + 1180) a121
+8(21a
6 − 73a
4 + 480a
2 + 320) a211}
.
 (28)

It is noted that all Vi1’s are linear polynomials in aij1 and bij1. It can be
shown that det8
1 = F1 ̸= 0, det9
1 = F2 ̸= 0, det10
1 = 0. (29)

In fact, with the solution of S8
1 solved from W 8
1 = 0, we obtain

V91 = G1 a031, V101 = G2 a031, V111 = G3 a031, (30)

where Gi’s are given in (27). Noticing G1 ̸= 0 for a < −25/4, we have V91 ̸= 0
if a031 ̸= 0. Moreover, det8
1 ̸= 0 and (23) indicate that perturbing W 8
1 and
V01 around the solutions S8
1 and b011 (see (22)) does yield 9 small limit cycles
around the equilibrium E0.
It is seen from (30) that V91 = V101 = V111 = 0 for a031 = 0. For convenience,
deﬁne the critical condition S
8
1c, satisfying (22), W 8
1 = 0 and a031 = 0, as

S
8
1c :
 



 b011 = C1 a121 − 9
8a
3a211,

a031 = b211 = 0, b121 = 7
2 a211, b021 = − 6 a121, b031 = 8
3 a121,

b111 = 9a a121 + 9
2 a211, b101 = C2 a121 + C3 a211,

b201 = C4 a121 + C5 a211, b301 = C6 a121 + C7 a211,
 (31)

where Ci’s are given in Appendix A.
We have the following result.

Theorem 2. The equilibrium E0 of system (11) is a center up to ε-order, i.e.
all ε-order focus values vanish if and only if the condition S
8
1c holds. Further-
more, there exist at most 9 small limit cycles around E0 for all parameters
aij1 and bij1, and 9 small limit cycles can be obtained for some parameter
values near S
8
1c.
 12

Proof. The existence of 9 small limit cycles has been shown under the solution
S8
1 with a031 ̸= 0 and det8
1 ̸= 0. It is obvious that the critical condition S
8
1c is
necessary for all ε-order focus values to vanish since Vi1 = 0, 0 ≤ i ≤ 11 under
this condition. To prove suﬃciency, under the critical condition S
8
1c, we use
(24) to obtain the following ε-order approximation of the ﬁrst integral,

H1(x, y, ε) = f1 + εf11
f2 + εf21 , (32)

where f1 and f2 are given in (13), f11 = a121r1+a211r2 and f21 = a121r3+a211r4
with

r1 = − 1
48 [
a
2(3a
2 + 4)(5 + 2y + 2x
2 + x
4) + 220 − 192ax + 280y
+120x
2 − 64y2 + 128ax
3 + 64x
2y + 76x
4]
,

r2 = − 1
8 a(5a
2 − 4) + 5x − 1
8a(a
2 − 4)(2y + 2x
2 + x
4) + 2xy − 2x
3,

r3 = 1
192 [
a
2(3a
2+4)(4a−15x+10xy+10x
3) + 304a + 16a
3 − 180x

− 40(
16ay−8ax
2+5xy−23x
3−8xy2+16ax
4+8x
3y)],

r4 = a2
8 (a
2−1)−a( 15
32a
2+ 5
8)x+ 5
2x
2( 3
2 +y−x
2)+ 5
16a(a
2 −4)x(y+x
2).
 (33)

This implies that setting the ﬁrst 10 focus values Vi1 = 0, i = 0, · · · , 9 yields
Vi1 = 0 for all i ≥ 10. Moreover, due to that all Vi1 are linear in all parameters
aij1 and bij1, by Theorem 1 at most 9 small limit cycles can be obtained for
this case. The proof is complete.

Now suppose the condition S
8
1c holds and so all ε-order focus values vanish,
we then need to use the ε2-order focus values to study bifurcation of limit
cycles. With an almost exact same procedure as that used in the ε-order
analysis, we can ﬁnd a solution S8
2 such that W 8
2 = 0, and then

V92 = G1 a032, V102 = G2 a032, V112 = G3 a032, det8
2 = F1 ̸= 0, (34)

where F1 and Gi’s are given in (27). Note that the above equations are
exactly the same as those given in (29) and (30), if we replace k = 1 by k = 2
in (29) and (30). This clearly shows that there can exist 9 limit cycles around
the equilibrium E0 when all ε-order focus values vanish. It is also noted that
all Vi2 are linear polynomials in aij2 and bij2.
Similarly, we see that setting a032 = 0 in (34) yields V92 = V102 = V112 = 0,
implying that the solution S8
2 with a032 = 0 and b012 given in (22) deﬁnes
a necessary condition for all ε2-order focus values to vanish. This critical

13

condition is given below:

S
8
2c :
 



 b012 = 9
64 a
4a
2
211 − 9
8 a
3a212 + C1a122 + C8a121a211 + C9a
2
121,

a032 = 0, b032 = 8
3 a122 + 5 a
2
121, b212 = a
2 a121(5a a121 − 9a211),

b122 = 7
2 a212 − 1
4 a121(31a a121 − 45a211),

b102 = C2 a122 + C3 a212 + C10 a
2
121 + C11 a
2
211 + C12 a121a211,

b202 = C4 a122 + C5 a212 + C13 a
2
121 + C14 a
2
211 + C15 a121a211,

b112 = 9a a122 + 9
2 a212 + 9a3
32 a
2
211 + C16 a
2
121 + C17 a121a211,

b022 = − 6a122 + C18 a
2
121 + C19 a121a211,

b302 = C6 a122 + C7 a212 + C20 a
2
121 + C21 a
2
211 + C22 a211a121,
 (35)

where Ci’s are given in Appendix A.
We have the following theorem.

Theorem 3. Assume S
8
1c holds. The equilibrium E0 of system (11) is a
center up to ε2-order, if and only if S
8
2c holds. Furthermore, there exist at
most 9 small limit cycles around E0 for all parameters aij2 and bij2, and 9
small limit cycles exist for some parameter values near S
8
2c.

Proof. Similarly, we only need to prove suﬃciency. With S
8
1c and S
8
2c holding,
we can use (24) to ﬁnd the following ε2-order approximation of the ﬁrst
integral,
 H2(x, y, ε) = f1 + εf11 + ε2f12
f2 + εf21 + ε2f22 , (36)

where f11 and f21 are given in H1(x, y, ε) (see Eq. 32), and

f21 = a122r1 + a212r2 + a
2
121s1 + a
2
211s2 + a121a211s3,
f22 = a122r3 + a212r4 + a
2
121s4 + a
2
211s5 + a121a211s6,

in which ri, i = 1, 2, 3, 4 are given in (33), and si, i = 1, 2, . . . , 8, are listed
in Appendix B.
The existence of 9 small limit cycles is easily seen from V92 ̸= 0 and det8
2 ̸= 0
when a032 ̸= 0 under the critical condition S
8
2c. On the other hand, the above
results show that setting Vi2, 0 ≤ i ≤ 9 results in Vi2 = 0 for all i ≥ 10.
Further, all Vi2’s are linear in aij2 and bij2, and S
8
2c is the unique solution of
Vi2 = 0, 0 ≤ i ≤ 9. Then by Theorem 1, at most 9 small limit cycles can be
obtained around E0 for all parameters aij2 and bij2.

14

3.2. ε3-order analysis
In this section, we assume the critical condition {S
8
1c, S
8
2c}, which stands
for that both the critical conditions S
8
1c and S
8
2c hold, under which all ε-
and ε2-order focus values vanish. Thus, we use ε3-order focus values Vi3 to
study bifurcation of limit cycles around the equilibrium E0. With a similar
procedure, but for this order, we solve 9 equations W 9
3 = 0 to obtain the
solution S9
3 for which

V103 = G4 a
3
121, V113 = G5 a
3
121, V123 = G6 a
3
121, det9
3 = F2 ̸= 0, (37)

where F2 and Gi’s are given in (27). Note that for this order, there is one
more independent coeﬃcient a033 in S9
3 for solving W 9
3 = 0, compared to
the solutions S8
1 and S8
2 which have only 8 independent coeﬃcients to be
used for solving the ﬁrst 8 focus value equations. The equations in (37)
show that when all ε- and ε2-order focus values vanish, the ε3-order focus
values can have solutions such that Vi3 = 0, i = 0, 1, · · · , 9 but V103 ̸= 0, as
well as det9
3 ̸= 0, implying that 10 small limit cycles can bifurcate from the
equilibrium E0.
Setting a121 = 0 in (37), we have V103 = V113 = V123 = 0, implying that
under the solution S9
3 with a121 = 0 and b013 given in (22), the equilibrium
E0 might be a center up to ε3 order. This critical condition is given by

S
9
3c :
 



 b013 = 9
32 a
4a211a212 − 9
8 a
3a213 + C1a123 + C8a122a211 + C23a
3
211,

a121 = a033 = 0, b033 = 8
3a123, b023 = − 6a123 + C19a122a211
b213 = − 9a
16 a211(8a122+a
2
211), b123 = 7
2a213 + 45
32 a211(8a122 +a
2
211),

b113 = 9a a123 + 9
2a213 + a211[ 9
16 a
3a212 + C17a122 + C24a
2
211]

b103 = C2a123 + C3a213 + a211[2C11a212 + C12a122 + C25a
2
211],

b203 = C4a123 + C5a213 + a211[2C14a212 + C15a122 + C26a
2
211]

b303 = C6a123 + C7a213 + a211[2C21a212 + C22a122 + C27a
2
211],
 (38)

under which the critical conditions S
8
1c and S
8
2c are simpliﬁed. Here, Ci’s are
given in Appendix A.
We have the following theorem.

Theorem 4. Let {S
8
1c, S
8
2c} hold. The equilibrium E0 of system (11) is a
center up to ε3-order, if and only if the condition S
9
3c holds. Furthermore,
there exist 10 small limit cycles around E0 for some parameter values of aij3
and bij3 near the critical value deﬁned by S
9
3c when V103 ̸= 0.

15

Proof. Similarly again, we only need to prove suﬃciency. Under the con-
dition {S
8
1c, S
8
2c, S
9
3c}, we obtain the following ε3-order approximation of ﬁrst
integral,

H3(x, y, ε) = f1 + εa211r1 + ε2(a122r1 + a212r2 + a
2
211s2) + ε3f31
f2 + εa211r4 + ε2(a122r3 + a212r4 + a
2
211s5) + ε3f32 , (39)

where
 f31 = a123r1 + a213r2 + a211(a122t1 + a212t2 + a
2
211t3),
f32 = a123r3 + a213r4 + a211(a122t4 + a212t5 + a
2
211t6),

in which ri, i = 1, 2, 3, 4 are given in (33), and s2, s5 and ti, i = 1, 2, . . . , 6
are listed in Appendix B. This implies that setting Vi3 = 0, 0 ≤ i ≤ 10 yields
Vi3 = 0 for all i ≥ 11. Then, there exist at most 10 small limit cycles for
this case. On the other hand, 10 small limit cycles exist since when a121 ̸= 0,
V101 ̸= 0 and det9
3 ̸= 0.

3.3. ε4–ε6-order analysis
The analyses for ε4-, ε5- and ε6-order are similar to that of ε1-, ε2- and
ε3-order, respectively.
Let {S
8
1c, S
8
2c, S
9
3c} hold. Following the same procedure used in the previous
sections, we can solve the equations W 8
4 = 0 to obtain a solution S8
4 such
that
 V94 = G1 a034, V104 = G2 a034, V114 = G3 a034, det8
4 = F1 ̸= 0, (40)

which has the exactly same form of the equations as those given in (30) and
(34), implying that perturbing the ε4-order focus values from the solution
S8
4 and b014 (see (22)) can yield 9 limit cycles around the equilibrium E0.
Similarly, the solution S8
4 and b014 with a034 = 0 yields a critical condition
S
8
4c, under which the equilibrium E0 is a center up to ε4 order.
Then let {S
8
1c, S
8
2c, S
9
3c, S
8
4c} hold. In the same line, we can solve the equa-
tions W 8
5 = 0 to obtain a solution S8
5 such that

V95 = G1 A035, V105 = G2 A035, V115 = G3 A035, det8
5 = F1 ̸= 0, (41)

where A035 = a035 + 1
48 a122 a211 (140 a122 + 35 a
2
211). (42)

16

This shows that perturbing the ε5-order focus values near the solution S8
5
and b015 given in (22) can also yield 9 limit cycles around the equilibrium E0.
It is easy to see that the solution of A035 = 0,

a035 = − 35
48 a122 a211 (4 a122 + a
2
211), (43)

yields V95 = V105 = V115 = 0. Now, we combine the solution S8
5, b015 and a035
to obtain the critical condition S
8
5c, under which the equilibrium E0 becomes
a center up to ε5 order.
The lengthy critical conditions S
8
4c and S
8
5c are omitted here for brevity.
Summarizing the above results leads to the following theorem.

Theorem 5. System (11) can have maximal 9 limit cycles around the equi-
librium E0 under the condition {S
8
1c, S
8
2c, S
9
3c} by perturbing the ε4-order fo-
cus values around the critical value S
8
4c; and under the critical condition
{S
8
1c, S
8
2c, S
9
3c, S
8
4c} by perturbing the ε5-order focus values near the critical
point S
8
5c. The equilibrium E0 becomes a center up to ε4 order under the
condition {S
8
1c, S
8
2c, S
9
3c, S
8
4c}, and a center up to ε5 order under the condition
{S
8
1c, S
8
2c, S
9
3c, S
8
4c, S
8
5c}.

Remark 2. The proof for the center conditions in Theorem 5 is similar to
that in proving Theorems 2, 3 and 4 by ﬁnding the ε4-order and ε5-order
approximations of the ﬁrst integrals. This is the major and tedious part. For
higher-order analysis, the proofs are similar. We omit the detailed proofs in
the following analysis for brevity.

Next, suppose the condition {S
8
1c, S
8
2c, S
9
3c, S
8
4c, S
8
5c} is satisﬁed, then all
εk, k = 1, 2, . . . , 5, order focus values vanish. Following a similar analysis as
that for ε3 order, we solve the equations W 9
6 = 0 to obtain a solution S9
6 such
that V106 = G4 a
2
122(
a122 + 9
8 a
2
211)
,

V116 = G5 a
2
122(
a122 + 9
8 a
2
211)
,

V126 = G6 a
2
122(
a122 + 9
8 a
2
211)
, det9
6 = F2 ̸= 0,
 (44)

which indeed shows the existence of 10 limit cycles around the equilibrium
E0, generated from perturbing the ε6-order focus values near the solution S9
6
under the condition {S
8
1c, S
8
2c, S
9
3c, S
8
4c, S
8
5c}. Moreover, when a122 = − 9
8 a
2
211
or a122 = 0, we have V106 = V116 = V126 = 0, indicating that the solution S9
6
with either a122 = − 9
8 a
2
211 or a122 = 0, plus b016 given by (22)|k=6, yields a
critical condition S
9a
6c (corresponding to the former) or S
9b
6c (corresponding to

17

the latter) under which all ε6-order focus values vanish. Thus, under the
critical condition {S
8
1c, S
8
2c, S
9
3c, S
8
4c, S
8
5c, S
9
6c} (S
9
6c equals either S
9a
6c or S
9b
6c ), the
equilibrium E0 becomes a center up to ε6 order.
We have the following theorem for this order.

Theorem 6. System (11) can have maximal 10 limit cycles bifurcating from
the equilibrium E0 under the condition {S
8
1c, S
8
2c, S
9
3c, S
8
4c, S
8
5c} by perturbing the
ε6-order focus values near the critical point S
9a
6c or S
9b
6c . Further, the equilib-
rium E0 becomes a center up to ε6 order under the condition {S
8
1c, S
8
2c, S
9
3c, S
8
4c,
S8
5c, S9
6c}, for which all εk-order (k = 1, 2, . . . , 6) focus values vanish.

Suppose the condition {S
8
1c, S
8
2c, S
9
3c, S
8
4c, S
8
5c, S
9
6c} holds. Then, all the εk-
order (k = 1, 2, . . . , 6) focus values vanish. We have two cases for higher-order
analysis, deﬁned as
 Case (A) {S
8
1c, S
8
2c, S
9
3c, S
8
4c, S
8
5c, S
9a
6c},

Case (B) {S
8
1c, S
8
2c, S
9
3c, S
8
4c, S
8
5c, S
9b
6c }. (45)

3.4. Higher-order analysis for Case (A)
First we consider Case (A), under which we will show that 11 limit cycles
can bifurcate from the equilibrium E0 based on the ε7-order focus values.

3.4.1. ε7-order analysis
Under the condition (A) deﬁned in (45) with a122 = − 9
8 a
2
211, we obtain

det10
7 = F3 a
4
211, det11
7 = F4 a
10
211, (46)

which shows that det10
7 ̸= 0 and det11
7 ̸= 0 when a211 ̸= 0, implying that we
may have solutions such that the ﬁrst ten focus values vanish but V117 ̸= 0
and so 11 small limit cycles may be obtained. Indeed, we can solve the ﬁrst
ten focus values equations: W 10
k = 0 to obtain a solution S10
7 such that

V117 = G7 a
7
211, V127 = G8 a
7
211, V137 = G9 a
7
211, (47)

which clearly shows that V117 ̸= 0 if a211 ̸= 0. In addition, due to det10
7 ̸= 0
when a211 ̸= 0, implying that 11 small limit cycles exist.
Letting a211 = 0, we have V117 = V127 = V137 = 0, leading to a critical
condition S
10
7c, deﬁned by
 18

S
10
7c :
 



 b017 = C1a127− 9
8 a
3a217 +C8C28+ 9
32 a
4C29+C23C30,

a211 = a123 = a037 = 0, b037 = 8
3 a127,

b027 = −6a127 + C19C28, b217 = − 9a
16 (8C28 + C30),

b127 = 7
2 a217 + 45
32 (8C28 + C30),

b107 = C2a127 + C3a217 + 2C11C29 + C12C28 + C25C30,

b207 = C4a127 + C5a217 + 2C14C29 + C15C28 + C26C30,

b117 = 9a a127 + 9
2 a217 + 9a3
16 C29 + C17C28 + C24C30,

b307 = C6a127 + C7a217 + 2C21C29 + C22C28 + C27C30,
 (48)

where Ci’s are given in Appendix A.
We have the following result.

Theorem 7. Let {S
8
1c, S
8
2c, S
9
3c, S
8
4c, S
8
5c, S
9a
6c} hold. The equilibrium E0 of (11)
becomes a center up to ε7 order under S
10
7c for which all ε7-order focus val-
ues vanish. Furthermore, there exist 11 small limit cycles around E0 for
parameter values of aij7 and bij7 near the critical point S
10
7c.

3.4.2. Higher-order analysis
For higher-order analysis (k ≥ 8), we ﬁrst brieﬂy list the results for a
few orders to see the patterns and then summarize the results in a table for
higher orders.
The analysis on εk (k = 8, 9, 10, 11) orders show the same pattern, giving
9 limit cycles for each order, as follows:

Order k :
(k = 8, 9, 10, 11) {S8
k, W 8
k },
 { V9k = G1 A03k, V10k = G2 A03k,

V11k = G3 A03k, det8
k = F1, (49)

where {Sm
k , W m
k } denotes the solution Sm
k solved from W m
k = 0, and

A038 = a038, A039 = a039,

A0310 = a0310 + 35
48 a124 a212 (4 a124 + a
2
212),

A0311 = a0311 + 35
48 [a125a212(8a124 + a
2
212) + a124a213(4a124 + 3a
2
212)]
.

This clearly shows that for each order of k = 8, 9, 10, 11, one can solve
A03k = 0 to get a unique solution for a03k under which (together with the

19

solutions Sm
k and b01k obtained in the previous orders and the current order)
the equilibrium E0 becomes a center up to that order.
When the equilibrium E0 is a center up to 11th order, as given in (49) we
obtain the following result for order 12:

Order 12 : {S9
12, W 9
12},
 



V1012 = G4 a
2
124(a124 + 9
8a
2
212),

V1112 = G5 a
2
124(a124 + 9
8a
2
212),

V1212 = G6 a
2
124(a124 + 9
8a
2
212), det9
12 = F2,
 (50)

which has the exactly the same pattern as order 6, shown in (44), indicating
that 10 limit cycles can be obtained from this order, and there are two
solutions from the equations V1012 = V1112 = V1212 = 0: a124 = − 9
8a
2
212 and
a124 = 0, which are again similar to that as in order 6. When a124 = 0, it will
be shown in Section 4.7 that it yields the same pattern as that for Case (B)
in higher orders. So in this section, we choose a124 = − 9
8 a
2
212, like we chose
a122 = − 9
8 a
2
212 in order 6 to obtain the center condition.
Let a124 = − 9
8 a
2
212, under which (together with the solutions obtained from
previous orders and this order) the equilibrium E0 becomes a center up to
ε12 order. Then, we have the result for ε13 order:

Order 13 : {S9
13, W 9
13},
 



V1013 = 81
64G4 a
4
212(a125 + 9
4 a212a213)
,

V1113 = 81
64G5 a
4
212(a125 + 9
4 a212a213)
,

V1213 = 81
64G6 a
4
212(a125 + 9
4 a212a213)
, det9
13 = F2,
(51)
which shows that perturbing ε13-order focus values can also yield 10 small
limit cycles around the equilibrium E0. It can be seen from (51) that either
a212 = 0 or a125 = − 9
4 a212a213 leads to the equilibrium E0 being a center.
However, it can be shown that setting a212 = 0 at this order will not yield 11
small limit cycles at the next order though it will resume the same pattern
at higher orders.
So let a125 = − 9
4 a212a213. Then, we obtain the following result for ε14

order:

Order 14 : {S10
14, W 10
14 },
 {V1114 = G7 a
7
212, V1214 = G8 a
7
212,

V1314 = G9 a
7
212, det10
14 = F3 ̸= 0, (52)

which shows that perturbing ε14-order focus values can yield 11 limit cycles
around the equilibrium E0, and setting a212 = 0 leads to E0 being a center up
to ε14 order. It has been noted that choosing a212 = 0 at order 13 or 14 makes

20

diﬀerences. More precisely, as shown in Table 1, if taking a125 = − 9
4a212a213 at
order 13, we have small limit cycles 11, 9, 9, 9, 9 for the orders 14–18; while
if taking a212 = 0 at order 13, then the limit cycles obtained for the orders
14–18 are 9, 10, 9, 9, 10, and then the two diﬀerent choices merge into the
same pattern from order 19. Note that the choice a212 = 0 at order 13 does
not yield 11 small limit cycles at order 14, but gives two more 10 small limit
cycles at orders 15 and 18. However, it returns to the general pattern at
order 19. So we treat a212 = 0 as a special case of the case a125 = − 9
4a212a213.
Summarizing the above results we have the following pattern: 11 limit
cycles are obtained from ε7 order, then 9 limit cycles from four consecutive
εk orders (k = 8, 9, 10, 11), and then 10 limit cycles from two consecutive εk

orders (k = 12, 13), and ﬁnally return to 11 limit cycles at ε14 order. This
pattern, starting from order 8, four 9 limit cycles, followed by two 10 limit
cycles, and then 11 limit cycle, has been veriﬁed up to ε35 order. We call
this as 94-102-111 generic pattern, and the corresponding solution (or center
condition) is called generic solution (or generic center condition). By generic
we mean that one should always choose a non-zero solution (if it exists) when
one solves the center conditions at each order. Other types of solutions are
called non-generic. For example, as discussed above, if choosing the non-
generic solution a212 = 0 at order 13, then 11 limit cycles will be missed
at order 14 but the solution procedure will return to the generic 94-102-111

pattern at order 19. However, it should be noted that a non-generic solution
in Case (A) does not always lead to the generic 94-102-111 pattern. For
instance, choosing the non-generic solution a124 = 0 at order 12 will generate
solutions in the form of generic patter of Case (B) at a higher order, as shown
in the next section.

Remark 3. It has been observed from the above analysis, the values of the
parameter a in the Hamiltonian function does not aﬀect the number of limit
cycles. In other words, a can not be used to increase the number of bifurcating
limit cycles. Thus, to simply the computations in higher order analysis, we
set a = − 3 in higher-order (k ≥ 15) computations, which greatly simplify
the computations.

We summarize the results of Case (A) in Table 1, where k is the order of εk

focus values, (Sm
k , W m
k ) represents the solution Sm
k solved from W m
k = 0, and
LC denotes limit cycles around the equilibrium E0 obtained by perturbing
the εk-order focus values. The “Condition for Center” in each row only lists
the condition for the current row, which assumes that the conditions in the
previous rows hold. For example, when k = 4, S
8
4c only gives the center

21

condition for k = 4, which should be combined with the conditions given
in the previous rows: S
8
1c, S
8
2c and S
9
3c to get a complete center condition
{S
8
1c, S
8
2c, S
9
3c, S
8
4c}. Note that the critical condition S
8
kc contains the solutions
S8
k, the b01k given in (22) and a particular coeﬃcient. For example, S
8
2c =
{S8
2, b012, a032}, S
9
3c = {S9
3, b013, a121}, and S
10
7c = {S10
7 , b017, a211}, etc. The
solutions of these key coeﬃcients are given below.

9 LC : k = 1, 2, 4, 8, 9 a03k = 0
k = 5 a035 = − 35
48 a122a211(4a122 + a
2
211)
k = 10 a0310 = − 35
48 a124a212(4a124 + a
2
212)
k = 11 a0311 = − 35
48 [a212a125(8a124 + a
2
212)
+a213a124(4a124 + 3a
2
212)]

k = 15 a0315 = − 735
256 a
5
213
k = 16 a0316 = 35
768 a
3
213(128a127 − 27a214a213)
k = 17 a0317 = − 35
768 a213[
32a127(2a127 − 3a214a213)
−a
2
213(128a128+54a
2
214−27a215a213)]

k = 18 a0318 = 35
6 a
3
213a129 − 35
24a213a128(4a127 − 3a214a213)
− 35
48 a127[a214(4a127 +3a214a213)−6a
2
213a215]

+ 3
4096 a
2
213[1120a214(a
2
214 + 6a215a213)
+3a
2
213(2269a
2
213 − 560a216)]

k = 22 a0322 = 35
768 a
3
214(128a1210 −486a
2
215−27a216a214)
k = 23 a0323 = 35
768 a
2
214[a214(128a1211 − 27a217a214)
+a215(384a1210 − 108a214a216 − 198a
2
215)]

k = 24, 25 a03k = · · ·
k = 29–32 a03k = · · ·

10 LC : k = 3 a121 = 0
k = 6 a122 = − 9
8 a
2
211
k = 12 a124 = − 9
8 a
2
212
k = 13 a125 = − 9
4 a213a212
k = 19 a127 = − 9
4 a213a214
k = 20 a128 = − 9
8 (a
2
214 + 2a215a213)
k = 26 a1210 = − 9
8 (a
2
215 + 2a216a214)
k = 27 a1211 = − 9
4 (a217a214 + a216a215)
k = 33 a1213 = − 9
4 (a218a215 + a217a216)
k = 34 a1214 = − 9
8 (a
2
217 + 2a219a215 + 2a218a216)

11 LC : k = 7m
m = 1–5 a21m = 0
 22

where ‘· · · ’ represents the omitted lengthy expressions for brevity. In ad-
dition, in Table 1, the blue and red colors denote the solutions and center
conditions corresponding to the 10 and 11 small limit cycle, respectively.

Table 1: Bifurcation of limit cycles for generic Case (A)

k (Sm
k , W m
k ) No. of LC Condition for Center
1,2 (S8
k, W 8
k ) 9 S
8
kc
3 (S9
3 , W 9
3 ) 10 S
9
3c
4,5 (S8
k, W 8
k ) 9 S
8
kc
6 (S9
6 , W 9
6 ) 10 S
9
6c
7 (S10
7 , W 10
7 ) 11 S
10
7c

8–11 (S8
k, W 8
k ) 9 S
8
kc
12,13 (S9
12, W 9
12) 10 S
9
kc
14 (S10
14 , W 10
14 ) 11 S
10
14c

15–18 (S8
15, W 8
15) 9 S
8
kc
19,20 (S8
19, W 9
19) 10 S
9
kc
21 (S10
21 , W 10
21 ) 11 S
10
21c

22–25 (S8
22, W 8
22) 9 S
8
kc
26,27 (S9
26, W 9
26) 10 S
9
kc
28 (S10
28 , W 10
28 ) 11 S
10
28c

29–32 (S8
k, W 8
k ) 9 S
8
kc
33,34 (S9
33, W 9
33) 10 S
9
kc
35 (S10
35 , W 10
35 ) 11 S
10
35c

3.5. Higher-order analysis for Case (B)
We now turn to Case (B) for which we choose a122 = 0 at ε6 order. Thus,
the results starting from ε6 order are diﬀerent from those given in Table 1.
Now under the condition a122 = 0, together with the conditions obtained in
previous orders, the equilibrium E0 becomes a center up to ε6 order. Then
for ε7-order focus values we solve W 8
7 = 0 to obtain S8
7 and then

V97 = G1 A037, V107 = G2 A037, V117 = G3 A037, det8
7 = F1,

where

A037 = a037 + 35
768 a211[a(a
2−4)a123a
3
211 +16a124a
2
211 +16a123(4a123+3a212a211)]
,

23

which shows that for Case (B) only 9 small limit cycles can be obtained from
ε7-order. Then, solving A037 = 0 gives a unique solution for a037, under which,
together with the conditions obtained in the previous orders as well as S8
7
and b017, the equilibrium E0 becomes a center up to ε7 order.
Next, the ε8-order analysis shows that 10 limit cycles can be obtained
by solving W 9
8 = 0 to have the solution S9
8, under which higher-order focus
values become

V108 = 9
8G4a
2
211a
2
123, V118 = 9
8 G5a
2
211a
2
123, V128 = 9
8 G6a
2
211a
2
123, det9
8 = F2.
(53)
This clearly indicates that either a211 = 0 or a123 = 0, together with b018, leads
to the equilibrium E0 being a center up to ε8 order. If taking a211 = 0, then
we again obtain 10 small limit cycles from ε9 order by solving W 9
9 = 0 to
obtain the solution S9
9 and

V109 = G4 a
3
123, V119 = G5 a
3
123, V129 = G6 a
3
123, det9
9 = F2.

Thus, for the equilibrium E0 being a center up to ε9 order, a123 must be taken
zero (with b019), yielding the same result as that generated from Case (A) at
order 9 (and so the result at order 8 also becomes same). In other words,
choosing the non-generic solution a211 = 0 at order 8 makes the higher-order
solutions (k ≥ 9) follow the generic pattern of Case (A).
Now we consider the choice a123 = 0 at ε8 order. It can be shown that
under this condition only 9 limit cycles exist for ε9 order. Then for the ε10

order, we solve W 9
10 = 0 to obtain the solution S9
10 and then get

V1010 = 9
8 G4 a
2
211(
a
2
124 − 5
16 a
4
211a124 + 429
40960 a
8
211),

V1110 = 9
8 G5 a
2
211(
a
2
124 − 5
16 a
4
211a124 + 429
40960 a
8
211),

V1210 = 9
8 G6 a
2
211(
a
2
124 − 5
16 a
4
211a124 + 429
40960 a
8
211), det9
10 = F2,
 (54)

which gives two solutions leading to a center at E0, one of them is a211 = 0,
which yields the same solution as that obtained in Case (A) at order 10.
Thus, choosing the non-generic solution a211 = 0 at this order leads to the
generic pattern of Case (A) starting from ε11 order (i.e., for k ≥ 11). The
second solution, given by

a124 = 1
64 (10 ± 1
10 √5710
) a
4
211, (55)

is a generic solution for Case (B), diﬀerent from the generic pattern of Case
(A). Then, following a similar computation procedure as that used in Case

24

(A), we obtain the generic solutions up to ε39 order. The results are given in
Table 2, showing a 96-106-111 generic pattern, starting from order 14. The
notations used in this table are the same as that used in Table 1. For each
k, the key coeﬃcient used to obtain the center condition is give below.

9 LC : k = 7 a037 = − 35
768 a211[
64a
2
123 − a211(15a123a
2
211
−16a124a211 − 48a123a212)]

k = 9 a039 = · · ·
k = 14 a0314 = − 35
48 a
3
212a128
k = 15 a0315 = − 35
48 a
2
212(a129a212 + 3a128a213)
k = 16 a0316 = − 35
768 a212[
48a
2
213a128 + a212(16a1210a212
+48a129a213 + 48a128a214 − 15a128a
2
212)]

k = 17–19 a03k = · · ·
k = 27–32 a03k = · · ·

10 LC : k = 8 a123 = 0

k = 10 a124 = 100±√5710
640 a
4
211
k = 11 a125 = 100±√5710
10240 a
3
211[
64a212 + a(a
2 − 4)a
2
211]

k = 12 a126 = · · ·

k = 20 a128 = 100±√5710
640 a
4
212
k = 21 a129 = 100±√5710
160 a
3
212a213
k = 22–25 a12(k−12) = · · ·

k = 33 a1215 = − 100±√5710
10240 a213[a
2
213(15a
2
213 − 64a216)
−64a214(a
2
214 + 3a213a215)]

k = 34–38 a12(k−18) = · · ·

11 LC : k = 13m
m = 1, 2, 3 a21m = 0

3.6. Non-generic solutions
Couple of non-generic solutions have been discussed in Case (B) (see
Section 3.5), showing that setting a211 = 0 at order 8 or 10 (see Eqns. (53) and
(54)) leads to the 94-102-111 generic pattern of Case (A) for orders greater
than 10 or 11. These two examples give a route from Case (B) to Case
(A). In this section, we present several more non-generic solutions to show
other possibilities that they eventually return to either the 94-102-111 generic

25

Table 2: Bifurcation of limit cycles for generic Case (B)

k (Sm
k , W m
k ) LC Condition for Center
7 (S8
7, W 8
7 ) 9 S
8
7c
8 (S9
8, W 9
8 ) 10 S
9
8c
9 (S8
9, W 8
9 ) 9 S
8
9c
10–12 (S9
10, W 9
10) 10 S
9
kc
13 (S10
13, W 10
13 ) 11 S
10
13c

14–19 (S8
k, W 8
k ) 9 S
8
kc
20–25 (S9
20, W 9
20) 10 S
9
kc
26 (S10
26, W 10
26 ) 11 S
10
26c

27–32 (S8
k, W 8
k ) 9 S
8
kc
33–38 (S9
k, W 9
k ) 10 S
9
kc
39 (S10
26, W 10
26 ) 11 S
10
39c

pattern of Case (A) or 96-106-111 generic pattern of Case (B). Other cases can
be similarly discussed. Since the discussions for diﬀerent cases are similar,
we will not give the details but list the cases below and summarize the results
in Table 3.

(A1) In Case (A), at order 13: a212 = 0, leading to Case (A).
(A2) In Case (A), at order 12: a124 = 0, leading to Case (B).
(B1) In Case (B), at order 11: a211 = 0, leading to Case (B).

For each k, the key coeﬃcient used to obtain the center condition is given
below.

Case (A1) k = 13 a212 = 0
k = 14 a0314 = − 35a125
48 [4a125a214 +a213(8a126+a
2
213)]

k = 16 a0316 = − 35
48 [a127a213(8a126 + a
2
213)
+a126a214(4a126 + 3a
2
213)]

k = 17 a0317 = − 35
48 a128a213(a
2
213 + 8a126)
− 35
48 a127(4a213a127+8a214a126+3a214a
2
213)
− 35
48 a126(3a
2
214a213+4a126a215+3a215a
2
213)
k = 15 a125 = 0
k = 18 a126 = − 9
8 a
2
213
 26

Case (B1) k = 11 a211 = 0
k = 12 a0312 = − 35
48 a212(a126a
2
212 +3a125a212a213 +4a
2
125)
k = 13, 15, 17 a03k = · · ·
k = 14, 16, 18 a12(k/2−2) = 0

Case (A2) k = 13 a0313 = − 35
48 a212[
a127a
2
212+a126(3a213a212 +8a125)]

+ 35
768a125(15a
4
212 − 48a
2
212a214
−48a212a
2
213 − 64a125a213)
k = 15, 17 a03k = · · ·
k = 12, 14, 16, 18 a12(k/2−2) = 0

Table 3: Non-generic solutions

Case k (Sm
k , W m
k ) LC Condition for Center
13,15 (S9
13, W 9
13) 10 S
9
kc
(A1) 14,16,17 (S8
14, W 8
14) 9 S
8
kc
18 (S9
k, W 9
k ) 10 S
9
18c =⇒ generic Case (A)

11,14,16 (S9
11, W 9
11) 10 S
9
kc
(B1) 12,13,15,17 (S8
k, W 8
k ) 9 S
8
kc
18 (S9
18, W 9
18) 10 S
9
18c =⇒ generic Case (B)

12,14,16 (S9
k, W 9
k ) 10 S
9
kc
(A2) 13,15,17 (S8
k, W 8
k ) 9 S
8
kc
18 (S9
18, W 9
18) 10 S
9
18c =⇒ generic Case (B)

Therefore, there are four possible routes for the non-generic solutions:
from Case (A) to Case (A) or Case (B); and from Case (B) to Case (A) or
Case (B).

3.7. Summary of this section
Summarizing the results obtained in sections 3.4, 3.5 and 3.6, we have
the following theorem.

Theorem 8. For system (11), based on the higher-order focus values, there
exist two generic patterns: One is 94-102-111 pattern starting from order
8 with four consecutive 9 limit cycles, followed by two consecutive 10 limit
cycles, and then one 11 limit cycles up to ε35 order; and the other is 96-
106-111 pattern, starting from order 14 with six consecutive 9 limit cycles,

27

followed by six consecutive 10 limit cycles, and then one 11 limit cycles up to
ε39 order. Other non-generic solutions deviate from the current pattern for
certain orders and eventually return to either the 94-102-111 pattern or the
96-106-111 pattern.

Finally, we propose a conjecture on the number of limit cycles around E0
for system (11).

Conjecture. For the perturbed system (11), the maximal number of small
limit cycles which can bifurcate from the equilibrium E0 is 11,

4. Conclusion

In this paper, we have applied high-order focus value computation to
prove that system (11) can have 11 limit cycles around the equilibrium of
(11), obtained by perturbing at least ε7-order focus values. Moreover, no
more than 11 limit cycles can be found up to ε39-order analysis. It is be-
lieved that system (11) can have maximal 11 small limit cycles around the
equilibrium.

Acknowledgment

This work was supported by the National Natural Science Foundation
of China (NSFC No. 11501370), and the Engineering Research Council of
Canada (NSERC No. R2686A02).

Appendix A

The coeﬃcients Ci’s in (31), (35) and (38) are given below.

C1 = − 3
16 (3a
4 + 4a
2 + 44) C2 = − a
48 (3a
4 + 12a
2 + 116)

C3 = − 1
8(a
4 + 2a
2 + 5) C4 = − 1
16 (9a
4 − 20a
2 + 172)

C5 = − 3 a
8 (3a
2 − 8) C6 = − a
12 (a
2 − 120)

C7 = − 1
8(3a
2 − 80) C8 = 3
128 a(7a
4 + 68a
2 − 900)

C9 = 1
64(3a
6+40a
4−860a
2−1600) C10 = − a
576 (303a
4 + 1596a
2 + 8096)

C11 = − a
64(55a
2 − 256) C12 = − 1
384 (569a
4 − 1660a
2 + 1420)

C13 = 1
192 (21a
6+80a
4−2996a
2−9040) C14 = 3
64 (7a
4 + 8a
2 + 160)

C15 = a
128 (49a
4 + 220a
2 − 380) C16 = a
32 (9a
4 + 36a
2 − 172)

C17 = 3
64(15a
4 + 28a
2 − 916) C18 = − 1
16 (3a
4 + 4a
2 + 340)

28

C19 = − 3a
8 (a
2 − 16) C20 = a
96 (45a
4 + 266a
2 − 644)

C21 = a
32 (41a
2 + 72) C22 = 1
192 (303a
4 + 1728a
2 − 3620)

C23 = − 9
512 a(a
4 + 12a
2 + 200) C24 = − 9
256 (a
4 + 160)

C25 = − 1
512 (70a
6−471a
4+128a
2−300) C26 = − 9
512 a(a
4 − 108a
2 + 696)

C27 = 3
256 (21a
4 + 58a
2 − 1880) C28 = a125a212 + a124a213
C29 = a215a212 + a214a213 C30 = 3a213a
2
212

Appendix B

The coeﬃcients si’s involved in H2 (see Eq. (36)) and ti’s involved in H3
(see Eq. (39)) are given as follows.

s1 = 1
3072 a
6(3a
2 + 16)(10 + 4y + 4x
2 + 3x
4) − 1
192(2850 + 1824a
2 − 85a
4)

+ a
18 (6a
2−319)x− 1
288(5902+1568a
2+45a
4)y − a
9 (53 + 10x
2)xy + 13
6 y2

− 1
72 a
2(3a
2 + 4)y(y − x
2) − 1
96 (1074 + 200a
2 + 45a
4)x
2 − 29
18 x
2y − 2
9 y3

+ a
36 (12 − 4a
2 + 3a
4)x
3 − 1
1152 (6746 + 3140a
2 + 91a
4 + 3a
6)x
4 + 2
3x
2y2

s2 = 1
128 a
2(24 − 10a
2 + 5a
4) − 1
64 (1120 − 24a
2 + 2a
4 − a
6)(y + x
2) − 1
2 x
2y

+ a
16 (4+5a
2)x− 25
4 x
2− a
256 (a
2−4)x[32(y−x
2)−3a
3x
3]− 1
8(73−2a
2)x
4

s3 = 1
384 a(−4716 + 376a
2 + 25a
4 + 15a
6) − 1
96 (2260 − 164a
2 − 15a
4)x

+ 1
192 a
5(5 + 3a
2)(y + x
2) − 1
12 a(a
2 − 4)y(y − x
2) − 2
3xy2 + 2x
3y

− 1
48 [a(1151 + 10a
2)y − a(1511 + 40a
2)x
2 + (100 − 4a
2 − 3a
4)xy

+(140 − 76a
2 + 11a
4)x
3] − 1
768 a(10216 + 100a
2 − 2a
4 − 9a
6)x
4

s4 = 1
9216 a(96656 + 17952a
2 + 3640a
4 + 24a
6 + 9a
8)

− 5
4608 (2256 + 7272a
2 − 56a
4 + 6a
6 + 9a
8)x − 5
72a(224 + 8a
2 + 3a
4)y

− 5
144 a(642 − 8a
2 − 3a
4)x
2 − 5
1152 (368 − 1628a
2 − 92a
4 + 3a
6)xy

− 5
2 ay2 + 5
1152 (5272 + 86a
4 + 2964a
2 − 3a
6)x
3 − 275
36 ax
2y

+ 5
288 (372 + 4a
2 + 3a
4)xy2 − 5
144 a(140 + 12a
2 + 3a
4)x
4

− 5
288 (268 + 3a
4 + 4a
2)x
3y − 5
18 xy3 − 25
18ax
4y + 5
6x
3y2

s5 = 1
256 a(−16a
2 − 8a
4 + a
6 + 1120) + 5
256 (560 + 9a
4 − 2a
6 − 4a
2)x

− 5
64 a(20 − 11a
2)x
2 − 5
128 a
2(3a
2 + 4)x(y + x
2) + 175
8 xy + 265
16 x
3

+ 5
32 a(a
2 − 4)x
2(y − x
2) − 5
8x
3y
29

s6 = 1
768 a
2(540a
2+3904−8a
4+3a
6) − 5
1536 a(484−100a
2−23a
4+12a
6)x

− 5
12 a
2(a
2−1)y− 35
384 (244−4a
2−7a
4)x
2+ 5
768 a(5132+84a
2−13a
4)xy

− 5
768 a(−3756 − 76a
2 + 13a
4)x
3 + 5
192(380 + 3a
4 + 4a
2)x
2y

+ 5
48 a(a
3 − 4)xy(y − x
2) − 5
192 (11a
4 + 20a
2 + 12)x
4 − 5
6 x
2y2 + 5
2 x
4y.

t1 = 1
384 a(−4716 + 376a
2 + 25a
4 + 15a
6) − 1
96 (2260 − 164a
2 − 15a
4)x

+ 1
192 a
5(5 + 3a
2)(y + x
2) − 1
48a(1151 + 10a
2)y − 2
3xy2 + 2x
3y

− 1
48 a(1511+40a
2)x
2 + 1
48(100−4a
2−3a
4)xy − 1
12a(a
2 − 4)y(y − x
2)

+ 1
48 (140 − 76a
2 + 11a
4)x
3 + 1
768 a(−100a
2 − 10216 + 9a
6 + 2a
4)x
4

t2 = 1
64 a
2(24 − 10a
2 + 5a
4) − 1
32 (1120 − 24a
2 + 2a
4 − a
6)(y + x
2)

+ 1
8a(5a
2 + 4)x − 25
2 x
2 − 1
4a(a
2 − 4)x(y − x
2) − x
2y

− 1
128 (2336 − 64a
2 + 12a
4 − 3a
6)x
4

t3 = − 1
2048 a
5(20 + a
4)(5 + 2y + 2x
2 + 2x
4) − 1
128 a(550 − 343a
2)

− 1
256 (6800−24a
2−10a
4+5a
6)x − 3
64a(25a
2+34)y − 1
32a(45a
2+61)x
2

− 1
1024 a
4(2 − a
2)x(8y − 8x
2 + 3ax
3) − 3
16(50 − a
2)xy + 3
16 (80 − a
2)x
3

+ 1
32 a(a
2 − 4)x
2y − 1
64a(197 − 2a
2)x
4 + 1
4x
3y

t4 = 1
768 a
2(3904+540a
2−8a
4+3a
6) − 5
1536 a(484−100a
2−23a
4+12a
6)x

− 5
12 a
2(a
2 − 1)y − 35
384 (244 − 7a
4 − 4a
2)x
2

− 5
768 a(−5132 − 84a
2 + 13a
4)xy − 5
768 a(−3756 − 76a
2 + 13a
4)x
3

+ 5
192 (380 + 4a
2 + 3a
4)x
2y + 5
48 a(a
2 − 4)xy(y − x
2)

− 5
192 (12 + 20a
2 + 11a
4)x
4 − 5
6x
2y2 + 5
2x
4y

t5 = 1
128 a(1120 − 16a
2 − 8a
4 + a
6) + 5
128 (560 − 4a
2 + 9a
4 − 2a
6)x

+ 5
32 a(11a
2 − 20)x
2 − 5
64a
2(4 + 3a
2)x(y + x
2) + 175
4 xy

+ 265
8 x
3 + 5
16a(a
2 − 4)x
2(y − x
2) − 5
4x
3y

t6 = − 1
2048 a
2(2544−2336a
2+8a
4+3a
6) − 5
2048 a(2632+276a
2+3a
4−8a
6)x

+ 5
512 (1240 − 4a
2 − 41a
4 + 4a
6)x
2 + 5
1024 a(−1832 + 892a
2 + a
4)xy

+ 5
1024 a(−1368 + 696a
2 + a
4)x
3 − 5
256 a
2(3a
2 + 4)x
2(y − x
2)

+ 375
32 x
2y − 65
16x
4 − 5
128 a(a
2 − 4)x
3y + 5
16x
4y

30

References

[1] M. Han, Bifurcation theory of limit cycles, Science Press, Beijing, 2013.

[2] D. Hilbert, Mathematical problems, (M. Newton, Transl.) Bull. Amer.
Math. 8 (1902) 437–479.

[3] S. Shi, A concrete example of the existence of four limit cycles for plane
quadratic systems, Sci. Sinica, 23 (1980) 153–158.

[4] L. Chen, M. Wang, The relative position, and the number, of limit
cycles of a quadratic diﬀerential system, Acta. Math. Sinica, 22 (1979)
751–758.

[5] J. Li, Y. Liu, New results on the study of Zq-equivariant planar poly-
nomial vector ﬁelds, Qualitative Theory of Dynamical Systems, 9(1-2)
(2010) 167–219.

[6] C. Li, C. Liu, J. Yang, A cubic system with thirteen limit cycles, J. Diﬀ.
Eqns. 246 (2009) 3609–3619.

[7] V. I. Arnold, Geometric Methods in the Theory of Ordinary Diﬀerential
Equations, Springer-Verlag, New York, 1983.

[8] M. Han, Bifurcation of limit cycles of planar systems, Handbook of
Diﬀerential Equations, Ordinary Diﬀerential Equations, Vol. 3 (Eds. A.
Canada, P. Drabek and A. Fonda), Elsevier, 2006.

[9] Han M., Yu, P., Normal Forms, Melnikov Functions and Bifurcations of
Limit Cycles. Sringer-Verlag, New York, 2012.

[10] N. Bautin, On the number of limit cycles appearing from an equilibrium
point of the focus or center type under varying coeﬃcients, Matem. Sb.
30 (1952) 181–196.

[11] P. Yu, R. Corless, Symbolic computation of limit cycles associated with
Hilbert’s 16th problem, Communications in Nonlinear Science and Nu-
merical Simulation, 14(12) (2009) 4041–4056.

[12] N. Lloyd, J. Pearson, A cubic diﬀerential system with nine limit cycles,
Journal of Applied Analysis and Computation 2 (2012) 293–304.

[13] C. Chen, R. Corless, M. Maza, P. Yu, Y. Zhang, A modular regular
chains method and its application to dynamical systems, Int. J. Bifur-
cation and Chaos 23(9) (2013) 1350154 (21 pages).

31

[14] P. Yu, Y. Tian, Twelve limit cycles around a singular point in a pla-
nar cubic-degree polynomial system, Commun. Nonlinear Sci. Numer.
Simulat. 19 (2014) 2690–2705.

[15] J. Guckenhermer, P. Holmes, Nonlinear Oscillations, Dynamical Sys-
tems, and Bifurcations of Vector Fields (4th Ed.). Springer, New York,
1993.

[16] S. N. Chow, C. C. Li, D. Wang, Normal Forms and Bifurcation of Planar
Vector Fields. Cambridge University Press, Cambridge, 1994.

[17] Yuri A. Kuznetsov, Elements of Applied Bifurcation Theory (2nd Ed.).
Springer, New York, 1998.

[18] M. Gazor, P. Yu, Spectral sequences and parametric normal forms. J.
Diﬀ. Eqns. (2012) 252: 1003-1031.

[19] P. Yu, Computation of normal forms via a perturbation technique, J.
Sound and Vib. 211 (1) (1998) 19–38.

[20] P. Yu, A. Y. T. Leung, The simplest normal form of Hopf bifurcation.
Nonlinearity (2003) 16: 277-300.

[21] Y. Tian, P. Yu, An explicit recursive formula for computing the normal
form and center manifold of n-dimensional diﬀerential systems associ-
ated with Hopf bifurcation. Int. J. Bifur. Chaos (2013) 23: 1350104 (18
pages).

[22] Y. Tian, P. Yu, An explicit recursive formula for computing the normal
forms associated with semisimple cases. Commun Nonlinear Sci. Numer.
Simul. (2014) 19: 2294-2308.

[23] H. ˙Zo l¸adek, Eleven small limit cycles in a cubic vector ﬁeld, Nonlinearity
8 (1995) 843–860.

[24] P. Yu, M. Han, A study on ˙Zo l¸adek’s example, J. Appl. Anal. Comput.
1 (2011) 143–153.

[25] Y. Tian, P. Yu, Bifurcation of ten small-amplitude limit cycles by per-
turbing a quadratic Hamiltonian system with cubic polynomials, J. Diﬀ.
Eqns. 260 (2016) 971–990.
 32
