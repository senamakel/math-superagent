<!-- source: https://hal.science/hal-05012023v3/document | converted from PDF -->

HAL Id: hal-05012023

https://hal.science/hal-05012023v3

Submitted on 21 Jun 2025

HAL is a multi-disciplinary open access archive
for the deposit and dissemination of scientific re-
search documents, whether they are published or not.
The documents may come from teaching and research
institutions in France or abroad, or from public or pri-
vate research centers.
 L’archive ouverte pluridisciplinaire HAL, est des-
tinée au dépôt et à la diffusion de documents scien-
tifiques de niveau recherche, publiés ou non, émanant
des établissements d’enseignement et de recherche
français ou étrangers, des laboratoires publics ou
privés.

Distributed under a Creative Commons CC BY-ND 4.0 - Attribution - No Derivative Works - International
License

On the Link Between Stopping Time and Non-Trivial Cycles
in the Collatz Problem

Lionel Laurore

To cite this version:

Lionel Laurore. On the Link Between Stopping Time and Non-Trivial Cycles in the Collatz Problem. Advances
in Pure Mathematics, 2025, 15 (06), pp.351-389. ⟨10.4236/apm.2025.156018⟩. ⟨hal-05012023v3⟩

On the Link Between Stopping Time and Non-Trivial Cycles in
the Collatz Problem

Lionel Laurore

LuxCarta Technology, Department of Computer Science & Artificial Intelligence,
Sophia-Antipolis,France

lionel@luxcarta.com

March 28, 2025

Abstract

The Collatz Conjecture asserts that for all positive integers s, every Syracuse integer sequence defined by T (s) = s/2
if s is even, and T (s) = (3s + 1)/2 otherwise, eventually reaches 1 after a finite number of iterations. The stopping
time of an integer is the smallest number of iterations required for the sequence to fall below its starting value, while
the total stopping time measures the iterations needed to reach 1.

In this paper, we revisit the notion of stopping time by introducing the coefficient stopping time, defined as the
smallest value of n such that the coefficient of s in T n(s), expressed as 3r/2
n, is less than 1. Building on foundational
results by Lynn E. Garner (1981), we leverage recent computational results by David Barina to extend Garner’s
estimation regarding the minimal length of non-trivial cycles. Specifically, we demonstrate the non-existence of non-
trivial cycles of length n < 19, 478, 780, 533, thus improving upon the previous result by Shalom Eliahou (2021). We
subsequently show that this result can be generalized to all integers n. We also introduce new properties concerning
the behavior of Syracuse sequences modulo 2n, which play a central role in our approach.

Inspired by the work of Mike Winkler (2017), we provide an exact formulation of the stopping time counting function,
which calculates the number of integers s < 2
n whose stopping time σ(s) = n. From this formulation, we demonstrate
that the density of integers with stopping time greater than n tends to zero as n approaches infinity. Furthermore, if
divergent sequences exist, the set of such sequences is of zero density in N.

Our results offer a deeper understanding of how stopping time behavior relates to the elusive search for non-trivial
cycles in the Collatz problem.

Keywords: Collatz problem, stopping time, coefficient stopping time, non-trivial cycles, Garner’s main theorem

1

1 Preamble

The 3x+1 problem, introduced by the mathematician Lothar Collatz in 1937, is the study of integer sequences defined
by the arithmetic function C:
 C(s) =
 {
3s + 1 if s ≡ 1 (mod 2),
s
2 otherwise.

We define C∞(s) as the sequence of all iterates of s under the function C: C∞(s) = {C i(s) : i ∈ N}.

Lothar Collatz conjectured that for any starting number s, the integer sequence C∞(s) eventually reaches 1. Another
equivalent formulation of the conjecture states that for any starting number s, the integer sequence C∞(s) has an iterate
below s.

In the following, we will mainly use two alternative formulations of the arithmetic function C:

T (s) =
 { 3s+1
2 if s ≡ 1 (mod 2),
s
2 otherwise.

We define T∞(s) as the sequence of all iterates of s under the function T : T∞(s) = {T i(s) : i ∈ N}.

Additionally, we define:
 N (s) =
 { 3s+1
2α if s ≡ 1 (mod 2),
s
2α otherwise,

where α(s) is the largest integer such that 3s+1
2α or s
2α is odd. We define N∞(s) as the sequence of all iterates of s under
the function N : N∞(s) = {N i(s) : i ∈ N}.

We define the subsequences:

Cm(s) = {C i(s) : i < m}, Tn(s) = {T j(s) : j < n}, Nr(s) = {N k(s) : k < r}

which are linked for the odd terms of these sequences by the relationship:

C n+r(s) = T n(s) = N r(s).

For example:
C∞(7) = {7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1, 4, 2, 1, . . .} has 16 iterates to reach 1.
T∞(7) = {7, 11, 17, 26, 13, 20, 10, 5, 8, 4, 2, 1, 2, 1, . . .} has 11 iterates to reach 1.
N∞(7) = {7, 11, 17, 13, 5, 1, 1, . . .} has 5 iterates, containing only odd terms.
And C 11(7) = T 7(7) = N 4(7) = 5 and C 7(7) = T 4(7) = N 3(7) = 13.

Another important formulation that we will extensively use later is the following:
if n is the number of iterates of T and r is the number of odd iterates in Tn(s), the n-th iterate of T can be represented
by the Diophantine equation:
 T n(s) = 3r

2n · s + 1
2n
 r∑

i=1 3
r−i · 2n−(αi+...+α
′
r), (1)

where n = ∑r−1
i=1 αi + α′
r and 1 ≤ α′
r ≤ αr.
The coefficient of s in (1) is 3
r
2n . As long as this coefficient is greater than 1, T n(s) will remain greater than s.

We will also use the following equivalent formulation of (1):

T n(s) = 3r(n)

2n · s + cn(s)
2n , (2)

where
 cn(s) =
 r∑

i=1 3
r−i · 2n−(αi+...+α′
r)

and n = ∑r−1
i=1 αi + α′
r.
For example, T 2(5) = 3
22 · 5 + 1
22 , with n = 2 = α′
1 and α′
1 ̸= α1 = 4 as defined in the function N (s).

2

Definition 1.1 (Stopping Time). The Stopping Time σ(s) is the number of iterates required for the sequence to drop
below the starting value: σ(s) = Min{p ∈ N : T p(s) < s}.

Definition 1.2 (Coefficient Stopping Time). The Coefficient Stopping Time ω(s) is the first iterate where the coefficient
of s in (1) is less than 1:
 ω(s) = Min{p ∈ N : 3r(p)

2p < 1}.

Definition 1.3 (Non-Trivial Cycle). Under the Collatz conjecture, every Syracuse sequence is conjectured to eventually
reach the trivial cycle {2, 1} under repeated application of the function T . A non-trivial cycle is defined as a periodic
sequence of n integers, all strictly greater than 2, that remains invariant under the iteration of T .

The Collatz conjecture asserts that no such non-trivial cycles exist.

Definition 1.4 (Coefficient of s in the diophantine equation 2). The coefficient of s in the diophantine equation 2 is
the value 3
r(n)
2n and will be noted :
 Coef (T n(s)) = 3
r(n)

2n
.

2 Major steps of our work

In the first part of this document, we will build upon the work of Lynn E. Garner [1] to present the following series of
properties regarding stopping time:

• There exists an integer N = 19, 478, 780, 533 which is the largest stopping time resulting from Lynn E. Garner’s
approach, based on the fact that David Barina has verified that the Collatz Conjecture holds for all integers
s < 702 × 2
60 ≈ 2
69.455327. For all s < 2N and σ(s) ≤ N , the stopping time of s is equal to the coefficient stopping
time of s.

• Two Syracuse sequences with starting numbers s and s
′, positive integers in N, such that s ≡ s
′ (mod 2n), have
the same variations and sequences of coefficients of s in Equation (2) for all iterates up to the n-th iterate.

• The density in N of the set of positive integers with stopping time σ(s) = n is entirely determined by the number
of integers modulo 2n having a stopping time equal to n, as long as n ≤ 19, 478, 780, 533.

• Finally, we will show by strong induction that if, for all p < n and for all integers s < 2
p with stopping time
σ(s) = p, the stopping time is equal to the Coefficient stopping time σ(s) = ω(s), then this also holds for all
integers s < 2n with stopping time σ(s) = n. This approach allows us to extend Lynn E. Garner’s results to all
stopping time values.

In a second part, building on the work of Mike Winkler [2], we will develop the following results:

• An exact formulation of the counting function giving the number of integers s < 2n for which the Stopping Time
σ(s) = n, for every positive integer n such that all positive integers s < 2
n with stopping time σ(s) = n satisfy
the condition σ(s) = ω(s).

• We will show that the density function of the positive integers, starting numbers of Syracuse sequences, having a
stopping time higher than n, tends to 0 when n grows to infinity, as long as, for every positive integer n such that
all positive integers s < 2
n with stopping time σ(s) = n satisfy the condition σ(s) = ω(s).

• We will give the exact structure of the highest and lowest trajectory of Syracuse sequences before stopping time
iterate.

3 No Non-Trivial Cycle of length lower than 19,478,780,533

In 1981, Lynn E. Garner published a paper in which he highlighted that the behavior of a Collatz sequence is closely
related to the distribution of powers of 2 among the powers of 3. He stated that the powers of 2 appear to be bounded
away from the powers of 3 by a lower bound that grows almost as rapidly as the powers of 3. Garner demonstrated that
σ(s) = ω(s) = n for all n < 64, 300 and proved that no non-trivial cycles of length less than n = 64, 300 exist.
In this section, we adopt the approach developed by Lynn E. Garner to extend his result to show the non-existence of
non-trivial cycles for all stopping times n ≤ 19, 478, 780, 533. This will also serve as a crucial step in applying the strong
induction approach to extend the result to all stopping times.
Our notations differ slightly from those of Garner, as we use the function T introduced earlier, whereas Lynn E. Garner’s
proof relies on the function C.
 3

Lemma 3.1. For all positive integers n ≤ 19, 478, 780, 533 and all s < 2n, the stopping time σ(s) corresponds exactly
to the coefficient stopping time ω(s). This implies that for all s < 2
19,478,780,533 such that σ(s) ≤ 19, 478, 780, 533, the
stopping time σ(s) of a Syracuse sequence with starting number s corresponds to the coefficient stopping time, in other
words, to the first iterate of T such that the coefficient of s in (2) satisfies 3
r(n)
2n < 1.

Proof. Let M ∈ N and let :

b(M ) := max
r<M{− log3
 (1 − 2
n−1

3r
 )
} and B(M ) := max
r<M{− log3
 ( 2
n

3r − 1)
} (3)

which implies : for all r < M, 3r − 2
n−1 > 3r−b(M ) (4)

for all r < M, 2n − 3
r > 3
r−B(M ) (5)

The values of M at which b(M) and B(M) increase are given in the below table.

The Main Garner’s Theorem states:

For all s , if ω(s) = n and r < min {M, s
2 · 3
1−B(M )

1 − 3−b(M )
 } , then σ(s) = ω(s) (6)

This implies that if all Syracuse sequences have a number of odd iterates not too large, the stopping time is equal to
the coefficient stopping time. In other words, the stopping time is the first iterate for which the coefficient of s in (1) is
less than 1.

If the Coefficient Stopping Time ω(s) = n, then : 3
r

2n(r) < 1 and for i < r , 3
i

2n(i) > 1

And since n = α(1) + · · · + α(r), we have the following inequality: 3
r−i

2α(i)+···+α(r) · 3
i

2α(1)+···+α(i−1) < 1.

By inequality 4 for any i < r, we have the following upper bound:

3r−i

2α(i)+···+α(r) < 2
α(1)+···+α(i−1)

3i ≤ 2n(i−1)

3i < 1
3 · (1 − 3−b(M )).

Then:
 T n(s) = 3
r

2n · s + 1
2n
 r∑

i=1 3r−i · 2
n−(α(i)+···+α(r)) < 3
r

2n · s + r
3 · (1 − 3−b(M )).

If we suppose that σ(s) > ω(s), which implies T n(s) > s, we reach a contradiction:

s < T n(s) < 3
r

2n · s + r
3 · (1 − 3−b(M )) < 3
r

2n · s +
 s
2 · 3
1−B(M )

1−3−b(M )
3 · (1 − 3
−b(M )) < 3r

2n · s + s
2 · 3−B(M ).

Using inequality 5 and the fact that 2
n−1 < 3r < 2
n, we have 2n − 3
r > 3
r−B(M ) > 2
n−1 · 3
−B(M ), yielding:

s < 3r

2n · s + s
2 · 3
−B(M ) < ( 3
r

2n + 2
n−1 · 3−B(M )

2n
 ) · s < ( 3
r

2n + 3
r−B(M )

2n
 ) · s < s.

This proves the contradiction.

Thanks to the recent work of David Barina [3] (2021), who computationally verified the Collatz conjecture up to
702 · 2
60 ≃ 2
69.4553, significantly improving the previous record held by Thomas Oliveira e Silva [4], and due to the
increased computational power now available compared to Garner’s time, we have computed all values of b(M ) and
B(M ) for all M < 200,000,000,000. The results are presented in the table 1. We observe that the values of M and
n(M ) correspond to the numerators and denominators of the successive convergents in the continued fraction expansion
of log(2)/ log(3).

This allows us to estimate, based on the highest values of B(M ) and b(M ), the maximum M (i.e., the number of
odd iterates of T ) before the stopping time, in accordance with Garner’s Main Theorem. It is known that the Collatz
conjecture has been computationally verified for all integers s ≤ 702.260. We have computed the condition of Garner’s
Main Theorem for all M and identified the highest value of r, corresponding to the largest s for which the Collatz
conjecture holds. The highest value of r is obtained for M = 12,289,742,202.

4

r < min (
12, 776, 063, 961, 702 · 2
60

2 . 31−23,043797

1 − 3−21,100591
 ) = 12, 289, 742, 202

Thus σ(s) = ω(s) for all s < 2n such that n(r) < n(12, 289, 742, 202) = 19, 478, 780, 533

According to Lynn E. Garner’s conclusions, this implies that there is no non-trivial cycle of length less than N =
19, 478, 780, 533, and consequently that no integer s < 2n can be a solution of the Diophantine equation T n(s) = s.
This improves on the lower bound n > 17, 026, 679, 261 found by Shalom Eliahou [5] in 2021 for the length of non-trivial
cycles. However, we would likely obtain the same result using the approach developed by Shalom Eliahou if we utilized
the computational record obtained by David Barina instead of the one by Oliveira e Silva. The main advantage of
Garner’s approach is that it links the nonexistence of non-trivial cycles to the equality between the Stopping Time and
the Coefficient Stopping Time.

Mi n(Mi) n(Mi) − n(Mi−1) b(Mi) B(Mi) Mi n(Mi) n(Mi) − n(Mi−1) b(Mi) B(Mi)
1 2 0,821692 1,134066 4684090 7424108 190537 11,921111
2 4 1 1,946921 4874627 7726102 190537 11,950185
3 5 1 1,613445 5065164 8028096 190537 11,980218
5 8 2 2,689105 5255701 8330090 190537 12,011276
7 12 2 2,478725 5446238 8632084 190537 12,043431
12 20 5 3,915205 5636775 8934078 190537 12,076763
17 27 5 2,963203 5827312 9236072 190537 12,111363
29 46 12 3,357256 6017849 9538066 190537 12,147331
41 65 12 4,067531 6208386 9840060 190537 12,184778
53 85 12 5,617528 6398923 10142054 190537 12,223832
94 149 41 4,250575 6589460 10444048 190537 12,264637
147 233 53 4,479936 6779997 10746042 190537 12,307357
200 317 53 4,787298 6970534 11048036 190537 12,352182
253 401 53 5,254823 7161071 11350030 190537 12,399329
306 485 53 6,267689 7351608 11652024 190537 12,449052
359 570 53 6,229625 7542145 11954018 190537 12,501649
665 1055 306 9,138086 7732682 12256012 190537 12,557472
971 1539 306 6,307414 7923219 12558006 190537 12,616944
1636 2593 665 6,348953 8113756 12860000 190537 12,680575
2301 3647 665 6,392479 8304293 13161994 190537 12,748991
2966 4701 665 6,438190 8494830 13463988 190537 12,822970
3631 5755 665 6,486320 8685367 13765982 190537 12,903498
4296 6809 665 6,537136 8875904 14067976 190537 12,991848
4961 7863 665 6,590959 9066441 14369970 190537 13,089704
5626 8917 665 6,648165 9256978 14671964 190537 13,199362
6291 9971 665 6,709209 9447515 14973958 190537 13,324063
6956 11025 665 6,774643 9638052 15275952 190537 13,468602
7621 12079 665 6,845148 9828589 15577946 190537 13,640506
8286 13133 665 6,921576 10019126 15879940 190537 13,852616
8951 14187 665 7,005014 10209663 16181934 190537 14,129668
9616 15241 665 7,096879 10400200 16483928 190537 14,529907
10281 16295 665 7,199068 10590737 16785922 190537 15,261307
10946 17349 665 7,314197 10781274 17087915 190537 16,585704
11611 18403 665 7,446026 21372011 33873837 10590737 15,503241
12276 19457 665 7,600233 32153285 50961752 10781274 15,833722
12941 20511 665 7,786004 42934559 68049667 10781274 16,357825
13606 21565 665 8,019673 53715833 85137582 10781274 17,729972
14271 22619 665 8,334854 64497107 102225496 10781274 16,890397
14936 23673 665 8,820964 118212940 187363077 53715833 17,351701
15601 24727 665 9,934703 171928773 272500658 53715833 18,333573
16266 25782 665 9,628894 225644606 357638240 53715833 18,389077
31867 50509 15601 10,770361 397573379 630138897 171928773 20,907339
47468 75235 15601 10,398601 623217985 987777137 225644606 18,448188
79335 125743 31867 11,393245 1020791364 1617916034 397573379 18,511405
111202 176252 31867 11,409410 1418364743 2248054931 397573379 18,579343
190537 301994 79335 15,070361 1815938122 2878193828 397573379 18,652763
301739 478246 111202 11,425867 2213511501 3508332725 397573379 18,732630
492276 780240 190537 11,442627 2611084880 4138471622 397573379 18,820183
682813 1082234 190537 11,459702 3008658259 4768610519 397573379 18,917064
873350 1384228 190537 11,477103 3406231638 5398749416 397573379 19,025498
1063887 1686222 190537 11,494843 3803805017 6028888313 397573379 19,148618
1254424 1988216 190537 11,512936 4201378396 6659027210 397573379 19,291036
1444961 2290210 190537 11,531396 4598951775 7289166107 397573379 19,459946
1635498 2592204 190537 11,550238 4996525154 7919305004 397573379 19,667508
1826035 2894198 190537 11,569478 5394098533 8549443901 397573379 19,936831
2016572 3196192 190537 11,589134 5791671912 9179582798 397573379 20,321013
2207109 3498186 190537 11,609224 6189245291 9809721695 397573379 20,998846
2397646 3800180 190537 11,629767 6586818670 10439860591 397573379 23,043797
2588183 4102174 190537 11,650784 12776063961 20249582286 6189245291 21,100591
2778720 4404168 190537 11,672298 19362882631 30689442877 6586818670 21,215156
2969257 4706162 190537 11,694333 25949701301 41129303468 6586818670 21,346246
3159794 5008156 190537 11,716915 32536519971 51569164059 6586818670 21,499444
3350331 5310150 190537 11,740071 39123338641 62009024650 6586818670 21,683750
3540868 5612144 190537 11,763832 45710157311 72448885241 6586818670 21,915100
3731405 5914138 190537 11,788230 52296975981 82888745832 6586818670 22,226059
3921942 6216132 190537 11,813299 58883794651 93328606423 6586818670 22,702068
4112479 6518126 190537 11,839079 65470613321 103768467014 6586818670 23,759345
4303016 6820120 190537 11,865610 72057431991 114208327605 65470613321 23,597310
4493553 7122114 190537 11,892938 137528045312 217976794617 65470613321 25,248104

Table 1: Highest values of b(M ) and B(M )

4 Remarkable properties of the Stopping Times

Before presenting, in Section 4, our approach to build the stopping time counting function, we are going to state some
preliminary definitions and lemmes useful for the following parts of this work.

5

Definition 4.1 (Stopping time Histogram on Z/2
nZ ). For every positive integer n,

Hn = {hn(p), p ∈ N}

where hn(p) = card{s < 2n, σ(s) = p} is the number of residue classes mod 2
n of Syracuse sequences of starting number
s such that σ(s) = p

By convention, we will write hn(∞) the number of Syracuse sequences of the starting number s that has no finite
stopping time. It concerns the Syracuse sequences, which eventually tend to infinity or reach a non-trivial cycle.

Definition 4.2 (Counting Function of Stopping Time lower or equal to n in Z/2
nZ ). For every positive integer n,

π(2n) = card{s < 2n, σ(s) ≤ n}

is the number of residue classes mod 2n of Syracuse sequences of starting number s such that σ(s) ≤ n.

Definition 4.3 (Counting Function of Stopping Time higher than n in Z/2
nZ ). For every positive integer n,

S(n) = card{s < 2
n, σ(s) > n}

is the number of residue classes mod 2n of Syracuse sequences of starting number s such that σ(s) > n

By definition, we have the following equalities :

π(2n) :=
 n∑

r=0 hn(p), S(n) :=
 ∞∑

n+1 hn(p), 2n :=
 ∞∑

p=0 hn(p), 2n := π(2n) + S(n)

We shall see in lemme (4.5), that hn(p) = 0 for all p which don’t satisfy to the relation p(r) = ⌊r.log2(3) + 1⌋ for r ∈ N.

Lemma 4.1. For all s ∈ 2N + 1, for all n and m ∈ N + 1, and for all p ≤ n, we have:

T p(2n · m + s) = 3
rp

2p · 2
n · m + T p(s) and cp(2
n · m + s) = cp(s) and rp(2
n · m + s) = rp(s) = rp. (7)

Proof. The goal of this lemma is to show that for all iterates p ≤ n of the function T , the expressions T p(2n · m + s),
3r(p)
2p , and T p(s) have the same variations up to the n-th iteration of T . Using equation (2), we know:

T p(s) = 3
rp

2p · s + cp(s)
2p ,

and T p+1(s) can be expressed in one of the following forms:
**Case 1:** If T p(s) is even, then:
 T p+1(s) = T p(s)
2 = 3rp

2p+1 · s + cp(s)
2p+1 ,

which implies that cp+1(s) = cp(s) and rp+1 = rp.
**Case 2:** If T p(s) is odd, then:
 T p+1(s) = 3T p(s) + 1
2 = 3rp+1

2p+1 · s + 3cp(s) + 2p

2p+1 ,

which implies that cp+1(s) = 3cp(s) + 2p and rp+1 = rp + 1.
We will now prove by induction that:

T p(2n · m + s) = 3
rp

2p · 2n · m + T p(s) and cp(2n · m + s) = cp(s) and rp(2
n · m + s) = rp(s) = rp.

**Base Case:** For p = 1, since s is odd:

T (2n · m + s) = 3(2
n · m + s) + 1
2 = 3
2 · (2n · m + s) + 1
2 = 3
2 · 2
n · m + 3s + 1
2 = 3
2 · 2n · m + T (s),

with c1(2n · m + s) = 1 = c1(s) and r1(2n · m + s) = r1(s) = 1
**Inductive Step:** Assume that for some p < n:

T p(2n · m + s) = 3rp

2p · 2n · m + T p(s) and cp(2n · m + s) = cp(s) and rp(2
n · m + s) = rp(s) = rp.

6

**Case 1:** If T p(2n · m + s) is even, then T p(s) is necessarily even because n > p, so:

T p+1(2n · m + s) = T p(2
n · m + s)
2 = 3
rp

2p+1 · (2n · m + s) + cp(2
n · m + s)
2p+1 ,

As by hypothesis cp(2
n · m + s) = cp(s), we can simplifies:

T p+1(2n · m + s) = 3rp

2p+1 · 2n · m + T p+1(s)

and we have
 cp+1(2n · m + s) = cp(2n · m + s) = cp(s) = cp+1(s) and rp+1(2n · m + s) = rp+1(s) = rp

**Case 2:** If T p(2
n · m + s) is odd, then T p(s) is necessarily odd, so:

T p+1(2n · m + s) = 3T p(2n · m + s) + 1
2 = 3r(p)+1

2p+1 · (2n · m + s) + 3cp(2
n · m + s) + 2p

2p+1 ,

which simplifies to:
 T p+1(2n · m + s) = 3r(p)+1

2p+1 · 2
n · m + T p+1(s),

and we have:

cp+1(2n · m + s) = 3cp(2n · m + s) + 2p = 3cp(s) + 2p = cp+1(s) and rp+1(2n · m + s) = rp+1(s) = rp + 1

This completes the proof.
Note: This property is very important because it shows that the variations of the two Syracuse sequences of starting
numberd s and 2
n · m + s are identical for the first n− iterations, and the sequences corresponding to the coefficients of s
and 2n ·m+s in (1) are also identical. In his work entitled "Empirical Verification of the 3x+1 and Related Conjectures",
published in the book The Ultimate Challenge: The 3x+1 Problem edited by Jeffrey C. Lagarias [6], Thomas Oliveira
e Silva [4] observed that the two sequences starting from 15 and 143 exhibit the same behavior up to the stopping time
iterate. We have now proven the reason why this observation holds.

Corollary 4.2. For all odd integers s ∈ N, and for all n, m ∈ N+ such that ω(s) = n, we have:

ω(s) = ω(2n · m + s).

Proof. Lemma 4.1 shows that the iterates of T starting from s and 2
n · m + s follow the same sequence of parities up to
step n. In particular, for all p ≤ n, the coefficient of s in the associated expression (2) is the same:

Coefs(T p(s)) = Coefs(T p(2
n · m + s)) = 3
r(p)

2p .

Now, if n is the smallest index for which 3
r(n)
2n < 1, then by definition ω(s) = n, and we also obtain ω(2n · m + s) = n,
completing the proof.

Lemma 4.3. For all odd integers s < 2
n such that σ(s) = ω(s) = n, all integers s
′ = 2
n · m + s, with m ∈ N + 1 also
have a finite stopping time σ(s
′) = n.

Proof. The proof follows directly from the previous corollary. Indeed, we have shown that if ω(s) = n, then for any
m ∈ N+, we have: ω(2n · m + s) = ω(s) = n.

Therefore, if ω(s) = σ(s), the same equality holds for 2n · m + s, and we may conclude that s and 2
n · m + s have the
same stopping time: σ(2n · m + s) = σ(s).

An immediate and noteworthy consequence of this result is that, for all n < N , hn(n + 1) = 2 · hn(n). More generally, for
all p > n, hp(n) = 2
p−n · hn(n). This result implies that all integers in N with a stopping time equal to n are completely
determined by the positive integers less than 2
n that have a stopping time equal to n, for all n satisfying Garner’s main
theorem.
 7

Lemma 4.4. If there exist positive integers s > 4 and n > 19, 478, 780, 533 such that T n(s) = s and T k(s) > s for all
0 < k < n, meaning that the starting number s in the Syracuse sequence is the smallest term of a non-trivial cycle of
length n, then s is the only integer in the residue class modulo 2n that satisfies T n(s) = s. Furthermore, all integers of
the form 2
n · m + s with m > 0 have a finite stopping time σ(2
n · m + s) ≤ n.

Proof. According to lemme 3.1, No Non-trivial cycle may exist for n > 19, 478, 780, 533. From equation (2), the n-th
iterate of s can be expressed as::
 T n(s) = 3r

2n · s + cn(s)
2n .

If s and n satisfy T n(s) = s and T k(s) > s for 0 < k < n, it follows that:

s = 3r

2n · s + cn(s)
2n =⇒ s − 3r

2n · s = cn(s)
2n > 0 which implies 3
r < 2n and ω(s) = n (8)

By Lemma 4.1, for all integers m > 0:

T n(2n · m + s) = 3
r

2n · (2n · m + s) + cn(2
n · m + s)
2n = 3
r

2n · (2n · m + s) + cn(s)
2n .

Simplifying, we get:
 T n(2n · m + s) = 3
r · m + 3
r

2n · s + cn(s)
2n = 3
r · m + T n(s) < 2
n · m + s.

Thus, σ(s) = ∞, and for all m > 0, σ(2n · m + s) = ω(2
n · m + s) = ω(s) = n.

We can conclude that if s is the starting number of a Syracuse sequence and belongs to a non-trivial cycle of length n,
then for all positive integers m > 0 and n > 0, 2n · m + s has a finite stopping time. This implies that s is the only
positive integer in the residue class modulo 2
n belonging to a non-trivial cycle. All other integers s
′ ≡ s mod 2n in this
residue class have a finite stopping time that is equal to or less than n.

Lemma 4.5. A positive integer n ≤ 19, 478, 780, 533 is a stopping time value if and only if n(r) = ⌊r log2 3 + 1⌋, where
r ∈ N.

Proof. According to the relation for the n-th iterate of a Syracuse sequence with starting number s, as expressed in (1):

T n(s) = 3
rn

2n s + cn(s)
2n , with rn = ⌊ n
log2 3
 ⌋ .

As shown in the previous section, for all n = 19, 478, 780, 533, the stopping time is equal to the coefficient stopping time.
If σ(s) = n, the coefficient of s in (1), 3
rn
2n , is less than 1.
If n is such that: 2n−1 < 3
rn < 2
n < 2n+1 < 3rn+1,

and we assume that the first iterate with a coefficient of s less than 1 is n + 1, then 3
rn+1
2n+1 < 1, and for all p < n + 1, we
have 3
rp
2p > 1.
We distinguish two cases:

• If the previous iterate was odd, then rn = rn+1 − 1, and 3rn
2n < 3
rn+1
2n+1 < 1.

• If the previous iterate was even, then rn = rn+1, and 3
rn
2n < 1, since by our hypothesis 3
rn < 2n < 2
n+1.

This contradicts the hypothesis σ(s) = n + 1.

Thus, we have justified why certain integer values cannot correspond to stopping times. Now, we can express the
arithmetic function that generates all stopping time values:

2
n−1 < 3r < 2
n ⇔ (n − 1) ln 2 < r ln 3 < n ln 2 ⇔ n = ⌊r log2 3 + 1⌋

We can also deduce that if n is a stopping time value, the number of odd iterates r satisfies r = ⌊ n
log2 3 ⌋
.

8

Lemma 4.6. The density function π(2n)
2n is an increasing function of n and satisfies for all n ≤ 19, 478, 780, 533:

r(n)∑

r=0
 zp(r)
2p(r) = π(2
n)
2n < 1,

where zp(r) = hp(r)(p(r)). Moreover, the density function S(n)
2n is a decreasing function and satisfies:

0 < S(n)
2n = 1 −
 r(n)∑

r=0
 zp(r)
2p(r) < 1.

Proof. We can express ∑∞
r=0 hn(p(r)) since this power series has at most 2
n strictly positive terms.
By Lemma (4.3), we have established that for all p < n:

hn(p) ≥ 2
n−php(p),

which implies:
 2
n ≥ π(2n) =
 r(n)∑

r=0 hn(p(r)) =
 r(n)∑

r=0 2n−php(p) > 0 ⇔ 1 > π(2
n)
2n =
 r(n)∑

r=0
 zp(r)
2p(r) > 0. (9)

This equation means that π(2n) is fully determined by the numbers hp(p) of integers s modulo [2p] such that σ(s) = p
for all p ≤ n
Additionally, we have:
 0 < S(n) = 2
n − π(2n) = 2
n −
 r(n)∑

r=0
 zp(r)
2p(r)

which leads to:
 0 < S(n)
2n = 1 −
 r(n)∑

r=0
 zp(r)
2p(r) . (10)

Therefore, π(2n)
2n is an increasing function bounded by 1, and S(n)
2n is a decreasing function bounded by 0.
In the next section, we are going to build an exact formulation of zn for all n ≤ 19, 478, 780, 533.

Definition 4.4. Let P (N ) be the property:

P (N ) : For all integers n ≤ N and all s < 2
n such that σ(s) = n, we have σ(s) = ω(s).

Remark. This property is true for all N ≤ 19, 478, 780, 533 thanks to our results in section 3.

Theorem 4.7. The property P (N ) holds for all N ∈ N+.

Proof. Although Section 3 establishes that the equality σ(s) = ω(s) holds for all s < 2
n with n ≤ 19,478,780,533, our
goal here is to show that this is not a strict upper bound. We first explicitly verify the case n = 19,478,780,534, then
generalize the result to all n using strong induction.

We proceed by contradiction. Assume that there exists a positive integer s < 2
N +1 such that σ(s) = N + 1 and
ω(s) = n < N + 1.

If s < 2
n, then by assumption — valid for all n ≤ N = 19,478,780,533 — we must have σ(s) = ω(s) = n, which
contradicts the assumption σ(s) = N + 1.

If s > 2
n, there exists an integer m such that:

s = 2
n · m + s
′, with s
′ < 2
n.

According to Lemma (4.1) and Corollary 4.2, we have shown that the two Syracuse sequences with starting numbers s
′

and s = 2
n · m + s
′ exhibit the same variations and follow the same sequence of coefficients in (2). This implies that:

ω(s
′) = ω(s) = n.

9

By assumption, since s
′ < 2
n and σ(s
′) = ω(s
′) = n, and by applying Lemma (4.3), it follows that:

σ(2n · m + s
′) = σ(s
′) = n.

This leads to a contradiction. Therefore, property σ(s) = ω(s) also holds for n = N + 1. We therefore have extended
the validity of the condition to all n ≤ 19,478,780,534. This reasoning can be iterated indefinitely for all subsequent
values of N , which corresponds to applying a strong (or total) induction argument, as presented below.

To begin the proof with strong induction, we know that the condition is true for small values of N , due to the result of
Section 3. And we will assume that it is true for all n ≤ N , in other terms, for all n ≤ N and for all integers s < 2n

such that σ(s) = n, σ(s) = ω(s). We will prove that it is true for n=N+1.
We proceed by contradiction. Assume that there exists a positive integer s < 2
N +1 such that σ(s) = N + 1 and
ω(s) = n < N + 1.

If s < 2n, then by assumption — valid for all n ≤ N — we must have σ(s) = ω(s) = n, which contradicts the assumption
σ(s) = N + 1.

If s > 2
n, there exists an integer m such that:

s = 2
n · m + s
′, with s
′ < 2
n.

According to Lemma (4.1) and Corollary 4.2, we have shown that the two Syracuse sequences with starting numbers s
′

and s = 2
n · m + s
′ exhibit the same variations and follow the same sequence of coefficients in (2). This implies that:

ω(s
′) = ω(s) = n.

By assumption, since s
′ < 2n and σ(s
′) = ω(s
′) = n, and by applying Lemma (4.3), it follows that:

σ(2
n · m + s
′) = σ(s
′) = n.

This leads to a contradiction. Finally, property σ(s) = ω(s) = N also holds for all integers s ∈ N+.
We have finally proven that the stopping time is equal to the stopping time coefficient for all positive integers.

We now establish a key logical consequence of the equality between stopping time and coefficient stopping time, showing
that it implies the non-existence of non-trivial cycles.

Theorem 4.8. If, for all positive integers s, the Stopping Time is equal to the Coefficient Stopping Time, σ(s) = ω(s)
, then No Non-Trivial Cycles exist.

Proof. We now revisit the reasoning of Lynn E. Garner in his foundational 1981 work. He shows that if a non-trivial
cycle of length N exists, then it is necessarily the case that there exists at least one element in the cycle for which the
stopping time cannot be equal to the coefficient stopping time.

Indeed, let us consider the integer s representing the minimum value in the cycle. Since the cycle has length N , we have
T N (s) = s, which implies ω(s) = N .

If σ(s) exists, it must by definition satisfy σ(s) > ω(s), since the sequence returns to s only after N steps, without
reaching 1 in fewer steps. This contradicts the assumption that s is the smallest element in the cycle.

Therefore, as long as σ(s) = ω(s), no non-trivial cycles can exist.

From the previous theorem, in which we proved that σ(s) = ω(s) for all s ∈ N+, we can thus conclude that no non-trivial
cycles exist in the Collatz dynamics.

Remark. Since the equality σ(s) = ω(s) has now been proven for all s ∈ N+, all previously established lemmas (e.g.,
Lemma 4.5, Lemma 4.6) are no longer restricted to n < 19,478,780,533, but hold for all values of n ∈ N.

10

5 The Stopping Time counting function

5.1 Theoritical approach

Definition 5.1. The Stopping Time Counting Function is an arithmetic function that, for every integer n, gives the
number of residue classes modulo 2
n of the starting numbers of Syracuse sequences with a stopping time equal to n:

z(n) = {s < 2
n | σ(s) = n}

In the following, we shall use the notation zn.

Mike Winkler [2] (2017) was the first mathematician to describe the stopping Time Counting Function. He stated
that the number zr of residue classes modulo 2
σr for starting numbers s with a finite stopping time σ(s) = σr, where
σr = ⌊r log2 3 + 1⌋, satisfies the following equation:

zr = (m + r − 2)!
m! · (r − 2)! −
 r−1∑

i=2
 (⌊ 3(r−i)+δ
2 ⌋
r − i
 ) · zi, with m = ⌊(r − 1) log2 3 − (r − 1)⌋, (11)

where δ can take different values modulo 3. However, Mike Winkler notes that estimating this value is complex and his
work provides a computational code limited to the first 50 values of zr.

In this section, we propose an exact formulation of the stopping-time counting function by slightly modifying the
approach suggested by Mike Winkler. Before presenting our formulation of this counting function, we introduce a set
of useful properties of the Syracuse sequences.

In our work, instead of using zr, we use zn(r) = hn(r)(n(r)), where n(r) = ⌊r log2 3 + 1⌋. This represents the number
of modulo residue classes 2n(r) for the starting numbers s such that σ(s) = n. In this section, we propose a new
formulation of the Winkler formula that is independent of the parameter δ, allowing us to compute the exact values of
zr for any r. In Winkler’s original formula, r denotes the number of odd integers in the Syracuse integer sequence up to
σr iterations. We introduce a new definition: zn, the number of modulo residue classes 2
n for Syracuse sequences with
starting numbers s such that σ(s) = n. This new definition enables us to reformulate zn as follows.

But before presenting our formulation of the stopping Time Counting Function, we need to introduce a preliminary
concept that is highly useful for understanding this formulation, the notion of sequence of transition of the coefficients,
associated with a Syracuse sequence.

Definition 5.2. A transition sequence, associated with a Syracuse sequence starting from a positive integer s, is a
sequence consisting of the multiplicative coefficients of s at each iteration: 3
2 if the previous term is odd and 1
2 otherwise.
More formally, if Tn(s) = {T k(s) | k ≤ n} = {s, T (s), . . . , T n(s)} is a finite Syracuse subsequence, the associated
transition subsequence is defined as

T rn(s) = {t1, . . . , tn} where ti = 3
2 if T i−1(s) is odd, and ti = 1
2 if T i−1(s) else

Lemma 5.1. Given a Syracuse subsequence Tn(s) = {T k(s) | k ≤ n} = {s, T (s), . . . , T n(s)} and its associated transition
sequence T rn(s) = {t1, . . . , tn}, we can express cn(s) = ∑r
i=1 3r−i2
n−(αi+···+α
′
r(n)), presented in the diophantine equation
(2), in terms of ti as follows:
 cn(s) = 2n

3
 r∑

i=1
 n∏

j=i
tj = 3
2
 tj.

Proof. The proof is carried out by induction. Since we systematically start with an odd number—because if the first
term of the sequence is even, we begin with a division by 2—then

c1(s) = 2
1

3
 r=1∑

i=1
 1∏

j=i
tj = 3
2
 tj = 1.

11

Now, suppose that the expression
 cn(s) = 2
n

3
 r∑

i=1
 n∏

j=i
tj = 3
2
 tj

holds for n, and let us show that it also holds for n + 1.

We have two cases to consider:
The first case occurs when the transition sequence with n + 1 elements is obtained by adding the term tn+1 = 1
2 to
T rn(s) = {t1, . . . , tn}. In this case, we have

cn+1(s) = cn(s) = 2
n

3
 r∑

i=1
 n∏

j=i
tj = 3
2
 tj = 2
n+1

3
 r∑

i=1
 1
2 ·
 n∏

j=i
tj = 3
2
 tj.

As tn+1 = 1
2 , then
 cn+1(s) = 2
n+1

3
 r∑

i=1 tn+1 ·
 n∏

j=i
tj = 3
2
 tj = 2n+1

3
 r∑

i=1
 n+1∏

j=i
tj = 3
2
 tj

The second case occurs when the transition sequence with n + 1 elements is obtained by adding the term tn+1 = 3
2 to
T rn(s) = {t1, . . . , tn}. In this case, we have

cn+1(s) = 3 · cn(s) + 2n = 3 · 2
n

3
 r∑

i=1
 n∏

j=i
tj = 3
2
 tj + 2n = 2n+1

3 · (
 r∑

i=1
 3
2 ·
 n∏

j=i
tj = 3
2
 tj + 3
2 ).

As tn+1 = 3
2 , then
 cn+1(s) == 2
n+1

3 · (
 r∑

i=1 tn+1 ·
 n∏

j=i
tj = 3
2
 tj + tn+1) = 2
n+1

3
 r+1∑

i=1
 n+1∏

j=i
tj = 3
2
 tj

In conclusion, we can say that cn(s) is fully defined by the terms ti of the transition sequence.

Lemma 5.2. Given three positive integers n, r, c, the Diophantine equation

2ny − 3rs = c

admits a unique solution for (y, s) such that y < 3
r and s < 2
n.

Proof. By Bachet-Bézout’s theorem, since 2
n and 3
r are co-prime, the equation

2
ny′ − 3rs
′ = 1

admits infinitely many integer solutions. Among these, there exists a unique pair (y′, s
′) such that:

0 ≤ y′ < 3
r and 0 ≤ s
′ < 2n.

Now, consider the original equation: 2
ny − 3
rs = c.

Multiplying the solution (y′, s
′) by c, we obtain a particular solution:

y = cy′, s = cs
′.

Since this may not satisfy the desired bounds, we introduce an integer k such that:

y = cy′ − k3r, s = cs
′ − k2
n.

The appropriate choice of k is given by:
 k = ⌊ cy′

3r
 ⌋ .

This ensures: 0 ≤ y < 3
r and 0 ≤ s < 2n.

Since the construction of y and s depends uniquely on c, n, and r, this solution is unique.

12

Consider the case σ(s) = 8, we use the same approach instead of checking all odd integers less than 2
8. The solution
(s
′, y′) of the reduced Diophantine equation 2
8y′ − 35s
′ = 1, using the Bachet-Bézout algorithm, is (187, 197). The
transition sequences T r8(s) satisfying (14) and their corresponding c values are:

T r8(s1) = { 3
2 , 3
2 , 3
2 , 1
2 , 3
2 , 3
2 , 1
2 , 1
2 } , c = 251,
T r8(s2) = { 3
2 , 3
2 , 3
2 , 3
2 , 1
2 , 1
2 , 3
2 , 1
2 } , c = 259,
T r8(s3) = { 3
2 , 3
2 , 3
2 , 3
2 , 3
2 , 1
2 , 1
2 , 1
2 } , c = 211 (highest trajectory before stopping time),
T r8(s4) = { 3
2 , 3
2 , 1
2 , 3
2 , 3
2 , 1
2 , 3
2 , 1
2 } , c = 319 (lowest trajectory before stopping time),
T r8(s5) = { 3
2 , 3
2 , 3
2 , 3
2 , 1
2 , 3
2 , 1
2 , 1
2 } , c = 227,
T r8(s6) = { 3
2 , 3
2 , 3
2 , 1
2 , 3
2 , 1
2 , 3
2 , 1
2 } , c = 283,
T r8(s7) = { 3
2 , 3
2 , 1
2 , 3
2 , 3
2 , 3
2 , 1
2 , 1
2 } , c = 287.

The corresponding solutions are:
For c = 251: s1 = 2
8 ( cs
′
1
28 − ⌊ cy′
1
35 ⌋) = 39, y1 = 38.

For c = 259: s2 = 2
8 ( cs
′
2
28 − ⌊ cy′
2
35 ⌋) = 79, y2 = 76.

For c = 211: s3 = 2
8 ( cs
′
3
28 − ⌊ cy′
3
35 ⌋) = 95, y3 = 91.

For c = 319: s4 = 2
8 ( cs
′
4
28 − ⌊ cy′
4
35 ⌋) = 123, y4 = 118.

For c = 227: s5 = 2
8 ( cs
′
5
28 − ⌊ cy′
5
35 ⌋) = 175, y5 = 167.

For c = 283: s6 = 2
8 ( cs
′
6
28 − ⌊ cy′
6
35 ⌋) = 199, y6 = 190.

For c = 287: s7 = 2
8 ( cs
′
7
28 − ⌊ cy′
7
35 ⌋) = 219, y7 = 209.

Thus, we obtain the set of 7 integers modulo 2
8 with stopping time σ(s) = 8: {39, 79, 95, 123, 175, 199, 219}. We have
efficiently determined these values without checking all 2
8 integers, which is even more beneficial for larger n.

Another example: Consider n = 16 and the transition sequence T r16(s) = { 3
2 , 3
2 , 1
2 , 3
2 , 3
2 , 1
2 , 3
2 , 3
2 , 1
2 , 3
2 , 3
2 , 1
2 , 3
2 , 3
2 , 1
2 , 1
2 },
which satisfies (14) for n = 16:
Using the Bachet-Bézout algorithm, we solve 216y′′ − 3
10s
′′ = 1 and find (y′, s
′′) = (52222, 57959). We then solve
2
16y′ − 310s
′ = c, where
 c = 2
16

3
 8∑

i=1
 16∏

j=i if tj = 3
2
 tj = 131405.

The final values are:
 y = cy′ − ⌊ cy′

310
 ⌋ 310 = 29522, and s = cs
′ − ⌊ cy′

310
 ⌋ 216 = 32763.

We can check that s = 32763 yields T 16(s) = 29522, confirming that σ(s) = 16.

Lemma 5.3. There exists a bijection between the set of Syracuse subsequences of length n, Tn(s), and the set of
transition sequences T rn(s).

Proof. Given a positive integer s, consider the subsequence generated by s consisting of the first n iterates, denoted by
Tn(s). By construction, there exists a unique transition sequence T rn(s) which records the sequence of coefficients ti
corresponding to the parity of each iterate.
Conversely, suppose we are given a transition sequence consisting of r terms ti = 3
2 and n − r terms tj = 1
2 . The value
c associated to this transition sequence is given by:

c = 2n

3
 r∑

i=1
 n∏

j=i
tj = 3
2
 tj.

According to Lemma 5.2, there exists a unique integer s < 2n satisfying the Diophantine equation:

2
ny − 3
rs = c.

This s uniquely generates a subsequence Tn(s) whose associated transition sequence is exactly the given one.
Therefore, the mapping is bijective.
 13

Theorem 5.4. For every positive integer n such that all positive integers s < 2
n with stopping time σ(s) = n satisfy
the condition σ(s) = ω(s), then the number of residue classes modulo 2
n of integers s such that σ(s) = n is given by
the following expression:
 zn = hn(n) = ( n
r(n)

) −
 n−1∑

i=1
 ( n − i
r − r(i)

) · zi (12)

with z1 = 1, and n(i) = ⌊i · log2(3) + 1⌋, for i ∈ N.

Proof. The main idea developed in this proof is to find the easiest way to count the number of positive integers s < 2
n,
starting number of suracuse sequences, which have a stopping time σ(s) = n.

Our proof of (5.4) relies on understanding the link between Syracuse sub-sequences Tn(s) and their corresponding
transition sequences T rn(s). We have shown that there is a one-to-one correspondence between the set of sub-sequences
Tn(s) and the set of transition sequences T rn(s). Afterward, we will demonstrate that it is easier to count the transition
sequences corresponding to Syracuse sequences of starting number s, such that σ(s) = n.

For any integer s, the corresponding sequence of transitions T rn(s) is associated by construction with a Syracuse sub-
sequence Tn(s). The reverse is also true, which we will prove in the following. Our transition sequences are similar to
parity vectors used in various studies of the Collatz problem.

Given a transition sequence T rn(.), and thanks to the results of Lemmas 5.1, 5.2, and 5.3, we know that there is a
unique solution to the following Diophantine equation:

2
ny − 3
rs = c, where c = cn(s) =
 r∑

i=1 3r−i2
n−(αi+···+α
′
r(n)) = 2
n

3
 r∑

i=1
 n∏

j=i
tj = 3
2
 tj. (13)

This implies that for each integer s, the starting number of a Syracuse sequence, there exists one and only one transition
sequence, and conversely.

Now, we focus on the transition sequences T rn(s) for integers s with σ(s) = n. As we specified that we will consider
the values of n such that σ(s) = ω(s) = n, it implies that We have to study and count all sequences of transitions
T rn(s) = {t1, . . . , tn} satisfying:

n∏

j=1 tj < 1 and for all k < n,
 k∏

j=1 tj > 1, with tj ∈ { 1
2 , 3
2
 } . (14)

If σ(s) = n, by definition: T n(s) = 3
r
2n s + cn(s) < s < T k(s) = 3
r(k)

2k s + ck(s) for k < n. Thanks to the main theorem
by Lynn E. Garner [1] and Lemma 2.3, for all σ(s) = n < 19, 478, 780, 533, the stopping time n corresponds to the first
iterate where 3r(n)
2n < 1, which has been extended to any integer n through Theorem 4.7. This implies:

n∏

j=1 tj = 3r(n)

2n < 1 and for all k < n,
 k∏

j=1 tj = 3
r(k)

2k > 1.

Thus, for each transition sequence T rn(s) that satisfies these conditions, there is a unique solution (s, y) to the Dio-
phantine equation 2ny − 3
rs = c, where c is defined in (13) and r = ⌊ n
log2 3 ⌋. Here, y = T n(s) < s < 2
n, y < 3
r, and
σ(s) = n.

As stated in Lemma (4.5), if s is a starting number such that σ(s) = n, then the transition sequence T rn(s) = {t1, . . . , tn}
contains exactly r = ⌊ n
log2 3 ⌋ elements of 3
2 and n − r elements of 1
2 , ensuring that ∏n
j=1 tj < 1 and ∏i
j=1 tj > 1 for all
i < n. The quantity zn is precisely the number of transition sequences T rn(s) that satisfy (14).

The number of combinations of r elements of 3
2 and n − r elements of 1
2 is ( n
r(n)), where r(n) = ⌊ n
log2(3) ⌋.

We must subtract the number of Syracuse sequences with stopping times less than n.
For all i < n, the number of sequences of transition T ri(s) = {t1, . . . , ti} satisfying :

j=i∏

j=1 tj < 1 and
 j=l∏

j=1 tj > 1 for all l < i

14

given by ( n − i
r(n) − r(i)

)zi

Thus, summing on all 0 < i < n the following sum :

r−1∑

i=1
 ( n − i
r(n) − r(i)
)
zi

This yields the final expression of the Stopping Time counting function available, for all n < 19,478,780,533 according
to the main Garner’s theorem and lemme 3.1 and mre generally for all n according to our theorem 4.7:

zn = hn(n) = ( n
r(n)

) −
 n−1∑

i=1
 ( n − i
r − r(i)

) · zi

We have provided an exact formulation of the counting function for the set of integers s in Z/2
nZ that have a finite
stopping time σ(s) = n, .

We compute below the first numbers of integers s < 2
n such that σ(s) = n.

z1 = (1
0
)

z2 = (2
1
) − (1
1).z1 = 1
z3 = (3
1
) − (2
1).z1 − (1
0).z2 = 0
z4 = (4
2
) − (3
2
).z1 − (2
1).z2 − (1
0).z3 = 1
z5 = (5
3
) − (4
3
).z1 − (3
2
).z2 − (2
1).z3 − (1
1).z4 = 2
z6 = (6
3
) − (5
3
).z1 − (4
2
).z2 − (3
1
).z3 − (2
1).z4 − (1
0).z5 = 0
z7 = (7
4
) − (6
4
).z1 − (5
3
).z2 − (4
2
).z3 − (3
2
).z4 − (2
1).z5 − (1
0).z6 = 3
z8 = (8
5
) − (7
5
).z1 − (6
4
).z2 − (5
3
).z3 − (4
3
).z4 − (3
2
).z5 − (2
1
).z6 − (1
1).z7 = 7
z9 = (9
5
) − (8
5
).z1 − (7
4
).z2 − (6
3
).z3 − (5
3
).z4 − (4
2
).z5 − (3
1
).z6 − (2
1
).z7 − (1
0).z8 = 0
z10 = (10
6 ) − (9
6
).z1 − (8
5
).z2 − (7
4).z3 − (6
4).z4 − (5
3).z5 − (4
2
).z6 − (3
2
).z7 − (2
1
).z8 − (1
0
).z9 = 12
z11 = (11
6 ) − (10
6 ).z1 − (9
5
).z2 − (8
4
).z3 − (7
4
).z4 − (6
3
).z5 − (5
2
).z6 − (4
2
).z7 − (3
1
).z8 − (2
0
).z9 − (1
0
).z10 = 0
z12 = (12
7 ) − (11
7 ).z1 − (10
6 ).z2 − (9
5
).z3 − (8
5
).z4 − (7
4
).z5 − (6
3
).z6 − (5
3
).z7 − (4
2
).z8 − (3
1
).z9 − (2
1).z10 − (1
0
).z11 = 30
z13 = (13
8 ) − (12
8 ).z1 − (11
7 ).z2 − (10
6 ).z3 − (9
6
).z4 − (8
5
).z5 − (7
4
).z6 − (6
4
).z7 − (5
3).z8 − (4
2).z9 − (3
2
).z10 − (2
1
).z11 − (1
1
).z12 = 85

We can see that this formulation of the Stopping time counting function give zn = 0 for the integers n which cannot be
a stopping time value. to stopping time, in other words, where zn = 0.

Theorem 5.5. For every integer n and if all integers s < 2
n such that σ(s) = n satisfy the condition σ(s) = ω(s),
then the number of residue classes modulo 2n of integers s such that σ(s) = n is given by the following expression:

zn(r) = hn(r)(n(r)) = (n(r)
r
 ) −
 r−1∑

i=0
 (n(r) − n(i)
r − i
 )zn(i) (15)

with z1 = 1, and r(i) = ⌊ i
log2(3) ⌋, for i ∈ N.

This formulation corresponds to a new indicial referential, the sum is done on the number of odd iterates and not on
all iterates. The main difference is that this formulation only provides the value of zn for all n which are a real
stopping time. We detail in the following the expression of the first values of zn and observe that the coefficients of zn,
where n is a stopping time, are identical in both formulations of Theorems 5.4 and 5.5.
z1 = 1
z2 = (2
1
) − (1
1).z1 = 1
z4 = (4
2
) − (3
1).z1 − (2
1).z2 = 2
z5 = (5
3
) − (4
3
).z1 − (3
2).z2 − (1
1).z4 = 2
z7 = (7
4
) − (6
4
).z1 − (5
3
).z2 − (3
2).z4 − (2
1).z5 = 3
z8 = (8
5
) − (7
5
).z1 − (6
4
).z2 − (4
3
).z4 − (3
2).z5 − (1
1).z7 = 7
z10 = (10
6 ) − (9
6
).z1 − (8
5
).z2 − (6
4
).z4 − (5
3
).z5 − (3
2
).z7 − (2
1
).z8 = 12
z12 = (12
7 ) − (11
7 ).z1 − (10
6 ).z2 − (8
5).z4 − (7
4).z5 − (5
3).z7 − (4
2
).z8 − (2
1
).z10 = 30
z13 = (13
8 ) − (12
8 ).z1 − (11
7 ).z2 − (9
6).z4 − (8
5).z5 − (6
4
).z7 − (5
3
).z8 − (3
2
).z10 − (1
1
).z12 = 85
z15 = (15
9 ) − (14
9 ).z1 − (13
8 ).z2 − (11
7 ).z4 − (10
6 ).z5 − (8
5
).z7 − (7
4
).z8 − (5
3
).z10 − (3
2
).z12 − (2
1
).z13 = 173
z16 = (16
10
) − (15
10
).z1 − (14
9 ).z2 − (12
8 ).z4 − (11
7 ).z5 − (9
6
).z7 − (8
5
).z8 − (6
4
).z10 − (4
3
).z12 − (3
2
).z13 − (2
1
).z15 = 476
z18 = (18
11
) − (17
11
).z1 − (16
10
).z2 − (14
9 ).z4 − (13
8 ).z5 − (11
7 ).z7 − (10
6 ).z8 − (8
5
).z10 − (6
4).z12 − (5
3
).z13 − (3
2
).z15 − (2
1
).z16 = 961

15

5.2 Computational results

We have applied (12) up to n=76001 (python code in Appendix B) and give in table 2 the 60 first values of zn(r). We
have also verified the collatz conjecture for all positive integer below 2
50 and have also computed all histograms Hn for
all n ≤ 50 giving the counts of hn(p) and particularly the hn(n) the number of positive integer s lower than 2n such
that σ(s) = n (python code in appendix A).

n r(n) zn = hn(n) π(2n )
2n = 1 − S(n)
2n S(n)
2n
1 0 1 0,50000000 0,50000000
2 1 1 0,75000000 0,25000000
3 1 0 0,75000000 0,25000000
4 2 1 0,81250000 0,18750000
5 3 2 0,87500000 0,12500000
6 3 0 0,87500000 0,12500000
7 4 3 0,89843750 0,10156250
8 5 7 0,92578125 0,07421875
9 5 0 0,92578125 0,07421875
10 6 12 0,93750000 0,06250000
11 6 0 0,93750000 0,06250000
12 7 30 0,94482422 0,05517578
13 8 85 0,95520020 0,04479980
14 8 0 0,95520020 0,04479980
15 9 173 0,96047974 0,03952026
16 10 476 0,96774292 0,03225708
17 10 0 0,96774292 0,03225708
18 11 961 0,97140884 0,02859116
19 11 0 0,97140884 0,02859116
20 12 2652 0,97393799 0,02606201
21 13 8045 0,97777414 0,02222586
22 13 0 0,97777414 0,02222586
23 14 17637 0,97987664 0,02012336
24 15 51033 0,98291844 0,01708156
25 15 0 0,98291844 0,01708156
26 16 108950 0,98454192 0,01545808
27 17 312455 0,98686989 0,01313011
28 17 0 0,98686989 0,01313011
29 18 663535 0,98810582 0,01189418
30 18 0 0,98810582 0,01189418
31 19 1900470 0,98899080 0,01100920
32 20 5936673 0,99037304 0,00962696
33 20 0 0,99037304 0,00962696
34 21 13472296 0,99115723 0,00884277
35 22 39993895 0,99232121 0,00767879
36 22 0 0,99232121 0,00767879
37 23 87986917 0,99296139 0,00703861
38 23 0 0,99296139 0,00703861
39 24 257978502 0,99343065 0,00656935
40 25 820236724 0,99417666 0,00582334
41 25 0 0,99417666 0,00582334
42 26 1899474678 0,99460855 0,00539145
43 27 5723030586 0,99525918 0,00474082
44 27 0 0,99525918 0,00474082
45 28 12809477536 0,99562325 0,00437675
46 29 38036848410 0,99616378 0,00383622
47 29 0 0,99616378 0,00383622
48 30 84141805077 0,99646271 0,00353729
49 30 0 0,99646271 0,00353729
50 31 248369601964 0,99668331 0,00331669
51 32 794919136728 0,99703633 0,00296367
52 32 0 0,99703633 0,00296367
53 33 1857112329035 0,99724251 0,00275749
54 34 5636545892795 0,99755540 0,00244460
55 34 0 0,99755540 0,00244460
56 35 12732900345928 0,99773210 0,00226790
57 35 0 0,99773210 0,00226790
58 36 38088111350198 0,99786425 0,00213575
59 37 123110229387834 0,99807781 0,00192219
60 37 0 0,99807781 0,00192219

Table 2: First 60 values of the stopping time counting function

For n=100, S(n)
2n ≃ 0, 000225 and θ(n) = log2(S(n))
n ≃ 0.8788221262 and z100 = 32053249939776775765443011

For n = 405, S(n)
2n ≃ 9.68160440706356E − 10 and θ(n) = log2(S(n))
n ≃ 0.9260641116 and
z405 =3476553789120508476368100052260690271283238505581916333757459587755180695960919229021382116342674546834066825086

For n=76001, S(n)
2n ≃ 5, 785339919e − 1152 and θ(n) = log2(S(n))
n ≃ 0.949680546787772

16

6 Asymptotic Density of Positive Integers with High Stopping Times

Thanks to (12), we have computed the values of the counting function zn(r) and of the density functions π(2
n)
2n , S(n)
2n up
to n=76001. The results presented in figure 1 and figure 2 , which seems to confirm that θ(n) = log2(S(n))
n tends to a
constant value less than 1. A formal proof is provided below.

Figure 1: function Log2(S(n))

Figure 2: function θ(n) = Log2(S(n))
n

These numerical results based on the application of the stopping time counting function illustrate that the above function
asymptotically tends towards a constant which seems to be less than 0.95. We will formally confirm this result in the
following theorem.

We aim to show that the density of integers s ∈ N whose stopping time satisfies σ(s) ≤ n tends to 1 as n → ∞. This
asymptotic behavior was first conjectured by Riho Terras [7] in 1976, and stronger forms were subsequently established
by Jean-Paul Allouche [8] in 1978 and Yvan Korec [9] in 1994. In this work, we introduce a new approach based on the
stopping-time counting function.
 17

Theorem 6.1. As long as σ(s) = ω(s) for all s < 2
n such that σ(s) = n, the percentage of residue classes mod 2n of
starting numbers s such that σ(s) > n, given by S(n)
2n , tends to 0 as n approaches infinity. Moreover, there exists a
constant θ < 1 such that S(n) < 2
nθ for sufficiently large n.

Proof. From (10) and Theoreme 4.7, we have

S(n) = 2
n
 

1 −
 r(n)∑

r=1
 zp(r)
2p(r)
 

 = 2
n ∞∑

r(n+1)
 zp(r)
2p(r) .

We seek an upper bound for the last term of the inequality above.
From (15), we have:
 zp(r) = (p(r)
r
 ) −
 r−1∑

i=0
 (p(r) − p(i)
r − i
 ) · zp(i) ≤ (p(r)
r
 )

Using the asymptotic Laplace approximation of the factorial, we have:

n! ∼ nne−n√2πn (1 + 1
12n + 1
288n2 − O ( 1
n3
 ))

we can derive an upper bound for ( p
xp) when p is sufficiently large, xp ∈ N, and 0 < x < 1
( p
xp
) = p!
(x.p)! · (p − x.p)! ,

We substitute the three factorials with their asymptotic formula.

( p
xp
) ≃
 pp

e−p · √2Πp · (1 + 1
12p + o ( 1
p2 ))

( (xp)xp
e−xp · √2πxp · (1 + 1
12.xp + o ( 1
(xp)2 ))) · ( ((1−x)p)(1−x)p

e(1−x)p · √
2π(1 − x)p · (1 + 1
12.(1−x)p + o ( 1
((1−x)p)2 )))

Which can be significantly simplified to write:
( p
xp
) ≃ 1
√2πx(1 − x)p · ( 1
xx(1 − x)1−x
 )p ·
 (

1 − A
12p + 1
2 · ( A
12p
 )2 + o ( 1
p3
 ))

with A = 1−x+x2
x·(1−x) . The last term (
1 − A
12p + 1
2 · ( A
12p )2 + o ( 1
p3 )) is less than one for all p. Finally, we can obtain the

following upper bound ;
( p
xp
) < a · qp
√p where a = 1
√2πx(1 − x) and q = 1
xx(1 − x)1−x with x = r
p(r) < ln(2)
ln(3)

Effectively, since p is a stopping time value and r is the number of odd iterates, we have r = ⌊ p
log2(3) ⌋. Therefore, by
definition of the floor function, it follows directly that r < p
log2(3) .
Moreover, if we study the variations of the following function which represent the main term of the above approximation
of ( p
xp
) :
 Fp(x) = 1

(xx(1 − x)1−x)p√2πx(1 − x)p

As Fp(x) = Fp(1 − x), this function is symmetric at x = 1
2 and tends to +∞ as x → 0 or x → 1. There is a minimum
at x = 1
2 and F is a strictly growing function between 1
2 and 1. So we have:

Fp
 ( 1
2
 ) < Fp
 ( r
p(r)
 ) < Fp
 ( ln(2)
ln(3)
 )

which implies that

zp(r) < (p(r)
r
 ) < a qp
√p where a = 1
√2πx(1 − x) and q = 1
xx(1 − x)1−x with x = ln(2)
ln(3)

We can give numerical values of these parameters : x ≃ log(2)
log(3) ≃ 0.63093, q ≃ 1.93181, and a ≃ 0.82673.
And we finally obtain an upper bound of the density function:

zp(r)
2p(r) < 1
2p
 (p
r
) ≃ a
√p
 ( q
2
 )p where q
2 ≃ 0.96591 (16)

18

This result aligns with the upper bound discussed by Terence Tao [10] on his blog about the Collatz conjecture. Using
(16), we derive an upper bound for (10):

S(n)
2n = ∑

i>r(n)
 zp(i)
2p(i) < ∑

j>n
 zj
2j < ∑

j>n
 a
√j
 ( q
2
 )j < a
√n + 1 · ∑

j>n
 √ n + 1
j
 ( q
2
 )j

As √ n+1
j ≤ 1 for all j > n then :

S(n)
2n < a
√n + 1 · ∑

j>n
 ( q
2
 )j = a
√n + 1 · ( q
2
 )n+1 ∑

i≥0
 ( q
2
 )j < C
√n + 1
 ( q
2
 )n+1

And finally S(n)
2n < C
√n + 1
 ( q
2
 )n+1 with C = a
(1 − q/2) ≃ 24.28 (17)

We conclude that, as S(n)
2n > 0 and has an upperbound which tends to 0 when n tends to infinity, then :

lim
n→∞ S(n)
2n = lim
n→∞ C
√n + 1
 ( q
2
 )n+1 = 0. (18)

Theorem 6.2. As long as σ(s) = ω(s) for all s < 2
n such that σ(s) = n, there exists a constant θ < 1 such that
S(n) < 2nθ for sufficiently large n.

Proof. For sufficiently large n, we are looking for a real number 0 < θ < 1 such that S(n) < 2nθ. According to the
previous theorem and equation (17), we have the following bound:

S(n) < C · qn+1

2
√n + 1 .

We seek θ satisfying:
 S(n) < C · qn+1

2
√n + 1 < 2
n·θ.

Taking the base-2 logarithm of both sides of the two inequalities (which preserves the inequality since log2(x) is
increasing), we are looking for θ which satisfy to:

log2 S(n) < n · log2(q) − log2(n + 1)
2 + log2
 ( C · q
2
 ) < n · θ.

Defining the arithmetic function:
 θ(n) = log2(q) − log2(n + 1)
2n + log2 ( C·q
2 )

n ,

which is a monotonically increasing function for sufficiently large n. It is clear that:

θ(n) ≤ log2(q) ≈ 0.94996.

Since we have already verified numerically that θ(n) = log2(S(n))
n ≈ 0.94968 for n = 76001, it confirms the coherence of
our estimation.
Therefore, for all n > 550, we can take: θ = log2(q) ≈ 0.94996,

such that the inequality S(n) < 2nθ holds, as supported by our computational results.

19

7 Highest and lowest trajectories before the stopping time iterate

As we have seen in Section 3, the set of integers s < 2n with a stopping time σ(s) = n generates a set of trajectories of
Syracuse sequences, from the starting number s to the iterate at the stopping time. We will characterize the lowest and
highest trajectories of this set. Specifically, we will show that the highest trajectory corresponds to the lowest value of
c = cn(s), as defined in (13), and the lowest trajectory corresponds to the highest value of c.
Let s be the starting number of a Syracuse sequence such that σ(s) = n. We have seen that (s, T n(s)) is a solution of
the Diophantine equation:

2
n · T n(s) − 3r · s = cn(s), where r = ⌊ n
log2(3)
 ⌋ and c = cn(s).

We define: cn,min = min
(s<2n,σ(s)=n) cn(s) and cn,max = max
(s<2n,σ(s)=n) cn(s).

First, we will derive the arithmetic function that gives cn,min as a function of n. For each n, the highest trajectory
corresponding to σ(s) = n is associated with a sequence of transitions T rn(s), where the first r terms are equal to 3
2
and the last n − r terms are equal to 1
2 :

T rn(s) = {t1, . . . , tn} where ti = 3
2 for 1 ≤ i ≤ r and ti = 1
2 for r < i ≤ n.

The Value of cn associated to the highest trajectory of the family of integer s such that σ(s) = n is given by the following
equation and we shall see in the next theorem that it corresponds to the minimum value of cn(s):

cn,min =
 r∑

i=1 3
(r−i) · 2
(i−1) = 3
r − 2
r. (19)

**Examples:**
1. For σ(s) = 7, the highest trajectory is obtained for s = 15, and the iterate at stopping time is T 7(s) = 10, which
satisfies the Diophantine equation 2
7 · T 7(s) − 3
4 · s = c with c = 3
4 − 2
4 = 65, the lowest value of c.
2. For σ(s) = 8, the highest trajectory is obtained for s = 95, and the iterate at the stopping time is T 8(s) = 91, which
satisfies the Diophantine equation 2
8 · T 8(s) − 3
5 · s = c with c = 3
5 − 2
5 = 211, also the lowest value of c.

To explicitly construct the lowest trajectory, we start from an integer s < 2
n such that σ(s) = n, and look for a syracuse
sequence corresponding to this trajectory. Like in a previous section, it appears more comfortable to use the transition
sequence associated with the lowest syracuse sequence of stopping time equal to n. This transition sequence has to
satisfy the following conditions:

for all k < n , 1 <
 k∏

j=1 tj < 2 or if
 k∏

j=1 tj > 2 then tk+1 = 1
2 and
 n∏

j=1 tj < 1

Formalizing precisely this iterative construction, we find that the r terms tj = 3
2 are exactly located:

j = ⌊(i − 1) log2(3)⌋ + 1, for 1 ≤ i ≤ r, with r = ⌊ n
log2(3)
 ⌋

Theorem 7.1. For all integers s < 2n such that σ(s) = n :

cn,max = max
(s<2n,σ(s)=n) cn(s) exist and cn,max =
 r∑

i=1 3
(r−i) · 2
⌊(i−1) log2(3)⌋, where r = ⌊ n
log2(3)
 ⌋ . (20)

cn,min = min
(s<2n,σ(s)=n) cn(s) exist and cn,min =
 r∑

i=1 3
(r−i) · 2(i−1) = 3
r − 2
r, where r = ⌊ n
log2(3)
 ⌋ . (21)

Proof. Any sequence of transitions corresponding to a Syracuse sequence starting from s with σ(s) = n contains r terms
equal to 3
2 and n − r terms equal to 1
2 . It is easy to see that the highest trajectory corresponds to the sequence of
transitions where ti = 3
2 for i ≤ r. We are going to show that when we permute the two elements of this pattern 3
2 , 1
2
in a sequence of transition, keeping the stopping time unchanged, the value of cn(s) increases.
Consider two sequences of transitions with the same terms ti, except at positions k and k + 1:

T rn(s1) = {ti, 1 ≤ i ≤ n} with tk = 3
2 and tk+1 = 1
2 ,

20

T rn(s2) = {ti, 1 ≤ i ≤ n} with tk = 1
2 and tk+1 = 3
2 .

Then:
 cn(s1) = 2
n

3
 

k−1∑

i=1
 n∏

j=i if ti= 3
2
 tj +
 n∏

j=k as tk= 3
2
 tj +
 n∑

i=k+2
 n∏

j=i if ti= 3
2
 tj


 ,

cn(s2) = 2n

3
 


k−1∑

i=1
 n∏

j=i if ti= 3
2
 tj +
 n∏

j=k+1 as tk+1= 3
2
 tj +
 n∑

i=k+2
 n∏

j=i if ti= 3
2
 tj


 .

The difference:
 cn(s2) − cn(s1) =
 n∏

j=k+1 as tk+1= 3
2
 tj −
 n∏

j=k if tk= 3
2
 tj = 1
2
 n∏

j=k+1 as tk+1= 3
2
 tj > 0,

which implies cn(s2) > cn(s1). This justifies that when we permute a pair { 3
2 , 1
2 } into { 1
2 , 3
2 }
, the value of cn(s) in-
creases. Since there are only a finite number of s with σ(s) = n, the maximum value cn,max is reached for a sequence
defined as above. The highest trajectory, the r terms 3
2 correspond to the r first terms of the sequence of transition and
according to the above result provide the minimum value of cn(s):

cn,min =
 r∑

i=1 3
(r−i) · 2(i−1) = 3
r − 2
r where r = ⌊ n
log2(3)
 ⌋

Starting from the sequence of transitions where the positions of the i-th term 3
2 are located at ⌊(i − 1) log2(3)⌋ + 1, any
permutation would result in a sequence with a stopping time lower than n. And according to the above result provide
the maximum value of cn(s) :
 cn,max =
 r∑

i=1 3r−i2
⌊(i−1) log2(3)⌋ where r = ⌊ n
log2(3)
 ⌋

By construction, the lowest trajectory oscillates mainly between s and 2s, and whenever an iterate at step i < n exceeds
2s, the next iterate (at step i + 1) is forced below 2s. If, in the associated transition sequence, we permute a pair { 3
2 , 1
2 },
the previous iterate would become less than s, which contradict the hypothesis that σ(s) = n. In table 3, we give the
first values of cnmax.
 n cnmax n cnmax
5 23 51 14535113675299973
7 85 53 44731240932742543
8 319 54 138697322425598125
10 1085 56 425099166531535367
12 3767 58 1311326296613570069
13 13349 59 4078094077916566079
15 44143 61 12522512609901409981
16 148813 62 3872045933431107691
18 479207 64 118467221012146924709
20 1568693 65 364625035073295549935
21 5230367 67 1112321849293596201421
23 16739677 69 3410752524175626810727
24 54413335 70 10527405477706233258037
26 171628613 72 32172512243477405425823
27 548440271 73 98878719971867038884317
29 1712429677 75 301358526398470761866647
31 5405724487 77 922965045126890866454725
32 17290915285 78 2844452999106586922783311
34 54020229503 80 8684474724771589415188205
35 170650623101 81 26657887084122082832917703
37 529131738487 83 81182587071980877673459285
39 1656114692197 85 248383464494401149719202559
40 5243221983535 86 764493206597037515952906493
42 16279421764493 88 2332165246018780681449317111
43 51037288549031 89 7151238242967014578710341861
45 157509912158197 91 21763199738722388804855806639
46 490121922519007 92 66527539255452546689466544141
48 1505550139645853 94 202058497844928400618197880871
50 4657387907292887 96 616079013849068244053786636405

Table 3: First values of cnmax

Lemma 7.2. cn,max has an upper bound : cn,max < r · 3
r−1

Proof. ach term in the above sum representing cn,max can be bounded above as follows:

3r−i2
⌊(i−1) log2(3)⌋ < 3
r−i2
(i−1) log2(3) = 3
r−i3
i−1 = 3
r−1.

Thus, cn,max =
 r∑

i=1 3
r−i2⌊(i−1) log2(3)⌋ <
 r∑

i=1 3r−1 = r · 3r−1 where r = ⌊ n
log2(3)
 ⌋

21

8 Conclusion

In this paper, we have established several important results regarding the link between stopping times and non-trivial
cycles in Syracuse (Collatz) sequences:

1. We extended the work initiated by Lynn E. Garner (1981), who demonstrated that as long as the stopping time
equals the coefficient stopping time, no non-trivial cycle can exist.

2. We revealed a particularly noteworthy property: two Syracuse sequences starting from integers s and 2
n · m + s
exhibit exactly the same behavior up to the nth iterate.

3. Building on these initial findings, we proved rigorously that the stopping time always equals the coefficient
stopping time. This result implies directly that non-trivial cycles cannot exist.

4. Furthermore, we provided an explicit formula for the stopping time counting function, giving the exact number
zn(r) of positive integers s < 2n with stopping time σ(s) = n:

zn = ( n
r(n)
) −
 n−1∑

i=1
 ( n − i
r − r(i)

) · zi

5. By combining these results, we demonstrated that the density of integers s < 2n satisfying σ(s) > n tends to zero
as n approaches infinity.

6. Lastly, we precisely characterized the Syracuse sequences corresponding to the highest and lowest trajectories
associated with a given stopping time σ(s) = n. We derived explicit arithmetic expressions for the corresponding
parameters cn,min and cn,max.

These results collectively provide a deeper understanding of the intricate behavior and structure of Syracuse sequences,
offering further insight into the validity and complexity of the Collatz conjecture.

References

[1] Lynn E. Garner. On the collatz 3n+1 algorithm. Proceedings of the American Mathematical Society, 82(1), 1981.

[2] Mike Winkler. New results on the stopping time behaviour of the collatz 3x+1 function, 2017. https://arxiv.
org/abs/1504.00212 https://www.mikematics.de.

[3] David Barina. Convergence verification of collatz problem. The Journal of Supercomputing, 77:2681–2688, 2021.

[4] Thomas Oliveira e Silva. Maximum excursion and stopping time record-holder for the 3x+1 problem: computational
results. Mathematics of Computation, 68(225):371–384, 1999.

[5] Shalom Eliahou. Le problème 3n+1 : Y a-t-il des cycles non triviaux ? https://images.math.cnrs.fr/
Le-probleme-3n-1-y-a-t-il-des-cycles-non-triviaux-III.html, 2011.

[6] Jeffrey C. Lagarias. The Ultimate Challenge: The 3x + 1 Problem. American Mathematical Society, 2011.

[7] Riho Terras. A stopping time problem on the positive integers. Acta Arithmetica, 30(3):241–252, 1976.

[8] Jean-Paul Allouche. Sur la conjecture de “syracuse - kakutani - collatz“. Séminaire de Théorie des Nombres de
Bordeaux, pages 1–16, 1978. http://eudml.org/doc/182044.

[9] Yvan Korec. A density estimate for the 3x+1 problem. Mathematica Slovaca, 44(1):85–89, 1994. http://eudml.
org/doc/32414.

[10] Terence Tao. The collatz conjecture, littlewood-oxford theory and powers of 2 and 3. https://terrytao.
wordpress.com, 2011.
 22

1 # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

2 # Script 1: Histogram computation of integers s < 2^ n

3 # such that Collatz stopping time of s is p

4 # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

5

6 import os

7 import argparse

8 import time

9 import multiprocessing as mp

10 import numpy as np

11 import struct

12 from numba import jit

13 import gc

14

15 LIMIT = 2 ** 60

16

17 def create_initial_file ( init_value , iterations , n_min , directory ) :

18 filename = os . path . join ( directory , f " Collatz_ { init_value } _ { n_min }. bin " )

19 with open ( filename , ’ wb ’) as f :

20 f . write ( struct . pack ( ’ qH ’ , init_value , iterations ) )

21 return filename

22

23 @jit ( nopython = True )

24 def count_trailing_zeros ( value ) :

25 count = 0

26 while ( value & 1) == 0:

27 value > >= 1

28 count += 1

29 return count

30

31 @jit ( nopython = True )

32 def c ol lat z_f un cti on _nu mba ( start_value ) :

33 iterations = 0

34 value = start_value

35 value = 3 * value + 1

36 zeros = count_trailing_zeros ( value )

37 value > >= zeros

38 iterations += zeros

39 while value > start_value :

40 value = 3 * value + 1

41 zeros = count_trailing_zeros ( value )

42 value > >= zeros

43 iterations += zeros

44 if value > LIMIT :

45 return value , iterations

46 while value < start_value :

47 value < <= 1

48 iterations -= 1

49 iterations += 1

50 return value , iterations

51

52 def co ll at z _f un ct i on _p y th on ( start_value , value , iterations ) :

53 while value > start_value :

54 value = 3 * value + 1

55 zeros = ( value & - value ) . bit_length () - 1

56 value > >= zeros

57 iterations += zeros

58 while value < start_value :

59 value < <= 1

60 iterations -= 1

61 iterations += 1

62 return iterations

63

64 def collatz_function ( start_value ) :

65 value , iterations = c oll at z_f unc ti on_ nu mba ( start_value )

23

66 if value >= LIMIT :

67 iterations = c ol l at z_ fu n ct io n _p yt ho n ( start_value , value , iterations )

68 return iterations

69

70 def process_block ( block , n ) :

71 results = []

72 two_power_n = 2 ** n

73 for number , input_iterations in block :

74 results . append (( number , input_iterations ) )

75 if input_iterations > n :

76 augmented_number = number + two_power_n

77 iteration_count = collatz_function ( augmented_number )

78 if iteration_count > n :

79 results . append (( augmented_number , iteration_count ) )

80 return results

81

82 def process_iteration ( input_file , output_file , histo_file , n , block_size , num_cores ,
↪→ previous_histogram ) :

83 pool = mp . Pool ( num_cores )

84 with open ( output_file , ’ wb ’) as out_f , open ( input_file , ’ rb ’) as in_f :

85 final_histogram = np . copy ( previous_histogram )

86 histo_tab = np . zeros ((1000 ,) , dtype = np . int64 )

87 block_group = []

88

89 while True :

90 for _ in range ( num_cores ) :

91 block = []

92 for _ in range ( block_size ) :

93 data = in_f . read (10)

94 if not data :

95 break

96 number , input_iterations = struct . unpack ( ’ qH ’ , data )

97 block . append (( number , input_iterations ) )

98 if block :

99 block_group . append ( block )

100 if not data :

101 break

102

103 if not block_group :

104 break

105

106 results = pool . starmap ( process_block , [( block , n ) for block in block_group ])

107

108 for processed_block in results :

109 out_f . write ( b ’ ’. join ([ struct . pack ( ’ qH ’ , num , it ) for num , it in
↪→ processed_block ]) )

110 out_f . flush ()

111 for num , it in processed_block :

112 if num > 2 ** n :

113 histo_tab [ it ] += 1

114

115 block_group = []

116

117 pool . close ()

118 pool . join ()

119 new_histogram = np . zeros ( len ( histo_tab ) , dtype = np . uint64 )

120 new_histogram [: len ( previous_histogram ) ] = previous_histogram

121 final_histogram = histo_tab + new_histogram

122 final_histogram = final_histogram . astype ( ’ uint64 ’)

123

124 with open ( histo_file , ’w ’) as f :

125 for count in final_histogram :

126 f . write ( f " { count }\ n " )

127

128 gc . collect ()
 24

129 return final_histogram

130

131 def re ad _p r ev io us _ hi st o gr am ( init_value , init_iterations , n , directory ) :

132 histo_file = os . path . join ( directory , f " Histo_ { init_value } _ { n }. txt " )

133 if os . path . exists ( histo_file ) :

134 with open ( histo_file , ’r ’) as f :

135 histogram = [ int ( line . strip () ) for line in f . readlines () ]

136 return np . array ( histogram , dtype = np . uint64 )

137 else :

138 return np . zeros ( init_iterations + 1 , dtype = np . uint64 )

139

140 def iterative_collatz ( init_value , init_iterations , n_min , n_max , block_size , num_cores ,
↪→ directory ) :

141 if not os . path . exists ( directory ) :

142 os . makedirs ( directory )

143 if not os . path . exists ( os . path . join ( directory , f " Collatz_ { init_value } _ { n_min }. bin " ) ) :

144 create_initial_file ( init_value , init_iterations , n_min , directory )

145

146 for n in range ( n_min , n_max + 1) :

147 current_input = os . path . join ( directory , f " Collatz_ { init_value } _ { n }. bin " )

148 current_output = os . path . join ( directory , f " Collatz_ { init_value } _ { n + 1}. bin " )

149 histo_file = os . path . join ( directory , f " Histo_ { init_value } _ { n + 1}. txt " )

150 if n > n_min + 1:

151 os . remove ( os . path . join ( directory , f " Histo_ { init_value } _ { n - 1}. txt " ) )

152 os . remove ( os . path . join ( directory , f " Collatz_ { init_value } _ { n - 1}. bin " ) )

153

154 print ( f " Processing n ={ n + 1} , init_value ={ init_value }... " , time . ctime () )

155 start_time = time . time ()

156

157 previous_histogram = re a d_ pr e vi ou s_ h is to gr a m ( init_value , init_iterations , n ,
↪→ directory )

158 if n == n_min and previous_histogram [ init_iterations ] == 0:

159 previous_histogram [ init_iterations ] += 1

160

161 final_histogram = process_iteration (

162 current_input , current_output , histo_file , n , block_size , num_cores ,
↪→ previous_histogram )

163

164 print ( f " Step { n + 1}: { final_histogram . tolist () } " )

165 print ( f " Elapsed time for n ={ n + 1}: { time . time () - start_time :.2 f } seconds " )

166

167 del previous_histogram

168 gc . collect ()

169

170 if __name__ == " __main__ " :

171 parser = argparse . ArgumentParser ( description = " Iterative Collatz histogram computation . "
↪→ )

172 parser . add_argument ( " - init " , " -- init_value " , type = int , default =3)

173 parser . add_argument ( " - init_iter " , " -- init_iterations " , type = int , default =4)

174 parser . add_argument ( " - nmin " , " -- n_min " , type = int , default =1)

175 parser . add_argument ( " - nmax " , " -- n_max " , type = int , default =49)

176 parser . add_argument ( " -b " , " -- block_size " , type = int , default =10**4)

177 parser . add_argument ( " -c " , " -- num_cores " , type = int , default =2)

178 parser . add_argument ( " -d " , " -- directory " , type = str , default = " F :/ Collatz / " )

179

180 args = parser . parse_args ()

181 iterative_collatz ( args . init_value , args . init_iterations , args . n_min , args . n_max , args .
↪→ block_size , args . num_cores , args . directory )

182

183 # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

184 # Script 2: Computing the number of residue classes z_n

185 # with stopping time exactly equal to n

186 # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

187

188 from math import floor , log2 , comb
 25

189 import time

190

191 print ( time . ctime () )

192

193 max_r = 48000

194 max_n = floor ( max_r * log2 (3) + 1)

195 n_list = [0] * ( int (1.6 * max_r ) )

196 n_list [0:4] = [1 , 2 , 4 , 5]

197 z_list = [0] * ( int (1.6 * max_r ) )

198 z_list [1] , z_list [2] , z_list [4] = 1 , 1 , 1

199 Pi_list = [0] * ( int (1.6 * max_r ) )

200 Pi_list [0:3] = [1 , 3 , 13]

201 comb_table = [[ None ] * ( max_r + 1) for _ in range ( max_n + 1) ]

202

203 print ( time . ctime () )

204 Log2_10 = 1 / log2 (10)

205 r = 3

206 den = 2** n_list [r -1]

207

208 while r < max_r :

209 n = floor ( r * log2 (3) + 1)

210 n_list [ r ] = n

211 sum_ = 0

212 for i in range ( r - 1 , 1 , -1) :

213 I = floor ( i * log2 (3) + 1)

214 if comb_table [ n - I ][ r - i ] is None :

215 comb_table [ n - I ][ r - i ] = comb ( n - I , r - i )

216 sum_ += comb_table [ n - I ][ r - i ] * z_list [ I ]

217

218 comb_table [ n - 2][ r - 2] = comb ( n - 2 , r - 2)

219 comb_table [ n ][ r ] = comb ( n - 2 , r - 2) * n * ( n - 1) // r // ( r - 1)

220 z_list [ n ] = comb_table [ n - 2][ r - 2] - sum_

221

222 mult_factor = 2 ** ( n - n_list [ r - 1])

223 Pi_list [ r ] = mult_factor * Pi_list [ r - 1] + z_list [ n ]

224 den *= mult_factor

225 Sn = den - Pi_list [ r ]

226 Log2_Sn = log2 ( Sn )

227 theta_n = Log2_Sn / n

228

229 print (n , r , theta_n , ( Log2_Sn - n ) * Log2_10 , time . ctime () )

230 r += 1

231

232 print ( time . ctime () )

233

234 # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

235 # Script 3: Computing b ( M ) and B ( M ) in Garner ’s theorem

236 # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

237

238 import mpmath as mp

239 from mpmath import ln , mpf

240 import time

241

242 mp . dps = 30

243 c2 = ln (2)

244 c3 = ln (3)

245 c23 , c32 = c2 / c3 , c3 / c2

246 C2 , C3 , C23 , C32 = mpf ( c2 ) , mpf ( c3 ) , mpf ( c23 ) , mpf ( c32 )

247

248 r = 1

249 BM = bM = mpf (1)

250 M = 10**12

251 threshold = mpf ( ’1e -10 ’)

252

253 print ( " Start : " , time . ctime () )
 26

254

255 while r <= M :

256 n = int ( r * c32 ) + 1

257 test1 = c23 - r / n

258 test2 = r / ( n - 1) - c23

259

260 if test1 < threshold :

261 B = C2 * n - C3 * r

262 if B < BM :

263 BM = B

264 print ( f ’ 1; r ={ r }; n ={ n }; BM ={ - ln ( BM ) / C3 }; Time : { time . ctime () } ’)

265

266 if test2 < threshold :

267 b = C3 * r - C2 * ( n - 1)

268 if b < bM :

269 bM = b

270 print ( f ’ 2; r ={ r }; n ={ n }; bM ={ - ln ( bM ) / C3 }; Time : { time . ctime () } ’)

271

272 if r % 10**10 == 0:

273 print ( f ’ Checkpoint ; r ={ r }; n ={ n }; Time : { time . ctime () } ’)

274 r += 1

275

276 print ( " End : " , time . ctime () )
 27
