<!-- source: https://ar5iv.labs.arxiv.org/html/2312.01222 | converted from HTML -->

[2312.01222] Phase portraits for quadratic systems possessing an infinite elliptic–saddle or an infinite nilpotent saddle

# Phase portraits for quadratic systems possessing an infinite elliptic–saddle or an infinite nilpotent saddle

Joan C. Artés Affiliation: Departament de Matemàtiques, Universitat Autònoma de Barcelona Affiliation: 08193, Barcelona, Spain Affiliation: E-mail: joancarles.artes@uab.cat Marcos C. Mota Affiliation: Instituto de Ciências Matemáticas e de Computação, Affiliation: Universidade de São Paulo Affiliation: 13566–590, São Carlos, São Paulo, Brazil Affiliation: E-mail: coutinhomotam@gmail.com Alex C. Rezende Affiliation: Departamento de Matemática, Universidade Federal de São Carlos Affiliation: 13565-905, São Carlos, São Paulo, Brazil Affiliation: E-mail: alexcr@ufscar.br

###### Abstract

This paper presents a global study of the class 𝐐 ​ 𝐄𝐒 ^ \bf{Q}{\widehat{ES}} of all real quadratic polynomial differential systems possessing exactly one elemental infinite singular point and one triple infinite singular point, which is either an infinite nilpotent elliptic–saddle or a nilpotent saddle. This class can be divided into three different families, namely, 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) \bf{Q}{{\widehat{ES}(A)}} of phase portraits possessing three real finite singular points, 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) \bf{Q}{{\widehat{ES}(B)}} of phase portraits possessing one real and two complex finite singular points, and 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) \bf{Q}{{\widehat{ES}(C)}} of phase portraits possessing one real triple finite singular point. Here we provide the complete study of the geometry of these three families. Modulo the action of the affine group and time homotheties, families 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) \bf{Q}{{\widehat{ES}(A)}} and 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) \bf{Q}{{\widehat{ES}(B)}} are three–dimensional and family 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) \bf{Q}{{\widehat{ES}(C)}} is two–dimensional. We study the respective bifurcation diagrams of their closures with respect to specific normal forms, in subsets of real Euclidean spaces. The bifurcation diagram of family 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) \bf{Q}{{\widehat{ES}(A)}} (respectively, 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) \bf{Q}{{\widehat{ES}(B)}} and 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) \bf{Q}{{\widehat{ES}(C)}}) yields 1274 (respectively, 89 and 14) subsets with 91 (respectively, 27 and 12) topologically distinct phase portraits for systems in the closure 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) ¯ \overline{\bf{Q}{{\widehat{ES}(A)}}} (respectively, 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) ¯ \overline{\bf{Q}{{\widehat{ES}(B)}}} and 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) ¯ \overline{\bf{Q}{{\widehat{ES}(C)}}}) within the representatives of 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) \bf{Q}{{\widehat{ES}(A)}} (respectively, 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) \bf{Q}{{\widehat{ES}(B)}} and 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) \bf{Q}{{\widehat{ES}(C)}}) given by a specific normal form.

Key-words: quadratic differential system; infinite elliptic–saddle; infinite nilpotent saddle; bifurcation diagram; phase portrait; algebraic invariants.

## 1 Introduction, brief review of the literature and statement of the results

Here we call quadratic differential systems, or simply quadratic systems, differential systems of the form

 | x ˙ = p ⁡ ( x, y), y ˙ = q ⁡ ( x, y), \begin{array}[]{lcccl}\dot{x}&=&p(x,y),\\ \dot{y}&=&q(x,y),\\ \end{array} |  | (1) |

where p, q ∈ ℝ ⁡ [x, y] p,q\in\mathbb{R}[x,y] verify max ⁡ { deg ⁡ ( p), deg ⁡ ( q) } = 2 \max\{\deg(p),\deg(q)\}=2. To such systems we can associate the quadratic vector field

 | ξ = p ​ ∂ ∂ x + q ​ ∂ ∂ y, \xi=p\frac{\partial}{\partial x}+q\frac{\partial}{\partial y}, |  | (2) |

as well as the differential equation

 | q ​ d ​ x − p ​ d ​ y = 0. q\,dx-p\,dy=0. |  | (3) |

Along this paper we shall use indistinctly the expressions quadratic systems and quadratic vector fields to refer to either ( 1), or ( 2), or ( 3).

The class of all quadratic differential systems is denoted by QS.

We can also write systems ( 1) as

 | x ˙ = p 0 + p 1 ​ ( x, y) + p 2 ​ ( x, y) ≡ p ⁡ ( x, y), y ˙ = q 0 + q 1 ​ ( x, y) + q 2 ​ ( x, y) ≡ q ⁡ ( x, y), \begin{array}[]{lcccl}\dot{x}&=&p_{0}+p_{1}(x,y)+p_{2}(x,y)\equiv p(x,y),\\ \dot{y}&=&q_{0}+q_{1}(x,y)+q_{2}(x,y)\equiv q(x,y),\\ \end{array} |  | (4) |

where p i p_{i} and q i q_{i} are homogeneous polynomials of degree i i in the variables x x and y y with real coefficients and p 2 2 + q 2 2 ≠ 0 p_{2}^{2}+q_{2}^{2}\neq 0.

Even after hundreds of studies on the topology of real planar quadratic vector fields, it is somewhat impossible at this point to fully characterize their phase portraits and try to topologically classify them (which is very common in applications) due to the large number of parameters involved.

The main purpose of this paper is to present the study of the bifurcation diagrams of the class of quadratic systems possessing exactly one elemental infinite singular point and one triple infinite singular point, being an infinite nilpotent elliptic–saddle (which can be of three types: ( 1 2) ^ ​ P ​ H ​ P − E \widehat{\!{1\choose 2}\!\!}\ PHP-E, ( 1 2) ^ ​ H − E \widehat{\!{1\choose 2}\!\!}\ H-E, or ( 1 2) ^ ​ P ​ E ​ P − H \widehat{\!{1\choose 2}\!\!}\ PEP-H) or a nilpotent saddle ( 1 2) ^ ​ H ​ H ​ H − H \widehat{\!{1\choose 2}\!\!}\ HHH-H (see [6] for details on this notation). We denote this class by 𝐐 ​ 𝐄𝐒 ^ \bf{Q}{\widehat{ES}}. A nilpotent singularity is a point where both eigenvalues are zero but the Jacobian matrix is nonzero.

Whenever one wants to study a specific family of differential systems sharing a common property, it is necessary to select one (or several) normal form which contains all the phase portraits sharing the desired property. However, except for a few trivial cases, it is impossible that the normal form does not contain other phase portraits, normally more degenerate than the cases under study. These other phase portraits are very important for understanding the bifurcations that occur within the chosen normal form. Therefore, we always check not only the family of systems with the desired properties, but also the clousure of the normal form which contains that family. That is, we examine the entire parameter space of the chosen normal form, whether or not it leads to the desired property. However, it is possible that a different normal form could have been chosen, in which case the generic elements of the family should be the same, but the elements in the border might not be. That is, some phase portraits in the border of one normal form could be common or not, with elements in the border of the second normal form.

It is well known that quadratic systems possess at most four real simple finite singular points and at most three pairs of infinite singular points. As our aim is to study QS possessing an infinite singular point of multiplicity three, formed by the coalescence of one finite singular point with one double infinite singular point, a quadratic differential system from the class 𝐐 ​ 𝐄𝐒 ^ ¯ \overline{\bf{Q}{\widehat{ES}}} can have at most three simple real finite singular points and, in case it has total multiplicity 3 of finite singularities, it will have two pairs of infinite singular points, being one simple and the other one triple. So, inside the class 𝐐 ​ 𝐄𝐒 ^ ¯ \overline{\bf{Q}{\widehat{ES}}} we must consider the following families:

- •

𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) \bf{Q}{{\widehat{ES}(A)}}: quadratic systems possessing three real finite singular points, either an infinite nilpotent elliptic–saddle or an infinite nilpotent saddle, and an elemental infinite singularity;

- •

𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) \bf{Q}{{\widehat{ES}(B)}}: quadratic systems possessing one real and two complex finite singular points, either an infinite nilpotent elliptic–saddle or an infinite nilpotent saddle, and an elemental infinite singularity;

- •

𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) \bf{Q}{{\widehat{ES}(C)}}: quadratic systems possessing one real triple finite singular point, either an infinite nilpotent elliptic–saddle or an infinite nilpotent saddle, and an elemental infinite singularity.

For our proposed study, we followed the pattern specified in [14, 9] and, in order to avoid repeating technical common sections, we refer to the mentioned papers for more complete information.

All the phase portraits in this paper are drawn in the Poincaré disc (for its definition we refer to [15, 14]). In the sequel, we give the concept of graphics, which play an important role in obtaining limit cycles when they arise, for example, from connection of separatrices.

A (nondegenerate) graphic as defined in [16] is formed by a finite sequence of singular points r 1, r 2, …, r n r_{1},r_{2},\ldots,r_{n} (with possible repetitions) and non–trivial connecting orbits γ i \gamma_{i} for i = 1, …, n i=1,\ldots,n such that γ i \gamma_{i} has r i r_{i} as α \alpha –limit set and r i + 1 r_{i+1} as ω \omega –limit set for i < n i<n and γ n \gamma_{n} has r n r_{n} as α \alpha –limit set and r 1 r_{1} as ω \omega –limit set. Also normal orientations n j n_{j} of the non–trivial orbits must be coherent in the sense that if γ j − 1 \gamma_{j-1} has left–hand orientation then so does γ j \gamma_{j}. A polycycle is a graphic which has a Poincaré return map.

A degenerate graphic is formed by a finite sequence of singular points r 1, r 2, …, r n r_{1},r_{2},\ldots,r_{n} (with possible repetitions) and non–trivial connecting orbits and/or segments of curves of singular points γ i \gamma_{i} for i = 1, …, n i=1,\ldots,n such that γ i \gamma_{i} has r i r_{i} as α \alpha –limit set and r i + 1 r_{i+1} as ω \omega –limit set for i < n i<n and γ n \gamma_{n} has r n r_{n} as α \alpha –limit set and r 1 r_{1} as ω \omega –limit set. Also normal orientations n j n_{j} of the non–trivial orbits must be coherent in the sense that if γ j − 1 \gamma_{j-1} has left–hand orientation then so does γ j \gamma_{j}. For more details, see [16].

In [2] the authors proved the existence of 44 topologically different phase portraits for the structurally stable quadratic planar differential systems modulo limit cycles, also known as the codimension–zero quadratic systems. Roughly speaking, these systems are characterized by having all singularities, finite and infinite, simple, no separatrix connection, and where any nest of limit cycles counts as a single point with the stability of the outer limit cycle.

In addition, in [3] the authors classified the structurally unstable quadratic systems of codimension one modulo limit cycles which have one and only one of the simplest structurally unstable objects: a saddle–node of multiplicity two (finite or infinite), a separatrix from one saddle point to another, or a separatrix forming a loop for a saddle point with its divergence nonzero. All the phase portraits of codimension one are split into four sets according to the possession of a structurally unstable element:

- (A)

possessing a finite semi–elemental saddle–node;

- (B)

possessing an infinite semi–elemental saddle–node ( 0 2) ¯ ​ S ​ N \overline{\!{0\choose 2}\!\!}\ SN;

- (C)

possessing an infinite semi–elemental saddle–node ( 1 1) ¯ ​ S ​ N \overline{\!{1\choose 1}\!\!}\ SN; and

- (D)

possessing a separatrix connection.

The study of the codimension–one systems was carried out during a period of approximately 20 years, and this study yielded at least 204 (and at most 211) topologically distinct phase portraits of codimension one modulo limit cycles. Some recent research (already at preprint level) showed two mistakes in that book and reduced (and confirmed) the number of cases to 202 (and a most 209).

The next step is to study the structurally unstable quadratic systems of codimension two, modulo limit cycles. The approach is the same as used in the previous two works [2, 3]. One starts by looking for all the potential topological phase portraits of codimension two, and then tries to realize all of them or show that some of them are impossible. So, it is also very convenient to have studied a bifurcation diagram that helps us to solve the realization problem. In many publications of this last type where families of phase portraits have been studied, it is quite common that the authors have missed one or several phase portraits, as we discuss in Appendix A. This may happen either because they have not interpreted correctly some of the bifurcation parts, or they have missed the existence of some nonalgebraic bifurcation, or there may exist some small “island” as they are described in Sec. 3.1.1, 3.2.1, and 3.3.1. However, when examining all the potential topological phase portraits and systematically compiling error–free list, then there is no possibility of missing a realizable case. It is just a problem of finding examples of realization or producing irrefutable proofs of the impossibility of realization of phase portraits.

Research on codimension–two quadratic systems is already ongoing. In [11] the authors have considered set (AA) obtained by the existence of a cusp point, or two saddle–nodes or the coalescence of three finite singular points forming a semi–elemental singularity, yielding either a triple saddle, or a triple node. They obtained all the possible topological phase portraits of set (AA) and proved their realization. In their study, they got 34 new topologically distinct phase portraits in the Poincaré disc modulo limit cycles. Moreover, they proved the impossibility of one phase portrait among the 204 204 phase portraits presented in [3].

Moreover, the bifurcation diagram for the class of the quadratic systems possessing a finite saddle–node s ​ n ¯ ( 2) \overline{sn}_{(2)} and an infinite saddle–node ( 0 2) ¯ ​ S ​ N \overline{\!{0\choose 2}\!\!}\ SN was studied in [13, 14], in which all the phase portraits obtained belong to the closure of set (AB). Also, in [8, 9] the authors studied the bifurcation diagram for the class of quadratic systems possessing a finite saddle–node s ​ n ¯ ( 2) \overline{sn}_{(2)} and an infinite saddle–node ( 1 1) ¯ ​ S ​ N \overline{\!{1\choose 1}\!\!}\ SN and all the phase portraits obtained belong to the closure of set (AC).

The topological classification of sets (AB) and (AC) was done in [10]. In this study, the authors obtained 71 topologically distinct phase portraits modulo limit cycles for the set (AB), and for the set (AC) they got 40 ones.

Consider now the set (BC), characterized by quadratic systems possessing two types of coalescence of singular points:

- •

coalescence of two infinite elemental singular points; and

- •

coalescence of a finite elemental singular point with an infinite one.

In a near future we will present a paper that includes the study of the bifurcation diagram of quadratic systems with infinite saddle–nodes ( 0 2) ¯ ​ S ​ N \overline{\!{0\choose 2}\!\!}\ SN and ( 1 1) ¯ ​ S ​ N \overline{\!{1\choose 1}\!\!}\ SN.

Since here we want to study quadratic systems with exactly one elemental infinite singular point and one triple infinite singular point (in the sense that it is the coalescence of two infinite singularities plus a finite one), families 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) \bf{Q}{{\widehat{ES}(A)}} and 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) \bf{Q}{{\widehat{ES}(B)}} can be considered as codimension–two cases from the border of set (BC) and family 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) \bf{Q}{{\widehat{ES}(C)}} can be seeing as a codimension–four case from the border of set (BC).

In the normal form ( 5), see page 5, the class 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) ¯ \overline{\bf{Q}{{\widehat{ES}(A)}}} is partitioned into 1274 parts: 288 three–dimensional ones, 573 two–dimensional ones, 351 one–dimensional ones, and 62 points. This partition is obtained by considering all the bifurcation surfaces of singularities, and bifurcation surfaces related to the presence of invariant straight lines, the presence of invariant parabolas, and connections of separatrices, modulo “islands” (see Sec. 3.1.1).

Also, in the normal form ( 9), see page 9, the class 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) ¯ \overline{\bf{Q}{{\widehat{ES}(B)}}} is partitioned into 89 parts: 26 three–dimensional ones, 39 two–dimensional ones, 20 one–dimensional ones, and four points. This partition is obtained by considering all the bifurcation surfaces of singularities, and bifurcation surfaces related to the presence of invariant straight lines, the presence of invariant parabolas, the presence of curves filled up with singular points, and connections of separatrices, modulo “islands” (see Sec. 3.2.1).

Finally, in the normal form ( 13), see page 13, the class 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) ¯ \overline{\bf{Q}{{\widehat{ES}(C)}}} is partitioned into 14 parts: four two–dimensional ones, seven one–dimensional ones, and three points. This partition is obtained by considering all the bifurcation surfaces of singularities, the presence of curves filled up with singular points, and bifurcation surfaces related to the presence of invariant straight line and invariant parabola, modulo “islands” (see Sec. 3.3.1).

###### Theorem 1.

There are 91 91 topologically distinct phase portraits for the closure of the family of quadratic vector fields possessing three real finite singular points, either an infinite nilpotent elliptic–saddle or an infinite nilpotent saddle, and an elemental infinite singularity, and given by the normal form ( 5) (class 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) ¯ \overline{\bf{Q}{{\widehat{ES}(A)}}}). The bifurcation diagram for this class is given in the parameter space which is a subset of the real Euclidean three–dimensional space ℝ 3 \mathbb{R}^{3}. All these phase portraits are shown in Figs. 1 to 3. Also, for this class, the following statements hold:

1. (a)

there are 18 18 topologically distinct phase portraits in 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) \bf{Q}{{\widehat{ES}(A)}}, namely, V 1 V_{1}, V 9 V_{9}, V 11 V_{11}, V 12 V_{12}, V 66 V_{66}, V 89 V_{89}, V 91 V_{91}, V 94 V_{94}, V 101 V_{101}, V 168 V_{168}, V 170 V_{170}, V 173 V_{173}, V 176 V_{176}, V 188 V_{188}, V 233 V_{233}, V 235 V_{235}, V 238 V_{238}, and V 240 V_{240};

2. (b)

consider the 18 18 phase portraits from the previous item. Such phase portraits can be split according to the type of infinite singularities:

  - •

phase portraits V 1 V_{1}, V 9 V_{9}, V 11 V_{11}, V 12 V_{12}, and V 66 V_{66} possess an infinite nilpotent elliptic–saddle ( 1 2) ^ ​ P ​ E ​ P − H \widehat{\!{1\choose 2}\!\!}\ PEP-H and also an infinite elemental node;

  - •

phase portraits V 89 V_{89}, V 91 V_{91}, V 94 V_{94}, and V 101 V_{101} possess an infinite nilpotent elliptic–saddle ( 1 2) ^ ​ P ​ E ​ P − H \widehat{\!{1\choose 2}\!\!}\ PEP-H and also an infinite elemental saddle;

  - •

phase portraits V 168 V_{168}, V 170 V_{170}, V 173 V_{173}, V 176 V_{176}, and V 188 V_{188} possess an infinite nilpotent elliptic–saddle ( 1 2) ^ ​ E − P ​ H ​ P \widehat{\!{1\choose 2}\!\!}\ E-PHP and also an infinite elemental saddle;

  - •

phase portraits V 233 V_{233}, V 235 V_{235}, V 238 V_{238}, and V 240 V_{240} possess an infinite nilpotent saddle ( 1 2) ^ ​ H − H ​ H ​ H \widehat{\!{1\choose 2}\!\!}\ H-HHH and also an infinite elemental node;

in addition, from the study of the bifurcation diagram of class 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) ¯ \overline{\bf{Q}{{\widehat{ES}(A)}}} we observe the existence of 35 35 two–dimensional regions (modulo islands) in which the corresponding phase portraits possess an infinite nilpotent elliptic–saddle ( 1 2) ^ ​ H − E \widehat{\!{1\choose 2}\!\!}\ H-E and also an infinite elemental saddle;

3. (c)

there are ten phase portraits possessing exactly one simple limit cycle (or an odd number of them taking into account their multiplicity), and they are in the parts V 11 V_{11}, V 66 V_{66}, V 91 V_{91}, V 170 V_{170}, V 235 V_{235}, 2 ​ S 18 2S_{18}, 2 ​ S 30 2S_{30}, 2 ​ S 40 2S_{40}, 5 ​ S 3 5S_{3}, and 2.5 ​ L 6 2.5L_{6};

4. (d)

phase portraits 4.5 ​ L 1 4.5L_{1} and P 44 P_{44} possess the line at infinity filled up with singular points. Moreover, they have one infinite family of degenerate graphics;

5. (e)

there are nine phase portraits possessing only one nondegenerate graphic (surrounding a focus). More precisely, phase portraits 2 ​ S 39 2S_{39}, 7 ​ S 15 7S_{15}, 2.5 ​ L 5 2.5L_{5}, 2.7 ​ L 3 2.7L_{3}, 5.7 ​ L 1 5.7L_{1}, and P 46 P_{46} have only one finite graphic and phase portraits 2.5 ​ L 4 2.5L_{4}, 2.8 ​ L 11 2.8L_{11}, and P 45 P_{45} have only one infinite graphic;

6. (f)

there are 56 56 phase portraits having only one infinite family of nondegenerate graphics (with no singularity inside), and these phase portraits are in the parts V 1 V_{1}, V 9 V_{9}, V 11 V_{11}, V 12 V_{12}, V 66 V_{66}, V 89 V_{89}, V 91 V_{91}, V 94 V_{94}, V 101 V_{101}, V 168 V_{168}, V 170 V_{170}, V 173 V_{173}, V 176 V_{176}, V 188 V_{188}, 2 ​ S 1 2S_{1}, 2 ​ S 4 2S_{4}, 2 ​ S 5 2S_{5}, 2 ​ S 6 2S_{6}, 2 ​ S 11 2S_{11}, 2 ​ S 12 2S_{12}, 2 ​ S 13 2S_{13}, 2 ​ S 17 2S_{17}, 2 ​ S 18 2S_{18}, 2 ​ S 20 2S_{20}, 2 ​ S 23 2S_{23}, 2 ​ S 24 2S_{24}, 2 ​ S 25 2S_{25}, 2 ​ S 26 2S_{26}, 2 ​ S 28 2S_{28}, 2 ​ S 29 2S_{29}, 2 ​ S 30 2S_{30}, 2 ​ S 32 2S_{32}, 4 ​ S 5 4S_{5}, 4 ​ S 34 4S_{34}, 4 ​ S 59 4S_{59}, 7 ​ S 1 7S_{1}, 7 ​ S 4 7S_{4}, 7 ​ S 7 7S_{7}, 7 ​ S 11 7S_{11}, 8 ​ S 7 8S_{7}, 8 ​ S 77 8S_{77}, 2.3 ​ L 2 2.3L_{2}, 2.3 ​ L 7 2.3L_{7}, 2.3 ​ L 9 2.3L_{9}, 2.4 ​ L 1 2.4L_{1}, 2.4 ​ L 4 2.4L_{4}, 2.4 ​ L 5 2.4L_{5}, 2.4 ​ L 6 2.4L_{6}, 2.4 ​ L 7 2.4L_{7}, 2.7 ​ L 1 2.7L_{1}, 2.7 ​ L 2 2.7L_{2}, 2.8 ​ L 2 2.8L_{2}, 2.8 ​ L 8 2.8L_{8}, 2.8 ​ L 9 2.8L_{9}, 3.7 ​ L 1 3.7L_{1}, and 4.8 ​ L 2 4.8L_{2};

7. (g)

there are phase portraits that possess an infinite family of nondegenerate graphics (with no singularity inside) plus a finite number of nondegenerate graphics (which do not belong to the infinite family):

  - •

phase portraits 2 ​ S 1 2S_{1}, 2 ​ S 13 2S_{13}, and 2 ​ S 26 2S_{26} possess an infinite family of nondegenerate graphics plus one nondegenerate graphic with no singularity inside;

  - •

phase portraits 2 ​ S 17 2S_{17}, 2 ​ S 29 2S_{29}, 7 ​ S 1 7S_{1}, 7 ​ S 4 7S_{4}, 7 ​ S 7 7S_{7}, 7 ​ S 11 7S_{11}, 2.7 ​ L 1 2.7L_{1}, and 2.7 ​ L 2 2.7L_{2} possess an infinite family of nondegenerate graphics plus one nondegenerate graphic surrounding a focus;

  - •

phase portraits 3.7 ​ L 1 3.7L_{1} and 4.8 ​ L 2 4.8L_{2} possess an infinite family of nondegenerate graphics plus one nondegenerate graphic surrounding a center;

  - •

phase portraits 2 ​ S 28 2S_{28} and 2.8 ​ L 9 2.8L_{9} possess an infinite family of nondegenerate graphics plus two nondegenerate graphics surrounding the same focus;

  - •

phase portrait 2.4 ​ L 5 2.4L_{5} possesses an infinite family of nondegenerate graphics plus two nondegenerate graphics in which one of them surrounds a focus and the other one with no singularity inside;

  - •

phase portrait 2.4 ​ L 7 2.4L_{7} possesses an infinite family of nondegenerate graphics plus three nondegenerate graphics in which two of them surround the same focus and the other one with no singularity inside;

8. (h)

phase portraits V 11 V_{11}, V 66 V_{66}, V 91 V_{91}, V 170 V_{170}, 2 ​ S 18 2S_{18}, and 2 ​ S 30 2S_{30} possess an infinite family of nondegenerate graphics plus one limit cycle.

###### Theorem 2.

There are 27 27 topologically distinct phase portraits for the closure of the family of quadratic vector fields possessing one real and two complex finite singular points, either an infinite nilpotent elliptic–saddle or an infinite nilpotent saddle, and an elemental infinite singularity, and given by the normal form ( 9) (class 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) ¯ \overline{\bf{Q}{{\widehat{ES}(B)}}}). The bifurcation diagram for this class is given in the parameter space which is a subset of the real Euclidean three–dimensional space ℝ 3 \mathbb{R}^{3}. All these phase portraits are shown in Fig. 4. Also, for this class, the following statements hold:

1. (a)

there are ten topologically distinct phase portraits in 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) \bf{Q}{{\widehat{ES}(B)}}, namely, V 1 V_{1}, V 5 V_{5}, V 9 V_{9}, V 12 V_{12}, V 14 V_{14}, V 15 V_{15}, V 16 V_{16}, V 17 V_{17}, V 20 V_{20}, and V 24 V_{24};

2. (b)

consider the ten phase portraits from the previous item. Such phase portraits can be split according to the type of infinite singularities:

  - •

phase portrait V 1 V_{1} possesses an infinite nilpotent elliptic–saddle ( 1 2) ^ ​ P ​ E ​ P − H \widehat{\!{1\choose 2}\!\!}\ PEP-H and also an infinite elemental node;

  - •

phase portraits V 5 V_{5} and V 9 V_{9} possess an infinite nilpotent elliptic–saddle ( 1 2) ^ ​ P ​ E ​ P − H \widehat{\!{1\choose 2}\!\!}\ PEP-H and also an infinite elemental saddle;

  - •

phase portraits V 12 V_{12}, V 14 V_{14}, V 15 V_{15}, V 16 V_{16}, and V 17 V_{17} possess an infinite nilpotent elliptic–saddle ( 1 2) ^ ​ E − P ​ H ​ P \widehat{\!{1\choose 2}\!\!}\ E-PHP and also an infinite elemental saddle;

  - •

phase portraits V 20 V_{20} and V 24 V_{24} possess an infinite nilpotent saddle ( 1 2) ^ ​ H − H ​ H ​ H \widehat{\!{1\choose 2}\!\!}\ H-HHH and also an infinite elemental node;

in addition, from the study of the bifurcation diagram of class 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) ¯ \overline{\bf{Q}{{\widehat{ES}(B)}}} we observe the existence of five two–dimensional regions (modulo islands) in which the corresponding phase portraits possess an infinite nilpotent elliptic–saddle ( 1 2) ^ ​ H − E \widehat{\!{1\choose 2}\!\!}\ H-E and also an infinite elemental saddle;

3. (c)

there are six phase portraits possessing exactly one simple limit cycle (or an odd number of them taking into account their multiplicity), and they are in the parts V 9 V_{9}, V 16 V_{16}, V 17 V_{17}, V 24 V_{24}, 5 ​ S 4 5S_{4} and 7 ​ S 2 7S_{2};

4. (d)

phase portraits 1 ​ S 1 1S_{1} and 1.1 ​ L 1 1.1L_{1} possess curves filled up with singular points. Moreover, they have one infinite family of degenerate graphics;

5. (e)

phase portraits 4.5 ​ L 1 4.5L_{1} and P 4 P_{4} possess the line at infinity filled up with singular points. Moreover, they have one infinite family of degenerate graphics;

6. (f)

there are three phase portraits possessing only one nondegenerate infinite graphic (surrounding a focus) and they are in the parts 5 ​ S 3 5S_{3}, 8 ​ S 5 8S_{5} and 5.8 ​ L 2 5.8L_{2}. In addition, phase portrait 4.8 ​ L 5 4.8L_{5} possesses only one nondegenerate infinite graphic (surrounding a center).

7. (g)

there are 15 15 phase portraits having only one infinite family of nondegenerate graphics (with no singularity inside), and these phase portraits are in the parts V 1 V_{1}, V 5 V_{5}, V 9 V_{9}, V 12 V_{12}, V 14 V_{14}, V 15 V_{15}, V 16 V_{16}, V 17 V_{17}, 4 ​ S 2 4S_{2}, 4 ​ S 3 4S_{3}, 7 ​ S 1 7S_{1}, 7 ​ S 2 7S_{2}, 8 ​ S 4 8S_{4}, 4.8 ​ L 3 4.8L_{3}, and 4.8 ​ L 4 4.8L_{4};

8. (h)

there are phase portraits that possess an infinite family of nondegenerate graphics (with no singularity inside) plus a finite number of nondegenerate graphics (which do not belong to the infinite family):

  - •

phase portraits 4 ​ S 2 4S_{2} and 7 ​ S 1 7S_{1} possess an infinite family of nondegenerate graphics plus one nondegenerate graphic surrounding a focus;

  - •

phase portrait 4.8 ​ L 3 4.8L_{3} possesses an infinite family of nondegenerate graphics plus one nondegenerate graphic surrounding a center;

  - •

phase portrait 7 ​ S 2 7S_{2} possesses an infinite family of nondegenerate graphics plus one nondegenerate graphic surrounding a limit cycle;

  - •

phase portraits V 14 V_{14}, V 15 V_{15}, 4 ​ S 3 4S_{3}, and 8 ​ S 4 8S_{4} possess an infinite family of nondegenerate graphics plus two nondegenerate graphics surrounding the same focus;

  - •

phase portrait V 16 V_{16} possesses an infinite family of nondegenerate graphics plus two nondegenerate graphics surrounding the same limit cycle;

  - •

phase portrait 4.8 ​ L 4 4.8L_{4} possesses an infinite family of nondegenerate graphics plus two nondegenerate graphics surrounding the same center;

9. (i)

phase portraits V 9 V_{9}, V 16 V_{16}, V 17 V_{17}, and 7 ​ S 2 7S_{2} possess an infinite family of nondegenerate graphics plus one limit cycle.

###### Theorem 3.

There are twelve topologically distinct phase portraits for the closure of the family of quadratic vector fields possessing one real triple finite singular point, either an infinite nilpotent elliptic–saddle or an infinite nilpotent saddle, and an elemental infinite singularity, and given by the normal form ( 13) (class 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) ¯ \overline{\bf{Q}{{\widehat{ES}(C)}}}). The bifurcation diagram for this class is given in the parameter space which is a subset of the real Euclidean two–dimensional space ℝ 2 \mathbb{R}^{2}. All these phase portraits are shown in Fig. 5. Also, for this class, the following statements hold:

1. (a)

there are four topologically distinct phase portraits in 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) \bf{Q}{{\widehat{ES}(C)}}, namely, S 1 S_{1}, S 2 S_{2}, S 3 S_{3}, and S 4 S_{4};

2. (b)

the four phase portraits from the previous item can be split according to the type of infinite singularities:

  - •

phase portrait S 1 S_{1} possesses an infinite nilpotent saddle ( 1 2) ^ ​ H − H ​ H ​ H \widehat{\!{1\choose 2}\!\!}\ H-HHH and also an infinite elemental node;

  - •

phase portrait S 2 S_{2} possesses an infinite nilpotent elliptic–saddle ( 1 2) ^ ​ E − P ​ H ​ P \widehat{\!{1\choose 2}\!\!}\ E-PHP and also an infinite elemental saddle;

  - •

phase portrait S 3 S_{3} possesses an infinite nilpotent elliptic–saddle ( 1 2) ^ ​ P ​ E ​ P − H \widehat{\!{1\choose 2}\!\!}\ PEP-H and also an infinite elemental saddle;

  - •

phase portrait S 4 S_{4} possesses an infinite nilpotent elliptic–saddle ( 1 2) ^ ​ P ​ E ​ P − H \widehat{\!{1\choose 2}\!\!}\ PEP-H and also an infinite elemental node;

in addition, from the study of the bifurcation diagram of class 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) ¯ \overline{\bf{Q}{{\widehat{ES}(C)}}} we observe the existence of one one–dimensional region (modulo islands) in which the corresponding phase portrait possesses an infinite nilpotent elliptic–saddle ( 1 2) ^ ​ H − E \widehat{\!{1\choose 2}\!\!}\ H-E and also an infinite elemental saddle;

3. (c)

there are no phase portraits possessing a limit cycle;

4. (d)

phase portraits 1 ​ L 1 1L_{1} and P 3 P_{3} possess curves filled up with singular points. Moreover, they have one infinite family of degenerate graphics;

5. (e)

phase portrait P 1 P_{1} possesses the line at infinity filled up with singular points. Moreover, it has two infinite families of degenerate graphics;

6. (f)

there is no phase portraits possessing only one nondegenerate graphic;

7. (g)

there are five phase portraits having only one infinite family of nondegenerate graphics (with no singularity inside), and these phase portraits are in the parts S 2 S_{2}, S 3 S_{3}, S 4 S_{4}, 8 ​ L 1 8L_{1}, and P 1 P_{1}. Moreover, phase portraits 8 ​ L 2 8L_{2}, 8 ​ L 3 8L_{3}, and P 2 P_{2} possess more than one infinite family of nondegenerate graphics;

8. (h)

there is no phase portrait possessing a finite number of nondegenerate graphics;

9. (i)

there is no phase portrait possessing an infinite family of nondegenerate graphics plus one limit cycle.

###### Proposition 1.

There are 13 13 topologically distinct phase portraits of codimension two, modulo limit cycles, in family 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) \bf{Q}{{\widehat{ES}(A)}} and six in family 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) \bf{Q}{{\widehat{ES}(B)}}. The four topologically distinct phase portraits of codimension four without limit cycles in family 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) \bf{Q}{{\widehat{ES}(C)}} are topologically equivalent to phase portraits from family 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) \bf{Q}{{\widehat{ES}(B)}}. So, in total we have 19 19 topologically distinct phase portraits, modulo limit cycles.

###### Corollary 1.

In Table 1 (respectively, Tables 2 and 3) we give the numbers of phase portraits of both families 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) \bf{Q}{{\widehat{ES}(A)}} (respectively, 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) \bf{Q}{{\widehat{ES}(B)}} and 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) \bf{Q}{{\widehat{ES}(C)}}) and its closure for special types of phase portraits.

Table 1: Comparison between the set 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) \bf{Q}{{\widehat{ES}(A)}} and its border (the numbers represent the absolute values in each subclass)

 | 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) \bf{Q}{{\widehat{ES}(A)}} | Border of |

 | 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) \bf{Q}{{\widehat{ES}(A)}} |

Distinct phase portraits | 18 18 | 73 73 |

Phase portraits with exactly one | 5 5 | 5 5 |

simple limit cycle |

Phase portraits with exactly one | 0 0 | 9 9 |

nondegenerate graphic |

Phase portraits with at least | 14 14 | 42 42 |

one infinite family of |

nondegenerate graphics |

Phase portraits with degenerate | 0 0 | 2 2 |

graphics |

Table 2: Comparison between the set 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) \bf{Q}{{\widehat{ES}(B)}} and its border (the numbers represent the absolute values in each subclass)

 | 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) \bf{Q}{{\widehat{ES}(B)}} | Border of |

 | 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) \bf{Q}{{\widehat{ES}(B)}} |

Distinct phase portraits | 10 10 | 15 15 |

Phase portraits with exactly one | 4 4 | 2 2 |

simple limit cycle |

Phase portraits with exactly one | 0 0 | 4 4 |

nondegenerate graphic |

Phase portraits with at least | 8 8 | 7 7 |

one infinite family of |

nondegenerate graphics |

Phase portraits with degenerate | 0 0 | 4 4 |

graphics |

Table 3: Comparison between the set 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) \bf{Q}{{\widehat{ES}(C)}} and its border (the numbers represent the absolute values in each subclass)

 | 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) \bf{Q}{{\widehat{ES}(C)}} | Border of |

 | 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) \bf{Q}{{\widehat{ES}(C)}} |

Distinct phase portraits | 4 4 | 6 6 |

Phase portraits with at least | 3 3 | 5 5 |

one infinite family of |

nondegenerate graphics |

Phase portraits with degenerate | 0 0 | 3 3 |

graphics |

###### Corollary 2.

There are seven topologically distinct phase portraits which appear simultaneously in both classes 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) ¯ \overline{\bf{Q}{{\widehat{ES}(B)}}} and 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) ¯ \overline{\bf{Q}{{\widehat{ES}(C)}}}. The correspondences are indicated in Table 4 and the phase portraits in each row are topologically equivalent.

Table 4: Topological equivalence between phase portraits from classes 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) ¯ \overline{\bf{Q}{{\widehat{ES}(B)}}} and 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) ¯ \overline{\bf{Q}{{\widehat{ES}(C)}}}

𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) ¯ \overline{\bf{Q}{{\widehat{ES}(B)}}} | 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) ¯ \overline{\bf{Q}{{\widehat{ES}(C)}}} |

V 1 V_{1} | S 4 S_{4} |

V 7 V_{7} | S 3 S_{3} |

V 18 V_{18} | S 2 S_{2} |

V 28 V_{28} | S 1 S_{1} |

1 ​ S 1 1S_{1} | 1 ​ L 1 1L_{1} |

5 ​ S 1 5S_{1} | 5 ​ L 1 5L_{1} |

1.1 ​ L 1 1.1L_{1} | P 3 P_{3} |

Figure 1: Phase portraits for quadratic vector fields possessing three real finite singular points, either an infinite nilpotent elliptic–saddle or an infinite nilpotent saddle, and an elemental infinite singularity, from class 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) ¯ \overline{\bf{Q}{{\widehat{ES}(A)}}} Figure 2: Continuation of Fig. 1 Figure 3: Continuation of Fig. 2 Figure 4: Phase portraits for quadratic vector fields possessing one real and two complex finite singular points, either an infinite nilpotent elliptic–saddle or an infinite nilpotent saddle, and an elemental infinite singularity, from class 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) ¯ \overline{\bf{Q}{{\widehat{ES}(B)}}} Figure 5: Phase portraits for quadratic vector fields possessing one real triple finite singular point, either an infinite nilpotent elliptic–saddle or an infinite nilpotent saddle, and an elemental infinite singularity, from class 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) ¯ \overline{\bf{Q}{{\widehat{ES}(C)}}}

In Figs. 1 to 5 we have illustrated all the singularities with a small disc. In case of degenerate systems we have also illustrated the infinite singular point belonging to the degenerate set with a small disc only if this point is an infinite singularity of the reduced system. We have drawn with thicker curves the separatrices and we have added some thinner orbits to avoid confusion in some cases.

We have drawn all the limit cycles (and loops) possessing a convex shape (see Lemma 3.31 from [3]). The limit cycles are colored in red (as in [9], for instance) and all the graphics are colored in blue.

###### Remark 1.

We label the phase portraits according to the parts of the bifurcation diagram where they occur. Here we call volumes ( V V) the three–dimensional parts of the bifurcation diagram, surfaces ( S S) the two–dimensional ones, curves ( L L) the one–dimensional ones, and points ( P P) the zero–dimensional ones. These labels could be different for two topologically equivalent phase portraits occurring in distinct parts. Some of the phase portraits in three–dimensional parts also occur in some lower dimensional parts bordering these three–dimensional parts. An example occurs when a node turns into a focus. An analogous situation happens for phase portraits in two–dimensional or one–dimensional parts, coinciding with some phase portraits situated on their border. Moreover, as in [4, 14, 9], we use the same pattern in order to indicate the elements ( V V), ( S S), ( L L) and ( P P) in the bifurcation diagram.

This paper is organized as follows. In this section we have presented an introduction to this study, a brief review and some results already existent on the literature, and the statement of our main results.

In Sec. 2 we describe the normal forms that describe families 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) \bf{Q}{{\widehat{ES}(A)}}, 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) \bf{Q}{{\widehat{ES}(B)}}, and 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) \bf{Q}{{\widehat{ES}(C)}}. Moreover, in such a section we present a study of invariant algebraic curves (straight lines and parabolas) for each family.

In Sec. 3 we present the study of the three bifurcation diagrams. More precisely, in Sec. 3.1 (respectively, Sec. 3.2 and Sec. 3.3) we present the bifurcation diagram of family 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) \bf{Q}{{\widehat{ES}(A)}} (respectively, 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) \bf{Q}{{\widehat{ES}(B)}} and 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) \bf{Q}{{\widehat{ES}(C)}}). Related to the study of each family we present three subsections discussing, respectively, on the possible existence of “islands” in the corresponding bifurcation diagram, on the classification (up to topological equivalence) of the phase portraits, and on the completion of the proof of the correspondent theorem from Sec. 1.

In Appendix A we present some incompatibilities found in previous studies of phase portraits possessing specific properties on its singularities.

## 2 Normal forms and invariant algebraic curves from class 𝐐 ​ 𝐄𝐒 ^ \bf{Q}{\widehat{ES}}

In Table 6.1 from the book [6] one can obtain canonical forms of quadratic systems possessing different kinds of singular points. In this section we use the invariant theory in order to perform some affine transformations and time rescaling so that we obtain the normal forms that describe families 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) \bf{Q}{{\widehat{ES}(A)}}, 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) \bf{Q}{{\widehat{ES}(B)}}, and 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) \bf{Q}{{\widehat{ES}(C)}}.

###### Proposition 2.

Every nondegenerate quadratic system possessing three real finite singular points plus either an infinite nilpotent elliptic–saddle or an infinite nilpotent saddle, can be brought via affine transformations and time rescaling to the following normal form

 |  | x ′ = c ​ x + y − c ​ x 2, \displaystyle x^{\prime}=cx+y-cx^{2}, |  | (5) |

 |  | y ′ = e ​ x + ( − 1 + e + f c) ​ y − e ​ x 2 + 2 ​ x ​ y, \displaystyle y^{\prime}=ex+\left(-1+\dfrac{e+f}{c}\right)y-ex^{2}+2xy, |  |

where c ∈ ℝ ∖ { 0 } c\in\mathbb{R}\setminus\{0\}, f ∈ ℝ + ∪ { 0 } f\in\mathbb{R}^{+}\cup\{0\}, and e ∈ ℝ e\in\mathbb{R} are parameters, describing family 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) \bf{Q}{{\widehat{ES}(A)}}.

###### Proof.

In fact, from [6, Table 6.1] we get the so called canonical form 10 (see systems ( 6)), obtained by using affine transformations and time rescaling, which describes quadratic systems possessing three real finite singular points and one infinite singular point of multiplicity two (formed by the coalescence of one finite and one infinite elemental singular points).

 |  | x ′ = c ​ x + d ​ y − c ​ x 2 + 2 ​ h ​ x ​ y, \displaystyle x^{\prime}=cx+dy-cx^{2}+2hxy, |  | (6) |

 |  | y ′ = e ​ x + f ​ y − e ​ x 2 + 2 ​ m ​ x ​ y, \displaystyle y^{\prime}=ex+fy-ex^{2}+2mxy, |  |

where c, d, h, e, f, m c,d,h,e,f,m are real parameters, verifying conditions

 | ( e ​ h − c ​ m) ​ ( c ​ f − d ​ e) ​ ( d ​ m − f ​ h) ​ ( 2 ​ ( e ​ h − c ​ m) − ( c ​ f − d ​ e)) ≠ 0. (eh\!-\!cm)(cf\!-\!de)(dm\!-\!fh)(2(eh\!-\!cm)\!-\!(cf\!-\!de))\!\neq\!0. |  |

For these systems, computations show that

 |  | μ 0 = 0, \displaystyle\mu_{0}=0, |  |

 |  | μ 1 = − 4 ​ ( e ​ h − c ​ m) ​ ( f ​ h − d ​ m) ​ x, \displaystyle\mu_{1}=-4(eh-cm)(fh-dm)x, |  |

 |  | η = 4 ​ h 2 ​ ( − 8 ​ e ​ h + ( c + 2 ​ m) 2), \displaystyle\eta=4h^{2}(-8eh+(c+2m)^{2}), |  |

 |  | M ~ = − 8 ​ ( ( − 6 ​ e ​ h + ( c + 2 ​ m) 2) ​ x 2 − 2 ​ h ​ ( c + 2 ​ m) ​ x ​ y + 4 ​ h 2 ​ y 2), \displaystyle\widetilde{M}\!=\!-8(\!(\!-6eh\!+\!(\!c\!+\!2m\!)^{2})x^{2}\!-\!2h(\!c\!+\!2m\!)xy\!+\!4h^{2}\!y^{2}), |  |

 |  | κ = − 128 ​ h 2 ​ ( e ​ h − c ​ m). \displaystyle\kappa=-128h^{2}(eh-cm). |  |

According to [6, Diagram 6.3] we observe that in order to have three real elemental finite singularities and two singular points at infinity, being one real elemental singularity and the other one a triple point formed by the coalescence of one finite singularity with two infinite ones, the previous invariants must verify

 | μ 0 = 0, μ 1 ≠ 0, η = 0, M ~ ≠ 0, κ = 0, \mu_{0}=0,\quad\mu_{1}\neq 0,\quad\eta=0,\quad\widetilde{M}\neq 0,\quad\kappa=0, |  |

respectively. So, by considering h = 0 h=0 at systems ( 6) we have systems

 |  | x ′ = c ​ x + d ​ y − c ​ x 2, \displaystyle x^{\prime}=cx+dy-cx^{2}, |  | (7) |

 |  | y ′ = e ​ x + f ​ y − e ​ x 2 + 2 ​ m ​ x ​ y, \displaystyle y^{\prime}=ex+fy-ex^{2}+2mxy, |  |

where c, d, e, f, m c,d,e,f,m are real parameters, verifying conditions

 | c ​ d ​ m ​ ( c ​ f − d ​ e) ​ [2 ​ c ​ m + ( c ​ f − d ​ e)] ≠ 0, cdm(cf-de)\left[2cm+(cf-de)\right]\!\neq\!0, |  | (8) |

and, for systems ( 7),

 |  | μ 0 = 0, \displaystyle\mu_{0}=0, |  |

 |  | μ 1 = − 4 ​ c ​ d ​ m 2 ​ x, \displaystyle\mu_{1}=-4cdm^{2}x, |  |

 |  | η = 0, \displaystyle\eta=0, |  |

 |  | M ~ = − 8 ​ ( c + 2 ​ m) 2 ​ x 2, \displaystyle\widetilde{M}=-8(c+2m)^{2}x^{2}, |  |

 |  | κ = 0. \displaystyle\kappa=0. |  |

Since d ≠ 0 d\neq 0 and m ≠ 0 m\neq 0 (due to ( 8)), we perform the change

 | ( x, y, t) → ( x, ( m / d) ​ y, t / m), (x,y,t)\rightarrow(x,(m/d)y,t/m), |  |

and we get systems

 |  | x ′ = c m ​ x + y − c m ​ x 2, \displaystyle x^{\prime}=\frac{c}{m}x+y-\frac{c}{m}x^{2}, |  |

 |  | y ′ = d ​ e m 2 ​ x + f m ​ y − d ​ e m 2 ​ x 2 + 2 ​ x ​ y. \displaystyle y^{\prime}=\frac{de}{m^{2}}x+\frac{f}{m}y-\frac{de}{m^{2}}x^{2}+2xy. |  |

By renaming

 | c m → c, d ​ e m 2 → e, f m → f, \frac{c}{m}\rightarrow c,\quad\frac{de}{m^{2}}\rightarrow e,\quad\frac{f}{m}\rightarrow f, |  |

we obtain systems ( 7) with d = m = 1 d=m=1.
Now we compute the following polynomial invariants:

 |  | ℬ 1 = 2 ​ ( c − f − 2) ​ ( c + f) ​ [e + c ⁡ ( c − e + c ​ f)], \displaystyle\mathcal{B}_{1}=2(c-f-2)(c+f)\left[e+c(c-e+cf)\right], |  |

 |  | 𝔻 = − 192 ​ ( c ​ f − e) 2 ​ ( 2 ​ c − e + c ​ f) 2. \displaystyle\mathbb{D}=-192(cf-e)^{2}(2c-e+cf)^{2}. |  |

These polynomial invariants (whose meaning will be explained later) shall define bifurcation surfaces. From the factors of ℬ 1 \mathcal{B}_{1} we observe that we can perform a translation

 | f = F − 1, f=F-1, |  |

and we obtain

 | 𝔻 = − 192 ​ ( c + e − c ​ F) 2 ​ ( c − e + c ​ F) 2. \mathbb{D}=-192(c+e-cF)^{2}(c-e+cF)^{2}. |  |

We rewrite the factors of 𝔻 \mathbb{D} as a pair of horizontal parallel straight lines, i.e. we solve

 | − c − e + c ⁡ ( f + 1) = F − c ~ and c − e + c ⁡ ( f + 1) = F + c ~, -c-e+c(f+1)=F-\tilde{c}\quad\text{and}\quad c-e+c(f+1)=F+\tilde{c}, |  |

which yield

 | f = e − c + F c, c ~ = c, f=\frac{e-c+F}{c},\quad\tilde{c}=c, |  |

and we rename F = f F=f. Remember that c ≠ 0 c\neq 0 due to conditions ( 8). Therefore we arrive at systems ( 5). Indeed, by considering the change

 | ( x, y, t) → ( − x + 1, y, − t) (x,y,t)\rightarrow(-x+1,y,-t) |  |

we obtain systems

 |  | x ′ = c ​ x + y − c ​ x 2, \displaystyle x^{\prime}=cx+y-cx^{2}, |  |

 |  | y ′ = − e ​ x − ( 1 + e + f c) ​ y + e ​ x 2 + 2 ​ x ​ y, \displaystyle y^{\prime}=-ex-\left(1+\dfrac{e+f}{c}\right)y+ex^{2}+2xy, |  |

i.e. ( c, e, f) → ( c, − e, − f) (c,e,f)\rightarrow(c,-e,-f), so one can consider f ∈ ℝ + ∪ { 0 } f\in\mathbb{R}^{+}\cup\{0\}. ∎

The next two results assure the existence of invariant straight lines and invariant parabolas, respectively, under certain conditions for family ( 5).

###### Lemma 1.

Family ( 5) possesses the following invariant straight line if and only if the corresponding condition is satisfied:

1. (i)

{ y = 0 } ⇔ e = 0 \{y=0\}\Leftrightarrow e=0;

2. (ii)

{ c − f − ( c − f) x + 2 y = 0 } ⇔ e = ( 2 + c) ( c − f) / 2 \{c-f-(c-f)x+2y=0\}\Leftrightarrow e=(2+c)(c-f)/2;

3. (iii)

{ ( c + f) x + 2 y = 0 } ⇔ e = − ( 2 + c) ( c + f) / 2 \{(c+f)x+2y=0\}\Leftrightarrow e=-(2+c)(c+f)/2.

###### Proof.

We consider the algebraic curves

 | f 1 ​ ( x, y) \displaystyle f_{1}(x,y) | ≡ y = 0, \displaystyle\equiv y=0, |  |

 | f 2 ​ ( x, y) \displaystyle f_{2}(x,y) | ≡ − c + f + ( c − f) ​ x − 2 ​ y = 0, \displaystyle\equiv-c+f+(c-f)x-2y=0, |  |

 | f 3 ​ ( x, y) \displaystyle f_{3}(x,y) | ≡ ( c + f) ​ x + 2 ​ y = 0, \displaystyle\equiv(c+f)x+2y=0, |  |

and we show that the polynomials

 | K 1 ​ ( x, y) \displaystyle K_{1}(x,y) | = 2 ​ x + ( f − c) / c, \displaystyle=2x+(f-c)/c, |  |

 | K 2 ​ ( x, y) \displaystyle K_{2}(x,y) | = 2 ​ x, \displaystyle=2x, |  |

 | K 3 ​ ( x, y) \displaystyle K_{3}(x,y) | = 2 ​ ( x − 1), \displaystyle=2(x-1), |  |

are the cofactors of f 1 = 0 f_{1}=0, f 2 = 0 f_{2}=0, and f 3 = 0 f_{3}=0, respectively, after restricting family ( 5) to the respective conditions. ∎

###### Lemma 2.

Family ( 5) possesses the following invariant parabola if and only if the corresponding condition is satisfied:

1. (i)

{ − c + c 2 + e c + 2 ​ c + 2 ​ c 2 + e c x − ( 1 + c) x 2 + y = 0 } ⇔ f = − ( 2 c 2 + c + 2 e) \left\{-\dfrac{c+c^{2}+e}{c}+\dfrac{2c+2c^{2}+e}{c}x-(1+c)x^{2}+y=0\right\}\Leftrightarrow f=-(2c^{2}+c+2e);

2. (ii)

{ e c x − ( 1 + c) x 2 + y = 0 } ⇔ f = 2 c 2 + c − 2 e \left\{\dfrac{e}{c}x-(1+c)x^{2}+y=0\right\}\Leftrightarrow f=2c^{2}+c-2e;

3. (iii)

{ ( 1 + c) x − ( 1 + c) x 2 + y = 0 } ⇔ e = − f ( 1 + c) \{(1+c)x-(1+c)x^{2}+y=0\}\Leftrightarrow e=-f(1+c);

###### Proof.

We consider the algebraic curves

 | g 1 ​ ( x, y) \displaystyle g_{1}(x,y) | ≡ − c + c 2 + e c + 2 ​ c + 2 ​ c 2 + e c ​ x − ( 1 + c) ​ x 2 + y = 0, \displaystyle\equiv-\dfrac{c+c^{2}+e}{c}+\dfrac{2c+2c^{2}+e}{c}x-(1+c)x^{2}+y=0, |  |

 | g 2 ​ ( x, y) \displaystyle g_{2}(x,y) | ≡ e c ​ x − ( 1 + c) ​ x 2 + y = 0, \displaystyle\equiv\dfrac{e}{c}x-(1+c)x^{2}+y=0, |  |

 | g 3 ​ ( x, y) \displaystyle g_{3}(x,y) | ≡ ( 1 + c) ​ x − ( 1 + c) ​ x 2 + y = 0, \displaystyle\equiv(1+c)x-(1+c)x^{2}+y=0, |  |

and we show that the polynomials

 | H 1 ​ ( x, y) \displaystyle H_{1}(x,y) | = − 2 ​ c ​ x, \displaystyle=-2cx, |  |

 | H 2 ​ ( x, y) \displaystyle H_{2}(x,y) | = 2 ​ c ​ ( 1 − x), \displaystyle=2c(1-x), |  |

 | H 3 ​ ( x, y) \displaystyle H_{3}(x,y) | = c − f − 2 ​ c ​ x, \displaystyle=c-f-2cx, |  |

are the cofactors of g 1 = 0 g_{1}=0, g 2 = 0 g_{2}=0, and g 3 = 0 g_{3}=0, respectively, after restricting family ( 5) to the respective conditions. ∎

The study of the bifurcation diagram of family ( 5) is presented in Sec. 3.1.

###### Proposition 3.

Every nondegenerate quadratic system possessing one real and two complex finite singular points plus either an infinite nilpotent elliptic–saddle or an infinite nilpotent saddle, can be brought via affine transformations and time rescaling to the following normal form

 |  | x ′ = − 2 ​ g ​ u ​ x + g ⁡ ( 1 + u 2) ​ y + g ​ x 2, \displaystyle x^{\prime}=-2gux+g(1+u^{2})y+gx^{2}, |  | (9) |

 |  | y ′ = − 2 ​ ( ℓ ​ u − 1) ​ x + ℓ ⁡ ( 1 + u 2) ​ y + ℓ ​ x 2 − 2 ​ x ​ y, \displaystyle y^{\prime}=-2(\ell u-1)x+\ell(1+u^{2})y+\ell x^{2}-2xy, |  |

where g ∈ ℝ ∖ { 0 } g\in\mathbb{R}\setminus\{0\}, u ∈ ℝ + ∪ { 0 } u\in\mathbb{R}^{+}\cup\{0\}, and ℓ ∈ ℝ \ell\in\mathbb{R} are parameters, describing family 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) \bf{Q}{{\widehat{ES}(B)}}.

###### Proof.

In fact, from [6, Table 6.1] we get the so called canonical form 11 (see systems ( 10)), obtained by using affine transformations and time rescaling, which describes quadratic systems possessing one real and two complex finite singular points plus one infinite singular point of multiplicity two (formed by the coalescence of one finite and one infinite elemental singular points).

 |  | x ′ = 2 ​ ( h − g ​ u) ​ x + g ⁡ ( u 2 + 1) ​ y + g ​ x 2 − 2 ​ h ​ x ​ y, \displaystyle x^{\prime}=2(h-gu)x+g(u^{2}+1)y+gx^{2}-2hxy, |  | (10) |

 |  | y ′ = 2 ​ ( m − ℓ ​ u) ​ x + ℓ ⁡ ( u 2 + 1) ​ y + ℓ ​ x 2 − 2 ​ m ​ x ​ y, \displaystyle y^{\prime}=2(m-\ell u)x+\ell(u^{2}+1)y+\ell x^{2}-2mxy, |  |

where h, g, u, m, ℓ h,g,u,m,\ell are real parameters, verifying condition

 | g ​ m − h ​ ℓ ≠ 0. gm-h\ell\neq 0. |  |

For these systems, computations show that

 | μ 0 = \displaystyle\mu_{0}= | 0, \displaystyle 0, |  |

 | μ 1 = \displaystyle\mu_{1}= | 4 ​ ( h ​ ℓ − g ​ m) 2 ​ ( 1 + u 2) ​ x, \displaystyle 4(h\ell-gm)^{2}(1+u^{2})x, |  |

 | η = \displaystyle\eta= | 4 ​ h 2 ​ [( g + 2 ​ m) 2 − 8 ​ h ​ ℓ], \displaystyle 4h^{2}\left[(g+2m)^{2}-8h\ell\right], |  |

 | M ~ = \displaystyle\widetilde{M}= | − 8 ​ [( ( g + 2 ​ m) 2 − 6 ​ h ​ ℓ) ​ x 2 − 2 ​ h ​ ( g + 2 ​ m) ​ x ​ y + 4 ​ h 2 ​ y 2], \displaystyle-8[\left((g+2m)^{2}-6h\ell\right)x^{2}-2h(g+2m)xy+4h^{2}y^{2}], |  |

 | κ = \displaystyle\kappa= | 128 ​ h 2 ​ ( g ​ m − h ​ ℓ). \displaystyle 128h^{2}(gm-h\ell). |  |

As in the proof of Proposition 2, from [6, Diagram 6.3], the previous invariants must verify

 | μ 0 = 0, μ 1 ≠ 0, η = 0, M ~ ≠ 0, κ = 0, \mu_{0}=0,\quad\mu_{1}\neq 0,\quad\eta=0,\quad\widetilde{M}\neq 0,\quad\kappa=0, |  |

respectively. So, by considering h = 0 h=0 at systems ( 10) we have systems

 |  | x ′ = − 2 ​ g ​ u ​ x + g ⁡ ( u 2 + 1) ​ y + g ​ x 2, \displaystyle x^{\prime}=-2gux+g(u^{2}+1)y+gx^{2}, |  | (11) |

 |  | y ′ = 2 ​ ( m − ℓ ​ u) ​ x + ℓ ⁡ ( u 2 + 1) ​ y + ℓ ​ x 2 − 2 ​ m ​ x ​ y, \displaystyle y^{\prime}=2(m-\ell u)x+\ell(u^{2}+1)y+\ell x^{2}-2mxy, |  |

where g, u, m, ℓ g,u,m,\ell are real parameters, verifying condition

 | g ​ m ≠ 0 gm\neq 0 |  | (12) |

and, for systems ( 11),

 |  | μ 0 = 0, \displaystyle\mu_{0}=0, |  |

 |  | μ 1 = 4 ​ g 2 ​ m 2 ​ ( 1 + u 2) ​ x, \displaystyle\mu_{1}=4g^{2}m^{2}(1+u^{2})x, |  |

 |  | η = 0, \displaystyle\eta=0, |  |

 |  | M ~ = − 8 ​ ( g + 2 ​ m) 2 ​ x 2, \displaystyle\widetilde{M}=-8(g+2m)^{2}x^{2}, |  |

 |  | κ = 0. \displaystyle\kappa=0. |  |

Since m ≠ 0 m\neq 0 (due to ( 12)), we perform the change

 | ( x, y, t) → ( x, y, t / m), (x,y,t)\rightarrow(x,y,t/m), |  |

and we get systems

 |  | x ′ = − 2 ​ g m ​ u ​ x + g m ​ ( u 2 + 1) ​ y + g m ​ x 2, \displaystyle x^{\prime}=-2\frac{g}{m}ux+\frac{g}{m}(u^{2}+1)y+\frac{g}{m}x^{2}, |  |

 |  | y ′ = 2 ​ ( 1 − ℓ m ​ u) ​ x + ℓ m ​ ( u 2 + 1) ​ y + ℓ m ​ x 2 − 2 ​ x ​ y. \displaystyle y^{\prime}=2\left(1-\frac{\ell}{m}u\right)x+\frac{\ell}{m}(u^{2}+1)y+\frac{\ell}{m}x^{2}-2xy. |  |

By renaming

 | g m → g, ℓ m → ℓ, \frac{g}{m}\rightarrow g,\quad\frac{\ell}{m}\rightarrow\ell, |  |

we obtain systems ( 11) with m = 1 m=1, i.e., we arrive at normal form ( 9), in which g ≠ 0 g\neq 0 due to ( 12). Indeed, by considering the change

 | ( x, y, t) → ( − x, y, − t), (x,y,t)\rightarrow(-x,y,-t), |  |

we obtain systems

 |  | x ′ = 2 ​ g ​ u ​ x + g ⁡ ( 1 + u 2) ​ y + g ​ x 2, \displaystyle x^{\prime}=2gux+g(1+u^{2})y+gx^{2}, |  |

 |  | y ′ = − 2 ​ ( − 1 + ℓ ​ u) ​ x − ℓ ⁡ ( 1 + u 2) ​ y − ℓ ​ x 2 − 2 ​ x ​ y, \displaystyle y^{\prime}=-2(-1+\ell u)x-\ell(1+u^{2})y-\ell x^{2}-2xy, |  |

i.e. ( u, ℓ, g) → ( − u, − ℓ, g) (u,\ell,g)\rightarrow(-u,-\ell,g), so one can consider u ∈ ℝ + ∪ { 0 } u\in\mathbb{R}^{+}\cup\{0\}. ∎

In the next result we prove the existence of invariant algebraic curves (straight lines and parabolas) under certain conditions for systems ( 9).

###### Lemma 3.

Systems ( 9) possess the following invariant algebraic curves if and only if the corresponding condition is satisfied:

1. (i)

{ y − 1 = 0 } ⇔ ℓ = 0 \{y-1=0\}\Leftrightarrow\ell=0;

2. (ii)

{ ℓ ​ x 2 − 2 ​ ℓ ​ u ​ x + 2 ​ u ℓ ​ u 2 + ℓ − 2 ​ u + y = 0 } ⇔ g = ℓ ​ u 2 + ℓ − 2 ​ u 2 ​ u \left\{\dfrac{\ell x^{2}-2\ell ux+2u}{\ell u^{2}+\ell-2u}+y=0\right\}\Leftrightarrow g=\dfrac{\ell u^{2}+\ell-2u}{2u};

3. (iii)

{ ( g + 1) ​ x 2 + 1 g + y = 0 } ⇔ ℓ = u = 0 \left\{\dfrac{(g+1)x^{2}+1}{g}+y=0\right\}\Leftrightarrow\ell=u=0.

###### Proof.

We consider the algebraic curves

 | f 1 ​ ( x, y) \displaystyle f_{1}(x,y) | ≡ y − 1 = 0, \displaystyle\equiv y-1=0, |  |

 | f 2 ​ ( x, y) \displaystyle f_{2}(x,y) | ≡ ℓ ​ x 2 − 2 ​ ℓ ​ u ​ x + 2 ​ u ℓ ​ u 2 + ℓ − 2 ​ u + y = 0, \displaystyle\equiv\dfrac{\ell x^{2}-2\ell ux+2u}{\ell u^{2}+\ell-2u}+y=0, |  |

 | f 3 ​ ( x, y) \displaystyle f_{3}(x,y) | ≡ ( g + 1) ​ x 2 + 1 g + y = 0, \displaystyle\equiv\dfrac{(g+1)x^{2}+1}{g}+y=0, |  |

and we show that the polynomials

 | K 1 ​ ( x, y) \displaystyle K_{1}(x,y) | = − 2 ​ x, \displaystyle=-2x, |  |

 | K 2 ​ ( x, y) \displaystyle K_{2}(x,y) | = x ⁡ ( ℓ ​ u 2 + ℓ − 2 ​ u) u, \displaystyle=\frac{x\left(\ell u^{2}+\ell-2u\right)}{u}, |  |

 | K 3 ​ ( x, y) \displaystyle K_{3}(x,y) | = 2 ​ g ​ x, \displaystyle=2gx, |  |

are the cofactors of f 1 = 0 f_{1}=0, f 2 = 0 f_{2}=0, and f 3 = 0 f_{3}=0, respectively, after restricting systems ( 9) to the respective conditions. ∎

The bifurcation diagram of systems ( 9) is studied in Sec. 3.2.

###### Proposition 4.

Every nondegenerate quadratic system possessing one triple real finite singular point plus either an infinite nilpotent elliptic–saddle or an infinite nilpotent saddle, can be brought via affine transformations and time rescaling to the following normal form

 |  | x ′ = g ​ y + g ​ x 2, \displaystyle x^{\prime}=gy+gx^{2}, |  | (13) |

 |  | y ′ = ℓ ​ y + 2 ​ x ​ y + ℓ ​ x 2, \displaystyle y^{\prime}=\ell y+2xy+\ell x^{2}, |  |

where g ∈ ℝ ∖ { 0 } g\in\mathbb{R}\setminus\{0\} and ℓ ∈ ℝ + ∪ { 0 } \ell\in\mathbb{R}^{+}\cup\{0\} are parameters, describing family 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) \bf{Q}{{\widehat{ES}(C)}}.

###### Proof.

In fact, from [6, Table 6.1] we get the so called canonical form 13, obtained by using affine transformations and time rescaling (see systems ( 14)), which describes quadratic systems possessing one real triple finite singular point and one infinite singular point of multiplicity two (formed by the coalescence of one finite and one infinite elemental singular points).

 |  | x ′ = g ​ y + g ​ x 2 + 2 ​ h ​ x ​ y, \displaystyle x^{\prime}=gy+gx^{2}+2hxy, |  | (14) |

 |  | y ′ = ℓ ​ y + ℓ ​ x 2 + 2 ​ m ​ x ​ y, \displaystyle y^{\prime}=\ell y+\ell x^{2}+2mxy, |  |

where g, h, ℓ, m g,h,\ell,m are real parameters, verifying condition

 | g ​ m − ℓ ​ h ≠ 0. gm-\ell h\neq 0. |  |

For these systems, computations show that

 | μ 0 = \displaystyle\mu_{0}= | 0, \displaystyle 0, |  |

 | μ 1 = \displaystyle\mu_{1}= | 4 ​ ( h ​ ℓ − g ​ m) 2 ​ x, \displaystyle 4(h\ell-gm)^{2}x, |  |

 | η = \displaystyle\eta= | 4 ​ h 2 ​ [8 ​ h ​ ℓ + ( g − 2 ​ m) 2], \displaystyle 4h^{2}\left[8h\ell+(g-2m)^{2}\right], |  |

 | M ~ = \displaystyle\widetilde{M}= | − 8 ​ [( ( g − 2 ​ m) 2 − 6 ​ h ​ ℓ) ​ x 2 − 2 ​ h ​ ( g − 2 ​ m) ​ x ​ y + 4 ​ h 2 ​ y 2], \displaystyle-8\left[\left((g-2m)^{2}-6h\ell\right)x^{2}-2h(g-2m)xy+4h^{2}y^{2}\right], |  |

 | κ = \displaystyle\kappa= | 128 ​ h 2 ​ ( h ​ ℓ − g ​ m). \displaystyle 128h^{2}(h\ell-gm). |  |

As in the proof of Propositions 2 and 3, from [6, Diagram 6.3], the previous invariants must verify

 | μ 0 = 0, μ 1 ≠ 0, η = 0, M ~ ≠ 0, κ = 0, \mu_{0}=0,\quad\mu_{1}\neq 0,\quad\eta=0,\quad\widetilde{M}\neq 0,\quad\kappa=0, |  |

respectively. So, by considering h = 0 h=0 at systems ( 14) we have systems

 |  | x ′ = g ​ y + g ​ x 2, \displaystyle x^{\prime}=gy+gx^{2}, |  | (15) |

 |  | y ′ = ℓ ​ y + ℓ ​ x 2 + 2 ​ m ​ x ​ y, \displaystyle y^{\prime}=\ell y+\ell x^{2}+2mxy, |  |

where g, ℓ, m g,\ell,m are real parameters, verifying condition

 | g ​ m ≠ 0 gm\neq 0 |  | (16) |

and, for systems ( 15),

 |  | μ 0 = 0, \displaystyle\mu_{0}=0, |  |

 |  | μ 1 = 4 ​ g 2 ​ m 2 ​ x, \displaystyle\mu_{1}=4g^{2}m^{2}x, |  |

 |  | η = 0, \displaystyle\eta=0, |  |

 |  | M ~ = − 8 ​ ( g − 2 ​ m) 2 ​ x 2, \displaystyle\widetilde{M}=-8(g-2m)^{2}x^{2}, |  |

 |  | κ = 0. \displaystyle\kappa=0. |  |

Since m ≠ 0 m\neq 0 (due to ( 16)), we perform the change

 | ( x, y, t) → ( x, y, t / m), (x,y,t)\rightarrow(x,y,t/m), |  |

and we get systems

 |  | x ′ = g m ​ y + g m ​ x 2, \displaystyle x^{\prime}=\frac{g}{m}y+\frac{g}{m}x^{2}, |  |

 |  | y ′ = ℓ m ​ y + ℓ m ​ x 2 + 2 ​ x ​ y. \displaystyle y^{\prime}=\frac{\ell}{m}y+\frac{\ell}{m}x^{2}+2xy. |  |

By renaming

 | g m → g, ℓ m → ℓ, \frac{g}{m}\rightarrow g,\quad\frac{\ell}{m}\rightarrow\ell, |  |

we obtain systems ( 15) with m = 1 m=1, i.e., we arrive at normal form ( 13), in which g ≠ 0 g\neq 0 due to ( 16). Indeed, by considering the change

 | ( x, y, t) → ( − x, y, − t), (x,y,t)\rightarrow(-x,y,-t), |  |

we obtain systems

 |  | x ′ = g ​ y + g ​ x 2, \displaystyle x^{\prime}=gy+gx^{2}, |  |

 |  | y ′ = − ℓ ​ y + 2 ​ x ​ y − ℓ ​ x 2, \displaystyle y^{\prime}=-\ell y+2xy-\ell x^{2}, |  |

i.e. ( g, ℓ) → ( g, − ℓ) (g,\ell)\rightarrow(g,-\ell), so one can consider ℓ ∈ ℝ + ∪ { 0 } \ell\in\mathbb{R}^{+}\cup\{0\}. ∎

In what follows we prove the existence of invariant algebraic curves (straight lines and parabolas) under certain conditions for family ( 13).

###### Lemma 4.

Family ( 13) possesses the following invariant algebraic curves if and only if the corresponding condition is satisfied:

1. (i)

{ y = 0 } ⇔ ℓ = 0 \{y=0\}\Leftrightarrow\ell=0;

2. (ii)

{ ( g − 1) ​ x 2 g + y = 0 } ⇔ ℓ = 0 \left\{\dfrac{(g-1)x^{2}}{g}+y=0\right\}\Leftrightarrow\ell=0.

###### Proof.

We consider the algebraic curves

 | f 1 ​ ( x, y) \displaystyle f_{1}(x,y) | ≡ y = 0, \displaystyle\equiv y=0, |  |

 | f 2 ​ ( x, y) \displaystyle f_{2}(x,y) | ≡ ( g − 1) ​ x 2 g + y = 0, \displaystyle\equiv\frac{(g-1)x^{2}}{g}+y=0, |  |

and we show that the polynomials

 | K 1 ​ ( x, y) \displaystyle K_{1}(x,y) | = 2 ​ x, \displaystyle=2x, |  |

 | K 2 ​ ( x, y) \displaystyle K_{2}(x,y) | = 2 ​ g ​ x, \displaystyle=2gx, |  |

are the cofactors of f 1 = 0 f_{1}=0 and f 2 = 0 f_{2}=0, respectively, after restricting systems ( 13) to the respective conditions. ∎

In Sec. 3.3 we present the study of the bifurcation diagram of normal form ( 13).

## 3 The bifurcation diagrams from class 𝐐 ​ 𝐄𝐒 ^ \bf{Q}{\widehat{ES}}

In this paper we intend to perform the study of three bifurcation diagrams. And to achieve this goal we shall use algebraic and topological invariants. The algebraic invariants make results independent of specific normal forms. They also distinguish the phase portraits as the topological invariants also do. In this paper we use the concepts of algebraic invariant and T–comitant as formulated by the Sibirsky’s School for differential equations. For a quick summary of the general theory of these polynomial invariants and their relevance in working with polynomial differential systems we recommend Sec. 7 of [4].

It is worth mentioning that from Sec. 7 of [7] and [20] we get formulas which give the bifurcation algebraic sets of singularities in ℝ 12 \mathbb{R}^{12}, produced by changes that may occur in the local nature of finite singularities. Also, from [19] we get equivalent formulas for the infinite singular points. All of these formulas were lately compiled and improved in the book [6]. In the next three subsections we shall use several results of such a book.

### 3.1 The bifurcation diagram of family 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) \bf{Q}{{\widehat{ES}(A)}}

In this section we present the study of the bifurcation diagram of family 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) \bf{Q}{{\widehat{ES}(A)}}, given by systems ( 5).

Initially remember that family ( 5) is described by the parameters c ∈ ℝ ∖ { 0 } c\in\mathbb{R}\setminus\{0\}, f ∈ ℝ + ∪ { 0 } f\in\mathbb{R}^{+}\cup\{0\}, and e ∈ ℝ e\in\mathbb{R}. So we shall consider the bifurcation diagram formed by planes c = c 0 ≠ 0 c=c_{0}\neq 0 and, in each plane, the Cartesian coordinates are ( e, f) (e,f) with f ≥ 0 f\geq 0.

Also, from [6, Lemma 5.2] we calculate

 | μ 0 = 0, μ 1 = − 4 ​ c ​ x. \mu_{0}=0,\quad\mu_{1}=-4cx. |  |

The condition c ≠ 0 c\neq 0 implies μ 1 ≠ 0 \mu_{1}\neq 0 and, therefore, we have nondegenerate systems.

Now we present the value of the algebraic invariants and T–comitants (with respect to family ( 5)) which are relevant in our study.

Bifurcation surfaces due to multiplicities of singularities

( 𝒮 2) (\mathcal{S}_{2}) This is the bifurcation surface in ℝ 3 \mathbb{R}^{3} due to multiplicity of finite singular points, formed by the coalescence of at least two finite singular points. For family ( 5), according to [6, Table 5.1] we calculate

 | 𝐃 = \displaystyle\mathbf{D}\!= | − 192 ​ ( c − f) 2 ​ ( c + f) 2, \displaystyle-192(c-f)^{2}(c+f)^{2}, |  |

and we define the surface

 | ( 𝒮 2): \displaystyle(\mathcal{S}_{2})\!: | ( c − f) ​ ( c + f) = 0, \displaystyle(c-f)(c+f)=0, |  |

which is clear formed by two planes in ℝ 3 \mathbb{R}^{3}. Additionally as the comitant

 | 𝐏𝐑 | c = ± f = 768 ​ f 4 ​ x 4 ​ y 2 \mathbf{P}\mathbf{R}\big|_{c=\pm f}=768f^{4}x^{4}y^{2} |  |

is nonzero, from [6, Table 5.1] we conclude that along surface ( 𝒮 2) (\mathcal{S}_{2}) we have one double and one simple real finite singular points.

( 𝒮 5 {\cal S}_{5}) This is the bifurcation surface due to multiplicity of infinite singular points. Previously we mentioned that an infinite elliptic–saddle is a triple infinite singular point formed by the coalescence of one finite singular point with two infinite ones. So, for family ( 5) we have at most two pairs of infinite singular points. According to [6, Lemma 5.5], for this family we calculate

 | η = 0, M ~ = − 8 ​ ( 2 + c) 2 ​ x 2, C 2 = x 2 ​ [e ​ x − ( 2 + c) ​ y], \eta=0,\quad\widetilde{M}=-8(2+c)^{2}x^{2},\quad C_{2}=x^{2}\left[ex-(2+c)y\right], |  |

and we observe that along surface (in fact a plane in ℝ 3 \mathbb{R}^{3})

 | ( 𝒮 5): \displaystyle(\mathcal{S}_{5})\!: | c + 2 = 0, \displaystyle c+2=0, |  |

we have a coalescence of infinite singular points. In addition, due to the mentioned result, on the plane c = − 2 c=-2 all the phase portraits corresponding to e = 0 e=0 have the line at infinity filled up with singular points.

The surface of C ∞ C^{\infty} bifurcation points due to a strong saddle or a strong focus changing the sign of their traces (weak saddle or weak focus)

( 𝒮 3 {\cal S}_{3}) This is the bifurcation surface due to weak finite singularities, which occurs when the trace of a finite singular point is zero. According to [20], for family ( 5) we calculate

 | 𝒯 4 = \displaystyle\mathcal{T}_{4}= | 𝒯 3 = 𝒯 2 = 𝒯 1 = 0, \displaystyle\mathcal{T}_{3}=\mathcal{T}_{2}=\mathcal{T}_{1}=0, |  |

 | σ = \displaystyle\sigma= | c ⁡ ( c − 1) + e + f − 2 ​ c ​ ( c − 1) ​ x c, \displaystyle\dfrac{c(c-1)+e+f-2c(c-1)x}{c}, |  |

then due to the results on the mentioned paper, in the case in which σ \sigma is generically nonzero, the family under consideration could possess one and only one weak singularity. Moreover as

 | ℱ 1 = \displaystyle\mathcal{F}_{1}= | − 2 ​ [3 ​ e + ( 2 + c) ​ f], ℋ = 0, \displaystyle-2\left[3e+(2+c)f\right],\qquad\mathcal{H}=0, |  |

 | ℬ 1 = \displaystyle\mathcal{B}_{1}= | 2 ​ [c 2 ​ ( c − 1 2) − ( e + f) 2] ​ ( e + c ​ f) c, \displaystyle\dfrac{2\left[c^{2}(c-1^{2})-(e+f)^{2}\right](e+cf)}{c}, |  |

 | ℬ 2 = \displaystyle\mathcal{B}_{2}= | − 2 ​ ( c − 1) 2 ​ [c 4 − 2 ​ c 3 + c 2 − 2 ​ c ​ f ​ ( e + f)] + 2 ​ ( c − 1) 2 ​ ( e + f) ​ ( 3 ​ e + f) c, \displaystyle\dfrac{-2(c-1)^{2}\left[c^{4}-2c^{3}+c^{2}-2cf(e+f)\right]+2(c-1)^{2}(e+f)(3e+f)}{c}, |  |

assuming ℱ 1 ≠ 0 \mathcal{F}_{1}\neq 0, for family ( 5) we can obtain one weak singularity ( s ( 1) s^{(1)} or f ( 1) f^{(1)}) along the surface given by ℬ 1 = 0 \mathcal{B}_{1}=0, i.e.

 | ( 𝒮 3): \displaystyle({\cal S}_{3})\!: | [c 2 ​ ( c − 1 2) − ( e + f) 2] ​ ( e + c ​ f) c = 0. \displaystyle\dfrac{\left[c^{2}(c-1^{2})-(e+f)^{2}\right](e+cf)}{c}=0. |  |

We highlight that this bifurcation can produce a topological change if the weak point is a focus or just a C ∞ C^{\infty} change if it is a saddle, except when this bifurcation coincides with a loop bifurcation associated with the same saddle, in which case, the change may also be topological (see for instance [14, p. 50]).

###### Remark 2.

1. 1.

We just saw that in order to define surface ( 𝒮 3 {\cal S}_{3}) we considered σ ≠ 0 \sigma\neq 0 and ℱ 1 ≠ 0 \mathcal{F}_{1}\neq 0. However, according to [20, item ( e) (e)], when σ ≠ 0 \sigma\neq 0 and ℱ 1 = 0 \mathcal{F}_{1}=0 we can have either an integrable saddle or a center. Later we shall analyze when we have an integrable saddle. Now we investigate when we have a finite singular point which is a center. In fact, as we already have ℋ = 0 \mathcal{H}=0, from the mentioned paper we solve ℱ 1 = ℬ 1 = 0 \mathcal{F}_{1}=\mathcal{B}_{1}=0 (together with σ ≠ 0 \sigma\neq 0 and f ≥ 0 f\geq 0), and we obtain two solutions

 | { e = 0, f = 0 }, { e = − c ⁡ ( c + 2), f = 3 ​ c }. \{e=0,f=0\},\ \{e=-c(c+2),f=3c\}. |  | (17) |

Also, when we compute ℬ 2 \mathcal{B}_{2} along these two solutions we obtain, in each case, − 8 ​ ( c − 1) 4 ​ c -8(c-1)^{4}c, which is generically negative if c > 0 c>0. Note that we must have c ≠ 1 c\neq 1, because each one of the two solutions together with c = 1 c=1 imply σ = 0 \sigma=0.
Therefore, from [20, item ( e 4 e_{4})– β \beta], this study shows that for c > 0 c>0 we shall always find a center type singular point when we have ( 17).

2. 2.

We observe that, independently of x x, for c ≠ 0 c\neq 0, we have σ = 0 \sigma=0 if and only if f = − e f=-e and c = 1 c=1. Under these conditions, we have that μ 0 = 0 \mu_{0}=0, 𝐃 = − 192 ​ ( f 2 − 1) 2 \mathbf{D}=-192\left(f^{2}-1\right)^{2}, and 𝐑 = 48 ​ x 2 \mathbf{R}=48x^{2}. So, according to [20, item ( f 3) (f_{3})] we have three finite singular points, being two integrable saddles and one center. In other words, when c = 1 c=1, during the study of the curve f = − e f=-e we shall always obtain a phase portrait containing two integrable saddles and one center type singular point.

The surface of C ∞ C^{\infty} bifurcation due to a node becoming a focus

( 𝒮 6 {\cal S}_{6}) This surface contains the points of the parameter space where a finite node of the systems turns into a focus. This surface is a C ∞ C^{\infty} but not a topological bifurcation surface. In fact, when we only cross the surface ( 𝒮 6 {\cal S}_{6}) in the bifurcation diagram, the topological phase portraits do not change. However, this surface is relevant for isolating the regions where a limit cycle surrounding an antisaddle cannot exist. According to [6, Table 6.2] we calculate

 | μ 0 = \displaystyle\mu_{0}= | 0, 𝐃 = − 192 ​ ( c 2 − f 2) 2, 𝐑 = 48 ​ c 2 ​ x 2, \displaystyle 0,\quad\mathbf{D}=-192(c^{2}-f^{2})^{2},\quad\mathbf{R}=48c^{2}x^{2}, |  |

 | K ~ = \displaystyle\widetilde{K}= | − 4 ​ c ​ x 2, G 9 = 0, \displaystyle-4cx^{2},\quad G_{9}=0, |  |

and for the mentioned table we conclude that the invariant W 7 W_{7} is responsible for describing the node–focus bifurcation. We compute this invariant polynomial and we define surface ( 𝒮 6 {\cal S}_{6}) by the zero set of

 |  | 1 c 4 [2 c 3 − e 2 − 2 c e f − c f 2 ( 2 + c)] × \displaystyle\dfrac{1}{c^{4}}\left[2c^{3}-e^{2}-2cef-cf^{2}(2+c)\right]\times |  |

 |  | [2 c 3 + c 4 + c 2 ( 1 + 2 e − 2 f) − 2 c ( e + f) + ( e + f) 2] × \displaystyle\left[2c^{3}+c^{4}+c^{2}(1+2e-2f)-2c(e+f)+(e+f)^{2}\right]\times |  |

 |  | [2 ​ c 3 + c 4 + c 2 ​ ( 1 − 2 ​ e + 2 ​ f) + 2 ​ c ​ ( e + f) + ( e + f) 2] = 0. \displaystyle\left[2c^{3}+c^{4}+c^{2}(1-2e+2f)+2c(e+f)+(e+f)^{2}\right]=0. |  |

Bifurcation surface in ℝ 3 \mathbb{R}^{3} due to the presence of invariant straight lines

( 𝒮 4 {\cal S}_{4}) This surface contains the points of the parameter space in which there appear invariant straight lines (see Lemma 1). This surface is split into some regions. Depending on these regions, the straight line may contain connections of separatrices from different points or not. So, in some cases, it may imply a topological bifurcation and, in others, just a C ∞ C^{\infty} bifurcation. According to [6], the equation of this surface is given by the invariant B 1 B_{1}. It is worth mentioning that B 1 = 0 B_{1}=0 is only a necessary condition for the existence of an invariant straight line, but it is not sufficient (see Corollary 4.6 from [18]), i.e. we may find some component of B 1 = 0 B_{1}=0 that does not represent an invariant straight line. For family ( 5) we compute the invariant B 1 B_{1} and we define the surface

 | ( 𝒮 4): \displaystyle({\cal S}_{4})\!: | e ⁡ [c ⁡ ( 2 + c − f) − 2 ​ ( e + f)] ​ [c ⁡ ( 2 + c + f) + 2 ​ ( e + f)] = 0, \displaystyle e\left[c(2+c-f)-2(e+f)\right]\left[c(2+c+f)+2(e+f)\right]=0, |  |

which is the union of one plane together with two quadric surfaces.

Bifurcation surface in ℝ 3 \mathbb{R}^{3} due to the presence of invariant parabolas

( 𝒮 8 {\cal S}_{8}) This surface contains the points of the parameter space in which there appear invariant parabolas. As in the case of surface ( 𝒮 4 {\cal S}_{4}), this surface is split into some regions. Depending on these regions, the parabola may contain connections of separatrices from different points or not. So, in some cases, it may imply a topological bifurcation and, in others, just a C ∞ C^{\infty} bifurcation. According to the conditions stated in Lemma 2 we define this surface by

 | ( 𝒮 8): \displaystyle({\cal S}_{8})\!: | − ( e + f + c ​ f) ​ [( c + 2 ​ c 2) 2 − ( 2 ​ e + f) 2] = 0. \displaystyle-(e+f+cf)\left[(c+2c^{2})^{2}-(2e+f)^{2}\right]=0. |  |

We suggest the reader to plot surface ( 𝒮 8) ({\cal S}_{8}) in order to visualize a three–dimensional picture.

Bifurcation surface in ℝ 3 \mathbb{R}^{3} due to the infinite elliptic–saddle

( 𝒮 0 {\cal S}_{0}) Along the plane c = − 1 c=-1 the corresponding phase portraits possess an infinite singularity of the type ( 1 2) ^ ​ E − H \widehat{\!{1\choose 2}\!\!}\ E-H, which is the transition between the singularities ( 1 2) ^ ​ P ​ E ​ P − H \widehat{\!{1\choose 2}\!\!}\ PEP-H and ( 1 2) ^ ​ E − P ​ H ​ P \widehat{\!{1\choose 2}\!\!}\ E-PHP. Such a plane is needed for the coherence of the bifurcation diagram. In fact, according to [6] we know that the comitant N ~ \widetilde{N} is related to this phenomenon. Moreover, N ~ \widetilde{N} “behaves like” 𝒯 4 {\cal{T}}_{4}, in the sense that N ~ = 0 \widetilde{N}=0 splits the parameter space into two distinct canonical regions and the phase portrait over N ~ = 0 \widetilde{N}=0 is topologically equivalent to the phase portrait in one of its sides and topologically distinct to the one in the other side (see this phenomenon in [9]). In such a way we need to determine the points on the parameter space that verifies the equation N ~ = 0 \widetilde{N}=0. Calculations yield

 | N ~ = − 4 ​ ( c + 1) ​ x 2. \widetilde{N}=-4(c+1)x^{2}. |  |

It is clear that the plane c + 1 = 0 c+1=0 verifies this equation. Therefore we define surface ( 𝒮 0 {\cal S}_{0}) by the equation

 | ( 𝒮 0): c + 1 = 0. ({\cal S}_{0})\!:c+1=0. |  |

The bifurcation surfaces listed previously are all algebraic and they, except ( 𝒮 4) ({\cal S}_{4}) and ( 𝒮 8) ({\cal S}_{8}), are the bifurcation surfaces of singularities of family ( 5) in the parameter space. We shall detect other bifurcation surface not necessarily algebraic. In such a nonalgebraic surface the family has global connection of separatrices different from those given by ( 𝒮 4) ({\cal S}_{4}) and ( 𝒮 8) ({\cal S}_{8}). The equation of this bifurcation surface can only be determined approximately by means of numerical tools. Using arguments of continuity in the phase portraits we can prove the existence of this component not necessarily algebraic in the part where it appears, and we can check it numerically. We shall name it surface ( 𝒮 7) ({\cal S}_{7}).

###### Remark 3.

Even though we can draw pictures of the algebraic bifurcation surfaces in ℝ 3 \mathbb{R}^{3}, it is pointless to see a single image of all these bifurcation surfaces together. As we shall see later, the partition of the parameter space obtained from these bifurcation surfaces together with the nonalgebraic one has 1274 parts.

Due to the last remark and, as we already said before, we shall foliate the three–dimensional bifurcation diagram in ℝ 3 \mathbb{R}^{3} by planes c = c 0 ≠ 0 c=c_{0}\neq 0, with c 0 c_{0} constant and we shall give pictures of the resulting bifurcation diagram on these planar sections in which the Cartesian coordinates are ( e, f) (e,f), where the horizontal line is the e e –axis and f ≥ 0 f\geq 0.

As the final bifurcation diagram is quite complex, it is useful to introduce colors which will be used to refer to the bifurcation surfaces:

1. (a)

surface ( 𝒮 2 {\cal S}_{2}) is drawn in green (coalescence of finite singular points);

2. (b)

surface ( 𝒮 3 {\cal S}_{3}) is drawn in yellow (when the trace of a singular point becomes zero). We draw it as a continuous curve if the singular point is a focus or as a dashed curve if it is a saddle;

3. (c)

surface ( 𝒮 4 {\cal S}_{4}) is drawn in purple (presence of at least one invariant straight line). We draw it as a continuous curve if it implies a topological change or as a dashed curve otherwise;

4. (d)

surface ( 𝒮 6 {\cal S}_{6}) is drawn in black (an antisaddle is on the edge of turning from a node to a focus or vice versa). In the papers [4, 13, 14, 9] the authors draw surface ( 𝒮 6 {\cal S}_{6}) as a continous curve. However, as it does not imply a topological change, we decided, from now on, to draw it as a dashed line.

5. (e)

nonalgebraic surface ( 𝒮 7 {\cal S}_{7}) is also drawn in purple (connections of separatrices); and

6. (f)

surface ( 𝒮 8 {\cal S}_{8}) is drawn in cyan (presence of an invariant parabola). We draw it as a continuous curve if it implies a topological change or as a dashed curve otherwise.

###### Remark 4.

Regarding the colors we use to draw the bifurcation surfaces, it is important to mention that:

- •

Here we use the same color for drawing ( 𝒮 4 {\cal S}_{4}) and ( 𝒮 7 {\cal S}_{7}), in order to follow the same pattern used in [14, 9] for instance.

- •

In the mentioned papers surface ( 𝒮 5 {\cal S}_{5}) was drawn in red (when two infinite singular points coalesce). However, for family ( 5) we are considering we saw that surface ( 𝒮 5 {\cal S}_{5}) defines the entire plane c = − 2 c=-2. So, in order to avoid the utilization of several colors in the same plane, here we decided to follow the pattern used in [8] and not to draw this entire plane in red color.

- •

In [9] the bifurcation line related to a presence of an infinite singular point of type ( 1 2) ^ ​ E − H \widehat{\!{1\choose 2}\!\!}\ E-H was drawing using brown color. However, for family ( 5) in the current paper we saw that surface ( 𝒮 0 {\cal S}_{0}) defines the entire plane c = − 1 c=-1. Then, by the same reason explained in the previous item, here we decided not to draw this plane in brown color.

Having defined the bifurcation surfaces related to the study of the bifurcation diagram of family ( 5) we are now interested in studying the geometrical behavior of all of these algebraic surfaces for c ≠ 0 c\neq 0, that is, their singularities, their intersection points and their extrema (maxima and minima) with respect to the coordinate c c (in other words, we have the “tangencies” with planes OPEN c = c 0 ≠ 0) c=c_{0}\neq 0). Since this study requires a lot of computations which would take a very large number of pages to present all the details (as in [14, 9] for instance), in order to be more succinct here we are using the same algorithm (written in software Mathematica) already used in [8]. Such an algorithm, applied to family ( 5), is available for free download through the link http://mat.uab.cat/~artes/articles/qvfES/qvfES-A.nb (some previous knowledge of Mathematica is recommended for using this algorithm). In order to avoid repetitions, we recommend paper [8] for more details on the notation used in this study and on the description and meaning of the so–called lists of objects.

###### Remark 5.

In the papers [4, 13, 14, 8, 9] in which families of quadratic systems were studied, the corresponding bifurcation diagram was done in an appropriate projective space, in which it was possible to analyze the slice at infinity and also to verify coherence in continuity (modulo islands) between the phase portraits on the infinite slice and phase portraits on the “highest” slice in the affine part. In those studies, with this approach the authors had the guarantee that they did not loose any phase portrait when one goes from the affine part towards the infinity. Due to the nature of normal form ( 5), it is not possible to perform an analogous study for family 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) \bf{Q}{{\widehat{ES}(A)}}. The next result presents all the algebraic values of the parameter c c corresponding to singular slices (or planes) in the bifurcation diagram and the greatest singular value of c c is c = 2 c=2. In addition, in Proposition 5 we have that the first algebraic slice is given by c = 5 c=5. So, taking into consideration the approach used in previous papers, we may say that in our study there is a possibility of finding a phase portrait in an slice corresponding to a value c > 5 c>5, which would be topologically distinct to those ones obtained in the study of slices c ≤ 5 c\leq 5. However, we believe that in case there exists such a different phase portrait in an slice c > 5 c>5, this phase portrait would belong to a region bordered by nonalgebraic bifurcations due to connections of separatrices, since our study of the geometrical behavior of all algebraic surfaces showed that we do not have to consider any slice c > 5 c>5.

Its proof follows from the study done with the help of the mentioned algorithm.

###### Lemma 5.

Consider the algebraic bifurcation surfaces defined before. The study of their singularities, their intersection points, and their tangencies with planes c = c 0 ≠ 0 c=c_{0}\neq 0 provides the following set of 12 singular values of the parameter c c:

 | { 2, 3, 1, 1 3, 1 2, − 1 2, − 1 3, − 2 3, − 1, − 3 2, − 3, − 2 }. \left\{2,\sqrt{3},1,\frac{1}{\sqrt{3}},\frac{1}{2},-\frac{1}{2},-\frac{1}{\sqrt{3}},-\frac{2}{3},-1,-\frac{3}{2},-\sqrt{3},-2\right\}\!. |  |

Note that, when we obtained the differential equations that define family ( 5), we proved that due to the symmetry on the bifurcation diagram, it is enough to consider the parameter f ≥ 0 f\geq 0. So, apart from the previous study we have also to consider all the possible intersections of algebraic bifurcation curves that occur along f = 0 f=0, since from such intersection points some open regions on f > 0 f>0 could arise (or disappear). In the following result we present the values of the parameter c c in which there exist intersection of bifurcation surfaces along f = 0 f=0. The proof is done on the mentioned Mathematica file and, as it is quite trivial, it is not presented here.

###### Lemma 6.

Consider the algebraic bifurcation surfaces defined before. When restricted to f = 0 f=0, such surfaces have intersection points on the planes corresponding to the following 13 values of the parameter c c:

 | { 4, 3 + 2, 2, 1, 1 2, 2 − 3, 1 4, − 1 4, − 9 16, − 1, − 16 9, − 2, − 4 }. \left\{4,\sqrt{3}+2,2,1,\frac{1}{2},2-\sqrt{3},\frac{1}{4},-\frac{1}{4},-\frac{9}{16},-1,-\frac{16}{9},-2,-4\right\}\!. |  |

We shall consider the planes corresponding to these intersection points also as singular planes (in fact, the previous two lists have nonempty intersection). So we collect the values of the parameter c c obtained from Lemmas 5 and 6 and, in the next result we present the complete list of algebraic singular planes corresponding to values of the parameter c c.

###### Proposition 5.

The full set of needed algebraic singular slices in the bifurcation diagram of family ( 5) is formed by 20 elements which correspond to the values of c c in ( 18).

 | c 1 = 4, c 3 = 3 + 2, c 5 = 2, c 7 = 3, c 9 = 1, c 11 = 1 3, c 13 = 1 2, c 15 = 2 − 3, c 17 = 1 4, c 21 = − 1 4, c 23 = − 1 2, c 25 = − 9 16, c 27 = − 1 3, c 29 = − 2 3, c 31 = − 1, c 33 = − 3 2, c 35 = − 3, c 37 = − 16 9, c 39 = − 2, c 41 = − 4. \begin{gathered}c_{1}=4,\ c_{3}=\sqrt{3}+2,\ c_{5}=2,\ c_{7}=\sqrt{3},\ c_{9}=1,\ c_{11}=\frac{1}{\sqrt{3}},\ c_{13}=\frac{1}{2},\ c_{15}=2-\sqrt{3},\\ c_{17}=\frac{1}{4},\ c_{21}=-\frac{1}{4},\ c_{23}=-\frac{1}{2},\ c_{25}=-\frac{9}{16},\ c_{27}=-\frac{1}{\sqrt{3}},\ c_{29}=-\frac{2}{3},\ c_{31}=-1,\\ c_{33}=-\frac{3}{2},\ c_{35}=-\sqrt{3},\ c_{37}=-\frac{16}{9},\ c_{39}=-2,\ c_{41}=-4.\\ \end{gathered} |  | (18) |

The numeration in ( 18) is not consecutive since we reserve numbers for generic slices. We point out that we have not found nonalgebraic slices, as in [9], for instance.

In order to determine all the parts generated by the bifurcation surfaces from ( 𝒮 0) ({\cal S}_{0}) to ( 𝒮 8) ({\cal S}_{8}), we first draw the horizontal slices of the three–dimensional parameter space which correspond to the explicit values of c c obtained in Proposition 5. However, as it will be discussed later, the presence of nonalgebraic bifurcation surfaces will be detected and their behavior as we move from slice to slice will be approximately determined. We add to each interval of singular values of c c an intermediate value for which we represent the bifurcation diagram of singularities. The diagram will remain essentially unchanged in these open intervals except the parts affected by the bifurcation. All the 42 sufficient values of c c are shown in ( 19).

The values indexed by positive odd indices in ( 19) correspond to explicit values of c c for which there is a bifurcation in the behavior of the systems on the slices. Those indexed by even values are just intermediate points which are necessary to the coherence of the bifurcation diagram. Note that we skip index c 19 c_{19} since such an index would correspond to c = 0 c=0, in which family ( 5) is not defined.

We now begin the analysis of the bifurcation diagram by studying completely one generic slice and after by moving from slice to slice and explaining all the changes that occur. As an exact drawing of the curves produced by intersecting the surfaces with the slices gives us very small parts which are difficult to distinguish, and points of tangency are almost impossible to recognize, we have produced topologically equivalent figures where parts are enlarged and tangencies are easy to observe. From this reason, pictures corresponding to entire planes ( e, f) (e,f) are split into two parts, see for instance Fig. 9 and 10.

 | c 0 = 5 c 9 = 1 c 18 = 1 / 10 c 27 = − 1 / 3 c 36 = − 175 / 100 c 1 = 4 c 10 = 3 / 4 c 19 =? ​? ​? c 28 = − 62 / 100 c 37 = − 16 / 9 c 2 = 385 / 100 c 11 = 1 / 3 c 20 = − 1 / 10 c 29 = − 2 / 3 c 38 = − 19 / 10 c 3 = 3 + 2 c 12 = 55 / 100 c 21 = − 1 / 4 c 30 = − 85 / 100 c 39 = − 2 c 4 = 3 c 13 = 1 / 2 c 22 = − 35 / 100 c 31 = − 1 c 40 = − 3 c 5 = 2 c 14 = 38 / 100 c 23 = − 1 / 2 c 32 = − 125 / 100 c 41 = − 4 c 6 = 185 / 100 c 15 = 2 − 3 c 24 = − 53 / 100 c 33 = − 3 / 2 c 42 = − 5 c 7 = 3 c 16 = 26 / 100 c 25 = − 9 / 16 c 34 = − 16 / 10 c 8 = 14 / 10 c 17 = 1 / 4 c 26 = − 57 / 100 c 35 = − 3 \hskip-5.69054pt\begin{array}[]{llllll}c_{0}=5&c_{9}=1&c_{18}=1/10&c_{27}=-1/\sqrt{3}&c_{36}=-175/100\\ c_{1}=4&c_{10}=3/4&c_{19}=???&c_{28}=-62/100&c_{37}=-16/9\\ c_{2}=385/100&c_{11}=1/\sqrt{3}&c_{20}=-1/10&c_{29}=-2/3&c_{38}=-19/10\\ c_{3}=\sqrt{3}+2&c_{12}=55/100&c_{21}=-1/4&c_{30}=-85/100&c_{39}=-2\\ c_{4}=3&c_{13}=1/2&c_{22}=-35/100&c_{31}=-1&c_{40}=-3\\ c_{5}=2&c_{14}=38/100&c_{23}=-1/2&c_{32}=-125/100&c_{41}=-4\\ c_{6}=185/100&c_{15}=2-\sqrt{3}&c_{24}=-53/100&c_{33}=-3/2&c_{42}=-5\\ c_{7}=\sqrt{3}&c_{16}=26/100&c_{25}=-9/16&c_{34}=-16/10&\\ c_{8}=14/10&c_{17}=1/4&c_{26}=-57/100&c_{35}=-\sqrt{3}&\\ \end{array} |  | (19) |

The reader may find the exact pictures of the 20 singular slices (containing only the algebraic surfaces) described in ( 18) in a PDF file available at the link http://mat.uab.es/~artes/articles/qvfES/qvfES-A.pdf.

We now describe the labels used for each part of the bifurcation space. As we have mentioned in Remark 1, the subsets of dimensions 3, 2, 1 and 0, of the partition of the parameter space will be denoted respectively by V V, S S, L L, and P P for Volume, Surface, Line and Point, respectively. The surfaces are named using a number which corresponds to each bifurcation surface which is placed on the left side of the letter S S. To describe the portion of the surface we place an index. The curves that are intersection of surfaces are named by using their corresponding numbers on the left side of the letter L L, separated by a point. To describe the segment of the curve we place an index. Volumes and Points are simply indexed (since three or more surfaces may be involved in such an intersection).

We consider an example: surface ( 𝒮 2) ({\cal S}_{2}) splits into 42 different two–dimensional parts labeled from 2 ​ S 1 2S_{1} to 2 ​ S 42 2S_{42}, plus some one–dimensional arcs labeled as 2. i ​ L j 2.iL_{j} (where i i denotes the other surface intersected by ( 𝒮 2) ({\cal S}_{2}) and j j is a number), and some zero–dimensional parts. In order to simplify the labels in all figures we see V1 which stands for the T e X notation V 1 V_{1}. Analogously, 2S1 (respectively, 2.3L1) stands for 2 ​ S 1 2S_{1} (respectively, 2.3 ​ L 1 2.3L_{1}), see Fig. 9 and 10, for example.

In Fig. 6 and 7 we represent the generic slice of the parameter space when c = c 0 = 5 c=c_{0}=5, showing only the algebraic surfaces. We note that there are some dashed branches of surface ( 𝒮 3 {\cal{S}}_{3}) (in yellow), ( 𝒮 4 {\cal{S}}_{4}) (in purple), and ( 𝒮 8 {\cal{S}}_{8}) (in blue). This means the existence of a weak saddle, in the case of surface ( 𝒮 3 {\cal{S}}_{3}), the existence of an invariant straight line without separatrix connection, in the case of surface ( 𝒮 4 {\cal{S}}_{4}), and the existence of an invariant parabola without separatrix connection, in the case of surface ( 𝒮 8 {\cal{S}}_{8}); they do not mean a topological change in the phase portraits but a C ∞ C^{\infty} change. In the next figures we shall use the same representation for these characteristics of these three surfaces.

Figure 6: Piece of generic slice of the parameter space when c = 5 c=5 (only algebraic surfaces), see also Fig. 7 Figure 7: Continuation of Fig. 6

With the purpose to explain all the changes in the bifurcation diagram, we would have to present two versions of the picture of each slice: one of them without labels and the other with labels in each new part (as it was done, for instance, in [12] and [13]).

However, as the number of slices is considerably large (see equation ( 19) – 42 slices to be more precise) we would have to present 84 pictures, which would occupy a large number of pages. Then, we shall present only the labeled drawings (just the “important part” in each slice) containing the algebraic and nonalgebraic bifurcation surfaces. Along this study we prove the existence of such nonalgebraic surfaces and their necessity for the coherence of the bifurcation diagram.

###### Remark 6.

Wherever two parts of equal dimension d d are separated only by a part of dimension d − 1 d-1 of the black bifurcation surface ( 𝒮 6) ({\cal S}_{6}), their respective phase portraits are topologically equivalent since the only difference between them is that a finite antisaddle has turned into a focus without change of stability and without appearance of limit cycles. We denote such parts with different labels, but we do not give specific phase portraits in pictures attached to Theorems 1, 2, and 3, for the parts with the focus. We only give portraits for the parts with nodes, except in the case of existence of a limit cycle or a graphic where the singular point inside them is portrayed as a focus. Neither do we give specific invariant description in Sec. 3.1.2 distinguishing between these nodes and foci.

Now we explain the generic slice when c = 5 c=5 presented in Fig. 6 and 7. In this slice we shall make a complete study of all its parts, whereas in the next slices we only describe the changes. Some singular slices will produce only few changes which are easy to describe, but others can produce simultaneously many changes, even a complete change of all parts and these will require a more detailed description.

As we said before, in the mentioned figures we present the slice when c = 5 c=5 with only the algebraic surfaces. We now place for each set of the partition on this slice the local behavior of the flow around the singular points. For a specific value of the parameters of each one of the sets in this partition we compute the global phase portrait with the numerical program P4 [1, 15].

In this slice we have a partition in two–dimensional parts bordered by curved polygons, some of them bounded, others bordered by infinity. From now on, we use lower–case letters provisionally to describe the sets found algebraically in order to do not interfere with the final partition described with capital letters.

For each two–dimensional part we obtain a phase portrait which is coherent with those of all their borders. Except for three parts, which are shown in Fig. 6 and 7 and named as follows:

- •

v 14 v_{14}: the triangle bordered by yellow and blue curves (in Fig. 6);

- •

v 44 v_{44}: the triangle bordered by yellow and blue curves (in Fig. 7);

- •

v 52 v_{52}: the quadrilateral bordered by yellow and blue curves and infinity (in Fig. 7).

The study of these parts is important for the coherence of the bifurcation diagram. That is why we have decided to present only these parts in the mentioned figures.

We begin with the analysis of part v 14 v_{14}. We consider the segment 3 ​ s 6 3s_{6} in Fig. 6, which is one of the borders of part v 14 v_{14}. On this segment, the corresponding phase portrait possesses a weak focus (of order one) and, consequently, this branch of surface ( 𝒮 3 {\cal{S}}_{3}) corresponds to a Hopf bifurcation. This means that the phase portrait corresponding to one of the sides of this segment must have a limit cycle; in fact it is in the triangle v 14 v_{14}.

However, when we get close to 8 ​ s 5 8s_{5} and 3 ​ s 14 3s_{14}, the limit cycle has been lost, which implies the existence of at least one element of surface ( 𝒮 7 {\cal{S}}_{7}) (see 7 ​ S 1 7S_{1} in Fig. 9), in a neighborhood of 3 ​ s 6 3s_{6}, due to a connection of separatrices from a saddle to itself (i.e. a loop–type connection). In Lemma 7 we show that 7 ​ S 1 7S_{1} is bounded and it has its endpoints at the curves 4.8 ​ ℓ 2 4.8\ell_{2} and 2.3 ​ ℓ 2 2.3\ell_{2}. We draw the sequence of phase portraits along these subsets (using the notation from Fig. 9) in Fig. 8 and we plot the complete bifurcation diagram for this part in Fig. 9.

###### Lemma 7.

The nonalgebraic curve 7 ​ S 1 7S_{1} is bounded and it has its endpoints at the curves 4.8 ​ ℓ 2 4.8\ell_{2} and 2.3 ​ ℓ 2 2.3\ell_{2}.

###### Proof.

Numerical analysis indicate the veracity of the result. Indeed, note that if one of the endpoints of this surface is any point of 3 ​ s 6 3s_{6}, then a portion of this subset must not refer to a Hopf bifurcation, which contradicts the fact that on 3 ​ s 6 3s_{6} we have a weak focus of order one. Also, observe that it is not possible that the starting point of these surfaces is on 3 ​ s 14 3s_{14}, since on this portion of the yellow surface we have only a C ∞ C^{\infty} bifurcation (weak saddle). Finally, the endpoints cannot be on 8 ​ s 5 8s_{5} because, in order to have this, first we need to break the invariant parabola. Then, the only possible endpoints of surface 7 ​ S 1 7S_{1} are 4.8 ​ ℓ 2 4.8\ell_{2} and 2.3 ​ ℓ 2 2.3\ell_{2}. ∎

Figure 8: Sequence of phase portraits in parts V 11 V_{11} and V 14 V_{14} of slice c = 5 c=5 (the labels are according to Fig. 9)

Now we consider parts v 44 v_{44} and v 52 v_{52} in Fig. 7. When are very close to the yellow curves 3 ​ s 15 3s_{15} and 3 ​ s 16 3s_{16} we have the existence of a limit cycle in the phase portraits corresponding to parts v 44 v_{44} and v 52 v_{52}, respectively. However, when we move away from these yellow curves we observe that the limit cycles disappear. So there exist at least one element of surface ( 𝒮 7 {\cal{S}}_{7}) (see 7 ​ S 2 7S_{2} and 7 ​ S 3 7S_{3} in Fig. 10), in a neighborhood of 3 ​ s 15 3s_{15} and 3 ​ s 16 3s_{16}, respectively, due to a loop–type connection. In fact, numerical verification shows the existence of such nonalgebraic surfaces. Moreover, as we have that:

- •

3 ​ s 6 3s_{6}, 3 ​ s 15 3s_{15}, and 3 ​ s 16 3s_{16} provide topologically equivalent phase portraits,

- •

3 ​ s 14 3s_{14}, 3 ​ s 7 3s_{7}, and 3 ​ s 5 3s_{5} provide topologically equivalent phase portraits,

- •

8 ​ s 5 8s_{5}, 8 ​ s 16 8s_{16}, and 8 ​ s 17 8s_{17} provide topologically equivalent phase portraits, and

- •

4.8 ​ ℓ 2 4.8\ell_{2} and 4.8 ​ ℓ 5 4.8\ell_{5} provide topologically equivalent phase portraits,

from the analysis we made from region v 14 v_{14} it is easy to conclude the following result.

###### Lemma 8.

The nonalgebraic curves 7 ​ S 2 7S_{2} and 7 ​ S 3 7S_{3} are continuation of 7 ​ S 1 7S_{1}. Moreover, 7 ​ S 2 7S_{2} is bounded and it has its endpoints at 4.8 ​ ℓ 5 4.8\ell_{5} and 2.3 ​ ℓ 2 2.3\ell_{2}, and 7 ​ S 3 7S_{3} is not bounded and starts at 4.8 ​ ℓ 5 4.8\ell_{5}.

The complete bifurcation diagram for this part can be seeing in Fig. 10.

Regarding Remark 2, item 1, in equation ( 17) we obtained regions of the parameter space in which the corresponding phase portrait possesses center type singular point. The regions we obtained in that equation correspond to the curves 4.8 ​ L 2 4.8L_{2} (see Fig. 9) and 4.8 ​ L 5 4.8L_{5} (see Fig. 10), respectively.

We have added in the bifurcation diagram a label associated to each part of the bifurcation ( 𝒮 7 {\cal{S}}_{7}) indicating the type of connection produced by this bifurcation. More precisely, in the pictures where it appears “( ł \l oop)” we are indicating this type of separatrix connection.

Figure 9: Piece of generic slice of the parameter space when c = 5 c=5, see also Fig. 10 Figure 10: Continuation of Fig. 9

Having analyzed all the parts pointed out on page 3.1 and explained the existence of all possible nonalgebraic surfaces in there (modulo islands), we have finished the study of the generic slice c = 5 c=5. However, we cannot be sure that these are all the additional bifurcation surfaces in this slice. There could exist others which are closed surfaces small enough to escape our numerical research. For all other two–dimensional parts of the partition of this slice, whenever we join two points which are close to different borders of the part, the two phase portraits are topologically equivalent. So, we do not encounter more situations than the ones mentioned before. In short, it is expected that the complete bifurcation diagram for c = 5 c=5 is the one shown in Fig. 9 and 10. In these and in the next figures we have colored in light yellow the open regions with one limit cycle, in black the labels referring to new parts which are created in a slice and in red the labels corresponding to parts which has already appeared in previous slices.

Due to the computation we mentioned before, we already know that there are no more singular slices for c > 5 c>5. Moreover, as we discussed in Remark 5, because normal form ( 5) does not allow the study of the slice at infinity, we cannot guarantee that for c > 5 c>5 it does not exist a nonalgebraic singular slice. So, having finished the complete study of slice c = 5 c=5, the next step is to decrease the values of c c, according to equation ( 19), and make an analogous study for each one of the slices that we need to consider and also search for changes when going from one slice to the next one.

We now start decreasing the values of the parameter c c in order to explain as much as we can the bifurcations in the parameter space.

Consider Fig. 9. When we move down from c = 5 c=5 to c = 4 c=4 (a singular slice) the curve 3.4 ​ L 2 3.4L_{2} goes to f = 0 f=0 and the bifurcation curves 3 ​ S 1 3S_{1} and 4 ​ S 7 4S_{7} intersect themselves on f = 0 f=0, more precisely, at 3.4 ​ L 4 3.4L_{4}, see Fig. 11.

Figure 11: Piece of singular slice of the parameter space when c = 4 c=4

Taking c = 385 / 100 c=385/100 we observe that 3.4 ​ L 2 3.4L_{2} goes to f < 0 f<0 and from 3.4 ​ L 4 3.4L_{4} it arises the volume region V 54 V_{54}, see Fig. 12.

Figure 12: Piece of generic slice of the parameter space when c = 385 / 100 c=385/100

When c = 2 + 3 c=2+\sqrt{3} we have that 3.6 ​ L 1 3.6L_{1} goes to f = 0 f=0 and the bifurcation curves 3 ​ S 17 3S_{17} and 6 ​ S 1 6S_{1} intersect themselves on f = 0 f=0, more precisely, at 3.6 ​ L 4 3.6L_{4}, see Fig. 13.

Figure 13: Piece of singular slice of the parameter space when c = 2 + 3 c=2+\sqrt{3}

When we consider c = 3 c=3 we notice that 3.6 ​ L 1 3.6L_{1} goes to f < 0 f<0 and from 3.6 ​ L 4 3.6L_{4} it arises the volume region V 55 V_{55}. In Fig. 14 we present a piece of this generic slice, where we label the mentioned regions and also another regions that appear in the sequence.

Figure 14: Piece of generic slice of the parameter space when c = 3 c=3

Consider Fig. 14. When we study the singular slice c = 2 c=2 we observe that:

- •

the triangles V 3 V_{3} and V 6 V_{6} coalesce at 2.4 ​ L 1 2.4L_{1}, generating point P 1 P_{1};

- •

bifurcation curve 6 ​ S 20 6S_{20} intercepts 4 ​ S 20 4S_{20} at 4.6 ​ L 7 4.6L_{7} (on f = 0 f=0); and

- •

4.6 ​ L 3 4.6L_{3} goes to f = 0 f=0, making V 19 V_{19} go to f < 0 f<0.

Also, by considering Fig. 10, we note that when c = 2 c=2 the bifurcation straight lines 3 ​ S 9 3S_{9}, 4 ​ S 11 4S_{11}, and 4 ​ S 18 4S_{18} are parallel, making both 3.4 ​ L 3 3.4L_{3} and V 32 V_{32} go to infinity. The singular slice under consideration is presented in Fig. 15 and 16, in which we label only the regions that are relevant in this slice.

Figure 15: Piece of singular slice of the parameter space when c = 2 c=2, see also Fig. 16 Figure 16: Another piece of singular slice of the parameter space when c = 2 c=2, compare this region with Fig. 10

Now we consider the generic slice c = 185 / 100 c=185/100. By studying completely this slice we observe that:

- •

4.6 ​ L 3 4.6L_{3} goes to f < 0 f<0;

- •

4.6 ​ L 7 4.6L_{7} goes to f > 0 f>0 and it arises volume region V 56 V_{56};

- •

from point P 1 P_{1} we get two new volume regions, namely, V 57 V_{57} and V 58 V_{58};

see Fig. 17. Moreover, we have that the yellow straight line 3 ​ S 9 3S_{9} now intercepts 4 ​ S 11 4S_{11} at 3.4 ​ L 7 3.4L_{7} and it arises volume region V 59 V_{59}, see Fig. 18.

Figure 17: Piece of generic slice of the parameter space when c = 185 / 100 c=185/100, see also Fig. 18 Figure 18: Another piece of generic slice of the parameter space when c = 185 / 100 c=185/100, compare this region with Fig. 16

When we move down and consider the singular slice c = 3 c=\sqrt{3} we note that the volume regions V 7 V_{7} and V 36 V_{36} are reduced to the points P 2 P_{2} and P 3 P_{3}, respectively (see Fig. 19). We also have that at this value of the parameter c c the volume region V 33 V_{33} is reduced to the point P 4 P_{4}, which can be seeing in Fig. 20.

Figure 19: Piece of singular slice of the parameter space when c = 3 c=\sqrt{3}, compare this region with Fig. 17 and see also Fig. 20 Figure 20: Another piece of singular slice of the parameter space when c = 3 c=\sqrt{3}, compare this region with Fig. 18

During the study of the generic slice c = 14 / 10 c=14/10 we observe that from the points P 2 P_{2} and P 3 P_{3} arise the volume regions V 60 V_{60} and V 61 V_{61}, respectively (see Fig. 21), and we also have that from the point P 4 P_{4} it arises the volume region V 62 V_{62}, as it can be seeing in Fig. 22.

Figure 21: Piece of generic slice of the parameter space when c = 14 / 10 c=14/10, compare this region with Fig. 19 and see also Fig. 22 Figure 22: Another piece of generic slice of the parameter space when c = 14 / 10 c=14/10, compare this region with Fig. 20

Now we sum up the study of the singular slice c = 1 c=1. At this slice there are several phenomena happening simultaneously.

1. 1.

Line 4.8 ​ L 3 4.8L_{3} goes to f = 0 f=0 and V 22 V_{22} goes to f < 0 f<0;

2. 2.

the bifurcation curves 4 ​ S 22 4S_{22} and 8 ​ S 1 8S_{1} intercept themselves along f = 0 f=0, more precisely, at 4.8 ​ L 6 4.8L_{6};

3. 3.

remember that, up to here we had, in each plane, the existence of three yellow straight lines and one nonalgebraic curve. However, at c = 1 c=1 all of these bifurcation curves coalesce along the straight line f = − e f=-e (in fact, ( 𝒮 3) | c = 1 = − ( e + f) 3 ({\cal S}_{3})|_{c=1}=-(e+f)^{3}). And from this coalescence we have that:

  1. (a)

the following 15 volume regions disappear along f = − e f=-e: V 8 V_{8}, V 9 V_{9}, V 10 V_{10}, V 11 V_{11}, V 14 V_{14}, V 17 V_{17}, V 35 V_{35}, V 42 V_{42}, V 43 V_{43}, V 44 V_{44}, V 47 V_{47}, V 49 V_{49}, V 50 V_{50}, V 51 V_{51}, V 52 V_{52}; and

  2. (b)

volume region V 34 V_{34} goes to infinity.

  3. (c)

In addition, remember Remark 2, item 2, in which we verified that, for c = 1 c=1 and f = − e f=-e the corresponding phase portrait possesses one center type singular point.

In Fig. 23 we present the entire singular slice c = 1 c=1 properly labeled.

Figure 23: Singular slice of the parameter space when c = 1 c=1

Now, as it was expected, the generic slice c = 3 / 4 c=3/4 brings several new information, as we describe in the sequence.

1. 1.

Line 4.8 ​ L 3 4.8L_{3} goes to f < 0 f<0;

2. 2.

4.8 ​ L 6 4.8L_{6} goes to f > 0 f>0 and it arises the volume region V 63 V_{63};

3. 3.

consider the bifurcation straight line f = − e f=-e presented at slice c = 1 c=1. For c = 3 / 4 c=3/4 this straight line splits itself into three yellow straight lines together with one nonalgebraic bifurcation curve. As a consequence, it arise the following 16 volume regions: V 64 V_{64} up to V 79 V_{79}.

We present this slice in Fig. 24 and 25.

Regarding the nonalgebraic curves 7 ​ S 4 7S_{4} up to 7 ​ S 6 7S_{6} that there appear in the mentioned figures, we point out that their existence can be proved by using numerical tools and, by analogous arguments as the ones we presented before, the following result can be easily proved.

###### Lemma 9.

In the generic slice c = 3 / 4 c=3/4 there exist three pieces of nonalgebraic surfaces, denoted by 7 ​ S 4 7S_{4}, 7 ​ S 5 7S_{5}, and 7 ​ S 6 7S_{6}. These curves are displayed as in Fig. 24 and 25. Moreover, 7 ​ S 5 7S_{5} and 7 ​ S 6 7S_{6} are continuation of 7 ​ S 4 7S_{4}.

Figure 24: Piece of generic slice of the parameter space when c = 3 / 4 c=3/4, compare this region with Fig. 23 and see also Fig. 25 Figure 25: Another piece of generic slice of the parameter space when c = 3 / 4 c=3/4, compare this region with Fig. 23

Now, for the singular slice c = 1 / 3 c=1/\sqrt{3} we observe that volume region V 13 V_{13} coalesces at P 8 P_{8} (see Fig. 26), V 45 V_{45} coalesces at P 9 P_{9} (see Fig. 27), and V 53 V_{53} coalesces at P 10 P_{10} (see Fig. 28).

Figure 26: Piece of singular slice of the parameter space when c = 1 / 3 c=1/\sqrt{3}, compare this region with Fig. 24 and see also Fig. 27 and 28 Figure 27: Piece of singular slice of the parameter space when c = 1 / 3 c=1/\sqrt{3}, compare this region with Fig. 25 and see also 28 Figure 28: Piece of singular slice of the parameter space when c = 1 / 3 c=1/\sqrt{3}, compare this region with Fig. 25

In the generic slice c = 55 / 100 c=55/100 we observe that from P 8 P_{8} it arises the volume region V 80 V_{80} (see Fig. 29), from P 9 P_{9} we get V 81 V_{81} (see Fig. 30), and from P 10 P_{10} we have V 82 V_{82} (see Fig. 31).

Figure 29: Piece of generic slice of the parameter space when c = 55 / 100 c=55/100, compare this region with Fig. 26 and see also Fig. 30 and 31 Figure 30: Piece of generic slice of the parameter space when c = 55 / 100 c=55/100, compare this region with Fig. 27 and see also Fig. 31 Figure 31: Piece of generic slice of the parameter space when c = 55 / 100 c=55/100, compare this region with Fig. 28

We now pass to describe the result of the study of the singular slice c = 1 / 2 c=1/2.

- •

Consider volume regions V 12 V_{12} (Fig. 29) and V 25 V_{25} (Fig. 30). By studying the singular slice c = 1 / 2 c=1/2 we observe that these two volume regions coalesce at P 11 P_{11}.

- •

We also have that 6.8 ​ L 2 6.8L_{2} goes to f = 0 f=0; and

- •

6 ​ S 21 6S_{21} intercepts 8 ​ S 20 8S_{20} on f = 0 f=0, more precisely, at 6.8 ​ L 10 6.8L_{10}.

In Fig. 32 one can see these movements of the algebraic bifurcation surfaces.

In addition to the previous description, when we have c = 1 / 2 c=1/2, curve 3.8 ​ L 9 3.8L_{9} together with V 41 V_{41} (see Fig. 31) go to infinity and the straight lines 3 ​ S 43 3S_{43}, 8 ​ S 4 8S_{4}, and 8 ​ S 26 8S_{26} are now parallel (see Fig. 33).

Figure 32: Piece of singular slice of the parameter space when c = 1 / 2 c=1/2, compare this region with Fig. 29 and Fig. 30 and see also Fig. 33 Figure 33: Another piece of singular slice of the parameter space when c = 1 / 2 c=1/2, compare this region with Fig. 31

After studying the singular slice c = 1 / 2 c=1/2, if we consider c = 38 / 100 c=38/100 as a generic value of the parameter c c, we observe that:

- •

6.8 ​ L 2 6.8L_{2} from Fig. 32 goes to f < 0 f<0;

- •

6.8 ​ L 10 6.8L_{10} goes to f > 0 f>0 and it arises volume region V 83 V_{83} (see Fig. 34);

- •

3 ​ S 43 3S_{43} intercepts 8 ​ S 4 8S_{4} at 3.8 ​ L 10 3.8L_{10}, generating volume region V 84 V_{84} (see Fig. 35);

- •

from P 11 P_{11} arise volume regions V 85 V_{85} and V 86 V_{86} (see Fig. 36).

Figure 34: Piece of generic slice of the parameter space when c = 38 / 100 c=38/100, compare this region with Fig. 32 and see also Fig. 35 and 36 Figure 35: Piece of generic slice of the parameter space when c = 38 / 100 c=38/100, compare this region with Fig. 33 and see also Fig. 36 Figure 36: Piece of generic slice of the parameter space when c = 38 / 100 c=38/100, compare this region with Fig. 32

Now, when we consider the singular value c = 2 − 3 c=2-\sqrt{3} we observe that 3.6 ​ L 11 3.6L_{11} goes to f = 0 f=0 and 3 ​ S 25 3S_{25} intercepts 6 ​ S 31 6S_{31} at 3.6 ​ L 14 3.6L_{14} (also on f = 0 f=0), see Fig. 37.

Figure 37: Piece of singular slice of the parameter space when c = 2 − 3 c=2-\sqrt{3}, compare this region with Fig. 32 and 34

In Fig. 38 we present piece of generic slice c = 26 / 100 c=26/100. For this value of the parameter c c we observe that 3.6 ​ L 11 3.6L_{11} goes to f < 0 f<0 and 3.6 ​ L 14 3.6L_{14} goes to f > 0 f>0 and this provokes the appearance of volume region V 87 V_{87}.

Figure 38: Piece of generic slice of the parameter space when c = 26 / 100 c=26/100, compare this region with Fig. 37

Consider Fig. 38. During the study of the singular slice c = 1 / 4 c=1/4 we notice that 3.8 ​ L 11 3.8L_{11} goes to f = 0 f=0 and then V 15 V_{15} goes to f < 0 f<0. Moreover, 3 ​ S 47 3S_{47} intercepts 8 ​ S 27 8S_{27} on f = 0 f=0, more precisely, at 3.8 ​ L 13 3.8L_{13}. In Fig. 39 one can see a piece of the parameter space corresponding to this singular slice.

Figure 39: Piece of singular slice of the parameter space when c = 1 / 4 c=1/4, compare this region with Fig. 38

Now we consider the last generic slice corresponding to c > 0 c>0. In fact, for c = 1 / 10 c=1/10 we see that 3.8 ​ L 11 3.8L_{11} goes to f < 0 f<0 and 3.8 ​ L 13 3.8L_{13} goes to f > 0 f>0 which allows the appearance of volume region V 88 V_{88}. Moreover, we point out that numerical verification shows that the nonalgebraic curves maintain their position (with respect to the algebraic curves) as it was verified in slice c = 3 / 4 c=3/4. In Fig. 40 we present the corresponding piece of the generic slice under consideration.

Figure 40: Piece of generic slice of the parameter space when c = 1 / 10 c=1/10, compare this region with Fig. 39

According to ( 19) now we start the study of the regions of the bifurcation diagram corresponding to negative values of the parameter c c. The first generic slice to be considered is given by c = − 1 / 10 c=-1/10.

As in the case of slice c = 5 c=5, here we have a partition in two–dimensional parts bordered by curved polygons, some of them bounded and others bordered by infinity. And we use lower–case letters provisionally to describe the sets found algebraically in order to do not interfere with the final partition described with capital letters, see the algebraic slice in Fig. 41 and 42.

Figure 41: Piece of generic slice of the parameter space when c = 5 c=5 (only algebraic surfaces), see also Fig. 42 Figure 42: Continuation of Fig. 41

For each two–dimensional part we obtain a phase portrait which is coherent with those of all their borders. Except for four parts, which are shown in Fig. 41 and 42 and named as follows:

- •

v 91 v_{91}: the quadrilateral bordered by yellow and purple curves and also by the line at infinity (in Fig. 41);

- •

v 97 v_{97}: the quadrilateral bordered by yellow, purple, and (due to the symmetry) green curves (in Fig. 41);

- •

v 115 v_{115}: the quadrilateral bordered by green, purple, and (due to symmetry) yellow curves (in Fig. 41);

- •

v 120 v_{120}: the quadrilateral bordered by yellow and purple curves and infinity (in Fig. 42).

The study of these parts is important for the coherence of the bifurcation diagram. That is why we have decided to present only these parts in the mentioned figures (in Fig. 44 and Fig. 45 one can see the complete bifurcation diagram for this slice).

We start the study of part v 91 v_{91}. Segment 3 ​ s 49 3s_{49} in Fig. 41 is one of the borders of this part and, the phase portrait corresponding to this segment possesses a weak focus (of order one), so this branch of surface ( 𝒮 3 {\cal{S}}_{3}) corresponds to a Hopf bifurcation. This means that the phase portrait corresponding to one of the sides of this segment must have a limit cycle; in fact it is in region v 91 v_{91}.

However, when we approach 4 ​ s 32 4s_{32} and 3 ​ s 55 3s_{55}, the limit cycle has been lost, which implies the existence of at least one element of surface ( 𝒮 7 {\cal{S}}_{7}) (see 7 ​ S 7 7S_{7} in Fig. 44), in a neighborhood of 3 ​ s 49 3s_{49}, due to a connection of separatrices from a saddle to itself (i.e. a loop–type connection). In Lemma 10 we show that 7 ​ S 7 7S_{7} is unbounded and it has one of its endpoints at the curve 2.3 ​ ℓ 7 2.3\ell_{7}. We draw the sequence of phase portraits along these subsets (using the notation from Fig. 44) in Fig. 43 and we plot the complete bifurcation diagram for this part in Fig. 44.

###### Lemma 10.

The nonalgebraic curve 7 ​ S 7 7S_{7} is unbounded and it has one of its endpoints at the curve 2.3 ​ ℓ 7 2.3\ell_{7}.

###### Proof.

Numerical analysis suggest that this result is true. In fact, note that if one of the endpoints of this surface is any point of 3 ​ s 49 3s_{49}, then a portion of this subset must not refer to a Hopf bifurcation, which contradicts the fact that on 3 ​ s 49 3s_{49} we have a weak focus of order one. Also, observe that it is not possible that the starting point of this surface is on 3 ​ s 55 3s_{55}, since on this portion of the yellow surface we have only a C ∞ C^{\infty} bifurcation (weak saddle). Finally, the endpoints cannot be on 4 ​ s 32 4s_{32} because, in order to have this, first we need to break the invariant straight line. Then, the only possible endpoint of surface 7 ​ S 7 7S_{7} is 2.3 ​ ℓ 7 2.3\ell_{7}. ∎

Figure 43: Sequence of phase portraits in parts V 91 V_{91} and V 92 V_{92} of slice c = − 1 / 10 c=-1/10 (the labels are according to Fig. 44)

Consider Fig. 44. Note that here we have an interesting situation. On one hand, 2.3 ​ L 7 2.3L_{7} is a transition between 2 ​ S 11 2S_{11} and 2 ​ S 12 2S_{12}, i.e. one can see a cusp point being a transition of different types of saddle–nodes. On the other hand, being 2.3 ​ L 7 2.3L_{7} an endpoint of 7 ​ S 7 7S_{7} we observe a cusp point formed by the coalescence of a focus with a saddle.

Now we consider parts v 97 v_{97}, v 115 v_{115}, and v 120 v_{120} in Fig. 41 and 42. As we have that:

- •

3 ​ s 49 3s_{49} produces a phase portrait that is topologically equivalent to the ones in 3 ​ s 54 3s_{54}, 3 ​ s 63 3s_{63}, and 3 ​ s 64 3s_{64};

- •

3 ​ s 55 3s_{55} produces a phase portrait that is topologically equivalent to the ones in 3 ​ s 50 3s_{50} and 3 ​ s 62 3s_{62};

- •

4 ​ s 32 4s_{32} produces a phase portrait that is topologically equivalent to the ones in 4 ​ s 38 4s_{38}, 4 ​ s 47 4s_{47}, and 4 ​ s 48 4s_{48};

by the same arguments used in the study of part v 91 v_{91} we conclude the existence of nonalgebraic surfaces 7 ​ S 8 7S_{8}, 7 ​ S 9 7S_{9}, and 7 ​ S 10 7S_{10} in Fig. 44 and 45. Moreover we also have that 7 ​ S 10 7S_{10} is not bounded, 7 ​ S 8 7S_{8} and 7 ​ S 9 7S_{9} are bounded (due to the symmetry on the bifurcation diagram), 7 ​ S 8 7S_{8} is a continuation of 7 ​ S 7 7S_{7}, and 7 ​ S 10 7S_{10} is a continuation of 7 ​ S 9 7S_{9}.

Figure 44: Piece of generic slice of the parameter space when c = − 1 / 10 c=-1/10, see also Fig. 45 Figure 45: Continuation of Fig. 44

Now we take the singular value c = − 1 / 4 c=-1/4. For this value of the parameter c c we notice that 6.8 ​ L 11 6.8L_{11} goes to f = 0 f=0 and 6 ​ S 47 6S_{47} intercepts 8 ​ S 45 8S_{45} at 6.8 ​ L 14 6.8L_{14}, see these phenomena along f = 0 f=0 in Fig. 46.

Figure 46: Piece of singular slice of the parameter space when c = − 1 / 4 c=-1/4, compare this region with Fig. 44

By considering c = − 35 / 100 c=-35/100 as a generic slice, two expected situations are detected, namely, 6.8 ​ L 11 6.8L_{11} goes to f < 0 f<0 and 6.8 ​ L 14 6.8L_{14} goes to f > 0 f>0 giving place to the appearance of volume region V 144 V_{144}, see Fig. 47.

Figure 47: Piece of generic slice of the parameter space when c = − 35 / 100 c=-35/100, compare this region with Fig. 46

Now we consider the singular slice c = − 1 / 2 c=-1/2. Up to here we had, in each plane, the existence of three cyan straight lines. However, at c = − 1 / 2 c=-1/2 these bifurcation curves coalesce along the straight line f = − 2 ​ e f=-2e (indeed, ( 𝒮 8) | c = − 1 / 2 = ( 2 e + f) 3 / 2 ({\cal S}_{8})|_{c=-1/2}=(2e+f)^{3}/2). And from this coalescence we have that:

1. 1.

Volume regions V 112 V_{112} (Fig. 47) and V 131 V_{131} (Fig. 45) coalesce at P 13 P_{13};

2. 2.

6.8 ​ L 12 6.8L_{12} together with V 141 V_{141} (Fig. 45) go to infinity; and

3. 3.

the following ten volume regions disappear along f = − 2 ​ e f=-2e: V 104 V_{104}, V 108 V_{108}, V 110 V_{110}, V 111 V_{111}, V 129 V_{129}, V 132 V_{132}, V 133 V_{133}, V 138 V_{138}, V 139 V_{139}, and V 140 V_{140}. We advise the reader to remember their location in Fig. 44 and 45.

In Fig. 48 we present the entire singular slice c = − 1 / 2 c=-1/2 completely labeled.

Figure 48: Piece of singular slice of the parameter space when c = − 1 / 2 c=-1/2

When we consider the generic slice c = − 53 / 100 c=-53/100 we observe that the triple cyan bifurcation straight line (obtained in the previous slice) splits itself into 16 new volume regions, namely, V 145 V_{145} up to V 160 V_{160}. These volume regions are displayed as in Fig. 49 and 50.

Figure 49: Piece of generic slice of the parameter space when c = − 53 / 100 c=-53/100, see also Fig. 50 Figure 50: Continuation of Fig. 49

After the analysis of the generic slice c = − 53 / 100 c=-53/100 we study the singular slice c = − 9 / 16 = − 0.5625 c=-9/16=-0.5625. Consider Fig. 49. For this singular value of the parameter c c we observe that 6.8 ​ L 17 6.8L_{17} goes to f = 0 f=0 and then V 144 V_{144} goes to f < 0 f<0. Also, we have that 6 ​ S 43 6S_{43} intercepts 8 ​ S 49 8S_{49} at 6.8 ​ L 21 6.8L_{21}. In Fig. 51 we present the piece of slice of the parameter space corresponding to these regions.

Figure 51: Piece of singular slice of the parameter space when c = − 9 / 16 c=-9/16

Now if we consider c = − 57 / 100 c=-57/100 as a generic slice one can detect the expected phenomena: 6.8 ​ L 17 6.8L_{17} goes to f < 0 f<0 and 6.8 ​ L 21 6.8L_{21} goes to f > 0 f>0 (from which it arises V 161 V_{161}), see Fig. 52.

Figure 52: Piece of generic slice of the parameter space when c = − 57 / 100 c=-57/100

Moving on with the study of the list of slices presented in ( 19), now we consider the singular slice c = − 1 / 3 c=-1/\sqrt{3}. During the study of this slice we observe that volume regions V 106 V_{106} (see Fig. 52), V 130 V_{130}, and V 142 V_{142} (see Fig. 50) are reduced to the points P 15 P_{15}, P 16 P_{16}, and P 17 P_{17}, respectively, as we illustrate in Fig. 53 and 54.

Figure 53: Piece of singular slice of the parameter space when c = − 1 / 3 c=-1/\sqrt{3}, see also Fig. 54 Figure 54: Another piece of singular slice of the parameter space when c = − 1 / 3 c=-1/\sqrt{3}, see also Fig. 53

Taking c = − 62 / 100 c=-62/100 as a generic slice, we observe that from the points P 15 P_{15}, P 16 P_{16}, and P 17 P_{17} arise the volume regions V 162 V_{162}, V 163 V_{163}, and P 164 P_{164}, respectively. A draw of these regions can be seeing in Fig. 55 and 56.

Figure 55: Piece of generic slice of the parameter space when c = − 62 / 100 c=-62/100, see also Fig. 56 Figure 56: Another piece of generic slice of the parameter space when c = − 62 / 100 c=-62/100, see also Fig. 55

Now when we perform the study of singular slice c = − 2 / 3 c=-2/3 we observe that volume regions V 103 V_{103} (Fig. 55), V 128 V_{128}, and V 137 V_{137} (Fig. 56) are reduced to the points P 18 P_{18}, P 19 P_{19}, and P 20 P_{20}, respectively. These points are drawn in Fig. 57 and 58.

Figure 57: Piece of singular slice of the parameter space when c = − 2 / 3 c=-2/3, see also Fig. 58 Figure 58: Another piece of singular slice of the parameter space when c = − 2 / 3 c=-2/3, see also Fig. 57

Now we consider the generic slice c = − 85 / 100 c=-85/100. From the points P 15 P_{15}, P 16 P_{16}, and P 17 P_{17} arise the volume regions V 165 V_{165}, V 166 V_{166}, and V 167 V_{167}, respectively, which can be seeing in Fig. 59 and 60.

Figure 59: Piece of generic slice of the parameter space when c = − 85 / 100 c=-85/100, see also Fig. 60 Figure 60: Continuation of Fig. 59

Now we consider the singular slice c = − 1 c=-1. One may say that this is a quite interesting singular slice, because:

- •

Previously we mentioned that surface ( 𝒮 0 {\cal S}_{0}), related to a presence of an infinite elliptic–saddle of type ( 1 2) ^ ​ E − H \widehat{\!{1\choose 2}\!\!}\ E-H, defines the entire plane c = − 1 c=-1. As it was pointed out in [9] each phase portrait obtained in the study of this slice is topologically equivalent to a phase portrait obtained in a neighborhood of this plane. However, in order to have a coherent bifurcation diagram, this plane must be studied. Here we follow the pattern established in Remark 4 and we shall not draw this plane in brown color.

- •

So far we had the existence of three purple bifurcation straight lines and three cyan bifurcation straight lines. For this value of the parameter c c we observe a coalescence among pairs of these straight lines. In fact, calculation show that

 | ( 𝒮 4) | c = − 1 = ( 𝒮 8) | c = − 1 = e ⁡ ( − 2 ​ e − f − 1) ​ ( 2 ​ e + f − 1), ({\cal S}_{4})|_{c=-1}=({\cal S}_{8})|_{c=-1}=e(-2e-f-1)(2e+f-1), |  |

so the bifurcation straight lines e = 0 e=0, f = − 2 ​ e − 1 f=-2e-1, and f = − 2 ​ e + 1 f=-2e+1 have multiplicity two.

In Fig. 61 we present the entire slice c = − 1 c=-1 completely labeled. In such a figure we use the pattern set out in [8] in order to draw the bifurcation straight lines which are double, and in order to present a label for each region (in this case the open regions are labeled as pieces of surface ( 𝒮 0 {\cal S}_{0}), a bifurcation curve X X is labeled as 0. X ​ L j 0.XL_{j}, j ∈ ℕ j\in\mathbb{N}, and each intersection of two or more bifurcation curves is indicated as a point.)

Figure 61: Singular slice of the parameter space when c = − 1 c=-1

From the list of slices presented in ( 19) we observe that the generic slice to be considered now is c = − 125 / 100 c=-125/100. Doing the study of this entire slice we observe that the purple and cyan bifurcation straight lines split themselves into three purple and three cyan bifurcation straight lines. Also, it is clear that in this case we no longer have ( 𝒮 0 {\cal S}_{0}) ≡ 0 \equiv 0. This generic slice is presented in Figs. 62 and 63.

Figure 62: Piece of generic slice of the parameter space when c = − 125 / 100 c=-125/100, see also Fig. 63 Figure 63: Continuation of Fig. 62

Now we consider the singular slice c = − 3 / 2 c=-3/2. At this value, the volume regions V 189 V_{189} (see Fig. 62), V 217 V_{217}, and V 222 V_{222} (see Fig. 63) are reduced to the points P 36 P_{36}, P 37 P_{37}, and P 38 P_{38}, respectively, and these points are presented in Fig. 64 and 65.

Figure 64: Piece of singular slice of the parameter space when c = − 3 / 2 c=-3/2, see also Fig. 65 Figure 65: Another piece of singular slice of the parameter space when c = − 3 / 2 c=-3/2, see also Fig. 64 and compare this region with Fig. 63

Now, as it was expected, if we consider c = − 16 / 10 c=-16/10 as a generic slice, from the points P 36 P_{36}, P 37 P_{37}, and P 38 P_{38} we get volume regions V 226 V_{226}, V 227 V_{227}, and V 228 V_{228}, respectively, which can be seeing in Fig. 66 and 67.

Figure 66: Piece of generic slice of the parameter space when c = − 16 / 10 c=-16/10, see also Fig. 67 Figure 67: Another piece of generic slice of the parameter space when c = − 16 / 10 c=-16/10, see also Fig. 66 and compare this region with Fig. 65

For the singular slice c = − 3 c=-\sqrt{3}, the volume regions V 190 V_{190} (see Fig. 62) V 216 V_{216}, and V 224 V_{224} (see Fig. 63) are reduced to the points P 39 P_{39}, P 40 P_{40}, and P 41 P_{41}, respectively, see Fig. 68 and 69.

Figure 68: Piece of singular slice of the parameter space when c = − 3 c=-\sqrt{3}, see also Fig. 69 and compare with Fig. 62 Figure 69: Another piece of singular slice of the parameter space when c = − 3 c=-\sqrt{3}, see also Fig. 68 and compare with Fig. 62 and 63

By considering the generic slice c = − 175 / 100 c=-175/100, from the points P 39 P_{39}, P 40 P_{40}, and P 41 P_{41} we obtain volume regions V 229 V_{229}, V 230 V_{230}, and V 231 V_{231}, respectively, see Fig. 70, 71, and 72.

Figure 70: Piece of generic slice of the parameter space when c = − 175 / 100 c=-175/100, see also Fig. 71 and 72 Figure 71: Another piece of generic slice of the parameter space when c = − 175 / 100 c=-175/100, see also Fig. 70 and 72 Figure 72: Another piece of generic slice of the parameter space when c = − 175 / 100 c=-175/100, see also Fig. 70 and 71

For the singular slice c = − 16 / 9 c=-16/9, we have that 4.6 ​ L 29 4.6L_{29} (Fig. 70) goes to f = 0 f=0 and V 192 V_{192} goes to f < 0 f<0. Also, we have an intersection between 4 ​ S 71 4S_{71} and 6 ​ S 82 6S_{82} (Fig. 62) at 4.6 ​ L 32 4.6L_{32}. See these phenomena along f = 0 f=0 in Fig. 73.

Figure 73: Piece of singular slice of the parameter space when c = − 16 / 9 c=-16/9, compare with Fig. 62 and 70

Taking into consideration Fig. 73, when we perform the study of the generic slice c = − 19 / 10 c=-19/10 we observe that 4.6 ​ L 29 4.6L_{29} goes to f < 0 f<0 e 4.6 ​ L 32 4.6L_{32} goes to f > 0 f>0 and it arises volume region V 232 V_{232}, see Fig. 74. We point out that Fig. 71 can be considered as a continuation of Fig. 74 since we did not detect any change in that region.

Figure 74: Piece of generic slice of the parameter space when c = − 19 / 10 c=-19/10, see again Fig. 71

Now we consider the singular slice c = − 2 c=-2. This is another interesting and important singular slice.

- •

Surface ( 𝒮 5 \mathcal{S}_{5}) = c + 2 =c+2 is related to a coalescence of infinite singular points. Remember that if e ≠ 0 e\neq 0 the phase portraits obtained in the study of this slice possess at most one pair of infinite singular points and, if e = 0 e=0 the corresponding phase portraits have the line at infinity filled up with singularities. Here we follow Remark 4 and we shall not draw the slice c = − 2 c=-2 in red color.

- •

So far we had the existence of three purple bifurcation straight lines. For this value of the parameter c c we observe that they coalesce along e = 0 e=0. In fact, calculation show that

 | ( 𝒮 4) | c = − 2 = − 4 ​ e 3, ({\cal S}_{4})|_{c=-2}=-4e^{3}, |  |

so the bifurcation straight line e = 0 e=0 has multiplicity three.

In Fig. 75 we present the entire slice c = − 2 c=-2 completely labeled. In such a figure we use the same pattern as the one used in the slice c = − 1 c=-1 in order to present a label for each region.

Figure 75: Singular slice of the parameter space when c = − 2 c=-2

###### Remark 7.

It is important to mention that the infinite nilpotent singularity is always an elliptic–saddle of type:

- •

( 1 2) ^ ​ P ​ E ​ P − H \widehat{\!{1\choose 2}\!\!}\ PEP-H, for all c > − 1 c>-1;

- •

( 1 2) ^ ​ E − H \widehat{\!{1\choose 2}\!\!}\ E-H, for c = − 1 c=-1; and

- •

( 1 2) ^ ​ E − P ​ H ​ P \widehat{\!{1\choose 2}\!\!}\ E-PHP, for − 2 < c < − 1 -2<c<-1.

In addition, when c = − 2 c=-2 we had an infinite nilpotent saddle–node and, for all c < − 2 c<-2 we shall have infinite nilpotent saddles ( 1 2) ^ ​ H ​ H ​ H − H \widehat{\!{1\choose 2}\!\!}\ HHH-H.

Now we present the study of the generic slice c = − 3 c=-3. In this case, the triple purple bifurcation straight line from c = − 2 c=-2 splits itself into three bifurcation straight lines. Moreover, here we no longer have a coalescence of infinite singular points, given by surface ( 𝒮 5 \mathcal{S}_{5}). This generic slice is presented in Fig. 76 and 77.

Figure 76: Piece of generic slice of the parameter space when c = − 3 c=-3, see also Fig. 77 Figure 77: Continuation of Fig. 76

Consider Fig. 76 and 77. When we perform the study of the singular slice c = − 4 c=-4 we notice that 4.6 ​ L 34 4.6L_{34} goes to f = 0 f=0 (carrying V 268 V_{268} to f < 0 f<0) and we also have that 4 ​ S 89 4S_{89} intercepts 6 ​ S 107 6S_{107} at 4.6 ​ L 36 4.6L_{36}, see Fig. 78.

Figure 78: Piece of singular slice of the parameter space when c = − 4 c=-4, compare with Fig. 76 and 77

Finally we consider the last generic slice from the list presented in ( 19), namely, c = − 5 c=-5. In this slice we observe that 4.6 ​ L 34 4.6L_{34} goes to f < 0 f<0 and 4.6 ​ L 36 4.6L_{36} goes to f > 0 f>0, giving place to the appearance of volume region V 288 V_{288}, see Fig. 79.

Figure 79: Piece of generic slice of the parameter space when c = − 5 c=-5, compare with Fig. 78

Since there is coherence among the generic and singular slices presented before, no more slices are needed for the complete coherence of the bifurcation diagram. So, all the values of the parameter c c in ( 19) are sufficient for the coherence of the bifurcation diagram. Thus, we can affirm that we have described a complete bifurcation diagram for class 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) ¯ \overline{\bf{Q}{{\widehat{ES}(A)}}} modulo islands and modulo any other nonalgebraic slice (above or below, or very close to c = 0 c=0), as we discuss in Sec. 3.1.1.

#### 3.1.1 Other relevant facts about the bifurcation diagram

The bifurcation diagram we have obtained for the class 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) ¯ \overline{\bf{Q}{{\widehat{ES}(A)}}} is completely coherent, i.e. in this family, by taking any two points in the parameter space and joining them by a continuous curve, along this curve the changes in phase portraits that occur when crossing the different bifurcation surfaces we mention can be completely explained.

Nevertheless, we cannot be sure that this bifurcation diagram is the complete bifurcation diagram for 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) ¯ \overline{\bf{Q}{{\widehat{ES}(A)}}} due to the possibility of the existence of “islands” inside the parts bordered by unmentioned bifurcation surfaces. In case they exist, these “islands” would not mean any modification of the nature of the singular points. So, on the border of these “islands” we could only have bifurcations due to saddle connections or multiple limit cycles.

In case there were more bifurcation surfaces, we should still be able to join two representatives of any two parts of the 1274 parts of 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) ¯ \overline{\bf{Q}{{\widehat{ES}(A)}}} found until now with a continuous curve either without crossing such a bifurcation surface or, in case the curve crosses it, it must do it an even number of times without tangencies, otherwise one must take into account the multiplicity of the tangency, so the total number must be even. This is why we call these potential bifurcation surfaces “ islands ”.

However, we have not found a different phase portrait which could fit in such an island. A potential “island” would be the set of parameters for which the phase portraits possess a double limit cycle and this “island” would be inside the parts where W 4 < 0 W_{4}<0 since we have the presence of a focus.

#### 3.1.2 Completion of the proof of Theorem 1

In the bifurcation diagram we may have topologically equivalent phase portraits belonging to distinct parts of the parameter space. As here we have 1274 distinct parts of the parameter space, to help us to identify or to distinguish phase portraits, we need to introduce some invariants and we actually choose integer valued, character and symbol invariants. Some of them were already used in [12] and [9], but we recall them and introduce some needed ones. These invariants yield a classification which is easier to grasp.

###### Definition 1.

We denote by I 1 ​ ( S) I_{1}(S) the number of real finite singular points.

###### Definition 2.

We denote by I 2 ​ ( S) I_{2}(S) the sum of the indices of the isolated real finite singular points.

###### Definition 3.

We denote by I 3 ​ ( S) I_{3}(S) the number of real infinite singular points. We note that this number can also be infinite, which is represented by ∞ \infty.

###### Definition 4.

For a given infinite singularity s s of a system S S, let ł s \l_{s} be the number of global or local separatrices beginning or ending at s s and which do not lie on the line at infinity. We have 0 ≤ ł s ≤ 4 0\leq\l_{s}\leq 4. We denote by I 4 ​ ( S) I_{4}(S) the sequence of all such ł s \l_{s} when s s moves in the set of infinite singular points of the system S S. We start the sequence at the infinite singular point which receives (or sends) the greatest number of separatrices and take the direction which yields the greatest absolute value, e.g. the values 2110 2110 and 2011 2011 for this invariant are symmetrical (and, therefore, they are the same), so we consider 2110 2110.

###### Definition 5.

We denote by I 5 ​ ( S) I_{5}(S) the number of graphics different from the orbits of the elliptic sector (including the border of the elliptic sector).

###### Definition 6.

We denote by I 6 ​ ( S) I_{6}(S) a character from the set { ∅, s ​ n ¯ ( 2), c ​ p ^ ( 2) } \{\emptyset,\overline{sn}_{(2)},\widehat{cp}_{(2)}\} which indicate the following types of finite multiple singularities, respectively: none (in this case the system does not contain a finite multiple singularity), saddle–node, and cusp.

###### Definition 7.

We denote by I 7 ​ ( S) I_{7}(S) a character from the set { ∅, ℓ, f − i } \{\emptyset,\ell,{f\!-\!i}\} which indicate the following types of separatrix connection, respectively: none (in this case the system does not contain a separatrix connection), ℓ \ell oop, and f inite– i nfinite.

###### Definition 8.

We denote by I 8 ​ ( S) I_{8}(S) the number of limit cycles around a foci.

###### Definition 9.

We denote by I 9 ​ ( S) I_{9}(S) the number of separatrices arriving or leaving one real finite antisaddle. In case we have two real finite antisaddles this invariant is given by a pair ( A, B) (A,B) where A A and B B indicate the corresponding numbers of separatrices arriving or leaving each antisaddle.

###### Definition 10.

We denote by I 10 ​ ( S) I_{10}(S) an element from the set { c, f ⁡ ( s), f ⁡ ( u) } \{c,f(s),f(u)\}, indicating the type of the real finite singularity located inside the region bordered by the graphic, which can be of the following types, respectively: center, stable focus, and unstable focus.

As we have noted previously in Remark 6, we do not distinguish between phase portraits whose only difference is that in one we have a finite node and in the other a focus. Both phase portraits are topologically equivalent and they can only be distinguished within the C 1 C^{1} class. In case we may want to distinguish between them, a new invariant may easily be introduced.

###### Theorem 4.

Consider the class 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) ¯ \overline{\bf{Q}{{\widehat{ES}(A)}}} and all the phase portraits that we have obtained for this family. The values of the affine invariant ℐ = ( I 1, I 2, I 3, I 4, I 5, I 6, I 7, I 8, I 9, I 10) {\cal I}=(I_{1},I_{2},I_{3},I_{4},I_{5},I_{6},I_{7},I_{8},I_{9},I_{10}) given in the diagram from Tables 5 to 8 yield a partition of these phase portraits of the class 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) ¯ \overline{\bf{Q}{{\widehat{ES}(A)}}}.

Furthermore, for each value of ℐ \cal I in this diagram there corresponds a single phase portrait; i.e. S S and S ′ S^{\prime} are such that ℐ ⁡ ( S) = ℐ ⁡ ( S ′) {\cal I}(S)={\cal I}(S^{\prime}), if and only if S S and S ′ S^{\prime} are topologically equivalent.

The bifurcation diagram for 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) ¯ \overline{\bf{Q}{{\widehat{ES}(A)}}} has 1274 parts which produce 91 topologically different phase portraits as described in Tables 5 to 19. The remaining 1183 parts do not produce any new phase portrait which was not included in the 91 previous ones. The difference is basically the presence of a strong focus instead of a node and vice versa, weak points, and a presence of invariant algebraic curves (lines or parabolas) which do not represent a separatrix connection.

The phase portraits having neither limit cycle nor graphic have been denoted surrounded by parenthesis, for example ( V 233) (V_{233}); the phase portraits having one limit cycle have been denoted surrounded by brackets, for example [V 235] [V_{235}]; the phase portraits having one graphic have been denoted surrounded by { ∗ } \{\ast\} and those ones having two or more graphics have been denoted surrounded by { { ∗ } } \{\!\{\ast\}\!\}, for example { 2 ​ S 39 } \{2S_{39}\} and { { 4 ​ S 59 } } \{\!\{4S_{59}\}\!\}, respectively. Moreover, the phase portraits having one limit cycle and more than one graphic have been denoted surrounded by [{ { ∗ } }] [\{\{\ast\}\}], for example [{ { 2 ​ S 18 } }] [\{\{2S_{18}\}\}].

###### Proof of Theorem 4.

The above result follows from the results in the previous sections and a careful analysis of the bifurcation diagrams given in Sec. 3.1, in Figs. 6 and 7 to Fig. 79, the definition of the invariants I j I_{j} and their explicit values for the corresponding phase portraits. ∎

We recall some observations regarding the equivalence relations used in this study: the affine and time rescaling, C 1 C^{1} and topological equivalences.

The coarsest one among these three is the topological equivalence and the finest is the affine equivalence. We can have two systems which are topologically equivalent but not C 1 − C^{1}- equivalent. For example, we could have a system with a finite antisaddle which is a structurally stable node and in another system with a focus, the two systems being topologically equivalent but belonging to distinct C 1 − C^{1}- equivalence classes, separated by the surface ( 𝒮 6) ({\cal S}_{6}) on which the node turns into a focus.

In Tables 9 to 19 we list in the first column 91 parts with all the distinct phase portraits of Figs. 1 to 3. Corresponding to each part listed in column one we have in each row all parts whose phase portraits are topologically equivalent to the phase portrait appearing in column 1 of the same row.

In the second column we set all the parts whose systems yield topologically equivalent phase portraits to those in the first column, but which may have some algebro–geometric features related to the position of the orbits. In the third column we present all the parts which are topologically equivalent to the ones from the first column having a focus instead of a node.

In the fourth (respectively, fifth; and sixth) column we list all parts whose phase portraits have a node which is at a bifurcation point producing foci close to the node in perturbations, a node–focus to shorten (respectively, a finite weak singular point; and possess an invariant curve (straight line and/or parabola) not yielding a connection of separatrices).

The last column refers to other reasons associated to different geometrical aspects and they are described as follows:

1. (1)

The phase portraits correspond to symmetric parts of the bifurcation diagram;

2. (2)

the phase portrait possesses a singularity of type ( 1 2) ^ ​ E − H \widehat{\!{1\choose 2}\!\!}\ E-H at infinity.

Whenever phase portraits appear in a row in a specific column, the listing is done according to the decreasing dimension of the parts where they appear, always placing the lower dimensions on lower lines.

#### 3.1.3 Proof of Theorem 1

The bifurcation diagram described in Sec. 3.1, plus Tables 5 to 8 of the geometrical invariants distinguishing the 91 phase portraits, plus Tables 9 to 19 giving the equivalences with the remaining phase portraits lead to the proof of Theorem 1.

Table 5: Geometric classification for the family 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) \bf{Q}{{\widehat{ES}(A)}}

 | I 1 = { 2 & I 2 = { − 1 & I 3 = 2 & I 4 = { 2210 ​ { { 2.4 ​ L 1 } }, 3101 ​ { { 2.8 ​ L 2 } }, 3201 & I 5 = { 1 & I 6 = { c ​ p ^ ( 2) ​ { { 2.3 ​ L 2 } }, s ​ n ¯ ( 2) ​ { { 2 ​ S 6 } }, 2 ​ { { 2 ​ S 1 } }, 3310 ​ { { 2 ​ S 4 } }, 4201 ​ { { 2 ​ S 5 } }, 1 & I 3 = { 1 & I 4 = { 21 & I 5 = { 0 ​ ( P 43), 1 ​ { P 45 }, 22 & I 5 = { 0 & I 6 = { c ​ p ^ ( 2) ​ ( P 42), s ​ n ¯ ( 2) ​ ( 2.5 ​ L 2), 1 & I 6 = s ​ n ¯ ( 2) & I 7 = { ∅ ​ { 2.5 ​ L 5 }, ℓ ​ { P 46 }, 31 & I 5 = { 0 ​ ( 2.5 ​ L 3), 1 ​ { 2.5 ​ L 4 }, 32 & I 5 = 0 & I 6 = s ​ n ¯ ( 2) & I 7 = ∅ & I 8 = { 0 & I 9 = { 1 ​ ( 2.5 ​ L 8), 2 ​ ( 2.5 ​ L 1), 1 ​ [2.5 ​ L 6], 2 & I 4 = { 1110 & I 5 = { 1 ​ { { 2.4 ​ L 4 } }, 3 ​ { { 2.4 ​ L 5 } }, 2100 & I 5 = { 0 ​ ( 2.8 ​ L 10), 1 ​ { 2.8 ​ L 11 }, 2101 & I 5 = { 0 ​ ( 2 ​ S 35), 1 & I 6 = { c ​ p ^ ( 2) ​ { { 2.3 ​ L 7 } }, s ​ n ¯ ( 2) ​ { { 2 ​ S 12 } }, 2 & I 6 = s ​ n ¯ ( 2) & I 7 = { ∅ & I 8 = 0 & I 9 = { 1 ​ { { 2 ​ S 17 } }, 2 ​ { { 2 ​ S 13 } }, ℓ ​ { { 2.7 ​ L 1 } }, 𝒜 1 ​ (next page), ∞ ​ { { P 44 } }, 𝒜 2 ​ (next page), I_{1}\!=\!\left\{\begin{array}[]{ll}2\,\,\&\,\,I_{2}\!=\!\left\{\begin{array}[]{ll}-1\,\,\&\,\,I_{3}\!=\!2\,\,\&\,\,I_{4}\!=\!\left\{\begin{array}[]{ll}2210\,\,\left\{\left\{2.4L_{1}\right\}\right\},\\ 3101\,\,\left\{\left\{2.8L_{2}\right\}\right\},\\ 3201\,\,\&\,\,I_{5}\!=\!\left\{\begin{array}[]{ll}1\,\,\&\,\,I_{6}\!=\!\left\{\begin{array}[]{ll}\widehat{cp}_{(2)}\,\,\left\{\left\{2.3L_{2}\right\}\right\},\\ \overline{sn}_{(2)}\,\,\left\{\left\{2S_{6}\right\}\right\},\\ \end{array}\right.\\ 2\,\,\left\{\left\{2S_{1}\right\}\right\},\\ \end{array}\right.\\ 3310\,\,\left\{\left\{2S_{4}\right\}\right\},\\ 4201\,\,\left\{\left\{2S_{5}\right\}\right\},\\ \end{array}\right.\\ 1\,\,\&\,\,I_{3}\!=\!\left\{\begin{array}[]{ll}1\,\,\&\,\,I_{4}\!=\!\left\{\begin{array}[]{ll}21\,\,\&\,\,I_{5}\!=\!\left\{\begin{array}[]{ll}0\,\,\left(P_{43}\right),\\ 1\,\,\left\{P_{45}\right\},\\ \end{array}\right.\\ 22\,\,\&\,\,I_{5}\!=\!\left\{\begin{array}[]{ll}0\,\,\&\,\,I_{6}\!=\!\left\{\begin{array}[]{ll}\widehat{cp}_{(2)}\,\,\left(P_{42}\right),\\ \overline{sn}_{(2)}\,\,\left(2.5L_{2}\right),\\ \end{array}\right.\\ 1\,\,\&\,\,I_{6}\!=\!\overline{sn}_{(2)}\,\,\&\,\,I_{7}\!=\!\left\{\begin{array}[]{ll}\emptyset\,\,\left\{2.5L_{5}\right\},\\ \ell\,\,\left\{P_{46}\right\},\\ \end{array}\right.\\ \end{array}\right.\\ 31\,\,\&\,\,I_{5}\!=\!\left\{\begin{array}[]{ll}0\,\,\left(2.5L_{3}\right),\\ 1\,\,\left\{2.5L_{4}\right\},\\ \end{array}\right.\\ 32\,\,\&\,\,I_{5}\!=\!0\,\,\&\,\,I_{6}\!=\!\overline{sn}_{(2)}\,\,\&\,\,I_{7}\!=\!\emptyset\,\,\&\,\,I_{8}\!=\!\left\{\begin{array}[]{ll}0\,\,\&\,\,I_{9}\!=\!\left\{\begin{array}[]{ll}1\,\,\left(2.5L_{8}\right),\\ 2\,\,\left(2.5L_{1}\right),\\ \end{array}\right.\\ 1\,\,\left[2.5L_{6}\right],\\ \end{array}\right.\\ \end{array}\right.\\ 2\,\,\&\,\,I_{4}\!=\!\left\{\begin{array}[]{ll}1110\,\,\&\,\,I_{5}\!=\!\left\{\begin{array}[]{ll}1\,\,\left\{\left\{2.4L_{4}\right\}\right\},\\ 3\,\,\left\{\left\{2.4L_{5}\right\}\right\},\\ \end{array}\right.\\ 2100\,\,\&\,\,I_{5}\!=\!\left\{\begin{array}[]{ll}0\,\,\left(2.8L_{10}\right),\\ 1\,\,\left\{2.8L_{11}\right\},\\ \end{array}\right.\\ 2101\,\,\&\,\,I_{5}\!=\!\left\{\begin{array}[]{ll}0\,\,\left(2S_{35}\right),\\ 1\,\,\&\,\,I_{6}\!=\!\left\{\begin{array}[]{ll}\widehat{cp}_{(2)}\,\,\left\{\left\{2.3L_{7}\right\}\right\},\\ \overline{sn}_{(2)}\,\,\left\{\left\{2S_{12}\right\}\right\},\\ \end{array}\right.\\ 2\,\,\&\,\,I_{6}\!=\!\overline{sn}_{(2)}\,\,\&\,\,I_{7}\!=\!\left\{\begin{array}[]{ll}\emptyset\,\,\&\,\,I_{8}\!=\!0\,\,\&\,\,I_{9}\!=\!\left\{\begin{array}[]{ll}1\,\,\left\{\left\{2S_{17}\right\}\right\},\\ 2\,\,\left\{\left\{2S_{13}\right\}\right\},\\ \end{array}\right.\\ \ell\,\,\left\{\left\{2.7L_{1}\right\}\right\},\\ \end{array}\right.\\ \end{array}\right.\\ \mathcal{A}_{1}\,\,\hbox{\it(next page)},\\ \end{array}\right.\\ \infty\,\,\left\{\left\{P_{44}\right\}\right\},\\ \end{array}\right.\\ \end{array}\right.\\ \mathcal{A}_{2}\,\,\hbox{\it(next page)},\\ \end{array}\right. |  |

Table 6: Geometric classification for the family 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) \bf{Q}{{\widehat{ES}(A)}} (cont.)

 | 𝒜 1 [I 1 = 2, I 2 = 1, I 3 = 2] & I 4 = { 2111 & I 5 = { 1 ​ { { 2.4 ​ L 6 } }, 4 ​ { { 2.4 ​ L 7 } }, 2121 & I 5 = { 1 ​ { { 2.8 ​ L 8 } }, 2 ​ { { 2 ​ S 26 } }, 3 ​ { { 2.8 ​ L 9 } }, 2200 & I 5 = { 0 & I 6 = { c ​ p ^ ( 2) ​ ( 2.3 ​ L 11), s ​ n ¯ ( 2) ​ ( 2 ​ S 34), 1 & I 6 = s ​ n ¯ ( 2) & I 7 = { ∅ ​ { 2 ​ S 39 }, ℓ ​ { 2.7 ​ L 3 }, 3101 & I 5 = 1 & I 6 = s ​ n ¯ ( 2) & I 7 = ∅ & I 8 = { 0 & I 9 = { 1 ​ { { 2 ​ S 20 } }, 2 ​ { { 2 ​ S 11 } }, 1 ​ [{ { 2 ​ S 18 } }], 3121 & I 5 = { 1 & I 6 = { c ​ p ^ ( 2) ​ { { 2.3 ​ L 9 } }, s ​ n ¯ ( 2) & I 7 = ∅ & I 8 = 0 & I 9 = { 3 ​ { { 2 ​ S 25 } }, 4 ​ { { 2 ​ S 24 } }, 2 & I 6 = s ​ n ¯ ( 2) & I 7 = { ∅ ​ { { 2 ​ S 29 } }, ℓ ​ { { 2.7 ​ L 2 } }, 3 ​ { { 2 ​ S 28 } }, 3200 & I 5 = 0 & I 6 = s ​ n ¯ ( 2) & I 7 = ∅ & I 8 = { 0 & I 9 = { 1 ​ ( 2 ​ S 42), 2 ​ ( 2 ​ S 33), 1 ​ [2 ​ S 40], 4121 & I 5 = 1 & I 6 = s ​ n ¯ ( 2) & I 7 = ∅ & I 8 = { 0 & I 9 = { 1 ​ { { 2 ​ S 32 } }, 3 ​ { { 2 ​ S 23 } }, 1 ​ [{ { 2 ​ S 30 } }], \begin{array}[]{ll}\begin{matrix}\mathcal{A}_{1}\\ \begin{bmatrix}I_{1}\!=\!2,\\ I_{2}\!=\!1,\\ I_{3}\!=\!2\end{bmatrix}\end{matrix}\,\,\&\,\,I_{4}\!=\!\left\{\begin{array}[]{ll}2111\,\,\&\,\,I_{5}\!=\!\left\{\begin{array}[]{ll}1\,\,\left\{\left\{2.4L_{6}\right\}\right\},\\ 4\,\,\left\{\left\{2.4L_{7}\right\}\right\},\\ \end{array}\right.\\ 2121\,\,\&\,\,I_{5}\!=\!\left\{\begin{array}[]{ll}1\,\,\left\{\left\{2.8L_{8}\right\}\right\},\\ 2\,\,\left\{\left\{2S_{26}\right\}\right\},\\ 3\,\,\left\{\left\{2.8L_{9}\right\}\right\},\\ \end{array}\right.\\ 2200\,\,\&\,\,I_{5}\!=\!\left\{\begin{array}[]{ll}0\,\,\&\,\,I_{6}\!=\!\left\{\begin{array}[]{ll}\widehat{cp}_{(2)}\,\,\left(2.3L_{11}\right),\\ \overline{sn}_{(2)}\,\,\left(2S_{34}\right),\\ \end{array}\right.\\ 1\,\,\&\,\,I_{6}\!=\!\overline{sn}_{(2)}\,\,\&\,\,I_{7}\!=\!\left\{\begin{array}[]{ll}\emptyset\,\,\left\{2S_{39}\right\},\\ \ell\,\,\left\{2.7L_{3}\right\},\\ \end{array}\right.\\ \end{array}\right.\\ 3101\,\,\&\,\,I_{5}\!=\!1\,\,\&\,\,I_{6}\!=\!\overline{sn}_{(2)}\,\,\&\,\,I_{7}\!=\!\emptyset\,\,\&\,\,I_{8}\!=\!\left\{\begin{array}[]{ll}0\,\,\&\,\,I_{9}\!=\!\left\{\begin{array}[]{ll}1\,\,\left\{\left\{2S_{20}\right\}\right\},\\ 2\,\,\left\{\left\{2S_{11}\right\}\right\},\\ \end{array}\right.\\ 1\,\,[\left\{\left\{2S_{18}\right\}\right\}],\\ \end{array}\right.\\ 3121\,\,\&\,\,I_{5}\!=\!\left\{\begin{array}[]{ll}1\,\,\&\,\,I_{6}\!=\!\left\{\begin{array}[]{ll}\widehat{cp}_{(2)}\,\,\left\{\left\{2.3L_{9}\right\}\right\},\\ \overline{sn}_{(2)}\,\,\&\,\,I_{7}\!=\!\emptyset\,\,\&\,\,I_{8}\!=\!0\,\,\&\,\,I_{9}\!=\!\left\{\begin{array}[]{ll}3\,\,\left\{\left\{2S_{25}\right\}\right\},\\ 4\,\,\left\{\left\{2S_{24}\right\}\right\},\\ \end{array}\right.\\ \end{array}\right.\\ 2\,\,\&\,\,I_{6}\!=\!\overline{sn}_{(2)}\,\,\&\,\,I_{7}\!=\!\left\{\begin{array}[]{ll}\emptyset\,\,\left\{\left\{2S_{29}\right\}\right\},\\ \ell\,\,\left\{\left\{2.7L_{2}\right\}\right\},\\ \end{array}\right.\\ 3\,\,\left\{\left\{2S_{28}\right\}\right\},\\ \end{array}\right.\\ 3200\,\,\&\,\,I_{5}\!=\!0\,\,\&\,\,I_{6}\!=\!\overline{sn}_{(2)}\,\,\&\,\,I_{7}\!=\!\emptyset\,\,\&\,\,I_{8}\!=\!\left\{\begin{array}[]{ll}0\,\,\&\,\,I_{9}\!=\!\left\{\begin{array}[]{ll}1\,\,\left(2S_{42}\right),\\ 2\,\,\left(2S_{33}\right),\\ \end{array}\right.\\ 1\,\,\left[2S_{40}\right],\\ \end{array}\right.\\ 4121\,\,\&\,\,I_{5}\!=\!1\,\,\&\,\,I_{6}\!=\!\overline{sn}_{(2)}\,\,\&\,\,I_{7}\!=\!\emptyset\,\,\&\,\,I_{8}\!=\!\left\{\begin{array}[]{ll}0\,\,\&\,\,I_{9}\!=\!\left\{\begin{array}[]{ll}1\,\,\left\{\left\{2S_{32}\right\}\right\},\\ 3\,\,\left\{\left\{2S_{23}\right\}\right\},\\ \end{array}\right.\\ 1\,\,[\left\{\left\{2S_{30}\right\}\right\}],\\ \end{array}\right.\\ \end{array}\right.\\ \end{array} |  |

Table 7: Geometric classification for the family 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) \bf{Q}{{\widehat{ES}(A)}} (cont.)

 | 𝒜 2 [I 1 = 3] & I 2 = { − 1 & I 3 = 2 & I 4 = { 2101 ​ { { 4.8 ​ L 2 } }, 2210 ​ { { 4 ​ S 5 } }, 3101 ​ { { 8 ​ S 7 } }, 3201 & I 5 = { 1 ​ { { V 1 } }, 2 & I 6 = ∅ & I 7 = ℓ & I 8 = 0 & I 9 = & I 10 = { c ​ { { 3.7 ​ L 1 } }, f ⁡ ( s) ​ { { 7 ​ S 1 } }, f ⁡ ( u) ​ { { 7 ​ S 4 } }, 3310 & I 5 = 1 & I 6 = ∅ & I 7 = ∅ & I 8 = { 0 ​ { { V 9 } }, 1 ​ [{ { V 11 } }], 4201 & I 5 = 1 & I 6 = ∅ & I 7 = ∅ & I 8 = { 0 ​ { { V 12 } }, 1 ​ [{ { V 66 } }], 1 & I 3 = { 1 & I 4 = { 21 ​ ( 5.8 ​ L 3), 22 & I 5 = { 0 ​ ( 5 ​ S 6), 1 ​ { 5.7 ​ L 1 }, 31 ​ ( 5 ​ S 9), 32 & I 5 = 0 & I 6 = ∅ & I 7 = ∅ & I 8 = { 0 ​ ( 5 ​ S 1), 1 ​ [5 ​ S 3], 2 & I 4 = { 1110 ​ { { 4 ​ S 34 } }, 2100 ​ ( 8 ​ S 99), 2101 & I 5 = { 0 ​ ( V 240), 1 & I 6 = ∅ & I 7 = ∅ & I 8 = 0 & I 9 = { ( 1, 3) ​ { { V 94 } }, ( 2, 2) ​ { { V 101 } }, 2 ​ { { 7 ​ S 7 } }, 2111 ​ { { 4 ​ S 59 } }, 2121 & I 5 = 1 & I 6 = ∅ & I 7 = { ∅ ​ { { V 188 } }, f − i ​ { { 8 ​ S 77 } }, 2200 & I 5 = { 0 ​ ( V 238), 1 ​ { 7 ​ S 15 }, 𝒜 3 ​ (next page), ∞ ​ { { 4.5 ​ L 1 } }, \begin{array}[]{ll}\begin{matrix}\mathcal{A}_{2}\\ \begin{bmatrix}I_{1}\!=\!3\end{bmatrix}\end{matrix}\,\,\&\,\,I_{2}\!=\!\left\{\begin{array}[]{ll}-1\,\,\&\,\,I_{3}\!=\!2\,\,\&\,\,I_{4}\!=\!\left\{\begin{array}[]{ll}2101\,\,\left\{\left\{4.8L_{2}\right\}\right\},\\ 2210\,\,\left\{\left\{4S_{5}\right\}\right\},\\ 3101\,\,\left\{\left\{8S_{7}\right\}\right\},\\ 3201\,\,\&\,\,I_{5}\!=\!\left\{\begin{array}[]{ll}1\,\,\left\{\left\{V_{1}\right\}\right\},\\ 2\,\,\&\,\,I_{6}\!=\!\emptyset\,\,\&\,\,I_{7}\!=\!\ell\,\,\&\,\,I_{8}\!=\!0\,\,\&\,\,I_{9}\!=0\!\,\,\&\,\,I_{10}\!=\!\left\{\begin{array}[]{ll}c\,\,\left\{\left\{3.7L_{1}\right\}\right\},\\ f(s)\,\,\left\{\left\{7S_{1}\right\}\right\},\\ f(u)\,\,\left\{\left\{7S_{4}\right\}\right\},\\ \end{array}\right.\\ \end{array}\right.\\ 3310\,\,\&\,\,I_{5}\!=\!1\,\,\&\,\,I_{6}\!=\!\emptyset\,\,\&\,\,I_{7}\!=\!\emptyset\,\,\&\,\,I_{8}\!=\!\left\{\begin{array}[]{ll}0\,\,\left\{\left\{V_{9}\right\}\right\},\\ 1\,\,[\left\{\left\{V_{11}\right\}\right\}],\\ \end{array}\right.\\ 4201\,\,\&\,\,I_{5}\!=\!1\,\,\&\,\,I_{6}\!=\!\emptyset\,\,\&\,\,I_{7}\!=\!\emptyset\,\,\&\,\,I_{8}\!=\!\left\{\begin{array}[]{ll}0\,\,\left\{\left\{V_{12}\right\}\right\},\\ 1\,\,[\left\{\left\{V_{66}\right\}\right\}],\\ \end{array}\right.\\ \end{array}\right.\\ 1\,\,\&\,\,I_{3}\!=\!\left\{\begin{array}[]{ll}1\,\,\&\,\,I_{4}\!=\!\left\{\begin{array}[]{ll}21\,\,\left(5.8L_{3}\right),\\ 22\,\,\&\,\,I_{5}\!=\!\left\{\begin{array}[]{ll}0\,\,\left(5S_{6}\right),\\ 1\,\,\left\{5.7L_{1}\right\},\\ \end{array}\right.\\ 31\,\,\left(5S_{9}\right),\\ 32\,\,\&\,\,I_{5}\!=\!0\,\,\&\,\,I_{6}\!=\!\emptyset\,\,\&\,\,I_{7}\!=\!\emptyset\,\,\&\,\,I_{8}\!=\!\left\{\begin{array}[]{ll}0\,\,\left(5S_{1}\right),\\ 1\,\,\left[5S_{3}\right],\\ \end{array}\right.\\ \end{array}\right.\\ 2\,\,\&\,\,I_{4}\!=\!\left\{\begin{array}[]{ll}1110\,\,\left\{\left\{4S_{34}\right\}\right\},\\ 2100\,\,\left(8S_{99}\right),\\ 2101\,\,\&\,\,I_{5}\!=\!\left\{\begin{array}[]{ll}0\,\,\left(V_{240}\right),\\ 1\,\,\&\,\,I_{6}\!=\!\emptyset\,\,\&\,\,I_{7}\!=\!\emptyset\,\,\&\,\,I_{8}\!=\!0\,\,\&\,\,I_{9}\!=\!\left\{\begin{array}[]{ll}(1,3)\,\,\left\{\left\{V_{94}\right\}\right\},\\ (2,2)\,\,\left\{\left\{V_{101}\right\}\right\},\\ \end{array}\right.\\ 2\,\,\left\{\left\{7S_{7}\right\}\right\},\\ \end{array}\right.\\ 2111\,\,\left\{\left\{4S_{59}\right\}\right\},\\ 2121\,\,\&\,\,I_{5}\!=\!1\,\,\&\,\,I_{6}\!=\!\emptyset\,\,\&\,\,I_{7}\!=\!\left\{\begin{array}[]{ll}\emptyset\,\,\left\{\left\{V_{188}\right\}\right\},\\ f\!-\!{i}\,\,\left\{\left\{8S_{77}\right\}\right\},\\ \end{array}\right.\\ 2200\,\,\&\,\,I_{5}\!=\!\left\{\begin{array}[]{ll}0\,\,\left(V_{238}\right),\\ 1\,\,\left\{7S_{15}\right\},\\ \end{array}\right.\\ \mathcal{A}_{3}\,\,\hbox{\it(next page)},\\ \end{array}\right.\\ \infty\,\,\left\{\left\{4.5L_{1}\right\}\right\},\\ \end{array}\right.\\ \end{array}\right.\\ \end{array} |  |

Table 8: Geometric classification for the family 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) \bf{Q}{{\widehat{ES}(A)}} (cont.)

 | 𝒜 3 [I 1 = 3, I 2 = 1, I 3 = 2] & I 4 = { 3101 & I 5 = 1 & I 6 = ∅ & I 7 = ∅ & I 8 = { 0 ​ { { V 89 } }, 1 ​ [{ { V 91 } }], 3121 & I 5 = { 1 & I 6 = ∅ & I 7 = ∅ & I 8 = 0 & I 9 = { ( 1, 3) ​ { { V 173 } }, ( 2, 2) ​ { { V 176 } }, 2 ​ { { 7 ​ S 11 } }, 3200 & I 5 = 0 & I 6 = ∅ & I 7 = ∅ & I 8 = { 0 ​ ( V 233), 1 ​ [V 235], 4121 & I 5 = 1 & I 6 = ∅ & I 7 = ∅ & I 8 = { 0 ​ { { V 168 } }, 1 ​ [{ { V 170 } }], \begin{array}[]{ll}\begin{matrix}\mathcal{A}_{3}\\ \begin{bmatrix}I_{1}\!=\!3,\\ I_{2}\!=\!1,\\ I_{3}\!=\!2\end{bmatrix}\end{matrix}\,\,\&\,\,I_{4}\!=\!\left\{\begin{array}[]{ll}3101\,\,\&\,\,I_{5}\!=\!1\,\,\&\,\,I_{6}\!=\!\emptyset\,\,\&\,\,I_{7}\!=\!\emptyset\,\,\&\,\,I_{8}\!=\!\left\{\begin{array}[]{ll}0\,\,\left\{\left\{V_{89}\right\}\right\},\\ 1\,\,[\left\{\left\{V_{91}\right\}\right\}],\\ \end{array}\right.\\ 3121\,\,\&\,\,I_{5}\!=\!\left\{\begin{array}[]{ll}1\,\,\&\,\,I_{6}\!=\!\emptyset\,\,\&\,\,I_{7}\!=\!\emptyset\,\,\&\,\,I_{8}\!=\!0\,\,\&\,\,I_{9}\!=\!\left\{\begin{array}[]{ll}(1,3)\,\,\left\{\left\{V_{173}\right\}\right\},\\ (2,2)\,\,\left\{\left\{V_{176}\right\}\right\},\\ \end{array}\right.\\ 2\,\,\left\{\left\{7S_{11}\right\}\right\},\\ \end{array}\right.\\ 3200\,\,\&\,\,I_{5}\!=\!0\,\,\&\,\,I_{6}\!=\!\emptyset\,\,\&\,\,I_{7}\!=\!\emptyset\,\,\&\,\,I_{8}\!=\!\left\{\begin{array}[]{ll}0\,\,\left(V_{233}\right),\\ 1\,\,\left[V_{235}\right],\\ \end{array}\right.\\ 4121\,\,\&\,\,I_{5}\!=\!1\,\,\&\,\,I_{6}\!=\!\emptyset\,\,\&\,\,I_{7}\!=\!\emptyset\,\,\&\,\,I_{8}\!=\!\left\{\begin{array}[]{ll}0\,\,\left\{\left\{V_{168}\right\}\right\},\\ 1\,\,[\left\{\left\{V_{170}\right\}\right\}],\\ \end{array}\right.\\ \end{array}\right.\\ \end{array} |  |

Table 9: Topological equivalences for the family 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) \bf{Q}{{\widehat{ES}(A)}}

Presented | Identical | Finite | Finite | Finite | Possessing |  |

phase | under | antisaddle | antisaddle | weak | invariant curve | Other reasons |

portrait | perturbations | focus | node–focus | point | (no separatrix) |  |

V 1 V_{1} | V 2 V_{2}, V 3 V_{3}, V 4 V_{4}, V 5 V_{5}, V 6 V_{6} | V 8 V_{8}, V 48 V_{48} |  |  |  | V 15 ( 1) V_{15}^{(1)}, V 16 ( 1) V_{16}^{(1)}, V 17 ( 1) V_{17}^{(1)}, V 18 ( 1) V_{18}^{(1)}, V 19 ( 1) V_{19}^{(1)}, V 20 ( 1) V_{20}^{(1)} |

V 7 V_{7}, V 36 V_{36}, V 37 V_{37}, V 38 V_{38} | V 49 V_{49}, V 55 V_{55} |  |  |  | V 21 ( 1) V_{21}^{(1)}, V 22 ( 1) V_{22}^{(1)}, V 23 ( 1) V_{23}^{(1)}, V 24 ( 1) V_{24}^{(1)}, V 26 ( 1) V_{26}^{(1)}, V 27 ( 1) V_{27}^{(1)} |

V 39 V_{39}, V 40 V_{40}, V 54 V_{54}, V 56 V_{56} | V 64 V_{64}, V 74 V_{74} |  |  |  | V 28 ( 1) V_{28}^{(1)}, V 29 ( 1) V_{29}^{(1)}, V 30 ( 1) V_{30}^{(1)}, V 31 ( 1) V_{31}^{(1)}, V 32 ( 1) V_{32}^{(1)}, V 33 ( 1) V_{33}^{(1)} |

V 63 V_{63}, V 82 V_{82}, V 83 V_{83}, V 84 V_{84} |  |  |  |  | V 46 ( 1) V_{46}^{(1)}, V 47 ( 1) V_{47}^{(1)}, V 69 ( 1) V_{69}^{(1)}, V 75 ( 1) V_{75}^{(1)}, V 80 ( 1) V_{80}^{(1)}, V 81 ( 1) V_{81}^{(1)} |

V 87 V_{87}, V 88 V_{88} |  |  |  |  | V 85 ( 1) V_{85}^{(1)}, V 86 ( 1) V_{86}^{(1)} |

 |  | 3 ​ S 4 3S_{4}, 3 ​ S 18 3S_{18} | 6 ​ S 1 6S_{1}, 6 ​ S 15 6S_{15}, 6 ​ S 16 6S_{16} | 3 ​ S 1 3S_{1}, 3 ​ S 2 3S_{2} | 4 ​ S 1 4S_{1}, 4 ​ S 2 4S_{2}, 4 ​ S 3 4S_{3} | 3 ​ S 8 ( 1) 3S_{8}^{(1)}, 3 ​ S 9 ( 1) 3S_{9}^{(1)}, 3 ​ S 10 ( 1) 3S_{10}^{(1)}, 3 ​ S 11 ( 1) 3S_{11}^{(1)}, 3 ​ S 12 ( 1) 3S_{12}^{(1)} |

 |  | 3 ​ S 25 3S_{25}, 3 ​ S 31 3S_{31} | 6 ​ S 17 6S_{17}, 6 ​ S 18 6S_{18}, 6 ​ S 20 6S_{20} | 3 ​ S 3 3S_{3}, 3 ​ S 17 3S_{17} | 4 ​ S 4 4S_{4}, 4 ​ S 7 4S_{7}, 4 ​ S 20 4S_{20} | 3 ​ S 13 ( 1) 3S_{13}^{(1)}, 3 ​ S 34 ( 1) 3S_{34}^{(1)}, 3 ​ S 39 ( 1) 3S_{39}^{(1)}, 3 ​ S 41 ( 1) 3S_{41}^{(1)}, 3 ​ S 42 ( 1) 3S_{42}^{(1)} |

 |  |  | 6 ​ S 21 6S_{21}, 6 ​ S 30 6S_{30}, 6 ​ S 31 6S_{31} | 3 ​ S 43 3S_{43}, 3 ​ S 44 3S_{44} | 4 ​ S 22 4S_{22}, 4 ​ S 28 4S_{28}, 8 ​ S 1 8S_{1} | 3 ​ S 45 ( 1) 3S_{45}^{(1)}, 3 ​ S 46 ( 1) 3S_{46}^{(1)}, 4 ​ S 12 ( 1) 4S_{12}^{(1)}, 4 ​ S 13 ( 1) 4S_{13}^{(1)}, 4 ​ S 14 ( 1) 4S_{14}^{(1)} |

 |  |  | 6 ​ S 32 6S_{32} | 3 ​ S 47 3S_{47}, 3 ​ S 48 3S_{48} | 8 ​ S 2 8S_{2}, 8 ​ S 3 8S_{3}, 8 ​ S 4 8S_{4} | 4 ​ S 15 ( 1) 4S_{15}^{(1)}, 4 ​ S 16 ( 1) 4S_{16}^{(1)}, 4 ​ S 17 ( 1) 4S_{17}^{(1)}, 4 ​ S 18 ( 1) 4S_{18}^{(1)}, 4 ​ S 19 ( 1) 4S_{19}^{(1)} |

 |  |  |  |  | 8 ​ S 20 8S_{20}, 8 ​ S 27 8S_{27} | 6 ​ S 4 ( 1) 6S_{4}^{(1)}, 6 ​ S 5 ( 1) 6S_{5}^{(1)}, 6 ​ S 6 ( 1) 6S_{6}^{(1)}, 6 ​ S 7 ( 1) 6S_{7}^{(1)}, 6 ​ S 9 ( 1) 6S_{9}^{(1)} |

 |  |  |  |  | 8 ​ S 28 8S_{28}, 8 ​ S 31 8S_{31} | 6 ​ S 10 ( 1) 6S_{10}^{(1)}, 6 ​ S 11 ( 1) 6S_{11}^{(1)}, 6 ​ S 12 ( 1) 6S_{12}^{(1)}, 6 ​ S 28 ( 1) 6S_{28}^{(1)}, 6 ​ S 29 ( 1) 6S_{29}^{(1)} |

 |  |  |  |  |  | 8 ​ S 8 ( 1) 8S_{8}^{(1)}, 8 ​ S 9 ( 1) 8S_{9}^{(1)}, 8 ​ S 10 ( 1) 8S_{10}^{(1)}, 8 ​ S 11 ( 1) 8S_{11}^{(1)}, 8 ​ S 12 ( 1) 8S_{12}^{(1)} |

 |  |  |  |  |  | 8 ​ S 13 ( 1) 8S_{13}^{(1)}, 8 ​ S 29 ( 1) 8S_{29}^{(1)}, 8 ​ S 30 ( 1) 8S_{30}^{(1)} |

 |  |  | 3.6 ​ L 3 3.6L_{3}, 3.6 ​ L 4 3.6L_{4} | 3.4 ​ L 1 3.4L_{1}, 3.4 ​ L 4 3.4L_{4} | 4.8 ​ L 1 4.8L_{1}, 4.8 ​ L 6 4.8L_{6} | 3.4 ​ L 2 ( 1) 3.4L_{2}^{(1)}, 3.4 ​ L 3 ( 1) 3.4L_{3}^{(1)}, 3.6 ​ L 1 ( 1) 3.6L_{1}^{(1)}, 3.6 ​ L 2 ( 1) 3.6L_{2}^{(1)} |

 |  |  | 3.6 ​ L 13 3.6L_{13}, 3.6 ​ L 14 3.6L_{14} | 3.8 ​ L 10 3.8L_{10}, 3.8 ​ L 13 3.8L_{13} |  | 3.6 ​ L 11 ( 1) 3.6L_{11}^{(1)}, 3.6 ​ L 12 ( 1) 3.6L_{12}^{(1)}, 3.8 ​ L 11 ( 1) 3.8L_{11}^{(1)}, 3.8 ​ L 12 ( 1) 3.8L_{12}^{(1)} |

 |  |  | 4.6 ​ L 1 4.6L_{1}, 4.6 ​ L 7 4.6L_{7} |  |  | 4.6 ​ L 3 ( 1) 4.6L_{3}^{(1)}, 4.6 ​ L 5 ( 1) 4.6L_{5}^{(1)}, 4.8 ​ L 3 ( 1) 4.8L_{3}^{(1)}, 4.8 ​ L 4 ( 1) 4.8L_{4}^{(1)} |

 |  |  | 6.8 ​ L 5 6.8L_{5}, 6.8 ​ L 10 6.8L_{10} |  |  | 6.8 ​ L 2 ( 1) 6.8L_{2}^{(1)}, 6.8 ​ L 3 ( 1) 6.8L_{3}^{(1)} |

V 9 V_{9} | V 35 V_{35}, V 57 V_{57}, V 58 V_{58} | V 10 V_{10}, V 42 V_{42}, V 60 V_{60} |  |  |  | V 34 ( 1) V_{34}^{(1)}, V 50 ( 1) V_{50}^{(1)}, V 59 ( 1) V_{59}^{(1)}, V 62 ( 1) V_{62}^{(1)}, V 76 ( 1) V_{76}^{(1)} |

 | V 61 V_{61}, V 65 V_{65}, V 73 V_{73} |  |  |  |  |

 |  | 3 ​ S 6 3S_{6}, 3 ​ S 15 3S_{15}, 3 ​ S 22 3S_{22} | 6 ​ S 2 6S_{2}, 6 ​ S 14 6S_{14}, 6 ​ S 22 6S_{22} | 3 ​ S 19 3S_{19}, 3 ​ S 20 3S_{20} |  | 3 ​ S 16 ( 1) 3S_{16}^{(1)}, 3 ​ S 21 ( 1) 3S_{21}^{(1)}, 3 ​ S 24 ( 1) 3S_{24}^{(1)}, 3 ​ S 40 ( 1) 3S_{40}^{(1)} |

 |  | 3 ​ S 23 3S_{23}, 3 ​ S 26 3S_{26}, 3 ​ S 30 3S_{30} | 6 ​ S 23 6S_{23} |  |  | 6 ​ S 8 ( 1) 6S_{8}^{(1)}, 6 ​ S 24 ( 1) 6S_{24}^{(1)} |

 |  |  | 3.6 ​ L 5 3.6L_{5}, 3.6 ​ L 6 3.6L_{6} |  |  | 3.6 ​ L 7 ( 1) 3.6L_{7}^{(1)} |

Table 10: Topological equivalences for the family 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) \bf{Q}{{\widehat{ES}(A)}} (cont.)

Presented | Identical | Finite | Finite | Finite | Possessing |  |

phase | under | antisaddle | antisaddle | weak | invariant curve | Other reasons |

portrait | perturbations | focus | node–focus | point | (no separatrix) |  |

V 11 V_{11} | V 43 V_{43} |  |  |  |  | V 51 ( 1) V_{51}^{(1)} |

V 12 V_{12} | V 25 V_{25}, V 67 V_{67}, V 70 V_{70} | V 13 V_{13}, V 14 V_{14}, V 44 V_{44} |  |  |  | V 41 ( 1) V_{41}^{(1)}, V 52 ( 1) V_{52}^{(1)}, V 53 ( 1) V_{53}^{(1)}, V 78 ( 1) V_{78}^{(1)}, V 79 ( 1) V_{79}^{(1)} |

 | V 45 V_{45}, V 68 V_{68}, V 71 V_{71} |  |  |  |  |

 |  | 3 ​ S 7 3S_{7}, 3 ​ S 14 3S_{14}, 3 ​ S 27 3S_{27} | 6 ​ S 3 6S_{3}, 6 ​ S 13 6S_{13} | 3 ​ S 36 3S_{36}, 3 ​ S 37 3S_{37} |  | 3 ​ S 5 ( 1) 3S_{5}^{(1)}, 3 ​ S 28 ( 1) 3S_{28}^{(1)}, 3 ​ S 32 ( 1) 3S_{32}^{(1)}, 3 ​ S 33 ( 1) 3S_{33}^{(1)} |

 |  | 3 ​ S 29 3S_{29}, 3 ​ S 35 3S_{35}, 3 ​ S 38 3S_{38} | 6 ​ S 25 6S_{25}, 6 ​ S 26 6S_{26} |  |  | 6 ​ S 19 ( 1) 6S_{19}^{(1)}, 6 ​ S 27 ( 1) 6S_{27}^{(1)} |

 |  |  | 3.6 ​ L 8 3.6L_{8}, 3.6 ​ L 9 3.6L_{9} |  |  | 3.6 ​ L 10 ( 1) 3.6L_{10}^{(1)} |

V 66 V_{66} | V 72 V_{72} |  |  |  |  | V 77 ( 1) V_{77}^{(1)} |

V 89 V_{89} | V 95 V_{95} | V 90 V_{90}, V 96 V_{96} |  |  |  | V 116 ( 1) V_{116}^{(1)}, V 117 ( 1) V_{117}^{(1)}, V 118 ( 1) V_{118}^{(1)}, V 119 ( 1) V_{119}^{(1)} |

 |  | 0 ​ S 2 0S_{2}, 0 ​ S 8 0S_{8}, 3 ​ S 49 3S_{49} | 6 ​ S 33 6S_{33}, 6 ​ S 39 6S_{39} |  |  | 0 ​ S 1 ( 2) 0S_{1}^{(2)}, 0 ​ S 7 ( 2) 0S_{7}^{(2)}, 0 ​ S 20 ( 1) 0S_{20}^{(1)}, 0 ​ S 21 ( 1) 0S_{21}^{(1)}, 0 ​ S 22 ( 1) 0S_{22}^{(1)} |

 |  | 3 ​ S 54 3S_{54} |  |  |  | 0 ​ S 23 ( 1) 0S_{23}^{(1)}, 3 ​ S 63 ( 1) 3S_{63}^{(1)}, 3 ​ S 64 ( 1) 3S_{64}^{(1)}, 6 ​ S 45 ( 1) 6S_{45}^{(1)}, 6 ​ S 46 ( 1) 6S_{46}^{(1)} |

 |  | 0.3 ​ L 1 0.3L_{1}, 0.3 ​ L 4 0.3L_{4} | 0.6 ​ L 1 0.6L_{1}, 0.6 ​ L 5 0.6L_{5} |  |  | 0.3 ​ L 9 ( 1) 0.3L_{9}^{(1)}, 0.3 ​ L 10 ( 1) 0.3L_{10}^{(1)}, 0.6 ​ L 8 ( 1) 0.6L_{8}^{(1)}, 0.6 ​ L 9 ( 1) 0.6L_{9}^{(1)} |

V 91 V_{91} | V 97 V_{97} |  |  |  |  | V 115 ( 1) V_{115}^{(1)}, V 120 ( 1) V_{120}^{(1)} |

 |  |  |  |  |  | 0 ​ S 3 ( 2) 0S_{3}^{(2)}, 0 ​ S 9 ( 2) 0S_{9}^{(2)}, 0 ​ S 19 ( 1) 0S_{19}^{(1)}, 0 ​ S 24 ( 1) 0S_{24}^{(1)} |

V 94 V_{94} | V 100 V_{100} | V 92 V_{92}, V 93 V_{93}, V 98 V_{98}, V 99 V_{99} |  |  |  | V 114 ( 1) V_{114}^{(1)}, V 121 ( 1) V_{121}^{(1)}, V 122 ( 1) V_{122}^{(1)}, V 123 ( 1) V_{123}^{(1)} |

 |  | 0 ​ S 4 0S_{4}, 0 ​ S 5 0S_{5}, 0 ​ S 10 0S_{10}, 0 ​ S 11 0S_{11} | 6 ​ S 34 6S_{34}, 6 ​ S 40 6S_{40} |  |  | 0 ​ S 6 ( 2) 0S_{6}^{(2)}, 0 ​ S 12 ( 2) 0S_{12}^{(2)}, 0 ​ S 18 ( 1) 0S_{18}^{(1)}, 0 ​ S 25 ( 1) 0S_{25}^{(1)}, 0 ​ S 30 ( 1) 0S_{30}^{(1)} |

 |  | 3 ​ S 50 3S_{50}, 3 ​ S 55 3S_{55} |  |  |  | 0 ​ S 31 ( 1) 0S_{31}^{(1)}, 3 ​ S 62 ( 1) 3S_{62}^{(1)}, 6 ​ S 52 ( 1) 6S_{52}^{(1)} |

 |  | 0.3 ​ L 2 0.3L_{2}, 0.3 ​ L 5 0.3L_{5} | 0.6 ​ L 2 0.6L_{2}, 0.6 ​ L 6 0.6L_{6} |  |  | 0.3 ​ L 8 ( 1) 0.3L_{8}^{(1)}, 0.6 ​ L 13 ( 1) 0.6L_{13}^{(1)} |

Table 11: Topological equivalences for the family 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) \bf{Q}{{\widehat{ES}(A)}} (cont.)

Presented | Identical | Finite | Finite | Finite | Possessing | Other |

phase | under | antisaddle | antisaddle | weak | invariant curve | reasons |

portrait | perturbations | focus | node–focus | point | (no separatrix) |  |

V 101 V_{101} | V 103 V_{103}, V 104 V_{104}, V 106 V_{106}, V 107 V_{107}, V 108 V_{108}, V 109 V_{109} | V 102 V_{102}, V 105 V_{105} |  |  |  |  |

V 110 V_{110}, V 111 V_{111}, V 112 V_{112}, V 124 V_{124}, V 125 V_{125}, V 128 V_{128} | V 113 V_{113}, V 126 V_{126} |  |  |  |  |

V 129 V_{129}, V 130 V_{130}, V 131 V_{131}, V 132 V_{132}, V 133 V_{133}, V 134 V_{134} | V 127 V_{127}, V 136 V_{136} |  |  |  |  |

V 135 V_{135}, V 137 V_{137}, V 138 V_{138}, V 139 V_{139}, V 140 V_{140}, V 141 V_{141} | V 143 V_{143}, V 149 V_{149} |  |  |  |  |

V 142 V_{142}, V 144 V_{144}, V 145 V_{145}, V 146 V_{146}, V 147 V_{147}, V 148 V_{148} | V 152 V_{152}, V 159 V_{159} |  |  |  |  |

V 150 V_{150}, V 151 V_{151}, V 153 V_{153}, V 154 V_{154}, V 155 V_{155}, V 156 V_{156} | V 161 V_{161}, V 162 V_{162} |  |  |  |  |

V 157 V_{157}, V 158 V_{158}, V 160 V_{160}, V 165 V_{165}, V 166 V_{166}, V 167 V_{167} | V 163 V_{163}, V 164 V_{164} |  |  |  |  |

 |  | 0 ​ S 14 0S_{14}, 0 ​ S 15 0S_{15} | 6 ​ S 35 6S_{35}, 6 ​ S 36 6S_{36}, 6 ​ S 37 6S_{37}, 6 ​ S 38 6S_{38}, 6 ​ S 41 6S_{41} | 3 ​ S 52 3S_{52} | 4 ​ S 35 4S_{35}, 4 ​ S 36 4S_{36}, 4 ​ S 37 4S_{37}, 4 ​ S 41 4S_{41}, 4 ​ S 42 4S_{42} | 0 ​ S 13 ( 2) 0S_{13}^{(2)} |

 |  | 0 ​ S 17 0S_{17}, 0 ​ S 26 0S_{26} | 6 ​ S 42 6S_{42}, 6 ​ S 43 6S_{43}, 6 ​ S 44 6S_{44}, 6 ​ S 47 6S_{47}, 6 ​ S 48 6S_{48} | 3 ​ S 53 3S_{53} | 4 ​ S 43 4S_{43}, 4 ​ S 44 4S_{44}, 4 ​ S 45 4S_{45}, 4 ​ S 46 4S_{46}, 4 ​ S 51 4S_{51} | 0 ​ S 16 ( 2) 0S_{16}^{(2)} |

 |  | 0 ​ S 29 0S_{29}, 0 ​ S 33 0S_{33} | 6 ​ S 49 6S_{49}, 6 ​ S 50 6S_{50}, 6 ​ S 51 6S_{51}, 6 ​ S 53 6S_{53}, 6 ​ S 54 6S_{54} | 3 ​ S 57 3S_{57} | 4 ​ S 52 4S_{52}, 4 ​ S 53 4S_{53}, 4 ​ S 54 4S_{54}, 4 ​ S 55 4S_{55}, 4 ​ S 56 4S_{56} | 0 ​ S 27 ( 2) 0S_{27}^{(2)} |

 |  | 0 ​ S 35 0S_{35}, 3 ​ S 51 3S_{51} | 6 ​ S 55 6S_{55}, 6 ​ S 56 6S_{56}, 6 ​ S 57 6S_{57}, 6 ​ S 58 6S_{58}, 6 ​ S 59 6S_{59} | 3 ​ S 58 3S_{58} | 8 ​ S 32 8S_{32}, 8 ​ S 33 8S_{33}, 8 ​ S 34 8S_{34}, 8 ​ S 35 8S_{35}, 8 ​ S 36 8S_{36} | 0 ​ S 28 ( 2) 0S_{28}^{(2)} |

 |  | 3 ​ S 56 3S_{56}, 3 ​ S 61 3S_{61} | 6 ​ S 60 6S_{60}, 6 ​ S 61 6S_{61}, 6 ​ S 62 6S_{62}, 6 ​ S 63 6S_{63}, 6 ​ S 64 6S_{64} | 3 ​ S 59 3S_{59} | 8 ​ S 37 8S_{37}, 8 ​ S 38 8S_{38}, 8 ​ S 39 8S_{39}, 8 ​ S 40 8S_{40}, 8 ​ S 41 8S_{41} | 0 ​ S 32 ( 2) 0S_{32}^{(2)} |

 |  | 3 ​ S 68 3S_{68}, 3 ​ S 69 3S_{69} | 6 ​ S 65 6S_{65}, 6 ​ S 66 6S_{66} | 3 ​ S 60 3S_{60} | 8 ​ S 42 8S_{42}, 8 ​ S 43 8S_{43}, 8 ​ S 44 8S_{44}, 8 ​ S 45 8S_{45}, 8 ​ S 46 8S_{46} | 0 ​ S 34 ( 2) 0S_{34}^{(2)} |

 |  | 3 ​ S 70 3S_{70}, 8 ​ S 61 8S_{61} |  | 3 ​ S 65 3S_{65} | 8 ​ S 47 8S_{47}, 8 ​ S 48 8S_{48}, 8 ​ S 49 8S_{49}, 8 ​ S 50 8S_{50}, 8 ​ S 51 8S_{51} |  |

 |  | 8 ​ S 63 8S_{63}, 8 ​ S 64 8S_{64} |  | 3 ​ S 66 3S_{66} | 8 ​ S 52 8S_{52}, 8 ​ S 53 8S_{53}, 8 ​ S 54 8S_{54}, 8 ​ S 55 8S_{55}, 8 ​ S 56 8S_{56} |  |

 |  | 8 ​ S 68 8S_{68}, 8 ​ S 69 8S_{69} |  | 3 ​ S 67 3S_{67} | 8 ​ S 57 8S_{57}, 8 ​ S 58 8S_{58}, 8 ​ S 59 8S_{59}, 8 ​ S 60 8S_{60}, 8 ​ S 62 8S_{62} |  |

 |  | 8 ​ S 71 8S_{71} |  |  | 8 ​ S 65 8S_{65}, 8 ​ S 66 8S_{66}, 8 ​ S 67 8S_{67}, 8 ​ S 70 8S_{70}, 8 ​ S 72 8S_{72} |  |

 |  |  |  |  | 8 ​ S 73 8S_{73}, 8 ​ S 74 8S_{74} |  |

 |  | 0.3 ​ L 3 0.3L_{3} | 0.6 ​ L 3 0.6L_{3}, 0.6 ​ L 4 0.6L_{4}, 0.6 ​ L 7 0.6L_{7}, 0.6 ​ L 10 0.6L_{10} | 3.8 ​ L 14 3.8L_{14} | 0.4 ​ L 4 0.4L_{4}, 0.4 ​ L 8 0.4L_{8}, 0.4 ​ L 9 0.4L_{9} |  |

 |  | 0.3 ​ L 6 0.3L_{6} | 0.6 ​ L 11 0.6L_{11}, 0.6 ​ L 12 0.6L_{12}, 3.6 ​ L 15 3.6L_{15}, 3.6 ​ L 16 3.6L_{16} | 3.8 ​ L 15 3.8L_{15} | 4.8 ​ L 9 4.8L_{9}, 4.8 ​ L 10 4.8L_{10}, 4.8 ​ L 11 4.8L_{11} |  |

 |  | 0.3 ​ L 7 0.3L_{7} | 3.6 ​ L 17 3.6L_{17}, 3.6 ​ L 18 3.6L_{18}, 3.6 ​ L 19 3.6L_{19}, 3.6 ​ L 20 3.6L_{20} | 3.8 ​ L 16 3.8L_{16} | 4.8 ​ L 12 4.8L_{12}, 4.8 ​ L 13 4.8L_{13}, 4.8 ​ L 14 4.8L_{14} |  |

 |  | 3.8 ​ L 20 3.8L_{20} | 4.6 ​ L 12 4.6L_{12}, 4.6 ​ L 14 4.6L_{14}, 4.6 ​ L 15 4.6L_{15}, 4.6 ​ L 17 4.6L_{17} | 3.8 ​ L 17 3.8L_{17} | 4.8 ​ L 15 4.8L_{15}, 4.8 ​ L 16 4.8L_{16}, 4.8 ​ L 17 4.8L_{17} |  |

 |  | 3.8 ​ L 21 3.8L_{21} | 4.6 ​ L 18 4.6L_{18}, 4.6 ​ L 19 4.6L_{19}, 6.8 ​ L 11 6.8L_{11}, 6.8 ​ L 12 6.8L_{12} | 3.8 ​ L 18 3.8L_{18} | 4.8 ​ L 18 4.8L_{18}, 4.8 ​ L 19 4.8L_{19}, 4.8 ​ L 20 4.8L_{20} |  |

 |  | 3.8 ​ L 22 3.8L_{22} | 6.8 ​ L 13 6.8L_{13}, 6.8 ​ L 14 6.8L_{14}, 6.8 ​ L 15 6.8L_{15}, 6.8 ​ L 16 6.8L_{16} | 3.8 ​ L 19 3.8L_{19} | 4.8 ​ L 21 4.8L_{21}, 8.8 ​ L 1 8.8L_{1}, 8.8 ​ L 2 8.8L_{2} |  |

 |  |  | 6.8 ​ L 17 6.8L_{17}, 6.8 ​ L 18 6.8L_{18}, 6.8 ​ L 19 6.8L_{19}, 6.8 ​ L 20 6.8L_{20} |  | 8.8 ​ L 3 8.8L_{3} |  |

 |  |  | 6.8 ​ L 21 6.8L_{21}, 6.8 ​ L 22 6.8L_{22}, 6.8 ​ L 23 6.8L_{23}, 6.8 ​ L 24 6.8L_{24} |  |  |  |

 |  |  | 6.8 ​ L 25 6.8L_{25}, 6.8 ​ L 26 6.8L_{26}, 6.8 ​ L 27 6.8L_{27} |  |  |  |

 |  |  | P 15 P_{15}, P 16 P_{16}, P 17 P_{17}, P 18 P_{18}, P 19 P_{19}, P 20 P_{20} |  | P 12 P_{12}, P 14 P_{14} |  |

 |  |  | P 30 P_{30}, P 33 P_{33} |  |  |  |

Table 12: Topological equivalences for the family 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) \bf{Q}{{\widehat{ES}(A)}} (cont.)

Presented | Identical | Finite | Finite | Finite | Possessing |  |

phase | under | antisaddle | antisaddle | weak | invariant curve | Other reasons |

portrait | perturbations | focus | node–focus | point | (no separatrix) |  |

V 168 V_{168} | V 178 V_{178} | V 169 V_{169}, V 179 V_{179} |  |  |  | V 200 ( 1) V_{200}^{(1)}, V 201 ( 1) V_{201}^{(1)}, V 202 ( 1) V_{202}^{(1)}, V 203 ( 1) V_{203}^{(1)} |

 |  | 3 ​ S 71 3S_{71}, 3 ​ S 76 3S_{76} | 6 ​ S 67 6S_{67}, 6 ​ S 74 6S_{74} |  |  | 3 ​ S 85 ( 1) 3S_{85}^{(1)}, 3 ​ S 86 ( 1) 3S_{86}^{(1)}, 6 ​ S 80 ( 1) 6S_{80}^{(1)}, 6 ​ S 81 ( 1) 6S_{81}^{(1)} |

V 170 V_{170} | V 180 V_{180} |  |  |  |  | V 199 ( 1) V_{199}^{(1)}, V 204 ( 1) V_{204}^{(1)} |

V 173 V_{173} | V 183 V_{183} | V 171 V_{171}, V 172 V_{172}, V 181 V_{181} |  |  |  | V 198 ( 1) V_{198}^{(1)}, V 205 ( 1) V_{205}^{(1)}, V 206 ( 1) V_{206}^{(1)}, V 207 ( 1) V_{207}^{(1)} |

 | V 182 V_{182} |  |  |  |  |

 |  | 3 ​ S 72 3S_{72}, 3 ​ S 77 3S_{77} | 6 ​ S 68 6S_{68}, 6 ​ S 75 6S_{75} |  |  | 3 ​ S 84 ( 1) 3S_{84}^{(1)}, 6 ​ S 89 ( 1) 6S_{89}^{(1)} |

V 176 V_{176} | V 177 V_{177}, V 185 V_{185}, V 226 V_{226} | V 174 V_{174}, V 175 V_{175}, V 184 V_{184} |  |  |  | V 197 ( 1) V_{197}^{(1)}, V 208 ( 1) V_{208}^{(1)}, V 209 ( 1) V_{209}^{(1)}, V 210 ( 1) V_{210}^{(1)} |

V 228 V_{228}, V 229 V_{229}, V 231 V_{231} | V 186 V_{186}, V 187 V_{187} |  |  |  | V 211 ( 1) V_{211}^{(1)}, V 227 ( 1) V_{227}^{(1)}, V 230 ( 1) V_{230}^{(1)}, V 232 ( 1) V_{232}^{(1)} |

 |  | 3 ​ S 73 3S_{73}, 3 ​ S 78 3S_{78} | 6 ​ S 69 6S_{69}, 6 ​ S 76 6S_{76}, 6 ​ S 90 6S_{90} | 3 ​ S 87 3S_{87}, 3 ​ S 89 3S_{89} | 8 ​ S 78 8S_{78}, 8 ​ S 84 8S_{84} | 3 ​ S 83 ( 1) 3S_{83}^{(1)}, 3 ​ S 88 ( 1) 3S_{88}^{(1)}, 6 ​ S 88 ( 1) 6S_{88}^{(1)}, 6 ​ S 91 ( 1) 6S_{91}^{(1)} |

 |  |  | 6 ​ S 92 6S_{92}, 6 ​ S 93 6S_{93}, 6 ​ S 95 6S_{95} |  | 8 ​ S 94 8S_{94}, 8 ​ S 96 8S_{96} | 6 ​ S 94 ( 1) 6S_{94}^{(1)}, 6 ​ S 96 ( 1) 6S_{96}^{(1)}, 8 ​ S 89 ( 1) 8S_{89}^{(1)}, 8 ​ S 95 ( 1) 8S_{95}^{(1)} |

 |  |  | 3.6 ​ L 24 3.6L_{24}, 3.6 ​ L 26 3.6L_{26} |  |  | 3.6 ​ L 25 ( 1) 3.6L_{25}^{(1)}, 6.8 ​ L 35 ( 1) 6.8L_{35}^{(1)} |

 |  |  | 6.8 ​ L 34 6.8L_{34}, 6.8 ​ L 36 6.8L_{36} |  |  |  |

V 188 V_{188} | V 189 V_{189}, V 191 V_{191}, V 193 V_{193} | V 190 V_{190}, V 192 V_{192} |  |  |  |  |

V 194 V_{194}, V 195 V_{195}, V 213 V_{213} | V 196 V_{196}, V 212 V_{212} |  |  |  |  |

V 214 V_{214}, V 215 V_{215}, V 217 V_{217} | V 216 V_{216}, V 224 V_{224} |  |  |  |  |

V 218 V_{218}, V 219 V_{219}, V 220 V_{220} | V 225 V_{225} |  |  |  |  |

V 221 V_{221}, V 222 V_{222}, V 223 V_{223} |  |  |  |  |  |

 |  | 3 ​ S 74 3S_{74}, 3 ​ S 79 3S_{79} | 6 ​ S 70 6S_{70}, 6 ​ S 71 6S_{71}, 6 ​ S 72 6S_{72}, 6 ​ S 73 6S_{73} | 3 ​ S 75 3S_{75}, 3 ​ S 80 3S_{80} | 4 ​ S 61 4S_{61}, 4 ​ S 62 4S_{62}, 4 ​ S 67 4S_{67} |  |

 |  | 3 ​ S 82 3S_{82} | 6 ​ S 77 6S_{77}, 6 ​ S 78 6S_{78}, 6 ​ S 79 6S_{79}, 6 ​ S 82 6S_{82} | 3 ​ S 81 3S_{81} | 4 ​ S 68 4S_{68}, 4 ​ S 69 4S_{69}, 4 ​ S 70 4S_{70} |  |

 |  |  | 6 ​ S 83 6S_{83}, 6 ​ S 84 6S_{84}, 6 ​ S 85 6S_{85}, 6 ​ S 86 6S_{86} |  | 8 ​ S 79 8S_{79}, 8 ​ S 80 8S_{80}, 8 ​ S 85 8S_{85} |  |

 |  |  | 6 ​ S 87 6S_{87} |  | 8 ​ S 86 8S_{86}, 8 ​ S 87 8S_{87}, 8 ​ S 88 8S_{88} |  |

 |  |  | 3.6 ​ L 21 3.6L_{21}, 3.6 ​ L 22 3.6L_{22}, 3.6 ​ L 23 3.6L_{23} |  | 4.8 ​ L 23 4.8L_{23}, 4.8 ​ L 26 4.8L_{26} |  |

 |  |  | 4.6 ​ L 21 4.6L_{21}, 4.6 ​ L 23 4.6L_{23}, 4.6 ​ L 24 4.6L_{24} |  |  |  |

 |  |  | 6.8 ​ L 29 6.8L_{29}, 6.8 ​ L 31 6.8L_{31}, 6.8 ​ L 32 6.8L_{32} |  |  |  |

V 233 V_{233} | V 252 V_{252} | V 234 V_{234}, V 253 V_{253} |  |  |  | V 273 ( 1) V_{273}^{(1)}, V 274 ( 1) V_{274}^{(1)}, V 275 ( 1) V_{275}^{(1)}, V 276 ( 1) V_{276}^{(1)} |

 |  | 3 ​ S 90 3S_{90}, 3 ​ S 95 3S_{95} | 6 ​ S 97 6S_{97}, 6 ​ S 103 6S_{103} |  |  | 3 ​ S 104 ( 1) 3S_{104}^{(1)}, 3 ​ S 105 ( 1) 3S_{105}^{(1)}, 6 ​ S 108 ( 1) 6S_{108}^{(1)}, 6 ​ S 109 ( 1) 6S_{109}^{(1)} |

Table 13: Topological equivalences for the family 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) \bf{Q}{{\widehat{ES}(A)}} (cont.)

Presented | Identical | Finite | Finite | Finite | Possessing |  |

phase | under | antisaddle | antisaddle | weak | invariant curve | Other reasons |

portrait | perturbations | focus | node–focus | point | (no separatrix) |  |

V 235 V_{235} | V 254 V_{254} |  |  |  |  | V 272 ( 1) V_{272}^{(1)}, V 277 ( 1) V_{277}^{(1)} |

V 238 V_{238} | V 257 V_{257} | V 236 V_{236}, V 237 V_{237} |  |  |  | V 271 ( 1) V_{271}^{(1)}, V 278 ( 1) V_{278}^{(1)} |

 | V 255 V_{255}, V 256 V_{256} |  |  |  | V 279 ( 1) V_{279}^{(1)}, V 280 ( 1) V_{280}^{(1)} |

 |  | 3 ​ S 91 3S_{91}, 3 ​ S 96 3S_{96} | 6 ​ S 98 6S_{98}, 6 ​ S 104 6S_{104} |  |  | 3 ​ S 103 ( 1) 3S_{103}^{(1)}, 6 ​ S 116 ( 1) 6S_{116}^{(1)} |

V 240 V_{240} | V 241 V_{241}, V 242 V_{242}, V 244 V_{244}, V 245 V_{245} | V 239 V_{239}, V 243 V_{243} |  |  |  |  |

V 246 V_{246}, V 247 V_{247}, V 248 V_{248}, V 249 V_{249} | V 260 V_{260}, V 262 V_{262} |  |  |  |  |

V 250 V_{250}, V 251 V_{251}, V 258 V_{258}, V 259 V_{259} | V 270 V_{270}, V 282 V_{282} |  |  |  |  |

V 261 V_{261}, V 263 V_{263}, V 264 V_{264}, V 265 V_{265} | V 283 V_{283} |  |  |  |  |

V 266 V_{266}, V 267 V_{267}, V 268 V_{268}, V 269 V_{269} |  |  |  |  |  |

V 281 V_{281}, V 284 V_{284}, V 285 V_{285}, V 286 V_{286} |  |  |  |  |  |

V 287 V_{287}, V 288 V_{288} |  |  |  |  |  |

 |  | 3 ​ S 92 3S_{92}, 3 ​ S 97 3S_{97} | 6 ​ S 99 6S_{99}, 6 ​ S 100 6S_{100}, 6 ​ S 101 6S_{101}, 6 ​ S 102 6S_{102} | 3 ​ S 93 3S_{93}, 3 ​ S 94 3S_{94} | 4 ​ S 83 4S_{83}, 4 ​ S 84 4S_{84}, 4 ​ S 85 4S_{85}, 4 ​ S 86 4S_{86} |  |

 |  |  | 6 ​ S 105 6S_{105}, 6 ​ S 106 6S_{106}, 6 ​ S 107 6S_{107}, 6 ​ S 110 6S_{110} | 3 ​ S 98 3S_{98}, 3 ​ S 99 3S_{99} | 4 ​ S 87 4S_{87}, 4 ​ S 88 4S_{88}, 4 ​ S 89 4S_{89}, 4 ​ S 90 4S_{90} |  |

 |  |  | 6 ​ S 111 6S_{111}, 6 ​ S 112 6S_{112}, 6 ​ S 113 6S_{113}, 6 ​ S 114 6S_{114} | 3 ​ S 100 3S_{100}, 3 ​ S 101 3S_{101} | 4 ​ S 91 4S_{91}, 4 ​ S 92 4S_{92}, 4 ​ S 93 4S_{93}, 4 ​ S 94 4S_{94} |  |

 |  |  | 6 ​ S 115 6S_{115}, 6 ​ S 117 6S_{117} | 3 ​ S 102 3S_{102} | 4 ​ S 95 4S_{95}, 4 ​ S 96 4S_{96}, 4 ​ S 97 4S_{97}, 4 ​ S 98 4S_{98} |  |

 |  |  |  |  | 4 ​ S 99 4S_{99}, 8 ​ S 100 8S_{100}, 8 ​ S 101 8S_{101}, 8 ​ S 102 8S_{102} |  |

 |  |  |  |  | 8 ​ S 106 8S_{106}, 8 ​ S 107 8S_{107}, 8 ​ S 108 8S_{108}, 8 ​ S 109 8S_{109} |  |

 |  |  |  |  | 8 ​ S 110 8S_{110}, 8 ​ S 111 8S_{111} |  |

 |  |  | 3.6 ​ L 27 3.6L_{27}, 3.6 ​ L 28 3.6L_{28}, 3.6 ​ L 29 3.6L_{29} | 3.4 ​ L 23 3.4L_{23}, 3.4 ​ L 24 3.4L_{24} | 4.8 ​ L 30 4.8L_{30}, 4.8 ​ L 31 4.8L_{31}, 4.8 ​ L 32 4.8L_{32} |  |

 |  |  | 4.6 ​ L 33 4.6L_{33}, 4.6 ​ L 34 4.6L_{34}, 4.6 ​ L 35 4.6L_{35} | 3.4 ​ L 25 3.4L_{25} | 4.8 ​ L 33 4.8L_{33}, 4.8 ​ L 34 4.8L_{34} |  |

 |  |  | 4.6 ​ L 36 4.6L_{36}, 6.8 ​ L 37 6.8L_{37}, 6.8 ​ L 40 6.8L_{40} |  |  |  |

 |  |  | 6.8 ​ L 41 6.8L_{41} |  |  |  |

Table 14: Topological equivalences for the family 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) \bf{Q}{{\widehat{ES}(A)}} (cont.)

Presented | Identical | Finite | Finite | Finite | Possessing |  |

phase | under | antisaddle | antisaddle | weak | invariant curve | Other reasons |

portrait | perturbations | focus | node–focus | point | (no separatrix) |  |

2 ​ S 1 2S_{1} | 2 ​ S 2 2S_{2}, 2 ​ S 3 2S_{3} |  |  |  |  |  |

 |  |  |  | 2.3 ​ L 1 2.3L_{1} | 2.8 ​ L 1 2.8L_{1} |  |

2 ​ S 4 2S_{4} | 2 ​ S 8 2S_{8} |  |  |  |  |  |

 |  |  |  | 2.3 ​ L 3 2.3L_{3} |  |  |

2 ​ S 5 2S_{5} | 2 ​ S 9 2S_{9} |  |  |  |  |  |

 |  |  |  | 2.3 ​ L 5 2.3L_{5} |  |  |

2 ​ S 6 2S_{6} | 2 ​ S 7 2S_{7}, 2 ​ S 10 2S_{10} |  |  |  |  |  |

 |  |  |  | 2.3 ​ L 6 2.3L_{6} | 2.4 ​ L 2 2.4L_{2} |  |

2 ​ S 11 2S_{11} |  |  |  |  |  |  |

 |  |  |  |  |  | 0.2 ​ L 1 ( 2) 0.2L_{1}^{(2)} |

2 ​ S 12 2S_{12} |  |  |  |  |  |  |

 |  |  |  |  |  | 0.2 ​ L 2 ( 2) 0.2L_{2}^{(2)} |

2 ​ S 13 2S_{13} | 2 ​ S 14 2S_{14}, 2 ​ S 15 2S_{15}, 2 ​ S 21 2S_{21} | 2 ​ S 16 2S_{16}, 2 ​ S 22 2S_{22} |  |  |  |  |

 |  | 0.2 ​ L 4 0.2L_{4}, 2.8 ​ L 7 2.8L_{7} | 2.6 ​ L 1 2.6L_{1}, 2.6 ​ L 3 2.6L_{3} |  | 2.8 ​ L 4 2.8L_{4}, 2.8 ​ L 5 2.8L_{5}, 2.8 ​ L 6 2.8L_{6} | 0.2 ​ L 3 ( 2) 0.2L_{3}^{(2)} |

 |  |  | P 23 P_{23} |  | P 13 P_{13} |  |

2 ​ S 17 2S_{17} |  |  |  |  |  |  |

 |  |  |  |  |  | 0.2 ​ L 5 ( 2) 0.2L_{5}^{(2)} |

2 ​ S 18 2S_{18} |  |  |  |  |  |  |

 |  |  |  |  |  | 0.2 ​ L 6 ( 2) 0.2L_{6}^{(2)} |

2 ​ S 20 2S_{20} | 2 ​ S 19 2S_{19} |  |  |  |  |  |

 |  | 0.2 ​ L 7 0.2L_{7}, 2.3 ​ L 8 2.3L_{8} | 2.6 ​ L 2 2.6L_{2} |  |  | 0.2 ​ L 8 ( 2) 0.2L_{8}^{(2)} |

 |  | P 26 P_{26} | P 27 P_{27} |  |  |  |

2 ​ S 23 2S_{23} |  |  |  |  |  |  |

2 ​ S 24 2S_{24} |  |  |  |  |  |  |

2 ​ S 25 2S_{25} |  |  |  |  |  |  |

2 ​ S 26 2S_{26} |  | 2 ​ S 27 2S_{27} |  |  |  |  |

 |  |  | 2.6 ​ L 4 2.6L_{4} |  |  |  |

Table 15: Topological equivalences for the family 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) \bf{Q}{{\widehat{ES}(A)}} (cont.)

Presented | Identical | Finite | Finite | Finite | Possessing |  |

phase | under | antisaddle | antisaddle | weak | invariant curve | Other reasons |

portrait | perturbations | focus | node–focus | point | (no separatrix) |  |

2 ​ S 28 2S_{28} |  |  |  |  |  |  |

2 ​ S 29 2S_{29} |  |  |  |  |  |  |

2 ​ S 30 2S_{30} |  |  |  |  |  |  |

2 ​ S 32 2S_{32} |  | 2 ​ S 31 2S_{31} |  |  |  |  |

 |  | 2.3 ​ L 10 2.3L_{10} | 2.6 ​ L 5 2.6L_{5} |  |  |  |

2 ​ S 33 2S_{33} |  |  |  |  |  |  |

2 ​ S 34 2S_{34} |  |  |  |  |  |  |

2 ​ S 35 2S_{35} | 2 ​ S 36 2S_{36}, 2 ​ S 37 2S_{37} | 2 ​ S 38 2S_{38} |  |  |  |  |

 |  |  | 2.6 ​ L 6 2.6L_{6} |  | 2.4 ​ L 8 2.4L_{8}, 2.4 ​ L 9 2.4L_{9} |  |

2 ​ S 39 2S_{39} |  |  |  |  |  |  |

2 ​ S 40 2S_{40} |  |  |  |  |  |  |

2 ​ S 42 2S_{42} |  | 2 ​ S 41 2S_{41} |  |  |  |  |

 |  | 2.3 ​ L 12 2.3L_{12} | 2.6 ​ L 7 2.6L_{7} |  |  |  |

4 ​ S 5 4S_{5} | 4 ​ S 8 4S_{8}, 4 ​ S 21 4S_{21} | 4 ​ S 6 4S_{6}, 4 ​ S 9 4S_{9}, 4 ​ S 25 4S_{25} |  |  |  | 4 ​ S 10 ( 1) 4S_{10}^{(1)}, 4 ​ S 11 ( 1) 4S_{11}^{(1)}, 4 ​ S 24 ( 1) 4S_{24}^{(1)}, 4 ​ S 27 ( 1) 4S_{27}^{(1)} |

4 ​ S 23 4S_{23} | 4 ​ S 26 4S_{26}, 4 ​ S 29 4S_{29}, 4 ​ S 31 4S_{31} |  |  |  | 4 ​ S 30 ( 1) 4S_{30}^{(1)} |

 |  | 3.4 ​ L 8 3.4L_{8}, 3.4 ​ L 9 3.4L_{9} | 4.6 ​ L 2 4.6L_{2}, 4.6 ​ L 6 4.6L_{6} | 3.4 ​ L 5 3.4L_{5}, 3.4 ​ L 6 3.4L_{6} |  | 3.4 ​ L 7 ( 1) 3.4L_{7}^{(1)}, 3.4 ​ L 10 ( 1) 3.4L_{10}^{(1)}, 3.4 ​ L 13 ( 1) 3.4L_{13}^{(1)} |

 |  | 3.4 ​ L 11 3.4L_{11}, 3.4 ​ L 12 3.4L_{12} | 4.6 ​ L 8 4.6L_{8}, 4.6 ​ L 9 4.6L_{9} |  |  | 4.6 ​ L 4 ( 1) 4.6L_{4}^{(1)}, 4.6 ​ L 10 ( 1) 4.6L_{10}^{(1)} |

 |  |  | P 2 P_{2}, P 3 P_{3} |  |  | P 4 ( 1) P_{4}^{(1)} |

4 ​ S 34 4S_{34} | 4 ​ S 40 4S_{40} | 4 ​ S 32 4S_{32}, 4 ​ S 33 4S_{33}, 4 ​ S 38 4S_{38}, 4 ​ S 39 4S_{39} |  |  |  | 4 ​ S 47 ( 1) 4S_{47}^{(1)}, 4 ​ S 48 ( 1) 4S_{48}^{(1)}, 4 ​ S 49 ( 1) 4S_{49}^{(1)}, 4 ​ S 50 ( 1) 4S_{50}^{(1)} |

 |  | 0.4 ​ L 1 0.4L_{1}, 0.4 ​ L 2 0.4L_{2}, 0.4 ​ L 5 0.4L_{5} | 4.6 ​ L 11 4.6L_{11} |  |  | 0.4 ​ L 3 ( 2) 0.4L_{3}^{(2)}, 0.4 ​ L 7 ( 2) 0.4L_{7}^{(2)}, 0.4 ​ L 10 ( 1) 0.4L_{10}^{(1)} |

 |  | 0.4 ​ L 6 0.4L_{6}, 3.4 ​ L 14 3.4L_{14}, 3.4 ​ L 16 3.4L_{16} |  |  |  | 0.4 ​ L 11 ( 1) 0.4L_{11}^{(1)}, 0.4 ​ L 12 ( 1) 0.4L_{12}^{(1)}, 0.4 ​ L 13 ( 1) 0.4L_{13}^{(1)} |

 |  | 4.6 ​ L 13 4.6L_{13} |  |  |  | 3.4 ​ L 15 ( 1) 3.4L_{15}^{(1)}, 4.6 ​ L 16 ( 1) 4.6L_{16}^{(1)} |

 |  | P 28 P_{28}, P 31 P_{31} | P 29 P_{29}, P 32 P_{32} |  |  | P 34 ( 1) P_{34}^{(1)}, P 35 ( 1) P_{35}^{(1)} |

Table 16: Topological equivalences for the family 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) \bf{Q}{{\widehat{ES}(A)}} (cont.)

Presented | Identical | Finite | Finite | Finite | Possessing |  |

phase | under | antisaddle | antisaddle | weak | invariant curve | Other reasons |

portrait | perturbations | focus | node–focus | point | (no separatrix) |  |

4 ​ S 59 4S_{59} | 4 ​ S 60 4S_{60}, 4 ​ S 65 4S_{65}, 4 ​ S 66 4S_{66}, 4 ​ S 76 4S_{76} | 4 ​ S 57 4S_{57}, 4 ​ S 58 4S_{58} |  |  |  | 4 ​ S 71 ( 1) 4S_{71}^{(1)}, 4 ​ S 72 ( 1) 4S_{72}^{(1)}, 4 ​ S 73 ( 1) 4S_{73}^{(1)}, 4 ​ S 74 ( 1) 4S_{74}^{(1)} |

4 ​ S 78 4S_{78}, 4 ​ S 79 4S_{79}, 4 ​ S 81 4S_{81} | 4 ​ S 63 4S_{63}, 4 ​ S 64 4S_{64} |  |  |  | 4 ​ S 75 ( 1) 4S_{75}^{(1)}, 4 ​ S 77 ( 1) 4S_{77}^{(1)}, 4 ​ S 80 ( 1) 4S_{80}^{(1)}, 4 ​ S 82 ( 1) 4S_{82}^{(1)} |

 |  | 3.4 ​ L 17 3.4L_{17}, 3.4 ​ L 19 3.4L_{19} | 4.6 ​ L 20 4.6L_{20}, 4.6 ​ L 22 4.6L_{22} | 3.4 ​ L 20 3.4L_{20}, 3.4 ​ L 22 3.4L_{22} | 4.8 ​ L 22 4.8L_{22}, 4.8 ​ L 25 4.8L_{25} | 3.4 ​ L 18 ( 1) 3.4L_{18}^{(1)}, 3.4 ​ L 21 ( 1) 3.4L_{21}^{(1)}, 4.6 ​ L 25 ( 1) 4.6L_{25}^{(1)} |

 |  |  | 4.6 ​ L 26 4.6L_{26}, 4.6 ​ L 28 4.6L_{28} |  | 4.8 ​ L 27 4.8L_{27}, 4.8 ​ L 29 4.8L_{29} | 4.6 ​ L 27 ( 1) 4.6L_{27}^{(1)}, 4.6 ​ L 30 ( 1) 4.6L_{30}^{(1)}, 4.6 ​ L 32 ( 1) 4.6L_{32}^{(1)} |

 |  |  | 4.6 ​ L 29 4.6L_{29}, 4.6 ​ L 31 4.6L_{31} |  |  | 4.8 ​ L 24 ( 1) 4.8L_{24}^{(1)}, 4.8 ​ L 28 ( 1) 4.8L_{28}^{(1)} |

 |  |  | P 36 P_{36}, P 38 P_{38}, P 39 P_{39}, P 41 P_{41} |  |  | P 37 ( 1) P_{37}^{(1)}, P 40 ( 1) P_{40}^{(1)} |

5 ​ S 1 5S_{1} | 5 ​ S 13 5S_{13} | 5 ​ S 2 5S_{2}, 5 ​ S 14 5S_{14} |  |  |  | 5 ​ S 29 ( 1) 5S_{29}^{(1)}, 5 ​ S 30 ( 1) 5S_{30}^{(1)}, 5 ​ S 31 ( 1) 5S_{31}^{(1)}, 5 ​ S 32 ( 1) 5S_{32}^{(1)} |

 |  | 3.5 ​ L 1 3.5L_{1}, 3.5 ​ L 5 3.5L_{5} | 5.6 ​ L 1 5.6L_{1}, 5.6 ​ L 6 5.6L_{6} |  |  | 3.5 ​ L 12 ( 1) 3.5L_{12}^{(1)}, 3.5 ​ L 13 ( 1) 3.5L_{13}^{(1)}, 5.6 ​ L 11 ( 1) 5.6L_{11}^{(1)} |

 |  |  |  |  |  | 5.6 ​ L 12 ( 1) 5.6L_{12}^{(1)} |

5 ​ S 3 5S_{3} | 5 ​ S 15 5S_{15} |  |  |  |  | 5 ​ S 28 ( 1) 5S_{28}^{(1)}, 5 ​ S 33 ( 1) 5S_{33}^{(1)} |

5 ​ S 6 5S_{6} | 5 ​ S 18 5S_{18} | 5 ​ S 4 5S_{4}, 5 ​ S 5 5S_{5} |  |  |  | 5 ​ S 27 ( 1) 5S_{27}^{(1)}, 5 ​ S 34 ( 1) 5S_{34}^{(1)}, 5 ​ S 35 ( 1) 5S_{35}^{(1)}, 5 ​ S 36 ( 1) 5S_{36}^{(1)} |

 | 5 ​ S 16 5S_{16}, 5 ​ S 17 5S_{17} |  |  |  |  |

 |  | 3.5 ​ L 2 3.5L_{2}, 3.5 ​ L 6 3.5L_{6} |  |  |  | 3.5 ​ L 11 ( 1) 3.5L_{11}^{(1)}, 5.6 ​ L 17 ( 1) 5.6L_{17}^{(1)} |

 |  | 5.6 ​ L 2 5.6L_{2}, 5.6 ​ L 7 5.6L_{7} |  |  |  |  |

5 ​ S 9 5S_{9} | 5 ​ S 10 5S_{10}, 5 ​ S 11 5S_{11}, 5 ​ S 12 5S_{12}, 5 ​ S 19 5S_{19} | 5 ​ S 7 5S_{7}, 5 ​ S 8 5S_{8} |  |  |  | 5 ​ S 26 ( 1) 5S_{26}^{(1)}, 5 ​ S 37 ( 1) 5S_{37}^{(1)}, 5 ​ S 38 ( 1) 5S_{38}^{(1)}, 5 ​ S 39 ( 1) 5S_{39}^{(1)} |

5 ​ S 20 5S_{20}, 5 ​ S 22 5S_{22}, 5 ​ S 24 5S_{24}, 5 ​ S 25 5S_{25} | 5 ​ S 21 5S_{21}, 5 ​ S 23 5S_{23} |  |  |  | 5 ​ S 40 ( 1) 5S_{40}^{(1)}, 5 ​ S 41 ( 1) 5S_{41}^{(1)}, 5 ​ S 42 ( 1) 5S_{42}^{(1)} |

 |  | 3.5 ​ L 3 3.5L_{3}, 3.5 ​ L 7 3.5L_{7} | 5.6 ​ L 3 5.6L_{3}, 5.6 ​ L 4 5.6L_{4} | 3.5 ​ L 4 3.5L_{4}, 3.5 ​ L 8 3.5L_{8} | 5.8 ​ L 4 5.8L_{4}, 5.8 ​ L 5 5.8L_{5} | 3.5 ​ L 9 ( 1) 3.5L_{9}^{(1)}, 3.5 ​ L 10 ( 1) 3.5L_{10}^{(1)}, 5.6 ​ L 13 ( 1) 5.6L_{13}^{(1)} |

 |  |  | 5.6 ​ L 5 5.6L_{5}, 5.6 ​ L 8 5.6L_{8} |  | 5.8 ​ L 9 5.8L_{9}, 5.8 ​ L 10 5.8L_{10} | 5.6 ​ L 14 ( 1) 5.6L_{14}^{(1)}, 5.6 ​ L 15 ( 1) 5.6L_{15}^{(1)}, 5.6 ​ L 16 ( 1) 5.6L_{16}^{(1)} |

 |  |  | 5.6 ​ L 9 5.6L_{9}, 5.6 ​ L 10 5.6L_{10} |  |  | 5.8 ​ L 11 ( 1) 5.8L_{11}^{(1)}, 5.8 ​ L 12 ( 1) 5.8L_{12}^{(1)} |

 |  |  | P 51 P_{51}, P 52 P_{52} | P 56 P_{56}, P 57 P_{57} |  | P 59 ( 1) P_{59}^{(1)}, P 60 ( 1) P_{60}^{(1)} |

7 ​ S 1 7S_{1} | 7 ​ S 2 7S_{2} |  |  |  |  | 7 ​ S 3 ( 1) 7S_{3}^{(1)} |

7 ​ S 4 7S_{4} | 7 ​ S 5 7S_{5} |  |  |  |  | 7 ​ S 6 ( 1) 7S_{6}^{(1)} |

Table 17: Topological equivalences for the family 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) \bf{Q}{{\widehat{ES}(A)}} (cont.)

Presented | Identical | Finite | Finite | Finite | Possessing |  |

phase | under | antisaddle | antisaddle | weak | invariant curve | Other reasons |

portrait | perturbations | focus | node–focus | point | (no separatrix) |  |

7 ​ S 7 7S_{7} | 7 ​ S 8 7S_{8} |  |  |  |  | 7 ​ S 9 ( 1) 7S_{9}^{(1)}, 7 ​ S 10 ( 1) 7S_{10}^{(1)} |

 |  |  |  |  |  | 0.7 ​ L 1 ( 2) 0.7L_{1}^{(2)}, 0.7 ​ L 2 ( 2) 0.7L_{2}^{(2)} |

 |  |  |  |  |  | 0.7 ​ L 3 ( 1) 0.7L_{3}^{(1)}, 0.7 ​ L 4 ( 1) 0.7L_{4}^{(1)} |

7 ​ S 11 7S_{11} | 7 ​ S 12 7S_{12} |  |  |  |  | 7 ​ S 13 ( 1) 7S_{13}^{(1)}, 7 ​ S 14 ( 1) 7S_{14}^{(1)} |

7 ​ S 15 7S_{15} | 7 ​ S 16 7S_{16} |  |  |  |  | 7 ​ S 17 ( 1) 7S_{17}^{(1)}, 7 ​ S 18 ( 1) 7S_{18}^{(1)} |

8 ​ S 7 8S_{7} | 8 ​ S 14 8S_{14}, 8 ​ S 24 8S_{24} | 8 ​ S 5 8S_{5}, 8 ​ S 6 8S_{6}, 8 ​ S 15 8S_{15} |  |  |  | 8 ​ S 17 ( 1) 8S_{17}^{(1)}, 8 ​ S 18 ( 1) 8S_{18}^{(1)}, 8 ​ S 19 ( 1) 8S_{19}^{(1)} |

8 ​ S 25 8S_{25} | 8 ​ S 16 8S_{16}, 8 ​ S 21 8S_{21}, 8 ​ S 22 8S_{22} |  |  |  | 8 ​ S 23 ( 1) 8S_{23}^{(1)}, 8 ​ S 26 ( 1) 8S_{26}^{(1)} |

 |  | 3.8 ​ L 1 3.8L_{1}, 3.8 ​ L 2 3.8L_{2} | 6.8 ​ L 1 6.8L_{1}, 6.8 ​ L 4 6.8L_{4} | 3.8 ​ L 7 3.8L_{7}, 3.8 ​ L 8 3.8L_{8} |  | 3.8 ​ L 3 ( 1) 3.8L_{3}^{(1)}, 3.8 ​ L 6 ( 1) 3.8L_{6}^{(1)}, 3.8 ​ L 9 ( 1) 3.8L_{9}^{(1)} |

 |  | 3.8 ​ L 4 3.8L_{4}, 3.8 ​ L 5 3.8L_{5} | 6.8 ​ L 7 6.8L_{7}, 6.8 ​ L 8 6.8L_{8} |  |  | 6.8 ​ L 6 ( 1) 6.8L_{6}^{(1)}, 6.8 ​ L 9 ( 1) 6.8L_{9}^{(1)} |

 |  |  | P 8 P_{8}, P 9 P_{9} |  |  | P 10 ( 1) P_{10}^{(1)} |

8 ​ S 77 8S_{77} | 8 ​ S 83 8S_{83} | 8 ​ S 75 8S_{75}, 8 ​ S 76 8S_{76} |  |  |  | 8 ​ S 90 ( 1) 8S_{90}^{(1)}, 8 ​ S 91 ( 1) 8S_{91}^{(1)} |

 | 8 ​ S 81 8S_{81}, 8 ​ S 82 8S_{82} |  |  |  | 8 ​ S 92 ( 1) 8S_{92}^{(1)}, 8 ​ S 93 ( 1) 8S_{93}^{(1)} |

 |  | 3.8 ​ L 23 3.8L_{23}, 3.8 ​ L 25 3.8L_{25} | 6.8 ​ L 28 6.8L_{28} |  |  | 3.8 ​ L 24 ( 1) 3.8L_{24}^{(1)}, 6.8 ​ L 33 ( 1) 6.8L_{33}^{(1)} |

 |  | 6.8 ​ L 30 6.8L_{30} |  |  |  |  |

8 ​ S 99 8S_{99} | 8 ​ S 105 8S_{105} | 8 ​ S 97 8S_{97}, 8 ​ S 98 8S_{98} |  |  |  | 8 ​ S 103 ( 1) 8S_{103}^{(1)}, 8 ​ S 112 ( 1) 8S_{112}^{(1)}, 8 ​ S 113 ( 1) 8S_{113}^{(1)} |

 | 8 ​ S 104 8S_{104} |  |  |  | 8 ​ S 114 ( 1) 8S_{114}^{(1)}, 8 ​ S 115 ( 1) 8S_{115}^{(1)} |

 |  | 3.8 ​ L 26 3.8L_{26}, 3.8 ​ L 27 3.8L_{27} | 6.8 ​ L 38 6.8L_{38}, 6.8 ​ L 39 6.8L_{39} |  |  | 3.8 ​ L 28 ( 1) 3.8L_{28}^{(1)}, 6.8 ​ L 42 ( 1) 6.8L_{42}^{(1)} |

2.3 ​ L 2 2.3L_{2} | 2.3 ​ L 4 2.3L_{4} |  |  |  |  |  |

 |  |  |  | P 6 P_{6} |  |  |

2.3 ​ L 7 2.3L_{7} |  |  |  |  |  |  |

 |  |  | P 21 P_{21} |  |  |  |

2.3 ​ L 9 2.3L_{9} |  |  |  |  |  |  |

2.3 ​ L 11 2.3L_{11} |  |  |  |  |  |  |

2.4 ​ L 1 2.4L_{1} | 2.4 ​ L 3 2.4L_{3} |  |  |  |  |  |

 |  |  |  | P 1 P_{1} |  |  |

2.4 ​ L 4 2.4L_{4} |  |  |  |  |  |  |

 |  |  |  |  | P 22 P_{22} |  |

Table 18: Topological equivalences for the family 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) \bf{Q}{{\widehat{ES}(A)}} (cont.)

Presented | Identical | Finite | Finite | Finite | Possessing |  |

phase | under | antisaddle | antisaddle | weak | invariant curve | Other reasons |

portrait | perturbations | focus | node–focus | point | (no separatrix) |  |

2.4 ​ L 5 2.4L_{5} |  |  |  |  |  |  |

 |  |  |  |  | P 24 P_{24} |  |

2.4 ​ L 6 2.4L_{6} |  |  |  |  |  |  |

2.4 ​ L 7 2.4L_{7} |  |  |  |  |  |  |

2.5 ​ L 1 2.5L_{1} |  |  |  |  |  |  |

2.5 ​ L 2 2.5L_{2} |  |  |  |  |  |  |

2.5 ​ L 3 2.5L_{3} |  |  |  |  |  |  |

2.5 ​ L 4 2.5L_{4} |  |  |  |  |  |  |

2.5 ​ L 5 2.5L_{5} |  |  |  |  |  |  |

2.5 ​ L 6 2.5L_{6} |  |  |  |  |  |  |

2.5 ​ L 8 2.5L_{8} |  | 2.5 ​ L 7 2.5L_{7} |  |  |  |  |

 |  | P 47 P_{47} | P 48 P_{48} |  |  |  |

2.7 ​ L 1 2.7L_{1} |  |  |  |  |  |  |

 |  | P 25 P_{25} |  |  |  |  |

2.7 ​ L 2 2.7L_{2} |  |  |  |  |  |  |

2.7 ​ L 3 2.7L_{3} |  |  |  |  |  |  |

2.8 ​ L 2 2.8L_{2} | 2.8 ​ L 3 2.8L_{3} |  |  |  |  |  |

 |  |  |  |  | P 11 P_{11} |  |

2.8 ​ L 8 2.8L_{8} |  |  |  |  |  |  |

2.8 ​ L 9 2.8L_{9} |  |  |  |  |  |  |

2.8 ​ L 10 2.8L_{10} |  |  |  |  |  |  |

2.8 ​ L 11 2.8L_{11} |  |  |  |  |  |  |

3.7 ​ L 1 3.7L_{1} | 3.7 ​ L 2 3.7L_{2} |  |  |  |  | 3.7 ​ L 3 ( 1) 3.7L_{3}^{(1)} |

4.5 ​ L 1 4.5L_{1} | 4.5 ​ L 2 4.5L_{2}, 4.5 ​ L 3 4.5L_{3} |  |  |  |  |  |

 |  |  |  | P 53 P_{53}, P 58 P_{58} |  |  |

4.8 ​ L 2 4.8L_{2} | 4.8 ​ L 5 4.8L_{5}, 4.8 ​ L 7 4.8L_{7}, 4.8 ​ L 8 4.8L_{8} |  |  |  |  |  |

 |  |  |  | P 5 P_{5}, P 7 P_{7} |  |  |

5.7 ​ L 1 5.7L_{1} | 5.7 ​ L 2 5.7L_{2} |  |  |  |  | 5.7 ​ L 3 ( 1) 5.7L_{3}^{(1)}, 5.7 ​ L 4 ( 1) 5.7L_{4}^{(1)} |

Table 19: Topological equivalences for the family 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) \bf{Q}{{\widehat{ES}(A)}} (cont.)

Presented | Identical | Finite | Finite | Finite | Possessing |  |

phase | under | antisaddle | antisaddle | weak | invariant curve | Other reasons |

portrait | perturbations | focus | node–focus | point | (no separatrix) |  |

5.8 ​ L 3 5.8L_{3} | 5.8 ​ L 8 5.8L_{8} | 5.8 ​ L 1 5.8L_{1}, 5.8 ​ L 2 5.8L_{2} |  |  |  | 5.8 ​ L 13 ( 1) 5.8L_{13}^{(1)}, 5.8 ​ L 14 ( 1) 5.8L_{14}^{(1)} |

 | 5.8 ​ L 6 5.8L_{6}, 5.8 ​ L 7 5.8L_{7} |  |  |  | 5.8 ​ L 15 ( 1) 5.8L_{15}^{(1)}, 5.8 ​ L 16 ( 1) 5.8L_{16}^{(1)} |

 |  | P 49 P_{49}, P 54 P_{54} | P 50 P_{50}, P 55 P_{55} |  |  | P 61 ( 1) P_{61}^{(1)}, P 62 ( 1) P_{62}^{(1)} |

P 42 P_{42} |  |  |  |  |  |  |

P 43 P_{43} |  |  |  |  |  |  |

P 44 P_{44} |  |  |  |  |  |  |

P 45 P_{45} |  |  |  |  |  |  |

P 46 P_{46} |  |  |  |  |  |  |

### 3.2 The bifurcation diagram of family 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) \bf{Q}{{\widehat{ES}(B)}}

In this section we present the study of the bifurcation diagram of family 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) \bf{Q}{{\widehat{ES}(B)}}, described by systems ( 9).

From normal form ( 9) we observe that the family under consideration depends on the parameters g ∈ ℝ ∖ { 0 } g\in\mathbb{R}\setminus\{0\} (in order to have nondegenerate systems), u ∈ ℝ + ∪ { 0 } u\in\mathbb{R}^{+}\cup\{0\} (due to the symmetry we proved before), and ℓ ∈ ℝ \ell\in\mathbb{R}. Here we shall consider the bifurcation diagram formed by planes g = g 0 g=g_{0} in which the Cartesian coordinates are ( u, ℓ) (u,\ell) with u ≥ 0 u\geq 0.

For systems ( 9), computations show that

 | 𝐃 = 12288 ​ g 6 ​ ( 1 + u 2) 4, 𝐑 = 48 ​ g 4 ​ ( 1 + u 2) 2 ​ x 2, \mathbf{D}=12288g^{6}(1+u^{2})^{4},\quad\mathbf{R}=48g^{4}(1+u^{2})^{2}x^{2}, |  |

therefore by [6, Table 5.1], for g ≠ 0 g\neq 0 systems ( 9) possess exactly one real simple finite singular point and two complex ones.

###### Remark 8.

In order to avoid unnecessary repetitions, along this section we shall omit most of the explanations similar to the ones already presented previously along the study of family ( 5).

Now we present the value of the algebraic invariants and T–comitants (with respect to systems ( 9)) which are relevant in our study.

Bifurcation surface in ℝ 3 \mathbb{R}^{3} due to degeneracy of the system

For family 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) \bf{Q}{{\widehat{ES}(B)}} we calculate

 | μ 0 = 0 and μ 1 = 4 ​ g 2 ​ ( 1 + u 2) ​ x, \mu_{0}=0\quad\text{ and }\quad\mu_{1}=4g^{2}(1+u^{2})x, |  |

and it is clear that the comitant μ 1 \mu_{1} vanishes if and only if g = 0 g=0. Moreover, computation show that

 | μ 2 | g = 0 = μ 3 | g = 0 = μ 4 | g = 0 = 0, \mu_{2}|_{g=0}=\mu_{3}|_{g=0}=\mu_{4}|_{g=0}=0, |  |

i.e., along the surface

 | ( 𝒮 1): g = 0, ({\cal S}_{1})\!:g=0, |  |

in fact, a plane, we have degenerate systems.

###### Remark 9.

Family 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) \bf{Q}{{\widehat{ES}(B)}} restricted to surface ( 𝒮 1) ({\cal S}_{1}) is given by

 |  | x ′ = 0, \displaystyle x^{\prime}=0, |  |

 |  | y ′ = 2 ​ ( 1 − ℓ ​ u) ​ x + ℓ ⁡ ( 1 + u 2) ​ y + ℓ ​ x 2 − 2 ​ x ​ y, \displaystyle y^{\prime}=2(1-\ell u)x+\ell(1+u^{2})y+\ell x^{2}-2xy, |  |

and, as we mentioned before, this two–parametric family has curves filled up with singular points. According to [6, Diagram 12.1], for these systems we calculate

 | η = 0, M ~ = − 32 ​ x 2, κ = K ~ = L ~ = κ 1 = K 1 = 0, \eta=0,\quad\widetilde{M}=-32x^{2},\quad\kappa=\widetilde{K}=\widetilde{L}=\kappa_{1}={K}_{1}=0, |  |

and

 | L 2 = − 6 ​ ℓ ​ ( 1 + u 2) ​ [4 + ℓ ⁡ ( ℓ − 4 ​ u + ℓ ​ u 2)] ​ x 4. {L}_{2}=-6\ell(1+u^{2})\left[4+\ell(\ell-4u+\ell u^{2})\right]x^{4}. |  |

Since the discriminant of 4 + ℓ ⁡ ( ℓ − 4 ​ u + ℓ ​ u 2) 4+\ell(\ell-4u+\ell u^{2}) is negative, we point out that L 2 = 0 {L}_{2}=0 is equivalent to ℓ = 0 \ell=0. So, according to the mentioned reference, for ℓ ≠ 0 \ell\neq 0 we have a hyperbola filled up with singular points, and for ℓ = 0 \ell=0 we have two real straight lines (filled up with singular points) intersecting at a finite point. Therefore, in the plane g = 0 g=0 the straight line ℓ = 0 \ell=0 yields a bifurcation of curves filled up with singular points.

The surface of C ∞ C^{\infty} bifurcation points due to weak singularities

( 𝒮 3 {\cal S}_{3}) This is the bifurcation surface due to weak finite singularities. According to [20], for systems ( 9) we calculate

 | 𝒯 4 = \displaystyle\mathcal{T}_{4}= | 𝒯 3 = 𝒯 2 = 𝒯 1 = 0, \displaystyle\mathcal{T}_{3}=\mathcal{T}_{2}=\mathcal{T}_{1}=0, |  |

 | σ = \displaystyle\sigma= | ℓ − 2 ​ g ​ u + ℓ ​ u 2 + 2 ​ ( g − 1) ​ x, \displaystyle\ell-2gu+\ell u^{2}+2(g-1)x, |  |

then due to the results on the mentioned paper, in the case in which σ \sigma is generically nonzero, the family under consideration could possess one and only one weak singularity. Moreover as

 | ℱ 1 = \displaystyle\mathcal{F}_{1}= | 2 ​ g 2 ​ ( 1 + u 2) ​ [2 ​ ( 2 + g) ​ u − 3 ​ ℓ ​ ( 1 + u 2)], ℋ = 0, \displaystyle 2g^{2}(1+u^{2})\left[2(2+g)u-3\ell(1+u^{2})\right],\qquad\mathcal{H}=0, |  |

 | ℬ 1 = \displaystyle\mathcal{B}_{1}= | 2 ​ g 2 ​ ( 1 + u 2) ​ [2 ​ g ​ u − ℓ ⁡ ( 1 + u 2)] ​ [4 ​ g ​ ( g − 2) + ( 1 + u 2) ​ ( 4 + ℓ ⁡ ( ℓ − 4 ​ u + ℓ ​ u 2))], \displaystyle 2g^{2}(1+u^{2})\left[2gu-\ell(1+u^{2})\right]\left[4g(g-2)+(1+u^{2})\left(4+\ell(\ell-4u+\ell u^{2})\right)\right], |  |

 | ℬ 2 = \displaystyle\mathcal{B}_{2}\!= | 2 g 3 ( g − 1) 2 ( 1 + u 2) 2 [4 g 2 + ( 1 + u 2) ( 4 − 8 ℓ u + 3 ℓ 2 ( 1 + u 2)) \displaystyle 2g^{3}(g-1)^{2}(1+u^{2})^{2}\left[4g^{2}+(1+u^{2})\left(4-8\ell u+3\ell^{2}(1+u^{2})\right)\right. |  |

 |  | − 4 g ( 2 − 2 u 2 + ℓ u ( 1 + u 2))], \displaystyle\left.-4g\left(2-2u^{2}+\ell u(1+u^{2})\right)\right], |  |

assuming ℱ 1 ≠ 0 \mathcal{F}_{1}\neq 0, for family ( 9) we can obtain one weak singularity ( s ( 1) s^{(1)} or f ( 1) f^{(1)}, depending on the sign of ℬ 2 \mathcal{B}_{2}) along the surface given by ℬ 1 = 0 \mathcal{B}_{1}=0, i.e.

 | ( 𝒮 3): \displaystyle({\cal S}_{3})\!\!: | 2 ​ g 2 ​ ( 1 + u 2) ​ [2 ​ g ​ u − ℓ ⁡ ( 1 + u 2)] ​ [4 ​ g ​ ( g − 2) + ( 1 + u 2) ​ ( 4 + ℓ ⁡ ( ℓ − 4 ​ u + ℓ ​ u 2))] = 0. \displaystyle 2g^{2}(1+u^{2})\left[2gu-\ell(1+u^{2})\right]\left[4g(g-2)+(1+u^{2})\left(4+\ell(\ell-4u+\ell u^{2})\right)\right]=0. |  |

###### Remark 10.

1. 1.

We observe that, independently of x x, we have σ = 0 \sigma=0 if and only if

 | { g = 1, ℓ = 2 ​ u / ( 1 + u 2) }. \{g=1,\,\ell=2u/(1+u^{2})\}. |  |

Under these conditions, we have that μ 0 = 0 \mu_{0}=0, 𝐃 = 12288 ​ ( 1 + u 2) 4 \mathbf{D}=12288\left(1+u^{2}\right)^{4}, and 𝐑 = 48 ​ ( 1 + u 2) 2 ​ x 2 \mathbf{R}=48(1+u^{2})^{2}x^{2}. So, according to [20, item ( f 6 f_{6})– β \beta] we have one finite singular point, which is an integrable saddle. In other words, when g = 1 g=1, during the study of the curve ℓ = 2 ​ u / ( 1 + u 2) \ell=2u/(1+u^{2}) we shall always obtain a phase portrait containing one integrable saddle.

2. 2.

We just saw that in order to define surface ( 𝒮 3 {\cal S}_{3}) we considered σ ≠ 0 \sigma\neq 0 and ℱ 1 ≠ 0 \mathcal{F}_{1}\neq 0. However, according to [20, item ( e) (e)], when σ ≠ 0 \sigma\neq 0 and ℱ 1 = 0 \mathcal{F}_{1}=0 we can have either an integrable saddle or a center. As we already have obtained conditions in order to have an integrable saddle, now we analyze when we have a center. In fact, as we already have ℋ = 0 \mathcal{H}=0, from the mentioned paper we solve ℱ 1 = ℬ 1 = 0 \mathcal{F}_{1}=\mathcal{B}_{1}=0 (together with σ ≠ 0 \sigma\neq 0 and g ≠ 0 g\neq 0), and we obtain the solution

 | { u = 0, ℓ = 0 }. \{u=0,\,\ell=0\}. |  |

Also, when we compute ℬ 2 \mathcal{B}_{2} along this solution we obtain 8 ​ ( g − 1) 4 ​ g 3 8(g-1)^{4}g^{3}, which is generically negative if g < 0 g<0. Note that we must have g ≠ 1 g\neq 1, because σ | { u = 0, ℓ = 0, g = 1 } = 0 \sigma|_{\{u=0,\,\ell=0,\,g=1\}}=0.
Therefore, from [20, item ( e 4 e_{4})– β \beta], this study shows that for g < 0 g<0 we shall always find a center type singular point when we have { u = 0, ℓ = 0 } \{u=0,\,\ell=0\}.

Bifurcation surfaces in ℝ 3 \mathbb{R}^{3} due to the presence of invariant algebraic curves

( 𝒮 4 {\cal S}_{4}) This surface contains the points of the parameter space in which there appear invariant straight lines (see Lemma 3). For systems ( 9) we compute the polynomial invariant B 1 B_{1} and we define surface

 | ( 𝒮 4): \displaystyle({\cal S}_{4})\!: | − 8 ​ g 6 ​ ℓ ​ ( 1 + u 2) 5 ​ [ℓ 2 + ( 2 + g − ℓ ​ u) 2] = 0. \displaystyle-8g^{6}\ell(1+u^{2})^{5}\left[\ell^{2}+(2+g-\ell u)^{2}\right]=0. |  |

( 𝒮 8 {\cal S}_{8}) This surface contains the points of the parameter space in which there appear invariant parabolas. According to the conditions stated in Lemma 3 we define this surface by

 | ( 𝒮 8): \displaystyle({\cal S}_{8})\!: | ℓ − 2 ​ u − 2 ​ g ​ u + ℓ ​ u 2 = 0. \displaystyle\ell-2u-2gu+\ell u^{2}=0. |  |

Bifurcation surface due to multiplicities of infinite singularities

( 𝒮 5 {\cal S}_{5}) This is the bifurcation surface due to multiplicity of infinite singular points. According to [6, Lemma 5.5], for this family we calculate

 | η = 0, M ~ = − 8 ​ ( 2 + g) 2 ​ x 2, C 2 = − x 2 ​ [ℓ ​ x − ( 2 + g) ​ y], \eta=0,\quad\widetilde{M}=-8(2+g)^{2}x^{2},\quad C_{2}=-x^{2}\left[\ell x-(2+g)y\right], |  |

and we observe that along

 | ( 𝒮 5): \displaystyle(\mathcal{S}_{5})\!: | g + 2 = 0, \displaystyle g+2=0, |  |

we have a coalescence of infinite singular points. In addition, due to the mentioned result, on the plane g = − 2 g=-2 all the phase portraits corresponding to ℓ = 0 \ell=0 have the line at infinity filled up with singular points.

The surface of C ∞ C^{\infty} bifurcation due to a node becoming a focus

( 𝒮 6 {\cal S}_{6}) This surface contains the points of the parameter space where a finite node of the systems turns into a focus. According to [6, Table 6.2] we calculate μ 0 = 0, 𝐃 = 12288 ​ g 6 ​ ( 1 + u 2) 4, 𝐑 = 48 ​ g 4 ​ ( 1 + u 2) 2 ​ x 2, K ~ = − 4 ​ g ​ x 2, G 9 = 0, \mu_{0}=0,\mathbf{D}=12288g^{6}(1+u^{2})^{4},\mathbf{R}=48g^{4}(1+u^{2})^{2}x^{2},\widetilde{K}=-4gx^{2},G_{9}=0, and for the mentioned table we conclude that the invariant W 7 W_{7} is responsible for describing the node–focus bifurcation. We compute this invariant polynomial and we define surface ( 𝒮 6 {\cal S}_{6}) by the zero set of

 | 12 ​ g 6 \displaystyle 12g^{6} | ( 1 + u 2) 4 [4 g 2 u 2 − 4 g ( ℓ u − 2) ( 1 + u 2) + ℓ 2 ( 1 + u 2) 2] × \displaystyle(1+u^{2})^{4}\left[4g^{2}u^{2}-4g(\ell u-2)(1+u^{2})+\ell^{2}(1+u^{2})^{2}\right]\times |  |

 | × \displaystyle\times | [16 g ( 1 + u 2) ( 4 + 4 ℓ u − 3 ℓ 2 ( 1 + u 2)) + 64 g 3 + 16 g 4 + ( 1 + u 2) 2 ( 4 + ℓ ( ℓ − 4 u + ℓ u 2)) 2 + \displaystyle\left[16g(1+u^{2})\left(4+4\ell u-3\ell^{2}(1+u^{2})\right)+64g^{3}+16g^{4}+(1+u^{2})^{2}\left(4+\ell(\ell-4u+\ell u^{2})\right)^{2}+\right. |  |

 |  | + 8 g 2 ( ℓ 2 ( 1 + u 2) 2 + 4 ( 3 + u 2) + 12 ℓ u ( 1 + u 2))] = 0. \displaystyle\left.+8g^{2}\left(\ell^{2}(1+u^{2})^{2}+4(3+u^{2})+12\ell u(1+u^{2})\right)\right]=0. |  |

Bifurcation surface in ℝ 3 \mathbb{R}^{3} due to the infinite elliptic–saddle

( 𝒮 0 {\cal S}_{0}) Along the plane g = − 1 g=-1 the corresponding phase portraits possess an infinite singularity of the type ( 1 2) ^ ​ E − H \widehat{\!{1\choose 2}\!\!}\ E-H. Due to results on [6] we compute the comitant

 | N ~ = − 4 ​ ( g + 1) ​ x 2, \widetilde{N}=-4(g+1)x^{2}, |  |

and we define surface

 | ( 𝒮 0): g + 1 = 0. ({\cal S}_{0})\!:g+1=0. |  |

The bifurcation surfaces listed previously are all algebraic and they, except ( 𝒮 4) ({\cal S}_{4}) and ( 𝒮 8) ({\cal S}_{8}), are the bifurcation surfaces of singularities of systems ( 9) in the parameter space. We shall detect other bifurcation surface not necessarily algebraic in which the family has global connection of separatrices different from those given by ( 𝒮 4) ({\cal S}_{4}) and ( 𝒮 8) ({\cal S}_{8}). We shall name it surface ( 𝒮 7) ({\cal S}_{7}).

As in the previous sections, here we shall foliate the three–dimensional bifurcation diagram in ℝ 3 \mathbb{R}^{3} by planes g = g 0 g=g_{0}, with g 0 g_{0} constant and we shall give pictures of the resulting bifurcation diagram on these planar sections in which the Cartesian coordinates are ( u, ℓ) (u,\ell), where the horizontal line is the u u –axis and u ≥ 0 u\geq 0.

Here we also use colors to refer to the bifurcation surfaces:

1. (a)

surface ( 𝒮 3 {\cal S}_{3}) is drawn in yellow (weak singularities). We draw it as a continuous curve if the singular point is a focus or as a dashed curve if it is a saddle;

2. (b)

surface ( 𝒮 4 {\cal S}_{4}) is drawn in purple (presence of at least one invariant straight line). We draw it as a continuous curve if it implies a topological change or as a dashed curve otherwise;

3. (c)

surface ( 𝒮 6 {\cal S}_{6}) is drawn in black and dashed (an antisaddle is on the edge of turning from a node to a focus or vice versa);

4. (d)

nonalgebraic surface ( 𝒮 7 {\cal S}_{7}) is also drawn in purple (connections of separatrices);

5. (e)

surface ( 𝒮 8 {\cal S}_{8}) is drawn in cyan (presence of an invariant parabola). We draw it as a continuous curve if it implies a topological change or as a dashed curve otherwise.

6. (f)

Here we follow the pattern established on Remark 4 for surfaces ( 𝒮 0 {\cal S}_{0}) and ( 𝒮 5 {\cal S}_{5}).

7. (g)

As surface ( 𝒮 1 {\cal S}_{1}) is the whole plane g = 0 g=0, due to the same reason presented on Remark 4, we shall not use a color for describing this entire bifurcation surface. However, for indicating the bifurcation straight line ℓ = 0 \ell=0 (belonging to surface ( 𝒮 1 {\cal S}_{1})) we shall use green color and draw it as a continuous line.

As in the previous section, in order to obtain the singular slices needed for the study of the bifurcation diagram of systems ( 9), here we also perform all the computations in an algorithm written in software Mathematica. The reader may find the computations in the file available for free download through the link http://mat.uab.cat/~artes/articles/qvfES/qvfES-B.nb.

The next result presents all the algebraic values of g g corresponding to singular slices (or planes) in the bifurcation diagram. Its proof follows from the study done with the help of the mentioned algorithm.

###### Lemma 11.

Consider the algebraic bifurcation surfaces defined before. The study of their singularities, their intersection points, and their tangencies with planes g = g 0 g=g_{0} provides the following set of four singular values of the parameter g g:

 | { 1, 0, − 1, − 2 }. \left\{1,0,-1,-2\right\}\!. |  |

###### Remark 11.

It is easy to conclude that surfaces ( 𝒮 6 {\cal S}_{6}) and ( 𝒮 8 {\cal S}_{8}) intercept themselves along

 | { g = − u 2 2 ​ ( 1 + u 2), ℓ = u ⁡ ( 2 + u 2) ( 1 + u 2) 2 }. \left\{g=-\dfrac{u^{2}}{2(1+u^{2})},\ \ell=\dfrac{u(2+u^{2})}{(1+u^{2})^{2}}\right\}\!. |  |

We notice that, when u → ∞ u\rightarrow\infty, such an intersection goes to

 | { g = − 1 2, ℓ = 0 }. \left\{g=-\dfrac{1}{2},\ \ell=0\right\}\!. |  |

So, g = − 1 / 2 g=-1/2 can be also considered as a singular value of the parameter g g. And at this singular value, surfaces ( 𝒮 6 {\cal S}_{6}) and ( 𝒮 8 {\cal S}_{8}) intercept themselves at infinity (at the endpoint of straight line ℓ = 0 \ell=0).

We collect the values of the parameter g g obtained from Lemma 11 and Remark 11 and, in the next result we present the complete list of algebraic singular planes corresponding to values of the parameter g g.

###### Proposition 6.

The full set of needed algebraic singular slices in the bifurcation diagram of family ( 9) is formed by five elements which correspond to the values of g g in ( 20).

 | g 1 \displaystyle g_{1} | = 1, g 3 = 0, g 5 = − 1 2, g 7 = − 1, g 9 = − 2. \displaystyle=1,\ g_{3}=0,\ g_{5}=-\frac{1}{2},\ g_{7}=-1,\ g_{9}=-2. |  | (20) |

The numeration in ( 20) is not consecutive since we reserve numbers for generic slices. We point out that we have not found nonalgebraic slices, as in [9], for instance.

In order to determine all the parts generated by the bifurcation surfaces from ( 𝒮 0) ({\cal S}_{0}) to ( 𝒮 8) ({\cal S}_{8}), we first draw the horizontal slices of the three–dimensional parameter space which correspond to the explicit values of g g obtained in Proposition 6. However, as it will be discussed later, the presence of nonalgebraic bifurcation surfaces will be detected and their behavior as we move from slice to slice will be approximately determined. We add to each interval of singular values of g g an intermediate value for which we represent the bifurcation diagram of singularities. The diagram will remain essentially unchanged in these open intervals except the parts affected by the bifurcation. All the eleven sufficient values of g g are shown in ( 21).

 | g 0 = 2 g 6 = − 3 / 4 g 1 = 1 g 7 = − 1 g 2 = 1 / 2 g 8 = − 3 / 2 g 3 = 0 g 9 = − 2 g 4 = − 1 / 4 g 10 = − 3 g 5 = − 1 / 2 \begin{array}[]{ll}g_{0}=2&g_{6}=-3/4\\ g_{1}=1&g_{7}=-1\\ g_{2}=1/2&g_{8}=-3/2\\ g_{3}=0&g_{9}=-2\\ g_{4}=-1/4&g_{10}=-3\\ g_{5}=-1/2&\end{array} |  | (21) |

The values indexed by positive odd indices in ( 21) correspond to explicit values of g g for which there is a bifurcation in the behavior of the systems on the slices. Those indexed by even values are just intermediate points which are necessary to the coherence of the bifurcation diagram.

We now begin the analysis of the bifurcation diagram by studying completely one generic slice and after by moving from slice to slice and explaining all the changes that occur. As an exact drawing of the curves produced by intersecting the surfaces with the slices gives us very small parts which are difficult to distinguish, and points of tangency are almost impossible to recognize, we have produced topologically equivalent figures where parts are enlarged and tangencies are easy to observe.

The reader may find the exact pictures of the five singular slices (containing only the algebraic surfaces) described in ( 20) in a PDF file available at the link http://mat.uab.es/~artes/articles/qvfES/qvfES-B.pdf.

As in the previous section we use the same pattern in order to describe each part of the bifurcation diagram (labels and colors) and we also use continuous and dashed (bifurcation) curves, as explained before.

In Fig. 80 we represent the entire generic slice of the parameter space when g = g 0 = 2 g=g_{0}=2 (remember that we proved that it is enough to consider u ≥ 0 u\geq 0). In this figure (and in the next ones) we denote the ℓ \ell –axis with a dashed and thin black straight line.

Figure 80: Generic slice of the parameter space when g = 2 g=2

When we consider the singular value g = g 1 = 1 g=g_{1}=1 of the parameter g g we observe that surface ( 𝒮 3 {\cal S}_{3}) reduces to

 | − 2 ​ ( 1 + u 2) ​ ( ℓ − 2 ​ u + ℓ ​ u 2) 3. -2(1+u^{2})(\ell-2u+\ell u^{2})^{3}. |  |

By discarding the factor − 2 ​ ( 1 + u 2) -2(1+u^{2}) (which does not have real roots) we observe that such a surface has multiplicity three. On the other hand, by item 1 of Remark 10 this change of multiplicity is related to the presence of an integrable saddle. For this case, the bifurcation diagram can be seeing in Fig. 81.

Figure 81: Singular slice of the parameter space when g = 1 g=1

Now, for the generic value g = g 2 = 1 / 2 g=g_{2}=1/2, the yellow curve is simple again (i.e. it has multiplicity one), see Fig. 82.

Figure 82: Generic slice of the parameter space when g = 1 / 2 g=1/2

As we said before, for g = g 3 = 0 g=g_{3}=0 systems ( 9) are degenerate. In fact, for this value of the parameter g g we have that bifurcation surfaces ( 𝒮 1 {\cal S}_{1}), ( 𝒮 3 {\cal S}_{3}), ( 𝒮 4 {\cal S}_{4}), and ( 𝒮 6 {\cal S}_{6}) vanish and, in addition, ( 𝒮 0 {\cal S}_{0}) | g = 0 = 1 |_{g=0}=1, ( 𝒮 5 {\cal S}_{5}) | g = 0 = 2 |_{g=0}=2, and ( 𝒮 8 {\cal S}_{8}) | g = 0 = ℓ − 2 u + ℓ u 2 |_{g=0}=\ell-2u+\ell u^{2}. Moreover, Remark 9 provides the type of the curve filled up with singular points, according to the value of the parameter ℓ \ell. In Fig. 83 we present the singular slice g = g 3 = 0 g=g_{3}=0 in which we are using the colors and pattern we mentioned in page g.

Figure 83: Singular slice of the parameter space when g = 0 g=0

We start the study of the negative values of the parameter g g (so according to item 2 of Remark 10, for every fixed g < 0 g<0, the point ( u, ℓ) = ( 0, 0) (u,\ell)=(0,0) corresponds to a phase portrait possessing a center type singularity). According to ( 21) we consider the generic slice given by g = g 4 = − 1 / 4 g=g_{4}=-1/4. For this value of the parameter g g:

- •

we now have the presence of two segments of the black surface ( 𝒮 6 {\cal S}_{6});

- •

the purple straight line ( 𝒮 4 {\cal S}_{4}) is now drawn as a continuous curve, since it represents a separatrix connection; and

- •

on the yellow segment 3 ​ S 3 3S_{3} the corresponding phase portrait possesses a weak focus (of order one) and, consequently, this branch of surface ( 𝒮 3 {\cal S}_{3}) corresponds to a Hopf bifurcation. This means that the phase portrait corresponding to one of the sides of this segment must have a limit cycle; in fact it is in the region V 9 V_{9}.

The corresponding slice is presented in Fig. 84.

Figure 84: Generic slice of the parameter space when g = − 1 / 4 g=-1/4

According to Remark 11, we know that for g < 0 g<0 and ℓ > 0 \ell>0 surfaces ( 𝒮 6 {\cal S}_{6}) and ( 𝒮 8 {\cal S}_{8}) have a common point, for every u > 0 u>0. In fact, this point is denoted in Fig. 84 by 6.8 ​ L 1 6.8L_{1}. The same remark shows that such an intersection point goes to infinity at g = g 5 = − 1 / 2 g=g_{5}=-1/2, and this displacement carries volume region V 8 V_{8} to infinity. For this singular value of the parameter g g, the corresponding bifurcation diagram is presented in Fig. 85.

Figure 85: Singular slice of the parameter space when g = − 1 / 2 g=-1/2

If we consider the generic slice given by g = g 6 = − 3 / 4 g=g_{6}=-3/4 we observe that the intersection point presented in Remark 11 goes to the complex plane. As there is no other significant phenomenon to analyze, we conclude that for the generic value under consideration, the bifurcation diagram behaves as the one presented in Fig. 85.

Now we consider the singular slice g = g 7 = − 1 g=g_{7}=-1. One may say that this is a quite interesting singular slice, because:

- •

Previously we mentioned that surface ( 𝒮 0 {\cal S}_{0}), related to a presence of an infinite elliptic–saddle of type ( 1 2) ^ ​ E − H \widehat{\!{1\choose 2}\!\!}\ E-H, defines the entire plane g = − 1 g=-1. As it was pointed out in [9] each phase portrait obtained in the study of this slice is topologically equivalent to a phase portrait obtained in a neighborhood of this plane. However, in order to have a coherent bifurcation diagram, this plane must be studied. Here we follow the pattern established in Remark 4 and we shall not draw this plane in brown color.

- •

For this value of the parameter g g, surfaces ( 𝒮 4 {\cal S}_{4}) and ( 𝒮 6 {\cal S}_{6}) coincides along ℓ = 0 \ell=0. The remaining parts of the bifurcation diagram behave as in the previous slice.

In Fig. 86 we present the singular slice g = − 1 g=-1 completely labeled. In such a figure we use the the same pattern as the one applied in Fig. 61 from the previous section.

Figure 86: Singular slice of the parameter space when g = − 1 g=-1

The next generic slice g = g 8 = − 3 / 2 g=g_{8}=-3/2 deserves a special attention. After passing by an infinite singularity of type ( 1 2) ^ ​ E − H \widehat{\!{1\choose 2}\!\!}\ E-H it is expected to obtain new phase portraits possessing orbits of the infinite elliptic–saddle in different positions (when we compare these new phase portrait with the ones we had before the bifurcation related to ( 1 2) ^ ​ E − H \widehat{\!{1\choose 2}\!\!}\ E-H). So, in the slice under consideration one may find distinct situations to analyze.

In Fig. 87 we present such a generic slice, showing only the algebraic surfaces. We note the existence of continuous branches of surfaces ( 𝒮 3 {\cal{S}}_{3}) (in yellow), ( 𝒮 4 {\cal{S}}_{4}) (in purple), and ( 𝒮 8 {\cal{S}}_{8}) (in cyan). This means the existence of a weak focus, in the case of surface ( 𝒮 3 {\cal{S}}_{3}), the existence of an algebraic invariant straight line provided by a separatrix connection, in the case of surface ( 𝒮 4 {\cal{S}}_{4}), and the existence of an algebraic invariant parabola formed by a separatrix connection, in the case of surface ( 𝒮 8 {\cal{S}}_{8}).

Figure 87: Generic slice of the parameter space when g = − 3 / 2 g=-3/2 (only algebraic surfaces)

We now place for each set of the partition on this slice the local behavior of the flow around the singular points. For a specific value of the parameters of each one of the sets in this partition we compute the global phase portrait with the numerical program P4 [1, 15].

In this slice we have a partition in two–dimensional unbounded parts. From now on, we use lower–case letters provisionally to describe the sets found algebraically in order to do not interfere with the final partition described with capital letters.

For each two–dimensional part we obtain a phase portrait which is coherent with those of all their borders. Except for two parts, which are shown in Fig. 87 and named as follows:

- •

v 13 v_{13}: the region { u ≥ 0, ℓ ≥ 0 } \{u\geq 0,\ell\geq 0\} bordered by the black curve and infinity;

- •

v 17 v_{17}: the region bordered by yellow and cyan curves and also by infinity.

The study of these parts is important for the coherence of the bifurcation diagram. That is why we have decided to present only these parts in the mentioned figures.

We begin with the analysis of part v 13 v_{13}. The phase portrait in v 13 v_{13} near 4 ​ s 3 4s_{3} possesses an infinite graphic formed by orbits contained in the parabolic sectors of the (infinite) elliptic–saddle. However, the phase portrait in v 13 v_{13} near 6 ​ s 4 6s_{4} does not possess such a graphic. Then, there must exist at least one element of surface ( 𝒮 7 {\cal{S}}_{7}) (see 7 ​ S 1 7S_{1} in Fig. 90) dividing part v 13 v_{13} into two “new” parts, V 13 V_{13} and V 14 V_{14}, which represents a bifurcation due to the connection between a separatrix of the infinite elliptic–saddle with a separatrix of the infinite saddle (see Fig. 88 for a sequence of phase portraits in these parts).

We claim that nonalgebraic surface 7 ​ S 1 7S_{1} is unbounded and 4.8 ​ ℓ 1 4.8\ell_{1} is one of its endpoints. In fact, numerical verifications indicate the truth of this statement. Note that it is not possible that the starting point of this surfaces is on 6 ​ s 4 6s_{4}, since on black surfaces we have only a C ∞ C^{\infty} node–focus bifurcation. On the other hand, the endpoint of 7 ​ S 1 7S_{1} cannot be on 4 ​ s 3 4s_{3} because, in order to have this, first we need to break the invariant straight line connecting the opposite infinite saddles. Then, the only possible endpoint of surface 7 ​ S 1 7S_{1} is 4.8 ​ ℓ 1 4.8\ell_{1}, and our claim is proved.

Figure 88: Sequence of phase portraits in parts V 13 V_{13} and V 14 V_{14} of slice g = − 3 / 2 g=-3/2 (the labels are according to Fig. 90)

Now, we carry out the analysis of part v 17 v_{17}. We consider the segment 3 ​ s 4 3s_{4} in Fig. 87, which is one of the borders of part v 17 v_{17}. On this segment, the corresponding phase portrait possesses a weak focus (of order one) and, consequently, this branch of surface ( 𝒮 3 {\cal{S}}_{3}) corresponds to a Hopf bifurcation. This means that the phase portrait corresponding to one of the sides of this segment must have a limit cycle; in fact it is in v 17 v_{17}. Moreover, the phase portrait in v 17 v_{17} near 8 ​ s 4 8s_{4} possesses an infinite graphic formed by orbits contained in the parabolic sectors of the (infinite) elliptic–saddle. However, the phase portrait in v 17 v_{17} near 3 ​ s 4 3s_{4} does not possess such a graphic. Then, there must exist at least one element of surface ( 𝒮 7 {\cal{S}}_{7}) (see 7 ​ S 2 7S_{2} in Fig. 90) dividing part v 17 v_{17} into two “new” parts, V 16 V_{16} and V 17 V_{17}, which represents a bifurcation due to the connection between a separatrix of the infinite elliptic–saddle with a separatrix of the infinite saddle (see Fig. 89 for a sequence of phase portraits in these parts).

In this paragraph we prove that nonalgebraic surface 7 ​ S 2 7S_{2} is unbounded and 4.8 ​ ℓ 1 4.8\ell_{1} is one of its endpoints. Indeed, numerical verifications indicate that this fact is true. Note that if the starting point of this surface is any point of 3 ​ s 4 3s_{4} then a portion of this subset must not refer to a Hopf bifurcation, which contradicts the fact that on 3 ​ s 4 3s_{4} we have a weak focus of order one. In addition, the endpoint of 7 ​ S 2 7S_{2} cannot be on 8 ​ s 4 8s_{4} because, in order to have this, first it is necessary to break the invariant parabola formed by a separatrix of the infinite elliptic–saddle. So, the only possible endpoint of surface 7 ​ S 2 7S_{2} is 4.8 ​ ℓ 1 4.8\ell_{1}, as we wanted to prove.

Figure 89: Sequence of phase portraits in parts V 16 V_{16} and V 17 V_{17} of slice g = − 3 / 2 g=-3/2 (the labels are according to Fig. 90)

The complete bifurcation diagram for this part can be seeing in Fig. 90.

Figure 90: Generic slice of the parameter space when g = − 3 / 2 g=-3/2

Now we consider the singular slice g = g 9 = − 2 g=g_{9}=-2. This is another interesting and important singular slice.

- •

Surface ( 𝒮 5 \mathcal{S}_{5}) = g + 2 =g+2 is related to a coalescence of infinite singular points. Remember that if ℓ ≠ 0 \ell\neq 0 the phase portraits obtained in the study of this slice possess at most one pair of infinite singular points and, if ℓ = 0 \ell=0 the corresponding phase portraits have the line at infinity filled up with singularities. Here we follow Remark 4 and we shall not draw the slice g = − 2 g=-2 in red color.

- •

By studying the transition among regions and phase portraits from g = − 3 / 2 g=-3/2 with regions and phase portraits from g = − 2 g=-2 we observe that V 14 V_{14} (respectively V 16 V_{16}) from slice g = − 3 / 2 g=-3/2 converges to 4.5 ​ L 1 4.5L_{1} (respectively 5.8 ​ L 2 5.8L_{2}) from slice g = − 2 g=-2. The correspondence among the remaining regions of these slices is clear.

In Fig. 91 we present the slice g = − 2 g=-2 completely labeled. In such a figure we use the same pattern as the one used in the slices g = 0 g=0 and g = − 1 g=-1 in order to present a label for each region.

Figure 91: Singular slice of the parameter space when g = − 2 g=-2

Finally we consider the generic slice g = g 10 = − 3 g=g_{10}=-3. In what follows we present some comments on this slice.

- •

We observe that due to the nature of the coalescence of infinite singularities on this slice, in the next generic slice g = g 10 = − 3 g=g_{10}=-3 we shall expect to obtain phase portraits with a reduced number of separatrices. In fact, at g = g 8 = − 3 / 2 g=g_{8}=-3/2 we had phase portraits possessing an infinite elliptic–saddle and also an infinite saddle. At g = g 9 = − 2 g=g_{9}=-2 the infinite saddle coalesced with the infinite elliptic–saddle. Now, at the generic slice g = g 10 = − 3 g=g_{10}=-3 we have an infinite elliptic–saddle and also an infinite node.

- •

At this value of the parameter g g the purple curve (surface ( 𝒮 4 \mathcal{S}_{4})) no longer represents a separatrix connection, and this is due to the fact that we do not have an enough number of separatrices in order to have an invariant straight line, since we passed by the mentioned coalescence of infinite singularities.

- •

Surfaces ( 𝒮 4 \mathcal{S}_{4}) and ( 𝒮 6 \mathcal{S}_{6}) have an intersection point along ℓ = 0 \ell=0.

The complete bifurcation diagram for this part is presented in Fig. 92.

Figure 92: Generic slice of the parameter space when g = − 3 g=-3

Since there is coherence among the generic and singular slices presented before, no more slices are needed for the complete coherence of the bifurcation diagram. So, all the values of the parameter g g in ( 21) are sufficient for the coherence of the bifurcation diagram. Thus, we can affirm that we have described a complete bifurcation diagram for class 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) ¯ \overline{\bf{Q}{{\widehat{ES}(B)}}} modulo islands, as we discuss in Sec. 3.2.1.

#### 3.2.1 Other relevant facts about the bifurcation diagram

The bifurcation diagram we have obtained for the class 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) ¯ \overline{\bf{Q}{{\widehat{ES}(B)}}} is completely coherent, i.e. in this family, by taking any two points in the parameter space and joining them by a continuous curve, along this curve the changes in phase portraits that occur when crossing the different bifurcation surfaces we mention can be completely explained.

Nevertheless, we cannot be sure that this bifurcation diagram is the complete bifurcation diagram for 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) ¯ \overline{\bf{Q}{{\widehat{ES}(B)}}} due to the possibility of the existence of “islands” inside the parts bordered by unmentioned bifurcation surfaces. In case they exist, these “islands” would not mean any modification of the nature of the singular points. So, on the border of these “islands” we could only have bifurcations due to saddle connections or multiple limit cycles.

In case there were more bifurcation surfaces, we should still be able to join two representatives of any two parts of the 89 parts of 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) ¯ \overline{\bf{Q}{{\widehat{ES}(B)}}} found until now with a continuous curve either without crossing such a bifurcation surface or, in case the curve crosses it, it must do it an even number of times without tangencies, otherwise one must take into account the multiplicity of the tangency, so the total number must be even. This is why we call these potential bifurcation surfaces “ islands ”.

However, we have not found a different phase portrait which could fit in such an island. A potential “island” would be the set of parameters for which the phase portraits possess a double limit cycle and this “island” would be inside the parts where W 4 < 0 W_{4}<0 since we have the presence of a focus.

#### 3.2.2 Completion of the proof of Theorem 2

In the bifurcation diagram we may have topologically equivalent phase portraits belonging to distinct parts of the parameter space. As here we have 89 distinct parts of the parameter space, to help us to identify or to distinguish phase portraits, we need to introduce some invariants and we actually choose integer valued, character and symbol invariants. Some of them were already used in [12] and [9], but we recall them and introduce some needed ones. These invariants yield a classification which is easier to grasp.

###### Definition 11.

We denote by I 1 ​ ( S) I_{1}(S) a symbol from the set { ∅, [×], [) (] } \{\emptyset,\left[\times\right],\left[)(\right]\} which indicates the following configuration of curves filled up with singularities, respectively: none (nondegenerate systems – in this case all systems do not contain a curve filled up with singularities), two real straight lines intersecting at a finite point, and an hyperbola. This invariant only makes sense to distinguish the degenerate phase portrait obtained.

###### Definition 12.

We denote by I 2 ​ ( S) I_{2}(S) the sum of the indices of the isolated real finite singular points.

###### Definition 13.

We denote by I 3 ​ ( S) I_{3}(S) the number of real infinite singular points. We note that this number can also be infinite, which is represented by ∞ \infty.

###### Definition 14.

For a given infinite singularity s s of a system S S, let ł s \l_{s} be the number of global or local separatrices beginning or ending at s s and which do not lie on the line at infinity. We have 0 ≤ ł s ≤ 4 0\leq\l_{s}\leq 4. We denote by I 4 ​ ( S) I_{4}(S) the sequence of all such ł s \l_{s} when s s moves in the set of infinite singular points of the system S S. We start the sequence at the infinite singular point which receives (or sends) the greatest number of separatrices and take the direction which yields the greatest absolute value, e.g. the values 2110 2110 and 2011 2011 for this invariant are symmetrical (and, therefore, they are the same), so we consider 2110 2110.

###### Definition 15.

We denote by I 5 ​ ( S) I_{5}(S) the number of limit cycles around a foci.

###### Definition 16.

We denote by I 6 ​ ( S) I_{6}(S) an element from the set { c, f } \{c,f\} indicating the type of the real finite singularity located inside the region bordered by the graphic, which can be either a c enter or a f ocus.

###### Definition 17.

We denote by I 7 ​ ( S) I_{7}(S) a pair ( A, B) (A,B) where A A and B B represent the number of separatrices arriving or leaving the corresponding parabolic sectors of the singularity ( 1 2) ^ ​ P ​ H ​ P − E \widehat{\!{1\choose 2}\!\!}\ PHP-E at infinity.

As we have noted previously in Remark 6, we do not distinguish between phase portraits whose only difference is that in one we have a finite node and in the other a focus. Both phase portraits are topologically equivalent and they can only be distinguished within the C 1 C^{1} class. In case we may want to distinguish between them, a new invariant may easily be introduced.

###### Theorem 5.

Consider the class 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) ¯ \overline{\bf{Q}{{\widehat{ES}(B)}}} and all the phase portraits that we have obtained for this family. The values of the affine invariant ℐ = ( I 1, I 2, I 3, I 4, I 5, I 6, I 7) {\cal I}=(I_{1},I_{2},I_{3},I_{4},I_{5},I_{6},I_{7}) given in the diagram from Table 20 yields a partition of these phase portraits of the class 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) ¯ \overline{\bf{Q}{{\widehat{ES}(B)}}}.

Furthermore, for each value of ℐ \cal I in this diagram there corresponds a single phase portrait; i.e. S S and S ′ S^{\prime} are such that ℐ ⁡ ( S) = ℐ ⁡ ( S ′) {\cal I}(S)={\cal I}(S^{\prime}), if and only if S S and S ′ S^{\prime} are topologically equivalent.

The bifurcation diagram for 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) ¯ \overline{\bf{Q}{{\widehat{ES}(B)}}} has 89 parts which produce 27 topologically different phase portraits as described in Tables 20 to 21. The remaining 62 parts do not produce any new phase portrait which was not included in the 27 previous ones. The difference is basically the presence of a strong focus instead of a node and vice versa, weak points, and a presence of invariant algebraic curves (lines or parabolas) which do not represent a separatrix connection.

The phase portraits having neither limit cycle nor graphic have been denoted surrounded by parenthesis, for example ( V 20) (V_{20}); the phase portraits having one limit cycle have been denoted surrounded by brackets, for example [V 24] [V_{24}]; the phase portraits having one graphic have been denoted surrounded by { ∗ } \{\ast\} and those ones having two or more graphics have been denoted surrounded by { { ∗ } } \{\!\{\ast\}\!\}, for example { 5 ​ S 3 } \{5S_{3}\} and { { V 1 } } \{\!\{V_{1}\}\!\}, respectively. Moreover, the phase portraits having one limit cycle and more than one graphic have been denoted surrounded by [{ { ∗ } }] [\{\{\ast\}\}], for example [{ { V 17 } }] [\{\{V_{17}\}\}].

###### Proof of Theorem 5.

The above result follows from the results in the previous sections and a careful analysis of the bifurcation diagrams given in Sec. 3.2, in Figs. 80 to Fig. 92, the definition of the invariants I j I_{j} and their explicit values for the corresponding phase portraits. ∎

We recall some observations regarding the equivalence relations used in this study: the affine and time rescaling, C 1 C^{1} and topological equivalences.

The coarsest one among these three is the topological equivalence and the finest is the affine equivalence. We can have two systems which are topologically equivalent but not C 1 − C^{1}- equivalent. For example, we could have a system with a finite antisaddle which is a structurally stable node and in another system with a focus, the two systems being topologically equivalent but belonging to distinct C 1 − C^{1}- equivalence classes, separated by the surface ( 𝒮 6) ({\cal S}_{6}) on which the node turns into a focus.

In Table 21 we list in the first column 27 parts with all the distinct phase portraits of Fig. 4. Corresponding to each part listed in column one we have in each row all parts whose phase portraits are topologically equivalent to the phase portrait appearing in column 1 of the same row.

In the second column we set all the parts whose systems yield topologically equivalent phase portraits to those in the first column, but which may have some algebro–geometric features related to the position of the orbits. In the third column we present all the parts which are topologically equivalent to the ones from the first column having a focus instead of a node.

In the fourth (respectively, fifth; and sixth) column we list all parts whose phase portraits have a node which is at a bifurcation point producing foci close to the node in perturbations, a node–focus to shorten (respectively, a finite weak singular point; and possess an invariant curve (straight line and/or parabola) not yielding a connection of separatrices).

The last column refers to other reasons associated to different geometrical aspects and they are described as follows:

1. (1)

The phase portraits correspond to symmetric parts of the bifurcation diagram;

2. (2)

the phase portrait possesses a singularity of type ( 1 2) ^ ​ E − H \widehat{\!{1\choose 2}\!\!}\ E-H at infinity.

Whenever phase portraits appear in a row in a specific column, the listing is done according to the decreasing dimension of the parts where they appear, always placing the lower dimensions on lower lines.

#### 3.2.3 Proof of Theorem 2

The bifurcation diagram described in Sec. 3.2, plus Table 20 of the geometrical invariants distinguishing the 27 phase portraits, plus Table 21 giving the equivalences with the remaining phase portraits lead to the proof of Theorem 2.

Table 20: Geometric classification for the family 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) \bf{Q}{{\widehat{ES}(B)}}

 | I 1 = { [) (] { { 1 S 1 } }, [×] ​ { { 1.1 ​ L 1 } }, ∅ & I 2 = { − 1 ​ { { V 1 } }, 1 & I 3 = { 1 & I 4 = { 20 ​ { { 5.8 ​ L 2 } }, 21 & I 5 = { 0 ​ { { 5 ​ S 1 } }, 1 ​ { { 5 ​ S 4 } }, 30 ​ { { 5 ​ S 3 } }, 2 & I 4 = { 1010 & I 5 = 0 & I 6 = { c ​ { { 4.8 ​ L 3 } }, f ​ { { 4 ​ S 2 } }, 1110 & I 5 = { 0 ​ { { V 5 } }, 1 ​ { { V 9 } }, 2000 & I 5 = 0 & I 6 = { c ​ { { 4.8 ​ L 5 } }, f ​ { { 8 ​ S 5 } }, 2100 & I 5 = { 0 ​ { { V 20 } }, 1 ​ { { V 24 } }, 2101 ​ { { 4.8 ​ L 4 } }, 2111 & I 5 = { 0 ​ { { 7 ​ S 1 } }, 1 ​ { { 7 ​ S 2 } }, 2121 & I 5 = { 0 ​ { { V 12 } }, 1 ​ { { V 17 } }, 3101 ​ { { 4 ​ S 3 } }, 3111 ​ { { 8 ​ S 4 } }, 4111 & I 5 = { 0 & I 6 = f & I 7 = { ( 2, 2) ​ { { V 14 } }, ( 3, 1) ​ { { V 15 } }, 1 ​ { { V 16 } }, ∞ & I 4 = 0 & I 5 = 0 & I 6 = { f ​ { { 4.5 ​ L 1 } }, c ​ { { P 4 } }, I_{1}\!=\!\left\{\begin{array}[]{ll}\left[)(\right]\,\,\left\{\left\{1S_{1}\right\}\right\},\\ \left[\times\right]\,\,\left\{\left\{1.1L_{1}\right\}\right\},\\ \emptyset\,\,\&\,\,I_{2}\!=\!\left\{\begin{array}[]{ll}-1\,\,\left\{\left\{V_{1}\right\}\right\},\\ 1\,\,\&\,\,I_{3}\!=\!\left\{\begin{array}[]{ll}1\,\,\&\,\,I_{4}\!=\!\left\{\begin{array}[]{ll}20\,\,\left\{\left\{5.8L_{2}\right\}\right\},\\ 21\,\,\&\,\,I_{5}\!=\!\left\{\begin{array}[]{ll}0\,\,\left\{\left\{5S_{1}\right\}\right\},\\ 1\,\,\left\{\left\{5S_{4}\right\}\right\},\\ \end{array}\right.\\ 30\,\,\left\{\left\{5S_{3}\right\}\right\},\\ \end{array}\right.\\ 2\,\,\&\,\,I_{4}\!=\!\left\{\begin{array}[]{ll}1010\,\,\&\,\,I_{5}\!=\!0\,\,\&\,\,I_{6}\!=\!\left\{\begin{array}[]{ll}c\,\,\left\{\left\{4.8L_{3}\right\}\right\},\\ f\,\,\left\{\left\{4S_{2}\right\}\right\},\\ \end{array}\right.\\ 1110\,\,\&\,\,I_{5}\!=\!\left\{\begin{array}[]{ll}0\,\,\left\{\left\{V_{5}\right\}\right\},\\ 1\,\,\left\{\left\{V_{9}\right\}\right\},\\ \end{array}\right.\\ 2000\,\,\&\,\,I_{5}\!=\!0\,\,\&\,\,I_{6}\!=\!\left\{\begin{array}[]{ll}c\,\,\left\{\left\{4.8L_{5}\right\}\right\},\\ f\,\,\left\{\left\{8S_{5}\right\}\right\},\\ \end{array}\right.\\ 2100\,\,\&\,\,I_{5}\!=\!\left\{\begin{array}[]{ll}0\,\,\left\{\left\{V_{20}\right\}\right\},\\ 1\,\,\left\{\left\{V_{24}\right\}\right\},\\ \end{array}\right.\\ 2101\,\,\left\{\left\{4.8L_{4}\right\}\right\},\\ 2111\,\,\&\,\,I_{5}\!=\!\left\{\begin{array}[]{ll}0\,\,\left\{\left\{7S_{1}\right\}\right\},\\ 1\,\,\left\{\left\{7S_{2}\right\}\right\},\\ \end{array}\right.\\ 2121\,\,\&\,\,I_{5}\!=\!\left\{\begin{array}[]{ll}0\,\,\left\{\left\{V_{12}\right\}\right\},\\ 1\,\,\left\{\left\{V_{17}\right\}\right\},\\ \end{array}\right.\\ 3101\,\,\left\{\left\{4S_{3}\right\}\right\},\\ 3111\,\,\left\{\left\{8S_{4}\right\}\right\},\\ 4111\,\,\&\,\,I_{5}\!=\!\left\{\begin{array}[]{ll}0\,\,\&\,\,I_{6}\!=\!f\,\,\&\,\,I_{7}\!=\!\left\{\begin{array}[]{ll}(2,2)\,\,\left\{\left\{V_{14}\right\}\right\},\\ (3,1)\,\,\left\{\left\{V_{15}\right\}\right\},\\ \end{array}\right.\\ 1\,\,\left\{\left\{V_{16}\right\}\right\},\\ \end{array}\right.\\ \end{array}\right.\\ \infty\,\,\&\,\,I_{4}\!=\!0\,\,\&\,\,I_{5}\!=\!0\,\,\&\,\,I_{6}\!=\!\left\{\begin{array}[]{ll}f\,\,\left\{\left\{4.5L_{1}\right\}\right\},\\ c\,\,\left\{\left\{P_{4}\right\}\right\},\\ \end{array}\right.\\ \end{array}\right.\\ \end{array}\right.\end{array}\right. |  |

Table 21: Topological equivalences for the family 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) \bf{Q}{{\widehat{ES}(B)}}

Presented | Identical | Finite | Finite | Finite | Possessing |  |

phase | under | antisaddle | antisaddle | weak | invariant curve | Other reasons |

portrait | perturbations | focus | node–focus | point | (no separatrix) |  |

V 1 V_{1} | V 2 V_{2}, V 3 V_{3}, V 4 V_{4} |  |  |  |  |  |

 |  |  |  | 3 ​ S 1 3S_{1}, 3 ​ S 2 3S_{2} | 4 ​ S 1 4S_{1}, 8 ​ S 1 8S_{1} |  |

 |  |  |  | 3.3 ​ L 1 3.3L_{1} | 4.8 ​ L 1 4.8L_{1}, 4.8 ​ L 2 4.8L_{2} |  |

 |  |  |  |  | P 1 P_{1} |  |

V 5 V_{5} | V 8 V_{8} | V 6 V_{6}, V 7 V_{7} |  |  |  | V 10 ( 1) V_{10}^{(1)}, V 11 ( 1) V_{11}^{(1)} |

 |  | 0 ​ S 2 0S_{2}, 6 ​ S 1 6S_{1} |  |  | 8 ​ S 3 8S_{3} | 0 ​ S 1 ( 2) 0S_{1}^{(2)}, 0 ​ S 4 ( 1) 0S_{4}^{(1)}, 0 ​ S 5 ( 2) 0S_{5}^{(2)} |

 |  | 6 ​ S 2 6S_{2}, 8 ​ S 2 8S_{2} |  |  |  | 3 ​ S 3 ( 1) 3S_{3}^{(1)}, 6 ​ S 3 ( 1) 6S_{3}^{(1)} |

 |  |  | 0.6 ​ L 1 0.6L_{1}, 6.8 ​ L 1 6.8L_{1} |  |  | 0.3 ​ L 1 ( 1) 0.3L_{1}^{(1)}, 0.6 ​ L 2 ( 1) 0.6L_{2}^{(1)} |

V 9 V_{9} |  |  |  |  |  |  |

 |  |  |  |  |  | 0 ​ S 3 ( 2) 0S_{3}^{(2)} |

V 12 V_{12} |  | V 13 V_{13} |  |  |  | V 18 ( 1) V_{18}^{(1)}, V 19 ( 1) V_{19}^{(1)} |

 |  |  | 6 ​ S 4 6S_{4} |  |  | 3 ​ S 4 ( 1) 3S_{4}^{(1)}, 6 ​ S 5 ( 1) 6S_{5}^{(1)} |

V 14 V_{14} |  |  |  |  |  |  |

V 15 V_{15} |  |  |  |  |  |  |

V 16 V_{16} |  |  |  |  |  |  |

V 17 V_{17} |  |  |  |  |  |  |

V 20 V_{20} | V 22 V_{22} | V 21 V_{21}, V 23 V_{23} |  |  |  | V 25 ( 1) V_{25}^{(1)}, V 26 ( 1) V_{26}^{(1)} |

 |  | 4 ​ S 4 4S_{4} | 6 ​ S 6 6S_{6}, 6 ​ S 7 6S_{7} |  | 4 ​ S 5 4S_{5} | 3 ​ S 5 ( 1) 3S_{5}^{(1)}, 6 ​ S 8 ( 1) 6S_{8}^{(1)} |

 |  |  | 4.6 ​ L 1 4.6L_{1} |  |  |  |

V 24 V_{24} |  |  |  |  |  |  |

1 ​ S 1 1S_{1} | 1 ​ S 2 1S_{2} |  |  |  |  | 1 ​ S 3 ( 1) 1S_{3}^{(1)} |

 | 1.8 ​ L 1 1.8L_{1} |  |  |  |  |  |

4 ​ S 2 4S_{2} |  |  |  |  |  |  |

 |  |  |  |  | 0.4 ​ L 1 0.4L_{1} |  |

4 ​ S 3 4S_{3} |  |  |  |  |  |  |

5 ​ S 1 5S_{1} |  | 5 ​ S 2 5S_{2} |  |  |  | 5 ​ S 5 ( 1) 5S_{5}^{(1)}, 5 ​ S 6 ( 1) 5S_{6}^{(1)} |

 |  | 5.8 ​ L 1 5.8L_{1} | 5.6 ​ L 1 5.6L_{1} |  |  | 3.5 ​ L 1 ( 1) 3.5L_{1}^{(1)}, 5.6 ​ L 2 ( 1) 5.6L_{2}^{(1)} |

5 ​ S 3 5S_{3} |  |  |  |  |  |  |

5 ​ S 4 5S_{4} |  |  |  |  |  |  |

7 ​ S 1 7S_{1} |  |  |  |  |  |  |

7 ​ S 2 7S_{2} |  |  |  |  |  |  |

8 ​ S 4 8S_{4} |  |  |  |  |  |  |

8 ​ S 5 8S_{5} |  |  |  |  |  |  |

1.1 ​ L 1 1.1L_{1} |  |  |  |  |  |  |

 | P 2 P_{2} |  |  |  |  |  |

4.5 ​ L 1 4.5L_{1} |  |  |  |  |  |  |

4.8 ​ L 3 4.8L_{3} |  |  |  |  |  |  |

 |  |  |  |  | P 3 P_{3} |  |

4.8 ​ L 4 4.8L_{4} |  |  |  |  |  |  |

4.8 ​ L 5 4.8L_{5} |  |  |  |  |  |  |

5.8 ​ L 2 5.8L_{2} |  |  |  |  |  |  |

P 4 P_{4} |  |  |  |  |  |  |

### 3.3 The bifurcation diagram of family 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) \bf{Q}{{\widehat{ES}(C)}}

In this section we present the study of the bifurcation diagram of family 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) \bf{Q}{{\widehat{ES}(C)}}, given by normal form ( 13). Note that this family depends on the parameters g ∈ ℝ ∖ { 0 } g\in\mathbb{R}\setminus\{0\} (in order to have nondegenerate systems) and ℓ ∈ ℝ + ∪ { 0 } \ell\in\mathbb{R}^{+}\cup\{0\} (due to the symmetry we proved before). Here we shall consider the bifurcation diagram formed by points with Cartesian coordinates ( g, ℓ) (g,\ell) with ℓ ≥ 0 \ell\geq 0.

For systems ( 13), computations show that

 | μ 0 = 𝐃 = 𝐏 = 0, 𝐑 = 48 ​ g 4 ​ x 2, \mu_{0}=\mathbf{D}=\mathbf{P}=0,\quad\mathbf{R}=48g^{4}x^{2}, |  |

therefore by [6, Table 5.1], for g ≠ 0 g\neq 0 systems ( 13) possess exactly one real triple finite singular point.

Now we present the value of the algebraic invariants and T–comitants (with respect to systems ( 13)) which are relevant in our study. Since we have a two–parameter bifurcation diagram, such algebraic tools shall give us bifurcation curves.

Bifurcation curve in ℝ 2 \mathbb{R}^{2} due to degeneracy of the system

From the normal form under consideration, calculation show that

 | μ 0 = 0, μ 1 = 4 ​ g 2 ​ x, μ 2 = μ 3 = μ 4 = 0. \mu_{0}=0,\quad\mu_{1}=4g^{2}x,\quad\mu_{2}=\mu_{3}=\mu_{4}=0. |  |

Then by [6, Lemma 5.2], for g = 0 g=0 systems ( 13) are reduced to

 |  | x ′ = 0, \displaystyle x^{\prime}=0, |  |

 |  | y ′ = ℓ ​ y + 2 ​ x ​ y + ℓ ​ x 2, \displaystyle y^{\prime}=\ell y+2xy+\ell x^{2}, |  |

they are degenerate and therefore we define the bifurcation straight line

 | ( ℒ 1): g = 0. ({\cal L}_{1})\!:g=0. |  |

According to [6, Diagram 12.1], for these systems we calculate

 | η = 0, M ~ = − 32 ​ x 2, κ = K ~ = L ~ = κ 1 = K 1 = 0, \eta=0,\quad\widetilde{M}=-32x^{2},\quad\kappa=\widetilde{K}=\widetilde{L}=\kappa_{1}={K}_{1}=0, |  |

and

 | L 2 = 6 ​ ℓ 3 ​ x 4. {L}_{2}=6\ell^{3}x^{4}. |  |

As in the case of family 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) \bf{Q}{{\widehat{ES}(B)}}, here we also have that L 2 = 0 {L}_{2}=0 is equivalent to ℓ = 0 \ell=0. So, according to the mentioned reference, for ℓ ≠ 0 \ell\neq 0 we have a hyperbola filled up with singular points, and for ℓ = 0 \ell=0 (i.e. at P 3 = ( g, ℓ) = ( 0, 0) P_{3}=(g,\ell)=(0,0)) we have two real straight lines (filled up with singular points) intersecting at a finite point.

Bifurcation curves in ℝ 2 \mathbb{R}^{2} due to the presence of invariant algebraic curves

( ℒ 4 {\cal L}_{4}) This curve contains the points of the parameter space in which there appear invariant straight lines (see Lemma 4). For systems ( 13) we compute the polynomial invariant B 1 B_{1} and we define curve

 | ( ℒ 4): \displaystyle({\cal L}_{4})\!: | 8 ​ g 6 ​ ℓ 3 = 0. \displaystyle 8g^{6}\ell^{3}=0. |  |

( ℒ 8 {\cal L}_{8}) This curve contains the points of the parameter space in which there appear invariant parabolas. According to the conditions stated in Lemma 4 we define this curve by

 | ( ℒ 8): \displaystyle({\cal L}_{8})\!: | ℓ = 0. \displaystyle\ell=0. |  |

We point out that for g ≠ 0 g\neq 0, the bifurcation curves ( ℒ 4 {\cal L}_{4}) and ( ℒ 8 {\cal L}_{8}) coincide.

Bifurcation curve due to multiplicities of infinite singularities

( ℒ 5 {\cal L}_{5}) This is the bifurcation curve due to multiplicity of infinite singular points. According to [6, Lemma 5.5], for this family we calculate

 | η = 0, M ~ = − 8 ​ ( g − 2) 2 ​ x 2, C 2 = x 2 ​ [− ℓ ​ x + ( g − 2) ​ y], \eta=0,\quad\widetilde{M}=-8(g-2)^{2}x^{2},\quad C_{2}=x^{2}\left[-\ell x+(g-2)y\right], |  |

and we observe that along

 | ( ℒ 5): \displaystyle(\mathcal{L}_{5})\!: | g − 2 = 0, \displaystyle g-2=0, |  |

we have a coalescence of infinite singular points. In addition, due to the mentioned result, along the straight line g = 2 g=2 the phase portrait corresponding to ℓ = 0 \ell=0 (i.e. the phase portrait corresponding to P 1 = ( g, ℓ) = ( 2, 0) P_{1}=(g,\ell)=(2,0)) have the line at infinity filled up with singular points.

Bifurcation curve in ℝ 2 \mathbb{R}^{2} due to the infinite elliptic–saddle

( ℒ 0 {\cal L}_{0}) Along the straight line g = 1 g=1 the corresponding phase portraits possess an infinite singularity of the type ( 1 2) ^ ​ E − H \widehat{\!{1\choose 2}\!\!}\ E-H. Due to results on [6] we compute the comitant

 | N ~ = 4 ​ ( g − 1) ​ x 2 \widetilde{N}=4(g-1)x^{2} |  |

and we define

 | ( ℒ 0): g − 1 = 0. ({\cal L}_{0})\!:g-1=0. |  |

The bifurcation curves listed previously are all algebraic and they, except ( ℒ 4) ({\cal L}_{4}) and ( ℒ 8) ({\cal L}_{8}), are the bifurcation curves of singularities of systems ( 13) in the parameter space.

Here we shall plot these bifurcation curves in a plane with Cartesian coordinates ( g, ℓ) (g,\ell), where the horizontal line is the g g –axis and ℓ ≥ 0 \ell\geq 0.

###### Remark 12.

We highlight that since for g ≠ 0 g\neq 0 the curve ( ℒ 4) ({\cal L}_{4}) coincides with ( ℒ 8) ({\cal L}_{8}), we decided to plot only curve ( ℒ 8) ({\cal L}_{8}), using the cyan color. In addition, ( ℒ 0) ({\cal L}_{0}) is drawn in brown, ( ℒ 1) ({\cal L}_{1}) is drawn in green, and ( ℒ 5) ({\cal L}_{5}) is drawn in red.

So, in summary we have the following (distinct) bifurcation curves:

 | ( ℒ 0): \displaystyle(\mathcal{L}_{0})\!: | g − 1 = 0, \displaystyle g-1=0, |  |

 | ( ℒ 1): \displaystyle(\mathcal{L}_{1})\!: | g = 0, \displaystyle g=0, |  |

 | ( ℒ 5): \displaystyle(\mathcal{L}_{5})\!: | g − 2 = 0, \displaystyle g-2=0, |  |

 | ( ℒ 8): \displaystyle(\mathcal{L}_{8})\!: | ℓ = 0. \displaystyle\ell=0. |  |

And, as our bifurcation diagram is given by { ( g, ℓ) ∈ ℝ 2; ℓ ≥ 0 } \{(g,\ell)\in\mathbb{R}^{2};\ell\geq 0\}, it is clear that (in such a set) we have to consider only the curves g = 0, g = 1, g = 2 g=0,g=1,g=2, and ℓ = 0 \ell=0, and also the intersection among them, i.e. the points P 1 = ( g, ℓ) = ( 2, 0) P_{1}=(g,\ell)=(2,0), P 2 = ( g, ℓ) = ( 1, 0) P_{2}=(g,\ell)=(1,0), and P 3 = ( g, ℓ) = ( 0, 0) P_{3}=(g,\ell)=(0,0).

In Fig. 93 we present the bifurcation diagram completely labeled. In such a figure we denote an open region by S0i, where i is a number, a bifurcation curve ( ℒ j) (\mathcal{L}_{j}) is labeled as jL0k, k ∈ ℕ k\in\mathbb{N}, and a point is denoted as in the previous sections. Moreover, we denote the ℓ \ell –axis (which represents the degenerate set) with a dashed and thin black straight line.

Figure 93: Parameter space

From the study of this bifurcation diagram, we obtain phase portraits possessing different types of triple finite singular points. In fact, from [6, Table 6.2] we calculate

 | K ~ = 4 ​ g ​ x 2. \widetilde{K}=4gx^{2}. |  |

For nondegenerate systems (i.e. g ≠ 0 g\neq 0), this comitant can be positive or negative, depending on the sign of the parameter g g. In what follows we present the different types of triple finite singularities we obtained in the study of the bifurcation diagram under consideration.

1. 1.

If g > 0 g>0 then K ~ > 0 \widetilde{K}>0 and, from the mentioned table we compute

 | G 10 = g 3 ​ ℓ 3. G_{10}=g^{3}\ell^{3}. |  |

Since g ≠ 0 g\neq 0, we have that sign ​ ( G 10) = sign ​ ( ℓ) \text{sign}(G_{10})=\text{sign}(\ell) and, from the mentioned table can have two possibilities:

  - •

If ℓ ≠ 0 \ell\neq 0 we have a finite semi–elemental triple node n ¯ ( 3) \bar{n}_{(3)};

  - •

If ℓ = 0 \ell=0 we have a finite nilpotent elliptic–saddle e ​ s ^ ( 3) \widehat{es}_{(3)}.

2. 2.

If g < 0 g<0 then K ~ < 0 \widetilde{K}<0. Now, from [6, Diagram 10.2] we calculate

 | κ = 0, ℱ 1 = 6 ​ g 2 ​ ℓ. \kappa=0,\quad\mathcal{F}_{1}=6g^{2}\ell. |  |

Since g ≠ 0 g\neq 0, we have that sign ​ ( ℱ 1) = sign ​ ( ℓ) \text{sign}(\mathcal{F}_{1})=\text{sign}(\ell) and, from the diagram under consideration again we come across two possibilities:

  - •

If ℓ ≠ 0 \ell\neq 0 we have a finite semi–elemental triple saddle s ¯ ( 3) \bar{s}_{(3)};

  - •

If ℓ = 0 \ell=0 we have a finite nilpotent triple saddle s ^ ( 3) \widehat{s}_{(3)}.

By performing the study of this bifurcation diagram we observe that there is coherence among all the phase portraits we obtained. Moreover, we point out that in our study we have not found any nonalgebraic bifurcation curve and there is no need of it so to complete coherence. So we can affirm that we have described a complete bifurcation diagram for class 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) ¯ \overline{\bf{Q}{{\widehat{ES}(C)}}} modulo islands, as we discuss in Sec. 3.3.1.

#### 3.3.1 Other relevant facts about the bifurcation diagram

The bifurcation diagram we have obtained for the class 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) ¯ \overline{\bf{Q}{{\widehat{ES}(C)}}} is completely coherent, i.e. in this family, by taking any two points in the parameter space and joining them by a continuous curve, along this curve the changes in phase portraits that occur when crossing the different bifurcation surfaces we mention can be completely explained.

Nevertheless, we cannot be sure that this bifurcation diagram is the complete bifurcation diagram for 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) ¯ \overline{\bf{Q}{{\widehat{ES}(C)}}} due to the possibility of the existence of “islands” inside the parts bordered by unmentioned bifurcation surfaces. In case they exist, these “islands” would not mean any modification of the nature of the singular points. So, on the border of these “islands” we could only have bifurcations due to saddle connections.

In case there were more bifurcation surfaces, we should still be able to join two representatives of any two parts of the 14 parts of 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) ¯ \overline{\bf{Q}{{\widehat{ES}(C)}}} found until now with a continuous curve either without crossing such a bifurcation surface or, in case the curve crosses it, it must do it an even number of times without tangencies, otherwise one must take into account the multiplicity of the tangency, so the total number must be even. This is why we call these potential bifurcation surfaces “ islands ”.

However, we have not found a different phase portrait which could fit in such an island. A potential “island” would be the set of parameters for which the phase portraits have a separatrix connection.

#### 3.3.2 Completion of the proof of Theorem 3

In the bifurcation diagram we may have topologically equivalent phase portraits belonging to distinct parts of the parameter space. As here we have 14 distinct parts of the parameter space, to help us to identify or to distinguish phase portraits, we need to introduce some invariants and we actually choose integer valued, character and symbol invariants. Some of them were already used in [12] and [9], but we recall them and introduce some needed ones. These invariants yield a classification which is easier to grasp.

###### Definition 18.

We denote by I 1 ​ ( S) I_{1}(S) a symbol from the set { ∅, [×], [) (] } \{\emptyset,\left[\times\right],\left[)(\right]\} which indicates the following configuration of curves filled up with singularities, respectively: none (nondegenerate systems – in this case all systems do not contain a curve filled up with singularities), two real straight lines intersecting at a finite point, and an hyperbola. This invariant only makes sense to distinguish the degenerate phase portrait obtained.

###### Definition 19.

We denote by I 2 ​ ( S) I_{2}(S) the sum of the indices of the isolated real finite singular points.

###### Definition 20.

We denote by I 3 ​ ( S) I_{3}(S) the number of real infinite singular points. We note that this number can also be infinite, which is represented by ∞ \infty.

###### Definition 21.

For a given infinite singularity s s of a system S S, let ł s \l_{s} be the number of global or local separatrices beginning or ending at s s and which do not lie on the line at infinity. We have 0 ≤ ł s ≤ 2 0\leq\l_{s}\leq 2. We denote by I 4 ​ ( S) I_{4}(S) the sequence of all such ł s \l_{s} when s s moves in the set of infinite singular points of the system S S. We start the sequence at the infinite singular point which receives (or sends) the greatest number of separatrices and take the direction which yields the greatest absolute value, e.g. the values 2100 2100 and 2001 2001 for this invariant are symmetrical (and, therefore, they are the same), so we consider 2100 2100.

###### Definition 22.

We denote by I 5 ​ ( S) I_{5}(S) an element from the set { y, n } \{y,n\} indicating if the phase portrait has ( y y) or has not ( n n) an infinite elliptic sector.

###### Definition 23.

We denote by I 6 ​ ( S) I_{6}(S) an element from the set { y, n } \{y,n\} indicating if the infinite elliptic sector is ( y y) or is not ( n n) bordered by separatrices that connect the finite elliptic–saddle and the infinite multiple point.

###### Theorem 6.

Consider the class 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) ¯ \overline{\bf{Q}{{\widehat{ES}(C)}}} and all the phase portraits that we have obtained for this family. The values of the affine invariant ℐ = ( I 1, I 2, I 3, I 4, I 5, I 6) {\cal I}=(I_{1},I_{2},I_{3},I_{4},I_{5},I_{6}) given in the diagram from Table 22 yields a partition of these phase portraits of the class 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) ¯ \overline{\bf{Q}{{\widehat{ES}(C)}}}.

Furthermore, for each value of ℐ \cal I in this diagram there corresponds a single phase portrait; i.e. S S and S ′ S^{\prime} are such that ℐ ⁡ ( S) = ℐ ⁡ ( S ′) {\cal I}(S)={\cal I}(S^{\prime}), if and only if S S and S ′ S^{\prime} are topologically equivalent.

The bifurcation diagram for 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) ¯ \overline{\bf{Q}{{\widehat{ES}(C)}}} has 14 parts which produce twelve topologically different phase portraits as described in Tables 22 to 23. The remaining two parts do not produce any new phase portrait which was not included in the ten previous ones. The difference is basically the presence of invariant algebraic curves (lines or parabolas) which do not represent a separatrix connection or a presence of an infinite singularity of type ( 1 2) ^ ​ E − H \widehat{\!{1\choose 2}\!\!}\ E-H.

The phase portraits having no graphics have been denoted surrounded by parenthesis, for example ( S 1) (S_{1}) and the phase portraits having two or more graphics have been denoted surrounded by { { ∗ } } \{\!\{\ast\}\!\}, for example { S 2 } \{S_{2}\}.

###### Proof of Theorem 6.

The above result follows from the results in the previous sections and a careful analysis of the bifurcation diagrams given in Fig. 93, the definition of the invariants I j I_{j} and their explicit values for the corresponding phase portraits. ∎

In Table 23 we list in the first column twelve parts with all the distinct phase portraits of Fig. 5. Corresponding to each part listed in column one we have in each row all parts whose phase portraits are topologically equivalent to the phase portrait appearing in column 1 of the same row. In the second column we set all the parts whose systems possess an invariant curve (straight line and/or parabola) not yielding a connection of separatrices and in the third column we put the phase portrait possessing a singularity of type ( 1 2) ^ ​ E − H \widehat{\!{1\choose 2}\!\!}\ E-H at infinity.

Whenever phase portraits appear in a row in a specific column, the listing is done according to the decreasing dimension of the parts where they appear, always placing the lower dimensions on lower lines.

#### 3.3.3 Proof of Theorem 3

The bifurcation diagram described in Sec. 3.3, plus Table 22 of the geometrical invariants distinguishing the ten phase portraits, plus Table 23 giving the equivalences with the remaining phase portraits lead to the proof of Theorem 3.

Table 22: Geometric classification for the family 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) \bf{Q}{{\widehat{ES}(C)}}

 | I 1 = { [) (] { { 1 L 1 } }, [×] ​ { { P 3 } }, ∅ & I 2 = { − 1 ​ { { S 4 } }, 1 & I 3 = { 1 ​ { { 5 ​ L 1 } }, 2 & I 4 = { 1010 ​ { { P 2 } }, 1110 ​ { { S 3 } }, 2100 ​ { { S 1 } }, 2101 & I 5 = { n ​ { { 8 ​ L 1 } }, y & I 6 = { n ​ { { 8 ​ L 2 } }, y ​ { { 8 ​ L 3 } }, 2121 ​ { { S 2 } }, ∞ ​ { { P 1 } }, I_{1}\!=\!\left\{\begin{array}[]{ll}\left[)(\right]\,\,\left\{\left\{1L_{1}\right\}\right\},\\ \left[\times\right]\,\,\left\{\left\{P_{3}\right\}\right\},\\ \emptyset\,\,\&\,\,I_{2}\!=\!\left\{\begin{array}[]{ll}-1\,\,\left\{\left\{S_{4}\right\}\right\},\\ 1\,\,\&\,\,I_{3}\!=\!\left\{\begin{array}[]{ll}1\,\,\left\{\left\{5L_{1}\right\}\right\},\\ 2\,\,\&\,\,I_{4}\!=\!\left\{\begin{array}[]{ll}1010\,\,\left\{\left\{P_{2}\right\}\right\},\\ 1110\,\,\left\{\left\{S_{3}\right\}\right\},\\ 2100\,\,\left\{\left\{S_{1}\right\}\right\},\\ 2101\,\,\&\,\,I_{5}\!=\!\left\{\begin{array}[]{ll}n\,\,\left\{\left\{8L_{1}\right\}\right\},\\ y\,\,\&\,\,I_{6}\!=\!\left\{\begin{array}[]{ll}n\,\,\left\{\left\{8L_{2}\right\}\right\},\\ y\,\,\left\{\left\{8L_{3}\right\}\right\},\\ \end{array}\right.\\ \end{array}\right.\\ 2121\,\,\left\{\left\{S_{2}\right\}\right\},\\ \end{array}\right.\\ \infty\,\,\left\{\left\{P_{1}\right\}\right\},\\ \end{array}\right.\\ \end{array}\right.\\ \end{array}\right. |  |

Table 23: Topological equivalences for the family 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) \bf{Q}{{\widehat{ES}(C)}}

Presented | Possessing | Possessing |

phase | invariant curve | ( 1 2) ^ ​ E − H \widehat{\!{1\choose 2}\!\!}\ E-H |

portrait | (no separatrix) | at infinity |

S 1 S_{1} |  |  |

S 2 S_{2} |  |  |

S 3 S_{3} |  |  |

 |  | 0 ​ L 1 0L_{1} |

S 4 S_{4} |  |  |

 | 8 ​ L 4 8L_{4} |  |

1 ​ L 1 1L_{1} |  |  |

5 ​ L 1 5L_{1} |  |  |

8 ​ L 1 8L_{1} |  |  |

8 ​ L 2 8L_{2} |  |  |

8 ​ L 3 8L_{3} |  |  |

P 1 P_{1} |  |  |

P 2 P_{2} |  |  |

P 3 P_{3} |  |  |

Acknowledgements. The first author is partially supported by a MEC/FEDER grant number MTM 2016–77278–P and by a CICYT grant number 2017 SGR 1617. The second author was partially supported by Conselho Nacional de Desenvolvimento Científico e Tecnológico (CNPq) grant number 166449/2020-2. The third author is partially supported by Coordenação de Aperfeiçoamento de Pessoal de Nivel Superior - Brazil (CAPES) and by Fundação de Amparo à Pesquisa do Estado de São Paulo (FAPESP) grants 2018/21320-7 and 2019/21181-0.

## Appendix A Some incompatibilities in previous classifications

It is quite common that by performing the study of a bifurcation diagram that produces some specific types of phase portraits, the authors lose one or several phase portraits. This may happen either because they do not interpret correctly some of the bifurcation parts or they miss the existence of some nonalgebraic bifurcations.

In [8] we have decided to start comparing our classification of phase portraits with already existing classifications. As we have mentioned in that occasion, we plan to do this section in every future work related to classification of phase portraits using normal forms. The aim of this study is to detect some incompatibilities in previous papers and also to help us look carefully our bifurcation diagram in order to do not lose any phase portrait. Such incompatibilities are obtained after we compare all of the phase portraits obtained in our bifurcation diagram with phase portraits from some previous papers which possess the same topological configuration of singularities, according to Def. 1 in [5].

This study also allows the corresponding authors to detect possible mistakes on their works. There are some previous papers which are not based on normal forms, but which seek all topological realizable phase portraits of a certain codimension (see [2, 3, 11, 10]). We have also crossed results from all the consulted papers with them and no discrepancy has been found. Additionally, with this study we are creating a data basis containing all the obtained phase portraits, specially containing those phase portraits obtained in our topological studies, in order to create an “encyclopedia” of phase portraits from quadratic differential systems.

In this paper we are dealing with phase portraits possessing either an infinite nilpotent elliptic–saddle or an infinite nilpotent saddle. Regarding the already existing studies related to this paper, in [17] the authors provide a list of phase portraits that have intersection with our investigation. We decided to perform a careful analysis of the phase portraits they present and also to compare their phase portraits with the ones we obtained.

By doing this study, we have detected some interesting phenomena and also some incompatibilities in the mentioned paper. We observe that there are phase portraits in [17] which are topologically equivalent, and this fact allowed us to create sets of topologically equivalent phase portraits. In what follows we present such sets. In each set the elements (i.e. phase portraits from that paper) are displayed in lines, where in each line we indicate the figure of that paper in which the phase portrait appears, followed by the caption of that phase portrait (using the notation of the paper under consideration), so one can easily identify all of them in the mentioned paper.

{ FIGURE 10.1: γ < 0 and μ = 0, FIGURE 10.1: γ < 0 and μ > 0, FIGURE 10.5: δ > 0 and μ = 0, FIGURE 10.5: δ > 0 and μ > 0, FIGURE 10.5: δ = 0 and μ = 0, FIGURE 10.5: δ = 0 and μ > 0, FIGURE 11.1: μ > 0 and γ < − 1 4 ​ μ, FIGURE 11.5c: μ > − 1 4 ​ γ and γ < 0 }, \left\{\!\!\begin{array}[]{c}\text{FIGURE 10.1:}\ \gamma<0\ \text{and}\ \mu=0,\\ \text{FIGURE 10.1:}\ \gamma<0\ \text{and}\ \mu>0,\\ \text{FIGURE 10.5:}\ \delta>0\ \text{and}\ \mu=0,\\ \text{FIGURE 10.5:}\ \delta>0\ \text{and}\ \mu>0,\\ \text{FIGURE 10.5:}\ \delta=0\ \text{and}\ \mu=0,\\ \text{FIGURE 10.5:}\ \delta=0\ \text{and}\ \mu>0,\\ \text{FIGURE 11.1:}\ \mu>0\ \text{and}\ \gamma<-\frac{1}{4\mu},\\ \text{FIGURE 11.5c:}\ \mu>-\frac{1}{4\gamma}\ \text{and}\ \gamma<0\\ \end{array}\!\!\right\}\!,

{ FIGURE 10.1: γ = 2 and μ = 0, FIGURE 10.2: γ = 2 and μ = δ = 0 }, \left\{\!\!\begin{array}[]{c}\text{FIGURE 10.1:}\ \gamma=2\ \text{and}\ \mu=0,\\ \text{FIGURE 10.2:}\ \gamma=2\ \text{and}\ \mu=\delta=0\\ \end{array}\!\!\right\}\!,

{ FIGURE 10.1: γ > 2 and μ = 0, FIGURE 10.2: γ > 2 and μ = δ = 0 }, \left\{\!\!\begin{array}[]{c}\text{FIGURE 10.1:}\ \gamma>2\ \text{and}\ \mu=0,\\ \text{FIGURE 10.2:}\ \gamma>2\ \text{and}\ \mu=\delta=0\\ \end{array}\!\!\right\}\!,

{ FIGURE 10.1: 0 < γ < 1 and μ = 0, FIGURE 10.4: μ = δ = 0 }, \left\{\!\!\begin{array}[]{c}\text{FIGURE 10.1:}\ 0<\gamma<1\ \text{and}\ \mu=0,\\ \text{FIGURE 10.4:}\ \mu=\delta=0\\ \end{array}\!\!\right\}\!,

{ FIGURE 10.1: 1 < γ < 2 and μ = 0, FIGURE 10.3: μ = δ = 0 }, \left\{\!\!\begin{array}[]{c}\text{FIGURE 10.1:}\ 1<\gamma<2\ \text{and}\ \mu=0,\\ \text{FIGURE 10.3:}\ \mu=\delta=0\\ \end{array}\!\!\right\}\!,

{ FIGURE 10.1: 2 < γ and μ < 0, FIGURE 10.1: γ = 2 and μ < 0, FIGURE 10.2: κ = − ∞ }, \left\{\!\!\begin{array}[]{c}\text{FIGURE 10.1:}\ 2<\gamma\ \text{and}\ \mu<0,\\ \text{FIGURE 10.1:}\ \gamma=2\ \text{and}\ \mu<0,\\ \text{FIGURE 10.2:}\ \kappa=-\infty\\ \end{array}\!\!\right\}\!,

{ FIGURE 10.2: κ = 0, FIGURE 10.2: − ∞ < κ < 0, FIGURE 11.1: γ > 2 and μ < − 1 4 ​ γ, FIGURE 11.2: d > d 1 ( m; g), FIGURE 11.2: d ε − 1 }, \left\{\!\!\begin{array}[]{c}\text{FIGURE 10.2:}\ \kappa=0,\\ \text{FIGURE 10.2:}\ -\infty<\kappa<0,\\ \text{FIGURE 11.1:}\ \gamma>2\ \text{and}\ \mu<-\frac{1}{4\gamma},\\ \text{FIGURE 11.2:}\ d>d_{1}(m;g),\\ \text{FIGURE 11.2:}\ d^{\varepsilon}-1\\ \end{array}\!\!\right\}\!,

{ FIGURE 10.1: 0 < γ < 1 and μ < 0, FIGURE 10.4: κ = − ∞ }, \left\{\!\!\begin{array}[]{c}\text{FIGURE 10.1:}\ 0<\gamma<1\ \text{and}\ \mu<0,\\ \text{FIGURE 10.4:}\ \kappa=-\infty\\ \end{array}\!\!\right\}\!,

{ FIGURE 10.4: κ = 0, FIGURE 10.4: − ∞ < κ < 0, FIGURE 11.1: 0 < γ < 1 and μ < − 1 4 ​ γ, FIGURE 11.4: δ > δ 1 ( μ; γ), FIGURE 11.4: δ ≤ − 1 }, \left\{\!\!\begin{array}[]{c}\text{FIGURE 10.4:}\ \kappa=0,\\ \text{FIGURE 10.4:}\ -\infty<\kappa<0,\\ \text{FIGURE 11.1:}\ 0<\gamma<1\ \text{and}\ \mu<-\frac{1}{4\gamma},\\ \text{FIGURE 11.4:}\ \delta>\delta_{1}(\mu;\gamma),\\ \text{FIGURE 11.4:}\ \delta\leq-1\\ \end{array}\!\!\right\}\!,

{ FIGURE 10.1: 1 < γ < 2 and μ < 0, FIGURE 10.3: κ = − ∞ }, \left\{\!\!\begin{array}[]{c}\text{FIGURE 10.1:}\ 1<\gamma<2\ \text{and}\ \mu<0,\\ \text{FIGURE 10.3:}\ \kappa=-\infty\\ \end{array}\!\!\right\}\!,

{ FIGURE 10.3: κ = κ 5, FIGURE 11.1: u.s.c., FIGURE 11.3c: δ = δ 4 ( μ; γ), FIGURE 11.3c: δ = δ 7 ( μ; γ) < − 1 }, \left\{\!\!\begin{array}[]{c}\text{FIGURE 10.3:}\ \kappa=\kappa_{5},\\ \text{FIGURE 11.1:}\ \text{u.s.c.},\\ \text{FIGURE 11.3c:}\ \delta=\delta_{4}(\mu;\gamma),\\ \text{FIGURE 11.3c:}\ \delta=\delta_{7}(\mu;\gamma)<-1\\ \end{array}\!\!\right\}\!,

{ FIGURE 10.3: κ = 0, FIGURE 10.3: κ 5 < κ < 0, FIGURE 11.1: 1 < γ < 2 and u.s.c. < μ < − 1 4 ​ γ, FIGURE 11.3c: δ > δ 4 ( μ; γ), FIGURE 11.3c: δ < δ ∗ ⁣ ∗ }, \left\{\!\!\begin{array}[]{c}\text{FIGURE 10.3:}\ \kappa=0,\\ \text{FIGURE 10.3:}\ \kappa_{5}<\kappa<0,\\ \text{FIGURE 11.1:}\ 1<\gamma<2\ \text{and}\ \text{u.s.c.}<\mu<-\frac{1}{4\gamma},\\ \text{FIGURE 11.3c:}\ \delta>\delta_{4}(\mu;\gamma),\\ \text{FIGURE 11.3c:}\ \delta<\delta^{\ast\ast}\\ \end{array}\!\!\right\}\!,

{ FIGURE 10.3: − ∞ < κ < κ 5, FIGURE 11.1: 1 < γ < 2 and μ < u.s.c., FIGURE 11.3c: δ 5 ( μ; γ) < δ < δ 4 ( μ; γ), FIGURE 11.3c: δ 7 ( μ; γ) < δ ≤ − 1 }, \left\{\!\!\begin{array}[]{c}\text{FIGURE 10.3:}\ -\infty<\kappa<\kappa_{5},\\ \text{FIGURE 11.1:}\ 1<\gamma<2\ \text{and}\ \mu<\text{u.s.c.},\\ \text{FIGURE 11.3c:}\ \delta_{5}(\mu;\gamma)<\delta<\delta_{4}(\mu;\gamma),\\ \text{FIGURE 11.3c:}\ \delta_{7}(\mu;\gamma)<\delta\leq-1\\ \end{array}\!\!\right\}\!,

{ FIGURE 11.1: γ < 0 and μ = 0, FIGURE 11.5c: μ = 0, γ < 0, and δ > δ 1 ( 0; γ) }, \left\{\!\!\begin{array}[]{c}\text{FIGURE 11.1:}\ \gamma<0\ \text{and}\ \mu=0,\\ \text{FIGURE 11.5c:}\ \mu=0,\gamma<0,\ \text{and}\ \delta>\delta_{1}(0;\gamma)\\ \end{array}\!\!\right\}\!,

{ FIGURE 11.1: γ > 2 and μ = 0, FIGURE 11.2: d = 0 }, \left\{\!\!\begin{array}[]{c}\text{FIGURE 11.1:}\ \gamma>2\ \text{and}\ \mu=0,\\ \text{FIGURE 11.2:}\ d=0\\ \end{array}\!\!\right\}\!,

{ FIGURE 11.1: 0 < γ < 1 and μ = 0, FIGURE 11.4: δ 1 ∗ ( 0; γ) < δ < δ 1 ( 0; γ) }, \left\{\!\!\begin{array}[]{c}\text{FIGURE 11.1:}\ 0<\gamma<1\ \text{and}\ \mu=0,\\ \text{FIGURE 11.4:}\ \delta_{1}^{\ast}(0;\gamma)<\delta<\delta_{1}(0;\gamma)\\ \end{array}\!\!\right\}\!,

{ FIGURE 11.1: 1 < γ < 2 and μ = 0, FIGURE 11.3d: δ = 0 }, \left\{\!\!\begin{array}[]{c}\text{FIGURE 11.1:}\ 1<\gamma<2\ \text{and}\ \mu=0,\\ \text{FIGURE 11.3d:}\ \delta=0\\ \end{array}\!\!\right\}\!,

{ FIGURE 10.1: γ < 0 and μ < 0, FIGURE 10.5: δ = 0 and μ < 0 }, \left\{\!\!\begin{array}[]{c}\text{FIGURE 10.1:}\ \gamma<0\ \text{and}\ \mu<0,\\ \text{FIGURE 10.5:}\ \delta=0\ \text{and}\ \mu<0\\ \end{array}\!\!\right\}\!,

{ FIGURE 10.5: δ > 0 and μ < 0, FIGURE 11.1: γ < 0 and μ < 0, FIGURE 11.5c: μ < 0, − 2 < γ < 0, and δ > δ 1 ( μ; γ), FIGURE 11.5c: μ < 0, − 2 < γ < 0, and δ > δ 3 ( μ; γ) }, \left\{\!\!\begin{array}[]{c}\text{FIGURE 10.5:}\ \delta>0\ \text{and}\ \mu<0,\\ \text{FIGURE 11.1:}\ \gamma<0\ \text{and}\ \mu<0,\\ \text{FIGURE 11.5c:}\ \mu<0,-2<\gamma<0,\ \text{and}\ \delta>\delta_{1}(\mu;\gamma),\\ \text{FIGURE 11.5c:}\ \mu<0,-2<\gamma<0,\ \text{and}\ \delta>\delta_{3}(\mu;\gamma)\\ \end{array}\!\!\right\}\!,

{ FIGURE 11.5c: μ < 0, − 2 < γ < 0, and δ = δ 2 ( μ; γ), FIGURE 11.5c: μ < 0, γ > − 2, and δ = δ 2 ( μ; γ) }, \left\{\!\!\begin{array}[]{c}\text{FIGURE 11.5c:}\ \mu<0,-2<\gamma<0,\ \text{and}\ \delta=\delta_{2}(\mu;\gamma),\\ \text{FIGURE 11.5c:}\ \mu<0,\gamma>-2,\ \text{and}\ \delta=\delta_{2}(\mu;\gamma)\\ \end{array}\!\!\right\}\!,

{ FIGURE 10.1: 2 < γ and μ > 0, FIGURE 10.1: γ = 2 and μ > 0, FIGURE 10.2: κ 1 < κ ≤ ∞, FIGURE 11.1: 2 < γ and μ > 0 }, \left\{\!\!\begin{array}[]{c}\text{FIGURE 10.1:}\ 2<\gamma\ \text{and}\ \mu>0,\\ \text{FIGURE 10.1:}\ \gamma=2\ \text{and}\ \mu>0,\\ \text{FIGURE 10.2:}\ \kappa_{1}<\kappa\leq\infty,\\ \text{FIGURE 11.1:}\ 2<\gamma\ \text{and}\ \mu>0\\ \end{array}\!\!\right\}\!,

{ FIGURE 10.1: 0 < γ < 1 and μ > 0, FIGURE 10.4: κ 1 < κ ≤ ∞, FIGURE 11.1: 0 < γ < 1 and μ > 0 }, \left\{\!\!\begin{array}[]{c}\text{FIGURE 10.1:}\ 0<\gamma<1\ \text{and}\ \mu>0,\\ \text{FIGURE 10.4:}\ \kappa_{1}<\kappa\leq\infty,\\ \text{FIGURE 11.1:}\ 0<\gamma<1\ \text{and}\ \mu>0\\ \end{array}\!\!\right\}\!, and

{ FIGURE 10.1: 1 < γ < 2 and μ > 0, FIGURE 10.3: κ 1 < κ ≤ ∞, FIGURE 11.1: 1 < γ < 2 and μ > 0 }. \left\{\!\!\begin{array}[]{c}\text{FIGURE 10.1:}\ 1<\gamma<2\ \text{and}\ \mu>0,\\ \text{FIGURE 10.3:}\ \kappa_{1}<\kappa\leq\infty,\\ \text{FIGURE 11.1:}\ 1<\gamma<2\ \text{and}\ \mu>0\\ \end{array}\!\!\right\}\!.

We also have a correspondence between the phase portraits from the paper under consideration and the phase portraits we obtained in our study (the reader may remember Table 4 of topological equivalence between phase portraits from families 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) \bf{Q}{{\widehat{ES}(B)}} and 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) \bf{Q}{{\widehat{ES}(C)}}). And most important, there is not a single phase portrait in [17] which is absent in our study. In case that happened and the phase portrait were confirmed to exist, we would have a gap in this study.

Table 24: Correspondence between phase portraits from [17] and phase portraits obtained from the studies of the bifurcation diagrams of families 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) \bf{Q}{{\widehat{ES}(A)}}, 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) \bf{Q}{{\widehat{ES}(B)}}, and 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) \bf{Q}{{\widehat{ES}(C)}}. In the first column we refer to the figures from [17], in the second column we list the phase portraits which appear in that figures (using the notation of that paper), and in the third column we indicate the corresponding phase portrait we obtained from the study of families 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) \bf{Q}{{\widehat{ES}(A)}}, 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) \bf{Q}{{\widehat{ES}(B)}}, or 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) \bf{Q}{{\widehat{ES}(C)}}

FIGURE | Phase portrait | Correspondent in families |

[17] | 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) \bf{Q}{{\widehat{ES}(A)}}, 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) \bf{Q}{{\widehat{ES}(B)}}, or 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) \bf{Q}{{\widehat{ES}(C)}} |

10.1 | γ > 2 \gamma>2 | μ < 0 \mu<0 | 4.8 ​ L 3 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) 4.8L_{3}-\bf{Q}{{\widehat{ES}(B)}} |

μ = 0 \mu=0 | 8 ​ L 3 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) 8L_{3}-\bf{Q}{{\widehat{ES}(C)}} |

μ > 0 \mu>0 | V 101 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) V_{101}-\bf{Q}{{\widehat{ES}(A)}} |

γ = 2 \gamma=2 | μ < 0 \mu<0 | 4.8 ​ L 3 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) 4.8L_{3}-\bf{Q}{{\widehat{ES}(B)}} |

μ = 0 \mu=0 | P 2 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) P_{2}-\bf{Q}{{\widehat{ES}(C)}} |

μ > 0 \mu>0 | V 101 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) V_{101}-\bf{Q}{{\widehat{ES}(A)}} |

1 < γ < 2 1<\gamma<2 | μ < 0 \mu<0 | 4.8 ​ L 4 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) 4.8L_{4}-\bf{Q}{{\widehat{ES}(B)}} |

μ = 0 \mu=0 | 8 ​ L 2 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) 8L_{2}-\bf{Q}{{\widehat{ES}(C)}} |

μ > 0 \mu>0 | V 188 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) V_{188}-\bf{Q}{{\widehat{ES}(A)}} |

0 < γ < 1 0<\gamma<1 | μ < 0 \mu<0 | 4.8 ​ L 5 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) 4.8L_{5}-\bf{Q}{{\widehat{ES}(B)}} |

μ = 0 \mu=0 | 8 ​ L 1 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) 8L_{1}-\bf{Q}{{\widehat{ES}(C)}} |

μ > 0 \mu>0 | V 240 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) V_{240}-\bf{Q}{{\widehat{ES}(A)}} |

γ < 0 \gamma<0 | μ < 0 \mu<0 | 4.8 ​ L 2 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 4.8L_{2}-\bf{Q}{{\widehat{ES}(A)}} |

μ = 0 \mu=0 | V 1 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) V_{1}-\bf{Q}{{\widehat{ES}(B)}} |

μ > 0 \mu>0 | V 1 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) V_{1}-\bf{Q}{{\widehat{ES}(B)}} |

10.2 | κ = 0 \kappa=0 | V 5 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) V_{5}-\bf{Q}{{\widehat{ES}(B)}} |

0 < κ ≤ κ 3 0<\kappa\leq\kappa_{3} | V 89 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) V_{89}-\bf{Q}{{\widehat{ES}(A)}} |

κ 3 < κ < κ 2 \kappa_{3}<\kappa<\kappa_{2} | V 91 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) V_{91}-\bf{Q}{{\widehat{ES}(A)}} |

− ∞ < κ < 0 -\infty<\kappa<0 | V 5 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) V_{5}-\bf{Q}{{\widehat{ES}(B)}} |

κ = − ∞ \kappa=-\infty | 4.8 ​ L 3 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) 4.8L_{3}-\bf{Q}{{\widehat{ES}(B)}} |

κ = κ 2 \kappa=\kappa_{2} | 7 ​ S 7 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 7S_{7}-\bf{Q}{{\widehat{ES}(A)}} |

κ 2 < κ < κ 1 \kappa_{2}<\kappa<\kappa_{1} | V 94 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) V_{94}-\bf{Q}{{\widehat{ES}(A)}} |

κ = κ 1 \kappa=\kappa_{1} | 4 ​ S 34 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 4S_{34}-\bf{Q}{{\widehat{ES}(A)}} |

κ 1 < κ ≤ ∞ \kappa_{1}<\kappa\leq\infty | V 101 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) V_{101}-\bf{Q}{{\widehat{ES}(A)}} |

μ = δ = 0 \mu=\delta=0 | γ = 2 \gamma=2 | P 2 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) P_{2}-\bf{Q}{{\widehat{ES}(C)}} |

γ > 2 \gamma>2 | 8 ​ L 3 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) 8L_{3}-\bf{Q}{{\widehat{ES}(C)}} |

Table 25: Continuation of Table 24

FIGURE | Phase portrait | Correspondent in families |

[17] | 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) \bf{Q}{{\widehat{ES}(A)}}, 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) \bf{Q}{{\widehat{ES}(B)}}, or 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) \bf{Q}{{\widehat{ES}(C)}} |

10.3 | κ = 0 \kappa=0 | V 12 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) V_{12}-\bf{Q}{{\widehat{ES}(B)}} |

0 < κ ≤ κ 4 0<\kappa\leq\kappa_{4} | V 168 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) V_{168}-\bf{Q}{{\widehat{ES}(A)}} |

κ 4 < κ < κ 3 \kappa_{4}<\kappa<\kappa_{3} | V 170 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) V_{170}-\bf{Q}{{\widehat{ES}(A)}} |

κ = κ 3 \kappa=\kappa_{3} | 7 ​ S 11 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 7S_{11}-\bf{Q}{{\widehat{ES}(A)}} |

κ 3 < κ < κ 2 \kappa_{3}<\kappa<\kappa_{2} | V 173 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) V_{173}-\bf{Q}{{\widehat{ES}(A)}} |

κ 5 < κ < 0 \kappa_{5}<\kappa<0 | V 12 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) V_{12}-\bf{Q}{{\widehat{ES}(B)}} |

κ = κ 5 \kappa=\kappa_{5} | 7 ​ S 1 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) 7S_{1}-\bf{Q}{{\widehat{ES}(B)}} |

− ∞ < κ < κ 5 -\infty<\kappa<\kappa_{5} | V 14 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) V_{14}-\bf{Q}{{\widehat{ES}(B)}} |

κ = κ 2 \kappa=\kappa_{2} | 8 ​ S 77 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 8S_{77}-\bf{Q}{{\widehat{ES}(A)}} |

κ 2 < κ < κ 1 \kappa_{2}<\kappa<\kappa_{1} | V 176 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) V_{176}-\bf{Q}{{\widehat{ES}(A)}} |

κ = κ 1 \kappa=\kappa_{1} | 4 ​ S 59 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 4S_{59}-\bf{Q}{{\widehat{ES}(A)}} |

κ = − ∞ \kappa=-\infty | 4.8 ​ L 4 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) 4.8L_{4}-\bf{Q}{{\widehat{ES}(B)}} |

μ = δ = 0 \mu=\delta=0 | 8 ​ L 2 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) 8L_{2}-\bf{Q}{{\widehat{ES}(C)}} |

κ 1 < κ ≤ ∞ \kappa_{1}<\kappa\leq\infty | V 188 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) V_{188}-\bf{Q}{{\widehat{ES}(A)}} |

10.4 | κ = 0 \kappa=0 | V 20 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) V_{20}-\bf{Q}{{\widehat{ES}(B)}} |

0 < κ ≤ κ 3 0<\kappa\leq\kappa_{3} | V 233 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) V_{233}-\bf{Q}{{\widehat{ES}(A)}} |

κ 3 < κ < κ 2 \kappa_{3}<\kappa<\kappa_{2} | V 235 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) V_{235}-\bf{Q}{{\widehat{ES}(A)}} |

− ∞ < κ < 0 -\infty<\kappa<0 | V 20 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) V_{20}-\bf{Q}{{\widehat{ES}(B)}} |

κ = − ∞ \kappa=-\infty | 4.8 ​ L 5 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) 4.8L_{5}-\bf{Q}{{\widehat{ES}(B)}} |

μ = δ = 0 \mu=\delta=0 | 8 ​ L 1 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) 8L_{1}-\bf{Q}{{\widehat{ES}(C)}} |

κ = κ 2 \kappa=\kappa_{2} | 7 ​ S 15 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 7S_{15}-\bf{Q}{{\widehat{ES}(A)}} |

κ 2 < κ < κ 1 \kappa_{2}<\kappa<\kappa_{1} | V 238 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) V_{238}-\bf{Q}{{\widehat{ES}(A)}} |

κ = κ 1 \kappa=\kappa_{1} | 8 ​ S 99 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 8S_{99}-\bf{Q}{{\widehat{ES}(A)}} |

κ 1 < κ ≤ ∞ \kappa_{1}<\kappa\leq\infty | V 240 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) V_{240}-\bf{Q}{{\widehat{ES}(A)}} |

10.5 | δ > 0 \delta>0 | μ < 0 \mu<0 | V 1 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) V_{1}-\bf{Q}{{\widehat{ES}(A)}} |

μ = 0 \mu=0 | V 1 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) V_{1}-\bf{Q}{{\widehat{ES}(B)}} |

μ > 0 \mu>0 | V 1 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) V_{1}-\bf{Q}{{\widehat{ES}(B)}} |

δ = 0 \delta=0 | μ < 0 \mu<0 | 4.8 ​ L 2 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 4.8L_{2}-\bf{Q}{{\widehat{ES}(A)}} |

μ = 0 \mu=0 | V 1 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) V_{1}-\bf{Q}{{\widehat{ES}(B)}} |

μ > 0 \mu>0 | V 1 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) V_{1}-\bf{Q}{{\widehat{ES}(B)}} |

Table 26: Continuation of Table 25

FIGURE | Phase portrait | Correspondent in families |

[17] | 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) \bf{Q}{{\widehat{ES}(A)}}, 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) \bf{Q}{{\widehat{ES}(B)}}, or 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) \bf{Q}{{\widehat{ES}(C)}} |

11.1 | γ > 2 \gamma>2 | μ < − 1 4 ​ γ \mu<-\frac{1}{4\gamma} | V 5 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) V_{5}-\bf{Q}{{\widehat{ES}(B)}} |

μ = 0 \mu=0 | 2.4 ​ L 5 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 2.4L_{5}-\bf{Q}{{\widehat{ES}(A)}} |

μ > 0 \mu>0 | V 101 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) V_{101}-\bf{Q}{{\widehat{ES}(A)}} |

1 < γ < 2 1<\gamma<2 | μ = u.s.c. \mu=\text{u.s.c.} | 7 ​ S 1 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) 7S_{1}-\bf{Q}{{\widehat{ES}(B)}} |

μ < u.s.c. \mu<\text{u.s.c.} | V 14 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) V_{14}-\bf{Q}{{\widehat{ES}(B)}} |

u.s.c. < μ < − 1 4 ​ γ \text{u.s.c.}<\mu<-\frac{1}{4\gamma} | V 12 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) V_{12}-\bf{Q}{{\widehat{ES}(B)}} |

μ = 0 \mu=0 | 2.4 ​ L 7 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 2.4L_{7}-\bf{Q}{{\widehat{ES}(A)}} |

μ > 0 \mu>0 | V 188 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) V_{188}-\bf{Q}{{\widehat{ES}(A)}} |

0 < γ < 1 0<\gamma<1 | μ < − 1 4 ​ γ \mu<-\frac{1}{4\gamma} | V 20 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) V_{20}-\bf{Q}{{\widehat{ES}(B)}} |

μ = 0 \mu=0 | 2 ​ S 35 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 2S_{35}-\bf{Q}{{\widehat{ES}(A)}} |

μ > 0 \mu>0 | V 240 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) V_{240}-\bf{Q}{{\widehat{ES}(A)}} |

γ < 0 \gamma<0 | μ < 0 \mu<0 | V 1 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) V_{1}-\bf{Q}{{\widehat{ES}(A)}} |

μ = 0 \mu=0 | 2 ​ S 6 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 2S_{6}-\bf{Q}{{\widehat{ES}(A)}} |

μ > − 1 4 ​ γ \mu>-\frac{1}{4\gamma} | V 1 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) V_{1}-\bf{Q}{{\widehat{ES}(B)}} |

11.2 | d > d 1 ​ ( m, g) d>d_{1}(m;g) | V 5 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) V_{5}-\bf{Q}{{\widehat{ES}(B)}} |

d = d 1 ​ ( m, g) d=d_{1}(m;g) | 4 ​ S 2 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) 4S_{2}-\bf{Q}{{\widehat{ES}(B)}} |

− 1 < d < d 1 ​ ( m, g) -1<d<d_{1}(m;g) | V 9 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) V_{9}-\bf{Q}{{\widehat{ES}(B)}} |

d ε − 1 d^{\varepsilon}-1 | V 5 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) V_{5}-\bf{Q}{{\widehat{ES}(B)}} |

d 2 ​ ( 0, g) < d < d − ​ ( 0, g) d_{2}(0;g)<d<d_{-}(0;g) | 2 ​ S 18 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 2S_{18}-\bf{Q}{{\widehat{ES}(A)}} |

0 < d < d 2 ​ ( 0, g) 0<d<d_{2}(0;g) | 2 ​ S 17 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 2S_{17}-\bf{Q}{{\widehat{ES}(A)}} |

d 1 ​ ( 0, g) < d < 0 d_{1}(0;g)<d<0 | 2 ​ S 13 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 2S_{13}-\bf{Q}{{\widehat{ES}(A)}} |

− 1 < d < d 1 ​ ( 0, g) -1<d<d_{1}(0;g) | 2 ​ S 12 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 2S_{12}-\bf{Q}{{\widehat{ES}(A)}} |

d < − 1 d<-1 | 2 ​ S 11 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 2S_{11}-\bf{Q}{{\widehat{ES}(A)}} |

d 3 ​ d − ​ ( 0, g) = 2 g d^{3}d_{-}(0;g)=\frac{2}{g} | 2 ​ S 20 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 2S_{20}-\bf{Q}{{\widehat{ES}(A)}} |

d = d 2 ​ ( 0, g) d=d_{2}(0;g) | 2.7 ​ L 1 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 2.7L_{1}-\bf{Q}{{\widehat{ES}(A)}} |

d = 0 d=0 | 2.4 ​ L 5 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 2.4L_{5}-\bf{Q}{{\widehat{ES}(A)}} |

d = d 1 ​ ( 0, g) d=d_{1}(0;g) | 2.4 ​ L 4 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 2.4L_{4}-\bf{Q}{{\widehat{ES}(A)}} |

d = − 1 d=-1 | 2.3 ​ L 7 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 2.3L_{7}-\bf{Q}{{\widehat{ES}(A)}} |

Table 27: Continuation of Table 26

FIGURE | Phase portrait | Correspondent in families |

[17] | 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) \bf{Q}{{\widehat{ES}(A)}}, 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) \bf{Q}{{\widehat{ES}(B)}}, or 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) \bf{Q}{{\widehat{ES}(C)}} |

11.3c | δ > δ 4 ​ ( μ, γ) \delta>\delta_{4}(\mu;\gamma) | V 12 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) V_{12}-\bf{Q}{{\widehat{ES}(B)}} |

δ = δ 4 ​ ( μ, γ) \delta=\delta_{4}(\mu;\gamma) | 7 ​ S 1 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) 7S_{1}-\bf{Q}{{\widehat{ES}(B)}} |

δ 5 ​ ( μ, γ) < δ < δ 4 ​ ( μ, γ) \delta_{5}(\mu;\gamma)<\delta<\delta_{4}(\mu;\gamma) | V 14 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) V_{14}-\bf{Q}{{\widehat{ES}(B)}} |

δ = δ 5 ​ ( μ, γ) \delta=\delta_{5}(\mu;\gamma) | 4 ​ S 3 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) 4S_{3}-\bf{Q}{{\widehat{ES}(B)}} |

δ 6 ​ ( μ, γ) < δ < δ 5 ​ ( μ, γ) \delta_{6}(\mu;\gamma)<\delta<\delta_{5}(\mu;\gamma) | V 15 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) V_{15}-\bf{Q}{{\widehat{ES}(B)}} |

δ = δ 6 ​ ( μ, γ) \delta=\delta_{6}(\mu;\gamma) | 8 ​ S 4 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) 8S_{4}-\bf{Q}{{\widehat{ES}(B)}} |

δ ∗ < δ < δ 6 ​ ( μ, γ) \delta^{\ast}<\delta<\delta_{6}(\mu;\gamma) | V 16 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) V_{16}-\bf{Q}{{\widehat{ES}(B)}} |

δ 7 ​ ( μ, γ) < δ ≤ − 1 \delta_{7}(\mu;\gamma)<\delta\leq-1 | V 14 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) V_{14}-\bf{Q}{{\widehat{ES}(B)}} |

δ = δ 7 ​ ( μ, γ) < − 1 \delta=\delta_{7}(\mu;\gamma)<-1 | 7 ​ S 1 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) 7S_{1}-\bf{Q}{{\widehat{ES}(B)}} |

δ = δ 7 ​ ( μ, γ) > − 1 \delta=\delta_{7}(\mu;\gamma)>-1 | 7 ​ S 2 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) 7S_{2}-\bf{Q}{{\widehat{ES}(B)}} |

− 1 < δ < δ 7 ​ ( μ, γ) -1<\delta<\delta_{7}(\mu;\gamma) | V 17 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) V_{17}-\bf{Q}{{\widehat{ES}(B)}} |

δ < δ ∗ ⁣ ∗ \delta<\delta^{\ast\ast} | V 12 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) V_{12}-\bf{Q}{{\widehat{ES}(B)}} |

11.3d | δ ≥ δ − ​ ( 0, γ) \delta\geq\delta_{-}(0;\gamma) | 2 ​ S 32 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 2S_{32}-\bf{Q}{{\widehat{ES}(A)}} |

δ 3 ​ ( 0, γ) < δ < δ − ​ ( 0, γ) \delta_{3}(0;\gamma)<\delta<\delta_{-}(0;\gamma) | 2 ​ S 30 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 2S_{30}-\bf{Q}{{\widehat{ES}(A)}} |

δ = δ 3 ​ ( 0, γ) \delta=\delta_{3}(0;\gamma) | 2.7 ​ L 2 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 2.7L_{2}-\bf{Q}{{\widehat{ES}(A)}} |

δ 2 ​ ( 0, γ) < δ < δ 3 ​ ( 0, γ) \delta_{2}(0;\gamma)<\delta<\delta_{3}(0;\gamma) | 2 ​ S 29 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 2S_{29}-\bf{Q}{{\widehat{ES}(A)}} |

δ = δ 2 ​ ( 0, γ) \delta=\delta_{2}(0;\gamma) | 2.8 ​ L 9 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 2.8L_{9}-\bf{Q}{{\widehat{ES}(A)}} |

0 < δ < δ 2 ​ ( 0, γ) 0<\delta<\delta_{2}(0;\gamma) | 2 ​ S 28 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 2S_{28}-\bf{Q}{{\widehat{ES}(A)}} |

δ = 0 \delta=0 | 2.4 ​ L 7 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 2.4L_{7}-\bf{Q}{{\widehat{ES}(A)}} |

δ 1 ∗ ​ ( 0, γ) < δ < 0 \delta_{1}^{\ast}(0;\gamma)<\delta<0 | 2 ​ S 26 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 2S_{26}-\bf{Q}{{\widehat{ES}(A)}} |

δ = δ 1 ∗ ​ ( 0, γ) \delta=\delta_{1}^{\ast}(0;\gamma) | 2.4 ​ L 6 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 2.4L_{6}-\bf{Q}{{\widehat{ES}(A)}} |

δ 2 ∗ ​ ( 0, γ) < δ < δ 1 ∗ ​ ( 0, γ) \delta_{2}^{\ast}(0;\gamma)<\delta<\delta_{1}^{\ast}(0;\gamma) | 2 ​ S 25 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 2S_{25}-\bf{Q}{{\widehat{ES}(A)}} |

δ = δ 2 ∗ ​ ( 0, γ) \delta=\delta_{2}^{\ast}(0;\gamma) | 2.8 ​ L 8 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 2.8L_{8}-\bf{Q}{{\widehat{ES}(A)}} |

− 1 < δ < δ 2 ∗ ​ ( 0, γ) -1<\delta<\delta_{2}^{\ast}(0;\gamma) | 2 ​ S 24 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 2S_{24}-\bf{Q}{{\widehat{ES}(A)}} |

δ = − 1 \delta=-1 | 2.3 ​ L 9 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 2.3L_{9}-\bf{Q}{{\widehat{ES}(A)}} |

δ < − 1 \delta<-1 | 2 ​ S 23 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 2S_{23}-\bf{Q}{{\widehat{ES}(A)}} |

Table 28: Continuation of Table 27

FIGURE | Phase portrait | Correspondent in families |

[17] | 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) \bf{Q}{{\widehat{ES}(A)}}, 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) \bf{Q}{{\widehat{ES}(B)}}, or 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) \bf{Q}{{\widehat{ES}(C)}} |

11.4 | δ > δ 1 ​ ( μ, γ) \delta>\delta_{1}(\mu;\gamma) | V 20 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) V_{20}-\bf{Q}{{\widehat{ES}(B)}} |

δ = δ 1 ​ ( μ, γ) \delta=\delta_{1}(\mu;\gamma) | 8 ​ S 5 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) 8S_{5}-\bf{Q}{{\widehat{ES}(B)}} |

− 1 < δ < δ 1 ​ ( μ, γ) -1<\delta<\delta_{1}(\mu;\gamma) | V 24 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) V_{24}-\bf{Q}{{\widehat{ES}(B)}} |

δ ≤ − 1 \delta\leq-1 | V 20 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) V_{20}-\bf{Q}{{\widehat{ES}(B)}} |

δ ≥ δ − ​ ( 0, γ) = 2 γ \delta\geq\delta_{-}(0;\gamma)=\frac{2}{\gamma} | 2 ​ S 42 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 2S_{42}-\bf{Q}{{\widehat{ES}(A)}} |

δ = δ 2 ​ ( 0, γ) \delta=\delta_{2}(0;\gamma) | 2.7 ​ L 3 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 2.7L_{3}-\bf{Q}{{\widehat{ES}(A)}} |

δ = δ 1 ​ ( 0, γ) \delta=\delta_{1}(0;\gamma) | 2.8 ​ L 11 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 2.8L_{11}-\bf{Q}{{\widehat{ES}(A)}} |

δ = δ 1 ∗ ​ ( 0, γ) \delta=\delta_{1}^{\ast}(0;\gamma) | 2.8 ​ L 10 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 2.8L_{10}-\bf{Q}{{\widehat{ES}(A)}} |

δ = − 1 \delta=-1 | 2.3 ​ L 11 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 2.3L_{11}-\bf{Q}{{\widehat{ES}(A)}} |

δ 2 ​ ( 0, γ) < δ < δ − ​ ( 0, γ) \delta_{2}(0;\gamma)<\delta<\delta_{-}(0;\gamma) | 2 ​ S 40 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 2S_{40}-\bf{Q}{{\widehat{ES}(A)}} |

δ 1 ​ ( 0, γ) < δ < δ 2 ​ ( 0, γ) \delta_{1}(0;\gamma)<\delta<\delta_{2}(0;\gamma) | 2 ​ S 39 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 2S_{39}-\bf{Q}{{\widehat{ES}(A)}} |

δ 1 ∗ ​ ( 0, γ) < δ < δ 1 ​ ( 0, γ) \delta_{1}^{\ast}(0;\gamma)<\delta<\delta_{1}(0;\gamma) | 2 ​ S 35 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 2S_{35}-\bf{Q}{{\widehat{ES}(A)}} |

− 1 < δ < δ 1 ∗ ​ ( 0, γ) -1<\delta<\delta_{1}^{\ast}(0;\gamma) | 2 ​ S 34 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 2S_{34}-\bf{Q}{{\widehat{ES}(A)}} |

δ < − 1 \delta<-1 | 2 ​ S 33 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 2S_{33}-\bf{Q}{{\widehat{ES}(A)}} |

11.5c |  | δ > δ 1 ​ ( μ, γ) \delta>\delta_{1}(\mu;\gamma) | V 1 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) V_{1}-\bf{Q}{{\widehat{ES}(A)}} |

 | δ = δ 1 ​ ( μ, γ) \delta=\delta_{1}(\mu;\gamma) | 8 ​ S 7 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 8S_{7}-\bf{Q}{{\widehat{ES}(A)}} |

 | δ 2 ​ ( μ, γ) < δ < δ 1 ​ ( μ, γ) \delta_{2}(\mu;\gamma)<\delta<\delta_{1}(\mu;\gamma) | V 12 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) V_{12}-\bf{Q}{{\widehat{ES}(A)}} |

μ < 0, \mu<0, | δ = δ 2 ​ ( μ, γ) \delta=\delta_{2}(\mu;\gamma) | 7 ​ S 4 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 7S_{4}-\bf{Q}{{\widehat{ES}(A)}} |

− 2 < γ < 0 -2<\gamma<0 | − 1 < δ < δ 2 ​ ( μ, γ) -1<\delta<\delta_{2}(\mu;\gamma) | V 11 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) V_{11}-\bf{Q}{{\widehat{ES}(A)}} |

 | δ 3 ​ ( μ, γ) < δ ≤ − 1 \delta_{3}(\mu;\gamma)<\delta\leq-1 | V 9 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) V_{9}-\bf{Q}{{\widehat{ES}(A)}} |

 | δ = δ 3 ​ ( μ, γ) \delta=\delta_{3}(\mu;\gamma) | 4 ​ S 5 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 4S_{5}-\bf{Q}{{\widehat{ES}(A)}} |

 | δ > δ 3 ​ ( μ, γ) \delta>\delta_{3}(\mu;\gamma) | V 1 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) V_{1}-\bf{Q}{{\widehat{ES}(A)}} |

μ < 0, γ = − 2, δ = − 1 \mu<0,\gamma=-2,\delta=-1 | 3.7 ​ L 1 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 3.7L_{1}-\bf{Q}{{\widehat{ES}(A)}} |

μ ​ < 0, γ > − 2 \mu<0,\gamma>-2 | δ 2 ​ ( μ, γ) < δ < − 1 \delta_{2}(\mu;\gamma)<\delta<-1 | V 66 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) V_{66}-\bf{Q}{{\widehat{ES}(A)}} |

δ = δ 2 ​ ( μ, γ) \delta=\delta_{2}(\mu;\gamma) | 7 ​ S 4 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 7S_{4}-\bf{Q}{{\widehat{ES}(A)}} |

μ = 0, γ < 0 \mu=0,\gamma<0 | δ > δ 1 ​ ( 0, γ) \delta>\delta_{1}(0;\gamma) | 2 ​ S 6 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 2S_{6}-\bf{Q}{{\widehat{ES}(A)}} |

δ = δ 1 ​ ( 0, γ) \delta=\delta_{1}(0;\gamma) | 2.8 ​ L 2 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 2.8L_{2}-\bf{Q}{{\widehat{ES}(A)}} |

− 1 < δ < δ 1 ​ ( 0, γ) -1<\delta<\delta_{1}(0;\gamma) | 2 ​ S 5 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 2S_{5}-\bf{Q}{{\widehat{ES}(A)}} |

δ = − 1 \delta=-1 | 2.3 ​ L 2 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 2.3L_{2}-\bf{Q}{{\widehat{ES}(A)}} |

δ 3 ​ ( 0, γ) < δ < − 1 \delta_{3}(0;\gamma)<\delta<-1 | 2 ​ S 4 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 2S_{4}-\bf{Q}{{\widehat{ES}(A)}} |

δ = δ 3 ​ ( 0, γ) \delta=\delta_{3}(0;\gamma) | 2.4 ​ L 1 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 2.4L_{1}-\bf{Q}{{\widehat{ES}(A)}} |

δ > δ 3 ​ ( 0, γ) \delta>\delta_{3}(0;\gamma) | 2 ​ S 1 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) 2S_{1}-\bf{Q}{{\widehat{ES}(A)}} |

μ > − 1 4 ​ γ, γ < 0 \mu>-\frac{1}{4\gamma},\gamma<0 | V 1 − 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) V_{1}-\bf{Q}{{\widehat{ES}(B)}} |

Therefore, as we proved that the phase portraits we obtained are topologically distinct we conclude that, from the 143 phase portraits from the mentioned paper, the number of topologically distinct phase portraits is indeed 94.

From the analysis of the phase portraits we obtained in the closures 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) ¯ \overline{\bf{Q}{{\widehat{ES}(A)}}}, 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐁) ¯ \overline{\bf{Q}{{\widehat{ES}(B)}}}, and 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐂) ¯ \overline{\bf{Q}{{\widehat{ES}(C)}}}, we observe the existence of 29 phase portraits which were not obtained by those authors. One example is our phase portrait 7 ​ S 1 7S_{1} in 𝐐 ​ 𝐄𝐒 ^ ​ ( 𝐀) ¯ \overline{\bf{Q}{{\widehat{ES}(A)}}} which was not found in [17].

Another relevant fact we want to add in this section is the following one. In [9] we presented a list of some small prints and incompatibilities found in [14]. In addition to that list, we point out that in equation (7), corresponding to slices n 62 n_{62} up to n 69 n_{69}, instead of the value 81 / 40 81/40, the correct is 81 / 400 81/400. This correction must be made in Figures 89 up to 96 and in Tables 33 up to 37 from that paper.

## References

- [1] Artés, J.C., Dumortier, F., Herssens, C., Llibre, J. & de Maesschalck, P. Computer program P4 to study phase portraits of planar polynomial differential equations. Available at: http://mat.uab.es/~artes/p4/p4.htm, 2005.
- [2] Artés, J.C., Kooij, R. & Llibre, J. Structurally stable quadratic vector fields. Memoires Amer. Math. Soc. 134 (639), 1998, 108pp.
- [3] Artés, J.C., Llibre, J. & Rezende, A.C. Structurally unstable quadratic vector fields of codimension one. 1. ed. Birkhäuser. v.1. 2018. 267pp.
- [4] Artés, J.C., Llibre, J. & Schlomiuk, D. The geometry of quadratic differential systems with a weak focus of second order. Internat. J. Bifur. Chaos Appl. Sci. Engrg. 16, 2006, 3127–3194.
- [5] Artés, J.C., Llibre, J., Schlomiuk, D. & Vulpe, N. Global topological configurations of singularities for the whole family of quadratic differential systems. Qual. Theor. Dyn. Syst. 19, 2020a, 32pp.
- [6] Artés, J.C., Llibre, J., Schlomiuk, D. & Vulpe, N. Geometric configurations of singularities of planar polynomial differential systems – A global classification in the quadratic case. 1. ed. Birkhäuser Basel. v.1. 2021a. 701 pp.
- [7] Artés, J.C., Llibre, J. & Vulpe, N. Singular points of quadratic systems: a complete classification in the coefficient space ℝ 12 \mathbb{R}^{12}. Internat. J. Bifur. Chaos Appl. Sci. Engrg. 18, 2008, 313–362.
- [8] Artés, J.C., Mota, M.C. & Rezende, A.C. Quadratic differential systems with a finite saddle–node and an infinite saddle–node ( 1, 1) ​ S ​ N (1,1)SN - (A). Internat. J. Bifur. Chaos Appl. Sci. Engrg. 31(2), 2021b, 2150026 – 24pp.
- [9] Artés, J.C., Mota, M.C. & Rezende, A.C. Quadratic differential systems with a finite saddle–node and an infinite saddle–node ( 1, 1) ​ S ​ N (1,1)SN - (B). Internat. J. Bifur. Chaos Appl. Sci. Engrg. 31(9), 2021c, 2130026 – 110pp.
- [10] Artés, J.C., Mota, M.C. & Rezende, A.C. Structurally unstable quadratic vector fields of codimension two: families possessing a finite saddle-node and an infinite saddle-node. Electron. J. Qual. Theo. 35, 2021d, 1–89.
- [11] Artés, J.C., Oliveira, R.D.S. & Rezende, A.C. Structurally unstable quadratic vector fields of codimension two: families possessing either a cusp point or two finite saddle–nodes. J. Dyn. Diff. Equat. 2020b, 43pp.
- [12] Artés, J.C., Rezende, A.C. & Oliveira, R.D.S. Global phase portraits of quadratic polynomial differential systems with a semi–elemental triple node. Internat. J. Bifur. Chaos Appl. Sci. Engrg. 23, 2013, 21pp.
- [13] Artés, J.C., Rezende, A.C. & Oliveira, R.D.S. The geometry of quadratic polynomial differential systems with a finite and an infinite saddle–node ( A, B) (A,B). Internat. J. Bifur. Chaos Appl. Sci. Engrg. 24, 2014, 30pp.
- [14] Artés, J.C., Rezende, A.C. & Oliveira, R.D.S. The geometry of quadratic polynomial differential systems with a finite and an infinite saddle–node C C. Internat. J. Bifur. Chaos Appl. Sci. Engrg. 25, 2015, 111pp.
- [15] Dumortier, F., Llibre, J. & Artés, J.C. Qualitative Theory of Planar Differential Systems. Universitext, Springer–Verlag, New York–Berlin. 2006.
- [16] Dumortier, F., Roussarie, R. & Rousseau, C. Hilbert’s 16th problem for quadratic vector fields. J. Differential Equations. 110, 1994, 66–133.
- [17] Reyn, J.W. & Huang, X. Phase portraits of quadratics systems with finite multiplicity three and a degenerate critical point at infinity. Rocky MT J Math. 27(3), 1997, 929–978.
- [18] Schlomiuk, D. & Vulpe, N. Planar quadratic vector fields with invariant lines of total multiplicity at least five. Qualitative Theory of Dynamical Systems. 5, 2004, 135–194.
- [19] Schlomiuk, D. & Vulpe, N. Geometry of quadratic differential systems in the neighborhood of the infinity. J. Differential Equations. 215, 2005, 357–400.
- [20] Vulpe, N. Characterization of the finite weak singularities of quadratic systems via invariant theory. Nonlinear Anal. 74, 2011, 6553–6582.

[◄][1][image: ar5iv homepage] [2]
[Feeling lucky?][3] [4]
[Conversion report][5]
[Report an issue][6]
[View original on arXiv][7] [►][8]


## Links

[1]: /html/2312.01221
[2]: /
[3]: /feeling_lucky
[4]: /land_of_honey_and_milk
[5]: /log/2312.01222
[6]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+2312.01222
[7]: https://arxiv.org/pdf/2312.01222
[8]: /html/2312.01223
