<!-- source: https://mathpages.com/home/kmath427/kmath427.htm | converted from HTML -->

Kevin 2 0 2020-04-26T23:21:00Z 2020-04-26T23:21:00Z 1 1424 8120 67 19 9525 15.00 false false false false EN-US X-NONE X-NONE MicrosoftInternetExplorer4

**Orthomagic Square of Squares**

 |

 |

It's not known if there exists a 3x3 magic square of squares, i.e., a 3x3 arrangement of nine distinct integer squares such that the sum of each row, column, and main diagonal is the same. In another section we discussed one approach to this problem, namely, to determine the form of all 3x3 arrangements of squares that satisfy the four sums involving the central number, and then see if any of those arrangements can be made to also satisfy the four outer sums. In this way it was shown that no solution is possible if the central square is expressible as a sum of two squares in only four ways (which is the simplest non-trivial case). It may be possible to extend that method to the general case, but I wonder if another approach might be more effective.

 |

 |

Instead of looking at the 3x3 arrangements that satisfy the four sums involving the central number, suppose we consider the arrangements that satisfy the six orthogonal sums, i.e., the sums of the rows and columns. If these "orthomagic squares" of squares could be completely characterized, it might be possible to show that they can never satisfy the sums on the two main diagonals, thereby proving the impossibility of a 3x3 magic square of squares. (Of course, if this can't be shown, this approach may help to construct an example.)

 |

 |

Remarkably, it turns out that most orthomagic squares of squares also possess another property: the common sum of the rows and columns is a square! For example, the smallest orthomagic arrangement of distinct squares is

 |

 |

 |

 |

and each rows and column of this arrangement sums to 3249 = 57 2. The same is true for the next several OMSOS's. In any case, this is nice because we know the common sum of a completely magic arrangement of squares must be of the form 3E 2 where E 2 is the central square. Therefore, since a square can't be 3 times a square, we can immediately rule out all orthomagic arrangements whose common sum is a square.

 |

 |

Of the twelve smallest OMSOS's, nine of them have a square common sum, so this just leaves three possibilities, and those can also be ruled out individually. Interestingly, the smallest OMSOS that does *not*have a square common sum happens to be unique in another sense, namely, all the entries are squared primes:

 |

 |

 |

 |

The common sum of the rows and columns is 5691 = (3)(7)(271). Obviously we can permute the rows and columns of an OMSOS without affecting the sums, but since (3)(7)(271) is not 3 times a square, we know this can't be permuted into a fully magic square. Still, this is an interesting square in its own right. The next two "all-prime" OMSOS's (after the one noted above) are based on the matrices

 |

 |

 |

 |

It's also interesting that the next two "exceptional" OMSOS's (meaning those whose common sum is *not*a square) also have common sums of the form (3)(7)(p) where p is a prime congruent to 1 (mod 6).

 |

 |

Even though the OMSOS's with square common sums are immediately excluded from being completely magic, they are interesting in their own right, and it's worthwhile to consider why the condition of equal sums for the row and columns predisposes the common sum to be a square (when the elements themselves are squares). First, notice that they seem to occur in infinite families, and it's not too hard to figure out parametric representations for some of them. For example, there's an infinite family containing "(1) 2 ":

 |

 |

 |

 |

with the common sum (9+16k+10k 2) 2. (Of course there are a few values of k for which the elements of this array are not distinct, so I exclude those from the set of orthomagic squares. Note also that k can be positive or negative, because all the results are squared anyway.) Similarly an infinite family containing (2) 2 is given by

 |

 |

 |

 |

with the common sum (15+14k+5k 2) 2. We can give a similar infinite 1-parameter family containing (n) 2 for any given n, so there ought to be a 2-parameter representation covering all of these. Ideally we'd like to find a complete characterization of all OMSOS's, or at least the possible common sums, to see if complete magicality can be ruled out.

 |

 |

The class of orthomagic squares whose "common sum" is a square is closely related to quaternions, spatial rotation matrices, and representations of numbers as sums of *four*squares. This is an observation that essentially goes back to Euler (see Dickson's History). Specifically, for any numbers a,b,c,d we can construct a 3x3 matrix

 |

 |

 |

 |

Each row and column, regarded as a 3D vector, has the magnitude

 |

 |

 |

 |

so obviously if we construct a 3x3 square whose components are the squares of the components of the above matrix, it will be an "orthomagic square of squares" with the common sum L 2. This accounts for the frequent occurrence of OMSOS's with a square common sum. For example, with a=1, b=2, c=4, d=6 we have the basic matrix

 |

 |

 |

 |

and if we square each number this is the smallest orthomagic square of squares, with the common sum 3249 = 57 2. The determinant is 57 3. Note that the three row vectors constitute an orthogonal triad, as do the three column vectors, and if we normalize each term by dividing it by the magnitude L=57 the above matrix is the rotation operator representing the space rotation relating the row triad to the column triad.

 |

 |

Obviously the product of two such base squares gives another base square. For example, we have the product

 |

 |

 |

 |

The second factor on the left side is given by setting a=1, b=3, c=5, and d=6, it's determinant is 71 3, and the common sum of squares of its rows and columns is 71 2. The matrix product is also a base square, i.e., the squares of its elements form an orthogonal orthomagic square of squares, with the common sum (57∙71) 2 and the base square has determinant (57∙71) 3. It is produced by setting a = �61, b = �1, c = 15, d = 10, which can be inferred from the four-square multiplication formula

 |

 |

 |

 |

where

 |

 |

 |

The above is an interesting example of how, when trying to work in three parameters (or dimensions), it often seems that we're led to a much more natural formulation by going to four. I had been looking at sums of *three*squares, noting that the most general solution (according to Dickson) of the equation X 2 + Y 2 + Z 2 = N 2 is of the form

 |

 |

 |

 |

In retrospect it's clear that there's a 4-parameter family hidden behind this, trying to get out. Indeed, it was derived from Euler's four-square product formula, suppressing one of the parameters.

 |

 |

Incidentally, the quaternionic formulas noted above are very similar to the generalized Heron's formula, relating the volume of a "perfect tetrahedron" in terms of the areas of its faces, as discussed in �Heron's Formula For Tetrahedrons�.

 |

 |

The OMSOS's with square common sum seem to be well covered by the above parameterization, although I'm not quite sure it necessarily includes ALL OMSOS's with square sum. Another interesting question is whether the OMSOS's that *don't*have a square sum are also given by the 4-parameter matrix above, with non-integer values of a,b,c,d. In other words, are there any sets of numbers a,b,c,d such that the nine elements of the basic matrix are integers but the magnitude of the row and column vectors is not an integer?

 |

 |

There are 91 primitive orthomagic squares of squares with common sums less than 30000. Of those, 56 have a square common sum, whereas the remaining 35 do not. Of the 35 non-square cases, none of them is of the form 3k 2, so they clearly can't give a complete magic square of squares. For more on the search for a magic square of squares, see the note Automedian Triangles and Magic Squares.

 |

 |

[Return to MathPages Main Menu][1]

 |


## Links

[1]: ../index.htm
