> **Excerpt only — read this first.** The complete text is one level down at `research/L0.1/simplex_volume_sections_lasserre.full.md`; open that only when this file does not answer the question, because it is large. Replace this excerpt with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://hal.science/hal-01095071/document | converted from PDF -->

HAL Id: hal-01095071

https://hal.science/hal-01095071v1

Submitted on 15 Dec 2014

HAL is a multi-disciplinary open access archive
for the deposit and dissemination of scientific re-
search documents, whether they are published or not.
The documents may come from teaching and research
institutions in France or abroad, or from public or pri-
vate research centers.
 L’archive ouverte pluridisciplinaire HAL, est des-
tinée au dépôt et à la diffusion de documents scien-
tifiques de niveau recherche, publiés ou non, émanant
des établissements d’enseignement et de recherche
français ou étrangers, des laboratoires publics ou
privés.

HAL Authorization

Volume of slices and sections of the simplex in closed form

Jean-Bernard Lasserre

To cite this version:

Jean-Bernard Lasserre. Volume of slices and sections of the simplex in closed form. Optimization Letters,
2015, 9 (7), pp.1263–1269. ⟨hal-01095071⟩

VOLUME OF SLICES AND SECTIONS OF THE
SIMPLEX IN CLOSED FORM

JEAN B. LASSERRE

Abstract. Given a vector a ∈ Rn, we provide an alternative and
direct proof for the formula of the volume of sections ∆ ∩ {x :
a
T x <= t} and slices ∆ ∩ {x : a
T x = t}, t ∈ R, of the simplex
∆. For slices the formula has already been derived but as a by-
product of the construction of univariate B-Splines. One goal of
the paper is to also show how simple and powerful can be the
Laplace transform technique to derive closed form expression for
some multivariate integrals. It also complements some previous
results obtained for the hypercube [0, 1]n.

1. Introduction

In Marichal and Mossinghof [7] the authors have provided a closed-
form expression of slices and slabs of the unit hypercube cube [0, 1]
n.
In the interesting discussion on the history and applications (e.g. in
probability and statistical mechanics) of this problem, they mention
how similar but earlier results had been already proved, notably by
P´olya in his PhD dissertation. In [7] the authors’ proof relies on a
signed simplicial decomposition of the unit cube and the inclusion-
exclusion principle whereas P´olya’s approach was diﬀerent and related
the volume to some sinc integrals as also did Borwein et al. [3] much
later. For more details the interested reader is referred to [7] and the
references therein.
For the simplex one can ﬁnd several contributions in the literature
for integrating polynomials and deﬁning cubatures formula; see for in-
stance the recent work of Baldoni et al. [2] and the many references
therein. But concerning the slice of a simplex it turns out that a formula
for the volume of the slice has already been derived ... as a by-product
in the construction of univariate B-splines! Indeed as explained in Mic-
chelli [8, pp. 150–153], in their construction of univariate B-splines of
degree n − 1, Curry and Schoenberg showed that they are interpreted

This work was supported by a grant of the PGMO program of the Fondation
Math´ematique Jacques Hadamard (FMJH), Paris).
1

2 JEAN B. LASSERRE

as volumes of slices of a n-simplex! In the description
1 of Chapter 4
in [8] one may even read “This chapter explores the powerful idea of
generating multivariate smooth piecewise polynomials as the volume of
slices of polyhedra.”

Contribution. The goal of this note is to provide a relatively sim-
ple and direct proof for volumes of sections and slices of the simplex
without taking a detour via the theory of univariate B-splines. It also
shows how powerful and “easy” can be Laplace techniques for such
a purpose. We consider sections and slices of the canonical simplex
∆ := {x : e
T x ≤ 1} (where e ∈ Rn is the vector of ones). That is,
given a vector a of the unit sphere S
n−1 and some t ∈ R, we want
to compute the n-dimensional (resp. (n − 1)-dimensional) Lebesgue
volume of the sets

Θ(a, t) := ∆ ∩ { x ∈ Rn : a
T x ≤ t }(1.1) S(a, t) := ∆ ∩ { x ∈ Rn : a
T x = t }(1.2)


*[excerpt ends; 9735 characters not shown — see `research/L0.1/simplex_volume_sections_lasserre.full.md`]*
