<!-- source: https://arxiv.org/pdf/2201.13446 | converted from PDF -->

arXiv:2201.13446v5  [math.CO]  3 Jan 2024
A Note on the Relation between
Recognisable Series and
Regular Sequences, and Their
Minimal Linear Representations

Clemens Heuberger, Daniel Krenn, Gabriel F. Lipnik

Abstract

In this note, we precisely elaborate the connection between recognisable series
(in the sense of Berstel and Reutenauer) and q-regular sequences (in the sense of
Allouche and Shallit) via their linear representations. In particular, we show that
the minimisation algorithm for recognisable series can also be used to minimise
linear representations of q-regular sequences.

1 Introduction

1.1 Overview

Every regular sequence can also be seen as a recognisable series—deﬁnitions of both
notions are recalled below—and both can be described by a linear representation using
a collection of square matrices and two vectors. So when the authors of this note imple-
mented both concepts in SageMath [7], this relation and property played fundamental
roles. For recognisable series, there exists an algorithm to minimise the dimension of

Clemens Heuberger clemens.heuberger@aau.at, https://wwwu.aau.at/cheuberg, Alpen-
Adria-Universität Klagenfurt, Austria

Daniel Krenn math@danielkrenn.at, http://www.danielkrenn.at, Paris Lodron University of
Salzburg, Austria

Gabriel F. Lipnik math@gabriellipnik.at, https://www.gabriellipnik.at, Graz University of
Technology, Austria

Support Clemens Heuberger is supported by the Austrian Science Fund (FWF): DOC 78. Gabriel
F. Lipnik is supported by the Austrian Science Fund (FWF): W 1230.

2020 Mathematics Subject Classiﬁcation 11A63, 68Q45, 68R05, 68R15

Key words and phrases regular sequence, recognisable series

1

their linear representations based on methods of Schützenberger [8, 9]; see Berstel and
Reutenauer [3, Chapter 2]. So it seemed to be reasonable
1 that this algorithm can also
be used for regular sequences.
When implementing the results of [6], the authors of this note suddenly encountered
a situation where the minimisation algorithm for recognisable series failed for a regular
sequence.
2 At ﬁrst, we were quite puzzled. It soon turned out that the linear represen-
tation we used for our regular sequence did not fulﬁl a certain eigenvector property that
should be fulﬁlled for regular sequences, but we were quite unsure whether ﬁxing this
completely solves the problem. The answer is yes, and the details are the topic of this
note.

1.2 Recognisable Series and Regular Sequences

Let N0 denote the set of non-negative integers and K be an arbitrary ﬁeld. Moreover,
let q ≥ 2 be an integer and set Aq := {0, . . . , q − 1}.
We ﬁrst recall the deﬁnition of a recognisable series; the book of Berstel and Reutenauer [3,
Chapter 2] provides an introduction to these series.

Deﬁnition 1.1. Let A be a ﬁnite set. A sequence x ∈ K A⋆ is said to be a recognisable
series if there are a non-negative integer D, a family M = (M(a))a∈A of D × D matrices
over K and vectors u ∈ K 1×D, w ∈ K D×1 such that for all b = b0 . . . bℓ−1 ∈ A⋆, we have

x(b) = uM(b)w

with
3
 M(b) := M(b0) · · · M(bℓ−1). (1)

We call (u, M, w) a linear representation of x and D the dimension of the linear
representation of x.

Note that we will use the convention (1) throughout this note. Next, we recall the
deﬁnition
4 of a regular sequence; see Allouche and Shallit [1, 2] for characterisations,
properties, and an abundance of examples. Asymptotic properties and further examples
have been studied; cf. [5], [6], and the references therein.

1We did not ﬁnd any reference for that. If a reader is aware of such a reference, please contact the
authors. Added in proof: a remark on the topic can be found in Dumas [4] after Deﬁnition 2.
2See https://github.com/sagemath/sage/issues/32921#issuecomment-1418154841. A smaller
example is presented in Example 1.3.
3In other words, we extend the map M : A → K D×D to a monoid homomorphism from A
⋆ to K D×D.
By convention, if b is the empty word in A
⋆, then M (b) is the D-dimensional identity matrix. If the
dimension D equals 0, then the product of an empty vector, M (b) (for any b) and another empty
vector is an empty double sum, so equals 0.
4Strictly speaking, this is an algorithmic characterisation of a regular sequence which is equivalent
to the deﬁnition given by Allouche and Shallit [1], who ﬁrst introduced this concept: they deﬁne a
sequence y to be q-regular if the kernel
{
y ◦ (n ↦→ qjn + r) ∣
∣ j, r ∈ N0 with 0 ≤ r < qj}

is contained in a ﬁnite dimensional vector space.

2

Deﬁnition 1.2. A sequence y ∈ K N0 is said to be q-regular 5 if there are a non-negative
integer D, a family M = (M(a))a∈Aq of D × D matrices over K, a vector u ∈ K 1×D and
a vector-valued sequence v ∈ (K D×1)N0 such that for all n ∈ N0, we have

y(n) = uv(n),

and such that for all r ∈ Aq and all n ∈ N0, we have

v(qn + r) = M(r)v(n). (2)

We call (u, M, w) a linear representation of x and D the dimension of the linear
representation of x.

By induction using (2), it is easily seen that for all n ∈ N0, we have

y(n) = uM(digitsq(n))w (3)

where digitsq(n) = n0 . . . nℓ−1 is the standard qary expansion of n, i. e., n = ∑
0≤j<ℓ njqj

with nℓ−1 ̸= 0, and w := v(0). In other words, given a q-regular sequence y with linear
representation (u, M, w) and considering the recognisable series x with linear represen-
tation (u, M, w) over the alphabet Aq, we can write y = x ◦ digitsq.
As mentioned in Section 1.1, this is how the authors of this note implemented regular
sequences in SageMath: these were a special case of recognisable series—technically
speaking, the class RegularSequence is a subclass of the class RecognizableSeries—
where accessing the values for integer values is translated accordingly and additional
properties (such as subsequences) are implemented. To construct a regular sequence in
SageMath, the input is a family of square matrices M and two vectors u and w.

1.3 Minimisation Failing?

Deﬁnitions 1.1 and 1.2 are worded in such a way as to allow several diﬀerent linear
representations of the same recognisable series or regular sequence. When working with
such objects algorithmically, inevitably, the question of minimality of the dimension of
the linear representation arises.
As mentioned in Section 1.1, Berstel and Reutenauer [3] describe an algorithm to
determine a linear representation of minimal dimension for a recognisable series, given
by some linear representation. The remarks at the end of Section 1.2 imply that this
algorithm is also used in SageMath to ﬁnd a linear representation of minimal dimension
of a regular sequence. As also mentioned in Section 1.1, this led to a problem, and here
is a simpliﬁed example illustrating it.

Example 1.3. Let q = 2,

u = (1 0
) , M(0) =
 (1 1
0 0
) , M(1) =
 (1 0
0 0

) , and w =
 (0
1
) , (4)

5In the standard literature, the basis is frequently denoted by k instead of our q here.

3

and consider the sequence y deﬁned by (3) for these values of u, M, and w.
We have y(0) = uw = 0 and for all positive integers n, the standard binary expansion
digits2(n) ends on a 1, so writing digits2(n) = b1 for some b ∈ {0, 1}⋆, we have

y(n) = uM(b)M(1)w = (1 0
) M(b)
 (1 0
0 0

) (0
1

) = (1 0
) M(b)
 (0
0
) = 0.

Hence, we have shown y(n) = 0 for all n ∈ N0. For the zero sequence, the minimal linear
representation is the representation of dimension 0, i. e., the left and right vectors as
well as the matrices M(a) are empty and all matrix products, vector-matrix products,
and matrix-vector products are empty sums and therefore 0, as required.
We now compare our result here with the one in SageMath. The input

S = RecognizableSeriesSpace(QQ, [0, 1])

u = vector([1, 0])
M_0 = matrix([[1, 1], [0, 0]])
M_1 = matrix([[1, 0], [0, 0]])
w = vector([0, 1])

x = S([M_0, M_1], u, w)
x.minimized().linear_representation()

yields the output

((1, 0), Finite family {0: [0 1] [0 1], 1: [1 0] [1 0]}, (0, 1)) .

We see that SageMath returns a linear representation of dimension 2 (not identical to
the input linear representation) and claims it to be minimal. Note that we used a
recognisable series here because the algorithm by Berstel and Reutenauer is formulated
for recognisable series.

So we do have a problem: we easily saw that our regular sequence y has a linear
representation of dimension 0, but SageMath answered that all linear representations of
the underlying recognisable series x have dimension at least 2.
A few possibilities come to mind. Almost unthinkably, there could be an error in
the algorithm of Berstel and Reutenauer, or, more probably, in our implementation of
that algorithm in SageMath. Despite a clear peer-reviewing policy for contributions into
SageMath, we might have overlooked something. We ask SageMath once more to get a
partial answer.

Example 1.4 (Continuation of Example 1.3). The input

x

gives the ﬁrst few terms of the recognisable series as

4

[0] + [00] + [10] + [000] + [010] + [100] + [110]
+ [0000] + [0010] + [0100] + ...

So it seems that the recognisable series does not vanish. The output suggests that the
recognisable series x with the linear representation deﬁned in (4) is one exactly for those
input words with trailing zeros. Indeed,

x(b0) = uM(b)M(0)w = (
1 0) M(b)
 (1 1
0 0
) (
0
1
) = (1 0) M(b)
 (1
0
) = 1

by induction.
This means that x(b) = 1 if 0 is a suﬃx of b and x(b) = 0 otherwise. It is therefore
clear that there cannot be a linear representation of x of dimension 0 (because that
would lead to all zeros due to empty sums). It is not hard to see that x cannot have a
linear representation of dimension 1, either: then the matrices M(0) and M(1) of that
linear representation would forcibly commute and x(b) could only depend on the number
of occurrences of the letters 0 and 1 in b, but not on their position. Thus, independently
of the algorithm of Berstel and Reutenauer (and its implementation in SageMath), we
conclude that any linear representation of x must have dimension at least 2.

So with Examples 1.3 and 1.4, we did not construct a counter example to the validity
of the minimisation algorithm of Berstel and Reutenauer for recognisable series, however
in this particular example, we see that we cannot apply the algorithm to ﬁnd a minimal
representation of the regular sequence. More generally, this means that choosing an
arbitrary family of matrices M and left and right vectors u and w, respectively, and
deﬁning a regular sequence by (3) can lead to situations where the algorithm of Berstel
and Reutenauer for recognisable series does not return a minimal linear representation
for the regular sequence.
Is that the ﬁnal word? Or can we somehow ﬁnd at least some situations where using
the minimisation algorithm for recognisable series is valid for the “corresponding” regular
sequence?

1.4 Why this Note is Needed

The short answer is, we need this note to discuss the questions raised by the example
above. So, let us brieﬂy come back to Example 1.3. A key feature was that at ﬁrst we only
inserted words with trailing one (or the empty word) into the recognisable series because
standard binary expansions of positive integers have exactly this property. And indeed,
as the discussion in the examples shows, inserting any other binary expansion (with
trailing zeros) instead of the standard binary expansion would lead to another result.
This seems to be an important distinction between recognisable series (all words allowed)
and regular sequences (only words without trailing zeros inserted into the corresponding
recognisable series).
At ﬁrst glance, the following observation seems to be a technical detail: If we insert
n = r = 0 into (2), we obtain v(0) = M(0)v(0). In other words, if not zero, then v(0) is

5

an eigenvector of M(0) associated with the eigenvalue 1. It seems to be a minor detail
because once we replace the formulation (2) by (3), it does not seem to be relevant
any more. However, we note that this condition is not fulﬁlled in Example 1.3, as
M(0)w = ( 1
0 ) ̸= w. So (u, M, w) as given by (4) is not a linear representation of the
2-regular sequence y considered in Example 1.3 (and we carefully never claimed it to be
one).
6

This raises two questions. Suppose we have a regular sequence y, take a linear represen-
tation (u, M, w) of that regular sequence (thus implying M(0)w = w), take it as a linear
representation of a recognisable series x, and then run the minimisation algorithm by
Berstel and Reutenauer on it. Will this approach yield a minimal linear representation
of y? And will that linear representation still fulﬁl the essential eigenvector property?
The answer to both questions is yes. But according to the saying “fool me once,
shame on you; fool me twice, shame on me”, we should make sure to have a proof.
The nature of SageMath as an open source software system also means that this proof
should not be a “well-known fact in the community” or some kind of an urban myth, but
something which can be clearly referenced. In particular, such a reference is put in the
documentation of SageMath. This note sets out to provide that proof and to clarify the
relation between recognisable series and regular sequences, their linear representations,
and their minimal linear representations.

1.5 Structure of this Note

In Section 2, we collect information on recognisable series and their minimal linear
representations. Finally, in Section 3, we consider regular sequences, their connection to
recognisable series, and prove the main result of this paper (Theorem 3.6) as outlined
in the last two paragraphs of Section 1.4. We close by Example 3.7 providing another
angle on what can go wrong with minimisation.

2 Recognisable Series

Deﬁnition 2.1. A linear representation of a recognisable series x is said to be a minimal 7

linear representation of x if its dimension is minimal over all linear representations of x.

Berstel and Reutenauer present a characterisation for minimal linear representations [3,
Proposition 2.1]. In this note we only need the direction of the following lemma and for
reasons of self-containedness, we give an ad-hoc proof here.

Lemma 2.2 (Berstel–Reutenauer [3, Proposition 2.1]). Let A be a ﬁnite set, x ∈ K A⋆

be a recognisable series and (u, M, w) be a minimal linear representation of x of dimen-
sion D. Then span({uM(b) | b ∈ A⋆}) = K 1×D.

6In order to construct a linear representation for a regular sequence out of a linear representation of
a recognisable series as given by (4), one can follow the proof of [1, Lemma 4.1].
7In [3], these linear representations are called reduced instead of minimal.

6

The basic idea of the proof is that if that span had lower dimension, then everything
would take place in a proper subspace. Taking matrix representations with respect to a
basis of the subspace would then give a lower dimensional linear representation.
We mention that by symmetry, we also have span({M(b)w | b ∈ A⋆}) = K D×1; but
we will not need this property here.

Proof of Lemma 2.2. Let S := {uM(b) | b ∈ A⋆}. Toward a contradiction, assume that
we have span(S) = W for some proper subspace W of K 1×D of dimension D′ and let
B be a basis of W . Let ΦB : K 1×D′ → W be the coordinate map with respect to the
basis B.
As an implication of the deﬁnition of W , we have u ∈ W , and so there exists a
u′ ∈ K 1×D′ such that ΦB(u′) = u. For all a ∈ A, the map v ↦→ vM(a) is an endo-
morphism of W by construction of W : for b ∈ A⋆, we have uM(b)M(a) = uM(ba) ∈
S, which implies that the map under consideration maps S into itself and therefore
maps W = span(S) into itself. We now construct a family M ′ = (M ′(a))a∈A of
D′ × D′ matrices over K as follows. For all a ∈ A, let M ′(a) be the matrix repre-
sentation of the endomorphism v ↦→ vM(a) of W with respect to the basis B, i. e.,
ΦB(v′)M(a) = ΦB(v′M ′(a)) holds for all v′ ∈ K 1×D′. Let w′ ∈ K D′×1 be the matrix
representation of the homomorphism v ↦→ vw from W to K with respect to the basis B
of W and the standard basis of K, i. e., ΦB(v′)w = v′w′ holds for all v′ ∈ K 1×D′.
For all b ∈ A⋆, this implies that

x(b) = uM(b)w = ΦB(u′)M(b)w = ΦB(u′M ′(b))w = u′M ′(b)w′.

In other words, (u′, M ′, w′) is a linear representation of x, and its dimension is D′ < D,
a contradiction to (u, M, w) being a minimal linear representation of x.

Let us consider a linear representation (u, M, w) of a recognisable series x ∈ K A⋆, A
a ﬁnite set. If there is a z ∈ A with M(z)w = w, then it is clear that x(bz) = x(b)
holds for all b ∈ A⋆. It turns out that the converse is true if the linear representation is
minimal. This is the assertion of the following proposition.

Proposition 2.3. Let A be a ﬁnite set, x ∈ K A⋆ be a recognisable series and (u, M, w)
be a minimal linear representation of x. Let z ∈ A be such that x(bz) = x(b) holds for
all b ∈ A⋆. Then we have M(z)w = w.

Proof. Let D be the dimension of the linear representation (u, M, w), and set S :=
{uM(b) | b ∈ A⋆}. As

uM(b)w = x(b) = x(bz) = uM(bz)w = uM(b)M(z)w

holds for all b ∈ A⋆, the linear maps v ↦→ vw and v ↦→ vM(z)w from K 1×D to K coincide
on S. As S generates K 1×D by Lemma 2.2, these maps also coincide on K 1×D = span(S).
Therefore, their matrix representations w and M(z)w coincide.

Deﬁnition 2.4. Let x ∈ K A⋆
q be a recognisable series such that x(b0) = x(b) holds for
all b ∈ A⋆
q. Then x is said to be compatible with regular sequences (or simply compatible).

7

Remark 2.5. Let x be a recognisable series with minimal linear representation (u, M, w).
Then by Proposition 2.3, x being compatible is equivalent to the condition M(0)w = w.

The following example shows, however, that non-minimal linear representations (u, M, w)
of a compatible recognisable series do not necessarily satisfy the property M(0)w = w.

Example 2.6. Consider the constant recognisable series x ∈ C{0,1}⋆ with x(b) = 1 for all
b ∈ {0, 1}⋆. It is clear that x is compatible and a minimal linear representation (u, M, w)
is given by

u = (1) ∈ C1×1, M(0) = M(1) = (1) ∈ C1×1 and w = (1) ∈ C1×1.

So M(0)w = w holds, as stated in Remark 2.5.
Moreover, (u′, M ′, w′) with

u′ = (
1 0) , M ′(0) = M ′(1) =
 (1 0
0 2

) and w′ =
 (1
1

)

is also a linear representation of x: for a word b ∈ {0, 1}⋆ of length ℓ, we have

u′M ′(b)w′ = (
1 0) (1 0
0 2
)ℓ (
1
1
)

= (
1 0) (1 0
0 2ℓ
) (
1
1
)

= (
1 0) ( 1
2ℓ
) = 1 = x(b);

the lower right entry in M ′(b) is annihilated by the zero in u′. However, M ′(0)w′ = w′

does not hold. This is no contradiction to Remark 2.5 because (u′, M ′, w′) is not minimal.

3 Regular Sequences

Deﬁnition 3.1. A linear representation of a regular sequence y is said to be a minimal
linear representation of y if its dimension is minimal over all linear representations of y.

The ﬁrst statement of the following lemma corresponds to [1, Lemma 4.1] and has
already been discussed in (3); the second statement has been discussed towards the
end of Section 1.4. Nevertheless, we restate it here for completeness and refer to the
mentioned references for proofs.

Lemma 3.2. Let y ∈ K N0 be a q-regular sequence with linear representation (u, M, w)
and let n ∈ N0. Then we have
 y(n) = uM(digitsq(n))w. (5)

Furthermore, we have M(0)w = w.
 8

In the following lemma, for b = a0 . . . aℓ−1 ∈ A⋆
q, we set

value(b) :=
 ℓ−1∑

j=0 ajqj,

with the usual convention that if b is the empty word in A⋆
q, then value(b) = 0.

Lemma 3.3. Let y ∈ K N0 be a q-regular sequence and (u, M, w) a linear representation
of y. Then y(value(b)) = uM(b)w

holds for all b ∈ A⋆
q. In particular, the value of uM(b)w is independent of the particular
choice of the linear representation (u, M, w) of y and of trailing zeros of b.

Proof. Let b ∈ A⋆
q and write b = c0ℓ for some c ∈ A⋆
q and some ℓ ∈ N0 such that ℓ is
maximal. Then value(b) = value(c), and by (5), we have

y(value(c)) = uM(c)w.

As M(0)w = w by Lemma 3.2, we also have

uM(b)w = uM(c)M(0)
ℓw = uM(c)w,

as required.

Deﬁnition 3.4. Let y ∈ K N0 be a q-regular sequence with linear representation (u, M, w).
Then the recognisable series x ∈ K A⋆ with linear representation (u, M, w) is called the
recognisable series associated to y.

Remark 3.5. From Lemma 3.3 we see that the recognisable series associated to a q-regular
sequence is well deﬁned. From Lemma 3.2 we see that a recognisable series associated to
a q-regular sequence is compatible. Moreover, we see that every linear representation of
a q-regular sequence is also a linear representation of its associated recognisable series.

Theorem 3.6. Let y be a q-regular sequence and (u, M, w) be a minimal linear represen-
tation of the recognisable series associated to y. Then (u, M, w) is a linear representation
of y, and it is also minimal.

In other words, to ﬁnd a minimal linear representation of a regular sequence, we can
use the minimisation algorithm presented by Berstel and Reutenauer [3, Chapter 2]
on the associated recognisable series, i. e., the recognisable series with the same linear
representation as the regular sequence.

Proof of Theorem 3.6. Let x denote the recognisable series associated to y and D de-
note the dimension of (u, M, w). By Remark 3.5, x is compatible, and therefore, by
Proposition 2.3 (see Remark 2.5), we have M(0)w = w.
We deﬁne a vector-valued sequence v ∈ (K D×1)N0 by v(0) := w and (2) for all n ∈ N0
and r ∈ Aq. Note that M(0)w = w implies the validity of (2) for n = 0 and r = 0.

9

By the above deﬁnition of v and Lemma 3.3, (u, M, w) is indeed a linear representation
of y.
Now, any linear representation of the q-regular sequence y of dimension D′ is also
a linear representation of the recognisable series x by Remark 3.5. Therefore, due to
minimality of (u, M, w), we have D′ ≥ D. In particular, by choosing a minimal linear
representation of y, we see that (u, M, w) is a minimal linear representation of y as
well.

At last, we can relax the assumptions of Theorem 3.6 and ask: Given a q-regular
sequence with minimal linear representation, can we ﬁnd a recognisable series that gives
the same values for each standard qary expansion of a non-negative integer, but whose
minimal linear representation has a smaller dimension than that of the regular sequence?
The following example provides an aﬃrmative answer.

Example 3.7. Let us consider the recognisable series x ∈ C{0,1}⋆ with x(b) = 2t and t
counting the letter 0 in b ∈ {0, 1}⋆. Note that x(b0) = 2x(b) ̸= x(b) for all b ∈ {0, 1}⋆;
in particular, x is not compatible. Moreover, a minimal linear representation (u, M, w)
of x is given by

u = (1) ∈ C1×1, M(0) = (2) ∈ C1×1, M(1) = (1) ∈ C1×1 and w = (1) ∈ C1×1.

In contrast, let y ∈ CN0 be the 2-regular sequence with y(n) = x(digits2(n)) for all
n ∈ N0. Then (u′, M ′, w′) with

u′ = (
1 0) , M ′(0) =
 (2 −1
0 1
 ) , M ′(1) =
 (
1 0
0 0
) and w′ =
 (
1
1
)

is a minimal linear representation of y.
Therefore, starting with the 2-regular sequence y whose minimal representation has
dimension 2 can lead to a minimal representation of dimension 1 of a recognisable series
when ignoring trailing zeros.

References

[1] Jean-Paul Allouche and Jeﬀrey Shallit, The ring of k-regular sequences, Theoret.
Comput. Sci. 98 (1992), no. 2, 163–197. MR 1166363

[2] , Automatic sequences: Theory, applications, generalizations, Cambridge
University Press, Cambridge, 2003. MR 1997038 (2004k:11028)

[3] Jean Berstel and Christophe Reutenauer, Noncommutative rational series with ap-
plications, Encyclopedia of Mathematics and its Applications, vol. 137, Cambridge
University Press, Cambridge, 2011. MR 2760561

[4] Philippe Dumas, Asymptotic expansions for linear homogeneous divide-and-conquer recurrences: Algebr
Theoret. Comput. Sci. 548 (2014), 25–53.

10

[5] Clemens Heuberger and Daniel Krenn, Asymptotic analysis of regular sequences, Al-
gorithmica 82 (2020), no. 3, 429–508. MR 4058416

[6] Clemens Heuberger, Daniel Krenn, and Gabriel F. Lipnik,
Asymptotic analysis of q-recursive sequences, Algorithmica 84 (2022), no. 9,
2480–2532. MR 4467813

[7] The SageMath Developers, SageMath Mathematics Software (Version 10.0), 2023,
http://www.sagemath.org.

[8] Marcel-Paul Schützenberger, On a special class of recurrent events, Ann. Math.
Statist. 32 (1961), 1201–1213. MR 133894

[9] , On the deﬁnition of a family of automata, Information and Control 4
(1961), 245–270. MR 135680
 11
