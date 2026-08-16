<!-- source: https://arxiv.org/html/2501.02637v3 | converted from HTML -->

Isomorphism in Union-Closed Sets

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: CC BY-NC-SA 4.0][2]

arXiv:2501.02637v3 [math.CO] 19 Sep 2025

# Isomorphism in Union-Closed Sets

Mohammad Javad Moghaddas Mehr Thanks: m.moghadas11235@gmail.com

January 5, 2025

###### Abstract

We prove that for any isomorphism h: 𝒦 1 → 𝒦 2 h:\mathcal{K}_{1}\to\mathcal{K}_{2} between pure union-closed families, there exists a hyperisomorphism H: ⋃ 𝒦 1 → ⋃ 𝒦 2 H:\bigcup\mathcal{K}_{1}\to\bigcup\mathcal{K}_{2} such that h ⁡ ( A) = { H ⁡ ( a) ∣ a ∈ A } h(A)=\{H(a)\mid a\in A\}, for all A ∈ 𝒦 1 A\in\mathcal{K}_{1}. Since every union-closed family forms a lattice under inclusion, this result establishes a strong connection between the two frameworks. More precisely, any such family can be uniquely reconstructed from its lattice up to isomorphism. Hence, the lattice representation provides a faithful encoding, offering a perspective that may yield new insights into problems on union-closed families, including Frankl’s union-closed sets conjecture.

Keywords: union-closed sets, lattice theory, hyperisomorphism, isomorphism, Frankl’s conjecture

## 1 Introduction

###

The motivation for this paper arose while studying structural properties of union-closed families, which revealed a strong connection between union-closed families and lattices. It is straightforward to show that any union-closed family containing the empty set can be uniquely represented as a lattice under set inclusion. Together with Theorem 4.1, this suggests that a lattice-theoretic approach can be highly effective in investigating properties of union-closed families. More precisely, converting a union-closed family into a lattice structure preserves all essential information about the family.

One of the central open questions concerning union-closed families is Frankl’s conjecture [11], which states that for any finite union-closed family there exists an element that belongs to at least half of the sets in the family. Despite decades of effort, the conjecture remains unresolved; see, for example, [5, 18, 13, 10, 6, 22, 4, 16, 8, 12, 17, 7] for background and recent progress.

In fact, the lattice formulation of Frankl’s conjecture has already been established for several important classes. Rival first observed that the conjecture holds for distributive and geometric lattices (without proof) [21], and Poonen later gave a complete proof and extended the result to relatively complemented lattices [19]. Abe and Nakano proved the conjecture for modular lattices [2], while Reinhold established it for lower semimodular lattices [20], which remains the strongest known result for a standard lattice class. Abe and Nakano also showed it for lower quasi-semimodular lattices [3], and Czédli and Schmidt confirmed it for large semimodular lattices and for planar semimodular lattices [9]. Joshi, Waphare, and Kavishwar proved the conjecture for dismantlable lattices, from which they derived as corollaries the cases of upper semimodular lattices of breadth at most two [15]. Later, Joshi and Waphare explicitly established the conjecture for all lattices of breadth two [14]. Independently, Abdollahi, Woodroofe, and Zaimi proved the conjecture for subgroup lattices of finite groups and, more generally, for lattices with a modular coatom—a class that includes supersolvable and dually semimodular lattices [1].

In the next section, we introduce the basic concepts needed for the proof of Theorem 4.1, which states that for every isomorphism h: 𝒦 1 → 𝒦 2 h:\mathcal{K}_{1}\to\mathcal{K}_{2} between two pure union-closed families of sets, there exists a corresponding hyperisomorphism H: ⋃ 𝒦 1 → ⋃ 𝒦 2 H:\bigcup\mathcal{K}_{1}\to\bigcup\mathcal{K}_{2} such that h ⁡ ( A) = { H ⁡ ( a) ∣ a ∈ A }, ∀ A ∈ 𝒦 1. h(A)=\{H(a)\mid a\in A\},\hskip 9.24994pt\forall\,A\in\mathcal{K}_{1}.

## 2 Preliminaries

###

For an integer n ∈ ℕ n\in\mathbb{N}, we define [n]:= { k ∈ ℕ ∣ k ≤ n } [n]:=\{k\in\mathbb{N}\mid k\leq n\}. A family 𝒦 ⊆ 2 [n] \mathcal{K}\subseteq 2^{[n]} is called union-closed if for all A, B ∈ 𝒦 A,B\in\mathcal{K}, it holds that A ∪ B ∈ 𝒦 A\cup B\in\mathcal{K}. A lattice is a poset ( L, ≤) (L,\leq) in which any two elements of L L have a unique meet and a unique join.

###### Definition 2.1 (Homomorphism).

Let 𝒦 1 \mathcal{K}_{1} and 𝒦 2 \mathcal{K}_{2} be union-closed families of sets. A mapping h: 𝒦 1 → 𝒦 2 h:\mathcal{K}_{1}\to\mathcal{K}_{2} is called a homomorphism if, for all A 1, A 2 ∈ 𝒦 1 A_{1},A_{2}\in\mathcal{K}_{1}, the following holds:

 | h ⁡ ( A 1 ∪ A 2) = h ⁡ ( A 1) ∪ h ⁡ ( A 2). h(A_{1}\cup A_{2})=h(A_{1})\cup h(A_{2}). |  |

###### Definition 2.2 (Isomorphism).

Let 𝒦 1 \mathcal{K}_{1} and 𝒦 2 \mathcal{K}_{2} be union-closed families of sets. A homomorphism h: 𝒦 1 → 𝒦 2 h:\mathcal{K}_{1}\to\mathcal{K}_{2} is called an isomorphism if it is bijective.

###

It is straightforward to see that any union-closed family containing the empty set forms a lattice under inclusion. In this way, homomorphisms and isomorphisms of families correspond exactly to homomorphisms and isomorphisms of the associated lattices.

###### Lemma 2.1.

Let 𝒦 1 \mathcal{K}_{1} and 𝒦 2 \mathcal{K}_{2} be two union-closed families, and h: 𝒦 1 → 𝒦 2 h:\mathcal{K}_{1}\to\mathcal{K}_{2} be a homomorphism between them. If A 1, A 2 ∈ 𝒦 1 A_{1},A_{2}\in\mathcal{K}_{1} such that A 1 ⊆ A 2 A_{1}\subseteq A_{2}, then:

 | h ⁡ ( A 1) ⊆ h ⁡ ( A 2). h(A_{1})\subseteq h(A_{2}). |  |

###### Proof.

By the homomorphism property, we have:

 | h ⁡ ( A 2) = h ⁡ ( A 1 ∪ A 2) = h ⁡ ( A 1) ∪ h ⁡ ( A 2). h(A_{2})=h(A_{1}\cup A_{2})=h(A_{1})\cup h(A_{2}). |  |

Thus, h ⁡ ( A 1) ⊆ h ⁡ ( A 2) h(A_{1})\subseteq h(A_{2}). ∎

###### Corollary 2.1.

Let 𝒦 1 \mathcal{K}_{1} and 𝒦 2 \mathcal{K}_{2} be two union-closed families, and h: 𝒦 1 → 𝒦 2 h:\mathcal{K}_{1}\to\mathcal{K}_{2} be an isomorphism between them. If A 1, A 2 ∈ 𝒦 1 A_{1},A_{2}\in\mathcal{K}_{1} such that A 1 ⊂ A 2 A_{1}\subset A_{2}, then:

 | h ⁡ ( A 1) ⊂ h ⁡ ( A 2). h(A_{1})\subset h(A_{2}). |  |

###### Lemma 2.2.

Let 𝒦 \mathcal{K} be a union-closed family of sets, and h: 𝒦 → 2 [n] h:\mathcal{K}\to 2^{[n]} be a homomorphism. Then the image of 𝒦 \mathcal{K} under h h forms a union-closed family of sets.

###### Proof.

Let B 1, B 2 ∈ h ⁡ ( 𝒦) B_{1},B_{2}\in h(\mathcal{K}). Then there exist A 1, A 2 ∈ 𝒦 A_{1},A_{2}\in\mathcal{K} such that B 1 = h ⁡ ( A 1) B_{1}=h(A_{1}) and B 2 = h ⁡ ( A 2) B_{2}=h(A_{2}). Therefore:

 | B 1 ∪ B 2 = h ⁡ ( A 1) ∪ h ⁡ ( A 2) = h ⁡ ( A 1 ∪ A 2). B_{1}\cup B_{2}=h(A_{1})\cup h(A_{2})=h(A_{1}\cup A_{2}). |  |

Thus, B 1 ∪ B 2 ∈ h ⁡ ( 𝒦) B_{1}\cup B_{2}\in h(\mathcal{K}), proving that h ⁡ ( 𝒦) h(\mathcal{K}) is union-closed. ∎

###### Corollary 2.2.

Let 𝒦 \mathcal{K} be a union-closed family of sets, and h: 𝒦 → 2 [n] h:\mathcal{K}\to 2^{[n]} be an injective homomorphism. Then h: 𝒦 → h ⁡ ( 𝒦) h:\mathcal{K}\to h(\mathcal{K}) is an isomorphism.

###### Definition 2.3 (Redundant Element).

Let 𝒦 ⊆ 2 [n] \mathcal{K}\subseteq 2^{[n]}. An element z ∈ ⋃ 𝒦 z\in\bigcup\mathcal{K} is called redundant, if removing z z from every set in 𝒦 \mathcal{K} does not reduce the cardinality of the collection. Specifically, we define:

 | 𝒦 ∖ z = { X ∖ { z } ∣ X ∈ 𝒦 }, \mathcal{K}^{\setminus z}=\{X\setminus\{z\}\mid X\in\mathcal{K}\}, |  |

where | 𝒦 | = | 𝒦 ∖ z | |\mathcal{K}|=|\mathcal{K}^{\setminus z}|. The collection 𝒦 ∖ z \mathcal{K}^{\setminus z} is called the reduced collection.

###### Definition 2.4 (Pure Collection).

A collection 𝒦 ⊆ 2 [n] \mathcal{K}\subseteq 2^{[n]} is called pure if it does not have any redundant element.

###

The next step is to remove redundant elements from a collection. Eliminating one element can change whether others remain redundant, so the process must be carried out iteratively until no redundant elements remain. The result of this process may depend on the order in which elements are removed. Corollary 2.3 shows, however, that all such outcomes are isomorphic. We therefore speak of the purified collection of 𝒦 \mathcal{K}, denoted by 𝒦 ∗ \mathcal{K}^{*}. If 𝒦 \mathcal{K} is already pure, then clearly 𝒦 = 𝒦 ∗ \mathcal{K}=\mathcal{K}^{*}.

###### Lemma 2.3.

Let 𝒦 \mathcal{K} be a union-closed family of sets, and z z be a redundant element of 𝒦 \mathcal{K}. Then there exists an isomorphism between 𝒦 \mathcal{K} and 𝒦 ∖ z \mathcal{K}^{\setminus z}.

###### Proof.

Define h: 𝒦 → 𝒦 ∖ z h:\mathcal{K}\to\mathcal{K}^{\setminus z} by h ⁡ ( A) = A ∖ { z } h(A)=A\setminus\{z\}. Let A, B ∈ 𝒦 A,B\in\mathcal{K}. Then:

 | h ⁡ ( A ∪ B) = ( A ∪ B) ∖ { z } = ( A ∖ { z }) ∪ ( B ∖ { z }) = h ⁡ ( A) ∪ h ⁡ ( B). h(A\cup B)=(A\cup B)\setminus\{z\}=(A\setminus\{z\})\cup(B\setminus\{z\})=h(A)\cup h(B). |  |

This shows that h h preserves the union operation, so h h is a homomorphism. It is clear that h h is surjective because every element of 𝒦 ∖ z \mathcal{K}^{\setminus z} is of the form A ∖ { z } A\setminus\{z\} for some A ∈ 𝒦 A\in\mathcal{K}. To show that h h is injective, suppose h ⁡ ( A) = h ⁡ ( B) h(A)=h(B) for some A, B ∈ 𝒦 A,B\in\mathcal{K}. This implies:

 | A ∖ { z } = B ∖ { z }. A\setminus\{z\}=B\setminus\{z\}. |  |

If A ≠ B A\neq B, removing z z would change the size of 𝒦 \mathcal{K}, contradicting the assumption that z z is a redundant element. Thus, A = B A=B, which implies that h h is injective. Since h h is both a homomorphism and a bijection, it follows that h h is an isomorphism between 𝒦 \mathcal{K} and 𝒦 ∖ z \mathcal{K}^{\setminus z}. ∎

###### Corollary 2.3.

For any union-closed family 𝒦 \mathcal{K}, there exists an isomorphism h: 𝒦 → 𝒦 ∗ h:\mathcal{K}\to\mathcal{K}^{*}.

## 3 Cardinality Theorem

###

This section establishes the Cardinality Theorem, which we will use in the proof of the main theorem. We first record some terminology and supporting lemmas.

###### Definition 3.1.

Let 𝒦 ⊆ 2 [n] \mathcal{K}\subseteq 2^{[n]} be a poset under set inclusion. An element X ∈ 𝒦 X\in\mathcal{K} is called minimal if it has no proper subset in 𝒦 \mathcal{K}. The set of all minimal elements in 𝒦 \mathcal{K} is denoted by 𝒦 ⊥ \mathcal{K}^{\bot} and is defined as:

 | 𝒦 ⊥ = { X ∈ 𝒦 ∣ ∄ A ∈ 𝒦 such that A ⊂ X }. \mathcal{K}^{\bot}=\{X\in\mathcal{K}\mid\nexists A\in\mathcal{K}\text{ such that }A\subset X\}. |  |

Figure 1: Two lattice diagrams; the red nodes are the elements of 𝒦 ⊥ \mathcal{K}^{\bot}.

###### Lemma 3.1.

Let 𝒦 \mathcal{K} be a union-closed family, and X ∈ 𝒦 ⊥ X\in\mathcal{K}^{\bot}. Then 𝒦 ∖ { X } \mathcal{K}\setminus\{X\} is also union-closed.

###### Proof.

Since X X is minimal, no member of 𝒦 ∖ { X } \mathcal{K}\setminus\{X\} is contained in X X; hence if A, B ∈ 𝒦 ∖ { X } A,B\in\mathcal{K}\setminus\{X\} then A ∪ B ≠ X A\cup B\neq X. Because 𝒦 \mathcal{K} is union-closed, A ∪ B ∈ 𝒦 A\cup B\in\mathcal{K}, and therefore A ∪ B ∈ 𝒦 ∖ { X } A\cup B\in\mathcal{K}\setminus\{X\}. ∎

###### Lemma 3.2.

Let 𝒦 1 \mathcal{K}_{1} and 𝒦 2 \mathcal{K}_{2} be union-closed families, and h: 𝒦 1 → 𝒦 2 h:\mathcal{K}_{1}\to\mathcal{K}_{2} be an isomorphism between them. If X X is a minimal element of 𝒦 1 \mathcal{K}_{1}, then h ⁡ ( X) h(X) is a minimal element of 𝒦 2 \mathcal{K}_{2}.

###### Proof.

Assume, for contradiction, that h ⁡ ( X) h(X) is not minimal in 𝒦 2 \mathcal{K}_{2}. Then there exists B ∈ 𝒦 2 B\in\mathcal{K}_{2} with B ⊂ h ⁡ ( X) B\subset h(X). Since h h is surjective, there is some A ∈ 𝒦 1 A\in\mathcal{K}_{1} such that h ⁡ ( A) = B h(A)=B. Clearly A ≠ X A\neq X. Now consider

 | h ⁡ ( A ∪ X) = h ⁡ ( A) ∪ h ⁡ ( X) = B ∪ h ⁡ ( X) = h ⁡ ( X). h(A\cup X)=h(A)\cup h(X)=B\cup h(X)=h(X). |  |

Because h h is injective, it follows that A ∪ X = X A\cup X=X, hence A ⊂ X A\subset X. This contradicts the minimality of X X in 𝒦 1 \mathcal{K}_{1}. Therefore, h ⁡ ( X) h(X) must be minimal in 𝒦 2 \mathcal{K}_{2}. ∎

###### Lemma 3.3.

Let 𝒦 \mathcal{K} be a pure union-closed family of sets. If | 𝒦 ⊥ | = 1 |\mathcal{K}^{\bot}|=1, then 𝒦 ⊥ = { ∅ } \mathcal{K}^{\bot}=\{\varnothing\}.

###### Proof.

By assumption, there exists exactly one set, denoted by A A, that belongs to 𝒦 ⊥ \mathcal{K}^{\bot}. It is straightforward to verify that every maximal chain in 𝒦 \mathcal{K} must start from a member of 𝒦 ⊥ \mathcal{K}^{\bot}. In this case, every maximal chain can be represented as:

 | A ⊂ C 1 ⊂ C 2 ⊂ ⋯ ⊂ ⋃ 𝒦. A\subset C_{1}\subset C_{2}\subset\cdots\subset\bigcup\mathcal{K}. |  |

Since every element X ∈ 𝒦 X\in\mathcal{K} lies on a maximal chain, it follows that A ⊂ X A\subset X. If A A contained any elements, those elements would be redundant, as A A is a subset of all elements in 𝒦 \mathcal{K}. However, because 𝒦 \mathcal{K} is a pure collection of sets, A A must be the empty set. ∎

###### Theorem 3.1 (Cardinality).

Let 𝒦 1 \mathcal{K}_{1} and 𝒦 2 \mathcal{K}_{2} be two pure union-closed families of sets. If there exists an isomorphism h: 𝒦 1 → 𝒦 2 h:\mathcal{K}_{1}\to\mathcal{K}_{2}, then for every A ∈ 𝒦 1 A\in\mathcal{K}_{1}, we have:

 | | A | = | h ⁡ ( A) |. |A|=|h(A)|. |  |

###### Proof.

We prove the statement by induction.

###

Base Case: Consider | 𝒦 1 | = | 𝒦 2 | = 1 |\mathcal{K}_{1}|=|\mathcal{K}_{2}|=1. In this case, 𝒦 1 = { A } \mathcal{K}_{1}=\{A\} and 𝒦 2 = { B } \mathcal{K}_{2}=\{B\} for some A, B ∈ 2 [n] A,B\in 2^{[n]}. Both A A and B B must necessarily be empty sets. If A A or B B were not empty, their elements would be redundant, and removing those elements would not affect the cardinality of 𝒦 1 \mathcal{K}_{1} or 𝒦 2 \mathcal{K}_{2}. Thus, for the base case, we have | ⋃ 𝒦 1 | = | ⋃ 𝒦 2 | = 0 |\bigcup\mathcal{K}_{1}|=|\bigcup\mathcal{K}_{2}|=0, as desired.

###

Inductive Step: Assume that the theorem holds for all pure union-closed families with cardinality strictly less than n n. Now, consider 𝒦 1 \mathcal{K}_{1} and 𝒦 2 \mathcal{K}_{2} such that | 𝒦 1 | = | 𝒦 2 | = n |\mathcal{K}_{1}|=|\mathcal{K}_{2}|=n, and let h: 𝒦 1 → 𝒦 2 h:\mathcal{K}_{1}\to\mathcal{K}_{2} be an isomorphism. Let X ∈ 𝒦 1 ⊥ X\in\mathcal{K}_{1}^{\bot}. By Lemma 3.2, we have h ⁡ ( X) = Y h(X)=Y where Y ∈ 𝒦 2 ⊥ Y\in\mathcal{K}_{2}^{\bot}. Consider the restriction h: 𝒦 1 ∖ { X } → 𝒦 2 ∖ { Y } h:\mathcal{K}_{1}\setminus\{X\}\to\mathcal{K}_{2}\setminus\{Y\}. By Lemma 3.1, this restricted mapping remains an isomorphism.

### Case 1:

Suppose 𝒦 1 ∖ { X } \mathcal{K}_{1}\setminus\{X\} and 𝒦 2 ∖ { Y } \mathcal{K}_{2}\setminus\{Y\} are pure collections. By the induction hypothesis, for all A ∈ 𝒦 1 ∖ { X } A\in\mathcal{K}_{1}\setminus\{X\}, we have | A | = | h ⁡ ( A) | |A|=|h(A)|. If | 𝒦 1 ⊥ | = 1 |\mathcal{K}_{1}^{\bot}|=1, then by Lemma 3.3, X = ∅ X=\varnothing and Y = ∅ Y=\varnothing as well. Consequently, for all A ∈ 𝒦 1 A\in\mathcal{K}_{1}, we conclude | A | = | h ⁡ ( A) | |A|=|h(A)|.

###

On the other hand, if | 𝒦 1 ⊥ | > 1 |\mathcal{K}_{1}^{\bot}|>1, let Z ∈ 𝒦 1 ⊥ Z\in\mathcal{K}_{1}^{\bot} such that Z ≠ X Z\neq X. If 𝒦 1 ∖ { Z } \mathcal{K}_{1}\setminus\{Z\} and 𝒦 2 ∖ { h ⁡ ( Z) } \mathcal{K}_{2}\setminus\{h(Z)\} are pure collections, then by the induction hypothesis, we again obtain | X | = | Y | |X|=|Y|, completing the proof for this case.

###

Thus, the theorem is proved for the scenario where removing one element of 𝒦 1 ⊥ \mathcal{K}_{1}^{\bot} and its corresponding map results in pure collections. Next, we consider the case where there exists at least one element in 𝒦 1 ⊥ \mathcal{K}_{1}^{\bot} or 𝒦 2 ⊥ \mathcal{K}_{2}^{\bot} such that its removal results in a non-pure collection.

### Case 2:

Without loss of generality, suppose 𝒦 1 ∖ { X } \mathcal{K}_{1}\setminus\{X\} is not pure and contains a redundant element, denoted by z z. To proceed, we establish three key facts:

1. 1.

z ∈ C z\in C for all C ∈ 𝒦 1 ∖ { X } C\in\mathcal{K}_{1}\setminus\{X\}.

2. 2.

𝒦 1 ∖ { X } \mathcal{K}_{1}\setminus\{X\} has at most one redundant element.

3. 3.

If 𝒦 1 ∖ { X } \mathcal{K}_{1}\setminus\{X\} has a redundant element, then 𝒦 2 ∖ { Y } \mathcal{K}_{2}\setminus\{Y\} also has a redundant element.

###

First, consider z z as a redundant element of 𝒦 1 ∖ { X } \mathcal{K}_{1}\setminus\{X\} but not of 𝒦 1 \mathcal{K}_{1}. This implies there exists exactly one element A X ∈ 𝒦 1 ∖ { X } A_{X}\in\mathcal{K}_{1}\setminus\{X\} such that A X ∖ { z } = X A_{X}\setminus\{z\}=X, and no distinct A 1, A 2 ∈ 𝒦 1 ∖ { X } A_{1},A_{2}\in\mathcal{K}_{1}\setminus\{X\} satisfy A 1 ∖ { z } = A 2 A_{1}\setminus\{z\}=A_{2}. Now, for the sake of contradiction, suppose there exists B ∈ 𝒦 1 ∖ { X } B\in\mathcal{K}_{1}\setminus\{X\} such that z ∉ B z\notin B. Then z ∉ B ∪ X z\notin B\cup X. Let A 1 = A X ∪ B A_{1}=A_{X}\cup B and A 2 = B ∪ X A_{2}=B\cup X. It is straightforward to verify that A 1 ∖ { z } = A 2 A_{1}\setminus\{z\}=A_{2}, leading to a contradiction. Thus, if z z is a redundant element of 𝒦 1 ∖ { X } \mathcal{K}_{1}\setminus\{X\}, it must belong to all its members.

###

Next, suppose t t is another redundant element of 𝒦 1 ∖ { X } \mathcal{K}_{1}\setminus\{X\}. From the previous fact, we know that t t must belong to all members of 𝒦 1 ∖ { X } \mathcal{K}_{1}\setminus\{X\} but not to X X. However, t t cannot satisfy this condition because A X ∖ { z } = X A_{X}\setminus\{z\}=X. Thus no additional redundant element can exist. Therefore, 𝒦 1 ∖ { X } \mathcal{K}_{1}\setminus\{X\} can contain at most one redundant element.

###

For the third fact, let z z be the redundant element of 𝒦 1 ∖ { X } \mathcal{K}_{1}\setminus\{X\} and A X = X ∪ { z } A_{X}=X\cup\{z\}. Define R = h ⁡ ( A X) ∖ Y R=h(A_{X})\setminus Y, which is non-empty by Corollary 2.1. We show that R R is a subset of all members of 𝒦 2 ∖ { Y } \mathcal{K}_{2}\setminus\{Y\}. For the sake of contradiction, suppose there exists D ∈ 𝒦 2 ∖ { Y } D\in\mathcal{K}_{2}\setminus\{Y\} such that R ⊄ D R\not\subset D. By fact 1, we know z ∈ h − 1 ​ ( D) z\in h^{-1}(D). Therefore:

 | h − 1 ​ ( D) ∪ X = h − 1 ​ ( D) ∪ A X ⟹ D ∪ Y = D ∪ h ⁡ ( A X). h^{-1}(D)\cup X=h^{-1}(D)\cup A_{X}\implies D\cup Y=D\cup h(A_{X}). |  |

###

This leads to a contradiction, since R R is not a subset of D ∪ Y D\cup Y, but it is a subset of D ∪ h ⁡ ( A X) D\cup h(A_{X}). Thus, R R must be a subset of all members of 𝒦 2 ∖ { Y } \mathcal{K}_{2}\setminus\{Y\}. Therefore, the members of R R are redundant. As previously proven, 𝒦 2 ∖ { Y } \mathcal{K}_{2}\setminus\{Y\} has at most one redundant element. Hence, | R | = 1 |R|=1, and we denote R = { r } R=\{r\}.

###

The mapping h ∗: ( 𝒦 1 ∖ { X }) ∗ → ( 𝒦 2 ∖ { Y }) ∗ h^{*}:{(\mathcal{K}_{1}\setminus\{X\})}^{*}\to{(\mathcal{K}_{2}\setminus\{Y\})}^{*}, defined as h ∗ ​ ( A ∖ { z }) = h ⁡ ( A) ∖ { r } h^{*}(A\setminus\{z\})=h(A)\setminus\{r\} where A ∈ 𝒦 1 ∖ { X } A\in\mathcal{K}_{1}\setminus\{X\}, is an isomorphism between two pure union-closed families of sets. Furthermore, the cardinalities satisfy | ( 𝒦 1 ∖ { X }) ∗ | = | ( 𝒦 2 ∖ { Y }) ∗ | = n − 1 |{(\mathcal{K}_{1}\setminus\{X\})}^{*}|=|{(\mathcal{K}_{2}\setminus\{Y\})}^{*}|=n-1. By the induction hypothesis, for all A ∖ { z } ∈ ( 𝒦 1 ∖ { X }) ∗ A\setminus\{z\}\in{(\mathcal{K}_{1}\setminus\{X\})}^{*}, we have:

 | | A ∖ { z } | = | h ∗ ​ ( A ∖ { z }) | = | h ⁡ ( A) ∖ { r } |. |A\setminus\{z\}|=|h^{*}(A\setminus\{z\})|=|h(A)\setminus\{r\}|. |  |

Since for all A ∈ 𝒦 1 ∖ { X } A\in\mathcal{K}_{1}\setminus\{X\}, we have z ∈ A z\in A and r ∈ h ⁡ ( A) r\in h(A), it follows that | A | = | h ⁡ ( A) | |A|=|h(A)|.

###

From fact 1 and fact 3, there exists a set A X ∈ 𝒦 1 A_{X}\in\mathcal{K}_{1} such that z ∈ A X z\in A_{X} but z ∉ X z\not\in X, and r ∈ h ⁡ ( A X) r\in h(A_{X}) but r ∉ Y r\not\in Y. This implies:

 | | X | = | A X | − 1 = | h ⁡ ( A X) | − 1 = | Y |. |X|=|A_{X}|-1=|h(A_{X})|-1=|Y|. |  |

Thus, for all A ∈ 𝒦 1 A\in\mathcal{K}_{1}, it follows that | A | = | h ⁡ ( A) | |A|=|h(A)|.

∎

###

We conclude with two corollaries used later in the proof of the main theorem.

###### Corollary 3.1.

Let 𝒦 1 \mathcal{K}_{1} and 𝒦 2 \mathcal{K}_{2} be two pure union-closed families of sets. If there exists an isomorphism h: 𝒦 1 → 𝒦 2 h:\mathcal{K}_{1}\to\mathcal{K}_{2}, then:

 | | ⋃ 𝒦 1 | = | ⋃ 𝒦 2 |. \left|\bigcup\mathcal{K}_{1}\right|=\left|\bigcup\mathcal{K}_{2}\right|. |  |

###### Corollary 3.2.

Let 𝒦 1 \mathcal{K}_{1} and 𝒦 2 \mathcal{K}_{2} be two pure union-closed families of sets. If there exists an isomorphism h: 𝒦 1 → 𝒦 2 h:\mathcal{K}_{1}\to\mathcal{K}_{2}, then for any A, B ∈ 𝒦 1 A,B\in\mathcal{K}_{1}, the following properties hold:

1. 1.

| A ∪ B | = | h ⁡ ( A) ∪ h ⁡ ( B) | |A\cup B|=|h(A)\cup h(B)|.

2. 2.

| A ∩ B | = | h ⁡ ( A) ∩ h ⁡ ( B) | |A\cap B|=|h(A)\cap h(B)|.

3. 3.

| A ∖ B | = | h ⁡ ( A) ∖ h ⁡ ( B) | |A\setminus B|=|h(A)\setminus h(B)|.

4. 4.

| A c | = | h ​ ( A) c | |A^{c}|=|h{(A)}^{c}|,

where A c = ⋃ 𝒦 1 ∖ A A^{c}=\bigcup\mathcal{K}_{1}\setminus A and h ​ ( A) c = ⋃ 𝒦 2 ∖ h ⁡ ( A) h{(A)}^{c}={\bigcup\mathcal{K}_{2}}\setminus h(A).

## 4 Hyperisomorphism

###

In this section we show that the internal structure of a pure union-closed family is faithfully preserved under isomorphism, in the sense that every isomorphism arises from a bijection of the ground sets.

###### Definition 4.1 (Hyperisomorphism).

Let 𝒦 1 \mathcal{K}_{1} and 𝒦 2 \mathcal{K}_{2} be two union-closed families of sets. A bijective mapping H: ⋃ 𝒦 1 → ⋃ 𝒦 2 H:\bigcup\mathcal{K}_{1}\to\bigcup\mathcal{K}_{2} is called a hyperisomorphism if the induced mapping h: 𝒦 1 → 𝒦 2 h:\mathcal{K}_{1}\to\mathcal{K}_{2}, defined by h ⁡ ( A) = { H ⁡ ( a) ∣ a ∈ A } h(A)=\{H(a)\mid a\in A\}, is an isomorphism.

###

To establish our main theorem, we require the following lemmas. First, we introduce the notation 𝒦 i \mathcal{K}^{i}, defined as:

 | 𝒦 i = { A ∈ 𝒦 ∣ i ∈ A }. \mathcal{K}^{i}=\{A\in\mathcal{K}\mid i\in A\}. |  |

###### Lemma 4.1.

Let 𝒦 \mathcal{K} be a pure union-closed family of sets. Then, for all i, j ∈ ⋃ 𝒦 i,j\in\bigcup\mathcal{K}, the following equivalence holds:

 | i = j ⇔ 𝒦 i = 𝒦 j. i=j\iff\mathcal{K}^{i}=\mathcal{K}^{j}. |  |

###### Proof.

Suppose i = j i=j. By definition, it follows that 𝒦 i = 𝒦 j \mathcal{K}^{i}=\mathcal{K}^{j}. Conversely, assume 𝒦 i = 𝒦 j \mathcal{K}^{i}=\mathcal{K}^{j}, but i ≠ j i\neq j. This would imply that i i and j j are redundant elements in 𝒦 \mathcal{K}, contradicting the purity of 𝒦 \mathcal{K}. Hence, it must be the case that i = j i=j. ∎

###### Lemma 4.2.

Let 𝒦 \mathcal{K} be a union-closed family of sets. Then, for any distinct elements i, j ∈ ⋃ 𝒦 i,j\in\bigcup\mathcal{K}, the following inequality holds:

 | | ( ⋂ 𝒦 i) ∪ ( ⋂ 𝒦 j) | ≥ 2. \left|\left(\bigcap\mathcal{K}^{i}\right)\cup\left(\bigcap\mathcal{K}^{j}\right)\right|\geq 2. |  |

###### Proof.

This follows since i i and j j, being distinct, are both in the union. ∎

###### Corollary 4.1.

Let 𝒦 \mathcal{K} be a union-closed family of sets. Then, for any distinct elements { a i } i = 1 n ⊆ ⋃ 𝒦 \{a_{i}\}_{i=1}^{n}\subseteq\bigcup\mathcal{K}, the following inequality holds:

 | | ⋃ i = 1 n ⋂ 𝒦 a i | ≥ n. \left|\bigcup_{i=1}^{n}\bigcap\mathcal{K}^{a_{i}}\right|\geq n. |  |

###### Lemma 4.3.

Let 𝒦 \mathcal{K} be a union-closed family of sets, and i i be an arbitrary element of ⋃ 𝒦 \bigcup\mathcal{K}. If ⋂ 𝒦 1 i = { a 1, …, a n } \bigcap\mathcal{K}_{1}^{i}=\{a_{1},\dots,a_{n}\}, then:

 | | ⋃ j = 1 n ⋂ 𝒦 1 a j | = n. \left|\bigcup_{j=1}^{n}\bigcap\mathcal{K}_{1}^{a_{j}}\right|=n. |  |

###### Proof.

Let a a be an arbitrary element of ⋂ 𝒦 i \bigcap\mathcal{K}^{i}. Since 𝒦 i ⊆ 𝒦 a \mathcal{K}^{i}\subseteq\mathcal{K}^{a}, it follows that ⋂ 𝒦 a ⊆ ⋂ 𝒦 i \bigcap\mathcal{K}^{a}\subseteq\bigcap\mathcal{K}^{i}. Consequently, we have:

 | ⋃ j = 1 n ⋂ 𝒦 a j ⊆ ⋂ 𝒦 i, \bigcup_{j=1}^{n}\bigcap\mathcal{K}^{a_{j}}\subseteq\bigcap\mathcal{K}^{i}, |  |

which implies:

 | | ⋃ j = 1 n ⋂ 𝒦 1 a j | ≤ n. \left|\bigcup_{j=1}^{n}\bigcap\mathcal{K}_{1}^{a_{j}}\right|\leq n. |  |

Applying Corollary 4.1, we conclude that:

 | | ⋃ j = 1 n ⋂ 𝒦 1 a j | = n. \left|\bigcup_{j=1}^{n}\bigcap\mathcal{K}_{1}^{a_{j}}\right|=n. |  |

This completes the proof. ∎

###### Lemma 4.4.

Let 𝒦 1 \mathcal{K}_{1} and 𝒦 2 \mathcal{K}_{2} be two pure union-closed families of sets, and h: 𝒦 1 → 𝒦 2 h:\mathcal{K}_{1}\to\mathcal{K}_{2} be an isomorphism between them. Then, for each i ∈ ⋃ 𝒦 1 i\in\bigcup\mathcal{K}_{1}, there exists a unique j ∈ ⋃ 𝒦 2 j\in\bigcup\mathcal{K}_{2} such that:

 | 𝒦 2 j = h ⁡ ( 𝒦 1 i), \mathcal{K}_{2}^{j}=h(\mathcal{K}_{1}^{i}), |  |

where h ⁡ ( 𝒦 1 i) = { h ⁡ ( A) ∣ A ∈ 𝒦 1 i } h(\mathcal{K}_{1}^{i})=\{h(A)\mid A\in\mathcal{K}_{1}^{i}\}.

###### Proof.

Let i ∈ ⋃ 𝒦 1 i\in\bigcup\mathcal{K}_{1}. Suppose ⋂ 𝒦 1 i = { a 1, …, a n } \bigcap\mathcal{K}_{1}^{i}=\{a_{1},\dots,a_{n}\}. By Lemma 4.3, we have:

 | | ⋃ j = 1 n ⋂ 𝒦 1 a j | = n. \left|\bigcup_{j=1}^{n}\bigcap\mathcal{K}_{1}^{a_{j}}\right|=n. |  |

By Corollary 3.2, we can assume ⋂ h ⁡ ( 𝒦 1 i) = { b 1, …, b n } \bigcap h(\mathcal{K}_{1}^{i})=\{b_{1},\dots,b_{n}\}.

###

Since h ⁡ ( 𝒦 1 i) ⊆ 𝒦 2 b h(\mathcal{K}_{1}^{i})\subseteq\mathcal{K}_{2}^{b} for each b ∈ ⋂ h ⁡ ( 𝒦 1 i) b\in\bigcap h(\mathcal{K}_{1}^{i}), it suffices to show that for exactly one b i ∈ ⋂ h ⁡ ( 𝒦 1 i) b_{i}\in\bigcap h(\mathcal{K}_{1}^{i}) we have:

 | | h ⁡ ( 𝒦 1 i) | = | 𝒦 2 b i |. |h(\mathcal{K}_{1}^{i})|=|\mathcal{K}_{2}^{b_{i}}|. |  |

###

Assume, for the sake of contradiction, that for all b ∈ ⋂ h ⁡ ( 𝒦 1 i) b\in\bigcap h(\mathcal{K}_{1}^{i}), we have | h ⁡ ( 𝒦 1 i) | < | 𝒦 2 b | |h(\mathcal{K}_{1}^{i})|<|\mathcal{K}_{2}^{b}|. This implies i ∉ ⋂ h − 1 ​ ( 𝒦 2 b) i\notin\bigcap h^{-1}(\mathcal{K}_{2}^{b}), and thus:

 | ⋂ h − 1 ​ ( 𝒦 2 b) ⊂ ⋂ 𝒦 1 i. \bigcap h^{-1}(\mathcal{K}_{2}^{b})\subset\bigcap\mathcal{K}_{1}^{i}. |  |

Consequently:

 | ⋃ j = 1 n ⋂ h − 1 ​ ( 𝒦 2 b j) ⊂ ⋂ 𝒦 1 i, \bigcup_{j=1}^{n}\bigcap h^{-1}(\mathcal{K}_{2}^{b_{j}})\subset\bigcap\mathcal{K}_{1}^{i}, |  |

which implies:

 | | ⋃ j = 1 n ⋂ h − 1 ​ ( 𝒦 2 b j) | < n. \left|\bigcup_{j=1}^{n}\bigcap h^{-1}(\mathcal{K}_{2}^{b_{j}})\right|<n. |  |

Then by Corollary 3.2, we have:

 | | ⋃ j = 1 n ⋂ 𝒦 2 b j | < n. \left|\bigcup_{j=1}^{n}\bigcap\mathcal{K}_{2}^{b_{j}}\right|<n. |  |

However, Corollary 4.1 ensures that:

 | | ⋃ j = 1 n ⋂ 𝒦 2 b j | ≥ n, \left|\bigcup_{j=1}^{n}\bigcap\mathcal{K}_{2}^{b_{j}}\right|\geq n, |  |

which is a contradiction. Therefore, by Lemma 4.1, there exists exactly one j ∈ ⋂ h ⁡ ( 𝒦 1 i) j\in\bigcap h(\mathcal{K}_{1}^{i}) such that:

 | 𝒦 2 j = h ⁡ ( 𝒦 1 i). \mathcal{K}_{2}^{j}=h(\mathcal{K}_{1}^{i}). |  |

This completes the proof. ∎

###### Theorem 4.1.

Let 𝒦 1 \mathcal{K}_{1} and 𝒦 2 \mathcal{K}_{2} be two pure union-closed families of sets. For every isomorphism h: 𝒦 1 → 𝒦 2 h:\mathcal{K}_{1}\to\mathcal{K}_{2}, there exists a hyperisomorphism H: ⋃ 𝒦 1 → ⋃ 𝒦 2 H:\bigcup\mathcal{K}_{1}\to\bigcup\mathcal{K}_{2} such that:

 | h ⁡ ( A) = { H ⁡ ( a) ∣ a ∈ A } ​ for all ​ A ∈ 𝒦 1. h(A)=\{H(a)\mid a\in A\}\hskip 9.24994pt\text{for all }A\in\mathcal{K}_{1}. |  |

###### Proof.

Let i ∈ ⋃ 𝒦 1 i\in\bigcup\mathcal{K}_{1}. By Lemma 4.4, there exists a corresponding j ∈ ⋃ 𝒦 2 j\in\bigcup\mathcal{K}_{2} which allows us to define H H. To show that H H is bijective, suppose H ⁡ ( a) = H ⁡ ( b) H(a)=H(b) for some a, b ∈ ⋃ 𝒦 1 a,b\in\bigcup\mathcal{K}_{1}. This implies that:

 | 𝒦 1 a = 𝒦 1 b. \mathcal{K}_{1}^{a}=\mathcal{K}_{1}^{b}. |  |

Using Lemma 4.1, we conclude that a = b a=b, establishing that H H is injective. Furthermore, by Corollary 3.1, H H is clearly surjective. Thus, H H is bijective. Next, let A ∈ 𝒦 1 A\in\mathcal{K}_{1} and i ∈ A i\in A. To complete the proof, we need to show that H ⁡ ( i) ∈ h ⁡ ( A) H(i)\in h(A). By Lemma 4.4, we have

 | h ⁡ ( A) ∈ 𝒦 2 H ⁡ ( i), h(A)\in\mathcal{K}_{2}^{H(i)}, |  |

which satisfies the required condition. ∎

## References

- [1] A. Abdollahi, R. Woodroofe, and G. Zaimi. Frankl’s conjecture for subgroup lattices. Electron. J. Combin., 24(3):Paper P3.25, 9 pp., 2017. [doi:10.37236/6248][3].
- [2] T. Abe and B. Nakano. Frankl’s conjecture is true for modular lattices. Graphs Combin., 14(4):305–311, 1998. [doi:10.1007/PL00021180][4].
- [3] T. Abe and B. Nakano. Lower semimodular types of lattices: Frankl’s conjecture holds for lower quasi-semimodular lattices. Graphs Combin., 16(1):1–16, 2000. [doi:10.1007/s00373-999-0128-5][5].
- [4] R. Alweiss, B. Huang, and M. Sellke. Improved lower bound for frankl’s union-closed sets conjecture. Electron. J. Combin., 31(3):P3.35, 2024. [doi:10.37236/12232][6].
- [5] H. Bruhn and O. Schaudt. The journey of the union-closed sets conjecture, 2015. URL: [https://arxiv.org/abs/1309.3297][7], [arXiv:1309.3297][7].
- [6] S. Cambie. Better bounds for the union-closed sets conjecture using the entropy approach, 2022. URL: [https://arxiv.org/abs/2212.12500][8], [arXiv:2212.12500][8].
- [7] A. Carvalho and A. Machiavelo. On supratopologies, normalized families and frankl conjecture, 2024. URL: [https://arxiv.org/abs/2408.11213][9], [arXiv:2408.11213][9].
- [8] C. H. Colbert. Chain conditions and optimal elements in generalized union-closed families of sets, 2024. URL: [https://arxiv.org/abs/2412.18740][10], [arXiv:2412.18740][10].
- [9] G. Czédli and E. T. Schmidt. Frankl’s conjecture for large semimodular and planar semimodular lattices. Acta Univ. Palacki. Olomuc., Fac. Rerum Nat. Mathematica, 47(1):47–53, 2008. URL: [http://eudml.org/doc/32473][11].
- [10] S. Das and S. Wu. Frequent elements in union-closed set families, 2024. URL: [https://arxiv.org/abs/2412.03862][12], [arXiv:2412.03862][12].
- [11] P. Frankl. Extremal set systems. In Handbook of Combinatorics, volume 2, pages 1293–1329. 1995.
- [12] G. Gendler. Partial results for union-closed conjectures on the weighted cube, 2025. URL: [https://arxiv.org/abs/2504.13347][13], [arXiv:2504.13347][13].
- [13] J. Gilmer. A constant lower bound for the union-closed sets conjecture, 2022. URL: [https://arxiv.org/abs/2211.09055][14], [arXiv:2211.09055][14].
- [14] V. Joshi and B. N. Waphare. Frankl’s conjecture for breadth two lattices. Commun. Algebra, 47(9):3730–3735, 2019. [doi:10.1080/00927872.2019.1593360][15].
- [15] V. Joshi, B. N. Waphare, and S. P. Kavishwar. A proof of frankl’s union-closed sets conjecture for dismantlable lattices. Algebra Universalis, 76(3):351–354, 2016. [doi:10.1007/s00012-016-0405-0][16].
- [16] I. Karpas. Two results on union-closed families, 2017. URL: [https://arxiv.org/abs/1708.01434][17], [arXiv:1708.01434][17].
- [17] K. Lu and A. Raz. A note on the union-closed sets conjecture and reimer’s average set size theorem, 2024. URL: [https://arxiv.org/abs/2405.10639][18], [arXiv:2405.10639][18].
- [18] M. J. Moghaddas Mehr. A note on the union-closed sets conjecture. arXiv, 2023. [arXiv:2309.01704][19], [doi:10.48550/arXiv.2309.01704][20].
- [19] B. Poonen. Union-closed families. J. Combin. Theory Ser. A, 59(2):253–268, 1992.
- [20] J. Reinhold. Frankl’s conjecture is true for lower semimodular lattices. Graphs Combin., 16(1):115–116, 2000. [doi:10.1007/s003730050008][21].
- [21] I. Rival, editor. Graphs and Order, volume 147 of NATO ASI Ser. Springer, Dordrecht, 1985.
- [22] L. Yu. Dimension-free bounds for the union-closed sets conjecture. Entropy, 25(5):767, 2023. [doi:10.3390/e25050767][22].


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: https://doi.org/10.37236/6248
[4]: https://doi.org/10.1007/PL00021180
[5]: https://doi.org/10.1007/s00373-999-0128-5
[6]: https://doi.org/10.37236/12232
[7]: https://arxiv.org/pdf/1309.3297
[8]: https://arxiv.org/pdf/2212.12500
[9]: https://arxiv.org/pdf/2408.11213
[10]: https://arxiv.org/pdf/2412.18740
[11]: http://eudml.org/doc/32473
[12]: https://arxiv.org/pdf/2412.03862
[13]: https://arxiv.org/pdf/2504.13347
[14]: https://arxiv.org/pdf/2211.09055
[15]: https://doi.org/10.1080/00927872.2019.1593360
[16]: https://doi.org/10.1007/s00012-016-0405-0
[17]: https://arxiv.org/pdf/1708.01434
[18]: https://arxiv.org/pdf/2405.10639
[19]: https://arxiv.org/pdf/2309.01704
[20]: https://doi.org/10.48550/arXiv.2309.01704
[21]: https://doi.org/10.1007/s003730050008
[22]: https://doi.org/10.3390/e25050767
