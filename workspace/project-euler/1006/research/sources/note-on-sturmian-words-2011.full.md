<!-- source: https://arxiv.org/pdf/1202.6175 | converted from PDF -->

This work has been submitted to the IEEE for possible publication. Copyright may be transferred

without notice, after which this version may no longer be accessible.arXiv:1202.6175v1  [cs.IT]  28 Feb 2012
Delay-limited Source and Channel Coding of

Quasi-Stationary Sources over Block Fading

Channels: Design and Scaling Laws

Roghayeh Joda
†∗ and Farshad Lahouti
†

†School of Electrical and Computer Engineering, University of Tehran, Iran

∗Department of Electrical and Computer Engineering, Polytechnic Institute of New

York University, USA

Email: [rjoda, lahouti]@ut.ac.ir, http://wmc.ut.ac.ir

Abstract

In this paper, delay-limited transmission of quasi-stationary sources over block fading channels are

considered. Considering distortion outage probability as the performance measure, two source and channel

coding schemes with power adaptive transmission are presented. The ﬁrst one is optimized for ﬁxed rate

transmission, and hence enjoys simplicity of implementation. The second one is a high performance scheme,

which also beneﬁts from optimized rate adaptation with respect to source and channel states. In high SNR

regime, the performance scaling laws in terms of outage distortion exponent and asymptotic outage distortion

gain are derived, where two schemes with ﬁxed transmission power and adaptive or optimized ﬁxed rates

are considered as benchmarks for comparisons. Various analytical and numerical results are provided which

demonstrate a superior performance for source and channel optimized rate and power adaptive scheme. It is

also observed that from a distortion outage perspective, the ﬁxed rate adaptive power scheme substantially

outperforms an adaptive rate ﬁxed power scheme for delay-limited transmission of quasi-stationary sources

over wireless block fading channels. The effect of the characteristics of the quasi-stationary source on

performance, and the implication of the results for transmission of stationary sources are also investigated.

Index Terms

Outage capacity, quasi-stationary source, outage distortion, source and channel coding, rate and power

adaptation.
 I. INTRODUCTION

Multimedia signals such as speech and video are usually quasi-stationary and their transmission

in real-time or streaming applications is subject to certain delay constraints. The delay limited

communications over a wireless block fading channel is studied from a channel coding perspective

in, e.g., [1], [2], where the performance is quantiﬁed in terms of channel outage probability, outage

capacity and delay-limited capacity. In this paper, we study the delay-limited transmission of a quasi-

stationary source over a block fading channel from the perspective of source and channel coding

designs and performance scaling laws.

The zero outage capacity region of the multiple access and the broadcast block fading channels,

respectively are studied in [2] and [3]. In [2], it is shown that the delay limited capacity of a single

user Rayleigh block fading channel is zero. In [1], [3] and [4], power adaptation for constant rate

transmission over point-to-point, broadcast and multiple access block fading channels is designed

for minimum outage probability. The outage performance of the relay block fading channel is

investigated in, e.g., [5]-[7].

The end to end mean distortion for transmission of a stationary source over a block fading channel

is considered in [8]-[13]. The performance is studied in terms of the (mean) distortion exponent or

the decay rate of the end to end mean distortion with (channel) signal to noise ratio (SNR) in high

SNR regime.

The transmission of a stationary source over a MIMO block fading channel is considered in

[14], where the distortion outage probability and the outage distortion exponent are considered as

performance measures. For constant power transmission, it is shown in [14] that separate source and

channel coding schemes with constant (optimized) or adaptive transmission rate essentially provide

the same distortion outage probability.

We consider the delay-limited transmission of a quasi-stationary source over a wireless block

fading channel. The assumption is that the channel state information is known at the transmitter.

The source and channel separation does not hold in this setting [15][16], however, for practical

reasons we are interested in exploring the designs that combine conventional high performance

source codes and channel codes in an optimized manner. Speciﬁcally, a framework for rate and/or

power adaptation using source and channel codes, that achieve the rate-distortion and the capacity in

a given state of source and channel, is presented. The applicable performance measures of interest,

as described in Section II, are the probability of distortion outage and the outage distortion exponent.

Under an average transmission power constraint, two designs are presented. The ﬁrst scheme devises

a channel optimized power adaptation to minimize the distortion outage probability for a given

optimized ﬁxed rate, and hence enjoys the simplicity of single rate transmission. The second scheme

1

formulates adaptation solutions for transmission power and source and channel coding rate such

that the distortion outage probability is minimized. As benchmarks, we consider two constant power

delay-limited communication schemes with channel optimized adaptive or ﬁxed rates.

The performance of the presented schemes are assessed and compared both analytically and

numerically. Speciﬁcally for large enough SNR, different scaling laws involving outage distortion

exponent and asymptotic outage distortion gain are derived. The analyses are mainly derived for

wireless block fading channels and are specialized to Rayleigh block fading channels in certain

cases. The results demonstrate the superior performance of the source and channel optimized rate

and power adaptive scheme. An interesting observation is that from a distortion outage perspective,

an adaptive power single rate scheme noticeably outperforms a rate adaptive scheme with constant

transmission power. This is the opposite of the observation made in [17] from the Shannon capacity

perspective. The effect of the statistics of quasi-stationary source on the performance of the presented

schemes is also investigated. In the marginal case of a stationary source, our studies reveal that a

ﬁxed optimized rate provides the same outage distortion as the optimized rate adaptation scheme,

either with adaptive or constant transmission power. The results shed light on proper cross-layer

design strategies for efﬁcient and reliable transmission of quasi-stationary sources over block fading

channels.

The paper is organized as follows. Following the preliminaries and the description of system

model in Section II, Section III presents the design based on ﬁxed source coding rate for minimized

distortion outage probability. Next, in Section IV, we present the adaptive rate and power source and

channel coding design. Finally performance evaluations and comparisons are presented in Section

V.
 II. SYSTEM MODEL

We consider the transmission of a quasi-stationary source over a block fading channel. Speciﬁcally,

the source is ﬁnite state quasi-stationary Gaussian with zero mean and variance σ2
s in a given block,

where s ∈ S : S = {1, 2, ..., Ns}[18]. The source state s from the set S is a discrete random

variable with the probability density function (pdf) P (s). The source coding rate in a block in state

s, is denoted by Rs bits per source sample. Hence, according to the distortion-rate function of a

Gaussian source [18][19], the instantaneous distortion in a block in state s is given by D = σ2
s 2
−2Rs.

We consider a point to point wireless block fading channel for transmitting the source information

to the destination. Let X, Y and Z, respectively indicate channel input, output and additive noise,

where Z is an i.i.d Gaussian noise ∼ N (0, 1). Therefore, we have Y = αX + Z, where α is

the multiplicative fading which is constant across one block and independently varies from one

2

block to another according to the continuous probability density function f (α). For a Rayleigh

fading channel, the channel gain |α|
2 is an exponentially distributed random variable, where we

here consider E[α] = 1.

The block diagram of the system is depicted in Fig. 1. We consider K source samples spanning

one source block coded into a ﬁnite index by the source encoder. This index is transmitted in N

channel uses spanning one fading block (bandwidth expansion ratio b = N
K , here b ∈ N). We assume

that K and N are large enough such that, over a given state of source and channel, the rate distortion

function of the quasi-stationary source and the instantaneous capacity of the block fading channel

may be achieved. The source coding rate Rs in bits per source sample and channel coding rate R

in bits per channel use are related by Rs = bR. The instantaneous capacity of the fading Gaussian

channel [1] over one block (in bits per channel use) is deﬁned as

C(α, γ) = 1
2 log2(1 + αγ). (1)

In case of a channel outage, in each state of the source and the channel (s, α), the instantaneous
distortion is equal to the variance of the source and the decoder reconstructs the mean of the source.

Whereas without channel outage, distortion is given by σ2
s 2
−2bR. Thus, the distortion at a given state

(s, α) is equal to
 D(σs, α, γ) =
 



σ2
s 2
−2bR if R ≤ C(α, γ)

σ2
s if R > C(α, γ), (2)

where C(α, γ) is given in (1). Let Dm be a nonnegative constant and represent the maximum

allowable distortion. The distortion outage probability evaluated at Dm is deﬁned as

PDout = Pr(D(σs, α, γ) > Dm), (3)

where γ = γ(σs, α) is the transmission power and we have the power constraint E[γ] ≤ ¯P .

The outage distortion exponent is deﬁned as [14]

∆OD = lim
¯P →∞−ln PDout
ln ¯P . (4)

Let ¯P1 and ¯P2 be the average powers transmitted to asymptotically achieve a speciﬁc distortion
outage probability by two different schemes. We deﬁne the asymptotic outage distortion gain as

follows GOD = 10 log10 ¯P2 − 10 log10 ¯P1. (5)

In the sequel, we also use the following mathematical deﬁnitions

[x]+ := max{x, 0} (6)

and E1(x) := ∫ ∞

x
 e−α

α dα, (7)

3

as well as the following two approximations (refer to (5.1.53) in [20])

E1(x) ∼= −Ec − ln(x) if x → 0 , (8)

where Ec = 0.5772156649 is the Euler constant and

ex ∼= 1 + x if x → 0. (9)

III. CHANNEL OPTIMIZED POWER ADAPTATION WITH FIXED RATE SOURCE AND CHANNEL

CODING

In this section, the aim is to ﬁnd the optimized power allocation strategy and ﬁxed rate such

that the distortion outage probability for communication of a quasi-stationary source over a wireless

fading channel is minimized. With a ﬁxed rate, the encoders do not need to be rate adaptive which

simpliﬁes the design and implementation of transceivers. Noting (3) the distortion outage probability

is computed as follows

PDout = Pr
(
R > C (α, γ)
)Pr
(
σ2
s > Dm) + (
1 − Pr
(
R > C (α, γ)
))Pr
(
σ2
s 2
−2bR > Dm). (10)

We have the following design problem.

Problem 1: The problem of delay-limited channel optimized power adaptation for communication

of a quasi-stationary source with minimum distortion outage probability (COPA-MDO) is formulated

as follows min
γ,R PDout

subject to E[γ] ≤ ¯P . (11)

The solution to Problem 1 is obtained in two steps. For a given ﬁxed rate and noting Pr
(
σ2
s 2
−2bR >

Dm) ≤ Pr
(
σ2
s > Dm) : ∀R > 0, minimizing (10) is equivalent to minimizing Pr
(R > C (α, γ))
.

Problem 2 below formulates this (sub)problem and provides the optimum power adaptation strategy

as a function of R. Next, solving Problem 3, as described below, provides the optimum solution for

R, and hence problem 1 is solved.

Problem 2: With COPA-MDO scheme and with a given ﬁxed channel coding rate R, the power

adaptation problem is formulated as follows
min
γ Pr(R > C(α, γ))

subject to E[γ] ≤ ¯P . (12)

Proposition 1: The solution to Problem 2 for optimized power adaptation over a block fading

channel is given by
 γ∗(α, R) =
 



 22R−1
α if α ≥ 22R−1
q∗
1
0 if α < 22R−1
q∗
1 , (13)

4

in which q∗
1 is selected such that the power constraint is satisﬁed with equality, i.e.,
∫

α≥ 22R−1
q∗
1
 2
2R − 1
α f (α) dα = ¯P . (14)

Speciﬁcally for Rayleigh block fading channel, (14) is simpliﬁed to

(
2
2R − 1
) E1
 ( 2
2R − 1
q∗
1
 ) = ¯P . (15)

Proof: The proof follows that of Proposition 4 in [1]. Based on (14), for Rayleigh block fading

channel q∗
1 is to satisfy (15). In fact q∗
1 sets the SNR threshold below which the channel outage

occurs.

Now for obtained γ∗(α, R), minimizing (10) is equivalent to maximizing

Λ(R) = Pr
(
R ≤ C (α, γ∗(α, R))
)(Pr (σ2
s > Dm) − Pr (
σ2
s 2
−2bR > Dm)
), (16)

as formulated in Problem 3 below.

Problem 3: For COPA-MDO scheme with optimum power adaptation γ∗(α, R), the optimum R,

denoted by R∗, is given by the solution to the following optimization problem

max
R Λ(R)

subject to Eα[γ∗(α, R)] ≤ ¯P . (17)

Proposition 2: Solution to Problem 3 for block fading channel is R∗, where R∗ is an element of

the set { 1
2b log2 σ2
s
Dm ; s ∈ S, σ2
s ≥ Dm} that maximizes

Pr (
α ≥ 2
2R − 1
q∗
1
 ) (
Pr (
σ2
s > Dm) − Pr (
σ2
s 2
−2bR > Dm)
) (18)

for q∗
1 satisfying (14).

Proof: Using (1) and (13), we have

C(α, γ) =
 


R if 22R−1
α ≤ q∗
1

0 if 22R−1
α > q∗
1 (19)

Therefore,
 Pr (R ≤ C (α, γ)) = Pr (α ≥ 2
2R − 1
q∗
1
 ) (20)

Thus, the maximization in Problem 3 is equivalent to

max
R Pr (α ≥ 2
2R − 1
q∗
1
 ) (
Pr (σ2
s > Dm)−Pr (
σ2
s 2
−2bR > Dm)
) (21)

where q∗
1 satisﬁes (14).
 5

It is clear in (21) that Pr (σ2
s > Dm)−Pr (
σ2
s 2
−2bR > Dm) is an ascending (stair case like) function

of R with discontinuity at R = 1
2b log2 σ2
s
Dm ; ∀s ∈ S, σ2
s ≥ Dm. On the other hand, noting (14),
(22R−1)
q∗
1 increases as R grows; and therefore Pr (α ≥ 22R−1
q∗
1
 ) decreases as R increases. Thus, the

objective function in Problem 3 has discontinuities at R = 1
2b log2 σ2
s
Dm ; ∀s ∈ S, σ2
s ≥ Dm and also is

a descending function of R between two subsequent discontinuity points. Hence, we can conclude

that the maximum of (21) occurs at one of these discontinuity points.

The next two Propositions quantify the performance of the proposed COPA-MDO scheme in

terms of the resulting distortion outage probability and outage distortion exponent, respectively.

Proposition 3: The distortion outage probability obtained by COPA-MDO scheme for transmis-

sion of a quasi-stationary source over a Rayleigh block fading channel is given by

PDout = (1 − exp (
−2
2R∗ − 1
q∗
1
 )) Pr(σ2
s > Dm) + exp (
−2
2R∗ − 1
q∗
1
 ) Pr(σ2
s 2
−2bR∗ > Dm) (22)

with q∗
1 satisfying the following equation

(2
2R∗ − 1
) E1
 ( 2
2R∗ − 1
q∗
1
 ) = ¯P (23)

and R∗ given in Proposition 2.

Proof: Noting (20) and with exponentially distributed channel gain, we obtain

Pr (R∗ ≤ C (α, γ)) = exp (−2
2R∗ − 1
q∗
1
 ) , (24)

where R∗ is given in Proposition 2. Hence, equation (22) is derived by replacing (24) in (10).

As expected, the power allocation and hence the resulting distortion outage probability are func-

tions of the optimized ﬁxed rate.

Proposition 4: For communication of a quasi-stationary source over a Rayleigh block fading

channel, the COPA-MDO scheme achieves the outage distortion exponent ∆OD of the order O ( ¯P
ln ¯P )

for large average power limit ¯P .

Proof: To compute ∆OD as deﬁned in (4), we ﬁrst note that according to (23) and Proposition

2 for large enough ¯P , we have 22R∗ −1
q∗
1 → 0. Thus, using the approximation given in (8), (23) can

be rewritten as follows.
 − (
2
2R∗ − 1
) (
ln 2
2R∗ − 1
q∗
1 + Ec
) ∼= ¯P (25)

or equivalently
 q∗
1 ∼= (2
2R∗ − 1
) exp ( ¯P
22R∗ − 1
 ) . (26)

Therefore, using (9) and (26) and noting 22R∗ −1
q∗
1 → 0, (22) can be rewritten as follows

6

PDout ∼= Pr (
σ2
s > Dm) exp (
− ¯P
22R∗ − 1
) + (1 − exp (− ¯P
22R∗ − 1
 )) Pr(σ2
s 2
−2bR∗ > Dm). (27)

Noting Proposition 2 or equivalently minimizing (27) for large power constraint, it is observed that

the optimum R∗ have to be set such that Pr(σ2
s 2
−2bR∗ > Dm) = 0, i.e.,

R∗ = 1
2b log2 max
s {σ2
s }

Dm (28)

Thus, we have
 PDout ∼= Pr (σ2
s > Dm) exp
 




 − ¯P
( max
s {σ2
s }

Dm
 ) 1
b − 1
 




 (29)

and therefore,
 ∆OD = lim
¯P →∞
 ¯P
( max
s {σ2
s }

Dm
 ) 1
b −1 − ln Pr (σ2
s > Dm)

ln ¯P . (30)

Hence, the proof is complete.

For the optimized ﬁxed rate R∗, the distortion outage exponent enhances when the average power

limit ¯P increases.

In the following three Corollaries, we summarize the implications of the COPA-MDO design for

transmission of stationary sources over block fading channels. The stationary source is a Gaussian

with zero mean and variance σ2 ≥ Dm. Obviously, with σ2 < Dm, the distortion outage probability

is equal to zero. The results are directly obtained from Propositions 1, 2, 3 and 4 and allows for

insights into the system performance as it relates to source statistical characteristics.

Corollary 1: The optimum power adaptation and channel coding rate prescribed by COPA-MDO

for transmission of a stationary source over a block fading channel are given by

R∗ = 1
2b log2 σ2

Dm (31)

and
 γ∗ =
 



 ( σ2
Dm
 ) 1
b −1

q∗
1 if α ≥
 ( σ2
Dm
 ) 1
b −1

q∗
1
0 otherwise (32)

in which q∗
1 is selected such that the power constraint is satisﬁed with equality, i.e.,

∫

α≥( σ2
Dm )
 1
b −1

q∗
1
 ( σ2
Dm
 ) 1
b − 1

α f (α) dα = ¯P . (33)

7

Speciﬁcally for Rayleigh block fading channel, (33) is simpliﬁed to
(( σ2

Dm
 ) 1
b − 1

)
 E1
 



( σ2
Dm
 ) 1
b − 1

q∗
1
 


 = ¯P . (34)

Thus, for transmission of a stationary source over a block fading channel, the optimized ﬁxed rate

is simply set such that the source coding distortion is equal to its maximum Dm.

Corollary 2: The distortion outage probability obtained by COPA-MDO for transmission of a

stationary source over a Rayleigh block fading channel is given by

PDout = 1 − exp
 


−
( σ2
Dm
 ) 1
b − 1

q∗
 


 (35)

with q∗ satisfying the following equation
(( σ2

Dm
 ) 1
b − 1

)
 E1
 



( σ2
Dm
 ) 1
b − 1

q∗
 


 = ¯P . (36)

The results in Corollary 2 is obtained noting that σ2 > Dm and Pr(σ2
s 2
−2bR∗ > Dm) = 0 for

stationary sources.

Corollary 3: For communication of a stationary source over a Rayleigh block fading channel and

with large average power limit ¯P , the COPA-MDO scheme achieves the outage distortion exponent

∆OD = lim
¯P →∞
 ¯P

ln ¯P
 (
( σ2
Dm
 ) 1
b −1

) of the order O ( ¯P
ln ¯P ).

This immediately follows the proof of Proposition 4 and noting that for stationary sources R∗ =

1
2b log2 σ2
Dm .

The performance of COPA-MDO scheme is studied and compared in Section V.

IV. SOURCE AND CHANNEL OPTIMIZED POWER AND RATE ADAPTATION

In this section, we consider power and rate adaptation with regard to source and channel states for

improved performance of communications of a quasi-stationary source over a wireless block fading

channel. Thus, the objective in this section is to devise power and rate adaptation strategies for

each state (s, α) such that the distortion outage probability is minimized, when the average power

is constrained to ¯P . We have the following design problem.

Problem 4: The problem of delay-limited source and channel optimized power adaptation for

transmission of a quasi-stationary source with minimum distortion outage probability (SCOPA-

MDO) over a block fading channel is formulated as follows

min
γ,R PDout = Pr (D(σs, α, γ) > Dm)

subject to E[γ] < ¯P , (37)

8

where D(σs, α, γ) is given in (2).

Proposition 5: The solution to Problem 4 for an arbitrary block fading channel is given by

γ∗(σs, α) =
 



 1
α
 [( σ2
s
Dm
 ) 1
b − 1
]+ if 1
α
 [( σ2
s
Dm
 ) 1
b − 1
]+ ≤ q∗
2

0 Otherwise (38)

and
 R =
 



 1
2b log σ2
s
Dm if σ2
s
Dm > 1 and 1
α
 [( σ2
s
Dm
 ) 1
b − 1
] < q∗
2

0 Otherwise, (39)

with q∗
2 satisfying the following equation

∑

s:σ2
s >Dm
 ∫

α: 1
α
 

( σ2
s
Dm
 ) 1
b −1



≤q∗
2
 ( σ2
s
Dm
 ) 1
b − 1

α f (α) P (s)dα = ¯P . (40)

Proof: The transmission rate may be controlled with respect to the channel state. Speciﬁcally,

it is logical to set the rate to its maximum as follows

R = C (α, γ) = 1
2 log(1 + αγ) (41)

and therefore, we have
 D(σs, α, γ) = σ2
s 2
−2bR = σ2
s
(1 + αγ)b . (42)

Let γ represent the probabilistically adapted transmission power. Obviously with distortion outage,

γ is set to zero and without distortion outage, the power is set to ´γ such that D(σs, α, ´γ) ≤ Dm. We

deﬁne ω(σs, α) to be the probability that (noting the channel SNR) the power is not zero in state

σs and α. We have,
 γ(σs, α) =
 


´γ(σs, α) with probability ω(σs, α)

0 with probability 1 − ω(σs, α). (43)

Thus, the distortion outage probability and the average transmitted power, respectively are 1 −

E[ω(σs, α)] and E[ω(σs, α)´γ(σs, α)]. Hence, using a Lagrangian optimization approach, the problem

may be restated as follows in which the Lagrangian variable λ is set such that the power constraint

in (37) is satisﬁed with equality.

max
ω(σs,α),´γ(σs,α)
E[ω(σs, α)] − λE[ω(σs, α)´γ(σs, α)] subject to (44)

C1 : σ2
s
(1 + α´γ(σs, α))b ≤ Dm

C2 : 0 < ω(σs, α) ≤ 1.

9

Note that ω(σs, α) = 0 is a trivial case that is excluded in C2 above. Due to the fact that C1
(representing D(σs, α, ´γ) ≤ Dm) and C2 are convex, the solution to the above for λ > 0 is globally

optimal. To solve this problem, we ﬁrst ﬁnd γ∗(σs, α) to maximize (44) for a given ω(σs, α). Then

for the resulting power adaptation strategy, we obtain ω∗(σs, α) to maximize (44). Thus, γ∗(σs, α)

is the solution to
 min
´γ(σs,α)
λE[ω(σs, α)´γ(σs, α)] subject to

C1 : σ2
s
(1 + α´γ(σs, α))b ≤ Dm. (45)

Noting λ > 0 and 0 < ω(σs, α) ≤ 1, (45) is equivalent to the following

min ´γ(σs, α)

subject to σ2
s
(1 + α´γ(σs, α))b ≤ Dm. (46)

Obviously, as γ∗(σs, α), the solution to the problem above, is to be nonnegative, we have

γ∗(σs, α) = 1
α
 [( σ2
s
Dm
 ) 1
b − 1

]+
 . (47)

Now, given the power adaptation γ∗(σs, α), the optimization problem (44) may be rewritten as follow

max
0≤ω(σs,α)≤1
E [ω(σs, α) (1 − λγ∗(σs, α))]. (48)

The solution to (48) is given by

ω∗(σs, α) =
 


1 if γ∗(σs, α) ≤ 1
λ

0 if γ∗(σs, α) > 1
λ. (49)

Therefore, noting (47), (49) and (43), we obtain (38). Substituting (38) in (41), achieving (39) is

straightforward.

The Lagrangian variable λ is set such that the power constraint E[ω∗(σs, α)γ∗(σs, α)] = ¯P is

satisﬁed. We have ∑

s∈S
 ∫

α:γ∗(σs,α)≤ 1
λ
 γ∗(σs, α)f (α) P (s)dα = ¯P , (50)

where replacing 1
λ with q∗
2 completes the proof.

The next two Propositions quantify the performance of the proposed SCOPA-MDO scheme in

terms of the resulting distortion outage probability and outage distortion exponent, respectively.

Proposition 6: The distortion outage probability for transmission of a quasi-stationary source

using the SCOPA-MDO scheme over a Rayleigh block fading channel is given by

10

PDout = Pr(σ2
s > Dm)− ∑

s:σ2
s >Dmexp
 


−
( σ2
s
Dm
 ) 1
b −1

q∗
2
 


P (s) (51)

with q∗
2 satisfying the following equation

∑

s:σ2
s >Dm
(( σ2
s
Dm
 ) 1
b − 1

)
 E1
 



( σ2
s
Dm
 ) 1
b − 1

q∗
2
 


 P (s) = ¯P . (52)

Proof: The proof is provided in Appendix A.

Proposition 7: For communication of a quasi-stationary source over a Rayleigh block fading

channel, the SCOPA-MDO scheme achieves an outage distortion exponent ∆OD of the order O ( ¯P
ln ¯P )

for large average power limit ¯P .

Proof: Noting (52), ¯P → ∞ requires that q∗
2 → ∞. In this case, using (8), we can rewrite (52)

as follows.
 ∑

s:σ2
s >Dm
−
 (( σ2
s
Dm
 ) 1
b − 1

)
 ln
 ( σ2
s
Dm
 ) 1
b − 1

q∗
2 P (s) ∼= ¯P (53)

and after some manipulations, we obtain

q∗
2 ∼= exp
 





 ¯P
∑

s:σ2
s >Dm
(( σ2
s
Dm
 ) 1
b − 1
) P (s)





 . exp






 ∑

s:σ2
s >Dm

(( σ2
s
Dm
 ) 1
b − 1
) ln (( σ2
s
Dm

) 1
b − 1
)P (s)

∑

s:σ2
s >Dm

(( σ2
s
Dm
 ) 1
b − 1
)
P (s)
 




 .

(54)

Considering (51) and (9) for q∗
2 → ∞, we have

PDout ∼= 1
q∗
2
 ∑

s:σ2
s >Dm
(( σ2
s
Dm
 ) 1
b − 1

)
 P (s). (55)

Hence, noting (54) for q∗
2 → ∞ we obtain

∆OD = lim
¯P →∞
 ¯P

ln ¯P ∑

s:σ2
s >Dm
(( σ2
s
Dm
 ) 1
b − 1
) P (s). (56)

Thus, the proof is completed.

The following Corollary expresses the implication of the SCOPA-MDO design for transmission

of a stationary source over block fading channels. This is directly obtained from Proposition 5 when

a stationary source is assumed.
 11

Corollary 4: The optimum channel coding rate and power adaptation prescribed by SCOPA-MDO

for transmission of a stationary source over a block fading channel are given by

R∗ =
 



 1
2b log2 σ2
Dm if α ≥
 ( σ2
Dm
 ) 1
b −1

q∗
2
0 otherwise (57)

γ∗ =
 



 ( σ2
Dm
 ) 1
b −1

q∗
2 if α ≥
 ( σ2
Dm
 ) 1
b −1

q∗
2 ,

0 otherwise (58)

in which q∗
2 is selected such that the power constraint is satisﬁed with equality, i.e.,

∫

α≥( σ2
Dm )
 1
b −1

q∗
2
 ( σ2
Dm
 ) 1
b − 1

α f (α) dα = ¯P . (59)

Speciﬁcally for Rayleigh block fading channel, (59) is simpliﬁed to

(( σ2

Dm
 ) 1
b − 1

)
 E1
 



( σ2
Dm
 ) 1
b − 1

q∗
2
 


 = ¯P . (60)

Remark 1: Examining Corollaries 1 and 4 for transmission of a stationary source over a block

fading channel, one sees that the SCOPA-MDO and COPA-MDO schemes provide the same distor-

tion outage probability and outage distortion exponent. This implies that in this setting with power

adaptation an optimized ﬁxed rate provides all the gain that may be obtained by rate adaptation.

The performance of SCOPA-MDO scheme is studied in Section V.

V. PERFORMANCE EVALUATION

In this section, we ﬁrst present two constant power transmission schemes as benchmarks for

comparisons. Next, we consider analytical performance comparison of different schemes followed

by numerical results. To this end, we consider four quasi-stationary sources, with Ns = 25 where

the variance of the source in the state s is given by σ2
s (s) = (1 + 1
6s)
2 : ∀s ∈ {0, 1, ..., NS − 1}. For

three of the sources, labeled as G1, G2 and G3, the probability of being in different states follows

a discrete Gaussian distribution with mean 3 and variances 0.05, 0.48, 1.07, respectively. For the

fourth source, U, the said distribution is considered uniform with the same mean and a variance of

1.44. We also consider an stationary source S with σs = 3 for a meaningful comparison. Unless

otherwise mentioned, we consider the source G2 for the following results and simulations.

12

A. Benchmark

Two constant power schemes for transmission of a quasi-stationary source over a block fading

channel are considered as benchmarks for comparisons. In the ﬁrst scheme, the channel coding

rate is adjusted based on the channel state to minimize the distortion outage probability; hence the

scheme is labeled as Channel Optimized Rate Adaptation with Constant Power (CORACP). In the

second scheme with Constant Rate and Constant Power (CRCP), the aim is to ﬁnd the optimized

ﬁxed rate such that the distortion outage probability is minimized.

1) Channel Optimized Rate Adaptation with Constant Power: With CORACP and constant trans-

mission power ¯P , the instantaneous capacity is given by C = 1
2 log2 (1 + α ¯P ); and hence to

minimize PDout it is logical to consider the rate adaptation strategy of R = C. The source coding

rate is then set as Rs = bR. The next two Propositions quantify the distortion outage performance

of CORACP.

Proposition 8: The distortion outage probability for transmission of a quasi-stationary source over

a Rayleigh block fading channel using CORACP is given by

PDout = Pr(σ2
s > Dm) − ∑

s:σ2
s >Dm exp
 (
− 1
¯P
 [( σ2
s
Dm
 ) 1
b − 1

])
 P (s). (61)

Proof: The proof is provided in Appendix B.

Proposition 9: For communication of a quasi-stationary source over a Rayleigh block fading

channel, the CORACP scheme achieves the outage distortion exponent ∆OD of the order O (1).

Proof: Using (9) and considering large enough ¯P , (61) can be rewritten as

PDout ∼= 1
¯P
 ∑

s:σ2
s >Dm
 (( σ2
s
Dm
 ) 1
b − 1

)
 P (s). (62)

Thus,
 ∆OD = lim
¯P →∞
−
− ln ¯P + ln ∑

s:σ2
s >Dm
 (( σ2
s
Dm
 ) 1
b − 1
) P (s)

ln ¯P = 1 (63)

and the proof is complete.

Based on Propositions 8 and 9, the following Corollary presents the performance of CORACP

with stationary sources.

Corollary 5: For communication of a stationary source over a Rayleigh block fading channel, the

CORACP scheme achieves a distortion outage probability of

PDout = 1 − exp
 


−
( σ2
Dm
 ) 1
b − 1
¯P
 


 (64)

13

and an outage distortion exponent of ∆OD of the order O (1).

2) Constant Rate Constant Power: With CRCP, the ﬁxed rate is optimized to minimize the

distortion outage probability when the power is constant. The following three Propositions express

the optimized ﬁxed rate, distortion outage probability and distortion outage exponent obtained by

CRCP.

Proposition 10: For transmission of a quasi-stationary source over a block fading channel using

the CRCP scheme, the optimum rate, R∗, is an element of the set { 1
2b log2 σ2
s
Dm ; s ∈ S, σ2
s ≥ Dm}

that maximizes
 Pr (
α ≥ 2
2R − 1
¯P
 ) (
Pr (
σ2
s > Dm) − Pr (
σ2
s 2
−2bR > Dm)
) (65)

Proof: The proof is similar to the proof of Proposition 3.

Proposition 11: For transmission of a quasi-stationary source over a Rayleigh block fading chan-

nel, the CRCP scheme achieves the distortion outage probability of

PDout = (1 − exp (−2
2R∗ − 1
¯P
 )) Pr(σ2
s > Dm) + exp (−2
2R∗ − 1
¯P
 ) Pr(σ2
s 2
−2bR∗ > Dm), (66)

with R∗ in Proposition 10, and the outage distortion exponent ∆OD of the order O (1).

Proof: Noting (10) and constant power ¯P with exponentially distributed channel gain, obtaining

PDout is straightforward. For a large power constraint, one can verify that R∗ is simpliﬁed to

R∗ = 1
2b log2 max
s {σ2
s }

Dm . (67)

Thus, from Proposition 11 and noting (9) and (67), we obtain

PDout ∼=
 ( max
s {σ2
s }

Dm
 ) 1
b − 1

¯P Pr (σ2
s > Dm) (68)

and therefore,
∆OD = lim
¯P →∞−
− ln( ¯P ) + ln
 ((( max
s {σ2
s }

Dm
 ) 1
b − 1

)
 Pr (σ2
s > Dm)

)

ln ¯P = 1. (69)

Based on the above two Propositions, the following two Corollaries present the optimum rate and

the performance of CRCP with stationary sources.

Corollary 6: The optimum channel coding rate prescribed by CRCP for transmission of a sta-

tionary source over a block fading channel is given by

R∗ = 1
2b log2 σ2

Dm (70)

14

Corollary 7: For communication of a stationary source over a Rayleigh block fading channel, the

CRCP scheme achieves a distortion outage probability of

PDout = 1 − exp
 


−
( σ2
Dm
 ) 1
b − 1
¯P
 


 (71)

and an outage distortion exponent of ∆OD of the order O (1).

Remark 2: Noting Corollaries 5 and 7 for transmission of a stationary source over a block

fading channel, one sees that the CORACP and CRCP schemes provide the same distortion outage

probability and outage distortion exponent. This implies that in this setting with constant power, an

optimized ﬁxed rate provides all the gain that may be obtained by rate adaptation.

B. Analytical Performance Comparison

In the sequel, we quantify the respective asymptotic outage distortion gain GOD of SCOPA-MDO,

COPA-MDO, CORACP and CRCP for transmission of a quasi-stationary source over a block fading

channel.

Proposition 12: In transmission of a quasi-stationary source over a Rayleigh block fading channel,

the asymptotic outage distortion gain obtained by SCOPA-MDO with respect to COPA-MDO is given

by
 GOD = 10 log10
 


(max
s {σ2
s }

Dm
 ) 1
b − 1



 − 10 log10 ∑

s:σ2
s >Dm
(( σ2
s
Dm
 ) 1
b − 1

)
 P (s). (72)

Proof: The proof is provided in Appendix C.

Proposition 13: In transmission of a quasi-stationary source over a Rayleigh block fading channel,

the asymptotic outage distortion gain obtained by COPA-MDO with respect to CORACP is given

by
 GOD = 10 log10 ¯P2
( max
s {σ2
s }

Dm
 ) 1
b − 1
 − 10 log10 ln ¯P2
∑

s:σ2
s >Dm
(( σ2
s
Dm
 ) 1
b − 1
) P (s), (73)

where ¯P1 and ¯P2 are power limits in COPA-MDO and CORACP; ¯P1(dB) = ¯P2(dB)-GOD.

Proof: The proof is provided in Appendix C.

Proposition 14: In transmission of a quasi-stationary source over a Rayleigh block fading channel,

the asymptotic outage distortion gain obtained by CORACP with respect to CRCP is given by

GOD = 10 log10
 





(max
s {σ2
s }

Dm
 ) 1
b − 1



 Pr (
σ2
s > Dm)

 − 10 log10 ∑

s:σ2
s >Dm
(( σ2
s
Dm
 ) 1
b − 1

)
 P (s).

(74)

15

TABLE I

ASYMPTOTIC OUTAGE DISTORTION GAIN GOD OF SCHEME 1 WITH RESPECT TO SCHEME 2 FOR SOURCE G2 EVALUATED AT

b = 1 AND Dm = 8dB.

Scheme 1 Scheme 2 GOD at ¯P2 = 25dB GOD at ¯P2 = 20dB

SCOPA-MDO COPA-MDO 7.14 7.14

COPA-MDO CORACP 12.28 8.16

CORACP CRCP 5.74 5.74

Proof: The proof is provided in Appendix C.

As evident, GOD of SCOPA-MDO with respect to COPA-MDO and CORACP with respect to

CRCP are independent of the power. This is while the gain of COPA-MDO with respect to CORACP

depends nonlinearly on the average transmission power limit and it improves when the power limit

increases. The dependency of GOD on the variance of the source in different states and the maximum

allowable distortion is also seen in (72) to (74). Table I presents the value of GOD at Dm = 8dB.

The distortion outage exponent ∆OD of the COPA-MDO and SCOPA-MDO schemes which are

derived in line with the proofs of the Propositions 4 and 7, are quantiﬁed in Table II. As denoted in

Propositions 9 and 11, CORACP and CRCP schemes give ∆OD = 1. The distortion outage exponent

indicates the speed at which the distortion outage (dB) reduces as the average power (limit) (dB)

increases. Therefore, as evident, this speed is noticeably high with SCOPA-MDO and very low with

CORACP and CRCP. Furthermore, the ∆OD obtained by SCOPA-MDO and COPA-MDO depends

on the average power limit ¯P , maximum allowable distortion Dm and bandwidth expansion ratio b.

It is observed that with SCOPA-MDO and COPA-MDO, ∆OD improves as b, ¯P or Dm increase. In

fact, for a given value of N , a larger b implies a more ﬁnely encoded source that is more sensitive

to channel errors and hence can more greatly beneﬁt from increased power. The results in Tables

I and II indicate that from the perspective of probability of distortion outage, for delay-limited

communication of quasi-stationary sources, CORACP and CRCP schemes may not be appropriate

designs.

The following three Corollaries quantify the asymptotic outage distortion gain in transmission of

a stationary source over block fading channels. These are directly obtained from Propositions 12

and 14 when a stationary source is considered.

Corollary 8: In transmission of a stationary source over a Rayleigh block fading channel, the

asymptotic outage distortion gain obtained by SCOPA-MDO with respect to COPA-MDO is equal

to zero.

Corollary 9: In transmission of a stationary source over a Rayleigh block fading channel, the

16

TABLE II

DISTORTION OUTAGE EXPONENT ∆OD OF THE PROPOSED SCHEMES FOR SOURCE G2

Bandwidth Expansion Ratio b=1 b=5

Schemes and Settings SCOPA-MDO COPA-MDO SCOPA-MDO COPA-MDO

Dm = 8dB, ¯P = 16dB 18.90 3.89 129.08 34.33

Dm = 8dB, ¯P = 20dB 37.97 7.53 259.39 68.69

Dm = 5dB, ¯P = 20dB 10.80 3.27 95.75 42.53

asymptotic outage distortion gain of COPA-MDO with respect to CORACP is equal to

GOD = 10 log10 X
ln X , (75)

where X := ¯P2
( σ2
Dm
 ) 1
b −1 and ¯P2 is the power limit of CORACP.

Corollary 10: In transmission of a stationary source over a Rayleigh block fading channel, the

asymptotic outage distortion gain of CORACP with respect to CRCP is equal to zero.

The values of GOD in (75) and ∆OD in Corollary 3 for the stationary source S, ¯P2 = 20dB and

Dm = 8dB respectively amount to 16.33dB and 51. Noting Remarks 1 and 2, it is observed that

with stationary sources and common settings, an optimized ﬁxed rate scheme and an adaptive rate

scheme provide the same distortion outage probability. Therefore, in this setting, with optimum

power adaptation, COPA-MDO and SCOPA-MDO schemes; and with constant power, CORACP

and CRCP schemes provide the same distortion outage probability.

C. Numerical Results

Figs. 2a and 2b depict the distortion outage probability performance of the presented schemes as

a function of the power constraint ¯P for Dm = 8 dB and Dm = 5 dB, respectively. As expected, for

a given ¯P , PDout decreases as Dm increases. It is evident that the proposed SCOPA-MDO scheme

achieves an asymptotic outage distortion gain of about 7.1 dB and 5.6 dB with respect to COPA-

MDO, for ¯P = 20 dB and Dm = 8 dB and Dm = 5 dB, respectively. In the same settings, the

COPA-MDO scheme achieves asymptotic outage distortion gains of about 9.1 dB and 6.3 dB with

respect to CORACP; and CORACP achieves gains of 6 dB and 4.9 dB with respect to CRCP. The

results obtained from simulations and what is reported in Table I from analyses match reasonably

well given the assumption of very high average SNR considered in the analytical performance

evaluations.

The analytical results in Table II for ∆OD performance, may also be observed in numerical results

of Figs. 2a and 2b. Speciﬁcally, at each point on the curves, the corresponding value in the vertical

17

coordinate in dB, i.e., 10 log10 PDout divided by the value in the horizontal coordinate, i.e., ¯P (dB),

indicates −∆OD. For example, as seen in Fig. 2b, ∆OD for SCOPA-MDO is almost equal to 38 at
¯P = 20 dB with Dm = 8 dB.

Figs. 3a and 3b depict the PDout performance of the presented schemes for different sources.

As observed, as the non-stationary characteristics of the source intensiﬁes (from source S to U),

the distortion outage probability increases in general. However, the sensitivity of the performance

of different schemes to the level of non-stationarity varies. Once again, the advantage of power

adaptation is clear. For the stationary source S, as noted in Remarks 1 and 2 and also seen in these

Figures, SCOPA-MDO and COPA-MDO schemes provide the same distortion outage probability

in this setting. This also holds true for CORACP and CRCP. It is observed that SCOPA-MDO (or

equivalently COPA-MDO) scheme achieves an asymptotic outage distortion gain of about 16.8 dB

with respect to CORACP (or equivalently CRCP) for ¯P = 20 dB and Dm = 8 dB.

It is noteworthy that the four methods discussed, rely on different levels of source and channel

state information (SSI and CSI). Speciﬁcally, it can be veriﬁed that three schemes of SCOPA-MDO,

COPA-MDO and CORACP require instantaneous CSI for rate and/or power adaptation, while CRCP

needs CSI statistics. The SCOPA-MDO scheme also needs instantaneous SSI, while COPA-MDO

and CRCP simply need SSI statistics.
 VI. CONCLUSIONS

In this paper, delay-limited transmission of a quasi-stationary source over a block fading channel

was considered. Aiming at minimizing the distortion outage probability, two transmission strategies

namely channel-optimized power adaptation with ﬁxed rate (COPA-MDO) and source and channel

optimized power (and rate) adaptation (SCOPA-MDO) were introduced. The SCOPA-MDO scheme

provides a superior performance, while the COPA-MDO scheme enjoys the simplicity of single rate

transmission. In high SNR regime, different scaling laws involving outage distortion exponent and

asymptotic outage distortion were derived. Our studies conﬁrm the beneﬁt of power adaption from

a distortion outage perspective and for delay-limited transmission of quasi-stationary sources over

wireless block fading channels. The analyses of the presented schemes in the case of stationary

sources indicate the same outage distortion performance with or without rate adaptation.

APPENDIX A

PROOF OF PROPOSITION 6

Noting (40) and (7) for exponentially distributed channel gain, we can obtain (52) and subsequently

q∗
2 by numerical methods. Using (38) and (42), the distortion for each state of the source and the

18

channel is given by
 D(σs, α, γ) =
 


Dm if σ2
s
Dm > 1 and
 

( σ2
s
Dm
 ) 1
b −1





α < q∗
2

σ2
s otherwise.
 (76)

Therefore, we have
 PDout = Pr
 ( 1
α
 [( σ2
s
Dm
 ) 1
b − 1

]
 ≥ q∗
2, σ2
s > Dm
)
 . (77)

Considering exponentially distributed channel gain α, deriving (51) is straightforward.

APPENDIX B

PROOF OF PROPOSITION 8

Noting (42) for γ = ¯P , distortion can be written as follows

D(σs, α, γ = ¯P ) = σ2
s 2
−2bR = σ2
s
(
1 + α ¯P )b (78)

and then we can derive

PDout = Pr
 ( σ2
s
(
1 + α ¯P )b > Dm, σ2
s > Dm
)
 = Pr
 (

α < 1
¯P
 (( σ2
s
Dm
 ) 1
b − 1

)
 , σ2
s > Dm
)
 . (79)

Considering exponentially distributed channel gain α, obtaining (61) is straightforward.

APPENDIX C

PROOF OF PROPOSITIONS 12 AND 13

The average power to asymptotically achieve a certain distortion outage probability using SCOPA-

MDO and COPA-MDO schemes are denoted by ¯P1 and ¯P2, respectively. Thus, we can use (5) to

derive GOD. Noting (54), (55) and (29) we set

lim
¯P1→∞
 ¯P1
∑

s:σ2
s >Dm
(( σ2
s
Dm
 ) 1
b − 1
) P (s) = lim
¯P2→∞
 ¯P2
( max
s {σ2
s }

Dm
 ) 1
b − 1
. (80)

Therefore, we can derive (72) and complete the proof of Proposition 12.

The proof of Propositions 13 or 14 is straightforward, when we use (29) and (62) or (62) and

(68); and obtain the following

lim
¯P2→∞
 ¯P1
( max
s {σ2
s }

Dm
 ) 1
b − 1
 = lim
¯P2→∞ ln ¯P2
∑

s:σ2
s >Dm
(( σ2
s
Dm
 ) 1
b − 1
) P (s) (81)

19

lim
¯P2→∞
 ¯P1
∑

s:σ2
s >Dm
(( σ2
s
Dm
 ) 1
b − 1
) P (s) = lim
¯P2→∞
 ¯P2(( max
s {σ2
s }

Dm
 ) 1
b − 1

)
 Pr (σ2
s > Dm)
. (82)

REFERENCES

[1] G. Caire, G. Taricco, and E. Biglieri, “Optimum power control over fading channels,” IEEE Trans. Inform. Theory, vol. 45,

pp. 1468–1489, July 1999.

[2] V. Hanly and D. Tse, “Multiaccess fading channels. Part II: Delay-limited capacities,” IEEE Trans. Inform. Theory, vol. 44,

pp. 2816–2831, Nov. 1998.

[3] L. Li and A. J. Goldsmith, “Capacity and optimal resource allocation for fading broadcast channels. Part II: Outage capacity,”

IEEE Trans. Inform. Theory, vol. 47, pp. 1103–1127, Mar. 2001.

[4] L. Li, N. Jindal, and A. Goldsmith, “Outage capacities and optimal power allocation for fading multiple-access channels,” IEEE

Trans. Inform. Theory, vol. 51, pp. 1326–1347, Nov. 2005.

[5] J. N. Laneman, D. N. C. Tse, and G. W. Wornell, “Cooperative diversity in wireless networks: Efﬁcient protocols and outage

behavior,” IEEE Trans. Inform. Theory, vol. 50, pp. 3062–3080, Nov. 2004.

[6] Y. Liang, V. V. Veeravalli, and H. V. Poor, “Resource allocation for wireless fading relay channels: Max-Min solution,” IEEE

Trans. Inform. Theory, vol. 53, pp. 3432–3453, Oct. 2007.

[7] D. Gunduz and E. Erkip, “Opportunistic cooperation by dynamic resource allocation,” IEEE Trans. Wireless Commun., vol. 6,

pp. 1446–1454, Oct. 2007.

[8] J. N. Laneman, G. W. Wornell, and J. G. Apostolopoulos, “Source-channel diversity for parallel channels,” IEEE Trans. Inform.

Theory, vol. 51, pp. 3518–3539, Oct. 2005.

[9] B. Dunn and J. N. Laneman, “Characterizing source-channel diversity approaches beyond the distortion exponent,” in 43rd

Annu. Allerton Conf. Communications, Control and Computing, (Monticello, IL), Oct. 2005.

[10] D. Gunduz and E. Erkip, “Joint source-channel codes for MIMO block-fading channels,” IEEE Trans. Inform. Theory, vol. 54,

pp. 116–134, Jan. 2008.

[11] D. Gunduz and E. Erkip, “Source and channel coding for cooperative relaying,” IEEE Trans. Inform. Theory, vol. 53, pp. 3454–

3475, Oct. 2007.

[12] T. Holliday, A. J. Goldsmith, and H. V. Poor, “Joint source and channel coding for MIMO systems: Is it better to be robust or

quick?,” IEEE Trans. Inform. Theory, vol. 54, pp. 1393–1405, Apr. 2008.

[13] K. Bhattad, K. R. Narayanan, and G. Caire, “On the distortion SNR exponent of some layered transmission schemes,” IEEE

Trans. Inform. Theory, vol. 54, pp. 2943–2958, July 2008.

[14] L. Peng and A. Guillen i Fabregas, “Distortion outage probability in MIMO block-fading channels,” in IEEE Int. Symp. Inform.

Theory, (Austin, Texas, U.S.A), pp. 2223–2227, June 2010.

[15] D. Gunduz, E. Erkip, A. Goldsmith, and H. V. Poor, “Source and channel coding for correlated sources over multiuser channels,”

IEEE Trans. Inform. Theory, vol. 55, pp. 3927–3944, Sept. 2009.

[16] S. Vembu, S. Verdu, and Y. Steinberg, “The source-channel separation theorem revisited,” IEEE Trans. Inform. Theory, vol. 41,

pp. 44–54, Jan. 1995.

[17] M. Alouini and A. Goldsmith, “Capacity of Rayleigh fading channels under different adaptive transmission and diversity-

combining techniques,” IEEE Trans. Veh. Technol., vol. 48, pp. 1165–1181, July 1996.

[18] Z. He, Y. Liang, L. Chen, I. Ahmad, and D. Wu, “Power-rate-distortion analysis for wireless video communication under energy

constraints,” IEEE Trans. Circuits Syst. Video Technol., vol. 15, pp. 1468–1489, May 2005.

[19] T. M. Cover and J. A. Thomas, Elements of Information Theory. New York: Wiley, 1991.

[20] M. Abramowitz and I. A. Stegun, Handbook of Mathematical Functions. June 1974.

20

Source
Encoder Channel
Encoder
 Wireless
Channel

Channel
Decoder
Source
Decoder

Rate and Power Control Unit Multiplicative Fading

Source
Input

Source
OutputSource Statistics
 Fig. 1. Block diagram of the system.

0 5 10 15 20 25 30

10
−40

10
−30

10
−20

10
−10

10
0
 Power Constraint (dB)PDout

CRCP
CORACP
COPA−MDO
SCOPA−MDO

0 5 10 15 20 25 30
10
−20

10
−15

10
−10

10
−5

10
0
 Power Constraint (dB)PDout

CRCP
CORACP
COPA−MDO
SCOPA−MDO

(a) (b)

Fig. 2. Distortion outage probability versus ¯P ; b = 1 and (a) Dm = 8 dB (b)Dm = 5 dB.

21

0 2 4 6 8 10 12 14 16 18 20

10
−15

10
−10

10
−5
 Power Constraint (dB)PDout
Source: S
Source: G1
Source: G2
Source: G3
Source: U

Source: S
Source: G1
Source: G2
Source: G3
Source: U

Source: S
Source: G1
Source: G2
Source: G3
Source: U
 COPA−MDO
SCOPA−MDO

0 2 4 6 8 10 12 14 16 18 20

10
−2

10
−1

10
0
 Power Constraint (dB)PDout
Source: S
Source: G1
Source: G2
Source: G3
Source: U
 CRCP
CORACP

(a) (b)

Fig. 3. Distortion outage probability versus ¯P for ﬁve different sources; b = 1 and Dm = 8 dB.

22
