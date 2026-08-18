<!-- source: https://faculty.washington.edu/cemann/Heesch.pdf | converted from PDF -->

Heesch’s Tiling Problem

Casey Mann

1. INTRODUCTION. Let T be a tile in the plane. By calling T a tile, we mean that
T is a topological disk whose boundary is a simple closed curve. But also implicit
in the word “tile” is our intent to use congruent or reﬂected copies of T to cover the
plane without gaps or overlapping; that is, we want to tessellate the plane with copies
of T . In a minor abuse of language, one often speaks of T (as opposed to copies of
it) as tiling or tessellating the plane, in the sense that T generates a tessellation. A
tessellation by T may or may not be possible, so in order to learn something of T ’s
abilities with regard to tessellating the plane, we perform the following procedure:
around a centrally placed copy of T , we attempt to form a full layer, or corona,of
congruent copies of T . We require as part of the deﬁnition that no point of T should
be visible from the exterior of a corona to a Flatland creature in this plane. Also,
we should form the corona without allowing gaps or overlapping, just as if we were
building a tessellation. If a corona can be formed, then we attempt to surround this
corona with yet another corona, and then another, and so on; if we get stuck, we go
back and change a previously placed tile and try again. If T tessellates the plane, then
this procedure will never end. On the other hand, if T does not tessellate the plane, and
if we check all of the possible ways of forming a ﬁrst corona, a second corona, and
so forth, we will ﬁnd that there is a maximum number of coronas that can be formed.
This maximum number of layers that can be formed around a single centrally placed
copy of T is called the Heesch number of T and is denoted by H (T ).
We consider a few examples before proceeding. Consider ﬁrst a regular hexagon.
All bees know that a regular hexagon tessellates the plane, so H =∞ for a regular
hexagon. Next consider a regular pentagon. It is not hard to see that not even a single
corona of copies of a regular pentagon can be formed around a central copy, whence
H = 0 for a regular pentagon. These two examples exhibit the “typical” behavior of
tiles with respect to Heesch numbers: if one considers an arbitrary tile, it is usually the
case either that the tile tessellates the plane (H =∞) or that one cannot form even a
single corona (H = 0). Naturally one wonders if there are tiles with Heesch number
1, 2, 3,... . This question is known as Heesch’s Tiling Problem (see [9, p. 23], [7,
p. 155], or [8, p. 187]):

Open Question 1 (Heesch’s Tiling Problem). Given a positive integer N , does there
exist a tile TN with H (TN ) = N?

Interestingly, before Heinrich Heesch stated his problem in 1968, only one tile with
Heesch number other than 0 or ∞ had been observed—a curvilinear tile called a
spandrel (Figure 1) with Heesch number 1 was published by Lietzmann in 1928 [10,
p. 242], [11]. Heesch himself identiﬁed a tile with Heesch number 1 in the same paper
where he ﬁrst posed his problem [9, p. 23]. It wasn’t until 1991 that examples with
ﬁnite Heesch number greater than 1 were given. First, an inﬁnite family of U-shaped
polyominoes, each having Heesch number 2, was described by Fontaine [4](seeFig-
ure 2). In that same year a hexagon with notched edges (Figure 3) having Heesch
number 3 that had been discovered by Robert Ammann was presented at a special
session on tiling at a regional AMS meeting in Philadelphia (and was featured on the

June–July 2004] HEESCH’S TILING PROBLEM 509

Figure 1. Lietzmann’s spandrel with one corona.

2
2
 4
4 1
 11
 33

Figure 2. Fontaine’s U-shaped polyomino with two coronas.

Figure 3. Ammann’s notched hexagon with three coronas.

coverofthe meetingprogram)[17], [18]. In this article we introduce a few families of
tiles with Heesch numbers 3, 4, and 5, as well as other examples.

2. NEW EXAMPLES. Consider Ammann’s notched hexagon more closely. First,
notice that all of the bumps and nicks are centered on the edges, and all are of the

510 c⃝ THE MATHEMATICAL ASSOCIATION OF AMERICA [Monthly 111

same shape. That the bumps and nicks have the same shape ensures that any bump
can meet any nick; that they are centered allows two copies of the tile to meet along an
edge regardless of whether or not one of the tiles has been reﬂected. One might wonder
if a different combination of bumps and nicks could give a hexagon with Heesch num-
ber greater than 3, but this is not so. To see this, one could simply enumerate all of the
possibilities and check each case individually, but there is an interesting phenomenon
at play here that is worth investigating. The reason that Ammann’s tile cannot tessel-
late the plane is that it is combinatorially unbalanced—it has more nicks than bumps.
Epstein [3] gave a simple proof that no hexagon can have Heesch number greater than
three if its edges are marked so that there are unequal numbers of bumps and nicks.
Suppose that a fourth corona of such a notched hexagon has been formed. Such a con-
ﬁguration contains sixty-one hexagonal tiles and has ﬁfty-four edges on its boundary.
Say that there are more bumps than nicks on this tile. Then there are at least sixty-one
unmatched bumps, bumps that must appear on the boundary of the conﬁguration. But
since there are only ﬁfty-four edges on the boundary, there is not enough room for all
of the bumps!
We can generalize Ammann’s hexagon by “fusing” two or more hexagons to form a
polyhex and marking the edges of the polyhex with bumps and nicks. To illustrate this
with a new example of our own, the tile in Figure 4 is formed by gluing together three
hexagons and marking a few edges with bumps and nicks. This particular example has
been shown by an exhaustive computer search to have Heesch number 2.

Figure 4. A combinatorially unbalanced polyhex with Heesch number 2.

The combinatorial device that constrained Ammann’s original tile is still in evi-
dence here. No polyhex with an unequal number of bumps and nicks can tile the plane,
and for essentially the same reason that Ammann’s original tile did not: at some stage
there would necessarily be more unmatched bumps (or nicks) than boundary edges of
the outer corona. However, as the size of a polyhex grows (in terms of the number
of hexagons it comprises), so does the potential for achieving a high Heesch number.
While we cannot accurately predict the Heesch number of an arbitrary combinatorially
unbalanced polyhex, we can give an upper bound for the Heesch numbers of combina-
torially unbalanced polyhexes formed from n hexagons; namely, the Heesch number
is roughly O(
√n) [12]. This is a very interesting and important observation, for it tells
us that combinatorially unbalanced polyhexes, which are geometrically and combina-
torially simple (relatively speaking), have the potential to give arbitrarily large Heesch

June–July 2004] HEESCH’S TILING PROBLEM 511

numbers. The reader should pause and reﬂect on this amazing possibility: imagine a
tile that allows, say, 1,000,000 coronas to be formed, but that somehow does not gen-
erate a complete tiling of the plane! One is tempted to discount this possibility, but we
hope that as the reader proceeds he or she may become more open to it.
We now consider an inﬁnite family of combinatorially unbalanced polyhexes that
we have named hexapillars.An n-hexapillar is a polyhex formed by fusing n hexagons
in a row and marking the edges with bumps and nicks as in Figure 5.

Figure 5. A 5-hexapillar.

The status of the Heesch numbers for these hexapillars is given in the following
theorem [12, p. 25]:

Theorem 1. The 2- and 3-hexapillars have Heesch number 4, while the n-hexapillars
with n ≥ 4 have Heesch number 5.

Finding the Heesch numbers of speciﬁc n-hexapillars for small n was accomplished
by means of an exhaustive computer search. A proof for the general case can be found
in [12]. It was discovered independently by Marshall that the 2-hexapillar has Heesch
number 4 [14]. Figure 6 depicts the 5-hexapillar along with ﬁve coronas.

Figure 6. A 5-hexapillar surrounded by ﬁve coronas of 5-hexapillars.

We have also discovered a second inﬁnite family of tiles in which each tile has
Heesch number 3. These tiles are analogous to the hexapillars, but instead of be-

512 c⃝ THE MATHEMATICAL ASSOCIATION OF AMERICA [Monthly 111

ing formed from hexagons they are constructed from squares. Tiles constructed from
squares are usually called polyominoes. We call these particular polyominoes polypil-
lars (Figure 7).
 Figure 7. A 7-polypillar.

Theorem 2. Let Tn be an n-polypillar. Then H (Tn) = 2 for n = 2 or 3, and H (Tn) = 3
for n ≥ 4.

The behavior of polypillars is similar to that of hexapillars, so Theorem 2 is es-
tablished in much the same way as Theorem 1. In Figure 8 we see a 7-polypillar
surrounded by three coronas.

Figure 8. A 7-polypillar surrounded by three coronas.

3. THE TILING PROBLEM. Heesch’s tiling problem is connected to another un-
solved tiling problem that is central to the subject. Before stating this problem, we need
to establish a small amount of terminology. Often one wants to use more than one kind
of shape to tile the plane. The shapes with which one wants to tessellate the plane are
collectively called a protoset. The individual tiles in a protoset are called prototiles.In
the case that a protoset contains only one prototile, the distinction between the protoset
and the prototile is blurred, and in this case both are called monotiles.

Open Question 2 (The Tiling Problem for Monotiles). Does there exist an algo-
rithm or standard procedure that can take as input an arbitrary single tile and deter-
mine in a ﬁnite number of steps whether or not that tile tessellates the plane?

June–July 2004] HEESCH’S TILING PROBLEM 513

If such an algorithm exists, we say that the problem is decidable. The tiling prob-
lem for arbitrary protosets was shown to be undecidable by Berger in [1] and later by
Robinson [16]. But for protosets of any ﬁxed size, the problem remains open; in par-
ticular, it is still open for monotiles. To see how Heesch’s tiling problem is connected
to the tiling problem for monotiles, we ﬁrst make the very mild restriction that two
copies of the tile can meet in only ﬁnitely many ways (i.e., we consider only tiles with
ﬁnitely many vertices and edges and require that tiles meet vertex-to-vertex). This re-
striction reduces the problem of deciding when two tiles can meet to consideration of
a ﬁnite number of possibilities. Now suppose that there is a maximum ﬁnite Heesch
number M that can be obtained by any single tile. An algorithm for this restricted ver-
sion of the tiling problem for monotiles would then go as follows. Given a tile with
only ﬁnitely many edges and vertices, start with a single centrally placed copy of the
tile and begin forming coronas around it, creating all possible ﬁrst coronas, then all
possible second coronas, then all possible third coronas, and so forth, until one of two
things happens: either we form more than M coronas, in which case the tile must tes-
sellate the plane, or we ﬁnd that it is impossible to form M coronas, in which case the
tile cannot tessellate the plane. Thus we have established the following theorem:

Theorem 3. If the tiling problem for monotiles with ﬁnitely many vertices and edges
is undecidable, then there is no ﬁnite upper bound on Heesch numbers.

On an interesting side note, the tiling problem for monotiles is connected with an-
other famous open problem in the theory of tilings, the Einstein problem.
1 This prob-
lem concerns aperiodic monotiles. A protoset is said to be aperiodic if (1) its tiles
tessellate the plane and (2) every possible tessellation by these tiles is nonperiodic.
2
Many aperiodic protosets have been discovered, from protosets containing many thou-
sands of tiles [1] down to protosets containing only two tiles, the most famous of these
being the Penrose rhombi [15], [5]. It remains to be seen whether or not an aperiodic
monotile exists:

Open Question 3 (Einstein Problem). Does there exist an aperiodic monotile?

To see how the Einstein problem is linked to the tiling problem for monotiles, sup-
pose that there does not exist an aperiodic monotile. Then every tile that tessellates the
plane must give rise to at least one periodic tessellation of the plane. An algorithm for
deciding whether or not an arbitrary tile tessellates the plane could then be constructed
as follows. First, we again need to assume that copies of the tile can meet in only
ﬁnitely many ways. If we then systematically form all possible ﬁnite patches of copies
of the tile that cover circular disks centered at the origin of discretely incremented in-
creasing area, one of two things can happen: (1) at some step a fundamental domain
for a periodic tiling group
3 is found (there are only seventeen periodic tiling groups, or
“crystallographic” groups), or (2) we ﬁnd a disk that cannot be covered, implying that

1The word “Einstein” in the Einstein problem is a pun: “ein” = “one” and “stein” = “tile.” It is attributed
to Ludwig Danzer.
2A tessellation of the plane is periodic if its symmetry group contains two nonparallel translations. There is
often some confusion distinguishing between the terms “aperiodic” and “nonperiodic.” The term “nonperiodic”
refers to a particular tessellation, whereas the term “aperiodic” refers to a protoset.
3A tiling group is representative of an isomorphism class of symmetry groups of tessellations. A funda-
mental domain for a tiling group is a smallest conﬁguration of tiles that when acted on by the tiling group
generates a tiling of the plane.

514 c⃝ THE MATHEMATICAL ASSOCIATION OF AMERICA [Monthly 111

a tessellation of the plane is not possible.
4 Thus we have proved the following theorem
(originally noted by Wang in [20]):

Theorem 4. If the tiling problem for monotiles is undecidable for monotiles that have
ﬁnitely many vertices and edges and that meet vertex-to-vertex, then there exists an
aperiodic monotile.

The tiling problem for monotiles has implications for several other open tiling prob-
lems; for further reading on this interesting topic see [5].

4. MORE ON HEESCH’S PROBLEM. Heesch’s tiling problem can, of course, be
posed for tiles in higher dimensional Euclidean space E
n and in spaces with alter-
nate geometries, such as n-dimensional hyperbolic space H
n and the n-dimensional
sphere Sn. Not only does the setting for Heesch’s tiling problem generalize, but so
does the problem itself. We brieﬂy summarize what is known in several different con-
texts:

• First, we note that any planar tile can be used to form a cylindrical tile with the same
Heesch number in E
3. This means that there are space tiles with Heesch numbers
0 through 5. We have identiﬁed nontiling space tiles that potentially have higher
Heesch numbers (as high as 8), but these tiles have deﬁed exhaustive computer
checks because of the vast number of combinatorial possibilities. In particular, if
a rhombic dodecahedron (Figure 9) is marked with conical bumps and nicks on its
faces so as to be combinatorially unbalanced, a simple counting argument reveals
that the maximum possible Heesch number is 8. However, it is unknown whether or
not eight coronas of such a tile can be realized.

Figure 9. A portion of a tessellation (two coronas) of E3 by the rhombic dodecahedron.

• For any hyperbolic regular polygon each of whose edges is marked with either a
bump or a nick, it is known whether or not the tile tessellates H
2; among those that
do not tessellate the hyperbolic plane, the highest Heesch number is 1 [13]. We have
also analyzed the slightly more general class of hyperbolic regular polygons where
only some of the edges are marked with bumps and nicks. Because of the nature of
the metric on H
2, the simple counting arguments that applied to tiles such as Am-
mann’s tile with Heesch number 3 become much more complicated. Nevertheless,
such an analysis has been performed with negative results in terms of large Heesch

4One may wonder if it is possible that larger and larger circular disks can be covered, yet a tessellation of
the entire plane still not be possible. Conveniently, a tessellation of the plane must exist under these conditions
(although this tessellation may not contain any of the ﬁnite patches postulated). This fact is called the Extension
Theorem [8, p. 151]. It can be also be demonstrated by an application of K¤onig’s lemma in this special case.

June–July 2004] HEESCH’S TILING PROBLEM 515

numbers [12]. To date, no tile with Heesch number greater than one has been identi-
ﬁed in H
2.

• Tiles on the sphere have not yet been studied systematically from a Heesch number
perspective. The only Heesch-number-related discovery in S
2 known to this author
is a 75
◦ equilateral triangle with Heesch number 3 (Figure 10) [2].

Figure 10. Dawson’s Heesch number 3 tile on the sphere. The ﬁgure at right is a 360◦ “ﬁsheye” view of
the partial tessellation of the sphere on the left. This projection inverts the coronas so that the center tile
corresponds to the exterior of the projection.

• While individual tiles in E
n that are marked with more bumps than nicks (or vice
versa) cannot tessellate space and must have ﬁnite Heesch number, there is no uni-
form upper bound on the Heesch numbers of such tiles, thus allowing for the possi-
bility that arbitrarily large Heesch numbers can be achieved using relatively simple
shapes. The idea here is that we can take a nice, regular shape in E
n (like the cube in
E
3, for example), glue together several copies of it, and mark the faces with bumps
and nicks in an unbalanced way. Then the geometry of the resulting tile is relatively
tame, so we might be able to form many coronas, but not inﬁnitely many. The more
unit shapes that are fused to create the tile, the greater the upper bound on the Heesch
number (based on the combinatorial imbalance alone) [12].

• We can consider other kinds of matching rules (other than bumps and nicks). For
example, we can color the edges of the tile and require that matching edges have
the same color. Or we can orient the edges and require that meeting edges have
the same orientation. One can even give the edges purely combinatorial matching
rules that aren’t geometrically realizable. Hexagons with multiple matching rules
have been studied to some extent. The author and a student have checked for their
Heesch numbers all hexagons with edges marked with bumps and nicks, colors, and
directions [19]. Our preliminary results ﬁnd no tiles with Heesch number greater
than three. Others have found high Heesch numbers for more general edge-matching
rules.

• Heesch’s tiling problem can be posed for protosets containing more than one pro-
totile and for a starting conﬁguration to be surrounded that comprises more than
one tile. In [8, p. 157] the authors conjecture the existence of a function f (n, m)
taking positive integer values and having the following property: if P is a protoset
of n prototiles such that every conﬁguration containing m tiles can be surrounded
at least f (n, m) times, then P admits a tessellation of the plane. Note that in the
case n = m = 1 this conjecture implies the existence of a maximal Heesch num-
ber (which implies the existence of a decision algorithm for the tiling problem for

516 c⃝ THE MATHEMATICAL ASSOCIATION OF AMERICA [Monthly 111

monotiles). Whether or not this conjecture is true is still open; however, in light of
the recent developments in ﬁnding tiles with higher and higher Heesch numbers, it
might not be unreasonable to conjecture in exactly the opposite way (i.e., that such
a function f (n, m) does not exist).

ACKNOWLEDGMENTS. The author would like to thank Chaim Goodman-Strauss for all of his help and
guidance, Robert Dawson for providing an image of his Heesch number 3 example, and George Martin and
the anonymous referees for their many helpful suggestions, corrections, and comments on improving the ex-
position and mathematics of the paper.

REFERENCES

1. R. Berger, The undecidability of the domino problem, Mem. Amer. Math. Soc. 66 (1966), 72 pp.
2. R. Dawson, Tilings of the sphere with isosceles triangles (to appear in Discrete Comput. Geom.).
3. D. Epstein, Heesch’s problem, The Geometry Junkyard, http://www.ics.uci.edu/˜eppstein/junkyard/
heesch/
4. A. Fontaine, An inﬁnite number of plane ﬁgures with heesch number two, J. Combin. Theory Ser. A 57
(1991) 151–156.
5. C. Goodman-Strauss, A small set of aperiodic tiles, European J. Combin. 20 (1999) 375–384.
6. , Open questions in tilings (manuscript).
7. G. Gr¤unbaum and G. Shephard, Some problems on plane tilings, in The Mathematical Gardner,D. A.
Klarner, ed., Wadsworth International, Belmont, CA, 1981, pp. 167–196.
8. , Tilings and Patterns, Freeman, New York, 1987.
9. H. Heesch, Regulares Parkettierungsproblem, Westdeutscher Verlag, Cologne, 1968.
10. W. Lietzmann, Lustiges und Merkwuerdiges von Zahlen und Formen, Hirt, Breslau, 1928.
11. , Visual Topology, American Elsevier, New York, 1955.
12. C. Mann, Heesch’s Problem and Other Tiling Problems, Ph.D. dissertation, University of Arkansas at
Fayetteville, 2001.
13. , Hyperbolic regular polygons with notched edges (in preparation).
14. W. Marshall, personal correspondence, January 2000.
15. R. Penrose, Pentaplexity, Math. Intelligencer 2 (1) (1979/80) 32–37.
16. R. Robinson, Undecidability and nonperiodicity of tilings of the plane, Invent. Math. 12 (1971) 177–209.
17. D. Schattschneider and M. Senechal, Tilings, in Handbook of Discrete and Computational Geometry,
J. Goodman and J. O’Rourke, eds., CRC Press, New York, 1997, pp. 43–62.
18. M. Senechal, Quasicrystals and Geometry, Cambridge University Press, Cambridge, 1995.
19. B. Thomas, Hexagon solutions to Heesch’s problem, UT-LSAMP Undergraduate Student Research Pro-
gram Presentation, University of Texas at Tyler, April 2003.
20. H. Wang, Dominoes and the AEA case of the decision problem, in Proc. Sympos. Math. Theory of
Automata (New York, 1962), Polytechnic Press of Polytechnic Inst. of Brooklyn, Brooklyn, NY, 1963,
pp. 23–55.

CASEY MANN earned his B.S. degree from East Central University in Ada, Oklahoma, in 1996 and his
Ph.D. degree from the University of Arkansas in 2001 under the direction of Chaim Goodman-Strauss. He
is currently an assistant professor of mathematics at the University of Texas at Tyler, as is his wife Jennifer
McLoud. His research interest is in tiling theory, making him a tiler in Tyler. He is also a proud 2002–2003
(forest dot) Project NExT fellow. In his free time, he enjoys getting soundly defeated in ping-pong by his
students and has a masochistic tendency to play golf.
University of Texas at Tyler, HPR 102, 3900 University Blvd., Tyler, TX 75799
cmann@uttyler.edu

June–July 2004] HEESCH’S TILING PROBLEM 517
