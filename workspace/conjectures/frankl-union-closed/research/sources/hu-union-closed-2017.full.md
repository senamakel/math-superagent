<!-- source: https://arxiv.org/html/1706.06167 | converted from HTML -->

On the Union-Closed Sets Conjecture

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:1706.06167v1 [math.CO] 19 Jun 2017

# On the Union-Closed Sets Conjecture

YINING HU Affiliation: CNRS, Institut de Mathématiques de Jussieu-PRG Affiliation: Université Pierre et Marie Curie, Case 247 Affiliation: 4 Place Jussieu Affiliation: F-75252 Paris Cedex 05 (France) Email: [yining.hu@imj-prg.fr][3]

## 1 Introduction

A collection of sets 𝒜 \mathcal{A} is *union-closed*if S, T ∈ 𝒜 S,T\in\mathcal{A} implies that S ∪ T ∈ 𝒜 S\cup T\in\mathcal{A}. The following conjecture, often attributed to Peter Frankl, dates back to 1979. Recently Blinovsky [1] and Schäge [10] claim to have proven the conjecture, but their proofs seem to be false. We refer the interested reader to a comprehensive overview of this conjecture by Bruhn and Schaudt [3].

###### Union-closed sets Conjecture.

Let 𝒜 \mathcal{A} be a union-closed finite collection of sets, containing at least one non-empty set, then there is an element which belongs to at least half of the sets in 𝒜 \mathcal{A}.

Here are some notation and convention that we will adopt in this article: We use abbreviated notation for collections of sets of integers. For example, { { 1, 2 }, { 1, 2, 3 }, { 3, 4 } } \{\{1,2\},\{1,2,3\},\{3,4\}\} denoted by { 12,123, 34 } \{12,123,34\}. The set { 1, 2, …, m } \{1,2,...,m\} is denoted by [m] [m], the power set of [m] [m] is denoted by 𝒫 ⁡ ( m) \mathcal{P}(m). For convenience we can always assume that a union-closed finite collection 𝒜 \mathcal{A} on n n elements is a subset of 𝒫 ⁡ ( n) \mathcal{P}(n). The *universe*U ⁡ ( 𝒜) U(\mathcal{A}) is the set of all elements that appear in the member sets of 𝒜 \mathcal{A}, that is, ∪ A ∈ 𝒜 A \cup_{A\in\mathcal{A}}A. 𝒜 \mathcal{A} is *separating*if for any two distinct elements in U ⁡ ( A) U(A), there is a set in 𝒜 \mathcal{A} that contains one of them but does not contain the other. In the conjecture we could also require the collection to be separating, but this does not make a difference. For an element a ∈ U ⁡ ( A) a\in U(A), its frequency in 𝒜 \mathcal{A} will be denoted by | a | 𝒜 |a|_{\mathcal{A}}. The sub-collection of sets containing a a will be noted by 𝒜 a \mathcal{A}_{a}, and its complement in 𝒜 \mathcal{A} by 𝒜 a ¯ \mathcal{A}_{\bar{a}}. Both 𝒜 a \mathcal{A}_{a} and 𝒜 a ¯ \mathcal{A}_{\bar{a}} are still union-closed sets. An element b b is said to *dominate*another element c c in 𝒜 \mathcal{A} if b b occurs in every set in 𝒜 \mathcal{A} that contains c c, using the notation above, this is equivalent to saying c ∉ U ⁡ ( 𝒜 b ¯) c\notin U(\mathcal{A}_{\bar{b}}). A set T ∈ 𝒜 T\in\mathcal{A} is said to be a *basis set*if it is not the union of other sets in 𝒜 \mathcal{A}. If we remove a basis set from 𝒜 \mathcal{A}, the rest is still closed by union.

## 2 On a minimal counterexample

In all this section, let 𝒜 \mathcal{A} be a union-closed, separating collection, where U ⁡ ( 𝒜) = { 1, …, m } U(\mathcal{A})=\{1,...,m\} with | 1 | 𝒜 ≤ … ≤ | m | 𝒜 |1|_{\mathcal{A}}\leq...\leq|m|_{\mathcal{A}}. Roberts and Simpson( [9]) have proven if 𝒜 \mathcal{A} is a counterexample with the least number of sets, then | 𝒜 | ≥ 4 ​ m + 1 |\mathcal{A}|\geq 4m+1. Here we give an alternative proof of their result. We need to define some other notions.

For all elements i i, we define the set

 | A i:= ∪ { A ∈ 𝒜 | i ∉ A } A, A_{i}:=\cup_{\{A\in\mathcal{A}\;|\;i\notin A\}}A, |  |

This set contains all elements j j greater than i i, because by the assumption of separation and | i | 𝒜 ≤ | j | 𝒜 |i|_{\mathcal{A}}\leq|j|_{\mathcal{A}}, there exists a set in 𝒜 \mathcal{A} that contain j j but not i i. Thus 𝒜 \mathcal{A} contains a sub-collection 𝒮 = { A 0 = U ⁡ ( 𝒜), A 1, …, A m − 1 } \mathcal{S}=\{A_{0}=U(\mathcal{A}),A_{1},...,A_{m-1}\} whose structure can be represented by the following table, where “1” means that the element in the column is in the set in the row, “0” means that the element in the column is not in the set in the row, “?” means not determined.

 | 1 1 | 2 2 | 3 3 | … | m − 3 m-3 | m − 2 m-2 | m − 1 m-1 | m m |

A m − 1 A_{m-1} | ? | ? | ? | … | ? | ? | 0 | 1 |

A m − 2 A_{m-2} | ? | ? | ? | … | ? | 0 | 1 | 1 |

A m − 3 A_{m-3} | ? | ? | ? | … | 0 | 1 | 1 | 1 |

⋮ | ⋮ |  |  |  |  | ⋮ | ⋮ | ⋮ |

A 2 A_{2} | ? | 0 | 1 | … | 1 | 1 | 1 | 1 |

A 1 A_{1} | 0 | 1 | 1 | … | 1 | 1 | 1 | 1 |

A 0 A_{0} | 1 | 1 | 1 | … | 1 | 1 | 1 | 1 |

If 𝒜 \mathcal{A} is a counterexample of the union-closed sets conjecture with the least number of sets, then we know that 𝒜 m ¯ \mathcal{A}_{\bar{m}}, which is also closed by union and has smaller cardinality than 𝒜 \mathcal{A}, satisfies the conjecture, thus containing an element that appears in at least half of the sets in 𝒜 m ¯ \mathcal{A}_{\bar{m}}. It would be nice if we knew that the most frequent element in 𝒜 m ¯ \mathcal{A}_{\bar{m}} is also frequent in 𝒮 \mathcal{S}, because then we would know that the maximal frequency in 𝒜 \mathcal{A} is at least the sum of its frequencies in 𝒜 m ¯ \mathcal{A}_{\bar{m}} and 𝒮 \mathcal{S}. Indeed we have such a result, which is the corollary of the following lemma:

###### Lemma 1.

For i ∈ { 1, …, m − 1 } i\in\{1,...,m-1\}, if | i | 𝒮 < m − 1 |i|_{\mathcal{S}}<m-1, then there exists an element in { 1, …, m − 1 } \{1,...,m-1\} with frequency m − 1 m-1 in 𝒮 {\mathcal{S}} that dominates i i in 𝒜 \mathcal{A}.

###### Proof.

If | i | 𝒮 < m − 1 |i|_{\mathcal{S}}<m-1, then there exists an element j j in { i + 1, …, m − 1 } \{i+1,...,m-1\} such that i ∉ A j i\notin A_{j}. This means that i i is dominated by j j in 𝒜 \mathcal{A}, as A j A_{j} is by definition the union of sets in 𝒜 j ¯ \mathcal{A}_{\bar{j}}. If | j | 𝒮 = m − 1 |j|_{\mathcal{S}}=m-1, we are done. If not, we apply the above process to j j and iterate until we find an element k k in { 1, …, m − 1 } \{1,...,m-1\} with | k | 𝒮 = m − 1 |k|_{\mathcal{S}}=m-1 that dominates i i.

∎

###### Corollary 1.

Among the elements of maximal frequency in a non-empty sub-collection of 𝒜 \mathcal{A}, there exists one with frequency m − 1 m-1 in 𝒮 \mathcal{S}.

###### Proof.

Let ℬ \mathcal{B} be a non-empty sub-collection of 𝒜 \mathcal{A}, and i i be an element of maximal frequency in ℬ \mathcal{B}. If i i appears less than m − 1 m-1 times in 𝒮 \mathcal{S}, then there exists an element j j in { 1, …, m − 1 } \{1,...,m-1\} with frequency | j | 𝒮 = m − 1 |j|_{\mathcal{S}}=m-1 that dominates i i in 𝒜 \mathcal{A}, thus in ℬ \mathcal{B}. ∎

If 𝒜 \mathcal{A} is a minimal counterexample of the conjecture, then | 𝒜 | = 2 ​ n + 1 |\mathcal{A}|=2n+1 for some integer n n. In fact, if ℬ \mathcal{B} is a counterexample with | ℬ | = 2 ​ n + 2 |\mathcal{B}|=2n+2, then we know that the maximal frequency in ℬ \mathcal{B} is less than n + 1 n+1. If we remove a basis set from ℬ \mathcal{B}, then we get a union-closed collection with 2 ​ n + 1 2n+1 sets whose maximal frequency is still less than n + 1 n+1, which makes a yet smaller counterexample. If a a is an element of maximal frequency in 𝒜 \mathcal{A}, then | a | 𝒜 = n |a|_{\mathcal{A}}=n. This is because if the frequency of a a were less than n n, then we could remove a basis set from 𝒜 \mathcal{A} and get a smaller counterexample.

Now we know that if 𝒜 \mathcal{A} is a minimal counterexample, then in 𝒜 m ¯ \mathcal{A}_{\bar{m}}, there are elements that occur in at least half of the sets, and among these elements, there is at least one with frequency m − 1 m-1 in 𝒮 \mathcal{S}. Thus 𝒜 m \mathcal{A}_{m} must contain more than 2 ​ m − 2 2m-2 elements for 𝒜 \mathcal{A} to be a counterexample. This, combined with the discussion above, leads to the following theorem:

###### Theorem 1.

If a separating, union-closed collection 𝒜 \mathcal{A} is a counterexample of the union-closed sets conjecture of minimal cardinality, then | 𝒜 | ≥ 4 ​ m − 1 |\mathcal{A}|\geq 4m-1, where m = | U ⁡ ( 𝒜) | m=|U(\mathcal{A})|.

###### Proof.

As 𝒜 \mathcal{A} is a minimal counterexample, | 𝒜 | = 2 ​ n + 1 |\mathcal{A}|=2n+1 for some integer n. 𝒜 m ¯ \mathcal{A}_{\bar{m}} is union-closed and | 𝒜 m ¯ | = n + 1 |\mathcal{A}_{\bar{m}}|=n+1, therefore the maximal frequency in 𝒜 m ¯ \mathcal{A}_{\bar{m}} is at least n + 1 2 \frac{n+1}{2} by the minimality of 𝒜 \mathcal{A}. By Corollary 1, there exists a ∈ U ⁡ ( 𝒜) a\in U(\mathcal{A}) such that | a | 𝒜 m ¯ ≥ n + 1 2 |a|_{\mathcal{A}_{\bar{m}}}\geq\frac{n+1}{2} and | a | 𝒮 = m − 1 |a|_{\mathcal{S}}=m-1. Also we must have | a | 𝒜 m ¯ + | ​ a | S ≤ | a | 𝒜 ≤ n |a|_{\mathcal{A}_{\bar{m}}}+|a|_{S}\leq|a|_{\mathcal{A}}\leq n, i.e., n + 1 2 + m − 1 ≤ n \frac{n+1}{2}+m-1\leq n. Therefore n ≥ 2 ​ m − 1 n\geq 2m-1 and 2 ​ n + 1 ≥ 4 ​ m − 1 2n+1\geq 4m-1. ∎

Bošnjak and Marković [2] have proved that a minimal counterexample has m ≥ 12 m\geq 12 this number is improved by Živković and Vučković [11] to 13. Thus Theorem 1 implies that a minimal counterexample contains at least 51 sets. We always assume separation when we talk about the relation of the size of the counterexample and the size of the universe, so that we could not just duplicate elements and make the size of the universe arbitrarily big with essentially the same collection.

## 3 The ε \varepsilon -union-closed sets conjecture

As the union-closed sets conjecture has proven to be a difficult problem, we may want to try to prove the following weakened conjecture:

###### ε \varepsilon -Union-Closed Sets Conjecture 1.

There exists ε > 0 \varepsilon>0 such that for all union-closed finite collection of sets 𝒜 \mathcal{A} containing at least one non-empty set, there is an element which belongs to at least ε ⋅ | 𝒜 | \varepsilon\cdot|\mathcal{A}| of the sets in 𝒜 \mathcal{A}.

In the last section we have proven that if 𝒜 \mathcal{A} is a minimal counterexample of the union-closed sets conjecture, then | 𝒜 | ≥ 4 ⋅ | U ⁡ ( 𝒜) | − 1 |\mathcal{A}|\geq 4\cdot|U(\mathcal{A})|-1. For a counterexample that is not necessarily minimal, what do we know about the relation of the size of the collection and the size of the universe? From the construction of the sub-collection 𝒮 \mathcal{S} in the last section, we know that for any union-closed finite collection of sets ℬ \mathcal{B}, there is an element of frequency at least | U ⁡ ( ℬ) | |U(\mathcal{B})|. Thus the union-closed sets conjecture holds for all union-closed finite collections ℬ \mathcal{B} with | ℬ | ≤ 2 ⋅ | U ⁡ ( ℬ) | |\mathcal{B}|\leq 2\cdot|U(\mathcal{B})|. This condition is fairly easy to establish. But can we obtain a better bound, for example with 2 + ε ′ 2+\varepsilon^{\prime} instead of 2 2? There is reason to believe that this would not be easy, as it would imply the ε \varepsilon -union-closed sets conjecture:

###### Theorem 2.

Let c > 2 c>2. If the union-closed sets conjecture is true for all separating, union-closed finite collection 𝒜 \mathcal{A} with | 𝒜 | ≤ c ⋅ | U ⁡ ( 𝒜) | |\mathcal{A}|\leq c\cdot|U(\mathcal{A})|, then for all union closed families ℬ \mathcal{B}, there exists x ∈ U ⁡ ( ℬ) x\in U(\mathcal{B}) with | x | ℬ ≥ c − 2 2 ​ ( c − 1) ⋅ | U ⁡ ( ℬ) | |x|_{\mathcal{B}}\geq\frac{c-2}{2(c-1)}\cdot|U(\mathcal{B})|.

###### Proof.

Suppose that for c > 2 c>2, the union-closed sets conjecture is true for all separating, union-closed finite collection 𝒜 \mathcal{A} such that | 𝒜 | ≤ c ⋅ | U ( 𝒜 |) |\mathcal{A}|\leq c\cdot|U(\mathcal{A}|).

Let ℬ \mathcal{B} be a union-closed finite collection with | U ⁡ ( ℬ) | = m |U(\mathcal{B})|=m and | ℬ | = n |\mathcal{B}|=n. If n ≤ c ⋅ m n\leq c\cdot m then the conclusion is true. Suppose now that n > c ⋅ m n>c\cdot m. Let p p be a positive integer whose value will be made precise later. We construct another collection 𝒞 \mathcal{C} by adding p p new elements to U ⁡ ( ℬ) U(\mathcal{B}) and p p new sets to ℬ \mathcal{B}:

 | U ⁡ ( 𝒞):= U ⁡ ( ℬ) ∪ { x 1, …, x p }, U(\mathcal{C}):=U(\mathcal{B})\cup\{x_{1},...,x_{p}\}, |  |

 | 𝒞:= ℬ ∪ { U ( 𝒞) \ { x i } | i = 1, …, p − 1 } ∪ { U ( 𝒞) }. \mathcal{C}:=\mathcal{B}\cup\{U(\mathcal{C})\backslash\{x_{i}\}\;|\;i=1,...,p-1\}\cup\{U(\mathcal{C})\}. |  |

𝒞 \mathcal{C} is still a union-closed, separating collection. In order to apply the assumption to 𝒞 \mathcal{C}, we need p p to satisfy

 | | 𝒞 | | U ⁡ ( 𝒞) | = n + p m + p ≤ c, \frac{|\mathcal{C}|}{|U(\mathcal{C})|}=\frac{n+p}{m+p}\leq c, |  |

that is,

 | p ≥ n − c ​ m c − 1. p\geq\frac{n-cm}{c-1}. |  |

On the other hand, as we will see shortly after, we want p p to be as small as possible. So we choose

 | p = ⌈ n − c ​ m c − 1 ⌉ < n − c ​ m c − 1 + 1. p=\left\lceil\frac{n-cm}{c-1}\right\rceil<\frac{n-cm}{c-1}+1. |  |

Now by the assumption and the choice of p p, we know that there is an element in U ⁡ ( 𝒞) U(\mathcal{C}) that appears in at least ⌈ n + p 2 ⌉ \left\lceil\frac{n+p}{2}\right\rceil sets in 𝒞 \mathcal{C}. As n > p n>p, this element cannot be one of the p p added elements, so it is in U ⁡ ( ℬ) U(\mathcal{B}). Its frequency in ℬ \mathcal{B} is ⌈ n − p 2 ⌉ \left\lceil\frac{n-p}{2}\right\rceil. We have

 | n − p 2 ​ n \displaystyle\frac{n-p}{2n} | > n − n − c ​ m c − 1 − 1 2 ​ n \displaystyle>\frac{n-\frac{n-cm}{c-1}-1}{2n} |  |

 |  | = ( c − 1) ​ n − n + c ​ m − c + 1 2 ​ n ​ ( c − 1) \displaystyle=\frac{(c-1)n-n+cm-c+1}{2n(c-1)} |  |

 |  | > 1 2 − 1 2 ​ ( c − 1) \displaystyle>\frac{1}{2}-\frac{1}{2(c-1)} |  |

 |  | = c − 2 2 ​ ( c − 1), \displaystyle=\frac{c-2}{2(c-1)}, |  |

which ends the proof.

∎

## 4 A bound for the minimal maximal frequency

We define a function ϕ: ℕ ∗ → ℕ ∗ \phi:\mathbbm{N}^{*}\rightarrow\mathbbm{N}^{*}, where ϕ ⁡ ( n) \phi(n) is the minimum of maximal frequencies of union-closed collections over n n sets:

 | ϕ ⁡ ( n) = min 𝒜 ​ union-closed, ​ | 𝒜 | = n ⁡ max a ∈ U ⁡ ( 𝒜) ​ | a | 𝒜 \phi(n)=\min_{\scriptscriptstyle{\mathcal{A}\mbox{\tiny union-closed, }|\mathcal{A}|=n}}\max_{\scriptscriptstyle{a\in U(\mathcal{A})}}|a|_{\mathcal{A}} |  |

The union-closed sets conjecture can be expressed as ϕ ⁡ ( n) ≥ 1 2 ⋅ n \phi(n)\geq\frac{1}{2}\cdot n.

### 4.1 Renaud’s construction and boundary function

Renaud and Fitina [8] has conjectured that ϕ ⁡ ( n) \phi(n) is equal to Conway’s challenge sequence ( a ⁡ ( n)) (a(n)) defined as:

 | a ⁡ ( 1) = a ⁡ ( 2) = 1, a ⁡ ( n) = a ⁡ ( a ⁡ ( n − 1)) + a ⁡ ( n − a ⁡ ( n − 1)) a(1)=a(2)=1,\;\;a(n)=a(a(n-1))+a(n-a(n-1)) |  |

Mallows [4] has proved that the sequence ( a ⁡ ( n)) (a(n)) has the property that a ⁡ ( n) ≥ 1 2 ⋅ n a(n)\geq\frac{1}{2}\cdot n. We also know that a ⁡ ( n + 1) ∈ { a ⁡ ( n), a ⁡ ( n) + 1 } a(n+1)\in\{a(n),a(n)+1\}. Renaud and Fitina [8] have proved that ϕ ⁡ ( n) \phi(n) has the same property and that ϕ ⁡ ( n) ≤ a ⁡ ( n) \phi(n)\leq a(n) by constructing a union-closed collection with maximal frequency a ⁡ ( n) a(n) for all n ≥ 2 n\geq 2.

Renaud [7] has calculated the values of ϕ ⁡ ( n) \phi(n) for n = 1, …, 18 n=1,...,18. The values coincide with that of a ⁡ ( n) a(n). But at n = 23 n=23, he has found an counterexample [6]. Using abbreviated notation, the union-closed collection

 | 𝒫 ⁡ ( 4) ∪ { 12345, 1235, 1245, 1345, 2345, 125, 345 } \mathcal{P}(4)\cup\{12345,1235,1245,1345,2345,125,345\} |  |

has highest element frequency 13, whereas a ⁡ ( 23) = 14 a(23)=14.

Renaud [6] then defined another function β: ℕ ∗ → ℕ ∗ \beta:\mathbb{N}^{*}\rightarrow\mathbb{N}^{*} with the property ϕ ⁡ ( n) ≤ β ⁡ ( n) ≤ a ⁡ ( n) \phi(n)\leq\beta(n)\leq a(n), whose value corresponds to the maximal frequency of the union-closed collection ℬ ⁡ ( n) \mathcal{B}(n) of n n sets, constructed in the following way: let k k be an integer such that 2 k − 1 < n ≤ 2 k 2^{k-1}<n\leq 2^{k}. We obtain ℬ ⁡ ( n) \mathcal{B}(n) by deleting sets containing k k from 𝒫 ⁡ ( k) \mathcal{P}(k), following rules: a smaller set is always deleted before a larger set; sets of the same size are deleted in an order such that the frequency of the element 1, …, k − 1 1,...,k-1 in the remaining sets are “balanced”, that is, the difference of their frequencies is at most 1. Therefore if

 | n = 2 k − ∑ i = 1 r − 1 ( k − 1 i) − v n=2^{k}-\sum\limits_{i=1}^{r-1}\binom{k-1}{i}-v |  |

where 0 ≤ r ≤ k − 1 0\leq r\leq k-1 and 0 ≤ v < ( k − 1 r) 0\leq v<\binom{k-1}{r}, then

 | β ⁡ ( n) = 2 k − 1 − ∑ i = 1 r − 1 ( k − 2 i − 1) − ⌊ r ⋅ v k − 1 ⌋. \beta(n)=2^{k-1}-\sum\limits_{i=1}^{r-1}\binom{k-2}{i-1}-\left\lfloor\frac{r\cdot v}{k-1}\right\rfloor. |  |

For example ℬ ⁡ ( 23) = 𝒫 ⁡ ( 4) ∪ { 12345, 1235, 1245, 1345, 2345, 125, 345 } \mathcal{B}(23)=\mathcal{P}(4)\cup\{12345,1235,1245,1345,2345,125,345\} is the collection mentioned above, and β ⁡ ( 23) = 13 < 14 = α ⁡ ( 23) \beta(23)=13<14=\alpha(23). Therefore β ⁡ ( n) \beta(n) is a better boundary function of ϕ ⁡ ( n) \phi(n). But β ⁡ ( n) \beta(n) is not optimal either. Renaud gives the example of the familly

 | 𝒫 ⁡ ( 6) \ { 6, 5, 16, 15, 36, 45, 136, 145 } \mathcal{P}(6)\backslash\{6,5,16,15,36,45,136,145\} |  |

in which the most frequent element appears in 30 sets, but β ⁡ ( 56) = 31 \beta(56)=31.

### 4.2 An improved bound of ϕ ⁡ ( n) \phi(n)

Here we give another way of constructing union-closed collections whose maximal frequency approximates ϕ ⁡ ( n) \phi(n) better, and we show that the gap between ϕ ⁡ ( n) \phi(n) and β ⁡ ( n) \beta(n) is not bounded. We make use of the following notion in our construction:

###### Definition 1.

An up-set 𝒰 \mathcal{U} on m elements is a subset of 𝒫 ⁡ ( m) \mathcal{P}(m) such that S ∈ 𝒰 S\in\mathcal{U} and S ⊂ T ∈ [m] S\subset T\in[m] implies that T ∈ 𝒰 T\in\mathcal{U}.

We note that in the construction of the up-set of Renaud, the smaller sets are discarded while the larger sets are kept. We could have a lower maximal frequency if we could keep more small sets while keeping frequency “balanced” among the elements. For example, consider the the union-closed collection 𝒞 \mathcal{C} composed of 𝒫 ⁡ ( 12) \mathcal{P}(12) and the up-set on 13 13 elements generated by the sets { 1, 2, 3, 4, 13 } \{1,2,3,4,13\}, { 5, 6, 7, 8, 13 } \{5,6,7,8,13\}, { 9, 10, 11, 12, 13 } \{9,10,11,12,13\}. In the up-set, there are “holes” at level 6 to 11 (which does not happen in the construction of Renaud), that is, we will not generate all sets of size 6 6 to 11 in 𝒫 ⁡ ( 13) \ 𝒫 ⁡ ( 12) \mathcal{P}(13)\backslash\mathcal{P}(12). At the same time, all the elements in { 1, 2, …, 12 } \{1,2,...,12\} have the same frequency by symmetry. Therefore the maximal frequency in 𝒞 \mathcal{C} is

 | 2 12 + ∑ C ∈ 𝒞 \ 𝒫 ⁡ ( 12) ( | C | − 1) 12 2^{12}+\frac{\sum_{C\in\mathcal{C}\backslash{\mathcal{P}(12)}}(|C|-1)}{12} |  |

Let ℬ = ℬ ⁡ ( | 𝒞 |) \mathcal{B}=\mathcal{B}(|\mathcal{C}|) be the union-closed collection with the same number of sets as 𝒞 \mathcal{C} using the construction of Renaud, the maximal frequency in ℬ \mathcal{B} is

 | 2 12 + ⌈ ∑ B ∈ ℬ \ 𝒫 ⁡ ( 12) ( | B | − 1) 12 ⌉ 2^{12}+\left\lceil\frac{\sum_{B\in\mathcal{B}\backslash{\mathcal{P}(12)}}(|B|-1)}{12}\right\rceil |  |

As ℬ \mathcal{B} and 𝒞 \mathcal{C} have the same number of sets but ℬ \mathcal{B} contains more larger sets, the maximal frequency of 𝒞 \mathcal{C} is smaller than that of ℬ \mathcal{B}.

More generally, let s s and k k be integers greater than 1, and not both equal to 2. Let 𝒞 s, k \mathcal{C}_{s,k} be the union of 𝒫 ⁡ ( s ​ k) \mathcal{P}(sk) and the up-set on s ​ k + 1 sk+1 elements generated by { 1, 2, …, s, s ​ k + 1 }, { s + 1, s + 2, …, 2 ​ s, s ​ k + 1 }, …, { ( k − 1) ​ s + 1, ( k − 1) ​ s + 2, …, k ​ s, s ​ k + 1 } \{1,2,\ldots,s,sk+1\},\;\{s+1,s+2,\ldots,2s,sk+1\},\ldots,\;\{(k-1)s+1,(k-1)s+2,\ldots,ks,sk+1\}. In the up-set, there are holes at level s + 2 s+2 to k ⁡ ( s − 1) + 1 k(s-1)+1. Therefore there exists a bijective function f f from 𝒞 s, k \mathcal{C}_{s,k} to ℬ ⁡ ( | 𝒞 s, k |) \mathcal{B}(|\mathcal{C}_{s,k}|) such that for all C ∈ 𝒞 s, k C\in\mathcal{C}_{s,k}, | C | ≤ | f ⁡ ( C) | |C|\leq|f(C)| and ∃ C ∈ 𝒞 \exists C\in\mathcal{C} such that | C | < | f ⁡ ( C) | |C|<|f(C)|. As in 𝒞 \mathcal{C} the elements 1, 2, …, s ​ k 1,2,...,sk have the same frequency by symmetry and the frequency of the element s ​ k + 1 sk+1 is the same in 𝒞 \mathcal{C} and ℬ ⁡ ( 𝒞) \mathcal{B}(\mathcal{C}), the maximal frequency in 𝒞 \mathcal{C} is smaller than that in ℬ ⁡ ( | 𝒞 |) \mathcal{B}(|\mathcal{C}|).

To show that the gap between the maximal frequency of this construction and that of Renaud is not bounded, consider 𝒞 2, N \mathcal{C}_{2,N}, which is the union of 𝒫 ⁡ ( 2 ​ N) \mathcal{P}(2N) and the up-set generated by the sets { 1, …, N, 2 ​ N + 1 } \{1,...,N,2N+1\} and { N + 1, …, 2 ​ N, 2 ​ N + 1 } \{N+1,...,2N,2N+1\}. This up-set contains 2 N + 1 − 1 2^{N+1}-1 sets, and the frequency of an element in { 1, 2, …, 2 ​ N } \{1,2,...,2N\} is 2 N + 2 N − 1 − 1 2^{N}+2^{N-1}-1. The construction of Renaud ℬ ⁡ ( 2 2 ​ N + 2 N + 1 − 1) = 𝒫 ⁡ ( 2 ​ N) ∪ 𝒰 \mathcal{B}(2^{2N}+2^{N+1}-1)=\mathcal{P}(2N)\cup\mathcal{U}, where 𝒰 \mathcal{U} is an up-set on 2 ​ N + 1 2N+1 elements. According to Mitzenmacher and Upfal [5], for all k ∈ ℕ k\in\mathbbm{N} and k < 2 ​ N k<2N, ( 2 ​ N k) ≥ 1 2 ​ N + 1 ⋅ 2 H ⁡ ( k / 2 ​ N) ⋅ 2 ​ N \binom{2N}{k}\geq\frac{1}{2N+1}\cdot 2^{H(k/2N)\cdot 2N}, where H H is the binary entropy defined by H ( p) = − p ⋅ log 2 ( p) − ( 1 − p) log 2 ( 1 − p) H(p)=-p\cdot\log_{2}(p)-(1-p)\log_{2}(1-p). For N N big enough and k = ⌈ 2 ​ N 5 ⌉ k=\left\lceil\frac{2N}{5}\right\rceil, H ⁡ ( k / 2 ​ N) > H ⁡ ( 0.2) > 0.7 H(k/2N)>H(0.2)>0.7. Therefore

 | ( 2 ​ N k) > 1 2 ​ N + 1 ⋅ 2 H ⁡ ( k / 2 ​ N) ⋅ 2 ​ N > 1 2 ​ N + 1 ⋅ 2 1.4 ​ N > 2 N + 1. \binom{2N}{k}>\frac{1}{2N+1}\cdot 2^{H(k/2N)\cdot 2N}>\frac{1}{2N+1}\cdot 2^{1.4N}>2^{N+1}. |  |

This means that in 𝒰 \mathcal{U}, there are no sets of size less than 2 ​ N − k = ⌊ 8 ​ N 5 ⌋ 2N-k=\left\lfloor\frac{8N}{5}\right\rfloor. Therefore the maximal frequency among the elements { 1, 2, …, 2 ​ N } \{1,2,...,2N\} in 𝒰 \mathcal{U} is at least

 | ⌊ 8 ​ N 5 ⌋ − 1 2 ​ N ⋅ ( 2 N + 1 − 1). \frac{\left\lfloor\frac{8N}{5}\right\rfloor-1}{2N}\cdot(2^{N+1}-1). |  |

The gap between this number and 2 N + 2 N − 1 − 1 2^{N}+2^{N-1}-1 goes up to infinity as N N approaches infinity.

The condition that s s and k k are both greater than one and not both equal to two is not always satisfied, for example when n = 56 n=56. In this case we obtain the same union-closed collection as Renaud. We have seen in the last subsection that β ⁡ ( 56) > ϕ ⁡ ( 56) \beta(56)>\phi(56). This means that our construction is not optimal either. Intuitively, this can be explained by the fact that in both constructions with n + 1 n+1 elements, while the frequency of elements { 1, …, n } \{1,...,n\} is “balanced”, the frequency of the element n + 1 n+1 is too low, which leaves some space for further “compression”.

## References

- [1] V. Blinovsky, “Proof of Union- Closed Sets Conjecture”, arXiv:1507.01270 .
- [2] I.Bošnjak and P. Marković, The 11-element case of Frankl’s conjecture, *Electronic J. Combinatorics 15 (2008)*, #R88
- [3] H. Bruhn and O. Schaudt, “The journey of the union-closed sets conjecture”, arXiv:1309.3297.
- [4] C.I. Mallows, Conway’s challenge sequence, *American Mathematical Monthly 98*(1991), 5–20.
- [5] M. Mitzenmacher and E. Upfal, Probability and computing: Randomized algorithms and probabilistic analysis, *Cambridge University Press*, 2005.
- [6] J.C. Renaud, A second approximation to the boundary function on union-closed collections, *Ars Combin.*41 (1995) 177–188.
- [7] J.C. Renaud, Is the Union-closed sets conjecture the best possible? *Journal of the Australian Mathematical Society (Series A)*51 (1991), 276–283.
- [8] J-C. Renaud and L.F. Fitina, On union-closed sets and Conway’s sequence, *Bulletin of the Australian Mathematical Society*47 No.2 (1993), 321–332.
- [9] I. Roberts and J. Simpson, A note on the union-closed sets conjecture, *Australas. J. Comb. 47*, 265–267 (2010)
- [10] S. Schäge, “On the Union-Closed Set Conjecture”, arXiv:1607.01007.
- [11] M. Živković and B. Vučković, “The 12 element case of Frankl’s conjecture”, preprint, 2012.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:
