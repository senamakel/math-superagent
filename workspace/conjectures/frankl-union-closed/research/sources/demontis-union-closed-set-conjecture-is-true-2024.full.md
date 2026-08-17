<!-- source: https://arxiv.org/pdf/2405.03731 | converted from PDF -->

arXiv:2405.03731v1  [math.CO]  6 May 2024The union-closed set conjecture is true

Roberto Demontis ∗

Abstract

We prove that the conjecture made by Peter Frankl in the late 1970s is
true. In other words for every ﬁnite union-closed family which contains a non-
empty set, there is an element that belongs to at least half of its members.

The union-closed set conjecture is one of the most famous combinatorial prob-
lems. It asserts that for every ﬁnite union-closed family which contains a non-empty
set, there is an element that belongs to at least half of its members. In literature,
there have been several partial results regarding this, as can be seen from the survey
paper of Bruhn and Schaudt [4]. For instance, in [1] V. B. Alekseev approximates
the number of union-closed families of subset of [n]. In [2] I. Balla , B. Bollob`as
and T. Eccles prove that the conjecture occurs for union-closed families with more
sets compared to the size of the universe, this size has been further improved by
Eccles in [5]. On the other hand in [3] I. Boˇsnjak and P. Markovi´c show that the
conjecture is true for any-closed family with a universe of 11 elements. Moreover in
[6] V. Falgas-Ravry proves that if a union-closed set with a universe of n elements
contains at most 2n element with the property to be separated, then the conjecture
holds. Moreover in [7] J. Massberg reinforces the latter result.

First of all we introduce some preliminary terminology and notation according
to the literature.
We call A = 2[n]−{∅}. We will use uppercase letters for elements of A , lowercase
letters for elements of ∪A, mathcal character uppercase letters for subsets of A.
Let F ⊆ A union-closed if for all X, Y ∈ F , X ∪ Y ∈ F .
For all i ≤ n we say F i = {X ∈ F : i ∈ X}.
We note |A| = 2n − 1 and |Ai| = 2n−1.
The purpose of this paper is to prove

Theorem 1 Let F ⊆ A be a union-closed set, we can ﬁnd i ≤ n such that

|F | ≤ 2|F i|.

∗robdemontis@gmail.com
 1

Summarizing the structure of the paper we say that we want to imagine each
union-closed set F obtained as the successive deletion of sets from the universe A:

1. Lemma 1, 2, 3 illustrate the properties of some elements of an union-closed
set, that we will call basis of F .

2. Theorem 2 shows that it is possible to obtain each union-closed set F through
successive deletions of individual elements of A so as to have only union-closed
sets during the whole procedure.

3. Lemma 5 shows that we can get a sequence described in Theorem 2 in which
the sets containing a certain element are eliminated only at the the end of the
procedure.

4. In Theorem 3 and Lemma 6 we create a sequence in which it is possibile to
use induction.

5. In Theorem 4 and Theorem 5 we prove a sentence that implies theorem 1.

Now we start the proof:

Deﬁnition 1 The set B(F ) = {X ∈ F | ∀Y, Z ∈ F − {X} : X ̸= Y ∪ Z} is said
basis of F .

We can prove

Lemma 1 For all X ∈ F , not necessarily union-closed, we can always ﬁnd a set
T = {T1; . . . ; Tr} ⊆ B(F ), such that X = ∪T .

Proof. By induction on |X| in F .
By deﬁnition of basis, if |X| = minY ∈F |Y |, we must have X ∈ B(F ), then we
set T = {X} and so the Lemma is true.
If |X| > minY ∈F |Y | we have two possibilities:

1. X ∈ B(F ), in this case the Lemma is true.

2. X /∈ B(F ), in this case X = Y ∪ Z, with Y, Z ∈ F and |Y |, |Z| < |X|, so the
Lemma is true by induction.
 □

Now we want to describe how to build a union-closed set F through successive
eliminations of elements of A.

Deﬁnition 2 For each F ⊆ A union-closed set, we say sequence from A to F
the sequence of sets A0, A1 . . . , At such that:

2

1. A0 = A,

2. A1 = A0 − {X1}

3. Ar = Ar−1 − {Xr}

4. At = At−1 − {Xt} = F .

Deﬁnition 3 For all union-closed sets F ⊆ A, we say union-closed sequence
from A to F the sequence A0, A1 . . . , At such that: ∀i = 1 . . . t Ai is a union-closed
set.

By the following two Lemmas, we will prove that for each F ⊆ A union-closed
set a union-closed sequence from A to F exists.

Lemma 2 Let F ⊆ A be a union-closed set, let B ∈ B(F ), F − {B} is a union-
closed set.

Proof. It is suﬃcient to observe that by deﬁnition of basis for each X, Y ∈ F − {B}
X ∪ Y ̸= B. As a consequence X ∪ Y ∈ F − {B}. □

Lemma 3 Let F ⊆ A (F is not neccessarily union-closed) let Z ∈ F − B(F ), then
B(F ) ⊆ B(F − {Z}).

Proof. Let T ∈ B(F ), for all X, Y ∈ F − {T } we have X ∪ Y ̸= T .In other words we
can claim that ∀X, Y ∈ F − {T ; Z} X ∪ Y ̸= T , as a consequence T ∈ B(F − {Z}).
□

Theorem 2 Let F ⊆ A be a union-closed set, then it exists a union-closed sequence
from A to F .

Proof. Let A0, A1 . . . , At a sequence from A to F .
If B(Ar−1) is not a subset of F then we can always choose Xr ∈ B(Ar−1) − F ,
so that Ar = Ar−1 − {Xr} is union-closed by Lemma 2 and F ⊂ Ar.
So the condition that may stop this process is when it exists q such that B(Aq−1) ⊆
F . In this case we must have that for all k ≥ q B(Aq−1) ⊆ B(Ak) by Lemma 3.
As a consequence B(Aq−1) ⊆ B(At). Let X ∈ Aq−1 − At, by Lemma 1 it exists
T = {T1; . . . Tr} ⊂ B(Aq−1) such that X = ∪T .
But B(Aq−1) ⊆ B(At), by hypothesis At = F union-closed set , then X ∈ At,
so we have found a contradiction.
In conclusion we can always choose {Xq} so that Aq is a union-closed set and in
this way we can build an union-closed sequence from A to F . □

3

A trivial example of union-closed sequence from A to F is a sequence in which
the elements X1, . . . Xt have the property that |Xi| ≤ |Xj| if i < j. Indeed we
can build a union-closed sequence starting from the end. Consider Xt such that for
all i we have |Xt| ≥ |Xi|, it must be F ∪ {Xt} is union-closed, as for all P ∈ F ,
P ∪ Xt ∈ F ∪ {Xt}.
Now we deﬁne D = A − F , D is the set of the elements eliminated by A in a
sequence from A to F .

Lemma 4 For all j ∈ ∪A, F ∪ Dj is a union-closed set.

Proof. Let X, Y ∈ F ∪ Dj we have two cases:

1. X, Y ∈ F , as F is a union-closed X ∪ Y ∈ F and then X ∪ Y ∈ F ∪ Dj.

2. X ∈ F ∪ Dj and Y ∈ Dj, as a consequence j ∈ X ∪ Y /∈ (D − Dj) and then
X ∪ Y ∈ F ∪ Dj.
 □

By the previous Lemma we can state the following deﬁnition

Deﬁnition 4 Let i be such that Di ̸= ∅. A union-closed sequence from A to F
deﬁned by D = {X1; . . . X|D|} is said to be an ideal sequence if and only if

1. A0 = A

2. for all l ≤ |D| − |Di| we have i /∈ Xl and Al = Al−1 − {Xl}.

3. for all s > |D| − |Di| we have i ∈ Xs and As = As−1 − {Xs}.

4. A|D| = F

Lemma 5 For all union-closed sets F ⊆ A there is an ideal sequence from A to F .

Proof.
By Lemma 4, F ∪ Di is a union-closed set. Thus, by Theorem 2, we can ﬁnd an
union-closed sequence from A to F ∪ Di.
Now we can build a union-closed sequence from F ∪ Di to F . Suppose Di =
{X1; . . . Xr} with the property |Xp−1| ≤ |Xp|. For all s > |D| − |Di| we have
A|D|−|Di|+1 = F ∪ Di − {X1} and As = As−1 − {Xs}.
Suppose for the sake of contradiction that in this sequence, Av is not union-
closed: we can ﬁnd Y, T ∈ Av such that Y ∪ T = Xv /∈ Av, obviously we must have
|Y |, |T | < |Xv|.
By construction of sequence for all k > v |Xk| ≥ |Xv|, then Y, T ∈ F and F is
not union-closed, hence there is a contradiction. As a consequence we have described
a way to build an ideal sequence. □

4

Deﬁnition 5 For all sets Y and X the set EX (Y ) = {T ∈ A|Y ⊆ T ⊆ Y ∪ X} is
called extension of Y on X.

Deﬁnition 6 X ∈ D is said to be vincolated if F ∪ {X} is not union closed. In
other words X ∈ D is said vincolated if ∃Y ∈ F such that X ∪ Y ∈ D.

Deﬁnition 7 X ∈ D is said to be vincolated to Y ∈ D if F ∪ {X} is not union
closed, but F ∪ {X; Y } is union closed.

Theorem 3 Let F ⊆ A be a union-closed set, let D = A − F , then if each X ∈
D − Di is vincolated, then it is possible to ﬁnd an element Y ∈ D − Di vincolated to
a non-vincolated R ∈ Di.

Proof.
Let Y ∈ D−Di of maximum cardinality on D−Di. By hypothesis Y is vincolated,
then it is possible to ﬁnd X ∈ F such that Y ∪ X = R ∈ D. Moreover, as Y has
maximum cardinality on D − Di, we must have R ∈ Di. As a consequence EX(Y )
must be a subset of D, otherwise F is not union-closed. Indeed for all T ∈ EX(Y )
we have T ∪ X = R. As we suppose Y has maximum cardinality we must conclude
Y ∪ {i} = R.
Moreover we have to observe that R could not be the set of maximum cardinality
in Di. In this case for the sake of contradiction suppose that R could be vincolated.
It means that we must have K ∈ Di, then we can ﬁnd P ∈ F such that P ∪ R = K.
But F is union-closed, then P ∪ X = P ′ ∈ F , then Y ∪ P ′ = K and EP ′(Y ) ⊆ D.
As a consequence there must be an element Y ∗ ∈ D − Di such that |Y ∗| > |Y | and
we ﬁnd a contradiction.
As a conclusion R is not vincolated and F ∪ {R} is union-closed. We want to
prove that F ∪ {R; Y } is union-closed. Suppose it is not. It would imply that Y is
vincolated to K ∈ Di with Y ⊂ R = Y ∪ {i} ⊂ K, then, by deﬁnition, we could
ﬁnd S ∈ F ∪ {R} such that Y ∪ S = K ∈ D. We have two cases:

1. S ̸= R thus R ∪ S = K ∈ D, then R is vincolated to K, that would be a
contradiction.

2. S = R thus K = R and we ﬁnd a contradiction because R ∈ F ∩ D = ∅.
 □

Deﬁnition 8 Let D = A − F and let Di ̸= D. A sequence A0, A1 . . . , At from A
to F is said optimal for i if and only if

1. i ∈ Xt,

2. i /∈ Xt−1
 5

3. Let A0, A1 . . . , At−2 is an ideal sequence from A to F ∪ {Xt; Xt−1}.

Lemma 6 If Di ̸= D, it is always possible to build an optimal sequence for i on D.

Proof.
We consider two diﬀerent cases:

1. if each X ∈ D − Di is vincolated, then by Theorem 3 it is possible to ﬁnd
an element Y ∈ D − Di vincolated to a non-vincolated R ∈ Di. Thus we can
build an ideal sequence A0, A1 . . . , At−2 from A to F ∪ {Y ; R} and an optimal
sequence from A to F with R = Xt and Y = Xt−1.

2. Otherwise it means that it exists an element X ∗ ∈ D − Di not vincolated, that
means F ∪ {X ∗} is union closed.

As F ∪{X ∗} is union closed, by Lemma 5 we have an ideal sequence A0, A1 . . . , At−1
from A to F ∪ {X ∗}, note that we must have F ∪ {X ∗; Xt−1} union closed
with i ∈ Xt−1 by deﬁnition of ideal sequence.

As a consequence consider the ideal sequence A0, A1 . . . , At−2 from A to F ∪
{X ∗; Xt−1}.

We set A′t−1 = At−2 − {X ∗}. A′t−1 must be union closed. If A′t−1 were not
union closed, as we know F is union closed, we would have S ∈ F such that
S ∪ Xt−1 = X ∗. That is impossible as i ∈ Xt−1 and i /∈ X ∗.

At the end we set A′t = A′t−1 − {Xt−1}. A′t = F then it is union closed.

In this way the sequence A0, A1 . . . , At−2, A′t−1, A′t is an optimal sequence
from A to F .
 □

Deﬁnition 9 Let D = A − F , i is said quasiminimal on D for a set Y =
{Y1; Y2} ⊂ F if and only if

1. i belongs to Y2

2. i does not belong to Y1

3. i is minimal on D ∪ Y

4. there exists an optimal sequence A0, A1 . . . , At+2 from A to F − Y such that
At+1 = At − {Y1} and At+2 = At+1 − {Y2}. As the optimal sequence ends with
F − Y, this set is union-closed.

Theorem 4 For all D, it exists i such that if it exists a set Y = {Y1; Y2} i quasi-
minimal on D for Y, then 2|(D ∪ Y)i| ≤ |(D ∪ Y)| + 1.

6

Proof.
By induction on |D|. If |D| = 0, for some i, if we can choose a set Y, by deﬁnition
of quasiminal we have 2|(D ∪ Y)i| ≤ |(D ∪ Y)| + 1.
If |D| = 1: as F is union closed, we must have for some j D = {{j}}. As a
consequence for all i we can choose a set Y i quasiminimal on D for Y we have
2|(D ∪ Y)i| ≤ |(D ∪ Y)| + 1.
If |D| = 2, as F is union closed, for some j; k we must have D = {{k}; {j}} or
D = {{j}; {k, j}}. As a consequence for all i we can choose a set Y i quasiminimal
on D for Y we have 2|(D ∪ Y)i| ≤ |(D ∪ Y)| + 1.
In general, let suppose the theorem true for |D| ≤ t and we prove it for |D| = t+1.
Particularly given a sequence from A to F , we indicate Dj = {X1, . . . Xj}. Consider
two diﬀerent cases:

1. Suppose that for some i that satisfay the theorem for Dt−1, |Di| < |D|, and by
Lemma 6 we have A0, A1 . . . , At+1 optimal sequence for i. If we could choose
Y such that i quasiminimal on D for Y, we could do as follows. We split
Dt+1 = Dt−1 ∪ {Xt; Xt+1}, such that i /∈ Xt and i ∈ Xt+1. By deﬁnition i
quasiminimal on Dt−1. Thus, by inductive hypothesys, 2|(Dt−1 ∪ {Xt; Xt+1} ∪
Y)i| ≤ |(D ∪ Y)| + 1.

2. Suppose i satisfay the theorem for Dt−1 and |Di| = |D|. Suppose a set Y
exists such that i quasiminimal on D for Y. That means i is minimal on
D ∪ {Y1; Y2}, thus i must be minimal in D ∪ {Y1}, as a result we have by
deﬁnition i quasiminimal on Dt for {Y1; Xt+1}.

Observe that A − (Dt ∪ {Y1}) is union-closed, because A − (Dt ∪ {Y1; Xt+1})
is union-closed and i ∈ Xt+1. On the other words for all T ∈ A − (Dt ∪ {Y1}).
T ∪ Xt+1 ∈ A − (Dt ∪ {Y1}).

As conclusion, 2|(Dt+1 ∪ {Y1; Y2})i| = 2|(Dt ∪ {Y1; Xt+1} ∪ {Y2})i| = 2|Di
t| + 4.
Moreover, by inductive hypothesys 2|(Dt ∪ {Y1; Xt+1} ∪ {Y2})i| ≤ |Dt| + 1 +
2 + 2.As a result, as 2|Di
t| + 4 ≤ |Dt| + 1 + 2 + 2 and |Di
t| = |Dt|, we have
|Dt| = 1 and we have just proved it at the inductive step.
 □

Theorem 5 Let D = A − F and let j minimal on D, with |D| > 1 . Then 2|Dj| ≤
|D| + 1.

Proof. First of all we deﬁne j minimal on D if and only if for all k |Dj| ≤ |Dk|. As
D ̸= {{j}} by hypothesys, |Dj| ̸= |D|.
By Lemma 6 it always possible to build an optimal sequence for j on D. Let
A0, A1 . . . , At+1 this optimal sequence from A to F , by deﬁnition we must have

7

1. j belongs to Xt+1

2. j does not belong to Xt

3. j is minimal on Dt−1 ∪ {Xt; Xt+1}

4. it exists an optimal sequence A0, A1 . . . , At+1 from A to F .

By Theorem 4, it exists i, not necessarily diﬀerent from j, such that for the
set {Xt; Xt+1} i quasiminimal on Dt−1 for {Xt; Xt+1} and 2|(Dt−1 ∪ {Xt; Xt+1}i| ≤
|Dt−1 ∪ {Xt; Xt+1}| + 1.
As a consequence 2|Di| ≤ |D| + 1. and by deﬁnition of minimality of j and
quasiminimality of i we have 2|Dj| = 2|Di| ≤ |D| + 1. □

Now we can prove Theorem 1
Proof. We just remember that |A| = 2n − 1 and |Ai| = 2n−1.

|F | = |A| − |D| = 2|Ai| − 1 − |D| ≤ 2|Ai| − 2|Di| = 2|F i|
 □

References

[1] V.B. Alekseev. On The Number of Intersection Semilattices. Diskretnaya Matem-
atika, 1:129-136, 1989.

[2] I. Balla, B. Bollob`as, T. Eccles. Union-Closed Families of Sets. Journal of
Combinatorial Theory, Series A, 120(3):531–544, 2013.

[3] I. Boˇsnjak , P. Markovi´c. The 11-element Case of Frankl’s Confecture Eletronic
Journal of Combinatorics, 15. Research Paper 88. (2008).

[4] H. Bruhn, O. Scahudt. The Journey of the Union- Closed sets Conjecture.
Graphs and Combinatorics 31 (6) (2015) 2043–2074.

[5] T. Eccles. Result for the Union-Closed size Problem. Combinatoris, Probability
and Computing, 25(3):399–418, 2016.

[6] V. Falgas-Ravry. Minimal Weight in Union- Closed Families. Eletronic Journal
of Combinatorics, 19 (P95):114. 2011.

[7] J. Massberg. The Union-Closed Sets Conjecture for small Families. Graphs and
Combinatorics,32(5):2047–2051. 2016.

[8] D.G. Sarvate, J. C. Renaud. On the union-closed sets conjecturei. Ars Combin.
27 (1989) 149–153.
 8
