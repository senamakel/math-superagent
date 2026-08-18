> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/yu-zeng-four-limit-cycles-near-integrable-2020.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://publish.uwo.ca/~pyu/pub/preprints/YZ_IJBC2020.pdf | converted from PDF -->

December 5, 2020 9:15 WSPC/S0218-1274 2050236

International Journal of Bifurcation and Chaos, Vol. 30, No. 15 (2020) 2050236 (11 pages)
c× World Scientiﬁc Publishing Company
DOI: 10.1142/S0218127420502363

Visualization of Four Limit Cycles in Near-Integrable
Quadratic Polynomial Systems*

Pei Yu† and Yanni Zeng‡

Department of Applied Mathematics, Western University,
London, Ontario, Canada N6A 5B7
†pyu@uwo.ca
‡yzeng243@uwo.ca

Received February 25, 2020; Revised May 3, 2020

It has been known for almost 40 years that general planar quadratic polynomial systems can
have four limit cycles. Recently, four limit cycles were also found in near-integrable quadratic
polynomial systems. To help more people to understand limit cycles theory, the visualization
of such four numerically simulated limit cycles in quadratic systems has attracted researchers’
attention. However, for near-integral systems, such visualization becomes much more diﬃcult
due to limitation on choosing parameter values. In this paper, we start from the simulation
of the well-known quadratic systems constructed around the end of 1979, then reconsider the
simulation of a recently published quadratic system which exhibits four big size limit cycles, and
ﬁnally provide a concrete near-integral quadratic polynomial system to show four normal size
limit cycles.

Keywords: Hilbert’s 16th problem; quadratic near-integrable system; limit cycle; Andronov–Hopf
bifurcation; Melnikov function; simulation.

1. Introduction

The well-known Hilbert’s 16th problem is remained
unsolved for more than one hundred years since
Hilbert [1902] proposed the 23 mathematical prob-
lems. A simpliﬁed version of the problem, based on
a general Li´enard equation, was chosen by Smale
[1998] as one of the 18 challenging mathematical
problems for the 21st century. Consider the follow-
ing planar system:

˙x = P (x, y), ˙y = Q(x, y), (1)

where the dot denotes diﬀerentiation with respect
to time t, P (x, y)and Q(x, y)are polynomials in x
and y. The second part of Hilbert’s 16th problem is
to ﬁnd the upper bound, called Hilbert number and
denoted by H(n), where n =max{deg P, deg Q},
 on the number of limit cycles that system (1) can
have. If the problem is restricted to the neighbor-
hood of isolated ﬁxed points, then the question
is reduced to studying degenerate Andronov–Hopf
bifurcations. In 1952, Bautin [1952] proved that
three small limit cycles exist around a ﬁne focus
or a center in quadratic systems. Almost 30 years
later, concrete examples were independently con-
structed by Shi [1979], and by Chen and Wang
[1979] to show the existence of four limit cycles in
quadratic, implying that H(2) ≥ 4. However, the
question whether H(2) = 4 is still open.
To reduce the diﬃculty in attacking the
Hilbert’s 16th problem, Arnold proposed a weak
version of the problem [Arnold, 1977], which trans-
forms the problem of determining the maximal
number of limit cycles (a geometric problem) to

∗The ﬁrst draft of this article has been posted on arXiv.org since February 25, 2020, No. 2002.09987v1.
†Author for correspondence
 2050236-1Int. J. Bifurcation Chaos 2020.30. Downloaded from www.worldscientific.comby CITY UNIVERSITY OF HONG KONG on 12/12/20. Re-use and distribution is strictly not permitted, except for Open Access articles.
December 5, 2020 9:15 WSPC/S0218-1274 2050236

P. Yu & Y. Zeng

ﬁnding the maximal number of isolated zeros of the
Abelian integral or Melnikov function (an algebraic
problem):

M (h)= ∮

H(x,y)=h Q(x, y)dx − P (x, y)dy, (2)

where H(x, y),P and Q are all real polynomials in x
and y with deg H = n+1, and max{deg P, deg Q}≤
n. The weak Hilbert’s 16th problem is closely
related to the maximal number of limit cycles in
the following near-Hamiltonian system [Han, 2006]:

˙x = ∂H(x, y)
∂y + εpn(x, y),

˙y = − ∂H(x, y)
∂x + εqn(x, y),
 (3)

where pn(x, y)and qn(x, y)are nth-degree polyno-

*[excerpt ends; 27574 characters not shown — see `research/sources/yu-zeng-four-limit-cycles-near-integrable-2020.full.md`]*
