<!-- source: https://arxiv.org/pdf/2508.16400 | converted from PDF -->

THE EXCEPTIONAL SET IN GOLDBACH’S PROBLEM WITH TWO
CHEN PRIMES

LASSE GRIMMELT AND JONI TER ¨AV ¨AINEN

Abstract. We show that all natural numbers n ” 4 pmod 6q are the sum of two Chen
primes (primes p such that p ` 2 has at most two prime factors), apart from a power-
saving set of exceptions. This improves on various previous results and is optimal, barring
substantial progress on the twin prime or binary Goldbach conjectures.
The proof is based on constructing a non-negative model for the Chen primes in a suitable
approximate sense. The key ingredient for this is showing that the primes are power saving
Fourier close to the rough number Cram´er model times p1 ` op1qq. Additionally, we develop
an efficient sieving strategy for additive problems that for large prime factors utilises a
power-saving variant of the Bombieri–Vinogradov theorem and for small prime factors a
fundamental Lemma type result.
 Contents

1. Introduction 1
2. Notation and structure 7
3. A variant of Chen’s sieve 11
4. Fourier approximants 18
5. Main-sieve removal 28
6. The additive problem with sieves 37
7. From primes to Cram´er’s model 51
8. Proof of Theorem 1.1 64
References 70

1. Introduction

In this paper, we study the exceptional set in the binary Goldbach problem with almost
twin primes. There are different ways to define what an almost twin prime should be. We
shall consider here those primes p for which p ` 2 has few prime factors. We define

Pk :“ tm P N : m has at most k prime factorsu,

and abbreviate P1 as P. Thanks to a celebrated result of Chen [1], we know that there are
infinitely many primes p such that p ` 2 P P2, and we call these primes Chen primes.
The binary Goldbach problem states that every even integer n ě 4 is the sum of two
primes. Over the years, various results have been proved showing this for all n outside an
exceptional set. Montgomery and Vaughan [21] were the first to show a power-saving bound
for this exceptional set; thus, there exists δ ą 0 such that all but at most OpN 1´δq even
1

arXiv:2508.16400v2  [math.NT]  29 Jul 2026

integers n ď N are the sum of two primes. Apart from the precise exponent δ, for which the
current record is due to Pintz [23], this is still the state of the art.
We prove the following hybrid of the results of Chen and Montgomery–Vaughan.

Theorem 1.1. There is a constant δ ą 0 such that all but OpN 1´δq natural numbers m ď
N, m ” 4 pmod 6q are the sum of two Chen primes.

Both δ and the implied constant in this theorem are effective and could in principle be
computed. Apart from the value of δ, any improvement to Theorem 1.1 would imply drastic
new results for either the binary Goldbach conjecture or the twin prime conjecture, and so
our result seems to be the best possible in the absence of a major advance on one of these
problems.

1.1. Previous works. Based on standard heuristics of Hardy–Littlewood type, we expect
that every large integer m ” 4 pmod 6q can be written as m “ p1 ` p2 with pi, pi ` 2 P P for
i P t1, 2u. Needless to say, this is far out of reach as it would imply as special cases both the
twin prime conjecture and the binary Goldbach conjecture (for large numbers congruent to
4 pmod 6q). Previously, various approximations to this have been proved. To state them, we
define the related exceptional set as

EpN, k1, k2q :“ |tm ď N : m ” 4 pmod 6q, m ‰ p1 ` p2 @pi P P X pPki ´ 2qu|.

Here (and in Theorem 1.1) the restriction to m ” 4 pmod 6q is imposed since for any fixed
k P N almost all elements of P X pPk ´ 2q are ” 5 pmod 6q.
Theorem 1.1 improves upon the following estimates. For any A ą 0, we have

EpN, 5, 7q !A N plog N q
´A, due to Tolev [28]

EpN, 3, 8q !A N plog N q
´A, due to Meng [20]

EpN, 2, 7q !A N plog N q
´A due to Matom¨aki [14],

(1.1)

where P8 “ N. All the implied constants appearing in (1.1) are ineffective.
Matom¨aki and Shao in [17] solved the ternary Goldbach problem for the Chen primes by
showing that every sufficiently large integer m ” 3 pmod 6q is the sum of three Chen primes.
Even though it is not explicitly stated there, the methods of [17] can be adapted to the
binary case with only minor modifications (see [27, Proposition 2.1] for a binary version of
the transference principle in [17]), and a preliminary calculation suggests that this leads to
an estimate of the form
 EpN, 2, 2q ! N plog log log N q
´δ

for some small δ ą 0. The expected saving of size plog log log N q
´δ is a consequence of three
factors: first, the Siegel–Walfisz theorem restricts the range of moduli to a power of log N ;
second, the W -trick loses another log iteration; third, the final log iteration is lost due to
the sparseness of high-rank Bohr sets.
It should also be mentioned that this paper improves on a previous preprint of the au-
thors [9], in which the weaker result EpN, 2, 3q ! N 1´δ was shown. The approach we take
here is technically simpler in addition to producing a stronger result. In particular, the
current approach does not require the spectral theory of automorphic forms, which featured
in [9] due to the use of Kloosterman sum estimates of Deshouillers–Iwaniec [2] and their
2

variants. Apart from a similar treatment of sieves for large prime factors, the approach here
is independent of [9] and supersedes it.

1.2. Background and strategy. We now give an informal overview of the proof strategy
for Theorem 1.1.
Let Λ2pnq be a normalised indicator of n having at most two prime divisors, defined
precisely in (3.6). We define a normalised indicator for the Chen primes as

ΛChenpnq :“ ΛpnqΛ2pn ` 2q.

Theorem 1.1 follows if we can show a reasonable lower bound for
ÿ

n1`n2“m ΛChenpn1qΛChenpn2q(1.2)

for all but OpN 1´δq natural numbers m ď N, m ” 4 pmod 6q. Since we do not understand
ΛChenpnq directly (we do not even know the mean value of this function), we need to employ
a suitably chosen sieve minorant ωChenpnq ď ΛChenpnq. Chen’s famous result ensures the
existence of such a minorant (sometimes called Chen’s sieve) with
ÿ

nďN ωChenpnq “ pc ` op1qqN(1.3)

for some constant c ą 0. However, we cannot immediately insert this minorant ωChenpnq
into (1.2), since ÿ

n1`n2“m ΛChenpn1qΛChenpn2q ě ÿ

n1`n2“m ωChenpn1qωChenpn2q,(1.4)

is not necessarily true as ωChenpnq can also take negative values. In the existing literature,
there are two ways to overcome this issue. First, one may apply a so-called vector sieve
inequality. However, this weakens the sieves and is the reason that the results in (1.1) cannot
reach two Chen primes. Second, one can apply a transference principle based approach.
This approach was introduced to this problem by Matom¨aki and Shao [17] and only gives
a relatively weak saving on the exceptional set, as mentioned above. Our strategy, inspired
by work of the first author [8] and Green’s recent work [7], is to construct a non-negative
approximant to Chen’s sieve ωChen that makes it possible to restore (1.4). Roughly speaking,
the strategy is based on three ingredients:
‚ We use Fourier closeness to approximate by suitable arithmetic functions.
‚ We treat sieves efficiently by using a power-saving Bombieri–Vinogradov theorem for
large moduli and by adapting the fundamental lemma of sieve theory to our additive
setting.
‚ We prove that primes can be replaced by the Cram´er model1 in an approximate sense.
Similarly to other works that consider the power-saving regime (for example, [21], [6]), we
need to consider the effect of a possible exceptional zero separately. See Subsection 1.2.5 for
more details.
We next give some details for the three aforementioned ingredients and then outline how
they come together in the proof of Theorem 1.1.

1This model, also known as the Cram´er–Granville model and used in many other recent works on additive
problems for the primes (see e.g. [26], [7], [18], [16], [13]), is a normalised indicator of integers having no
small prime factors; see (1.6) below. 3

1.2.1. A general approximation framework. A key aspect of the transference principle is to
use convolutions with Bohr sets to extract a Fourier-close approximant for any function. To
create a non-negative approximant for ωChenpnq, we develop this perspective further in the
given additive context and write f « g to roughly mean that
ÿ

n1`n2“m

`f pn1q ´ gpn1q
˘ΛChenpn2q

is negligible for all natural numbers m ď N outside of a power-saving exceptional set. See
Definition 2.4 below for the rigorous definition. One way of obtaining approximants is by
Fourier analysis. In this sense, the major arc contribution in the classical circle method can
be seen as approximating the original function, if a sufficient minor arc bound is provided.
However, our more general perspective allows on the one hand for different approximants
than the major arcs and on the other hand also for other ways than Fourier-closeness to
achieve approximation. Our main goal is to show that there exists a function T pnq ě 0 such
that
 ωChenpnq « T pnq,(1.5)

which makes it possible to restore (1.4).

1.2.2. Sieves. Our construction of the approximant T is intricately linked to sieves. In
particular, we make extensive use of sieving separately for small primes, say less than P ; we
call such sieves pre-sieves. We denote by rP the Cram´er model, given by

rP pnq “ ź

păP
 ˆ1 ´ 1
p
 ˙´1 1p∤n.(1.6)

This function is a normalised indicator for n being P -rough (i.e., n having no prime factors
less than P ). We further denote by ω, Ω in this sketch the associated lower and upper bound
pre-sieves (normalised to have mean comparable to 1), so that ω ď rP ď Ω. See Definition 2.2
for the precise choice. By ωM, ΩM we denote the lower and upper bound sieves handling
the primes larger than P ; we call these informally main-sieves. See Definition 2.3 for their
precise requirements. Importantly, to achieve a power saving we take P “ N δ0 to be a small
power of N , and the obtained saving δ in Theorem 1.1 is a function of δ0. We do not specify
the level of the sieves for this sketch.
We will prove two types of results for sieves. First, we show that there exists a constant
cM ą 0 such that we can replace the main-sieves with it, that is

Λpnqωpn ` 2qωMpn ` 2q « cMΛpnqωpn ` 2q(1.7)

and similarly for Ω, ΩM and combinations thereof. The approximation (1.7) is based on the
fact that the Bombieri–Vinogradov theorem can produce a power saving, provided the main
term includes the contribution of low conductor characters. See Drappeau’s work [3] for a
related strategy. Second, as a consequence of fundamental lemma-type results, we show that
the rough numbers can be exchanged with upper and lower bound sieves in the sense that

f pnqωpn ` 2q « f pnqΩpn ` 2q « f pnqrP pn ` 2q,(1.8)

for f P tΛ, rP u. 4

1.2.3. Replacing primes by the Cram´er model. The technical centrepiece of the proof of
Theorem 1.1 is replacing the primes by the Cram´er model (1.6).
To be more precise, we want to show in the language of the previous subsection that

Λpnqωpn ` 2q « rP pnqωpn ` 2q.(1.9)

The key ingredient for this is showing that Λ is Fourier-close to rP pnqp1 ` op1qq with a power
saving. Since it allows one to replace Λ by a function that is on the one hand non-negative
and on the other hand can be upper and lower bounded effectively by sieves, we expect that
this result may be useful for other purposes. We state here a simplified version that assumes
that there is no exceptional zero; see Theorem 7.9 for the full statement.

Theorem 1.2 (Fourier-approximating primes by Cram´er model). Let exppplog N q
1{2q ď
R40 ď P ď N 1{5 and assume that there is no exceptional zero of level R2 and quality κ (see
Definition 7.1). Let hξ be the multiplicative function supported on square-free integers only
and given on the primes by
 hξppq “ min
!
1, 10p1 ` |ξ|q log p
log R
 )
,

and let
 HRpnq “ τ pnqplog Rq ż

R
 hξpnq
p1 ` |ξ|q10 dξ.

There exists an arithmetic function E and a constant c ą 0 such that the following holds.
We have
 sup
αPR
ˇ
ˇ ÿ

N {2ănďNpΛpnq ´ rP pnq ´ Epnqqepαnq
ˇ
ˇ ! N R´1{3

and
 |Epnq| ! HRpnq
´exp
`´cκlog N
log R ´ clog N
log P
 ˘ ` log N
log P exp
`´clog P
log R
 ˘¯
.

This theorem is inspired by Green’s work [7], where Λ was power-saving Fourier approxi-
mated by ÿ

qďR
 µpqqcqpnq
φpqq
(1.10)

plus additional terms that account for potential bad zeros of Dirichlet L-functions with
conductor up to R, which in our notation are contained in E. Here as there, the crucial
saving exp`´cκ log N
log R ˘ comes from zero-density estimates, for us in the form of Gallagher’s
prime number theorem [5]. Going one step further from (1.10) to rP introduces the other
components in E and requires both log N
log P and log P
log R to be sufficiently large. To introduce rP ,
we first bound the difference of (1.10) and rP . Doing this with Green’s explicit formula
based strategy would impose considerable technical challenges. We instead extract a major
arc model by convolving with a physical space major arc indicator, see bR in Definition 4.5.
Another difference compared to [7] is that we upper bound the error E in physical space
by the term involving HR. The estimation of E involves certain functions that resemble the
non-squared Selberg sieve weights and our treatment is inspired by the work of the Polymath
5

8b project ([24, Proposition 4.2]). Observe that hξpnq becomes negligible when n has prime
divisors that are much smaller than R1{p1`|ξ|q and one can show that
ÿ

nďN HRpnq ! N.(1.11)

In other words, this means that HR behaves similarly to the Cram´er model of range R. This
justifies the intuition that Λ is power-saving Fourier-close to rP p1 ` op1qq (or more precisely
rP `oprRq). We remark that under the assumption of GRH, the error term E can be omitted
from the statement. In contrast to [7], this does not, however, considerably simplify the rest
of the proof of Theorem 1.1.

1.2.4. Sketch of proof, unexceptional case. Assume first that there is no exceptional zero
for L-functions up to a certain conductor (see Definition 7.1). Let ΛE3 denote a weighted
indicator for numbers having exactly three prime divisors in certain suitable ranges; this is a
function that facilitates the sieve switching approach that Chen [1] pioneered. In a slightly
simplified form, our chain of lower bounds and approximants for Chen primes takes the
following shape. There are some absolute constants 0 ă c2 ă c1 ă 1 such that for P “ N δ0
we have
 ωChenpnq ě ΛpnqωωMpn ` 2q ´ ΩΩMpnqΛE3pn ` 2q(1.12)
 « c1Λpnqωpn ` 2q ´ c2ΩpnqΛE3pn ` 2q(1.13)
 « c1rP pnqωpn ` 2q ´ c2ΩpnqrP pn ` 2q(1.14)
 « c1rP pnqrP pn ` 2q ´ c2rP pnqrP pn ` 2q(1.15)
 “ pc1 ´ c2qrP pnqrP pn ` 2q.

We remark that in the rigorous proof, for technical reasons, we split the single roughness level
P into P0, P1, see remark 8.2. This achieves the goal (1.5) of constructing a non-negative
approximant, and Theorem 1.1 can be deduced as follows. For some error terms Eipmq that
are negligible outside of a power-saving exceptional set, we have
ÿ

n1`n2“m ΛChenpn1qΛChenpn2q

ěpc1 ´ c2q ÿ

n1`n2“m Λpn1qΛ2pn1 ` 2qrP pn2qrP pn2 ` 2q ` E1pmq

ěpc1 ´ c2q2 ÿ

n1`n2“m rP pn1qrP pn1 ` 2qrP pn2qrP pn2 ` 2q ` E2pmq

“pc1 ´ c2q2mSpmq ` E3pmq,(1.16)

where Spmq is the singular series that encodes local solution densities and that agrees with
the expected Hardy–Littlewood heuristics. The step (1.16) is a consequence of a fundamental
lemma-type result that allows us to handle P -rough numbers in essentially any additive setup
easily with high precision, as long as plog mq{plog P q is large enough in absolute terms.
We now outline what goes into each of the steps in the chain of inequalities and approxi-
mations (1.12)–(1.15). The sieve ωChen in (1.12) is a combination of the usual sieve-switching
approach for Chen primes with a separate sieve for small prime factors. In reality, one needs
to be slightly more careful, as the product of two lower bound sieves is not a lower bound
sieve. Note that for our purposes ΛE3 behaves the same way as Λ. In step (1.13), we remove
6

the contribution of the main-sieves by (1.7). In step (1.14), we replace the primes (respec-
tively, the E3-numbers) with the much easier-to-handle P -Cram´er model; this follows from
Theorem 1.2 or more precisely from (1.9). The final step (1.15) is a consequence of (1.8).

1.2.5. Sketch of proof, exceptional case. If the exceptional zero rβ with exceptional character
rχ exists, there are two additional technical complications, apart from which the general
strategy is identical.
First, we have to include a correction term of the form 1 ´ rχpnqn rβ´1 when replacing Λ
or ΛE3 with rP . This will, in some cases, reduce the number of expected representations
by introducing a factor related to p1 ´ rβq log N . We need to compensate for this possibly
smaller main term with a better saving in the affected cases.
Second, following the strategy of the unexceptional case without modification would lead
to roughly

ΛpnqΛ2pn ` 2q Ç rP pnqrP pn ` 2q
`c1p1 ´ rχpnqn rβ´1q ´ c2p1 ´ rχpn ` 2qn rβ´1q˘.

This function is not, and cannot be well approximated by, a non-negative model. Indeed, it
has a negative average in residue classes b modulo rr with rχpbq “ 1 and rχpb ` 2q “ ´1. To
circumvent this issue, we exclude this bad case before the application of Chen’s lower bound
by multiplying with a factor of p1 ´ rχpnqq{2 “ 1 rχpnq“´1 or p1 ` rχpnqqp1 ` rχpn ` 2qq{4 “
1 rχpnq“ rχpn`2q“1.

1.3. Acknowledgements. The first author received funding from the European Research
Council (ERC) under the European Union’s Horizon research and innovation programme,
grant agreement no. 851318 and no. 101162746. The second author was supported by
Academy of Finland grant no. 362303 and funding from the European Union’s Horizon
Europe research and innovation programme under Marie Sk lodowska-Curie grant agreement
no. 101058904 and ERC grant agreement no. 101162746. The authors thank James Maynard
for helpful comments and discussions and Kaisa Matom¨aki for encouragement to obtain the
optimal result.
 2. Notation and structure

2.1. Notation. Euler’s totient function, the divisor function, and the von Mangoldt function
are denoted by φpnq, τ pnq, Λpnq, respectively. The k-fold divisor function is written as τkpnq.
By apqq in a summation index we mean that a runs over a complete system of residues modulo
q; similarly by χpqq in a summation index we mean that χ runs over the multiplicative
characters modulo q. By ÿ˚ we mean that a summation is restricted to primitive residue
classes or primitive characters.
The symbols ˚, ‹ denote the additive and multiplicative convolution of two arithmetic
functions, respectively. For any functions f, g : Z Ñ C, we write

f ˚ gpnq “ ÿ

mPZ f pmqgpn ´ mq,

f ‹ gpnq “ ÿ

d|n f pdqgpn{dq.

We denote by } ¨ }1, } ¨ }2, and } ¨ }8 the L1, L2, and L8 norms of arithmetic sequences (we
will use } ¨ }^
8 in a Fourier context, see Definition 4.1).
7

We call n P -rough if it has no prime factor less than P (equivalently every prime factor
of n is ě P , equivalently pn, ś

păP pq “ 1).
We use p¨q
˘ to denote the shift operator by ˘2. We only use this notation in statements
that benefit from not having the variable explicit, for example

}f g`}1 “ ÿ

nPZ |f pnqgpn ` 2q| and f ˚ g`pnq “ ÿ

mPZ f pmqgpn ` 2 ´ mq.

We use the standard exponential phase notation

epzq :“ e2πiz, erpzq :“ epz{rq,

and also denote Ramanujan’s sum by

cqpnq “ ÿ˚

bpqq eqpbnq.

We write n „ N to denote the condition N {2 ă n ď N .

2.2. Choices of parameters. We use c exclusively in error terms to mean the existence of
an absolute constant c ą 0 such that the statement holds. It can vary from line to line.
We fix a global parameter δ1 ą 0 on which the saving in Theorem 1.1 depends. We assume
that the final size of N in Theorem 1.1 is chosen sufficiently large in terms of δ1, whenever
necessary.
The letter R denotes major arc cutoff ranges and P , D denote sifting ranges and sifting
levels, respectively. The proof of Theorem 1.1 will involve certain parameter choices that
need to be powers of N that have suitable relative sizes. We state their final choices now,
but will restate them in the relevant lemmas and propositions.

Definition 2.1. We introduce the following parameters depending on N and δ1:

DM,1 “ N 1{3´δ1, DM,2 “ N 1{6´δ1, D1 “ N δ3
1 {100,

P0 “ N δ1, P1 “ N δ4
1 ,

R0 “ N δ3
1 , R1 “ N δ4
1 {100, rR “ N 2δ5
1 .

Then we have the hierarchy

DM,1 Ï DM,2 Ï P0 Ï R0 " D1 Ï P1 " R1 Ï rR.

2.3. Sieve definitions. As seen in the chain of inequalities following (1.12), pre- and main-
sieves play a crucial role in proving Theorem 1.1 and they will appear throughout the paper.
We now introduce relevant definitions and notation and give some motivation.
Generalising the notion of the Cram´er model, for P, Q ě 2, we define a normalised indicator
for integers with no prime factor in the interval rQ, P q as

rrQ,P qpnq :“ ź

QďpăP
 ˆ1 ´ 1
p
 ˙´1 1p∤n.

Thus
 rP pnq “ rr1,P qpnq.

8

With this normalisation, by the fundamental lemma of the sieve [4, Lemma 6.8], for N ě P
we have 1
N
 ÿ

nďN rP pnq “ 1 ` O ˆexp ˆ´1
2 log N
log P
 ˙ ` N ´1{2 log P ˙ .

Next we define pre-sieves that sift out primes up to P1 (where P1 and other parameters
are defined in Definition 2.1).

Definition 2.2 (Pre-sieves). Denote by ω and Ω the following normalised lower bound and
upper bound sieves. Define them to handle the primes 2 and 3 directly and sift for the
primes 5 ď p ă P1 “ N δ4
1 with a beta sieve with β “ 200 and level D1 “ N δ3
1 {100. That is,

ωpnq :“ 1pn,6q“1 ź

păP1
 ˆ1 ´ 1
p
 ˙´1 ÿ

d|n λ´pdq, Ωpnq :“ 1pn,6q“1 ź

păP1
 ˆ1 ´ 1
p
˙´1 ÿ

d|n λ`pdq,

where λ
˘pdq “ µpdq1d|ś
5ďpăP1 p1dPD˘ and D´, D` are given by [4, equation (6.55)] with
β “ 200.

Choosing pre-sieves as beta sieves gives us a convenient way of encoding a fundamental
lemma-type result; see Lemma 6.2. We choose the relatively large value β “ 200 to absorb
local density fluctuations of our additive problem of interest; see the proof of Proposition 6.3.
The normalisation is chosen so that, if D1 is large compared to P1, the pre-sieves have mean
1 ` op1q. The primes 2 and 3 are involved in the local solubility of our additive problem,
and it is technically easier to handle them separately. Observe that by definition,

ωpnq ď rP1pnq ď Ωpnq.

The complementary part to the pre-sieves of Definition 2.2 is played by main-sieves that sift
for primes larger than P1. It will be important that the weights of main-sieves have certain
factorisation properties. Recall that a function λ supported on r1, Ds is well-factorable if
for any R, S ě 1 with D “ RS we can write λ “ γ1 ‹ γ2 with γ1 and γ2 being bounded
coefficients, supported on r1, Rs and r1, Ss, respectively.

Definition 2.3 (Main-sieves). Let DM,1 “ N 1{3´δ1, DM,2 “ N 1{6´δ1, P1 “ N δ4
1 . We say fM is
a main-sieve, if for some |CfM| ! log N we have

fMpnq “ CfM ÿ

d|n λpdq,

where the function λ fulfils the following.
(1) λp1q “ 1 and λpdq ‰ 0 implies p ∤ d for all p ă P1.
(2) λ “ λ1 ‹ λ2 with |λipdq| ! τ pdq
Op1q, and λ1 is supported on r1, DM,1s, and λ2 is a sum
of Oδ1p1q many well-factorable functions supported on r1, DM,2s.

Condition (1) ensures a good saving when the main-sieves are removed in Proposition 5.1,
whereas the factorisation conditions in (2) make sure that Λpnqωpn ` 2q fulfils minor arc
bounds, see Lemma 5.8, which in particular uses work of Matom¨aki [14] on twisted Bombieri–
Vinogradov estimates. We remark that Definition 2.3 may be a misnomer in that it does
not include any requirement that fM should be a lower or upper bound sieve, making more
general functions admissible than classical sieves. These main-sieves will come up for us in
the construction of Chen’s minorant in Proposition 3.4. As is well known, the linear sieve
9

can be written as a sum of well-factorable weights (see Lemma 3.3). Thus, by choosing λ1 to
be trivial, it is a main-sieve as long as the sifting range does not include primes less than P1.
When we speak of the linear sieve, we always mean the version with well-factorable weights.

2.4. Approximations. As usual in an application of the circle method, the expected num-
ber of representations for the counting problem in Theorem 1.1 involves a singular series.
With our choice of normalisation, it is given by

Spmq :“ 1m”4 pmod 6q 27
2
 ź

pě5
 ˆ1 ´ 6p2 ´ 4p ` 1
pp ´ 1q4
 ˙ ź

pě5
p|mpm`4q
 ˆ1 ` 1
p ´ 4
 ˙ ź

pě5
p|m`2
 ˆ1 ` 2
p ´ 4
 ˙ .

(2.1)

We next define an approximation relation «ϵ, which is a rigorous version of the « relation
used in (1.13) to (1.15). Showing that certain functions approximate each other in this sense
is one of our central tasks.

Definition 2.4. Let ϵ ą 0 and f, g be finitely supported arithmetic functions. Let Ω denote
the upper bound pre-sieve from Definition 2.2. We write f «ϵ g if for every |hpnq| ď
ΩpnqΩpn ` 2q it holds that

ˇ
ˇ ÿ

n1`n2“m
N {2ăn1,n2ďN
pf ´ gqpn1qhpn2qˇ
ˇ ď ϵm
`Spmq ` 1
˘

for all m P r5N {4, 7N {4s with at most N 1´pδ1{10q4 exceptions.

2.5. Structure. In Section 3, we construct a version of Chen’s lower bound sieve that
includes a pre-sieving, in preparation for step (1.12). The key result for this is Proposition 3.4.
In Section 4, we gather some basic facts about Fourier approximation and how it relates
to our approximation notion «ϵ. These basic facts are then applied in Section 5 to show
how to replace the main-sieves in our additive problem with constants with respect to the
«ϵ notation, thus making step (1.13) rigorous. This is achieved in Proposition 5.1.
In Section 6, we consider our additive problem in the case where all constituents are pre-
sieves or |ΛR,r|. In particular, we show the more general version of (1.11) in Proposition 6.8
and obtain the asymptotics (1.16) in Proposition 6.3, from which (1.8) also follows.
In Section 7, we state and prove analogues of Gallagher’s prime number theorem for rP and
ΛE˚
3 . This is the place where Theorem 7.9, which is a more general version of Theorem 1.2,
is proved. From this we deduce that we can replace primes (respectively, E˚
3 numbers) with
the Cram´er model in our additive problem; see Propositions 7.10 and 7.11. They are precise
forms of (1.9) in the unexceptional and exceptional cases, respectively.
Finally, in Section 8 we combine the results of the previous sections to prove Theorem 1.1
in the way indicated in the steps leading to (1.16). The final proof can be described by the
following dependency diagram, where we combined pairs that correspond to unexceptional
or exceptional variants of the same statement into one node:
10

Lemma 6.7

Theorem 7.9

Theorem 1.2
 Propositions 7.10 / 7.11 Lemmas 8.3 / 8.4

Proposition 3.4

Proposition 5.1

Propositions 6.3 / 6.5
 Main Theorem 1.1

3. A variant of Chen’s sieve

In this section, we construct a sieve minorant for the Chen primes. Our minorant is closely
related to (a modern interpretation of) Chen’s original construction. More precisely, for the
most part we follow the construction of [17, Appendix A] to ensure that the required minor
arc bound can be shown. The main technical difference is that we include a pre-sieving
process.

3.1. Setup of the sieves. The sieving process for Chen primes involves classical upper and
lower bound sieves for rough numbers as well as numbers with precisely three prime factors
in certain ranges. The latter come into play to facilitate Chen’s sieve switching.

Definition 3.1. Let

B1 “ tp1p2p3 : N 1{10 ď p1 ă N 1{3´δ1 ď p2 ď pN {p1q1{2, p3 ě N 1{10u,(3.1)
 B2 “ tp1p2p3 : N 1{3´δ1 ď p1 ď p2 ď pN {p1q1{2, p3 ě N 1{10u,(3.2)

and define the related densities

cB1pnq “ ż
1{10ďt1ď1{3´δ1ďt2ďp1´t1q{2
log n
log N ´t1´t2ě1{10
 dt1 dt2
t1t2 logpn{N t1`t2q ,

cB2pnq “ ż
1{3´δ1ďt1ďt2ďp1´t1q{2
log n
log N ´t1´t2ě1{10
 dt1 dt2
t1t2 logpn{N t1`t2q ,

cE˚
3 pnq “ cB1pnq
2 ` cB2pnq.

Then we write
 ΛE˚
3 pnq “ 1nPB1{2 ` 1nPB2
cE˚
3 pnq .(3.3)

We also write cE˚
3 “ cE˚
3 pN q log N , noting that this is indeed a constant.

The choices of B1 and B2 are identical to [17, equations (6.2a), (6.2b)], and the normalisa-
tion function appears for the choice n “ N in [17, equation (6.3)]. It will be useful on several
occasions to note that cE˚
3 ptq is a smooth function. Furthermore, since for N 3{4 ď t ď 2N ,
11

the integration range of cBiptq becomes independent of t, one obtains the estimates

cE˚
3 ptq — 1
log N ,

d
dtcE˚
3 ptq ! 1
tplog N q2 .
(3.4)

One can show that a version of the Siegel–Walfisz theorem holds: if χ is any Dirichlet
character of modulus ď plog N q
A, we have

ÿ

nďN ΛE˚
3 pnqχpnq “ 1χ principal N ` OA
 ˆ N
plog N qA
 ˙ .

In fact, in Lemma 7.5 we show a version of Gallagher’s prime number theorem [5, Theorem
7] for ΛE˚
3 .

3.2. Construction of the minorant. To include pre-sieves, we use a vector sieve inequal-
ity. This standard idea of constructing a lower bound sieve by composition goes back at
least to Selberg [25].

Lemma 3.2 (Vector sieve inequality). Let A, B` ě 0 and A
`, A
´, B, B´ P R satisfy

B´ ď B ď B`

A
´ ď A ď A
`.

Then
 A
`B´ ` pA´ ´ A`qB` ď AB.

Proof. Since A ě 0, we have

AB ě AB´ “ A`B´ ` pA ´ A
`qB´.

As A ´ A
` ď 0, we can bound this from below by

ě A
`B´ ` pA ´ A`qB`.

Since B` ě 0, this is
 ě A`B´ ` pA
´ ´ A
`qB`,

as required. □

By Definition 2.3, the main-sieves in the construction of Chen’s minorant need to fulfil
certain factorisation properties. To achieve this we now record a version of the linear sieve
with well-factorable weights.

Lemma 3.3 (Well-factorable linear sieve). Let ε ą 0, D be sufficiently large in terms of
ε, and assume that Dε2 ď P ď z ď D1{p2`2ε9q. Let f psq and F psq be the functions of the
linear sieve defined by the systems [4, eq. (12.1), (12.2)]. Let Jpεq “ eCε´3 for an absolute
12

constant C ą 0. Then there exist well-factorable functions λ
˘
j pdq supported on d P r1, Ds and
d | ś

P ďpăz p such that
ÿ

jďJpεq
 ÿ

d|n λ´
j pdq ď 1p|n ùñ pRrP,zq ď ÿ

jďJpεq
 ÿ

d|n λ
`
j pdq,

ź

P ďpăz
 ˆ1 ´ 1
p
 ˙´1 ÿ

jďJpεq
 ÿ

d
 λ
´
j pdq
φpdq ě f ˆlog D
log z
 ˙ ` Opε5q,

ź

P ďpăz
 ˆ1 ´ 1
p
 ˙´1 ÿ

jďJpεq
 ÿ

d
 λ
`
j pdq
φpdq ď F ˆ log D
log z
 ˙ ` Opε5q.

Proof. The result follows the construction in [4, Section 12.7], with two differences: we skip
the pre-sieving (which actually simplifies the proof), and we make statements about the sieve
weights instead of the sifted set. We give the resulting details below.
We only consider the case of a lower bound sieve, the upper bound being very similar. By
the standard construction of the linear sieve (see [4, eq. (12.10)]) we have for any D0

1p|n ùñ pRrP,zq ě ÿ

d|n
dPD´pD0q
 µpdq1p|d ùñ pPrP,zq,

where D´pD0q is given by [4, eq. (12.32)] as

D´pD0q “ td “ p1 ¨ ¨ ¨ pr : p1 ą . . . ą pr, p1 ¨ ¨ ¨ pmp2
m ă D0 for all m evenu.

As shown in [4, Corollary 12.17], as long as z ă ?
D0, this set already enjoys good factorisa-
tion properties. To make use of those, we call r the number of prime divisors of d and split
the relevant primes into short intervals. Let η “ ε9, set D0 “ D1{p1`ηq, and let D1, . . . , Dr
run over numbers of the type P p1`ηqj . Define for even r

Dr “ tpD1, . . . , Drq : Dr ď . . . ď D1 ď a
D0, D1 . . . DmD2
m ă D0, m ď r, m evenu

and for odd r

Dr “ tpD1, . . . , Drq : Dr ď . . . ď D1 ď D0, D1 . . . DmD2
m ă D0, m ă r, m evenu.

Note that the condition m ” r pmod 2q in [4, eq. (12.84), (12.85)] is a typo. Similarly as
in [4, eq. (12.86)], we get

ÿ

d|n
dPD´pD0q
 µpdq1p|d ùñ pPrP,zq ě ÿ

rďlog D0{ log Pp´1q
r ÿ

pD1,...DrqPDr γpD1, . . . , Drq
´1 ÿ

p1¨¨¨pr|n
Dj ďpj ďmintD1`η
j ,zu
 1.
(3.5)

Here, since we drop the condition p1 ą . . . ą pr, we let γpD1, . . . , Drq “ k1! ¨ ¨ ¨ kℓ! account
for the multiplicity of the components if ki of the Dj are equal. We follow the argument
leading up to [4, eq. (12.91)]. The argument in [4, Lemma 12.16] shows that for each
fixed pD1, . . . Drq P Dr the sum over p1 ¨ ¨ ¨ pr is well-factorable. Thus, again accounting
for the multiplicity, we can write the right-hand side of (3.5) as a sum of at most e
Opε´3q

13

well-factorable functions ÿ

d|n λ´
j pdq

of level D supported on divisors of ś

P ďpăz p.
To complete the proof of the lemma, it remains to lower bound
ÿ

jďJpεq
 ÿ

d
 λ
´
j pdq
φpdq .

Observe that ź

P ďpăz
 ˆ1 ´ 1
p ´ 1
˙ “ `1 ` OpP ´1q˘ ź

P ďpăz
 ˆ1 ´ 1
p
 ˙ .

Thus, if we did not split into Dr and if we did not reduce the available level to D0 “ D1{p1`ηq,
the stated bound would follow directly from [4, eq. (12.5)]. To account for the splitting,
there are two terms to consider. The first comes from two prime divisors that are within
a ratio of Dη (or more precisely P η ă Dη, but this is inconsequential), the second from
boundary regions not covered precisely. Using P ě Dε2, both errors are shown to be Opε5q
after [4, eq. (12.88)] and [4, eq. (12.89)] respectively. Finally, the reduction of the level can
be absorbed by the smoothness of f , introducing another admissible Opηq error. □

We are now ready to construct a lower bound for the Chen primes and define

Λ2pnq :“ 1nPP2rN 1{10pnq,(3.6)

so that ΛpnqΛ2pn ` 2q becomes a weighted indicator of Chen primes (with the additional
restriction that n ` 2 is N 1{10-rough).

Proposition 3.4 (Chen’s lower bound sieve with pre-sieves). Assume that N is sufficiently
large, and let P1 “ N δ4
1 . There exist main-sieves

ωMpnq “ ÿ

d|n λ
ω
Mpdq,

ΩMpnq “ ÿ

d|n λ
Ω
Mpdq,

Ω
1
Mpnq “ ÿ

d|n λ
Ω1
M pdq,

as in Definition 2.3, and an error function Epnq such that the following three statements
hold.
(i) Let ω, Ω be pre-sieves as in Definition 2.2 and denote

g1pnq “ ΛpnqΩpn ` 2qωMpn ` 2q,

g2pnq “ p3{5 ` δ1qcE˚
3 ΩpnqΩMpnqΛE˚
3 pn ` 2q,

g3pnq “ Λpnq
`ω ´ Ω
˘pn ` 2qΩ
1
Mpn ` 2q.

We have for N {2 ă n ď N the inequality

ΛpnqΛ2pn ` 2q ě g1pnq ´ g2pnq ` g3pnq ` ΛpnqEpn ` 2q.(3.7) 14

(ii) The sieve weights fulfil

ź

P1ďpăN 1{10
 ˆ1 ´ 1
p
 ˙´1 ˜
ÿ

d
 λΩ1
M pdq
φpdq
 ¸
 ! 1,(3.8)
 and, if δ1 is sufficiently small, there exists an absolute constant c0 ą 0 such that

ź

P1ďpăN 1{10
 ˆ1 ´ 1
p
˙´1 ˜
ÿ

d
 λ
ω
Mpdq
φpdq ´ p3{5 ` δ1qcE˚
3 ÿ

d
 λ
Ω
Mpdq
φpdq
 ¸
 ě c0.(3.9)

(iii) We have the approximation

ΛpnqEpn ` 2q «N ´1{100 0(3.10)
 in the sense of Definition 2.4.

Proof. The proof is an incorporation of pre-sieves into the construction of [17, Appendix A].
In the case of lower bound sieves, Lemma 3.2 is used to facilitate this.
Recall the definition of Λ2 in (3.6). Similarly to [17, Appendix A.2] with B1 and B2 given
as in (3.1) and (3.2), we have for N {2 ă n ď N that

Λ2pnq ě rN 1{10pnq
 ¨

˚
˚
˝1 ´ 1
2
 ÿ

p|n
N 1{10ďpďN 1{3´δ1
 1 ´ 1
2 1nPB1 ´ 1nPB2 ´ E1pnq

˛

‹
‹
‚,(3.11)

where
 0 ď E1pnq ! ÿ

p2|n
pěN 1{10
 1

accounts for square divisors, and summing this bound gives ř

n„N E1pnq ! N ř

pěN 1{10 p´2 !
N 9{10, so Epnq :“ rN 1{10pnqE1pnq fulfils (3.10). Indeed, if n P pN {2, N s is square-free and
N 1{10-rough, then n has either two prime divisors from rN 1{10, N 1{3´δ1s or n “ p1p2p3 with
p2, p3 ą N 1{3´δ1. But then either n P B2 or n P B1 and p1 ď N 1{3´δ1. Thus, by (3.11) and
the definition of ΛE˚
3 in (3.3), we get

Λ2pnq ě rN 1{10pnq
 ¨

˚
˚
˝1 ´ 1
2
 ÿ

p|n
N 1{10ďpďN 1{3´δ1
 1

˛

‹
‹
‚´ cE˚
3 pnqΛE˚
3 pnq ´ Epnq,(3.12)

and then clearly (3.10) holds for this error function E. We rewrite the first component on
the right-hand side of (3.12) as

rN 1{10pnq
 ¨

˚
˚
˝1 ´ 1
2
 ÿ

p|n
N 1{10ďpďN 1{3´δ1
 1

˛

‹
‹
‚“ rP1pnq
 ¨

˚
˚
˝rrP1,N 1{10qpnq ´ 1
2
 ÿ

p|n
N 1{10ďpďN 1{3´δ1
 rrP1,N 1{10qpnq

˛

‹
‹
‚,

15

and next minorise this with the help of Lemma 3.2. Let

A “ rP1pnq,

B “ rrP1,N 1{10qpnq ´ 1
2
 ÿ

p|n
N 1{10ďpďN 1{3´δ1
 rrP1,N 1{10qpnq

with ω, Ω as in Definition 2.2. We choose

A
´ “ ωpnq,

A
` “ Ωpnq,

so that
 A
´ ď A ď A
`.

We lower bound B as in [17, Appendix A.3], using the well-factorable sieve from Lemma 3.3
with ε “ δ3
1. We apply a lower bound linear sieve of range rP1, N 1{10q and level N 1{2´2δ1 to
the first component. Separately for each p, we use an upper bound linear sieve with range
rP1, N 1{10q and level N 1{2´2δ1{p on rrP1,N 1{10q. The sum of both sieves (including summation
over p) is admissible for Definition 2.3, and so we get the existence of some main-sieve ωM
such that for
 B´ “ ωMpnq,

we have
 B´ ď B.

Clearly
 B ď rrP1,N 1{10qpnq ď Ω1
Mpnq :“ B`,

where Ω
1
M is the (well-factorable) upper bound linear sieve with range rP1, N 1{10q and level
N 1{2´2δ1. By the basic theory of the beta-sieve [4, Theorem 11.12] and Mertens’ theorem,
the left-hand side of (3.8) is bounded in absolute terms. Since A “ rP1pnq ě 0 and B` “
Ω
1
Mpnq ě rrP1,N 1{10qpnq ě 0, the hypotheses of Lemma 3.2 hold, and it gives

rN 1{10pnq
 ¨

˚
˚
˝1 ´ 1
2
 ÿ

p|n
N 1{10ďpďN 1{3´δ1
 1

˛

‹
‹
‚ě ΩpnqωMpnq ` pω ´ ΩqpnqΩ
1
Mpnq.(3.13)

Plugging this into (3.12), we get for N {2 ă n ď N ´ 2 that

ΛpnqΛ2pn ` 2q

ěg1pnq ` g3pnq ´ ΛpnqcE˚
3 pn ` 2qΛE˚
3 pn ` 2q ` ΛpnqEpn ` 2q.
(3.14)

We follow [17, Appendix A.4] to majorise

Λpnq ď plog N q ź

păN 1{6
 ˆ1 ´ 1
p
 ˙ ¨ rP1pnqrrP1,N 1{6qpnq ď plog N q ź

păN 1{6
 ˆ1 ´ 1
p
 ˙ ¨ ΩpnqΩMpnq,

16

where ΩM is the (well-factorable) upper bound linear sieve with range rP1, N 1{6q and level
N 1{2´2δ1. Observe further that by (3.4), we have cE˚
3 pn ` 2q “ cE˚
3 pN qp1 ` Opplog N q
´1qq
and recall that we write cE˚
3 pN q log N “ cE˚
3 . By Mertens’ theorem,

ź

păN 1{6
´
1 ´ 1
p
¯ “ ź

N 1{10ďpăN 1{6
´
1 ´ 1
p
 ¯ ź

păN 1{10
´
1 ´ 1
p
¯ “ ´3
5 ` Opδ1q
¯ ź

păN 1{10
´
1 ´ 1
p
 ¯
,

the middle factor tending to p1{10q{p1{6q “ 3{5. The remaining product ś

păN 1{10p1 ´ 1{pq
cancels against the normalisations built into Ωpnq and ΩMpnq, leaving exactly the factor
3{5 ` Opδ1q recorded in g2. We apply Mertens’ theorem and this approximation so that for
any δ1 ą 0 and N sufficiently large in terms of δ1, we have

ΛpnqcE˚
3 pn ` 2qΛE˚
3 pn ` 2q ďp3{5 ` δ1qcE˚
3 ΩpnqΩMpnqΛE˚
3 pn ` 2q

“g2pnq.

Together with (3.14) and since the contribution of n P tN ´ 1, N u can be absorbed in the
error term, this shows (3.7).
The proof of (3.9) follows from the calculations in [17, Appendices A.3, A.4, A.5]. Indeed
by Lemma 3.3, we have

ź

P1ďpăN 1{10
 ˆ1 ´ 1
p
 ˙´1 ÿ

d
 λω
Mpdq
φpdq ě f p5q ´ 1
2
 ÿ

N 1{10ďpăN 1{3´δ1
 F p5 ´ 10 log p{ log N q
φppq ´ Opδ1q

ě f p5q ´ 1
2
 ż 1{3

1{10 F p5 ´ 10tq dt
t ´ Opδ1q

and

3
5cE˚
3 ź

P1ďpăN 1{10
 ˆ1 ´ 1
p
 ˙´1 ÿ

d
 λΩ
Mpdq
φpdq ď 1
2 ¨ 3
5F p3q ż

1{10ďt1ď1{3ďt2ďp1´t1q{2
1´t1´t2ě1{10
 dt1 dt2
t1t2p1 ´ t1 ´ t2q ` Opδ1q.

That the difference of these is strictly positive for sufficiently small δ1 is stated explicitly in
[17, Appendix A.5]. □

We require one more type of main-sieve that majorises rrP1,P0q.

Lemma 3.5. Recall the parameter choices in Definition 2.1: P1 “ N δ4
1 , P0 “ N δ1, DM,1 “
N 1{3´δ1. There exist main-sieves
 ωrP1,P0qpnq “ ÿ

d|n λω
Mpdq,

ΩrP1,P0qpnq “ ÿ

d|n λΩ
Mpdq

such that
 ωrP1,P0qpnq ď rrP1,P0qpnq ď ΩrP1,P0qpnq(3.15)
 17

and ź

P1ďpăP0
´
1 ´ 1
p
 ¯´1 ÿ

d
 λΩ
Mpdq
φpdq “ 1 ` O`e´ log DM,1
40 log P0 ` δ15
1 ˘,

ź

P1ďpăP0
´
1 ´ 1
p
 ¯´1 ÿ

d
 λω
Mpdq
φpdq “ 1 ` O`e´ log DM,1
40 log P0 ` δ15
1 ˘.
(3.16)

Proof. We let ΩrP1,P0qpnq be the sum of the Oδ1p1q well-factorable upper-bound linear sieve
weights of Lemma 3.3 with sifting range rP1, P0q and level DM,1 “ N 1{3´δ1, normalised
by ś

P1ďpăP0`1 ´ 1{p˘´1; see Lemma 3.3. By construction, this fulfils (3.15). Since the
sifting range includes no primes less than P1 and the level is DM,1, this fits Definition 2.3.
The condition (3.16) follows from the basic theory of the linear sieve; see for example [4,
Theorem 11.12, eq. (11.134)]. Note that strictly speaking only one-sided inequalities are
proved there; the asymptotics follow from the fact that
ÿ

d
 λω
Mpdq
φpdq ď ÿ

d
 λ
Ω
Mpdq
φpdq .
 □

4. Fourier approximants

The fact that additive convolution translates to multiplication in Fourier space gives an
immediate way to show an approximation f «ϵ g (in the language of Definition 2.4) by
showing a power-saving estimate for

sup
α
 ˇ
ˇ
ˇ
ˇ
ˇ
ˇ
 ÿ

N {2ănďNpf ´ gqpnqepαnq

ˇ
ˇ
ˇ
ˇ
ˇ
ˇ .

In this section, we make this precise, gather some basic results about Fourier series, and
define the function bRpnq that replaces the classical major/minor arc decomposition.
We use the following notation to abbreviate the statements involving the Fourier series.

Definition 4.1 (Fourier norm). For a function f : N Ñ C, define its Fourier norm as

}f }
^
8 :“ sup
αPR
 ˇ
ˇ
ˇ
ˇ
ˇ
ˇ
 ÿ

N {2ănďN f pnqepαnq
ˇ
ˇ
ˇ
ˇ
ˇ
ˇ .

Note that this differs from the similar notation in [7, Section 8.1]. We first show that
closeness in Fourier norm implies the approximation relation of Definition 2.4. Recall for
this that δ1 is a global parameter that also appears in that definition, as it will fix the
quantitative thresholds in the lemma below.

Lemma 4.2 (Fourier-closeness implies «). Let f1, f2 : N Ñ C. If

}f1 ´ f2}^
8 ! N 1´2pδ1{10q4,

then for ϵ " N ´pδ1{10q4 we have
 f1 «ϵ f2.
18

Proof. In view of Definitions 2.4 and 4.1, we can assume that all involved functions are
supported on n P pN {2, N s only.
Let η “ N ´2pδ1{10q4. Write f “ f1 ´ f2 and let g : pN {2, N s Ñ C be any function. By the
assumption of the lemma we have

sup
αPR
 ˇ
ˇ
ˇ
ˇ
ˇ
ˇ
 ÿ

N {2ănďN f pnqepαnq
ˇ
ˇ
ˇ
ˇ
ˇ
ˇ ď ηN.(4.1)

We will show that for all but at most η2{3N integers m P r5N {4, 7N {4s, we have

|f ˚ gpmq| ď η2{3N 1{2}g}2.

This implies the lemma: the exceptional count η2{3N “ N 1´ 4
3 pδ1{10q4 ď N 1´pδ1{10q4 is within
the allowance of Definition 2.4, as the functions required for Definition 2.4 fulfil }g}2 ď
N 1{2`op1q.
Let S Ă r5N {4, 7N {4s be the set of m for which

|f ˚ gpmq| ą η2{3N 1{2}g}2.

Pick unimodular complex numbers cm such that

cmpf ˚ gpmqq ą η2{3N 1{2}g}2
for m P S.
Then, summing over m P r5N {4, 7N {4s and applying the orthogonality of characters, we
obtain
 η2{3N 1{2}g}2|S| ă ÿ

n1,n2PpN {2,N s f pn1qgpn2qcn1`n21Spn1 ` n2q

“ ż 1

0 F pαqGpαqSp´αq dα,
(4.2)

where
 F pαq :“ ÿ

N {2ănďN f pnqepnαq,

Gpαq :“ ÿ

N {2ănďN gpnqepnαq,

Spαq :“ ÿ

n cn1Spnqepnαq.

Now, by the assumption (4.1), we can apply Cauchy–Schwarz and Parseval’s identity
to (4.2) to conclude that

η2{3N 1{2}g}2|S| ď ηN ˆż 1

0 |Gpαq|2 dα˙1{2 ˆż 1

0 |Spαq|2 dα˙1{2

ď ηN }g}2|S|1{2.

This implies
 |S| ď η2{3N,

as desired. □
19

The next lemma allows us to estimate trivially the effect of twisting by a sieve or character
when calculating the Fourier norm.

Lemma 4.3 (Fourier properties of sieve and character twists). Let f : N Ñ C be of the form
f pnq “ 1 ‹ λpnq “ ř

d|n λpdq for some arithmetic function λ. Let χ be a primitive Dirichlet
character of conductor r P N. Then for any arithmetic function g, we have

}f g}
^
8 ď }λ}1}g}^
8
}χg}
^
8 ď ?
r}g}
^
8.

Proof. By the definition of the Fourier norm, we can assume that g is supported on pN {2, N s
and in particular any sum over gpnq is convergent. We open the definition of f to get

sup
αPR
 ˇ
ˇ
ˇ
ˇ
ˇ
ÿ

n f pnqgpnqepαnq

ˇ
ˇ
ˇ
ˇ
ˇ “ sup
α
 ˇ
ˇ
ˇ
ˇ
ˇ
ˇ
ÿ

d λpdq ÿ

n”0 pmod dq gpnqepαnq

ˇ
ˇ
ˇ
ˇ
ˇ
ˇ

“ sup
αPR
 ˇ
ˇ
ˇ
ˇ
ˇ
ˇ
ÿ

d
 λpdq
d
 ÿ

bpdq
 ÿ

n gpnqeppα ` b{dqnq

ˇ
ˇ
ˇ
ˇ
ˇ
ˇ

ď ÿ

d |λpdq| sup
αPR
 ˇ
ˇ
ˇ
ˇ
ˇ
ÿ

n gpnqepαnq

ˇ
ˇ
ˇ
ˇ
ˇ

“ }λ}1}g}
^
8.

For the second statement, we use the well known estimate for Gauss sums that gives for
primitive characters
 max
bprq
 ˇ
ˇÿ

aprq χpaqerpabq
ˇ
ˇ ď r1{2.

Indeed, this follows for pb, rq “ 1 from [21, Lemma 5.1] and for pb, rq ‰ 1, the sum vanishes.
Thus,
 sup
αPR
 ˇ
ˇ
ˇ
ˇ
ˇ
ÿ

n χpnqgpnqepαnq

ˇ
ˇ
ˇ
ˇ
ˇ “ sup
αPR
 ˇ
ˇ
ˇ
ˇ
ˇ
ˇ
1
r
 ÿ

bprq
 ÿ

aprq χpaqerp´abq ÿ

n gpnqeppα ` b{rqnq

ˇ
ˇ
ˇ
ˇ
ˇ
ˇ

ď 1
r
 ÿ

bprq
 ˇ
ˇ
ˇ
ˇ
ˇ
ˇ
ÿ

aprq χpaqerp´abq

ˇ
ˇ
ˇ
ˇ
ˇ
ˇ sup
βPR
 ˇ
ˇ
ˇ
ˇ
ˇ
ÿ

n gpnqepβnq

ˇ
ˇ
ˇ
ˇ
ˇ

ď ?
r}g}
^
8.

This completes the proof. □

We now define our notion of major arcs of order R and the related function bR.

Definition 4.4 (Major and minor arcs). Define the major arcs of order R ě 1 by

MpRq :“ r0, 1q X ď

1ďqďR
 ď

bPZ
pb,qq“1
 „ b
q ´ R
N , b
q ` R
N
 ȷ

20

and the minor arcs by
 mpRq :“ r0, 1qzMpRq.

We also write
 }f }
^
MpRq :“ sup
αPMpRq
 ˇ
ˇ
ˇ
ˇ
ˇ
ˇ
 ÿ

N {2ănďN f pnqepαnq
ˇ
ˇ
ˇ
ˇ
ˇ
ˇ ,

}f }
^
mpRq :“ sup
αPmpRq
 ˇ
ˇ
ˇ
ˇ
ˇ
ˇ
 ÿ

N {2ănďN f pnqepαnq

ˇ
ˇ
ˇ
ˇ
ˇ
ˇ .

Definition 4.5 (Physical-space major-arc kernel bR). Let G be a fixed smooth and non-
negative function that is supported in r´2, 2s and is equal to 1 in r0, 1s, and let R ě 2.
Define
 bRpnq :“ ÿ

rě1
 ÿ˚

b pmod rq erpbnq1|n|ďN {R4 R4

2N G
` log r
log R
 ˘.

The important property for us is that |pbRpαq ´ 1| is small for α P MpRq.

Lemma 4.6 (bR extracts the major arc contribution). Let f be any arithmetic function
supported on pN {2, N s, and assume that 2 ď R ď N 1{11. We have

}f ´ f ˚ bR}
^
8 ! }f }
^
mpRq ` }f }1
R ` }f }8N log R
R2 .

Proof. We first note that by the support condition of f and Definition 4.5, we have the trivial
upper bound

|f ˚ bRpnq| “
ˇ
ˇ ÿ

n1`n2“n f pn1qbRpn2qˇ
ˇ

ď}f }81nPpN {2´N {R4,N `N {R4s R4

2N
 ÿ

|n´n1|ďN {R4
 ÿ

rďR2 |crpn ´ n1q|

!}f }81nPpN {2´N {R4,N `N {R4sR2 log R.

Here we used |crpn2q| ď pr, n2q with n2 “ n ´ n1, and that the bound ř

rďR2 |crpn2q| !
R2 log R holds on average over the range |n2| ď N {R4 present in the display. Indeed, writing
pr, n2q “ ř

d|pr,n2q φpdq and summing over n2 first,

ÿ

|n2|ďN {R4
 ÿ

rďR2pr, n2q “ ÿ

rďR2
 ÿ

d|r φpdq ÿ

|n2|ďN {R4
d|n2
 1 ! N
R4 ÿ

rďR2
 ÿ

d|r
 φpdq
d “ N
R4 ÿ

dďR2
 φpdq
d
 YR2

d
 ] ! N
R4 R2 log R,

21

using ř
dďR2 φpdq{d
2 ď ř

dďR2 1{d ! log R. Multiplying by the prefactor R4{p2N q gives the
pointwise bound }f }8R2 log R. We use this to estimate
ˇ
ˇ
ˇÿ

n pf ˚ bRqpnqepαnq ´ ÿ

N {2ănďNpf ˚ bRqpnqepαnq
ˇ
ˇ
ˇ

ď ÿ

nďN {2 |pf ˚ bRqpnq| ` ÿ

nąN |pf ˚ bRqpnq|

!}f }8N log R
R2 .

Thus, up to an admissible error we can replace
ÿ

N {2ănďNpf ˚ bRqpnqepαnq

by ÿ

n pf ˚ bRqpnqepαnq “ pf pαqpbRpαq.

Here pf is the unrestricted Fourier transform, which agrees with the one of Definition 4.1
because f is supported on pN {2, N s. Consequently, the lemma follows if we can show that

pbRpαq “
 #
1 ` Op1{Rq if α P MpRq
Op1q if α P mpRq.
(4.3)

Given α P R, let a P Z, q P N be such that |a{q ´ α| is minimal among all choices with
pa, qq “ 1, q ď R2. Write β “ α ´ a{q so that

pbRpαq “ R4

2N G
` log q
log R
 ˘ ÿ

|n|ďN {R4 ep´βnq ` ÿ

rě1
 ÿ

1ďbăr
pb,rq“1
b{r‰a{q
 G
` log r
log R
 ˘ R4

2N
 ÿ

|n|ďN {R4 e`pα ´ b{rqn
˘.

(4.4)

As the points b{r with pb, rq “ 1 and r ď R2 are 1{R4 well spaced, in the second sum on the
right-hand side of (4.4) we have |α ´ b{r| " 1{R4 and can estimate it by
ˇ
ˇ
ˇ
ˇ
ˇ
ˇ
ˇ
ˇ
ˇ
ˇ
ÿ

rě1
 ÿ

1ďbăr
pb,rq“1
b{r‰a{q
 G
` log r
log R
 ˘ R4

2N
 ÿ

|n|ďN {R4 e
`pα ´ b{rqn˘
ˇ
ˇ
ˇ
ˇ
ˇ
ˇ
ˇ
ˇ
ˇ
ˇ
 ! ÿ

rě1 G
` log r
log R
 ˘ R4

2N
 `R4 ` ÿ

1ďbďr
 r
b
 ˘

! R8

N
 ÿ

rďR2 G
` log r
log R
 ˘

! R10

N

! 1
R ,

22

where we used that R11 ď N . Furthermore, the first term on the right-hand side of (4.4) is
always ! 1 in absolute value. Hence pbRpαq ! 1 for α P mpRq, which is the α P mpRq case
of (4.3).
If α P MpRq, then q ď R and |β| ď R{N in (4.4). In this case we have |βn| ď 1{R3 and a
Taylor expansion gives us

R4

2N G
` log q
log R
 ˘ ÿ

|n|ďN {R4 ep´βnq “ R4

2N
 ÿ

|n|ďN {R4
`1 ` Op1{R3q
˘

“ 1 ` Op1{Rq.

Hence pbRpαq “ 1 ` Op1{Rq for α P MpRq, which is the α P MpRq case of (4.3). □

The next lemma reduces major arc behaviour to short interval twists with multiplicative
characters.

Lemma 4.7 (Reduction to multiplicative characters). Let 1 ď R ď N 1{3 and let f be an
arithmetic function supported on R-rough integers in pN {2, N s. Then we have

}f }^
MpRq ! R5{2 max
N {2´N {R2ďnďN `N {R2 max
qďR,
χ pmod qq
χ primitive
 ˇ
ˇ
ˇ
ˇ
ˇ
ˇ
 ÿ

|n1´n|ďN {R2 f pn1qχpn1q
ˇ
ˇ
ˇ
ˇ
ˇ
ˇ ` }f }1{R ` }f }8 N
R2 .

Proof. Since f is supported in pN {2, N s, we can write pf for the associated Fourier series and
have
 }f }
^
MpRq “ sup
αPMpRq

ˇ
ˇ
ˇÿ

n f pnqepαnq
ˇ
ˇ
ˇ “ sup
αPMpRq
ˇ
ˇ
ˇ pf pαq
ˇ
ˇ
ˇ.

We set
 bq,apnq :“ R2

2N 1|n|ďN {R2eqp´anq

and observe that xbq,apαq “ 1 ` OpR´1q

for |α ´ a{q| ď R{N , by the same arguments as leading to the major arc case of (4.3).
Recalling Definition 4.4, we then get

sup
αPMpRq

ˇ
ˇ
ˇ pf pαq
ˇ
ˇ
ˇ “ max
qďR
pa,qq“1 sup
|α´a{q|ďR{N | pf pαq|

! max
qďR
pa,qq“1 sup
|α´a{q|ďR{N | {f ˚ bq,apαq| ` }f }1{R.

By discarding some terms trivially — f ˚ bq,a is supported on pN {2 ´ N {R2, N ` N {R2s
with |f ˚ bq,apnq| ď }f }8 there, so restricting to N {2 ă n ď N costs only the two boundary
intervals of total length OpN {R2q — we can write

{f ˚ bq,apαq “ ÿ

N {2´N {R2ďnďN `N {R2 f ˚ bq,apnqepαnq ` O ˆ}f }8 N
R2
 ˙

23

and thus

sup
|α´a{q|ďR{N
 ˇ
ˇ
ˇ
ˇ
ˇ
 ÿ

N {2´N {R2ďnďN `N {R2 f ˚ bq,apnqepαnq

ˇ
ˇ
ˇ
ˇ
ˇ ď 2N max
N {2´N {R2ďnďN `N {R2 |f ˚ bq,apnq|.

We denote by τ pχq the usual Gauss sum. Since f is supported on R-rough integers, for
f pn
1q ‰ 0 we have pn1, qq “ 1 for q ď R, so that eqpan1q “ 1
φpqq ř

χpqq τ p ¯χqχpaqχpn1q. Thus

|f ˚ bq,apnq| “ R2

2N
 ˇ
ˇ
ˇ
ˇ
ˇ
ˇ
 ÿ

|n1´n|ďN {R2 f pn
1qeqpan
1q
ˇ
ˇ
ˇ
ˇ
ˇ
ˇ

“ R2

2N φpqq
 ˇ
ˇ
ˇ
ˇ
ˇ
ˇ
 ÿ

χpqq τ pχqχpaq ÿ

|n1´n|ďN {R2 f pn1qχpn1q
ˇ
ˇ
ˇ
ˇ
ˇ
ˇ

ď R2q1{2

N max
χ pmod qq
χ primitive
 ˇ
ˇ
ˇ
ˇ
ˇ
ˇ
 ÿ

|n1´n|ďN {R2 f pn1qχpn1q
ˇ
ˇ
ˇ
ˇ
ˇ
ˇ .

In the last step, each character χ pmod qq agrees on the support of f with the primitive
character χ
˚ inducing it, and we bounded |τ pχq| ď q1{2 before maximising over these primitive
characters. Recalling that we take the maximum over q ď R, the lemma follows. □

The next lemma allows us to move a smooth function inside the convolution with bR,
provided its derivative is not too large. We require it only in the proof of Proposition 7.8
to move factors of n rβ´1 (where rβ is the exceptional zero of Definition 7.1) in or out of the
convolution.

Lemma 4.8. Let ψ be a smooth function, g any arithmetic function, N {2 ă n ď N and
R ě 2. Then we have

ψpnqpg ˚ bRqpnq “ pψgq ˚ bRpnq ` O ˆ N log R
R2 }ψ11rN {3,2N s}8}g}8
˙ .

Proof. Since R ě 2, Definition 4.5 gives that bR is supported on |m| ď N {R4 ď N {16, so
|t ´ n| ď N {R4 implies t P rN {3, 2N s. By the mean value theorem we have

ψpnqpg ˚ bRqpnq ´ pψgq ˚ bRpnq

“ ÿ

|m|ďN {R4pψpnq ´ ψpn ´ mqqgpn ´ mqbRpmq

! sup
|t´n|ďN {R4 |ψ1ptq| ÿ

|m|ďN {R4 |mgpn ´ mqbRpmq|

!}ψ11rN {3,2N s}8}g}8 ÿ

|m|ďN {R4 |m||bRpmq|

!}ψ11rN {3,2N s}8}g}8 R4

N
 ÿ

|m|ďN {R4 |m| ÿ

rďR2pr, mq

!N log R
R2 }ψ11rN {3,2N s}8}g}8,

24

as desired. Here we used |crpmq| ď pr, mq and, with M “ N {R4, the estimates ř

|m|ďM |m|pr, mq ď

2M 2 ř
d|r φpdq
d ď 2M 2τ prq and ř

rďR2 τ prq ! R2 log R. □

For functions that are supported on rough numbers, we now rewrite their convolution with
bR in terms of multiplicative characters.

Definition 4.9 (Smooth Heath–Brown kernel ΛR,r). Recall that G is the fixed smooth
function of Definition 4.5. For r ě 1 we set

ΛR,rpnq :“ ÿ

q
pq,rq“1
 µpqqcqpnq
φpqq G
`log rq
log R
 ˘.(4.5)

Then we have the following lemma; see [7, eq. (6.6)] for the analogue in Green’s work.

Lemma 4.10. Let R ě 2. Let f be any arithmetic function supported on R2-rough integers
only. For N {2 ă n ď N , we have

f ˚ bRpnq “ ÿ

rďR2
 ÿ˚

χ pmod rq χpnq r
φprq ΛR,rpnq R4 ř

|n1´n|ďN {R4 f pn1qχpn1q

2N .(4.6)

Proof. By definition

f ˚ bRpnq “ ÿ

r G
` log r
log R
 ˘ R4

2N
 ÿ

|n1´n|ďN {R4 f pn
1qcrpn ´ n1q.

By the support condition of G, we have r ď R2 and so pn
1, rq “ 1. We rewrite Ramanujan’s
sum as crpmq “ ř

d|pr,mq µpr{dqd and get

f pn1qcrpn ´ n1q “ ÿ

d|pr,n´n1q µpr{dqd ¨ f pn
1q

“ ÿ

d|r µpr{dqd1n1”n pmod dqf pn1q

“ ÿ

d|r
 µpr{dqd
φpdq
 ÿ

χpdq χpnqχpn
1qf pn1q

“ ÿ

s|r
 ÿ˚

χ pmod sq χpnqχpn
1qf pn1q ÿ

d1
d1|r{s
 µpr{psd1qqsd
1

φpsd1q

“ ÿ

s|r
ps,r{sq“1
 ÿ˚

χ pmod sq χpnqχpn1qf pn1q s
φpsq
 ÿ

d1|r{s
 µppr{sq{d1qd
1

φpd1q 1pn,d1q“1

“ ÿ

s|r
ps,r{sq“1
 ÿ˚

χ pmod sq χpnq s
φpsq µpr{sqcr{spnq
φpr{sq f pn1qχpn
1q,

where we sorted the d | r sum by conductor: each χ pmod dq is induced by a unique primitive
character χ
˚ pmod sq with s | d, and χpnq “ χ
˚pnq1pn,dq“1 while χpn1q “ χ
˚pn1q since pn1, rq “
1, so writing d “ sd1 with d1 | r{s leaves the inner sum over d1, in which only squarefree r{s
25

coprime to s survive. This inner sum ř

d1|r{s µppr{sq{d1qd1

φpd1q 1pn,d1q“1 is multiplicative in m “ r{s.

At m “ p it equals µppq ` p
φppq 1p∤n, which is 1
p´1 if p ∤ n and ´1 if p | n, both equal to µppqcppnq
φppq ,
while at prime powers pk with k ě 2 it vanishes, as does µppkq. Multiplying over p | m gives
µpr{sqcr{spnq
φpr{sq , using also that pn, sq “ 1 in the support of the sum. Summing over n
1 and r now
gives the result. □

In the proof of Theorem 1.2 or the more general Theorem 7.9, we will show that |ΛR,r| is
bounded by HR and so behaves Cram´er-like.
We next provide a suitable multiplicative upper bound for |ΛR,r| to be used together with
Lemma 6.7. It involves the function HR defined in Theorem 1.2.

Lemma 4.11. For n P N and r ď R2, we have

1pn,rq“1 r
φprq |ΛR,rpnq| ď HRpnq.

Proof. We may assume that pn, rq “ 1, as otherwise the claim is trivial. Using the formula

cqpnq “ ÿ

d|pq,nq dµ ´ q
d
¯

for Ramanujan sums (which is easily verified by noting that both sides are multiplicative in
q), we can write
 ΛR,rpnq “ ÿ

d|n dµpdq ÿ

q”0 pmod dq
pq,rq“1
 µpqq2

φpqq G ˆlogpqrq
log R
 ˙

“ ÿ

d|n
pd,rq“1
 dµpdq
φpdq
 ÿ

ℓ
pℓ,drq“1
 µpℓq
2

φpℓq G ˆ logpℓdrq
log R
 ˙ ,(4.7)

where, writing the square-free q with d | q as q “ dℓ with pd, ℓq “ 1, we used µpqqµpq{dq “
µpdqµpqq
2 to extract dµpdq and the multiplicativity φpdℓq “ φpdqφpℓq, µpdℓq
2 “ µpℓq
2. To
proceed further, we follow a Fourier-analytic approach similar to [24, equation (37)]. Let ψ
be the Fourier transform of t ÞÑ e
tGptq. Then by Fourier inversion for x P R we have

exGpxq “ ż

R ψpξqe´iξx dξ.(4.8)

By the smoothness of G, for any B ą 0 we have ψptq !B p1`|t|q´B. Plugging (4.8) into (4.7),
we get
 ΛR,rpnq “ ż
R ψpξqr´p1´iξq{ log R ÿ

d|n
pd,rq“1
 dµpdq
φpdqdp1´iξq{ log R ÿ

ℓ
pℓ,drq“1
 µpℓq2

φpℓqℓp1´iξq{ log R dξ.

Thus, the lemma follows if we can show that the double sum over d, ℓ is bounded by
ˇ
ˇ
ˇ ÿ

d|n
pd,rq“1
 dµpdq
φpdqdp1´iξq{ log R ÿ

ℓ
pℓ,drq“1
 µpℓq2

φpℓqℓp1´iξq{ log R
 ˇ
ˇ
ˇ ! φprq
r τ pnqplog Rqhξpnq,(4.9)
 26

with a multiplicative function hξ given on the primes by

hξppq “ min
!
1, 10p1 ` |ξ|q log p
log R
 )
.

We successively write the summations over ℓ and d as products so that
ÿ

d|n
pd,rq“1
 dµpdq
φpdqdp1´iξq{ log R ÿ

ℓ
pℓ,drq“1
 µpℓq
2

φpℓqℓp1´iξq{ log R

“ ÿ

d|n
pd,rq“1
 dµpdq
φpdqdp1´iξq{ log R ź

p1∤dr
´
1 ` 1

pp1 ´ 1qpp1´iξq{ log R
1
 ¯

“ ź

p1∤r
´
1 ` 1

pp1 ´ 1qpp1´iξq{ log R
1
 ¯ ź

p2|n
p2∤r
 ˜

1 ´ p2
pp2 ´ 1qpp1´iξq{ log R
2
 ´
1 ` 1

pp2 ´ 1qpp1´iξq{ log R
2
 ¯´1¸

“ ź

p1∤rn
´
1 ` 1

pp1 ´ 1qpp1´iξq{ log R
1
 ¯ ź

p2|n
p2∤r
 ˜

1 ´ 1

pp1´iξq{ log R
2
 ¸
 .

Here the last equality uses the identity `1 ` 1
pp2´1qps
2 ˘`1 ´ p2
pp2´1qps
2 `1 ` 1
pp2´1qps
2 ˘´1˘ “ 1 ´ p´s
2
with s “ p1 ´ iξq{ log R, the factor 1 ` 1
pp2´1qps
2 for each p2 | n being drawn from the product
over p1. To estimate the product over p1, we first note that since r ď R2 we have

r
φprq
 ź

p|r
 ´
1 ` 1
pp ´ 1qpp1´iξq{ log R
 ¯´1 ! ź

p|r
 ´
1 ` 1
p ´ 1
 ¯´
1 ` 1
pp ´ 1qp1{ log R
 ¯´1

! ź

p|r
 ´
1 ` 1 ´ p´1{ log R

p ´ 1
 ¯

! ź

p|r
 ´
1 ` O` log p
p log R
 ˘¯

! exp
´
O` ÿ

pďlog r
 log p
p log R
 ˘¯

! 1.

Thus the product over p1 can be estimated by
ˇ
ˇ
ˇ ź

p1∤rn
´1 ` 1

pp1 ´ 1qpp1´iξq{ log R
1
 ¯ˇ
ˇ
ˇ ď ź

p1∤r
´1 ` 1

pp1 ´ 1qp1{ log R
1
 ¯

! φprq
r exp
 ˜
ÿ

p1 p´1´1{plog Rq
1
 ¸

! φprq
r log R.

27

We next consider the factor involving p2. By using a trivial bound in the case that p1 `
|ξ|q log p2
log R ą 1{10 and Taylor approximation in the remaining case, we get
ˇ
ˇ
ˇ
ˇ
ˇ1 ´ 1

pp1´iξq{ log R
2
 ˇ
ˇ
ˇ
ˇ
ˇ ď 2 min
!
1, 10p1 ` |ξ|q log p2
log R
 )
.

The bound (4.9) and with it the lemma follows. □

5. Main-sieve removal

The functions g1, g2, g3 in Proposition 3.4 are products of Λ or ΛE˚
3 with a main-sieve and a
pre-sieve or a difference of pre-sieves. In this section, our goal is to show that the main-sieve
component can be replaced by a constant, in the approximate sense of Definition 2.4. We do
so in the generality Λ
˚ P tΛ, ΛE˚
3 , rP1u, as the case Λ˚ “ rP1 is needed later for the Cram´er
model.

Proposition 5.1 (Main-sieve removal). Assume the following conditions.

‚ Λ˚ P tΛ, ΛE˚
3 , rP1u with P1 “ N δ4
1 .
‚ fMpnq “ ř

d|n λMpdq is a main-sieve as in Definition 2.3.
‚ fPre P tω, Ωu is a pre-sieve.

Let ϵ ě N ´pδ1{10q4. Then we have

Λ˚pnqfMpn ` 2qfPrepn ` 2q «ϵ
 ¨

˝ ź

P1ďpăN 1{10
 ˆ1 ´ 1
p
 ˙´1 ÿ

d
 λMpdq
φpdq
 ˛

‚Λ˚pnqfPrepn ` 2q

and similarly with the roles of n and n ` 2 reversed. Let further χ be a primitive quadratic
character with conductor at most rR “ N 2δ5
1 and let cpnq “ 1χpnq“´1 or cpnq “ 1χpnq“χpn`2q“1.
Expanding these indicators into characters via 1χpnq“´1 “ 1
2p1 ´ χpnqq and 1χpnq“χpn`2q“1 “
1
4p1 ` χpnqqp1 ` χ`pnqq produces the four twists b P t1, χ, χ`, χχ
`u met below. We have

cpnqΛ˚pnqfMpn ` 2qfPrepn ` 2q «ϵ cpnq
 ¨

˝ ź

P1ďpăN 1{10
 ˆ1 ´ 1
p
 ˙´1 ÿ

d
 λMpdq
φpdq
 ˛

‚Λ˚pnqfPrepn ` 2q

and similarly with the roles of n and n ` 2 reversed.

We make two remarks on this. First, the proof does not require the pre-sieves to be
precisely as in Definition 2.2, any arithmetic function that is of the form λ ‹ 1 with a
bounded function λ that is supported on P1-smooth integers d ď D1 would do. Second,
the parts of the statement involving a quadratic character χ are required to deal with a
possible exceptional character.
We consider only the case of the roles of n, n ` 2 as in the displays of the proposition;
the reversed role case works the same way. By Lemma 4.2, Proposition 5.1 follows if we can
show
 }bΛ˚pfM ´ cMq`f `
Pre}
^
8 ! N 1´2pδ1{10q4,(5.1)
 28

where
 cM “ ź

P1ďpăN 1{10
 ˆ1 ´ 1
p
 ˙´1 ÿ

d
 λMpdq
φpdq
(5.2)

and b P t1, χ, χ`, χχ
`u. Then, applying Lemma 4.3 (possibly twice) together with the
assumed bound for the conductor of χ, we see that it suffices to show

}Λ˚pfM ´ cMq
`f `
Pre}^
8 ! N 1´3pδ1{10q4.

With the help of the triangle inequality, this follows from the following separate major and
minor arc statements:
 }Λ˚pfM ´ cMq
`f `
Pre}^
MpR1q ! N 1´3pδ1{10q4,(5.3)
 }Λ˚f `
Mf `
Pre}
^
mpR1q ` |cM|}Λ˚f `
Pre}
^
mpR1q ! N 1´3pδ1{10q4.(5.4)

In the next four subsections, we first import some routine combinatorial decompositions,
and then show a variant of the Bombieri–Vinogradov theorem with a power saving. After-
wards we apply it to obtain the major arc case bound (5.3). Finally, we prove the comple-
menting minor arc bound (5.4) with the help of Bombieri–Vinogradov type estimates twisted
by minor arc additive phases based on [14].

5.1. Combinatorial decompositions. For both major and minor arc bounds, we rely on
type I and II sum decompositions for the relevant Λ
˚ functions.
To handle some of the smooth normalisations (like log n or cE˚
3 pnq), we first state a simple
consequence of partial summation.

Lemma 5.2. Let panqnPN be a sequence of complex numbers and let f be a smooth function
such that for t P r
?
N , N s we have
 |f ptq| — log N,

|f 1ptq| ! 1{t.

Then we have ˇ
ˇ
ˇ ÿ

?
N ănďN anˇ
ˇ
ˇ ! 1
log N max?
N ăξďN
ˇ
ˇ
ˇ ÿ

?
N ănďξ anf pnq
ˇ
ˇ
ˇ,

ˇ
ˇ
ˇ ÿ

?
N ănďN anf pnqˇ
ˇ
ˇ ! log N max?
N ăξďN
ˇ
ˇ
ˇ ÿ

?
N ănďξ anˇ
ˇ
ˇ.

Lemma 5.3 (Combinatorial decomposition). Let pγnqnPN be a sequence of complex numbers.
Let Λ˚ P tΛ, ΛE˚
3 , rP u with P ă N 1{3. Let Q ď N 1{10 and N {2 ă N 1 ď N . Assume we have
the following type I and II estimates:
ˇ
ˇ
ˇ ÿ

N1{2ăn1ďN1
N {2ăn1n2ďξ
 an1bn2γn1n2ˇ
ˇ
ˇ ! N Q´1,

whenever N1 ď N 1{3, ξ ď N 1, |an| ď τ pnq log n and bn ” 1 or bn ” log n;
ˇ
ˇ
ˇ ÿ

N1{2ăn1ďN1
N2{2ăn2ďN2
 an1bn2γn1n2ˇ
ˇ
ˇ ! N Q´1,

29

whenever N {2 ă N1N2 ă 4N 1 and N1 P rN 1{3, 2N 1{2s, |an|, |bn| ď τ pnq log n.
Then we have that ˇ
ˇ
ˇ ÿ

N {2ănďN 1 Λ˚pnqγnˇ
ˇ
ˇ ! N 1`op1qQ´1.

Proof. We consider separately the case of each choice for Λ
˚.
The case of Λ.
When Λ˚ “ Λ, we use Vaughan’s identity [4, Cor. 17.4] to obtain
ÿ

N {2ănďN 1 Λpnqγn ! T1 ` T2,

where
 T1 “ ÿ

N {2ănďN 1 log n γn ÿ

b|n
bďpN {2q1{3
 µpbq

and
 T2 “ ÿ

N {2ănďN 1 γn ÿ

bc“n
b,cąpN {2q1{3
 αbβc

for some |αb| ď 1, |βc| ď log c. Writing log n “ log b ` logpn{bq, we can estimate T1 with the
type I bound. For T2, we split b, c into dyadic intervals pN1{2, N1s, pN2{2, N2s and observe
that the sum is empty unless N {2 ă N1N2 ă 4N 1. Next, we denote by }θ} the distance of θ
to the nearest integer and remove the cross-condition by

1N {2ăbcďN 1 “ ż 1

0
 ÿ

N {p2cqďjďN 1{c epθjqep´θbq dθ(5.5)
 “ ż 1

0 νθ,c mintN 1{c, }θ}´1uep´θbq dθ

for some measurable function |νθ,c| ď 1. Taking the maximum over θ and incorporating
νθ,c and ep´θbq into the coefficients gives a valid type II sum after observing that either
N1 ď 2
?
N 1 or N2 ď 2
?
N 1.
The case of ΛE˚
3 .
If Λ
˚ “ ΛE˚
3 , we follow the strategy in [17, Sections 10.2, 10.3]. Recalling (3.4), we can
remove the weight 1{cE˚
3 pnq with Lemma 5.2. Afterwards, we are left with

1nPIp1nPB1{2 ` 1nPB2q

for some interval I Ď pN {2, N 1s, with Bi given in (3.1) and (3.2).
Observe that for both B1 and B2, we have N 1{3{2 ď p1p2 ď N 2{3. Thus, letting n1 “ p1p2
and n2 “ p3, dyadically splitting the variables, and removing the cross-condition n1n2 P I
by (5.5), we obtain an admissible type II sum.
The case of rP . This case follows from Harman’s fundamental theorem; see for exam-
ple [10, Theorem 3.1] and a subsequent application of (5.5) to remove the cross condition in
the type II case. □
30

We remark that if we were to consider rP with N 1{3 ă P ď N 1{2, we could get a similar
decomposition with Ramar´e’s identity [4, eq. (17.9)]. This introduces some additional
complications with square divisors that require care to not interact badly with the trivial
bound for vP in the sequel. For this reason, we do not pursue this generality here.

5.2. Bombieri–Vinogradov with power saving. The Bombieri–Vinogradov theorem im-
plies that for any A ě 1, the approximation
ÿ

nďN
n”a pmod dq
 Λpnq “ 1
φpdq
 ÿ

nďN Λpnqp1 ` OApplog N q
´Aqq(5.6)

is valid for almost all d up to N 1{2plog N q
´10A. The quality of this saving stems from the
application of the Siegel–Walfisz theorem for small conductor characters and the large sieve
inequality for large conductor characters. The term on the right-hand side of (5.6) is the
contribution of the principal character pmod dq, i.e., the unique character modulo d that
has conductor 1. If we instead include the contribution of all the characters with conductor
up to a value P larger than any fixed power of log N , the large sieve inequality will give a
saving that is a fixed power of P .
This idea was applied by Drappeau [3], and similarly to [3, equation (5.1)] we write

vP pn; qq :“ 1
φpqq
 ÿ

ψpqq
condpψq not P -smooth
 ψpnq(5.7)
 “ 1
φpqq
 ÿ

ψpqq ψpnq ´ 1
φpqq
 ÿ

ψpqq
condpψq P -smooth
 ψpnq.

In [3] the main term consists of the characters of conductor at most P , whereas for us it is
more convenient to retain the characters whose conductor has a prime factor larger than P ,
since this is what our sieve decomposition produces. As a conductor that is not P -smooth
exceeds P , the large sieve applies to these characters just as well. For any residue class a
with pa, qq “ 1, we use a to denote the multiplicative inverse of a modulo q. With this
notation we can state the following type I and II estimate, see also [3, Lemma 5.2].

Lemma 5.4 (Type I and II in arithmetic progressions). Let N1, N2, X ě 1 with N1N2 — X,
and let 2 ď P ă Q ď X. Then for any character χ of modulus at most P , we have

ÿ

qďQ
 ÿ

n1„N1 max
1ďaďq
pa,qq“1 max
ξďX{N1
 ˇ
ˇ
ˇ
ˇ
ˇ
 ÿ

n2ďξ χpn2qvP pn1n2a; qq

ˇ
ˇ
ˇ
ˇ
ˇ ! N1Q
3{2P 1{2X op1q.(5.8)

Let further αn, βn be complex sequences with |αn|, |βn| ď 1, supported on pN1{2, N1s and
pN2{2, N2s, respectively. Then we have

ÿ

qďQ max
1ďaďq
pa,qq“1
 ˇ
ˇ
ˇ
ˇ
ˇ
 ÿ

n1,n2 αn1βn2vP pn1n2a; qq
ˇ
ˇ
ˇ
ˇ
ˇ ! X 1{2`op1qpQ ` X 1{2{P ` N 1{2
1 ` N 1{2
2 q.(5.9)
 31

Proof. We first prove (5.8). We have
ÿ

n2ďξ χpn2qvP pn1n2a; qq “ 1
φpqq
 ÿ

ψpqq
condpψq not P -smooth
 ψpn1aq ÿ

n2ďξ χψpn2q.

Since χ has modulus at most P , the character χψ (of modulus ď P Q) is never principal. Let
χψ have modulus s and let it be induced by a character ψ1 of modulus 1 ă s1 ď s. Applying
M¨obius inversion and then the P´olya–Vinogradov inequality, we get
ÿ

n2ďξ χψpn2q “ ÿ

d|s µpdqψ1pdq ÿ

n1
2ďξ{d ψ1pn
1
2q ! X op1qaP Q,

uniformly in ξ ď X{N1. Thus, trivially bounding the number of ψ pmod qq with condpψq
not P -smooth by φpqq, we get (5.8).
The bound (5.9) follows from the large sieve inequality, as applied for large conductor
characters in the proof of [12, Proposition 17.4]. □

From the previous lemma we can deduce the following version of the Bombieri–Vinogradov
theorem with an additional character twist and improved error term.

Lemma 5.5 (Bombieri–Vinogradov with large savings). Let Λ˚ P tΛ, ΛE˚
3 , rP1u with P1 “
N δ4
1 . Assume that χ is a character of modulus at most R1 “ N δ4
1 {100 and let Q ď N 1{2´δ1.
Then for any N {2 ă N 1 ď N we have

ÿ

qďQ max
1ďaďq
pa,qq“1
 ˇ
ˇ
ˇ
ˇ
ˇ
ˇ
 ÿ

N {2ănďN 1 Λ˚pnqχpnqvP1pna; qq

ˇ
ˇ
ˇ
ˇ
ˇ
ˇ ! N 1`op1qP ´1
1 .

Proof. By Lemma 5.3, it suffices to show the following type I and II bounds for γn “
vP1pna; qqχpnq. We claim that
ˇ
ˇ
ˇ ÿ

N1{2ăn1ďN1
N {2ăn1n2ďN 1
 an1bn2vP1pn1n2a; qqχpn1n2qˇ
ˇ
ˇ ! N 1`op1qP ´1
1(5.10)

whenever N1 ď N 1{3, |an| ď τ pnq log n and bn ” 1 or bn ” log n and
ˇ
ˇ
ˇ ÿ

N1{2ăn1ďN1
N2{2ăn2ďN2
N {2ăn1n2ďN 1
 an1bn2vP1pn1n2a; qqχpn1n2q
ˇ
ˇ
ˇ ! N 1`op1qP ´1
1 ,(5.11)

whenever N {2 ă N1N2 ă 4N 1 with N1 P rN 1{3, 2N 1{2s and |an|, |bn| ď τ pnq log n.
Both type I and II cases are amenable to Lemma 5.4, after absorbing τ pnq log n ! N op1q

into the coefficients. In the type I case we distinguish two ranges of N1.
For N1 ď N 1{4 we pull the sum over n1 outside with the triangle inequality and remove
the logarithm with log n “ şN
1 1tďnt
´1 dt. For every fixed n1 the remaining range of n2 is an
interval contained in r1, 2N {N1s, so (5.8) with X — N and P “ P1 applies to each of the
two cutoffs. Summing over q, we bound the left-hand side of (5.10) by

! N 1{4`op1qQ3{2P 1{2
1 ! N 1{4`3{4´3δ1{2`δ4
1{2`op1q ! N 1´δ1 ! N P ´1
1 .

32

For N 1{4 ă N1 ď N 1{3 we instead interpret the sum as a type II sum. Splitting n2 into
Op1q dyadic intervals pN2{2, N2s with N2 — N {N1 ă N 3{4 and removing the cross-condition
by (5.5), we obtain an admissible type II sum. Since N 1{2
1 ď N 1{6 and N 1{2
2 ! N 3{8, summing
over q and applying (5.9) with X — N and P “ P1 bounds the left-hand side of (5.10) by

! N 1{2`op1q`Q ` N 1{2{P1 ` N 1{2
1 ` N 1{2
2 ˘ ! N 1{2`op1q`N 1{2´δ1 ` N 1{2{P1 ` N 3{8˘ ! N 1`op1qP ´1
1 .

Similarly, in the type II case, summing over q and applying (5.9) bounds the left-hand
side of (5.11) by

! N 1{2`op1qpN 1{2´δ1 ` N 1{2{P1 ` N 1{3q ! N 1´δ4
1 `op1q “ N 1`op1qP ´1
1 .
 □

5.3. Major arc contribution. In this subsection we apply the Bombieri–Vinogradov the-
orem with large savings, Lemma 5.5, to show (5.3).

Lemma 5.6 (Key major arc estimate). Assume the conditions of Proposition 5.1. Then we
have
 }Λ˚f `
Pref `
M ´ cMΛ˚f `
Pre}^
MpR1q ! N 1`op1qpP ´1{2
1 R1{2
1 ` R´1
1 q,

with cM given by (5.2), and similarly with ` placed on Λ˚ instead. In particular, (5.3) holds.

Proof. We only consider the first case, the second case where ` is placed on Λ˚ is very
similar. Since Λ
˚ is supported on P1-rough numbers outside a negligible set, we can appeal
to Lemma 4.7. Therefore it suffices to show that
ˇ
ˇ
ˇ
ˇ
ˇ
ˇ
 ÿ

|n1´n|ďN {R2
1 Λ˚pn1qχpn1q1n1ďN fPrepn
1 ` 2qpfMpn1 ` 2q ´ cMq
ˇ
ˇ
ˇ
ˇ
ˇ
ˇ ! N 1`op1qP ´1{2
1 R´2
1(5.12)

uniformly for N {2 ´ N {R2
1 ď n ď N ` N {R2
1 and for primitive characters χ of modulus
ď R1. By assumption we can write (incorporating the condition 1pn,6q“1 of the pre-sieve via
M¨obius inversion into the sieve weights)

fPrepnq “ ź

păP1
 ˆ1 ´ 1
p
˙´1 ÿ

d|n λPrepdq,

fMpnq “ ź

P1ďpăN 1{10
 ˆ1 ´ 1
p
 ˙´1 ÿ

d|n λMpdq,

where the weights λPre, λM are supported on integers having only prime divisors up to or
greater than P1, respectively. Recall further that by (5.2) we have

cM “ ź

P1ďpăN 1{10
 ˆ1 ´ 1
p
 ˙´1 ÿ

d
 λMpdq
φpdq .

To proceed, it is convenient to include a condition pn
1, dq “ 1 by setting

c1
Mpn1q “ ź

P1ďpăN 1{10
 ˆ1 ´ 1
p
 ˙´1 ÿ

d
 λMpdq1pn1,dq“1
φpdq .

33

Since λM is supported on P1-rough d, any j “ pn1, dq ą 1 satisfies j ě P1 and j | n1, so that

|c1
Mpn1q ´ cM| ! N op1q ÿ

P1ďdăN
 1pn1,dqą1
d ! N op1q ÿ

jěP1
 1j|n1
j ! N op1q

P1 .

As |Λ˚pn1qfPrepn
1 `2q| ! N op1q, replacing cM by c1
Mpn
1q changes the left-hand side of (5.12) by
! N 1`op1qP ´1
1 R´2
1 , which is admissible as P1 is a power of N . Thus it suffices to prove (5.12)
with cM replaced by c1
Mpn
1q.
Let d “ dďP1dąP1 be the decomposition of d into its P1-smooth and P1-rough parts. Let

λpdq “ λPrepdďP1qλMpdąP1q.

Then we can write

fPrepn1 ` 2qpfMpn1 ` 2q ´ c1
Mpn1qq “ ź

păN 1{10
 ˆ1 ´ 1
p
˙´1 ÿ

d λpdq ˆ1n1”´2 pmod dq ´ 1pn1,dąP1 q“11n1”´2 pmod dďP1 q
φpdąP1q
 ˙ .

To make Lemma 5.5 applicable, we rewrite, denoting by χpsq
0 the principal character pmod sq
and by ´2 the inverse of ´2 modulo d,

1n1”´2 pmod dq ´ 1pn1,dąP1 q“11n1”´2 pmod dďP1 q
φpdąP1q

“ 1
φpdq
 ÿ

ψ1pdq ψ1p´2n
1q ´ 1
φpdq
 ÿ

ψ2pdďP1 q ψ2p´2n1qχpdąP1 q
0 p´2n1q

“ 1
φpdq
 ÿ

ψpdq
condpψq not P1-smooth
 ψp´2n1q

“ vP1p´2n1; dq.

Coming back to the left-hand side of (5.12), we have reduced it to showing
ˇ
ˇ
ˇ
ˇ
ˇ
ˇ
 ÿ

pd,2q“1 λpdq ÿ

|n1´n|ďN {R2
1 Λ˚pn1qχpn1q1n1ďN vP1p´2n
1; dq

ˇ
ˇ
ˇ
ˇ
ˇ
ˇ ! N P ´1{2
1 R´2
1 plog N q
´2.(5.13)

Recall that by the definition of pre- and main-sieve we have d ď D1DM,1DM,2 “: Q ď N 1{2´δ1
and trivially estimate the weight |λpdq| ! τ pdq
Op1q ! nop1q, so that it suffices to prove

ÿ

dďQ
pd,2q“1
 ˇ
ˇ
ˇ
ˇ
ˇ
ˇ
 ÿ

|n1´n|ďN {R2
1 Λ˚pn
1qχpn
1q1n1ďN vP1p´2n1; dq

ˇ
ˇ
ˇ
ˇ
ˇ
ˇ ! N R´2
1 P ´1{2´1{1000
1 ,(5.14)

where we have used that P1 is a power of N to absorb N op1q losses. After subtracting the
upper and lower bound of the interval and applying the triangle inequality, we can apply
Lemma 5.5 to estimate the left-hand side of (5.14) by

N 1`op1qP ´1
1 “ N 1`op1q´δ4
1 ď N 1´δ4
1 p2{100`1{2`1{1000q “ N R´2
1 P ´1{2´1{1000
1 .

This shows the main statement of the lemma. Since P ´1{2
1 R1{2
1 ď R´2
1 “ N ´2δ4
1 {100 ď
N ´3pδ1{10q4, the estimate (5.3) is an immediate consequence. □
34

5.4. Minor arcs. In this subsection, we show (5.4). The required ingredients can essentially
be found in [14] and [17], but since in the former our type of weights is not treated explicitly
and the latter has different aims that do not easily adapt to power saving, we give the details.
The central ingredients are the following type I and II estimates that can be found in [14].

Lemma 5.7 (Type I and II minor arc estimate). Let a, q P N with pa, qq “ 1. Let |an|, |bn| ď
τ pnq log n, and assume that |α ´ a{q| ď q´2 with q ď X. Then for any fixed c P Z‰0, we
have the type I estimate
ÿ

rďD
 ˇ
ˇ
ˇ
ˇ ÿ

N1{2ăn1ďN1
X{p2n1qăn2ďX{n1
n1n2”c pmod rq
 an1bn2epαn1n2q
ˇ
ˇ
ˇ
ˇ ! X 1`op1qˆ 1
q ` DN1
X ` q
X
 ˙1{2.(5.15)

We have the type II estimate
ÿ

S1{2ăs1ďS1
S2{2ăs2ďS2
 ˇ
ˇ
ˇ
ˇ ÿ

N1{2ăn1ďN1
X{p2N1qăn2ďX{N1
n1n2”c pmod s1s2q
 an1bn2epαn1n2q
ˇ
ˇ
ˇ
ˇ

!X 1{2`op1qˆX ˆ 1
q ` q
X
 ˙1{3 ` min "X 11{10S2
1S2
2
N1 ` N1, S2
1S2
2 ` N1S2 ` XS2
1S2
N1 ` X

S1{3
2
 *˙1{2.

(5.16)

Proof. The type I bound (5.15) follows from [14, Lemma 6] in the same way as [14, eq. (6)]
is obtained. The type II bound (5.16) is a combination of [14, equation (7)] with η “ 1{10
and the estimate at the end of the proof of [14, Proposition 9]. □

We can now provide the minor arc bound that complements Lemma 5.6.

Lemma 5.8 (Minor arc estimate). Let Λ˚ P tΛ, ΛE˚
3 , rP1u with P1 “ N δ4
1 . Let fM, fPre be as
in Proposition 5.1 and assume that R ď N δ2
1 . Then we have

}Λ˚f `
Mf `
Pre}^
mpRq ! N 1`op1qR´1{6,(5.17)
 }Λ˚f `
Pre}^
mpRq ! N 1`op1qR´1{6,(5.18)

and similarly with the shift operator ` changing places to be on Λ˚. In particular, (5.4) holds.

Proof. Moving the shift operator does not change the proof apart from flipping `2 to ´2,
so we only consider the stated case. We first show (5.17).
By Lemma 5.3 it suffices to show that

max
αPmpRq

ˇ
ˇ
ˇ ÿ

N1{2ăn1ďN1
N {2ăn1n2ďN
 an1bn2fMpn1n2 ` 2qfPrepn1n2 ` 2qepαn1n2q
ˇ
ˇ
ˇ ! N 1`op1qR´1{6,(5.19)

whenever N1 ď N 1{3, |an| ď τ pnq log n and bn ” 1 or bn ” log n; and

max
αPmpRq

ˇ
ˇ
ˇ ÿ

N1{2ăn1ďN1
N2{2ăn2ďN2
N {2ăn1n2ďN
 an1bn2 fMpn1n2 ` 2qfPrepn1n2 ` 2qepαn1n2q
ˇ
ˇ
ˇ ! N 1`op1qR´1{6,(5.20)
 35

whenever N {2 ă N1N2 ă 4N and N1 P rN 1{3, 2N 2{3s, |an|, |bn| ď τ pnq log n.
We recall that by Definitions 2.2 and 2.3, we have

fMpnq “ CfM ÿ

d1d2|n λM,1pd1qλM,2pd2q,

fPrepnq “ 1pn,6q“1 ź

păP1
`1 ´ 1
p
˘´1 ÿ

d|n λPrepdq,

where the sieve weights λPre are 1-bounded, λPre is of level D1, and |λM,jpdq| ď τ pdqOp1q,
λM,1 is of level DM,1 “ N 1{3´δ1, and λM,2pd2q a sum of Oδ1p1q well-factorable weights of level
DM,2 “ N 1{6´δ1 and |CfM| ! plog N q.
We first consider the type I estimate (5.19). We combine the three sieve weights into one,
apply the triangle inequality and then the type I case of Lemma 5.7 to obtain for (5.19) the
bound

!N op1q max
αPmpRq
 ÿ

rďD1DM,1DM,2
 ˇ
ˇ
ˇ
ˇ ÿ

N {2ăn1n2ďN
n1n2”´2 pmod rq
N1{2ăn1ďN1
 an1bn2epαn1n2q
ˇ
ˇ
ˇ
ˇ ! N 1`op1qˆ 1
R ` N1D1DM,1DM,2
N
 ˙1{2,

where we used the fact that every α P mpRq satisfies |α ´ a{q| ď 1{pqpN {Rqq for some integer
R ă q ď N {R and some a coprime to q. Since

N1D1DM,1DM,2 ď N 1{3`1{3´δ1`1{6´δ1`δ3
1 {100 ď N {R,

this bound is ! N 1`op1qR´1{2.
For the type II estimate (5.20), we proceed similarly to [14, end of proof of Proposition 9]
and split the weights dyadically into segments d „ D with

D ď D1DM,1DM,2.

If D ď N 1{10, we apply the type II case of Lemma 5.7 with S1 “ D and S2 “ 1, using the
first part of the minimum to obtain for the left-hand side of (5.20) the upper bound

! N 1{2`op1q `N R´1{3 ` N 9{10˘1{2 ! N 1`op1qR´1{6.

For the remaining case of N 1{10 ď D ď D1DM,1DM,2 we use the factorisation properties
and choose
 S2 “ min "
D, N 1´δ1{2

N1
 * .

This choice fulfils S2 ě mintD, N 1{3´δ1{2u, and thus, using the facts that λM,2 is a sum of
Oδ1p1q well-factorable weights and that D1N 1{3´2δ1 ď N 1{3´δ1{2, we can group and dyadi-
cally decompose the sieve weights into Opplog N q
2q components of the shape λ
1 ‹ λ
2, where
|λ
1pdq|, |λ
2pdq| ď τ pdq
Op1q, λ1 is supported on rS2{2, S2s, and λ2 is supported on rS1{2, S1s
with S1 :“ D{S2. Observe that for these choices we have

N S2
1S2{N1 “ D2N {pS2N1q ď D2N δ1{2,

N 1{10 ď S2 ď N 1´δ1{2{N1.

36

Thus, using the second part of the minimum in the type II case of Lemma 5.7, we can
estimate the left-hand side of (5.20) by

! N 1{2`op1q `N R´1{3 ` N 1´δ1{2 ` D2N δ1{2˘1{2 .

Since D ď D1DM,1DM,2 “ N 1{2´2δ1`δ3
1 {100, R ď N δ2
1 and N1 ě N 1{3, this is bounded by

! N 1`op1qR´1{6,

and (5.20) follows.
The estimate (5.18) follows directly from the same argument (taking fMpnq “ 1 and
skipping the steps about the decomposition of fM).
Recalling R1 “ N δ4
1 {100, (5.4) follows immediately. □

We end this section by stating a minor arc bound for the Cram´er model twisted by a
power function. It is used in the proof of Proposition 7.8.

Lemma 5.9. Let 2 ď plog N q
100 ă R2 ď P ď N 1{4 and 1{2 ď β ď 1. We have

sup
αPmpRq
 ˇ
ˇ
ˇ
ˇ
ˇ
 ÿ

nďN rP pnqn
β´1epαnq

ˇ
ˇ
ˇ
ˇ
ˇ ! N R´1{3.

Proof. Since
 n
β´1 “ 1 ` pβ ´ 1q ż n

1 t
β´2 dt,(5.21)

and şN
1 t
β´2 dt ! log N , by the triangle inequality it suffices to prove the claim without the
nβ´1 factor and with the summation range replaced by n ď ξ for ξ ď N . We discard the
contribution of n ď N R´1{2 trivially, dyadically decompose and apply Lemma 5.3, noting
that pN R´1{2q
1{3 ą N 1{4. The claim then follows from standard minor arc estimates, see for
example [12, Lemmas 13.7 and 13.8]. □

6. The additive problem with sieves

In this section, we consider a sifted convolution sum related to our additive problem. We
are concerned with expressions of the form
ÿ

n1`n2“m f1pn1qf2pn1 ` 2qf3pn2qf4pn2 ` 2q,(6.1)

where each of the functions fi is sifted in the sense that the contribution of n that have small
prime divisors is negligible.
In Subsection 6.1 we prove some basic results related to sieves. In Subsection 6.2 we
consider (6.1) in the case of all the fi being pre-sieves as in Definition 2.2 for which we prove
an asymptotics, see Proposition 6.3 and Proposition 6.5 for additional twists by quadratic
characters to handle the possible exceptional character. In Subsection 6.3 we consider (6.1) in
the case where three of the fi are absolute values of pre-sieves and the last one is of the form
|ΛR,r| (recall (4.5)), for which we provide an upper bound of correct order in Proposition 6.8.
37

6.1. Sieve lemmas. We require two sieve lemmas to understand (6.1).
The first result is an identity to relate sums of sieve weights over multiples of a given
integer to the sieve.

Lemma 6.1. Let P be a square-free positive integer, pλdqdě1 be a sequence of complex num-
bers supported on the divisors of P only and assume that e | P. Let g be a multiplicative
function such that 0 ď gppq ă 1 for all primes p and gppq ą 0 for all p | e, and define a
multiplicative function h supported on square-free numbers by hppq “ gppq
1´gppq. Then we have

gpeq ÿ

d|P{e λdegpdq “ ź

p|P
 `1 ´ gppq
˘µpeqhpeq ÿ

b|P θpbqhpbq µppb, eqq
hppb, eqq ,

where θpnq “ ř

d|n λd.

Proof. This is shown in the first display of the proof of [15, Lemma 6.1] for the case gpdq “
1{d; the general case works exactly the same. Note that this fixes a mistake in [4, Lemma
6.18]. □

The second sieve result is of fundamental lemma type. It is a minor variant of [19, Lemma
3.2], see also [15, after equation (58)].

Lemma 6.2. Let f P tω, Ωu be pre-sieves as in Definition 2.2, and let β “ 200. Write

Ppyq “ ś

5ďpăy p and Pr “ PpP
 ` β´1
β`1˘r

1 q, and assume that s “ log D1
log P1 ą β ` 2. Then we have

|f pnq ´ rP1pnq| ď ź

păP1
 ˆ1 ´ 1
p
 ˙´1 τ pnq2 ÿ

rPN
rąps´β´1q{2
 4
´r1pn,Prq“1.

Proof. The beta sieve is a combinatorial sieve that is constructed by iteration with certain
cutoff parameters, see [4, equations (6.31)–(6.34), (6.54)]. From this it follows immediately
that for the upper bound sieve Ω we have the identity

Ωpnq “ rP1pnq ` ź

păP1
 ˆ1 ´ 1
p
 ˙´1 ÿ

r odd Vrpnq,

and similarly for the lower bound sieve ω we have

ωpnq “ rP1pnq ´ ź

păP1
 ˆ1 ´ 1
p
 ˙´1 ÿ

r even Vrpnq,

where
 Vrpnq “ ÿ

p1¨¨¨pr|n
pi|PpP1q, prăpr´1ă...ăp1
p1p2¨¨¨prpβ
r ěD1
p1p2¨¨¨phpβ
hăD1 for all hăr,h”r pmod 2q
 1pn{pp1¨¨¨prq,Ppprqq“1.

By [4, Corollary 6.6], in the last sum we have pr ě P
 ` β´1
β`1˘r{2

1 . We also have D1 ď pr`β
1 ď
P r`β
1 , which is impossible unless r ě s´β. We complete the proof by repeating the argument
in [15, after equation (58)]: In the sum defining Vr, the distinct primes pi | PpP1q satisfy
38

pi ě 5, so writing νpnq for the number of prime divisors of n we have νpnq ě r so that
2
νpnq´r ě 1. Hence,
 Vrpnq ď 1pn,Pr{2q“12
νpnq´r ÿ

k|n 1 ď 1pn,Pr{2q“1τ pnq
22
´r.

Writing r “ 2r1 ` 1 or r “ 2r1, respectively for the case of an upper bound or lower bound
sieve, the lemma follows. □

6.2. Asymptotics for the sifted convolution sum. We now apply Lemmas 6.1 and 6.2 to
prove an asymptotic formula for the additive problem with four pre-sieves (Proposition 6.3),
its variant twisted by the exceptional character (Proposition 6.5), and the resulting upper
and lower bounds (Corollary 6.4).

Proposition 6.3 (The additive problem with pre-sieves). For 1 ď i ď 4, let the functions
fi P tω, Ωu be pre-sieves as in Definition 2.2. For any natural number m and any 1 ď X ď m,
we have ÿ

nďX f1pnqf2pn ` 2qf3pm ´ nqf4pm ´ n ` 2q

“XSpmq ˆ1 ` O ˆe´ log D1
10 log P1 ` log m
P1
 ˙˙ ` OpD4
1plog P1q4q.
(6.2)

Proof. We write P “ ś
5ďpăP1 p, expand out the sieves fi according to their definitions, and
observe that pn, 6q “ 1, pn ` 2, 6q “ 1, pm ´ n, 6q “ 1, pm ´ n ` 2, 6q “ 1 is equivalent to
m ” 4 pmod 6q, n ” 5 pmod 6q. This leads to
ÿ

nďX f1pnqf2pn ` 2qf3pm ´ nqf4pm ´ n ` 2q

“ 3
4
ś

păP1p1 ´ 1{pq4 1m”4 pmod 6q ÿ

d1,d2,d3,d4|P
 4ź

i“1 λipdiq ÿ

nďX
d1|n
d2|n`2
d3|m´n
d4|m´n`2
 1n”5p6q.(6.3)

There exists a solution to the divisibility conditions in the innermost sum if and only if

pd1, d2q “ 1,

pd3, d4q “ 1,

pd1, d3q | m,

pd1, d4q | m ` 2,

pd2, d3q | m ` 2,

pd2, d4q | m ` 4.

(6.4)

Let us abbreviate these conditions as pd1, d2, d3, d4q P Dm. Under these conditions, the sum
over n in (6.3) equals
 X
6rd1, d2, d3, d4s ` Op1q.

39

The Op1q error term contributes to (6.3) at most Opplog P1q4D4
1q by Mertens’ theorem.
Hence, (6.3) becomes

3
4X
6 ś
păP1p1 ´ 1{pq4 1m”4 pmod 6q ÿ

d1,d2,d3,d4|P
pd1,d2,d3,d4qPDm
 ś4
i“1 λipdiq
rd1, d2, d3, d4s ` Opplog P1q
4D4
1q.(6.5)

We want to evaluate the summation over each of the di with Lemma 6.1 and afterwards
apply Lemma 6.2. To make this possible we need to carefully disentangle the coprimality
and divisibility conditions in order to not lose relative to the size of the expected main term
in the error terms.
In the rest of the proof, we use ÿ1 to indicate that the summation variables are supported
on divisors of P only. Next, write e1 “ pd1, d3q, e2 “ pd1, d4q, e3 “ pd2, d3q, e4 “ pd2, d4q and
further d1 “ d1
1e1e2, d2 “ d
1
2e3e4, d3 “ d1
3e1e3, d4 “ d1
4e2e4. Note that this is possible since
by pd3, d4q “ 1 we have pe1, e4q “ 1 (and pe2, e3q “ 1 etc.), and by pd1, d2q “ 1 we have
pe1, e3q “ 1 (and so on). Note further that (6.4) implies that the variables d1
i and ej are
mutually coprime. Thus, rd1, d2, d3, d4s “ d1
1d1
2d1
3d1
4e1e2e3e4 and the central sum in (6.5)
becomes
 ÿ1

d1,d2,d3,d4
pd1,d2,d3,d4qPDm
 ś4
i“1 λipdiq
rd1, d2, d3, d4s

“ ÿ1

e1|m
e2,e3|m`2
e4|m`4
ei coprime
 1
e1e2e3e4
 ÿ1

d1
1
pd1
1,e3e4q“1
 λ1pd1
1e1e2q
d
1
1
 ÿ1

d1
2
pd1
2,d1
1e1e2q“1
 λ2pd
1
2e3e4q
d1
2

ˆ ÿ1

d1
3
pd1
3,d1
1d1
2e2e4q“1
 λ3pd
1
3e1e3q
d1
3
 ÿ1

d1
4
pd1
4,d1
1d1
2d1
3e1e3q“1
 λ4pd
1
4e2e4q
d1
4 .

To ease notation, write e “ e1e2e3e4 and remove the 1 from the d
1
i variables again. The
strategy to approach (6.5) is to evaluate the sums over d4, d3, d2, d1 in the last display with
Lemma 6.1, successively exchanging the order of summation. Note that since the function
θ of Lemma 6.1 associated with a given sequence λi is ś

păP1p1 ´ 1{pq ¨ fi, each successive
application will cancel one of the p1 ´ 1{pq
´1 factors in (6.5).
40

Starting with the summation over d4, we apply of Lemma 6.1 with gpdq “ 1pd,d1d2d3e1e3q“1
d
and e “ e2e4. This gives us

ź

păP1
 ˆ1 ´ 1
p
 ˙´1 ÿ1

d4
pd4,d1d2d3e1e3q“1
 λ4pd4e2e4q
d4

“ ź

p|P{pd1d2d3e1e3q
 ˆ1 ´ 1
p
 ˙ µpe2e4qe2e4
φpe2e4q
 ÿ1

b4
pb4,d1d2d3e1e3q“1
 f4pb4q
φpb4q µppb4, e2e4qqφppb4, e2e4qq

“ ź

p|P
 ˆ1 ´ 1
p
 ˙ d1d2d3eµpe2e4q
φpd1d2d3eq
 ÿ1

j4|e2e4 µpj4q ÿ1

b4
pb4,d1d2d3eq“1
 f4pb4j4q
φpb4q .

For i P t2, 3, 4u, we denote by φi the multiplicative function given on primes p by p ´ i.
We only employ this notation for d | P, so that pd, 6q “ 1 and d is square-free, ensuring
φipdq ą 0. By an application of Lemma 6.1, the relevant d3 sum now is

ź

păP1
 ˆ1 ´ 1
p
 ˙´1 ÿ1

d3
pd3,b4d1d2e2e4q
 λ3pd3e1e3q
φpd3q

“ ź

p|P
 ˆ1 ´ 1
φppq
 ˙ φpd1d2b4eqµpe1e3q
φ2pd1d2b4eq
 ÿ1

j3|e1e3 µpj3q ÿ1

b3
pb3,d1d2b4eq“1
 f3pb3j3q
φ2pb3q .

The d2 sum becomes

ź

păP1
 ˆ1 ´ 1
p
 ˙´1 ÿ1

d2
pd2,d1b3b4e1e2q“1
 λ2pd2e3e4q
φ2pd2q

“ ź

p|P
 ˆ1 ´ 1
φ2ppq
 ˙ φ2pd1b3b4e1e2e3e4qµpe3e4q
φ3pd1b3b4e1e2e3e4q
 ÿ1

j2|e3e4 µpj2q ÿ1

b2|P
pb2,d1b3b4eq“1
 f2pb2j2q
φ3pb2q .

Finally, for the d1 sum we get

ź

păP1
 ˆ1 ´ 1
p
 ˙´1 ÿ1

d1
pd1,b2b3b4e3e4q“1
 λ1pd1e1e2q
φ3pd1q

“ ź

p|P
 ˆ1 ´ 1
φ3ppq
 ˙ φ3pb2b3b4eqµpe1e2q
φ4pb2b3b4eq
 ÿ1

j1|e1e2 µpj1q ÿ1

b1
pb1,b2b3b4eq“1
 f1pb1j1q
φ4pb1q .

Note that for p ě 5
ˆ1 ´ 1
p
 ˙ ˆ
1 ´ 1
φppq
˙ ˆ
1 ´ 1
φ2ppq
˙ ˆ
1 ´ 1
φ3ppq
 ˙ “ 1 ´ 4
p .

41

Combining the four evaluations and recalling the normalisation of the fi, we get for the term
of interest in (6.5) the identity

3
4

6 X1m”4 pmod 6q 1
ś
păP1p1 ´ 1{pq4 ÿ

d1,d2,d3,d4|P
pd1,d2,d3,d4qPDm
 ś4
i“1 λipdiq
rd1, d2, d3, d4s

“3
4

6 X1m”4 pmod 6q ź

p|P
 ˆ1 ´ 4
p
˙ ÿ1

e1|m
e2,e3|m`2
e4|m`4
ei coprime
 1
φ4peq

ˆ ÿ1

j1|e1e2
j2|e3e4
j3|e1e3
j4|e2e4
 ÿ1

bi
pbi,bj q“1, @i‰j
pbi,eq“1
 µpj1qµpj2qµpj3qµpj4q f1pb1j1qf2pb2j2qf3pb3j3qf4pb4j4q
φ4pb1b2b3b4q .(6.6)

Write b “ b1b2b3b4 and j “ j1j2j3j4. The term with bj “ 1 in (6.6) is the main term. Since
P is coprime to the primes less than 5, we have

ÿ1

e1|m
e2,e3|m`2
e4|m`4
ei coprime
 1
φ4peq “ ÿ1

e1|m
 1
φ4pe1q
 ÿ1

e2|m`2
 1
φ4pe2q
 ÿ1

e3|m`2
 1
φ4pe3q
 ÿ1

e4|m`4
 1
φ4pe4q
(6.7)
 “ ź

5ďpăP1
p|mpm`4q
 ˆ1 ` 1
p ´ 4
˙ ź

5ďpăP1
p|m`2
 ˆ1 ` 2
p ´ 4
 ˙ .

Observe that the sums on the right-hand side of (6.7) are multiplicative in m, m ` 2,
m ` 4, respectively, and recall that P “ ś

5ďpăP1 p is square-free. Since 3
4{6 “ 27{2 and
fip1q “ ś

p|Pp1 ´ 1{pq
´1, it follows that terms with bj “ 1 in (6.6) contribute

X1m”4 pmod 6q 27
2
 ź

5ďpăP1
 ˆ1 ´ 4
p
˙ ź

5ďpăP1
p|mpm`4q
 ˆ1 ` 1
p ´ 4
 ˙ ˆ
1 ´ 1
p
 ˙´4 ź

5ďpăP1
p|m`2
 ˆ1 ` 2
p ´ 4
 ˙

“:Spm; P1q,
 42

say. We can complete the product by introducing an acceptable error term. Indeed, the tail
product is
 ź

pąP1
 ˆ1 ´ 6p2 ´ 4p ` 1
pp ´ 1q4
 ˙ ź

pąP1
p|mpm`4q
 ˆ1 ` 1
p ´ 4
 ˙ ź

pąP1
p|m`2
 ˆ1 ` 2
p ´ 4
 ˙

“ ź

pąP1
 ˆ1 ` O ˆ 1
p2
 ˙˙ ź

pąP1
p|mpm`2qpm`4q
 ˆ1 ` O ˆ 1
p
˙˙

“ exp
 ¨

˚
˚
˝O
 ¨

˚
˚
˝ ÿ

pąP1
 1
p2 ` ÿ

pąP1
p|mpm`2qpm`4q
 1
p
˛

‹
‹
‚

˛

‹
‹
‚

“ exp ˆO ˆ 1
P1 ` log m
P1 log P1
 ˙˙

“1 ` O ˆ log m
P1
 ˙ .

Thus Spm; P1q “ Spmq ´1 ` O` log m
P1 ˘¯
, where the completed singular series is as in (2.1).
It remains to estimate the contribution of the remaining terms with bj ‰ 1 in (6.6). To
do so, we first apply the triangle inequality and then split up the ji, 1 ď i ď 4 into two
components li, 1 ď i ď 8 with the properties

j1 “ l1l2 with l1 | e1, l2 | e2,

j2 “ l3l4 with l3 | e3, l4 | e4,

j3 “ l5l6 with l5 | e1, l6 | e3,

j4 “ l7l8 with l7 | e2, l8 | e4.

We can then upper bound the e sum with the additional li conditions by

ÿ

e1|m,l1l5|e1
e2,e3|m`2,l2l7|e2,l3l6|e3
e4|m`4,l4,l8|e4
ei|P,ei coprime
 1
φ4peq

ď ź

p|P
p|mpm`4q
 ˆ1 ` 1
p ´ 4
 ˙ ź

p|P
p|m`2
 ˆ1 ` 2
p ´ 4
 ˙ ś8
i“1 ś

p|li p1 ` Op1q{pq

rl1, l5srl2, l7srl3, l6srl4, l8s .

This reduces the required estimate to showing that

ÿ

li,bi|P
bl‰1
 |f1pb1l1l2qf2pb2l3l4qf3pb3l5l6qf4pb4l7l8q| ś
p|bl p1 ` Op1q{pq

brl1, l5srl2, l7srl3, l6srl4, l8s ! e
´ log D1
10 log P1 .(6.8)
 43

Write pl1, l5q “ d1, pl2, l7q “ d2, pl3, l6q “ d3, pl4, l8q “ d4, d “ d1d2d3d4, and l “ ś8
i“1 li. We
can then recombine the remaining variables and estimate the left-hand side of (6.8) by

ď ÿ

di,bi|P
bd‰1
 |f1pb1d1d2qf2pb2d3d4qf3pb3d1d3qf4pb4d2d4q| τ pbq
4 ś

p|bdl p1 ` Op1q{pq

bd1d2d3d4 .

Note that for n | P with n ą 1, we have rP1pnq “ 0 and so Lemma 6.2 gives an upper bound
for |f pnq| in that case. Thus, writing s “ log D1
log P1 and applying Lemma 6.2, we upper bound
the previous display by

ď ÿ

r1,r2,r3,r4ąps´β´1q{2 4
´r1´r2´r3´r4 ÿ τ pbq6τ pdq
2 ś
p|bdl p1 ` Op1q{pq

db ,

where the summation ranges over bi, di with

b1d1d2 | P, b2d3d4 | P,

b3d1d3 | P, b4d2d4 | P,

and
 pb1d1d2, Pr1q “ pb2d3d4, Pr2q “ pb3d1d3, Pr3q “ pb4d2d4, Pr4q “ 1,

and where we wrote Pr for the product of primes between 5 and P
 ` β´1
β`1˘r

1 . Dropping in each
of these conditions one of the di in a suitable manner, we get the upper bound

ď
 ¨

˚
˚
˝ ÿ

rąps´β´1q{2 4
´r ÿ

b|P
pb,Prq“1
 τ 7pbq ś
p|b`1 ` Op1q{p˘

b
 ˛

‹
‹
‚

4
 .(6.9)

By Mertens’ theorem we have

ÿ

b|P
pb,Prq“1
 τ pbq
7 ś

p|b`1 ` Op1q{p˘

b ! ź

P` β´1
β`1˘r

1 ăpăP1
´
1 ` 2
7

p
 ¯

! ´ log P1

log P
 ` β´1
β`1 ˘r

1
 ¯27

“ ´β ` 1
β ´ 1
 ¯128r.

Recall β “ 200, whence we have ´ β`1
β´1¯128{4 ď 0.9 and the tail sum over r in (6.9) is bounded

by Ope
´s{10q. This shows (6.8) and completes the proof. □

As an immediate corollary, we get that upper and lower bound pre-sieves are approximately
the same for our additive problem. 44

Corollary 6.4. Let f, g be arithmetic functions, satisfying |f ´ g|pnq ď `Ω ´ ω˘pnqΩpn ` 2q

with ω, Ω being pre-sieves as in Definition 2.2. Then, for ϵ " e
´ log D1
10 log P1 , we have

f «ϵ g.

The same holds with the roles of n and n ` 2 reversed.

If the exceptional zero exists, we expect a different main term for some m. To accommodate
this, we now prove a variant of Proposition 6.3 that includes restrictions on n and m ´ n
into certain residue classes depending on a given primitive quadratic character.

Proposition 6.5. For 1 ď i ď 4, let the functions fi P tω, Ωu be pre-sieves as in Def-
inition 2.2. Let χ be a primitive quadratic character to the modulus r ě 3. There exist
functions σ1, σ2 : N Ñ r´1, 1s (depending on χ) — they are real since χ is real-valued —
with |σ1|, |σ2| ď 1 such that for any 1 ď X ď m, we have

ÿ

nďX 1χpnq“χpm´nq“´11pn`2,rq“pm´n`2,rq“1f1pnqf2pn ` 2qf3pm ´ nqf4pm ´ n ` 2q

“XSpmq ˆ 1 ` σ1pmq
4 ` Oϵpr´1`ϵq
˙ ˆ
1 ` O ˆe
´ log D1
10 log P1 ` log m
P1
 ˙˙ ` OprD4
1plog P1q4q

(6.10)

and
ÿ

nďX 1χpnq“χpn`2q“11χpm´nq“´11pm´n`2,rq“1f1pnqf2pn ` 2qf3pm ´ nqf4pm ´ n ` 2q

“XSpmq ˆ 1 ´ σ1pmq ´ σ2pmq
8 ` Oϵpr´1{2`ϵq
˙ `1 ` Ope´ log D1
10 log P1 ` log m
P1 q
˘ ` OprD4
1plog P1q4q.

(6.11)

Proof. Splitting into congruence classes modulo r, we have to consider
ÿ

bprq apbq ÿ

nďX
n”bprq
 f1pnqf2pn ` 2qf3pm ´ nqf4pm ´ n ` 2q,

where a P ta1, a2u with
 a1pbq “ 1χpbq“χpm´bq“´11pb`2,rq“pm´b`2,rq“1

and
 a2pbq “ 1χpbq“χpb`2q“11χpm´bq“´11pm´b`2,rq“1.

We treat the sum over n just as in the proof of Proposition 6.3, the only difference being
that fixing n into a residue class modulo r means that primes dividing r are not part of the
45

calculations. Indeed, opening the sieves we now have
ÿ

nďX
n”bprq
 f1pnqf2pn ` 2qf3pm ´ nqf4pm ´ n ` 2q

“ 3
4
ś

păP1p1 ´ 1{pq4 1m”4 pmod 6q ÿ

d1,d2,d3,d4|P
 4ź

i“1 λipdiq ÿ

nďX
n”bprq
d1|n
d2|n`2
d3|m´n
d4|m´n`2
 1n”5p6q.

Apart from the congruence condition modulo r, this is just as in (6.3). By considering the
support of a, we can assume that pb, rq “ 1 and thus also pd1d2d3d4, rq “ 1. Furthermore, the
arising condition that b, m ´ b ” 5 pmod p6, rqq is automatic by the support of a. From this
point, we can follow the argument in the proof of Proposition 6.3 verbatim, apart from the
additional condition that pd1d2d3d4, rq “ 1 and the additional factor 1{r when approximating
the sum over n. Explicitly, for p6, rq “ 1 the innermost sum equals X
6rrd1,d2,d3,d4s ` Op1q, the
term Op1q contributing OprD4
1plog P1q
4q after summation over the di and over b pmod rq.
This shows that
ÿ

bprq apbq ÿ

nďX
n”bprq
 f1pnqf2pn ` 2qf3pm ´ nqf4pm ´ n ` 2q

“
 ř

bprq apbq

r X ź

p|r
 ´
1 ´ 1
p ¯´4S
1pm, rq ˆ1 ` O´
e
´ log D1
10 log P1 ` log m
P1
 ¯˙ ` OprD4
1plog P1q
4q,

where

S
1pm, rq “ 1m”4 pmod 6q 27
2
 ź

pě5
p∤r
 ˆ1 ´ 6p2 ´ 4p ` 1
pp ´ 1q4
 ˙ ź

pě5
p|mpm`4q
p∤r
 ˆ1 ` 1
p ´ 4
 ˙ ź

pě5
p|m`2
p∤r
 ˆ1 ` 2
p ´ 4
˙ .

It remains to consider the sum over b. We have 1χpbq“´1 “ 1pb,rq“1p1 ´ χpbqq{2 and so in the
case of a “ a1
 4 ÿ

bprq a1pbq “ ÿ

bprq 1pb,rq“pb`2,rq“pm´b,rq“pm´b`2,rq“1

´ 2 ÿ

bprq χpbq1pbpb`2qpm´bqpm´b`2q,rq“1

` ÿ

bprq χpbqχpm ´ bq1ppb`2qpm´b`2q,rq“1

“:S1pm, rq ´ 2S2pm, rq ` S3pm, rq,

say. Naturally all the Si are functions of both m and r. By the nature of the singular series
being a product of local solution densities (or a short direct verification), we see that

S1pm, rq
r
 ź

p|r
 ´
1 ´ 1
p ¯´4 “ Spmq
S1pm, rq .

46

We set
 σ1pmq :“ S3pm, rq
S1pm, rq .

An application of the triangle inequality immediately shows |σ1| ď 1. The sum S2 is multi-
plicative in r. Indeed, for coprime r “ r1r2 the Chinese Remainder Theorem and χ “ χr1χr2
factor the sum as S2pm, r1qS2pm, r2q. Using a simple inclusion-exclusion argument and or-
thogonality of characters gives |S2pm, rq| ! rop1q. This shows (6.10).
For the case a “ a2 we observe 1χpbq“χpb`2q“1 “ 1pbpb`2q,rq“1p1 ` χpbqqp1 ` χpb ` 2qq{4 so
that
 8 ÿ

bprq a2pbq “ S1 ´ S3 ´ S4 ` S5 ´ S6 ` Oϵ`r1{2`ϵ˘,

where S1 and S3 are as above and

S4 “ ÿ

bprq χpb ` 2qχpm ´ bq1pbpm´b`2q,rq“1,

S5 “ ÿ

bprq χpb ` 2q1pbpm´bqpm´b`2q,rq“1,

S6 “ ÿ

bprq χpbqχpb ` 2qχpm ´ bq1pm´b`2,rq“1.

Here the error term Oϵpr1{2`ϵq collects the three single- and double-character sums ř
bprq χpbq,
ř

bprq χpbqχpb ` 2q and ř

bprq χpm ´ bq arising in the expansion, each !ϵ r1{2`ϵ as for S5, S6.
We set
 σ2pmq :“ S4pm, rq
S1pm, rq .

The triangle inequality again shows |σ2pmq| ď 1. We have |S5pm, rq| ! rop1q by the same
argument as for S2. Finally, since χ is primitive and quadratic we have that r{p4, rq is square-
free. Thus, using that S6 is multiplicative in r, a simple inclusion-exclusion argument, and
the Weil bound [12, Corollary 11.24], we get |S6pm, rq| !ϵ r1{2`ϵ. This shows (6.11) and
completes the proof. □

Remark 6.6. It is not difficult to calculate σ1pmq and σ2pmq and write them as products of
local densities. However, when compared to the related case of rSpmq in [21], the treatment is
more involved. In particular the primes 3, 5 and 7 need to be handled separately. To simply
show the existence of suitable representations of m as in Theorem 1.1, the precise evaluation
of the functions σi plays no role. It matters only that both |σ1| and |σ2| are 1-bounded and
that σ1 appears with different signs in (6.10) and (6.11).

6.3. Upper bounds for the sifted sum. In order to prove upper bounds of the correct
order of magnitude for the sifted additive problem (6.1) involving beta sieves and ΛR,r as
in (4.5), we require the following lemma about correlations.

Lemma 6.7 (An upper bound for correlations of multiplicative functions). Let A ě 1 be
fixed. Let h : N Ñ Rě0 be a multiplicative function that satisfies hpnq ď nop1q and hppkq ď A
k

47

for all primes p and all k P N. Let log N ď P 1
1, P 1
2, P 1
3 ď N . Then, for any m P r5N {4, 7N {4s
and m ” 4 pmod 6q, we have
ÿ

N {2ănďN hpnqpτ 2rP 1
1qpn ` 2qpτ 2rP 1
2qpm ´ nqpτ 2rP 1
3qpm ´ n ` 2q(6.12)
 ! N
log N Spmq
 3ź

i“1
 ˆ log N
log P 1
i
 ˙3 ź

păN
 ˆ1 ` hppq
p
 ˙ ź

p|mpm`2qpm`4q
pěmintP 1
1,P 1
2,P 1
3u

´
1 ` Op1q
p
 ¯
.

The same bound holds if hpnq swaps places with any of the other weights on n ` 2, m ´ n, m ´
n ` 2.

Proof. We want to apply Henriot’s bound ([11, Corollary 1]) to the four-variable multiplica-
tive function
 F pn1, n2, n3, n4q “ hpn1q
 3ź

i“1 τ 2pni`1q1pni`1,PpP 1
i qq“1,

the tuple of polynomials

pQ1puq, Q2puq, Q3puq, Q4puqq “ pu, u ` 2, m ´ u, m ´ u ` 2q,

and with choices x “ y “ N {2. Note that Q :“ Q1Q2Q3Q4 has discriminant D “ 2
4m2pm `
2q
4pm ` 4q
2, that Q is primitive since its leading coefficient is 1, and that the sum of the
absolute values of the coefficients of Q is ! N 2.
Moreover, if ρQpnq denotes the number of solutions to the congruence Qpuq ” 0 pmod nq,
then since m — N , we have
ź

4ăpďN
 ˆ1 ´ ρQppq
p
 ˙ “ ź

4ăpďN
p∤D
 ˆ1 ´ 4
p
 ˙ ź

4ăpďN
p|mpm`4q
 ˆ1 ´ 3
p
 ˙ ź

4ăpďN
p|m`2
 ˆ1 ´ 2
p
 ˙

! ź

4ăpďN
 ˆ1 ´ 4
p
 ˙ ź

p|mpm`4q
 ˆ1 ` 1
p
˙ ź

p|m`2
 ˆ1 ` 2
p
 ˙

! Spmq
plog N q4 .

We can now apply [11, Corollary 1], observing that in Henriot’s notation we have rF “ rG “ F ,
and that we can simplify the main term there with the trivial inequality

ÿ

n1n2n3n4ďN an1,1an2,2an3,3an4,4 ď
 4ź

j“1
 ÿ

nďN an,j,

valid for an,j ě 0. Then, recalling Henriot’s notation of ∆D given in [11, eq. (1.3)], and our
normalisation of rP 1
i , we can estimate the left-hand side of (6.12) by

!∆DN Spmq 1
plog N q4
 3ź

i“1
 ź

pďP 1
i
 ˆ1 ´ 1
p
 ˙´1 ÿ

nďN
pn,Dq“1
 hpnq
n
 3ź

i“1
 ÿ

nďN
 τ 2pnq1pn,PpP 1
i qq“1
n .

48

We upper bound each of the four sums over n by products

!∆DN Spmq 1
plog N q4 ź

pďN
p∤D
 ˆ1 ` hppq
p
 ˙ 3ź

i“1
 ¨

˝ ź

pďP 1
i
 ˆ1 ´ 1
p
 ˙´1 ź

P 1
i ăpďN
 ˆ1 ` 4
p
 ˙˛

‚

!∆DN Spmq 1
plog N q4 ź

pďN
p∤D
 ˆ1 ` hppq
p
 ˙ 3ź

i“1
 ˜log P 1
i
log 2
 ˆ log N
log P 1
i
 ˙4¸
 .

By Mertens’ theorem, this is bounded by

!∆DN Spmq 1
log N
 ź

pďN
p∤D
 ˆ1 ` hppq
p
 ˙ 3ź

i“1
 ˆ log N
log P 1
i
 ˙3 .(6.13)

It remains to consider the ∆D factor. We have

∆D “ ź

p|D
 ¨

˚
˚
˝1 ` 1
p
 ÿ

κ1,κ2,κ3,κ4Pt0,1u
pκ1,κ2,κ3,κ4q‰p0,0,0,0q
 hppκ1q
 3ź

i“1 τ 2ppκi`1q1pěP 1
i
 ˛

‹
‹
‚

! ź

p|D
 ˆ1 ` hppq
p
 ˙ ź

p|D
pěmintP 1
1,P 1
2,P 1
3u
´
1 ` Op1q
p
 ¯
.

Plugging this into (6.13) we are done, since we can assume that hppq “ 0 for p ą N . □

In the next proposition, we show that this upper bound for sums of multiplicative func-
tions, when combined with Lemma 6.2, allows us to estimate correlations of sieves and the
function HR with absolute values. In particular, this shows that the absolute value of a lower
bound sieve is still sieve-like in our additive setup.

Proposition 6.8 (Correlations of absolute values of sieve weights). Let m ě 10 be an integer,
and let ε ą 1{ log log m and N ε ď R, P1 ď N . For 1 ď i ď 3, let the functions fi P tω, Ωu be
pre-sieves as in Definition 2.2, and let P 500
1 ď D1 ď N 1{100. Let HR be as in Theorem 1.2.
Then for any m P r5N {4, 7N {4s and m ” 4 pmod 6q, we have
ÿ

N {2ănďN HRpnq|f1pn ` 2q||f2pm ´ nq||f3pm ´ n ` 2q| ! ε´10N Spmq.

The same bound holds if HRpnq swaps places with any of the other weights on n ` 2, m ´
n, m ´ n ` 2.

Proof. We start by relating all the summands to multiplicative functions. We recall that

HRpnq “ plog Rqτ pnq ż

R
 hξpnq
p1 ` |ξ|q10 dξ,(6.14)

where
 hξppq “ min
!
1, 10p1 ` |ξ|q log p
log R
 )
.

49

We next apply Lemma 6.2 and recall the notation therein (in particular, Pr “ PpP
 ` β´1
β`1 ˘r

1 q).
Since |fipnq| ď rP1pnq ` |fipnq ´ rP1pnq| and rP1pnq “ ś

păP1`1 ´ 1
p ˘´11pn,P0q“1 is the r “ 0
term of the sum below, we get the upper bound

|fipnq| ! ź

păP1
 ˆ1 ´ 1
p
 ˙´1 τ pnq
2 ÿ

rě0 4
´r1pn,Prq“1.

Write aprq :“ ppβ ´ 1q{pβ ` 1qq
r with β “ 200. Then by Mertens’ theorem,

ź

păP1
 ˆ1 ´ 1
p
˙´1 1pn,Prq“1 “ ź

P aprq
1 ďpăP1
 ˆ1 ´ 1
p
˙´1 r
P aprq
1 pnq

!aprq
´1r
P aprq
1 pnq.

Thus, ÿ

N {2ănďN HRpnq|f1pn ` 2q||f2pm ´ nq||f3pm ´ n ` 2q|

!plog Rq ż
R
 1
p1 ` |ξ|q10 ÿ

r1,r2,r3ě0 4
´r1´r2´r3apr1q
´1apr2q
´1apr3q´1Hpξ, r1, r2, r3q dξ,(6.15)

where

Hpξ, r1, r2, r3q “ ÿ

N {2ănďN τ pnqhξpnqpτ 2r
P apr1q
1 qpn ` 2qpτ 2r
P apr2q
1 qpm ´ nqpτ 2r
P apr3q
1 qpm ´ n ` 2q.

This is amenable for an application of Lemma 6.7 (with hppq “ 2hξppq). To prepare this
application, we estimate
ˇ
ˇ
ˇ
ˇ
ˇ
 ź

păN
 ˆ1 ` 2hξppq
p
 ˙ˇ
ˇ
ˇ
ˇ
ˇ ď exp
 ˜ ÿ

pďN
 2hξppq
p
 ¸

! exp
´ ÿ

pďR1{p1`|ξ|q
 20p1 ` |ξ|q log p
p log R ` ÿ

R1{p1`|ξ|qăpďN
 2
p
¯

!
´ log N
log R
 ¯2p1 ` |ξ|q2,

by a trivial bound for |ξ| ą 10{ log R and Mertens’ theorem in the complementary range.
Consequently, an application of Lemma 6.7 gives

Hpξ, r1, r2, r3q

!´ log N
log R
 ¯2p1 ` |ξ|q2 N
log N Spmq
 3ź

i“1
 ˜ log N

log P apriq
1
 ¸3 ź

p|mpm`2qpm`4q

pěmintP apr1q
1 ,P apr2q
1 ,P apr3q
1 u
´
1 ` Op1q
p
 ¯
.

50

Plugging this into (6.15), the integral over ξ converges and we get the upper bound

! N Spmqlog N
log R
 ´ log N
log P1
 ¯9
 ¨

˚
˚
˚
˝
ÿ

rě0 4
´raprq´4 ź

p|mpm`2qpm`4q
pěP aprq
1
 ´
1 ` Op1q
p
 ¯

˛

‹
‹
‹
‚

3
 .

Since R, P1 ě N ε, we have log N
log R ´ log N
log P1
 ¯9 ď ε´10, so that it only remains to show that the

sum over r converges. If P aprq
1 ą log m, then
ź

p|mpm`2qpm`4q
pěP aprq
1
 ´
1 ` Op1q
p
 ¯ ! 1.

On the other hand, we always have
ź

p|mpm`2qpm`4q
pěP aprq
1
 ´
1 ` Op1q
p
 ¯ ! log log m.

Also, recalling β “ 200, we have

ap1q
´4{4 “ ˆβ ` 1
β ´ 1
 ˙4 {4 ă 1{3.

Thus, ÿ

rě0 4
´raprq
´4 ź

p|mpm`2qpm`4q
pěP aprq
1
 ´
1 ` Op1q
p
 ¯ ď ÿ

r 3
´r ` plog log mq ÿ

rě0
P aprq
1 ďlog m
 3
´r.

If P aprq
1 ď log m, then r " log log P1
log log m , so that

plog log mq ÿ

r
P aprq
1 ďlog m
 3
´r ! plog log mq2

log P1 ! plog log mq
3

log m ! 1,

since P1 ě N ε " m
ε and ε ě plog log mq´1. □

7. From primes to Cram´er’s model

In this section, we combine Proposition 6.8 with variants of Gallagher’s prime number
theorem to show results of the type Λpnqωpn ` 2q « rP0pnqωpn ` 2q.
Since the results depend on the possible existence of an exceptional zero, we first define it
and import some well known results about it in Subsection 7.1. Afterwards, in Subsection 7.2
we import or show variants of Gallagher’s prime number theorem. We apply those in Sub-
section 7.3 to show that all of Λ, ΛE˚
3 (if taking into account the possible exceptional zeros)
and the Cram´er model rP are Fourier-close to Heath-Brown’s model ΛR,1. These statements
are combined in Subsection 7.4 to prove Theorem 7.9, which contains Theorem 1.2. From it,
we can quickly deduce Propositions 7.10 and 7.11, which are the key ingredients for proving
Theorem 1.1. 51

7.1. Exceptional zeros. We now define some necessary terminology involving the excep-
tional character and zero.

Definition 7.1 (Exceptional zero). We say that a real number rβ is an exceptional zero of
level P ě 3 and quality κ P p0, 1q if there exists a primitive Dirichlet character rχ of some
modulus rr ď P such that Lp rβ, rχq “ 0 and

rβ ě 1 ´ κ
log P .(7.1)

The character rχ is called an exceptional character and rr is called the exceptional modulus.

By the Landau–Page theorem [22, Corollary 11.10], if there is an exceptional zero of level
P and quality κ, and P is large enough in terms of κ, then the zero is unique, simple and
there is a unique exceptional character, which is a quadratic character. We further have the
well known bound (see [21, equation (4.1)])

1 ´ rβ " 1
rr1{2plog rrq2 .(7.2)

In particular, putting (7.1) and (7.2) together we obtain

rr " ˆ log P
κ log log P
 ˙2 .(7.3)

We need to use the fact that we can choose the quality parameter such that there is either
no exceptional zero or its modulus is small. The procedure for this is standard; for our
purposes, the most suitable is [7, Proposition 7.3.], which we rephrase as follows.

Lemma 7.2. Let R0 “ N δ3
1 and rR “ N 2δ5
1 . There exists an absolute constant λ ą 0 such
that for every δ ą 0 the global parameter δ1 may be chosen with δ1 ď δ so that one of the
following holds.

(1) There are no exceptional zeros of quality λδ2
1 and level R2
0.
(2) If rr is the modulus of an exceptional zero of quality λδ2
1 and level R2
0, then rr ď rR.

7.2. Gallagher-type estimates. Gallagher [5] proved a flexible version of the prime num-
ber theorem in arithmetic progressions that allows moduli up to a power of the summation
range, at the cost of giving only a weak saving. We now state his result and prove three
variants involving first the indicator of the primes without logarithmic weight, then ΛE˚
3 ,
and finally rP pnq.

Lemma 7.3 (Gallagher). Let 2 ď exppplog N q
1{2q ď R ď N . Let 0 ă κ ă 1.

(1) If there is no exceptional zero of level R and quality κ, then we have

ÿ

rďR
 ÿ˚

χ pmod rq max
IĂr1,N s
I interval
 1
|I| ` N {R
 ˇ
ˇ
ˇ
ˇ
ˇ
ÿ

nPIpΛpnqχpnq ´ 1r“1q
ˇ
ˇ
ˇ
ˇ
ˇ ! exp ˆ´cκlog N
log R
 ˙ .

52

(2) If there is an exceptional zero rβ of level R, then if rχ is the exceptional character, we
have ÿ

rďR
 ÿ˚

χ pmod rq max
IĂr1,N s
I interval
 1
|I| ` N {R
 ˇ
ˇ
ˇ
ˇ
ˇ
ÿ

nPIpΛpnqχpnq ´ 1r“1 ` 1χ“ rχn rβ´1q

ˇ
ˇ
ˇ
ˇ
ˇ

!p1 ´ rβqplog N q exp ˆ´c log N
log R
 ˙ .

Proof. This follows from Gallagher’s work [5] after noting that the contribution of prime
powers to the von Mangoldt function is trivial and keeping track of the dependence on the
quality of the zero explicitly. □

We now remove the logarithmic weight of the von Mangoldt function in Lemma 7.3 with
summation by parts.

Lemma 7.4 (Gallagher for prime indicator). Let 2 ď exppplog N q
1{2q ď R ď N 1{7 and
0 ă κ ă 1. We have
(1) If there is no exceptional zero of level R and quality κ, then we have

ÿ

rďR
 ÿ˚

χ pmod rq max
IĂr2,N s
I interval
 log N
|I| ` N {R
 ˇ
ˇ
ˇ
ˇ
ˇ
ÿ

nPI
 ˆ1nPPχpnq ´ 1r“1
log n
 ˙ˇ
ˇ
ˇ
ˇ
ˇ ! exp ˆ´cκlog N
log R
 ˙ .

(2) If there is an exceptional zero rβ of level R and quality κ, then if rχ is the exceptional
character, we have

ÿ

rďR
 ÿ˚

χ pmod rq max
IĂr2,N s
I interval
 log N
|I| ` N {R
 ˇ
ˇ
ˇ
ˇ
ˇ
ÿ

nPI
 ˜

1nPPχpnq ´ 1r“1
log n ` 1χ“ rχn rβ´1

log n
 ¸ˇ
ˇ
ˇ
ˇ
ˇ

!p1 ´ rβqplog N q exp ˆ´clog N
log R
 ˙ .

Proof. Write
 an “ 1nPI
 ˆ1nPPχpnq ´ 1r“1
log n
˙

in the unexceptional case and

an “ 1nPI
 ˜
1nPPχpnq ´ 1r“1
log n ` 1χ“ rχn rβ´1

log n
 ¸

in the exceptional case. The contribution of n ď ?
N is at most R3N ´1{2 log N . By
exppplog N q
1{2q ď R ď N 1{7 this is ! N ´1{14 log N , and hence small enough, using addi-
tionally (7.2) in the exceptional case. In the remaining range n ą ?
N , we apply Lemma 5.2.
Since I X r
?
N , ξs is again an interval, the stated estimate follows from Lemma 7.3, after
handling prime powers trivially. □

We now show a version of Lemma 7.3 for the function ΛE˚
3 (see Definition 3.1).

Lemma 7.5. Let 2 ď exppplog N q4{5q ď R ď N 1{50 and 0 ă κ ă 1.
53

(1) If there is no exceptional zero of level R and quality κ, then we have

ÿ

1ďrďR
 ÿ˚

χ pmod rq max
IĂr1,N s
I interval
 1
|I| ` N {R
 ˇ
ˇ
ˇ
ˇ
ˇ
ÿ

nPIpΛE˚
3 pnqχpnq ´ 1r“1q

ˇ
ˇ
ˇ
ˇ
ˇ ! exp ˆ´cκlog N
log R
 ˙ .

(2) If there is an exceptional zero rβ of level R, then if rχ is the exceptional character, we
have
ÿ

1ďrďR
 ÿ˚

χ pmod rq max
IĂr1,N s
I interval
 1
|I| ` N {R
 ˇ
ˇ
ˇ
ˇ
ˇ
 ÿ

nPI
 ´
ΛE˚
3 pnqχpnq ´ 1r“1 ` 1χ“ rχn rβ´1¯ ˇ
ˇ
ˇ
ˇ
ˇ

! p1 ´ rβqplog N q exp ˆ´clog N
log R
 ˙ .

(7.4)

Proof. Let us prove part (2); part (1) is similar but somewhat easier. Similar to the proof
of the previous Lemma, we apply Lemma 5.2, but here to multiply by cE˚
3 pnq. Every
summand is Op1q, so for each pair pr, χq the terms with n ă N {R4 contribute at most
O`plog N qpN {R4q{pN {Rq˘ “ OpR´3 log N q, and OpR´1 log N q in total. Since rr ď R and
log R ě plog N q
4{5, this is O`p1 ´ rβqplog N q expp´c log N { log Rq
˘ by (7.2), once c is small
enough. We may therefore restrict to I Ă rN {R4, N s, where (3.4) applies. Recalling Defini-
tion 3.1, it then suffices to show for j P t1, 2u the bound

ÿ

1ďrďR
 ÿ˚

χ pmod rq max
IĂrN {R4,N s
I interval
 log N
|I| ` N {R
 ˇ
ˇ
ˇ
ˇ
ˇ
 ÿ

nPI
 ´
1nPBj χpnq ´ cBj pnq1r“1 ` cBj pnq1χ“ rχn rβ´1¯ ˇ
ˇ
ˇ
ˇ
ˇ

! p1 ´ rβqplog N q exp ˆ´c log N
log R
 ˙ .

Let β P r1{2, 1s. Note that for pt1, t2, t3q P rK1, K1 ` 1q ˆ rK2, K2 ` 1q ˆ rK3, K3 ` 1q with
Ki P rN 1{10, N s we have
 t
β´1
3
log t3 “ K β´1
3
log K3 ` OpN ´1{10q

pt1t2t3q
β´1

plog t1qplog t2qplog t3q “ pK1K2K3qβ´1

plog K1qplog K2qplog K3q ` OpN ´1{10q.

We use this to swap between integration and summation and get that for any I Ă rN {R4, N s
we have
ÿ

nPI cB1pnqnβ´1 “ ÿ

nPI n
β´1 ż

1{10ďt1ď1{3´δ1ďt2ďp1´t1q{2
log n
log N ´t1´t2ě1{10
 dt1 dt2
t1t2 logpn{N t1`t2q

“ ż

tPI
 ż

1{10ďt1ď1{3´δ1ďt2ďp1´t1q{2
log t
log N ´t1´t2ě1{10
 t
β´1 dt1 dt2 dt
t1t2 logpt{N t1`t2q ` Op|I|N ´1{9q

“ ÿ

n1n2n3PI
1{10ď log n1
log N ď1{3´δ1ď log n2
log N ďp1´ log n1
log N q{2

log n3
log N ě1{10
 pn1n2n3q
β´1

plog n1qplog n2qplog n3q ` Op|I|N ´1{9q,

54

and similarly for B2. Let S be a polygonal subset of p1{10, 1q3 and for brevity denote
Lpn1, n2, n3q “ pplog n1q{plog N q, plog n2q{plog N q, plog n3q{plog N qq. It now suffices to show

ÿ

1ďrďR
 ÿ˚

χ pmod rq max
IĂrN {R4,N s
I interval
 log N
|I| ` N {R
 ˇ
ˇ
ˇ
ˇ
ˇ
 ÿ

n1n2n3PI
Lpn1,n2,n3qPS
 ˜

1Ppn1q1Ppn2q1Ppn3qχpn1n2n3q

´ 1r“1 ´ 1χ“ rχpn1n2n3q rβ´1

plog n1qplog n2qplog n3q
 ¸ˇ
ˇ
ˇ
ˇ
ˇ

! p1 ´ rβqplog N q exp ˆ´c log N
log R
 ˙ .

When r “ 1 or χ “ rχ, we get the required result, by successively replacing in the sums
over ni the prime indicator (and possibly character) by their expected approximation with
Lemma 7.4, noting that for each fixed n1, n2 the condition n3 P I{pp1p2q, Lpn1, n2, n3q P S
defines a union of intervals. For the remaining characters (r ą 1, χ ‰ rχ) we bound two of
the three prime indicators trivially by 1 and apply Lemma 7.4 to the sum over the third
variable, whose range is again a union of intervals. The resulting sum over r ď R, χ mod r
is directly of the form estimated there, giving the claim by the triangle inequality. Here
the lower bound exppplog N q
4{5q is any convenient value exceeding exppplog N q
1{2q, ensuring
Lemma 7.4 applies on each of the sub-intervals arising above. □

The last Gallagher-type result we need is for P -rough numbers. If P is a sufficiently small
power of N , the exceptional zero plays no role here.

Lemma 7.6. Let N 1{5 ě P ě R10 ě exppplog N q
1{2q ě 2. There exists an absolute constant
c ą 0 such that

ÿ

2ďrďR
 ÿ˚

χ pmod rq max
IĂr1,N s
I interval
 1
|I| ` N {R
 ˇ
ˇ
ˇ
ˇ
ˇ
ÿ

nPI rP pnqχpnq

ˇ
ˇ
ˇ
ˇ
ˇ ! log N
log P exp ˆ´clog P
log R
 ˙ ` exp ˆ´clog N
log P
 ˙ .

(7.5)

Proof. Let us first handle the possible contribution of the exceptional character rχ pmod rrq
of level R. Let λ˘
d be the upper and lower linear sieve coefficients with sifting parameter P
and level D “ N 1{2. Then ÿ

d|n
dďD
 λ
´
d ď 1pn,
ś
pďP pq“1 ď ÿ

d|n
dďD
 λ
`
d ,

so for v P t´1, `1u we have
ÿ

d|n
dďD
 λ´
d 1 rχpnq“v ď 1pn,ś
pďP pq“11 rχpnq“v ď ÿ

d|n
dďD
 λ
`
d 1 rχpnq“v.

Hence, for any v P t´1, `1u and any interval I Ă r1, N s with |I| ě N 9{10, by the P´olya–
Vinogradov inequality and the fundamental lemma of the linear sieve [4, eq. (11.134) and
55

Theorem 11.13] we have
ÿ

nPI 1pn,
ś
pďP pq“11 rχpnq“v ď ÿ

dďD λ
`
d ÿ

nPI
d|n
 1 rχpnq“v

“ ÿ

dďD λ
`
d ÿ

mPI{d
pm,rrq“1
 ˆ1
2 ` v
2 rχpmq
˙

“ φprrq
rr
 ÿ

dďD λ
`
d |I|
d ` OprrDq ` OpDR1{2 log Rq

“ φprrq
rr
 ˆ1 ` O ˆexp ˆ´1
2 log N
log P
 ˙˙˙ ź

pďP
 ˆ1 ´ 1
p
˙ |I|.

By a symmetric argument, we also have the corresponding lower bound. Hence,

1
|I|
 ˇ
ˇ
ˇ
ˇ
ˇ
ÿ

nPI 1pn,
śpďP pq“1 rχpnq

ˇ
ˇ
ˇ
ˇ
ˇ “ 1
|I|
 ˇ
ˇ
ˇ
ˇ
ˇ
ÿ

nPI 1pn,
ś
pďP pq“11 rχpnq“`1 ´ ÿ

nPI 1pn,
ś
pďP pq“11 rχpnq“´1
ˇ
ˇ
ˇ
ˇ
ˇ

! exp ˆ´1
2 log N
log P
 ˙ ź

pďP
 ˆ1 ´ 1
p
 ˙ .

This is an admissible error term, so now it suffices to prove (7.5) with the additional
summation condition χ ‰ rχ.
We write

rP pnq “ ź

păP
 ˆ1 ´ 1
p
 ˙´1 ¨

˚
˝ ÿ

1ďkăplog N q{plog P q
 1
k!
 ÿ

n“p1¨¨¨pk
p1,...,pkěP
 1 ` Op1DpąP : p2|n log N q

˛

‹
‚.

Since P ě R10, the contribution of the term involving higher prime powers is negligible.
Thus, by the triangle inequality and Mertens’ theorem, to show (7.5) it suffices to show that

ÿ

1ďkď log N
log P
 Sk ! log N
log P exp ˆ´clog P
log R
 ˙ ,

where

Sk “ log P
k!
 ÿ

P ďp1,p2,...,pk´1ďN
 ÿ

1ďrďR
 ÿ˚

χ pmod rq
χ‰ rχ
 max
IĂr1,N s
I interval
 1
|I| ` N {R
 ˇ
ˇ
ˇ
ˇ
ˇ
 ÿ

pkPI{pp1p2¨¨¨pk´1q
pkěP
 χppkq
ˇ
ˇ
ˇ
ˇ
ˇ.

If p1p2 ¨ ¨ ¨ pk´1 ą N {P , then by I Ă r1, N s and pk ą P the innermost sum is empty. We
make use of this and insert a factor of 1 “ p1p2¨¨¨pk´1
p1p2¨¨¨pk´1 to arrive at

Sk “ log P
k!
 ÿ

P ďp1,p2,...,pk´1ďN
p1p2¨¨¨pk´1ďN {P
 1
p1p2 ¨ ¨ ¨ pk´1
 ÿ

1ďrďR
 ÿ˚

χ pmod rq
χ‰ rχ
 max
IĂr1,N s
I interval
 p1p2 ¨ ¨ ¨ pk´1
|I| ` N {R
 ˇ
ˇ
ˇ
ˇ
ˇ
 ÿ

pkPI{pp1p2¨¨¨pk´1q
pkěP
 χppkq

ˇ
ˇ
ˇ
ˇ
ˇ.

56

Since we handled the exceptional character separately, we can assume that there exists no
exceptional zero of level R. Thus Lemma 7.4, with N replaced by N {pp1 ¨ ¨ ¨ pk´1q ě P , gives
the estimate

Sk ! 1
k!
 ÿ

P ăp1,p2,...,pk´1ďN
p1p2¨¨¨pk´1ďN {P
 1
p1p2 ¨ ¨ ¨ pk´1 e
´c log P
log R ď 1
k!
 ˆlog log N
log P ` Op1q
˙k´1 exp ˆ´c log P
log R
 ˙ .

By the Taylor expansion of the exponential function, the sum over k of this is

! log N
log P exp ˆ´c log P
log R
 ˙ .

This completes the proof. □

The summation windows in the next subsection have length 2N {R4, coming from Def-
inition 4.5, while the moduli occurring there run over r ď R2 only. We therefore apply
Lemmas 7.3, 7.5 and 7.6 with R4 in place of R, so that the normalising factor |I| ` N {R4

matches the window, and restrict the resulting sum over r to r ď R2. This does not change
the level at which we exclude an exceptional zero. Indeed, an exceptional zero of level R4

and quality κ of modulus at most R2 is by rβ ě 1 ´ κ{ log R4 ě 1 ´ κ{ log R2 also one of level
R2 and quality κ, and conversely an exceptional zero of level R2 and quality κ is one of level
R4 and quality 2κ. If the exceptional modulus exceeds R2, then rχ does not occur among
the primitive characters of modulus r ď R2 and the term 1χ“ rχ may be dropped, which by
1 ´ rβ ď κ{ log R4 turns the exceptional bound of part (2) into the unexceptional one.

7.3. Approximation by Heath-Brown’s model. We now show that both primes (or the
E˚
3 numbers) and the Cram´er model are Fourier-close to Heath-Brown’s model ΛR,1 with a
power saving, if one includes an additional error term that is related to HR. For this purpose,
recall that we let hξ be the multiplicative function supported on square-free integers only
and given on the primes by
 hξppq “ min
!
1, 10p1 ` |ξ|q log p
log R
 )
,

and we set
 HRpnq “ τ pnqplog Rq ż

R
 hξpnq
p1 ` |ξ|q10 dξ.

Proposition 7.7 (From (almost) primes to Heath-Brown’s model). Let exppplog N q1{2q ď
R ď N 1{200 and let Λ˚ P tΛ, ΛE˚
3 u. There exists an arithmetic function E such that the
following hold.
(1) If there is no exceptional zero of level R2 and quality κ, then we have

}Λ˚ ´ ΛR,1 ´ E}
^
8 ! N R´1{3(7.6)
 and
 |Epnq| ! HRpnq exp
`´cκlog N
log R
 ˘.(7.7)
 57

(2) If there is an exceptional zero rβ of level R2 and quality κ with exceptional character
rχ, then we have

}Λ˚ ´ ΛR,1p1 ´ p¨q rβ´1 rχq ` E}
^
8 ! N pR´1{3 ` R´1`op1qrr3{2q(7.8)
 and
 |Epnq| ! HRpnqp1 ´ rβqplog N q exp
`´c log N
log R
 ˘.(7.9)

Proof. Let us first consider the unexceptional case. Recall the definition of bR in Defini-
tion 4.5. By Lemma 4.6, the combinatorial decomposition in Lemma 5.3 and standard
minor arc bounds [12, Lemma 13.7, 13.8], we have for Λ
˚ P tΛ, ΛE˚
3 u the bound

}Λ˚ ´ Λ˚ ˚ bR}
^
8 ! N R´1{3.(7.10)

Of course, with slightly weaker R dependence this also follows immediately from Lemma 5.8.
Recall the definition of ΛR,r in (4.5) and let

E0pnq :“ ÿ

n1`n2“n bRpn1qΛpn2q1p|n2ñpďR2

´ ÿ

rďR2
 ÿ˚

χ pmod rq χpnq r
φprq ΛR,rpnq
ř
|n1´n|ďN {R4 Λ˚pn1q1p|n1ñpďR2χpn
1q

2N {R4

account for the discrepancy of potential prime power divisor less than R2. By Lemma 4.10
and the fact that ΛR,r vanishes for r ą R2, we have for n P pN {2, N s that

Λ˚ ˚ bRpnq “ ÿ

rďR2
 ÿ˚

χ pmod rq χpnq r
φprq ΛR,rpnq
 ř

|n1´n|ďN {R4 Λ˚pn1qχpn1q

2N {R4 ` E0pnq

“ ΛR,1pnq ` E1pnq ` E0pnq,

where
 E1pnq “ ÿ

rďR2
 ÿ˚

χ pmod rq χpnq r
φprq ΛR,rpnq
 ř

|n1´n|ďN {R4pΛ˚pn1qχpn1q ´ 1r“1q

2N {R4 .

We first bound E0 in L
1. Both sums defining E0 collect the non-R2-rough discrepancy that
Lemma 4.10 does not capture, and are supported on n divisible by a prime power pk with
p ď R2. Estimating each sum trivially, using
ÿ

pďR2
 ÿ

kě1
pkďN
 log p ! R2 log N

together with the normalisation of bR and the bound }ΛR,r}8 ! HR of Lemma 4.11, we
obtain ÿ

n |E0pnq| ! R2`op1q ! N R´1{3,

the last step since R ď N 1{200. As E enters the proposition only through the Fourier norm
} ¨ }^
8 ď } ¨ }1 (via (7.6) and the downstream application of Lemma 4.2), this L1 bound
makes E0 admissible in the required averaged sense, and it is absorbed into the N R´1{3

58

error of (7.6). Only E1 needs the pointwise bound (7.7), so we set E :“ E1. By Lemma 4.11,
and the unexceptional cases of Lemmas 7.3 and 7.5, applied with R4 in place of R, we have

|E1pnq| !HRpnq ÿ

rďR2 max
1ďnďN
 ÿ˚

χ pmod rq
 ˇ
ˇ
ˇ
ˇ
ˇ
ř

|n1´n|ďN {R4pΛ˚pn
1qχpn
1q ´ 1r“1q

2N {R4
 ˇ
ˇ
ˇ
ˇ
ˇ

!HRpnq exp
`´cκlog N
log R
 ˘.

This shows (7.7) (with E “ E1) and completes the proof of the unexceptional case.
We now consider the exceptional case. To proceed we need to extract the contribution of
the exceptional zero to Λ˚ ˚ bR. We have

Λ˚ ˚ bRpnq “ ΛR,1pnq ´ rχpnq rr
φprrq ΛR,rrpnqn rβ´1 ` E2pnq ` O ˆlog N
R
 ˙ ,(7.11)

where we used the estimate
ř
|n1´n|ďN {R4pn1q rβ´1

2N {R4 “ n rβ´1 ` O´ log N
R
 ¯
(7.12)

coming from the mean value theorem and wrote

E2pnq “ ÿ

rďR2
 ÿ˚

χ pmod rq χpnq r
φprqΛR,rpnq
ř
|n1´n|ďN {R4pΛ˚pn
1qχpn
1q ´ 1r“1 ` 1χ“ rχpn1q rβ´1q

2N {R4 .

Here, Lemma 4.11 and the exceptional cases of Lemmas 7.3, 7.5, applied with R4 in place of
R, show that
 |E2pnq| ! HRpnqp1 ´ rβqplog N q exp ˆ´c log N
log R
 ˙ .

Thus E2 is admissible for (7.9). Absorbing E0 into the N R´1{3 error as in the unexceptional
case and setting E :“ E2, we have so far proved the existence of an admissible function E
such that
 }Λ˚ ´ ΛR,1 ` p¨q rβ´1 rχΛR,rr ` E}^
8 ! N R´1{3.

To show (7.8) and thus complete the proof of the proposition, we need to replace ΛR,rr by
ΛR,1. For this, it suffices to show that

}F }
^
8 ! N R´1`op1qrr3{2,(7.13)

where
 F pnq “ΛR,1pnq ´ rχpnq rr
φprrqΛR,rrpnqn rβ´1 ´ p1 ´ rχpnqn rβ´1qΛR,1pnq

“rχpnqn rβ´1`ΛR,1pnq ´ rr
φprrqΛR,rrpnq
˘.

59

We have F pnq “ 0 unless pn, rrq “ 1. Opening the definition of ΛR,1 and writing q1 “ dq
where d | rr and pq, rrq “ 1, we get

ΛR,1pnq “ ÿ

q1
 µpq1qcq1pnq
φpq1q G ˆ log q1
log R
 ˙

“ ÿ

d|rr
 ÿ

pq,rrq“1
 µpdqqcdqpnq
φpdqq G ˆlog dq
log R
 ˙

“ ÿ

pq,rrq“1
 µpqqcqpnq
φpqq
 ÿ

d|rr
 µpdqcdpnq
φpdq G ˆ log dq
log R
 ˙

“ ÿ

pq,rrq“1
 µpqqcqpnq
φpqq
 ÿ

d|rr
 µpdq2

φpdq G ˆlog dq
log R
 ˙ ,

since cdpnq “ µpdq for pd, nq “ 1. Thus, for pn, rrq “ 1, we get

ΛR,1pnq ´ rr
φprrq ΛR,rrpnq “ ÿ

pq,rrq“1
 µpqqcqpnq
φpqq
 ¨

˝
ÿ

d|rr
 µpdq2

φpdq G ˆ log dq
log R
 ˙ ´ rr
φprrq G ˆ log rrq
log R
 ˙˛

‚

“ E3pnq ` E4pnq,

say, where E3pnq accounts for the contribution of q ď R{rr and E4pnq for the remaining q.
We claim E3pnq “ 0. Indeed, recalling that Gptq “ 1 for 0 ď t ď 1 we have for q ď R{rr that
ÿ

d|rr
 µpdq
2

φpdq G ˆ log dq
log R
 ˙ ´ rr
φprrq G ˆ log rrq
log R
 ˙ “ ÿ

d|rr
 µpdq2

φpdq ´ rr
φprrq

“ 0.

Thus, (7.13) follows, if we can show

}rχp¨q rβ´1E4}
^
8 ! N R´1`op1qrr3{2.(7.14)

By Lemma 4.3 we have
 }rχp¨q rβ´1E4}^
8 ! ?rr}p¨q rβ´1E4}^
8.

We then estimate the Fourier transform of p¨q rβ´1E4 at α P R as
ÿ

nďN n rβ´1E4pnqepαnq

“ ÿ

pq,rrq“1
qąR{rr
 µpqq
φpqq
 ¨

˝
ÿ

d|rr
 µpdq
2

φpdq G ˆlog dq
log R
 ˙ ´ rr
φprrq G ˆ log rrq
log R
 ˙˛

‚ ÿ˚

a pmod qq
 ÿ

nďN n rβ´1e pnpα ´ a{qqq

! ÿ

pq,rrq“1
R{rrăqďR2
 Rop1q

q
 ÿ˚

a pmod qq
 ˇ
ˇ
ˇ
ˇ
ˇ
 ÿ

nďN n rβ´1e pnpα ´ a{qq
ˇ
ˇ
ˇ
ˇ
ˇ .

By partial summation (or [7, Proposition 5.3]), the sum over n is bounded by mintN, }α ´
a{q}´1u. Observe that the appearing fractions a{q are at least R´4-spaced. The nearest
60

fraction to α (with q ą R{rr) we estimate trivially by mint¨u ď N , contributing ! Rop1qN {q !
Rop1qN rr{R. The remaining R´4-spaced fractions contribute ! Rop1q ř1 }α´a{q}´1 ! R4`op1q.
Hence the previous expression is

! N Rop1qrr
R ` R4`op1q ! N Rop1qrr
R .

Thus, (7.14) follows, and this was enough to complete the proof. □

Proposition 7.8 (From Cram´er to Heath-Brown). Let exppplog N q
1{2q ď R40 ď P ď N 1{5.
There exists an arithmetic function E such that the following hold.
(1) We have
 }rP ´ ΛR,1 ´ E}^
8 ! N R´1{3(7.15)
 and
 |Epnq| ! HRpnq´log N
log P exp
`´c log P
log R
 ˘ ` exp
`´clog N
log P
 ˘¯.(7.16)

(2) Let β P p1{2, 1q, and let χ be a primitive quadratic character of modulus r P N. Then
we have
 }rP p1 ´ p¨qβ´1χq ´ ΛR,1p1 ´ p¨qβ´1χq ` E}
^
8 ! N R´1{3r1{2.(7.17)
 Here E fulfils again (7.16), and now additionally

1χpnq“1|Epnq| ! HRpnqp1 ´ βqplog N q´log N
log P exp ˆ´clog P
log R
 ˙ ` exp ˆ´clog N
log P
 ˙¯.(7.18)

Proof. The proof of (7.15) and (7.16) is identical to the one of Proposition 7.7 in the unex-
ceptional case, apart from using Lemma 7.6, applied with R4 in place of R, here.
To prove the statements involving a quadratic character, let f1pnq “ rP pnqp1 ´ χpnqnβ´1q.
We first approximate this by f2pnq “ p1 ´ χpnqnβ´1qprP ˚ bRqpnq and claim that

}f1 ´ f2}^
8 ! N R´1{3?
r.(7.19)

By the triangle inequality

}f1 ´ f2}
^
8 ď }rP ´ rP ˚ bR}
^
8 ` }p¨qβ´1χ ¨ prP ´ rP ˚ bRq}^
8.

By a standard minor arc bound based on Lemma 5.3 and [12, Lemmas 13.7 and 13.8], the
first part is acceptably small. To estimate the second term on the right, we remove the
character with Lemma 4.3 and move the weight n
β´1 inside the convolution. By Lemma 4.8
with ψpnq “ nβ´1 and the upper bound

}ψ11rN {3,2N s}8 ď N ´1

we then have

}p¨qβ´1χ ¨ prP ´ rP ˚ bRq}^
8 ! ?
r´
}rP p¨q
β´1 ´ rP p¨q
β´1 ˚ bR}^
8 ` N R´1¯
.

The remaining Fourier norm is sufficiently small by Lemmas 4.6 and 5.9. The bound (7.19)
follows. 61

We now consider f2. We rewrite the convolution with multiplicative characters as in (4.6)
and extract an error term to get

f2pnq “ p1 ´ χpnqnβ´1qΛR,1pnq ` E2pnq,(7.20)

where

E2pnq “ p1 ´ χpnqn
β´1q ÿ

qďR2
 ÿ˚

ψ pmod qq ψpnq q
φpqq ΛR,qpnq
 ř

|n1´n|ďN {R4prP pn1qψpn1q ´ 1q“1q

2N {R4 .

Observe that
 1χpnq“1p1 ´ χpnqnβ´1q ď 1 ´ n
β´1 ! p1 ´ βq log N,

so that an application of Lemmas 4.11 and 7.6, applied with R4 in place of R, for the terms
2 ď q ď R2, together with the mean-value estimate for rP bounding the q “ 1 term by
HRpnq expp´c log N { log P q, shows that

|E2pnq| !HRpnq´log N
log P exp ˆ´clog P
log R
 ˙ ` exp ˆ´c log N
log P
 ˙¯

1χpnq“1|E2pnq| !HRpnqp1 ´ βq log N ´ log N
log P exp ˆ´c log P
log R
 ˙ ` exp ˆ´clog N
log P
 ˙¯
.

This implies that E2 satisfies both (7.16) and (7.18). □

7.4. Approximation by Cram´er’s model. We now combine Propositions 7.7 and 7.8 to
go from Λ
˚ to rP in Fourier space. This is the final ingredient we need to achieve the goal
of this section, which is the proof of Propositions 7.10 and 7.11. Note that Theorem 1.2 is
contained as a special case.

Theorem 7.9 (Fourier-approximating primes by Cram´er). Let exppplog N q
1{2q ď R40 ď P ď
N 1{5, and let Λ˚ P tΛ, ΛE˚
3 u. There exists an arithmetic function E such that the following
hold.
(1) If there is no exceptional zero of level R2 and quality κ, then we have

}Λ˚ ´ rP ´ E}
^
8 ! N R´1{3(7.21)
 and
 |Epnq| ! HRpnq
´ log N
log P exp
`´c log P
log R
 ˘ ` exp
`´cκlog N
log R ´ c log N
log P
 ˘¯
.(7.22)

(2) If there is an exceptional zero rβ of level R2, then if rχ is the exceptional character,
we have
 }Λ˚ ´ rP p1 ´ p¨q rβ´1 rχq ` E}^
8 ! N pR´1{3rr1{2 ` R´1`op1qrr3{2q.(7.23)
 Here E satisfies again (7.22), and now additionally

1 rχpnq“1|Epnq| ! HRpnqp1 ´ rβqplog N q ˆ log N
log P exp
`´clog P
log R
 ˘ ` exp
`´c log N
log P
 ˘˙ .(7.24)
 62

Proof. This is an immediate consequence of Propositions 7.7 and 7.8, and the triangle in-
equality, part (2) being obtained by combining (7.8) with (7.17) at χ “ rχ, β “ rβ, r “ rr,
whose R´1{3rr1{2 dominates the R´1{3 of (7.8). □

Proposition 7.10 (Reduction to Cram´er model, unexceptional case). Let P0 “ N δ1, R0 “
N δ3
1 , P1 “ N δ4
1 , D1 “ N δ3
1 {100, and let λ be the constant from Lemma 7.2. Let f P tω, Ωu be
a pre-sieve as in Definition 2.2. Assume there is no exceptional zero of level R2
0 and quality
λδ2
1. Then, for any ϵ " e
´cδ´1{2
1 , we have

Λpnqf pn ` 2q «ϵ rP0pnqf pn ` 2q,

f pnqΛE˚
3 pn ` 2q «ϵ f pnqrP0pn ` 2q.

Proof. We only consider the case Λpnqf pn ` 2q, the other case being similar. We apply
Theorem 7.9 with P “ P0, R “ R0 and let Epnq be as in (7.21). Discarding the sieve weights
with Lemma 4.3, we get

}f `pΛ ´ rP0 ´ Eq}
^
8 ! D1N R´1{3
0 ! N 1´δ3
1 {3`δ3
1 {100.

By Lemma 4.2 we obtain

Λpnqf pn ` 2q «ϵ rP0pnqf pn ` 2q ` Epnqf pn ` 2q

as long as ϵ " N ´pδ1{10q4, which is much better than required.
By (7.22) and the choice of parameters,

|Epnq| ! HR0pnq´
δ´1
1 e
´cδ´2
1 ` e
´cδ2
1 δ´3
1 ´cδ´1
1 ¯ ! HR0pnqe´cδ´1
1 .

Then, an application of Proposition 6.8 gives us
ÿ

N {2ănďN |Epnq||f pn ` 2q|Ωpm ´ nqΩpm ´ n ` 2q ! δ´40
1 e
´cδ´1
1 N Spmq

! e´cδ´1{2
1 N Spmq,

if δ1 is small enough in absolute terms. This implies the proposition, after recalling that
in Definition 2.4 the companion function gpnq is majorised in absolute value by ΩpnqΩpn `
2q. □

Proposition 7.11 (Reduction to Cram´er model, exceptional case). Let P0 “ N δ1, R0 “
N δ3
1 , P1 “ N δ4
1 , D1 “ N δ3
1 {100, λ the constant from Lemma 7.2 and let f P tω, Ωu be a pre-
sieve as in Definition 2.2. Assume that rχ is the exceptional character with exceptional zero
rβ of quality λδ2
1 and level R2
0. Then for any ϵ ą e
´cδ´1{2
1 , we have

1 rχpnq“´1Λpnqf pn ` 2q «ϵ 1 rχpnq“´1p1 ` n rβ´1qrP0pnqf pn ` 2q,

1 rχpnq“´1f pnqΛE˚
3 pn ` 2q «ϵ cE˚
3 1 rχpnq“´1f pnqp1 ´ rχpn ` 2qn rβ´1qrP0pn ` 2q.

Further, for rϵ ą p1 ´ rβqplog N qe´cδ´1{2
1 , it holds that

1 rχpnq“ rχpn`2q“1Λpnqf pn ` 2q «rϵ 1 rχpnq“ rχpn`2q“1p1 ´ n rβ´1qrP0pnqf pn ` 2q,

1 rχpnq“ rχpn`2q“1f pnqΛE˚
3 pn ` 2q «rϵ 1 rχpnq“ rχpn`2q“1p1 ´ n rβ´1qf pnqrP0pn ` 2q.
63

Proof. We again only handle the case of Λpnqf pn ` 2q, the others being similar (noting that
pn ` 2q rβ´1 can be replaced by n rβ´1 with respect to « by Taylor expansion). We start with
the observation that 1 rχpnq“˘1 “ 1
2p1 ˘ rχpnqq that holds for pn, rrq “ 1 and write cpnq for
1 rχpnq“´1 or 1 rχpnq“ rχpn`2q“1 and dpnq “ 1 ´ rχpnqn rβ´1. Note that higher prime powers can be
again discarded easily.
By Lemma 7.2 we can assume that the exceptional modulus is bounded by rR “ N 2δ5
1 . We
use this bound to apply the exceptional case of Theorem 7.9 with P “ P0 “ N δ1, R “ R0 “
N δ3
1 together with Lemma 4.3 and Lemma 7.2 to get

}cf `pΛ ´ rP0d ` Eq}
^
8 ! rR2D1N R´1{3
0 “ N 1`4δ5
1 `δ3
1 {100´δ3
1 {3 ! N 1´δ3
1 {4,

where Epnq can be estimated by (7.24). By Lemma 4.2, we have

cpnqΛpnqf pn ` 2q «ϵ1 cpnqrP0pnqdpnq ` cpnqEpnqf pn ` 2q.

for any ϵ
1 ą N ´δ4
1 . This is acceptable, as both ϵ and rϵ are larger than the lower bound for ϵ
1

by (7.2).
In the case cpnq “ 1 rχpnq“´1 we have

cpnqdpnq “ 1 rχpnq“´1p1 ` n rβ´1q,

and we trivially bound
 |1 rχpnq“´1Epnq| ď |Epnq|.

So, just as in the unexceptional case (see proof of Proposition 7.10), we get

cpnqEpnqf pn ` 2q «ϵ 0

in the required range of ϵ.
In the case cpnq “ 1 rχpnq“ rχpn`2q“1 we have

cpnqdpnq “ 1 ´ n rβ´1,

and we can make use of the improved error in (7.24) to get

1 rχpnq“ rχpn`2q“1Epnqf pn ` 2q «rϵ 0.
 □

8. Proof of Theorem 1.1

We are now ready to prove Theorem 1.1. We again consider the unexceptional case and
exceptional case separately. For the proof it is convenient to extend the «ϵ notation, given
by Definition 2.4, to allow for lower bounding.

Definition 8.1. Let ϵ ą 0 and f, g be finitely supported arithmetic functions. We write
f Çϵ g if there exists a sequence of functions fi, 0 ď i ď J with f0 “ f, fJ “ g and either
fi «ϵ fi`1 or fi ě fi`1. 64

8.1. Unexceptional Case. We now prove Theorem 1.1 in the unexceptional case. Before
we do this, we include the following remark that explains some of the choices we make.

Remark 8.2. It is at this point that we use the hierarchy of parameters in Definition 2.1.
We now summarise the reasoning and in particular explain why the proof below requires us
to work with two roughness scales P0, P1, instead of the one scale as in the sketch in the
introduction.
Proposition 7.10 applies Theorem 7.9 with P “ P0 and R “ R0. Its error term (7.22) is
admissible only when both log N
log P0 and log P0
log R0 are large, which requires N Ï P0 Ï R0.

Next, Theorem 7.9 produces in (7.21) a saving of R´1{3
0 , which needs to be sufficient to
compensate the loss of D1 from discarding the sieve weights with Lemma 4.3. This forces
D1 ! R1{3
0 .
The application of the fundamental lemma type bound of Lemma 6.2 in Proposition 6.3
requires D1 Ï P1.
Finally, the major arc estimate of Lemma 5.6, which is the main input to Proposition 5.1,
is of size N 1`op1qpP ´1{2
1 R1{2
1 ` R´1
1 q and saves only for R1 a power of N with P1 " R1.
In particular, this explains the difference in size of P1 and P0, and why the direct appli-
cation of our results will, in the language of Proposition 3.4, produce

g1pnq «ϵ VpωMq rP0pnqrP1pn ` 2q,

g2pnq «ϵ p3{5 ` δ1qcE˚
3 VpΩMq rP1pnqrP0pn ` 2q,

the scale P0 appearing where Λ, respectively ΛE˚
3 , stood. Thus, to create identical terms
apart from constants, we need to include an additional step in which we descend from rP0
to rP1. We do so by writing rP0 “ rP1rrP1,P0q and inserting for rrP1,P0q the intermediate sieve
of Lemma 3.5, which we then remove with Proposition 5.1. This is possible because at this
point of the argument we can freely switch between P1-rough numbers and lower and upper
bound pre-sieves with Corollary 6.4, recalling ω ď rP1 ď Ω.

We are now able to show the following lemma from which the unexceptional case of
Theorem 1.1 will follow quickly.

Lemma 8.3. Let P1 “ N δ4
1 , R0 “ N δ3
1 and λ the constant from Lemma 7.2. Assume that
there exists no exceptional zero of level R2
0 and quality λδ2
1. There exists c1 ą 0 such that for
ϵ “ e
´cδ´1{2
1 we have
 ΛpnqΛ2pn ` 2q Çϵ c1rP1pnqrP1pn ` 2q.(8.1)

Proof of Lemma 8.3. We fix again the choices P0 “ N δ1, D1 “ N δ3
1 {100 and start by applying
Proposition 3.4 which gives us the existence of main-sieves ωM, ΩM, Ω
1
M as in Definition 2.3
such that
 ΛpnqΛ2pn ` 2q Çϵ g1pnq ´ g2pnq ` g3pnq,(8.2)

with
 g1pnq “ ΛpnqΩpn ` 2qωMpn ` 2q

g2pnq “ p3{5 ` δ1qcE˚
3 ΩpnqΩMpnqΛE˚
3 pn ` 2q

g3pnq “ Λpnq`ω ´ Ω
˘pn ` 2qΩ
1
Mpn ` 2q.

65

We define the following constants that are related to our main-sieves:

VpωMq :“ ź

P1ďpăN 1{10
 ˆ1 ´ 1
p
˙´1 ÿ

d
 λω
Mpdq
φpdq

VpΩMq :“ ź

P1ďpăN 1{10
 ˆ1 ´ 1
p
˙´1 ÿ

d
 λΩ
Mpdq
φpdq

VpΩ
1
Mq :“ ź

P1ďpăN 1{10
 ˆ1 ´ 1
p
˙´1 ÿ

d
 λΩ1
M pdq
φpdq .

Here each Vp¨q carries the same normalising product ś
P1ďpăN 1{10p1 ´ 1{pq
´1 emitted by
Proposition 5.1, even though ΩM is constructed on the larger range rP1, N 1{6q — this delib-
erate normalisation is the source of the constant 3{5 in g2. The next task is to remove the
main-sieve. Proposition 5.1 together with the fact that ϵ “ e
´cδ´1{2
1 ě N ´pδ1{10q4 gives us

g1pnq «ϵ VpωMqΛpnqΩpn ` 2q

g2pnq «ϵ VpΩMqp3{5 ` δ1qcE˚
3 ΩpnqΛE˚
3 pn ` 2q

g3pnq «ϵ VpΩ
1
MqΛpnq
`ω ´ Ω
˘pn ` 2q.

We consider the contribution of each gi separately now. We start with g3 and show that
it is negligible. Indeed, using the facts that Ω ě ω, that VpΩ
1
Mq is bounded by (3.8), and
applying Corollary 6.4, we get

0 ě VpΩ
1
MqΛpnq
`ω ´ Ω˘pn ` 2q

" VpΩ
1
Mqδ´4
1 Ωpnq`ω ´ Ω
˘pn ` 2q
«ϵ 0,

as long as ϵ " δ´4
1 e
´δ´1
1 {10, which is acceptable. Thus,

g3pnq «ϵ 0.(8.3)

For g1, an application of Proposition 7.10 shows

g1pnq «ϵ VpωMqrP0pnqΩpn ` 2q.

By definition rP0 “ rP1rrP1,P0q and we can use Lemma 3.5 to lower bound

rP0 ě rP1ωrP1,P0q.

Since Ω is non-negative, we obtain

g1pnq Çϵ VpωMqrP1ωrP1,P0qpnqΩpn ` 2q.

We now remove the rP1, P0q sieve component via Proposition 5.1. Together with (3.16) of
Lemma 3.5 and two applications of Corollary 6.4 (recalling ω ď rP1 ď Ω), we obtain

g1pnq Çϵ VpωMqrP1ωrP1,P0qpnqΩpn ` 2q

«ϵ VpωMqrP1pnqrP1pn ` 2q.(8.4)

For g2 we similarly apply first Proposition 7.10 to get

g2pnq «ϵ VpΩMqp3{5 ` δ1qcE˚
3 ΩpnqrP0pn ` 2q.

66

We can then follow the same steps as for g1, with the exception of using an upper bound
sieve in the range rP1, P0q, since g2 appears with negative sign. This shows

´g2pnq Çϵ ´VpΩMqp3{5 ` δ1qcE˚
3 rP1pnqrP1pn ` 2q.(8.5)

Combining (8.2), (8.3), (8.4), and (8.5), we have shown that

ΛpnqΛ2pn ` 2q Çϵ
 ˆVpωMq ´ VpΩMqp3{5 ` δ1qcE˚
3
 ˙rP1pnqrP1pn ` 2q.

By (3.9), the leading constant is lower bounded away from 0 if δ1 is small enough in absolute
terms. □

Proof of Theorem 1.1 in the unexceptional case. Applying a simple upper bound sieve, we
see that
 ΛpnqΛ2pn ` 2q ď δ´8
1 rP1pnqrP1pn ` 2q

ď δ´8
1 ΩpnqΩpn ` 2q.

Thus, by the non-negativity of ΛpnqΛ2pn ` 2q, the definition of Çϵ, and Lemma 8.3, there
exist a constant c1 ą 0 and a function E1 fulfilling

ΛΛ`
2 ˚ ΛΛ`
2 pmq ě c1ΛΛ`
2 ˚ rP1r`
P1pmq ` ΛΛ`
2 ˚ E1pmq,

and such that for all natural numbers m P r5N {4, 7N {4s with at most N 1´pδ1{10q4 exceptions
we have
 |ΛΛ`
2 ˚ E1pmq| ! δ´8
1 e
´cδ´1{2
1 mSpmq.

Similarly, using the non-negativity of rP1pnqrP1pn ` 2q, there exists a function E2 whose
contribution is bounded in the same manner and such that

c1ΛΛ`
2 ˚ rP1r`
P1pmq ě c2
1rP1r`
P1 ˚ rP1r`
P1pmq ` E2 ˚ rP1r`
P1pmq.

Finally, using upper and lower bound pre-sieves in conjunction with Corollary 6.4 and Propo-
sition 6.3, we get the asymptotics

rP1r`
P1 ˚ rP1r`
P1pmq “ mSpmq ` O ´
mSpmqe´δ´1
1 {10¯ .

If δ1 is sufficiently small in absolute terms, the factors e´δ´1
1 {10 and δ´8
1 e´cδ´1{2
1 are small. We
conclude from our chain of inequalities and error term estimates that

ΛΛ`
2 ˚ ΛΛ`
2 pmq ě c2
1
2 mSpmq

for all natural numbers m P r5N {4, 7N {4s with ! N 1´pδ1{10q4 exceptions. Since Spmq " 1
for all m ” 4 pmod 6q, this proves Theorem 1.1 in the unexceptional case, after sorting m
into intervals of the form r5N {4, 7N {4s. □
67

8.2. Exceptional Case. The exceptional case of Theorem 1.1 works in broad terms simi-
larly to the unexceptional case, apart from two additional technical complications described
in the introduction, see Subsection 1.2.5.

Lemma 8.4. Let P1 “ N δ4
1 , R0 “ N δ3
1 and λ the constant from Lemma 7.2. Assume that
there exists an exceptional character rχ with exceptional zero rβ of level R2
0 and quality λδ2
1.
There exist c1 ą 0 such that the following holds. Let

ϵ “ e´cδ´1{2
1 , rϵ “ ϵp1 ´ rβq log N.

We have
 1 rχpnq“´1ΛpnqΛ2pn ` 2q Çϵ c11 rχpnq“´1rP1pnqrP1pn ` 2q(8.6)
 1 rχpnq“ rχpn`2q“1ΛpnqΛ2pn ` 2q Çrϵ c1p1 ´ rβqplog N q1 rχpnq“ rχpn`2q“1rP1pnqrP1pn ` 2q.(8.7)

Proof of Lemma 8.4. Let cpnq “ 1 rχpnq“´1 or cpnq “ 1 rχpnq“ rχpn`2q“1 for the two cases we need
to consider. We start as in the proof of Lemma 8.3 and apply Proposition 3.4 to lower bound

cpnqΛpnqΛ2pn ` 2q ě cpnq`g1pnq ´ g2pnq ` g3pnq
˘.

By Lemma 7.2, after possibly decreasing the size of δ1, we can assume that condprχq ď rR,
and recalling (7.2) we consequently have rϵ ą N ´δ4
1 . This allows us to remove the main-sieves
using the second statement of Proposition 5.1. We get

cpnqg1pnq «rϵ cpnqVpωMqΛpnqΩpn ` 2q

cpnqg2pnq «rϵ cpnqVpΩMqp3{5 ` δ1qcE˚
3 ΩpnqΛE˚
3 pn ` 2q

cpnqg3pnq «rϵ cpnqVpΩ
1
MqΛpnq
`ω ´ Ω˘pn ` 2q.

By the same argument as in the unexceptional case,

cpnqg3pnq «ϵ 0.

To improve this in the case cpnq “ 1 rχpnq“ rχpn`2q“1, we first apply Proposition 7.11 to replace
the Λ component. Together with Corollary 6.4 and the bound 1 ´ n rβ´1 ! p1 ´ rβq log n, this
yields
 1 rχpnq“ rχpn`2q“1VpΩ1
MqΛpnq
`ω ´ Ω
˘pn ` 2q

«rϵ1 rχpnq“ rχpn`2q“1VpΩ1
Mqp1 ´ n rβ´1qrP0pnq
`ω ´ Ω˘pn ` 2q
«rϵ0.

Apart from replacing Proposition 7.10 by Proposition 7.11, we can follow the same steps
as in the unexceptional case to get

1 rχpnq“´1g1pnq Çϵ VpωMqp1 ` n rβ´1qrP1pnqrP1pn ` 2q

and
 ´1 rχpnq“´1g2pnq Çϵ ´VpΩMqp3{5 ` δ1qcE˚
3 p1 ´ rχpn ` 2qn rβ´1qrP1pnqrP1pn ` 2q

ě ´VpΩMqp3{5 ` δ1qcE˚
3 p1 ` n rβ´1qrP1pnqrP1pn ` 2q.

68

Combining the terms and discarding the non-negative n rβ´1 term, (8.6) follows. The remain-
ing case (8.7) is proved in the same way: we either immediately get «rϵ from Proposition 7.11
or have a factor of p1 ´ rβqplog N q that improves the approximation correspondingly. □

Proof of Theorem 1.1 in the exceptional case. We partition the relevant m according to whether
σ1pmq ě ´1{2 or σ1pmq ă ´1{2, and bound the exceptional set within each class separately.
As 0 ď 1 rχpnq“´1 ď 1,
 ΛΛ`
2 ˚ ΛΛ`
2 pmq ě 1 rχp¨q“´1ΛΛ`
2 ˚ 1 rχp¨q“´1ΛΛ`
2 pmq.

We use (8.6) of Lemma 8.4 and follow the same strategy as in the unexceptional case to get

1 rχp¨q“´1ΛΛ`
2 ˚ 1 rχp¨q“´1ΛΛ`
2 pmq ě c2
11 rχp¨q“´1rP1r`
P1 ˚ 1 rχp¨q“´1rP1r`
P1pmq ` rEpmq,

where
 | rEpmq| ! δ´8
1 e
´cδ´1{2
1 mSpmq.

for all natural numbers m P r5N {4, 7N {4s with at most OpN 1´pδ1{10q4q exceptions. By the
first case of Proposition 6.5 and the lower bound of the exceptional modulus (7.3) we get

1 rχp¨q“´1rP1r`
P1 ˚ 1 rχp¨q“´1rP1r`
P1pmq “ mSpmq ˆ 1 ` σ1pmq
4 ` Opδ´5
1 plog N q
´1q
˙ `1 ` Ope
´cδ´1
1 q
˘.

This shows that
 ΛΛ`
2 ˚ ΛΛ`
2 pmq ě 1
10mSpmq

for all natural numbers m P r5N {4, 7N {4s with

σ1pmq ě ´1{2,

apart from OpN 1´pδ1{10q4q exceptions. It remains to prove Theorem 1.1 under the assumption
that
 σ1pmq ă ´1{2.(8.8)

Multiplying now one of the functions with 1 rχp¨q“ rχp¨`2q“1, we have

ΛΛ`
2 ˚ ΛΛ`
2 pmq ě 1 rχp¨q“´1ΛΛ`
2 ˚ 1 rχp¨q“ rχp¨`2q“1ΛΛ`
2 pmq.

By (8.7) there exists an arithmetic function rE1 with

1 rχp¨q“´1ΛΛ`
2 ˚ 1 rχp¨q“ rχp¨`2q“1ΛΛ`
2 pmq

ěc1p1 ´ rβqplog N q1 rχp¨q“´1ΛΛ`
2 ˚ 1 rχp¨q“ rχp¨`2q“1rP1r`
P1pmq ` OpΛΛ`
2 ˚ rE1pmqq

such that
 |ΛΛ`
2 ˚ rE1pmq| ! δ´8
1 p1 ´ rβqplog N qe´cδ´1{2
1 mSpmq

69

for all natural numbers m P r5N {4, 7N {4s with at most OpN 1´pδ1{10q4q exceptions. Using the
non-negativity of rP1pnqrP1pn ` 2q and (8.6), there exists an arithmetic function rE2 such that

c1p1 ´ rβqplog N q1 rχp¨q“´1ΛΛ`
2 ˚ 1 rχp¨q“ rχp¨`2q“1rP1r`
P1pmq

ěc2
1p1 ´ rβqplog N q1 rχp¨q“´1rP1r`
P1 ˚ 1 rχp¨q“ rχp¨`2q“1rP1r`
P1pmq

` p1 ´ rβqplog N q rE2 ˚ rP1r`
P1pmq

with
 |p1 ´ rβqplog N q rE2 ˚ rP1r`
P1pmq| ! p1 ´ rβqplog N qe
´cδ´1{2
1 mSpmq,

outside of an acceptable exceptional set of natural numbers m. By the second case of
Proposition 6.5,

c2
1p1 ´ rβqplog N q1 rχp¨q“´1rP1r`
P1 ˚ 1 rχp¨q“ rχp¨`2q“1rP1r`
P1pmq

“c2
1p1 ´ rβqplog N qmSpmq
´ 1 ´ σ1pmq ´ σ2pmq
8 ` Opδ´3
1 plog N q
´1{3q
¯`1 ` Ope
´cδ´1
1 q
˘.

Since we can assume (8.8) and since |σ2pmq| ď 1, we have

1 ´ σ1pmq ´ σ2pmq
8 ` Opδ´3
1 plog N q
´1{3q ě 1{16 ` Opδ´3
1 plog N q´1{3q.

If δ1 is sufficiently small in absolute terms, together with (7.2) and the fact that Spmq " 1
for m ” 4 pmod 6q, this shows that

ΛΛ`
2 ˚ ΛΛ`
2 pmq ě 1
20p1 ´ rβqplog N qmSpmq " N 1´δ6
1

for all natural numbers m P r5N {4, 7N {4s, m ” 4 pmod 6q that fulfil (8.8), apart from
OpN 1´pδ1{10q4q exceptions. □

References

[1] J. R. Chen. On the representation of a larger even integer as the sum of a prime and the product of at
most two primes. Sci. Sinica, 16:157–176, 1973.
[2] J.-M. Deshouillers and H. Iwaniec. Kloosterman Sums and Fourier Coefficients of Cusp Forms. Invent.
Math., 70:219–219, 1982/83.
[3] S. Drappeau. Sums of Kloosterman sums in arithmetic progressions, and the error term in the dispersion
method. Proc. London Math. Soc., 114(4):684–732, 2017.
[4] J. Friedlander and H. Iwaniec. Opera de Cribro, volume 57 of American Mathematical Society Colloquium
Publications. American Mathematical Society, Providence, RI, 2010.
[5] P. X. Gallagher. A large sieve density estimate near σ “ 1. Invent. Math., 11(4):329–339, 1970.
[6] B. Green. Roth’s theorem in the primes. Ann. of Math., 161(3):1609–1636, 2005.
[7] B. Green. On S´ark¨ozy’s theorem for shifted primes. J. Amer. Math. Soc., 37(4):1121–1201, 2024.
[8] L. Grimmelt. Goldbach numbers in short intervals. Ann. Sc. Norm. Super. Pisa Cl. Sci. (5), 23(3):1395–
1416, 2022.
[9] L. Grimmelt and J. Ter¨av¨ainen. The Exceptional Set in Goldbach’s Problem with Almost Twin Primes.
arXiv e-prints, page arXiv:2207.08805, July 2022.
[10] G. Harman. Prime-Detecting Sieves, volume 33 of London Mathematical Society Monographs. Princeton
University Press, Princeton, NJ, November 2007.
[11] K. Henriot. Nair-Tenenbaum bounds uniform with respect to the discriminant. Math. Proc. Cambridge
Philos. Soc., 152(3):405–424, 2012. 70

[12] H. Iwaniec and E. Kowalski. Analytic number theory, volume 53 of American Mathematical Society
Colloquium Publications. American Mathematical Society, Providence, RI, 2004.
[13] J. Leng. Efficient Equidistribution of Nilsequences. arXiv e-prints, page arXiv:2312.10772, December
2023.
[14] K. Matom¨aki. A Bombieri-Vinogradov type exponential sum result with applications. J. Number Theory,
129(9):2214–2225, 2009.
[15] K. Matom¨aki. Almost primes in almost all very short intervals. J. Lond. Math. Soc. (2), 106(2):1061–
1097, 2022.
[16] K. Matom¨aki, M. Radziwi l l, X. Shao, T. Tao, and J. Ter¨av¨ainen. Higher uniformity of arithmetic
functions in short intervals II. Almost all intervals. arXiv e-prints, page arXiv:2411.05770, November
2024.
[17] K. Matom¨aki and X. Shao. Vinogradov’s three primes theorem with almost twin primes. Compos. Math.,
153(6):1220–1256, 2017.
[18] K. Matom¨aki, X. Shao, T. Tao, and J. Ter¨av¨ainen. Higher uniformity of arithmetic functions in short
intervals I. All intervals. Forum Math. Pi, 11:Paper No. e29, 97, 2023.
[19] K. Matom¨aki and J. Merikoski. Siegel zeros, twin primes, goldbach’s conjecture, and primes in short
intervals. International Mathematics Research Notices, 2023(23):20337–20384, 04 2023.
[20] X. M. Meng. The Goldbach problems with prime numbers of special type. Acta Math. Sinica (Chin.
Ser.), 50(2):255–260, 2007.
[21] H. L. Montgomery and R. C. Vaughan. The exceptional set in Goldbach’s problem. Acta Arith., 27:353–
370, 1975.
[22] H. L. Montgomery and R. C. Vaughan. Multiplicative number theory. I. Classical theory, volume 97 of
Cambridge Studies in Advanced Mathematics. Cambridge University Press, Cambridge, 2007.
[23] J. Pintz. A new explicit formula in the additive theory of primes with applications II. the exceptional
set in goldbach’s problem, 2018.
[24] D. H. J. Polymath. Variants of the Selberg sieve, and bounded intervals containing many primes. Res.
Math. Sci., 1:Art. 12, 83, 2014.
[25] A. Selberg. Sieve methods. In 1969 Number Theory Institute (Proc. Sympos. Pure Math., Vol. XX, State
Univ. New York, Stony Brook, N.Y., 1969), pages 311–351, 1971.
[26] T. Tao and J. Ter¨av¨ainen. Quantitative bounds for Gowers uniformity of the M¨obius and von Mangoldt
functions. J. Eur. Math. Soc. (JEMS), 27(4):1321–1384, 2025.
[27] J. Ter¨av¨ainen. The Goldbach problem for primes that are sums of two squares plus one. Mathematika,
64(1):20–70, 2018.
[28] D. I. Tolev. Additive problems with prime numbers of special type. Acta Arith., 96(1):53–88, 2000.

Department of Pure Mathematics and Mathematical Statistics, University of Cambridge,
Cambridge CB3 0WB, UK
Email address: lpg31@cam.ac.uk

Department of Pure Mathematics and Mathematical Statistics, University of Cambridge,
Cambridge CB3 0WB, UK
Email address: joni.p.teravainen@gmail.com
 71
