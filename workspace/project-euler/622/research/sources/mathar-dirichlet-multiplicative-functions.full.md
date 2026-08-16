<!-- source: https://arxiv.org/pdf/1106.4038 | converted from PDF -->

arXiv:1106.4038v2  [math.NT]  4 Jul 2012
SURVEY OF DIRICHLET SERIES OF MULTIPLICATIVE
ARITHMETIC FUNCTIONS

RICHARD J. MATHAR

Abstract. The manuscript reviews Dirichlet Series of important multiplica-
tive arithmetic functions. The aim is to represent these as products and ratios
of Riemann ζ-functions, or, if that concise format is not found, to provide the
leading factors of the inﬁnite product over ζ-functions. If rooted at the Dirich-
let series for powers, for sums-of-divisors and for Euler’s totient, the inheritance
of multiplicativity through Dirichlet convolution or ordinary multiplication of
pairs of arithmetic functions generates most of the results.

1. Scope

1.1. Deﬁnition. Multiplicative functions are arithmetic functions a(n)—functions
deﬁned for integer argument n ∈ Z—for which evaluation commutes with multipli-
cation for coprime arguments:

Deﬁnition 1. (Multiplicative function a)

(1.1) a(nm) = a(n)a(m) ∀(n, m) = 1.

The topic of the manuscript is the computation of the Dirichlet series ζD of
arithmetic functions of that kind for suﬃciently large real part of the argument s:

Deﬁnition 2. (Dirichlet generating function ζD)

(1.2) a(n) ↦→ ζD(s) ≡ ∑

n≥1
 a(n)
ns .

As an immediate consequence of the deﬁnition, the ζD of the product of nk times
a multiplicative function a(n) is given by replacing s → s − k in the ζD of a(n):

(1.3) nka(n) ↦→ ζD(s − k).

1.2. Properties. For ease of reference further down, we summarize well-known
features of arithmetic functions.
A consequence of the deﬁnition (1.1) is that the function is already entirely
deﬁned if speciﬁed for prime powers pe, because all remaining values follow by the
prime power factorization of the arguments:

(1.4) a(pe1
1 pe2
2 · · · pem
m ) = ∏

p a(pe).

The equation that explicitly speciﬁes values of a(pe) will be called the master equa-
tion of that sequence in the sequel.

Date: November 26, 2024.
2010 Mathematics Subject Classiﬁcation. Primary 11K65, 11Y70; Secondary 30B50, 11M41.
Key words and phrases. Arithmetic Function, multiplicative, Dirichlet Generating Function.

1

2 RICHARD J. MATHAR

If a is multiplicative, the Dirichlet series reduces to a product over all primes p:
(1.5)

ζD(s) = ∏

p
 (
1 + a(p)
ps + a(p2)
p2s + · · · ) = ∏

p
 

1 + ∑

e≥1
 a(pe)
pes
 

 = ∏

p
 ∑

e≥0
 a(pe)
pes .

This sum over e ≥ 0 at some ﬁxed p will be called the Bell series of that a(n).
The product over the primes p may be a ﬁnite product and/or ratio of cyclotomic
polynomials of some power of p; then it is rephrased as a ﬁnite product of Riemann
zeta-functions. In the general case, this expansion will lead to an inﬁnite product,
and will be represented in the followup chapters in the format

(1.6) ζD(s) = ∏

p
 ∞∏

i=1(1 − Sipli−uis)
γi,

where the vector of the Si contains sign factors ±1, and the li, ui and γi are integers.
The natural order of the factors is smallest ui ﬁrst, and if these are the same largest
li ﬁrst. This order stresses which terms put the tightest constraints on the region
of convergence in the plane of complex s. With Euler’s formula, these constituents
are equivalent to Riemann ζ-functions:

(1.7) ∏

p (1 − pli−uis)
γi = ζ−γi (uis − li); ∏

p (1 + pli−uis)
γi = ζγi (uis − li)
ζγi (2uis − 2li) .

(We write ζD for a generic Dirichlet series and ζ for the Riemann zeta function.)
Truncating the product expansion is a tool of numerical evaluation of the ζD(s).
The diﬀerence of this work to the Gould-Shonhiwa table [15] of the transfor-
mations a(n) ↦→ ζD(s) is that we will (i) cover Dirichlet series which require this
type of inﬁnite Euler products, and (ii) will detail the six-digit A-numbers of indi-
vidual sequences in Sloane’s Online Encylopedia of Integer Sequences (OEIS) [31];
due credit to individual’s discovery of many formulae that follow is stored in this
database.

1.3. Dirichlet convolution. Dirichlet convolution is the construction of a new
series by summation over divisor and complementary divisor arguments of two
arithmetic functions:

Deﬁnition 3. (Dirichlet Convolution of a and b)

(1.8) (a ⋆ b)(n) ≡ ∑

d|n a(d)b(n/d).

The master equation of a multiplicative function derived via Dirichlet convolu-
tion (1.8) is related to the master equations of the factors [35]:

(1.9) (a ⋆ b)(pe) =
 e∑

l=0 a(pl)b(pe−l).

The ordinary (Hadamard) and the Dirichlet (convolution) product of two multi-
plicative functions, the ordinary (Hadamard) ratio of two multiplicative functions,
and the Dirichlet inverse of a multiplicative function are multiplicative [2, 9], which
creates multiplicative function by inheritance from “simpler” multiplicative func-
tions. As a special case, the j−th power of a multiplicative function is multiplicative
and the associated a(pe) is the the j-th power of the one for the ﬁrst power.

DIRICHLET GENERATING FUNCTIONS 3

The Dirichlet series of the Dirichlet product is the (ordinary) product of the
Dirichlet series:

(1.10) a ⋆ b ↦→ ζD,a(s)ζD,b(s).

As a corollary, the Dirichlet series of the Dirichlet inverse deﬁned by (a(−1) ⋆a)(n) ≡
δ1,n is given by the reciprocal Dirichlet series of a:

(1.11) a(−1) ↦→ 1/ζD(s).

2. Classifications

2.1. Completely Multiplicative.

2.1.1. Generic Properties. Completely multiplicative functions are a sub-species of
multiplicative functions which obey the equation (1.1) for argument pairs n and m
irrespective of common divisors:

Deﬁnition 4. (Completely Multiplicative function a)

(2.1) a(nm) = a(n)a(m).

The well-known properties of completely multiplicative functions are that the
Dirichlet inverse can be written as a multiplication with the M¨obius function,

(2.2) a(−1)(n) = µ(n)a(n),

that the master equation allows interchange of exponentiation and evaluation,

(2.3) a(pe) = ae(p),

and that the sum over the exponents e in (1.5) is a geometric series [2],

(2.4) ζD = ∏

p
 1
1 − a(p)p−s .

2.1.2. Powers. The Dirichlet series of powers is obvious from (1.2):

(2.5) nk ↦→ ζ(s − k).

The most important example is the exponent k = 0,

(2.6) 1 ↦→ ζ(s).

Its Dirichlet inverse is the M¨obius function µ(n) (which is not completely multi-
plicative, A008683), with Dirichlet generating function

(2.7) µ(n) ↦→ 1/ζ(s)

obtained combining (1.11) and (2.6). The master equation of µ(n) is

(2.8) a(pe) = { −1, e = 1;
0, e > 1.

Squaring one obtains the Bell series of µ2(n),

(2.9) 1 + ∑

e=1
 1
pes = 1 + p−s = 1 − p−2s

1 − p−s

which will be used further down as

(2.10) µ2(n) ↦→ ζ(s)/ζ(2s).

4 RICHARD J. MATHAR

Remark 1. These nk cover k = 0 in A000012, k = 1 in A000027 with inverse
nµ(n) in A055615, k = 2 in A000290, k = 3 in A000578, k = 4 and 5 in A000583
and A000584, k = 6–9 in A001014–A001017, k = 10–12 in A008454–A008456,
k = 13–25 in A010801–A010813, k = 26 in A089081, k = 27-30 in A122968–
A122971 [31].

2.1.3. Primes to constants. If the master equation of a completely multiplicative
function is

(2.11) a(p) = c,

the Dirichlet series is usually expanded into an Euler product

(2.12) ζD(s) = ∏

p
 1
1 − c/ps = ∏

j≥1(1 − p−s)
γj (c).

for numerical eﬃcienty, such that the Dirichlet generating function becomes an
(inﬁnite) product of the form ∏
j≥1 ζ−γj (c)(s) [27].

Remark 2. For c = 2–11 the γj(c) are A001037, A027376, A027377, A001692,
A032164, A001693, A027380, A027381, A032165, and A032166 in that order.
These exponents appear essentially as γ(C)
r,j in my expansions of Hardy-Littlewood
constants [25, chapt. 7]. In numerical practise, Wynn’s partial-product algorithm is
used to accelerate convergence of the Euler products [37].

The cases of negative c are mapped via

(2.13) ∏

p
 1
1 − cp−s = ∏

p
 1 + cp−s

1 − c2p−2s

to a division of two Hardy-Littlewood constants.

Remark 3. For a ﬁxed integer s, one may factorize the polynomial of 1/p over the
reals numerically, to face a Weierstrass product representation

(2.14) ζD = ∏

p
 ∏

j (1 + βj
pt ).

The number of factors in the j-product is equivalent to the order of the polynomial,
and βj are essentially its roots. Interchange of the two products rewrites ζD as a
ﬁnite product of prime zeta-functions of squarefree k-almost primes [24]:
(2.15)

ζD = ∏

j
 [
1 + βj ∑

p
 1
pt + β2
j ∑

p<q
 1
(pq)t + · · ·
 ]
 = ∏

j
 

1 + ∑

k≥1(−βj)
kP (µ)
k (t)



 .

Remark 4. This covers A061142 and A165872 (c = ±2) and A165824 (c = 3) up
to A165871 (c = 50) [31].

2.1.4. Liouville. The Liouville function λ(n) (A008836) is the parity of the number
Ω(n) of prime divisors of n. The master equation is [30]

(2.16) a(p) = −1,

which evaluates by immediate application of (2.4) to [23]

(2.17) λ(n) = (−1)
Ω(n) ↦→ ζ(2s)/ζ(s),

DIRICHLET GENERATING FUNCTIONS 5

the D-inverse of (2.10). With (1.10) follows that λ ⋆ 1 is the characteristic function
of the squares [30]:

(2.18) λ ⋆ 1 = ǫ2(n) ↦→ ζ(2s).

2.2. Persistently Multiplicative.

2.2.1. Deﬁnition. I call a multiplicative function a persistently multiplicative if a
product of coprime arguments leads to a coprime product of the function,

Deﬁnition 5. (Persistently multiplicative function a)

(2.19) a(nm) = a(n)a(m) and (a(n), a(m)) = 1 ∀(n, m) = 1.

If a persistently multiplicative function g is the inner function of a compositorial
product a(n) = f (g(n)), and if f is multiplicative, then a is also multiplicative.
Persistently multiplicative are for example those multiplicative functions where
master equations only modify the exponent of the prime power through some func-
tion E, a(pe) = pE(e). The important subclass are the powers. This also includes
functions which remove all powers of some ﬁxed prime pj from n, characterized by

(2.20) ζD = ζ(s − 1)(1 − p1−s
j )/(1 − p−s
j ).

Remark 5. Examples with pj = 2, 3 or 5 are A000265, A038502, and A132739.

Other persistently multiplicative functions permute the prime bases p in the
master equation, for example replace primes by their successors (A003961) or swap
with the adjacent prime (A061898).

2.2.2. Squarefree core. Persistently multiplicative are functions that reduce n to its
squarefree (t = 2), cubefree (t = 3) etc cores, where E(e) = e mod t is a modulo
function which partitions e into periodically modulated classes. The function which
reduces n to the t-free core has the Bell series

(2.21)
 t−1∑

r=0
 ∑

e=r,r+t,r+2t,...
 pr

pes =
 t−1∑

r=0
 ∞∑

j=0
 pr

p(r+jt)s = 1 − pt(1−s)

(1 − p−ts)(1 − p1−s)

and therefore with (1.7) the generating function

(2.22) coret(n) ↦→ ζ(ts)ζ(s − 1)/ζ(ts − t).

Remark 6. This concerns sequences A007913 (squarefree), A050985 (cubefree)
and A053165 (4-free).

2.2.3. Largest t-free Divisor. The largest t-free number dividing n, radt(n), is com-
plementary to the functionality of the previous subsection. The master equation
admits exponents limited by t and by the exponent in n:

(2.23) a(pe) = pmin(e,t−1).

The Bell series is

(2.24)
 t−1∑

e=0
 pe

pes + ∑

e≥t
 pt−1

pes = 1 − p−s − pt(1−s) + pt(1−s)−1

(1 − p−s)(1 − p1−s)

= (1 − p−s) ∑t−2
l=0 p(1−s)l + p(1−s)(t−1)

1 − p−s .

6 RICHARD J. MATHAR

The denominator contributes ζ(s) to the Dirichlet series. For t = 2, the Euler
expansion of the numerator starts:

(2.25) ∏

p (1 + p1−s − p−s) = ∏

p (1 + p1−s)(1 − p−s)(1 + p1−2s)(1 − p2−3s)

× (1 + p1−3s)(1 + p3−4s)(1 − p2−4s)(1 + p1−4s)(1 − p4−5s)(1 + p3−5s)
2

× (1 − p2−5s)
2(1 + p1−5s) · · · , s > 2.

Remark 7. The cases t = 2–3 are shown in A007947–A007948, the case t = 4 in
A058035. 1 ⋆ rad2 is A191750.

2.2.4. Even-odd Splitting. Persistently multiplicative are the functions that assign
1 to all odd arguments and some other values to even arguments. A fundamental
example maps all even arguments to some constant c, which creates an arithmetic
sequence of period length 2:

(2.26) a(pe) = { c, p = 2;
1, p > 2;
 } ↦→ [1 + (c − 1) · 2−s]ζ(s).

In a variant, multiples of 4 could be assigned to some constant c1, the other even
arguments to another constant c2:

(2.27) a(n) =
 



 1, n odd
c1, n ≡ 0 mod 4
c2, n ≡ 2 mod 4
 


 ↦→ [1 + (c2 − 1) · 2−s + (c1 − c2) · 4−s]ζ(s).

These periodic functions are additive overlays of L-series [26, 7]. The computational
strategy usually involves subtracting the Riemann ζ-function, expansion of the
remaining a(n) − 1 into a discrete Fourier series, and writing each component as a
Hilbert zeta-function.

Remark 8. This applies to A109008 (c1 = 4, c2 = 2), A010121 (c1 = 4, c2 = 1),
A010123 (c1 = 6, c2 = 2), A010130 (c1 = 10, c2 = 1), A010131 (c1 = 10, c2 = 2),
A010137 (c1 = 12, c2 = 5), A010146 (c1 = 14, c2 = 6), A112132 (c1 = 7, c2 = 3),
A010127 (c1 = 8, c2 = 3), A089146 (c1 = 4, c2 = 8), or A010132 (c1 = 10, c2 = 4).

3. Core Classes

3.1. Characteristic Function of t-th powers. The characteristic function ǫt(n)
of the t-th powers equals 1 if the argument is a t-th power of some positive integer
b, 0 otherwise [35]. The Dirichlet generating function (1.2) collects 1/bts summing
over all b ≥ 1:

(3.1) ǫt(n) ↦→ ζ(ts).

The application of (1.3) with (2.5) yields

(3.2) nk/2ǫ2(n) ↦→ ζ(2s − k).

Remark 9. √
nǫ2(n) is A037213.

The characteristic function of the numbers which are t-free (which cannot be
divided by a non-trivial t-th power) shall be denoted ξt(n). The master equation
puts a cap on the maximum power admitted in each factor:

(3.3) a(pe) = { 1, e < t;
0, e ≥ t.

DIRICHLET GENERATING FUNCTIONS 7

The Bell series is

(3.4)
 t−1∑

e=0 1/pes = 1 − p−st

1 − p−s ,

therefore

(3.5) ξt(n) ↦→ ζ(s)/ζ(st)

and [35]

(3.6) ξt(n) ⋆ ǫt(n) = 1.

Remark 10. The case t = 2 comprises µ2(n), the characteristic function of square-
free integers (A008966) [30], the D-inverse of (2.17). The derived nξ2(n) is repre-
sented by the absolute values of A055615.

3.2. Depleted ζ-functions. Characteristic functions of numbers which are not
multiples of some prime power qk are multiplicative with

(3.7) a(pe) =
 



 1, if p ̸= q;
1, if p = q, e < k;
0, if p = q, e ≥ k.

The Bell series is 1/(1 − p−s) for all p ̸= q and ∑k−1
e=0 1/pes = (1 − p−sk)(1 − p−s)
for p = q. The merger of both is

(3.8) δqk∤n ↦→ (1 − q−sk)ζ(s).

Remark 11. Examples are qk = 21 in A000035, 22 in A166486, 23 in A168181, 31

in A011655 (multiplied by n in A091684), 32 in A168182, 51 in A011558 (multiplied
by n in A091703), 71 in A109720, 111 in A145568, or any principal Dirichlet
character modulo some prime.

3.3. Greatest Common Divisors. The greatest common divisor (n, c) with re-
spect to a constant c is periodic (n + c, c) = (n, c) [2, §8.1] and multiplicative.
(Periodicity is revealed by the Euclidean algorithm which starting from n + c on
one hand or c on the other yields the same quotients and remainders already after
the ﬁrst step of the algorithm.)
Let c = ∏

p pec specify the prime exponents of the constant; then the master
equation is

(3.9) a(pe) = pmin(e,ec).

The Bell series is again an exercise in geometric series [16, 0.113][20],

(3.10)
 ec∑

e=0
 pe

pes + ∑

e>ec
 pec

pes = 1 − p−s + pecp−(ec+1)s(1 − p)
(1 − p−s)(1 − p1−s) .

The product over all primes, the Dirichlet series, is the Riemann ζ-function mul-
tiplied by a product of rational polynomials over the primes with non-vanishing
ec:

(3.11) (n, c) ↦→ ζ(s) ∏

ec >0
 1 − p−s + pecp−(ec+1)s(1 − p)
1 − p1−s

= ζ(s) ∏

ec>0
 (

1 + (p − 1)
 ec−1∑

l=0 pl(1−s)−s)
 .

8 RICHARD J. MATHAR

Remark 12. The reference sequences are A109007–A109015 for c =3–12 in the
OEIS [31], with the exception of c = 6 which is A089128.

3.4. Least Common Multiples. The least common multiple [n, c] of n and a
constant c is constructed with the master equation a(pe) = pmax(e,ec) but is not
multiplicative in general. With (n, c)[n, c] = nc and multiplicativity of (n, c), the
divided [n, c]/c = n/(n, c) serves as a multiplicative substitute. The master equa-
tion of [n, c]/c is

(3.12) a(pe) = pmax(e,ec)/pec = pmax(e−ec,0).

The Bell series is

(3.13)
 ec∑

e=0
 1
pes + ∑

e>ec
 pe−ec

pes = 1 − p1−s + p−s(1+ec)(p − 1)
(1 − p−s)(1 − p1−s) .

The analog of (3.11) becomes

(3.14) [n, c]/c ↦→ ζ(s − 1) ∏

ec>0
 (

1 + (1 − p)
 ec−1∑

l=0 p−(l+1)s)
 .

Remark 13. This refers for c = 2–20 to A026741, A051176, A060819, A060791,
A060789, A106608–A106612, A051724, and A106614–A106621.

3.5. Sigma: Sum of Divisors.

3.5.1. Base Sequence. The divisors of some number n

(3.15) n = ∏

p pei
i

are of the form d = ∏
p pmi
i with 0 ≤ mi ≤ ei. The sum of the k-th power of
divisors is

(3.16) σk(n) = (1 + pk
1 + p2k
1 + · · · pe1k
1 )(1 + pk
2 + p2k
2 + · · · pe2k
2 ) · · ·

which is a product of geometric sums [17, p. 239]:

(3.17) σk(pe) =
 { p
k(e+1)−1
pk−1 , k > 0;
e + 1, k = 0.

Inserted into (1.5) provides the Dirichlet series

(3.18) ζD = ∏

p
 


∑

e≥0
 pk(e+1) − 1
pk − 1 · 1
pes
 

 , k > 0,

and the geometric series is summarized as [33, (1.3.1)][14, p. 293]

(3.19) σk(n) ↦→ ζ(s)ζ(s − k), k ≥ 0.

In view of (1.8) and (2.5) this shows

(3.20) σk(n) = nk ⋆ 1.

Remark 14. This covers k = 0, 1⋆1 = σ0(n), in A000005 with D-inverse A007427,
k = 1 in A000203 with D-inverse A046692, k = 2 in A001157 with D-inverse
A053822, k = 3 in A001158 with D-inverse A053825, k = 4 in A001159 with D-
inverse A053826, k = 5 in A001160 with D-inverse A178448, and k = 6–24 in
A013954–A013972.
 DIRICHLET GENERATING FUNCTIONS 9

The sum over the inverse k-th powers deals with negative indices of the σ-
function. By inspection of the complementary divisors n/d for each d this is

(3.21) σ−k(n) = ∑

d|n
 1
dk = σk(n)
nk .

Applying the shift-theorem (1.3) demonstrates that (3.19) is also valid in the range
k < 0.

3.5.2. Convolutions. With (3.19) we derive for example σ1(n) ⋆ 1 ↦→ ζ2(s)ζ(s − 1)
(A007429), σ0(n) ⋆ σ1(n) ↦→ ζ3(s)ζ(s − 1) (A007430), σ2(n) ⋆ 1 ↦→ ζ2(s)ζ(s − 2)
(A007433) or σ1(n) ⋆ σ1(n) ↦→ ζ2(s)ζ2(s − 1) (A034761).

3.6. Sums of Divisors which are t-th Powers. The sum over all divisors of n
which are perfect t−th powers is

(3.22) a(n) = ∑

d|n dǫt(d) = nǫt(n) ⋆ 1 ↦→ ζ(s)ζ(ts − t)

using the notation of the characteristic function ǫt (Section 3.1).

Proof. The Dirichlet generating function in (3.22) is derived (i) either by summing
the Bell series and noting that the denominators of the intermediate result are
cyclotomic polynomials of p−s which allows to express the Euler product as a ﬁnite
product of ζ-functions, or (ii) more quickly starting from the generating function
(3.1) of ǫt(n), using the shift theorem (1.3) to produce the generating function for
nǫt(n),

(3.23) nǫt(n) ↦→ ζ(ts − t)

and exploiting the convolution with 1 via (1.10) and (2.6). □

Remark 15. The examples are t = 2, the sums of the square divisors (A035316),
and t = 3, the sum of the cube divisors (A113061).

The master equation is

(3.24) a(pe) =
 ⌊e/t⌋∑

l=0 plt = pt(1+⌊e/t⌋) − 1
pt − 1

which can be made more explicit by writing this down for each remainder of e
mod t in the style of (2.21).
The largest t-th power dividing n = ∏
p pe may be written as maxbt|n. For each
prime basis p it selects the maximum exponent e which is a multiple of t. This
reduces the sum (3.24) over all multiples to its largest term:

(3.25) a(pe) = pt⌊e/t⌋

Substituting e = kt + r in the Bell series yields
(3.26)

1 + ∑

e≥1
 pe−r

pes =
 t−1∑

r=0
 ∑

k≥0
 pkt

p(kt+r)s =
 t−1∑

r=0 p−rs 1
1 − pt(1−s) = 1 − p−st

(1 − p−s)(1 − pt(1−s)) .

The product over all primes is

(3.27) max
bt|n ↦→ ζ(s)ζ(ts − t)/ζ(st).

10 RICHARD J. MATHAR

Multiplying this ζ-product by (2.22) shows in conjunction with (1.10) and (3.19)
that

(3.28) max
bt|n ⋆ coret(n) = σ1(n).

Remark 16. Examples are t = 2, the largest square dividing n (A008833), t = 3,
the largest cube dividing n (A008834), or t = 4, the largest 4th power dividing n
(A008835).

One can also split the product in view of (3.23) and (3.5),

(3.29) max
bt|n = ξt(n) ⋆ (nǫt(n)).

A similar function is the t-th root of the largest t-th power dividing n,

(3.30) a(pe) = p⌊e/t⌋,

pulling the t-th root out of (3.25). Bell and Dirichlet series are
(3.31)
∑

e≥0
 p⌊e/t⌋

pes =
 t−1∑

r=0
 ∑

k≥0
 pk

p(kt+r)s = 1 − p−st

(1 − p−s)(1 − p1−st) ↦→ ζ(st − 1)ζ(s)/ζ(st).

Remark 17. This theory applies to A000118 (t = 2), A053150 (t = 3) and
A053164 (t = 4).

3.7. Sum of t-free Divisors. The sum of the k-th powers of t-free divisors of n
is —in the notation of section 3.1—

(3.32) ∑

d|n d
kξt(d) = (nkξt(n)) ⋆ 1 ↦→ ζ(s)ζ(s − k)/ζ(ts − tk), k ≥ 0.

This Dirichlet series follows applying (1.3) to (3.5) and then (2.6) and (1.10).

Remark 18. The count of the squarefree divisors is A034444 with D-inverse in
A158522; the count of the cubefree divisors is A073184. The sum of squarefree
divisors (A048250) has the master equation

(3.33) a(pe) = p + 1.

Multiplication by n generates A181797. The sum of the cubefree divisors is A073185.

The count of the t-full divisors has the master equation [32]

(3.34) a(pe) = max(1, e − t + 2),

assuming 1 is included in the set of t-full numbers. Compared to the full count of
divisors, this eliminates contributions of the powers p1, p2,. . . ,pt−1 from the prime
factorization of the divisors. The Bell series is

(3.35)
 t−1∑

e=0
 1
pes + ∑

e≥t
 e − t + 2
pes = p−st − p−s + 1
(1 − p−s)2 .

For t = 2, the numerator polynomial is the cyclotomic polynomial Φ6(p−s), and
expansion of numerator and denominator with 1 + p−s yields

(3.36) ∑

d:ξ2(d)=0 1 ↦→ ζ(s)ζ(2s)ζ(3s)/ζ(6s).

DIRICHLET GENERATING FUNCTIONS 11

For t = 3 and t = 4 the inﬁnite Euler products start as
(3.37)∑

d:ξ3(d)=0 1 ↦→ ζ(s) ∏

p (1 + p−3s)(1 + p−4s)(1 + p−5s)(1 + p−6s)(1 − p−9s) · · · , s > 1,

and
(3.38)∑

d:ξ4(d)=0 1 ↦→ ζ(s) ∏

p (1+p−4s)(1+p−5s)(1+p−6s)(1+p−7s)(1+p−8s)(1−p−11s) · · · , s > 1.

Remark 19. t = 2 is A005361. t = 3 is A190867.

3.8. Sigma of powers. σk(n2) is an arithmetic function with master equation
obtained by the substitution e → 2e in (3.17):

(3.39) a(pe) = pk(2e+1) − 1
pk − 1 , k > 0; a(pe) = 2e + 1, k = 0.

The Bell series is

(3.40) ∑

e≥0
 pk(2e+1) − 1
(pk − 1)pes = 1 + pk−s

(1 − p2k−s)(1 − p−s) , k ≥ 0,

which induces

(3.41) σk(n2) ↦→ ζ(s)ζ(s − k)ζ(s − 2k)/ζ(2s − 2k).

If the right hand side is interpreted as the product of ζ(s)ζ(s − 2k) and ζ(s −
k)/ζ(2s − 2k), equations (3.5) and (3.19) demonstrate

(3.42) σk(n2) = σ2k(n) ⋆ (nkξ2(n)).

An alternative interpretation as a product of ζ(s − 2k) and ζ(s)ζ(s − k)/ζ(2s − 2k)
shows with (3.32)

(3.43) σk(n2) = [∑

d|n d
kξ2(d)] ⋆ n2k.

Remark 20. The case σ0(n2) in A048691 is documented by Titchmarsh [33, (1.2.9)]
with σ0(n2) ↦→ ζ3(s)/ζ(2s). σ1(n2) is A065764, and σ2(n2) is A065827.

Moving on to higher powers in the argument, subsampled sums of divisors, we
ﬁrst meet σ0(nt) with Bell series

(3.44) 1 + ∑

e≥1
 te + 1
pes = 1 + (t − 1)p−s

(1 − p−s)2 .

The denominator contributes a factor ζ2(s) to the Dirichlet series, and the numer-
ator is covered by division through the associated term of (2.12).
The master equation of σ1(nt) replaces e by et in (3.17),

(3.45) a(pe) = pet+1 − 1
p − 1 ,

which generates a Bell series

(3.46) 1 + ∑

e≥1
 pte+1 − 1
(p − 1)pes = 1 + p1−s ∑t−2
l=0 pl

(1 − p−s)(1 − pt−s) .

12 RICHARD J. MATHAR

At t = 3, the Euler expansion starts

(3.47) σ1(n3) ↦→ ζ(s)ζ(s − 3) ∏

p (1 + p2−s)(1 + p1−s)(1 − p3−2s)(1 + p5−3s)

× (1 + p4−3s)(1 − p7−4s)(1 − p6−4s)(1 − p5−4s)(1 + p9−5s)

× (1 + p8−5s)
2(1 + p7−5s)
2(1 + p6−5s) · · · , s > 4,

for example. At t = 4 it is

(3.48) σ1(n4) ↦→ ζ(s)ζ(s − 4) ∏

p (1 + p3−s)(1 + p2−s)(1 + p1−s)(1 − p5−2s)

× (1 − p4−2s)(1 − p3−2s)(1 + p8−3s)(1 + p7−3s)
2(1 + p6−3s)
2

× (1 + p5−3s)
2(1 + p4−3s)(1 − p11−4s)(1 − p10−4s)
2(1 − p9−4s)
4

× (1 − p8−4s)
4(1 − p7−4s)
4(1 − p6−4s)
2(1 − p5−4s) · · · , s > 5.

Remark 21. Templates of these sequences are σ0(n3) is A048785, σ1(n3) in A175926.
σ0(n2) ⋆ 1 is A035116. σ0(n3) ⋆ 1 is A061391.

3.9. Sum of Gcd or Lcm. Following (3.9), the gcd of a divisor d and its com-
plementary divisor n/d contributes with a factor (pm, pe−m)
t = pt·min(m,e−m) to∑

d|n(d, n/d)
t. Summing over m from 0 to e yields the master equation

(3.49) a(pe) =
 { pet/2 + 2 ∑e/2−1
m=0 ptm = [(pt + 1)pet/2 − 2]/(pt − 1), e even;
2 ∑(e−1)/2
m=0 ptm = 2[pt(e+1)/2 − 1]/(pt − 1), e odd.

The Bell series is
(3.50) ∑

e=0,2,4,...
 (pt + 1)pet/2 − 2
(pt − 1)pes + ∑

e=1,3,5,... 2 pt(e+1)/2 − 1
(pt − 1)pes = 1 + p−s

(1 − p−s)(1 − pt−2s) ,

which reveals

(3.51) ∑

d|n (d, n/d)
t ↦→ ζ2(s)ζ(2s − t)/ζ(2s).

The associated analysis for the lcm starts from (3.12). The prime p and ex-
ponent m of the divisor d contribute to ∑
d[d, n/d]t with a term [pm, pe−m]t =
pt·max(m,e−m). The master equation splits again into two cases depending on
whether a middle term at m = e/2 is present or not:
(3.52)

a(pe) =
 { pet/2 + 2 ∑e/2−1
m=0 pt(e−m) = [2pt(1+e) − (pt + 1)pet/2]/(pt − 1), e even;
2 ∑(e−1)/2
m=0 pt(e−m) = 2et(e+1)/2[pt(e+1)/2 − 1]/(pt − 1), e odd.

The Bell series factorizes in the ζ-basis similar to (3.51):

(3.53) ∑

d|n [d, n/d]t ↦→ ζ2(s − t)ζ(2s − t)/ζ(2s − 2t).

Remark 22. ∑d(d, n/d)
t is A055155 for t = 1 and A068976 for t = 2. ∑d[d, n/d]
is A057670.

3.10. Sigma powers.
 DIRICHLET GENERATING FUNCTIONS 13

3.10.1. Ordinary Products. The t-th power of (3.17) is

(3.54) σt
k(pe) = (pk(e+1) − 1)
t

(pk − 1)t , e ≥ 0.

The binomial expansion of the associated Bell series is

(3.55) ∑

e≥0
 σt
k(pe)
pes = 1
(pk − 1)t ∑

e≥0
 t∑

t′=0
(−)
t−t
′ ( t
t′
) pt
′k(e+1)

pes

= 1
(pk − 1)t
 t∑

t′=0
(−)
t−t
′ ( t
t′
) pt
′k

1 − p(t′k−s) .

For the squares of σ, t = 2,

(3.56) ∑

e≥0
 σ2
k(pe)
pes = 1 − p2k−2s

(1 − p−s)(1 − pk−s)2(1 − p2k−s)

produces the Dirichlet series

(3.57) σ2
k(n) ↦→ ζ(s)ζ2(s − k)ζ(s − 2k)
ζ(2s − 2k) .

Because this equals (3.41) multiplied by ζ(s − k), we ﬁnd with (1.3) and (1.8):

(3.58) σ2
k(n) = σk(n2) ⋆ nk.

Remark 23. These considerations cover A035116 with the Dirichlet series [33,
(1.2.10)]

(3.59) σ2
0(n) = σ0(n2) ⋆ 1 = σ0(n) ⋆ σ∗
0 (n) ↦→ ζ4(s)/ζ(2s),

where σ∗
0 (n) is the number of unitary divisors of n (A034444). They also cover
σ2
1(n) in A072861.

For larger t, the denominators of (3.55) contribute ∏t
t′=0 ζ(s−t′k) to the Dirichlet
series (represented for k = 1 and various t by A001001 and A038991–A038999), but
the numerators do not factor as nicely. The examples are

(3.60) ∑

e≥0
 σ3
k(pe)
pes = p3k−2s + 2p2k−s + 2pk−s + 1
∏3
t′=0(1 − pt′k−s)

or
(3.61)
∑

e≥0
 σ4
k(pe)
pes = p6k−3s + (3p2k + 5pk + 3)p3k−2s + (3p2k + 5pk + 3)pk−s + 1
∏4
t′=0(1 − pt′k−s) .

The Euler product expansions for these two cases start as

(3.62) σ3
k(n) = ζ(s)ζ(s − k)ζ(s − 2k)ζ(s − 3k) ∏

p (1 + p2k−s)
2(1 + pk−s)
2

× (1 − p4k−2s)(1 − p3k−2s)
3(1 − p2k−2s)(1 + p6k−3s)
2(1 + p5k−3s)
6

× (1 + p4k−3s)
6(1 + p3k−3s)
2(1 − p8k−4s)
3(1 − p7k−4s)
12(1 − p6k−4s)
15

× (1 − p5k−4s)
12(1 − p4k−4s)
3 · · · , s > 1 + 3k,

14 RICHARD J. MATHAR

and

(3.63) σ4
k(n) = ζ(s)ζ(s − k)ζ(s − 2k)ζ(s − 3k)ζ(s − 4k) ∏

p (1 + p3k−s)
3

× (1 + p2k−s)
5(1 + pk−s)
3(1 − p6k−2s)
3(1 − p5k−2s)
12(1 − p4k−2s)
14(1 − p3k−2s)
12

× (1 − p2k−2s)
3(1 + p9k−3s)
8(1 + p8k−3s)
36(1 + p7k−3s)
72(1 + p6k−3s)
88(1 + p5k−3s)
72

× (1 + p4k−3s)
36(1 + p3k−3s)
8 · · · , s > 1 + 4k.

3.10.2. Hybrid Products. Dirichlet series of mixed products are [33, (1.3.3)][35, 5]

(3.64) σa(n)σb(n) ↦→ ζ(s)ζ(s − a)ζ(s − b)ζ(s − a − b)
ζ(2s − a − b) ,

of which (3.57) is a special case. An example of this type is σ0(n)σ1(n) in A064840.

3.10.3. Dirichlet Convolutions. τk(n) is the number of ways of expressing n as a
product of k factors. τ2(n) = σ0(n) and iterated convolution with 1 yield the ladder
of larger k [33, (1.2.2.)][35]:

(3.65) τk(n) ↦→ ζk(s).

Remark 24. τ2 is A000005, τ3 is A007425, τ4 = σ0(n) ⋆ σ0(n) is A007426, τ5 is
A061200, τ6 is A034695, τ7–τ11 are A111217–A111221, and τ12 is A111306.

Remark 25. σ2
1(n) ⋆ 1 is A065018. σ2
0(n) ⋆ 1 is A062367. σ3
0(n) ⋆ 1 is A097988.

3.11. Powers times Sigma.

3.11.1. Ordinary product. Products with powers have Dirichlet generating func-
tions derived from (1.3) with (3.19) or (3.57):

(3.66) ntσk(n) ↦→ ζ(s − t)ζ(s − k − t), k ≥ 0.

(3.67) ntσ2
k(n) ↦→ ζ(s − t)ζ2(s − k − t)ζ(s − 2k − t)
ζ(2s − 2k − 2t)

Remark 26. This concerns nσ0(n) in A038040, n2σ0(n) in A034714, and nσ1(n)
in A064987.

3.11.2. Dirichlet convolutions. Convolutions with powers have Dirichlet generating
functions which are products of (2.5) with (3.19) or (3.57):

(3.68) nt ⋆ σk(n) ↦→ ζ(s)ζ(s − t)ζ(s − k), k ≥ 0.

(3.69) nt ⋆ σ2
k(n) ↦→ ζ(s)ζ(s − t)ζ2(s − k)ζ(s − 2k)
ζ(2s − 2k) .

Remark 27. n ⋆ σ0(n) is A007429. n ⋆ σ2
0(n) is A062369. n ⋆ σ1(n) is A060640.
n2 ⋆ σ0(n) is A007433. n2 ⋆ σ1(n) = n ⋆ σ2(n) is A001001. n3 ⋆ σ1(n) = n ⋆ σ3(n)
is A027847. Multiplication of (3.19) with ζ(s − t) shows [14, p. 285]

(3.70) σk(n) ⋆ nt = σt(n) ⋆ nk.

DIRICHLET GENERATING FUNCTIONS 15

3.12. Sums of Odd Divisors. The master equation for the sum of odd divisors
of n, σ(o)
k (n) ≡ ∑d|n,d odd d
k is

(3.71) a(2e) = 1; a(pe) =
 { p
ke+k−1
pk−1 , k > 0, p > 2.
e + 1, k = 0, p > 2.

The two Bell series for the prime 2 on one hand or any odd prime on the other
hand repeat (3.17), ∑

e≥0
 1
2es = 1
1 − 2−s(3.72)
 ∑

e≥0
 pk(e+1) − 1
(pk − 1)pes = 1
(1 − p−s)(1 − pk−s) , p > 2.(3.73)

The Dirichlet series is the interlaced product

(3.74) σ(o)
k (n) ↦→ (1 − 2k−s)ζ(s)ζ(s − k), k ≥ 0.

Remark 28. The OEIS examples are k = 0 in A001227, k = 1 in A000593, and
k = 2–5 in A050999–A051002.

3.13. Euler’s Totient.

3.13.1. Basis function. The totient ϕ(n) counts numbers ≤ n and coprime to n,
represented by A000010 and its D-inverse A023900. The master equation is

(3.75) ϕ(pe) = (p − 1)pe−1, e > 0.

The Bell series factorizes in the form [4, p. 111]

(3.76) ϕ(n) = µ(n) ⋆ n ↦→ ζ(s − 1)
ζ(s)

Remark 29. The sum of the k−th powers of the divisors coprime to n, ϕk(n), is
generally not multiplicative for k > 0. This is easily shown by ﬁnding small indices
that violate the deﬁning equation (1.1).

Remark 30. Equation (3.76) has been generalized to deﬁne ϕk,l(n) ≡ µ(n)nk⋆nl ↦→
ζ(s − l)/ζ(s − k) [10]. ϕ1,2(n) is A002618, ϕ1,3(n) is A000056, ϕ2,3(n) is A053191.

The square of (3.76) deﬁnes ϕ
2(n) in A127473,

(3.77) a(pe) = (p − 1)
2p2e−2,

which leads to the Bell series

(3.78) 1 + ∑

e≥1
 (p − 1)
2p2e−2

pes = 1 − 2p1−s + p−s

1 − p2−s ,

and the inﬁnite Euler product

(3.79) ϕ
2(n) ↦→ ζ(s − 2) ∏

p (1 − p1−s)
2(1 + p−s)(1 − p2−2s)(1 + p1−2s)
2

× (1 − p3−3s)
2(1 + p2−3s)
4(1 − p1−3s)
2(1 − p4−4s)
3(1 + p3−4s)
8(1 − p2−4s)
5

× (1 + p1−4s)
2(1 − p5−5s)
6(1 + p4−5s)
16(1 − p3−5s)
16

× (1 + p2−5s)
8(1 − p1−5s)
2 · · · , s > 3.

16 RICHARD J. MATHAR

Cohen deﬁnes a multiplicative function ϕ
′ with a simple master equation build from
the product of (2.8) squared and (3.75) [11]:

(3.80) ϕ
′(n) ≡ µ2(n)ϕ(n) ↦→ ∏

p (1 + p1−s − p−s).

This has already been met in (2.25), which can be combined into

(3.81) 1 ⋆ ϕ
′(n) = rad2(n).

Remark 31. ϕ
′ is given by the absolute values of A097945.

3.13.2. Basic Convolution. ϕ⋆ϕ is A029935. (2.10) and (3.76) combine as (A007431,
A063659)

(3.82) µ(n) ⋆ ϕ(n) ↦→ ζ(s − 1)/ζ2(s); µ2(n) ⋆ ϕ(n) ↦→ ζ(s − 1)/ζ(2s).

3.13.3. Ordinary product with powers. The ϕ(nt) are obtained from (3.76) by the
substitution e → et, so the Bell series is

(3.83) 1 + ∑

e≥1
 (p − 1)pet−1

pes = ps − pt−1

ps − pt = 1 − pt−s−1

1 − pt−s

and therefore

(3.84) ϕ(nt) ↦→ ζ(s − t)/ζ(s + 1 − t).

Applying (1.3) establishes the well-known [11]

(3.85) ϕ(nt) = nt−1ϕ(n).

Remark 32. This describes nϕ(n) (A002618), twice the sum of the integers co-
prime to n and not exceeding n [10], and n2ϕ(n) (A053191).

3.13.4. Dirichlet product with powers. ϕ⋆1 = n is obvious from (3.76) [10]. Building
ϕ
2 ⋆ 1 we generate A029939. From (1.9) and (3.77) its master equation ensues,

(3.86) a(pe) = 1 + ∑

l=1..e(p − 1)
2p2l−2 = p2e(p − 1) + 2
p + 1 .

By construction, the Dirichlet series is (3.79) multiplied by ζ(s).

Remark 33. n⋆ϕ(n) is A018804 with D-inverse in A101035. n2⋆ϕ(n) is A069097.

3.14. Jordan Functions. Dirichlet convolution of nk and µ(n) deﬁnes Jordan
functions Jk. The generating functions are an immediate consequence of (1.3) and
(2.7):

(3.87) nk ⋆ µ(n) = Jk(n) ↦→ ζ(s − k)/ζ(s).

Remark 34. OEIS representatives are A000010 (k = 1), A007434 (k = 2) with
D-inverse A046970, A059376 (k = 3) with D-inverse A063453, A059377–A059378
(k = 4–5), and A069091–A069095 (k = 6–10).

Via (1.9), the master equation for Jk is

(3.88) a(pe) = pk(e−1)(pk − 1), e > 0.

An immediate consequence of the divisibility properties of the cyclotomic polyno-
mial pk − 1 in this equation is that Jd(n)|Jk(n) if d|k [8, 22].

DIRICHLET GENERATING FUNCTIONS 17

3.14.1. Products. A000056 is nJ2(n). A115224 is n2J3(n). The convolution prod-
ucts nk ⋆ Jk(n) ↦→ ζ2(s − k)/ζ(s) generalize Pillai’s function [18].

3.14.2. Dedekind ψ. The Dedekind ψ-function is the ratio

(3.89) ψ(n) = J2(n)/J1(n) ↦→ ζ(s)ζ(s − 1)/ζ(2s),

which can be phrased as

(3.90) ψ(n) = n ⋆ ξt(n)

with the aid of (1.10), (2.5) and (3.5).

Remark 35. The M¨obius transform µ(n) ⋆ ψ(n) drops the factor ζ(s) in (3.89)
and is found in A063659. The Dirichlet series of nψ(n) (A000082) and n2ψ(n)
(A033196) follow from (1.3). µ(n) ⋆ nψ(n) is A140697.

Remark 36. The Jk(n)/J1(n) for k = 2–17 are A001615, A160889, A160891,
A160893, A160895, A160897, A160908, A160953, A160957, A160960, A160972,
A161010, A161025, A161139, A161167, and A161213.

The master equation for Jk(n)/J1(n) is a ratio of terms of (3.88):

(3.91) a(pe) = pk(e−1)(pk − 1)
pe−1(p − 1) = p(k−1)(e−1)(pk − 1)
p − 1 , e > 0,

with Bell series

(3.92) 1 + ∑

e≥1
 p(k−1)(e−1)(pk − 1)
(p − 1)pes = p − 1 + pk−1−s − p−s

(p − 1)(1 − pk−1−s) = 1 + (
∑k−2
l=0 pl)p−s

1 − pk−1−s .

At k = 2 this reduces to (3.89). If k > 2, (3.92) is (3.46) multiplied by 1 − p−s

followed by the substitution s → s + 1; the Dirichlet series of Jk(n)/J1(n) are
obtained from prime products like (3.47) by deleting ζ(s) and the substitution
s → s + 1, to wit

(3.93) 1 ⋆ [n Jk(n)
J1(n) ] = σ1(nk), k = 1, 2, . . . .

Multiplicative generalized Dedekind functions ψk = J2k(n)/Jk(n) are another
generalization which—by virtue of (3.88)—have integer entries governed by

(3.94) a(pe) = pk(e−1)(pk + 1), e > 0.

The Bell series are

(3.95) 1 + ∑

e≥1
 pke−k(pk + 1)
pes = 1 + p−s

1 − pk−s ,

and their product over all primes generates

(3.96) ψk ↦→ ζ(s)ζ(s − k)/ζ(2s).

Mediated by (3.5) and (3.19), factorizations of this product lead to

ψk(n) = nk ⋆ µ2(n);(3.97)
 ǫ2(n) ⋆ ψk(n) = σk(n).(3.98)

Remark 37. Associated OEIS entries are ψ2(n) (A065958), ψ3(n) (A065959),
ψ4(n) (A065960), J6(n)/J2(n) (A194532) and J8(n)/J4(n) (A194533) .

3.15. Sigma times Totient.

18 RICHARD J. MATHAR

3.15.1. Ordinary products. The multiplicative σ0(n)ϕ(n) is represented by A062355.
The master equation is the product of (3.17) and (3.75),

(3.99) a(pe) = (e + 1)(p − 1)pe−1, e > 0.

The Bell series is

(3.100) 1 + ∑

e≥1(e + 1)(p − 1)pe−1/pes = 1 − 2p−s + p1−2s

(1 − p1−s)2 .

The inﬁnite Euler product is

(3.101) σ0(n)ϕ(n) ↦→ ζ2(s − 1) ∏

p (1 − p−s)
2(1 + p1−2s)(1 − p−2s)(1 + p1−3s)
2

× (1 − p−3s)
2(1 + p1−4s)
4(1 − p−4s)
3(1 − p2−5s)
2(1 + p1−5s)
8 · · · , s > 2.

σ0(n)ϕ
2(n) is A126775 with Bell series

(3.102) 1 + ∑

e≥1
 (e + 1)(p − 1)
2p2(e−1)

pes = 1 − 4p1−s + 2p3−2s + 2p−s − p2−2s

(1 − p2−s)2

and Euler product

(3.103) ζD = ζ2(s − 2) ∏

p (1 − p1−s)
4(1 + p−s)
2(1 + p3−2s)
2(1 − p2−2s)
7

× (1 + p1−2s)
8(1 − p−2s)(1 + p4−3s)
8(1 − p3−3s)
28(1 + p2−3s)
34

× (1 − p1−3s)
16(1 + p−3s)
2(1 − p6−4s) · · · , s > 3.

σ2
0(n)ϕ(n) is A110601 with Bell series

(3.104) 1 + ∑

e≥1
 (e + 1)
2(p − 1)pe−1

pes = p1−s + 1 − p2−3s + 3p1−2s − 4p−s

(1 − p1−s)3 .

(3.105) σ2
0(n)ϕ(n) ↦→ ∏

p (1 + p1−s)(1 − p−s)(1 + p1−2s)
7(1 − p−2s)
6(1 − p2−3s)
8

× (1 + p1−3s)
28(1 − p−3s)
20(1 + p3−4s)
8(1 − p2−4s)
53(1 + p1−4s)
112

× (1 − p−4s)
60 · · · , s > 2.

The master equation of σ1(n)ϕ(n) (A062354) is a product of (3.17) by (3.75),

(3.106) a(pe) = pe−1(pe+1 − 1).

The Bell series is

(3.107) 1 + ∑

e≥1
 pe−1(pe+1 − 1)
pes = 1 − p1−s − p−s + p2−2s

(1 − p2−s)(1 − p1−s) ,

and the Euler product

(3.108) ζD(s) = ζ(s − 2) ∏

p (1 − p−s)(1 + p2−2s)(1 − p1−2s)(1 + p3−3s)

× (1 − p1−3s)(1 + p4−4s)(1 + p3−4s)(1 − p1−4s)(1 + p4−5s)

× (1 + p3−5s)(1 − p2−5s)(1 − p1−5s) · · · , s > 3.

DIRICHLET GENERATING FUNCTIONS 19

3.15.2. Dirichlet convolutions. The application of (1.3) and (1.10) to (3.19) and
(3.76) yields [14, p. 293]

(3.109) ntϕ(n) ⋆ σt(n) = n1+t ⋆ 1

Remark 38. Examples of these convolutions are σ0(n) ⋆ ϕ(n) in A000203, σ2
0(n) ⋆
ϕ(n) in A060724, σ1(n) ⋆ ϕ(n) in A038040, and σ2(n) ⋆ ϕ(n) in A064987.

4. Miscellany

4.1. Ramanujan sums. For our purposes the following deﬁnition suﬃces [2, 19]:

Deﬁnition 6. (Ramanujan sum ck(n))

(4.1) ck(n) = ∑

d|n,d|k µ(k/d)d.

The associated Dirichlet series are [33, 17]:

cn(k) ↦→ σ1−s(k)
ζ(s) ,(4.2)
 ck(n) ↦→ ζ(s) ∑

d|k µ(k/d)d
1−s,(4.3)

and

(4.4) ck(n)τ (n) ↦→ ζ2(s) ∑

δ|k δ1−sµ(k/δ) ∏

p|δ (l + 1 − lp−s)

where δ ≡ ∏ pl.

Remark 39. We ﬁnd cn(1) = µ(n), cn(2) in A086831, cn(3) in A085097, cn(4) in
A085384, cn(5) in A085639, and cn(6) in A085906. c1(n) = 1, but if the role of the
argument and index are swapped, the functions are non-multiplicative in general:
c2(n) = −(−1)
n and c3(n) in A099837, c4(n) in A176742, and c6(n) in A100051.

4.2. Unitary Arithmetics.

4.2.1. Properties. The unitary convolution

(4.5) (a ⊕ b)(n) ≡ ∑

d|n,(d,n/d)=1 a(d)b(n/d)

shows parallels to the Dirichlet convolution. Because it preserves the multiplicative
property of its factors [11, 29, 34] and because its basic associated M¨obius, Sums-
of-Divisors and totient functions are multiplicative, inheritance similar to Section
3 ensues. The formula that parallels (1.9) is

(4.6) (a ⊕ b)(pe) = a(1)b(pe) + a(pe)b(1), e > 0.

Cohen deﬁnes for example [11]

(4.7) σ′(n) = nµ2(n) ⊕ 1.

Because the master equation of nµ2(n) ↦→ ζ(s − 1)/ζ(2s − 2) is

(4.8) a(pe) = { pe, e ≤ 1;
0, e > 1,

20 RICHARD J. MATHAR

the master equation of σ′ is constructed from (4.6) as

(4.9) a(pe) =
 



 1, e = 0;
1 + p, e = 1;
1, e > 1.

The Bell series is (1 + p1−s − p1−2s)/(1 − p−s), which leads to the Dirichlet series

(4.10) σ′(n) ↦→ ζ(s) ∏

p (1 + p1−s − p1−2s) = ζ(s) ∏

p (1 + p1−s)(1 − p1−2s)

× (1 + p2−3s)(1 − p3−4s)(1 + p4−5s)(1 + p3−5s)(1 − p5−6s)(1 − p4−6s) · · · , s > 2.

Remark 40. σ′ is A092261.

4.2.2. Unitary µ. The ω-analog of (2.17) is the unitary M¨obius function (A076479)
[11, 29, 13]

(4.11) µ∗(n) = (−1)
ω(n),

where ω(n) is the number of distinct prime factors of n. Master equation and Bell
series are [12]

(4.12) a(pe) = −1; 1 + ∑

e≥1
 a(pe)
pes = 1 − 2p−s

1 − p−s .

The Dirichlet series is ζ(s) divided by (2.12) at c = 2, i. e., ζ(s) multiplied by the
associated Feller-Tornier constant [25, Tab. 6]:

(4.13) µ∗(n) ↦→ ∏

p (1 − p−s)(1 − p−2s)(1 − p−3s)
2(1 − p−4s)
3(1 − p−5s)
6

× (1 − p−6s)
9(1 − p−7s)
18(1 − p−8s)
30 · · · , s > 1.

Remark 41. The Dirichlet series of Cohen’s exponentially odd numbers µ∗
2(n) is
the same at doubled argument 2s [11].

4.2.3. Unitary Sigma. The unitary σ-function sums over the divisors d which are
coprime to their complementary divisors n/d:

Deﬁnition 7. (Unitary sigma σ⋆)

(4.14) σ∗
k(n) = nk ⊕ 1 = ∑

d|n,(d,n/d)=1 d
k.

Applying (4.6), the master equation for the k-power of the divisors is [36]

(4.15) a(pe) = 1 + pke.

The Bell series is

(4.16) 1 + ∑

e≥1(1 + pek)/pes = 1 − pk−2s

(1 − p−s)(1 − pk−s) ,

which becomes

(4.17) σ∗
k(n) ↦→ ζ(s)ζ(s − k)/ζ(2s − k).

Multiplication with ζ(2s − k) generates in view of (3.2) and (3.19)

(4.18) (nk/2ǫ2(n)) ⋆ σ∗
k(n) = σk(n).

DIRICHLET GENERATING FUNCTIONS 21

The sum of the k-th power of the odd unitary divisors σ∗(o)
k (n) is determined
by a master equation which counts only the ﬁrst or both of the terms in (4.15)
depending on p being even or odd:

(4.19) a(pe) = { 1, p = 2;
1 + pek, p > 2.

The Bells series is 1/(1 − 2−s) for p = 2 and (4.16) for p > 2. In summary

(4.20) σ∗(o)
k (n) ↦→ ζ(s)ζ(s − k)(1 − 2k−s)
ζ(2s − k)(1 − 2k−2s) .

Remark 42. σ∗
0 (n) is A034444. σ∗
1 (n) is A034448 with D-inverse in A178450.
σ∗
k(n) with k = 2–8 are A034676–A034682. σ∗(o)
0 (n) is A068068. σ∗(o)
1 (n) is
A192066.

4.2.4. Unitary Phi. The unitary totient is the unitary convolution of µ∗ and n [11]:

Deﬁnition 8. (Unitary Totient)

(4.21) ϕ
∗(n) = µ⋆(n) ⊕ n.

The master equation is [21]

(4.22) a(pe) = pe − 1

which sums to

(4.23) 1 + ∑

e≥1
 pe − 1
pes = 1 − 2p−s + p1−2s

(1 − p−s)(1 − p1−s) .

Comparison of numerator and denominator with (3.100) shows that the Dirichlet
series is given by replacing one of the two ζ(s − 1) in (3.101) by ζ(s); this can be
phrased via (3.76) as

(4.24) ϕ
∗(n) ⋆ ϕ(n) = σ0(n)ϕ(n).

Remark 43. ϕ
∗(n) is A047994

The unitary Jordan functions generalize ϕ
⋆(n) akin to (3.87) [28]:

(4.25) J ⋆
k (n) = µ⋆(n) ⊕ nk.

Via (4.6), its master equation and Bell series are

(4.26) a(pe) = pek − 1,

(4.27) 1 + ∑

e≥1
 pek − 1
pes = 1 − 2p−s + pk−2s

(1 − p−s)(1 − pk−s) .

The inﬁnite Euler product becomes

(4.28) J ⋆
k (n) ↦→ ζ(s − k) ∏

p (1 − p−s)(1 + pk−2s)(1 − p−2s)(1 + pk−3s)
2

× (1 + pk−4s)
4(1 − p−4s)
3(1 − p2k−5s)
2(1 + pk−5s)
8(1 − p−5s)
6 · · · , s > 1 + k.

(4.22) and (4.26) are related by the substitution e → ek on the right hand sides,
which shows

(4.29) J ∗
k (n) = ϕ
∗(nk).

22 RICHARD J. MATHAR

Unitary analogues of (3.65) might be created as

(4.30) τ ∗
2 (n) = σ∗
0(n); τ ∗
k+1(n) = τ ∗
k (n) ⊕ 1.

The Bell series is bootstrapped from (4.15) with (4.6),

(4.31) 1 + ∑

e≥1
 k
pes = 1 + (k − 1)p−s

1 − p−s .

The similarity with (3.44) induces

(4.32) 1 ⋆ τ ∗
k (n) = σ0(nk).

Remark 44. J ∗
1 (n) is A047994. J ∗
2 (n) is A191414. τ ∗
3 (n) is A074816.

4.3. Higher Order M¨obius. Apostol’s higher order µk(n) generalize (2.8) and
are deﬁned as µk(n) = 0 if any prime power pk+1 divides n, and µk(n) = (−1)
r

where r is the number of maximum prime powers pk which divide n [2, 1, 3]. The
master equation is

(4.33) a(pe) =
 



 1, 0 ≤ e < k;
−1, e = k;
0, e > k.

The Bell series is

(4.34)
 k−1∑

e=0
 1
pes − 1
pks = 1 − 2p−ks + p−(k+1)s

1 − p−s ,

with Dirichlet generating function

(4.35) µk(n) ↦→ ζ(s) ∏

p (1 − p−ks)
2(1 + p−(k+1)s)(1 − p−2ks)(1 + p−(2k+1)s)
2

× (1 − p−3ks)
2(1 + p−(3k+1)s)
4(1 − p−(3k+2)s)
2(1 − p−4ks)
3(1 + p−(4k+1)s)
8

× (1 − p−(4k+2)s)
5(1 + p−(4k+3)s)
2(1 − p−5ks)
6(1 + p−(5k+1)s)
16 · · · , s > 1.

Remark 45. µ2(n)–µ4(n) are A189021–A189023 in the OEIS [31]. n ⋆ µ2(n) is
A181549.

4.4. Powers Congruential to Zero. The number of solutions to x
t ≡ 0 (mod n)
in the interval 1 ≤ x ≤ n is a multiplicative function with [6]

(4.36) a(pe) = pe−⌈e/t⌉ = p⌊(t−1)e/t⌋.

Proof. It is multiplicative because solutions x for n a product of prime powers are all
products of solutions to the individual prime powers, and therefore the cardinality
of the solutions equals the product of the cardinality of solutions to the individual
prime powers. The master equation is derived by noting that the solutions are
x = cp⌈e/t⌉, c = 1, 2, . . ., with a maximum of x = pe. The number of solutions
equals the maximum c, which is the maximum solution divided by the minimum
solution. □

DIRICHLET GENERATING FUNCTIONS 23

The Bell series is accumulated by splitting e = kt + r with remainder 0 ≤ r < t,
and treating r = 0 and r ̸= 0 separately:

(4.37) ∑

e≥0
 p⌊(t−1)(k+r/t)⌋

pes = ∑

k≥0
 p(t−1)k

pkts +
 t−1∑

r=1
 ∑

k≥0
 p(t−1)k+r−1

p(kt+r)s

= 1 + ∑t−1
r=1 pr−1−rs

1 − pt−1−st .

The case t = 2 is dealt with by plugging t = 2 into (3.31). The Euler product for
the case t = 3 is

(4.38) ∏

p
 1 + p−s + p1−2s

1 − p2−3s = ζ(3s − 2) ∏

p (1 + p−s)(1 + p1−2s)(1 − p1−3s)

× (1 + p1−4s)(1 + p2−5s)(1 − p1−5s)(1 − p2−6s)(1 + p1−6s) · · · , s > 1.

Remark 46. t = 2–4 are A000188–A000190.

The associated smallest positive x whose t-th power is divisible by n have master
equations a(pe) = p⌈e/t⌉ and Bell series

(4.39) ∑

e≥0
 p⌈e/t⌉

pes =
 t−1∑

r=0
 ∑

k≥0
 pk+⌈r/t⌉

p(tk+r)s = 1 + ∑t−1
r=1 p1−rs

1 − p1−ts .

For t = 2, the product over primes is

(4.40) min
x>0,x2≡0 mod n x ↦→ ∏

p
 1 + p1−s

1 − p1−2s = ζ(2s − 1)ζ(s − 1)/ζ(2s − 2).

For t = 3, a variation of (4.10) appears:

(4.41) min
x>0,x3≡0 mod n x ↦→ ∏

p
 1 + p1−s + p1−2s

1 − p1−3s = ζ(3s − 1) ∏

p (1 + p1−s + p1−2s)

= ζ(3s − 1) ∏

p (1 + p1−s)(1 + p1−2s)(1 − p2−3s)(1 + p3−4s)(1 − p4−5s)

× (1 + p3−5s)(1 + p5−6s)(1 − p4−6s) · · · , s > 2.

Remark 47. These are A019554 and A019555 for t = 2 and t = 3, A053166 for
t = 4, A015052 and A015053 for t = 5 and t = 6.

References

1. Tom M. Apostol, M¨obius function of order k, Pac. J. Math. 32 (1970), no. 1, 21–27.
MR 0253999 (40 #7212)
2. , Introduction to analytic number theory, Undergraduate Texts in Mathematics,
Springer, 1976. MR 0434929 (55#7892)
3. Antal Bege, Generalized M¨obius-type functions and special set of k-free numbers, Acta Univ.
Sapientiae Math. 1 (2009), no. 2, 143–150. MR 2521184 (2010f:11148)
4. Richard Bellman, Analytic number theory, Mathematics Lecture note series, vol. 57, Benjamin,
1980. MR 0596579 (83c:1001)
5. Jonathan Borwein and Kwok-Kwong Stephen Choi, On dirichlet series for sums of squares,
Ramanujan J. 7 (2003), no. 1–3, 95–127. MR 2076564 (2005i:11123a)
6. Henry Bottomley, Some Smarandache-type multiplicative sequences, Smarandache Notions
Journal 13 (2002), no. 1–3, 134–135. MR 1933254

24 RICHARD J. MATHAR

7. David M. Bradley, Series acceleration formulas for Dirichlet series with periodic coeﬃcients,
Ramanujan J. 6 (2002), no. 3, 331–346. MR 1926998 (2003g:11094)
8. Richard P. Brent, On computing factors of cyclotomic polynomials, Math. Comp. 61 (1993),
no. 203, 131–149. MR 1205459 (93m:11131)
9. P. G. Brown, Some comments on inverse arithmetic functions, Math. Gaz. 89 (2005), no. 516,
403–308.
10. E. D. Cashwell and C. J. Everett, The ring of number-theoretic functions, Pac. J. Math. 9
(1959), no. 4, 975–985. MR 0108510
11. Eckford Cohen, Arithmetical functions associated with the unitary divisors of an integer,
Math. Zeitschr. 74 (1960), 66–80. MR 0112861 (22#3707)
12. , Unitary products of arithmetical functions, Acta Arith. 7 (1961/1962), 29–38.
MR 0130210 (24 #A77)
13. D. E. Daykin, Generalized M¨obius inversion formulae, Quart. J. Math. 15 (1964), no. 1b,
349–354. MR 0174508 (30 #4709)
14. Leonard Eugene Dickson, History of the theory of numbers, Chelsea, New York, 1966.
MR 0245499 (39 #6807a)
15. H. W. Gould and Temba Shonhiwa, A catalogue of interesting Dirichlet series, Miss. J. Math.
Sci 20 (2008), no. 1.
16. I. Gradstein and I. Ryshik, Summen-, Produkt- und Integraltafeln, 1st ed., Harri Deutsch,
Thun, 1981. MR 0671418 (83i:00012)
17. G. H. Hardy and E. M. Wright, An introduction to the theory of numbers, 3 ed., 1954.
MR 0067125 (16,673c)
18. Pentti Haukkanen, On a gcd-sum function, Aequat. Math. 76 (2008), no. 1–2, 168–178.
MR 2443468 (2009j:11010)
19. Pentti Haukkanen and L´aszl´o T´oth, An analogue of Ramanujan’s sum with respect to regular
integers (mod r), Ramanujan J. 27 (2012), no. 1, 71–88. MR 2886490
20. Leetsch Charles Hsu and Evelyn L. Tan, A reﬁnement of de Bruyn’s formula for ∑ akkp,
Fib. Quart. 38 (2000), no. 1, 56–59. MR 1738647 (2000k:11030)
21. Mohan Lal, Iterates of the unitary totient function, Math. Comp. 28 (1974), no. 125, 301–302.
MR 0355419 (49 #201)
22. T. Y. Lam and K. H. Leung, On the cyclotomic polynomial φpq(x), Am. Math. Monthly 103
(1996), no. 7, 562–563. MR 1404079 (97h:11150)
23. R. Sherman Lehman, On Liouville’s function, Math. Comp. 14 (1960), no. 72, 311–320.
MR 0120198 (22 #10955)
24. Richard J. Mathar, Series of reciprocal powers of k-almost primes, arXiv:0803.0900 [math.NT]
(2008).
25. , Hardy–Littlewood constants embedded into iniﬁnite products over all positive integers,
arXiv:0903.2514 [math.NT] (2009).
26. , Table of Dirichlet L-series and prime zeta modulo functions for small moduli,
arXiv:1008.2547 [math.NT] (2010).
27. Pieter Moree, The formal series Witt transform, Discr. Math. 295 (2005), no. 1–3, 143–160.
MR 2143453 (2006b:05015)
28. K. Nageswara Rao, On the unitary analogues of certain totients, Monatsh. Math. 70 (1966),
no. 2, 149–154. MR 0200231 (34# 130)
29. J´ozsef S´andor and Antal Berge, The M¨obius function: generalizations and extensions, Adv.
Stud. Contemp. Math. (Kyungshang) 6 (2003), no. 2, 77–128. MR 1962765 (2004b:11011)
30. Wac law Sierpi´nski, Elementary theory of numbers, Monograﬁe Matematyczne 42 (1964).
MR 0175840 (31 #116)
31. Neil J. A. Sloane, The On-Line Encyclopedia Of Integer Sequences, Notices Am. Math. Soc.
50 (2003), no. 8, 912–915, http://oeis.org/. MR 1992789 (2004f:11151)
32. D. Suryanarayana and R. Sita Rama Chandra Rao, The number of square-full divisors of an
integer, Proc. Am. Math. Soc. 34 (1972), no. 1, 79–80. MR 0291104 (45 # 198)
33. E. C. Titchmarch and D. R. Heath-Brown, The theory of the Riemann zeta-function, 2 ed.,
Oxford Science Publications, 1986. MR 0882550 (88c:11049)
34. L´aszl´o T´oth, On a class of arithmetic convolutions involving arbitrary sets of integers,
Mathem. Pannon. 13 (2002), no. 2, 249–263. MR 1932431
35. R. Vaidyanathaswamy, The theory of multiplicative arithmetic functions, Trans. Am. Math.
Soc. 33 (1931), 579–662. MR 1501607

DIRICHLET GENERATING FUNCTIONS 25

36. Charles R. Wall, The ﬁfth unitary perfect number, Canad. Math. Bull. 18 (1975), no. 1,
115–122. MR 0376515
37. P. Wynn, A note on the generalised Euler transformation, Comp. J. 14 (1971), no. 4, 437–441.
MR 0321266 (47 #9799)
URL: http://www.strw.leidenuniv.nl/~mathar
E-mail address: mathar@strw.leidenuniv.nl

Leiden Observatory, Leiden University, P.O. Box 9513, 2300 RA Leiden, The Nether-
lands
