<!-- source: https://denisevellachemla.eu/empirical-verification-of-the-even-CG.pdf | converted from PDF -->

MATHEMATICS OF COMPUTATION
Volume 83, Number 288, July 2014, Pages 2033–2060
S 0025-5718(2013)02787-1
Article electronically published on November 18, 2013

EMPIRICAL VERIFICATION OF THE EVEN
GOLDBACH CONJECTURE AND COMPUTATION
OF PRIME GAPS UP TO 4 · 10
18

TOM ´AS OLIVEIRA e SILVA, SIEGFRIED HERZOG, AND SILVIO PARDI

Abstract. This paper describes how the even Goldbach conjecture was con-
ﬁrmed to be true for all even numbers not larger than 4 · 1018. Usingaresult
of Ramar´e and Saouter, it follows that the odd Goldbach conjecture is true
up to 8.37 · 1026. The empirical data collected during this extensive veriﬁca-
tion eﬀort, namely, counts and ﬁrst occurrences of so-called minimal Goldbach
partitions with a given smallest prime and of gaps between consecutive primes
with a given even gap, are used to test several conjectured formulas related
to prime numbers. In particular, the counts of minimal Goldbach partitions
and of prime gaps are in excellent accord with the predictions made using the
prime k-tuple conjecture of Hardy and Littlewood (with an error that appears
to be O(√t log log t), where t is the true value of the quantity being estimated).
Prime gap moments also show excellent agreement with a generalization of a
conjecture made in 1982 by Heath-Brown.

The Goldbach conjecture [13] is a famous mathematical problem whose proof, or
disproof, has so far resisted the passage of time [20, Problem C1]. (According to [1],
Waring and, possibly, Descartes also formulated similar conjectures.) It states, in
its modern even form, that every even number larger than four is the sum of two
odd prime numbers, i.e., that n = p + q. Here, and in what follows, n will always
be an even integer larger than four, and p and q will always be odd prime numbers.
The additive decomposition n = p + q is called a Goldbach partition of n.The
one with the smallest p will be called the minimal Goldbach partition of n;the
corresponding p will be denoted by p(n) and the corresponding q by q(n).
It is knownthatupto a givennumber x at most O(x0.879) even integers do
not have a Goldbach partition [30], and that every large enough even number is
the sum of a prime and the product of at most two primes [24]. Furthermore,
according to [48], every odd number greater that one is the sum of at most ﬁve
primes. As described in Table 1, over a time span of more than a century the
even Goldbach conjecture was conﬁrmed to be true up to ever-increasing upper
limits. Section 1 describes the methods that were used by the ﬁrst author, with
computational help from the second and third authors, and others, to set the limit
of veriﬁcation of the Goldbach conjecture at 4 · 10
18. Section 2 presents a small
subset of the empirical data that was gathered during the veriﬁcation, namely,
counts and ﬁrst occurrences of primes in minimal Goldbach partitions, and counts
and ﬁrst occurrences of prime gaps, and compares it with the predictions made by

Received by the editor May 21, 2012 and, in revised form, December 6, 2012.Mathematics Subject Classiﬁcation. Primary 11A41, 11P32, 11N35; Secondary 11N05,
11Y55.
Key words and phrases. Goldbach conjecture, prime gaps, prime k-tuple conjecture.

c⃝2013 American Mathematical Society

2033

License or copyright restrictions may apply to redistribution; see https://www.ams.org/journal-terms-of-use

2034 T. OLIVEIRA e SILVA, S. HERZOG, AND S. PARDI

Table 1. Some records of veriﬁcation of the even Goldbach conjecture.

limit year who
unknown 1742 Goldbach [13]
104 1855 Desboves [13]
(conﬁrmed by Haussner in 1896 [13])
105 1940 Pipping [44]
3.3 · 107 1964 Shen [44]
108 1965 Stein and Stein [47]
(conﬁrmed by Light et al. in 1980 [28])
2 · 1010 1989 Granville, Van de Lune, and te Riele [19]
4 · 1011 1993 Sinisalo [46]
1014 1998 Deshouillers, te Riele, and Saouter [11]
4 · 1014 2001 Richstein [40]
3 · 1017 (double checked) 2012 Oliveira e Silva, Herzog, and Pardi (this paper)
4 · 1018 2012 Oliveira e Silva, Herzog, and Pardi (this paper)

conjectured asymptotic formulas. It is also established there that the odd Goldbach
conjecture, which states that every odd number larger than 5 is the sum of three
primes, is true up to 8.37 · 10
26. Section 2.4 acknowledges those that contributed
computational resources to this extensive veriﬁcation eﬀort.

1. Methods

To verify the even Goldbach conjecture for a given n two primes p and q must
be found, possibly with q equal to p, such that n = p + q. Although any p for which
n − p is prime will do [11, 12, 44], we opted to compute for each n the minimal
Goldbach partition p(n)+ q(n). The main reason for this choice is that the number
of occurrences of a given smallest prime in a minimal Goldbach partition, as well
as the smallest n for which it occurs, has some theoretical interest [19].
In order to compute the minimal Goldbach partitions for all even numbers be-
longing to a given interval it is necessary to have a list of the primes belonging to a
possibly slightly larger interval; these primes will be the candidates for q(n). Sub-
section 1.1 describes the modiﬁed segmented Eratosthenes sieve used to generate
these primes. This modiﬁcation, devised in 2001 when the computations reported
in this paper were started, exhibits excellent data-cache behavior. Near 1018 our
production code takes an average of about 10 clock cycles to determine if an odd
number is prime or not.
Subsection 1.2 describes how the minimal Goldbach partition can be computed in
a very eﬃcient way for each even number belonging to a given interval. Irrespective
of the order of magnitude of n, our production code takes an average of about 9 clock
cycles to compute and collect statistics about each minimal Goldbach partition.
Subsection 1.3 describes how the computations were distributed among many
computers. It also describes the measures that were taken in order to attempt
to ensure that the computations were performed correctly. They were essential
to locate occasional bad results due to random low probability hardware failures.
Although very rare, such hardware failures are almost unavoidable in a computa-
tion that used a mixture of reliable and unreliable (low-cost personal computers)
computing resources, and which took about 770 one-core CPU years to ﬁnish.

License or copyright restrictions may apply to redistribution; see https://www.ams.org/journal-terms-of-use

EMPIRICAL VERIFICATION OF THE EVEN GOLDBACH CONJECTURE 2035

1.1. Cache-eﬃcient segmented Eratosthenes sieve. Although several algo-
rithms with better asymptotic computational complexity exist [2, 14, 17], the seg-
mented Eratosthenes sieve [3, 5, 45] — with our own modiﬁcations — appears to be
the fastest way to generate all primes in a relatively large interval with an upper
limit near 10
18. This is so because the simplicity of the algorithm and its regular
data requirements can be used to reduce the frequency of branch mispredictions
and accesses to out-of-cache data, thus speeding up considerably the program on
contemporary state-of-the-art general purpose processors. This is apparently not
so easy to do with the other algorithms.
We begin with a description of the standard segmented Eratosthenes sieve and
with an explanation of its shortcomings; pk is the k-th prime number, i.e., p1 =2,
p2 =3, and so on, ⌊x⌋ is the largest integer not larger than x, x mod y = x − y⌊ x
y ⌋
,
and π(x) denotes the number of primes not larger than x.

Algorithm 1.1 (Segmented Eratosthenes sieve [3]). To generate all odd primes in
the interval (A, B),with B> A > 0,with A even, with K and Δ integers, and with
B = A +2KΔ, do:
1. [Initialize.] Set a to A and b to A +2Δ.Set j to 2.
2. [New interval.] Set m0,m1,... ,m∆−1 to 1.Set i to 2.
3. [New primes.] If p2 ≥ b then advance to step 5.
4. If p2 <a then set oj to (
2pj − 1 − (a + pj)mod (2pj))
/2; otherwise set oj
to (p2 − a − 1)/2.Add 1 to j and go back to step 3.
Comment: a +2oj +1 is the smallest odd multiple of pj larger than a that
needs to be considered.
5. [Mark composites.] If i ≥ j then advance to step 8.
6. If oi ≥ Δ then subtract Δ to oi, add 1 to i, and go back to step 5.
7. Set moi to 0.Add pi to oi. Gobackto step6.
8. [Next interval.] Add 2Δ to a and to b.If a<B then go back to step 2;
otherwise terminate.
At the beginning of step 8, mi is equal to 1 if and only if a +2i +1 is prime.

This algorithm requires that a list of the odd primes up to √

B, plus the ﬁrst
prime larger than √
B, to be available. Such a list can be computed easily with
a simple modiﬁcation of the same algorithm. It is possible to avoid storing thej variables; they can be recomputed every time a new (a, b) interval is being
dealt with. Doing so, however, slows down the algorithm because divisions on
contemporary processors are slow.
Under normal conditions only the inner (steps 6 and 7) and middle loops (steps 5
to 7) of Algorithm 1.1 are signiﬁcant parts of the computation [3]. The number of
times the middle loop is performed is

Nmiddle =
 K∑=1 π(√

A +2kΔ) − K ≈ Kπ(√B)

(the approximation is valid when A is much larger that B − A, asisusually thecase
in practice). The number of times the inner loop is performed is, approximately

Ninner ≈
 K∑

k=1
 ∑

2<p≤√
a+2k∆
 Δ
p ≈ B − A
2
 (log log B − 0.93165
)

License or copyright restrictions may apply to redistribution; see https://www.ams.org/journal-terms-of-use

2036 T. OLIVEIRA e SILVA, S. HERZOG, AND S. PARDI

xTime(inseconds)
10
10 10
11 10
12 10
13 10
14 10
15 10
16 10
17 10
18 10
19
0

15

30

45

60
 •◦• •◦• •◦• •◦• •◦• •◦• •◦• •◦• •◦
• •◦
• •◦
• •◦
• •◦
• •◦
• •◦

•
 •◦

•
 •◦

•
 •◦

•
 •◦

•
 •◦

•
 •◦

•
 •◦

•
 •◦

•
 •◦

•
 •◦

•
 •◦

•
 •◦

•
 •◦

•◦ — Intel 2.83GHz Q9550 Core2 Quad (6MB L2 cache)
8GB of dual channel 1100MHz DDR2 memory

• — AMD 2.20GHz Athlon64 (512kB L2 cache)
2GB of dual channel 333MHz DDR memory

Figure 1. Time needed to generate all primes in an interval of
2
30 integers centered at x using a simple implementation of Algo-
rithm 1.1 [34, second program version], for two processors (only one
core used on the Intel processor). The older single-core Athlon64
processor has a much smaller L2 cache, and slower main memory,
which for large x makes the algorithm rather slow. For both pro-
cessors, when x increases the optimal value of Δ also increases (not
shown). The initialization time of the algorithm (steps 3 and 4 for
the ﬁrst interval), about a minute for the largest x on the slower
processor, was not taken into consideration.

(the last approximation is a simple application of Mertens’ second theorem [22]).
The execution time of Algorithm 1.1 can then be reasonably well approximated bymiddleNmiddle +αinnerNinner,where αmiddle and αinner are constants that depend on
the actual implementation of the algorithm and, of course, on the processor where
it is run. The second term corresponds to the useful work made by the algorithm.
The ﬁrst corresponds to overheads and so should be made as small as possible. In
the standard segmented Eratosthenes sieve this is achieved by making K small or,
what is the same, by making Δ large [3]. Doing this, however, increases the amount
of memory accessed in an essentially random way in the inner loop. If this amount
of memory exceeds the amount that can be stored in the processor’s data cachesinner will be large and so the algorithm will be slow.
A small value of Δ, on the other hand, gives rise to a large value of K.In this
case the algorithm spends a larger fraction of its time just updating the oj variables.
This is so because the middle loop is run more times and because the fraction of
primes that have an odd multiple in the interval (a, b) decreases as b increases.
For example, for B =10
18 and Δ = 2
19,only 0.553% (2 81049 in 508 47533) of
the odd primes used to mark composites have an odd multiple belonging to the
interval (B − 2Δ,B). The best value for Δ will then be a trade-oﬀ between the
need to make Δ small (to keep all frequently used variables in the data cache),
and the need to make it large (to reduce the computational overheads). The end
result is a program which slows down considerably when b increases beyond an
implementation dependent limit, as illustrated in Figure 1.
There is a simple way to eliminate this problem. The main idea is to leave to
later intervals all primes that do not have an odd multiple in the current interval.

License or copyright restrictions may apply to redistribution; see https://www.ams.org/journal-terms-of-use

EMPIRICAL VERIFICATION OF THE EVEN GOLDBACH CONJECTURE 2037

In order to do this eﬃciently it is necessary to split the primes pj in two classes:
those that are smaller than Δ (the “small” primes), and those that are not (the
“large” primes). The former are guaranteed to have at least one odd multiple in an
interval of 2Δ consecutive integers, and can be dealt with as in Algorithm 1.1. The
latter are guaranteed to have at most one odd multiple in such an interval (this
observation was used in [3] to speedup the inner loop of Algorithm 1.1). To deal
with them eﬃciently, the tuples (pj,oj) are placed in lists, one list per interval of
the form (A + kΔ,A +(k + 1)Δ), in such a way that at the beginning of the middle
loop of the algorithm the list associated with the current interval contains only the
“large” primes which have an odd multiple in that interval. This idea gives rise to
the following algorithm.

Algorithm 1.2 (Cache-eﬃcient segmented Eratosthenes sieve). To generate all
odd primes in the interval (A, B),with B> A > 0,with A even, with K and Δ
integers, and with B = A +2KΔ, do:

1. [Initialize.] Set a to A and b to A +2Δ.Set k to 0, j to 2,and p to 3.Set
the lists L0,L1,..., to the empty list.
2. [New interval.] Set m0,m1,... ,m∆−1 to 1.Set i to 2.
3. [New “small” primes.] If p ≥ Δ or if p2 ≥ b then advance to step 5.
4. Set pj to p.If p2 <a then set oj to (
2p − 1 − (a + p)mod (2p))
/2;otherwise
set oj to (p2 − a − 1)/2.Add 1 to j and replace p by the smallest prime
larger than p. Gobackto step3.
5. [Mark composites.] If i ≥ j then advance to step 8.
6. If oi ≥ Δ then subtract Δ to oi, add 1 to i, and go back to step 5.
7. Set moi to 0.Add pi to oi. Gobackto step6.
8. [New “large” primes.] If p2 ≥ b then advance to step 10.
9. If p2 <a then set o to (
2p − 1 − (a + p)mod (2p))
/2; otherwise set o to
(p2 − a − 1)/2. Insert the tuple (p, o mod Δ) in the list Lk+⌊o/∆⌋.Replace
p by the smallest prime larger than p and go back to step 8.
10. [Mark composites.] For each tuple (p, o) of the list Lk,set mo to 0 and
insert the tuple (
p, (o + p)mod Δ
) in the list Lk+⌊(o+p)/∆⌋.
11. [New interval.] Set k to k +1 and add 2Δ to a and to b.If a<B then go
back to step 2; otherwise terminate.

At the beginning of step 11, mi is equal to 1 if and only if a +2i +1 is prime.

On contemporary processors, the test at the beginning of step 6 generates many
time-consuming branch mispredictions when pj approaches Δ; in a practical im-
plementation this can be ameliorated by dealing with the primes between, say,/8 and Δ (the “middle primes”) in a way similar to how the “large” primes are
handled. There is no such problem in step 10.
If there is enough space in the data caches to hold the mi variables, the informa-
tion where each list insertion point resides in memory, and one cache line for each
active list, then the speed of the algorithm does not change much as b is increased,
as illustrated in Figure 2.
An auxiliary sieve, updated using, for example, Algorithm 1.1, can be used to
compute in an eﬃcient way the sequence of the primes p used by Algorithm 1.2.
The speed of both algorithms can be slightly improved by changing the way the
variables mi are initialized. For example, it is possible to set i to 7 in step 2
of both algorithms if the mi variables are initialized with a precomputed pattern

License or copyright restrictions may apply to redistribution; see https://www.ams.org/journal-terms-of-use

2038 T. OLIVEIRA e SILVA, S. HERZOG, AND S. PARDI

xTime(inseconds)
10
10 10
11 10
12 10
13 10
14 10
15 10
16 10
17 10
18 10
19
0

2

4

6

8
 •◦
• •◦
• •◦
• •◦
• •◦
• •◦
• •◦

• •◦

•
 •◦

•
 •◦

•
 •◦

•
 •◦

•
 •◦

•
 •◦

•
 •◦

•
 •◦

•
 •◦

•
 •◦

•
 •◦

•
 •◦

•
 •◦

•
 •◦

•
 •◦

•
 •◦

•
 •◦

•
 •◦

•
 •◦

•
 •◦

•
◦ — Intel 2.83GHz Q9550 Core2 Quad
• — AMD 2.20GHz Athlon64

Figure 2. Time needed to generate all primes in an interval of
2
30 integers centered at x using a simple implementation of Algo-
rithm 1.2 [34, second program version] (see also [25]), for the two
processors described in Figure 1 (only one core used on the Intel
processor). The initialization time, about half a minute for thex on the slower processor, was not taken into considera-
tion. For x =10
19 this algorithm is about 8.4 times faster than
Algorithm 1.1 on the Athlon64 and about 4.4 times faster on the
Core2 Quad. Note that the improvement is larger on the processor
with the smaller L2 cache.

determined by the ﬁrst 5 odd primes (this pattern has a period of 3×5×7×11×13).
Of course, each mi variable should be associated with a single memory bit.
In a practical implementation of Algorithm 1.2 the memory used by each list
should grow as the need for it arises, i.e., it should be a linked list. Furthermore, at
most 2 + ⌊ √
B
∆ ⌋ linked lists can be non-empty at any given time. A circular buﬀer
with a suitable size (a power of two is particularly useful) should then be used to
store pointers to the insertion points of the linked lists. In order to use the data
caches in an eﬃcient way and to take advantage of the automatic memory prefetch
mechanism of contemporary processors each linked list should be subdivided in
relatively large chunks (each with, say, 4096 bytes of memory). The starting address
of each chunk should be a multiple of the processor’s data cache line size. Due to
the large chunk size of each linked list component, the memory overhead needed to
manage the linked lists is very small. Hence, the memory used by Algorithm 1.2 is
only slightly larger than that used by Algorithm 1.1.
The single-threaded 32-bit prime generation code used in our empirical veriﬁca-
tion of the Goldbach conjecture is capable of generating primes up to (30 × 2
26)2 ≈
4.05 · 10
18. It uses a modulo 30 wheel [37, 38] variant of Algorithm 1.2, i.e., only
the numbers which are not multiples of 2, 3 and 5 are represented in the sieve.
This complicates the algorithm but makes it almost twice as fast; near 1018 the
average number of clock cycles required to determine if an odd integer is prime or
not dropped from 14.8to8.7, and from 22.1to10.5, respectively, for the Core2
Quad and for the Athlon64 processors described in Figure 1. Assembly language
was also extensively used.

License or copyright restrictions may apply to redistribution; see https://www.ams.org/journal-terms-of-use

EMPIRICAL VERIFICATION OF THE EVEN GOLDBACH CONJECTURE 2039

Table 2. Empirical average value of i when Algorithm 1.3 termi-
nates for intervals of the form (
10
12k, 10
12(k +1))
.

ki-average i-average
log(k+1/2)+12 log 10
115.58519 0.55589
10 16.67964 0.55631
100 17.93997 0.55643
1000 19.22367 0.55657
10000 20.51067 0.55673
1 00000 21.79939 0.55690
10 00000 23.08907 0.55708

1.2. Computation of the minimal Goldbach partition of all even numbers
belonging to a given interval. We begin by presenting a simple algorithm,
capable of computing the minimal Goldbach partition of a single even number n.
It will be used by a more eﬃcient algorithm, presented below, to deal with the
(rare) cases not dealt with by that algorithm.

Algorithm 1.3 (Computation of the minimal Goldbach partition of n). To com-
pute the minimal Goldbach partition n = p(n)+ q(n), do:
1. [Initialize.] Set i to 2.
2. [Test.] If 2pi >n then terminate, stating that there is no Goldbach partition
of n.
3. If n − pi is prime, then set p(n) to pi and q(n) to n − pi,and terminate.
4. [Try next prime.] Increase i andgoback tostep2.

It was found empirically that the average value of i when this algorithm termi-
nates (successfully) is approximately 0.557 log n (cf. Table 2). This, and the clock
cycles lost due to a branch misprediction that is usually present when the algorithm
terminates makes it too slow to be used in the computation of the minimal Gold-
bach partition of all even integers belonging to a large interval. That can be done
eﬃciently using a segmented version (not presented) of the following algorithm.
1

Algorithm 1.4 (Computation of the minimal Goldbach partition of all even num-
bers belonging to an interval). To compute the minimal Goldbach partition for all
even numbers belonging to the interval (C, D),with C and D odd, do:
1. [Initialize.] Set I to a value that depends on D and on the processor model
(see below). Set J to (pI +1)/2.Set L to (D − C)/2.Set u0, u1, ...,
uL+J−1 to zero.
Comment: ui will contain information about the smallest prime in the min-
imal Goldbach partition of C +1+2i.
2. [Mark.] For each prime q belonging to the interval (C − 3,D − 3),ordered
in increasing order, do step 3 (a subroutine) with j set to (q − C)/2.After
all primes q have been dealt with, go to step 4.
3. For i =2, 3,... ,I,set k to j +(pi − 1)/2 and then set uk to i.
Comment: uk may be updated latter with a smaller i value (larger q prime).

1We rediscovered this way of speeding up Algorithm 1.3. Haussner used a similar idea to speed
up the construction of Goldbach partition tables up to 104 [1]. The algorithms used in [19, 40, 46]
only compute the minimal Goldbach partition when p(n) is larger than an implementation-deﬁned
limit; also, they loop on n and not on q.

License or copyright restrictions may apply to redistribution; see https://www.ams.org/journal-terms-of-use

2040 T. OLIVEIRA e SILVA, S. HERZOG, AND S. PARDI

Table 3. Best average number of clock cycles (Tavg)usedby
Algorithm 1.4 to compute p(n), and to collect statistical data,
foraneveninteger near x, and the corresponding best value of
the I parameter for two diﬀerent processor models (cf. Figure 1);
for the Core2 Quad I ≈ 2.50 log x − 13.7, and for the Athlon64
I ≈ 2.83 log x − 12.4.

Core2 Quad Athlon64
xTavg I I+13.7
log x Tavg I I+12.4
log x
1012 9.837 56 2.523 8.234 66 2.837
1013 9.788 61 2.496 8.238 72 2.820
1014 9.746 67 2.503 8.212 79 2.835
1015 9.714 72 2.481 8.195 85 2.820
1016 9.707 78 2.489 8.210 92 2.834
1017 9.701 84 2.496 8.207 98 2.820
1018 9.707 90 2.502 8.226 105 2.833

4. [Finish.] For i =0, 1,... ,L − 1,set n to C +1+ 2i;if ui is not zero then
set p(n) to pui; otherwise compute p(n) using Algorithm 1.3 (with i set to
I +1 in its ﬁrst step). Set q(n) to n − p(n).

In other words, for each prime q belonging to the interval (C − 3,D − 3) one
updates the array u in the positions corresponding to the even integers 3 + q,5 + q,
..., pI + q with the values 2, 3, ..., I. In the end, the number stored in each array
position will be either zero, if no Goldbach partition was generated for the even
number corresponding to that position, or the index of the smaller prime of the last
Goldbach partition that was generated for that even integer (it will be the minimal
Goldbach partition if the primes q are processed in increasing order). In the former
case the minimal Goldbach partition has to be computed using Algorithm 1.3.
It turns out that the choice I = ⌊α log D + β⌋, with α and β parameters that
depend on the processor model, approximately minimizes the execution time of
the algorithm. This is illustrated in Table 3, which presents best I values and the
corresponding average number of clock cycles per even integer used by our most
eﬃcient implementation (in assembly) of a segmented version of Algorithm 1.4
for the two processors described in Figure 1. Remarkably, the average number of
clock cycles remains practically constant. This is so because for the best I the
amount or work done in steps 2 and 3 of Algorithm 1.4 is approximately given byD − C)(α + β/ log D), i.e., it does not change much with D when D − C is held
constant, and because for the best I the relative frequency that Algorithm 1.3 is
invoked in step 4 of Algorithm 1.4 is approximately inversely proportional to log D.
In order to make Algorithm 1.4 as fast as possible, the loop of step 3 should be
unrolled. In our ﬁnal implementation when the computation starts, self-modifying
assembly code is used to trim this unrolled loop to the appropriate value of I.Fur-
thermore, each loop iteration is performed by a single move immediate instruction,
using the base register plus constant oﬀset addressing mode (depending on the pro-
cessor, up to two such instructions can usually be executed in each clock cycle).I is large enough, then in step 4 ui will be non-zero with a relative frequency
close to one. The test “ui is not zero” will then not be mispredicted often by the
processor, and the slower Algorithm 1.3 will be invoked rarely.

License or copyright restrictions may apply to redistribution; see https://www.ams.org/journal-terms-of-use

EMPIRICAL VERIFICATION OF THE EVEN GOLDBACH CONJECTURE 2041

1.3. Computational details and error detection and correction measures.
Our code was developed in 2001 for Intel/AMD (x86 instruction set) single-core
32-bit processors. Although later a 64-bit instruction set for AMD/Intel processors
appeared, given the initial large investment in both the optimization (assembly
language, software pipelining) and in the veriﬁcation of the correctness of the code
(the output of each assembly language routine was compared to the output of a
slower C language routine that used a simpler fool-proof algorithm), it was deemed
prudent to not produce a 64-bit version of the code. Given the programming
techniques used, it was estimated that a 64-bit version would be a few percent
faster that a 32-bit version.
The entire computation was split into disjoint intervals of 10
12 integers; the
k-th interval, 0 ≤ k< 4 · 10
6, covers the even integers that satisfy the conditions
max(4, 10
12k) <n ≤ 10
12(k+1). Testing each interval required between eight hours
(in the year 2001) and about forty minutes (in the year 2012). Processors with more
than one core can test in parallel, with a very mild degradation in performance, a
number of intervals equal to the number of cores they have. On Intel processors
with hyper-threading capabilities, testing two intervals on the same processor core
takes between 50% (core i7) and 80% (core i3) more time than testing a single
interval on that core (a gain between 2/1.5and 2/1.8).
A master-worker paradigm was used to automatically manage the computations:
a central master, used to distribute the intervals among a pool of workers and to
collect the data of processed intervals, and many workers that did the actual testing
work. Each worker had a unique ID and was capable of processing several intervals
without contacting the master. Intervals not processed within a prespeciﬁed time
limit were redistributed to other workers. Windows and GNU/Linux versions of
the worker code were produced (to ensure correctness, the low-level functions were
exactly the same in the two cases). A worker was also capable of working without
a master; that capability was used on high-performance computing environments.
In those cases, the distribution of the intervals and collection of results was done
using semi-automatic tools specially developed for that purpose.
The data computed and recorded for each interval of 10
12 integers includes:

• two worker IDs (intervals can be double checked by workers with diﬀerent
IDs), and the respective number of seconds that were used to process them,
• counts of the number of primes in each of the 32 primitive residue classes
modulo 120,
• counts and the ﬁrst occurrence of minimal Goldbach partitions with a given
smallest prime,
• counts and the ﬁrst occurrence of gaps between prime numbers, and
• a 32-bit cyclic redundancy check sum.

(Due to an unfortunate oversight, a high-precision approximation to the sum of the
inverses of the twin primes was not collected.) The entire data was stored in 4000
ﬁles, each holding information about 1000 intervals, using a total of about 27GB of
storage space.
The processed data of an interval received from a worker was screened by the
master to detect obvious errors: the sum of the counts of minimal Goldbach par-
titions had to match the number of even numbers belonging to the interval, and
the sum of the counts of prime gaps had to match the sum of the primes in the
residue classes modulo 120. These two tests never failed. The following oﬄine

License or copyright restrictions may apply to redistribution; see https://www.ams.org/journal-terms-of-use

2042 T. OLIVEIRA e SILVA, S. HERZOG, AND S. PARDI

screening test was then performed for each interval of 1012 integers: the computed
number of primes belonging to the interval was compared to an independent count
obtained using the ﬁrst author’s implementation of a combinatorial method to com-π(x) [8, 27, 35] (this extra data was generated using about 20 one-core CPU
years). It turned out that this test was very good at detecting bad results. This
happened on a few occasions in the early stages of the computation (and very, very
rarely later on), when personal computers, in particular, their memory subsystems,
were less reliable than those that can be bought in 2012 (when the computations
reported in this paper were ﬁnished). Once a bad result was detected the entire
interval was recomputed, the computer that produced it was black-listed, and all in-
tervals previously processed by that computer were double-checked. This procedure
did not uncover more bad results.
Some time after the veriﬁcation limit of 1018 was reached, the number of primes
in the residue classes modulo 4 reported in [9] was compared to those counted in
our veriﬁcation eﬀorts. To our dismay, a discrepancy of one was found in two of
the residue classes between 3 · 10
17 and 4 · 10
17. Fortunately, Mark Del´eglise’s
program was publicly available. Using it, a bisection strategy allowed us to locate
quickly the interval with the bad result. This was dealt with as described at the
end of the previous paragraph. To reduce considerably the probability of a (very
rare) error of this kind to remain undetected, a ﬁnal screening test was performed,
this time for each interval of 1015 integers: the counts of the primes in the residue
classes modulo 120 were compared to the counts obtained using Del´eglise’s program
(this extra data was generated using about 10 one-core CPU years). No further
discrepancies were detected.
As a ﬁnal precaution, the entire interval up to 3 · 10
17 was double-checked, and
the intervals containing one of the ﬁrst 100 occurrences of a smallest prime in a
minimal Goldbach partition or of a prime gap, as well as about 4% of the remaining
intervals were also double-checked. No further discrepancies were detected. As
expected, no errors were ever found on computations done on high-performance
computing environments (they account for about 25% of all our data). We are
therefore highly conﬁdent that all of our counts and ﬁrst occurrences are correct.
We feel that further double-checks are best left for a future still larger veriﬁcation

2. Results

In this section we present some results extracted from the data collected by our
conﬁrmation of the truth of the even Goldbach conjecture up to 4 · 10
18. In subsec-
tion 2.1 we present record values of ﬁrst and late ﬁrst occurrences of a prime in a
minimal Goldbach partition, test the conjecture [19] that p(n)= O(log2 n log log n),
and compare the number of occurrences of a given prime in the minimal Gold-
bach partitions up to 4 · 10
18 with predictions made using the inclusion-exclusion
principle applied to the prime k-tuples conjecture [21]. In subsection 2.2 we do
the same, but for prime gaps (testing this time the conjecture [7, 18, 43] thatn+1 − pn = O(log2 n)). In subsection 2.3 we compare prime gap moment data
with corresponding predictions made by a conjecture of Heath-Brown [23]. Finally,
in subsection 2.4 it is shown that our new veriﬁcation limit of the even Goldbach
conjecture can be used to prove without extra computation that the odd Goldbach
conjecture is true up to 8.37 · 10
26.

License or copyright restrictions may apply to redistribution; see https://www.ams.org/journal-terms-of-use

EMPIRICAL VERIFICATION OF THE EVEN GOLDBACH CONJECTURE 2043

Table 4. Record-breaking values of p(n)for n ≤ 4 · 10
18.

np(n) np(n) np(n)
6 3 107 59922 829 834 29455 44436 3917
12 5 241 06882 929 1059 16059 00482 4003
30 7 277 89878 997 1298 22701 97518 4027
98 19 379 98938 1039 1519 79009 94218 4057
220 23 601 19912 1093 2899 80506 50046 4327
308 31 1136 32822 1163 4687 84427 66282 4519
556 47 1878 52862 1321 7690 35744 97118 4909
992 73 3350 70838 1427 18416 24778 60248 5077
2642 103 4199 11924 1583 21736 13167 06568 5209
5372 139 7210 13438 1789 38996 50268 19938 5569
7426 173 18471 33842 1861 1 04761 05758 36828 6469
43532 211 74732 02036 1877 6 25326 23459 30828 6961
54244 233 1 10010 80372 1879 24 92555 60081 75266 7559
63274 293 1 27039 43222 2029 31 28417 79105 28922 7753
1 13672 313 2 12485 58888 2089 121 00502 23040 07026 8443
1 28168 331 3 58840 80836 2803 255 32912 66885 55994 8501
1 94428 359 10 59638 12462 3061 258 54942 69161 49682 8933
1 94470 383 24 48855 95672 3163 555 27435 15567 50822 8941
4 13572 389 59 95335 46358 3457 887 12380 30778 37868 9161
5 03222 523 313 20592 94006 3463 906 03057 95622 79642 9341
10 77422 601 362 08211 73302 3529 2795 93511 65744 69638 9629
35 26958 727 443 83276 72994 3613 3325 58170 73339 60528 9781
38 07404 751 532 05038 15888 3769

2.1. Minimal Goldbach partitions. As in [19], let S(p) be the smallest even
integer n for which p(n)= p and let L(p, x) be the number of even integers not
larger than x for which p(n)= p. Table 4 presents the record-breaking values of
p(n), i.e., values of p(n) larger than those for all smaller values of n (sometimes
also called maximal values), that were found in this veriﬁcation. It extends Table 3
of [4], Table 3 of [19], Table 1 of [46], and Table 1 of [40]. Table 5 presents the
record-breaking values of S(p) that were found. It extends Table 2 of [46].

2.1.1. Conjectures concerning p(n) bounds. In [19] it was conjectured that p(n)=
O(log2 n log log n). In an email exchange in April 2012, Andrew Granville, us-
ing probabilistic arguments, suggested to the ﬁrst author two more precise (in-
compatible) conjectures, both of the form p(n) ≤ (C + o(1)) log2 n log log n:one
with C = C −1
2 ≈ 1.51478 and another, using a more reﬁned argument, with
C =2e
−γC −1
2 ≈ 1.70098, where C2 ≈ 0.66016 is the twin primes constant and
where γ ≈ 0.57722 is Euler’s constant. To test these conjectures, Figure 3 presents
a plot of the values of
 Q1(p)= p
log2 S(p) log log S(p)

that we were able to compute. For our data Q1(p) clearly stays below 1.7and only
two points lie above 1.514: Q1(3) ≈ 1.60231 and Q1(6469) ≈ 1.52627. As explained
in subsubsection 2.1.3, our empirical L(p, x) data suggests that the slowly increasing
trend that can be observed in Figure 3 will not persist for ever. Given that these
conjectures allow a ﬁnite number of solutions of Q1(p) >C + ǫ, and taking into

License or copyright restrictions may apply to redistribution; see https://www.ams.org/journal-terms-of-use

2044 T. OLIVEIRA e SILVA, S. HERZOG, AND S. PARDI

Table 5. Record-breaking values of S(p)for S(p) ≤ 4 · 10
18.

pS(p) pS(p) pS(p)
3 6 1049 3794 10652 4133 21528 58899 79816
5 12 1061 5544 63808 4241 28078 06211 53342
7 30 1091 6785 46502 4373 31924 55155 37554
11 124 1097 11688 88534 4457 33263 84502 61204
17 418 1283 16732 68292 4523 44568 54135 00946
37 1274 1301 19275 28888 4621 55724 95547 49362
53 2512 1327 23314 65314 4643 65020 45060 20934
59 3526 1429 25388 33642 4679 66695 60251 01272
71 4618 1439 28165 93312 4721 81441 08625 37738
83 7432 1451 44071 65118 4733 1 02520 38425 12482
89 12778 1493 58018 28806 4817 1 24657 87228 03144
101 26098 1559 89466 30856 4937 1 84205 42851 36636
131 34192 1571 2 14399 65412 5051 2 30360 82907 75108
149 37768 1787 2 60702 02114 5087 2 74844 32963 52086
167 59914 1811 3 03257 42068 5227 3 77167 15201 32578
179 88786 1867 3 08343 71756 5333 4 46303 92199 37862
191 97768 1873 3 26526 27542 5471 5 12249 86761 96358
197 1 12558 1889 4 44603 16708 5483 6 19847 81686 28056
223 2 21942 1907 6 42439 62808 5501 14 21174 44030 75144
257 2 37544 1997 6 53347 25368 5879 15 81237 99596 45512
263 4 85326 2027 11 38431 30358 5903 20 01798 63813 70774
281 6 42358 2153 24 48089 93116 5987 31 82162 58292 50454
317 6 86638 2351 38 46192 17512 6131 48 03378 79780 24768
347 10 42078 2441 74 38910 46202 6263 55 10400 89583 65746
379 11 72918 2459 83 88139 74892 6491 107 15720 71018 94788
401 20 41402 2663 157 80847 23724 6761 182 74530 72010 20658
419 24 06448 2837 254 12467 52056 6899 237 09861 61937 22886
463 42 88574 2963 322 83172 20754 7013 296 54004 27271 13116
487 49 38848 2969 604 65005 99278 7187 344 20574 38160 95468
509 92 92156 3023 711 95508 17194 7307 370 58110 67669 09188
521 143 41888 3137 740 55675 22324 7489 411 41162 99917 22966
569 177 26098 3203 1077 03538 52014 7577 558 61954 75699 07716
593 207 57292 3323 1745 51588 97256 7649 754 27622 88329 57188
659 325 07242 3449 1856 69525 90488 7691 813 69562 21921 68004
739 343 62758 3557 3636 14483 59204 7703 1473 61172 23318 22212
743 378 90844 3659 3902 83776 47218 7853 1599 56602 59143 18344
761 493 58128 3677 4085 46803 72224 7949 1793 16778 59048 03016
773 687 88066 3701 4477 67061 82504 8039 2043 43718 01888 10768
839 1297 96642 3761 5413 30158 34948 8087 2758 16342 81002 38178
853 1445 16902 3863 6091 30487 45092 8243 3244 40008 45058 12356
911 1503 86932 3923 10325 23255 78522 8273 3511 79756 73597 60604
941 2068 92484 4073 12998 77000 25542 8369 3714 75979 38306 49402
977 2470 13164 4079 14352 12522 89068 8387 3878 29701 74376 46306
1031 2994 34108 4127 19453 91791 43308 8423 > 4 · 1018

consideration the logarithmic scale associated to this problem, it seems likely that
much more data (up to 10
100 or even more) will be needed to empirically determine
C directly with some accuracy, and hence determine which of the two conjectures
is more plausible.

License or copyright restrictions may apply to redistribution; see https://www.ams.org/journal-terms-of-use

EMPIRICAL VERIFICATION OF THE EVEN GOLDBACH CONJECTURE 2045

pQ1(p)
0 1000 2000 3000 4000 5000 6000 7000 8000 9000 10000
0.0

0.4

0.8

1.2

1.6
 ·
···
····
·
·
·

·
·
·
·
·····
·
·
·
·
·
·
·

·
···
·
··
·
··
···
·
·······
·
·
······
··
·
··
·
·
···········
·
····
·
··
·
····
·
······
·
·
··
····
·
··
·
··
·
···
···
·
·
···
······
··
··
··
··
·····
···
···
·
·
···
·
···
··
·
······
·

··

·

·······
·
······
··
·
···
··
···············
·
·
···
··········
···
··
······
···
····
·
·
···
·
····
·
··
·
··
··
·
·
·
···
·
··
·
······
·
····
·
···
··
··
·
··········
·
··
·
··
····
··
·
··
··
·
····
·
··
··
··
·

·
·
·
···
···
·
·
·
·
·

·
·
·
······
····
···

·

·
·
·
·
··
·
·
·
···
······
·
···
·
·········
·
····
·················
·················
··
···
·
··
···
·
···
··
·················
·
··
·
·········
·····
·
·
·
······
··
·
····
····
····
·
·
·
··
·
······
······
·
··········
·······
···
·
·····
····
··
·
·
···
······
·
·····
·
···
·
·····
··
··
··
····
··········
····
··
········
·
·
····
······
··
····················

·
·····
·
··
·
·
·
·
·····
·
··
·
··
·
·
·······
·····
·
·
···
·
·
·····
·
·········
·
·······
··
···
·
·
··
·····
···
·
······
·
·
·······
··
··
···
···
····
·
·
·
·
······
·····
·
······
········
·
······
·
······
··
·
·
··
······
·
····
·
·
·
····
·
·······
·············
····
·
·
······
·
···
·······
·
·······
·
····

•◦
•◦
•◦
•◦•◦
•◦•◦•◦•◦
•◦
•◦•◦•◦•◦•◦•◦
•◦
•◦•◦
•◦•◦
•◦•◦•◦•◦•◦•◦•◦
•◦•◦•◦
•◦•◦•◦•◦•◦•◦
•◦•◦•◦•◦•◦•◦•◦
•◦ •◦•◦•◦
•◦•◦
•◦•◦•◦
•◦ •◦•◦•◦•◦•◦•◦
•◦•◦•◦ •◦•◦•◦ •◦ •◦•◦
•◦•◦•◦•◦•◦•◦•◦•◦•◦•◦•◦•◦•◦ •◦•◦•◦•◦•◦•◦•◦•◦•◦•◦•◦•◦•◦•◦•◦•◦•◦•◦•◦•◦•◦
•◦ •◦•◦•◦•◦•◦ •◦ •◦•◦•◦ •◦•◦ •◦•◦•◦•◦•◦ •◦•◦•◦•◦ •◦•◦•◦•◦

•

•
•

•
•
•

••
•

•

•
•

•
•••
•

•
••••
••
•••• •• • •
•

•
• ••
 • •
• •

••• • •••• • • • •• •
 • • • • •
• •
• • • • •

Figure 3. Plot of Q1(p)for S(p) ≤ 4 · 10
18. Disks (•), circles (◦),
and dots (·) correspond respectively to data obtained from Table 4,
from Table 5, and to values of S(p) thatdid notmakeittoeither
of the two tables.

2.1.2. Estimate of L(p, x) using the prime k-tuple conjecture. Let h = {h1,... ,hk}
be a set of k distinct integers, all of the same parity, and let π(x; h)bethe number
of k-tuples (m + h1,... ,m + hk), with 1 ≤ m ≤ x, containing only primes. By the
inclusion-exclusion principleL(p, x)= − ∑

s (−1)|s|π(x; s),

where the sum is over all subsets s of {−3, −5, −7, −11,... , −p } which contain
−p,and where |s| denotes the cardinality of s. In [21] Hardy and Littlewood
conjectured, with c =2, that

(2.2) π(x; h) ∼ G(h) ∫ x

c
 dt

logk t ,

where G(h)=2
k−1 ∏

p
 (1 − νp(h)

p
 )(
1 − 1
p
 )−k

and where νp(h) is the number of distinct residue classes modulo p occupied by the
elements of h. Using this so-called prime k-tuple conjecture to approximate π(x; s)
in (2.1) yields ˆL(p, x)=
 π(p)−1∑

k=1 (−1)k+1Cp,k
 ∫ x

c
 dt

logk t ,

where Cp,k = ∑

|s|=k G(s). The Cp,k constants can be computed using a simple
adaptation of the method used in [6] to compute other constants of the same kind.
The ﬁrst author computed them all for p< 250 using about 16 one-core CPU
months. As an example of the general behavior of these constants, Table 6 presents
the non-zero values of C241,k.
It turns out that for relatively small values of x the lower limit of integration of 2
suggested by Hardy and Littlewood for (2.2) is a very bad choice for (2.4) when

License or copyright restrictions may apply to redistribution; see https://www.ams.org/journal-terms-of-use

2046 T. OLIVEIRA e SILVA, S. HERZOG, AND S. PARDI

Table 6. Non-zero values of C241,k (only 21 signiﬁcant digits shown).

kC241,k kC241,k
11.00000 00000 00000 00000 23 3.70204 14661 49439 69979 · 1024

21.13158 66859 65499 59139 · 102 24 1.31461 87368 38578 84258 · 1025

36.93019 94386 60869 24137 · 103 25 4.22256 92828 55965 63028 · 1025

43.00886 99646 95696 40719 · 105 26 1.22482 06601 55783 90143 · 1026

51.01640 78939 12162 69790 · 107 27 3.20204 63609 01368 30154 · 1026

62.79258 80742 87881 31431 · 108 28 7.52660 46955 07176 17022 · 1026

76.41741 99060 14428 77794 · 109 29 1.58609 30493 60132 31281 · 1027

81.25913 74972 52254 51935 · 1011 30 2.98608 21872 48675 88621 · 1027

92.14288 09248 75761 71467 · 1012 31 5.00143 91728 42627 39468 · 1027

10 3.20144 28071 44559 73700 · 1013 32 7.41494 33404 69631 24282 · 1027

11 4.23668 72148 78062 42359 · 1014 33 9.67103 74237 26498 34947 · 1027

12 4.99990 15938 62122 23271 · 1015 34 1.10137 98332 87079 45198 · 1028

13 5.28865 62801 63349 25545 · 1016 35 1.08516 76207 67543 49852 · 1028

14 5.03316 43841 95479 05620 · 1017 36 9.14471 69789 56584 84128 · 1027

15 4.32228 77040 16020 86166 · 1018 37 6.49627 26305 32786 34274 · 1027

16 3.35672 30146 84477 12695 · 1019 38 3.81830 48373 21482 47613 · 1027

17 2.36124 94061 35894 65715 · 1020 39 1.81159 68041 87622 69166 · 1027

18 1.50615 10047 65390 73306 · 1021 40 6.70676 47470 80130 86245 · 1026

19 8.71726 56912 30150 63187 · 1021 41 1.84470 56245 09659 86010 · 1026

20 4.57924 55341 30673 89384 · 1022 42 3.49098 59394 38777 29499 · 1025

21 2.18311 41710 01000 00195 · 1023 43 3.96213 08971 56314 45799 · 1024

22 9.44187 69191 50547 38724 · 1023 44 1.95366 73527 22360 22383 · 1023

accurate estimates are desired. For example, using c =2 we get ˆL(241, 10
4) ≈
−4 · 10
24, which is very far from its true value of zero, while using c =0 we get
ˆL(241, 10
4) ≈−1.23592, which is a much more reasonable estimate. Using c = p we
get ˆL(241, 10
4) ≈ 0.00084, which is again a very reasonable estimate.
2 The same
behavior was observed of all other values of p and of x that were tried. Therefore,
for simplicity of computation, in all of our comparisons between L(p, x)and ˆL(p, x)
a lower limit of integration of c = 0 was used. Furthermore, as illustrated in Table 7
for x =4 · 10
18 and p = 241, most of the non-zero Cp,k constants are important (for
x large enough all will be important).
Inspired by formula 5 of [7], which results from the application of the law of the
iterated logarithm [15] to a random counting function that attempts to mimic the
large scale behavior of π(x), it was decided to test the possibility that the large
deviation behavior of ˆL(p, x) − L(p, x) follows a similar law. Considering that it is
reasonable to expect that prime number patterns follow, asymptotically, a Poisson
distribution [16, 26], which implies that variances should be equal to means, one
may expect that ∣ ˆL(p, x) − L(p, x)∣ exceeds (1 + ǫ)√

2L(p, x) log log L(p, x)at most
a ﬁnite number of times. However, the law of the iterated logarithm assumes that

2It is necessary to avoid a lower limit of integration near 1, because ˆL(p, x) blows up in that
case (the principal values of the integrals present in (2.4) are used when c< 1and x> 1). It is
remarkable that, for c =0, ∣ ˆL(p, p)∣ < 6for p< 250. (We have no explanation for this behavior;
it implies an almost perfect cancellation of the large terms in the ﬁnite alternating series (2.4).)
Thus, both c =0 and c = p are reasonable lower integration limits (c = 2 in not), at least for
p< 250. The partial sums of (2.4) appear to converge faster when c =0 than when c = p.The
choice c = 0 has the added advantages of being more natural and being constant.

License or copyright restrictions may apply to redistribution; see https://www.ams.org/journal-terms-of-use

EMPIRICAL VERIFICATION OF THE EVEN GOLDBACH CONJECTURE 2047

Table 7. Approximation of L(p, x) by truncation of ˆL(p, x)to K
terms, for c =0, p = 241, and x =4 · 10
18.

K ˆL(p, x) K ˆL(p, x)
1 95 67626 09731 64698.5 10 6 29668 65710 23021.9
2 −163 45040 70427 19193.7 15 8 30450 15601 29840.7
3 216 63550 93958 03246.5 20 8 30304 11009 71376.4
4 −178 87696 79611 98263.7 25 8 30304 11896 68030.5
5 141 58277 14924 86186.5 30 8 30304 11896 67526.0
6 −69 77094 80643 09200.0 44 8 30304 11896 67526.0
L(p, x) 8 30304 11498 24931

xQ2(p,x)
10
10 10
11 10
12 10
13 10
14 10
15 10
16 10
17 10
18 10
19
−1.5

−1.0

−0.5

0.0

0.5

1.0

1.5
 ····
··

···
·

·

··
·

·
··
·

·
·
··

·
·
·
·

·

·····
··

·
·
·
·

·

··
·

··
··

·

·
·
·

·
··
·
··

·

······
·
··
·
·
·

·

·

···

·

·

·

·

·
··
·
·

·

·····
·
···
·
·
·

·

··

··
·

·

·

·
···

·
·

·

···
·
·

··
·
·
·
·
·

·
·
·
·
·

··

·

·
··

·

·
·

·

···
··
·

··
·
··
·

·

·
·

··
·

··

·

·
·

·

·
·
·

·

···
···

·
·

·
·
··
·

·
·

·
·

·
·

·
·
·
·

·
·
·

·

···
··

·
·

·
·
···

·
·

··
·

·

·

·
·

·

·
·

·

·
···
···

·
·

·
·
·
·

··
·
·
·

··

·

·

·

·
·

···
·
·

·
·
·
·
··

·
·
·

·

·

·
·

·
·

····
···
·
··
·

····

···

·

··

·

·

·

·

·

·
······
·
··
·

···

··
·

·

·

·
·

·

·

··
······
·
·
·

···
·

··
·

···
·

·
·

·

·

·

·····
·
·
··
·

···
·

··

·

·

···
·

·

·

·

·

·
··
··
·
·
·
·
··

···
··

·
·

·
·
··

·

·

·

·

·
····
·
·
·
·
··
···
·
·
··
·
·
··

·
·

·

·

·
····
··
·
··
··
·
·

·
·

···
·
·
·
·

·
·

·

·

·
··
··
··
·

·
···

·
·
··
·

·
·
·
··
··

·

·

·

····
·
···
·

··
·
·

·
·
··

·

·
·
··
·
··

·

·

·

···
·
···
·

····

·

·

·

·

·
··
·
·
·
·

·

·

·
····
·
···
·

·
··
·
·

·

·

·

·
·
··

·

·

·

·

·

·

···
·
·
··
·
···

·

·

·

··

·

···

·

·

·

··

·

·
···
·
·
·
·
··
···

·

·
·

·
·

·
·
··
·

·
·
·

·
·

·
····
·
·
··
·
·
·
··

·
·
·

··

··
·
··

·
··

·
·

·
·····
···
··

··

·
·

·

·
·
··
·
·
·
·
·
·
·
·

·
·
······
·····
·
··

·
·

··

·
·
·
···
·
·
··

··

·
·
····
·
···
·
·

·
··

··
·

··
··
·
·
·
·
··
·
·
····
··
·
·
·

··

··
·

··

·····
·
···
·
·

·····
··
·
·
·

··

··
·

·

··

·

··
·

·

·····
·
·
·
·
··
··
·

·
·

·
·
··

···

·
··
··

·

····
·
·
·
·
·

··
·
··

··
·
·
··

·
···

·

·
·
···
·
·····

·
··
·
·

··
·
·
·
·

·

··

·
·

·
·····
·
·
··

··

·
·
·
·
··
·
··

·
·
·
·

·
·

·····
·
·
·
·
··
·
·
·

·
··
···
··
·

···

·

·
······
·
·
·
··
·

·

·

·

·

·
·

··
·
·
··

·

······
·
·
·
·
··
··

·

·
·
·
·

·
·
·
·

···

·

·
·····
·
·
·
·

·
·
·
·

·

·
·
·

·

···

·
··
·

··
····
·
·
·
·
·
·
·
·
·

·

··
··
·

··

·
·
····

·
····
·

·
·
·
·
·
·
·
·

·
··
··
·

···
·
·
··
·

·
····
·
·
·

··
·
·
·

·

·

·
·

·

·
·
·
····

·
····
·
·
·

·
·
··

·
·

·

·

··

·

·
·
·

·
·

··
····
·
·
·

·
·
·

·
·

·
·

··

·

·
··

·

·

··
··
·
·
·

·····
·

·

·

·

··

·

·
·

·
·
·
·
····
·
·
·

····

·

·

·

·
·
·

·

·
··

·

·
·

·
····
·
·
·

···
··

·

·

·
··
··

·

·

·
·
·

··
·
·
·
·······
·

···
·
·

··
·
·
···
·

·
·
·
·
··
···
···
···
·

·
··
··

···
·
·
·
·
·

·

·
·

·
·
·
·

·
··
······
·

···
·
·
·
·

·

·
·
···

·
·
·

·
·
·

·
··
·
····
··
·

·
·

·
·
·

·

·
·

···

··
·

·

·

···
····
·
·

·
·

·
·
·

·
·
·

··

·

·

·

···

·

····
··
·
·
··
·
·
·

·

··

·
·

·

·

·
·
·

·

····
··
·
·
··
·
··
···
·

·
·

··

·
·

··
·

·
··
····
·
··
·
··
·
··

·
·
·
·

·

··

··
·

·

·
······
·
··
··
··
··
·

·

·
·

·

··
··

····

·

··
··
···
·
·····
·
··
·

·

·

·

··

·
·
·

·
·
··
·
·
··
·

···
·
·
····
·
·

·

·

·

·
·

·
·

··
·
·

·

···
·
···
···
·
·
·
·
·

·

·
·

·
·

··
·

·
·
·

·
··
·
····
·
·
·
·
·
·
·

·

·
·

·

·

·
···

·

·

·
·
···
···
·
·
·
·
·
·
·

·

·

·

·

·
·
·
·

·

·

··
·
·······
·
·

··
·
·
···

·

·

·

·

·

··
·

·

·

··

·
·
·

··
···
··

·
·
·
···

·

·

·

·

·

··
·

·

·

·
·

··
·
·
·····
··

··
·
·
·

·

·

·

·

·

·
·

·
·

·
·

·
·
·
····
···
·
·
·

·
·
·

·

·

·

·

·

·
·
·

·
·
·

·
·
··

···
··
·
···
·
·
··

·
·
·
·

·

··
·
·

·
·
·

·
·
·

···
·

···
·
···
····

·

·

·
·

·
·

··

·
···

····
··
··
·
··
··

··
·

·
··

·
·

··

··

··
·

····
··
···
··
··
··
·

·
··

·
·

·

·
·
··

······
··
·
·
·
·
··
·

·
··

·
·

··

····

·

·········
·
·
··
·
·

·
·
·

·
·
·
·

··

·
·

······
···
·

·
·
···
·
·

·
··

·
·

·
·

·

·
·
·

····
···
··
·
·

·
··
···
··
·
·
··
·
·

·

·
·
··

·········
··

··
·
·

··
···
··
·

·

·
·
··

·····
·
·
·
··
·
···

··
··
·
·
··

··

·
·

·

···
·····
·
··
·
···
··
···
·
·
·

··

·

·

··

······
·
···
··
·

·
····
·

·
··

·

·

·

··

····
··
·
···
·
·
··

·
·
····

·
··

·

·

·

··
···
·
····
·
··

·

·

··
··
·

·

·

·
·
·
····
·
··
·
·
·
··

·

··
······

·

·

····
······
···
·
···
·
·

·

·
·
···
··

·

·

····
····
·
·
·····
·
·

··

·

·
·
··

··

·

·
·
··
····
·
·
·
····
·
·
·

··

··
·
·
·
··

·

·

··
····
·
·
·
···
··

··

··

·

·
·
·
··

·

········
·
·
··
···
·

·
·
··

·
·

···

·

·
·
······
·
··
·
··
·
·
·

·
·
··

···
··
·

·

·
·
·
·····
····
··
·
··

·
·
··

·
·
··
·
···

·

·
·
·
·····
·
·
··
·
··
·
·
··

·

····
··

·

·
·
·
·····
·
·
··
·
·
·
·
··

·

···

·

·

·
·

·
·····
·····
·
··
··
·
··

·

·
··
·

·

·
·

·
·
····
·
······
·
·
··
·
·

·

··
·

·

·
·
·

··

·
····
··
····
·
·
·
···

·

··
·

·

·
··

·
··

·
····
·
·
··
··
·
·
·
·
·

·

·
·

·

·
··

··

·

·
····
·
·
··
··
·
·
·
·
·

·

·
·

·

·
···

··
·

·
··
·
··
·
··
···

·

·
·

·

·
·

·

·
···

·
·

·

···
·
···
··
··

·
·

·

·

··

·

··
·
·
··

·
···
·
··
·····
·

·
·
·

·

··

··

·
··
··
··

·

···
·
···
·
··
·

·
·
·

·

··

·
·

·
···
·
··

·

···
·
··
···
·

·
·
·

·

··
·
·
·····

·

·

···
·
··

·
··
·

·
·

·

·

·
··
··

·
··

··

·

···
·
·

·
····
·

·
·

·

·

·
·
··

··
··

·
·
·

·
···
·
·

·
··
··

·

·

··

·

·
··
··
··
·

··

·

·
···
·
··

··
··
··

·

·

·

·

··
··
·

·
·
··

·
·

·
···
·
·
··

··
·
·
·

·

·
·

·

·
··
··

·
·
··

·
·

·
···
·
·

··

···
··

·

·
·

·

··
·
·

·
·
···

·
·

·
···
·
··

·

··
··

·

·
·

·

··
·
·
·
·
··

·
·

·
···
·
··

·

·
·

·

·
··

·

·

·
·
·
···

·
·

·
···
·
··
··
·
·

·

·

··

·

·

·
·

··

·
·

·
····
·
·
·
·

·

·
···

·

·

···

··

···

····
·
··
·

·
··

·

·

··

·

·

··

·

···
·····
··
·

···

·

·
·
·

·

··
·····

·
·

··
·
·····
····

···

·

·
···

·
·

·
·

·

·

··

···
···
·······

···

·

·

··
·

·
·

··

·
···
·
·
·
·
····
···
··

···

·

·
··
·

··
··

·
·
··
·
·

·
········
··

·
·

·

·
··

··

··

·

··
·
·

·

·
·····
·
··
·
··
·

·

·
·

···

··

·

·
·

··

·
··
·····
··
·
·
··
·

·

·
·

··

··

·

··

·
··
·
··
···
·
·
·
··
··

·

·
·

·
··
··

·

··

··
·
·
····
·
·
·
··
··
·

··

··
·
·
·

·

·
·
·
··
·
····
·
·
···
··

·

··
·
·
·
·
··

·

·
·

··
··
···
·
·
··
·
·

··
·

·····
·
·

·

·
·

···

··
····
·
·
·
·
·
·

····

··
·
·
·

·
·
·

·
···
····
·
·
·
·
·
·

·
··

·
···
·

·

·
·
·

···
··
····
·
·

·
·
·

·

····
·
·
··
·

·
·

·
·

··
·
········
·
·

··
·
·

···
··
·
·
·
·

·

·
·
·

·
······
·
·

·
·
·

·

·····
·
·

··

·

·
··

·
·
··
····
·
·
·
·
··

··
··
··
·
·

··

·

·
·
·

·

·
··
·····
··

·
·
··

··
··
·
··

··
·

···

··

·

··
···
····
····

·

··
·
·
··
··
·

··

·
·

·
·
········

·
···

·

·
·
·
·
·
·
·
·

··
·
·

·
·

···
···
·

···
·

·

·
···
·
·
·
·

·

··
·

·
·

···
···
·

·
·
·

·

·
·
·
·
·

··

·

··

·

·
··

···
·
·

·
·
·

·

··
·
·

·
·

·
·

·

···
·

·
··
···
·
·

·
·
·

·

···
·
·
·
·
·
·

··
·
·

·
·
·
···
···
·

·
··
·

·

··

·
·
·
·

·

··

···

·

··
·

···
··
·

·
··

·

·

·
··

·
·
·
·

··

·

·
·

···
···
·

·
··

·

·

·

·
·

·

·

··
·
·

··

···
···
·

·
·
·

·

·
·

·
·

·

·

·
··
·

··

···
··
·
·
··
··

·

·
·
·
·

·

·

·
···

··

·
···
···
·

····

·

·
·
·
·

··

·

··
··
··
·
···
···
·

···

·

·
·
···
·

··

·
·
·
·····

···
···
·

·
···

·

··

···

·
·
·
·
··
··

····
···
·
··
··

·

·

··
·

·

···
·
··
·
·

······
·
·
··

·

·

··
·
·
·
·
·
··
··

·····
·
··
··

·

··
·
·
·
·
··
·
···
·····

····
·
·
··
··

··

·
···
·
·
·
·
···

····

···
·
·
··
·
·

·

·
··
·
·
·
·
·
·
··
·
·
·

··
··
·
·
·
··

·

·
··
·
·
·
·
·
··
·
·
·
·
·

····
·
··
··

·
·
··
·
·
·
·

·
··
·

·
·

·

····
·
···

·
·
·
·
·

··
·
····
·

··
·

·····
·
····
·

·
·
·
·

·

·
···
·

·
·

···
·
·
···
·

·
·
··

·
·

·
·

·
·

·

···

···
·
·
···
·
··

··
·
·
·
·

·

·
·
·

··
·

···
·
·
··
·
·
·

··
·
·
··
·
·

··
··

··

···
·
··
·
·
·

·
·
·
·
·

·
·
·

··
·
·

··

····
·
··
·

·
·

·
·

·
···
·
·

··
··
·

··

·

·····
·
···
·
·

·
·
··
··
·
··
·

·
···

·
·

····
·
··
··

·
·

·
·
·
··
·
·
·
·
··
·
·

·
·
·

····

·
···

·
·

·
··
··
·
··
·
····
·

·
·
··

····

·
·
·
·

··

··
·
·
·
·
·
····
··
·

·
··

···

·
··
·

··

··
·
·
··
··
···
·
·

··
·

···

·

····
·

······
··

··
···
·

·
···

··
·

·
·····
··

··
·
····
··
·
·

·
·
··
·

···
·

·
·····
··

··
·····
····
·
·
·
···

···
··
·
····
·
·

·
·
·······
··

·

·
··

···
··
·
··
·
·

·
·
····
··

·

·
·
·
·

··
··
····
··

···

·
··

····
·
·

·
····
··
··
····
···
·
·

··

·
···
·
·

···
··
··
··
···
·
·
·
·
·

··
·
·
·
·
·

··
·
··
·
··
··
··
·
··
·
···
···

·
·
·
··
·
·
···
·
···
·
·
··
···
··
·

····
·
··
··
··
···

···
·
·
····

·
·
··
·
·
·
·
·
·
·
·
·

·
···
·
·

···

·
·
··
·
·
·

····
··
·
··
··
·
···
·

····

·
·
···

·
·
·
···
·

·
·

·
·
·
···
·
···
·
·
··

·
·

·
·
··

·
·

·

·
··

Figure 4. Plot of Q2(p, x)for p< 250 and for some values of x.

the random variables are independent, which is not the case here, so the above
bound may not be correct. Nonetheless, one may hope that it captures the correct
order of magnitude of the error term. To test this, Figure 4 presents a plot of some
values of
 Q2(p, x)= ˆL(p, x) − L(p, x)

√
2L(p, x) log log L(p, x) ,

for p< 250 and for selected values of x between 10
10 and 4·10
18 (twenty per decade,
approximately equispaced on a logarithmic scale). From this ﬁgure it appears thatQ2(p, x)∣ may indeed be bounded (if not its growth rate should be very, very small).
It also appears that the factor of two inside the square root may be slightly too
large. These empirical observations suggest that, asymptotically, one should have

∣ ˆL(p, x) − L(p, x)∣ = O
 (√
 x log log x
log x
 )

(since Cp,1 = 1 one has ˆL(p, x) ∼ x
log x , and so one should also have L(p, x) ∼ x
log x ).

2.1.3. Rate of decay of L(p, x). It appears that, on a logarithmic scale, L(p, x)does
not deviate much from π(x)exp
(
−(π(p) − 2)/(0.755 log x − 4.19))
. This empirical
result was obtained by ﬁrst using best least-squares ﬁts to approximate log L(p, x)
by m1(x)π(p)+ b1(x) for several values of x between 10
10 and 4 · 10
18 (discarding

License or copyright restrictions may apply to redistribution; see https://www.ams.org/journal-terms-of-use

2048 T. OLIVEIRA e SILVA, S. HERZOG, AND S. PARDI

π(p)Q3(p)
0 100 200 300 400 500 600 700 800 900 1000
0.0

0.3

0.6

0.9

1.2
 •◦
•◦•◦
•◦
•◦
•◦•◦
•◦
•◦•◦
•◦
•◦•◦
•◦•◦•◦
•◦•◦
•◦
•◦•◦•◦
•◦•◦•◦
•◦•◦
•◦•◦•◦
•◦
•◦•◦•◦•◦
•◦
•◦•◦
•◦
•◦•◦•◦•◦•◦
•◦•◦
•◦
•◦
•◦
•◦
•◦
•◦•◦•◦•◦
•◦
•◦
•◦
•◦
•◦
•◦
•◦
•◦•◦
•◦•◦
•◦
•◦•◦•◦
•◦
•◦
•◦•◦•◦
•◦
•◦
•◦

•◦

•◦
•◦•◦•◦•◦•◦
•◦•◦
•◦•◦•◦•◦
•◦
•◦
•◦•◦
•◦
•◦
•◦•◦•◦•◦
•◦•◦
•◦
•◦
•◦
•◦•◦
•◦
•◦•◦•◦•◦
•◦
•◦
•◦
•◦
•◦•◦
•◦
•◦
•◦
•◦

•◦•◦•◦•◦
•◦
•◦•◦
•◦
•◦
•◦
•◦
•◦•◦
•◦•◦•◦
•◦
•◦•◦
•◦
•◦
•◦•◦
•◦
•◦•◦
•◦•◦
•◦•◦
•◦
•◦

•◦
•◦
•◦
•◦
•◦

•◦

•◦
•◦
•◦•◦•◦
•◦
•◦

•◦•◦•◦•◦•◦
•◦
•◦
•◦•◦
•◦•◦

•◦•◦•◦•◦
•◦
•◦•◦
•◦•◦
•◦
•◦

•◦
•◦
•◦
•◦
•◦
•◦•◦
•◦
•◦
•◦•◦

•◦
•◦•◦•◦
•◦

•◦
•◦

•◦

•◦

•◦
•◦

•◦
•◦
•◦•◦
•◦•◦•◦
•◦
•◦
•◦

•◦

•◦
•◦•◦

•◦•◦
•◦
•◦
•◦
•◦
•◦•◦•◦•◦
•◦

•◦
•◦
•◦
•◦

•◦
•◦
•◦
•◦•◦
•◦•◦•◦•◦
•◦
•◦•◦
•◦
•◦
•◦
•◦•◦
•◦
•◦
•◦
•◦•◦
•◦
•◦

•◦

•◦

•◦
•◦

•◦•◦•◦

•◦
•◦
•◦

•◦
•◦

•◦
•◦•◦

•◦

•◦

•◦
•◦•◦•◦
•◦
•◦
•◦•◦•◦
•◦

•◦•◦•◦

•◦
•◦•◦
•◦•◦

•◦

•◦•◦

•◦

•◦

•◦
•◦
•◦
•◦•◦
•◦•◦
•◦

•◦
•◦

•◦

•◦
•◦

•◦

•◦

•◦
•◦

•◦

•◦

•◦
•◦•◦
•◦
•◦

•◦

•◦

•◦

•◦
•◦
•◦•◦

•◦

•◦

•◦
•◦

•◦

•◦

•◦•◦

•◦

•◦

•◦•◦•◦

•◦

•◦

•◦
•◦

•◦
•◦

•◦

•◦

•◦

•◦
•◦

•◦•◦

•◦

•◦

•◦
•◦

•◦

•◦

•◦
•◦
•◦

•◦

•◦•◦•◦
•◦

•◦

•◦
•◦

•◦

•◦

•◦

•◦

•◦

•◦

•◦
•◦
•◦
•◦
•◦

•◦

•◦

•◦

•◦

•◦

•◦•◦

•◦

•◦

•◦

•◦

•◦

•◦
•◦

•◦

•◦

•◦

•◦

•◦

•◦

•◦

•◦

•◦
•◦
•◦
•◦

•◦•◦

•◦

•◦
•◦

•◦

•◦

•◦

•◦

•◦
•◦

•◦
•◦

•◦
•◦

•◦

•◦
•◦

•◦
•◦
•◦

•◦

•◦

•◦
•◦
•◦
•◦
•◦•◦

•◦

•◦

•◦
•◦
•◦

•◦•◦

•◦

•◦

•◦•◦•◦

•◦

•◦

•◦

•◦

•◦

•◦
•◦

•◦

•◦

•◦

•◦

•◦

•◦

•◦•◦

•◦

•◦
•◦

•◦
•◦

•◦
•◦

•◦

•◦

•◦

•◦
•◦•◦

•◦
•◦

•◦•◦

•◦

•••
•
••
•
•
••
•••••
•••••
••••••••
••••••••••••••••••••••••
•
•••
••
•••••••••••
•
•
•••••••••••••••••••••••••••
•
•
•
•
•••
•••••••••••
•••••••••
••••••
•
•••
•
•••
•••
••••
••••••••••
•
•••••••••••••••
••
••••
••
•••••••
•
••••
••••••••••••••••••
•
•••••••••••••••••••
••••••••••••
•
••••••••
•••••••••••
•
••••••••
••••••••••••
•••••••
•
••••
•
••
•••
•
••
•••••••••
•
•••
•
•
••
•••••••••••••••••••
•••
•••
••••
••
•••••••••••••••••••••••••
•••
••
•
•
•
••••
•••
••••
•••
•••
•
•••
••
••
•
•••••
••••••
••••••••••••
•
••
•
••••
•••
•••
•

•
•••
•••
••
•••
••
•
•••
•
••
•••
••
••
••

•

•
•
•
•
•

•

•••
••••
•
•

••

•

•

•

••
•

•

•

•
•

•

•

π(p)Q4(p)Q3(p)
0 100 200 300 400 500 600 700 800 900 1000
0.0

0.3

0.6

0.9

1.2
 ·········
·······
···
·
······
················
·····························
··
·
························
·······························
······
·······························
·
····················
·
···
·
····································
··························
··
·
·
··
··················
··
··················
··
········
·········
·
········
····
···
··········
·········
·
··
········
····
·········
·
···············
··
·
············
·
·
·
······
····
·
··
·
·····
·
···
·
····
·······
·····
····
···
·
·····
··
·
········
·········
·
···························
······
···
·
············
·
···
·
···
···
·
·····
·······
·
·····
···
·
·····
·
··
······
·
···
·
······
···
·····
·
······
·
·
··
·
·
····
·
··
·
·
·
·
············
·
···
··
·
···
·
······
·

·
··
·
·········

·
····
·
·········
·

·
·······
·
···········
·
·
······
··
·····
·
······
·
·····
··

·
·
·
··
··
···
·
··
·

···
·····

··
·
·
·
··
·
·

·
·········
··
·
··

·
····
·
··
··
··
·
··
·····
··
·

·
·
···
··
·
·
····
·
···
·
···
··
····
·

··
·
·
··
··
·
·
··
·
······
···
·

·
···
·
·
·
·
·
··
·
··
·
···
·
·
·
··
·
·
·
·
·
··
·

·
··
·

·····
·
·
·····
··
·
·
·
·

·
····
·
····
··
··
·

··
··
···
·
·
··
···

·
··
·
·
··
·
·

·
·

·
·
·
·
·
·
·
··

·
·
·
·
···
·
··
··
·
···
·
·
·

·

·
·

·

····
·

···

·

·
·
·

·
··

·
·
·
·

·

·

Figure 5. Plot of Q3(p)and of Q4(p)Q3(p), for 2 ≤ π(p) ≤ 1000,
i.e., for 3 ≤ p ≤ 7919. On the plot of Q3(p) the points with
p mod 3 = 1 are represented by circles (◦) and the rest by disks (•).

data points as soon as L(p, x) < 100), and then by using another best least-squares
ﬁt to approximate 1/m1(x)by m2 log x + b2 (this last ﬁt was extremely good). To
study the deviations of the decay of L(p, x) from a true exponential decay, the
upper part of Figure 5 presents a plot of some values of

Q3(p)=10
−17e
0.0355π(p)L(p, 4 · 10
18).

The factor e
0.0355π(p) removes most of the exponential decay of L(p, 4 · 10
18). The
scale factor 10
−17 ≈ 1/π(4 · 10
18) places Q3(p) close to 1. Similar behavior was
observed for other values of x (with diﬀerent exponents and scale factors). The ups
and downs of the p mod 3 =1points(◦)and of the p mod 3=2 points (•)are
closely connected to what is happening to the diﬀerence Δ(p)= π(p;3, 2)−π(p;3, 1),
where π(x; m, a) denotes the number of primes up to x congruent to a modulo m.
The extra factor
 Q4(p)=
 {1 − 0.04Δ(p), if p mod 3 = 1,
1+0.04Δ(p), if p mod 3 ̸=1,

approximately removes most of the ﬂuctuations of Q3(p), as can be observed in the
lower part of Figure 5 (the constant 0.04 was found by trial and error). Section 5

License or copyright restrictions may apply to redistribution; see https://www.ams.org/journal-terms-of-use

EMPIRICAL VERIFICATION OF THE EVEN GOLDBACH CONJECTURE 2049

pQ5(p)
1000 2000 3000 4000 5000 6000 7000 8000 9000 10000
0.8

1.0

1.2

1.4

1.6
 ·
·

·

·
·

·

·
·

·

·
··

·
·
·

·

·

···
··
·
···
··

·
·
··

·
·

···
·
·

··
·
··
·

·

·

··

··

·
·
··

·
·

·

····
·
·

·

·
·

·

·
··
·
···
·
·
··
··
·
·
·

·

···

·
·

···
··
···
·
·
··
·
·
·

·
·
··
·
··
··
···
··

·
··
··
···
···
···

·
·
·
·
·

·

···

·
····
·

·
·

·

·
·
·
·

·

·
·

··
·

·
··

·

··
····

·
·
··

·

··
·
··
·
·
·

···
··
·
····

·

·
·

·

·
·
·
·
··
·
·

·

·
·

·
·

·
···
·

·

·
·
·
·

··

·

·

·

·

·
··
·
··

·

·

·
·

·

·

·

·
·
·
····

····

·
·
·

·

·

·
·

·

··
·
·
·
·
·
·
·
···
··

·

·
··

·

·
·
··
·
···
··

·

··
··
··
····
··
·
·····
·
··
·
·
···
·····
··
····
·
·
·
·
··
·
·
·
·
···

·

···
··
·
·
·
·
·
·
·
··
···
·
····

·
··
·
·····
····
·

·
···
·

·
·
·
·
··
·
·
·
·
·
·

··
·
·
·
···
·
···
·

·
·
··
·
······

·
·
··
··

·

···
·····
··
·····
··
·
··

·
···
·
·

··
·
·

·
·
·
·
·
··
···
···
·
·····
·

·
··

·
····
·
··
·
·
··
····
·······
···
·
·
··
·
·
·
·····
·
·

·

·

·
··
·····
·
··
·
·
·····
··
··
··
······

·

···
·
·
·
·
·
·
·
·
·
·····
·

·
·
·
·
·
·
·
······
·
······
·
·
···
·
·
·
···
·

·
·
···
····
·
··
·
···
··
·
·
···
·
·
·
·
······
··
·
·
······
·
·
·
·
·
·
·
··
··
··
··
·
···
·
···
·
·

·

·
·
····
··
·
····
·

······
·
··
·
·
···
·
·
·
····
·
····
··
··

·
·
··
···
··
·

·
·
···

·
·

·

····
·
··
····
··
··
····
·
······
···
·

·
·
··
···
·
·
··
·······
·
·······
·
··· ·

•◦•◦
•◦•◦

•◦
 •◦•◦•◦
•◦•◦
•◦•◦•◦

•◦
 •◦•◦•◦•◦
•◦
•◦
•◦
•◦•◦ •◦
•◦•◦ •◦ •◦•◦
•◦•◦
•◦•◦•◦•◦•◦
•◦•◦•◦•◦•◦
•◦ •◦•◦•◦•◦•◦ •◦•◦•◦•◦•◦•◦•◦•◦•◦•◦•◦•◦ •◦•◦ •◦•◦
•◦ •◦•◦
•◦ •◦ •◦ •◦ •◦ •◦•◦ •◦•◦ •◦•◦•◦•◦
•◦ •◦•◦•◦•◦ •◦•◦•◦•◦

•
•

•
 •
•
 • •

•

•
• •
•
 • •

• •

••• • •••• • • • •• •
 •
 • • • •
• •
• • • • •

Figure 6. Plot of Q5(p)for S(p) ≤ 4 · 10
18 and for p> 1000.
Disks (•), circles (◦), and dots (·) correspond respectively to data
obtained from Table 4, from Table 5, and to values of S(p)that
did not make it to either of the two tables.

of [19] provides an heuristic explanation for this last empirical observation. We
were unable to explain the residual pattern observed in the lower part of Figure 5.
It is reasonable to expect that the ﬁrst occurrence of a minimal Goldbach par-
tition with p(n)= p has an order of magnitude similar to that of the solution of
ˆL(p, x) = 1 (this is indeed the case for p< 250). From our observed approximate
exponential decay of L(p, x) it then follows that it is likely that S(p) has an order
of magnitude similar to that of the solution ofπ(x)exp (
− π(p) − 2

0.755 log x − 4.19
 ) =1.

The left-hand side of this equation gives a rough estimate of the value of L(p, x),
obtained by ignoring the (relatively small) deviations of the decay of L(p, x)from
a true exponential decay. Disregarding the −2 in (2.5) and using the asymptotic
estimate π(x) ∼ x
log x , (2.5) becomes Q5(p) ≈ 1, where

Q5(p)= π(p)
0.755 log2 S(p) − 0.755 log S(p) log log S(p) − 4.19 log S(p) .

Our empirical data (cf. Figure 6) supports the validity of this approximation. Note
that this ﬁgure does not exhibit the slightly increasing trend observed in Figure 3 (if
the term −4.19 log S(p) is ignored then that trend becomes clearly visible). Using
the rough approximation pk ≈ k log k to solve Q5(p) ≈ 1in order toget p yields

p ∼ 1.51 log2 S(p) log log S(p).

Remarkably, this result is consistent with the Granville conjecture with C = C −1
2 .
However, this may be what happens for a typical ﬁrst occurrence. Extreme values• points) may behave diﬀerently, perhaps in a way consistent with the Granville
conjecture with C =2e
−γC −1
2 . As stated before, much more data is needed to settle
this issue by empirical means.

License or copyright restrictions may apply to redistribution; see https://www.ams.org/journal-terms-of-use

2050 T. OLIVEIRA e SILVA, S. HERZOG, AND S. PARDI

Table 8. Record-breaking values of gk for pk ≤ 4 · 10
18.

pk gk pk gk pk gk
2 1 1221 64747 222 134 62943 10749 582
3 2 1896 95659 234 140 86954 93609 588
7 4 1919 12783 248 196 81885 56461 602
23 6 3870 96133 250 261 49417 10599 652
89 8 4362 73009 282 717 71626 11713 674
113 14 12942 68491 288 1382 90485 59701 716
523 18 14531 68141 292 1958 13341 92423 766
887 20 23009 42549 320 4284 22839 25351 778
1129 22 38426 10773 336 9087 43294 11493 804
1327 34 43024 07359 354 17123 13424 20521 806
9551 36 1 07269 04659 382 21820 94054 36543 906
15683 44 2 06780 48297 384 1 18945 99698 25483 916
19609 52 2 23670 84959 394 1 68699 49409 55803 924
31397 72 2 50560 82087 456 1 69318 23187 46371 1132
1 55921 86 4 26526 18343 464 43 84154 78455 41059 1184
3 60653 96 12 79763 34671 468 55 35077 64319 03243 1198
3 70261 112 18 22268 96239 474 80 87362 46272 34849 1220
4 92113 114 24 11606 24143 486 203 98647 85174 55989 1224
13 49533 118 29 75010 75799 490 218 03472 11942 14273 1248
13 57201 132 30 33714 55241 500 305 40582 65210 87869 1272
20 10733 148 30 45995 08537 514 352 52122 34513 64323 1328
46 52353 154 41 66086 95821 516 401 42992 59991 53707 1356
170 51707 180 46 16905 10011 532 418 03264 59367 12127 1370
208 31323 210 61 44874 53523 534 804 21283 06866 77669 1442
473 26693 220 73 88329 27927 540 1425 17282 44376 99411 1476

2.2. Prime gaps (and counts of twin primes). Let gk = pk+1 − pk be the gap
between the consecutive primes pk and pk+1, and, for g restricted to be either 1
or a positive even integer, let P (g) be the smallest prime pk such that gk = g,if
one exists, of inﬁnity otherwise. The Polignac conjecture [36] asserts that P (g)
is always ﬁnite. Also, let N (g, x) be the number of solutions, with pk+1 ≤ x,of
the equation gk = g. (The choice of counting limit, either pk ≤ x or pk+1 ≤ x,
is a matter of implementation; we chose the latter because it does not require the
computation of the smallest prime larger than x.)
Table 8 presents the record-breaking values of gk, i.e., values of gk larger than
those for all smaller values of k (called maximal prime gaps), and Table 9 presents
the record-breaking values of P (g), that were found up to 4 · 10
18.To save some
space, we do not present other ﬁrst occurrences of prime gaps. For pk < 5 · 10
16,
the previous published record of computation of prime gaps, they can be found
in [31, 32, 50], were references to even earlier computations can be found (the rest
can be found either on the ﬁrst author’s web pages or on Thomas Nicely’s web
pages). The entries for gk = 1172, gk = 1186, gk = 1356 and gk = 1370 were ﬁrst
discovered by Donald Knuth, and the entry for gk = 1048 was ﬁrst discovered by
Bertil Nyman, in unrelated computations.

License or copyright restrictions may apply to redistribution; see https://www.ams.org/journal-terms-of-use

EMPIRICAL VERIFICATION OF THE EVEN GOLDBACH CONJECTURE 2051

Table 9. Record-breaking values of P (g)for P (g) ≤ 4 · 10
18.

gP (g) gP (g) gP (g)
1 2 256 18728 51947 708 14367 94957 84681
2 3 264 23578 81993 722 21835 68728 45927
4 7 278 42609 28601 752 25529 45938 22687
6 23 294 56926 30189 764 32381 14816 25339
8 89 298 86505 24583 768 42368 30305 75549
10 139 314 89484 18749 774 46978 91428 49483
12 199 316 1 21091 72293 780 47191 16993 84963
16 1831 328 1 30868 61181 782 72650 72235 59111
26 2477 334 3 08271 38509 796 1 27130 98386 31957
28 2971 362 3 58777 24601 812 1 71027 09585 51941
30 4297 368 5 14305 18413 848 2 53707 06528 96083
32 5591 370 5 99423 58571 866 2 75931 76844 46707
36 9551 388 15 67987 92223 882 3 37105 54523 81147
38 30593 422 28 09748 65361 886 4 12707 41657 53081
46 81463 436 36 74590 59871 898 4 19816 81494 92463
56 82073 442 41 74705 54687 922 4 28612 92018 82221
64 89689 452 46 68551 87471 926 6 38194 41364 89827
66 1 62143 466 56 58556 95631 928 10 24431 62284 69423
70 1 73359 470 68 17532 56133 932 10 67648 05159 67939
74 4 04597 472 86 52447 09607 968 19 12499 02449 92669
80 5 42603 482 105 16027 87181 980 19 40368 49017 55939
88 5 44279 488 127 53631 52099 986 34 84747 41189 74633
92 9 27869 506 133 93477 50707 1006 37 34319 22965 58573
94 11 00977 508 184 10864 84491 1018 37 96724 08364 35909
102 14 44309 510 220 90169 10131 1040 46 24684 83928 75127
108 22 38823 518 229 64970 58133 1048 88 08967 23316 29091
116 58 45193 520 233 61672 62449 1052 89 21924 28734 19107
124 67 52623 536 537 12842 17763 1066 98 43614 75403 71287
134 69 58667 568 601 03305 72331 1094 139 03365 64467 25643
140 76 21259 576 881 77920 98461 1114 198 88751 28069 88729
142 103 43761 580 938 30813 40541 1124 203 15341 65230 88323
144 119 81443 590 2076 12522 61751 1144 236 55290 66620 07587
150 136 26257 608 2076 73305 30329 1150 293 46416 14651 35373
156 179 83717 624 2492 30339 18059 1172 400 24093 47413 22419
158 492 69581 626 3360 54804 00197 1186 404 44469 23233 76357
166 837 51121 628 3414 00476 13391 1192 703 39072 49524 90921
186 1476 84137 632 4567 86858 80759 1202 819 61534 49961 14321
194 1667 26367 646 5102 71604 68351 1208 1331 71124 79690 25019
200 3780 43979 654 5491 60860 07427 1264 1798 55672 01943 08703
224 4098 66323 656 6586 29660 31241 1290 2980 70756 30312 38363
226 5196 53371 676 7861 08331 15261 1306 3278 01806 91024 80227
228 8958 58039 680 8238 54353 31119 1346 > 4 · 1018

254 12024 42089 688 11052 66702 35599

License or copyright restrictions may apply to redistribution; see https://www.ams.org/journal-terms-of-use

2052 T. OLIVEIRA e SILVA, S. HERZOG, AND S. PARDI

gQ6(g)
0 250 500 750 1000 1250 1500
0.20

0.40

0.60

0.80

1.00
 ··
······
·
·····
··
·
·····
·
···
···
··
········
····
·
·
··
········
·
·
··
···········
·
····
···
·····
···
···
·
···
············
····
·
····
·
·
···
·
···
····
····
·
·
·

·
··
·
··
······
·
··
·
················
··
····
···
······
····
·
·
········
·
·
·
·
··
·
·······
·
·
··
··
··
·
·
··
····
·
·
·
····
·
·
·
····
··
·····
··
·
·
·
·
···········
···
·
··············
···
·
··
·

·
·················
··
··
·····
········
·
······
···
······
·····
·······
···
·
···
·
···
··
····
·········
···
·
·····
·
··
····
···········
··
·
···
·····
·
·········
·
··············
·········
·······
·
·······
·····
··
··········
·
··
··
·
··
·
···
······ ·

•◦•◦

•◦

•◦•◦•◦•◦

•◦•◦

•◦
•◦
•◦
•◦
•◦•◦
•◦•◦•◦
•◦•◦
•◦
•◦
•◦•◦•◦•◦•◦•◦
•◦•◦•◦•◦
•◦ •◦•◦
•◦ •◦
•◦•◦•◦•◦•◦
•◦•◦•◦
•◦ •◦•◦•◦•◦ •◦•◦•◦•◦•◦•◦•◦•◦•◦
•◦•◦•◦•◦•◦•◦ •◦•◦•◦
•◦
•◦•◦•◦•◦•◦•◦•◦•◦•◦•◦•◦•◦•◦ •◦•◦•◦•◦•◦•◦•◦•◦ •◦•◦•◦•◦•◦ •◦•◦•◦•◦ •◦•◦•◦•◦•◦•◦•◦•◦•◦ •◦•◦•◦•◦•◦•◦•◦•◦•◦•◦ •◦ •◦•◦

•

•

•

•
••

•

•
•

•
•

••

••

•

•
•
• •
 •
•

••
•
•
 •

•• ••
• •
••
 •
•

•••••
••••• ••• •• • •
• •
•
 •

••
 •
 •••
• • • • •• • •

Figure 7. Plot of Q6(g)for P (g) ≤ 4 · 10
18 and for g> 4.
Disks (•), circles (◦), and dots (·) correspond respectively to data
obtained from Table 8, from Table 9, and to values of P (g)that
did not make it to either of the two tables.

2.2.1. Conjectures concerning prime gap upper bounds. Cram´er [7] conjectured that
the equation g> c log2 P (g) has only a ﬁnite number of solutions for c> 1, and
an inﬁnite number of solutions for c< 1, i.e., he conjectured that the largest
gap between consecutive primes smaller than x should be approximately log2 x.
Granville [18] conjectured that it should be 2e
−γ log2 x. Shanks, on the other hand,
conjectured in [43] that g ∼ log2 P (g) should hold for all ﬁrst occurrences, and not
only for a subsequence of them. To test these conjectures, Figure 7 presents a plot
of almost all the values of Q6(g)= g
log2 P (g)
that we were able to compute (the points corresponding to Q6(1) ≈ 2.08137, to
Q6(2) ≈ 1.65707 and to Q6(4) ≈ 1.05637 were omitted to reduce signiﬁcantly the
vertical range of the plot). Figure 7 shows that Q6(g) stays below 1 for g> 4
and for P (g) < 4 · 10
18 (thus, also below 2e
−γ ≈ 1.12292), and that Q6(g) is slowly
increasing. As explained later in subsubsection 2.2.3 the increase of Q6(g) will likely
not persist for ever. Given the absence of a clear limiting value (or accumulation
point) in Figure 7, our direct evidence, based solely on the ﬁrst occurrence of
prime gaps, is clearly insuﬃcient to settle any of the three conjectures. As in
subsubsection 2.1.1, much more data is needed before some tentative conclusions
can be drawn.Estimate of N (g, x) using the prime k-tuple conjecture. From the inclusion-
exclusion principle it follows that (for g positive and even)

N (g, x)= ∑

s (−1)|s|π(x; s),

where the sum is over all subsets s of { 0, −2, −4,... , −g } which contain 0 and −g.
Using the prime k-tuple conjecture to approximate π(x; s) yields

(2.6) ˆN (g, x)=
 1+g/2∑

k=2 (−1)kAg,k
 ∫ x

c
 dt

logk t ,

License or copyright restrictions may apply to redistribution; see https://www.ams.org/journal-terms-of-use

EMPIRICAL VERIFICATION OF THE EVEN GOLDBACH CONJECTURE 2053

Table 10. Non-zero values of A210,k (only 21 signiﬁcant digits shown).

kA210,k kA210,k
24.22503 56214 19965 27314 24 1.30654 90389 76895 22546 · 1026

38.55271 41397 87032 74328 · 102 25 3.98015 77849 08386 50567 · 1026

48.36792 68833 33357 58482 · 104 26 1.07941 25739 42675 11873 · 1027

55.27139 32786 77592 64771 · 106 27 2.60080 37854 40621 31982 · 1027

62.40311 09723 02572 10228 · 108 28 5.55372 35291 47820 70330 · 1027

78.44821 97025 17459 94316 · 109 29 1.04795 36474 29832 87798 · 1028

82.38329 96966 57191 74741 · 1011 30 1.74142 93763 38787 42144 · 1028

95.54337 34738 69664 85470 · 1012 31 2.53865 33161 01092 25766 · 1028

10 1.08393 95312 84895 97964 · 1014 32 3.23275 89373 30916 84257 · 1028

11 1.80792 42248 15396 08373 · 1015 33 3.57913 90799 32642 56033 · 1028

12 2.60095 23110 19640 17470 · 1016 34 3.42783 40356 80761 84324 · 1028

13 3.25558 92220 22344 78432 · 1017 35 2.82441 80085 26862 50480 · 1028

14 3.56978 17581 63630 82201 · 1018 36 1.99018 32570 50074 25081 · 1028

15 3.44762 24282 49207 49866 · 1019 37 1.19070 12781 96056 59918 · 1028

16 2.94524 14940 75784 28189 · 1020 38 5.99032 61021 74504 60492 · 1027

17 2.23304 45335 51780 41017 · 1021 39 2.49657 02568 80552 25160 · 1027

18 1.50646 92038 79818 67663 · 1022 40 8.40819 41558 71382 32490 · 1026

19 9.05996 67381 18660 00136 · 1022 41 2.19451 40146 49314 36474 · 1026

20 4.86355 36308 62522 36983 · 1023 42 4.13354 37049 56213 13673 · 1025

21 2.33219 01487 92830 32932 · 1024 43 4.93576 18160 53210 32685 · 1024

22 9.99223 09979 82591 31946 · 1024 44 2.76114 18521 61063 83771 · 1023

23 3.82427 45568 44084 48541 · 1025

where Ag,k = ∑

|s|=k G(s)and where G(s) is given by (2.3). The Ag,k constants
can be computed using the method described in [6] (our Ag,k constants are equal to
Brent’s (−1)kAr,k−1 constants, where g =2r). The second author computed them
all for g ≤ 212 using about 40 one-core CPU years (the ﬁrst author double-checked
the results for g ≤ 190). As an example of the general behavior of these constants,
Table 10 presents the non-zero values of A210,k.
Just like in subsubsection 2.1.2, it turns out that the lower limit of integration
of 2 is also a very bad choice for (2.6); both c =0 and c = g give very good
approximations to N (g, x) (remarkably, ∣ ˆN (g, g)∣ < 6for g ≤ 212). In all of our
comparisons between N (g, x)and ˆN (g, x) a lower limit of integration of c =0 was
used. Truncated versions of (2.6) behaved just like the truncated versions of (2.4)
did: good approximations require all or, for small x, almost all terms.
As before, it seems reasonable to apply the law of the iterated logarithm to
attempt to bound ∣ ˆN (g, x) − N (g, x)∣ by √
2N (g, x) log log N (g, x). To test the
accuracy of this error bound estimate, Figure 8 plots some values of

Q7(g, x)= ˆN (g, x) − N (g, x)
√
2N (g, x) log log N (g, x) .

Like Q2(p, x), it appears that ∣Q7(g, x)∣ may indeed be bounded. In this case
the factor of two inside the square root appears to be about right. Given that
ˆN (g, x) ∼ Ag,2 x

log2 x , we should have N (g, x)= O( x
log2 x ), and so our empirical

License or copyright restrictions may apply to redistribution; see https://www.ams.org/journal-terms-of-use

2054 T. OLIVEIRA e SILVA, S. HERZOG, AND S. PARDI

xQ7(g,x)
10
10 10
11 10
12 10
13 10
14 10
15 10
16 10
17 10
18 10
19
−2.0

−1.0

0.0

1.0

2.0
 ·
··
·
·

·
··

·
·
·
··

··

·
··
··
·

·
·
·

·

·

·
·
·
·

·

·
·

·

·

·

·

·

·

·

·
··
·

··

·

·
·

·
·
·

·

··
·····
·
··

·
·
·
·

··
··

·
·

·
··

·
·

·
·
··
·

·

·
·

·
·

·

·

·

·

··

·

·

·

·

·
·
·
·
·

·

·

·
·
·
·

·
·
·
··
·
···
·

·····
·

·
·

·

·
·
·
·
·

··
·
·
·
··

·
·

·

·

·
·
·
·

·

·

·
·

·

·
·

·
··
·
··

·

··

·

·

··
·

·
·

·
·

·

·
·
···
·

···
·
·
·

·
·
·
·
·
·
·

·

·
·
·
·

·
·
·

·

·

·

·
·
·

·

·

·

·
··

·
··
·

·
···

·

·
·
·

·
·
·
·
·

·

··

·

·
·
···
·

··

··
·

·

·
·
·
·

···
·
··

·
·

·

·

·

·

··

·

·

·

····

···

·

··
··

·

·

·

·
··

·

·

·
·

·

·
··
·
··
·

·
·

··

·

·
···

·
·
·
·
·
··
·
·

·

·

·

·

·
·
·

·

·

·
·
·
··

··
·
·
·

··
·

··

··
·

·

·

··

·

·
··
·
·
·

·

····

···

··

·
···

·
·

·
···

·

·
·

·

·

·
··
·

·

·

·

·
··
·
·
··

··
··

··

··

··

·

·

·
·

·

·

··
·
·
·

·

·
···

·
·

·
·

·
··

·

·

·
····
··

·
·

·

·

··

·

·

·

·

··
·
·
·
·
·

···
·

·

·

·

··

·
·

·

·
··
·

·
·

·

···

·
·

·
·
·

··

·

·
·
··
·
·
·

·
·

·

·

·
·

·

·
·

·

··

·
··

·

··
·

·

··

·

·

·

·
·
·
·
·
·
·
·

·

·
···

·
·

·
·
·

·

·

·

·
·
·
··

·
·

·

·
·

·
·
··

·

·
·

·

··
··

·
·

·
·
·

··

··

·

·
·
···
·
·
··
·

··
·
·
···
··

·
·

·

·

·

··
·

·
·

·
·
··

·
·
·
·

·

·

·

·

··

··
·
·

·
·
··

·
·

·
··

·

·

·
·
·
·
·
·

···
·
···
·
·
·
·

·

·

·

·
··

·
·
·

·
··
··
·
·

·

·
··
·

·

··
·

·
·

·
··
·

·

····

·

·

·
·
·
·
·
·
·

···
·
··
··
··

·

·

·

·
··

·
·
·
··
·
··
·

·

·

·

·

·
··
·
·
·
·
·
·
·

·

··
··
·
·

·

·
··
·
·
·
·
·
·
·
···
·

··
·
·
····

·

·

·

·
·

··
·

··
·
·
·
·

·

···

·

·

·
·
·
·

··

··

·

·
··

··
·

·

·

·

·
·

·
·
·
·
·
·
·
··

·
··
··

··
·

·

·

·
·
·
·

··
·
··
·
·
··
·

·

·
·
··

·
··
·
·

·

·

·
·

·
···
···

·

·

·

·

·
·

·
···
··
··
··
·
··

·
··

·
·
·

·

·

··
·
·

··
·

·
·

·
··

··
··
·

·
·

··

·

··

·
·

·

····
·
·
·

·

·

·

·

·

·

··
·
··
··
·
··
·

·
·

·

·
·

·

·
··

··

·
··
·

·
··

·
··
·

·

·
··

·

·
·
·

·

·
···
·
·

·
·

·

··

·

·
·
·
··
····
·

·
·

·
·

·
·

·

·
·
··

·

·
·
·
·

·

·

·

···

·
·

···

·
··

·

·

······
·
·

·
·

·
·
·

·

·
·

····
·
·
··
·

·
·
·

·

·

·
·
·
·

·
·
··
·

·
·

·

·
··
·

··
·
·

·

·

·
·
·
·

···
·
·

·

·
··

·
···
·
·

··
···
··
··
·

·

·

·
·
·

··

·

·

·
·

·
·
··
·
·

·

·

··
·

·
·
···

·
·

·

·

·
·
·

···
·

·
·

·
·

·
···
·
·
·

·
·
·
···
·

·

·
·
·

·

·
·

·

·
·
·

··

···
··

···

·

···
·
·

·

···

·
·

·

·

·
·

·

·
·
·

··

···

·
···
·

··
··

···
·
·

·

·
··

·

·

·

·

·
··
·
·
·
··
·

·
·
··

·

·
·
···

··

·
·

·

·

··
·

·

··

·
·

·
·

·

··
····

·
·
·
·
·
·

·

·
··

·

·

·

·

····

·

··

·
·
·
·

·

·
·
·

·

·
·
·

·

··

·

·

·
·

·

·
·
·

·
·
·
··
·

·
·
··
·

·

·

·
··

·

·

·

·

···

·

··

·
·

·

··

·

··
·
·

··

··

·

·
·
··

·

···
·
·

·

·
··

·
··
··

··
·

·

··

·
·

·
·

·
·
·

·

··
·
·
·

·

·

·
·
··
·

···
··

·
·
··

·
··
·
·

·

·
·

·

·

··

·

·

·
·

·
·

··

·

·
·
·

·
·

·

··

·

··

·

·
·
·
·

·
·

·

·
·

··
·

··
·

·

·
·
·
·
·

·
·
·

·

·
·

··

·

·

·

···
·
··

·

·
·
·
·

···
·

·

··

·

·

·
·
·
·

·

·
·
·

··
·

··

·

··

·
·
·

··

·

·

·
·

·

·

·

·

··

···
·
··

··
·

·
··

····
·
··

·

·

·

··
··
·

·

··
·
·

·
·
·

··
·

··
·
·
·

·
··

·

·

·

·

··

·

·
·

···
·
··

·
·
·
·

··
··
·
·
··

·
·

·

·

··
··
·

·

··
··

··
·
·
····

··
···

·
··

·
·

·

·

·

·

·

··

··
·
··
·

·
·
·

·

··
·
·
·
··

·

·

·

·

·
·
·
·
·

·

·
·
·
·

·
··
·

···
·

·
·
·
·

···

·

·
·

·

·

·

·

··

·
·
·
·
··

·
·
·
·

··

·
·
·

·

·

·
·

·

·
·

·
·
·

·

··
·
·
·

·
··

·
·
··

···
·
·

·
·
·

···
·
·

·

·

··

··
··
··

·
·
·
·

··
··
·
·
·

·

·
·

·

·
·
·
·
·

·

··
·
·

·

·
·

·
·

·
·

··
·

·

·
·
·

··
·

·

·

·

·

··
·
··
·
·
·
·

·

·
·
···
·

·
·
·
··
··

··

·

·
·
·
·

·
·
··
·
··
··

·

··
·

·
·
··

·
·
··

·

··

·

·

··
·
··

·
·
·

·

·
··
·
··
··

··

··
··
··
·

·

··

··
·
·
··
··

·

·
·

··

·
·

··

·

··

·

·

····

·
··
·

·
·
·

··
··
··
·
·

··
·
·
·
·
··
·

·

··

··
·
·

··

·

·
··
·

·

·
·

·

··

·

·

····

·
·
·
·
·
···

··

···
·
·
·

·
·
·
··
·
·
·

·

··

·

·
·

·
·

·

·
·
·

·

·
·

·
·
·

·
·

·

·

···

··
·
·

·
··
··
·
·

····
·
·
·
·

·
···
··

·

··
·
·
·

····

·

·
·

·

·

·

·

·
·
·
·
·

·
·

·

·

···

··
·
·
·
··
··
···
·
·
··
·
·

·

·

··
·
·

·
·
·
·
·
·

··
··
·

·

·

·

·

·

·
·
·

····

·

··

·

·

·
·
·

·
·

·
·
·
·

·
·
··
·

··

·
·
·
··

·
·

··
··

·
·
·
·
·
·

·

·
·
·

·

·

·

·

·

·
·

·

·

··
·

··

·
··

·
··

···
·
·
··
·
·
·

·

··
·
·
·
·

·
·

···
···

·
·
··
··

·

·

·

·

·

·

·

·

·
·

·

·

··
·

·
·

·
·
·
·
···

··
·

··
··

·
··

·

·

·
·
··
·
·
·

··

·
·

·

·

··

·
··

·····

·

··

·

·

·
·
··

·

··

·

·
·

··

·
··

·
·
·

·
·

·
·

·

·

·
··
·
·
···
·
·

·
·

·

··
·

·

··

··
·

·

·
·

·
·

··
··

·

··

·

·
·

··
·

·

·
··
·

·
·

·

·
·

·

·
·
·
······
·
·
·
·

·

·
·
··
·
·

··

·
·
·
·

·

··

·

·

·

·

·

·

·
·

··

··

·

····

·
·

·

··
·

·

·

·

·
··
·
·
·

·
·
·

·

··
··
·

·

·
·

·
·
·
·

·

·

·

··

·
·
··

·

·

··
·

··
··

·
·
··
·
·

·

·
·

·
·

·
·
·
··
·
·
·
··
·
·
·
·
·

··
·

···
··

·

·

·

··

·
·

·

·
··

·
·
··

··
·
···

·
·
·

·
·

·
·
·
·

·

·

·
·

··
·
·
···
·

·

·

·
·

··
·
····
··

·

·

·
·

·

·

·

·
···
·
··
·

·
·
·
·

·
··

···

·
··
·

··

·
·

·
··
··
·

·

·

·

··

·
·
··
··

·

·

·
·

·

·

·

··
·
·
····

·

···
·
·
·

·
··

·

··

··
·
·
·

·
·

··

··
··
···

·

·

·

·

···

·
·
·
·
·

·

·
·

·

·

·

··
··
···

·
·

·
·
·
·

·
·
··

·
··

·
··
·

·
·

·
·
·
····
·

·

·

·

·

·

·
·

···
·
·
·
·

·

·

·

·

·

·

··
·
··
·

·
·

··
··
·

··
··

·

·

·

··
·
··

·

·
·

··
···

·

·

·

·

·

·

·
·

·
·
·

·
·

·
·

·
·

·

·

·
··

····

·
·

··
·

·

···

·

·

·

·
·
·
·
·

·

·

·
·
·
·
·
·
·

·

··
·

··

·
·

··

·

··

·
··
·

·
·

····
·

·

·
··
··

··

·

·

·
··

·

·

·

·
·
·
·
·

·

·

·
·
·
··
·
·
·

·

··
·

·

·
·

··

·

·
·

··
·
··

·
·

···
·

·
·

·

·
·

··

·

·

·
·
·

·

··

·

·
·
·
·
·

·

·

·
··

·
·

·

·

··
·
·
·

·
·

··
·

·

·
·

··
·
·

·

·

·

··

·
·

··

··

··
·

·

·

·
·

·

·
·

·

··
·

·

·

·
·
·
·
·
·
·

·

·

·

·
·
·

·

··
·

·
·

··
··

·

·

·
·
·
·
·
·

··
·
·

·
··
·

·

···
·
·
·

·

·
·
·

·

·

·
·

·····
·

·

·

·

···

··

·
·

·

·

·
·
·

·
·

·
·
··
·
·

··
·
·

·

··

··
·

·
·

··
·

·
·

··

·
·
·

·

·

··

··
·
·

·
·

·

··

···

···

·

··

····
··
·

·
·
·
·
·

··
·
·
·

·
··

·
·
·

·

·
·
·

·
·
·

·
·
·

·

·

·
·

···
·

·

·
·

·

···

·
··
··

·

··

···
··
·

·

·
·

·
·

··
··

·

·
·
··
·

·
·
·
·
·
·
··

·

·
··

·

·

·
·
···
·
·
·

··
·
··

·
··
··

·

·
·

··
·
·
·

·
·

·
·
·

·
·

·
·
··

·

·
·
·
··
·

·
·

·

·

·
··

·
··
·

·

··
·

·
·
·
··

·

···

·
·
·
··

·

·
·

·
·
·

·
·

·

·
··

·
·

··

·

··
·
···

··

·
·
·
·

·
·
·
·
·

··
·

···

··

·

·
·

·

··
·
·
·

·

·
·
·

·
··

·
·

·

·
·

·
·

··
·

·

·

·
·
···

··

·
·
·
··

·

··

·

·

··
·
···
·
·
·
··

···

·
·

·
·
·

··

·

·
·

·
·

·
·

·

·

·
·

·
·

··

·

·

·

··
·
·

··

·
··
·
·

·

··

·
·

·

·

···
··
··
···

·
·

··
·
·

·

·

··

·
·

··

·

·

···

·
·
·
·

·

·

·

···
·

··

·
·
·
·

·

··

·
·

·

·

·
·
····
·

··
·

·
··
·

·

·

·
·

··

··

·

·

·
·
·

·
·

·
·

·

·

·
·
·

·

··

·
·
·
·

·

··

·
·

·
·

·
·
·
·
··

·
·

·
·
·
·

·
·

··

··
·
·

·

·

·
··

·

·
·
·

·

·

·

·
·
··
··
·
···
·

·

·
·

·
·

·
··

·
·
·

·
··

·
·

·
·

·

·
·

·
·

··
·
·
·
·

·

·

··

··
·
··
·
·

·
·

·

··
·
···
·
··
·

·

·

·
·

·

·

·
·
·

···

·
···

·

·

·
·
·

··

··

··

·
·
·

·

·

··
·

··
·

·

·

·

·
·

·

··
·
···
·
·
··

·

·
··

·

·

··
·

·
··

·
··
·

·
·

····

·

·
·

··
·

·

·
·
··
···
·
·
·

·

·
·

·

··
···
·

·
·
·
·

·
·

·

·

·
·
·

·
·
·

·

···

·

·

·

·
·

··

·

··

·
·

·

·
··
·

·
·

·
·

·

·
·

·

··
···
·
···
·

·

·
··

·

·

·
·
·

···

·
··
·

··
·
·
·

···

·
·

·

·
·
·
·
··

·

·
·
··

··
·
·

·
·

·

··
···
·
··
··

·

·
··

··

·
·

···

·

·
·

·
··
··

··
·

·

·

·

·
·
·

·
··

·

·
···
·

·

·

·

·

·
·

·

·
·
····
···
··

·

·

·
·

·
·
·

··
·

···

·
··
··

·

·

··

·

·

·
·

·

··

·

···
·
·

··
·

·

·
·

·

·
·
·
·
···
··

·

·
··

·
·

··
···

···

·
····
··

·
·
·

·
·

·

·

·

·

·

·
·

·

·
·
·
·

··

·

·
··

·

·
·
····
···
·

·

·
·

·
·

·
·
··

···

·

···

·
··
··

·
·

·

··

·

·
·

··

·

··
·
·

·

·

···

·

·
······
·
·
·

··

·
·
·
····

··

·

·
·

·
·
·
·
··

·

·

·

·

··

·

··

·

··
··

·

·

···
·
·
·····
·····
·

··
·

··
·
·
···

·

·

·
·

·
····
·
·
·

··

·
·

·

·
·

··

·
·
··
·

·
·

··
··
··
··
··
···
·

·
··

·
·
·

·
·

··

·

·

·

·

····

·
·
·

···
·

·

·

·
·

·

·
·
·
·
·
·
·
···
··
··
·
··

·
··
·
·

·
·
·

·
··

·
··

·

·

·
··

·

···
·
·
··

··

·

·

·
··
·

·
·

·

·
··
·
·

··
·
·
·
··
··
·
·
···
·

·

·
·

·

·
·
·
·

··

·
·
·
·

·
··
·

·
·

·
·
·

·

·
·
·
·

·

·
··
·
·
·
··
·
·
··
··
·
·
·
·····

·

·
·
·
·
·

·

·

··

···

·

·
·
·
·
·

···

·
·

·

·
·
·

·

·

·

··
·
·
···
·
··
··
·

·
·
·
··
·

·
·

··
·
·
··
·

·

·

·
·
··

·

··

·
·

·
·

·
·
·

·

·
·
··

·

·

·
·
·
·
··
·
····
··
·
···

·

···

·
···
·

·
··

·

·

·
·
·

·
··
·

·

··
·
·

·
·

·
·
·

·

··

·
·

··
·

·

····

·
·
··
·
··

·
··

·

·
··

·

·
··
·
·
·
·

·

·
·

·

·
·

·

··

··
·

·
·

·

·····
·
·

·

·

·
··

·

····

·

···
·
·
··

·
···

·

··
·

·

····
·
·
·

·

·
·
·
·
··
·
·

·

··
···

··
·

·

·
·
··

··

·

·

·
··

·

·

··

·

·
··
··

··

··
···

·

··
·

·

··
·
·
··

·

·
·
·
·
·
·
·
·
·

·

·
·
····

·
·

·

·
··

·
·
·

·
·

··
·

·

·
··
·

··
·
·
·
·

·
·

·
·
·

·

···

·

··
··

··

·

·
····

·
·
·
·

·

·
·
····

·
··

·
·
·
··

·
·

·
·

·

·
·

·

··
·
·
···
·
·
·
··

·
·

·
··
··

·
·
·

·

·
·
·
··

·

·
···
·
·

··
·

·

·
·

·

·

·
··

·
·

·

·
·
··

·

·

·

·
·

·
·

·
··
··
·
··

·
··

·

·

·
·
·
··

·

·
··

·

·
·
·
··
·

·

·
··
·
·

·
·

·

·
·

·
·

·
·
·

·
·
·

·
·
·

··

·

·
·

·

··

····
·
··

··

·

·

·
·
·
·
·

·
··

·

·

·
·
·

·
·

·

····
·
·

··

·

·

·

·
·
·

···

·
·

··
·

··

·
·

·

·
··

····
··
··

·

·

·
·
·
·
·

·
·

·

·
·

·
··

··
·
·

··

··

··

·

·

·

·
·
·

··
·

·
·
·

·
·

··
·
·

·
·
·
··

·

·
·····
·
·
·
·

·
·
··
·
·

·
·
···

·
··

··
·

·
·
·

··
·
·

··

·

·
·

··
·

·
·
·

·
···
·
·

·
·

·
·

·
·
·

·
··

·
···

·
···

·
·
··
·
·

·
·

·
·

··
·

·

·

·
·
·

··

·

·
·

··
·

·

·
·

·
·
··
·

·

··

·

·
··
·
·
·
···
··
··

··
··

··

·

·

·
·

·

·
·

···

···
·
·
·
·

·

·
·

·

·
·

·
·

··
·
·
·

·

·

·

·

·
·

·
·

·
···
·
·
··

····

·

·
···

·
·
·
·
·
·

·
·
·

··
····
·
·
·
·

·

·
·

·

·
·

··

·

·

·
·

·

··
·
·
··
·
·

·
··
·
··
·
··

·
·
··

·

··
··
····
·
··
·

··
·
·
···
··

·

·
·

·

·
·
··
·

·

·
·

·

·

··
·
·

·
··
··

·

·
·
·

··
··
·

·
····

·

·

···
·
·

·
·
·
·
·

·
······
·
·

·
·

·

·
·
·

·

·

·

··

·

·
·
·
·
··
·
·
·
·
·
·
·

·
···

····
·
·

··
·
·
·

·

··
·
·
··

···
··
·

··

··
·

·
·

·

·

·

·

·
·

·

·
·

·
·
··
·
·
·
·
··
·
·

···
·
·
·

·
·
·
·

·

·
·
··
··
·

·

·

·
··
···
··

·
·
·
·
·
·

··

·

·

·

·
··
·

·
··
·
·

··
·

··
··
··
··
·

·
·
·
··

··
·

·

··
··
·
·
·

·

·

·
·

·
·
·
··
·
··
··

··

·

···
·

·

·

·

·
·

·
··

·
··

·

··

·
·····
·

···
··

··
··
·

·
·
·

·
·
·

·
·
·
··

··

··

·
·
·
··

··
·

·
·

·
·

·

·

·
·

·
·
·

··

·

·
·
··

·

··
··

··
·
··

·
·
·
·
·
·

·
·
·
·
·
··
·
··
·
·
··

·
·
·

··

·
·

·
·

·
··

·
·
·

·
··

·
·
·
··
·

·

·
·
··

··
·
··

··

··

··
·

·
···

··

·
·
·
·
·
···
·

·
···

··
·

··

···

·

·
·

·
··

··
·
·
·
··

··

·
··
··

····
··

··

·
·
··
·

·
·

·
·

·
·

··
·
·
·

·
···

···
·

·
·

·

·

·

·
·
·
·
·
·

·
·
·
·
·

·

·

·

·
·
··
·

·
··
·
··

··

·
·

·

·
··
·
·
·

·
·

·
··
·
···

·
·
·

··
·
·

··
·
·

·

·
·
·
·
·

·

·
·
·

·
··
·
·

·
·
·
·
·

·
···
·
··

··
·

·
·
·
··

··

·
·

·
···
···

·
··
·

·
·
·
·

··
·

·

·

·
·

·
·
·

·

·

·
··

·
···

·
·

··
·

·
···
·
···

·
·
·
·

·
·
·
·

··

·

·

·
·
·
·
·

··
·

·
··
·

···
·

·

·
·
·
·
·

·

·

·
·
·

···
·

·
·
·
·
·

·
·
·
··

·

·
·

·
···
·

··

·
·

·
·

···

···

····

·

··

·
·

·
·
·

··

·

·

···

·
····

··
·
·

·
·
··
·
··

·

·
·
·
····
·

·
·

·

·
·
·
·
·

·
·

··
·

·

·

·
·

·
·
·

·
·

·
·

·
·

·····
·
·
··

·
·

·
·
·
·
·

·

·
·
·

·
·
·

·
·

·

·

·
·
···

·
·

·
···

·

··

·

·

·
·

·
·

·
·
·
·

·
··
·

·
····

·
·
·
···
··

·
·
·
·
·

···
·

··

·
·

·
·

··

··

·
·
·
·

·

·

·
·

···

·
·

·

···

···
·

·

·

··

··
·
··

·
·

··

····
·
···

·
·

·
·

···
·
·

····
·

·

·
··

·

·

·
·

···

·
·····

···
·

·
··

··
·

·
·
·

·
·
·
·

···
··
·
··

·

·

·

·
·
··
··

·
·
··

·

·

·

·

·
··

··

···

·
·
·

·

·
·

··
···
·
·
·

·
··

··

···
···
··

·

·

·

·
·
·
·
··

··
·
··

··

··

·
·

·

··

·
·

·
··
·

··

·

·

··

··
·
··
·

···

·
··

·

······
··
·

·

·

·
·

·

···

·
··
··
·
·

·

·

·

·

·
···
·

·
···

·

·

·
··

·
·
···
·

·

····

·

····
·
·
·

·

·

·
·

·

·
·
·

·
··
·

·
·

·
··

·

·

···

·
···

···

·

·
···

··
··
···

·

···
·
·

··
··
·
·
·
·

·

·

·

·
·
·

·
··
··

··
·
·

··

·

·
···

··
·
·

···

·

····

··
··
··

···

··
·
··

·
·
·
·
·

·
·

·

·

·

··
·
·

·
·
·
··

··

·
·

·
·

·

···

···
·

·
·

·

·
·
·

·
·
·
·
··
··

··
·
··

···
·
·
·

·
·

·

·

·
·
·
··
·
·
·

·

·
·
·
·

·
·

·

··
··
··
·
·

···
·
·

·
···

·
·
·
·
··

··
·

··
·

·
·
·
·

·

·
·

·

·

·
·
··
·
·
·

·
·

·
·
·
·

··

·

··
··

·
·
·
·

·
·

·
·
··
·

·
·
·
·

·

··

···

··
·

·
·
···
·

·
··
·

·
·

·
·
·
·

·
·

·
··
·

··

·

····

··

··

··
·
·

·
·
·

·
·

·
·
·

·
·

··
·
·
·

·

·

·
·

·
··
·

··

·
·

·
·

·
·

·

··
·

·
·

·

··
··
·
·
··

·
··

·

·

···
·
·
·

·
·

··

··
··
·

·

·
·
···

··
·
·

·
·
·

·
·
·
·
··
··
··

··

·

··
··
·
·
··

·
·
··

·

·

··
·
·
·
··

·

·
·

··

···
·

·

·
·
·
·

·
·
··
·

·
·
·
·
·
·
··

·
··
·

·

·

·
·
··
·
·
·
··
·

·

·

··

·
··
··
···

·
·

··
··

·

·
·
···

·

·
·····

·

·
··

·
·
·
··

···
·

·
·

·

·
·
·
·
·

···
··
·
·

·

··

·

·
·

··
·
··
·
·

·
···
·
·

···
··

·

···
·

·

··

·
·
·
·
·

··
·
·
·

·
·
·
···

·

··
·
·

·
··

···

·

·
·

·
·
·
·
·
·

·
··

·

·

·
·
··
·

··
·
·
·

·

··
·

·
·
··

·
·
·
·
·

·

·
··
·
·

···
·
·

·
·
·

·
·

·

·
·

··
·
·
·
·
·
·

·
·

·
··

·

·
·
·
·
·

·

·
·
·

··

·
·

··
·
··

·

··
··

·

·

··
··
·

··
·

·
·

·

·
·

··
···
·
·
·

·

·

·
·
·
·

·
·
··
·

·
·
··
·

·

··
·

··

·
·
·
·

····
···

·
·
··

·
··

··
·
·

·
·
··
·
··
·
·
·

·

·

··
·

·

·
·
·

·
·
·
·
··
·

·

·

·

··

·
·
·
·

·
·····
·

·
··
··

·
·
·

·

·
·

·
·
·

·

·
··

·

·

·

·
·
··
·
·
··
·
·

·
·

·
·
··

·

·
·

·

·

··
·
·
····
·
·

··
··
··

··
·

·

·

·

·
·

·

·

·
··

·

·

·

··
·
·
·
··

·
·

·
·

·
··

·

·
·

·
·

·

·
·
·
··
···

·

·
·
··

·
·
·

·
·

··

·
··

··

··

·

·

··
·
·
·
··
·
·

·

·
·
··
·
··

··

·
·

·
·
·
·
·
·

··

·

·

·

·
·
·

·

·
·

·
·

··

·
··

··

·

·

·

·
·
·

··
·
·

·

·
·
··
·
·
·

··

·

·

·
·
·

·
·

·
··

·

·

·
·
·
·
·
··

·

·
··
·

··

·
·
·

··
··

·

·

···

·
·

···
·
·

·

·

·
··
·
·

·
·

·

·

·
·

·

·

·
·

·

·

·
·
··
·
·
··

·

·

··
·

·
·
·
·
·

··
··

·

·

··
·

·
··
·
·

·
··

····
·
·

·
·
·
·

·
·

·
··

··

·

·
·

·
··
·

·
·
·

·

·

·

·

··
··
·
·

·
·

·

·

··

·
·

·
·
·
··

·
·

···
·

·
···

·
·

··
··

··
·

·
·
·

·
··
·
·
·
·

·
·
··

·

·
·
··

·
·
·

··
·
·

·
·
·

·····
·

·
··

····
·

·
·

·

·
··
·

···

·
·
·

·

·

·

·
·
·

·
·

·
·

·

·
·

·

·
··

··
·

··
·
·

··
··

·
·
·

·
·

·
·

·

·

·

·
·
··

·
·
·

·
·
··
··
·

·

·
·

··

··
·

··
··
·
·
·
····

·
·

·
··

····
·

·

·

··

·
·
·
·

··

·
·
··
·

·
·
·

·
·
·
·

·

·

·

··

·
·
·

·

·
·
··

·
·
··
···

··
·
·
·
·
··
·

·

·

·
·
·

··

·
·
·

··

·
····

·
·
·

··
·
·
·

·

·
··
··
·

·
·
·

·

··
··

·
·
·
····

·
·
·
·

·
··

·

·

·
·
·

·
·
·
·

··

··
·
··

·
·
·

·
·
·
··
·

·
·

··
·

·

··

·

·
·
·
·

·
·
·····

·
·
·
··

·
·
·
·

·

·

·
·
·

·
·

·
··

··

···
··
·
·

·
·
·
·
·
·

·

·
··

·

·
·
·
·
·
·
·

·
·
····

·
·
·
·
·

···
·
·

·

·

·

··
·
·

··

·
··

·
·
·

·
·
·
·
·

···

·
··
··

·

·

·
··
·

·
·
·
···
·
·

·
···
···

·
·
·
·

·
·

·

·

·

·

··
··

····
·
·
·

·
·
·
·
··
·

·
·

··
·
·
··

·

··
··
·

··
·
·

···
·
·

·
··
··
·
··

·
·
·
·
·
·
·

·
·

·
·

····
·
···

·

·
·

··
·
··
···

··
·

·
·
·
··

·

·
··
·

·
·
·
·
··

·

·
·
··
·

··
·

·
·
··
··
·
·
·
·

··

·
·
·
··
··
···

·

·
·

··

··
··
··
·

·
··
·

·

·

···
·

···

····

·

·

····

·
·

··
··
··
·
·
·
·
·

·
·
··
·
·
····

··
·

··

··
···
··
··
·

·
·
·
·

·

·
·
·
·
·
·

·
····

·

·
···

··
·

··
·
·
·

··
··
··
·

·
·

···
·
·
···

·
·
·
·

·
·
·
··
··
··

·

··

···

·

·
·
···
·

··
·
·
·
····

·

·

····
·
·
·

·

··
·

·
·
·

···
·
·
··

·
·
·
·
··
·
·
·
··
·

·

·
·

·
·

·

·
·
·

···
·

·
·
·
·
·
·

·
·
·
·
·
·

·

·
··
·

··
·
···

···

··
·
·

···
·
·
·
·
·
··

·
·
·

··
·
·
·

····
·

·
·
·
·
··

·

·
·
·
·
·
·

·

·
··
·

·
·
···
·
·
·
·

·

·
·
·

··
·
··
·

··
·

··

·
·

·
·
·

·

·
·
·
·

··
·
·
·

·

··
·
·
··
··
·
·
·
·

·
·
··
···
··

·

·
·
·
·
·

·
··
··

···
·

··

·

·

·
·
·
·

··
·
·
·
··
·

·
·

·

··
··

·
·
·
··

·
·

·
·
··
···

··
·

·
·
·

·
··

·

··
·
··
·
·

··

·

·

··
···
·

·····
·
·
··
·

··

·

··

···
····
·

·
·

··
·
··
·
·

··

··
·
·

·
·
·
·
·
··
·
·
·

·

·

·
·

·
·
·

·
·
····
····
··
·
··

·

·

···
·····

·
·

·
·

····
···
·
·

·
·
·

·

·
·
·
··
·
··

·

··
·

··

·
··

·

·
·

·
···
···
··
·
··
·

·

·
·
···

·
·

·
·
·
·
··
···
·
·

·
·
·
·

·
·
·
··
·
·
·
·

·
·

·

·

··

·

··
···
·
····
··

·
·
·

·

·
···
···

·

·
·

·
·
··
···

·
·

·
·
·
·

·

·
·
··
·

·
·
·
·

·
·
·

···

··

·

·
·
····
···
··

··
·
·
·

·

······
·
·

·

··
·
···
·

·
·

·
··
·

·

·
·
··

·
·

··

·
·
·
·

·
·
·

·

·

··
·
·
·
··
··
··

···
·
·

·

·
··
···
··
··

·

·
·
··
·
·
·

·

·

·

·

···
·
·

··

·

··
·
·

·

·

··
·

·
·

·
·
·
··
·
·
·

··
·
·
·

·
··

·
··
·
·
··

·

··
·
···
·
·
·
·

·

·

·

·

··
·
·

··

·
·

··
·
·
·

·

···
·

·
·
·

···
·
·
·
·
·
···
·

·

·
···

·
···
····
·

·

··
·
·

·
··
··

·

·
·
·
·
·
·
··

·

·
·
·
·
·

·
·

·

·
··
·

·
·

·

·
·
·

·
·
··

·
··

·

·

·
·
·
·

·
·
··
·
·

·

··
·

·

··

·

·

·
·
·

·
···
·
·

·

·
·
·
·

··

·

·
·
·

··

·
···
·

·
·
·

·
·
·

·

·

·
·
·
·

·
··
·
·
·

·

·
·
·

·
···

··

·

·
·
·

·
···
·

·

·
···

·

·

···
·

··
·
··
·
·

·
·
·
·
···
·
·

·

·
·
··
·
·
··
··
··

·

·
·

·

·
·
·
·
·
·

·
·
·

··
····

·
·
·
··

·

·

···
·
····
·
·

·
·
·
···

·
·

·

·
··
·
·
··

··
··
·

··

·

·
··
·
··
·

·
··

···
·
·

·

·
·
·
·

·

·

···
·

····
··

·
·
·
··
·

·

·
··

·

·
·
·
·
·
··
··

·
·

··
·
·
·
··

····
·
·
·
·
·

·

··
·

··
·

·
···
···
·
·
·

·
··
·
·
··
·
·
·
·
·
·
·
·
·
···
··
·

·
·

·
·
·
·
·
·
·

···

··
···
··

·

·
·
·

·
··
·
···
··
·
·
·

·
··

·
·

·
·
·

·
·
·
·
··
·
·
··
··

·
·

·
··
··

··

···
·
·
·
····

·

·
··

·
·

·
··
····
·
·
·

·
·
·

·

·

·
··
··
·
·
·

···

·
··
·

··
·

·
··
·
·

·

·
·····
·
····

·

·
·
·

···
·

·
···
·
·
·

·
·
·

·
·

·
·
··
·
·
·
··
·
·
·····
·

·
·

··
·

·

·

··
··
·
····
·
··
··

·
·

···

··
··
···

·

·
·

·

·

·
·

·
·
·

··
·
·
······

·

·
··
··

·

·

·
·

·

··
·
·
·

··
·

·

·
··

·
··
·
·
·
·

·

·
·
·
·

····

·
··

··
·
·
··

·

·

·

·
·

·
·

·
·

··
·

·
·
·
··
·

·

·
·
·

·

··

·

··
·····
·

·
··

·
·
····

·

·

··

·
·
·
·
·
·

·

·

·

·

·

·

·
·

·
·
·

·
·
·
·

·
·

··
·
·

·

·
··

·

·
···
·

·
··

·

·
·
···

··

·

··
·

·

··

·

·

·

·

·

·
·

··

·

·

·
·

·
·

·
·

·
··
·

·

·
·
·

·
·
··

Figure 8. Plot of Q7(x)for 2 ≤ g ≤ 212 and for some values of x.

data suggests that, asymptotically, one should have
∣ ˆN (g, x) − N (g, x)∣ = O ( √

x log log x
log x
 ) ,

wherenow theconstant implied by the O notation depends on g.It may very well
be that a similar result, with appropriate modiﬁcations, holds for the prime k-tuple
conjecture itself. Numerical experiments up to 10
17 appear to conﬁrm that this is
so. Rate of decay of N (g, x). It appears that, on a logarithmic scale, N (g, x)
does not deviate much from Ag,2 ∫ x
0 dt

log2 t exp
(
−g/(0.960 log x − 3.58)) (see, for ex-
ample, Figure 1 of [33] or Figure 2 of [49]). This empirical result was obtained using
a method similar to that used in subsubsection 2.1.3 to quantify the decay rate of(p, x). According to [33, 49] the exponent should be, asymptotically, −g/ log x,
which agrees reasonably well with our empirical results. The more prominent devi-
ations from a true exponential behavior are, in this case, due to the multiplicativeAg,2 =2C2 ∏p|g p−1

p−2 that are associated with the main term of ˆN (g, x). To
study the residual deviation of the exponential decay of N (g, x), Figure 9 presents
a plot of some values of

Q8(g)= 1
Ag,2 5 · 10
−16e
0.0266gN (g, 4 · 10
18).

The factor e
0.0266g removes most of the exponential decay of N (g, 4 · 10
18). The
scale factor 5 · 10
−16 ≈ log2 4 · 10
18/4 · 10
18 places Q8(p) close to 1. Similar behavior
was observed for other values of x (with diﬀerent exponents and scale factors). We
were unable to explain the residual pattern observed in Figure 9.
Just like what was done in subsubsection 2.1.3 to estimate the order of magnitude
of S(p), the order of magnitude of P (g) (or the order of magnitude of the largest g
for a given x) can be estimated by solving

2x
log2 x exp (
− g
0.960 log x − 3.58
 ) =1.

The left-hand side of this equation gives a rough estimate of the value of N (g, x),
obtained by ignoring the (relatively small) deviations of the decay of N (g, x)from

License or copyright restrictions may apply to redistribution; see https://www.ams.org/journal-terms-of-use

EMPIRICAL VERIFICATION OF THE EVEN GOLDBACH CONJECTURE 2055

gQ8(g)
0 100 200 300 400 500 600 700 800 900 1000
1.2

1.3

1.4

1.5

1.6

1.7
 ·

···
·
·
···
·

·
··

·
·
·

···
·
··
··
·
···

·

·
·

·
·
·
·
·
··
·
·
··
·
·
·
·
···
·
··
··
·
·
··

·

·
·

·
·
·
·
·
··
·
·
··
·

·

·

·

·
····
···
·
···

·
·

·

·
·
·

·

····
·

··
·

·

·

·

···
·
·
·
·
·
·

·
··
·
·
·
···
·
···
·
·
··
·

·

·

·

·
·
·

·

·
···
·
·
·
·
·
·
·
··
·

·

··

··

·

·
··
·

·
·
·
··
·
·
·
·
·

·
·
·
·

·

·
·
·····
···

·
···

·

·

·

·
·
·

·

···
·
·

·
·
·

·

·

·

···
··
··
·

·

·
·
·

·

·
·

·
··
·

···
·
··
·
·

·

·

·

·
··
·
·
·
·
·
·
··
·

·

·

·

·
·
·

·

··

··

·
···

·
·
·
·
·
··
·
·
·
·
···
·

·

·

·

·
··
·
·
·
··

·
··
·

·
·
·

·
·
·

·

·
··
·
····
·

·

·
···
·
····

·

·
·
·

·

·

·

·
··

·

···
·
·
··
·

·

·

·

·
··
·
·
·
·
·
·
··
·

·
·
·

··
·

·

··

··

·

·
··

·

··
·
··
··

·

·

·
···
·

·

·

·

·
··
·
··
··

·
···

·
·

·

·
·
·

·

···
·
·
··
·

·

·

·

·
··

·
·
···

·

·
·
·

·

·
·

·
··
·
···
·
·
·
·
·

·

·

·

·

··
·

·

·
·
·
·
·
·
·
·
·
·
·
·
·
·
··
··
·
·
·
··
·
·

·
·
·
·
·
··
·

·

·
·

·

·

·

·

·
·
·
·

Figure 9. Plot of Q8(g), for 2 ≤ g ≤ 1000.

gQ9(g)
100 300 500 700 900 1100 1300 1500
0.8

1.0

1.2

1.4

1.6
 ·

·
··
·
·

·

·
··

···

··

·
·
·
·
·
··
·

·
···

·
·

··
·
···
·
···

·

·
··
·
··
·
·
·····
·

·

··
·
·
···

·
··
·
·
·
··
···

·

··
·
·
··
·
·
······
·
·
···
·
····

·

·
·
··
·
··
·

·
···

·
·
··

·

·
·

·

··
·

··
······
·
·
·
·
·
········
···
····
·
·

···
·
···
·
·
·
···
····
·
·
····
·
··
·
·

·
·

·

··

·
··
·
····
·

·
··
··
··

·
·
··
···
·
·
·
·

····
·
·

·

····
·
·
·····
··

·

·
·
·
··
·
·····
···
·
·
·
·
···
·
···
·
····
·
·

·
··
·
··
·

·

······
··
·····
···
·

·
·
··
·
····
····
·
··
·
·
······

·
··
··
··
··
··
·
··
·
·····
·
···

·
·
·
·
·
·
··
·
·
·
···
····
·····
··
·
·
··
···
·
··
·
·
·
·
··
···
···
···
··
·
·
·
·
·
·
··
·
·
··
·······
·
······
········
··
··
·····
·
···
·
··
·
·······
·····
·
·
·········
·
·
·
·

·
·
·
·
·
·
···
······ ·
•◦
•◦

•◦
•◦

•◦
•◦
•◦•◦
•◦•◦

•◦
•◦•◦
•◦

•◦
 •◦
•◦
•◦
 •◦
•◦•◦•◦
•◦
•◦
•◦
•◦
•◦

•◦
 •◦•◦•◦•◦ •◦•◦•◦•◦•◦•◦•◦•◦•◦•◦
•◦•◦•◦•◦
•◦ •◦•◦•◦
•◦•◦•◦•◦•◦•◦•◦•◦•◦•◦•◦•◦•◦•◦ •◦•◦•◦•◦•◦
•◦•◦•◦ •◦•◦•◦•◦•◦ •◦
•◦
•◦•◦ •◦•◦
•◦•◦•◦ •◦
•◦•◦•◦ •◦•◦•◦•◦•◦ •◦•◦
•◦•◦
•◦ •◦ •◦•◦

•

•

•

•

•

•
 •
 •

•

••

•

•
 •

•• ••• •

•
•
 •
•

•
•••
•
•
•
•
•• •••
 • • • •
• •
•
 •

••
 •
 •• •
• •• • •• • •

Figure 10. Plot of Q9(g), for g ≥ 100 and P (g) < 4 · 10
18.
Disks (•), circles (◦), and dots (·) correspond respectively to data
obtained from Table 8, from Table 9, and to values of P (g)that
did not make it to either of the two tables.

a true exponential decay and by replacing Ag,2 by its average value of 2. We get
Q9(g) ≈ 1, where

Q9(g)= g
(0.960 log P (g) − 3.58)(log P (g) − 2 log log P (g) + log 2) .

Our empirical data (cf. Figure 10) supports the validity of this approximation.
The absence of the term −3.58 log P (g) in the denominator of Q6(g)appears to
be responsible for most of the increasing trend observed in Figure 7. Remarkably,9(g) ≈ 1gives g ∼ 0.96 log2 P (g), which is close to Shanks’ conjecture. It may be
that typical ﬁrst occurrences behave as Shanks’ conjecture predicts, and that max-
imal prime gap occurrences (the • points of Figures 7 and 10) behave as Granville
predicts. As in subsubsection 2.1.3, much more data is needed to settle this issue
(by empirical means).

License or copyright restrictions may apply to redistribution; see https://www.ams.org/journal-terms-of-use

2056 T. OLIVEIRA e SILVA, S. HERZOG, AND S. PARDI

Table 11. Number of twin-primes.

kπ2(10
k) π2(2 · 10
k) π2(4 · 10
k)
12 18705 85220 35527 70943 67568 32076
13 1 58346 64872 3 01988 62775 5 76572 48284
14 13 57803 21665 25 98584 00254 49 77948 45572
15 117 72092 42304 225 97583 03674 434 14016 30211
16 1030 41956 97298 1983 18470 25792 3819 68438 33352
17 9094 88393 53159 17544 83288 23978 33867 25524 19828
18 80867 58885 77436 1 56320 34990 75902 3 02346 31232 35320

Table 12. Normalized prime gap moments, and corresponding
best least-squares ﬁt data.

x D2(x)
2x log x D3(x)
6x log2 x D4(x)
24x log3 x
1010 0.84640 98596 0.69745 79430 0.56752 97645
1011 0.85853 04971 0.71959 94626 0.59635 95130
1012 0.86878 26270 0.73858 95560 0.62149 28727
1013 0.87758 46594 0.75507 98973 0.64360 59388
1014 0.88521 89506 0.76951 03964 0.66316 24243
1015 0.89190 91355 0.78225 50563 0.68059 59792
1016 0.89782 13100 0.79359 38057 0.69623 28171
1017 0.90308 62730 0.80375 06718 0.71033 90224
1018 0.90780 65824 0.81290 43169 0.72313 23343

best ﬁt data k =2 k =3 k =4
dk0 0.99260 0.98357 0.97109
dk1 −3.7012 −7.6839 −11.515
dk2 7.7338 25.268 51.238
max
x
 |Dk (x)− ˆDk (x)|
k! x logk−1 x 3.2 · 10−5 6.5 · 10−5 1.6 · 10−4

2.2.4. Counts of twin-primes. As usual, let π2(x) be the number of twin-primes
up to x, i.e., let it be the number of solutions, with pk ≤ x,of gk =2. When x
is an even integer, π2(x) diﬀers from N (2,x) only when x lies in the middle of a
twin-prime pair. Contrary to what happens to the π(x) function, the only known
way to compute π2(x) is to enumerate all twin-primes up to x. Table 11 presents a
small subset of the values of π2(x) collected during our veriﬁcation of the Goldbach
conjecture. As expected, π2(10
16) agrees with the value found by Pascal Sebah and
Xavier Gourdon in their computation of an estimate of Brun’s constant [42].Prime gap moments. Let

Dk(x)= ∑

pi+1≤x
(pi+1 − pi)k

be the k-order prime gap moment. In 1982 Heath-Brown [23] conjectured that
D2(x) ∼ 2x log x. As suggested by the ﬁrst author (based solely on empirical
evidence), and corroborated by Heath-Brown in an email exchange in April 2011,
the following more general conjecture is plausible:

Dk(x) ∼ k! x logk−1 x, k ≥ 1

License or copyright restrictions may apply to redistribution; see https://www.ams.org/journal-terms-of-use

EMPIRICAL VERIFICATION OF THE EVEN GOLDBACH CONJECTURE 2057

(the generalization to non-integral k is obvious). The upper part of Table 12
presents some empirical data supporting this conjecture. As suggested by Heath-
Brown, it turns out that our empirical data is very well approximated by

ˆDk(x)= k! x logk−1 x
 N∑

n=0
 dkn
logn x ,

where N is the order of the approximation. The lower part of Table 12 presents
the dkn coeﬃcients, to ﬁve signiﬁcant ﬁgures, obtained by performing second order
(N = 2) best least-squares ﬁts to the normalized data. Twenty approximately
equispaced (on a logarithmic scale) data points per decade, for 10
10 ≤ x ≤ 4 · 10
18,
were used to perform these ﬁts. The last row presents the normalized worst observed
absolute error for all of these data points, obtained using full-precision coeﬃcients.
Using a higher-order approximation, or using data starting at a higher value of x,
produced even better ﬁts, with dk0 coeﬃcients even closer to one (it appears that
we do not have enough data to estimate reliably the remaining coeﬃcients).

2.4. Veriﬁcation limit of the odd Goldbach conjecture. The odd Goldbach
conjecture states that every odd number larger than 5 is the sum of three prime
numbers. It is known to be true for all odd numbers larger than e
3100 [29], and
for all odd numbers larger than 5 and smaller than 1.13256 · 10
22 [39]. It is also
known to be true if the truth of the Riemann hypothesis is assumed [10]. Without
further computational eﬀort, this last limit can be extended to 8.37 · 10
26 using our
new veriﬁcation limit of the even Goldbach conjecture and the prime gaps bounds
of [39], as stated in the following theorem.

Theorem 2.1. Each odd number larger than 5 and smaller than

2092 67308 × 4 · 10
18 =8.37069232 · 10
26

is the sum of three prime numbers.

Proof. Let N0 =4 · 10
18 and let Δ = 2092 67308. From our prime gaps results
up to N0 (cf. subsection 2.2) and, in succession, from Theorems 3 and 2 of [39], it
can be inferred that, up to N0Δ, the gap between consecutive primes cannot be
larger than N0. The theorem follows by observing that using the odd primes up
to N0Δ to extend the minimal Goldbach partitions of 4, 6, ..., N0, and also of
N0 +2 = 211 +(N0 − 209) and N0 +4 = 313 +(N0 − 309), will necessarily create at
least one way of expressing each odd number larger than 5 and smaller than N0Δ
as a sum of three primes (actually, any suﬃciently dense subsequence starting with
the prime 3 will do [41]). □

Acknowledgments

In addition to the authors and their institutions (in particular, the third author
used the INFN-Grid infrastructure and the “SCoPE” supercomputing center of the
University of Naples Federico II), the following persons and institutions donated
processor cycles to the extensive computations reported in this paper (in decreasing
order of importance): NICS (National Institute for Computational Sciences, Cray
XT5 Kraken supercomputer, USA), Christian Kern (Germany), National Center
for Supercomputing Applications (NCSA, Xeon cluster, USA), Jo˜ao Rodrigues,
Ant´onio Teixeira, Carlos Bastos, the SIAS group, Rui Costa, Armando Pinho, and

License or copyright restrictions may apply to redistribution; see https://www.ams.org/journal-terms-of-use

2058 T. OLIVEIRA e SILVA, S. HERZOG, AND S. PARDI

Miguel Oliveira e Silva (all from the Department of Electronics, Telecommunica-
tions, and Informatics and from IEETA, University of Aveiro, Portugal), and Lau-
rent Desnogu`es (France). Mark Del´eglise (France) provided the computer program
used to compute the number of primes up to x belonging to each of the primitive
residue classes modulo 120.
 References

[1] Ralph G. Archibald, Goldbach’s theorem, Scripta Mathematica 3 (1935), 44–50, 153–161.
[2] A.O.L.Atkin andD.J. Bernstein, Prime sieves using binary quadratic forms,Math.Comp.
73 (2004), no. 246, 1023–1030 (electronic), DOI 10.1090/S0025-5718-03-01501-1. MR2031423
(2004i:11147)
[3] Carter Bays and Richard H. Hudson, The segmented sieve of Eratosthenes and primes in
arithmetic progressions to 1012, Nordisk Tidskr. Informationsbehandling (BIT) 17 (1977),
no. 2, 121–127. MR0447090 (56 #5405)
[4] Jan Bohman and Carl-Erik Fr¨oberg, Numerical results on the Goldbach conjecture,Nordisk
Tidskr. Informationsbehandling (BIT) 15 (1975), no. 3, 239–243. MR0389814 (52 #10644)
[5] Richard P. Brent, The ﬁrst occurrence of large gaps between successive primes,Math. Comp.
27 (1973), 959–963. MR0330021 (48 #8360)
[6] Richard P. Brent, The distribution of small gaps between successive primes,Math.Comp.
28 (1974), 315–324. MR0330017 (48 #8356)
[7] Harald Cram´er, On the order of magnitude of the diﬀerence between consecutive prime num-
bers, Acta Arithmetica II (1937), 23–46.
[8] M. Del´eglise and J. Rivat, Computing π(x): the Meissel, Lehmer, Lagarias, Miller, Odlyzko
method,Math. Comp. 65 (1996), no. 213, 235–245, DOI 10.1090/S0025-5718-96-00674-6.
MR1322888 (96d:11139)
[9] Marc Del´eglise, Pierre Dusart, and Xavier-Fran¸cois Roblot, Counting primes in residue
classes,Math. Comp. 73 (2004), no. 247, 1565–1575 (electronic), DOI 10.1090/S0025-5718-
04-01649-7. MR2047102 (2005a:11152)
[10] J.-M. Deshouillers, G. Eﬃnger, H. te Riele, and D. Zinoviev, A complete Vinogradov 3-primes
theorem under the Riemann hypothesis, Electron. Res. Announc. Amer. Math. Soc. 3 (1997),
99–104, DOI 10.1090/S1079-6762-97-00031-0. MR1469323 (98g:11112)
[11] J.-M. Deshouillers, H. J. J. te Riele, and Y. Saouter, New experimental results concerning
the Goldbach conjecture, Algorithmic Number Theory: ANTS-III Proceedings (J. P. Buhler,
ed.), Lecture Notes in Computer Science, vol. 1423, Springer-Verlag, Berlin / New York, 1998,
pp. 204–215.
[12] Jean-Marc Deshouillers and Herman te Riele, On the probabilistic complexity of numerically
checking the binary Goldbach conjecture in certain intervals, Number Theory and Its Appli-
cations (S. Kanemitsu and K. G¨yory, eds.), Kluwer Academic Publishers, Dordrecht / Boston
/ London, 1999, pp. 89–99.
[13] Leonard Eugene Dickson, History of the theory of numbers, vol. I: Divisibility and Primality,
AMS Chelsea Publishing, Providence, Rhode Island, USA, 1992, Published originally by the
Carnegie Institute of Washington (publication number 256) in 1919.
[14] Brian Dunten, Julie Jones, and Jonathan Sorenson, A space-eﬃcient fast prime number
sieve, Inform. Process. Lett. 59 (1996), no. 2, 79–84, DOI 10.1016/0020-0190(96)00099-3.
MR1409956 (97g:11141)
[15] W. Feller, The general form of the so-called law of the iterated logarithm, Trans. Amer. Math.
Soc. 54 (1943), 373–402. MR0009263 (5,125c)
[16] P. X. Gallagher, On the distribution of primes in short intervals,Mathematika 23 (1976),
no. 1, 4–9. MR0409385 (53 #13140)
[17] William F. Galway, Dissecting a sieve to cut its need for space, Algorithmic number theory
(Leiden, 2000), Lecture Notes in Comput. Sci., vol. 1838, Springer, Berlin, 2000, pp. 297–312,
DOI 10.1007/10722028 17. MR1850613 (2002g:11176)
[18] A. Granville, Harald Cram´er and the distribution of prime numbers, Scandinavian Actuarial
Journal 1995 (1995), no. 1, 12–28.

License or copyright restrictions may apply to redistribution; see https://www.ams.org/journal-terms-of-use

EMPIRICAL VERIFICATION OF THE EVEN GOLDBACH CONJECTURE 2059

[19] A. Granville, J. van de Lune, and H. J. J. te Riele, Checking the Goldbach conjecture on
a vector computer, Number Theory and Applications (R. A. Mollin, ed.), Kluwer Academic
Publishers, Dordrecht / Boston / London, 1989, pp. 423–433.
[20] Richard K. Guy, Unsolved problems in number theory, 3rd ed., Problem Books in Mathemat-
ics, Springer-Verlag, New York, 2004. MR2076335 (2005h:11003)
[21] G. H. Hardy and J. E. Littlewood, Some problems of ‘partitio numerorum’; III: On the
expression of a number as a sum of primes, Acta Mathematica 44 (1922), 1–70.
[22] G. H. Hardy and E. M. Wright, An introduction to the theory of numbers,5th ed., The
Clarendon Press Oxford University Press, New York, 1979. MR568909 (81i:10002)
[23] D. R. Heath-Brown, Gaps between primes, and the pair correlation of zeros of the zeta
function,ActaArith. 41 (1982), no. 1, 85–99. MR667711 (83m:10078)
[24] Chen Jing-Run, On the representation of a large even number as the sum of a prime and the
product of at most two primes,Sci.Sinica 21 (1978), 157–176, In chinese.
[25] Donald E. Knuth, 2006, PRIME-SIEVE-SPARSE program, retrieved on March 2012 from
http://www-cs-faculty.stanford.edu/~uno/programs/prime-sieve-sparse.w.
[26] Emmanuel Kowalski, Averages of Euler products, distribution of singular series and the
ubiquity of Poisson distribution,ActaArith. 148 (2011), no. 2, 153–187, DOI 10.4064/aa148-
2-4. MR2786162 (2012d:11199)
[27] J. C. Lagarias, V. S. Miller, and A. M. Odlyzko, Computing π(x): the Meissel-Lehmer method,
Math. Comp. 44 (1985), no. 170, 537–560, DOI 10.2307/2007973. MR777285 (86h:11111)
[28] W. A. Light, J. Forrest, N. Hammond, and S. Roe, A note on Goldbach’s conjecture,BIT 20
(1980), no. 4, 525, DOI 10.1007/BF01933648. MR605912 (82h:10003)
[29] Ming-Chit Liu and Tianze Wang, On the Vinogradov bound in the three primes Goldbach
conjecture,Acta Arith. 105 (2002), no. 2, 133–175, DOI 10.4064/aa105-2-3. MR1932763
(2003i:11147)
[30] Wen Chao Lu, Exceptional set of Goldbach number, J. Number Theory 130 (2010), no. 10,
2359–2392, DOI 10.1016/j.jnt.2010.03.017. MR2660899 (2011f:11133)
[31] Thomas R. Nicely, New maximal prime gaps and ﬁrst occurrences,Math. Comp. 68 (1999),
no. 227, 1311–1315, DOI 10.1090/S0025-5718-99-01065-0. MR1627813 (99i:11004)
[32] Bertil Nyman and Thomas R. Nicely, New prime gaps between 1015 and 5 × 1016, J. Integer
Seq. 6 (2003), no. 3, Article 03.3.1, 6 pp. (electronic). MR1997838 (2004e:11143)
[33] Andrew Odlyzko, Michael Rubinstein, and Marek Wolf, Jumping champions, Experiment.
Math. 8 (1999), no. 2, 107–118. MR1700573 (2000f:11164)
[34] Tom´as Oliveira e Silva, Fast implementation of the segmented sieve of Eratosthenes, Available
at http://www.ieeta.pt/~tos/software/prime_sieve.html#n, August 2003, 2010.
[35] Tom´as Oliveira e Silva, Computing π(x): the combinatorial method,Revista do DETUA 4
(2006), no. 6, 759–768, Available at http://www.ieeta.pt/~tos/bib/5.4.html.
[36] Alphonse de Polignac, Six propositions arithmologiques d´eduites du cribe d’Eratosth`ene,Nou-
velles Annales de Math´ematiques 8 (1849), 423–429.
[37] Paul Pritchard, Explaining the wheel sieve,ActaInform. 17 (1982), no. 4, 477–485, DOI
10.1007/BF00264164. MR685983 (84g:10015)
[38] Paul Pritchard, Fast compact prime number sieves (among others), J. Algorithms 4 (1983),
no. 4, 332–344, DOI 10.1016/0196-6774(83)90014-7. MR729229 (85h:11080)
[39] Olivier Ramar´e and Yannick Saouter, Short eﬀective intervals containing primes,J. Num-
ber Theory 98 (2003), no. 1, 10–33, DOI 10.1016/S0022-314X(02)00029-X. MR1950435
(2004a:11095)
[40] J¨org Richstein, Verifying the Goldbach conjecture up to 4 · 1014,Math.Comp. 70
(2001), no. 236, 1745–1749 (electronic), DOI 10.1090/S0025-5718-00-01290-4. MR1836932
[41] Yannick Saouter, Checking the odd Goldbach conjecture up to 1020,Math. Comp. 67 (1998),
no. 222, 863–866, DOI 10.1090/S0025-5718-98-00928-4. MR1451327 (98g:11115)
[42] Pascal Sebah and Xavier Gourdon, Introduction to twin primes and Brun’s constant compu-
tation, Retrieved from http://numbers.computation.free.fr/Constants/Primes/twin.html
on March 2012, 2002.
[43] Daniel Shanks, On maximal gaps between successive primes,Math. Comp. 18 (1964), 646–
651. MR0167472 (29 #4745)
[44] Mok-kong Shen, On checking the Goldbach conjecture, Nordisk Tidskr. Informations-
Behandling 4 (1964), 243–245. MR0172834 (30 #3051)

License or copyright restrictions may apply to redistribution; see https://www.ams.org/journal-terms-of-use

2060 T. OLIVEIRA e SILVA, S. HERZOG, AND S. PARDI

[45] Richard C. Singleton, Algorithm 357: An eﬃcient prime number generator, Communications
of the ACM 12 (1969), no. 10, 563–564.
[46] Matti K. Sinisalo, Checking the Goldbach conjecture up to 4 · 1011,Math.Comp. 61 (1993),
no. 204, 931–934, DOI 10.2307/2153264. MR1185250 (94a:11157)
[47] M. L. Stein and P. R. Stein, Experimental results on additive 2-bases, Mathematics of Com-
putation 19 (1965), no. 91, 427–434.
[48] Terence Tao, Every odd number greater than 1 is the sum of at most ﬁve primes,Math.
Comp., published electronically June 24, 2013.
[49] Marek Wolf, Some heuristics on the gaps between consecutive primes, arXiv:1102.0481v2
[math.NT], May 2011.
[50] Jeﬀ Young and Aaron Potler, First occurrence prime gaps,Math. Comp. 52 (1989), no. 185,
221–224, DOI 10.2307/2008665. MR947470 (89f:11019)

Departamento de Electr´onica, Telecomunicac¸ ˜oes e Inform´atica / IEETA, Universi-
dade de Aveiro, Portugal
E-mail address: tos@ua.pt
URL: http://www.ieeta.pt/~tos

Mont Alto Campus, The Pennsylvania State University, One Campus Drive, Mont
Alto, Pennsylvania 17237
E-mail address: hgn@psu.edu
URL: http://mac6.ma.psu.edu

INFN–Sezione di Napoli, Italy
E-mail address: spardi@na.infn.it

License or copyright restrictions may apply to redistribution; see https://www.ams.org/journal-terms-of-use
