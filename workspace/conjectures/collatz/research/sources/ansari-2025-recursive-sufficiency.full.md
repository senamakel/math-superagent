<!-- source: https://nntdm.net/papers/nntdm-31/NNTDM-31-3-471-480.pdf | converted from PDF -->

Notes on Number Theory and Discrete Mathematics
Print ISSN 1310–5132, Online ISSN 2367–8275
2025, Volume 31, Number 3, 471–480
DOI: 10.7546/nntdm.2025.31.3.471-480

Recursive sufficiency for the Collatz conjecture
and computational verification

Mohammad Ansari

Department of Mathematics, Azad University of Gachsaran
Gachsaran, Iran
e-mail: mo.ansari@iau.ac.ir

Received: 13 December 2024 Revised: 24 July 2025
Accepted: 28 July 2025 Online First: 4 August 2025

Abstract: We define the notion of recursive sufficiency for the Collatz conjecture and we use
it to present some results concerning the computational verification of the conjecture. For any
integer N ≥ 1 and any recursively sufficient set F , it is proved that all integers in the interval
[1, N ] satisfy the conjecture if and only if F ∩ [1, N ] satisfies the conjecture. We offer a sequence
of sieves for which the corresponding sequence of elimination percentages tends to 100%, and as
a result, for any integer P arbitrarily close to 100, we give a sieve whose elimination percentage
is at least P %. Also, we prove that if N = 2(3
n) + 1 is the largest known integer for which all
integers 1, 2, . . . , N satisfy the conjecture, then all integers N + 1, N + 2, . . . , 2N will satisfy the
conjecture as well, and hence, they can be eliminated from the verification process.
Keywords: Collatz conjecture, Recursive sufficiency, Computational verification.
2020 Mathematics Subject Classification: 11A99, 11Y55.

1 Introduction

The Collatz conjecture, also known as the 3x + 1 problem, is one of the most famous open
problems in mathematics which says that repeating two simple arithmetic operations will eventually
transform every positive integer into 1. More precisely, if N is the set of all positive integers, then
the Collatz conjecture can be formulated as follows: If C : N → N is the map defined by

Copyright © 2025 by the Author. This is an Open Access paper distributed under the
terms and conditions of the Creative Commons Attribution 4.0 International License
(CC BY 4.0). https://creativecommons.org/licenses/by/4.0/

C(n) =
 


3n + 1 for odd n,

n/2 for even n,

then there is some k ∈ N such that C k(n) = 1. For example, let us try the integers 1, 3 and 14:

• 1 : 1, 4, 2, 1.

• 3 : 3, 10, 5, 16, 8, 4, 2, 1.

• 14 : 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1.

While computational verification has shown that the conjecture holds true for all positive integers
up to 1.5×2
70 [2], no mathematical proof has been offered. We refer the reader to [1,4–6] for more
information on the studies done on the problem. The problem is named after the mathematician
Lothar Collatz, who introduced the idea in 1937.
Since C(n) is even for any odd integer n, the problem is often reformulated by using the map
T on N defined by
 T (n) =
 


(3n + 1)/2 for odd n,

n/2 for even n.

Then the conjecture says that, for each n ∈ N, there is some k ∈ N such that T k(n) = 1.
For a pair of positive integers n, m, we say that n merges with m and we write n ↔ m,
whenever there are some i, j ≥ 0 for which T i(n) = T j(m) (note that T 0(p) = p for all p ∈ N).
It is clear that if n ↔ m then n satisfies the conjecture if and only if m satisfies it.
In [7], the authors show that, for all pairs of integers B > 0, A ≥ 0, the set BN0 + A is
sufficient for the Collatz conjecture, where N0 = N ∪ {0}, that is, for any n ∈ N, there is some
m ∈ BN0 + A such that n merges with m. We believe that we had better call this property the
merge sufficiency and offer the notion of sufficiency in another way. We bring the two notions
in the following definition. Note that, when we say a subset E of N satisfies the conjecture, we
mean that all members of E satisfy it.

Definition 1.1. A nonempty subset E of N is called sufficient for the Collatz conjecture provided
that, E satisfies the conjecture if and only if the conjecture is true. A nonempty set E is called
merge sufficient whenever, for any n ∈ N, there is some m ∈ E such that n merges with m
(n ↔ m).

It is clear that merge sufficiency implies sufficiency, but we will see later that the converse is
true if and only if the conjecture is true.
In the computational verification of the Collatz conjecture, the relevant algorithms do not
need to check all integers, for example, since the conjecture is true if and only if it is true for all
odd integers, it is not necessary to consider even integers as starting values (input integers which
should be checked). Thus 50% of all integers are eliminated from the verification process. As
another instance, since for any n ∈ N0, we have that 2n + 1 ↔ 3n + 2 (T (2n + 1) = 3n + 2),
the algorithms can skip all integers of the form 3n + 2 and only evaluate all odd integers having
the forms 3n or 3n + 1, that is all integers of the forms 6n + 3 and 6n + 1. Hence, for any block
472

of 6 consecutive integers, it suffices to evaluate only 2 of them. In other words, we can eliminate
at least 66.6% of all starting values (the exact percentage is 4
6 × 100). Thus the notion of a sieve
which is used in computational verification of the conjecture, is in fact a synonym for the notion of
a sufficient set for the conjecture. It may come together with the notion of elimination percentage
which is defined as follows.

Definition 1.2. Let S be a sieve for the Collatz conjecture. If there are positive integers m, n
such that, for any block of n consecutive integers, exactly m of them should be checked (or
equivalently, n − m of them could be eliminated), we say that the elimination percentage of S is
ep(S) = 100( n−m
n )%.

In this article, we define the notion of recursive sufficiency for the Collatz conjecture and use
it to offer a sequence of sieves for which the corresponding sequence of elimination percentages
tends to 100%. Thus, for any integer P arbitrarily close to 100, we can offer a sieve whose
elimination percentage is at least P %.

Definition 1.3. A positive integer n > 1 is said to be recursive if there is some positive integer
m < n such that m ↔ n. A subset R of N is called recursive whenever n is recursive for every
1 < n ∈ R. Finally, a proper subset F of N is said to be recursively sufficient if N\F is recursive.

Example 1.1. It is easily seen that the sufficient set F = 2N0 + 1 is in fact recursively sufficient.
Indeed, if 1 < n /∈ F and we take m = n
2 , then it is clear that m < n and m ↔ n. As another
sample, we show that F0 = 4N0 +3 is recursively sufficient. Suppose 1 < n /∈ F . If n is even then
it merges with m = n
2 < n. If n is odd then n = 4k + 1 for some k ≥ 0. Then, for m = 3k + 1,
we have that m < n and m ↔ n (T 2(n) = m).

We see that the recursive sufficiency of the sufficient set F = 2N is equivalent to the truth of
the Collatz conjecture.

Proposition 1.1. The sufficient set F = 2N is recursively sufficient if and only if the Collatz
conjecture is true.

Proof. Assume that the Collatz conjecture is true, i.e., for every n ∈ N we have that n ↔ 1. Now
let n be an arbitrary integer satisfying 1 < n /∈ F . Then, by our assumption, n ↔ 1. Thus, if we
take m = 1, then m < n and m ↔ n. This shows that F is recursively sufficient.
To prove the converse, assume that F is recursively sufficient. To show that the Collatz
conjecture is true, since 2N+1 is a sufficient set, we only need to show that all integers n ∈ 2N+1
satisfy the conjecture. We use that complete mathematical induction to achieve our goal. For
n = 3 the assertion of the conjecture holds true. Suppose that 3 < n ∈ 2N + 1 and the conjecture
is true for all odd integers i satisfying 1 ≤ i < n. We show that the conjecture is true for n. Since
n /∈ F and F is recursively sufficient (by our assumption), there is some positive integer m < n
such that m ↔ n. Now, if m is odd, then m ↔ 1 by our inductive assumption, and so, n ↔ 1.
Otherwise, there is an integer s ≥ 1 and an odd integer p ≥ 1 such that m = 2
sp. But then p < n
and since p ↔ m, we have that p ↔ n. On the other hand, p ↔ 1 by our inductive assumption,
and hence, n ↔ 1.
 473

It is natural to talk about the relationship between the properties of sufficiency and recursive
sufficiency.

Proposition 1.2. Every nonempty recursively sufficient set is sufficient. The converse is true if
and only if the Collatz conjecture is true.

Proof. Suppose F ⊊ N is recursively sufficient. To show that F is sufficient, assume that all
members of F satisfy the Collatz conjecture. We need to prove that all positive integers satisfy
the conjecture. We use the complete mathematical induction to prove this assertion. It is clear
that n = 1 satisfies the conjecture. Assume that n > 1 and for all integers 1 ≤ j < n we have
that j ↔ 1. Now we need to show that n ↔ 1. If n ∈ F then n ↔ 1 by our assumption. On the
other hand, if n ∈ N\F then, by the recursive sufficiency of F , there is some m ∈ N such that
m < n and m ↔ n. But m < n implies that m ↔ 1 by our inductive assumption, and hence, we
have that n ↔ 1.
To prove the second assertion of the proposition, first assume that the Collatz conjecture
is true. Then it is easily seen that, not only every sufficient set, but also every subset of N is
recursively sufficient. Now assume that the Collatz conjecture is not true. Then the sufficient set
2N is not recursively sufficient by Proposition 1.1, and we are done.

We need the following lemma to talk about the implication “sufficiency ⇒ merge sufficiency”.

Lemma 1.1. The intersection of any family of recursively sufficient sets is recursively sufficient.

Proof. Let J be an arbitrary index set and let {Fα : α ∈ J } be a family of recursively sufficient
sets. To show that F = ⋂
α∈J Fα is recursively sufficient, suppose that 1 < n /∈ F. Then there is
some β ∈ J such that n /∈ Fβ, and since Fβ is recursively sufficient by our assumption, there is
some m < n such that m ↔ n, and hence, F is recursively sufficient.

Proposition 1.3. Sufficiency implies merge sufficiency if and only if the conjecture is true.

Proof. If the conjecture is true then n ↔ m for any pair n, m ∈ N, and hence, every nonempty
subset of N is merge sufficient. To prove the converse, assume that sufficiency implies merge
sufficiency. Let F be the intersection of all recursively sufficient sets. Then F is recursively
sufficient by Lemma 1.1. We show that F = ∅. To get a contradiction, assume that F ̸= ∅.
Then F is sufficient by Proposition 1.2, and so, it is merge sufficient by our assumption. Hence
there is some m ∈ F such that 1 ↔ m. Now it is clear that F = F\{m} is also recursively
sufficient. But then the definition of F shows that F ⊆ F which says that m /∈ F. This
contradiction shows that we must have F = ∅.
Now we show that the Collatz conjecture is true. By the definition of recursive sufficiency we
have that N\F = N is recursive, i.e., for any 1 < n ∈ N, there is some m ∈ N such that m < n
and m ↔ n. Now, to get a contradiction, assume that the Collatz conjecture is not true and let n1
be the smallest positive integer which does not satisfy the conjecture. Then it is clear that n1 > 1,
and so, there is some m1 ∈ N such that m1 < n1 and m1 ↔ n1. But m1 satisfies the conjecture,
and hence, n1 should satisfy the conjecture as well, which is a contradiction. Therefore, the
Collatz conjecture is true.
 474

We see that, with an extra weak assumption, recursive sufficiency implies merge sufficiency.

Proposition 1.4. Let F be a recursively sufficient set. Then F is merge sufficient if and only if
there is some p ∈ F which satisfies the Collatz conjecture.

Proof. Suppose that there is some p ∈ F which satisfies the conjecture. To get a contradiction,
assume that F is not merge sufficient and let n be the smallest integer which does not merge with
any member of F . Then it is obvious that n > 1 (because 1 ↔ p), and since F is recursively
sufficient by our hypothesis, there is some m < n such that m ↔ n. But the choice of n shows
that there is some k ∈ F such that k ↔ m. Then we have that n ↔ k which is a contradiction.
Thus F must be merge sufficient.
To prove the converse, suppose that F is merge sufficient. Then any positive integer merges
with some element in F . In particular, there is some p ∈ F such that 1 ↔ p, and so, p satisfies
the conjecture.

As a direct consequence of the above proposition, we give the following corollary.

Corollary 1.1. If F is a recursively sufficient set and p ∈ N satisfies the Collatz conjecture then
F ∪ {p} is merge sufficient.

In Section 2, we prove that if F is recursively sufficient then, for any N ∈ N, the set

SN = {1, 2, 3, . . . , N }

satisfies the Collatz conjecture if and only if F ∩ SN satisfies the conjecture. In Section 3, we
offer a sequence (Fn)
∞
n=0 of recursively sufficient sets for which the corresponding sequence of
elimination percentages tends to 100%. Then we use the recursively sufficient set F = ⋂∞
n=0 Fn
to show that if N = 2(3
n) + 1 is the largest known integer for which the set SN satisfies the
conjecture, then all integers in the interval (N, 2N ] will satisfy the conjecture as well, and hence,
they can be eliminated from the verification process.

2 Recursive sufficiency and computational verification
of the conjecture

Assume that for some N ∈ N, all members of SN have successfully passed the computational
verification process of the Collatz conjecture and let F be a recursively sufficient set. If we want
to apply the verification process to all integers in the interval (N, M ], where M > N is any
integer, we claim that we only need to apply the process to all members of F ∩ (N, M ]. This
result is offered as Corollary 2.1 which is a direct consequence of the following theorem.

Theorem 2.1. Let F be a recursively sufficient set and let N ≥ 1 be any integer. Then SN satisfies
the Collatz conjecture if and only if F ∩ SN satisfies it. The assertion may not remain valid if we
replace recursive sufficiency with merge sufficiency.

475

Proof. The necessity is obvious, and so, we only prove the sufficiency. Assume that F ∩ SN
satisfies the conjecture. We prove that SN satisfies the conjecture by applying the complete
mathematical induction. We know that n = 1 satisfies the conjecture. Suppose 1 < n ∈ SN
and for all 1 ≤ j < n we have that j ↔ 1, i.e., j satisfies the conjecture. We show that n satisfies
it as well. If n ∈ F ∩ SN then n satisfies the conjecture by our assumption. If n /∈ F then, since
F is recursively sufficient, there exists some m < n such that m ↔ n. But m < n implies that
m ↔ 1 by our inductive assumption, and hence, n ↔ 1.
To prove the second assertion of the theorem, we show that if the Collatz conjecture is not
true then there is some integer N such that 2N ∩ SN satisfies the conjecture but SN does not.
To this end, assume that the Collatz conjecture is not true. Then, in view of Proposition 1.1, the
merge sufficient set 2N is not recursively sufficient. Now let n1 = min C ′, where C ′ is the set of
all positive integers which do not satisfy the conjecture. Then it is clear that n1 is an odd integer,
because otherwise, 1 ↔ n1
2 ↔ n1 which is a contradiction. Then N = n1 + 1 is even, and so,
1 ↔ N
2 ↔ N because N
2 < n1. Now it is readily seen that 2N ∩ SN satisfies the conjecture while
SN does not.

Corollary 2.1. Let F be a recursively sufficient set and let 1 < N < M be any integers. If both
sets SN and F ∩ (N, M ] satisfy the conjecture then all integers in the interval (N, M ] satisfy the
conjecture.

Proof. In view of Theorem 2.1, F ∩ SM satisfies the conjecture if and only if SM satisfies it.
But, since by our assumption, SN satisfies the conjecture, we see that F ∩ (N, M ] satisfies the
conjecture if and only if all integers in the interval (N, M ] satisfy it.

A particular case for the above corollary can be presented as follows.

Corollary 2.2. Let F be a recursively sufficient set and let 1 < N < M be any integers. If SN
satisfies the conjecture and F ∩ (N, M ] = ∅, then SM satisfies the conjecture.

Remark 2.1. It is worth mentioning that the assertion of Theorem 2.1 may not remain valid if we
replace the recursively sufficient set F with the merge sufficient set E = BN + A (B > 0, A ≥ 0)
because, in view of [7], no order-friendly argument is guaranteed in merging a given integer with
some members of E. As a result, we cannot use the mathematical induction for the set SN .

We finish this section by highlighting the fact that, in view of Corollary 2.1, if N is the largest
known integer for which SN satisfies the Collatz conjecture, F is a recursively sufficient set, and
M > N is any integer, then, to verify the conjecture for all integers in the interval (N, M ], it
suffices to apply the computational verification process only to all members of F ∩ (N, M ].

3 Making a sieve finer and finer

It is easily seen that, if F is recursively sufficient and A ⊆ F , then F1 = F \A is recursively
sufficient if and only if A is recursive. For example, for the recursively sufficient set F0 = 4N0+3,
we can write F0 = ⋃2
a0=0 (4(3N0 + a0) + 3
)
, and since A = 12N0 + 11 is a recursive subset of
F0 (8n + 7 ↔ 12n + 11), we have that the set
 476

F1 = F0\A = (12N0 + 3) ∪ (12N0 + 7) =
 1⋃

a0=0
 (4(3N0 + a0) + 3)

is recursively sufficient.
Now, it is clear that if we consider F0 and F1 ⊊ F0 as sieves for the computational verification
of the Collatz conjecture, then F1 is finer than F0, that is, ep(F1) > ep(F0). Thus we have made a
finer sieve F1 by removing the recursive subset A = 12N0 + 11 from F0. We will use this pattern
to obtain other recursively sufficient sets Fn (n ≥ 2) such that F0 ⊋ F1 ⊋ F2 ⊋ · · · . In other
words, we will repeatedly make the sieve F0 finer and finer.
Let us define Fn (n ≥ 0) as follows: F0 = 4N0 + 3 and, for n ≥ 1,

Fn =
 1⋃

a0=0 · · ·
 1⋃

an−1=0
 (
4(3
nN0) + 4(3n−1an−1) + · · · + 4a0 + 3). (1)

Then, it is obvious that F1 = (12N0 + 3) ∪ (12N0 + 7).
Note that in (1) we had better write aj,n for aj (0 ≤ j ≤ n − 1) to show the dependence of
these scalars to n in Fn, but, for simplicity in notations and since we will not face any ambiguity
in our computations, we write aj instead of aj,n.
Now we prove that F0 ⊋ F1 ⊋ F2 ⊋ · · · , and that each Fn (n ≥ 0) is a recursively sufficient
set.

Lemma 3.1. For the sets Fn (n ≥ 0) defined in (1), we have that F0 ⊋ F1 ⊋ F2 ⊋ · · · . Moreover,
each Fn (n ≥ 0) is a recursively sufficient set.

Proof. It is clear that N0 = ⋃2
i=0(3N0 + i). Thus, if we use this fact in (1), then we have that

Fn =
 1⋃

a0=0 · · ·
 1⋃

an−1=0
 2⋃

an=0
 (4(3
n(3N0 + an)) + 4(3n−1an−1) + · · · + 4a0 + 3),

which can also be written as

Fn =
 1⋃

a0=0 · · ·
 1⋃

an−1=0
 2⋃

an=0
 (4(3
n+1N0) + 4(3nan) + 4(3n−1an−1) + · · · + 4a0 + 3)
. (2)

Now, in view of (1) (with n + 1 instead of n) and (2), it is clear that Fn+1 ⊊ Fn, and hence, the
first assertion of the lemma is proved.
Now we prove that each Fn (n ≥ 0) is recursively sufficient. We use the complete mathematical
induction to achieve our goal. For n = 0 and n = 1 we have that F0 = 4N0 + 3 and F1 =
(12N0 + 3) ∪ (12N0 + 7), and we have already shown that these two sets are recursively sufficient.
Now suppose that n ≥ 1 and Fj is recursively sufficient for all 1 ≤ j ≤ n. We show that
then Fn+1 would also be recursively sufficient. Let us replace n with n − 1 in (2) to obtain the
following identity:

Fn−1 =
 1⋃

a0=0 · · ·
 1⋃

an−2=0
 2⋃

an−1=0
 (
4(3
nN0) + 4(3n−1an−1) + 4(3n−2an−2) + · · · + 4a0 + 3)
. (3)

477

Now, if we compare (1) and (3), we will observe that Fn = Fn−1\A where A is the following
subset of Fn−1:

A =
 1⋃

a0=0 · · ·
 1⋃

an−2=0
 (4(3
nN0) + 8(3n−1) + 4(3n−2an−2) + · · · + 4a0 + 3).

In fact, A is the yield of choosing an−1 = 2 in (3). Now, since both Fn and Fn−1 are recursively
sufficient by our inductive assumption, we see that A is a recursive set. Thus, for any typical
element m ∈ A with the form

m = 4(3
nk) + 8(3n−1) + 4(3n−2an−2) + · · · + 4a0 + 3 (k ∈ N0),

there is some positive integer f (m) < m such that f (m) ↔ m. Now, let us consider a particular
subset A′ of A comprising of all integers m ∈ A for which k = 3p + 2 (p ∈ N0). Then any
m ∈ A
′ has the form

m = 4(3
n+1p) + 8(3n) + 8(3n−1) + 4(3n−2an−2) + · · · + 4a0 + 3.

Now it is clear that A
′ is defined by

A′ =
 1⋃

a0=0 · · ·
 1⋃

an−2=0
 (4(3
n+1N0) + 8(3n) + 8(3n−1) + 4(3n−2an−2) + · · · + 4a0 + 3),

and evidently, A
′ is also a recursive set. But A′ is a subset of F ′
n, where

F ′
n =
 1⋃

a0=0 · · ·
 1⋃

an−2=0
 2⋃

an−1=0
 2⋃

an=0
 (
4(3
n+1N0) + 4(3nan) + 4(3n−1an−1) + 4(3n−2an−2)+

· · · + 4a0 + 3).

In fact, A
′ is obtained by taking an−1 = an = 2 in the above identity. On the other hand, F ′
n is
recursively sufficient because Fn ⊆ F ′
n (see (2)) and Fn is recursively sufficient (by our inductive
assumption). Therefore, F ′
n\A′ is also recursively sufficient. But, in view of (1) with n+1 instead
of n, it is clear that Fn+1 = F ′
n\A
′, and hence, Fn+1 is recursively sufficient.

Now we compute the elimination percentages of the sieves Fn (n ≥ 0).

Proposition 3.1. For any n ≥ 0 we have that ep(Fn) = 100( 4(3n)−2n

4(3n) )%.

Proof. We claim that, for any fixed non-negative integer n, any block of 4(3
n) consecutive
positive integers contains exactly 2
n elements of Fn. In fact, we use the mathematical induction to
prove this claim. For n = 0, any block of 4 = 4(30) consecutive integers contains 1 = 20 integer
of the form 4k + 3. Assume that the assertion is true for n > 0. We show that then it is also true
for n + 1. Let B be a block of 4(3
n+1) consecutive positive integers. Since 4(3
n+1) = 3(4(3n)),
the block B contains 3(2
n) members of Fn by our inductive assumption. On the other hand,
one-third of these members are removed in the process of obtaining Fn+1 from Fn (see (3) and
the three lines following it in the proof of Lemma 3.1). Therefore, two-third of them are members
of Fn+1, and so, Fn+1 has 2
n+1 members among the integers in B and the assertion is proved.
Now, in view of Definition 1.2, the elimination percentage of Fn is ep(Fn) = 100( 4(3n)−2n

4(3n) )%,
and hence, we are done.
 478

It is clear that (the sequence (ep(Fn))n is strictly increasing and) ep(Fn) →100% as n→∞. This
means that, for any integer P arbitrarily close to 100, we have a sieve FN for which ep(Fn) ≥ P %
for all n ≥ N . For example, if P = 99.999, it is easily seen that ep(Fn) > P % for any n ≥ 25.
So, in the computational verification of the conjecture, if we only check the elements of F25 then
we can claim that we are checking less than 0.001% of all integers.
We will use the following lemma in the proof of Proposition 3.2.

Lemma 3.2. Let Fn (n ≥ 0) be the recursively sufficient sets obtained in Lemma 3.1. Then we
have that

∞⋂

n=0 Fn = {4(3
n) + 4(3n−1)an−1 + · · · + 4(3a1) + 4a0 + 3 : n ≥ 0, ai ∈ {0, 1}, 0 ≤ i ≤ n − 1}

(4)

Proof. Let F = ⋂∞
n=0 Fn and E be the right hand side of (4). First we show that E ⊆ F . Let
e ∈ E be arbitrary. Then there is some N ≥ 0 such that

e = 4(3
N ) + 4(3N −1)aN −1 + · · · + 4(3a1) + 4a0 + 3.

It is clear that e ∈ Fn for all 0 ≤ n ≤ N (remember that F0 ⊇ F1 ⊇ · · · ). Now, for any n > N ,
we can write

e = 4(3
n)(0) + · · · + 4(3N +1)(0) + 4(3N )(1) + 4(3N −1)aN −1 + · · · + 4(3a1) + 4a0 + 3,

which shows that e ∈ Fn (see (1)), and since n > N was arbitrary, we deduce that e ∈ F .
Now we show that F ⊆ E. Pick an arbitrary element f ∈ F . Then f ∈ Fn for all n ≥ 0, and
hence, for any n ≥ 0, there exists a non-negative integer kn such that

f = 4(3
n)kn + 4(3n−1)an−1 + · · · + 4(3a1) + 4a0 + 3 > 4(3
n)kn

Now it is clear that there must exist some N > 0 such that kn = 0 for all n ≥ N . Then f ∈ FN
and kN = 0 imply that
 f = 4(3
N −1)an−1 + · · · + 4(3a1) + 4a0 + 3.

Now assume that 0 ≤ m ≤ N − 1 is the largest integer for which am ̸= 0. Then am = 1, and so,

f = 4(3
m) + 4(3m−1)am−1 + · · · + 4a0 + 3.

This shows that f ∈ E and we are done.

As a consequence of Corollary 2.2 and Lemmas 1.1, 3.1, and 3.2, we offer the following
result.

Proposition 3.2. Let N = 2(3
n) + 1 be the largest known integer for which SN satisfies the
Collatz conjecture. Then all integers in the interval (N, 2N ] will satisfy the conjecture as well.

479

Proof. By Lemmas 1.1, 3.1, and 3.2, the set

F =
 ∞⋂

n=0 Fn

= {4(3
n) + 4(3n−1)an−1 + · · · + 4(3a1) + 4a0 + 3 : n ≥ 0, ai ∈ {0, 1}, 0 ≤ i ≤ n − 1}

is recursively sufficient. Now, since

N = 4(3
n−1) + 4(3n−2) + · · · + 4(3) + 4 + 3,

we observe that N ∈ F . Then the smallest member of F which is greater than N would be
4(3
n) + 3, and hence, we have that (N, 2N ] ∩ F = ∅. Now, by Corollary 2.2, all integers in the
interval (N, 2N ] will satisfy the conjecture.

Remark 3.1. Before the last stage of preparing this paper for publication, we noticed that the
website in [2] has been updated recently and the new verification limit 2
71 has been achieved (see
also [3]). Now, since 2(3
44) + 1 < 2
71 < 4(3
44) + 2, a superficial glance at the statement of
Proposition 3.2 shows that all integers in the interval [2
71, 4(3
44) + 2] will satisfy the conjecture,
and hence, the number 4(3
44) + 2 ≈ 1.66 × 2
71 would be an upgraded verification limit.

Acknowledgements

We are very grateful to the reviewers and editors who carefully read this paper.

References

[1] Barina, D. (2021). Convergence verification of the Collatz problem. The Journal of
Supercomputing, 77(3), 2681–2688.

[2] Barina, D. (2025). Convergence verification of the Collatz problem. Available online at:
https://pcbarina.fit.vutbr.cz/

[3] Barina, D. (2025). Improved verification limit for the convergence of the Collatz conjecture.
The Journal of Supercomputing, 81, Article ID 810.

[4] Lagarias, J. C. (1985). The 3x + 1 problem and its generalizations. The American
Mathematical Monthly, 92(1), 3–23.

[5] Lagarias, J. C. (2009). The 3x + 1 problem: An Annotated bibliography, II (2000-2009).
ArXiv. Available online at: https://arxiv.org/abs/math/0608208v5

[6] Lagarias, J. C. (2021). The 3x + 1 problem: An overview. ArXiv. Available online at:
https://arxiv.org/abs/2111.02635

[7] Monks, K. M. (2006). The sufficiency of arithmetic progressions for the 3x + 1 conjecture.
Proceedings of the American Mathematical Society, 134(10), 2861–2872.

480
