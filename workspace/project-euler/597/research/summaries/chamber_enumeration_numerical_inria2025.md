> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/chamber_enumeration_numerical_inria2025.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://inria.hal.science/hal-05002249/document | converted from PDF -->

## What it claims

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

Distributed under a Creative Commons CC BY-ND 4.0 - Attribution - No Derivative Works - International
License

Primal and dual approaches for the chamber enumeration of
real hyperplane arrangements

Jean-Pierre Dussault, Jean Charles Gilbert, Baptiste Plaquevent-Jourdain

To cite this version:

Jean-Pierre Dussault, Jean Charles Gilbert, Baptiste Plaquevent-Jourdain. Primal and dual approaches for
the chamber enumeration of real hyperplane arrangements. Inria - Paris; Université de Sherbrooke (Québec,
Canada). 2025, pp.40. ⟨hal-05002249v3⟩

P…

## Statements it makes

Proposition 3.2 (symmetry characterization). Let A(V, τ ) be a proper arrangement. Then, the
following properties are equivalent:
(i) S(V, τ ) is symmetric,
(ii) τ ∈ R(V T),
(iii) the arrangement is centered.

Proposition 3.3 (symmetry in S(V, τ )).
1) S(V, 0) ⊆ S(V, τ ), with equality if and only if S(V, τ ) is symmetric,
2) Ss(V, τ ) = S(V, 0).

Lemma 3.4 (matroid circuit detection). Suppose that I ⊆ [1 : p] is such that null(V : ,I ) = 1 and
that α ∈ N (V : ,I ) \ {0}. Then, J := {i ∈ I : αi ̸= 0} is a matroid circuit of V and the unique one
included in I.

Proposition 3.7(1) below claims that σ ∈ Ss(V, τ ) when ±σ ∈ S(V, τ ), which justiﬁes a posteriori the
qualiﬁer “symmetric” given to the stem vectors in Ss(V, τ ).
6) A matrix V ∈ Rn×p of rank r has at most ( p
r+1
) circuits and this bound is reached if and only
if the columns of V are in linear general position (deﬁnition 3.13 below) [14]; in that case, the circuits
are exactly the selections of r + 1 columns of V . Since there are 1 or 2 stem vectors per circuit, there
are at most between ( p
r+1) and 2( p
r+1
) stem vectors. These numbers can be exponential in p.

Proposition 3.7 (stem vector properties). Let V ∈ Rn×p and τ ∈ Rp. Then,
1) S(V, τ ) ∩ S(V, −τ ) = Ss(V, τ ) = Ss(V, −τ ),
2) S(V, τ ) ∪ S(V, −τ ) = S(V, 0),
3) Ss(V, τ ) ·∪ Sa(V, τ ) ·∪ Sa(V, −τ ) = S(V, τ ) ·∪ Sa(V, −τ ) = S(V, 0).

Proposition 3.8 (centered arrangement and symmetric stem vector set). For an aﬃne hyper-
plane arrangement, the following properties are equivalent:
(i) the arrangement is centered,
(ii) all the stem vectors are symmetric.

Proposition 3.9 (covering test). For s ∈ {±1}
p,

Proposition 3.10 (properties with S([V ; τ T], 0)). Let A(V, τ ) be an arrangement with V ∈ Rn×p

Proposition 3.11 (circuits of V and [V ; τ T]). Let V ∈ Rn×p and τ ∈ Rp. Then, the following
properties are equivalent:
(i) C(V ) = C([V ; τ T]),
(ii) C(V ) ⊆ C([V ; τ T]),
(iii) τ ∈ R(V T), meaning that that the arrangement A(V, τ ) is centered.

Proposition 3.12 (stem vectors of A(V, τ ) and A([V ; τ T], 0)). Consider an arrangement A(V, τ ).
Then,

Definition 3.13 (linear general position). Let be given V ∈ Rn×p of rank r, without zero column.
The linear arrangement A(V, 0) is (or the columns of V are) said to be in linear general position if the
following equivalent properties hold

Definition 3.14 (aﬃne general position). Let be given V ∈ Rn×p of rank r, without zero column.
The aﬃne arrangement A(V, τ ) is said to be in aﬃne general position if the following equivalent

Proposition 3.15 (chamber boundedness). Let A(V, τ ) be a proper arrangement.
1) If rank(V ) < n, then none of the chambers are bounded.
2) For s ∈ S(V, τ ), one has

Algorithm 4.1 (p stree). // primal S-tree algorithm [45]

Algorithm 4.2 (p stree rec(s ∈ {±1}
k, x ∈ Rn)).
It is assumed that x is a witness point for s.

Proposition 4.3 (binary S-tree). Let…

Pr…


*[further statements in the full text]*

*[digest of a 136726 character source; every section, statement, and proof in full at `research/sources/chamber_enumeration_numerical_inria2025.full.md`]*
