<!-- ✗ DEFECTIVE SOURCE FILE — DO NOT USE. This file was downloaded as arXiv:math/0208012 but contains "Anchored vector bundles and algebroids" (differential geometry), NOT Vaughan's "Families implying the Frankl conjecture" (Eur. J. Combin. 23, 2002). The correct Vaughan content is carried via Morris (math/0702348), Poonen errata, Pulaj, and the Bruhn-Schaudt survey. See research/summaries/vaughan-families-implying-frankl-2002.md. -->

<!-- source: https://arxiv.org/html/math/0208012 | converted from HTML -->

Anchored vector bundles and algebroids

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: Assumed arXiv.org perpetual non-exclusive license][2]

arXiv:math/0208012v1 [math.DG] 02 Aug 2002

# Anchored vector bundles and algebroids

Michel Nguiffo Boyom Address: GTA UMR CNRS 5030 Université Montpellier2 Email address: [boyom@math.univ-montp2.fr][3]

###### Abstract.

Inspired by recent works of Zang Liu, Alan Weinstein and Ping Xu, we introduce the notions of CC algebroids and non asymmetric Courant algebroids and study these structures. It is shown that CC algebroids of rank greater than 3 are the same as Courant algebroids up to a constant factor, though the definition of CC algebroids is much simpler than that of Courant algebroids,requiring only 2 axioms instead of 5. The situation is similar to that of Lie algebroids, where in the usual definition used by all of he experts there is a redundant axiom, e.g.[GG,KO1,KO2,MK,PL].
Non asymmetric Courant algebroids are shown to be nothing but (pseudo)clan bundles (in the sense of E.B. Vinberg-Katz) which arise in affine geometry of convex bounded domains. The study of CC algebroids and non asymmetric Courant algebroids involves the cohomology theory of Koszul-Vinberg algebras and their modules.

###### Key words and phrases:

algebroids , anomaly , non asymmetric , Koszul-Vinberg algebra , clans , hessian

###### 1991 Mathematics Subject Classification

Primaries 53B05 , 53C15 . Secondaries 54U15 , 55R10 , 57R22

## 1. INTRODUCTION

Let M M be a connected smooth manifold and V V be a real vector bundle on M M. The main subject of the present paper is the study of smooth vector bundles with extra algebraic or geometric structures .
Let Γ ⁡ ( V) \Gamma(V) be the real vector space of smooth sections of V V. A vector bundle morphism ρ \rho from V V to the tangent bundle of the base manifold M M is called an anchor. The vector space Γ ⁡ ( V) \Gamma(V) is a (left) module of the associative commutative algebra F ​ ( M):= C ∞ ​ ( M) F(M):=C^{\infty}(M) of smooth real valued functions on M M, but in general the multiplication defining a real algebra structure of Γ ⁡ ( V) \Gamma(V) is not required to be F ⁡ ( M) F(M) - bilinear. The role of the anchor map is to control relationships between the algebra structure of Γ ⁡ ( V) \Gamma(V) and its F ⁡ ( M) F(M) -module structure. That is the main idea behind geometric objets such as Lie algebroids, Koszul-Vinberg algebroids, Lie-Rinehart algebras and Courant algebroids.
On the other hand the anchor ρ \rho induces a linear map from the vector space Γ ⁡ ( V) \Gamma(V) to the vector space X ⁡ ( M) X(M) of smooth vector fields on the base manifold M M.
There are two situations depending on whether the multiplication map in Γ ⁡ ( V) \Gamma(V) is skew symmetric or not.
To each skew symmetric multiplication, (that we denote by [.,.] [.,.]), one assigns the so called Jacobi anomaly, namely

 | J ⁡ ( s, s ′, s ​ ") = ∮ [[s, s ′], s ​ "] J(s,s^{\prime},s")=\oint[[s,s^{\prime}],s"] |  |

where ∮ \oint denotes the cyclic sum in s, s ′, s ​ " s,s^{\prime},s"

In the present paper, multiplications which are not skew symmetric will be called non asymmetric. To each non asymmetric multiplication we will assign its Koszul-Vinberg anomaly, namely

 | K ​ V ​ ( s, s ′, s ​ ") = ( s, s ′, s ​ ") − ( s ′, s, s ​ ") KV(s,s^{\prime},s")=(s,s^{\prime},s")-(s^{\prime},s,s") |  |

where ( s, s ′, s ") = s. ( s ′. s ") − ( s. s ′). s " (s,s^{\prime},s")=s.(s^{\prime}.s")-(s.s^{\prime}).s" is the associator (which vanishes for associative algebras).

From a non asymmetric multiplication, say s. s ′ s.s^{\prime}, one can construct a skew symmetric one by setting

 | [s, s ′] = s. s ′ − s ′. s [s,s^{\prime}]=s.s^{\prime}-s^{\prime}.s |  |

The Jacobi anomaly of the last bracket is related to the Koszul-Vinberg anomaly by the following equation

 | J ⁡ ( s, s ′, s ​ ") = ∮ K ⁡ ( s, s ′, s ​ ") J(s,s^{\prime},s")=\oint K(s,s^{\prime},s") |  |

Given an element s s of Γ ⁡ ( V) \Gamma(V), its image ρ ⁡ ( s) \rho(s) under the anchor map acts on F ⁡ ( M) F(M) as first order differential operator. The relationship between the real algebra structure of Γ ⁡ ( V) \Gamma(V) and its F ⁡ ( M) F(M) -module structure is controlled by the following Leibniz anomaly

 | L ( s, f, s ′) = s. ( f s ′) − ( ρ ( s) f) s ′ − f ( s. s ′) \textit{L}(s,f,s^{\prime})=s.(fs^{\prime})-(\rho(s)f)s^{\prime}-f(s.s^{\prime}) |  |

We will call an almost algebroid on the base manifold M M any couple ( V,.) (V,.) consisting of a vector bundle V V on M M together with a real algebra structure ( Γ ( V),.) (\Gamma(V),.) in the vector space of smooth sections of V V.

The present work is concerned with the study of the couple ( J ⁡ ( s, s ′, s ​ "), L ⁡ ( s, f, s ′)) (J(s,s^{\prime},s"),L(s,f,s^{\prime})) (resp. ( K ​ V ​ ( s, s ′, s ​ "), L ⁡ ( s, f, s ′)) (KV(s,s^{\prime},s"),L(s,f,s^{\prime}))) of Jacobi anomaly and Leiniz anomaly (resp. the Koszul-Vinberg anomaly and Leibniz anomaly) of an anchored almost algebroid whose multplication is skew symmetric (resp. non asymmetric).
For instance one easily sees that

 | ( J ⁡ ( s, s ′, s ​ "), L ⁡ ( s, f, s ′)) = ( 0, 0) ​ ∀ s, s ′ ∈ Γ ⁡ ( V) ​ ∀ f ∈ F ⁡ ( M) (J(s,s^{\prime},s"),L(s,f,s^{\prime}))=(0,0)\,\,\forall s,s^{\prime}\in\Gamma(V)\,\forall f\in F(M) |  |

if and only if ( V, ρ, [.,.]) (V,\rho,[.,.]) is a Lie algebroid. On the other hand

 | ( K V ( s, s ′, s "), L ( s, f, s ′) = ( 0, 0) ∀ s, s ′, s " ∈ Γ ( V), ∀ f ∈ F ( M) (KV(s,s^{\prime},s"),L(s,f,s^{\prime})=(0,0)\,\,\forall s,s^{\prime},s"\in\Gamma(V),\,\forall f\in F(M) |  |

if and only if ( V, ρ,.) (V,\rho,.) is a Koszul-Vinberg algebroid.

Our work is inspired by those of Z.J. Liu, A. Weinstein and P. Xu on Dirac structures, (see [LWX1,LWX2].)
We have adopted the use of the cohomology of the algebra F ⁡ ( M) F(M) viewed as a Koszul-Vinberg algebra .
Resolving a old problem raised by Gerstenhaber [GM], we recently constructed the cohomolgy theory of Koszul-Vinberg algebras and their modules which controls deformations of those structures, [NB1]. That cohomology is also related to Poisson geometry [NB2,NB3].
It is remarkable that from each vector bundle V V on the base manifold M M arise two cochain complexes of the Koszul-Vinberg algebra F ⁡ ( M) F(M), namely

( c) C ∗ ​ ( F ⁡ ( M), V) = ⨁ k H ​ o ​ m ​ ( ⨂ k F ⁡ ( M), Γ ⁡ ( V)). |  |  |  |

( c ⋆) C ∗ ​ ( F ⁡ ( M), V ∗) = ⨁ k H ​ o ​ m ​ ( ⨂ k F ⁡ ( M), Γ ⁡ ( V ⋆)). |  |  |  |

To control the Jacobi anomaly and the Leibniz anomaly, the cohomology theory of the Koszul-Vinberg F ⁡ ( M) F(M) turns out to be more efficient than the Hoschschild cohomology of the associative algebra F ⁡ ( M) F(M).
It is reasonable to conjecture that many ingredients that are involved in the theory of Courant algebroid structures and Dirac structures lie in the derived objets of the complexes (c) and ( c ⋆) (c^{\star}).
In the present work, we will introduce the notions of CC algebroids and non asymmetric Courant algebroids. The cochain complexes (c) and ( c ⋆) (c^{\star}) will be used to study these structures.

Our main result concerning CC algebroids is Theorem 5.1 which in particular implies that the system of five axioms in the usual definition of Courant algebroids contains three axioms which are superfluous whenever the rank of the vector bundle is greater than 3. For more details on Courant algebroid structures and related topics, the reader may consult works of Liu-Weinstein-Xu, mainly [LWX1,LWX2].

We take this opportunity to recall that some years ago (1995 and 2000) we have pointed out a similar redundancy in the usual definition of Lie algebroid structures. Namely: a Lie algebroid is an anchored almost Lie algebroid ( V, ρ, [.,.]) (V,\rho,[.,.]) such that the following axioms hold

( A ​ X ​ 1) J ⁡ ( s, s ′, s ​ ") = 0. |  |  |  |

( A ​ X ​ 2) L ⁡ ( s, f, s ′) = 0. |  |  |  |

( A ​ X ​ 3) ρ ⁡ ( [s, s ′]) = [ρ ⁡ ( s), ρ ⁡ ( s ′)] = 0. |  |  |  |

However (AX3) is superfluous .
In fact, it is easily seen that (Ax3) is a consequence of the other two axioms (AX1) and (AX2). The reader is referred to Section 2 of our paper [NB1] in Banach Center Publications , Vol. 54, page 103, Warszawa 2001; ibidem, page 45, DEFINITION 2, joint paper by J.Grabowski and K. Grabowska, [GG], contains the superfluous axiom (AX3). Thereafter, the later joint paper by J.Grabowski and G. Marmo, [GMa], attests that those authors hadn’t read the reference we just recalled.

Another consequence of our Theorem 5.1 is that the theory of Courant algebroid structures of rank less than three differs from that of Courant algebroid structures of rank greater than three. That phenomenon is illustrated by our Example 5.2

Non asymmetric Courant algebroid structures are studied in Section 7 and Section 8. They lead us to features which are quite different from those inherited from CC algebroid structures. Indeed, those structures lead to locally flat (pseudo)clan bundles (Theorem 7.2). That phenomenon is an unexpected incursion of the affine geometry of homogeneous bounded domains in the theory of non asymmetric Courant algebroid structures. We obtain interesting relationships between the differential geometry of non asymmetric Courant algebroid structures and their Koszul-Vinberg cohomology (Theorem 7.5).
An another result concerns the class of non asymmetric Courant algebroid structures with a definite forms <.,. > <.,.>. We will show that under some additional conditions, the cohomology class of <.,. > <.,.> doesn’t vanish (Theorem 8.1). This fact is in contrast to properties of clans which arise from the affine geometry of homogeneous hyperbolic bounded domains, [KV,JLK1,KJ]. (The cohomology theory used in [KJ] is derived from the Chevalley-Eilenberg cohomology theory of Lie algebras). Nevertheless Theorem 8.1 may be compared to similar results in [JLK2] where Jean-Louis Koszul has pointed out a lot of canonical vector bundle valued superorder differential forms whose cohomology classes never vanish. (For instance, the divergence class associated to a volume form , cocycles defined by torsion free linear connection). Two examples of clan bundle and pseudo clan bundle are given in Section 8. Section 9 is devoted to some miscellaneous items. In section 10 some observations are made about relationships of algebroid structures with various topics.

## 2. ALGEBROIDS

Given a connected smooth manifold M M, the associative algebra of smooth real valued functions defined on M M is denoted by F ⁡ ( M) F(M).

Let V V be a smooth vector bundle on M M and let Γ ⁡ ( V) \Gamma(V) be the vector space of smooth sections of V. V. We shall consider Γ ⁡ ( V) \Gamma(V) as a Koszul-Vinberg module of F ⁡ ( M) F(M) by setting the following axioms

( 1) ( s ​ f) ​ ( x) = ( f ​ s) ​ ( x) = f ⁡ ( x) ​ s ​ ( x) |  |  |  |

for any s s in Γ ⁡ ( V) \Gamma(V) and any f f in F ⁡ ( M). F(M). A vector bundle V V will be called an almost algebroid whenever Γ ⁡ ( V) \Gamma(V) is endowed with a real algebra structure. Therefore the product of two sections s s and s ′ s^{\prime} will be denoted by s ​ s ′ ss^{\prime}.

Given an almost algebroid, it is to be noticed that in general Γ ⁡ ( V) \Gamma(V) is not an algebra over the ring F ⁡ ( M). F(M).
A vector bundle V V on M M together with a vector bundle morphism ρ \rho to the tangent bundle T ​ M TM is called anchored vector bundle. The anchor ρ \rho induces a map from Γ ⁡ ( V) \Gamma(V) to Γ ⁡ ( T ​ M) \Gamma(TM) which is F ⁡ ( M) F(M) linear. The anchor map of an anchored almost algebroid V V is used to relate the F ⁡ ( M) F(M) -module structure of Γ ⁡ ( V) \Gamma(V) with its real algebra structure. Such relationships yield to the concept of labelled algebroids.
Before pursuing, let us recall some important labelled almost algebroid structures .

(e1): A Lie algebroid is an anchored almost Lie algebroid ( V, ρ, [.,.]) (V,\rho,[.,.]) such that

( 2 i) ( Γ ( V), [.,.]) is a real Lie algebra.  |  |  |  |

Given s s, s ′ s^{\prime} in Γ ⁡ ( V) \Gamma(V) and f f in F ⁡ ( M) F(M) one has

( 2 ​ i ​ i) [s, f ​ s ′] = ( ρ ⁡ ( s) ​ f) ​ s ′ + f ⁡ [s, s ′]. |  |  |  |

(e2): A Koszul-Vinberg algebroid is an anchored almost algebroid ( V, ρ,.) (V,\rho,.) such that given elements s s, s ′ s^{\prime} and s ​ " s" of Γ ⁡ ( V) \Gamma(V) and an element f f of F ⁡ ( M), F(M), one has

( 3 i) s. ( s ′. s ") − ( s. s ′). s " − s ′. ( s. s ") + ( s ′. s). s " = 0. |  |  |  |

( 3 i ​ i) ( f s). s ′ − f ( s. s ′) = 0. |  |  |  |

( 3 i ​ i ​ i) s. ( f s ′) − ( ρ ( s) f) s ′ − f ( s. s ′) = 0. |  |  |  |

## 3. ALMOST LIE ALGEBROIDS

In this section, we will be concerned with the so called almost Lie algebroid structures, viz those almost algebroids ( V, [.,.]) (V,[.,.]) whose multiplications [.,.] [.,.] are skew symmetric. Let ( V, [.,.]) (V,[.,.]) be an anchored almost Lie algebroid on M M. Let s s, s ′ s^{\prime} and s ​ " s" be sections of V V and let f f be an element of F ⁡ ( M) F(M). The only obstructions for an almost Lie algebroid ( V, ρ, [.,.]) (V,\rho,[.,.]) to be an Lie algebroid are

(ob1): Jacobi anomaly

 | J ⁡ ( s, s ′, s ​ ") = ∮ [[s, s ′], s ​ "]. J(s,s^{\prime},s")=\oint[[s,s^{\prime}],s"]. |  |

(ob2): Leibniz anomaly

 | L ⁡ ( s, f, s ′) = [s, f ​ s ′] − ( ρ ⁡ ( s) ​ f) ​ s ′ − f ⁡ [s, s ′]. L(s,f,s^{\prime})=[s,fs^{\prime}]-(\rho(s)f)s^{\prime}-f[s,s^{\prime}]. |  |

Regarding the case of non asymmetric anchored almost algebroid structure, we will replace the Jacobi anomaly by the following quantity,which is called Koszul-Vinberg anomaly:

( 4) K V ( s, s ′, s ") = s. ( s ′. s ") − ( s. s ′). s " − s ′. ( s. s ") + ( s ′. s). s ". |  |  |  |

We intend to point out that the cohomology theory of Koszul-Vinberg algebras and their modules provides tools which are useful in studying the Jacobi anomaly and the Koszul-Vinberg anomaly. This idea has been inspired to us by the theory of Courant algebroid structures. [LWX1,LWX2,LW], see also [UK].

## 4. KV-COHOMOLOGY H ∗ ​ ( F ​ ( M), V) H^{\ast}(F(M),V)

Recall that an algebra A A whose associator is symmetric with respect to the first two arguments, viz K ​ V ​ ( a, b, c) = 0 KV(a,b,c)=0 ∀ a, b, c ∈ A \forall a,b,c\in A, is called a Koszul-Vinberg algebra. In particular any associative algebra is a Koszul-Vinberg algebra . So is the case for F ⁡ ( M) F(M) when it is endowed with its natural associative commutative real algebra structure.
A two-sided module of F ⁡ ( M) F(M), say W W, is called a Koszul-Vinberg module if the following identities hold

 | f ⁡ ( g ​ w) − ( f ​ g) ​ w = g ⁡ ( f ​ w) − ( g ​ f) ​ w f(gw)-(fg)w=g(fw)-(gf)w |  |

 | f ⁡ ( w ​ g) − ( f ​ w) ​ g = w ⁡ ( f ​ g) − ( w ​ f) ​ g, ∀ f, g ∈ F ⁡ ( M), ∀ w ∈ W f(wg)-(fw)g=w(fg)-(wf)g,\,\forall f,g\in F(M),\,\forall w\in W |  |

Let V V be a vector bundle on M M. Then, according to (1), the vector space Γ ⁡ ( V) \Gamma(V) is a Koszul-Vinberg module of F ⁡ ( M) F(M). We shall deal with the cochain complex whose k t ​ h k^{th} homogeneous space is the vector space C k ​ ( F ​ ( M), V) C^{k}(F(M),V) of k k -multi-linear maps from F ⁡ ( M) F(M) to Γ ⁡ ( V) \Gamma(V), k k being a positive integer. When k k = 0 we set

 | C 0 ​ ( F ⁡ ( M), V) = Γ ⁡ ( V) C^{0}(F(M),V)=\Gamma(V) |  |

The coboundary operator

 | δ: C k ​ ( F ⁡ ( M), V) → C OPEN k + 1) ​ ( F ⁡ ( M), V) \delta:C^{k}(F(M),V)\rightarrow C^{k+1)}(F(M),V) |  |

is defined as follows

( 5 i) δ = 0 i ​ f ​ k = 0. |  |  |  |

If k k is a positive integer, then

( 5 i ​ i) δ ( Θ) ( a 1,.., a k + 1) = ∑ j ( − 1) j ( ( a j Θ) ( a 1,.., a ^ j,.., a k + 1) + |  |  |  |

 | a k + 1 ( Θ ( a 1,.., a ^ j, …, a k, a j))) a_{k+1}(\Theta(a_{1},..,\hat{a}_{j},...,a_{k},a_{j}))) |  |

where

 | ( a j Θ) ( a 1,., a k) = a j ( Θ ( a 1, …, a k)) − ∑ r Θ ( a 1, …, a j a r, …, a k) (a_{j}\Theta)(a_{1},.,a_{k})=a_{j}(\Theta(a_{1},...,a_{k}))-\sum_{r}\Theta(a_{1},...,a_{j}a_{r},...,a_{k}) |  |

It is easy to check that

 | H 0 ​ ( F ⁡ ( M), V) = Γ ⁡ ( V), H^{0}(F(M),V)=\Gamma(V), |  |

 | H 1 ​ ( F ⁡ ( M, V) = D ​ e ​ r ​ ( F ⁡ ( M, Γ ⁡ ( V)) CLOSE CLOSE. H^{1}(F(M,V)=Der(F(M,\Gamma(V)). |  |

Thus, two cocycles in C 1 ​ ( F ​ ( M), V) C^{1}(F(M),V) are cohomologuous if and only if there are equal.

Let ( V, ρ, [.,.]) (V,\rho,[.,.]) be an anchored almost Lie algebroid and let us suppose that the corresponding vector bundle is endowed with a symmetric bilinear form which is denoted by <.,. > <.,.>. We adopt notations of [LWX1,LWX2]. To each triple ( s s, s ′ s^{\prime}, s ​ " s") of elements of Γ ⁡ ( V) \Gamma(V) we assign the smooth function T ⁡ ( s, s ′, s ​ ") T(s,s^{\prime},s") which is defined by

 | T ⁡ ( s, s ′, s ​ ") = ∮ < [s, s ′], s ​ " >. T(s,s^{\prime},s")=\oint<[s,s^{\prime}],s">. |  |

The high lighted focus in the theory of Courant algebroid structures consists of using the function T T to control the Jacobi anomaly (see [LWX1,LWX2]).

## 5. THE MAIN THEOREM

Keeping in mind the notations used above, we are in position to prove the following statement.

###### Theorem 5.1.

Let ( V, [.,.], ρ) (V,[.,.],\rho) be an anchored almost Lie algebroid on M M. Let one suppose that the following assumptions to hold.
(i) The vector bundle V V is endowed with a non degenerate symmetric bilinear form which is denoted by <.,. > <.,.>.
(ii) There is a cocycle D D in C 1 ​ ( F ​ ( M), V) C^{1}(F(M),V) satisfying the following two identities

( r ​ 1) J ⁡ ( s, s ′, s ​ ") = D ⁡ ( T ⁡ ( s, s ′, s ​ ")) ∀ s, s ′, s ​ " ∈ Γ ⁡ ( V). |  |  |  |

( r 2) ρ ( s) ( < s ′, s " >) = < [s, s ′] + D ( < s, s ′ >), s " > + < s ′, [s, s "] + D ( < s, s " >) >. |  |  |  |

If r ​ a ​ n ​ k ​ ( V) > 3, rank(V)>3, then the anchor map ρ \rho satisfies the following identity

 | ρ ⁡ ( [s, s ′]) = [ρ ⁡ ( s), ρ ⁡ ( s ′)] \rho([s,s^{\prime}])=[\rho(s),\rho(s^{\prime})] |  |

Proof
Following [UK], the hypothesis (r2) allows one to control the Leibniz anomaly. More precisely let f ∈ F ⁡ ( M) f\in F(M). Taking in account both (r2) and the the δ \delta -closeness of D D, a direct calculation of the quantity ρ ⁡ ( s) ​ ( < f ​ s ′, s ​ " >) \rho(s)(<fs^{\prime},s">) yields to the following identity

( 6) [s, f ​ s ′] − ( ρ ⁡ ( s) ​ f) ​ s ′ − f ⁡ [s, s ′] = − < s, s ′ > ​ D ​ ( f). |  |  |  |

Let s s and s ′ s^{\prime} be fixed elements of Γ ⁡ ( V) \Gamma(V). Under the assumption that r ​ a ​ n ​ k ​ ( V) > 3, rank(V)>3, we can choose a non zero element s ​ " s" of Γ ⁡ ( V) \Gamma(V) such that

 | < s, s ​ " > = < s ′, s ​ " > = < [s, s ′], s ​ " >= 0. <s,s">=<s^{\prime},s">=<[s,s^{\prime}],s">=0. |  |

Therefore, for each f ∈ F ⁡ ( M) f\in F(M) the Jacobi anomaly J (, s, s ′, f s ") J(,s,s^{\prime},fs") is reduced to

( 7) J ⁡ ( s, s ′, f ​ s ​ ") = f ​ J ​ ( s, s ′, s ​ ") + T ⁡ ( s, s ′, s ′) ​ D ​ ( f) + ( ρ ⁡ ( [s, s ′]) ​ f − [ρ ⁡ ( s), ρ ⁡ ( s ′)] ​ f) ​ s ​ ". |  |  |  |

On the other hand, under the same hypothesis as above, one easily checks the following identity

 | T ⁡ ( s, s ′, f ​ s ​ ") = f ​ T ​ ( s, s ′, s ​ "). T(s,s^{\prime},fs")=fT(s,s^{\prime},s"). |  |

By the virtu of (r1), the following identity holds

 | J ⁡ ( s, s ′, f ​ s ​ ") = D ⁡ ( T ⁡ ( s, s ′, f ​ s ​ ")). J(s,s^{\prime},fs")=D(T(s,s^{\prime},fs")). |  |

Combining those results with the closeness assumption δ ⁡ ( D) = o, \delta(D)=o, we conclude that the following quantity

 | ρ ⁡ ( [s, s ′]) ​ f − ρ ⁡ ( s) ​ ( ρ ⁡ ( s ′) ​ f) + ρ ⁡ ( s ′) ​ ( ρ ⁡ ( s) ​ f) \rho([s,s^{\prime}])f-\rho(s)(\rho(s^{\prime})f)+\rho(s^{\prime})(\rho(s)f) |  |

vanishes identically. That ends the proof of Theorem 5.1 □ \square

EXAMPLE 5.2

Theorem 5.1 fails when the r ​ a ​ n ​ k ​ ( V) < 3. rank(V)<3.
Indeed, let 𝐌 \mathbf{M} be the field of real numbers. Let us set

 | V = M × R. V=M\times R. |  |

Elements of V V are denoted by ( x, y x) (x,y_{x}) where x x and y x y_{x} are two real numbers.
On the other hand, let us denote the tangent bundle of M M by

 | T M = M × R ∂ x. TM=M\times R\partial_{x}. |  |

Smooth sections of V V are real valued smooth functions of one real variable. Let f f, g g and h h be three real valued smooth functions defined on M M. Let us define the bilinear symmetric form on V V by setting

 | < f, g > ( x) = f ⁡ ( x) ​ g ​ ( x) ​ ∀ f, g ∈ Γ ⁡ ( V). <f,g>(x)=f(x)g(x)\,\,\forall f,g\in\Gamma(V). |  |

We define the almost Lie algebroid structure on V V by the following bracket

 | [f, g] = f ​ ∂ x g − g ​ ∂ x f ​ ∀ f, g ∈ Γ ⁡ ( V). [f,g]=f\partial_{x}g-g\partial_{x}f\,\,\forall f,g\in\Gamma(V). |  |

We now define the anchor map ρ \rho on Γ ⁡ ( V) \Gamma(V) by putting

 | ρ ( f) = 2 f ∂ x. \rho(f)=2f\partial_{x}. |  |

The 1-cocycle D ∈ C 1 ​ ( F ⁡ ( M), V) D\in C^{1}(F(M),V) is defined by

 | D ⁡ ( f) = ∂ x f. D(f)=\partial_{x}f. |  |

The reader will easily verify that the data just defined, say ( V, ρ, [.,.], <.,. >, D), (V,\rho,[.,.],<.,.>,D), satisfy both conditions (r1) and (r2) of Theorem 5.1. Nevertheless it is easily seen that the conclusion of Theorem 5.1 fails ◊ \lozenge

## 6. CC ALGEBROIDS

Considerations to be discussed in this section are inspired by Theorem 5.1 and some problems which are raised in [LWX2] and in [UK].

###### Definition 6.1.

A CC algebroid is a datum ( V, ρ, [.,.], <.,. >, D) (V,\rho,[.,.],<.,.>,D) where ( V, ρ, [.,.], <.,. >) (V,\rho,[.,.],<.,.>) is an anchored almost Lie algebroid endowed with a non degenerate bilinear symmetric form <.,. > <.,.> and D D is 1-cocycle in C 1 ​ ( F ​ ( M), V) C^{1}(F(M),V) with relationships (r1) and (r2) stated in Theorem 5.1, namely

( r ​ 1) J ⁡ ( s, s ′, s ​ ") = D ⁡ ( T ⁡ ( s, s ′, s ​ ") ​ ∀ s, s ′, s ​ " ∈ Γ ⁡ ( V) CLOSE. |  |  |  |

( r 2) ρ ( s) < s ′, s " > = < [s, s ′] + D ( < s, s ′ >), s " > + < s ′, [s, s "] + D ( < s, s " >) > |  |  |  |

The notion of CC algebroid structure that we just introduced is different from that of Courant algebroid structures studied by Lu, Weinstein and Xu.(See [LWX1],LWX2]). Below is the usually given definiton of Courant algebroid structures

###### Definition 6.2.

([LWX1,LWX2]) A Courant algebroid is an anchored almost Lie algebroid, say ( V, ρ, [.,.] (V,\rho,[.,.], endowed with a non degenerate symmetric 2-form <.,. > <.,.> and with a 1-cocycle D ∈ C 1 ​ ( F ⁡ ( M), V) D\in C^{1}(F(M),V) subject to satisfy the following five axioms
∀ s, s ′, s ​ " ∈ Γ ⁡ ( V), ∀ f ∈ F ⁡ ( M) \forall s,s^{\prime},s"\in\Gamma(V),\forall f\in F(M) the following identities hold

A ​ x ​ 1 3 ​ J ​ ( s, s ′, s ​ ") = D ⁡ ( T ⁡ ( s, s ′, s ​ ") CLOSE. |  |  |  |

A ​ x ​ 2 ρ ⁡ ( [s, s ′]) = [ρ ⁡ ( s), ρ ⁡ ( s ′)]. |  |  |  |

A ​ x ​ 3 [s, f ​ s ′] = ( ρ ⁡ ( s) ​ f) ​ s ′ + f ⁡ [s, s ′] − < s, s ′ > D ⁡ ( f). |  |  |  |

A ​ x ​ 4 ρ ⁡ ( D ⁡ ( f)) = 0. |  |  |  |

A x 5 ρ ( s) < s ′, s " > = < [s, s ′] + D ( < s, s ′ >), s " > + < s ′, [s, s "] + D ( < s, s " >) > |  |  |  |

###### Remark 6.3.

Our Theorem 5.1 implies that up to a constant factor, each CC algebroid of r ​ a ​ n ​ k > 3 rank>3 is a Courant algebroid. Our assertion is made clear by the following Proposition which is a straight corollary of Theorem 5.1.

###### Proposition 6.4.

Let ( V, ρ, [.,.], D, <.,. >) (V,\rho,[.,.],D,<.,.>) be a CC algebroid whose rank is greater than three. Then, ∀ s, s ′, s ​ " ∈ Γ ⁡ ( V) \forall s,s^{\prime},s"\in\Gamma(V) and ∀ f ∈ F ⁡ ( M) \forall f\in F(M) the following identities hold

( i) [s, f ​ s ′] = ( ρ ⁡ ( s) ​ f) ​ s ′ + f ⁡ [s, s ′] − < s, s ′ > D ⁡ ( f) |  |  |  |

( i ​ i) ρ ⁡ ( [s, s ′]) = [ρ ⁡ ( s), ρ ⁡ ( s ′)] |  |  |  |

( i ​ i ​ i) ρ ⁡ ( D ⁡ ( f)) = 0. |  |  |  |

Proof
By the virtue of (r2), (Theorem 5.1), a direct calculation of ρ ⁡ ( s) ​ < f ​ s ′, s ​ " > \rho(s)<fs^{\prime},s"> yields to Identity (i). Identity (ii) is nothing but the conclusion of Theorem 5.1. To end the proof, one only calculates the following expression

 | ρ ⁡ ( [s, f ​ s ′]) = ( ρ ⁡ ( s) ​ f) ​ ρ ​ ( s ′) + f ​ ρ ​ ( [s, s ′]) − < s, s ′ > ​ ρ ​ ( D ⁡ ( f)) \rho([s,fs^{\prime}])=(\rho(s)f)\rho(s^{\prime})+f\rho([s,s^{\prime}])-<s,s^{\prime}>\rho(D(f)) |  |

Taking into account that Identity (ii) holds, one easily checks the following

 | < s, s ′ > ​ ρ ​ ( D ⁡ ( f)) = 0 <s,s^{\prime}>\rho(D(f))=0 |  |

Proposition 6.4 is proved. □ \square

Here is an another direct consequence of Definition 6.1 :

###### Theorem 6.5.

Given a CC algebroid ( V, ρ, [.,.], <.,. >, D) (V,\rho,[.,.],<.,.>,D), the following assertions are equivalent:

( A ​ 1) ρ ⁡ ( [s, s ′]) = [ρ ⁡ ( s), ρ ⁡ ( s ′)] ​ ∀ s, s ′ ∈ Γ ⁡ ( V) |  |  |  |

( A ​ 2) ρ ⁡ ( D ⁡ ( f)) = 0 ​ ∀ f ∈ F ⁡ ( M). |  |  |  |

Proof.
First. (A2) implies (A1)

Step1. If r ​ a ​ n ​ k ​ ( V) = 1, rank(V)=1, then, let us choose s ∈ Γ ⁡ ( V) s\in\Gamma(V) such that s s is a basis of the F ⁡ ( M) F(M) -module Γ ⁡ ( V) \Gamma(V) in an open subset U ⊂ M. U\subset M. Therefore, let V U V_{U} be the inverse image of U U under the projection of V V on M. M. Then, ∀ s ′ ∈ Γ ⁡ ( V U), \forall s^{\prime}\in\Gamma(V_{U}), ∃ f ∈ F ⁡ ( M) \exists f\in F(M) such that s ′ = f ​ s. s^{\prime}=fs. The Leibniz equation gives the following identity

 | [s, s ′] = [s, s ​ f] = ( ρ ⁡ ( s) ​ f) ​ s − < s, s > ​ D ​ ( f). [s,s^{\prime}]=[s,sf]=(\rho(s)f)s-<s,s>D(f). |  |

On the other hand, we have

 | [ρ ⁡ ( s), ρ ⁡ ( f ​ s)] = [ρ ⁡ ( s), f ​ ρ ​ ( s)] = ( ρ ⁡ ( s) ​ f) ​ ρ ​ ( s) [\rho(s),\rho(fs)]=[\rho(s),f\rho(s)]=(\rho(s)f)\rho(s) |  |

By the virtue of (A2) we have

 | ρ ⁡ ( [s, f ​ s] = ( ρ ⁡ ( s) ​ f) ​ ρ ​ ( s) CLOSE. \rho([s,fs]=(\rho(s)f)\rho(s). |  |

In conclusion, (A2) implies (A1) if r ​ a ​ n ​ k ​ ( V) = 1. rank(V)=1.

Step2. Suppose that r ​ a ​ n ​ k ​ ( V) > 1 rank(V)>1. Let s, s ′, s ​ " ∈ Γ ⁡ ( V) s,s^{\prime},s"\in\Gamma(V) and f ∈ F ⁡ ( M). f\in F(M). Our hypothesis is that ∀ f ∈ F ⁡ ( M) \forall f\in F(M) one has ρ ⁡ ( D ⁡ ( f)) = 0. \rho(D(f))=0.. Then, the calculation of ρ ⁡ ( J ⁡ ( s, s ′, f ​ s ​ ")) \rho(J(s,s^{\prime},fs")) yields to

 | ρ ( J ( s, s ′, f s ") = ( ρ ( [s, s ′]) − [ρ ( s, ρ ( s ′)]) f) ρ ( s ") + \rho(J(s,s^{\prime},fs")=(\rho([s,s^{\prime}])-[\rho(s,\rho(s^{\prime})])f)\rho(s")+ |  |

 | < s ′, s ​ " > ρ ⁡ ( [s, D ⁡ ( f)]) − < s, s ​ " > ρ ⁡ ( [s ′, D ⁡ ( f)]). <s^{\prime},s">\rho([s,D(f)])-<s,s">\rho([s^{\prime},D(f)]). |  |

Since the left member of the equality above vanishes, we deduce the following identity

( ∗) ( ρ ( [s, s ′]) − [ρ ( s, ρ ( s ′)]) f) ρ ( s ") = < s, s " > ρ ( [s ′, D ( f)]) − < s ′, s " > ρ ( [s, D ( f)]). |  |  |  |

Now, let us choose an element g ∈ F ⁡ ( M) g\in F(M) satisfying the following two conditions in some open sub-set of the base manifold M M

( C ​ 1) < s, D ⁡ ( g) = 0. |  |  |  |

( C ​ 2) < s ′, D ⁡ ( g) > ≠ 0. |  |  |  |

Therefore, replacing s ​ " s" by D ⁡ ( g) D(g) in ( ∗) (\ast) we obtain the following identy

( ∗ ∗) < s ′, D ( g) > ρ ( [s, D ( f)] = o ∀ f ∈ F ( M) |  |  |  |

Thus, the right member of the identity ( ∗) (\ast) vanishes identically.

Second: (A1) implies (A2)

Now, our assumption is that ρ \rho is an algebra homomorphism from ( Γ ( V), [.,.]) (\Gamma(V),[.,.]) to the Lie algebra of smooth vector fields on the base manifold M M. Then, from the following Leibniz equation

 | L ⁡ ( s, f, s ′) = − < s, s ′ > ​ D ​ ( f), L(s,f,s^{\prime})=-<s,s^{\prime}>D(f), |  |

one easily deduces that ρ ⁡ ( D ⁡ ( f)) \rho(D(f)) vanishes identically. That ends the proof of Theorem 6.5 □ \square

N.B. In [UK], Uchino raises the question to know whether the axiom (Ax2) of Courant algebroid structures may be deduced from the other axioms. Example 5.2 and Theorem 6.5 show that this question is a relevant one. Theorems 5.1, Proposition 6.4 and 6.5 give the complete answer to U c h i n o, s Uchino^{,s} question.
However the two axioms (Ax3) and (Ax4) in the usual definition of Courant algebroid structures are always superfluous.
On the other hand the three axioms (A2),(A3) and (A4) are superfluous whenever the rank of the Courant algebroid is greater than three.
The author recently brought Alan W e i n s t e i n, s Weinstein^{,s} attention to the last observations . Our Theorem 5.1 shows that only the two axioms (Ax1) and (Ax5) are necessary to define Courant algebroid structures of r ​ a ​ n ​ k > 3 rank>3.

So, in regard to a Courant algebroid structure, say ( V, ρ, [.,.], <.,. >, D), (V,\rho,[.,.],<.,.>,D), the cases where r ​ a ​ n ​ k ​ ( V) ≤ 3 rank(V)\leq 3 are quite different from those where OPEN r ​ a ​ n ​ k ​ ( V) > 3) rank(V)>3).
In the cases where r ​ a ​ n ​ k ​ ( V) < 3 rank(V)<3, it becomes necessary to add the axiom (Ax2) ( or its equivalent ρ ⁡ ( D ⁡ ( f)) = 0 ​ ∀ f ∈ F ⁡ ( M). \rho(D(f))=0\,\forall f\in F(M).)

Many years ago(in 1995 and in 2000) we pointed out a similar remark about the system of three axioms in the usual definition Lie algebroid structures. The correct definition of Lie algebroid structures is that we have written out , [NB2]. Let us recall it below.)

###### Definition 6.6.

A Lie algebroid on the base manifold M M is an anchored almost Lie algebroid ( V, ρ, [.,.]) (V,\rho,[.,.]) on M M with the following two properties

( P ​ 1) J ⁡ ( s, s ′, s ​ ") = o ​ ∀ s, s ′, s ​ " ∈ Γ ⁡ ( V). |  |  |  |

( P ​ 2) [s, f ​ s ′] − ( ρ ⁡ ( s) ​ f) ​ s ′ − f ⁡ [s, s ′] = 0 ​ ∀ f ∈ F ⁡ ( M). |  |  |  |

###### Remark 6.7.

Both properties (P1) and (P2) imply that the anchor map ρ \rho induces a Lie algebra homomorphism from ( Γ ( V), [.,.]) (\Gamma(V),[.,.]) to the Lie algebra of smooth vector fields on the base manifold.

Regarding the abundance of literature on the theory of Lie algebroid structures we concluded and claimed (in 1995) that the redundancy of the axiom (Ax3), namely

 | ρ ⁡ ( [s, s ′]) = [ρ ⁡ ( s), ρ ⁡ ( s ′)] \rho([s,s^{\prime}])=[\rho(s),\rho(s^{\prime})] |  |

has remained unknown to the totaly of experts for many decades. Today in our knowledge the contrary is still uncertain. That is reason why, once more, we would like to repeat things here. First authors to be recently convinced are J.P. Dufour, A. Banyaga, J. Leslie, T.Z. Nguyen, A.Weinstein [private communications]; J. Grabowski and M. Marmo, [GMa].

Digressions.

Regarding various generalizations of the theory of Lie Algebroid structures, the only exiting problem is to handle the Lie algebroid structure defect. That defect is represented by the couple consisting of Jacobi anomaly and Leibniz anomaly of anchored almost Lie algebroid structures. That is the main concern of many fundamental works. For instance [KO1,KO2,LWX1,LWX2,LX,MK]. To handle the Lie algebroid structure defects, many interesting ideas arise from [PP].

The highlighted point behind the theory of Courant algebroid structures is to ask both Jacobi anomaly and Leibniz anomaly to lie in the kernel of the anchor map,(via some special first order differential operator D D, which is really a 1-cocycle of the complex (5) (of the Koszul-Vinberg algebra F ⁡ ( M) F(M))).
Similar ideas work in anchored almost Koszul-Vinberg algebroid structures. In the next section we intend to perform the idea that Courant algebroid structures provide an efficient framework for many interesting investigations, (see[LWX1,LWX2] for more details about other relationships, (such as Manin triple, Dirac structures and so on).

## 7. NON ASYMMETRIC COURANT ALGEBROIDS

We plan pointing out close relationships between non asymmetric almost algebroid structures, (viz those ( V,.) (V,.) such that the multiplication of the real algebra ( Γ ( V),.) (\Gamma(V),.) is not assumed to be skew symmetric) and the geometry of some class of bounded domains.

Let ( V, ρ,.) (V,\rho,.) be an anchored almost algebroid on the smooth manifold M. M. To elements s s, s ′ s^{\prime} and s ​ " s" of Γ ⁡ ( V) \Gamma(V) is assigned the associator s ⁡ ( s ′ ​ s ​ " − ( s ​ s ′) ​ s ​ " CLOSE s(s^{\prime}s"-(ss^{\prime})s" where s ​ s ′ ss^{\prime} stands for s. s ′ s.s^{\prime}. Let us recall that ( V, ρ,.) (V,\rho,.) is a Koszul-Vinberg algebroid if the following two axioms hold

( k ​ v ​ 1) s ⁡ ( s ′ ​ s ​ ") − ( s ​ s ′) ​ s ​ " − s ′ ​ ( s ​ s ​ ") + ( s ′ ​ s) ​ s ​ " = 0 ​ ∀ s, s ′, s ​ " ∈ Γ ⁡ ( V). |  |  |  |

( k ​ v ​ 2) s ⁡ ( f ​ s ′) − ( ρ ⁡ ( s) ​ f) ​ s − f ​ s ​ s ′ = 0 ​ ∀ f ∈ F ⁡ ( M). |  |  |  |

We recall that the Koszul-Vinberg anomaly is the following quantity

 | ( s, s ′, s ​ ") − ( s ′, s, s ​ ") (s,s^{\prime},s")-(s^{\prime},s,s") |  |

where ( s, s ′, s ​ ") (s,s^{\prime},s") stands for s ⁡ ( s ′ ​ s ​ ") − ( s ​ s ′) ​ s ​ ". s(s^{\prime}s")-(ss^{\prime})s".

Given an anchored almost algebroid on the base manifold M M, say ( V, ρ,.) (V,\rho,.), its KV-algebroid structure defect is represented by the couple consisting of the Koszul-Vinberg anomaly and the following Leibniz anomaly

 | L ​ ( s, f, s ′) = s ⁡ ( f ​ s ′) − ( ρ ⁡ ( s) ​ f) ​ s ′ − f ⁡ ( s ​ s ′), \textit{L}(s,f,s^{\prime})=s(fs^{\prime})-(\rho(s)f)s^{\prime}-f(ss^{\prime}), |  |

KV stands for Koszul-Vinberg.
Let us consider an anchored almost algebroid with a non degenerate symmetric bilinear form, say ( V, ρ,., <.,. >) (V,\rho,.,<.,.>)

We shall consider the vector space Γ ⁡ ( V) \Gamma(V) endowed with its F ⁡ ( M) F(M) -module structure defined by (1). Now, let us set the following definition

###### Definition 7.1.

A non asymmetric Courant algebroid is an anchored almost algebroid ( V, ρ,.) (V,\rho,.) with a non degenerate symmetric bilinear form, say <.,. > <.,.>, and with a 1-cocycle D ∈ C 1 ​ ( F ⁡ ( M), V) D\in C^{1}(F(M),V) subject to satisfy the following requirements:
∀ s, s ′, s ​ " ∈ Γ ⁡ ( V), \forall s,s^{\prime},s"\in\Gamma(V), ∀ f ∈ F ⁡ ( M) \forall f\in F(M) one has

( R 1) ( s, s ′, s ") − ( s ′, s, s ") = D ( δ ( <.,. > ( s, s ′, s ")). |  |  |  |

( R ​ 2) ( f ​ s) ​ s ′ = f ⁡ ( s ​ s ′). |  |  |  |

( R 3) ρ ( s) < s ′, s " > = < s s ′ + D ( < s, s ′), s " > + < s ′, s s " + D ( < s, s " >) >, |  |  |  |

the right member of the first equality in (R1) has the following meaning

 | δ <.,. > ( s, s ′, s ​ ") = − ρ ⁡ ( s) ​ < s ′, s ​ " > + < s ​ s ′, s ​ " > + < s ′, s ​ s ​ " > + \delta<.,.>(s,s^{\prime},s")=-\rho(s)<s^{\prime},s">+<ss^{\prime},s">+<s^{\prime},ss">+ |  |

 | ρ ⁡ ( s ′) ​ < s, s ​ " > − < s ′ ​ s, s ​ " > − < s, s ′ ​ s ​ " > \rho(s^{\prime})<s,s">-<s^{\prime}s,s">-<s,s^{\prime}s"> |  |

Our first result concerning non asymmetric Courant algebroid structures is the following statement.

###### Theorem 7.2.

Let ( V, ρ,., <.,. >, D) (V,\rho,.,<.,.>,D) be a non asymmetric Courant algebroid. If its rank is greater than two, then the anchor map ρ \rho satisfies the following identity

 | [ρ ⁡ ( s), ρ ⁡ ( s ′)] = ρ ⁡ ( s ​ s ′) − ρ ⁡ ( s ′ ​ s) ​ ∀ s, s ′ ∈ Γ ⁡ ( V) [\rho(s),\rho(s^{\prime})]=\rho(ss^{\prime})-\rho(s^{\prime}s)\,\,\forall s,s^{\prime}\in\Gamma(V) |  |

Proof
Let s s and s ′ s^{\prime} be elements of Γ ⁡ ( V) \Gamma(V) and let f f be an element of F ⁡ ( M) F(M). Then the following identity is a straight consequence of (R3)

 | s ⁡ ( f ​ s ′) − ( ρ ⁡ ( s) ​ f) ​ s ′ − f ⁡ ( s ​ s ′) = − < s, s ′ > ​ D ​ ( f). s(fs^{\prime})-(\rho(s)f)s^{\prime}-f(ss^{\prime})=-<s,s^{\prime}>D(f). |  |

Thus, (R3) is an efficient tool to handle the Leibniz anomaly. Since the rank of V V is greater than two let s ​ " s" be a non zero element of Γ ⁡ ( V) \Gamma(V) such that

 | < s, s ​ " > = < s ′, s ​ " > = 0. <s,s">=<s^{\prime},s">=0. |  |

Therefore, using the identity we just pointed out, a direct calculation yields to the following identity

 | ( s, s ′, f s ") − ( s ′, s, f s ") = f ( ( s, s ′, s ") − ( s ′, s, s ")) + ( δ <.,. > ( s, s ′, s " >)) D ( f) + (s,s^{\prime},fs")-(s^{\prime},s,fs")=f((s,s^{\prime},s")-(s^{\prime},s,s"))+(\delta<.,.>(s,s^{\prime},s">))D(f)+ |  |

 | ( ( [ρ ⁡ ( s), ρ ⁡ ( s ′)] − ρ ⁡ ( s ​ s ′) + ρ ⁡ ( s ′ ​ s)) ​ f) ​ s ​ ". (([\rho(s),\rho(s^{\prime})]-\rho(ss^{\prime})+\rho(s^{\prime}s))f)s". |  |

On the other hand, a similar calculation yields to the following identity

 | δ <.,. > ( s, s ′, f ​ s ​ ") = f ​ δ <.,. > ( s, s ′, s ​ "). \delta<.,.>(s,s^{\prime},fs")=f\delta<.,.>(s,s^{\prime},s"). |  |

Therefore, by the virtu of (R1) one must conclude that the quantity

 | ( [ρ ⁡ ( s), ρ ⁡ ( s ′)] − ρ ⁡ ( s ​ s ′) + ρ ⁡ ( s ′ ​ s)) ​ f ([\rho(s),\rho(s^{\prime})]-\rho(ss^{\prime})+\rho(s^{\prime}s))f |  |

vanishes identically. That ends the demonstration of Theorem 7.2 □ \square

Let us make some remark. Let V,., <.,. > V,.,<.,.> be an non asymmetric Courant algebroid and let s, s ′, s ​ " ∈ Γ ⁡ ( V) s,s^{\prime},s"\in\Gamma(V). As above, let us put

 | K ​ V ​ ( s, s ′, s ​ ") = ( s, s ′, s ​ ") − ( s ′, s, s ​ "). KV(s,s^{\prime},s")=(s,s^{\prime},s")-(s^{\prime},s,s"). |  |

Then V,., <.,. > V,.,<.,.> gives rise to the anchored almost Lie algebroid structure V, [.,.] V,[.,.] whose bracket is defined by

 | [s, s ′] = s ​ s ′ − s ′ ​ s. [s,s^{\prime}]=ss^{\prime}-s^{\prime}s. |  |

The Jacobi anomaly of the last almost Lie algebroid structure is related to the Koszul-Vinberg anomaly K ​ V ​ ( s, s ′, s ​ ") KV(s,s^{\prime},s") as follows

 | J ⁡ ( s, s ′, s ​ ") = ∮ K ​ V ​ ( s, s ′, s ​ "). J(s,s^{\prime},s")=\oint KV(s,s^{\prime},s"). |  |

The digressions above lead to close relationships between non asymmetric Courant algebroid structures on a base manifold M M and locally hessian Lie group bundles on the same base manifold M M.
In fact, consider a non asymmetric Courant algebroid ( V, ρ,., <.,. >, D) (V,\rho,.,<.,.>,D). Let us use (R1), (R2) and (R3) to calculate the quantity ρ ⁡ ( f ​ s) ​ < s ′, s ​ " > \rho(fs)<s^{\prime},s">. Then, we obtain the following identity

 | < s, s ′ > ​ < D ⁡ ( f), s ​ " > + < s, s ​ " > < D ⁡ ( f), s ′ >= 0. <s,s^{\prime}><D(f),s">+<s,s"><D(f),s^{\prime}>=0. |  |

Therefore, we must conclude that D = 0 D=0. The last condition is equivalent to ρ = 0 \rho=0. Thus, a non asymmetric Courant algebroid is nothing but a Koszul-Vinberg algebra bundle endowed with a non degenerate symmetric bilinear form which is invariant under the left multiplication by elements of Γ ⁡ ( V) \Gamma(V). We can write out those particular items in terms of the real valued cohomology the complex (5).

Roughly speaking, let R be an associative commutative ring and let A A be a R -Koszul-Vinberg algebra. We will endow R with the trivial A A -module structure. We now consider the cochain complex whose the k t ​ h k^{th} homogeneous subspaces is the vector space

 | C k ( A, K) = H o m K ( ⊗ k A, K). C^{k}(A,K)=Hom_{K}(\otimes^{k}A,K). |  |

The coboundary operator is defined as in (5).

Considering the case of a non asymmetric Courant algebroid on the base manifold M M, say ( V,., <.,. >) (V,.,<.,.>), we are dealing with a cohomology class in H 2 ​ ( Γ ⁡ ( V), F ⁡ ( M)) H^{2}(\Gamma(V),F(M)) containing a non degenerate cocyle, namely <.,. > <.,.>.

Let us return to the general case of non asymmetric Courant algebroid structures. Let ( V,., <.,. >) (V,.,<.,.>) be such an algebroid structure. We consider elements s, s ′, s ​ " ∈ Γ ⁡ ( V) s,s^{\prime},s"\in\Gamma(V) and an element f ∈ F ⁡ ( M) f\in F(M). By the virtue of (R3) one has the following identity

 | < s ​ s, s ​ " > + < s ′, s ​ s ​ " > = 0. <ss,s">+<s^{\prime},ss">=0. |  |

Thus, regarding the bilinear form <.,. > <.,.> as an element of C 2 ​ ( Γ ⁡ ( V), F ⁡ ( M)), C^{2}(\Gamma(V),F(M)), one easily sees that

 | δ <.,. > ( s, s ′, s ​ ") = 0. \delta<.,.>(s,s^{\prime},s")=0. |  |

An interesting consequence of the last calculations is the following statement.

###### Theorem 7.3.

Each non asymmetric Courant algebroid on the base manifold M M is a locally flat (pseudo) clan bundle on M. M.

Proof
Let us recall that (by definition) a real clan (resp. pseudo clan) is a couple ( A, <.,. >) (A,<.,.>) of real Koszul-Vinberg algebra A A together with a positive definite (resp non degenerate) real valued symmetric 2-cocyle <.,. > ∈ C 2 ( A, R), <.,.>\in C^{2}(A,R), [VK,VE,SH].
A (pseudo) clan A, <.,. > A,<.,.> is locally flat when the left multiplication by each element of A A lies in the orthogonal algebra of <.,. > <.,.>.
Considering the case of a non asymmetric Courant algebroid the vanishing property of the anchor map implies that the associator map ( s, s ′, s ​ ") (s,s^{\prime},s") is symmetric with respect to the pair ( s s, s ′ s^{\prime}). Therefore, we get the following identity

 | K ​ V ​ ( s, s ′, s ​ ") = o ​ ∀ s, s ′, s ​ " ∈ Γ ⁡ ( V). KV(s,s^{\prime},s")=o\,\,\forall s,s^{\prime},s"\in\Gamma(V). |  |

Moreover, if x x is a fixed element of the base manifold M M, then ∀ s, s ′ ∈ Γ ⁡ ( V) \forall s,s^{\prime}\in\Gamma(V), the element ( s ​ s ′) ​ ( x) (ss^{\prime})(x) of V x V_{x} depends on s ⁡ ( x) s(x) and on s ′ ​ ( x) s^{\prime}(x) only. Thus if we set

 | s ⁡ ( x). s ′ ​ ( x) = ( s ​ s ′) ​ ( x) s(x).s^{\prime}(x)=(ss^{\prime})(x) |  |

then, the fiber V x V_{x} is a Koszul-Vinberg algebra endowed with a non degenerate symmetric 2-cocycle, namely <.,. > ( x) <.,.>(x). That ends the proof of Theorem 7.3 □ \square

###### Remark 7.4.

Let us keep in mind the conclusion of Theorem 7.3, the question rises to know whether the Koszul-Vinberg algebra bundle deduced from a non asymmetric Courant algebroid is locally trivial. In other words is there a Koszul-Vinberg algebra fiber type for the bundle ( V,.) (V,.)?

From the theoretic viewpoint, the cohomology theory of Koszul-Vinberg algebras is helpful in studying this question. To perform the last idea, one must remind that the cochain complex to be considered is C ∗ ​ ( Γ ​ ( V), V) C^{*}(\Gamma(V),V) whose coboundary operator is recalled below. Let Θ \Theta be an element of C k ​ ( Γ ​ ( V), V) C^{k}(\Gamma(V),V) and let s 1,.., s k + 1 s_{1},..,s_{k+1} be smooth sections of V V, then

( 8) δ Θ ( s 1,., s k + 1) = ∑ j ( − 1) j ( ( s j Θ) ( s 1,., s j − 1, s j + 1,., s k + 1) + |  |  |  |

 | ( Θ ( s 1,., s k, x j)) s k + 1) (\Theta(s_{1},.,s_{k},x_{j}))s_{k+1}) |  |

Following our previous remarks, (see the demonstration of Theorem 7.2,) the coboundary operator δ \delta is F ⁡ ( M) F(M) -linear. Thereafter a helpful tool in answering the question raised in Remark 7.4 lies in H 2 ​ ( V o, V o), H^{2}(V_{o},V_{o}), where V o V_{o} stands for a fixed fiber of the vector bundle V. V.
In fact, the deformation theory of Koszul-Vinberg algebras may be controlled by cohomology classes of the complex (8). So, our digressions allow the application of a classical rigidity theorem,[KM,GM1,KM]. More precisely, we can state the following result

###### Theorem 7.5.

Let ( V,., <.,. >) (V,.,<.,.>) be a non asymmetric Courant algebroid on a connected base manifold M M. If H 2 ​ ( V x, V x) H^{2}(V_{x},V_{x}) vanishes ∀ x ∈ M \forall x\in M, then the K-V algebra bundle ( V,.) (V,.) is a locally trivial.

An outline of Proof
Without loss of generality, we may suppose the vector bundle V V to be a trivial bundle. Since M M is connected, given arbitrary points x o, x ∈ M x_{o},x\in M, there is an isotopy ( V x ⁡ ( t),.) (V_{x(t)},.) whose extremities are ( V o,.) (V_{o},.) and ( V x,.) (V_{x},.); V o V_{o} stands for the fiber of V V at the point x o x_{o}. Under the vanishing hypothesis, i.e. H 2 ​ ( Γ ⁡ ( V), V) = 0 ​ ∀ x ∈ M, H^{2}(\Gamma(V),V)=0\,\,\forall x\in M, all of the fibers ( V x,.) (V_{x},.) is isomorphic to the fixed Koszul-Vinberg algebra ( V o,.) (V_{o},.). Let us denote by K ​ V ​ ( V o) KV(V_{o}) the set of Koszul-Vinberg algebra structures on the vector space V o V_{o}. We denote by μ o \mu_{o} the Koszul-Vinberg multiplication that V o V_{o} inherits from ( V,., <.,. >) (V,.,<.,.>). Under the action in H o m ( ⊗ 2 V o, V o) Hom(\otimes^{2}V_{o},V_{o}) of the linear group of the vector space V o V_{o}, the orbit of μ o \mu_{o} is a Zariski open subset of K ​ V ​ ( V o) KV(V_{o}). Those ingredients are used to obtain smooth family ϕ x \phi_{x} of isomorphisms from ( V x,.,) (V_{x},.,) to ( V o, μ o) (V_{o},\mu_{o}) □ \square

## 8. A NON VANISHING THEOREM

Let ( V, ρ,., <.,. >, D) (V,\rho,.,<.,.>,D) be a non asymmetric Courant algebroid on the base manifold M M. According to Theorem 7.3, such a datum may be regarded as a (pseudo) clan bundle on M. M.
Keeping notations in Section 7, we denote by G x G_{x} the connected and simply connected Lie Group whose Lie algebra is the vector space V x V_{x} endowed with the bracket defined by

 | [s ⁡ ( x), s ′ ​ ( x)] = ( s ​ s ′) ​ ( x) − ( s ′ ​ s) ​ ( x). [s(x),s^{\prime}(x)]=(ss^{\prime})(x)-(s^{\prime}s)(x). |  |

Under some additional conditions, a relevant non trivial invariant of ( V,., <.,. > (V,.,<.,.> is the cohomology class of the bilinear form <.,. >. <.,.>.
To make precise our assertion, let us set the following definition

###### Definition 8.1.

A non asymmetric Courant algebroid is called co-compact if each Lie group G x G_{x} contains a co-compact lattice, say Λ x \Lambda_{x}

Many homogeneous convex domains are base manifolds of co-compact non asymmetric Courant algebroids, [KJL3,KV,VEB].
Below, we are going to perform that idea.

###### Theorem 8.2.

Let ( V,., <.,. >) (V,.,<.,.>) be a co-compact non asymmetric Courant algebroid. If the cocycle <.,. > <.,.> is definite, then its cohomology class in H 2 ​ ( Γ ⁡ ( V), F ⁡ ( M)) H^{2}(\Gamma(V),F(M)) doesn’t vanish.

Proof
First of all, if the multiplication in ( Γ ( V),.) (\Gamma(V),.) is the zero map, then the conclusion of Theorem 8.2 holds. Now let us suppose that the multiplication in ( Γ ( V),.) (\Gamma(V),.) is not the zero map. Let us assume the cocycle <.,. > <.,.> to be (positive definite and) exact. Then there is a 1-cochain Θ ∈ C 1 ​ ( Γ ⁡ ( V), F ⁡ ( M)) \Theta\in C^{1}(\Gamma(V),F(M)) such that

 | <.,. > = δ Θ. <.,.>=\delta\Theta. |  |

In other words, one has

 | < s, s ′ > = Θ ⁡ ( s ​ s ′) ​ ∀ s, s ′ ∈ Γ ⁡ ( V). <s,s^{\prime}>=\Theta(ss^{\prime})\,\forall s,s^{\prime}\in\Gamma(V). |  |

We know that <.,. > <.,.> is invariant under the left multiplications by elements of Γ ⁡ ( V) \Gamma(V). Let s s, s ′ s^{\prime} and s ​ " s" be elements of Γ ⁡ ( V) \Gamma(V). For each x ∈ M, x\in M, let G x G_{x} be the connected and simply connected Lie group whose Lie algebra is the vector space V x V_{x} endowed with the bracket defined by

 | [s ⁡ ( x), s ′ ​ ( s)] = ( s ​ s ′) ​ ( x) − ( s ′ ​ s) ​ ( x). [s(x),s^{\prime}(s)]=(ss^{\prime})(x)-(s^{\prime}s)(x). |  |

Let ∇ \nabla be the left invariant linear connection on G x G_{x} defined by

 | ( ∇ s s ′) ​ ( x) = ( s ​ s ′) ​ ( x). (\nabla_{s}s^{\prime})(x)=(ss^{\prime})(x). |  |

Actually, the differential form Θ \Theta is De Rham closed. Then the locally flat manifold ( G x, ∇) (\textit{G}_{x},\nabla) carries the (left) invariant closed 1-form Θ x \Theta_{x} whose covariant derivative, say ∇ ( Θ) \nabla(\Theta), is positive definite. Both Θ \Theta and ∇ \nabla are left invariant in each Lie group G x G_{x}. Therefore, the triple ( Θ, ∇, Λ x) (\Theta,\nabla,\Lambda_{x}) gives rise to a hyperbolic locally flat structure on the manifold Λ x \ G x \Lambda_{x}\backslash G_{x} whose simply connected covering is the triple ( G x, Θ, ∇). (G_{x},\Theta,\nabla). Therefore, each ( G x, ∇) (G_{x},\nabla) is isomorphic to a convex cone not containing any straight line. Thereafter, following [KJL1], the manifold G x G_{x} carries a (unique) smooth vector field H H satisfying the following identity

given any smooth vector field X ∈ Γ ⁡ ( T ​ G x) X\in\Gamma(TG_{x}) the following identity hold

 | ∇ X ( H) = X. \nabla_{X}(H)=X. |  |

Thereafter, let us consider elements s, s ′ ∈ V x s,s^{\prime}\in V_{x} as left invariant vector fields on G x G_{x}. Since ∇ \nabla is the Levi-Civita connection of the Riemannian structure ( G x, <.,. >) (G_{x},<.,.>), we check that the following identity holds

 | < s ​ s ′, H > + < s ′, ∇ s ( H) > = 0. <ss^{\prime},H>+<s^{\prime},\nabla_{s}(H)>=0. |  |

Thus, the vector field H H is left invariant in the Lie group G x G_{x}. From the last identity we deduce that

 | < s ​ s ′, H > = − < s ′, s >. <ss^{\prime},H>=-<s^{\prime},s>. |  |

From the exactness of the 2-cocycle <.,. > <.,.>, we deduce the following identities

 | < s ​ s ′, H > = Θ ⁡ ( ( s ​ s ′) ​ H) = Θ ⁡ ( s ​ s ′). <ss^{\prime},H>=\Theta((ss^{\prime})H)=\Theta(ss^{\prime}). |  |

 | < s ′, ∇ s ( H) > = < s ′, s ​ H > = < s ′, s >= Θ ⁡ ( s ′ ​ s). <s^{\prime},\nabla_{s}(H)>=<s^{\prime},sH>=<s^{\prime},s>=\Theta(s^{\prime}s). |  |

In conclusion, we deduce from the calculations above the following identity

 | Θ ⁡ ( s ​ s ′) = < s, s ′ > = 0 ​ ∀ s, s ′ ∈ V x. \Theta(ss^{\prime})=<s,s^{\prime}>=0\,\forall s,s^{\prime}\in V_{x}. |  |

That is absurd and ends the proof of Theorem 8.2 □ \square

Example 8.3

Let L L be the linear endomorphism of R 2 R^{2} defined by

 | L ⁡ ( x, y) = ( y, x) ​ ∀ ( x, y) ∈ R 2. L(x,y)=(y,x)\,\,\forall(x,y)\in R^{2}. |  |

We now consider the semi-direct product of R 2 R^{2} with the one parameter subgroup generated by L L. We obtain the connected and simply connected Lie group whose Lie algebra is R 3 R^{3} endowed with the following bracket

 | [( x, y, z), ( x ′, y ′, z ′)] = ( z ​ y ′ − z ′ ​ y, z ​ x ′ − z ′ ​ x, o). [(x,y,z),(x^{\prime},y^{\prime},z^{\prime})]=(zy^{\prime}-z^{\prime}y,zx^{\prime}-z^{\prime}x,o). |  |

That Lie group carries a left invariant locally flat structure defined by the following left invariant linear connection

 | ∇ ( x, y, z) ( x ′, y ′, z ′) = ( z ​ y ′, z ​ x ′, o). \nabla_{(x,y,z)}(x^{\prime},y^{\prime},z^{\prime})=(zy^{\prime},zx^{\prime},o). |  |

Actually, each pair ( α, β) (\alpha,\beta) of real numbers with α ​ β ≠ 0 \alpha\beta\neq 0 defines the following left invariant metric

 | < ( x, y, z), ( x ′, y ′, z ′) > = α ⁡ ( x ​ x ′ − y ​ y ′) + β ⁡ ( z ​ z ′). <(x,y,z),(x^{\prime},y^{\prime},z^{\prime})>=\alpha(xx^{\prime}-yy^{\prime})+\beta(zz^{\prime}). |  |

It is easily seen that the metric defined above is a non exact cocycle ◊ {\lozenge}
.

Example 8.4

Let us consider Lie algebra structure in R 3 R^{3} defined by the following bracket

 | [( x, y, z), ( x ′, y ′, z ′)] = ( z ​ y ′ − z ′ ​ y, z ​ x ′ − z ′ ​ x, 0). [(x,y,z),(x^{\prime},y^{\prime},z^{\prime})]=(zy^{\prime}-z^{\prime}y,zx^{\prime}-z^{\prime}x,0). |  |

The associated connected and simply connected Lie group ,say G G, carries a left invariant locally flat structure corresponding to the following multiplication

 | ( x, y, z). ( x ′, y ′, z ′) = ( z ​ y ′, − z ​ x, 0). (x,y,z).(x^{\prime},y^{\prime},z^{\prime})=(zy^{\prime},-zx,0). |  |

If α \alpha is a non zero real number, then we define the following on exact cocycle

 | < ( x, y, z), ( x ′, y ′, z ′) > = x ​ x ′ + y ​ y ′ + α ⁡ ( z ​ z ′). <(x,y,z),(x^{\prime},y^{\prime},z^{\prime})>=xx^{\prime}+yy^{\prime}+\alpha(zz^{\prime}). |  |

The connected and simply connected Lie group associated to the Lie algebra which is defined above contains Z 3 Z^{3} as a co-compact lattice ◊ {\lozenge}.

## 9. MISCELLENEA

Let ( V,., <.,. >) (V,.,<.,.>) be a non asymmetric Courant algebroid on M. M. Once for all, let us fix an element x o x_{o} of the base manifold M. M. We regard ( V,., <.,. >) (V,.,<.,.>) as a smooth deformation of the (pseudo) clan ( V o, <.,. >) (V_{o},<.,.>), where V o V_{o} stands for the fiber of V V at x o. x_{o}. As in Section 8, to each ( V x, <.,. >) (V_{x},<.,.>) is assigned the connected and simply connected Lie group G x G_{x} whose Lie algebra of is the vector space V x V_{x} endowed with the bracket defined by

( 9) [s ⁡ ( x), s ′ ​ ( x)] = ( s ​ s ′) ​ ( x) − ( s ′ ​ s) ​ ( x). |  |  |  |

All of those Lie groups is endowed with a left invariant locally flat structure, (equivalently, with a left invariant locally flat linear connection, say ∇. \nabla.) Each G x G_{x} also carries a left invariant locally hessian (pseudo) Riemannian metric. That picture forms a smooth deformation of ( G o, ∇, <.,. >), (G_{o},\nabla,<.,.>), where ∇ x \nabla_{x} is the covariant derivation in G x G_{x} defined by the Koszul-Vinberg multiplication in V x. V_{x}. So, we can view the multiplication μ x \mu_{x} in each Koszul-Vinberg algebra ( V x,.) (V_{x},.) as new multiplication on the same fixed vector space V o. V_{o}. Therefore the cochain ν x \nu_{x} = μ x − μ o \mu_{x}-\mu_{o} is a Koszul-Vinberg element of the complex C ∗ ​ ( V o, V o). C^{\ast}(V_{o},V_{o}). In other words, ν x \nu_{x} satisfies the following KV equation

( 10) δ ⁡ ( ν x) + K ​ V ν x = 0. |  |  |  |

The complex in consideration is that in REMARK 7.4. Koszul-Vinberg elements of that complex are the analogues of the classical Maurer-Cartan elements which arise from the deformation theory of associative algebra structures and Lie algebras structures. The equation (10) above is the analogue of the Maurer-Cartan equation

 | δ ​ ν + 1 / 2 ​ [ν, ν] = 0. \delta\nu+1/2[\nu,\nu]=0. |  |

(See [GM, NA, NR, KM, LWX1, [VI] and other references ibidem).

We recall that to each ν ∈ C 2 ​ ( V o, V o) \nu\in C^{2}(V_{o},V_{o}) is assigned the cochain K ​ V ν ∈ C 3 ​ ( V o, V o) KV_{\nu}\in C^{3}(V_{o},V_{o}) which defined by

 | K ​ V ν ​ ( s, s ′, s ​ ") = ν ⁡ ( s, ν ⁡ ( s ′, s ​ ")) − ν ⁡ ( ν ⁡ ( s, s ′), s ​ ") − ν ⁡ ( s ′, ν ⁡ ( s, s ​ ")) + ν ⁡ ( ν ⁡ ( s ′ ​ s), s ​ "). KV_{\nu}(s,s^{\prime},s")=\nu(s,\nu(s^{\prime},s"))-\nu(\nu(s,s^{\prime}),s")-\nu(s^{\prime},\nu(s,s"))+\nu(\nu(s^{\prime}s),s"). |  |

To end those miscellaneous items, let us denote by G the union of all of the G x G_{x} when x x runs over the base manifold M M. Then, G is a set bundle over M M under the set projection

 | G x ⟶ x. G_{x}\longrightarrow x. |  |

We equip G with the finest topology that makes open the projection we just defined. We observe that ( G x, ∇ x, <.,. > x) (G_{x},\nabla_{x},<.,.>_{x}) depends smoothly on x x. So, we obtain the locally hessian Lie group bundle ( G, ∇, <.,. >) (\textit{G},\nabla,<.,.>) on the base manifold M M.
Naturally, arises the question to know whether ( G, ∇, <.,. >) (\textit{G},\nabla,<.,.>) is a locally trivial bundle. The complex (8) is an ingredient for studying the affinely flat Lie group bundle ( G, ∇,). (\textit{G},\nabla,). In particular, under the hypothesis of Theorem 7.4, ( G, ∇) (\textit{G},\nabla) is a locally trivial affine Lie group bundle on the base manifold M. M.

## 10. OBSERVATIONS

(O1) Clans arose from the geometry of convex domains, [KV],KJL3]. In particular, the Lie algebra of a locally simply transitive group of affine transformations of a convex cone containing no straight line is a clan. More details can be found in fundamental papers by E.B. Vinberg, e.g. [EBV]. See also [KJL1,KJL2,KJL3,SH,VJ].

(O2) The literature on the theory of Lie algebroid structures is impressive. We have related some aspects of that theory with the cohomology theory of Koszul-Vinberg algebras. In regard to global invariants of algebroid structures those relationships are efficient ([NB1,NB2,NBW1,NBW2]).

There are many other aspects, such as the third Lie Theorem,[AM,DP]. The holonomy and the monodromy principle, the duality theory are studied. The theory of Singularities, and so on. There is an abundance of references, for instance [DC,BR,HJ,DJ,DP,DV,DZ,NTZ MK PJ,PL,WA,WeA].

(O3) Relationships with Poisson structures and singular foliations are exciting also and have been widely studied from various viewpoints. For instance [FR,Ia,KJ] deal with characteristic classes viewpoint. The normal forms are the aim of [DJ,DZ,NBW2,NTZ]. Under some careful subtle techniques, the last viewpoint also walks in the theory of KV-algebroid structures, [NBW2].

(O4) Above, we just mentioned that the theory of characteristic classes of Lie algebroid structures is subject of intense research programs,[FR,KJ]. Given a CC algebroid on the base manifold M, M, say ( V, ρ, [.,.], <.,. >), (V,\rho,[.,.],<.,.>), let F be the image of Γ ⁡ ( V) \Gamma(V) under the anchor map ρ. \rho. If the rank of V V is greater than three, then F is a subalgebra of the Lie algebra X ⁡ ( M) X(M) of smooth vectors fields on M. M. Unfortunately the Frobenius theorem generally fails for singular differential systems, [AM]. However it may occur that F be completely integrable in the sense of Stefan; in such an occurrence the techniques developed by R.Fernandes, J.Kubarski (among others) will provide characteristic classes of ( V, ρ, [.,.]), (V,\rho,[.,.]), though the last triple fails to be an Lie algebroid. See [FR] for a similar remark on Courant algebroid structures. For instance let Π \Pi be a smooth two vector on M M, then the cotangent bundle is provided with the almost Lie algebroid structure ( T ⋆ M, ♯, [.,.] Π), (T^{\star}M,\sharp,[.,.]_{\Pi}), where ♯ \sharp is the vector bundle morphism from T ⋆ ​ M T^{\star}M to T ​ M TM defined by Π. \Pi. The bracket of two differential forms α, β ∈ Γ ⁡ ( T ⋆ ​ M) \alpha,\beta\in\Gamma(T^{\star}M) is defined by

 | [α, β] Π = L ♯ ​ α ​ β − L ♯ ​ β ​ α − d ​ Π ​ ( α, β). [\alpha,\beta]_{\Pi}=L_{\sharp\alpha}\beta-L_{\sharp\beta}\alpha-d\Pi(\alpha,\beta). |  |

The Jacobi anomaly of the almost Lie algebroid above is related to the Schouten square of Π. \Pi. Examples of such structures are twisted Poisson structures.

To conclude the author apologizes for limiting the references above to those he has needed to prepare the present work.

Acknowledgements. The author would like to thank Augustin Banyaga, Jean-Paul Dufour and Joshua Leslie for useful discussions. He also thanks Nguen Tien Zung for carefully reading preliminary versions of the present work.

## References

- [AM] Almeida R. and Molino P. Suite d’Atyiah et feuilletage transversalement complets, C. R. Acad. Sci. Paris 300 (1985) 13-15
- [BRa1] Brown R.,Içen I. and Mucuk O. Holonomy and monodromy groupoids. Banach Center Publ. vol 54 (2001) 9-20
- [BR] Brown R. From groups to groupoids : a brief survey , Bull London Math. Soc 19 (1987), 113-134
- [CaW] Cannas da Silva A. and Weinstein A. Geometric models for noncommutative algebras, Berkeley Mathematics Lectures, Amer Math. Soc, Provisdence 1999
- [DP] Dazord P. Groupoids d’holonomie et géométrie globale, C. R. Acad Sci Paris 324 (1997), 77-80
- [CT] Courant T.J. Dirac manifolds , trans. Amer. Math. Soc. 319 (1990) 631-661
- [DC] Debord C. Local integration of Lie algebroids. Banach Center Publ 54 (2001) 21-41
- [DJ] Dufour JP Normal forms for Lie algebroids: Banach Center Publ, vol 54 (2001) 35-41
- [DuZ] Dufour JP and Zhitomirskii M. Classification of non resonant Poisson structures, J. London Math. Soc. (2) 60 (1999) 935-950
- [DV] Drinfel’d V.G. Hamiltonian structures, Lie bialgebras and the geometric meaning of the classical Yang Baxter equation, Soviet Math. Dokl. 27 (1983) 68-71
- [FR] Fernandes R.L. Lie algebroids, holonomy and characteristic classes, Preprint DG/007132 (2000)
- [GM] Gerstenhaber M. Deformations of Rings and Algebras, Ann of Math. 79 (1964) 59-103
- [GG] Grabowski J. and Grabowska K. The Lie algebras of algebroids, Banach Center Publ 54 (2001) 43-49
- [GMa] Grabowski J and Marmo G. Non asymmetric version of Nambu-Poisson bracket, J. Phys. A-34 (2001),3803-3809
- [HJ] Huesbschmann J. Duality for Lie -Rinehart algebras and modular class, J. reine angen Math. 510 (1997) 103-159
- [Ia] Iglesias D. and al. Triangular generized Lie bialgebroids holonomy and cohomology theoies, Banach Cenetr Publ vol 54 (2001) 111-133
- [KY] Katsumi Y. On hessian structure on an affine manifold, in Manifolds and Lie groups in Honor of Yozo Matsushima, Progress in mathematics vol 114, 449-459
- [KO1] Kosmann-Schwarzbach Y. Exact Gerstenhaber algebras and Lie algebroids, Acta App. Math.41 (1995) 153-165
- [KO2] Kosmann-Schwarzbach Y. Jacobian quasi-bialgebras and quasi-Poisson-Lie groups, Contemp. Math. 132 1992) 459-489
- [KM] [KM] : Kontsevich M. Deformation quantization of Poisson manifolds, Alg/97090400
- [KJL1] Koszul J-L. Domaines bornés homogènes et orbites des transformations affines, Bull Soc. Math. France 89 (1961) 515-533
- [KJL2] Koszul J-L Sous-groupes discrets des groupes de transformations affines admettant trajectoire ouverte, C.R. Acad. Sc. Paris 259 (1964) 3675-3677
- [KJL3] Koszul J-L Déformations des connections localement plates, Ann. Inst. Fourier 18 (1968) 103-114
- [KJL4] Koszul J-L Homology des formes différentielles d’ordre supérieur, Ann Scient Ec. Norm Sup 7 (1974) 139-159
- [KJ1] Kubarski J. Bott’s vanishing theorem for regular algebroids, trans. Amer Math Soc. 348 (1996) 2151-2167
- [KJ2] Kubarski J. Characteristic homomorphism, Banach Center Publication vol 54 (2001)135-173
- [LP] Libermann P. Lie algebroids and Mechanics , Arch . Math. (Brno) 32 (1996) 147-162
- [LWX1] Liu Z.J., Weinstein A and Xu P. Dirac structutres and Poisson homogeneous spaces dg-ga/9611001 vol VI (1996)
- [LWX2] Liu Z.J, Weinstein A and Xu P. Manin triple for bialgebroids, Jour Diff Geom 45 (1997) 547-574
- [LU] Lu J-H Lie algebroids associated to Poisson actions, Duke Math. J. (to appear)
- [MK1] Mackenzie K.C.H. Lie groupoids and Lie algebroids in Differential geometry, Cambridge University Press,1987
- [MK2] Mackenzie K.C.H. Double algebroids and second oreder geometry I, Adv in Math 94 (1992) 180-239
- [MK3] Mackenzie K.C.H. Lie algebroids and Lie pseudoalgebras, Bull London Math Soc. 27 (1995)97-147
- [MX] Mackenzie K.C.H. and Xu P. Integration of Lie bialgebroids, Toplogy, 39 (2000) 445-467
- [NB1] Nguiffo Boyom M. The cohomology theory of Koszul-Vinberg algebras and their modules Math. dg/0202259
- [NB2] The homology of Koszul-Vinberg algebroids of Poisson manifolds I, Banach Center Publ (2001) 99-110
- [NB3] Nguiffo Boyom M. The cohomology of Koszul-Vinberg algebroids and Poisson manifolds II ( preprint)
- [NBW1] Nguiffo Boyom M. and Wolak R. Affine structure and KV-cohomology, Jour of Diff Geom and Phys (to appear)
- [NBW2] Nguiffo Boyom M. and Wolak R. Normal forms of Koszul-Vinberg algebroids (in prepartion)
- [NTZ] Nguen T.Z. Another note on focus singularities, Lett in Math Phys 60 (2002) 87-99
- [PP] Popescu P. and Popescu M. Anchored vector bundles and Lie algebroids, Banach Center Publ vol 54 (2001) 51-69
- [SH] Shima H. Homogeneous hessian manifolds, in honnor of Yozo Matsushima, Progress in Mathematics, 14, Birkhauser, Boston 1981, 385-392
- [UK] Uchino K. Remarks on COURANT algebroids, Lett. Math. Phys. (to appear)
- [VI] Vaisman I. Lectures on Geometry of Poisson manifolds, Progres in Math. Birkhauser, Basel 1994
- [VV] Veshinin V. Poisson-Malcev structures (preprint Montpellier 2002)
- [VJ1] Vey J. Deformations du crochet de Poisson sur une variété symplectique, Comment Math helv 50 (1975) 421-454
- [VJ2] Vey J. Sur la division des domaines de Siegel, Ann Scient Ec Norm Sup 4t3 (1970) 479-506
- [VK] Vinberg E.B. and Katz V. Kvaziodnorodnye konusy, Mat. Zametki 1 (1967)347-354
- [VE] Vinberg E.B. Convex homogeneous cones,Transl Moscow Math. Soc 12 (1963)340-403
- [WA] Wade A. Normalisation formelle des structures de Poisson, CR Acad Sc Paris I-324 (1997) 531-536
- [WeA] Weinstein A. Linearization problem for Lie algebroids and Lie groupoids, Lett. Math. Phys. 52 (2001) 93-103


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:boyom@math.univ-montp2.fr
