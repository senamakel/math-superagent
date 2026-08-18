> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/sutherland-wiman-tschirnhaus.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/2106.09247 | converted from PDF -->

arXiv:2106.09247v1  [math.HO]  17 Jun 2021
On the Application of Tschirnhaus Transformations to the
Reduction of Algebraic Equations

A Translation by Alexander J. Sutherland

June 18, 2021

1 Original Bibliographic Information

1.1 German

• Author: Anders Wiman

• Title: ¨Uber die Anwendung der Tschirnhausen-Transformation auf die Reduktion algebraischer Gle-
ichungen

• Year: 1927

• Language: German

• Publisher: Nova Acta Regiae Societatis Scientiarum Upsaliensis (Nova Acta R. Soc. scient. Uppsala)

• Note: Der K¨onigi. Societ¨at der Wissenschaften Zu Uppsala Mitgeteilt

1.2 English

• Author: Anders Wiman

• Title: On the Application of Tschirnhaus Transformations to the Reduction of Algebraic Equations

• Year: 1927

• Language: German

• Publisher: New Proceedings of the Royal Society of Scientists of Uppsala

• Note: Notice to the Royal Society of Scientists of Uppsala on 06 May 1927

This work was supported by the National Science Foundation under Grant No. DMS-1944862.

1

2 The Translation

Part 1

1We consider a general equation of nth degree:

x
n + c1x
n−1 + · · · + cn = 0 (1)

with roots x1, . . . , xn. We then apply a Tschirnhaus transformation, which has the general form

y = a0 + a1x + · · · + an−1x
n−1. (2)

This will transform (1) into an equation

yn + C1yn−1 + · · · + Cn = 0, (3)

where the coeﬃcients Ci are all homogeneous functions of degree i in the variables aν and include all such
functions of weight up to i in the coeﬃcents ci. Tschirnhaus hoped to use this type of transformation to
convert equation (1) to the binomial form in such a way that the determination of parameters aν should
require the solution of equations of degree at most n − 1. As is well known, this is not the case, even though
there have many attempts for the degree 5; this will never be the case, just like for [the problem of] trisecting
an angle. However, the situation is completely diﬀerent if the problem is formulated in the following way: Is
it possible to satisfy the conditions

Ci(a0, a1, . . . , an−1) = 0, i = 1, . . . , m (4)

in such a way that determining the parameters aν only requires equations of degree up to m, when n is
suﬃciently large? As a result of the following treatment for the case m = 4, it should not appear doubtful
that question should also be decided in the aﬃrmative for larger m. However, the general problem of
determining the lower bound on n associated to each m appears to be very complex.

Section 2

Observe that
 C1(a0, . . . , an−1) = na0 + · · · .

If C1 = 0, then a0 is expressed linearly in the other parameters. The coeﬃcients Ci, (i = 2, . . . , n − 1) are
then homogeneous functions of degree i in the parameters a1, . . . , an−1. In order to [ﬁnd a point that will]
satisfy a single condition Cx = 0, (x > 1)

it is evident that it is only necessary to ﬁnd an intersection of the hypersurface Cx = 0 with an arbitrary
straight line to solve an equation of degree x. If all the roots of (1) are real, then you cannot get a real
solution for x = 2 because the hypersurface
 n∑

i=1 y2
i = C2 = 0 (5)

has only the trivial 0. In contrast, there are always real points on the surface C3 = 0. Indeed, as you can
easily see, the same is the case for all surfaces Cx = 0 (x > 2) if x is an even number.

1Translator’s Note: This is a translation of the original mathematics. In particular, errors in the text have not been ﬁxed.
The errors in question come from considering intersections in aﬃne spaces instead of in projective spaces. Throughout this
translation, there are additional footnotes with the identiﬁer “Translator’s Footnote:.” These footnotes refer to remarks in
Section 3 in which the translator provides additional mathematical commentary.

2

If one has n ≥ 5, then one obtains the solution of (4) for m = 3 by the well-known Bring-Jerrard

*[excerpt ends; 12198 characters not shown — see `research/sources/sutherland-wiman-tschirnhaus.full.md`]*
