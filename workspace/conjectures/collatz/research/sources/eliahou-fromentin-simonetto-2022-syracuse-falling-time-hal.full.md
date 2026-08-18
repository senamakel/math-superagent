<!-- source: https://hal.science/hal-03294829v3/file/falling%20time.pdf | converted from PDF -->

HAL Id: hal-03294829

https://hal.science/hal-03294829v3

Preprint submitted on 25 Aug 2021 (v3), last revised 18 Oct 2021 (v4)

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

HAL Authorization

Is the Syracuse falling time bounded by 12?

Shalom Eliahou, Rénald Simonetto

To cite this version:

Shalom Eliahou, Rénald Simonetto. Is the Syracuse falling time bounded by 12?. 2021. ⟨hal-03294829v3⟩

Is the Syracuse falling time bounded by 12?

Shalom Eliahou∗ and R´enald Simonetto
†

Abstract
Let T : N → N denote the 3x+1 function, where T (n) = n/2 if n is
even, T (n) = (3n+1)/2 if n is odd. As an accelerated version of T , we
deﬁne a jump at n ≥ 1 by jp(n) = T (ℓ)(n), where ℓ is the number of
digits of n in base 2. We present computational and heuristic evidence
leading to surprising conjectures. The boldest one states that for any
n ≥ 2150, at most four jumps starting from n are needed to fall below
n, a strong form of the Collatz conjecture.

Keywords. Collatz conjecture, 3x + 1 problem, stopping time,
glide record, jump function.

1 Introduction

We denote by N the set of positive integers. Let T : N → N be the notorious
3x + 1 function, deﬁned by T (n) = n/2 if n is even, T (n) = (3n + 1)/2 if n
is odd. For k ≥ 0, denote by T (k) the kth iterate of T . The orbit of n under
T is the sequence OT (n) = (n, T (n), T (2)(n), . . . ).

The famous Collatz conjecture states that for all n ≥ 1, there exists r ≥ 1
such that T (r)(n) = 1. The least such r is denoted σ∞(n) and called the total
stopping time of n. An equivalent version of the Collatz conjecture states
that for all n ≥ 2, there exists s ≥ 1 such that T (s)(n) < n. The least such s
is denoted by σ(n) and called the stopping time of n. For instance, we have

σ(n) =
 {
1 if n is even,
2 if n ≡ 1 mod 4, (1)

∗eliahou@univ-littoral.fr
†renalds@microsoft.com
 1

as is well known and easy to check. A stopping time record is an integer
n ≥ 2 such that σ(m) < σ(n) for all 2 ≤ m ≤ n − 1.
For the original slower version C : N → N, where C(n) = n/2 or 3n + 1
according as n is even or odd, the analog of the stopping time is called the
glide in [5]. The list of all currently known glide records, complete up to
at least 260, is maintained in [6]. It is quite likely that glide records and
stopping time records coincide; we have veriﬁed it by computer up to 232.
It is well known that σ(n) is unbounded as n grows. For instance, since

T (ℓ)(2
ℓ − 1) = 3ℓ − 1, (2)

as follows from the formula T (2a3
b − 1) = 2a−13
b+1 − 1 for a ≥ 1, we have
σ(2
ℓ − 1) ≥ ℓ for all ℓ ≥ 2.
In this paper, we propose an accelerated version of the function T . The
idea, somewhat as in [7], is to apply an iterate of T to n depending on the
number of digits of n in base 2. Accordingly, we introduce the following
function.

Deﬁnition 1.1 The jump function jp : N → N is deﬁned for n ∈ N by

jp(n) = T (ℓ)(n),

where ℓ = ⌊log2(n) + 1⌋ is the number of digits of n in base 2.

Example 1.2 We have jp(1) = T (1)(1) = 2, and jp(2) = T (2)(2) = 2 since 2
is of length ℓ = 2 in base 2. For n = 27, written 11011 in base 2, hence of
length ℓ = 5, we have jp(27) = T (5)(27) = 71. In turn, 71 is of length ℓ = 7
in base 2 since 2
6 ≤ 71 < 2
7, whence jp(71) = T (7)(71) = 137. The orbit of
27 under jumps is displayed below in (4).

Example 1.3 A single jump at n = 2
ℓ − 1 with ℓ ≥ 1 yields

jp(2
ℓ − 1) = 3ℓ − 1. (3)

This follows from the equalities ℓ = ⌊log2(2
ℓ − 1) + 1⌋ and (2).

Example 1.4 We have jp(2n) = jp(n) for all n ≥ 1, since 2n is of length
one more than n in base 2.

In analogy with the stopping time relative to T , we now introduce the
falling time relative to jumps. As jp(1) = jp(2) = 2, we only consider n ≥ 3.

2

Deﬁnition 1.5 Let n ≥ 3. The falling time of n, denoted ft(n), is the least
k ≥ 1 such that jp
(k)(n) < n, or ∞ if there is no such k.

There is no tight comparison between stopping time and falling time. It
may happen that σ(a) < σ(b) whereas ft(a) > ft(b). For instance, for a = 41
and b = 43, we have
 σ(41) = 2 < σ(43) = 5,
ft(41) = 8 > ft(43) = 2.

It may also happen that ft(n) > σ(n), as shown by the case n = 41.

Of course, the Collatz conjecture is equivalent to ft(n) < ∞ for all n ∈ N.
In Section 2, we provide computational evidence leading us to a stronger
conjecture, namely that ft(n) is in fact bounded for all n ≥ 3. Speciﬁcally,
all integers n we have tested so far satisfy ft(n) ≤ 15. See Conjecture 2.3. In
Section 3, in analogy with the falling time, we introduce the Syracuse falling
time sft(n), and corresponding conjectures, by only considering the odd terms
in the orbits OT (n). In Section 4, we report surprising computational results
on ft(2
ℓ − 1) and sft(2
ℓ − 1) for ℓ ≤ 100 000, and we formulate corresponding
conjectures. In the last Section 5, inspired by the case n = 2ℓ − 1, we
formulate still stronger conjectures on ft(n) and sft(n) for very large integers
n. We conclude the paper with some supporting heuristics.
For a wealth of information, developments and commented references
related to the 3x + 1 problem, see the webpage and book of J. C. Lagarias [3,
4]. To date, the Collatz conjecture has been veriﬁed by computer up to 2
68

by D. Barina [1]. Using this bound, it follows from [2] that any non-trivial
cycle of T must have length at least 114 208 327 604.

2 Falling time records

In this section, we only consider those positive integers n satisfying σ(n) ≥ 3,
i.e. such that n ≡ 3 mod 4 by (1). Let us denote by 4N + 3 the set of
those integers. Here is our ﬁrst computational evidence that the falling time
remains small.

Proposition 2.1 We have ft(n) ≤ 14 for all n ∈ [1, 2
35 − 1] such that
n ≡ 3 mod 4.
 3

Proof. With Mathematica 12 [9], in a few days of home computer time.

As shown in Table 1, the smallest n ∈ 4N+3 such that ft(n) ≥ 14, namely
n = 12 235 060 455, actually satisﬁes ft(n) = 14 and exceeds 233.

Deﬁnition 2.2 A falling time record is an integer n ∈ 4N + 3 such that
ft(m) < ft(n) for all m ∈ 4N + 3 with m < n.

n ≡ 3 mod 4 ⌊log2(n) + 1⌋ ft(n)
3 2 2
7 3 3
27 5 8
60 975 16 9
1 394 431 21 10
6 649 279 23 11
63 728 127 26 13
12 235 060 455 34 14

Table 1: Falling time records up to 2
35

The list of falling time records up to 235 is given in Table 1. It was built
while establishing Proposition 2.1. For instance, we have ft(3) = 2, ft(7) = 3
and ft(n) ≤ 3 for all 3 ≤ n < 27 such that n ≡ 3 mod 4. The value ft(27) = 8
follows from the fact that 8 jumps are needed from 27 to fall below it, as
shown by the orbit of 27 under jumps:

Ojp(27) = (27, 71, 137, 395, 566, 3 644, 650, 53, 8, 2, 2, . . . ). (4)

Interestingly, ﬁve of the falling time records in Table 1 are also glide records,
namely 3, 7, 27, 63 728 127 and 12 235 060 455, as seen by consulting [6].
Table 1 shows that the number 12 and a few smaller ones fail to occur as
falling time records. One may then wonder about the smallest n ∈ 4N + 3
reaching ft(n) = 12.
The answer is to be found in Table 2. Let us deﬁne a new falling time as
an integer n ∈ 4N + 3 such that ft(n) is distinct from ft(m) for all smaller
m ∈ 4N + 3. Of course, every falling time record is a new falling time. The
list of new falling times we know so far, which are not already falling time
records, is given in Table 2.
 4

n 111 103 71 55 217 740 015
ft(n) 4 5 6 7 12

Table 2: Some new falling times

To date, we only know two integers n such that ft(n) exceeds 14, and they
just reach ft(n) = 15. These two integers are displayed in Section 2.1, under
the names g30 and g32. We do not know whether g30, the smaller one and
greater than 2
48, is a falling time record. Now, is the inequality ft(n) ≥ 16
reachable? We do not know either, but a negative answer would constitute
a strong positive solution of the Collatz conjecture.

2.1 From Roosendaal’s website

Eric Roosendaal maintains the list of all currently known glide records [6],
complete up to at least 260. At the time of writing, there are 34 of them,
denoted g1, . . . , g34 below. As noted in [6], only the ﬁrst 32 ones have been
independently checked. The ten biggest are displayed in descending order in
Table 3. It turns out that
 ft(g1), . . . , ft(g34) ≤ 15.

Moreover, the highest value ft(n) = 15 is only reached by g30 and g32. As
mentioned above, we do not know whether ft(n) ≥ 16 is at all reachable.
This leads us to the following conjecture, a strong version of the Collatz
conjecture.

Conjecture 2.3 There exists B ≥ 15 such that ft(n) ≤ B for all n ≥ 3.

An even bolder conjecture would be to take B = 15 in Conjecture 2.3.

2.2 A variant of jumps

Let h ∈ N. For all n ∈ N, we deﬁne

jph(n) = T (hℓ)(n)

where, as before, ℓ is the number of digits of n in base 2. This is not the
same, of course, as the h-iterate jp(h)(n). Note also that for h = 1, we recover

5

n ⌊log2(n) + 1⌋ glide of n σ(n) ft(n)
g34 2 602 714 556 700 227 743 61 1 639 1005 13
g33 1 236 472 189 813 512 351 60 1 614 990 14
g32 180 352 746 940 718 527 57 1 575 966 15
g31 118 303 688 851 791 519 56 1 471 902 12
g30 1 008 932 249 296 231 49 1 445 886 15
g29 739 448 869 367 967 49 1 187 728 12
g28 70 665 924 117 439 46 1 177 722 13
g27 31 835 572 457 967 44 1 161 712 13
g26 13 179 928 405 231 43 1 122 688 14
g25 2 081 751 768 559 40 988 606 12

Table 3: Top ten known glide records

jumps, i.e. jp1(n) = jp(n). For n ≥ 3, the h-falling time fth(n) is deﬁned
correspondingly, as the smallest k ≥ 1, if any, such that ft
(k)
h (n) < n.
It turns out that for h = 18, and for the glide records g1, . . . , g34, we have

ft18(gi) = 1

for all 1 ≤ i ≤ 34. In view of that fact, is it conceivable that ft18(n) = 1 for
all n ≥ 3? We do not know. But this cannot be outright dismissed, given
the conjectural behavior of ft(n) for very large n as discussed in Section 5.
On the other hand, uncovering any counterexample would be quite a feat.

3 The Syracuse version

Let O = 2N + 1 denote the set of odd positive integers. Another well-studied
version of the 3x + 1 function is syr : O → O, deﬁned on any n ∈ O by

syr(n) = (3n + 1)/2
ν,

where ν ≥ 1 is the largest integer such that 2ν divides 3n + 1. Thus syr(n) is
the largest odd factor of 3n + 1. This speciﬁc version is called the Syracuse
function in [7].

In analogy with the functions jp(n) and ft(n) related to the 3x+1 function
T , we now introduce the corresponding functions sjp(n) and sft(n) related
to the Syracuse version syr.
 6

Deﬁnition 3.1 We deﬁne the Syracuse jump function sjp : O → O by

sjp(n) = syr
(ℓ)(n), where ℓ = ⌊log2(n) + 1⌋.

Example 3.2 We have sjp(1) = 1, sjp(3) = 2 and sjp(27) = syr
(5)(27) =
107.

Here is the corresponding Syracuse falling time.

Deﬁnition 3.3 Let n ∈ O \{1}. The Syracuse falling time of n, denoted
sft(n), is the least k ≥ 1 such that sjp(k)(n) < n, or ∞ if there is no such k.

Example 3.4 We have sft(27) = 6, as witnessed by the orbit of 27 under
Syracuse jumps, namely

Osjp(27) = (27, 107, 233, 377, 911, 53, 1, 1, . . . ).

As one may expect, the inequality sft(n) ≤ ft(n) holds very often, but
not always. For instance, for n = 199, we have ft(199) = 1 but sft(199) = 5.
The former equality follows from the orbit

OT (199) = (199, 299, 449, 674, 337, 506, 253, 380, 190, . . . )

and the value ⌊log2(199) + 1⌋ = 8, yielding jp(199) = 190, while the latter
one follows from the orbit

Osyr(199) = (199, 323, 395, 479, 577, 1, . . . ).

Deﬁnition 3.5 A Syracuse falling time record is an integer n ∈ 4N + 3 such
that n ≥ 7 and sft(m) < sft(n) for all m ∈ 4N + 3 with m < n.

The complete list of Syracuse falling time records up to 2
35 is displayed
in Table 4. Compared with Table 1, it turns out that all current Syracuse
falling time records are also falling time records. The converse does not hold,
as shown by the falling time records 60 975 and 1 394 431 in Table 1.

7

n ≡ 3 mod 4 ⌊log2(n) + 1⌋ sft(n)
7 3 2
27 5 6
6 649 279 23 7
63 728 127 26 9

Table 4: Syracuse falling time records up to 2
35

3.1 Current maximum

The Collatz conjecture is equivalent to the statement sft(n) < ∞ for all
n ∈ O \{1}. Again, it is likely that a stronger form holds, namely that
sft(n) is bounded on O \{1}. Besides the computational evidence above and
below, some heuristics point to that possibility in Section 5. Similarly to
Proposition 2.1, here is a computational result in that direction.

Proposition 3.6 We have sft(n) ≤ 9 for all n ∈ [3, 2
35 − 1] such that n ≡
3 mod 4.

Proof. With Mathematica 12, in a few days of home computer time.

As yet another hint pointing to the same direction, it turns out that

sft(g1), . . . , sft(g34) ≤ 10 (5)

for the 34 currently known glide records. For deﬁniteness, Table 5 displays
the Syracuse falling times of the top ten glide records as listed in Table 3.

n g25 g26 g27 g28 g29 g30 g31 g32 g33 g34
sft(n) 9 8 8 8 8 10 8 10 9 8

Table 5: Syracuse falling times of top ten glide records

Among the gi, and as in Section 2.1 for the falling time, only g30 and g32
reach the current maximum of the Syracuse falling time, namely sft(n) = 10.
Interestingly, the biggest currently known glide record, namely n = g34, only
satisﬁes sft(n) = 8. With Proposition 3.6 and (5) in the background, here is
our formal conjecture.
 8

Conjecture 3.7 There exists C ≥ 10 such that sft(n) ≤ C for all n ≡
3 mod 4.

Again, the truth of this conjecture would yield a strong positive solution
of the Collatz conjecture. At the time of writing, no single positive integer
n ≡ 3 mod 4 is known to satisfy sft(n) ≥ 11. Thus, a still bolder conjecture
would be to take C = 10 in Conjecture 3.7, or C = 12 to be on a safer side.
Whence the title of this paper.

4 The case 2ℓ − 1

In sharp contrast with the stopping time of 2
ℓ − 1, for which σ(2
ℓ − 1) ≥ ℓ
for all ℓ ≥ 2, the falling time and the Syracuse falling time of 2
ℓ − 1 seem to
remain very small as ℓ grows. Here is some strong computational evidence.

Proposition 4.1 Besides ft(2
5 − 1) = ft(26 − 1) = 8, we have ft(2
ℓ − 1) ≤ 5
for all 2 ≤ ℓ ≤ 100 000 with ℓ /∈ {5, 6}.

Proof. With Mathematica 12, in about two days of home computer time.

Moreover, the value ft(2
ℓ −1) = 5 seems to occur ﬁnitely many times only,
the last one being presumably at ℓ = 132. In turn, the value ft(2ℓ − 1) = 4
seems to occur inﬁnitely often. Whence the following conjecture, veriﬁed by
computer up to ℓ = 100 000.

Conjecture 4.2 We have ft(2
ℓ − 1) ≤ 4 for all ℓ ≥ 133.

Here are the analogous statement and conjecture for the Syracuse falling
time. For a, b ∈ N, we denote by [a, b] = {n ∈ N | a ≤ n ≤ b} the integer
interval they span.

Proposition 4.3 Besides sft(2
5 − 1) = sft(26 − 1) = 5, and sft(2
24 − 1) = 4,
we have sft(2
ℓ − 1) ∈ {2, 3} for all ℓ ∈ [2, 4 624] \ {5, 6, 24},

sft(2
ℓ − 1) = 2 for all ℓ ∈ [4 625, 100 000].

Proof. With Mathematica 12, in about two days of home computer time.

This leads us to the following conjecture, true up to ℓ = 100 000.

Conjecture 4.4 We have sft(2
ℓ − 1) = 2 for all ℓ ≥ 4 625.

9

5 For very large n

As hinted by the computational evidence and conjectures of Section 4 on
the case n = 2ℓ − 1, by intensive semi-random search, and by the heuristics
below, it appears to be increasingly diﬃcult for integers n to satisfy ft(n) ≥ 5
or sft(n) ≥ 3 as they grow very large. Here then are still bolder conjectures.

Conjecture 5.1 We have ft(n) ≤ 4 for all n ≥ 2
150.

This threshold of 2150 is directly inspired by Conjecture 4.2, of course with
a margin for safety. It cannot be signiﬁcantly lowered, since ft(2
132 − 1) = 5
as noted before Proposition 4.1.
In further support of Conjecture 5.1, our intensive semi-random search
looking for occurrences of ft(n) ≥ 5 with n ≥ 2
130 only produced a single
solution so far, namely

n = 2 272 460 998 861 782 137 133 024 949 484 617 360 879.

This number has 131 binary digits, falling time ft(n) = 5, and stopping time
σ(n) = 562. To increase the odds of ﬁnding solutions, we limit our search
to those n with stopping time σ(n) ≥ 24, i.e. to the corresponding 286 581
classes mod 2
24. See [8] for more details on the description of the condition
σ(n) ≥ k by classes mod 2
k.

Here is the analogous conjecture for the Syracuse falling time. Its thresh-
old of 2
5000 is similarly inspired by Proposition 4.3 and Conjecture 4.4.

Conjecture 5.2 We have sft(n) ≤ 2 for all odd n ≥ 2
5000.

5.1 Heuristics

Besides the computational evidence leading to Conjectures 2.3, 3.7, 4.2,
4.4, 5.1 and 5.2, a heuristic argument would run as follows. It is well known
that the Collatz conjecture is equivalent to the statement that, starting with
any integer n ≥ 1, the probability for T (k)(n) to be even or odd tends to 1/2
as k grows to inﬁnity. Thus, even if n written in base 2 is a highly structured
binary string, as e.g. for n = 2
ℓ − 1, one may expect that for ℓ = the length
of that string, then T (ℓ)(n) in base 2 will already look more random. That
is, a single jump or Syracuse jump at n ≥ 3 should already introduce a good
dosis of randomness, all the more so as n grows very large. And therefore, a
bounded number of jumps or Syracuse jumps at n might well suﬃce to fall
below n.
 10

5.2 A challenge

We hope that the experts in highly eﬃcient computation of the 3x+1 function
will tackle the challenge of probing these conjectures to much higher levels
than the ones reported here. For instance, as both a challenge and a request
to the reader, and in view of Conjecture 5.1, if you do ﬁnd any n ≥ 2
140

satisfying ft(n) ≥ 5, please e-mail it to the authors. Your solution will be
duly recorded on a dedicated webpage.

References

[1] D. Barina, Convergence veriﬁcation of the Collatz problem, The Journal
of Supercomputing 77 (2021) 2681–2688.

[2] S. Eliahou, The 3x + 1 problem: new lower bounds on nontrivial cycle
lengths, Discrete Math. 11 (1993) 45–56.

[3] J. C. Lagarias, 3x + 1 problem and related problems, https://dept.
math.lsa.umich.edu/~lagarias//3x+1.html

[4] The Ultimate Challenge: The 3x + 1 Problem. J. C. Lagarias, Editor.
Amer. Math. Soc., Providence, RI, 2010.

[5] E. Roosendaal, www.ericr.nl/wondrous

[6] E. Roosendaal, www.ericr.nl/wondrous/glidrecs.html

[7] T. Tao, Almost all orbits of the Collatz map attain almost bounded values
(2019) arXiv:1909.03562

[8] R. Terras, A stopping time problem on the positive integers, Acta Arith.
30 (1976) 241–252.

[9] Wolfram Research, Inc., Mathematica, Version 12, Champaign, IL
(2019).

Authors’ addresses:
Shalom Eliahoua,b and R´enald Simonetto
a,b,c

aUniv. Littoral Cˆote d’Opale, UR 2597 - LMPA - Laboratoire de Math´ematiques
Pures et Appliqu´ees Joseph Liouville, F-62100 Calais, France
bCNRS, FR2037, France
cMicrosoft France, 37 Quai du Pr´esident Roosevelt, 92130 Issy-les-Moulineaux,
France
 11
