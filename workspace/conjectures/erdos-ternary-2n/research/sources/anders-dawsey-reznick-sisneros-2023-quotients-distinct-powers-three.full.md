<!-- source: https://arxiv.org/pdf/2308.07252 | converted from PDF -->

arXiv:2308.07252v1  [math.NT]  14 Aug 2023
REPRESENTATIONS OF INTEGERS AS QUOTIENTS OF SUMS OF DISTINCT
POWERS OF THREE

KATIE ANDERS, MADELINE LOCUS DAWSEY, BRUCE REZNICK, AND SIMONE SISNEROS-THIRY

Abstract. Which integers can be written as a quotient of sums of distinct powers of three? We outline our

ﬁrst steps toward an answer to this question, beginning with a necessary and almost suﬃcient condition.

Then we discuss an algorithm that indicates whether it is possible to represent a given integer as a quotient

of sums of distinct powers of three. When the given integer is representable, this same algorithm generates

all possible representations. We develop a categorization of representations based on their connections to

0, 1-polynomials and give a complete description of the types of representations for all integers up to 364.

Finally, we discuss in detail the representations of 7, 22, 34, 64, and 100, as well as some inﬁnite families of

integers.
 1. Introduction

We investigate which integers can be written as a quotient of sums of distinct powers of 3. Such an integer

m is of the form

(1.1) m = 3a1 + · · · + 3aℓ−1 + 3aℓ

3b1 + · · · + 3bn−1 + 3bn = 3aℓ−bn · 3a1−aℓ + · · · + 3aℓ−1−aℓ + 30

3b1−bn + · · · + 3bn−1−bn + 30 ,

where a1, a2, . . . , aℓ and b1, b2, . . . , bn are non-negative integers with a1 > a2 > · · · > aℓ, b1 > b2 > · · · > bn,

and aℓ − bn ≥ 0. We can restrict our attention to integers m congruent to 1 mod 3. Why? Since the

numerator and denominator of the right side of (1.1) are congruent to 1 mod 3, we have m ≡ 1 (mod 3) if

aℓ − bn = 0 and m ≡ 0 (mod 3) if aℓ − bn > 0. If m ≡ 0 (mod 3), then we can write m = 3km1, where

m1 ≡ 1 (mod 3). Consequently, we will only consider integers congruent to 1 mod 3.

A straightforward estimate, given below as Theorem 1.2, shows that any integer written as a quotient of

sums of distinct powers of three must be contained in

(1.2)
 ∞⋃

r=0

( 2
3 · 3r, 3
2 · 3r)
.

Can every integer congruent to 1 mod 3 belonging to the union (1.2) be written as a quotient of sums of

distinct powers of 3? No, this necessary condition is nearly suﬃcient but not quite. The smallest integers

m ≡ 1 (mod 3) that belong to the union of intervals in (1.2) but have no representation of the form (1.1)

are m = 529, m = 592, m = 601, and m = 616, and there are only ten exceptions less than 6.2 × 106.

Date: August 15, 2023.
2010 Mathematics Subject Classiﬁcation. 11A63.
Key words and phrases. digital representations, ternary representations, Newman polynomials.

1

A very preliminary version of some of the material in this paper was presented by the third author in 2015

[9], and this presentation included the next smallest counterexample, 5368, which was found by his student

Sakulbuth Ekvittayaniphon. Independently, a few years later, Jeﬀrey Shallit and his student Sajed Haque

[5] found a total of eleven exceptions less than 107 million. See also A339636 in [8], in which it is stated

that “A simple automaton-based (or breadth-ﬁrst search) algorithm can establish in O(n) time whether n

is . . . ,” in our terms, representable. These exceptions are also discussed in [3, p,4]; the distinction of local

and universal representations does not arise. See also the thesis of the fourth author [10, pp.128-130].

1.1. Deﬁnitions, Notation, and Background Material. For r ≥ 1, let

Ar =
 {
1 +
 r−1∑

k=1 ǫk3k + 3r ∣
∣
∣
∣ ǫk ∈ {0, 1}
}
 and A = {1} ∪
 ∞⋃

r=1 Ar.

Returning to (1.1), we see that in the rightmost fraction, both the numerator and denominator are elements

of A. We use the following notation for the set of 0,1-polynomials with constant term 1, also known as

Newman polynomials, which are investigated more thoroughly in [7]:

Pr =
 {
1 +
 r−1∑

k=1 ǫkx
k + x
r ∣
∣
∣
∣ ǫk ∈ {0, 1}
}
 and P = {1} ∪
 ∞⋃

r=1 Pr.

Note that m ∈ Ar if and only if there exists a polynomial p(x) ∈ Pr such that m = p(3). With this notation,

the subject of our investigation is A/A, deﬁned as the set of integers congruent to 1 mod 3 that can be

written as a quotient of two elements of A. Since 1 ∈ A, we see that 1 can be the denominator of such a

quotient, and it follows that A ⊆ A/A. There are, however, elements of A/A that do not belong to A. One

such example is 7, which we shall consider shortly.

We use the notation w = [ǫr ǫr−1 . . . ǫ1 ǫ0]3 to indicate the standard base 3 representation of the integer

w, where the digits ǫr, . . . , ǫ0 ∈ {0, 1, 2}. For example, the standard base 3 representation of the integer 7 is

7 = [21]3. We see from this standard base 3 representation that 7 does not belong to A; because

(1.3) 7 = 28
4 = [1001]3
[11]3 = 33 + 1
3 + 1 = p(3)
q(3) ,

where p(x) = x
3 + 1 ∈ P3 and q(x) = x + 1 ∈ P1, we have that 7 ∈ A/A.

Throughout this document, we say an integer is representable if it can be written as a quotient of sums

of distinct powers of 3 using any of the types of formats illustrated in (1.3). In the example of the integer

7, we notice that p(x)
q(x) = x
2 − x + 1, which, when evaluated at any integer x, will yield an integer. We call

such a representation universal. Not every representation is universal; those that are not we call local, and

the smallest example of a local representation in base 3 is

22 = 22 · 37
37 = 814
37 = 36 + 34 + 3 + 1
33 + 32 + 1 = p(3)
q(3) ,

where p(x) = x
6 + x
4 + x + 1 ∈ P6 and q(x) = x
3 + x
2 + 1 ∈ P3. Note that q(x) does not divide p(x) in this

example, and so in general the quotient p(b)
q(b) need not be an integer when evaluated at an integer b ̸= 3. As

2

an example, p(1)
q(1) = 4
3 . Note also that 22 = 33 − 32 + 3 + 1, and it is not surprising that

x
6 + x
4 + x + 1 = (x
3 + x
2 + 1)(x
3 − x
2 + x + 1) + x
3(x − 3),

since the polynomials involved in the representation of 22 indicate that the remainder from polynomial

division must be divisible by x − 3. We now state the deﬁnitions of universal representation and local

representation more formally.

Deﬁnition 1.1. Let m be an integer such that m ≡ 1 (mod 3) and m = p(3)
q(3) , where p(x), q(x) ∈ P. If

q(x) | p(x), then the representation of m as p(3)
q(3) is universal. If q(x) ∤ p(x), then this representation of m is

local.

Notice that any integer m ≡ 1 (mod 3) which can be written as a sum of distinct powers of 3 has a

universal representation m = p(3)
q(3) with q(x) = 1. Throughout, we refer to a universal representation for

which q(x) = 1 as a trivial universal representation.

Next we prove the aforementioned theorem that states that an integer written as a quotient of sums of

distinct powers of 3 must belong to the union given in (1.2).

Theorem 1.2. For any integer r, let Ir = ( 2
3 · 3r, 3
2 · 3r)
. If m ∈ A/A, then m ∈ Ir for some r. Moreover,

if m = p(3)
q(3) for some p(x), q(x) ∈ P, then there exists an integer e such that p(x) ∈ Pe+r and q(x) ∈ Pe.

Proof. Suppose p(x) ∈ Pd. Then

3d < 1 + 3d ≤ p(3) ≤ 1 +
 d−1∑

k=1 3k + 3d = 3 · 3d − 1
3 − 1 < 3
2 · 3d.

Accordingly, if q(x) ∈ Pe, then 3e < q(3) < 3
2 · 3e, so

2
3 · 3d−e = 3d

3
2 · 3e < p(3)
q(3) <
 3
2 · 3d

3e = 3
2 · 3d−e,

and thus p(3)
q(3) ∈ Id−e. This inequality holds regardless of whether p(3)
q(3) is an integer. If m = p(3)
q(3) , then

m ∈ Id−e, establishing the necessary condition; if m ∈ Ir, then d = e + r. □

What do the intervals in Theorem 1.2 remind us of? This question led to our initial interest in these

representations of integers. In 2019, Athreya, Tyson, and the third author studied the standard Cantor set,

C =
 { ∞∑

k=1
 αk
3k
 ∣
∣
∣
∣ αk ∈ {0, 2}
}
 ,

and they proved in [2, Theorem 1] that

(1.4) { u
v
 ∣
∣
∣
∣ u, v ∈ C, v ̸= 0} =
 ∞⋃

r=−∞
 [ 2
3 · 3r, 3
2 · 3r] .

Note the similarity between this union and that given in (1.2). We also highlight and explain some of the

diﬀerences. Since we are only considering integers in our work, the union in (1.2) is over r ≥ 0. Another

diﬀerence is that we only consider integers congruent to 1 mod 3, while in (1.4), there is no restriction

3

regarding the congruence class of the integer mod 3. For example, 1
3 , 2
3 ∈ C, so 2/3
1/3 = 2 is a quotient of

elements of the Cantor set, but of course 2 ≡ 2 (mod 3) cannot be represented as a quotient of sums of

distinct powers of 3, as we have discussed.

The usual construction of the Cantor set involves a sequence of sets Cn consisting of 2n closed intervals,

each of length 3−n. Consider the set of quotients of left endpoints of these intervals:
{ ∑d
k=1 αk
3k
∑e
j=1 βj
3j
 ∣
∣
∣
∣ αk, βj ∈ {0, 2}
}
 =
 { 2 · 3−d ∑d
k=1 1
2 αk · 3d−k

2 · 3−e ∑e
j=1 1
2 βj · 3e−j
 ∣
∣
∣
∣ αk, βj ∈ {0, 2}
}

=
 { 3e−d · ∑d
k=1 1
2 αk · 3d−k
∑e
j=1 1
2 βj · 3e−j
 ∣
∣
∣
∣ αk, βj ∈ {0, 2}
}
 .

Each element of this set is a quotient of two elements of P, evaluated at x = 3, multiplied by a power of 3.

The question of which polynomials are quotients of two elements of P seems to be both open and hard.

One observation is that if r(x) = p(x)
q(x) , then the zeros of r(x) are a subset of the zeros of p(x). Determining

the zeros of polynomials in P also seems to be a very hard question; see [7].

In 1987, John Loxton and Alf van der Poorten wrote a paper entitled “An awful problem about integers

in base four” [6], which was dedicated to proving that every odd integer can be written as a quotient of

sums and diﬀerences of powers of 4. What was “awful” was only that there was not an elegant top-down

solution. Their paper reports that Selfridge and LaCampagne asked a similar question for 3, and the authors

mentioned that if diﬀerences are removed, as in the case we are investigating, “There is some diﬃculty in

describing which integers can occur.”

We concur with this quote, and in this paper we report our ﬁndings and early progress in determining

which integers congruent to 1 mod 3 can be written as quotients of sums of distinct powers of 3. In Section

2, we exhibit several families of integers having only universal representations, and then we consider 100, the

smallest integer having only universal representations but not belonging to any of these families. In contrast

to the integers discussed in Section 2, some integers have only local representations. We investigate two

such examples, 22 and 34, in Section 3.1. Then, in Section 3.2, we present 64 as an example of an integer

having both nontrivial universal representations and local representations. In Section 4, we provide a table

that indicates for each integer m ≡ 1 (mod 3) contained in the union (1.2) up to m = 364 whether m has a

universal representation and whether m has a local representation. Finally, we outline further directions to

explore in Section 5.

The following examples illustrate a few of the possible combinations of types of representations that can

exist for a single integer m ≡ 1 (mod 3).

Example 1.3. The integer 31 = 33 + 3 + 1 has a trivial universal representation with p(x) = x
3 + x + 1 and

q(x) = 1. It is also the case that if g(x) = x
5 − x
3 + 1 and h(x) = x
2 − x + 1, then g(3)
h(3) = 217
7 = 31, and

h(x) ∤ g(x). Since neither g(x) nor h(x) is in P, we know that g(3)
h(3) is not a universal representation of 31.

However, with a suitable common multiplier for g(x) and h(x), we can obtain polynomials in P and see that

31 has a local representation in addition to its trivial universal representation. In fact, 31 actually has many

local representations, and the algorithm in Section 1.2 describes how to ﬁnd them. As a speciﬁc example of

4

such a local representation, observe that

x
5 − x
3 + 1
x2 − x + 1 = (x
5 − x
3 + 1)(x
4 + x
3 + x
2 + x + 1)
(x2 − x + 1)(x4 + x3 + x2 + x + 1) = x
9 + x
8 + x
2 + x + 1
x6 + x4 + x3 + x2 + 1 .

Example 1.4. As another example of an integer that has both a trivial universal representation and a local

representation, consider 37 = 33 + 32 + 1. We can also write

37 = 36 − 33 + 1
33 − 32 + 1 .

The polynomials x
6 − x
3 + 1 and x
3 − x
2 + 1 are not in P, but if we multiply each by x
5 + x
4 + x
3 + x
2 + x + 1,

we obtain polynomials that do belong to P, and we have 37 = p(3)
q(3) , where p(x) = x
11 + x
10 + x
9 + x
2 + x + 1

and q(x) = x
8 + x
5 + x
4 + x
3 + x + 1. To conclude that this is a local representation, we must have that

q(x) ∤ p(x). We could show this with polynomial long division, or we can consider evaluating the quotient

p(x)
q(x) at x = 2, for example. This yields 3591
315 , which is not an integer and tells us the representation of 37 as

p(3)
q(3) must be local.

Example 1.5. It is also possible for an integer to have two universal representations with diﬀerent polyno-

mial quotients. For example, 841 = 36 + 34 + 33 + 3 + 1 is a trivial universal representation of 841 with the

polynomial quotient being x
6 + x
4 + x
3 + x + 1. In addition, 841 has a nontrivial universal representation

with polynomial quotient x
6 + x
5 − x
4 − 2x
3 + x + 1, since 841 = 36 + 35 − 34 − 2 · 33 + 3 + 1 = p(3)
q(3) with

p(x) = x
15 + x
14 + x
11 + x
5 + x
4 + x
2 + x + 1 and q(x) = x
9 + x
7 + x
6 + x
5 + x
4 + x
3 + x
2 + 1.

For a given integer m, we have developed an algorithm for determining whether m is an element of A/A.

This algorithm is a reﬁnement of a multiplication transducer, which we shall discuss in more detail in Section

1.2. As noted previously, we need only consider the integers m ≡ 1 (mod 3) belonging to an interval of the

form given in Theorem 1.2. For such m, this algorithm explores all possibilities for multiples of m by q, a sum

of distinct powers of 3, such that mq = p is also a sum of distinct powers of 3. This can be done manually

or through the construction of a directed graph that represents all possible multiplications. The algorithm

leverages intuition similar to more familiar multiplication algorithms in base 10, performing multiplication

in steps, starting with the ones digit, and “carrying” powers of 3. However, our algorithm does not require

the summation of partial products.

Rather than using our algorithm to compute the product p of given integers m and q, we instead start

with a given integer m ≡ 1 (mod 3) and construct both p and q simultaneously to ensure that they are

elements of A, choosing only paths forward that preserve this necessary condition. Thus, we begin with

30 = 1 copy of m, and then for each positive power i of 3, we need to choose whether or not to include 3i

additional copies of m in q, building the base 3 representation of q as we move through the algorithm.

1.2. The Algorithm, Digraphs, and Multiplication Transducers. We begin with a familiar example,

using the algorithm to construct the quotient given in (1.3) for m = 7. Denote this quotient by 7 = p
q ∈ A/A.

The procedure of constructing this quotient involves iterating through steps, where each step “records” the

ith digit of the product 7 · q = p in base 3, as well as the ith digit of q. Since p, q ∈ A, it is necessary to

record a digit of 1 in the 30 place of the base 3 expansions of both p and q. Write the base 3 expansion

5

of 7 as 7 = (2 · 31 + 1) · 30. After recording 1 into the 30 place of p, the remaining unrecorded value is

(2 · 31) · 30 = 2 · 31 to “carry” into the next step, which is the 31 step. Note that the number of copies of 31

in this unrecorded value that we must carry into the next step is 2, which is congruent to 2 mod 3. In order

to record either 0 or 1 into the 31 place of p = 7 · q, we need to ﬁrst add more copies of 31 to q. Hence we

add m = 7 to the carried value of 2, which gives us (m + 2) · 31 = (7 + 2) · 31 = 9 · 31. To account for this

addition of m · 31 = 7 · 31 into 7 · q = p, we must record a digit of 1 in the 31 place of q. Now, we observe that

9 · 31 = 3 · 32, so 3 is the value which we must carry at the 32 step. Since 3 is a sum of distinct powers of 3,

we can stop iterating and complete the construction. In fact, we have that 3 · 32 = 33, so we record a digit of

0 in the 32 place of p and a digit of 1 in the 33 place of p. The result of the algorithm is therefore 7 · q = p,

which is given by the equation 7 · (31 + 30) = 33 + 30. It follows that 7 = p
q = [1001]3
[11]3 , the representation

from (1.3). A complete description of all possible representations of 7 is given by Theorem 2.4 Part (3) with

r = k = 1.

In general, we can perform the algorithm iteratively by following the steps below, and in the case that

m = p
q ∈ A/A, each step i produces the digit of the ith power of 3 in the base 3 expansions of both q and

p. We record either 0 · 3i or 1 · 3i into the base 3 expansions of q and p in the ith step, depending on the

result of the previous step, and then we consider the remaining unrecorded value as carrying multiples of

3i+1 into the next step. We refer to the number of copies of 3i+1 which are carried into the next step as

the carry value. As described in the following procedure, we use an initial carry value of 0 in Step 0. The

general algorithm is that for Step i, where i ≥ 1:

(1) Determine the number of copies of 3i recorded into the base 3 expansions of p and q in Step i by

following the bullet point below which corresponds to the carry value at the end of Step i − 1.

• If the carry value is congruent to 1 mod 3: record 0 · 3i into q, record 1 · 3i into p, and subtract

1 from the carry value.

• If the carry value is congruent to 2 mod 3: add m to the carry value, record 1 · 3i into q, and

record 0 · 3i into p.

• If the carry value is congruent to 0 mod 3, we have a choice: either

– add m to the carry value, record 1 · 3i into q, record 1 · 3i into p, and subtract 1 from the

carry value (note: we always make this choice at Step 0), or

– record 0 · 3i into q, and record 0 · 3i into p.

(2) After recording 0 · 3i or 1 · 3i into p and q according to the conditions above and subtracting 1 from

the carry value if necessary, the result will be divisible by 3i+1. Factor out 3i+1 from this result, and

what remains is the new carry value at the end of Step i.

(3) Move to Step i + 1 using this new carry value.

The algorithm terminates when either (i) the carry value is w, a sum of distinct powers of 3, or (ii) all

possible destinations from a given Step i have already been visited without arriving at a sum of distinct

powers of 3.

In Case (i), the base 3 expansion of the integer q is complete when the algorithm terminates, and the

base 3 expansion of the integer p is completed by appending the base 3 representation of w to the left of the

6

values already recorded for p. In our example m = 7, the algorithm terminated when we arrived at a carry

value of 3 from 9 ∗ 31 = 3 ∗ 32. The algorithm terminated because the carry value w = 3 is a sum of distinct

powers of 3. We then completed p by appending [10]3, the base 3 expansion of 3, to arrive at 7 = [1001]3
[11]3 .

In Case (ii), the integer m is not representable, because the algorithm enters an inﬁnite loop and never

arrives at a ﬁnite quotient. This is precisely what happens with m = 529, m = 592, m = 601, m = 616,

and the other integers that are congruent to 1 mod 3 and belong to the union given in (1.2) but cannot be

represented as quotients of sums of distinct powers of 3.

The remarks below provide additional justiﬁcation as to why the algorithm builds a representation of m

as p
q , where p, q ∈ A.

• The procedure builds the base 3 expansions of q and p one digit at a time based on the powers of

3 required to obtain mq = p, where p and q are both sums of distinct powers of 3. Since p and q

cannot have any digits of 2 in their base 3 expansions, we must add m to any carry values congruent

to 2 mod 3 in order to record either 0 · 3i or 1 · 3i for p in Step i. This addition corresponds to adding

1 · 3i to q, since then we will have added m · 3i to the product mq = p. After adding m ≡ 1 (mod 3)

to such a carry value in Part (1) of the algorithm, the result will be divisible by 3i+1, so we may

move to Part (2) of the algorithm.

• The carry value is the part of the remaining unrecorded value, after recording 0 · 3i or 1 · 3i into p in

Step i, which carries multiples of 3i+1 into the next step. For this reason, we must subtract 1 from

the carry value every time we record 1 · 3i into p, so that what remains is the part of the carry value

which was unrecorded in Step i.

• When a carry value is congruent to 0 mod 3, the two choices in Part (1) of the algorithm correspond

to the two diﬀerent ways of arriving at a multiple of 3i+1 to be carried from Step i into Step i + 1.

The ﬁrst way is to add m to the carry value and correspondingly record 1 · 3i into q, then subtract

1 · 3i from the carry value after recording a digit of 1 into the 3i place of p, and move to Part (2) of

the algorithm with the resulting multiple of 3i+1. The second way is to simply factor out another 3

from the carry value, which is divisible by 3 in this case, to get a multiple of 3i+1.

The algorithm can be illustrated through a directed graph with the carry values as vertices. We present

the graph for m = 22 in Figure 1. In Example 1.6, we discuss how to use the directed graph to obtain

representations of 22 as a quotient.

Example 1.6. Let’s consider the algorithm for m = 22. We will use Figure 1 to keep track of what happens

in each step.
 0 7 2 8 10

1
1 11
01
 011
101 0011
1101

Figure 1. Directed graph of the steps of the algorithm for m = 22.

7

• Step 0: As always, we start with a carry value of 0, which is congruent to 0 mod 3, and we choose

to add m = 22 to the carry value, record 1 · 30 into q and into p, subtract 1 from the carry value

accordingly, and move to Step 1. The remaining unrecorded value is (22 − 1) · 30 = 21 · 30 = 7 · 31,

which yields a carry value of 7. Note that in Figure 1, Step 0 corresponds to the edge from the vertex

0 to the vertex 7, which is the new carry value, and the label on the edge denotes the 30 digits of

the base 3 expansions of p (in the numerator) and q (in the denominator).

• Step 1: The carry value is 7 ≡ 1 (mod 3). We record 0 · 31 into q and 1 · 31 into p, and we subtract 1

from the carry value accordingly. The remaining unrecorded value is now (7 − 1) · 31 = 6 · 31 = 2 · 32,

which yields a carry value of 2. In Figure 1, Step 1 corresponds to the edge from the vertex 7 to the

vertex 2, the new carry value, and the new recorded digits in the edge label, p in the numerator and

q in the denominator, are the 31 digits.

• Step 2: The carry value is 2 ≡ 2 mod 3. We add m = 22 to the carry value, record 1 · 32 into q, and

record 0 · 32 into p. The remaining unrecorded value at this step is (2 + 22) · 32 = 24 · 32 = 8 · 33,

which yields a carry value of 8. Step 2 corresponds to the edge from the vertex 2 to the vertex 8

with the 32 digits of p and q recorded.

• Step 3: The carry value is 8 ≡ 2 (mod 3), so we again add m = 22 to the carry value, record 1 · 33

into q, and record 0 · 33 into p. The remaining unrecorded value is (8 + 22) · 33 = 30 · 33 = 10 · 34,

which yields a carry value of 10. Step 3 corresponds to the edge from the vertex 8 to the vertex 10

with the 33 digits of p and q recorded.

• Step 4: The carry value is 10 = 32 + 30, which is a sum of distinct powers of 3, so the algorithm

terminates.

At this point, we append the base 3 representation of 10, [101]3, to the left of the digits for p, and we arrive

at the ﬁnal quotient 22 = [1010011]3
[1101]3 .

In the example m = 22, for vertices congruent to 0 mod 3, we make the ﬁrst choice in the description of

the algorithm (adding m) only in the ﬁrst step, as the second option would loop back to the vertex 0 and

keep us from moving toward our goal of obtaining a representation of m. If we continued beyond the carry

value of 10 to draw edges for all possible paths originating at the vertex 0, we would have the extended graph

in Figure 2. Such an extended graph shows all representations of an integer m. The particular representation

of m = 22 constructed above by stopping after the carry value of 10 is the same representation we obtain

from following the path 0 → 7 → 2 → 8 → 10 → 3 → 1 → 0 in Figure 2, since the subpath 10 → 3 → 1 → 0

appends the same digits to p as the digits in the base 3 representation of 10. We see this by observing that

the subpath 10 → 3 → 1 → 0 contributes no digits to q while contributing to p the digits 101.

In general, the algorithm serves two main purposes for this paper. First, if the algorithm terminates for a

given integer m ≡ 1 (mod 3), as in Step 4 of Example 1.6, then the algorithm proves that m is representable.

Second, if all possible paths back to 0 are included in the graph produced by the algorithm for a given m, then

the algorithm provides an explicit construction of all representations of m. The directed graph involves two

8

0 7 2 8 10 3 1

Figure 2. The subgraph of the multiplication transducer for m = 22 in base 3 that
encodes all representations of 22 as a quotient of sums of distinct powers of 3.

branches corresponding to the two choices in the algorithm. Next we will discuss the additional information

about an integer m and its representations that can be gleaned from an extended graph.

The graph in Figure 1 is a subgraph of the graph in Figure 2, while the graph in Figure 2 can be generated

as a subgraph of a multiplication transducer. A multiplication transducer, as described in [4], is a ﬁnite state

automaton which performs the operation of multiplication by m in base b for any given positive integers m

and b. The multiplication transducer that performs multiplication by m in base 3 can multiply m · q = p

for any positive integer q as follows: by reading the digits of the base 3 representation of q from right to

left, following the directed edges of the graph, and recording the digits of p after each step. This process

continues until all digits have been read and the value carried over from the previous step is 0. As noted, the

graph in Figure 2 is a subgraph of the multiplication transducer that multiplies by m = 22 in base 3, and

this subgraph can be generated from the transducer as follows: by restricting edges to those that generate

q, p ∈ A and subsequently restricting vertices to the carry values that are possible steps in the computation

m · q = 22 · q = p for q, p ∈ A.

When exploring the representations of an integer m through an expanded graph that includes the path

back to the vertex 0, such as Figure 2, we can generate all possible representations of m as a quotient of

sums of distinct powers of 3. Each representation corresponds to a speciﬁc closed walk through the vertices

of the digraph, starting and ending at the vertex 0. We note that a closed walk must include at least one

step away from the vertex 0 in order to correspond to a valid representation, and by restricting our attention

to elements of A, we ensure that the initial step away from the vertex 0 will never be from the vertex 0 to

itself. In the example above, we outlined the representation 22 = [1010011]3
[1101]3 = 814
37 , but taking a diﬀerent

closed walk, stepping up from the vertex 3 to the vertex 8 before returning to the vertex 0 in Figure 2, would

give the representation 22 = [1010110011]3
[1101101]3 = 22198
1009 .

Deﬁnition 1.7. An indecomposable walk is a closed walk through the graph that contains the vertex 0 as

the initial point and terminal point but not as an interior point, and an indecomposable representation is a

representation corresponding to such a walk. A decomposable walk is a closed walk through the graph that

contains the vertex 0 not only as the initial point and terminal point but also as an interior point, and a

decomposable representation is a representation corresponding to a decomposable walk.

9

In the example of m = 22, the representations given in the paragraph above Deﬁnition 1.7 are indecom-

posable representations, while 22 = [10100111010011]3
[11010001101]3 is an example of a decomposable representation. In

general, a decomposable representation can be thought of as the concatenation of multiple indecomposable

representations written in base 3. Before concatenating, we append copies of the digit 0 to the denomina-

tor of each indecomposable representation to make the lengths of the numerator and denominator match.

To create the decomposable representation we gave for m = 22, we concatenated two copies of [1010011]3
[1101]3 ,

appending three digits of 0 as placeholders in the denominator of the ﬁrst (underlined) copy. This can also

be thought of in base 10 as creating the representation 22 = 3
7·814+814
37·37+37 . In other words, a decomposable

representation can be written as 3
kp1+p2
3kq1+q2 for two representations m = p1
q1 and m = p2
q2 , where k is at least the

length of the base 3 representation of p2.

2. Integers with only universal representations

In our exploration of representations of integers as quotients of sums of distinct powers of 3, we have

encountered many integers m ≡ 1 (mod 3) which have only universal representations. We devote this

section to such integers. We begin in Section 2.1 by describing how to build new universal representations

from a given universal representation. In Section 2.2, we prove that four inﬁnite families of integers have

only universal representations. Finally, we investigate the representations of integers of the form m = 3n − 2

in Section 2.3 and of m = 100 in Section 2.4.

2.1. Tools for Building New Representations. Given a representation of an integer m as a quotient of

sums of distinct powers of 3, there are several ways we can generate new representations. Some aspects of

this study can be handled quickly, using only properties of the set P. Before proceeding, it will be helpful

to adopt an alternative description of Newman polynomials and to establish two lemmas. Write

p(x) = 1 +
 r−1∑

k=1 ǫkx
k + x
r =
 m∑

j=0 x
aj ,

where 0 = a0 < a1 < · · · < am = r, and let ∆(p) := {ai − aj : 0 ≤ j < i ≤ m}. The following lemma

identiﬁes exactly when a product of Newman polynomials is itself a Newman polynomial.

Lemma 2.1. Suppose s(x), t(x) ∈ P. Then (st)(x) ∈ P if and only if ∆(s) ∩ ∆(t) = ∅.

Proof. If s(x) = m∑

k=0 x
ak and t(x) = n∑

ℓ=0 x
bℓ , then (st)(x) = m∑

k=0
 n∑

ℓ=0 x
ak+bℓ. The coeﬃcient of x
j in (st)(x)

is the number of times that ak + bℓ = j, which is always non-negative and is in {0, 1} if and only if

ak + bℓ = ak′ + bℓ′ implies k = k′ and ℓ = ℓ′. This happens if and only if ak − ak′ = bℓ′ − bℓ is equivalent to

k = k′ and ℓ = ℓ′, which happens if and only if ∆(s) ∩ ∆(t) = ∅. □

We remark here that one simple way to avoid common exponent gaps between two Newman polynomials

s(x), t(x) is to require that all exponent gaps in s(x) are greater than the degree of t(x), or vice versa. This

is a recurring idea in this paper and will be referenced several times in the remainder of this subsection as

well as in the proof of Theorem 2.6.
 10

We now present a diﬀerent version of Lemma 2.1 which can be used to view exponent gaps within Newman

polynomials more generally from the perspective of universal representations. This lemma can be proved by

a direct computation, which is omitted.

Lemma 2.2. Suppose pj(x), qj (x) ∈ P for all 1 ≤ j ≤ w and p(x) = ∑
j x
nj pj(x), q(x) = ∑j x
nj qj(x) ∈ P,

with no other conditions on the non-negative integers nj. Suppose further that pj (x)
qj (x) = t(x) for all j. Then

p(x)
q(x) = t(x) as well. Similarly, if pj (3)
qj (3) = t(3) = m for all j, then p(3)
q(3) = m.

Note that if we impose the additional condition that nj > deg (∑i<j x
ni pi(x)
) for each j, then we obtain

a special case of Lemma 2.2 that will be applied in the proof of Theorem 2.6 to prove the universality of

some representations of 100.

Equipped with these lemmas, we now discuss two ways to build new representations from a given rep-

resentation. First, we can generate additional representations of the same integer m. Every integer having

one representation in fact has inﬁnitely many representations. Suppose m = p(3)
q(3) , where p(x), q(x) ∈ P and

deg p(x), deg q(x) ≤ T . If f (x) is any polynomial in A for which the gaps in exponents are greater than T ,

then the exponent gaps in f (x) ensure that there are no possible cross-terms in the products (f p)(x) and

(f q)(x). By Lemma 2.1, we have that (f p)(x), (f q)(x) ∈ A, and so m = (f p)(3)
(f q)(3) , giving a new representation

of the same integer m, and this new representation is decomposable.

Secondly, we can work with a given representation of m to obtain representations of other integers.

Suppose m = p(3)
q(3) ∈ A/A and f (x) ∈ P is any polynomial for which ∆(f ) ∩ ∆(p) = ∅. Then (f p)(x) ∈ P

by Lemma 2.1, so, multiplying m by f (x) and evaluating at x = 3, we have that f (3) · m = (f p)(3)
q(3) is in

A/A and is a representation not of m but of f (3) · m. A particular type of polynomial f (x) that will yield

such a representation of a new integer is a polynomial f (x) with exponent gaps larger than the degree of

p(x). More explicitly, if deg p(x) = r and f (x) ∈ P such that min ∆(f ) > r, then (f p)(x) ∈ P and thus

f (3) · m ∈ A/A.

2.2. Special families. This section is dedicated to proving that several inﬁnite families of integers m ≡ 1

(mod 3) have only universal representations and, moreover, that those universal representations must have a

speciﬁc form. There are certain values of m for which the representation m = p(3)
q(3) ∈ A/A gives very strong

conditions on p(x) and q(x), and the following lemma will be useful as we prove these conditions.

Lemma 2.3. Let C, D be sets of integers, and suppose one of the following two cases holds:

• Case 1: C = D = {n, n + 1, n + 2}, where n ∈ Z;

• Case 2: C = {0, 1} and D = {−1, 0, 1, 2}.

Let a(x) = ∑
i aix
i and b(x) = ∑i bix
i, where ai ∈ C and bi ∈ D. If a(3) = b(3), then ai = bi for all i, so

a(x) = b(x).

Proof. We prove the result by induction on max{deg a(x), deg b(x)}; the assertion is clear when this maximum

is 0. Since a(3) = b(3), we know ∑i ai3i = ∑i bi3i, and this gives a0 ≡ b0 (mod 3). In the ﬁrst case, this

means that a0 = b0; we may write a(x) = a0 + x˜a(x) and b(x) = b0 + x˜b(x) and apply the inductive argument

to ˜a, ˜b. In the second case, we ﬁrst note that b0 /∈ {−1, 2} and, again, a0 = b0 and repeat the argument. □

11

These results allow us to make explicit statements about representations of certain special families of

integers congruent to 1 mod 3. If m belongs to one of the families described below in Theorem 2.4, then m

has only universal representations, and they must be of a particular kind.

Theorem 2.4. Let p(x), q(x) ∈ P.

(1) If 3r + 1 = p(3)
q(3) , then p(x) = (x
r + 1)q(x).

(2) If 3rk + 3(r−1)k + · · · + 3k + 1 = p(3)
q(3) , then

p(x) = (x
rk + x
(r−1)k + · · · + x
k + 1)q(x) = x
(r+1)k − 1
xk − 1 q(x).

(3) If 32rk − 3(2r−1)k + · · · − 3k + 1 = p(3)
q(3) , then

p(x) = (x
2rk − x
(2r−1)k + · · · − x
k + 1)q(x) = x
(2r+1)k + 1
xk + 1 q(x).

(4) If r > s > 0 and 3r − 3s + 1 = p(3)
q(3) , then

p(x) = (x
r − x
s + 1)q(x).

In each of these four cases, there exist p(x), q(x) ∈ P which satisfy the particular condition.

Proof. The proofs of the various parts of this theorem are similar and begin by letting p(x), q(x) ∈ P.

For Part 1, assume 3r + 1 = p(3)
q(3) , and consider the polynomials p(x) and (x
r + 1)q(x). Observe that the

coeﬃcients of p(x) are in {0, 1} and the coeﬃcients of (x
r + 1)q(x) are in {0, 1, 2}. Since p(3) = (3r + 1)q(3),

we know from Lemma 2.3 that p(x) = (x
r + 1)q(x). A simple example with p(x), q(x) ∈ P comes from taking

q(x) = 1.

Similarly, in Part 2, assume 3rk + 3(r−1)k + · · · + 3k + 1 = p(3)
q(3) , and consider the polynomials (x
k − 1)p(x)

and (x
(r+1)k − 1)q(x). Since p(x), q(x) ∈ P, it follows that both (x
k − 1)p(x) and (x
(r+1)k − 1)q(x) have

coeﬃcients in {−1, 0, 1}. We take their quotient at x = 3 and use the hypothesis regarding p(3)
q(3) to obtain

(3(r+1)k − 1)q(3)
(3k − 1)p(3) = (3(r+1)k − 1)
(3k − 1)
 ( p(3)
q(3)
 )−1 = 3(r+1)k − 1
3(r+1)k − 1 = 1.

Thus (3k − 1)p(3) = (3(r+1)k − 1)q(3), and it follows from Lemma 2.3 that (x
k − 1)p(x) = (x
(r+1)k − 1)q(x).

Again, a simple example with p(x), q(x) ∈ P comes from taking q(x) = 1.

In Part 3, assume 32rk − 3(2r−1)k + · · · − 3k + 1 = p(3)
q(3) , and consider the polynomials (x
k + 1)p(x) and

(x
(2r+1)k + 1)q(x). The coeﬃcients of these products are in {0, 1, 2}. As in the proof of Part 2, we take the

quotient of these two polynomials at x = 3 and use the hypothesis regarding p(3)
q(3) to obtain

(3k + 1)p(3) = (3(2r+1)k + 1)q(3).

Again by Lemma 2.3, it follows that (x
k + 1)p(x) = (x
(2r+1)k + 1)q(x). As an example, take q(x) = x
k + 1.

Then p(x) = x
(2r+1)k + 1, and we can see that p(x), q(x) ∈ P, and p(x)
q(x) = x
2rk − x
(2r−1)k + · · · − x
k + 1.

12

Lastly, in Part 4, assume 3r − 3s + 1 = p(3)
q(3) , and consider the polynomials p(x) and (x
r − x
s + 1)q(x). By

hypothesis p(x), q(x) ∈ P, so we can write q(x) = v∑

j=0 x
bj , and

(x
r − x
s + 1)q(x) = (x
r + 1)
 

 v∑

j=0 x
bj
 

 − x
s
 

 v∑

j=0 x
bj
 

 .

We see that (x
r − x
s + 1)q(x) is the diﬀerence of a polynomial with coeﬃcients in {0, 1, 2} and a polynomial

with coeﬃcients in {0, 1}, so the coeﬃcients of (x
r − x
s + 1)q(x) are in {−1, 0, 1, 2}. Since p(3) = (3r − 3s +

1)q(3), we can use Lemma 2.3 one ﬁnal time to conclude that p(x) = (x
r − x
s + 1)q(x). Finally, an example

comes from taking q(x) = x
r−1 + · · · + x + 1, and then p(x) = x
2r−1 + · · · + x
r+s + x
s−1 + · · · + x + 1. □

Among the integers congruent to 1 mod 3 and less than or equal to 121, the following are covered by one

or more of the parts of Theorem 2.4 and thus have only universal representations: 4, 7, 10, 13, 19, 25, 28,

40, 55, 61, 73, 79, 82, 91, 121. The integers in intervals excluded by Theorem 1.2 are 16, 43, 46, 49, 52. This

leaves open 22, 31, 34, 37, 58, 64, 67, 70, 76, 85, 88, 94, 97, 103, 106, 109, 112, 115, 118. The ﬁrst open two

have quite diﬀerent behavior; as we shall see in Section 3.1, 22 has only local representations, but we already

know from Example 1.3 that 31 can go either way!

2.3. Integers of the form 3n − 2. Here we describe the representations of integers of the form m = 3n − 2,

where n ≥ 3. First note that any integer of this form is covered by Theorem 2.4 Part 4, since 3n−2 = 3n−3+1.

Hence we know that all representations of such an integer must be universal. We now describe all possible

representations for m = 3n − 2 and give the speciﬁc polynomials p(x) and q(x) such that m = p(3)
q(3) .

Suppose that m = 3n − 2 = p(3)
q(3) , where p(x) = 1 + w−1∑

i=1 cix
i + x
w and q(x) = 1 + s−1∑

i=1 dix
i + x
s with

ci, di ∈ {0, 1}. Let g(x) := p(x)
q(x) ∈ Z[x]. Then by Theorem 1.2, we know

2
3 · 3w−s < 3n − 2 < 3
2 · 3w−s,

so n = w − s = deg g(x).

Since the constant terms and the coeﬃcients of x
w in p(x) and x
s in q(x) are 1, we may then write

g(x) = 1 + n−1∑

i=1 eix
i + x
n. Equating coeﬃcients of powers of x in p(x) = g(x)q(x) now gives the system of

equations
 ci =
 



di + ei if i = 1,

di + i−1∑

j=1 di−j ej + ei if 1 < i < n,

di + i−1∑

j=1 di−j ej + 1 if i = n,

di + n−1∑

j=1 di−j ej + di−n if n < i ≤ w.

We now use this system of equations to determine the coeﬃcients ci, di, and ei in the polynomials p(x), q(x),

and g(x). We will approach this in sections:

• We ﬁrst consider the coeﬃcients corresponding to i = 1 and then 2 ≤ i ≤ n − 1.

13

• Next, we consider the coeﬃcients corresponding to i = n.

• After dealing with i = n, we reach a point where we can choose either to continue toward the end

of the algorithm or to carry the value m−1
2 repeatedly before continuing. We consider the choice of

carrying m−1
2 repeatedly k times, for n + 1 ≤ i ≤ n + k.

• We then consider the remaining coeﬃcients, when n + k < i.

We begin by considering g(3). Since

3n − 2 = g(3) = 1 + 3e1 + 9e2 + 27e3 + · · · + 3n−1en−1 + 3n,

−3 = 3e1 + 9e2 + 27e3 + · · · + 3n−1en−1,

−1 = e1 + 3e2 + 9e3 + · · · + 3n−2en−1,

so e1 ≡ 2 (mod 3). Since e1 = c1 − d1, we see c1 = 0, d1 = 1, and e1 = −1. Next observe that 3e2 ≡ 0

(mod 9), so e2 ≡ 0 (mod 3). The second equation in our system is c2 = d2 − 1 + e2. Since c2, d2 ∈ {0, 1},

we must have c2 = 0, d2 = 1, and e2 = 0.

Suppose that 2 ≤ i ≤ n − 1 and that for all j with 2 ≤ j < i, we have cj = 0, dj = 1, and ej = 0. Consider

the i-th equation
 ci = di + di−1e1 + di−2e2 + · · · + d2ei−2 + d1ei−1 + ei.

This is
 ci = di + 1(−1) + 1(0) + · · · + 1(0) + 1(0) + ei,

or, more simply, ci = di − 1 + ei. We know 3i−1ei ≡ 0 (mod 3i), so ei ≡ 0 (mod 3). Then ci = 0, di = 1,

and ei = 0. Thus we have c1 = 0, d1 = 1, and e1 = −1; and c2 = · · · = cn−1 = 0, d2 = · · · = dn−1 = 1, and

e2 = · · · = en−1 = 0.

Now consider the n-th equation

cn = dn + dn−1e1 + dn−2e2 + · · · + d2en−2 + d1en−1 + 1.

This is
 cn = dn + 1(−1) + 0 + · · · + 0 + 0 + 1,

so cn = dn. We have g(x) = 1 + n−1∑

i=1 eix
i + x
n = 1 − x + x
n.

As we complete the description of representations of 3n − 2, we will refer to the digraph in Figure

3. Choosing cn = dn = 0 uniquely determines a universal representation for 3n − 2, and it is the same

representation that comes from choosing to carry m−1
6 at the ﬁrst possible opportunity after carrying m−1
2
(without ever taking the loop at the vertex m−1
2 in Figure 3). It is straightforward to prove by induction

that m−1
6 is a sum of distinct powers of 3 when m = 3n − 2, and therefore choosing to carry m−1
6 without

taking the loop leads to the immediate termination of the algorithm.

14

0 1m − 3

2
 m − 1

2
m − 1

3 4
m − 1

6... ...

Figure 3. The subgraph of the multiplication transducer for m = 3n − 2 with n ≥ 3 in
base 3 that encodes all representations of m as a quotient of sums of distinct powers of 3.

We now show that choosing to take the loop k times for any positive integer k will still result in a universal

representation. Suppose we choose cn = dn = 1. Then the (n + 1)-th equation in our system is

cn+1 = dn+1 + dne1 + dn−1e2 + · · · + d2en−1 + d1,

which is
 cn+1 = dn+1 + 1(−1) + 0 · · · + 0 + 1,

so cn+1 = dn+1. Choose cn+1 = dn+1 = 1. The (n + 2)-th equation is

cn+2 = dn+2 + dn+1e1 + dne2 + · · · + d3en−1 + d2,

which is
 cn+2 = dn+2 + 1(−1) + 0 + · · · + 0 + 1,

so cn+2 = dn+2. In general, suppose that i ≥ 1 and for all 1 ≤ j < i, we have chosen cn+j = dn+j = 1. Then

the (n + i)-th equation is

cn+i = dn+i + dn+i−1e1 + dn+i−2e2 + · · · + di+1en−1 + di,

which is
 cn+i = dn+i + 1(−1) + 0 + · · · + 0 + 1,

so cn+i = dn+i. Suppose that for all i with 1 ≤ i ≤ k − 1, we choose cn+i = dn+i = 1. Then we have

c1 = 0, d1 = 1, and e1 = −1; and c2 = · · · = cn−1 = 0, cn = · · · = cn+k−1 = 1, d2 = · · · = dn−1 = 1, dn =

· · · = dn+k−1 = 1, and e2 = · · · = en−1 = 0. Then the (n + k)-th equation is

cn+k = dn+k + dn+k−1e1 + dn+k−2e2 + · · · + dk+1en−1 + dk,

which is
 cn+k = dn+k + 1(−1) + 0 + · · · + 0 + 1,

so cn+k = dn+k. We have now taken the loop from the vertex m−1
2 to itself k times. We choose cn+k =

dn+k = 0 to stop taking the loop and allow the algorithm to terminate. Similar arguments to those outlined

above show that cn+k+1 = · · · = cn+k+(n−1) = 1 and dn+k+1 = · · · = dn+k+(n−1) = 0. Then we use the

15

values we found for the coeﬃcients ci and di to write down the polynomials involved in the representation of

3n − 2 that corresponds to taking the loop k times. These polynomials are pk(x) = 1 + x
n + · · · + x
n+k−1 +

x
n+k+1 + · · · + x
n+k+(n−1) and qk(x) = 1 + x + · · · + x
n+k−1. We have 3n − 2 = pk(3)
qk(3) , and x
n − 2 = pk(x)
qk(x) ,

giving a universal representation for 3n − 2, and we note that we can obtain such a representation for any

positive integer k.

2.4. Representations of 100. Now let us consider m = 100, which is not covered by any of the theorems

previously established in this section. In fact, m = 100 is the smallest integer that has only universal

representations but is not covered by these theorems.

Following the algorithm for m = 100, we note that at the end of Step 1 we have a carry value of 33. As

stated in Section 1.2, whenever the carry value is a multiple of 3, we have a choice of two directions. Here, in

Step 2, we have a choice to move forward carrying either 44 or 11. We will refer to these choices in general

as a step up and a step down from the current carry value, where the step up corresponds to the choice to

add m to the carry value and record 1 · 3i into q and into p, while the step down corresponds to the choice

to record 0 · 3i into q and into p. Returning to the algorithm for 100, we see in Figure 4 that if we choose

to step up from 33 and move forward carrying 44, this will never lead us back to 0. Thus, in an eﬀort to

continue our search for representations of 100, we step down from 33 to 11.

0 33 11 37 12 4 1

44
 48 16

49
 5 35 45

15 38

46

Figure 4. The subgraph of the multiplication transducer for m = 100 that encodes all
representations of 100 as a quotient of sums of distinct powers of 3.

Continuing with the algorithm, our next carry value is 37 = 33 + 32 + 30, a sum of distinct powers of

3. According to the algorithm, we now record 100 = [1101001]3
[101]3 , where the rightmost three digits in both

the numerator and denominator come from the three steps carrying 0, then 33, then 11, and the remaining

bold digits in the numerator come from appending [1101]3, the base 3 expansion of 37, to p. We have

16

100 = 3
6+3
5+3
3+1
32+1 , and with p(x) = x
6 + x
5 + x
3 + 1 and q(x) = x
2 + 1, this is 100 = p(3)
q(3) . Is this a universal

representation or a local representation? Since p(x) = (x
4 + x
3 − x
2 + 1)q(x), this representation is universal.

As soon as we reach a carry value that is a sum of distinct powers of 3, in this case the carry value 37, the

algorithm takes the shortest possible path back to 0 by always choosing to step down when the carry value

is congruent to 0 mod 3. We could obtain other indecomposable representations of 100 by deviating from

the algorithm and instead choosing to step up from 12, possibly repeatedly, and each step up from 12 would

create a two-step loop in the journey back to 0. In fact, we could obtain inﬁnitely many indecomposable

representations in this fashion. Would they be all universal, all local, or some of each?

Theorem 2.5. Every indecomposable representation of 100 is universal. Moreover, for any indecomposable

representation of 100 as p(3)
q(3) , the quotient p(x)
q(x) is x
4 + x
3 − x
2 + 1.

Proof. As noted above, taking a step up from 33 does not lead to a representation of 100. Also noted above,

if we step down the ﬁrst time we encounter a carry value of 12, we obtain a universal representation. Instead,

suppose that when we ﬁrst encounter a carry value of 12, we step up from 12 to 37, follow the two-step loop

exactly once, and then continue as usual. This yields the recorded quotient

100 = [110111001]3
[010101]3 = 38 + 37 + 35 + 34 + 33 + 1
34 + 32 + 1 .

If we step up from 12 to 37 exactly twice and then continue, we record

100 = [11011111001]3
[01010101]3 = 310 + 39 + 37 + 36 + 35 + 34 + 33 + 1
36 + 34 + 32 + 1 .

To generalize, after stepping up from 12 to 37 exactly j times, which means taking the two-step loop in

Figure 4 exactly j times, we have

100 =
 34+2j+2 + 34+2j+1 +
 4+2j−1∑

k=4 3k + 33 + 1

j∑

i=1 32+2i + 32 + 1
 .

For any j ≥ 0, let pj(x) = x
4+2j+2 + x
4+2j+1 + 4+2j−1∑

k=4 x
k + x
3 + 1 and qj(x) = j∑

i=1 x
2+2i + x
2 + 1. We will

show by induction that pj(x) = (x
4 +x
3 −x
2 +1)qj(x) for any j ≥ 0. For the base case, note that when j = 0,

we have p0(x) = x
6 + x
5 + x
3 + 1 and q0(x) = x
2 + 1, so p0(x) = (x
4 + x
3 − x
2 + 1)q0(x). Suppose that t is a

non-negative integer with pt(x) = (x
4 +x
3−x
2+1)qt(x). We will show that pt+1(x) = (x
4+x
3−x
2+1)qt+1(x)

to complete the proof. First note that

(x
4 + x
3 − x
2 + 1)qt+1(x) = (x
4 + x
3 − x
2 + 1)
 (t+1∑

i=1 x
2+2i + x
2 + 1
)

= (x
4 + x
3 − x
2 + 1)
 (
x
2+2(t+1) +
 t∑

i=1 x
2+2i + x
2 + 1
)

= (x
4 + x
3 − x
2 + 1)(x
2+2t+2) + pt(x).

17

Now observe that pt(x) = x
4+2t+2 + x
4+2t+1 + 4+2t−1∑

k=4 x
k + x
3 + 1, while

pt+1(x) = x
4+2(t+1)+2 + x
4+2(t+1)+1 +
 4+2(t+1)−1∑

k=4 x
k + x
3 + 1

= x
4+2t+4 + x
4+2t+3 + x
4+2t+1 + x
4+2t +
 4+2t−1∑

k=4 x
k + x
3 + 1

= x
4+2t+4 + x
4+2t+3 + x
4+2t+1 + x
4+2t +
 4+2t−1∑

k=4 x
k + x
3 + 1 + (x
4+2t+2 − x
4+2t+2)

= x
4+2t+4 + x
4+2t+3 − x
4+2t+2 + x
4+2t + pt(x)

= x
4+2t(x
4 + x
3 − x
2 + 1) + pt(x).

Thus pt+1(x) = (x
4 + x
3 − x
2 + 1)qt+1(x), and our proof by induction is complete.

Since we have considered all indecomposable representations of 100, we conclude that every indecompos-

able representation of 100 is universal. □

Theorem 2.6. Every representation of 100 is universal. Moreover, for any representation of 100 as p(3)
q(3) ,

the quotient p(x)
q(x) is x
4 + x
3 − x
2 + 1. This includes both indecomposable and decomposable representations.

Proof. We have addressed the indecomposable representations of 100 in Theorem 2.5, so it remains to

consider the decomposable representations of 100. Suppose we have a representation of 100 resulting from

the concatenation of two indecomposable walks through the digraph with no loops at 0 occurring between

the two walks. On the ﬁrst indecomposable walk, we step up from 12 to 37 exactly j times, and on the

second indecomposable walk, we step up from 12 to 37 exactly k times.

The contributions to p(x) and q(x) coming from this ﬁrst indecomposable walk are pj(x) and qj(x), as

deﬁned in the proof of Theorem 2.5, while the contributions coming from the second indecomposable walk

are x
2j+7pk(x) and x
2j+7qk(x). Note that there are a total of 2j + 7 steps in the ﬁrst indecomposable

walk, so the second indecomposable walk begins recording powers of 3 starting with 32j+7. Thus, for the

representation of 100 resulting from two indecomposable walks, we have p(x) = x
2j+7pk(x) + pj(x) and

q(x) = x
2j+7qk(x) + qj(x).

Note that
 (x
4 + x
3 − x
2 + 1)q(x) = (x
4 + x
3 − x
2 + 1) (
x
2j+7qk(x) + qj(x)
)

= x
2j+7(x
4 + x
3 − x
2 + 1)qk(x) + (x
4 + x
3 − x
2 + 1)qj(x)

= x
2j+7pk(x) + pj(x)

= p(x).

Thus q(x) | p(x), and this representation of 100 must be universal.

18

What if a representation results from concatenating not just two indecomposable walks through the

digraph but n indecomposable walks with no loops at 0 between any two walks? Let i1, i2, . . . in be the non-

negative integers such that ih is the number of times we step up from 12 to 37 on the hth indecomposable

walk through the digraph. Then we have

p(x) = x
2(i1+i2+···+in−1)+7(n−1)pin (x) + x
2(i1+i2+···+in−2)+7(n−2)pin−1(x) + · · ·

+ x
2(i1+i2)+7(2)pi3 (x) + x
2i1+7pi2 (x) + pi1 (x)

=
 n∑

j=1 x
2aj +7(j−1)pij (x),

where aj = j−1∑

k=1 ik, and

q(x) = x
2(i1+i2+···+in−1)+7(n−1)qin (x) + x
2(i1+i2+···+in−2)+7(n−2)qin−1 (x) + · · ·

+ x
2(i1+i2)+7(2)qi3 (x) + x
2i1+7qi2 (x) + qi1 (x)

=
 n∑

j=1 x
2aj +7(j−1)qij (x).

Each pair of polynomials pih (x) and qih (x) gives an indecomposable representation of 100 as 100 = pih (3)
qih (3) ,

so from Theorem 2.5, we have pih (x) = (x
4 + x
3 − x
2 + 1)qih (x) for each ih. Then we see that

(x
4 + x
3 − x
2 + 1)q(x) = (x
4 + x
3 − x
2 + 1)
 n∑

j=1 x
2aj +7(j−1)qij (x)

=
 n∑

j=1 x
2aj +7(j−1)(x
4 + x
3 − x
2 + 1)qij (x)

=
 n∑

j=1 x
2aj +7(j−1)pij (x)

= p(x).

Thus q(x) | p(x), and this representation of 100 must be universal.

We conclude by proving that adding loops at 0 between any two indecomposable walks results in new

representations of 100 which are also universal. Consider p(x) = ∑h x
bh pih (x) and q(x) = ∑h x
bh qih (x),

where i1, i2, . . . in are as above and b1, b2, . . . bn are non-negative integers. Then by Lemma 2.2, we see that

p(x) = (x
4 + x
3 − x
2 + 1)q(x) as well. Therefore, since adding loops at 0 changes only the powers bh of x in

p(x) and q(x), we see that representations of 100 including loops at 0 are still universal. As an example, if

we take ℓ loops at 0 between walk id and walk id+1, the resulting polynomials p(x) and q(x) yield

(x
4 + x
3 − x
2 + 1)q(x) = (x
4 + x
3 − x
2 + 1)
 

 d∑

j=1 x
2aj +7(j−1)qij (x) +
 n∑

j=d+1 x
2aj +7(j−1)+ℓqij (x)





19

=
 d∑

j=1 x
2aj +7(j−1)(x
4 + x
3 − x
2 + 1)qij (x)

+
 n∑

j=d+1 x
2aj +7(j−1)+ℓ(x
4 + x
3 − x
2 + 1)qij (x)

=
 d∑

j=1 x
2aj +7(j−1)pij (x) +
 n∑

j=d+1 x
2aj +7(j−1)+ℓpij (x)

= p(x).

Hence all representations of 100 are universal. □

3. Integers with local representations

As we have seen in Examples 1.3 and 1.4, some integers m ≡ 1 (mod 3) have local representations in

addition to a trivial universal representation. In this section, we identify several other examples of integers

with local representations. Speciﬁcally, in Section 3.1, we restrict our attention to integers m with only

local representations, and in Section 3.2, we show that m = 64 has both local representations and nontrivial

universal representations.

3.1. Integers with only local representations. Some integers m ≡ 1 (mod 3) have only local represen-

tations. Here we prove that all representations of m = 22 and m = 34 are local, and we list many more

integers m whose representations are all local.

Theorem 3.1. There do not exist p(x), q(x) ∈ P with q(x) | p(x) such that 22 = p(3)
q(3) ; that is, all represen-

tations of 22 are local, including both decomposable and indecomposable representations.

Proof. Suppose to the contrary that 22 = p(3)
q(3) , where p(x), q(x) ∈ P and g(x) := p(x)
q(x) ∈ Z[x]. Let r =

deg p(x) and s = deg q(x). By Theorem 1.2,

2
3 · 3r−s < 22 < 3
2 · 3r−s,

which implies r − s = deg g(x) = 3. Since the constant terms and the coeﬃcients of x
r in p(x) and x
s in q(x)

are 1, we may then write g(x) = 1 + e1x + e2x
2 + x
3. It is now convenient to take p(x) = 1 + r−1∑

i=1 cix
i + x
r

and q(x) = 1 + s−1∑

i=1 dix
i + x
s, where ci, di ∈ {0, 1}. The equation p(x) = g(x)q(x) thus implies that

c1 = d1 + e1,

c2 = d2 + d1e1 + e2,

c3 = d3 + d2e1 + d1e2 + 1.

Since 22 = g(3) = 1 + 3e1 + 9e2 + 27, we have e1 + 3e2 = −2, and so e1 ≡ 1 (mod 3). But e1 = c1 − d1

and c1, d1 ∈ {0, 1}, so we must have that c1 = 1, d1 = 0, and e1 = 1. Thus 3e2 = −3, so e2 = −1 and

20

g(x) = x
3 − x
2 + x + 1. Note that g(3) = 22. The remaining two equations become

c2 = d2 + 0 · 1 + (−1) = d2 − 1,

c3 = d3 + d2 · 1 + 0 · (−1) + 1 = d3 + d2 + 1.

It follows from the ﬁrst of these two equations that c2 = 0 and d2 = 1. It then follows from the second

equation that c3 = d3 + 2, which is impossible. □

We can implement the same approach to prove that all representations of 34 are local, or we can instead

use Theorem 3.1 and prove the result regarding 34 as a corollary. Here we implement the latter approach.

Corollary 3.2. There do not exist p(x), q(x) ∈ P with q(x) | p(x) such that 34 = p(3)
q(3) ; that is, all represen-

tations of 34 are local, including both decomposable and indecomposable representations.

Proof. Let p(x), q(x), r, and s be as in the proof of Theorem 3.1, and let h(x) := p(x)
q(x) ∈ Z[x]. Again,

2
3 · 3r−s < 34 < 3
2 · 3r−s,

which implies r − s = deg h(x) = 3, and we will continue following the same procedure as in the proof of

Theorem 3.1. Now 34 = h(3) = 1 + 3e1 + 9e2 + 27, so e1 + 3e2 = 2 and e1 ≡ 2 (mod 3). But e1 = c1 − d1

and c1, d1 ∈ {0, 1}, so we have that c1 = 0, d1 = 1, and e1 = −1. Thus e2 = 1 and h(x) = x
3 + x
2 − x + 1.

At this point, our argument diverges from that in the proof of Theorem 3.1. Write p(x) = m∑

k=0 x
ak and

q(x) = n∑

ℓ=0 x
bℓ . We have q(x)(x
3 + x
2 − x + 1) = p(x). Now reverse the polynomials by taking x ↦→ 1/x and

multiplying q(x) by x
s, h(x) by x
3, and p(x) by x
r to obtain

(3.1)
 ( n∑

ℓ=0 x
s−bℓ )
 (x
3 − x
2 + x + 1) =
 m∑

k=0 x
r−ak .

Note that x
3h ( 1
x ) = g(x), where g(x) is as in the proof of Theorem 3.1. Since the polynomials x
sq ( 1
x )

and x
rp ( 1
x ) are still in P, we have already seen in the proof of Theorem 3.1 that Equation (3.1) cannot be

satisﬁed, and we have a contradiction. □

The same type of proof by contradiction that we used to prove Theorem 3.1 by examining the coeﬃcients

of p(x) and q(x) can also be used to show that the following numbers have only local representations: 34,

58, 67, 97, 103, 106, 115, 175, 178, 184, 193, 199, 202, 205, 208, 214, 229, 232, 238, 259, 265, 277, 286, 295,

298, 304, 307, 310, 313, 331, 340. Additionally, the procedure can be applied to test larger integers, but the

computations become increasingly tedious.

3.2. Integers with both nontrivial universal representations and local representations. Here we

consider m = 64 as an example of an integer that has both nontrivial universal representations and local

representations. See the digraph for m = 64 in Figure 5 for reference.

We begin by applying the algorithm as usual, stepping down from 9, and this yields 64 = 3
5+3
2+3+1
3+1 .

Letting p(x) = x
5 + x
2 + x + 1 and q(x) = x + 1, we have 64 = p(3)
q(3) . Since p(x) = (
x
4 − x
3 + x
2 + 1) q(x),

this is a universal representation of 64. Since q(x) ̸= 1, this universal representation is nontrivial.

21

0 21 28 9 3 1

24 8

29

7 2 22
 31 10

Figure 5. The subgraph of the multiplication transducer for m = 64 that encodes all
representations of 64 as a quotient of sums of distinct powers of 3.

Suppose we continued with the algorithm beyond 28, the ﬁrst carry value that is a sum of distinct powers

of 3. Would we get local representations or universal representations? The ﬁrst choice to be made occurs

when the carry value is 9. We will show that any representation of 64 that takes a step up from carrying 9

to carrying 24 upon ﬁrst arriving at the carry value 9 must be a local representation. This is true for both

decomposable and indecomposable representations, and we prove it using the same approach as in the proof

of Theorem 3.1.

Theorem 3.3. Any representation of 64 that steps up upon ﬁrst arriving at the carry value 9 is a local

representation. This holds for both decomposable and indecomposable representations.

Proof. Suppose to the contrary that 64 = p(3)
q(3) for some p(x), q(x) ∈ P, g(x) := p(x)
q(x) ∈ Z[x], and the

representation p(3)
q(3) results from stepping up upon ﬁrst arriving at the carry value 9. Let r = deg p(x) and

s = deg q(x). By Theorem 1.2, 2
3 · 3r−s < 64 < 3
2 · 3r−s,

which implies r − s = deg g(x) = 4. Since the constant terms and the coeﬃcients of x
r in p(x) and x
s in q(x)

are 1, we may then write g(x) = x
4 + e3x
3 + e2x
2 + e1x + 1. It is now convenient to take p(x) = 1 + r∑

i=1 cix
i

and q(x) = 1 + s∑

i=1 dix
i, where ci, di ∈ {0, 1}.

Since 64 = g(3) = 81 + 27e3 + 9e2 + 3e1 + 1, we have −6 = 9e3 + 3e2 + e1, and e1 ≡ 0 (mod 3). Since

e1 = c1 − d1, we see c1 = d1 and e1 = 0. After the ﬁrst step of the algorithm, we have a carry value of 21 ≡ 0

(mod 3) and thus must make a choice. As in the case of m = 100, one step, the step from 21 down to 7, does

not lead to any representations. Thus, to have a chance at actually obtaining a representation of 64, we must

22

step up from 21 to 28, and this corresponds to taking c1 = d1 = 1. Note that e1 = 0 gives −6 = 9e3 + 3e2,

so −2 = 3e3 + e2, and e2 ≡ 1 (mod 3). Since e2 = c2 − d2 − d1e1 = c2 − d2, we see c2 = 1, d2 = 0, and

e2 = 1. Then −3 = 3e3, so e3 = −1. Then c3 = d3 + d2e1 + d1e2 + e3 is c3 = d3. Since we are interested

in representations that step up from 9 to 24, we take c3 = d3 = 1. Then, substituting the values we have

already determined, c4 = d4 + d3e1 + d2e2 + d1e3 + 1 becomes c4 = d4.

Suppose c4 = d4 = 0. Then c5 = d5 + d4e1 + d3e2 + d2e3 + d1 is c5 = d5 + 2, which is a contradiction to

c5, d5 ∈ {0, 1}.

Now suppose c4 = d4 = 1. Then c5 = d5 + d4e1 + d3e2 + d2e3 + d1 is c5 = d5 + 2, which is a contradiction

to c5, d5 ∈ {0, 1}.

Since in all cases we arrive at a contradiction, we may conclude that q(x) ∤ p(x), and thus all representations

of 64 that choose the step up when ﬁrst carrying 9 are local. □

We conclude this section by discussing a speciﬁc example of a local representation of 64, one that steps

up upon ﬁrst arriving at the carry value 9.

Example 3.4. Suppose that m = 64 = p
q ∈ A/A. As usual, we start with a carry value of 0, and we choose

to add m = 64 to the carry value, record 1 · 30 into q and into p, then subtract 1 from the carry value, and

move on to Step 1. The remaining unrecorded value is (64 − 1) · 30 = 63 · 30 = 21 · 31, so the carry value at

the end of Step 1 is now 21 ≡ 0 (mod 3). As in the case of m = 100, we must make a choice. One choice, the

step from 21 down to 7, does not lead to any representations. Thus, to have a chance at actually obtaining

a representation of 64, we must step up from 21 to 28. To implement this choice, we add m = 64 to the

carry value again, record 1 · 31 into q and into p, and then subtract 1 from the carry value. The remaining

unrecorded value is (21 + 64 − 1) · 31 = 84 · 31 = 28 · 32, so the new carry value at the end of Step 2 is

28. Since 28 = 33 + 30 is a sum of distinct powers of 3, the algorithm would terminate here, and we would

append the digits of the base 3 representation 28 = [1001]3 to the left of p to get the nontrivial universal

representation 64 = [100111]3
[11]3 = 3
5+3
2+3+1
3+1 = 256
4 discussed above.

At present, we seek to characterize representations of 64 that step up upon ﬁrst arriving at the carry value

9. To obtain such a representation of 64, we must continue the algorithm instead of allowing the algorithm

to terminate in Step 2, when our carry value is 28 ≡ 1 (mod 3). To continue, we record 1 · 32 into p, subtract

1 from the carry value, and arrive at the unrecorded value (28 − 1) · 32 = 27 · 32 = 9 · 33. The new carry value

at the end of Step 3 is 9. Because we are exploring representations of 64 that step up upon ﬁrst arriving at

the carry value 9, we choose to add m = 64 to the carry value and record 1 · 33 into q and into p. Then, after

subtracting 1 from the carry value, the remaining unrecorded value is (9 + 64 − 1) · 33 = 72 · 33 = 24 · 34,

so our carry value at the end of Step 4 is 24. We choose again to add m = 64 to the carry value and record

1 · 34 into q and into p. After subtracting 1 from the carry value, we have the remaining unrecorded value

(24 + 64 − 1) · 34 = 87 · 34 = 29 · 35, so we are left with a new carry value of 29 at the end of Step 5. Since

29 ≡ 2 (mod 3), we must add m = 64 to the carry value and correspondingly record 1 · 35 into q. Then

the remaining unrecorded value is (29 + 64) · 35 = 93 · 35 = 31 · 36, so our carry value at the end of Step

6 is 31. Since 31 = 33 + 31 + 30 is a sum of distinct powers of 3, we can terminate this extension of the

23

algorithm by appending the digits of the base 3 representation 31 = [1011]3 to the left of p. This yields the

local representation
64 = [1011011111]3
[111011]3 = 39 + 37 + 36 + 34 + 33 + 32 + 3 + 1
35 + 34 + 33 + 3 + 1 = 22720
355 .

Notice that this representation is 64 = p(3)
q(3) where p(x) = x
9 + x
7 + x
6 + x
4 + x
3 + x
2 + x + 1 and q(x) =

x
5 + x
4 + x
3 + x + 1, and that q(x) ∤ p(x).

4. Catalog of knowledge

This table classiﬁes all indecomposable representations of integers m ≡ 1 (mod 3) in the intervals given

in 1.2 up to 3
2 · 35. For some integers, such as 22, 34, and 229, information is also known about decomposable

representations, as discussed for 22 in Theorem 3.1 and for 34 in Corollary 3.2. In the table, ⋆ indicates

that m has representations of that type, an empty cell indicates m does not have representations of that

type, and ? indicates that it is not known whether m has representations of that type. The only ? appears

for local representations of 289.

In addition to the techniques already discussed in this paper, another approach we employed to ﬁnd

representations of an integer m utilized Mathematica as follows. For all Newman polynomials p(x) up to

a ﬁxed degree, construct a table of the values p(3). It was computationally feasible for us to do this up to

degree 18. Search for those values p(3) which are multiples of m. If p(3) = m · t, then see if the ternary

expansion of t uses only the digits 0 and 1. If so, then t = q(3) for a Newman polynomial q(x). Finally,

check if q(x) | p(x).
 24

m universal local
1 ⋆
4 ⋆
7 ⋆
10 ⋆
13 ⋆
19 ⋆
22 ⋆
25 ⋆
28 ⋆
31 ⋆ ⋆
34 ⋆
37 ⋆ ⋆
40 ⋆
55 ⋆
58 ⋆
61 ⋆
64 ⋆ ⋆
67 ⋆
70 ⋆ ⋆
73 ⋆
76 ⋆ ⋆
79 ⋆
82 ⋆
85 ⋆ ⋆
88 ⋆ ⋆
91 ⋆
94 ⋆ ⋆
97 ⋆
100 ⋆
103 ⋆
106 ⋆
109 ⋆ ⋆
112 ⋆ ⋆
115 ⋆
118 ⋆ ⋆
121 ⋆
 m universal local
163 ⋆
166 ⋆
169 ⋆ ⋆
172 ⋆
175 ⋆
178 ⋆
181 ⋆
184 ⋆
187 ⋆ ⋆
190 ⋆ ⋆
193 ⋆
196 ⋆ ⋆
199 ⋆
202 ⋆
205 ⋆
208 ⋆
211 ⋆ ⋆
214 ⋆
217 ⋆
220 ⋆ ⋆
223 ⋆ ⋆
226 ⋆
229 ⋆
232 ⋆
235 ⋆
238 ⋆
241 ⋆
244 ⋆
247 ⋆ ⋆
250 ⋆ ⋆
253 ⋆ ⋆
256 ⋆ ⋆
259 ⋆
262 ⋆
265 ⋆
268 ⋆
271 ⋆ ⋆
274 ⋆ ⋆
277 ⋆
280 ⋆ ⋆
283 ⋆ ⋆
286 ⋆
289 ⋆ ?
292 ⋆ ⋆
295 ⋆
298 ⋆
 m universal local
301 ⋆ ⋆
304 ⋆
307 ⋆
310 ⋆
313 ⋆
316 ⋆ ⋆
319 ⋆ ⋆
322 ⋆
325 ⋆ ⋆
328 ⋆ ⋆
331 ⋆
334 ⋆ ⋆
337 ⋆ ⋆
340 ⋆
343 ⋆
346 ⋆
349 ⋆
352 ⋆ ⋆
355 ⋆ ⋆
358 ⋆
361 ⋆ ⋆
364 ⋆

25

5. Further directions

Ultimately, we want to know which integers can be written as a quotient of sums of distinct powers of

3. An additional long-term goal is to ﬁnd a complete classiﬁcation of the types of representations integers

can have as quotients of sums of distinct powers of 3. For example, we seek a complete description of the

integers congruent to 1 mod 3 in (1.2) which do not lie in A/A. This paper makes progress toward this goal

and also provides a launching point for several related questions and directions.

5.1. Properties of the Directed Graphs. In Figure 2 in Section 1.2, we introduce an example of an

expanded digraph generated as a subgraph of the multiplication transducer that performs multiplication by

m in base 3. These digraphs are worthy of study in their own right, beyond the information they encode

regarding representations of integers as quotients of sums of distinct powers of 3. For any positive integer

m = 3t + 1, deﬁne the digraph Dm as follows: The vertices of Dm are a subset of {0, . . . , ⌊m/2⌋}. There are

four kinds of directed edges in Dm. What kind of edge we see originating at a given vertex depends on the

congruence class of the given vertex modulo 3. The four kinds of edges are

{3k → k, 3k → k + t, 3k + 1 → k, 3k + 2 → k + t + 1}.

If i is in the vertex set of Dm and i → j is in the set of possible edges above, then j must also belong to the

vertex set of Dm.

This digraph Dm is the digraph produced by applying the algorithm of Section 1.2 to m, as done in Figure

2 for m = 22, in Figure 4 for m = 100, and in Figure 5 for m = 64, and the four kinds of edges correspond

to the four possible ways to move from Step i to Step i + 1 in the algorithm. Every representation of m as

p(3)
q(3) with p(x), q(x) ∈ P can be read oﬀ from the vertices in a walk from the vertex 0 to itself. When no such

walk exists, as in the case m = 529, there is no such representation. More information about these digraphs

and various related topics will appear in [1].

5.2. Extending to diﬀerent bases. It is natural to ask the questions of this paper for digital bases b ̸= 3.

If b = 2, then the standard binary representation for n, n = ∑i ai2i with ai ∈ {0, 1}, gives n = p(2), where

p(x) = ∑i aix
i ∈ P.

For any b ≥ 2, local representations still exist: if p(x), q(x) ∈ P and p(x) = q(x)t(x) for t(x) ∈ Z[x], then

t(b) = p(b)
q(b) will be a quotient of sums of distinct powers of b. For example,

b2 − b + 1 = [(b − 1) 1]b = b3 + 1
b + 1 .

On the other hand, b2 ≡ 1 (mod b + 1), and

(5.1) b2b + · · · + b4 + b2 + 1
b + 1 ∈ Z.

Further, (x + 1) ∤ (
x
2b + · · · + x
4 + x
2 + 1)
, because x = −1 is not a root of the polynomial on the right.

Thus, for every base b, there are local representations of quotients of distinct sums of powers of b; for b = 3,

(5.1) is a local representation of 729+81+9+1
3+1 = 205.
 26

The phrase “quotients of sums of distinct powers of b” may be rewritten as “quotients of integers with

base b representations using only digits from {0, 1}.” Written this way, we can extend our work to ask

similar questions for diﬀerent sets of digits when b ≥ 3. The fourth-named author studied generalizations of

this problem in her dissertation [10], exploring quotients of integers which, when written in base b, have a

restricted digit set.
 6. Acknowledgments

The second author was supported by an AMS-Simons Travel Grant. The third and fourth authors wish

to acknowledge the warm hospitality of the Department of Mathematics of the University of Texas at Tyler

during a visit in June 2022.
 References

[1] K. Anders, M. Dawsey, B. Reznick, and S. Sisneros-Thiry, Digraphs for representations of integers as quotients of sums

of distinct powers of three, in preparation.

[2] J. Athreya, B. Reznick, and J. Tyson, Cantor set arithmetic, American Mathematical Monthly, 126 (2019), 4–17

(MR3904605, arXiv:1711.08791).

[3] J. H. Bai, J. Meleshko, S. Riasat, and J. Shallit, Quotients of Palindromic and Antipalindromic Numbers,

arXiv:22021.13694v1.

[4] F. Blanchard, J. M. Dumont, and A. Thomas, Generic sequences, transducers and multiplication of normal numbers, Israel

Journal of Mathematics, 80(3) (1992), 257–287.

[5] S. Haque, email to the third and fourth authors, May 26, 2017.

[6] J. Loxton and A. van der Poorten, An awful problem about integers in base four, Acta Arith., 49 (1987), 193–203.

MR0928637 (89m:11004).

[7] A. Odlyzko and B. Poonen, Zeros of polynomials with 0,1 coeﬃcients, Enseign. Math. (2) 39 (1993), no. 3-4, 317–348,

MR1252071 (95b:11026).

[8] Online Encyclopedia of Integer Sequences, https://oeis.org/ consulted August 11, 2023.

[9] B. Reznick, Quotients of sums of distinct powers of three, presentation at AMS Central Sectional Meeting, Loyola-Chicago,

October 3, 2015, https://faculty.math.illinois.edu/reznick/loyola-10315Fc.pdf.

[10] S. Sisneros-Thiry, Combinatorial number theory through diagramming and gesture, Thesis (Ph.D.) University of Illinois at

Urbana-Champaign. 2020.

University of Texas at Tyler

Email address: kanders@uttyler.edu

University of Texas at Tyler

Email address: mdawsey@uttyler.edu

University of Illinois at Urbana-Champaign

Email address: reznick@illinois.edu

California State University- East Bay

Email address: simone.sisnerosthiry@csueastbay.edu
 27
