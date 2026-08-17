<!-- source: https://arxiv.org/html/2208.03803 | converted from HTML -->

Notes on the Union Closed Sets Conjecture

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: CC BY 4.0][2]

arXiv:2208.03803v2 [math.CO] 04 Apr 2023

# Notes on the Union Closed Sets Conjecture

Nicolas Nagel Affiliation: Department of Mathematics, TU Chemnitz, Germany
nicolas.nagel@math.tu-chemnitz.de

###### Abstract

The *Union Closed Sets Conjecture*states that in every finite, nontrivial set family closed under taking unions there is an element contained in at least half of all the sets of the family. We investigate two new directions with respect to the conjecture. Firstly, we consider the frequencies of all elements among a union closed family and pose a question generalizing the Union Closed Sets Conjecture. Secondly, we investigate structures equivalent to union closed families and obtain a weakening of the Union Closed Sets Conjecture. We pose some new open questions about union closed families and related structures and hint at some further directions of research regarding the conjecture.

Keywords: Union closed sets conjecture, element frequencies, interior operator, congruence relation, up-sets, intersecting families

## 1 Introduction

For an integer n ∈ ℕ n\in\mathbb{N} set [n] ≔ { 1, …, n } [n]\coloneqq\{1,\dots,n\} and let 𝒫 ⁡ ( n) ≔ 𝒫 ⁡ ( [n]) \mathcal{P}(n)\coloneqq\mathcal{P}([n]) be the power set over [n] [n]. A family ℱ ⊆ 𝒫 ⁡ ( n) \mathcal{F}\subseteq\mathcal{P}(n) is called *nontrivial*if

 | ⋃ ℱ ≔ ⋃ F ∈ ℱ F = [n] \bigcup\mathcal{F}\coloneqq\bigcup_{F\in\mathcal{F}}F=[n] |  |

( ⋂ ℱ \bigcap\mathcal{F} being defined similarly) and *union closed*if for A, B ∈ ℱ A,B\in\mathcal{F} also A ∪ B ∈ ℱ A\cup B\in\mathcal{F}. Notice that for any nontrivial, union closed family ℱ ⊆ 𝒫 ⁡ ( n) \mathcal{F}\subseteq\mathcal{P}(n) we have [n] = ⋃ ℱ ∈ ℱ [n]=\bigcup\mathcal{F}\in\mathcal{F}.

###### Conjecture 1.1 (Union Closed Sets Conjecture).

For every nontrivial, union closed ℱ ⊆ 𝒫 ⁡ ( n) \mathcal{F}\subseteq\mathcal{P}(n) there is an x ∈ [n] x\in[n] with

 | #⁡ { F ∈ ℱ: x ∈ F } ≥ 1 2 ⋅ #​ ℱ. \#\{F\in\mathcal{F}:x\in F\}\geq\frac{1}{2}\cdot\#\mathcal{F}. |  |

Here #​ X \#X denotes the cardinality of a set X X. If we desire, we may assume that ∅ ∈ ℱ \emptyset\in\mathcal{F}, since this only makes the above conjecture harder. Dating back to at least the 1980s, the Union Closed Sets Conjecture 1.1 (also referred to as *Frankl’s conjecture*) has a long and rich history. For more details on the development of the conjecture and what is known about it see the survey [7]. In recent years [1, 2, 6, 12, 15, 18, 20, 22, 23, 25] have further been published investigating the conjecture with respect to one aspect or another. In this context, the collaborative effort in [14] should also be mentioned.

Even though the Union Closed Sets Conjecture 1.1 has a rather simple statement, so far no proof or counterexample is known. In this paper, we want to investigate the conjecture in two new ways. Firstly, we may reformulate the conjecture to the statement that for every nontrivial, union closed family ℱ \mathcal{F} the *most frequent*element among ℱ \mathcal{F} is contained in at least half of all sets of ℱ \mathcal{F}. It is natural to ask, whether we can make similar statements about the other less frequent elements, which leads to a generalization of the conjecture.

Secondly, we will investigate structures equivalent (*cryptomorphic*) to union closed families. While studying the Union Closed Sets Conjecture 1.1 by use of equivalent structures is not new, it seems that this approach has not been used to its fullest yet. These equivalent structures enable us to get a better idea of the inner structure of union closed families. In particular, we will prove a weaker version of the conjecture. These ideas, while not being strong enough to prove the conjecture itself, certainly give new insights on how one can study union closed families further. Again, we pose some new questions that give a hint on how to approach the conjecture in a new way.

## 2 Frequencies

Let ℱ ⊆ 𝒫 ⁡ ( n) \mathcal{F}\subseteq\mathcal{P}(n) be a nontrivial, union closed family. By permuting the elements of the *ground set*[n] [n], we may assume

 | #⁡ { F ∈ ℱ: 1 ∈ F } ≥ #⁡ { F ∈ ℱ: 2 ∈ F } ≥ ⋯ ≥ #⁡ { F ∈ ℱ: n ∈ F }. \displaystyle\#\{F\in\mathcal{F}:1\in F\}\geq\#\{F\in\mathcal{F}:2\in F\}\geq\dots\geq\#\{F\in\mathcal{F}:n\in F\}. |  | (2.1) |

The Union Closed Sets Conjecture 1.1 is then equivalent to the statement that

 | #⁡ { F ∈ ℱ: 1 ∈ F } ≥ 1 2 ⋅ #​ ℱ. \#\{F\in\mathcal{F}:1\in F\}\geq\frac{1}{2}\cdot\#\mathcal{F}. |  |

What can be said about the other, less frequent elements? Notice that, assuming the Union Closed Sets Conjecture 1.1 holds, the family

 | ℱ ′ ≔ { F ∖ { 1 }: 1 ∈ F ∈ ℱ } \mathcal{F}^{\prime}\coloneqq\{F\setminus\{1\}:1\in F\in\mathcal{F}\} |  |

is again a nontrivial, union closed family of size at least 1 2 ⋅ #​ ℱ \frac{1}{2}\cdot\#\mathcal{F} now over the ground set { 2, …, n } \{2,\dots,n\}. Applying the Union Closed Sets Conjecture 1.1 to ℱ ′ \mathcal{F}^{\prime} we get an element x ∈ { 2, …, n } x\in\{2,\dots,n\} with

 | #⁡ { F ∈ ℱ: x ∈ F } ≥ #⁡ { F ∈ ℱ ′: x ∈ F } ≥ 1 2 ⋅ #​ ℱ ′ ≥ 1 4 ⋅ #​ ℱ. \#\{F\in\mathcal{F}:x\in F\}\geq\#\{F\in\mathcal{F}^{\prime}:x\in F\}\geq\frac{1}{2}\cdot\#\mathcal{F}^{\prime}\geq\frac{1}{4}\cdot\#\mathcal{F}. |  |

In particular, since the element 2 2 is at least as frequent in ℱ \mathcal{F} as x x we get

 | #⁡ { F ∈ ℱ: 2 ∈ F } ≥ 1 4 ⋅ #​ ℱ. \#\{F\in\mathcal{F}:2\in F\}\geq\frac{1}{4}\cdot\#\mathcal{F}. |  |

Iterating this argument we have shown (assuming the Union Closed Sets Conjecture 1.1)

 | #⁡ { F ∈ ℱ: k ∈ F } ≥ 1 2 k ⋅ #​ ℱ \displaystyle\#\{F\in\mathcal{F}:k\in F\}\geq\frac{1}{2^{k}}\cdot\#\mathcal{F} |  | (2.2) |

for all k ∈ [n] k\in[n]. However, one might feel that every iterative step is a bit wasteful since we only consider sets from ℱ ′ \mathcal{F}^{\prime} even though there might be a lot of sets in ℱ ∖ ℱ ′ \mathcal{F}\setminus\mathcal{F}^{\prime} also containing 2 2 or any other element. We therefore ask whether the right hand side of ( 2.2) can be improved. We suggest that this is indeed the case and that even the constant fraction on the right hand side can be raised.

###### Question 2.1.

Let ℱ ⊆ 𝒫 ⁡ ( n) \mathcal{F}\subseteq\mathcal{P}(n) be a nontrvial, union closed family fulfilling ( 2.1), is it then true that

 | #⁡ { F ∈ ℱ: k ∈ F } ≥ 1 2 k − 1 + 1 ⋅ #​ ℱ \displaystyle\#\{F\in\mathcal{F}:k\in F\}\geq\frac{1}{2^{k-1}+1}\cdot\#\mathcal{F} |  | (2.3) |

for all k ∈ [n] k\in[n]?

Notice that k = 1 k=1 yields the Union Closed Sets Conjecture 1.1. If Question 2.1 indeed holds then the constant 1 / ( 2 k − 1 + 1) 1/(2^{k-1}+1) on the right hand side of ( 2.3) is optimal. For this fix k ∈ [n] k\in[n] and consider the family

 | ℱ = 𝒫 ⁡ ( k − 1) ∪ { [n] }, \displaystyle\mathcal{F}=\mathcal{P}(k-1)\cup\{[n]\}, |  | (2.4) |

which already fulfils ( 2.1). Here #​ ℱ = 2 k − 1 + 1 \#\mathcal{F}=2^{k-1}+1 and { F ∈ ℱ: k ∈ F } = { [n] } \{F\in\mathcal{F}:k\in F\}=\{[n]\}, so that ( 2.3) holds with equality. While this shows that the constant for this specific k k cannot be improved (if it holds at all), notice how ( 2.3) is very far off for all the other l ∈ [n] ∖ { k } l\in[n]\setminus\{k\}. This leads to a multitude of other related questions one could ask in this context.

###### Question 2.2.

How do the families ℱ \mathcal{F} look where equality is achieved in ( 2.3) for some k ∈ [n] k\in[n]? Are there other extremal construction next to ( 2.4)?

A family ℱ ⊆ 𝒫 ⁡ ( n) \mathcal{F}\subseteq\mathcal{P}(n) is called *separating*if

 | { F ∈ ℱ: x ∈ F } ≠ { F ∈ ℱ: y ∈ F } \displaystyle\{F\in\mathcal{F}:x\in F\}\neq\{F\in\mathcal{F}:y\in F\} |  | (2.5) |

for all x, y ∈ [n], x ≠ y x,y\in[n],x\neq y. Notice how in general (for k < n k<n) the construction ( 2.4) is not separating.

###### Question 2.3.

Can the right hand side of ( 2.3) be improved if in addition we assume ℱ \mathcal{F} to be separating?

We will now give some justification for Question 2.1. The general idea would be an inductive proof of ( 2.3) via induction on k k with the induction start k = n k=n. Our aim should thus be to prove Question 2.1 for large k k first. To do this, we use the following lemma.

###### Lemma 2.4.

Let ℱ ⊆ 𝒫 ⁡ ( n) \mathcal{F}\subseteq\mathcal{P}(n) be a nontrivial, union closed family and x ∈ [n] x\in[n]. For every A ∈ ℱ A\in\mathcal{F} with x ∈ A x\in A it holds

 | { F ∈ ℱ: x ∈ F } ≥ 1 2 #​ A − 1 + 1 ⋅ #​ ℱ. \{F\in\mathcal{F}:x\in F\}\geq\frac{1}{2^{\#A-1}+1}\cdot\#\mathcal{F}. |  |

###### Remark 2.5.

To get large lower bounds on the frequency of x x we would wish to choose a small set A ∈ ℱ A\in\mathcal{F} containing x x. The proof of the lemma will be analogous to the proof of the “folklore” theorem (see [7]) that if ℱ \mathcal{F} is a nontrivial, union closed family with { x } ∈ ℱ \{x\}\in\mathcal{F} (that is it contains a singleton) then x x is contained in at least half of all the sets of ℱ \mathcal{F}.

###### Proof of Lemma 2.4.

Consider the surjective map

 | φ: { X ⊆ [n]: x ∉ X } → { Y ⊆ [n]: A ⊆ Y }, X ↦ X ∪ A. \varphi:\{X\subseteq[n]:x\notin X\}\rightarrow\{Y\subseteq[n]:A\subseteq Y\},X\mapsto X\cup A. |  |

We claim that for every Y ⊆ [n], A ⊆ Y Y\subseteq[n],A\subseteq Y the fiber φ − 1 ​ ( Y) \varphi^{-1}(Y) is of cardinality 2 #​ A − 1 2^{\#A-1}. Indeed, it even holds that

 | φ − 1 ​ ( Y) = { X ⊆ [n] ∖ { x }: X ∩ ( [n] ∖ A) = Y ∩ ( [n] ∖ A) }, \varphi^{-1}(Y)=\{X\subseteq[n]\setminus\{x\}:X\cap([n]\setminus A)=Y\cap([n]\setminus A)\}, |  |

which is clear by the elementary equivalence

 | X ∪ A = Y ⇔ X ∖ A = Y ∖ A. X\cup A=Y\quad\Leftrightarrow\quad X\setminus A=Y\setminus A. |  |

Since Y ∩ ( [n] ∖ A) Y\cap([n]\setminus A) is a fixed set, we can only vary X X on A ∖ { x } A\setminus\{x\}, so that

 | #​ φ − 1 ​ ( Y) = 2 #⁡ ( A ∖ { x }) = 2 #​ A − 1. \#\varphi^{-1}(Y)=2^{\#(A\setminus\{x\})}=2^{\#A-1}. |  |

Let now ℱ \mathcal{F}, x x and A A be as in the statement. Assume that { G ∈ ℱ: x ∉ G } ≠ ∅ \{G\in\mathcal{F}:x\notin G\}\neq\emptyset, otherwise the claim of the lemma is clear. Notice then, since ℱ \mathcal{F} is union closed, the above map φ \varphi restricts to a map

 | φ: { G ∈ ℱ: x ∉ G } → { F ∈ ℱ: x ∈ F }, G ↦ G ∪ A. \varphi:\{G\in\mathcal{F}:x\notin G\}\rightarrow\{F\in\mathcal{F}:x\in F\},G\mapsto G\cup A. |  |

By the first part of the proof, for every F ∈ ℱ, x ∈ F F\in\mathcal{F},x\in F there are at most 2 #​ A − 1 2^{\#A-1} many G ∈ ℱ, x ∉ G G\in\mathcal{F},x\notin G with G ∪ A = F G\cup A=F. Thus

 | #⁡ { G ∈ ℱ: x ∉ G } ≤ 2 #​ A − 1 ⋅ #⁡ { F ∈ ℱ: x ∈ F } \#\{G\in\mathcal{F}:x\notin G\}\leq 2^{\#A-1}\cdot\#\{F\in\mathcal{F}:x\in F\} |  |

and using #⁡ { G ∈ ℱ: x ∉ G } = #​ ℱ − #⁡ { F ∈ ℱ: x ∈ F } \#\{G\in\mathcal{F}:x\notin G\}=\#\mathcal{F}-\#\{F\in\mathcal{F}:x\in F\} we proved the lemma. ∎

###### Theorem 2.6.

Question 2.1 holds for k = n k=n and k = n − 1 k=n-1.

###### Proof.

The case k = n k=n follows by applying Lemma 2.4 to x = n x=n and A = [n] A=[n]. For k = n − 1 k=n-1, we may assume ℱ \mathcal{F} to be separating (see ( 2.5)). Otherwise, we may combine elements that cannot be separated and we get a separating, nontrivial, union closed family over a smaller ground set on which we could work instead. Since then

 | { F ∈ ℱ: n − 1 ∈ F } ≠ { F ∈ ℱ: n ∈ F } \{F\in\mathcal{F}:n-1\in F\}\neq\{F\in\mathcal{F}:n\in F\} |  |

but also

 | #⁡ { F ∈ ℱ: n − 1 ∈ F } ≥ #⁡ { F ∈ ℱ: n ∈ F }, \#\{F\in\mathcal{F}:n-1\in F\}\geq\#\{F\in\mathcal{F}:n\in F\}, |  |

there must be an

 | A ∈ { F ∈ ℱ: n − 1 ∈ F } ∖ { F ∈ ℱ: n ∈ F }. A\in\{F\in\mathcal{F}:n-1\in F\}\setminus\{F\in\mathcal{F}:n\in F\}. |  |

Notice that A ≠ [n] A\neq[n], so in particular #​ A ≤ n − 1 \#A\leq n-1. Apply now Lemma 2.4 with x = n − 1 x=n-1 and this A A to get the bound for k = n − 1 k=n-1. ∎

To prove the statement of Question 2.1 it remains to proceed by induction, that is if the statement holds for k > 1 k>1 we would need to show it for k − 1 k-1. It remains open how this could be done precisely.

## 3 Weakenings of the Union Closed Sets Conjecture

We now present some different ideas for the Union Closed Sets Conjecture 1.1. We begin by introducing some general theory which we will later apply to study the structure of union closed families.

### 3.1 Equivalent Structures

To start, we recapitulate some of the already applied structures to investigate the Union Closed Sets Conjecture 1.1 (see [7]). It is easy to show that a family ℱ ⊆ 𝒫 ⁡ ( n) \mathcal{F}\subseteq\mathcal{P}(n) is union closed if and only if 𝒢 ≔ { [n] ∖ F: F ∈ ℱ } \mathcal{G}\coloneqq\{[n]\setminus F:F\in\mathcal{F}\} is *intersection closed*(that is if A, B ∈ 𝒢 A,B\in\mathcal{G} also A ∩ B ∈ 𝒢 A\cap B\in\mathcal{G}). Furthermore, an element x x is contained in at least half of all sets of ℱ \mathcal{F} if and only if it is contained in at most half of all sets of 𝒢 \mathcal{G}. This observation gives the *Intersection Closed Sets Conjecture*:

For every intersection closed family 𝒢 ⊆ 𝒫 ⁡ ( n) \mathcal{G}\subseteq\mathcal{P}(n) with ⋂ 𝒢 = ∅ \bigcap\mathcal{G}=\emptyset (the nontriviality condition) there is an x ∈ [n] x\in[n] with

 | #⁡ { G ∈ 𝒢: x ∈ G } ≤ 1 2 ⋅ #​ 𝒢. \#\{G\in\mathcal{G}:x\in G\}\leq\frac{1}{2}\cdot\#\mathcal{G}. |  |

Of course, we have not gained very much by this equivalent statement. However, other structures might be more useful, as described in [7]. A family 𝒢 ⊆ 𝒫 ⁡ ( n) \mathcal{G}\subseteq\mathcal{P}(n) is called *simply rooted*if for every ∅ ≠ G ∈ 𝒢 \emptyset\neq G\in\mathcal{G} there is an x ∈ G x\in G with

 | [x, G] ≔ { X ⊆ G: x ∈ X } ⊆ 𝒢. \displaystyle[x,G]\coloneqq\{X\subseteq G:x\in X\}\subseteq\mathcal{G}. |  | (3.1) |

It is straightforward to prove (see for example [4] Lemma 18) that ℱ ⊆ 𝒫 ⁡ ( n) \mathcal{F}\subseteq\mathcal{P}(n) is union closed if and only if 𝒢 ≔ 𝒫 ⁡ ( n) ∖ ℱ \mathcal{G}\coloneqq\mathcal{P}(n)\setminus\mathcal{F} is simply rooted. In a similar way to intersection closed sets above we also get an analogue of the Union Closed Sets Conjecture 1.1 for simply rooted families.

More akin to how we will use it below there is also an equivalent way to state the Union Closed Sets Conjecture 1.1 in the languages of lattices and even graphs (see [7] for more details and references). In what follows, we will use some theory from [8, 10] and apply it to study the Union Closed Sets Conjecture 1.1. We will adapt the terminology from [8]. Let us start with the following consideration.

Let ℱ ⊆ 𝒫 ⁡ ( n) \mathcal{F}\subseteq\mathcal{P}(n) be a union closed family with ∅ ∈ ℱ \emptyset\in\mathcal{F}. For every set X ⊆ [n] X\subseteq[n]

 | τ ⁡ ( X) ≔ ⋃ { F ∈ ℱ: F ⊆ X } ∈ ℱ \displaystyle\tau(X)\coloneqq\bigcup\{F\in\mathcal{F}:F\subseteq X\}\in\mathcal{F} |  | (3.2) |

is the unique maximal set from ℱ \mathcal{F} contained in X X. This gives a map

 | τ: 𝒫 ⁡ ( n) → ℱ \tau:\mathcal{P}(n)\rightarrow\mathcal{F} |  |

with the properties

- (i)

for all X ∈ 𝒫 X\in\mathcal{P} it holds τ ⁡ ( X) ⊆ X \tau(X)\subseteq X (*exclusivity*);

- (ii)

for all X ⊆ Y ⊆ [n] X\subseteq Y\subseteq[n] it holds τ ⁡ ( X) ⊆ τ ⁡ ( Y) \tau(X)\subseteq\tau(Y) (*monotonicity*);

- (iii)

for all X ⊆ [n] X\subseteq[n] it holds τ ⁡ ( τ ⁡ ( X)) = τ ⁡ ( X) \tau(\tau(X))=\tau(X) (*idempotence*).

A map τ: 𝒫 ⁡ ( n) → 𝒫 ⁡ ( n) \tau:\mathcal{P}(n)\rightarrow\mathcal{P}(n) fulfilling the above conditions (i - iii) is called an *interior operator*(notice that [8] uses the dual concept of a *closure operator*as is more common in the order theoretic literature, but for union closed families it is more convenient to work with interior operators; all statements below will be taken from [8] with according adjustments). It is not hard to show that for a given union closed ∅ ∈ ℱ ⊆ 𝒫 ⁡ ( n) \emptyset\in\mathcal{F}\subseteq\mathcal{P}(n) the map τ \tau from ( 3.2) is an interior operator and that furthermore

 | Fix ⁡ τ ≔ { X ⊆ [n]: τ ⁡ ( X) = X } = ℱ. \operatorname{Fix}\tau\coloneqq\{X\subseteq[n]:\tau(X)=X\}=\mathcal{F}. |  |

In this way, union closed families containing the empty set are cryptomorphic to interior operators.

###### Theorem 3.1.

Let n ∈ ℕ n\in\mathbb{N}, the correspondence

 | { ℱ ⊆ 𝒫 ⁡ ( n): ∅ ∈ ℱ ​ union closed } \displaystyle\{\mathcal{F}\subseteq\mathcal{P}(n):\emptyset\in\mathcal{F}\text{ union closed}\} | → { τ: 𝒫 ⁡ ( n) → 𝒫 ⁡ ( n) ​ interior operator } \displaystyle\rightarrow\{\tau:\mathcal{P}(n)\rightarrow\mathcal{P}(n)\text{ interior operator}\} |  |

 | ℱ \displaystyle\mathcal{F} | ↦ ( X ↦ ⋃ { F ∈ ℱ: F ⊆ X }) \displaystyle\mapsto\left(X\mapsto\bigcup\{F\in\mathcal{F}:F\subseteq X\}\right) |  |

is a bijection with inverse given by

 | τ ↦ Fix ⁡ τ. \tau\mapsto\operatorname{Fix}\tau. |  |

###### Proof.

See [8] Section 2.2 and references therein. ∎

There does not seem to be a useful way to translate the Union Closed Sets Conjecture 1.1 into the language of interior operators. However, they will turn out useful in the study of the structure of union closed families. To go further into this direction we will continue to study interior operators. Let τ: 𝒫 ⁡ ( n) → 𝒫 ⁡ ( n) \tau:\mathcal{P}(n)\rightarrow\mathcal{P}(n) be an interior operator and set ℱ ≔ Fix ⁡ τ \mathcal{F}\coloneqq\operatorname{Fix}\tau. For every F ∈ ℱ F\in\mathcal{F} define

 | 𝒯 ⁡ ( F) ≔ τ − 1 ​ ( F) ⊆ 𝒫 ⁡ ( n). \mathcal{T}(F)\coloneqq\tau^{-1}(F)\subseteq\mathcal{P}(n). |  |

Then 𝐏 ≔ { 𝒯 ⁡ ( F): F ∈ ℱ } \mathbf{P}\coloneqq\{\mathcal{T}(F):F\in\mathcal{F}\} is a partition of 𝒫 ⁡ ( n) \mathcal{P}(n) into #​ ℱ \#\mathcal{F} classes. We call a partitioning of 𝒫 ⁡ ( n) \mathcal{P}(n) that is obtained from an interior operator in this way a *congruence partition*. Every partition implies a corresponding equivalence relation γ \gamma given by

 | X γ Y ⇔ X, Y ∈ 𝒯 ( F) for some F ∈ ℱ. X\gamma Y\quad\Leftrightarrow\quad X,Y\in\mathcal{T}(F)\text{ for some }F\in\mathcal{F}. |  |

By the way 𝐏 \mathbf{P} is constructed out of τ \tau we have

 | X γ Y ⇔ τ ( X) = τ ( Y). X\gamma Y\quad\Leftrightarrow\quad\tau(X)=\tau(Y). |  |

An equivalence relation γ \gamma that is constructed out of an interior operator τ \tau in the above manner will be called a *congruence relation*. There is an intrinsic way to characterize congruence operator without mentioning any interior operators.

###### Theorem 3.2.

Let γ \gamma be an equivalence relation on 𝒫 ⁡ ( n) \mathcal{P}(n). Then γ \gamma is a congruence relation if and only if for all A, B, C ⊆ [n] A,B,C\subseteq[n] it holds

 | A ​ γ ​ B ⇒ ( A ∩ C) ​ γ ​ ( B ∩ C). \displaystyle A\gamma B\quad\Rightarrow\quad(A\cap C)\gamma(B\cap C). |  | (3.3) |

###### Proof.

See [8] Section 2.2 and references therein. Notice that congruence relations there are defined in a dual way with unions instead of intersections. This is again due to the fact that we are interested in union closed families and not in intersection closed families. ∎

Notice that the above theorem gives another cryptomorphic way to study union closed families now via equivalence relations on 𝒫 ⁡ ( n) \mathcal{P}(n) (and their implied partitions) fulfilling ( 3.3). We will continue to study the structure of congruence partitions in further detail.

###### Corollary 3.3.

Let 𝐏 = { P 1, …, P m } \mathbf{P}=\{P_{1},...,P_{m}\} be a congruence partition. Then every P i P_{i} is intersection closed and for all A, B ∈ P i, A ⊆ B A,B\in P_{i},A\subseteq B it holds

 | [A, B] ≔ { X ⊆ B: A ⊆ X } ⊆ P i. [A,B]\coloneqq\{X\subseteq B:A\subseteq X\}\subseteq P_{i}. |  |

###### Proof.

Let P i P_{i} be an equivalence class of a congruence partition and γ \gamma the corresponding congruence relation. For the first part, notice that since A, B ∈ P i A,B\in P_{i}, applying ( 3.3) with C = A C=A we get

 | A ​ γ ​ ( A ∩ B), A\gamma(A\cap B), |  |

so that (since A ∈ P i A\in P_{i}) A ∩ B ∈ P i A\cap B\in P_{i}. For the second part let A ⊆ B A\subseteq B in P i P_{i} and take A ⊆ X ⊆ B A\subseteq X\subseteq B. Applying ( 3.3) with C = X C=X we get

 | A = ( A ∩ X) ​ γ ​ ( B ∩ X) = X, A=(A\cap X)\gamma(B\cap X)=X, |  |

so (since A ∈ P i A\in P_{i}) X ∈ P i X\in P_{i}. ∎

###### Remark 3.4.

By the above corollary every class P i P_{i} of a congruence partition has a minimal element X = ⋂ P i X=\bigcap P_{i} and it holds that

 | P i = ⋃ Y ∈ P i [X, Y]. P_{i}=\bigcup_{Y\in P_{i}}[X,Y]. |  |

If τ \tau is the interior operator associated to the congruence partition, then X = τ ⁡ ( Y) X=\tau(Y) for all Y ∈ P i Y\in P_{i}. In particular, the minimal elements of all equivalence classes are precisely the union closed family which generated the interior operator τ \tau according to ( 3.2).

For our purpose the following will be of importance.

###### Lemma 3.5.

Let ∅ ∈ ℱ ⊆ 𝒫 ⁡ ( n) \emptyset\in\mathcal{F}\subseteq\mathcal{P}(n) be a union closed family, τ: 𝒫 ⁡ ( n) → 𝒫 ⁡ ( n) \tau:\mathcal{P}(n)\rightarrow\mathcal{P}(n) the corresponding interior operator and 𝐏 = { 𝒯 ⁡ ( F): F ∈ ℱ } \mathbf{P}=\{\mathcal{T}(F):F\in\mathcal{F}\} the corresponding congruence partition. Let E, F ∈ ℱ E,F\in\mathcal{F} with E ⊆ F E\subseteq F, then #​ 𝒯 ​ ( F) ≤ #​ 𝒯 ​ ( E) \#\mathcal{T}(F)\leq\#\mathcal{T}(E).

###### Proof.

We will prove that

 | ι = ι E F: 𝒯 ⁡ ( F) → 𝒯 ⁡ ( E), X ↦ X ∖ ( F ∖ E) \iota=\iota_{E}^{F}:\mathcal{T}(F)\rightarrow\mathcal{T}(E),X\mapsto X\setminus(F\setminus E) |  |

is an order embedding (that is X ⊆ Y X\subseteq Y if and only if ι ⁡ ( X) ⊆ ι ⁡ ( Y) \iota(X)\subseteq\iota(Y)), in particular injective (see [9]). From this the statement follows.
We should first show that ι \iota is well defined, that is if X ∈ 𝒯 ⁡ ( F) X\in\mathcal{T}(F) then X ∖ ( F ∖ E) ∈ 𝒯 ⁡ ( E) X\setminus(F\setminus E)\in\mathcal{T}(E). Indeed, apply ( 3.3) with A = X A=X, B = F B=F and C = [n] ∖ ( F ∖ E) C=[n]\setminus(F\setminus E). Since X, F ∈ 𝒯 ⁡ ( F) X,F\in\mathcal{T}(F) we thus get

 | X ∖ ( F ∖ E) ​ γ ​ F ∖ ( F ∖ E) = E ∈ 𝒯 ⁡ ( E), X\setminus(F\setminus E)\gamma F\setminus(F\setminus E)=E\in\mathcal{T}(E), |  |

so that X ∖ ( F ∖ E) ∈ 𝒯 ⁡ ( E) X\setminus(F\setminus E)\in\mathcal{T}(E) as desired. To check that ι \iota is an order embedding simply note that for all X, Y ∈ 𝒯 ⁡ ( F) X,Y\in\mathcal{T}(F) it holds (since F ∖ E ⊆ X, Y F\setminus E\subseteq X,Y)

 | X ⊆ Y ⇔ X ∖ ( F ∖ E) ⊆ Y ∖ ( F ∖ E). X\subseteq Y\quad\Leftrightarrow\quad X\setminus(F\setminus E)\subseteq Y\setminus(F\setminus E). |  |

∎

In particular we conclude the following.

###### Corollary 3.6.

Let ∅ ∈ ℱ ⊆ 𝒫 ⁡ ( n) \emptyset\in\mathcal{F}\subseteq\mathcal{P}(n) be a union closed family and let { 𝒯 ⁡ ( F): F ∈ ℱ } \{\mathcal{T}(F):F\in\mathcal{F}\} be the corresponding congruence partition. Then there is a way to label the sets from ℱ = { F 1, …, F m } \mathcal{F}=\{F_{1},\dots,F_{m}\} in such a way that

- (i)

#​ 𝒯 ​ ( F 1) ≤ #​ 𝒯 ​ ( F 2) ≤ … ≤ #​ 𝒯 ​ ( F m) \#\mathcal{T}(F_{1})\leq\#\mathcal{T}(F_{2})\leq...\leq\#\mathcal{T}(F_{m}) and

- (ii)

if F i ⊇ F j F_{i}\supseteq F_{j} then i ≤ j i\leq j.

###### Proof.

Define the ordering F 1, …, F m F_{1},\dots,F_{m} by setting F 1 F_{1} to be the unique (by union closedness) maximal set of ℱ \mathcal{F} and, having F 1, …, F i F_{1},\dots,F_{i} already defined, choosing F i + 1 = F F_{i+1}=F to be a maximal set from F ∈ ℱ ∖ { F 1, …, F i } F\in\mathcal{F}\setminus\{F_{1},\dots,F_{i}\} such that #​ 𝒯 ​ ( F) \#\mathcal{T}(F) is of minimal cardinality. The claimed properties (i) and (ii) then follow from Lemma 3.5 and the given construction respectively. ∎

### 3.2 Up-sets

An *up-set*(also called *increasing family*) is a family 𝒰 ⊆ 𝒫 ⁡ ( n) \mathcal{U}\subseteq\mathcal{P}(n) such that if A ⊆ B ⊆ [n] A\subseteq B\subseteq[n] with A ∈ 𝒰 A\in\mathcal{U}, then also B ∈ 𝒰 B\in\mathcal{U}. That is, up-sets are closed under taking super sets. It is not new to study union closed sets using up-sets via *up-compression techniques*(see [7] for details). We will give some insight into this technique, also to demonstrate why the considerations below use up-sets in a nouvelle way. Clearly, every up-set is union closed and it is not hard to show that the Union Closed Sets Conjecture 1.1 holds for all up-sets. By trying to add elements to the sets from a given nontrivial, union closed family one tries to construct an up-set that is easier to work with than general union closed families, but still gives information about the original union closed family.

For what follows, up-sets will play a different roll. Let ℱ ⊆ 𝒫 ⁡ ( n) \mathcal{F}\subseteq\mathcal{P}(n) be a union closed family and notice that for every x ∈ [n] x\in[n] we can write

 | { F ∈ ℱ: x ∈ F } = ℱ ∩ [x, [n]] \{F\in\mathcal{F}:x\in F\}=\mathcal{F}\cap[x,[n]] |  |

(see ( 3.1)). Notice that [x, [n]] [x,[n]] is an up-set of cardinality 2 n − 1 2^{n-1}. Thus the following, which we will prove next using the theory developed in the previous section, is a weakening of the Union Closed Sets Conjecture 1.1.

###### Theorem 3.7.

Let ℱ ⊆ 𝒫 ⁡ ( n) \mathcal{F}\subseteq\mathcal{P}(n) be a nontrivial, union closed family. There is an up-set 𝒰 ⊆ 𝒫 ⁡ ( n) \mathcal{U}\subseteq\mathcal{P}(n) with #​ 𝒰 ≤ 2 n − 1 \#\mathcal{U}\leq 2^{n-1} such that

 | #⁡ ( ℱ ∩ 𝒰) ≥ 1 2 ⋅ #​ 𝒰. \#(\mathcal{F}\cap\mathcal{U})\geq\frac{1}{2}\cdot\#\mathcal{U}. |  |

###### Remark 3.8.

It should be noted that the n n up-sets of the form [x, [n]] [x,[n]] only make up a vanishingly small part out of all up-sets in 𝒫 ⁡ ( n) \mathcal{P}(n) of cardinality at most 2 n − 1 2^{n-1}. We therefore hope that these ideas can be improved upon to get better results regarding the Union Closed Sets Conjecture 1.1 in the future. We will also demonstrate how the above result can be used to get a statement about the frequency of the most common element among ℱ \mathcal{F} in the next section.

For the proof we need an elementary lemma.

###### Lemma 3.9.

Let 0 ≤ n 1 ≤ ⋯ ≤ n m 0\leq n_{1}\leq\dots\leq n_{m} be real numbers, set N = ∑ i = 1 m n i N=\sum_{i=1}^{m}n_{i} and let ϑ ∈ [0, 1] \vartheta\in[0,1]. Then

 | ϑ ​ N ≥ ∑ i = 1 ⌊ ϑ ​ m ⌋ n i. \vartheta N\geq\sum_{i=1}^{\lfloor\vartheta m\rfloor}n_{i}. |  |

Here ⌊ ⋅ ⌋ \lfloor\cdot\rfloor denotes the *floor-function*. In the proof we will also use the *ceiling-function*⌈ ⋅ ⌉ \lceil\cdot\rceil.

###### Proof.

The statement is clear for ϑ < 1 m \vartheta<\frac{1}{m}, since then the right hand side is zero. Suppose ϑ ≥ 1 m \vartheta\geq\frac{1}{m}, define the function f: ( 0, m] → ℝ, f ⁡ ( x) ≔ n ⌈ x ⌉ f:(0,m]\rightarrow\mathbb{R},f(x)\coloneqq n_{\lceil x\rceil}. By monotonicity for the n i n_{i} ’s the function f f is also monotonically increasing. Thus, since m ⌊ ϑ ​ m ⌋ ≥ 1 \frac{m}{\lfloor\vartheta m\rfloor}\geq 1, we have

 | f ⁡ ( x) ≤ f ⁡ ( m ⌊ ϑ ​ m ⌋ ⋅ x) f(x)\leq f\left(\frac{m}{\lfloor\vartheta m\rfloor}\cdot x\right) |  |

for x ∈ ( 0, ⌊ ϑ ​ m ⌋] x\in(0,\lfloor\vartheta m\rfloor]. By the substitution y = m ⌊ ϑ ​ m ⌋ ⋅ x y=\frac{m}{\lfloor\vartheta m\rfloor}\cdot x we get

 | ∑ i = 1 ⌊ ϑ ​ m ⌋ n i \displaystyle\sum_{i=1}^{\lfloor\vartheta m\rfloor}n_{i} | = ∫ 0 ⌊ ϑ ​ m ⌋ f ⁡ ( x) ​ 𝑑 x ≤ ∫ 0 ⌊ ϑ ​ m ⌋ f ⁡ ( m ⌊ ϑ ​ m ⌋ ⋅ x) ​ 𝑑 x = ∫ 0 m f ⁡ ( y) ⋅ ⌊ ϑ ​ m ⌋ m ​ 𝑑 y \displaystyle=\int_{0}^{\lfloor\vartheta m\rfloor}f(x)dx\leq\int_{0}^{\lfloor\vartheta m\rfloor}f\left(\frac{m}{\lfloor\vartheta m\rfloor}\cdot x\right)dx=\int_{0}^{m}f(y)\cdot\frac{\lfloor\vartheta m\rfloor}{m}dy |  |

 |  | = ⌊ ϑ ​ m ⌋ m ⋅ ∑ i = 1 m n i ≤ ϑ ​ N. \displaystyle=\frac{\lfloor\vartheta m\rfloor}{m}\cdot\sum_{i=1}^{m}n_{i}\leq\vartheta N. |  |

∎

We can now proof Theorem 3.7 in a more general version.

###### Theorem 3.10.

Let n, t ∈ ℕ n,t\in\mathbb{N} and let ℱ ⊆ 𝒫 ⁡ ( n) \mathcal{F}\subseteq\mathcal{P}(n) be a nontrivial, union closed. Then there is an up-set 𝒰 ⊆ 𝒫 ⁡ ( n) \mathcal{U}\subseteq\mathcal{P}(n) with #​ 𝒰 ≤ ⌈ 2 n / t ⌉ \#\mathcal{U}\leq\lceil 2^{n}/t\rceil and

 | #⁡ ( ℱ ∩ 𝒰) ≥ 1 t ⋅ #​ ℱ. \#(\mathcal{F}\cap\mathcal{U})\geq\frac{1}{t}\cdot\#\mathcal{F}. |  |

###### Proof.

We may assume ∅ ∈ ℱ \emptyset\in\mathcal{F}. Order #​ ℱ = { F 1, …, F m } \#\mathcal{F}=\{F_{1},\dots,F_{m}\} as in Corollary 3.6. We claim that 𝒰 ≔ ⋃ i = 1 ⌈ m / t ⌉ 𝒯 ⁡ ( F i) \mathcal{U}\coloneqq\bigcup_{i=1}^{\lceil m/t\rceil}\mathcal{T}(F_{i}) does the job. First, we have ℱ ∩ 𝒰 = { F 1, …, F ⌈ m / t ⌉ } \mathcal{F}\cap\mathcal{U}=\{F_{1},\dots,F_{\lceil m/t\rceil}\} so #⁡ ( ℱ ∩ 𝒰) ≥ 1 t ⋅ #​ ℱ \#(\mathcal{F}\cap\mathcal{U})\geq\frac{1}{t}\cdot\#\mathcal{F}. It remains to show that 𝒰 \mathcal{U} is an up-set with

 | #​ 𝒰 ≤ ⌈ 1 t ⋅ 2 n ⌉. \#\mathcal{U}\leq\left\lceil\frac{1}{t}\cdot 2^{n}\right\rceil. |  |

The fact that 𝒰 \mathcal{U} is an up-set stems from the fact { 𝒯 ⁡ ( F 1), …, 𝒯 ⁡ ( F ⌈ m / t ⌉) } \{\mathcal{T}(F_{1}),...,\mathcal{T}(F_{\lceil m/t\rceil})\} is a partition of 𝒰 \mathcal{U} fulfilling property (i) from Corollary 3.6. To bound #​ 𝒰 \#\mathcal{U} notice that F 1 = [n] F_{1}=[n] by nontriviality of ℱ \mathcal{F}. Setting f i = #​ 𝒯 ​ ( F i) f_{i}=\#\mathcal{T}(F_{i}) we thus have 1 = f 1 ≤ f 2 ≤ ⋯ ≤ f m 1=f_{1}\leq f_{2}\leq\dots\leq f_{m} and

 | ∑ i = 2 m f i = 2 n − 1. \sum_{i=2}^{m}f_{i}=2^{n}-1. |  |

Applying Lemma 3.9 to n 1 = f 2, …, n m − 1 = f m n_{1}=f_{2},\dots,n_{m-1}=f_{m} with ϑ = ⌈ m t ⌉ − 1 m − 1 \vartheta=\frac{\lceil\frac{m}{t}\rceil-1}{m-1} we get

 | #​ 𝒰 \displaystyle\#\mathcal{U} | = ∑ i = 1 ⌈ m / t ⌉ f i = 1 + ∑ i = 1 ⌈ m / t ⌉ − 1 n i ≤ 1 + ⌈ m t ⌉ − 1 m − 1 ⋅ ∑ i = 1 m − 1 n i \displaystyle=\sum_{i=1}^{\lceil m/t\rceil}f_{i}=1+\sum_{i=1}^{\lceil m/t\rceil-1}n_{i}\leq 1+\frac{\lceil\frac{m}{t}\rceil-1}{m-1}\cdot\sum_{i=1}^{m-1}n_{i} |  |

 |  | ≤ 1 + m + t − 1 t − 1 m − 1 ​ ( 2 n − 1) = 1 + 1 t ⋅ ( 2 n − 1) < 1 t ⋅ 2 n + 1, \displaystyle\leq 1+\frac{\frac{m+t-1}{t}-1}{m-1}(2^{n}-1)=1+\frac{1}{t}\cdot(2^{n}-1)<\frac{1}{t}\cdot 2^{n}+1, |  |

but since #​ 𝒰 \#\mathcal{U} is an integer we get the desired bound. ∎

Setting t = 2 t=2 yields Theorem 3.7.

### 3.3 A Demonstration

We demonstrate how one can apply Theorem 3.7 to get a bound about the frequency of the most frequent element among a nontrivial, union closed family ℱ \mathcal{F}. The here proven bound is unfortunately worse than all already known bounds which we will collect further below. The author hopes that these results still turn out fruitful in the further development of the Union Closed Sets Conjecture 1.1. The following result might be interesting on its own.

###### Theorem 3.11.

Let n ∈ ℕ, n ≥ 2 n\in\mathbb{N},n\geq 2 and 𝒰 ⊆ 𝒫 ⁡ ( n) \mathcal{U}\subseteq\mathcal{P}(n) be an upset with #​ 𝒰 ≤ 2 n − 1 \#\mathcal{U}\leq 2^{n-1}. Let C = 1 + e − 1 = 1.367 ​ … C=1+e^{-1}=1.367\dots and t ∈ ℕ, t ≥ C ​ n log 2 ⁡ n t\in\mathbb{N},t\geq\frac{Cn}{\log_{2}n}. For any collection of sets A 1, …, A t ∈ 𝒰 A_{1},\dots,A_{t}\in\mathcal{U} there are indices i < j i<j with A i ∩ A j ≠ ∅ A_{i}\cap A_{j}\neq\emptyset.

That is, for any sufficiently large collection of sets from a sufficiently small up-set there are two intersecting sets from that collection.

###### Proof.

Assume 𝒰 ⊆ 𝒫 ⁡ ( n) \mathcal{U}\subseteq\mathcal{P}(n) is an up-set with #​ 𝒰 ≤ 2 n − 1 \#\mathcal{U}\leq 2^{n-1} and A 1, …, A t ∈ 𝒰 A_{1},\dots,A_{t}\in\mathcal{U} are pairwise disjoint. We aim to bound t t. For all i = 1, …, t i=1,\dots,t then [A i, [n]] ⊆ 𝒰 [A_{i},[n]]\subseteq\mathcal{U}, so

 | ⋃ i = 1 t [A i, [n]] ⊆ 𝒰. \bigcup_{i=1}^{t}[A_{i},[n]]\subseteq\mathcal{U}. |  |

It holds that ⋂ i ∈ I [A i, [n]] = [⋃ i ∈ I A i, [n]] \bigcap_{i\in I}[A_{i},[n]]=[\bigcup_{i\in I}A_{i},[n]] for all nonempty set of indices I ⊆ [t] I\subseteq[t]. For i ∈ [t] i\in[t] set a i ≔ #​ A i a_{i}\coloneqq\#A_{i}. Since the A i A_{i} ’s are pairwise disjoint it holds

 | #​ ⋃ i ∈ I A i = ∑ i ∈ I a i \#\bigcup_{i\in I}A_{i}=\sum_{i\in I}a_{i} |  |

for all nonempty I ⊆ [t] I\subseteq[t]. By inclusion-exclusion we get

 | #​ 𝒰 \displaystyle\#\mathcal{U} | ≥ #⋃ i = 1 t [A i, [n]] = ∑ ∅ ≠ I ⊆ [t] ( − 1) #​ I − 1 ⋅ #⋂ i ∈ I [A i, [n]] = ∑ ∅ ≠ I ⊆ [t] ( − 1) #​ I − 1 ⋅ 2 n − ∑ i ∈ I a i \displaystyle\geq\#\bigcup_{i=1}^{t}[A_{i},[n]]=\sum_{\emptyset\neq I\subseteq[t]}(-1)^{\#I-1}\cdot\#\bigcap_{i\in I}[A_{i},[n]]=\sum_{\emptyset\neq I\subseteq[t]}(-1)^{\#I-1}\cdot 2^{n-\sum_{i\in I}a_{i}} |  |

 |  | = 2 n ​ ( 1 − ∏ i = 1 t ( 1 − 2 − a i)). \displaystyle=2^{n}\left(1-\prod_{i=1}^{t}(1-2^{-a_{i}})\right). |  |

For variables x 1, …, x t ≥ 0 x_{1},\dots,x_{t}\geq 0 under the constraint ∑ i = 1 t x i ≤ n \sum_{i=1}^{t}x_{i}\leq n, the expression

 | 1 − ∏ i = 1 t ( 1 − 2 − x i) 1-\prod_{i=1}^{t}(1-2^{-x_{i}}) |  |

is minimized for x 1 = ⋯ = x t = n t x_{1}=\dots=x_{t}=\frac{n}{t}. This yields

 | 2 n − 1 ≥ #𝒰 ≥ 2 n ( 1 − ( 1 − 2 − n / t) t) = 2 n − ( 2 n / t − 1) t, 2^{n-1}\geq\#\mathcal{U}\geq 2^{n}\left(1-\left(1-2^{-n/t}\right)^{t}\right)=2^{n}-\left(2^{n/t}-1\right)^{t}, |  |

equivalently

 | n ≥ t ⋅ log 2 ⁡ ( 1 1 − 2 − 1 / t). n\geq t\cdot\log_{2}\left(\frac{1}{1-2^{-1/t}}\right). |  |

Using e − x > 1 − x e^{-x}>1-x with x = ln ⁡ 2 t x=\frac{\ln 2}{t} one obtains

 | n > t ⋅ log 2 ⁡ ( t ln ⁡ 2). n>t\cdot\log_{2}\left(\frac{t}{\ln 2}\right). |  |

Straightforward but lengthy calculations finally show

 | t < C ​ n log 2 ⁡ n. t<\frac{Cn}{\log_{2}n}. |  |

∎

###### Remark 3.12.

In the above theorem, it seems to be possible to relax the condition

 | t ≥ C ​ n log 2 ⁡ n t\geq\frac{Cn}{\log_{2}n} |  |

to

 | t ≥ ( 1 + o ⁡ ( 1)) ​ n log 2 ⁡ n, t\geq\frac{(1+o(1))n}{\log_{2}n}, |  |

where o ⁡ ( 1) o(1) denotes a function varying in n n and tending to 0 0 as n n tends to infinity. While this will not affect the considerations below very much, it might be of separate interest to investigate optimal conditions for Theorem 3.11 and related statements.

To continue we repeat some notions from graph theory, see [11] for a detailed introduction. For a set X X let ( X 2) {X\choose 2} be the set of two element subsets of X X. Let G = ( V, E) G=(V,E) be a (simple) graph. A *clique*in G G is a subset X ⊆ V X\subseteq V with

 | ( X 2) ⊆ E. {X\choose 2}\subseteq E. |  |

The *clique number*ω ⁡ ( G) \omega(G) of G G is the size of a largest clique in G G. A set A ⊆ V A\subseteq V is an *independent set*in G G if

 | ( A 2) ∩ E = ∅. {A\choose 2}\cap E=\emptyset. |  |

The *independence number*α ⁡ ( G) \alpha(G) of G G is the size of a largest independent set in G G. The inequality α ⁡ ( G) < t \alpha(G)<t is equivalent to the statement that any t t vertices contain at least one edge. Denoting by G ¯ ≔ ( V, ( V 2) ∖ E) \overline{G}\coloneqq(V,{V\choose 2}\setminus E) the *complement*of G G, by definition it holds α ⁡ ( G) = ω ⁡ ( G ¯) \alpha(G)=\omega(\overline{G}). *Turán’s theorem*[24] gives a bound on the number of edges in a graph with a given clique number.

###### Theorem 3.13.

Let G = ( V, E) G=(V,E) be a graph on #​ V = n \#V=n vertices and #​ E = m \#E=m edges. Let t ∈ ℕ t\in\mathbb{N}.

- (i)

If ω ⁡ ( G) < t \omega(G)<t then m ≤ ( 1 − 1 t − 1) ⋅ n 2 2 m\leq\left(1-\frac{1}{t-1}\right)\cdot\frac{n^{2}}{2}.

- (ii)

If α ⁡ ( G) < t \alpha(G)<t then m ≥ 1 t − 1 ⋅ n 2 2 − n 2 m\geq\frac{1}{t-1}\cdot\frac{n^{2}}{2}-\frac{n}{2}.

###### Proof.

For (i) see [11]. For (ii) apply (i) to the complement G ¯ \overline{G}. ∎

We will use Turán’s theorem together with Theorem 3.11 to get a bound on the frequency of the most frequent element among a nontrivial, union closed family.

###### Theorem 3.14.

Let n ∈ ℕ, n ≥ 2 n\in\mathbb{N},n\geq 2 and let ℱ ⊆ 𝒫 ⁡ ( n) \mathcal{F}\subseteq\mathcal{P}(n) be a nontrivial, union closed family. Set #​ ℱ = m \#\mathcal{F}=m and assume

 | m ≥ 7 ​ n log 2 ⁡ n. m\geq\frac{7n}{\log_{2}n}. |  |

Then there is an x ∈ [n] x\in[n] with

 | #⁡ { F ∈ ℱ: x ∈ F } ≥ log 2 ⁡ n 3 ​ n ⋅ #​ ℱ. \#\{F\in\mathcal{F}:x\in F\}\geq\frac{\sqrt{\log_{2}n}}{3n}\cdot\#\mathcal{F}. |  |

###### Proof.

By Theorems 3.7 and 3.11 there is a subfamily ℰ ⊆ ℱ \mathcal{E}\subseteq\mathcal{F} with μ:= #​ ℰ ≥ m 2 \mu:=\#\mathcal{E}\geq\frac{m}{2} and such that, setting t:= ⌈ C ​ n log 2 ⁡ n ⌉ t:=\left\lceil\frac{Cn}{\log_{2}n}\right\rceil with C = 1 + e − 1 C=1+e^{-1}, for any A 1, …, A t ∈ ℰ A_{1},...,A_{t}\in\mathcal{E} at least two of these sets have a nonempty intersection. Consider the graph G = ( ℰ, E ⁡ ( G)) G=(\mathcal{E},E(G)) with

 | E ⁡ ( G) = { E 1 ​ E 2 ∈ ( ℰ 2): E 1 ∩ E 2 ≠ ∅ }. E(G)=\left\{E_{1}E_{2}\in{\mathcal{E}\choose 2}:E_{1}\cap E_{2}\neq\emptyset\right\}. |  |

By construction α ⁡ ( G) < t \alpha(G)<t, so that by Theorem 3.13 (ii) we have

 | #​ E ​ ( G) ≥ 1 t − 1 ⋅ μ 2 2 − μ 2. \#E(G)\geq\frac{1}{t-1}\cdot\frac{\mu^{2}}{2}-\frac{\mu}{2}. |  |

For every E 1 ​ E 2 ∈ E ⁡ ( G) E_{1}E_{2}\in E(G) pick a c ⁡ ( E 1 ​ E ​ 2) ∈ E 1 ∩ E 2 c(E_{1}E2)\in E_{1}\cap E_{2}. This defines an edge coloring c: E ⁡ ( G) → [n] c:E(G)\rightarrow[n]. Consequently, there is an x ∈ [n] x\in[n] that appears on at least

 | 1 n ⋅ ( 1 t − 1 ⋅ μ 2 2 − μ 2) \displaystyle\frac{1}{n}\cdot\left(\frac{1}{t-1}\cdot\frac{\mu^{2}}{2}-\frac{\mu}{2}\right) |  | (3.4) |

edges. Let G ′ G^{\prime} be the graph induced by the edges of color x x and let μ ′ \mu^{\prime} be the number of vertices in G ′ G^{\prime}, so that (using ( 3.4) and t ≤ C ​ n log 2 ⁡ n + 1 t\leq\frac{Cn}{\log_{2}n}+1)

 | ( μ ′) 2 2 ≥ ( μ ′ 2) ≥ 1 n ⋅ ( 1 t − 1 ⋅ μ 2 2 − μ 2) ≥ μ 2 2 ​ n ⋅ C ​ n log 2 ⁡ n − μ 2 ​ n, \frac{(\mu^{\prime})^{2}}{2}\geq{\mu^{\prime}\choose 2}\geq\frac{1}{n}\cdot\left(\frac{1}{t-1}\cdot\frac{\mu^{2}}{2}-\frac{\mu}{2}\right)\geq\frac{\mu^{2}}{2n\cdot\frac{Cn}{\log_{2}n}}-\frac{\mu}{2n}, |  |

so that

 | μ ′ ≥ μ 2 ​ log 2 ​ n C ​ n 2 − μ n \mu^{\prime}\geq\sqrt{\frac{\mu^{2}\log_{2}n}{Cn^{2}}-\frac{\mu}{n}} |  |

The right hand side for μ ≥ m 2 \mu\geq\frac{m}{2} is minimized at μ = m 2 \mu=\frac{m}{2} (using the assumptions from the statement), so that

 | μ ′ ≥ m 2 ​ log 2 ​ n 4 ​ C ​ n 2 − m 2 ​ n = 1 4 ​ C − n 2 ​ m ​ log 2 ⁡ n ⋅ log 2 ⁡ n n ⋅ m. \mu^{\prime}\geq\sqrt{\frac{m^{2}\log_{2}n}{4Cn^{2}}-\frac{m}{2n}}=\sqrt{\frac{1}{4C}-\frac{n}{2m\log_{2}n}}\cdot\frac{\sqrt{\log_{2}n}}{n}\cdot m. |  |

Using again the assumptions we finally obtain

 | #⁡ { F ∈ ℱ: x ∈ F } ≥ μ ′ ≥ 1 4 ​ C − 1 14 ⋅ log 2 ⁡ n n ⋅ m ≥ log 2 ⁡ n 3 ​ n ⋅ m. \#\{F\in\mathcal{F}:x\in F\}\geq\mu^{\prime}\geq\sqrt{\frac{1}{4C}-\frac{1}{14}}\cdot\frac{\sqrt{\log_{2}n}}{n}\cdot m\geq\frac{\sqrt{\log_{2}n}}{3n}\cdot m. |  |

∎

###### Remark 3.15.

There are already known lower bounds on the frequency of a most frequent element in ℱ \mathcal{F}, see [7]. In particular, by [3, 21, 26] respectively (the third being an improvement by a constant of a bound in [16]), it is known that there is an element that is contained in an

 | Ω ⁡ ( max ⁡ { log 2 ⁡ n n, log 2 ⁡ m n, 1 log 2 ⁡ m }) \Omega\left(\max\left\{\sqrt{\frac{\log_{2}n}{n}},\frac{\log_{2}m}{n},\frac{1}{\log_{2}m}\right\}\right) |  |

-fraction of all sets from ℱ \mathcal{F} (for n n and m m sufficiently large). The first lower bound supersedes the bound from Theorem 3.14. Notice however that the above proof does not use all the information known about ℰ \mathcal{E}. In particular, one could assume ℰ \mathcal{E} to be union closed. Also, one might see that the above technique via Turán’s theorem might not be optimal since the intersection E 1 ∩ E 2 E_{1}\cap E_{2} might be very large so that there are a lot of possibilities for c ⁡ ( E 1 ​ E 2) c(E_{1}E_{2}). There is some hope that more refined arguments also yield a better bound.

### 3.4 Intersecting Families

The idea of the proof of Theorem 3.14 was that any union closed family ℱ \mathcal{F} contains a large subfamily ℰ \mathcal{E} so that any sufficiently large quantity of sets from ℰ \mathcal{E} must contain two intersecting sets. One way one could improve the bound from Theorem 3.14 is via the following open question. A family of sets ℰ \mathcal{E} is called *intersecting*if for all A, B ∈ ℰ A,B\in\mathcal{E} it holds A ∩ B ≠ ∅ A\cap B\neq\emptyset.

###### Question 3.16.

For every nontrivial, union closed family ℱ ⊆ 𝒫 ⁡ ( n) \mathcal{F}\subseteq\mathcal{P}(n) does there exist an intersecting subfamily ℰ ⊆ ℱ \mathcal{E}\subseteq\mathcal{F} with #​ ℰ ≥ 1 2 ⋅ #​ ℱ \#\mathcal{E}\geq\frac{1}{2}\cdot\#\mathcal{F}?

This is again a weaker version of the Union Closed Sets Conjecture 1.1, but would strengthen Theorem 3.7. In this context, it is natural to ask about the frequency of a most frequent element in an intersecting family. Even though intersecting families are well studied objects in combinatorics (dating back to [13] for example), this aspect does not seem to have been investigated so far.

###### Theorem 3.17.

Let ℰ ⊆ 𝒫 ⁡ ( n) \mathcal{E}\subseteq\mathcal{P}(n) be an intersecting family of size #​ ℰ = m \#\mathcal{E}=m. There is an x ∈ [n] x\in[n] with

 | #⁡ { E ∈ ℰ: x ∈ F } ≥ 1 2 + 1 4 + m 2 − m n ≥ m − 1 m ​ n ⋅ #​ ℰ. \#\{E\in\mathcal{E}:x\in F\}\geq\frac{1}{2}+\sqrt{\frac{1}{4}+\frac{m^{2}-m}{n}}\geq\sqrt{\frac{m-1}{mn}}\cdot\#\mathcal{E}. |  |

The proof is an adapted version of the proof of Theorem 3.14.

###### Proof.

Consider the graph G = ( ℰ, ( ℰ 2)) G=(\mathcal{E},{\mathcal{E}\choose 2}) and a coloring

 | c: ( ℰ 2) → [n], c ⁡ ( E 1 ​ E 2) ∈ E 1 ∩ E 2. c:{\mathcal{E}\choose 2}\rightarrow[n],c(E_{1}E_{2})\in E_{1}\cap E_{2}. |  |

There is a color x ∈ [n] x\in[n] that appears on at least

 | 1 n ⋅ ( m 2) \frac{1}{n}\cdot{m\choose 2} |  |

edges from G G. Let G ′ G^{\prime} be the subgraph induced by the edges of color x x and let m ′ m^{\prime} be the number of vertices in G ′ G^{\prime}. Thus

 | ( m ′ 2) ≥ 1 n ⋅ ( m 2), {m^{\prime}\choose 2}\geq\frac{1}{n}\cdot{m\choose 2}, |  |

equivalently

 | m ′ ≥ 1 2 + 1 4 + m 2 − m n. m^{\prime}\geq\frac{1}{2}+\sqrt{\frac{1}{4}+\frac{m^{2}-m}{n}}. |  |

Since (by construction) every vertex from G ′ G^{\prime} is a set containing x x, the claim follows. ∎

The bound from the above theorem can be sharp, for example for *projective planes*(see [5] for details). For #​ ℰ ≥ 2 \#\mathcal{E}\geq 2 the theorem gives an element contained in at least ( 2 n) − 1 / 2 ⋅ #ℰ (2n)^{-1/2}\cdot\#\mathcal{E}. Together with Question 3.16 one would then get an element contained in at least an Ω ( n − 1 / 2) \Omega(n^{-1/2}) -fraction of sets from a nontrivial, union closed family ℱ \mathcal{F}. While this is again worse than the bound from [3], one could again try to refine the argument from above. In particular, one can consider the following question.

###### Question 3.18.

What can be said about the frequency of the most frequent element in a nontrivial, union closed, intersecting family ℱ ⊆ 𝒫 ⁡ ( n) \mathcal{F}\subseteq\mathcal{P}(n)?

We finish by stating that it can also be of interest to combine Question 3.18 with Question 2.1. We leave this for future research.

## 4 Acknowledgement

I would like to thank my mentors Christoph Helmberg, Martin Winter and Tino Ullrich of the TU Chemnitz and Tibor Szabó of the FU Berlin, as well as all my colleagues of the TU Chemnitz and FU Berlin for their continued support.

## References

- [1] J. Aaronson, D. Ellis, I. Leader, A Note on Transitive Union-Closed Families, The Electronic Journal of Combinatorics 28(2) #P2.3 (2021)
- [2] B. Amaral, L. Dalton, D. Polakowski, A. Raymond, B. Thomas, The Linear Relaxation of an Integer Program for the Union-Closed Conjecture, [arXiv:2004.05210][3] (2020)
- [3] I. Balla, Minimum density of union-closed families, [arXiv:1106.0369][4] (2011)
- [4] I. Balla, B. Bollobás, T. Eccles, Union-closed families of sets, Journal of Combinatorial Theory, Series A 120, Issue 3, pp. 531-544 (2013)
- [5] T. Beth, D. Jungnickel, H. Lenz, Design Theory, Cambridge University Press, Volume 1, Second Edition (1999)
- [6] G. Brinkmann, R. Deklerck, Generation of Union-Closed Sets and Moore Families, Journal of Integer Sequences 21, Article 18.1.7 (2018)
- [7] H. Bruhn, O. Schaudt, The Journey of the Union-Closed Sets Conjecture, Graphs and Combinatorics 31, pp. 2043-2074 (2015)
- [8] N. Caspard, B. Monjardet, The lattices of closure systems, closure operators, and implicational systems on a finite set: a survey, Discrete Applied Mathematics 127, Issue 2, pp. 241-269 (2003)
- [9] B. A. Davey, H. A. Priestley, Introduction to Lattices and Order, Cambridge University Press, Second Edition (2002)
- [10] A. Day, The Lattice Theory of Functional Dependencies and Normal Decompositions, International Journal of Algebra and Computation 2, Number 4, pp. 409-431 (1992)
- [11] R. Diestel, Graph Theory, Springer-Verlag, Graduate Texts in Mathematics, Volume 173, Fifth Edition (2016/17)
- [12] D. Ellis, M.-R. Ivan, I. Leader, Small sets in union-closed families, [arXiv:2201.11484][5] (2022)
- [13] P. Erdős, C. Ko, R. Rado, Intersection Theorems for Systems of Finite Sets, The Quarterly Journal of Mathematics, Volume 12, Issue 1, pp. 313-320 (1961)
- [14] W. T. Gowers, et al., [gowers.wordpress.com/2016/01/21/frankls-union-closed-conjecture-a-possible-polymath-project/][6] (2016)
- [15] I. Karpas, Two Results on Union-Closed Families, [arXiv:1708.01434][7] (2017)
- [16] E. Knill, Graph Generated Union-closed Families of Sets, [arXiv:math/9409215][8] (1994)
- [17] U. Leck, I. T. Roberts, J. Simpson, Minimizing the weight of the union-closure of families of two-sets, Australasian Journal of Combinatorics 52, pp. 67-73 (2012)
- [18] J. Maßberg, The Union-Closed Sets Conjecture for Small Families, Graphs and Combinatorics 32, pp. 2047-2051 (2016)
- [19] Y. Peng, P. Sissokho, C. Zhao, An extremal problem for set families generated with the union and symmetric difference operations, Journal of Combinatorics 3, Number 4, pp. 651-668 (2012)
- [20] A. Raz, Note on the union-closed sets conjecture, The Electronic Journal of Combinatorics 24(3) #P3.53 (2017)
- [21] D. Reimer, An Average Set Size Theorem, Combinatorics, Probability and Computing 12, Issue 1, pp. 89-93 (2003)
- [22] L. Studer, An asymptotic version of the union-closed sets conjecture, The American Mathematical Monthly, Volume 128, Issue 7, pp. 652-654 (2021)
- [23] C. Tian, Union-closed Sets Conjecture Holds for Height H ⁡ ( ℱ) ≤ 3 H(\mathcal{F})\leq 3 and H ⁡ ( ℱ) ≥ n − 1 H(\mathcal{F})\geq n-1, [arXiv:2112.06659][9] (2021)
- [24] P. Turán, On an extremal problem in graph theory, Matematikai és Fizikai Lapok 48, pp. 436-452 (1941)
- [25] B. Vučković, M. Živković, The 12-Element Case of Frankl’s Conjecture, IPSI BgD Transactions on Internet Research, Volume 13, Number 1, pp. 65-71 (2017)
- [26] P. Wójcik, Union-closed families of sets, Discrete Mathematics 199, Issues 1-3, pp. 173-182 (1999)


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: https://arxiv.org/pdf/2004.05210
[4]: https://arxiv.org/pdf/1106.0369
[5]: https://arxiv.org/pdf/2201.11484
[6]: https://gowers.wordpress.com/2016/01/21/frankls-union-closed-conjecture-a-possible-polymath-project/
[7]: https://arxiv.org/pdf/1708.01434
[8]: https://arxiv.org/pdf/math/9409215
[9]: https://arxiv.org/pdf/2112.06659
