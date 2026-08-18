> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/beck-haase-matthews-dedekind-carlitz-ar5iv.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://ar5iv.labs.arxiv.org/html/0710.1323 | converted from HTML -->

## What is in it

- Dedekind–Carlitz Polynomials as Lattice-Point Enumerators in Rational Polyhedra Thanks:…
        - Abstract.
        - Key words and phrases:
        - 2000 Mathematics Subject Classification
  - 1. Introduction
        - Theorem 1 (Carlitz).
        - Theorem 2 (Mordell–Pommersheim).
  - 2. Polyhedral Cones Give Rise to Dedekind–Carlitz Polynomials
  - 3. Carlitz Reciprocity
        - Proof of Theorem 1.
        - Theorem 3 (Berndt–Dieter).
        - Proof.
  - 4. Computational Complexity
        - Theorem 4 (Barvinok).
        - Theorem 5.
  - 5. Variations on a Theme
        - Lemma 6.
        - Proof.
        - Theorem 7.
        - Proof.
        - Theorem 8 (Pommersheim).
        - Corollary 9 (Rademacher).
- …


## What it claims

We study higher-dimensional analogs of the *Dedekind–Carlitz polynomials*

| c ⁡ ( u, v, a, b):= ∑ k = 1 b − 1 u ⌊ k ​ a b ⌋ ​ v k − 1, {\rm c}\left(u,v;a,b\right):=\sum_{k=1}^{b-1}u^{\left\lfloor{\frac{ka}{b}}\right\rfloor}v^{k-1}, |  |

where u u and v v are indeterminates and a a and b b are positive integers. Carlitz proved that these polynomials satisfy the *reciprocity law*

| ( v − 1) ​ c ​ ( u, v, a, b) + ( u − 1) ​ c ​ ( v, u, b, a) = u a − 1 ​ v b − 1 − 1, \left(v-1\right)\,{\rm c}\left(u,v;a,b\right)+\left(u-1\right)\,{\rm c}\left(v,u;b,a\right)=u^{a-1}v^{b-1}-1\,, |  |

from which one easily deduces many classical reciprocity theorems for the Dedekind sum and its generalizations. We illustrate that Dedekind–Carlitz polynomials appear naturally in generating functions of rational cones and use this fact to give geometric proofs of the Carlitz reciprocity law and various extensions of it. Our approach gives rise to new reciprocity theorems and computational complexity results for Dedekind–Carlitz polynomials, a characterization of Dedekind–Carlitz polynomials in terms of…

## Statements it makes

###### Theorem 1 (Carlitz).

###### Theorem 2 (Mordell–Pommersheim).

###### Theorem 3 (Berndt–Dieter).

Theorem 3 follows upon clearing denominators in this identity. ∎

###### Theorem 4 (Barvinok).

###### Theorem 5.

###### Lemma 6.

###### Theorem 7.

Theorem 7 is the polynomial analogue of the following result due to Pommersheim [18, Theorem 7]:

###### Theorem 8 (Pommersheim).

###### Corollary 9 (Rademacher).

Theorem 7 could be generalized in several ways, e.g., to higher dimensions or to more than three cones in dimension 2 (this yields a Carlitz polynomial analogue of [18, Theorem 8]), but we digress.

Theorem 7 simplifies when a ​ d − b ​ c = 1 ad-bc=1: then the third Dedekind–Carlitz polynomial disappears. Geometrically, this stems from the fact that the cone 𝒦 2 {\mathcal{K}}_{2} is *unimodular*, i.e., its fundamental parallelogram contains only the origin.

###### Corollary 10.

###### Corollary 11 (Rademacher).

###### Theorem 12 (Brion).

###### Theorem 13.

###### Theorem 14.

Theorem 14 gives σ t ​ 𝒯 ​ ( u, v, w) = N D \sigma_{t{\mathcal{T}}}(u,v,w)=\frac{N}{D} with numerator

*[digest of a 56413 character source; every section, statement, and proof in full at `research/sources/beck-haase-matthews-dedekind-carlitz-ar5iv.full.md`]*
