<!-- source: https://www.numdam.org/item/10.1051/ita:2006017.pdf | converted from PDF -->

RAIRO-Inf. Theor. Appl. 40 (2006) 107-121

DOI: 10.1051/ita:2006017

INCREASING INTEGER SEQUENCES
AND GOLDBACH’S CONJECTURE ∗

Mauro Torelli 1

Abstract. Increasing integer sequences include many instances of in-
teresting sequences and combinatorial structures, ranging from tour-
naments to addition chains, from permutations to sequences having
the Goldbach property that any integer greater than 1 can be obtained
as the sum of two elements in the sequence. The paper introduces
and compares several of these classes of sequences, discussing recur-
rence relations, enumerative problems and questions concerning short-
est sequences.

Mathematics Subject Classiﬁcation. 11Y55, 11P32, 05A15,
11B99.
 1. Introduction

Long-standing conjectures are obviously diﬃcult to settle, but we can derive
some – hopefully interesting – sequences from them. Let us see three examples.
The well-known Goldbach’s conjecture, open since 1742, states that any even
number greater than 2 can be expressed as the sum of two primes. A relatively
recent paper on the subject, with pointers to the huge number of references, is [5].
The conjecture has been veriﬁed up to 4 × 1014 [19], and several theorems have
been proved, such as the following: every positive even integer is the sum of at
most 6 primes,or every suﬃciently large even integer may be written as the sum
of a prime and a number that has at most 2 prime factors.
Let Z
+ be the positive integers, P the primes and E the even positive integers.
Let A be a subset of Z
+: we will write 2A to indicate the sumset A + A obtained
by summing any two (not necessarily distinct) elements of A (cf. e.g. [15], p. 192).
The aim of this notation is to express Goldbach’s conjecture in the terse form

∗ The present work has been supported by M.I.U.R. COFIN, under the project “Linguaggi
formali e automi: metodi, modelli e applicazioni”.
1 Universit`a di Milano, Dipartimento di Scienze dell’Informazione, via Comelico 39, 20135
Milano, Italy; torelli@dsi.unimi.it c× EDP Sciences 2006

Article published by EDP Sciences and available at  http://www.edpsciences.org/ita or http://dx.doi.org/10.1051/ita:2006017

108 M. TORELLI

2 357111317 1235 68 1 23510 22 49
122 4 2 4 11212 112 5 12 27
1022 2 011 1 013 7 15
12 00 100 12 4 8
120 10 1 2 4
12 1 1 2
11
(a) (b) (c)

Figure 1. Gilbreath sequences and absolute diﬀerence triangles.

E −{2}⊆ 2P. But we would like also to eliminate the irrelevant fact of 2 being
the only even prime number, and are thus led to deﬁne Goldbach sets as those
subsets S of Z
+ such that Z
+ −{1}⊆ 2S (in fact, Z
+ −{1} =2S). Furthermore,
we will only consider ﬁnite subsets of any such set S, uptoagiven maximum value,
and will represent them as increasing sequences, to be called Goldbach sequences.
Some further terminology and notation about sequences will now be introduced,
and Goldbach sequences will be deﬁned formally.

Deﬁnition 1. An increasing integer sequence (iis) of length r is a ﬁnite sequence
a0,a1, ..., ar of positive integers such that a0 =1 and ai−1 <ai, 1 ≤ i ≤ r.

Let s be an iis, then the length r of s will be denoted by l(s), while max(s) will
denote the maximum element ar.Observe that l(s) < max(s).

Deﬁnition 2. An iis is a Goldbach sequence if and only if for any integer x such
that 2 ≤ x ≤ ar, x = aj + ak for some j, k with 0 ≤ j ≤ k< r.

Example 1. s = 12356891114 1518 is a Goldbach sequence, as canbe
easily checked. Its length is 10 and, for 0 ≤ i ≤ 10, 2ai +1 is the (i + 2)-nd prime.
12 48is not a Goldbach sequence, since 7 cannot be obtained as speciﬁed in the
deﬁnition.

Sequence s in Example 1 shows that it would be convenient to have a name
for numbers q such that 2q + 1 is prime: perhaps primoids would be adequate,
so that we could refer to the inﬁnite sequence starting with s as the sequence of
primoids. Then, Goldbach’s conjecture could be stated in the form: any integer
greater than 1 can be obtained as the sum of two primoids.
Goldbach sequences clearly are a (very) particular case of addition chains,to
be introduced in Deﬁnition 9, where only each element in the chain is required
to be the sum of two preceding elements. Before examining more general classes
of sequences, let us consider another, slightly less-well-known, number-theoretic
conjecture: Gilbreath’s conjecture (cf. e.g. [13, 17]). This conjecture is best
explained by an example: let us take a short preﬁx of the sequence of primes, say
2 3 5 7 11 13 17, and construct a triangle in which each element is the absolute
value of the diﬀerence of the two elements above it, like in Figure 1a.

INCREASING INTEGER SEQUENCES AND GOLDBACH’S CONJECTURE 109

Gilbreath’s conjecture simply states that, for the sequence of primes, the ﬁrst
element in each subsequent row of the triangle is 1. For an iis we can adopt the
following deﬁnition.

Deﬁnition 3. An iis is a Gilbreath sequence if and only if for any i with 0 ≤ i< r,
ai,0 ≤ 1, where a0,k := ak,0 ≤ k ≤ r; ai+1,j := |ai,j − ai,j+1|,0 ≤ i<r,
0 ≤ j< r − i.

Cases (b) and (c) of Figure 1 show, in the ﬁrst row a0,k, two examples of
Gilbreath sequences, together with the subsequent rows ai,j. Deﬁnition 3 requires
the condition ai,0 ≤ 1, instead of the conjecture statement ai,0 =1, because, as
before, it eliminates the peculiarities due to 2 being the only even prime number;
in fact, in the examples, a2,0 = 0, and example (b) is nothing but example (a) after
removing ai,0 and dividing by 2, passing from primes to primoids. Example (c)
will be considered later on.
Let us now introduce the last conjecture. Sequence 3 10 5 16 8 4 2 1 is not an
iis, but should be easily recognized as an example of Collatz 3x +1 problem:start
with any integer number x> 1, divide it by 2 if it is even, otherwise take 3x +1.
The conjecture is that we always get to 1 (cf., e.g., [12]). Now, to get to an iis,
reverse the original sequence: 124816510 3, start from 1and compare each
element with its successor: if there is an increase, then increase by 1, otherwise
increase by 2: 123457810. In the following, sequences obtained in this way,
although not deﬁned formally, will be called Collatz sequences.
Collatz sequences increase very slowly, since ai ≤ ai−1 +2, 2 ≤ i ≤ r and
therefore ai ≤ 2i, but, of course, not every iis with ai ≤ 2i is Collatz. However, we
shall show in next section that every iis with ai ≤ 2i is Goldbach, therefore every
Collatz sequence is Goldbach. On the other hand, it is easy to ﬁnd a Gilbreath
sequence which is not Goldbach, and vice versa, thus showing that these two
conjectures for primes are – at least in this respect – independent. Here are the
counterexamples: the Goldbach sequence 123 6isnot Gilbreath (a3,0 = 2), while
the sequence in Figure 1c cannot be Goldbach, since 22 > 2 × 10, and therefore at
least 21 and 22 cannot be obtained by adding two preceding elements.
The condition ai+1 ≤ 2ai is obviously necessary for an iis to be Goldbach, and
we are thus led to examine sequences verifying this condition. However, we have
already seen that such a condition is violated by Gilbreath sequences. Therefore,
looking for a set including all of the already mentioned sequences, we are forced to
relax this condition. What happens if we construct the diﬀerence triangle bottom-
up by putting 1 at the beginning of each row and then increasing each row as
much as possible? The upper row will be made by the successive powers of 2:
therefore, the appropriate condition is ai ≤ 2i. Fortunately, this condition also
yields an upper bound for all sequences (including Goldbach) satisfying the former
necessary condition.
We will examine these classes of sequences (and a few more) in the next sec-
tion. Section 3 will be devoted to enumeration, while Section 4 will discuss some
questions about shortest sequences.

110 M. TORELLI

2. Subexponential sequences

In the present paper only sequences satisfying the condition ai ≤ 2i are consid-
ered, and this choice was motivated in the Introduction. It seems, therefore, more
or less appropriate to call these sequences subexponential sequences, since they are
superiorly bound by the exponential sequence 1 2 4 8 16 ... Actually, sequences
satisfying this condition are in bijection with full (or complete) sets (sets whose
elements are also subsets: cf. [3], p. 122). Sequences in this class can, of course,
increase exponentially with length, so in this respect the name is misleading: we
use it in the same sense in which sequences superiorly bound by Fibonacci numbers
have been expressively called sub-Fibonacci [9].
Now we want to progressively restrict the range of possible sequences. It turns
out that one of the weakest restrictions is obtained by relaxing the condition
deﬁning Goldbach sequences: instead of requiring that value x be obtained by
summing two elements, we can require x to be obtained by summing any number
of elements. The following lemma is general enough to allow for repeated elements.

Lemma 1. Let a0 ≤ a1 ≤ ... ≤ ar be positive integers and set σ(k):= )k
j=0 aj
for k ≤ r. For any x, 1 ≤ x ≤ σ(r), one can determine χi(x) ∈{0, 1}, 0 ≤ i ≤ r,
such that x = )r
i=0 ai · χi(x),if and only if a0 =1 and ai+1 ≤ σ(i)+1 for
0 ≤ i<r.

Proof. Case x =1 requires a0 = 1, and then the lemma is true for r =0. Let it
be true for r = k ≥ 0: then any x ≤ σ(k) can be obtained, but if ak+1 >σ(k)+ 1,
then there is no way to obtain x = σ(k) + 1. On the contrary, if ak+1 ≤ σ(k)+ 1
and ak+1 ≤ x ≤ σ(k +1) = σ(k)+ ak+1,then x = ak+1 + )k
i=0 ai · χi(x − ak+1),
since x − ak+1 ≤ σ(k). □

We are now ready to deﬁne increasing integer sequences permitting to obtain
any possible value as a sum of elements in the sequence.

Deﬁnition 4. An iis is a complete sequence if and only if ai+1 ≤ σ(i)+ 1, 0 ≤
i< r,where σ(i):= )i
j=0 aj.

The name complete has been chosen after [8], where this name is used with
the same meaning but for inﬁnite sequences. Other encountered names were at
least practical and regular.The term practical was suggested by practical num-
bers, which, after Deﬁnition 4, can be deﬁned simply as those numbers whose
sequence of divisors, when written as an iis, is complete. The inﬁnite sequence
of practical numbers has recently been proved to possess Goldbach property [14]!
Regular sequences are nondecreasing sequences introduced by Fishburn et al. [9]:
they satisfy conditions similar to those in Deﬁnition 4 and are shown to ensure
uniqueness of solutions for ﬁnite measurement structures.
Let us now deﬁne sequences satisfying the necessary condition ai+1 ≤ 2ai for a
sequence to be Goldbach, and then examples and comparisons will be made.

Deﬁnition 5. An iis is a tournament if and only if ai+1 ≤ 2ai, 0 ≤ i< r.

INCREASING INTEGER SEQUENCES AND GOLDBACH’S CONJECTURE 111

Tournaments [1] have been called so because ai can be considered as the number
of players in a knock-out tournament after round i, starting from the ﬁnal round as
round 0, if in each round at least one and at most half of the players are knocked
out. It is immediate to show that tournaments, according to Deﬁnition 5, are
complete sequences.

Example 2. There are 9 subexponential sequences or full sets of length three:
1234, 1235, 1236, 1237, 1 238, 1 245, 1 2 4 6, 124 7, 1248 (remember
that the number of elements in the sequence is one more than the length, since the
sequence starts with a0). Of the 9 sequences above, 1238 is the only one which
is not complete: it is also not a tournament, the only other non-tournament being
123 7.

Let us now consider the Gilbreath sequence in the ﬁrst row of Figure 1c,
12351022 49: sinceits last element, 49, is bigger thanthe sum of all the
preceding elements plus 1, then that sequence is not complete. We shall not con-
sider Gilbreath sequences any more, but would like instead to brieﬂy introduce a
subclass of complete sequences which neither contains nor is contained in the class
of tournaments.
Consider a simple graph with m edges having weights 1 2 3... m:which in-
creasing integer sequences may represent the sequence of weights of a Minimum
Spanning Forest (MSF ) of the graph? Edges with weights 1 and 2 can always
be chosen, but the edge of weight 3 (let us say “edge 3” for short) might close a
circuit with edges 1 and 2: in any case, either edge 3 or edge 4 (or both) will be
chosen. Which is the worst case, the one with maximum weights? Suppose that
i edges have been chosen (perhaps by a greedy algorithm), then they can make a
tree with i + 1 nodes and the worst case is that of a complete graph with (
i+1
2 )

edges. Then we are led to the following deﬁnition for MSF sequences.

Deﬁnition 6. An iis is a MSF sequence if and only if ai ≤ (
i+1
2 ) +1, 1 ≤ i ≤ r.

An interesting consequence of the deﬁnition is that we have a polynomially in-
creasing limit sequence for this class: in fact, the sequence with maximal elements
is 124 711162229... (r2 + r +2)/2, which is the sequence of central polygo-
nal numbers (sequence A000124 in [20]). Since 1 plus the sum of elements of the
smallest sequence 1 2 3... i exactly equals the maximum value for ai,then any
MSFsequenceis complete; however, MSFsequence1237is surely not atourna-
ment, while 1248is a tournament and not an MSF. However, MSFsequences
(properly) include all Goldbach sequences: we shall prove in Section 4 that, in a
Goldbach sequence, ar cannot exceed the corresponding central polygonal number
(r2 + r +2)/2. We shall now abandon MSF sequences to explore only subsets of
tournaments, starting with sub-Fibonacci sequences.

Deﬁnition 7. An iis is a sub-Fibonacci sequence if and only if ai ≤ ai−1 +ai−2 +1,
2 ≤ i ≤ r; a1 =2.

The original deﬁnition in [9] referred to nondecreasing sequences and did not
add 1 on the right hand side. It turns out that there is an immediate bijection

112 M. TORELLI

Figure 2. Integer sequences corresponding to 3-permutations.

between sequences “with the addition of 1” and those without, but with one more
element. Although less elegant, Deﬁnition 7 permits to include sequences with
a2 = 4, which would otherwise be excluded, therefore designing a much richer
class of sequences. In particular, as will be seen later on, this class properly
includes permutations. The limit sequence 1 2 4 7 12 20... is given by Fibonacci
numbers decreased by 1. The condition for tournaments is obviously satisﬁed, but
1 2 3 6 11, for instance, is both a tournament and an MSF, but it is not sub-
Fibonacci. More interestingly, it may not be obvious that a Goldbach sequence
must be sub-Fibonacci: suppose ai >ai−1 + ai−2 + 1, then, which elements will
generate x = ai−1 + ai−2 + 1? The only possibility is x = ai−1 + ai−2 +1 = 2ai−1,
but now ai > 2ai−1.
Another surprise may be to ﬁnd permutations among these classes: I cannot
quote any paper where permutations are represented as increasing sequences. How-
ever, one of the referees pointed out the connection between arrangements of lines
and permutations, as described e.g. in Chapter 2 of [7]. My approach was to start
from the already mentioned sequence of central polygonal numbers: they count the
maximum number of pieces that can be obtained by slicing a pancake with n cuts
(see Fig. M1041 in [21]). Orderly numbering the cuts on one half of the pancake,
then, on the other half, a permutation will be obtained, the sequence being given
by the record of the number of pieces (not necessarily maximum) obtained after
each cut. See Figure 2.
In the iis of a permutation, ai is the number of pieces obtained after the i-
th cut, and this is given by ai−1 + 1 + (the number of inversions generated by
element i in the permutation = the number of crossing points on line i). The
number of inversions is the number of elements smaller than i which follow i in
the permutation: since element i cannot be followed by more than i − 1 smaller
elements, we are led to the following deﬁnition.

Deﬁnition 8. An iis is a permutation if and only if ai ≤ ai−1 + i,1 ≤ i ≤ r.

The table enumerating permutations according to the number of inversions (see
[11] Vol. 3, Tab. 1 in Sect. 5.1.1), quite similar to that enumerating tournaments
(see next section), has been illuminating in discovering how to represent permuta-
tions as a subclass of tournaments. In fact, permutations are sub-Fibonacci,since
i ≤ ai−2 + 1; on the other hand, 1 2 4 5 10 is sub-Fibonacci and Goldbach, but is
not a permutation, while 1 2 4 7 is a non-Goldbach permutation.

INCREASING INTEGER SEQUENCES AND GOLDBACH’S CONJECTURE 113

All the deﬁnitions in this section have involved inequalities: it is time to deﬁne
some more sequences through equalities, as we did for Goldbach sequences, where
we asked for any x to be the sum of two elements in the sequence, were x in the
sequence or not. By asking x to be the sum of two elements only if x itself is
in the sequence, we obtain the well-studied class of (ascending) addition chains.
Our notation for increasing integer sequences was chosen to conform to that for
addition chains in [11] (Vol. 2), which is, besides, almost universally adopted.

Deﬁnition 9. An iis is an addition chain if and only if ai = ak + aj for some j, k
with 0 ≤ j ≤ k< i and each 1 ≤ i ≤ r.A star chain is an addition chain with
k = i − 1for each i.

12458 is anon-star chain, while 12 48isa star chain, showingthatweare
outside the class of sub-Fibonacci and permutation sequences, although Goldbach
sequences are obviously contained in the class of addition chains, but not in that
of star chains: 12458is Goldbach!
The last class we are going to introduce will be contained in all the classes we
have deﬁned (with the exception of Collatz sequences, which are, on the contrary,
contained in it). In particular, we want these sequences to be Goldbach. To get
to this point it is better to introduce a characterization of Goldbach sequences,
having maximum n, through binary sequences b1,b2, ..., bn with bi =1 if there is
a j such that i = aj, 0 otherwise. Consider now a preﬁx b1,b2, ..., bk of the binary
sequence: if the convolution b1bk +b2bk−1 +...+bkb1 is greater than 0, then there is
a bibk−i+1 = 1, meaning that i = aj, k − i +1 = am, and therefore aj + am = k +1.
If the convolution is positive for each k between 1 and n − 1, then the sequence is
Goldbach! Suppose that, for each k, b1 + b2 + ... + bk >k/2, i.e. there are more
1’s than 0’s: then the convolution must be positive, and the sequence is Goldbach.
Now, consider the iis a0,a1, ..., ai and the corresponding binary sequence of length
ai − 1: this sequence has exactly i ones, and we want the number of zeros to be
strictly less, at most i − 1, therefore ai − 1 ≤ i + i − 1or ai ≤ 2i. We need a
name for these sequences: since they are enumerated (according to the maximum
value in the sequence) by central binomial coeﬃcients (see next section) the name
of binomial sequences seems to be apt.

Deﬁnition 10. An iis is a binomial sequence if and only if ai ≤ 2i,1 ≤ i ≤ r.

Having deﬁned, at last, all the classes of increasing integer sequences we need,
we can aﬀord a digression on prime numbers and primoids. First of all, it is easy
to see that the sequence of primoids (deﬁned after Ex. 1) is not a star chain:since
4 is not in the sequence, any gap of 4 in the sequence will yield a counterexample,
the ﬁrst such gap occurring between 44 and 48. Element 48 is a23 in the sequence,
thus showing also that the sequence of primoids is (obviously!) not binomial. We
can state at least one simple theorem concerning primoids, Theorem 2 below.
Let us call sub-permutation a permutation such that ai ≤ ai−1+⌈i/2⌉, 1 ≤ i ≤ r.
Thereare only 4sub-permutations of length 4: 12345, 1 2 346, 12356and
12357, and in general ai has ⌈i/2⌉ possible values for 1 ≤ i ≤ r, so that the
number of sub-permutations of length r is given by sequence A010551 in [20].

114 M. TORELLI

Figure 3. A Venn diagram showing the inclusions of the families
of sequences.

Theorem 2. Any preﬁx of the sequence of primoids is a sub-permutation.

Proof. Let pn be the nth prime. We ﬁrst have to prove that pn+1 ≤ pn + n,
a result not diﬃcult to obtain, although not mentioned in any of the books on
number theory I consulted. P. Dusart [6] proved that pn ≥ n(ln n +ln ln n − 1)
for n ≥ 2and pn ≤ n(ln n +ln ln n − 0.9484) for n ≥ 39017. Observing that
ln(n +1) = ln(n(1 + 1/n)) < ln n +1/n, it is easy to write the upper bound for
pn+1, isolate in it the term n(ln n +ln ln n − 1) and substitute back pn, obtaining
pn+1 ≤ pn + n, or even a slightly better inequality, valid for n ≥ 39017. A program
check shows that pn+1 ≤ pn + n is actually true for any n ≥ 1.
Now we simply have to apply the inequality to primoids: since 3 = p2 =2a0 +1,
we have pn =2an−2 +1, from which an ≤ an−1 + ⌈n/2⌉ follows immediately. □

The largest gap between consecutive primes or primoids increases, as a mat-
ter of fact, much more slowly than predicted by the theorem, and, for example,
a94906079599 − a94906079598 = 326 is the maximal gap thus far! Moreover, it seems
that 6 is the only even number requiring doubling of an odd prime to obtain. If we
call elementary, following Fishburn’s terminology, the addition chains or Goldbach
sequences in which doubling is forbidden (except trivially to obtain 2), then we
could perhaps modify Goldbach’s conjecture stating that the sequence of primoids
is an elementary Goldbach sequence.

3. Enumeration

There are at least two ways of enumerating increasing integer sequences s:
according to the value n of max(s) or according to the length l(s)= r. When talking
about “sequences” there is the possibility of some confusion between increasing
integer sequences, which are the objects to be counted, and their counting sequence,
which is the sequence giving their numbers as functions of r or n. We shall use
the term “counting sequence” to avoid this confusion.
A ﬁrst, very simple, result is that the number of increasing integer sequences s
such that max(s)= n is 2n−2:in fact, n − 2 integers may appear (or not) between

INCREASING INTEGER SEQUENCES AND GOLDBACH’S CONJECTURE 115

a0 =1and ar = n. Full sets are counted according to number of elements (or
corresponding subexponential sequences according to length) by sequence A001192
in [20]: 12988 1802... Counting by maximum is not there, but we can adapt a
formula in [2] to count the number of sequences satisfying any inequality whose
right hand side increases only as a function of index i. While the formula is valid
only for these classes, the recurrence relation is valid, with slight modiﬁcations,
even for some sequences satisfying an inequality in which the bound is a function
of ai as well as of index i. Let us derive the recurrence equation ﬁrst.
Let a class of increasing integer sequences be deﬁned by ai ≤ f (i), where f
is an integer-valued function such that f (i) >f (i − 1) ≥ i ≥ 1. Denoting with
S(r, n) the number of sequences of length r and maximum n, we can easily deduce
recurrence relations, the boundary conditions being S(r, n)=0 if r ≥ n or n>
f (r), S(n − 1,n) = 1. Since from a0,a1, ..., ar−1 we can obtain a sequence of
length r by adding ar = n if and only if ar−1 <n ≤ f (r), the recurrence relation
is the following:
 S(r, n)=
 n−1∑

j=r S(r − 1,j)for 0 <r < n ≤ f (r). (1)

We are interested in the counting sequence according to length r: S(r, ∗):=
)f (r)
n=r+1 S(r, n) and the counting sequence according to maximum element n:
S(∗,n):= )n−1
r=0 S(r, n).

Theorem 3. S(∗,n +1) = 2S(∗,n) − δn,f (r)S(r − 1, ∗).

Proof. Kronecker function δn,f (r) is 1 if f (r)= n,0 otherwise. Let a0,a1, ..., ar−1,n
be an iis with maximum n and length r. From it, we can obtain two sequences
with maximum n +1: a0,a1, ..., ar−1,n,n +1 and a0,a1, ..., ar−1,n + 1. While
the former can always be obtained, the latter is only possible if n +1 ≤ f (r). In
case n = f (r), all sequences a0,a1, ..., ar−1,n must be subtracted, and there are
S(r − 1, ∗)of them. □

Theorem 3 shows that S(∗,n +1) ≤ 2S(∗,n) and permits to derive S(∗,n)once
S(r, ∗) is known. For instance, there are 3 full sets with maximum 5: S(∗, 5) = 3,
f (i)=2i, therefore we can double up to n =8: S(∗, 8) = 24, then S(∗, 9) =
48 − S(2, ∗) = 46, then keep on doubling up to 16... But Theorem 3 also permits
to deduce, vice versa, S(r, ∗)from S(∗,n), since, by inversion when f (r +1) = n,
we have S(r, ∗)=2 S(∗,f (r +1)) − S(∗,f (r + 1) + 1)). However, what can be done
if we do not have either sequence? Then, to ﬁnd S(r, ∗), we can use the following
theorem.

Theorem 4.

S(r, ∗)=
 r−1∑

k=0(−1)
k(
f (r − k) − (r − k)
k +1
 )
S(r − k − 1, ∗).

116 M. TORELLI

Table 1. Values of T (r, n)and T (r)= T (r, ∗), 1 ≤ r ≤ 5, n =
k + r,1 ≤ k ≤ 27

k
r 123456 78910 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 T(r)

1 1 1

2 11 2

3 12211 7

4 13566 6 44 22 11 41

5 14915 21 26 30 31 33 30 31 26 26 20 20 14 14 10 10 664 4221 1 397

Proof. By adapting Theorem 1 in [2] to increasing integer sequences. □

Unfortunately, no similar theorems seem to be available when ai satisﬁes in-
equalities involving elements of the sequence. However, these formulae solve the
enumeration problem for full sets, MSF and binomial sequences. We still have
to justify the name of binomial sequences: remember that binomial sequences
are represented by binary vectors whose preﬁxes always have more ones than ze-
ros. These sequences can be interpreted as paths in constrained regions of the
plane, and a little experimenting will convince that the number of sequences with
maximum n is the central binomial coeﬃcient ( n−2
⌊(n−2)/2⌋
), proofs being similar to
classical proofs for Catalan numbers. The corresponding enumeration by number
of ones (which is the length of the iis) yields in fact Catalan numbers 1
r+1 (
2r
r )
.
Tournaments are enumerated according to maximum element as sequence
A002083 in [20]: 1 23611224284165 ... andasimple recurrence formula
is given there (cf. also [4] and [16]). To enumerate tournaments according to
length, let T (r, n) be the number of tournaments t with l(t)= r and max(t)= n.
Recurrence (1) is still valid, provided the start value r in the summation is replaced
by ⌈n/2⌉, since tournaments with one more element, of value n, can be obtained
by sequences ending with an element at least n/2. A few values of T (r, n)are tab-
ulated in Table 1; columns are labeled by values of k to obtain n = k + r,so that
the table can be contained in the page and resemble Knuth’s table quoted after
Deﬁnition 8. The last column reports values of T (r), the number of tournaments
of length r, irrespective of n. The sequence of values of T (r) is now sequence
A008934 in [20].
The enumeration of sub-Fibonacci sequences also requires a two-variable recur-
rence, which is as simple as that for tournaments. Consider a sequence ending with
the two elements j and m,and let F (j, m) denote the number of sub-Fibonacci
sequences of this sort. From each such sequence we can generate j +1 new se-
quences by appending m +1, or m + 2, ..., or m + j + 1. Therefore, we obtain
the recurrence relation F (m, n)= )m−1
j=n−m−1 F (j, m)since n ≤ m + j +1 yields
j ≥ n − m − 1. The boundary conditions can be expressed as F (m, n)= 0if m ≥ n
or m< n/2, F (1, 2) = F (2, 3) = F (2, 4) = 1. The counting sequence for F (∗,n),
the number of sequences ending with n, begins 1 1 1 2 3 6 11 21 41 81 159 316.
The counting sequence according to length is sequence A005270 in [20].

INCREASING INTEGER SEQUENCES AND GOLDBACH’S CONJECTURE 117

Permutations are obviously very easy to count according to length, since there
are r! of them. Just a bit more surprising is the fact that also star chains are r!:
from a chain of length r − 1it ispossibletoobtain r star chains of length r by
successively adding ar−1 to a0,a1, ..., ar−1, and there is just 1 star chain of length 1.
It is also possible to exhibit an explicit bijection between the two classes. Consider
the class of integer functions f such that 0 ≤ f (i) <i for each i with 2 ≤ i ≤ r.We
do not require f to be increasing nor even monotone. There are r! such functions,
since there are i independent choices for each f (i). Now we can use f in at least
two ways to obtain increasing sequences: elements a0 =1 and a1 =2 of the
sequence are ﬁxed, while for 2 ≤ i ≤ r
1) ai = ai−1 + af (i): we obtain a star chain, by Deﬁnition 9, one for each f ;
2) ai = ai−1 + f (i) + 1: we obtain a permutation, by Deﬁnition 8, since
f (i)+ 1 ≤ i.
The recurrence equation for P (r, n), the number of permutations of length r and
maximum n, is given by (1), starting the summation from the maximum between
n − r and r,since n − r is the minimum value that the element preceding n in the
sequence can have, provided it is greater than r − 1. The counting sequence starts
111 236112141 80157 310 (sequence A008930 in [20]).
Things are still not too diﬃcult for complete sequences, despite the apparently
complicate inequality in the deﬁnition. We only need a recurrence in three vari-
ables: denoting by C(r, n, s) the number of complete sequences of length r,max-
imum n and sum σ(r)= s, any such sequence can be obtained by a sequence of
length r−1, maximum x and sum s−n by simply appending n,provided x is smaller
than n and also not greater than s − n. Therefore, setting y := min(n − 1,s − n),
the required recurrence is

C(r, n, s)=
 y∑

x=r C(r − 1,x,s − n).

The counting sequences are

C(r, ∗, ∗) = 12860814 19682 845368 ...

C(∗,n, ∗) = 1 1123612234590 180 359 ...
Well, what about addition chains and Goldbach sequences? I wrote some pro-
grams to compute them, by explicitly generating and then counting, but recur-
rence formulae have eluded me up to now. We will see some motivations for this
unsatisfactory situation in the next section. However, having found that binomial
sequences are common to all classes helps to speed up testing, while, on the other
hand, upper bounds for Goldbach sequences (see next section) allow to eliminate
elements too big. We can display two comparative tables: Table 2 lists increasing
integer sequences of diﬀerent types, enumerated according to maximum element,
while Table 3 lists them according to length.
Table 3 is quite misleading if used to compare diﬀerent sequences, since the
maximum element of a binomial sequence of length 8 can be at most 16, while

118 M. TORELLI

Table 2. Increasing integer sequences of diﬀerent types enumer-
ated according to maximum element. The ﬁrst six values are
common to all sequences: 1 1 1 2 3 6.

Max ∗Chains Binomial Goldbach Chains Perms Tournaments
7 10 10 10 10 11 11
8 20 20 20 21 21 22
9 36 35 37 38 41 42
10 70 70 73 77 80 84
11 130 126 139 144 157 165
12 252 252 275 293 310 330
13 475 462 533 563 614 654
14 916 924 1059 1131 1218 1308
15 1745 1716 2075 2205 2421 2605
16 3362 3432 4126 4434 4819 5210
17 6438 6435 8134 8711 9602 10398
18 12410 12870 16194 17466 19147 20796
19 23852 24310 32058 34506 38204 41550
20 46020 48620 63910 69169 76266 83100

Table 3. Increasing integer sequences of diﬀerent types enumer-
ated according to length. The ﬁrst two values are common to all
sequences: 1 2.

Length Binomial Goldbach Perms &∗ Chains Tournam. Full Sets
3 55 6 6 7 9
4 14 17 24 25 41 88
5 42 65 120 135 397 1802
6 132 292 720 913 6377 75598
7 429 1434 5040 7499 171886 6421599
8 1430 7875 40320 73191 7892642 1097780312

in a chain, tournament or full set it can be as big as 256. On the other hand,
it is rather surprising to discover, in Table 2, that star chains are asymptotically
less than binomial sequences, when enumerated according to maximum element,
whereas permutations are not much less than tournaments.
How much less than tournaments are Goldbach sequences? We only know at
present that Goldbach sequences are asymptotically more than binomial sequences,
and central binomial coeﬃcients grow slower than 2
n/√
n.Since the number of
tournaments grows faster than 2n−4, the ratio Goldbach/tournaments might ap-
proach 0 as n tends to inﬁnity, meaning in a sense that an inﬁnite tournament
cannot be Goldbach by chance. We can, however, exhibit Goldbach sequences
much shorter than the primoids, and establish a lower bound on the length of
Goldbach sequences with maximum n, which will be done in the next section.

INCREASING INTEGER SEQUENCES AND GOLDBACH’S CONJECTURE 119

4. Looking for shortest sequences

Let us consider a Goldbach sequence a0,a1, ..., ar: we can take (unordered)
pairs of elements in (
r+1
2 ) ways, but, to obtain an x between 2 and ar as sum of
one or more pairs, we do not need ar: however, we can use ar merely to represent
doubling of the other element in the pair. Since we have to obtain all the ar − 1
values x between 2 and ar, even if all the pairs yield distinct sums, ar cannot
exceed (r+1
2 ) +1 = r2+r+2
2 ,the central polygonal numbers. After inverting the
inequality we can state the following theorem.

Theorem 5. In a Goldbach sequence s with l(s)= r and max(s)= n the following
inequalities must hold:
 r ≥ √
8n − 7 − 1
2 ,n ≤ r2 + r +2
2 ·

Unfortunately, these inequalities only yield the order of magnitude, but are not
strict and in fact grossly overestimate the strict bounds: for instance, the maxi-
mum element for Goldbach sequences of length 9 is 34 and not 46 as given by the
theorem. Looking at computer-generated tables for the sequences reaching max-
ima, we were struck by the symmetries of the sequences up to length 9. Highly
symmetric sequences attain a bound for n of

n = r2 +6r + m(2 − m)
4 , where m = r mod4. (2)

In fact, for each r =4d + m,where d = ⌊r/4⌋,we can set k =(2d + m)(d +1)
and construct the following sequence: 1, 2, 3, ..., d+1, 2(d+1), 3(d+1), ..., k, k+1,
k+2, ..., k+d,2(k+d). Then n = ar =2(k + d) is given exactly by Equation (2),
while the number of elements in the sequence is d+(2d+m)+(d+1) = 4d+m+1 =
r+1, therefore the length is r.An example will both make things clear and convince
that such a sequence is Goldbach. For r =9 we have d =2, m =1 and k = 15:
the sequenceis1236912 15 1617 34. There is nodoubt that values up to 17
can be obtained, since gaps do not exceed 3, and 1 2 3 are in the sequence: but the
sequence, excluding ar,is symmetric (ai+ar−i−1 = ar−1+a0), and so if ai+aj = x,
then ar−j−1 + ar−i−1 = ar−j−1 + ar−i−1 + ai + aj − (ai + aj)= 2ar−1 +2 − x:all
values up to 2ar−1 are obtained as well.
The sequence of maximum values for n, according toEquation (2), is 1 24610
14 18 22 28 34 40 ... Unfortunately, (2) is not an upper bound for lengths greater
than 9: for r =10the sequence 12 4510121718 202142attainsthe maximum,
but 42 > 40.
However, needing a sequence for 30, say, we know that a sequence of length 8 will
not suﬃce, while we can use the sequence for 34 substituting 30 to 34. The biggest
the number, the longest the sequence... Actually, the requirement of obtaining all
values x, speciﬁc to Goldbach sequences, has been the key to Theorem 5 and
Equation (2). For addition chains, however, this requirement is absent and “no

120 M. TORELLI

conjecture about addition chains is safe!”, as Knuth writes. In particular, the
length of the shortest chain, not being monotone, strongly depends on the value of
n. Were it possible to ﬁnd the counting function S(r, n) for addition chains, or even
some recurrence relation, then we would know (in principle) the shortest length a
chain for n can have, thus perhaps solving both the Scholz-Brauer conjecture and
several other problems of practical as well as theoretical interest.

5. Conclusions

We have rather few conclusions and a lot of open questions, or work to do. We
hope to have succeeded in showing that the subject is worth some more study,
so to have a commencement, not a conclusion. At least, we would like to obtain
some more recurrences or closed-form formulae for the sequences just deﬁned, in
particular Goldbach sequences and addition chains, so to have information on the
asymptotic behavior of their number. This is almost all we can say at present
about a hypothetical contribution of this approach to the conjectures themselves
which originated it.
Other conjectures in number theory might be explored by examining the set
of sequences having the conjectured property; moreover, all the work concerning
Gilbreath’s conjecture and the 3x + 1 problem is still to be done.
Diﬀerent structures, such as Davenport-Schinzel sequences (E20 in[10]), might
also be connected some way with increasing integer sequences. Moreover, a few
known counting sequences are also interestingly “similar” to some counting se-
quences of ours, suggesting they might count “similar” objects: e.g. sequence
A001258 in [20], concerning labeled trees with unlabeled end-points, is the same
as the sequence of chains up to length 5, and then smaller; sequence A005130,
counting alternating sign matrices [18], is 1 2 7 42 429 ..., just over tournaments...
All these may well be worth exploring.

Acknowledgements. The author thanks N.J.A. Sloane for kindly sending some papers
and for the invaluable On-Line Encyclopedia of Integer Sequences [20]; O.M. D’Antona,
P. Massazza, C. Mereghetti, E. Neuwirth and R. Principato for help and discussion,
the anonymous referees for useful suggestions, and A. Bertoni for introducing him to
combinatorics and teaching most of what he knows about.

References

[1] P. Capell and T.V. Narayana, On Knock-out Tournaments. Canad. Math. Bull. 13 (1970)
105–109.
[2] L. Carlitz, D.P. Roselle and R.A. Scoville, Some Remarks on Ballot-Type Sequences of
Positive Integers. J. Combinatorial Theory, Ser. A 11 (1971) 258–271.
[3] L. Comtet, Advanced Combinatorics. Reidel, Dordrecht (1974).
[4] M. Cook and M. Kleber, Tournament sequences and Meeussen sequences. Electron. J. Com-
bin. 7 (2000), Research Paper 44, p. 16 (electronic).

INCREASING INTEGER SEQUENCES AND GOLDBACH’S CONJECTURE 121

[5] J-M. Deshouillers, H.J.J. te Riele and Y. Saouter, New experimental results concerning the
Goldbach conjecture, in Proc. 3rd Int. Symp. on Algorithmic Number Theory. Lect. Notes
Comput. Sci. 1423 (1998) 204–215.
[6] P. Dusart, The kth prime is greater than k(ln k +ln ln k − 1) for k ≥ 2. Math. Comp. 68
(1999) 411–415.
[7] H. Edelsbrunner, Algorithms in Combinatorial Geometry. Springer, Berlin (1987).
[8] P. Erd¨os and M. Lewin, d-Complete Sequences of Integers. Math. Comp. 65 (1996) 837–840.
[9] P.C. Fishburn and F.S. Roberts, Uniqueness in ﬁnite measurement, in Applications of Com-
binatorics and Graph Theory to the Biological and Social Sciences,edited by F.S.Roberts.
Springer, New York (1989) 103–137.
[10] R.K. Guy, Unsolved Problems in Number Theory. Springer, New York, 2nd ed. (1994).
[11] D.E. Knuth, The Art of Computer Programming, Vols. 2 and 3. Addison-Wesley, Reading
(1997 and 1998).
[12] J.C. Lagarias, The 3x + 1 problem and its generalizations. American Math. Monthly 92
(1985) 3–23.
[13] W.J. LeVeque, Fundamentals of Number Theory. Addison-Wesley, Reading (1977).
[14] G. Melﬁ, On Two Conjectures about Practical Numbers. J. Number Theory 56 (1996)
205–210.
[15] M.B. Nathanson, Additive Number Theory. Springer, New York (1996).
[16] E. Neuwirth, Computing Tournament Sequence Numbers eﬃciently with Matrix Techniques.
S·em. Lothar. Combin. 47 (2002), Article B47h, p. 12 (electronic).
[17] A.M. Odlyzko, Iterated Absolute Values of Diﬀerences of Consecutive Primes. Math. Comp.
61 (1993) 373–380.
[18] D.P. Robbins, The Story of 1, 2, 7, 42, 429, 7436, ... Math. Intellig. 13 (1991) 12–19.
[19] J. Richstein, Verifying the Goldbach Conjecture up to 4 × 1014. Math. Comp. 70 (2001)
1745–1749.
[20] N.J.A. Sloane, The On-Line Encyclopedia of Integer Sequences. World-Wide Web URL
http://www.research.att.com/~njas/sequences/
[21] N.J.A. Sloane and S. Plouﬀe, The Encyclopedia of Integer Sequences. Academic Press,
New York (1995).
