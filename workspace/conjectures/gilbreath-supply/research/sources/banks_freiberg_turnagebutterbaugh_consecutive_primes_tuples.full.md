<!-- source: https://arxiv.org/pdf/1311.7003 | converted from PDF -->

arXiv:1311.7003v3  [math.NT]  19 Oct 2014
CONSECUTIVE PRIMES IN TUPLES

WILLIAM D. BANKS, TRISTAN FREIBERG,
AND CAROLINE L. TURNAGE–BUTTERBAUGH

Abstract. In a stunning new advance towards the Prime k-tuple Conjecture,
Maynard and Tao have shown that if k is suﬃciently large in terms of m, then
for an admissible k-tuple Hpxq “ tgx ` hjuk
j“1 of linear forms in Zrxs, the set
Hpnq “ tgn ` hjuk
j“1 contains at least m primes for inﬁnitely many n P N. In
this note, we deduce that Hpnq “ tgn ` hjuk
j“1 contains at least m consecutive
primes for inﬁnitely many n P N. We answer an old question of Erd˝os and
Tur´an by producing strings of m ` 1 consecutive primes whose successive gaps
δ1, . . . , δm form an increasing (resp. decreasing) sequence. We also show that
such strings exist with δj´1 | δj for 2 ď j ď m. For any coprime integers a and
D we ﬁnd arbitrarily long strings of consecutive primes with bounded gaps in
the congruence class a mod D.

1. Introduction and statement of results

We say that a k-tuple of linear forms in Zrxs, denoted by

Hpxq “ tgjx ` hju
k
j“1,

is admissible if the associated polynomial fHpxq “ ś

1ďjďkpgjx ` hjq has no ﬁxed
prime divisor, that is, if the inequality

#tn mod p : fHpnq ” 0 mod pu ă p

holds for every prime number p. In this note we consider only k-tuples for which

g1, . . . , gk ą 0 and ś
1ďiăjďkpgihj ´ gjhiq ‰ 0. (1)

One form of the Prime k-tuple Conjecture asserts that if Hpxq is admissible and
satisﬁes (1), then Hpnq “ tgjn ` hju
k
j“1 is a k-tuple of primes for inﬁnitely many
n P N. Recently, Maynard [5] and Tao have made great strides towards proving
this form of the Prime k-tuple Conjecture, which rests among the greatest un-
solved problems in number theory. The following formulation of their remarkable
theorem has been given by Granville [3, Theorem 6.2].

Theorem (Maynard–Tao). For any m P N with m ě 2 there is a number km,
depending only on m, such that the following holds for every integer k ě km.
If tgjx ` hju
k
j“1 is admissible and satisﬁes (1), then tgjn ` hju
k
j“1 contains m
primes for inﬁnitely many n P N. In fact, one can take km to be any number
such that km log km ą e
8m`4.

Zhang [10, Theorem 1] was the ﬁrst to prove that lim inf nÑ8ppn`1 ´ pnq is
bounded; he showed that for an admissible k-tuple Hpxq “ tx`bju
k
j“1 there exist

Date: October 21, 2014.
CLT-B is supported by a GAANN fellowship (grant no. P200A90092).
1

2 W. D. BANKS, T. FREIBERG, AND C. L. TURNAGE-BUTTERBAUGH

inﬁnitely many integers n such that Hpnq contains at least two primes, provided
that k ě 3.5 ˆ 106. Zhang’s proof was subsequently reﬁned in a polymath
project [7, Theorem 2.3] to the point where one could take k2 “ 632 (at least in
the case of monic linear forms). Maynard [5, Propositions 4.2, 4.3] has shown
that one can take k2 “ 105 and km “ cm
2e
4m in the Maynard–Tao theorem,
where c is an absolute (and eﬀective) constant. Another polymath project [8,
Theorem 3.2] has since reﬁned Maynard’s work so that one can take k2 “ 50
and km “ ce
p4´28{157qm. (In [5, 8], only tuples of monic linear forms are treated
explicitly, although the results should extend to general linear forms as considered
in [3].)
The purpose of the present note is to explain some interesting consequences
of the Maynard–Tao theorem. We refer the reader to the expository article [3]
of Granville for the recent history and ideas leading up to this breakthrough
result, as well as a discussion of its potential impact. Without doubt, this result
and its proof will have numerous applications, many of which have already been
given in [3]. We are grateful to Granville for pointing out to us that Corollary 1
(below) can now be proved.
The following theorem establishes the existence of m-tuples that inﬁnitely
often represent strings of consecutive prime numbers.

Theorem 1. Let m, k P N with m ě 2 and k ě km, where km is as in the
Maynard–Tao theorem. Let b1, . . . , bk be distinct integers such that tx ` bju
k
j“1
is admissible, and let g be any positive integer coprime with b1 ¨ ¨ ¨ bk. Then, for
some subset th1, . . . , hmu Ď tb1, . . . , bku, there are inﬁnitely many n P N such
that gn ` h1, . . . , gn ` hm are consecutive primes.

A special case of Theorem 1, with m “ 2, g “ 1 (and the weaker bound
k2 ě 3.5 ˆ 106), has already been established in recent work of Pintz [6, Main
Theorem], which is based on Zhang’s method but uses a diﬀerent argument to
the one presented here.
Theorem 1 (which is proved in §2) has various applications to the study of
gaps between consecutive primes. To state our results, let us call a sequence
pδjqm
j“1 of positive integers a run of consecutive prime gaps if

δj “ dr`j “ pr`j`1 ´ pr`j p1 ď j ď mq

for some natural number r, where pn denotes the n-th smallest prime. The
following corollary of Theorem 1 answers an old question of Erd˝os and Tur´an [1]
(see also Erd˝os [2] and Guy [4, A11]).

Corollary 1. For every m ě 2 there are inﬁnitely many runs pδjqm
j“1 of consec-
utive prime gaps with δ1 ă ¨ ¨ ¨ ă δm, and inﬁnitely many runs with δ1 ą ¨ ¨ ¨ ą δm.

Moreover, in the proof (see §2) we construct inﬁnitely many runs pδjqm
j“1 of
consecutive prime gaps with

δ1 ` ¨ ¨ ¨ ` δj´1 ă δj p2 ď j ď mq,

and inﬁnitely many runs with

δj ą δj`1 ` ¨ ¨ ¨ ` δm p1 ď j ď m ´ 1q.

CONSECUTIVE PRIMES IN TUPLES 3

Using a similar argument, we can impose a divisibility requirement amongst
gaps between consecutive primes as well.

Corollary 2. For every m ě 2 there are inﬁnitely many runs pδjqm
j“1 of con-
secutive prime gaps such that δj´1 | δj for 2 ď j ď m, and inﬁnitely many runs
such that δj`1 | δj for 1 ď j ď m ´ 1.

In the proof (see §2) we construct inﬁnitely many runs pδjqm
j“1 of consecutive
prime gaps with δ1 ¨ ¨ ¨ δj´1 | δj for 2 ď j ď m, and inﬁnitely many runs with
δmδm´1 ¨ ¨ ¨ δj`1 | δj for 1 ď j ď m ´ 1.
As another application of Theorem 1, in §2 we prove the following extension
of a result of Shiu [9] on consecutive primes in a given congruence class.

Corollary 3. Let a and D ě 3 be coprime integers. For every m ě 2, there
are inﬁnitely many r P N such that pr`1 ” pr`2 ” ¨ ¨ ¨ ” pr`m ” a mod D and
pr`m ´ pr`1 ď DCm, where Cm is a constant depending only on m.

Shiu [9] attributes to Chowla the conjecture that there are inﬁnitely many pairs
of consecutive primes pr and pr`1 with pr ” pr`1 ” a mod D (see also [4, A4]),
and proved the above result without the constraint pr`m ´ pr`1 ď DCm.

2. Proofs

Proof of Theorem 1. Replacing each bj with bj ` gN for a suitable integer N, we
can assume without loss of generality that

1 ă b1 ă ¨ ¨ ¨ ă bk.

Let S be the set of integers t such that 1 ď t ď bk, t R tb1, . . . , bku. Let tqt : t P Su
be distinct primes coprime to g such that t ı bj mod qt for all t P S, 1 ď j ď k.
By the Chinese remainder theorem we can ﬁnd an integer a such that

ga ` t ” 0 mod qt pt P Sq, (2)

and therefore ga ` bj ı 0 mod qt pt P S, 1 ď j ď kq. (3)
Consider the k-tuple

Apxq “ tgQx ` ga ` bju
k
j“1 where Q “ ś

tPS qt.

In view of (3) and the fact that gcdpg, b1 ¨ ¨ ¨ bkq “ 1, we have gcdpgQ, ga` bjq “ 1
for each j, and since tx ` bju
k
j“1 is admissible, it follows that the k-tuple Apxq
is also admissible. Moreover, Apxq satisﬁes (1) (with gj “ gQ and hj “ ga ` bj)
as the integers b1, . . . , bk are distinct and gQ ě 1.
For every N P N, the congruences (2) and our choices of Q and a imply that

gpQN ` aq ` t ” 0 mod qt pt P Sq.

Consequently, any prime number in the interval rgpQN ` aq ` b1, gpQN ` aq ` bks
must lie in Apnq. Let m
1 be the largest integer for which there exists a subset
th1, . . . , hm1u Ď tb1, . . . , bku with the property that the numbers

gpQN ` aq ` hi p1 ď i ď m
1q (4)

4 W. D. BANKS, T. FREIBERG, AND C. L. TURNAGE-BUTTERBAUGH

are simultaneously prime for inﬁnitely many N P N. Since k ě km we can apply
the Maynard–Tao theorem with Apxq to deduce that m
1 ě m.
By the maximal property of m
1, it must be the case that for all suﬃciently
large N P N, if the numbers in (4) are all prime, then gpQN ` aq ` bj is composite
for every bj P tb1, . . . , bkuzth1, . . . , hm1u. Hence, for inﬁnitely many N P N, the
interval rgpQN ` aq ` b1, gpQN ` aq ` bks contains precisely m
1 primes, namely,
the numbers tgn ` hiu
m1
i“1 with n “ QN ` a. □

Proof of Corollary 1. Let m ě 2, and let k ě km`1. Let Apxq “ tx ` 2ju
k
j“1,
which is easily seen to be admissible. By Theorem 1, there exists an pm`1q-tuple

Bpxq “ tx ` 2νj u
m`1
j“1 Ď Apxq

such that Bpnq is an pm ` 1q-tuple of consecutive primes for inﬁnitely many n.
Here, 1 ď ν1 ă ¨ ¨ ¨ ă νm`1 ď k. For such n, writing

Bpnq “ tn ` 2νj u
m`1
j“1 “ tpr`1, . . . , pr`m`1u

with some integer r, we have

δj “ dr`j “ pr`j`1 ´ pr`j “ 2νj`1 ´ 2νj p1 ď j ď mq.

Then

j´1ÿ

i“1 δi “
 j´1ÿ

i“1p2νi`1 ´ 2νiq “ 2νj ´ 2ν1 ă 2νj`1 ´ 2νj “ δj p2 ď j ď mq.

Hence, δj´1 ď δ1 ` ¨ ¨ ¨` δj´1 ă δj for each j, which proves the ﬁrst statement. To
obtain runs of consecutive prime gaps with δj ą δj`1 ` ¨ ¨ ¨ ` δm ě δj`1, consider
instead the admissible k-tuple tx ´ 2ju
k
j“1. This completes the proof. □

Proof of Corollary 2. Let m ě 2, and let k ě km`1. Put Q “ ś

pďk p, and deﬁne
the sequence b1, . . . , bk inductively as follows. Let

b1 “ 0, b2 “ Q, b3 “ 2Q,

and for any j ě 3 let
 bj “ bj´1 ` ź

1ďsătďj´1
pbt ´ bsq.

Note that pbu`1 ´ buq | pbv`1 ´ bvq pv ě u ě 1q. (5)

Now put Apxq “ tx ` bju
k
j“1, and observe that Apxq is admissible since Q
divides each integer bj. By Theorem 1, there exists an pm ` 1q-tuple

Bpxq “ tx ` bνj u
m`1
j“1 Ď Apxq

such that Bpnq is an pm ` 1q-tuple of consecutive primes for inﬁnitely many n.
Here, 1 ď ν1 ă ¨ ¨ ¨ ă νm`1 ď k. For any such n, writing

Bpnq “ tn ` bνj u
m`1
j“1 “ tpr`1, . . . , pr`m`1u

with some integer r, we have

δj “ dr`j “ pr`j`1 ´ pr`j “ bνj`1 ´ bνj p1 ď j ď mq.

CONSECUTIVE PRIMES IN TUPLES 5

Then
 j´1ź

i“1 δi “
 j´1ź

i“1pbνi`1 ´ bνiq ˇ
ˇ
ˇ
ˇ ź

1ďsătďνjpbt ´ bsq “ bνj`1 ´ bνj

if 2 ď j ď m. On the other hand, using (5) we see that

pbνj `1 ´ bνj q ˇ
ˇ
ˇ
ˇ
 νj`1´1ÿ

i“νj pbi`1 ´ biq “ bνj`1 ´ bνj “ δj.

Hence, δ1 ¨ ¨ ¨ δj´1 | δj for 2 ď j ď m, which proves the ﬁrst statement. To obtain
runs of consecutive prime gaps with δmδm´1 ¨ ¨ ¨ δj`1 | δj for 1 ď j ď m ´ 1,
consider instead the admissible k-tuple tx ´ bju
k
j“1. The corollary is proved. □

Proof of Corollary 3. Let m ě 2, and let k ě km. Let tx ` aju
k
j“1 be any
admissible k-tuple with a1 ă ¨ ¨ ¨ ă ak, and put bj “ Daj ` a for 1 ď j ď k;
then tx ` bju
k
j“1 is also admissible. Since gcdpD, bjq “ gcdpD, aq “ 1 for each
j, we can apply Theorem 1 with g “ D to conclude that there is a subset
th1, . . . , hmu Ď tb1, . . . , bku such that Dn ` h1, . . . , Dn ` hm are consecutive
primes for inﬁnitely many n P N; as such primes lie in the arithmetic progression
a mod D and are contained in an interval of length bk ´ b1 “ Dpak ´ a1q, the
corollary follows. □

Acknowledgements. In the ﬁrst draft of this manuscript, we proved Theorem
1 under the assumption that k ě exppe
12mq. We thank Andrew Granville for
showing that k need not be larger than the number km in the Maynard–Tao
theorem and for simplifying our original proof of Theorem 1. We also thank
Gergely Harcos, James Maynard, and the referee for providing helpful comments
on our earlier drafts.
 References

[1] Erd˝os, P. and P. Tur´an. “On some new questions on the distribution of prime num-
bers.” Bull. Amer. Math. Soc. 54:371–378, 1948.
[2] Erd˝os, P. “On the diﬀerence of consecutive primes.” Bull. Amer. Math. Soc. 54:885–889,
1948.
[3] Granville, A. “Primes in intervals of bounded length.” Bull. Amer. Math. Soc. To ap-
pear.
[4] Guy, R. Unsolved problems in number theory. Third edition. Problem Books in Mathe-
matics. Springer–Verlag, New York, 2004.
[5] Maynard, J. “Small gaps between primes.” Ann. of Math. (2 ). To appear.
[6] Pintz, J. “Polignac numbers, conjectures of Erd˝os on gaps between primes arithmetic
progressions in primes, and the bounded gap conjecture.” Preprint. arXiv:1305.6289,
14pp., 2013.
[7] Polymath, D. H. J. “New equidistribution estimates of Zhang type, and bounded gaps
between primes.” Preprint. arXiv:1402.0811, 165pp., 2014.
[8] Polymath, D. H. J. “Variants of the Selberg sieve, and bounded intervals containing
many primes.” Preprint. arXiv:1407.4897, 79pp., 2014.
[9] Shiu, D. K. L. “Strings of congruent primes.” J. London Math. Soc. (2 ) 61(2):359–373,
2000.
[10] Zhang, Y. “Bounded gaps between primes.” Ann. of Math. (2 ), 179(3):1121–1174, 2014.

6 W. D. BANKS, T. FREIBERG, AND C. L. TURNAGE-BUTTERBAUGH

Department of Mathematics, University of Missouri, Columbia MO, USA.
E-mail address: bankswd@missouri.edu

Department of Mathematics, University of Missouri, Columbia MO, USA.
E-mail address: freibergt@missouri.edu

Department of Mathematics, University of Mississippi, University MS, USA.
E-mail address: clbutter@olemiss.edu
