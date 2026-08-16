<!-- source: https://arxiv.org/html/1101.2589 | converted from HTML -->

Minimal weight in union-closed families

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:1101.2589v1 [math.CO] 13 Jan 2011

# Minimal weight in union-closed families

Victor Falgas–Ravry Note: School of Mathematical Sciences, Queen Mary, University of London, London E1 4NS, England

###### Abstract

Let Ω \Omega be a finite set and let 𝒮 ⊆ 𝒫 ⁡ ( Ω) \mathcal{S}\subseteq\mathcal{P}(\Omega) be a set system on Ω \Omega. For x ∈ Ω x\in\Omega, we denote by d 𝒮 ​ ( x) d_{\mathcal{S}}(x) the number of members of 𝒮 \mathcal{S} containing x x. A long-standing conjecture of Frankl [6] states that if 𝒮 \mathcal{S} is union-closed then there is some x ∈ Ω x\in\Omega with d 𝒮 ​ ( x) ≥ 1 2 ​ | 𝒮 | d_{\mathcal{S}}(x)\geq\frac{1}{2}|\mathcal{S}|.

We consider a related question. Define the *weight*of a family 𝒮 \mathcal{S} to be w ⁡ ( 𝒮):= ∑ A ∈ 𝒮 | A | w(\mathcal{S}):=\sum_{A\in\mathcal{S}}|A|. Suppose 𝒮 \mathcal{S} is union-closed. How small can w ⁡ ( 𝒮) w(\mathcal{S}) be? Reimer [11] showed

 | w ⁡ ( 𝒮) ≥ 1 2 ​ | 𝒮 | ​ log 2 ​ | 𝒮 |, w(\mathcal{S})\geq\frac{1}{2}|\mathcal{S}|\log_{2}|\mathcal{S}|, |  |

and that this inequality is tight. In this paper we show how Reimer’s bound may be improved if we have some additional information about the domain Ω \Omega of 𝒮 \mathcal{S}: if 𝒮 \mathcal{S} separates the points of its domain, then

 | w ⁡ ( 𝒮) ≥ ( | Ω | 2). w(\mathcal{S})\geq\binom{|\Omega|}{2}. |  |

This is stronger than Reimer’s Theorem when Ω > | 𝒮 | ​ log 2 ​ | 𝒮 | \Omega>\sqrt{|\mathcal{S}|\log_{2}|\mathcal{S}|}. In addition we construct a family of examples showing the combined bound on w ⁡ ( 𝒮) w(\mathcal{S}) is tight except in the region | Ω | = Θ ⁡ ( | 𝒮 | ​ log 2 ​ | 𝒮 |) |\Omega|=\Theta(\sqrt{|\mathcal{S}|\log_{2}|\mathcal{S}|}), where it may be off by a multiplicative factor of 2 2.

Our proof also gives a lower bound on the average degree: if 𝒮 \mathcal{S} is a point-separating union-closed family on Ω \Omega, then

 | 1 | Ω | ​ ∑ x ∈ Ω d 𝒮 ​ ( x) ≥ 1 2 ​ | 𝒮 | ​ log 2 ​ | 𝒮 | + O ⁡ ( 1), \frac{1}{|\Omega|}\sum_{x\in\Omega}d_{\mathcal{S}}(x)\geq\frac{1}{2}\sqrt{|\mathcal{S}|\log_{2}|\mathcal{S}|}+O(1), |  |

and this is best possible except for a multiplicative factor of 2 2.

## 1 Introduction

Let Ω \Omega be a finite set. We may identify X ⊆ Ω X\subseteq\Omega with its characteristic function and consider a collection of subsets of Ω \Omega as a family of functions from Ω \Omega into { 0, 1 } \{0,1\}. For such a family 𝒮 ⊆ 𝒫 ⁡ ( Ω) \mathcal{S}\subseteq\mathcal{P}(\Omega), we refer to Ω = Ω ⁡ ( S) \Omega=\Omega(S) as the *domain*of 𝒮 \mathcal{S}. Note that the domain of a set system 𝒮 \mathcal{S} is not uniquely determined by knowledge 𝒮 \mathcal{S}. Therefore when we speak of ‘a set system 𝒮 \mathcal{S} ’, we shall in fact mean ‘a pair ( 𝒮, Ω) (\mathcal{S},\Omega), where 𝒮 ⊆ 𝒫 ⁡ ( Ω) \mathcal{S}\subseteq\mathcal{P}(\Omega) ’ so that the domain of 𝒮 \mathcal{S} is implicitly specified.

We also let V ⁡ ( S):= ⋃ A ∈ 𝒮 A V(S):=\bigcup_{A\in\mathcal{S}}A be the set of all elements x ∈ Ω x\in\Omega which appear as a member of at least one set A ∈ 𝒮 A\in\mathcal{S}. For x ∈ Ω x\in\Omega we denote by d 𝒮 ​ ( x) d_{\mathcal{S}}(x) the number of members of 𝒮 \mathcal{S} containing x x. We call d 𝒮 ​ ( x) d_{\mathcal{S}}(x) the *degree*of x x in 𝒮 \mathcal{S}.

A set system 𝒮 \mathcal{S} is *union-closed*if it is closed under pairwise unions. This is essentially the same as being closed under arbitrary unions except that we do not require 𝒮 \mathcal{S} to contain the empty set. In 1979, Frankl [6] made a simple-sounding conjecture on the maximal degree in a union-closed family. This remains open and has become known as the Union-closed sets conjecture:

###### Conjecture 1 (Union-closed sets conjecture).

Let 𝒮 \mathcal{S} be a set system on some finite set Ω \Omega. Then there is an element x ∈ Ω x\in\Omega which is contained in at least half of the members of 𝒮 \mathcal{S}.

(An equivalent lattice-theoretic version also exists. See for example Abe and Nakano, Poonen or Stanley [1, 10, 13].)

Very little progress has been made on Conjecture 1. A simple argument due to Knill [7] establishes that for any union-closed family 𝒮 \mathcal{S} with | 𝒮 | = m |\mathcal{S}|=m, there always exists some x x contained in at least m log 2 ⁡ m \frac{m}{\log_{2}m} members of 𝒮 \mathcal{S}. Wójcik [14] improved this by a multiplicative constant. The conjecture is also known to hold if | 𝒮 | < 40 |\mathcal{S}|<40 (see [9, 12]) or | V ⁡ ( 𝒮) | < 11 |V(\mathcal{S})|<11 (see [8, 2]), if | 𝒮 | > 5 8 × 2 | V ⁡ ( 𝒮) | |\mathcal{S}|>\frac{5}{8}\times 2^{|V(\mathcal{S})|} (see [3, 4, 5]), or if 𝒮 \mathcal{S} contains some very specific collections of small sets (see [8, 2]).

In a different direction, Reimer [11] found a beautiful shifting argument to obtain a sharp lower bound on the average set size of 𝒮 \mathcal{S} as a function of | 𝒮 | |\mathcal{S}|. We state his result here.

###### Theorem (Reimer’s Average Set Size Theorem).

Let 𝒮 \mathcal{S} be a union-closed family. Then

 | 1 | 𝒮 | ​ ∑ A ∈ 𝒮 | A | ≥ log 2 ⁡ | 𝒮 | 2 \frac{1}{|\mathcal{S}|}\sum_{A\in\mathcal{S}}|A|\geq\frac{\log_{2}|\mathcal{S}|}{2} |  |

with equality if and only if 𝒮 \mathcal{S} is a powerset.

Define the *weight*of a family 𝒮 \mathcal{S} to be

 | w ⁡ ( 𝒮) \displaystyle w(\mathcal{S}) | : = ∑ A ∈ 𝒮 | A | \displaystyle:=\sum_{A\in\mathcal{S}}|A| |  |

 |  | = ∑ x ∈ Ω d 𝒮 ​ ( x). \displaystyle=\sum_{x\in\Omega}d_{\mathcal{S}}(x). |  |

We shall think of Reimer’s Theorem as a lower bound for the smallest possible weight of a union-closed family of a given size. Let 𝒮 \mathcal{S} be a union-closed family. In this form, Reimer’s Theorem states that

 | w ⁡ ( 𝒮) \displaystyle w(\mathcal{S}) | ≥ | 𝒮 | ​ log 2 ​ | 𝒮 | 2 \displaystyle\geq\frac{|\mathcal{S}|\log_{2}|\mathcal{S}|}{2} |  |

with equality if and only if 𝒮 \mathcal{S} is a powerset. The purpose of this paper is to show how we may improve this inequality if we have some additional information about Ω ⁡ ( 𝒮) \Omega(\mathcal{S}). As a corollary, we also give asymptotically tight (up to a constant) lower bounds on the average degree over Ω \Omega, 1 | Ω | ​ ∑ x ∈ Ω d 𝒮 ​ ( x) \frac{1}{|\Omega|}\sum_{x\in\Omega}d_{\mathcal{S}}(x).

As we remarked earlier, Ω ⁡ ( 𝒮) \Omega(\mathcal{S}) is not uniquely specified by 𝒮 \mathcal{S}. For example, Ω ⁡ ( 𝒮) \Omega(\mathcal{S}) could contain many elements which do not appear in 𝒮 \mathcal{S}. This would bring the average degree in Ω \Omega arbitrarily close to 0 0. Restricting our attention to V ⁡ ( 𝒮) V(\mathcal{S}) does not entirely resolve this problem: pick x ∈ V ⁡ ( 𝒮) x\in V(\mathcal{S}). Replacing every instance of x x in a member of 𝒮 \mathcal{S} by a set x 1, x 2, … ​ x M x_{1},x_{2},\ldots x_{M} for some arbitrarily large M M gives us a new union-closed family 𝒮 ′ \mathcal{S}^{\prime} with the same structure as 𝒮 \mathcal{S} but with average degree over V ⁡ ( 𝒮 ′) V(\mathcal{S}^{\prime}) arbitrarily close to d 𝒮 ​ ( x) d_{\mathcal{S}}(x).

Thus to say anything interesting about average degree, we need to impose a restriction on 𝒮 \mathcal{S} and its domain. In particular we want to make sure that no element of Ω ⁡ ( 𝒮) \Omega(\mathcal{S}) is ‘cloned’ many times over. We make therefore the following natural definition.

###### Definition.

A family 𝒮 \mathcal{S}*separates*a pair ( i, j) (i,j) of elements of Ω ⁡ ( 𝒮) \Omega(\mathcal{S}) if there exists A ∈ 𝒮 A\in\mathcal{S} such that A A contains exactly one of i i and j j. 𝒮 \mathcal{S} is *separating*if it separates every pair of distinct elements of Ω ⁡ ( 𝒮) \Omega(\mathcal{S}). If | Ω ⁡ ( S) | = n |\Omega(S)|=n and 𝒮 \mathcal{S} is separating, we say that 𝒮 \mathcal{S} is n n -separating.

Recalling our identification of sets with their characteristic functions, 𝒮 \mathcal{S} is separating if and only if it separates the points of Ω ⁡ ( 𝒮) \Omega(\mathcal{S}) as a family of functions Ω → { 0, 1 } \Omega\rightarrow\{0,1\}.

Trivially, a family 𝒮 \mathcal{S} of size | 𝒮 | = m |\mathcal{S}|=m can be at most 2 m 2^{m} -separating. In Section 2, we make use of certain heredity properties of union-closed families to prove that if in addition 𝒮 \mathcal{S} is union-closed it can be at most ( m + 1) (m+1) -separating. The main result of that section, Theorem 3, establishes that for any n n there is a unique (up to relabelling of vertices) n n -separating union-closed family of minimal weight.

In the third section, we use Theorem 3 together with Reimer’s Theorem to obtain lower bounds on the weight of n n -separating union-closed families of size m m for every realisable pair ( m, n) (m,n).

We construct families of examples showing these bounds are sharp up to a multiplicative factor of 2 + O ⁡ ( 1 log 2 ⁡ m) 2+O\left(\frac{1}{\log_{2}m}\right).

In the final section we consider a generalisation of our original problem. We define the *l l -fold weight*of a family 𝒮 \mathcal{S} to be

 | w l ​ ( 𝒮):= ∑ A ∈ 𝒮 ( | A | l). w_{l}(\mathcal{S}):=\sum_{A\in\mathcal{S}}\binom{|A|}{l}. |  |

The 0 0 -fold weight of 𝒮 \mathcal{S} is just the size of 𝒮 \mathcal{S}, while the 1 1 -fold weight is the weight w ⁡ ( 𝒮) w(\mathcal{S}) we introduced earlier. Similarly to the l = 1 l=1 case, we can bound w l w_{l} below for l ≥ 2 l\geq 2 when 𝒮 \mathcal{S} is separating using a combination of Reimer’s Theorem and Theorem 3 together with some elementary arguments. Again we provide constructions showing our bounds are the best possible up to a multiplicative factor of 2 + O ⁡ ( 1 / log 2 ⁡ m) 2+O\left(1/\log_{2}m\right). As instant corollaries to our results in sections 3 and 4, we have for any l ≥ 1 l\geq 1 sharp (up to a multiplicative constant) lower bounds on the expected number of sets in 𝒮 \mathcal{S} containing a randomly selected l l -tuple from Ω ⁡ ( 𝒮) \Omega(\mathcal{S}). These results are related to a generalisation of the union-closed sets conjecture.

## 2 Separation

In this section we use our definition of *separation*to prove some results about separating union-closed families. We begin with an item of notation. Let 𝒮 \mathcal{S} be a family with domain Ω \Omega. Given X ⊆ Ω X\subseteq\Omega, we will denote by 𝒮 ⁡ [X] \mathcal{S}[X] the family *induced*by X X on 𝒮 \mathcal{S},

 | 𝒮 [X]:= { A ∖ X | A ⊇ X, A ∈ 𝒮 }. \mathcal{S}[X]:=\left\{A\setminus X|A\supseteq X,A\in\mathcal{S}\right\}. |  |

We shall consider 𝒮 ⁡ [X] \mathcal{S}[X] as a family with domain Ω ⁡ ( 𝒮) ∖ X \Omega(\mathcal{S})\setminus X. In a slight abuse of notation we shall usually write 𝒮 ⁡ [x] \mathcal{S}[x] for 𝒮 ⁡ [{ x }] \mathcal{S}[\{x\}]. Note that | 𝒮 ​ [x] | = d 𝒮 ​ ( x) |\mathcal{S}[x]|=d_{\mathcal{S}}(x).

Recall that 𝒮 \mathcal{S}*separates*a pair ( i, j) (i,j) of elements of Ω ⁡ ( 𝒮) \Omega(\mathcal{S}) if there exists A ∈ 𝒮 A\in\mathcal{S} such that A A contains exactly one of i i and j j. 𝒮 \mathcal{S} is said to be *separating*if it separates every pair of distinct elements of Ω ⁡ ( 𝒮) \Omega(\mathcal{S}). We introduce an equivalence relation ≅ 𝒮 \cong_{\mathcal{S}} on its domain Ω ⁡ ( 𝒮) \Omega(\mathcal{S}) by setting x ≅ 𝒮 y x\cong_{\mathcal{S}}y if 𝒮 \mathcal{S} does not separate x x from y y. Quotienting Ω \Omega by ≅ 𝒮 \cong_{\mathcal{S}} in the obvious way, we obtain a reduced family

 | 𝒮 ′ = 𝒮 / ≅ 𝒮 \mathcal{S}^{\prime}=\mathcal{S}/\cong_{\mathcal{S}} |  |

on a new domain Ω ′ \Omega^{\prime} consisting of the ≅ 𝒮 \cong_{\mathcal{S}} equivalence classes on Ω \Omega. It follows from the definition of ≅ 𝒮 \cong_{\mathcal{S}} that 𝒮 ′ \mathcal{S}^{\prime} is separating and uniquely determined by the knowledge of 𝒮 \mathcal{S} and Ω \Omega. We shall refer to 𝒮 ′ \mathcal{S}^{\prime} as the *reduction*of 𝒮 \mathcal{S}.

Union-closure is clearly preserved by our quotienting operation. Every union-closed family S S may thus be reduced to a unique separating union-closed family in this way. Such separating union-closed families will be the main object we study in this paper. Before proving anything about them, let us give a few examples.

For n ≥ 2 n\geq 2, we define the *staircase*of height n n to be the union-closed family

 | T n = { { n }, { n − 1, n }, { n − 2, n − 1, n }, … ​ { 2, 3, … ​ n } } T_{n}=\left\{\{n\},\{n-1,n\},\{n-2,n-1,n\},\ldots\{2,3,\ldots n\}\right\} |  |

with domain Ω ⁡ ( T n) = { 1, 2, 3 ​ … ​ … ​ n } \Omega(T_{n})=\{1,2,3\ldots...n\}. Note that T n T_{n} is n n -separating, has size n − 1 n-1 and that V ⁡ ( T n) ≠ Ω ⁡ ( T n) V(T_{n})\neq\Omega(T_{n}), since the element 1 1 is not contained in any set of T n T_{n}. For completeness, we define T 1 T_{1} to be the empty family with domain Ω ⁡ ( T 1) = { 1 } \Omega(T_{1})=\{1\} and size 0 0. Recall that T n ​ [X] T_{n}[X] is the subfamily of T n T_{n} induced by X X. T n T_{n} has the property that T n ​ [{ n }] = T n − 1 ∪ { ∅ } T_{n}[\{n\}]=T_{n-1}\cup\{\emptyset\}.

We shall prove that T n T_{n} is an n n -separating union-closed family of least weight.

For n ≥ 2 n\geq 2, the *plateau*of width n n is the n n -separating union-closed family

 | U n = { { 1, 2, … ​ n − 1 }, { 1, 2, … ​ n − 2, n }, … ​ { 1, 3, 4 ​ … ​ n }, { 2, 3, … ​ n }, [n] }. U_{n}=\left\{\{1,2,\ldots n-1\},\{1,2,\ldots n-2,n\},\ldots\{1,3,4\ldots n\},\{2,3,\ldots n\},[n]\right\}. |  |

with domain Ω ⁡ ( U n) = [n] \Omega(U_{n})=[n] and size n + 1 n+1. For completeness we let E 1 E_{1} be the family { ∅, { 1 } } \{\emptyset,\{1\}\} with domain { 1 } \{1\}. It is easy to see that U n U_{n} is the n n -separating union-closed family of size n + 1 n+1 with maximal weight. It has weight roughly twice that of T n T_{n}, and the additional property that for every pair { i, j } ⊆ [n] \{i,j\}\subseteq[n] there is a set in U n U_{n} containing i i and not j j as well as a set containing j j and not i i.

Finally, or n ≥ 1 n\geq 1, the powerset of [n] [n], P n = 𝒫 ⁡ [n] P_{n}=\mathcal{P}[n] is, of course, a n n -separating union-closed family with domain Ω ⁡ ( P n) = V ⁡ ( P n) = [n] \Omega(P_{n})=V(P_{n})=[n]. Note that P n ​ [{ n }] = P n − 1 P_{n}[\{n\}]=P_{n-1}, and that P n P_{n} is the largest n n -separating family in every sense of the word, having both the maximum size and the maximum weight possible.

Let us now turn to the main purpose of this section.

We begin with a trivial lemma.

###### Lemma 1.

Let 𝒮 \mathcal{S} be a separating family on Ω = [n] \Omega=[n] with elements labelled in order of increasing degree. Then if 1 ≤ i < j ≤ n 1\leq i<j\leq n there exists A ∈ 𝒮 A\in\mathcal{S} with j ∈ A j\in A, i ∉ A i\notin A.

###### Proof.

Since 𝒮 \mathcal{S} is separating, there is some A A in 𝒮 \mathcal{S} containing one but not both of i i, j j. But we also know that d 𝒮 ​ ( i) ≤ d 𝒮 ​ ( j) d_{\mathcal{S}}(i)\leq d_{\mathcal{S}}(j), so at least one such A A contains j j and not i i. ∎

Repeated applications of Lemma 1 yield the following:

###### Lemma 2.

Let 𝒮 \mathcal{S} be a separating union-closed family with Ω ⁡ ( 𝒮) = [n] \Omega(\mathcal{S})=[n] and elements of Ω \Omega labelled in order of increasing degree. Then for every i ∈ [n − 1] i\in[n-1], 𝒮 \mathcal{S} contains a set A i = ( [n] ∖ [i]) ∪ X i A_{i}=\left([n]\setminus[i]\right)\cup X_{i}, where X i ⊆ [i − 1] X_{i}\subseteq[i-1]. These n − 1 n-1 sets are distinct.

###### Proof.

Pick i ∈ [n − 1] i\in[n-1]. By Lemma 1, for each j > i j>i there exists B j ∈ 𝒮 B_{j}\in\mathcal{S} containing j j and not i i. Let A i = ⋃ j > i B j A_{i}=\bigcup_{j>i}B_{j}. By union-closure, A i ∈ 𝒮 A_{i}\in\mathcal{S}. A i A_{i} is clearly of the form { i + 1, i + 2, … ​ n } ∪ X i \{i+1,i+2,\ldots n\}\cup X_{i}, where X i X_{i} is a subset of [i − 1] [i-1]. Moreover if i < j i<j we have A i ≠ A j A_{i}\neq A_{j} since j ∈ A i j\in A_{i}, j ∉ A j j\notin A_{j}. ∎

The main result of this section follows easily.

###### Theorem 3.

Let 𝒮 \mathcal{S} be a separating union-closed family on Ω ⁡ ( 𝒮) = [n] \Omega(\mathcal{S})=[n] with elements labelled in order of increasing degree. Then d 𝒮 ​ ( i) ≥ i − 1 d_{\mathcal{S}}(i)\geq i-1 for all i ∈ [n] i\in[n]. In particular, | 𝒮 | ≥ n − 1 |\mathcal{S}|\geq n-1, and the weight of 𝒮 \mathcal{S} satisfies :

 | w ⁡ ( 𝒮) ≥ ( n 2). w(\mathcal{S})\geq\binom{n}{2}. |  |

Moreover, w ⁡ ( 𝒮) = ( n 2) w(\mathcal{S})=\binom{n}{2} if and only if 𝒮 \mathcal{S} is one of T n T_{n} or T n ∪ { ∅ } T_{n}\cup\{\emptyset\}, where T n T_{n} is the staircase of height n n introduced earlier.

###### Proof.

By Lemma 2, 𝒮 \mathcal{S} contains n − 1 n-1 distinct sets A 1 A_{1}, A 2 A_{2}, … ​ A n − 1 \ldots A_{n-1} such that [n] ∖ [i] ⊆ A i [n]\setminus[i]\subseteq A_{i}. It follows in particular that | 𝒮 | ≥ n − 1 |\mathcal{S}|\geq n-1 and that d 𝒮 ​ ( i) ≥ i − 1 d_{\mathcal{S}}(i)\geq i-1 for all i ∈ [n] i\in[n]. Moreover

 | w ⁡ ( 𝒮) \displaystyle w(\mathcal{S}) | ≥ ∑ i ∈ [n − 1] | A i | \displaystyle\geq\sum_{i\in[n-1]}|A_{i}| |  |

 |  | ≥ ∑ i ∈ [n − 1] ( n − i) = ( n 2) \displaystyle\geq\sum_{i\in[n-1]}(n-i)=\binom{n}{2} |  |

with equality if and only if A i = [n] ∖ [i] A_{i}=[n]\setminus[i] for every i i and in addition 𝒮 \mathcal{S} contains no nonempty set other than the A i A_{i}. Thus w ⁡ ( 𝒮) = ( n 2) w(\mathcal{S})=\binom{n}{2} if and only if 𝒮 \mathcal{S} is one of T n T_{n} or T n ∪ { ∅ } T_{n}\cup\{\emptyset\}, as claimed. ∎

## 3 Minimal weight

In this section we use Reimer’s Theorem and Theorem 3 together to obtain a lower bound on the weight of an n n -separating union-closed family of size m m. We then give constructions in the entire range of possible n n, log 2 ⁡ m ≤ n ≤ m + 1 \log_{2}m\leq n\leq m+1, showing our bounds are asymptotically sharp except in the region n = Θ ⁡ ( m ​ log 2 ​ m) n=\Theta\left(\sqrt{m\log_{2}m}\right) (where they are differ by a multiplicative factor of at most 2 2). As a corollary, we obtain a lower bound on the average degree in a separating union-closed family.

Let 𝒮 \mathcal{S} be an n n -separating union-closed family with | 𝒮 | = m |\mathcal{S}|=m. Recall that the *weight*of 𝒮 \mathcal{S}, w ⁡ ( 𝒮) w(\mathcal{S}) is

 | w ⁡ ( 𝒮) = ∑ A ∈ 𝒮 | A | = ∑ x ∈ Ω ⁡ ( 𝒮) d 𝒮 ​ ( x). w(\mathcal{S})=\sum_{A\in\mathcal{S}}|A|=\sum_{x\in\Omega(\mathcal{S})}d_{\mathcal{S}}(x). |  |

We know from Reimer’s Theorem that

 | w ⁡ ( 𝒮) ≥ m ​ log 2 ​ m 2. w(\mathcal{S})\geq\frac{m\log_{2}m}{2}. |  |

We have another bound for w ⁡ ( 𝒮) w(\mathcal{S}) coming from our separation result, Theorem 3:

 | w ⁡ ( 𝒮) ≥ n ⁡ ( n − 1) 2. w(\mathcal{S})\geq\frac{n(n-1)}{2}. |  |

If n ≤ 1 2 ​ ( 1 + 1 + 4 ​ m ​ log 2 ⁡ m) = m ​ log 2 ​ m + O ⁡ ( 1) n\leq\frac{1}{2}\left(1+\sqrt{1+4m\log_{2}m}\right)=\sqrt{m\log_{2}m}+O(1), the ‘bound in m m ’ from Reimer’s Theorem is stronger; if on the other hand n ≥ 1 2 ​ ( 1 + 1 + 4 ​ m ​ log 2 ⁡ m) n\geq\frac{1}{2}\left(1+\sqrt{1+4m\log_{2}m}\right), the ‘bound in n n ’ from Theorem 3 is sharper.

For the bound in m m, equality occurs if and only if 𝒮 \mathcal{S} is a powerset, that is if and only n = log 2 ⁡ m n=\log_{2}m. For the bound in n n, equality occurs if and only if 𝒮 \mathcal{S} is a staircase (with possibly the empty set added in). This can only occur if n = m n=m or n = m + 1 n=m+1. Remarkably the combined bound is asymptotically sharp everywhere except in the region n = Θ ⁡ ( m ​ log 2 ​ m) n=\Theta\left(\sqrt{m\log_{2}m}\right), where it is only asymptotically sharp up to a constant. We shall show this by constructing intermediate families between powersets and staircases. Roughly speaking these intermediary families will look like staircases sitting on top of a powerset-like bases. This will allow Reimer’s Theorem and Theorem 3 to give us reasonably tight bounds. Some technicalities arise to make this work for all all possible ( m, n) (m,n).

We call a pair of integers ( n, m) (n,m)*satisfiable*if there exists an n n -separating union-closed family of size m m – in particular n n and m m must satisfy n − 1 ≤ m ≤ 2 n n-1\leq m\leq 2^{n}. Of course for m = 2 n m=2^{n} the powerset P n P_{n} is the only n n -separating family of the right size. By Theorem 3 we know already how to construct n n -separating union-closed families of sizes m = n − 1 m=n-1 or m = n m=n with minimal weight. Also if m = n + 1 m=n+1, it is easy to see that the family T n ∪ { ∅ } ∪ { { n − 1 } } T_{n}\cup\{\emptyset\}\cup\{\{n-1\}\} has minimal weight, so for our purposes we may as well assume 2 n > m > n + 1 2^{n}>m>n+1 in what follows.

Given a satisfiable pair ( m, n) (m,n) with 2 n > m > n + 1 2^{n}>m>n+1, there exists a unique integer b b such that 2 b − b ≤ m − n < 2 b + 1 − ( b + 1) 2^{b}-b\leq m-n<2^{b+1}-(b+1). Our aim is to take for our powerset-like base a suitable family of m − ( n − b − 1) m-(n-b-1) subsets of [b + 1] [b+1], and to place on top of it a staircase of height n − ( b + 1) n-(b+1), thus obtaining a separating union-closed family with the right size and domain.

For such a b b we have 2 b + 1 ≤ m − n + b + 1 ≤ 2 b + 1 2^{b}+1\leq m-n+b+1\leq 2^{b+1}. Write out the binary expansion of m − n + b + 1 m-n+b+1 as 2 b 1 + 2 b 2 + … ​ 2 b t 2^{b_{1}}+2^{b_{2}}+\ldots 2^{b_{t}} with 0 ≤ b t < b t − 1 < … < b 1 0\leq b_{t}<b_{t-1}<\ldots<b_{1}, and note b ≤ b 1 ≤ b + 1 b\leq b_{1}\leq b+1. We shall build the base ℬ \mathcal{B} of our intermediate family by adding up certain subcubes of 𝒫 ⁡ [b + 1] \mathcal{P}[b+1].

First of all if b 1 = b + 1 b_{1}=b+1, we shall just let ℬ \mathcal{B} be the whole of 𝒫 ⁡ [b + 1] \mathcal{P}[b+1]. This is the “nontechnical case” of our construction. If on the other hand b 1 = b b_{1}=b, we let Q 1 Q_{1} denote the b 1 b_{1} -dimensional subcube { X ∪ { b + 1 } ∣ X ⊆ [b] } \{X\cup\{b+1\}\mid X\subseteq[b]\}, and for every i: 2 ≤ i ≤ t i:\ 2\leq i\leq t we let Q i Q_{i} be the b i b_{i} -dimensional subcube { X ∪ { b i − 1 } ∣ X ⊆ [b i] } \{X\cup\{b_{i-1}\}\mid X\subseteq[b_{i}]\}. We then set ℬ = ⋃ i Q i \mathcal{B}=\bigcup_{i}Q_{i}.

It is easy to see that the Q i Q_{i} are disjoint. Indeed write b 0 b_{0} for b + 1 b+1 and suppose i < j i<j; for every X ∈ Q i X\in Q_{i}, b i − 1 b_{i-1} is the largest element in X X whereas for every X ′ ∈ Q j X^{\prime}\in Q_{j}, b j − 1 < b i − 1 b_{j-1}<b_{i-1} is the largest element contained in X ′ X^{\prime}, so that X ≠ X ′ X\neq X^{\prime}.

###### Claim.

ℬ \mathcal{B} is a ( b + 1) (b+1) -separating union-closed family.

###### Proof.

Q 1 Q_{1} is ( b + 1) (b+1) -separating since it contains the singleton { b + 1 } \{b+1\} and the pairs { i, b + 1 } \{i,b+1\} for every i < b + 1 i<b+1. Thus ℬ \mathcal{B} is ( b + 1) (b+1) -separating also.

Clearly each of the Q i Q_{i} is closed under pairwise unions. Now consider 1 ≤ i < j 1\leq i<j (or alternatively b 0 > b i > b j b_{0}>b_{i}>b_{j}) and take X ∈ Q i X\in Q_{i}, Y ∈ Q j Y\in Q_{j}. Then

 | Y \displaystyle Y | ⊆ [b j] ∪ { b j − 1 } \displaystyle\subseteq[b_{j}]\cup\{b_{j-1}\} |  |

 |  | ⊆ [b i], \displaystyle\subseteq[b_{i}], |  |

from which it follows that X ∪ Y ⊆ [b i] ∪ { b i − 1 } X\cup Y\subseteq[b_{i}]\cup\{b_{i-1}\}, and hence that X ∪ Y ∈ Q i X\cup Y\in Q_{i}. Thus ℬ = ⋃ i Q i \mathcal{B}=\bigcup_{i}Q_{i} is closed under pairwise unions, as claimed. ∎

We now turn to the staircase-like top of our family, 𝒯 \mathcal{T}, which we set to be

 | 𝒯 = { [b + 2], [b + 3], … ​ [n] }. \mathcal{T}=\{[b+2],[b+3],\ldots[n]\}. |  |

Our intermediate family will then be:

 | 𝒮 = ℬ ∪ 𝒯 \mathcal{S}=\mathcal{B}\cup\mathcal{T} |  |

It is easy to see from our construction that 𝒮 \mathcal{S} is union-closed, n n -separating and has size

 | | ℬ | + | 𝒯 | = ( m − n + b + 1) + ( n − b − 1) = m. |\mathcal{B}|+|\mathcal{T}|=(m-n+b+1)+(n-b-1)=m. |  |

We do not claim that 𝒮 \mathcal{S} is an n n -separating union-closed family of size m m with minimal weight; however as we shall see w ⁡ ( 𝒮) w(\mathcal{S}) is quite close to minimal.

###### Lemma 4.

 | w ⁡ ( ℬ) < | ℬ | ​ log 2 ​ | ℬ | 2 + | ℬ |. w(\mathcal{B})<\frac{|\mathcal{B}|\log_{2}|\mathcal{B}|}{2}+|\mathcal{B}|. |  |

###### Proof.

In the “non-technical case” where ℬ = 𝒫 ⁡ [b + 1] \mathcal{B}=\mathcal{P}[b+1] our assertion is trivial. We turn therefore to the “technical case” where | ℬ | = 2 b 1 + 2 b 2 + 2 b 3 + … ​ 2 b t |\mathcal{B}|=2^{b_{1}}+2^{b_{2}}+2^{b_{3}}+\ldots 2^{b_{t}} with b = b 1 > b 2 > … > b t ≥ 0 b=b_{1}>b_{2}>\ldots>b_{t}\geq 0:

 | w ⁡ ( ℬ) \displaystyle w(\mathcal{B}) | = ∑ i: b i ≠ 0 2 b i ( b i 2 + 1) \displaystyle=\sum_{i:\ b_{i}\neq 0}2^{b_{i}}\left(\frac{b_{i}}{2}+1\right) |  |

 |  | = b 2 ∑ i: b i ≠ 0 2 b i + ∑ i: b i ≠ 0 2 b i b i − b + 2 2 \displaystyle=\frac{b}{2}\sum_{i:\ b_{i}\neq 0}2^{b_{i}}+\sum_{i:\ b_{i}\neq 0}2^{b_{i}}\frac{b_{i}-b+2}{2} |  |

 |  | ≤ b ​ | ℬ | 2 + 2 b 1 + 2 b 2 / 2 \displaystyle\leq\frac{b|\mathcal{B}|}{2}+2^{b_{1}}+2^{b_{2}}/2 |  |

 |  | < | ℬ | ​ log 2 ​ | ℬ | 2 + | ℬ |. \displaystyle<\frac{|\mathcal{B}|\log_{2}|\mathcal{B}|}{2}+|\mathcal{B}|. |  |

∎

Now | ℬ | ≤ m |\mathcal{B}|\leq m, and the weight of 𝒯 \mathcal{T} is clearly less than n ⁡ ( n + 1) 2 \frac{n(n+1)}{2}. Thus it follows that

 | w ⁡ ( 𝒮) < m ​ log 2 ​ m 2 + n ⁡ ( n + 1) 2 + m. w(\mathcal{S})<\frac{m\log_{2}m}{2}+\frac{n(n+1)}{2}+m. |  |

On the other hand we already know from Reimer’s theorem and Theorem 3 that

 | w ⁡ ( 𝒮) ≥ max ⁡ ( m ​ log 2 ​ m 2, n ⁡ ( n − 1) 2), w(\mathcal{S})\geq\max\left(\frac{m\log_{2}m}{2},\frac{n(n-1)}{2}\right), |  |

which is asymptotically the same except when n 2 ∼ m ​ log 2 ​ m n^{2}\sim m\log_{2}m when the lower and upper bounds may diverge by a multiplicative factor of at most 2 2.

We have thus proved the following theorem.

###### Theorem 5.

Let ( n, m) (n,m) be a satisfiable pair of integers. Suppose 𝒮 \mathcal{S} is an n n -separating union-closed family of size m m with minimal weight. Then

 | max ⁡ ( m ​ log 2 ​ m 2, n ⁡ ( n − 1) 2) ≤ w ⁡ ( 𝒮) ≤ m ​ log 2 ​ m 2 + n ⁡ ( n + 1) 2 + m. \max\left(\frac{m\log_{2}m}{2},\frac{n(n-1)}{2}\right)\leq w(\mathcal{S})\leq\frac{m\log_{2}m}{2}+\frac{n(n+1)}{2}+m. |  |

In particular if ( n m, m) m ∈ ℕ (n_{m},m)_{m\in\mathbb{N}} is a sequence of satisfiable pairs and 𝒮 m \mathcal{S}_{m} a sequence of n m n_{m} -separating union-closed families of size m m with minimal weight, we have the following:

- •

If n m / m ​ log ⁡ m → 0 n_{m}/\sqrt{m\log m}\rightarrow 0 as m → ∞ m\rightarrow\infty then

 | lim m → ∞ w ⁡ ( 𝒮 m) / ( m ​ log 2 ​ m 2) = 1. \lim_{m\rightarrow\infty}w(\mathcal{S}_{m})/(\frac{m\log_{2}m}{2})=1. |  |

- •

If n m / m ​ log ⁡ m → ∞ n_{m}/\sqrt{m\log m}\rightarrow\infty as m → ∞ m\rightarrow\infty then

 | lim m → ∞ w ⁡ ( 𝒮 m) / ( n 2 2) = 1. \lim_{m\rightarrow\infty}w(\mathcal{S}_{m})/(\frac{n^{2}}{2})=1. |  |

- •

Otherwise

 | 1 ≤ lim ¯ ​ w ​ ( 𝒮 m) / max ⁡ ( n 2 2, m ​ log 2 ​ m 2), and 1\leq\underline{\lim}\ w(\mathcal{S}_{m})/\max(\frac{n^{2}}{2},\frac{m\log_{2}m}{2}),\textrm{ and} |  |

 | lim ¯ ​ w ​ ( 𝒮 m) / max ⁡ ( n 2 2, m ​ log 2 ​ m 2) ≤ 2 \overline{\lim}\ w(\mathcal{S}_{m})/\max(\frac{n^{2}}{2},\frac{m\log_{2}m}{2})\leq 2 |  |

∎

As a corollary to Theorems 3, 5 and Reimer’s Theorem we have the following result regarding average degree.

###### Corollary 6.

Let 𝒮 \mathcal{S} be a separating union-closed family. Then,

 | 1 | Ω ⁡ ( 𝒮) | ​ ∑ x ∈ Ω ⁡ ( 𝒮) d 𝒮 ​ ( x) ≥ | 𝒮 | ​ log 2 ​ | 𝒮 | 2 + O ⁡ ( 1). \frac{1}{|\Omega(\mathcal{S})|}\sum_{x\in\Omega(\mathcal{S})}d_{\mathcal{S}}(x)\geq\frac{\sqrt{|\mathcal{S}|\log_{2}|\mathcal{S}|}}{2}+O(1). |  |

Moreover there exist arbitrarily large separating union-closed families with

 | 1 | Ω ⁡ ( 𝒮) | ​ ∑ x ∈ Ω ⁡ ( 𝒮) d 𝒮 ​ ( x) ≤ | 𝒮 | ​ log 2 ​ | 𝒮 | + O ⁡ ( | 𝒮 | / log 2 ⁡ | 𝒮 |), \frac{1}{|\Omega(\mathcal{S})|}\sum_{x\in\Omega(\mathcal{S})}d_{\mathcal{S}}(x)\leq\sqrt{|\mathcal{S}|\log_{2}|\mathcal{S}|}+O(\sqrt{|\mathcal{S}|/\log_{2}|\mathcal{S}|}), |  |

so our bound is asymptotically sharp except for a multiplicative factor of at most 2 2.

###### Proof.

The average degree in a separating family 𝒮 \mathcal{S} is

 | 1 | Ω ⁡ ( 𝒮) | ​ ∑ x ∈ Ω ⁡ ( 𝒮) d 𝒮 ​ ( x) = w ⁡ ( 𝒮) | Ω ⁡ ( 𝒮) |. \frac{1}{|\Omega(\mathcal{S})|}\sum_{x\in\Omega(\mathcal{S})}d_{\mathcal{S}}(x)=\frac{w(\mathcal{S})}{|\Omega(\mathcal{S})|}. |  |

If 𝒮 \mathcal{S} is an n n -separating union-closed family of size m m, we get two lower bounds on w ⁡ ( 𝒮) w(\mathcal{S}) from Reimer’s Theorem and Theorem 3. Dividing through by | Ω ⁡ ( 𝒮) | = n |\Omega(\mathcal{S})|=n and optimising yields

 | 1 | Ω ⁡ ( 𝒮) | ​ ∑ x ∈ Ω ⁡ ( 𝒮) d 𝒮 ​ ( x) ≥ | 𝒮 | ​ log 2 ​ | 𝒮 | 2 − 1 4. \frac{1}{|\Omega(\mathcal{S})|}\sum_{x\in\Omega(\mathcal{S})}d_{\mathcal{S}}(x)\geq\frac{\sqrt{|\mathcal{S}|\log_{2}|\mathcal{S}|}}{2}-\frac{1}{4}. |  |

The constructions from the proof of Theorem 5 then give us for each satisfiable pair ( n, m) (n,m) examples of n n -separating families of size m m with close to minimal average degree. In particular, take m = 2 r m=2^{r} and n = ⌈ 2 r ​ r ⌉ n=\lceil\sqrt{2^{r}r}\rceil: the corresponding family we constructed has weight 2 r ​ r + O ⁡ ( 2 r) 2^{r}r+O(2^{r}). It has therefore average degree r ​ 2 r + O ⁡ ( 2 r / r) = m ​ log 2 ​ m + O ⁡ ( m / log 2 ⁡ m). \sqrt{r2^{r}}+O(\sqrt{2^{r}/r})=\sqrt{m\log_{2}m}+O(\sqrt{m/\log_{2}m}). ∎

We believe our bounds are in fact asymptotically sharp, and that the constructions we gave in the proof of Theorem 5 are essentially the best possible. We conjecture to that effect.

###### Conjecture 2.

Suppose n = c ​ m ​ log 2 ​ m + o ⁡ ( m ​ log 2 ​ m) n=c\sqrt{m\log_{2}m}+o(\sqrt{m\log_{2}m}), for some c > 0 c>0, and that 𝒮 \mathcal{S} is an n n -separating union-closed family of size m m. Then

 | w ⁡ ( 𝒮) ≥ 1 + c 2 2 ​ m ​ log 2 ​ m + o ⁡ ( m ​ log 2 ​ m). w(\mathcal{S})\geq\frac{1+c^{2}}{2}m\log_{2}m+o(m\log_{2}m). |  |

## 4 Minimal l l -fold weight

Let 𝒮 \mathcal{S} be a separating union-closed family. Recall that the l l -fold weight of a family 𝒮 \mathcal{S} is

 | w l ​ ( 𝒮) = ∑ A ∈ 𝒮 ( | A | l). w_{l}(\mathcal{S})=\sum_{A\in\mathcal{S}}\binom{|A|}{l}. |  |

In the previous section we obtained lower-bounds for w 1 ​ ( 𝒮) w_{1}(\mathcal{S}) in terms of | 𝒮 | |\mathcal{S}| and | Ω ⁡ ( 𝒮) | |\Omega(\mathcal{S})| and gave constructions showing these were asymptotically sharp up to a multiplicative constant. Using easy generalisations of Reimer’s Theorem and Theorem 3, we can obtain similar results concerning w l ​ ( 𝒮) w_{l}(\mathcal{S}). As a corollary, we will obtain lower bounds on the expected number of sets containing a random l l -subset of Ω ⁡ ( 𝒮) \Omega(\mathcal{S}), and show these are again asymptotically sharp up to a constant.

Results in this section are motivated by the remark that repeated iterations of the classical union-closed sets conjecture imply the following stronger looking statement:

###### Conjecture 3 (Generalised union-closed sets conjecture).

Let 𝒮 \mathcal{S} be a union-closed family. Then for every integer l: 1 ≤ l ≤ log 2 ⁡ | 𝒮 | l:\ 1\leq l\leq\log_{2}|\mathcal{S}|, there is an l l -subset X X of Ω ⁡ ( 𝒮) \Omega(\mathcal{S}) which is contained in at least | 𝒮 | / 2 l |\mathcal{S}|/2^{l} members of 𝒮 \mathcal{S}.

Let us first show how Reimer’s Theorem can be immediately generalised to l l -fold weights.

###### Lemma 7.

Let l ∈ ℕ l\in\mathbb{N} and let 𝒮 \mathcal{S} be a union-closed family. Then

 | w l ​ ( 𝒮) > | 𝒮 | ​ ( log 2 ⁡ | 𝒮 | / 2 l). w_{l}(\mathcal{S})>|\mathcal{S}|\binom{\log_{2}|\mathcal{S}|/2}{l}. |  |

###### Proof.

The function x ↦ ( x l) x\mapsto\binom{x}{l} is convex in ℝ + \mathbb{R}^{+}. By Jensen’s inequality, it follows that

 | w l ​ ( 𝒮) = ∑ A ∈ 𝒮 ( | A | l) ≥ | 𝒮 | ​ ( ∑ A ∈ 𝒮 | A | / | 𝒮 | l) w_{l}(\mathcal{S})=\sum_{A\in\mathcal{S}}\binom{|A|}{l}\geq|\mathcal{S}|\binom{\sum_{A\in\mathcal{S}}|A|/|\mathcal{S}|}{l} |  |

with equality if and only if all the members of 𝒮 \mathcal{S} have the same size. On the other hand, Reimer’s average set size theorem tell us

 | ∑ A ∈ 𝒮 | A | | 𝒮 | ≥ log 2 ⁡ | 𝒮 | 2, \frac{\sum_{A\in\mathcal{S}}|A|}{|\mathcal{S}|}\geq\frac{\log_{2}|\mathcal{S}|}{2}, |  |

with equality if and only if 𝒮 \mathcal{S} is a powerset (in which case not all the member of 𝒮 \mathcal{S} have the same size). Thus

 | w l ​ ( 𝒮) > | 𝒮 | ​ ( log 2 ⁡ | 𝒮 | / 2 l), w_{l}(\mathcal{S})>|\mathcal{S}|\binom{\log_{2}|\mathcal{S}|/2}{l}, |  |

and this inequality is strict (since we cannot have equality in both Jensen’s inequality and Reimer’s Theorem.)

Now, the l l -fold weight of a powerset P r = 𝒫 ⁡ ( [r]) P_{r}=\mathcal{P}([r]) is

 | w l ( P r) = ∑ A: | A | = l ∑ B 1 A ⊆ B = 2 r − l ( r l) > 2 r ( r / 2 l). w_{l}(P_{r})=\sum_{A:\ |A|=l}\sum_{B}1_{A\subseteq B}=2^{r-l}\binom{r}{l}>2^{r}\binom{r/2}{l}. |  |

However for a fixed l l,

 | w l ​ ( P r) 2 r ​ ( r / 2 l) → 1 ​ as r → ∞, \frac{w_{l}(P_{r})}{2^{r}\binom{r/2}{l}}\rightarrow 1\ \textrm{as $r\rightarrow\infty$,} |  |

so the bound on w l w_{l} is still asymptotically sharp. ∎

Next, let us generalise our result that for 𝒮 \mathcal{S} an n n -separating union-closed family,

 | w 1 ​ ( 𝒮) ≥ ( n 2). w_{1}(\mathcal{S})\geq\binom{n}{2}. |  |

Again this comes as an easy consequence of Lemmar 2.

###### Lemma 8.

Let l ∈ ℕ l\in\mathbb{N} and let 𝒮 \mathcal{S} be a separating union-closed family with Ω ⁡ ( 𝒮) = [n] \Omega(\mathcal{S})=[n] and elements of Ω \Omega labelled in order of increasing degree d 𝒮 d_{\mathcal{S}}. Then

 | w l ​ ( 𝒮) ≥ ( n l + 1), w_{l}(\mathcal{S})\geq\binom{n}{l+1}, |  |

with equality if and only if 𝒮 \mathcal{S} is of the form

 | 𝒮 = { [n] ∖ [1], [n] ∖ [2], [n] ∖ [3], … ​ [n] ∖ [n − l] } ∪ ℛ, \mathcal{S}=\left\{[n]\setminus[1],[n]\setminus[2],[n]\setminus[3],\ldots[n]\setminus[n-l]\right\}\cup\mathcal{R}, |  |

where ℛ ∪ { [n] ∖ [n − l] } \mathcal{R}\cup\{[n]\setminus[n-l]\} is a separating and union-closed subfamily of 𝒫 ⁡ ( [n] ∖ [n − l]) \mathcal{P}([n]\setminus[n-l]).

###### Proof.

By Lemma 2, 𝒮 \mathcal{S} contains at least n − 1 n-1 distinct sets A i A_{i}, i ∈ [n − 1] i\in[n-1], of the form

 | A i = { i + 1, i + 2 ​ … ​ n } ∪ X i, X i ⊆ [i − 1]. A_{i}=\left\{i+1,i+2\ldots n\right\}\cup X_{i},\ X_{i}\subseteq[i-1]. |  |

Thus

 | w l ​ ( 𝒮) \displaystyle w_{l}(\mathcal{S}) | ≥ ∑ i ∈ [n − 1] ( | A i | l) \displaystyle\geq\sum_{i\in[n-1]}\binom{|A_{i}|}{l} |  |

 |  | ≥ ∑ i ∈ [n − 1] ( n − i l) = ( n l + 1). \displaystyle\geq\sum_{i\in[n-1]}\binom{n-i}{l}=\binom{n}{l+1}. |  |

Equality may occur in the above if and only if A i = [n] ∖ [i] A_{i}=[n]\setminus[i] for all i ≤ n − l i\leq n-l and 𝒮 \mathcal{S} contains no other set of size greater or equal to l l. Suppose this is the case, and that 𝒮 \mathcal{S} contains a set B B with B ∩ [n − l] ≠ ∅ B\cap[n-l]\neq\emptyset.

Then B B contains some x ∈ [n − l] x\in[n-l]. Suppose it does not contain n − l + 1 n-l+1. Then by union-closure B ∪ A n − l + 1 B\cup A_{n-l+1} is an element of 𝒮 \mathcal{S} of size at least | { x, n − l + 2, … ​ n } | = l |\{x,n-l+2,\ldots n\}|=l. As it does not contain n − l + 1 n-l+1, it is not amongst the sets A i: i ≤ n − l A_{i}:i\leq n-l we identified earlier, a contradiction. B B therefore contains n − l + 1 n-l+1. By iterating this argument, we see that B B must also contain all of n − l + 2, n − l + 3, … ​ n − 1 n-l+2,n-l+3,\ldots n-1. But then B B has size at least | { x, n − l + 1, n − l + 2, … ​ n − 1 } | = l |\{x,n-l+1,n-l+2,\ldots n-1\}|=l. If it does not contain n n, it is distinct from the sets A i: i ≤ n − l A_{i}:i\leq n-l we identified earlier, which is a contradiction. If it does contain n n, then it has size at least l + 1 > l l+1>l. This is only possible if B = A i B=A_{i} for some i ∈ [n − l] i\in[n-l].

It follows that 𝒮 = { [n], [n] ∖ { 1 }, [n] ∖ { 2 } ​ … ​ [n] ∖ { n − l } } ∪ ℛ \mathcal{S}=\{[n],[n]\setminus\{1\},[n]\setminus\{2\}\ldots[n]\setminus\{n-l\}\}\cup\mathcal{R} with ℛ ∪ { [n] ∖ [n − l] } \mathcal{R}\cup\{[n]\setminus[n-l]\} a union-closed and separating subset of 𝒫 ⁡ ( [n] ∖ [n − l]) \mathcal{P}([n]\setminus[n-l]) as required. ∎

With Lemmas 7 and 8 in hand, we can now generalise Theorem 5.

###### Theorem 9.

Let ( n, m) (n,m) be a satisfiable pair of integers, and let l ∈ ℕ l\in\mathbb{N}. Suppose 𝒮 \mathcal{S} is an n n -separating union-closed family of size m m with minimal l l -fold weight w l ​ ( | 𝒮 |) = w l w_{l}(|\mathcal{S}|)=w_{l}. Then,

 | max ⁡ ( ( n l + 1), m ​ ( log 2 ⁡ m / 2 l)) ≤ w l \max\left(\binom{n}{l+1},m\binom{\log_{2}m/2}{l}\right)\leq w_{l} |  |

and

 | w l ≤ ( ( n l + 1) + m ​ ( log 2 ⁡ m / 2 l)) ​ ( 1 + o ⁡ ( 1)). w_{l}\leq\left(\binom{n}{l+1}+m\binom{\log_{2}m/2}{l}\right)(1+o(1)). |  |

Again the lower and upper bounds on w l w_{l} are asymptotically the same except when n ∼ m 1 / ( l + 1) ​ log 2 ​ m 1 − 1 / ( l + 1) n\sim m^{1/(l+1)}\log_{2}m^{1-1/(l+1)}.

###### Proof.

As this proof is essentially the same as that of Theorem 5, we omit the details. The lower bound on w l w_{l} follows from Lemmas 7 and 8. The upper bound follows from considering the l l -fold weight of the families we introduced in the proof of Theorem 5. The only difficulty involved lies in adapting Lemma 4 to l l -fold weights. We state and prove below the required generalisation in the “technical case”.

###### Lemma 10.

Let ℬ \mathcal{B} be as defined in the previous section, and assume | ℬ | = 2 b + 2 b 2 + … ​ 2 b t |\mathcal{B}|=2^{b}+2^{b_{2}}+\ldots 2^{b_{t}}. Then

 | w l ​ ( ℬ) < ( 1 + 2 ​ l log 2 ⁡ | ℬ |) ​ | ℬ | l! ​ ( log 2 ⁡ | ℬ | 2) l. w_{l}(\mathcal{B})<\left(1+\frac{2l}{\log_{2}|\mathcal{B}|}\right)\frac{|\mathcal{B}|}{l!}\left(\frac{\log_{2}|\mathcal{B}|}{2}\right)^{l}. |  |

###### Proof.

 | w l ​ ( ℬ) \displaystyle w_{l}(\mathcal{B}) | = ∑ i ( b i l) ​ 2 b i − l + ( b i l − 1) ​ 2 b i − l + 1 \displaystyle=\sum_{i}\binom{b_{i}}{l}2^{b_{i}-l}+\binom{b_{i}}{l-1}2^{b_{i}-l+1} |  |

 |  | ≤ ( ( b l) + 2 ​ ( b l − 1)) ​ ∑ i 2 b i − l \displaystyle\leq\left(\binom{b}{l}+2\binom{b}{l-1}\right)\sum_{i}2^{b_{i}-l} |  |

 |  | < ( 1 + 2 ​ l b) ​ b l l! ​ | ℬ | \displaystyle<(1+\frac{2l}{b})\frac{b^{l}}{l!}|\mathcal{B}| |  |

 |  | < ( 1 + 2 ​ l log 2 ⁡ | ℬ |) ​ | ℬ | l! ​ ( log 2 ⁡ | ℬ | 2) l. \displaystyle<\left(1+\frac{2l}{\log_{2}|\mathcal{B}|}\right)\frac{|\mathcal{B}|}{l!}\left(\frac{\log_{2}|\mathcal{B}|}{2}\right)^{l}. |  |

∎

Theorem 9 follows straightforwardly from here. ∎

As in the previous section we can use our result on l l -fold weights to obtain information about the average number of sets containing a randomly chosen l l -subset in a separating union-closed family.

###### Corollary 11.

Let 𝒮 \mathcal{S} be a separating union-closed family, and let X X be an l l -subset of Ω ⁡ ( 𝒮) \Omega(\mathcal{S}) chosen uniformly at random. Then

 | 𝔼 X ​ d 𝒮 ​ ( X) ≥ | 𝒮 | 1 l + 1 ​ ( log 2 ⁡ | 𝒮 | 2 ​ ( l + 1)) 1 − 1 l + 1 + O ⁡ ( ( | 𝒮 | log 2 ⁡ | 𝒮 |) 1 l + 1). \mathbb{E}_{X}d_{\mathcal{S}}(X)\geq{|\mathcal{S}|}^{\frac{1}{l+1}}{\left(\frac{\log_{2}|\mathcal{S}|}{2(l+1)}\right)}^{1-\frac{1}{l+1}}+O\left({\left(\frac{|\mathcal{S}|}{\log_{2}|\mathcal{S}|}\right)}^{\frac{1}{l+1}}\right). |  |

Moreover there exist arbitrarily large separating union-closed families 𝒮 \mathcal{S} with

 | 𝔼 X ​ d 𝒮 ​ ( X) ≤ 2 ​ | 𝒮 | 1 l + 1 ​ ( log 2 ⁡ | 𝒮 | 2 ​ ( l + 1)) 1 − 1 l + 1 + O ⁡ ( ( | 𝒮 | log 2 ⁡ | 𝒮 |) 1 l + 1), \mathbb{E}_{X}d_{\mathcal{S}}(X)\leq 2{|\mathcal{S}|}^{\frac{1}{l+1}}{\left(\frac{\log_{2}|\mathcal{S}|}{2(l+1)}\right)}^{1-\frac{1}{l+1}}+O\left({\left(\frac{|\mathcal{S}|}{\log_{2}|\mathcal{S}|}\right)}^{\frac{1}{l+1}}\right), |  |

so this bound is asymptotically sharp except for a multiplicative factor of at most 2 2.

###### Proof.

This is instant from Lemma 7, Lemma 8 and Theorem 9. ∎

We end our paper with the natural generalisation of Conjecture 2.

###### Conjecture 4.

Let l l be an integer. Suppose n = n ⁡ ( m) n=n(m) satisfies

 | n = c ​ m 1 / l + 1 ​ ( log 2 ⁡ m) 1 − 1 / ( l + 1) ​ ( 1 + o ⁡ ( 1)) n=cm^{1/l+1}\left(\log_{2}m\right)^{1-1/(l+1)}(1+o(1)) |  |

for some c = c ⁡ ( m) c=c(m). Then if 𝒮 \mathcal{S} is an n n -separating union-closed family of size m m, its l l -fold weight satisfies

 | w l ​ ( 𝒮) ≥ m ​ ( log 2 ⁡ m) l ​ ( 1 l! ​ 2 l + c l + 1 ( l + 1)!) ​ ( 1 + o ⁡ ( 1)). w_{l}(\mathcal{S})\geq m(\log_{2}m)^{l}\left(\frac{1}{l!2^{l}}+\frac{c^{l+1}}{(l+1)!}\right)(1+o(1)). |  |

## References

- [1] T. Abe and B. Nakano, Frankl’s conjecture is true for modular lattices, Graphs and Combinatorics 14 (1998), 305-311.
- [2] I. Bosňjak and P. Markovíc, The 11-element case of Frankl’s conjecture, Electronic Journal of Combinatorics 15, (1): R88.
- [3] G. Czédli, On averaging Frankl’s conjecture for large union-closed sets, Journal of Combinatorial Theory - Series A 116 (2009), 24-729.
- [4] G. Czédli, M. Maróti and E. T. Schmidt, On the scope of averaging for Frankl’s conjecture, Order 26 (2009), 31-48.
- [5] G. Czédli and E. T. Schmidt, Frankl’s conjecture for large semimodular and planar semimodular lattices, Acta Univ. Palacki. Olomuc., Fac. rer. nat., Mathematica 47 (2008), 47-53.
- [6] P. Frankl, Extremal set systems. Handbook of combinatorics, Vols. 1, 2, 1293-1329, Elsevier, Amsterdam, 1995.
- [7] E. Knill, Graph generated union-closed families of set, (1993), unpublished manuscript.
- [8] R. Morris, FC-families and improved bounds for Frankl’s conjecture, European Journal of Combinatorics 27 (2006), 269-282.
- [9] G. Lo Faro, Union-closed sets conjectures: improved bounds, Journal of Combinatorial Mathematics and Combinatorial Computing 16, 97-102.
- [10] B. Poonen, Union-closed families, Journal of Combinatorial Theory — Series A 59 (1992), 253-268.
- [11] D. Reimer, An Average Set Size Theorem, Combinatorics, Probability and Computing 12 (2003), 89-93.
- [12] I. Roberts, The union closed sets conjecture, Technical Report No 2/92, School of Mathematical Statistics, Curtin University of Technology, Perth (1992).
- [13] R. P. Stanley, Enumerative Combinatorics, Vol. 1, Wadsworth and Brooks/Coole, Belmont CA, 1996.
- [14] P. Wójcik, Union-closed families of sets, Discrete Mathematics 199 (1999), 173-182.
- [15] P. Wójcik Density of union-closed families, Discrete Mathematics 105 (1992), 259-267.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
