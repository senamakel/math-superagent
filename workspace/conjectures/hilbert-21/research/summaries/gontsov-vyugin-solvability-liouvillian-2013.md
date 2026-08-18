> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/gontsov-vyugin-solvability-liouvillian-2013.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/1312.2518 | converted from PDF -->

## What it claims

The paper concerns the solvability by quadratures of linear diﬀerential systems, which is
one of the questions of diﬀerential Galois theory. We consider systems with regular singu-
lar points as well as those with (non-resonant) irregular ones and propose some criteria of
solvability for systems whose (formal) exponents are suﬃciently small.

1 Introduction

Consider on the Riemann sphere C a linear diﬀerential system

dy
dz = B(z) y, y(z) ∈ Cp, (1)

of p equations with a meromorphic coeﬃcient matrix B(z) having singularities at points a1, . . . , an.
A singular point z = ai is said to be regular, if any solution of the system has at most polyno-
mial growth in any sector of small radius with vertex at this point and an opening less than 2π.
Otherwise the point z = ai is said to be irregular.
The Picard–Vessiot extension of the ﬁeld C(z) of rational functions corresponding to the
system (1) is a diﬀerential ﬁeld F obtained by adjoining to C(z) all entries of a fundamental
matrix Y (z) of the system (1). One says that the system (1) is solvable by quadratures, if the
entries of the…

## Statements it makes

Lemma 1. If a holomorphically trivial vector bundle E of rank p over C endowed with a
meromorphic connection ∇ has a holomorphically trivial subbundle E′ ⊂ E of rank k that is
stabilized by the connection, then the corresponding linear system (1) is reduced to a blocked
upper-triangular form via a constant gauge transformation ˜y(z) = Cy(z), C ∈ GL(p, C). That
is,
 CB(z)C −1 = ( B′(z) ∗
0 ∗
 ) ,

Theorem 1. Let for some k ∈ {1, . . . , p − 1} the exponents βj
i of the regular singular system
(1) satisfy the condition

Lemma 2. Let the exponents βj
i of the regular singular system (1) satisfy the condition (13).
If the monodromy matrices of this system are upper-triangular, then there is a constant matrix
C ∈ GL(p, C) such that the matrix CB(z)C −1 has the form as in Theorem 1.

Lemma 3. There is a number N = N (p) such that if the matrices M1, . . . , Mn are not
N -resonant, then the existence of a solvable normal subgroup of ﬁnite index in M implies their
triangularity.

Corollary 1. Let the eigenvalues βj
i of the residue matrices Bi of the Fuchsian system (2)
satisfy the condition

Theorem 2. Let at each singular point ai the formal exponents λj
i of the irregular system
(1) be pairwise distinct and satisfy the condition

*[digest of a 39348 character source; every section, statement, and proof in full at `research/sources/gontsov-vyugin-solvability-liouvillian-2013.full.md`]*
