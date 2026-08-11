> **Excerpt only — read this first.** The complete text is beside it at `research/cabanillas_variant_pdf.full.md`; open that only when this file does not answer the question, because it is large. Replace this excerpt with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, and specific enough that nobody needs the full text.

<!-- source: https://arxiv.org/pdf/1904.01874 | converted from PDF -->

arXiv:1904.01874v2  [math.NT]  12 Sep 2019
A variant of Ostrowski numeration

Emmanuel Cabanillas

ABSTRACT :

In this article, we propose a variant of the usual Ostrowski α-numeration ( where α is a real in
[0, 1[) that codes integers ( positive as well as negative) and reals of [0, 1[ ( instead of [−α, 1−α[),
so that for every integer n, n and {nα} have the same coding sequence. These coding sequences
respect natural lexicographic orders and will be used to prove well known results on order prop-
erties of Kronecker sequences ({nα − β})n.

Contents

1 Introduction 2
1.1 overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.2 notations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.3 continued fraction expansions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.4 semi-convergents and best rationals . . . . . . . . . . . . . . . . . . . . . . . . . . 4

2 A numeration system 7
2.1 Ostrowski’s numeration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2.2 α-numeration for a rational α . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
2.3 α-numeration for an irrational α . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
2.4 α-numeration of negative integers . . . . . . . . . . . . . . . . . . . . . . . . . . . 18

3 Complements 22
3.1 dynamic generating α-numeration . . . . . . . . . . . . . . . . . . . . . . . . . . 22
3.2 α-germs and orbits of α-rotation . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
3.3 shift and inductive structure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25

4 Order properties of Kronecker sequences 28
4.1 a one-page proof of the ”three distance theorem” . . . . . . . . . . . . . . . . . . 28
4.2 order coincidence of ({nα})n and ({nα′})n . . . . . . . . . . . . . . . . . . . . . . 30
4.3 best left or right α-approximation of a real in [0, 1[ . . . . . . . . . . . . . . . . . 32
4.4 measure of repartition of ({kα})0⩽k<ν . . . . . . . . . . . . . . . . . . . . . . . . 34

5 References 37

1

1 Introduction

1.1 overview

Ostrowski’s numeration system is based on convergents (qn)n∈N of a real α ∈ [0, 1[ and code,
with a sequence of digits non negative integers as well as reals in [−α, 1 − α[ ( see [6] for the
original article and [1] for a survey). Deﬁnitions are mentioned in 2.1
In 2.2 and 2.3, we propose a variant of this system : it is still based on (qn)n, but the ”
markovian condition” is changed and we will be able to code any integer n and any real {nα}
with the same ﬁnite sequence ( {x} denotes the fractional part of a real x). We study separately
the cases α irrational and α rational. This last case could appear uninteresting, but it is useful
for applications to numerical semigroups for example ( see [3]).
In 3, we give some dynamical aspects of this α-numeration.
In 4, we use it to explore some order properties of Kronecker sequences ({nα + β})n, as the
famous ” three distance theorem”. These sequences have been widely studied with various points
of view and we refer to [1] for an exhaustive bibliography.

1.2 notations

All along this paper, we will denote : Z the set of integers, N∗ the set of positive integers and
N the set of non negative integers.
For all reals x, ⌊x⌋ denotes its ﬂoor ,⌈x⌉ its ceiling and {x} its fractional part.
For a sequence d = (dk)k∈N∗, we use the following notations for slices of d : for all integers r, s
such that 0 < r ⩽ s :
 d[r,s] = (dr, dr+1, · · · , ds) ; d[r,∞] = (dr, dr+1, · · · )

We will also use concatenation of sequences and intuitive notations as (3, 5, 04, 1, 6, 0∞) to de-
note (3, 5, 0, 0, 0, 0, 1, 6, 0, 0, 0, · · · ). Moreover, if (ak)k∈N∗ is a sequence of positive integers and
if we restrict ourself to sequences in ∏k{0 · · · ak}, then max at the index k will denote ak : for

*[excerpt ends; 76952 characters not shown — see `research/cabanillas_variant_pdf.full.md`]*
