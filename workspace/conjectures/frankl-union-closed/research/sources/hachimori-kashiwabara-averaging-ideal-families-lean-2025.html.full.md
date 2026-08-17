<!-- source: https://arxiv.org/html/2504.13454 | converted from HTML -->

On the Averaging Problem of Ideal Families Related to Frankl’s Conjecture with Formal Proof by Lean 4

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2504.13454v1 [math.CO] 18 Apr 2025

# On the Averaging Problem of Ideal Families Related to Frankl’s Conjecture with Formal Proof by Lean 4 Corresponding author

Masahiro Hachimori University of Tsukuba Affiliation: Kenji Kashiwabara The University of Tokyo

###### Abstract

Frankl’s conjecture, also known as the union-closed sets conjecture, can be equivalently expressed in terms of intersection-closed set families by considering the complements of sets. It posits that any family of sets closed under intersections, and containing both the ground set and the empty set, must have a “rare vertex” — a vertex belonging to at most half of the members of the family. The concept of *average rarity*describes a set family where the average degree of all the elements is at most half of the number of its members. Average rarity is a stronger property that implies the existence of a rare vertex. This paper focuses on ideal families, which are set families that are downward-closed (except the ground set) and include the ground set. We present a proof that the normalized degree sum of any ideal family is non-positive, which is equivalent to saying that every ideal family satisfies the average rarity condition. This proof is formalized and verified using the Lean 4 theorem prover.

## 1 Introduction

### 1.1 Frankl’s conjecture

Frankl’s conjecture, also referred to as the union-closed sets conjecture, is a well-known and enduring open problem in combinatorics, first proposed in 1979 by P. Frankl [8]. Its deceptively simple formulation and far-reaching implications have sparked significant interest. It states that in any nonempty union-closed family on finite sets, there exists an element that is contained in at least half of the sets. When considering the dual notion through complements, the conjecture can also be phrased in terms of intersection-closed families, asserting the existence of an element contained in at most half of the members.

Consider set families on a nonempty finite ground set U U. An element in U U is called a *vertex*. We call a member of a set family ℱ \mathcal{F} a *hyperedge*. A family of sets ℱ \mathcal{F} is called *intersection-closed*if for any two sets A, B ∈ ℱ A,B\in\mathcal{F}, their intersection A ∩ B A\cap B is also in ℱ \mathcal{F}.

In the intersection-closed form, Frankl’s conjecture asserts that any nonempty intersection-closed family on a finite set, containing both the empty set and the ground set, must have at least one *rare vertex*, which is an element appearing in at most half of the hyperedges in the family. Instead of assuming the existence of the ground set and the empty set, it is equivalent to assume that the set family contains at least two sets for considering the conjecture.

Despite substantial efforts, the conjecture remains unresolved [4]. However, it has been verified for specific cases, such as families with small cardinality (up to 11 elements [3]) or those exhibiting particular structural properties [18, 19, 26]. It also connects to lattice theory and related areas of combinatorics, highlighting its mathematical richness [1, 24, 25]. Recent significant progress by Gilmer [9] establishes that the existence of an element contained in a constant ratio of sets of the family (for the union-closed form of the conjecture). The ratio was improved to 3 − 5 2 ≈ 0.381966 \frac{3-\sqrt{5}}{2}\approx 0.381966 by several authors [2, 6, 23, 27], and further improvements have been made in subsequent works [5, 16, 28], but there still remains a gap to the conjectured ratio of 1/2.

Hachimori and Kashiwabara [12] investigated Frankl’s conjecture in the intersection-closed form through minor operations such as deletion and contraction. Their work focuses on the properties that minimal counterexamples of the conjecture have to satisfy. In this paper, we continue to adopt the approach of the intersection-closed form, but focus on a different direction.

In this paper, as explained later, we provide a formalized proof by Lean 4. Previously, Marić, Zivković, and Vučković [17] utilized the Coq proof assistant to formalize FC-families and upward-closed families, offering a structured framework for systematically analyzing these families. Coq is another theorem prover system that is widely used. Their Coq-based techniques are invaluable for handling upward-closed families in formal proof contexts.

### 1.2 Averaging approach to Frankl’s conjecture

In this paper, we focus on the averaging approach, which discusses the average degree over all vertices instead of the existence of the rare (or abundant) vertices. This is one of the important approaches, see [4, Sec. 6], [7] for example. In this paper, the average rarity of set families is the main topic, where a set family is average rare if the average of the degrees of the vertices is at most 1/2. This is a stronger property than the existence of a rare vertex. To analyze the average rarity of a set family, we introduce the normalized degree sum of a set family as a measure. If the normalized degree sum of a set family is non-positive, it is an average rare family.

It should be remarked that the average rarity is a condition strictly stronger than the existence of a rare vertex, and the intersection-closed families that are average rare form a strict subclass. Therefore, the problem to identify the class of average rare families is a different problem from Frankl’s conjecture. Still, this problem itself has an importance in the study of the combinatorial structures of set families, and may contribute to the conjecture to some extent. The main theorem of this paper provides a new class of intersection-closed families, ideal families, that are average rare.

Ideal families, introduced in Section 2.2 of this paper, constitute a particular class of set families that are downward-closed except the ground set and include both the empty set and the ground set. Although we have not found the exact same statement, it is probably known that any ideal family has a rare vertex. For example, [21] refers that a filter family cannot be a counterexample of the union-closed set conjecture. However, it is different from ours because our ideal family has always the ground set as its hyperedge. We show in Lemma 2.2 that ideal families contain rare vertices, that is, no counterexamples to Frankl’s conjecture can be found among ideal families. Further, we show in Theorem 4.1 that they are average rare.

### 1.3 Formalization of the theorem

As well as giving a (human-written) proof for the main theorem, we additionally provide a formalized proof by Lean 4. This formalization is publicly available on our GitHub repository [13]. We describe the outline in Section 5. Lean 4 [20] is a modern theorem prover and programming language based on dependent type theory, and is designed to formalize mathematical proofs.

The formal verification of the proof using a theorem prover like Lean 4 not only enhances the rigor of the result but also demonstrates the utility of formal methods in ensuring correctness in mathematical research. The ability to formalize and verify proofs provides a high level of assurance that can be difficult to achieve through traditional human verification. This can benefit readers, for example, by making it easier to verify the proofs. Formal proofs eliminate ambiguity and ensure that all logical steps are valid. This level of rigor is especially valuable in complex combinatorial proofs, where subtle errors can easily go unnoticed. In this paper, the correctness of the statements and their proofs have been rigorously validated using the Lean 4 system. For verification, it is not necessary for the readers to directly examine the Lean 4 proof code. Barring exceptional circumstances, it is reasonable to trust in the validity of the proofs. Formal proofs will reduce the efforts of the readers in verifying the correctness and, instead, the readers can focus their efforts in grasping the outlines.

The theorem prover can also identify gaps or errors that might be overlooked in human-written proofs. This capability helped us refine the inductive argument and ensure that all cases were properly handled. Lean 4 can detect conditions that are not used in the proof.

Once the definitions and lemmas are formalized in Lean 4, they can be reused in future proofs and research. The structures and operations defined for ideal families can be extended to broader classes of set families, making Lean 4 a powerful tool for ongoing combinatorial research. It is also well-suited for collaborative proof development by large groups.

The study [11] formalizes the minor excluded characterization of binary matroids using the Lean 4 theorem prover. This study is not directly related to Frankl’s conjecture, but is relevant within the framework of set families. We incorporated some of the definitions in his paper.

Here, we briefly explain how we created the proofs written in Lean 4. In general, creating formal proofs in Lean 4 was cumbersome and time-consuming. However, the advent of AI assistants and large language models (LLMs) has introduced tools that greatly streamline high-level code creation. Thanks to these advancements, the process of writing proof code has become much more efficient. In creating the proofs presented here, we greatly benefited from the assistance of AI assistant tools such as ChatGPT [22]. There are several other tools that are helpful. Lean Copilot [14] is a tool integrated into the Lean 4 system. GitHub Copilot [10] is an AI-powered coding assistant that supports various other programming languages. Lean search [15] is a search engine for Lean 4 tactics. However, writing formal proofs in Lean 4 is still a time-consuming work. Currently, AI assistants often suggest outdated syntax or theorems in the format of Lean 3, which requires corrections and adjustments. This issue is expected to be improved in the future. In the future, these tools are expected to evolve further and come closer to achieving automated theorem proving.

The remainder of this paper is organized as follows. In Section 2, we provide definitions of key concepts, including set families, ideal families, normalized degree sum, and minors. Section 3 presents examples of ideal families to illustrate these concepts in a more concrete way and calculates their normalized degree sum. In Section 4, we detail the proof of the main theorem, that is, the average rarity condition for ideal families. Section 5 presents the formal proof of the main theorem by Lean 4. Section 6 concludes the paper and suggests directions for future research.

## 2 Mathematical preliminaries

### 2.1 Intersection-closed families, rarity, and average rarity

Let U U be a nonempty finite ground set. An element of U U is called a *vertex*. A set family ℱ \mathcal{F} is a collection of subsets of U U. An element of ℱ \mathcal{F} is called a *hyperedge*.

###### Definition 2.1 (Intersection-closed family).

A set family ℱ \mathcal{F} on U U is *intersection-closed*if, for any A, B ∈ ℱ A,B\in\mathcal{F}, their intersection A ∩ B A\cap B is also in ℱ \mathcal{F}.

###### Definition 2.2 (Degree of a vertex).

For a vertex v ∈ U v\in U, the *degree*of v v in ℱ \mathcal{F}, denoted deg ℱ ⁡ ( v) \deg_{\mathcal{F}}(v), is the number of hyperedges in ℱ \mathcal{F} that contain the vertex v v:

 | deg ℱ ⁡ ( v) = | { H ∈ ℱ ∣ v ∈ H } |. \deg_{\mathcal{F}}(v)=|\{H\in\mathcal{F}\mid v\in H\}|. |  |

###### Definition 2.3 (Rare vertex).

For a set family ℱ \mathcal{F} and a vertex v ∈ U v\in U, v v is rare if deg ℱ ⁡ ( v) ≤ | ℱ | / 2 \deg_{\mathcal{F}}(v)\leq|\mathcal{F}|/2.

By these terminologies, Frankl’s conjecture can be expressed as follows.

###### Conjecture 2.1.

Every intersection-closed set family ℱ \mathcal{F} with { U, ∅ } ⊆ ℱ \{U,\emptyset\}\subseteq\mathcal{F} has a rare vertex.

In this paper, our main concern is in average rarity. We say that a family is *average rare*if the average of the degrees over all vertices is at most half the number of hyperedges of the family. This can be expressed using the normalized degree sum as follows.

###### Definition 2.4 (Normalized degree sum).

The *normalized degree sum*of ℱ \mathcal{F} is defined as:

 | NDS ⁡ ( ℱ) = 2 ⋅ ∑ v ∈ U deg ℱ ⁡ ( v) − | U | ⋅ | ℱ |. {\rm NDS}(\mathcal{F})=2\cdot\sum_{v\in U}\deg_{\mathcal{F}}(v)-|U|\cdot|\mathcal{F}|. |  |

If NDS ⁡ ( ℱ) ≤ 0 {\rm NDS}(\mathcal{F})\leq 0, we say that ℱ \mathcal{F} satisfies the *average rarity condition*.

A family is average rare if it satisfies the average rarity condition, since NDS ​ ( ℱ) ≤ 0 \text{NDS}(\mathcal{F})\leq 0 is equivalent to ∑ v ∈ U deg ℱ ⁡ ( v) / | U | ≤ 1 2 ​ | ℱ | \sum_{v\in U}\deg_{\mathcal{F}}(v)/|U|\leq\frac{1}{2}|\mathcal{F}|. From this, the following lemma is straightforward.

###### Lemma 2.1.

If a set family ℱ \mathcal{F} satisfies the average rarity condition, ℱ \mathcal{F} has a rare vertex.

Some intersection-closed set families may not satisfy the average rarity condition. For example, { ∅, { a }, { a, b }, { a, c }, { a, b, c } } \{\,\emptyset,\{a\},\{a,b\},\{a,c\},\{a,b,c\}\,\} is an intersection-closed family but NDS = 1 > 0 {\rm NDS}=1>0. (Though this family is not average rare, this family has rare vertices b b and c c.)

The normalized degree sum measures the deviation from an even distribution of vertices among hyperedges.

Denote the total sum of the size of the hyperedge by

 | TSH ​ ( ℱ) = ∑ H ∈ ℱ | H | = ∑ v ∈ U deg ℱ ⁡ ( v). \text{TSH}(\mathcal{F})=\sum_{H\in{\mathcal{F}}}|H|=\sum_{v\in U}\deg_{\mathcal{F}}(v). |  |

The second equality above follows from the double counting principle. By this, we have

 | NDS ⁡ ( ℱ) = 2 ⋅ TSH ⁡ ( ℱ) − | U | ⋅ | ℱ |. {\rm NDS}(\mathcal{F})=2\cdot{\rm TSH}(\mathcal{F})-|U|\cdot|\mathcal{F}|. |  |

### 2.2 Ideal families

###### Definition 2.5 (Ideal family).

A set family ℱ ⊆ 2 U \mathcal{F}\subseteq 2^{U} is called an *ideal family*if it satisfies the following conditions:

1. 1.

Contains Empty Set: ∅ ∈ ℱ \emptyset\in\mathcal{F}.

2. 2.

Contains Ground Set: U ∈ ℱ U\in\mathcal{F}.

3. 3.

Downward-Closed except U U: For all A, B ∈ ℱ A,B\in\mathcal{F} with A ≠ U A\neq U, if B ⊆ A B\subseteq A, then B ∈ ℱ B\in\mathcal{F}.

In other words, an ideal family includes all subsets of its nonempty hyperedges, except the ground set. This property ensures that once a hyperedge (which is not the ground set) is contained, all smaller hyperedges contained by it are also included. Obviously, every ideal family is closed under intersections. Remark that the set family in which the ground set is its sole hyperedge is not allowed by the condition that the family must contain the empty set.

The next lemma can be proven relatively easily by demonstrating the existence of an injection, which is a commonly used argument in this field.

###### Lemma 2.2.

Every ideal family has a rare vertex.

###### Proof.

Consider a maximal hyperedge with respect to the inclusion relation, excluding the ground set. Let v v be a vertex that does not belong to this maximal set. To show that vertex v v is rare, it suffices to construct an injection from hyperedges containing v v to hyperedges not containing v v. Such a required mapping can be defined as follows:

- •

If a hyperedge H H containing v v is not the ground set, then map H H to the hyperedge H ∖ { v } H\setminus\{v\}, which does not contain v v.

- •

If a hyperedge containing v v is the ground set, map it to a maximal hyperedge under the inclusion relation that does not include v v, excluding the ground set.

This mapping is injective because different hyperedges are mapped to different hyperedges. If two hyperedges are mapped to the same hyperedge J J, the original hyperedge is J ∪ { v } J\cup\{v\} (the case that J ∪ { v } J\cup\{v\} is a hyperedge) or the ground set (the case that J ∪ { v } J\cup\{v\} is not a hyperedge).

∎

The main theorem (Theorem 4.1) of this paper states that any ideal family ℱ \mathcal{F} over a nonempty finite ground set U U is average rare, i.e., the normalized degree sum NDS ​ ( ℱ) ≤ 0 \text{NDS}(\mathcal{F})\leq 0. That is, our main aim is to strengthen Lemma 2.2 to average rarity. Note that our proof of the main theorem relies on Lemma 2.2.

### 2.3 Minors of ideal families

Consider a set family ℱ \mathcal{F} on the ground set U U. In this subsection, we assume that ℱ \mathcal{F} has a ground set whose size is at least two. We consider three operators, deletion, contraction, and trace. These operators map a set family to a set family whose ground set is smaller by one. These minor operations are defined for general set families, and especially, they preserve intersection-closedness [12], that is, intersection-closed families are mapped to intersection-closed families by these operators. In using these operators for ideal families, however, we need specialized treatments in order to ensure the operations preserve the families to be ideal.

#### *Deletion minor*: ℱ. del ​ v {\mathcal{F}}.{\rm del}\,{v}

For a set family ℱ \mathcal{F} and v ∈ U v\in U, the deletion ℱ. del ​ v {\mathcal{F}}.{\rm del}\,{v} is the family consisting of the hyperedges in ℱ \mathcal{F} that do not contain v v, i.e., ℱ. del ​ v = { H ∈ ℱ ∣ v ∉ H } {\mathcal{F}}.{\rm del}\,{v}=\{H\in\mathcal{F}\mid v\notin H\}. When ℱ \mathcal{F} is an ideal family, the deletion is downward-closed, but it may not contain the ground set U ∖ { v } U\setminus\{v\}. In this case, in order to make the family to be an ideal family, we add the ground set to the family. We define this operation as the deletion operator for ideal families as follows.

 | ℱ. del ​ v ′ = { H ∈ ℱ ∣ v ∉ H } ∪ { U ∖ { v } }. {\mathcal{F}}.{\rm del}{{}^{\prime}}\,{v}=\{H\in\mathcal{F}\mid v\notin H\}\cup\{U\setminus\{v\}\}. |  |

It is easy to verify that this family is an ideal family.

###### Lemma 2.3.

For an ideal family ℱ \mathcal{F} and v ∈ U v\in U, the deletion ℱ. del ​ v ′ {\mathcal{F}}.{\rm del}{{}^{\prime}}\,{v} of v v is also an ideal family on the ground set U ∖ { v } U\setminus\{v\}.

#### *Contraction minor*: ℱ. cont ​ v {\mathcal{F}}.\text{cont}\,{v}

For a set family ℱ \mathcal{F} and v ∈ U v\in U, the contraction of ℱ \mathcal{F} by v v is the collection of all hyperedges containing v v in ℱ \mathcal{F} and remove v v from each hyperedge, i.e.,

 | ℱ. cont v = { H ∖ { v } ∣ v ∈ H, H ∈ ℱ }. {\mathcal{F}}.\text{cont}\,{v}=\{H\setminus\{v\}\mid v\in H,H\in\mathcal{F}\}. |  |

When ℱ \mathcal{F} is an ideal family, ℱ. cont ​ v {\mathcal{F}}.\text{cont}\,{v} is an ideal family under the condition that { v } \{v\} is a hyperedge.

###### Lemma 2.4.

For an ideal family ℱ \mathcal{F} and v ∈ U v\in U with a hyperedge { v } \{v\}, the contraction ℱ. cont ​ v {\mathcal{F}}.\text{cont}\,{v} of v v is an ideal family on the ground set U ∖ { v } U\setminus\{v\}.

###### Proof.

Since { v } \{v\} is a hyperedge, the contraction minor has the empty set. ∎

The following lemma characterizes whether { v } \{v\} is a hyperedge or not, which will be used in the proof of the main theorem.

###### Lemma 2.5.

For an ideal family with | U | ≥ 2 |U|\geq 2, { v } \{v\} is not a hyperedge if and only if deg ℱ ​ v = 1 \mbox{deg}_{\mathcal{F}}v=1.

###### Proof.

Recall that the ground set is always contained in the ideal family. When deg v = 1 v=1, the ground set is the unique hyperedge which contains v v. ∎

#### *Trace minor*: ℱ. trace ​ v {\mathcal{F}}.{\rm trace}\,{v}

For a set family ℱ \mathcal{F} and v ∈ U v\in U, the trace ℱ. trace ​ v {\mathcal{F}}.{\rm trace}\,{v} of ℱ \mathcal{F} by v v is the set family with hyperedges { H ∖ { v } ∣ H ∈ ℱ } \{H\setminus\{v\}\mid H\in\mathcal{F}\}. It is easy to show that the trace of an ideal family is always an ideal family.

###### Lemma 2.6.

For an ideal family ℱ \mathcal{F} and v ∈ U v\in U, the trace ℱ. trace ​ v {\mathcal{F}}.{\rm trace}\,{v} by v v is an ideal family on the ground set U ∖ { v } U\setminus\{v\}.

The trace minor is important in the discussions of intersection-closed families and ideal families, but will not appear explicitly in the proofs in this paper. (When the degree of v v is 1, the trace minor coincides with the deletion for an ideal family, and such a case will appear in the proof of the main theorem.)

## 3 Examples

To make the theoretical concepts more concrete, we provide examples of ideal families and calculate their normalized degree sums.

### 3.1 Ground set with two vertices

Let U = { v 1, v 2 } U=\{v_{1},v_{2}\}. Consider the ideal family ℱ \mathcal{F} defined as:

 | ℱ = { ∅, { v 1 }, { v 2 }, { v 1, v 2 } }. \mathcal{F}=\{\emptyset,\{v_{1}\},\{v_{2}\},\{v_{1},v_{2}\}\}. |  |

This family includes all subsets of U U, satisfying the properties of an ideal family. We have | U | = 2 |U|=2 and | ℱ | = 4 |\mathcal{F}|=4.

The degrees are calculated as follows:

 | deg ℱ ⁡ ( v 1) = 2 ( { v 1 }, { v 1, v 2 }), \deg_{\mathcal{F}}(v_{1})=2\quad\quad(\{v_{1}\},\{v_{1},v_{2}\}), |  |

 | deg ℱ ⁡ ( v 2) = 2 ( { v 2 }, { v 1, v 2 }). \deg_{\mathcal{F}}(v_{2})=2\quad\quad(\{v_{2}\},\{v_{1},v_{2}\}). |  |

The total size of hyperedges is:

 | TSH ​ ( ℱ) = ∑ v ∈ U deg ℱ ⁡ ( v) = 2 + 2 = 4. \text{TSH}(\mathcal{F})=\sum_{v\in U}\deg_{\mathcal{F}}(v)=2+2=4. |  |

Hence, the normalized degree sum is:

 | NDS ​ ( ℱ) = 2 ​ TSH ​ ( ℱ) − | U | ⋅ | ℱ | = 2 ⋅ 4 − 2 ⋅ 4 = 8 − 8 = 0. \text{NDS}(\mathcal{F})=2\text{TSH}(\mathcal{F})-|U|\cdot|\mathcal{F}|=2\cdot 4-2\cdot 4=8-8=0. |  |

Therefore, ℱ \mathcal{F} meets the average rarity condition. It is easy to verify that the normalized degree sum of the power set of a finite set is always 0.

All other ideal families with the ground set of size 2 also have non-positive NDS.

### 3.2 Ground set with three vertices

Let U = { v 1, v 2, v 3 } U=\{v_{1},v_{2},v_{3}\}. Define the ideal family ℱ \mathcal{F} as:

 | ℱ = { ∅, { v 1 }, { v 2 }, { v 3 }, { v 1, v 2 }, { v 1, v 3 }, { v 1, v 2, v 3 } }. \mathcal{F}=\{\emptyset,\{v_{1}\},\{v_{2}\},\{v_{3}\},\{v_{1},v_{2}\},\{v_{1},v_{3}\},\{v_{1},v_{2},v_{3}\}\}. |  |

We have | U | = 3 |U|=3 and | ℱ | = 7 |\mathcal{F}|=7.

The degrees are calculated as follows:

 |  | deg ℱ ⁡ ( v 1) = 4 ( { v 1 }, { v 1, v 2 }, { v 1, v 3 }, { v 1, v 2, v 3 }), \displaystyle\deg_{\mathcal{F}}(v_{1})=4\qquad(\{v_{1}\},\{v_{1},v_{2}\},\{v_{1},v_{3}\},\{v_{1},v_{2},v_{3}\}), |  |

 |  | deg ℱ ⁡ ( v 2) = 3 ( { v 2 }, { v 1, v 2 }, { v 1, v 2, v 3 }), \displaystyle\deg_{\mathcal{F}}(v_{2})=3\qquad(\{v_{2}\},\{v_{1},v_{2}\},\{v_{1},v_{2},v_{3}\}), |  |

 |  | deg ℱ ⁡ ( v 3) = 3 ( { v 3 }, { v 1, v 3 }, { v 1, v 2, v 3 }). \displaystyle\deg_{\mathcal{F}}(v_{3})=3\qquad(\{v_{3}\},\{v_{1},v_{3}\},\{v_{1},v_{2},v_{3}\}). |  |

The total size of hyperedges is:

 | TSH ​ ( ℱ) = ∑ v ∈ U deg ℱ ⁡ ( v) = 4 + 3 + 3 = 10. \text{TSH}(\mathcal{F})=\sum_{v\in U}\deg_{\mathcal{F}}(v)=4+3+3=10. |  |

Hence, the normalized degree sum is:

 | NDS ​ ( ℱ) = 2 ​ TSH ​ ( ℱ) − | U | ⋅ | ℱ | = 2 ⋅ 10 − 3 ⋅ 7 = 20 − 21 = − 1. \text{NDS}(\mathcal{F})=2\text{TSH}(\mathcal{F})-|U|\cdot|\mathcal{F}|=2\cdot 10-3\cdot 7=20-21=-1. |  |

Thus, ℱ \mathcal{F} satisfies the average rarity condition.

### 3.3 Ideal family with a vertex of degree 1 and a large hyperedge

We consider an ideal family with a vertex v v of degree 1 and the hyperedge U \ { v } U\backslash\{v\}. For an ideal family, { v } \{v\} is not a hyperedge when v v has degree 1 (Lemma 2.5). The hyperedges of this ideal family are given by { H ∣ v ∉ H } ∪ { U } \{H\mid v\notin H\}\cup\{U\}. This ideal family appears in one of the cases in the proof of the main theorem.

Let | U | = n |U|=n. The number of hyperedges in this family is:

 | | ℱ | = 2 n − 1 + 1. |\mathcal{F}|=2^{n-1}+1. |  |

The total sum of the sizes of the hyperedges is calculated as:

 | TSH ​ ( ℱ) = ( ∑ i = 0 n − 1 ( n − 1 i) ⋅ i) + n = ( n − 1) ⋅ 2 n − 2 + n. \text{TSH}(\mathcal{F})=\bigg(\sum_{i=0}^{n-1}\binom{n-1}{i}\cdot i\bigg)+n=(n-1)\cdot 2^{n-2}+n. |  |

The normalized degree sum is calculated as:

 | NDS ​ ( ℱ) = 2 ​ TSH ​ ( ℱ) − | U | ⋅ | ℱ | = 2 ​ ( ( n − 1) ⋅ 2 n − 2 + n) − n ⋅ ( 2 n − 1 + 1) = n − 2 n − 1. \text{NDS}(\mathcal{F})=2\text{TSH}(\mathcal{F})-|U|\cdot|\mathcal{F}|=2((n-1)\cdot 2^{n-2}+n)-n\cdot(2^{n-1}+1)=n-2^{n-1}. |  |

This value is non-positive for any natural number n ≥ 1 n\geq 1, hence the family satisfies the average rarity condition.

## 4 The average rarity of ideal families

The following is our main theorem.

###### Theorem 4.1.

For any ideal family ℱ \mathcal{F} on a nonempty finite ground set U U, the normalized degree sum is non-positive:

 | NDS ​ ( ℱ) ≤ 0. \text{NDS}(\mathcal{F})\leq 0. |  |

Consequently, all ideal families satisfy the average rarity condition.

###### Proof.

We prove the theorem using induction on the size of the ground set | U | |U|.

The base case is when | U | = 1 |U|=1. In this case, the hyperedges in the ideal family are ∅ \emptyset and U U. This yields that the normalized degree sum is zero.

For the inductive step, assume that the theorem holds for any ideal family with a ground set of size n − 1 n-1. We verify the statement for an ideal family ℱ \mathcal{F} on U U with | U | = n ≥ 2 |U|=n\geq 2.

By Lemma 2.2 there exists at least one rare vertex in ℱ \mathcal{F}, and choose one arbitrary rare vertex v v. Since v v is rare, we have:

 | 2 ​ deg ℱ ⁡ ( v) − | ℱ | ≤ 0. 2\deg_{\mathcal{F}}(v)-|\mathcal{F}|\leq 0. |  |

[The case deg ℱ ⁡ ( v) = 1 \deg_{\mathcal{F}}(v)=1]
First, we consider the case with deg ℱ ⁡ ( v) = 1 \deg_{\mathcal{F}}(v)=1. The next lemma follows from Lemma 2.5.

###### Lemma 4.1.

For an ideal family ℱ \mathcal{F} with | U | ≥ 2 |U|\geq 2 and v ∈ U v\in U, { v } \{v\} is a hyperedge if and only if deg v ≥ 2 v\geq 2.

When U ∖ { v } U\setminus\{v\} is a hyperedge in ℱ \mathcal{F}, the calculation in Subsection 3.3 shows that NDS ⁡ ( ℱ) ≤ 0 {\rm NDS}(\mathcal{F})\leq 0 and we are done.

When U ∖ { v } U\setminus\{v\} is not a hyperedge in ℱ \mathcal{F}, by the definition of the deletion operation,

 | TSH ( ℱ) = TSH ( ℱ. del v ′) + 1, \text{TSH}(\mathcal{F})=\text{TSH}({\mathcal{F}}.{\rm del}{{}^{\prime}}\,{v})+1, |  |

and

 | | ℱ | = | ℱ. del ′ v |. |\mathcal{F}|=|{\mathcal{F}}.{\rm del}{{}^{\prime}}\,{v}|. |  |

By Lemma 2.3, ℱ. del ​ v ′ {\mathcal{F}}.{\rm del}{{}^{\prime}}\,{v} is an ideal family on U ∖ { v } U\setminus\{v\}. Therefore,

 | NDS ( ℱ. del v ′) = 2 TSH ( ℱ. del v ′) − ( n − 1) | ℱ. del v ′ | ≤ 0 \text{NDS}({\mathcal{F}}.{\rm del}{{}^{\prime}}\,{v})=2\text{TSH}({\mathcal{F}}.{\rm del}{{}^{\prime}}\,{v})-(n-1)|{\mathcal{F}}.{\rm del}{{}^{\prime}}\,{v}|\leq 0 |  |

by the induction hypothesis. Hence, we have

 | NDS ​ ( ℱ) \displaystyle\text{NDS}(\mathcal{F}) | = \displaystyle= | 2 ​ TSH ​ ( ℱ) − n ​ | ℱ | \displaystyle 2\text{TSH}(\mathcal{F})-n|\mathcal{F}| |  |

 |  | = \displaystyle= | 2 ( TSH ( ℱ. del v ′) + 1) − n | ℱ. del v ′ | \displaystyle 2(\text{TSH}({\mathcal{F}}.{\rm del}{{}^{\prime}}\,{v})+1)-n|{\mathcal{F}}.{\rm del}{{}^{\prime}}\,{v}| |  |

 |  | = \displaystyle= | 2 TSH ( ℱ. del v ′) − ( n − 1) | ℱ. del v ′ | + 2 − | ℱ. del v ′ | \displaystyle 2\text{TSH}({\mathcal{F}}.{\rm del}{{}^{\prime}}\,{v})-(n-1)|{\mathcal{F}}.{\rm del}{{}^{\prime}}\,{v}|+2-|{\mathcal{F}}.{\rm del}{{}^{\prime}}\,{v}| |  |

 |  | = \displaystyle= | NDS ( ℱ. del v ′) + ( 2 − | ℱ. del v ′ |) \displaystyle\text{NDS}({\mathcal{F}}.{\rm del}{{}^{\prime}}\,{v})+(2-|{\mathcal{F}}.{\rm del}{{}^{\prime}}\,{v}|) |  |

 |  | ≤ \displaystyle\leq | 0. \displaystyle 0. |  |

Note that | ℱ. del ′ v | ≥ 2 |{\mathcal{F}}.{\rm del}{{}^{\prime}}\,{v}|\geq 2 holds because it contains the empty set and the ground set.

We conclude that NDS ⁡ ( ℱ) ≤ 0 {\rm NDS}(\mathcal{F})\leq 0 in the case deg ℱ ⁡ ( v) = 1 \deg_{\mathcal{F}}(v)=1.

[The case deg ℱ ⁡ ( v) ≥ 2 \deg_{\mathcal{F}}(v)\geq 2]

We consider the case deg ℱ ⁡ ( v) ≥ 2 \deg_{\mathcal{F}}(v)\geq 2, i.e., the case that { v } \{v\} is a hyperedge.

Since ℱ. del ​ v ′ {\mathcal{F}}.{\rm del}{{}^{\prime}}\,{v} and ℱ. cont ​ v {\mathcal{F}}.\text{cont}\,{v} are ideal families by Lemmas 2.3 and 2.6, they satisfy the average rarity condition:

 | NDS ( ℱ. del v ′) ≤ 0, NDS ( ℱ. cont v) ≤ 0. \text{NDS}({\mathcal{F}}.{\rm del}{{}^{\prime}}\,{v})\leq 0,\quad\text{NDS}({\mathcal{F}}.\text{cont}\,{v})\leq 0. |  |

By definitions, we have the following.

 | NDS ( ℱ. cont v) = 2 TSH ( ℱ. cont v) − ( n − 1) | ℱ. cont v |, \text{NDS}({\mathcal{F}}.\text{cont}\,{v})=2\text{TSH}({\mathcal{F}}.\text{cont}\,{v})-(n-1)|{\mathcal{F}}.\text{cont}\,{v}|, |  |

 | NDS ( ℱ. del v ′) = 2 TSH ( ℱ. del v ′) − ( n − 1) | ℱ. del v ′ |, \text{NDS}({\mathcal{F}}.{\rm del}{{}^{\prime}}\,{v})=2\text{TSH}({\mathcal{F}}.{\rm del}{{}^{\prime}}\,{v})-(n-1)|{\mathcal{F}}.{\rm del}{{}^{\prime}}\,{v}|, |  |

 | | ℱ | = | ℱ. cont v | + | ℱ. del v |, |\mathcal{F}|=|{\mathcal{F}}.\text{cont}\,{v}|+|{\mathcal{F}}.{\rm del}\,{v}|, |  |

 | TSH ( ℱ) = TSH ( ℱ. cont v) + TSH ( ℱ. del v) + deg ℱ v. \text{TSH}(\mathcal{F})=\text{TSH}({\mathcal{F}}.\text{cont}\,{v})+\text{TSH}({\mathcal{F}}.{\rm del}\,{v})+\text{deg}_{\mathcal{F}}v. |  |

We divide the cases depending on whether U ∖ { v } U\setminus\{v\} is a hyperedge of ℱ \mathcal{F} or not.

- •

In the case that U ∖ { v } U\setminus\{v\} is a hyperedge of ℱ \mathcal{F}, we have

 | | ℱ. del v | = | ℱ. del ′ v |, |{\mathcal{F}}.{\rm del}\,{v}|=|{\mathcal{F}}.{\rm del}{{}^{\prime}}\,{v}|, |  |

and

 | TSH ( ℱ. del v) = TSH ( ℱ. del v ′). \text{TSH}({\mathcal{F}}.{\rm del}\,{v})=\text{TSH}({\mathcal{F}}.{\rm del}{{}^{\prime}}\,{v}). |  |

The statement is deduced as follows.

 |  |  | NDS ​ ( ℱ) \displaystyle\text{NDS}({\mathcal{F}}) |  |

 |  | = \displaystyle= | 2 ​ TSH ​ ( ℱ) − n ​ | ℱ | \displaystyle 2\text{TSH}({\mathcal{F}})-n|\mathcal{F}| |  |

 |  | = \displaystyle= | 2 ( TSH ( ℱ. cont v) + TSH ( ℱ. del v) + deg ℱ) − n ( | ℱ. cont v | + | ℱ. del v |) \displaystyle 2(\text{TSH}({\mathcal{F}}.\text{cont}\,{v})+\text{TSH}({\mathcal{F}}.{\rm del}\,{v})+\text{deg}_{\mathcal{F}})-n(|{\mathcal{F}}.\text{cont}\,{v}|+|{\mathcal{F}}.{\rm del}\,{v}|) |  |

 |  | = \displaystyle= | ( 2 TSH ( ℱ. cont v) − ( n − 1) | ℱ. cont v |) + ( 2 TSH ( ℱ. del v) − ( n − 1) | ℱ. del v |) \displaystyle(2\text{TSH}({\mathcal{F}}.\text{cont}\,{v})-(n-1)|{\mathcal{F}}.\text{cont}\,{v}|)+(2\text{TSH}({\mathcal{F}}.{\rm del}\,{v})-(n-1)|{\mathcal{F}}.{\rm del}\,{v}|) |  |

 |  |  | + 2 deg ℱ ( v) − ( | ℱ. cont v | + | ℱ. del v |) \displaystyle+2\deg_{\mathcal{F}}(v)-(|{\mathcal{F}}.\text{cont}\,{v}|+|{\mathcal{F}}.{\rm del}\,{v}|) |  |

 |  | = \displaystyle= | NDS ( ℱ. del v ′) + NDS ( ℱ. cont v) + 2 deg ℱ ( v) − | ℱ | \displaystyle\text{NDS}({\mathcal{F}}.{\rm del}{{}^{\prime}}\,{v})+\text{NDS}({\mathcal{F}}.\text{cont}\,{v})+2\deg_{\mathcal{F}}(v)-|\mathcal{F}| |  |

 |  | ≤ \displaystyle\leq | 0. \displaystyle 0. |  |

The last inequality follows from 2 ​ deg ℱ ⁡ ( v) − | ℱ | ≤ 0 2\deg_{\mathcal{F}}(v)-|\mathcal{F}|\leq 0.

- •

If U ∖ { v } U\setminus\{v\} is not a hyperedge of ℱ \mathcal{F}, we have

 | | ℱ. del v | = | ℱ. del ′ v | − 1, |{\mathcal{F}}.{\rm del}\,{v}|=|{\mathcal{F}}.{\rm del}{{}^{\prime}}\,{v}|-1, |  |

and

 | TSH ( ℱ. del v) = TSH ( ℱ. del v ′) − n + 1. \text{TSH}({\mathcal{F}}.{\rm del}\,{v})=\text{TSH}({\mathcal{F}}.{\rm del}{{}^{\prime}}\,{v})-n+1. |  |

Hence,

 | NDS ( ℱ. del v) \displaystyle\text{NDS}({\mathcal{F}}.{\rm del}\,{v}) | = \displaystyle= | 2 T S H ( ℱ. del v) − ( n − 1) | ℱ. del v | \displaystyle 2{\rm TSH}({\mathcal{F}}.{\rm del}\,{v})-(n-1)|{\mathcal{F}}.{\rm del}\,{v}| |  |

 |  | = \displaystyle= | 2 TSH ( ℱ. del v ′) − ( n − 1) | ℱ. del v ′ | − 2 n + 2 + ( n − 1) \displaystyle 2\text{TSH}({\mathcal{F}}.{\rm del}{{}^{\prime}}\,{v})-(n-1)|{\mathcal{F}}.{\rm del}{{}^{\prime}}\,{v}|-2n+2+(n-1) |  |

 |  | = \displaystyle= | NDS ( ℱ. del v ′) − n + 1. \displaystyle\text{NDS}({\mathcal{F}}.{\rm del}{{}^{\prime}}\,{v})-n+1. |  |

The statement is verified as follows.

 |  |  | NDS ​ ( ℱ) \displaystyle\text{NDS}({\mathcal{F}}) |  |

 |  | = \displaystyle= | ( 2 TSH ( ℱ. cont v) − ( n − 1) | ℱ. cont v |) + ( 2 TSH ( ℱ. del v) − ( n − 1) | ℱ. del v |) \displaystyle(2\text{TSH}({\mathcal{F}}.\text{cont}\,{v})-(n-1)|{\mathcal{F}}.\text{cont}\,{v}|)+(2\text{TSH}({\mathcal{F}}.{\rm del}\,{v})-(n-1)|{\mathcal{F}}.{\rm del}\,{v}|) |  |

 |  |  | + 2 deg ℱ ( v) − ( | ℱ. cont v | + | ℱ. del v |) \displaystyle+2\deg_{\mathcal{F}}(v)-(|{\mathcal{F}}.\text{cont}\,{v}|+|{\mathcal{F}}.{\rm del}\,{v}|) |  |

 |  | = \displaystyle= | ( 2 TSH ( ℱ. cont v) − ( n − 1) | ℱ. cont v |) \displaystyle(2\text{TSH}({\mathcal{F}}.\text{cont}\,{v})-(n-1)|{\mathcal{F}}.\text{cont}\,{v}|) |  |

 |  |  | + ( 2 ( TSH ( ℱ. del v ′) − n + 1) − ( n − 1) ( | ℱ. del v ′ | − 1) \displaystyle+(2(\text{TSH}({\mathcal{F}}.{\rm del}{{}^{\prime}}\,{v})-n+1)-(n-1)(|{\mathcal{F}}.{\rm del}{{}^{\prime}}\,{v}|-1) |  |

 |  |  | + 2 deg ℱ ( v) − ( | ℱ. cont v | + | ℱ. del v |) \displaystyle+2\deg_{\mathcal{F}}(v)-(|{\mathcal{F}}.\text{cont}\,{v}|+|{\mathcal{F}}.{\rm del}\,{v}|) |  |

 |  | = \displaystyle= | NDS ( ℱ. del v ′) + NDS ( ℱ. cont v) + ( 2 deg ℱ ( v) − | ℱ |) − n + 1 \displaystyle\text{NDS}({\mathcal{F}}.{\rm del}{{}^{\prime}}\,{v})+\text{NDS}({\mathcal{F}}.\text{cont}\,{v})+(2\deg_{\mathcal{F}}(v)-|\mathcal{F}|)-n+1 |  |

 |  | ≤ \displaystyle\leq | 0. \displaystyle 0. |  |

Recall that 2 ​ deg ℱ ⁡ ( v) − | ℱ | ≤ 0 2\deg_{\mathcal{F}}(v)-|\mathcal{F}|\leq 0 and n ≥ 2 n\geq 2.

∎

Remark: The proof relies on ℱ \mathcal{F} being an ideal family to guarantee the existence of a rare vertex v v. In addition, it is used to ensure that the contraction ℱ. cont ​ v {\mathcal{F}}.\text{cont}\,{v} includes the empty set. For a general intersection-closed family, it may not contain the empty set. In the base case, NDS ≤ 0 {\rm NDS}\leq 0 is not guaranteed if the empty set is not contained in the family.

## 5 Formalization in Lean 4

In this section, we present a formalized proof of the main theorem in Lean 4. The code shown here is slightly simplified from the full implementation to enhance clarity, such as by excluding conversions between natural numbers and integers. The complete implementation can be found in the repository [13].

### 5.1 Basic Definitions in Lean 4

Below, we outline the core definitions employed in our Lean 4 formalization.

[⬇][3]

-- Definition of set families

structure SetFamily ( α \alpha: Type):=

( ground: Finset α \alpha)

( sets: Finset α \alpha → \rightarrow Prop)

( inc_ground: ∀ \forall s, sets s → \rightarrow s ⊆ \subseteq ground)

( nonempty_ground: ground. Nonempty)

-- Definition of intersection - closed families

def isIntersectionClosedFamily ( F: SetFamily α \alpha): Prop:=

∀ \forall { s t: Finset α \alpha }, F. sets s → \rightarrow F. sets t → \rightarrow F. sets ( s ∩ \cap t)

-- Definition of rare vertices

def is_rare ( F: SetFamily α \alpha) ( v: α \alpha): Prop:=

2 *F. degree v - F. number_of_hyperedges ≤ \leq 0

-- Ideal families

structure IdealFamily ( α \alpha: Type) extends SetFamily α \alpha:=

( has_empty: sets ∅ \emptyset)

( has_ground: sets ground)

( downward_closed: ∀ \forall ( A B: Finset α \alpha), sets B → \rightarrow B ≠ \neq ground → \rightarrow A ⊆ \subseteq B → \rightarrow sets A)

-- Total size of hyperedges

def SetFamily. total_size_of_hyperedges ( F: SetFamily α \alpha): 𝐙 \mathbf{Z}:=

(( Finset. powerset F. ground). filter F. sets). sum Finset. card

-- Number of hyperedges

def SetFamily. number_of_hyperedges ( F: SetFamily α \alpha): 𝐙 \mathbf{Z}:=

(( Finset. powerset F. ground). filter F. sets). card

-- Normalized degree sum

def SetFamily. normalized_degree_sum ( F: SetFamily α \alpha):=

2 *F. total_size_of_hyperedges - F. number_of_hyperedges *F. ground. card

Listing 1: Definition of SetFamily and IdealFamily in Lean 4

In this formalization: ‘`SetFamily`’ represents a general set family on finite type ‘ α \alpha ’. ‘`IdealFamily`’ extends ‘`SetFamily`’ with the specific properties of an ideal family.
‘`downward_closed`’ is a condition that hyperedges are closed with respect to taking subsets. ‘`Set.card`’ means the cardinality of the set. The ground set U U of a set family ‘`F`’ is written as ‘`F.ground`’.

The Lean 4 code below states Frankl’s conjecture, with ‘`sorry`’ indicating that the proof remains incomplete.

[⬇][4]

theorem frankl_conjecture:

∀ \forall ( F: SetFamily α \alpha):

has_empty F → \rightarrow

has_univ F → \rightarrow

is_closed_under_intersection F → \rightarrow

∃ ( v ∈ 𝙲𝙻𝙾𝚂𝙴 \exists(v\in F. ground), 2 *F. degree v ≤ \leq F. number_of_hyperedges:= sorry

Listing 2: Frankl’s conjecture

Here, `F.degree v`indicates the degree of a set family ℱ \mathcal{F} at v v.

### 5.2 Basic structure of the proof of the main theorem

[⬇][5]

theorem ideal_average_rarity ( F: IdealFamily α \alpha):

F. normalized_degree_sum ≤ 0 \leq 0:= by

-- Induction on the size of the ground set

induction F. ground. card with

| one =>

exact nds_nonposi_card_one F

| succ ih => -- ih is induction hypothesis.

-- v is a rare vertex, and rv provides the evidence for it.

obtain ⟨ v, r ​ v ⟩ \langle v,rv\rangle:= ideal_version_of_frankl_conjecture F

have geq2: F. ground. card ≥ 2 \geq 2:= by sorry

-- proof for this is omitted here.

by_cases h_v: F. sets { v }

case pos =>

-- Now consider whether ( F. ground \ { v }) is a hyperedge

by_cases h_uv: F. sets ( F. ground \ { v })

case pos =>

-- If ( U \{ v }) is a hyperedge

exact case_hs_haveUV F v h_v rv geq2 h_uv ih

case neg =>

-- If ( U \{ v }) is not a hyperedge

exact case_hs_noneUV F v h_v rv geq2 h_uv ih

case neg =>

by_cases h_uv: F. sets ( F. ground \ { v })

case pos =>

-- If ( U \{ v }) is a hyperedge

exact case_degone_haveUV F v rv geq2 h_v h_uv

case neg =>

exact case_degone_noneUV F v rv geq2 h_v h_uv ih

Listing 3: Concept proof of the main theorem in Lean 4

The code above offers a conceptual overview rather than executable Lean 4 code. Still, readers versed in Lean 4 syntax can view it as a pseudocode capturing the proof’s overall structure.

In this code: The sentences followed by ‘`--`’ are comments. In theorem
‘`ideal_average_rarity``(F : IdealFamily`α \alpha`)`: `normalized_degree_sum`F ≤ \leq 0’, the part of ‘`(F : IdealFamily`α \alpha`)`’ is an assumption, and the part of ‘`normalized_degree_sum F `≤ \leq 0 ’ is the goal to be proved. Using tactics in Lean 4, we can transform the goal step by step and then complete the proof by demonstrating that the goal follows from the assumptions, for example, using `exact`. The part following by ‘`:=`’ is the proof of the theorem.

The proof proceeds by induction of ‘`F.ground`’, the cardinality of the ground set of the ideal family. For the base case, we handle the situation where the ground set is of size one.

In the inductive step, we select a vertex v v as a rare vertex by using theorem
We define the deletion and contraction families ‘ ℱ. del ​ v ′ {\mathcal{F}}.{\rm del}{{}^{\prime}}\,{v} ’ and ‘ ℱ. cont ​ v {\mathcal{F}}.\text{cont}\,{v} ’. Under the appropriate assumptions, it is clear that these are ideal families. Since these minors have a smaller ground set, we can apply the induction hypothesis to both minors. Since the deletion minors and contraction minors differ depending on whether { v } \{v\} or F.ground ∖ { v } \text{F.ground}\setminus\{v\} is a hyperedge, it is necessary to consider separate cases. To resolve subcases, we use lemma ‘`case_hs_haveUV`’ and others. The part following from the lemma name corresponds to the argument and is assumed to hold.

In the proof, `cases`represents case analysis. ‘`case pos =>`’ indicates the case where the condition holds, while ‘`case neg =>`’ represents the case where the condition does not hold. ‘`have label:statement`’ is a mini lemma used in the proof. ‘`sorry`’ represents the omission of a proof.

The next code is a concise version of the statement of a key lemma when U ∖ { v } U\setminus\{v\} and { v } \{v\} are both hyperedges. The part before the outer colon is the assumption of this lemma, and the part after the outer colon is the goal of this lemma.

The following lemma in Lean 4 corresponds to

 | NDS ( ℱ) = NDS ( ℱ. del v) + NDS ( ℱ. cont v) + 2 deg ℱ ( v) − | ℱ |. \text{NDS}({\mathcal{F}})=\text{NDS}({\mathcal{F}}.{\rm del}\,{v})+\text{NDS}({\mathcal{F}}.\text{cont}\,{v})+2\deg_{\mathcal{F}}(v)-|\mathcal{F}|. |  |

[⬇][6]

lemma nds_set_minors ( F: IdealFamily α \alpha) ( v: α \alpha) ( hv: v ∈ \in F. ground) ( geq2: F. ground. card ≥ \geq 2)

( hs: F. sets { v }):

F. toSetFamily. normalized_degree_sum =

( F. toSetFamily. deletion v hv geq2). normalized_degree_sum +

( F. toSetFamily. contraction v hv geq2). normalized_degree_sum

+ 2 *( F. degree v) - F. number_of_hyperedges:=

Listing 4: Concept statement of a key lemma in Lean 4

The deletion ℱ. del ​ v ′ {\mathcal{F}}.{\rm del}{{}^{\prime}}\,{v} for set families corresponds to “`F.toSetFamily.deletion’ v hv geq2`” in Lean 4 code. The deletion ℱ. del ​ v ′ {\mathcal{F}}.{\rm del}{{}^{\prime}}\,{v} for ideal families corresponds to ‘`F.deletion v hv geq2`’. The following lemma corresponds to NDS ( ℱ. del v) = NDS ( ℱ. del v ′) − n + 1 \text{NDS}({\mathcal{F}}.{\rm del}\,{v})=\text{NDS}({\mathcal{F}}.{\rm del}{{}^{\prime}}\,{v})-n+1 under the assumption that F.ground ∖ { 𝚟 } \verb+F.ground+{\tt\setminus\{v\}} is not a hyperedge.

[⬇][7]

lemma nds_deletion_noneuv ( F: IdealFamily α \alpha) ( v: α \alpha) ( hv: v ∈ \in F. ground) ( geq2: F. ground. card ≥ \geq 2)

( h_uv: ¬ \neg F. sets ( F. ground \ { v })):

( F. deletion ’ v hv geq2). normalized_degree_sum = ( F. toSetFamily. deletion v hv geq2). normalized_degree_sum + F. ground. card - 1:=

Listing 5: Relation between deletion and ideal deletion in Lean 4

We connect the normalized degree sums through the relationships defined earlier. Then, by applying the Lean 4 tactic ‘`linarith`’ to resolve the linear inequalities, we establish that ‘`normalized_degree_sum`F ≤ \leq 0 ’.

The full formal proof of our result by Lean 4 is published in our GitHub repository [13]: [https://github.com/kashiwabarakenji/][8]

## 6 Concluding remarks

We have shown that every ideal family has a non-positive normalized degree sum, meaning it satisfies the average rarity condition, using induction on the size of the ground set. This proof offers insights into understanding how intersection-closed families will meet the average rarity condition. Future research will explore the applicability of the average rarity condition to broader classes of intersection-closed families and further developments related to Frankl’s conjecture.

We also formalized the proof in Lean 4. As more theorems in this field are formalized in Lean 4 and made publicly available, this could enable AI to learn from them, enhancing its capabilities in combinatorial research.

By assuming that a set family has the ground set as one of its hyperedges, a set family closed under intersection can be represented as a closure system. Consequently, the set family can be expressed in terms of rooted circuits. The approach of considering Frankl’s conjecture in the context of rooted circuits will be explored in a separate paper in the future.

This paper establishes that ideal families are average rare by using a lemma ensuring a rare vertex exists. Generally, exploring the average rarity proves advantageous because it implies the existence of a rare vertex. However, the approach taken in this paper is in a sense reversed: we deduced the average rarity of ideal families from the existence of a rare vertex. Whether average rarity can be established independently of the existence of a rare vertex remains unresolved.

## References

- [1] T. Abe, Strong semimodular lattices and Frankl’s conjecture, Algebra Universalis. 44 (2000), 379–382.
- [2] R. Alweiss, B. Huang, M. Sellke, Improved lower bound for Frankl’s union-closed sets conjecture (2022). arXiv:2211.11731 [https://arxiv.org/abs/2211.11731][9]
- [3] I. Bošnjak and P. Marković, The 11-element case of Frankl’s conjecture, Electronic Journal of Combinatorics 15 (2008), R88.
- [4] H. Bruhn and O. Schaudt, The journey of the Union-Closed Sets Conjecture, Graphs and Combinatorics 31 (2015), 2043–2074.
- [5] S. Cambie, Better bounds for the union-closed sets conjecture using the entropy approach (2022). arXiv:2212.12500 [https://arxiv.org/abs/2212.12500][10]
- [6] Z. Chase, S. Lovett, Approximate union closed conjecture (2022). arXiv:2211.11689 [https://arxiv.org/abs/2211.11689][11]
- [7] G. Czédli, M. Maróti and E.T. Schmidt, On the scope of averaging for Frankl’s Conjecture, Order 26 (2009), 31–48.
- [8] P. Frankl, On the Union-Closed Sets Conjecture, Unpublished manuscript, 1979.
- [9] J. Gilmer, A constant lower bound for the Union-Closed Sets Conjecture (2022). arXiv:2202.10087 [https://arxiv.org/abs/2202.10087][12]
- [10] GitHub, GitHub Copilot. [https://github.com/features/copilot][13]
- [11] A. Gusakov, Formalizing the excluded minor characterization of binary matroids in the Lean theorem prover, Master Thesis, University of Waterloo, 2024. [https://uwspace.uwaterloo.ca/items/d35d17be-485d-4f60-8696-4dce7ae907bb][14]
- [12] M. Hachimori and K. Kashiwabara, Several minimality concepts related to Frankl’s conjecture, Graphs and Combinatorics 40 (2024), article 130.
- [13] K. Kashiwabara, Formal proof of a problem of ideal families by Lean 4, GitHub. [https://github.com/kashiwabarakenji/frankl_lean/][15]
- [14] Lean Copilot Team, “Lean Copilot: Assisting formal proof development in Lean,” Available at: [https://github.com/lean-dojo/LeanCopilot][16]
- [15] LeanSearch, [https://leansearch.net][17]
- [16] J. Liu, Improving the lower bound for the union-closed sets conjecture via conditionally IID coupling, 58th Annual Conference on Information Sciences and Systems (CISS), IEEE, 2024.
- [17] F. Marić, M. Živković, and B. Vucković, Formalizing Frankl’s conjecture: FC-families (2012). arXiv:1207.3604 [https://arxiv.org/abs/1207.3604][18]
- [18] M. J. Moghaddas Mehr, A note on the Union-closed Sets Conjecture (2023) arXiv:2309.01704 [https://arxiv.org/abs/2309.01704][19]
- [19] R. Morris, FC-families and improved bounds for Frankl’s conjecture, European Journal of Combinatorics 27 (2006), 269–282.
- [20] L. de Moura et al., The Lean 4 theorem prover and programming language, Proceedings of the 13th International Conference on Interactive Theorem Proving (ITP 2022), 2021. [https://lean-lang.org/papers/lean4.pdf][20]
- [21] N. Nagel, Notes on the Union Closed Sets Conjecture (2022). arXiv:2208.03803 [https://arxiv.org/abs/2208.03803][21]
- [22] OpenAI. ChatGPT, [https://openai.com][22]
- [23] L. Pebody, Extension of a method of Gilmer (2022). arXiv:2211.13139 [https://arxiv.org/abs/2211.13139][23]
- [24] B. Poonen, Union-closed families, Journal of Combinatorial Theory, Series A 59 (1992), 253–268.
- [25] J. Reinhold, Frankl’s conjecture is true for lower semimodular lattices, Graphs and Combinatorics, 16 (2000), 115–116.
- [26] I. Roberts and J. Simpson, A note on the Union-Closed Sets Conjecture, Australasian Journal of Combinatorics 47 (2010), 265–267.
- [27] W. Sawin, An improved lower bound for the union-closed set conjecture (2022). arXiv:2211.11504. [https://arxiv.org/pdf/2211.11504][24]
- [28] L. Yu, Dimension-free bounds for the union-closed sets conjecture. Entropy 25 (2023), 767.

### Funding Statement

The authors have no relevant financial or non-financial interests to disclose.

### Data Availability Statement

All formalized proofs and related Lean 4 source code used in this article are publicly available at the following GitHub repository URL and can be freely accessed and verified.
[https://github.com/kashiwabarakenji/frankl_lean][25]
No proprietary or confidential data were used.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: data:text/plain;base64,LS0gRGVmaW5pdGlvbiBvZiBzZXQgZmFtaWxpZXMKc3RydWN0dXJlIFNldEZhbWlseSAowqckXGFscGhhJMKnIDogVHlwZSkgOj0KICAoZ3JvdW5kIDogRmluc2V0IMKnJFxhbHBoYSTCpykKICAoc2V0cyA6IEZpbnNldCDCpyRcYWxwaGEkwqcgwqckXHJpZ2h0YXJyb3ckwqcgUHJvcCkKICAoaW5jX2dyb3VuZCA6IMKnJFxmb3JhbGwkwqcgcywgc2V0cyBzIMKnJFxyaWdodGFycm93JMKnIHMgwqckXHN1YnNldGVxJMKnIGdyb3VuZCkKICAobm9uZW1wdHlfZ3JvdW5kIDogZ3JvdW5kLk5vbmVtcHR5KQoKLS0gRGVmaW5pdGlvbiBvZiBpbnRlcnNlY3Rpb24tY2xvc2VkIGZhbWlsaWVzCmRlZiBpc0ludGVyc2VjdGlvbkNsb3NlZEZhbWlseSAgKEYgOiBTZXRGYW1pbHkgwqckXGFscGhhJMKnKSA6IFByb3AgOj0KICDCpyRcZm9yYWxsJMKnIHtzIHQgOiBGaW5zZXQgwqckXGFscGhhJMKnfSwgRi5zZXRzIHMgwqckXHJpZ2h0YXJyb3ckwqcgRi5zZXRzIHQgwqckXHJpZ2h0YXJyb3ckwqcgRi5zZXRzIChzIMKnJFxjYXAkwqcgdCkKCi0tIERlZmluaXRpb24gb2YgcmFyZSB2ZXJ0aWNlcwpkZWYgaXNfcmFyZSAoRiA6IFNldEZhbWlseSDCpyRcYWxwaGEkwqcpICh2IDogwqckXGFscGhhJMKnKSA6IFByb3AgOj0KICAyICogRi5kZWdyZWUgdiAtIEYubnVtYmVyX29mX2h5cGVyZWRnZXMgwqckXGxlcSTCpyAwCgotLSBJZGVhbCBmYW1pbGllcwpzdHJ1Y3R1cmUgSWRlYWxGYW1pbHkgICjCpyRcYWxwaGEkwqcgOiBUeXBlKSBleHRlbmRzIFNldEZhbWlseSDCpyRcYWxwaGEkwqcgOj0KICAoaGFzX2VtcHR5IDogc2V0cyDCpyRcZW1wdHlzZXQkwqcpCiAgKGhhc19ncm91bmQgOiBzZXRzIGdyb3VuZCkKICAoZG93bndhcmRfY2xvc2VkIDogwqckXGZvcmFsbCTCpyAoQSBCIDogRmluc2V0IMKnJFxhbHBoYSTCpyksIHNldHMgQiDCpyRccmlnaHRhcnJvdyTCpyBCIMKnJFxuZXEkwqcgZ3JvdW5kIMKnJFxyaWdodGFycm93JMKnIEEgwqckXHN1YnNldGVxJMKnIEIgwqckXHJpZ2h0YXJyb3ckwqcgc2V0cyBBKQoKLS0gVG90YWwgc2l6ZSBvZiBoeXBlcmVkZ2VzCmRlZiBTZXRGYW1pbHkudG90YWxfc2l6ZV9vZl9oeXBlcmVkZ2VzIChGIDogU2V0RmFtaWx5IMKnJFxhbHBoYSTCpykgICA6IMKnJFxtYXRoYmYgWiTCpyA6PQogICAoKEZpbnNldC5wb3dlcnNldCBGLmdyb3VuZCkuZmlsdGVyIEYuc2V0cykuc3VtIEZpbnNldC5jYXJkCgotLSBOdW1iZXIgb2YgaHlwZXJlZGdlcwpkZWYgU2V0RmFtaWx5Lm51bWJlcl9vZl9oeXBlcmVkZ2VzICAoRiA6IFNldEZhbWlseSDCpyRcYWxwaGEkwqcpOiDCpyRcbWF0aGJmIFokwqcgOj0KICAgKChGaW5zZXQucG93ZXJzZXQgRi5ncm91bmQpLmZpbHRlciBGLnNldHMpLmNhcmQKCi0tIE5vcm1hbGl6ZWQgZGVncmVlIHN1bQpkZWYgU2V0RmFtaWx5Lm5vcm1hbGl6ZWRfZGVncmVlX3N1bSAoRiA6IFNldEZhbWlseSDCpyRcYWxwaGEkwqcpIDo9CiAgMiAqIEYudG90YWxfc2l6ZV9vZl9oeXBlcmVkZ2VzIC0gRi5udW1iZXJfb2ZfaHlwZXJlZGdlcypGLmdyb3VuZC5jYXJk
[4]: data:text/plain;base64,dGhlb3JlbSBmcmFua2xfY29uamVjdHVyZSA6CiAgwqckXGZvcmFsbCTCpyAgKEYgOiBTZXRGYW1pbHkgwqckXGFscGhhJMKnKToKICAgIGhhc19lbXB0eSAgRiDCpyRccmlnaHRhcnJvdyTCpwogICAgaGFzX3VuaXYgRiDCpyRccmlnaHRhcnJvdyTCpwogICAgaXNfY2xvc2VkX3VuZGVyX2ludGVyc2VjdGlvbiBGIMKnJFxyaWdodGFycm93JMKnCiAgICDCpyRcZXhpc3RzICh2IFxpbiTCpyBGLmdyb3VuZCksIDIgKiBGLmRlZ3JlZSB2IMKnJFxsZXEkwqcgRi5udW1iZXJfb2ZfaHlwZXJlZGdlcyA6PSBzb3JyeQ==
[5]: data:text/plain;base64,dGhlb3JlbSBpZGVhbF9hdmVyYWdlX3Jhcml0eSAoRiA6IElkZWFsRmFtaWx5IMKnJFxhbHBoYSTCpyk6CiAgRi5ub3JtYWxpemVkX2RlZ3JlZV9zdW0gwqckXGxlcSAwICTCpzo9IGJ5CiAgLS0gSW5kdWN0aW9uIG9uIHRoZSBzaXplIG9mIHRoZSBncm91bmQgc2V0CiAgaW5kdWN0aW9uIEYuZ3JvdW5kLmNhcmQgd2l0aAogIHwgb25lID0+CiAgICAgIGV4YWN0IG5kc19ub25wb3NpX2NhcmRfb25lIEYKICB8IHN1Y2MgaWggPT4gLS0gaWggaXMgaW5kdWN0aW9uIGh5cG90aGVzaXMuCiAgICAtLSB2IGlzIGEgcmFyZSB2ZXJ0ZXgsIGFuZCBydiBwcm92aWRlcyB0aGUgZXZpZGVuY2UgZm9yIGl0LgogICAgb2J0YWluIMKnJFxsYW5nbGUgdiwgcnYgXHJhbmdsZSTCpyA6PSBpZGVhbF92ZXJzaW9uX29mX2ZyYW5rbF9jb25qZWN0dXJlIEYKCiAgICBoYXZlIGdlcTI6IEYuZ3JvdW5kLmNhcmQgwqckIFxnZXEgMiAkwqcgOj0gYnkgc29ycnkKICAgIC0tIHByb29mIGZvciB0aGlzIGlzIG9taXR0ZWQgaGVyZS4KCiAgICBieV9jYXNlcyBoX3YgOiBGLnNldHMge3Z9CiAgICBjYXNlIHBvcyA9PgogICAgICAtLSBOb3cgY29uc2lkZXIgd2hldGhlciAoRi5ncm91bmQgXCB7dn0pIGlzIGEgaHlwZXJlZGdlCiAgICAgIGJ5X2Nhc2VzIGhfdXYgOiBGLnNldHMgKEYuZ3JvdW5kIFwge3Z9KQogICAgICBjYXNlIHBvcyA9PgogICAgICAgIC0tIElmIChVXHt2fSkgaXMgYSBoeXBlcmVkZ2UKICAgICAgICBleGFjdCBjYXNlX2hzX2hhdmVVViBGIHYgaF92IHJ2IGdlcTIgaF91diBpaAogICAgICBjYXNlIG5lZyA9PgogICAgICAgIC0tIElmIChVXHt2fSkgaXMgbm90IGEgaHlwZXJlZGdlCiAgICAgICAgZXhhY3QgY2FzZV9oc19ub25lVVYgRiB2IGhfdiBydiBnZXEyIGhfdXYgaWgKICAgIGNhc2UgbmVnID0+CiAgICAgIGJ5X2Nhc2VzIGhfdXYgOiBGLnNldHMgKEYuZ3JvdW5kIFwge3Z9KQogICAgICBjYXNlIHBvcyA9PgogICAgICAgIC0tIElmIChVXHt2fSkgaXMgYSBoeXBlcmVkZ2UKICAgICAgICBleGFjdCBjYXNlX2RlZ29uZV9oYXZlVVYgRiB2IHJ2IGdlcTIgaF92IGhfdXYKICAgICAgY2FzZSBuZWcgPT4KICAgICAgICBleGFjdCBjYXNlX2RlZ29uZV9ub25lVVYgRiB2IHJ2IGdlcTIgaF92IGhfdXYgaWg=
[6]: data:text/plain;base64,bGVtbWEgbmRzX3NldF9taW5vcnMgKEYgOiBJZGVhbEZhbWlseSDCpyRcYWxwaGEkwqcpICAodiA6IMKnJFxhbHBoYSTCpykgKGh2IDogdiDCpyRcaW4kwqcgRi5ncm91bmQpIChnZXEyOiBGLmdyb3VuZC5jYXJkIMKnJFxnZXEkwqcgMikKIChocyA6IEYuc2V0cyB7dn0pOgogIEYudG9TZXRGYW1pbHkubm9ybWFsaXplZF9kZWdyZWVfc3VtID0KICAoRi50b1NldEZhbWlseS5kZWxldGlvbiB2IGh2IGdlcTIpLm5vcm1hbGl6ZWRfZGVncmVlX3N1bSArCiAgKEYudG9TZXRGYW1pbHkuY29udHJhY3Rpb24gdiBodiBnZXEyKS5ub3JtYWxpemVkX2RlZ3JlZV9zdW0KICArIDIgKiAoRi5kZWdyZWUgdikgLSBGLm51bWJlcl9vZl9oeXBlcmVkZ2VzIDo9
[7]: data:text/plain;base64,bGVtbWEgbmRzX2RlbGV0aW9uX25vbmV1diAoRiA6IElkZWFsRmFtaWx5IMKnJFxhbHBoYSTCpykgICh2IDogwqckXGFscGhhJMKnKSAoaHYgOiB2IMKnJFxpbiTCpyBGLmdyb3VuZCkgKGdlcTI6IEYuZ3JvdW5kLmNhcmQgwqckXGdlcSTCpyAyKQogICAoaF91diA6IMKnJFxuZWckwqdGLnNldHMgKEYuZ3JvdW5kIFwge3Z9KSkgOgogIChGLmRlbGV0aW9uJyB2IGh2IGdlcTIpLm5vcm1hbGl6ZWRfZGVncmVlX3N1bSA9IChGLnRvU2V0RmFtaWx5LmRlbGV0aW9uIHYgaHYgZ2VxMikubm9ybWFsaXplZF9kZWdyZWVfc3VtICsgRi5ncm91bmQuY2FyZCAtIDEgOj0=
[8]: https://github.com/kashiwabarakenji/
[9]: https://arxiv.org/pdf/2211.11731
[10]: https://arxiv.org/pdf/2212.12500
[11]: https://arxiv.org/pdf/2211.11689
[12]: https://arxiv.org/pdf/2202.10087
[13]: https://github.com/features/copilot
[14]: https://uwspace.uwaterloo.ca/items/d35d17be-485d-4f60-8696-4dce7ae907bb
[15]: https://github.com/kashiwabarakenji/frankl_lean/
[16]: https://github.com/lean-dojo/LeanCopilot
[17]: https://leansearch.net
[18]: https://arxiv.org/pdf/1207.3604
[19]: https://arxiv.org/pdf/2309.01704
[20]: https://lean-lang.org/papers/lean4.pdf
[21]: https://arxiv.org/pdf/2208.03803
[22]: https://openai.com
[23]: https://arxiv.org/pdf/2211.13139
[24]: https://arxiv.org/pdf/2211.11504
[25]: https://github.com/kashiwabarakenji/frankl_lean
