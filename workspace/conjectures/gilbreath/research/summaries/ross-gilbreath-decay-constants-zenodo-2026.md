> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/ross-gilbreath-decay-constants-zenodo-2026.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://zenodo.org/records/21326026/files/Empirical_Structure_of_the_Gilbreath_Decay_Constants.pdf | converted from PDF -->

Empirical Structure of the Gilbreath Decay Constants

Michael M. Ross
Independent Researcher
michaelmross@cantab.net

July 2026

Abstract

Chase, Hunter, and Tao introduced a stationary continuous Gilbreath model in which the
top row consists of independent standard exponential variables and ci := E a(i, j) denotes the
expected entry at depth i. They proved ∑

i≤n ci ≥ log(n + e), computed c0, . . . , c3 exactly, and
could not prove that (ci) is bounded. This note reports a Monte Carlo study to depth 8192,
anchored by new exact rational values of c4, c5, and c6. The principal empirical law is

ci ≈ C λs2(i)

i ,

where s2(i) is the binary digit sum and the effective λ drifts slowly through approximately
1.14–1.20 in the sampled windows. The conjectural 1/i behavior thus becomes visible after
conditioning on digit-sum classes, while pooled data decay more slowly and display a pronounced
dyadic sawtooth; at extreme digit sums the modulation saturates below its geometric extrapola-
tion. Complementary finite-depth experiments indicate a polynomial-versus-exponential growth
transition for continuous uniform data, a full-row relaxation law of order G
0.63–G
0.66, and a spike
survival distance asymptotic to its amplitude. These findings quantify the decay mechanism of
the Gilbreath array that lies beyond the elementary parity wave.

1 Introduction

Given a sequence a1, a2, . . ., its Gilbreath array is defined recursively by

a(0, j) = aj, a(i + 1, j) = |a(i, j) − a(i, j + 1)|. (1)

For the prime sequence, Gilbreath’s conjecture asserts that the left edge equals 1 at every positive
depth. There are two distinct mechanisms in that statement. If a sequence begins with 2 and is
followed by odd integers, parity alone forces every subsequent leading entry to be odd. It does not
force that entry to be 1. The latter behavior requires the array to reach and sustain the closed
{0, 2} regime, in which a leading 1 remains pinned. This distinction is developed in the companion
note [3].
The present paper concerns the quantitative question behind that second mechanism: how
rapidly do typical amplitudes in an absolute-difference array decay? Chase, Hunter, and Tao (CHT)
study the continuous stationary model in which the aj are independent exponential random variables
of mean one [2]. Translation invariance in j gives

E a(i, j) = ci, (2)

1

where ci depends only on the depth. They prove

n∑

i=0 ci ≥ log(n + e), (3)

so exponential decay is impossible. They tentatively suggest that 1/i may be the maximal plausible
rate, but note that the available theory does not even establish that (ci) is bounded [2, Remark 1.5].
The experiments below reveal a more structured version of the 1/i picture. The binary digit sum

s2(i) := the number of ones in the binary expansion of i

modulates the leading order. This is natural: CHT already point to Lucas’ theorem and the fact
that row i of Pascal’s triangle has 2s2(i) odd entries. The new numerical claim is that this parity
statistic enters approximately geometrically.

All asymptotic-looking statements in this note, except the exact low-depth values and identities
explicitly derived below, are empirical. The figures are intended to identify theorem-shaped targets,
not to substitute for proofs.

2 Exact low-depth anchors

The constants ci are rational. Writing ar = sbr, where s = ∑i+1
r=1 ar and (b1, . . . , bi+1) is uniform on
the standard simplex, homogeneity gives

ci = (i + 1)E b(i, 1). (4)

On each region where the signs of all intermediate differences are fixed, b(i, 1) is a linear form.
Partitioning the simplex into these rational sign cones therefore reduces ci to a finite sum of rational
polytope volumes and first moments.
CHT record c0, c1, c2, c3. Exact sign-cone computations in the present study extend the table by
three values: c4 = 778959731701

*[excerpt ends; 11955 characters not shown — see `research/sources/ross-gilbreath-decay-constants-zenodo-2026.full.md`]*
