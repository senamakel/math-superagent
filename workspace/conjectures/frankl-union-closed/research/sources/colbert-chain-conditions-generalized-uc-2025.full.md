<!-- source: https://arxiv.org/pdf/2310.02482 | converted from PDF -->

arXiv:2310.02482v2  [math.CO]  24 Sep 2024
Conjectures on union-closed families of sets

Christopher Bouchard

Abstract

A family of sets A is union-closed if it is ﬁnite and nonempty with member sets that are all ﬁnite and
distinct (at least one of which is nonempty) and it satisﬁes the property X, Y ∈ A =⇒ X ∪ Y ∈ A. Let(
S
k) be the set of all k-element subsets of a set S, and let [n] = {1, 2, · · · , n} represent ⋃
A∈A A. Further,
let AB = {A ∈ A | A ∩ B = B} and AB = {A ∈ A | A ∩ B = ∅}. We consider, for any union-closed family
A, the class of conjectures UCx : ∃B ∈ ( [n]
n−x+1
) | |AB| ≥ |AB|, where x ∈ [n]. The extremal case x = n is
equivalent to the union-closed sets conjecture, also known as Frankl’s conjecture, which states that there
exists an element of [n] that is in at least |A|
2 member sets of A. We prove UCx for x ∈ [⌈ n
3 ⌉ + 1], and
also investigate two strengthenings of the union-closed sets conjecture.

1. Introduction

A family of sets A is union-closed if it is ﬁnite and nonempty with member sets that are all ﬁnite and
distinct (at least one of which is nonempty) and it satisﬁes the property X, Y ∈ A =⇒ X ∪ Y ∈ A.
For a union-closed family A, let [n] = {1, 2, · · · , n} represent its base set ⋃
A∈A A. The union-closed sets
conjecture, also known as Frankl’s conjecture, states the following:

Conjecture 1.1. For any union-closed family A, there exists an element of [n] that is in at least |A|
2
member sets of A.

Conjecture 1.1 has been proved for n ≤ 12 (see [11]) and |A| ≤ 50 (see [5] and [9] together with
[11]). Equivalent conjectures include the lattice formulation of the union-closed sets conjecture, which
has been veriﬁed for lower semimodular lattices (see [8]), and the graph formulation of the union-closed
sets conjecture (see [1]). The frequency in A of an element y ∈ [n] is the number of member sets in A that
contain y. A popular approach to Conjecture 1.1 is to improve the lower bound for the highest frequency
of an element from [n], proving a sequence of increasingly stronger results. In [3], entropic methods were
used to prove that there exists an element from [n] that is in at least ε|A| member sets of A for a constant
ε = 1
100 , a result which in [10] was improved to ε = 3−√5
2 . Another well-studied approach aims to prove
the full lower bound |A|
2 for union-closed families that decrease in size |A| as a function of n. In [4],
methods of Boolean analysis were applied to prove Conjecture 1.1 for |A| ≥ 2
n−1. For a survey of many
results regarding Conjecture 1.1, see [2].
Let AB = {A ∈ A | A ∩ B = B}, AB = {A ∈ A | A ∩ B = ∅}, and AB1B2 = AB1 ∩ AB2 . Also, let
(
S
k) be the set of all k-element subsets of a set S. In the present work, we consider the following class of
conjectures for any union-closed family A:

UCx
x∈[n] : ∃B ∈
 ( [n]
n − x + 1

)
 such that |AB| ≥ |AB|. (1.1)

Conjecture 1.1 is itself the extremal case x = n of UCx, being equivalent to the statement ∃B ∈(
[n]
1 ) | |AB| ≥ |AB |. Therefore, another approach to Conjecture 1.1 is to prove UCx for increasing
x. We prove UCx for x ∈ [⌈ n
3 ⌉ + 1] and pose a question which, if answered in the aﬃrmative, would prove
UCx for x ∈ [⌊ n
2 ⌋ + 1], where ⌈ n
3 ⌉ is the smallest integer greater than or equal to n
3 and ⌊ n
2 ⌋ is the largest
integer less than or equal to n
2 . We then proceed to investigate two strengthenings of Conjecture 1.1:
one that imposes further constraint on the nested structure of union-closed families, and another that
proposes an alternate deﬁnition of a ﬁnite power set.

1

2. Considering UCx for various values of x ∈ [n]

We now prove, for any union-closed family A, UCx of (1.1) whenever x ∈ [⌈ n
3 ⌉ + 1].

Theorem 2.1. For any union-closed family A, ∀x ∈ [⌈ n
3 ⌉ + 1] UCx.

Proof. The case n = 1 consists of the statements ∃B ∈ (
[1]
1 ) | |AB| ≥ |AB | and ∃B ∈ (
[1]
0 ) | |AB | ≥ |AB|,
for which B = [1] and B = ∅, respectively. For n > 1, we use induction on x.

Base Case ( x = 1): ∃B ∈ (
[n]
n ) | |AB | ≥ |AB |.

Proof. [n] = ⋃
A∈A A and A is union-closed. Therefore, [n] ∈ A and |A[n]| = 1. If ∅ ∈ A then |A[n]| = 1,

and if ∅ ̸∈ A then |A[n]| = 0. In either case, B = [n] ∈ (
[n]
n ) with |AB| ≥ |AB|.

Induction Step: ∀x ∈ [⌈ n
3 ⌉](∃B ∈ ( [n]
n−x+1
) | |AB| ≥ |AB| =⇒ ∃B′ ∈ ( [n]
n−x) | |AB′ | ≥ |AB′ |).

Proof. We recall the notation AB1B2 = AB1 ∩ AB2 .

If ∃y′ ∈ B | A{y′}B\{y′} = ∅, then B′ = B \ {y′} with |AB′ | ≥ |AB| ≥ |AB| = |AB′ |.

Else, ∀y ∈ B A{y}B\{y} ̸= ∅, in which case we have the following:

∃C ∈ ( [n]
n−x) in A.

Proof. Consider the family P = ⋃
y∈B A{y}B\{y} and the set P = ⋃
p∈P p. We have that B ⊆ P ⊆ [n].
By the construction of P , ∀w ∈ P \ B ∃u ∈ B with a z ∈ A{u}B\{u} such that w ∈ z. Let Z be the family
containing a (possibly repeated) z for every w, so |Z| = |P \ B|, and let Z = ⋃
z∈Z z. Then Z ⊇ P \ B
and |Z| ≤ 2|P \ B|. By the union-closed property, Z must be in A if Z ̸= ∅. We observe that together
|B| = n−x +1, x ≤ ⌈ n
3 ⌉, |P | ≤ n, and |Z| ≤ 2|P \B| imply that |Z| ≤ 2⌈ n
3 ⌉−2. Similarly, |B| = n−x +1,
x ≤ ⌈ n
3 ⌉, and |P | ≥ |B| imply that |P | ≥ n − ⌈ n
3 ⌉ + 1. Therefore, |Z| < |P |, and P \ Z ̸= ∅. Now, consider
a V ⊊ P \ Z with |V | = n − x − |Z|. Such a V must exist because of the following two facts:

1.) n − x − |Z| ≥ 0, as x ≤ ⌈ n
3 ⌉ and |Z| ≤ 2|P \ B| ≤ 2|[n] \ B| = 2(n − (n − x + 1)) = 2x − 2, making
n − x − |Z| have a minimum of n − 3⌈ n
3 ⌉ + 2, which itself has a minimum of 0 when n = 3k + 1 for some
whole number k.

2.) n − x − |Z| < |P \ Z|, as |P \ Z| = |P | − |Z| and |P | ≥ |B| = n − x + 1.

Because V ⊊ P \ Z ⊆ B and ∀y ∈ B A{y}B\{y} ̸= ∅, we have that ∀v ∈ V ∃V ′ ∈ A{v}B\{v}. We collect
a V ′ for every v into a family V and let F = ⋃
V ′∈V V ′. By the union-closed property, F must be in A
if F ̸= ∅. Also, V ⊆ F and F \ V ⊆ P \ B ⊆ Z, making Z ∪ F = Z ∪ V . And because Z ∩ V = ∅, we
have |Z ∪ V | = |Z| + |V | = |Z| + (n − x − |Z|) = n − x. Thus, Z ∪ F ∈ ( [n]
n−x)
, and, noting that Z and F
cannot both be empty, we have that Z ∪ F is in A by the union-closed property.

Therefore, C = Z ∪ F , and C ∈ ( [n]
n−x) is in A.

It follows that |AC | ≥ |AC |, as any X in AC can be uniquely matched with C ∪ X in AC . C ∪ X must
be in AC by the existence of C in A and the union-closed property, and every C ∪ X must be unique as
∀X ∈ AC C ∩ X = ∅.

Thus, B′ = C is in ( [n]
n−x) with |AB′ | ≥ |AB′ |.

The induction step is proved, as we have proved the existence of a B′ in ( [n]
n−x) such that |AB′ | ≥ |AB′ |
when ∃y′ ∈ B | A{y′}B\{y′} = ∅, and when ∀y ∈ B A{y}B\{y} ̸= ∅.

As the induction step is proved, the proof of Theorem 2.1 is complete.

The proof method reached its limit as it achieved a minimum of n − x − |Z| = 0. We now consider a
question which, if answered in the aﬃrmative, would extend the result to x ∈ [⌊ n
2 ⌋ + 1].

Question 2.2. If F is a (not necessarily union-closed) ﬁnite family of (not necessarily distinct) ﬁnite
sets such that |F| > | ⋃
F ∈F F | + 1, must there exist F ′ ⊊ F with |F| − |F ′| = | ⋃
F ∈F ′ F | + 1?

Proposition 2.3. An aﬃrmative answer to Question 2.2 would prove, for any union-closed family A,
UCx for all x ∈ [⌊ n
2 ⌋ + 1].

Proof. The proof for x ∈ [⌊ n
2 ⌋ + 1] would start the same as the proof for x ∈ [⌈ n
3 ⌉ + 1] started (except
for the case n = 1 now consisting only of the statement ∃B ∈ ([1]
1 ) | |AB | ≥ |AB| (for which B = [1]),

2

and the induction step for n > 1 being extended from x ∈ [⌈ n
3 ⌉] to x ∈ [⌊ n
2 ⌋]). The proofs diﬀer in the
induction step in how they show existence of C. We resume the proof at that point:

∃C ∈ ( [n]
n−x) in A.

Proof. Recall that at this point in the proof we had assumed that ∀y ∈ B A{y}B\{y} ̸= ∅. Therefore,
there must be a family S ⊊ A with |S| = |B| such that ∀b ∈ B ∃S ∈ S ∩ A{b}B\{b}.

In this case, F from Question 2.2 corresponds to T = {S ∩ ([n] \ B) | S ∈ S}. T satisﬁes the deﬁnition
of F because |T | > | ⋃
T ∈T T | + 1, as |T | = |B| = n − x + 1 ≥ n − ⌊ n
2 ⌋ + 1 and | ⋃
T ∈T T | ≤ |[n] \ B| =
x − 1 ≤ ⌊ n
2 ⌋ − 1. Further, T need not be union-closed, and could have repeated member sets if some of
the member sets of S shared exactly the same elements from [n] \ B.

Now applying Question 2.2 to T , there exists T ′ ⊊ T with |T | − |T ′| = | ⋃
T ∈T ′ T | + 1. It follows that
| ⋃
T ∈T ′ T | + |T ′| = |T | − 1 = |B| − 1 = (n − x + 1) − 1 = n − x. Recall that every member set T
of T could be written as T = S \ {b} for some unique S ∈ S and b ∈ B. Let S ′ ⊊ S be the family
consisting of the corresponding S for every T ∈ T ′. Then | ⋃
S∈S′ S| = | ⋃
T ∈T ′ T | + |T ′| = n − x, as
⋃
S∈S′ S = (⋃
T ∈T ′ T ) ∪ B∗ and (⋃
T ∈T ′ T ) ∩ B∗ = ∅, where B∗ ∈ ( B
|T ′|)
. Finally, ⋃
S∈S′ S ∈ A by S ′ ⊊ A
and the union-closed property. Therefore, C = ⋃
S∈S′ S.

After C is shown to exist, the proof for x ∈ [⌊ n
2 ⌋ + 1] is the same as that for x ∈ [⌈ n
3 ⌉ + 1]. This concludes
the proof of Proposition 2.3.

We note that this particular method that ﬁnds C ∈ ( [n]
n−x) in A breaks down for x > ⌊ n
2 ⌋ in the
induction step. This is because the method is not able to guarantee that [n] \ B is not a proper subset
of C, and so a fundamental problem arises when |[n] \ B| ≥ |C|, which occurs in the induction step when
x ≥ n+1
2 .

The following theorem also deals with UCx of (1.1).

Theorem 2.4. For any union-closed family A with n > 1, UCn−1 =⇒ UCn.

Proof. Without loss of generality, let {1, 2} be the doubleton from UCn−1, so |A{1,2}| ≥ |A{1,2}|. Using
the notation A{1}{2} = A{1} ∩ A{2} and A{2}{1} = A{2} ∩ A{1}, we observe that if |A{1}{2}| ≥ |A{2}{1}|,
then the singleton from UCn is equal to {1}, as (A{1,2} ∪ A{1}{2} = A{1}) ∧ (A{1,2} ∩ A{1}{2} = ∅) =⇒
|A{1}| = |A{1,2}| + |A{1}{2}| and (A{1,2} ∪ A{2}{1} = A{1}) ∧ (A{1,2} ∩ A{2}{1} = ∅) =⇒ |A{1}| =
|A{1,2}| + |A{2}{1}|. Else, |A{2}{1}| > |A{1}{2}|, making the singleton from UCn equal to {2}, as (A{1,2} ∪
A{2}{1} = A{2}) ∧ (A{1,2} ∩ A{2}{1} = ∅) =⇒ |A{2}| = |A{1,2}| + |A{2}{1}| and (A{1,2} ∪ A{1}{2} =
A{2}) ∧ (A{1,2} ∩ A{1}{2} = ∅) =⇒ |A{2}| = |A{1,2}| + |A{1}{2}|. This concludes the proof of Theorem
2.4.

UCn−1 =⇒ UCn in fact holds for any ﬁnite family of ﬁnite sets with n > 1, whether the family
be union-closed or not. Further, by considering the contrapositive, we have a necessary condition for
any counterexample to Conjecture 1.1, namely that a counterexample ˜A on a base set [˜n] must have
| ˜A{x,y}| < | ˜A{x,y}| for every {x, y} in (
[˜n]
2 )
. Another question is the following:

Question 2.5. For a union-closed family A with n > 1, does UCn imply UCx for all x ∈ [n − 1]?

We have already veriﬁed by Theorem 2.4 that for a union-closed family A with n > 1, UCn−1 =⇒
UCn. For answering Question 2.5, a starting point could be to prove the converse, i.e. that UCn =⇒
UCn−1. At the core of understanding Conjecture 1.1 is understanding the union-closed property in
general. The following could help in this development:

1.) Answering Question 2.2 in the aﬃrmative, thus proving UCx for x ∈ [⌊ n
2 ⌋ + 1].

2.) Proving certain implications with regard to UCx, especially, for n > 4, ﬁnding x ∈ [n − 1] \ [⌈ n
3 ⌉ + 1]
such that UCx+1 =⇒ UCx.

3. A strengthening of Conjecture 1.1

Before presenting the strengthening of Conjecture 1.1, we discuss a theorem of Reimer in the context of
an important characteristic of union-closed families. The binary logarithm and natural logarithm of a
positive real number x are denoted by log(x) and ln(x), respectively.

Theorem 3.1 (Reimer [7]). For any union-closed family A, ∑n
k=1 |A{k}| ≥ |A|
2 log(|A|).

3

Theorem 3.1 was proved conclusively by Reimer without need of assuming Conjecture 1.1. However,
we show that Theorem 3.1 follows directly if we assume Conjecture 1.1, in order to highlight the nested
structure of union-closed families.

Proposition 3.2. Conjecture 1.1 =⇒ Theorem 3.1.

Proof. We show Theorem 3.1, assuming Conjecture 1.1. We use induction on size of the base set.

Base Case ( n = 1): The only two union-closed families on the base set [1] are {∅, {1}} and {{1}}. In
the ﬁrst case, ∑n
k=1 |A{k}| = 1 ≥ |A|
2 log(|A|) = log(2) = 1. In the second case, ∑n
k=1 |A{k}| = 1 ≥
|A|
2 log(|A|) = 1
2 log(1) = 0.

Induction Step: Without loss of generality, we consider a union-closed family A with n > 1 such that
|A{n}| = maxx∈[n]{|A{x}|}. We show that: (For every union-closed family A
∗ on a base set N ∗ ⊆ [n − 1],
∑
k∈N ∗ |A
∗ {k}| ≥ |A
∗|
2 log(|A
∗|)) =⇒ ∑n
k=1 |A{k}| ≥ |A|
2 log(|A|).

Proof. We have c = |A{n}|
|A| ∈ [ 1
2 , 1], as we are assuming Conjecture 1.1. Let A{n} ′ = {A\{n} | A ∈ A{n}}.
It follows that ⋃
A∈A{n}′ A = [n − 1], and ⋃
A∈A{n} A = N ⊆ [n − 1]. We consider three cases:

1.) A{n} = ∅ (i.e. c = 1): By the hypothesis of the induction step, we have ∑n−1
k=1 |(A{n} ′){k}| ≥

|A{n}′|
2 log(|A{n} ′|). In this case, |A{n} ′| = |A|, and ∑n−1
k=1 |(A{n} ′){k}| = (∑n
k=1 |A{k}|) − |A|. Therefore,
∑n
k=1 |A{k}| ≥ |A|
2 log(|A|) + |A| > |A|
2 log(|A|).

2.) A{n} = {∅}: By the hypothesis of the induction step, we again have ∑n−1
k=1 |(A{n}′){k}| ≥

|A{n}′|
2 log(|A{n} ′|). In this case, |A{n} ′| = |A| − 1, and ∑n−1
k=1 |(A{n} ′){k}| = (∑n
k=1 |A{k}|) − (|A| − 1).

Therefore, ∑n
k=1 |A{k}| ≥ |A|−1
2 log(|A| − 1) + |A| − 1. If |A|
2 log(|A|) is a lower bound for
|A|−1
2 log(|A| − 1) + |A| − 1, then it must also be a lower bound for ∑n
k=1 |A{k}|. Thus, in order to
prove that ∑n
k=1 |A{k}| ≥ |A|
2 log(|A|), it suﬃces to show that |A|−1
2 log(|A| − 1) + |A| − 1 ≥ |A|
2 log(|A|).

This is equivalent to showing that ( 2|A|−2
|A| )|A|−1 ( 2
|A|−1

|A| ) ≥ 1, which is true when |A| ≥ 2. Now,

A{n} = {∅} =⇒ ∅ ∈ A, and because A is union-closed, A must also contain its base set [n]. Thus,

|A| ≥ 2 and ∑n
k=1 |A{k}| ≥ |A|
2 log(|A|).

3.) A{n} ̸= ∅ ∧ A{n} ̸= {∅}: In this case, A{n} is union-closed in addition to A{n} ′ being union-closed,
and we establish a lower bound for ∑n
k=1 |A{k}| by solving the following problem:

min
c∈[ 1
2 ,1){I(c)}, where I(c) = c|A| + c|A|
2 log(c|A|) + (1 − c)|A|
2 log((1 − c)|A|).

In I(c), the ﬁrst term c|A| comes from the c|A| = |A{n}| number of times that element n was removed
from A{n} to make A{n} ′. By the hypothesis of the induction step, the second term c|A|
2 log(c|A|) is a
lower bound of ∑n−1
k=1 |(A{n}′){k}|, as c|A| = |A{n}| = |A{n} ′|, and the ﬁnal term (1−c)|A|
2 log((1 − c)|A|)

is a lower bound of ∑
k∈N |(A{n}){k}|, as (1 − c)|A| = |A{n}|. For c ∈ [ 1
2 , 1), dI
dc = |A| + |A|
2 (log(c) −

log(1 − c)) > 0, as dI
dc ∣
∣
∣c= 1
2 = |A| > 0 and when c ∈ [ 1
2 , 1), d2I
dc2 = |A|
2 ln(2) ( 1
c(1−c) ) > 0. Thus, the global

minimum of I(c) for c ∈ [ 1
2 , 1) is achieved uniquely at c = 1
2 . Plugging this minimizer into I(c) gives

I( 1
2 ) = ( 1
2 )|A| + ( 1
2 )|A|
2 log(( 1
2 )|A|) + (1− 1
2 )|A|
2 log((1 − 1
2 )|A|) = |A|
2 log(|A|), which is exactly the lower
bound that we intended to prove for ∑n
k=1 |A{k}|. This proves the ﬁnal case of the induction step,
concluding the proof of Proposition 3.2.

In general, induction can be useful for proving properties of union-closed families, especially when
coupled with additional assumptions, because union-closed families are rich in subfamilies that are also
union-closed. The nested structure of union-closed families motivates the following strengthening of
Conjecture 1.1.

Conjecture 3.3. For any union-closed family A, if y ∈ [n] with |A{y}| = maxx∈[n]{|A{x}|} and there
exists z ∈ [n] such that A = A{y} ∪ A{z}, then |A{y}| ≥ 2|A{y}|.

Before proving that Conjecture 3.3 implies Conjecture 1.1, we present a framework for considering
union-closed families. For any union-closed family A, we deﬁne the following:

4

R
(i) : i ∈ Z≥0,

P = {P (i) | i ∈ [min({i | R
(i) = ∅})]}, and

P : [min({i | R
(i) = ∅})] → [n],

such that R
(0) = A, and:

For i ∈ Z>0:














If R
(i−1) ̸= ∅, then:








P (i) = min({
y ∣
∣
∣ |(R
(i−1)){y}| = maxx∈⋃

R∈R(i−1) R{|(R
(i−1)){x}|}
}).

If (R
(i−1)){P (i)} ̸= {∅}, then P (i) = (R
(i−1)){P (i)} and R
(i) = (R
(i−1)){P (i)}.

If (R
(i−1)){P (i)} = {∅}, then P (i) = (R
(i−1)){P (i)} ∪ {∅} and R
(i) = ∅.

If R
(i−1) = ∅, then R
(i) = ∅.

We note that P is a partition of A with |P| = min({i | R
(i) = ∅}).

Theorem 3.4. If S is a nonempty subset of [|P|], then ⋃
k∈S P (k) is union-closed.

Proof. ⋃
k∈S P (k) is a subfamily of A, so all of its member sets are ﬁnite and distinct. Also, ⋃
k∈S P (k)

has at least one nonempty member set. To prove the union-closed property for ⋃
k∈S P (k), we observe
that (X, Y ∈ ⋃
k∈S P (k)) =⇒ (X ∈ P (i) ∧ Y ∈ P (l)), where 1 ≤ i ≤ l ≤ |P| without loss of generality.
X ∪ Y ∈ A because X, Y ∈ A and A is union-closed. If X = ∅, then X ∪ Y = Y ∈ P (l) ⊆ ⋃
k∈S P (k).
Else, P (i) is in X, implying that P (i) is also in X ∪ Y . If i = 1, then (X ∪ Y ∈ A) ∧ (P (i) ∈ X ∪ Y ) =⇒
X ∪ Y ∈ P (i) ⊆ ⋃
k∈S P (k). If i > 1, then ∀j ∈ [i − 1] ((P (j) ̸∈ X ∧ P (j) ̸∈ Y ) =⇒ P (j) ̸∈ X ∪ Y ), and it
follows that ((X ∪ Y ∈ A) ∧ (P (i) ∈ X ∪ Y ) ∧ (∀j ∈ [i − 1] P (j) ̸∈ X ∪ Y )) =⇒ X ∪ Y ∈ P (i) ⊆ ⋃
k∈S P (k).
Therefore, ⋃
k∈S P (k) satisﬁes the union-closed property, and the proof of Theorem 3.4 is complete.

Corollary 3.5. Conjecture 1.1 implies that |P (j)| ≥ ∑
i∈S |P (i)| for any nonempty subset S of [|P|] \ [k],
whenever 1 ≤ j ≤ k < |P|.

Theorem 3.6. Conjecture 3.3 =⇒ Conjecture 1.1.

Proof. We consider a union-closed family A with |P| > 1, as Conjecture 1.1 holds trivially when |P| = 1.
Assume that ∅ ̸∈ A. Theorem 3.6 will be proved when we show that Conjecture 1.1 holds for both A and
A ∪ {∅}. For all i in [|P| − 1], P (i) ∪ P (i+1) is a union-closed family that, according to the framework under
consideration, has its own partition ˆP = { ˆP (1), ˆP (2)} and function ˆP : {1, 2} → { ˆP (1), ˆP (2)} such that
ˆP (1) = P (i), ˆP (2) = P (i+1), ˆP (1) = P (i), and ˆP (2) = P (i+1). Conjecture 3.3 then applies to P (i) ∪P (i+1)

with y and z from Conjecture 3.3 respectively equal to ˆP (1) and ˆP (2). Thus, |P (i)| ≥ 2|P (i+1)| for all
i ∈ [|P| − 1], implying the following upper bound µ(P) of ∑|P|
i=2 |P (i)|:

µ(P) =
 |P|−1 terms
︷ ︸︸ ︷⌊ 1
2 |P (1)|
⌋ + ⌊ 1
2
 ⌊ 1
2 |P (1)|
⌋⌋ + ⌊ 1
2
 ⌊ 1
2
 ⌊ 1
2 |P (1)|
⌋⌋⌋ + · · · + ⌊ 1
2
 ⌊ 1
2
 ⌊ 1
2 · · · ⌊ 1
2 |P (1)|
⌋ · · ·
⌋⌋⌋ .

|P|∑

i=2 |P (i)| ≤ µ(P) ≤ |P (1)|
 |P|−1∑

i=1
 1
2i < |P (1)|
 ∞∑

i=1
 1
2i = |P (1)|.

Therefore, |P (1)| > ∑|P|
i=2 |P (i)|, and we have that P (1) ∈ [n] with |A{P (1)}| = |P (1)| > ∑|P|
i=2 |P (i)| =
|A{P (1)}|. Conjecture 1.1 then holds for A, as |A{P (1)}| > |A|
2 .

Now consider A ∪ {∅}. We have that (A ∪ {∅}){P (1)} = A{P (1)} and (A ∪ {∅}){P (1)} = A{P (1)} ∪ {∅}.
It follows that |(A ∪ {∅}){P (1)}| > |(A ∪ {∅}){P (1)}| − 1, and so |(A ∪ {∅}){P (1)}| ≥ |(A ∪ {∅}){P (1)}|

because |(A ∪ {∅}){P (1)}| and |(A ∪ {∅}){P (1)}| are both integers. Thus, |(A ∪ {∅}){P (1)}| ≥ |A∪{∅}|
2 , and
Conjecture 1.1 also holds for A ∪ {∅}. This completes the proof of Theorem 3.6.

5

For any union-closed family A with |P| > 1, we have that |A{P (1)}{P (2)}| ≥ |A{P (2)}{P (1)}|, where
A{P (1)}{P (2)} = A{P (1)} ∩ A{P (2)} and A{P (2)}{P (1)} = A{P (2)} ∩ A{P (1)}. We observe that Conjecture
1.1 holds if |P| = 2. A proof technique for Conjecture 1.1 would show, for any union-closed family A with
|P| > 2, that |A{P (1),P (2)}| ≥ |A{P (1),P (2)}| (see Theorem 2.4). On the other hand, a proof technique for
Conjecture 3.3 would show, for any union-closed family A with ∅ ̸∈ A and |P| = 2, that, without loss of
generality, |A{P (1),P (2)}| ≥ |A{P (2)}{P (1)}|. Figures 3.1 and 3.2 illustrate the respective techniques.

Figure 3.1: A technique for Conjecture 1.1 attempts to ﬁnd, for any union-closed family A with
|P| > 2, a unique y ∈ A{P (1),P (2)} for every x ∈ A{P (1),P (2)}.
 A{P (1),P (2)}A{P (1)}{P (2)}

A{P (2)}{P (1)}

A{P (1),P (2)}

P (1)

P (2)

⋃

3≤i≤|P| P (i)

Figure 3.2: A technique for Conjecture 3.3 attempts to ﬁnd, for any union-closed family A with ∅ ̸∈ A
and |P| = 2, a unique y ∈ A{P (1),P (2)} for every x ∈ A{P (2)}{P (1)}.
 A{P (1),P (2)}A{P (1)}{P (2)}

A{P (2)}{P (1)}

P (1)

P (|P|) = P (2)

In both of these techniques, we determine member sets of A that necessarily belong to A{P (1),P (2)}.
To do so, we can utilize the facts that x1 ∈ A{P (1)}{P (2)} ∧ x2 ∈ A{P (2)}{P (1)} =⇒ x1 ∪x2 ∈ A{P (1),P (2)}
and y1 ∈ A{P (1),P (2)} ∧ y2 ∈ A \ A{P (1),P (2)} =⇒ y1 ∪ y2 ∈ A{P (1),P (2)}.

4. A second strengthening of Conjecture 1.1

We now consider a strengthening of Conjecture 1.1 that proposes an alternate deﬁnition of a ﬁnite power
set.

A family of sets F is called separating if (x, y ∈ ⋃
F ∈F F ) ∧ (F{x} = F{y}) =⇒ x = y. In other
words, F is separating if no two distinct elements of its base set are in exactly the same member sets.

Conjecture 4.1 (Poonen [6]). If A is a separating union-closed family and is not a power set, then
maxx∈[n]{|A{x}|} > |A|
2 .

Conjecture 4.1 implies Conjecture 1.1 because any ﬁnite power set with at least one nonempty member
set satisﬁes Conjecture 1.1, and Conjecture 4.1 states that no other separating union-closed family A has
maxx∈[n]{|A{x}|} less than |A|
2 . This need not be explicitly stated, however, as the following conjecture
also implies Conjecture 1.1.

Conjecture 4.2. A family of sets A is a ﬁnite power set if and only if either A = {∅} or A is union-closed
and separating with maxx∈[n]{|A{x}|} = |A|
2 .
 6

For families X and Y, let X ⊔ Y = {X ∪ Y | X ∈ X ∧ Y ∈ Y}. The following lemma will be used in
showing that Conjecture 4.2 implies Conjecture 1.1.

Lemma 4.3. If X and Y are union-closed families, then X ⊔ Y is also a union-closed family.

Proof. If X and Y are union-closed families, then X ⊔ Y has member sets that are all ﬁnite and distinct,
and has at least one nonempty member set. To verify the union-closed property for X ⊔ Y, we observe
that for all A and B in X ⊔ Y, there are X, X ′ in X and Y , Y ′ in Y such that A = X ∪Y and B = X ′ ∪Y ′.
We must show that A ∪ B = (X ∪ Y ) ∪ (X ′ ∪ Y ′) is in X ⊔ Y. Because ∪ is commutative and associative,
(X ∪ Y ) ∪ (X ′ ∪ Y ′) = (X ∪ X ′) ∪ (Y ∪ Y ′). X ∪ X ′ ∈ X and Y ∪ Y ′ ∈ Y because X and Y are union-closed.
Then (X ∪ X ′) ∪ (Y ∪ Y ′) is by deﬁnition in X ⊔ Y. Thus, X ⊔ Y satisﬁes the union-closed property, and
the proof of Lemma 4.3 is complete.

Theorem 4.4. Conjecture 4.2 =⇒ Conjecture 1.1.

Proof. We ﬁrst note that if a counterexample to Conjecture 1.1 exists, then a separating counterexample
to Conjecture 1.1 exists; if a counterexample is not separating, then we can make a separating family on
a smaller base set by representing as a single element every grouping of two or more elements (from the
original base set) that are contained within exactly the same member sets of the original family. This
separating family is also a counterexample as it has the same number of member sets and the same set
of element frequencies as of the original family.

Now assume that Conjecture 1.1 is false, and ˜A is a separating counterexample on a base set [˜n]. We form
a union-closed family ˜A
′ = ˜A ⊔{{z}, ∅} such that z ̸∈ [˜n]. By Lemma 4.3, ˜A
′ is union-closed because ˜A
and {{z}, ∅} are both union-closed.

Next, we prove that maxx∈⋃
A∈ ˜A′ A{| ˜A
′
{x}|} = | ˜A
′|
2 .

Proof. ( ˜A
′ = ˜A ∪ {y ∪ {z} | y ∈ ˜A}) ∧ (z ̸∈ [˜n]) =⇒ | ˜A
′| = 2| ˜A|. Also, ∀x ∈ [˜n] (( ˜A
′
{x} =

˜A{x} ∪ {y ∪ {z} | y ∈ ˜A{x}}) ∧ (z ̸∈ [˜n]) =⇒ | ˜A
′
{x}| = 2| ˜A{x}|). Therefore, ∀x ∈ [˜n] | ˜A
′
{x}|

| ˜A′| = | ˜A{x}|

| ˜A| < 1
2 ,

making all elements, except for z, in ⋃
A∈ ˜A′ A = [˜n]∪{z} have frequency in ˜A
′ less than | ˜A
′|
2 . | ˜A
′
{z}| = | ˜A
′|
2 ,
as | ˜A
′
{z}| + | ˜A
′
{z}| = | ˜A
′| and ( ˜A
′ = ˜A ∪ {y ∪ {z} | y ∈ ˜A}) ∧ (z ̸∈ [˜n]) =⇒ | ˜A
′
{z}| = | ˜A
′
{z}|. Thus, z

has the highest frequency in ˜A
′ among elements of ⋃
A∈ ˜A′ A, and maxx∈⋃
A∈ ˜A′ A{| ˜A
′
{x}|} = | ˜A
′|
2 .

We also have that ˜A
′ is separating. To prove this, we observe that {x, y} ∈ (
[˜n]
2 ) =⇒ ˜A{x} ̸= ˜A{y}, as
˜A itself is separating. It follows that {x, y} ∈ (
[˜n]
2 ) =⇒ ˜A
′
{x} ̸= ˜A
′
{y}. Now, ∀x ∈ [˜n] (∀A ∈ ˜A{x} (A ∈
˜A
′ ∧ z ̸∈ A)) =⇒ ˜A
′
{x} ̸= ˜A
′
{z}. Thus, no two distinct elements of the base set of ˜A
′ are in exactly the
same member sets of ˜A
′.

˜A
′ is not a ﬁnite power set, as all elements of [˜n] have nonzero frequency in ˜A
′ less than | ˜A
′|
2 .

Hence, ˜A
′ is a counterexample to Conjecture 4.2, as ˜A
′ ̸= {∅}, ˜A
′ is union-closed and separating with
maxx∈⋃
A∈ ˜A′ A{| ˜A
′
{x}|} = | ˜A′|
2 , and ˜A
′ is not a ﬁnite power set. We have that ¬ (Conjecture 1.1) =⇒ ¬
(Conjecture 4.2). Therefore, Conjecture 4.2 =⇒ Conjecture 1.1.

A motivation for decoupling Conjecture 4.2 from Conjecture 4.1 is to emphasize possible equivalence
with Conjecture 1.1. Conjecture 4.2 implies Conjecture 1.1, but it remains to be shown whether
Conjecture 1.1 also implies Conjecture 4.2.

References

[1] H. Bruhn, P. Charbit, O. Schaudt, and J.A. Telle, The graph formulation of the union-closed sets
conjecture, European J. Combin. 43 (2015), 210-219.

[2] H. Bruhn and O. Schaudt, The journey of the union-closed sets conjecture, Graphs Combin. 31
(2015), 2043-2074.

[3] J. Gilmer, A constant lower bound for the union-closed sets conjecture, preprint (2022),
arXiv:2211.09055.

[4] I. Karpas, Two results on union-closed families, preprint (2017), arXiv:1708.01434.

7

[5] G. Lo Faro, Union-closed sets conjecture: Improved bounds, J. Combin. Math. Combin. Comput. 16
(1994), 97-102.

[6] B. Poonen, Union-closed families, J. Combin. Theory Ser. A 59 (1992), 253-268.

[7] D. Reimer, An average set size theorem, Combin. Probab. Comput. 12 (2003), 89-93.

[8] J. Reinhold, Frankl’s conjecture is true for lower semimodular lattices, Graphs Combin. 16 (2000),
115-116.

[9] I. Roberts and J. Simpson, A note on the union-closed sets conjecture, Australas. J. Combin. 47
(2010), 265-267.

[10] W. Sawin, An improved lower bound for the union-closed set conjecture, preprint (2023),
arXiv:2211.11504.

[11] B. Vuˇckovi´c and M. ˇZivkovi´c, The 12-element case of Frankl’s conjecture, IPSI BgD Transactions
on Internet Research 13(1) (2017), 65-71.
 8
