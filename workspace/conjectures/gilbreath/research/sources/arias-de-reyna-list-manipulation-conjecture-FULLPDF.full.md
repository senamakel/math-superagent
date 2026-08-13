<!-- source: https://arxiv.org/pdf/2005.00530 | pdftotext -layout of the FULL PDF -->

                                               A RANDOM ANALOGUE OF GILBREATH’S CONJECTURE

                                                                                   ZACHARY CHASE




arXiv:2005.00530v3 [math.CO] 11 Jan 2022
                                                   Abstract. A well-known conjecture of Gilbreath, and independently Proth from
                                                   the 1800s, states that if a0,n = pn denotes the nth prime number and ai,n =
                                                   |ai−1,n − ai−1,n+1 | for i, n ≥ 1, then ai,1 = 1 for all i ≥ 1. It has been postulated
                                                   repeatedly that the property of having ai,1 = 1 for i large enough should hold for
                                                   any choice of initial (a0,n )n≥1 provided that the gaps a0,n+1 − a0,n are not too
                                                   large and are sufficiently random. We prove (a precise form of) this postulate.



                                                                                   1. Introduction
                                              Given any sequence of non-negative integers (an )n≥1 , we can form the sequence of
                                           non-negative integers (|an − an+1 |)n≥1 . Start with the primes as the initial sequence
                                           and iterate this consecutive differencing procedure. Gilbreath’s conjecture is that
                                           the first term in every sequence, starting with the first iteration, is a 1. Precisely,
                                           if a0,n = pn for n ≥ 1 and ai,n = |ai−1,n − ai−1,n+1 | for i, n ≥ 1, then ai,1 = 1 for all
                                           i ≥ 1. Below are the first few terms of the first few iterations.
                                                                               2    3   5
                                                                                        7 11 13 17
                                                                                   1 2 2 4 2 4
                                                                                    1 0 2 2 2
                                                                                     1 2 0 0
                                                                                      1 2 0
                                                                                       1 2
                                                                                        1
                                             Proth [6] discussed Gilbreath’s conjecture in 1878, before Gilbreath independently
                                           made the conjecture. Many sources claim Proth asserted he had a proof of the
                                           conjecture, and that his proof was wrong. However, we believe this claim is baseless.
                                           See Section 7 for more details. Odlyzko [3] verified Gilbreath’s conjecture for 1 ≤
                                           i ≤ π(1013 ) ≈ 3.34 × 1011 . One is led to wonder how special the primes are in
                                           Gilbreath’s conjecture and whether any sequence beginning with 2 followed by an
                                           increasing sequence of odd numbers with small and “random” gaps between them
                                           will have first term 1 from some iteration onwards.
                                              Date: May 1, 2020.
                                              The author is partially supported by Ben Green’s Simons Investigator Grant 376201 and grate-
                                           fully acknowledges the support of the Simons Foundation.



                                                                                             1
   Odlyzko, at the end of Section 2 of [3], speculates that such a random sequence
indeed will have first term 1 from some iteration onwards. Additionally, Problem 68
of [2] asks what gap or density properties of an initial sequence suffices to ensure the
conclusion of Gilbreath’s conjecture. Despite Gilbreath’s conjecture being around
for over a decade and several additional sources postulating that the conjecture
should hold for initial sequences with small and random gaps, as of date, nothing has
actually been proven along these lines, nor about Gilbreath’s conjecture specifically.
  In this paper, we initiate a rigorous study of Gilbreath’s conjecture by proving a
random analogue of it.
                                                                          1   log log M
Theorem 1. Let f : N → N be an increasing function with f (M) ≤ 100         log log log M
for M large and f (M) ≥ 2 for all M ≥ 1. Let a1 , a2 , . . . be a random infinite
sequence formed as follows. Let a1 = 2, a2 = 3, and for n ≥ 2, an+1 = an + 2un ,
where un is drawn uniformly at random from {0, 1, . . . , f (n) − 1}, independent of
the other ui ’s. Then, with probability 1, there is some M0 so that for all M ≥ M0 ,
after M iterations of consecutive differencing, the first term of the sequence is a 1.
   Computations suggest that Gilbreath’s conjecture holds because 0s and 2s form to
the right of the leading 1 early on. We prove Theorem 1 by showing that our random
initial sequence indeed has that property almost surely. Since the first iteration is
1, 2u2, 2u3 , . . . , if we ignore the leading 1 and divide by 2, what we wish to show is
encapsulated by the following theorem, which is the heart of the paper.
                                                           1   log log M
Theorem 2. For M large, for any C with 2 ≤ C ≤ 100           log log log M
                                                                             , if we form an
initial sequence of length M by choosing numbers from {0, . . . , C √− 1} independently
                                                                      20 log M          √
                                                                                        5
and uniformly at random, then, with probability at least 1 − e−e               , after e log M
iterations of consecutive differencing, everything is a 0 or 1.
   The randomness in Theorem 2 is certainly necessary. For example, if the initial
sequence consists of only 0s and 3s, then after any number of iterations, everything
is still a 0 or 3. However, there are more exotic examples of initial sequences
         2 0 6 0 2 2 6 5 0 0 6 1 3 2 2 3 0 6 0 5
           2 6 6 2 0 4 1 5 0 6 5 2 1 0 1 3 6 6 5
             4 0 4 2 4 3 4 5 6 1 3 1 1 1 2 3 0 1
              4 4 2 2 1 1 1 1 5 2 2 0 0 1 1 3 1
                0 2 0 1 0 0 0 4 3 0 2 0 1 0 2 2
                  2 2 1 1 0 0 4 1 3 2 2 1 1 2 0
                    0 1 0 1 0 4 3 2 1 0 1 0 1 2
                     1 1 1 1 4 1 1 1 1 1 1 1 1
                       0 0 0 3 3 0 0 0 0 0 0 0
for which all future iterations have only 0s and 3s (say). These exotic examples1
suggest that we are far away from a proof of Gilbreath’s conjecture.
  1To clarify, in the setting in which the primes are the initial sequence, the analogous situation
to having only 0s and 3s is having only 0s and 6s past the first index, making the first index very
likely to repeatedly change from 1 to 5 (see Lemma 3.5), thereby violating Gilbreath’s conjecture.
                                                2
                    2. A General Bootstrapping Argument
  In this section, we prove a result about random walks on regular directed graphs
that will be of use to proving Theorem 2.
Definition 2.1. A directed graph is regular if there is a positive integer d such that
each vertex has in-degree and out-degree equal to d. We allow our graphs to have
self-loops (but no multiple edges). For our discussion, a simple random walk on a
regular directed graph of degree d is formed by choosing a starting point uniformly
at random, and then walking along the directed edges, with each out-edge chosen
with probability 1/d, independent of the previous steps.
Proposition 2.2. Let G = (V, E) be a regular directed graph. Suppose V is red-
blue colored such that the probability a simple random walk on G of length L consists
entirely of red vertices is at least c. Then the probability a simple random walk on
                    1 2                                                    1 2
G of length ⌊(1 + 10  c )L⌋ consists entirely of red vertices is at least 10 c.
Proof. Let X1 , X2 , . . . denote the steps of a simple random walk. Define functions
w1 , . . . , wL on V by wj (v) := Pr(X1 , . . . , XL all red|Xj = v). Note (by, e.g., induc-
tion on the number of steps) the regularity assumption implies
                      wj (v) = |V | Pr(X1 , . . . , XL all red, Xj = v).
Thus, for any j, letting                                X
                                           wj (V ) :=             wj (v),
                                                        v∈V
we have by assumption
                                 X
                    wj (V ) =             |V | Pr(X1 , . . . , XL all red, Xj = v)
                                      v
                               = |V | Pr(X1 , . . . , XL all red)
                               ≥ c|V |.
Let K = ⌈ c32 ⌉, and let k1 , . . . , kK be kj := ⌊ Kj L⌋. By Cauchy-Schwarz,
                          !2 "             #                     !2 
        XX                            X         X X
(1)                wkj (v) ≤             12 ·             wkj (v) 
            v   j                          v                v       j
                                               "                                                      #
                                                XX                          XX
                                = |V |                  wkj (v)2 + 2                    wkj (v)wkj′ (v) .
                                               j   v                        j<j ′   v

Note, since ||wj ||∞ ≤ 1, we have
    XX                  XX               X
             wkj (v)2 ≤        wkj (v) =   |V | Pr(X1 , . . . , XL all red) ≤ K|V |;
        j   v              j      v                     j

also,                    XX                            X
                                          wkj (v) =             wkj (V ) ≥ Kc|V |.
                           v      j                     j
                                                        3
So (1) implies
                                            "                                          #
                                                             XX
                        K 2 c2 |V |2 ≤ |V | K|V | + 2                    wkj (v)wkj′ (v) ,
                                                             j<j ′   v

and thus, since K 2 c2 |V | − K|V | is increasing in K for K ≥ 3/c2 ,
                             6           XX
                                |V | ≤ 2        wkj (v)wkj′ (v).
                             c2            ′ v   j<j

By the pigeonhole principle, there are j < j ′ with
                          X                       1 3
                              wkj (v)wkj′ (v) ≥ 2 2 |V |.
                            v
                                                K c
Using
wkj (v) ≤ Pr(Xkj +1 , . . . , XL all red|Xkj = v) = Pr(Xkj′ +1 , . . . , XL+kj′ −kj all red|Xkj′ = v),
which is true merely due to translation invariance of the random walk, and
                           wkj′ (v) ≤ Pr(X1 , . . . , Xkj′ all red|Xkj′ = v),
we obtain
 1 3         X
  2 2
      |V | ≤      Pr(X1 , . . . , Xkj′ all red|Xkj′ = v) Pr(Xkj′ +1 , . . . , XL+kj′ −kj all red|Xkj′ = v)
K c           v
                  X
           = |V |    Pr(X1 , . . . , Xkj′ all red, Xkj′ = v) Pr(Xkj′ +1 , . . . , XL+kj′ −kj all red|Xkj′ = v)
                    v
                    X
           = |V |       Pr(X1 , . . . , XL+kj′ −kj all red, Xkj′ = v)
                    v
           = |V | Pr(X1 , . . . , XL+kj′ −kj all red),
yielding
                                                         1 3
                              Pr(X1 , . . . , XL+kj′ −kj all red) ≥
                                                               .
                                                        K 2 c2
Note K ≤ c32 + 1 ≤ c42 , so K12 c32 ≥ 163 2  1 2
                                         c ≥ 10 c . Since the proposition is trivial if
                                                                   2         c2
        2                             2
L < 10/c , we may assume L ≥ 10/c to obtain kj ′ −kj ≥ K   L
                                                             −1 ≥ c4 L−1 ≥ 10   L. 

Remark. It is natural to think that Proposition 2.2 can be extended, in some form,
to arbitrary length increases. However, such an extension is not possible in general
(note that iterating Proposition 2.2 results in only a summable geometric series of
length increases). For example, consider V = {1, . . . , n}, E = {(1 7→ 2), . . . , (n−1 7→
                                             1
n), (n 7→ 1)} with the vertices {1, . . . , 10 n} colored red and the rest blue. Then with
      1             1
L = 20 n and c = 20 , it holds that a simple random walk on G of length L will hit
only red vertices with probability at least c. However, of course no simple (random)
walk on G of length 5L = 12 n will hit only red vertices.
  Examples of such “bad” colorings also exist on the graph we apply Proposition
2.2 to, namely a Debrujin graph. We don’t think these colorings are actually the
ones we need to address in our proof of Theorem 2, but we couldn’t prove that.
                                                         4
                        3. A Lower Bound for Ending with 0
  We begin by exploiting the main property of the “dynamical system” of taking
consecutive differences: the supremum never increases. In fact, we use that it quickly
decreases provided there is no trivial obstruction to it doing so (Lemma 3.2).
Definition 3.1. We say non-negative integers a1 , . . . , ai come from a       e1 , . . . , a
                                                                                            ei+1 if
|e
 aj − a
      ej+1 | = aj for each 1 ≤ j ≤ i. Given a1 , . . . , ai and a subset E ⊆ Z, an E-block
is a contiguous set of terms aj1 +1 , . . . , aj1′ such that aj ∈ E for each j1 + 1 ≤ j ≤ j1′ ;
the length of the block is j1′ − j1 .
Lemma 3.2. Let a1 , . . . , ai be non-negative integers with d := maxj aj . Let L denote
the length of the longest {0, d}-block containing at least one d. If L ≤ i − 1, then,
after L iterations of consecutive differencing, the largest number is at most d − 1.
Proof. We induct on L. For L = 1, the result is clear. Assume L ≥ 2 and the result
is true for all L′ < L. It is easy to see that, since d is the maximum, any {0, d}-block
containing a d after an iteration would have had to have come from a {0, d}-block
of greater length containing a d, so the longest {0, d}-block containing a d after one
iteration is at most L − 1, say L′ . By induction, after L′ more iterations, the largest
number is at most d −1. It follows that after L (total) iterations, the largest number
is at most d − 1.                                                                     
  So, to prove Theorem 2, “all” we need to do is argue that long {0, d}-blocks
are unlikely to exist. In this next lemma, we observe that any large {0, d}-block
essentially must have come from a block with no 0s.
Lemma 3.3. Suppose that after i iterations, there is a dZ-block of length L. Then
either there was a dZ-block of length L + i in the initial sequence, or there is some
i′ , 0 ≤ i′ ≤ i − 1, such that after i′ iterations, there is a block of length L + i − i′
with no 0s.
Proof. We prove by induction on i the statement for all L. For i = 0, the result is
tautological. Take i ≥ 1, and suppose the result holds for i − 1. The dZ-block of
length L had to come from either a dZ-block of length L + 1 or a block of length
L + 1 with no 0s (since everything will have the same residue modulo d), so we are
done by the induction hypothesis.                                                
   Another nice property of the consecutive differencing operation is that it “com-
mutes” with reducing mod 2. This allows for a decently explicit formula for the
parity of a term after a given number of iterations, merely in terms of the parities
of the initial terms.
Definition 3.4. For non-negative integers a1 , a2 , define f1 (a1 , a2 ) = |a1 − a2 |, and for
any i ≥ 2 and non-negative a1 , . . . , ai+1 , define fi (a1 , . . . , ai+1 ) = |fi−1 (a1 , . . . , ai ) −
fi−1 (a2 , . . . , ai+1 )|. We say a1 , . . . , ai+1 ultimately iterate to fi (a1 , . . . , ai+1 ).
Lemma 3.5. For any i ≥ 1, there is a subset Ji ⊆ [i + 1] containing             P 1 and i + 1 so
that for any non-negative integers a1 , . . . , ai+1 , fi (a1 , . . . , ai+1 ) ≡ j∈Ji aj mod 2.
                                                    5
Proof. We induct on i. For i = 1, the result follows from |a1 − a2 | ≡ a1 + a2 mod 2.
Assume i ≥ 2 and the result is true for i − 1. Note that fi (a1 , . . . , ai+1 ) ≡
|f                  i ) − fi−1 (a2 , . . .P
Pi−1 (a1 , . . . , aP                     , ai+1 )| ≡ fi−1 (a1 , . . . , ai ) + fi−1 (a2 , . . . , ai+1 ) ≡
   j∈Ji−1 aj +         j∈Ji−1 aj+1 ≡        j∈Ji−1 △(Ji−1 +1) aj mod 2. By induction, Ji−1 contains
1 and i, and so Ji := Ji−1 △(Ji−1 + 1) contains 1 and i + 1, as desired.                                    

   We take a moment to note some useful corollaries of Lemma 3.5 which tells us
that the parity of what a1 , . . . , ai+1 ultimately iterate to depends linearly on each
of the parities of a1 and ai+1 . For example, let a1 , . . . , ai+1 be drawn independently,
uniformly at random from {0, . . . , C − 1}. Then, the probability a1 , . . . , ai+1 ulti-
mately iterate to an even integer is between 13 and 23 . And the probability that, for
j = i/2 say, all of fj (at , . . . , at+j ) are even, for t = 1, . . . , i/2, is exponentially small
in i/2.
   Let [C]0 = {0, . . . , C − 1}.
   The following proposition shows that 0s are not too rare, which will be useful
in conjuction with Lemma 3.3. Before the proof, we introduce some notation (for
                                                        ij
a given C and i). Define i0 = i and ij+1 = ⌊ 100C          2 ⌋ for 0 ≤ j ≤ C − 3.     For
1 ≤ j ≤ C − 2, let Ej denote the event that after i − ij−1 iterations there’s a
{0, C − j}-block of length (at least) ij−1 − ij . For example, E1 is the event that after
0 iterations, there’s a {0, C − 1}-block of length i − i1 , and E2 is the event that after
i − i1 iterations, there’s a {0, C − 2}-block of length i1 − i2 .
Proposition 3.6. For any C ≥ 2 and any i ≥ (200C 2 )2C , if a1 , . . . , ai are chosen
independently and uniformly at random from {0, . . . , C − 1}, then the probability
                                           1
they ultimately iterate to 0 is at least 200C 2.


Proof. Fix C ≥ 2 and i ≥ (200C 2 )2C . If C = 2, then Lemma 3.5 gives the result,
so assume C ≥ 3. We may suppose that the desired probability is at most 0.01.
Let B0 denote all i-tuples in [C]i0 that ultimately iterate to something 0 mod 2; we
say “conditional probability” when speaking of the conditional probability that B0
induces. Then, by Lemma 3.5, the conditional probability of ultimately iterating to
0 is at most 0.03, and so the conditional probability of not having only 0s and 1s
after some iteration is at least 0.97.
   Therefore, with conditional probability at least 0.97, some Ej occurs. Indeed,
otherwise, repeated use of Lemma 3.2 shows that after i−iC−2 iterations, everything
is a 0 or a 1: after i − i1 iterations, there are no more (C − 1)s and thus no (C − 1)s
ever again; after i − i2 iterations, there are no more (C − 2)s and thus no (C − 2)s
ever again, etc..
   Therefore, by the pigeonhole principle, there is some j, 1 ≤ j ≤ C − 2, such
                                                        0.97
that Ej occurs with conditional probability at least C−2     . Clearly j cannot be 1,
since we have the uniform distribution after 0 iterations. Also, j must be such that
C − j is odd, since by Lemma 3.5, the probability of having 2ij evens in a row is
                                                     6
                                   2 C
at most ( 23 )2ij ≤ ( 32 )2(200C ) (since, as is easy to verify, ij ≥ iC−2 ≥ (200C 2 )C for
each j). Since after i − ij−1 iterations, there are only ij−1 indices, a block of length
ij−1 − ij must contain the block [ij + 1, ij−1 − ij ] (see figure 1). So, with conditional
                          0.97
probability at least C−2       , all indices ij + ∆, for 1 ≤ ∆ ≤ ij−1 − 2ij , will be a 0 or
C − j.
   Let a1 , . . . , ai be the initial sequence, and note that, after i − ij−1 iterations, none
of the indices ij +∆ depend on a1 or ai (only the first and last indices do). Therefore,
                                                                  0.30
by Lemma 3.5, with (unconditional) probability at least C−2            , all ij + ∆ will be 0 or
C − j. Now, note that after i := i − ij−1 iterations, the integer at any index r is
equal to fi (ar , ar+1 , . . . , ar+i ).
                                                                            i − (ij−1 − ij )
                 0   ij   ij−1 − ij      ij−1                         i − ij−1            i − ij   i




                                                0   ij     ij−1 − ij ij−1

        Figure 1: Indicates which initial indices (in [i]) a particular index after i iterations depends on.

    Define a (regular) directed graph on [C]i0 by (x1 , . . . , xi ) → (x2 , . . . , xi , y) for
any x1 , . . . , xi , y ∈ [C]0 . Color a tuple (x1 , . . . , xi ) ∈ [C]i0 “red” if and only if it
                                                                                               0.30
ultimately iterates to 0 or C − j. The fact that, with probability at least C−2                     , all
fi (ar , ar+1 , . . . , ar+i ), for ij + 1 ≤ r ≤ (1 − ǫj )ǫ1 . . . ǫj−1 i, are 0 or C − j corresponds
                                                 0.30
exactly to: with probability at least C−2             , a simple random walk in [C]i0 of length
L := ij−1 − 2ij consists entirely of red vertices.
                                                                1
   Hence, by Proposition 2.2, with probability at least 20C       2 a simple random walk of
               1                                                        1              1
length2 (1+ 20C  2 )L consists entirely of red  vertices.  Now,  (1+  20C 2
                                                                            )L ≥ (1+ 40C 2 )ij−1
                             1                   1                                  ij−1
since it is equivalent to 40C 2 ij−1 ≥ (2 + 10C 2 )ij , which is true since ij ≤ 100C 2 . We
have thus shown that, if a1 , . . . , a(1+ 1 2 )ij−1 +i are chosen independently and uni-
                                                     40C
                                                              1
formly at random from [C]0 , then with probability at least 20C 2 , all fi (ar , . . . , ar+i )
                   1
for 1 ≤ r ≤ (1 + 40C 2 )ij−1 are either 0 or C − j.
   We’re nearly done, as (fi (ar , . . . , ar+i ))1≤r≤L′ is the whole sequence after i iter-
ations; since C − j is odd, we just need to additionally ensure that the ultimate
iterate is even. Specifically, we argue as follows.
  2To be light on notation, we suppress ceiling and floor functions in the rest of this section.
                                                           7
   We now deduce that, for L′ := ij−1 , if a1 , . . . , ai are chosen independently and
                                                                                  1
uniformly at random from [C]0 , then with probability at least 160C                  2 , they ulti-

mately iterate to something 0 mod 2 and each fi (ar , . . . , ar+i ), for 1 ≤ r ≤ L′ ,
                                             1
are either 0 or C − j. Let δ = 40C             2.    By Lemma 3.5, the proportion of walks
                                                                              ′
(X1 , . . . , X(1+δ)L′ ) in [C]0 of length (1 + δ)L′ that have at most δL4 values of j ∈ [δL′ ]
                               i
                                                                   ′ 
with3 (Xj+1 , Xj+2, . . . , Xj+L′ ) ∈ B0 is at most4 δL4 δLδL′ /4 2−δL ≤ 40C
                                                              ′            ′     1
                                                                                    2 . Therefore,

since the proportion of walks (X1 , . . . , X(1+δ)L′ ) with X1 , . . . , X(1+δ)L′ all red is at
          1
least 20C    2 , if we let A denote the walks (X1 , . . . , X(1+δ)L′ ) such that X1 , . . . , X(1+δ)L′
                                                      ′
are all red and such that there are at least δL4 values of j with (Xj+1, Xj+2 , . . . , Xj+L′ ) ∈
                                               1
B0 , then the density of A is at least 40C        2 . So on one hand,

                                      δL  ′
                     X                X                                     δL′ 1                ′
                                              1(Xj+1 ,...,Xj+L′ )∈B0 ≥             2
                                                                                     C i C (1+δ)L −1 ,
                                                                             4 40C
              (X1 ,...,X(1+δ)L′ )∈A j=1

while on another hand,
                    δL  ′                                  δL ′
       X            X                                      X              X                              X
                            1(Xj+1 ,...,Xj+L′ )∈B0 =                                                                      1
(X1 ,...,X(1+δ)L′ )∈A j=1                                  j=1 (Xj+1 ,...,Xj+L′ )∈B0 X1 ,...,Xj ,Xj+L′ +1 ,...,X(1+δ)L′
                                                                                            (X1 ,...,X(1+δ)L′ )∈A

                                                           δL ′
                                                           X              X                     ′
                                                       ≤                                C δL 1Xj+1 ,...,Xj+L′ all red
                                                           j=1 (Xj+1 ,...,Xj+L′ )∈B0
                                                                    ′
                                                                              X
                                                       = δL′ C δL                           1X1 ,...,XL′ all red .
                                                                        (X1 ,...,XL′ )∈B0

We deduce that
                                  X                                        1           ′
                                                1Xl ,...,XL′ all red ≥        2
                                                                                C i C L −1 ,
                                                                         160C
                            (X1 ,...,XL′ )∈B0

which is what we wanted to deduce.                                                                                        

Corollary 3.7. For any C ≥ 2 and any i ≥ 1, if a1 , . . . , ai are chosen independently
and uniformly at random from {0, . . . , C − 1}, then the probability they ultimately
                                    2 2C
iterate to 0 is at least ( C1 )(200C ) .
                                                                       1
Proof. For i ≥ (200C 2 )2C , Proposition 3.6 yields a lower bound of 200C 2 , and for
              2 2C
1 ≤ i < (200C ) , we use the trivial lower bound coming from aj = 0 for all j. 
   3Here we have abused notation, by associating the i-tuple that X
                                                                                j+1 , . . . , Xj+L′ form with
(Xj+1 , . . . , Xj+L′ ).                                                                  
   4The inequality following this footnote follows from the well known n ≤ ( en )k , giving
             −δL′                                                                      k         k
δL′ δL′                   ′
                              eδL′ δL′ /4 −δL′      ′
                                                          δL′
 4 δL′ /4 2         ≤ δL 4 ( δL′ /4 )    2     < δL
                                                  4 (0.91)
                                                                             1
                                                              . Note δL′ ≥ 40C 2 (200C ) .
                                                                                           2 C




                                                             8
                        4. Finishing the Proof of Theorem 2
  We now finish the proof of Theorem 2, copied below for the reader’s convenience.
                                                           1   log log M
Theorem 2. For M large, for any C with 2 ≤ C ≤ 100           log log log M
                                                                             , if we form an
initial sequence of length M by choosing numbers from {0, . . . , C √− 1} independently
                                                                      20 log M          √
                                                                                        5
and uniformly at random, then, with probability at least 1 − e−e               , after e log M
iterations of consecutive differencing, everything is a 0 or 1.
                                            1     log log M
   Fix M large and C in the range [3, 100       log log log M
                                                              ] (the case C = 2 is trivial). Let
             5
E1 denote√
               the event that after 0 iterations, there is a {0, C − 1}-block of length
        10
           log M
R := e           . Let E2 be the event that after 2R iterations, there is a {0, C −2}-block
of length R2 . Let E3 be the event that after 2R2 iterations, there is a {0, C − 3}-
block of length R3 . In general, for 2 ≤ j ≤ C − 2, Ej is the event that after 2Rj−1
iterations, there is a {0, C − j}-block of length Rj . Since 2Rj−1 ≥ 2Rj−2 + Rj−1 for
3 ≤ j ≤ C − 1, we see that, as before, by Lemma 3.2, if no Ej√occurs, then after
                                                                             5
2RC−2 iterations, everything is a 0 or a 1. Note that 2RC−2 ≤ e√ log M , so it suffices
                                                                           20 log M
to show that the probability that some Ej occurs is at most e−e                     . By the union
                                              √
                                             13
                                          −e log M
bound, it suffices to show Pr(Ej ) ≤ e                , say, for each 1 ≤ j ≤ C − 2.
                                             √
                                            13 log M
   Clearly, Pr(E1 ) ≤ M( 32 )R ≤ e−e        , so fix some j with 2 ≤ j ≤ C − 2. By
Lemma 3.3, if Ej occurs, either there is a (C − j)Z-block of length Rj in the initial
sequence or there is a block of length Rj in the first 2Rj−1 −1 iterations containing
                                                                                   √
                                                                                      no
                                                                                  13
                                                                      2 Rj   1 −e log M
0s. Once again, the first option holds with probability at most M( 3 ) ≤ 2 e            ,
                                                                            j−1
so by the union bound, it suffices to show that for each √     0 ≤ i ≤ 2R       − 1, the
                                                              10
probability that there is √a block of length L := Rj = ej log M without 0s after i
                          12 log M
iterations is at most e−e          , say.
     So fix some i ∈ [0, 2Rj−1 − 1]. Let b1 , . . . , bM −i denote the sequence after i itera-
tions. Let’s first focus on the block b1 , . . . , bL . Say the initial sequence is a1 , . . . , aM .
Note that bk(i+1)+1 = fi (ak(i+1)+1 , . . . , a(k+1)(i+1) ) for 0 ≤ k ≤ 12 R − 1. Since
( 12 R − 1)(i + 1) + 1 ≤ 21 R(i + 1) ≤ L and the sets {ak(i+1)+1 , . . . , a(k+1)(i+1) } are dis-
joint as k ranges, by independence the probability that b1 , . . . , bL are all nonzero is at
                            R/2
                       2 2C
most 1 − ( C1 )(200C )                by Corollary 3.7. Using the standard 1 −x ≤ e−x , we see
                            R/2                                                                  
               1 (200C 2 )2C                    R 1 (200C 2 )2C                   R −(log C)e5C log C
that 1 − ( C )                        ≤ exp − 2 ( C )               ≤ exp − 2 e                         ≤
                             1 log log M
                                                         √
                                                          15
                                                                               11√         
exp − R2 e−(log log log M )e 19             ≤ exp − R2 e− log M ≤ exp −e log M . There-
fore, by the union bound, the probability that √there is some√ block of length L after
                                                         11 log M        12 log M
i iterations containing no 0s is at most Me−e                      ≤ e−e          . The proof is thus
complete.                                                                                               
  5To be light on notation, we suppress ceiling and floor functions in this section.


                                                       9
                                5. Proof of Theorem 1
  In this section we deduce Theorem 1 from Theorem 2. We start with a lemma.
                                                                 1   log log M
Lemma 5.1. Take M large. Let f : [M] → {2, 3, . . . , ⌊ 100        log log log M
                                                                                 ⌋} be an increas-
ing function. Form a random initial sequence b1 , . . . , bM by choosing bm uniformly
at random from {0, 1, . . . , f (n) − 1}, independently of the other bi ’s. Then, with
                             1    2
probability at least 1 − e− 20 log M , after 3 logM2 M iterations of consecutive differencing,
everything is a 0 or 1.
  Before proving Lemma 5.1, let’s prove Theorem 1 assuming it.

Proof of Theorem 1. Let AM denote the event that after M iterations, the first term
is not a 1. We wish to show that, with probability 1, only finitely many AM ’s occur.
By Borel-Cantelli, it suffices to show that for all M large, the probability of AM
                               1    2
occurring is at most e− 30 log M . Note that AM is equivalent to a1 , . . . , aM +1 not
ultimately iterating to 1. For M large enough, by Lemma 5.1, with probability at
             1   2
least 1−e− 20 log M , after 3 logM2 M iterations of consecutive differencing beginning with
initial sequence u2 , . . . , uM , everything is a 0 or 1. Therefore, with probability at
             1   2
least 1−e− 20 log M , after 3 logM2 M iterations of consecutive differencing beginning with
initial sequence 2u2 , . . . , 2uM , everything is a 0 or 2. It follows that with probability
               1    2
at least 1−e− 20 log M , after 1+3 logM2 M iterations of consecutive differencing beginning
with initial sequence a1 , . . . , aM +1 , the obtained sequence starts off with an odd
                      1   log log M
number at most 100      log log log M
                                      followed by only 0s and 2s. By Lemma 3.5, with
                                1    2
probability at least 1 − e− 10 log M , the second term of the sequence is congruent
to 2 mod 4 at least 31 log2 M times out of the log2 M iterations following the (1 +
                                                                      1    2       1     2
3 logM2 M )th iteration. Therefore, with probability at least 1 − e− 20 log M − e− 10 log M ≥
        1   2
1 − e− 30 log M , starting with a1 , . . . , aM +1 , after 1 + 3 logM2 M + log2 M iterations, the
first term will be a 1, and therefore will remain a 1 all the way until the final (i.e.,
M th ) iteration, since everything else is a 0 or 2.                                           

Definition 5.2. Let a1 , . . . , aM +1 be non-negative integers. We say that an index
i ∈ [M + 1] influenced the index j ∈ [M + 1 − t] after t iterations if 0 ≤ i − j ≤ t.
Recall that ft (aj , . . . , aj+t) is the value at index j after t iterations.
   We finish by proving Lemma 5.1. The idea of the proof is as follows. By Theorem
2, the blocks on which f is constant will become all 0s and 1s after not too many
iterations. Although there are some indices that were influenced by indices where
f took different values, these indices are contained in not too many not too large
intervals, so we can let all the 0s and 1s drop the values at these “bad indices” with
a few extra iterations.
   We start by proving a lemma that allows us to isolate these “bad indices”. For an
interval I ⊆ N, let L(I) and R(I) denote its left and right endpoints, respectively.
                                               10
Lemma 5.3. Suppose M is large, and let CM be a positive integer with CM ≤
log log
      √
         M. Let I1 , . . . , Ir ⊆ [M] be disjoint intervals with r ≤ CM and |It | ≤
      5
        log M
CM e          for each t. Then there are pairwise disjoint intervals J1 , . . . , Js ⊆ [M],
each containing some It , such that the following two hold.
      • For all t, 1 ≤ t ≤ r, there is some m with It ⊆ Jm .
      • For any m, 1 ≤ m ≤ s, if we let Bm denote the smallest interval con-
          taining all of the It ’s in Jm , then we have that either L(Bm ) − L(Jm ) ≥
          (log2 M)CM |Bm | or R(Jm ) − R(Bm ) ≥ (log2 M)CM |Bm |, with both being true
          if Jm contains neither 1 nor M.
Proof. For a subset A of [r], let BA denote the smallest interval containing ∪t∈A It ,
and let J(A) denote the smallest interval containing ∪t∈A It such that either L(BA )−
L(J(A)) ≥ (log2 M)CM |BA | or R(J(A))−R(BA ) ≥ (log2 M)CM |BA |, with both being
true if J(A) contains neither 1 nor M; if no such interval exists, we let J(A) = ∅. Let
C0 = {J({t}) : 1 ≤ t ≤ r}. For i ≥ 0, if Ci contains two intervals J(A1 ), J(A2 ) that
intersect, we define Ci+1 to be the same as Ci , except we replace J(A1 ) and J(A2 )
with J(A1 ∪ A2 ) (Ci+1 thus could depend on the choice of intersecting intervals).
Say C0 , . . . , Ck−1 are the defined collections. It is clear that k ≤ r and that if each
element of Ck−1 is non-empty, then the elements of Ck−1 satisfy the conditions of
Lemma√ 5.3. The largest diameter      √
                                         of an interval in C0 is at most (2(log2 M)CM +
        5                              5
1)CM e log M ≤ 3(log2 M)CM CM e log M . If J(A1 ) and J(A2 ) each have diameter at
most D and intersect, then the diameter of J(A1 ∪ A2 ) is at most (2(log2 M)CM +
1)(2D) ≤ 6(log2 M)CM D. Therefore, √each interval in any Ci−1 has √diameter at√ most
                                           5                             5          4
6i−1 (log2 M)(i−1)CM 3(log2 M)CM CM e log M ≤ 6r (log2 M)rCM CM e log M ≤ e log M .
To finish the√ proof, it just remains to note that J(A) 6= ∅ if the diameter of ∪t∈A It
                 4
is at most e log M .                                                                    

                                √
                                5
Proof of Lemma 5.1. Do e log M iterations of consecutive differencing. For 2 ≤ C ≤
 1    log log M
100 log log log M
                  =: CM , we say that an index j is C-pure if f took the value C at
                                                                        √
                                                                        5
all indices in the initial sequence that influenced j (after e log M iterations). Let I
denote the indices that are not C-pure for any C. Write I = ⊔rt=1 It as a disjoint√
                                                                                  5
union of intervals with r minimal. Clearly r ≤ CM . Also, crudely, |It | ≤ CM e log M
for each t.
  Let J1 , . . . , Js be the intervals guaranteed6 by Lemma 5.3, and let B1 , . . . , Bs be
as in Lemma 5.3. For any C, by7 Theorem 2 applied to the (interval of) C-pure         √
                                                                                     20 log M
indices, the probability that all C-pure indices are 0 or 1 is at least 1 − e−e               ,
                                             √
  6We are applying Lemma 5.3 with M − e 5 log M instead of M , but all bounds are essentially the
same.
   7As stated, Theorem 2 only applies to initial sequences of length M . However, given any shorter
initial sequence, we can independently
                                    √
                                        add elements uniformly chosen from {0, . . . , C −1} to obtain
                                     5
a sequence of length M , then do e log M iterations, and then truncate the sequence to keep only
indices influenced by the original initial sequence.
                                                 11
and therefore the probability         that all indices that are C-pure for some C are 0 or 1
                             √
                            20                  √
                         −e log M            − 21 log M
is at least
         √
              1 −   C M e           ≥  1  − e           . In particular, with probability at least
        21
1 − e− log M , all indices in ∪sm=1 (Jm \ Bm ) are 0 or 1; we from here on condition on
                                                                             j
this being the case. For 1 ≤ m ≤ s and 1 ≤ j ≤ CM − 1, let Jm                    denote the interval
                             2    j                                      2    j
(of length
      √
             |J m | −  2(log   M)   |Bm  |) whose   indices  after 2(log   M)   |Bm | iterations past
      5
        log M                                                              j
the e         th are influenced by indices only in Jm , and let Bm denote the interval (of
length
  √
         |Bm |+2(log2 M)j |Bm |) whose indices after 2(log2 M)j |Bm | iterations past the
  5
e log M th are influenced by at least one index in Bm . Note that Lemma 5.3 implies
Bmj
     ⊆ Jm j
             for each 1 ≤ j ≤ CM − 1 (since 2(log2 M)CM −1 |Bm | ≤ (log2 M)CM |Bm |).
                           0
   For 1 ≤ m ≤ s, let Em     denote the event that there is a {0, CM }-block in Jm
of length (log2 M)|Bm | containing a CM . For 1 ≤ m ≤ s and 1 ≤ j ≤√CM − 2,
                                                                                 5
let Emj
        denote the event that, after 2(log2 M)j |Bm | iterations (past the e log M th),
there is a {0, CM − j}-block in Jm j
                                     of length (log2 M)j+1 |Bm | containing a CM − j.
Fix m with 1 ≤ m ≤ s. As in the proofs of Proposition 3.6 and Theorem 2, since
2(log2 M)i+1 |Bm | ≥ (log2 M)i+1 |Bm |+2(log2 M)i |Bm |, if none of Em
                                                                     0    1
                                                                       , Em            CM −2
                                                                            , . . . , Em
occur, then after 2(log2 M)CM −1 iterations, the largest number in Jm   CM −1
                                                                                is a 1.
   Note that any CM ’s in Jm lie in Bm , so by Lemma 3.5, the probability that
                                    1   2
Em0
     occurs is at most 2( 21 ) 2 log M , since either to the left or to the right of Bm
must be 12 log2 M consecutive 0s. Similarly, the length of the longest {0, CM − j}-
              j                                  j
block in Jm      is at most the whole of Bm           and 0s surrounding it, so the probability
                                   1   2
                                1 4 log M
  j
Em occurs is at most 2( 2 )                . Therefore, the probability that at least one of
                                                 1      2                      1   2          1   2
  0           CM −2
Em , . . . , Em      occurs is at most 2( 21 ) 2 log M + (CM − 2)2( 12 ) 4 log M ≤ e− 10 log M .
            CM −1      CM −1                 0              Cm −2
Since Bm          ⊆ Jm       , if none of Em   , . . . , Em        occur, then the elements of (the
growing) Bm became 0 and 1 quickly enough to not affect anything outside of (the
                                                    0            CM −2
shrinking) Jm . In particular, if none of Em          , . . . , Em     occur for any m (i.e. for each
                                          2
                          8
m, none occur), then after 2(log M)            CM −1
                                                         max1≤m≤s |Bm | ≤ 2 logM2 M iterations past
      √
      5
the e log M th, everything is a 0 or 1. Since the probability at least one Em j
                                                                                (over all
                             1     2       1     2
                           − 10 log M    − 20 log M
j, m) occurs is at most se            ≤e            , Lemma 5.1 is established.        
                       6. Additional Mathematical Remarks
  The proof of Theorem 2 can be relatively easily adapted to handle any distribution
(not just the uniform distribution) on {0, . . . , C −1} that gives not too large, positive
weight to each of 0, . . . , C − 1 (one should create duplicate vertices in [C]i0 so that
the obtained simple random walk models this different probability distribution).
                                                            √
                                                           20 log M
                                                                         √
                                                                         5
  In Theorem 2 we did not try to optimize e−e         nor e log M . A proof allowing
                               2
C to go all the way up to log M, or even a power of M, would be interesting. We
expect that, in reality, the highest C can go is M, in that if C = o(M), then with
  8It is clear from Lemma 5.3 that |B              M
                                        m | ≤ (log2 M)CM   for each m.

                                                 12
probability 1 − o(1), after M2 iterations, everything is a 0 or 1, while if C = ω(M),
with probability o(1), after M2 iterations, everything is a 0 or 1.

                               7. A Historical Remark
  Various sources (websites, blog posts, etc.) have claimed that Proth believed he
had proven Gilbreath’s conjecture, and that his proof turned out to be wrong.
  Not only do we currently have no evidence for this claim, the apparent source of
this claim has retracted it.
   The claim seemed plausible, for Proth did publish a paper [6] on (what later
became known as) Gilbreath’s conjecture and did, admittedly confusingly, call it a
“theorem”. However, a reading through the paper shows he did not seriously claim
a proof. Indeed, Hugh Williams who made the claim about Proth without reference
[7, p. 123], said “On rereading his actual paper ... I can find no support for my
assertion. ... My apologies for seeming to have started a myth” [8].
   We also take this time to correct another historical error, which actually is com-
posed of two suberrors. The first suberror is that many sources incorrectly cited
[5] when referring to Proth’s discussion of Gilbreath’s conjecture, referring to the
correct title “Théorèmes sur les nombres premiers” but citing Comp. Rend. Acad.
Sci. Paris, 85 (1877) instead of Comp. Rend. Acad. Sci. Paris, 87 (1877). The
former actually corresponds to a completely unrelated paper of Pepin [4]. The sec-
ond suberror is that, the intended reference, [5], didn’t even discuss Gilbreath’s
conjecture! We were only able to find Proth discussing Gilbreath’s conjecture in [6].
  We refer the reader to [1] for more information surrounding all of this.

                                 8. Acknowledgments
   I would like to thank my advisor, Ben Green, for suggesting this problem to me
and Daniel Korandi for helpful feedback on the introduction. I would also like to
thank Juan Arias de Reyna for bringing to attention the dubious nature of the
claim discussed in Section 7, and Hugh Williams for kindly responding to emails
and helping resolve the situation.

                                        References
 [1] J.    Arias-de-Reyna,        Gilbreath’s    conjecture,      blog     post    available  at
     https://institucional.us.es/blogimus/en/2020/07/gilbreaths-conjecture/
 [2] H. L. Montgomery, Ten lectures on the interface between analytic number theory and harmonic
     analysis, CBMS No. 84, Amer. Math. Soc, Providence, 1994.
 [3] A. M. Odlyzko, “Iterated absolute values of differences of consecutive primes”, Math. Comp.,
     61 (1993) 373-380.
                                  n
 [4] F. Pepin, “Sur la formule 22 + 1”, Comp. Rend. Acad. Sci. Paris, 85 (1877), 329-331.

                                               13
[5] F. Proth, “Théorèmes sur les nombres premiers”, Comp. Rend. Acad. Sci. Paris, 87 (1877)
    329-331.
[6] F. Proth, “Sur la série des nombres premiers”, Nouvelle Correspondance Mathématique, 4
    (1878) 236-240.
[7] H. C. Williams, Edouard Lucas and Primality Testing, Canad. Math. Soc. Ser. Monogr. Adv.
    Texts, Wiley, (1998).
[8] H. C. Williams, Email correspondence (2020).

  Mathematical Institute, Andrew Wiles Building, Radcliffe Observatory Quar-
ter, Woodstock Road, Oxford OX2 6GG, UK
  Email address: zachary.chase@maths.ox.ac.uk




                                            14
