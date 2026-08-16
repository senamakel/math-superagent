<!-- source: https://en.wikipedia.org/wiki/Union-closed_sets_conjecture | converted from HTML -->

Union-closed sets conjecture - Wikipedia

Jump to content

From Wikipedia, the free encyclopedia

1979 conjecture in combinatorics

Unsolved problem in mathematics

If any two sets in some finite family of sets have a union that also belongs to the family, must some element belong to at least half of the sets in the family?

[More unsolved problems in mathematics][1]

[2] A [hypergraph][3] representing a family of union-closed sets. Vertices 1 and 2 (highlighted red and blue respectively) are present in over half the edges.

The **union-closed sets conjecture**, also known as **Frankl’s conjecture**, is an [open problem][4] in [combinatorics][5] posed by [Péter Frankl][6] in 1979. A [family of sets][7] is said to be *union-closed*if the [union][8] of any two [sets][9] from the family belongs to the family. The [conjecture][10] states:

For every finite union-closed family of sets, other than the empty family, there exists an element that belongs to at least half of the sets in the family.

Professor [Timothy Gowers][11] has called this "*one of the best known open problems in combinatorics*" and has said that the conjecture "*feels as though it ought to be easy (and as a result has attracted a lot of false [proofs][12] over the years). A good way to understand why it isn't easy is to spend an afternoon trying to prove it. That clever averaging argument you had in mind doesn't work ...*" [1]

## Example

[[edit][13]]

The family of sets

∅, { 1 }, { 1, 2 }, { 2, 3, 4 }, { 1, 2, 3, 4 } {\displaystyle \varnothing ,\{1\},\{1,2\},\{2,3,4\},\{1,2,3,4\}}[image: {\displaystyle \varnothing ,\{1\},\{1,2\},\{2,3,4\},\{1,2,3,4\}}]

consists of five different sets and is union-closed. The element 1 {\displaystyle 1}[image: {\displaystyle 1}] is contained in three of the five sets (and so is the element 2 {\displaystyle 2}[image: {\displaystyle 2}]), thus the conjecture holds in this case.

## Basic results

[[edit][14]]

It is easy to show that if a union-closed family contains a [singleton][15] { a } {\displaystyle \{a\}}[image: {\displaystyle \{a\}}] (as in the example above), then the element a {\displaystyle a}[image: {\displaystyle a}] must occur in at least half of the sets of the family.

If there is a [counterexample][16] to the conjecture, then there is also a counterexample consisting only of finite sets. Therefore, without loss of generality, we will assume that all sets in the given union-closed family are finite. [2]

Given a finite non-empty set U {\displaystyle U}[image: {\displaystyle U}], the [power set][17] P ( U) {\displaystyle P(U)}[image: {\displaystyle P(U)}] consisting of all [subsets][18] of U {\displaystyle U}[image: {\displaystyle U}] is union-closed. Each element of U {\displaystyle U}[image: {\displaystyle U}] is contained in exactly half of the subsets of U {\displaystyle U}[image: {\displaystyle U}]. Therefore, in general we cannot ask for an element contained in more than half of the sets of the family: the [bound][19] of the conjecture is sharp.

## Equivalent forms

[[edit][20]]

### Intersection formulation

[[edit][21]]

The union-closed set conjecture is true [if and only if][22] a set system X {\displaystyle X}[image: {\displaystyle X}] which is intersection-closed contains an element of U ( X) {\displaystyle U(X)}[image: {\displaystyle U(X)}] in at most half of the sets of X {\displaystyle X}[image: {\displaystyle X}], where U ( X) {\displaystyle U(X)}[image: {\displaystyle U(X)}] is the universe set, i.e. the union of all members of the system X {\displaystyle X}[image: {\displaystyle X}].

The following facts show the equivalence.

Firstly, we show that a set system is union-closed if and only if its complement is intersection-closed.

Lemma 1. If X {\displaystyle X}[image: {\displaystyle X}] is a union-closed family of sets with universe U ( X) {\displaystyle U(X)}[image: {\displaystyle U(X)}], the family of [complement sets][23] to sets in X {\displaystyle X}[image: {\displaystyle X}] is closed under [intersection][24].

Proof. We define the complement of the set system X {\displaystyle X}[image: {\displaystyle X}] as X c:= { U ( X) − S: S ∈ X } {\displaystyle X^{c}:=\{U(X)-S:S\in X\}}[image: {\displaystyle X^{c}:=\{U(X)-S:S\in X\}}].

Let X 1 {\displaystyle X_{1}}[image: {\displaystyle X_{1}}], X 2 {\displaystyle X_{2}}[image: {\displaystyle X_{2}}] be arbitrary sets in X {\displaystyle X}[image: {\displaystyle X}] and so U ( X) − X 1 {\displaystyle U(X)-X_{1}}[image: {\displaystyle U(X)-X_{1}}] and U ( X) − X 2 {\displaystyle U(X)-X_{2}}[image: {\displaystyle U(X)-X_{2}}] are both in X c {\displaystyle X^{c}}[image: {\displaystyle X^{c}}]. Since X {\displaystyle X}[image: {\displaystyle X}] is union-closed, X 1 ∪ X 2 = X 3 {\displaystyle X_{1}\cup X_{2}=X_{3}}[image: {\displaystyle X_{1}\cup X_{2}=X_{3}}] is in X {\displaystyle X}[image: {\displaystyle X}], and therefore the complement of X 3 {\displaystyle X_{3}}[image: {\displaystyle X_{3}}], U ( X) − X 3 {\displaystyle U(X)-X_{3}}[image: {\displaystyle U(X)-X_{3}}] is in X c {\displaystyle X^{c}}[image: {\displaystyle X^{c}}], the elements in neither X 1 {\displaystyle X_{1}}[image: {\displaystyle X_{1}}], nor X 2 {\displaystyle X_{2}}[image: {\displaystyle X_{2}}].

And this is exactly the intersection of the complements of X 1 {\displaystyle X_{1}}[image: {\displaystyle X_{1}}] and X 2 {\displaystyle X_{2}}[image: {\displaystyle X_{2}}], ( U ( X) − X 1) ∩ ( U ( X) − X 2) {\displaystyle (U(X)-X_{1})\cap (U(X)-X_{2})}[image: {\displaystyle (U(X)-X_{1})\cap (U(X)-X_{2})}]. Therefore, X {\displaystyle X}[image: {\displaystyle X}] is union-closed if and only if the complement of X {\displaystyle X}[image: {\displaystyle X}], X c {\displaystyle X^{c}}[image: {\displaystyle X^{c}}] is intersection closed.

Secondly, we show that if a set system contains an element in at least half the sets, then its complement has an element in at most half.

Lemma 2. A set system X {\displaystyle X}[image: {\displaystyle X}] contains an element in half of its sets if and only if the complement set system X {\displaystyle X}[image: {\displaystyle X}], X ∗ {\displaystyle X^{*}}[image: {\displaystyle X^{*}}] contains an element in at most half of its sets. Proof. Trivial.

Therefore, if X {\displaystyle X}[image: {\displaystyle X}] is a union-closed family of sets, the family of complement sets to sets in X {\displaystyle X}[image: {\displaystyle X}] relative to the universe U ( X) {\displaystyle U(X)}[image: {\displaystyle U(X)}] is closed under intersection, and an element that belongs to at least half of the sets of X {\displaystyle X}[image: {\displaystyle X}] belongs to at most half of the complement sets. Thus, an equivalent form of the conjecture (the form in which it was originally stated) is that, for any intersection-closed family of sets that contains more than one set, there exists an element that belongs to at most half of the sets in the family.

### Lattice formulation

[[edit][25]]

Although stated above in terms of families of sets, Frankl's conjecture has also been formulated and studied as a question in [lattice theory][26]. A [lattice][27] is a [partially ordered set][28] in which for two elements *x*and *y*there is a unique greatest element less than or equal to both of them (the [meet][29] of *x*and *y*) and a unique least element greater than or equal to both of them (the [join][29] of *x*and *y*). The family of all subsets of a set *S*, ordered by set inclusion, forms a lattice in which the meet is represented by the [set-theoretic][30] intersection and the join is represented by the set-theoretic union; a lattice formed in this way is called a [Boolean lattice][31]. The lattice-theoretic version of Frankl's conjecture is that in any finite lattice there exists an element *x*that is not the join of any two smaller elements, and such that the number of elements greater than or equal to *x*totals at most half the lattice, with equality only if the lattice is a Boolean lattice. As Abe (2000) shows, this statement about lattices is equivalent to the Frankl conjecture for union-closed sets: each lattice can be translated into a union-closed set family, and each union-closed set family can be translated into a lattice, such that the truth of the Frankl conjecture for the translated object implies the truth of the conjecture for the original object. This lattice-theoretic version of the conjecture is known to be true for several natural subclasses of lattices [3] but remains open in the general case.

### Proof of equivalence

[[edit][32]]

Let *L*be a finite lattice, and let *J(L)*denote the set of [join-irreducible elements][33] of *L*. For each element x ∈ L {\displaystyle x\in L}[image: {\displaystyle x\in L}], define T x = { j ∈ J ( L): j ≤ x }. {\displaystyle T_{x}=\{j\in J(L):j\leq x\}.}[image: {\displaystyle T_{x}=\{j\in J(L):j\leq x\}.}]

The map x ↦ T x {\displaystyle x\mapsto T_{x}}[image: {\displaystyle x\mapsto T_{x}}] is injective, because in a finite lattice every element is the join of the join-irreducible elements below it. Thus, if T x = T y {\displaystyle T_{x}=T_{y}}[image: {\displaystyle T_{x}=T_{y}}], then *x*and *y*have the same join-irreducible elements below them, and therefore x = y {\displaystyle x=y}[image: {\displaystyle x=y}]. It follows that the family F = { T x: x ∈ L } {\displaystyle {\mathcal {F}}=\{T_{x}:x\in L\}}[image: {\displaystyle {\mathcal {F}}=\{T_{x}:x\in L\}}] has cardinality | L | {\displaystyle |L|}[image: {\displaystyle |L|}].

Moreover, F {\displaystyle {\mathcal {F}}}[image: {\displaystyle {\mathcal {F}}}] is intersection-closed. Indeed, for any x, y ∈ L {\displaystyle x,y\in L}[image: {\displaystyle x,y\in L}], j ≤ x ∧ y {\displaystyle j\leq x\wedge y}[image: {\displaystyle j\leq x\wedge y}] if and only if j ≤ x {\displaystyle j\leq x}[image: {\displaystyle j\leq x}] and j ≤ y {\displaystyle j\leq y}[image: {\displaystyle j\leq y}], so T x ∧ y = T x ∩ T y. {\displaystyle T_{x\wedge y}=T_{x}\cap T_{y}.}[image: {\displaystyle T_{x\wedge y}=T_{x}\cap T_{y}.}]

Assume now that every finite intersection-closed family has an element contained in at most half of its sets. Applying this statement to F {\displaystyle {\mathcal {F}}}[image: {\displaystyle {\mathcal {F}}}], there exists some j ∈ J ( L) {\displaystyle j\in J(L)}[image: {\displaystyle j\in J(L)}] such that *j*belongs to at most half of the sets T x {\displaystyle T_{x}}[image: {\displaystyle T_{x}}]. But j ∈ T x {\displaystyle j\in T_{x}}[image: {\displaystyle j\in T_{x}}] holds exactly when j ≤ x {\displaystyle j\leq x}[image: {\displaystyle j\leq x}]. Therefore the number of members of F {\displaystyle {\mathcal {F}}}[image: {\displaystyle {\mathcal {F}}}] containing *j*is exactly the number of elements of *L*lying above *j*, namely | ↑ j | {\displaystyle |\uparrow j|}[image: {\displaystyle |\uparrow j|}], where ↑ j = { x ∈ L: j ≤ x }. {\displaystyle \uparrow j=\{x\in L:j\leq x\}.}[image: {\displaystyle \uparrow j=\{x\in L:j\leq x\}.}] Hence | ↑ j | ≤ | L | 2. {\displaystyle |\uparrow j|\leq {\frac {|L|}{2}}.}[image: {\displaystyle |\uparrow j|\leq {\frac {|L|}{2}}.}] This proves the lattice-theoretic statement.

For the converse, let A {\displaystyle {\mathcal {A}}}[image: {\displaystyle {\mathcal {A}}}] be a finite intersection-closed family of sets. Ordered by inclusion, A {\displaystyle {\mathcal {A}}}[image: {\displaystyle {\mathcal {A}}}] is a finite lattice in which the meet is set intersection and the join of two elements is the least member of A {\displaystyle {\mathcal {A}}}[image: {\displaystyle {\mathcal {A}}}] containing their union. Assume that every finite lattice contains a join-irreducible element *j*such that | ↑ j | ≤ | L | 2. {\displaystyle |\uparrow j|\leq {\frac {|L|}{2}}.}[image: {\displaystyle |\uparrow j|\leq {\frac {|L|}{2}}.}] Applying this to the lattice L = A {\displaystyle L={\mathcal {A}}}[image: {\displaystyle L={\mathcal {A}}}], choose such a join-irreducible element *j*.

Because *j*is join-irreducible in a finite lattice, it has a unique lower cover, denoted j ∗ {\displaystyle j_{*}}[image: {\displaystyle j_{*}}]. Choose an element a ∈ j ∖ j ∗. {\displaystyle a\in j\setminus j_{*}.}[image: {\displaystyle a\in j\setminus j_{*}.}] Such an element exists because j ∗ ⊊ j {\displaystyle j_{*}\subsetneq j}[image: {\displaystyle j_{*}\subsetneq j}].

It is then claimed that every member of A {\displaystyle {\mathcal {A}}}[image: {\displaystyle {\mathcal {A}}}] containing *a*lies above *j*. Let A ∈ A {\displaystyle A\in {\mathcal {A}}}[image: {\displaystyle A\in {\mathcal {A}}}] and suppose a ∈ A {\displaystyle a\in A}[image: {\displaystyle a\in A}]. If j ⊈ A {\displaystyle j\nsubseteq A}[image: {\displaystyle j\nsubseteq A}], then j ∧ A = j ∩ A {\displaystyle j\wedge A=j\cap A}[image: {\displaystyle j\wedge A=j\cap A}] is a proper subset of *j*, and hence j ∧ A ≤ j ∗. {\displaystyle j\wedge A\leq j_{*}.}[image: {\displaystyle j\wedge A\leq j_{*}.}] But a ∈ j {\displaystyle a\in j}[image: {\displaystyle a\in j}] and a ∈ A {\displaystyle a\in A}[image: {\displaystyle a\in A}], so a ∈ j ∩ A = j ∧ A {\displaystyle a\in j\cap A=j\wedge A}[image: {\displaystyle a\in j\cap A=j\wedge A}], which would imply a ∈ j ∗ {\displaystyle a\in j_{*}}[image: {\displaystyle a\in j_{*}}], contrary to the choice of *a*. Therefore j ⊆ A {\displaystyle j\subseteq A}[image: {\displaystyle j\subseteq A}], that is, j ≤ A {\displaystyle j\leq A}[image: {\displaystyle j\leq A}] in the lattice order.

So every set in A {\displaystyle {\mathcal {A}}}[image: {\displaystyle {\mathcal {A}}}] containing *a*belongs to ↑ j {\displaystyle \uparrow j}[image: {\displaystyle \uparrow j}]. Conversely, if A ∈ ↑ j {\displaystyle A\in \uparrow j}[image: {\displaystyle A\in \uparrow j}], then j ⊆ A {\displaystyle j\subseteq A}[image: {\displaystyle j\subseteq A}], and since a ∈ j {\displaystyle a\in j}[image: {\displaystyle a\in j}], the set *A*contains *a*. Thus the sets in A {\displaystyle {\mathcal {A}}}[image: {\displaystyle {\mathcal {A}}}] containing *a*are exactly the elements of ↑ j {\displaystyle \uparrow j}[image: {\displaystyle \uparrow j}].

It follows that the number of members of A {\displaystyle {\mathcal {A}}}[image: {\displaystyle {\mathcal {A}}}] containing *a*is | ↑ j | ≤ | A | 2. {\displaystyle |\uparrow j|\leq {\frac {|{\mathcal {A}}|}{2}}.}[image: {\displaystyle |\uparrow j|\leq {\frac {|{\mathcal {A}}|}{2}}.}] Therefore *a*belongs to at most half of the sets in A {\displaystyle {\mathcal {A}}}[image: {\displaystyle {\mathcal {A}}}]. This proves the intersection-closed formulation.

### Graph-theoretic formulation

[[edit][34]]

Another equivalent formulation of the union-closed sets conjecture uses [graph theory][35]. In an [undirected graph][36], an [Independent set][37] is a set of vertices no two of which are adjacent to each other; an independent set is [maximal][38] if it is not a subset of a larger independent set. In any graph, the "heavy" vertices that appear in more than half of the maximal independent sets must themselves form an independent set. So, if the graph is non-empty, there always exists at least one non-heavy vertex, a vertex that appears in at most half of the maximal independent sets. The graph formulation of the union-closed sets conjecture states that every finite non-empty graph contains two adjacent non-heavy vertices. It is automatically true when the graph contains an [odd][39] [cycle][40], because the independent set of all heavy vertices cannot cover all the edges of the cycle. Therefore, the more interesting case of the conjecture is for [bipartite graphs][41], which have no odd cycles. Another equivalent formulation of the conjecture is that, in every bipartite graph, there exist two vertices, one on each side of the bipartition, such that each of these two vertices belongs to at most half of the graph's maximal independent sets. This conjecture is known to hold for [chordal bipartite graphs][42], bipartite [series–parallel graphs][43], and bipartite graphs of maximum [degree][44] three. [4]

## Partial results

[[edit][45]]

The conjecture has been proven for many special cases of union-closed set families. In particular, it is known to be true for

- families of at most 50 sets, [5]
- families of sets whose union has at most 12 elements, [6]
- families of sets in which the smallest set has one or two elements, [7]
- families of at least ( 1 2 − ε) 2 n {\displaystyle ({\tfrac {1}{2}}-\varepsilon )2^{n}}[image: {\displaystyle ({\tfrac {1}{2}}-\varepsilon )2^{n}}] subsets of an n {\displaystyle n}[image: {\displaystyle n}] -element set, for some constant 0"}}'> 0}"> ε > 0 {\displaystyle \varepsilon >0} 0}"/>, according to an unpublished preprint. [8]
- families of sets with short chain no more than 3 or long chain no less than n − 1 {\displaystyle n-1}[image: {\displaystyle n-1}]. [9]

Additionally, for every union-closed family, other than the family containing only the [empty set][46], there exists an element that belongs to at least 0.38271 {\displaystyle 0.38271}[image: {\displaystyle 0.38271}] of the sets in the family. [10] [11] The proof of this was built upon the work of Gilmer who showed the first constant bound of 0.01 {\displaystyle 0.01}[image: {\displaystyle 0.01}] which was improved by others the same week to 3 − 5 2 ≈ 0.381966 {\displaystyle {\frac {3-{\sqrt {5}}}{2}}\approx 0.381966}[image: {\displaystyle {\frac {3-{\sqrt {5}}}{2}}\approx 0.381966}]. [12]

## History

[[edit][47]]

[Péter Frankl][6] stated the conjecture in terms of intersection-closed set families in 1979, and so the conjecture is usually credited to him and is sometimes referred to as the **Frankl conjecture**. The earliest publication of the union-closed version of the conjecture appears to be by Duffus (1985). A history of the work on the conjecture up to 2013 was published by Bruhn & Schaudt (2015).

## Notes

[[edit][48]]

1. ↑ [Gowers, Timothy [@wtgowers]][11] (17 November 2022). ["One of the best known open problems in combinatorics is the union-closed conjecture, which states that if you have a finite collection X of sets such that if A and B belong to X then so does the union of A and B, then at least one element of X belongs to at least half of them. 1/"][49] ( [Tweet][50]) – via [Twitter][51]. The conjecture feels as though it ought to be easy (and as a result has attracted a lot of false proofs over the years). A good way to understand why it isn't easy is to spend an afternoon trying to prove it. That clever averaging argument you had in mind doesn't work ... 4/4
2. ↑ Bruhn & Schaudt (2015).
3. ↑ Abe (2000); Poonen (1992); Reinhold (2000).
4. ↑ Bruhn et al. (2015).
5. ↑ Roberts & Simpson (2010) show that a minimal counterexample's number of sets is at least 4 q − 1 {\displaystyle 4q-1}[image: {\displaystyle 4q-1}], where q {\displaystyle q}[image: {\displaystyle q}] is the number of elements in the union of all the sets. Combined with the statement of Vuckovic & Zivkovic (2017) stating that a counterexample has at least 13 elements in the union, the conjecture follows for families of at most 50 sets.
6. ↑ Vuckovic & Zivkovic (2017), improving previous bounds by Bošnjak & Marković (2008), Morris (2006), Lo Faro (1994) and others.
7. ↑ Sarvate & Renaud (1989), since rediscovered by several other authors. If a one-element or two-element set *S*exists, some element of *S*belongs to at least half the sets in the family, but the same property does not hold for three-element sets, due to counterexamples of Sarvate, Renaud, and [Ronald Graham][52].
8. ↑ Karpas (2017).
9. ↑ Tian (2021).
10. ↑ Liu, Jingbo (2023-06-15). "Improving the Lower Bound for the Union-closed Sets Conjecture via Conditionally IID Coupling". [arXiv][53]: [2306.08824][54] [[cs.IT][55]].
11. ↑ Lu, Kengbo; Raz, Abigail (2024). "Note on the union-closed sets conjecture and Reimer's average set size theorem". [arXiv][53]: [2405.10639][56] [[math.CO][57]].
12. ↑ Gilmer, Justin (2022). "A constant lower bound for the union-closed sets conjecture". [arXiv][53]: [2211.09055][58] [[math.CO][57]].

## References

[[edit][59]]

- Abe, Tetsuya (2000). "Strong semimodular lattices and Frankl's conjecture". *Algebra Universalis*. **44**( 3– 4): 379– 382. [doi][60]: [10.1007/s000120050195][61]. [S2CID][62] [120741780][63].
- Vuckovic, Bojan; Zivkovic, Miodrag (2017). ["The 12-Element Case of Frankl's Conjecture"][64] (PDF). *[IPSI BGD Transactions on Internet Research][65]*. **13**(1): 65.
- Bošnjak, Ivica; Marković, Peter (2008). ["The 11-element case of Frankl's conjecture"][66]. *[Electronic Journal of Combinatorics][67]*. **15**(1): R88. [doi][60]: [10.37236/812][68].
- Bruhn, Henning; Charbit, Pierre; Schaudt, Oliver; Telle, Jan Arne (2015). "The graph formulation of the union-closed sets conjecture". *[European Journal of Combinatorics][69]*. **43**: 210– 219. [arXiv][53]: [1212.4175][70]. [doi][60]: [10.1016/j.ejc.2014.08.030][71]. [MR][72] [3266293][73]. [S2CID][62] [2373192][74].
- Bruhn, Henning; Schaudt, Oliver (2015-11-01). ["The Journey of the Union-Closed Sets Conjecture"][75]. *Graphs and Combinatorics*. **31**(6): 2043– 2074. [arXiv][53]: [1309.3297][76]. [doi][60]: [10.1007/s00373-014-1515-0][77].
- [Duffus, D.][78] (1985). [Rival, I.][79] (ed.). *Open problem session*. Graphs and Order. D. Reidel. p. 525.
- Karpas, Ilan (2017). "Two Results on Union-Closed Families". [arXiv][53]: [1708.01434][80] [[math.CO][57]].
- Tian, Chenxiao (2021). "Union-closed Sets Conjecture Holds for Height H(𝓕)≤ 𝟑 and H(𝓕)≥ 𝐧 - 𝟏". [arXiv][53]: [2112.06659][81] [[math.CO][57]].
- Lo Faro, Giovanni (1994). "Union-closed sets conjecture: improved bounds". *J. Combin. Math. Combin. Comput*. **16**: 97– 102. [MR][72] [1301213][82].
- [Morris, Robert][83] (2006). "FC-families and improved bounds for Frankl's conjecture". *[European Journal of Combinatorics][69]*. **27**(2): 269– 282. [arXiv][53]: [math/0702348][84]. [doi][60]: [10.1016/j.ejc.2004.07.012][85]. [MR][72] [2199779][86]. [S2CID][62] [17633023][87].
- [Poonen, Bjorn][88] (1992). ["Union-closed families"][89]. *[Journal of Combinatorial Theory][90]*. Series A. **59**(2): 253– 268. [doi][60]: [10.1016/0097-3165(92)90068-6][89]. [MR][72] [1149898][91].
- Reinhold, Jürgen (2000). "Frankl's conjecture is true for lower semimodular lattices". *[Graphs and Combinatorics][92]*. **16**(1): 115– 116. [doi][60]: [10.1007/s003730050008][93]. [S2CID][62] [12660895][94].
- Roberts, Ian; Simpson, Jamie (2010). ["A note on the union-closed sets conjecture"][95] (PDF). *Australas. J. Combin*. **47**: 265– 267.
- Sarvate, D. G.; Renaud, J.-C. (1989). "On the union-closed sets conjecture". *Ars Combin*. **27**: 149– 153. [MR][72] [0989460][96].
- Yu, Lei (2023). ["Dimension-free bounds for the union-closed sets conjecture"][97]. *Entropy*. **25**(5): 767. [arXiv][53]: [2212.00658][98]. [Bibcode][99]: [2023Entrp..25..767Y][100]. [doi][60]: [10.3390/e25050767][101]. [PMC][102] [10217025][97]. [PMID][103] [37238522][104].

## External links

[[edit][105]]

- [Frankl's union-closed sets conjecture][106], the Open Problem Garden.
- [Union-Closed Sets Conjecture (1979)][107]. In *[Open Problems – Graph Theory and Combinatorics][108]*, collected by D. B. West.

Retrieved from " [https://en.wikipedia.org/w/index.php?title=Union-closed_sets_conjecture&oldid=1350313043][109] "

[Categories][110]:

- [Families of sets][111]
- [Conjectures][112]
- [Unsolved problems in mathematics][113]
- [Lattice theory][114]
- [Extremal combinatorics][115]

Hidden categories:

- [Articles with short description][116]
- [Short description matches Wikidata][117]

Search

Union-closed sets conjecture

3 languages Add topic


## Links

[1]: https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_mathematics
[2]: https://en.wikipedia.org/wiki/File:Union-closed_sets.svg
[3]: https://en.wikipedia.org/wiki/Hypergraph
[4]: https://en.wikipedia.org/wiki/Open_problem
[5]: https://en.wikipedia.org/wiki/Combinatorics
[6]: https://en.wikipedia.org/wiki/Péter_Frankl
[7]: https://en.wikipedia.org/wiki/Family_of_sets
[8]: https://en.wikipedia.org/wiki/Union_(set_theory)
[9]: https://en.wikipedia.org/wiki/Set_(mathematics)
[10]: https://en.wikipedia.org/wiki/Conjecture
[11]: https://en.wikipedia.org/wiki/Timothy_Gowers
[12]: https://en.wikipedia.org/wiki/Mathematical_proof
[13]: /w/index.php?title=Union-closed_sets_conjecture&amp;action=edit&amp;section=1
[14]: /w/index.php?title=Union-closed_sets_conjecture&amp;action=edit&amp;section=2
[15]: https://en.wikipedia.org/wiki/Singleton_(mathematics)
[16]: https://en.wikipedia.org/wiki/Counterexample
[17]: https://en.wikipedia.org/wiki/Power_set
[18]: https://en.wikipedia.org/wiki/Subset
[19]: https://en.wikipedia.org/wiki/Upper_and_lower_bounds
[20]: /w/index.php?title=Union-closed_sets_conjecture&amp;action=edit&amp;section=3
[21]: /w/index.php?title=Union-closed_sets_conjecture&amp;action=edit&amp;section=4
[22]: https://en.wikipedia.org/wiki/If_and_only_if
[23]: https://en.wikipedia.org/wiki/Complement_set
[24]: https://en.wikipedia.org/wiki/Intersection_(set_theory)
[25]: /w/index.php?title=Union-closed_sets_conjecture&amp;action=edit&amp;section=5
[26]: https://en.wikipedia.org/wiki/Lattice_theory
[27]: https://en.wikipedia.org/wiki/Lattice_(order)
[28]: https://en.wikipedia.org/wiki/Partially_ordered_set
[29]: https://en.wikipedia.org/wiki/Meet_and_join
[30]: https://en.wikipedia.org/wiki/Set-theoretic
[31]: https://en.wikipedia.org/wiki/Boolean_algebra_(structure)
[32]: /w/index.php?title=Union-closed_sets_conjecture&amp;action=edit&amp;section=6
[33]: https://en.wikipedia.org/wiki/Join-irreducible_element?action=edit&amp;redlink=1
[34]: /w/index.php?title=Union-closed_sets_conjecture&amp;action=edit&amp;section=7
[35]: https://en.wikipedia.org/wiki/Graph_theory
[36]: https://en.wikipedia.org/wiki/Undirected_graph
[37]: https://en.wikipedia.org/wiki/Independent_set_(graph_theory)
[38]: https://en.wikipedia.org/wiki/Maximal_independent_set
[39]: https://en.wikipedia.org/wiki/Parity_(mathematics)
[40]: https://en.wikipedia.org/wiki/Cycle_(graph_theory)
[41]: https://en.wikipedia.org/wiki/Bipartite_graph
[42]: https://en.wikipedia.org/wiki/Chordal_bipartite_graph
[43]: https://en.wikipedia.org/wiki/Series–parallel_graph
[44]: https://en.wikipedia.org/wiki/Degree_(graph_theory)
[45]: /w/index.php?title=Union-closed_sets_conjecture&amp;action=edit&amp;section=8
[46]: https://en.wikipedia.org/wiki/Empty_set
[47]: /w/index.php?title=Union-closed_sets_conjecture&amp;action=edit&amp;section=9
[48]: /w/index.php?title=Union-closed_sets_conjecture&amp;action=edit&amp;section=10
[49]: https://twitter.com/wtgowers/status/1593157232543207424
[50]: https://en.wikipedia.org/wiki/Tweet_(social_media)
[51]: https://en.wikipedia.org/wiki/Twitter
[52]: https://en.wikipedia.org/wiki/Ronald_Graham
[53]: https://en.wikipedia.org/wiki/ArXiv_(identifier)
[54]: https://arxiv.org/pdf/2306.08824
[55]: https://arxiv.org/archive/cs.IT
[56]: https://arxiv.org/pdf/2405.10639
[57]: https://arxiv.org/archive/math.CO
[58]: https://arxiv.org/pdf/2211.09055
[59]: /w/index.php?title=Union-closed_sets_conjecture&amp;action=edit&amp;section=11
[60]: https://en.wikipedia.org/wiki/Doi_(identifier)
[61]: https://doi.org/10.1007%2Fs000120050195
[62]: https://en.wikipedia.org/wiki/S2CID_(identifier)
[63]: https://api.semanticscholar.org/CorpusID:120741780
[64]: https://ipsitransactions.org/journals/papers/tir/2017jan/p9.pdf
[65]: https://en.wikipedia.org/wiki/IPSI_BGD_Transactions_on_Internet_Research?action=edit&amp;redlink=1
[66]: http://www.combinatorics.org/Volume_15/Abstracts/v15i1r88.html
[67]: https://en.wikipedia.org/wiki/Electronic_Journal_of_Combinatorics
[68]: https://doi.org/10.37236%2F812
[69]: https://en.wikipedia.org/wiki/European_Journal_of_Combinatorics
[70]: https://arxiv.org/pdf/1212.4175
[71]: https://doi.org/10.1016%2Fj.ejc.2014.08.030
[72]: https://en.wikipedia.org/wiki/MR_(identifier)
[73]: https://mathscinet.ams.org/mathscinet-getitem?mr=3266293
[74]: https://api.semanticscholar.org/CorpusID:2373192
[75]: https://doi.org/10.1007/s00373-014-1515-0
[76]: https://arxiv.org/pdf/1309.3297
[77]: https://doi.org/10.1007%2Fs00373-014-1515-0
[78]: https://en.wikipedia.org/wiki/Dwight_Duffus
[79]: https://en.wikipedia.org/wiki/Ivan_Rival
[80]: https://arxiv.org/pdf/1708.01434
[81]: https://arxiv.org/pdf/2112.06659
[82]: https://mathscinet.ams.org/mathscinet-getitem?mr=1301213
[83]: https://en.wikipedia.org/wiki/Robert_Morris_(mathematician)
[84]: https://arxiv.org/pdf/math/0702348
[85]: https://doi.org/10.1016%2Fj.ejc.2004.07.012
[86]: https://mathscinet.ams.org/mathscinet-getitem?mr=2199779
[87]: https://api.semanticscholar.org/CorpusID:17633023
[88]: https://en.wikipedia.org/wiki/Bjorn_Poonen
[89]: https://doi.org/10.1016%2F0097-3165%2892%2990068-6
[90]: https://en.wikipedia.org/wiki/Journal_of_Combinatorial_Theory
[91]: https://mathscinet.ams.org/mathscinet-getitem?mr=1149898
[92]: https://en.wikipedia.org/wiki/Graphs_and_Combinatorics
[93]: https://doi.org/10.1007%2Fs003730050008
[94]: https://api.semanticscholar.org/CorpusID:12660895
[95]: http://ajc.maths.uq.edu.au/pdf/47/ajc_v47_p265.pdf
[96]: https://mathscinet.ams.org/mathscinet-getitem?mr=0989460
[97]: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10217025
[98]: https://arxiv.org/pdf/2212.00658
[99]: https://en.wikipedia.org/wiki/Bibcode_(identifier)
[100]: https://ui.adsabs.harvard.edu/abs/2023Entrp..25..767Y
[101]: https://doi.org/10.3390%2Fe25050767
[102]: https://en.wikipedia.org/wiki/PMC_(identifier)
[103]: https://en.wikipedia.org/wiki/PMID_(identifier)
[104]: https://pubmed.ncbi.nlm.nih.gov/37238522
[105]: /w/index.php?title=Union-closed_sets_conjecture&amp;action=edit&amp;section=12
[106]: http://garden.irmacs.sfu.ca/?q=op/frankls_union_closed_sets_conjecture
[107]: http://www.math.uiuc.edu/~west/openp/unionclos.html
[108]: http://www.math.uiuc.edu/~west/openp/index.html
[109]: https://en.wikipedia.org/w/index.php?title=Union-closed_sets_conjecture&amp;oldid=1350313043
[110]: /wiki/Help:Category
[111]: /wiki/Category:Families_of_sets
[112]: /wiki/Category:Conjectures
[113]: /wiki/Category:Unsolved_problems_in_mathematics
[114]: /wiki/Category:Lattice_theory
[115]: /wiki/Category:Extremal_combinatorics
[116]: /wiki/Category:Articles_with_short_description
[117]: /wiki/Category:Short_description_matches_Wikidata
