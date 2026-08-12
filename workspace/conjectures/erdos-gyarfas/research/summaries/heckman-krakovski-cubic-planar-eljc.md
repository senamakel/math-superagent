> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/heckman-krakovski-cubic-planar-eljc.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v20i2p7/pdf | converted from PDF -->

Erd˝os-Gy´arf´as Conjecture for Cubic Planar Graphs

Christopher Carl Heckman

School of Mathematical and Statistical Sciences
Arizona State University
Tempe, AZ 85287 - 1804

checkman@math.asu.edu
 Roi Krakovski

Department of Computer Science
Ben-Gurion University
Beer-Sheva, 84105, Israel

roikr@math.bgu.ac.il

Submitted: May 23, 2011; Accepted: Mar 30, 2013; Published: Apr 9, 2013

Abstract

In 1995, Paul Erd˝os and Andr´as Gy´arf´as conjectured that for every graph of
minimum degree at least 3, there exists a non-negative integer m such that G
contains a simple cycle of length 2m. In this paper, we prove that the conjecture
holds for 3-connected cubic planar graphs. The proof is long, computer-based in
parts, and employs the Discharging Method in a novel way.

Keywords: Erd˝os-Gy´arf´as Conjecture, Cycles of prescribed lengths, Cubic graphs.

1 Introduction

In this paper all graphs are ﬁnite and simple. Paths and cycles are simple, that is, have
no “repeated” vertices. A k-cycle is a cycle of length k. The well-known Erd˝os-Gy´arf´as
conjecture [1] states that every graph of minimum degree at least 3 contains a 2m-cycle,
for some m ⩾ 2.
A graph is planar if it can be embedded in the plane without crossing edges. A plane
graph is an embedded planar graph. A graph G is 3-connected if |V (G)| ⩾ 4 and there is
no S ⊆ V (G) such that |S| < 3 and G \ S is disconnected (\ denotes deletion). A graph
G is cubic if every vertex of G is of degree three.
By computer searches, Markstr¨om [2] veriﬁed the conjecture for cubic graphs of order
at most 29, and found that the smallest cubic planar graph with no 4- or 8-cycles has 24
vertices (see Figure 1). Note that this graph contains a 16-cycle. Shauger [3] proved the
conjecture for K1,m-free graphs of minimum degree at least m + 1 or maximum degree at
least 2m − 1. Daniel and Shauger [4] proved the conjecture for planar claw-free graphs.
The following is the main result of this paper.

1.1. Every 3-connected cubic planar graph contains a 2
m-cycle, for some 2 ⩽ m ⩽ 7.

It is not clear whether 1.1 is tight. It is possible that 2 ⩽ m ⩽ 7 in 1.1 can be replaced
with 2 ⩽ m ⩽ 4. The proof of 1.1 implies the following corollary (which implies a linear
time algorithm for detecting a 2m-cycle):

the electronic journal of combinatorics 20(2) (2013), #P7 1

Figure 1: A 3-connected cubic planar graph, with no 4- or 8-cycles.

1.2. There exists an absolute constant, c, such that every 3-connected cubic plane graph
G has a face f ∈ F (G) with |f | ⩽ 71 and a subgraph H ⊆ G with |V (H)| ⩽ c such that
the following holds:

1. f ⊆ H and for every v ∈ V (H) there exists u ∈ V (f ) and a path of length at most
six between v and u in H.

2. H contains a 2
m-cycle, for some 2 ⩽ m ⩽ 7.

We say that two cycles in a graph intersect if they have at least one vertex in common.
Thus, if two cycles in a cubic graph intersect, then they have at least one edge in common.
It is well-known that two distinct faces in a 3-connected plane graph have at most one
edge in common (or equivalently, the dual graph of a 3-connected plane graph is simple).
As this fact is used frequently, it is stated in the following lemma.

1.3. Let G be a 3-connected cubic plane graph, and let f1, f2 ∈ F (G) be distinct. Then
either f1 and f2 are disjoint, or V (f1) ∩ V (f2) = {u, v} and uv ∈ E(G).

For a graph G, we denote by G \ X the graph obtained by deleting X, where X can
be a vertex or an edge, or a set of vertices or edges. For a set X ⊆ V (G), we denote by
G[X] the subgraph of G induced by the vertices of X. Similarly, for a set X ⊆ E(G),
G[X] is the subgraph of G induced by the edges of X.
For subgraphs A1, A2 ⊆ G, disjoint means vertex-disjoint. By A1 ∪ A2 we mean the
subgraph of H with vertex-set V (A1) ∪ V (A2) and edge-set E(A1) ∪ E(A2).

*[excerpt ends; 104684 characters not shown — see `research/sources/heckman-krakovski-cubic-planar-eljc.full.md`]*
