<!-- source: https://www.renyi.hu/~p_erdos/1988-06.pdf | converted from PDF -->

Cycles in graphs without proper subgraphs of minimum degree 3

P . ERDOS * , R . FAUDREE, A . GYÁRFÁS ** , R . H . SCIIELP ***

Memphis State University

1 . Introduction .

Let G(n,m) denote the set of graphs with n vertices and m edges . It is well-known

that each G c G(n,2n - 2) contains a subgraph of minimum degree 3 but there exists a

G cG(n,2n - 3) with no subgraphs of minimum degree 3 (see [1] p . xvü) .

It was proved in ~2] that each G e G(n, 2n - 1) contains a proper subgraph of minimum

degree 3, but there exists G cG(n, 2n - 2) without this property. In fact, a stronger result

was proved in [2], namely that GcG(n,2n- 1) must contain a subgraph of minimum

degree 3 with at most n - c V/n vertices for some c > 0 . It was conjectured in [21, that each

GcG(n,2n - 1) contains a subgraph of minimum degree 3 with at most cn vertices for

some absolute constant c < 1 .

In this paper we study cycle lengths of graphs which have no proper subgraphs of

minimum degree 3 . For ease of reference, let G* (n, m) denote the set of graphs with n

vertices, m edges and with the property that no proper subgraph has minimum degree

3 . The results mentioned so far show that C c G* (n, m) implies m < 2n - 2, and if

G eG*(n, 2n - 2) then G has miminum degree 3. Throughout the paper we investigate the

cycle structure of graphs G, with G e G*(n, 2r.-2) . In fact we give the following conjecture .

CONJECTURE : If GeG*(n,2n-2), then G contains all cycles of length at most k where

k tends to infinity with n .

Our results are all related to this conjecture . We have several examples to demon-

strate the role of 2n - 2 in this conjecture . For example for each n there exists graphs

G, GeG*(n,2n -3), such that G has no triangle (Examples 1 and 2) . It is also true that

there are G eG*(n, 2n- 3) such that G has no cycles of length 5 or more (Example 3) . For

every r, we construct a graph G cG* (n, 2n - c(r)) such that G has no cycles of length less

than or equal to r (Theorem 4) . In fact, the minimum value of c(r) is determined precisely

for r = 3, 4 .

On one hand, our conjecture says that the graphs in G * (n, 2n -2) contain small cycles .

We prove that these graphs contain C3 i C4 and CS (Theorem 2 .) On the other hand, our

conjecture says that the graphs in G* (n, 2n - 2) contain long cycles . Our main result is

that G e G* (n, 2n - 2) contains a cycle of length at least (lognj (Theorem 5 .) . However,

*Hungarian Academy of Sciences
**On leave from Computer and Automation Institute, Hungarian Academy of Sciences
***Research partially supported under NSF grant no . D`vIS-8603717

ARS COMBINATORIA 258(1988), pp . 195-201 .

graphs in G'(n, 2n - 2) does not always contain very long cycles (as large as of for some

c > 0, Example 7) .

2 . Properties of Graphs without proper subgraphs of minimum degree 3 .

In this section we give a lemma and a theorem which we shall use frequently in sections

3 and 4. We first introduce some terminology .

Consider an ordering x1, x2, . . .,x2 of the vertex set of a graph . An edge xixj,i > j

of the graph is called a forward edge on x i and a backward edge on xj . The forward

(backward) degree of xi is the number of forward (backward) edges incident to xi . We shall

let d+(xi), d- (xi) denote the forward and backward degree of xi, respectively .

For any graph G we formally define an ordering of the vertices of G as follows : x 1

is a vertex of minimum degree in G . If x1,x2, . . . xt are already defined and t < V(G)I,

then let xt+1 be a vertex of minimum degree in G - {x1,x2, . . .,xt} . If G has no proper

subgraph of minimum degree 3, then d+(xi) <- 2 for 2 <_ i < ~V(G)J . Since we shall use

this ordering often, we formulate this statement as lemma .

LEMMA 1 . Let G have n vertices and contain no proper subgraph of minimum degree 3 .

Then, the vertices of G can be ordered so that d+(x1) is the minimum degree of G and

d+(zi) <_ 2 for i > 2 .

THEOREM 1 . IfG EG'(n,2n-2), then the vertices ofG can be ordered so that d+(x1) _

3, d+(xi) = 2 for 2 <- i <- n - 2, and d + (xn-1) = 1 . Moreover d- (xi) >_ 1 for 2 <_ i 5 n .

PROOF : In the ordering of the vertices described in Lemma 1 observe that

n-1
2n-2=I E(G)i=

 d+(xi)<d(x1) +2(n-3)+1<2n-2 .

i=l

Since d(x1) <- 3 (otherwise G has at least 2n edges), d-(xi) <- 2 for i = 2,3, . . . , (n - 2)

and d+(x n -1) < 1, all the inequalities are equalities . Thus, d+(x1) = 3, d (xi) = 2

for 2 <- i <- n - 2, and d-(x n 1) = 1 . Since d(xi) ? d(x1) = 3 and d+(xi) < 2 for

1 < i <_ n, d - (xi ) ->- 1 follows . ∎

COROLLARY 1 . IfGeG'(n,2n-2) then G has minimum degree 3 .

3 . Small Cycles in G'(n,2n - 2) .

THEOREM 2 . If GcG'(n,2n - 2) then for n ? 5, G contains a C3 and a C; . If

G e G' (n, 2n - 3) and n > 6, then G contains Cq .

PROOF : For G E G' (n, 2n-2) consider the ordering of vertices given in Theorem 1 . Clearly,

196

xn-2,xn-1 and x n determine a C3 . Without loss of generality we may assume that xn-3

is adjacent to x n_1 and xn .

Assume that i is the largest index such that xi is adjacent to xj for some j, i < j < n-1 .

There exists such an index since i = 1 is a suitable choice. If xi is adjacent to xn -1 or

to xn , say to x n, then select any k > i such that k # j,k # n,k # n - 1. This gives the

C5, xix n xkxn _Lxjxi in G .

If xi is not adjacent to either x n_1 or to xn , then (since d+(xi) = 2) xi is adjacent to

some xk, with i < k, j k, n # k, n - 1 0 k . But then xixkxn -1x n xj xi is a C5 in G .

To see that GcG`(n, 2n - 3) contains a C4, observe that Theorem I almost holds in

that we can order the vertices of G as x1, x2, . . . , x n so that at most one of the equalities

d+(xi) = 2 for 2 <- i <- n - 2, d+(xi) = 3, and d + (xn _1) = 1 fails to hold . Moreover if

equality does not hold for some i then d+(xi) is just one less than the value shown above . If

each of the equalities d+ (xn _1) = 1, d+(x n_2) = d+(x n_3) = 2 hold then the subgraph of

G induced by X = {xn-3, xn-2, xn-1, xn } has five edges and there is a C4 in G . Therefore,

we assume that there is no C4 in the subgraph induced X . Also, by a suitable permutation

of the vertices in X, we may assume that xn-3xn-2i xn-3xn-1, xn-3xn and xn -2xn -1 are

edges in X . But d+(xn _4) = 2 and the only way to avoid a C4 in G is to assume xn -4 to

be adjacent to xn _3 and to x n . Since n ? 6, xn _5 exists and d+(xn _5) >_ 2 . Thus, there

exists a C4 in G containing x n_5 and three vertices of {xn,xa-1X-1, X-2, X-3, Xn-4} -E

With more work it is possible to show that GcG'(2n-2) always contains Cc, for n ? 6 .

The following constructions show that Theorem 2 is sharp .

EXAMPLE 1 : Let n > 6 be even . Consider the graph on n vertices defined as follows . Let

x1x2 . . . xn-2 be a cycle of length n - 2. Let y and w be two new vertices with y adjacent

to all xi of even index and w adjacent to all xi of odd index . Finally place an edge between

y and w . The graph obtained contains no triangles, (in fact, is bipartite) has no proper

subgraph of minimum degree 3, and has 2n - 3 edges. ∎

EXAMPLE 2 : Let n = 2k } 1 ? 9 and consider a cycle of length k with vertices xl x2 - - xk

For í = 1,2, . . .,k - 1 place new vertices y i in the graph with each yi adjacent to xi.

Finally, let v and w be two additional vertices of the graph such that each are adjacent to

y1, y2, . .,yk-1 and xk . The resulting graph has 2n - 3 edges, no triangle and no proper

subgraph of minimum degree 3 . ∎

EXAMPLE 3 : Consider the graph obtained from K2 n-2 by placing an edge between the

two vertices of the two-vertex color class . This graph has no cycles of length 5 or more, has

2n - 3 vertices, and contains no proper subgraph of minimum degree 3 . ∎

EXAMPLE 4 : Assume that n - 2 is divisible by 4, n >- 10, and consider a cycle of length

n - 2 with vertices x1, x2, x3, . . . , xn _2 . Let y and w be two new vertices . Join vertex y to

197

xi for i - 1 or i - 2(mod 4) and join w to xi for i 0 or i = 3 (mod 4) . This graph has

no C4, has 2n - 4 vertices, and has no proper subgraphs of minimum degree 3 . It is easy

to modify this example for n = 0, 1, 3 (mod 4) . ∎

Based on these examples, we conclude that Theorem 2 is sharp : there exists

G cG*(n, 2n - 3) without C3 (Example 1 and 2) ; there exists G c G* (n, 2n - 3) without

C5 (Example 1 and 3) ; there exist G cG*(n,2n- 4) without C4 (Example 4) .

Up to now we've only considered the existence of Ck (for k = 3,4,5) in G cG*(n, 2n-2) .

V6 'e continue by looking for the minimum m that GeG* (n, m) contains a cycle of length

less than r . Theorem 2 and Examples 1 and 2 show that m = 2n - 2 when r = 4 . The

upper bound for m in cases r = 5 and r = 6 are given in the next result .

THEOREM 3 . Let g(G) denote the girth ofG . Ifn >: 6 and G cG*(n, 2n-4), then g(G) <- 4
 .

Ifn? 8 and G c G*(n, 2n - 6) then g(G) <<-5
 .

PROOF : Assume G cG*(n,2n- 4) and apply Lemma 1 . Clearly d+(xi) <- 3, otherwise G

has at least 2n edges . If n ? 6 the subgraph H induced by x n , x n_t, xn-2, xn-3, xn-4 in G

has at least (2n - 4) - 3 - 2(n - 6) = 5 edges . We may assume that H is a cycle of length

5, otherwise H contains C3 or C4 and g(G) _< 4 follows . Therefore d+(xt) = 3,d+(xi) = 2

for i = 2,3, . . . , n - 5 . But xn _5 is adjacent to two vertices of the five-cycle H giving a C3

or C4 .

To prove the second part of the Theorem, assume G c G* (n, 2n-6) and apply Lemma 1
 .

Again, d+(xl) < 3 . Since n ? 8, we consider the subgraph H induced by {xn, xn-L xn-2,

xn-3, xn-4, xn-5, xn-6} in G . Thus, H contains at least (2n - 6) - 3 - 2(n - 8) = 7 edges .

Let C be a cycle of H with minimum length, so that C is a cycle without a diagonal . If
C 1 = 7 then H - C and d+(x r ) = 3, d+(xi) = 2 for i = 2,3,.,,, n - 7 . In particular,

zn _7 is adjacent to at least two verices of C giving a cycle of length at most 5 . If ~C 1 = 6,

then without loss of generality assume xn,xn-t,xn-2,xn-3,xn-4,xn_5,xn is a 6 - cycle

and x_ G is adjacent to x n_5 . If xn _6 is adjacent to any vertex x i for n - 4 < i <- n then

we have a C3, C 4 or C5 . Therefore, H has 7 edges and again d+(xl) = 3,d - (xi) = 2 for

2 < i <- n - 7 . In particular d+(x n _7) = 2, and it is easy to check that the only case

when x n_7 ixn _6, . . . ,x n does not induce a cycle of length at most 5 in G occurs if x n_7 is

adjacent to x n_6 and xn _2 (see Figure 4) . It is easy to see that d+ (x n_8) = 2 implies the

existence of a cycle of length at most 5 . Thus C1 <- 5 completing proof of the theorem . ∎

To show that the first part of Theorem 3 is best possible we give the following example .

EXAMPLE 5 : Assume n is divisible by 5 and n ? 10 . Let x l x3 x5x 2x 4x r be a five-cycle

and y ly2 . . . yn-5 yt is a n - 5 cycle. Vertex xi is adjacent to yj if and only if j i (mod

5) (for all i, 1 < i <- 5) . This graph has 2n - 5 edges, has no proper subgraph of minimum

degree 3 and contains no C3 or C4 .
 198

We do not know examples of G c G' (n, 2n - 7) with g(G) > 6 for infinitely many n .

However, it is possible to find G cG'(n, 2n - 8) with g(G) = 6 for infinitely many n .

The next theorem shows that graphs in G'(n,2n - c) do not always contain small

cycles .

THEOREM 4 . For every postive integer r there exists c = c(r) and a graph

GeG'(n,2n-c(r)) such thatg(G) > r .

PROOF : Let k be a natural number and let C1, C2, . .. ,Ck be vertex disjoint cycles of length

t = 2 .5'+ 1 -1 . We shall define the graph Gk by adding edges to the graph C1 UC2 U . . .UCk .

Assume that the vertices of C i are xj, x'2 , .. . , x, (indexed in the natural order of the cycle)
 .

The definition of Gk is recursive . Set G, = C l . If G 1,G2, . . . ' Gk_ 1 are already defined we

shall define Gk by adding edges xy to Gk- 1 U Ck such that xcCk, ycCk-1
 . The definition

will preserve the following properties (for each i, 1 <- i <- k) :

(i) each cycle of Gi is longer than r

(ü) the maximum degree of Gi is at most 5, and

(iii) dG . (xi) = 4, dG. (xt) = 2, dG . (x~) = 3 for 2 < j -< t - 1 and i >- 2 .

Note that properties (i), (ü) and (iii) trivally hold for i = 1, since G, = C1 .

To define Gk we add edges eo = xkW, ei = xjy1, e2 = x kY2, e3 = xjy3, -et-1 =

xt-lyt_1 to Gk-1 U Ck, such that yjEV(Ck- 1) for j = 0,l, . . .,t - 1 and Gk satisfies

properties (i), (ü), and (iii) for i = k . Observe that (iii) holds independent of the choice of

each yj , so that we need only select each yj such that (i) and (ü) hold . The edge eo can be

defined arbitrarily . Assume that eo , el, . . . , ea are defined for 0 S s < t - 1 in such a way

that properties (i) and (ü) hold for G' = Gk- 1 U Ck U {eo,el, . . .,e,,) . We define e g-1 as

follows . Let W denote the set of vertices in Ck_ 1 which can be reached by a path of length

at most r from xs+, in the graph G' . Since (ü) holds for G', W
 1 < 5'+1 and therefore

~V(Ck_ 1) - W 1 > t - 5'+1 = 5r+1 - 1. Let T be a subset of V(Ck- 1 ) - W such that

DTI = 5'+ 1 By definition, for any yET the graph G' U es+1 statisfies (i) with e,,+1 = xs+1y .

Using property (iii) for i = k - 1

dG,;_,(y) < 31T 1 + 1 = 3 .5r+1 + 1 .

ycT

Since G' is obtained from Gk_ 1 by adding s + 1 edges,

J~ dG'(y)<~,d0k_1(y)+s-*-1<3 .5'+1+1 t-1=5 r+2 -

ycT

 ycT

Thus there exists an ys+1cT with dG (ys+i) < 5 . Thus with es+, = x k,+lye+L the graph

199

G" = G' U ee+1 satisfies properties (i), (ü) and (iii) . Therefore Gk is defined .

It is clear that IV(G k )l = kt and JE(Gk)l = 2kt-t . The proof is completed by showing

that Gk has no proper subgraph of minimum degree 3 . Assume to the contrary that G*

is such a proper subgraph. Since dGk (xt) = 2, x~ V(G*) . However, dCk _ zi (xL_ 1 ) = 2

implies XL_ 1 V(G*) . Repeating this argument we get that xj V(G*) for 1 <_ j <_ 1.

But dGk -Ck (xk-1 ) = 2 and by observations just like those made above, none of the

vertices of Ck_ 1 belong to G* . Continuing in this way we see that G* is the empty graph,

a contradiction . Hence Gk c G* (ík, 2tk - t) for all k with t = 2 • 5r+ 1 - 1, showing that

c(r) = 2 •fi r+ 1 - 1 is a suitable choice . ∎

4 . Long cycles in G*(n,2n-2) .

In this section we prove one of the main results o£ the paper, that is G c G* (n, 2n - 2)

contains a long cycle . Note that G cG*(n, 2n - 3) does not necessarily contain even a path

of length 4 (see Example 3 in Section 2) .

THEOREM 5 : If GcG*(n,2n - 2), then G contains a cycle of length at least (logn) .

PROOF : Consider the ordering of G of Theorem 1 . Since d- (x%) > 0 for i = 2, . . ., n, we

can find a spanning tree T recursively in G as follows . Place x1 in T . Ifx1, x2, . . . , xt are in

T and t < n, then choose any edge xixt+l of G such that 1 <_ i <- t . Redefine T by adding

vertex xt-1 and the edge xixt+l to the old T . By definition of the tree, d- (x%) = 1 in T

for 2 < i < n and d- (x i ) <- 2 in T for 2 <_ i < n . Since d+(x 1) = 3 in G, T is a tree of

maximum degree < 3. Therefore, T contains a path P of length at least [logn] starting

with xi .

Let x1 = xi,,xi 2 , . . . , xi k denote the vertices of P in the natural order defined by P i .e

xi, xi1+i 's an edge of P for 1 <_ j < k - 1 . Notice that i1 < i2 < . . . < ik follows from the

definition of T since d- (xi) < 2 in T for 2 <- i <_ n . We call a path P = (xil , xi2 , . . .
 I " 'k)

in G a forward path if i1 < i2, • . . < ik . Note that the definition depends on the order

x1, x2, . . .x„ defined by Theorem 1 . The discussion up to this point insures that G has a

forward path of length at least (logn) .

Let P = (xü,xi2, . . . . xi.) be a forward path of G with a maximum length . Since

d - (xi) ? 1, and d+(xi) ? 1 in G for 2 < i <- n- 1, it follows that i1 = 1, ik = n. Let

t be any positive integer such that 1 < t < k and it 0 n - 1 . Since d+(xi) ? 2 in G for

1 < i < n-2, we can find a forward path Pt in G starting at xi* and ending at some vertex

xi* r of P such that

(a) Pt and P are edge disjoint

(b) V(Pt) nV(P)={x ,x }

:Vote that (a) implies t+1 < t' . We claim for t < s that the paths Pt and Ps are vertex

disjoint if t1 < s or if s = t'- 1 . The case t' < s is obvious since both Pt and Pg are forward

200

paths . Assume s = t' - 1 . But t + 1 < t' and s + 1 < s implies that Pt and Pa do not have

common endpoints . Assume that x is the last common vertex of Pe and Pt we find on Ps

by traveling along P, from its starting point xi a . It is easy to see that the following edge

sequence is a forward path : starting from xi, = x t , travel along P to xie ; continue on Ps

to x; from x travel to xi,i = xia+, along Pt : finally from xi,, to xi k = x„ travel along P .

This path is longer that P . This contradiction proves the claim .

Choose a subset Q1,Q2, . . .Q r of the paths P1,P2, . . .,Pt as follows. Set Ql = P1 . If

Ql,Q2, . . .,Qs are defined and the endpoint xie , ofQ,9 is not x a then Qs+1 = Ps,-1 . If the

endpoint xi. t of Q s is x„ then set r = s .

It is now easy to construct a cycle using all the vertices of P U Qt U . . . U Qr . But P

has at least [logn] vertices so that the cycle C has length at least (logn) .∎

Finally, to see that GcG*(n,2n - 2) does not contain necessarily a very long cycle,

(larger that cVn) consider the following example .

EXAMPLE G: Let k be an integer, k ? 4 . Let C be a k -cycle with vertices 11, M2- . , xk .

Select a new vertex w and connect w to each xi with vertex-disjoint paths of length k - 1 .

(The only common vertex of these paths is w) . Select another new vertex y and let y be

adjacent to all vertices except those of {x2,x3, . . .,xk} . Let G k be the graph just defined .

The graph Gk has k(k-1)+2= n vertices. Since d(w) = k+1, d(y) = n- k, d(x l) = 4

and all the other vertices are of degree 3, Gk has

k+1+n-k+4+(n - 3)3 _2n-2
2

edges. It is easy to check that G k has no proper subgraph of minimum degree 3 . It is also

easy to see that the longest path of Gk - y is smaller that 5k . Therefore the longest path

of Gk is smaller that 10k <- 10 Jn + 1.

REFERENCES

1. B. Bollobas, Extremal Graph Theory, AP 1978 .

2 . P . Erdős, R.F. Faudree, C.C. Rousseau, R .H. Schelp, Graphs With Proper Subgraphs

Of Fixed Minimum Degree, in preparation .
