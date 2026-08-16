<!-- source: https://arxiv.org/html/1309.3297v2 | converted from HTML -->

The journey of the union-closed sets conjecture

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:1309.3297v2 [math.CO] 30 Oct 2013

# The journey of the union-closed sets conjecture

Henning Bruhn Oliver Schaudt

###### Abstract

We survey the state of the union-closed sets conjecture.

## 1 Introduction

One of the first mentions [6] of the union-closed sets conjecture calls it “a much-travelled conjecture”. This is indeed so. Geographically it has spread from Europe to at least North America, Asia, Oceania and Australia. Mathematically it has ventured from its origins in extremal set theory to lattice and graph theory. In this survey we strive to trace its journey.

The main attraction of the conjecture is certainly its simple formulation. A family 𝒜 \mathcal{A} of sets is *union-closed*if for every two member-sets A, B ∈ 𝒜 A,B\in\mathcal{A} also their union A ∪ B A\cup B is contained in 𝒜 \mathcal{A}.

###### Union-closed sets conjecture.

Any finite union-closed family of sets 𝒜 ≠ { ∅ } \mathcal{A}\neq\{\emptyset\} has an element that is contained in at least half of the member-sets.

An example of a union-closed family is given in Figure 1(a), where we have omitted commas and parentheses. There, one may count that the elements 1, 2, 3 1,2,3 appear each in only 12 12 of the 25 25 member-sets, which is less than half of the sets. Each of the other elements 4, 5, 6 4,5,6 however is contained in 16 16 sets, more than enough for the family to satisfy the conjecture. Power sets are other examples of union-closed families, and there the conjecture is tight: every element appears in exactly half of the member-sets.

123456 123456
12345 ​ 12346 ​ 12356 ​ 12456 ​ 13456 ​ 23456 12345\hskip 9.24994pt12346\hskip 9.24994pt12356\hskip 9.24994pt12456\hskip 9.24994pt13456\hskip 9.24994pt23456
1234 ​ 1235 ​ 1236 ​ 1456 ​ 2456 ​ 3456 1234\hskip 9.24994pt1235\hskip 9.24994pt1236\hskip 9.24994pt1456\hskip 9.24994pt2456\hskip 9.24994pt3456
123 ​ 145 ​ 246 ​ 356 ​ 456 123\hskip 9.24994pt145\hskip 9.24994pt246\hskip 9.24994pt356\hskip 9.24994pt456
45 ​ 46 ​ 56 45\hskip 9.24994pt46\hskip 9.24994pt56
4 ​ 5 ​ 6 4\hskip 9.24994pt5\hskip 9.24994pt6
∅ \emptyset

(a) Union-closed

123456 123456
12356 ​ 12346 ​ 12345 12356\hskip 9.24994pt12346\hskip 9.24994pt12345
1236 ​ 1235 ​ 1234 1236\hskip 9.24994pt1235\hskip 9.24994pt1234
456 ​ 236 ​ 135 ​ 124 ​ 123 456\hskip 9.24994pt236\hskip 9.24994pt135\hskip 9.24994pt124\hskip 9.24994pt123
56 ​ 46 ​ 45 ​ 23 ​ 13 ​ 12 56\hskip 9.24994pt46\hskip 9.24994pt45\hskip 9.24994pt23\hskip 9.24994pt13\hskip 9.24994pt12
6 ​ 5 ​ 4 ​ 3 ​ 2 ​ 1 6\hskip 9.24994pt5\hskip 9.24994pt4\hskip 9.24994pt3\hskip 9.24994pt2\hskip 9.24994pt1
∅ \emptyset

(b) Intersection-closed

Figure 1: A union-closed family and its complement

Despite its apparent simplicity the union-closed sets conjecture remains wide open. This is certainly not for lack of interest – there are about 50 articles dedicated to the conjecture, as well as several websites [28, 69, 70]. Due to this extensive research activity, we now know that the conjecture is satisfied for various union-closed families 𝒜 \mathcal{A}. For instance:

- •

if 𝒜 \mathcal{A} has at most 12 12 elements or at most 50 50 member-sets;

- •

if the number n n of member-sets is large compared to the number m m of elements, that is, when n ≥ 2 3 ​ 2 m n\geq\tfrac{2}{3}2^{m};

- •

if n n is small compared to m m: when n ≤ 2 ​ m n\leq 2m (where we need to assume that 𝒜 \mathcal{A} is *separating*, that is, for any two elements there exists a member-set containing exactly one of them);

- •

if 𝒜 \mathcal{A} contains one of a number of subconfigurations, such as a singleton-set;

- •

or if 𝒜 \mathcal{A} has a particular structure, for instance, if 𝒜 \mathcal{A} may be represented by a lower semimodular lattice, or by a subcubic graph.

We will discuss all these results, and give proper attributions, in the course of the article. All these partial results notwithstanding, we still seem to be far from a proof of the conjecture, and this is even the case for the obvious relaxation in which we settle for an element that appears in only, say, ≥ 1 % \geq 1\% of the member-sets. The best result in this respect is an observation by Knill (slightly improved by Wójcik) that yields always an element of frequency at least n − 1 log 2 ⁡ n \tfrac{n-1}{\log_{2}n}.

In an article [7] of 1987, Peter Winkler 1 1 1 Winkler informed us that the article was never intended to be published. Rather, this is the case of an informal letter ending up in print without Winkler even knowing. wrote “the ‘union-closed sets conjecture’ is well known indeed, except for (1) its origin and (2) its answer!” While the answer remains elusive, we can shed some light on its origins.

Most authors today attribute the conjecture to Peter Frankl, and following Frankl [26] date it to 1979. The sole exception are Balla, Bollobás and Eccles [9], who call it a “folklore conjecture” that “was well known by the mid-1970s”. We cannot resolve this conflict of attribution, nor do we have the intention to do so. However, there is no doubt that Frankl did discover the conjecture (whether he was not the first is for others to decide) and that he played an instrumental role in popularising it. Consequently, we will sometimes speak of *Frankl’s conjecture*.

In late 1979, Frankl [23] was working on traces of finite sets, a work that culminated in his article [24] of 1983. Motivated by the observation that it could be used to improve a number of bounds, Frankl formulated the conjecture when travelling from Paris to Montreal. On his way, Frankl told the conjecture to Ron Graham, who disseminated it widely. In about 1981, Dwight Duffus learnt about it, which then led to its first appearance in print: the proceedings of a workshop held in 1984 in Banff, edited by Rival [56], contain a short report of Duffus on a “problem of P. Frankl”. The second mention is Stanley [64], which simply cites Rival.

The next time the conjecture appeared in print, it had apparently travelled with Franz Salzborn from Europe to Australia. An article of 1987 in the Australian Mathematical Society Gazette [6] reports on the Annual Meeting of the society during which Jamie Simpson publicised the conjecture. We may only speculate that this is how the conjecture arrived in Papua New Guinea, where Renaud and Sarvate went on to write the first published research articles about it [62, 63, 53] in 1989–1991. They were succeeded in 1992 by Wójcik [71] in Poland and, in the USA, by Poonen [50], who wrote his influential article when he was an undergraduate. Many others followed in subsequent years.

In this survey, we aim to give a complete review of the literature on the conjecture. While we tried to track down every article with a substantial connection to the conjecture, we were not entirely successful as we could not obtain an unpublished manuscript of Zagaglia Salvi [60] that, as Wójcik [71] writes, apparently contains reformulations of the conjecture.

The focus of this survey is on the methods employed to attack the conjecture. Our treatment of the literature is therefore somewhat uneven. Whenever we can identify a technique that, to our eyes, seems interesting and potentially powerful we discuss it in greater detail.

## 2 Elementary facts and definitions

We quickly settle some notation and mention the most elementary facts. Let 𝒜 \mathcal{A} be a family of sets. We call the set U ⁡ ( 𝒜):= ⋃ A ∈ 𝒜 A U(\mathcal{A}):=\bigcup_{A\in\mathcal{A}}A of all the elements that appear in some member-set of 𝒜 \mathcal{A} the *universe of 𝒜 \mathcal{A}*. If 𝒜 \mathcal{A} is union-closed then taking the complements of all member-sets results in a family 𝒟 = { U ⁡ ( 𝒜) ∖ A: A ∈ 𝒜 } \mathcal{D}=\{U(\mathcal{A})\setminus A:A\in\mathcal{A}\} that is *intersection-closed*: if C, D ∈ 𝒟 C,D\in\mathcal{D} then also C ∩ D ∈ 𝒟 C\cap D\in\mathcal{D}.

The union-closed sets conjecture has the following equivalent form for intersection-closed families.

###### Intersection-closed sets conjecture.

Any finite intersection-closed family of at least two sets has an element that is contained in at most half of the member-sets.

Continuing with notation, we denote by

 | 𝒜 x:= { A ∈ 𝒜: x ∈ A }. \mathcal{A}_{x}:=\{A\in\mathcal{A}:x\in A\}. |  |

the subfamily of member-sets containing any given element x ∈ U ⁡ ( 𝒜) x\in U(\mathcal{A}). The cardinality | 𝒜 x | |\mathcal{A}_{x}| is the *frequency of x x*in 𝒜 \mathcal{A}. We also introduce notation for the complement of 𝒜 x \mathcal{A}_{x}:

 | 𝒜 x ¯:= 𝒜 ∖ 𝒜 x = { A ∈ 𝒜: x ∉ A }. \mathcal{A}_{\overline{x}}:=\mathcal{A}\setminus\mathcal{A}_{x}=\{A\in\mathcal{A}:x\notin A\}. |  |

We point out that, if 𝒜 \mathcal{A} is union-closed, both 𝒜 x \mathcal{A}_{x} and 𝒜 x ¯ \mathcal{A}_{\overline{x}} are union-closed as well.

With this terminology, the union-closed sets conjecture states that in every (finite) union-closed family 𝒜 \mathcal{A} there is an x ∈ U ⁡ ( 𝒜) x\in U(\mathcal{A}) with | 𝒜 x | ≥ 1 2 ​ | 𝒜 |. |\mathcal{A}_{x}|\geq\tfrac{1}{2}|\mathcal{A}|. We will call such an element x x*abundant*. When we consider an intersection-closed family 𝒟 \mathcal{D}, the intersection-closed sets conjecture asserts the existence of an element y ∈ U ⁡ ( 𝒟) y\in U(\mathcal{D}) with | 𝒟 y | ≤ 1 2 ​ | 𝒟 | |\mathcal{D}_{y}|\leq\tfrac{1}{2}|\mathcal{D}|. Such a y y is *rare*in 𝒟 \mathcal{D}. (We realise that this leads to the slightly bizarre situation that an element with frequency | 𝒜 x | = 1 2 ​ | 𝒜 | |\mathcal{A}_{x}|=\tfrac{1}{2}|\mathcal{A}| is at the same time abundant and rare.)

As Poonen [50] observed, the union-closed sets conjecture becomes false if the family is allowed to have infinitely many member-sets. Indeed, the union-closed family consisting of the sets { i, i + 1, i + 2, … } \{i,i+1,i+2,\ldots\} for every positive integer i i has infinitely many member-sets but no element has infinite frequency. As a consequence, we will tacitly presuppose that every union-closed family considered in this survey has only finitely many member-sets.

Additionally, we will always require the universe to be finite as well. This is no restriction. If, for a union-closed family 𝒜 \mathcal{A}, the universe has infinite cardinality there will be infinitely many pairs of elements x x and y y in the universe of 𝒜 \mathcal{A} that cannot be separated by 𝒜 \mathcal{A}, in the sense that x ∈ A x\in A if and only if y ∈ A y\in A for all A ∈ 𝒜 A\in\mathcal{A}. In that case, we may simply delete y y from all member-sets of 𝒜 \mathcal{A}. This results again in a union-closed family that satisfies the union-closed sets conjecture if and only if 𝒜 \mathcal{A} does. Consequently, it suffices to prove the conjecture for *separating*families 𝒜 \mathcal{A}, those in which, for any two distinct elements x, y ∈ U ⁡ ( 𝒜) x,y\in U(\mathcal{A}), there is an A ∈ 𝒜 A\in\mathcal{A} that contains exactly one of x, y x,y. It is an easy observation that the universe of any (finite) separating family is finite.

We remark furthermore that, if necessary, we may always assume a union-closed family to include the empty set as a member. Adding ∅ \emptyset will at most increase the number of sets, while obviously the frequency of any element stays the same. In the case of an intersection-closed family 𝒟 \mathcal{D}, it is no restriction to suppose that ∅, U ⁡ ( 𝒟) ∈ 𝒟 \emptyset,U(\mathcal{D})\in\mathcal{D}. Indeed, adding U ⁡ ( 𝒟) U(\mathcal{D}) to 𝒟 \mathcal{D} makes satisfying the intersection-closed sets conjecture only harder, while ∅ \emptyset is always a member-set of 𝒟 \mathcal{D} unless there is an element x x appearing in every set of 𝒟 \mathcal{D}. In that case, deleting x x from every member results in an intersection-closed family that satisfies the conjecture if and only if 𝒟 \mathcal{D} does.

Given a family 𝒮 \mathcal{S} of sets, the *union-closure*of 𝒮 \mathcal{S} is the union-closed family 𝒜 \mathcal{A} defined by

 | 𝒜 = { ⋃ S ∈ 𝒮 ′ S: 𝒮 ′ ⊆ 𝒮 }. \mathcal{A}=\big\{\bigcup_{S\in\mathcal{S}^{\prime}}S:\mathcal{S}^{\prime}\subseteq\mathcal{S}\big\}. |  |

We may also say that 𝒜 \mathcal{A} is *generated*by 𝒮 \mathcal{S}.

Every union-closed family 𝒜 \mathcal{A} has a unique subset ℬ ⊆ 𝒜 \mathcal{B}\subseteq\mathcal{A} such that (a) 𝒜 \mathcal{A} is the union-closure of ℬ \mathcal{B} and (b) ℬ \mathcal{B} is inclusionwise minimal with this property. Observe that ℬ \mathcal{B} is simply the subfamily of non-empty sets B ∈ 𝒜 B\in\mathcal{A} with the property that if B = X ∪ Y B=X\cup Y for some X, Y ∈ 𝒜 X,Y\in\mathcal{A}, then X = B X=B or Y = B Y=B. The sets in ℬ \mathcal{B} are the *basis sets*of 𝒜 \mathcal{A}. Observe that 𝒜 ∖ { B } \mathcal{A}\setminus\{B\} is union-closed for B ∈ 𝒜 B\in\mathcal{A} if and only if B B is a basis set (or B = ∅ B=\emptyset).

Finally, for i, n ∈ ℕ i,n\in\mathbb{N} we use the notation [n] [n] to denote { 1, …, n } \{1,\ldots,n\} and [i, n] [i,n] for the set { i, i + 1, …, n } \{i,i+1,\ldots,n\}. We write 2 X 2^{X} for the power set of a set X X. Any set of cardinality k k is a *k k -set*. For a set X X and an element x x, we often write X + x X+x for X ∪ { x } X\cup\{x\} and X − x X-x for X ∖ { x } X\setminus\{x\}.

## 3 The many faces of the conjecture

The union-closed sets conjecture has several equivalent reformulations that each highlight a different aspect. In this section we present three reformulations, one in terms of lattices, one in the language of graphs and the last again in terms of sets. That the same problem can be posed quite naturally in such different fields is a clear indication that Frankl’s question is a very basic and fundamental one.

The reformulations also help us to gain confidence in the veracity of the conjecture. Indeed, each offers natural special cases such as semimodular lattices or subcubic graphs that would appear quite artificial in the other formulations. Proving the conjecture for such special cases then clearly adds evidence in support of the conjecture. Finally, each reformulation opens up new tools and techniques to attack the conjecture.

### 3.1 The lattice formulation

Already in its earliest mention [56] it is recognised that the union-closed sets conjecture, or rather its twin, the intersection-closed sets conjecture, has an equivalent formulation in terms of lattices. In fact, any intersection-closed 2 2 2 Or union-closed family, for that matter. However, it seems customary in the lattice context to consider intersection-closed families. family together with inclusion forms a lattice.

We recall a minimum of lattice terminology. A *finite lattice*is a finite poset ( L, ≤) (L,\leq) in which every pair a, b ∈ L a,b\in L of elements has a unique greatest lower bound, denoted by a ∧ b a\wedge b (the *meet*), and a unique smallest upper bound, denoted by a ∨ b a\vee b (the *join*). All the lattices considered in this survey will be finite. The unique minimal element is denoted by 0 0, the unique maximal element is 1 1. A non-zero element a ∈ L a\in L is *join-irreducible*if a = b ∨ c a=b\vee c implies a = b a=b or a = c a=c. We write [a):= { x ∈ L: x ≥ a } [a):=\{x\in L:x\geq a\}. For more on lattices see, for instance, Grätzer [29].

Let us first see that an intersection-closed family 𝒜 \mathcal{A} defines a lattice in a quite direct way. This is illustrated in Figure 2, which shows the lattice corresponding to the family of Figure 1(b). As pointed out in the previous section, we may assume that 𝒜 \mathcal{A} contains its universe U ⁡ ( 𝒜) U(\mathcal{A}). Then ( 𝒜, ⊆) (\mathcal{A},\subseteq) is a lattice. Indeed, the unique greatest lower bound of any A, B ∈ 𝒜 A,B\in\mathcal{A} is A ∧ B = A ∩ B ∈ 𝒜 A\wedge B=A\cap B\in\mathcal{A}, while U ⁡ ( 𝒜) ∈ 𝒜 U(\mathcal{A})\in\mathcal{A} guarantees that A A and B B always have a minimal upper bound. Such a minimal upper bound is unique: If R R and S S are two upper bounds then also R ∩ S ∈ 𝒜 R\cap S\in\mathcal{A} is an upper bound. Let us note that while A ∨ B A\vee B always contains A ∪ B A\cup B, it is usually larger.

Figure 2: The lattice of the set system in Figure 1. The join-irreducible elements are precisely { 1 }, { 2 }, { 3 }, { 4 }, { 5 }, { 6 } \{1\},\{2\},\{3\},\{4\},\{5\},\{6\}.

We now state the lattice formulation of Frankl’s conjecture:

###### Conjecture 1.

Let L L be a finite lattice with at least two elements. Then there is a join-irreducible element a a with | [a) | ≤ 1 2 | L | |[a)|\leq\tfrac{1}{2}|L|.

Let us see why Conjecture 1 is equivalent to the intersection-closed sets conjecture. Let 𝒜 \mathcal{A} be an intersection-closed family containing its universe and consider the lattice ( 𝒜, ⊆) (\mathcal{A},\subseteq). Assume Conjecture 1 to hold, that is, there is a join-irreducible J ∈ 𝒜 J\in\mathcal{A} with | [J) | ≤ 1 2 | 𝒜 | |[J)|\leq\tfrac{1}{2}|\mathcal{A}|. Suppose that every element of J J appears in some proper subset of J J that is in 𝒜 \mathcal{A}: ⋃ A ⊂ J A = J \bigcup_{A\subset J}A=J. Then, ⋁ A ⊂ J A ⊇ ⋃ A ⊂ J A = J \bigvee_{A\subset J}A\supseteq\bigcup_{A\subset J}A=J, from which follows that ⋁ A ⊂ J A = J \bigvee_{A\subset J}A=J, which is impossible as J J is join-irreducible. Thus there is an x ∈ J x\in J that does not lie in any proper subset of J J.

Next, consider an A ∈ 𝒜 A\in\mathcal{A} containing x x. Then J ∩ A J\cap A is a subset of J J containing x x and therefore equal to J J. In particular, J ⊆ A J\subseteq A and thus A ∈ [J) A\in[J). Since | [J) | ≤ 1 2 | 𝒜 | |[J)|\leq\tfrac{1}{2}|\mathcal{A}|, it follows that x x appears in at most half of the member-sets of 𝒜 \mathcal{A}.

For the other direction, consider a lattice L L and associate to every x ∈ L x\in L the set S ⁡ ( x) S(x) of join-irreducible elements z z with z ≤ x z\leq x. Then, for x, y ∈ L x,y\in L we obtain that S ⁡ ( x ∧ y) = S ⁡ ( x) ∩ S ⁡ ( y) S(x\wedge y)=S(x)\cap S(y), and thus the family 𝒜 = { S ⁡ ( x): x ∈ L } \mathcal{A}=\{S(x):x\in L\} is intersection-closed. Moreover, | 𝒜 | = | L | |\mathcal{A}|=|L|.

Supposing that the intersection-closed sets conjecture holds, we obtain a join-irreducible x ∈ L x\in L that is contained in at most half of the member-sets of 𝒜 \mathcal{A}. Then for any y ≥ x y\geq x, it follows that x ∈ S ⁡ ( y) x\in S(y) and thus | [x) | |[x)| is bounded by the number of member-sets of 𝒜 \mathcal{A} containing x x, which gives | [x) | ≤ 1 2 | L | |[x)|\leq\tfrac{1}{2}|L|.

###### Theorem 2.

Conjecture 1 is equivalent to the union-closed sets conjecture.

In view of this equivalence we will say that a lattice *satisfies Frankl’s conjecture*if Conjecture 1 holds for it. To include the trivial case, we will extend this to any lattice on less than two elements.

What are the advantages of the lattice formulation? In some sense, Frankl’s conjecture is stripped down to its bare essential parts: the elements have vanished and all that counts is the inclusion relation between the sets. Moreover, in comparison with the set formulation new special cases become natural – and attackable. We will review them next.

### 3.2 Lattice results

The formulation of the lattice version resulted in a series of verified special cases of Frankl’s conjecture. Already in Rival [56] it is mentioned, without proof, that the conjecture holds for distributive and geometric lattices. This was explicitly proved by Poonen [50], who also extended the latter case to complemented lattices.

Abe and Nakano [3] showed the conjecture for modular lattices, a case that includes distributive lattices. This, in turn, was generalised by Reinhold [52] to lower semimodular lattices. We present the proof here, as it seems to be the strongest result concerning lattice classes, and also because the proof is nice and succinct.

Let x < y x<y be two elements of a lattice. Then x x is a *lower cover*of y y if x ≤ z ≤ y x\leq z\leq y implies x = z x=z or y = z y=z for all elements z z. A lattice L L is *lower semimodular*if a ∧ b a\wedge b is a lower cover of a ∈ L a\in L, whenever b ∈ L b\in L is a lower cover of a ∨ b a\vee b.

###### Theorem 3 (Reinhold [52]).

Lower semimodular lattices satisfy Frankl’s conjecture.

###### Proof.

Let L L be a lower semimodular lattice with | L | ≥ 2 |L|\geq 2. If the unique largest element 1 ∈ L 1\in L is join-irreducible then Frankl’s conjecture is trivially satisfied. If not, we may pick a lower cover b ∈ L b\in L of 1 1, and a join-irreducible a ∈ L a\in L with a ≰ b a\nleq b. Then 1 = a ∨ b 1=a\vee b.

We claim that the function [a) → L ∖ [a) [a)\to L\setminus[a), x ↦ x ∧ b x\mapsto x\wedge b is an injection, which then finishes the proof. So, suppose that there are two distinct x, y ∈ [a) x,y\in[a) with x ∧ b = y ∧ b x\wedge b=y\wedge b. As either x ∧ y < x x\wedge y<x or x ∧ y < y x\wedge y<y, we may assume the former. This implies

 | x ∧ b = x ∧ y ∧ b ≤ x ∧ y < x. x\wedge b=x\wedge y\wedge b\leq x\wedge y<x. |  | (1) |

Now, as L L is lower semimodular, and as b b is a lower cover of 1 = x ∨ b 1=x\vee b, we obtain that x ∧ b x\wedge b is a lower cover of x x. Thus, x ∧ b = x ∧ y x\wedge b=x\wedge y by ( 1) and therefore

 | a ≤ x ∧ y = x ∧ b ≤ b, a\leq x\wedge y=x\wedge b\leq b, |  |

which contradicts our choice of a ≰ b a\nleq b. ∎

Theorem 3 was also independently proved by Herrmann and Langsdorf [30] and by Abe and Nakano [4]. In the latter article, the conjecture is also verified for a superclass, lower quasi-semimodular lattices.

If there are lower semimodular lattices there are clearly *upper semimodular*ones as well. However, this class seems to be much harder with respect to Frankl’s conjecture. Already in Rival [56] it is mentioned, without proof, that *geometric lattices*satisfy the conjecture. A proper proof was later given by Poonen [50]. A lattice is geometric, and then upper semimodular, if it may be represented as the lattice of flats of a matroid. Abe [1] treats another subclass, the so called *strong*upper semimodular lattices. Czédli and Schmidt [15] show the conjecture for upper semimodular lattices L L that are large, in the sense that | L | > 5 8 ​ 2 m |L|>\tfrac{5}{8}2^{m} where m m is the number of join-irreducible elements; they also consider planar upper semimodular lattices.

Let us mention that it is an easy consequence of the lattice formulation that, for any lattice L L, Frankl’s conjecture holds for L L or for its dual L ∗ L^{*}, or both. (The dual lattice is obtained by reversing the order.) Duffus and Sands [18] and Abe [2] derive stronger assertions for special classes of lattices.

We close this section with a wonderful application of Reinhold’s theorem that was indicated to us by one of the anonymous referees. The application concerns *graph-generated*intersection-closed families. Let G G be a fixed graph. For every set X ⊆ V ⁡ ( G) X\subseteq V(G) we write E X E_{X} for the set of edges of G G that have both their endvertices in X X. Then { E X: X ⊆ V ⁡ ( G) } \{E_{X}:X\subseteq V(G)\} is intersection-closed.

###### Theorem 4 (Knill [38]).

Given a graph G = ( V, E) G=(V,E) with at least one edge, the intersection-closed family { E X: X ⊆ V } \{E_{X}:X\subseteq V\} satisfies the intersection-closed sets conjecture.

This result is also part of Knill’s PhD thesis [37]. The theorem was later restated as a conjecture by El-Zahar [19], and, as a response to El-Zahar’s paper, reproved by Llano, Montellano-Ballesteros, Rivera-Campo and Strausz [42].

As L = { E X: X ⊆ V ⁡ ( G) } L=\{E_{X}:X\subseteq V(G)\} is intersection-closed, it is a lattice with respect to ⊆ \subseteq. We show that L L is lower semimodular. Thus, Knill’s theorem becomes a consequence of Theorem 3.

We call X ⊆ V ⁡ ( G) X\subseteq V(G)*proper*if E X ≠ E X ′ E_{X}\neq E_{X^{\prime}} for any X ′ ⊊ X X^{\prime}\subsetneq X. Note that L = { E X: X ⊆ V ⁡ ( G) ​ and X is proper } L=\{E_{X}:X\subseteq V(G)\mbox{ and $X$ is proper}\}, and so we may restrict our attention to proper vertex sets. Let X, Y ⊆ V ⁡ ( G) X,Y\subseteq V(G) be proper. First we note that

 | E X ∧ E Y = E X ∩ E Y = E X ∩ Y ​ and ​ E X ∨ E Y = E X ∪ Y. E_{X}\wedge E_{Y}=E_{X}\cap E_{Y}=E_{X\cap Y}\text{ and }E_{X}\vee E_{Y}=E_{X\cup Y}. |  |

Next we observe that E X E_{X} is a lower cover of E Y E_{Y} if and only if

 | Y = X + y 1 Y=X+y_{1} or E Y = E X + y 1 ​ y 2 E_{Y}=E_{X}+y_{1}y_{2} for some y 1, y 2 ∈ Y ∖ X y_{1},y_{2}\in Y\setminus X.  |  |

Indeed, let E X E_{X} be a lower cover of E Y E_{Y} and consider an edge y 1 ​ y 2 ∈ E Y ∖ E X y_{1}y_{2}\in E_{Y}\setminus E_{X}. Then, E X ⊊ E X ∪ { y 1, y 2 } ⊆ E Y E_{X}\subsetneq E_{X\cup\{y_{1},y_{2}\}}\subseteq E_{Y} and thus Y = X ∪ { y 1, y 2 } Y=X\cup\{y_{1},y_{2}\}. Now, if one of y 1, y 2 y_{1},y_{2}, y 2 y_{2} say, is contained in X X we have Y = X + y 1 Y=X+y_{1} and we are in the first case. If y 1, y 2 ∉ X y_{1},y_{2}\notin X then neither of y 1, y 2 y_{1},y_{2} may have a neighbour in X X as otherwise E X E_{X} would be a proper subset of E X + y 1 E_{X+y_{1}} or of E X + y 2 E_{X+y_{2}}. The other direction is obvious.

So, assume that for proper A, B ⊆ V ⁡ ( G) A,B\subseteq V(G), the set E B E_{B} is a lower cover of E A ∨ E B E_{A}\vee E_{B}. Then there are a 1, a 2 ∈ A ∖ B a_{1},a_{2}\in A\setminus B so that either A ∪ B = B + a 1 A\cup B=B+a_{1} or E A ∪ B = E B + a 1 ​ a 2 E_{A\cup B}=E_{B}+a_{1}a_{2}. If A ∪ B = B + a 1 A\cup B=B+a_{1} then A = ( A ∩ B) + a 1 A=(A\cap B)+a_{1}, and E A ∩ B E_{A\cap B} is a lower cover of E A E_{A}. In the other case, when E A ∪ B = E B + a 1 ​ a 2 E_{A\cup B}=E_{B}+a_{1}a_{2} we get

 | E A = E A ∩ E A ∪ B = ( E A ∩ E B) + a 1 ​ a 2 = E A ∩ B + a 1 ​ a 2, E_{A}=E_{A}\cap E_{A\cup B}=(E_{A}\cap E_{B})+a_{1}a_{2}=E_{A\cap B}+a_{1}a_{2}, |  |

and again E A ∩ B E_{A\cap B} is a lower cover of E A E_{A}. Thus, L L is lower semimodular, and Knill’s theorem is proved.

El-Zahar [19] observed that, when Knill’s theorem is generalised to hypergraphs, it becomes yet another reformulation of the union-closed sets conjecture.

### 3.3 The graph formulation

A more recent reformulation of the union-closed sets conjecture is stated in terms of maximal stable sets of bipartite graphs. A *stable set*of a graph G G is a vertex subset so that no two of its vertices are adjacent. A stable set is called *maximal*if no further vertex of G G can be added without violating the stable set condition. We refer to Diestel [16] for general terminology and notions on graphs.

The graph formulation of the union-closed sets conjecture is as follows:

###### Conjecture 5.

Any bipartite graph with at least one edge contains in each of its bipartition classes a vertex that lies in at most half of the maximal stable sets.

The conjecture was proposed by Bruhn, Charbit, Schaudt and Telle [11], who also proved the equivalence to Frankl’s conjecture. In analogy to the intersection-closed sets conjecture, let us call a vertex *rare*if it is contained in at most half of the maximal stable sets. Note that for every edge u ​ v uv of a bipartite graph, always one of u u and v v is rare. Indeed, this follows directly from the fact that no stable set may contain both u u and v v. Hence, in a hypothetical counterexample to Conjecture 5, one bipartition class of the graph contains only rare vertices, while no vertex in the other class is rare.

We sketch why Conjecture 5 and the intersection-closed sets conjecture are equivalent.

###### Theorem 6.

[11] Conjecture 5 holds if and only if the union-closed sets conjecture is true.

###### Proof.

To prove equivalence to the intersection-closed sets conjecture, let us first consider a bipartite graph G G with bipartition classes X, Y X,Y. By symmetry it is enough to find a rare vertex in X X. Let 𝒜 \mathcal{A} be the set of maximal stable sets of G G. It is straightforward to check that the traces of maximal stable sets in X X, the set { A ∩ X: A ∈ 𝒜 } \{A\cap X:A\in\mathcal{A}\}, is intersection-closed. Thus, if the intersection-closed sets conjecture is true, there must be a rare element x x of { A ∩ X: A ∈ 𝒜 } \{A\cap X:A\in\mathcal{A}\}, which then is a rare vertex of G G.

For the converse direction, let an intersection-closed family 𝒜 \mathcal{A} be given. We may assume that 𝒜 \mathcal{A} contains its universe U U. We define a bipartite graph G = ( V, E) G=(V,E) on V = 𝒜 ∪ U V=\mathcal{A}\cup U with edge set E = { S x: S ∈ 𝒜, x ∈ U, x ∈ S } E=\{Sx:S\in\mathcal{A},\,x\in U,\,x\in S\}. That is, G G is the incidence graph of 𝒜 \mathcal{A}. See Figure 3 for an illustration.

Then, if ℬ \mathcal{B} denotes the set of maximal stable sets of G G, it follows that 𝒜 = { B ∩ U: B ∈ ℬ } \mathcal{A}=\{B\cap U:B\in\mathcal{B}\}. Thus, if x x is a rare vertex of G G in U U, then x x is a rare element of 𝒜 \mathcal{A}. This completes the proof. ∎

Figure 3: The incidence graph of the intersection-closed family shown in Figure 1

As for the lattice fromulation, we will say that a bipartite graph *satisfies Frankl’s conjecture*if the graph is not a counterexample to Conjecture 5, or if it is edgeless.

Figure 3 shows the graph representation of intersection-closed family in Figure 1. We have to admit that it does not appear very appealing, as listing the family seems much simpler. Nonetheless, the graph formulation allows for a very compact representation of Frankl’s conjecture. This is exemplified by the graph in Figure 4 that encodes the same family as the graph in Figure 3. We arrive at this graph by iteratively deleting any vertex v v whose neighbourhood is equal to the union of neighbourhoods of some other vertices. It is easy to check that the resulting graph with v v deleted satisfies the conjecture only if the original graph does, see also [11].

Figure 4: A more succinct representation

### 3.4 Graph results

The literature on graphs provides a rich selection of natural graph classes, even bipartite ones, that may now serve as test cases for Frankl’s conjecture. So far, the conjecture has been verified for chordal bipartite, subcubic, series-parallel [11] and, in an approximate version, random bipartite graphs [12]. We present some of these results here.

A bipartite graph is said to be *chordal bipartite*if deleting vertices from the graph can never result in a chordless cycle of length ≥ 6 \geq 6.

###### Theorem 7.

[11] Chordal bipartite graphs satisfy Frankl’s Conjecture.

The proof rests on the local structure of chordal bipartite graphs. This is a general strategy that we will discuss in more detail in Section 5. The main tool here is the following lemma, where we denote by N 2 ​ ( x) N^{2}(x) the neighbours of the neighbours of a vertex x x (including x x).

###### Lemma 8.

[11] Let x, y x,y be two adjacent vertices of a bipartite graph with N 2 ​ ( x) ⊆ N ​ ( y) N^{2}(x)\subseteq N(y). Then y y is rare.

###### Proof.

Let 𝒜 \mathcal{A} denote the maximal stable sets of the chordal bipartite graph G G, and consider A ∈ 𝒜 y A\in\mathcal{A}_{y}, that is, a maximal stable set containing y y. Since y ∈ A y\in A, no neighbour of y y may be in A A and hence N 2 ​ ( x) ∩ A = ∅ N^{2}(x)\cap A=\emptyset as N 2 ​ ( x) ⊆ N ​ ( y) N^{2}(x)\subseteq N(y). Therefore, no vertex in N ⁡ ( x) N(x) is adjacent with a vertex in A A, which implies N ⁡ ( x) ⊆ A N(x)\subseteq A.

We now construct an injective mapping 𝒜 y → 𝒜 x \mathcal{A}_{y}\to\mathcal{A}_{x}: given a set A ∈ 𝒜 y A\in\mathcal{A}_{y}, first remove all members of N ⁡ ( x) N(x) from A A and then fill up the resulting set to a maximal stable set with vertices from N 2 ​ ( x) N^{2}(x). Finally, since x x is adjacent to y y, we have 𝒜 x ⊆ 𝒜 y ¯ \mathcal{A}_{x}\subseteq\mathcal{A}_{\overline{y}}. Altogether, there is an injection 𝒜 y → 𝒜 y ¯ \mathcal{A}_{y}\to\mathcal{A}_{\overline{y}}, which means that y y is rare. ∎

To finish the proof of Theorem 7 it now suffices to observe that a type of vertex known as a *weakly simplicical*vertex satisfies the conditions of the lemma. That such a vertex always exists in each bipartition class is known from the literature on chordal bipartite graphs. For details see [11].

Using results of Vaughan on 3 3 -sets and Knill’s graph generated families (discussed in Sections 5 and 3.2 respectively), we obtain Frankl’s conjecture for another natural graph class. Recall that a graph is *subcubic*if every vertex has degree at most three.

###### Theorem 9.

[11] Every subcubic bipartite graph satisfies Frankl’s conjecture.

The third class of graphs we treat are random bipartite graphs, where we can only prove a slight weakening of Frankl’s conjecture. A *random bipartite graph*is a graph on bipartition classes of cardinalities m m and n n, where any two vertices from different classes are independently joined by an edge with probability p p.

For δ > 0 \delta>0, let us say that a bipartite graph *satisfies Frankl’s conjecture up to δ \delta*if each of its two bipartition classes has a vertex for which the number of maximal stable sets containing it is at most 1 2 + δ \tfrac{1}{2}+\delta times the total number of maximal stable sets. We say that almost every random bipartite graph has property P P if for every ε > 0 \varepsilon>0 there is an N N such that, whenever m + n ≥ N m+n\geq N, the probability that a random bipartite graph on m + n m+n vertices has P P is at least 1 − ε 1-\varepsilon.

###### Theorem 10.

[12] Let p ∈ ( 0, 1) p\in(0,1) be a fixed edge-probability. For every δ > 0 \delta>0, almost every random bipartite graph satisfies Frankl’s conjecture up to δ \delta.

The main tool in the proof is the averaging approach detailed in Section 6.

### 3.5 The Salzborn formulation

Returning to the sets point of view, let us present a surprising reformulation of the conjecture that Wójcik [72] attributes to Salzborn [61]. Recall that a union-closed family 𝒜 \mathcal{A} is separating if for any two elements of its universe there is a member-set that contains exactly one of the two. It is easy to check that 𝒜 \mathcal{A} needs to have at least | U ⁡ ( 𝒜) | |U(\mathcal{A})| non-empty sets to separate all elements of its universe. Thus, if ∅ ∈ 𝒜 \emptyset\in\mathcal{A} then 𝒜 \mathcal{A} will have at least | U ⁡ ( 𝒜) | + 1 |U(\mathcal{A})|+1 member-sets. It turns out that the families with this minimum number of member-sets have a surprisingly rich structure.

Let us call a union-closed family 𝒩 \mathcal{N}*normalised*if it holds that ∅ ∈ 𝒩 \emptyset\in\mathcal{N}, 𝒩 \mathcal{N} is separating and | U ⁡ ( 𝒩) | = | 𝒩 | − 1 |U(\mathcal{N})|=|\mathcal{N}|-1. The following conjecture may be found in Wójcik [72], or, with less details, in Salzborn [61].

###### Conjecture 11 (Salzborn [61]).

Any normalised family 𝒩 ≠ { ∅ } \mathcal{N}\neq\{\emptyset\} contains a basis set B B of size | B | ≥ 1 2 ​ | 𝒩 | |B|\geq\tfrac{1}{2}|\mathcal{N}|.

Following Wójcik [72], we outline why Salzborn’s conjecture implies the union-closed sets conjecture. Consider a union-closed family 𝒜 \mathcal{A} that we may assume to contain ∅ \emptyset as a member-set. We define

 | 𝒜 ⊈ X:= { A ∈ 𝒜: A ⊈ X } ​ and ​ 𝒜 ∗:= { 𝒜 ⊈ X: X ∈ 𝒜 }. \mathcal{A}_{\nsubseteq X}:=\{A\in\mathcal{A}:A\nsubseteq X\}\text{ and }\mathcal{A}^{*}:=\{\mathcal{A}_{\nsubseteq X}:X\in\mathcal{A}\}. |  |

It is easy to check that 𝒜 ∗ \mathcal{A}^{*} is union-closed and separating. We note that X ⊆ Y X\subseteq Y if and only if 𝒜 ⊈ X ⊇ 𝒜 ⊈ Y \mathcal{A}_{\nsubseteq X}\supseteq\mathcal{A}_{\nsubseteq Y} for any X, Y ∈ 𝒜 X,Y\in\mathcal{A}. This has several consequences. Firstly, 𝒜 ⊈ X ≠ 𝒜 ⊈ Y \mathcal{A}_{\nsubseteq X}\neq\mathcal{A}_{\nsubseteq Y} if X ≠ Y X\neq Y, which implies that | 𝒜 | = | 𝒜 ∗ | |\mathcal{A}|=|\mathcal{A}^{*}|. Secondly, U ⁡ ( 𝒜 ∗) = 𝒜 ⊈ ∅ = 𝒜 ∖ { ∅ } U(\mathcal{A}^{*})=\mathcal{A}_{\nsubseteq\emptyset}=\mathcal{A}\setminus\{\emptyset\}. Finally, we remark that 𝒜 ∗ \mathcal{A}^{*} has the dual lattice structure of 𝒜 \mathcal{A}.

To summarise, 𝒜 ∗ \mathcal{A}^{*} is normalised and has the same number of members as 𝒜 \mathcal{A}. Next, we consider the basis sets of 𝒜 ∗ \mathcal{A}^{*}.

 | Every basis set of 𝒜 ∗ \mathcal{A}^{*} is of the form 𝒜 x \mathcal{A}_{x} for some x ∈ U ⁡ ( 𝒜) x\in U(\mathcal{A}).  |  | (2) |

Indeed, consider a basis set 𝒜 ⊈ X \mathcal{A}_{\nsubseteq X} of 𝒜 ∗ \mathcal{A}^{*}, and observe that 𝒜 ⊈ X = ⋃ y ∈ U ⁡ ( 𝒜) ∖ X 𝒜 y \mathcal{A}_{\nsubseteq X}=\bigcup_{y\in U(\mathcal{A})\setminus X}\mathcal{A}_{y}. Pick a smallest set S ⊆ U ⁡ ( 𝒜) ∖ X S\subseteq U(\mathcal{A})\setminus X so that still 𝒜 ⊈ X = ⋃ y ∈ S 𝒜 y \mathcal{A}_{\nsubseteq X}=\bigcup_{y\in S}\mathcal{A}_{y} and consider a bipartition S 1 ∪ S 2 = S S_{1}\cup S_{2}=S. Since 𝒜 y = 𝒜 ⊈ U ⁡ ( 𝒜 y ¯) \mathcal{A}_{y}=\mathcal{A}_{\nsubseteq U(\mathcal{A}_{\overline{y}})}, both ⋃ y ∈ S 1 𝒜 y \bigcup_{y\in S_{1}}\mathcal{A}_{y} and ⋃ y ∈ S 2 𝒜 y \bigcup_{y\in S_{2}}\mathcal{A}_{y} are members of 𝒜 ∗ \mathcal{A}^{*}. Since 𝒜 ⊈ X = ⋃ y ∈ S 1 𝒜 y ∪ ⋃ y ∈ S 2 𝒜 y \mathcal{A}_{\nsubseteq X}=\bigcup_{y\in S_{1}}\mathcal{A}_{y}\cup\bigcup_{y\in S_{2}}\mathcal{A}_{y}, 𝒜 ⊈ X \mathcal{A}_{\nsubseteq X} is the union of two member-sets of 𝒜 ∗ \mathcal{A}^{*}. As 𝒜 ⊈ X \mathcal{A}_{\nsubseteq X} is a basis set that implies that already 𝒜 ⊈ X = ⋃ y ∈ S i 𝒜 y \mathcal{A}_{\nsubseteq X}=\bigcup_{y\in S_{i}}\mathcal{A}_{y} for i = 1 i=1 or i = 2 i=2, which by the minimality of S S forces S = S i S=S_{i}. Therefore, S S has to contain a unique element x x, that is, 𝒜 ⊈ X = 𝒜 x \mathcal{A}_{\nsubseteq X}=\mathcal{A}_{x}.

Assume now Conjecture 11 to hold. Then the normalised family 𝒜 ∗ \mathcal{A}^{*} contains a basis set B ∗ B^{*} with

 | | B ∗ | ≥ 1 2 ​ | 𝒜 ∗ | = 1 2 ​ | 𝒜 |. |B^{*}|\geq\tfrac{1}{2}|\mathcal{A}^{*}|=\tfrac{1}{2}|\mathcal{A}|. |  |

As B ∗ = 𝒜 x B^{*}=\mathcal{A}_{x} for some x ∈ U ⁡ ( 𝒜) x\in U(\mathcal{A}) by ( 2) we deduce that 𝒜 \mathcal{A} satisfies the union-closed sets conjecture. We therefore have proved one direction of:

###### Theorem 12 (Salzborn [61]).

Conjecture 11 is equivalent to the union-closed sets conjecture.

We omit the proof of the other direction, which may be found in Wójcik [72].

Why do we find the Salzborn reformulation surprising? At first glance, normalised families seem to be very restricted and in some sense this is true. For instance, the statement of the union-closed sets conjecture is almost trivial for them, see Theorem 23. From a lattice point of view, however, normalised families turn out to be as general as union-closed families. We have already remarked that 𝒜 ∗ \mathcal{A}^{*} has the dual lattice structure of 𝒜 \mathcal{A}, which directly implies that every lattice type of a union-closed family is realisable as a normalised family.

We know only one application of the Salzborn formulation: Wójcik [72] uses it to obtain a non-trivial lower bound on the maximum frequency of an element in a union-closed family; see the next section.

The family 𝒜 ∗ \mathcal{A}^{*} also appears in Johnson and Vaughan [34], although defined in a slightly different way. In order to obtain a duality result, Johnson and Vaughan associate to any union-closed family 𝒜 \mathcal{A} the dual family 𝒜 ∗ \mathcal{A}^{*} and then observe that the union-closed sets conjecture is satisfied for at least one of 𝒜 \mathcal{A} and 𝒜 ∗ \mathcal{A}^{*}. We note that the analogous results in the lattice formulation and in the graph formulation are almost trivial: for lattices this amounts to considering the dual lattice, and for graphs it reduces to the observation that no stable set may contain both endvertices of an edge.

The majority of the results on the union-closed sets conjecture are with respect to the original set formulation. In the remainder of this article we stick to this formulation as well. However, a good part of the discussed techniques has a more or less direct analogue in the other formulations.

## 4 Obstacles to a proof

There are many results on special cases of the conjecture. Amazingly, if we consider an arbitrary union-closed family, without any special structure or information on the number of elements, (almost) the best result we have seems to be a simple observation due to Knill:

###### Theorem 13 (Knill [38]).

Any union-closed family 𝒜 \mathcal{A} on n n member-sets has an element of frequency at least n − 1 log 2 ⁡ ( n) \tfrac{n-1}{\log_{2}(n)}.

###### Proof.

We may assume that ∅ ∈ 𝒜 \emptyset\in\mathcal{A}. Let us choose S ⊆ U ⁡ ( 𝒜) S\subseteq U(\mathcal{A}) minimal such that every non-empty set of 𝒜 \mathcal{A} intersects S S. Then for every x ∈ S x\in S there is a A ∈ 𝒜 A\in\mathcal{A} with A ∩ S = { x } A\cap S=\{x\}; otherwise S − x S-x would still meet every non-empty A ∈ 𝒜 A\in\mathcal{A}, which contradicts the minimality of S S. As 𝒜 \mathcal{A} is union-closed it follows that { A ∩ S: A ∈ 𝒜 } = 2 S \{A\cap S:A\in\mathcal{A}\}=2^{S}. Hence n ≥ 2 | S | n\geq 2^{|S|} and so | S | ≤ log 2 ⁡ ( n) |S|\leq\log_{2}(n). As every of the n − 1 n-1 non-empty member-sets of 𝒜 \mathcal{A} intersects S S, there is an element in S S that belongs to at least ( n − 1) / log 2 ⁡ ( n) (n-1)/\log_{2}(n) many member-sets of 𝒜 \mathcal{A}. ∎

Wójcik [72] improved the bound to 2.4 ​ n log 2 ⁡ n \frac{2.4n}{\log_{2}{n}} for large n n. His proof is not trivial, but the result is still far from Frankl’s conjecture.

Here are two observations that could be interpreted as signs that the conjecture is, after all, perhaps not as hard as thought: normally the most frequent element appears more often than needed, and there are several abundant elements. Indeed, the powerful averaging technique discussed in Section 6 builds solely on these facts.

These observations are due to Poonen, who also found exceptions to them. Power sets are an obvious example for families in which the maximum frequency is exactly half the size of the family. Poonen conjectured that, among separating families, these are the only ones.

###### Conjecture 14 (Poonen [50]).

Let 𝒜 \mathcal{A} be a separating union-closed family. Unless 𝒜 \mathcal{A} is a power set, it contains an element that appears in strictly more than half of the member-sets of 𝒜 \mathcal{A}.

A similar conjecture was offered by Renaud [53]. Moreover, Poonen described families with a unique abundant element and again conjectured that these are the only ones:

###### Conjecture 15 (Poonen [50]).

Let 𝒜 \mathcal{A} be a separating union-closed family on universe U U. If 𝒜 \mathcal{A} contains a unique abundant element a a then

 | 𝒜 = { ∅ } ∪ { B + a: B ⊆ U − a }. \mathcal{A}=\{\emptyset\}\cup\{B+a:B\subseteq U-a\}. |  |

If these conjectures are to be believed, then there is a bit of a margin when attacking the union-closed sets conjecture. So, why then has the conjecture withstood more than twenty years of proof attempts?

The obvious first approach is to try an induction, for instance on the number of member-sets. If, given a union-closed family, we could delete one (or two) basis sets so that the maximum frequency drops then, by induction, the original family would satisfy the conjecture, too. Unfortunately, this is not always possible: in a power set of sufficient size, deleting one or two basis sets will never reduce the maximum frequency.

So, naive induction will not succeed. Often, induction can only be made to work if the hypothesis is strengthened, usually by exploiting some structural insight. However, we feel that we are lacking in just that. We do not know what the extremal families look like, those that have minimal maximum frequency among all union-closed families of a given size. So far, there are not even any good candidates. We will continue this discussion in Section 8.

A second reason why the conjecture has resisted so long lies in the weakness of the techniques at our disposal. Let us briefly review the main techniques used to prove that a given family satisfies the conjecture: *injections*, *local configurations*and *averaging*. In averaging we try to show that the average frequency is large enough so that some element must be abundant. Averaging is very powerful but has the drawback that there are families for which the average is simply too low for the method to work. We discuss averaging and its limits in Section 6. For the local configurations method one strives to identify small families so that any large union-closed family containing the small one will automatically satisfy the conjecture. Unfortunately, given what we know at the moment it seems doubtful that we will be able to show that any union-closed family always contains such a local configuration. We will have a closer look at local configurations in the next section.

That leaves injections, the simplest of the three techniques. For an almost trivial example, consider the case when a union-closed family 𝒜 \mathcal{A} contains a singleton, that is, there is an element x x so that { x } ∈ 𝒜 \{x\}\in\mathcal{A}. Then

 | 𝒜 x ¯ → 𝒜 x, A ↦ A + x \mathcal{A}_{\overline{x}}\to\mathcal{A}_{x},\,A\mapsto A+x |  |

defines an injection, which clearly implies that 2 ​ | 𝒜 x | ≥ | 𝒜 x | + | 𝒜 x ¯ | = | 𝒜 | 2|\mathcal{A}_{x}|\geq|\mathcal{A}_{x}|+|\mathcal{A}_{\overline{x}}|=|\mathcal{A}|. Consequently, x x is abundant. In fact, we have used this method already twice: once for lower semimodular lattices and then for chordal bipartite graphs. The main problem with the injection method is that we need to first identify an element that is likely to be abundant.

Sarvate and Renaud [62] were probably the first to observe (in print) that a singleton is always abundant. In a similar way, one of the two elements of any 2 2 -set is abundant. The pattern, however, breaks with 3 3 -sets. Renaud and Sarvate [63] describe a family with a unique smallest member-set of 3 3 elements, none of which is abundant. Poonen [50] constructs a similar family, a generalisation of which we present here:

For each k ≥ 3 k\geq 3 we define a union-closed family 𝒜 k \mathcal{A}^{k} with the property that [k] [k] is the unique smallest set, but no element of [k] [k] is abundant. For this, we use Poonen’s notation 𝒜 ⊎ ℬ \mathcal{A}\uplus\mathcal{B} for two set families 𝒜 \mathcal{A} and ℬ \mathcal{B} to denote the family

 | 𝒜 ⊎ ℬ:= { S ∪ T: S ∈ 𝒜, T ∈ ℬ }. \mathcal{A}\uplus\mathcal{B}:=\{S\cup T:S\in\mathcal{A},\,T\in\mathcal{B}\}. |  |

Now let

 | 𝒜 k = { [k] } ∪ ⋃ i = 1 k ( { ∅, { i }, [k] } ⊎ ℬ i) ∪ ( 2 [k] ⊎ [k + 1, 3 ​ k]), \displaystyle\mathcal{A}^{k}=\{[k]\}\cup\bigcup_{i=1}^{k}(\{\emptyset,\{i\},[k]\}\uplus\mathcal{B}^{i})\cup(2^{[k]}\uplus[k+1,3k]), |  |

where

 | ℬ i = { [k + 1, 3 ​ k] ∖ { 2 ​ i + 2 }, [k + 1, 3 ​ k] ∖ { 2 ​ i + 3 } } ​ for every ​ i ∈ [k]. \mathcal{B}^{i}=\{[k+1,3k]\setminus\{2i+2\},[k+1,3k]\setminus\{2i+3\}\}\text{ for every }i\in[k]. |  |

Note that the set [k] [k] is the unique smallest set in 𝒜 \mathcal{A}. In total, 𝒜 k \mathcal{A}^{k} contains 1 + 6 ​ k + 2 k 1+6k+2^{k} many sets, but every i ∈ [k] i\in[k] is contained in exactly 1 + ( 2 ​ k + 2) + 2 k − 1 1+(2k+2)+2^{k-1} sets of 𝒜 \mathcal{A}. Therefore, no element of [k] [k] is abundant.

Poonen’s family highlights one of the major obstacles on the way to a proof of the union-closed sets conjecture: we do not know where to expect an abundant element. However, there are special cases where this is known. We treat these cases next.

## 5 Local configurations

Sarvate and Renaud [62] observed that any singleton in a union-closed family is abundant, and of the two elements of a 2 2 -set at least one is abundant. This motivates the search for good *local configurations*: a family ℒ \mathcal{L} on few elements so that any union-closed family 𝒜 \mathcal{A} containing ℒ \mathcal{L} has an abundant element among the elements of ℒ \mathcal{L}. Poonen [50] gives a complete characterisation of such families:

###### Theorem 16 (Poonen [50]).

Let ℒ \mathcal{L} be a union-closed family with universe [k] [k]. The following statements are equivalent:

1. (i)

Every union-closed family 𝒜 \mathcal{A} containing ℒ \mathcal{L} satisfies the union-closed sets conjecture. In particular, 𝒜 \mathcal{A} has an abundant element in [k] [k].

2. (ii)

There are reals c 1, c 2, …, c k ≥ 0 c_{1},c_{2},\ldots,c_{k}\geq 0 with ∑ i = 1 k c i = 1 \sum_{i=1}^{k}c_{i}=1 such that for every union-closed family 𝒦 ⊆ 2 [k] \mathcal{K}\subseteq 2^{[k]} with 𝒦 = ℒ ⊎ 𝒦 \mathcal{K}=\mathcal{L}\uplus\mathcal{K} it holds that

 | ∑ i = 1 k c i ​ | 𝒦 i | ≥ 1 2 ​ | 𝒦 |. \sum_{i=1}^{k}c_{i}|\mathcal{K}_{i}|\geq\tfrac{1}{2}|\mathcal{K}|. |  |

We stress that (ii) is indeed a local condition: for fixed k k there are only finitely many such families 𝒦 \mathcal{K}. As an application of his theorem, Poonen showed that the union-closed family consisting of a 4 4 -set together with any three distinct 3 3 -subsets satisfies the conditions of his theorem. This was later generalised by Vaughan [67] to three distinct 3 3 -sets with a non-empty common intersection. As mentioned in Section 3.4, Vaughan’s result is used to prove Frankl’s conjecture for subcubic bipartite graphs.

A union-closed family ℒ \mathcal{L} as in Theorem 16 is called *Frankl-complete*by Vaughan [66], *FC*for short. Several FC-families are listed in [66], for example a 5 5 -set together with all its 4 4 -subsets or a 6 6 -set with all 5 5 -subsets and eight 4 4 -subsets. The list was later extended by Morris [46], who, in particular, completely characterised the FC-families on at most 5 5 elements.

To study FC-families in a more quantitative way, Morris [46] introduced the function FC ​ ( k, m) \mbox{FC}(k,m) defined as the smallest r r for which the set of every r r of the k k -sets in [m] [m] generates an FC-family. He showed that ⌊ m 2 ⌋ + 1 ≤ FC ​ ( 3, m) \lfloor\tfrac{m}{2}\rfloor+1\leq\mbox{FC}(3,m), while Vaughan [67] gave an upper bound of FC ​ ( 3, m) ≤ 2 ​ m 3 \mbox{FC}(3,m)\leq\tfrac{2m}{3}. A proof of Morris’ conjecture that FC ​ ( 3, m) = ⌊ m 2 ⌋ + 1 \mbox{FC}(3,m)=\lfloor\tfrac{m}{2}\rfloor+1 was announced by Vaughan [65], but has apparently never been published.

Marić, Živković and Vučković [44] verified some known FC-families and found a new one using the automatic proof assistant Isabelle/HOL. For this, they formalised the condition of FC-families to enable a computer search. As a result, we know now that all families containing four 3 3 -subsets of a 7 7 -set are FC-families.

### 5.1 Small finite families

The union-closed sets conjecture has been verified for families on few member-sets or few elements. The current best results use local configurations to reduce the number of special cases substantially.

With respect to the size of the universe, the conjecture has to-date been verified up to m = 12 m=12:

###### Theorem 17 (Živković and Vučković [68]).

The union-closed sets conjecture holds for union-closed families on at most 12 12 elements.

The following result, that has not been improved upon in the last twenty years, allows to leverage bounds on the universe size to bounds on the number of member-sets:

###### Lemma 18 (Lo Faro [22]).

Under the assumption that the union-closed sets conjecture fails, let m m denote the minimum cardinality of | U ⁡ ( 𝒜) | |U(\mathcal{A})| taken over all counterexamples 𝒜 \mathcal{A} to the union-closed sets conjecture. Then any counterexample has at least 4 ​ m − 1 4m-1 member-sets.

The lemma was later rediscovered by Roberts and Simpson [58]. Together with Theorem 17 we obtain:

###### Corollary 19.

The union-closed sets conjecture holds for union-closed families with at most 50 sets.

Various authors verified the conjecture for small values of n n and m m, where as usual n n is the number of member-sets and m m the size of the universe. The first were Sarvate and Renaud [62] who treated a close variant that excludes the empty set. In a first paper they covered all cases up to n ≤ 11 n\leq 11; in Sarvate and Renaud [63] the case analysis was pushed up to n ≤ 19 n\leq 19. Using his Theorem 16, Poonen improved the bounds to m ≤ 7 m\leq 7 and n ≤ 28 n\leq 28. This was followed by Lo Faro [22], who settled the union-closed sets conjecture for m ≤ 9 m\leq 9 and n ≤ 36 n\leq 36. For this, he investigated several necessary conditions on a minimal counterexample, among them Lemma 18 above. Roberts [57] shows the conjecture up to n ≤ 40 n\leq 40.

Using the list of known FC-families, Morris [46] proved the union-closed sets conjecture for families with m ≤ 9 m\leq 9 and n ≤ 36 n\leq 36, apparently unaware of the older result by Lo Faro [22]. Nevertheless, there is merit in Morris’ proof as it showcases how FC-families may be used to substantially reduce the number of cases. This method is at the heart of all subsequent work in this direction.

In order to prove the conjecture for m ≤ 10 m\leq 10, Marković [45] imitated the method of Theorem 16: he assigns non-negative weights to the elements of 𝒜 \mathcal{A} and extends this to the member-sets of 𝒜 \mathcal{A}. He then observes that a total weight of the member-sets of at least 1 2 ​ n \tfrac{1}{2}n times the weight of the universe is sufficient for the union-closed sets conjecture. As a by-product of this method, Marković discovered a number of new FC-families.

Bošnjak and Marković [10] improve upon [45] by developing more general local configurations that allow them to verify the conjecture up to m = 11 m=11. With a very similar method and the use of a computer, Živković and Vučković [68] pushed this to m ≤ 12 m\leq 12.

## 6 Averaging

Obviously, a union-closed family 𝒜 \mathcal{A} has an element of frequency ≥ 1 2 ​ | 𝒜 | \geq\tfrac{1}{2}|\mathcal{A}| if the *average frequency*is at least 1 2 ​ | 𝒜 | \tfrac{1}{2}|\mathcal{A}|. In other words, if

 | 1 | U ⁡ ( 𝒜) | ⋅ ∑ u ∈ U ⁡ ( 𝒜) | 𝒜 u | ≥ 1 2 ​ | 𝒜 |, \frac{1}{|U(\mathcal{A})|}\cdot\sum_{u\in U(\mathcal{A})}|\mathcal{A}_{u}|\geq\frac{1}{2}|\mathcal{A}|, |  | (3) |

then 𝒜 \mathcal{A} satisfies the union-closed sets conjecture.

So far, not much is gained. Calculating ∑ u ∈ U ⁡ ( 𝒜) | 𝒜 u | \sum_{u\in U(\mathcal{A})}|\mathcal{A}_{u}| directly is clearly out of question, as this would presuppose knowledge about the individual frequencies | 𝒜 u | |\mathcal{A}_{u}|. Fortunately, this is not necessary, as the sum of frequencies can be determined indirectly with a simple double-counting argument:

 | ∑ u ∈ U ⁡ ( 𝒜) | 𝒜 u | = ∑ A ∈ 𝒜 | A |. \sum_{u\in U(\mathcal{A})}|\mathcal{A}_{u}|=\sum_{A\in\mathcal{A}}|A|. |  | (4) |

This identity is the heart of the averaging method. The total set size is usually much easier to control, and in some cases may be estimated quite well.

Combining ( 3) and ( 4), a condition equivalent to ( 3) is that

 | 1 | 𝒜 | ⋅ ∑ A ∈ 𝒜 | A | ≥ 1 2 ​ | U ⁡ ( 𝒜) |. \frac{1}{|\mathcal{A}|}\cdot\sum_{A\in\mathcal{A}}|A|\geq\frac{1}{2}|U(\mathcal{A})|. |  |

That is, if the *average set size*of 𝒜 \mathcal{A} is at least half the size of the universe then 𝒜 \mathcal{A} again satisfies the union-closed sets conjecture.

As discussed in Section 4, it is not obvious where to look for an abundant element. The averaging method has the clear advantage that it simply sidesteps this obstacle. In this section we describe how both ( 3) and ( 4) lead to some of the strongest results on the union-closed sets conjecture.

### 6.1 Large families

In a clearly overlooked paper, Nishimura and Takahashi [47] prove for the first time that the union-closed sets conjecture always holds for large families. Their proof uses the average set size argument: it is shown that the average set size is greater than m 2 \tfrac{m}{2}, which implies that there is an abundant element.

###### Theorem 20 (Nishimura and Takahashi [47]).

Let 𝒜 \mathcal{A} be a union-closed family of more than 2 m − 1 2 ​ 2 m 2^{m}-\tfrac{1}{2}\sqrt{2^{m}} member-sets on a universe of size m m. Then 𝒜 \mathcal{A} satisfies the union-closed sets conjecture.

###### Proof.

Suppose there is a set S ⊆ U ⁡ ( 𝒜) S\subseteq U(\mathcal{A}) with S ∉ 𝒜 S\notin\mathcal{A} but | S | ≥ m 2 |S|\geq\frac{m}{2}. Then for any subset R ⊆ S R\subseteq S with R ∈ 𝒜 R\in\mathcal{A} it holds that S ∖ R ∉ 𝒜 S\setminus R\notin\mathcal{A}. Thus, at least half of the subsets of S S are missing in 𝒜 \mathcal{A}. This gives | 𝒜 | ≤ 2 m − 1 2 ⋅ 2 m 2 |\mathcal{A}|\leq 2^{m}-\frac{1}{2}\cdot 2^{\frac{m}{2}}, a contradiction. Hence, every set S ⊆ U ⁡ ( 𝒜) S\subseteq U(\mathcal{A}) of size at least m 2 \tfrac{m}{2} is contained in 𝒜 \mathcal{A}. This means that the average set size is at least m 2 \tfrac{m}{2}, finishing the proof. ∎

Czédli [13] employed some involved lattice-theoretic arguments to push the bound from 2 m − 1 2 ​ 2 m 2^{m}-\tfrac{1}{2}\sqrt{2^{m}} to 2 m − 2 m 2^{m}-\sqrt{2^{m}}. A weaker result than Nishimura and Takahashi’s was proved by Gao and Yu [27]. Recently, a serious improvement of the above bound was given by Balla, Bollobás and Eccles [9], which we present in Section 6.4.

### 6.2 Bounds on the average

Averaging does not always work. It is easy to construct union closed families with an average frequency and average set size that is too low to deduce the union-closed sets conjecture. Reimer [51] gave a bound on the average set size that is in some respect best possible.

###### Theorem 21 (Reimer [51]).

Let 𝒜 \mathcal{A} be a union-closed family on n n sets. Then

 | 1 n ⋅ ∑ A ∈ 𝒜 | A | ≥ log 2 ⁡ n 2. \frac{1}{n}\cdot\sum_{A\in\mathcal{A}}|A|\geq\frac{\log_{2}n}{2}. |  | (5) |

The result is too weak for Frankl’s conjecture as usually log 2 ⁡ ( n) < m \log_{2}(n)<m. In terms of the average frequency, Reimer’s bound reads as

 | 1 m ⋅ ∑ u ∈ U ⁡ ( 𝒜) | 𝒜 u | ≥ log 2 ⁡ n m ⋅ n 2. \frac{1}{m}\cdot\sum_{u\in U(\mathcal{A})}|\mathcal{A}_{u}|\geq\frac{\log_{2}n}{m}\cdot\frac{n}{2}. |  | (6) |

We discuss the beautiful proof of Theorem 21 in Section 6.4.

We now focus on separating union-closed families, where for every two elements there is a set containing exactly one of them. As explained in Section 2, for the purpose of the union-closed sets conjecture it is not a restriction to consider only separating families.

###### Theorem 22 (Falgas-Ravry [20]).

Let 𝒜 \mathcal{A} be a separating union-closed family on m m elements. Then

 | 1 m ⋅ ∑ u ∈ U ⁡ ( 𝒜) | 𝒜 u | ≥ m + 1 2. \frac{1}{m}\cdot\sum_{u\in U(\mathcal{A})}|\mathcal{A}_{u}|\geq\frac{m+1}{2}. |  | (7) |

He remarks that this bound is stronger than Reimer’s bound if m > n ​ log 2 ​ n m>\sqrt{n\log_{2}n}. The proof of ( 7) is rather simple:

###### Proof.

Assume that the elements 1, 2, …, m 1,2,\ldots,m of U ⁡ ( 𝒜) U(\mathcal{A}) are labelled in order of increasing frequency. As 𝒜 \mathcal{A} is separating, this ordering ensures that for any 1 ≤ i < j ≤ m 1\leq i<j\leq m there is a set X i ​ j ∈ 𝒜 X_{ij}\in\mathcal{A} such that i ∉ X i ​ j i\notin X_{ij} and j ∈ X i ​ j j\in X_{ij}. For all 1 ≤ i ≤ m − 1 1\leq i\leq m-1 let X i = ⋃ j = i + 1 m X i ​ j X_{i}=\bigcup_{j=i+1}^{m}X_{ij}, and put X 0:= U ⁡ ( 𝒜) X_{0}:=U(\mathcal{A}). Observe that (a) the X i X_{i} are all distinct and that (b) [i + 1, m] ⊆ X i [i+1,m]\subseteq X_{i}. Thus, the statement follows from

 | ∑ u ∈ U ⁡ ( 𝒜) | 𝒜 u | ≥ ( a) ∑ i = 0 m − 1 | X i | ≥ ( b) ∑ i = 0 m − 1 ( m − i) = m ⁡ ( m + 1) 2. \sum_{u\in U(\mathcal{A})}|\mathcal{A}_{u}|\stackrel{{\scriptstyle(a)}}{{\geq}}\sum_{i=0}^{m-1}|X_{i}|\stackrel{{\scriptstyle(b)}}{{\geq}}\sum_{i=0}^{m-1}(m-i)=\frac{m(m+1)}{2}. |  |

∎

Let us point out an easy consequence of the proof. As Nishimura and Takahashi observed, the union-closed sets conjecture holds for families that are very large with respect to their universe. Here we obtain the analogous result for very *small*families:

###### Theorem 23.

Any separating family on m m elements with at most 2 ​ m 2m member-sets satisfies the union-closed sets conjecture.

###### Proof.

Each of the m m sets X i X_{i} as constructed above contains the most frequent element x m x_{m}. ∎

We note that this is a weaker bound than the one obtained by Lo Faro for a minimal counterexample (Lemma 18): n ≤ 4 ​ m − 1 n\leq 4m-1. However, Lo Faro’s techniques do not extend easily to small families and there is a good reason for this. If the factor in Theorem 23 can be improved to c > 2 c>2 then we may deduce that there is always an element whose frequency is a constant fraction of the number of member-sets. This natural weakening of the union-closed sets conjecture is still very much open.

###### Theorem 24 (Hu [31]).

Suppose there is a c > 2 c>2 so that any separating union-closed family 𝒜 ′ \mathcal{A}^{\prime} with | 𝒜 ′ | ≤ c ​ | U ⁡ ( 𝒜 ′) | |\mathcal{A}^{\prime}|\leq c|U(\mathcal{A}^{\prime})| satisfies the union-closed sets conjecture. Then, for every union-closed family 𝒜 \mathcal{A}, there is an element u u of frequency

 | | 𝒜 u | ≥ c − 2 2 ​ ( c − 1) ​ | 𝒜 |. |\mathcal{A}_{u}|\geq\frac{c-2}{2(c-1)}|\mathcal{A}|. |  |

The theorem is proved along the following lines: by cloning some element, the universe U U of 𝒜 \mathcal{A} is enlarged to U ′ U^{\prime}. At the same time, we add sets of the form U ′ − x U^{\prime}-x in order to separate the clones from each other. The resulting family 𝒜 ′ \mathcal{A}^{\prime} is then separating and will be made to have size | 𝒜 ′ | ≤ c ​ | U ′ | |\mathcal{A}^{\prime}|\leq c|U^{\prime}|. Now an element of frequency ≥ 1 2 ​ | 𝒜 ′ | \geq\tfrac{1}{2}|\mathcal{A}^{\prime}| will still have high frequency in 𝒜 \mathcal{A}.

Falgas-Ravry also gives a family of separating union-closed families which shows that the combination of the bounds ( 5) and ( 7) is close to optimal, in the sense that the sum of both bounds can serve as an upper bound on the minimum possible weight of a separable union-closed family. For this, he calls a pair ( m, n) (m,n)*satisfiable*if there is a separating union-closed family with n n sets on a universe of m m elements.

###### Theorem 25 (Falgas-Ravry [20] and Reimer [51]).

Let ( m, n) (m,n) be a satisfiable pair of integers. Let 𝒜 \mathcal{A} be a union-closed family on m m elements and n n sets of minimal average frequency. Then

 | max ⁡ ( n ​ log 2 ​ n 2 ​ m, m + 1 2) ≤ 1 m ⋅ ∑ u ∈ U ⁡ ( 𝒜) | 𝒜 u | ≤ n ​ log 2 ​ n 2 ​ m + m + 1 2 + n m. \max\left(\frac{n\log_{2}n}{2m},\frac{m+1}{2}\right)\leq\frac{1}{m}\cdot\sum_{u\in U(\mathcal{A})}|\mathcal{A}_{u}|\leq\frac{n\log_{2}n}{2m}+\frac{m+1}{2}+\frac{n}{m}. |  | (8) |

To establish the upper bound in Theorem 25, Falgas-Ravry uses a construction not unlike that of Duffus and Sands [18] that we discuss below.

### 6.3 Limits of averaging

In the framework of the lattice formulation, Czédli, Maróti and Schmidt [14] construct for every size m m of the universe a family of ⌊ 2 3 ​ 2 m ⌋ \lfloor\tfrac{2}{3}2^{m}\rfloor members, for which averaging fails. We present here a lattice-free version of their family and a short and elementary proof that the average is always too small.

On the set ℕ < ω \mathbb{N}^{<\omega} of finite subsets of the positive integers, let < < be the order defined by first sorting by increasing largest element and then by reverse colex order. In other words, we set A < B A<B if

- •

max ⁡ A < max ⁡ B \max A<\max B; or

- •

max ⁡ A = max ⁡ B \max A=\max B but max ⁡ ( A ​ Δ ​ B) ∈ A \max(A\Delta B)\in A

for finite A, B ⊆ ℕ A,B\subseteq\mathbb{N}.

As an illustration, here is the initial segment of the order, where we write 124 124 for the set { 1, 2, 4 } \{1,2,4\}:

 | ∅ < 1 < 12 < 2 < 123 < 23 < 13 < 3 < 1234 < 234 \displaystyle\emptyset<1<12<2<123<23<13<3<1234<234 |  |  |

 | < 134 < 34 < 124 < 24 < 14 < 4 < 12345 < … \displaystyle<134<34<124<24<14<4<12345<... |  |

For any positive integer n n, define the *Hungarian family ℋ ( n) \mathcal{H}^{(n)}*to be the inital segment of length n n of ℕ < ω \mathbb{N}^{<\omega} under < <. It is easy to check that ℋ ( n) \mathcal{H}^{(n)} is union-closed and that its universe is [⌈ log 2 ⁡ n ⌉] [\lceil\log_{2}n\rceil].

###### Theorem 26 (Czédli, Maróti and Schmidt).

For the Hungarian family on [m] [m] of size n = ⌊ 2 3 ​ 2 m ⌋ n=\lfloor\tfrac{2}{3}2^{m}\rfloor

 | 1 m ⋅ ∑ i ∈ [m] | ℋ i ( n) | < | ℋ ( n) | 2. \frac{1}{m}\cdot\sum_{i\in[m]}|\mathcal{H}^{(n)}_{i}|<\frac{|\mathcal{H}^{(n)}|}{2}. |  |

for any m > 1 m>1.

###### Proof.

The key to the proof are the simple and well-known identities

 | ⌊ 2 3 ​ 2 m ⌋ \displaystyle\lfloor\tfrac{2}{3}2^{m}\rfloor | = 2 m + 1 − 1 3 = 2 m − 1 + 2 m − 3 + … + 4 + 1 ​ if m odd. \displaystyle=\frac{2^{m+1}-1}{3}=2^{m-1}+2^{m-3}+\ldots+4+1\text{ if $m$ odd.} |  | (9) |

 | ⌊ 2 3 ​ 2 m ⌋ \displaystyle\lfloor\tfrac{2}{3}2^{m}\rfloor | = 2 m + 1 − 2 3 = 2 m − 1 + 2 m − 3 + … + 8 + 2 ​ if m even. \displaystyle=\frac{2^{m+1}-2}{3}=2^{m-1}+2^{m-3}+\ldots+8+2\text{ if $m$ even.} |  | (10) |

Put k = ⌊ m − 1 2 ⌋ k=\lfloor\tfrac{m-1}{2}\rfloor. Denote by I 0 I_{0} the initial segment of ℕ < ω \mathbb{N}^{<\omega} of length 2 m − 1 2^{m-1}, by I 1 I_{1} the set of the next 2 m − 3 2^{m-3} sets in the order, by I 2 I_{2} the following 2 m − 5 2^{m-5} sets and so on until we reach I k I_{k}.

Clearly, | I i | = 2 m − ( 2 ​ i + 1) |I_{i}|=2^{m-(2i+1)} and ℋ ( n) = I 0 ∪ I 1 ∪ … ∪ I k. \mathcal{H}^{(n)}=I_{0}\cup I_{1}\cup\ldots\cup I_{k}. Moreover, we can see that I 0 = 2 [m − 1] I_{0}=2^{[m-1]} and that for i ≥ 1 i\geq 1, the set I i I_{i} is the set of all X ⊆ [m] X\subseteq[m] that contain all of m − 1, m − 3, …, m − ( 2 ​ i − 1) m-1,m-3,\ldots,m-(2i-1) and of m, m − 2 ​ i m,m-2i, but none of m − 2, m − 4, …, m − ( 2 ​ i − 2) m-2,m-4,\ldots,m-(2i-2).

Thus, an element m − ( 2 ​ i − 1) m-(2i-1) appears in half of the members of I 0 ∪ … ∪ I i − 1 I_{0}\cup\ldots\cup I_{i-1} and in all of the sets in I i ∪ … ∪ I k I_{i}\cup\ldots\cup I_{k}. Its frequency is therefore

 | | ℋ m − ( 2 ​ i − 1) ( n) | = 1 2 ​ ( | I 0 | + … + | I i − 1 |) + | I i | + … + | I k |. |\mathcal{H}^{(n)}_{m-(2i-1)}|=\tfrac{1}{2}\left(|I_{0}|+\ldots+|I_{i-1}|\right)+|I_{i}|+\ldots+|I_{k}|. |  | (11) |

An element m − 2 ​ i m-2i is contained in half of the sets of I 0 ∪ … ∪ I i − 1 I_{0}\cup\ldots\cup I_{i-1}, in all of the sets in I i I_{i} but in none of I i + 1 ∪ … ∪ I k I_{i+1}\cup\ldots\cup I_{k}. Its frequency is

 | | ℋ m − 2 ​ i ( n) | = 1 2 ​ ( | I 0 | + … + | I i − 1 |) + | I i |. |\mathcal{H}^{(n)}_{m-2i}|=\tfrac{1}{2}\left(|I_{0}|+\ldots+|I_{i-1}|\right)+|I_{i}|. |  | (12) |

Moreover, we observe that m m lies in all of sets of ℋ ( n) \mathcal{H}^{(n)} but those in I 0 I_{0}.

For the final argument, we assume m m to be even, that is m = 2 ​ k + 2 m=2k+2. The case of odd m m is very similar. With ( 11) and ( 12), we obtain

 | ∑ j = 1 m | ℋ j ( n) | \displaystyle\sum_{j=1}^{m}|\mathcal{H}^{(n)}_{j}| | = | ℋ m ( n) | + ∑ i = 1 k ( | ℋ m − ( 2 ​ i − 1) ( n) | + | ℋ m − 2 ​ i ( n) |) + | ℋ 1 ( n) | \displaystyle=|\mathcal{H}^{(n)}_{m}|+\sum_{i=1}^{k}\left(|\mathcal{H}^{(n)}_{m-(2i-1)}|+|\mathcal{H}^{(n)}_{m-2i}|\right)+|\mathcal{H}^{(n)}_{1}| |  |

 |  | = | ℋ ( n) | − | I 0 | + ∑ i = 1 k ( | ℋ ( n) | + | I i |) + 1 2 ​ | ℋ ( n) | \displaystyle=|\mathcal{H}^{(n)}|-|I_{0}|+\sum_{i=1}^{k}\left(|\mathcal{H}^{(n)}|+|I_{i}|\right)+\frac{1}{2}|\mathcal{H}^{(n)}| |  |

 |  | = ( k + 1) ​ | ℋ ( n) | − 2 ​ | I 0 | + 3 2 ​ | ℋ ( n) | \displaystyle=(k+1)|\mathcal{H}^{(n)}|-2|I_{0}|+\frac{3}{2}|\mathcal{H}^{(n)}| |  |

 |  | = m 2 ​ | ℋ ( n) | − 2 m + 3 2 ⋅ 2 m + 1 − 2 3 = m 2 ​ | ℋ ( n) | − 1, \displaystyle=\frac{m}{2}|\mathcal{H}^{(n)}|-2^{m}+\frac{3}{2}\cdot\frac{2^{m+1}-2}{3}=\frac{m}{2}|\mathcal{H}^{(n)}|-1, |  |

where we used ( 10) in the penultimate step. ∎

So, the averaging method can never yield the union-closed sets conjecture in its full generality. Might it perhaps be possible to at least obtain the natural relaxation, in which we only ask for an element that appears in ≥ 1 % \geq 1\% of the member-sets? As Duffus and Sands [18] observed, not even this more modest aim may be attained just by averaging. We present here their construction.

Let V V be a set of size 2 ​ t 2t, and W = { w 1, …, w 2 t } W=\{w_{1},\ldots,w_{2^{t}}\} be a disjoint set of 2 t 2^{t} elements. Put

 | 𝒜 = 2 V ∪ { V ∪ { w 1, …, w i }: i = 1 …, 2 t }. \mathcal{A}=2^{V}\cup\{V\cup\{w_{1},\ldots,w_{i}\}:i=1\ldots,2^{t}\}. |  |

Then 𝒜 \mathcal{A} is a (separating) union-closed family of size | 𝒜 | = 2 2 ​ t + 2 t |\mathcal{A}|=2^{2t}+2^{t} on a universe U = V ∪ W U=V\cup W of size 2 ​ t + 2 t 2t+2^{t}. Averaging yields

 | 1 | U | ⋅ ∑ u ∈ U | 𝒜 u | | 𝒜 | \displaystyle\frac{1}{|U|}\cdot\sum_{u\in U}\frac{|\mathcal{A}_{u}|}{|\mathcal{A}|} | = 2 ​ t ​ ( 2 2 ​ t − 1 + 2 t) + ∑ i = 1 2 t ( 2 t − i + 1) ( 2 ​ t + 2 t) ​ ( 2 2 ​ t + 2 t) \displaystyle=\frac{2t(2^{2t-1}+2^{t})+\sum_{i=1}^{2^{t}}(2^{t}-i+1)}{(2t+2^{t})(2^{2t}+2^{t})} |  |

 |  | = 2 ​ t ​ ( 2 2 ​ t − 1 + 2 t) + 2 t − 1 ​ ( 2 t − 1) ( 2 ​ t + 2 t) ​ ( 2 2 ​ t + 2 t) → 0 ​ as ​ t → ∞, \displaystyle=\frac{2t(2^{2t-1}+2^{t})+2^{t-1}(2^{t}-1)}{(2t+2^{t})(2^{2t}+2^{t})}\to 0\text{ as }t\to\infty, |  |

as the largest summand in the numerator is t ​ 2 2 ​ t t2^{2t}, while the largest one in the denominator is 2 3 ​ t 2^{3t}. This shows that an averaging argument cannot always guarantee an element of frequency at least c ​ | 𝒜 | c|\mathcal{A}| for any c > 0 c>0.

### 6.4 Up-compression

We now outline Reimer’s proof of Theorem 21 because it uses a common technique in extremal combinatorics: shifting or compression. We first restate the theorem.

###### Theorem 21 (Reimer [51]).

Let 𝒜 \mathcal{A} be a union-closed family on n n sets. Then

 | 1 n ⋅ ∑ A ∈ 𝒜 | A | ≥ log 2 ⁡ n 2. \frac{1}{n}\cdot\sum_{A\in\mathcal{A}}|A|\geq\frac{\log_{2}n}{2}. |  |

Compression subjects the given initial object (the union-closed family), to small incremental changes until a simpler object is reached (an up-set), while maintaining the essential properties of the initial object. Variants of compression have been used by Frankl in order to prove the Kruskal-Katona theorem [25] and in the context of traces of finite sets [24]. The technique is also used by Alon [5] and various others; see Kalai’s blog post [35] for an enlightening discussion.

Returning to Reimer’s proof we define the *up-compression*of a union-closed family 𝒜 \mathcal{A}. For this, consider an element i i, and define

 | u i ​ ( A) = { A + i if A + i ∉ 𝒜 A otherwise, u_{i}(A)=\begin{cases}A+i&\text{ if $A+i\notin\mathcal{A}$}\\ A&\text{ otherwise},\end{cases} |  |

for every A ∈ 𝒜 A\in\mathcal{A}. Then it turns out that the up-compressed family u i ​ ( 𝒜):= { u i ​ ( A): A ∈ 𝒜 } u_{i}(\mathcal{A}):=\{u_{i}(A):A\in\mathcal{A}\} is still union-closed. Moreover, iteratively applying up-compression for every element i i in the universe of 𝒜 \mathcal{A} results in an *up-set*: a family 𝒰 \mathcal{U} on universe U U for which X ∈ U X\in U and X ⊆ Y ⊆ U X\subseteq Y\subseteq U implies Y ∈ 𝒰 Y\in\mathcal{U}. We may always assume 𝒜 \mathcal{A} to have universe [m] [m]. We then write u ⁡ ( 𝒜) u(\mathcal{A}) for the iterated up-compression u m ∘ … ∘ u 1 ​ ( 𝒜) u_{m}\circ\ldots\circ u_{1}(\mathcal{A}).

###### Lemma 27 (Reimer [51]).

Let 𝒜 \mathcal{A} be a union-closed family on universe U U. Then

1. (i)

u i ​ ( 𝒜) u_{i}(\mathcal{A}) is union-closed for any i ∈ U i\in U; and

2. (ii)

u ⁡ ( 𝒜) u(\mathcal{A}) is an up-set.

What have we gained? The key to the averaging technique is to control the total set size ∑ A ∈ 𝒜 | A | \sum_{A\in\mathcal{A}}|A|. For an up-set the total set size can be given in a closed form. Define the *edge boundary*of an up-set 𝒰 \mathcal{U} on a universe U U to be

 | E B ( 𝒰) = { ( A, A + i): A ∉ 𝒰, i ∈ U and A + i ∈ 𝒰 }. EB(\mathcal{U})=\{(A,A+i):A\notin\mathcal{U},\,i\in U\text{ and }A+i\in\mathcal{U}\}. |  |

Now

###### Lemma 28 (Reimer [51]).

Let 𝒰 \mathcal{U} be an up-set on m m elements. Then

 | 2 ​ ∑ A ∈ 𝒰 | A | = m ​ | 𝒰 | + | E ​ B ​ ( 𝒰) |. 2\sum_{A\in\mathcal{U}}|A|=m|\mathcal{U}|+|EB(\mathcal{U})|. |  |

In order to finish Reimer’s proof we need to see that the second essential part of the compression argument holds: that the object does not change too much during compression. Here this means that the total set size has controlled growth.

###### Lemma 29 (Reimer [51]).

Let 𝒜 \mathcal{A} be union-closed family. Then

1. (i)

∑ A ∈ 𝒜 | u ⁡ ( A) − A | ≤ | E ​ B ​ ( u ⁡ ( 𝒜)) | \sum_{A\in\mathcal{A}}|u(A)-A|\leq|EB(u(\mathcal{A}))|; and

2. (ii)

∑ A ∈ 𝒜 | u ⁡ ( A) − A | ≤ | 𝒜 | ( m − log 2 ⁡ ( | 𝒜 |)) \sum_{A\in\mathcal{A}}|u(A)-A|\leq|\mathcal{A}|(m-\log_{2}(|\mathcal{A}|)).

###### Proof of Theorem 21.

Applying the previous lemmas we obtain

 | 2 ​ ∑ A ∈ 𝒜 | A | = \displaystyle 2\sum_{A\in\mathcal{A}}|A|= | 2 ​ ∑ A ∈ 𝒜 | u ⁡ ( A) | − 2 ​ ∑ A ∈ 𝒜 | u ⁡ ( A) − A | \displaystyle\,2\sum_{A\in\mathcal{A}}|u(A)|-2\sum_{A\in\mathcal{A}}|u(A)-A| |  |

 | ≥ \displaystyle\geq | m ​ | u ⁡ ( 𝒜) | + | E ​ B ​ ( u ⁡ ( 𝒜)) | − 2 ​ ∑ A ∈ 𝒜 | u ⁡ ( A) − A | \displaystyle\,m|u(\mathcal{A})|+|EB(u(\mathcal{A}))|-2\sum_{A\in\mathcal{A}}|u(A)-A| |  |

 | ≥ \displaystyle\geq | m | 𝒜 | + | E ​ B ​ ( u ⁡ ( 𝒜)) | − | E ​ B ​ ( u ⁡ ( 𝒜)) | − | 𝒜 | ​ ( m − log 2 ⁡ ( | 𝒜 |)) \displaystyle\,m|\mathcal{A}|+|EB(u(\mathcal{A}))|-|EB(u(\mathcal{A}))|-|\mathcal{A}|(m-\log_{2}(|\mathcal{A}|)) |  |

 | = \displaystyle= | | 𝒜 | ⋅ log 2 ⁡ ( | 𝒜 |). \displaystyle\,|\mathcal{A}|\cdot\log_{2}(|\mathcal{A}|). |  |

∎

Refining Reimer’s approach, Balla, Bollobás and Eccles improve substantially on Nishimura and Takahashi’s observation that large union-closed families never pose a counterexample to Frankl’s conjecture.

###### Theorem 30 (Balla, Bollobás and Eccles [9]).

Any union-closed family on m m elements with at least ⌈ 2 3 ​ 2 m ⌉ \lceil\tfrac{2}{3}2^{m}\rceil member-sets satisfies the union-closed sets conjecture.

In fact, Balla et al. prove that the average frequency of such a family 𝒜 \mathcal{A} is always at least | 𝒜 | 2 \frac{|\mathcal{A}|}{2}. In view of Theorem 26 this is best possible.

The key idea of the proof of Theorem 30 is to exploit the Kruskal-Katona theorem in conjunction with up-compression. This allows to show that, among all union-closed families on n n member-sets, the Hungarian family ℋ ( n) \mathcal{H}^{(n)} has minimal total set size. Since the total set size of ℋ ( n) \mathcal{H}^{(n)} is large, provided that n ≥ ⌈ 2 3 ​ 2 m ⌉ n\geq\lceil\tfrac{2}{3}2^{m}\rceil, the double-counting argument ( 4) then yields an average frequency that is large enough to imply the union-closed sets conjecture for the given family.

Up-compression, and in particular, the effect of the order in which the elements i i of the universe are chosen for the up-compression is further investigated by Rodaro [59]. In a fairly involved article with a heavy algebraic flavour he arrives at an upper-bound on the number of basis sets of the union-closed family. (Recall that a non-empty B ∈ 𝒜 B\in\mathcal{A} is a basis set if B = A ∪ A ′ B=A\cup A^{\prime} for A, A ′ ∈ 𝒜 A,A^{\prime}\in\mathcal{A} implies A = B A=B or A ′ = B A^{\prime}=B.) Rodaro’s bound, however, is weaker than a result of Kleitman from 1976 on set families that are union-free. Cast in the language of basis sets of a union-closed family the result becomes:

###### Theorem 31 (Kleitman [36]).

Let 𝒜 \mathcal{A} be a union-closed family on m m elements. Then the number of basis sets is at most

 | ( m ⌊ m 2 ⌋) + 2 m m. {m\choose\lfloor\frac{m}{2}\rfloor}+\frac{2^{m}}{m}. |  |

While it is not clear how sharp the bound is, a family with ( m ⌊ m 2 ⌋) {m\choose\lfloor\frac{m}{2}\rfloor} basis sets is easily found: simply take all subsets of 2 [m] 2^{[m]} of size at least ⌊ m 2 ⌋ \lfloor\frac{m}{2}\rfloor.

Up-compression is clearly a powerful concept. So, it seems enticing to apply the method in a more direct way to attack Frankl’s conjecture: given a union-closed family 𝒜 \mathcal{A}, choose an element i i in its universe and apply up-compression with respect to i i, and then reduce the problem to the hopefully simpler family u i ​ ( 𝒜) u_{i}(\mathcal{A}). Unfortunately, the up-compressed family u i ​ ( 𝒜) u_{i}(\mathcal{A}) is much too simple with respect to the union-closed sets conjecture: the family satisfies it for trivial reasons. Indeed, the element i i always appears in at least half of the member-sets of u i ​ ( 𝒜) u_{i}(\mathcal{A}).

Lo Faro [22] found a way to circumvent this. Call an element y y*dominated by x x*if y ∈ A ∈ 𝒜 y\in A\in\mathcal{A} implies x ∈ A x\in A —in other words, when 𝒜 y ⊆ 𝒜 x \mathcal{A}_{y}\subseteq\mathcal{A}_{x}. Then we may apply up-compression with respect to y y selectively to the sets in 𝒜 x \mathcal{A}_{x}. That is, we set

 | u y ′ ​ ( A):= { A + y if A ∈ 𝒜 x and A + y ∉ 𝒜 A otherwise. u^{\prime}_{y}(A):=\begin{cases}A+y&\text{ if $A\in\mathcal{A}_{x}$ and $A+y\notin\mathcal{A}$}\\ A&\text{ otherwise}.\end{cases} |  |

The resulting family 𝒜 ′:= u y ′ ​ ( 𝒜) \mathcal{A}^{\prime}:=u^{\prime}_{y}(\mathcal{A}) is still union-closed. Moreover, the frequency of y y is bounded by the frequency of x x, which has not changed. If 𝒜 ′ \mathcal{A}^{\prime} satisfies the union-closed sets conjecture then this is also the case for the original family 𝒜 \mathcal{A}. Thus, this restricted up-compression allows to force more structure without augmenting the frequency. While Lo Faro manages to exploit this technique in order to obtain a bound on a minimal counterexample it is not clear whether it or a variant may be used to a more far-reaching effect.

We note that up-compression is also used by Leck and Roberts [40] in the context of the union-closed sets conjecture.

### 6.5 Generalised averages

We saw in the previous section that the Hungarian family ℋ ( n) \mathcal{H}^{(n)} has minimum total set size among all union-closed families with n n member-sets. Leck, Roberts and Simpson [41] study a more general set-up, in which they allow the set sizes to be weighted. For this, they consider non-negative weight functions w: 2 [m] → ℝ ≥ 0 w:2^{[m]}\to\mathbb{R}_{\geq 0} that are constant on all sets of the same size. That is, there are reals w i ≥ 0 w_{i}\geq 0 so that w ⁡ ( X) = w i w(X)=w_{i} if | X | = i |X|=i, for every X ⊆ [m] X\subseteq[m]. Moreover, the weights are non-decreasing with i i, meaning w 0 ≤ w 1 ≤ … ≤ w m w_{0}\leq w_{1}\leq\ldots\leq w_{m}. The *weight*of a non-empty union-closed family 𝒜 \mathcal{A} is then defined as ∑ A ∈ 𝒜 w ⁡ ( A) \sum_{A\in\mathcal{A}}w(A). For example, if w i = i w_{i}=i for all i ∈ [0, m] i\in[0,m], then w ⁡ ( 𝒜) w(\mathcal{A}) is just the total set size.

For families generated by 2 2 -sets, Leck et al. managed to determine the extremal families. These families turn out to be independent of the actual weight. In contrast to above, where we used the reverse colex order we need here the standard colex order: if X, Y ⊆ [m] X,Y\subseteq[m] are distinct then X < Y X<Y if and only if max ⁡ ( X ​ Δ ​ Y) ∈ Y \max(X\Delta Y)\in Y. Then, we define 𝒰 k \mathcal{U}_{k} to be the union-closure of the first k k distinct 2 2 -sets in the colex order. For any weight w w, Leck et al. calculate the weight of 𝒰 k \mathcal{U}_{k} to be

 | ∑ i = 2 a + 2 ( ( a + 1 i) − ( a − b i − 1)) ⋅ w i, \sum_{i=2}^{a+2}\left({a+1\choose i}-{a-b\choose i-1}\right)\cdot w_{i}, |  |

where a a and b b are any integers such that 0 ≤ b ≤ a 0\leq b\leq a and k = ( a 2) + b k={a\choose 2}+b.

###### Theorem 32 (Leck, Roberts and Simpson [41]).

For every k k and every weight w w, the family 𝒰 k \mathcal{U}_{k} has minimum weight w ⁡ ( 𝒰 k) w(\mathcal{U}_{k}) among all union-closed families generated by k k distinct 2 2 -sets.

A partial result of this had already been proved by Imrich, Sauer and Woess [33], first mentioned in their technical report [32], which showed that any union-closed family 𝒜 \mathcal{A} that is generated by basis sets of size 2 2, has an average set size of at least 1 2 ​ | U ⁡ ( 𝒜) | \tfrac{1}{2}|U(\mathcal{A})|.

As we observed in Section 6.3, averaging does not always succeed, that is, the arithmetic mean of the frequencies is sometimes too low to conclude that the union-closed sets conjecture holds for a given family. For some families, such as the Hungarian family discussed above, this is because there is one or perhaps a few elements with very low frequency. Those elements might be so rare that, on the whole, the average frequency drops below the Frankl threshold of half of the member-sets.

One way to overcome this obstacle is to use a different mean than the arithmetic mean, one that de-emphasises the weight of extremely rare outliers. This approach has been pursued by Duffus and Sands [18]. While they consider a quasi-arithmetic mean for the lattice formulation, we present here the equivalent form in the set formulation. In particular, Duffus and Sands pose the question whether there is a c > 1 c>1 so that

 | 1 | U | ​ ∑ u ∈ U c | 𝒜 u | ≥ c | 𝒜 | 2 \frac{1}{|U|}\sum_{u\in U}c^{|\mathcal{A}_{u}|}\geq c^{\frac{|\mathcal{A}|}{2}} |  | (13) |

for all union-closed families 𝒜 \mathcal{A} with universe U U. Clearly, ( 13) would imply the union-closed sets conjecture. As evidence, Duffus and Sands prove that the lattice version of ( 13) holds for distributive lattices when c = 4 c=4.

While ( 13) seems quite enticing, a new idea is needed to make this, or some other, generalised average work. Indeed, it is no longer obvious how the main advantage of the averaging approach can be exploited, namely that the frequencies are analysed *indirectly*via the set sizes. In the case of distributive lattices, Duffus and Sands could investigate the individual frequencies | 𝒜 u | |\mathcal{A}_{u}| to arrive at their result. In general, this will not be possible. For, if it was, then there would be no need to consider a quasiarithmetic mean (or of any other kind), as one could immediately exhibit an abundant element.

### 6.6 Families of minimum density

Rather than averaging the frequencies over the whole universe, we may hope to gain more by restricting the range of the average, for example to the elements of the smallest member-set. This approach was developed by Wójcik [71] and followed up by Balla [8].

Define s k s_{k} to be the largest real so that for any union-closed family 𝒜 \mathcal{A} and any k k -set S S in 𝒜 \mathcal{A} it holds that

 | 1 | S | ​ ∑ u ∈ S | 𝒜 u | ≥ s k ​ | 𝒜 |. \frac{1}{|S|}\sum_{u\in S}|\mathcal{A}_{u}|\geq s_{k}|\mathcal{A}|. |  | (14) |

The first 10 10 values have been determined exactly by Wójcik; we list here the first five: s 1 = 1 2 s_{1}=\tfrac{1}{2}, s 2 = 1 2 s_{2}=\tfrac{1}{2}, s 3 = 4 9 s_{3}=\tfrac{4}{9}, s 4 = 2 5 s_{4}=\tfrac{2}{5} and s 5 = 9 25 s_{5}=\tfrac{9}{25}. So, in particular, any 5 5 -set in any union-closed family will always contain an element that appears in at least a third of the member-sets.

Somewhat surprisingly, the value s k s_{k} coincides with the so-called minimal *density*of a family on k k elements:

###### Theorem 33 (Wójcik [71]).

For every k ∈ ℕ k\in\mathbb{N} it holds that

 | s k = min 𝒜 ⁡ 1 k ​ | 𝒜 | ⋅ ∑ u ∈ U ⁡ ( 𝒜) | 𝒜 u |, s_{k}=\min_{\mathcal{A}}\frac{1}{k|\mathcal{A}|}\cdot\sum_{u\in U(\mathcal{A})}|\mathcal{A}_{u}|, |  |

where the minimum ranges over all union-closed families 𝒜 \mathcal{A} with | U ⁡ ( 𝒜) | = k |U(\mathcal{A})|=k.

We mention that we have reversed here definition and consequence, as Wójcik defines the s k s_{k} as minimal densities but then proves the equivalence to ( 14).

Wójcik conjectured and Balla proved that:

###### Theorem 34 (Balla [8]).

For all k k, s k ≥ log 2 ⁡ k 2 ​ k s_{k}\geq\frac{\log_{2}k}{2k}.

The main step in the proof is an application of Reimer’s theorem. As Wójcik [71] indicated, this lower bound is asymptotically optimal. To see this, consider the family 2 [r] ∪ [k] 2^{[r]}\cup[k], where r = ⌈ log 2 ⁡ k ⌉ r=\lceil\log_{2}k\rceil, and observe that its density is ( 1 + o ⁡ ( 1)) ​ log 2 ⁡ k 2 ​ k (1+o(1))\frac{\log_{2}k}{2k}. Note, however, that this family is not separating.

Combining Theorems 33 and 34, Balla arrives at a lower bound on the maximum frequency in terms of the size of the universe.

###### Corollary 35 (Balla [8]).

In every union-closed family on m ≥ 16 m\geq 16 elements and n n sets there is an element contained in at least log 2 ⁡ m m ⋅ n 2 \sqrt{\tfrac{\log_{2}m}{m}}\cdot\tfrac{n}{2} many member-sets.

## 7 Further results

Sarvate and Renaud [62] observed that if the union-closed sets conjecture holds for union-closed families on n n sets, n n odd, then it holds for union-closed families with n + 1 n+1 sets. In particular, n 0 n_{0} is odd. Lo Faro [22] and later Roberts and Simpson [58] proved n 0 ≥ 4 ​ m 0 − 1 n_{0}\geq 4m_{0}-1. As discussed earlier, this result turns out to be very useful for families on few sets.

Another result in this direction is given by Norton and Sarvate [48]: any counterexample with n 0 n_{0} sets contains at least three distinct elements of frequency exactly n 0 − 1 2 \tfrac{n_{0}-1}{2}. Other necessary properties of counterexamples were given by Lo Faro [21, 22] and Dohmen [17].

Peng, Sissokho and Zhao [49] study what they call the *half-life*of set families. Given a set family ℬ \mathcal{B} that is not necessarily union-closed, they consider the family ⋃ k ℬ \bigcup^{k}\mathcal{B} defined as the family of unions of at most k k sets of ℬ \mathcal{B}. The half-life of ℬ \mathcal{B} is then the least k k such that ⋃ k ℬ \bigcup^{k}\mathcal{B} satisfies the assertion of the union-closed sets conjecture.

## 8 Extremal frequency

Any induction proof of the union-closed sets conjecture will likely necessitate a strengthened induction hypothesis coupled with structural insight on those families with low maximum frequencies. Let us therefore look at the minimal maximum element frequency a family on a given number of sets may have.

For a union-closed family 𝒜 \mathcal{A} define ϕ ⁡ ( 𝒜) \phi(\mathcal{A}) to be the maximum frequency of an element of the universe, that is,

 | ϕ ⁡ ( 𝒜) = max u ∈ U ⁡ ( 𝒜) ⁡ | 𝒜 u |. \phi(\mathcal{A})=\max_{u\in U(\mathcal{A})}|\mathcal{A}_{u}|. |  |

Let ϕ ⁡ ( n) \phi(n) be the minimum over all ϕ ⁡ ( 𝒜) \phi(\mathcal{A}), where 𝒜 \mathcal{A} is a union-closed family of n ≥ 2 n\geq 2 member-sets. Clearly, this allows the trivial reformulation of the union-closed sets conjecture as:

###### Conjecture 36.

ϕ ⁡ ( n) ≥ n 2 \phi(n)\geq\tfrac{n}{2} for all integers n ≥ 2 n\geq 2.

In this way, the union-closed sets conjecture becomes a problem about an integer sequence. What can be said about this sequence ϕ ⁡ ( n) \phi(n)? For instance, that it is a slowly growing sequence:

###### Lemma 37 (Renaud [53]).

ϕ ⁡ ( n − 1) ≤ ϕ ⁡ ( n) ≤ ϕ ⁡ ( n − 1) + 1 \phi(n-1)\leq\phi(n)\leq\phi(n-1)+1 for all n ≥ 2 n\geq 2.

Renaud 3 3 3 We point out here that our sequence ϕ ⁡ ( n) \phi(n) equals Renaud’s [53] ϕ ⁡ ( n − 1) \phi(n-1). used the lemma to compute the first 17 17 values of ϕ ⁡ ( n) \phi(n). We put ϕ ⁡ ( 1) = 1 \phi(1)=1 so that the sequence starts from n = 1 n=1 on:

 | 1, 1, 2, 2, 3, 4, 4, 4, 5, 6, 7, 7, 8, 8, 8, 8, 9, 10, … 1,1,2,2,3,4,4,4,5,6,7,7,8,8,8,8,9,10,... |  | (15) |

Moreover, if the union-closed sets conjecture is true, then ϕ ⁡ ( n) = n 2 \phi(n)=\tfrac{n}{2} if n n is a power of two, and ϕ ⁡ ( n) > n 2 \phi(n)>\tfrac{n}{2} otherwise, provided Poonen’s conjecture (Conjecture 14) is valid as well.

Now, there is a well-known slowly growing integer sequence that coincides with ϕ ⁡ ( n) \phi(n) on the initial segment ( 15) and that, in addition, has a ⁡ ( n) = n 2 a(n)=\tfrac{n}{2} if and only if n n is power of two. This is Conway’s challenge sequence, defined by a ⁡ ( 1) = a ⁡ ( 2) = 1 a(1)=a(2)=1 and the recurrence relation

 | a ⁡ ( n) = a ⁡ ( a ⁡ ( n − 1)) + a ⁡ ( n − a ⁡ ( n − 1)). a(n)=a(a(n-1))+a(n-a(n-1)). |  |

See, for instance, Kubo and Vakil [39] for background on the sequence.

As Mallows [43] proved that a ⁡ ( n) ≥ n 2 a(n)\geq\tfrac{n}{2} for all n ≥ 1 n\geq 1, it seems tempting to seek a deeper relation between ϕ ⁡ ( n) \phi(n) and a ⁡ ( n) a(n), and in some sense there is one. Renaud and Fitina construct, for every n n, a union-closed family whose maximum element frequency is exactly equal to a ⁡ ( n) a(n). We discuss this construction next.

Let us define an order < < on ℕ ( < ω) \mathbb{N}^{(<\omega)}, the set of finite subsets of ℕ \mathbb{N}, by first sorting by largest element, then by decreasing cardinality and finally by colex order. Thus, A < B A<B if

- •

max ⁡ A < max ⁡ B \max A<\max B; or

- •

max ⁡ A = max ⁡ B \max A=\max B but | A | > | B | |A|>|B|; or

- •

max ⁡ A = max ⁡ B \max A=\max B and | A | = | B | |A|=|B| but max ⁡ ( A ​ Δ ​ B) ∈ B \max(A\Delta B)\in B

Omitting parentheses and commas this yields

 | ∅ < 1 < 12 < 2 < 123 < 13 < 23 < 3 < 1234 < 124 \displaystyle\emptyset<1<12<2<123<13<23<3<1234<124 |  |  |

 | < 134 < 234 < 14 < 24 < 34 < 4 < 12345 < … \displaystyle<134<234<14<24<34<4<12345<... |  |

as initial segment. It is easy to see that A ≤ C A\leq C and B ≤ C B\leq C implies A ∪ B ≤ C A\cup B\leq C, which means that the first n n sets of this order form a union-closed family, denoted by ℛ ⁡ ( n) \mathcal{R}(n).

###### Theorem 38 (Renaud and Fitina [55]).

For every n ≥ 2 n\geq 2, the most frequent element of the Renaud-Fitina family ℛ ⁡ ( n) \mathcal{R}(n) has frequency a ⁡ ( n) a(n), that is,

 | ϕ ⁡ ( n) ≤ a ⁡ ( n). \phi(n)\leq a(n). |  |

So, is ϕ ⁡ ( n) \phi(n) always equal to a ⁡ ( n) a(n)? By Mallows’ result, that would clearly prove the union-closed sets conjecture. Unfortunately, this is not the case. In a subsequent paper, Renaud [54] described families ℬ ⁡ ( n) \mathcal{B}(n) whose element frequency is sometimes strictly smaller than Conways’ challenge sequence. This happens for the first time at n = 23 n=23, where a ⁡ ( n) = 14 a(n)=14. However, no element in the family

 | ℬ ⁡ ( 23) = 2 [4] ∪ { 12345, 1235, 1245, 1345, 2345, 125, 345 } \mathcal{B}(23)=2^{[4]}\cup\{12345,1235,1245,1345,2345,125,345\} |  |

on 23 23 member-sets appears more often than 13 13 times. We omit the precise construction of ℬ ⁡ ( n) \mathcal{B}(n) but mention that it only differs from ℛ ⁡ ( n) \mathcal{R}(n) in the last step, when we delete sets of the same size of the power set 2 [m] 2^{[m]}. There the sets to delete are chosen in a more balanced way, so that the frequency of the elements 1, …, m − 1 1,\ldots,m-1 differs by at most one.

Renaud determines the maximum frequency as follows. Let

 | n = 2 m − ∑ i = 0 r − 1 ( m − 1 i) − v, n=2^{m}-\sum_{i=0}^{r-1}{m-1\choose i}-v, |  |

where 0 ≤ r < m − 1 0\leq r<m-1 and 0 ≤ v < ( m − 1 r) 0\leq v<{m-1\choose r}. Then

 | ϕ ⁡ ( ℬ ⁡ ( n)) = 2 m − 1 − ∑ i = 0 r − 2 ( m − 1 i) − ⌊ r ​ v m − 1 ⌋ \phi(\mathcal{B}(n))=2^{m-1}-\sum_{i=0}^{r-2}{m-1\choose i}-\left\lfloor\frac{rv}{m-1}\right\rfloor |  |

Furthermore, he shows that always ϕ ⁡ ( ℬ ⁡ ( n)) ≤ a ⁡ ( n) \phi(\mathcal{B}(n))\leq a(n). Are the families ℬ ⁡ ( n) \mathcal{B}(n) now truly extremal, that is ϕ ⁡ ( n) = ϕ ⁡ ( ℬ ⁡ ( n)) \phi(n)=\phi(\mathcal{B}(n)) for all n n? Again, this is not the case. Renaud gives the example of the family

 | 𝒞 = 2 [6] ∖ { 6, 5, 16, 25, 36, 45, 136, 245 }, \mathcal{C}=2^{[6]}\setminus\{6,5,16,25,36,45,136,245\}, |  |

in which the most frequent element appears in 30 30 member-sets. However, in ℬ ⁡ ( 56) \mathcal{B}(56) there is an element of frequency 31 31.

To conclude, we do not know much, in general, about the structure of an extremal family, nor are there any convincing candidates. The only exception are power sets 𝒫 \mathcal{P}, for which holds ϕ ⁡ ( 𝒫) = ϕ ⁡ ( | 𝒫 |) \phi(\mathcal{P})=\phi(|\mathcal{P}|), provided the union-closed sets conjecture is true. Nevertheless, the examples in this section seem to indicate that an extremal family would have relatively few elements compared to the number of member-sets: let us call a family on n n member-sets and a universe of size m m*compact*if 2 m − 1 < n ≤ 2 m 2^{m-1}<n\leq 2^{m}. For example, power sets, the Renaud-Fitina families as well as the Hungarian families are compact.

###### Question 39.

Is it true that for a union-closed family 𝒜 \mathcal{A} it follows from ϕ ⁡ ( 𝒜) = ϕ ⁡ ( | 𝒜 |) \phi(\mathcal{A})=\phi(|\mathcal{A}|) that 𝒜 \mathcal{A} is compact?

An affirmative answer would be a major step towards the union-closed sets conjecture. Indeed, Reimer’s bound ( 6) in conjunction with Theorem 17 gives:

###### Observation 40.

Any compact union-closed family 𝒜 \mathcal{A} contains an element that is contained in at least 6 13 ​ | 𝒜 | \tfrac{6}{13}|\mathcal{A}| member-sets.

While we have arrived at the end of this survey, the union-closed sets conjecture still has a bit of a journey ahead of it. We hope it will be an exciting trip.

## Acknowledgement

We are grateful for the extensive bibliography of Marković [45] that was of great help for our own literature research. We thank Bela Bollobás, Dwight Duffus, Peter Frankl, Tomasz Łuczak, Ian Roberts, Jamie Simpson, Peter Winkler and David Yost for their input on the history of the conjecture and for help in tracking down seemingly lost items of the literature. We thank Eric Balandraud for inspiring discussions about the Hungarian family. Finally, we thank the referee who pointed us to the result of Kleitman in Section 6.4, and observed that Knill’s graph-generated families form lower semimodular lattices.

## References

- [1] T. Abe, *Strong semimodular lattices and Frankl’s conjecture*, Algebra univers. 44 (2000), 379–382.
- [2], *Excess of a lattice*, Graphs Comb. 18 (2002), 395–402.
- [3] T. Abe and B. Nakano, *Frankl’s conjecture is true for modular lattices*, Graphs Comb. 14 (1998), 305–311.
- [4], *Lower semimodular types of lattices: Frankl’s conjecture holds for lower quasi-semimodular lattices*, Graphs Comb. 16 (2000), 1–16.
- [5] N. Alon, *On the density of sets of vectors*, Disc. Math. 46 (1983), 199–202.
- [6]*A much-travelled conjecture*, Austr. Math. Soc. Gaz. 14/3 (1987), 63.
- [7]*Union-closed sets conjecture*, Austr. Math. Soc. Gaz. 14/4 (1987), 99.
- [8] I. Balla, *Minimum densities of union-closed families*, arXiv:1106.0369v1 [math.CO], 2011.
- [9] I. Balla, B. Bollobas, and T. Eccles, *Union-closed families of sets*, J. Combin. Theory (Series A) 120 (2013), 531–544.
- [10] I. Bošnjak and P. Marković, *The 11-element case of Frankl’s conjecture*, Europ. J. Combin. 15 (2008), R88.
- [11] H. Bruhn, P. Charbit, O. Schaudt, and J.A. Telle, *The graph formulation of the union-closed sets conjecture*, preprint, 2013.
- [12] H. Bruhn and O. Schaudt, *The union-closed sets conjecture almost holds for almost all random bipartite graphs*, preprint, 2012.
- [13] G. Czédli, *On averaging Frankl’s conjecture for large union-closed sets*, J. Combin. Theory (Series A) 116 (2009), 724–729.
- [14] G. Czédli, M. Maróti, and E.T. Schmidt, *On the scope of averaging for Frankl’s conjecture*, Order 26 (2009), 31–48.
- [15] G. Czédli and E.T. Schmidt, *Frankl’s conjecture for large semimodular and planar semimodular lattices*, Acta Univ. Palacki. Olomuc., Fac. rer. nat., Mathematica 47 (2008), 47–53.
- [16] R. Diestel, *Graph theory *(3rd edition)**, Springer-Verlag, 2005.
- [17] K. Dohmen, *A new perspective on the union-closed sets conjecture*, Ars Combin. 58 (2001), 183–185.
- [18] D. Duffus and B. Sands, *An inequality for the sizes of prime filters of finite distributive lattices*, Disc. Math. 201 (1999), 89–99.
- [19] M. El-Zahar, *A graph-theoretic version of the union-closed sets conjecture*, J. Graph Theory 26 (1997), 155–163.
- [20] V. Falgas-Ravry, *Minimal weight in union-closed families*, Electron. J. Combin. 18 (2011), #P95.
- [21] G. Lo Faro, *A note on the union-closed sets conjecture*, J. Austral. Math. Soc. (Series A) 57 (1994), 230–236.
- [22], *Union-closed sets conjecture: Improved bounds*, J. Combin. Math. Combin. Comput. 16 (1994), 97–102.
- [23] P. Frankl, personal communication.
- [24], *On the trace of finite sets*, J. Combin. Theory (Series A) 34 (1983), 41–45.
- [25], *A new short proof for the Kruskal-Katona theorem*, Disc. Math. 48 (1984), 327–329.
- [26], *Handbook of combinatorics (vol. 2)*, MIT Press, Cambridge, MA, USA, 1995, pp. 1293–1329.
- [27] W. Gao and H. Yu, *Note on the union-closed sets conjecture*, Ars Combin. 49 (1998), 280–288.
- [28] Open Problem Garden, *Frankl’s union-closed sets conjecture*, http://www.openproblemgarden.org/op/frankls_union_closed_sets_conjecture, accessed: 06/05/2013.
- [29] G. Grätzer, *General lattice theory*, Springer-Verlag, 2003.
- [30] C. Herrmann and R. Langsdorf, *Frankl’s conjecture for lower semimodular lattices*, unpublished preprint, 1999.
- [31] Y. Hu, Master’s thesis, in preparation.
- [32] W. Imrich, N. Sauer, and W. Woess, *The average size of admissible sets in a graph*, Tech. report, Montanuniversität Leoben, 1988.
- [33], *The average size of nonsingular sets in a graph*, Finite and Infinite Combinatorics in Sets and Logic (N.W. Sauer et al., ed.), Kluwer Academic Publishers, Dordrecht, Netherlands, 1993, pp. 199–205.
- [34] R.T. Johnson and T.P. Vaughan, *On union-closed families, I*, J. Combin. Theory (Series A) 85 (1999), 112–119.
- [35] G. Kalai, *Extremal Combinatorics IV: Shifting*, http://gilkalai.wordpress.com/2008/10/06/extremal-combinatorics-iv-shifting/, accessed: 01/05/2013.
- [36] D.J. Kleitman, *Extremal properties of collections of subsets containing no two sets and their union*, J. Combin. Theory (Series A) 20 (1976), 390–392.
- [37] E. Knill, *Generalized degrees and densities for families of sets*, PhD thesis, University of Colorado, 1991.
- [38], *Graph generated union-closed families of sets*, arXiv:math/9409215v1 [math.CO], 1994.
- [39] T. Kubo and R. Vakil, *On Conway’s recursive sequence*, Disc. Math. 152 (1996), 225–252.
- [40] U. Leck and I.T. Roberts, *Inequalities for cross-unions of collections of finite sets*, preprint, 2013.
- [41] U. Leck, I.T. Roberts, and J. Simpson, *Minimizing the weight of the union-closure of families of two-sets*, Australas. J. Combin. 52 (2012), 67–73.
- [42] B. Llano, J.J. Montellano-Ballesteros, E. Rivera-Campo, and R. Strausz, *On conjectures of Frankl and El-Zahar*, J. Graph Theory 57 (2008), 344–352.
- [43] C.I. Mallows, *Conway’s challenge sequence*, Amer. Math. Monthly 98 (1991), 5–20.
- [44] F. Marić, M. Živković, and B. Vučković, *Formalizing Frankl’s conjecture: Fc-families*, Lecture Notes in Comput. Sci. 7362 (2012), 248–263.
- [45] P. Marković, *An attempt at Frankl’s conjecture*, Publications de l’Institut Mathématique. Nouvelle Série 81 (2007), 29–43.
- [46] R. Morris, *FC-families, and improved bounds for Frankl’s conjecture*, Europ. J. Combin. 27 (2006), 269–282.
- [47] T. Nishimura and S. Takahashi, *Around Frankl conjecture*, Sci. Rep. Yokohama Nat. Univ. Sect. I Math. Phys. Chem. 43 (1996), 15–23.
- [48] R.M. Norton and D.G. Sarvate, *A note on the union-closed sets conjecture*, J. Austral. Math. Soc. (Series A) 55 (1993), 411–413.
- [49] Y. Peng, P. Sissokho, and C. Zhao, *An extremal problem for set families generated with the union and symmetric difference operations*, J. Combin. 3 (2012), 651–668.
- [50] B. Poonen, *Union-closed families*, J. Combin. Theory (Series A) 59 (1992), 253–268.
- [51] D. Reimer, *An average set size theorem*, Comb., Probab. Comput. (2003), 89–93.
- [52] J. Reinhold, *Frankl’s conjecture is true for lower semimodular lattices*, Graphs Comb. 16 (2000), no. 1, 115–116.
- [53] J.-C. Renaud, *Is the union-closed sets conjecture the best possible?*, J. Austral. Math. Soc. (Series A) 51 (1991), 276–283.
- [54] J-C. Renaud, *A second approximation to the boundary function on union-closed collections*, Ars Combin. 41 (1995), 177–188.
- [55] J.-C. Renaud and L.F. Fitina, *On union-closed sets and Conway’s sequence*, Bull. Austral. Math. Soc. 47 (1993), 321–332.
- [56] I. Rival (ed.), *Graphs and order*, NATO ASI Series, vol. 147, Springer Netherlands, 1985.
- [57] I. Roberts, *The union-closed sets conjecture*, Tech. Report 2/92, Curtin University of Technology, 1992.
- [58] I. Roberts and J. Simpson, *A note on the union-closed sets conjecture*, Australas. J. Combin. 47 (2010), 265–267.
- [59] E. Rodaro, *Union-closed vs upward-closed families of finite sets*, arXiv:math/1208.5371v2 [math.CO], 2012.
- [60] N. Zagaglia Salvi, *An equivalent formulation of the union-closed sets conjecture*, manuscript.
- [61] F. Salzborn, *A note on the intersecting sets conjecture*, manuscript, 1989.
- [62] D.G. Sarvate and J.-C. Renaud, *On the union-closed sets conjecture*, Ars Combin. 27 (1989), 149–154.
- [63], *Improved bounds for the union-closed sets conjecture*, Ars Combin. 29 (1990), 181–185.
- [64] R.P. Stanley, *Enumerative combinatorics, vol. I*, Wadsworth & Brooks/Cole, 1986.
- [65] T.P. Vaughan, *More on 3-sets in union-closed families: The end is in sight*, http://atlas-conferences.com/c/a/q/a/23.htm, accessed: 24/03/2013.
- [66], *Families implying the Frankl conjecture*, Europ. J. Combin. 23 (2002), 851–860.
- [67], *Three-sets in a union-closed family*, J. Combin. Math. Combin. Comput. 49 (2004), 73–84.
- [68] M. Živković and B. Vučković, *The 12 element case of Frankl’s conjecture*, preprint, 2012.
- [69] D. West, *Union-closed sets conjecture (1979)*, http://www.math.uiuc.edu/~west/openp/unionclos.html, accessed: 06/05/2013.
- [70] Wikipedia, *Union-closed sets conjecture*, http://en.wikipedia.org/wiki/Union-closed_sets_conjecture, accessed: 06/05/2013.
- [71] P. Wójcik, *Density of union-closed families*, Disc. Math. 105 (1992), 259–267.
- [72], *Union-closed families of sets*, Disc. Math. 199 (1999), 173–182.

Version 25 Oct 2013

Henning Bruhn <henning.bruhn@uni-ulm.de>
Universität Ulm, Germany
Oliver Schaudt <schaudto@uni-koeln.de>
Institut für Informatik
Universität zu Köln
Weyertal 80
Germany


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
