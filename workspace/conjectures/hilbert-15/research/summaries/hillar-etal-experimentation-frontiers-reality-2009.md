> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/hillar-etal-experimentation-frontiers-reality-2009.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/0906.2497 | converted from PDF -->

arXiv:0906.2497v2  [math.AG]  20 Nov 2009
Contemporary Mathematics

Experimentation at the Frontiers of Reality
in Schubert Calculus

Christopher Hillar, Luis Garc´ıa-Puente, Abraham Mart´ın del Campo,
James Ruﬀo, Zach Teitler, Stephen L. Johnson, and Frank Sottile

Abstract. We describe a general framework for large-scale computational ex-
periments in mathematics using computer resources that are available in most
mathematics departments. This framework was developed for an experiment
that is helping to formulate and test conjectures in the real Schubert calculus.
Largely using machines in instructional computer labs during oﬀ-hours and
University breaks, it consumed in excess of 350 GigaHertz-years of computing
in its ﬁrst six months of operation, solving over 1.1 billion polynomial systems.

Introduction

Mathematical discovery has long been informed by experimentation and compu-
tation. Understanding key examples is typically the ﬁrst step towards formulating
theorems and devising proofs. The computer age enables many more potentially in-
tricate examples to be studied than ever before. Sometimes, this leads to a fruitful
dialog between theory and experiment. Other times, this work leads serendipitously
to new ideas and theorems. Many examples are described in the books [1, 5].
We believe there is much greater potential for computer-aided experimentation
than what has been achieved. This is particularly true for scientiﬁc discovery,
using advanced computing to study subtle phenomena and amass evidence for the
mathematical facts which will become the theorems of tomorrow. Currently, much
computer experimentation is (often appropriately) on a fairly small scale. A notable
exception is Odlyzko’s study [28] (using Cray supercomputers) of the zeroes of
Riemann’s ζ-function on the critical line 1
2 + R√−1, which led to a rich data set
that has stimulated much intriguing mathematics [8].
A diﬀerent large scale use of computers is the Great Internet Mersenne Prime
Search (GIMPS) [22], which searches for primes of the form 2p−1 for p a prime,
such as 3, 7, 31, and 127. Volunteers run software on otherwise idle computers to
search for Mersenne primes. This project has found the largest known primes since
it started in 1996. Daily, it uses over 60 GigaHertz-years of computation.

Research of Sottile supported in part by NSF grant DMS-070105.
Research of Hillar supported in part by an NSF Postdoctoral Fellowship and an NSA Young
Investigator grant.
 c⃝0000 (copyright holder)

1

2 HILLAR, GARC´IA, MART´IN DEL CAMPO, RUFFO, TEITLER, JOHNSON, AND SOTTILE

GIMPS is a mathematical analog of big-science physics. We feel there is more
scope for such investigations in mathematics. We describe our use of a supercom-
puter to study a conjecture in the real Schubert calculus, which may serve as a
model for research in mathematics based on computational experiments. Rather
than Odlyzko’s Cray supercomputers, or GIMPS’s thousands of volunteers, we
use more pedestrian computer resources that are available to many mathemat-
ics departments together with modern (and free) software tools such as Perl [48],
MySQL [46], and PHP [49], as well as freely available mathematical software such
as Singular [16], Macaulay 2 [15], and Sage [45].
This is a methods paper whose purpose is to explain the framework we de-
veloped. We do not present mathematical conclusions from this ongoing compu-
tational experiment, but instead explain how you, the reader, can take advantage
of readily available yet often underutilized computer resources to employ in your
mathematical research.
To get an idea of the available resources, in its ﬁrst six months of data acquisi-
tion, this experiment used over 350 GigaHertz-years of computing primarily on 191
computers in instructional labs that are maintained by the Department of Mathe-

*[excerpt ends; 46956 characters not shown — see `research/sources/hillar-etal-experimentation-frontiers-reality-2009.full.md`]*
