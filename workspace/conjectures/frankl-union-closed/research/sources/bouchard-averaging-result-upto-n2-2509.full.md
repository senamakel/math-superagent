<!-- source: https://arxiv.org/html/2509.12537 | converted from HTML -->

An averaging result for union-closed families of sets

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2509.12537v1 [math.CO] 16 Sep 2025

# An averaging result for union-closed families of sets

Christopher Bouchard

###### Abstract

Let 𝒜 \mathcal{A} be a union-closed family of sets with base set b ⁡ ( 𝒜) = ⋃ A ∈ 𝒜 A b(\mathcal{A})=\bigcup_{A\in\mathcal{A}}A denoted by [n] = { 1, ⋯, n } [n]=\{1,\cdots,n\}, and for any real x > 0 x>0, let 𝒜 < x = { A ∈ 𝒜 | | A | < x } \mathcal{A}_{<x}=\{A\in\mathcal{A}\ |\ |A|<x\}. Also, denote by ℬ \mathcal{B} any smallest irredundant subfamily of 𝒜 < n / 2 \mathcal{A}_{<n/2} such that b ⁡ ( ℬ) = b ⁡ ( 𝒜 < n / 2) b(\mathcal{B})=b(\mathcal{A}_{<n/2}). We prove that if 𝒜 \mathcal{A} is separating with height h = 4 ≤ n h=4\leq n and 0 ≤ | ℬ | ≤ 2 0\leq|\mathcal{B}|\leq 2, then the average size of a member set from 𝒜 \mathcal{A} is at least n / 2 n/2. We show that h = 4 h=4 is greatest possible with respect to this result, and conclude by considering the remaining domain 3 ≤ | ℬ | ≤ 4 3\leq|\mathcal{B}|\leq 4.

## 1. Introduction

A family of sets 𝒜 \mathcal{A} is union-closed if it is finite with at least one nonempty member set, all of its member sets are finite and distinct, and X, Y ∈ 𝒜 X,Y\in\mathcal{A} implies that X ∪ Y ∈ 𝒜 X\cup Y\in\mathcal{A}. Denote the base set ⋃ A ∈ 𝒜 A \bigcup_{A\in\mathcal{A}}A of 𝒜 \mathcal{A} by [n] = { 1, ⋯, n } [n]=\{1,\cdots,n\} (and generally of a family ℱ \mathcal{F} by b ⁡ ( ℱ) ≔ ⋃ F ∈ ℱ F b(\mathcal{F})\coloneqq\bigcup_{F\in\mathcal{F}}F). The union-closed sets conjecture, also referred to as Frankl’s conjecture, is a well-known problem that has been studied from various perspectives, including those of graph and lattice theory (see [2] and [10], respectively, for details of the pertinent formulations), and also information theory (see [9] for the initial breakthrough work and [4] for a description of several follow-up results). The conjecture is stated as follows:

Conjecture 1.1. For any union-closed family 𝒜 \mathcal{A}, there exists an element of [n] [n] that is in at least | 𝒜 | 2 \frac{|\mathcal{A}|}{2} member sets of 𝒜 \mathcal{A}.

For two sets X 1 X_{1} and X 2 X_{2}, we use the notation X 1 ⊊ X 2 X_{1}\subsetneq X_{2} to denote that X 1 X_{1} is a proper subset of X 2 X_{2}, i.e. ( X 1 ⊆ X 2) ∧ ( X 1 ≠ X 2) (X_{1}\subseteq X_{2})\land(X_{1}\neq X_{2}). A chain 𝒞 \mathcal{C} in a finite family of sets 𝒜 \mathcal{A} is a subfamily of 𝒜 \mathcal{A} such that ( X 1, X 2 ∈ 𝒞) ∧ ( X 1 ≠ X 2) ⟹ ( X 1 ⊊ X 2) ∨ ( X 2 ⊊ X 1) (X_{1},X_{2}\in\mathcal{C})\ \land\ (X_{1}\neq X_{2})\implies(X_{1}\subsetneq X_{2})\ \lor\ (X_{2}\subsetneq X_{1}), and the height of 𝒜 \mathcal{A}, denoted by h h, is the maximum size of a chain in 𝒜 \mathcal{A}. Conjecture 1.1 has been shown to hold for any union-closed family 𝒜 \mathcal{A} with h ≤ 3 h\leq 3 (see [13], as well as [5]). In general, we have the following:

Theorem 1.2. For any union-closed family 𝒜 \mathcal{A} with | 𝒜 | > 1 |\mathcal{A}|>1, there exists an element of [n] [n] that is in at least | 𝒜 | + h − 3 h − 1 \frac{|\mathcal{A}|+h-3}{h-1} member sets of 𝒜 \mathcal{A}.

Proof. Let 𝒜 \mathcal{A} be a union-closed family with | 𝒜 | > 1 |\mathcal{A}|>1, and consider any chain 𝒞 = { C 1, ⋯, C h } \mathcal{C}=\{C_{1},\cdots,C_{h}\} in 𝒜 \mathcal{A} of maximum size, where 1 ≤ i < j ≤ h 1\leq i<j\leq h implies that C j ⊊ C i C_{j}\subsetneq C_{i} without loss of generality. Since [n] ∈ 𝒜 [n]\in\mathcal{A} and every member set of 𝒜 \mathcal{A} is a subset of [n] [n], we have that C 1 = [n] C_{1}=[n]. For every i ∈ [h − 1] i\in[h-1], let c i c_{i} be some element from C i ∖ C i + 1 C_{i}\setminus C_{i+1}. We consider any X ∈ 𝒜 ∖ { C 1, C h } X\in\mathcal{A}\setminus\{C_{1},C_{h}\}, and assume that c i ∉ X c_{i}\not\in X for all i ∈ [h − 1] i\in[h-1]. It must be that X ∩ ( C 1 ∖ C 2) = ∅ X\cap(C_{1}\setminus C_{2})=\emptyset. (Otherwise, ∅ ⊊ X ∩ ( C 1 ∖ C 2) ⊊ C 1 ∖ C 2 \emptyset\subsetneq X\cap(C_{1}\setminus C_{2})\subsetneq C_{1}\setminus C_{2}, which implies that { C 1, C 2 ∪ X, C 2, ⋯, C h } \{C_{1},C_{2}\cup X,C_{2},\cdots,C_{h}\} is a chain of size h + 1 h+1 in 𝒜 \mathcal{A}, contradicting the definition of h h.) Now consider any i ∈ [h − 1] i\in[h-1] such that i ≥ 2 i\geq 2. If, for all j ∈ [i − 1] j\in[i-1], X ∩ ( C j ∖ C j + 1) = ∅ X\cap(C_{j}\setminus C_{j+1})=\emptyset, then X ∩ ( C i ∖ C i + 1) = ∅ X\cap(C_{i}\setminus C_{i+1})=\emptyset. (Otherwise, ∅ ⊊ X ∩ ( C i ∖ C i + 1) ⊊ C i ∖ C i + 1 \emptyset\subsetneq X\cap(C_{i}\setminus C_{i+1})\subsetneq C_{i}\setminus C_{i+1}, which implies that { C 1, ⋯, C i, C i + 1 ∪ X, C i + 1, ⋯, C h } \{C_{1},\cdots,C_{i},C_{i+1}\cup X,C_{i+1},\cdots,C_{h}\} is a chain of size h + 1 h+1 in 𝒜 \mathcal{A}, again contradicting the definition of h h.) Therefore, we have by induction that X ∩ ( C i ∖ C i + 1) = ∅ X\cap(C_{i}\setminus C_{i+1})=\emptyset for every i ∈ [h − 1] i\in[h-1], which implies that X ⊊ C h X\subsetneq C_{h}. We then have that { C 1, ⋯, C h, X } \{C_{1},\cdots,C_{h},X\} is a chain in 𝒜 \mathcal{A} of size h + 1 h+1, once again a contradiction with the definition of h h. Hence, there must exist i ∈ [h − 1] i\in[h-1] such that c i ∈ X c_{i}\in X. It follows that, for some j ∈ [h − 1] j\in[h-1], c j c_{j} is in at least | 𝒜 ∖ { C 1, C h } | h − 1 = | 𝒜 | − 2 h − 1 \frac{|\mathcal{A}\setminus\{C_{1},C_{h}\}|}{h-1}=\frac{|\mathcal{A}|-2}{h-1} member sets of 𝒜 ∖ { C 1, C h } \mathcal{A}\setminus\{C_{1},C_{h}\}. Then because c j c_{j} is in C 1 C_{1}, it must belong to at least | 𝒜 | − 2 h − 1 + 1 = | 𝒜 | + h − 3 h − 1 \frac{|\mathcal{A}|-2}{h-1}+1=\frac{|\mathcal{A}|+h-3}{h-1} member sets of 𝒜 \mathcal{A}, which completes the proof of Theorem 1.2.

A chain 𝒞 \mathcal{C} in 𝒜 \mathcal{A} is maximal if 𝒞 ⊆ 𝒞 ′ \mathcal{C}\subseteq\mathcal{C}^{\prime} implies that 𝒞 = 𝒞 ′ \mathcal{C}=\mathcal{C}^{\prime} for any chain 𝒞 ′ \mathcal{C}^{\prime} in 𝒜 \mathcal{A}. We observe that Theorem 1.2 continues to hold if we replace h h with r r, where r r is the minimum size of a maximal chain in 𝒜 \mathcal{A}, thereby verifying Conjecture 1.1 for r ≤ 3 r\leq 3. Now, for h ≥ 4 h\geq 4, Conjecture 1.1 is stronger than Theorem 1.2. (Moreover, Theorem 1.2 is not optimal for h ≥ 4 h\geq 4 because in [12] it is shown that there is an element from [n] [n] in at least 3 − 5 2 ​ | 𝒜 | \frac{3-\sqrt{5}}{2}|\mathcal{A}| member sets of 𝒜 \mathcal{A}.) Hence, for values of h h greater than or equal to 4 4, Conjecture 1.1 requires other proof techniques. Averaging is a common approach to Conjecture 1.1 (see Section 6 of [3] for detailed discussion, [1], [6], and [7] for example applications, and [11] for the lowest average set size of a union-closed family in terms of family size). In the present work, we consider its application to the case h = 4 h=4.

The following definitions pertain to any finite family of sets 𝒜 \mathcal{A} with base set [n] [n]:

- •

𝒜 \mathcal{A} is separating if, for any two distinct elements x x and y y in [n] [n], there exists A ∈ 𝒜 A\in\mathcal{A} such that ( x ∈ A ∧ y ∉ A) ∨ ( x ∉ A ∧ y ∈ A) (x\in A\ \land\ y\not\in A)\ \lor\ (x\not\in A\ \land\ y\in A).

- •

For any 𝒮 ⊆ 𝒜 \mathcal{S}\subseteq\mathcal{A} and S ∈ 𝒮 S\in\mathcal{S}, irr 𝒮 ​ ( S) ≔ { s ∈ S | s ∉ b ⁡ ( 𝒮 ∖ { S }) } \texttt{irr}_{\mathcal{S}}(S)\coloneqq\{s\in S\ |\ s\not\in b(\mathcal{S}\setminus\{S\})\}. Accordingly, 𝒮 \mathcal{S} is irreduntant if S ∈ 𝒮 S\in\mathcal{S} implies that irr 𝒮 ​ ( S) ≠ ∅ \texttt{irr}_{\mathcal{S}}(S)\neq\emptyset.

- •

For any real x ≥ 0 x\geq 0, 𝒜 < x ≔ { A ∈ 𝒜 | | A | < x } \mathcal{A}_{<x}\coloneqq\{A\in\mathcal{A}\ |\ |A|<x\}, 𝒜 ≤ x ≔ { A ∈ 𝒜 | | A | ≤ x } \mathcal{A}_{\leq x}\coloneqq\{A\in\mathcal{A}\ |\ |A|\leq x\}, 𝒜 > x ≔ { A ∈ 𝒜 | | A | > x } \mathcal{A}_{>x}\coloneqq\{A\in\mathcal{A}\ |\ |A|>x\}, and 𝒜 ≥ x ≔ { A ∈ 𝒜 | | A | ≥ x } \mathcal{A}_{\geq x}\coloneqq\{A\in\mathcal{A}\ |\ |A|\geq x\}. Similarly, for any X ⊆ [n] X\subseteq[n], 𝒜 ⊊ X ≔ { A ∈ 𝒜 | A ⊊ X } \mathcal{A}_{\subsetneq X}\coloneqq\{A\in\mathcal{A}\ |\ A\subsetneq X\} and 𝒜 ⊆ X ≔ { A ∈ 𝒜 | A ⊆ X } \mathcal{A}_{\subseteq X}\coloneqq\{A\in\mathcal{A}\ |\ A\subseteq X\}.

- •

We set B = b ⁡ ( 𝒜 < n / 2) B=b(\mathcal{A}_{<n/2}), and denote by ℬ ≔ ℬ ⁡ ( 𝒜) \mathcal{B}\coloneqq\mathcal{B}(\mathcal{A}) any irredundant subfamily of 𝒜 < n / 2 \mathcal{A}_{<n/2} of minimum size such that b ⁡ ( ℬ) = B b(\mathcal{B})=B.

The main result of this work, proved in the next section, is that the average size of a member set in any separating union-closed family 𝒜 \mathcal{A} with h = 4 ≤ n h=4\leq n and 0 ≤ | ℬ | ≤ 2 0\leq|\mathcal{B}|\leq 2 is at least n 2 \frac{n}{2}, which implies that Conjecture 1.1 holds for these particular families. We also demonstrate via an appropriate construction that, with respect to this averaging result, h = 4 h=4 is greatest possible, and we conclude with partial results for when 3 ≤ | ℬ | ≤ 4 3\leq|\mathcal{B}|\leq 4. The following lemma is essential to this study.

Lemma 1.3. For any separating union-closed family 𝒜 \mathcal{A}, every maximal chain 𝒞 \mathcal{C} in 𝒜 \mathcal{A} contains a member set of size n − 1 n-1.

Proof: Let 𝒜 \mathcal{A} be a separating union-closed family, and 𝒞 = { C 1, ⋯, C | 𝒞 | } \mathcal{C}=\{C_{1},\cdots,C_{|\mathcal{C}|}\} be any maximal chain in 𝒜 \mathcal{A}, where 1 ≤ i < j ≤ | 𝒞 | 1\leq i<j\leq|\mathcal{C}| implies that C j ⊊ C i C_{j}\subsetneq C_{i} without loss of generality. We have that C 1 = [n] C_{1}=[n], as [n] ∈ 𝒜 [n]\in\mathcal{A} and every member set of 𝒜 \mathcal{A} is a subset of [n] [n]. Assume that 𝒞 \mathcal{C} has no member set of size n − 1 n-1, which is equivalent to the assumption that | C 2 | < n − 1 |C_{2}|<n-1. This implies that | C 1 ∖ C 2 | ≥ 2 |C_{1}\setminus C_{2}|\geq 2. Then, because 𝒜 \mathcal{A} is separating, there must exist A ∈ 𝒜 A\in\mathcal{A} and two elements x, y ∈ C 1 ∖ C 2 x,y\in C_{1}\setminus C_{2} such that x ∈ A x\in A and y ∉ A y\not\in A. It follows that 𝒞 ′ = { C 1, C 2 ∪ A, C 2, ⋯, C | 𝒞 | } \mathcal{C}^{\prime}=\{C_{1},C_{2}\cup A,C_{2},\cdots,C_{|\mathcal{C}|}\} is a chain in 𝒜 \mathcal{A} such that 𝒞 ⊊ 𝒞 ′ \mathcal{C}\subsetneq\mathcal{C}^{\prime}, which contradicts the maximality of 𝒞 \mathcal{C}. Thus, | C 2 | = n − 1 |C_{2}|=n-1, proving Lemma 1.3.

Lemma 1.3 of course applies to any chain of maximum size h h in 𝒜 \mathcal{A}. Throughout this writing, we denote by Y Y some member set of 𝒜 \mathcal{A} such that | Y | = n − 1 |Y|=n-1, with existence guaranteed by the lemma. We also denote by Avg ​ ( 𝒜) \textrm{Avg}(\mathcal{A}) the average size of a member set in 𝒜 \mathcal{A}, i.e. Avg ​ ( 𝒜) = ∑ A ∈ 𝒜 | A | | 𝒜 | \textrm{Avg}(\mathcal{A})=\frac{\sum_{A\in\mathcal{A}}|A|}{|\mathcal{A}|}. Considering Lemma 1.3, we conclude the current section with the following theorem:

Theorem 1.4. If 𝒜 \mathcal{A} is a separating union-closed family with h ≤ 3 h\leq 3, then Avg ​ ( 𝒜) ≥ n 2 \textrm{Avg}(\mathcal{A})\geq\frac{n}{2}.

Proof. First, we assume that h ≤ 2 h\leq 2. By Lemma 1.3, 𝒜 = [n] ∪ ℳ \mathcal{A}=[n]\cup\mathcal{M}, where M ∈ ℳ M\in\mathcal{M} implies that | M | = n − 1 |M|=n-1. Thus, Avg ​ ( 𝒜) = n + k ⁡ ( n − 1) k + 1 \textrm{Avg}(\mathcal{A})=\frac{n+k(n-1)}{k+1} for some k ∈ { 0, 1, ⋯, n } k\in\{0,1,\cdots,n\}, which implies that Avg ​ ( 𝒜) ≥ n 2 \textrm{Avg}(\mathcal{A})\geq\frac{n}{2}. Next, we assume that h = 3 h=3. If | 𝒜 < n / 2 | = 0 |\mathcal{A}_{<n/2}|=0, then | 𝒜 | ≥ n 2 |\mathcal{A}|\geq\frac{n}{2} for every A ∈ 𝒜 A\in\mathcal{A}, implying that Avg ​ ( 𝒜) ≥ n 2 \textrm{Avg}(\mathcal{A})\geq\frac{n}{2}. If | 𝒜 < n / 2 | = 1 |\mathcal{A}_{<n/2}|=1, then the subfamily 𝒜 ^ = 𝒜 < n / 2 ∪ { [n] } \hat{\mathcal{A}}=\mathcal{A}_{<n/2}\cup\{[n]\} of 𝒜 \mathcal{A} has Avg ​ ( 𝒜 ^) ≥ n 2 \textrm{Avg}(\hat{\mathcal{A}})\geq\frac{n}{2}, implying again that Avg ​ ( 𝒜) ≥ n 2 \textrm{Avg}(\mathcal{A})\geq\frac{n}{2}, as any member set in 𝒜 ∖ 𝒜 ^ \mathcal{A}\setminus\hat{\mathcal{A}} has size greater than or equal to n 2 \frac{n}{2}. Now, if | 𝒜 < n / 2 | ≥ 2 |\mathcal{A}_{<n/2}|\geq 2, then any distinct member sets X 1 X_{1} and X 2 X_{2} in 𝒜 < n / 2 \mathcal{A}_{<n/2} have X 1 ∩ X 2 = ∅ X_{1}\cap X_{2}=\emptyset and | X 1 | = | X 2 | = n − 1 2 |X_{1}|=|X_{2}|=\frac{n-1}{2}. (Otherwise, | X 1 ∪ X 2 | < n − 1 |X_{1}\cup X_{2}|<n-1 and ( X 1 ⊊ X 1 ∪ X 2 ⊊ [n]) ∨ ( X 2 ⊊ X 1 ∪ X 2 ⊊ [n]) (X_{1}\subsetneq X_{1}\cup X_{2}\subsetneq[n])\lor(X_{2}\subsetneq X_{1}\cup X_{2}\subsetneq[n]), contradicting Lemma 1.3.) If there exist only two member sets X 1 X_{1} and X 2 X_{2} in 𝒜 < n / 2 \mathcal{A}_{<n/2}, then the subfamily 𝒜 ^ = { X 1, X 2, [n] } \hat{\mathcal{A}}=\{X_{1},X_{2},[n]\} of 𝒜 \mathcal{A} has Avg ​ ( 𝒜 ^) = 2 ​ n − 1 3 ≥ n 2 \textrm{Avg}(\hat{\mathcal{A}})=\frac{2n-1}{3}\geq\frac{n}{2}, again implying that Avg ​ ( 𝒜) ≥ n 2 \textrm{Avg}(\mathcal{A})\geq\frac{n}{2}. Else, 𝒜 = { { 1, 2, 3 }, { 1, 2 }, { 1, 3 }, { 2, 3 }, { 1 }, { 2 }, { 3 } } \mathcal{A}=\{\{1,2,3\},\{1,2\},\{1,3\},\{2,3\},\{1\},\{2\},\{3\}\} and Avg ​ ( 𝒜) = 12 7 ≥ n 2 = 3 2 \textrm{Avg}(\mathcal{A})=\frac{12}{7}\geq\frac{n}{2}=\frac{3}{2}, completing the proof of Theorem 1.4.

## 2. The main result

We first note that 0 ≤ | ℬ | ≤ h 0\leq|\mathcal{B}|\leq h for any union-closed family 𝒜 \mathcal{A}. (Otherwise, for such a family 𝒜 \mathcal{A}, there exists { B 1, ⋯, B h + 1 } ⊆ ℬ \{B_{1},\cdots,B_{h+1}\}\subseteq\mathcal{B}, and B 1 ⊊ B 1 ∪ B 2 ⊊ ⋯ ⊊ ⋃ j ∈ [i] B j ⊊ ⋯ ⊊ ⋃ j ∈ [h] B j ⊊ ⋃ j ∈ [h + 1] B j B_{1}\subsetneq B_{1}\cup B_{2}\subsetneq\cdots\subsetneq\bigcup_{j\in[i]}B_{j}\subsetneq\cdots\subsetneq\bigcup_{j\in[h]}B_{j}\subsetneq\bigcup_{j\in[h+1]}B_{j}, forming a chain of size h + 1 h+1 in 𝒜 \mathcal{A}, which contradicts the definition of h h.) Thus, for any union-closed family 𝒜 \mathcal{A} with h = 4 h=4, | ℬ | |\mathcal{B}| must belong to the set { 0, 1, 2, 3, 4 } \{0,1,2,3,4\}. We now state the main theorem of this work:

Theorem 2.1. For any separating union-closed family 𝒜 \mathcal{A} with h = 4 ≤ n h=4\leq n and 0 ≤ | ℬ | ≤ 2 0\leq|\mathcal{B}|\leq 2:

 | Avg ​ ( 𝒜) = ∑ A ∈ 𝒜 | A | | 𝒜 | ≥ n 2 ​. \textrm{Avg}(\mathcal{A})=\frac{\sum_{A\in\mathcal{A}}|A|}{|\mathcal{A}|}\geq\frac{n}{2}\textrm{.} |  |

Proof of Theorem 2.1

The need for Theorem 2.1 to state that 4 ≤ n 4\leq n is a consequence of the separating union-closed family 𝒜 = { { 1, 2, 3 }, { 1, 2 }, { 1 }, { 2 }, ∅ } \mathcal{A}=\{\{1,2,3\},\{1,2\},\{1\},\{2\},\emptyset\} (or any relabeling thereof), which has h = 4 h=4 and 0 ≤ | ℬ | ≤ 2 0\leq|\mathcal{B}|\leq 2, yet also has n = 3 n=3 and Avg ​ ( 𝒜) = 7 5 < n 2 = 3 2 \textrm{Avg}(\mathcal{A})=\frac{7}{5}<\frac{n}{2}=\frac{3}{2}.

Let 𝒜 \mathcal{A} be any separating union-closed family with h = 4 ≤ n h=4\leq n and 0 ≤ | ℬ | ≤ 2 0\leq|\mathcal{B}|\leq 2. For the proof of Theorem 2.1, we must show that Avg ​ ( 𝒜) ≥ n 2 \textrm{Avg}(\mathcal{A})\geq\frac{n}{2}.

We first establish Propositions A, B, and C, valid for | B | < n − 1 |B|<n-1.

Proposition A. If X 1 X_{1} and X 2 X_{2} are distinct member sets of 𝒜 ⊊ B \mathcal{A}_{\subsetneq B}, then ( B ∖ X 1) ∩ ( B ∖ X 2) = ∅ (B\setminus X_{1})\cap(B\setminus X_{2})=\emptyset.

Proof. If not, then there exist some distinct X 1, X 2 ∈ 𝒜 ⊊ B X_{1},X_{2}\in\mathcal{A}_{\subsetneq B} such that ( B ∖ X 1) ∩ ( B ∖ X 2) ≠ ∅ (B\setminus X_{1})\cap(B\setminus X_{2})\neq\emptyset, and we have that ( X 1 ⊊ X 1 ∪ X 2 ⊊ B ⊊ [n]) ∨ ( X 2 ⊊ X 1 ∪ X 2 ⊊ B ⊊ [n]) (X_{1}\subsetneq X_{1}\cup X_{2}\subsetneq B\subsetneq[n])\lor(X_{2}\subsetneq X_{1}\cup X_{2}\subsetneq B\subsetneq[n]), contradicting Lemma 1.3.

Proposition B. ( Avg ​ ( 𝒜) ≥ n 2) ∨ ( 1 ≤ | 𝒜 ⊊ B | ≤ | B |) (\textrm{Avg}(\mathcal{A})\geq\frac{n}{2})\ \lor\ (1\leq|\mathcal{A}_{\subsetneq B}|\leq|B|).

Proof. If | 𝒜 ⊊ B | < 1 |\mathcal{A}_{\subsetneq B}|<1, then 𝒜 ⊊ B = ∅ \mathcal{A}_{\subsetneq B}=\emptyset and the subfamily 𝒜 ^ = 𝒜 ⊆ B ∪ { [n] } \hat{\mathcal{A}}=\mathcal{A}_{\subseteq B}\cup\{[n]\} of 𝒜 \mathcal{A} has Avg ​ ( 𝒜 ^) ≥ n 2 \textrm{Avg}(\hat{\mathcal{A}})\geq\frac{n}{2}. Then, because any member set of 𝒜 ∖ 𝒜 ^ \mathcal{A}\setminus\hat{\mathcal{A}} has size greater than or equal to n 2 \frac{n}{2}, we have that Avg ​ ( 𝒜) ≥ n 2 \textrm{Avg}(\mathcal{A})\geq\frac{n}{2}. Next, if | 𝒜 ⊊ B | > | B | |\mathcal{A}_{\subsetneq B}|>|B|, then 𝒜 ⊊ B = { X 1, ⋯, X k } \mathcal{A}_{\subsetneq B}=\{X_{1},\cdots,X_{k}\} for some k > | B | k>|B|. By Proposition A, ( B ∖ X 1), ⋯, ( B ∖ X k) (B\setminus X_{1}),\cdots,(B\setminus X_{k}) are all mutually disjoint. It follows that | B | < | ⋃ i ∈ [k] ( B ∖ X i) | |B|<\ |\bigcup_{i\in[k]}(B\setminus X_{i})|, which contradicts that ⋃ i ∈ [k] ( B ∖ X i) ⊆ B \bigcup_{i\in[k]}(B\setminus X_{i})\subseteq B.

Proposition C. ∑ X ∈ 𝒜 ⊊ B | X | ≥ ( | 𝒜 ⊊ B | − 1) ​ | B | \sum_{X\in\mathcal{A}_{\subsetneq B}}|X|\geq(|\mathcal{A}_{\subsetneq B}|-1)|B|.

Proof. By Proposition A, we have that ∑ X ∈ 𝒜 ⊊ B | B ∖ X | ≤ | B | \sum_{X\in\mathcal{A}_{\subsetneq B}}|B\setminus X|\leq|B|. Proposition C then follows from the identity ∑ X ∈ 𝒜 ⊊ B | X | = | B | ​ | 𝒜 ⊊ B | − ∑ X ∈ 𝒜 ⊊ B | B ∖ X | \sum_{X\in\mathcal{A}_{\subsetneq B}}|X|=|B||\mathcal{A}_{\subsetneq B}|-\sum_{X\in\mathcal{A}_{\subsetneq B}}|B\setminus X|.

We now divide the proof of Theorem 2.1 into cases based on the value of | ℬ | |\mathcal{B}|.

Case 0: ( | ℬ | = 0) (|\mathcal{B}|=0)

Here, if 𝒜 < n / 2 = ∅ \mathcal{A}_{<n/2}=\emptyset, then | A | ≥ n 2 |A|\geq\frac{n}{2} for every A ∈ 𝒜 A\in\mathcal{A}, making Avg ​ ( 𝒜) ≥ n 2 \textrm{Avg}(\mathcal{A})\geq\frac{n}{2}. Else, if 𝒜 < n / 2 = { ∅ } \mathcal{A}_{<n/2}=\{\emptyset\}, then consider the subfamily 𝒜 ^ = { ∅, [n] } \hat{\mathcal{A}}=\{\emptyset,[n]\} of 𝒜 \mathcal{A}. Because any member set in 𝒜 ∖ 𝒜 ^ \mathcal{A}\setminus\hat{\mathcal{A}} must have size greater than or equal to n 2 \frac{n}{2}, it follows from Avg ​ ( 𝒜 ^) = n 2 \textrm{Avg}(\hat{\mathcal{A}})=\frac{n}{2} that Avg ​ ( 𝒜) ≥ n 2 \textrm{Avg}(\mathcal{A})\geq\frac{n}{2}.

Case 1: ( | ℬ | = 1) (|\mathcal{B}|=1)

In this case, B B is the unique member set of ℬ \mathcal{B}, and we have that 𝒜 < | B | = 𝒜 ⊊ B \mathcal{A}_{<|B|}=\mathcal{A}_{\subsetneq B} and 𝒜 ≤ | B | = 𝒜 ⊆ B \mathcal{A}_{\leq|B|}=\mathcal{A}_{\subseteq B}.

We consider any A ∈ 𝒜 > | B | A\in\mathcal{A}_{>|B|}. If | A | < n 2 |A|<\frac{n}{2}, then either B ⊊ A B\subsetneq A, which contradicts that | B | |B| is greatest among member sets of 𝒜 < n / 2 \mathcal{A}_{<n/2}, or B ∖ A ≠ ∅ B\setminus A\neq\emptyset, implying that | ℬ | > 1 |\mathcal{B}|>1, again a contradiction.

By Proposition B, we have that | 𝒜 ⊆ B | ≤ | B | + 1 |\mathcal{A}_{\subseteq B}|\leq|B|+1. (We may assume that n > 4 n>4, as n = 4 n=4 implies that | 𝒜 < n / 2 | = 2 |\mathcal{A}_{<n/2}|=2, which when coupled with { Y, [n] } ⊆ 𝒜 > n / 2 \{Y,[n]\}\subseteq\mathcal{A}_{>n/2} in turn implies that Avg ​ ( 𝒜) ≥ n 2 \textrm{Avg}(\mathcal{A})\geq\frac{n}{2}.) It follows that | 𝒜 > | B | ∖ { Y, [n] } | ≥ | 𝒜 | − | B | − 3 ≥ | 𝒜 | − n + 5 2 ≥ | 𝒜 | − n |\mathcal{A}_{>|B|}\setminus\{Y,[n]\}|\geq|\mathcal{A}|-|B|-3\geq|\mathcal{A}|-\frac{n+5}{2}\geq|\mathcal{A}|-n. We let 𝒜 ^ = 𝒜 ∖ 𝒜 ~ \hat{\mathcal{A}}=\mathcal{A}\setminus\tilde{\mathcal{A}}, where 𝒜 ~ ⊆ 𝒜 > | B | ∖ { Y, [n] } \tilde{\mathcal{A}}\subseteq\mathcal{A}_{>|B|}\setminus\{Y,[n]\} such that | 𝒜 ~ | = | 𝒜 | − n |\tilde{\mathcal{A}}|=|\mathcal{A}|-n, so we have that | 𝒜 ^ | = n |\hat{\mathcal{A}}|=n. Existence of such a family 𝒜 ~ \tilde{\mathcal{A}} is guaranteed by the following lemma:

Lemma 2.1.1 (Falgas-Ravry [8]). If 𝒜 \mathcal{A} is a separating union-closed family, then | 𝒜 | ≥ n |\mathcal{A}|\geq n.

Proof: This follows from Lemma 2 of [8]. We provide a proof by induction on family size. For any family of sets ℱ \mathcal{F} and x ∈ b ⁡ ( ℱ) x\in b(\mathcal{F}), let ℱ { x } = { F ∈ ℱ | x ∈ F } \mathcal{F}_{\{x\}}=\{F\in\mathcal{F}\ |\ x\in F\}. Now, let 𝒜 \mathcal{A} be any separating union-closed family of sets. If | 𝒜 | = 1 |\mathcal{A}|=1, then | b ⁡ ( 𝒜) | = 1 |b(\mathcal{A})|=1 and | 𝒜 | ≥ | b ⁡ ( 𝒜) | |\mathcal{A}|\geq|b(\mathcal{A})|. If | 𝒜 | > 1 |\mathcal{A}|>1, then consider any x ∈ [n] x\in[n] such that | 𝒜 { x } | = max y ∈ [n] ⁡ { | 𝒜 { y } | } |\mathcal{A}_{\{x\}}|=\max_{y\in[n]}\{|\mathcal{A}_{\{y\}}|\}, and let 𝒜 ^ { x } = { A ∖ { x } | A ∈ 𝒜 { x } } \hat{\mathcal{A}}_{\{x\}}=\{A\setminus\{x\}\ |\ A\in\mathcal{A}_{\{x\}}\}. If 𝒜 { x } ⊊ 𝒜 \mathcal{A}_{\{x\}}\subsetneq\mathcal{A}, then let 𝒜 ′ = 𝒜 { x } \mathcal{A}^{\prime}=\mathcal{A}_{\{x\}}. Else, if 𝒜 { x } = 𝒜 \mathcal{A}_{\{x\}}=\mathcal{A}, then let 𝒜 ′ = ( 𝒜 ^ { x }) { y } \mathcal{A}^{\prime}=(\hat{\mathcal{A}}_{\{x\}})_{\{y\}} for some y ∈ b ⁡ ( 𝒜 ^ { x }) y\in b(\hat{\mathcal{A}}_{\{x\}}) such that | ( 𝒜 ^ { x }) { y } | = max z ∈ b ⁡ ( 𝒜 ^ { x }) ⁡ { | ( 𝒜 ^ { x }) { z } | } |(\hat{\mathcal{A}}_{\{x\}})_{\{y\}}|=\max_{z\in b(\hat{\mathcal{A}}_{\{x\}})}\{|{(\hat{\mathcal{A}}_{\{x\}}})_{\{z\}}|\}. In either case, 𝒜 ′ \mathcal{A}^{\prime} is union-closed and separating with | 𝒜 ′ | < | 𝒜 | |\mathcal{A}^{\prime}|<|\mathcal{A}|. We have that | 𝒜 ′ | ≥ | b ⁡ ( 𝒜 ′) | |\mathcal{A}^{\prime}|\geq|b(\mathcal{A}^{\prime})| by the induction hypothesis. Further, n − 1 ≤ | b ⁡ ( 𝒜 ′) | n-1\leq|b(\mathcal{A}^{\prime})|. It follows that | 𝒜 | ≥ n |\mathcal{A}|\geq n, completing the proof of Lemma 2.1.1.

Since any member set of 𝒜 ~ \tilde{\mathcal{A}} has size greater than or equal to n 2 \frac{n}{2}, it is sufficient for resolving Case 1 to prove that Avg ​ ( 𝒜 ^) ≥ n 2 \textrm{Avg}(\hat{\mathcal{A}})\geq\frac{n}{2}.

In this regard, we introduce the lower bound ζ ⁡ ( | B |, | 𝒜 ⊊ B |) \zeta(|B|,|\mathcal{A}_{\subsetneq B}|) of Avg ​ ( 𝒜 ^) \textrm{Avg}(\hat{\mathcal{A}}):

 | Avg ​ ( 𝒜 ^) = ∑ A ∈ 𝒜 ^ | A | | 𝒜 ^ | = | Y | + n + ∑ A ∈ 𝒜 ≤ | B | | A | + ∑ A ∈ 𝒜 ^ > | B | ∖ { Y, [n] } | A | n \hskip-19.20569pt\textrm{Avg}(\hat{\mathcal{A}})=\frac{\sum_{A\in\hat{\mathcal{A}}}|A|}{|\hat{\mathcal{A}}|}=\frac{|Y|+n+\sum_{A\in\mathcal{A}_{\leq|B|}}|A|+\sum_{A\in\hat{\mathcal{A}}_{>|B|}\setminus\{Y,[n]\}}|A|}{n} |  |

 | ≥ ζ ⁡ ( | B |, | 𝒜 ⊊ B |) = 2 ​ n − 1 + | B | ​ | 𝒜 ⊊ B | + ( n − | B | − 1) ​ ( n − | 𝒜 ⊊ B | − 3) n ​. \hskip 37.69981pt\geq\zeta(|B|,|\mathcal{A}_{\subsetneq B}|)=\frac{2n-1+|B||\mathcal{A}_{\subsetneq B}|+(n-|B|-1)(n-|\mathcal{A}_{\subsetneq B}|-3)}{n}\textrm{.} |  |

In the numerator of ζ ⁡ ( | B |, | 𝒜 ⊊ B |) \zeta(|B|,|\mathcal{A}_{\subsetneq B}|), 2 ​ n − 1 2n-1 comes from equality with | Y | + n |Y|+n, | B | ​ | 𝒜 ⊊ B | |B||\mathcal{A}_{\subsetneq B}| comes from being less than or equal to ∑ A ∈ 𝒜 ≤ | B | | A | \sum_{A\in\mathcal{A}_{\leq|B|}}|A| (by Proposition C), and ( n − | B | − 1) ​ ( n − | 𝒜 ⊊ B | − 3) (n-|B|-1)(n-|\mathcal{A}_{\subsetneq B}|-3) comes from all n − | 𝒜 ⊊ B | − 3 n-|\mathcal{A}_{\subsetneq B}|-3 member sets of 𝒜 ^ > | B | ∖ { Y, [n] } \hat{\mathcal{A}}_{>|B|}\setminus\{Y,[n]\} having size greater than or equal to n − | B | − 1 n-|B|-1. (If there exists X ∈ 𝒜 ^ > | B | ∖ { Y, [n] } X\in\hat{\mathcal{A}}_{>|B|}\setminus\{Y,[n]\} with | X | < n − | B | − 1 |X|<n-|B|-1, then | B ∪ X | < n − 1 |B\cup X|<n-1 and by Proposition B, we may assume that there exists A ∈ 𝒜 ⊊ B A\in\mathcal{A}_{\subsetneq B}. It follows that A ⊊ B ⊊ B ∪ X ⊊ [n] A\subsetneq B\subsetneq B\cup X\subsetneq[n], which contradicts Lemma 1.3.) A continuous relaxation of ζ \zeta is the function f: ℝ 2 → ℝ f\colon\mathbb{R}^{2}\to\mathbb{R} such that:

 | f ⁡ ( x, y) = n − x − y − 2 + 2 ​ x ​ y + 3 ​ x + y + 2 n. \ \ f(x,y)=n-x-y-2+\frac{2xy+3x+y+2}{n}{.} |  |

For Case 1, B B belongs to 𝒜 < n / 2 \mathcal{A}_{<n/2}, so | B | ≤ n − 1 2 |B|\leq\frac{n-1}{2}. Also, by Proposition B we may assume that 1 ≤ | 𝒜 ⊊ B | ≤ | B | 1\leq|\mathcal{A}_{\subsetneq B}|\leq|B|. Therefore, solving the following problem would provide a lower bound for Avg ​ ( 𝒜 ^) \textrm{Avg}(\hat{\mathcal{A}}):

 | min { f ( x, y) } s.t. 1 ≤ y ≤ x ≤ n − 1 2. \ \ \min\Bigr\{f(x,y)\Bigr\}\textrm{ s.t. }1\leq y\leq x\leq\frac{n-1}{2}\textrm{.} |  |

 | The problem has solution: f ( x ∗, y ∗) = n 2, at ( x ∗, y ∗) = ( n 2 − 1, n 2 − 1). \textrm{\hskip-123.76965ptThe problem has solution:}\hskip 27.03003ptf(x^{*},y^{*})=\frac{n}{2}\textrm{, at }(x^{*},y^{*})=\ \Bigr(\frac{n}{2}-1,\frac{n}{2}-1\Bigr)\textrm{.} |  |

Hence, Avg ​ ( 𝒜) ≥ n 2 \textrm{Avg}(\mathcal{A})\geq\frac{n}{2}, proving Case 1 of Theorem 2.1.

Denote by ( S k) \binom{S}{k} the family of k k -element subsets of a set S S. We conjecture that the minimum average member set size of a union-closed family 𝒜 \mathcal{A} such that h = 4 ≤ n h=4\leq n and | ℬ | = 1 |\mathcal{B}|=1 is achieved by the following family 𝒜 ∗ \mathcal{A}^{*} with b ⁡ ( 𝒜 ∗) = [n] b(\mathcal{A}^{*})=[n], as illustrated in Figure 2.1:

 | 𝒜 ∗ = { [n], [⌈ n 2 ⌉ − 1] } ∪ { [n] ∖ { x } | x ∈ [n] ∖ [⌈ n 2 ⌉] } ∪ ( [⌈ n 2 ⌉ − 1] ⌈ n 2 ⌉ − 2). \mathcal{A}^{*}=\ \Bigr\{[n],\Bigr[\Bigr\lceil\frac{n}{2}\Bigr\rceil-1\Bigr]\Bigr\}\ \ \cup\ \ \Bigr\{[n]\setminus\{x\}\ \Bigr|\ x\in\ [n]\ \setminus\ \Bigr[\Bigr\lceil\frac{n}{2}\Bigr\rceil\Bigr]\Bigr\}\ \ \cup\ \ \binom{[\lceil\frac{n}{2}\rceil-1]}{\lceil\frac{n}{2}\rceil-2}\textrm{.} |  |

To verify that 𝒜 ∗ \mathcal{A}^{*} is separating, we observe that for any two distinct elements x x and y y in [n] [n], the following member set S S of 𝒜 ∗ \mathcal{A}^{*} contains exactly one element from { x, y } \{x,y\}:

 | S = { [⌈ n 2 ⌉ − 1] ∖ { x } if ​ x, y ∈ [⌈ n 2 ⌉ − 1] [⌈ n 2 ⌉ − 1] if ​ min ⁡ { x, y } ∈ [⌈ n 2 ⌉ − 1] ∧ max ⁡ { x, y } ∈ [n] ∖ [⌈ n 2 ⌉ − 1] [n] ∖ { max ⁡ { x, y } } if ​ x, y ∈ [n] ∖ [⌈ n 2 ⌉ − 1] ​. S=\begin{cases}[\lceil\frac{n}{2}\rceil-1]\setminus\{x\}&\textrm{ if }x,y\in[\lceil\frac{n}{2}\rceil-1]\\ [\lceil\frac{n}{2}\rceil-1]&\textrm{ if }\min\{x,y\}\in[\lceil\frac{n}{2}\rceil-1]\ \land\ \max\{x,y\}\in[n]\setminus[\lceil\frac{n}{2}\rceil-1]\\ [n]\setminus\{\max\{x,y\}\}&\textrm{ if }x,y\in[n]\setminus[\lceil\frac{n}{2}\rceil-1]\par\end{cases}\textrm{.} |  |

Figure 2.1: Both parameters of ζ \zeta are equal to ⌈ n 2 ⌉ − 1 \lceil\frac{n}{2}\rceil-1 for 𝒜 ∗ \mathcal{A}^{*}. A ∈ 𝒜 ∗ A\in\mathcal{A}^{*} | A | |A| n n n − 1 n-1 n − 1 n-1 n − 1 n-1 ⋮ \vdots n − 1 n-1 n − 1 n-1 n − 1 n-1 ⌈ n / 2 ⌉ − 1 \lceil n/2\rceil-1 ⌈ n / 2 ⌉ − 2 \lceil n/2\rceil-2 ⌈ n / 2 ⌉ − 2 \lceil n/2\rceil-2 ⌈ n / 2 ⌉ − 2 \lceil n/2\rceil-2 ⋮ \vdots ⌈ n / 2 ⌉ − 2 \lceil n/2\rceil-2 ⌈ n / 2 ⌉ − 2 \lceil n/2\rceil-2 ⌈ n / 2 ⌉ − 2 \lceil n/2\rceil-2 ⋮ \vdots ⋮ \vdots

Case 2 ( | ℬ | = 2) (|\mathcal{B}|=2)

In this case, we let ℬ = { B 1, B 2 } \mathcal{B}=\{B_{1},B_{2}\}. We first assume that | B | < n − 1 |B|<n-1.

Let 𝒜 ^ = 𝒜 ⊆ B ∪ { Y, [n] } \hat{\mathcal{A}}=\mathcal{A}_{\subseteq B}\cup\{Y,[n]\}. We observe that | B | ≥ n 2 |B|\geq\frac{n}{2}, and that | A | ≥ n 2 |A|\geq\frac{n}{2} for any A ∈ 𝒜 < | B | ∖ 𝒜 ⊊ B A\in\mathcal{A}_{<|B|}\setminus\mathcal{A}_{\subsetneq B}. Therefore, any member set of 𝒜 ∖ 𝒜 ^ \mathcal{A}\setminus\hat{\mathcal{A}} has size greater than or equal to n 2 \frac{n}{2}, and it is sufficient for resolving this subcase to prove that Avg ​ ( 𝒜 ^) ≥ n 2 \textrm{Avg}(\hat{\mathcal{A}})\geq\frac{n}{2}. We introduce the lower bound η ⁡ ( | B |, | 𝒜 ⊊ B |) \eta(|B|,|\mathcal{A}_{\subsetneq B}|) of Avg ​ ( 𝒜 ^) \textrm{Avg}(\hat{\mathcal{A}}):

 | Avg ​ ( 𝒜 ^) = ∑ A ∈ 𝒜 ^ | A | | 𝒜 ^ | = | Y | + n + ∑ A ∈ 𝒜 ⊆ B | A | | 𝒜 ⊊ B | + 3 \hskip-24.89615pt\textrm{Avg}(\hat{\mathcal{A}})=\frac{\sum_{A\in\hat{\mathcal{A}}}|A|}{|\hat{\mathcal{A}}|}=\frac{|Y|+n+\sum_{A\in\mathcal{A}_{\subseteq B}}|A|}{|\mathcal{A}_{\subsetneq B}|+3} |  |

 | ≥ η ⁡ ( | B |, | 𝒜 ⊊ B |) = 2 ​ n − 1 + | B | ​ | 𝒜 ⊊ B | | 𝒜 ⊊ B | + 3 ​. \hskip 5.26369pt\geq\eta(|B|,|\mathcal{A}_{\subsetneq B}|)=\frac{2n-1+|B||\mathcal{A}_{\subsetneq B}|}{|\mathcal{A}_{\subsetneq B}|+3}\textrm{.} |  |

In the numerator of η ⁡ ( | B |, | 𝒜 ⊊ B |) \eta(|B|,|\mathcal{A}_{\subsetneq B}|), 2 ​ n − 1 2n-1 again comes from being equal to | Y | + n |Y|+n, and | B | ​ | 𝒜 ⊊ B | |B||\mathcal{A}_{\subsetneq B}| comes from being less than or equal to ∑ A ∈ 𝒜 ⊆ B | A | \sum_{A\in\mathcal{A}_{\subseteq B}}|A|. Then similar to f f from Case 1, a continuous relaxation of η \eta is the function g: ℝ × ℝ ∖ { − 3 } → ℝ g\colon\mathbb{R}\times\mathbb{R}\setminus\{-3\}\to\mathbb{R} such that:

 | g ⁡ ( x, y) = 2 ​ n + x ​ y − 1 y + 3. \ \ g(x,y)=\frac{2n+xy-1}{y+3}{.} |  |

Recall that n 2 ≤ | B | < n − 1 \frac{n}{2}\leq|B|<n-1, and by Proposition B, we may assume that 1 ≤ | 𝒜 ⊊ B | ≤ | B | 1\leq|\mathcal{A}_{\subsetneq B}|\leq|B|. Therefore, solving the following problem would provide a lower bound for Avg ​ ( 𝒜 ^) \textrm{Avg}(\hat{\mathcal{A}}):

 | min { g ( x, y) } s.t. ( n 2 ≤ x ≤ n − 2) ∧ ( 1 ≤ y ≤ x). \ \ \min\Bigr\{g(x,y)\Bigr\}\textrm{ s.t. }\Bigr(\frac{n}{2}\leq x\leq n-2\Bigr)\ \land\ \Bigr(1\leq y\leq x\Bigr)\textrm{.} |  |

 | The problem has solution: g ( x ∗, y ∗) = n 2 + n − 2 n + 6 > n 2, at ( x ∗, y ∗) = ( n 2, n 2). \textrm{\hskip-112.38829ptThe problem has solution:}\hskip 14.93752ptg(x^{*},y^{*})=\frac{n}{2}+\frac{n-2}{n+6}>\frac{n}{2}\textrm{, at }(x^{*},y^{*})=\ \Bigr(\frac{n}{2},\frac{n}{2}\Bigr)\textrm{.} |  |

Thus, Avg ​ ( 𝒜) ≥ n 2 \textrm{Avg}(\mathcal{A})\geq\frac{n}{2}, resolving Case 2 for | B | < n − 1 |B|<n-1.

Next, we assume that | B | = n − 1 |B|=n-1, and let B 1 = [n − 1 2] B_{1}=[\frac{n-1}{2}] and B 2 = [n − 1] ∖ B 1 B_{2}=[n-1]\setminus B_{1} without loss of generality.

If 𝒜 < n / 2 = ℬ \mathcal{A}_{<n/2}=\mathcal{B}, then we let 𝒜 ^ = { B 1, B 2, [n] } \hat{\mathcal{A}}=\{B_{1},B_{2},[n]\}, so Avg ​ ( 𝒜 ^) = 2 ​ n − 1 3 ≥ n 2 \textrm{Avg}(\hat{\mathcal{A}})=\frac{2n-1}{3}\geq\frac{n}{2}. Then Avg ​ ( 𝒜) ≥ n 2 \textrm{Avg}(\mathcal{A})\geq\frac{n}{2} because any member set in 𝒜 ∖ 𝒜 ^ \mathcal{A}\setminus\hat{\mathcal{A}} has size greater than or equal to n 2 \frac{n}{2}.

If there exist X 1 X_{1} and X 2 X_{2} in 𝒜 < n / 2 \mathcal{A}_{<n/2} such that ( X 1 ⊊ B 1) ∧ ( X 2 ⊊ B 2) (X_{1}\subsetneq B_{1})\land(X_{2}\subsetneq B_{2}), then X 1 ⊊ B 1 ⊊ B 1 ∪ X 2 ⊊ B ⊊ [n] X_{1}\subsetneq B_{1}\subsetneq B_{1}\cup X_{2}\subsetneq B\subsetneq[n], forming a chain of size 5 5 in 𝒜 \mathcal{A}, which contradicts h = 4 h=4.

There are two remaining assumptions that are possible for Case 2 when | B | = n − 1 |B|=n-1:

1.) 𝒜 < n / 2 ≠ ℬ ∧ ( ( A ∈ 𝒜 < n / 2 ∖ ℬ ⟹ A ⊊ B 1) ∨ ( A ∈ 𝒜 < n / 2 ∖ ℬ ⟹ A ⊊ B 2)) \mathcal{A}_{<n/2}\neq\mathcal{B}\ \land\ ((A\in\mathcal{A}_{<n/2}\setminus\mathcal{B}\implies A\subsetneq B_{1})\lor(A\in\mathcal{A}_{<n/2}\setminus\mathcal{B}\implies A\subsetneq B_{2})):

Without loss of generality, we assume that A ∈ 𝒜 < n / 2 ∖ ℬ ⟹ A ⊊ B 1 A\in\mathcal{A}_{<n/2}\setminus\mathcal{B}\implies A\subsetneq B_{1}. We observe that 𝒜 ′ = 𝒜 ∖ { B 2 } \mathcal{A}^{\prime}=\mathcal{A}\setminus\{B_{2}\} is a union-closed family with ℬ ⁡ ( 𝒜 ′) = { B 1 } = { B ′ } \mathcal{B}(\mathcal{A}^{\prime})=\{B_{1}\}=\{B^{\prime}\}. Additionally, we have that 𝒜 ′ \mathcal{A}^{\prime} is separating. (Otherwise, there exist x ∈ B 2 x\in B_{2} and y ∈ [n] ∖ B 2 y\in[n]\setminus B_{2} such that for any A ∈ 𝒜 ′ A\in\mathcal{A}^{\prime}, ( x ∈ A ∨ y ∈ A) ⟹ ( x ∈ A ∧ y ∈ A) (x\in A\ \lor\ y\in A)\implies(x\in A\ \land\ y\in A). Then B 1 ∩ B 2 = ∅ B_{1}\cap B_{2}=\emptyset implies that y ∉ B 1 y\not\in B_{1}, making y = n y=n. Thus, y ∉ [n − 1] y\not\in[n-1], yet x ∈ [n − 1] = B 1 ∪ B 2 ∈ 𝒜 ′ x\in[n-1]=B_{1}\cup B_{2}\in\mathcal{A}^{\prime}, a contradiction.) Hence, | 𝒜 ′ | ≥ n |\mathcal{A}^{\prime}|\geq n by Lemma 2.1.1, and 𝒜 ′ \mathcal{A}^{\prime} falls within the scope of Case 1. We apply the proof for Case 1 to 𝒜 ′ \mathcal{A}^{\prime}, considering the corresponding family 𝒜 ^ ′ = 𝒜 ′ ∖ 𝒜 ~ ′ \hat{\mathcal{A}}^{\prime}=\mathcal{A}^{\prime}\setminus\tilde{\mathcal{A}}^{\prime}, where 𝒜 ~ ′ ⊆ 𝒜 > | B ′ | ′ ∖ { Y, [n] } \tilde{\mathcal{A}}^{\prime}\subseteq\mathcal{A}^{\prime}_{>|B^{\prime}|}\setminus\{Y,[n]\} such that | 𝒜 ~ ′ | = | 𝒜 ′ | − n |\tilde{\mathcal{A}}^{\prime}|=|\mathcal{A}^{\prime}|-n. Because | B 2 | = n − 1 2 = n − | B ′ | − 1 |B_{2}|=\frac{n-1}{2}=n-|B^{\prime}|-1, B 2 B_{2} may be counted as one of the n − | 𝒜 ′ ⊊ B ′ | − 3 n-|{\mathcal{A}^{\prime}}_{\subsetneq B^{\prime}}|-3 member sets of 𝒜 ^ > | B ′ | ′ ∖ { Y, [n] } \hat{\mathcal{A}}^{\prime}_{>|B^{\prime}|}\setminus\{Y,[n]\} of size greater than or equal to n − | B ′ | − 1 n-|B^{\prime}|-1. (If there were no such member set, then n − | 𝒜 ⊊ B ′ ′ | − 3 = 0 ≥ n − n − 1 2 − 3 n-|\mathcal{A}^{\prime}_{\subsetneq B^{\prime}}|-3=0\geq n-\frac{n-1}{2}-3, implying that n ≤ 5 n\leq 5. Then n n being odd would imply that n = 5 n=5, and 𝒜 ′ \mathcal{A}^{\prime} would be equal to { { 1, 2, 3, 4, 5 }, Y, { 1, 2 }, { 1 }, { 2 } } \{\{1,2,3,4,5\},Y,\{1,2\},\{1\},\{2\}\} for some Y Y of size 4 4, contradicting the fact that 𝒜 ′ \mathcal{A}^{\prime} is separating.) It is thus sufficient for resolving this subcase to show that f ⁡ ( n − 1 2, y) ≥ n 2 f(\frac{n-1}{2},y)\geq\frac{n}{2} for 1 ≤ y ≤ n − 1 2 1\leq y\leq\frac{n-1}{2}, which follows from f ⁡ ( n − 1 2, y) f(\frac{n-1}{2},y) being greater than or equal to f ⁡ ( n 2 − 1, n 2 − 1) f(\frac{n}{2}-1,\frac{n}{2}-1) for all such y y.

2.) There exists B 3 B_{3} in 𝒜 < n / 2 \mathcal{A}_{<n/2} such that ( B 1 ∩ B 3 ≠ ∅) ∧ ( B 2 ∩ B 3 ≠ ∅) (B_{1}\cap B_{3}\neq\emptyset)\land(B_{2}\cap B_{3}\neq\emptyset):

If 𝒜 < n / 2 = { B 1, B 2, B 3 } \mathcal{A}_{<n/2}=\{B_{1},B_{2},B_{3}\}, then Avg ​ ( 𝒜 ^) ≥ 2 ​ n + 1 4 \textrm{Avg}(\hat{\mathcal{A}})\geq\frac{2n+1}{4} for 𝒜 ^ = { B 1, B 2, B 3, [n] } \hat{\mathcal{A}}=\{B_{1},B_{2},B_{3},[n]\}, making Avg ​ ( 𝒜) ≥ n 2 \textrm{Avg}(\mathcal{A})\geq\frac{n}{2}, as any member set of 𝒜 ∖ 𝒜 ^ \mathcal{A}\setminus\hat{\mathcal{A}} must have size greater than or equal to n 2 \frac{n}{2}. Else, { B 1, B 2, B 3 } ⊊ 𝒜 < n / 2 \{B_{1},B_{2},B_{3}\}\subsetneq\mathcal{A}_{<n/2}, and we consider the partition 𝒫 = { P 1, P 2, P 3, P 4 } \mathcal{P}=\{P_{1},P_{2},P_{3},P_{4}\} of B B, where P 1 = B 1 ∖ B 3 P_{1}=B_{1}\setminus B_{3}, P 2 = B 3 ∖ B 2 P_{2}=B_{3}\setminus B_{2}, P 3 = B 3 ∖ B 1 P_{3}=B_{3}\setminus B_{1}, and P 4 = B 2 ∖ B 3 P_{4}=B_{2}\setminus B_{3}. For any X ∈ 𝒜 < n / 2 ∖ { B 1, B 2, B 3 } X\in\mathcal{A}_{<n/2}\setminus\{B_{1},B_{2},B_{3}\} and i ∈ { 1, 2, 3, 4 } i\in\{1,2,3,4\}, we have that X ∩ P i ∈ { ∅, P i } X\cap P_{i}\in\{\emptyset,P_{i}\}. (If not, then there exists X ∈ 𝒜 < n / 2 ∖ { B 1, B 2, B 3 } X\in\mathcal{A}_{<n/2}\setminus\{B_{1},B_{2},B_{3}\} such that, without loss of generality, ∅ ⊊ X ∩ P 1 ⊊ P 1 \emptyset\subsetneq X\cap P_{1}\subsetneq P_{1}, and we have that B 2 ⊊ B 2 ∪ B 3 ⊊ B 2 ∪ B 3 ∪ X ⊊ B ⊊ [n] B_{2}\subsetneq B_{2}\cup B_{3}\subsetneq B_{2}\cup B_{3}\cup X\subsetneq B\subsetneq[n], which forms a chain in 𝒜 \mathcal{A} of size 5 5, contradicting h = 4 h=4.) Now, we observe that | ⋃ P ∈ 𝒫 ∖ { P i } P | ≥ n + 1 2 |\bigcup_{P\in\mathcal{P}\setminus\{P_{i}\}}P|\geq\frac{n+1}{2} for any i ∈ { 1, 2, 3, 4 } i\in\{1,2,3,4\}. We also observe that ( 𝒫 ∪ { ∅ }) ∩ ( 𝒜 < n / 2 ∖ { B 1, B 2, B 3 }) = ∅ (\mathcal{P}\cup\{\emptyset\})\cap(\mathcal{A}_{<n/2}\setminus\{B_{1},B_{2},B_{3}\})=\emptyset. (Otherwise, there exists X ∈ 𝒜 < n / 2 ∖ { B 1, B 2, B 3 } X\in\mathcal{A}_{<n/2}\setminus\{B_{1},B_{2},B_{3}\} such that either X = ∅ ⊊ B 1 ⊊ B 1 ∪ B 3 ⊊ B ⊊ [n] X=\emptyset\subsetneq B_{1}\subsetneq B_{1}\cup B_{3}\subsetneq B\subsetneq[n], or without loss of generality, X = P 1 ⊊ B 1 ⊊ B 1 ∪ B 3 ⊊ B ⊊ [n] X=P_{1}\subsetneq B_{1}\subsetneq B_{1}\cup B_{3}\subsetneq B\subsetneq[n], again contradicting h = 4 h=4.) It follows that any X ∈ 𝒜 < n / 2 X\in\mathcal{A}_{<n/2} must be the union of exactly two distinct member sets of 𝒫 \mathcal{P}. The maximum cardinality of 𝒜 < n / 2 \mathcal{A}_{<n/2} is thus ( | 𝒫 | 2) = 6 \binom{|\mathcal{P}|}{2}=6, as illustrated in Figure 2.2.

Figure 2.2: 𝒜 < n / 2 = { B 1, B 2, B 3, B 4, B 5, B 6 } \mathcal{A}_{<n/2}=\{B_{1},B_{2},B_{3},B_{4},B_{5},B_{6}\} has maximum size. B = [n − 1] B=[n-1] B 1 { B_{1}\ \Bigr\{ B 2 { B_{2}\ \Bigr\{ B 3 { B_{3}\ \Bigr\{ B 4 { B_{4}\ \Bigr\{ B 5 { B_{5}\ \Bigr\{ B 6 { B_{6}\ \Bigr\{ P 1 P_{1} P 2 P_{2} P 3 P_{3} P 4 P_{4}

Therefore, we have that | 𝒜 < n / 2 | ∈ { 4, 5, 6 } |\mathcal{A}_{<n/2}|\in\{4,5,6\}. We next establish Proposition D and, under this present assumption, Proposition E.

Proposition D. If N N is a positive integer, then for any P = { p 1, ⋯, p N } ∈ ℝ N P=\{p_{1},\cdots,p_{N}\}\in\mathbb{R}^{N} and k ∈ [N] k\in[N]:

 | ( N − 1 k − 1) ​ ∑ i ∈ [N] p i = ∑ S ∈ ( [N] k) ∑ j ∈ S p j ​. \binom{N-1}{k-1}\sum_{i\in[N]}p_{i}\ =\sum_{S\in\binom{[N]}{k}}\ \sum_{j\in S}p_{j}\textrm{.} |  |

Proof. For any m ∈ [N] m\in[N], there are ( N − 1 k − 1) \binom{N-1}{k-1} subsets of P P that contain both p m p_{m} and exactly k − 1 k-1 other elements of P P, making p m p_{m} occur on the right-hand side ( N − 1 k − 1) \binom{N-1}{k-1} times. The proposition then follows from adding these occurences together across all m ∈ [N] m\in[N].

We observe that setting P P from Proposition D equal to { 1 } N \{1\}^{N} yields the identity ( N − 1 k − 1) ​ N = ( N k) ​ k \binom{N-1}{k-1}N=\binom{N}{k}k.

Proposition E. For any four distinct A 1 A_{1}, A 2 A_{2}, A 3 A_{3}, and A 4 A_{4} in 𝒜 < n / 2 \mathcal{A}_{<n/2}, ∑ i = 1 4 | A i | ≥ 3 ​ n + 1 2 \sum_{i=1}^{4}|A_{i}|\geq\frac{3n+1}{2}.

Proof. There must exist two member sets from { A 1, A 2, A 3, A 4 } \{A_{1},A_{2},A_{3},A_{4}\} whose union is equal to [n − 1] [n-1]. Thus, we assume without loss of generality that A 1 = B 1 A_{1}=B_{1}, A 2 = B 2 A_{2}=B_{2}, and A 3 = B 3 = P 2 ∪ P 3 A_{3}=B_{3}=P_{2}\cup P_{3}. If A 4 = P 1 ∪ P 4 A_{4}=P_{1}\cup P_{4}, then | A 1 | + | A 2 | + | A 3 | + | A 4 | = 2 ​ n − 2 ≥ 3 ​ n + 1 2 |A_{1}|+|A_{2}|+|A_{3}|+|A_{4}|=2n-2\geq\frac{3n+1}{2}. Else, we have that A 4 = P 1 ∪ P 3 A_{4}=P_{1}\cup P_{3} and B 1 ⊊ A 3 ∪ A 4 B_{1}\subsetneq A_{3}\cup A_{4}, or otherwise that A 4 = P 2 ∪ P 4 A_{4}=P_{2}\cup P_{4} and B 2 ⊊ A 3 ∪ A 4 B_{2}\subsetneq A_{3}\cup A_{4}. In either case, A 3 ∩ A 4 ≠ ∅ A_{3}\cap A_{4}\neq\emptyset, and ( | A 1 | + | A 2 |) + ( | A 3 | + | A 4 |) ≥ ( n − 1) + ( n − 1 2 + 2) = 3 ​ n + 1 2 (|A_{1}|+|A_{2}|)+(|A_{3}|+|A_{4}|)\geq(n-1)+(\frac{n-1}{2}+2)=\frac{3n+1}{2}, completing the proof of Proposition E.

We let 𝒜 ^ = 𝒜 < n / 2 ∪ { Y, [n] } \hat{\mathcal{A}}=\mathcal{A}_{<n/2}\cup\{Y,[n]\} and address the three possible values of | 𝒜 < n / 2 | |\mathcal{A}_{<n/2}|:

(i) | 𝒜 < n / 2 | = 4 |\mathcal{A}_{<n/2}|=4: Let 𝒜 < n / 2 = { B 1, B 2, B 3, B 4 } \mathcal{A}_{<n/2}=\{B_{1},B_{2},B_{3},B_{4}\}. By Proposition E, we have that:

 | Avg ​ ( 𝒜 ^) = | Y | + n + ∑ i = 1 4 | B i | 6 ≥ 2 ​ n − 1 + 3 ​ n + 1 2 6 = 7 ​ n − 1 12 > n 2 ​. \textrm{Avg}(\hat{\mathcal{A}})=\frac{|Y|+n+\sum_{i=1}^{4}|B_{i}|}{6}\geq\frac{2n-1+\frac{3n+1}{2}}{6}=\frac{7n-1}{12}>\frac{n}{2}\textrm{.} |  |

(ii) | 𝒜 < n / 2 | = 5 |\mathcal{A}_{<n/2}|=5: Let 𝒜 < n / 2 = { B 1, B 2, B 3, B 4, B 5 } \mathcal{A}_{<n/2}=\{B_{1},B_{2},B_{3},B_{4},B_{5}\}. Applying Proposition D, we set N = 5 N=5, k = 4 k=4, and p i = | B i | p_{i}=|B_{i}| for each i ∈ { 1, 2, 3, 4, 5 } i\in\{1,2,3,4,5\} to obtain:

 | ( 4 3) ​ ∑ i = 1 5 | B i | = ∑ S ∈ ( [5] 4) ∑ j ∈ S | B j | ​. \binom{4}{3}\sum_{i=1}^{5}|B_{i}|\ =\ \sum_{S\in\binom{[5]}{4}}\ \sum_{j\in S}|B_{j}|\textrm{.} |  |

 | It follows by Proposition E that: ( 4 3) ∑ i = 1 5 | B i | ≥ ( 5 4) 3 ​ n + 1 2. \hskip-165.73721pt\textrm{It follows by Proposition E that: }\hskip 16.64505pt\binom{4}{3}\sum_{i=1}^{5}|B_{i}|\ \geq\ \binom{5}{4}\frac{3n+1}{2}\textrm{.} |  |

 | Thus, we have that: Avg ( 𝒜 ^) = | Y | + n + ∑ i = 1 5 | B i | 7 ≥ 2 ​ n − 1 + 15 ​ n + 5 8 7 = 31 ​ n − 3 56 > n 2. \hskip-80.37894pt\textrm{Thus, we have that:}\hskip 9.95863pt\textrm{Avg}(\hat{\mathcal{A}})=\frac{|Y|+n+\sum_{i=1}^{5}|B_{i}|}{7}\geq\frac{2n-1+\frac{15n+5}{8}}{7}=\frac{31n-3}{56}>\frac{n}{2}\textrm{.} |  |

(iii) | 𝒜 < n / 2 | = 6 |\mathcal{A}_{<n/2}|=6: Let 𝒜 < n / 2 = { B 1, B 2, B 3, B 4, B 5, B 6 } \mathcal{A}_{<n/2}=\{B_{1},B_{2},B_{3},B_{4},B_{5},B_{6}\}. We again apply Proposition D, this time setting N = 6 N=6, k = 4 k=4, and p i = | B i | p_{i}=|B_{i}| for each i ∈ { 1, 2, 3, 4, 5, 6 } i\in\{1,2,3,4,5,6\} to obtain:

 | ( 5 3) ​ ∑ i = 1 6 | B i | = ∑ S ∈ ( [6] 4) ∑ j ∈ S | B j | ​. \binom{5}{3}\sum_{i=1}^{6}|B_{i}|\ =\ \sum_{S\in\binom{[6]}{4}}\ \sum_{j\in S}|B_{j}|\textrm{.} |  |

 | By Proposition E, we have that: ( 5 3) ∑ i = 1 6 | B i | ≥ ( 6 4) 3 ​ n + 1 2. \hskip-163.60333pt\textrm{By Proposition E, we have that: }\hskip 18.49411pt\binom{5}{3}\sum_{i=1}^{6}|B_{i}|\ \geq\ \binom{6}{4}\frac{3n+1}{2}\textrm{.} |  |

 | As a result: Avg ( 𝒜 ^) = | Y | + n + ∑ i = 1 6 | B i | 8 ≥ 2 ​ n − 1 + 9 ​ n + 3 4 8 = 17 ​ n − 1 32 > n 2. \hskip-92.47145pt\textrm{As a result:}\hskip 32.00934pt\textrm{Avg}(\hat{\mathcal{A}})=\frac{|Y|+n+\sum_{i=1}^{6}|B_{i}|}{8}\geq\frac{2n-1+\frac{9n+3}{4}}{8}=\frac{17n-1}{32}>\frac{n}{2}\textrm{.} |  |

Thus, Avg ​ ( 𝒜 ^) ≥ n 2 \textrm{Avg}(\hat{\mathcal{A}})\geq\frac{n}{2} for any | 𝒜 < n / 2 | |\mathcal{A}_{<n/2}|. It follows that Avg ​ ( 𝒜) ≥ n 2 \textrm{Avg}(\mathcal{A})\geq\frac{n}{2}, as any member set of 𝒜 ∖ 𝒜 ^ \mathcal{A}\setminus\hat{\mathcal{A}} has size greater than or equal to n 2 \frac{n}{2}, proving the subcase | B | = n − 1 |B|=n-1 of Case 2.

This concludes the proof of Case 2, which then completes the overall proof of Theorem 2.1.

Corollary 2.2. For any separating union-closed family 𝒜 \mathcal{A} with h = 4 ≤ n h=4\leq n and 0 ≤ | ℬ | ≤ 2 0\leq|\mathcal{B}|\leq 2, there exists an element of [n] [n] that is in at least | 𝒜 | 2 \frac{|\mathcal{A}|}{2} member sets of 𝒜 \mathcal{A}.

Proof. If not, then there is a separating union-closed family 𝒜 \mathcal{A} with h = 4 ≤ n h=4\leq n and 0 ≤ | ℬ | ≤ 2 0\leq|\mathcal{B}|\leq 2 such that the family 𝒜 { x } = { A ∈ 𝒜 | x ∈ A } \mathcal{A}_{\{x\}}=\{A\in\mathcal{A}\ |\ x\in A\} has size less than | 𝒜 | 2 \frac{|\mathcal{A}|}{2} for every x ∈ [n] x\in[n]. It follows that Avg ​ ( 𝒜) = ∑ A ∈ 𝒜 | A | | 𝒜 | = ∑ x ∈ [n] | 𝒜 { x } | | 𝒜 | < n ⁡ ( | 𝒜 | / 2) | 𝒜 | = n 2 \textrm{Avg}(\mathcal{A})=\frac{\sum_{A\in\mathcal{A}}|A|}{|\mathcal{A}|}=\frac{\sum_{x\in[n]}|\mathcal{A}_{\{x\}}|}{|\mathcal{A}|}<\frac{n(|\mathcal{A}|/2)}{|\mathcal{A}|}=\frac{n}{2}. This contradicts Theorem 2.1, which states that Avg ​ ( 𝒜) ≥ n 2 \textrm{Avg}(\mathcal{A})\geq\frac{n}{2}.

## 3. Limitation of averaging for larger values of h h

In this section, Theorem 3.2 demonstrates that the technique of averaging member set sizes of separating union-closed families cannot be used to prove Conjecture 1.1 for any h ≥ 5 h\geq 5. We first establish Lemma 3.1.

Lemma 3.1. For any integer n ≥ 9 n\geq 9, there exists a separating union-closed family 𝒜 \mathcal{A} with h = 5 h=5 and | ℬ | = 1 |\mathcal{B}|=1 such that:

 | Avg ​ ( 𝒜) = ∑ A ∈ 𝒜 | A | | 𝒜 | < n 2 ​. \textrm{Avg}(\mathcal{A})=\frac{\sum_{A\in\mathcal{A}}|A|}{|\mathcal{A}|}<\frac{n}{2}\textrm{.} |  |

Proof. Consider 𝒜 ∗ \mathcal{A}^{*} from Figure 2.1. For any integer n ≥ 9 n\geq 9, we construct a union-closed family 𝒜 ∗ ⁣ ∗ \mathcal{A}^{**} with base set [n] [n], height h = 5 h=5, and | ℬ ⁡ ( 𝒜 ∗ ⁣ ∗) | = 1 |\mathcal{B}(\mathcal{A}^{**})|=1 as follows:

 | 𝒜 ∗ ⁣ ∗ = 𝒜 ∗ ∪ ( [⌈ n 2 ⌉ − 1] ⌈ n 2 ⌉ − 3) = { [n], [⌈ n 2 ⌉ − 1] } ∪ { [n] ∖ { x } | x ∈ [n] ∖ [⌈ n 2 ⌉] } ∪ ⋃ i = 2 3 ( [⌈ n 2 ⌉ − 1] ⌈ n 2 ⌉ − i). \mathcal{A}^{**}=\mathcal{A}^{*}\cup\binom{[\lceil\frac{n}{2}\rceil-1]}{\lceil\frac{n}{2}\rceil-3}=\ \Bigr\{[n],\Bigr[\Bigr\lceil\frac{n}{2}\Bigr\rceil-1\Bigr]\Bigr\}\ \ \cup\ \ \Bigr\{[n]\setminus\{x\}\ \Bigr|\ x\in\ [n]\ \setminus\ \Bigr[\Bigr\lceil\frac{n}{2}\Bigr\rceil\Bigr]\Bigr\}\ \ \cup\ \ \bigcup_{i=2}^{3}\binom{[\lceil\frac{n}{2}\rceil-1]}{\lceil\frac{n}{2}\rceil-i}\textrm{.} |  |

𝒜 ∗ ⁣ ∗ \mathcal{A}^{**} is separating because it is a superfamily of 𝒜 ∗ \mathcal{A}^{*}, which itself is a separating union-closed family with b ⁡ ( 𝒜 ∗) = b ⁡ ( 𝒜 ∗ ⁣ ∗) = [n] b(\mathcal{A}^{*})=b(\mathcal{A}^{**})=[n]. We compute the average size of a member set from 𝒜 ∗ ⁣ ∗ \mathcal{A}^{**} to be:

 | Avg ​ ( 𝒜 ∗ ⁣ ∗) = n + ( ⌈ n 2 ⌉ − 1) + ( n − ⌈ n 2 ⌉) ( n − 1) + ( ⌈ n 2 ⌉ − 1) ( ⌈ n 2 ⌉ − 2) + 1 2 ( ⌈ n 2 ⌉ − 1) ( ⌈ n 2 ⌉ − 2) ( ⌈ n 2 ⌉ − 3) 2 + ( n − ⌈ n 2 ⌉) + ( ⌈ n 2 ⌉ − 1) + 1 2 ( ⌈ n 2 ⌉ − 1) ( ⌈ n 2 ⌉ − 2) ​. \textrm{Avg}(\mathcal{A}^{**})=\frac{n+\Bigr(\lceil\frac{n}{2}\rceil-1\Bigr)+\Bigr(n-\lceil\frac{n}{2}\rceil\Bigr)\Bigr(n-1\Bigr)+\Bigr(\lceil\frac{n}{2}\rceil-1\Bigr)\Bigr(\lceil\frac{n}{2}\rceil-2\Bigr)+\frac{1}{2}\Bigr(\lceil\frac{n}{2}\rceil-1\Bigr)\Bigr(\lceil\frac{n}{2}\rceil-2\Bigr)\Bigr(\lceil\frac{n}{2}\rceil-3\Bigr)}{2+\Bigr(n-\lceil\frac{n}{2}\rceil\Bigr)+\Bigr(\lceil\frac{n}{2}\rceil-1\Bigr)+\frac{1}{2}\Bigr(\lceil\frac{n}{2}\rceil-1\Bigr)\Bigr(\lceil\frac{n}{2}\rceil-2\Bigr)}\textrm{.} |  |

Thus, Avg ​ ( 𝒜 ∗ ⁣ ∗) \textrm{Avg}(\mathcal{A}^{**}) is equal to n 3 + 36 ​ n − 32 2 ​ n 2 + 4 ​ n + 32 \frac{n^{3}+36n-32}{2n^{2}+4n+32} when n n is even, and equal to n 3 + 3 ​ n 2 + 15 ​ n − 3 2 ​ n 2 + 8 ​ n + 22 \frac{n^{3}+3n^{2}+15n-3}{2n^{2}+8n+22} when n n is odd. In either case, Avg ​ ( 𝒜 ∗ ⁣ ∗) < n 2 \textrm{Avg}(\mathcal{A}^{**})<\frac{n}{2}, completing the proof of Lemma 3.1.

For proving Theorem 3.2, we let [0] = ∅ [0]=\emptyset and [c, d] = { i ∈ ℤ | c ≤ i ≤ d } [c,d]=\{i\in\mathbb{Z}\ |\ c\leq i\leq d\} for any two integers c c and d d.

Theorem 3.2. For any integer n ≥ 11 n\geq 11 and k ∈ [5, n + 1] k\in[5,n+1], there exists a separating union-closed family 𝒜 ( k) \mathcal{A}^{(k)} with base set [n] [n] and height h = k h=k, as well as | ℬ ⁡ ( 𝒜 ( k)) | = 1 |\mathcal{B}(\mathcal{A}^{(k)})|=1, such that:

 | Avg ​ ( 𝒜 ( k)) = ∑ A ∈ 𝒜 ( k) | A | | 𝒜 ( k) | < n 2 ​. \textrm{Avg}(\mathcal{A}^{(k)})=\frac{\sum_{A\in\mathcal{A}^{(k)}}|A|}{|\mathcal{A}^{(k)}|}<\frac{n}{2}\textrm{.} |  |

Proof. For any integer n ≥ 11 n\geq 11, we set 𝒜 ( 5) = 𝒜 ∗ ⁣ ∗ \mathcal{A}^{(5)}=\mathcal{A}^{**} and Δ = n − 2 ​ ⌈ n 2 ⌉ + 2 \Delta=n-2\lceil\frac{n}{2}\rceil+2, and establish a conditional recurrence relation for k ∈ [5, n] k\in[5,n] as follows:

 | 𝒜 ( k + 1) = 𝒜 ( k) ∪ { { [⌈ n 2 ⌉ + k − 5] } if k ∈ [5, 5 + Δ] { [⌈ n 2 ⌉ − k + 2 − Δ 2] } if k ∈ { 2 i + Δ | i ∈ [3, n − Δ 2] } { [⌈ n 2 ⌉ + k − 5 + Δ 2] } if k ∈ { 2 i + Δ + 1 | i ∈ [3, n − Δ − 2 2] } ​. \mathcal{A}^{(k+1)}=\mathcal{A}^{(k)}\ \cup\ \begin{cases}\Bigr\{\Bigr[\lceil\frac{n}{2}\rceil+k-5\Bigr]\Bigr\}&\textrm{if }k\in\ \Bigr[5,5+\Delta\Bigr]\\[5.0pt] \Bigr\{\Bigr[\lceil\frac{n}{2}\rceil-\frac{k+2-\Delta}{2}\Bigr]\Bigr\}&\textrm{if }k\in\ \Bigr\{2i+\Delta\ |\ i\in\ \Bigr[3,\frac{n-\Delta}{2}\Bigr]\Bigr\}\\[5.0pt] \Bigr\{\Bigr[\lceil\frac{n}{2}\rceil+\frac{k-5+\Delta}{2}\Bigr]\Bigr\}&\textrm{if }k\in\ \Bigr\{2i+\Delta+1\ |\ i\in\ \Bigr[3,\frac{n-\Delta-2}{2}\Bigr]\Bigr\}\end{cases}\textrm{.} |  |

In the same way that 𝒜 ∗ ⁣ ∗ \mathcal{A}^{**} was separating in the proof of Lemma 3.1, 𝒜 ( k) \mathcal{A}^{(k)} is separating because it is a superfamily of 𝒜 ∗ \mathcal{A}^{*}, which itself is a separating family with the same base set.

For k ∈ [6, 6 + Δ] k\in[6,6+\Delta], we have that 𝒜 ( k) = 𝒜 ∗ ⁣ ∗ ∪ ⋃ i = 5 k − 1 { [⌈ n 2 ⌉ + i − 5] } \mathcal{A}^{(k)}=\mathcal{A}^{**}\cup\ \bigcup_{i=5}^{k-1}\{[\lceil\frac{n}{2}\rceil+i-5]\}. Thus, showing that Avg ​ ( 𝒜 ( 6 + Δ)) < n 2 \textrm{Avg}(\mathcal{A}^{(6+\Delta)})<\frac{n}{2} is sufficient for implying that Avg ​ ( 𝒜 ( k)) < n 2 \textrm{Avg}(\mathcal{A}^{(k)})<\frac{n}{2} for all such k k. We compute Avg ​ ( 𝒜 ( 6 + Δ)) \textrm{Avg}(\mathcal{A}^{(6+\Delta)}) to be n 3 + 60 ​ n + 16 2 ​ n 2 + 4 ​ n + 80 \frac{n^{3}+60n+16}{2n^{2}+4n+80} when n n is even and n 3 + 3 ​ n 2 + 31 ​ n + 29 2 ​ n 2 + 8 ​ n + 54 \frac{n^{3}+3n^{2}+31n+29}{2n^{2}+8n+54} when n n is odd, in both cases less than n 2 \frac{n}{2}.

For k ∈ { 2 ​ i + Δ | i ∈ [3, n − Δ − 2 2] } k\in\{2i+\Delta\ |\ i\in[3,\frac{n-\Delta-2}{2}]\}, we have that 𝒜 ( k + 1) = 𝒜 ( k) ∪ { [⌈ n 2 ⌉ − k + 2 − Δ 2] } \mathcal{A}^{(k+1)}=\mathcal{A}^{(k)}\ \cup\ \{[\lceil\frac{n}{2}\rceil-\frac{k+2-\Delta}{2}]\} and 𝒜 ( k + 2) = 𝒜 ( k) ∪ { [⌈ n 2 ⌉ − k + 2 − Δ 2], [⌈ n 2 ⌉ + k − 5 + Δ 2] } \mathcal{A}^{(k+2)}=\mathcal{A}^{(k)}\ \cup\ \{[\lceil\frac{n}{2}\rceil-\frac{k+2-\Delta}{2}],[\lceil\frac{n}{2}\rceil+\frac{k-5+\Delta}{2}]\}. Therefore, 𝒜 ( k + 1) = 𝒜 ( k) ∪ 𝒞 1 \mathcal{A}^{(k+1)}=\mathcal{A}^{(k)}\cup\ \mathcal{C}_{1} and 𝒜 ( k + 2) = 𝒜 ( k) ∪ 𝒞 2 \mathcal{A}^{(k+2)}=\mathcal{A}^{(k)}\cup\ \mathcal{C}_{2}, where 𝒞 1 \mathcal{C}_{1} and 𝒞 2 \mathcal{C}_{2} are families such that Avg ​ ( 𝒞 1) < n 2 \textrm{Avg}(\mathcal{C}_{1})<\frac{n}{2} and Avg ​ ( 𝒞 2) < n 2 \textrm{Avg}(\mathcal{C}_{2})<\frac{n}{2}. Hence, Avg ​ ( 𝒜 ( k)) < n 2 \textrm{Avg}(\mathcal{A}^{(k)})<\frac{n}{2} implies that both Avg ​ ( 𝒜 ( k + 1)) < n 2 \textrm{Avg}(\mathcal{A}^{(k+1)})<\frac{n}{2} and Avg ​ ( 𝒜 ( k + 2)) < n 2 \textrm{Avg}(\mathcal{A}^{(k+2)})<\frac{n}{2}. Noting that Avg ​ ( 𝒜 ( 6 + Δ)) < n 2 \textrm{Avg}(\mathcal{A}^{(6+\Delta)})<\frac{n}{2}, it follows by induction that Avg ​ ( 𝒜 ( k)) < n 2 \textrm{Avg}(\mathcal{A}^{(k)})<\frac{n}{2} for all k ∈ [7 + Δ, n] k\in[7+\Delta,n]. Finally, 𝒜 ( n + 1) = 𝒜 ( n) ∪ { ∅ } \mathcal{A}^{(n+1)}=\mathcal{A}^{(n)}\cup\{\emptyset\} and Avg ​ ( 𝒜 ( n)) < n 2 \textrm{Avg}(\mathcal{A}^{(n)})<\frac{n}{2} together imply that Avg ​ ( 𝒜 ( n + 1)) < n 2 \textrm{Avg}(\mathcal{A}^{(n+1)})<\frac{n}{2}, completing the proof of Theorem 3.2.

## 4. Considering 3 ≤ | ℬ | ≤ 4 3\leq|\mathcal{B}|\leq 4 for h = 4 h=4

It remains to consider the technique of averaging for when 3 ≤ | ℬ | ≤ 4 3\leq|\mathcal{B}|\leq 4 (where h h is again equal to 4 4). Extending Theorem 2.1 by these final two values of | ℬ | |\mathcal{B}| would imply Conjecture 1.1 for h = 4 h=4 (and more generally would conclude proof of Avg ​ ( 𝒜) ≥ n / 2 \textrm{Avg}(\mathcal{A})\geq n/2 for all separating union-closed families with h = 4 h=4). We prove some respective propositions for | ℬ | = 3 |\mathcal{B}|=3 and | ℬ | = 4 |\mathcal{B}|=4.

### The case | ℬ | = 3 |\mathcal{B}|=3

We establish Propositions F, G, H, and I under the assumption that | ℬ | = 3 |\mathcal{B}|=3. Let ℬ = { B 1, B 2, B 3 } \mathcal{B}=\{B_{1},B_{2},B_{3}\}, and for i ∈ { 1, 2, 3 } i\in\{1,2,3\}, let k i k_{i} be the number of elements from [n] [n] that are contained in exactly i i member sets of ℬ \mathcal{B}.

Proposition F. | B | ∈ { n − 1, n } |B|\in\{n-1,n\}.

Proof. Otherwise, | B | ≤ n − 2 |B|\leq n-2, and B 1 ⊊ B 1 ∪ B 2 ⊊ B ⊊ [n] B_{1}\subsetneq B_{1}\cup B_{2}\subsetneq B\subsetneq[n] contradicts Lemma 1.3.

Proposition G. If | B | = n |B|=n and A ∈ 𝒜 < n / 2 ∖ ℬ A\in\mathcal{A}_{<n/2}\setminus\mathcal{B}, then ⋃ i = 1 3 irr ℬ ​ ( B i) ⊈ A \bigcup_{i=1}^{3}\texttt{irr}_{\mathcal{B}}(B_{i})\not\subseteq A.

Proof. We let | B | = n |B|=n, and assume that there exists A ∈ 𝒜 < n / 2 ∖ ℬ A\in\mathcal{A}_{<n/2}\setminus\mathcal{B} such that ⋃ i = 1 3 irr ℬ ​ ( B i) ⊆ A \bigcup_{i=1}^{3}\texttt{irr}_{\mathcal{B}}(B_{i})\subseteq A. By double counting, we have that ∑ i = 1 3 i ​ k i = ∑ i = 1 3 | B i | \sum_{i=1}^{3}ik_{i}=\sum_{i=1}^{3}|B_{i}|. We further note that k 1 + 2 ​ ( k 2 + k 3) ≤ ∑ i = 1 3 i ​ k i k_{1}+2(k_{2}+k_{3})\leq\sum_{i=1}^{3}ik_{i}, k 2 + k 3 = n − k 1 k_{2}+k_{3}=n-k_{1}, and | B i | ≤ n − 1 2 |B_{i}|\leq\frac{n-1}{2} for every i ∈ { 1, 2, 3 } i\in\{1,2,3\}. Consequently, k 1 + 2 ​ ( n − k 1) ≤ 3 ​ ( n − 1 2) k_{1}+2(n-k_{1})\leq 3(\frac{n-1}{2}), which implies that k 1 ≥ n + 3 2 k_{1}\geq\frac{n+3}{2}. Then k 1 = ∑ i = 1 3 | irr ℬ ​ ( B i) | = | ⋃ i = 1 3 irr ℬ ​ ( B i) | k_{1}=\sum_{i=1}^{3}|\texttt{irr}_{\mathcal{B}}(B_{i})|=\ |\bigcup_{i=1}^{3}\texttt{irr}_{\mathcal{B}}(B_{i})| implies that | A | ≥ n + 3 2 |A|\geq\frac{n+3}{2}, which contradicts A ∈ 𝒜 < n / 2 A\in\mathcal{A}_{<n/2}. This concludes the proof of Proposition G.

Proposition H. If | B | = n |B|=n, then for all A ∈ 𝒜 < n / 2 A\in\mathcal{A}_{<n/2} and i ∈ { 1, 2, 3 } i\in\{1,2,3\}, | irr ℬ ​ ( B i) | > 1 |\texttt{irr}_{\mathcal{B}}(B_{i})|>1 implies that | A ∩ irr ℬ ​ ( B i) | ∈ { 0, | irr ℬ ​ ( B i) | − 1, | irr ℬ ​ ( B i) | } |A\cap\texttt{irr}_{\mathcal{B}}(B_{i})|\in\{0,|\texttt{irr}_{\mathcal{B}}(B_{i})|-1,|\texttt{irr}_{\mathcal{B}}(B_{i})|\}.

Proof. Assume otherwise, i.e. that | B | = n |B|=n and there exists A ∈ 𝒜 < n / 2 A\in\mathcal{A}_{<n/2} and i ∈ { 1, 2, 3 } i\in\{1,2,3\} such that both | irr ℬ ​ ( B i) | > 2 |\texttt{irr}_{\mathcal{B}}(B_{i})|>2 and 1 ≤ | A ∩ irr ℬ ​ ( B i) | ≤ | irr ℬ ​ ( B i) | − 2 1\leq|A\cap\texttt{irr}_{\mathcal{B}}(B_{i})|\leq|\texttt{irr}_{\mathcal{B}}(B_{i})|-2. Without loss of generality, let i = 1 i=1. Then B 2 ⊊ B 2 ∪ B 3 ⊊ B 2 ∪ B 3 ∪ A ⊊ [n] B_{2}\subsetneq B_{2}\cup B_{3}\subsetneq B_{2}\cup B_{3}\cup A\subsetneq[n] with | B 2 ∪ B 3 ∪ A | < n − 1 |B_{2}\cup B_{3}\cup A|<n-1. This contradicts Lemma 1.3, completing the proof of Proposition H.

Proposition I. If | B | = n − 1 |B|=n-1 and A ∈ 𝒜 < n / 2 ∖ ℬ A\in\mathcal{A}_{<n/2}\setminus\mathcal{B}, then either A = ⋃ i = 1 3 irr ℬ ​ ( B i) A=\bigcup_{i=1}^{3}\texttt{irr}_{\mathcal{B}}(B_{i}) or A A satisfies exactly one of the following three conditions:

(i) A ∩ irr ℬ ​ ( B 1) = ∅ ∧ ( B 2 ∪ B 3) ∖ ( B 2 ∩ B 3) ⊆ A \hskip 2.48944ptA\cap\texttt{irr}_{\mathcal{B}}(B_{1})=\emptyset\ \land\ (B_{2}\cup B_{3})\setminus(B_{2}\cap B_{3})\subseteq A;

(ii) A ∩ irr ℬ ​ ( B 2) = ∅ ∧ ( B 1 ∪ B 3) ∖ ( B 1 ∩ B 3) ⊆ A A\cap\texttt{irr}_{\mathcal{B}}(B_{2})=\emptyset\ \land\ (B_{1}\cup B_{3})\setminus(B_{1}\cap B_{3})\subseteq A;

(iii) A ∩ irr ℬ ​ ( B 3) = ∅ ∧ ( B 1 ∪ B 2) ∖ ( B 1 ∩ B 2) ⊆ A \hskip-2.13387ptA\cap\texttt{irr}_{\mathcal{B}}(B_{3})=\emptyset\ \land\ (B_{1}\cup B_{2})\setminus(B_{1}\cap B_{2})\subseteq A.

Proof. We let | B | = n − 1 |B|=n-1 and consider any A ∈ 𝒜 n / 2 ∖ ℬ A\in\mathcal{A}_{n/2}\setminus\mathcal{B}. For every i ∈ { 1, 2, 3 } i\in\{1,2,3\}, we have that irr ℬ ​ ( B i) ∩ A ∈ { ∅, irr ℬ ​ ( B i) } \texttt{irr}_{\mathcal{B}}(B_{i})\cap A\in\{\emptyset,\texttt{irr}_{\mathcal{B}}(B_{i})\}. (Otherwise, without loss of generality ∅ ⊊ irr ℬ ​ ( B 1) ∩ A ⊊ irr ℬ ​ ( B 1) \emptyset\subsetneq\texttt{irr}_{\mathcal{B}}(B_{1})\cap A\subsetneq\texttt{irr}_{\mathcal{B}}(B_{1}), which implies that B 2 ⊊ B 2 ∪ B 3 ⊊ B 2 ∪ B 3 ∪ A ⊊ B 2 ∪ B 3 ∪ A ∪ B 1 ⊊ [n] B_{2}\subsetneq B_{2}\cup B_{3}\subsetneq B_{2}\cup B_{3}\cup A\subsetneq B_{2}\cup B_{3}\cup A\cup B_{1}\subsetneq[n], contradicting h = 4 h=4.)

- •

First, we assume that irr ℬ ​ ( B i) ⊆ A \texttt{irr}_{\mathcal{B}}(B_{i})\subseteq A for all i ∈ { 1, 2, 3 } i\in\{1,2,3\}. Applying the double counting argument from the proof of Proposition G to this case, we have that k 1 + 2 ​ ( ( n − 1) − k 1) ≤ 3 ​ ( n − 1 2) k_{1}+2((n-1)-k_{1})\leq 3(\frac{n-1}{2}), which implies that k 1 ≥ n − 1 2 k_{1}\geq\frac{n-1}{2}. Noting that k 1 = ∑ i = 1 3 | irr ℬ ​ ( B i) | = | ⋃ i = 1 3 irr ℬ ​ ( B i) | k_{1}=\sum_{i=1}^{3}|\texttt{irr}_{\mathcal{B}}(B_{i})|=\ |\bigcup_{i=1}^{3}\texttt{irr}_{\mathcal{B}}(B_{i})|, we observe that if A ∖ ⋃ i = 1 3 irr ℬ ​ ( B i) ≠ ∅ A\setminus\bigcup_{i=1}^{3}\texttt{irr}_{\mathcal{B}}(B_{i})\neq\emptyset, then | A | > n 2 |A|>\frac{n}{2}, which contradicts the fact that A ∈ 𝒜 < n / 2 A\in\mathcal{A}_{<n/2}. Therefore, A = ⋃ i = 1 3 irr ℬ ​ ( B i) A=\bigcup_{i=1}^{3}\texttt{irr}_{\mathcal{B}}(B_{i}).

- •

Next, we assume that that there is no i ∈ { 1, 2, 3 } i\in\{1,2,3\} such that irr ℬ ​ ( B i) ⊆ A \texttt{irr}_{\mathcal{B}}(B_{i})\subseteq A. In this case, A ⊊ A ∪ B 1 ⊊ A ∪ B 1 ∪ B 2 ⊊ A ∪ B 1 ∪ B 2 ∪ B 3 ⊊ [n] A\subsetneq A\cup B_{1}\subsetneq A\cup B_{1}\cup B_{2}\subsetneq A\cup B_{1}\cup B_{2}\cup B_{3}\subsetneq[n], contradicting h = 4 h=4.

- •

Now, we assume that that there exists exactly one i ∈ { 1, 2, 3 } i\in\{1,2,3\} such that irr ℬ ​ ( B i) ⊆ A \texttt{irr}_{\mathcal{B}}(B_{i})\subseteq A. Without loss of generality, let i = 1 i=1. Then ( B 1 ⊊ A ∪ B 1 ⊊ A ∪ B 1 ∪ B 2 ⊊ B ⊊ [n]) ∨ ( A ⊊ B 1 ⊊ B 1 ∪ B 2 ⊊ B ⊊ [n]) (B_{1}\subsetneq A\cup B_{1}\subsetneq A\cup B_{1}\cup B_{2}\subsetneq B\subsetneq[n])\ \lor\ (A\subsetneq B_{1}\subsetneq B_{1}\cup B_{2}\subsetneq B\subsetneq[n]), again a contradiction with h = 4 h=4.

- •

Finally, we assume that there exist exactly two distinct elements i i and j j in { 1, 2, 3 } \{1,2,3\} such that irr ℬ ​ ( B i) ⊆ A \texttt{irr}_{\mathcal{B}}(B_{i})\subseteq A and irr ℬ ​ ( B j) ⊆ A \texttt{irr}_{\mathcal{B}}(B_{j})\subseteq A. Denote by k k the unique element from the set { 1, 2, 3 } ∖ { i, j } \{1,2,3\}\setminus\{i,j\}. If ( B i ∩ B k) ∖ B j ⊈ A (B_{i}\cap B_{k})\setminus B_{j}\not\subseteq A, then B j ⊊ B j ∪ A ⊊ B i ∪ B j ∪ A ⊊ B ⊊ [n] B_{j}\subsetneq B_{j}\cup A\subsetneq B_{i}\cup B_{j}\cup A\subsetneq B\subsetneq[n]. Similarly, if ( B j ∩ B k) ∖ B i ⊈ A (B_{j}\cap B_{k})\setminus B_{i}\not\subseteq A, then B i ⊊ B i ∪ A ⊊ B i ∪ B j ∪ A ⊊ B ⊊ [n] B_{i}\subsetneq B_{i}\cup A\subsetneq B_{i}\cup B_{j}\cup A\subsetneq B\subsetneq[n]. In either case, there exists a chain of size 5 5 in 𝒜 \mathcal{A}, contradicting h = 4 h=4. It follows that ( B i ∩ B k) ∖ B j ⊆ A (B_{i}\cap B_{k})\setminus B_{j}\subseteq A and ( B j ∩ B k) ∖ B i ⊆ A (B_{j}\cap B_{k})\setminus B_{i}\subseteq A (as well as irr ℬ ​ ( B i) ⊆ A \texttt{irr}_{\mathcal{B}}(B_{i})\subseteq A and irr ℬ ​ ( B j) ⊆ A \texttt{irr}_{\mathcal{B}}(B_{j})\subseteq A), as illustrated in Figure 4.1.

Hence, if A ≠ ⋃ i = 1 3 irr ℬ ​ ( B i) A\neq\bigcup_{i=1}^{3}\texttt{irr}_{\mathcal{B}}(B_{i}), then A A satisfies exactly one of (i), (ii), or (iii). This completes the proof of Proposition I.

Figure 4.1: If | ℬ | = 3 |\mathcal{B}|=3 and | B | = n − 1 |B|=n-1, then any A ∈ 𝒜 < n / 2 ∖ ℬ A\in\mathcal{A}_{<n/2}\setminus\mathcal{B} such that A ≠ ⋃ i = 1 3 irr ℬ ​ ( B i) A\neq\bigcup_{i=1}^{3}\texttt{irr}_{\mathcal{B}}(B_{i}) must have one of three forms.

(i) irr ℬ ​ ( B 1) \texttt{irr}_{\mathcal{B}}(B_{1}) irr ℬ ​ ( B 2) \texttt{irr}_{\mathcal{B}}(B_{2}) irr ℬ ​ ( B 3) \texttt{irr}_{\mathcal{B}}(B_{3}) ∴ \therefore ∴ \therefore B 1 B_{1} B 2 B_{2} B 3 B_{3}

(ii) irr ℬ ​ ( B 1) \texttt{irr}_{\mathcal{B}}(B_{1}) irr ℬ ​ ( B 2) \texttt{irr}_{\mathcal{B}}(B_{2}) irr ℬ ​ ( B 3) \texttt{irr}_{\mathcal{B}}(B_{3}) ∴ \therefore ∴ \therefore B 1 B_{1} B 2 B_{2} B 3 B_{3}

(iii) irr ℬ ​ ( B 1) \texttt{irr}_{\mathcal{B}}(B_{1}) irr ℬ ​ ( B 2) \texttt{irr}_{\mathcal{B}}(B_{2}) irr ℬ ​ ( B 3) \texttt{irr}_{\mathcal{B}}(B_{3}) ∴ \therefore ∴ \therefore B 1 B_{1} B 2 B_{2} B 3 B_{3}

∗ {}^{*}\ Gray indicates that the region is a subset of A A.

∗∗ Three dots indicate that part of the region may be a subset of A A.

### The case | ℬ | = 4 |\mathcal{B}|=4

We conclude this study with propositions valid for | ℬ | = 4 |\mathcal{B}|=4, culminating in Theorem 4.1.

Let ℬ = { B 1, B 2, B 3, B 4 } \mathcal{B}=\{B_{1},B_{2},B_{3},B_{4}\}.

Proposition J. | B | = n |B|=n.

Proof. If not, then B 1 ⊊ B 1 ∪ B 2 ⊊ B 1 ∪ B 2 ∪ B 3 ⊊ B ⊊ [n] B_{1}\subsetneq B_{1}\cup B_{2}\subsetneq B_{1}\cup B_{2}\cup B_{3}\subsetneq B\subsetneq[n], which contradicts h = 4 h=4.

Proposition K. For each i ∈ { 1, 2, 3, 4 } i\in\{1,2,3,4\}, | irr ℬ ​ ( B i) | = 1 |\texttt{irr}_{\mathcal{B}}(B_{i})|=1.

Proof. Otherwise, let | irr ℬ ​ ( B 1) | > 1 |\texttt{irr}_{\mathcal{B}}(B_{1})|>1 without loss of generality. It follows that B 2 ⊊ B 2 ∪ B 3 ⊊ B 2 ∪ B 3 ∪ B 4 ⊊ [n] B_{2}\subsetneq B_{2}\cup B_{3}\subsetneq B_{2}\cup B_{3}\cup B_{4}\subsetneq[n] with | B 2 ∪ B 3 ∪ B 4 | < n − 1 |B_{2}\cup B_{3}\cup B_{4}|<n-1, contradicting Lemma 1.3.

Proposition L. (i) If n n is even, then ∑ i = 1 4 | B i | = 2 ​ n − 4 \sum_{i=1}^{4}|B_{i}|=2n-4 and | B i | = n − 2 2 |B_{i}|=\frac{n-2}{2} for all i ∈ { 1, 2, 3, 4 } i\in\{1,2,3,4\}. (ii) If n n is odd, then 2 ​ n − 4 ≤ ∑ i = 1 4 | B i | ≤ 2 ​ n − 2 2n-4\leq\sum_{i=1}^{4}|B_{i}|\leq 2n-2 and | B i | ≥ n − 5 2 |B_{i}|\geq\frac{n-5}{2} for all i ∈ { 1, 2, 3, 4 } i\in\{1,2,3,4\}. Further, if there exists i ∈ { 1, 2, 3, 4 } i\in\{1,2,3,4\} such that | B i | = n − 5 2 |B_{i}|=\frac{n-5}{2}, then | B j | = n − 1 2 |B_{j}|=\frac{n-1}{2} for all j ∈ { 1, 2, 3, 4 } ∖ { i } j\in\{1,2,3,4\}\setminus\{i\}.

Proof. For i ∈ { 1, 2, 3, 4 } i\in\{1,2,3,4\}, let k i k_{i} be the number of elements from [n] [n] that are contained in exactly i i member sets of ℬ \mathcal{B}. We observe that k 1 = 4 k_{1}=4 by Proposition K, and that n − k 1 = k 2 + k 3 + k 4 n-k_{1}=k_{2}+k_{3}+k_{4}. Additionally, double counting gives ∑ i = 1 4 i ​ k i = ∑ i = 1 4 | B i | \sum_{i=1}^{4}ik_{i}=\sum_{i=1}^{4}|B_{i}|. Therefore, we have that k 1 + 2 ​ ( k 2 + k 3 + k 4) = 2 ​ n − 4 ≤ ∑ i = 1 4 | B i | k_{1}+2(k_{2}+k_{3}+k_{4})=2n-4\leq\sum_{i=1}^{4}|B_{i}|.

For part (i), we assume that n n is even. Then ∑ i = 1 4 | B i | ≤ 4 ​ ( n − 2 2) = 2 ​ n − 4 \sum_{i=1}^{4}|B_{i}|\leq 4(\frac{n-2}{2})=2n-4, which together with the above inequality 2 ​ n − 4 ≤ ∑ i = 1 4 | B i | 2n-4\leq\sum_{i=1}^{4}|B_{i}| implies that ∑ i = 1 4 | B i | = 2 ​ n − 4 \sum_{i=1}^{4}|B_{i}|=2n-4. Because n n is even, | B i | ≤ n − 2 2 |B_{i}|\leq\frac{n-2}{2} for every i ∈ { 1, 2, 3, 4 } i\in\{1,2,3,4\}. Together with ∑ i = 1 4 | B i | = 2 ​ n − 4 \sum_{i=1}^{4}|B_{i}|=2n-4, this then implies that | B i | = n − 2 2 |B_{i}|=\frac{n-2}{2} for every i ∈ { 1, 2, 3, 4 } i\in\{1,2,3,4\}.

For part (ii), we assume that n n is odd. Then ∑ i = 1 4 | B i | ≤ 4 ​ ( n − 1 2) = 2 ​ n − 2 \sum_{i=1}^{4}|B_{i}|\leq 4(\frac{n-1}{2})=2n-2, so in this case we have that 2 ​ n − 4 ≤ ∑ i = 1 4 | B i | ≤ 2 ​ n − 2 2n-4\leq\sum_{i=1}^{4}|B_{i}|\leq 2n-2. It follows that for every i ∈ { 1, 2, 3, 4 } i\in\{1,2,3,4\}, | B i | ≥ n − 5 2 |B_{i}|\geq\frac{n-5}{2}. If there exists i ∈ { 1, 2, 3, 4 } i\in\{1,2,3,4\} such that | B i | = n − 5 2 |B_{i}|=\frac{n-5}{2}, then ∑ j ∈ { 1, 2, 3, 4 } ∖ { i } | B j | ≥ 2 ​ n − 4 − n − 5 2 = 3 ​ n − 3 2 \sum_{j\in\{1,2,3,4\}\setminus\{i\}}|B_{j}|\geq 2n-4-\frac{n-5}{2}=\frac{3n-3}{2}. Since B j ∈ 𝒜 < n / 2 B_{j}\in\mathcal{A}_{<n/2} for all j ∈ { 1, 2, 3, 4 } ∖ { i } j\in\{1,2,3,4\}\setminus\{i\}, we then have that | B j | = n − 1 2 |B_{j}|=\frac{n-1}{2} for all such j j, completing the proof of Proposition L.

Theorem 4.1. For any separating union-closed family 𝒜 \mathcal{A} with h = | ℬ | = 4 h=|\mathcal{B}|=4:

 | Avg ( 𝒜) > ⌊ n 2 ⌋ − 1. \textrm{Avg}(\mathcal{A})\ >\ \Bigr\lfloor\frac{n}{2}\Bigr\rfloor-1\textrm{.} |  |

Proof. The following blocks comprise the proof of this theorem:

- 1.

For each i ∈ { 1, 2, 3, 4 } i\in\{1,2,3,4\}, we denote by b i b_{i} the unique element from irr ℬ ​ ( B i) \texttt{irr}_{\mathcal{B}}(B_{i}) (see Proposition K). We consider any A ∈ 𝒜 < n / 2 ∖ ℬ A\in\mathcal{A}_{<n/2}\setminus\mathcal{B}, and note that b i ∈ A b_{i}\in A for some i ∈ { 1, 2, 3, 4 } i\in\{1,2,3,4\}. (Otherwise, A ⊊ A ∪ B 1 ⊊ A ∪ B 1 ∪ B 2 ⊊ A ∪ ⋃ i = 1 3 B i ⊊ [n] A\subsetneq A\cup B_{1}\subsetneq A\cup B_{1}\cup B_{2}\subsetneq A\cup\bigcup_{i=1}^{3}B_{i}\subsetneq[n], contradicting h = 4 h=4.) Without loss of generality, we assume that b 1 ∈ A b_{1}\in A and let ℬ ′ = { A, B 2, B 3, B 4 } \mathcal{B}^{\prime}=\{A,B_{2},B_{3},B_{4}\}. Noting that b ⁡ ( ℬ) = b ⁡ ( ℬ ′) b(\mathcal{B})=b(\mathcal{B}^{\prime}), it must be that ℬ ′ \mathcal{B}^{\prime} is an irredundant subfamily of 𝒜 \mathcal{A}. (If not, then | ℬ | < 4 |\mathcal{B}|<4, a contradiction.) Then, because ℬ \mathcal{B} is defined as any smallest irredundant subfamily of 𝒜 < n / 2 \mathcal{A}_{<n/2} such that b ⁡ ( ℬ) = b ⁡ ( 𝒜 < n / 2) b(\mathcal{B})=b(\mathcal{A}_{<n/2}), and ℬ ′ \mathcal{B^{\prime}} satisfies these conditions, the propositions of this section also apply to ℬ ′ \mathcal{B}^{\prime}.

- 2.

We assume that n n is even. By Proposition L, | B ′ | = n − 2 2 |B^{\prime}|=\frac{n-2}{2} for every B ′ ∈ ℬ ′ B^{\prime}\in\mathcal{B}^{\prime}, implying that | A | = n − 2 2 |A|=\frac{n-2}{2}. Therefore, any member set from 𝒜 < n / 2 \mathcal{A}_{<n/2} must have size equal to n − 2 2 \frac{n-2}{2}, implying that every member set in 𝒜 \mathcal{A} has size greater than or equal to n − 2 2 \frac{n-2}{2}. Noting that [n] ∈ 𝒜 [n]\in\mathcal{A}, we then have the result that Avg ​ ( 𝒜) > n − 2 2 = ⌊ n 2 ⌋ − 1 \textrm{Avg}(\mathcal{A})>\frac{n-2}{2}=\lfloor\frac{n}{2}\rfloor-1.

- 3.

We now assume that n n is odd.

  - A.

There must be some element j ∈ { 2, 3, 4 } j\in\{2,3,4\} such that b j ∈ A b_{j}\in A. (Otherwise, we again have a contradiction with h = 4 h=4 in that A ⊊ A ∪ B 2 ⊊ A ∪ B 2 ∪ B 3 ⊊ A ∪ ⋃ i = 2 4 B i ⊊ [n] A\subsetneq A\cup B_{2}\subsetneq A\cup B_{2}\cup B_{3}\subsetneq A\cup\bigcup_{i=2}^{4}B_{i}\subsetneq[n].) Without loss of generality, we assume that b 2 ∈ A b_{2}\in A and let ℬ ′′ = { B 1, A, B 3, B 4 } \mathcal{B}^{\prime\prime}=\{B_{1},A,B_{3},B_{4}\}. ℬ ′′ \mathcal{B}^{\prime\prime} is yet another family satisfying the conditions of ℬ \mathcal{B}, and is thus subject to the propositions of this section. We assume that there exists i ∈ { 1, 2, 3, 4 } i\in\{1,2,3,4\} such that | B i | = n − 5 2 |B_{i}|=\frac{n-5}{2}. Recall that, by part (ii) of Proposition L, if there exists i ∈ { 1, 2, 3, 4 } i\in\{1,2,3,4\} such that | B i | = n − 5 2 |B_{i}|=\frac{n-5}{2}, then | B j | = n − 1 2 |B_{j}|=\frac{n-1}{2} for all j ∈ { 1, 2, 3, 4 } ∖ { i } j\in\{1,2,3,4\}\setminus\{i\}. Therefore, we have that | A | = n − 1 2 |A|=\frac{n-1}{2} by applying Proposition L to ℬ ′′ \mathcal{B}^{\prime\prime} if | B 1 | = n − 5 2 |B_{1}|=\frac{n-5}{2}, to ℬ ′ \mathcal{B}^{\prime} if | B 2 | = n − 5 2 |B_{2}|=\frac{n-5}{2}, and to ℬ ′ \mathcal{B}^{\prime} (or ℬ ′′ \mathcal{B}^{\prime\prime}) if | B 3 | = n − 5 2 |B_{3}|=\frac{n-5}{2} or | B 4 | = n − 5 2 |B_{4}|=\frac{n-5}{2}. We now assume that no member set of ℬ \mathcal{B} has size n − 5 2 \frac{n-5}{2}, i.e. that | B i | ≥ n − 3 2 |B_{i}|\geq\frac{n-3}{2} for every i ∈ { 1, 2, 3, 4 } i\in\{1,2,3,4\}. If | A | ≤ n − 5 2 |A|\leq\frac{n-5}{2}, then | A | = n − 5 2 |A|=\frac{n-5}{2} by Proposition L, and we further apply Proposition L to ℬ ′′ \mathcal{B}^{\prime\prime} in order to obtain that | B 1 | = n − 1 2 |B_{1}|=\frac{n-1}{2}, to ℬ ′ \mathcal{B}^{\prime} in order to obtain that | B 2 | = n − 1 2 |B_{2}|=\frac{n-1}{2}, and to ℬ ′ \mathcal{B}^{\prime} (or ℬ ′′ \mathcal{B}^{\prime\prime}) in order to obtain that | B 3 | = n − 1 2 |B_{3}|=\frac{n-1}{2} and | B 4 | = n − 1 2 |B_{4}|=\frac{n-1}{2}.

  - B.

We execute block 1 of this proof followed by block 3A, applying the local reassignment A ← A ′ A\leftarrow A^{\prime} and ℬ ← ℬ ′ \mathcal{B}\leftarrow\mathcal{B}^{\prime}, in order to obtain that | A ′ | = n − 1 2 |A^{\prime}|=\frac{n-1}{2}. A A is therefore the only member set of 𝒜 \mathcal{A} with size less than or equal to n − 5 2 \frac{n-5}{2}. Again noting that [n] ∈ 𝒜 [n]\in\mathcal{A}, this implies that Avg ​ ( 𝒜) > n − 3 2 = ⌊ n 2 ⌋ − 1 \textrm{Avg}(\mathcal{A})>\frac{n-3}{2}=\lfloor\frac{n}{2}\rfloor-1, completing the proof of Theorem 4.1.

## References

- [1] I. Balla, B. Bollobás, and T. Eccles, Union-closed families of sets, J. Combin. Theory Ser. A 120 (2013), 531–544.
- [2] H. Bruhn, P. Charbit, O. Schaudt, and J.A. Telle, The graph formulation of the union-closed sets conjecture, European J. Combin. 43 (2015), 210–219.
- [3] H. Bruhn and O. Schaudt, The journey of the union-closed sets conjecture, Graphs Combin. 31 (2015), 2043–2074.
- [4] S. Cambie, Progress on the union-closed conjecture and offsprings in winter 2022-2023, preprint (2023), arXiv:2306.12351.
- [5] C. Colbert, Chain conditions and optimal elements in generalized union-closed families of sets, preprint (2025), arXiv:2412.18740.
- [6] G. Czédli, On averaging Frankl’s conjecture for large union-closed-sets, J. Combin. Theory Ser. A 116 (2009), 724–729.
- [7] G. Czédli, M. Maróti, and E.T. Schmidt, On the scope of averaging for Frankl’s conjecture, Order 26 (2009), 31–48.
- [8] V. Falgas-Ravry, Minimal weight in union-closed families, Electron. J. Combin. 18(1) (2011), P95.
- [9] J. Gilmer, A constant lower bound for the union-closed sets conjecture, preprint (2022), arXiv:2211.09055.
- [10] B. Poonen, Union-closed families, J. Combin. Theory Ser. A 59 (1992), 253–268.
- [11] D. Reimer, An average set size theorem, Combin. Probab. Comput. 12 (2003), 89–93.
- [12] W. Sawin, An improved lower bound for the union-closed set conjecture, preprint (2023), arXiv:2211.11504.
- [13] C. Tian, Union-closed sets conjecture holds for height no more than 3 and height no less than N-1, preprint (2022), arXiv:2112.06659.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
