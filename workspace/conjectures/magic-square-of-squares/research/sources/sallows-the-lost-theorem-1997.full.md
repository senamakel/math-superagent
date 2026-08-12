<!-- source: http://www.multimagie.com/Sallows.pdf | converted from PDF -->

The Lost Theorem

 Lee Sallows

  "Almost the last word has been said on this subject"
  ⎯ H. E. Dudeney on magic squares [1]

A magic square, as all the world knows, is a square array of numbers whose sum in any row,
column, or main diagonal is the same. So-called "normal" squares are ones in which the numbers
used are 1,2,3, and so on, but other numbers may be used. Squares using repeated entries are
deemed trivial. We say that a square of  size N × N is of order N. Clearly, magic squares of order-
1 lack glamour, while a moment's thought shows that a square of order 2 cannot be realized using
distinct entries. The smallest magic squares of any interest are thus of order-3.

Writing in Quantum recently [2], Martin Gardner offered $100 to anyone able to produce a 3×3
magic square composed of any nine distinct square numbers. So far nobody has produced a
solution, or proof of its impossibility, although a near miss I discovered is the following:

 222
 222
 222
 978274
 941132
 5846127

a specimen whose rows, columns, and just one of the two main diagonals sum to the same
number, itself a square: 1472. It was while tinkering in connection with this problem that I was
startled to discover an elementary correspondence between 3×3 magic squares and
parallelograms. The reason for my surprise is worth explaining.

Magic squares have been a special hobby of mine for over twenty years; the literature on the
topic, much of which I have collected, is extensive. As already noted, 3×3 magic squares are the
smallest and hence simplest types, for which reason they are the earliest to appear in history, as
well as being the most thoroughly investigated squares of all. Innumerable books and articles on
magic squares begin with a discussion of 3×3 types, the properties of which have long been
regarded as completely understood. Writing in the well known  Mathematical Recreations
published in 1930, for instance, Maurice Kraitchik begins by saying that, "The theory of the
squares of the third order is simple and complete ..", and then goes on to present that theory in
just two pages of text.

Yet for all its extreme simplicity, the elementary correspondence with parallelograms that I had
stumbled upon while working on Gardner's problem, has, to the best of my knowledge, never
previously been identified. I feel sure that many readers will share my incredulity on inspecting
the theorem below. They may agree with me that the correlation with parallelograms it describes
is so basic that it deserves to be regarded as the fundamental theorem of order-3 magic squares,

  1

and the very first thing that any newcomer to the subject should learn. How then could such a
theorem escape the attention of every researcher in the field from ancient times down to the
present day?

An explanation lies in the orthodox focus on magic squares using natural numbers. Once our
attention broadens to include squares that use  complex numbers, the familiar integer types
become only a special case, preoccupation with which has obscured the wider picture. Moving
beyond this narrow view, we step into a realm of greater clarity and harmony. And at the very
center of that realm we shall find an undiscovered prize, the atomic magic square.

Standard Theory

What makes a 3×3 square magic?
The well-known algebraic formula due to Édouard Lucas describes the structure of every magic
square of order-3:

 bcbacac
 baccbac
 acbacbc
 +−−+
 −++−
 −++−

Lucas’s formula conveys much of the essential information in a single swoop. In particular, we
can see at a glance that the constant total, which is 3c, is equal to three times the center number,
while a closer look shows that whatever the nine numbers used in the square, they must always
include eight 3-term arithmetic progressions, namely:

1 : c+a, c, c-a,
2 : c+b, c, c-b,
3 : c+a+b, c, c-a-b,
4 : c+a-b, c, c-a+b,
5 : c+a-b, c+a , c+a+b
6 : c-a+b, c-a, c-a-b,
7 : c+a+b, c+b, c-a+b,
8 : c+a-b, c-b, c-a-b,

The identification of these arithmetic triads is  a recurrent feature in discussions of order-3
theory, a point we shall return to later, although it is rare to find an explicit list of all eight.

Of course, just as any magic square can be rotated and reflected to result in 8 trivially distinct
squares that are deemed equivalent, so there are 8 trivially distinct rotations and reflections of the
formula, all of them isomorphic to each other, and again comprising one equivalence class.

So much for a bird's eye view of the theory of order 3 magic squares as it is met within the
literature. Let us now turn our attention elsewhere.

  2

Complex Squares.

Consider Figure 1, which depicts an arbitrary parallellogram, PQRS, centered at some arbitrary
point, M, on the Euclidean plane, with axes  X  and Y. Point O is the origin of the plane. The
corner points, P, Q, R, and S, together with T, U, V , and W, the midpoints of the sides of the
parallelogram, as well as the center, M, can thus each be identified with vectors or complex
numbers of form x + yi, in which x and y are the real number coordinates of each point, and i =
1− .

                               Figure 1

Equally, the lines connecting these points m ay themselves be interpreted as vectors, three of
which are identified in the Figure as: MT  = a,  MU = b, and OM  = c. Note that given any three
particular complex values for  a,  b and  c, we could im mediately proceed to construct the
corresponding  parallelogram.

Now by the law for the addition of vectors, the point or com plex num ber, T (which is the vector
OT), is the resultant of  the two vectors c and a, or c + a. And likewise, it takes but a glance to
identify the rem aining points on PQRS in terms of the vectors, a, b, and c, as indicated in the
Figure:  P = c + a - b, Q = c + a + b, R = c - a + b, S = c - a - b, U  = c + b, V = c - a, W = c - b.
and M = c.
Looking next at the 3 ×3 square shown below left in Figure 1, observe what happens when a new
square is created by replacing P,Q,.. with their corresponding expressions in terms of a, b and c:

  3
 bcbacac
 baccbac
 acbacbc
 +−−+
 −++−
 −++−

The outcom e is nothing less than a reappearance of Lucas's formula for 3×3 magic squares.

The im plication is as obvious as it is surprising: given any particular parallelogram on the
Euclidean plane, and then transcribing the com plex num bers corresponding to its four
corners, four edge midpoints, and center, into a 3×3 matrix, in the same way as above, the
resulting square will always  be magic. Or alternatively, starting with any 3×3 magic square
that uses complex num ber entries, we will find that they define nine points on the Euclidean
plane that coincide with the four corners, four edge midpoints, and center of a parallelogram

In summary, we have:

Theorem . To every parallelogram drawn on the plane  there corresponds a unique equivalence
class of 8 complex 3 ×3 magic squares, and for every equivalence class of 8 complex 3 ×3 magic
squares there corresponds a unique parallellogram on the plane .

Or in a nutshell: rotations and reflections disregarded, every parallelogram defines a unique 3×3
magic square, and vice versa.

In this light it is interesting to recall the eight arithmetic progressions previously identified  in
every 3×3 magic square. For just as arithmetic progressions of real numbers correspond to
equidistant points along the real number line, so arithmetic progressions of complex num bers
correspond to equidistant colinear  points on the plane. See then how the eight progressions listed
earlier precisely correlate with the eight sets of 3 colinear points lying along the four edges and
four bisectors of the parallelogram in Figure 1:
  1 :  c+a, c, c-a = T,M,V
2 : c+b, c, c-b = U,M,W
3 : c+a+b, c, c-a-b = Q,M,S
4 : c+a-b, c, c-a+b = P,M,R
5 : c+a-b, c+a, c+a+b = P,T,Q
6 : c-a+b, c-a, c-a-b = R,V,S
7 : c+a+b, c+b, c-a+b = Q,U,R
8 : c+a-b, c-b, c-a-b = P,W,S.

 In the magic square literature to date, discussion of theory never gets further than identifying
these progressions; now at last we can s ee how the geom etry of the parallellogram explains  their
presence.

  4

From our new perspective we can see also how the corellation with parallelograms has escaped
previous notice. Traditionally magic squares have used integers, which are entries without
imaginary component. The parallelograms corresponding to these squares are thus collapsed or
degenerate  specimens of zero area, m aking their presen ce undetectable. In fact, a closer look at
one such parallelogram will prove instructive, as well as preparing us for an unexpected
developm ent: the discovery of a lost archetype, the primordial magic square.

A Flaw in the Crystal

I suppose that, until now, the most obvious candidate for the title of archetypal magic square
would have been the Chinese Lo shu, the simplest, oldest, and most well known square of all. Its
magic sum is 15:
 816
 357
 492

Legend has it that the Lo shu was first espied by King Yü on the back of a sacred turtle that
emerged from the river Lo in the 23rd century BC. In fact, historical references to the square date
from the 4th century BC, while Cammann has argued that it played a major part in Chinese
philosophical and religious thought for centuries afterward [3]. In the West, the Lo shu has long
been held up as a paradigm, or "one of the most elegant patterns in the history of combinatorial
number theory," as Martin Gardner has written. Nevertheless, taking a lens to this ancient gem,
we can discover an interesting irregularity in its crystal lattice.

Consider the Lo shu's flattened parallelogram, which is that segment of the real number line
between 1 and 9, along which lie its four corners, four edge midpoints, and center, occupying
nine equidistant points. Recalling Figure 1, the relation between these points and their position in
the magic square can be diagrammed as follows:

         3   6   9               2   9   4
      2   5   8        ⇔      7   5   3
   1   4   7                     6   1   8
     Parallelogram           Magic Square

The distance between the parallelogram's corners at points 1 and 3 (or 7 and 9 ) is thus 2 units,
while the distance between those at points 3 and 9 (or 1 and 7) is 6 units; a ratio in side lengths of
1:3. The remarkable fact is thus that the Lo shu parallelogram is not equilateral, which is a bit
disappointing for a pattern whose famous symmetry has won acclaim down the ages, from the
banks of the river Lo to the pages of Scientific American.  It is beginning to look as if that turtle
was not quite as sacred as King Yü had imagined.

However, as a prisoner in Flatland, the  Lo shu is doomed to this imbalance: squash any
equilateral parallelogram, and two pairs of edge midpoints and two corners will coincide, forcing
repeated entries in the associated magic square. In other words, unless it is trivial, an
asymmetrical parallelogram must accompany every non-complex magic square, the one on the
(mock?) turtle included.

Where then is the magic square with the symmetrical parallelogram that King Yü was denied?

  5

The Atomic Square

Of course, the most sym metrical case of all is an equilateral parallelogram that is equiangular as
well: the square .

A ma gic square whose associated parallelogram is again a square; the idea is at once compelling.
But what kind of a m agic square would that be?  To find out, all we have to do is draw a square
on the plane, read off the complex values of its f our corners, etc, and then write these into a 3×3
matrix in the usual way. Sim plest of all is this canonical or atomic case:

It is a square centered on the origin of the plane, such that its four corners and four edge
midpoints coincide with the 8 com plex integers immediately surrounding the origin. The magic
square corresponding to this geometric square is consequently an atomic paradigm of its kind
too: it is the smallest, most perfectly sym metrical magic square, composed of the nine sm allest
gaussian integers:
 ii
 ii
 ii
 −−
 −+−
 −+−
 11
 101
 11

The elegance of this flawless prism  is beyond com pare.  The two main diagonals and two central
orthogonals are like four balanced beam s pivoted on the center number, the integer at the end of
each beam offset by its opposing negative im age, an equipoise reflected in the magic sum of
zero. Rewriting the square in the form  of vectors as ordered pairs, [a,b], its structural harmony
reappears in the shape of palindromic rows and antipalindromic columns, a quality that is better
highlighted when 1  replaces −1, and the commas and brackets are discarded:

  6
 011110 110011 011110

Analysing the square in terms of Lucas's formula, we find that the variables a and b have here
taken on the values of 1 and i, the real and imaginary forms of unity, while c is equal to zero.
Could anything be more natural, or poetic?

My interest in magic squares began a couple of decades ago when I first encountered the Lo shu.
 I recall my delight in exploring its symmetries, but I also recall my disquiet in detecting a
strange lopsidedness. In Lucas's formula, the variables a and b appear in two patterns that are
perfect mirror images. In the Lo shu, however, a = 1, while b = 3, a numerical imbalance that
clashed with the symmetry of the patterns. Attempts to construct a square in which a = b, or a =
−b, wouldn't work either, because the result is then trivial. Yet a craving for symmetry is what
makes the mathemagical mind tick. Down the years this unease has continued to quietly
smoulder, until recent events brought the parallelogram theorem to light, and with it a sudden
resolution of the mystery in the shape of the atomic square, whose symmetry is without flaw. It is
a relief; I look forward to sleeping at nights once again.
  *     *     *     *     *

The above article appeared in The Mathematical Intelligencer Vol 19, No. 4, pp 51-4, 1997.

References

[1] H.E. Dudeney, Amusement in Mathematics, p. 119
[2] M. Gardner, The Magic of 3×3, Quantum, January/February 1996, pp. 24-6
[3] S. Cammann, The Magic Square of Three in Old Chinese Philosophy and Religion,
     History of Religions I (1961), pp. 37-80

  7
