<!-- source: https://www.renyi.hu/~gyarfas/Cikkek/ar2erdos.pdf | converted from PDF -->

arXiv:1307.1768v1  [math.CO]  6 Jul 2013Problems and Memories∗

Andr´as Gy´arf´as †

Alfr´ed R´enyi Institute of Mathematics

July 22, 2013

1 First encounter

My ﬁrst encounter with Paul Erd˝os took place in 1962 at the M´atrah´aza Guest House

of the Hungarian Academy of Sciences. I was a high school student and was rather

embarrassed by the solemn formalities, especially at the dinner tables. I was pleased to

hear the signs of some unaccepted behavior from a neighboring table, where an “old”

man about ﬁfty was regulated by his mother: “Pali you should keep your fork properly!”

I soon learned that the unruled boy is a famous mathematician who travels around the

world with his mother. Next day I had opportunity to play ping pong against “Pali” and

I was very angry upon being beaten by such an old man playing in a ridiculous style. As

a consolation he told me what a graph is and what does Tur´an theorem say about the

number of edges in a graph that does not contain Kk+1. “Adding any edge to the Tur´an

graph we get a Kk+1 but what is the smallest graph with this property?” - asked during

the revenge game which I lost again. Then he left but the problem bugged me and about

a year later, after a lecture he gave in Budapest, I handed him my typewritten solution

for the case when the number of vertices is large in terms of k. It was disappointing

to learn that his question was not an unsolved problem, but his result with Hajnal and

Moon, [10]. Two years later, at E¨otv¨os University, I listened to B´ela Bollob´as’ talk at the

∗A talk at Erd˝os 100
†Supported in part by OTKA grant K104343
 1

Haj´os seminar about extending the result to hypergraphs. I remember B´ela’s comment:

“this is trivial” [5]... Trivial or not, certainly important and rediscovered several times

[27, 28]. The underlying idea, cross-intersecting sets, developed further and have many

applications.

2 Memphis Tennessee...

Long distance information, give me Memphis Tennessee,

Help me ﬁnd the party trying to get in touch with me,

She could not leave her number, but I know who placed the call,

’Cause my uncle took the message and he wrote it on the wall...

... sang Chuck Berry, and beside Elvis Presley, Chuck Berry and Fedex, Memphis

Tennessee is also known as a hub during the movements of Paul Erd˝os in the US. Indeed,

I have had much more chance to meet (and think on math) with him there than in

Budapest. The University of Memphis (with Faudree, Ordman, Rousseau and Schelp as

permanent faculty and me as permanent visitor) provided many opportunities to pursue

theorems, problems and conjectures. From the early 90-s the department was fortiﬁed

by B´ela Bollob´as, who leads a Chair of Excellence in Combinatorics since then.

2.1 Cyles in graphs without proper subgraphs of minimum de-

gree 3

The following observation is due to Erd˝os, Faudree, Rousseau and Schelp [9].

• Graphs with n vertices and 2n−1 edges must contain proper subgraphs of minimum

degree 3 but this fails for graphs with n vertices and 2n − 2 edges, for example the

wheel is such a graph.

In [7] we had a closer look on the family G(n) of graphs with n vertices, 2n − 2 edges

and without proper subgraphs of minimum degree 3. We showed that graphs in G(n)

contain cycles C3, C4, C5 and also Ck for k ≥ log2 n but not necessarily for k ≥ c√n.

However, we could not resolve the following.

2

Conjecture 1. ([7]) Every G ∈ G(n) contains cycles of length i for every integer 3 ≤

i ≤ k where k tends to inﬁnity with n.

2.2 Large chordal subgraphs

In [17] we discussed the size of chordal (interval, threshold) subgraphs present in graphs

with several ranges of edges. One particular jump is observed at graphs with n vertices

and n
2/3 edges.

• Any graph with n vertices and at least n
2/3 edges contains a chordal subgraph

with at least 2n − 3 edges. The complete tripartite graph shows that this is sharp.

Conjecture 2. ([17]) Any graph with n vertices and more than n
2/3 edges contains a

chordal subgraph with at least 8n/3 − 4 edges. The complete tripartite graph with one

additional edge shows that this would be sharp.

We could prove a weaker result, that graphs with n vertices and more than n
2/3

edges contain chordal subgraphs with at least 7n/3 − 6 edges [17].

2.3 Monochromatic domination

The following result, conjectured by Erd˝os and Hajnal [11], was proven in [6] and inde-

pendently by Kostochka [29]. In an edge colored complete graph K a subset S of vertices

dominate in color i those vertices in V (K) − S that send at least one edge of color i to

S.
 • ([6]) Assume that the edges of Kn are 2-colored and k is a positive integer. There

exist k vertices of Kn such that in one of the colors they dominate all but at most

n−1
2k vertices of Kn.

It turned out, that for 3 colors the situation is diﬀerent.

• ([8]) If the edges of Kn are 3-colored then in one of the colors at most 22 vertices

dominate at least 2n/3 vertices of Kn.

3

Conjecture 3. ([8]) If the edges of Kn are 3-colored then in one of the colors at most

3 vertices dominate at least 2n/3 vertices of Kn.

The random 3-coloring shows that no two vertices dominate much more than 5n/8

vertices. Note that one cannot dominate more than 2n/3 vertices of Kn with any number

of vertices because of the following 2-coloring: partition the vertices into three almost

equal parts A1, A2, A3 and color the edges inside Ai and between Ai, Ai+1 with color i.

In this coloring no set dominates more than 2n/3 vertices in any of the three colors.

Recently Kral, Liu, Sereni, Whalen and Yilma [30] got very close to the solution of

Problem 3, showing that 22 can be replaced by 4.

2.4 Covering by monochromatic cycles

Let the cycle partition number be the minimum k such that the vertex set of any r-

edge-colored complete graph can be covered by at most k vertex disjoint monochromatic

cycles.

• ([15]) The cycle partition number of any r-colored complete graph depends only

on r and it is at most cr2 log r.

Conjecture 4. ([15]) The cycle partition number of any r-colored complete graph is at

most r.

The case r = 2 in Conjecture 4 is due to J. Lehel and was proved for large enough

complete graphs by  Luczak, R¨odl and Szemer´edi in [32] using the regularity lemma

and later by Allen in [1] without it. Then Bessy and Thomass´e [3] proved it for all

complete graphs with an elementary approach. The estimate cr2 log r of [15] is improved

to cr log r in [25]. Although Conjecture 4 for r = 3 was proved asymptotically in [24],

Pokrovskiy [35] found a counterexample. Nevertheless, in the counterexample for r = 3

three monochromatic cycles cover all but one vertices thus a slightly weaker version of

Conjecture 4 can be easily true. Extensions, related problems can be found in [26].

4

2.5 B + M graphs

At the conference in Orsay in 1976 we had a chat with Paul about 4-critical (4-chromatic

but removing any edge becomes 3-colorable) graphs that can be written as the union of

a bipartite graph and a matching [19]. We returned to this problem in [4] calling them

4-critical B + M-graphs. A B + 3 graph is a graph which can be written as the union of

a bipartite graph and a matching with three edges.

Problem 5. ([4]) “We know that one has to be careful with conjectures in this area.

That is why we only suspect that 4-critical B + 3-graphs on n vertices must have at least

2n edges asymptotically and dare to conjecture only that they have signiﬁcantly more

than 5n/3 edges.”

3 Szentendre

During the years 1993 - 1996 Paul spent with us some summer weeks as our guest

at Szentendre. Almost all essentials for his life had been present (a mathematician, a

mathematician’s wife who could prepare beef Stroganoﬀ and take part in literary and

theological debates) - although at the beginning there was no phone and it was a regular

program to walk to the nearest phone booth. Another program was to walk to vista

point Kada at a hilltop nearby. Or just walk in the garden and enjoy the shade under

the huge old walnut tree. Paul often invited us to dinner at the Merry Monks where we

became regulars, one waiter have always greeted him asking “how are you and how are

the prime numbers?”

He liked to sit at the terrace in front of the house struggling with problems after

problems. Time to time he exclaimed: “It is very annoying that we do not see this!”

Sometimes we were more successful: “This is enough for a paper, don’t you think so?”

3.1 Decreasing the diameter of triangle-free graphs

For a triangle-free graph G we deﬁned hd(G) ([16]) as the minimum number of edges to

be added to G to obtain a triangle-free graph of diameter at most d.

5

• ([16]) For every connected triangle-free graph G on n vertices, h3(G) ≤ n − 1 and

h5(G) ≤ n−1
2 .

The case d = 3 is left open, in particular we asked the following.

Problem 6. ([16]) Is there a positive ǫ such that h4(G) ≤ (1 − ǫ)n for every connected

triangle-free graph G on n vertices?

3.2 A problem on set mappings

The ﬁrst (out of 56) joint paper of Erd˝os and Hajnal, [18], deﬁned set mappings as a

function from proper subsets of S to S such that f (A) /∈ A. In [18] they deﬁned H(n)

as the smallest integer for which there exists a set mapping on S with |S| = n such that

∪X⊆T f (X) = S

for every T ⊂ S, |T | ≥ H(n) and they proved that log2 n < H(n) and conjectured that

H(n) − log2(n) tends to inﬁnity with n. We tried in vain to make the following small

step toward this:

Problem 7. ([20]) Show that H(n) > k + 1 for n = 2k.

3.3 When every path spans a 3-colorable subgraph

During the summer of 1995 Paul cited the following from one of his problem books. “I

asked this with Hajnal: if each odd cycle of a graph spans a subgraph with chromatic

number at most r then the chromatic number of the graph is bounded by a function of

r.” Some days later I created a warm-up to this question which is still open.

Conjecture 8. ([22]) If each path of a graph spans at most 3-chromatic subgraph then

the graph is c-colorable, perhaps with c = 4.

6

3.4 Balanced colorings

We called an edge coloring of Kn with r colors balanced if every subset of ⌊n/r⌋ vertices

contains at least one edge in each color.

• ([14]) Balanced r-coloring of Kn exists when n = r2 + r + 1 and r + 1 is a prime

power.

We conjectured that this result gives the smallest n for which balanced r-coloring

exists.

Conjecture 9. ([14]) In every r-coloring of the edges of Kr2+1 there exist r + 1 vertices

with at least one missing color among them (r ≥ 3, true for r = 3, 4).

3.5 Nearly bipartite graphs

Erd˝os and Hajnal asked if every subset S of vertices in a graph G contains an independent

set of size at least ⌊ |S|
2 ⌋−k then can one remove f (k) vertices from G so that the remaining

graph is bipartite? This is settled in the aﬃrmative by Bruce Reeed [36]. I looked at the

case k = 0 and called a graph G nearly bipartite if every S ⊆ V (G) has an independent

set of size ⌊ |S|
2 ⌋.

• ([22]) A graph is nearly bipartite if and only if it contains neither two vertex disjoint

odd cycles nor odd subdivisions of K4 (where each edge is subdivided to form an

odd path).

Conjecture 10. [22] A nearly bipartite graph can be made bipartite by deleting at most

5 vertices.

Molloy and Reed believed [36] they can prove Conjecture 10 but so far they did not

work out the details... The following example shows that Conjecture 10 would be sharp.

Take a 5 × 5 grid with vertex set {vi,j : 1 ≤ i, j ≤ 5}, subdivide its horizontal edges and

add the edges v1,1v5,5, v1,2v5,4, v1,3v5,3, v1,4v5,2, v1,5v5,1.

7

3.6 Covering by monochromatic paths

I mentioned to Paul that the vertices of a 2-colored complete graph can be covered by

the vertices of two monochromatic paths - an easy exercise, a footnote in my ﬁrst paper

(with Gerencs´er) [23]. Paul said he did not believe that and it turned out soon that he

thought that the covering paths must have the same color. Within two weeks we arrived

to a partial answer to this new problem.

• The vertex set of a 2-colored Kn can be always covered by the vertices of at most

2√n monochromatic paths of the same color.

Problem 11. ([12]) Is it possible to cover the vertex set of a 2-colored Kn with at

most
√n monochromatic paths of the same color? This would be best possible.

3.7 (p, q)-colorings of complete graphs

It is sad to look at the submission date on our paper [13]: September 15, 1996 - one

day before Paul died in Varsaw. We called an edge coloring of a complete graph Kn a

(p, q)-coloring if every Kp ⊂ Kn spans at least q colors. Thus a (p, 2)-coloring means

that there is no monochromatic Kp, a (3, 3)-coloring means that the coloring is proper.

Let f (n, p, q) denote the minimum number of colors needed for a (p, q)-coloring of Kn.

Some of the general bounds of this paper have been improved by S´ark¨ozy and Selkow

[37]. There are much improvements on interesting small cases as well.

On f (n, 4, 3) the best upper bound is n
o(1) given in Mubayi [33]. The lower bound

of Kostochka and Mubayi [31] is improved to c log n by Fox and Sudakov [21]. Lower

bounds of [13] and upper bounds of Mubayi [34] imply that f (n, 4, 4) = n
1/2+o(1).

In the next problem the debate of the authors whether the lower or upper bound is

closer to the truth is not resolved (yet). As already noted in [13], f (n, 4, 5) ≤ n − 1 for

all even n ≥ 6 would follow from the existence of a factorization of Kn where there is no

C4 in the union of any two color classes. Such factorizations exist if n = 2p with odd p

or n = s + 1 where s is not divisible by three.

Problem 12. ([13]) 5(n−1)
6 ≤ f (n, 4, 5) ≤ n - improve the estimates!

8

One of my favorite problems from [13] is to decide whether f (n, 5, 9) is linear which

is equivalent to the following:

Problem 13. ([13]) Is there a constant c such that Kn has a proper edge coloring with

cn colors, such that the union of any two color classes has no path or cycle with four

edges?

G´eza T´oth proved 2n − 6 ≤ f (n, 5, 9) [38] and f (n, 5, 9) ≤ 2n
1+c/
√logn is due to

Axenovich [2].

3.8 Problems and solutions

With so many problems to ask, think about, share, transfer, it was unavoidable that

sometimes Paul created some confusion. For me a remarkable adventure of this kind

was my problem that Paul announced at the 18-th Southeastern Conference on Combi-

natorics and Graph Theory held in Boca Raton (February 23-27, 1987).

Years went by, Paul forgot what happened and contributed the problem to himself...

I mentioned his slip of mind at Szentendre in a summer evening of 1995. “It is not

important who asked the problem, the important thing is that the problem is solved” -

he said and I heartily agreed...

It was not always easy to live and work with Paul. But it was hard to except that

we had no more summers with him. Chess, pingpong, card games, conjectures, proofs

continued, but not with the same passionate way. And the huge old walnut tree in the

garden also died in 1996. Nevertheless, his results, conjectures, proofs and passionate love

of mathematics are with us and carry over to the present and forthcoming generations

of mathematicians.
 9

References

[1] P. Allen, Covering two-edge-coloured complete graphs with two disjoint monochro-

matic cycles, Combinatorics, Probability and Computing, 17 (2008), 471-486.

[2] M. Axenovich, A generalized Ramsey problem, Discrete Mathematics 222. (2000)

247–249.

[3] S. Bessy, S. Thomass´e, Partitioning a graph into a cycle and an anticycle, a proof

of Lehel’s conjecture, Journal of Combinatorial Theory B., 100 (2009), 176-180.

[4] G. Chen, P. Erd˝os, A. Gy´arf´as, R. H. Schelp, A class of edge critical 4-chromatic

graphs, Graphs and Combinatorics 13. (1997) 139–146.

[5] B. Bollob´as, On generalized graphs, Acta Math. Acad. Sci. Hung. 16 (1965), 447–

452.

[6] P. Erd˝os, R. Faudree, A. Gy´arf´as, R. H. Schelp, Domination in colored complete

graph, Journal of graph Theory 13 (1989) 713–718.

[7] P. Erd˝os, R. Faudree, A. Gy´arf´as, R. H. Schelp, Cyles in graphs without proper

subgraphs of minimum degree 3, Ars Combinatoria 25 B. (1988) 195–201.

[8] P. Erd˝os, R. Faudree, R. Gould, A. Gy´arf´as, C. Rousseau, R. H. Schelp, Monochro-

matic coverings in colored complete graphs, Congressus Numerantium 71. (1990)

29–38.

[9] P. Erd˝os, R. Faudree, C. C. Rousseau, R. H. Schelp, Subgraphs of minimum degree

k, Discrete Mathematics 85. (1990) 53–58.

[10] P. Erd˝os, A. Hajnal, J. W. Moon, A problem in graph theory, Amer. Math. Monthly

71 (1964), 1107–1110.

[11] P. Erd˝os, A. Hajnal, Ramsey-type theorems, Discrete Appl. Math. 25. (1989) 37–52.

[12] P. Erd˝os, A. Gy´arf´as, Vertex covering with monochromatic paths, Mathematica

Pannonica 6 (1995), 7-10.
 10

[13] P. Erd˝os, A. Gy´arf´as, A variant of the classical Ramsey problem, Combinatorica 17

(1997) 459–467.

[14] P. Erd˝os, A. Gy´arf´as, Split and balanced colorings of complete graphs, Discrete

Mathematics 200. (1999) 79–86.

[15] P. Erd˝os, A. Gy´arf´as, L. Pyber, Vertex coverings by monochromatic cycles and

trees, Journal of Combinatorial Theory B 51. (1991) 90–95.

[16] P. Erd˝os, A. Gy´arf´as, M. Ruszink´o, How to decrease the diameter of triangle-free

graphs? Combinatorica 18 (1998) 493–501.

[17] P. Erd˝os, A. Gy´arf´as, E. T. Ordman, Y. Zalcstein, The size of chordal, interval and

thresold subgraphs, Combinatorica 9 (1989) 245–253.

[18] P. Erd˝os, A. Hajnal, Egy kombinatorikus probl´em´ar´ol, Matematikai Lapok 19.

(1968) 345-348.

[19] P. Erd˝os, Problems and results in graph theory and combinatorial analysis (French

summary), Probl`emes combinatoires et thorie des graphes (Colloq. Internat. CNRS,

Univ. Orsay, Orsay, 1976), Colloq. Internat. CNRS, 260 , pp. 127–129, CNRS, Paris,

1978

[20] P. Erd˝os, A selection of problems and results in combinatorics, Combinatorics,

Probability and Computing 8. (1999) 1-6.

[21] J. Fox, B. Sudakov, Ramsey-type problem for an almost monochromatic K4, SIAM

Journal of Discrete Mathematics 23 (2008), 155-162.

[22] A. Gy´arf´as, Fruit salad, Electronic J. of Combinatorics 4 (1997) 1-8.

[23] L. Gerencs´er, A. Gy´arf´as, On Ramsey type problems, Ann. Univ. Sci. E¨otv¨os, Bu-

dapest 10 (1967) 167 – 170.

[24] A. Gy´arf´as, M. Ruszink´o, G. N. S´ark¨ozy, E. Szemer´edi, Partitioning 3-colored

complete graphs into three monochromatic cycles, Electronic J. of Combinatorics

18(2011) N.53.
 11

[25] A. Gy´arf´as, M. Ruszink´o, G. N. S´ark¨ozy, E. Szemer´edi, An improved bound for the

monochromatic cycle partition number, J. of Combinatorial Theory B. 96(2006)

855–873.

[26] A. Gy´arf´as, G. N. S´ark¨ozy, S. Selkow, Coverings by few monochromatic pieces - a

transition between two Ramsey problems, arXiv:1304.0871v1 [math.CO] 3 Apr 2013

[27] F. Jaeger, CH. Payan, Nombre maximal dar´etes dun hypergraphe critique de rang

h, C. R. Acad. Sci. Paris 273 (1971) 221–223.

[28] G. O. H. Katona, Solution of a problem of Ehrenfeucht and Mycielski, J. Combin.

Theory A 17 (1974) 265–266.

[29] A. Kostochka, Sequences of dominating sets, Math. Pannonica 1 (1990) 51–54.

[30] D. Kral, C. Liu, J. Sereni, P. Whalen, Z. B. Yilma, A new bound for the 2/3 conjec-

ture, Combinatorics, Probability and Computing doi:10.1017/S0963548312000612

[31] A. Kostochka, D. Mubayi, When is an almost monochromatic K4 is guaranteed?

Combinatoics, Probability and Computing 17 (2008) 823–830.

[32] T.  Luczak, V. R¨odl, E. Szemer´edi, Partitioning two-colored complete graphs into

two monochromatic cycles, Probability, Combinatorics and Computing 7 (1998),

423–436.

[33] D. Mubayi, Edge coloring cliques with three colors on all 4-cliques, Combinatorica

18 (1988) 293–296.

[34] D. Mubayi, An explicit construction for a Ramsey problem, Combinatorica 24

(2004) 313–324.

[35] A. Pokrovskiy, Partitioning edge-coloured complete graphs into monochromatic cy-

cles and paths, arXiv:12.05.5492v1

[36] B. Reed, Mangoes and blueberries, Combinatorica 19 (1999) 267-296

12

[37] G. N. S´ark¨ozy, S. M. Selkow, On edge colorings with at least q colors in every subset

of p vertices, Electronic J. of combinatorics 8 (2001) RP9.

[38] G. T´oth, unpublished.
 13
