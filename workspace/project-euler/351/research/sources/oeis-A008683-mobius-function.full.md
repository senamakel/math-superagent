<!-- source: https://oeis.org/A008683 | converted from HTML -->

A008683 - OEIS

[login][1]

The OEIS is supported by [the many generous donors to the OEIS Foundation][2].

[image: A008683 - OEIS] [3]

A008683

Möbius (or Moebius) function mu(n). mu(1) = 1; mu(n) = (-1)^k if n is the product of k different primes; otherwise mu(n) = 0.

1682

1, -1, -1, 0, -1, 1, -1, 0, 0, 1, -1, 0, -1, 1, 1, 0, -1, 0, -1, 0, 1, 1, -1, 0, 0, 1, 0, 0, -1, -1, -1, 0, 1, 1, 1, 0, -1, 1, 1, 0, -1, -1, -1, 0, 0, 1, -1, 0, 0, 0, 1, 0, -1, 0, 1, 0, 1, 1, -1, 0, -1, 1, 0, 0, 1, -1, -1, 0, 1, -1, -1, 0, -1, 1, 0, 0, 1, -1

( [list][4]; [graph][5]; [refs][6]; [listen][7]; [history][8]; [text][9]; [internal format][10])

OFFSET

1,1

COMMENTS

Moebius inversion: f(n) = Sum_{d|n} g(d) for all n <=> g(n) = Sum_{d|n} mu(d)*f(n/d) for all n.

a(n) depends only on prime signature of n (cf. [A025487][11]). So a(24) = a(375) since 24 = 2^3 * 3 and 375 = 3 * 5^3 both have prime signature (3, 1).

[A008683][12] = [A140579][13] ^(-1) * [A140664][14]. - [Gary W. Adamson][15], May 20 2008

Coons & Borwein prove that Sum_{n>=1} mu(n) z^n is transcendental. - [Jonathan Vos Post][16], Jun 11 2008; edited by [Charles R Greathouse IV][17], Sep 06 2017

Equals row sums of triangle [A144735][18] (the square of triangle [A054533][19]). - [Gary W. Adamson][15], Sep 20 2008

Conjecture: a(n) is the determinant of Redheffer matrix [A143104][20] where T(n, n) = 0. Verified for the first 50 terms. - [Mats Granvik][21], Jul 25 2008

From [Mats Granvik][21], Dec 06 2008: (Start)

The Editorial Office of the Journal of Number Theory kindly provided (via B. Conrey) the following proof of the conjecture: Let A be [A143104][20] and B be [A143104][20] where T(n, n) = 0.

"Suppose you expand det(B_n) along the bottom row. There is only a 1 in the first position and so the answer is (-1)^n times det(C_{n-1}) say, where C_{n-1} is the (n-1) by (n-1) matrix obtained from B_n by deleting the first column and the last row. Now the determinant of the Redheffer matrix is det(A_n) = M(n) where M(n) is the sum of mu(m) for 1 <= m <= n. Expanding det(A_n) along the bottom row, we see that det(A_n) = (-1)^n * det(C_{n-1}) + M(n-1). So we have det(B_n) = (-1)^n * det(C_{n-1}) = det(A_n) - M(n-1) = M(n) - M(n-1) = mu(n)." (End)

Conjecture: Consider the table [A051731][22] and treat 1 as a divisor. Move the value in the lower right corner vertically to a divisor position in the transpose of the table and you will find that the determinant is the Moebius function. The number of permutation matrices that contribute to the Moebius function appears to be [A074206][23]. - [Mats Granvik][21], Dec 08 2008

Convolved with [A152902][24] = [A000027][25], the natural numbers. - [Gary W. Adamson][15], Dec 14 2008

[Pickover, p. 226]: "The probability that a number falls in the -1 mailbox turns out to be 3/Pi^2 - the same probability as for falling in the +1 mailbox". - [Gary W. Adamson][15], Aug 13 2009

Let A = [A176890][26] and B = A * A * ... * A, then the leftmost column in matrix B converges to the Moebius function. - [Mats Granvik][21], [Gary W. Adamson][15], Apr 28 2010 and May 28 2020

Equals row sums of triangle [A176918][27]. - [Gary W. Adamson][15], Apr 29 2010

Calculate matrix powers: [A175992][28] ^0 - [A175992][28] ^1 + [A175992][28] ^2 - [A175992][28] ^3 + [A175992][28] ^4 - ... Then the Mobius function is found in the first column. Compare this to the binomial series for (1+x)^-1 = 1 - x + x^2 - x^3 + x^4 - ... . - [Mats Granvik][21], [Gary W. Adamson][15], Dec 06 2010

From [Richard L. Ollerton][29], May 08 2021: (Start)

Formulas for the numerous OEIS entries involving the Möbius transform (Dirichlet convolution of a(n) and some sequence h(n)) can be derived using the following (n >= 1):

Sum_{d|n} mu(d)*h(n/d) = Sum_{k=1..n} h(gcd(n,k))*mu(n/gcd(n,k))/phi(n/gcd(n,k)) = Sum_{k=1..n} h(n/gcd(n,k))*mu(gcd(n,k))/phi(n/gcd(n,k)), where phi = [A000010][30].

Use of gcd(n,k)*lcm(n,k) = n*k provides further variations. (End)

Formulas for products corresponding to the sums above are also available for sequences f(n) > 0: Product_{d|n} f(n/d)^mu(d) = Product_{k=1..n} f(gcd(n,k))^(mu(n/gcd(n,k))/phi(n/gcd(n,k))) = Product_{k=1..n} f(n/gcd(n,k))^(mu(gcd(n,k))/phi(n/gcd(n,k))). - [Richard L. Ollerton][29], Nov 08 2021

REFERENCES

T. M. Apostol, Introduction to Analytic Number Theory, Springer-Verlag, 1976, page 24.

L. Comtet, Advanced Combinatorics, Reidel, 1974, p. 161, #16.

G. H. Hardy, Ramanujan: twelve lectures on subjects suggested by his life and work, Cambridge, University Press, 1940, pp. 64-65.

G. H. Hardy and E. M. Wright, An Introduction to the Theory of Numbers, 5th ed., Oxford Univ. Press, 1979, th. 262 and 287.

Clifford A. Pickover, "The Math Book, from Pythagoras to the 57th Dimension, 250 Milestones in the History of Mathematics", Sterling Publishing, 2009, p. 226. - [Gary W. Adamson][15], Aug 13 2009

G. Pólya and G. Szegő, Problems and Theorems in Analysis Volume II. Springer_Verlag 1976.

James J. Tattersall, Elementary Number Theory in Nine Chapters, Cambridge University Press, 1999, pages 98-99.

J. V. Uspensky and M. A. Heaslet, Elementary Number Theory, McGraw-Hill, NY, 1939, pp. 109-112.

LINKS

Daniel Forgues, [Table of n, a(n) for n = 1..100000][31] (first 10000 terms from N. J. A. Sloane)

Milton Abramowitz and Irene A. Stegun, eds., [Handbook of Mathematical Functions][32], National Bureau of Standards Applied Math. Series 55, Tenth Printing, 1972, p. 826.

All Angles, [What is the Moebius function?][33], video, 2024.

Joerg Arndt, [Matters Computational (The Fxtbook)][34], pp. 705-707.

Yu Hin (Gary) Au, [Decompositions of Unit Hypercubes and the Reversion of a Generalized Möbius Series][35], arXiv:2205.03680 [math.CO], 2022.

Anders Björner and Richard P. Stanley, [A combinatorial miscellany][36].

Olivier Bordellès, [Some Explicit Estimates for the Mobius Function][37], J. Int. Seq. 18 (2015), Article 15.11.1

G. J. Chaitin, [Thoughts on the Riemann hypothesis][38] arXiv:math/0306042 [math.HO], 2003.

Michael Coons and Peter Borwein, [Transcendence of Power Series for Some Number Theoretic Functions][39], arXiv:0806.1563 [math.NT], 2008.

Marc Deléglise and Joël Rivat, [Computing the summation of the Mobius function][40], Experiment. Math. 5(4) (1996), 291-295.

Tom Edgar, [Posets and Möbius Inversion][41], slides, (2008).

Mats Granvik, [Inverse of a triangular matrix using determinants][42], [Inverse of a triangular matrix using matrix multiplication][43], [Inverse of a triangular matrix as a binomial series][44], [The ordinary generating function for the Mobius function][45].

Roman Le Lan, [Note on the Möbius function][46], 2025.

Keith Matthews, [Factorizing n and calculating phi(n),omega(n),d(n),sigma(n) and mu(n)][47].

A. F. Möbius, [Über eine besondere Art von Umkehrung der Reihen][48], Journal für die reine und angewandte Mathematik 9 (1832), 105-123.

Ed Pegg Jr., [The Mobius function (and squarefree numbers)][49].

Maxie Dion Schmidt, [Picking up the partial sums of the Möbius function problem with probabilistic number theory][50], arXiv:2604.23517 [math.NT], 2026. See p. 1 (Def. 1.2).

Paul Tarau, [Emulating Primality with Multiset Representations of Natural Numbers][51], in Theoretical Aspects Of Computing, ICTAC 2011, Lecture Notes in Computer Science, 2011, Volume 6916/2011, 218-238.

Paul Tarau, [Towards a generic view of primality through multiset decompositions of natural numbers][52], Theor. Comp. Sci. 537 (Jun 05 2014), 105-124.

Gerard Villemin's Almanac of Numbers, [Nombres de Moebius et de Mertens][53].

Eric Weisstein's World of Mathematics, [Moebius Function][54].

Eric Weisstein's World of Mathematics, [Redheffer Matrix][55].

Wikipedia, [Moebius function][56].

[Index entries for "core" sequences][57]

[Index entries for sequences computed from exponents in factorization of n][58]

FORMULA

Sum_{d|n} mu(d) = 1 if n = 1 else 0.

Dirichlet generating function: Sum_{n >= 1} mu(n)/n^s = 1/zeta(s). Also Sum_{n >= 1} mu(n)*x^n/(1-x^n) = x.

In particular, Sum_{n > 0} mu(n)/n = 0. - [Franklin T. Adams-Watters][59], Jun 20 2014

phi(n) = Sum_{d|n} mu(d)*n/d.

a(n) = [A091219][60] ( [A091202][61] (n)).

Multiplicative with a(p^e) = -1 if e = 1; 0 if e > 1. - [David W. Wilson][62], Aug 01 2001

abs(a(n)) = Sum_{d|n} 2^ [A001221][63] (d)*a(n/d). - [Benoit Cloitre][64], Apr 05 2002

Sum_{d|n} (-1)^(n/d)*mobius(d) = 0 for n > 2. - [Emeric Deutsch][65], Jan 28 2005

a(n) = (-1)^omega(n) * 0^(bigomega(n) - omega(n)) for n > 0, where bigomega(n) and omega(n) are the numbers of prime factors of n with and without repetition ( [A001222][66], [A001221][63], [A046660][67]). - [Reinhard Zumkeller][68], Apr 05 2003

Dirichlet generating function for the absolute value: zeta(s)/zeta(2s). - [Franklin T. Adams-Watters][59], Sep 11 2005

mu(n) = [A129360][69] (n) * (1, -1, 0, 0, 0, ...). - [Gary W. Adamson][15], Apr 17 2007

mu(n) = -Sum_{d < n, d|n} mu(d) if n > 1 and mu(1) = 1. - [Alois P. Heinz][70], Aug 13 2008

a(n) = [A174725][71] (n) - [A174726][72] (n). - [Mats Granvik][21], Mar 28 2010

a(n) = first column in the matrix inverse of a triangular table with the definition: T(1, 1) = 1, n > 1: T(n, 1) is any number or sequence, k = 2: T(n, 2) = T(n, k-1) - T(n-1, k), k > 2 and n >= k: T(n,k) = (Sum_{i = 1..k-1} T(n-i, k-1)) - (Sum_{i = 1..k-1} T(n-i, k)). - [Mats Granvik][21], Jun 12 2010

Product_{n >= 1} (1-x^n)^(-a(n)/n) = exp(x) (product form of the exponential function). - [Joerg Arndt][73], May 13 2011

a(n) = Sum_{k=1..n, gcd(k,n)=1} exp(2*Pi*i*k/n), the sum over the primitive n-th roots of unity. See the Apostol reference, p. 48, Exercise 14 (b). - [Wolfdieter Lang][74], Jun 13 2011

mu(n) = Sum_{k=1..n} [A191898][75] (n,k)*exp(-i*2*Pi*k/n)/n. (conjecture). - [Mats Granvik][21], Nov 20 2011

Sum_{k=1..n} a(k)*floor(n/k) = 1 for n >= 1. - [Peter Luschny][76], Feb 10 2012

a(n) = floor(omega(n)/bigomega(n))*(-1)^omega(n) = floor( [A001221][63] (n)/ [A001222][66] (n))*(-1)^ [A001221][63] (n). - [Enrique Pérez Herrero][77], Apr 27 2012

Multiplicative with a(p^e) = binomial(1, e) * (-1)^e. - [Enrique Pérez Herrero][77], Jan 19 2013

G.f. A(x) satisfies: x^2/A(x) = Sum_{n>=1} A( x^(2*n)/A(x)^n ). - [Paul D. Hanna][78], Apr 19 2016

a(n) = - [A008966][79] (n)*[A008836][80] (n)/(-1)^ [A005361][81] (n) = -floor(rad(n)/n)Lambda(n)/(-1)^tau(n/rad(n)). - [Anthony Browne][82], May 17 2016

a(n) = Kronecker delta of [A001221][63] (n) and [A001222][66] (n) (which is [A008966][79]) multiplied by [A008836][80] (n). - [Eric Desbiaux][83], Mar 15 2017

a(n) = [A132971][84] ( [A156552][85] (n)). - [Antti Karttunen][86], May 30 2017

a(n) = Sum_{k>=0} (-1)^(k-1)*binomial( [A001222][66] (n)-1, k)*binomial( [A001221][63] (n)-1+k, k), for n > 1. [Conjectured by [Mats Granvik][21], Sep 08 2018 and proved by [Roman Le Lan][87], Oct 10 2025]

From [Peter Bala][88], Mar 15 2019: (Start)

Sum_{n >= 1} mu(n)*x^n/(1 + x^n) = x - 2*x^2. See, for example, Pólya and Szegő, Part V111, Chap. 1, No. 71.

Sum_{n >= 1} (-1)^(n+1)*mu(n)*x^n/(1 - x^n) = x + 2*(x^2 + x^4 + x^8 + x^16 + ...).

Sum_{n >= 1} (-1)^(n+1)*mu(n)*x^n/(1 + x^n) = x - 2*(x^4 + x^8 + x^16 + x^32 + ...).

Sum_{n >= 1} |mu(n)|*x^n/(1 - x^n) = Sum_{n >= 1} (2^w(n))*x^n, where w(n) is the number of different prime factors of n (Hardy and Wright, Chapter XVI, Theorem 264).

Sum_{n odd} |mu(n)|*x^n/(1 + x^(2*n)) = Sum_{n in S_1} (2^w_1(n))*x^n, where S_1 = {1, 5, 13, 17, 25, 29, ...} is the multiplicative semigroup of positive integers generated by 1 and the primes p = 1 (mod 4), and w_1(n) is the number of different prime factors p = 1 (mod 4) of n.

Sum_{n odd} (-1)^((n-1)/2)*mu(n)*x^n/(1 - x^(2*n)) = Sum_{n in S_3} (2^w_3(n))*x^n, where S_3 = {1, 3, 7, 9, 11, 19, 21, ...} is the multiplicative semigroup of positive integers generated by 1 and the primes p = 3 (mod 4), and where w_3(n) is the number of different prime factors p = 3 (mod 4) of n. (End)

G.f. A(x) satisfies: A(x) = x - Sum_{k>=2} A(x^k). - [Ilya Gutkovskiy][89], May 11 2019

a(n) = sign( [A023900][90] (n)) * [[A007947][91] (n) = n] where [] is the Iverson bracket. - [I. V. Serov][92], May 15 2019

a(n) = Sum_{k = 1..n} gcd(k, n)*a(gcd(k, n)) = Sum_{d divides n} a(d)*d*phi(n/d). - [Peter Bala][88], Jan 16 2024

EXAMPLE

G.f. = x - x^2 - x^3 - x^5 + x^6 - x^7 + x^10 - x^11 - x^13 + x^14 + x^15 + ...

MAPLE

with(numtheory): [A008683][12]:= n->mobius(n);

with(numtheory): [ seq(mobius(n), n=1..100) ];

# Note that older versions of Maple define mobius(0) to be -1.

# This is unwise! Moebius(0) is better left undefined.

with(numtheory):

mu:= proc(n::posint) option remember; `if`(n=1, 1,

-add(mu(d), d=divisors(n) minus {n}))

end:

seq(mu(n), n=1..100); # [Alois P. Heinz][70], Aug 13 2008

MATHEMATICA

Array[ MoebiusMu, 100]

(* Alternative: *)

m = 100; A[_] = 0;

Do[A[x_] = x - Sum[A[x^k], {k, 2, m}] + O[x]^m // Normal, {m}];

CoefficientList[A[x]/x, x] (* [Jean-François Alcover][93], Oct 20 2019, after [Ilya Gutkovskiy][89] *)

PROG

(Axiom) [moebiusMu(n) for n in 1..100]

(Magma) [ MoebiusMu(n) : n in [1..100]];

(PARI) a=n->if(n<1, 0, moebius(n));

(PARI) {a(n) = if( n<1, 0, direuler( p=2, n, 1 - X)[n])};

(PARI) list(n)=my(v=vector(n, i, 1)); forprime(p=2, sqrtint(n), forstep(i=p, n, p, v[i]*=-1); forstep(i=p^2, n, p^2, v[i]=0)); forprime(p=sqrtint(n)+1, n, forstep(i=p, n, p, v[i]*=-1)); v \\ [Charles R Greathouse IV][17], Apr 27 2012

(Maxima) [A008683][12] (n):=moebius(n)$ makelist( [A008683][12] (n), n, 1, 30); /* [Martin Ettl][94], Oct 24 2012 */

(Haskell)

import Math.NumberTheory.Primes.Factorisation (factorise)

a008683 = mu . snd . unzip . factorise where

mu [] = 1; mu (1:es) = - mu es; mu (_:es) = 0

-- [Reinhard Zumkeller][68], Dec 13 2015, Oct 09 2013

(Haskell)

a008683 1 = 1

a008683 n = - sum [a008683 d | d <- [1..(n-1)], n `mod` d == 0]

-- [Harry Richman][95], Jun 13 2025

(SageMath)

@cached_function

def mu(n):

if n < 2: return n

return -sum(mu(d) for d in divisors(n)[:-1])

# Changing the sign of the sum gives the number of ordered factorizations of n [A074206][23].

print([mu(n) for n in (1..96)]) # [Peter Luschny][76], Dec 26 2016

(Python)

from sympy import mobius

print([mobius(i) for i in range(1, 101)]) # [Indranil Ghosh][96], Mar 18 2017

CROSSREFS

Variants of a(n) are [A178536][97], [A181434][98], [A181435][99].

Cf. [A000010][30], [A001221][63], [A008966][79], [A007423][100], [A080847][101], [A002321][102] (partial sums), [A069158][103], [A055615][104], [A129360][69], [A140579][13], [A140664][14], [A140254][105], [A143104][20], [A152902][24], [A206706][106], [A063524][107], [A007427][108], [A007428][109], [A124010][110], [A073776][111], [A074206][23], [A132971][84], [A156552][85].

Cf. [A059956][112] (Dgf at s=2), [A088453][113] (Dgf at s=3), [A215267][114] (Dgf at s=4), [A343308][115] (Dgf at s=5).

Sequence in context: [A130047][116] [A293233][117] [A302050][118] * [A008966][79] [A080323][119] [A157657][120]

Adjacent sequences: [A008680][121] [A008681][122] [A008682][123] * [A008684][124] [A008685][125] [A008686][126]

KEYWORD

core, sign, easy, mult, nice

AUTHOR

[N. J. A. Sloane][127]

STATUS

approved

[Lookup][3] [Welcome][128] [Wiki][129] [Register][130] [Music][131] [Plot 2][132] [Demos][133] [Index][134] [WebCam][135] [Contribute][136] [Format][137] [Style Sheet][138] [Transforms][139] [Superseeker][140] [Recents][141]

[The OEIS Community][142]

Maintained by [The OEIS Foundation Inc.][143]

Last modified August 14 12:19 EDT 2026. Contains 398312 sequences.

[License Agreements, Terms of Use, Privacy Policy][144]


## Links

[1]: /login?redirect=%2fA008683
[2]: http://oeisf.org/#DONATE
[3]: /
[4]: /A008683/list
[5]: /A008683/graph
[6]: /search?q=A008683+-id:A008683
[7]: /A008683/listen
[8]: /history?seq=A008683
[9]: /search?q=id:A008683&fmt=text
[10]: /A008683/internal
[11]: /A025487
[12]: /A008683
[13]: /A140579
[14]: /A140664
[15]: /wiki/User:Gary_W._Adamson
[16]: /wiki/User:Jonathan_Vos_Post
[17]: /wiki/User:Charles_R_Greathouse_IV
[18]: /A144735
[19]: /A054533
[20]: /A143104
[21]: /wiki/User:Mats_Granvik
[22]: /A051731
[23]: /A074206
[24]: /A152902
[25]: /A000027
[26]: /A176890
[27]: /A176918
[28]: /A175992
[29]: /wiki/User:Richard_L._Ollerton
[30]: /A000010
[31]: /A008683/b008683.txt
[32]: http://www.convertit.com/Go/ConvertIt/Reference/AMS55.ASP
[33]: https://www.youtube.com/watch?v=fGbJrY75LU8
[34]: http://www.jjj.de/fxt/#fxtbook
[35]: https://arxiv.org/pdf/2205.03680
[36]: http://www-math.mit.edu/~rstan/papers/comb.pdf
[37]: https://cs.uwaterloo.ca/journals/JIS/VOL18/Bordelles2/bordelles21.html
[38]: https://arxiv.org/pdf/math/0306042
[39]: https://arxiv.org/pdf/0806.1563
[40]: http://projecteuclid.org/euclid.em/1047565447
[41]: http://www.plu.edu/~edgartj/
[42]: http://mobiusfunction.wordpress.com/2010/08/07/the-inverse-of-triangular-matrix-using-determinants/
[43]: http://mobiusfunction.wordpress.com/2010/08/07/the-inverse-of-a-triangular-matrix/
[44]: http://mobiusfunction.wordpress.com/2010/12/08/the-inverse-of-triangular-matrix-as-a-binomial-series/
[45]: http://mobiusfunction.wordpress.com/2011/03/08/the-ordinary-generating-function-for-the-mobius-function/
[46]: https://rorolelan.wordpress.com/wp-content/uploads/2025/10/note_on_mobius_function-1.pdf
[47]: http://www.numbertheory.org/php/factor.html
[48]: http://gdz.sub.uni-goettingen.de/dms/resolveppn/?PPN=GDZPPN002138654
[49]: https://www.mathpuzzle.com/MAA/02-Mobius%20Function/mathgames_11_03_03.html
[50]: https://arxiv.org/pdf/2604.23517
[51]: https://doi.org/10.1007/978-3-642-23283-1_15
[52]: https://doi.org/10.1016/j.tcs.2014.04.025
[53]: http://villemin.gerard.free.fr/TABLES/aaaFArit/MobiusMe.htm
[54]: https://mathworld.wolfram.com/MoebiusFunction.html
[55]: https://mathworld.wolfram.com/RedhefferMatrix.html
[56]: https://en.wikipedia.org/wiki/Mobius_function
[57]: /index/Cor#core
[58]: /index/Eu#epf
[59]: /wiki/User:Franklin_T._Adams-Watters
[60]: /A091219
[61]: /A091202
[62]: /wiki/User:David_W._Wilson
[63]: /A001221
[64]: /wiki/User:Benoit_Cloitre
[65]: /wiki/User:Emeric_Deutsch
[66]: /A001222
[67]: /A046660
[68]: /wiki/User:Reinhard_Zumkeller
[69]: /A129360
[70]: /wiki/User:Alois_P._Heinz
[71]: /A174725
[72]: /A174726
[73]: /wiki/User:Joerg_Arndt
[74]: /wiki/User:Wolfdieter_Lang
[75]: /A191898
[76]: /wiki/User:Peter_Luschny
[77]: /wiki/User:Enrique_Pérez_Herrero
[78]: /wiki/User:Paul_D._Hanna
[79]: /A008966
[80]: /A008836
[81]: /A005361
[82]: /wiki/User:Anthony_Browne
[83]: /wiki/User:Eric_Desbiaux
[84]: /A132971
[85]: /A156552
[86]: /wiki/User:Antti_Karttunen
[87]: /wiki/User:Roman_Le_Lan
[88]: /wiki/User:Peter_Bala
[89]: /wiki/User:Ilya_Gutkovskiy
[90]: /A023900
[91]: /A007947
[92]: /wiki/User:I._V._Serov
[93]: /wiki/User:Jean-François_Alcover
[94]: /wiki/User:Martin_Ettl
[95]: /wiki/User:Harry_Richman
[96]: /wiki/User:Indranil_Ghosh
[97]: /A178536
[98]: /A181434
[99]: /A181435
[100]: /A007423
[101]: /A080847
[102]: /A002321
[103]: /A069158
[104]: /A055615
[105]: /A140254
[106]: /A206706
[107]: /A063524
[108]: /A007427
[109]: /A007428
[110]: /A124010
[111]: /A073776
[112]: /A059956
[113]: /A088453
[114]: /A215267
[115]: /A343308
[116]: /A130047
[117]: /A293233
[118]: /A302050
[119]: /A080323
[120]: /A157657
[121]: /A008680
[122]: /A008681
[123]: /A008682
[124]: /A008684
[125]: /A008685
[126]: /A008686
[127]: /wiki/User:N._J._A._Sloane
[128]: /wiki/Welcome
[129]: /wiki/Main_Page
[130]: /wiki/Special:RequestAccount
[131]: /play.html
[132]: /plot2.html
[133]: /demo1.html
[134]: /wiki/Index_to_OEIS
[135]: /webcam
[136]: /Submit.html
[137]: /eishelp2.html
[138]: /wiki/Style_Sheet
[139]: /transforms.html
[140]: /ol.html
[141]: /recent
[142]: /community.html
[143]: http://oeisf.org
[144]: /wiki/Legal_Documents
