<!-- source: https://arxiv.org/pdf/math/0610932 | converted from PDF -->

arXiv:math/0610932v3  [math.CO]  18 Nov 2006
Sierpinski’s Triangle and the Prouhet-Thue-Morse Word

DAVID CALLAN
Department of Statistics
University of Wisconsin-Madison
1300 University Ave
Madison, WI 53706-1532
callan@stat.wisc.edu

November 18, 2006

Abstract

Sierpinski’s triangle is a fractal and the Prouhet-Thue-Morse word is suﬃciently
chaotic to avoid cubes. Here we observe that there is at least a tenuous connection
between them: the Sierpinski triangle is evident in Pascal’s triangle mod 2 whose
inverse, as an inﬁnite lower-triangular matrix, involves the Prouhet-Thue-Morse
word.

Pascal’s triangle mod 2 (Fig. 1b) is a discrete version of the fractal known as the
Sierpinski triangle [1]. Left-justiﬁed, it forms an inﬁnite lower-triangular (0,1)-matrix S
with 1s on the diagonal (Fig. 1c).

Pascal’s triangle Pascal’s triangle
mod 2 Pascal’s triangle mod 2
as an inﬁnite matrix S

1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
. . .
 1
1 1
1 0 1
1 1 1 1
1 0 0 0 1
. . .
 











 1 0 0 0 0 . . .
1 1 0 0 0
1 0 1 0 0
1 1 1 1 0
1 0 0 0 1
. . . .
 












Fig. 1a Fig. 1b Fig. 1c

The Prouhet-Thue-Morse word on a 2-letter alphabet {a, b} can be formed as follows.
Start with a, switch letters and append to get ab. Again switch letters and append to get

1

abba. Repeat to get abbabaab and iterate. The result is the inﬁnite Prouhet-Thue-Morse
word t(a, b) (t for Thue) that crops up in diverse contexts [2]. Here we observe that the
word t is related to the matrix S.

Theorem 1. S−1 is a (−1, 0, 1)-matrix. It has the same pattern of zeroes as S and the
nonzero entries in each column form the Prouhet-Thue-Morse word t(1, −1).

This is an immediate corollary of a more general result, Theorem 4 below.

For nonnegative integers i and j, say i is (binary-)free of j if the binary expansion of
i has 0s in the positions where j has 1s, equivalently, if the operation of adding i and j in
base 2 involves no “carries”. By Kummer’s well known criterion for the power of a prime
dividing a binomial coeﬃcient [3, Ex. 5.36], i is free of j ⇔ (i+j
j ) is odd. Thus the matrix
S has 0s precisely in the positions (i, j) where i − j is not free of j. For nonnegative
integer n, let b(n) denote the sum of the binary digits of n. For example, 62 = 110 and
b(6) = 2. The Prouhet-Thue-Morse word t(1, −1) has the explicit form (
(−1)b(n))

n≥0 [2].
With x an indeterminate, let S(x) denote the inﬁnite lower-triangular matrix deﬁned by

S(x)ij =
 



x
b(i−j) if i ≥ j ≥ 0 and i − j is free of j, and

0 otherwise.

Thus
 S(x) =
 


















 1
x 1
x 0 1
x
2 x x 1
x 0 0 0 1
x
2 x 0 0 x 1
x
2 0 x 0 x 0 1
x
3 x
2 x
2 x x
2 x x 1
. . . .
 



















and S(1) = S.
 2

Theorem 2. S(x)S(y) = S(x + y).

Proof First, as an example, consider i = 47, j = 9 and k between j and i of
the form displayed, where a, b, c are bits (0 or 1) and a prime superscript indicates the
complementary bit: a
′ = 1 − a.

integer binary expansion

i 1 0 1 1 1 1
j 0 0 1 0 0 1
i − j 1 0 0 1 1 0
k a 0 1 b c 1
i − k a
′ 0 0 b
′ c′ 0
k − j a 0 0 b c 0

Here, i − j is free of j. Also, k has 1s where j has 1s and 0s where i has 0s. And
so i − k is free of k and k − j is free of j and these are the only such k. In the sum
∑i
k=j S(x)ikS(y)kj for the (i, j) entry of S(x)S(y), k contributes x
a′+b′+c′ya+b+c and the
sum over all bits a, b, c is (x + y)3, the (i, j) entry of S(x + y). This works in general, as
we now demonstrate.

Suppose i ≥ j. The (i, j) entry of S(x)S(y) is ∑i
k=j S(x)ikS(y)kj. For 0 ≤ k ≤ i, if
i − k is free of k then both must have 0s in the positions where i has 0s. The bits of k
in the positions where i has 1s are arbitrary, and then i − k has the complementary bits
in these positions. For example, with i = 1 0 1 1 1 1 (in binary), k must have the binary
form a 0 b c d e so that i − k = a
′ 0 b
′ c′ d′ e
′. If, further, k ≥ j and k − j is free of j then
the bits of k are further restricted: they must be 1 in each position where j has a 1. In
short, if i − k is free of k and k − j is free of j, then k must have 0s where i has 0s and
1s where j has 1s and is unrestricted where i has a 1 and j has a 0. In particular, the
existence of k ∈ [j, i] with i − k free of k and k − j free of j implies that i must have a
1 in each position where j has a 1 and hence i − j is free of j. So, if i − j is not free of
j, then (S(x)S(y))

ij = ∑i
k=j 0 = 0 = S(x + y)ij. On the other hand, if i − j is free of j,
suppose there are t ≥ 0 positions where i has a 1 and j has a 0 (and so b(i − j) = t). As
above, the k ∈ [j, i] for which i − k is free of k and k − j is free of j are unrestricted in

3

these positions and both i − k and k − j have 0s in all other positions. Hence

(
S(x)S(y))

ij =
 i∑

k=j S(x)ikS(y)kj

= ∑

(i1,...,it)∈{0,1}t x
i1+...+ityi′
1+...+i′
t

=
 t∑

m=0
 ( t
m

)x
myt−m

= (x + y)t

= S(x + y)ij.

Induction yields

Corollary 3. For q a positive integer, S(x)q = S(qx).

Theorem 4. For rational r, Sr = S(r).

Proof For r = p/q with p, q positive integers, this follows from

S(p/q)q =
Cor. 3 S(p) =
Cor. 3 S(1)p = Sp.

For negative r, it now suﬃces to show that S−1 = S(−1) and this follows from

S(−1) S = S(−1) S(1) =
Thm. 2 S(0) = I.

Added in Proof. Roland Bacher informs me that he has obtained these results more
simply by observing that the 2k × 2k upper left submatrix of S(x) is the k-fold Kronecker
product of ( 1 0
x 1 ) [4, 5]. Emmanuel Ferrand treats similar material in an interesting recent
paper [6].

References

[1] MathWorld, The Sierpinski Sieve .

[2] J.-P. Allouche and J. O. Shallit, The Ubiquitous Prouhet-Thue-Morse Sequence in
C. Ding. T. Helleseth and H. Niederreiter, eds., Sequences and Their Applications:
Proceedings of SETA ’98, Springer-Verlag, 1999, pp. 1-16.

4

[3] Ronald L. Graham, Donald E. Knuth, Oren Patashnik, Concrete Mathematics (2nd
edition), Addison-Wesley, 1994.

[4] Roland Bacher and Robin Chapman, Symmetric Pascal matrices modulo p, European
J. Combin. 25 (2004), 459–473, http://front.math.ucdavis.edu/math.NT/0212144 .

[5] Roland Bacher, La suite de Thue-Morse et la cat´egorie Rec, Comptes Rendues Acad.
des Sci. Paris Ser I, 342 (2006), 161–164.

[6] Emmanuel Ferrand, An analogue of the Thue-Morse sequence, preprint, 2006,
http://www-fourier.ujf-grenoble.fr/˜eferrand/ZTM.pdf .

5
