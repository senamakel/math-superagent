<!-- source: https://arxiv.org/pdf/2002.03317 | converted from PDF -->

1

Reed-Muller Codes: Theory and Algorithms

Emmanuel Abbe Amir Shpilka Min Ye

Abstract

Reed-Muller (RM) codes are among the oldest, simplest and perhaps most ubiquitous family of codes.
They are used in many areas of coding theory in both electrical engineering and computer science. Yet,
many of their important properties are still under investigation. This paper covers some of the recent
developments regarding the weight enumerator and the capacity-achieving properties of RM codes, as
well as some of the algorithmic developments. In particular, the paper discusses the recent connections
established between RM codes, thresholds of Boolean functions, polarization theory, hypercontractivity,
and the techniques of approximating low weight codewords using lower degree polynomials (when
codewords are viewed as evaluation vectors of degree r polynomials in m variables). It then overviews
some of the algorithms for decoding RM codes. It covers both algorithms with provable performance
guarantees for every block length, as well as algorithms with state-of-the-art performances in practical
regimes, which do not perform as well for large block length. Finally, the paper concludes with a few
open problems.

E. Abbe is with the Mathematics Institute and the School of Computer and Communication Sciences at EPFL, Switzerland, and
the Program in Applied and Computational Mathematics and the Department of Electrical Engineering in Princeton University,
USA.
A. Shpilka is with the Blavatnik school of Computer Science at Tel Aviv University, Tel Aviv, Israel. Email: sh-
pilka@tauex.tau.ac.il.
M. Ye is with the Data Science and Information Technology Research Center, Tsinghua-Berkeley Shenzhen Institute, Tsinghua
Shenzhen International Graduate School, Shenzhen, China. Email: yeemmi@gmail.com
The ﬁrst and third authors were partly supported by the NSF CAREER Award CCF-1552131. The second author received
funding from the Israel Science Foundation (grant number 552/16) and from the Len Blavatnik and the Blavatnik Family
foundation.arXiv:2002.03317v2  [cs.IT]  10 Jun 2020
2

CONTENTS

I Introduction 3
I-A Outline . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4

II Deﬁnitions and basic properties 4
II-A Deﬁnition and parameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
II-B Recursive structure and distance . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
II-C Duality . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
II-D Afﬁne-invariance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
II-E General ﬁnite ﬁelds and locality . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
II-F Notations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8

III Weight enumerator 8
III-A Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
III-B Proof strategy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
III-B1 The ϵ-net approach for upper bounding the weight enumerator (Theo-
rems 2, 3, 4, 7, 8) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
III-B2 Connection to hypercontractivity . . . . . . . . . . . . . . . . . . . . . . 14
III-B3 Lower bounds on the weight enumerator . . . . . . . . . . . . . . . . . 15

IV Capacity results 15
IV-A RM codes achieve capacity at low rate [1], [2] . . . . . . . . . . . . . . . . . . . . 15
IV-A1 BEC . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
IV-A2 BSC . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
IV-B RM codes achieve capacity on the BEC at high rate [1] . . . . . . . . . . . . . . . 17
IV-C RM codes achieve capacity on the BEC at constant rate [3] . . . . . . . . . . . . . 18
IV-D RM codes polarize and Twin-RM codes achieve capacity on any BMS [4] . . . . . 23

V Decoding algorithms 29
V-A Reed’s algorithm [5]: Unique decoding up to half the code distance . . . . . . . . . 30
V-B Practical algorithms for short to medium length RM codes . . . . . . . . . . . . . . 31
V-B1 Fast Hadamard Transform (FHT) for ﬁrst order RM codes [6], [7] . . . 31
V-B2 Sidel’nikov-Pershakov algorithm [8] and its variant [9] . . . . . . . . . . 32
V-B3 Dumer’s recursive list decoding [10]–[12] . . . . . . . . . . . . . . . . . 34
V-B4 Recursive projection aggregation decoding [13] . . . . . . . . . . . . . . 37
V-B5 Additional methods [14], [15] . . . . . . . . . . . . . . . . . . . . . . . 38
V-C Berlekamp-Welch type decoding algorithm [16] . . . . . . . . . . . . . . . . . . . . 39

VI Open problems 40
VI-A RM codes and Twin-RM codes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
VI-B Weight enumerator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
VI-C Algorithms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41

References 42

3

I. INTRODUCTION
A large variety of codes have been developed over the past 70 years. These were driven by various
objectives, in particular, achieving efﬁciently the Shannon capacity [17], constructing perfect or good
codes in the Hamming worst-case model [18], matching the performance of random codes, improving
the decoding complexity, the weight enumerator, the scaling law, the universality, the local properties of
the code [19]–[25], and more objectives in theoretical computer science such as in cryptography (e.g.,
secrete sharing, private information retrieval), pseudorandomness, extractors, hardness ampliﬁcation or
probabilistic proof systems; see [1] for references. Among this large variety of code developments, one
of the ﬁrst, simplest and perhaps most ubiquitous code is the Reed-Muller (RM) code.
The RM code was introduced by Muller in 1954 [26], and Reed developed shortly after a decoding
algorithm decoding up to half its minimum distance [5]. The code construction can be described with a
greedy procedure. Consider building a linear code (with block length a power of two); it must contain the
all-0 codeword. If one has to pick a second codeword, then the all-1 codeword is the best choice under
any meaningful criteria. If now one has to keep these two codewords, the next best choice to maximize
the code distance is the half-0 half-1 codeword, and to continue building a basis sequentially, one can
add a few more vectors that preserve a relative distance of half, completing the simplex code, which has
an optimal rate for the relative distance half. Once saturation is reached at relative distance half, it is less
clear how to pick the next codeword, but one can simply re-iterate the simplex construction on any of
the support of the previously picked vectors, and iterate this after each saturation, reducing each time the
distance by half. This gives the RM code, whose basis is equivalently deﬁned by the evaluation vectors
of bounded degree monomials.
As mentioned, the ﬁrst order RM code is the augmented simplex code or equivalently the Hadamard
code, and the simplex code is the dual of the Hamming code that is ‘perfect’. This strong property is
clearly lost once the RM code order gets higher, but RM codes preserve nonetheless a decent distance (at
root block length for constant rate). Of course this does not give a ‘good’ code (i.e., a code with constant
rate and constant relative distance), and it is far from achieving the distance that other combinatorial
codes can reach, such as Golay codes, BCH codes or expander codes [19]. However, once put under the
light of random errors, i.e., the Shannon setting, for which the minimum distance is no longer the right
ﬁgure or merit, RM codes may perform well again. In [27], Levenshtein and co-authors show that for
the binary symmetric channel, there are codes that improve on the simplex code in terms of the error
probability (with matching length and dimension). Nonetheless, in the lens of Shannon capacity, RM
codes seem to perform very well. In fact, more than well; it is plausible that they achieve the Shannon
capacity on any Binary-input Memoryless Symmetric (BMS) channel [1], [3], [4], [28], [29] and perform
comparably to random codes on criteria such as the scaling law [30] or the weight enumerator [19],
[31]–[35].
The fact that RM codes have good performance in the Shannon setting, and that they seem to achieve
capacity, has long been observed and conjectured. It is hard to track back the ﬁrst appearance of this
belief in the literature, but [3] reports that it was likely already present in the late 60s. The claim was
mentioned explicitly in a 1993 talk by Shu Lin, entitled ?RM Codes are Not So Bad? [36]. It appears
that a 1994 paper by Dumer and Farrell contains the earliest printed discussion on this matter [37]. Since
then, the topic has become increasingly prevalent
1 [1], [15], [28], [38]–[41].
But the research activity has truly sparked in the recent years, with the emergence of polar codes [38].
Polar codes are the close cousins of RM codes. They are derived from the same square matrix but with a
different row selection. The more sophisticated and channel dependent construction of polar codes gives
them the advantage of being provably capacity-achieving on any BMS channel, due to the polarization
phenomenon. Even more impressive is the fact that they possess an efﬁcient decoding algorithm down
to the capacity.

1The capacity conjecture for the BEC at constant rate was posed as one of the open problems at the Information Theory
Semester at the Simons Institute, Berkeley, in 2015.
 4

Shortly after the polar code breakthrough, and given the close relationship between polar and RM codes,
the hope that RM codes could also be proved to achieve capacity on any BMS started to propagate, both
in the electrical engineering and computer science communities. A ﬁrst conﬁrmation of this was obtained
in extremal regimes of the BEC and BSC [1], exploiting new bounds on the weight enumerator [34], and
a ﬁrst complete proof for the BEC at constant rate was ﬁnally obtained in [29]. These however did not
exploit the close connection between RM and polar codes, recently investigated in [4], showing that the
RM transform is also polarizing and that a third variant of the RM code achieves capacity on any BMS
with the conjecture that this variant is indeed the RM code itself. Nonetheless, the general conjecture
that RM codes achieve capacity on any BMS channel remains open.
Polar codes and RM codes can be compared in different ways. In most performance metrics, and putting
aside the decoding complexity, RM codes seem to be superior to polar codes [4], [15]. Namely, they
seem to achieve capacity universally and with an optimal scaling-law, while polar codes have a channel-
dependent construction with a suboptimal scaling-law [30], [42]. However, RM codes seem more complex
both in terms of obtaining performance guarantees (as evidenced by the long standing conjectures) and
in terms of their decoding complexity.
The efﬁcient decoding of RM codes is the second main challenge regarding RM codes. Many algorithms
have been propose since Reed’s algorithm [5], such as [6]–[12], and newer ones have appeared in the
post polar code period [13], [14], [16]. Some of these already show that at various block-lengths and
rates that are relevant for communication applications, RM codes are indeed competing or even superior
to polar codes [13], [15], even compared to the improved versions considered for 5G [43].
This survey is meant to overview these recent developments regarding both the performance guarantees
(in particular on weight enumerator and capacity) and the decoding algorithms for RM codes.

A. Outline
The organization of this survey is as follows. We start in Section II with the main deﬁnitions and basic
properties of RM codes (their recursive structure, distance, duality, symmetry group and local properties).
We then cover the bounds on their weight enumerator in Section III. In Section IV, we cover results
tackling the capacity achievability, using results on weight enumerator, thresholds of monontone Boolean
functions and connections to polarization theory. We then cover various decoding algorithms in Section
V, providing pseudo-codes for them, and conclude in SectionVI with a selection of open problems.

II. DEFINITIONS AND BASIC PROPERTIES
A. Deﬁnition and parameters
Codewords of binary Reed-Muller codes consist of the evaluation vectors of multivariate polynomials
over the binary ﬁeld F2. The encoding procedure of RM codes maps the information bits stored in the poly-
nomial coefﬁcients to the polynomial evaluation vector. Consider the polynomial ring F2[x1, x2, . . . , xm]
with m variables. For a polynomial f ∈ F2[x1, x2, . . . , xm] and a binary vector z = (z1, z2, . . . , zm) ∈
Fm
2 , let Evalz(f ) := f (z1, z2, . . . , zm) be the evaluation of f at the vector z, and let Eval(f ) :=
(Evalz(f ) : z ∈ Fm
2 ) be the evaluation vector of f whose coordinates are the evaluations of f at all
2m vectors in Fm
2 . Reed-Muller codes with parameters m and r consist of all the evaluation vectors of
polynomials with m variables and degree no larger than r.

Deﬁnition 1. The r-th order (binary) Reed-Muller code RM(m, r) code is deﬁned as the following set
of binary vectors
 RM(m, r) := {Eval(f ) : f ∈ F2[x1, x2, . . . , xm], deg(f ) ≤ r} .

Note that in later sections, we might use Eval(f ) and f interchangeably to denote the codeword of
RM codes. For a subset A ⊆ [m] := {1, 2, . . . , m}, we use the shorthand notation xA := ∏i∈A xi. Notice
that we always have xn = x in F2 for any integer n ≥ 1, so we only need to consider the polynomials

5

in which the degree of each xi is no larger than 1. All such polynomials with degree no larger than r
are linear combinations of the following set of monomials

{xA : A ⊆ [m], |A| ≤ r}.

There are ∑r
i=0 (m
i ) such monomials, and the encoding procedure of RM(m, r) maps the coefﬁcients of
these monomials to their corresponding evaluation vectors. Therefore, RM(m, r) is a linear code with
code length n = 2m and code dimension ∑r
i=0 (m
i ). Moreover, the evaluation vectors {Eval(xA) : A ⊆
[m], |A| ≤ r} form a generator matrix of RM(m, r). Here we give a few examples of generator matrices
for RM codes with code length 8:

RM(3, 0) : [
Eval(1)] = [
1 1 1 1 1 1 1 1] RM(3, 1) :
 




Eval(x1)
Eval(x2)
Eval(x3)
Eval(1)
 


 =
 




1 1 1 1 0 0 0 0
1 1 0 0 1 1 0 0
1 0 1 0 1 0 1 0
1 1 1 1 1 1 1 1





RM(3, 2) :
 










Eval(x1x2)
Eval(x1x3)
Eval(x2x3)
Eval(x1)
Eval(x2)
Eval(x3)
Eval(1)
 









 =
 










1 1 0 0 0 0 0 0
1 0 1 0 0 0 0 0
1 0 0 0 1 0 0 0
1 1 1 1 0 0 0 0
1 1 0 0 1 1 0 0
1 0 1 0 1 0 1 0
1 1 1 1 1 1 1 1










 RM(3, 3) :
 












Eval(x1x2x3)
Eval(x1x2)
Eval(x1x3)
Eval(x2x3)
Eval(x1)
Eval(x2)
Eval(x3)
Eval(1)
 











 =
 












1 0 0 0 0 0 0 0
1 1 0 0 0 0 0 0
1 0 1 0 0 0 0 0
1 0 0 0 1 0 0 0
1 1 1 1 0 0 0 0
1 1 0 0 1 1 0 0
1 0 1 0 1 0 1 0
1 1 1 1 1 1 1 1













From this example, we can see that RM(m, 0) is the repetition code, and RM(m, m) consists of all the
binary vectors of length n = 2m, i.e., the evaluation vectors {Eval(xA) : A ⊆ [m]} form a basis of Fn
2 .
Another equivalent way of deﬁning RM codes is the Plotkin (u, u + v) construction, which we discuss
in detail below in Section II-B. We also note that RM codes can be deﬁned as geometry codes and refer
to [19], [44] for further details.

B. Recursive structure and distance
For any polynomial f ∈ F2[x1, x2, . . . , xm], we can always decompose it into two parts, one part
containing xm and the other not containing xm:

f (x1, x2, . . . , xm) = g(x1, x2, . . . , xm−1) + xmh(x1, x2, . . . , xm−1). (1)

Here we use the fact that xn
m = xm in F2 for any integer n ≥ 1.
We can also decompose the evaluation vector Eval(f ) into two subvectors, one subvector consisting
of the evaluations of f at all z = (z1, . . . , zm)’s with zm = 0 and the other subvector consisting of the
evaluations of f at all z = (z1, . . . , zm)’s with zm = 1. We denote the ﬁrst subvector as Eval[zm=0](f ) and
the second one as Eval[zm=1](f ). We also deﬁne their sum over F2 as Eval[/zm](f ) := Eval
[zm=0](f ) +
Eval[zm=1](f ). Note that all three vectors Eval[zm=0](f ), Eval[zm=1](f ) and Eval[/zm](f ) have length
2m−1, and their coordinates are indexed by (z1, z2, . . . , zm−1) ∈ Fm−1
2 .
By (1), Eval[zm=0](f ) is the evaluation vector of g(x1, x2, . . . , xm−1), and Eval[/zm](f ) is the evaluation
vector of h(x1, x2, . . . , xm−1). Now assume that Eval(f ) ∈ RM(m, r), or equivalently, assume that
deg(f ) ≤ r. Then we have deg(g) ≤ r and deg(h) ≤ r − 1. Therefore, Eval[zm=0](f ) ∈ RM(m − 1, r)
and Eval[/zm](f ) ∈ RM(m − 1, r − 1). This is called the Plotkin (u, u + v) construction of RM codes,
meaning that if we take a codeword c ∈ RM(m, r), then we can always divide its coordinates into
two subvectors u and u + v of length 2m−1, where u ∈ RM(m − 1, r), v ∈ RM(m − 1, r − 1) and
c = (u, u + v).
A consequence of this recursive structure is that the code distance of RM(m, r) is d = 2m−r. We
prove this by induction. It is easy to establish the induction basis. For the inductive step, suppose that
the claim holds for m − 1 and all r ≤ m − 1; then we only need to show that the Hamming weight of

6

code code length code dimension code distance dual code
RM(m, r) n = 2
m k = ∑r
i=0 (
m
i ) d = 2
m−r RM(m, m − r − 1)

TABLE I: Important parameters of RM(m, r).

the vector (u, u + v) is at least 2m−r for any u ∈ RM(m − 1, r) and v ∈ RM(m − 1, r − 1), i.e., we
only need to show that w(u) + w(u + v) ≥ 2m−r, where w(·) is the Hamming weight of a vector. Since
w(u + v) ≥ w(v) − w(u), we have w(u) + w(u + v) ≥ w(v). By the inductive hypothesis, w(v) ≥ 2m−r,
so w(u) + w(u + v) ≥ 2m−r. This completes the proof of the code distance.
The Plotkin construction also implies a recursive relation between the generator matrices of RM codes.
More precisely, let G(m − 1, r − 1) be a generator matrix of RM(m − 1, r − 1) and let G(m − 1, r) be a
generator matrix of RM(m − 1, r). Then we can obtain a generator matrix G(m, r) of RM(m, r) using
the following relation:
 G(m, r) = [
G(m − 1, r) G(m − 1, r)
0 G(m − 1, r − 1)

] ,

where 0 denotes the all-zero matrix with the same size as G(m − 1, r − 1).

C. Duality
The dual code of a binary linear code C ⊆ Fn
2 is deﬁned as
2

C⊥ := {x ∈ Fn
2 : ⟨x, c⟩ = 0 ∀c ∈ C}, where ⟨x, c⟩ =
 n∑

i=1 xici.

By deﬁnition, the dual code C⊥ is also a linear code, and we have

dim(C) + dim(C⊥) = n. (2)

Next we will show that the dual code of RM(m, r) is RM(m, m − r − 1). First, observe that the
Hamming weight of every codeword in RM(m, m − 1) is even, i.e., for every f ∈ F2[x1, . . . , xm] with
deg(f ) ≤ m − 1, we have ∑
z∈Fm
2 Evalz(f ) = 0, where the summation is over F2. This is because the
Hamming weight of Eval(xA) is 2m−|A|, so ∑
z Evalz∈F
m
2 (xA) = 0 for all subsets A with size |A| ≤
m−1. For every f ∈ F2[x1, . . . , xm] with deg(f ) ≤ m−1, we can write it as f = ∑
A⊂[m],|A|≤m−1 uAxA.
Therefore,
∑

z∈Fm
2 Evalz(f ) = ∑

z∈Fm
2 Evalz( ∑

A⊂[m],|A|≤m−1 uAxA) = ∑

A⊂[m],|A|≤m−1
 (uA ∑

z∈Fm
2 Evalz(xA)
) = 0.

Suppose that Eval(f ) is a codeword of RM(m, r) and Eval(g) is a codeword of RM(m, m−r−1). Then
deg(f ) ≤ r and deg(g) ≤ m − r − 1. Notice that ⟨Eval(f ), Eval(g)⟩ = ∑
z∈Fm
2 Evalz(f ) Evalz(g) =∑
z∈Fm
2 Evalz(f g). Since deg(f g) ≤ m − 1, we have ⟨Eval(f ), Eval(g)⟩ = ∑
z∈Fm
2 Evalz(f g) = 0.
Therefore, every codeword of RM(m, m−r −1) belongs to the dual code of RM(m, r), i.e., RM(m, m−
r − 1) ⊆ RM(m, r)⊥.
Since
 dim(RM(m, m − r − 1)) =
 m−r−1∑

i=0
 (m
i
 ) =
 m−r−1∑

i=0
 ( m
m − i
) =
 m∑

i=r+1
 (m
i
 ),

we have

dim(RM(m, r)) + dim(RM(m, m − r − 1)) =
 r∑

i=0
 (m
i
 ) +
 m∑

i=r+1
 (m
i
 ) =
 m∑

i=0
 (m
i
 ) = 2
m = n.

2As we work over F2 all calculations are done in that ﬁeld.
 7

Combining this with (2), we know that dim(RM(m, m − r − 1)) = dim(RM(m, r)⊥). Thus we conclude
that RM(m, m − r − 1) = RM(m, r)⊥.

This in particular tells us that the parity check matrix of RM(m, r) is the generator matrix of RM(m, m−
r − 1). The important parameters of RM(m, r) are summarized in Table I.

D. Afﬁne-invariance
The automorphism group of a code C is the set of permutations under which C remains invariant. More
precisely, the automorphism group of a code C with code length n is deﬁned as A(C) := {π ∈ Sn :
π(C) = C}, where π(C) := {π(c) : c ∈ C}, and π(c) is vector obtained from permuting the coordinates
of c according to π. It is easy to verify that A(C) is always a subgroup of the symmetric group Sn.
RM codes are afﬁne-invariant in the sense that A(RM(m, r)) contains a subgroup isomorphic to the
afﬁne linear group. More speciﬁcally, since the codewords of RM codes are evaluation vectors and they
are indexed by the vectors z ∈ Fm
2 , the afﬁne linear transform gA,b : z ↦→ Az + b gives a permutation on
the coordinates of the codeword when A is an m × m invertible matrix over F2 and b ∈ Fm
2 . Next we
show that such a permutation indeed belongs to A(RM(m, r)). For any codeword c ∈ RM(m, r), there is
a polynomial f ∈ F2[x1, . . . , xm] with deg(f ) ≤ r such that c = Eval(f ). Since gA,b(c) = Eval(f ◦ gA,b)
and deg(f ◦ gA,b) = deg(f ) ≤ r, we have gA,b(c) ∈ RM(m, r). Therefore, gA,b ∈ A(RM(m, r)), and
RM codes are afﬁne-invariant.
Recall that in Section II-B we showed that Eval[/zm](f ) ∈ RM(m − 1, r − 1) if Eval(f ) ∈ RM(m, r).
Using the afﬁne-invariant property, we can replace zm in this statement with any linear combination
of z1, . . . , zm. More speciﬁcally, for any ℓ = b1z1 + · · · + bmzm with nonzero coefﬁcient vector b =
(b1, . . . , bm) ̸= 0, we deﬁne Eval[ℓ=0](f ), Eval[ℓ=1](f ), Eval[/ℓ](f ) in the same way as Eval[zm=0](f ), Eval[zm=1](f ),
Eval[/zm](f ). For any such ℓ, one can always ﬁnd an afﬁne linear transform mapping zm to ℓ. Since RM
codes are invariant under such afﬁne transforms, we have Eval[/ℓ](f ) ∈ RM(m − 1, r − 1) whenever
Eval(f ) ∈ RM(m, r). This observation will be used in several decoding algorithms in Section V.

E. General ﬁnite ﬁelds and locality
The deﬁnition of binary RM codes above can be naturally extended to more general ﬁnite ﬁelds
Fq. Let us consider the polynomial ring Fq[x1, x2, . . . , xm] of m variables. For a polynomial f ∈
Fq[x1, x2, . . . , xm], we again use Eval(f ) := (Evalz(f ) : z ∈ Fm
q ) to denote the evaluation vector
of f . Since xq = x in Fq, we only need to consider the polynomials in which the degree of each xi is
no larger than q − 1, and the degree of such polynomials is no larger than m(q − 1).

Deﬁnition 2. Let n := qm and r ≤ m(q − 1). The r-th order q-ary Reed-Muller code RMq(m, r) code
is deﬁned as the following set of vectors in Fn
q :

RMq(m, r) := {Eval(f ) : f ∈ Fq[x1, x2, . . . , xm], deg(f ) ≤ r}.

A locally decodable code (LDC) is an error-correcting code that allows a single bit of the original
message to be decoded with high probability by only examining (or querying) a small number of bits of
a possibly corrupted codeword. RM codes over large ﬁnite ﬁelds are the oldest and most basic family of
LDC. When RM codes are used as LDC, the order r of RM codes is typically set to be smaller than the
ﬁeld size q. At a high level, local decoding of RM codes requires us to efﬁciently correct the evaluation
of a multivariate polynomial at a given point z from the evaluation of the same polynomial at a small
number of other points. The decoding algorithm chooses a set of points on an afﬁne line that passes
through z. It then queries the codeword for the evaluation of the polynomial on the points in this set and
interpolates that polynomial to obtain the evaluation at z. We refer the readers to [25] for more details
on this topic.
 8

F. Notations
We summarize here a few notations and parameters used in the paper. We use n = 2m to denote the
code length (or blocklength) and k = ∑r
i=0 (m
i ) to denote the code dimension of RM codes. We use 1[·]
for the indicator function. We also use the notation W : X → Y to denote a communication channel
that maps input random variable X to output random variable Y , with the channel transition probability
W (y|x) = P(Y = y|X = x). We use | · | to denote the Hamming weight of a binary vector, i.e., the
number of 1’s in this vector, and we use wt(·) to denote its relative Hamming weight, i.e., Hamming
weight divided by the length of the vector. We use hz(·) to denote the extrinsic information transfer
(EXIT) function and H2(x) := −x log2(x) − (1 − x) log2(1 − x) to denote the binary entropy function.
Finally, in Section V, if two vectors belong to Fm
2 , then by default their sum is over F2 unless mentioned
otherwise.
 III. WEIGHT ENUMERATOR
In this section we survey known results on the weight distribution of binary Reed-Muller codes. We
ﬁrst give the basic deﬁnition and discuss known results, then we explain the ideas of the proofs of some
of the main results. In Section IV-A, we explain how these results can be used to prove that Reed-Muller
codes achieve capacity for the BEC and the BSC for a certain range of parameters.

The weight enumerator of a code measures how many codewords of a given weight are there in the
code.

Deﬁnition 3 (Weight, Bias, Weight enumerator). For a codeword f we denote its hamming weight
by |f | = |{z ∈ Fm
2 | f (z) = 1}|, and its relative weight, which we refer to simply as weight, with
wt(f ) = |f |/2m = EZ[f (Z)] = PZ[f (Z) = 1] where Z is drawn uniformly at random in Fm
2 . When
no distribution is mentioned, we draw the underlying random variable, in this case Z, according to the
uniform distribution. We also denote the bias of a codeword by bias(f ) = EZ[(−1)f (Z)]. For β ∈ [0, 1] we
deﬁne Am,r (β) ≜ |{f ∈ RM(m, r) | wt(f ) = β}| and Am,r (≤ β) ≜ |{f ∈ RM(m, r) | wt(f ) ≤ β}|.

Thus, Am,r (≤ β) counts the number of codewords of (relative) weight at most β. In particular, for
β < 2−r, Am,r (≤ β) = 1. The weight enumerator is one of the most useful measures for proving that
a code achieves capacity as there are formulas that relate the distribution of weights in a code to the
probability of correcting random erasures or random errors (see Section IV-A). Intuitively, if the weight
enumerator behaves similarly to that of a random code then we can expect the code to achieve capacity
in a similar manner to random codes. Clearly, RM codes are quite different than random codes. In
particular, for a random code we expect that besides the zero codeword, every other codeword will have
weight roughly (1/2 ± ϵ) (where ϵ is a constant depending on the rate), whereas RM codes contain many
codewords of small weight. Nevertheless, as we shall see, if one can show that the weight enumerator
drops quickly for β < 1/2 then this may be sufﬁcient for proving that the code achieves capacity.
Thus, proving strong upper bound on the weight enumerator for weights slightly smaller than 1/2 is an
interesting and in some cases also a fruitful approach to proving that RM codes achieve capacity.

A. Results
Computing the weight enumerator of RM codes is a well known problem that is open in most ranges
of parameters. In 1970 Kasami and Tokura [32] characterized all codewords of weight less than twice
the minimum distance. This was later improved in [33] to all codewords of weight less than 2.5 times
the minimal distance. For degrees larger than 3 they obtained the following result.

Theorem 1 (Theorem 1 of [33]). If r ≥ 3 and f ∈ RM(m, r) satisﬁes wt(f ) < 2.5 · 2−r then, up to an
invertible linear transformation,

f = x1g(x3, . . . , xm) + x2h(x3, . . . , xm) + x1x2k(x3, . . . , xm) ,
 9

where deg(g) = deg(h) = r − 1 and deg(k) = r − 2.

By counting the number of such representations one can get a good estimate on the number of
codewords of such weight.
No signiﬁcant progress was then made for over thirty years until the work of Kaufman, Lovett and
Porat [34] gave, for any constant degree r = O(1), asymptotically tight bounds on the weight enumerator
of RM codes of degree r.

Theorem 2 (Theorem 3.1 of [34]). Let 1 ≤ ℓ ≤ r − 1 and 0 < ϵ ≤ 1/2. It holds that

(1/ϵ)
cr·mr−ℓ ≤ Am,r (
≤ (1 − ϵ)2
−ℓ) ≤ (1/ϵ)
Cr·mr−ℓ ,

where cr, Cr > 0 are constants that depend only on r.

Note that the relative weight of a codeword in RM(m, r) is between 2−r and 1, hence we consider only
1 ≤ ℓ ≤ r − 1 in the statement of the theorem. Unfortunately, as the degree gets larger, the estimate in
Theorem 2 becomes less and less tight. Building on the techniques of [34], Abbe, Shpilka and Wigderson
[1] managed to get better bounds for degrees up to m/4, which they used to show that RM codes achieve
capacity for the BEC and the BSC for degrees r = o(m).

Theorem 3 (Theorem 3.3 of [1]). Let 1 ≤ ℓ ≤ r − 1 < m/4 and 0 < ϵ ≤ 1/2. Then,3

Am,r (≤ (1 − ϵ)2
−ℓ) ≤ (1/ϵ)
O(
ℓ
4( m−ℓ
≤r−ℓ)
) .

Sberlo and Shpilka [2] polished the techniques of [1] and managed to obtain good estimates for every
degree.

Theorem 4 (Theorem 1.2 of [2]). Let γ = r/m. Then, for every integer ℓ,

Am,r (≤ 2−ℓ) ≤ 2
(
O(m4)+17(cγ ℓ+dγ )γℓ−1( m
≤r)) ,

where cγ = 1
1−γ and dγ = 2−γ
(1−γ)2 .

To better understand the upper bound, note that the leading term in the exponent is O (ℓγℓ−1( m
≤r))

(when 0 < γ < 1 is a constant) whereas, if we were to state Theorem 3 in the same way, then its leading
term would be O (ℓ4γℓ−1( m
≤r)).
Recently, Samorodnitsky [35] proved a remarkable general result regarding the weight enumerator of
codes that either they or their dual code achieve capacity for the BEC. His techniques are completely
different than the techniques of [1], [2], [34].

Theorem 5 (Proposition 1.6 in [35]). Let C ⊆ {0, 1}n a linear code of rate R. Let (a0, . . . , an) be the
distribution of hamming weights
4 in C. For 0 ≤ k ≤ n, let k∗ = min{k, n − k}. Let θ = R2 ln 2.
1) If C⊥ achieves capacity on the BEC then for all 0 ≤ k ≤ n

ak ≤ 2o(n) · ( 1
1 − R
 )k∗·2 ln 2 .

2) If C achieves capacity on the BEC then for all 0 ≤ k ≤ n

ak ≤ 2
o(n) ·
 { |C|
(1−θ)k∗ (1+θ)n−k∗ 0 ≤ k∗ ≤ 1−θ
2 · n

|C| · ( n
k∗)
2n otherwise

3We use the notation ( n
≤k) ≜ ∑k
i=0 (
n
i )
.
4I.e., there are exactly ai codewords whose hamming weight is exactly i in C.
 10

Observe that Item 2 in Theorem 5 says that for k/n ∈ [ 1
2 ±R2 ln 2], the weight distribution of a capacity
achieving code is (up to the 2o(n) term) the same as that of a random code.
As Kudekar et al. [29] proved that all codes with parameters RM(m, m/2 ± O(√m)) achieve capacity
for the BEC, Theorem 5 gives strong upper bound on the weight enumerator of RM codes for linear
weights, some are as tight as possible.
On the other hand, for hamming weight k = o(n), the theorem fails to give meaningful bounds as the
2o(n) term becomes too large to ignore and in fact, it dominates the entire estimate, and in particular
it is a weaker bound than the one given in Theorem 4. In addition, when the rate R approaches zero
(e.g. when r < (1/2 − ϵ)m) Theorem 5 does not give a meaningful estimate, again due to the 2o(n)

term, whereas Theorem 4 works for such degrees as well. Thus, Theorem 5 gives very strong bounds
for constant rate and constant relative weight, while Theorem 4 gives better bounds for small weight or
small rate.
So far we mostly discussed results on the weight distribution for weights that are a constant factor
smaller than 1/2. However, one expects that a random codeword will have weight roughly 1/2. Thus,
an interesting question to understand is the concentration of the weight, in particular it is interesting to
know how many codewords have weight smaller than (1 − ϵ)/2 for small ϵ, or, in terms of bias, how
many codewords have bias at least ϵ. To the best of our knowledge, for other range of parameters, the
ﬁrst such result was obtained by Ben Eliezer, Hod and Lovett [45] who proved the following.

Theorem 6 (Lemma 2 in [45]). Let m, r ∈ N and δ > 0 such that r ≤ (1 − δ)m. Then there exist
positive constants c1, c2 (which depend solely on δ) such that,

Am,r
 (≤ 1 − 2
−c1 m
r
2
 ) ≤ 2
(
(1−c2)( m
≤r)) ,

where the probability is over a uniformly random polynomial with m variables and degree ≤ r.

This result was later extended to other prime ﬁelds in [46]. Note that for RM codes of constant rate,
Theorem 5 gives much sharper estimates, but it does not extend to other ranges of parameters.
Observe that when the degree r is linear in m Theorem 6 only applies to weights that are some constant
smaller than 1/2 and does not give information about the number of polynomials that have bias o(1).
Such a result was obtained by Sberlo and Shpilka [2], and it played an important role in their results on
the capacity of RM codes. They ﬁrst proved a result for the case that r < m/2 and then for the general
case (with a weaker bound).

Theorem 7 (Theorem 1.4 of [2]). Let ℓ, m ∈ N and let 0 < γ(m) < 1/2 − Ω (√ log m
m
 ) be a parameter

(which may be constant or depend on m) such that ℓ+log 1
1−2γ
(1−2γ)2 = o(m). Then,

Am,γm
 (≤ 1 − 2−ℓ

2
 ) ≤ 2

(
O(m4)+(1−2
−c(γ,ℓ))( m
≤r)
) ,

where c(γ, ℓ) = O ( γ2ℓ+γ log(1/1−2γ)
1−2γ + γ).

As the form of the bound is a bit complicated, the following remark was made in [2].

Remark 1. To make better sense of the parameters in the theorem we note the following.

• When γ < 1/2 is a constant, c(γ, ℓ) = O(ℓ).

• The bound is meaningful up to degrees ( 1
2 − Ω ( √log m√m
 )) m, but falls short of working for constant
rate RM codes.

• For γ which is a constant the upper bound is applicable to ℓ = o(m) (in fact it is possible to push
it all the way to some ℓ = Ω(m)). For γ approaching 1/2, i.e γ = 1/2 − o(1), there is a trade-off
between how small the o(1) is and the largest ℓ for which the bound is applicable to. Nevertheless,

11

even if γ = 1/2 − Ω (√ log m
m
 ) the lemma still holds for ℓ = Ω(log m) (i.e, for a polynomially

small bias).

We see that for linear degrees (r = Ω(m)) Theorem 6 gives a bound on the number of polynomials
(or codewords) that have at least some constant bias, whereas Theorem 7 holds for a wider range of
parameters and in particular can handle bias which is nearly exponentially small in m. For general
degrees, Sberlo and Shpilka obtained the following result.

Theorem 8 (Theorem 1.7 of [2]). Let r ≤ m ∈ N and ϵ > 0. Then,

Am,r
 (≤ 1 − ϵ
2
 ) ≤ exp (− 2rϵ2

2
 ) · 2( m
≤r) .

Observe that the main difference between Theorem 6 and Theorem 8 is that in Theorem 6 the bias
(ϵ = 2−c1m/r) is directly linked to the degree. In particular, for every ϵ Theorem 6 allows for polynomials
of degree r = O(m/ log(1/ϵ)) whereas Theorem 8 allows for r and ϵ to be arbitrary. When r =
O(m/ log(1/ϵ)) the bound in Theorem 6 is stronger than the one given in Theorem 8. However, when
ϵ = o(1) (as a function of m) then the result of Theorem 6 is meaningful only for r = o(m) whereas
Theorem 8 gives strong bounds for polynomials of every degree.
To complete the picture we state two lower bounds on the weight enumerator. The ﬁrst is a fairly
straightforward observation.

Observation 1. 1
2 · 2( m−ℓ+1
≤r−ℓ+1) ≤ Am,r (≤ 2
−ℓ) .

Comparing to Theorem 4 and Theorem 5, we see that for ℓ = O(1) the lower bound in Observation 1
is roughly of the form 1
2 2
(r/m)
ℓ−1·( m
≤r). Thus, for r = m/2 it is similar to what Theorem 5 gives, except
that it has a smaller constant in the exponent: 2 versus 4 ln 2. For r = γm it gives a much smaller
constant in the exponent compared to Theorem 4: 2 versus 17(cγℓ + dγ). The main difference is for
very small weights, say ℓ = (1 − ϵ)r. Then, the estimate in Observation 1 is much smaller than what
Theorem 4 gives. This is mainly due to the fact that Theorem 4 heavily relies on estimates of binomial
coefﬁcients that become less and less good as (r − ℓ) → 0.
The second lower bounds was given in [2] and it concerns weights around 1/2.

Theorem 9 (Theorem 1.8 of [2]). Let 20 ≤ r ≤ m ∈ N. Then for any integer ℓ < r/3 and sufﬁciently
large m it holds that 1
2 · 2
(∑ℓ−1
j=1 ( m−j
≤r−1)
) ≤ Am,r
 (≤ 1 − 2−ℓ

2
 ) .

Comparing the upper bound in Theorem 7 to Theorem 9 we see that there is a gap between the
two bounds. Roughly, the lower bound on the number of polynomials that have bias at least ϵ matches
the upper bound corresponding to bias at least √ϵ. This may be a bit difﬁcult to see when looking at
Theorem 4 but we refer to Remark 3.16 in [2] for a qualitative comparison.

B. Proof strategy
In this section we explain the basic ideas behind the proofs of the theorems stated in Section III-A.
The most common proof strategy is based on the approach of Kaufman et al. [34], which, following [2],
we call the ϵ-net approach. Theorem 5 is proved using a completely different approach.
 12

1) The ϵ-net approach for upper bounding the weight enumerator (Theorems 2, 3, 4, 7, 8): The
main idea in the work of [34], which was later reﬁned in [1] and [2], is that in order to upper bound
the number of polynomials of certain weight we should ﬁnd a relatively small set, in the space of all
functions Fm
2 → F2, such that all low weight polynomials are contained in balls of (relative) radius at
most ϵ around the elements of the set, with respect to the hamming distance. We call such a set an ϵ-net
for RM(m, r).
Why is this approach useful? Assuming we have found such a net, we can upper bound the number
of low weight codewords by the number of codewords in each ball times the size of the net. The crux of
the argument is to note that the number of codewords in each ball is upper bounded by Am,r (2ϵ). This
gives rise to a recursive approach whose base case is when the radius of the ball is smaller than half the
minimum distance (and then there is at most one codeword in the ball). Formally, this idea is captured
by the next simple claim.

Lemma 1. Let S ⊆ RM(m, r) be a subset of polynomials with an ϵ-net N . Then,

|S| ≤ |N | · Am,r (2ϵ) .

Thus, to get strong upper bounds on the number of low weight/bias polynomials we would like the
ϵ-net to be as effective as possible. This means that on the one hand we would like the ϵ-net to be small
and on the other hand that no ball around an element of the net should contain too many codewords.
Before explaining how to get such an ϵ-net we ﬁrst explain how this approach was developed in the
papers [34],[1],[2]. To prove Theorem 2 Kaufman et al. [34] constructed an ϵ-net such that each ball
contains at most one low weight polynomial. To achieve this they picked ϵ = 2−r−1. However, since
they insisted on having at most one low weight polynomial in every ball, this resulted in a relatively
large net. To prove Theorem 3, Abbe et al. observed that one can bound the number of codewords in
each ball using the weight enumerator at smaller weights. This allowed them to pick a larger ϵ and use
recursion. [1] used the same approach as [34] to construct the ϵ-net, though with different parameters
and with tighter analysis on the net size. [2] improved further on [1] by observing that the ϵ-net approach
was used only to bound the weight enumerator at weights which are somewhat smaller than 1/2. The
reason for that is that the calculations performed in [1], [34] were not tight enough and stopped working
as the weights got closer to 1/2 or as the degree got larger. Thus, [2] ﬁrst improved the calculations
upper bounding the size of the ϵ-net and then, using the improved calculations, obtained results for the
weight enumerator also for weights close to 1/2, and for all degrees, as stated in Theorems 4, 7 and 8.
We now explain the main idea of Kaufman et al. for constructing the ϵ-net. For this we will need the
notion of discrete derivative. The discrete derivative of a function f : Fm
2 → F2 at direction y ∈ Fm
2 is
the function ∆yf : x ↦→ ∆yf (x) ≜ f (x + y) + f (x) . (3)

It is not hard to see that if f is a degree r polynomial then, for every y, ∆yf has degree at most r − 1.
Another basic observation is that if a function f : Fm
2 → F2 has weight β, then, for each x,

PY [∆Y f (x) = f (x)] = 1 − β ,

where by Y we mean a random variable that is distributed uniformly over Fm
2 . Thus, if β < 1/2 then
∆yf (x) gives a good estimate for f (x). Hence, if we consider t directions y1, . . . , yt ∈ Fm
2 and deﬁne

Fy1,...,yt(x) ≜ Majority (∆y1f (x), . . . , ∆ytf (x))

then we get from the Chernoff-Hoeffding bound that

EX,Y1,...,Yt[1[FY1,...,Yt(X) ̸= f (X)]] ≈ exp(−t) .

Picking t = O(log 1/ϵ) we see that for each polynomial f ∈ RM(m, r) there is some Fy1,...,yt at hamming
distance at most ϵ. Thus, the set of all such Fy1,...,yt forms an ϵ-net for polynomials of weight at most β
in RM(m, r). All that is left to do is to count the number of such functions Fy1,...,yt to obtain a bound
on the size of our net.
 13

In fact, one can carry the same approach further and rather than approximating f by its ﬁrst order
derivatives, use instead higher order derivatives. For a set of k directions Y = {y1, . . . , yk} ∈ (Fm
2 )k we
deﬁne ∆Y f (x) = ∆yk∆yk−1 · · · ∆y1f (x) .

The following version of Lemma 2.2 of [34] appeared in [2].

Lemma 2. Let f : Fm
2 → F2 be a function such that wt(f ) ≤ 2−k for k ≥ 2 and let ϵ > 0. Then, there
exist directions Y1, . . . , Yt ∈ (Fm
2 )k−1 such that

PX [f (X) ̸= Majority (∆Y1f (X), . . . , ∆Ytf (X))] ≤ ϵ ,

where t = ⌈17 log(1/ϵ)⌉.

Denote
5
 FY1,...,Yt ≜ Majority (∆Y1f, . . . , ∆Ytf )

and Nk,t ≜ {
FY1,...,Yt : Y1, . . . , Yt ∈ (Fm
2 )
k , f ∈ RM(m, r) and wt(f ) ≤ 2−k−1} .

Combining Lemma 1 with recursive applications of Lemma 2, we obtain the following bound on the
weight enumerator.

Corollary 1. Let r, m, ℓ ∈ N such that r ≤ m. Then,

Am,r (
≤ 2
−ℓ) ≤ |Nℓ−1,t| · Am,r (2−ℓ−1) ,

where t = 17(ℓ + 2). Consequently,

Am,r (≤ 2
−ℓ) ≤
 r∏

j=ℓ
 ∣
∣Nj−1,17(j+2)∣
∣ .

The way that Kaufman et al. bounded the size of Nk,t was simply to say that each FY1,...,Yt is an
explicit function of t polynomials of degree r−k and hence the size of the net is at most |RM(m, r − k)|
t.
One idea in the improvement of [1] over [34] is that derivatives of polynomials can be represented as
polynomials in fewer variables. Speciﬁcally, one can think of ∆Y f as a polynomial deﬁned on the vector
space span(Y)⊥. This allows for some saving in the counting argument, namely,

|Nk,t| ≤ 2
mkt · |RM(m − k, r − k)|
t ,

where the term 2mkt comes from the fact that now we need to explicitly specify the sets Y1, . . . , Yt.
[2] further improved the upper bound by noting that different derivatives contain information about each
other. I.e., they share monomials. This allowed them to get a better control of the amount of information
encoded in the list of derivatives and as a result to obtain a better bound on the size of the net. This
proved signiﬁcant for bounding the number of codewords having small bias.
The discussion above relied on Lemma 2 that works for weights at most 1/4. For weights closer to
1/2 a similar approach is taken except that this time Kaufman et al. noted that one can pick a subspace
of dimension t and consider all 2t − 1 non-trivial ﬁrst order derivatives, according to directions in the
subspace, to obtain a good approximation for the polynomial. Since the directions according to which
we take derivatives are no longer independent they could no longer use the Chernoff-Hoeffding bound
in their argument. Instead they observed that the directions are 2-wise independent and could therefore
use the Chebyshev bound instead to bound t. Speciﬁcally, Lemma 2.4 of [34] as stated in [2] gives:

5Actually, we have to take a weighted majority, but for sake of clarity we ignore this detail in our presentation.
 14

Lemma 3 (Lemma 2.4 in [34]). Let f : Fn
2 → F2 be a function such that bias(f ) ≥ δ > 0 and let ϵ > 0.
Then, for t = ⌈log(1/ϵ) + 2 log(1/δ) + 1⌉, there exist directions y1, . . . , yt ∈ Fm
2 such that,

PX [f (X) = Majority (∆∑

i∈I yif (X) : ∅ ̸= I ⊆ [t]
)] ≥ 1 − ϵ .

Corollary 2. For any t ∈ N deﬁne,

Bt = {
Majority (
∆∑
i∈I yif (x) : ∅ ̸= I ⊆ [t]) : f ∈ RM(m, r) , y1, . . . , yt ∈ Fm
2 } .

Then, for t = ⌈log(1/ϵ) + 2 log(1/δ) + 1⌉, Bt is an ϵ-net for {f ∈ RM(m, r) : bias(f ) ≥ δ}.

To conclude, the ϵ-net approach works as follows. We ﬁrst show that each polynomial of weight at
most β can be approximated by an explicit function of some lower order derivatives. We then count the
number of such possible representations and then continue recursively to bound the number of codewords
that are close to each such function.

2) Connection to hypercontractivity: Samordnitsky proved Theorem 5 as a corollary of a more general
result concerning the behavior of Boolean functions under noise. We shall only give a high level
description of his approach.
For a Boolean function φ : {0, 1}n → R and a noise parameter η let us denote

φη(x) ≜ ∑

y∈{0,1}n ηdist(x,y)(1 − η)
n−dist(x,y)φ(y) ,

where dist (x, y) is the hamming distance between x and y. Thus, φη(x) averages the value of φ around
x according to the η-biased measure. As φη is a convex combination of many shifted copies of φ, it’s
ℓq norm cannot be larger than φ’s. Samordnitsky’s main theorem quantiﬁes that loss in norm. To state
his main result we shall need the following notation. For 0 ≤ λ ≤ 1, let T ∼ λ denote a random subset
T of {1, . . . , n} in which each element is chosen independently with probability λ. Let E(φ|T ) be the
conditional expectation of φ with respect to T , that is, E(φ|T )(x) ≜ EY :Y |T =x|T φ(Y ).

Theorem 10 (Theorem 1.1 of [35]). Let φ : {0, 1}n → R be non negative. Then, for any q > 1

log2 ∥φη∥q ≤ ET ∼λ log2 ∥E(φ|T )∥q ,

with λ = (1 − 2η)a(q), where
 a(q) =
 { 1
2 ln 2 2
3−q(2
q−1−1)
q−1 1 < q ≤ 2
1
2 ln 2 q
q−1 q ≤ 2 .

Results quantifying the decrease in norm due to noise are called hypercontractive inequalities, and
Samorodnitsky’s proof follows the proof of a hypercontractive inequality due to Gross [47]. As Samorod-
nitsky writes, the idea of the proof is to “view both sides of the corresponding inequality as functions
of η (for a ﬁxed q) and compare the derivatives. Since noise operators form a semigroup it sufﬁces to
compare the derivatives at zero, and this is done via an appropriate logarithmic Sobolev inequality.” While
Theorem 10 does not seem related to RM codes it turns out that if one takes φ to be the characteristic
function of the code then this gives a lot of information about the weight distribution of the code. For a
linear code C ⊆ {0, 1}n with generating matrix G, let φC = 2
n
|C| 1C. For T ⊆ {1, . . . , n} let rankC(T )
denote the rank of the submatrix of G generated by the rows whose indices are in T . The following is
a consequence of Theorem 10.

Theorem 11 (Proposition 1.3,1.4 of [35] specialized to q = 2). Let (a0, . . . , an) be the distribution of
hamming weights in C and (b0, . . . , bn) the distribution of hamming weights in C⊥. For 0 ≤ λ ≤ 1 let
η = 1−λln 2
2 . Then, for any such λ, and θ = λ2 ln 2, it holds that

λn − ET ∼λ rankC ⊥(T ) ≥ log2 (E[φC 2
η]
) = log2
 ( n∑

i=0 biλ
2i·ln 2)
 15

= log2
 ( 1
|C| ·
 n∑

k=0 ak(1 − θ)
k(1 + θ)n−k)
 .

Samordnitsky then observed that if C⊥ achieves capacity for the BEC then for λ = Rate(C⊥) + o(1) it
holds that λn−ET ∼λ rankC ⊥(T ) = o(n). Similar result follows if C achieves capacity, for the appropriate
λ. Combining this with Theorem 11 he obtained his main result on the weight enumerator of codes that
either they or their duals achieve capacity.

3) Lower bounds on the weight enumerator: The proofs of both Observation 1 and Theorem 9 are
based on exhibiting a large set of polynomials having the claimed weight.
Observation 1 follows from the simple fact that for a random polynomial g(xℓ, . . . , xn), of degree
r − ℓ + 1, the degree r polynomial f (x1, . . . , xn) = x1 · x2 · · · xℓ−1 · g will have weight at most 2−ℓ with
probability 1/2 (as half of the polynomials g have weight at most 1/2).
To prove Theorem 9 we consider all polynomials of the form

g(x1, . . . , xm) =
 ℓ∑

i=1 xifi(xi+1, . . . , xm−i) ,

where fi ∈ RM(m − i, r − 1). It is not hard to prove that with high probability, when we choose the
fi’s at random we get that bias(g) ≥ 2−ℓ+1. A simple counting argument then gives the claimed lower
bound.
 IV. CAPACITY RESULTS
A. RM codes achieve capacity at low rate [1], [2]
The results on the weight enumerator that were described in Section III can be used to show that RM
codes having low rate achieve capacity for the BEC and the BSC. Note that in the case of rates close
to 0 achieving capacity means that, for the BEC we can correct a fraction p ≥ 1 − R(1 + ϵ) of random
erasures (with high probability), and for the BSC we can correct a fraction p of random errors (with
high probability) for p satisfying h(p) ≥ 1 − R(1 + ϵ). See [1] for a discussion of achieving capacity
in extremal regimes. In the following subsections we shall show how to relate the error of the natural
decoder for each channel to the weight distribution of the code. Such results were ﬁrst prove in [1] and
later strengthened in [2] using essentially the same approach so we only give the state of the art results
of [2].

1) BEC: In this section we relate the weight distribution of a RM code to the probability of correctly
decoding from random erasures. In [1], [2] this was used to conclude that RM codes achieve capacity
for the BEC at certain parameter range.
Denote by err(p, m, r) the probability that RM(m, r) cannot recover from random erasures with
parameter p (i.e. when the erasure probability is p). To upper bound err(p, m, r) we need to understand
when can we correct a codeword f from some erasure pattern, where the erasure pattern is the set of
coordinates erased in f . Thus, given a codeword f and an erasure pattern S ⊆ Fm
2 , the corresponding
corrupted codeword is the evaluation vector of f with the evaluations over the set S erased. The basic
idea is based on the simple fact that an erasure pattern can be recovered from if and only if no codeword
is supported on the pattern. By that we mean that there is no codeword f that obtains nonzero values
only for points in S, and therefore there is no other codeword that agrees with the transmitted one on the
unerased section. Thus, to bound the probability of failing to correct we need to bound the probability that
a codeword is supported on a random erasure pattern (where each coordinate is selected with probability
p).

Lemma 4. For r ≤ m ∈ N. For R = Rate (RM(rm, r)) it holds that,

err(p, m, r) ≤ ∑

β (1 − β)(1−p)2m · Am,r (β) , (4)

16

where β ranges over all possible weights.

Proof sketch. To simplify matters assume that the erasure pattern consists of exactly p·2m = pn erasures.
We now wish to bound that probability that a random set S ⊂ Fm
2 of size |S| = p · 2m contains the
support of a codeword. To bound this probability, ﬁx a codeword f . Then, this probability is exactly
equivalent to the probability that the complement of the support of f contains the complement of S.
Thus, assuming we only care about error patterns of size p · 2m we get

err(p, m, r) ≈ ∑

0̸=f ∈RM(m,r)
 ((1−wt(f ))2
m

(1−p)·2m )

( 2m
(1−p)·2m) ≤ ∑

0̸=f ∈RM(m,r)
(1 − wt(f ))
(1−p)·2
m .

Thus, if we want to use Lemma 4 to prove that RM codes achieve capacity for random erasures then
we basically have to show that Am,r (≤ β) decays faster than (1 − β)(1−p)2m, for p = 1 − (1 + o(1))R. In
order to estimate the sum in (4), [2] partitions the summation over β to the dyadic intervals [2−k−1, 2−k]
and shows that each such interval sums to a small quantity. For k ≥ 2 they use the estimate given
in Theorem 4. To handle the interval [1/4, 1/2] they partition it further to smaller dyadic intervals.
Speciﬁcally, they start with polynomials of bias ϵ, for some sub-constant ϵ, and double the bias until they
reach bias 1/2 (equivalently, weight 1/4). To estimate the contribution of each such sub-interval to the
sum they use Theorem 7. This gives the following result from [2].

Theorem 12 (Theorem 1.9 from [2]). For any r ≤ m/50, RM(m, r) achieves capacity on the BEC.

In addition, they proved that for higher degrees, that lead to codes of rate 1/ poly(log n), RM codes
can correct a fraction 1 − o(1) of random erasures. The proof idea is essentially the same.

Theorem 13. For any r < m/2 − Ω (√m log m
), RM(m, r) can efﬁciently correct a fraction of 1 − o(1)
random erasures (as m increases).

While this result is not enough to deduce that the code achieves capacity, it shows that it is very close
to doing that.

2) BSC: Similarly to what we did in Section IV-A1 we shall relate the probability that we fail to
correct random errors to the weight distribution of the code. For simplicity we shall assume that instead
of ﬂipping each bit with probability p the channel ﬂips exactly p · 2m = pn locations at random. Consider
the decoder that returns the closest codeword to the received word. A bad error pattern z ∈ Fn
2 is one
for which there exists another error pattern z′ ∈ Fn
2 , of weight s = pn, such that z + z′ is a codeword in
RM(m, r). Note that since both z and z′ are different and have the same weight, the weight of z +z′ must
be even and in {d, . . . , 2pn}. As both z + z′ and the all 1 vector are codewords, we also have that the
weight of z + z′ is at most n − d, hence |z + z| ∈ {d, . . . , n − d}. Therefore, counting the number of bad
error patterns is equivalent to counting the number of weight s vectors that can be obtained by “splitting”
codewords whose (un-normalized) weight is an even number in {d, . . . , n − d}. For a codeword y of
hamming weight |y| = w, there are w/2 choices for the support of z inside
6 support(y) and pn − w/2
choices outside the codeword’s support (z and z′ must cancel each other outside the support of y and
hence have the same weight inside support(y)). Denote by B the set of bad error patterns, the union
bound then gives

P{B} ≤ ∑

w∈{d,...,n−d} Am,r (w/n)
 ( w
w/2
)( n−w
pn−w/2
)

( n
pn) = ∑

β∈ 1
n ·{d,...,n−d} Am,r (β)
 ( βn
βn/2
)( (1−β)n
(p−β/2)n
)

( n
pn) .

6By support(y) we mean the set of nonzero coordinates of y.
 17

As before, Sberlo and Shpilka partition the sum to small interval around weight 1/2 and then to dadic
interval of the form [2−k−1, 2−k] and bound the contribution of each interval separately to the sum using
Theorems 7 and 4, respectively. They thus were able to prove the following result.

Theorem 14 (Theorem 1.10 of [2]). For any r ≤ m/70, RM(m, r) achieves capacity on the BSC.

Similarly to the BEC case, we can show that up to degrees close to m/2, RM codes can correct a
fraction 1/2 − o(1) of random errors.

Theorem 15. For any r < m/2 − Ω (√m log m
) the maximum likelihood decoder for RM(m, r) can
correct a fraction of 1/2 − o(1) random errors.

As in Theorem 13, this is not enough to show that RM codes achieve capacity at this range of
parameters (as the o(1) term is not the correct one), but it gives a good indication that it does.

B. RM codes achieve capacity on the BEC at high rate [1]
In this section we explain the high level idea of the proof of [1] that RM codes of very high degree
achieve capacity for the BEC. Similar to the case of R → 0, we say that a family of codes of rate R → 1
achieves capacity for the BEC if it can correct (with high probability) a fraction p ≥ (1 − ϵ)(1 − R) of
erasures. Thus, for such a code to achieve capacity for the BEC it must hold that, with high probability,
(1 − (1 − ϵ)(1 − R)) n random rows of the generating span the row space. This is equivalent to saying
that if we consider the parity check matrix of the code, then a random subset of (1 − ϵ)(1 − R)n columns
is full rank (i.e. the columns are linearly independent) with high probability.
Since we will be dealing with very high rates (i.e. very high degrees) it will be more convenient for
us to think of our code as RM(m, m − r − 1) (i.e. RM code of degree m − r − 1). As the parity check
matrix of RM(m, m − r − 1) is the generating matrix of RM(m, r), the discussion above gives rise to
the question that we discuss next.
For an input z ∈ Fm
2 and degree r denote with zr the column of Rn corresponding to the evaluation
point z (recall Equation (12)). In other words, zr contains the evaluation of all multilinear monomials of
degree at most r at z. Thus, the code RM(m, m − r − 1) achieves capacity for the BEC if it holds with
high probability that a random subset Z ⊂ F m
2 , of size |Z| = (1 − ϵ)( m
≤r), satisﬁes that the set {zr |
z ∈ Z} is linearly independent.
Abbe et al. [1] show that this is indeed the case for small enough r.

Theorem 16. [1] For r = o(√m/ log m), RM(m, m − r − 1) achieves capacity on the BEC.

The idea of the proof is to view the random Z as if the points were picked one after the other, and to
prove that as long as r is not too large, the relevant set remains independent with high probability. An
important observation made in [1] connects this problem to a question about common zeros of degree r
polynomials.

Claim 1 (Lemmas 4.6-4.9 of [1]). Let z1, . . . , zs ∈ Fm
2 be such that the vectors {zr
i } are linearly
independent. Let I = {f ∈ RM(m, r) | f (zi) = 0 for every 1 ≤ i ≤ s}. Then, for z ∈ Fm
2 , zr is not in
the span of {zr
i } if and only if there is some f ∈ I such that f (z) ̸= 0.

Proof Sketch. Observe that a vector c ∈ F( m
≤r)
2 is perpendicular to zr (in the sense that the dot product
is zero) if and only if the polynomial whose coefﬁcients are given by the coordinates of c vanishes at z.
Thus, the claim says that for a vector zr to be linearly independent of a set of vectors Z it must be the
case that the dual space to Z ∪ {zr} is smaller than the dual space of Z.

Thus, we have to understand what is the probability that a new point is a common zero of the
polynomials in I. By dimension arguments, dim(span(Z)) = s and hence dim(span(I)) = ( m
≤r) − s. It
remains to prove that if r = o(√m/ log m) and s = (1 − ϵ)( m
≤r) then the number of common zeroes of

18

the polynomials in I is o(2m). This will guarantee that a random point z is, with high probability, not
a common zero and by Claim 1 this will ensure that zr is linearly independent of Z as desired.
Denote with V ⊂ Fm
2 the set of common zeroes of the polynomials in I. That is, V = {z ∈ Fm
2 |
∀f ∈ I , f (z) = 0}. To prove that V is not too large, [1] show that if V was large then there would
be many degree r polynomials whose evaluation vectors on the points in V are linearly independent.
Indeed, by dimension arguments again we have that the dimension of the evaluation vectors of degree r
polynomials, restricted to the points in V , is at most ( m
≤r) − dim(span(I)) = ( m
≤r) − (( m
≤r) − s
) = s.
Thus, if one could show that must be more than that many linearly independent polynomials when V is
large, then one would get a contradiction. This is captured in the next lemma.

Lemma 5 (Lemma 4.10 of [1]). Let V ⊆ Fm
2 such that |V | > 2m−t. Then there are more than (m−t
≤r )

linearly independent polynomials of degree ≤ r that are deﬁned on V .

The proof relies on the notion of generalized hamming weight and on a theorem of Wei [48]. To
present this result we need some deﬁnitions. Let C ⊆ Fn
2 be a linear code and D ⊆ C a linear subcode.
We denote supp(D) = {i : ∃y ∈ D, such that yi ̸= 0}.

Deﬁnition 4 (Generalized Hamming weight). For a code C of length n and an integer a we deﬁne

da(C) = min{supp(D) | D ⊆ C is a linear subcode with dim(D) = a}.

The following lemma follows from arguments similar to what we described above.

Lemma 6. For a code C of length n and an integer a we have that

da(C) = max{b | ∀|S| < b we have that dim(C[Sc]) > dim(C) − a},

where for a set of coordinates S, C[Sc] is the linear code obtained by projecting each codeword in C
to the coordinate set Sc, the complement of the set S.

Wei’s theorem then gives the following identity.

Theorem 17 ([48]). Let 0 ≤ a ≤ ( m
≤r) be an integer. Then, da(RM(m, r)) = ∑ℓ
i=1 2mi, where a =
∑ℓ
i=1 ( mi
≤ri) is the unique representation of a.
7

Setting parameters carefully, we can prove Lemma 5.

Proof of Lemma 5. For a = ∑t
i=1 ( m−i
≤r−1)
, Theorem 17 implies that da(RM(m, r)) = ∑t
i=1 2m−i =
2m − 2m−t. Thus, if |V | > 2m − da(RM(m, r)) = 2m−t then there are more than ( m
≤r) − a = ( m
≤r) −
∑t
i=1 ( m−i
≤r−1
) = (m−t
≤r ) many linearly independent degree-r polynomials deﬁned on Z.

The result showing that RM(m, m − r − 1) achieves capacity for r = o(
√m/ log m) now follows
from the argument above by careful calculations.

C. RM codes achieve capacity on the BEC at constant rate [3]
In [3], [29], Kudekar et al. made use of the classic results about sharp thresholds of monotone boolean
functions [49]–[52] to prove that RM codes achieve capacity on erasure channels. More precisely, deﬁne

Q(x) := 1
√2π
 ∫ ∞

x e
−t
2/2dt.

Theorem 18. For any constant p ∈ (0, 1), the sequence of RM codes {RM(m, rm)} with

rm = max {⌊ m
2 + √m
2 Q
−1(p)⌋
, 0}

7Wei also proved that every 0 ≤ a ≤ ( m
≤r) has a unique representation as a = ∑ℓ
i=1 ( mi
≤ri)
, where mi − ri = m − r − i + 1.

19

has code rates approaching 1 − p and achieves capacity over BEC with erasure probability p.

While their proof applies to (Generalized) RM codes with larger alphabet Fq over the q-ary erasure
channel, in this section we focus on the proof for the binary RM codes over BEC.
We denote the output alphabet of BEC as {0, 1, ∗}, where ∗ is the erasure symbol. Consider the
transmission of a codeword x = (xz : z ∈ Fm
2 ) ∈ RM(m, r) through n = 2m copies of BEC channels,
and the channel output vector is denoted as y = (yz : z ∈ Fm
2 ). The probabilistic model is set up as
follows: Let X = (Xz : z ∈ Fm
2 ) be a random codeword uniformly chosen from RM(m, r) and let Y (p)
be the corresponding random output vector after transmitting X through n = 2m copies of BEC channels
with erasure probability p. Since the conditional entropy H(Xz|Y (p) = y) = 0 for every channel output
vector y with yz ̸= ∗, we have

H(Xz|Y (p)) = P(Yz = ∗)H(Xz|Y∼z(p)) = pH(Xz|Y∼z(p)), (5)

where Y∼z(p) := (Yz′(p) : z′ ∈ Fm
2 , z′ ̸= z). An important property of the BEC is that for any index
z ∈ Fm
2 and any output vector y, the conditional entropy H(Xz|Y (p) = y) and H(Xz|Y∼z(p) = y∼z)
can only take two values, either 0 or 1, i.e., given these outputs, each codeword coordinate Xz can either
be exactly reconstructed or Xz is equally likely to be 0 or 1. In the latter case, no useful information is
provided about Xz, and we say that Xz is “erased”. Further, since H(Xz|Y (p)) = ∑
y H(Xz|Y (p) =
y)P(Y (p) = y) = ∑
y:H(Xz|Y (p)=y)=1 P(Y (p) = y), we have that H(Xz|Y (p)) gives the probability that
Y (p) takes on values such that Xz is equally likely to be 0 or 1, i.e., such that Xz is “erased”. Therefore,
the channel mapping Xz to Y (p) is equivalent to a BEC with erasure probability H(Xz|Y (p)) (and
similarly for H(Xz|Y∼z(p))). When the channel output vector is y, the bit-MAP decoder decodes Xz as

argmaxx∈{0,1} P(Xz = x|Y (p) = y),

and if the maximum is not unique, i.e., if P(Xz = 0|Y (p) = y) = P(Xz = 1|Y (p) = y), then the decoder
declares an erasure and this takes place with probability H(Xz|Y (p)). From now on, we write

hz(p) := H(Xz|Y∼z(p)).

This function is called the extrinsic information transfer (EXIT) function and it was introduced by ten
Brink [53] in the context of turbo decoding. According to (5), analyzing the behavior of hz(p) is equivalent
to analyzing the decoding error probability of the bit-MAP decoder. We also deﬁne the average EXIT
function as h(p) := 1
n
 ∑

z∈Fm
2 hz(p).

Since RM codes are afﬁne invariant, for any two coordinates z and z′, we can always ﬁnd a permutation
in the automorphism group of RM codes mapping from z to z′. As a consequence, one can easily show
that the value of hz(p) is independent of the index z, i.e.,

h(p) = hz(p) for every z ∈ Fm
2 .

Furthermore, we also have that 0 ≤ h(p) ≤ 1 for any 0 ≤ p ≤ 1. The average EXIT functions of some
rate-1/2 Reed-Muller codes are shown in Fig. 1. The following three properties of the (average) EXIT
function allow us to prove that RM codes achieve capacity under bit-MAP decoding:
1) h(p) is a strictly increasing function of p.
2) h(p) has a sharp transition from 0 to 1. More precisely, for any 0 < ϵ < 1/2, we have

h
−1(1 − ϵ) − h−1(ϵ) → 0

as the code length n → ∞.
3) The average EXIT function satisﬁes the area theorem
∫ 1

0 h(p)dp = k
n , (6)

20

Fig. 1: The average EXIT function of the rate-1/2 Reed-Muller code with blocklength n. This is originally
Fig. 1 in [29].

where k is the dimension of the RM code and n is code length.
Property 2) here simply means that as the blocklength increases, the transition width of the average
EXIT function decreases, as illustrated in Fig. 1.
The ﬁrst two properties imply that the function h(p) has a threshold p∗ and a small transition width
w → 0 as n → ∞. When p < p∗ − w/2, we have h(p) ≈ 0; when p is around p∗, i.e., when p∗ − w/2 ≤
p ≤ p∗ + w/2, the function h(p) increases very fast from 0 to 1; when p > p∗ + w/2, we have h(p) ≈ 1.
More precisely, for a given ϵ ∈ (0, 1/2), we deﬁne the threshold as p∗(ϵ) = 1
2 h−1(1 − ϵ) + 1
2 h−1(ϵ)
and the transition width as w(ϵ) = h−1(1 − ϵ) − h−1(ϵ). For p < p∗(ϵ) − w(ϵ)/2, we have h(p) < ϵ;
then the function h(p) increases from ϵ to 1 − ϵ between p∗(ϵ) − w(ϵ)/2 < p < p∗(ϵ) + w(ϵ)/2; for
p > p∗(ϵ) + w(ϵ)/2, we have h(p) > 1 − ϵ. Property 2) above tells us that for any given ϵ ∈ (0, 1/2),
the transition width w(ϵ) → 0 as n → ∞. Finally, property 3) above allows us to locate the threshold
p∗(ϵ): Let us think of the extreme case where the transition width w(0) = 0. Under this assumption, we
have h(p) = 0 for all p < p∗ and h(p) = 1 for all p > p∗. Then ∫ 1
0 h(p)dp = 1 − p∗, so by (6) we
have that p∗ = 1 − k
n . Now back to the case where we only have w(ϵ) → 0 for any given ϵ instead of
w(0) = 0, we can still use a similar calculation to show that p∗(ϵ) → 1 − k
n for any given ϵ ∈ (0, 1/2)
when n → ∞. This in particular means that for any ϵ > 0, there exists δ > 0 such that h(p) < ϵ for all
p < 1 − k
n − δ and all large enough n. Since the decoding error of bit-MAP decoder is ph(p), we have
shown that the decoding error goes to 0 when the code rate approaches 1 − p, the capacity of BEC, i.e.,
we have shown that RM codes achieve capacity of BEC under bit-MAP decoder.
Next we will explain how to prove properties 1)–3). Property 3) ﬁrst appeared in [54], and it follows
directly from the following equality

H(X|Y (1)) − H(X|Y (0)) = ∫ 1

0
 

 ∑

z∈Fm
2 hz(p)


 dp (7)

Indeed, H(X|Y (1)) = k and H(X|Y (0)) = 0, so the left-hand side of (7) is k. By deﬁnition, the
right-hand side of (7) is n ∫ 1
0 h(p)dp. Therefore, (6) follows immediately from (7). Equation (7) itself is
implied by the results of both [54] and [55], and it can be proved using the chain rule of derivatives as
follows: We consider a slightly different model where different coordinates in the codeword are transmitted
through BEC channels with (possibly) different erasure probabilities. More speciﬁcally, assume that Xz
is transmitted through a BEC with erasure probability pz; previously we assumed that pz = p for all

21

z ∈ Fm
2 . For a parametrized path (pz(t) : z ∈ Fm
2 ) deﬁned for t ∈ [0, 1], one ﬁnds that

H(X|Y (1)) − H(X|Y (0)) = ∫ 1

0
 

 ∑

z∈Fm
2
 ∂H(X|Y (pz : z ∈ Fm
2 ))
∂pz
 dpz
dt
 

 dt.

One can further show (e.g. using (5)) that

H(Xz|Y∼z(p∼z)) = ∂H(X|Y (pz : z ∈ Fm
2 ))
∂pz .

Therefore,
 H(X|Y (1)) − H(X|Y (0)) = ∫ 1

0 ( ∑

z∈Fm
2 H(Xz|Y∼z(p∼z)) dpz
dt )dt.

Equation (7) follows immediately by taking the parametrized path (pz(t) : z ∈ Fm
2 ) to be pz(t) = t for
all z ∈ Fm
2 in the above equation.
Both property 1) and property 2) are established by connecting h(p) to monotone and symmetric
boolean functions and making use of the classic results on such functions [49]–[52]. In order to connect
h(p) to boolean functions, we use the fact that h(p) = hz(p) for every z ∈ Fm
2 . Below we ﬁx an index z
and associate an erasure pattern e∼z(y∼z) = (ez′(y∼z) : z′ ∈ Fm
2 , z′ ̸= z) ∈ {0, 1}n−1 with each channel
output vector y∼z as follows:

ez′(y∼z) = 1[yz′ = ∗] for all z′ ∈ (Fm
2 \ {z}),

i.e., e∼z(y∼z) is an indicator vector of the erasures in y∼z. We further deﬁne the set Ωz ⊆ {0, 1}n−1 as

Ωz := {e∼z(y∼z) : H(Xz|Y∼z(p) = y∼z) = 1}.

This is the set of erasure patterns that prevent the recovery of Xz from Y∼z(p). Note that the set Ωz
is completely determined by the RM code construction and it is independent of the channel erasure
probability p. We say that an erasure pattern e∼z covers another erasure pattern ˜e∼z if ez′ ≥ ˜ez′ for all
z′ ∈ (Fm
2 \ {z}). The set Ωz has the following monotone property: if (1) ˜e∼z ∈ Ωz and (2) e∼z covers
˜e∼z, then e∼z ∈ Ωz.
For each erasure pattern e∼z, we use |e∼z| to denote its Hamming weight. We write the probability of
erasure pattern e∼z under BEC with channel erasure probability p as µp(e∼z), and it is given by

µp(e∼z) = p
|e∼z|(1 − p)
n−1−|e∼z|.

Using this notation, µp(Ωz) = ∑

e∼z∈Ωz p|e∼z|(1 − p)
n−1−|e∼z|.

By deﬁnition, we have h(p) = hz(p) = µp(Ωz). (8)

Next we deﬁne the “boundary” of Ωz. For an erasure pattern e∼z ∈ {0, 1}n−1, we deﬁne ﬂip(e∼z, z′)
to be another erasure pattern obtained by ﬂipping the z′ coordinate in e∼z. The “boundary” of Ωz across
the z′ coordinate is deﬁned as

∂z′Ωz := {e∼z : 1[e∼z ∈ Ωz] ̸= 1[ﬂip(e∼z, z′) ∈ Ωz]}.

Notice that ∂z′Ωz contains the “boundary” erasure patterns both inside and outside of Ωz. This is because
by deﬁnition if e∼z ∈ ∂z′Ωz, then ﬂip(e∼z, z′) ∈ ∂z′Ωz. The probability measure µp(∂z′Ωz) is called the
inﬂuence of the z′ coordinate, and one further deﬁnes the total inﬂuence as

I (p)(Ωz) := ∑

z′∈(Fm
2 \{z}) µp(∂z′Ωz);
 22

see [56]–[59] for discussions and properties of these functions.
An important consequence of the monotone property is the following equality [56]–[58] connecting
the derivative of µp(Ωz) with the total inﬂuence

dµp(Ωz)
dp = I (p)(Ωz).

Property 1) of h(p) follows immediately from this equality and (8).
As for Property 2) of h(p), observe that the set Ωz also has a symmetric property which follows from the
afﬁne-invariant property of RM codes. More precisely, for any z′, z′′ ∈ (Fm
2 \{z}), the inﬂuences of the z′

and z′′ coordinates are always the same for all 0 ≤ p ≤ 1, i.e., we always have µp(∂z′Ωz) = µp(∂z′′Ωz).
This is because for any triple z, z′, z′′ ∈ Fm
2 we can always ﬁnd an invertible afﬁne linear transform over
Fm
2 that ﬁxes z and maps z′ to z′′.
This symmetric property of Ωz allows us to use the following classic result on Boolean functions:

Theorem 19 ([49]–[52]). Let Ω ⊆ {0, 1}M be a monotone set and suppose that for all 0 ≤ p ≤ 1, the
inﬂuences of all bits under the measure µp are equal. Then for all 0 ≤ p ≤ 1,

dµp(Ω)
dp = I (p)(Ω) ≥ ln(M )µp(Ω)(1 − µp(Ω)).

Applying this theorem to Ωz, we obtain that for all 0 < p < 1,

dµp(Ωz)
dp = I (p)(Ωz) ≥ ln(n − 1)µp(Ωz)(1 − µp(Ωz)).

Combining this with (8), we have
 dh(p)
dp ≥ ln(n − 1)h(p)(1 − h(p)). (9)

This inequality tells us that for any given ϵ ∈ (0, 1/2), we always have dh(p)
dp → ∞ as n → ∞ for all p
satisfying h(p) ∈ (ϵ, 1 − ϵ). Therefore, h(p) has a sharp transition from ϵ to 1 − ϵ for arbitrarily small
ϵ > 0 when the code length n is large enough, and this proves property 2) of h(p).
Now this shows that RM codes achieve capacity of BEC under the bit-MAP decoder. In [3], [29], it
was also proved that RM codes achieve capacity of BEC under the block-MAP decoder. The proof uses
the same framework and relies on a reﬁnement of (9) in [60]. In particular, Bourgain and Kalai [60]
showed that there exists a universal constant C such that
dh(p)
dp ≥ C ln(ln(n − 1)) ln(n − 1)h(p)(1 − h(p)).

The proof for block-MAP decoder then follows the same line of arguments as the proof for bit-MAP
decoder but requires a few more technical details which we will omit here.

Remark 2. For BEC, the conditional entropy H(Xz|Y∼z(p) = y∼z) can only be either 0 or 1, and it is
independent of the channel erasure probability p. This property allows us to connect h(p) with boolean
functions and use the classic results to analyze h(p). Unfortunately, this property no longer holds for
general communication channels such as BSC. Now suppose instead that Y (p) is the random output
vector after transmitting X through n = 2m copies of BSC with channel crossover probability p. In this
case, the conditional entropy H(Xz|Y∼z(p) = y∼z) will vary with p and its range is clearly not limited
to {0, 1}. Moreover, the monotone property of the set Ωz is also a consequence of transmitting codewords
through erasure channels, and it does not hold for general communication channels like BSC. In other
words, for BSC, more errors do not necessarily lead to larger conditional entropy H(Xz|Y∼z(p) = y∼z).
For example, since the all-one vector is a codeword of RM codes, we always have the equality

H(Xz|Y∼z(p) = 0) = H(Xz|Y∼z(p) = 1),
 23

U1

U2
...

Un
 Gn: n × n
tensor
product
matrix
 X1

X2
...

Xn
 W

W
...
W
 Y1

Y2
...
Yn

(a) Polarization framework
 UA1
UA2
...

UAn
 Rn : n × n
generator
matrix of
RM(m, m)
 X1

X2
...

Xn
 W

W
...
W
 Y1

Y2
...
Yn

(b) Polarization framework for RM codes

Fig. 2: Polarization framework: The input vector U n are i.i.d. Bernoulli(1/2) random variables. Given
the channel output vector Y n, we use successive decoder to decode the input vector U n one by one from
top to bottom.

where 0 and 1 are the all-zero and all-one vectors, respectively. Now assume that we transmit the all-zero
codeword. Then this equality means that the conditional entropy given an output with no errors is the
same as the conditional entropy given an output that is erroneous in every bit. This clearly does not
satisfy the monotone property. Finally, the area theorem (see (6)) for EXIT function only holds for BEC.
For general channels, one needs to work with the generalized EXIT (GEXIT) function introduced in [61].
The GEXIT function is similar in many respects to the EXIT function: The GEXIT function satisﬁes the
area theorem for general channels and it is neither boolean nor monotonic. New ideas are certainly
required to analyze such functions in order to generalize the method of [3], [29] for the cases of BSC
or more general communication channels.

Remark 3. Note that the approach in this subsection only works for the constant rate regime and does
not extend to the extremal rate regimes discussed in Section IV-A and Section IV-B.

D. RM codes polarize and Twin-RM codes achieve capacity on any BMS [4]
Recall that a binary memoryless symmetric (BMS) channel is a channel W : {0, 1} → Y such that
there is a permutation π on the output alphabet Y satisfying i) π−1 = π and ii) W (y|1) = W (π(y)|0)
for all y ∈ Y. In particular, the binary erasure channel (BEC), the binary symmetric channel (BSC), and
the binary input additive white Gaussian noise channel (BIAWGN) are all BMS channels.
We now consider an arbitrary BMS channel W . We use the communication model in Fig. 2a to
transmit information over W . The input vector U n consists of n i.i.d. Bernoulli(1/2) random variables.
We encode U n by multiplying it with an n × n invertible matrix Gn and denote the resulting vector as
(X1, . . . , Xn) = (U1, . . . , Un)Gn. Then we transmit each Xi through an independent copy of W . Given
the channel output vector Y n, our task is to recover the input vector U n, and we use a successive decoder
to do so. The successive decoder decodes the input vector bit by bit from U1 to Un. When decoding Ui,
it makes use of all the channel outputs Y n and all the previously decoded8 inputs U i−1. The conditional
entropy Hi := H(Ui|U i−1, Y n)

indicates whether Ui is noisy or noiseless under the successive decoder: If Hi ≈ 0, then Ui is (almost)
noiseless and can be correctly decoded with high probability. If Hi is bounded away from 0, then so is
the decoding error probability of decoding Ui.
Informally, we say that the matrix Gn polarizes if almost all Hi, 1 ≤ i ≤ n are close to either 0 or 1,
or equivalently, if almost all Ui, i ≤ i ≤ n become either noiseless or completely noisy. An important
consequence of polarization is that every polarizing matrix automatically gives us a capacity-achieving
code under the successive decoder. Indeed, if Gn polarizes, then we can construct the capacity achieving
code by putting all the information in the Ui’s whose corresponding Hi is close to 0 and freezing all

8Assuming no decoding errors up to U i−1.
 24

the other Ui’s to be 0, i.e., we only put information in the (almost) noiseless Ui’s. Let G be the set of
indices of the noiseless Ui’s. Then the generator matrix of this code is the submatrix of Gn obtaining by
retaining only the rows whose indices belong to G. To show that this code achieves capacity, we only
need to argue that |G| is asymptotic to nI(W ), and this directly follows from

n∑

i=1 Hi = H(U n|Y n) = H(X n|Y n) = nH(Xi|Yi) = n(1 − I(W )), (10)

where the last equality relies on the assumption that W is symmetric. Since almost all Hi’s are close to
either 0 or 1, by the equation above we know that the number of Hi’s that are close to 1 is asymptotic
to n(1 − I(W )), so the number of Hi’s that are close to 0 is asymptotic nI(W ), i.e., |G| is asymptotic
to nI(W ).
In his inﬂuential paper [38], Arıkan gave an explicit construction of a polarizing matrix

Gn := [
1 0
1 1
]⊗m ,

where ⊗ is the Kronecker product and n = 2m. For example

G4 := [
1 0
1 1
]⊗2 =
 




1 0 0 0
1 1 0 0
1 0 1 0
1 1 1 1




 .

Polar codes are simply the capacity-achieving codes constructed from Gn. More precisely:

Theorem 20 (Polarization for Gn). For any BMS channel W and any 0 < ϵ < 1/2,

|{i ⊆ [2
m] : Hi ∈ (ϵ, 1 − ϵ)}| = o(2
m). (11)

In particular, the above still holds for some choices of ϵ = ϵn that are o(1/n) (in fact, ϵn can even
decay exponentially with roughly the square-root of n). Therefore, the polar code retaining only rows i
of Gn such that Hi ≤ ϵn has a block error probability that is upper-bounded by |Gn|ϵn ≤ nϵn, and if
ϵn = o(1/n), the block error probability is upper-bounded by nϵn = o(1), and the code achieves capacity.
The encoding procedure of polar codes amounts to ﬁnding G, the set of noiseless (or “good”) bits,
and efﬁcient algorithms for ﬁnding these were proposed in [38], [62]. In [38], Arıkan also showed that
the successive decoder for polar codes allows for an O(n log n) implementation. Later in [63], a list
decoding version of the successive decoder was proposed, and its performance is nearly the same as the
Maximum Likelihood (ML) decoder of polar codes for a wide range of parameters.
In [4], the authors develop a similar polarization framework to analyze RM codes; see Fig. 2b for an
illustration. More precisely, the monomials xA1, . . . , xAn deﬁned by the n := 2m subsets A1, . . . , An
of [m], are used in replacement to the increasing integer index i in [n]. We arrange these subsets in
the following order: Larger sets always appear before smaller sets; for sets with equal size, we use the
lexicographic order. More precisely, if i < j, we always have |Ai| ≥ |Aj|, and we have Ai < Aj –where
< denotes the lexicographic order– if |Ai| = |Aj|. Deﬁne the matrix

Rn :=
 




Eval(xA1)
Eval(xA2)
...
Eval(xAn)





 (12)

25

whose row vectors are arranged according to the order of the subsets. By deﬁnition, Rn is a generator
matrix of RM(m, m). Here we give a concrete example of the order of sets and Rn for m = 3 and
n = 2m = 8: A1 = {1, 2, 3}
A2 = {1, 2}
A3 = {1, 3}
A4 = {2, 3}
A5 = {1}
A6 = {2}
A7 = {3}
A8 = ∅
 R8 =
 












1 0 0 0 0 0 0 0
1 1 0 0 0 0 0 0
1 0 1 0 0 0 0 0
1 0 0 0 1 0 0 0
1 1 1 1 0 0 0 0
1 1 0 0 1 1 0 0
1 0 1 0 1 0 1 0
1 1 1 1 1 1 1 1













 .

Note that Rn is a row permutation of Gn. Let UA1, . . . , UAn be the (random) coefﬁcients of the monomials
xA1, . . . , xAn. Multiplying the coefﬁcient vector (UA1, . . . , UAn) with Rn gives us a mapping from the
coefﬁcient vector to the evaluation vector X n := (UA1, . . . , UAn)Rn. Then we transmit each Xi through
an independent copy of W and get the channel output vector Y n. We still use the successive decoder
to decode the coefﬁcient vector bit by bit from UA1 to UAn. Similarly to Hi, we deﬁne the conditional
entropy HAi := H(UAi|UA1, . . . , UAi−1, Y n),

and by the chain rule we also have the balance equation

n∑

i=1 HAi = n(1 − I(W )), (13)

In [4], a polarization result for HAi is obtained, showing that with this ordering too, almost all HAi
are close to either 0 or 1. More precisely:

Theorem 21 (Polarization of RM codes). For any BMS channel W and any 0 < ϵ < 1/2,

|{i ∈ [2
m] : HAi ∈ (ϵ, 1 − ϵ)}| = o(2
m). (14)

In particular, the above still holds for some choices of ϵ = ϵn that decay faster than 1/n. Therefore
the code obtained by retaining only the monomials xAi in Rn corresponding to Ai’s such that HAi ≤ ϵn
has a vanishing block error probability and achieves capacity; this follows from the same reasoning as
in polar codes. We call this code the Twin-RM code as it is not necessarily the RM code. In fact, if the
following implication were true,
 |A| > |B| ?
=⇒ HA ≥ HB, (15)

then the Twin-RM would be exactly the RM code, and the latter would also achieve capacity on any
BMS. The same conclusion would hold if (15) held true for most sets; it is nonetheless conjectured in
[4] that (15) holds in the strict sense. To further support this claim, [4] provides two partial results:
(i) Partial order:
 A ⊇ B =⇒ HA ≥ HB, (16)

more generally, the implication is shown to hold if there exists ˜B s.t. A ⊇ ˜B, | ˜B| = |B| and ˜B is
less than B and each component of ˜B is smaller than or equal to the corresponding component of
B (as integers).
(ii) For the BSC, (15) is proved up to 2m = 16, and numerically veriﬁed for some larger block lengths.
It is also shown in [4] that it sufﬁces to check (15) for speciﬁc subsets. It is useful at this point to
introduce the division of the input bits of RM(m, r) into m + 1 layers, where the jth layer corresponds
to the subsets of [m] with size j, and the range of j is from 0 to m. Therefore, the 0th layer only has
one bit U1, and the ﬁrst layer has m bits U2, U3, . . . , Um+1. In general, the ith layer has (
m
i ) bits. It is

26

shown in [4] that it sufﬁces to check (15) for subsets A, B that are respectively the last and ﬁrst subsets
in consecutive layers, as these are shown to achieve respectively the largest and least entropy within
layers. We now present the proof technique for Theorem 21.
Proof technique for Theorem 21. When m = 1 and n = 2, the polar and RM matrices are the same:

G2 = R2 = [
1 0
1 1
] .

Deﬁne H(W ) := 1 − I(W ). The balance equation gives

2H(W ) = H(U1|Y1, Y2) + H(U2|Y1, Y2, U1),

and since H(U2|Y1, Y2, U1) ≤ H(U2|Y2) = H(W ), we can create two synthetic channels W − : U1 →
(Y1, Y2) and W + : U2 → (Y1, Y2, U1) such that for ∆ := H(W +) − H(W ),

H(W −) = H(W ) + ∆/2 ≥ H(W ) ≥ H(W +) = H(W ) − ∆/2, (17)

and the above inequalities are strict unless ∆ = H(W +) − H(W ) = 0, which is equivalent to H(W ) ∈
{0, 1}, i.e., the channel is already extremal. One can write a quantitative version of this, i.e., for any
binary input symmetric output channel W , there exists a positive continuous function δ on [0, 1/2) that
vanishes only at 0, such that for any ϵ ∈ (0, 1/2),

H(W ) ∈ (ϵ, 1 − ϵ) =⇒ ∆ = H(W +) − H(W ) ≥ δ(ϵ). (18)

Therefore, unless the initial channel W was already close to extremal, the synthesized channel W + is
strictly better by a bounded amount.
If we move to m = 2, then we still have G4 = R4, and we can create four synthetic channels
W −−, W −+, W +−, W ++ corresponding to the channels mapping Ui to (Y 4, U i−1) where the binary
expansion of i (mapping 0 to − and 1 to +) gives the channel index. Note that the behavior of these
channels at m = 2 can be related to that at m = 1, as suggested by the notation W s1s2, s1, s2 ∈
{−, +}. Namely, the two channels (W ∗−, W ∗+) are the synthesized channels obtained by composing
two independent copies of W ∗, ∗ ∈ {−, +} with the transformation G2, as done for m = 1.
In the case of polar codes, one intentionally preserves this induction. Namely, after obtaining n synthetic
channels W s, s ∈ {−, +}m, one produce twice more channels with the + and - versions of these, such
that for each one:

H(W s−) = H(W s) + ∆s/2 ≥ H(W s) ≥ H(W s+) = H(W s) − ∆s/2, (19)

with ∆s := H(W s+) − H(W s), s ∈ {−, +}m. This follows by the inductive property of G2n:

G2n = [
Gn 0
Gn Gn
] .

The polarization result is then a consequence of this recursive process: if one tracks the entropies of the
2m channels at level m, at the next iteration, i.e., at level m + 1, one breaks symmetrically each of the
previous entropies into one strictly lower and one strictly larger value, as long as the produced entropies
are not extremal, i.e., not 0 or 1. Therefore, extremal conﬁgurations are the only stable points of this
process, and most of the values end up at these extremes. This can be deduced by using the martingale
convergence theorem,9 and the fact that the only ﬁxed point of the −, + transform are at the extremes,
or conversely, that for values that are not close to the extremes, a strict movement takes place as in (18).
One needs however a stronger condition than (18). In fact, (18) holds for any W , but the function δ
could depend on the channel W , and we need to apply (18) to the channels W s that have an output
alphabet that grows as s grows. We therefore need a universal function δ that applies to all the channels
W s, so that we can lower-bound ∆s universally when H(W s) ∈ (ϵ, 1 − ϵ). Note that if W is a BMS
channels, then each W s is still a BMS channel, so we can restrict ourselves to this class of channels. The

9It is sufﬁcient to check that the variance of the 2
m entropies at time m decreases when m increases.
 27

existence of a universal function δ follows then from the following inequality,
10 which can be proved as
a consequence of the so-called Mrs. Gerber’s Lemma
11:

H(U1 + U2|T1, T2) − H(U2|T2) ≥ H(V1 + V2) − H(V2) (20)

where (U1, T1), (U2, T2) are i.i.d. with U1 binary uniform, T1 is arbitrary discrete valued, and V1, V2 are
i.i.d. binary uniform such that H(U2|T2) = H(V2). Therefore, the entropy spread H(W s+) − H(W s)
for any s is as large as the entropy spread of a simple BSC that has a matching entropy, since 1 − H(V2)
is a BSC capacity and H(U2|T2) = H(V2). The universal function δ can then be found explicitly by
inspecting the right hand side of (20), and for any ϵ ∈ (0, 1/2), there exists δ(ϵ) > 0 such that for any
m ≥ 1, s ∈ {−, +}m,

H(W s) ∈ (ϵ, 1 − ϵ) =⇒ ∆s = H(W s+) − H(W s) ≥ δ(ϵ). (21)

For RM codes, the inductive argument is broken. In particular, we no longer have a symmetric break
of the conditional entropies as in (19), hence no obvious martingale argument. Nonetheless, we next
argue that the loss of the inductive/symmetric structure takes place in a favorable way, i.e., the spread
in (19) tends to be greater for RM codes than for polar codes. In turn, we claim that the conditional
entropies polarize faster in the RM code ordering (see [4]). We next explain this and show how one
can take a short-cut to show that RM codes polarize using increasing chains of subsets, exploiting the
Plotkin recursive structure of RM codes and known inequalities from polar codes. We ﬁrst need to deﬁne
increasing chains.

Deﬁnition 5 (Increasing chains). We say that ∅ = B0 ⊆ B1 ⊆ B2 ⊆ · · · ⊆ Bm = [m] is an increasing
chain if |Bi| = i for all i = 0, 1, 2, . . . , m.

As for polar codes, we will make use of the recursive structure of RM codes, i.e., the fact that
RM(m+1, m+1) can be decomposed into two independent copies of RM(m, m). In order to distinguish
HA’s for RM codes with different parameters, we add a superscript to the notation, writing H (m)
A instead
of HA. A main step in our argument consist in proving the following theorem:

Theorem 22 (RM polarization on chains). For every BMS channel W , every positive m and every
increasing chain {Bi}m
i=0, we have

H (m)
B0 ≤ H (m)
B1 ≤ H (m)
B2 ≤ · · · ≤ H (m)
Bm . (22)

Further, for any ϵ ∈ (0, 1/2), there is a constant D(ϵ) such that for every positive m and every increasing
chain {Bi}m
i=0, ∣
∣
∣{
i ∈ {0, 1, . . . , m} : ϵ < H (m)
Bi < 1 − ϵ
}∣
∣
∣ ≤ D(ϵ). (23)

Note that D(ϵ) does not depend on m here. This theorem relies strongly on the following interlacing
property over chains.

Lemma 7 (Interlacing property). For every BMS channel W , every positive m and every increasing
chain {Bi}m
i=0, we have
 H (m+1)
Bi ≤ H (m)
Bi ≤ H (m+1)
Bi+1 ∀i ∈ {0, 1, . . . , m}. (24)

10This strong inequality may not be needed to obtain a universal function δ; weaker bounds and functions can be obtained,
as for example in [64] for non-binary alphabets.
11(20) is a convexity argument: H(U1 + U2|T1, T2) − H(U2|T2) = ∑

t1,t2 [H2(pt1 ⋆ pt2 ) − H2(pt2 )]P (T2 = t2)P (T1 = t1),
where pt = H(U1|T1 = t), H2 is the binary entropy function, and one can introduce the expectation inside H2 due to the
convexity property of Mrs. Gerber’s Lemma [65].
 28

. . . . . . . . .

. . . . . . . . .

ϵ 1 − ϵ

H (m+1)
B0
 H (m)
B0

H (m+1)
B1
 > δ

H (m)
B1

H (m+1)
B2
 > δ

H (m)
B2
 > δ
H (m+1)
B3 H (m+1)
Bm−2
> δ

H (m)
Bm−2

> δ

H (m+1)
Bm−1

> δ

H (m)
Bm−1

H (m+1)
Bm

H (m)
Bm

H (m+1)
Bm+1

Fig. 3: Illustration of the interlacing property in (24) used in the proofs of Theorem 22.

Polar transform

RM transform

H (m)
A4 H (m)
A3 H (m)
A2 H (m)
A1

H (m+1)
A2 H (m+1)
A2∪{m+1}

H((W (m)
A2 )+) H((W (m)
A2 )−)

“+” “−”

Fig. 4: The fast polar transform with block size 4. The dots on the second line are the results of the
standard polar transform, and the dots on the third line are the results of fast polar transform. In the fast
polar transform, the bit-channel obtained by adding a monomial gets even worse (i.e., has even more
entropy) than what would the classical polar − transform produce on that bit-channel, and similarly, the
better bit-channel obtained by not adding the monomial is even better (less entropic) that what the polar
+ transform would produce. Therefore, the gap between H (m+1)
Ai∪{m+1} and H (m+1)
Ai is always larger than

the gap between H((W (m)
Ai )−) and H((W (m)
Ai )+). Intuitively, this explains why RM codes polarize and
do so even faster than polar codes (although the formal proof uses the increasing chain argument).

The proof of Theorem 22 relies mainly on the previous lemma and the following polar-like inequality:
for any ϵ ∈ (0, 1/2), there is δ(ϵ) > 0 such that for any increasing chain and any i ∈ {0, 1, . . . , m},

H (m)
Bi ∈ (ϵ, 1 − ϵ) =⇒ H (m)
Bi − H (m+1)
Bi > δ(ϵ) and H (m+1)
Bi+1 − H (m)
Bi > δ(ϵ). (25)

Note that (25) is analogous to (21) except that (i) it does not involve the +, − transform of polar codes
but the augmentation or not of a monomial with a new element, (ii) the resulting spread is not necessarily
symmetrical as in (19). This is where it can be seen that RM codes have a bigger spread of polarization
than polar codes, as further discussed below.
We ﬁrst note that (22) follows directly from the interlacing property (24); see Fig. 3 for an illustration
of this. To prove (23), we combine (22) with the polar-like inequality (25). Indeed, by (25) we know that
as long as H (m)
Bi > ϵ and H (m)
Bi+1 < 1 − ϵ, we have H (m)
Bi+1 − H (m)
Bi > 2δ; see Fig. 3 for an illustration. Let

29

j be the smallest index such that H (m)
Bj > ϵ, and let j′ be the largest index such that H (m)
Bj′ < 1 − ϵ. Then
∣
∣
∣{
i ∈ {0, 1, . . . , m} : ϵ < H (m)
Bi < 1 − ϵ
}∣
∣
∣ = j′ − j + 1.

Since H (m)
Bi increases with i, we have H (m)
Bj′ − H (m)
Bj = ∑j′−1
i=j (H (m)
Bi+1 − H (m)
Bi ) > 2(j′ − j)δ, and since

H (m)
Bj′ − H (m)
Bj is upper bounded by 1, we have j′ − j < 1
2δ . Therefore,
∣
∣
∣{
i ∈ {0, 1, . . . , m} : ϵ < H (m)
Bi < 1 − ϵ
}∣
∣
∣ < 1
2δ + 1.

Thus we have proved (23) with the choice of D(ϵ) = 1/(2δ(ϵ)) + 1.
Now we are left to explain how to prove (24)–(25). In Fig. 2b, we deﬁne the bit-channel W (m)
Ai as the
binary-input channel that takes U (m)
Ai as input and Y n, (U (m)
Aj : j < i) as outputs, i.e., W (m)
Ai is the channel

seen by the successive RM decoder when decoding U (m)
Ai . By deﬁnition, we have H (m)
Ai = 1 − I(W (m)
Ai ).
Making use of the fact that RM(m + 1, m + 1) can be decomposed into two independent copies of
RM(m, m), one can show the larger spread of RM code split. More precisely, for every Ai ⊆ [m],
the bit-channel W (m+1)
Ai is always better than the “+” polar transform of W (m)
Ai , and the bit-channel
W (m+1)
Ai∪{m+1} is always worse than the “−” polar transform of W (m)
Ai , i.e.,

H (m+1)
Ai ≤ H((W (m)
Ai )+) ≤ H (m)
Ai ≤ H((W (m)
Ai )
−) ≤ H (m+1)
Ai∪{m+1}.

Therefore, the gap between H (m+1)
Ai∪{m+1} and H (m)
Ai is even larger than the gap between H((W (m)
Ai )−)

and H (m)
Ai . Similarly, the gap between H (m)
Ai and H (m+1)
Ai is even larger than the gap between H (m)
Ai and
H((W (m)
Ai )+); see Fig. 4 for an illustration. Combining this with the polar inequality (21), we have shown
that (24)–(25) hold for any Bi+1 = Bi ∪ {m + 1}. Then by the symmetry of RM codes, one can show
that H (m+1)
Bi∪{j} ≥ H (m+1)
Bi∪{m+1} for all j ∈ [m] \ Bi. This proves (24)–(25) and Theorem 22.
Theorem 22 proves a polarization on each increasing chain (See equation (23)). In order to obtain the
global polarization of RM codes (Theorem 21), we observe that there are in total m! increasing chains,
and a careful averaging argument over these m! chains gives the result in Theorem 21.

V. DECODING ALGORITHMS
We will survey various decoding algorithms for RM codes in this section. We divide these algorithms
into three categories. The ﬁrst category (Section V-A) only consists of Reed’s algorithm [5]: This is
the ﬁrst decoding algorithm for RM codes, designed for the worst-case error correction, and it can
efﬁciently correct any error pattern with Hamming weight up to half the code distance. The second
category (Section V-B) includes efﬁcient algorithms designed for correcting random errors or additive
Gaussian noise. These algorithms afford good practical performance in the short to medium code length
regime or for low-rate RM codes. Yet due to complexity constraints, most of them are not efﬁcient for
decoding RM codes with long code length. More speciﬁcally, we will cover the Fast Hadamard Transform
decoder [6], [7] for ﬁrst-order RM codes, Sidel’nikov-Pershakov algorithm and its variants [8], [9],
Dumer’s list decoding algorithm [10]–[12] and Recursive Projection-Aggregation algorithm [13] as well as
an algorithm based on minimum-weight parity checks [14]. Finally, the last category (Section V-C) again
only consists of a single decoding algorithm—a Berlekamp-Welch type decoding algorithm proposed
in [16]. This algorithm is designed for correcting random errors. Its performance guarantee (i.e., its
polynomial run-time estimate) was established for decoding RM codes of degrees up to r = o(
√m)
while all the previous decoding algorithms discussed in this section only have performance guarantee for
constant value of r (i.e., we do not have polynomial upper bounds on their run time at other regimes of
parameters). In fact, this algorithm also gives interesting results for degrees r = m − o(
√m/ log m).
 30

A. Reed’s algorithm [5]: Unique decoding up to half the code distance
In this section, we recap Reed’s decoding algorithm [5] for RM(m, r). It can correct any error pattern
with Hamming weight less than 2m−r−1, half the code distance.
For a subset A ⊆ [m], we write A = [m] \ A and we use VA := {z ∈ Fm
2 : zi = 0 ∀i ∈ A} to denote
the |A|-dimensional subspace of Fm
2 , i.e., VA is the subspace obtained by ﬁxing all zi’s to be 0 for i
outside of A. For a subspace VA in Fm
2 , there are 2m−|A| cosets of the form VA + b := {z + b : z ∈ VA},
where b ∈ Fm
2 . For any A ⊆ [m] and any b ∈ Fm
2 , we always have
∑

z∈(VA+b) Evalz(xA) = 1, (26)

and we also have that for any A ̸⊂ B, ∑

z∈(VA+b) Evalz(xB) = 0. (27)

The sums in (26)–(27) are both over F2. To see (26), notice that Evalz(xA) = 1 if and only if zi = 1
for all i ∈ A, and there is only one such z ∈ (VA + b). To see (27): Since A ̸⊆ B, there is i ∈
(A\B). The value of zi does not affect the evaluation Evalz(xB). Therefore, ∑
z∈(VA+b),zi=0 Evalz(xB) =∑
z∈(VA+b),zi=1 Evalz(xB), and (27) follows immediately.
Suppose that the binary vector y = (yz : z ∈ Fm
2 ) is a noisy version of a codeword Eval(f ) ∈ RM(m, r)
such that y and Eval(f ) differ in less than 2m−r−1 coordinates. Reed’s algorithm recovers the original
codeword from y by decoding the coefﬁcients of the polynomial f . Since deg(f ) ≤ r, we can always
write f = ∑
A⊆[m],|A|≤r uAxA, where uA’s are the coefﬁcients of the corresponding monomials. Reed’s
algorithm ﬁrst decodes the coefﬁcients of all the degree-r monomials, and then it decodes the coefﬁcients
of all the degree-(r − 1) monomials, so on and so forth, until it decodes all the coefﬁcients.
To decode the coefﬁcients uA for |A| = r, Reed’s algorithm ﬁrst calculates the sums ∑
z∈(VA+b) yz
over each of the 2m−r cosets of the subspace VA, and then it performs a majority vote among these 2m−r

sums: If there are more 1’s than 0’s, then we decode uA as 1. Otherwise we decode it as 0. Notice that
if there is no error, i.e., if y = Eval(f ), then we have
∑

z∈(VA+b) yz = ∑

z∈(VA+b) Evalz( ∑

B⊆[m],|B|≤r uBxB) = ∑

B⊆[m],|B|≤r uB ∑

z∈(VA+b) Evalz(xB).

According to (26)–(27), for the subsets B ⊆ [m] with |B| ≤ r = |A|, ∑
z∈(VA+b) Evalz(xB) = 1 if and
only if B = A. Therefore, ∑
z∈(VA+b) yz = uA for all the 2m−r cosets of the form VA +b if y = Eval(f ).
Since we assume that y and Eval(f ) differ in less than 2m−r−1 coordinates, there are less than 2m−r−1

cosets for which ∑
z∈(VA+b) yz ̸= uA. After the majority voting among these 2m−r sums, we will obtain
the correct value of uA.
After decoding all the coefﬁcients of the degree-r monomials, we can calculate

y′ = y − Eval( ∑

B⊆[m],|B|=r uBxB).

This is a noisy version of the codeword Eval(f − ∑
B⊆[m],|B|=r uBxB) ∈ RM(m, r − 1), and the number
of errors in y′ is less than 2m−r−1 by assumption. Now we can use the same method to decode the
coefﬁcients of all the degree-(r − 1) monomials from y′. We then repeat this procedure until we decode
all the coefﬁcients of f .

Theorem 23. For a ﬁxed r and growing m, Reed’s algorithm corrects any error pattern with Hamming
weight less than 2m−r−1 in O(n logr n) time when decoding RM(m, r).

Reed’s algorithm is summarized below:
 31

Algorithm 1 Reed’s algorithm for decoding RM(m, r)
Input: Parameters m and r of the RM code, and a binary vector y = (yz : z ∈ Fm
2 ) of length n = 2m

Output: A codeword c ∈ RM(m, r)

1: t ← r
2: while t ≥ 0 do
3: for each subset A ⊆ [m] with |A| = t do
4: Calculate ∑
z∈(VA+b) yz for all the 2m−t cosets of VA
5: num1 ← number of cosets (VA + b) such that ∑
z∈(VA+b) yz = 1

6: uA ← 1[num1 ≥ 2m−t−1]
7: end for
8: y ← y − Eval(∑
A⊆[m],|A|=t uAxA)
9: t ← t − 1
10: end while
11: c ← Eval(∑
A⊆[m],|A|≤r uAxA)
12: Output c

B. Practical algorithms for short to medium length RM codes
1) Fast Hadamard Transform (FHT) for ﬁrst order RM codes [6], [7]: The dimension of the ﬁrst order
RM code RM(m, 1) is m + 1, so there are in total 2m+1 = 2n codewords. A naive implementation of
the Maximum Likelihood (ML) decoder requires O(n2) operations. In this section we recap an efﬁcient
implementation of the ML decoder based on FHT which requires only O(n log n) operations. We will
focus on the soft-decision version of this algorithm, and the hard-decision version can be viewed as a
special case.
Consider a binary-input memoryless channel W : {0, 1} → W. The log-likelihood ratio (LLR) of an
output symbol x ∈ W is deﬁned as
 LLR(x) := ln ( W (x|0)
W (x|1)
 ).

We still use y = (yz : z ∈ Fm
2 ) to denote the noisy version of a codeword in RM(m, 1). Given the
channel output vector y, the ML decoder for ﬁrst order RM codes aims to ﬁnd c ∈ RM(m, 1) to
maximize ∏z∈Fm
2 W (yz|cz). This is equivalent to ﬁnding c which maximizes the following quantity:

∏

z∈F
m
2
 W (yz|cz)
√W (yz|0)W (yz|1) ,

which is further equivalent to maximizing
∑

z∈Fm
2 ln ( W (yz|cz)
√W (yz|0)W (yz|1)
 ). (28)

As the codeword c is a binary vector,

ln ( W (yz|cz)
√W (yz|0)W (yz|1)
 ) =
 { 1
2 LLR(yz) if cz = 0

− 1
2 LLR(yz) if cz = 1 .

From now on we will use the shorthand notation

Lz := LLR(yz),

and the formula in (28) can be written as 1
2
 ∑

z∈Fm
2
 ((−1)
cz Lz), (29)

32

so we want to ﬁnd c ∈ RM(m, 1) to maximize this quantity.
By deﬁnition, every c ∈ RM(m, 1) corresponds to a polynomial in F2[x1, x2, . . . , xm] of degree one, so
we can write every codeword c as a polynomial u0+∑m
i=1 uixi. In this way, we have cz = u0+∑m
i=1 uizi,
where z1, z2, . . . , zm are the coordinates of the vector z. Now our task is to ﬁnd u0, u1, u2, . . . , um ∈ F2
to maximize ∑

z∈Fm
2
 ((−1)
u0+
∑m
i=1 uiziLz) = (−1)
u0 ∑

z∈Fm
2
 ((−1)
∑m
i=1 uiziLz). (30)

For a binary vector u = (u1, u2, . . . , um) ∈ Fm
2 , we deﬁne

ˆL(u) := ∑

z∈Fm
2
 (
(−1)
∑m
i=1 uiziLz).

To ﬁnd the maximizer of (30), we only need to compute ˆL(u) for all u ∈ Fm
2 , but the vector ( ˆL(u) :
u ∈ Fm
2 ) is exactly the Hadamard Transform of the vector (Lz : z ∈ Fm
2 ), so it can be computed using
the Fast Hadamard Transform with complexity O(n log n). Once we know the values of ( ˆL(u), u ∈ Fm
2 ),
we can ﬁnd u∗ = (u∗
1, u∗
2, . . . , u∗
m) ∈ Fm
2 that maximizes | ˆL(u)|. If ˆL(u∗) > 0, then the decoder outputs
the codeword corresponding to u∗
0 = 0, u∗
1, u∗
2, . . . , u∗
m. Otherwise, the decoder outputs the codeword
corresponding to u∗
0 = 1, u∗
1, u∗
2, . . . , u∗
m. This completes the description of the soft-decision FHT decoder
for ﬁrst order RM codes.
The hard-decision FHT decoder is usually used for random errors, or equivalently, used for error
corrections over BSC. For BSC, the channel output y = (yz : z ∈ Fm
2 ) is a binary vector. Suppose that
the crossover probability of BSC is p < 1/2, then Lz = ln( 1−p
p ) if yz = 0, and Lz = − ln( 1−p
p ) if
yz = 1. Since rescaling the LLR vector by a positive factor does not change the maximizer of (30), we
can divide the LLR vector by ln( 1−p
p ) when decoding RM codes over BSC(p). This is equivalent to
setting Lz = 1 for yz = 0 and Lz = −1 for yz = 1. Then the rest of the hard-decision FHT decoding is
the same as the soft-decision version.

Theorem 24. The FHT decoder ﬁnds the ML decoding result in O(n log n) time when decoding ﬁrst
order RM codes.

FHT can also be used for list decoding of ﬁrst order RM codes. For list decoding with list size s, we
ﬁnd s vectors u(1), . . . , u(s) that give the largest values of | ˆL(u)| among all vectors in Fm
2 .
As a ﬁnal remark, we mention that ﬁrst order RM codes can also be decoded efﬁciently as geometry
codes [66].

Algorithm 2 FHT decoder for ﬁrst order RM codes
Input: Code length n = 2m, and the LLR vector (Lz : z ∈ Fm
2 ) of the received (noisy) codeword
Output: A codeword c ∈ RM(m, 1)

1: ( ˆL(u) : u ∈ Fm
2 ) ← FHT(Lz : z ∈ Fm
2 )
2: u∗ = (u∗
1, u∗
2, . . . , u∗
m) ← argmaxu∈Fm
2 | ˆL(u)|

3: if ˆL(u∗) > 0 then
4: c ← Eval(∑m
i=1 u∗
i xi)
5: else
6: c ← Eval(1 + ∑m
i=1 u∗
i xi)
7: end if
8: Output c

2) Sidel’nikov-Pershakov algorithm [8] and its variant [9]: In [8], Sidel’nikov and Pershakov proposed
a decoding algorithm that works well for second order RM codes with short or medium code length

33

(e.g. ≤ 1024). A version of their decoding algorithm also works for higher-order RM codes, but the
performance is not as good as the one for second order RM codes.
In this section, we recap Sidel’nikov-Pershakov algorithm for second order RM codes. Consider a
polynomial f ∈ F2[x1, . . . , xm] with deg(f ) ≤ 2:

f (z1, . . . , zm) = ∑

1≤i<j≤m ui,jzizj +
 m∑

i=1 uizi + u0.

For a vector b = (b1, . . . , bm) ∈ Fm
2 , we have

Evalz+b(f ) + Evalz(f ) = ∑

1≤i<j≤m ui,j(zi + bi)(zj + bj) + ∑

1≤i<j≤m ui,jzizj +
 m∑

i=1 uibi

= ∑

1≤i<j≤m ui,jzibj + ∑

1≤i<j≤m ui,jbizj + ∑

1≤i<j≤m ui,jbibj +
 m∑

i=1 uibi

=bU zT + ∑

1≤i<j≤m ui,jbibj +
 m∑

i=1 uibi, (31)

where the matrix U is deﬁned as

U :=
 






 0 u1,2 u1,3 . . . u1,m
u1,2 0 u2,3 . . . u2,m
u1,3 u2,3 0 . . . u3,m
... ... ... ... ...
u1,m u2,m u3,m . . . 0
 





 .

Note that Evalz+b(f ) + Evalz(f ) is the coordinate of the discrete derivative of f at direction b, as deﬁned
in (3).
We ﬁrst describe the decoder for BSC and then generalize it to other binary-input channels. Suppose
that we transmit the codeword c = Eval(f ) ∈ RM(m, 2) through some BSC, and we denote the channel
output vector as y ∈ Fn
2 . For a ﬁxed b, the vector (yz+b + yz : z ∈ Fm
2 ) is the noisy version of the
codeword in RM(m, 1) corresponding to the polynomial in (31). Note that the vector bU consist of the
coefﬁcients of all the degree-1 monomials in this polynomial. Therefore, we can decode bU from the
noisy codeword (yz+b + yz : z ∈ Fm
2 ). A naive way to do so is to decode each bU separately using
the FHT decoder for different vectors b ∈ Fm
2 . Sidel’nikov and Pershakov instead proposed to decode
bU for all b ∈ Fm
2 collectively: The ﬁrst step is to calculate s candidates for bU that have the largest
posterior probability by decoding (yz+b + yz : z ∈ Fm
2 ) with the FHT list decoder described at the end
of Section V-B1. We denote these s candidates as D(1)
b , . . . , D(s)
b and associate each of them with a
reliability value initialized as its posterior probability. Since bU = b′U + (b + b′)U for all b′ ∈ Fm
2 , the
correct candidates (D∗
b : b ∈ Fm
2 ) satisfy D∗
b = D∗
b′ + D∗
b+b′. In order to ﬁnd D∗
b , for each i = 1, . . . , s,
we check for all b′ ∈ Fm
2 whether there are certain i1 and i2 such that D(i)
b = D(i1)
b′ + D(i2)
b+b′. Each
time when we ﬁnd such b′ and i1, i2, we increase the reliability value of D(i)
b by some function12 of
the reliability values of D(i1)
b′ and D(i2)
b+b′. Finally, we set D∗
b to be D(i)
b with the largest reliability value
among all i = 1, . . . , s.
At this point, we have obtained D∗
b for all b ∈ Fm
2 . Notice that D∗
b is the noisy version of bU , and in
particular, the ﬁrst coordinate of D∗
b is the noisy version of u1,2b2 + u1,3b3 + · · · + u1,mbm. Therefore,
if we pick the ﬁrst coordinate of D∗
b for all b ∈ Fm
2 , we will obtain the noisy version of a codeword
from RM(m, 1), and this codeword is the evaluation vector of the polynomial u1,2x2 + u1,3x3 + · · · +
u1,mxm. After decoding this noisy codeword using the FHT decoder, we will obtain the coefﬁcients

12The choice of this function is somewhat ad hoc, and we omit the precise deﬁnition here.
 34

u1,2, u1,3, . . . , u1,m, which form the ﬁrst column of the matrix U . Similarly, we can also pick the ith
coordinate of D∗
b for all b ∈ Fm
2 and decode it with the FHT decoder. This will allow us to calculate
the ith column of U . Once we decode all the entries in U , we have the coefﬁcients of all the degree-2
monomials in f . Then we use the FHT decoder again to decode all the other coefﬁcients in f , which
gives us the ﬁnal decoding result.
For more general binary-input channels other than BSC, we are not able to calculate yz+b + yz since
the two summands are not binary any more. We instead work with the LLRs Lz := LLR(yz). Given
Lz+b and Lz, we want to estimate how likely Evalz+b(f ) + Evalz(f ) is 0 or 1. The LLR of the sum
Evalz+b(f ) + Evalz(f ) can be calculated as

ln ( exp (Lz+b + Lz) + 1) − ln ( exp(Lz) + exp(Lz+b)). (32)

Once we replace yz+b + yz with this LLR, we can follow the decoding procedure described above for
BSC to decode the output vector of more general binary-input channels.
In [8], Sidel’nikov and Pershakov showed that for second order RM codes RM(m, 2), their algorithm
can correct almost all error patterns with Hamming weight no more than (n − Cm1/4n3/4)/2 for any
constant C > ln 4 when the code length n → ∞.
In [9], Sakkour proposed a simpliﬁed and improved version of the Sidel’nikov-Pershakov algorithm
for decoding second order RM codes. The main change in Sakkour’s algorithm is to use a simple
majority voting to obtain D∗
b from Db, replacing the more complicated procedure in Sidel’nikov-Pershakov
algorithm. Such a simpliﬁcation also leads to smaller decoding error probability. We summarize Sakkour’s
algorithm below in Algorithm 3 since it is simpler and has better performance:

Algorithm 3 Sakkour’s algorithm for decoding second order RM codes over BSC
Input: The code length n = 2m; the received (noisy) codeword y = (yz : z ∈ Fm
2 );
Output: A codeword c ∈ RM(m, 2)

1: for every b ∈ Fm
2 do
2: Db ← FHT_Decoder(yz+b + yz : z ∈ Fm
2 ) ◃ FHT_Decoder for RM(m, 1)
3: end for
4: for every b ∈ Fm
2 do
5: D∗
b ← Majority(Db+b′ + Db′ : b′ ∈ Fm
2 )
6: ◃ Majority function picks the vector occurring the largest number of times
7: end for
8: for i = 1, 2, . . . , m do
9: Ei ← (the i-th coordiante of D∗
b : b ∈ Fm
2 ) ◃ Ei is a vector of length n

10: ˆEi ← FHT_Decoder(Ei) ◃ FHT_Decoder for RM(m, 1)
11: (u{i,j} : j ∈ [m] \ {i}) ← coefﬁcients of the polynomial corresponding to ˆEi
12: end for

13: y ← y − Eval(∑
A⊆[m],|A|=2 uAxA)

14: ˆD ← FHT_Decoder(y) ◃ FHT_Decoder for RM(m, 1)
15: (uA : A ⊆ [m], |A| ≤ 1) ← coefﬁcients of the polynomial corresponding to ˆD
16: c ← Eval(∑
A⊆[m],|A|≤2 uAxA)
17: Output c

3) Dumer’s recursive list decoding [10]–[12]: Dumer’s recursive list decoding makes use of the
Plotkin (u, u + v) construction of RM codes (see Section II-B for discussions), and it works well for
short or medium length RM codes. More precisely, for RM codes with length ≤ 256, Dumer’s recursive
list decoding algorithm can efﬁciently approach the decoding error probability of the ML decoder. For
code length 512 or 1024, Dumer’s algorithm works well for RM codes with low code rates. In [12],

35

Dumer and Shabunov also proposed to construct subcodes of RM codes that have better performance
than RM codes themselves under the recursive list decoding algorithm.
We start with the basic version of Dumer’s recursive decoding algorithm (without list decoding).
Suppose that we transmit a codeword c = Eval(f ) ∈ RM(m, r) through some binary-input channel W ,
and we denote the output vector as y and the corresponding LLR vector as L. The original codeword
Eval(f ) has two components Eval[zm=0](f ) and Eval[zm=1](f ). We also devide the LLR vector L into
two subvectors L[zm=0] and L[zm=1] in the same way so that L[zm=0] and L[zm=1] are the LLR vectors of
Eval[zm=0](f ) and Eval[zm=1](f ), respectively. We then construct the LLR vector of Eval[/zm](f ) from
L[zm=0] and L[zm=1] and we denote it as L[/zm]: Each coordinate of L[/zm] is obtained by combining the
corresponding coordinates in L[zm=0] and L[zm=1] using formula (32).
13

We ﬁrst decode Eval[/zm](f ) ∈ RM(m − 1, r − 1) from L[/zm] and denote the decoding result as ˆc[/zm].
Then we use ˆc[/zm] together with L[zm=0] and L[zm=1] to form an updated LLR vector of Eval[zm=0](f ),
which we denote as ˜L[zm=0]. The updating rule is as follows: For each z = (z1, . . . , zm−1) ∈ Fm−1
2 ,
if ˆc
[/zm]
z = 0, then we set ˜L[zm=0]
z = L
[zm=0]
z + L
[zm=1]
z , and if ˆc
[/zm]
z = 1, then we set ˜L
[zm=0]
z =
L
[zm=0]
z − L
[zm=1]
z . As the next step, we decode Eval[zm=0](f ) ∈ RM(m − 1, r) from ˜L[zm=0] and denote
the decoding result as ˆc[zm=0]. Finally, we combine ˆc[/zm] and ˆc[zm=0] to form the ﬁnal decoding result
ˆc = (ˆc[zm=0], ˆc[zm=0] + ˆc[/zm]).
In this recursive decoding algorithm, we decompose the decoding of RM(m, r) into two tasks: First, we
decode a codeword from RM(m − 1, r − 1). After that, we decode another codeword from RM(m − 1, r).
Then the decoding of RM(m − 1, r − 1) and RM(m − 1, r) are further decomposed into decoding another
four codewords from RM codes with shorter code length and smaller order. This decomposition procedure
continues until we reach codewords from ﬁrst order RM codes RM(i, 1) for some i or full RM codes
RM(j, j) for some j. For ﬁrst order RM codes we use the FHT decoder, and for full RM codes we simply
use the ML decoder. The summary of the algorithm and an illustration of how it works for RM(6, 2)
and RM(6, 3) are given in Fig. 5.
Next we brieﬂy discuss the recursive list decoding algorithm. In the list decoding version, we usually
stop at the zero order RM codes instead of the ﬁrst order ones 14. Note that the zero order RM codes
are simply repetition codes with dimension 1. We still go through the same procedure as illustrated in
Fig. 5, i.e., we keep decomposing the RM codes and eventually we only decode the RM codes on “leaf
nodes”. In the list decoding algorithm, the codes on “leaf nodes” are either repetition codes or full RM
codes. Each time when we decode a new leaf node, we examine several possible decoding results of
this new node for every candidate in the list: If this new leaf node is a repetition code, then there are
only two possible decoding results–all zero or all one; if this new leaf node is a full RM code, then we
take the 4 most likely decoding results of it for every candidate in the list. In this way, we will increase
the list size by a factor of 2 or 4 at each step, depending on whether the new leaf node is a repetition
code or a full RM code. We then calculate a reliability value for each candidate in the new list. When
the list size is larger than some pre-speciﬁed value µ, we prune the list down to size µ by only keeping
the candidates with the largest reliability values. Clearly, large µ leads to longer running time of the
algorithm but smaller decoding error probability.
In [12], a family of subcodes of RM codes were also proposed. The subcodes have smaller decoding
probability under the recursive list decoding algorithm. The idea is quite natural: Each repetition code
on the “leaf nodes” only contain one information bit. Some of these information bits are relatively noisy,
and the others are relatively noiseless. Dumer and Shabunov proposed to set all the noisy bits to be 0.
In this way, one can get smaller decoding error at the cost of decreasing the code rate.

13In [12], Dumer and Shabunov proposed to work with the quantity W (x|1) − W (x|0) instead of LLR, but one can show
that formula (32) for LLR is equivalent to the combining method in [12] expressed in terms of W (x|1) − W (x|0).
14In fact, stopping at ﬁrst order RM codes in list decoding allows one to achieve smaller decoding error probability than
stopping at zero order RM codes. In this paper, we only describe the version of list decoding stopping at zero order RM codes
for two reasons: First, it is easier to describe; second, this is the version presented in Dumer and Shabunov’s original paper [12,
Section III].
 36

Algorithm 4 Dumer’s Algorithm Φm
r for decoding RM(m, r)

Input: LLR vector L = (L[zm=0], L[zm=1])
Output: ˆc
1: if 1 < r < m then
2: Calculate L[/zm] from L[zm=0] and L[zm=1]

3: ˆc[/zm] ← Φm−1
r−1 (L[/zm])

4: Calculate ˜L[zm=0] from L[zm=0], L[zm=1] and ˆc[/zm]

5: ˆc[zm=0] ← Φm−1
r ( ˜L[zm=0])
6: ˆc ← (ˆc[zm=0], ˆc[zm=0] + ˆc[/zm])
7: else if r = 1 then
8: use FHT decoder
9: else if r = m then
10: use ML decoder
11: end if
 RM(6, 2)

RM(5, 1) RM(5, 2)

RM(4, 1) RM(4, 2)

RM(3, 1) RM(3, 2)

RM(2, 1) RM(2, 2)

RM(6, 3)

RM(5, 2) RM(5, 3)

RM(4, 1) RM(4, 2) RM(4, 2) RM(4, 3)

RM(3, 1) RM(3, 2) RM(3, 1) RM(3, 2) RM(3, 2) RM(3, 3)

RM(2, 1) RM(2, 2) RM(2, 1) RM(2, 2) RM(2, 1) RM(2, 2)

Fig. 5: The recursive decoding algorithm Φm
r for RM(m, r) and an illustration of how it works for
RM(6, 2) and RM(6, 3): We decompose RM(6, 2) and RM(6, 3) until we reach the leaf nodes, which
are the ﬁrst order or full RM codes marked in red. Eventually we only need to decode these RM codes
on the leaf nodes using FHT or ML decoders. The order of decoding these leaf nodes is indicated by
the red dashed arrows.
 37

Decode RM(m, 3)

Nmax
iterations
 Recursive
decoding

. . . . . .

. . . . . .

Projection

Aggregation

y

y[/B1] y[/B2] y[/Bn−1]

ˆy[/B1] ˆy[/B2] ˆy[/Bn−1]

ˆy
 Decode RM(m − 1, 2)

. . . . . .

y[/Bn−1]

ˆy[/Bn−1]

FHT FHT FHT
 Decode
RM(m − 2, 1) with
Fast Hadamard
Transform

Fig. 6: Recursive Projection-Aggregation decoding algorithm for third order RM codes

4) Recursive projection aggregation decoding [13]: The Recursive Projection Aggregation (RPA)
decoding algorithm was proposed recently by Ye and Abbe [13]. It works well for second and third
order RM codes with short or medium code length (e.g. ≤ 1024). In particular, the RPA algorithm can
efﬁciently achieve the same decoding error probability as the ML decoder for second order RM codes
with length ≤ 1024. Moreover, RPA decoder naturally allows parallel implementation.
We will focus mainly on the RPA decoder for BSC channels and brieﬂy mention how to adapt it
to general communication channels at the end of this section. In Section II-D, we have shown that
Eval[/p](f ) ∈ RM(m − 1, r − 1) whenever Eval(f ) ∈ RM(m, r) for any p = b1z1 + · · · + bmzm with
nonzero coefﬁcients b = (b1, . . . , bm) ̸= 0. Let B be the one-dimensional subspace of Fm
2 consisting of
the 0 vector and b. Then Eval[/p](f ) is obtained by taking the sums in each of the 2m−1 cosets of B,
i.e., each coordinate in Eval[/p](f ) is the sum ∑
z∈T Evalz(f ) for some coset T of B. For this reason,
we will use the two notations Eval[/B](f ) and Eval[/p](f ) interchangeably from now on. For a noisy
codeword y, we also use y[/B] and y[/p] interchangeably, and we call y[/B] the projection of y onto the
cosets of B. There are in total n − 1 one-dimensional subspaces in Fm
2 . We denote them as B1, . . . , Bn−1.
Suppose that we transmit a codeword c = Eval(f ) ∈ RM(m, r) through BSC, and that the channel
output is y. The RPA decoder for RM(m, r) consists of three steps: First, the projection step, then the
recursive decoding step, and third, the aggregation step. More precisely, the ﬁrst step is to project the
noisy codeword y onto all n − 1 one-dimensional subspaces B1, . . . , Bn−1. Note that this projection step
also appears in Sidel’nikov-Pershakov algorithm [8] and Sakkour’s algorithm [9];see Section V-B2. The
second step is to decode each y[/Bi] using the RPA decoder for RM(m − 1, r − 1). If r = 2, then we
simply use the FHT decoder for y[/Bi]. We denote the decoding result of the second step as ˆy[/Bi]. Note
that ˆy[/B1], . . . , ˆy[/Bn−1] consist of the (noisy) estimates of the sum Evalz(f ) + Evalz′(f ) for all z ̸= z′.
We denote the estimate of Evalz(f ) + Evalz′(f ) as ˆy(z,z′). Finally, in the aggregation step, observe that
ˆy(z,z′) + yz′ is an estimate of Evalz(f ) for all z′ ̸= z. For a ﬁxed z, we have in total n − 1 such estimates
of Evalz(f ), and we perform a majority vote among these n − 1 estimates to obtain ˆyz, i.e., we count
the number of 0’s and 1’s in the set {ˆy(z,z′) + yz′ : z′ ∈ Fm
2 , z′ ̸= z}: If there are more 1’s than 0’s, then
we set ˆyz to be 1. Otherwise, we set it to be 0. Next we replace the original channel output vector y
with ˆy = (ˆyz : z ∈ Fm
2 ), and run the Projection-Recursive decoding-Aggregation cycle again for a few

38

more rounds
15. The vector ˆy = (ˆyz : z ∈ Fm
2 ) in the last round is the ﬁnal decoding result of the RPA
decoder. See Fig. 6 for a high-level illustration of the RPA decoder.
For general communication channels we need to work with LLR, and we only need to make two changes
in the RPA decoder for BSC. The ﬁrst change is in the projection step: In order to calculate y[/B], we need
to calculate the sums yz + yz′ for the BSC case. We cannot do this for general communication channels
because the channel output vector is not binary anymore. Instead, we calculate the projected LLR vectors
L[/B] using (32), and in the recursive decoding step, we decode from L[/B1], . . . , L[/Bn−1]. The second
change is in the aggregation step: We replace the majority vote with a weighted sum of the LLRs. More
precisely, for a ﬁxed z, we calculate the sum ˆLz = 1
n−1 ∑
z′̸=z ˜y(z,z′)Lz′, where we set ˜y(z,z′) = 1 if
ˆy(z,z′) = 0 and ˜y(z,z′) = −1 if ˆy(z,z′) = 1. After each round, we replace the LLR vector of the original
channel output with ˆL = ( ˆLz : z ∈ Fm
2 ) and run the Projection-Recursive decoding-Aggregation cycle
again. After the last round, we decode ˆyz as 0 if ˆLz > 0 and otherwise we decode ˆyz as 1. The vector
ˆy = (ˆyz : z ∈ Fm
2 ) is the ﬁnal decoding result of the RPA decoder.
In practical implementation, we combine the RPA decoder with the following list decoding procedure
proposed by Chase [67] to boost the performance. We ﬁrst sort |Lz|, z ∈ Fm
2 from small to large. Assume
for example that |Lz1|, |Lz2|, |Lz3| are the three smallest components in the LLR vector, meaning that
yz1, yz2, yz3 are the three most noisy symbols in the channel outputs. Next we enumerate all 8 the possible
cases of these three bits: We set Lzi = ±Lmax for i = 1, 2, 3, where Lmax is some large real number.
In practice, we can choose Lmax := 2 max(|Lz| : z ∈ Fm
2 ). For each of these 8 cases, we use the RPA
decoder to obtain a decoded codeword (candidate). Finally, we calculate the posterior probability for each
of these 8 candidates, and choose the largest one as the ﬁnal decoding result, namely, we perform the
ML decoding among the 8 candidates in the list. This list decoding version of the RPA decoder allows
us to efﬁciently achieve the same decoding error probability as the ML decoder for second order RM
codes with length ≤ 1024.

Algorithm 5 RPA decoder for RM codes over BSC
Input: The parameters of the Reed-Muller code m and r; the received (noisy) codeword y = (yz : z ∈
Fm
2 ); the maximal number of iterations Nmax
Output: ˆy = (ˆyz : z ∈ Fm
2 ) ∈ Fn
2
1: for j = 1, 2, . . . , Nmax do
2: ˆy/Bi ← RPA(m − 1, r − 1, y/Bi, Nmax) for i = 1, 2, . . . , n − 1
3: {ˆy(z,z′) : z, z′ ∈ Fm
2 , z ̸= z′} ← coordinates of ˆy/B1, . . . , ˆy/Bn−1

4: for every z ∈ Fm
2 do
5: num1 ← number of z′ ∈ Fm
2 \ {z} such that ˆy(z,z′) + yz′ = 1

6: ˆyz ← 1[num1 > n−1
2 ]
7: end for
8: if y = ˆy then
9: break
10: end if
11: y ← ˆy
12: end for
13: Output ˆy

5) Additional methods [14], [15]: In [14], Santi et al. applied iterative decoding to a highly-redundant
parity-check (PC) matrix that contains only the minimum-weight dual codewords as rows. In particular,
[14] proposed to use the peeling decoder for the binary erasure channel, linear-programming and belief
propagation (BP) decoding for the binary-input additive white Gaussian noise channel, and bit-ﬂipping

15In practice, usually three rounds are enough for the algorithm to converge.
 39

and BP decoding for the binary symmetric channel. For short block lengths, it was shown that near-ML
performance can indeed be achieved in many cases. [14] also proposed a method to tailor the PC matrix to
the received observation by selecting only a small fraction of useful minimum-weight PCs before decoding
begins. This allows one to both improve performance and signiﬁcantly reduce complexity compared to
using the full set of minimum-weight PCs.
In [15], Mondelli et al. explored the relationship between polar and RM codes, and they proposed
a coding scheme which improves upon the performance of the standard polar codes at practical block
lengths. The starting point is the experimental observation that RM codes have a smaller error proba-
bility than polar codes under MAP decoding. This motivates one to introduce a family of codes that
“interpolates” between RM and polar codes, call this family Cinter = {Cα : α ∈ [0, 1]}, where Cα|α=1
is the original polar code, and Cα|α=0 is an RM code. Based on numerical observations, one can see
that the error probability under MAP decoding is an increasing function of α. MAP decoding has in
general exponential complexity, but empirically the performance of polar codes at ﬁnite block lengths is
boosted by moving along the family Cinter even under low-complexity decoding schemes such as belief
propagation or successive cancellation list decoder. Performance gain was also demonstrated in [15] via
numerical simulations for transmission over the erasure channel as well as the Gaussian channel.

C. Berlekamp-Welch type decoding algorithm [16]
In this section we explain the algorithm of Saptharishi, Shpilka and Volk [16] for decoding RM
codes of degrees up to r = o(√m). In fact, their algorithm also gives interesting results for degrees
r = m − o(√m/ log m). The algorithm is similar in spirit to the works of Pellikaan, Duursma and
K¨otter ([68], [69]), which abstract the Berlekamp-Welch algorithm. Thus, it is very different from the
algorithms given in the other subsections of Section V.
Before stating their main theorem we will need the following notation. For u, v ∈ Fn
q , we denote by
u∗v ∈ Fn
q the vector (u1v1, . . . , unvn). For A, B ⊆ Fn
q we similarly deﬁne A∗B = {u∗v | u ∈ A, v ∈ B}.
The algorithm considers three codes C, E and N , all subsets of Fn
q , such that E ∗ C ⊆ N , and is able
to correct in C error patterns that are correctable from erasures in N , through the use of an error-locating
code E.

Algorithm 6 Decoding Algorithm of [16]

Require: received word y ∈ Fn
q such that y = c + e, with c ∈ C and e is supported on a set U
1: Solve for a ∈ E, b ∈ N , the linear system a ∗ y = b.
2: Let {a1, . . . , ak} be a basis for the solution space of a, and let E denote the common zeros of
{ai | i ∈ [k]}.
3: For every j ∈ E, replace yj with ‘?’, to get a new word y′.
4: Correct y′ from erasures in C.

Theorem 25. Let Fq be a ﬁnite ﬁeld and E, C, N ⊆ Fn
q be codes with the following properties.
1) E ∗ C ⊆ N
2) For any pattern 1U that is correctable from erasures in N , and for any coordinate i ̸∈ U there
exists a codeword a ∈ E such that aj = 0 for all j ∈ U and ai = 1.
Then Algorithm 6 corrects in C any error pattern 1U which is correctable from erasures in N .

It is worth pointing out the differences between Algorithm 6 and the abstract Berlekamp-Welch decoder
of Pellikaan, Duursma and K¨otter [68], [69]. They similarly set up codes E, C and N such that E∗C ⊆ N .
However, instead of Property 2, they require that for any e ∈ E and c ∈ C, if e ∗ c = 0 then e = 0 or
c = 0 (or similar requirements regarding the distances of E and C that guarantee this property). This
property, as well as the distance properties, do not hold in the case of Reed-Muller codes, which is the
main application of Theorem 25.
 40

Proof Sketch. It is relatively easy to show that Property 2 in the statement of the theorem guarantees that
every erasure pattern that is correctable in N is also correctable in C. The main point of the algorithm
is that, under the hypothesis of the theorem, the common zeros of the possible solutions for a determine
exactly the error locations.
Denote y = c + e, where c ∈ C is the transmitted codeword and e is supported on the set of
error locations U . The following two claims guarantee that the algorithm correctly ﬁnds the set of error
locations. The ﬁrst claim shows that error locations are common zeros and the second claim shows that
no other coordinate is a common zero.

Claim 2. For every a ∈ E, b ∈ N such that a ∗ y = b, it holds that a ∗ e = 0.

Proof. Observe that a ∗ e = a ∗ y − a ∗ c is also a codeword in N . As a ∗ e is supported on U , and since
U is an erasure-correctable pattern in N , it must be the zero codeword.

Claim 3. For every i ̸∈ U there exists a ∈ E, b ∈ N such that a is 0 on U , ai = 1 and a ∗ y = b.

Proof. Property 2 implies that since U is correctable from erasures in N , for every i ̸∈ U we can pick
a ∈ E such that a is 0 on U and ai = 1. Set b = a ∗ y. As b = a ∗ c + a ∗ e = a ∗ c it follows that
b ∈ N .

Together, Claims 2 and 3 imply the correctness of the algorithm.

To apply Theorem 25 to RM codes we note that for m ∈ N and r ≤ m/2 − 1 the codes C =
RM(m, m − 2r − 2), N = RM(m, m − r − 1) and E = RM(m, r + 1) satisfy the conditions of Theo-
rem 25.
Theorem 18 shows that RM(m, m − r − 1) achieves capacity for r = m/2 ± O(
√m). Letting r =
m/2 − o(
√m) and looking at the code RM(m, m − 2r − 2) = RM(m, o(
√m)) so that ( m
≤r) = (1/2 −
o(1))2m, Saptharishi et al. obtained the following corollary to Theorem 25.

Corollary 3. There exists an efﬁcient (deterministic) algorithm that is able to correct a fraction of
(1/2 − o(1)) random errors in RM(m, o(
√m)), with probability 1 − o(1).

Similar arguments allow [16] to obtain results for high rate RM codes.

Theorem 26 (Theorem 2 of [16]). Let r = o(
√m/ log m). Then, there is an efﬁcient algorithm that can
correct RM(m, m − (2r + 2)) from a random set of (1 − o(1))
( m
≤r) errors. Moreover, the running time
of the algorithm is 2m · poly(
( m
≤r)).

In [70], Kopparty and Potukuchi improved the running time of the decoding algorithm of Theorem 26
to run in time polynomial in the length of the syndrome, that is in time poly(
( m
≤r)).

VI. OPEN PROBLEMS
A. RM codes and Twin-RM codes
As mentioned in Section IV-D, the twin-RM code, obtained by retaining the low-entropy components
of the squared RM code (proceeding in the RM ordering) is proved to achieve capacity on any BMS.
There are now three possible outcomes: (i) the twin-RM code is exactly the RM code, (ii) the twin-RM
code is equivalent to the RM code, in that only a vanishing fraction of rows selected by the two codes
are different, (iii) the twin-RM code is not equivalent to the RM code. If (i) or (ii) are true, the RM
code will also be capacity achieving for any BMS. If (iii) is true instead, then the RM code is not
capacity-achieving (for the considered BMS channel).

Conjecture 1. The twin-RM code is the RM code, i.e., with the notation of Section IV-D where U n =
RnX n and Rn is the squared RM code matrix, for i, j ∈ [n],

|Ai| > |Aj| =⇒ H(Ui|U i−1, Y n) ≥ H(Uj|U j−1, Y n), (33)

41

in words, the conditional entropy is non-decreasing as we go to lower degree layers.

Using the symmetry of RM codes, [4] shows that this is implied by the following conjecture.

Conjecture 2. Let i be the index of the last row in a layer of Rn (besides the last layer), then

H(Ui|U i−1, Y n) ≥ H(Ui+1|U i, Y n), (34)

in words, the conditional entropy is non-decreasing as we cross layers.

Finally, since the RM code construction is the same for the BEC, the BSC or any other channel, and
since it is already proved to achieve capacity on the BEC [3], it follows that the RM and twin-RM codes
must be equivalent on the BEC. Consequently, we have the following conjecture that also implies that
RM codes achieve capacity on the BSC.

Conjecture 3. The Twin-RM codes for the BEC and BSC are equivalent. I.e., for some ϵ = o(1/n),
|{i ∈ [n] : H(Ui|U i−1, Y n
BSC) ≤ ϵ, H(Ui|U i−1, Y n
BEC) ≥ ϵ}| = o(n).

One could also exploit the ordering between BEC and BSC entropies, showing that for any two
indices i, j of rows with j in a lower degree layer than i, H(Ui|U i−1, Y n
BEC) ≥ H(Uj|U j−1, Y n
BEC)
implies H(Ui|U i−1, Y n
BSC) ≥ H(Uj|U j−1, Y n
BSC). Finally, one may also look for a BMS channel such
that the Twin-RM code is not equivalent to the RM code, which would imply that the RM code does
not achieve capacity for this BMS.

B. Weight enumerator
1. Uniﬁed bounds for two different regimes
As mentioned in Section III, we now have two different approaches to bound the number of codewords
in two different regimes. More precisely, the method proposed in [35] gives strong and in some cases
nearly optimal bounds in the constant relative weight regime for constant rate codes. Yet this method
does not produce meaningful bound when the code rate approaches 0 or in the small weight regime. On
the other hand, the method in [2] gives good bound for small rate codes or in small weight regime, but
it does not work well in the linear weight regime for constant rate codes. A natural open problem is thus
to obtain a uniﬁed bound that is effective in both regimes.

2. Use the capacity-achieving results for BEC to prove the conjecture for BSC
As discussed in Section III, Samorodnitsky gave a nearly optimal upper bound in a certain linear
weight regime for any code that achieves capacity for the BEC. This in particular means that the weight
distribution of RM codes in this regime is (nearly) the same as that of random codes. Since random
codes achieve capacity of BSC, can we thus extend this result to prove that RM codes achieve capacity
on the BSC?

3. Close the gap between the upper and lower bounds for small weight codewords
There is a gap between the existing upper and lower bounds on small weight codewords; see Theorem 7
and Theorem 9. A natural open problem is to close this gap.

C. Algorithms
Another open problem is to develop an efﬁcient (polynomial time) decoder for the twin-RM codes.
Similarly to polar codes, twin-RM codes are also suitable for successive decoding by construction.
Moreover, both twin-RM codes and polar codes have similar but different recursive structures that can be
used to reduce the complexity of the successive decoder. The difference is that the recursive structure of
polar codes allows for an FFT-like implementation of the successive decoder which only has O(N log N )
complexity [38]. On the other hand, the naive utilization of the recursive structure of twin-RM codes
does not give such an obvious reduction. The hope is to still ﬁnd a more efﬁcient (polynomial-time)

42

implementation of the successive decoder for twin-RM codes based on a divide-and-conquer method.

The results of [2], as described in Section IV-A, show that RM(m, m/2 − O(√m log m)) can correct
a fraction of 1/2−o(1) random errors. Currently, the best algorithm that we have can only handle degrees
up to o(
√m) [16] (see Section V-C). It is a natural open problem to extend these up to any constant
fraction of errors.
 REFERENCES

[1] E. Abbe, A. Shpilka, and A. Wigderson, “Reed–Muller codes for random erasures and errors,” IEEE Transactions on
Information Theory, vol. 61, no. 10, pp. 5229–5252, 2015.
[2] O. Sberlo and A. Shpilka, “On the performance of Reed-Muller codes with respect to random errors and erasures,”
arXiv:1811.12447, 2018.
[3] S. Kudekar, S. Kumar, M. Mondelli, H. D. Pﬁster, E. S¸ as¸o˘glu, and R. Urbanke, “Reed-Muller codes achieve capacity on
erasure channels,” in Proceedings of the forty-eighth annual ACM Symposium on Theory of Computing (STOC). ACM,
2016, pp. 658–669.
[4] E. Abbe and M. Ye, “Reed-Muller codes polarize,” in 2019 IEEE 60th Annual Symposium on Foundations of Computer
Science (FOCS). IEEE, 2019, pp. 273–286.
[5] I. Reed, “A class of multiple-error-correcting codes and the decoding scheme,” Transactions of the IRE Professional Group
on Information Theory, vol. 4, no. 4, pp. 38–49, 1954.
[6] R. R. Green, “A serial orthogonal decoder,” JPL Space Programs Summary, vol. 37, pp. 247–253, 1966.
[7] Y. Be’ery and J. Snyders, “Optimal soft decision block decoders based on fast Hadamard transform,” IEEE transactions
on information theory, vol. 32, no. 3, pp. 355–364, 1986.
[8] V. M. Sidel’nikov and A. S. Pershakov, “Decoding of Reed-Muller codes with a large number of errors,” Problemy peredachi
informatsii, vol. 28, no. 3, pp. 80–94, 1992.
[9] B. Sakkour, “Decoding of second order Reed-Muller codes with a large number of errors,” in IEEE Information Theory
Workshop, 2005. IEEE, 2005, pp. 176–178.
[10] I. Dumer, “Recursive decoding and its performance for low-rate Reed-Muller codes,” IEEE Transactions on Information
Theory, vol. 50, no. 5, pp. 811–823, 2004.
[11] ——, “Soft-decision decoding of Reed-Muller codes: A simpliﬁed algorithm,” IEEE transactions on information theory,
vol. 52, no. 3, pp. 954–963, 2006.
[12] I. Dumer and K. Shabunov, “Soft-decision decoding of Reed-Muller codes: Recursive lists,” IEEE Transactions on
information theory, vol. 52, no. 3, pp. 1260–1266, 2006.
[13] M. Ye and E. Abbe, “Recursive projection-aggregation decoding of Reed-Muller codes,” in 2019 IEEE International
Symposium on Information Theory (ISIT), July 2019, pp. 2064–2068.
[14] E. Santi, C. Hager, and H. D. Pﬁster, “Decoding Reed-Muller codes using minimum-weight parity checks,” in 2018 IEEE
International Symposium on Information Theory (ISIT). IEEE, 2018, pp. 1296–1300.
[15] M. Mondelli, S. H. Hassani, and R. L. Urbanke, “From polar to Reed-Muller codes: A technique to improve the ﬁnite-length
performance,” IEEE Transactions on Communications, vol. 62, no. 9, pp. 3084–3091, 2014.
[16] R. Saptharishi, A. Shpilka, and B. L. Volk, “Efﬁciently decoding Reed–Muller codes from random errors,” IEEE
Transactions on Information Theory, vol. 63, no. 4, pp. 1954–1960, 2017.
[17] C. E. Shannon, “A mathematical theory of communication,” Bell system technical journal, vol. 27, no. 3, pp. 379–423,
1948.
[18] R. W. Hamming, “Error detecting and error correcting codes,” The Bell system technical journal, vol. 29, no. 2, pp.
147–160, 1950.
[19] F. J. MacWilliams and N. J. A. Sloane, The theory of error-correcting codes. Elsevier, 1977.
[20] J. H. van Lint, Introduction to coding theory. Springer, 1999.
[21] R. E. Blahut, Algebraic codes for data transmission. Cambridge university press, 2003.
[22] T. Helleseth, T. Kløve, and V. I. Levenshtein, “Error-correction capability of binary linear codes,” IEEE Transactions on
Information Theory, vol. 51, no. 4, pp. 1408–1423, 2005.
[23] T. Richardson and R. Urbanke, Modern coding theory. Cambridge university press, 2008.
[24] W. C. Huffman and V. Pless, Fundamentals of error-correcting codes. Cambridge university press, 2010.
[25] S. Yekhanin, “Locally decodable codes,” Foundations and Trends R⃝ in Theoretical Computer Science, vol. 6, no. 3, pp.
139–255, 2012.
[26] D. E. Muller, “Application of Boolean algebra to switching circuit design and to error detection,” Transactions of the IRE
professional group on electronic computers, no. 3, pp. 6–12, 1954.
[27] T. Helleseth, T. Kløve, and V. I. Levenshtein, “The simplex codes and other even-weight binary linear codes for error
correction,” IEEE transactions on information theory, vol. 50, no. 11, pp. 2818–2823, 2004.
[28] D. J. Costello and G. D. Forney, “Channel coding: The road to channel capacity,” Proceedings of the IEEE, vol. 95, no. 6,
pp. 1150–1177, 2007.
[29] S. Kudekar, S. Kumar, M. Mondelli, H. D. Pﬁster, E. S¸ as¸o?lu, and R. Urbanke, “Reed–Muller codes achieve capacity on
erasure channels,” IEEE Transactions on Information Theory, vol. 63, no. 7, pp. 4298–4316, 2017.
 43

[30] H. Hassani, S. Kudekar, O. Ordentlich, Y. Polyanskiy, and R. Urbanke, “Almost optimal scaling of Reed-Muller codes
on BEC and BSC channels,” in 2018 IEEE International Symposium on Information Theory (ISIT). IEEE, 2018, pp.
311–315.
[31] N. Sloane and E. Berlekamp, “Weight enumerator for second-order Reed-Muller codes,” IEEE Transactions on Information
Theory, vol. 16, no. 6, pp. 745–751, 1970.
[32] T. Kasami and N. Tokura, “On the weight structure of reed-muller codes,” IEEE Transactions on Information Theory,
vol. 16, no. 6, pp. 752–759, 1970.
[33] T. Kasami, N. Tokura, and S. Azumi, “On the weight enumeration of weights less than 2.5 d of reed-muller codes,”
Information and control, vol. 30, no. 4, pp. 380–395, 1976.
[34] T. Kaufman, S. Lovett, and E. Porat, “Weight distribution and list-decoding size of Reed–Muller codes,” IEEE Transactions
on Information Theory, vol. 58, no. 5, pp. 2689–2696, 2012.
[35] A. Samorodnitsky, “An upper bound on ℓq norms of noisy functions,” IEEE Transactions on Information Theory, pp.
1–1, 2019. [Online]. Available: https://ieeexplore.ieee.org/document/8853269
[36] S. Lin, “RM codes are not so bad,” in IEEE Inform. Theory Workshop, 1993, invited talk.
[37] I. Dumer and P. Farrell, “Erasure correction performance of linear block codes,” in Workshop on Algebraic Coding.
Springer, 1993, pp. 316–326.
[38] E. Arıkan, “Channel polarization: A method for constructing capacity-achieving codes for symmetric binary-input
memoryless channels,” IEEE Transactions on Information Theory, vol. 55, no. 7, pp. 3051–3073, 2009.
[39] E. Arikan, “A survey of Reed-Muller codes from polar coding perspective,” in 2010 IEEE Information Theory Workshop
on Information Theory (ITW 2010, Cairo). IEEE, 2010, pp. 1–5.
[40] C. Carlet and P. Gaborit, “On the construction of balanced Boolean functions with a good algebraic immunity,” in
Proceedings. International Symposium on Information Theory, 2005. ISIT 2005. IEEE, 2005, pp. 1101–1105.
[41] F. Didier, “A new upper bound on the block error probability after decoding over the erasure channel,” IEEE Transactions
on Information Theory, vol. 52, no. 10, pp. 4496–4503, 2006.
[42] S. H. Hassani, K. Alishahi, and R. L. Urbanke, “Finite-length scaling for polar codes,” IEEE Transactions on Information
Theory, vol. 60, no. 10, pp. 5875–5898, 2014.
[43] “Final report of 3GPP TSG RAN WG1 #87 v1.0.0,” http://www.3gpp.org/ftp/tsg ran/WG1 RL1/TSGR1 87/Report/.
[44] S. Lin and D. J. Costello, Error control coding. Prentice hall, 2001.
[45] I. Ben-Eliezer, R. Hod, and S. Lovett, “Random low-degree polynomials are hard to approximate,” computational
complexity, vol. 21, no. 1, pp. 63–81, 2012.
[46] P. Beame, S. O. Gharan, and X. Yang, “On the bias of reed-muller codes over odd prime ﬁelds,” arXiv preprint
arXiv:1806.06973, 2018.
[47] L. Gross, “Logarithmic sobolev inequalities,” American Journal of Mathematics, vol. 97, no. 4, pp. 1061–1083, 1975.
[48] V. K. Wei, “Generalized Hamming weights for linear codes,” IEEE Transactions on Information Theory, vol. 37, no. 5,
pp. 1412–1418, 1991. [Online]. Available: http://dx.doi.org/10.1109/18.133259
[49] J. Kahn, G. Kalai, and N. Linial, “The inﬂuence of variables on boolean functions,” in Proceedings of the 29th Annual
Symposium on Foundations of Computer Science. IEEE Computer Society, 1988, pp. 68–80.
[50] J. Bourgain, J. Kahn, G. Kalai, Y. Katznelson, and N. Linial, “The inﬂuence of variables in product spaces,” Israel Journal
of Mathematics, vol. 77, no. 1-2, pp. 55–64, 1992.
[51] M. Talagrand, “On Russo’s approximate zero-one law,” The Annals of Probability, vol. 22, no. 3, pp. 1576–1587, 1994.
[52] E. Friedgut and G. Kalai, “Every monotone graph property has a sharp threshold,” Proceedings of the American
mathematical Society, vol. 124, no. 10, pp. 2993–3002, 1996.
[53] S. ten Brink, “Convergence of iterative decoding,” Electronics letters, vol. 35, no. 10, pp. 806–808, 1999.
[54] A. Ashikhmin, G. Kramer, and S. ten Brink, “Extrinsic information transfer functions: Model and erasure channel
properties,” IEEE Transactions on Information Theory, vol. 50, no. 11, pp. 2657–2673, 2004.
[55] C. M´easson, A. Montanari, and R. Urbanke, “Maxwell construction: The hidden bridge between iterative and maximum a
posteriori decoding,” IEEE Transactions on Information Theory, vol. 54, no. 12, pp. 5277–5307, 2008.
[56] G. A. Margulis, “Probabilistic characteristics of graphs with large connectivity,” Problemy peredachi informatsii, vol. 10,
no. 2, pp. 101–108, 1974.
[57] L. Russo, “An approximate zero-one law,” Probability Theory and Related Fields, vol. 61, no. 1, pp. 129–139, 1982.
[58] S. Boucheron, G. Lugosi, and P. Massart, Concentration inequalities: A nonasymptotic theory of independence. Oxford
university press, 2013.
[59] R. O’Donnell, Analysis of boolean functions. Cambridge University Press, 2014.
[60] J. Bourgain and G. Kalai, “Inﬂuences of variables and threshold intervals under group symmetries,” Geometric and
Functional Analysis, vol. 7, no. 3, pp. 438–461, 1997.
[61] C. M´easson, A. Montanari, T. J. Richardson, and R. Urbanke, “The generalized area theorem and some of its consequences,”
IEEE Transactions on Information Theory, vol. 55, no. 11, pp. 4793–4821, 2009.
[62] I. Tal and A. Vardy, “How to construct polar codes,” IEEE Transactions on Information Theory, vol. 59, no. 10, pp.
6562–6582, 2013.
[63] ——, “List decoding of polar codes,” IEEE Transactions on Information Theory, vol. 61, no. 5, pp. 2213–2226, 2015.
[64] J. Błasiok, V. Guruswami, P. Nakkiran, A. Rudra, and M. Sudan, “General strong polarization,” in Proceedings of the 50th
Annual ACM SIGACT Symposium on Theory of Computing. ACM, 2018, pp. 485–492.
[65] A. Wyner and J. Ziv, “A theorem on the entropy of certain binary sequences and applications–Part I,” IEEE Transactions
on Information Theory, vol. 19, no. 6, pp. 769–772, 1973.
 44

[66] L. G. Tallini and B. Bose, “Reed-Muller codes, elementary symmetric functions and asymmetric error correction,” in 2011
IEEE International Symposium on Information Theory Proceedings. IEEE, 2011, pp. 1051–1055.
[67] D. Chase, “Class of algorithms for decoding block codes with channel measurement information,” IEEE Transactions on
Information Theory, vol. 18, no. 1, pp. 170–182, 1972.
[68] R. Pellikaan, “On decoding by error location and dependent sets of error positions,” Discrete Mathematics, vol. 106-107,
pp. 369–381, 1992. [Online]. Available: http://dx.doi.org/10.1016/0012-365X(92)90567-Y
[69] I. M. Duursma and R. K¨otter, “Error-locating pairs for cyclic codes,” IEEE Transactions on Information Theory, vol. 40,
no. 4, pp. 1108–1121, 1994. [Online]. Available: http://dx.doi.org/10.1109/18.335964
[70] S. Kopparty and A. Potukuchi, “Syndrome decoding of reed-muller codes and tensor decomposition over ﬁnite
ﬁelds,” in Proceedings of the Twenty-Ninth Annual ACM-SIAM Symposium on Discrete Algorithms, SODA 2018,
New Orleans, LA, USA, January 7-10, 2018, A. Czumaj, Ed. SIAM, 2018, pp. 680–691. [Online]. Available:
https://doi.org/10.1137/1.9781611975031.44
