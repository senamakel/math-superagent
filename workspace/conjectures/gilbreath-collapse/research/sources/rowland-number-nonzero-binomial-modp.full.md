<!-- source: https://arxiv.org/pdf/1001.1783 | converted from PDF -->

arXiv:1001.1783v3  [math.NT]  20 Mar 2011
THE NUMBER OF NONZERO
BINOMIAL COEFFICIENTS MODULO pα

ERIC ROWLAND

Abstract. In 1947 Fine obtained an expression for the number ap(n) of bi-
nomial coeﬃcients on row n of Pascal’s triangle that are nonzero modulo p.
In this paper we use Kummer’s theorem to generalize Fine’s theorem to prime
powers, expressing the number apα (n) of nonzero binomial coeﬃcients modulo
pα as a sum over certain integer partitions. For ﬁxed α, this expression can be
rewritten to show explicit dependence on the number of occurrences of each
subword in the base-p representation of n.

1. Introduction

The study of arithmetic properties of binomial coeﬃcients has a rich history. A
main theme is that properties of ( n
m) modulo a prime p are related to the base-p
representations of n and m. Let nlnl−1 · · · n0 be the word consisting of the standard
base-b digits of a nonnegative integer n. We use n and nlnl−1 · · · n0 interchangeably.
We consider the base-b representation of 0 to be the empty word ǫ. For 0 ≤ m ≤ n
we write mlml−1 · · · m0 for the base-b representation of m, where we pad with zeros
if it is otherwise shorter than nlnl−1 · · · n0. With the exception of the proposition
in Section 2, we will take b = p to be prime.
Two of the classic results are Kummer’s theorem of 1852 [15, pages 115–116] and
Lucas’ theorem of 1878 [16].

Theorem (Kummer). Let p be a prime, and let 0 ≤ m ≤ n. The exponent of the
highest power of p dividing ( n
m) is the number of borrows involved in subtracting m
from n in base p.

Theorem (Lucas). Let p be a prime, and let 0 ≤ m ≤ n. Then
( n
m
) ≡
 l∏

i=0
 ( ni
mi
) mod p.

Let ak(n) be the number of integers 0 ≤ m ≤ n such that ( n
m) ̸≡ 0 mod k; that
is, ak(n) is the number of nonzero entries on row n of Pascal’s triangle modulo k.
Let |n|w be the number of occurrences of the word w in nlnl−1 · · · n0.
In 1899 Glaisher [8, §14] initiated the study of counting entries on row n of
Pascal’s triangle modulo k by using Lucas’ theorem to determine a2(n) = 2|n|1.
The proof is simple: In order that ( n
m
) be odd, each term ( ni
mi) in the product must
be 1, so if ni = 0 then mi = 0 and if ni = 1 then mi can be either 0 or 1.
In 1947 Fine [6] generalized Glaisher’s result to an arbitrary prime. Fine’s result
follows from Lucas’ theorem in the same way.

Date: March 19, 2011.
I would like to thank Elizabeth Kupin and Doron Zeilberger for helpful discussions.

1

2 Eric Rowland

Theorem (Fine). Let p be a prime, and let n ≥ 0. The number of nonzero entries
on row n of Pascal’s triangle modulo p is

ap(n) =
 l∏

i=0 (ni + 1) .

Note that Fine’s expression may be rewritten as

ap(n) =
 p−1∏

r=0(r + 1)
|n|r,

which more directly identiﬁes the contribution of each digit 0 ≤ r ≤ p − 1.
In Section 2 we generalize Fine’s result to prime powers, obtaining a formula for
apα(n). In Section 3 we provide an algorithm for rewriting this formula in terms of
|n|w, as we have just done with Fine’s expression. Previously, such formulas were
only known for a4(n), a9(n), and a8(n).
We mention that one may generalize Glaisher’s result in a diﬀerent direction,
namely to ask for the number ak,r(n) of integers 0 ≤ m ≤ n such that ( n
m) ≡ r
mod k. In this context, Fine’s result is an evaluation of the sum over all nonzero
residue classes when k = p is prime, and the main result of this paper is an evalu-
ation of the sum
 apα (n) =
 p
α−1∑

r=1 apα,r(n)

for a prime power modulus.
There have been several studies of ak,r(n). For prime k = p, Hexel and Sachs [11,
§5] determined a formula for ap,ri(n) in terms of (p − 1)th roots of unity, where r
is a primitive root modulo p, and from this obtained a3,1(n) = 2|n|1−1(3|n|2 + 1),
a3,2(n) = 2|n|1−1(3|n|2 − 1), and explicit formulas for a5,ri(n) in terms of |n|1,
|n|2, |n|3, and |n|4. Garﬁeld and Wilf [7] provided an algorithm to compute the
generating function ∑p−2
i=0 ap,ri(n)x
i, where again r is a primitive root. Recently,
Amdeberhan and Stanley [2, Theorem 2.1] studied the number of coeﬃcients equal
to r in the nth power of a general multivariate polynomial over a ﬁnite ﬁeld, where
r is an invertible element of the ﬁeld.
In the late 1980s researchers began to consider ak,r(n) for certain prime power
moduli k = pα. Davis and Webb [3] gave formulas for a4,1(n), a4,2(n), and a4,3(n)
in terms of |n|1, |n|10, and |n|11. Around the same time, Granville [9] showed that if
r is odd and α ∈ {2, 3} then a2α,r(n) is either 0 or a power of 2. Huard, Spearman,
and Williams [12, 14] gave formulas for a9,r(n) and a8,r(n) (and their sums, which
we derive again below). Some of these results use a generalization of Lucas’ theorem
to prime powers found by Davis and Webb [4].
There has also been some general work on squares of primes. Huard, Spearman,
and Williams [13] used the result of Hexel and Sachs to ﬁnd, when p | r and r ̸= 0,
a formula for ap2,r(n) depending only on |n|w for words w of length at most 2.
Earlier, Webb [18, Theorem 3] showed if p ∤ r then ap2,r(n) does not depend only
the subwords of length at most 2 but does depend only on the blocks of nonzero
digits in n. However, the corollary in the next section implies that by summing
ap2,r(n) over all nonzero residue classes r modulo p2 the dependence on only the
subwords of length at most 2 is achieved.

The number of nonzero binomial coeﬃcients modulo p
α 3

We would be remiss to not mention Granville’s thorough survey [10], which
discusses many additional arithmetic aspects of binomial coeﬃcients and provides
another generalization of Lucas’ theorem to prime powers.

2. Generalizing Fine’s theorem

We adopt the usual conventions that an empty sum is 0, an empty product is 1,
and there is precisely one integer partition of 0 (namely, the empty set).
For k ≥ 1, let

c(wkwk−1 · · · w0) = wk
wk + 1 ·
 (k−1∏

h=1
 b − wk−h
wk−h + 1
 )
 · b − w0 − 1
w0 + 1 .

The function c assigns a rational number to a word on the alphabet {0, 1, . . . , b−1}.
We will see this function arise naturally in the proof of Theorem 1.
For a nonnegative integer γ, let Sα(γ) be the set of integer partitions of γ into
at least max(0, γ − (α − 1)) parts, all of size at least 2. For example,

S8(10) = {{6, 2, 2}, {5, 3, 2}, {4, 4, 2}, {4, 3, 3}, {4, 2, 2, 2}, {3, 3, 2, 2}, {2, 2, 2, 2, 2}}.

Let |P | be the number of parts in the integer partition P . Let
∑

n/P c(v)c(w) · · · c(z)

be the sum over the sets {v, w, . . . , z} of |P | nonoverlapping subwords of n =
nlnl−1 · · · n0 such that the multiset {|v|, |w|, . . . , |z|} of subword lengths is equal
to P . In this sum we consider two subwords ni1 ni1−1 · · · nf1 and ni2 ni2−1 · · · nf2
to be distinct precisely when i1 ̸= i2 or f1 ̸= f2, so it would be more precise (but
more cumbersome) to say that ∑n/P is a sum over certain sets of pairs of indices.
For example, if n = n5n4n3n2n1n0 then
∑

n/{3,2}
c(v)c(w) · · · c(z)

= c(n5n4n3)c(n2n1) + c(n5n4n3)c(n1n0) + c(n4n3n2)c(n1n0)

+ c(n5n4)c(n3n2n1) + c(n5n4)c(n2n1n0) + c(n4n3)c(n2n1n0)

and ∑

n/{2,2}
c(v)c(w) · · · c(z)

= c(n5n4)c(n3n2) + c(n5n4)c(n2n1) + c(n5n4)c(n1n0)

+ c(n4n3)c(n2n1) + c(n4n3)c(n1n0) + c(n3n2)c(n1n0).

We now have the notation to state the main result of the paper.

Theorem 1. Let p be a prime, let α ≥ 0, and let n ≥ 0. The number of nonzero
entries on row n of Pascal’s triangle modulo pα is

apα (n) =
 

 l∏

i=0 (ni + 1)




 2(α−1)∑

γ=0
 ∑

P ∈Sα(γ)
 ∑

n/P c(v)c(w) · · · c(z).

4 Eric Rowland

Note that if it is convenient we may extend the sum over Sα(γ) to a sum over
partitions including 1 if we set c(w0) = 0.
Theorem 1 follows from the following proposition. Let b ≥ 2, and let An(β)
be the number of integers 0 ≤ m ≤ n such that there are exactly β borrows
involved in computing n − m in base b. Let S(γ, δ) be the set of integer parti-
tions of γ into δ parts where all parts are at least 2. For example, S(10, 3) =
{{6, 2, 2}, {5, 3, 2}, {4, 4, 2}, {4, 3, 3}}.

Proposition. Let b ≥ 2, let α ≥ 0, and let n ≥ 0. Then

An(β)
An(0) =
 2β∑

γ=β
 ∑

P ∈S(γ,γ−β)
 ∑

n/P c(v)c(w) · · · c(z).

Everett [5] gave a diﬀerent expression for An(β) as a sum over all length-l words
on {0, 1} with precisely β 1s. Everett’s expression is simpler to state and faster to
compute for an explicit integer n. However, because of its high-level dependence
on l, it is farther away from being able to produce formulas in terms of subword
counts. Note that neither expression for An(β) relies on the base b being prime.
Now let b = p be prime. By Kummer’s theorem, ( n
m) ̸≡ 0 mod pα precisely
when there are fewer than α borrows when subtracting m from n in base p. There-
fore apα(n) = ∑α−1
β=0 An(β). Substituting the expression for An(β)/An(0) in the
proposition and interchanging the two outermost sums gives the statement of the
theorem.
Therefore it suﬃces to prove the proposition. For n = nlnl−1 · · · n0 and m =
mlml−1 · · · m0, let n′ = nl−1 · · · n0 and m′ = ml−1 · · · m0. Furthermore, let n(i) =
nl−i · · · n0.

Proof of the proposition. We ﬁrst ﬁnd a recurrence for An(β) by establishing the
relationship between borrows in n − m and borrows in n′ − m′. Since An(β) = 0
when β > l, it suﬃces to consider β ≤ l.
It may happen that m′ > n′ even if m ≤ n, so we must decide how to count
borrows in the computation of n′ − m′ in this case. The standard subtraction
algorithm produces inﬁnitely many borrows. However, the only borrows that are
preserved when passing from n′ − m′ to n − m are those up through the borrow
from the lth digit in n′ (which is 0). Therefore, let Bn(β) be the number of integers
n < m ≤ bl+1 − 1 such that there are exactly β borrows up through the borrow
from nl+1 = 0 involved in computing n − m.
Now we write An(β) in terms of An′ (β) and Bn′ (β). In the computation of n−m,
a borrow from the digit ni+1 occurs if mi > ni. Moreover, if there is a borrow from
ni then the borrow is propagated to ni+1 whenever mi > ni − 1. Thus if m′ ≤ n′

then there are nl + 1 choices for ml such that m ≤ n. Similarly, if m′ > n′ then
there are nl choices for ml such that m ≤ n. Therefore

An(β) = (nl + 1)An′(β) + nlBn′ (β).

We ﬁnd a recurrence for Bn(β) analogously: If m′ ≤ n′ then there are b − nl − 1
choices for ml such that m > n. If m′ > n′ then there are b − nl choices for ml
such that m > n. In each case we gain one additional borrow, so

Bn(β) = (b − nl − 1)An′(β − 1) + (b − nl)Bn′ (β − 1).

The number of nonzero binomial coeﬃcients modulo p
α 5

Iteratively substituting the equation for Bn(β) into the equation for An(β) until
we reach Bn(β+1) (0) = 0 produces the recurrence

An(β) = (nl + 1)An′ (β) +
 β∑

i=1 nl
 

i−1∏

j=1(b − nl−j)



 (b − nl−i − 1)An(i+1) (β − i)

for n ≥ 1 and 0 ≤ β ≤ l. Divide both sides of this recurrence by An(0), which (as
in Fine’s theorem) is ∏l
i=0 (ni + 1), to obtain

An(β)
An(0) − An′ (β)
An′ (0) =
 β∑

i=1 c(nlnl−1 · · · nl−i) · An(i+1) (β − i)
An(i+1) (0) ,

where c(wkwk−1 · · · w0) is as deﬁned above. Replacing n with n(j) in this equation
and summing over 0 ≤ j ≤ l − β causes the left side to telescope, and we see that

An(β)
An(0) − An(l−β+1) (β)
An(l−β+1) (0) =
 l−β∑

j=0
 β∑

i=1 c(nl−j nl−j−1 · · · nl−j−i) · An(j+i+1) (β − i)
An(j+i+1) (0) .

If β ≥ 1 then An(l−β+1) (β) = 0, and if β = 0 then An(l−β+1) (β) = Aǫ(0) = 1.
We now verify that the expression for An(β)/An(0) given in the statement of
the proposition satisﬁes this recurrence and the correct boundary conditions. The
boundary conditions are easily checked; for β = 0 the expression is 1, and for β > l
it is 0. After substituting, the right side of the recurrence is

l−β∑

j=0
 β∑

i=1 c(nl−j · · · nl−j−i)
 2(β−i)∑

γ=β−i
 ∑

P ∈S(γ,γ−β+i)
 ∑

n(j+i+1)/P c(v)c(w) · · · c(z)

=
 l−β∑

j=0
 β∑

i=1
 2β+1−i∑

γ=β+1
 ∑

P ∈S(γ−1−i,γ−1−β)
 ∑

n(j+i+1)/P c(nl−j · · · nl−j−i)c(v)c(w) · · · c(z)

=
 2β∑

γ=β+1
 2β+1−γ∑

i=1
 l−β∑

j=0
 ∑

P ∈S(γ−1−i,γ−1−β)
 ∑

n(j+i+1)/P c(nl−j · · · nl−j−i)c(v)c(w) · · · c(z)

after shifting γ ↦→ γ − 1 − i and interchanging the sums over i and γ.
Momentarily ﬁx β + 1 ≤ γ ≤ 2β. For each 1 ≤ i ≤ 2β + 1 − γ, take each integer
composition of γ − 1 − i into γ − 1 − β parts, where all parts are at least 2, and
prepend i + 1 to get a composition of γ into γ − β parts at least 2. In doing this
we form each composition of γ into γ − β parts at least 2 precisely once. Therefore

2β+1−γ∑

i=1
 l−β∑

j=0
 ∑

P ∈S(γ−1−i,γ−1−β)
 ∑

n(j+i+1)/P c(nl−j · · · nl−j−i)c(v)c(w) · · · c(z)

= ∑

P ∈S(γ,γ−β)
 ∑

n/P c(v)c(w) · · · c(z).

The right side of the recurrence then becomes

2β∑

γ=β+1
 ∑

P ∈S(γ,γ−β)
 ∑

n/P c(v)c(w) · · · c(z),

6 Eric Rowland

which if β ≥ 1 is equal to

2β∑

γ=β
 ∑

P ∈S(γ,γ−β)
 ∑

n/P c(v)c(w) · · · c(z)

and if β = 0 is equal to

2β∑

γ=β
 ∑

P ∈S(γ,γ−β)
 ∑

n/P c(v)c(w) · · · c(z) − 1 = 0

as desired. □

We mention that the recurrences appearing early in the proof are suﬃcient to
compute apα (n) symbolically for ﬁxed α; for example, for β = 0 we have

An(0) = (nl + 1)An′ (0),

giving Fine’s theorem
 ap(n) = An(0) =
 l∏

i=0 (ni + 1) .

Of course, Fine’s theorem also follows from the full statement of Theorem 1; S1(0) =
{{}}, so the inner sum is a sum over one term, and the summand is the empty
product.
For α = 2 we have S2(0) = {{}}, S2(1) = {}, and S2(2) = {{2}}, so

ap2 (n) =
 ( l∏

i=0 (ni + 1)

)
 ·
 

 ∑

n/{} 1 + ∑

n/{2} c(w)



 .

The second sum is simply the sum over all subwords of length 2, so we have proved
the following corollary.

Corollary. Let p be a prime, and let n ≥ 0. The number of nonzero entries on
row n of Pascal’s triangle modulo p2 is

ap2(n) =
 ( l∏

i=0 (ni + 1)

)
 ·
 (
1 +
 l−1∑

i=0
 ni+1
ni+1 + 1 · p − ni − 1
ni + 1
 )
 .

Brief words are in order regarding how one can experimentally guess the general
expression for An(β)/An(0) given by the proposition once one knows the recurrence

An(β)
An(0) − An(l−β+1) (β)
An(l−β+1) (0) =
 l−β∑

j=0
 β∑

i=1 c(nl−j nl−j−1 · · · nl−j−i) · An(j+i+1) (β − i)
An(j+i+1) (0) .

It is clear from this recurrence that the fully resolved expression for An(β)/An(0)
is a sum of terms of the form c(v)c(w) · · · c(z), where (v, w, . . . , z) is a tuple of
nonoverlapping subwords of n. For example, if n = n5n4n3n2n1n0 then

An(3)/An(0) = c(n5n4n3n2) + c(n4n3n2n1) + c(n3n2n1n0)

+ c(n5n4n3)c(n2n1) + c(n5n4n3)c(n1n0) + c(n4n3n2)c(n1n0)

+ c(n5n4)c(n3n2n1) + c(n5n4)c(n2n1n0) + c(n4n3)c(n2n1n0)

+ c(n5n4)c(n3n2)c(n1n0).

The number of nonzero binomial coeﬃcients modulo p
α 7

Moreover, each tuple appears at most once. Thus it suﬃces to determine which
tuples appear.
Upon explicitly computing An(3)/An(0) and several additional values, one ob-
serves that if a tuple (v, w, . . . , z) appears in An(β)/An(0) and (˜v, ˜w, . . . , ˜z) is
a tuple of nonoverlapping subwords of the same length such that the multisets
{|v|, |w|, . . . , |z|} and {|˜v|, | ˜w|, . . . , |˜z|} are equal, then (˜v, ˜w, . . . , ˜z) also seems to ap-
pear, regardless of the order that the subwords of either tuple occur in n. For exam-
ple, all pairs of nonoverlapping subwords with lengths {3, 2} appear in An(3)/An(0).
So presumably it suﬃces to determine which multisets of subword lengths appear
for a given β (and l). From the data, one guesses that the multisets are certain
integer partitions of integers γ into γ −β parts, hence the proposition. For example,
the set of partitions appearing in An(3)/An(0) is {{4}, {3, 2}, {2, 2, 2}}.

3. Expressions in terms of |n|w

In this section we describe, for ﬁxed α, how to rewrite the expression for apα(n)
of the previous section to show explicit dependence on the subword counts for
symbolic n. Note that if w begins with 0 or ends with p − 1 then c(w) = 0, so
apα(n) does not depend on |n|w.
In Section 1 we did this for Fine’s theorem (where α = 1). For α = 2 it is also
done easily; collecting identical terms of the sum appearing in the corollary yields

ap2 (n) =
 ( p−1∏

w0=0
(w0 + 1)
|n|w0
 )
 ·
 (
1 +
 p−1∑

w1=0
 p−1∑

w0=0
 w1
w1 + 1 · p − w0 − 1
w0 + 1 · |n|w1w0
 )
 .

Now any explicit prime can be substituted to produce a formula. For example,
p = 2 gives a4(n) = 2|n|1(1 + 1
2 |n|10). For p = 3 we have

a9(n) = 2|n|13|n|2 (
1 + |n|10 + 1
4 |n|11 + 4
3 |n|20 + 1
3 |n|21
)

(ﬁrst found by Huard, Spearman, and Williams [12]), for p = 5 we have

a25(n)
2|n|13|n|24|n|35|n|4 = 1 + 2|n|10 + 3
4 |n|11 + 1
3 |n|12 + 1
8 |n|13

+ 8
3 |n|20 + |n|21 + 4
9 |n|22 + 1
6 |n|23 + 3|n|30 + 9
8 |n|31 + 1
2 |n|32 + 3
16 |n|33

+ 16
5 |n|40 + 6
5 |n|41 + 8
15 |n|42 + 1
5 |n|43,

and so on. To give a very explicit example, the base-5 representation of 1947 is
30242, so a25(1947) = 32 · 41 · 51 · (1 + 3 + 8/15) = 816.
For α = 3 the theorem provides

ap3(n)
ap(n) = ∑

n/{} 1 + ∑

n/{2} c(w) + ∑

n/{3} c(w) + ∑

n/{2,2} c(v)c(w).

The ﬁrst three sums can be directly rewritten in terms of |n|w. The ﬁnal sum
over nonoverlapping pairs of length-2 subwords can be written as the sum over
unrestricted pairs of subwords minus the sum over overlapping pairs of subwords

8 Eric Rowland

(of which there are two kinds — overlapping in one letter and overlapping in both):

2 ∑

n/{2,2} c(v)c(w)

=
 l−1∑

i=0
 l−1∑

j=0 c(ni+1ni)c(nj+1nj) − 2
 l−2∑

i=0 c(ni+2ni+1)c(ni+1ni) −
 l−1∑

i=0 c(ni+1ni)
2.

The coeﬃcients take care of symmetries among the subword lengths. Since each
of these three new sums consists of sums over the entire word length, they can be
rewritten to show the dependence on subwords of lengths 2 and 3 as
∑

v∈[p]2
 ∑

w∈[p]2 c(v)c(w)|n|v |n|w − 2 ∑

w∈[p]3 c(w2w1)c(w1w0)|n|w − ∑

w∈[p]2 c(w)
2|n|w,

where [p] = {0, 1, . . . , p − 1} is the alphabet of base-p digits. Thus we can write out
an expression for ap3 (n) in terms of |n|w. Letting p = 2 in this expression gives

a8(n) = 2|n|1 (
1 + 3
8 |n|10 + |n|100 + 1
4 |n|110 + 1
8 |n|2
10
) ,

which was obtained by Huard, Spearman, and Williams [14]. Formulas for other
primes can be found similarly: p = 3 gives

a27(n)
2|n|13|n|2 = 1 + 1
2 |n|10 + 7
32 |n|11 + 4
9 |n|20 + 5
18 |n|21

+ 3|n|100 + 3
4 |n|101 + 3
4 |n|110 + 3
16 |n|111 + 1
3 |n|120 + 1
12 |n|121

+ 4|n|200 + |n|201 + |n|210 + 1
4 |n|211 + 4
9 |n|220 + 1
9 |n|221

+ 1
2 |n|2
10 + 1
4 |n|10|n|11 + 4
3 |n|10|n|20 + 1
3 |n|10|n|21 + 1
32 |n|2
11

+ 1
3 |n|11|n|20 + 1
12 |n|11|n|21 + 8
9 |n|2
20 + 4
9 |n|20|n|21 + 1
18 |n|2
21.

For a general α we will need to be able to rewrite ∑
n/P c(v)c(w) · · · c(z) — the
sum over subwords with 0 overlaps — in terms of |n|w for any given partition P .
To do this we can use inclusion–exclusion to express this sum as sums over sets of
words with forced overlap conditions rather than restrictive overlap conditions:
∑

n/P c(v)c(w) · · · c(z) = ∑

i≥0(−1)
i ∑

ways to guarantee
i overlaps
 c(v)c(w) · · · c(z).

Now each term is a sum over all sets of subwords of the desired lengths where
certain pairs of subwords are required to overlap. For such a sum, determine the
“connected components” induced by these pairs, and for each connected component
ﬁnd all clusters of the subwords in which the required pairs overlap. Then allow
each connected component to range independently over the entire word n. Since
each sum now is over the entire word n, the expression can readily be rewritten in
terms of |n|w.
An implementation of this procedure is available in the Mathematica package
BinomialCoefficients [17]. This implementation produces formulas for a16(n),

The number of nonzero binomial coeﬃcients modulo p
α 9

a32(n), and a64(n) fairly quickly on a standard machine (in less than a minute for
a64(n)). For example,

a16(n)
2|n|1 = 1 + 5
12 |n|10 + 1
2 |n|100 + 1
8 |n|110 + 2|n|1000 + 1
2 |n|1010 + 1
2 |n|1100

+ 1
8 |n|1110 + 1
16 |n|2
10 + 1
2 |n|10|n|100 + 1
8 |n|10|n|110 + 1
48 |n|3
10.

For slightly larger powers of 2, the expressions do not become unmanageably large,
but the running time of the computation does grow quickly because of the many
ways to force i overlaps. Computing a128(n) took an hour and a half. After perform-
ing these computations, the author was made aware of Everett’s work [5], which
raises the possibility of using Everett’s expression for An(β) to compute formulas
for apα(n) more quickly. This question has not been investigated, although the
results would be interesting to know.
For an integer partition P , rewriting ∑n/P c(v)c(w) · · · c(z) as described yields
a multivariate polynomial in |n|w for various words w. Therefore apα(n)/ap(n) is
also a polynomial in |n|w. For 2 ≤ γ ≤ 2(α − 1), the longest partition in Sα(γ)
is {3, 2, . . . , 2} or {2, 2, . . . , 2} and has length ⌊γ/2⌋, so the degree of apα (n)/ap(n)
is α − 1. Moreover, the longest clusters occurring for a given α have length α, so
apα(n)/ap(n) depends only on |n|w for words w of length at most α.

Theorem 2. Let p be a prime, and let α ≥ 1. Then apα (n)/ap(n) is a polynomial
of degree α − 1 in |n|w for |w| ≤ α.

It would be nice to know more about these polynomials: How does the number
of terms grow? What can be said about the coeﬃcients? In particular, why are
the coeﬃcients always nonnegative? Can any sense be made of them as series
expansions for (n+ 1)/ap(n) if we ﬁx p and let α → ∞? For example, the coeﬃcient
of |n|10 in a2α(n)/2|n|1 for α = 1, 2, . . . takes on the values

0, 1
2 , 3
8 , 5
12 , 77
192 , 391
960 , 259
640 , . . . ,

and a plot of these values suggests that the limit of this sequence exists.
For any w it is known that |n|w is a p-regular sequence in the sense of Allouche
and Shallit [1, Theorem 6.1]. That is, |n|w is determined by a ﬁnite set of linear
recurrences in |pen + i|w along with ﬁnitely many initial conditions. From closure
properties of p-regular sequences it follows from Theorem 2 that apα(n) is also p-
regular. Experimental evidence suggests that the rank of apα(n) — the minimal
number of initial conditions required — is 2α − 1. We leave this as another open
problem.

10 Eric Rowland

References

[1] Jean-Paul Allouche and Jeﬀrey Shallit, The ring of k-regular sequences, Theoretical Com-
puter Science 98 (1992) 163–197.
[2] Tewodros Amdeberhan and Richard Stanley, Polynomial coeﬃcient enumeration,
http://arxiv.org/abs/0811.3652v1 .
[3] Kenneth Davis and William Webb, Pascal’s triangle modulo 4, The Fibonacci Quarterly 29
(1989) 79–83.
[4] Kenneth Davis and William Webb, Lucas’ theorem for prime powers, European Journal of
Combinatorics 11 (1990) 229–233.
[5] William Everett, Number of binomial coeﬃcients divisible by a ﬁxed power of a prime,
Integers 8 (2008) A11.
[6] Nathan Fine, Binomial coeﬃcients modulo a prime, The American Mathematical Monthly
54 (1947) 589–592.
[7] Richard Garﬁeld and Herbert Wilf, The distribution of the binomial coeﬃcients modulo p,
Journal of Number Theory 41 (1992) 1–5.
[8] James Glaisher, On the residue of a binomial-theorem coeﬃcient with respect to a prime
modulus, Quarterly Journal of Pure and Applied Mathematics 30 (1899) 150–156.
[9] Andrew Granville, Zaphod Beeblebrox’s brain and the ﬁfty-ninth row of Pascal’s triangle,
The American Mathematical Monthly 99 (1992) 318–331.
[10] Andrew Granville, Binomial coeﬃcients modulo prime powers, Canadian Mathematical So-
ciety Conference Proceedings 20 (1997) 253–275.
[11] Erhard Hexel and Horst Sachs, Counting residues modulo a prime in Pascal’s triangle, Indian
Journal of Mathematics 20 (1978) 91–105.
[12] James Huard, Blair Spearman, and Kenneth Williams, Pascal’s triangle (mod 9), Acta
Arithmetica 78 (1997) 331–349.
[13] James Huard, Blair Spearman, and Kenneth Williams, On Pascal’s triangle modulo p2, Col-
loquium Mathematicum 74 (1997) 157–165.
[14] James Huard, Blair Spearman, and Kenneth Williams, Pascal’s triangle (mod 8), European
Journal of Combinatorics 19 (1998) 45–62.
[15] Ernst Kummer, ¨Uber die Erg¨anzungss¨atze zu den allgemeinen Reciprocit¨atsgesetzen, Journal
f¨ur die reine und angewandte Mathematik 44 (1852) 93–146.
[16] ´Edouard Lucas, Sur les congruences des nombres eul´eriens et les coeﬃcients diﬀ´erentiels des
functions trigonom´etriques suivant un module premier, Bulletin de la Soci´et´e Math´ematique
de France 6 (1878) 49–54.
[17] Eric Rowland, BinomialCoefficients [a Mathematica package], available from the author’s
web site.
[18] William Webb, The number of binomial coeﬃcients in residue classes modulo p and p2,
Colloquium Mathematicum 60/61 (1990) 275–280.

Mathematics Department, Tulane University, New Orleans, LA 70118, USA
