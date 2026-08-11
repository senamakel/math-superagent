> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/L0.1/markstrom-extremal-cycles.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: http://abel.math.umu.se/~klasm/Uppsatser/cycex.pdf | converted from PDF -->

Extremal graphs for some problems on cycles in
graphs

Klas Markstr¨om

Abstract. This paper contain a collection of extremal graphs for
some questions on cycles in graphs. The graphs have been found by
exhaustive computer search.
I list the extremal graphs and values for the maximum and
minum numer of cycles in a graph, graphs without cycles of length 4
and 8 relating to a conjecture of Erd¨os and Gyarfas and the smallest
3-connected non-hamiltonian cubic graphs of class I.

1. Introduction

Many basic questions regarding the cycle structure of graphs in general,
and cubic graphs in particular, are very poorly understood. In the literat-
ure we ﬁnd unsolved problems of all degree of sophistication, from the cycle
double cover conjecture to the hamiltonicity of various classes of graphs.
In this paper I list extremal graphs and values for some graph properties
related to cycles in graphs which I have happend to be working on during
the last few years. Next to more traditional pen and paper work I have
done some computational work which has been collected in this note.
The four diﬀerent problems treated are brieﬂy: the maximum number
of cycles, the minimum number of cycles, the existence of cycles of length
a power of 2, and ﬁnding nonhamiltonian 3-connected, 3-edge colourable
cubic graphs.

2. Graphs with many cycles

In [ES81] Entringer and Slater studied graphs with the maximum possible
number of cycles among all graphs on n vertices and m edges. More
speciﬁcally they deﬁned ψ(G) to be the number of cycles in the graph G
and ψ(k) as the maximum number of cycles in a graph with n + k − 1
edges. Furthermore they showed that given any value of k there is a cubic
graph G on 2(k − 1) vertices such that ψ(G) = ψ(k), i.e. there is always a
reasonably small extremal graph for a given k.
Since k is the dimension of the cycle space of a graph on n + k − 1
edges we ﬁnd that ψ(k) < 2
k. Entringer and Slater proved that ψ(k) ≥
1

2
k−1 + k2 − 3k + 3 by calculating the number of cycles in the M¨obius
wheels. Using an exhaustive computer search they found the value of ψ(k)
for k ≤ 8 and based on these values conjectured that ψ(k) ∼ 2
k−1.
I have extended the computer search for cubic graphs on 2(k−1) vertices
for which ψ(G) = ψ(k). I have found the extremal graphs for k ≤ 11. For
12 ≤ k ≤ 22 I have computed lower bounds for ψ(k) by narrowing our
search to graphs with high girth. The results are given in Table 1.
In [ES81] it was conjectured that all cubic graphs which are extremal
for ψ would have as large girth as is possible for a cubic graph on 2(k − 1).
This conjecture was disproved in [Gui96], however it still seems to be true
that the extremal graphs tend to have a girth which is close to the largest
possible one. Thus it is not unreasonable to expect the lower bounds for
ψ(k) given here to actually be the value of ψ(k).
The generalised Petersen graph GP(n, m), n ≥ 3, 1 ≤ m < n/2, is a
cubic graph with vertex-set {ui; i ∈ Zn} ∪ {vi; i ∈ Zn}, and edge-set

{uiui+1, uivi, vivi+m; i ∈ Zn}.

For k = 6 we have seen that GP (6 − 1, 2), the ordinary Petersen graph,
is extremal with respect to ψ(G), likewise for k = 5 the graph GP (5 −
1, 2), the cube, is extremal. Motivated by these to initial coincidences we
computed the number of cycles in all small generalised Petersen graphs
and found that for suitable m they come very close indeed to the extremal
value of ψ(n − 1), see Table 2. We thus make the following conjecture.
Conjecture 2.1. Let p(k) = maxm ψ(GP (k − 1, m)).
(1) p(k) = 2
k−1 + f (k), where f (k) is a function not bounded by any
polynomial.
(2) ψ(k) − 2
k−1 = O(p(k) − 2
k−1).
From our data for small k one ﬁnd a decent ﬁt with f (k) = O(kln k).
However there is little else in support for a sharper conjecture.
That p(k) is greater than 2
k−1 is immediate since GP (k − 1, 1) is the
family of ordinary cyclic ladders and for these we have that


*[excerpt ends; 10227 characters not shown — see `research/L0.1/markstrom-extremal-cycles.full.md`]*
