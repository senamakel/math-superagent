<!-- source: https://doi.org/10.1016/j.jtusci.2015.02.008 | converted from HTML -->

Full article: On the number of real polynomials of the Casas-Alvero type

Skip to Main Content

[Advanced search][1]

[image: Publication Cover]

[Journal of Taibah University for Science][2] Volume 9, 2015 - [Issue 3][3]

[Submit an article][4] [Journal homepage][5]

Free access

427

Views

0

CrossRef citations to date

0

Altmetric

[Listen][6]

Original Article

# On the number of real polynomials of the Casas-Alvero type Footnote

Peer review under responsibility of Taibah University.

Footnote

Article submitted for the “Proceedings of the Workshop on Algebra and Applications” held in Fez, Morocco 18–21 June, 2014.

**[Mustapha Chellali][7] Université Mohamed Premier, Faculté des sciences, MathInfo, Oujda, Morocco Correspondence**[mustapha.chellali@gmail.com][8]

Pages 351-356 | Published online: 16 Apr 2018

- **Cite this article
- **[https://doi.org/10.1016/j.jtusci.2015.02.008][9]
- [image: CrossMark Logo] CrossMark

In this article**Article contents

**Related research

- Abstract
- 1 Casas-Alvero conjecture
- 2 Estimate of *u**n*
- 3 Algorithm for computing *u**n*
- 4 Other applications of Rolle graphs
- Footnotes
- References

- **[Full Article][10]
- **[Figures & data][11]
- **[References][12]
- **[Citations][13]
- **[Metrics][14]
- **[Reprints & Permissions][15]
- **[View PDF (open in a new window) PDF (open in a new window)][16]

Formulae display:[image: MathJax Logo]? Mathematical formulae have been encoded as MathML and are displayed in this HTML version using MathJax in order to improve their display. Uncheck the box to turn MathJax off. This feature requires Javascript. Click on a formula to zoom.

## Abstract

Let *K*be a field and *P*∈ *K*[*X*] is a polynomial of degree *n*, then the conjecture of Casas-Alvero states that if *P*is not prime with each of its *n*− 1 first derivatives, then it is a monomial, i.e., of the form *c*(*X*− *r*)*n*. We consider the case where K = ℝ and *P*is split over ℝ, where we show that the number *u**n*of hypothetical counterexamples of degree *n*satisfies (*n*− 4) ! ≤ *u**n*≤ *c*(*n*− 3)*n*−2, where c = 2 e − 1 ( ∏ n = 2 ∞ e − 1 ( ∑ k = 0 n 1 / k!)) 2 = 0.59373381 …. We also show how the Rolle theorem implies simply some previous results (see [Citation 1 – Citation 4]) and we improve them.

Keywords:

- [Polynomial][17]
- [Monomial][18]
- [Derivatives][19]
- [Roots][20]
- [Rolle theorem][21]
- [Graph][22]
- [Conjecture of Casas-Alvero][23]

## 1 Casas-Alvero conjecture

Let *K*be a field of characteristic 0. P ∈ K X if *P*= *c*(*X*− *α*)*m*is a monomial, and the nonconstant derivatives *P*′, *P*″, …, *P*(*m*−1) (*m*= *d*°(*P*)) have common roots with *P*. Casas-Alvero (2001) conjectured that the reverse statement is true. This question may appear to be easy but it is actually extremely difficult. It has been proved for *P*of degree *p**e*and 2*p**e*( p prime number, e ∈ ℕ) (cf [Citation 1] 2007). In this study, we consider the case where K = ℝ and *P*is split over ℝ, hence *P*′, *P*″, …, *P*(*m*−1) are also split over ℝ. With Rolle's theorem, it is easy to prove the conjecture until *d*°(*P*) ≤ 4. Unfortunately, for *d*°(*P*) ≥ 5, Rolle's theorem alone is not conclusive, which is shown by the following hypothetical counterexamples.

Table

[Download CSV][24] Display Table

Table

[Download CSV][25] Display Table

P = X 2 ( X − x 3) ( X − x 4) ( X − x 5) 0 < x 3 < x 4 < x 5

Display full size

We can ask whether are there many such hypothetical counterexamples for an arbitrary integer *n*. In the next section, we give an estimate of the number *u**n*of hypothetical counterexamples associated with the polynomial of the following form. P = X 2 ( X − x 3) ⋯ ( X − x n) 0 < x 3 < ⋯ < x n

In Section 3, we give an explicit algorithm for computing *u**n*. The first values of *u**n*show that *u**n*does not appear to be negligible compared with its bound (*n*− 3)*n*−2. In Section 3, we show how Rolle's theorem only implies some results of [Citation 2 – Citation 4], and we improve them.

## 2 Estimate of *u**n*

Let us begin by precisely defining the term “hypothetical counterexample.”

Definition 2.1

A Casas–Rolle graph with size *n*is a paired array of real numbers ( x i j) 0 ≤ j ≤ n, 1 ≤ i ≤ n − j and a map f: 2, 4, …, n − 1 → 3, 4, … n − 1 such that:

x 1 0 = x 1 1 = x 2 0 x i j < x i j + 1 < x i + 1 j if ( i, j) ≠ ( 1, 0) ( *) and

∀ j ∈ 2, 4, …, n − 1 x f ( j) 0 ∈ x 1 j, x 2 j, … x n − j j.

If *P*is a counterexample of the Casas-Alvero conjecture of the form:

P = X 2 ( X − x 3) ⋯ ( X − x n) 0 < x 3 < ⋯ < x n, then x i j represents the graph of zeros of the derivatives *P*(*j*) (0 ≤ *j*≤ *n*− 1), and the reverse is false, e.g., the Casas–Rolle graph of size 5 given in Section 1 cannot be associated with any polynomial of degree 5 because by the theorem of [Citation 1], such polynomials do not exist.

**Remarks**

1.  |

Regardless of the values of x i j, the only significant function is *f*that distributes the zeros of the first floor *j*= 0 to *j*= 2, 4, …, *n*− 1 floors, which satisfy the constraint of Rolle (*).

 |

2.  |

Roots located on the boundary: x 1 0 = x 2 0 and x n 0 are not sought in accordance with the constraints on Rolle's Theorem.

 |

3.  |

The second floor *j*= 1 is not important (the function *f*has no value for *j*= 1).

 |

4.  |

For a node x i j, four remarkable areas are distinguished, as follows.

 | (a)  |

The lower nodes x α β < x i j characterized by *α*≤ *i*and *α*+ *β*≤ *i*+ *j*and (*α*, *β*) ≠ (*i*, *j*) (which we denote as x α β ≪ x i j).

 |

 | (b)  |

The upper nodes x α β > x i j characterized by *α*≥ *i*and *α*+ *β*≥ *i*+ *j*and (*α*, *β*) ≠ (*i*, *j*) (which we denote as x α β ≫ x i j).

Note that the above order is related to the nodes and not to the values of nodes (which are variable), so we have

x α β ≪ x i j ⇒ x α β < x i j.

The reverse is false.

 |

 | (c)  |

The semi-ancestors x α β such that *α*> *i*and *α*+ *β*< *i*+ *j*.

 |

 | (d)  |

The semi-progeny x α β such that *α*< *i*and *α*+ *β*> *i*+ *j*.

 |

For the semi-ancestors or semi-progeny we cannot say anything about the comparison x α β, x i j; in particular, nothing can oppose there equality.

 |

Display full size

Definition 2.2

Two Casas–Rolle graphs are said to be equivalent if they are the same size and have the same map *f*. A Casas graph is any equivalence class of a Casas–Rolle graph.

Thus, the number of Casas graphs of size *n*is finite and at most 3, 4, …, n − 1 2, 3,, …, n − 1 = ( n − 3) n − 2.

Theorem 2.3

*Let u**n**be the number of Casas graphs of size n; thus, we have:*( n − 4)! ≤ u n < < c ( n − 3) n − 2,*where*c = 2 e − 1 ∏ n = 2 ∞ e − 1 ∑ k = 0 n 1 k! 2 = 0.59373381...

It is desirable that *u**n*is negligible compared with (*n*− 3)*n*−2, but numerically this does not appear to be the case.

To show that (*n*− 4) ! ≤ *u**n*, we require that the notion of a partial Casas graph is to complete step by step from the top. A Rolle graph is said to be partial Casas–Rolle to *m*(*m*≤ *n*− 1) if there is partial function f: 2, 4, …, m ⟶ 3, 4, … n − 1 that satisfies

∀ j ∈ 2, 4, …, m x f ( j) 0 ∈ x 1 j, x 2 j, … x n − j j.

Let x i j be a node of a partial Casas–Rolle graph that is not a root, i.e., such that x i j ≠ x f ( j) 0, where *f*is the function associated with the graph. We refer to the interval of the extension at the node x i j as the set of m ∈ 3, 4, …, n − 1 such that we can change the graph by replacing the value x i j by x m 0 while maintaining the partial Casas–Rolle property and the function *f*. We note that I i j and we naturally refer to a root node as a node x m 0 on the first floor or a node x i j such that the value “by *f*” is x f ( j) 0 = x i j. The following proposition justifies the term interval:

Proposition 2.4

I i j =] α, β [∩ ℕ*with*α = sup m | there is a root node x p q = x m 0 ≪ x i j*and*β = inf m | there is a root node x p q = x m 0 ≫ x i j*.*

For convenience, if x i j is a root x f ( j) 0, we set I i j = f ( j).

Proof of the Proposition

If we can replace x i j by the root x m 0, then we have either x i j ≪ x m 0 or x m 0 ≪ x i j, and thus *m*> *α*and *m*< *β*. Indeed, for example, if *m*≤ *α*because there is a root node x p q = x α 0 ≪ x i j, then we have x m 0 ≤ x α 0 < x i j = x m 0. Conversely, if *α*< *m*< *β*, suppose that, for example, x i j ≪ x m 0. By construction, the root x β 0 is attached to a node x r s ≫ x i j. Let D = x p q | x i j ≪ x p q and x p q < x β 0. We can check that *D*is a Rolle subgraph of the Rolle graph global *C*, because whenever it contains two adjacent nodes, it also contains their father and son nodes. However, by constructing *β*, the field *D*does not contain any root nodes (attached to a root) and we can then move x i j to the right to assign it the value x m 0 and the other nodes of *D*move right to a region x β 0 − ɛ < x p q < x β 0, which preserves their relationship (all of these moves are possible because *D*does not contain any fixed node). Next, we show that the Rolle graph has retained its overall structure as a Rolle graph. Since there has only been a move right, we simply check every node x a b for which the left son x a − 1 b + 1 has moved (right) between the two remaining sons. This is true by construction if x a b ∈ D, otherwise as x a − 1 b + 1 ∈ D ⟶ x i j ≪ x a b ⟶ x β ≤ x a b, and the right son x a b + 1 ∉ D; therefore, x a − 1 b + 1 < x β 0 ≤ x a b < x a b + 1. □

Proposition 2.5

*Let C a partial Casas–Rolle graph until m, let j*> *m for all i*≤ *n*− *j, let*I i j =] α, β [*and*I i + 1 j =] α ′, β ′ [*, then*I i j + 1 =] inf ( α, α ′), sup ( β, β ′) [*.*

Proof of the Proposition

We have x i j < x i j + 1 < x i + 1 j; therefore, for a root node x p q located above the floor *m*(i.e., *p*≤ *m*), we have x i j < x p q ⇔ x i j + 1 < x p q so if I i j + 1 =] α ″, β ″ [, we have *β*″ = sup(*β*, *β*′) and even *α*″ = inf(*α*, *α*′). □

Proof of the Theorem

To show that (*n*− 4) ! ≤ *u**n*, we note that any graph of Casas *C**k*of size *k*≤ *n*fits naturally in a graph of Casas *C**n*of size *n*in *n*− *k*+ 1 ways (which are distinct given the values of their function on the floor *k*). The *n*− *k*last floors of *C**n*still need to be assigned a root from the first floor, so we use the roots of *C**n*that are not located on the edge and not interior roots of *C**k*. Their number is exactly *n*− *k*, so if we let x i 1 < x i 2 < … < x i n − k be these roots, the floor *k*(the first floor of *C**n*\ *C**k*) has *n*− *k*nodes x 1 k, x 2 k … and a simple calculation by Proposition 2.4 shows that each *i**s*is in I s k ( x i s, see x i s). Therefore, we can choose x s k arbitrarily and fix it as x i s, before again ordering y i 1 < y i 2 < … < y i n − k − 1 as the roots that remain after selection. The floor *k*+ 1 has *n*− *k*− 1 nodes x 1 k + 1, x 2 k + 1 …, so by Proposition 2.5, each I s k + 1 has i s, i s + 1 before making a choice, which necessarily contains the new *i**s*after selection, and thus we find ourselves in the same position as described previously. By recursion, we can see that we have (*n*− *k*) ! ways to complete *C**k*, then *u**n*≥ (*n*− *k*+ 1) ! *u**k*with *k*= 5 (we now have *u*5 = 1), which gives the inequality (we can try to iterate the inequality *u**n*≥ (*n*− *k*+ 1) ! *u**k*to obtain a better inequality than *u**n*≥ (*n*− 4) !, but this does not work because we always have *a*1! *a*2! … *a**k*! ≤ (*a*1 + *a*2 + … + *a**k*)) ! □

We show the other inequality, as follows.

Lemma 2.6

*Let C a Casas graph of size n and let*f: 2, 3, …, n − 1 ⟶ 3, 4, …, n − 1*be the associated sharing function. For k*= 3, 4, …, *n*− 1*, we have:*

| f − 1 k | ≤ inf ( k − 1, n − k).

Proof of the Lemma

If the root x k 0 is shared at the floors *j*1, *j*2, …, *j**t*in the positions x i 1 j 1, x i 2 j 2, …, x i t j t, then it is mandatory that each position is the semi-progeny of the previous one; otherwise, it will not be equal, so:

1 ≤ i t < i t − 1 < … < i 1 < m and

m < i 1 + j 1 < i 2 + j 2 < … < i t + j t ≤ n.

Therefore, *t*≤ *m*− 1 and *t*≤ *n*− *m*. □

Proof of the second inequality

From the lemma, a simple count shows the following. Let:

E = ( i 3, …, i n − 1) ∈ ℕ n − 3 | i 3 + … + i n − 1 = n − 2 0 ≤ i k ≤ inf ( k − 1, n − k) u n ≤ ∑ ( i 3, …, i n − 1) ∈ E n − 2 i 1 n − 2 − i 1 i 2 … n − 2 − i 1 − i 2 − … − i n − 2 i n − 1, that is,

u n ≤ ∑ ( i 3, …, i n − 1) ∈ E ( n − 2)! i 1! i 2! … i n − 1!.

Note that inf(*k*− 1, *n*− *k*) is invariant under change *k*⟷ *n*− *k*+ 1. We will impose the restriction *i**k*≤ inf(*k*− 1, *n*− *k*) that can only be a constant number of *i**k*and we free others. For an integer *k*∈ [3, (*n*+ 1/2)] fixé, let A k = 3, 4, …, k ∪ n − 2, n − 3, … n − k + 1 ∪ n − 1. Let E k = ( i 3, …, i n − 1) ∈ ℕ n − 3 | i 3 + … + i n − 1 = n − 2 0 ≤ i s ≤ inf ( s − 1, n − s) if s ≤ A k.

As *E*⊂ *E**k*, we have:

u n ≤ ∑ ( i 3, …, i n − 1) ∈ E k ( n − 2)! i 1! i 2! … i n − 1!.

If we let B = ∏ s = 2 k − 1 [0, s] 2 × [0, 1], then the sum above is written as

∑ ( s 1, s 2, …, s 2 k − 3) ∈ B 1 s 1! s 2! … s 2 k − 3! ( n − 2)! ( n − 2 − ∑ s i)! ( n − 2 − ( 2 k − 3)) n − 2 − ∑ s i.

If we divide by (*n*− 3)*n*−2 and let *n*⟶ ∞, then we obtain

u n / ( n − 3) n − 2 < < 2 e − 1 ∏ s = 2 k − 1 e − 1 1 + 1 1! ⋯ + 1 s! 2.

Hence, by *k*⟶ ∞ the inequality □

## 3 Algorithm for computing *u**n*

The algorithm is based on Proposition 2.4, where on each node, we are given the interval of the roots that can be fixed (pinned) on the node and that can even distort the graph, but without touching the already pinned nodes. However, the graph remains a Rolle graph. The algorithm is recursive and it explores all of the possibilities from top to bottom and from left to right.

1.  |

For each floor *j*= 2, …, *n*− 1 do

 |

2.  |

For each node *i*= 1, 2, . . . . , *n*− *j*do

 |

3.  |

For each root m ∈ I i j do

 | (a)  |

fix (pin up) the node x i j to the value x m 0

 |

 | (b)  |

If *j*= *n*− 1 it is a success, keep the combination of roots if it has not been found already; else, update the extension intervals of the floor *j*+ 1

 |

 |

The algorithm fails when browsing a floor *j*it finds that all of the extension intervals are empty, and thus it then looks recursively at the next node.

Remark 1

Updating the extension interval is very easy using Proposition 2.5.

For example, 4543 means that we have to pin to the root x 4 0 at the floor 2, the root x 5 0 at the floor 3, the root x 4 0 at the floor 4, and the root x 3 0 at the floor 5.

Display full size

For *n*≤ 10, the values of *u**n*clearly suggest that *u**n*is not negligible before (*n*− 3) (*n*−2).

## 4 Other applications of Rolle graphs

We now return to the notion of more general Rolle graphs.

Definition 4.1

We call a Rolle graph of size *n*( n ∈ ℕ ≥ 2) a triangular data of a real number ( x i j) 0 ≤ j ≤ n − 1, 1 ≤ i ≤ n − j such that:

∀ j = 0, 1, …, n − 2 ∀ i = 1, 2, …, n − j − 1 x i j + 1 = x i j = x i + 1 j if x i j = x i + 1 j x i j + 1 < x i j + 1 < x i + 1 j if x i j ≠ x i + 1 j.

As in the previous paragraph, for a node x i j, we define the following.

•  |

The proper right fathers of the node x i j: x p q | p + q = i + j et q ≤ j.

 |

•  |

The proper left fathers of the node x i j: x p q | p = i et q ≤ j.

 |

•  |

The semi-ancestors of x i j:

x p q | p ≥ i and p + q ≤ i + j.

 |

•  |

The semi-progeny of x i j:

x p q | p ≤ i and p + q ≥ i + j.

 |

•  |

The lower nodes of x i j:

x p q | p ≤ i and p + q ≤ i + j.

 |

•  |

The upper nodes of x i j:

x p q | p ≥ i and p + q ≥ i + j.

 |

Proposition 4.2

*If in a Rolle graph, the proper right fathers of a node coincide with the proper left fathers of this node, then all of the ancestors (proper and improper) of this node coincide.*As immediate consequence (see also [Citation 6]):

Corollary 4.3

*If a polynomial of degree n which split over*ℝ*has one derivative of order*>*n*− 1 *monomial, then it is a monomial.*

Definition 4.4

A polynomial of degree *n*is said to be Casas if it has a common root with each of its non-constant derivatives.

As immediate consequences of the properties of a Rolle graph, we have the following (see also [Citation 5]).

Proposition 4.5

*Let P a Casas polynomial which split over*ℝ*, then the number of roots of P is*≠ *2.*

Proof

Suppose that *P*= (*X*− *α*)*m*(*X*− *β*)*n*with *α*< *β*and *n*, *m*> 0, and let *s*= sup(*n*, *m*), then the derivative of order *s*has a root ∈]*α*, *β*[ in common with *P*, which is absurd □

As further immediate consequences of the properties of a Rolle graph, we have the following.

Proposition 4.6

*Let P a Casas polynomial which split over*ℝ*, then the number of roots of P is*≠3*.*

Proof

Suppose that *P*= (*X*− *α*)*p*(*X*− *β*)*q*(*X*− *γ*)*r*with *α*< *β*< *γ*and *p*, *q*, *r*> 0. If we let *s*= sup(*p*, *q*, *r*) and we have *s*≠ *n*− 1, then the derivatives of order *s*and *s*+ 1 have a common root with *P*and necessarily = *β*, and then *β*is a multiple root of *P**s*. By Proposition 4.2, *β*is a root of order *s*+ of *P*, which is a contradiction.□

We may surmise that for all *k*, N k ∈ ℕ exist such that every Casas polynomial of degree *n*> *N**k*cannot have exactly *k*roots. Unfortunately, due to the properties of Rolle graphs alone, we cannot prove this result, as shown by the following counterexample, where *k*= and any n ∈ ℕ.

Display full size

However, using methods analogous to those described by [Citation 3], we can prevent this case.

We end with the following result, the proof of which is purely elementary.

Proposition 4.7

*There is no Casas polynomial of the form Q**m**with*Q ∈ ℂ X*of degree*≥2 *such that all of the roots are distinct.*

Proof

If not, there will be a root *α*in common with *P*(*m*), but *α*would then be a root of order *m*+ 1, so (*X*− *α*)*m*+1 |*P*, which is a contradiction.□

Corollary 4.8

*If a Casas polynomial is of the form Q**n*/2*with n*= *d*°(*P*)*, then it is a monomial.*

## Notes

Article submitted for the “Proceedings of the Workshop on Algebra and Applications” held in Fez, Morocco 18–21 June, 2014.

Peer review under responsibility of Taibah University.

## References

- H.-C. graf von Bothmer, O. Labs, J. Schicho, C. Van de Woestijne, The Casas-Alvero Conjecture for Infinitely Many Degrees, [http://arxiv.org/abs/math/0605090v2 (open in a new window)][26].

[(Open in a new window) Google Scholar][27]

- W. Castryck, R. Laterveer, M. Ounaies, Constraints on Counter Examples to the Casas-Alvero Conjecture, and a Verification in Degree 12, [http://arxiv.org/abs/1208.5404 (open in a new window)][28].

[(Open in a new window) Google Scholar][29]

- R. Laterveer, M. Ounaïes, Constraints on Hypothetical Counterexamples to the Casas-Alvero Conjecture, [http://arxiv.org/abs/1204.0450 (open in a new window)][30].

[(Open in a new window) Google Scholar][31]

- T.PolstraConvex Hulls and the Casas-Alvero Conjecture for the complex plane Rose–Hulman Undergrad. Math. J. 13120123242 Spring

[(Open in a new window) Google Scholar][32]

- JanDraismaJohan P.JongOn the Casas-Alvero conjecture. (English) Eur. Math. Soc. Newsl. 8020112933 MSC2000: *37-99 30-99

[(Open in a new window) Google Scholar][33]

- S. Yakubovich, Polynomial problems of the Casas-Alvero type. arXiv:1308.5320.

[(Open in a new window) Google Scholar][34]

Please note: Selecting permissions **does not**provide access to the full text of the article,
please see our help page [How do I view content?][35]

### Academic Permissions

Obtain permissions instantly via Rightslink by clicking on the button below:

[Request Academic Permissions][36]

For more information, please visit our [Permissions help page][37].

### Corporate Permissions

To request corporate permissions for this article, please click on the button below:

[Request Corporate Permissions][38]

### Reprints

To request a reprint for this article, please click on the button below:

[Order Reprints][36]

[Download PDF][39]

-

**[Share][40]

- Back to Top**

## Related research

**People also read**lists articles that other readers of this article have read.

**Recommended articles**lists articles that we recommend and is powered by our AI driven recommendation engine.

**Cited by**lists all citing articles based on Crossref citations.
Articles with the Crossref icon will open in a new tab.

- People also read
- Recommended articles
- Cited by

[41]

## Your download is now in progress and you may close this window

Did you know that with a free Taylor & Francis Online account you can gain access to the following benefits?

- **Choose new content alerts to be informed about new research of interest to you
- **Easy remote access to your institution's subscriptions on any device, from any location
- **Save your searches and schedule alerts to send you new results
- **Export your search results into a .csv file to support your research

Have an account?
[Login now][42] Don't have an account?
[Register for free][43]

## Save your searches

and schedule alerts to send you new results.

[Register for free][43] [Login now][44]

View all benefits of registration**

- **Choose new content alerts to be informed about new research of interest to you
- **Export your search results into a .csv file to support your research
- **Save your searches and schedule alerts to send you new results


## Links

[1]: /search/advanced
[2]: /journals/tusc20
[3]: /toc/tusc20/9/3
[4]: https://rp.tandfonline.com/submission/create?journalCode#x3D;TUSC
[5]: /tusc20
[6]: //app-eu.readspeaker.com/cgi-bin/rsent?customerid=10118&amp;lang=en_us&readclass=rs_readArea&url=https%3A%2F%2Fwww.tandfonline.com%2Fdoi%2Ffull%2F10.1016%2Fj.jtusci.2015.02.008
[7]: /author/Chellali%2C+Mustapha
[8]: mailto:mustapha.chellali@gmail.com
[9]: https://doi.org/10.1016/j.jtusci.2015.02.008
[10]: /doi/full/10.1016/j.jtusci.2015.02.008?scroll=top&amp;needAccess=true
[11]: /doi/figure/10.1016/j.jtusci.2015.02.008?scroll=top&amp;needAccess=true
[12]: /doi/ref/10.1016/j.jtusci.2015.02.008?scroll=top
[13]: /doi/citedby/10.1016/j.jtusci.2015.02.008?scroll=top&amp;needAccess=true
[14]: /doi/metrics/10.1016/j.jtusci.2015.02.008?scroll=top
[15]: /doi/permissions/10.1016/j.jtusci.2015.02.008?scroll=top
[16]: /doi/epdf/10.1016/j.jtusci.2015.02.008?needAccess=true
[17]: /keyword/Polynomial
[18]: /keyword/Monomial
[19]: /keyword/Derivatives
[20]: /keyword/Roots
[21]: /keyword/Rolle+theorem
[22]: /keyword/Graph
[23]: /keyword/Conjecture+of+Casas-Alvero
[24]: /action/downloadTable?id=T0005&amp;doi=10.1016%2Fj.jtusci.2015.02.008&amp;downloadType=CSV
[25]: /action/downloadTable?id=T0010&amp;doi=10.1016%2Fj.jtusci.2015.02.008&amp;downloadType=CSV
[26]: https://arxiv.org/pdf/math/0605090v2
[27]: /action/getFTRLinkout?url=http%3A%2F%2Fscholar.google.com%2Fscholar%3Fhl%3Den%26q%3DH.-C.%2Bgraf%2Bvon%2BBothmer%252C%2BO.%2BLabs%252C%2BJ.%2BSchicho%252C%2BC.%2BVan%2Bde%2BWoestijne%252C%2BThe%2BCasas-Alvero%2BConjecture%2Bfor%2BInfinitely%2BMany%2BDegrees%252C%2B.&doi=10.1016%2Fj.jtusci.2015.02.008&doiOfLink=&linkType=gs&linkLocation=Reference&linkSource=FULL_TEXT
[28]: https://arxiv.org/pdf/1208.5404
[29]: /action/getFTRLinkout?url=http%3A%2F%2Fscholar.google.com%2Fscholar%3Fhl%3Den%26q%3DW.%2BCastryck%252C%2BR.%2BLaterveer%252C%2BM.%2BOunaies%252C%2BConstraints%2Bon%2BCounter%2BExamples%2Bto%2Bthe%2BCasas-Alvero%2BConjecture%252C%2Band%2Ba%2BVerification%2Bin%2BDegree%2B12%252C%2B.&doi=10.1016%2Fj.jtusci.2015.02.008&doiOfLink=&linkType=gs&linkLocation=Reference&linkSource=FULL_TEXT
[30]: https://arxiv.org/pdf/1204.0450
[31]: /action/getFTRLinkout?url=http%3A%2F%2Fscholar.google.com%2Fscholar%3Fhl%3Den%26q%3DR.%2BLaterveer%252C%2BM.%2BOuna%25C3%25AFes%252C%2BConstraints%2Bon%2BHypothetical%2BCounterexamples%2Bto%2Bthe%2BCasas-Alvero%2BConjecture%252C%2B.&doi=10.1016%2Fj.jtusci.2015.02.008&doiOfLink=&linkType=gs&linkLocation=Reference&linkSource=FULL_TEXT
[32]: /action/getFTRLinkout?url=http%3A%2F%2Fscholar.google.com%2Fscholar_lookup%3Fhl%3Den%26volume%3D13%26publication_year%3D2012%26pages%3D32-42%26journal%3DRose%25E2%2580%2593Hulman%2BUndergrad.%2BMath.%2BJ.%26issue%3D1%26author%3DT.%2BPolstra%26title%3DConvex%2BHulls%2Band%2Bthe%2BCasas-Alvero%2BConjecture%2Bfor%2Bthe%2Bcomplex%2Bplane&doi=10.1016%2Fj.jtusci.2015.02.008&doiOfLink=&linkType=gs&linkLocation=Reference&linkSource=FULL_TEXT
[33]: /action/getFTRLinkout?url=http%3A%2F%2Fscholar.google.com%2Fscholar_lookup%3Fhl%3Den%26volume%3D80%26publication_year%3D2011%26pages%3D29-33%26journal%3DEur.%2BMath.%2BSoc.%2BNewsl.%26author%3DJan%2BDraisma%26author%3DJohan%2BP.%2BJong%26title%3DOn%2Bthe%2BCasas-Alvero%2Bconjecture.%2B%2528English%2529&doi=10.1016%2Fj.jtusci.2015.02.008&doiOfLink=&linkType=gs&linkLocation=Reference&linkSource=FULL_TEXT
[34]: /action/getFTRLinkout?url=http%3A%2F%2Fscholar.google.com%2Fscholar%3Fhl%3Den%26q%3DS.%2BYakubovich%252C%2BPolynomial%2Bproblems%2Bof%2Bthe%2BCasas-Alvero%2Btype.%2BarXiv%253A1308.5320.&doi=10.1016%2Fj.jtusci.2015.02.008&doiOfLink=&linkType=gs&linkLocation=Reference&linkSource=FULL_TEXT
[35]: https://help.tandfonline.com/s/article/How-do-I-view-content
[36]: 
[37]: https://help.tandfonline.com/Librarian/s/article/Permissions
[38]: /action/requestPermissions?doi=10.1016/j.jtusci.2015.02.008&amp;typesOfUse=Corporate&amp;start=true
[39]: https://www.tandfonline.com/doi/pdf/10.1016/j.jtusci.2015.02.008
[40]: https://www.addtoany.com/share
[41]: /action/showCitFormats?doi=10.1016/j.jtusci.2015.02.008
[42]: /action/showLogin?uri=
[43]: /action/registration?redirectUri=
[44]: /action/showLogin?redirectUri=
