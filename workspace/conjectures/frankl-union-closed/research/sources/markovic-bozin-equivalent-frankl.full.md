<!-- source: https://people.dmi.uns.ac.rs/~markovicp/papers/AAA99%20-%20handout.pdf | converted from PDF -->

On Vladimir Boºin's equivalent to Frankl's
union-closed sets conjecture
 Petar Markovi¢

University of Novi Sad, Serbia

Arbeitstagung Allgemeine Algebra 99, Siena, February 2020

Frankl's conjecture
 It is a simple enough statement:

Conjecture (P. Frankl, 1979)

Let F be a ˝nite family of ˝nite sets closed under unions. If
F ̸= {∅}, then there exists a ∈ ⋃ F which is an element of at
least one-half of the sets in F.

Equivalently,

Conjecture
Let L be a ˝nite lattice. Then there exists a join-irreducible
element a ∈ L such that |a↑| ≤ 1
2 |L|.

Probably around 100 research papers and surveys written on it,
some by famous people (Poonen, Stanley, Bollobas, . . . )

Weights
 Poonen [1992] introduced weights on elements. The idea was
used for several things:

• Families on a small enough set satisfy the conjecture,
• Families with few enough sets satisfy the conjecture,
• Finding FC families - when an FC family F is a subfamily
of an union-closed family G, then the conjecture is true
with one of the elements of ⋃ F being in ≥ half of the sets.

Ultimately, these weights just allow for quick checking of large,
but ˝nite sets of cases - useless for the whole problem.

The version we'll work with today and a bit of notation

De˝nition
Let T be a nonvoid ˝nite set. We say F ⊆ P (T ) is an IC family
[on T ] if T, ∅ ∈ F and F is closed under intersection.

For an IC family F ⊆ P (T ), Fa := {X ∈ F : a ∈ X},

fF (a) := |Fa|
|F| - the frequency of a [in F].

Conjecture
Frankl's conjecture says that for every IC family F on T there
exists a ∈ T such that fF (a) ≤ 1
2 .

Note that each IC family F, together with inclusion, forms the
lattice L(F).

More notation
 [N ] := {1, 2, . . . , N }.

When certain parameters get large, a ≪ b means that the ratio
a
b tends to in˝nity, and a ≈ b means that the same ratio tends
to 1.

For an IC family A ⊆ P (T ),

πX (A) := {X ∩ Y : Y ∈ A},

Probability measure is p : A → [0, 1] so that ∑

X∈A p(X) = 1, and

P (a ∈ X) := ∑

X∈Aa p(X);

E(f (X)) := ∑

X∈A p(X)f (X);

Ap := {X ∈ A : p(X) > 0}.

The Equivalence Theorem

Theorem (The Equivalence Theorem, V. Boºin, 2004)

Frankl's Conjecture is true i˙ for every IC family A ⊆ P (T ),
and every probability measure p : A → [0, 1] which satis˝es
P (a ∈ X) ≥ 1 − fA(a) for all a ∈ T ,

E(log |πX (A)|)
log |A| ≥ 1
2 .

The main di˙erence compared to old weights: The probability
measure assigns weights to sets, and this is more general than
each element having its weight.

The proof of (⇐)

Assume that Frankl's Conjecture is false for some IC family
A ⊆ P (T ).

Then there exists some q > 1
2 such that for all a ∈ T , fA(a) ≥ q.

Hence for all a ∈ T , 1 − fA(a) ≤ 1 − q.

Select p(T ) = 1 − q, and p(∅) = q.

Then for all a ∈ T , P (a ∈ X) = 1 − q ≥ 1 − fA(a) and

E(log |πX (A)|)
log |A| = (1 − q) log |A| + q log 1
log |A| = 1 − q < 1
2 .

The proof of (⇒): Synopsis

We aim toward constructing two IC families of sets, A3 and C,
both on a universe consisting of two types of elements, the
a-elements and the c-elements. A3 and C will have the following
properties: • {X ∩ Y : X ∈ A3, Y ∈ C} ⊆ C,
• fA3(a-element ) + fC(a-element ) > 1,
• fA3(c-element ) − 1
2 > 1
2 − fC(c-element ) > 0 and
• |A3| ≫ |C|.

Then we make a convex combination of one copy of A3 and
below it many copies of C so that the number of sets in the
copies of C is almost equal to |A3|. Thus the frequencies of all
elements in the combination are ≈ the arithmetic mean of the
frequencies in A3 and C, hence greater than 1
2 .

The construction A ⊗ I

Let A ⊆ P (T ) be an IC family and I a nonvoid set. The IC
family A ⊗ I ⊆ P (T × I) is given by:

For any X ⊆ T × I, X ∈ A ⊗ I if for all i ∈ I, X ∩ (T × {i}) ∈ A.

In other words,
• The universe of A ⊗ I can be seen as a disjoint union of |I|
copies of the universes of A,
• and the sets in A ⊗ I are represented by sequences of sets
in A of length |I|, where Xi := {a ∈ T : (a, i) ∈ X}.

Properties: • The lattice L(A ⊗ I) ∼= (L(A))|I|.
• fA⊗I (a, i) = fA(a) for all a ∈ T and i ∈ I.
• (A ⊗ I) ⊗ J = A ⊗ (I × J), up to ((a, i), j) ↔ (a, (i, j)).

For X ∈ A, X I denotes the constant tuple in A ⊗ I, i.e.
Y = X I i˙ for all i ∈ I, Yi = X.

The proof of (⇒): On the constants

We will have four natural parameters K1, K2, K3 and K4.

The ˝rst two are related by K1 > 2K2 and both are chosen
simultaneously as large enough that several conditions are
ful˝lled (the conditions will be speci˝ed by-and-by).

The frequencies of c-elements in A3 and C depend on these two
parameters.

Then the other two parameters are chosen, even larger than the
˝rst two, depending on the choice of K1 and K2, and such that
the ratio K3
K4 is ˝xed.

K3 makes |A3| grow but does not a˙ect |C|, while K4 makes |C|
grow but does not a˙ect |A3|.

The proof of (⇒): The initial adjustment

Assume that A ⊆ P (T ) is an IC family, and p : A → [0, 1] a
probability measure so that P (a ∈ X) ≥ 1 − fA(a) for all a ∈ T ,
but E(log |πX (A)|)
log |A| < 1
2 .

Due to continuity, we may slightly increase p(T ) and decrease
all other positive p(X) so that
• for some t > 0, P (a ∈ X) ≥ 1 − fA(a) + t for all a ∈ T ,
• p(X) ∈ Q for all X ∈ A and still

• E(log |πX (A)|)
log |A| = m < 1
2 .

The constants t > 0 and 0 < m < 1
2 are ˝xed from now on.

The proof of (⇒): The family A1

We introduce the parameters K1, K2 ∈ N. Let K2 > 1
1
2 −m ,

K1 > 2K2 and K1 is a common multiple of all denominators of
p(X), X ∈ A. Moreover, both K1 and K2 must be large enough
(denoted: K1 ≫ 1 and K2 ≫ 1) to make two further estimates
close enough for our purpose.

Let I := [K1].

Let A1 := A ⊗ I.

The proof of (⇒): The probability measure p1

Fix Z := {Zi : i ∈ [K1]}, such that for all i ∈ [K1], Zi ∈ A and
for all X ∈ A, if p(X) = k
K1 , then {i ∈ [K1] : Zi = X} is a set of
consecutive indices of size k.

De˝ne the probability measure p1 : A1 → [0, 1] by

p1(X) = { 1
K1 if (∃k ≤ K1)(∀i ∈ I)X ∩ (T × {i}) = Zi+k;
0 otherwise.

(Addition in indices is mod K1, so Ap1
1 consists of Z and its
cyclic permutations, each with the probability 1
K1 ).

We see that P1((a, i) ∈ X) = P (a ∈ X) for all a ∈ T .

Denote Ap1
1 := {Y ∈ A1 : p1(Y ) ̸= 0}. We have

|A
p1
1 | = {Z and all its cyclic permutations } = K1.

(Unless |Ap| = 1, which easily leads to a contradiction.)

The proof of (⇒): The expectation in A1

For each Y ∈ A1 such that p1(Y ) = 1
K1 (i.e. for Y ∈ A
p1
1 ),

|πY (A1)| =
 K1∏

i=1 πYi(A) = ∏

X∈A πX (A)
p(X)K1.

E(log |πY (A1)|)
log |A1| =
 ∑

Y ∈Ap1
1
 1
K1 log |πY (A)|

log |A1| =

K1
K1 log | ∏

X∈A πX (A)p(X)K1|

log |A1| = K1 ∑

X∈A p(X) log |πX (A)|

K1 log |A| =

E(log |πX (A|)
log |A| = m log |A|
log |A| = m.

To remember: For all Y ∈ A
p1
1 , |πY (A1)| = |A1|m < √
|A1|.

The proof of (⇒): The family A2

Let J = [2K2 − 1] and L = [K3]. K3 is such that K3 ≫ 2K2.

Let A2 ⊆ P (T × I × J × L) be given by
A2 := A ⊗ (I × J × L) = A1 ⊗ (J × L).

We know that fA2(a, i, j, l) = fA1(a, i) = fA(a) for all a ∈ T .
De˝ne p2 : A2 → [0, 1] by

p2(X) =
 



 1
K1 , if (∃Y ∈ A
p1
1 )(X = Y J×L)
(X is a constant tuple in A1 ⊗ (J × L));

0, otherwise.

Analogously as with A1, P2((a, i, j, l) ∈ X) = P (a ∈ X) and for
each Y ∈ A
p2
2 , the projection |πY (A2)| = |A2|m.

The proof of (⇒): The family A
′
3

We make A′
3 ⊆ P ({c1, . . . , c2K2−1} ∪ (T × I × J × L)) in several
steps:

First we consider only the sets Y ∈ A2 for which there exists
j ∈ J such that Y ∩ (T × I × {j} × L) = ∅.

For any Y ∈ A2 and j ∈ J such that Y ∩ (T × I × {j} × L) = ∅,
put X = Y ∪ {cj, cj+1, . . . , cj+K2−1} into the family AI
3.
(Addition in indices is modulo 2K2 − 1; we add exactly one set
into AI
3 for each suitable choice of the pair Y and j.)

Close AI
3 under intersections to obtain A′
3. Denote
AII
3 := A′
3 \ AI
3.

For any X ∈ AII
3 we will have |X ∩ {c1, . . . , c2K2−1}| < K2,
while for X ∈ AI
3, |X ∩ {c1, . . . , c2K2−1}| = K2.

The proof of (⇒): The frequencies in family A
′
3

|AI
3| = (2K2 − 1)|A|K1(2K2−2)K3.

Bounding |AII
3 | from above:

|A
II
3 | ≤
 2K2−1∑

t=2
 (
2K2 − 1
t
 )|A|
K1(2K2−1−t)K3 ≤

|A|
K1(2K2−3)K3 2K2−1∑

t=2
 (
2K2 − 1
t
 ) ≤ |A|
K1(2K2−3)K322K2−1 =

22K2−1

(2K2 − 1)|A|K1K3 |A
I
3| ≪ |A
I
3|.

(The last inequality used K3 ≫ K2.)

The frequency fA′
3(a, i, j, l) ≈ 2K2−2
2K2−1 fA(a) ≈ fA(a) and

fA′
3(cj) ≈ K2
2K2−1 . Using: |AI
3| ≫ |AII
3 | and K2 ≫ 1.

The proof of (⇒): The family A3

For j ∈ [2K2 − 1] we de˝ne new elements

Cj := {ci,j,k : 1 ≤ i ≤ K1, 1 ≤ k ≤ K4}.

K4 - a new large constant to be speci˝ed later.

A3 ⊆ P (C1 ∪ · · · ∪ C2K2−1 ∪ (A × I × J × L)) is obtained from
A′
3 by replacing each occurrence of cj with the whole subset Cj.

Still, |A3| = |AI
3| + |AII
3 | ≈ |AI
3| = (2K2 − 1)|A|K1(2K2−2)K3.

The frequencies of fA3(ci,j,k) = fA′
3(cj) while the frequencies of
(a, i, j, l) are unchanged.

The proof of (⇒): The family CI

Let Ap2
2 = {Xℓ : ℓ ∈ [K1]}.

For each ℓ ∈ [K1], let Dℓ be the Boolean family

Dℓ := P ({ci,j,k : i ∈ [K1] \ {ℓ}, j ∈ [2K2 − 1], k ∈ [K4]}).

De˝ne CI := K1⋃

ℓ=1
{Xℓ ∪ Y : Y ∈ Dℓ}.

We assume K4 ≫ K2 and 2K4 ≫ K1, but the relationship
between K4 and K3 TBD later.

The proof of (⇒): The family C - estimating |CI| and
|CII|

We de˝ne C′ to be the closure of CI under intersection,
CII := C′ \ CI , C := C′ ∪ {X ∩ Y : X ∈ C′, Y ∈ A3}, and
CIII := C \ C′. We estimate the sizes |CI | and |CII |.

|CI | = K12
(K1−1)(2K2−1)K4,

|CII | ≤
 K1∑

t=2
 (K1
t
 )
2(K1−t)(2K2−1)K4 <

K1∑

t=2 Kt
12
(2K2−1)(K1−t)K4 < 2
(K1−2)(2K2−1)K4 K2
1
1 − K1
2(2K2−1)K4 =

K1
2(2K2−1)K4(1 − K1
2(2K2−1)K4 ) |CI |

Since 2K4 ≫ K1, we get |CI | ≫ |CII |.

The proof of (⇒): The family C - estimating |CIII|

Any set X ∈ CIII is a disjoint union of X ∩ (C1 ∪ · · · ∪ C2K2−1)
and X ∩ (T × I × J × L).

X ∩ (C1 ∪ · · · ∪ C2K2−1) ⊆ {ci,j,k : i ∈ [K1] \ {ℓ},

j0 ≤ j < j0 + K2, k ∈ [K4]},

where (ℓ, j0) ∈ [K1] × [2K2 − 1] must be chosen ˝rst. So,
X ∩ (C1 ∪ · · · ∪ C2K2−1) can be chosen in at most

K1(2K2 − 1)2
(K1−1)K2K4

ways. X ∩ (T × I × J × L) is an element of πY (A2), where
Y ∈ A
p2
2 , so X ∩ (T × I × J × L) can be chosen in

K1|A2|
m = K1|A|
mK1(2K2−1)K3 = K12mK1(2K2−1)K3 log |A|

ways. Putting it all together we get

|CIII | ≤ K2
1 (2K2 − 1)2
(K1−1)K2K4+m log |A|K1(2K2−1)K3.

The proof of (⇒): Adjusting K3 and K4

In order to obtain |CIII | ≪ |CI | ≪ |A3|, it su˚ces to have the
desired inequalities among the exponents. So, we need

m log |A|K1(2K2 − 1)K3 < (K1 − 1)(K2 − 1)K4 and

(K1 − 1)(2K2 − 1)K4 < log |A|K1(2K2 − 1)K3.

These inequalities boil down to
 K1 − 1
K1 log |A| < K3
K4 < (K1 − 1)(K2 − 1)
mK1(2K2 − 1) log |A| .

For these to be possible, we need
 K1 − 1
K1 log |A| < (K1 − 1)(K2 − 1)
mK1(2K2 − 1) log |A| , equivalently

m < K2 − 1
2K2 − 1 , i.e. m < 1
2 − 1
2(2K2 − 1) ,

4K2 − 2 > 1
1
2 − m , which we know from K2 > 1
1
2 − m .

The proof of (⇒): The family C - estimating frequencies

We let K3 and K4 simultaneously tend to in˝nity, their ratio
˝xed and in the interval ( K1−1
K1 log |A| , (K1−1)(K2−1)
mK1(2K2−1) log |A| ). From

|C| ≈ |CI | we get

fC(a, i, j, l) ≈ fCI (a, i, j, l) = |{ℓ ≤ K1 : (a, i, j, l) ∈ Xℓ}|
K1 =

P2((a, i, j, l) ∈ X) = P (a ∈ X) > 1 − fA(a),

and fC(ci,j,k) ≈ fCI (ci,j,k) = K1 − 1
2K1 .

The proof of (⇒): Convex combination

We have |A3| ≫ |C| and we combine them:
Let M AX be the largest natural number such that
M AX · |C| < |A3|. We construct the IC family F of subsets of

(T × I × J × L) ∪ C1 ∪ C2 ∪ · · · ∪ CK1 ∪ {e1, e2, . . . , eM AX }

as C ∪ {X ∪ {e1, . . . , ek} : X ∈ C, 1 ≤ k < M AX}∪

{X ∪ {e1, . . . , eM AX } : X ∈ A3}.

The proof of (⇒): The frequencies in F

The frequencies of the new elements are all at least
 fF (ei) ≥ s := |A3|
|A3| + M AX|C| > 1
2 ,

while the frequencies of old elements are
 fF (x) = sfA3(x) + (1 − s)fC(x).

Here s > 1
2 but s ≈ 1
2 as K3 and K4 tend to in˝nity.

Thus

fF (a, i, j, l) ≈ sfA(a) + (1 − s)(1 − fA(a) + t) ≈ 1
2 + (1 − s)t > 1
2 .

Here we used s ≈ 1
2 ≈ 1 − s. Also,

fF (ci,j,k) ≈ s K2
2K2 − 1 + (1 − s) K1 − 1
2K1 > 1
2 .

The last follows from K1 > 2K2 and s > 1 − s. Thus F
contradicts Frankl's conjecture.

How to (maybe) apply the Equivalence Theorem

There are examples out there of IC families where the
frequencies of most elements fail Frankl's Conjecture, but a
small number of elements satis˝es it.

The idea is to construct a family and select a probability
measure such that each set with positive probability contains all
elements which satisfy Frankl's conjecture, and the probability
of the remaining ones being in a set satis˝es the condition of the
Equivalence Theorem.

Moreover, the conclusion of the Equivalence Theorem should
fail.

We have not been successful in constructing such a family and
probability measure yet.

Dedication
 This talk is dedicated to the memory of Velibor Tintor and
Jarda Jeºek.

THANK YOU FOR YOUR ATTENTION!
