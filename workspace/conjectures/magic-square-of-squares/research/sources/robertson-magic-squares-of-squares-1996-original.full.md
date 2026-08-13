<!-- source: http://www.mathpages.com/home/kmath417.htm | converted from HTML -->

Magic Square of Squares

## Magic Square of Squares

```

For an updated version of this article, see [Magic Square of Squares][1].

It's an open question whether there exists a 3x3 magic square comprised
entirely of square integers.  Before considering the possibility of
such a square, it's worthwhile to review some basic facts about
arbitrary 3x3 magic squares, defined as an array of numbers

                    A B C
                    D E F
                    G H I

such that each row, column, and main diagonal has the same sum.
Letting S denote the common sum, we have the eight defining
conditions

       A+B+C=S    D+E+F=S    G+H+I=S    A+E+I=S
       A+D+G=S    B+E+H=S    C+F+I=S    C+E+G=S

Adding up the four conditions involving E, and re-arranging terms,
gives

      (A+B+C)  +  (D+E+F)  +  (G+H+I)  +   3E   =   4S

Since each quantity in parentheses equals S, this shows that 3E = S.
Substituting for S into the four basic equations involving E, we
have
               A+I = B+H = C+G = D+F  =  2E

If we subtract 2E from both sides of A+I=2E (for example) we get
(A-E) + (I-E) = 0, which shows that A-E = E-I, and likewise for the
other cases, proving that each row, column, and diagonal containing
E is an arithmetic progression.  If we define n = A-E and m = C-E,
the magic square contains the terms

                  E+n       E+m
                        E
                  E-m       E-n

From this the remaining terms follow, due to the requirement that
each row and column sum to 3E, so the entire magic square can be
expressed in terms of the three numbers E,m,n as shown below:

                  E+n   E-n-m   E+m
                 E-n+m    E    E+n-m                    (1)
                  E-m   E+n+m   E-n

Now, suppose we imagine a magic square comprised entirely of square
integers.  This implies the existence of integers E,m,n such that
the magic square given by (1) has the values

                  a^2   b^2   c^2
                  d^2   e^2   f^2
                  g^2   h^2   i^2

We will require these values to be distinct, and without loss of
generality we can divide out any common factor, so hereafter we assume
they have no common factor.  Equating the nine terms to their equivalents
in (1) gives the relations

         a^2 = E+n       b^2 = E-n-m      c^2 = E+m
         d^2 = E-n+m     e^2 = E          f^2 = E+n-m           (2)
         g^2 = E-m       h^2 = E+n+m      i^2 = E-n

Summing the pairs symmetrical about E, we have

    a^2 + i^2 = b^2 + h^2 = c^2 + g^2 = f^2 + d^2  =  2e^2       (3)

Furthermore, if we multiply the pairs symmetrical about E we find
that e^4 is expressible as a sum of two squares in the following four
ways
                    (ai)^2  +  n^2  =  e^4
                    (bh)^2 + (n+m)^2 = e^4
                    (cg)^2  +  m^2  =  e^4
                    (df)^2 + (n-m)^2 = e^4

These equations, along with (3), show that both e^4 and 2e^2 are
expressible as sums of two squares in four different ways.  In addition,
if we square both sides of the previous relation a^2 + i^2 = 2e^2 (for
example) we get

                 a^4 + 2(ai)^2 + i^4 = 4e^4

so we can solve this for (ai)^2 and substitute into the above
expression for e^4, and likewise for the other three expressions,
to give
                a^4  +  i^4   =   2[e^4  +  n^2  ]
                b^4  +  h^4   =   2[e^4 + (n+m)^2]
                c^4  +  g^4   =   2[e^4  +  m^2  ]
                d^4  +  f^4   =   2[e^4 + (n-m)^2]

This is a very strong set of conditions.  It requires a fourth power
(e^4) which, if increased by any one of four distinct squares, equals
half a sum of two fourth powers.  Furthermore, the roots of the four
distinct squares must be of the form n, m, n+m, and n-m.

We can also infer more Pythagorean relations by multiplying together
other pairs of relations from (2).  For example, if we multiply b^2
by f^2 and re-arrange the terms, and likewise for the other pairs,
we get
                 (bf)^2  +  n^2  =  (E-m)^2
                 (fh)^2  +  m^2  =  (E+n)^2
                 (hd)^2  +  n^2  =  (E+m)^2
                 (db)^2  +  m^2  =  (E-n)^2

Squaring both sides of the relation b^2 + f^2 = 2(E-m) and solving
for (bf)^2, we can substitute into the first of these equations, and
likewise for the other pairs, to give

                 b^4 + f^4 = 2[(e^2 - m)^2 + n^2]
                 f^4 + h^4 = 2[(e^2 + n)^2 + m^2]
                 h^4 + d^4 = 2[(e^2 + m)^2 + n^2]
                 d^4 + b^4 = 2[(e^2 - n)^2 + m^2]

Recall that we previously derived the conditions

                 b^4 + h^4 = 2[(e^2)^2 + (n+m)^2]
                 d^4 + f^4 = 2[(e^2)^2 + (n-m)^2]

so we have found that a necessary condition for a magic square of
squares is that there must be four 4th powers b^4, d^4, f^4, h^4
whose sums in pairs each equal twice a sum of squares.  This also
leads to relations such as

    f^4 - d^4 = 2(n-m)e^2        h^4 - b^4 = 2(n+m)e^2

However, all these relations just follow algebraically from the more
basic conditions, so to prove that no magic square of squares is
possible we should probably focus on the basic conditions.  Recall
that the relations (2) imply

            a^2 + i^2 = 2e^2       b^2 + f^2 = 2g^2
            b^2 + h^2 = 2e^2       f^2 + h^2 = 2a^2           (4)
            c^2 + g^2 = 2e^2       h^2 + d^2 = 2c^2
            d^2 + f^2 = 2e^2       d^2 + b^2 = 2i^2

The four equations on the left show that 2e^2 must be a sum of two
squares in four different ways, so e itself is a sum of squares in
(at least) two different ways.  The first non-trivial occurrence is
e = 65 = 5*13, because this is the smallest number that is the
product of distinct primes congruent to 1 (mod 4).  Each of the
factors, in turn, is necessarily a sum of two squares, i.e.,

             5 = 1^2 + 2^2      13 = 2^2 + 3^2

The two expressions for 65 arise from the two ways of multiplying
these according to the ancient formula

     (X^2 + Y^2)(A^2 + B^2) = (XB +- YA)^2 + (XA -+ YB)^2        (5)

Taking X=1, Y=2, A=2, B=3 we have

        e  =  65  =  (5)(13)   =   1^2 + 8^2   =   4^2 + 7^2

The four ways of expressing e^2 as a sum of two squares arise from
the four ways of multiplying these two forms using equation (5) (and
applying the factor 2 = 1^2 + 1^2, which doesn't change the number
of expressions).  Thus we have

 2(65)^2  =  2(1^2 + 8^2)(1^2 + 8^2)  =  47^2 + 79^2

          =  2(1^2 + 8^2)(4^2 + 7^2)  =  23^2 + 89^2  =  35^2 + 85^2

          =  2(4^2 + 7^2)(4^2 + 7^2)  =  13^2 + 91^2

We can assemble these squares into a square of squares such as

                   13^2   23^2   47^2
                   35^2   65^2   85^2
                   79^2   89^2   91^2

which has the required equal sums on all four of the lines through
the center square (the two main diagonals, the center row, and the
center column).  Notice, however, that the outer rows and columns do
not give the required sum.  In general, we can show that

PROPOSITION 1:  Any square whose elements satisfy the central sums
                and whose central number is expressible as a sum of
                two squares in no more than four distinct ways will
                NOT give the required sums for the outer rows and
                columns.

This proposition doesn't completely rule out the existence of a magic
square of squares, because it doesn't cover possible squares whose
central numbers are expressible as a sum of two squares in MORE than
four distinct ways.  However, it does show that the root of the
central number of any magic square of squares would have to be the
product of more than two distinct primes of the form 4k+1.

To prove this proposition, note that the above conditions can be
expressed parametrically in terms of X,Y,A,B (which had the values
1,2,2,3 in the above example).  If we define

               u = YA - XB        r = YB - XA
               v = YB + XA        s = YA + XB

then we have squares such as

          (2uv-uu+vv)^2     (ur+vs+vr-us)^2     (2rs+rr-ss)^2

          (us+vr-vs+ur)^2      (uu+vv)^2       (us+vr+vs-ur)^2

          (2rs-rr+ss)^2      (ur+vs-vr+us)^2    (2uv+uu-vv)^2

which automatically has equal sums on the diagonals and the central
row and column.  The common sum along each of these lines is

   S = 3(u^2 + v^2) = 3(r^2 + s^2) = 3[(A^2 + B^2)(X^2 + Y^2)]^2

Any magic square of squares whose central element is a sum of two
squares in no more than four ways must consist of some arrangement
of the four pairs of opposite terms shown in the square above, but
they need not be arranged as shown above.  It's convenient to refer
to each of the outer elements by the negative term it contains.  For
example, we will let US denote the quantity (ur+vs+vr-us)^2, and we
will let RR denote (2rs-rr+ss)^2, and so on.  Thus we have the four
pairs of opposite squares (UU,VV), (RR,SS), (US,VR), and (UR,VS).

We note that the system is symmetrical under exchange of (u,v) with
(r,s), and we consider first the possibility that UU is in the same
row or column with two of the "crossed" elements.  In order for the
square to be magic the sum of these three quantities must equal the
common sum S given above.  However, if we examine all six of these
case we find that

           UU+VR+VS-S =  8XY(A+B)(A-B)(v+u)(v-u)
           UU+VR+US-S =  4vu(v+u)(v-u)
           UU+VR+UR-S =  32ABXYuv
           UU+VS+US-S =  8uv(A+B)(A-B)(X+Y)(X-Y)
           UU+VS+UR-S =  4vu(v+u)(v-u)
           UU+US+UR-S = -8AB(X+Y)(X-Y)(v+u)(v-u)

In order for the terms of the overall square to be distinct, the
values of u,v,r,s must all be non-zero, and the quantities u^2 - v^2
and r^2 - s^2 must also be non-zero.  Furthermore, each of the
quantities A,B,X,Y must be non-zero, as must be the quantities
A^2 - B^2 and X^2 - Y^2.  These last two condition are due to the
fact that if X=Y, for example, we have u=X(A-B), v=X(A+B), r=X(B-A),
and s=X(A+B), which implies v=s and u=-r.  Inserting these expressions
for v and u into ur+vs+us-vr gives -r^2 + s^2 - 2rs, so we have VR=SS.
It follows from all these conditions that none of the six quantities
shown above can equal zero, so no arrangement with any of those
combinations of terms in any row or column can be a magic square
of squares.  Of course, this also rules out any squares with rows or
columns containing SS with any two of the cross terms, since those
appear on the opposite side of the above squares.

It remains to consider the possibility of a magic square with each
of the outer rows and columns containing two "pure" terms (i.e.,
UU, VV, RR, SS) and one cross term.  This implies that the pure
terms must be at the four corners.  Therefore, one of the rows or
columns will be [UU  *  RR] where "*" denotes one of the four
cross terms.  Two of these cases can be ruled out immediately,
because we have

   UU+VS+RR-S = 4XY(X+Y)(X-Y)(3A^2 - B^2)(A^2 - 3B^2)
   UU+UR+RR-S = 4XY(X+Y)(X-Y)(A^2 + 4AB + B^2)(A^2- 4AB + B^2)

The first is impossible because a non-zero square cannot be 3 times
a square, and the second is impossible because it implies

                  A = +-2B[2+-sqrt(3)]

The only two remaining cases are [UU VR RR] and [UU US RR], each of
which corresponds to either of the two squares (because we can
transpose the placement of the remaining pair of terms).  To prove
that these are impossible, we can make use of the right-hand relations
in (4), which state that the double of each corner equals the sum of
the middle terms of the two opposite sides.  This leads us to examine
the sums shown below for the indicated square

 UU VR RR
 VS    UR   VR+UR-2SS = 4(s+r)(s-r)[3AB(Y^2 - X^2) + XY(B^2 - A^2)]
 SS US VV   UR+US-2UU = 4(v+u)(v-u)[3XY(B^2 - A^2) - AB(Y^2 - X^2)]

In order for this to be a magic square, both of the indicated sums
must vanish, which (for distinct terms) requires the trailing factors
to vanish.  But these are of the form 3m+n=0 and 3n-m=0 and therefore
m=n=0, which is to say AB(Y^2 - X^2) = XY(B^2 - A^2) = 0.  This is
impossible for distinct terms.

The three remaining cases can be ruled out similarly, based on the
sums shown below:

 UU VR RR
 UR    VS   VR+VS-2SS = 4rs[3(A^2 - B^2)(Y^2 - X^2) + 4 ABXY]
 SS US VV   VS+US-2UU = 4uv[(A^2 - B^2)(Y^2 - X^2) - 12 ABXY]

 UU US RR
 VS    UR   US+UR-2SS = 4rs[(A^2 - B^2)(Y^2 - X^2) + 12 ABXY]
 SS VR VV   UR+VR-2UU = 4uv[3(A^2 - B^2)(Y^2 - X^2) - 4 ABXY]

 UU US RR
 UR    VS   US+VS-2SS = 4(s+r)(s-r)[AB(Y^2 - X^2) + 3XY(B^2 - A^2)]
 SS VR VV   VS+VR-2UU = 4(v+u)(v-u)[3AB(X^2 - Y^2) + XY(B^2 - A^2)]

This completes the proof.  So, what has been shown here is that if
the central number 2e^2 is expressible as a sum of two squares in
just four distinct ways (which is the minimum number necessary to
satisfy the diagonal and center row and column conditions), then
it's impossible to satisfy the outer row and column conditions.  Of
course, every array will be based on just four partitions of 2e^2
into two squares, but those partitions won't all necessarily come
from the same factorization of e, so those cases aren't covered by
the above argument.

For more on the search for a magic square of squares, see the notes
[Orthomagic Square of Squares][2]
[Automedian Triangles and Magic Squares][3]
[Discordance Impedes Square Magic][4]
```

---

[Return to MathPages Main Menu][5]

---


## Links

[1]: kmath417/kmath417.htm
[2]: kmath427/kmath427.htm
[3]: kmath429/kmath429.htm
[4]: kmath511/kmath511.htm
[5]: index.htm
