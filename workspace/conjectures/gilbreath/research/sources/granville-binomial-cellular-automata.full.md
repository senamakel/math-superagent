<!-- source: https://dms.umontreal.ca/~andrew/Binomial/cellautom.html | converted from HTML -->

Pascal's triangle via cellular automata.

# Pascal's triangle via cellular automata.

A beautiful aspect of Pascal's triangle modulo *2*is that the `pattern' inside any triangle of *1*'s is similar in design to that of any subtriangle, though larger in size. If we extend Pascal's triangle to infinitely many rows, and reduce the scale of our picture in half each time that we double the number of rows, then the resulting design is called *self-similar*- that is, our picture can be reproduced by taking any subtriangle and magnifying it. Such an approach to Pascal's triangle is taken by [Wolfram][1]; and many examples of self-similarity have been investigated by [Mandelbrot][2].

We can study the value of entries in Pascal's triangle by such a `pictorial approach': has *1*'s on either end with *0*'s all the way in-between; and from the fact that any entry of the triangle is just the sum of the two adjacent entries on the line immediately above, we form a triangle underneath each of these *1*'s whose entries are the same as those of Pascal's triangle . These two triangles stay independant of one another until they meet in the *2p*th row. Thus, in that row, we have two copies of the *p*th row of Pascal's triangle, side-by-side, except that the middle term, has the corner terms of our two triangles overlayed: Therefore this row has a *1*on either end, a *2*in the middle, and *0*'s all the way in-between.

Again, underneath each of these *1*'s we form a triangle whose entries are the same as those of Pascal's triangle , while underneath the *2*we form a triangle whose entries are twice that in Pascal's triangle . These three triangles meet in the *3p*th row, which thus has *1*'s on either end, *3*'s at one-third and two-thirds of the way across and *0*'s everywhere else. Now underneath each of the *1*'s we again form a triangle whose entries are the same as those of Pascal's triangle , while underneath the *3*'s we form a triangle whose entries are three times that in Pascal's triangle .

Continuing this process, we see that the *np*th row of Pascal's triangle is a copy of the *n*th row, with 's placed between consecutive entries; and that the *p-1*rows immediately beneath the *np*th row are given by forming triangles underneath each non-zero entry of the *np*th row (say, ), that are times Pascal's triangle . Thus , so that Lucas' Theorem may be viewed as a result about automata with *p*possible states !

Wolfram gave an elegant proof of Glaisher's Theorem (that the number of odd entries in a given row of Pascal's triangle is a power of *2*), via the following induction hypothesis: For each , rows to modulo *2*are given by taking two copies of rows *0*to of Pascal's triangle, modulo *2*, side-by-side, and filling the space in-between with *0*'s; moreover Glaisher's result holds for each of these rows. For *n=1*we observe this by computation. For note that row must be all *1*'s so that row has *1*'s on either end with *0*'s all the way in-between. Thus, underneath each of these *1*'s we obtain a triangle whose entries are the same as those of Pascal's triangle, and the triangles don't meet until after the th row. Therefore the th row () modulo *2*is just two copies of the *r*th row modulo *2*, with some *0*'s in-between, and so has twice as many odd entries as the *r*th row; this completes the proof.

Also, as row is two copies of row *r*, whose first entries are seperated by *0*'s, thus Roberts' integer

The above approach has a further pretty consequence (see also [Long][3]): If we cut Pascal's triangle modulo *p*into subtriangles whose boundaries have entries, in the obvious way (that is, with rows *0*to in the first such triangle, then rows to cut into three subtriangles, two outer and one inner inverted triangle, etc. etc.), then any given subtriangle is exactly the sum of the two adjacent subtriangles, in the row of subtriangles immediately above. In other words these subtriangles obey the same addition law as Pascal's triangle itself. The behaviour of Pascal's triangle modulo higher powers of *p*is somewhat more complicated, but still follows certain rules which are discussed in [my paper][4].

We may also consider patterns in the count of the number of odd entries in a given row of Pascal's Triangle: Click [here][5].

---


## Links

[1]: references.html#Wo
[2]: references.html#Ma
[3]: references.html#Lo
[4]: references.html#Gr
[5]: binarydigit.html
