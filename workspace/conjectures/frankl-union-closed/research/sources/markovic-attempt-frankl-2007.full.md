<!-- source: https://people.dmi.uns.ac.rs/~markovicp/papers/2007-Frankl10.pdf | converted from PDF -->

PUBLICATIONS DE L’INSTITUT MATH ·EMATIQUE
Nouvelle s·erie, tome 81(95) (2007), 29–43 DOI 102298/PIM0795029M

AN ATTEMPT AT FRANKL’S CONJECTURE

Petar Markovi·c

Abstract. In 1979 Frankl conjectured that in a ﬁnite union-closed family F
of ﬁnite sets, F ̸= {∅} there has to be an element that belongs to at least half
of thesetsin F .We prove this when | ) F| ⩽ 10.

1. Introduction

Frankl’s conjecture (sometimes also called the union-closed sets conjecture)
is one of the most famous problems in combinatorics. There has been extensive
research of this problem and the amount of papers published is quite large. One
of the most popular lines of attack is to prove the conjecture for the ﬁrst ﬁnitely
many cases. There are two ways in which this was done: proving the conjecture
for |F| ⩽ n and proving the conjecture for | ) F| ⩽ m. The second approach has
managed to achieve m ⩽ 9 (in [13]). In this paper we push it one step further.
Another approach is to ﬁnd small union-closed G families which imply that
any union-closed family F containing G satisﬁes the Frankl’s conjecture, with the
element appearing in one-half of the sets being one of the elements which belong
to ) G. In the present paper we include several such results, which are not new, as
lemmas when we need them. Credit for these lemmas will be assigned where it is
due, but we will reprove them here in order to keep the paper self-contained and to
familiarize the reader with the basic technique which will be used for the most of
the paper. Along these lines, Vaughan (with coauthors) has recently proved several
nice results in [24], [25], [4] and [26] and these results were further improved by
Morris in [13].
It is important to mention that the main technique used here (assigning weights
to elements and sets) is mostly a rephrasing of the technique initially discovered by
Poonen in [16]. However, the new idea is to (implicitly) use several weights at the
same time. This allows us to push the bounds much further than was previously
possible. This method will most probably not prove the whole conjecture. However,
it does deal with the small cases eﬃciently, and is amenable to an algorithmic

2000 Mathematics Subject Classiﬁcation: Primary 05D05; Secondary 05A05, 04A20.
Key words and phrases: Frankl’s conjecture, union-closed sets conjecture.
Supported by Ministry of Science and Environment of Serbia, grant 144011G..

29

30 MARKOVI ·C

approach. We feel that in the hands of a good programmer it could probably push
the bounds of the Frankl’s conjecture even further.
The results in this paper were ﬁrst proved as a part of the author’s qualifying
paper at the Vanderbilt University, in 2000. Because of the requirements for such a
paper, the bibliography was quite extensive. Rather than reducing the bibliography,
since there is quite a lot of activity in the ﬁeld recently, we updated it. We feel that
a large bibliography could be an asset to a researcher starting to work on Frankl’s
Conjecture.
 2. Initial Results

Throughout this paper F will denote a ﬁnite family of ﬁnite sets closed under
unions and X will denote the union of F. We will call F Frankl’s if X = ) F
contains an element which is in at least one half of the sets from F.

Definition 2.1. We call any function w : X →{x ∈ R | x ⩾ 0}, such that
w(a) > 0 for some a ∈ X,a weight function. The weight w(S), for S ⊆ X is equal
to ∑

x∈S w(x). The number 0.5w(X) will be called the target weight and denoted
by t(w).

Lemma 2.1. F is Frankl’s if and only if there is a weight function w assigned
to elements of X = ) F such that ∑S∈F w(S) ⩾ t(w)|F|.

Proof. (⇒)Let a be an element of at least half of the sets in F.Take the
weight function w such that w(a)=1 and w(x)=0 for x ̸= a. Then t(w)=0.5,
and the inequality is obviously satisﬁed.
(⇐) Assume that F is not Frankl’s. Let na(F) be the number of occurrences
of the element a in sets from F. We take an arbitrary weight function w. Then
∑

S∈F w(S)= ∑

S∈F
 ∑

a∈S w(a)= ∑

a∈X w(a)na(F) < ∑

a∈X w(a) |F|
2 = t(w)|F|. □

The following lemma is one of the earliest results on union-closed families.

Lemma 2.2. If F contains a one-element set, or a two-element set, then it is
Frankl’s.

Proof. In case of a one-element set, let this set be {a}. Consider the sets in
F that do not contain a. For each such set K, the set K ∪{a} must also be a
member of F. Therefore we have an injection from sets in F that do not contain a
into the sets in F that do contain a,so a must be a member of at least half of the
sets in F.
Now, let F contain a two-element set {a, b}. Let us assign weight function w
to members of X such that w(a)= w(b)=1 and w(x) = 0 for all other x ∈ X.
The target weight t(w) = 1. If we consider the full powerset lattice of subsets of
X, we can partition this lattice into intervals [K, K ∪{a, b}], where K are subsets
of X which do not contain a or b. If we just look at the sets which are in one such
interval, we see that:
• If K ∈F (w(K) = 0), then K ∪{a, b}∈F (w(K ∪{a, b}) = 2) and

AN ATTEMPTATFRANKL’SCONJECTURE 31

• w(K ∪{a})= w(K ∪{b})=1.

Therefore, for sets from F which are in this interval, we have that the average
weight is at least 1. As the interval was picked arbitrarily, the same can be said for
all of F. This, by Lemma 2.1 is suﬃcient to show that F is Frankl’s. □

Definition 2.2. For S, K ⊆ X, S ∩ K = ∅ we call any interval in the Boolean
lattice P(X) of the form [K, K ∪ S]an S-hypercube. We can partition a hypercube
into levels, where set is on level k if and only if k is the cardinality of its intersection
with S.
Let F a union-closed family of sets and w a weight function. The deﬁcit of a
set L ⊆ X with w(L) <t(w)is d(L)= t(w) − w(L). The surplus of a set L ⊆ X
with w(L) >t(w)is s(L)= w(L) − t(w)Let C be an S-hypercube. The deﬁcit of
C and is the surplus of C are deﬁned to be

d(C)= ∑

L∈C∩F
w(L)<t(w)
(t(w) − w(L)) and s(C)= ∑

L∈C∩F
w(L)>t(w)
(w(L) − t(w)).

respectively.

It is an obvious consequence of Lemma 2.1 that if for some weight function
w the sum of surpluses of the sets in F which have weights greater than t(w)is
greater than or equal to the sum of deﬁcits of the sets in F which have weights less
than t(w), then F is Frankl’s. Also, if for every hypercube C, s(C) ⩾ d(C), then F
is Frankl’s.
The following proposition was proved in [16].

Proposition 2.1. Assume that F contains three diﬀerent 3-element sets which
are all subsets of the same four-element set. Then F is Frankl’s.

Proof. Assume that {a, b, c}, {a, b, d} and {a, c, d} are the three sets from the
statement. Then also {a, b, c, d}∈F. We are considering the weight w(x)=1
for x ∈{a, b, c, d},and w(x) = 0 else. Take an arbitrary {a, b, c, d}-hypercube,
C =[K, K ∪{a, b, c, d}].
If any set in C is in F, then the top set of C is in F, also. If K ∈F, then
s(C) ⩾ 5, as three of the level 3 sets are in F. So, either s(C) ⩾ d(C), or all four
level 1 sets are also in F. But then all four level 3 sets are in F, too, so again we
have that s(C) ⩾ d(C).
If K/∈F, then either d(C) = 0, or a level 1 set is in F. If latter is the case,
then s(C) ⩾ 4, as the top set and at least 2 level 3 sets are in F (the second as each
of a, b, c, d is in at least two of the three sets from the statement of the lemma).
Again, we get s(C) ⩾ d(C). □

Notice that in all the S-hypercubes we considered in the previous proof we
had that if they had nonempty intersection with F, then their top is in F. This
is a consequence of our choice of S,aswehad S ∈F. We will continue with this
practice, so we will not repeat later that if an S-hypercube contains a set from F,
then the top of this hypercube must also be in F.

32 MARKOVI ·C

The results in [26] give a sharper bound for the number of three-element subsets
of a six-element set which can be in F, but the following will be suﬃcient for our
purpose:

Corollary 2.1. If F contains 11 three-element sets which are all subsets of
the same six-element set, then F is Frankl’s.

Proof. We will prove that in such case F contains three three-element sets in
the same four-element set, and then we are done by Proposition 2.1.
In a six-element set there are (6
3) = 20 three-element subsets. They can be
partitioned into 10 pairs of complements. By the pigeon-hole principle, there must
be two three element sets among the 11 in F which are complements of each other.
Let these two sets be A and B. Each of the other 9 three-element sets intersects
one of A and B in a two-element set and the other in a one-element set. Without
loss of generality we may assume that at least 5 of the three-element sets from F
have a two-element intersection with A and one-element intersection with B.
Now we consider these 5 three-element sets. There must be two among them,
C and D which have C ∩ B = D ∩ B = {b} (pigeon-hole principle again, as there
are 5 sets, and B has only 3 elements). We see that A, C, D ∈F, and all three
are contained in A ∪{b}. □

The next lemma was stated, without proof in [25].

Proposition 2.2. Suppose that F contains 3 three-element sets which all con-
tain the same two elements. Then F is Frankl’s.

Proof. Let us denote these three sets by {a, b, c}, {a, b, d} and {a, b, e}. Again
we assume that F is not Frankl’s. We pick the weight function w such that w(a)=
w(b)=3, w(c)= w(d)= w(e)=2 and w(x) = 0 for all other x ∈ X. Then
t(w) = 6. We consider an {a, b, c, d, e}-hypercube C with bottom set K. Let us ﬁrst
assume K ∈F. Then we also have the top set of the hypercube in F, whose surplus
equals the deﬁcit of the bottom set (and these two cancel out, so we won’t count
them in deﬁcits/surpluses). Three level 3 sets each with surplus 2 are guaranteed
to be in F, as well as the three level 4 sets (unions of pairs of the former), each
with surplus 4. So, we are guaranteed a surplus of at least 18 from level 3 and 4
sets. We have diﬀerent cases depending on the number of level 1 sets which are
in F:
(1) If there are less than two level 1 sets in F, then the combined deﬁcit from
levels 1 and 2 can be at most 16 (upto 12 from level 2 and upto 4 from level 1).
Thus, s(C) ⩾ d(C).
(2) There are two level 1 sets in F. Then the combined deﬁcit from level 1 is
at most 8, so the combined deﬁcit from level 2 needs to be at least 11. Thus, all
three level 2 sets with weight 4 are in F(and so is K ∪{c, d, e}), and at least ﬁve
of the six weight 5 sets are in F. By taking union of a weight 5 set with the set
K ∪{c, d, e}, we get a weight 9 set (surplus 3) in F. Now, the surpluses from levels
3 and 4 are at least 21, which is unachieveable by deﬁcits from levels 1 and 2.
(3) There are three level 1 sets in F. If both of weight 3 sets are among them,
then weight 4 sets cancel out with weight 7 sets, as each weight 4 set in F implies

AN ATTEMPTATFRANKL’SCONJECTURE 33

two of the weight 7 sets in F. The level 1 sets and weight 5 sets have combined
deﬁcit of at most 16, which is less than 18 (surplus from weight 8 and 10 sets).
If one of the level 1 sets in F has weight 3 and the other two weight 2, then
the total deﬁcit from level 1 sets is 11, while the known surpluses from weight 10
and weight 8 sets add up to 18. Therefore, the level 2 sets have to produce deﬁcit
of 8. Because of the weight 3 set which is in F, each weight 4 set in F implies a
weight 7 set in F. Therefore, level 2 contains at least 8 sets which are in F.So,
two of the weight 4 sets must be in F, and by union of these two and the weight
3 set we get a weight 9 set in F. Now, the deﬁcit produced by level 2 sets should
be 11, and, as weight 4 sets are contributing just 1 to the deﬁcit (aech adds 1 to
surplus and 2 to the deﬁcit), this is impossible.
If the level 1 sets in F are K ∪{c}, K ∪{d} and K ∪{e}, then all three weight 4
sets are also in F. The surpluses and deﬁcits of the known sets cancel out and the
only remaining sets in C which may produce deﬁcit are of weight 5. However, if any
those three that contain a is in F, that implies that the weight 9 set K ∪{a, c, d, e}
is in F, while the three containing b similarly union to K ∪{b, c, d, e} with {c, d, e}.
So s(C) ⩾ d(C) in this case, as well.

(4) There are four level 1 sets in F. If both K ∪{a} and K ∪{b} are in F,
then without loss of generality we may assume that K ∪{e} is not in F.Each
of the weight 4 sets in F implies two of the weight 7 sets in F(as before), so we
may disregard these two groups. The deﬁcits of the level 1 sets add up to 14, while
the surpluses of weight 8 and weight 10 sets add up to 18. So, at least ﬁve of the
weight 5 sets should be in F. But that would imply one of them contains e,and
that unions with weight 2 sets to a weight 9 set. Then the deﬁcits of weight 5 sets
should now be at least 8, which is impossible.
If the missing level 1 set is K ∪{a} or K ∪{b} (say, the latter), then all three
weight 4 sets, all three weight 7 sets which contain a and the set K ∪{a, c, d, e} are
forced to be in F. The deﬁcits of level 1 and weight 4 sets add up to 21, while the
surpluses of level 3 and 4 sets which we know are in F add up to 24. So, at least
4 weight 5 sets should be in F. But one of them then contains b, which implies
K ∪{b, c, d, e}∈F. Now the surpluses add up to 27, which can not be surpassed
by the deﬁcits.

(5) There are ﬁve level 1 sets in F. Then C⊆ F,and s(C)= d(C)

Now we investigate the case when K/∈F. The number of weight 2 sets in F is
less then or equal to the number of weight 10 sets in F, so these two groups cancel
each other out. Our cases are:

(5.1) Both K ∪{a},K ∪{b}∈F. Then all three weight 8 sets are in F,and
each weight 4 set in F implies two of the weight 7 sets in F, so we may disregard
these two groups. The surpluses of weight 8 sets, plus the level 5 set add up to 12,
while the deﬁcits of the weight 3 and weight 5 sets can be at most 12.

(5.2) Both K ∪{a},K ∪{b} /∈F. Each weight 5 set in F implies that one of
the weight 8 sets in F, and if there are at least three weight 5 sets in F, then all
three weight 8 sets are in F, so the surplus of weight 8 sets is greater or equal to

34 MARKOVI ·C

the deﬁcit of weight 5 sets. The deﬁcit of the weight 4 sets can be at most 6, which
is covered by the surplus of the top set. So, in this case also, s(C) ⩾ d(C).
(5.3) One of the sets K ∪{a}, K ∪{b} is in F (say, K ∪{a}), and the other is
not. Then all three weight 8 sets are in F, and the combined surplus of them and
the top set is 12. The deﬁcit of K ∪{a} is 3, and each of the weight 4 sets in F,
when unioned with K ∪{a} produces a weight 7 set in F. So, the total deﬁcit of
the weight 4 sets may be considered to be at most 3, and the deﬁcit of the weight
5 sets is at most 6. Thus, these deﬁcits are covered by the surpluses of the weight
8 sets and the top set.
This shows that in all possible cases s(C) ⩾ d(C), so F is Frankl’s. □

To proceed, we deﬁne a relation ’≼’ on elements of X. For now we assume that
F is a counterexample to the conjecture with |X| minimal.

Definition 2.3 (McKenzie). For a, b ∈ X we say that a ≼ b iﬀ for all K ∈F,
if b ∈ K then a ∈ K.

Fact 2.1. The relation ‘≼’ is a partial order.

Proof. It is obvious that this is a pre-order (a reﬂexive, transitive relation).
If it is not a partial order, then there are elements a, b in X such that a ≼ b and
b ≼ a, i.e., they either both belong to a set in F, or neither of them does. But
then, by identifying these two elements as one new element, we get that the new
family F ′ is also a counterexample, and that | ) F ′| < |X|. This contradicts the
minimality of |X|. □

Lemma 2.3 (McKenzie). For every element a ∈ X which is maximal in the
partial order ≼ deﬁned above, X −{a} belongs to F.

Proof. We know that (∀b ∈ X −{a})(a ̸≼ b). So for every b ∈ X −{a} there
is a set Kb ∈F so that b ∈ Kb and a ̸∈ Kb. Then X −{a} = )

b∈X−{a} Kb ∈F □

McKenzie has also noticed that there must be at least two maximal elements
in this partial order in a minimal counterexample, but we do not need that result
for the purposes of this paper. We do need the following simple corollary:

Corollary 2.2. If there exists a counterexample F to the Frankl’s conjecture
with | ) F| = m and let m
′ ⩾ m. Then there exists a counterexample G to the
Frankl’s conjecture such that | ) G| = m′ and G contains a set of the size m′ − 1.

Proof. If m
′ is the minimal size of the largest set in a counterexample, then
the Lemma 2.3 is providing us with the desired set. So, assume that there is a
counterexample H with | ) H| = m′′ <m
′ and that m′′ is minimal. We take any
element of the set in H with size m
′′ −1, guaranteed by Lemma 2.3. We replace this
element by several elements (as in the proof of Lemma 2.4) to get a counterexample
to Frankl’s conjecture with | ) G| = m′ and such that G contains a m
′ − 1-element
set. □

Lemma 2.4. If every family F with |X| = k is Frankl’s, then every family F ′

with top set X ′, |X ′| < |X| is Frankl’s.

AN ATTEMPTATFRANKL’SCONJECTURE 35

Proof. Assume not. Then there is a family F ′ with l-element top set, l< k
which is not Frankl’s. Consider the family F ′′, which is constructed from F ′ by
taking an element a of X ′, and replacing each occurrence of this element in a
set of F ′ with k − l + 1 new elements, a0,a1,...,ak−l. The family F ′′ is union
closed, because F ′ was, and every element is less than half of the sets (the old ones
because they were such in F ′, and the ais because a was in less than half of the
sets of F ′). □

3. Results for |X| =10

Lemma 3.1. If |X| =10 and F contains two three-element sets with a two-
element intersection, then F is Frankl’s.

Proof. Similarly as in the proof of Lemma 2.4, we suppose F is not Frankl’s,
so we may assume that F contains no one- or two-element sets. Let {a, b, c} and
{a, b, d} be the two sets in F. We consider the weight function w, with w(a)=
w(b)=8, w(c)= w(d)=6 and w(x)=1 for x ∈ X −{a, b, c, d}.We have
t(w) = 17. Let C be an {a, b, c, d}-hypercube with bottom set K. We consider the
cases:
(1) |K| = 1. In such hypercubes only levels 2, 3 and 4 may contain sets from
F. The surplus of the top set K ∪{a, b, c, d} is 12, and there are only ﬁve sets with
weights less than t(w), all of them on level 2. K ∪{c, d} has deﬁcit 4, while the
other four have deﬁcit 2. So, d(C) ⩽ 12, and d(C) ⩽ s(C).
(2) |K| = 2. Here the sum of deﬁcits of the sets on level 2 is 7. If we consider
the number of level 1 sets, we have subcases:
(1) There are no level 1 sets in F. Then the surplus of the top set is 13, while
the sum of deﬁcits can be at most 7 (ﬁve level 2 sets).
(2) There is one level 1 set in F. That set implies that at least one of the sets
K ∪{a, b, c} and K ∪{a, b, d} is in F(each has surplus 7). Thus, s(C) ⩾ 20,
and as the deﬁcit of a level 1 set is at most 9, d(C) ⩽ 16.
(3) There are two level 1 sets in F. That implies that both of the sets K ∪
{a, b, c} and K ∪{a, b, d} are in F,so s(C) ⩾ 27. The combined deﬁcit of
the level 1 sets is at most 18, and that means that d(C) ⩽ 25.
(4) There at least three level 1 sets in F. Then they form three 3-element
sets with common two-element intersection. Then F is Frankl’s by the
Proposition 2.2.

(3) |K| =3. If K/∈F, the surplus of the top set is 14. The sets producing
deﬁcit are on the level 1 (two with weight 9 and two with weight 11) and the set
K ∪{c, d}, with weight 15. Thus, at least two of the level 1 sets must be in F.
That implies that K ∪{a, b, c} and K ∪{a, b, d} are both in F. The surplusisnow
at least 30, and that is equal to the combined deﬁcits of all the sets in C.
If K ∈F we would like to prove that, although such hypercubes may have
deﬁcit greater than the surplus, d(C) ⩽ s(C) + 2. We see that the top set and the
bottom one cancel each other out, and that K ∪{a, b, c} and K ∪{a, b, d} are both
in F. Their combined surplus is 16, so we must have at least three level 1 sets in

36 MARKOVI ·C

F, or the two which are in F must be K ∪{c} and K ∪{d}. In the second case,
the only remaining set producing deﬁcit is K ∪{c, d}, and now d(C)= s(C)+2.
If there are all four level 1 sets in F, then C⊆ F,and s(C)= d(C). If the three
level 1 sets which are in F contain both K ∪{c} and K ∪{d}, then the union of
the three of them gives us another level 3 set in F, with weight 23, and surplus 6.
Thus, level 3 sets have surplus at least equal to the deﬁcit of the level 1 sets, and
the set K ∪{c, d} produces extra deﬁcit of 2, again. The last case is when the three
level 1 sets in F contain both of the sets K ∪{a} and K ∪{b}. Then the combined
deﬁcit of the level 1 sets is 20, and we have that K ∪{a, b}∈F, with surplus 2.
Together with the surplus of 16 coming from the two level 3 sets, this gives us a
combined surplus of 18 and the third case when deﬁcit is greater by 2 than the
surplus. If, however, K ∪{c, d}∈F, this adds 2 to deﬁcit, but the sets K ∪{a, c, d}
and K ∪{b, c, d} are forced to be in Fwhich increases the surplus by 12.

(4) |K| =4 or |K| = 5. In these cases we just imitate the proof for |K| =3, as
the numbers work even better, and just check the three cases when K ∈F and d(C)
was s(C) + 2 in the case |K| = 3. All three corresponding cases have d(C) <s(C)
now, so in general, d(C) ⩽ s(C).

(5) The top and bottom hypercubes we deal with together. The only set with
a deﬁcit in the bottom hypercube is ∅, whose deﬁcit is equal to the surplus of X.
We also have three sets with surplus in the bottom hypercube, namely {a, b, c},
{a, b, d} and {a, b, c, d}. Their combined surplus is 21. No other sets from bottom
hypercube may be in F,else F is Frankl’s by Proposition 2.1.
We would like to prove that the remaining sets in the top hypercube have
surplus greater than or equal to deﬁcit. The sets in the top hypercube with deﬁcit
are the bottom one (deﬁcit 11) and the level 1 sets (two with deﬁcit 5 and two with
deﬁcit 3).
If the bottom set is in F, then so are the two level 3 sets with surplus 11 each.
Thus, we would have to have at least 3 of the level 1 sets in F. They imply that
three level 2 sets are in F, and the surpluses of them are at least 7 (X −{a, b} with
surplus 1 and the other two with surpluses at least 3 each). So all the level 1 sets
are in F, which implies that all the top hypercube is in F, and surpluses of the
level 2 and 3 sets add up to 58, which is more than the deﬁcits of the level 0 and 1
sets (27).
If the bottom set is not in F,any level 1 set in F implies that at least one level
3 set with surplus 11 is in F, too. If there are at least two level 1 sets then both
of those sets with surplus 11 are in F, and their combined surplus is greater then
the combined deﬁcit of all the level 1 sets.

We have proved that the top and bottom hypercube together have surplus of
at least 20 greater than the deﬁcit. Thus, at least 11 of the ’bad’ hypercubes with
deﬁcit by 2 greater then the surplus are in F. But all such have their bottom set,
a three-element set disjoint from the set {a, b, c, d} in F.Thus F contains 11 three
element sets, all subsets of the six-element set X −{a, b, c, d}. By the Corollary
2.1, F is Frankl’s. □

AN ATTEMPTATFRANKL’SCONJECTURE 37

Lemma 3.2. Let |X| =10 and F contain two intersecting three-element sets.
Then F is Frankl’s.

Proof. Again, we may assume that F does not contain one- or two-element
sets. We know also that two three-element sets in F can not intersect in a two-
element set by Lemma 3.1. So, let {a, b, c}, {a, d, e}∈F. The weight function we
choose is w(a)=7, w(b)= w(c)= w(d)= w(e)=5 and w(x) = 1 for all other
x ∈ X. The target weight t(w) = 16. We consider an {a, b, c, d, e}-hypercube C
with bottom set K. Let us deﬁne a few groups of sets we will use often in this
proof: • L10 = {K ∪{b},K ∪{c},K ∪{d},K ∪{e}}
• L20 = {K ∪{a, b},K ∪{a, c},K ∪{a, d},K ∪{a, e}}
• L21 = {K ∪{b, d},K ∪{b, e},K ∪{c, d},K ∪{c, e}}
• L22 = {K ∪{b, c},K ∪{d, e}
• L30 = {K ∪{a, b, c},K ∪{a, d, e}
• L31 = {K ∪{a, b, d},K ∪{a, b, e},K ∪{a, c, d},K ∪{a, c, e}}
• L32 = {K ∪{b, c, d},K ∪{b, c, e},K ∪{b, d, e},K ∪{c, d, e}}
• L40 = {K ∪{a, b, c, d},K ∪{a, b, c, e},K ∪{a, b, d, e},K ∪{a, c, d, e}}
Notice that

(3.1) |L40 ∩F| ⩾ max{|L10 ∩F|, |L21 ∩F|}

We consider possible sizes of K and have cases:
(1) |K| = 1. Then the surplus of the top set of C is 12, and we do not have
level 0 and level 1 sets in F. Moreover, if there are more that two level 2 sets in
F, then two of them must form a couple of three-element sets with common two
elements, so F is Frankl’s by Lemma 3.1. On the other hand, if there are at most
two level 2 sets in F, then their combined deﬁcit is at most 10, which is less than
surplus of the top set. All the sets on levels 3 and 4 have weight at least t(w) = 16,
so in these hypercubes s(C) ⩾ d(C).
(2) |K| = 2. Then K/∈F, and by Lemma 3.1 there can be at most 1 level 1
set in F. The surplus of the top set is 13.
If there are no level 1 sets in F, then the only sets in C with weights less than
t(w) are on the level 2 and their combined deﬁcit must be at least 14. Any set
from L22 (deﬁcit 4) which is in F implies that a set from L30 (surplus 3) is also in
F, which means that the sets from L22 contribute to the total deﬁcit by at most
2. The sets from L21 have deﬁcit 4 each, while the sets from L40 have surplus 8
each, so we may disregard these two groups. Finally, the combined deﬁcit of the
sets from L20 is at most 8, so in this case s(C) ⩾ d(C).
Let us now assume that one level 1 set is in F. If this set is K ∪{a} (deﬁcit 7),
then both sets in L30 and the top set of the hypercube are in F, which means
s(C) ⩾ 19. So, the deﬁcit of the level 2 sets must be at least 13. Any set from L21
(deﬁcit 4) which is in F implies that a set from L31 (surplus 3) is also in F.The
total deﬁcit from these two groups is at most 4. It means that L20 and L22 have to
contribute by 9 to the total deﬁcit. Hence, at least 1 set from L22 is in F. If there
is precisely 1 of them, say K ∪{b, c}∈F, then there must be at least 3 sets from

38 MARKOVI ·C

L20 in F, so one of them contains neither b,nor c. This set together with K ∪{b, c}
implies that a set from L40 is in F, which adds 8 to the total surplus, and that can
not be equaled by remaining set from L20. Thus, both sets from L22 are in F. But,
then the set K ∪{b, c, d, e}∈F (surplus 6), which means that the total deﬁcit of
the sets from L20 must be at least 7, so all four are in F. This means that again
we have a set from L40 in F, and that s(C) is again greater than d(C).
Now, let the the level 1 set in F be from L10,say K ∪{b} (deﬁcit 9). Then
the sets K ∪{a, b, c} and K ∪{a, b, d, e} are both in F, so the total surplus of them
and the top set is at least 24. Hence, the sets on level 2 must contribute at least 16
to the total deﬁcit. The deﬁcits of the sets in L21 (4 each) which are in F can be
cancelled by surpluses of the sets K ∪{a, b, c, d} and K ∪{a, b, c, e} (8 each), as any
one of L21 sets which is in Fimplies that one of K ∪{a, b, c, d} and K ∪{a, b, c, e} is
in F, while any three L21 sets in Fimply that both K ∪{a, b, c, d} and K ∪{a, b, c, e}
are in F. Thus, the deﬁcit 16 must come entirely from L20 and L22, which means
that all six of those sets must be in F. But then the set K ∪{a, d, e} (surplus 3) is
also in F, which again pushes the surplus of C above the deﬁcit.

(3) |K| =3 and K ∈F. There can be at most two such hypercubes, otherwise
there would be two three-element sets in F which intersect in a two-element set.
We wish to prove that in such hypercubes d(C) ⩽ s(C) + 4. Assume not. Both L30
sets must be in F, and combined surplus of them and the top set is 22, while the
deﬁcit of K is 13. Any L10 set in F has the deﬁcit 8, while any L40 set has surplus
9. As |L40 ∩F| ⩾ |L10 ∩F|, we may disregard these two groups. If K ∪{a}∈F,
the deﬁcit increases to 19. But, then |L31 ∩F| ⩾ |L21 ∩F| and the deﬁcit of a L21
set is 3, while the surplus of a L21 set is 4, so we may disregard these two groups,
as well. Thus, the sets in L20 (each with deﬁcit 1) and L22 (each with deﬁcit 3)
must contribute by 8 to the total deﬁcit, so both sets in L22 must be in F. But,
then the set K ∪{b, c, d, e}∈F, and the surplus is increased by 7. The deﬁcit from
the sets in L20 and L22 should now be at least 15, which is impossible. We get
d(C) ⩽ s(C) + 4 in this case.
If K ∪{a} /∈F, then the level 2 sets must contribute to the deﬁcit by at least
14 (the surpluses of the top set and L30 sets adds up to 22, while the deﬁcit of K
is 13; the sets in L10 and L40 are still disregarded). The deﬁcits of sets in L20 are 1
each, and the deﬁcits of the sets in L21 and L22 are 3 each. So, at least 4 of the sets
in L21 and L22 are in F. The sets in L21 and L22 can be split into three disjoint
pairs, such that the union of any two is K ∪{b, c, d, e}.Thus, K ∪{b, c, d, e}∈F,
and the surplus is increased by 7. Now, the sets on level 2 must contribute at least
21 to the total deﬁcit which means that all of L21 and L22 sets are in F, as well
as three of the L20 sets. But, then we get that (by unions of L20 and L21 sets) all
four of L31 sets are in F, and the surplus of each is 4. Again, d(C) ⩽ s(C)+4.

(4) |K| =3and K/∈F. The surplus of the top set is 14, the sets in L10
and L40 are disregarded. If K ∪{a}∈F (deﬁcit 6), then both L30 sets are in F
(surplus 4 each). In this case again |L31 ∩F| ⩾ |L21 ∩F| and we can disregard these
two groups. Then the sets in L20 and L22 can have total deﬁcit at most 16, which
means that d(C) ⩽ s(C). If K ∪{a} /∈F, then the sets in L21 ∩F contribute to

AN ATTEMPTATFRANKL’SCONJECTURE 39

the total deﬁcit at most 12, so L20 and L22 should contribute by at least 3. But, if
any of them is in F, then a set from L30 (surplus 4) is in F. Thus, the total deﬁcit
of the L20 and L22 sets should be at least 7, so either both of the L22 sets, or all
four L20 sets should be in F. In both cases, the other set from L30 is in F, and the
total deﬁcit of the sets from L20 and L22 which are in F should be at least 10. But,
then all six of them are in F, which means that K ∪{b, c, d, e}∈F (as the union
of the two L22 sets). Therefore, in all cases d(C) ⩽ s(C) in such hypercubes C.

(5) |K| = 4. Then each set has weight by 1 greater than the corresponding
set in a hypercube with three-element bottom set. So, because of the previous
case, we only need to investigate the hypercubes C with at most 3 sets in F (as
d(C′) ⩽ s(C′)+4 in hypercubes C′ with three-element bottom set), and with K ∈F.
However, such hypercubes do not exist, as K ∈F implies that both L30 sets and
the top set of C are in F.

(6) |K| =0 and |K| = 5. The bottom and the top hypercube will be shown
to have combined surplus at least 8 greater than the deﬁcit, which will cover for
the deﬁcits from the two ‘bad’ hypercubes with three-element bottom sets. In the
bottom hypercube, we may assume ∅∈F (deﬁcit 16), and we know that the sets
{a, b, c}, {a, d, e} and {a, b, c, d, e} are all in F, with combined surpluses adding
up to 13. Any other set in the bottom hypercube which might be in F must be
on the level 4 and have weight greater than t(w). In the top hypercube we have
X ∈F, with surplus 16. So, we need to show that combined deﬁcits of the sets in
the top hypercube which are in F can be by at most 5 greater than the surpluses
of the sets in the top hypercube which are in F other than X. Assume not. By
the inequality (3.1) and the fact that the surplus of a set from a set from L40 is
11, while the deﬁcit of a set from L10 is 6, and the deﬁcit of a set from L21 is 1,
we can disregard the sets from L40, L10 and L21. The remaining sets in the top
hypercube with the weight less than t(w) are the bottom (X −{a, b, c, d, e}, deﬁcit
11), the set X −{b, c, d, e} with deﬁcit 4, and the two L22 sets, each with deﬁcit 1.
Their combined deﬁcits can be at most 17. But if any of the ﬁrst two is in F, then
so are both of the L30 sets, each with surplus 6. This ﬁnishes the proof. □

Lemma 3.3. If |X| =10 and F contains no three-element sets, then F is
Frankl’s.

Proof. Assume not. Then F does not contain one- or two-element sets, either.
If there are no four-element sets in F, then the average cardinality of a set in F is
at least 5 (i.e., we pick for our weight function any nonzero constant function), so
we are done. Otherwise, let {a, b, c, d}∈F. We pick the weight function w, deﬁned
by w(a)= w(b)= w(c)= w(d)=2.5and w(x) = 1 for all other x ∈ X. The target
weight t(w) = 8. Let us consider an {a, b, c, d}-hypercube C with the bottom set
K. We have cases:

(1) |K| = 1. Then any set from C that may be in F has weight at least 8.5.

(2) |K| = 2. The only sets in C that can be in F and have weight less than
t(w) are those on the level 2, each with deﬁcit 1. The top set has surplus 4, so at

40 MARKOVI ·C

least 5 of the level 2 sets must be in F. But that implies that all four of the level
3 sets (each with surplus 1.5) must be in F,so d(C) ⩽ s(C).

(3) |K| = 3. The sets in such a hypercube that have weight less than t(w)
are all on level 1 (each with deﬁcit 2.5), and the top set has surplus 5. So, at least
three level 1 sets must be in F. However, the union of three such gives a level 3 set
in F,so s(C) ⩾ 7.5. Then we must have all four level 1 sets in F, which in turn
implies all four level 3 sets are in F. In all cases d(C) ⩽ s(C).

(4) |K| =4or |K| = 5. We prove just for |K| = 4, as the case |K| = 5 is easier
(each set has weight by 1 greater than the corresponding set in a hypercube with
a four-element bottom set). The sets with weight less than t(w)are K (deﬁcit 4)
and the level 1 sets (each with deﬁcit 1.5). The surplus of the top set is 6, so K
and at least two of the level 1 sets are in F. The two level 1 sets imply a level 2
set (surplus 1) in F, so then s(C) ⩾ 7. Thus, at least three level 1 sets must be
in F. But, then at least three level 2 sets and a level 3 set are in F,too,which
means that s(C) ⩾ 12.5. This is more than the combined deﬁcits of levels 0 and 1,
so again d(C) ⩽ s(C).

(5) |K| =0 and |K| = 6. These two hypercubes together can contain at most
two sets with weights less than t(w), namely ∅ and X −{a, b, c, d}. The combined
deﬁcits of those equals the combined surpluses of X and {a, b, c, d}, which we know
are in F. □

Lemma 3.4. If F contains precisely one or precisely three 3-element sets and
|X| =10, then F is Frankl’s.

Proof. Again we assume the opposite, and may assume F contains no one-
or two-element sets. We ﬁrst consider the case when F contains precisely three
three-element sets. Let these sets be {a, b, c}, {d, e, f } and {g, h, i}. The weight
function will be w(a)= w(b)= w(c) = 3, with w(x) = 1 for all other x ∈ X,and
the target weight t(w) = 8. As before, we consider an {a, b, c}-hypercube C with
least set K and have cases:

(1) |K| = 1. The only set in such a hypercube which may be in F is the top
one, which has weight 10.

(2) |K| = 2. Again, the only sets in such a hypercube which may be in F are
on levels 2 and 3, and they have weight at least t(w)=8.

(3) |K| =3 and K/∈{{d, e, f }, {g, h, i}}. The sets in such a hypercube with
weights less than t(w) are on level 1, with deﬁcits 2 each. The top set has surplus
4, so all three level 1 sets must be in F. But, then all three level 2 sets are in F,
too, which means s(C)=7 > 6 ⩾ d(C).

(4) 4 ⩽ |K| ⩽ 6, and K ̸= {d, e, f, g, h, i}.We prove it for |K| =4, as in the
other cases we have corresponding sets with larger weights, so an analogous proof
will work. K has deﬁcit 4, and the surplus of the top set is 5, so there must be at
least two level 1 sets (each with deﬁcit 1) in F. But, then their union gives at least
one level 2 set in F,so s(C)=7 ⩾ d(C).

AN ATTEMPTATFRANKL’SCONJECTURE 41

(5) |K| =0 and |K| = 7. The sets in these two hypercubes which may be in
Fand have weight less than t(w)are ∅ and X −{a, b, c} with aggregate deﬁcit 9,
while the sets which we know are in F, X and {a, b, c}, have aggregate surplus 9.
(6) K1 = {d, e, f }, K2 = {g, h, i} and K3 = {d, e, f, g, h, i}. All three bottom
sets and all three top sets are in F, the deﬁcits of former adding up to 12, while
the surpluses of the latter add up to 15. Moreover, the number of level i sets in
the hypercube with bottom set K3 which are in F is greater than or equal to the
number of level i sets in each of the other two hypercubes, for i = 1, 2. The only
sets in these three hypercubes, other than the bottom ones, which have weights less
than t(w) are the level 1 sets of the hypercubes with bottom sets K1 and K2.
If the hypercube with bottom set K3 contains no level 1 sets in F, then there
are no sets in these three hypercubes with weight less than t(w) other then K1, K2
and K3, so deﬁcits add to 12, while surpluses are at least 15.
If the hypercube with bottom set K3 contains exactly one level 1 set in F(sur-
plus 1), then the deﬁcit of the level 1 sets in the other two hypercubes are at most
4, so the combined deﬁcits are at most 16, and combined surpluses are at least 16.
If the hypercube with bottom set K3 contains exactly two level 1 sets in F
(combined surplus 2), then it also contains a level 2 set in F (surplus 4). The
deﬁcits of the level 1 sets in the other two hypercubes can be at most 8, so the
combined deﬁcits are at most 20, and combined surpluses are at least 22.
If the hypercube with bottom set K3 contains exactly three level 1 sets in F,
all three level 2 sets of this hypercube are also in F. The aggregate surplus of these
three hypercubes must be at least 30, which is more than the deﬁcits of all the sets
in these hypercubes with weight less than t(w) (24).
The case when there is exactly one three-element set in F is dealt with in
exactly the same fashion (same weights etc.), except that there are no ‘special’
hypercubes from the last case of the proof for three three-element sets in F. □

Now we consider a counterexample to Frankl’s conjecture with |X| = 10. By
the Corollary 2.2, F must contain a nine-element set. Alternatively, we could have
just used the Lemma 2.3 and quoted [13] result that there are no counterexamples
with a 9-element largest set.

Lemma 3.5. Let |X| =10 and F contain precisely two three-element sets, which
do not intersect, and a nine-element set. Then F is Frankl’s.

Proof. Assume not. Then F contains no one- or two-element sets. Let the two
three-element sets mentioned in the statement be {a, b, c} and {d, e, f }. We consider
the {a, b, c}-hypercube C1 with bottom set {d, e, f } and the {d, e, f }-hypercube C2
with bottom set {a, b, c}. Without loss of generality we may assume that the
number of level 1 sets in C1 which are in F is not less than the number of level 1
sets in C2 which are in F. Then we consider weight function w such that w(a)=
w(b)= w(c)=3 and w(x) = 1 for all other x ∈ X. The proof goes the same
as when there is precisely one three-element set in F, with the exception of the
hypercube C2. The level 1 sets in this hypercube which are in F produce deﬁcit of
2 each. However, the level 1 sets in the {d, e, f }-hypercube C2 are top sets of their

42 MARKOVI ·C

{a, b, c}-hypercubes, which have |K| = 1 and no other set from these hypercubes
is in F. As each such hypercube has surplus 2 and there are at least as many of
them as there are level 1 sets in C1 which are in F, the deﬁcit of level 1 sets of C1 is
covered. The level 2 sets of C1 have weight 9 (surplus 1), so we need not consider
them, either. Finally, {d, e, f } has deﬁcit 5, while {a, b, c, d, e, f } has surplus 3. So,
we need only to cover the total deﬁcit of 2 from C1. This we do with the nine-
element set we assume is in F. Let this set be L.If {a, b, c} ̸⊆ L, then L is in the
top hypercube and has weight 13 (surplus 5). Other sets of the top and bottom
hypercubes which have deﬁcit have already been covered by surpluses of {a, b, c}
and X, so this set covers the deﬁcit of C2.If {a, b, c}⊆ L, then L is the top set
of an {a, b, c}-hypercube with a six-element bottom set. The bottom set of this
hypercube is the only set in it which has weight less than t(w) (deﬁcit 2), so the
surplus 7 of L is suﬃcient to cover both the deﬁcit of 2 from this bottom set and
deﬁcit 2 fron C2. □

Theorem 3.1. A ﬁnite union-closed family F of ﬁnite sets with largest set
having at most ten elements contains an element a such that a is a member of at
least half of the sets in F.
 Acknowledgements

The author wishes to thank several people for help in getting these results.
Ralph Mckenzie is responsible for the relation ‘⩽’ from Deﬁnition 2.3 and the proof
of Lemma 2.3. Mikl´os Mar´oti suggested assigning the weights to the sets after he
heard some of the initial proofs (which worked for the case |X| = 9). Ivica Boˇsnjak
found an error in one of the proofs and proofread the paper.

References

[1] T. Abe, Strong semimodular lattices and Frankl’s conjecture, Algebra Universalis 44:3–4
(2000), 379–382.
[2] T. Abe, Excess of a lattice, Graphs Combin. 18:3 (2002), 395–402.
[3] T. Abe and B. Nakano, Lower semimodular types of lattices: Frankl’s conjecture holds for
lower quasi-semimodular lattices, Graphs Combin. 16:1 (2000), 1–16.
[4] E. Brown and T. P. Vaughan, Conﬁgurations with subset restrictions, J. Combin. Math.
Combin. Comput. 48 (2004), 197–215.
[5] K. Dohmen, A new perspective on the union-closed sets conjecture, Ars Combin. 58 (2001),
183–185.
[6] D. Duﬀus and B. Sands, An inequality for the sizes of prime ﬁlters of ﬁnite distributive
lattices, Discrete Math. 201:1–3 (1999), 89–99.
[7] M. El-Zahar, A graph-theoretic version of the union-closed sets conjecture, J. Graph Theory
26:3 (1997), 155–163.
[8] L. F. Fitina and J-C. Renaud, On union-closed sets and Conway’s sequence, Bull. Austral.
Math. Soc. 47:2 (1993), 321–332.
[9] W. Gao and H. Yu, Note on the union-closed sets conjecture,Ars Combin. 49 (1998), 280–
288.
[10] R. T. Johnson and T. P. Vaughan, On union-closed families, I, J. Combin. Theory Ser. A
84:2 (1998), 242–249.
[11] G. Lo Faro, A note on the union-closed sets conjecture, J. Austral. Math. Soc. Ser A 57:2
(1994), 230–236.
 AN ATTEMPTATFRANKL’SCONJECTURE 43

[12] G. Lo Faro, Union-closed sets conjecture: improved bounds, J. Combin. Math. Combin.
Comp. 16 (1994), 97–102.
[13] R. Morris, FC-families and improved bounds for Frankl’s conjecture, European J. Combin.
27:2 (2006), 269–282.
[14] T. Nishimura and S. Takashi, Around Frankl’s conjecture, Sci. Rep. Yokohama Nat. Univ.
Sect. I Math. Phys. Chem. 43 (1996), 15–23.
[15] R. M. Norton and D. G. Sarvate, A note of the union-closed sets conjecture, J. Austral. Math.
Soc. Ser A 16:3 (1993), 411–413.
[16] B. Poonen, Union-closed families, J. Combin. Theory Ser. A 59:2 (1992), 253–268.
[17] D. Reimer, An average set size theorem, Combin., Probab. and Comput. 12:1 (2003), 89–93.
[18] J-C. Renaud, Is the union-closed sets conjecture the best possible?, J. Austral. Math. Soc.
Ser A 51 (1991), no. 2, 276–283.
[19] J-C. Renaud, A second approximation to the boundary function on union-closed collections,
Ars Combin. 41 (1995), 177–188.
[20] J-C. Renaud and D. G. Sarvate, On the union-closed sets conjecture,Ars Combin. 27 (1989),
149–153.
[21] J-C. Renaud and D. G. Sarvate, Improved bounds for the union-closed sets conjecture,Ars
Combin. 29 (1990), 181–185.
[22] I. Rival (ed.), Graphs and Order, NATO Advanced Science Institute Series C: Mathematical
and Physical Sciences, 147, Reidel, Dordrecht–Boston, 1985, p. 525.
[23] R. P. Stanley, Enumerative Combinatorics, Vol. I, The Wadsworth and Brooks/Cole Math-
ematics Series, The Wadsworth and Brooks/Cole Advanced Books and Software, Monterey,
1986.
[24] T. P. Vaughan, Families implying the Frankl conjecture, European J. Combin. 23:7 (2002),
851–860.
[25] T. P. Vaughan, A note on the union-closed sets conjecture, J. Combin. Math. Combin. Com-
put. 45 (2003), 95–108.
[26] T. P. Vaughan, Three-sets in a union-closed family, J. Combin. Math. Combin. Comput. 49
(2004), 73–84.
[27] P. Winkler, Union-closed sets conjecture, Austral. Math. Soc. Gaz. 14 (1987), 99.
[28] P. W´ojcik, Density of union-closed families, Discrete Math. 105:1–3 (1992), 259–267.

Prirodno-matematiˇcki fakultet
21000 Novi Sad
Serbia
pera@im.ns.ac.yu
