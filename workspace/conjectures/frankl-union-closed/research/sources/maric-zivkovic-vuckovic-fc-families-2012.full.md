<!-- source: https://ar5iv.labs.arxiv.org/html/1207.3604 | converted from HTML -->

[1207.3604] Formalizing Frankl’s Conjecture: FC-families

# Formalizing Frankl’s Conjecture: FC-families Thanks: The first author was partially supported by the Serbian Ministry of Education and Science grant 174021 and by the SNF grant SCOPES IZ73Z0127979/1, the second author by the Serbian Ministry of Education and Science grant 174021 and the third author by the Serbian Ministry of Education and Science grant 044006 (III). Affiliation: Faculty of Mathematics, University of Belgrade

Filip Marić Affiliation: Faculty of Mathematics, University of Belgrade Miodrag Živković Bojan Vučković

###### Abstract

The Frankl’s conjecture, formulated in 1979. and still open, states that in every family of sets closed for unions there is an element contained in at least half of the sets. FC-families are families for which it is proved that every union-closed family containing them satisfies the Frankl’s condition (e.g., in every union-closed family that contains a one-element set a, the element a is contained in at least half of the sets, so families of the form a are the simplest FC-families). FC-families play an important role in attacking the Frankl’s conjecture, since they enable significant search space pruning. We present a formalization of the computer assisted approach for proving that a family is an FC-family. Proof-by-computation paradigm is used and the proof assistant Isabelle/HOL is used both to check mathematical content, and to perform (verified) combinatorial searches on which the proofs rely. FC-families known in the literature are confirmed, and a new FC-family is discovered.

## 1 Introduction

Formalized mathematics and interactive theorem provers (sometimes referred to as proof assistants) have made great progress in recent years. Many classical mathematical theorems have been formally proved and proof assistants have been intensively used in hardware and software verification. The most successful proof assistants now days are Coq, Isabelle/HOL, HOL Light, etc.

Several of the most important results in formal theorem proving are for the problems that require proofs with much computational content. These proofs are usually highly complex (and therefore often require justifications by formal means) since they combine classical mathematical statements with complex computing machinery (usually computer implementation of combinatorial algorithms). The corresponding paradigm is sometimes referred to as *proof-by-evaluation*or *proof-by-computation*. Probably, the most famous examples of this approach are the proofs of the Four-Color Theorem and the Kepler’s conjecture.

Georges Gonthier has formalized a proof of the Four-Color Theorem 1 1 1 In 1852. Francis Guthrie conjectured that every map can be colored with at most 4 colors such that no two adjacent regions share the same color. in Coq [6]. The Four Colour Theorem is famous for being the first long-standing mathematical problem, analyzed by many famous mathematicians, finally resolved by a computer program (Appel and Haken [2]). This proof broke new ground because it involved using IBM 370 assembly language computer programs to carry out a gigantic case analysis, which could not be performed by hand. The proof attracted criticism: computer programming is known to be error-prone, and difficult to relate precisely to the formal statement of a mathematical theorem. Several attempts to simplify the proofs were made (e.g., Robertson et al. [13]), number of cases was reduced and programs were written in C instead of assembly language. However, all doubts were removed only when Gonthier employed proof assistant Coq reducing the whole proof to several basic logical principles.

Another example of a similar kind is the proof of Kepler’s conjecture 2 2 2 In 1611 Kepler asserted that the so called cannonball packing is a densest arrangement of 3-dimensional balls of the same size.. As described by Nipkow et al. [9]: “In 1998. Thomas Hales announced the first (by now) accepted proof of Kepler’s conjecture. It involves 3 distinct large computations. After 4 years of refereeing by a team of 12 referees, the referees declared that they were 99% certain of the correctness of the proof. Dissatisfied with this, Hales started the informal open-to-all collaborative *flyspeck*project to formalize the whole proof with a theorem proof.”

In this work, we apply the proof-by-evaluation paradigm to a problem of verifying FC-families --- a special case of the Frankl’s conjecture. Frankl’s conjecture, an elementary and fundamental statement formulated by Péter Frankl in 1979., states that for every family of sets closed under unions, there is an element contained in at least half of the sets (or, dually, in every family of sets closed under intersections, there is an element contained in at most half of the sets). Up to the best of our knowledge, the problem is still open. The conjecture has been proved for many special cases. In particular, it is known to be true for: (i) families of at most 36 sets 3 3 3 Unpublished report by Roberts from 1992 claimis a similar result for families of at most 40 sets. [4]; (ii) families of sets such that their union has at most 11 elements [3].

FC-families are families for which it is proved that all union closed families containing them satisfy the Frankl’s condition (if the Frankl’s conjecture would be proved, then every family would be an FC-family). For example, it can easily be shown that if a family contains a one-element set, then it satisfies the Frankl’s condition. Similar results holds for any two-element set, etc. FC-families are important building block for attempting to prove the Frankl’s conjecture since they justify pruning large portions of the search space.

#### Related work.

The Frankl’s conjecture has also been formulated and studied as a question in lattice theory [12, 1].

FC-families have been introduced by Poonen [11] and further studied by Gao and Yu [5], Vaughan [14, 15, 16], Morris [8], Marković [7], Bošnjak and Marković [3], and Živković and Vučković [17].

The basic technique used (the Frankl’s condition characterization based on weight functions and shares) is introduced by Poonen [11] and later successfully used by Bošnjak and Marković [7, 3], and Živković and Vučković [17].

First attempts in using computer-assisted computational approach on solving special cases of the Frankl’s conjecture are described by Živković and Vučković [17]. Computations are performed by (unverified) Java programs. However, in order to increase the level of trust, Java programs generate certificates that can be checked by independent tools.

The present paper represent a formalized reformulation of the results of Živković and Vučković [17]. All mathematical content is rigorously formalized within Isabelle/HOL and proofs are mechanically checked. JAVA programs are reimplemented in a functional language of Isabelle/HOL and their correctness is formally verified. A clear separation of mathematical and computational content is done and parts of the proofs that rely on computations are clearly isolated. Since the whole formalization is performed and verified within a proof assistant, there is no need for explicit certificates for statements proved by computation.

Our main contribution are rigorous, machine-verifiable proofs 4 4 4 Corresponding Isabelle/HOL proof documents are available from http://argo.matf.bg.ac.rs that all FC-families previously described in the literature are indeed FC-families. Unlike most pen-and-paper proofs, our proofs follow a uniform approach, supported by an underlying combinatorial search procedure. The second contribution is a new type of FC-families: four three-element sets all contained in a seven-element set.

#### Background logic and notation.

Logic and the notation given in this paper will follow Isabelle/HOL. Isabelle/HOL [10] is a development of Higher Order Logic (HOL), and it conforms largely to everyday mathematical notation. The basic types include truth values ( 𝑏𝑜𝑜𝑙 \mathit{bool}), natural numbers ( 𝑛𝑎𝑡 \mathit{nat}) and integers ( 𝑖𝑛𝑡 \mathit{int}). Functions can be defined by recursion (either primitive or general). Sets over type α \alpha, type α ​ 𝑠𝑒𝑡 \alpha\,\mathit{set}, follow the usual mathematical conventions 5 5 5 In a strict type setting, sets containing elements of mixed types are not allowed.. Sets of sets (i.e., object of the type α ​ 𝑠𝑒𝑡 ​ 𝑠𝑒𝑡 \alpha\,\mathit{set}\,\mathit{set}) are called families. Set of all subset for a set A A is denoted by 𝗉𝗈𝗐 ​ A {\sf pow}\ A, and its number of elements is denoted by | A | |A|. Lists over type α \alpha, type α ​ 𝑙𝑖𝑠𝑡 \alpha\,\mathit{list}, come with the empty list [] [\,], the infix prepend constructor #\#, the infix @ @ that appends two lists, and the conversion function 𝑠𝑒𝑡 \mathit{set} from lists to sets. N-th element of a list l l is denoted by l [n] l_{[n]}. List [0, 1, …, n − 1] [0,1,\ldots,n-1] is denoted by [0.. < n] [0..<n]. The function 𝗌𝗈𝗋𝗍 {\sf sort} sorts a list, 𝗅𝗂𝗌𝗍𝗌𝗎𝗆 {\sf listsum} calculates its sum, and 𝗋𝖾𝗆𝖽𝗎𝗉𝗌 {\sf remdups} removes duplicate elements. List with no repeated elements are called distinct. Standard higher order functions 𝗆𝖺𝗉 {\sf map}, 𝖿𝗂𝗅𝗍𝖾𝗋 {\sf filter}, 𝖿𝗈𝗅𝖽𝗅 {\sf foldl} are also supported (for details see [10]).

All definitions and statements given in this paper are formalized within Isabelle/HOL. However, in order to make the text accessible to a more general audience not familiar with Isabelle/HOL, many minor details are omitted and some imprecisions are introduced (for example, we used standard symbolics used in related work, although it is clear that some symbols are ambigous). Statements are grouped into propositions, lemmas, and theorems. Propositions usually express simple, technical results and are printed here without proofs. All sets and families are considered to be finite and this assumptions (present in Isabelle/HOL formalization) will not be explicitly stated in the rest of the paper.

#### Outline.

The rest of the paper is organized as follows. In Section 2 we give mathematical background on union-closed families, the Frankl’s conjecture and prove main theoretical results. In Section 3 we formulate the combinatorial search algorithm, prove its correctness and give its efficient implementation. In Section 4 we introduce uniform families and techniques used for avoiding symmetries when analyzing them. In Section 5 we verify several kinds of uniform FC-families. Finally, in Section 6 we draw conclusions and give directions for further work.

## 2 Frankl’s Families

### 2.1 Union Closed Families

First we give basic definitions of union-closed families, closure under unions, and operations used to incrementally obtain closed families.

###### Definition 1

Let F F and F c F_{c} be families.

F F is *union closed*, denoted by 𝗎𝖼 ​ F {\sf uc}\ F, iff ∀ A ∈ F. ∀ B ∈ F. A ∪ B ∈ F. \forall A\in F.\ \forall B\in F.\ A\cup B\in F. F F is *union closed for F c F_{c}*, denoted by 𝗎𝖼 F c ​ F {\sf uc}_{F_{c}}\ F, iff 𝗎𝖼 F ∧ ( ∀ A ∈ F. ∀ B ∈ F c. A ∪ B ∈ F). {\sf uc}\ F\wedge(\forall A\in F.\ \forall B\in F_{c}.\ A\cup B\in F).

*Closure of F F*, denoted by ⟨ F ⟩ \left\langle F\right\rangle, is the minimal family of sets (in sense of inclusion) that contains F F and is union closed. *Closure of F F for F c F_{c}*, denoted by ⟨ F ⟩ F c \left\langle F\right\rangle_{F_{c}}, is the minimal family of sets (in sense of inclusion) that contains F F and is union closed for F c F_{c}.

*Insert and close operation*of set A A to family F F, denoted by 𝗂𝖼 ​ A ​ F {\sf ic}\ A\ F, is the family F ∪ { A } ∪ { A ∪ B. B ∈ F }. F\cup\ \{A\}\ \cup\ \{A\cup B.\ B\in F\}.*Insert and close operation for F c F_{c}*of set A A to family F F, denoted by 𝗂𝖼 F c ​ A ​ F {\sf ic}_{F_{c}}\ A\ F, is the family F ∪ { A } ∪ { A ∪ B. B ∈ F } ∪ { A ∪ B. B ∈ F c }. F\cup\ \{A\}\ \cup\ \{A\cup B.\ B\in F\}\ \cup\ \{A\cup B.\ B\in F_{c}\}.

###### Proposition 1

1. 1.

⟨ F ⟩ = { ⋃ F ′. F ′ ∈ 𝗉𝗈𝗐 F − { ∅ } } \left\langle F\right\rangle=\{\bigcup F^{\prime}.\ F^{\prime}\in{\sf pow}\ F-\{\emptyset\}\}

2. 2.

⟨ F ∪ { A } ⟩ = 𝗂𝖼 ​ A ​ ⟨ F ⟩ \left\langle F\cup\{A\}\right\rangle={\sf ic}\ A\ \left\langle F\right\rangle, ⟨ F ∪ { A } ⟩ I = 𝗂𝖼 I ​ A ​ ⟨ F ⟩ \left\langle F\cup\{A\}\right\rangle_{I}={\sf ic}_{I}\ A\ \left\langle F\right\rangle

3. 3.

If F ⊆ 𝗉𝗈𝗐 ​ ⋃ A F\subseteq{\sf pow}\ \bigcup A and 𝗎𝖼 A ​ F {\sf uc}_{A}\ F then 𝗎𝖼 ⟨ A ⟩ ​ F {\sf uc}_{\left\langle A\right\rangle}\ F.

### 2.2 The Frankl’s Condition

The next definition formalizes the Frankl’s condition and the notion of FC-family.

###### Definition 2

Family of sets F F satisfies the *Frankl’s condition*and we say that it is a *Frankl’s family*, denoted by 𝖿𝗋𝖺𝗇𝗄𝗅 ​ F {\sf frankl}\ F, if it contains an element that occurs in at least half sets in the family, i.e., 𝖿𝗋𝖺𝗇𝗄𝗅 ​ F ≡ ∃ a. a ∈ ⋃ F ∧ 2 ⋅ #a ​ F ≥ | F | {\sf frankl}\ F\ \equiv\ \exists a.\ a\in\bigcup F\ \wedge\ 2\cdot\#_{a}F\geq|F|, where #a ​ F \#_{a}F denotes | { A ∈ F. a ∈ A } | |\{A\in F.\ a\in A\}|

Family of sets F c F_{c} is *FC-family*if it is proved that every union closed family such that F ⊇ F c F\supseteq F_{c} is Frankl’s.

### 2.3 Family Isomorphisms

The domain of the family does not play any important role for many properties related to the Frankl’s condition — many properties are invariant for domain changes using injective functions (that establish a kind of isomorphisms between two families). Therefore, in many cases it suffices to consider only families over canonical domains — initial ranges { 0, 1, …, n − 1 } \{0,1,\ldots,n-1\} of natural numbers.

###### Proposition 2

Let F F be a family of sets and f f a function injective on ⋃ F \bigcup{F}. Let F ′ F^{\prime} be the image of F F under f f (then f f is a bijection between ⋃ F \bigcup{F} and ⋃ F ′ \bigcup{F^{\prime}}).

1. 1.

If a ∈ ⋃ F a\in\bigcup{F}, then #a ​ F = #f ⁡ ( a) ​ F ′ \#_{a}F=\#_{f(a)}F^{\prime}.

2. 2.

| F | = | F ′ | |F|=|F^{\prime}|

3. 3.

If A ∈ F A\in F and A ′ ∈ F ′ A^{\prime}\in F^{\prime} is the image of A A under f f, then | A | = | A ′ | |A|=|A^{\prime}|.

4. 4.

F F is union closed if and only if F ′ F^{\prime} is.

5. 5.

F F is Frankl’s if and only if F ′ F^{\prime} is.

6. 6.

If F ′ F^{\prime} is an FC-family, then so is F F.

### 2.4 FC Characterization by Weight Functions and Shares

We describe the central technique for proving that a family is FC-family, relying on characterizations of the Frankl’s condition using weights and shares.

###### Definition 3

A function w: X → ℕ w:X\rightarrow\mathbb{N} is a *weight function on*A ⊆ X A\subseteq X, denoted by 𝗐𝖿 A ​ w {\sf wf}_{A}\ w, iff ∃ a ∈ A. w ⁡ ( a) > 0 \exists a\in A.\ w(a)>0. *Weight of a set A A wrt. weight function w w*, denoted by w ⁡ ( A) w(A), is the value ∑ a ∈ A w ⁡ ( a) \sum_{a\in A}w(a). *Weight of a family F F wrt. weight function w w*, denoted by w ⁡ ( F) w(F), is the value ∑ A ∈ F w ⁡ ( A) \sum_{A\in F}w(A).

###### Lemma 1

𝖿𝗋𝖺𝗇𝗄𝗅 ​ F ⇔ ∃ w. 𝗐𝖿 ( ⋃ F) ​ w ∧ 2 ⋅ w ⁡ ( F) ≥ w ⁡ ( ⋃ F) ⋅ | F | {\sf frankl}\ F\iff\exists w.\ {\sf wf}_{(\bigcup F)}\ w\ \wedge\ 2\cdot w(F)\;\geq\;w(\bigcup{F})\cdot|F|

###### Proof

Assume 𝖿𝗋𝖺𝗇𝗄𝗅 ​ F {\sf frankl}\ F and let a a be the element satisfying the Frankl’s condition. Let w w be the weight function assigning 1 to a a and 0 to all other elements. Since w ⁡ ( F) = #a ​ F w(F)=\#_{a}F and w ⁡ ( ⋃ F) = 1 w(\bigcup{F})=1, the statements holds.

Conversely, suppose that ¬ 𝖿𝗋𝖺𝗇𝗄𝗅 ​ F \neg{\sf frankl}\ F. Then, for every a ∈ ⋃ F a\in\bigcup{F}, 2 ⋅ #a ​ F < | F | 2\cdot\#_{a}F<|F|. Hence, 2 ⋅ w ⁡ ( F) = ∑ a ∈ ⋃ F w ⁡ ( a) ⋅ 2 ⋅ #a ​ F 2\cdot w(F)=\sum_{a\in\bigcup{F}}w(a)\cdot 2\cdot\#_{a}F < < | F | ⋅ ∑ a ∈ ⋃ F w ⁡ ( a) |F|\cdot\sum_{a\in\bigcup{F}}w(a) = = | F | ⋅ w ⁡ ( ⋃ F) |F|\cdot w(\bigcup{F}).

A concept that will enable a slightly more operative formulation of the previous characterization is the concept of *share*6 6 6 Note that in order to accommodate for computer implementation only integer weights are allowed, and to avoid rational numbers share of a set A A is defined as 2 ⋅ w ⁡ ( A) − w ⁡ ( X) 2\cdot w(A)-w(X), instead of w ⁡ ( A) − w ⁡ ( X) / 2 w(A)-w(X)/2 that is used in the literature..

###### Definition 4

Let w w be a weight function. *Share of a set A A wrt. w w and a set X X*, denoted by w ¯ X ​ ( A) \bar{w}_{X}(A), is the value 2 ⋅ w ⁡ ( A) − w ⁡ ( X) 2\cdot w(A)-w(X). *Share of a family F F wrt. w w and a set X X*, denoted by w ¯ X ​ ( F) \bar{w}_{X}(F), is the value ∑ A ∈ F w ¯ X ​ ( A) \sum_{A\in F}\bar{w}_{X}(A).

###### Example 1

Let w w be a function such that w ⁡ ( a 0) = 1, w ⁡ ( a 1) = 2 w(a_{0})=1,w(a_{1})=2, and w ⁡ ( a) = 0 w(a)=0 for all other elements. w w is clearly a weight function. Then, w ⁡ ( { a 0, a 1, a 2 }) = 3 w(\{a_{0},a_{1},a_{2}\})=3 and w ⁡ ( { { a 0, a 1 }, { a 1, a 2 }, { a 1 } }) = 7 w(\{\{a_{0},a_{1}\},\{a_{1},a_{2}\},\{a_{1}\}\})=7. Also, w ¯ { a 0, a 1, a 2 } ​ ( { a 1, a 2 }) = 2 ⋅ w ⁡ ( { a 1, a 2 }) − w ⁡ ( { a 0, a 1, a 2 }) = 4 − 3 = 1, \bar{w}_{\{a_{0},a_{1},a_{2}\}}(\{a_{1},a_{2}\})=2\cdot w(\{a_{1},a_{2}\})-w(\{a_{0},a_{1},a_{2}\})=4-3=1, and w ¯ { a 0, a 1, a 2 } ​ ( { { a 0, a 1 }, { a 1, a 2 }, { a 1 } }) = ( 2 ⋅ 3 − 3) + ( 2 ⋅ 2 − 3) + ( 2 ⋅ 2 − 3) = 5. \bar{w}_{\{a_{0},a_{1},a_{2}\}}(\{\{a_{0},a_{1}\},\{a_{1},a_{2}\},\{a_{1}\}\})=(2\cdot 3-3)+(2\cdot 2-3)+(2\cdot 2-3)=5.

###### Proposition 3

w ¯ X ​ ( F) = 2 ⋅ w ⁡ ( F) − w ⁡ ( X) ⋅ | F | \bar{w}_{X}(F)=2\cdot w(F)-w(X)\cdot|F|

###### Lemma 2

𝖿𝗋𝖺𝗇𝗄𝗅 ​ F ⇔ ∃ w. 𝗐𝖿 ( ⋃ F) ​ w ∧ w ¯ ( ⋃ F) ​ ( F) ≥ 0 {\sf frankl}\ F\iff\exists w.\ {\sf wf}_{(\bigcup{F})}\ w\ \wedge\ \bar{w}_{(\bigcup{F})}(F)\geq 0

###### Proof

Follows directly from Proposition 3 and Lemma 1.

#### Hypercubes.

Sets of a family can be grouped into so called hypercubes.

###### Definition 5

An S S -*hypercube*with a base K K, denoted by 𝗁𝖼 K S {\sf hc}_{K}^{S}, is the family { A. K ⊆ A ∧ A ⊆ K ∪ S } \{A.\ K\subseteq A\wedge A\subseteq K\cup S\}. Alternatively, a hypercube can be characterized by 𝗁𝖼 K S = { K ∪ A. A ∈ 𝗉𝗈𝗐 S } {\sf hc}_{K}^{S}=\{K\cup A.\ A\in{\sf pow}\ S\}.

###### Example 2

Let S ≡ { s 0, s 1 } S\equiv\{s_{0},s_{1}\}, and K ≡ { k 0, k 1 } K\equiv\{k_{0},k_{1}\}. If K ′ ⊆ K K^{\prime}\subseteq K, then all S S -hypercubes with a base K ′ K^{\prime} are:

 | 𝗁𝖼 { } S \displaystyle{\sf hc}_{\{\}}^{S} | = \displaystyle= | { { }, { s 0 }, { s 1 }, { s 0, s 1 } } \displaystyle\{\{\},\{s_{0}\},\{s_{1}\},\{s_{0},s_{1}\}\} |  |

 | 𝗁𝖼 { k 0 } S \displaystyle{\sf hc}_{\{k_{0}\}}^{S} | = \displaystyle= | { { k 0 }, { k 0, s 0 }, { k 0, s 1 }, { k 0, s 0, s 1 } } \displaystyle\{\{k_{0}\},\{k_{0},s_{0}\},\{k_{0},s_{1}\},\{k_{0},s_{0},s_{1}\}\} |  |

 | 𝗁𝖼 { k 1 } S \displaystyle{\sf hc}_{\{k_{1}\}}^{S} | = \displaystyle= | { { k 1 }, { k 1, s 0 }, { k 1, s 1 }, { k 1, s 0, s 1 } } \displaystyle\{\{k_{1}\},\{k_{1},s_{0}\},\{k_{1},s_{1}\},\{k_{1},s_{0},s_{1}\}\} |  |

 | 𝗁𝖼 { k 0, k 1 } S \displaystyle{\sf hc}_{\{k_{0},k_{1}\}}^{S} | = \displaystyle= | { { k 0, k 1 }, { k 0, k 1, s 0 }, { k 0, k 1, s 1 }, { k 0, k 1, s 0, s 1 } } \displaystyle\{\{k_{0},k_{1}\},\{k_{0},k_{1},s_{0}\},\{k_{0},k_{1},s_{1}\},\{k_{0},k_{1},s_{0},s_{1}\}\} |  |

Previous example indicates that (disjoint) S S -hypercubes can span the whole 𝗉𝗈𝗐 ⁡ ( K ∪ S) {\sf pow}\ (K\cup S). Indeed, this is generally the case.

###### Proposition 4

(i) 𝗉𝗈𝗐 ⁡ ( K ∪ S) = ⋃ K ′ ⊆ K 𝗁𝖼 K ′ S {\sf pow}\ (K\cup S)=\bigcup_{K^{\prime}\subseteq K}{\sf hc}_{K^{\prime}}^{S}. (ii) If K 1 K_{1} and K 2 K_{2} are different and disjoint with S S, then 𝗁𝖼 K 1 S {\sf hc}_{K_{1}}^{S} and 𝗁𝖼 K 2 S {\sf hc}_{K_{2}}^{S} are disjoint.

Families of sets can be separated into (disjoint) parts belonging to different hypercubes (formed as 𝗁𝖼 K S ∩ F {\sf hc}_{K}^{S}\cap F).

###### Definition 6

A *hyper-share of a family F F wrt. weight function w w, the hypercube 𝗁𝖼 K S {\sf hc}_{K}^{S} and the set X X*, denoted by w ¯ K ​ X S ​ ( F) \bar{w}^{S}_{KX}(F), is the value ∑ A ∈ 𝗁𝖼 K S ∩ F w ¯ X ​ ( A) \sum_{A\in{\sf hc}_{K}^{S}\cap F}\bar{w}_{X}(A).

###### Example 3

Let S S and K K be as in the Example 2, let X ≡ K ∪ S X\equiv K\cup S, let F ≡ { { s 0 }, { s 1 }, { k 0, s 0 }, { k 0, k 1, s 0, s 1 } } F\equiv\{\{s_{0}\},\{s_{1}\},\{k_{0},s_{0}\},\{k_{0},k_{1},s_{0},s_{1}\}\}, and w ⁡ ( a) = 1 w(a)=1 for all a ∈ X a\in X. Then, w ¯ { } ​ X S ​ ( F) = w ¯ X ​ ( { s 0 }) + w ¯ X ​ ( { s 1 }) = − 4 \bar{w}^{S}_{\{\}X}(F)=\bar{w}_{X}(\{s_{0}\})+\bar{w}_{X}(\{s_{1}\})=-4, w ¯ { k 0 } ​ X S ​ ( F) = w ¯ X ​ ( { k 0, s 0 }) = 0 \bar{w}^{S}_{\{k_{0}\}X}(F)=\bar{w}_{X}(\{k_{0},s_{0}\})=0, w ¯ { k 1 } ​ X S ​ ( F) = 0 \bar{w}^{S}_{\{k_{1}\}X}(F)=0, and w ¯ { k 0, k 1 } ​ X S ​ ( F) \bar{w}^{S}_{\{k_{0},k_{1}\}X}(F) = = w ¯ X ​ ( { k 0, k 1, s 0, s 1 }) = 4 \bar{w}_{X}(\{k_{0},k_{1},s_{0},s_{1}\})=4.

Share of a family can be expressed in terms of sum of hyper-shares.

###### Proposition 5

If K ∪ S = ⋃ F K\cup S=\bigcup{F} and K ∩ S = ∅ K\cap S=\emptyset, then w ¯ ( ⋃ F) ​ ( F) = ∑ K ′ ⊆ K w ¯ K ′ ​ ( ⋃ F) S ​ ( F) \bar{w}_{(\bigcup{F})}(F)=\sum_{K^{\prime}\subseteq K}\bar{w}^{S}_{K^{\prime}(\bigcup{F})}(F).

###### Lemma 3

Let w w be a weight function on ⋃ F \bigcup{F}. If K ∪ S = ⋃ F K\cup S=\bigcup{F}, K ∩ S = ∅ K\cap S=\emptyset, and ∀ K ′ ⊆ K. w ¯ K ′ ​ ( ⋃ F) S ​ ( F) ≥ 0 \forall K^{\prime}\subseteq K.\ \bar{w}^{S}_{K^{\prime}(\bigcup{F})}(F)\geq 0, then 𝖿𝗋𝖺𝗇𝗄𝗅 ​ F {\sf frankl}\ F.

###### Proof

Immediate consequence of Proposition 5 and Lemma 2.

###### Definition 7

*Projection of a family F F onto a hypercube 𝗁𝖼 K S {\sf hc}_{K}^{S}*, denoted by 𝗁𝖼 K S ​ ⌊ F ⌋ {\sf hc}_{K}^{S}\left\lfloor{F}\right\rfloor, is the set { A − K. A ∈ 𝗁𝖼 K S ∩ F } \{A-K.\ A\in{\sf hc}_{K}^{S}\cap F\}.

###### Example 4

Let K K, S S and F F be as in Example 3. Then 𝗁𝖼 { } S ​ ⌊ F ⌋ = { { s 0 }, { s 1 } } {\sf hc}_{\{\}}^{S}\left\lfloor{F}\right\rfloor=\{\{s_{0}\},\{s_{1}\}\}, 𝗁𝖼 { k 0 } S ​ ⌊ F ⌋ = { { s 0 } } {\sf hc}_{\{k_{0}\}}^{S}\left\lfloor{F}\right\rfloor=\{\{s_{0}\}\}, 𝗁𝖼 { k 1 } S ​ ⌊ F ⌋ = { } {\sf hc}_{\{k_{1}\}}^{S}\left\lfloor{F}\right\rfloor=\{\}, and 𝗁𝖼 { k 0, k 1 } S ​ ⌊ F ⌋ = { { s 0, s 1 } } {\sf hc}_{\{k_{0},k_{1}\}}^{S}\left\lfloor{F}\right\rfloor=\{\{s_{0},s_{1}\}\}.

###### Proposition 6

1. 1.

If K ∩ S = ∅ K\cap S=\emptyset and K ′ ⊆ K K^{\prime}\subseteq K, then 𝗁𝖼 K ′ S ​ ⌊ F ⌋ ⊆ 𝗉𝗈𝗐 ​ S {\sf hc}_{K^{\prime}}^{S}\left\lfloor{F}\right\rfloor\subseteq{\sf pow}\ S

2. 2.

If 𝗎𝖼 ​ F {\sf uc}\ F, then 𝗎𝖼 ⁡ ( 𝗁𝖼 K S ​ ⌊ F ⌋) {\sf uc}\ ({\sf hc}_{K}^{S}\left\lfloor{F}\right\rfloor).

3. 3.

If 𝗎𝖼 ​ F {\sf uc}\ F, F c ⊆ F F_{c}\subseteq F, S = ⋃ F c S=\bigcup F_{c}, K ∩ S = ∅ K\cap S=\emptyset, then 𝗎𝖼 F c ​ ( 𝗁𝖼 K S ​ ⌊ F ⌋) {\sf uc}_{F_{c}}\ ({\sf hc}_{K}^{S}\left\lfloor{F}\right\rfloor).

4. 4.

If ∀ x ∈ K. w ⁡ ( x) = 0 \forall x\in K.\ w(x)=0, then w ¯ K ​ X S ​ ( F) = w ¯ X ​ ( 𝗁𝖼 K S ​ ⌊ F ⌋) \bar{w}^{S}_{KX}(F)=\bar{w}_{X}({\sf hc}_{K}^{S}\left\lfloor{F}\right\rfloor).

#### Union closed extensions.

The next definition introduces an important notion for checking FC-families.

###### Definition 8

*Union closed extensions*of a family F c F_{c} are families that are created from elements of F c F_{c} and are union closed for F c F_{c}. Family of all union closed extensions is denoted by 𝗎𝖼𝖾 ​ F c {\sf uce}\ F_{c}, and 𝗎𝖼𝖾 F c ≡ { F ′. F ′ ⊆ 𝗉𝗈𝗐 ⋃ F c ∧ 𝗎𝖼 F c F ′ } {\sf uce}\ F_{c}\equiv\{F^{\prime}.\ F^{\prime}\subseteq{\sf pow}\ \bigcup{F_{c}}\wedge{\sf uc}_{F_{c}}\ F^{\prime}\}.

###### Lemma 4

Let F F be a non-empty union closed family, and let F c F_{c} be a subfamily (i.e., F c ⊆ F F_{c}\subseteq F). Let S S denote ⋃ F c \bigcup{F_{c}}, and let K K denote ⋃ F − ⋃ F c \bigcup{F}-\bigcup{F_{c}}. Let w w be a weight function on ⋃ F \bigcup{F}, that is zero for all elements of K K. If shares of all union closed extension of F c F_{c} are nonnegative, then F F is Frankl’s, i.e., if ∀ F ′ ∈ 𝗎𝖼𝖾 ​ F c. w ¯ ( ⋃ F c) ​ ( F ′) ≥ 0 \forall F^{\prime}\in{\sf uce}\ F_{c}.\ \bar{w}_{(\bigcup{F_{c}})}(F^{\prime})\geq 0, then 𝖿𝗋𝖺𝗇𝗄𝗅 ​ F {\sf frankl}\ F.

###### Proof

Since, K ∪ S = ⋃ F K\cup S=\bigcup F and K ∩ S = ∅ K\cap S=\emptyset, by Lemma 3, it suffices to show that ∀ K ′ ⊆ K. w ¯ K ′ ​ ( ⋃ F) S ​ ( F) ≥ 0 \forall K^{\prime}\subseteq K.\ \bar{w}^{S}_{K^{\prime}(\bigcup{F})}(F)\geq 0. Fix K ′ K^{\prime} and assume that K ′ ⊆ K K^{\prime}\subseteq K. Since w w is zero on K K, by Proposition 6, it holds that w ¯ K ′ ​ ( ⋃ F) S ​ ( F) = w ¯ ( ⋃ F) ​ ( 𝗁𝖼 K ′ S ​ ⌊ F ⌋) \bar{w}^{S}_{K^{\prime}(\bigcup{F})}(F)=\bar{w}_{(\bigcup{F})}({\sf hc}_{K^{\prime}}^{S}\left\lfloor{F}\right\rfloor). On the other hand, since 𝗎𝖼 ​ F {\sf uc}\ F, F c ⊆ F F_{c}\subseteq F, and K ∩ S = ∅ K\cap S=\emptyset, by Proposition 6 it holds that 𝗎𝖼 F c ​ ( 𝗁𝖼 K ′ S ​ ⌊ F ⌋) {\sf uc}_{F_{c}}\ ({\sf hc}_{K^{\prime}}^{S}\left\lfloor{F}\right\rfloor). Moreover, 𝗁𝖼 K ′ S ​ ⌊ F ⌋ ⊆ 𝗉𝗈𝗐 ​ S {\sf hc}_{K^{\prime}}^{S}\left\lfloor{F}\right\rfloor\subseteq{\sf pow}\ S, so 𝗁𝖼 K ′ S ​ ⌊ F ⌋ ∈ 𝗎𝖼𝖾 ​ F c {\sf hc}_{K^{\prime}}^{S}\left\lfloor{F}\right\rfloor\in{\sf uce}\ F_{c}. Then, w ¯ ( ⋃ F c) ​ ( 𝗁𝖼 K ′ S ​ ⌊ F ⌋) ≥ 0 \bar{w}_{(\bigcup{F_{c}})}({\sf hc}_{K^{\prime}}^{S}\left\lfloor{F}\right\rfloor)\geq 0 holds from the assumption. However, since w w is zero on K K, it holds that w ⁡ ( ⋃ F c) = w ⁡ ( ⋃ F) w(\bigcup{F_{c}})=w(\bigcup{F}) and w ¯ ( ⋃ F) ​ ( 𝗁𝖼 K ′ S ​ ⌊ F ⌋) = w ¯ ( ⋃ F c) ​ ( 𝗁𝖼 K ′ S ​ ⌊ F ⌋) ≥ 0 \bar{w}_{(\bigcup{F})}({\sf hc}_{K^{\prime}}^{S}\left\lfloor{F}\right\rfloor)=\bar{w}_{(\bigcup{F_{c}})}({\sf hc}_{K^{\prime}}^{S}\left\lfloor{F}\right\rfloor)\geq 0

###### Theorem 2.1

A family F c F_{c} is an FC-family if there is a weight function w w such that shares (wrt. w w and ⋃ F c \bigcup F_{c}) of all union closed extension of F c F_{c} are nonnegative.

###### Proof

Consider a union-closed family F ⊇ F c F\supseteq F_{c}. Let w w be the weight function such that ∀ F ′ ∈ 𝗎𝖼𝖾 ​ F c. w ¯ ( ⋃ F c) ​ ( F ′) ≥ 0 \forall F^{\prime}\in{\sf uce}\ F_{c}.\ \bar{w}_{(\bigcup{F_{c}})}(F^{\prime})\geq 0. Let w ′ w^{\prime} be a function equal to w w on ⋃ F c \bigcup F_{c} and 0 on other elements. Since ∀ F ′ ∈ 𝗎𝖼𝖾 ​ F c. w ′ ¯ ( ⋃ F c) ​ ( F ′) = w ¯ ( ⋃ F c) ​ ( F ′) \forall F^{\prime}\in{\sf uce}\ F_{c}.\ \bar{w^{\prime}}_{(\bigcup{F_{c}})}(F^{\prime})=\bar{w}_{(\bigcup{F_{c}})}(F^{\prime}), Lemma 4 applies to F F and F F is Frankl’s.

## 3 Combinatorial search

Theorem 2.1 inspires a procedure for verifying FC families. It should take a weight function on ⋃ F c \bigcup{F_{c}} and check that all union closed extensions of F c F_{c} have nonnegative shares. We will now define a procedure *SomeShareNegative*, denoted by 𝗌𝗌𝗇 ​ F c ​ w {\sf ssn}\ F_{c}\ w, such that if 𝗌𝗌𝗇 F c w = ⊥ {\sf ssn}\ F_{c}\ w=\bot, then for all F ′ ∈ 𝗎𝖼𝖾 ​ F c F^{\prime}\in{\sf uce}\ F_{c} it holds that w ¯ ( ⋃ F c) ​ ( F ′) ≥ 0 \bar{w}_{(\bigcup{F_{c}})}(F^{\prime})\geq 0. The heart of this procedure will be a recursive function 𝗌𝗌𝗇 F c, w, X ​ L ​ F t {\sf ssn}^{F_{c},w,X}\ L\ F_{t} that preforms a systematic traversal of all union closed extensions of F c F_{c}, but with pruning that speeds up the search. If a union closed extension of F c F_{c} has a negative share, it must contain one or more sets with a negative share. Therefore, a list L L of all different subsets of ⋃ F c \bigcup{F_{c}} with negative shares is formed and each candidate family is determined by elements of L L that it includes. A recursive procedure creates all candidate families by processing elements of L L sequentially, either skipping them (in one recursive branch) or including them into the current candidate family F t F_{t} (in the other recursive branch), maintaining the invariant that the current candidate family F t F_{t} is always union closed. If the current element of L L has been already included in F t F_{t} (by earlier closure operations required to maintain the invariant) the search can be pruned. If the sum of (negative) shares of the remaining elements of L L is less then the (nonnegative) share of the current F t F_{t}, then F t F_{t} cannot be extended to a family with a negative share (even in the extreme case when all the remaining elements of L L are included) so, again, the search can be pruned.

###### Definition 9

The function 𝗌𝗌𝗇 F c, w, X ​ L ​ F t {\sf ssn}^{F_{c},w,X}\ L\ F_{t} is defined by a primitive recursion (over the structure of the list L L):

 | 𝗌𝗌𝗇 F c, w, X ​ [] ​ F t \displaystyle{\sf ssn}^{F_{c},w,X}\ [\,]\ F_{t} | ≡ \displaystyle\equiv | w ¯ X ​ ( F t) < 0 \displaystyle\bar{w}_{X}(F_{t})<0 |  |

 | 𝗌𝗌𝗇 F c, w, X ​ ( h ​ #​ t) ​ F t \displaystyle{\sf ssn}^{F_{c},w,X}\ (h\;\#\;t)\ F_{t} | ≡ \displaystyle\equiv | if ​ w ¯ X ​ ( F t) + ∑ A ∈ h ​ #​ t w ¯ X ​ ( A) ≥ 0 ​ then ⊥ \displaystyle\mathrm{if\ }\bar{w}_{X}(F_{t})+\sum_{A\in h\;\#\;t}\bar{w}_{X}(A)\geq 0\mathrm{\ then\ }\bot |  |

 |  |  | else ​ if ​ 𝗌𝗌𝗇 F c, w, X ​ t ​ F t ​ then ⊤ \displaystyle\mathrm{else\ if\ }{\sf ssn}^{F_{c},w,X}\ t\ F_{t}\mathrm{\ then\ }\top |  |

 |  |  | else ​ if ​ h ∈ F t ​ then ⊥ \displaystyle\mathrm{else\ if\ }h\in F_{t}\mathrm{\ then\ }\bot |  |

 |  |  | else ​ 𝗌𝗌𝗇 F c, w, X ​ t ​ ( 𝗂𝖼 F c ​ h ​ F t) \displaystyle\mathrm{else\ }{\sf ssn}^{F_{c},w,X}\ t\ ({\sf ic}_{F_{c}}\ h\ F_{t}) |  |

Let L L be a distinct list such that its set is { A. A ∈ 𝗉𝗈𝗐 ⋃ F c ∧ w ¯ X ( A) < 0 } \{A.\ A\in{\sf pow}\ \bigcup{F_{c}}\wedge\bar{w}_{X}(A)<0\}.

 | 𝗌𝗌𝗇 ​ F c ​ w ≡ 𝗌𝗌𝗇 ⟨ F c ⟩, w, ( ⋃ F c) ​ L ​ ∅ {\sf ssn}\ F_{c}\ w\equiv{\sf ssn}^{\left\langle F_{c}\right\rangle,w,(\bigcup{F_{c}})}\ L\ \emptyset |  |

Next we prove the soundnes of the 𝗌𝗌𝗇 ​ F c ​ w {\sf ssn}\ F_{c}\ w function.

###### Lemma 5

If (i) 𝗌𝗌𝗇 F c, w, X L F t = ⊥ {\sf ssn}^{F_{c},w,X}\ L\ F_{t}=\bot, (ii) for all elements A A in L L it holds that w ¯ X ​ ( A) < 0 \bar{w}_{X}(A)<0, (iii) for all A ∈ F ′ − F t A\in F^{\prime}-F_{t}, if w ¯ X ​ ( A) < 0 \bar{w}_{X}(A)<0, then A A is in L L, (iv) F ′ ⊇ F t F^{\prime}\supseteq F_{t}, and (v) 𝗎𝖼 F c ​ F ′ {\sf uc}_{F_{c}}\ F^{\prime}, then w ¯ X ​ ( F ′) ≥ 0 \bar{w}_{X}(F^{\prime})\geq 0.

###### Proof

The proof is by induction. First, note that

 | w ¯ X ​ ( F ′) = ∑ A ∈ F ′ w ¯ X ​ ( A) = ∑ A ∈ F t w ¯ X ​ ( A) + ∑ A ∈ F ′ − F t w ¯ X ​ ( A). \bar{w}_{X}(F^{\prime})=\sum_{A\in F^{\prime}}\bar{w}_{X}(A)=\sum_{A\in F_{t}}\bar{w}_{X}(A)+\sum_{A\in F^{\prime}-F_{t}}\bar{w}_{X}(A). |  | (1) |

Consider the base case of L = [] L=[\,]. Since 𝗌𝗌𝗇 F c, w, X [] F t = ⊥ {\sf ssn}^{F_{c},w,X}\ [\,]\ F_{t}=\bot, it holds that ∑ A ∈ F t w ¯ X ​ ( A) = w ¯ X ​ ( F t) ≥ 0 \sum_{A\in F_{t}}\bar{w}_{X}(A)=\bar{w}_{X}(F_{t})\geq 0 and first term in ( 1) is nonnegative. If there were some A ∈ F ′ − F t A\in F^{\prime}-F_{t} such that w ¯ X ​ ( A) < 0 \bar{w}_{X}(A)<0, then, from the assumptions it would be in L L, which is impossible since L L is empty. Therefore, the second term in ( 1) is also nonnegative which completes the proof.

Consider the inductive step, and assume that L ≡ h ​ #​ t L\equiv h\;\#\;t.

First consider the case when w ¯ X ​ ( F t) + ∑ A ∈ h ​ #​ t w ¯ X ​ ( A) ≥ 0 \bar{w}_{X}(F_{t})+\sum_{A\in h\;\#\;t}\bar{w}_{X}(A)\geq 0. Let P P denote the set { A. A ∈ F ′ − F t ∧ w ¯ X ( A) ≥ 0 } \{A.\ A\in F^{\prime}-F_{t}\wedge\bar{w}_{X}(A)\geq 0\}, and let N N denote the set { A. A ∈ F ′ − F t ∧ w ¯ X ( A) < 0 } \{A.\ A\in F^{\prime}-F_{t}\wedge\bar{w}_{X}(A)<0\}. Since, by assumptions, all elements of N N are in L ≡ h ​ #​ t L\equiv h\;\#\;t, and since, by assumptions, all shares of h ​ #​ t − N h\;\#\;t-N are negative, it holds that

 | ∑ A ∈ h ​ #​ t w ¯ X ​ ( A) = ∑ A ∈ N w ¯ X ​ ( A) + ∑ A ∈ h ​ #​ t − N w ¯ X ​ ( A) ≤ ∑ A ∈ N w ¯ X ​ ( A). \sum_{A\in h\;\#\;t}\bar{w}_{X}(A)=\sum_{A\in N}\bar{w}_{X}(A)+\sum_{A\in h\;\#\;t-N}\bar{w}_{X}(A)\leq\sum_{A\in N}\bar{w}_{X}(A). |  | (2) |

It holds that ∑ A ∈ F ′ − F t w ¯ X ​ ( A) = ∑ A ∈ P w ¯ X ​ ( A) + ∑ A ∈ N w ¯ X ​ ( A). \sum_{A\in F^{\prime}-F_{t}}\bar{w}_{X}(A)=\sum_{A\in P}\bar{w}_{X}(A)+\sum_{A\in N}\bar{w}_{X}(A). Therefore, since all shares of P P are nonnegative, from ( 1) and ( 2) and the assumption of the current case it holds that

 | w ¯ X ​ ( F ′) ≥ ∑ A ∈ F t w ¯ X ​ ( A) + ∑ A ∈ N w ¯ X ​ ( A) ≥ w ¯ X ​ ( F t) + ∑ A ∈ h ​ #​ t w ¯ X ​ ( A) ≥ 0. \bar{w}_{X}(F^{\prime})\geq\sum_{A\in F_{t}}\bar{w}_{X}(A)+\sum_{A\in N}\bar{w}_{X}(A)\geq\bar{w}_{X}(F_{t})+\sum_{A\in h\;\#\;t}\bar{w}_{X}(A)\geq 0. |  |

Next, consider the case when w ¯ X ​ ( F t) + ∑ A ∈ h ​ #​ t w ¯ X ​ ( A) < 0 \bar{w}_{X}(F_{t})+\sum_{A\in h\;\#\;t}\bar{w}_{X}(A)<0. Since, by assumptions, 𝗌𝗌𝗇 F c, w, X ( h #t) F t = ⊥ {\sf ssn}^{F_{c},w,X}\ (h\;\#\;t)\ F_{t}=\bot, by the definition of 𝗌𝗌𝗇 {\sf ssn} it must hold that 𝗌𝗌𝗇 F c, w, X t F t = ⊥ {\sf ssn}^{F_{c},w,X}\ t\ F_{t}=\bot.

Consider the case when h ∈ F t h\in F_{t} or h ∉ F ′ h\notin F^{\prime}. Then h ∉ F ′ − F t h\notin F^{\prime}-F_{t}. The conclusion follows by induction hypothesis for the recursive call 𝗌𝗌𝗇 F c, w, X ​ t ​ F t {\sf ssn}^{F_{c},w,X}\ t\ F_{t}, since all assumptions are satisfied. Indeed, all elements of F ′ − F t F^{\prime}-F_{t} with negative shares must be in t t, since h ∉ F ′ − F t h\notin F^{\prime}-F_{t}, and other assumptions are trivially satisfied.

Finally, consider the case when h ∉ F t h\notin F_{t} and h ∈ F ′ h\in F^{\prime}. The conclusion follows by induction hypothesis for the recursive call 𝗌𝗌𝗇 F c, w, X ​ t ​ ( 𝗂𝖼 F c ​ h ​ F t) {\sf ssn}^{F_{c},w,X}\ t\ ({\sf ic}_{F_{c}}\ h\ F_{t}), since all assumptions are satisfied for this call. Indeed, in this case 𝗌𝗌𝗇 F c, w, X ​ ( h ​ #​ t) ​ F t = 𝗌𝗌𝗇 F c, w, X ​ t ​ ( 𝗂𝖼 F c ​ h ​ F t) {\sf ssn}^{F_{c},w,X}\ (h\;\#\;t)\ F_{t}={\sf ssn}^{F_{c},w,X}\ t\ ({\sf ic}_{F_{c}}\ h\ F_{t}) and the left hand side is ⊥ \bot from the current assumptions. All elements of F ′ − 𝗂𝖼 F c ​ h ​ F t F^{\prime}-{\sf ic}_{F_{c}}\ h\ F_{t} with negative shares must be in t t. Indeed, this holds since F t ⊆ 𝗂𝖼 F c ​ h ​ F t F_{t}\subseteq{\sf ic}_{F_{c}}\ h\ F_{t}, and h ∈ 𝗂𝖼 F c ​ h ​ F t h\in{\sf ic}_{F_{c}}\ h\ F_{t}, and since all elements of F ′ − F t F^{\prime}-F_{t} with negative shares are in h ​ #​ t h\;\#\;t. It holds that 𝗂𝖼 F c ​ h ​ F t ⊆ F ′ {\sf ic}_{F_{c}}\ h\ F_{t}\subseteq F^{\prime} since F t ⊆ F ′ F_{t}\subseteq F^{\prime}, h ∈ F ′ h\in F^{\prime} and 𝗎𝖼 F c ​ F ′ {\sf uc}_{F_{c}}\ F^{\prime}. Other assumptions trivially hold.

###### Theorem 3.1

If 𝗌𝗌𝗇 F c w = ⊥ {\sf ssn}\ F_{c}\ w=\bot and F ′ ∈ 𝗎𝖼𝖾 ​ F c F^{\prime}\in{\sf uce}\ F_{c} then w ¯ ( ⋃ F c) ​ ( F ′) ≥ 0 \bar{w}_{(\bigcup{F_{c}})}(F^{\prime})\geq 0.

###### Proof

Fix F ′ F^{\prime} from 𝗎𝖼𝖾 ​ F c {\sf uce}\ F_{c}. Then F ′ ⊆ 𝗉𝗈𝗐 ​ ⋃ F c F^{\prime}\subseteq{\sf pow}\ \bigcup{F_{c}} and 𝗎𝖼 F c ​ F ′ {\sf uc}_{F_{c}}\ F^{\prime}. Let L L be a distinct list such that its set is { A. A ∈ 𝗉𝗈𝗐 ⋃ F c ∧ w ¯ X ( A) < 0 } \{A.\ A\in{\sf pow}\ \bigcup{F_{c}}\wedge\bar{w}_{X}(A)<0\}. From 𝗌𝗌𝗇 F c w = ⊥ {\sf ssn}\ F_{c}\ w=\bot and the definition of 𝗌𝗌𝗇 {\sf ssn} it holds that 𝗌𝗌𝗇 ⟨ F c ⟩, w, ( ⋃ F c) L ∅ = ⊥ {\sf ssn}^{\left\langle F_{c}\right\rangle,w,(\bigcup{F_{c}})}\ L\ \emptyset=\bot. All assumptions of Lemma 5 apply. Indeed, for all A A in L L, w ¯ ( ⋃ F c) ​ ( A) < 0 \bar{w}_{(\bigcup{F_{c}})}(A)<0. For all A A in F ′ − ∅ F^{\prime}-\emptyset, if w ¯ ( ⋃ F c) ​ ( A) < 0 \bar{w}_{(\bigcup{F_{c}})}(A)<0, then, since F ′ ⊆ 𝗉𝗈𝗐 ​ ⋃ F c F^{\prime}\subseteq{\sf pow}\ \bigcup{F_{c}}, A A is in L L. ∅ ⊆ F ′ \emptyset\subseteq F^{\prime}. Since 𝗎𝖼 F c ​ F ′ {\sf uc}_{F_{c}}\ F^{\prime}, by Proposition 1, it holds that 𝗎𝖼 ⟨ F c ⟩ ​ F ′ {\sf uc}_{\left\langle F_{c}\right\rangle}\ F^{\prime}. Therefore, w ¯ ( ⋃ F c) ​ ( F ′) ≥ 0 \bar{w}_{(\bigcup{F_{c}})}(F^{\prime})\geq 0 holds.

Apart from being sound, the procedure can also be shown to be complete. Namely, it could be shown that if 𝗌𝗌𝗇 F c w = ⊤ {\sf ssn}\ F_{c}\ w=\top, then there is an F ′ ∈ 𝗎𝖼𝖾 ​ F c F^{\prime}\in{\sf uce}\ F_{c} such that w ¯ ( ⋃ F c) ​ ( F ′) < 0 \bar{w}_{(\bigcup{F_{c}})}(F^{\prime})<0. This comes from the invariant that the current family F t F_{t} in the search is always in 𝗎𝖼𝖾 ​ F c {\sf uce}\ F_{c}, which is maintained by taking the closure 𝗂𝖼 F c ​ h ​ F t {\sf ic}_{F_{c}}\ h\ F_{t} whenever an element h h is added. Since this aspect of the procedure is not relevant for the rest of the proofs, it will not be formally stated nor proved.

### 3.1 Efficient implementation

In order to obtain executability and increase efficiency, a series of refinements of 𝗌𝗌𝗇 ​ F ​ w {\sf ssn}\ F\ w is done. Each refined version introduces a new implementation feature that makes it more efficient than the previous one, but still equivalent with it.

First, a function cannot operate on families of sets. Without loss of generality, it suffices only to consider families of sets of natural numbers. Sets of natural numbers are represented by natural number codes. A set A A is represented by the code A ~ = ∑ k ∈ A 2 k \tilde{A}=\sum_{k\in A}2^{k}. Families of sets of natural numbers F F are represented by (distinct) lists of natural number codes F ~ \tilde{F}. This representation will be referred to as *list-of-nats*representation (e.g., F = { { 0, 1 }, { 1, 2 }, { 0, 1, 2 } } F=\{\{0,1\},\{1,2\},\{0,1,2\}\} is represented by the list-of-nats F ~ = [3, 6, 7] \tilde{F}=[3,6,7]). Basic set operations have their corresponding list-of-nat counterparts.

- •

The union of two sets ∪ \cup corresponds to bitwise disjunction (denoted by ⊔ \sqcup). It holds that if C = A ∪ B C=A\;\cup\;B, then C ~ = A ~ ⊔ B ~ \tilde{C}=\tilde{A}\;\sqcup\;\tilde{B}.

- •

Adding a set A A to a family of sets F F (i.e., A ∪ F A\;\cup\;F) corresponds to the operation (also denoted by ⊔ \sqcup) that prepends A ~ \tilde{A} to F ~ \tilde{F}, but only if it is not already present, i.e., by: if ​ A ~ ∈ F ~ ​ then ​ F ~ ​ else ​ A ~ ​ #​ F ~ \mathrm{if\ }\tilde{A}\in\tilde{F}\mathrm{\ then\ }\tilde{F}\mathrm{\ else\ }\tilde{A}\;\#\;\tilde{F}. It holds that if F ′ = A ∪ F F^{\prime}=A\cup F, then F ′ ~ = A ~ ⊔ F ~ \tilde{F^{\prime}}=\tilde{A}\sqcup\tilde{F}.

- •

Union of two families (i.e., F ′ ∪ F F^{\prime}\cup F), also denoted by ⊔ \sqcup, is performed by iteratively adding sets from one family to another, i.e., as 𝖿𝗈𝗅𝖽𝗅 ( λ A ~ F ~. A ~ ⊔ F ~) F ~ F ′ ~ {\sf foldl}\ (\lambda\ \tilde{A}\ \tilde{F}.\ \tilde{A}\sqcup\tilde{F})\ \tilde{F}\ \tilde{F^{\prime}}. It holds that if F ′′ = F ∪ F ′ F^{\prime\prime}=F\cup F^{\prime}, then F ′′ ~ = F ~ ⊔ F ′ ~ \tilde{F^{\prime\prime}}=\tilde{F}\sqcup\tilde{F^{\prime}}.

- •

Adding a set A A to all members of a family of sets F F (i.e., { A ∪ B. B ∈ F } \{A\cup B.\ B\in F\}), denoted by [A ~ ⊔ B ~. B ~ ∈ F ~] [\tilde{A}\;\sqcup\;\tilde{B}.\ \tilde{B}\in\tilde{F}], is performed by 𝗆𝖺𝗉 ( λ B ~. A ~ ⊔ B ~) F ~ {\sf map}\ (\lambda\ \tilde{B}.\ \tilde{A}\sqcup\tilde{B})\ \tilde{F}. It holds that if F ′ = { A ∪ B. B ∈ F } F^{\prime}=\{A\cup B.\ B\in F\}, then F ′ ~ = [A ~ ⊔ B ~. B ~ ∈ F ~] \tilde{F^{\prime}}=[\tilde{A}\;\sqcup\;\tilde{B}.\ \tilde{B}\in\tilde{F}].

- •

Insert and close for F F (i.e., 𝗂𝖼 F c ​ a ​ F {\sf ic}_{F_{c}}\ a\ F), denoted by 𝗂𝖼 ~ \tilde{{\sf ic}}, is computed as ( [A ~] @ [A ~ ⊔ B ~. B ~ ∈ F ~] @ [A ~ ⊔ B ~. B ~ ∈ F c ~]) ⊔ F ~ ([\tilde{A}]\ @\ [\tilde{A}\;\sqcup\;\tilde{B}.\ \tilde{B}\in\tilde{F}]\ @\ [\tilde{A}\;\sqcup\;\tilde{B}.\ \tilde{B}\in\tilde{F_{c}}])\ \sqcup\ \tilde{F}. It holds that if F ′ = 𝗂𝖼 F c ​ a ​ F F^{\prime}={\sf ic}_{F_{c}}\ a\ F, then F ′ ~ = 𝗂𝖼 ~ F c ~ ​ a ~ ​ F ~. \tilde{F^{\prime}}={\sf\tilde{ic}}_{\tilde{F_{c}}}\ \tilde{a}\ \tilde{F}.

Important optimization to the basic 𝗌𝗌𝗇 ​ F c ​ w {\sf ssn}\ F_{c}\ w procedure is to avoid repeated computations of family shares (both for the elements of the list L L and the current family F t F_{t}). So, instead of accepting a list of families of sets L L, and the current family of sets F t F_{t}, the function is modified to accept a list of ordered pairs where first component is a list-of-nats representation of corresponding element of L L, and the second component is its share (wrt. w w and X X), and to accept an ordered pair ( F t ~, s t) (\tilde{F_{t}},s_{t}) where F t ~ \tilde{F_{t}} is the list-of-nats representation of F t F_{t}, and s t s_{t} is its family share (wrt. w w and X X). The summation of shares of elements in L L is also unnecessarily repeated. It can be avoided if the sum ( s l s_{l}) is passed trough the function.

 | 𝗌𝗌𝗇 F c ~, w, X ​ ( [], 0) ​ ( F t ~, s t) \displaystyle{\sf ssn}^{\tilde{F_{c}},w,X}\ ([\,],0)\ (\tilde{F_{t}},s_{t}) | ≡ \displaystyle\equiv | s t < 0 \displaystyle s_{t}<0 |  |

 | 𝗌𝗌𝗇 F c ~, w, X ​ ( ( h ~, s h) ​ #​ t, s l) ​ ( F t ~, s t) \displaystyle{\sf ssn}^{\tilde{F_{c}},w,X}\ ((\tilde{h},s_{h})\;\#\;t,\;s_{l})\ (\tilde{F_{t}},\;s_{t}) | ≡ \displaystyle\equiv | if ​ s t + s l ≥ 0 ​ then ⊥ \displaystyle\mathrm{if\ }s_{t}+s_{l}\geq 0\mathrm{\ then\ }\bot |  |

 |  |  | else ​ if ​ 𝗌𝗌𝗇 F c ~, w, X ​ ( t, s l − s h) ​ ( F t ~, s t) ​ then ⊤ \displaystyle\mathrm{else\ if\ }{\sf ssn}^{\tilde{F_{c}},w,X}\ (t,\;s_{l}-s_{h})\ (\tilde{F_{t}},\;s_{t})\mathrm{\ then\ }\top |  |

 |  |  | else ​ if ​ h ~ ∈ F t ~ ​ then ⊥ \displaystyle\mathrm{else\ if\ }\tilde{h}\in\tilde{F_{t}}\mathrm{\ then\ }\bot |  |

 |  |  | else ​ let ​ F t ~ ′ = 𝗂𝖼 ~ F c ~ ​ h ~ ​ F t ~; s t ′ = w ¯ X ​ ( F t ~ ′) ​ in \displaystyle\mathrm{else\ let\ }\tilde{F_{t}}^{\prime}={\sf\tilde{ic}}_{\tilde{F_{c}}}\ \tilde{h}\ \tilde{F_{t}};\ s_{t}^{\prime}=\bar{w}_{X}(\tilde{F_{t}}^{\prime})\mathrm{\ in} |  |

 |  |  | 𝗌𝗌𝗇 F c ~, w, X ​ ( t, l ​ s − s h) ​ ( F t ~ ′, s t ′) \displaystyle\hskip 9.24994pt{\sf ssn}^{\tilde{F_{c}},w,X}\ (t,ls-s_{h})\ (\tilde{F_{t}}^{\prime},s_{t}^{\prime}\;) |  |

Another source of inefficiency is the calculation of w ¯ X ​ ( F t ~ ′) \bar{w}_{X}(\tilde{F_{t}}^{\prime}). If performed directly based on the definition of family share for F t ~ ′ \tilde{F_{t}}^{\prime}, the sum would contain shares of all elements from F t ~ \tilde{F_{t}} and of all elements that are added to F t ~ \tilde{F_{t}} when adding h ~ \tilde{h} and closing for F ~ \tilde{F}. However, it is already known that the sum of shares for elements of F t ~ \tilde{F_{t}} is s t s_{t} and the implementation could benefit from this fact. Also, calculating shares of sets that are added to F t ~ \tilde{F_{t}} can be made faster. Namely, it happens that set share of a same set is calculated over and over again in different parts of the search space. So, it is much better to precompute shares of all sets from 𝗉𝗈𝗐 ​ X {\sf pow}\ X and store them in a lookup table that will be consulted each time a set share is needed. Note that in this case there is no more need to pass the function w w itself, nor the domain X X, but only the lookup table, denoted by s w s_{w}.

 | 𝗌𝗌𝗇 F ~ c, s w ​ ( [], 0) ​ ( F t ~, s t) \displaystyle{\sf ssn}^{\tilde{F}_{c},s_{w}}\ ([\,],0)\ (\tilde{F_{t}},s_{t}) | ≡ \displaystyle\equiv | s t < 0 \displaystyle s_{t}<0 |  |

 | 𝗌𝗌𝗇 F ~ c, s w ​ ( ( h ~, s h) ​ #​ t, s l) ​ ( F t ~, s t) \displaystyle{\sf ssn}^{\tilde{F}_{c},s_{w}}\ ((\tilde{h},s_{h})\;\#\;t,\;s_{l})\ (\tilde{F_{t}},\;s_{t}) | ≡ \displaystyle\equiv | if ​ s t + s l ≥ 0 ​ then ⊥ \displaystyle\mathrm{if\ }s_{t}+s_{l}\geq 0\mathrm{\ then\ }\bot |  |

 |  |  | else ​ if ​ 𝗌𝗌𝗇 F ~ c, s w ​ ( t, s l − s h) ​ ( F t ~, s t) ​ then ⊤ \displaystyle\mathrm{else\ if\ }{\sf ssn}^{\tilde{F}_{c},s_{w}}\ (t,\;s_{l}-s_{h})\ (\tilde{F_{t}},\;s_{t})\mathrm{\ then\ }\top |  |

 |  |  | else ​ if ​ h ~ ∈ F t ~ ​ then ⊥ \displaystyle\mathrm{else\ if\ }\tilde{h}\in\tilde{F_{t}}\mathrm{\ then\ }\bot |  |

 |  |  | else ​ 𝗌𝗌𝗇 F ~ c, s w ​ ( t, s l − s h) ​ ( 𝗂𝖼 ~ F ~ c s w ​ h ~ ​ ( F t ~, s t)) \displaystyle\mathrm{else\ }{\sf ssn}^{\tilde{F}_{c},s_{w}}\ (t,s_{l}-s_{h})\ ({\sf\tilde{ic}}_{\tilde{F}_{c}}^{s_{w}}\ \tilde{h}\ (\tilde{F_{t}},s_{t})) |  |

 | 𝗂𝖼 ~ F ~ c s w ​ h ~ ​ ( F t ~, s t) \displaystyle{\sf\tilde{ic}}_{\tilde{F}_{c}}^{s_{w}}\ \tilde{h}\ (\tilde{F_{t}},s_{t}) | ≡ \displaystyle\equiv | let a d d = [h ~] @ [h ~ ⊔ A ~. A ~ ∈ F t ~] @ [h ~ ⊔ A ~. A ~ ∈ F ~ c]; \displaystyle\mathrm{let\ }\ add\ =\ [\tilde{h}]\ @\ [\tilde{h}\;\sqcup\;\tilde{A}.\ \tilde{A}\in\tilde{F_{t}}]\ @\ [\tilde{h}\;\sqcup\;\tilde{A}.\ \tilde{A}\in\tilde{F}_{c}]; |  |

 |  |  | a d d = 𝖿𝗂𝗅𝗍𝖾𝗋 ( λ A ~. A ~ ∉ F ~) ( 𝗋𝖾𝗆𝖽𝗎𝗉𝗌 a d d) in \displaystyle\hskip 18.49988ptadd\ =\ {\sf filter}\ (\lambda\tilde{A}.\ \tilde{A}\notin\tilde{F})\ ({\sf remdups}\ add)\ \textrm{in} |  |

 |  |  | ( a ​ d ​ d ​ @ ​ F ~, s + 𝗅𝗂𝗌𝗍𝗌𝗎𝗆 ⁡ ( 𝗆𝖺𝗉 ​ s w ​ a ​ d ​ d)) \displaystyle(add\;@\;\tilde{F},\ s+{\sf listsum}\ ({\sf map}\ s_{w}\ add)) |  |

It is shown that this implementation is (in some sense) equivalent to the starting, abstract one. This proof is technically involved, but conceptually uninteresting so we omit it in the text.

## 4 Uniform n ​ k ​ m nkm -families

Most FC-families that are considered in this paper are *uniform*, i.e., consist of sets having the same number of elements.

###### Definition 10

A family of sets F F is a *uniform n ​ k ​ m nkm -family*if it contains m m different sets, each containing k k elements and their union has at most n n elements. Uniform n ​ k ​ m nkm -family is *natural*if its union is contained in { 0, 1, …, n − 1 } \{0,1,\ldots,n-1\}.

Within the Isabelle/HOL implementation, natural n ​ k ​ m nkm -families will be represented by *n ​ k ​ m nkm -lists*— (lexicografically) sorted, distinct lists of length m m containing sorted, distinct lists of length k k with all elements contained in { 0, 1, …, n − 1 } \{0,1,\ldots,n-1\}. To simplify presentation, we will identify natural n ​ k ​ m nkm -families with their corresponding n ​ k ​ m nkm -lists. Assuming that the Isabelle/HOL function 𝖼𝗈𝗆𝖻 ​ l ​ k {\sf comb}\;l\;k generates all sorted k k -element sublists of a sorted list l l, all n ​ k ​ m nkm -lists for given n n, k k and m m can be generated by 𝖿𝖺𝗆𝗌 n ​ k ​ m ≡ 𝖼𝗈𝗆𝖻 ( 𝖼𝗈𝗆𝖻 [0.. < n] k) m {\sf fams}^{nkm}\equiv{\sf comb}\;({\sf comb}\;[0..<n]\;k)\;m.

#### Symmetries.

Often one uniform n ​ k ​ m nkm -family can be obtained from the other by permuting its elements (e.g., { { a 0, a 1, a 2 }, { a 1, a 3, a 4 }, { a 2, a 3, a 4 } } \{\{a_{0},a_{1},a_{2}\},\{a_{1},a_{3},a_{4}\},\{a_{2},a_{3},a_{4}\}\} can be obtained from { { a 0, a 1, a 2 }, { a 0, a 1, a 3 }, { a 2, a 3, a 4 } } \{\{a_{0},a_{1},a_{2}\},\{a_{0},a_{1},a_{3}\},\{a_{2},a_{3},a_{4}\}\} by the permutation ( a 0 CLOSE, (a_{0}, a 1, a_{1}, a 2, a_{2}, a 3, a_{3}, OPEN a 4) a_{4}) ↦ \mapsto ( a 3, a 4, a 1, a 2, a 0) (a_{3},a_{4},a_{1},a_{2},a_{0})). Applying permutations on sets and families can be implemented in Isabelle/HOL by the functions 𝗉𝖾𝗋𝗆 _ 𝗌𝖾𝗍 A p ≡ 𝗌𝗈𝗋𝗍 ( 𝗆𝖺𝗉 ( λ x. p [x]) A) {\sf perm\_set}\ A\ p\equiv{\sf sort}\ ({\sf map}\ (\lambda x.\ p_{[x]})\ A) and 𝗉𝖾𝗋𝗆 ​ _ ​ 𝖿𝖺𝗆 ​ F ​ p ≡ 𝗌𝗈𝗋𝗍 ⁡ ( 𝗆𝖺𝗉 ​ 𝗉𝖾𝗋𝗆 ​ _ ​ 𝗌𝖾𝗍 ​ F) {\sf perm\_fam}\ F\ p\equiv{\sf sort}\ ({\sf map}\ {\sf perm\_set}\ F). Permutations establish bijections between natural uniform families:

###### Proposition 7

If p p is a permutation of [0, 1, …, n − 1] [0,1,\ldots,n-1] and F F is a natural uniform family, then 𝗉𝖾𝗋𝗆 ​ _ ​ 𝖿𝖺𝗆 ​ F ​ p {\sf perm\_fam}\ F\ p is also natural uniform family and there is a bijection between F F and 𝗉𝖾𝗋𝗆 ​ _ ​ 𝖿𝖺𝗆 ​ F ​ p {\sf perm\_fam}\ F\ p.

Since, by Proposition 2, FC-families are preserved under bijections (isomorphisms), to check if all elements of a given list of n ​ k ​ m nkm -families ℱ \mathcal{F} are FC-families, many elements need not be considered. Indeed, it suffices to consider only a list (denoted by 𝗇𝖾𝖿 P ​ ℱ {\sf nef}^{P}\ \mathcal{F}) of its non-equivalent representatives (under a given list of permutations P P). Computation of such representatives can start from the given list ℱ \mathcal{F}, choose its arbitrary member for a representative, remove it and all its permuted variants from the lists, and repeat this sieving process until the list becomes empty. Isabelle/HOL implementation of this procedure can be given by:

 | 𝗇𝖾𝖿 ​ _ ​ 𝖺𝗎𝗑 P ​ ℱ ​ ℱ r \displaystyle{\sf nef\_aux}^{P}\ \mathcal{F}\ \mathcal{F}_{r} | ≡ \displaystyle\equiv | case ​ ℱ ​ of ​ [] ⇒ ℱ r \displaystyle\mathrm{case}\ \mathcal{F}\ \mathrm{of}\ [\,]\Rightarrow\mathcal{F}_{r} |  |

 |  | | \displaystyle| | F #⇒ let ℱ F P = 𝗋𝖾𝗆𝖽𝗎𝗉𝗌 ( 𝗆𝖺𝗉 ( λ p. 𝗉𝖾𝗋𝗆 _ 𝖿𝖺𝗆 F p) P) in \displaystyle F\;\#\;\vbox{\hrule width=5.55002pt}\Rightarrow\mathrm{let}\ \mathcal{F}_{F}^{P}={\sf remdups}\ ({\sf map}\ (\lambda\ p.\ {\sf perm\_fam}\ F\ p)\ P)\ \mathrm{in} |  |

 |  |  | 𝗇𝖾𝖿 _ 𝖺𝗎𝗑 P ( 𝖿𝗂𝗅𝗍𝖾𝗋 ( λ F. F ∉ ℱ F P) ℱ) ( F #ℱ r) \displaystyle\hskip 18.49988pt\hskip 18.49988pt{\sf nef\_aux}^{P}\ ({\sf filter}\ (\lambda\ F.\ F\notin\mathcal{F}_{F}^{P})\ \mathcal{F})\ (F\;\#\;\mathcal{F}_{r}) |  |

 | 𝗇𝖾𝖿 P ​ ℱ \displaystyle{\sf nef}^{P}\ \mathcal{F} | ≡ \displaystyle\equiv | 𝗇𝖾𝖿 ​ _ ​ 𝖺𝗎𝗑 P ​ ℱ ​ [] \displaystyle{\sf nef\_aux}^{P}\ \mathcal{F}\ [\,] |  |

The following lemma proves the correctness of this implementation.

###### Lemma 6

If P P is a list of permutations of [0, 1, …, n − 1] [0,1,\ldots,n-1] and if ℱ \mathcal{F} is a list of natural n ​ k ​ m nkm -families, then for each element F ∈ ℱ F\in\mathcal{F} there is an F ′ ∈ 𝗇𝖾𝖿 P ​ ℱ F^{\prime}\in{\sf nef}^{P}\ \mathcal{F} such there is a bijection between F F and F ′ F^{\prime}.

###### Proof

First, note that the function 𝗇𝖾𝖿 ​ _ ​ 𝖺𝗎𝗑 P ​ ℱ ​ ℱ r {\sf nef\_aux}^{P}\ \mathcal{F}\ \mathcal{F}_{r} is monotone, i.e., ℱ r ⊆ 𝗇𝖾𝖿 ​ _ ​ 𝖺𝗎𝗑 P ​ ℱ ​ ℱ r \mathcal{F}_{r}\subseteq{\sf nef\_aux}^{P}\ \mathcal{F}\ \mathcal{F}_{r}.

By induction, we show that if the assumptions hold for ℱ \mathcal{F} and P P, then for each element F ∈ ℱ F\in\mathcal{F} there is an element F ′ ∈ 𝗇𝖾𝖿 ​ _ ​ 𝖺𝗎𝗑 P ​ ℱ ​ ℱ r F^{\prime}\in{\sf nef\_aux}^{P}\ \mathcal{F}\ \mathcal{F}_{r} such there is a bijection between F F and F ′ F^{\prime}.

In the base case, when ℱ \mathcal{F} is empty, the statement trivially holds.

Assume that ℱ ≡ F ​ #​ ℱ ′ \mathcal{F}\equiv F\;\#\;\mathcal{F}^{\prime}. Let ℱ F P \mathcal{F}_{F}^{P} denote all different families obtained by permuting F F by all elements of P P (i.e., ℱ F P ≡ 𝗋𝖾𝗆𝖽𝗎𝗉𝗌 ( 𝗆𝖺𝗉 ( λ p. 𝗉𝖾𝗋𝗆 _ 𝖿𝖺𝗆 F p) P) \mathcal{F}_{F}^{P}\equiv{\sf remdups}\ ({\sf map}\ (\lambda\ p.\ {\sf perm\_fam}\ F\ p)\ P)) and let ℱ − \mathcal{F}^{-} denote what remains of ℱ \mathcal{F} when those are removed (i.e., ℱ − ≡ 𝖿𝗂𝗅𝗍𝖾𝗋 ( λ F. F ∉ ℱ F P) ℱ \mathcal{F}^{-}\equiv{\sf filter}\ (\lambda\ F.\ F\notin\mathcal{F}_{F}^{P})\ \mathcal{F}. It holds that 𝗇𝖾𝖿 ​ _ ​ 𝖺𝗎𝗑 P ​ ℱ ​ ℱ r = 𝗇𝖾𝖿 ​ _ ​ 𝖺𝗎𝗑 P ​ ℱ − ​ ( F ​ #​ ℱ r) {\sf nef\_aux}^{P}\ \mathcal{F}\ \mathcal{F}_{r}={\sf nef\_aux}^{P}\ \mathcal{F}^{-}\ (F\;\#\;\mathcal{F}_{r}).

Let F ′ F^{\prime} be an arbitrary element from ℱ \mathcal{F}. Since ℱ = F ​ #​ ℱ ′ \mathcal{F}=F\;\#\;\mathcal{F}^{\prime}, either F ′ = F F^{\prime}=F or F ′ ∈ ℱ ′ F^{\prime}\in\mathcal{F}^{\prime}.

Assume that F ′ = F F^{\prime}=F. By monotonicity it holds that F ∈ 𝗇𝖾𝖿 ​ _ ​ 𝖺𝗎𝗑 P ​ ℱ ​ ℱ r F\in{\sf nef\_aux}^{P}\ \mathcal{F}\ \mathcal{F}_{r}, so F F is an element from 𝗇𝖾𝖿 ​ _ ​ 𝖺𝗎𝗑 P ​ ℱ ​ ℱ r {\sf nef\_aux}^{P}\ \mathcal{F}\ \mathcal{F}_{r} such that there is a bijection (identity function) between F ′ F^{\prime} and it.

Assume that F ′ ∈ ℱ ′ F^{\prime}\in\mathcal{F}^{\prime}.

Consider the case when F ′ ∈ ℱ F P F^{\prime}\in\mathcal{F}_{F}^{P}. Then there is p ∈ P p\in P such that F ′ = 𝗉𝖾𝗋𝗆 ​ _ ​ 𝖿𝖺𝗆 ​ F ​ p F^{\prime}={\sf perm\_fam}\ F\ p. Since F ′ ∈ ℱ F^{\prime}\in\mathcal{F} is natural and p ∈ P p\in P is a permutation of [0, 1, …, n − 1] [0,1,\ldots,n-1], by Proposition 7, there is a bijection between F F and F ′ F^{\prime}. Since, by monotonicity, it holds that F ∈ 𝗇𝖾𝖿 ​ _ ​ 𝖺𝗎𝗑 P ​ ℱ ​ ℱ r F\in{\sf nef\_aux}^{P}\ \mathcal{F}\ \mathcal{F}_{r}, F F is an element in 𝗇𝖾𝖿 ​ _ ​ 𝖺𝗎𝗑 P ​ ℱ ​ ℱ r {\sf nef\_aux}^{P}\ \mathcal{F}\ \mathcal{F}_{r} such that there is a bijection between F ′ F^{\prime} and it.

Consider the case when F ′ ∉ ℱ F P F^{\prime}\notin\mathcal{F}_{F}^{P}. Then F ′ ∈ ℱ − F^{\prime}\in\mathcal{F}^{-}. By inductive hypothesis for the call 𝗇𝖾𝖿 ​ _ ​ 𝖺𝗎𝗑 P ​ ℱ − ​ ( F ​ #​ ℱ r) {\sf nef\_aux}^{P}\ \mathcal{F}^{-}\ (F\;\#\;\mathcal{F}_{r}), there is an element F ′′ F^{\prime\prime} in F ​ #​ ℱ r F\;\#\;\mathcal{F}_{r} such that there is a bijection between F ′ F^{\prime} and it. By monotonicity, F ′′ ∈ F ​ #​ ℱ r ⊆ 𝗇𝖾𝖿 ​ _ ​ 𝖺𝗎𝗑 P ​ ℱ − ​ ( F ​ #​ ℱ r) = 𝗇𝖾𝖿 ​ _ ​ 𝖺𝗎𝗑 P ​ ℱ ​ ℱ r F^{\prime\prime}\in F\;\#\;\mathcal{F}_{r}\subseteq{\sf nef\_aux}^{P}\ \mathcal{F}^{-}\ (F\;\#\;\mathcal{F}_{r})={\sf nef\_aux}^{P}\ \mathcal{F}\ \mathcal{F}_{r}, so the statement holds.

Finally, the following lemma shows that only non-equivalent representatives need to be considered when checking FC-families.

###### Lemma 7

Let ℱ ⊆ 𝖿𝖺𝗆𝗌 n ​ k ​ m \mathcal{F}\subseteq{\sf fams}^{nkm} and P ⊆ 𝗉𝖾𝗋𝗆 ⁡ [0, 1, …, n − 1] P\subseteq{\sf perm}\;[0,1,\ldots,n-1]. If all families represented by elements of 𝗇𝖾𝖿 P ​ ℱ {\sf nef}^{P}\ \mathcal{F} are FC-families, then all families represented by elements of 𝖿𝖺𝗆𝗌 n ​ k ​ m {\sf fams}^{nkm} are FC-families.

###### Proof

Let F ∈ 𝖿𝖺𝗆𝗌 n ​ k ​ m F\in{\sf fams}^{nkm}. By Lemma 6 there is an F ′ ∈ 𝗇𝖾𝖿 P ​ ℱ F^{\prime}\in{\sf nef}^{P}\ \mathcal{F} and a bijection between F F and F ′ F^{\prime}. So, F ′ F^{\prime} is an FC-family, and by Proposition 2, so is F F.

## 5 FC-families verified

Having established all the necessary mathematics, in this Section we prove that certain uniform families are FC-families (mainly by performing verified calculations). First, we calculate non-equivalent representatives for 𝖿𝖺𝗆𝗌 533 {\sf fams}^{533}, 𝖿𝖺𝗆𝗌 634 {\sf fams}^{634}, and 𝖿𝖺𝗆𝗌 734 {\sf fams}^{734}.

###### Lemma 8

The first column of Table 1 contains (respectively) all elements of:

𝗇𝖾𝖿 𝗉𝖾𝗋𝗆 [0.. < 5] 𝖿𝖺𝗆𝗌 533 {\sf nef}^{{\sf perm}\;[0..<5]}\ {\sf fams}^{533},

𝗇𝖾𝖿 𝗉𝖾𝗋𝗆 [0.. < 6] ( 𝖿𝗂𝗅𝗍𝖾𝗋 ( λ F. ¬ 𝖼𝗁𝖾𝖼𝗄 𝟧𝟥𝟥 𝖥) 𝖿𝖺𝗆𝗌 634) {\sf nef}^{{\sf perm}\;[0..<6]}\ ({\sf filter}\ (\lambda F.\ \neg{\sf check_{533}\ F})\ {\sf fams}^{634}),

𝗇𝖾𝖿 𝗉𝖾𝗋𝗆 [0.. < 7] ( 𝖿𝗂𝗅𝗍𝖾𝗋 ( λ F. ¬ 𝖼𝗁𝖾𝖼𝗄 𝟧𝟥𝟥 F ∧ ¬ 𝖼𝗁𝖾𝖼𝗄 𝟨𝟥𝟦 F) 𝖿𝖺𝗆𝗌 734), {\sf nef}^{{\sf perm}\;[0..<7]}\ ({\sf filter}\ (\lambda F.\ \neg{\sf check_{533}}\ F\wedge\neg{\sf check_{634}}\ F)\ {\sf fams}^{734}),

where 𝗉𝖾𝗋𝗆 ​ l {\sf perm}\;l is the function that generates all permutations of a list l l, 𝖼𝗁𝖾𝖼𝗄 𝟧𝟥𝟥 {\sf check_{533}} is a function that checks if any 3 of the 4 given 3-element sets are have their union contained in a 5-element set, and 𝖼𝗁𝖾𝖼𝗄 𝟨𝟥𝟦 {\sf check_{634}} is a function that checks if the union of 4 given 3-element sets is contained in a 6-element set. 7 7 7 Formal definition of these functions is not given here and is available in the Isabelle/HOL proof documents, along with correctness arguments.

###### Proof

By calculations performed by a computer.

F c F_{c} | w w |

[[0, 1]] [[0,1]] | 0 ↦ 1, 1 ↦ 1 0\mapsto 1,1\mapsto 1 |

[[0, 1, 2], [0, 1, 3], [2, 3, 4]] [[0,1,2],[0,1,3],[2,3,4]] | 0 ↦ 2, 1 ↦ 2, 2 ↦ 2, 3 ↦ 2, 4 ↦ 1 0\mapsto 2,1\mapsto 2,2\mapsto 2,3\mapsto 2,4\mapsto 1 |

[[0, 1, 2], [0, 1, 3], [0, 2, 4]] [[0,1,2],[0,1,3],[0,2,4]] | 0 ↦ 6, 1 ↦ 5, 2 ↦ 5, 3 ↦ 3, 4 ↦ 3 0\mapsto 6,1\mapsto 5,2\mapsto 5,3\mapsto 3,4\mapsto 3 |

[[0, 1, 2], [0, 1, 3], [0, 2, 3]] [[0,1,2],[0,1,3],[0,2,3]] | 0 ↦ 1, 1 ↦ 1, 2 ↦ 1, 3 ↦ 1 0\mapsto 1,1\mapsto 1,2\mapsto 1,3\mapsto 1 |

[[0, 1, 2], [0, 1, 3], [0, 1, 4]] [[0,1,2],[0,1,3],[0,1,4]] | 0 ↦ 3, 1 ↦ 3, 2 ↦ 2, 3 ↦ 2, 4 ↦ 2 0\mapsto 3,1\mapsto 3,2\mapsto 2,3\mapsto 2,4\mapsto 2 |

[[0, 1, 2], [0, 3, 4], [1, 3, 5], [2, 4, 5]] [[0,1,2],[0,3,4],[1,3,5],[2,4,5]] | 0 ↦ 1, 1 ↦ 1, 2 ↦ 1, 3 ↦ 1, 4 ↦ 1, 5 ↦ 1 0\mapsto 1,1\mapsto 1,2\mapsto 1,3\mapsto 1,4\mapsto 1,5\mapsto 1 |

[[0, 1, 2], [0, 1, 3], [2, 4, 5], [3, 4, 5]] [[0,1,2],[0,1,3],[2,4,5],[3,4,5]] | 0 ↦ 1, 1 ↦ 1, 2 ↦ 1, 3 ↦ 1, 4 ↦ 1, 5 ↦ 1 0\mapsto 1,1\mapsto 1,2\mapsto 1,3\mapsto 1,4\mapsto 1,5\mapsto 1 |

[[0, 1, 2], [0, 3, 4], [1, 3, 5], [2, 4, 6]] [[0,1,2],[0,3,4],[1,3,5],[2,4,6]] | 0 ↦ 2, 1 ↦ 2, 2 ↦ 2, 3 ↦ 2, 4 ↦ 2, 5 ↦ 1, 6 ↦ 1 0\mapsto 2,1\mapsto 2,2\mapsto 2,3\mapsto 2,4\mapsto 2,5\mapsto 1,6\mapsto 1 |

[[0, 1, 2], [0, 3, 4], [0, 5, 6], [1, 3, 5]] [[0,1,2],[0,3,4],[0,5,6],[1,3,5]] | 0 ↦ 2, 1 ↦ 1, 2 ↦ 1, 3 ↦ 1, 4 ↦ 1, 5 ↦ 1, 6 ↦ 1 0\mapsto 2,1\mapsto 1,2\mapsto 1,3\mapsto 1,4\mapsto 1,5\mapsto 1,6\mapsto 1 |

[[0, 1, 2], [0, 1, 3], [2, 4, 5], [4, 5, 6]] [[0,1,2],[0,1,3],[2,4,5],[4,5,6]] | 0 ↦ 3, 1 ↦ 3, 2 ↦ 4, 3 ↦ 2, 4 ↦ 3, 5 ↦ 3, 6 ↦ 2 0\mapsto 3,1\mapsto 3,2\mapsto 4,3\mapsto 2,4\mapsto 3,5\mapsto 3,6\mapsto 2 |

[[0, 1, 2], [0, 1, 3], [2, 4, 5], [3, 4, 6]] [[0,1,2],[0,1,3],[2,4,5],[3,4,6]] | 0 ↦ 3, 1 ↦ 3, 2 ↦ 3, 3 ↦ 3, 4 ↦ 2, 5 ↦ 1, 6 ↦ 1 0\mapsto 3,1\mapsto 3,2\mapsto 3,3\mapsto 3,4\mapsto 2,5\mapsto 1,6\mapsto 1 |

[[0, 1, 2], [0, 1, 3], [0, 4, 5], [4, 5, 6]] [[0,1,2],[0,1,3],[0,4,5],[4,5,6]] | 0 ↦ 6, 1 ↦ 4, 2 ↦ 3, 3 ↦ 3, 4 ↦ 4, 5 ↦ 4, 6 ↦ 2 0\mapsto 6,1\mapsto 4,2\mapsto 3,3\mapsto 3,4\mapsto 4,5\mapsto 4,6\mapsto 2 |

[[0, 1, 2], [0, 1, 3], [0, 4, 5], [2, 4, 6]] [[0,1,2],[0,1,3],[0,4,5],[2,4,6]] | 0 ↦ 3, 1 ↦ 2, 2 ↦ 3, 3 ↦ 1, 4 ↦ 3, 5 ↦ 2, 6 ↦ 2 0\mapsto 3,1\mapsto 2,2\mapsto 3,3\mapsto 1,4\mapsto 3,5\mapsto 2,6\mapsto 2 |

[[0, 1, 2], [0, 1, 3], [0, 4, 5], [1, 4, 6]] [[0,1,2],[0,1,3],[0,4,5],[1,4,6]] | 0 ↦ 2, 1 ↦ 2, 2 ↦ 1, 3 ↦ 1, 4 ↦ 1, 5 ↦ 1, 6 ↦ 1 0\mapsto 2,1\mapsto 2,2\mapsto 1,3\mapsto 1,4\mapsto 1,5\mapsto 1,6\mapsto 1 |

[[0, 1, 2], [0, 1, 3], [0, 4, 5], [0, 4, 6]] [[0,1,2],[0,1,3],[0,4,5],[0,4,6]] | 0 ↦ 2, 1 ↦ 1, 2 ↦ 1, 3 ↦ 1, 4 ↦ 1, 5 ↦ 1, 6 ↦ 1 0\mapsto 2,1\mapsto 1,2\mapsto 1,3\mapsto 1,4\mapsto 1,5\mapsto 1,6\mapsto 1 |

Table 1: Families and weights

Next, we show that all these representatives have non-negative shares.

###### Lemma 9

For all F c F_{c} and w w given in Table 1, it holds that 𝗌𝗌𝗇 F c ~ w = ⊥ {\sf ssn}\ \tilde{F_{c}}\ w=\bot.

###### Proof

By calculations performed by a computer.

Finally, the main result can be easily proved.

###### Theorem 5.1

The following are FC-families:

1. 1.

all families containing one 1-element set (i.e., { { a } } \{\{a\}\});

2. 2.

all families containing one 2-element set (i.e., { { a, b } } \{\{a,b\}\}, for a ≠ b a\neq b);

3. 3.

all families containing 3 3-element sets whose union is contained in a 5-element set (i.e., uniform 533 533 -families);

4. 4.

all families containing 4 3-element sets whose union is contained in a 6-element set (i.e., uniform 634 634 -families);

5. 5.

all families containing 4 3-element sets whose union is contained in a 7-element set (i.e., uniform 734 734 -families).

###### Proof

The case 1 trivially holds (since for each family member A A that does not contain a a, there is a member A ∪ { a } A\cup\{a\} that contains a a).

Other proofs are based on the techniques described in this paper. By Proposition 2 it suffices to consider only families F F such that ⋃ F ⊆ { 0, 1, …, n − 1 } \bigcup F\subseteq{\{0,1,\ldots,n-1\}}. All families corresponding to rows in Table 1 are FC-families. Indeed, for each F c F_{c} and w w given in a table row, by Lemma 9 it holds that 𝗌𝗌𝗇 ​ F c ​ w {\sf ssn}\ F_{c}\ w. Therefore, by Lemma 3.1 for all F ′ ∈ 𝗎𝖼𝖾 ​ F c F^{\prime}\in{\sf uce}\ F_{c} it holds that w ¯ ( ⋃ F c) ​ ( F ′) ≥ 0 \bar{w}_{(\bigcup{F_{c}})}(F^{\prime})\geq 0. Then, F c F_{c} is FC-family by Theorem 2.1.

In the case 2 this completes the proof.

In the case 3 the statement holds by Lemma 7, since, by Lemma 8 four rows given in Table 1 correspond to four non-equivalent families.

To show the case 4, let F c F_{c} be any family containing 4 3-element sets whose union is contained in { 0, 1, …, 5 } \{0,1,\ldots,5\} and let F F be a union-closed family such that F ⊇ F c F\supseteq F_{c}. If 𝖼𝗁𝖾𝖼𝗄 533 ​ F c {\sf check}_{533}\ F_{c} holds (i.e., if union of any 3 members of F c F_{c} is contained in a 5-element set), then F F is Frankl’s by case 3. If ¬ 𝖼𝗁𝖾𝖼𝗄 533 ​ F c \neg{\sf check}_{533}\ F_{c} holds, then F c F_{c} is in 𝖿𝗂𝗅𝗍𝖾𝗋 ( λ F. ¬ 𝖼𝗁𝖾𝖼𝗄 533 F) 𝖿𝖺𝗆𝗌 634 {\sf filter}\ (\lambda F.\neg{\sf check}_{533}\ F)\ {\sf fams}^{634}. The statement then holds by Lemma 7, since, by Lemma 8 two rows given in Table 1 correspond to two non-equivalent families of 𝖿𝗂𝗅𝗍𝖾𝗋 ( λ F. ¬ 𝖼𝗁𝖾𝖼𝗄 533 F) 𝖿𝖺𝗆𝗌 634 {\sf filter}\ (\lambda F.\neg{\sf check}_{533}\ F)\ {\sf fams}^{634}.

The case 5 is proved similarly, using the proofs for both the case 3 and the case 4.

## 6 Conclusions and further work

In this paper, we have formalized (within Isabelle/HOL) a computer-assisted approach of Živković and Vučković for verifying FC-families. Well-known FC-families are confirmed and a new uniform FC-family is discovered.

The Isabelle/HOL formalization has around 260KB of data organized into around 6500 lines of Isabelle/Isar proof text. Ratio between the size of the formalization and the size of the corresponding pen and paper proof (DeBruijn index) is estimated at around 5.5. Total time required to do the formalization is very roughly estimated at around 200 man/hours (25 full working days spread over a period of around 8 months).

Total proof checking time of Isabelle/HOL takes around 28 minutes on a notebook PC with 2.1GHz Intel/Pentium CPU and 4GB RAM. The major fraction of this time (around 23 minutes) is spent in the combinatorial search. Checking Lemma 9 consumes most of this time, and its last 8 cases (related to the uniform-734 families) alone take 22.8 minutes. This is quite long compared to the original JAVA programs (that perform the whole combinatorial search in around 1 minute), but still bearable. The big difference is due to the use of machine-integers supporting atomic bitwise-or in JAVA and the use of big-integers that do not support atomic bitwise-or in Isabelle/ML. The search time could be reduced if machine-integers were also used in Isabelle/ML. In a simple approach, the code generator could be instructed to replace mathematical integers in the formalization by machine-integers in the code, but that would make a gap between the formalization and the generated code and would require trusting that no overflows occur. A better approach would require formalizing machine-integers and their properties and using them within the formalization itself.

Compared to the prior pen-and-paper work, the computer assisted approach significantly reduces the complexity of mathematical arguments behind the proof and employs computing-machinery in doing its best — quickly enumerating and checking a large search space. This enables formulation of a general framework for checking various FC-families, without the need of employing human intellectual resources in analyzing specificities of separate families. Compared to the work of Živković and Vučković, apart from achieving the highest level of trust possible, the significant contribution of the formalization is the clear separation of mathematical background and combinatorial search algorithms, not present in earlier work. Also, separation of abstract properties of search algorithms and technical details of their implementation significantly simplifies reasoning about their correctness and brings them much closer to classic mathematical audience, not inclined towards computer science.

This work represents a significant part in formally proving the Frankl’s conjecture for families F F such that | ⋃ F | ≤ 11 |\bigcup{F}|\leq 11, and | ⋃ F | ≤ 12 |\bigcup{F}|\leq 12 (already informally done by Živković and Vučković [17]) which in the focus of our current and future work. We also plan to investigate other FC-families (not necessarily uniform).

## References

- [1] Tetsuya Abe. Strong Semimodular Lattices and Frankl’s Conjecture. Algebra Universalis, 44:379–382, 2000.
- [2] Kenneth I. Appel and Wolfgang Haken. Every Planar Map is Four Colorable. American Mathematical Society, 1989.
- [3] Ivica Bošnjak and Petar Marković. The 11-element Case of Frankl’s Conjecture. Electronic Journal of Combinatorics, 15(1), 2008.
- [4] Giovanni Lo Faro. Union-closed Sets Conjecture: Improved Bounds. J. Combin. Math. Combin. Comput., 16:97–102, 1994.
- [5] Weidong Gao and Hongquan Yu. Note on the Union-Closed Sets Conjecture. Ars Combinatorica, 49, 1998.
- [6] Georges Gonthier. Formal Proof – the Four-Color Theorem. Notices of AMS, 55(11), 2008.
- [7] Petar Marković. An attempt at Frankl’s Conjecture. Publications de l’Institut Mathématique, 81(95):29–43, 2007.
- [8] Robert Morris. FC-families and Improved Bounds for Frankl’s Conjecture. European Journal of Combinatorics, 27(2):269 – 282, 2006.
- [9] Tobias Nipkow, Gertrud Bauer, and Paula Schultz. Flyspeck I: Tame Graphs. In Ulrich Furbach and Natarajan Shankar, editors, IJCAR, volume 4130 of LNCS, pages 21–35. Springer, 2006.
- [10] Tobias Nipkow, Lawrence C. Paulson, and Markus Wenzel. Isabelle/HOL — A Proof Assistant for Higher-Order Logic, volume 2283 of LNCS. Springer, 2002.
- [11] Bjorn Poonen. Union-closed Families. Journal of Combinatorial Theory, Series A, 59(2):253 – 268, 1992.
- [12] Jürgen Reinhold. Frankl’s Conjecture is True for Lower Semimodular Lattices. Graphs and Combinatorics, 16:115–116, 2000.
- [13] N. Robertson, D. P. Sanders, P. D. Seymour, and R. Thomas. The Four Colour Theorem. Journal of Combinatorial Theory, Series B, 1997.
- [14] Theresa P. Vaughan. Families Implying the Frankl Conjecture. European Journal of Combinatorics, 23(7):851 – 860, 2002.
- [15] Theresa P. Vaughan. A Note on the Union-closed Sets Conjecture. J. Combin. Math. Combin. Comput., 45:95–108, 2003.
- [16] Theresa P. Vaughan. Three-sets in a Union-closed Family. J. Combin. Math. Combin. Comput., 49:95–108, 2004.
- [17] Miodrag Živković and Bojan Vučković. The 12-element Case of Frankl’s Conjecture. submitted, 2012.

[◄][1][image: ar5iv homepage] [2]
[Feeling lucky?][3] [4]
[Conversion report][5]
[Report an issue][6]
[View original on arXiv][7] [►][8]


## Links

[1]: /html/1207.3602
[2]: /
[3]: /feeling_lucky
[4]: /land_of_honey_and_milk
[5]: /log/1207.3604
[6]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+1207.3604
[7]: https://arxiv.org/pdf/1207.3604
[8]: /html/1207.3605
