> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/brown-mathpages-orthomagic-square-of-squares.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

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


*[excerpt ends; 4383 characters not shown — see `research/sources/brown-mathpages-orthomagic-square-of-squares.full.md`]*
