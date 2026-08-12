> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/abrahamsen-best-laid-plans-lions-men.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: http://dagstuhl.sunsite.rwth-aachen.de/volltexte/2017/7205/pdf/LIPIcs-SoCG-2017-6.pdf | converted from PDF -->

Best Laid Plans of Lions and Men

Mikkel Abrahamsen
∗1, Jacob Holm
2, Eva Rotenberg
3, and
Christian Wulﬀ-Nilsen4

1 Department of Computer Science, University of Copenhagen, Copenhagen,
Denmark
miab@di.ku.dk
2 Department of Computer Science, University of Copenhagen, Copenhagen,
Denmark
jaho@di.ku.dk
3 Department of Computer Science, University of Copenhagen, Copenhagen,
Denmark
roden@di.ku.dk
4 Department of Computer Science, University of Copenhagen, Copenhagen,
Denmark
koolooz@di.ku.dk

Abstract

We answer the following question dating back to J. E. Littlewood (1885–1977): Can two lions
catch a man in a bounded area with rectiﬁable lakes? The lions and the man are all assumed
to be points moving with at most unit speed. That the lakes are rectiﬁable means that their
boundaries are ﬁnitely long. This requirement is to avoid pathological examples where the man
survives forever because any path to the lions is inﬁnitely long. We show that the answer to
the question is not always “yes” by giving an example of a region R in the plane where the
man has a strategy to survive forever. R is a polygonal region with holes and the exterior and
interior boundaries are pairwise disjoint, simple polygons. Our construction is the ﬁrst truly
two-dimensional example where the man can survive.
Next, we consider the following game played on the entire plane instead of a bounded area:
There is any ﬁnite number of unit speed lions and one fast man who can run with speed 1 + ε
for some value ε > 0. Can the man always survive? We answer the question in the aﬃrmative
for any constant ε > 0.

1998 ACM Subject Classiﬁcation I.3.5 Computational Geometry and Object Modeling

Keywords and phrases Lion and man game, Pursuit evasion game, Winning strategy

Digital Object Identiﬁer 10.4230/LIPIcs.SoCG.2017.6

1 Introduction

‘A lion and a man in a closed circular arena have equal maximum speeds. What tactics should
the lion employ to be sure of his meal?’
1 These words (including the footnote) introduce the
now famous lion and man problem, invented by R. Rado in the late thirties, in Littlewood’s
Miscellany [15]. It was for a long time believed that in order to avoid the lion, it was optimal
for the man to run on the boundary of the arena. A simple argument then shows that the

∗ Research partly supported by Mikkel Thorup’s Advanced Grant from the Danish Council for Independent
Research under the Sapere Aude research career programme.
1 The curve of pursuit (L running always straight at M ) takes inﬁnite time, so the wording has its point.

© Mikkel Abrahamsen, Jacob Holm, Eva Rotenberg, and Christian Wulﬀ-Nilsen;
licensed under Creative Commons License CC-BY
33rd International Symposium on Computational Geometry (SoCG 2017).
Editors: Boris Aronov and Matthew J. Katz; Article No. 6; pp. 6:1–6:16
Leibniz International Proceedings in Informatics
Schloss Dagstuhl – Leibniz-Zentrum für Informatik, Dagstuhl Publishing, Germany

6:2 Best Laid Plans of Lions and Men

lion could always catch the man by staying on the radius OM deﬁned by the man while
approaching him as much as possible. However, A.S. Besicovitch proved in 1952 that the man
has a very simple strategy (following which he will approach but not reach the boundary)
that enables him to avoid capture forever no matter what the lion does. See [15] for details.

Throughout this paper, all men, lions, and other animals are assumed to be points. One
can prove that two lions are enough to catch the man in a circular arena, and Croft [8]
proves that in general a necessary and suﬃcient number of birds to catch a ﬂy inside an
n-dimensional spherical cage is just n (again, we assume that the ﬂy and the birds have
equal maximum speeds).

A well-known related discrete game is the cop and robber game: Let G be a ﬁnite connected

*[excerpt ends; 45014 characters not shown — see `research/sources/abrahamsen-best-laid-plans-lions-men.full.md`]*
