arXiv:1910.14485v1  [math.NT]  31 Oct 2019
ELLIPTIC CUR VES WITH LONG ARITHMETIC PROGRESSIONS HA VE
LARGE RANK
NATALIA GARCIA-FRITZ AND HECTOR PASTEN
Abstract. For any family of elliptic curves over the rational numbers w ith ﬁxed j-invariant, we
prove that the existence of a long sequence of rational point s whose x-coordinates form a non-trivial
arithmetic progression implies that the Mordell-Weil rank is large, and similarly for y-coordinates.
We give applications related to uniform boundedness of rank s, conjectures by Bremner and Mohanty,
and arithmetic statistics on elliptic curves. Our approach involves Nevanlinna theory as well as
R´ emond’s quantitative extension of results of Faltings.
1. Introduction
It is an open problem whether the ranks of elliptic curves ove r Q are uniformly bounded. Various
heuristics have been developed in support of uniform bounde dness [1, 27, 31, 32, 37, 46]. Also,
the second author has shown [28] that a conjecture of Lang in d iophantine approximation implies
uniform boundedness of ranks for families of elliptic curve s with a ﬁxed j-invariant. In the direction
of unboundedness, it is known that elliptic curves over a glo bal function ﬁeld such as Fp(t) can have
arbitrarily large rank even if one considers quadratic twis ts families [38, 43] and examples over Q
with remarkably large rank are known [8]. It is natural to loo k for a mechanism forcing the rank
of elliptic curves over Q to be large, and certain patterns on rational points seem to a chieve this.
Given an elliptic curve E over Q, an x-arithmetic progression is a sequence P1, ..., PN of Q-rational
points on E having their x-coordinates in arithmetic progression for some choice of W eierstrass
equation y2 = x3 + ax2 + bx + c for E. A y-arithmetic progression on E is deﬁned similarly. Such
sequences are said to be non-trivial if the resulting arithmetic progression in x or y coordinates is
non-constant. These deﬁnitions are in fact independent of t he choice of Weierstrass equation.
Bremner [5] has conjectured that rational points of an x-arithmetic progression on an elliptic
curve E over Q tend to be linearly independent in the Mordell-Weil group. T he conjecture is
motivated by numerous examples, as well as theoretical evid ence such as [6] where it is shown that
for a quadratic twist family over Q, the elliptic curves of rank 1 have x-arithmetic progressions
of uniformly bounded length. See also [7, 14, 26, 41, 42] and t he references therein for further
examples supporting Bremner’s conjecture.
In this work we prove Bremner’s conjecture for families of el liptic curves with ﬁxed j-invariant,
in particular, for quadratic twist families. Given an ellip tic curve E over Q, we let βx(E) be the
maximal length of a non-trivial x-arithmetic progression of rational points in E, and βy(E) is
deﬁned similarly for y-arithmetic progressions. We prove
Theorem 1.1. Let j0 ∈ Q. There is an eﬀectively computable constant c(j0) > 0 that only depends
on j0, such that for every elliptic curve E over Q with j-invariant equal to j0 we have
1 + rank E(Q) ≥ c(j0) · log max{βx(E), βy(E)}.
Date: November 1, 2019.
2010 Mathematics Subject Classiﬁcation. Primary 11G05; Secondary 30D35, 11B25.
Key words and phrases. Ranks, arithmetic progression, elliptic curve, Nevanlinn a theory, abelian varieties.
N. G.-F. was supported by the FONDECYT Iniciaci´ on en Invest igaci´ on grant 11170192 and the CONICYT PAI
grant 79170039. H.P. was supported by FONDECYT Regular gran t 1190442.
1In this work, by “eﬀectively computable” we always mean that a n explicit closed formula can be
obtained after some calculation. For instance, in Theorem 1 .1 we can take
(1.1) c(j0) = 1
8046 (209 + max{log(1 + log H(j0)), 255 + log (2 + log(1 + log H(j0)))})
where H(j0) is the naive height, namely H(a/b) = max {|a|, |b|} for coprime integers a, b with
b ⁄= 0. Although it should be clear from the formula that we did no t try to numerically optimize
this estimate, let us remark that this value for c(j0) is satisfactory in the aspect that it is of the
order of magnitude of 1 /(log log H(j0)), so, it tends to 0 extremely slowly.
We prove that (1.1) is admissible for Theorem 1.1 in Section 6 .5 using (among other tools) a
comparison between the Theta height and the Faltings height of abelian varieties [30].
It turns out that arithmetic progressions on elliptic curve s not only relate to the rank. We also
prove that the (algebraic) torsion points do not have arbitr arily long patterns of this type.
Theorem 1.2. Let E be an elliptic curve over Qalg with a given Weierstrass equation. The set of x-
coordinates of the torsion points of E(Qalg) does not contain arbitrarily long non-trivial arithmetic
progressions. The same holds for y-coordinates. A bound for the length of such progressions ca n be
eﬀectively computed from the j-invariant of E.
Heuristically, these results are consistent with the fact t hat the group structure on elliptic curves
is incompatible with the additive structure of the aﬃne line via the x or y-coordinate maps.
Theorems 1.1 and 1.2 (cf. Section 6.4) are special cases of Th eorem 6.1 which concerns ellip-
tic curves over number ﬁelds and more general patterns on alg ebraic points, not just arithmetic
progressions on x or y-coordinates of rational points. Our proof of Theorem 6.1 he avily uses Nevan-
linna’s value distribution theory for complex holomorphic maps in order to compute the Kawamata
locus of certain sub-varieties of abelian varieties. This w ill allow us to apply Remond’s quantitative
version of Faltings’ theorem on rational points of sub-vari eties of abelian varieties (cf. [10, 11, 34]),
which will be our main tool to control x and y-arithmetic progressions on elliptic curves.
Let us now discuss some applications of Theorem 1.1. Given an elliptic curve E over Q and a
squarefree integer D, we let E(D) be the quadratic twist of E by D. The number of distinct prime
factors of D is denoted by ω(D). From Theorem 1.1 and standard rank bounds we deduce
Corollary 1.3 (cf. Sec. 7.1) . Given an elliptic curve E over Q, there is an eﬀectively computable
constant C(E) > 0 such that for every squarefree integer D we have
max{βx(E(D)), βy(E(D))} ≤ C(E)ω(D)+1.
In connection with conjectures on uniform boundedness of ra nks, Theorem 1.1 directly gives
Corollary 1.4. Let j0 ∈ Q. Suppose that the elliptic curves over Q of j-invariant equal to j0 have
uniformly bounded Mordell-Weil rank. Then there is a number N (j0) only depending on j0 with the
following property: For each elliptic curve E over Q with j-invariant equal to j0 we have
max{βx(E), βy(E)} ≤ N (j0).
We remark that, in view of [28], the assumption that elliptic curves over Q with a ﬁxed j-invariant
have uniformly bounded Mordell-Weil rank, is implied by a co njecture of Lang on the error terms
in Diophantine approximation.
Mohanty [24, 25] conjectured that there is a uniform bound fo r the length of x and y-arithmetic
progressions on Mordell elliptic curves An : y2 = x3 + n with n ∈ Z sixth-power free. Mohanty in
fact made the stronger conjecture that βx(An) and βy(An) are at most 4, but this was disproved for
y-arithmetic progressions by Lee and Velez [20]. Several con structions as well as extensive numerical
searches have been carried out looking for long x or y-arithmetic progressions on Mordell elliptic
2curves (cf. [42] and the references therein), but the record continues to be x-arithmetic progressions
of length 4 and y-arithmetic progressions of length 6 as found by Lee and Vele z [20].
Mohanty’s conjecture on uniform boundedness of x and y arithmetic progressions on Mordell
elliptic curves remains open. In support of this conjecture besides the search for examples, the ﬁrst
author used extensions of methods by Bogomolov and Vojta to s how that the case of y-arithmetic
progressions follows from the Bombieri-Lang conjecture fo r surfaces of general type [13]. In addition,
let us remark that Corollary 1.4 with j0 = 0 gives
Corollary 1.5. The uniform boundedness conjecture for ranks of elliptic cur ves over Q with j-
invariant equal to 0 implies Mohanty’s conjecture for both x and y-arithmetic progressions.
Theorem 1.1 also allows us to prove unconditionally that Mohanty’s conjecture holds on average,
in the sense that the average τ -moments of βx(An) and βy(An) are ﬁnite for certain τ > 0.
Theorem 1.6 (cf. Sec. 7.2) . For x > 0 let S(x) be the set of sixth-power free integers n with
|n| ≤ x. There are absolute constants τ, M > 0 such that for all x > 1 we have
1
#S(x)
∑
n∈S(x)
max{βx(An), βy(An)}τ < M.
The proof of Theorem 1.6 combines Theorem 1.1 with results of Fouvry [12] on upper bounds
for the average size of 3-isogeny Selmer groups for Mordell e lliptic curves, which in turn relies on
the Davenport-Heilbronn theorem on 3-torsion of class grou ps of quadratic ﬁelds. See [2] for the
exact computation of the average size of the 3-isogeny Selme r groups of Mordell elliptic curves.
More generally, Theorem 1.1 allows us to study arithmetic st atistic questions related to βx(E)
and βy(E) provided that we have good control on Selmer groups. Indeed , given a positive integer
m and an elliptic curve E over Q we have the exact sequence
(1.2) 0 → E(Q)/mE(Q) → Sm(E) → X(E)[m] → 0
where Sm(E) is the m-Selmer group and X(E)[m] is the m-torsion of the Shafarevich-Tate group.
The classical proof of the Mordell-Weil theorem shows that Sm(E) is ﬁnite, and from (1.2) we have
mrank E(Q) ≤ # (E(Q)/mE(Q)) ≤ #Sm(E).
Therefore, estimates for the size of m-Selmer groups give bounds for exponential functions of the
rank, and we remark that there are several strong results in t he literature for the arithmetic statistics
for the size of m-Selmer group of elliptic curves. This is well-suited for ou r applications, as Theorem
1.1 (and, more generally, Theorem 6.1) bounds the maximal le ngth of an arithmetic progression in
terms of an exponential function of the rank. For applicatio ns along these lines, it is crucial that
our lower bound for the rank in Theorem 1.1 is logarithmic; se e Section 7 for details.
As the literature on arithmetic statistics of m-Selmer groups of elliptic curves is abundant and
growing, we will only focus on the particularly convenient c ase of the elliptic curves Bn deﬁned by
y2 = x3 − n2x. These elliptic curves are associated to the classical “con gruent number problem”.
Here, results of Heath-Brown [17] allow us to control all the average moments of βx(Bn) and βy(Bn).
Theorem 1.7 (cf. Sec. 7.3) . Let Q(x) be the set of odd squarefree integers n with 1 ≤ n ≤ x. Let
k > 0. There is a constant M (k) > 0 depending only on k such that for all x > 1 we have
1
#Q(x)
∑
n∈Q(x)
max{βx(Bn), βy(Bn)}k < M (k).
Let us mention that x-arithmetic progressions on the elliptic curves Bn are studied in detail in [6]
under the assumption rank Bn(Q) ≤ 1 and in [41] for a speciﬁc sub-family arising from an ellipti c
surface of rank 3. The study in [6] is motivated by a connectio n with the problem of existence of
a 3 × 3 magic square formed by diﬀerent integer squares [36].
32. Review of Nevanlinna theory
In this section we set up the notation regarding Nevanlinna t heory for holomorphic maps into
complex projective varieties. Specially, we introduce the counting, proximity and height functions.
We also recall the fundamental properties of these function s, including the First and Second Main
Theorems. All the results in this section are standard and we include them for later reference. See
for instance [45] for proofs and more general versions of the results in this section.
2.1. Deﬁnitions. Let X be a smooth projective variety over C (we will identify the algebraic
variety X with the complex manifold X(C) if no confusion can arise). Let D be a divisor on X and
for each point x ∈ X we let φD,x be a local equation for D. The support of D is supp D. Given a
complex holomorphic map f : C → X with image not contained in supp D, we deﬁne for r ≥ 0
nX(f, D, r) =
∑
|z|≤r
ordz(f ∗φD,f (z)).
For each r the sum is ﬁnite. The counting function is
NX(f, D, r) =
∫ r
0
(nX(f, D, t) − nX(f, D, 0)) dt
t + n(f, D, 0) log r
=
∑
0<|z|≤r
ordz(f ∗φD,f (z)) log r
|z| + ord0(f ∗φD,f (z)) log r.
If f (0) /∈ supp D, then the counting function takes the simpler form
NX(f, D, r) =
∫ r
0
n(f, D, t) dt
t .
A Weil function for D is a function λX,D : X − supp D → R satisfying that for each x ∈ X
there is a complex neighborhood Ux ⊆ X of x and a continuous function αx : Ux → R such that
λX,D(y) = − log |φD,x(y)|+αx(y) for all y ∈ Ux −supp D. It is a standard result that Weil functions
for D exist, and they are unique up to a bounded continuous functio n on X − supp D.
With f : C → X and D as before and a choice of Weil function λX,D, the proximity function is
mX(f, D, r) =
∫ 2π
0
λX,D (f (r · exp(iθ))) dθ
2π .
The function mX(f, D, −) : R≥0 → R is well-deﬁned up to adding a bounded function.
The Nevanlinna height of f with respect to D is the function TX (f, D, −) : R≥0 → R deﬁned by
TX (f, D, r) = NX(f, D, r) + mX (f, D, r).
Due to the choice of Weil function in mX(f, D, −), we have that TX (f, D, −) is well deﬁned up to
a bounded function of r.
2.2. Basic properties. Let us brieﬂy recall some of the fundamental properties of th e counting,
proximity, and height functions. We use Landau’s notation u(x) = O(v(x)) for functions u, v :
R≥0 → C with v positive valued, to indicate that there is a constant M independent of x such that
for all x > 0 we have |u(x)| ≤ M · v(x).
Lemma 2.1. Let X be a smooth complex projective variety and f : C → X a holomorphic map.
• (Additivity) Let D1, D2 be divisors on X such that the image of f is not contained in
supp D1 ∪ supp D2. Let a, b ∈ Z. Then for all r > 0 we have
NX (f, aD1 + bD2, r) = aNX(f, D1, r) + bNX (f, D2, r)
mX(f, aD1 + bD2, r) = amX(f, D1, r) + bmX(f, D2, r) + O(1)
TX (f, aD1 + bD2, r) = aTX(f, D1, r) + bTX(f, D2, r) + O(1)
4where the error terms are independent of r.
• (Eﬀectivity) Let D be an eﬀective divisor on X such that the image of f is not contained
in supp D. Then for all r ≥ 1 we have
NX(f, D, r) ≥ 0, m X (f, D, r) ≥ O(1), T X (f, D, r) ≥ O(1)
where the error terms are independent of r.
• (Functoriality) Let Y be a smooth complex projective variety, D a divisor on Y and let
γ : X → Y be a morphism. If the image of γ ◦ f is not contained in supp D, then
NX (f, γ ∗D, r) = NY (γ ◦ f, D, r)
mX(f, γ ∗D, r) = mY (γ ◦ f, D, r) + O(1)
TX (f, γ ∗D, r) = TY (γ ◦ f, D, r) + O(1)
where the error terms are independent of r.
Lemma 2.2 (Ample height property). Let X be a smooth complex projective variety. Let f : C → X
be a holomorphic map. Let D be an ample divisor on X such that the image of f is not contained
in supp D. If f is non-constant, then TX (f, D, r) grows to inﬁnity.
Lemma 2.3 (First Main Theorem). Let X be a smooth complex projective variety and let f : C → X
be a holomorphic map. Let D1, D2 be linearly equivalent divisors on X such that the image of f is
not contained in supp D1 ∪ supp D2. Then TX(f, D1, r) = TX (f, D2, r) + O(1).
2.3. T runcated counting functions. When D is an eﬀective reduced divisor on X and the image
of f : C → X is not contained in supp D, we deﬁne
n(1)
X (f, D, r) = # {z ∈ C : |z| ≤ r and f (z) ∈ supp D}
and the truncated counting function
N (1)
X (f, D, r) =
∫ r
0
(
n(1)
X (f, D, t) − n(1)
X (f, D, 0)
) dt
t + n(1)
X (f, D, 0) log r.
We note that N (1)
X (f, D, r) ≥ 0 for r ≥ 1. In general, the truncated counting function does not
respect additivity. It is useful to observe that for an eﬀecti ve reduced divisor D on X and a
holomorphic map f : C → X whose image is not contained in supp D, for all r ≥ 1 we have
(2.1) 0 ≤ N (1)
X (f, D, r) ≤ NX(f, D, r) ≤ TX(f, D, r) + O(1)
where the last estimate is due to the eﬀectivity property of mX(f, D, r).
2.4. Second Main Theorem. Let us state the Second Main Theorem of Nevanlinna theory in t he
case of holomorphic maps to a curve X. For functions u, v : R≥0 → R, the notation u(r) ≤exc v(r)
means that u(r) ≤ v(r) holds for r outside a subset of R≥0 of ﬁnite Lebesgue measure. Similarly
for u(r) = exc v(r). In addition, for v positive valued we use Landau’s notation u(x) = o(v(x)) to
indicate that lim x→∞ u(x)/v(x) = 0.
Theorem 2.4 (Second Main Theorem) . Let X be a smooth projective curve. Let K be a canonical
divisor on X and let A be an ample divisor on X. Let α1, ..., αq ∈ X be diﬀerent points. Let
f : C → X be a holomorphic map diﬀerent from the constant function αj for each j, with image
not contained in the support of K and A. We have
TX (f, K, r) +
q∑
j=1
TX (f, αj, r) ≤exc
q∑
j=1
N (1)
X (f, αj, r) + O (log max{1, TX (f, A, r)}) + o(log r).
5When f is constant, the result is trivial. If f is non-constant, then the statement takes a simpler
form, as the image of f is not contained in the support of any divisor.
Due to Picard’s theorem, the theorem is non-trivial only whe n X has genus 0 or 1. We remark
that a general second main theorem for algebraic varieties i s still conjectural and pertains to the
general setting of Vojta’s conjectures, but we will only nee d the case of curves in this work.
2.5. Meromorphic functions on C. The case of X = P1 will be particularly relevant for us.
Here we identify the Riemann sphere C∞ = C ∪ {∞} with P1 so that C corresponds to the aﬃne
chart {[1 : α] : α ∈ C} ⊆ P1 and ∞ corresponds to [0 : 1] ∈ P1.
Let M be the ﬁeld of complex meromorphic functions on C. Under the previous identiﬁcations,
a function h ∈ M can be seen as a holomorphic map h : C → P1. In this way, given h ∈ M and
a point α ∈ C∞ we can deﬁne N (h, α, r), m(h, α, r), T (h, α, r), and N (1)(h, α, r) in the obvious
way using the corresponding holomorphic map h : C → P1 (the subscript P1 is omitted as in this
context it is clear). Furthermore, we deﬁne
T (h, r) = T (h, ∞, r)
and we observe that for any choice of α ∈ C, the First Main Theorem gives
T (h, r) = T (h, α, r) + O(1)
as functions of r > 0, provided that h is not the constant function α. Also, since −2∞ is a canonical
divisor on P1, the Second Main Theorem takes the form
(2.2) ( q − 2 + o(1))T (h, r) ≤exc
q∑
j=1
N (1)(h, αj, r)
where α1, ..., αq ∈ C∞ are diﬀerent points and f ∈ M a meromorphic function diﬀerent from the
constant function αj for each j (the error term can be made more precise if necessary).
3. Preliminary lemmas on holomorphic maps
3.1. Comparison of counting functions. The next lemma will allow us to compare counting
functions of various sorts.
Lemma 3.1. Let n1(r), n2(r) : Rr≥0 → Z≥0 be functions whose points of discontinuity form a
discrete set. Deﬁne
Ni(r) =
∫ r
0
(ni(t) − ni(0))t−1dt + ni(0) log r
for i = 1, 2. If n1(r) ≤ n2(r) for all r ≥ 0, then N1(r) ≤ N2(r) + O(1).
Proof. By linearity, we may assume that n1(r) = 0 for all r, and we need to show that N2(r) is
bounded from below by a constant. It suﬃces to consider r ≥ 1, in which case we have
N2(r) =
∫ r
0
(n2(t) − n2(0))dt
t + n2(0) log r ≥
∫ 1
0
(n2(t) − n2(0))dt
t .
The last quantity is a constant. □
3.2. Holomorphic maps to elliptic curves.
Lemma 3.2. Let E be a complex elliptic curve and let α ∈ E. Let f : C → E be a non-constant
holomorphic map. Then
TE(f, α, r) = exc (1 + o(1))NE (f, α, r) = exc (1 + o(1))N (1)
E (f, α, r).
Furthermore, for every eﬀective non-zero divisor D we have
TE(f, D, r) = exc (1 + o(1))NE (f, D, r).
6Proof. A canonical divisor for E is D = 0, and the divisor α is ample. By the Second Main Theorem
TE(f, α, r) ≤exc N (1)
E (f, α, r) + O(log max{1, TE (f, α, r)}) + o(log r).
As f is transcendental, the error term is o(TE(f, α, r)). The ﬁrst part follows from (2.1). The second
part is deduced by additivity and the fact that positive degr ee divisors on curves are ample. □
3.3. Meromorphic functions arising from elliptic curves. We will be considering meromor-
phic functions h ∈ M that can be written in the form h = g ◦ φ with E an elliptic curve over C,
φ : C → E holomorphic, and g : E → P1 a rational function. Meromorphic functions h of this type
have better value distribution properties than general mer omorphic functions.
Lemma 3.3. Let E be a complex elliptic curve, g : E → P1 a non-constant morphism of degree d,
and φ : C → E a non-constant holomorphic map. Let h = g ◦ φ ∈ M and let α ∈ C∞. We have
(3.1) N (h, α, r) = exc (1 + o(1))T (h, r)
and
(3.2) N (1)(h, α, r) = exc
( #g−1(α)
d + o(1)
)
T (h, r).
Proof. By functoriality of the counting function we have
N (h, α, r) = N (g ◦ φ, α, r) = NE(φ, g∗α, r).
By Lemma 3.2 and functoriality of the height
NE(φ, g∗α, r) = exc (1 + o(1))TE (φ, g∗α, r) = (1 + o(1))T (h, α, r).
which proves (3.1).
For z0 ∈ C we have φ(z0) ∈ g−1(α) if and only if h(z0) = α. Together with Lemma 3.2, this gives
N (1)(h, α, r) =
∑
β∈g− 1(α)
N (1)
E (φ, β, r) = exc (1 + o(1))
∑
β∈g− 1(α)
TE(φ, β, r).
The divisor g∗(∞) on E is ample of degree d, hence, it is numerically equivalent to the divisor d · β
for any given point β ∈ E. Lemma 3.2 in [22] allows us to compare the height for two eﬀect ive,
ample, numerically equivalent divisors, and we get
d · TE(φ, β, r) = TE(φ, d · β, r) + O(1) = (1 + o(1))TE (φ, g∗(∞), r)
from which we deduce
∑
β∈g− 1(α)
TE(φ, β, r) = 1
d
∑
β∈g− 1(α)
d · TE(φ, β, r) = 1
d
∑
β∈g− 1(α)
(1 + o(1))TE (φ, g∗(∞), r)
=
( #g−1(α)
d + o(1)
)
TE(φ, g∗(∞), r) =
( #g−1(α)
d + o(1)
)
T (h, r).
This proves (3.2). □
3.4. GCD counting functions. Given non-constant meromorphic functions h1, h2 ∈ M we deﬁne
nGCD (h1, h2, r) =
∑
|z|≤r
min{ord+
z (h1), ord+
z (h2)}.
The GCD counting function is
NGCD (h1, h2, r) =
∫ r
0
(nGCD (h1, h2, t) − nGCD (h1, h2, 0)) dt
t + nGCD (h1, h2, 0) log r.
7From Lemma 3.1 and the eﬀectivity for proximity functions we d educe the trivial GCD bound
NGCD (h1, h2, r) ≤ N (hj, 0, r) ≤ T (hj, 0, r) + O(1) = T (hj, r) + O(1), for j = 1, 2.
There are several works in the literature on the problem of im proving this trivial bound for the
GCD counting function under various assumptions, see for in stance [29, 23, 21]. For our purposes,
the following will suﬃce.
Lemma 3.4. Let α1, ..., αq ∈ C be distinct and let h1, h2 ∈ M be non-constant meromorphic
functions. We have
q∑
j=1
NGCD (h1 − αj, h2 − αj, r) ≤ T (h1, r) + T (h2, r) − NGCD (1/h1, 1/h2, r) + O(1).
Proof. For z ∈ C and each j we have
min{ord+
z (h1 − αj), ord+
z (h2 − αj)} ≤ ord+
z (h1 − h2)
and
min{ord+
z (1/h1), ord+
z (1/h2)} ≤ ord+
( 1
h1
− 1
h2
)
.
Let H = ( h1, h2) : C → P1 × P1 and let ∆ ⊆ P1 × P1 be the diagonal. From the previous order
estimates and the deﬁnition of the various counting functio ns involved, it follows that
NGCD (1/h1, 1/h2, r) +
q∑
j=1
NGCD (h1 − αj, h2 − αj, r) ≤ NP1×P1(H, ∆ , r).
Let π1, π2 : P1 × P1 → P1 be the projections onto the two factors respectively. On P1 × P1 we have
the linear equivalence ∆ ∼ π∗
1∞ + π∗
2∞, and we get
NP1×P1(H, ∆ , r) ≤ TP1×P1(H, ∆ , r) + O(1) eﬀectivity
= TP1×P1(H, π∗
1∞ + π∗
2∞, r) + O(1) First Main Theorem
= TP1×P1(H, π∗
1∞, r) + TP1×P1(H, π∗
2∞, r) + O(1) additivity
= T (h1, r) + T (h2, r) + O(1) functoriality .
□
4. Arithmetic progressions of holomorphic maps
4.1. Bound for arithmetic progressions. In this section we prove
Theorem 4.1. Let E be an elliptic curve over C and let g : E → P1 be a non-constant morphism
of degree d. Let M ≥ 2 be an integer and for j = 1 , 2, ..., M let φj : C → E be non-constant
holomorphic maps. Deﬁne the meromorphic functions fj = g ◦ φj ∈ M . Suppose that there are
F1, F2 ∈ M with F2 not the zero function, and pairwise distinct complex number s a1, ..., aM ∈ C
such that fj = F1 + ajF2 for each j. Then M ≤ 10d2 − 4d.
The result will be applied in Section 6 in a case where the func tions f1, ..., fj are distinct (not
necessarily consecutive) terms of an arithmetic progressi on in M .
84.2. Pole computation.
Lemma 4.2. Let us keep the notation and assumptions of Theorem 4.1. Let ǫ > 0. There are
indices i1 ⁄= i2 in {1, 2, ..., M} and a Borel set U ⊆ R≥0 of inﬁnite Lebesgue measure such that for
all r ∈ U we have T (fi2, r) ≤ T (fi1, r) and
(
1 − 2
M − ǫ
)
max
1≤j≤M
T (fj, r) ≤ NGCD (1/fi1 , 1/fi2, r) ≤ T (fi1, r) + O(1).
Proof. Given z0 ∈ C, we note that if some of the fj = F1 + ajF2 has a pole at z0, then F1 or F2
has a pole at z0. As the complex numbers aj are diﬀerent, for all 1 ≤ j ≤ M with at most one
exception we get that
ordz0(fj) = min {ordz0F1, ordz0F2} = min
1≤i≤M
ordz0fi < 0.
Therefore, ∑
i<j
nGCD (1/fi, 1/fj, r) =
∑
|z|≤r
∑
i<j
min{ord+
z (1/fi), ord+
z (1/fj)}
≥
∑
|z|≤r
( M − 1
2
)
max
1≤i≤M
ord+
z (1/fi).
It follows that for each 1 ≤ i0 ≤ M we have
∑
i<j
nGCD (1/fi, 1/fj, r) ≥
( M − 1
2
)
n(fi0, ∞, r).
By Lemma 3.1 and Lemma 3.3, for any given ǫ > 0 we get
∑
i<j
NGCD (1/fi, 1/fj , r) ≥
( M − 1
2
)
N (fi0, ∞, r) ≥exc
( M − 1
2
)
(1 − ǫ)T (fi0, r).
Since i0 is arbitrary, we get
∑
i<j
NGCD (1/fi, 1/fj, r) ≥exc
( M − 1
2
)
(1 − ǫ) max
1≤i≤M
T (fi, r).
The ﬁrst sum has
( M
2
)
terms. A contradiction argument shows that there are indice s i1 ⁄= i2 in
{1, 2, ..., M} and a Borel set V ⊆ R≥0 of inﬁnite Lebesgue measure such that for all r ∈ V we have
NGCD (1/fi1, 1/fi2 , r) ≥
( M −1
2
)
( M
2
) (1 − ǫ) max
1≤i≤M
T (fi, r) =
(
1 − 2
M
)
(1 − ǫ) max
1≤i≤M
T (fi, r).
After switching i1, i2 if necessary and replacing V by an inﬁnite measure subset U , for all r ∈ U
we also have T (fi2, r) ≤ T (fi1, r). Finally, the trivial GCD bound gives
NGCD (1/fi1 , 1/fi2, r) ≤ N (1/fi1, 0, r) = N (fi1, ∞, r) ≤ T (fi1, r) + O(1).
We get the result adjusting ǫ. □
4.3. Two numerical lemmas.
Lemma 4.3. For x ∈ R, let us write x+ = max{0, x}. For every A, B ∈ R we have
(A − B)+ ≥ A+ − min{A+, B+}.
Proof. This is readily checked by considering the following cases: A ≤ B; 0 ≥ A > B ; A > 0 ≥ B;
A > B > 0. The details are left to the reader. □
9Lemma 4.4. Let E be a complex elliptic curve and let g : E → P1 be a non-constant morphism of
degree d. Let α1, ..., αk ∈ C be the set of aﬃne branch points (after identifying P1 = C∞). We have
1 ≤ k ≤ 2d and
k∑
j=1
#g−1(αj)
d ≤ k − 1 − 1
d .
Proof. The total number of branch points of a ramiﬁed morphism to P1 is always at least 2, so
k ≥ 1. The Riemann-Hurwitz formula gives (2 · 1 − 2) = d · (2 · 0 − 2) + ∑
α∈P1
(
d − #g−1(α)
)
, thus
2d =
∑
α∈P1
(
d − #g−1(α)
)
≥
∑
α∈P1
α branch
1 ≥ k.
This proves the bounds for k. Finally, there is at most one branch points other than the αj, so the
Riemann-Hurwitz formula gives
2d =
∑
α∈P1
(
d − #g−1(α)
)
≤ (d − 1) +
k∑
j=1
(d − #g−1(αj)) = ( k + 1)d − 1 −
k∑
j=1
#g−1(αj)
and the result follows. □
4.4. Proof of Theorem 4.1. Let us keep the notation and assumptions of Theorem 4.1. Furt her-
more, we may assume M ≥ 4, so that the expressions M − 1, M − 2, and M − 3 are positive (this
is relevant as we will eventually divide by them in some compu tations).
Let ǫ > 0. Up to relabeling the functions fj if necessary, Lemma 4.2 shows that there is a Borel
set U ⊆ R≥0 of inﬁnite Lebesgue measure such that for all r ∈ U we have
(4.1) T (f2, r) ≤ T (f1, r)
and
(4.2)
(
1 − 2
M − ǫ
)
max
1≤j≤M
T (fj, r) ≤ NGCD (1/f1, 1/f2, r) ≤ T (f1, r) + O(1).
For each 1 ≤ j ≤ M deﬁne the complex numbers
λj = a2 − aj
a2 − a1
, µ j = a1 − aj
a1 − a2
γj = aj − a2
aj − a1
and observe that
• All the numbers λj, µj, γj are non-zero.
• The numbers λj are pairwise diﬀerent. Similarly for the numbers µj and the numbers γj.
• λj + µj = 1.
• λja1 + µja2 = aj.
• γj = −λj/µj.
Let α ∈ C. We note that
λj(f1 − α) + µj(f2 − α) = ( λj + µj)F1 + (λja1 + µja2)F2 + (λj + µj)α = fj − α.
hence
(4.3) f2 − α
f1 − α − γj = µ−1
j · fj − α
f1 − α .
From this equation we observe that the meromorphic function (f2 − α)/(f1 − α) ∈ M is not the
constant function γj for any j, since fj is not the constant function α (fj is non-constant).
Also from (4.3) we see that given any complex number α ∈ C, for all r ≥ 0 we have
(4.4) N (1)
( f2 − α
f1 − α , γj, r
)
= N (1)
( fj − α
f1 − α , 0, r
)
.
10Given α ∈ C, let us give an upper bound for the average (for 2 ≤ j ≤ M ) of the right hand side
of the previous expression. Let B[r] = {z ∈ C : |z| ≤ r}. First we observe
M∑
j=2
n(1)
( fj − α
f1 − α , 0, r
)
≤
M∑
j=2
n(1) (fj − α, 0, r) +
M∑
j=2
# {z ∈ B[r] : ord z(f1 − α) < ordz(fj − α) ≤ 0} .
Since fj = F1 + ajF2, we see that if f1 has a pole at some z0, then all the fj have a pole of the
same order at z0 with at most one possible exception for j. Thus, given z0 ∈ C, the condition
ordz0(f1 − α) < ordz0(fj − α) ≤ 0 holds for at most one j, in which case f1 has a pole. We get
M∑
j=2
# {z ∈ B[r] : ord z(f1 − α) < ordz(fj − α) ≤ 0} ≤ n(1)(f1, ∞, r),
from which we deduce
M∑
j=2
n(1)
( fj − α
f1 − α , 0, r
)
≤ n(1)(f1, ∞, r) +
M∑
j=2
n(1) (fj − α, 0, r) .
Therefore, Lemma 3.1 gives
(4.5)
M∑
j=2
N (1)
( fj − α
f1 − α , 0, r
)
≤ N (1)(f1, ∞, r) +
M∑
j=2
N (1) (fj − α, 0, r) + O(1).
Let us write
T (r) = max
1≤j≤M
T (fj, r).
Using (4.5), (4.4), the fact that N (1) (fj − α, 0, r) = N (1) (fj, α, r), and Lemma 3.3, we deduce that
for any given α ∈ C
(4.6)
M∑
j=2
N (1)
( f2 − α
f1 − α , γj, r
)
≤ N (1)(f1, ∞, r) +
M∑
j=2
N (1) (fj, α, r) + O(1)
=exc N (1)(f1, ∞, r) +
( #g−1(α)
d + o(1)
) M∑
j=2
T (fj, r)
≤ T (f1, r) +
( #g−1(α)
d + o(1)
)
(M − 1)T (r).
As explained after (4.3), the meromorphic function ( f2 − α)/(f1 − α) ∈ M is not equal to the
constant function γj for any j. The Second Main Theorem (2.2) with the targets γ2, ..., γM (here,
q = M − 1) gives that for any ﬁxed α ∈ C
(4.7) ( M − 3 + o(1))T
( f2 − α
f1 − α , r
)
≤exc
M∑
j=2
N (1)
( f2 − α
f1 − α , γj, r
)
.
11Let us give a lower bound for the expression on the left hand si de of (4.7). By Lemma 4.3 we have
n
( f2 − α
f1 − α , ∞, r
)
=
∑
|z|≤r
max{0, ordz(f1 − α) − ordz(f2 − α)}
≥
∑
|z|≤r
ord+
z (f1 − α) −
∑
|z|≤r
min{ord+
z (f1 − α), ord+
z (f2 − α)}
= n(f1, α, r) − nGCD (f1 − α, f2 − α, r).
Lemma 3.1 gives the desired lower bound for the left hand side of (4.7):
(4.8) N (f1, α, r) − NGCD (f1 − α, f2 − α, r) ≤ N
( f2 − α
f1 − α , ∞, r
)
+ O(1) ≤ T
( f2 − α
f1 − α , r
)
+ O(1).
We conclude that for any given α ∈ C the following holds:
(M − 3 + o(1)) ((1 + o(1))T (f1, r) − NGCD (f1 − α, f2 − α, r))
=exc (M − 3 + o(1)) (N (f1, α, r) − NGCD (f1 − α, f2 − α, r)) by Lemma 3.3
≤exc
M∑
j=2
N (1)
( f2 − α
f1 − α , γj, r
)
by (4.8) and (4.7)
≤exc T (f1, r) +
( #g−1(α)
d + o(1)
)
(M − 1)T (r) by (4.6) .
Rearranging and collecting the error terms, we conclude
(4.9) ( M − 4)T (f1, r) ≤exc
( #g−1(α)
d + o(1)
)
(M − 1)T (r) + (M − 3)NGCD (f1 − α, f2 − α, r).
Let k be the number of aﬃne branch points in C∞ = P1 of g : E → P1 and let α1, ..., αk ∈ C be
these branch points. Lemma 3.4 gives
k∑
i=1
NGCD (f1 − αi, f2 − αi, r) ≤ T (f1, r) + T (f2, r) − NGCD (1/f1, 1/f2, r) + O(1).
Using (4.1) and (4.2) we get for all r in the inﬁnite measure set U
k∑
i=1
NGCD (f1 − αi, f2 − αi, r) ≤ 2T (f1, r) −
(
1 − 2
M − ǫ
)
T (r) + O(1).
Removing a ﬁnite measure subset from U we get an inﬁnite measure set U ′ ⊆ U ⊆ R≥0 such that
for all r ∈ U ′ the previous estimate holds as well as (4.9) for α = αj with 1 ≤ j ≤ k. This gives
that for all r ∈ U ′ we have
k(M − 4)T (f1, r) ≤


k∑
j=1
#g−1(αj)
d + o(1)

 (M − 1)T (r)
+ 2(M − 3)T (f1, r) − (M − 3)
(
1 − 2
M − ǫ
)
T (r).
Let us write
S =
k∑
j=1
#g−1(αj)
d .
12Rearranging we get
( M − 4
M − 3 · k − 2
)
T (f1, r) ≤
( M − 1
M − 3 · S + o(1) − 1 + 2
M + ǫ
)
T (r).
Using (4.2) (which is valid for r ∈ U ′) we get
( M − 4
M − 3 · k − 2
) (
1 − 2
M − ǫ
)
T (r) ≤
( M − 1
M − 3 · S + o(1) − 1 + 2
M + ǫ
)
T (r).
Since U ′ ⊆ R≥0 has inﬁnite measure, we can let r → +∞ over a sequence in U ′. As the functions
fj are non-constant, we get T (r) → +∞ over this sequence, and we deduce
( M − 4
M − 3 · k − 2
) (
1 − 2
M − ǫ
)
≤ M − 1
M − 3 · S − 1 + 2
M + ǫ.
Since ǫ > 0 is arbitrary and S ≤ k − 1 − 1/d (cf. Lemma 4.4) we obtain
( M − 4
M − 3 · k − 2
) (
1 − 2
M
)
≤ M − 1
M − 3
(
k − 1 − 1
d
)
− 1 + 2
M .
If M were very large, this would approximately give k − 2 ≤ k − 1 − 1/d − 1 = k − 2 − 1/d which
is not possible. So, it is clear that this expression constra ins the size of M . Let us work out the
precise details in order to get the desired bound: Rearrangi ng we obtain
(4.10) (M − 1)M
d + 2(2M − 3) − (5M − 8) · k ≤ 0.
The quadratic function
u(t) = t(t − 1)/d + 2(2t − 3) − (5t − 8)k
is increasing for t ≥ t0 = (1+(5 k−4)d)/2 and satisﬁes u((5k−4)d) = 3 k−2 ≥ 1. Since (5 k−4)d ≥ t0
we deduce that u(t) ≥ 1 for t ≥ (5k − 4)d. Therefore, (4.10) with Lemma 4.4 shows that
M ≤ (5k − 4)d ≤ 10d2 − 4d.
This concludes the proof of Theorem 4.1. □
5. Some geometric constructions
5.1. Notation and ﬁrst constructions. Let k be an algebraically closed ﬁeld of characteristic
0, let E be an elliptic curve over k and let n be a positive integer. Let g ∈ k(E) be a non-constant
rational function of degree d. We identify A1
k with the aﬃne chart {[x0 : x1] ∈ P1
k : x0 ⁄= 0 } of
P1
k. In particular, g can be identiﬁed with a morphism g : E → P1
k of degree d deﬁned over k.
We consider the abelian variety A = En of dimension n. Let Gn : A → (P1)n be the morphism
obtained from n copies of g.
Lemma 5.1. The morphism Gn is ﬁnite of degree dn and ﬂat.
Proof. The map g : E → P1
k is surjective and ﬁnite of degree d. Hence, Gn : En → (P1
k)n is
surjective and ﬁnite of degree dn. On the other hand, the map g is ﬂat by [16] III Prop. 9.7. Hence,
repeated applications of [16] III Prop. 9.2 give that G is ﬂat. □
135.2. The surfaces Un and Hn. Let us assume that n ≥ 3. Let u1, ..., un be the coordinates on
An
k and let us deﬁne the aﬃne variety
(5.1) Un :







u3 − 2u2 + u1 = 0
.
.
.
un − 2un−1 + un−2 = 0
⊆ An
k .
Under the previously chosen inclusion A1
k ⊆ P1
k, we have An
k ⊆ (P1
k)n. Let Hn be the Zariski closure
of Un in ( P1
k)n. Let pj : (P1
k)n → P1
k be the j-th coordinate projection.
Lemma 5.2. We have that Un is a linear surface in An
k and Hn is an irreducible projective surface.
Furthermore, for every j we have that pj restricts to a surjective map Hn → P1
k.
Proof. Un is a linear surface because the n − 2 linear equations deﬁning it are linearly independent.
The other claims follow. □
Lemma 5.3. Let 1 ≤ i < j ≤ n. The projection pij : ( P1
k)n → (P1
k)2 onto the coordinates i and j
restricts to a map Hn → (P1
k)2 which is ﬁnite of degree 1 above A2
k.
Proof. From the equations of Un, we note that if a point ( α1, ..., αn) ∈ Hn has some coordinate
αj = ∞ ∈ P1
k, then all other coordinates with at most one exception are al so equal to ∞. Thus,
the preimage of A2
k under pij|Hn : Hn → (P1
k)2 is precisely Un. Finally, since k has characteristic 0,
ﬁxing ui and uj in k (with i ⁄= j) determines a unique point in Un, namely
uℓ = ℓ − j
i − j · ui + ℓ − i
j − i · uj, 1 ≤ ℓ ≤ n.
□
5.3. The surfaces Vn and Xn. Let us deﬁne
Xn = G−1
n (Hn) ⊆ A and Vn = G−1
n (Un) ⊆ Xn.
Lemma 5.4. We have that Xn is a projective surface and Vn is a dense open subset in Xn.
Moreover, the morphism Gn : En → (P1
k)n restricts to a morphism G′
n : Xn → Hn which is
surjective, ﬁnite of degree dn, and ﬂat.
Proof. Since Gn is ﬂat (cf. Lemma 5.1), it is open by [16] III Exer. 9.1. It foll ows that G−1
n (cl(S)) =
cl(G−1
n (S)) for every set S ⊆ (P1
k)n, where cl(−) denotes Zariski closure. As cl(Un) = Hn, we get
that Xn is the Zariski closure of Vn.
The branch divisor of Gn is ∑ n
j=1 p∗
j Bg where Bg ⊆ P1
k is the branch divisor of g. From Lemma
5.2 we deduce that Hn is not contained in the branch locus of Gn. It follows that Gn restricts to a
ﬁnite surjective map G′
n : Xn → Hn of degree dn. We note that Vn = G−1
n (Un) = ( G′)−1
n (Un) and
Un is open in Hn, thus Vn is open.
Finally, note that G′
n is the base change of Gn by the closed immersion Hn → (P1
k)n, hence G′
n
is ﬂat (cf. [16] III Prop. 9.2). As Gn has pure relative dimension 0, we obtain from Lemma 5.2 and
[16] III Coro. 9.6 that dim Xn = dim Hn = 2. □
5.4. A line sheaf on En. Let πj : En → E be the j-th coordinate projection. Let eE be the
neutral point of E and consider the following line sheaf on En:
Ln = O


n∑
j=1
π∗
j eE

 .
Lemma 5.5. The line sheaf Ln on the abelian variety En is ample and symmetric.
14Proof. For m ∈ Z and B an abelian variety, we write [ m]B for the endomorphism of multiplication
by m on B. Let A = En as before. We have [ −1]∗
EeE = eE, hence
[−1]∗
A
n∑
j=1
π∗
j eE =
n∑
j=1
[−1]∗
Aπ∗
j eE =
n∑
j=1
(πj[−1]A)∗eE
=
n∑
j=1
([−1]Eπj)∗eE =
n∑
j=1
π∗
j [−1]∗
E eE =
n∑
j=1
π∗
j eE.
It follows that Ln is symmetric on En. Since Ln ≃ ⨂ n
j=1 π∗
j O(eE ) and O(eE ) is ample on E (it
has degree 1), we get that Ln is ample on En. □
5.5. Degree estimates. Given a line sheaf F on a smooth projective variety Y and a closed set
Z ⊆ Y , we deﬁne deg F Z as deg([ F ]dim Z · [Z]) if Z is irreducible, and we extend this deﬁnition
linearly for general Z. Here, the intersection product occurs in the Chow ring Ch(Y ) = ⊕jCh j(Y )
of Y (graded by codimension) and deg : Ch 0(Y ) → Z is the usual degree map on 0-cycles —we
use the standard convention that Ch j denotes codimension j cycles, while Ch j denotes cycles of
dimension j. For instance, see Appendix A in [16] for a survey of intersec tion theory.
Lemma 5.6. We have degLn Xn ≤ (n2 − n)d2n−2.
Proof. For the following computations, let us recall that if f : Y → Z is a morphism of smooth
projective varieties over k, then the pull-back f ∗ : Ch(Z) → Ch(Y ) is a graded ring morphism,
while the push-forward f∗ : Ch(Y ) → Ch(Z) respects addition and shifts the grading.
As Xn is a surface, we have deg Ln Xn = deg([Ln]2 · [Xn]). We expand the intersection product
[Ln]2 · [Xn] =
n∑
i=1
n∑
j=1
[π∗
i eE] · [π∗
j eE] · [Xn]
=
n∑
i=1
[π∗
i eE]2 · [Xn] + 2
∑
1≤i<j≤n
[π∗
i eE] · [π∗
j eE] · [Xn]
Moving eE on E, we see that [ π∗
i eE]2 = 0 ∈ Ch 2(A). On the other hand, [ Xn] = G∗
n[Hn] ∈ Ch 2(A)
by Lemma 5.4. Hence, the projection formula gives the follow ing identities in Ch 0((P1
k)n)
(Gn)∗
(
[Ln]2 · [Xn]
)
= 2
∑
1≤i<j≤n
(Gn)∗
(
[π∗
i eE] · [π∗
j eE] · G∗
n[Hn]
)
= 2
∑
1≤i<j≤n
(Gn)∗([π∗
i eE] · [π∗
j eE]) · [Hn]
= 2
∑
1≤i<j≤n
(Gn)∗([π∗
ij((eE, eE ))]) · [Hn]
where πij : En → E2 is the projection onto the i and j coordinates.
Note that π∗
ij((eE , eE)) is obtained from En by replacing the copies of E in the coordinates i and
j by {eE }. Let pij : (P1
k)n → (P1
k)2 be the projection onto the coordinates i and j. We deduce that
the map π∗
ij((eE , eE)) → p∗
ij((g(eE ), g(eE ))) induced by Gn is (up to the obvious isomorphisms) the
same as Gn−2 : En−2 → (P1
k)n−2, which has degree dn−2 by Lemma 5.1. This gives
(Gn)∗([π∗
ij((eE, eE ))]) = dn−2[p∗
ij((g(eE ), g(eE ))] ∈ Ch 2((P1
k)n).
Choose a k-rational point x ∈ A1
k ⊆ P1
k. For i < j , Lemma 5.3 gives the following on ( P1
k)n
deg
(
[p∗
ij((g(eE ), g(eE ))] · [Hn]
)
= deg
(
[p∗
ij((x, x))] · [Hn]
)
= 1.
15From here we deduce
deg
(
(Gn)∗
(
[Ln]2 · [Xn]
))
= (n2 − n)dn−2.
As Gn : A → (P1
k)n is ﬁnite of degree dn (cf. Lemma 5.1), we get the desired bound. □
6. Arithmetic progressions for finite rank groups
6.1. Main arithmetic result. Let L be a ﬁeld. An arithmetic progression in L is a sequence
u1, ..., un of elements of L such that for some a, b ∈ L we have uj = a + jb for each j = 1 , ..., n.
We say that the arithmetic progression u1, ..., un is trivial if al the terms uj are equal, i.e. b = 0.
Otherwise, the arithmetic progression is said to be non-trivial.
The rank of an abelian group Γ is deﬁned as
rank Γ = dim Q(Γ ⊗Z Q).
In particular, if Γ is a torsion abelian group, then rank Γ = 0.
Theorem 6.1. Let j0 ∈ Qalg and let d ≥ 2 be an integer. There is an eﬀectively computable
constant κ(j0, d) depending only on j0 and d such that the following holds:
Let E be an elliptic curve over Qalg with j-invariant equal to j0. Let g ∈ k(E) be a non-constant
rational function on E of degree d deﬁned over Qalg. Let Γ ⊆ E(Qalg) be a subgroup of ﬁnite rank.
Suppose that for a positive integer N there is a sequence P1, ..., PN of points in Γ such that no Pj is
a pole of g, and the sequence g(P1), ..., g(PN ) ∈ Qalg is a non-trivial arithmetic progression. Then
1 + rank Γ > κ(j0, d) · log N.
We remark that if L is a ﬁeld of positive characteristic p > 0, then a non-trivial arithmetic
progression in L can have repeated terms. However, if L has characteristic 0, then an arithmetic
progression is non-trivial (i.e. not all terms are the same) if and only if all its terms are diﬀerent.
For our purposes, we will work in characteristic zero.
We will need the following characterization of arithmetic p rogressions.
Lemma 6.2. Let n ≥ 3 be an integer, let L be a ﬁeld, and let u1, ..., un ∈ L. The sequence u1, ..., un
is an arithmetic progression if and only if uj − 2uj−1 + uj−2 = 0 for each 3 ≤ j ≤ n.
Proof. Arithmetic progressions satisfy the required equations si nce one directly checks
(a + jb) − 2(a + (j − 1)b) + (a + (j − 2)b) = 0 .
Conversely, if the sequence u1, ..., un satisﬁes uj − 2uj−1 + uj−2 = 0 for each 3 ≤ j ≤ n, then
inductively one proves that uj = a + jb with a = 2u1 − u2 and b = u2 − u1. □
6.2. Lang’s conjecture after V ojta, F altings, and R´ emond.In [10, 11] Faltings proved Lang’s
conjecture on rational points in sub-varieties of abelian v arieties. Namely, if L is a number ﬁeld, A
is an abelian variety over L and X ⊆ A is a sub-variety deﬁned over L, then all but ﬁnitely many
L-rational points of X are contained in the Kawamata locus of X; i.e., the union of translates
of positive dimensional abelian sub-varieties of A contained in X. (We recall that the Kawamata
locus is Zariski closed by a theorem of Kawamata [18].) This p roof extended ideas of Vojta’s proof
[44] of Falting’s theorem for curves [9]. See also Bombieri’ s simpliﬁcation [3] of Vojta’s argument.
Faltings theorem on sub-varieties of abelian varieties has been extended in several directions. We
need a quantitative generalization due to R´ emond [34, 35], which also extends Raynaud’s theorem
on torsion points [33] (i.e. the Manin-Mumford conjecture) .
Theorem 6.3 (R´ emond). Let A be an abelian variety of dimension n deﬁned over Qalg, and let L
be a symmetric ample invertible sheaf on A. There is an eﬀectively computable number c(A, L ) > 0
such that the following holds:
16Let X be a closed subvariety of A of dimension m, and let Λ be a subgroup of A(Qalg) such that
its rank r = dim Q(Λ ⊗Z Q) is ﬁnite. There is a non-negative integer
R ≤ (c(A, L ) degL X)(r+1)n5(m+1)2
and there exist points x1, . . . , xR in X(Qalg) ∩ Λ and abelian subvarieties T1, . . . , TR of A satisfying
that xi + Ti ⊆ X for each 1 ≤ i ≤ R, and
X(Qalg) ∩ Λ =
R⋃
i=1
(xi + Ti)(Qalg) ∩ Λ .
This formulation is the same as Th´ eor` eme 1.2 in [34], with the additional remark that the number
c(A, L ) can be eﬀectively computed. In fact, this point is explained in loc. cit. after the statement
of Th´ eor` eme 1.2, and the precise details are given in Th´ eor` eme 2.1 and the paragraph after it.
Moreover, a simple closed formula for c(A, L ) is given in Th´ eor` eme 1.3 of [35] using the notion
of theta height of A, under the assumption that L induces a principal polarization. See Section
6.5 for details on how to use these explicit eﬀective estimate s in our context.
6.3. Proof of Theorem 6.1. Let us keep the notation and assumptions of Theorem 6.1. Let u s
consider constructions from Section 5 with k = Qalg, n = 10 d2 − 4d + 2, and the choice of E and
g given in Theorem 6.1. Especially, we obtain the morphism Gn : En → (P1
k)n, the projective
surfaces Hn ⊆ (P1
k)n and Xn ⊆ En, the open sets Un ⊆ Hn and Vn ⊆ Xn, and the line sheaf Ln on
En.
Let ∆ n = {u1 = u2 = ... = un} ⊆ An
k be the diagonal line. We observe that ∆ n is a Zariski
closed set in Un. Let us deﬁne
U 0
n = Un − ∆ n and V 0
n = G−1
n (U 0
n) ⊆ Vn.
Lemma 6.4. Let L/k be a ﬁeld extension. Let α1, ..., αn ∈ L. We have that the sequence is
an arithmetic progression in L if and only if (α1, ..., αn) ∈ Un(L). In this case, the arithmetic
progression is non-trivial if and only if (α1, ..., αn) ∈ U 0
n(L).
Furthermore, let P1, ..., Pn be a sequence of points in E(L). We have that g(P1), ..., g(Pn) is an
arithmetic progression in L = A1
k(L) if and only if (P1, ..., Pn) ∈ Vn(L). In this case, the arithmetic
progression is non-trivial if and only if (P1, ..., Pn) ∈ V 0
n (L).
Proof. The sequence α1, ..., αn is an arithmetic progression if and only if it has second diﬀer ences
equal to 0 (cf. Lemma 6.2). This is equivalent to the conditio n that ( α1, ..., αn) ∈ Un(L). The
sequence is trivial if and only if all terms are equal, which i s equivalent to ( α1, ..., αn) ∈ ∆ n(L).
The second part follows from the ﬁrst part, using Vn = G−1
n (Un) and V 0
n = G−1
n (U 0
n). □
Note that V 0
n is a non-empty open set of Vn, thus, of Xn. Let Zn = Xn − V 0
n ; this is a proper
Zariski closed subset of Xn. We now show that the Kawamata locus of Xn is contained in Zn.
Lemma 6.5. Let T ⊆ En be an abelian sub-variety of strictly positive dimension, a nd suppose that
x ∈ Xn(k) satisﬁes x + T ⊆ Xn. Then x + T ⊆ Zn.
Proof. Let T ′ = x + T . Since T ′(C) is a positive dimensional complex torus, there is a non-con stant
holomorphic map φ : C → Xn whose image is Zariski dense in T ′; this can be seen by considering
T ′ ≃ Cg/Λ for a lattice Λ ⊆ Cg. Let us write φj = πj ◦ φ : C → E, so that φ = (φ1, ..., φn).
By contradiction, suppose that T ′ is not contained in Zn. Then the image of φ meets V 0
n .
Thus, the image of Gn ◦ φ meets U 0
n. In particular, all the compositions fj = g ◦ φj are complex
meromorphic functions (i.e. φj is not identically a pole of g, for each j).
Since the image of Gn ◦ φ = (f1, ..., fn) meets the Zariski open set U 0
n ⊆ (P1
k)n, we see that for all
but countably many z0 ∈ C we have ( f1(z0), ..., fn(z0)) ∈ U 0
n(C). Thus, by the identity principle,
17we get that ( f1, ..., fn) ∈ M n satisﬁes the equations deﬁning Un but not the equations deﬁning ∆ n.
This means that ( f1, ..., fn) ∈ U 0
n(M ) as an M -rational point. By Lemma 6.4 with L = M , we get
that f1, ..., fn is a non-trivial arithmetic progression in M . Hence, there are F1, F2 ∈ M such that
F2 is not the zero function and fj = F1 + jF2 for each 1 ≤ j ≤ n.
As φ is non-constant and g is ﬁnite, at least one of the fj is non-constant. Thus, at least one
of F1 or F2 is non-constant, and it follows that at most one of the f1, ..., fn can be constant.
Relabeling if necessary and deleting one term, we apply Theo rem 4.1 with M = n − 1 to conclude
that M ≤ 10d2 − 4d. Since n = 10d2 − 4d + 2 we get 10 d2 − 4d + 1 ≤ 10d2 − 4d, a contradiction. □
Finally, we proceed to conclude the proof of Theorem 6.1.
We apply Theorem 6.3 with A = En and L = Ln; this choice of sheaf is allowed by Lemma
5.5. We obtain the eﬀectively computable constant c(En, Ln) > 0 provided by Theorem 6.3. This
constant only depends on the isomorphism class of E over k = Qalg and our choice n = 10d2 −4d+2.
So, c(En, Ln) only depends on d and j0, the j-invariant of E, and this dependence is eﬀective. Let
us write c(j0, d) instead of c(En, Ln) to make explicit that this quantity only depends on j0 and d.
We take X = Xn, which has dimension m = 2 (cf. Lemma 5.4). Let us consider the group
Λ = Γ × · · · × Γ ⊆ En(k) with Γ as in Theorem 6.1 and observe that Λ has ﬁnite rank
r = rank Λ = n · rank Γ.
By Lemma 5.6, the number R provided by Theorem 6.3 satisﬁes
(6.1) R ≤ (c(j0, d) degLn Xn)n45(r+1) ≤ R0 :=
(
c(j0, d) · (n2 − n)d2n−2) n45(1+n·rank Γ)
.
In addition, there are points x1, ..., xR ∈ Xn(k) and abelian sub-varieties T1, ..., TR ⊆ En such that
V 0
n (k) ∩ Λ ⊆ Xn(k) ∩ Λ ⊆
R⋃
i=1
(xi + Ti)(k).
By Lemma 6.5, all the Ti with dim Ti ≥ 1 satisfy xi + Ti ⊆ Zn. Thus, writing
I = {1 ≤ i ≤ R : Ti = {eA}}
we get
V 0
n (k) ∩ Λ ⊆
⋃
i∈I
(xi + Ti)(k) = {xi : i ∈ I}.
In particular,
(6.2) #
(
V 0
n (k) ∩ Λ
)
≤ R.
Let us deﬁne
(6.3) C(j0, d) =
(
c(j0, d) · (n2 − n)d2n−2) n46
with n = 10d2 − 4d + 2.
By (6.1) and (6.2), we see that
(6.4) C(j0, d)1+rank Γ = R0
(
c(j0, d) · (n2 − n)d2n−2) n46−n45
> 2R0 > n + R0 ≥ n + #
(
V 0
n (k) ∩ Λ
)
.
Let P1, ..., PN ∈ Γ be as in the statement of Theorem 6.1, i.e, g(P1), ..., g(PN ) is a non-trivial arith-
metic progression in k. We note that for each j = 1, ..., N−n the sequence g(Pj ), g(Pj+1), ..., g(Pj+n−1)
is a non-trivial arithmetic progression in k of length n, and all these N − n sequences are diﬀerent.
From Lemma 6.4 we deduce that ( Pj, ..., Pj+n−1) ∈ V 0
n (k) for each j = 1 , ..., N − n and these are
diﬀerent points as their images under Gn are diﬀerent. Furthermore, by assumption Pi ∈ Γ for
each i, so we get ( Pj , ..., Pj+n−1) ∈ V 0
n (k) ∩ Λ. This proves #
(
V 0
n (k) ∩ Λ
)
≥ N − n.
Together with (6.4) we ﬁnally get
C(j0, d)1+rank Γ > N.
18This proves Theorem 6.1 with
(6.5) κ(j0, d) = 1 / log C(j0, d).
Since c(j0, d) is eﬀectively computable, so are C(j0, d) and κ(j0, d). □
6.4. Consequences. Let us formulate here two direct consequences of Theorem 6.1 that relate
arithmetic progressions of rational points to two diﬀerent a spects of the arithmetic of elliptic curves:
the rank, and on the other hand, the torsion part.
Corollary 6.6. Let j0 ∈ Qalg and let d be a positive integer. There is an eﬀectively computable
constant κ(j0, d) > 0 depending only on j0 and d such that the following holds:
Let L ⊆ Qalg be a number ﬁeld containing j0 and let E be an elliptic curve over L with j-invariant
equal to j0. Let g be a non-constant rational function on E deﬁned over L of degree d. If for some N
there is a sequence of points P1, ..., PN ∈ E(L) such that g(P1), ..., g(PN ) is a non-trivial arithmetic
progression in L, then
1 + rank E(L) > κ(j0, d) · log N
Proof. All elliptic curves over number ﬁelds with j-invariant equal to j0 are isomorphic to each other
after base change to Qalg. Thus, the result is immediate from Theorem 6.1 applied to E′ = E⊗LQalg
choosing the group Γ = E(L), which is a group of ﬁnite rank by the Mordell-Weil theorem. Here,
we use the inclusion Γ ⊆ E(Qalg) ≃ E′(Qalg). □
Corollary 6.7. Let E be an elliptic curve over Qalg and let d be a positive integer. There is an
eﬀectively computable constant N (E, d) depending only on E and d such that the following holds:
Let g be a non-constant rational function on E deﬁned over Qalg of degree d. Let Sg ⊆ E(Qalg)
be the set of poles of g and let E(Qalg)tor be the group of all torsion points of E. The set
g
(
E(Qalg)tor − Sg
)
⊆ Qalg
does not contain non-trivial arithmetic progressions of le ngth greater than N (E, d).
Proof. The group Γ = E(Qalg)tor has rank 0 and the isomorphism class of E over Qalg is determined
by the j-invariant. Thus, the result is a direct consequence of Theo rem 6.1. □
As a special case, we obtain two of the main results stated in t he Introduction.
Proof of Theorem 1.1. The result follows from Corollary 6.6 with d = 2 for x-coordinates, d = 3
for y-coordinates, and choosing L = Q. □
Proof of Theorem 1.2. The result follows from Corollary 6.7 with d = 2 for x-coordinates and d = 3
for y-coordinates. □
6.5. Eﬀectivity. Here we prove that (1.1) gives an admissible value for c(j0) in Theorem 1.1.
Although we restrict ourselves to the setting of Theorem 1.1 for the sake of simplicity, it will be
clear from the argument that a similar (although lengthier) computation gives an explicit value for
the eﬀective constants in Theorem 6.1 and its consequences.
Let j0 ∈ Q. From the proof of Theorem 1.1 (cf. Section 6.4) we note that c(j0) can be chosen as
any value smaller than
min{κ(j0, 2), κ(j0, 3)} = 1
log max{C(j0, 2), C(j0, 3)} = 1
log C(j0, 3)
with κ(j0, d) and C(j0, d) as deﬁned in (6.3) and (6.5). Here we used that for j0 ﬁxed, one can
check that the quantity C(j0, d) is increasing on d. We compute
(6.6) log C(j0, 3) = 80 46 (log(c(j0, 3)) + log(6320) + 158 log(3)) < 8046 (log(c(j0, 3)) + 183)
19where c(j0, 3) is as in Section 6.3. Namely, c(j0, 3) = c(En, Ln) where n = 10 · 32 − 4 · 3 + 2 = 80,
E is an elliptic curve over Qalg with j-invariant equal to j0, and c(A, L ) is the constant appearing
in Theorem 6.3.
An admissible value for c(A, L ) is given in Th´ eor` eme 1.3 of [35] under the additional assumption
that L induces a principal polarization. In our case, L = Ln ≃ ⨂ n
j=1 π∗
j O(eE ) induces a principal
polarization on En, see [19]. Therefore, the formula from [35] directly applie s. In our case, the
abelian variety A = En and the sheaf Ln can be deﬁned over Q because j0 ∈ Q. Therefore,
Th´ eor` eme 1.3 of [35] allows us to take
(6.7) c(j0, 3) = c(En, Ln) = 2 34 · max{1, hΘ (En)}, n = 80
where hΘ denotes the Theta height associated to the line sheaf L ⊗16. Let us estimate the Theta
height. First we compare it to the semi-stable Faltings’ hei ght hF using results by Pazuki, namely
Corollary 1.3(2) in [30]. Here we use the normalization of hF used in loc. cit. As we are using the
Theta height associated to L ⊗16, we must choose r = 4 in [30] Corollary 1.3(2), which gives
hΘ (En) ≤ 1
2 max{1, hF (En)} + C2(80, 4) log (2 + max{1, hF (En)})
< 1
2 max{1, hF (En)} + e256 log(2 + max{1, hF (En)}).
Since the Faltings height satisﬁes hF (A1 × A2) = hF (A1) + hF (A2) (cf. equation (2.7) in [4] for
instance) and we chose n = 80, we ﬁnd
hΘ (En) < 1
2 max{1, 80hF (E)} + e256 log(2 + max{1, 80hF (E)}).
Lemme 7.9 in [15] (see also [39]) gives hF (E) ≤ h(j0)/12 − 0.72 < h(j0) where h(x) = log H(x) for
x ∈ Q (note that the normalization of the Faltings height in [15] a nd [30] is the same), from which
we get
hΘ (En) < 1
2 max
{
1, 20
3 h(j0)
}
+ e256 log
(
2 + max
{
1, 20
3 h(j0)
})
≤ 10
3 (1 + h(j0)) + e256 log
( 20
3 (1 + h(j0))
)
≤ max
{ 20
3 (1 + h(j0)), e257 log
( 20
3 (1 + h(j0))
)}
.
From (6.7) we get
log c(j0, 3) < 34 log 2 + max
{
log 20
3 + log(1 + h(j0)), 257 + log
(
log 20
3 + log(1 + h(j0))
)}
< 24 + max{2 + log(1 + h(j0)), 257 + log (2 + log(1 + h(j0)))}
= 26 + max {log(1 + h(j0)), 255 + log (2 + log(1 + h(j0)))}.
Finally (6.6) gives
log C(j0, 3) < 8046 (209 + max{log(1 + h(j0)), 255 + log (2 + log(1 + h(j0)))})
which proves (1.1). □
7. Bounding the rank and applications
7.1. Pointwise rank bounds. Let us recall the following bound for the rank of the quadrati c twist
of an elliptic curve. A similar result holds over number ﬁeld s, although to simplify the notation we
only state the case of Q. Here we recall that ω(D) is the number of distinct prime divisors of D.
20Lemma 7.1. Let E be an elliptic curve over Q. There is an eﬀectively computable constant c(E)
depending only on E such that for all squarefree integers D we have
rank E(D)(Q) ≤ 12 · ω(D) + c(E).
Proof. This follows from [40] Ch. VIII, Exercise 8.1 with m = 2. In particular, c(E) is bounded
by a multiple of the number of places of bad reduction of E plus the 2-rank of the class group of
K = Q(E[2]) = Q(E(D)[2]). □
From this we get
Corollary 7.2. Let E be an elliptic curve over Q and let d be a positive integer. There is an
eﬀectively computable constant C(E, d) depending only on E and d such that the following holds:
Let D be a squarefree integer. Let g be a rational function on E(D) deﬁned over Q of de-
gree d. If for some N there is a sequence of rational points P1, ..., PN ∈ E(D)(Q) satisfying that
g(P1), ..., g(PN ) is a non-trivial arithmetic progression in Q, then N < C (E, d)ω(D)+1.
Proof. The result is obtained from Corollary 6.6 with L = Q, using the fact that taking quadratic
twists does not change the j-invariant, and using Lemma 7.1 to bound rank E(D)(Q). □
We note that Corollary 1.3 is a special case of Corollary 7.2.
7.2. Average bounds for Mordell curves. As in the introduction, for x > 0 we let S(x) be
the set of sixth-power free integers n with |n| ≤ x. It is an elementary result in Analytic Number
Theory that the number of k-power free positive integers up to x is asymptotic to x/ζ(k) where
ζ(s) is the Riemann zeta function. In particular we have
Lemma 7.3. As x → ∞ we have the asymptotic estimate
#S(x) ∼ 2
ζ(6) · x = 1890
π6 · x.
For n a sixth-power free integer, we consider the Mordell ellipti c curve An deﬁned by the equation
y2 = x3 + n. The following theorem is a special case of a result due to Fou vry, cf. [12] Th´ eor` eme 1
(using the bounds R+(
√
3) ≤ 115 and R−(
√
3) ≤ 100 given there).
Theorem 7.4. The following estimate holds for all large enough x:
∑
n∈S(x)
3(rank An(Q))/2 < 216 · x.
With these results, we can proceed to the proof of Theorem 1.6 .
Proof of Theorem 1.6. By Theorem 1.1 with j0 = 0 we have
max{βx(An), βy(An)} ≤ exp ((1 + rank An(Q))/c)
where c = c(0) > 0 is an absolute constant. Let us take τ = (c · log 3)/2 > 0 and note that
max{βx(An), βy(An)}τ ≤
√
3 · 3(rank An(Q))/2.
Theorem 7.4 gives that for all large enough x we have
∑
n∈S(x)
max{βx(An), βy(An)}τ ≤ 216
√
3 · x.
Since 216
√
3 · 1890/π6 < 735.5, Lemma 7.3 gives that for all large enough x we have
∑
n∈S(x)
max{βx(An), βy(An)}τ < 800 · #S(x).
The result follows □
21We remark that we can use Corollary 6.6 instead of Theorem 1.1 to obtain a version of Theorem
1.6 for more general rational functions, not just x and y-coordinates.
As explained in the introduction, a crucial aspect in the pro of of Theorem 1.6 is that our lower
bounds for the rank are logarithmic on the maximal length of a n arithmetic progression (cf. The-
orems 1.1 and 6.1), and not worse than logarithmic. Brieﬂy, t he reason why Fouvry’s theorem
can control averages of an exponential function of the rank t hat the core of [12] is an average
estimate for the size of certain 3-isogeny Selmer groups, wh ich is then used as an upper bound for
# (An(Q)/3An(Q)) ≥ 3rank An(Q).
7.3. Average bounds for congruent number curves. For x > 0, let Q(x) be the set of odd
squarefree positive integers n ≤ x. We remark that it is an elementary exercise in sieve theory t o
check that # Q(x) ∼ (3/π2) · x as x → ∞.
Given a squarefree integer n, we consider the elliptic curve Bn deﬁned by y2 = x3 − n2x. These
elliptic curves are associated to the classical congruent n umber problem. The following theorem is
a direct consequence of Theorem 1 in [17] by Heath-Brown.
Theorem 7.5. Let ℓ be a positive integer. As x → ∞ we have the asymptotic estimate
∑
n∈Q(x)
(#S2(Bn))ℓ ∼ 4ℓ+1
ℓ∏
j=1
(
1 + 2j)
· #Q(x).
In particular, there is a positive constant γ(ℓ) depending only on m such that for all x > 1 we have
∑
n∈Q(x)
(#S2(Bn))ℓ < γ (ℓ) · #Q(x).
The previous bound for the moments of # S2(Bn) allows us to prove Theorem 1.7.
Proof. All the elliptic curves Bn have j-invariant equal to 1728. For each squarefree positive inte ger
n, Theorem 1.1 with j0 = 1728 gives
max{βx(Bn), βy(Bn)} ≤ exp ((1 + rank Bn(Q))/c)
where c = c(1728) > 0 is an absolute constant. Given k > 0 we choose the positive integer
ℓ = ℓ(k) =
⌈ k
c log 2
⌉
where ⌈t⌉ is the smallest integer bigger than or equal to t. Thus, ℓ log 2 ≥ k/c and we deduce
max{βx(Bn), βy(Bn)}k ≤ 2(1+rank Bn(Q))·ℓ < # (Bn(Q)/2Bn(Q))ℓ
for each squarefree positive integer n. Here we used the classical fact that the rational torsion of
Bn is isomorphic to Z/2Z × Z/2Z, so that # ( Bn(Q)/2Bn(Q)) = 2 2+rank Bn(Q).
The fundamental injective map Bn(Q)/2Bn(Q) → S2(Bn(Q)) (cf. the exact sequence (1.2))
together with Theorem 7.5 ﬁnally give that for all x > 1
∑
n∈S(x)
max{βx(Bn), βy(Bn)}k < γ
(⌈ k
c log 2
⌉)
· #Q(x)
□
Finally, we remark that using Corollary 6.6 instead of Theor em 1.1, the same argument gives a
version of Theorem 1.7 for any non-constant rational functi on on Bn, not just x and y coordinates.
228. Acknowledgments
The ﬁrst author was supported by the FONDECYT Iniciaci´ on en Investigaci´ on grant 11170192,
and the CONICYT PAI grant 79170039. The second author was sup ported by FONDECYT Regular
grant 1190442.
We thank Dino Lorenzini and Eduardo Friedman for encouragin g us to extend our methods
beyond the case of arithmetic progressions in x and y-coordinates. Also, we are indebted to ´Eric
Gaudron for valuable suggestions regarding eﬀectivity.
References
[1] M. Bhargava, D. Kane, H. Lenstra, B. Poonen, E. Rains, Modeling the distribution of ranks, Selmer groups, and
Shafarevich-Tate groups of elliptic curves . Camb. J. Math. 3 (2015), no. 3, 275-321.
[2] M. Bhargava, N. Elkies, A. Shnidman, The average size of the 3-isogeny Selmer groups of elliptic curves y2 = x3+k.
Journal of the London Mathematical Society (2019). DOI: 10. 1112/jlms.12271
[3] E. Bombieri, The Mordell conjecture revisited . Annali della Scuola Normale Superiore di Pisa-Classe di Sc ienze,
1990, vol. 17, no 4, p. 615-640.
[4] J.-B. Bost, P´ eriodes et isog´ enies des vari´ et´ es ab´ eliennes sur lescorps de nombres . Ast´ erisque, tome 237 (1996),
S´ eminaire Bourbaki, exp. no 795, p. 115-161.
[5] A. Bremner, On arithmetic progressions on elliptic curves. Experimental Mathematics, 1999, vol. 8, no 4, p.
409-413.
[6] A. Bremner, J. Silverman, N. Tzanakis, Integral points in arithmetic progression on y2 = x(x2 − n2). Journal of
Number Theory, (2000) 80(2), 187-208.
[7] G. Campbell, A note on arithmetic progressions on elliptic curves . J. Integer Seq 6 (2003), no. 03.1.3.
[8] N. Elkies, Z28 in E(Q), etc. Listserv. 3 Apr. 2006. NmbrThry.
[9] G. Faltings, Endlichkeitss¨ atze f¨ ur abelsche Variet¨ aten ¨ uber Zahlk¨orpern. (German) [Finiteness theorems for abelian
varieties over number ﬁelds] Invent. Math. 73 (1983), no. 3, 349-366.
[10] G. Faltings, Diophantine approximation on abelian varieties . Annals of Mathematics, 133 (1991), 549-576.
[11] G. Faltings, The general case of S. Lang’s conjecture. Barsotti Symposium in Algebraic Geometry (Abano Terme,
1991). Perspect. Math. 15. Academic Press. San Diego. 1994. p. 175-182
[12] E. Fouvry, Sur le comportement en moyenne du rang des courbes y2 = x3 +k. S´ eminaire de Th´ eorie des Nombres,
Paris, 1990-91, Progr. Math (1993) 61-84.
[13] N. Garcia-Fritz, Quadratic sequences of powers and Mohanty’s conjecture . International Journal of Number
Theory 14.02 (2018), 479-507.
[14] I. Garcia-Selfa, J. Tornero. Searching for simultaneous arithmetic progressions on ell iptic curves. Bulletin of the
Australian Mathematical Society 71, no. 3 (2005): 417-424.
[15] ´E. Gaudron, G. R´ emond, Th´ eor` eme des p´ eriodes et degr´ es minimaux d’isog´ enies. Comment. Math. Helv. 89
(2014), no. 2, 343-403.
[16] R. Hartshorne, Algebraic geometry. Graduate Texts in Mathematics, No. 52. Springer- Verlag, Ne w York-
Heidelberg, 1977.
[17] D. R. Heath-Brown, The size of Selmer groups for the congruent number problem, I I. Inventiones Mathematicae,
(1994) vol. 118, no 1, p. 331-370.
[18] Y. Kawamata. On Bloch’s conjecture. Inv. Math. 57 (1980) 97-100.
[19] H. Lange, Principal polarizations on products of elliptic curves. (English summary) The geometry of Riemann
surfaces and abelian varieties, 153-162, Contemp. Math., 3 97, Amer. Math. Soc., Providence, RI, 2006.
[20] J. Lee, W. V´ elez, Integral solutions in arithmetic progression for y2 = x3 + k. Periodica Mathematica Hungarica
25, no. 1 (1992): 31-49.
[21] A. Levin, J. Wang, Greatest common divisors of analytic functions and Nevanli nna theory on algebraic tori .
arXiv preprint arXiv:1903.03876 (2019).
[22] H. Liao, M. Ru, A note on the second main theorem for holom orphic curves into algebraic varieties. Bulletin of
the Institute of Mathematics Academia Sinica (New Series) V ol. 9 (2014), No. 4, pp. 671-684
[23] X. Liu, G. Yu, Upper Bounds of GCD Counting Function for Holomorphic Maps . The Journal of Geometric
Analysis (2019) 29:1032-1042
[24] S. P. Mohanty, On consecutive integer solutions for y2 − k = x3. Proc. Amer. Math. Soc. 48 (1975), 281-285.
[25] S. P. Mohanty, Integer solutions in arithmetic progression for y2 − k = x3. Acta Mathematica Academiae
Scientiarum Hungaricae, (1980) 36, 261-265
23[26] D. Moody, A. Zargar, On the rank of elliptic curves with long arithmetic progress ions. In Colloquium Mathe-
maticum (Vol. 148, pp. 47-68). Instytut Matematyczny Polsk iej Akademii Nauk (2017).
[27] J. Park, B. Poonen, J. Voight, M. Wood. A heuristic for boundedness of ranks of elliptic curves . Journal of the
European Mathematical Society (2019). DOI: 10.4171/JEMS/ 893
[28] H. Pasten, Bounded ranks and Diophantine error terms. (2018) To appear in Mathematical Research Letters.
[29] H. Pasten, J. Wang, GCD Bounds for Analytic Functions . International Mathematics Research Notices (2017),
no. 1, 47-95.
[30] F. Pazuki, Theta height and Faltigs height . Bull. Soc. math. France 140 (1), (2012), p. 19-49.
[31] B. Poonen, Heuristics for the arithmetic of elliptic curves . Preprint (2017). arXiv: 1711.10112
[32] B. Poonen, E. Rains, Random maximal isotropic subspaces and Selmer groups . J. Amer. Math. Soc. 25 (2012),
no. 1, 245-269
[33] M. Raynaud, Sous-vari´ et´ es d’une vari´ et´ e ab´ elienne et points de torsion, In Arithmetic and geometry, Vol. I ,
volume 35 of Progr. Math., pages 327-352. Birkh¨ auser Boston, Boston, MA, 1983.
[34] G. R´ emond, D´ ecompte dans une conjecture de Lang. Inventiones Mathematicae, (2000) 142 (3), 513-545.
[35] G. R´ emond, Sur les sous-vari´ et´ es des tores. Compositio Mathematica 134.3 (2002) 337-366.
[36] J. Robertson, Magic Squares of Squares . Mathematics Magazine, Vol. 69, No. 4 (1996), pp. 289-293.
[37] K. Rubin, A. Silverberg, Ranks of elliptic curves in families of quadratic twists . Experiment. Math. 9 (2000), no.
4, 583-590.
[38] I. Shafarevitch, J. Tate, The rank of elliptic curves . Akad. Nauk SSSR 175 (1967), 770-773
[39] J. Silverman, Heights and elliptic curves . Arithmetic geometry (Storrs, Conn., 1984), 253-265, Spri nger, New
York, (1986).
[40] J. Silverman, The arithmetic of elliptic curves . Second edition. Graduate Texts in Mathematics, 106. Sprin ger,
Dordrecht, (2009). xx+513 pp. ISBN: 978-0-387-09493-9
[41] B. Spearman, Arithmetic progressions on congruent number elliptic curv es. The Rocky Mountain Journal of
Mathematics, Vol. 41, No. 6 (2011), pp. 2033-2044
[42] M. Ulas, Rational Points in Arithmetic Progressions on y2 = xn + k. Canadian Mathematical Bulletin 55, no. 1
(2012): 193-207.
[43] D. Ulmer, Elliptic curves with large rank over function ﬁelds , Ann. of Math. (2) 155 (2002), no. 1, 295-315
[44] P. Vojta, Siegel’s theorem in the compact case . Annals of Mathematics, 1991, p. 509-548.
[45] P. Vojta, Diophantine approximation and Nevanlinna theory . Arithmetic geometry, 111-224, Lecture Notes in
Math. 2009, Springer, Berlin (2011).
[46] M. Watkins, S. Donnelly, N. Elkies, T. Fisher, A. Granvi lle, N. Rogers, Ranks of quadratic twists of elliptic
curves, Publ. math. de Besan¸ con 2014/2 (2014), 63-98
Departamento de Matem ´aticas
Pontificia Universidad Cat ´olica de Chile
F acultad de Matem´aticas
4860 A v. Vicu ˜na Mackenna
Macul, RM, Chile
E-mail address, N. Garcia-Fritz: natalia.garcia@mat.uc.cl
Departamento de Matem ´aticas
Pontificia Universidad Cat ´olica de Chile
F acultad de Matem´aticas
4860 A v. Vicu ˜na Mackenna
Macul, RM, Chile
E-mail address, H. Pasten: hector.pasten@mat.uc.cl
24