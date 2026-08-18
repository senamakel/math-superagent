# Masáková & Pelantová — Relation between powers of factors and recurrence function characterizing Sturmian words

<!-- source: https://ar5iv.labs.arxiv.org/html/0809.0603 (arXiv:0809.0603; DOI 10.48550/arXiv.0809.0603) | full text at research/sources/masakova-pelantova-powers-factors-recurrence-sturmian-ar5iv.full.md -->

**Zuzana Masáková, Edita Pelantová** (2008). Czech Technical University. 11 pages. Subjects math.CO, math.DS. MSC 68R15.

## What it establishes

- **Definitions (Preliminaries, §2).** A factor w is *left special* if both Aw and Bw (A≠B letters) are factors; *right special* if both wA and wB are factors; *bispecial* if both. An aperiodic word with minimal complexity C(n) = n+1 for all n is Sturmian.
- **Unique special factors (verbatim, §2).** "in the language of a Sturmian word u one has exactly one left special and exactly one right special factor of each length, and Sturmian words are characterized by this property." — This is the structural fact the run's adopted approach `pe1006-rauzy-right-special-extension-recurrence` cites as precedent for its extension recurrence Ψ(k+1)=100Ψ(k)+100V(R_k)²+20S1(k)+J(k), whose hinge is the unique right-special length-k factor R_k.
- **Main result (Theorem 1.1).** A uniformly recurrent infinite word u is Sturmian iff there exist infinitely many factors w with R(|w|) = |w|·ind(w) + 1, where R is the recurrence function and ind(w) the maximal rational exponent with w^r a factor. A new characterization of Sturmian words via index and recurrence function.
- **Byproduct.** A new proof that the index of a Sturmian word is given by the continued fraction expansion of its slope (independent of Carpi–de Luca Acta Informatica 36 (2000) and Damanik–Lenz EJC 2002). §4 upper bound, §5 sharpness via Sturmian morphisms.

## Convention

Uses two-letter alphabet {A,B}, slope α, exchange of two intervals. The Fibonacci word appears as the most prominent Sturmian example. Slope/letter conventions differ from PE1006's 0→01,1→0 in letter names only; the special-factor uniqueness is convention-free.

## Why it matters for PE1006

The unique right-special factor of each length (with its value V(R_k) constant on Wythoff runs) is the exact structural input to the run's independently-verified extension recurrence. This source is now the on-disk primary reference for that uniqueness (previously only cited from memory).

## Status

Full text on disk, read and verified. Summary written by librarian (the automatic digest is superseded).
