<!-- source: https://www.michaelnielsen.org/polymath/index.php?title=Frankl%27s_union-closed_conjecture | converted from HTML -->

Frankl's union-closed conjecture - Polymath Wiki

# Frankl's union-closed conjecture

From Polymath Wiki

Jump to navigation Jump to search

A family [math]\displaystyle{ \mathcal{A} }[/math] of sets is called *union closed*if [math]\displaystyle{ A\cup B\in\mathcal{A} }[/math] whenever [math]\displaystyle{ A\in\mathcal{A} }[/math] and [math]\displaystyle{ B\in\mathcal{A} }[/math]. Frankl's conjecture is a disarmingly simple one: if [math]\displaystyle{ \mathcal{A} }[/math] is a union-closed family of n sets, then must there be an element that belongs to at least n/2 of the sets? The problem has been open for decades, despite the attention of several people.

## Contents

- 1 Definitions
- 2 Partial results
- 3 The m=13 case
- 4 General proof strategies
- 5 Strengthenings

  - 5.1 Conjectures that imply FUNC

    - 5.1.1 Injection-to-superset
    - 5.1.2 Injection-to-larger
    - 5.1.3 Weighted FUNC
    - 5.1.4 Uniform weighted FUNC
    - 5.1.5 FUNC for subsets
    - 5.1.6 Disjoint intervals
    - 5.1.7 Strengthenings involving two families
    - 5.1.8 Abundant pairs

  - 5.2 Relationships between them

- 6 Structural theory
- 7 Important examples and constructions of examples
- 8 Discussion on Gowers's Weblog
- 9 Links

## Definitions

For any [math]\displaystyle{ x }[/math] in the ground set, write [math]\displaystyle{ \mathcal{A}_x = \{A \in \mathcal{A} : x \in A\} }[/math].

We say that [math]\displaystyle{ \mathcal{A} }[/math] is *separating*if for any two elements of the ground set there is a set in the family containing exactly one of them (in other words, if the [math]\displaystyle{ \mathcal{A}_x }[/math] are all distinct).

## Partial results

Let [math]\displaystyle{ \mathcal{A} }[/math] be a union-closed family of n sets, with a ground set of size m. It is known that Frankl's conjecture is true for the cases:

- [math]\displaystyle{ m \leq 12 }[/math]; or
- [math]\displaystyle{ n \leq 50 }[/math]; or
- [math]\displaystyle{ n \geq \frac23 2^m }[/math]; or
- [math]\displaystyle{ n \leq 4m-2 }[/math], assuming [math]\displaystyle{ \mathcal{A} }[/math] is separating; or
- [math]\displaystyle{ 0 \lt \lvert A \rvert \leq 2 }[/math] for some [math]\displaystyle{ A \in \mathcal{A} }[/math].
- [math]\displaystyle{ \mathcal{A} }[/math] contains three sets of three elements that are all subsets of the same five element set.

If [math]\displaystyle{ \mathcal{A} }[/math] is union-closed then there is an element [math]\displaystyle{ x }[/math] such that [math]\displaystyle{ \lvert \mathcal{A}_x \rvert \geq \frac{n-1}{\log_2 n} }[/math]. For large [math]\displaystyle{ n }[/math] this can be improved slightly to [math]\displaystyle{ \frac{2.4 n}{\log_2 n} }[/math].

## The m=13 case

Here is my work on the [m=13 case of FUNC][1]

## General proof strategies

- Find a strengthened hypothesis that permits an inductive proof
- [Find set configurations that imply FUNC][2]

## Strengthenings

Various strengthenings of FUNC have been proposed. Some have been disproved, and some implications between them have been shown.

### Conjectures that imply FUNC

##### Injection-to-superset

Is there always some [math]\displaystyle{ x \in X }[/math] and some injection [math]\displaystyle{ \phi : \mathcal{A}_{\bar{x}} \to \mathcal{A}_x }[/math] such that [math]\displaystyle{ A \subset \phi(A) }[/math] for all [math]\displaystyle{ A }[/math]? This was [answered in the negative][3].

##### Injection-to-larger

Is there always some [math]\displaystyle{ x \in X }[/math] and some injection [math]\displaystyle{ \phi : \mathcal{A}_{\bar{x}} \to \mathcal{A}_x }[/math] such that [math]\displaystyle{ \lvert A \rvert \lt \lvert \phi(A) \rvert }[/math] for all [math]\displaystyle{ A }[/math]?

##### Weighted FUNC

Let [math]\displaystyle{ f : \mathcal{A} \to \mathbb{R} }[/math] be such that [math]\displaystyle{ f(A) \geq 0 }[/math] for all [math]\displaystyle{ A }[/math] and [math]\displaystyle{ f(A) \leq f(B) }[/math] whenever [math]\displaystyle{ A \subseteq B }[/math]. Is there always an [math]\displaystyle{ x \in X }[/math] such that [math]\displaystyle{ \sum_{A : x \in A} f(A) \geq \sum_{A : x \notin A} f(A) }[/math]?

##### Uniform weighted FUNC

Is there always an [math]\displaystyle{ x \in X }[/math] such that [math]\displaystyle{ \sum_{A : x \in A} f(A) \geq \sum_{A : x \notin A} f(A) }[/math] for every [math]\displaystyle{ f : \mathcal{A} \to \mathbb{R} }[/math] such that [math]\displaystyle{ f(A) \geq 0 }[/math] for all [math]\displaystyle{ A }[/math] and [math]\displaystyle{ f(A) \leq f(B) }[/math] whenever [math]\displaystyle{ A \subseteq B }[/math]?

This is [equivalent][4] to the conjecture that there is some [math]\displaystyle{ x }[/math] that is abundant in every upper set in [math]\displaystyle{ \mathcal{A} }[/math].

This conjecture [is false][5].

##### FUNC for subsets

Is there for every [math]\displaystyle{ r }[/math] a subset [math]\displaystyle{ S \subseteq X }[/math] of size [math]\displaystyle{ r }[/math] such that [math]\displaystyle{ \lvert \{A \in \mathcal{A} : S \subseteq A\} \rvert \geq 2^{-r} \lvert \mathcal{A} \rvert }[/math]?

By recursively applying FUNC to [math]\displaystyle{ \mathcal{A}_x }[/math] for abundant [math]\displaystyle{ x }[/math], this can be seen to be equivalent to FUNC.

##### Disjoint intervals

Igor Balla [points out][6] that the following conjecture implies FUNC: suppose we have a collection of disjoint intervals [math]\displaystyle{ [A_i, B_i] = \{S : A_i \subseteq S \subseteq B_i\} }[/math] where [math]\displaystyle{ A_i \subseteq B_i }[/math], and the [math]\displaystyle{ B_i }[/math] form an upward-closed family in a ground set [math]\displaystyle{ X }[/math]. Then there is some [math]\displaystyle{ x \in X }[/math] belonging to at least half of the [math]\displaystyle{ A_i }[/math].

##### Strengthenings involving two families

One can look for strengthening that apply to [pairs of set systems][7] [math]\displaystyle{ \mathcal{A},\mathcal{B} }[/math] that satisfy some condition which specializes to union-closure in the case [math]\displaystyle{ \mathcal{A}=\mathcal{B} }[/math]. The idea is that it may be easier to [get an induction argument to work][8].

##### Abundant pairs

For any union-closed family [math]\displaystyle{ \mathcal{A} }[/math] on a ground set [math]\displaystyle{ X }[/math] with at least two elements there are two distinct elements [math]\displaystyle{ x, y\in X }[/math] such that the number of sets [math]\displaystyle{ A \in \mathcal A }[/math] containing neither [math]\displaystyle{ x }[/math] nor [math]\displaystyle{ y }[/math] is not larger than the number of sets [math]\displaystyle{ A \in \mathcal A }[/math] containing both [math]\displaystyle{ x }[/math] and [math]\displaystyle{ y }[/math]. Suggested [here][9].

### Relationships between them

Various implications between these conjectures [have been shown][10]. We have:

- injection-to-superset implies uniform weighted FUNC;
- uniform weighted FUNC implies weighted FUNC;
- uniform weighted FUNC implies injection-to-larger.

(These implications are only relevant in so far as they restrict the search space for counterexamples to the weaker conjectures.)

## Structural theory

There are various ways to investigate the structure of a union-closed family or of a finite lattice.

- [Horn clause formulation][11]
- [Lattice approach][12]

## Important examples and constructions of examples

Most basic:

- Power sets [math]\displaystyle{ \mathcal{A} = 2^X }[/math]
- Total orders: let [math]\displaystyle{ \mathcal{A} = \{1,12,123,\ldots,1\ldots n\} }[/math]
- Combinations of the previous two, as in the Duffus-Sands example

More sophisticated:

- [Renaud-Sarvate example][13]
- Examples based on [Steiner systems][14]

General constructions:

- [fibre bundle construction][15]
- Hom-lattices [math]\displaystyle{ \mathrm{Hom}(\mathcal{P},\mathcal{A}) }[/math], for [math]\displaystyle{ \mathcal{P} }[/math] a finite poset and [math]\displaystyle{ \mathcal{A} }[/math] a finite lattice. For example for [math]\displaystyle{ \mathcal{P} = \{0,1\} }[/math], the hom-lattice is the interval lattice of [math]\displaystyle{ \mathcal{A} }[/math].

## Discussion on Gowers's Weblog

- [Introductory post][16]
- [FUNC1][17]
- [FUNC2][15]
- [FUNC3][18]
- [FUNC4][19]

## Links

- A good [survey article][20]

Retrieved from " [https://michaelnielsen.org/polymath/index.php?title=Frankl%27s_union-closed_conjecture&oldid=9869][21] "

[Category][22]:

- [Frankl's union-closed sets conjecture][23]

## Navigation menu

### Page actions

- [Page][24]
- [Discussion][25]
- [Read][24]
- [View source][26]
- [History][27]

### Page actions

- [Page][24]
- [Discussion][25]
- More
- Tools

### Personal tools

- [Log in][28]

[29]

### Navigation

- [Main page][29]
- [Recent changes][30]
- [Random page][31]
- [Help about MediaWiki][32]

### Search

### Tools

- [What links here][33]
- [Related changes][34]
- [Special pages][35]
- Printable version
- [Permanent link][36]
- [Page information][37]

[image: Powered by MediaWiki] [38]

- This page was last edited on 27 October 2016, at 02:38.
- [Privacy policy][39]
- [About Polymath Wiki][40]
- [Disclaimers][41]


## Links

[1]: /polymath/index.php?title=M%3D13_case_of_FUNC
[2]: /polymath/index.php?title=Find_set_configurations_that_imply_FUNC
[3]: https://gowers.wordpress.com/2016/02/13/func3-further-strengthenings-and-variants/#comment-154441
[4]: https://gowers.wordpress.com/2016/02/13/func3-further-strengthenings-and-variants/#comment-154652
[5]: https://gowers.wordpress.com/2016/02/13/func3-further-strengthenings-and-variants/#comment-154685
[6]: https://gowers.wordpress.com/2016/01/21/frankls-union-closed-conjecture-a-possible-polymath-project/#comment-153911
[7]: https://gowers.wordpress.com/2016/02/22/func4-further-variants/#comment-154820
[8]: https://gowers.wordpress.com/2016/02/22/func4-further-variants/#comment-154825
[9]: https://gowers.wordpress.com/2016/02/22/func4-further-variants/#comment-154873
[10]: https://gowers.wordpress.com/2016/02/13/func3-further-strengthenings-and-variants/#comment-154651
[11]: /polymath/index.php?title=Horn_clause_formulation
[12]: /polymath/index.php?title=Lattice_approach
[13]: http://mathoverflow.net/a/228124/27013
[14]: https://gowers.wordpress.com/2016/01/29/func1-strengthenings-variants-potential-counterexamples/#comment-154069
[15]: https://gowers.wordpress.com/2016/02/08/func2-more-examples/
[16]: https://gowers.wordpress.com/2016/01/21/frankls-union-closed-conjecture-a-possible-polymath-project/
[17]: https://gowers.wordpress.com/2016/01/29/func1-strengthenings-variants-potential-counterexamples/
[18]: https://gowers.wordpress.com/2016/02/13/func3-further-strengthenings-and-variants/
[19]: https://gowers.wordpress.com/2016/02/22/func4-further-variants/
[20]: http://www.zaik.uni-koeln.de/~schaudt/UCSurvey.pdf
[21]: https://michaelnielsen.org/polymath/index.php?title=Frankl%27s_union-closed_conjecture&amp;oldid=9869
[22]: /polymath/index.php?title=Special:Categories
[23]: /polymath/index.php?title=Category:Frankl%27s_union-closed_sets_conjecture
[24]: /polymath/index.php?title=Frankl%27s_union-closed_conjecture
[25]: /polymath/index.php?title=Talk:Frankl%27s_union-closed_conjecture
[26]: /polymath/index.php?title=Frankl%27s_union-closed_conjecture&amp;action=edit
[27]: /polymath/index.php?title=Frankl%27s_union-closed_conjecture&amp;action=history
[28]: /polymath/index.php?title=Special:UserLogin&amp;returnto=Frankl%27s+union-closed+conjecture
[29]: /polymath/index.php?title=Main_Page
[30]: /polymath/index.php?title=Special:RecentChanges
[31]: /polymath/index.php?title=Special:Random
[32]: https://www.mediawiki.org/wiki/Special:MyLanguage/Help:Contents
[33]: /polymath/index.php?title=Special:WhatLinksHere/Frankl%27s_union-closed_conjecture
[34]: /polymath/index.php?title=Special:RecentChangesLinked/Frankl%27s_union-closed_conjecture
[35]: /polymath/index.php?title=Special:SpecialPages
[36]: /polymath/index.php?title=Frankl%27s_union-closed_conjecture&amp;oldid=9869
[37]: /polymath/index.php?title=Frankl%27s_union-closed_conjecture&amp;action=info
[38]: https://www.mediawiki.org/
[39]: /polymath/index.php?title=Polymath_Wiki:Privacy_policy
[40]: /polymath/index.php?title=Polymath_Wiki:About
[41]: /polymath/index.php?title=Polymath_Wiki:General_disclaimer
