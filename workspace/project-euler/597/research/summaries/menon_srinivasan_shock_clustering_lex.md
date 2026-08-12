> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/menon_srinivasan_shock_clustering_lex.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/0909.4036 | converted from PDF -->

## What it claims

We study shock statistics in the scalar conservation law ∂tu+∂xf (u) =
0, x ∈ R, t > 0, with a convex ﬂux f and spatially random initial data. We
show that the Markov property (in x) is preserved for a large class of ran-
dom initial data (Markov processes with downward jumps and derivatives
of L´evy processes with downward jumps). The kinetics of shock clustering
is then described completely by an evolution equation for the generator
of the Markov process u(x, t), x ∈ R. We present four distinct derivations
for this evolution equation, and show that it takes the form of a Lax pair.
The Lax equation admits a spectral parameter as in [35], and has remark-
able exact solutions for Burgers equation (f (u) = u
2/2). This suggests
the kinetic equations of shock clustering are completely integrable.

MSC classiﬁcation: 60J75, 35R60, 35L67, 82C99

Keywords: Shock clustering, stochastic coalescence, kinetic theory, integrable
systems, Burgers turbulence.

1 Introduction

We consider the scalar conservation law

∂tu + ∂xf (u) = 0, x ∈ R, t > 0, u(x, 0) = u0(x), (1)

with a strictly convex,…

## Statements it makes

Theorem 1 (Getoor [25]). Consider a c`adl`ag strong Markov process Xs. Let
M ⊂ R be a ﬁxed set and let L = sup{s ∈ R : Xs ∈ M } be the end of M . Then
the post-L process {Xs}s≥L is independent of {Xs}s<L given XL.

Theorem 2. Let u0 be a spectrally negative strong Markov process such that
(4) holds a.s. Under the law µ0 and for any ﬁxed t > 0, the inverse Lagrangian
process a(x, t) is a Markov process. Thus, u(x, t) is a spectrally negative Markov
process.

Theorem 3. Suppose U0 = (Ω, G, Gs, U0(s), M0) is a two-sided spectrally nega-
tive process with independent increments and satisﬁes (4) a.s. Then under M0
and for all t > 0, u(x, t) is a spectrally negative Markov process.

*[digest of a 67765 character source; every section, statement, and proof in full at `research/sources/menon_srinivasan_shock_clustering_lex.full.md`]*
