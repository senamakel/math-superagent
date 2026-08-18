<!-- source: https://en.wikipedia.org/wiki/Schubert_calculus | converted from HTML -->

Schubert calculus - Wikipedia

Jump to content

From Wikipedia, the free encyclopedia

Branch of algebraic geometry

In [mathematics][1], **Schubert calculus**[1] is a branch of [algebraic geometry][2] introduced in the nineteenth century by [Hermann Schubert][3] in order to solve various counting problems of [projective geometry][4] and, as such, is viewed as part of [enumerative geometry][5]. Giving it a more rigorous foundation was the aim of [Hilbert's 15th problem][6]. It is related to several more modern concepts, such as [characteristic classes][7], and both its algorithmic aspects and applications remain of current interest. The term **Schubert calculus**is sometimes used to mean the enumerative geometry of linear subspaces of a vector space, which is roughly equivalent to describing the cohomology ring of Grassmannians. Sometimes it is used to mean the more general enumerative geometry of algebraic varieties that are homogenous spaces of simple Lie groups. Even more generally, **Schubert calculus**is sometimes understood as encompassing the study of analogous questions in [generalized cohomology theories][8].

The objects introduced by Schubert are the **Schubert cells**, [2] which are [locally closed][9] sets in a [Grassmannian][10] defined by conditions of [incidence][11] of a [linear subspace][12] in projective space with a given [flag][13]. For further details see [Schubert variety][14].

The [intersection theory][15] [3] of these cells, which can be seen as the product structure in the [cohomology ring][16] of the Grassmannian, consisting of associated [cohomology classes][17], allows in particular the determination of cases in which the intersections of cells results in a [finite set][18] of points. A key result is that the Schubert cells (or rather, the classes of their Zariski closures, the **Schubert cycles**or **[Schubert varieties][19]**) span the whole cohomology ring.

The combinatorial aspects mainly arise in relation to computing intersections of Schubert cycles. Lifted from the [Grassmannian][10], which is a [homogeneous space][20], to the [general linear group][21] that acts on it, similar questions are involved in the [Bruhat decomposition][22] and classification of [parabolic subgroups][23] (as [block triangular][24] matrices).

## Construction

[[edit][25]]

Schubert calculus can be constructed using the [Chow ring][26] [3] of the [Grassmannian][10], where the generating cycles are represented by geometrically defined data. [4] Denote the Grassmannian of k {\displaystyle k}[image: {\displaystyle k}] -planes in a fixed n {\displaystyle n}[image: {\displaystyle n}] -dimensional vector space V {\displaystyle V}[image: {\displaystyle V}] as G r ( k, V) {\displaystyle \mathbf {Gr} (k,V)}[image: {\displaystyle \mathbf {Gr} (k,V)}], and its Chow ring as A ∗ ( G r ( k, V)) {\displaystyle A^{*}(\mathbf {Gr} (k,V))}[image: {\displaystyle A^{*}(\mathbf {Gr} (k,V))}]. (Note that the Grassmannian is sometimes denoted G r ( k, n) {\displaystyle \mathbf {Gr} (k,n)}[image: {\displaystyle \mathbf {Gr} (k,n)}] if the vector space is not explicitly given or as G ( k − 1, n − 1) {\displaystyle \mathbb {G} (k-1,n-1)}[image: {\displaystyle \mathbb {G} (k-1,n-1)}] if the ambient space V {\displaystyle V}[image: {\displaystyle V}] and its k {\displaystyle k}[image: {\displaystyle k}] -dimensional subspaces are replaced by their projectivizations.) Choosing an (arbitrary) [complete flag][27]

V = ( V 1 ⊂ ⋯ ⊂ V n − 1 ⊂ V n = V), dim ⁡ V i = i, i = 1, …, n, {\displaystyle {\mathcal {V}}=(V_{1}\subset \cdots \subset V_{n-1}\subset V_{n}=V),\quad \dim {V}_{i}=i,\quad i=1,\dots ,n,}[image: {\displaystyle {\mathcal {V}}=(V_{1}\subset \cdots \subset V_{n-1}\subset V_{n}=V),\quad \dim {V}_{i}=i,\quad i=1,\dots ,n,}]

to each weakly decreasing k {\displaystyle k}[image: {\displaystyle k}] -tuple of integers a = ( a 1, …, a k) {\displaystyle \mathbf {a} =(a_{1},\ldots ,a_{k})}[image: {\displaystyle \mathbf {a} =(a_{1},\ldots ,a_{k})}], where

n − k ≥ a 1 ≥ a 2 ≥ ⋯ ≥ a k ≥ 0, {\displaystyle n-k\geq a_{1}\geq a_{2}\geq \cdots \geq a_{k}\geq 0,}[image: {\displaystyle n-k\geq a_{1}\geq a_{2}\geq \cdots \geq a_{k}\geq 0,}]

i.e., to each [partition][28] of weight

| a | = ∑ i = 1 k a i, {\displaystyle {\mathopen {|}}\mathbf {a} {\mathclose {|}}=\sum _{i=1}^{k}a_{i},}[image: {\displaystyle {\mathopen {|}}\mathbf {a} {\mathclose {|}}=\sum _{i=1}^{k}a_{i},}]

whose [Young diagram][29] fits into the k × ( n − k) {\displaystyle k\times (n-k)}[image: {\displaystyle k\times (n-k)}] rectangular one for the partition ( n − k) k {\displaystyle (n-k)^{k}}[image: {\displaystyle (n-k)^{k}}], we associate a **Schubert variety**[1] [2] (or **Schubert cycle**) Σ a ( V) ⊂ G r ( k, V) {\displaystyle \Sigma _{\mathbf {a} }({\mathcal {V}})\subset \mathbf {Gr} (k,V)}[image: {\displaystyle \Sigma _{\mathbf {a} }({\mathcal {V}})\subset \mathbf {Gr} (k,V)}], defined as

Σ a ( V) = { w ∈ G r ( k, V): dim ⁡ ( V n − k + i − a i ∩ w) ≥ i for i = 1, …, k }. {\displaystyle \Sigma _{\mathbf {a} }({\mathcal {V}})=\{w\in \mathbf {Gr} (k,V):\dim(V_{n-k+i-a_{i}}\cap w)\geq i{\text{ for }}i=1,\dots ,k\}.}[image: {\displaystyle \Sigma _{\mathbf {a} }({\mathcal {V}})=\{w\in \mathbf {Gr} (k,V):\dim(V_{n-k+i-a_{i}}\cap w)\geq i{\text{ for }}i=1,\dots ,k\}.}]

This is the closure, in the [Zariski topology][30], of the **Schubert cell**[1] [2]

X a ( V):= { w ∈ G r ( k, V): dim ⁡ ( V j ∩ w) = i for all n − k − a i + i ≤ j ≤ n − k − a i + 1 + i, 1 ≤ j ≤ n } ⊂ Σ a ( V), {\displaystyle X_{\mathbf {a} }({\mathcal {V}}):=\{w\in \mathbf {Gr} (k,V):\dim(V_{j}\cap w)=i{\text{ for all }}n-k-a_{i}+i\leq j\leq n-k-a_{i+1}+i,\quad 1\leq j\leq n\}\subset \Sigma _{\mathbf {a} }({\mathcal {V}}),}[image: {\displaystyle X_{\mathbf {a} }({\mathcal {V}}):=\{w\in \mathbf {Gr} (k,V):\dim(V_{j}\cap w)=i{\text{ for all }}n-k-a_{i}+i\leq j\leq n-k-a_{i+1}+i,\quad 1\leq j\leq n\}\subset \Sigma _{\mathbf {a} }({\mathcal {V}}),}]

which is used when considering [cellular homology][31] instead of the Chow ring. The latter are disjoint affine spaces, of dimension | a | {\displaystyle |\mathbf {a} |}[image: {\displaystyle |\mathbf {a} |}], whose union is G r ( k, V) {\displaystyle \mathbf {Gr} (k,V)}[image: {\displaystyle \mathbf {Gr} (k,V)}].

An equivalent characterization of the Schubert cell X a ( V) {\displaystyle X_{\mathbf {a} }({\mathcal {V}})}[image: {\displaystyle X_{\mathbf {a} }({\mathcal {V}})}] may be given in terms of the [dual complete flag][27]

V ~ = ( V ~ 1 ⊂ V ~ 2 ⋯ ⊂ V ~ n = V), {\displaystyle {\tilde {\mathcal {V}}}=({\tilde {V}}_{1}\subset {\tilde {V}}_{2}\cdots \subset {\tilde {V}}_{n}=V),}[image: {\displaystyle {\tilde {\mathcal {V}}}=({\tilde {V}}_{1}\subset {\tilde {V}}_{2}\cdots \subset {\tilde {V}}_{n}=V),}]

where

V ~ i:= V n ∖ V n − i, i = 1, …, n ( V 0:= ∅). {\displaystyle {\tilde {V}}_{i}:=V_{n}\backslash V_{n-i},\quad i=1,\dots ,n\quad (V_{0}:=\emptyset ).}[image: {\displaystyle {\tilde {V}}_{i}:=V_{n}\backslash V_{n-i},\quad i=1,\dots ,n\quad (V_{0}:=\emptyset ).}]

Then X a ( V) ⊂ G r ( k, V) {\displaystyle X_{\mathbf {a} }({\mathcal {V}})\subset \mathbf {Gr} (k,V)}[image: {\displaystyle X_{\mathbf {a} }({\mathcal {V}})\subset \mathbf {Gr} (k,V)}] consists of those k {\displaystyle k}[image: {\displaystyle k}] -dimensional subspaces w ⊂ V {\displaystyle w\subset V}[image: {\displaystyle w\subset V}] that have a basis ( W ~ 1, …, W ~ k) {\displaystyle ({\tilde {W}}_{1},\dots ,{\tilde {W}}_{k})}[image: {\displaystyle ({\tilde {W}}_{1},\dots ,{\tilde {W}}_{k})}] consisting of elements

W ~ i ∈ V ~ k + a i − i + 1, i = 1, …, k {\displaystyle {\tilde {W}}_{i}\in {\tilde {V}}_{k+a_{i}-i+1},\quad i=1,\dots ,k}[image: {\displaystyle {\tilde {W}}_{i}\in {\tilde {V}}_{k+a_{i}-i+1},\quad i=1,\dots ,k}]

of the subspaces { V ~ k + a i − i + 1 } i = 1, …, k. {\displaystyle \{{\tilde {V}}_{k+a_{i}-i+1}\}_{i=1,\dots ,k}.}[image: {\displaystyle \{{\tilde {V}}_{k+a_{i}-i+1}\}_{i=1,\dots ,k}.}]

Since the homology class [Σ a ( V)] ∈ A ∗ ( G r ( k, V)) {\displaystyle [\Sigma _{\mathbf {a} }({\mathcal {V}})]\in A^{*}(\mathbf {Gr} (k,V))}[image: {\displaystyle [\Sigma _{\mathbf {a} }({\mathcal {V}})]\in A^{*}(\mathbf {Gr} (k,V))}], called a **Schubert class**, does not depend on the choice of complete flag V {\displaystyle {\mathcal {V}}}[image: {\displaystyle {\mathcal {V}}}], it can be written as

σ a:= [Σ a] ∈ A ∗ ( G r ( k, V)). {\displaystyle \sigma _{\mathbf {a} }:=[\Sigma _{\mathbf {a} }]\in A^{*}(\mathbf {Gr} (k,V)).}[image: {\displaystyle \sigma _{\mathbf {a} }:=[\Sigma _{\mathbf {a} }]\in A^{*}(\mathbf {Gr} (k,V)).}]

It can be shown that these classes are linearly independent and generate the Chow ring as their [linear span][32]. The associated intersection theory is called **Schubert calculus**. For a given sequence a = ( a 1, …, a j, 0, …, 0) {\displaystyle \mathbf {a} =(a_{1},\ldots ,a_{j},0,\ldots ,0)}[image: {\displaystyle \mathbf {a} =(a_{1},\ldots ,a_{j},0,\ldots ,0)}] with 0"}}'> 0}"> a j > 0 {\displaystyle a_{j}>0} 0}"/> the Schubert class σ ( a 1, …, a j, 0, …, 0) {\displaystyle \sigma _{(a_{1},\ldots ,a_{j},0,\ldots ,0)}}[image: {\displaystyle \sigma _{(a_{1},\ldots ,a_{j},0,\ldots ,0)}}] is usually just denoted σ ( a 1, …, a j) {\displaystyle \sigma _{(a_{1},\ldots ,a_{j})}}[image: {\displaystyle \sigma _{(a_{1},\ldots ,a_{j})}}]. The Schubert classes given by a single integer σ a 1 {\displaystyle \sigma _{a_{1}}}[image: {\displaystyle \sigma _{a_{1}}}], (i.e., a horizontal partition), are called **special classes**. Using the [Giambelli formula][33] below, all the Schubert classes can be generated from these special classes.

### Other notational conventions

[[edit][34]]

In some sources, [1] [2] the Schubert cells X a {\displaystyle X_{\mathbf {a} }}[image: {\displaystyle X_{\mathbf {a} }}] and Schubert varieties Σ a {\displaystyle \Sigma _{\mathbf {a} }}[image: {\displaystyle \Sigma _{\mathbf {a} }}] are labelled differently, as S λ {\displaystyle S_{\lambda }}[image: {\displaystyle S_{\lambda }}] and S ¯ λ {\displaystyle {\bar {S}}_{\lambda }}[image: {\displaystyle {\bar {S}}_{\lambda }}], respectively, where λ {\displaystyle \lambda }[image: {\displaystyle \lambda }] is the *complementary partition*to a {\displaystyle \mathbf {a} }[image: {\displaystyle \mathbf {a} }] with parts

λ i:= n − k − a k − i + 1 {\displaystyle \lambda _{i}:=n-k-a_{k-i+1}}[image: {\displaystyle \lambda _{i}:=n-k-a_{k-i+1}}],

whose Young diagram is the complement of the one for a {\displaystyle \mathbf {a} }[image: {\displaystyle \mathbf {a} }] within the k × ( n − k) {\displaystyle k\times (n-k)}[image: {\displaystyle k\times (n-k)}] rectangular one (reversed, both horizontally and vertically).

Another labelling convention for X a {\displaystyle X_{\mathbf {a} }}[image: {\displaystyle X_{\mathbf {a} }}] and Σ a {\displaystyle \Sigma _{\mathbf {a} }}[image: {\displaystyle \Sigma _{\mathbf {a} }}] is C L {\displaystyle C_{L}}[image: {\displaystyle C_{L}}] and C ¯ L {\displaystyle {\bar {C}}_{L}}[image: {\displaystyle {\bar {C}}_{L}}], respectively, where L = ( L 1, …, L k) ⊂ ( 1, …, n) {\displaystyle L=(L_{1},\dots ,L_{k})\subset (1,\dots ,n)}[image: {\displaystyle L=(L_{1},\dots ,L_{k})\subset (1,\dots ,n)}] is the multi-index defined by

L i:= n − k − a i + i = λ k − i + 1 + i. {\displaystyle L_{i}:=n-k-a_{i}+i=\lambda _{k-i+1}+i.}[image: {\displaystyle L_{i}:=n-k-a_{i}+i=\lambda _{k-i+1}+i.}]

The integers ( L 1, …, L k) {\displaystyle (L_{1},\dots ,L_{k})}[image: {\displaystyle (L_{1},\dots ,L_{k})}] are the **pivot**locations of the representations of elements of X a {\displaystyle X_{\mathbf {a} }}[image: {\displaystyle X_{\mathbf {a} }}] in reduced matricial [echelon form][35].

### Explanation

[[edit][36]]

In order to explain the definition, consider a generic k {\displaystyle k}[image: {\displaystyle k}] -plane w ⊂ V {\displaystyle w\subset V}[image: {\displaystyle w\subset V}]. It will have only a zero intersection with V j {\displaystyle V_{j}}[image: {\displaystyle V_{j}}] for j ≤ n − k {\displaystyle j\leq n-k}[image: {\displaystyle j\leq n-k}], whereas

dim ⁡ ( V j ∩ w) = i {\displaystyle \dim(V_{j}\cap w)=i}[image: {\displaystyle \dim(V_{j}\cap w)=i}] for j = n − k + i ≥ n − k. {\displaystyle j=n-k+i\geq n-k.}[image: {\displaystyle j=n-k+i\geq n-k.}]

For example, in G r ( 4, 9) {\displaystyle \mathbf {Gr} (4,9)}[image: {\displaystyle \mathbf {Gr} (4,9)}], a 4 {\displaystyle 4}[image: {\displaystyle 4}] -plane w {\displaystyle w}[image: {\displaystyle w}] is the solution space of a system of five independent homogeneous linear equations. These equations will generically span when restricted to a subspace V j {\displaystyle V_{j}}[image: {\displaystyle V_{j}}] with j = dim ⁡ V j ≤ 5 = 9 − 4 {\displaystyle j=\dim V_{j}\leq 5=9-4}[image: {\displaystyle j=\dim V_{j}\leq 5=9-4}], in which case the solution space (the intersection of V j {\displaystyle V_{j}}[image: {\displaystyle V_{j}}] with w {\displaystyle w}[image: {\displaystyle w}]) will consist only of the zero vector. However, if n=9"}}'> n=9}"> dim ⁡ ( V j) + dim ⁡ ( w) > n = 9 {\displaystyle \dim(V_{j})+\dim(w)>n=9} n=9}"/>, V j {\displaystyle V_{j}}[image: {\displaystyle V_{j}}] and w {\displaystyle w}[image: {\displaystyle w}] will necessarily have nonzero intersection. For example, the expected dimension of intersection of V 6 {\displaystyle V_{6}}[image: {\displaystyle V_{6}}] and w {\displaystyle w}[image: {\displaystyle w}] is 1 {\displaystyle 1}[image: {\displaystyle 1}], the intersection of V 7 {\displaystyle V_{7}}[image: {\displaystyle V_{7}}] and w {\displaystyle w}[image: {\displaystyle w}] has expected dimension 2 {\displaystyle 2}[image: {\displaystyle 2}], and so on.

The definition of a Schubert variety states that the first value of j {\displaystyle j}[image: {\displaystyle j}] with dim ⁡ ( V j ∩ w) ≥ i {\displaystyle \dim(V_{j}\cap w)\geq i}[image: {\displaystyle \dim(V_{j}\cap w)\geq i}] is generically smaller than the expected value n − k + i {\displaystyle n-k+i}[image: {\displaystyle n-k+i}] by the parameter a i {\displaystyle a_{i}}[image: {\displaystyle a_{i}}]. The k {\displaystyle k}[image: {\displaystyle k}] -planes w ⊂ V {\displaystyle w\subset V}[image: {\displaystyle w\subset V}] given by these constraints then define special subvarieties of G r ( k, n) {\displaystyle \mathbf {Gr} (k,n)}[image: {\displaystyle \mathbf {Gr} (k,n)}]. [4]

### Properties

[[edit][37]]

#### Inclusion

[[edit][38]]

There is a partial ordering on all k {\displaystyle k}[image: {\displaystyle k}] -tuples where a ≥ b {\displaystyle \mathbf {a} \geq \mathbf {b} }[image: {\displaystyle \mathbf {a} \geq \mathbf {b} }] if a i ≥ b i {\displaystyle a_{i}\geq b_{i}}[image: {\displaystyle a_{i}\geq b_{i}}] for every i {\displaystyle i}[image: {\displaystyle i}]. This gives the inclusion of Schubert varieties

Σ a ⊂ Σ b ⟺ a ≥ b, {\displaystyle \Sigma _{\mathbf {a} }\subset \Sigma _{\mathbf {b} }\iff \mathbf {a} \geq \mathbf {b} ,}[image: {\displaystyle \Sigma _{\mathbf {a} }\subset \Sigma _{\mathbf {b} }\iff \mathbf {a} \geq \mathbf {b} ,}]

showing an increase of the indices corresponds to an even greater specialization of subvarieties.

#### Dimension formula

[[edit][39]]

A Schubert variety Σ a {\displaystyle \Sigma _{\mathbf {a} }}[image: {\displaystyle \Sigma _{\mathbf {a} }}] has codimension equal to the weight

| a | = ∑ a i {\displaystyle {\mathopen {|}}\mathbf {a} {\mathclose {|}}=\sum a_{i}}[image: {\displaystyle {\mathopen {|}}\mathbf {a} {\mathclose {|}}=\sum a_{i}}]

of the partition a {\displaystyle \mathbf {a} }[image: {\displaystyle \mathbf {a} }]. Alternatively, in the notational convention S λ {\displaystyle S_{\lambda }}[image: {\displaystyle S_{\lambda }}] indicated above, its dimension in G r ( k, n) {\displaystyle \mathbf {Gr} (k,n)}[image: {\displaystyle \mathbf {Gr} (k,n)}] is the weight

| λ | = ∑ i = 1 k λ i = k ( n − k) − | a |. {\displaystyle {\mathopen {|}}\lambda {\mathclose {|}}=\sum _{i=1}^{k}\lambda _{i}=k(n-k)-{\mathopen {|}}\mathbf {a} {\mathclose {|}}.}[image: {\displaystyle {\mathopen {|}}\lambda {\mathclose {|}}=\sum _{i=1}^{k}\lambda _{i}=k(n-k)-{\mathopen {|}}\mathbf {a} {\mathclose {|}}.}]

of the complementary partition λ ⊂ ( n − k) k {\displaystyle \lambda \subset (n-k)^{k}}[image: {\displaystyle \lambda \subset (n-k)^{k}}] in the k × ( n − k) {\displaystyle k\times (n-k)}[image: {\displaystyle k\times (n-k)}] dimensional rectangular Young diagram.

This is stable under inclusions of Grassmannians. That is, the inclusion

i ( k, n): G r ( k, C n) ↪ G r ( k, C n + 1), C n = span { e 1, …, e n } {\displaystyle i_{(k,n)}:\mathbf {Gr} (k,\mathbf {C} ^{n})\hookrightarrow \mathbf {Gr} (k,\mathbf {C} ^{n+1}),\quad \mathbf {C} ^{n}={\text{span}}\{e_{1},\dots ,e_{n}\}}[image: {\displaystyle i_{(k,n)}:\mathbf {Gr} (k,\mathbf {C} ^{n})\hookrightarrow \mathbf {Gr} (k,\mathbf {C} ^{n+1}),\quad \mathbf {C} ^{n}={\text{span}}\{e_{1},\dots ,e_{n}\}}]

defined, for w ∈ G r ( k, C n) {\displaystyle w\in \mathbf {Gr} (k,\mathbf {C} ^{n})}[image: {\displaystyle w\in \mathbf {Gr} (k,\mathbf {C} ^{n})}], by

i ( k, n): w ⊂ C n ↦ w ⊂ C n ⊕ C e n + 1 = C n + 1 {\displaystyle i_{(k,n)}:w\subset \mathbf {C} ^{n}\mapsto w\subset \mathbf {C} ^{n}\oplus \mathbf {C} e_{n+1}=\mathbf {C} ^{n+1}}[image: {\displaystyle i_{(k,n)}:w\subset \mathbf {C} ^{n}\mapsto w\subset \mathbf {C} ^{n}\oplus \mathbf {C} e_{n+1}=\mathbf {C} ^{n+1}}]

has the property

i ( k, n) ∗ ( σ a) = σ a, {\displaystyle i_{(k,n)}^{*}(\sigma _{\mathbf {a} })=\sigma _{\mathbf {a} },}[image: {\displaystyle i_{(k,n)}^{*}(\sigma _{\mathbf {a} })=\sigma _{\mathbf {a} },}]

and the inclusion

i ~ ( k, n): G r ( k, n) ↪ G r ( k + 1, n + 1) {\displaystyle {\tilde {i}}_{(k,n)}:\mathbf {Gr} (k,n)\hookrightarrow \mathbf {Gr} (k+1,n+1)}[image: {\displaystyle {\tilde {i}}_{(k,n)}:\mathbf {Gr} (k,n)\hookrightarrow \mathbf {Gr} (k+1,n+1)}]

defined by adding the extra basis element e n + 1 {\displaystyle e_{n+1}}[image: {\displaystyle e_{n+1}}] to each k {\displaystyle k}[image: {\displaystyle k}] -plane, giving a ( k + 1) {\displaystyle (k+1)}[image: {\displaystyle (k+1)}] -plane,

i ~ ( k, n): w ↦ w ⊕ C e n + 1 ⊂ C n ⊕ C e n + 1 = C n + 1 {\displaystyle {\tilde {i}}_{(k,n)}:w\mapsto w\oplus \mathbf {C} e_{n+1}\subset \mathbf {C} ^{n}\oplus \mathbf {C} e_{n+1}=\mathbf {C} ^{n+1}}[image: {\displaystyle {\tilde {i}}_{(k,n)}:w\mapsto w\oplus \mathbf {C} e_{n+1}\subset \mathbf {C} ^{n}\oplus \mathbf {C} e_{n+1}=\mathbf {C} ^{n+1}}]

does as well

i ~ ( k, n) ∗ ( σ a) = σ a. {\displaystyle {\tilde {i}}_{(k,n)}^{*}(\sigma _{\mathbf {a} })=\sigma _{\mathbf {a} }.}[image: {\displaystyle {\tilde {i}}_{(k,n)}^{*}(\sigma _{\mathbf {a} })=\sigma _{\mathbf {a} }.}]

Thus, if X a ⊂ G r k ( n) {\displaystyle X_{\mathbf {a} }\subset \mathbf {Gr} _{k}(n)}[image: {\displaystyle X_{\mathbf {a} }\subset \mathbf {Gr} _{k}(n)}] and Σ a ⊂ G r k ( n) {\displaystyle \Sigma _{\mathbf {a} }\subset \mathbf {Gr} _{k}(n)}[image: {\displaystyle \Sigma _{\mathbf {a} }\subset \mathbf {Gr} _{k}(n)}] are a cell and a subvariety in the Grassmannian G r k ( n) {\displaystyle \mathbf {Gr} _{k}(n)}[image: {\displaystyle \mathbf {Gr} _{k}(n)}], they may also be viewed as a cell X a ⊂ G r k ~ ( n ~) {\displaystyle X_{\mathbf {a} }\subset \mathbf {Gr} _{\tilde {k}}({\tilde {n}})}[image: {\displaystyle X_{\mathbf {a} }\subset \mathbf {Gr} _{\tilde {k}}({\tilde {n}})}] and a subvariety Σ a ⊂ G r k ~ ( n ~) {\displaystyle \Sigma _{\mathbf {a} }\subset \mathbf {Gr} _{\tilde {k}}({\tilde {n}})}[image: {\displaystyle \Sigma _{\mathbf {a} }\subset \mathbf {Gr} _{\tilde {k}}({\tilde {n}})}] within the Grassmannian G r k ~ ( n ~) {\displaystyle \mathbf {Gr} _{\tilde {k}}({\tilde {n}})}[image: {\displaystyle \mathbf {Gr} _{\tilde {k}}({\tilde {n}})}] for any pair ( k ~, n ~) {\displaystyle ({\tilde {k}},{\tilde {n}})}[image: {\displaystyle ({\tilde {k}},{\tilde {n}})}] with k ~ ≥ k {\displaystyle {\tilde {k}}\geq k}[image: {\displaystyle {\tilde {k}}\geq k}] and n ~ − k ~ ≥ n − k {\displaystyle {\tilde {n}}-{\tilde {k}}\geq n-k}[image: {\displaystyle {\tilde {n}}-{\tilde {k}}\geq n-k}].

### Intersection product

[[edit][40]]

The intersection product was first established using the **[Pieri][41]**and **[Giambelli][42]**formulas.

#### Pieri formula

[[edit][43]]

In the special case b = ( b, 0, …, 0) {\displaystyle \mathbf {b} =(b,0,\ldots ,0)}[image: {\displaystyle \mathbf {b} =(b,0,\ldots ,0)}], there is an explicit formula of the product of σ b {\displaystyle \sigma _{b}}[image: {\displaystyle \sigma _{b}}] with an arbitrary Schubert class σ a 1, …, a k {\displaystyle \sigma _{a_{1},\ldots ,a_{k}}}[image: {\displaystyle \sigma _{a_{1},\ldots ,a_{k}}}] given by

σ b ⋅ σ a 1, …, a k = ∑ | c | = | a | + b a i ≤ c i ≤ a i − 1 σ c, {\displaystyle \sigma _{b}\cdot \sigma _{a_{1},\ldots ,a_{k}}=\sum _{\begin{matrix}{\mathopen {|}}c{\mathclose {|}}={\mathopen {|}}a{\mathclose {|}}+b\\a_{i}\leq c_{i}\leq a_{i-1}\end{matrix}}\sigma _{\mathbf {c} },}[image: {\displaystyle \sigma _{b}\cdot \sigma _{a_{1},\ldots ,a_{k}}=\sum _{\begin{matrix}{\mathopen {|}}c{\mathclose {|}}={\mathopen {|}}a{\mathclose {|}}+b\\a_{i}\leq c_{i}\leq a_{i-1}\end{matrix}}\sigma _{\mathbf {c} },}]

where | a | = a 1 + ⋯ + a k {\displaystyle {\mathopen {|}}\mathbf {a} {\mathclose {|}}=a_{1}+\cdots +a_{k}}[image: {\displaystyle {\mathopen {|}}\mathbf {a} {\mathclose {|}}=a_{1}+\cdots +a_{k}}], | c | = c 1 + ⋯ + c k {\displaystyle |\mathbf {c} |=c_{1}+\cdots +c_{k}}[image: {\displaystyle |\mathbf {c} |=c_{1}+\cdots +c_{k}}] are the weights of the partitions. This is called the **[Pieri formula][44]**, and can be used to determine the intersection product of any two Schubert classes when combined with the **[Giambelli formula][33]**. For example,

σ 1 ⋅ σ 4, 2, 1 = σ 5, 2, 1 + σ 4, 3, 1 + σ 4, 2, 1, 1. {\displaystyle \sigma _{1}\cdot \sigma _{4,2,1}=\sigma _{5,2,1}+\sigma _{4,3,1}+\sigma _{4,2,1,1}.}[image: {\displaystyle \sigma _{1}\cdot \sigma _{4,2,1}=\sigma _{5,2,1}+\sigma _{4,3,1}+\sigma _{4,2,1,1}.}]

and

σ 2 ⋅ σ 4, 3 = σ 4, 3, 2 + σ 4, 4, 1 + σ 5, 3, 1 + σ 5, 4 + σ 6, 3 {\displaystyle \sigma _{2}\cdot \sigma _{4,3}=\sigma _{4,3,2}+\sigma _{4,4,1}+\sigma _{5,3,1}+\sigma _{5,4}+\sigma _{6,3}}[image: {\displaystyle \sigma _{2}\cdot \sigma _{4,3}=\sigma _{4,3,2}+\sigma _{4,4,1}+\sigma _{5,3,1}+\sigma _{5,4}+\sigma _{6,3}}]

#### Giambelli formula

[[edit][45]]

Schubert classes σ a {\displaystyle \sigma _{\mathbf {a} }}[image: {\displaystyle \sigma _{\mathbf {a} }}] for partitions of any length ℓ ( a) ≤ k {\displaystyle \ell (\mathbf {a} )\leq k}[image: {\displaystyle \ell (\mathbf {a} )\leq k}] can be expressed as the determinant of a ( k × k) {\displaystyle (k\times k)}[image: {\displaystyle (k\times k)}] matrix having the special classes as entries.

σ ( a 1, …, a k) = | σ a 1 σ a 1 + 1 σ a 1 + 2 ⋯ σ a 1 + k − 1 σ a 2 − 1 σ a 2 σ a 2 + 1 ⋯ σ a 2 + k − 2 σ a 3 − 2 σ a 3 − 1 σ a 3 ⋯ σ a 3 + k − 3 ⋮ ⋮ ⋮ ⋱ ⋮ σ a k − k + 1 σ a k − k + 2 σ a k − k + 3 ⋯ σ a k | {\displaystyle \sigma _{(a_{1},\ldots ,a_{k})}={\begin{vmatrix}\sigma _{a_{1}}&\sigma _{a_{1}+1}&\sigma _{a_{1}+2}&\cdots &\sigma _{a_{1}+k-1}\\\sigma _{a_{2}-1}&\sigma _{a_{2}}&\sigma _{a_{2}+1}&\cdots &\sigma _{a_{2}+k-2}\\\sigma _{a_{3}-2}&\sigma _{a_{3}-1}&\sigma _{a_{3}}&\cdots &\sigma _{a_{3}+k-3}\\\vdots &\vdots &\vdots &\ddots &\vdots \\\sigma _{a_{k}-k+1}&\sigma _{a_{k}-k+2}&\sigma _{a_{k}-k+3}&\cdots &\sigma _{a_{k}}\end{vmatrix}}}[image: {\displaystyle \sigma _{(a_{1},\ldots ,a_{k})}={\begin{vmatrix}\sigma _{a_{1}}&\sigma _{a_{1}+1}&\sigma _{a_{1}+2}&\cdots &\sigma _{a_{1}+k-1}\\\sigma _{a_{2}-1}&\sigma _{a_{2}}&\sigma _{a_{2}+1}&\cdots &\sigma _{a_{2}+k-2}\\\sigma _{a_{3}-2}&\sigma _{a_{3}-1}&\sigma _{a_{3}}&\cdots &\sigma _{a_{3}+k-3}\\\vdots &\vdots &\vdots &\ddots &\vdots \\\sigma _{a_{k}-k+1}&\sigma _{a_{k}-k+2}&\sigma _{a_{k}-k+3}&\cdots &\sigma _{a_{k}}\end{vmatrix}}}]

This is known as the **[Giambelli formula][33]**. It has the same form as the first ****[Jacobi-Trudi identity][46], expressing arbitrary ****[Schur functions][47] s a {\displaystyle s_{\mathbf {a} }}[image: {\displaystyle s_{\mathbf {a} }}] as determinants in terms of the ****[complete symmetric functions][46] { h j:= s ( j) } {\displaystyle \{h_{j}:=s_{(j)}\}}[image: {\displaystyle \{h_{j}:=s_{(j)}\}}].

For example,

σ 2, 2 = | σ 2 σ 3 σ 1 σ 2 | = σ 2 2 − σ 1 ⋅ σ 3 {\displaystyle \sigma _{2,2}={\begin{vmatrix}\sigma _{2}&\sigma _{3}\\\sigma _{1}&\sigma _{2}\end{vmatrix}}=\sigma _{2}^{2}-\sigma _{1}\cdot \sigma _{3}}[image: {\displaystyle \sigma _{2,2}={\begin{vmatrix}\sigma _{2}&\sigma _{3}\\\sigma _{1}&\sigma _{2}\end{vmatrix}}=\sigma _{2}^{2}-\sigma _{1}\cdot \sigma _{3}}]

and

σ 2, 1, 1 = | σ 2 σ 3 σ 4 σ 0 σ 1 σ 2 0 σ 0 σ 1 |. {\displaystyle \sigma _{2,1,1}={\begin{vmatrix}\sigma _{2}&\sigma _{3}&\sigma _{4}\\\sigma _{0}&\sigma _{1}&\sigma _{2}\\0&\sigma _{0}&\sigma _{1}\end{vmatrix}}.}[image: {\displaystyle \sigma _{2,1,1}={\begin{vmatrix}\sigma _{2}&\sigma _{3}&\sigma _{4}\\\sigma _{0}&\sigma _{1}&\sigma _{2}\\0&\sigma _{0}&\sigma _{1}\end{vmatrix}}.}]

#### General case

[[edit][48]]

The intersection product between any pair of Schubert classes σ a, σ b {\displaystyle \sigma _{\mathbf {a} },\sigma _{\mathbf {b} }}[image: {\displaystyle \sigma _{\mathbf {a} },\sigma _{\mathbf {b} }}] is given by

σ a σ b = ∑ c c a b c σ c, {\displaystyle \sigma _{\mathbf {a} }\sigma _{\mathbf {b} }=\sum _{\mathbf {c} }c_{\mathbf {a} \mathbf {b} }^{\mathbf {c} }\sigma _{\mathbf {c} },}[image: {\displaystyle \sigma _{\mathbf {a} }\sigma _{\mathbf {b} }=\sum _{\mathbf {c} }c_{\mathbf {a} \mathbf {b} }^{\mathbf {c} }\sigma _{\mathbf {c} },}]

where { c a b c } {\displaystyle \{c_{\mathbf {a} \mathbf {b} }^{\mathbf {c} }\}}[image: {\displaystyle \{c_{\mathbf {a} \mathbf {b} }^{\mathbf {c} }\}}] are the [Littlewood-Richardson][49] coefficients. [5] The **Pieri formula**is a special case of this, when b = ( b, 0, …, 0) {\displaystyle \mathbf {b} =(b,0,\dots ,0)}[image: {\displaystyle \mathbf {b} =(b,0,\dots ,0)}] has length ℓ ( b) = 1 {\displaystyle \ell (\mathbf {b} )=1}[image: {\displaystyle \ell (\mathbf {b} )=1}].

## Relation with Chern classes

[[edit][50]]

There is an easy description of the cohomology ring, or the Chow ring, of the Grassmannian G r ( k, V) {\displaystyle \mathbf {Gr} (k,V)}[image: {\displaystyle \mathbf {Gr} (k,V)}] using the Chern classes of two natural [vector bundles][51] over G r ( k, V) {\displaystyle \mathbf {Gr} (k,V)}[image: {\displaystyle \mathbf {Gr} (k,V)}]. We have the [exact sequence][52] of vector bundles over G r ( k, V) {\displaystyle \mathbf {Gr} (k,V)}[image: {\displaystyle \mathbf {Gr} (k,V)}]

0 → T → V _ → Q → 0 {\displaystyle 0\to T\to {\underline {V}}\to Q\to 0}[image: {\displaystyle 0\to T\to {\underline {V}}\to Q\to 0}]

where T {\displaystyle T}[image: {\displaystyle T}] is the **tautological bundle**whose fiber, over any element w ∈ G r ( k, V) {\displaystyle w\in \mathbf {Gr} (k,V)}[image: {\displaystyle w\in \mathbf {Gr} (k,V)}] is the subspace w ⊂ V {\displaystyle w\subset V}[image: {\displaystyle w\subset V}] itself, V _:= G r ( k, V) × V {\displaystyle \,{\underline {V}}:=\mathbf {Gr} (k,V)\times V}[image: {\displaystyle \,{\underline {V}}:=\mathbf {Gr} (k,V)\times V}] is the trivial vector bundle of rank n {\displaystyle n}[image: {\displaystyle n}], with V {\displaystyle V}[image: {\displaystyle V}] as fiber and Q {\displaystyle Q}[image: {\displaystyle Q}] is the quotient vector bundle of rank n − k {\displaystyle n-k}[image: {\displaystyle n-k}], with V / w {\displaystyle V/w}[image: {\displaystyle V/w}] as fiber. The Chern classes of the bundles T {\displaystyle T}[image: {\displaystyle T}] and Q {\displaystyle Q}[image: {\displaystyle Q}] are

c i ( T) = ( − 1) i σ ( 1) i, {\displaystyle c_{i}(T)=(-1)^{i}\sigma _{(1)^{i}},}[image: {\displaystyle c_{i}(T)=(-1)^{i}\sigma _{(1)^{i}},}]

where ( 1) i {\displaystyle (1)^{i}}[image: {\displaystyle (1)^{i}}] is the partition whose Young diagram consists of a single column of length i {\displaystyle i}[image: {\displaystyle i}] and

c i ( Q) = σ i. {\displaystyle c_{i}(Q)=\sigma _{i}.}[image: {\displaystyle c_{i}(Q)=\sigma _{i}.}]

The tautological sequence then gives the presentation of the Chow ring as

A ∗ ( G r ( k, V)) = Z [c 1 ( T), …, c k ( T), c 1 ( Q), …, c n − k ( Q)] ( c ( T) c ( Q) − 1). {\displaystyle A^{*}(\mathbf {Gr} (k,V))={\frac {\mathbb {Z} [c_{1}(T),\ldots ,c_{k}(T),c_{1}(Q),\ldots ,c_{n-k}(Q)]}{(c(T)c(Q)-1)}}.}[image: {\displaystyle A^{*}(\mathbf {Gr} (k,V))={\frac {\mathbb {Z} [c_{1}(T),\ldots ,c_{k}(T),c_{1}(Q),\ldots ,c_{n-k}(Q)]}{(c(T)c(Q)-1)}}.}]

## Gr(2,4)

[[edit][53]]

One of the classical examples analyzed is the Grassmannian G r ( 2, 4) {\displaystyle \mathbf {Gr} (2,4)}[image: {\displaystyle \mathbf {Gr} (2,4)}] since it parameterizes lines in P 3 {\displaystyle \mathbb {P} ^{3}}[image: {\displaystyle \mathbb {P} ^{3}}]. Using the Chow ring A ∗ ( G r ( 2, 4)) {\displaystyle A^{*}(\mathbf {Gr} (2,4))}[image: {\displaystyle A^{*}(\mathbf {Gr} (2,4))}], Schubert calculus can be used to compute the number of lines on a [cubic surface][54]. [4]

### Chow ring

[[edit][55]]

The Chow ring has the presentation

A ∗ ( G r ( 2, 4)) = Z [σ 1, σ 1, 1, σ 2] ( ( 1 − σ 1 + σ 1, 1) ( 1 + σ 1 + σ 2) − 1) {\displaystyle A^{*}(\mathbf {Gr} (2,4))={\frac {\mathbb {Z} [\sigma _{1},\sigma _{1,1},\sigma _{2}]}{((1-\sigma _{1}+\sigma _{1,1})(1+\sigma _{1}+\sigma _{2})-1)}}}[image: {\displaystyle A^{*}(\mathbf {Gr} (2,4))={\frac {\mathbb {Z} [\sigma _{1},\sigma _{1,1},\sigma _{2}]}{((1-\sigma _{1}+\sigma _{1,1})(1+\sigma _{1}+\sigma _{2})-1)}}}]

and as a graded Abelian group [6] it is given by

A 0 ( G r ( 2, 4)) = Z ⋅ 1 A 2 ( G r ( 2, 4)) = Z ⋅ σ 1 A 4 ( G r ( 2, 4)) = Z ⋅ σ 2 ⊕ Z ⋅ σ 1, 1 A 6 ( G r ( 2, 4)) = Z ⋅ σ 2, 1 A 8 ( G r ( 2, 4)) = Z ⋅ σ 2, 2 {\displaystyle {\begin{aligned}A^{0}(\mathbf {Gr} (2,4))&=\mathbb {Z} \cdot 1\\A^{2}(\mathbf {Gr} (2,4))&=\mathbb {Z} \cdot \sigma _{1}\\A^{4}(\mathbf {Gr} (2,4))&=\mathbb {Z} \cdot \sigma _{2}\oplus \mathbb {Z} \cdot \sigma _{1,1}\\A^{6}(\mathbf {Gr} (2,4))&=\mathbb {Z} \cdot \sigma _{2,1}\\A^{8}(\mathbf {Gr} (2,4))&=\mathbb {Z} \cdot \sigma _{2,2}\\\end{aligned}}}[image: {\displaystyle {\begin{aligned}A^{0}(\mathbf {Gr} (2,4))&=\mathbb {Z} \cdot 1\\A^{2}(\mathbf {Gr} (2,4))&=\mathbb {Z} \cdot \sigma _{1}\\A^{4}(\mathbf {Gr} (2,4))&=\mathbb {Z} \cdot \sigma _{2}\oplus \mathbb {Z} \cdot \sigma _{1,1}\\A^{6}(\mathbf {Gr} (2,4))&=\mathbb {Z} \cdot \sigma _{2,1}\\A^{8}(\mathbf {Gr} (2,4))&=\mathbb {Z} \cdot \sigma _{2,2}\\\end{aligned}}}]

### Lines on a cubic surface

[[edit][56]]

Recall that a line in P 3 {\displaystyle \mathbb {P} ^{3}}[image: {\displaystyle \mathbb {P} ^{3}}] gives a dimension 2 {\displaystyle 2}[image: {\displaystyle 2}] subspace of A 4 {\displaystyle \mathbb {A} ^{4}}[image: {\displaystyle \mathbb {A} ^{4}}], hence an element of G ( 1, 3) ≅ G r ( 2, 4) {\displaystyle \mathbb {G} (1,3)\cong \mathbf {Gr} (2,4)}[image: {\displaystyle \mathbb {G} (1,3)\cong \mathbf {Gr} (2,4)}]. Also, the equation of a line can be given as a section of Γ ( G ( 1, 3), T ∗) {\displaystyle \Gamma (\mathbb {G} (1,3),T^{*})}[image: {\displaystyle \Gamma (\mathbb {G} (1,3),T^{*})}]. Since a cubic surface X {\displaystyle X}[image: {\displaystyle X}] is given as a generic homogeneous cubic polynomial, this is given as a generic section s ∈ Γ ( G ( 1, 3), Sym 3 ( T ∗)) {\displaystyle s\in \Gamma (\mathbb {G} (1,3),{\text{Sym}}^{3}(T^{*}))}[image: {\displaystyle s\in \Gamma (\mathbb {G} (1,3),{\text{Sym}}^{3}(T^{*}))}]. A line L ⊂ P 3 {\displaystyle L\subset \mathbb {P} ^{3}}[image: {\displaystyle L\subset \mathbb {P} ^{3}}] is a subvariety of X {\displaystyle X}[image: {\displaystyle X}] [if and only if][57] the section vanishes on [L] ∈ G ( 1, 3) {\displaystyle [L]\in \mathbb {G} (1,3)}[image: {\displaystyle [L]\in \mathbb {G} (1,3)}]. Therefore, the [Euler class][58] of Sym 3 ( T ∗) {\displaystyle {\text{Sym}}^{3}(T^{*})}[image: {\displaystyle {\text{Sym}}^{3}(T^{*})}] can be integrated over G ( 1, 3) {\displaystyle \mathbb {G} (1,3)}[image: {\displaystyle \mathbb {G} (1,3)}] to get the number of points where the generic section vanishes on G ( 1, 3) {\displaystyle \mathbb {G} (1,3)}[image: {\displaystyle \mathbb {G} (1,3)}]. In order to get the Euler class, the total Chern class of T ∗ {\displaystyle T^{*}}[image: {\displaystyle T^{*}}] must be computed, which is given as

c ( T ∗) = 1 + σ 1 + σ 1, 1 {\displaystyle c(T^{*})=1+\sigma _{1}+\sigma _{1,1}}[image: {\displaystyle c(T^{*})=1+\sigma _{1}+\sigma _{1,1}}]

The splitting formula then reads as the formal equation

c ( T ∗) = ( 1 + α) ( 1 + β) = 1 + α + β + α ⋅ β, {\displaystyle {\begin{aligned}c(T^{*})&=(1+\alpha )(1+\beta )\\&=1+\alpha +\beta +\alpha \cdot \beta \end{aligned}},}[image: {\displaystyle {\begin{aligned}c(T^{*})&=(1+\alpha )(1+\beta )\\&=1+\alpha +\beta +\alpha \cdot \beta \end{aligned}},}]

where c ( L) = 1 + α {\displaystyle c({\mathcal {L}})=1+\alpha }[image: {\displaystyle c({\mathcal {L}})=1+\alpha }] and c ( M) = 1 + β {\displaystyle c({\mathcal {M}})=1+\beta }[image: {\displaystyle c({\mathcal {M}})=1+\beta }] for formal line bundles L, M {\displaystyle {\mathcal {L}},{\mathcal {M}}}[image: {\displaystyle {\mathcal {L}},{\mathcal {M}}}]. The splitting equation gives the relations

σ 1 = α + β {\displaystyle \sigma _{1}=\alpha +\beta }[image: {\displaystyle \sigma _{1}=\alpha +\beta }] and σ 1, 1 = α ⋅ β {\displaystyle \sigma _{1,1}=\alpha \cdot \beta }[image: {\displaystyle \sigma _{1,1}=\alpha \cdot \beta }].

Since Sym 3 ( T ∗) {\displaystyle {\text{Sym}}^{3}(T^{*})}[image: {\displaystyle {\text{Sym}}^{3}(T^{*})}] can be viewed as the direct sum of formal line bundles

Sym 3 ( T ∗) = L ⊗ 3 ⊕ ( L ⊗ 2 ⊗ M) ⊕ ( L ⊗ M ⊗ 2) ⊕ M ⊗ 3 {\displaystyle {\text{Sym}}^{3}(T^{*})={\mathcal {L}}^{\otimes 3}\oplus ({\mathcal {L}}^{\otimes 2}\otimes {\mathcal {M}})\oplus ({\mathcal {L}}\otimes {\mathcal {M}}^{\otimes 2})\oplus {\mathcal {M}}^{\otimes 3}}[image: {\displaystyle {\text{Sym}}^{3}(T^{*})={\mathcal {L}}^{\otimes 3}\oplus ({\mathcal {L}}^{\otimes 2}\otimes {\mathcal {M}})\oplus ({\mathcal {L}}\otimes {\mathcal {M}}^{\otimes 2})\oplus {\mathcal {M}}^{\otimes 3}}]

whose total Chern class is

c ( Sym 3 ( T ∗)) = ( 1 + 3 α) ( 1 + 2 α + β) ( 1 + α + 2 β) ( 1 + 3 β), {\displaystyle c({\text{Sym}}^{3}(T^{*}))=(1+3\alpha )(1+2\alpha +\beta )(1+\alpha +2\beta )(1+3\beta ),}[image: {\displaystyle c({\text{Sym}}^{3}(T^{*}))=(1+3\alpha )(1+2\alpha +\beta )(1+\alpha +2\beta )(1+3\beta ),}]

it follows that

c 4 ( Sym 3 ( T ∗)) = 3 α ( 2 α + β) ( α + 2 β) 3 β = 9 α β ( 2 ( α + β) 2 + α β) = 9 σ 1, 1 ( 2 σ 1 2 + σ 1, 1) = 27 σ 2, 2, {\displaystyle {\begin{aligned}c_{4}({\text{Sym}}^{3}(T^{*}))&=3\alpha (2\alpha +\beta )(\alpha +2\beta )3\beta \\&=9\alpha \beta (2(\alpha +\beta )^{2}+\alpha \beta )\\&=9\sigma _{1,1}(2\sigma _{1}^{2}+\sigma _{1,1})\\&=27\sigma _{2,2}\,,\end{aligned}}}[image: {\displaystyle {\begin{aligned}c_{4}({\text{Sym}}^{3}(T^{*}))&=3\alpha (2\alpha +\beta )(\alpha +2\beta )3\beta \\&=9\alpha \beta (2(\alpha +\beta )^{2}+\alpha \beta )\\&=9\sigma _{1,1}(2\sigma _{1}^{2}+\sigma _{1,1})\\&=27\sigma _{2,2}\,,\end{aligned}}}]

using the fact that

σ 1, 1 ⋅ σ 1 2 = σ 2, 1 σ 1 = σ 2, 2 {\displaystyle \sigma _{1,1}\cdot \sigma _{1}^{2}=\sigma _{2,1}\sigma _{1}=\sigma _{2,2}}[image: {\displaystyle \sigma _{1,1}\cdot \sigma _{1}^{2}=\sigma _{2,1}\sigma _{1}=\sigma _{2,2}}] and σ 1, 1 ⋅ σ 1, 1 = σ 2, 2. {\displaystyle \sigma _{1,1}\cdot \sigma _{1,1}=\sigma _{2,2}.}[image: {\displaystyle \sigma _{1,1}\cdot \sigma _{1,1}=\sigma _{2,2}.}]

Since σ 2, 2 {\displaystyle \sigma _{2,2}}[image: {\displaystyle \sigma _{2,2}}] is the top class, the integral is then

∫ G ( 1, 3) 27 σ 2, 2 = 27. {\displaystyle \int _{\mathbb {G} (1,3)}27\sigma _{2,2}=27.}[image: {\displaystyle \int _{\mathbb {G} (1,3)}27\sigma _{2,2}=27.}]

Therefore, there are 27 {\displaystyle 27}[image: {\displaystyle 27}] lines on a cubic surface.

## See also

[[edit][59]]

- [Enumerative geometry][5]
- [Chow ring][26]
- [Intersection theory][15]
- [Grassmannian][10]
- [Giambelli's formula][60]
- [Pieri's formula][61]
- [Chern class][62]
- [Quintic threefold][63]
- [Mirror symmetry conjecture][64]

## References

[[edit][65]]

1. 1 2 3 4 [Kleiman, S.L.][66]; [Laksov, Dan][67] (1972). "Schubert Calculus". *American Mathematical Monthly*. **79**(10). American Mathematical Society: 1061– 1082. [doi][68]: [10.1080/00029890.1972.11993188][69]. [ISSN][70] [0377-9017][71].
2. 1 2 3 4 [Fulton, William][72] (1997). *Young Tableaux. With Applications to Representation Theory and Geometry, Chapt. 9.4*. London Mathematical Society Student Texts. Vol. 35. Cambridge, U.K.: Cambridge University Press. [doi][68]: [10.1017/CBO9780511626241][73]. [ISBN][74] [9780521567244][75].
3. 1 2 [Fulton, William][72] (1998). *Intersection Theory*. Berlin, New York: [Springer-Verlag][76]. [ISBN][74] [978-0-387-98549-7][77]. [MR][78] [1644323][79].
4. 1 2 3**[3264 and All That][80] (PDF). pp. 132, section 4.1, 200, section 6.2.1.
5. ↑ [Fulton, William][72] (1997). *Young Tableaux. With Applications to Representation Theory and Geometry, Chapt. 5*. London Mathematical Society Student Texts. Vol. 35. Cambridge, U.K.: Cambridge University Press. [doi][68]: [10.1017/CBO9780511626241][73]. [ISBN][74] [9780521567244][75].
6. ↑ [Katz, Sheldon][81]. *Enumerative Geometry and String Theory*. p. 96.

- Summer school notes [http://homepages.math.uic.edu/~coskun/poland.html][82]
- [Phillip Griffiths][83] and [Joseph Harris][84] (1978), *Principles of Algebraic Geometry*, Chapter 1.5
- [Kleiman, Steven][66] (1976). "Rigorous foundations of Schubert's enumerative calculus". In [Felix E. Browder][85] (ed.). *Mathematical Developments Arising from Hilbert Problems*. [Proceedings of Symposia in Pure Mathematics][86]. Vol. XXVIII.2. [American Mathematical Society][87]. pp. 445– 482. [ISBN][74] [0-8218-1428-1][88].
- [Steven Kleiman][66] and [Dan Laksov][67] (1972). ["Schubert calculus"][89] (PDF). *[American Mathematical Monthly][90]*. **79**(10): 1061– 1082. [doi][68]: [10.2307/2317421][91]. [JSTOR][92] [2317421][93]. Archived from [the original][94] (PDF) on 2022-01-20. Retrieved 2014-03-15.
- Sottile, Frank (2001) [1994], ["Schubert calculus"][95], *[Encyclopedia of Mathematics][96]*, EMS Press
- [David Eisenbud][97] and [Joseph Harris][84] (2016), "3264 and All That: A Second Course in Algebraic Geometry".
- [Fulton, William][72] (1997). *Young Tableaux. With Applications to Representation Theory and Geometry, Chapts. 5 and 9.4*. London Mathematical Society Student Texts. Vol. 35. Cambridge, U.K.: Cambridge University Press. [doi][68]: [10.1017/CBO9780511626241][73]. [ISBN][74] [9780521567244][75].
- [Fulton, William][72] (1998). *Intersection Theory*. Berlin, New York: [Springer-Verlag][76]. [ISBN][74] [978-0-387-98549-7][77]. [MR][78] [1644323][79].

Retrieved from " [https://en.wikipedia.org/w/index.php?title=Schubert_calculus&oldid=1363311537][98] "

[Categories][99]:

- [Algebraic geometry][100]
- [Topology of homogeneous spaces][101]

Hidden categories:

- [Articles with short description][102]
- [Short description matches Wikidata][103]
- [CS1: long volume value][104]
- [Template SpringerEOM with broken ref][105]

Search

Schubert calculus

3 languages Add topic


## Links

[1]: https://en.wikipedia.org/wiki/Mathematics
[2]: https://en.wikipedia.org/wiki/Algebraic_geometry
[3]: https://en.wikipedia.org/wiki/Hermann_Schubert
[4]: https://en.wikipedia.org/wiki/Projective_geometry
[5]: https://en.wikipedia.org/wiki/Enumerative_geometry
[6]: https://en.wikipedia.org/wiki/Hilbert's_problems
[7]: https://en.wikipedia.org/wiki/Characteristic_class
[8]: https://en.wikipedia.org/wiki/Generalized_cohomology_theories
[9]: https://en.wikipedia.org/wiki/Locally_closed
[10]: https://en.wikipedia.org/wiki/Grassmannian
[11]: https://en.wikipedia.org/wiki/Incidence_(geometry)
[12]: https://en.wikipedia.org/wiki/Linear_subspace
[13]: https://en.wikipedia.org/wiki/Flag_(linear_algebra)
[14]: https://en.wikipedia.org/wiki/Schubert_variety
[15]: https://en.wikipedia.org/wiki/Intersection_theory
[16]: https://en.wikipedia.org/wiki/Cohomology_ring
[17]: https://en.wikipedia.org/wiki/Cohomology_class
[18]: https://en.wikipedia.org/wiki/Finite_set
[19]: https://en.wikipedia.org/wiki/Schubert_varieties
[20]: https://en.wikipedia.org/wiki/Homogeneous_space
[21]: https://en.wikipedia.org/wiki/General_linear_group
[22]: https://en.wikipedia.org/wiki/Bruhat_decomposition
[23]: https://en.wikipedia.org/wiki/Borel_subgroup
[24]: https://en.wikipedia.org/wiki/Block_matrix
[25]: /w/index.php?title=Schubert_calculus&amp;action=edit&amp;section=1
[26]: https://en.wikipedia.org/wiki/Chow_ring
[27]: https://en.wikipedia.org/wiki/Flag_manifold
[28]: https://en.wikipedia.org/wiki/Partition_(number_theory)
[29]: https://en.wikipedia.org/wiki/Young_diagram
[30]: https://en.wikipedia.org/wiki/Zariski_topology
[31]: https://en.wikipedia.org/wiki/Cellular_homology
[32]: https://en.wikipedia.org/wiki/Linear_span
[33]: https://en.wikipedia.org/wiki/Giambelli_formula
[34]: /w/index.php?title=Schubert_calculus&amp;action=edit&amp;section=2
[35]: https://en.wikipedia.org/wiki/Echelon_form
[36]: /w/index.php?title=Schubert_calculus&amp;action=edit&amp;section=3
[37]: /w/index.php?title=Schubert_calculus&amp;action=edit&amp;section=4
[38]: /w/index.php?title=Schubert_calculus&amp;action=edit&amp;section=5
[39]: /w/index.php?title=Schubert_calculus&amp;action=edit&amp;section=6
[40]: /w/index.php?title=Schubert_calculus&amp;action=edit&amp;section=7
[41]: https://en.wikipedia.org/wiki/Mario_Pieri
[42]: https://en.wikipedia.org/wiki/Giovanni_Giambelli
[43]: /w/index.php?title=Schubert_calculus&amp;action=edit&amp;section=8
[44]: https://en.wikipedia.org/wiki/Pieri_formula
[45]: /w/index.php?title=Schubert_calculus&amp;action=edit&amp;section=9
[46]: https://en.wikipedia.org/wiki/Schur_polynomials#Jacobi_Trudi_identities
[47]: https://en.wikipedia.org/wiki/Schur_polynomial
[48]: /w/index.php?title=Schubert_calculus&amp;action=edit&amp;section=10
[49]: https://en.wikipedia.org/wiki/Littlewood-Richardson_rule
[50]: /w/index.php?title=Schubert_calculus&amp;action=edit&amp;section=11
[51]: https://en.wikipedia.org/wiki/Vector_bundle
[52]: https://en.wikipedia.org/wiki/Exact_sequence
[53]: /w/index.php?title=Schubert_calculus&amp;action=edit&amp;section=12
[54]: https://en.wikipedia.org/wiki/Cubic_surface
[55]: /w/index.php?title=Schubert_calculus&amp;action=edit&amp;section=13
[56]: /w/index.php?title=Schubert_calculus&amp;action=edit&amp;section=14
[57]: https://en.wikipedia.org/wiki/If_and_only_if
[58]: https://en.wikipedia.org/wiki/Euler_class
[59]: /w/index.php?title=Schubert_calculus&amp;action=edit&amp;section=15
[60]: https://en.wikipedia.org/wiki/Giambelli's_formula
[61]: https://en.wikipedia.org/wiki/Pieri's_formula
[62]: https://en.wikipedia.org/wiki/Chern_class
[63]: https://en.wikipedia.org/wiki/Quintic_threefold
[64]: https://en.wikipedia.org/wiki/Mirror_symmetry_conjecture
[65]: /w/index.php?title=Schubert_calculus&amp;action=edit&amp;section=16
[66]: https://en.wikipedia.org/wiki/Steven_Kleiman
[67]: https://en.wikipedia.org/wiki/Dan_Laksov
[68]: https://en.wikipedia.org/wiki/Doi_(identifier)
[69]: https://doi.org/10.1080%2F00029890.1972.11993188
[70]: https://en.wikipedia.org/wiki/ISSN_(identifier)
[71]: https://search.worldcat.org/issn/0377-9017
[72]: https://en.wikipedia.org/wiki/William_Fulton_(mathematician)
[73]: https://doi.org/10.1017%2FCBO9780511626241
[74]: https://en.wikipedia.org/wiki/ISBN_(identifier)
[75]: https://en.wikipedia.org/wiki/Special:BookSources/9780521567244
[76]: https://en.wikipedia.org/wiki/Springer-Verlag
[77]: https://en.wikipedia.org/wiki/Special:BookSources/978-0-387-98549-7
[78]: https://en.wikipedia.org/wiki/MR_(identifier)
[79]: https://mathscinet.ams.org/mathscinet-getitem?mr=1644323
[80]: https://scholar.harvard.edu/files/joeharris/files/000-final-3264.pdf
[81]: https://en.wikipedia.org/wiki/Sheldon_Katz
[82]: http://homepages.math.uic.edu/~coskun/poland.html
[83]: https://en.wikipedia.org/wiki/Phillip_Griffiths
[84]: https://en.wikipedia.org/wiki/Joe_Harris_(mathematician)
[85]: https://en.wikipedia.org/wiki/Felix_Browder
[86]: https://en.wikipedia.org/wiki/Proceedings_of_Symposia_in_Pure_Mathematics
[87]: https://en.wikipedia.org/wiki/American_Mathematical_Society
[88]: https://en.wikipedia.org/wiki/Special:BookSources/0-8218-1428-1
[89]: https://web.archive.org/web/20220120134126/http://www.mat.unimi.it/users/bertolin/GeometriaAlgebrica%20proiettiva/Kleiman-Laksov.pdf
[90]: https://en.wikipedia.org/wiki/American_Mathematical_Monthly
[91]: https://doi.org/10.2307%2F2317421
[92]: https://en.wikipedia.org/wiki/JSTOR_(identifier)
[93]: https://www.jstor.org/stable/2317421
[94]: http://www.mat.unimi.it/users/bertolin/GeometriaAlgebrica%20proiettiva/Kleiman-Laksov.pdf
[95]: https://www.encyclopediaofmath.org/index.php?title=Schubert_calculus
[96]: https://en.wikipedia.org/wiki/Encyclopedia_of_Mathematics
[97]: https://en.wikipedia.org/wiki/David_Eisenbud
[98]: https://en.wikipedia.org/w/index.php?title=Schubert_calculus&amp;oldid=1363311537
[99]: /wiki/Help:Category
[100]: /wiki/Category:Algebraic_geometry
[101]: /wiki/Category:Topology_of_homogeneous_spaces
[102]: /wiki/Category:Articles_with_short_description
[103]: /wiki/Category:Short_description_matches_Wikidata
[104]: /wiki/Category:CS1:_long_volume_value
[105]: /wiki/Category:Template_SpringerEOM_with_broken_ref
