<!-- source: https://cs.uwaterloo.ca/journals/JIS/VOL8/Iannucci/iannucci45.pdf | converted from PDF -->

23 11 Article 05.4.8
Journal of Integer Sequences, Vol. 8 (2005),2
 3

6

1

47
 Kaprekar Triples

Douglas E. Iannucci and Bertrum Foster
University of the Virgin Islands
2 John Brewers Bay
St. Thomas, VI 00802
USA
diannuc@uvi.edu
bfosterk@yahoo.com

Abstract

We say that 45 is a Kaprekar triple because 453 = 91125 and 9 + 11 + 25 = 45. We
ﬁnd a necessary condition for the existence of Kaprekar triples which makes it quite
easy to search for them. We also investigate some Kaprekar triples of special forms.

1 Introduction

Kaprekar triples (sequence A006887, Sloan [5]) are numbers with a property which is easily
demonstrated by example. Observe that

83 = 512, 5 + 1 + 2 = 8,
453 = 91125, 9 + 11 + 25 = 45,
2973 = 26198073, 26 + 198 + 073 = 297,
49493 = 121213882349, 1212 + 1388 + 2349 = 4949,
444433 = 87782935806307, 8778 + 29358 + 06307 = 44443,
5651373 = 180493358291026353, 180493 + 358291 + 026353 = 565137.

Therefore 8, 45, 297, 4949, 44443, and 565137 are all examples of Kaprekar triples.
Kaprekar triples generalize the Kaprekar numbers (sequence A006886, Sloan [5]), which
were introduced by Kaprekar [4], discussed by Charosh[2], and completely characterized by
Iannucci [3]. Kaprekar triples are mentioned in Wells’s Dictionary of Curious and Interesting
Numbers [6].
 1

Formally, an n-Kaprekar triple k (where n is a natural number) satisﬁes the pair of
equations
 k3 = p · 102n + q · 10n + r ,
k = p + q + r ,

where 0 ≤ r < 10n, 0 ≤ q < 10n, and p > 0 are integers. As the 3-Kaprekar triple 297 shows,
p may have fewer than n digits, and so may q or r (note the leading zero in r = 073). The
stipulation that p > 0 precludes many otherwise trivial examples such as

1003 = 0 · 108 + 100 · 104 + 0 ,
100 = 0 + 100 + 0 ,

i.e., 100 as a 4-Kaprekar triple. Having p > 0 also precludes 1 as a Kaprekar triple, in spite
of its inclusion in sequence A006887 by Sloan [5].

2 The Set K(N )

Let N be a natural number such that N ̸≡ 1 (mod 4). We deﬁne the set K(N ) of positive
integers as follows: We say k ∈ K(N ) if there exist nonnegative integers r < N , q < N , and
a positive integer p, such that k3 = pN 2 + qN + r (1)

and such that k = p + q + r . (2)

Although N satisﬁes (1) and (2) (with p = N , q = r = 0), we nonetheless disallow N as
an element of K(N ). Therefore, it follows that k < N if k ∈ K(N ). For, subtracting (2)
from (1) yields k(k − 1)(k + 1) = (N − 1)(p(N + 1) + q) , (3)

so that k > N implies k < p + q
k + 1 .

Since q/(k + 1) < 1, we have k ≤ p. Since k < p contradicts (2), we have k = p, but this
implies q = r = 0 and hence k = N by (1). Contradiction. Therefore k < N if k ∈ K(N ).
Suppose k ∈ K(N ). Then (3) implies N − 1 | k(k − 1)(k + 1). Because N ̸≡ 1 (mod 4),
there exist pairwise relatively prime integers d, d1, and d2 such that

N − 1 = dd1d2 , d | k , d1 | k − 1 , d2 | k + 1 . (4)

Since d | k we write k = dm

for a positive integer m. Then d1 | dm − 1 and d2 | dm + 1 and so we have

dm ≡ 1 (mod d1) , dm ≡ −1 (mod d2) . (5)

2

Let
 ξ1 ≡ d−1 (mod d1) , ξ2 ≡ d−1 (mod d2) ,
µ1 ≡ d−1
1 (mod d2) , µ2 ≡ d−1
2 (mod d1) .

Then we have m ≡ ξ1 (mod d1) , m ≡ −ξ2 (mod d2) ,

so that by the Chinese remainder theorem we have

m ≡ ξ1µ2d2 − ξ2µ1d1 (mod d1d2) . (6)

Moreover, m is the least positive residue such that (6) is satisﬁed; this is because dm = k <
N = dd1d2 + 1 and thus m ≤ d1d2.
For a positive integer n, we call d a unitary divisor of n if d | n and (d, n
d ) = 1. In this
case we write d∥n. We have shown

Theorem 1 If N ̸≡ 1 (mod 4), then every element k ∈ K(N ) is divisible by a unitary
divisor d of N − 1. If we write k = dm, then m satisﬁes (4) for some pair d1, d2, of unitary
divisors of N − 1 such that d1d2 = (N − 1)/d.

If N ̸≡ 1 (mod 4), then Theorem 1 gives a necessary condition for ﬁnding elements k
of K(N ), and hence it may be applied to ﬁnd an upper bound for |K(N )|, the number of
elements in K(N ). For, if N −1 has the unique prime factorization given by N −1 = ∏t
i=1 pai
i ,
then we call the prime powers pai
i the components of N − 1. Then d∥N − 1 if and only if
d is a product of components of N − 1 (including the empty product 1). We refer to t, the
number of components of N − 1, as ω(N − 1). Thus by Theorem 1, if N ̸≡ 1 (mod 4) then

|K(N )| ≤ 3ω(N −1) . (7)

It is possible to deﬁne K(N ) when N ≡ 1 (mod 4). In this case, the factors d, d1, and d2
in (4) will be pairwise relatively prime if and only if d is even. If this is so, we may proceed
exactly as above, so that (7) is still true.
Otherwise d is odd. Since 2ν∥N − 1 for some ν ≥ 2, we have either 2∥d1, 2ν−1∥d2, or,
2ν−1∥d1, 2∥d2. Note that these two cases are identical when 22∥N − 1. In either case, the
equations (5) still hold, and since (d, d1) = (d, d2) = 1, we see that m may be determined
uniquely modulo [d1, d2]. Here, d∥N − 1, and d1 and d2 are each some power of 2 multiplied
by an odd unitary divisor of N − 1. Thus (7) still holds in the case when N ≡ 1 (mod 4).

3 Kaprekar Triples

In the notation of the previous section,we refer to the set ∪∞
n=1K(10n) as the set of Kaprekar
triples. If we prefer, we may refer to the set K(10n), for ﬁxed n, as the set of n-Kaprekar
triples. To illustrate Theorem 1, consider the set of 6-Kaprekar triples, and note the factor-
ization 106 − 1 = 33 · 7 · 11 · 13 · 37 .

3

We may take d = 27, d1 = 259, and d2 = 143. Then

ξ1 = 48 , ξ2 = 53 , µ1 = 90 , µ2 = 96 ,

giving m ≡ 143 · 96 · 48 − 259 · 90 · 53 ≡ 20931 (mod 37037) .

Therefore m = 20931 , d = 27 , k = 20931 · 27 = 565137 .

Since
 5651373 = 180493358291026353 ,
565137 = 180493 + 358291 + 026353 ,

we have 565137 ∈ K(106). To show that the conditions in Theorem 1 are not suﬃcient,
consider d = 297, d1 = 37, and d2 = 91. Here,

ξ1 = 1 , ξ2 = 19 , µ1 = 32 , µ2 = 24 ,

giving m ≡ 3257 , d = 297 , k = 967329 .

However, 9673293 = 905154309885752289 ,

but 905154 + 309885 + 752289 = 1967328 ,

and so 967329 /∈ K(106). Note that 1967328 = 967329 + (106 − 1). Experimentally, we have
seen that roughly one fourth of the 3ω(N −1) possible triples (d, d1, d2) of unitary divisors of
N − 1 produce an element k ∈ K(N ) when Theorem 1 is applied. The other three fourths
produce k such that when p, q, and r in (1) are obtained we get

p + q + r = k + (N − 1)

instead of (2). Generally, the larger the value of ω(N − 1), the closer to 1:3 the ratio of
elements of K(N ) to non-elements becomes.
We provide some data for N = 10n, for various values of n, where “ratio” refers to the
ratio |K(10n − 1)|/3ω(10n−1):
 4

n 3ω(10n−1) |K(10n)| ratio
5 27 5 0.185185
6 243 37 0.152263
7 27 8 0.296296
10 243 64 0.263374
12 2187 527 0.240969
15 729 195 0.267490
19 9 1 0.111111
20 6561 1649 0.251334
21 2187 538 0.245999
23 9 1 0.111111
24 59049 14702 0.248980
30 1594323 398838 0.250161
42 4782969 1196902 0.250242
64 43046721 10759839 0.249957
80 14348907 3587901 0.250047

4 Applications

It is a simple matter to search for Kaprekar triples by applying Theorem 1. To do so, one
only needs the factorizations of 10n − 1 for n ≥ 1, which are easily available (for example
see Brillhart et al. [1]).
In this section we will discuss Kaprekar triples of certain forms. For example, consider
the set K(64M 2) for some positive integer M . Since

64M 2 − 1 = (8M − 1)(8M + 1) ,

and since 8M − 1 and 8M + 1 are relatively prime, we can apply Theorem 1 by choosing d,
d1, and d2 from among the unitary divisors 8M ± 1 and 1 of 64M 2 − 1. If we let d2 = 1,
there are at least two ways to do this, one of which is to let d = 8M − 1 and d1 = 8M + 1.
In this case we have ξ1 = 4M and ξ2 = µ1 = µ2 = 1, and thus

m = d2µ2ξ1 − d1µ1ξ2 = −4M − 1 ≡ 4M (mod 8M + 1) ,

taking the least positive residue modulo 8M + 1. This gives k = dm = 4M (8M − 1).
Similarly, taking d = 8M + 1 and d1 = 8M − 1 gives k = 4M (8M + 1).
Thus it is possible that 4M (8M ± 1) are both elements of K(64M 2). Indeed they are, for

k3 = 64M 3(8M ± 1)3

= 4096M 4(8M 2 ± 3M ) + 64M 2(24M 2 ± M ) ,

and, (8M 2 ± 3M ) + (24M 2 ± M ) = 32M 2 ± 4M = k .

Note that if n ≥ 3 then 102n is of the form 64M 2 with M = 53 · 10n−3. We have

Theorem 2 For n ≥ 3, the integers 5 · 10n−1(10n ± 1) are 2n-Kaprekar triples.

5

For example, 499500 and 500500 are both 6-Kaprekar triples, 49995000 and 50005000 are
both 8-Kaprekar triples, and so forth.
For positive integers r > 1 and n ≥ 1, we refer to an element of K(rn) as a base-r
Kaprekar triple. Note that if p ≥ 3 then 22p has the form 64M 2 where M = 2p−3. Hence
2p−1(2p ± 1) are binary (or base-2) Kaprekar triples. Since every even perfect number has
the form 2p−1(2p − 1) where 2p − 1 is prime (a fact ﬁrst proved by Euler), we have

Theorem 3 Every even perfect number is a binary Kaprekar triple.

As examples, we see that

283 = 5 · 642 + 23 · 64, 5 + 23 = 28;
4963 = 116 · 10242 + 380 · 1024, 116 + 380 = 496;
81283 = 2000 · 163842 + 6128 · 16384, 2000 + 6128 = 8128.

We can also consider the set K(4096M 4) for some positive integer M . Similarly as we
did above, we can show that 256M 3 + 4M belongs to this set. Letting M = 53 · 10n−3 for
n ≥ 3 gives us

Theorem 4 If n ≥ 3 then 5 · 103n−1 + 5 · 10n−1 is a 4n-Kaprekar triple.

Hence 500000500 is a 12-Kaprekar triple:

5000005003 = 1250003750003750001250000000 ,
125 + 000375000375 + 000125000000 = 500000500 .

Also, 500000005000 is a 16-Kaprekar triple, 500000000050000 is a 20-Kaprekar triple, and
so forth.

5 Concluding Remarks

Theorem 2 shows that there always exists an n-Kaprekar triple when n ≥ 6 is even. What
about odd n? By (7), there are fewer such triples when ω(10n − 1) is small. In fact,
ω(10n − 1) = 2 when n = 19, 23, and 317 (see Brillhart et. al. [1]), although it is not known
how long this list may be extended. The table following section 3 shows that an n-Kaprekar
exists when n = 19 or 23. However, a simple computer search reveals that no 317-Kaprekar
triples exist; thus there do not exist n-Kaprekar triples for every n.
A more general question is, are there certain forms of N for which K(N ) is empty? For
example, we can show K(N ) = ∅ whenever N > 8 is of the form pα + 1 for odd prime p
and α ≥ 1; note that K(8) consists of the perfect number 6 by Theorem 3. Indeed, since
N − 1 = pα, if k ∈ K(N ) then by (4) one of three cases occur: (i) pα | k; (ii) pα | k − 1; (iii)
pα | k + 1.
In case (i), as k < N we must have k = pα. But here,

k3 = (N − 3)N 2 + 2N + (N − 1),
(N − 3) + 2 + (N − 1) = k + (N − 1) ̸= k.

6

In case (ii) we have k ≡ 1 (mod pα) by (6).
In case (iii), k ≡ −1 (mod pα) by (6), which implies k = pα − 1. But

k3 = (N − 6)N 2 + 11N + (N − 8),
(N − 6) + 11 + (N − 8) = k + (N − 1) ̸= k.

All three cases lead to contradiction (case (ii) contradicts 1 < k < N ).
On the other hand, there are forms of N for which K(N ) ̸= ∅ (as we’ve already seen
when N = 102n). For example, it is straightforward to check that when N = 2n + 1, n ≥ 2,
we have k = 2n−1 − 1 ∈ K(N ).

References

[1] J. Brillhart, D. Lehmer, J. Selfridge, B. Tuckerman, and S. Wagstaﬀ Factorizations
of bn ± 1, b =2, 3, 5, 6, 7, 10, 11, 12 Up to High Powers (3rd Ed.), Contemporary
Mathematics 22, 2001.

[2] M. Charosh, Some Applications of Casting Out 999. . . ’s J.Recreational Math. 13 (1980),
111–118.

[3] D. Iannucci, The Kaprekar Numbers, J. Integer Seq. 3 (2000), article 00.1.2.

[4] D. Kaprekar, On Kaprekar Numbers J. Recreational Math. 13 (1980), 81–82.

[5] N. Sloane, The On-Line Encyclopedia of Integer Sequences.

[6] D. Wells, The Penguin Dictionary of Curious and Interesting Numbers, Penguin Books,
New York, 1986.

2000 Mathematics Subject Classiﬁcation: Primary 11A63; Secondary 11Y55 .
Keywords: Kaprekar triples, division algorithm, Chinese remainder theorem, components,
perfect numbers.

(Concerned with sequences A006886 and A006887.)

Received August 30 2004; revised version received October 7 2005. Published in Journal of
Integer Sequences, October 20 2005.

Return to Journal of Integer Sequences home page.

7
