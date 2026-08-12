<!-- source: https://www.mathpages.com/home/kmath417/kmath417.htm | converted from HTML -->

**Magic Square of Squares**

 |

 |

It's an open question whether there exists a 3x3 magic square comprised entirely of square integers. Before considering the possibility of such a square, it's worthwhile to review some basic facts about arbitrary 3x3 magic squares, defined as an array of numbers

 |

 |

 |

 |

such that each row, column, and main diagonal has the same sum. Letting S denote the common sum, we have the eight defining conditions

 |

 |

 |

 |

Adding up the four conditions involving E, and re-arranging terms, gives

 |

 |

 |

 |

Since each quantity in parentheses equals S, this shows that 3E = S. Substituting for S into the four basic equations involving E, we have

 |

 |

 |

 |

If we subtract 2E from both sides of A+I = 2E (for example) we get (A−E) + (I−E) = 0, which shows that A−E = E−I, and likewise for the other cases, proving that each row, column, and diagonal containing E is an arithmetic progression. If we define n = A−E and m = C−E, the magic square contains the terms

 |

 |

 |

 |

From this the remaining terms follow, due to the requirement that each row and column sum to 3E, so the entire magic square can be expressed in terms of the three numbers E,m,n as shown below:

 |

 |

 |

 |

Now, suppose we imagine a magic square comprised entirely of square integers. This implies the existence of integers E,m,n such that the magic square given by (1) has the values

 |

 |

 |

 |

We will require these values to be distinct, and without loss of generality we can divide out any common factor, so hereafter we assume they have no common factor. Equating the nine terms of the square of squares to their equivalents in (1) gives the relations

 |

 |

 |

 |

Summing the pairs symmetrical about E, we have

 |

 |

 |

 |

From this we can infer that no two elements of any set of three numbers on a line through the center can share any common prime factor of the form 4k−1, because any such prime would have to divide all three numbers, and therefore all the numbers in the square. (This relies on the fact that x 2 + y 2 = 0 has no solutions modulo any prime p = 4k−1 other than x = y = 0.)

 |

 |

Furthermore, if we multiply the pairs symmetrical about E we find that e 4 is expressible as a sum of two squares in the following four ways

 |

 |

 |

 |

These equations, along with (3), show that both e 4 and 2e 2 are expressible as sums of two squares in four different ways. In addition, if we square both sides of the previous relation a 2 + i 2 = 2e 2 (for example) we get

 |

 |

 |

 |

so we can solve this for (ai) 2 and substitute into the above expression for e 4, and likewise for the other three expressions, to give

 |

 |

 |

 |

This is a very strong set of conditions. It requires a fourth power (e 4) which, if increased by any one of four distinct squares, equals half a sum of two fourth powers. Furthermore, the roots of the four distinct squares must be of the form n, m, n+m, and n−m.

 |

 |

We can also infer more Pythagorean relations by multiplying together other pairs of relations from (2). For example, if we multiply b 2 by f 2 and re-arrange the terms, and likewise for the other pairs, we get

 |

 |

 |

 |

Squaring both sides of the relation b 2 + f 2 = 2(E−m) and solving for (bf) 2, we can substitute into the first of these equations, and likewise for the other pairs, to give

 |

 |

 |

 |

Recall that we previously derived the conditions

 |

 |

 |

 |

so we have found that a necessary condition for a magic square of squares is that there must be four 4th powers b 4, d 4, f 4, h 4 whose sums in pairs each equal twice a sum of squares. This also leads to relations such as

 |

 |

 |

 |

However, all these relations just follow algebraically from the more basic conditions, so to prove that no magic square of squares is possible we should probably focus on the basic conditions. Recall that the relations (2) imply

 |

 |

 |

 |

The four equations on the left show that 2e 2 must be a sum of two squares in four different ways, so e itself is a sum of squares in (at least) two different ways. The first non-trivial occurrence is e = 65 = (5)(13), because this is the smallest number that is the product of distinct primes congruent to 1 (mod 4). Each of the factors, in turn, is necessarily a sum of two squares, i.e.,

 |

 |

 |

 |

The two expressions for 65 arise from the two ways of multiplying these according to the ancient formula

 |

 |

 |

 |

Taking X=1, Y=2, A=2, B=3 we have

 |

 |

 |

 |

The four ways of expressing e 2 as a sum of two squares arise from the four ways of multiplying these two forms using equation (5) (and applying the factor 2 = 1 2 + 1 2, which doesn't change the number of expressions). Thus we have

 |

 |

 |

 |

We can assemble these squares into a square of squares such as

 |

 |

 |

 |

which has the required equal sums on all four of the lines through the center square (the two main diagonals, the center row, and the center column). Notice, however, that the outer rows and columns do not give the required sum. In general, we can show that

 |

 |

PROPOSITION 1:� Any square whose elements satisfy the central sums and whose central number is expressible as a sum of two squares in no more than four distinct ways will *not*give the required sums for the outer rows and columns.

 |

 |

This proposition doesn't completely rule out the existence of a magic square of squares, because it doesn't cover possible squares whose central numbers are expressible as a sum of two squares in *more*than four distinct ways. However, it does show that the root of the central number of any magic square of squares would have to be the product of more than two distinct primes of the form 4k+1.

 |

 |

To prove this proposition, note that the above conditions can be expressed parametrically in terms of X,Y,A,B (which had the values 1,2,2,3 in the above example). If we define

 |

 |

 |

 |

then we have squares such as

 |

 |

 |

 |

which automatically has equal sums on the diagonals and the central row and column. The common sum along each of these lines is

 |

 |

 |

 |

Any magic square of squares whose central element is a sum of two squares in no more than four ways must consist of some arrangement of the four pairs of opposite terms shown in the square above, but they need not be arranged as shown above. It's convenient to refer to each of the outer elements by the negative term it contains. For example, we will let US denote the quantity (ur+vs+vr−us) 2, and we will let RR denote (2rs−r 2 +s 2) 2, and so on. Thus we have the four pairs of opposite squares (UU,VV), (RR,SS), (US,VR), and (UR,VS).

 |

 |

We note that the system is symmetrical under exchange of (u,v) with (r,s), and we consider first the possibility that UU is in the same row or column with two of the "crossed" elements. In order for the square to be magic the sum of these three quantities must equal the common sum S given above. However, if we examine all six of these case we find that

 |

 |

 |

 |

In order for the terms of the overall square to be distinct, the values of u,v,r,s must all be non-zero, and the quantities u 2 − v 2 and r 2 − s 2 must also be non-zero. Furthermore, each of the quantities A,B,X,Y must be non-zero, as must be the quantities A 2 − B 2 and X 2 − Y 2. These last two condition are due to the fact that if X = Y, for example, we have u = X(A−B), v = X(A+B), r = X(B−A), and s = X(A+B), which implies v = s and u = −r. Inserting these expressions for v and u into ur+vs+us−vr gives −r 2 + s 2 − 2rs, so we have VR=SS. It follows from all these conditions that none of the six quantities shown above can equal zero, so no arrangement with any of those combinations of terms in any row or column can be a magic square of squares. Of course, this also rules out any squares with rows or columns containing SS with any two of the cross terms, since those appear on the opposite side of the above squares.

 |

 |

It remains to consider the possibility of a magic square with each of the outer rows and columns containing two "pure" terms (i.e., UU, VV, RR, SS) and one cross term. This implies that the pure terms must be at the four corners. Therefore, one of the rows or columns will be [UU� *� RR] where "*" denotes one of the four cross terms. Two of these cases can be ruled out immediately, because we have

 |

 |

 |

 |

The first is impossible because a non-zero square cannot be 3 times a square, and the second is impossible because it implies A = �2B(2 � √3).

 |

 |

The only two remaining cases are [UU VR RR] and [UU US RR], each of which corresponds to either of the two squares (because we can transpose the placement of the remaining pair of terms). To prove that these are impossible, we can make use of the right-hand relations in (4), which state that the double of each corner equals the sum of the middle terms of the two opposite sides. This leads us to examine the sums shown below for the indicated square

 |

 |

 |

 |

In order for this to be a magic square, both of the indicated sums must vanish, which (for distinct terms) requires the trailing factors to vanish. But these are of the form 3m + n = 0 and 3n − m = 0 and therefore m = n = 0, which is to say AB(Y 2 − X 2) = XY(B 2 − A 2) = 0. This is impossible for distinct terms.

 |

 |

The three remaining cases can be ruled out similarly, based on the sums shown below:

 |

 |

 |

 |

 |

 |

 |

 |

 |

This completes the proof. So, what has been shown here is that if the central number 2e 2 is expressible as a sum of two squares in just four distinct ways (which is the minimum number necessary to satisfy the diagonal and center row and column conditions), then it's impossible to satisfy the outer row and column conditions. Of course, every array will be based on just four partitions of 2e 2 into two squares, but those partitions won't all necessarily come from the same factorization of e, so those cases aren't covered by the above argument.

 |

 |

For more on the search for a magic square of squares, see the notes

 |

 |

[Orthomagic Square of Squares][1]

 |

[Automedian Triangles and Magic Squares][2]

 |

[Discordance Impedes Square Magic][3]

 |

[No Progression of Four Rectangles On A Conic?][4]

 |

 |

[Return to MathPages Main Menu][5]

 |


## Links

[1]: ../kmath427.htm
[2]: ../kmath429.htm
[3]: ../kmath511.htm
[4]: ../kmath512/kmath512.htm
[5]: ../index.htm
