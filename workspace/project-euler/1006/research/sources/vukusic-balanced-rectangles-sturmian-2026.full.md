<!-- source: https://arxiv.org/pdf/2602.12801 | converted from PDF -->

BALANCED RECTANGLES OVER STURMIAN WORDS AND MINIMAL
DISCREPANCY INTERVALS

INGRID VUKUSIC

Abstract. We consider m × n rectangular matrices formed from Sturmian words with
slope α, and we fully characterise their balance properties in terms of the Ostrowski
representations of m and n with respect to α. This generalises recent results by Anselmo
et al., as well as those by Shallit and the author, where only quadratic irrational slopes
were considered. In contrast to the two mentioned papers, the approach in this paper is
based on the distribution of nα mod 1.

1. Introduction

Let α ∈ (0, 1) be irrational and θ ∈ [0, 1). Then the Sturmian word a = a1a2a3 · · · with
slope α and intercept θ can be defined via

(1.1) an := ⌊(n + 1)α + θ⌋ − ⌊nα + θ⌋ ∈ {0, 1}.

For example, setting α = (3 − √5)/2 and θ = 0 we get the famous infinite Fibonacci word

f = 010010100100101 · · · .

Recall that a factor is simply a contiguous block of symbols within a word, and the weight
of a factor of a binary word is the number of 1’s contained in it. One of the basic properties
of Sturmian words is that they are balanced, that is, the weights of any two factors of the
same length differ by at most 1. (For example, in the Fibonacci word above, all factors of
length 5 either contain exactly one or exactly two 1’s.) In fact, the converse holds as well:
every non-periodic balanced word is a Sturmian word.
The notion of balance was extended to multidimensional words by Berth´e and Tijde-
man [4]. In particular, they proved that in dimension larger than 1 only periodic words can
be balanced. Among other results, they also considered 2-dimensional Sturmian words and
gave a quantitative measure of their non-balancedness. Recently, Anselmo et al. [2] proved
that a certain family of rectangles of the Fibonacci word is balanced, and a full characteri-
sation was provided in [8]. Let us discuss these results in a bit more detail because the goal
of the present paper is to generalise them.
For every infinite word a = a1a2a3 · · · let us define the infinite Hankel matrix A =
(ak,ℓ)k≥1,ℓ≥0 by ak,ℓ := ak+ℓ. Then we can consider m × n submatrices where the entry in
the upper left corner has index sum i:

A(i, m, n) :=
 





 ai ai+1 . . . ai+n−1
ai+1 ai+2 . . . ai+n
... ... ...
ai+m−1 ai+m . . . ai+m+n−2





 .

The sum over all entries in the matrix A(i, m, n) equals

(1.2) T (i, m, n) :=
 m−1∑

k=0
 n−1∑

ℓ=0 ai+k+ℓ.

2020 Mathematics Subject Classification. 11J71, 68R15, 11J70.
Key words and phrases. Sturmian words, balancedness, discrepancy, Ostrowski representation, distribu-
tion modulo 1.
Research funded by the Austrian Science Fund (FWF) 10.55776/J4850.

1arXiv:2602.12801v2  [math.NT]  17 Apr 2026
2 I. VUKUSIC

Definition 1.1. Let a = a1a2a3 · · · be an infinite word over {0, 1}. We say that the m × n
rectangles of a are balanced if there exists an integer c = c(a, m, n) such that

T (i, m, n) ∈ {c, c + 1}

for all i ≥ 1.1

For example, for the Fibonacci word it turns out that the 2 × 3 rectangles are balanced
(they always have weight 2 or 3), whereas the 2 × 4 rectangles are not balanced (they can
have weight 2, 3, or 4). Anselmo et al. [2] proved that if max(m, n) is a Fibonacci number,
then the m×n rectangles of the Fibonacci word are balanced. In [8], a full characterisation of
balancedness was given in terms of the Zeckendorf representations of m, n. (The Zeckendorf
representation of a positive integer is its unique representation as the sum of distinct and
non-consecutive Fibonacci numbers). Moreover, it was described how the software Walnut
can be used to do the same for every fixed quadratic irrational α and the corresponding
representations. Note that the assumption that α is a quadratic irrational is essential for
using Walnut, since quadratic irrationals are precisely the numbers with eventually periodic
continued fraction expansion.
In this paper, we completely solve the 2-dimensional balance problem for all irrationals α.
The characterisation (Theorem 2.1 in the next section) is in terms of the Ostrowski repre-
sentations of m, n with respect to α. The proof is based on Diophantine approximation and
ideas used by Berth´e and Tijdeman [4]. Berth´e and Tijdeman also mentioned the connection
between balance and so-called bounded remainder sets, which is a concept from dynamical
systems/discrepancy theory. We provide a little bit of background, as our main result will
turn out to be equivalent to a specific statement about the distribution of nα mod 1. For
some quick intuition on this, note that (1.1) can equivalently be phrased as

an = 1 : ⇐⇒ {nα} ∈ [1 − α − θ, 1 − θ).

Here {x} = x − ⌊x⌋ denotes the fractional part of x, and the interval is understood modulo 1,
i.e., in case 1−α−θ < 0, we mean the interval that is “wrapped around 0”, [{1 − α − θ} , 1)∪
[0, 1−θ). Thus, the exact distribution of nα mod 1 contains full information on our Sturmian
sequence.
It is well known (see, e.g., [5, Chapt. 1]) that for irrational α the sequence (nα)n≥0 is
uniformly distributed modulo 1. In other words, if we consider the fractional parts {nα} for
n = 0, 1, 2, . . ., every interval I ⊆ [0, 1) gets “its fair share of points” in the following sense:

lim
N →∞ #{n : 0 ≤ n ≤ N − 1 and {nα} ∈ I}
N = |I|,

where |I| denotes the length of I. Of course, not all intervals can get “exactly their fair share
of points” if we consider finite sets of points. This is quantified by the discrepancy

DN ((nα)n≥0) = sup
I⊆[0,1]
 ∣
∣
∣
∣ #{n : 0 ≤ n ≤ N − 1 and {nα} ∈ I}
N − |I|
∣
∣
∣
∣ .

In view of this, it seems appropriate to say that an interval I has “minimal discrepancy with
respect to α and N ”, if

(1.3) ∣
∣#{n : 0 ≤ n ≤ N − 1 and {nα} ∈ I} − N |I|
∣
∣ < 1.

This again is somewhat related to bounded remainder sets, where the bound 1 is relaxed to
C but has to be satisfied for all N .
In this paper, we are interested in when all intervals of a fixed length have minimal
discrepancy for a fixed N . More specifically, the balancedness of the m × n rectangles will
turn out to be equivalent (see Theorem 3.1) to the balancedness of intervals of length {nα}
with respect to α and m, in the following sense.

1This notion of balance for rectangles appears in [6], described via “abelian complexity”.

BALANCED RECTANGLES 3

Definition 1.2. Let α, δ ∈ (0, 1) and let N ≥ 1 be an integer. We say the intervals of length
δ are balanced with respect to (α, N ) if there exists an integer c = c(α, δ, N ) such that for all
half open intervals I = [ξ, ξ + δ), 0 ≤ ξ < 1, we have

(1.4) #{n : 0 ≤ n ≤ N − 1 and {nα} ∈ I} ∈ {c, c + 1}.

Note that the intervals I are understood modulo 1, i.e., if ξ + δ ≥ 1 then the interval is
I = [ξ, 1) ∪ [0, {ξ + δ}).

It is not hard to see that (1.4) is indeed closely related to (1.3), justifying the second part
of the title of this paper.
In the next section, we state the full characterisation of balanced m × n rectangles. In
Section 3 we prove the equivalence between balanced rectangles and balanced intervals.
Then we make preparations for proving the characterisation of balanced intervals of length
{nα}: In Section 4 we rephrase balancedness in terms of bijectivity of a certain function;
in Section 5 we recall some specific properties of Ostrowski representations. Finally, in
Section 6, we prove the full characterisation of balanced m × n rectangles.
We conclude this introduction with two remarks on the parameters α and θ of Sturmian
words.

Remark 1.3. In the rest of the paper, we will assume θ = 0. This can be justified by the
following: It is a basic fact (see, e.g., [1, Theorem 10.5.3]) that two Sturmian words have the
same slope if and only if they have the same sets of factors. Since each rectangle A(i, m, n)
is fully determined by the factor ai · · · ai+m+n−2, the infinite Hankel matrices corresponding
to two Sturmian words with the same slope have exactly the same rectangles.

Remark 1.4. We will also often assume α < 1/2. It is easy to check that the Sturmian
word with slope 1 − α and intercept 0 can be obtained by flipping the digits of the Sturmian
word with slope α and intercept 0. Of course, for every pair (m, n), the m × n rectangles
of one sequence are balanced if and only if the m × n rectangles of the other sequence are.
Therefore, if α > 1/2, we can equivalently consider 1 − α < 1/2 instead.

2. Full characterisation via Ostrowski representations

In this section we state our main result, namely the full characterisation of the m × n
balanced rectangles. But first, let us briefly recall continued fractions and the Ostrowski
representation; see, e.g., [7] for a reference book.
Every irrational real number α can be uniquely represented by its infinite simple continued
fraction expansion
 α = [a0; a1, a2, . . .] = a0 + 1
a1 + 1
a2+ 1
...
 ,

where a0 is an integer and a1, a2, . . . are positive integers, called partial quotients. We can
truncate the continued fraction expansion of α at its k-th partial quotient, and obtain the
rational number pk/qk = [a0; a1, . . . , ak], called the k-th convergent to α. These convergents
are famously particularly good approximations to α. In particular, the numbers qkα are
very close to an integer (at least for large k), or, in other words, very close to 0 modulo 1.
Since we are interested in nα mod 1, the natural way to represent an integer n therefore is
to write it as the sum of qk’s, using a greedy algorithm. This is known as the Ostrowski
representation. To be precise, every positive integer n has a unique representation

n =
 N∑

k=0 bkqk

with bN ̸= 0, 0 ≤ bk ≤ ak+1 for k ≥ 1 and 0 ≤ b0 ≤ a1 − 1, and the additional rule that
bk−1 = 0 whenever bk = ak+1. For more properties of the Ostrowski representation, see
Section 5. In the rest of the paper, if we write an expression of the shape n = ∑N
k=L bkqk,

4 I. VUKUSIC

we always imply that it is a valid Ostrowski representation with respect to α, but we do not
necessarily assume bL, bN > 0.
Now we state our characterisation of balanced m × n rectangles of a Sturmian word with
slope α in terms of the Ostrowski representations of m, n. Since the infinite Hankel matrix
A = (ak,ℓ)k≥1,ℓ≥0 is symmetric, the balance problem for rectangles is symmetric, and from
now on we assume m ≤ n. Moreover, we can assume m ≥ 2 because for m = 1 the rectangles
are just the factors of the 1-dimensional Sturmian word, which are of course balanced. It
turns out that there are essentially only two situations when the rectangles with 2 ≤ m ≤ n
are balanced:

• The integer m only has small digits, and n only has large digits in its Ostrowski
representation with respect to α. In the edge case, where m and n share exactly one
digit, there are some extra conditions.

• The integer m is either the denominator of a convergent or of a semi-convergent. (A
semi-convergent is a number of the shape (pk−1 + apk)/(qk−1 + aqk) with 1 ≤ a ≤
ak+1 − 1.) Moreover, parity restrictions on the corresponding digits in n apply.

Theorem 2.1. Let α ∈ (0, 1) be irrational and 2 ≤ m ≤ n. Then the m × n rectangles of
the Sturmian words with slope α are balanced if and only if the Ostrowski representations of
m, n with respect to α are of at least one of the following four shapes.
They have “split representations” in the following sense:

(i) m = ∑M
k=0 bkqk and n = ∑N
k=M +1 bkqk;

(ii) m = ∑M
k=0 bkqk with bM ̸= 0, and n = qM + ∑N
k=M +1+2t bkqk with t ≥ 0 and
bM +1+2t ̸= 0.

The smaller number m is the denominator of a (semi-)convergent, and we have certain
parity restrictions on the large digits in n:

(iii) m = qM and n = ∑M −1
k=0 bkqk + ∑N
k=M +2t bkqk with t ≥ 0 and bM +2t ̸= 0;

(iv) m = qM −1 + aqM with 1 ≤ a ≤ aM +1 − 1 and n = ∑M −1
k=0 bkqk + ∑N
k=M +1+2t bkqk
with t ≥ 0 and bM +1+2t ̸= 0.

Example 2.2. For α = π/4 we have α = [0; 1, 3, 1, 1, 1, 15, 2, 72, . . .], and q0 = 1, q1 = 1,
q2 = 4, q3 = 5, q4 = 9, . . . . Thus, if we want to know whether the 2 × 10 rectangles are
balanced, we can use a greedy algorithm to get the Ostrowski representations

m = 2 = 2q1,

n = 10 = q4 + q1.

This falls under the case (ii) in Theorem 2.1, and so we know that the 2 × 10 rectangles are
balanced. Indeed, one can check that they always have weight 15 or 16.
On the other hand, let us consider m = 5, n = 10:

m = 5 = q3,

n = 10 = q4 + q1.

This does not correspond to any of the cases in Theorem 2.1, and indeed one can check that
the 5 × 10 rectangles can have weight 38, 39, or 40.

Remark 2.3. In Remark 1.4 we mentioned that from a balance point of view it doesn’t
matter if we consider α or 1 − α. Indeed, the same is true for the shape of the Ostrowski
representations. The next lemma implies, in particular, that the Ostrowski representations
of m, n with respect to α are of one of the four special shapes in Theorem 2.1 if and only if
those with respect to 1 − α are. Together with Remark 1.4, this allows us to assume α < 1/2
in the rest of the paper, without loss of generality.

BALANCED RECTANGLES 5

Note that for α = [0; a1, a2, . . .] we have α > 1/2 ⇐⇒ a1 = 1, in which case, by the rules
of the Ostrowski representation, we have b0 = 0. In other words, if α > 1/2, then the first
possible nonzero term in the representation is b1q1.

Lemma 2.4. Let α < 1/2 be irrational and n a positive integer. Then the Ostrowski repre-
sentation of n with respect to α is n = ∑N
k=0 bkqk if and only if the Ostrowski representation
of n with respect to 1 − α is n = ∑N +1
k=1 bk−1qk.

Proof. For α < 1/2 and α = [0; a1, a2, a3, . . .] one can check that 1 − α = [0; 1, a1 −
1, a2, a3, . . .]. Then from the recurrence formula for convergents (see also (5.1) in Section 5.1)
one can see that α and 1 − α have the same sequence of denominators q0, q1, q2, . . ., except
for the index shift. □

3. Correspondence between balancedness and low discrepancy intervals

In this section we prove the equivalence between balancedness of rectangles and balanced-
ness of intervals. We start by checking the well known fact that Sturmian words are balanced,
as the corresponding formula will be useful in a moment. We can directly compute the weight
of a factor of length n starting at index i by using (1.1) with θ = 0 and telescoping:

ai + ai+1 + · · · + ai+n−1 = ⌊(i + n)α⌋ − ⌊iα⌋

= ⌊nα⌋ +
 {
1, if {nα} + {iα} ≥ 1;
0, else.

(3.1)

Therefore, the weight of every factor of length n is either ⌊nα⌋ or ⌊nα⌋ + 1, and in particular
the factors of length n are balanced for every n.
We can now use this to compute T (i, m, n) (defined in (1.2)) by summing over the rows of
A(i, m, n). Note that the conditional expression in (3.1) can be expressed using the indicator
function in the following way: 1 [1−{nα},1)({iα}).
Thus, we obtain
 T (i, m, n) =
 m−1∑

ℓ=0 (ai+ℓ + ai+ℓ+1 + · · · + ai+ℓ+n−1)

= m⌊nα⌋ +
 m−1∑

ℓ=0 1 [1−{nα},1)({(i + ℓ)α}).

Of course, the value of m⌊nα⌋ is independent of i, and so the m × n rectangles are balanced
if and only if the sum
 S(i, m, n) :=
 m−1∑

ℓ=0 1 [1−{nα},1)({(i + ℓ)α})

takes exactly two values for all i. This and the fact that iα mod 1 is dense in [0, 1) lead to
the following theorem. (Recall Definition 1.2 for the balancedness of intervals.)

Theorem 3.1. Let a be a Sturmian word with slope α. Then the m × n rectangles are
balanced if and only if the intervals of length {nα} are balanced with respect to (α, m).

Proof. As explained above, the m×n rectangles are balanced if and only if the sum S(i, m, n)
is balanced as a sequence indexed by i. Note that we can rewrite S(i, m, n) as

S(i, m, n) =
 m−1∑

ℓ=0 1 [1−{nα}−{iα},1−{iα})({ℓα}).

In other words, the m×n rectangles are balanced if and only if for every i ≥ 1 the interval [1−
{nα}−{iα} , 1−{iα}) contains either c or c+1 of the points {0} , {α} , {2α} , . . . , {(m − 1)α}
for some fixed c. Here, and everywhere else, the intervals are understood modulo 1. Thus,

6 I. VUKUSIC

the balancedness of the intervals of length {nα} with respect to (α, m) clearly implies the
balancedness of the m × n rectangles.
For the reversed implication let [ξ, ξ + {nα}) be an arbitrary interval of length {nα}. If
[ξ, ξ + {nα}) contains none of the points {ℓα} with 0 ≤ ℓ ≤ m − 1, set ε1 := 1. Otherwise,
set ε1 := min
0≤ℓ≤m−1 {ξ + {nα} − {ℓα}} ,

i.e., ε1 is the distance between the right endpoint of the interval and the rightmost point
{ℓα} contained in the interval. Similarly, set

ε2 := min
0≤ℓ≤m−1
{ℓα}̸=ξ {ξ − {ℓα}} ,

i.e., ε2 is the distance between the left endpoint of the interval and the closest point {ℓα}
lying strictly to the left of the interval. Set ε := min{ε1, ε2} and recall that iα mod 1 is
dense in [0, 1). Thus, there exists an i ≥ 1 such that 1 − {nα} − {iα} ∈ (ξ − ε, ξ]. Then,
by construction, the interval [ξ, ξ + {nα}) contains exactly the same points as the interval
[1 − {nα} − {iα} , 1 − {iα}). Therefore, the balancedness of the m × n rectangles implies the
balancedness of the intervals of length {nα}. □

Remark 3.2. As mentioned before, since the infinite Hankel matrix A = (ak,ℓ)k≥1,ℓ≥0 is
symmetric, the balance problem for rectangles is symmetric. From Theorem 3.1 we imme-
diately get the following fact: Let m, n ≥ 1 be integers. Then the intervals of length {mα}
are balanced with respect to (α, n) if and only if the intervals of length {nα} are balanced
with respect to (α, m).

Remark 3.3. In view of Theorem 3.1, some of the cases of Theorem 2.1 become quite ob-
vious, provided one is familiar with the basic properties of Ostrowski representations. For
example, the cases (i) and (ii), where n has only large digits, correspond to the intervals of
length {nα} being extremely short (or extremely long, but then one can think of the comple-
ments). In fact, it is not very hard to prove that in the cases (i) and (ii) the corresponding
intervals each contain at most one point, and thus they are balanced.
For some of the other cases, one can use other known tricks as well. For example, if
m = qM , the points {ℓα}, for 0 ≤ ℓ ≤ m − 1, are particularly evenly distributed and one
can use the trick that α ≈ pM /qM , and therefore {ℓα} ≈ (ℓpM mod qM )/qM , to characterise
balancedness.
Overall, one can say that the intervals are balanced in the two following cases: Either
the intervals are very short (or very long); this corresponds to the cases (i) and (ii) in
Theorem 2.1. Or the points are very evenly distributed, and the interval lengths are slightly
longer (or slightly shorter) than the distance between certain two points; this corresponds
to the cases (iii) and (iv) in Theorem 2.1.
In this paper we want to deal with all cases in a somewhat uniform way. To that aim,
we rephrase balancedness of intervals in terms of bijectivity of a certain map f∗. This is
done in the next section. Later, we will rephrase the bijectivity of f∗ again in terms of
another function, which is more closely related to approximation properties of Ostrowski
representations.
 4. Balanced intervals and certain bijective maps

We start by defining balancedness of intervals in a slightly more general setting because
this makes the arguments clearer. Note that, as before, all intervals are understood modulo
1. To make this more rigorous, we speak of the torus T = R/Z, which can be thought of as
the interval [0, 1), where we compute modulo 1.

Definition 4.1. Let B = {ξ0, ξ1, . . . , ξm−1} be a set of m distinct points on the torus T and
let δ ∈ (0, 1). We say that the intervals of length δ are balanced with respect to B if there

BALANCED RECTANGLES 7

exists an integer c = c(B, δ) such that for all ξ ∈ T we have

#([ξ, ξ + δ) ∩ B) ∈ {c, c + 1}.

The goal of this section is to find a way to determine this balance property without
actually counting the points in each interval. This morally corresponds to the idea in [8,
Lemma 1]. The first step is to focus on the intervals [ξℓ, ξℓ + δ) for 0 ≤ ℓ ≤ m − 1 and to find
the closest points ξj ∈ B to the left and to the right of ξℓ + δ. We define the corresponding
functions in terms of the indices of the points.

Definition 4.2. Let B = {ξ0, ξ1, . . . , ξm−1} ⊆ T be a set of m distinct points and let
δ ∈ (0, 1). Then we define the following two maps on the set {0, 1, . . . , m − 1}: fleft maps ℓ
to the index of the closest point in B that lies to the left of ξℓ + δ, and fright maps ℓ to the
index of the closest point in B that lies to the right of ξℓ + δ. In other words,

fleft(ℓ) = j : ⇐⇒ ξℓ + δ − ξj = min
0≤i≤m−1
(ξℓ + δ) − ξi,

fright(ℓ) = j : ⇐⇒ ξj − (ξℓ + δ) = min
0≤i≤m−1 ξi − (ξℓ + δ),

where everything is taken modulo 1 and then ordered in the usual way in [0, 1).

Now in the case that the interval length δ does not match the distance between any two
points in B, we have the following main lemma.

Lemma 4.3. Let B = {ξ0, ξ1, . . . , ξm−1} ⊆ T be a set of m distinct points. Moreover, let
δ ∈ (0, 1) be such that δ ̸= ξi − ξj for all i, j. Then the following statements are equivalent:

(a) The intervals of length δ are balanced with respect to B.

(b) The function fleft is bijective on {0, 1, . . . , m − 1}.

(c) The function fright is bijective on {0, 1, . . . , m − 1}.

Proof. Assume without loss of generality that 0 ≤ ξ0 < ξ1 < · · · < ξm−1 < 1. Moreover, in
the following we use the notation ξm := ξ0.
Start with the interval [0, δ) and observe what happens as we shift it continuously to the
right, i.e., consider [ξ, ξ + δ) ⊂ T as ξ runs through [0, 1]. Every time ξ increases from ξℓ to
ξℓ + ε for some ℓ and small ε > 0, we “lose” the point ξℓ. Every time ξ increases from ξj − δ
to ξj − δ + ε for some j, we “gain” the point ξj. Since δ ̸= ξj − ξℓ for all ℓ, j, we never gain
a point and lose a point at exactly the same time. Therefore, the intervals of length δ are
balanced if an only if, as we slide our interval across the torus, we always alternate between
gaining and losing a point. In other words, the intervals of length δ are balanced if an only
if for every ℓ there exists a unique j such that ξj lies between ξℓ + δ and ξℓ+1 + δ. (This
corresponds to the fact that as we shift from [ξℓ, ξℓ + δ) to [ξℓ+1, ξℓ+1 + δ) we lose ξℓ and then
gain ξj, before losing ξℓ+1.) Moreover, note that in this situation j = fright(ξℓ) = fleft(ξℓ+1),
and thus balancedness implies that fleft, fright are bijective.
For the other implication, note that fleft being bijective or fright being bijective each imply
that for every ℓ there exists a unique j such that ξj lies between ξℓ + δ and ξℓ+1 + δ. As
described above, this is equivalent to the intervals of length δ being balanced. □

Remark 4.4. The assumption in Lemma 4.3 that δ ̸= ξi − ξj for all i, j is necessary. For
example, consider the three points ξ0 = 0, ξ1 = 1/4, and ξ2 = 1/2, and set δ = 1/2. Then
it is easy to check that the half open intervals of length δ contain either 1 or 2 points, and
thus are balanced. However, fleft(0) = 2 = fleft(1) and fright(2) = 0 = fright(1). One can
also check that changing the definitions of fleft, fleft to contain the restriction “strictly to the
left/right” does not resolve the issue.

Remark 4.5. In our application of Lemma 4.3 in Section 6 we will have

B = {0, α, {2α} , . . . , {(m − 1)α}}

and δ = {nα} .

8 I. VUKUSIC

Then, if we assume n ≥ m, we indeed get that δ ̸= {iα} − {jα} for all 0 ≤ i, j ≤ m − 1 < n.

Finally, we state a simple lemma which will also be useful later.

Lemma 4.6. Let B = {ξ0, ξ1, . . . , ξm−1} ⊆ T be a set of m distinct points and let δ ∈ (0, 1).
Then the intervals of length δ are balanced with respect to B if and only if the intervals of
length 1−δ are balanced. Moreover, if δ ̸= ξi −ξj for all i, j, then for all ε with |ε| sufficiently
small, the intervals of length δ are balanced if and only if the intervals of length 1 − δ + ε are
balanced.

Proof. The first statement is clear because the half open intervals of length 1 − δ correspond
to the complements of the intervals of length δ. If δ ̸= ξi − ξj for all i, j, then it is clear that
for |ε| < mini,j|δ − (ξi − ξj)| we can modify the interval length δ to δ + ε without changing
the occurring values of #([ξ, ξ + δ) ∩ B). □

5. Properties of convergents and Ostrowski representations

The strategy for proving our main result (Theorem 2.1) in the next section will be to
apply Lemma 4.3 to the points ξℓ = {ℓα} with 0 ≤ ℓ ≤ m − 1 and δ = {nα}. Therefore, the
right endpoints of the intervals [ξℓ, ξℓ + δ) will be of the shape {ℓα} + {nα} = {(ℓ + n)α},
where ℓ + n > m − 1. In order to determine fleft(ℓ), fright(ℓ) we will need to figure out which
point {jα} with 0 ≤ j ≤ m − 1 lies closest to the left and which one closest to the right of
{(ℓ + n)α}. We will do this using the Ostrowski representations mentioned in Section 2.
We now recall several properties of Ostrowski representations which that be useful. All
lemmas in this section are probably well known to experts (except perhaps for Lemma 5.16,
but this one is not very hard to see either). Rather unfortunately though, there does not
seem to exist a suitable reference book. In order to provide proofs for the lemmas, we recall
some basic properties of convergents first; see, e.g., [7] for a reference. Throughout the rest of
this paper, α ∈ (0, 1) is a fixed irrational, and all Ostrowski representations are with respect
to α. In fact, in view of Lemma 2.4 and Remark 2.3, we assume α < 1/2.

5.1. Basic properties of convergents

As before, let pk/qk denote the convergents to α ∈ (0, 1/2). Then the numerators and
denominators follow the recursions

p0 = 0, p1 = 1, pk+1 = ak+1pk + pk−1 for k ≥ 1;

q0 = 1, q1 = a1, qk+1 = ak+1qk + qk−1 for k ≥ 1.(5.1)

Convergents are the best approximations in the following sense: Let ∥ξ∥ := minx∈Z|ξ − x|
denote the distance to the nearest integer to ξ. Then we have

(5.2) 0 < q < qk+1 =⇒ ∥qα∥ ≥ ∥qkα∥.

We set δk := qkα − pk.

Then we have (see, e.g., [7, p. 9])

(5.3) δk = (−1)
k∥qkα∥ for k ≥ 0,

and, moreover,

(5.4) |δk| = ∥qkα∥ ≤ 1/qk+1.

In particular, since ∥qkα∥ ≤ 1/qk+1 ≤ 1/2 for k ≥ 0, we have

(5.5) {qkα} =
 {
∥qkα∥, if k is even;
1 − ∥qkα∥, if k is odd.

BALANCED RECTANGLES 9

5.2. Basic properties of Ostrowski representations

Recall that the Ostrowski representation of n with respect to α is unique and of the shape
n = ∑N
k=0 bkqk, with 0 ≤ bk ≤ ak+1 for k ≥ 1, and 0 ≤ b0 ≤ a1 − 1, and the additional rule
that bk−1 = 0 whenever bk = ak+1. The Ostrowski representation of n can be obtained by a
greedy algorithm. In particular, we have

(5.6) n =
 N∑

k=0 bkqk with bN ̸= 0 ⇐⇒ qN ≤ n < qN +1.

The Ostrowski representation is “the correct way to represent integers” in the following
sense: Roughly speaking, the digits of n with small index determine where {nα} lies in [0, 1),
and the digits with large index produce a small error term. This is plausible in view of (5.4).
Let us be more precise.
First, note that from (5.1) and (5.3) it follows that

(5.7)
 ∞∑

t=0 aL+2+2t∥qL+2t+1α∥ = ∥qLα∥,

for L ≥ 0 (recall that we are assuming α < 1/2).
Let bk(n) denote the coefficient of qk in the Ostrowski representation of n, and let k0(n)
be the index of the first nonzero coefficient in the Ostrowski representation of n, i.e.,

k0(n) := min{k : bk(n) > 0}.

The next lemma describes the fact that if k0(n) is large, then nα is close to 0 modulo 1.
In particular, this shows that indeed digits with large index only have little impact on the
position of {nα}. Later in this paper, we will need somewhat precise bounds for the size of
∥nα∥ if n only has large digits, which is why the lemma is a bit lengthy. For quick intuition,
focus on the second estimate.

Lemma 5.1. Let α ∈ (0, 1/2) and n ≥ 1 with k0(n) = L. Then

(1) ∥nα∥ > ∥qL+1α∥;

(2) ∥nα∥ < ∥qL−1α∥, provided that L ≥ 1.

Some other, more precise estimates are the following:

(3) ∥nα∥ ≥ ∥qL+1α∥ + ∥qN +2∥ if n < qN +1;

(4) ∥nα∥ > ∥qLα∥ + ∥qL+1α∥ if bL(n) ≥ 2;

(5) ∥nα∥ < ∥qL−1α∥ − ∥qN +2∥, provided that L ≥ 1 and n < qN +1;

(6) ∥nα∥ < ∥(qL−1 + qL)α∥ if bL(n) ≤ aL+1 − 1 and L ≥ 1;

(7) ∥nα∥ < ∥n′α∥ if k0(n
′) = k0(n) = L and bL(n) < bL(n
′);

(8) ∥nα∥ < ∥qLα∥ if and only if the Ostrowski representation of n is of the shape n =
qL + ∑N
k=L+1+2t bkqk with t ≥ 0 and bL+1+2t > 0;

(9) ∥nα∥ ≥ ∥qLα∥ + ∥qN α∥ if qL < n < qN +1 and n is not of the shape n = qL +
∑N
k=L+1+2t bkqk with t ≥ 0 and bL+1+2t > 0.

Proof. All statements follow pretty straightforwardly from (5.3), (5.7), and the rules for
the digits of Ostrowski representations. See also, for example, [7, p. 24–25, Lemma 1 and
Theorem 1]. □

The next lemma follows from similar arguments; see, for example, [3, Lemma 4.1] for a
reference.

Lemma 5.2. Let α ∈ (0, 1/2) and n ≥ 1 and assume that k0(n) ≥ 1. Then we have

∥nα∥ =
 {{nα} , if k0(n) is even;
1 − {nα} , if k0(n) is odd.

10 I. VUKUSIC

Lemma 5.2 cannot be extended to k0(n) ≥ 0, so when the smallest allowed digit in the
representation of n shows up, then {nα} might lie on “the wrong side of 1/2”. Indeed, if
k0(n) = 0, we might have {nα} > 1/2 if b0(n) is large, even though from the parity of
k0(n) we would expect {nα} < 1/2. The next lemma will be useful when dealing with such
exceptional cases.

Lemma 5.3. Assume α < 1/2 and k0(n) = 0. Then

{nα} > 1/2 =⇒ {nα} < {(n + 1)α} .

Note that the implied statement is equivalent to ∥(n + 1)α∥ < ∥nα∥.

Proof. If n = ∑N
k=0 bkqk with b0 > 0, then we get from (5.3) and (5.7) that

{nα} ≤ {b0q0α} + {(b1q1 + . . . )α}

< {b0q0α} + {(a2q2 + a4q4 + . . . )α}

≤ {(q1 − 1)α} + {−q1α} = 1 − {α} .

Thus, {nα} + {α} < 1 and so {(n + 1)α} = {nα} + {α} > {nα}, as desired. □

5.3. One-sided approximations

For real ξ, let us define the distance to the nearest integer on the left, and the distance
to the nearest integer on the right:

⟨ξ⟩left := {ξ} and ⟨ξ⟩right := {−ξ} .

The overload of notation is justified by the fact that we will go on to focus on one of
⟨·⟩left, ⟨·⟩right at a time; see also the lemma below. Moreover, in Section 6 we will consider
the functions fleft, fright, xleft, xright, and the definition above will be compatible with those
functions. Note that if {⟨·⟩∗, ⟨·⟩∗∗} = {⟨·⟩left, ⟨·⟩right}, we have

⟨−ξ⟩∗ = 1 − ⟨ξ⟩∗ = ⟨ξ⟩∗∗, for all real non-integers ξ.

Moreover, we have the same “addition rules” as for {·}:

⟨ξ1⟩∗ + ⟨ξ2⟩∗ < 1 ⇐⇒ ⟨ξ1 + ξ2⟩∗ = ⟨ξ1⟩∗ + ⟨ξ2⟩∗;

⟨ξ1⟩∗ ≥ ⟨ξ2⟩∗ ⇐⇒ ⟨ξ1 − ξ2⟩∗ = ⟨ξ1⟩∗ − ⟨ξ2⟩∗.

We will also use the fact that

⟨ξ⟩∗ < ⟨ξ + ξ1⟩∗ < ⟨ξ + ξ2⟩∗ =⇒ ⟨ξ1⟩∗ < ⟨ξ2⟩∗.

We start with a simple lemma for the situation where ⟨nα⟩∗ > 1/2.

Lemma 5.4. Let ⟨·⟩∗ ∈ {⟨·⟩left, ⟨·⟩right}. If ⟨nα⟩∗ > 1/2, then either ⟨(n − 1)α⟩∗ < ⟨nα⟩∗ or
⟨(n + 1)α⟩∗ < ⟨nα⟩∗.

Proof. Since either ⟨α⟩∗ < 1/2 or ⟨−α⟩∗ < 1/2, we have that ⟨±α⟩∗ < 1/2 < ⟨nα⟩∗ for one
choice of ±. Then ⟨(n ∓ 1)α⟩∗ = ⟨nα⟩∗ − ⟨±α⟩∗ < ⟨nα⟩∗. □

Below, we will focus on one of ⟨·⟩left, ⟨·⟩right at a time. In fact, we will usually fix an
integer n and set

(5.8) ⟨·⟩∗ :=
 {
⟨·⟩left, if ∥nα∥ = {nα} ;
⟨·⟩right, if ∥nα∥ = 1 − {nα} .

In other words, we choose ⟨·⟩∗ such that ⟨nα⟩∗ = ∥nα∥ < 1/2.
We rephrase Lemma 5.2 in terms of ⟨·⟩∗:

Lemma 5.5. Let α ∈ (0, 1/2) and n, n′ ≥ 1 with k0(n), k0(n
′) ≥ 1. Set ⟨·⟩∗ as in (5.8).
Then ⟨n′α⟩∗ < 1/2 ⇐⇒ k0(n) ≡ k0(n
′) (mod 2).

The next two lemmas describe how we can compare ⟨nα⟩∗ and ⟨n′α⟩∗ by looking at the
first nonzero digits in n, n
′.
 BALANCED RECTANGLES 11

Lemma 5.6. Let α ∈ (0, 1/2) and n ≥ 1 and set ⟨·⟩∗ as in (5.8). Then for all n
′ ≥ 1 we
have k0(n
′) < k0(n) =⇒ ⟨nα⟩∗ < ⟨n
′α⟩∗.

Proof. If k0(n) = 0 , the implication is trivial.
Assume next that k0(n) ≥ 2. Then if k0(n
′) = k0(n) − 1, we have from Lemma 5.5
that ⟨n
′α⟩∗ > 1/2 > ⟨nα⟩∗. If k0(n
′) ≤ k0(n) − 2, then we obtain ⟨n′α⟩∗ > ⟨nα⟩∗ from
Lemma 5.1(1, 2).
We are left with the case k0(n) = 1. Lemma 5.2 implies that ⟨·⟩∗ = ⟨·⟩right. Assume
k0(n
′) = 0. If {n′α} < 1/2, then ⟨n′α⟩right > 1/2 > ⟨nα⟩right, as desired. If {n′α} > 1/2,
then as in the proof of Lemma 5.3 we see that {n′α} < 1 − {α}, and so ⟨n′α⟩right > ∥α∥ =
∥q0α∥ > ∥nα∥ = ⟨nα⟩right, where we used Lemma 5.1(2). □

Lemma 5.7. Let α ∈ (0, 1/2) and n, n
′ ≥ 1 with k0(n) = k0(n′) = L. Assume L ≥ 1 and
set ⟨·⟩∗ as in (5.8). Then

bL(n) < bL(n
′) =⇒ ⟨nα⟩∗ < ⟨n
′α⟩∗.

Proof. By our assumptions and by Lemma 5.5, we have ⟨nα⟩∗ = ∥nα∥ and ⟨n′α⟩∗ = ∥n
′α∥.
Thus, the inequality is the statement (7) in Lemma 5.1. □

Now we state the best approximation property of (semi-)convergents in the one-sided
setting.

Lemma 5.8. Let α ∈ (0, 1/2) and L ≥ 0. Let ⟨·⟩∗ ∈ {⟨·⟩left, ⟨·⟩right} be such that ⟨qLα⟩∗ <
1/2. Then

(5.9) ⟨qLα⟩∗ > ⟨(qL + qL+1)α⟩∗ > · · · > ⟨(qL + (aL+2 − 1)qL+1)α⟩∗ > ⟨qL+2α⟩∗.

Moreover, for 0 ≤ a ≤ aL+2 − 1 we have

(5.10) 0 < q < qL + (a + 1)qL+1 =⇒ ⟨qα⟩∗ ≥ ⟨(qL + aqL+1)α⟩∗.

Proof. The inequalities in (5.9) follow from (5.5) and the fact that aL+2∥qL+1α∥ < ∥qLα∥
(which follows, for example, from (5.7)).
For the best approximation property (5.10), note that all q in the range 0 < q < qL+2
which are not of the shape qL + aqL+1 with 0 ≤ a ≤ aL+2 − 1, by (5.6), must either have
k0(q) = L + 1, or k0(q) = L and bL(q) ≥ 2, or k0(q) ≤ L − 1.
If k0(q) = L + 1, then Lemma 5.2 implies ⟨qα⟩∗ > 1/2 > ⟨qLα⟩∗.
If k0(q) ≤ L − 1, then Lemma 5.6 implies ⟨qα⟩∗ > ⟨qLα⟩∗.
If k0(q) = L and bL(q) ≥ 2, then in the case L ≥ 1, Lemma 5.7 implies ⟨qα⟩∗ > ⟨qLα⟩∗.
If L = 0, this is easy to see as well.
Overall, ⟨qα⟩∗ > ⟨qLα⟩∗ holds for all q that are not of the shape qL + aqL+1, and so the
implication (5.10) follows from (5.9). □

5.4. Minimising distances in certain ranges of integers

The lemmas in this subsection will be particularly useful for characterising balancedness.

Lemma 5.9. Let α ∈ (0, 1/2) and assume that k0(n) = L with L ≥ 1. Set ⟨·⟩∗ as in (5.8).
Then ⟨(n + qL+1)α⟩∗ < ⟨nα⟩∗.
More generally, the inequality holds for all n with k0(n) ≤ L, as long as ⟨nα⟩∗ < 1/2 and
⟨qLα⟩∗ < 1/2.

Proof. This follows from the fact that ⟨nα⟩∗ = ∥nα∥ > ∥qL+1α∥ (by Lemma 5.1(1)) and
⟨qL+1α⟩∗ = 1 − ∥qL+1α∥ (by Lemma 5.5, since L and L + 1 have distinct parities). □

In the cases where L is too small for the above lemma, we will use the next two lemmas.

Lemma 5.10. Assume that k0(n) = 0 and set ⟨·⟩∗ as in (5.8). Then we have

⟨(n − q1)α⟩∗ < ⟨nα⟩∗ or ⟨(n + q1)α⟩∗ < ⟨nα⟩∗.

12 I. VUKUSIC

Proof. This follows from the fact that ⟨nα⟩∗ = ∥nα∥ > ∥q1α∥, by Lemma 5.1(1). □

Lemma 5.11. Assume b0(n) ≥ 2 and set ⟨·⟩∗ as in (5.8). Then we have

⟨(n − 1)α⟩∗ < ⟨nα⟩∗ or ⟨(n + 1)α⟩∗ < ⟨nα⟩∗.

Proof. Similarly to the proof of Lemma 5.3, one can use (5.3) and (5.7) to show that {α} <
{nα} < 1 − {α}. This implies {(n − 1)α} < {nα} < {(n + 1)α}, and so ⟨(n − 1)α⟩left <
⟨nα⟩left and ⟨(n + 1)α⟩right < ⟨nα⟩right. This proves the lemma. □

Lemma 5.12. Assume that either k0(n) ≥ L or n = qL−1 + ∑N
k=L+2t bkqk with t ≥ 0 and
bL+2t ̸= 0. Set ⟨·⟩∗ as in (5.8). Then

(5.11) ⟨nα⟩∗ = min{⟨xα⟩∗ : n − qL < x < n + qL}.

Proof. Let n be as in the statement of the lemma. If L = 0, then qL = 1, so the statement is
trivial. Otherwise, by Lemma 5.1(2, 8), we have ∥nα∥ < ∥qL−1α∥. On the other hand, by the
best approximation property of convergents (5.2), we have ∥dα∥ ≥ ∥qL−1α∥ for all 1 ≤ d <
qL. Thus, for all 1 ≤ d < qL with ⟨dα⟩∗ < 1/2, we have ⟨(n + d)α⟩∗ = ⟨nα⟩∗ + ⟨dα⟩∗ > ⟨nα⟩∗
and ⟨(n − d)α⟩∗ > 1/2 > ⟨nα⟩∗. Similarly, for all 1 ≤ d < qL with ⟨dα⟩∗ > 1/2, we have
⟨(n + d)α⟩∗ > 1/2 > ⟨nα⟩∗ and ⟨(n − d)α⟩∗ = ⟨nα⟩∗ + ∥dα∥ > ⟨nα⟩∗. This implies (5.11). □

Lemma 5.13. Let α ∈ (0, 1) and assume that k0(n) ≥ L with L ≥ 1. Set ⟨·⟩∗ as in (5.8).
Then ⟨nα⟩∗ = min{⟨xα⟩∗ : n ≤ x < n + qL−1 + qL}.
Moreover, if bL(n) ≤ aL+1 − 1, we can extend the range to

⟨nα⟩∗ = min{⟨xα⟩∗ : n ≤ x < n + qL−1 + 2qL}.

Proof. Assume first that k0(n) = L with L ≥ 1 and ⟨nα⟩∗ < 1/2. Then Lemma 5.1(2)
implies ⟨nα⟩∗ = ∥nα∥ < ∥qL−1α∥. Let ⟨·⟩∗∗ denote the distance to the nearest integer in
the opposite direction, i.e., {⟨·⟩∗, ⟨·⟩∗∗} = {⟨·⟩left, ⟨·⟩right}. Then by Lemma 5.5 we have
⟨qLα⟩∗ < 1/2 and ⟨qL−1α⟩∗∗ < 1/2.
For the sake of contradiction, assume ⟨(n + d)α⟩∗ < ⟨nα⟩∗ for some 1 ≤ d < qL−1 + qL.
This is equivalent to ⟨(n + d)α⟩∗∗ > ⟨nα⟩∗∗, and so

⟨dα⟩∗∗ = ⟨(n + d)α⟩∗∗ − ⟨nα⟩∗∗ < 1 − ⟨nα⟩∗∗ = ⟨nα⟩∗ < ∥qL−1α∥ = ⟨qL−1α⟩∗∗
for some 1 ≤ d < qL−1 + qL, contradicting Lemma 5.8 with a = 0.
If k0(n) > L, then the previous case just gives us a stronger result than necessary.
Finally, assume that k0(n) = L and bL ≤ aL+1 − 1. Then Lemma 5.1(6) says that in fact
⟨nα⟩∗ < ∥(qL−1 + qL)α∥, and we get the better bound by the same argument as before, this
time using Lemma 5.8 with a = 1. □

Next, we determine integers larger than n which minimise ⟨xα⟩∗ in certain ranges strictly
above n.

Lemma 5.14. Let α ∈ (0, 1) and L ≥ 0, and assume ⟨qLα⟩∗ < 1/2. Let n ≥ 1 and

n′ := min{x > n : ⟨xα⟩∗ < ⟨nα⟩∗}.

Moreover, let 0 ≤ a ≤ aL+2 − 1 and assume n + qL + aqL+1 < n
′. Set

u := min{n′, n + qL + (a + 1)qL+1}.

Then we have ⟨(n + qL + aqL+1)α⟩∗ = min
n<x<u⟨xα⟩∗.

Proof. First, note that the assumption n + qL + aqL+1 < n
′ implies ⟨(n + qL + aqL+1)α⟩∗ >
⟨nα⟩∗. For the sake of contradiction, assume there exists an integer x with n < x < u such
that ⟨xα⟩∗ < ⟨(n + qL + aqL+1)α⟩∗. Then, since u ≤ n
′ and u ≤ n + qL + (a + 1)qL+1, we
have in fact

(5.12) ⟨nα⟩∗ < ⟨xα⟩∗ = ⟨(n + d)α⟩∗ < ⟨(n + qL + aqL+1)α⟩∗

BALANCED RECTANGLES 13

with 0 < d < qL + (a + 1)qL+1. But (5.12) implies ⟨dα⟩∗ < ⟨(qL + aqL+1)α⟩∗, contradicting
Lemma 5.8. □

5.5. Ostrowski representations of n and qT − n

Finally, we want to describe how the shape of the Ostrowski representations of n and
qT − n are related to each other, for T sufficiently large.

Lemma 5.15. Let α ∈ (0, 1/2) and assume that k0(n) = L with L ≥ 1 and qL < n < qN +1,
but that n is not of the shape n = qL + ∑N
k=L+1+2t bkqk with t ≥ 0 and bL+1+2t > 0.
Then for T ≥ N + 2 we have that qT − n is of the shape qT − n = qL−1 + ∑T −1
k=L+2t b′
kqk
with t ≥ 0 and b
′
L+2t > 0.

Proof. Let n be as in the statement of the lemma. Then by Lemma 5.1(9) we have ∥nα∥ ≥
∥qLα∥ + ∥qN ∥ > ∥qLα∥ + ∥qT α∥, and so ∥(qT − n)α∥ > ∥qLα∥. Now Lemma 5.1(2) implies
that k0(qT − n) ≤ L. Note that {(qT − n)α} < 1/2 ⇐⇒ {nα} > 1/2. Thus, by Lemma 5.2,
k0(n) and k0(qT − n) must have distinct parities, and so in fact k0(qT − n) ≤ L − 1.
Finally, since k0(n) = L, Lemma 5.1(5) tells us that ∥nα∥ < ∥qL−1α∥ − ∥qN +2∥ ≤
∥qL−1α∥ − ∥qT ∥, and so ∥(qT − n)α∥ < ∥qL−1α∥. Thus, we get from Lemma 5.1(1, 8) that
qT − n is of the shape qL−1 + ∑T −1
k=L+2t b
′
kqk with t ≥ 0 and b′
L+2t > 0. □

In preparation for our second lemma, we introduce some more notation: For M ≥ 0 let
us define the “small part of n”, obtained by discarding terms with indices larger than M :

n[≤M ] :=
 M∑

k=0 bk(n)qk.

Note that, by (5.6), we have

(5.13) n
[≤M ] < qM +1.

Similarly, we define the “large part of n”:

n[≥M ] :=
 ∞∑

k=M bk(n)qk.

Moreover, let k≥M (n) := min{k : k ≥ M and bk(n) > 0}.

Note that this generalises our previous definition of k0(n) = k≥0(n).

Lemma 5.16. Assume that n[≤M −1] > 0 and n[≥M ] > 0. Then if qT −1 > n, we have

k≥M (n) ≡ k≥M (qT − n) (mod 2).

Proof. Note that the assumption n[≤M −1] > 0 implies that M ≥ 1. Moreover, assume
n < qN +1 and T ≥ N + 2.

Case 1: k≥M (n) ≡ M + 1 (mod 2). In particular, we have bM (n) = 0 in this case, and we
can write n = n
[≤M −1] + n[≥M +1],

and we have k0(n
[≥M +1]) = k≥M (n) ≡ M + 1 (mod 2).

Let us write
 qT − n = (qT − n[≥M +1] − qM )
︸ ︷︷ ︸
:=n′
large
 + (qM − n[≤M −1])
︸ ︷︷ ︸
:=n′
small
 .

First, note that 0 < n
′
small < qM . (This follows from the assumption n
[≤M −1] > 0 and
(5.13).) Our goal is to show that k0(n
′
large) ≥ M and k0(n
′
large) ≡ M + 1 (mod 2).

14 I. VUKUSIC

Choose ⟨·⟩∗ ∈ {⟨·⟩left, ⟨·⟩right} so that ⟨qM +1α⟩∗ < 1/2. Then by the case assumption and
Lemmas 5.1(5) and 5.2, we have

⟨n[≥M +1]α⟩∗ = ∥n
[≥M +1]α∥ < ∥qM α∥ − ∥qN +2α∥ ≤ ∥qM α∥ − ∥qT α∥.

Since, moreover, ∥qT α∥ < ⟨n[≥M +1]α⟩∗, we get that

⟨(−qT + n[≥M +1])α⟩∗ < ∥qM α∥ = 1 − ⟨qM α⟩∗.

This implies
 1 − ∥qM α∥ = ⟨qM α⟩∗ < ⟨qM α⟩∗ + ⟨(−qT + n[≥M +1])α⟩∗

= ⟨(−qT + n[≥M +1] + qM )α⟩∗ < 1,

and so ⟨n′
largeα⟩∗ = ⟨(qT − n[≥M +1] − qM )α⟩∗ < ∥qM α∥.
The fact that ∥n
′
largeα∥ = ⟨n
′
largeα⟩∗ < ∥qM α∥ implies that k0(n
′
large) ≥ M . Moreover, since
⟨qM +1α⟩∗ < 1/2, Lemma 5.5 implies that k0(n
′
large) ≡ M + 1 (mod 2).
Overall, qT − n = n
′
large + n′
small has the correct shape, namely k≥M (qT − n) ≡ M + 1
(mod 2).

Case 2: k≥M (n) ≡ M (mod 2). We want to show that k≥M (qT − n) ≡ M (mod 2) as well.
Assume the contrary, i.e.,
 k≥M (qT − n) ≡ M + 1 (mod 2).

If (qT − n)[≤M −1] > 0, then we can apply the result from Case 1 to qT − n: for n′′ :=
qT +2 − (qT − n) = n + (qT +2 − qT ) we have

(5.14) k≥M (n′′) ≡ M + 1 (mod 2).

From qT +2 − qT = aT +2qT +1 we see that n′′ and n have exactly the same digits up the digit
with index T + 1. Therefore, the congruence (5.14) contradicts the case assumption.
We are left with the case (qT − n)[≤M −1] = 0. Then k0(qT − n) ≥ M + 1. Lemma 5.1(2)
implies ∥(qT − n)α∥ < ∥qM α∥, and so ∥nα∥ < ∥qM α∥ + ∥qT α∥ ≤ ∥qM α∥ + ∥qN +2α∥. But
then Lemma 5.1(3) implies that k0(n) ≥ M , which contradicts the assumption in the lemma
that n[≤M −1] > 0. □

We combine the previous two lemmas in the way we will want to apply in the next section.

Lemma 5.17. Let α ∈ (0, 1/2) and qM < n < qN −1 for some M ≥ 1. Assume that
bM (n) > 0, and that n is not of the shape n = qM + ∑N
k=M +1+2t bkqk with t ≥ 0 and
bM +1+2t > 0. Then for T ≥ N + 2 we have k≥M (qT − n) ≡ M (mod 2).

Proof. If n
[≤M −1] > 0, then Lemma 5.16 implies that k≥M (qT −n) ≡ k≥M (n) = M (mod 2).
If n
[≤M −1] = 0, then k0(n) = M , and so Lemma 5.15 implies that k≥M (qT − n) ≡ M
(mod 2). □

6. Proof of the full characterisation

In this section, we prove our main result, namely the full characterisation of balanced
rectangles of Sturmian sequences (Theorem 2.1). As before, let α ∈ (0, 1/2) be irrational
and fix integers 2 ≤ m ≤ n. In view of Theorem 3.1, we can phrase Theorem 2.1 in terms of
balanced intervals. Moreover, as mentioned in Remark 4.5, we can use Lemma 4.3, setting

B := {ξ0, ξ1, . . . , ξm−1} with ξℓ := {ℓα} for 0 ≤ ℓ ≤ m − 1;

δ := {nα} .

This means that we need to characterise the situations when fleft and fright from Defini-
tion 4.2 are bijective (and we know from Lemma 4.3 that one is bijective if and only if the
other is bijective, so we can focus on either of them).
Recall that to describe fleft, fright, we need to find the closest points from the set B on
either side of ξℓ + δ mod 1 = {(n + ℓ)α}. In other words, we need to subtract some positive

BALANCED RECTANGLES 15

integer x from n + ℓ, so that n + ℓ − x falls into [0, m − 1], and so that {xα} causes a minimal
shift to the left or to the right.
To formalise this, we define
 xleft(ℓ) := n + ℓ − fleft(ℓ),(6.1)
 xright(ℓ) := n + ℓ − fright(ℓ),

for 0 ≤ ℓ ≤ m − 1. Note that since fleft(ℓ), fright(ℓ) ∈ [0, m − 1], we have

(6.2) xleft(ℓ), xright(ℓ) ∈ [n + ℓ − m + 1, n + ℓ] =: X(ℓ)

for 0 ≤ ℓ ≤ m − 1.
The next lemma captures the fact that {xleft(ℓ)α} and {xright(ℓ)α} must correspond to
“minimal shifts”.

Lemma 6.1. With the above definitions we have

{xleft(ℓ)α} = min
x∈X(ℓ) {xα} ,

{xright(ℓ)α} = max
x∈X(ℓ) {xα} .

Proof. This follows directly from the definitions: for xleft(ℓ) we have

{xleft(ℓ)α} (6.1)
= {ℓα + nα − fleft(ℓ)α}

Def. 4.2
= min
0≤i≤m−1 {ℓα + nα − iα}

= min
n+ℓ−m+1≤x≤n+ℓ {xα} ,

and we can check the formula for {xright(ℓ)α} analogously. □

Remark 6.2. Since {xα} ̸= {yα} for irrational α and integers x ̸= y, Lemma 6.1 gives us
an alternative definition for the functions xleft, xright.

Now we can phrase fleft, fright being bijective in terms of xleft, xright.

Lemma 6.3. Let (f∗, x∗) = (fleft, xleft) or (fright, xright). Then f∗ is bijective if and only if

x∗(ℓ) − ℓ ̸= x∗(ℓ′) − ℓ′

for all 0 ≤ ℓ < ℓ
′ ≤ m − 1.

Proof. This follows directly from the definition: We have x∗(ℓ) = n + ℓ − f∗(ℓ), which gives
us f∗(ℓ) = n + ℓ − x∗(ℓ), and so f∗(ℓ) = f∗(ℓ
′) ⇐⇒ x∗(ℓ) − ℓ = x∗(ℓ
′) − ℓ′. Since f∗ is a
map on the finite set {0, 1, . . . , m − 1}, it is injective if and only if it is bijective. Thus, f∗
is bijective if and only if f∗(ℓ) ̸= f∗(ℓ′) for all ℓ ̸= ℓ
′, and by the previous argument this is
equivalent to x∗(ℓ) − ℓ ̸= x∗(ℓ
′) − ℓ′ for all ℓ ̸= ℓ′. □

A brief recap: We want to characterise all 2 ≤ m ≤ n such that the m × n rectangles of
the Sturmian words with slope α are balanced (prove Theorem 2.1). The m × n rectangles
of the Sturmian words with slope α being balanced is equivalent to the intervals of length
{nα} being balanced with respect to (α, m) (Theorem 3.1). This again is equivalent to the
function f∗ = fleft or f∗ = fright being bijective (Lemma 4.3). And to decide whether f∗ is
bijective, we can use Lemma 6.3 and the corresponding function x∗ = xleft or x∗ = xright,
which can be defined via Lemma 6.1. Indeed, this is our strategy. In order to unify our
arguments, recall that in the previous section we defined

⟨ξ⟩left = {ξ} and ⟨·⟩right = {−ξ} .

In the rest of this section, we will always either set (f∗, x∗, ⟨·⟩∗) = (fleft, xleft, ⟨·⟩left) or
(f∗, x∗, ⟨·⟩∗) = (fright, xright, ⟨·⟩right). In either case, we can now phrase Lemma 6.1 as

⟨x∗(ℓ)α⟩∗ = min
x∈X(ℓ)
⟨xα⟩∗,

16 I. VUKUSIC

where the range X(ℓ) = [n + ℓ − m + 1, n + ℓ] was defined in (6.2). In view of this and
Lemma 6.3, we are interested in integers x in the range

[n − m + 1, n + m − 1] = ⋃

0≤ℓ≤m−1 X(ℓ)

that minimise ⟨xα⟩left or ⟨xα⟩right.
Let ̂xleft, ̂xright be the integers that minimise ⟨xα⟩left or ⟨xα⟩right, respectively, in the full
range [n − m + 1, n + m − 1]. Again, according to the setting, we will write just ̂x∗ for ̂xleft
or ̂xright. In other words, in our notation we have

⟨̂x∗α⟩∗ = min
n−m+1≤x≤n+m−1
⟨xα⟩∗.

Note that the only integer that occurs in the range X(ℓ) = [n + ℓ − m + 1, n + ℓ] for every
0 ≤ ℓ ≤ m − 1 is the integer n. Therefore, the case ̂x∗ = n is particularly easy, and we start
with this case.

6.1. The case n = ̂x∗

Lemma 6.4. Let (f∗, ̂x∗) = (fleft, ̂xleft) or (f∗, ̂x∗) = (fright, ̂xright). If ̂x∗ = n, then f∗ is
bijective.

Proof. Since ̂x∗ = n ∈ X(ℓ) = [n + ℓ − m + 1, n + ℓ] for every 0 ≤ ℓ ≤ m − 1, we have in
fact x∗(ℓ) = ̂x∗ for all 0 ≤ ℓ ≤ m − 1. Thus, x∗(ℓ) − ℓ = ̂x∗ − ℓ ̸= ̂x∗ − ℓ′ = x∗(ℓ′) − ℓ
′ for all
ℓ ̸= ℓ′, and by Lemma 6.3 the function f∗ is bijective. □

We also characterise the case ̂x∗ = n in terms of the Ostrowski representations of m, n.

Lemma 6.5. Let 2 ≤ m ≤ n with qM −1 < m ≤ qM . We have n ∈ {̂xleft, ̂xright} if and only
if the Ostrowski representation of n with respect to α is of one of the following two shapes:

(a) n = ∑N
k=L bkqk with L ≥ M ;

(b) n = qM −1 + ∑N
k=M +2t bkqk with t ≥ 0 and bM +2t ̸= 0.

Proof. Let
 n =
 N∑

k=L bkqk with bL ̸= 0.

If ⟨nα⟩∗ > 1/2 for ⟨·⟩∗ = ⟨·⟩left or ⟨·⟩∗ = ⟨·⟩right, then, by Lemma 5.4, one of ⟨(n−1)α⟩∗, ⟨(n+
1)α⟩∗ must be strictly smaller than ⟨nα⟩∗. Since n−1, n+1 are both in the range [n−m+1, n+
m − 1], we have n ̸= ̂x∗. Therefore, it suffices to consider the choice of ⟨·⟩∗ ∈ {⟨·⟩left, ⟨·⟩right}
for which ⟨nα⟩∗ < 1/2, and check whether ̂x∗ = n. We systematically go through all possible
representations of n.

Case 1: Either L ≥ M , or L = M − 1 and n = qM −1 + ∑N
k=M +2t bkqk with t ≥ 0 and
bM +2t ̸= 0. In other words, n has the representation from (a) or (b). Then Lemma 5.12 says
that n minimises ⟨nα⟩∗ in the range [n − qM + 1, n + qM − 1] ⊇ [n − m + 1, n + m − 1]. Thus,
we have indeed n = ̂x∗.

Case 2: L = M − 1 and n = qM −1 + ∑N
k=M +1+2t bkqk with t ≥ 0 and bM +1+2t ̸= 0. Set
n1 := ∑N
k=M +1+2t bkqk. By Lemma 5.2 we have ⟨n1α⟩∗ < 1/2 as well, except possibly if
M − 1 = 0. In the exceptional case (i.e., if {nα} is “on the wrong side of 1/2”), we can
apply Lemma 5.3 and obtain ⟨(n + 1)α⟩∗ < ⟨nα⟩∗. Otherwise, if ⟨n1α⟩∗ < 1/2, then since
qM −1 < m, the integer n1 is in the range [n − m + 1, n + m − 1]. By Lemma 5.6, we have
⟨n1α⟩∗ < ⟨nα⟩∗, and so n ̸= ̂x∗.

Case 3: L = M − 1 and n = bM −1qM −1 + ∑N
k=M bkqk with bM −1 ≥ 2. If L ≥ 1, we set
n1 := n − qM −1 > n − m. Then, by Lemma 5.7, we have ⟨n1α⟩∗ < ⟨nα⟩∗, and so n ̸= ̂x∗. If
L = 0, the same follows from Lemma 5.11.

Case 4: L ≤ M − 2. If L ≥ 1, we set n1 := n + qL+1 < n + m. Then by Lemma 5.9, we
have ⟨n1α⟩∗ < ⟨nα⟩∗, and so n ̸= ̂x∗. If L = 0, the same follows from Lemma 5.10. □

BALANCED RECTANGLES 17

The two above lemmas give us a partial result towards the full characterisation in Theo-
rem 2.1; note that the cases (a) and (b) in Lemma 6.5 are almost the same as the cases (i)
and (ii) in Theorem 2.1. Next, we provide some lemmas that will be useful in the situation
where ̂x∗ ̸= n. We start with two lemmas which will, roughly speaking, allow us to assume
̂x∗ < n without loss of generality.

6.2. Switching between n and qT − n

Lemma 6.6. Let 2 ≤ m ≤ n. Then, for sufficiently large T , the intervals of length {nα} are
balanced with respect to (α, m) if and only if the intervals of length {(qT − n)α} are balanced
with respect to (α, m).

Proof. This follows directly from Lemma 4.6 and the fact that ∥qT α∥ gets arbitrarily small
for large T . □

Lemma 6.7. Let ̂xleft(m, n) = ̂xleft be defined as before, and define ̂xright(m, qT − n) in an
analogous way, i.e., ̂xright(m, qT − n) minimises ⟨xα⟩right in the range [qT − n − m + 1, qT −
n + m − 1]. Then for sufficiently large T we have

̂xleft(m, n) > n ⇐⇒ ̂xright(m, qT − n) < qT − n.

Proof. Note that since ⟨ξ⟩left = ⟨−ξ⟩right, we have

⟨−̂xleftα⟩right = ⟨̂xleftα⟩left = min
n−m+1≤x≤n+m−1
⟨xα⟩left = min
−(n+m−1)≤x≤−(n−m+1)
⟨xα⟩right.

If qT is sufficiently large, adding qT to every x in the range [−(n + m − 1), −(n − m + 1)] =
[−n − m + 1, −n + m − 1] does not change the ordering of the numbers ⟨xα⟩right, and so the
above equation implies

⟨(qT − ̂xleft)α⟩right = max
qT −n−m+1≤x≤qT −n+m−1
⟨xα⟩right.

This means that qT − ̂xleft = ̂xright(m, qT − n), and so ̂xleft > n ⇐⇒ ̂xright(m, qT − n) <
qT − n. □

6.3. Technical lemmas for the case ̂x∗ < n

If ̂x∗ < n, then we do not have x∗(ℓ) = ̂x∗ for all ℓ ∈ [0, m − 1]. However, it is not hard
to see that x∗(ℓ) = ̂x∗ for a certain range of ℓ’s (which, admittedly, might be only the single
integer ℓ = n − m + 1). We can say more about the precise values of x∗(ℓ) in adjacent ranges.
This is probably the most technical part of the paper; after that we will be able to prove
(non-)balancedness in various cases.
Recall that we always implicitly assume either (f∗, x∗, ⟨·⟩∗, ̂x∗) = (fleft, xleft, ⟨·⟩left, ̂xleft)
or (f∗, x∗, ⟨·⟩∗, ̂x∗) = (fright, xright, ⟨·⟩right, ̂xright). For technical reasons, we assume m ≥ q1;
the cases where m is very small are actually quite easy and we will deal with them separately
in Section 6.5.

Lemma 6.8. Assume 2 ≤ q1 ≤ m ≤ n and qM −1 < m ≤ qM . Moreover, assume that
̂x∗ < n. Then we have

x∗(ℓ) = ̂x∗ ⇐⇒ ℓ ∈ [0, m − 1 + ̂x∗ − n] =: R0.

If ⟨qM −1α⟩∗ < 1/2, then

x∗(ℓ) = ̂x∗ + qM −1
⇐⇒ ℓ ∈ [m + ̂x∗ − n, min{m + ̂x∗ − n − 1 + qM −1, m − 1}] =: R1.

If ⟨qM α⟩∗ < 1/2 and m = qM , then

x∗(ℓ) = ̂x∗ + qM ⇐⇒ ℓ ∈ [m + ̂x∗ − n, m − 1] =: R′
1.

18 I. VUKUSIC

If ⟨qM α⟩∗ < 1/2 and qM −2 + aqM −1 ≤ m < qM −2 + (a + 1)qM −1 with 0 ≤ a ≤ aM − 1, then

x∗(ℓ) = ̂x∗ + qM −2 + aqM −1
for all ℓ ∈ [m + ̂x∗ − n, min{̂x∗ − n + qM −2 + (a + 1)qM −1 − 1, m − 1}] =: R′′
1 ;

x∗(ℓ) = ̂x∗ + qM −2 + (a + 1)qM −1
for all ℓ ∈ [̂x∗ − n + qM −2 + (a + 1)qM −1,

min{̂x∗ − n + qM −2 + (a + 2)qM −1 − 1, m − 1}] =: R′′
2 .

Note that the range R′′
2 is empty if and only if m − 1 ≤ ̂x∗ − n + qM −2 + (a + 1)qM −1 − 1.

Proof. By the definitions of ̂x∗ and x∗(·), we clearly have x∗(ℓ) = ̂x∗ if and only if ̂x∗ ∈
X(ℓ) = [n + ℓ − m + 1, n + ℓ]. Under our assumption ̂x∗ < n, this happens exactly for
ℓ ∈ [0, m − 1 + ̂x∗ − n]. This settles the statement regarding the range R0. Now we go
through all the cases from the statement of the lemma.

Case 1: ⟨qM −1α⟩∗ < 1/2.
First, note that ̂x∗ + qM −1 ∈ X(ℓ) = [n + ℓ − m + 1, n + ℓ] if and only if ℓ ∈ [̂x∗ −
n + qM −1, m + ̂x∗ − n − 1 + qM −1]. Since ̂x∗ − n + qM −1 ≤ m + ̂x∗ − n, we have indeed
̂x∗ + qM −1 ∈ X(ℓ) for all ℓ ∈ R1 = [m + ̂x∗ − n, min{m + ̂x∗ − n − 1 + qM −1, m − 1}] (and
not for any larger ℓ). Now we only need to show that ̂x∗ + qM −1 indeed minimises ⟨xα⟩∗ in
each range X(ℓ) for ℓ ∈ R1. In other words, we need to show that

(6.3) ⟨(̂x∗ + qM −1)α⟩∗ = min{⟨xα⟩∗ : x ∈ [̂x∗ + 1, min{m + ̂x∗ − 1 + qM −1, n + m − 1}]}.

From the definition of ̂x∗ it follows that

x′ := min{x > ̂x∗ : ⟨xα⟩∗ < ⟨̂x∗α⟩∗} > n + m − 1.

Moreover, note that m + ̂x∗ − 1 + qM −1 < ̂x∗ + qM −1 + qM . Therefore, we get (6.3) directly
from Lemma 5.14 with a = 0. This settles the statement regarding the range R1.

Case 2: ⟨qM α⟩∗ < 1/2 and m = qM
First, note that ̂x∗ + qM ∈ X(ℓ) = [n + ℓ − m + 1, n + ℓ] if and only if ℓ ∈ [̂x∗ − n + qM , m +
̂x∗ − n − 1 + qM ] = [m + ̂x∗ − n, 2m + ̂x∗ − n − 1]. Since 2m + ̂x∗ − n − 1 ≥ m, we have in
fact ̂x∗ + qM ∈ X(ℓ) for all ℓ ∈ R′
1 = [m + ̂x∗ − n, m − 1]. Now we only need to show that
̂x∗ + qM indeed minimises ⟨xα⟩∗ in each range X(ℓ) for ℓ ∈ R′
1. Since the largest element in
all these ranges is n + m − 1 ≤ ̂x∗ + 2m − 2 = ̂x∗ + 2qM − 2 < ̂x∗ + qM + qM +1, this follows
again directly from Lemma 5.14 with a = 0.

Case 3: ⟨qM α⟩∗ < 1/2 and qM −2 + aqM −1 ≤ m < qM −2 + (a + 1)qM −1 with 0 ≤ a ≤ aM − 1.
First, note that ̂x∗ + qM −2 + aqM −1 ∈ X(ℓ) = [n + ℓ − m + 1, n + ℓ] if and only if
ℓ ∈ [̂x∗ − n + qM −2 + aqM −1, m + ̂x∗ − n − 1 + qM −2 + aqM −1]. On the one hand, we have
̂x∗ −n+qM −2 +aqM −1 ≤ m+ ̂x∗ −n. On the other hand, recall that in the lemma we assume
m > qM −1, and so m + ̂x∗ − n − 1 + qM −2 + aqM −1 ≥ ̂x∗ − n + qM −2 + (a + 1)qM −1 − 1. Thus,
we have indeed ̂x∗ + qM −2 + aqM −1 ∈ X(ℓ) for ℓ ∈ R′′
1 = [m + ̂x∗ − n, min{̂x∗ − n + qM −2 +
(a + 1)qM −1 − 1, m − 1}]. We need to check that ̂x∗ + qM −2 + aqM −1 minimises ⟨xα⟩∗ in the
range [̂x∗ + 1, ̂x∗ + qM −2 + (a + 1)qM −1 − 1]. Indeed, this follows directly from Lemma 5.14.
The proof for the range R′′
2 is completely analogous, except for the following detail: if
a + 1 = aM , then qM −2 + (a + 1)qM −1 = qM , and Lemma 5.14 would allow us to make R′′
2
even larger. □

In the case ̂x∗ < n we can now use the above lemma to characterise f∗ being bijective in
terms of the shape of ̂x∗ and m. Again, we assume m ≥ q1.

Lemma 6.9. Assume 2 ≤ q1 ≤ m ≤ n and qM −1 < m ≤ qM . Moreover, assume that
̂x∗ < n. Then f∗ is bijective in exactly the three following cases:

• ⟨qM α⟩∗ < 1/2 and m = qM ;

• ⟨qM α⟩∗ < 1/2, m = qM −2 + aqM −1 for some 1 ≤ a ≤ aM − 1 and M − 2 ≥ 0, and
̂x∗ ≥ n − qM −1;
 BALANCED RECTANGLES 19

• ⟨qM α⟩∗ < 1/2, qM −2 + aqM −1 < m < qM −2 + (a + 1)qM −1 for some 0 ≤ a ≤ aM − 1
and ̂x∗ = n − qM −1.

Proof. We distinguish between five cases, according to whether ⟨qM α⟩∗ < 1/2 or ⟨qM −1α⟩∗ <
1/2, and some extra conditions.

Case 1: ⟨qM −1α⟩∗ < 1/2.
Then, by Lemma 6.8, we have x∗(ℓ) = ̂x∗ for ℓ ∈ R0 and x∗(ℓ) = ̂x∗ + qM −1 for ℓ ∈ R1.
Since m − 1 ≥ qM −1 and m + ̂x∗ − n − 1 + qM −1 ≥ qM −1, the range R0 ∪ R1 contains at
least qM −1 + 1 consecutive integers. Therefore, there exist ℓ ∈ R0 and ℓ′ ∈ R1 such that
ℓ
′ − ℓ = qM −1. For these ℓ, ℓ
′ we have x∗(ℓ′) − x∗(ℓ) = qM −1 = ℓ′ − ℓ, and so f∗ is not
bijective by Lemma 6.3.

Case 2: ⟨qM α⟩∗ < 1/2 and m = qM .
By Lemma 6.8, we have either x∗(ℓ) = ̂x∗ or x∗(ℓ) = ̂x∗ + qM for all ℓ ∈ R0 ∪ R′
1 =
[0, m − 1] = [0, qM − 1]. Therefore, it is clear that we cannot have ℓ − ℓ′ = x∗(ℓ) − x∗(ℓ
′) for
ℓ ̸= ℓ
′ ∈ [0, m − 1], and so f∗ is bijective by Lemma 6.3.

Case 3: ⟨qM α⟩∗ < 1/2 and m = qM −2 + aqM −1 with 1 ≤ a ≤ aM − 1 and ̂x∗ ≥ n − qM −1.
Then, by Lemma 6.8, we have x∗(ℓ) = ̂x∗ for ℓ ∈ R0 and x∗(ℓ) = ̂x∗ + qM −2 + aqM −1 for
ℓ ∈ R′′
1 . Moreover, since we are assuming ̂x∗ ≥ n − qM −1, we have

̂x∗ − n + qM −2 + (a + 1)qM −1 − 1 ≥ qM −2 + aqM −1 − 1 = m − 1.

In other words, R0 ∪ R′′
1 = [0, m − 1], and so for all ℓ ∈ [0, m − 1] = [0, qM −2 + aqM −1 − 1]
either x∗(ℓ) = ̂x∗ or x∗(ℓ) = ̂x∗ + qM −2 + aqM −1. As in Case 2, it is clear that f∗ is bijective.

Case 4: ⟨qM α⟩∗ < 1/2 and m = qM −2+aqM −1 with 1 ≤ a ≤ aM −1, but now ̂x∗ < n−qM −1.
Then ̂x∗ − n + qM −2 + (a + 1)qM −1 − 1 < m − 1,

and so there is at least one ℓ ∈ R′′
2 . Now since the range R′′
1 contains exactly qM −1 integers
(note that m = qM −2 + aqM −1), the range R′′
1 ∪ R′′
2 contains at least qM −1 + 1 consecutive
integers. Moreover, Lemma 6.8 says that x∗(ℓ) = ̂x∗ + qM −2 + aqM −1 for ℓ ∈ R′′
1 and
x∗(ℓ) = ̂x∗ + qM −2 + (a + 1)qM −1 for ℓ ∈ R′′
2 . Thus, there must exist ℓ ∈ R′′
1 and ℓ′ ∈ R′′
2
with ℓ′ − ℓ = qM −1 = x∗(ℓ′) − x∗(ℓ), and so f∗ is not bijective.

Case 5: ⟨qM α⟩∗ < 1/2 and qM −2 + aqM −1 < m < qM −2 + (a + 1)qM −1 for some 0 ≤ a ≤
aM − 1.
If ̂x∗ > n − qM −1, then one can check that R0 ∪ R′′
1 ⊇ [0, qM −2 + aqM −1]. Therefore, there
must exist ℓ ∈ R0 and ℓ′ ∈ R′′
1 with ℓ′ − ℓ = qM −2 + aqM −1 = x∗(ℓ
′) − x∗(ℓ). Thus, f∗ is not
bijective.
If ̂x∗ < n − qM −1, then one can check that the range R′′
1 ∪ R′′
2 contains at least qM −1 + 1
consecutive integers, and that R′′
1 , R′′
2 are non-empty, and so, as in Case 4, f∗ is not bijective.
If ̂x∗ = n − qM −1, then the first term in the minimum in the upper bound of R′′
2 is

̂x∗ − n + qM −2 + (a + 2)qM −1 − 1 = qM +2 + (a + 1)qM −1 − 1 ≥ m − 1,

so R0 ∪ R′′
1 ∪ R′′
2 = [0, m − 1]. Also, one can check that R0 ∪ R′′
1 ̸⊇ [0, qM −2 + aqM −1], and
that R′′
1 ∪ R′′
2 contains at most qM −1 consecutive integers. Thus, x∗(ℓ′) − x∗(ℓ) ̸= ℓ
′ − ℓ for
all ℓ ∈ R0 and ℓ
′ ∈ R′′
1 , as well as for all ℓ ∈ R′′
1 and ℓ
′ ∈ R′′
2 . It is also easy to see that
x∗(ℓ′) − x∗(ℓ) ̸= ℓ
′ − ℓ for all ℓ ∈ R0 and ℓ ∈ R′′
2 because m − 1 < qM −2 + (a + 1)qM −1. Thus,
f∗ is bijective. □

6.4. The cases where ̂x∗ ̸= n

We now collect some of our results to show that “usually” we are in the not balanced
situation, which is a big step towards finishing the proof of Theorem 2.1.
First, we show that the third special case from Lemma 6.9 actually corresponds to the
case where n ∈ {̂xleft, ̂xright}.

20 I. VUKUSIC

Lemma 6.10. Let 2 ≤ q1 ≤ m ≤ n and qM −1 < m < qM . Assume that ⟨qM α⟩∗ < 1/2 and
̂x∗ = n − qM −1. Then n ∈ {̂xleft, ̂xright}.

Proof. The assumptions q1 ≤ m < qM imply M ≥ 2. The assumption ⟨qM α⟩∗ < 1/2 implies
that k0(̂x∗) ≡ M (mod 2) (or possibly k0(̂x∗) = 0).
If k0(̂x∗) ≥ M , then it follows from the basic properties of Ostrowski representations
that n = qM −1 + ̂x∗ has one of the two shapes (a), (b) from Lemma 6.5, which implies
n ∈ {̂xleft, ̂xright}.
If k0(̂x∗) ≤ M − 2, then Lemma 5.9 implies that ⟨nα⟩∗ = ⟨(̂x∗ + qM −1)α⟩∗ < ⟨̂x∗α⟩∗,
contradicting the definition of ̂x∗. □

Remark 6.11. In view of Lemma 6.10, if we assume n /∈ {̂xleft, ̂xright}, then Lemma 6.9
now only gives us two cases where f∗ is bijective, namely where m is either a convergent or
a semi-convergent (and some extra condition).

Lemma 6.12. Let 2 ≤ q1 ≤ m ≤ n. Assume that qM −1 < m < qM and that m is not a
semi-convergent. Moreover, assume that n /∈ {̂xleft, ̂xright}. Then fleft, fright are not bijective.

Proof. Recall from Lemma 4.3 that fleft being bijective is equivalent to fright being bijective,
which is equivalent to the intervals of length {nα} with respect to (α, m) being balanced.
Moreover, recall from Lemma 6.6 that the intervals of length {nα} are balanced if and only
if the intervals of length {(qT − n)α} are balanced, for T sufficiently large.
Now, if ̂xleft < n, then Lemmas 6.9 and 6.10 imply that fleft is not bijective.
If ̂xleft > n, then by Lemma 6.7 we have ̂xright(m, qT −n) < qT −n. Then again Lemmas 6.9
and 6.10 imply that the intervals of length {(qT − n)α} are not balanced with respect to
(α, m), and so neither are those of length {nα}. □

In the last two lemmas we deal with the cases where m is a (semi-)convergent. Note that
n[≤M ], n[≥M ], and k≥M (n) were defined in Section 5.5.

Lemma 6.13. Let 2 ≤ m = qM ≤ n, and assume n[≤M −1] > 0. Then fleft, fright are
bijective if and only if k≥M (n) ≡ M (mod 2).

Proof. Note that M ≥ 1. Choose ⟨·⟩∗ ∈ {⟨·⟩left, ⟨·⟩right} so that ⟨n[≥M ]α⟩∗ < 1/2. We want
to show that ̂x∗ < n because then we can finish with Lemma 6.9. In fact, we want to show
that ̂x∗ ≤ n
[≥M ].
First, note that n
[≥M ] = n − n[≤M −1] ∈ [n − m + 1, n − 1] because 0 < n
[≤M −1] < qM = m.
Therefore, we want to show that for all x ∈ [n[≥M ] +1, n+m−1] we have ⟨xα⟩∗ > ⟨n
[≥M ]α⟩∗.
Assume first that k0(n[≥M ]) ≥ M + 1. Then Lemma 5.13 tells us that n
[≥M ] minimises
⟨xα⟩∗ in the range [n
[≥M ], n
[≥M ] + qM + qM +1 − 1]. The upper bound of this range is

n[≥M ] + qM + qM +1 − 1 ≥ n − m + 1 + qM + qM +1 − 1 = n + qM +1 > n + m − 1.

Therefore, we indeed have ̂x∗ ≤ n
[≥M ].
Now assume k0(n
[≥M ]) = M . By the same argument as before, Lemma 5.13 tells us that
n[≥M ] minimises ⟨xα⟩∗ in the range [n
[≥M ], n
[≥M ] + qM −1 + qM − 1]. If

(6.4) n
[≥M ] + qM −1 + qM − 1 ≥ n + m − 1,

then, as before, we know that n
[≥M ] minimises ⟨xα⟩∗ in the range [n[≥M ], n + m − 1], and
thus ̂x∗ ≤ n
[≥M ]. If the inequality (6.4) does not hold, then, after cancelling qM − 1 = m − 1,
we get n[≥M ] + qM −1 < n.

Since n
[≤M −1] = n − n[≥M ], this implies n[≤M −1] > qM −1, and so by the property (5.6) of
Ostrowski representations, we have bM −1(n) > 0. But then, by the digit rules for Ostrowski
representations, we must have bM (n) ≤ aM +1−1, and so we can use the stronger statement in
Lemma 5.13: In this case n[≥M ] minimises ⟨xα⟩∗ in the range [n[≥M ], n
[≥M ]+qM −1+2qM −1].
This now covers the full range [n
[≥M ] + 1, n + m − 1], and thus ̂x∗ ≤ n
[≥M ].

BALANCED RECTANGLES 21

Overall, we have proven that ̂x∗ ≤ n
[≥M ] < n, and so Lemma 6.9 says that f∗ is bijective
if and only if ⟨qM α⟩∗ < 1/2, which is equivalent to k≥M (n) ≡ M (mod 2) by Lemma 5.5. □

Lemma 6.14. Let m = qM −2 + aqM −1 with 1 ≤ a ≤ aM − 1 and M − 2 ≥ 0. Let n ≥ m
and assume that n is not of the shape (a) or (b) from Lemma 6.5 (or, in other words,
n /∈ {̂xleft, ̂xright}). Then fleft, fright are bijective if and only if k≥M −1(n) ≡ M (mod 2).

Proof. Let m, n be as in the lemma. We distinguish between two cases according to whether
qM −1 shows up in the representation of n or not.

Case 1: n = n[≤M −2] + n[≥M ].
Since n[≤M −2] < qM −1 < m, we have n[≥M ] ∈ [n − m + 1, n + m − 1].
Moreover, since m ≤ qM − qM −1 and n
[≥M ] > n − qM −1, we have [n − m + 1, n + m − 1] ⊆
[n
[≥M ] − qM + 1, n
[≥M ] + qM − 1]. Thus, Lemma 5.12 implies that n[≥M ] = ̂x∗ for the
appropriate choice of ̂x∗ ∈ {̂xleft, ̂xright}. In particular, we have ̂x∗ < n. Now Lemma 6.9
says that f∗ is bijective if and only if ⟨qM α⟩∗ < 1/2, which is equivalent to k≥M −1(n) =
k0(n
[≥M ]) ≡ M (mod 2), by Lemma 5.5.

Case 2: n = n[≤M −2] + bM −1qM −1 + n[≥M ] with 1 ≤ bM −1 ≤ aM .
We want to show that fleft, fright are not bijective.
Our first goal is to show that we may assume that one of ̂xleft, ̂xright is smaller than n. If
̂xleft < n, this is of course the case. Assume now that ̂xleft > n. Then Lemma 6.7 says that
if we consider qT − n instead of n for sufficiently large T , we get ̂xright(m, qT − n) < qT − n.
Lemma 6.6 guarantees that the balancedness property doesn’t change if we replace n by
qT − n. Lemma 5.17 implies (note that by assumption n is not of the shape (b)) that
k≥M −1(qT − n) ≡ M − 1 (mod 2). If qM −1 does not show up in the representation of qT − n,
then we know from Case 1 that we are in the not balanced situation. If qM −1 shows up in
the representation of qT − n, then qT − n has the same shape (the shape of Case 2) as n,
and we can replace qT − n by n, knowing that now the new ̂xright is smaller than the new n.
Overall, in Case 2, we may now assume that at least one of ̂xleft, ̂xright is smaller than n.
We fix this ̂x∗ < n, and our goal is to show that f∗ is not bijective.
In order to apply Lemma 6.9 we use the fact that ⟨qM α⟩∗ < 1/2 if and only if k0(̂x∗) ≡ M
(mod 2). This is guaranteed by Lemma 5.5, unless k0(̂x∗) = 0. In the exceptional case
we still have ⟨q0α⟩∗ < 1/2. (To see this, assume the contrary and use Lemma 5.3 and the
assumption ̂x∗ < n to obtain a contradiction.)
Now, if k0(̂x∗) ≡ M + 1 (mod 2), i.e., ⟨qM −1α⟩∗ < 1/2, then Lemma 6.9 says that f∗ is
not bijective, as desired.
If k0(̂x∗) ≡ M (mod 2), i.e., ⟨qM α⟩∗ < 1/2, and if ̂x∗ < n − qM −1, then Lemma 6.9 again
says that f∗ is not bijective.
We are left with the case n − qM −1 ≤ ̂x∗ < n and k0(̂x∗) ≡ M (mod 2). We need to show
that this is impossible for n = n[≤M −2] +bM −1qM −1 +n
[≥M ] with 1 ≤ bM −1 ≤ aM (and n not
of the shape (b)). The shape of n and the assumptions n − qM −1 ≤ ̂x∗ < n and k0(̂x∗) ≡ M
(mod 2) imply that k0(̂x∗) ≥ M is impossible. Thus, we must have k0(̂x∗) ≤ M − 2. But
then, ⟨(̂x∗ + qM −1)α⟩∗ < ⟨̂x∗α⟩∗ by Lemma 5.9. Since ̂x∗ + qM −1 ∈ [n − m + 1, n + m − 1],
this contradicts the fact that ̂x∗ minimises ⟨xα⟩∗ in the range [n − m + 1, n + m − 1]. □

6.5. Very small m

In the previous two subsections we assumed m ≥ q1 for technical reasons. The cases where
2 ≤ m < q1 are actually quite easy and we deal with them by going back to the original
definition of balanced intervals.

Lemma 6.15. Let 2 ≤ m ≤ n with m < q1. Then the intervals of length {nα} are balanced
with respect to {0, α, . . . , (m−1)α} if and only if either n is either of the shape n = ∑N
k=1 bkqk
or n = q0 + ∑N
k=1+2t bkqk with t ≥ 0 and b1+2t ̸= 0.

Proof. From the basic properties of continued fractions we know that α < 1/q1, and so we
have 0 < α < 2α < · · · < (q1 − 1)α < q1α < 1.

22 I. VUKUSIC

If n is of one of the two special shapes from the lemma, then we know from Lemma 5.1(2, 8)
that ∥nα∥ < α, and so the intervals of length ∥nα∥ (which are either exactly the intervals of
length {nα} or their complements) each contain either no points or one point. In particular,
the intervals are balanced.
If n is not of one of the two special shapes, then we know from Lemma 5.1(8) that
1/2 > ∥nα∥ > α, and so {nα} > α.
By simply counting points, we see that the interval [0, {nα}) contains exactly ⌈{nα} /α⌉ ≥
2 points.
On the other hand, since (q1 − 1)α < q1α < 1 and m − 1 ≤ q1 − 2, we see that the
interval [1 − {nα} , 0) contains at most ⌈{nα} /α⌉ − 2 points. Thus, the intervals are not
balanced. □

6.6. Finishing the proof of the full characterisation

We have now essentially proved Theorem 2.1, and we summarise the arguments below.

Proof of Theorem 2.1. Recall the four cases from Theorem 2.1:

(i) m = ∑M
k=0 bkqk and n = ∑N
k=M +1 bkqk;

(ii) m = ∑M
k=0 bkqk with bM ̸= 0, and n = qM + ∑N
k=M +1+2t bkqk with t ≥ 0 and
bM +1+2t ̸= 0.

(iii) m = qM and n = ∑M −1
k=0 bkqk + ∑N
k=M +2t bkqk with t ≥ 0 and bM +2t ̸= 0;

(iv) m = qM −1 + aqM with 1 ≤ a ≤ aM +1 − 1 and n = ∑M −1
k=0 bkqk + ∑N
k=M +1+2t bkqk
with t ≥ 0 and bM +1+2t ̸= 0.

Note that some of the cases overlap; for example if the small parts of n in (iii) or (iv) are zero,
then we are also in the case (i). (This was done for readability in Theorem 2.1.) We need to
show that m, n are of the shape of at least one of the cases if and only if the m × n rectangles
of the Sturmian words with slope α are balanced. By Theorem 3.1 and Lemma 4.3, this is
equivalent to fleft, fright being bijective (and we know that one function is bijective if and
only if the other is bijective).
We first check that if m, n are of the shape of one of the cases (i)–(iv), then fleft, fright
are bijective. In the cases (i), (ii) we have m < qM +1, and so Lemma 6.5 implies that
n ∈ {̂xleft, ̂xright}, and Lemma 6.4 implies that the corresponding function f∗ is bijective. If
we are in the case (iii) and n
[≤M −1] = 0, then again Lemmas 6.5 and 6.4 imply that fleft, fright
are bijective. If we are in the case (iii) and n
[≤M −1] > 0, this is provided by Lemma 6.13.
If we are in the case (iv) and not in one of the previous cases, then Lemma 6.14 says that
fleft, fright are bijective.
For the implication in the other direction, assume that 2 ≤ m ≤ n and that fleft, fright
are bijective.
If n ∈ {̂xleft, ̂xright}, then Lemma 6.5 and the property (5.6) imply that m, n are of the
shape (i) or (ii), or m = qM . If m is a convergent, then Lemma 6.13 implies that m, n are of
the shape (iii) or (i).
If n ̸= ̂xleft, ̂xright, then Lemma 6.12 implies that m must either be a convergent or a semi
convergent, or m < q1. If m is a convergent, then as before Lemma 6.13 implies that m, n
are of the shape (iii) or (i). If m is a semi-convergent, then Lemma 6.14 implies that m, n
are of the shape (iv) or (i) or (ii). Finally, if m < q1, Lemma 6.15 implies that m, n are of
the shape (i) or (ii). □

7. Acknowledgements

I want to thank Jeffrey Shallit for helpful discussions and for providing several automata
which hugely helped to guess the characterisation in Theorem 2.1. I am also grateful to
Manuel Hauke for helpful discussions, and to Benjamin Ward and Victor Beresnevich for
their support in moments of despair.

BALANCED RECTANGLES 23

References

[1] J.-P. Allouche and J. Shallit. Automatic sequences. Cambridge University Press, Cambridge, 2003.
doi:10.1017/CBO9780511546563. Theory, applications, generalizations.
[2] M. Anselmo, D. Giammarresi, M. Madonia, and C. Selmi. Fibonacci pictures on a binary alphabet. In
Descriptional complexity of formal systems. 26th IFIP WG 1.02 international conference, DCFS 2025,
Loughborough, UK, July 22–24, 2025. Proceedings, pages 1–16. Cham: Springer, 2025. doi:10.1007/978-
3-031-97100-6 1.
[3] V. Beresnevich, A. Haynes, and S. Velani. Sums of reciprocals of fractional parts and multiplicative Dio-
phantine approximation, volume 1276 of Mem. Am. Math. Soc. Providence, RI: American Mathematical
Society (AMS), 2020. doi:10.1090/memo/1276.
[4] V. Berth´e and R. Tijdeman. Balance properties of multi-dimensional words. Theor. Comput. Sci., 273(1-
2):197–224, 2002. doi:10.1016/S0304-3975(00)00441-2.
[5] Y. Bugeaud. Distribution modulo one and Diophantine approximation, volume 193 of Camb. Tracts
Math. Cambridge: Cambridge University Press, 2012. doi:10.1017/CBO9781139017732.
[6] S. Puzynina. Aperiodic two-dimensional words of small abelian complexity. Electron. J. Comb., 26(4):re-
search paper p4.15, 21, 2019. doi:10.37236/8580.
[7] A. M. Rockett and P. Sz¨usz. Continued fractions. World Scientific Publishing Co., Inc., River Edge, NJ,
1992. doi:10.1142/1725.
[8] J. Shallit and I. Vukusic. Balanced Fibonacci word rectangles, and beyond. Discrete Mathematics &
Theoretical Computer Science, vol. 28:2, Apr 2026. doi:10.46298/dmtcs.16955.

I. Vukusic, Department of Mathematics, University of York, Ian Wand Building, Deramore
Lane, York, YO10 5GH, United Kingdom
Email address: ingrid.vukusic@york.ac.uk
