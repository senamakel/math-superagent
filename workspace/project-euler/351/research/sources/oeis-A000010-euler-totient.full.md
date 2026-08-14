<!-- source: https://oeis.org/A000010 | converted from HTML -->

A000010 - OEIS

[login][1]

The OEIS is supported by [the many generous donors to the OEIS Foundation][2].

[image: A000010 - OEIS] [3]

A000010

Euler totient function phi(n): count numbers <= n and prime to n.
(Formerly M0299 N0111)

4429

1, 1, 2, 2, 4, 2, 6, 4, 6, 4, 10, 4, 12, 6, 8, 8, 16, 6, 18, 8, 12, 10, 22, 8, 20, 12, 18, 12, 28, 8, 30, 16, 20, 16, 24, 12, 36, 18, 24, 16, 40, 12, 42, 20, 24, 22, 46, 16, 42, 20, 32, 24, 52, 18, 40, 24, 36, 28, 58, 16, 60, 30, 36, 32, 48, 20, 66, 32, 44

( [list][4]; [graph][5]; [refs][6]; [listen][7]; [history][8]; [text][9]; [internal format][10])

OFFSET

1,3

COMMENTS

Number of elements in a reduced residue system modulo n.

Degree of the n-th cyclotomic polynomial (cf. [A013595][11]). - [Benoit Cloitre][12], Oct 12 2002

Number of distinct generators of a cyclic group of order n. Number of primitive n-th roots of unity. (A primitive n-th root x is such that x^k is not equal to 1 for k = 1, 2, ..., n - 1, but x^n = 1.) - [Lekraj Beedassy][13], Mar 31 2005

Also number of complex Dirichlet characters modulo n; Sum_{k=1..n} a(k) is asymptotic to (3/Pi^2)*n^2. - [Steven Finch][14], Feb 16 2006

a(n) is the highest degree of irreducible polynomial dividing 1 + x + x^2 + ... + x^(n-1) = (x^n - 1)/(x - 1). - [Alexander Adamchuk][15], Sep 02 2006, corrected Sep 27 2006

a(p) = p - 1 for prime p. a(n) is even for n > 2. For n > 2, a(n)/2 = [A023022][16] (n) = number of partitions of n into 2 ordered relatively prime parts. - [Alexander Adamchuk][15], Jan 25 2007

Number of automorphisms of the cyclic group of order n. - [Benoit Jubin][17], Aug 09 2008

a(n+2) equals the number of palindromic Sturmian words of length n which are "bispecial", prefix or suffix of two Sturmian words of length n + 1. - [Fred Lunnon][18], Sep 05 2010

Suppose that a and n are coprime positive integers, then by Euler's totient theorem, any factor of n divides a^phi(n) - 1. - [Lei Zhou][19], Feb 28 2012

If m has k prime factors, (p_1, p_2, ..., p_k), then phi(m*n) = (Product_{i=1..k} phi (p_i*n))/phi(n)^(k-1). For example, phi(42*n) = phi(2*n)*phi(3*n)*phi(7*n)/phi(n)^2. - [Gary Detlefs][20], Apr 21 2012

Sum_{n>=1} a(n)/n! = 1.954085357876006213144... This sum is referenced in Plouffe's inverter. - [Alexander R. Povolotsky][21], Feb 02 2013 (see [A336334][22]. - [Hugo Pfoertner][23], Jul 22 2020)

The order of the multiplicative group of units modulo n. - [Michael Somos][24], Aug 27 2013

A strong divisibility sequence, that is, gcd(a(n), a(m)) = a(gcd(n, m)) for all positive integers n and m. - [Michael Somos][24], Dec 30 2016

From [Eric Desbiaux][25], Jan 01 2017: (Start)

a(n) equals the Ramanujan sum c_n(n) (last term on n-th row of triangle [A054533][26]).

a(n) equals the Jordan function J_1(n) (cf. [A007434][27], [A059376][28], [A059377][29], which are the Jordan functions J_2, J_3, J_4, respectively). (End)

For n > 1, a(n) appears to be equal to the number of semi-meander solutions for n with top arches containing exactly 2 mountain ranges and exactly 2 arches of length 1. - [Roger Ford][30], Oct 11 2017

a(n) is the minimum dimension of a lattice able to generate, via cut-and-project, the quasilattice whose diffraction pattern features n-fold rotational symmetry. The case n=15 is the first n > 1 in which the following simpler definition fails: "a(n) is the minimum dimension of a lattice with n-fold rotational symmetry". - [Felix Flicker][31], Nov 08 2017

Number of cyclic Latin squares of order n with the first row in ascending order. - [Eduard I. Vatutin][32], Nov 01 2020

a(n) is the number of rational numbers p/q >= 0 (in lowest terms) such that p + q = n. - [Rémy Sigrist][33], Jan 17 2021

From [Richard L. Ollerton][34], May 08 2021: (Start)

Formulas for the numerous OEIS entries involving Dirichlet convolution of a(n) and some sequence h(n) can be derived using the following (n >= 1):

Sum_{d|n} phi(d)*h(n/d) = Sum_{k=1..n} h(gcd(n,k)) [see P. H. van der Kamp link] = Sum_{d|n} h(d)*phi(n/d) = Sum_{k=1..n} h(n/gcd(n,k))*phi(gcd(n,k))/phi(n/gcd(n,k)). Similarly,

Sum_{d|n} phi(d)*h(d) = Sum_{k=1..n} h(n/gcd(n,k)) = Sum_{k=1..n} h(gcd(n,k))*phi(gcd(n,k))/phi(n/gcd(n,k)).

More generally,

Sum_{d|n} h(d) = Sum_{k=1..n} h(gcd(n,k))/phi(n/gcd(n,k)) = Sum_{k=1..n} h(n/gcd(n,k))/phi(n/gcd(n,k)).

In particular, for sequences involving the Möbius transform:

Sum_{d|n} mu(d)*h(n/d) = Sum_{k=1..n} h(gcd(n,k))*mu(n/gcd(n,k))/phi(n/gcd(n,k)) = Sum_{k=1..n} h(n/gcd(n,k))*mu(gcd(n,k))/phi(n/gcd(n,k)), where mu = [A008683][35].

Use of gcd(n,k)*lcm(n,k) = n*k and phi(gcd(n,k))*phi(lcm(n,k)) = phi(n)*phi(k) provide further variations. (End)

From [Richard L. Ollerton][34], Nov 07 2021: (Start)

Formulas for products corresponding to the sums above may found using the substitution h(n) = log(f(n)) where f(n) > 0 (for example, cf. formulas for the sum [A018804][36] and product [A067911][37] of gcd(n,k)):

Product_{d|n} f(n/d)^phi(d) = Product_{k=1..n} f(gcd(n,k)) = Product_{d|n} f(d)^phi(n/d) = Product_{k=1..n} f(n/gcd(n,k))^(phi(gcd(n,k))/phi(n/gcd(n,k))),

Product_{d|n} f(d)^phi(d) = Product_{k=1..n} f(n/gcd(n,k)) = Product_{k=1..n} f(gcd(n,k))^(phi(gcd(n,k))/phi(n/gcd(n,k))),

Product_{d|n} f(d) = Product_{k=1..n} f(gcd(n,k))^(1/phi(n/gcd(n,k))) = Product_{k=1..n} f(n/gcd(n,k))^(1/phi(n/gcd(n,k))),

Product_{d|n} f(n/d)^mu(d) = Product_{k=1..n} f(gcd(n,k))^(mu(n/gcd(n,k))/phi(n/gcd(n,k))) = Product_{k=1..n} f(n/gcd(n,k))^(mu(gcd(n,k))/phi(n/gcd(n,k))), where mu = [A008683][35]. (End)

a(n+1) is the number of binary words with exactly n distinct subsequences (when n > 0). - [Radoslaw Zak][38], Nov 29 2021

REFERENCES

M. Abramowitz and I. A. Stegun, eds., Handbook of Mathematical Functions, National Bureau of Standards Applied Math. Series 55, 1964 (and various reprintings), p. 840.

T. M. Apostol, Introduction to Analytic Number Theory, Springer-Verlag, 1976, page 24.

M. Baake and U. Grimm, Aperiodic Order Vol. 1: A Mathematical Invitation, Encyclopedia of Mathematics and its Applications 149, Cambridge University Press, 2013: see Tables 3.1 and 3.2.

Miklos Bona, Introduction to Enumerative and Analytic Combinatorics, CRC Press, 2025, pp. 88-90.

Florian Cajori, A History of Mathematical Notations, Dover edition (2012), par. 409.

L. Comtet, Advanced Combinatorics, Reidel, 1974, p. 193.

John H. Conway and Richard K. Guy, The Book of Numbers, New York: Springer-Verlag, 1996. See pp. 154-156.

C. W. Curtis, Pioneers of Representation Theory ..., Amer. Math. Soc., 1999; see p. 3.

J.-M. De Koninck & A. Mercier, 1001 Problèmes en Théorie Classique des Nombres, Ellipses, Paris, 2004, Problème 529, pp. 71-257.

L. E. Dickson, History of the Theory of Numbers. Carnegie Institute Public. 256, Washington, DC, Vol. 1, 1919; Vol. 2, 1920; Vol. 3, 1923, see vol. 1, Chapter V.

S. R. Finch, Mathematical Constants, Cambridge, 2003, pp. 115-119.

Carl Friedrich Gauss, "Disquisitiones Arithmeticae", Yale University Press, 1965; see p. 21.

Ronald L. Graham, Donald E. Knuth and Oren Patashnik, Concrete Math., 2n-d ed.; Addison-Wesley, 1994, p. 137.

R. K. Guy, Unsolved Problems in Number Theory, Springer, 1st edition, 1981. See section B36.

G. H. Hardy and E. M. Wright, An Introduction to the Theory of Numbers, 5th ed., Oxford Univ. Press, 1979, th. 60, 62, 63, 288, 323, 328, 330.

Peter Hilton and Jean Pedersen, A Mathematical Tapestry, Demonstrating the Beautiful Unity of Mathematics, Cambridge University Press, pages 261-264, the Coach theorem.

Jean-Marie Monier, Analyse, Exercices corrigés, 2ème année MP, Dunod, 1997, Exercice 3.2.21 pp. 281-294.

G. Pólya and G. Szegő, Problems and Theorems in Analysis, Springer-Verlag, New York, Heidelberg, Berlin, 2 vols., 1976, Vol. II, problem 71, p. 126.

Paulo Ribenboim, The New Book of Prime Number Records.

Paulo Ribenboim, The Little Book of Bigger Primes, Springer-Verlag NY 2004. See pp. 28-33.

N. J. A. Sloane, A Handbook of Integer Sequences, Academic Press, 1973 (includes this sequence).

N. J. A. Sloane and Simon Plouffe, The Encyclopedia of Integer Sequences, Academic Press, 1995 (includes this sequence).

James J. Tattersall, Elementary Number Theory in Nine Chapters, Cambridge University Press, 1999, pages 162-167.

J. V. Uspensky and M. A. Heaslet, Elementary Number Theory, McGraw-Hill, NY, 1939, pp. 107-109, 113-116.

LINKS

Daniel Forgues, [Table of n, phi(n) for n = 1..100000][39] (first 10000 terms from N. J. A. Sloane)

Milton Abramowitz and Irene A. Stegun, eds., [Handbook of Mathematical Functions][40], National Bureau of Standards Applied Math. Series 55, Tenth Printing, 1972.

Dario A. Alpern, [Factorization using the Elliptic Curve Method (along with sigma_0, sigma_1 and phi functions)][41].

Joerg Arndt, [Matters Computational (The Fxtbook)][42], section 39.7, pp. 776-778.

F. Bayart, [Indicateur d'Euler][43] (in French).

Alexander Bogomolny, [Euler Function and Theorem][44].

Chris K. Caldwell, The Prime Glossary, [Euler's phi function][45].

Robert D. Carmichael, [A table of the values of m corresponding to given values of phi(m)][46], Amer. J. Math., 30 (1908), 394-400. [Annotated scanned copy]

Paul Erdős, Andrew Granville, Carl Pomerance and Claudia Spiro, [On the normal behavior of the iterates of some arithmetic functions][47], Analytic number theory, Birkhäuser Boston, 1990, pp. 165-204.

Paul Erdős, Andrew Granville, Carl Pomerance and Claudia Spiro, [On the normal behavior of the iterates of some arithmetic functions][48], Analytic number theory, Birkhäuser Boston, 1990, pp. 165-204. [Annotated copy with A-numbers]

Kevin Ford, [The number of solutions of phi(x)=m][49], arXiv:math/9907204 [math.NT], 1999.

Kevin Ford, Florian Luca and Pieter Moree, [Values of the Euler phi-function not divisible by a given odd prime, and the distribution of Euler-Kronecker constants for cyclotomic fields][50], arXiv:1108.3805 [math.NT], 2011-2012.

Sela Fried, [Proof of a conjecture stated in A000010][51], 2025.

Sela Fried, [Further proofs of conjectures from the OEIS][52], arXiv:2607.24832 [math.GM], 2026. See pp. 2-3.

H. Fripertinger, [The Euler phi function][53].

Daniele A. Gewurz and Francesca Merola, [Sequences realized as Parker vectors of oligomorphic permutation groups][54], J. Integer Seqs., Vol. 6, 2003.

E. Pérez Herrero, [Totient Carnival partitions][55], Psychedelic Geometry Blogspot.

Peter H. van der Kamp, [On the Fourier transform of the greatest common divisor][56], arXiv:1201.3139 [math.NT], 2012.

M. Lal and P. Gillard, [Table of Euler's phi function, n < 10^5][57], Math. Comp., 23 (1969), 682-683.

Eric Lehman, F. Thomson Leighton, and Albert R. Meyer, [Mathematics for Computer Science][58], Massachusetts Institute of Technology, 2015. See pp. 586-587.

Derrick N. Lehmer, [Review of Dickson's History of the Theory of Numbers][59], Bull. Amer. Math. Soc., 26 (1919), 125-132.

Roman Le Lan, [A limit definition of J_z(n)][60], Sep 14 2025.

Peter Luschny, [Sequences related to Euler's totient function][61].

R. J. Mathar, [Graphical representation among sequences closely related to this one][62] (cf. N. J. A. Sloane, "Families of Essentially Identical Sequences").

Mathematics Stack Exchange, [Is the Euler phi function bounded below?][63] (2013).

Mathforum, [Proving phi(m) Is Even][64].

Keith Matthews, [Factorizing n and calculating phi(n), d(n), omega(n), sigma(n), lambda(n) and mu(n)][65].

Graeme McRae, [Euler's Totient Function][66].

François Nicolas, [A simple, polynomial-time algorithm for the matrix torsion problem][67], arXiv:0806.2068 [cs.DM], 2008-2009.

Matthew Parker, [The first 5 million terms (7-Zip compressed file)][68].

Carl Pomerance and Hee-Sung Yang, [Variant of a theorem of Erdős on the sum-of-proper-divisors function][69], Math. Comp., to appear (2014).

Primefan, [Euler's Totient Function Values For n=1 to 500, with Divisor Lists][70].

Marko Riedel, [Combinatorics and number theory page][71].

J. Barkley Rosser and Lowell Schoenfeld, [Approximate formulas for some functions of prime numbers][72], Illinois J. Math. 6 (1962), no. 1, 64-94.

K. Schneider, [Euler phi-function][73], PlanetMath.org.

Wacław F. Sierpiński, [Euler's Totient Function And The Theorem Of Euler][74].

N. J. A. Sloane, [Families of Essentially Identical Sequences][75], Mar 24 2021 (Includes this sequence)

N. J. A. Sloane, ["A Handbook of Integer Sequences" Fifty Years Later][76], arXiv:2301.03149 [math.NT], 2023, p. 14.

Ulrich Sondermann, [Euler's Totient Function][77].

William A. Stein, [Phi is a Multiplicative Function][78].

Pinthira Tangsupphathawat, Takao Komatsu and Vichian Laohakosol, [Minimal Polynomials of Algebraic Cosine Values, II][79], J. Int. Seq., Vol. 21 (2018), Article 18.9.5.

László Tóth, [Multiplicative arithmetic functions of several variables: a survey][80], arXiv preprint arXiv:1310.7053 [math.NT], 2013-2014.

G. Villemin, [Totient d'Euler][81].

K. W. Wegner, [Values of phi(x) = n for n from 2 through 1978][82], mimeographed manuscript, no date. [Annotated scanned copy]

Eric Weisstein's World of Mathematics, [Modulo Multiplication Group][83].

Eric Weisstein's World of Mathematics, [Moebius Transform][84].

Eric Weisstein's World of Mathematics, [Totient Function][85].

Wikipedia, [Euler's totient function][86].

Wikipedia, [Multiplicative group of integers modulo n][87].

Wikipedia, [Ramanujan's sum][88].

Wolfram Research, [First 50 values of phi(n)][89].

Gang Xiao, [Numerical Calculator][90]. To display phi(n) operate on "eulerphi(n)".

[Index entries for "core" sequences][91]

[Index to divisibility sequences][92]

FORMULA

phi(n) = n*Product_{distinct primes p dividing n} (1 - 1/p).

Sum_{d divides n} phi(d) = n.

phi(n) = Sum_{d divides n} mu(d)*n/d, i.e., the Moebius transform of the natural numbers; mu() = Moebius function [A008683][35] ().

Dirichlet generating function Sum_{n>=1} phi(n)/n^s = zeta(s-1)/zeta(s). Also Sum_{n >= 1} phi(n)*x^n/(1 - x^n) = x/(1 - x)^2.

Multiplicative with a(p^e) = (p - 1)*p^(e-1). - [David W. Wilson][93], Aug 01 2001

Sum_{n>=1} (phi(n)*log(1 - x^n)/n) = -x/(1 - x) for -1 < x < 1 (cf. [A002088][94]) - [Henry Bottomley][95], Nov 16 2001

a(n) = binomial(n+1, 2) - Sum_{i=1..n-1} a(i)*floor(n/i) (see [A000217][96] for inverse). - [Jon Perry][97], Mar 02 2004

It is a classical result (certainly known to Landau, 1909) that lim inf n/phi(n) = 1 (taking n to be primes), lim sup n/(phi(n)*log(log(n))) = e^gamma, with gamma = Euler's constant (taking n to be products of consecutive primes starting from 2 and applying Mertens' theorem). See e.g. Ribenboim, pp. 319-320. - Pieter Moree, Sep 10 2004

a(n) = Sum_{i=1..n} |k(n, i)| where k(n, i) is the Kronecker symbol. Also a(n) = n - #{1 <= i <= n : k(n, i) = 0}. - [Benoit Cloitre][12], Aug 06 2004 [Corrected by [Jianing Song][98], Sep 25 2018]

Conjecture: Sum_{i>=2} (-1)^i/(i*phi(i)) exists and is approximately 0.558 ( [A335319][99]). - Orges Leka (oleka(AT)students.uni-mainz.de), Dec 23 2004

From [Enrique Pérez Herrero][100], Sep 07 2010: (Start)

a(n) = Sum_{i=1..n} floor(sigma_k(i*n)/sigma_k(i)*sigma_k(n)), where sigma_2 is [A001157][101].

a(n) = Sum_{i=1..n} floor(tau_k(i*n)/tau_k(i)*tau_k(n)), where tau_3 is [A007425][102].

a(n) = Sum_{i=1..n} floor(rad(i*n)/rad(i)*rad(n)), where rad is [A007947][103]. (End)

a(n) = [A173557][104] (n)*[A003557][105] (n). - [R. J. Mathar][106], Mar 30 2011

a(n) = [A096396][107] (n) + [A096397][108] (n) for n >= 2. - [Reinhard Zumkeller][109], Mar 24 2012

phi(p*n) = phi(n)*(floor(((n + p - 1) mod p)/(p - 1)) + p - 1), for primes p. - [Gary Detlefs][20], Apr 21 2012

For odd n, a(n) = 2*[A135303][110] ((n-1)/2)*[A003558][111] ((n-1)/2) or phi(n) = 2*c*k; the Coach theorem of Pedersen et al. Cf. [A135303][110]. - [Gary W. Adamson][112], Aug 15 2012

G.f.: Sum_{n>=1} mu(n)*x^n/(1 - x^n)^2, where mu(n) = [A008683][35] (n). - [Mamuka Jibladze][113], Apr 05 2015

a(n) = n - cototient(n) = n - [A051953][114] (n). - [Omar E. Pol][115], May 14 2016

a(n) = lim_{s->1} n*zeta(s)*(Sum_{d divides n} [A008683][35] (d)/(e^(1/d))^(s-1)), for n > 1. - [Mats Granvik][116], Jan 26 2017

Conjecture: a(n) = Sum_{a=1..n} Sum_{b=1..n} Sum_{c=1..n} 1 for n > 1. The sum is over a,b,c such that n*c - a*b = 1. - [Benedict W. J. Irwin][117], Apr 03 2017

Irwin's conjecture is true (see Fried link). - [Sela Fried][118], Dec 04 2025

a(n) = Sum_{j=1..n} gcd(j, n) cos(2*Pi*j/n) = Sum_{j=1..n} gcd(j, n) exp(2*Pi*i*j/n) where i is the imaginary unit. Notice that the Ramanujan's sum c_n(k) := Sum_{j=1..n, gcd(j, n) = 1} exp(2*Pi*i*j*k/n) gives a(n) = Sum_{k|n} k*c_(n/k)(1) = Sum_{k|n} k*mu(n/k). - [Michael Somos][24], May 13 2018

G.f.: x*d/dx(x*d/dx(log(Product_{k>=1} (1 - x^k)^(-mu(k)/k^2)))), where mu(n) = [A008683][35] (n). - [Mamuka Jibladze][113], Sep 20 2018

a(n) = Sum_{d|n} [A007431][119] (d). - [Steven Foster Clark][120], May 29 2019

G.f. A(x) satisfies: A(x) = x/(1 - x)^2 - Sum_{k>=2} A(x^k). - [Ilya Gutkovskiy][121], Sep 06 2019

a(n) >= sqrt(n/2) (Nicolas). - [Hugo Pfoertner][23], Jun 01 2020

a(n) > n/(exp(gamma)*log(log(n)) + 5/(2*log(log(n)))), except for n=223092870 (Rosser, Schoenfeld). - [Hugo Pfoertner][23], Jun 02 2020

From [Bernard Schott][122], Nov 28 2020: (Start)

Sum_{m=1..n} 1/a(m) = [A028415][123] (n)/ [A048049][124] (n) -> oo when n->oo.

Sum_{n >= 1} 1/a(n)^2 = [A109695][125].

Sum_{n >= 1} 1/a(n)^3 = [A335818][126].

Sum_{n >= 1} 1/a(n)^k is convergent iff k > 1.

a(2n) = a(n) iff n is odd, and, a(2n) > a(n) iff n is even. (End) [Actually, a(2n) = 2*a(n) for even n. - [Jianing Song][98], Sep 18 2022]

a(n) = 2*[A023896][127] (n)/n, n > 1. - [Richard R. Forberg][128], Feb 03 2021

From [Richard L. Ollerton][34], May 09 2021: (Start)

For n > 1, Sum_{k=1..n} phi^{(-1)}(n/gcd(n,k))*a(gcd(n,k))/a(n/gcd(n,k)) = 0, where phi^{(-1)} = [A023900][129].

For n > 1, Sum_{k=1..n} a(gcd(n,k))*mu(rad(gcd(n,k)))*rad(gcd(n,k))/gcd(n,k) = 0.

For n > 1, Sum_{k=1..n} a(gcd(n,k))*mu(rad(n/gcd(n,k)))*rad(n/gcd(n,k))*gcd(n,k) = 0.

Sum_{k=1..n} a(gcd(n,k))/a(n/gcd(n,k)) = n. (End)

a(n) = Sum_{d|n, e|n} gcd(d, e)*mobius(n/d)*mobius(n/e) (the sum is a multiplicative function of n by Tóth, and takes the value p^e - p^(e-1) for n = p^e, a prime power). - [Peter Bala][130], Jan 22 2024

Sum_{n >= 1} phi(n)*x^n/(1 + x^n) = x + 3*x^3 + 5*x^5 + 7*x^7 + ... = Sum_{n >= 1} phi(2*n-1)*x^(2*n-1)/(1 - x^(4*n-2)). For the first equality see Pólya and Szegő, problem 71, p. 126. - [Peter Bala][130], Feb 29 2024

a(n) = lim_{k->oo} (n^(k + 1))/ [A000203][131] (n^k). conjectured by [Velin Yanev][132], Dec 04 2024 and proved by [Roman Le Lan][133] Sep 14 2025 [[A000010][134] (p) = p-1, [A000203][131] (p^k) = (p^(k+1)-1)/(p-1), so the conjecture is true if n is prime. - [Vaclav Kotesovec][135], Dec 19 2024]

EXAMPLE

G.f. = x + x^2 + 2*x^3 + 2*x^4 + 4*x^5 + 2*x^6 + 6*x^7 + 4*x^8 + 6*x^9 + 4*x^10 + ...

a(8) = 4 with {1, 3, 5, 7} units modulo 8. a(10) = 4 with {1, 3, 7, 9} units modulo 10. - [Michael Somos][24], Aug 27 2013

From [Eduard I. Vatutin][32], Nov 01 2020: (Start)

The a(5)=4 cyclic Latin squares with the first row in ascending order are:

0 1 2 3 4 0 1 2 3 4 0 1 2 3 4 0 1 2 3 4

1 2 3 4 0 2 3 4 0 1 3 4 0 1 2 4 0 1 2 3

2 3 4 0 1 4 0 1 2 3 1 2 3 4 0 3 4 0 1 2

3 4 0 1 2 1 2 3 4 0 4 0 1 2 3 2 3 4 0 1

4 0 1 2 3 3 4 0 1 2 2 3 4 0 1 1 2 3 4 0

(End)

MAPLE

with(numtheory): [A000010][134]:= phi; [ seq(phi(n), n=1..100) ];

# Alternative:

with(numtheory): phi := proc(n) local i, t1, t2; t1 := ifactors(n)[2]; t2 := n*mul((1-1/t1[i][1]), i=1..nops(t1)); end;

# Alternative: without library function

A000010List := proc(N) local i, j, phi;

phi := Array([seq(i, i = 1 .. N+1)]);

for i from 2 to N + 1 do

if phi[i] = i then

for j from i by i to N + 1 do

phi[j] := phi[j] - iquo(phi[j], i) od

fi od;

return phi end:

A000010List(68); # [Peter Luschny][136], Sep 03 2023

MATHEMATICA

Array[EulerPhi, 70]

PROG

(Axiom) [eulerPhi(n) for n in 1..100]

(Magma) [ EulerPhi(n) : n in [1..100] ]; // Sergei Haller (sergei(AT)sergei-haller.de), Dec 21 2006

(PARI) {a(n) = if( n==0, 0, eulerphi(n))}; /* [Michael Somos][24], Feb 05 2011 */

(SageMath) def [A000010][134] (n): return euler_phi(n) # [Jaap Spies][137], Jan 07 2007

(SageMath) [euler_phi(n) for n in range(1, 70)] # [Zerinvary Lajos][138], Jun 06 2009

(Maxima) makelist(totient(n), n, 0, 1000); /* [Emanuele Munarini][139], Mar 26 2011 */

(Haskell) a n = length (filter (==1) (map (gcd n) [1..n])) -- [Allan C. Wechsler][140], Dec 29 2014

(Python)

from sympy.ntheory import totient

print([totient(i) for i in range(1, 70)]) # [Indranil Ghosh][141], Mar 17 2017

(Python) # Note also the implementation in [A365339][142].

(Julia) # Computes the first N terms of the sequence.

function A000010List(N)

phi = [i for i in 1:N + 1]

for i in 2:N + 1

if phi[i] == i

for j in i:i:N + 1

phi[j] -= div(phi[j], i)

end end end

return phi end

println(A000010List(68)) # [Peter Luschny][136], Sep 03 2023

CROSSREFS

Cf. [A002088][94] (partial sums), [A008683][35], [A003434][143] (steps to reach 1), [A007755][144], [A049108][145], [A002202][146] (values), [A011755][147] (Sum k*phi(k)).

Cf. also [A005277][148] (nontotient numbers). For inverse see [A002181][149], [A006511][150], [A058277][151].

Jordan function J_k(n) is a generalization - see [A059379][152] and [A059380][153] (triangle of values of J_k(n)), this sequence (J_1), [A007434][27] (J_2), [A059376][28] (J_3), [A059377][29] (J_4), [A059378][154] (J_5).

Cf. [A054521][155], [A023022][16], [A054525][156].

Row sums of triangles [A134540][157], [A127448][158], [A143239][159], [A143353][160] and [A143276][161].

Equals right and left borders of triangle [A159937][162].

Values for prime powers p^e: [A006093][163] (e=1), [A036689][164] (e=2), [A135177][165] (e=3), [A138403][166] (e=4), [A138407][167] (e=5), [A138412][168] (e=6).

Values for perfect powers n^e: [A002618][169] (e=2), [A053191][170] (e=3), [A189393][171] (e=4), [A238533][172] (e=5), [A306411][173] (e=6), [A239442][174] (e=7), [A306412][175] (e=8), [A239443][176] (e=9).

Cf. [A003558][111], [A135303][110].

Cf. [A152455][177], [A080737][178].

Cf. [A076479][179].

Cf. [A023900][129] (Dirichlet inverse of phi), [A306633][180] (Dgf at s=3).

Sequence in context: [A080737][178] [A152455][177] [A293484][181] * [A372681][182] [A372677][183] [A003978][184]

Adjacent sequences: [A000007][185] [A000008][186] [A000009][187] * [A000011][188] [A000012][189] [A000013][190]

KEYWORD

easy, core, nonn, mult, nice, [hear][7], changed

AUTHOR

[N. J. A. Sloane][191]

STATUS

approved

[Lookup][3] [Welcome][192] [Wiki][193] [Register][194] [Music][195] [Plot 2][196] [Demos][197] [Index][198] [WebCam][199] [Contribute][200] [Format][201] [Style Sheet][202] [Transforms][203] [Superseeker][204] [Recents][205]

[The OEIS Community][206]

Maintained by [The OEIS Foundation Inc.][207]

Last modified August 14 12:19 EDT 2026. Contains 398312 sequences.

[License Agreements, Terms of Use, Privacy Policy][208]


## Links

[1]: /login?redirect=%2fA000010
[2]: http://oeisf.org/#DONATE
[3]: /
[4]: /A000010/list
[5]: /A000010/graph
[6]: /search?q=A000010+-id:A000010
[7]: /A000010/listen
[8]: /history?seq=A000010
[9]: /search?q=id:A000010&fmt=text
[10]: /A000010/internal
[11]: /A013595
[12]: /wiki/User:Benoit_Cloitre
[13]: /wiki/User:Lekraj_Beedassy
[14]: /wiki/User:Steven_Finch
[15]: /wiki/User:Alexander_Adamchuk
[16]: /A023022
[17]: /wiki/User:Benoit_Jubin
[18]: /wiki/User:Fred_Lunnon
[19]: /wiki/User:Lei_Zhou
[20]: /wiki/User:Gary_Detlefs
[21]: /wiki/User:Alexander_R._Povolotsky
[22]: /A336334
[23]: /wiki/User:Hugo_Pfoertner
[24]: /wiki/User:Michael_Somos
[25]: /wiki/User:Eric_Desbiaux
[26]: /A054533
[27]: /A007434
[28]: /A059376
[29]: /A059377
[30]: /wiki/User:Roger_Ford
[31]: /wiki/User:Felix_Flicker
[32]: /wiki/User:Eduard_I._Vatutin
[33]: /wiki/User:Rémy_Sigrist
[34]: /wiki/User:Richard_L._Ollerton
[35]: /A008683
[36]: /A018804
[37]: /A067911
[38]: /wiki/User:Radoslaw_Zak
[39]: /A000010/b000010.txt
[40]: https://www.convertit.com/Go/ConvertIt/Reference/AMS55.ASP
[41]: https://www.alpertron.com.ar/ECM.HTM
[42]: https://www.jjj.de/fxt/#fxtbook
[43]: https://www.bibmath.net/dico/index.php?action=affiche&amp;quoi=./i/indicateureuler.html
[44]: https://www.cut-the-knot.org/blue/Euler.shtml
[45]: https://t5k.org/glossary/page.php?sort=EulersPhi
[46]: /A002180/a002180.pdf
[47]: https://math.dartmouth.edu/~carlp/iterate.pdf
[48]: /A000010/a000010_1.pdf
[49]: https://arxiv.org/pdf/math/9907204
[50]: https://arxiv.org/pdf/1108.3805
[51]: /A000010/a000010_3.pdf
[52]: https://arxiv.org/pdf/2607.24832
[53]: https://web.archive.org/web/20150910232858/http://www.uni-graz.at/~fripert/fga/k1euler.html
[54]: https://cs.uwaterloo.ca/journals/JIS/VOL6/Gewurz/gewurz5.html
[55]: https://psychedelic-geometry.blogspot.com/2010/07/totient-carnival.html
[56]: https://arxiv.org/pdf/1201.3139
[57]: https://doi.org/10.1090/S0025-5718-69-99858-5
[58]: https://people.csail.mit.edu/meyer/mcs.pdf
[59]: https://projecteuclid.org/journals/bulletin-of-the-american-mathematical-society-new-series/volume-26/issue-3/Dicksons-History-of-the-Theory-of-Numbers/bams/1183425137.full
[60]: https://rorolelan.wordpress.com/wp-content/uploads/2025/09/theorem.pdf
[61]: https://oeis.org/wiki/User:Peter_Luschny/EulerTotient
[62]: /A000010/a000010_2.pdf
[63]: https://math.stackexchange.com/questions/301837/is-the-euler-phi-function-bounded-below
[64]: https://web.archive.org/web/20200729151301/http://mathforum.org/library/drmath/view/51541.html
[65]: http://www.numbertheory.org/php/factor.html
[66]: https://web.archive.org/web/20130508193928/http://2000clicks.com/MathHelp/NumberFactorsTotientFunction.aspx
[67]: https://arxiv.org/pdf/0806.2068
[68]: https://oeis.org/A000010/a000010_5M.7z
[69]: https://math.dartmouth.edu/~carlp/uupaper7.pdf
[70]: https://primefan.tripod.com/Phi500.html
[71]: https://web.archive.org/web/20170406154901/http://www.mathematik.uni-stuttgart.de/~riedelmo/combnumth.html
[72]: https://doi.org/10.1215/ijm/1255631807
[73]: https://planetmath.org/eulerphifunction
[74]: http://matwbn.icm.edu.pl/ksiazki/mon/mon42/mon4206.pdf
[75]: /A115004/a115004.txt
[76]: https://arxiv.org/pdf/2301.03149
[77]: https://web.archive.org/web/20110823215228/http://home.earthlink.net/~usondermann/eulertot.html
[78]: https://wstein.org/edu/Fall2001/124/lectures/lecture6/html/node3.html
[79]: https://cs.uwaterloo.ca/journals/JIS/VOL21/Laohakosol/lao8.html
[80]: https://arxiv.org/pdf/1310.7053
[81]: http://villemin.gerard.free.fr/Wwwgvmm/Nombre/TotEuler.htm
[82]: /A002180/a002180_1.pdf
[83]: https://mathworld.wolfram.com/ModuloMultiplicationGroup.html
[84]: https://mathworld.wolfram.com/MoebiusTransform.html
[85]: https://mathworld.wolfram.com/TotientFunction.html
[86]: https://en.wikipedia.org/wiki/Euler%27s_totient_function
[87]: https://en.wikipedia.org/wiki/Multiplicative_group_of_integers_modulo_n
[88]: https://en.wikipedia.org/wiki/Ramanujan%27s_sum
[89]: https://functions.wolfram.com/NumberTheoryFunctions/EulerPhi/03/02/
[90]: https://wims.univ-cotedazur.fr/wims/en_tool~number~calcnum.en.html
[91]: /index/Cor#core
[92]: /index/Di#divseq
[93]: /wiki/User:David_W._Wilson
[94]: /A002088
[95]: /wiki/User:Henry_Bottomley
[96]: /A000217
[97]: /wiki/User:Jon_Perry
[98]: /wiki/User:Jianing_Song
[99]: /A335319
[100]: /wiki/User:Enrique_Pérez_Herrero
[101]: /A001157
[102]: /A007425
[103]: /A007947
[104]: /A173557
[105]: /A003557
[106]: /wiki/User:R._J._Mathar
[107]: /A096396
[108]: /A096397
[109]: /wiki/User:Reinhard_Zumkeller
[110]: /A135303
[111]: /A003558
[112]: /wiki/User:Gary_W._Adamson
[113]: /wiki/User:Mamuka_Jibladze
[114]: /A051953
[115]: /wiki/User:Omar_E._Pol
[116]: /wiki/User:Mats_Granvik
[117]: /wiki/User:Benedict_W._J._Irwin
[118]: /wiki/User:Sela_Fried
[119]: /A007431
[120]: /wiki/User:Steven_Foster_Clark
[121]: /wiki/User:Ilya_Gutkovskiy
[122]: /wiki/User:Bernard_Schott
[123]: /A028415
[124]: /A048049
[125]: /A109695
[126]: /A335818
[127]: /A023896
[128]: /wiki/User:Richard_R._Forberg
[129]: /A023900
[130]: /wiki/User:Peter_Bala
[131]: /A000203
[132]: /wiki/User:Velin_Yanev
[133]: /wiki/User:Roman_Le_Lan
[134]: /A000010
[135]: /wiki/User:Vaclav_Kotesovec
[136]: /wiki/User:Peter_Luschny
[137]: /wiki/User:Jaap_Spies
[138]: /wiki/User:Zerinvary_Lajos
[139]: /wiki/User:Emanuele_Munarini
[140]: /wiki/User:Allan_C._Wechsler
[141]: /wiki/User:Indranil_Ghosh
[142]: /A365339
[143]: /A003434
[144]: /A007755
[145]: /A049108
[146]: /A002202
[147]: /A011755
[148]: /A005277
[149]: /A002181
[150]: /A006511
[151]: /A058277
[152]: /A059379
[153]: /A059380
[154]: /A059378
[155]: /A054521
[156]: /A054525
[157]: /A134540
[158]: /A127448
[159]: /A143239
[160]: /A143353
[161]: /A143276
[162]: /A159937
[163]: /A006093
[164]: /A036689
[165]: /A135177
[166]: /A138403
[167]: /A138407
[168]: /A138412
[169]: /A002618
[170]: /A053191
[171]: /A189393
[172]: /A238533
[173]: /A306411
[174]: /A239442
[175]: /A306412
[176]: /A239443
[177]: /A152455
[178]: /A080737
[179]: /A076479
[180]: /A306633
[181]: /A293484
[182]: /A372681
[183]: /A372677
[184]: /A003978
[185]: /A000007
[186]: /A000008
[187]: /A000009
[188]: /A000011
[189]: /A000012
[190]: /A000013
[191]: /wiki/User:N._J._A._Sloane
[192]: /wiki/Welcome
[193]: /wiki/Main_Page
[194]: /wiki/Special:RequestAccount
[195]: /play.html
[196]: /plot2.html
[197]: /demo1.html
[198]: /wiki/Index_to_OEIS
[199]: /webcam
[200]: /Submit.html
[201]: /eishelp2.html
[202]: /wiki/Style_Sheet
[203]: /transforms.html
[204]: /ol.html
[205]: /recent
[206]: /community.html
[207]: http://oeisf.org
[208]: /wiki/Legal_Documents
