<!-- source: https://ddd.uab.cat/pub/artpub/2001/110469/extmat_a2001v16n3p441.pdf | converted from PDF -->

E extracta mathematicae Vol. 16, N´um. 3, 441 – 447 (2001)

Polynomial Systems: a Lower Bound for the
Weakened 16th Hilbert Problem

Chengzhi Li 1, Weigu Li 1, Jaume Llibre 2, Zhifen Zhang 1

1 Department of Mathematics, Peking University, Beijing 100871, China

2 Dept. de Matem`atiques, Universitat Aut`onoma de Barcelona, 08193 Bellaterra, Spain

(Research paper)

AMS Subject Class. (2000): 58F14, 58F21, 34C05 Received June 6, 2001

In this paper we provide the greatest lower bound about the number of
(non–inﬁnitesimal) limit cycles surrounding a unique singular point for a pla-
nar polynomial diﬀerential system of arbitrary degree.

We prove that for m and n odd the maximum number bm,n of isolated
zeros (taking into account their multiplicity) of the Abelian integral I(h) =∫

H(x,y)=h y ¯Q(x, y)dx, where H(x, y) = 1
2 y2 + 1
m+1 xm+1, and ¯Q and arbitrary
polynomial of degree at most n − 1 is

(n + 1)(n + 3)
8 − 1 if n ≤ m , (m + 1)(2n − m + 3)
8 − 1 if n ≥ m .

Moreover, there are perturbations of the Hamiltonian system ˙x = −∂H/∂y,
˙y = ∂H/∂x, such that the indicated maximum number bm,n of continuous
families of limit cycles can be made to emerge from a corresponding number of
arbitrarily prescribed periodic orbits within the period annulus of the center.
Consequently,
 bm,n ≤ N (m, n) ≤ Hmax{m,n} .

This result provides the greatest lower bound about the number of (non–
inﬁnitesimal) limit cycles surrounding a unique singular point for a planar
polynomial diﬀerential system of arbitrary degree m = n.

441

442 c. li, w. li, j. llibre, z. zhang

1. Introduction and the main result

We consider two–dimensional diﬀerential systems

˙x = P (x, y) , ˙y = Q(x, y) , (1)

where P and Q are real polynomials in the variables x and y. In his address
to the International Congress of Mathematics in Paris in 1900, Hilbert raised
the question of the number of limit cycles of these diﬀerential systems. It
remains one of the most diﬃcult open questions in the qualitative theory of
planar polynomial diﬀerential systems.
Let Hm be the maximum possible number of limit cycles of (1) when P
and Q are of degree at most m. The Hm are the Hilbert numbers, and it is still
an open problem whether Hm is ﬁnite, even for the simplest case of quadratic
polynomial diﬀerential systems (m = 2). Probably the best result in that
direction has been the proof of Dulac’s Conjecture by Il’yashenko [14] and
Ecalle [9] using diﬀerent methods. This result states that a given polynomial
system cannot have inﬁnitely many limit cycles. Note that this does not imply
that the Hm are ﬁnite.
On the other hand there has been some success in ﬁnding lower bounds
for Hm. Thus it is known that H2 ≥ 4 (see Shi [27]) and H3 ≥ 11 (see Li and
Li [16]). Several authors have established that Hm grows at least as fast as
m2 with m. Thus, Il’yashenko [13] proved that

Hm ≥ 1
2 (
m2 + m − 2
) ;

Basarab–Horwath and Lloyd [2] shown that

Hm ≥ 1
4 (m − 1)(m + 2) ;

Christopher and Lloyd [5] proved that

Hm ≥ 1
2 (m + 1)
2 (log2(m + 1) − 3) + 3m .

In these last three results the limit cycles occur in several nests, i.e., they are
not surrounding a unique singular point.
Let H(x, y) be a real polynomial of degree m + 1, and let P (x, y) and
Q(x, y) be real polynomials of degree at most n. The problem of ﬁnding an

polynomial systems 443

upper bound N (m, n, H, P, Q) for the number of isolated zeros of the Abelian
integrals
 I(h) = ∫

Γh Q(x, y)dx − P (x, y)dy , (2)

where Γh varies in the compact components of H −1(h) is called the weakened
16th Hilbert problem. It was posed by Arnold in [1].
The weakened 16th Hilbert problem is closely related to the problem of
determinating an upper bound for the number of limit cycles of the perturbed
Hamiltonian system

˙x = − ∂H
∂y + εP (x, y) , ˙y = ∂H
∂x + εQ(x, y) , (3)

where 0 < ε << 1. The relationship between both problems comes from the
following two facts:

(i) If I(h∗) = 0 and I ′(h∗) ̸= 0, then there exists a hyperbolic limit cycle
Lh∗ of system (3) such that Lh∗ → Γh∗ as ε → 0; and conversely, if there
exists a hyperbolic limit cycle Lh∗ of system (3) such that Lh∗ → Γh∗
as ε → 0, then I(h∗) = 0.

(ii) The total number of isolated zeros of (2) (taking into account their
multiplicity) is an upper bound for the number of limit cycles of system
(3) with ε > 0 tending to some periodic orbit Γh of system (3) with
ε = 0 when ε → 0.

Khovansky [15] and Varchenko [28] proved independently that N (m, n, H,
P, Q) is ﬁnite, but an explicit expression for N (m, n, H, P, Q) is unknown.
Many authors have contributed to estimate or to give upper bounds for the
numbers N (m, n, H, P, Q), usually they ﬁx H and take arbitrary polynomials
P and Q with n ﬁxed or not. In this last case the upper bounds that they
obtain are linear functions in n; see for instance Bogdanov [3] and [4], Petrov
[24] and [25], Cushman and Sanders [6], Dumortier, Roussarie and Sotomayor
[8], Drachman, van Gils and Zhang [7], Li and Rousseau [20], Gavrilov [10],
Gavrilov and Horozov [11], Horozov and Iliev [12], Li, Llibre and Zhang [17]
and [18], Li and Zhang [21], Novikov and Yakovenko [23], Zholadek [29], ...
Let N (m, n) be the supremum of N (m, n, H, P, Q) when H varies inside
the class of all polynomials of degree at most m + 1, and P and Q vary inside
the class of all polynomials of degree at most n.
This paper is concerned with the rate of growth of N (m, n), and since
N (m, n) ≤ Hmax{m,n} we also provide a lower bound of Hmax{m,n}. Our result
is the following.

444 c. li, w. li, j. llibre, z. zhang

For m odd let H(x, y) = 1
2 y2 + 1
m + 1 x
m+1 , (4)

and let P (x, y) ≡ 0 , Q(x, y) = y ¯Q(x, y) , (5)

be polynomials with degree of ¯Q at most n−1. Then we consider the perturbed
Hamiltonian system
 ˙x = −y , ˙y = xm + εy ¯Q(x, y) . (6)

Theorem. For m and n odd the maximum number bm,n of isolated zeros
(taking into account their multiplicity) of the Abelian integral (2) with H, P
and Q given by (4) and (5) is

(n + 1)(n + 3)
8 − 1 if n ≤ m , (m + 1)(2n − m + 3)
8 − 1 if n ≥ m .

Moreover, there are perturbations of system (6) such that the indicated maxi-
mum number bm,n of continuous families of limit cycles can be made to emerge
from a corresponding number of arbitrarily prescribed periodic orbits within
the period annulus of the center. Consequently,

bm,n ≤ N (m, n) ≤ Hmax{m,n} .

2. Proof of the theorem

The key point in the proof of this theorem is that, by using Green’s The-
orem, we will compute the Abelian integral through a double integral. These
double integrals for system (6) are very easy to compute in comparison with
the usual single Abelian integral. As far as we know this technique applied to
Abelian integrals was used by ﬁrst time in [19]. The proof of the theorem is
given in the next section.
We write the function ¯Q(x, y) of system (6) as follows

¯Q(x, y) = ∑

0≤i+j≤n−1 ai,jx
iyj ,

and a periodic orbit of the unperturbed system (6) for ε = 0 as

H(x, y) = 1
2 y2 + 1
m + 1 x
m+1 = h .

polynomial systems 445

By using Green’s Theorem the Abelian integral (2) goes over to

I(h) = ∫ ∫

H(x,y)≤h
 ∂(y ¯Q)
∂y dxdy

= ∑

0≤i+j≤n−1
 ∫ ∫
H(x,y)≤h(j + 1)ai,jx
iyjdxdy

= ∑

0≤2i+2j≤n−1
(2j + 1)a2i,2j
 ∫ ∫

H(x,y)≤h x2iy2jdxdy

= ∑

0≤2i+2j≤n−1 2a2i,2j
 ∫ ¯x

−¯x x2i (
2h − 2
m + 1 x
m+1)j+ 1
2 dx

= ∑

0≤2i+2j≤n−1 Cijh
αij

where
 ¯x = [(m + 1)h] 1
m+1 ,

x = [(m + 1)h] 1
m+1 y ,

Cij = 2
j+ 3
2 a2i,2j(m + 1) 2i+1
m+1 ∫ 1

−1 y2i (
1 − ym+1)j+ 1
2 dy ,

αij = 2i + 1
m + 1 + j + 1
2 .

We note that the number of αij that appear as exponents in the powers
of h inside the last expression of the Abelian integral I(h) is equal to

(n + 1)(n + 3)
8 if n ≤ m , or to (m + 1)(2n − m + 3)
8 if n ≥ m .

Therefore the Theorem follows.

Acknowledgements

The authors are partially supported by a DGICYT grant number
PB96–1153. Chengzhi Li, Weigu Li and Zhifen Zhang want to thank
to the Centre de Recerca Matem`atica and to the Department of Mathe-
matics of the Universitat Aut`onoma de Barcelona for their support and
hospitality during the period in which this paper was written. They are
partially supported by the NSFC and the DEPT of China.

446 c. li, w. li, j. llibre, z. zhang

References

[1] Arnold, V.I., Loss of stability of self–oscillation close to resonance and
versal deformations of equivariant vector ﬁelds, Funct. Anal. Appl. 11
(1977), 1 – 10.
[2] Basarab–Horwath, P., Lloyd, N.G., Co–existing ﬁne foci and bifur-
cating limit cycles, Neieuw Arch. Wisk. 6 (1988), 295 – 302.
[3] Bogdanov, R.I., Bifurcation of the limit cycle of a family of a planar vector
ﬁelds, Selecta Math. Soviet 1 (1981), 373 – 387.
[4] Bogdanov, R.I., Versal deformation of a singularity of a vector ﬁeld
on the plane in the case of zero eigenvalues, Selecta Math. Soviet 1 (1981),
389 – 421.
[5] Christopher, C.J., Lloyd, N.G., Polynomial systems: a lower bound
for the Hilbert numbers, Proc. Royal Soc. London, Serie A, 450 (1995),
219 – 224.
[6] Cushman, R., Sanders, J.A., A codimension two bifurcation with
a third order Picard–Fuchs equation, J. Diﬀerential Equations 59 (1985),
243 – 256.
[7] Drachman, B., van Gils, S.A., Zhang, Z., Abelian integrals for
quadratic vector ﬁelds, J. Reine Angew. Math. 382 (1987), 165 – 180.
[8] Dumortier, F., Roussarie, R., Sotomayor, J., Generic 3–parameter
families of vector ﬁelds on the plane, unfolding a singularity with nilpotent
linear part. The cusp case, Ergod. Th. & Dyn. Sys. 7 (1987), 375 – 413.
[9] Ecalle, J., “Introduction aux Fonctions Analysables et Preuve Constructive
de la Conjecture de Dulac”, Actualit´es Math´ematiques, Hermann, Paris,
1992.
[10] Gavrilov, L., Abelian integrals related to Morse polynomials and perturba-
tions of plane Hamiltonian vector ﬁelds, preprint (1998).
[11] Gavrilov, L., Horozov, E., Limit cycles and zeros of abelian integrals
satisfying third order Picard–Fuchs equations, in Lect. Notes in Math. 1455,
Springer–Verlag, 1990, pp. 160 – 196.
[12] Horozov, E., Iliev, I.D., On the number of limit cycles in perturba-
tions of quadratic Hamiltonian systems, Proc. London Math. Soc. 69 (1994),
198 – 224.
[13] Il’yashenko, Yu.S., The origin of limit cycles under perturbations of the
equation dw/dz = −Rz/Rw where R(z, w) is a polynomial, Math. USSR–Sb.
7 (1969), 353 – 364.
[14] Il’yashenko, Yu.S., “Finiteness Theorems for Limit Cycles”, Translations
of Mathematical Monographs, Vol. 94, Amer. Math. Soc., Providence, RI,
1991.
[15] Khovansky, A.G., Real analytic manifolds with ﬁniteness properties and
complex Abelian integrals, Funct. Anal. Appl. 18 (1984), 119 – 128.
[16] Jibin, L., Chunfu, L., Global bifurcations of planar disturbed Hamiltonian
systems and distributions of limit cycles of cubic systems, Acta Math. Sinica
28 (1985), 509 – 521.

polynomial systems 447

[17] Li, C., Llibre, J., Zhang, Z., Weak focus, limit cycles and bifurcations
for bounded quadratic systems, J. Diﬀerential Equations 115 (1995),
193 – 223.
[18] Li, C., Llibre, J., Zhang, Z., Abelian integrals of quadratic Hamiltonian
vector ﬁelds with an invariant straight line, Publicacions Matem`atiques 39
(1995), 355 – 366.
[19] Li, C., Li, W., Llibre, J., Zhang, Z., Bifurcation of limit cycles from
quadratic isochronous centers, preprint (1998).
[20] Li, C., Rousseau, C., A system with three limit cycles appearing in a Hopf
bifurcation and dying in a homoclinic bifurcation: The cusp of order 4, J.
Diﬀerential Equations 79 (1989), 132 – 161.
[21] Li, B., Zhang, Z., A note on a result of G.S. Petrov about the weakened
16-th Hilbert problem, J. Math. Anal. Appl. 190 (1995), 489 – 516.
[22] Mardesic, P., The number of limit cycles of polynomials deformations of a
Hamiltonian vector ﬁeld, Ergodic Theory & Dynamical Systems 10 (1990),
523 – 529.
[23] Novikov, D., Yakovenko, S., Simple exponential estimate for the number
of real zeros of complete abelian integrals, Ann. Inst. Fourier 45 (1995),
897 – 927.
[24] Petrov, G.S., Number of zeros of complete elliptic integrals, Funct. Anal.
Appl. 18 (1988), 148 – 149.
[25] Petrov, G.S., The Chebyshev property of elliptic integrals, Funct. Anal.
Appl. 22 (1988), 72 – 73.
[26] Shafer, D.S., Zegeling, A., Bifurcation of limit cycles from quadratic
centers, J. Diﬀerential Equations 122 (1995), 48 – 70.
[27] Songling, S., A concrete example of the existence of four limit cycles for
plane quadratic sytems, Sci. Sinica A23 (1980), 153 – 158.
[28] Varchenko, A.N., Estimate of the number of zeros of an Abelian integral
depending on a parameter and limit cycles, Funct. Anal. Appl. 18 (1984),
98 – 108.
[29] Zoladek, H., Quadratic systems with centers and their perturbations, J.
Diﬀerential Equations 109 (1994), 223 – 273.
