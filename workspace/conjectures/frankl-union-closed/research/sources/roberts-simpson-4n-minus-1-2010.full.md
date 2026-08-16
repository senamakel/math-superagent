<!-- source: http://ajc.maths.uq.edu.au/pdf/47/ajc_v47_p265.pdf | converted from PDF -->

AUSTRALASIAN JOURNAL OF COMBINATORICS
Volume 47 (2010), Pages 265–267

A note on the union-closed sets conjecture

Ian Roberts

School of Engineering and Information Technology
Charles Darwin University
Darwin, Northern Territory 0909
Australia
Ian.Roberts@cdu.edu.au

Jamie Simpson

Department of Mathematics and Statistics
Curtin University of Technology
GPO Box U1987, Perth
Western Australia 6845
Australia
simpson@maths.curtin.edu.au

Abstract

A collection A of ﬁnite sets is closed under union if A, B ∈A implies
that A ∪ B ∈A. The Union-Closed Sets Conjecture states that if A is
a union-closed collection of sets, containing at least one non-empty set,
then there is an element which belongs to at least half of the sets in
A. We show that if q is the minimum cardinality of ∪A taken over all
counterexamples A, then any counterexample A has cardinality at least
4q − 1.

A collection A of ﬁnite sets is closed under union if A, B ∈A implies that
A ∪ B ∈A. The Union-Closed Sets Conjecture (also called Frankl’s Conjecture)
states that if A is a union-closed collection of sets, containing at least one non-
empty set, then there is an element which belongs to at least half of the sets in
A. The conjecture dates from 1979 and is generally attributed to Peter Frankl [2].
Some authors place the further condition on A that it does not contain the empty
set. The results of this note apply to either version of the conjecture. A number of
necessary conditions for a counterexample have been established, including that if A
is a counterexample then |A| ≥ 37 [4] and that |∪A| ≥ 12 [1] where ∪A = ∪A∈AA.
See [1] and [3] and their bibliographies for more background. In this note we show
that if q is the minimum cardinality of ∪A taken over all counterexamples then for
any counterexample A we have |A| ≥ 4q − 1. It is known that q ≥ 12 [1] so this
implies that a counterexample has cardinality at least 47.

266 IAN ROBERTS AND JAMIE SIMPSON

We say that A is a basis set in A if it is not the union of other sets in A. Suppose
that A is a counterexample with |A| =2n + 2 for some integer n. Then no element
occurs in more than n of its sets. If we remove a basis set from A,then weget a
smaller collection which is also a counterexample. A counterexample of minimum
size must therefore contain an odd number of sets.
Let q be the minimum cardinality of ∪A taken over all counterexamples A.We
will obtain a lower bound for |A| in terms of q. Henceforth A will be a minimal
counterexample to the conjecture with |A| =2n +1. Set S = ∪A and note that
|S|≥ q. We deﬁne
 Ax = {A ∈A : x ∈ A}
Ax = {A ∈A : x ̸∈ A}
Cx = ∪Ax
C = {Cx : x ∈ S}
D = A\{S}\C
Dx = {A ∈D : x ∈ A}.

Clearly, Cx is an element of A for each element x of S. Since A is a minimal
counterexample there will be elements which occur in exactly n of the sets in A
(otherwise we could remove a basis set to give a smaller counterexample). We set
H = {x : |Ax| = n}. Let B be the collection of basis sets in A. If a and b are elements
of A,thenwesay that a dominates b if whenever b occurs in a set A in A then a
also occurs in that set. This is equivalent to saying b ̸∈ Ca. We will assume that A
contains no mutually dominating pair of elements, since if such a pair existed then
we could replace it with a single element without altering the size of A.Note that
by this assumption the sets Ca are distinct.

Lemma 1 If a ̸∈ H,then H ⊆ Ca and if x ∈ H,then H\{x}⊆ Cx.

Proof: Let y ∈ H. We show that y ∈ Ca where a ̸∈ H. Since y occurs in n sets and
a occurs in fewer than n sets, there exists A in A such that y ∈ A and a ̸∈ A which
implies y ∈ Ca. It follows that H ⊆ Ca.

For the second part let y ∈ H, y ̸= x. We are assuming that x and y do not dominate
each other. So there exists A ∈A such that y ∈ A, x ̸∈ A so A ⊆ Cx and therefore
y ∈ Cx. □

Lemma 2 No set Ca is a basis set.

Proof: Suppose that Ca is a basis set. If a ̸∈ H then by Lemma 1 A\{Ca} is a union-
closed collection in which no element occurs more than n − 1 times, contradicting
the minimality of A. If, on the other hand, a ∈ H, then choose a basis set B which
contains a. Then by Lemma 1 A\{B, Ca} is a union-closed collection of 2n−1setsin
which no element occurs more than n − 1 times, again contradicting the minimality
of A. □

THE UNION-CLOSED SETS CONJECTURE 267

Theorem 3 If x ∈ H and a ̸∈ H,then |Dx| = n − q and |Da| <n − q.

Proof: Let x ∈ H. By Lemma 1, x occurs in all sets Cb with b ̸= x as well as in S,
so x occurs in |Ax|− q = n − q sets in D.

Now assume, without loss of generality, that |Da| is maximal for a ∈ S\H..

If there exists b ̸= a such that a ̸∈ Cb,then b dominates a and there exists a basis set
which contains b but not a. By Lemma 2 this belongs to D so b occurs more often
in D than a which is a contradiction.

If, on the other hand, a ∈ Cb for all b ̸= a then a occurs in q sets of A\D.If a occurs
in n − q or more sets in D then it occurs in at least n sets in A which means a ∈ H.
□

Theorem 4 If A is a minimal counterexample, then |A| ≥ 4q − 1.

Proof: Consider Ax and Ax for some x ∈ H. Then |Ax| = n, |Ax| = n +1 and
|Dx| = n − q by Theorem 3. Since Ax is union-closed, there exists an element a in
at least half its sets. By Theorem 3 a occurs in at most n − q sets in D. By Lemma
1, each set in A\D except Cx contains x so Ax ⊆D ∪ {Cx}.Thus a is in at most
n − q +1 sets in Ax. Hence |Ax|≤ 2(n − q + 1) which implies n ≥ 2q − 1. Thus
|A| =2n +1 ≥ 4q − 1. □

Corollary 5 If A is a minimal counterexample, then |A| ≥ 47.

Proof: Boˇsnjak and Markovi«c [1] have recently shown that a minimal counterexample
to the conjecture has q ≥ 12. □

Acknowledgement We thank the referee for many suggestions.

References

[1] I. Boˇsnjak and P. Markovi«c, The 11-element case of Fankl’s conjecture, Electr. J.
Combin. 15 (2008), #R88.

[2] P. Frankl, Extremal set systems, in The Handbook of Combinatorics, MIT Press,
North-Holland, 1995 (Chap. 24).

[3] P. Markovi«c, An attempt at Frankl’s Conjecture, Publ. Inst. Math. (Beograd)
(N.S.) 81 (95) (2007), 29—43.

[4] R. Morris, FC-families and improved bounds for Frankl’s conjecture, Europ. J.
Combin. 27 (2004), 269—282.

(Received 20 Nov 2009; revised 11 Mar 2010)
