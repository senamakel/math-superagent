<!-- source: https://matwbn.icm.edu.pl/ksiazki/aa/aa95/aa9534.pdf | converted from PDF -->

ACTA ARITHMETICA
XCV.3 (2000)

The Diophantine equation f (x) = g(y)

by

Yuri F. Bilu (Basel) and Robert F. Tichy (Graz)

1. Introduction. Let f (x) and g(x) be polynomials with rational
coeﬃcients. We study the following question: does the equation

(1) f (x) = g(y)

have ﬁnitely or inﬁnitely many solutions in rational integers x and y?
Due to the classical theorem of Siegel (see Theorem 10.1 below), the
ﬁniteness problem for (1), and even for a more general equation F (x, y) = 0
with F (x, y) ∈ Z[x, y], is decidable (1). One has to:

• decompose the polynomial F (x, y) into Q-irreducible factors;
• for those factors which are not Q-reducible, determine the genus g and
the number d of points at inﬁnity of the corresponding plane curve;
• for the factors with g = 0 and d ≤ 2 determine whether the corre-
sponding equation has ﬁnitely or inﬁnitely many integral solutions (see [4,
Section 1]).

Though this procedure completely solves the problem when the polyno-
mials f (x) and g(x) are given numerically, it is not very helpful when they
depend on unknown parameters, which often happens in applications.
In this paper we obtain a very explicit ﬁniteness criterion for the equa-
tion (1). It turns out to be more convenient to study a slightly more gen-
eral question: when does (1) have inﬁnitely many rational solutions with a
bounded denominator? We say that the equation F (x, y) = 0 has inﬁnitely

2000 Mathematics Subject Classiﬁcation: Primary 14H45; Secondary 11C08, 11D41,
11G30, 12E05, 12E10, 14H05, 14H25.
Key words and phrases: Ritt’s second theorem, Dickson polynomials, reducibility,
Diophantine equations.
The ﬁrst author supported by the Lise Meitner Fellowship (Austria), grant M00421-
MAT.
(
1) We mention in passing that the decidability of the existence problem (that is,
whether or not F (x, y) = 0 has at least one solution) is still an open question. The
answer, which is believed to be positive, is known only in particular cases.

[261]

262 Yu. F. Bilu and R. F. Tichy

many rational solutions with a bounded denominator if there exists a positive
integer ∆ such that F (x, y) = 0 has inﬁnitely many solutions (x, y) ∈ Q × Q
with ∆x, ∆y ∈ Z.
To formulate our criterion, we have to deﬁne ﬁve types of standard
pairs (f (x), g(x)).

1.1. Standard pairs. In what follows a and b are non-zero elements of
some ﬁeld, m and n are positive integers, and p(x) is a non-zero polynomial
(which may be constant).
A standard pair of the ﬁrst kind is

(x
m, ax
rp(x)
m)

or switched, (ax
rp(x)
m, x
m), where 0 ≤ r < m, (r, m) = 1 and r + deg p(x)
> 0.
A standard pair of the second kind is

(x
2, (ax
2 + b)p(x)
2)

(or switched).
Denote by Dm(x, a) the mth Dickson polynomial, deﬁned by

Dm(z + a/z, a) = zm + (a/z)
m

(see Section 3). A standard pair of the third kind is

(Dm(x, a
n), Dn(x, a
m)),

where gcd(m, n) = 1.
A standard pair of the fourth kind is

(a
−m/2Dm(x, a), −b−n/2Dn(x, b)),

where gcd(m, n) = 2.
A standard pair of the ﬁfth kind is

((ax
2 − 1)
3, 3x
4 − 4x
3)

(or switched).
When we want to specify that the parameters a and b and the coeﬃcients
of the polynomial p(x) belong to a ﬁeld K we say standard pair over K.
If (f (x), g(x)) is a standard pair over Q of the ﬁrst or third kind then (1)
has inﬁnitely many rational solutions with a bounded denominator. For
the third kind, an inﬁnite family of solutions is given by x = Dn(t, a) and
y = Dm(t, a), where t ∈ Z. For the ﬁrst kind, ﬁnd positive integers q
and s with qm − sr = 1. Then an inﬁnite family of solutions is given by
x = a
qtrp(a
stm) and y = a
stm, where t ∈ Z.
If (f (x), g(x)) is a standard pair over Q of the second, fourth or ﬁfth kind
then (1) has inﬁnitely many rational solutions with a bounded denominator
for inﬁnitely many choices of the parameters a and b.

Diophantine equation f (x) = g(y) 263

For instance, for the second kind let (u, v) satisfy u2 = av2 + b. Then
x = up(v) and y = v is a solution of (1). Hence (1) has inﬁnitely many
rational solutions with a bounded denominator whenever u2 = av2 + b does,
which happens for inﬁnitely many choices of a and b.
For the fourth kind (where we assume, without loss of generality, that
n/2 is odd), let (u, v) be a solution of a
m/2u2 + bv2 = 4ab. Then x =
a
(2−n)/4Dn/2(v, a) and y = uEm/2(v, a) (where En(t, a) is deﬁned in (8)) is
a solution of (1), as follows from Proposition 3.1.
For the ﬁfth kind, let (u, v) be a solution of 3au2 = v2 + 2. Then
x = u(v + 2) and y = ((v + 1)
3 + 4)/3 is a solution of (1).

1.2. The criterion

Theorem 1.1. Let f (x), g(x) ∈ Q[x] be non-constant polynomials. Then
the following two assertions are equivalent.

(1.1.a) The equation (1) has inﬁnitely many rational solutions with a
bounded denominator.
(1.1.b) We have f = ϕ ◦ f1 ◦ λ and g = ϕ ◦ g1 ◦ µ, where λ(x), µ(x) ∈
Q[x] are linear polynomials, ϕ(x) ∈ Q[x], and (f1(x), g1(x)) is a
standard pair over Q such that the equation f1(x) = g1(y) has
inﬁnitely many rational solutions with a bounded denominator.

We make several comments on this result.

Remark 1.2. (i) The implication (1.1.b)⇒(1.1.a) is trivial. The non-
trivial part is (1.1.a)⇒(1.1.b).
(ii) If gcd(deg f, deg g) = 1 then in (1.1.b) we have deg ϕ = 1, and
(f1(x), g1(x)) is a standard pair of the ﬁrst or third kind (over Q). This
reproduces a result of Schinzel [27, Theorem 8].
(iii) Write f = apx
p + . . . + a0 and g = bqx
q + . . . + b0, and assume
that ap/bq is not a perfect power in Q. Then in (1.1.b) we have deg ϕ = 1.
(Indeed, ap/bq = (a
′/b′)
deg ϕ, where a
′ and b′ are the leading coeﬃcients
of f1 and g1, respectively.) Using this, one can easily prove, for instance,
that the equation ( x
m ) = y(y − 1) . . . (y − n + 1) has ﬁnitely many solutions
in integers x and y, when m and n are integers greater than 2. This was
originally done by Brindza and Pint´er [9].
(iv) One can express the assertion “f1(x) = g1(y) has inﬁnitely many
rational solutions with a bounded denominator” as an explicit arithmetical
condition on the parameters a and b. For instance, for the second kind
this means that a is positive, not a square, and b = NQ(√
a)/Qβ for some
β ∈ Q(
√a). For the other kinds one can proceed similarly. We do not
go into this because we ﬁnd Theorem 1.1 in its present form completely
suﬃcient for applications.

264 Yu. F. Bilu and R. F. Tichy

(v) Actually, we obtain a more general result, on solutions of (1) in
S-integers of an arbitrary number ﬁeld (see Theorem 10.5). In this case one
more kind of pairs can occur; to distinguish it from the standard pairs just
deﬁned, we call this new kind speciﬁc pairs (see Section 9).
(vi) Various applications of Theorem 1.1 will be given in the forthcoming
papers [6, 8]. In particular, we solve the Diophantine problem involving
Meixner polynomials, studied in [22]. (Beukers, Shorey and Tijdeman [3]
considered another type of equations of the form (1), using methods very
similar to ours.)

1.3. Un peu d’histoire. Finiteness conditions for the equation (1) were
studied by many authors. For the equation f (x) = yn a ﬁniteness theorem
was established by Siegel [29] and LeVeque [24]. Evertse and Silverman [13]
obtained a sharp estimate for the number of solutions. (See also a more
recent paper of Voutier [34].)
Starting from Baker [2], methods for the eﬀective analysis of the equation
f (x) = yn were developed by Sprindˇzuk, Trelina, Brindza, Poulakis, Voutier
and Bugeaud; see [31, 10] for the references. An eﬃcient algorithm for the
numerical solution of this equation was suggested in [7].
Davenport, Lewis and Schinzel [12] obtained a ﬁniteness condition for the
general equation (1). However, it was too restrictive for many applications.
Fried investigated the problem from various points of view in a remark-
able series of paper [16, 17, 18]. In particular, he gave in [18, Corollary after
Theorem 3] a new ﬁniteness condition, much more general than that of [12],
but still far from explicit.
Schinzel [27, Theorem 8] obtained a completely explicit ﬁniteness crite-
rion for the equation (1) under the assumption (deg f, deg g) = 1. His result
is, basically, Remark 1.2(ii) of our paper.
Quite recently, Beukers, Shorey and Tijdeman [3] applied a similar ap-
proach to certain particular types of the equation (1).

1.4. An overview of the paper. The proof of Theorem 1.1 follows the
main lines of the arguments of Fried [18] and Schinzel [27]. However, sev-
eral substantially new ideas were required to drop Schinzel’s assumption
(deg f, deg g) = 1, retaining the explicit character of his result.
Call an absolutely irreducible polynomial F (x, y) ∈ Q[x, y] exceptional
if the corresponding plane curve is of genus 0 and has at most 2 points at
inﬁnity. To deduce Theorem 1.1 from Siegel’s theorem, one has to determine
when the polynomial f (x) − g(y) has an exceptional factor.
Our argument consists of two parts. In the ﬁrst part (Sections 4–7) we
show that if the polynomial f (x) − g(y) itself is exceptional then (f, g) is a
standard pair up to a linear transformation and linear change of variables.
This generalizes the classical “Second theorem of Ritt”.

Diophantine equation f (x) = g(y) 265

In the second part (Sections 8–10) we classify pairs (f, g) such that f (x)−
g(y) has an exceptional factor. Due to a clever observation of Fried (see
Theorem 8.1) this reduces to solving two independent problems.

(a) Determine when f (x) − g(y) has a factor of degree at most 2.
(b) Given a polynomial q(x, y) of degree at most two, determine for
which f (x) and g(x) the polynomial q(f (x), g(y)) is exceptional.

Problem (a) is completely solved in [5]. The solution of (b) depends
on whether ∂2q/∂x∂y vanishes or not. If it does, then q(f (x), g(y)) can
be written as f1(x) − g1(y), reducing the problem to the generalized Ritt’s
second theorem, just proved. If ∂2q/∂x∂y ̸= 0 then the solution of (b) is
remarkably simple (see Proposition 9.2).
After all this work is done, our ﬁniteness criterion becomes an (almost)
immediate consequence of Siegel’s theorem (see Section 10).

Acknowledgments. We are pleased to thank Roberto Maria Avanzi,
Frits Beukers, Michael Fried, Peter M¨uller, Attila Peth˝o, Andrzej Schinzel,
Robert Tijdeman, Gerhard Turnwald and Umberto Zannier for stimulating
discussions and helpful suggestions. We are especially grateful to Andrzej
Schinzel for detecting a number of inaccuracies in the text.

2. Terminology, notation, conventions

2.1. General. We use (a, b) for the greatest common divisor of a and b,
when a and b are either integers or polynomials (in the latter case (a, b) is
well deﬁned up to a multiplicative constant). When it can be confused with
(a, b) as an ordered pair, we write gcd(a, b).
We denote by ⌊x⌋ the maximal integer not exceeding x ∈ R.

2.2. Fields. All ﬁelds in this paper are of characteristic 0 (although
some of the results are valid in arbitrary characteristic). The capital letter
K (with or without indices) always stands for a ﬁeld. We assume that all
ﬁelds that occur in the paper are contained in one big algebraically closed
(unnamed) ﬁeld. In particular, any ﬁeld K has a well deﬁned algebraic
closure K, any two ﬁelds K and K ′ have well deﬁned intersection K ∩ K ′

and composite KK ′, etc.

2.3. Polynomials. All polynomials are assumed non-constant, unless the
contrary is stated explicitly. Given a polynomial f (x) having s distinct roots
(in an algebraically closed ﬁeld), its root type is the array (µ1, . . . , µs) formed
of the multiplicities of its roots. Obviously, µ1 +. . .+µs = deg f . The f -type
of a scalar γ is the root type of the polynomial f (x) − γ. When it is clear
which polynomial is referred to, we say simply “type” instead of “f -type”.
If f (x) − γ has at least one multiple root (in other terms, if the f -type of γ
is distinct from (1, . . . , 1)) then γ is called an extremum of f (x).

266 Yu. F. Bilu and R. F. Tichy

Given a polynomial f (x) ∈ K[x] and γ ∈ K of type (µ1, . . . , µs), put

δf (γ) = (µ1 − 1) + . . . + (µs − 1) = deg f − s

(so that δf (γ) > 0 if and only if γ is an extremum of f ). Then

(2) ∑

γ∈K δf (γ) = deg f − 1.

To see this, notice that δf (γ) = deg gcd(f − γ, f ′). Hence the sum in (2) is
equal to deg f ′ = deg f − 1, as wanted. Equality (2) will often be used in
the paper, sometimes without special reference.

2.4. Curves and function ﬁelds. Let F (x, y) ∈ K[x, y] be an absolutely
irreducible polynomial. By points of the plane curve F (x, y) = 0 we always
mean algebraic points, i.e. places of its function ﬁeld K(x, y). (With a
standard abuse of notation, we use x, y for both independent variables and
coordinate functions on the plane curve.) The place is inﬁnite if it is a pole
of x or y. The corresponding point of the plane curve is called a point at
inﬁnity.
Similarly, by the genus of a plane curve we always mean the genus of its
function ﬁeld.

3. Dickson polynomials. In this section, we collect miscellaneous
facts about Dickson polynomials.
For a ∈ K, the nth Dickson polynomial Dn(x, a) is deﬁned from the
relation

(3) Dn(z + a/z, a) = zn + (a/z)
n.

The following identities will often be used in the paper, sometimes without
special reference:
 D1(x, a) = x; D2(x, a) = x
2 − 2a;(4)
 Dmn(x, a) = Dm(Dn(x, a), an);(5)
 bnDn(x, a) = Dn(bx, b2a);(6)
 D2n(x, a) − 2a
n = (x
2 − 4a)En(x, a)
2,(7)

where the polynomial En(x, a) is deﬁned from the relation

(8) En(z + a/z, a) = (zn − (a/z)
n)/(z − a/z).

The proofs of (4)–(7) are immediate, upon substituting x = z + a/z into
both sides.
An important consequence of (6) is

(9) (a, cos 2α ∈ K) ⇒ (Dn(x cos α, a) ∈ K[x]).

Here is a slightly less obvious consequence of (4)–(7).

Diophantine equation f (x) = g(y) 267

Proposition 3.1. Let m, n be positive even numbers with n/2 odd. Then

(10) a
m/2u2 + bv2 = 4ab
⇓
a
−m/2Dm(a
(2−n)/4Dn/2(v, a), a) = −b−n/2Dn(uEm/2(v, a), b).

P r o o f. This is just a calculation:

−b−n/2Dn(uEm/2(v, a), b) = Dn/2(−D2(uEm/2(v, a)/√b, 1), 1)

= Dn/2(2 − b−1u2Em/2(v, a)
2, 1)

= Dn/2(2 + a
−m/2(v2 − 4a)Em/2(v, a)
2, 1)

= Dn/2(a
−m/2Dm(v, a), 1)

= Dmn/2(v/
√a, 1)

= a
−m/2Dm(a
(2−n)/4Dn/2(v, a), a),

as wanted.

For further facts about Dickson polynomials, including equivalent deﬁ-
nitions, diﬀerential equations, etc., see [25, Chapter 2] and [32].

3.1. Factorization. It is well known that Dn(x, a) + Dn(y, a) splits into
factors of degree at most two. More precisely, put

(11) Φn(x, y, a) = ∏

1≤k<n
k≡1 mod 2
 (x
2 − 2xy cos(πk/n) + y2 − 4a sin
2(πk/n)).

Then

(12) Dn(x, a) + Dn(y, a) = { Φn(x, y, a) if n is even,
(x + y)Φn(x, y, a) if n is odd

(see, for instance, [5, Proposition 3.1]). If a ̸= 0 then the factors on the
right-hand side of (11) are absolutely irreducible.

3.2. Semi-deﬁnite polynomials. Call a polynomial F (x, y) ∈ R[x, y] semi-
deﬁnite if there exist positive constants X, C and A such that |F (x, y)| ≥
C max(|x|, |y|)
A as soon as max(|x|, |y|) ≥ X. The following properties of
semi-deﬁnite polynomials are immediate.

Proposition 3.2. (i) A product of semi-deﬁnite polynomials is semi-
deﬁnite.
(ii) If F (x, y) is semi-deﬁnite and f (x), g(x) are non-constant real poly-
nomials then F (f (x), g(y)) is semi-deﬁnite.
(iii) If F (x, y) is semi-deﬁnite then the level set {(x, y) ∈ R2 : F (x, y) =
C} is bounded for any C ∈ R.

268 Yu. F. Bilu and R. F. Tichy

Proposition 3.3. Let a be a real number. If d = gcd(m, n) is even then
the polynomial

(13) Dm(x, a
n/d) + Dn(y, a
m/d)

is semi-deﬁnite. If d = gcd(m, n) is odd and greater than 1 then the poly-
nomial

(14) Dm(x, a
n/d) + Dn(y, a
m/d)
Dm/d(x, an/d) + Dn/d(y, am/d)

is semi-deﬁnite.

P r o o f. One immediately veriﬁes that all the quadratic factors in (11)
are semi-deﬁnite, which implies that the polynomial Φn(x, y, a) is semi-
deﬁnite for n > 1. Since each of the polynomials (13) and (14) is equal
to Φd(Dm/d(x, a
n/d), Dn/d(x, a
m/d), amn/d), the result follows.

4. The genus formula. Let f (x), g(x) be polynomials over a ﬁeld K
of degrees m, n respectively. Given γ ∈ K of f -type (µ1, . . . , µs) and g-type
(ν1, . . . , νt), deﬁne the quantities

Ω(γ) = ∑

1≤i≤s
 ∑

1≤j≤t
(µi, νj),

σ(γ) = ∑

1≤i≤s
 ∑

1≤j≤t
(µi − (µi, νj)) = mt − Ω(γ),

τ (γ) = ∑

1≤i≤s
 ∑

1≤j≤t
(νj − (µi, νj)) = ns − Ω(γ).

Obviously, mn − Ω(γ) = σ(γ) = τ (γ) = 0 for all but ﬁnitely many γ ∈ K.

Proposition 4.1. Assume that f (x) = g(y) is an absolutely irreducible
plane curve of genus g. Then

2g − 2 = ∑

γ∈K σ(γ) − m − d = ∑

γ∈K τ (γ) − n − d(15)
 = ∑

γ∈K(mn − Ω(γ)) − mn − d,

where d = (m, n).

P r o o f. This is due to Fried [17, Proposition 2 on page 240]. Since our
notation is very diﬀerent from Fried’s, we include a proof for the convenience
of the reader.
We use the Riemann–Hurwitz formula

(16) 2g − 2 = ∑

P (eP − 1) − 2n,

Diophantine equation f (x) = g(y) 269

where the sum extends to the places P of the function ﬁeld K(x, y) and eP
is the ramiﬁcation index of the place P over the ﬁeld K(x).
Fix α, β, γ ∈ K satisfying

(17) f (α) = g(β) = γ.

Let µ be the order of the root α of the polynomial f − γ, and ν the order
of the root β of the polynomial g − γ. Then there are exactly (µ, ν) places
P of K(x, y) with the property

(18) x(P ) = α and y(P ) = β,

and eP = ν/(µ, ν) for every such P . It follows that
∑

P satisﬁes (18)(eP − 1) = ν − (µ, ν).

Deﬁning z ∈ K(x, y) by z = f (x) = g(y), we obtain

∑

z(P )=γ(eP −1) = ∑

(α,β) satis-
ﬁes (17)
 ∑

P satisﬁes (18)(eP −1) =
 s∑

i=1
 t∑

j=1(νj −(µi, νj)) = τ (γ).

Also, there exist d = (m, n) places P with x(P ) = y(P ) = ∞, and eP = n/d
for every such P . Hence ∑

z(P )=∞
(eP − 1) = n − d.

Now

2g − 2 = ∑

γ∈K
 ∑

z(P )=γ(eP − 1) + ∑

z(P )=∞
(eP − 1) − 2n = ∑

γ∈K τ (γ) − n − d,

which proves the second formula in (15). The ﬁrst formula follows by sym-
metry. Finally, using (2), we obtain
∑

γ∈K τ (γ) − n − d = ∑

γ∈K((m − δf (γ))n − Ω(γ)) − n − d

= ∑

γ∈K(mn − Ω(γ)) − n ∑

γ∈K δf (γ) − n − d

= ∑

γ∈K(mn − Ω(γ)) − mn − d,

which proves the last formula in (15).

5. Polynomials with a few extrema. It is well known that Dickson
polynomials Dn(x, a) with a ̸= 0 have exactly two extrema. More precisely,
one has the following.

270 Yu. F. Bilu and R. F. Tichy

Proposition 5.1. If a ̸= 0 and n ≥ 3 then Dn(x, a) has exactly two
extrema ±2a
n/2. If n is odd then both are of type (1, 2, . . . , 2). If n is even
then 2a
n/2 is of type (1, 1, 2, . . . , 2), and −2a
n/2 is of type (2, . . . , 2).

For a proof see, for instance [5, Proposition 3.3].

It is of fundamental importance that, basically, the Dickson polynomials
are characterized by this property. We shall use this classical fact in the
following form.

Theorem 5.2. Let f (x) ∈ K[x] be a polynomial of degree m having ex-
actly two extrema in K. Moreover , let its extrema be of one of the following
types:

(19) (2, . . . , 2), (1, 2, . . . , 2), (1, 1, 2, . . . , 2).

Then f (x) = αDm(x + β, a) + γ, where a, α ∈ K ∗ and β, γ ∈ K.

P r o o f. We use induction on m. If m is odd then both the extrema are
of the type (1, 2, . . . , 2). In this case the assertion is a particular case of [32,
Lemma 1.11] (reproduced in [25] as Lemma 6.16).
Now assume that m is even, and write m = 2n. Since f (x) has two
extrema, we have m ≥ 4. By (2), one of the extrema is of type (2, . . . , 2)
and the other is of type (1, 1, 2, . . . , 2). Since the extrema have distinct types,
they both belong to K. Without loss of generality we may assume that the
polynomial f (x) is monic and that the extremum of type (2, . . . , 2) is 0.
This means that f (x) = g(x)
2, where g(x) ∈ K[x] is a monic polynomial of
degree n.
If n = 2 then g(x) = D2(x + β, a), where a, β ∈ K. Moreover, a ̸= 0,
because g(x) has simple roots.
Now assume that n = deg g > 2. Let κ ̸= 0 be the other extremum of
f (x). Then (g(x) − √κ)(g(x) + √κ) has 2 simple roots, all the other roots
being of order 2. It follows that ±
√κ are extrema of g(x), of one of the
types from (19). Identity (2) applied to the polynomial g(x) certiﬁes that
it has no other extrema. By induction, g(x) = αDn(x + β, a) + γ, where
a, α ∈ K ∗ and β, γ ∈ K. Since g(x) is monic, α = 1. Since its extrema ±
√κ
are symmetric with respect to 0, we have γ = 0.
Thus, in either the case n = 2 or n > 2 we have g(x) = Dn(x + β, a),
where a ∈ K ∗ and β ∈ K. It follows that f (x) = g(x)
2 = Dm(x+β, a)+2a
n,
as wanted.

Corollary 5.3. Let f (x) ∈ K[x] and γ1, γ2 ∈ K be such that f (x) − γi
has at most si simple roots, where s1 + s2 ≤ 2. (We assume that γ1 ̸= γ2.)
Then f (x) = αDm(x + β, a) + γ, where a, α ∈ K ∗ and β, γ ∈ K.

P r o o f. We may assume that m = deg f ≥ 3, since otherwise there is
nothing to prove. In particular, both γ1 and γ2 are extrema of f .

Diophantine equation f (x) = g(y) 271

We have

(20) δf (γi) ≥ (m − si)/2 (i = 1, 2),

the equality being attained when f (x) − γi has si simple and (m − si)/2
double roots. On the other hand, (2) implies that

(m − s1)/2 + (m − s2)/2 = m − 1 ≥ δf (γ1) + δf (γ2).

Hence we have equalities in (20), and f has no extrema other than γi. We
have shown that f satisﬁes the assumptions of Theorem 5.2.

Corollary 5.4. Let f (x) ∈ K[x] be a polynomial of degree m such that
for some b ∈ K ∗, the polynomial f (x)
2 − 4b has at most 2 roots of odd order.
Then for some linear polynomial λ(x) ∈ K[x] one of the following options
takes place.

(5.4.a) The degree m is even, b is a perfect square in K, and f (x) =√bDm(λ(x)
√a, 1), for some a ∈ K and a suitable choice of the
sign of √b.
(5.4.b) The degree m is odd , and f (x) = √bDm(λ(x)
√b, 1).

P r o o f. As b ̸= 0, the polynomial f (x) satisﬁes the assumption of Corol-
lary 5.3. Hence f (x) = αDm(x + β, a) + γ, where a, α ∈ K ∗ and β, γ ∈ K.
The extrema of f (x) are ±2√b, which implies γ = 0 and b = α2a
m. If m
is even then f (x) = αa
m/2Dm(λ(x)
√a, 1), where λ(x) = (x + β)/a. If m is
odd then f (x) = √bDm(λ(x)
√b, 1), where λ(x) = (x + β)α−1a
−(m+1)/2.

Proposition 5.5. If f (x) ∈ K[x] has only one extremum then f (x) =
a(x − α)
m + γ, where a, α, γ ∈ K and a ̸= 0.

P r o o f. If γ is the extremum then (2) implies that its f -type is (n), and
the result follows.

6. Ritt’s second theorem. Let f1(x), g1(x), f2(x), g2(x) be polyno-
mials over K. We say that pairs (f1, g1) and (f2, g2) are equivalent over K
(notation: (f1, g1) K
∼ (f2, g2)) if there exist (non-constant) linear polynomi-
als ℓ(x), λ(x), µ(x) ∈ K[x] such that f1 = ℓ ◦ f2 ◦ λ and g1 = ℓ ◦ g2 ◦ µ.

Theorem 6.1. Let f (x), g(x) ∈ K[x] be polynomials of degree m and n
respectively. Assume that d = gcd(m, n) ≤ 2, and that

(21) f (x) = g(y)

is an absolutely irreducible plane curve of genus 0. Then (f, g) K
∼ (f1, g1),
where (f1, g1) is a standard pair over K.

The case d = 1 of this theorem follows from the classical “second theorem
of Ritt” [26], as presented, for instance, in [27, Section 5]. The case d = 2

272 Yu. F. Bilu and R. F. Tichy

was examined by Fried [18, Theorem 3]. We give, however, a much more
explicit classiﬁcation of the possible pairs (f, g).
Recently, Avanzi and Zannier [1] classiﬁed the pairs (f, g) over an al-
gebraically closed ﬁeld and over Q such that gcd(deg f, deg g) = 1 and the
genus of f (x) = g(y) is 1. Extending their result to number ﬁelds leads to
interesting problems in the arithmetic of elliptic curves.
Theorem 6.1 will be proved in the next section. We conclude this section
with several auxiliary statements required for the proof.
As the genus formula suggests, we have to deal with sums of the form∑
(µi, νj). Some simple properties of such sums are listed in the following
lemma.

Lemma 6.2. Let µ1, . . . , µs and ν1, . . . , νt be positive integers, and put

(22) m = µ1 + . . . + µs, n = ν1 + . . . + νt, Ω = ∑

1≤i≤s
 ∑

1≤j≤t
(µi, νj).

Then

(i) We have Ω ≤ sn, the equality being attained when every νj divides
every µi.
(ii) If min(µ1, . . . , µs) = 1, then Ω ≤ n(s − 1) + t.
(iii) (Schinzel) If gcd(µ1, . . . , µs, ν1, . . . , νt) = 1, then

Ω ≤ max(m(t − 1) + s, n(s − 1) + n/2).

P r o o f. (i) For every i we have (µi, ν1)+. . .+(µi, νt) ≤ ν1 +. . .+νt = n,
the equality being attained when every νj divides this µi. Summing up over
i, we complete the proof.
(ii) Say, let µ1 = 1. Then

(µi, ν1) + . . . + (µi, νt) { = t if i = 1,
≤ n if i ≥ 2.

We again complete the proof, summing up over i.
(iii) We consider two cases.

Case 1: For every i either

there exists a j with (µi, νj) = 1, or(23)
 there exist distinct j1 and j2 such that µi does not divide νj1 and νj2.(24)

If for a given i we have (23) then

(µi, ν1) + . . . + (µi, νt) ≤ (t − 1)µi + 1.

If we have (24) then (µi, νj1) and (µi, νj2) do not exceed µi/2, and

(µi, ν1) + . . . + (µi, νt) ≤ (t − 1)µi < (t − 1)µi + 1.

Summing up over i, we obtain Ω ≤ (t − 1)(µ1 + . . . + µs) + s = (t − 1)m + s.

Diophantine equation f (x) = g(y) 273

Case 2: There exist i0 and j0 such that

(25) j ̸= j0 ⇒ µi0 | νj and d := (µi0, νj0) > 1.

It follows from (25) that d divides ν1, . . . , νt. But

gcd(µ1, . . . , µs, ν1, . . . , νt) = 1,

whence d does not divide at least one of the numbers µi, say, µ1. It follows
that none of the νj divides µ1, which implies that (µ1, νj) ≤ νj/2 for all j.
Therefore
 (µi, ν1) + . . . + (µi, νt) ≤ { n/2 if i = 1,
n if i ≥ 2.

Summing up over i, we obtain Ω ≤ (s − 1)n + n/2. The proof is complete.

The following trivial observation will often be used.

Proposition 6.3. If f (x) − γ has at least r simple roots then τ (γ) ≥
rδg(γ) (we use the notation of Section 4).

P r o o f. At least r of the numbers µ1, . . . , µs are equal to 1, say, µ1 =
. . . = µr = 1. Hence

τ (γ) ≥
 r∑

i=1
 t∑

j=1(νj − (µi, νj)) =
 r∑

i=1
 t∑

j=1(νj − 1) = rδg(γ),

as wanted.

Finally, we consider three simple particular cases of Theorem 6.1.

Proposition 6.4. In the set-up of Theorem 6.1 assume that m ≥ 3,
n ≥ 2 and f (x) = a(x−α)
m+γ. Then d = 1 and g(x) = b(x−β)
rg1(x)
m+γ,
where 0 < r < m, b ∈ K ∗, β ∈ K and the polynomial g1(x) ∈ K[x] may be
constant.

P r o o f. Plainly, γ ∈ K. Hence we may write g(x) = g2(x)g1(x)
m + γ,
where g1, g2 ∈ K[x] and the root type of g1 is (ν1, . . . , νt) with νi < m. We
have

(26) gcd(m, ν1, . . . , νt) = 1,

since otherwise the curve (21) would have been reducible.
The second formula in (15) implies that −2 = 2g − 2 = σ(γ) − m − d
(because σ(γ′) = 0 for γ′ ̸= γ). Further,

σ(γ) =
 t∑

j=1(m − (m, νj)) > tm/2,

because (m, νj) ≤ m/2 for all j, and (m, νj) < m/2 for at least one j
(otherwise we violate (26)).

274 Yu. F. Bilu and R. F. Tichy

If t ≥ 2 then −2 > (t − 2)m/2 − d, a contradiction. Thus, t = 1, which
completes the proof.

Proposition 6.5. In the set-up of Theorem 6.1 assume that m = 2 and
f (x) = a(x − α)
2 + γ. Then g(x) = g1(x)
2g2(x) + γ, where g2(x) ∈ K[x] is
a separable polynomial of degree at most 2, and the polynomial g1(x) ∈ K[x]
may be constant.

P r o o f (similar to the proof of Proposition 6.4 and simpler). Now we
have ν1 = . . . = νt = 1 and σ(γ) = t. The genus formula reads −2 = t−2−d,
which yields t = deg g2 = d ≤ 2, as desired.

Proposition 6.6. In the set-up of Theorem 6.1 assume that n is odd ,
m, n ≥ 3 and g(x) = Dn(x, b), where b ∈ K ∗. Then for some linear polyno-
mial λ(x) ∈ K[x] we have the following.

(i) If m is odd then f (x) = b(n−m)/2Dm(λ(x), b).
(ii) If m is even then b is a perfect square in K, and we have f (x) =
a
−m/2bn/2Dn(λ(x), a) for some a ∈ K ∗ and for a suitable choice of the sign
of bn/2.

P r o o f. By Proposition 5.1, g(x) has two extrema ±bn/2, both of type
(1, 2, . . . , 2). Let s+ (respectively, s−) be the number of odd entries in the
f -type of bn/2 (respectively, −bn/2). Then τ (±bn/2) = s±(n − 1)/2, and the
second formula in (15) implies that −2 ≥ (s++ s−)(n−1)/2−n−1. It follows
that s+ + s− = 2, and Corollary 5.3 implies that f (x) = αDm(x + β, a) + γ,
where α, a ∈ K ∗ and β, γ ∈ K.
The extrema of f are ±αam/2 + γ. On the other hand, they are ±bn/2.
It follows that γ = 0 and

(27) α = εa
−m/2bn/2,

where ε ∈ {1, −1} depends on the signs of a
−m/2 and bn/2.
Now recall that α ∈ K. If m is even, then (27) implies that b is a
perfect square in K, say, b = b2
1. The sign of b1 can be deﬁned to have
f (x) = a
−m/2bn
1 Dn(λ(x), a), which completes the proof in this case.
If m is odd then (27) implies that a/b is a perfect square in K, say, b =
ac
2. We deﬁne that sign of c so that (27) turns to f (x) = b(n−m)/2Dn(λ(x), b)
with λ(x) = c(x + β). This completes the proof also in this case.

7. Proof of Theorem 6.1. Everywhere in this section “equivalent”
means “equivalent over K”, and “standard pair” means “standard pair over
K”.
If min(m, n) = 1 then (f, g) is equivalent to a standard pair of the ﬁrst
kind. If min(m, n) = 2 then (f, g) is equivalent to a standard pair of the

Diophantine equation f (x) = g(y) 275

ﬁrst or second kind by Proposition 6.5. Hence we may assume that

min(m, n) ≥ 3.

We use the quantities σ(γ), etc., deﬁned at the beginning of Section 4. We
start with the following observation.

Assertion 1. Let γ ∈ K have f -type (µ1, . . . , µs) and g-type (ν1, . . . , νt).
Then

(28) gcd(µ1, . . . , µs, ν1, . . . , νt) = 1.

Indeed, assume that for some γ we have q = gcd(µ1, . . . , µs, ν1, . . . , νt)
> 1. Then both f (x) − γ and g(x) − γ are qth powers in the ring K[x],
which contradicts the irreducibility of the curve (21).

The following assertion is just a reformulation of Lemma 6.2(iii).

Assertion 2. For any γ ∈ K either σ(γ) ≥ δf (γ), or τ (γ) ≥ n/2.

We say that γ ∈ K is a σ-point (respectively, τ -point) (
2) if δf (γ) > σ(γ)
(respectively, δg(γ) > τ (γ)). Reformulating item (ii) of Lemma 6.2, we
obtain the following.

Assertion 3. If γ is a τ -point then f (x) − γ has no simple roots. In
particular , δf (γ) ≥ m/2.

It follows that there can be at most one σ-point and at most one τ -point.

Case 1: There exist a σ-point γ1 and a τ -point γ2.

Subcase 1.1: γ1 = γ2. We follow [27, pp. 37–38] with some changes.
Assertion 2 implies that

δf (γ1) > σ(γ1) ≥ m/2, δg(γ1) > τ (γ1) ≥ n/2.

Write δf (γ1) = m/2 + κ and δg(γ1) = n/2 + λ. Without loss of generality
κ ≥ λ. Assume that g(x) has an extremum γ3 ̸= γ1. Since

δf (γ3) ≤ m − 1 − δf (γ1) = m/2 − κ − 1,

the polynomial f (x)−γ3 has at least 2κ+2 simple roots. By Proposition 6.3

τ (γ3) ≥ (2κ + 2)δg(γ3) ≥ δg(γ3) + 2κ + 1.

We also have τ (γ1) ≥ δg(γ1) − λ ≥ δg(γ1) − κ,

and τ (γ) ≥ δg(γ) for γ ̸= γ1, γ3. By the genus formula (15),

−2 = ∑

γ∈K τ (γ) − n − d ≥ ∑

γ∈K δg(γ) + κ + 1 − n − d = κ − d > −d,

a contradiction.

(
2) In Ritt’s [26] terminology, extra point of f (respectively, g).

276 Yu. F. Bilu and R. F. Tichy

Thus, g(x) cannot have an extremum distinct from γ1. Proposition 5.5
implies that g(x) = a(x − α)
n + γ1, and Proposition 6.4 implies that (f, g)
is equivalent to a standard pair of the ﬁrst kind.

Subcase 1.2: γ1 ̸= γ2. By Assertion 3,

(29) δf (γ1) ≥ m/2, δg(γ2) ≥ n/2,

and by Lemma 6.2,

(30) Ω(γ1) ≤ n(m − δf (γ1)), Ω(γ2) ≤ m(n − δg(γ2)).

Using (29), (30) and Proposition 4.1, we obtain

−2 = ∑

γ∈K(mn − Ω(γ)) − mn − d

≥ (mn − Ω(γ1)) + (mn − Ω(γ2)) − mn − d(31)
 ≥ δf (γ1)n + δg(γ2)m − mn − d

≥ −d.(32)

Thus, d = 2, and inequalities (31) and (32) are equalities. This has the
following consequences:

• Ω(γ) = mn for any γ ̸= γ1, γ2. This implies that f and g have no
extrema distinct from γ1 and γ2.
• Inequalities (29) are equalities, which implies that the f -type of γ1 and
the g-type of γ2 are (2, . . . , 2).
• Inequalities (30) are equalities. Hence Lemma 6.2(i) together with (2)
implies that the f -type of γ2 and the g-type of γ1 are (1, 1, 2, . . . , 2).

Now Theorem 5.2 implies

f (x) = αDn(x + β, a) + γ, g(x) = α′Dn(x + β′, b) + γ′.

Since

γ1 = −αa
m/2 + γ = α′bn/2 + γ′, γ2 = αa
m/2 + γ = −α′bn/2 + γ′,

we have γ = γ′ and αa
m/2 = −α′bn/2, which shows that (f, g) is equivalent
to a standard pair of the fourth kind. This completes the proof in Case 1.

Case 2: There exist no σ-point. If f has a single extremum, then
f (x) = a(x − α)
m + γ by Proposition 5.5, which reduces the theorem to
Proposition 6.4.
From now on assume that

(33) f has at least two distinct extrema.

Subcase 2.1: For every extremum γ of f , the polynomial g − γ has at
most one simple root. Let γ1 and γ2 be two distinct extrema of f (which
exist by (33)). Since g − γ1 and g − γ2 have at most one simple root, we

Diophantine equation f (x) = g(y) 277

have δg(γ1), δg(γ2) ≥ (n − 1)/2. Since δg(γ1) + δg(γ2) ≤ n − 1, we have
δg(γ1) = δ(γ2) = (n − 1)/2 and the polynomial g has no extrema other than
γ1 and γ2. Also, both γ1 and γ2 have g-type (1, 2, . . . , 2). In particular, n
is odd and d = 1.
It follows from Theorem 5.2 that g(x) = αDn(x + β, b) + γ, where α, b ∈
K ∗ and β, γ ∈ K. If m is even then Proposition 6.6 implies that b = b2
1,
where b1 ∈ K ∗, and f (x) = αa
−m/2bn
1 Dm(λ(x), a) + γ. Writing

f (x) = αa
−mn/2bn
1 Dm(a
(n−1)/2λ(x), an) + γ,

g(x) = αa
−mn/2bn
1 Dn(a
(m−1)/2b−1
1 (x + β), am) + γ,

we conclude that (f, g) is equivalent to a standard pair of the third kind.
If m is odd then Proposition 6.6 implies that

f (x) = αb(n−m)/2Dn(λ(x), b) + γ.

Writing
 f (x) = αb−n(m+1)/2Dn(b(n−1)/2λ(x), bn) + γ,

g(x) = αb−n(m+1)/2Dn(b(m−1)/2(x + β), bm) + γ,

we again see that (f, g) is equivalent to a standard pair of the third kind.

Subcase 2.2: For some extremum γ1 of f , the polynomial g − γ1 has at
least two simple roots. Since the argument in this subcase is rather lengthy,
we divide it into short logically complete steps.

Step 1: The f -type and further properties of γ1. By Proposition 6.3 we
have σ(γ1) ≥ 2δf (γ1). Since there is no σ-point, σ(γ) ≥ δf (γ) for all γ ∈ K.
By the genus formula,

−2 = σ(γ1)+ ∑

γ̸=γ1 σ(γ)−n−d ≥ 2δf (γ1)+ ∑

γ̸=γ1 δf (γ)−n−d = δf (γ1)−1−d.

Since γ1 is an extremum of f , we have δf (γ1) ≥ 1. Hence

d = 2, δf (γ1) = 1, σ(γ1) = 2,(34)
 σ(γ) = δf (γ) (γ ̸= γ1).(35)

It follows from (34) that the f -type of γ1 is (2, 1, . . . , 1).

Step 2: The deﬁnition of γ2. Equality (35) together with Proposition 6.3
implies that for any extremum γ of f (x), distinct from γ1, the polynomial
g(x) − γ has at most one simple root. Since n is even, δg(γ) ≥ n/2 for any
such γ. Also, (34) and Proposition 6.3 imply that g(x) − γ1 has exactly two
simple roots, whence δg(γ1) ≥ (n − 2)/2. It follows that f has exactly two
extrema, one of which is γ1; denote the other by γ2. Since δg(γ1) + δg(γ2) ≥
(n − 2)/2 + n/2 = n − 1, these γ1 and γ2 are the only extrema of g as well,

278 Yu. F. Bilu and R. F. Tichy

and

(36) δg(γ1) = (n − 2)/2, δg(γ2) = n/2.

Step 3: Possible g-types of γ1 and γ2. As we have seen in the previous
step, g(x) − γ2 has at most one simple root, and g(x) − γ1 has exactly two
simple roots. Comparing this with (36), we conclude that the g-type of γ1
is (1, 1, 2, . . . , 2), and the g-type of γ2 is either (1, 3, 2, . . . , 2) or (2, . . . , 2).

Step 4: Possible m and n. The third genus formula (15) implies that
−2 = mn − Ω(γ1) − Ω(γ2) − 2. The f - and g-types of γ1 being known, one
ﬁnds Ω(γ1) = mn/2 + m − 2. Hence

(37) Ω(γ2) = mn/2 − m + 2.

On the other hand, by Lemma 6.2(i),

(38) Ω(γ2) ≤ n(m − δf (γ2)) = n(δf (γ1) + 1) = 2n.

Comparing (37) and (38), we obtain

(39) m ≤ (2n − 2)/(n/2 − 1),

which implies one of the following options:

m = 6, n = 4,(40)
 m = 4, n ≡ 2 (mod 4).(41)

Step 5: Impossibility of (41). In case (41) we have δf (γ2) = 3 − δf (γ1) =
2, and the f -type of γ2 can be either (2, 2) or (1, 3).
Notice that the f -type (2, 2) and the g-type (2, . . . , 2) together vio-
late (28). There remain three possibilities for the f - and g-types of γ2,
respectively:

(1, 3) and (1, 3, 2, . . . , 2); (2, 2) and (1, 3, 2, . . . , 2); (1, 3) and (2, . . . , 2).

In the ﬁrst case Ω(γ2) = n + 2, in the second case Ω(γ2) = 2n − 4, and in
the third case Ω(γ2) = n. In any case, this contradicts (37), which shows
that (41) is impossible.

Step 6: The f - and g-types of γ2. Thus, we have (40). Moreover, we
have equality in (38), which means, by Lemma 6.2(i), that

(42) every entry of the g-type of γ2 divides every entry of its f -type.

This shows that the g-type (2, 2) is impossible (it violates (28)), and the
single possibility for the g-type of γ2 is (1, 3). By (42), the only possible
f -type for γ2 is (3, 3).

Step 7: Normalizing γ1 and γ2. Since f has no extrema of type (3, 3)
other than γ2, we have γ2 ∈ K. Similarly, γ1 ∈ K. Replacing f and g by
(f − γ2)/(γ2 − γ1) and (g − γ2)/(γ2 − γ1), we may assume that γ1 = −1 and
γ2 = 0.
 Diophantine equation f (x) = g(y) 279

Step 8: The polynomial f . Since γ2 = 0 is an extremum of f of type
(3, 3), we have f (x) = αf1(x)
3, where α ∈ K ∗ and f1(x) ∈ K[x] is a
separable quadratic polynomial. After a linear change of the variable we
may write f1(x) = a1x
2 − a2, where a1, a2 ∈ K ∗. The second extremum
of f is −αa3
2 = γ1 = −1. Thus, α = a
−3
2 and f (x) = (ax
2 − 1)
3, where
a = a1/a2.
Step 9: The polynomial g. Since γ2 = 0 has g-type (1, 3), we may write,
after a linear change of variable, that g(x) = (px − q)x
3, where p, q ∈ K ∗.
The second extremum of g is −27q4/(256p3) = −1. Hence (q/4)
4 = (p/3)
3 =
θ12
1 , where θ1 ∈ K ∗. Thus, q/4 = θ3
1ξ4 and p/3 = θ4
1ξ3, where ξ3 and ξ4
are third and fourth root of unity, respectively (not necessarily primitive).
Notice that ξ3, ξ4 ∈ K. Putting θ = θ1ξ−1
3 ξ4, we obtain q = 4θ3 and p = 3θ4.
Thus, g(x) = 3(θx)
4 − 4(θx)
3.
We have shown that (f, g) is equivalent to a standard pair of the ﬁfth
kind. The theorem is proved.

8. Irreducible factors of f (x) − g(y). Everywhere in this section
“irreducible” means “irreducible over K”, and “factor” means “K-factor”,
unless the contrary is stated explicitly.
Given f (x) ∈ K[x], denote by ℧f the splitting ﬁeld of f (x) − t over K(t)
(where t is a new indeterminate). Two polynomials f (x) and g(x) are called
similar if ℧f = ℧g.
A place of ℧f is called inﬁnite if it lies over the inﬁnite place of K(t).
The ramiﬁcation index (over K(t)) of any inﬁnite place of ℧f is equal to
deg f . It follows that

(43) similar polynomials have equal degrees.

Fried [16, Proposition 2] observed that the problem of factoring polyno-
mials of the form f (x) − g(y) reduces to the case of similar f and g.

Theorem 8.1 (Fried). Given f (x), g(x) ∈ K[x], there exist similar poly-
nomials f1(x), g1(x) ∈ K[x], and polynomials f2(x), g2(x) ∈ K[x] such that

f = f1 ◦ f2, g = g1 ◦ g2,

and
• for every irreducible factor F1(x, y) of f1(x) − g1(y), the polynomial
F (x, y) := F1(f2(x), g2(y)) is irreducible;
• every irreducible factor of f (x) − g(y) is of the form F1(f2(x), g2(y)),
where F1(x, y) is an irreducible factor of f1(x) − g1(y).
Thereby,

(44) F1(x, y) ↔ F (x, y) := F1(f2(x), g2(y))

gives a one-to-one correspondence between the irreducible factors of f1(x) −
g1(y) and of f (x) − g(y).

280 Yu. F. Bilu and R. F. Tichy

P r o o f. We give a proof for the convenience of the reader. We use
induction on deg f + deg g. If f (x) − t has a root in ℧g and g(x) − t has a
root in ℧f then ℧f = ℧g and there is nothing to prove. Therefore we may
assume that, say, g(x) − t has no root in ℧f .
Let y1 be a root of g(x) − t. By assumption, y1 ̸∈ ℧f . We have a tower
of rational ﬁelds: K(t) ⊆ ℧f ∩ K(y1) ⊊ K(y1).

The inﬁnite place of the ﬁeld K(t) totally ramiﬁes in K(y1). Hence it totally
ramiﬁes in the intermediate ﬁeld ℧f ∩K(y1). Therefore ℧f ∩K(y1) = K(y2),
where y2 is integral over the ring K[t]. We have t = ̃g(y2) ∈ K[y2] and
y2 = ̂g(y1) ∈ K[y1]. It is important to notice that deg ̃g < deg g, because
K(y2) is a proper subﬁeld of K(y1).
Now let F (x, y) = aq(y)x
q + . . . + a0(y) be a factor of f (x) − g(y). Then
a0(y1), . . . , aq(y1) are polynomials in the roots of f (x) − g(y1) = f (x) − t.
Hence a0(y1), . . . , aq(y1) ∈ ℧f . It follows that

a0(y1), . . . , aq(y1) ∈ ℧f ∩ K(y1) = K(y2).

Therefore ai(y) = ̃ai(̂g(y)), where ̃a0(y), . . . , ̃aq(y) ∈ K[y].
Obviously, ̃F (x, y) := ̃aq(y)x
q + . . . + ̃a0(y) is a factor of f (x) − ̃g(y). We
have proved that every factor of f (x) − g(y) is of the form ̃F (x, ̂g(y)), where
̃F (x, y) is a factor of f (x) − ̃g(y).
Conversely, for any factor ̃F (x, y) of f (x)−̃g(y), the polynomial F (x, y) =
̃F (x, ̂g(y)) is a factor of f (x) − g(y), distinct ̃F giving rise to distinct F .
Hence ̃F (x, y) ↔ F (x, y) := ̃F (x, ̂g(y))

is a one-to-one correspondence between the factors of f (x) − ̃g(y) and of
f (x) − g(y). Moreover, since this correspondence preserves the divisibility
relation, it restricts to a one-to-one correspondence between the irreducible
factors of f (x) − ̃g(y) and of f (x) − g(y).
Since deg ̃g < deg g, there exist, by induction, similar polynomials f1(x),
g1(x) ∈ K[x], and polynomials f2(x), ̃g2(x) ∈ K[x] such that f = f1 ◦ f2,
̃g = g1 ◦ ̃g2 and F1(x, y) ↔ ̃F (x, y) := F1(f2(x), ̃g2(y)) is a one-to-one
correspondence between the irreducible factors of f1(x)−g1(y) and of f (x)−
̃g(y). Putting g2 = ̃g2 ◦ ̂g, we complete the proof.

As Fried indicated in [18], the study of the Diophantine equation
f (x) = g(y) requires classiﬁcation of polynomials of the form f (x) − g(y)
having quadratic factors. This problem is solved in [5].

Theorem 8.2. Let f (x) and g(x) be polynomials over K, and let q(x, y) ∈
K[x, y] be an irreducible (over K) factor of f (x) − g(y) of degree at most 2.

Diophantine equation f (x) = g(y) 281

Then there exist polynomials ϕ(x), f1(x), g1(x) ∈ K[x] such that f = ϕ ◦ f1,
g = ϕ ◦ g1 and one of the following two options takes place.

(8.2.a) We have max(deg f1, deg g1) = 2 and q(x, y) = f1(x) − g1(y).
(8.2.b) There exists an integer n > 2 with cos(2π/n) ∈ K such that for
some α ∈ K ∗ and a, β, γ ∈ K we have

f1(x) = Dn(x + β, a), g1(x) = −Dn((αx + γ) cos(π/n), a),

and q(x, y) is a quadratic factor of f1(x) − g1(y). If q(x, y) is
absolutely irreducible then a ̸= 0.

P r o o f. See [5, Theorem 1.3].

Note in conclusion that the problem of factorization of f (x) − g(y) has a
long history, which cannot be presented here. We just mention that among
the contributors were Cassels, Davenport, Feit, Fried, Lewis, Schinzel, Tver-
berg, and many others. In particular, Tverberg [33, Chapter 2] obtained
some results complementary to Theorem 8.2. Fried [16, Theorem 1 on
pp. 141–142] proved that if f is an indecomposable (
3) polynomial of degree
n and K contains no complex subﬁeld of Q(e
2πi/n) (in particular, if K = Q),
then f (x) − g(y) is reducible (over Q) only in trivial cases. He also showed
that the problem with indecomposable f and general K reduces to a certain
problem in group theory, studied by Feit [14]. For further advances see [15,
19, 20]. Quite recently, Cassou-Nogu`es and Couveignes [11], essentially us-
ing the previous work of Fried and Feit, and assuming the classiﬁcation of
ﬁnite simple groups, completely classiﬁed the pairs of polynomials f, g with
indecomposable f such that f (x) − g(y) is reducible (4).

9. Exceptional factors of f (x) − g(y) and speciﬁc pairs. An ab-
solutely irreducible polynomial F (x, y) ∈ K[x, y] is called exceptional if the
plane curve F (x, y) = 0 is of genus 0 and has at most two points at inﬁnity.
In this section we use Theorems 8.1 and 8.2 to classify polynomials of
the form f (x) − g(y) having exceptional factors.

Proposition 9.1. Let Φ(x, y), f (x, y), g(x, y) ∈ K[x, y] be non-constant
polynomials such that Φ(f (x, y), g(x, y)) is an exceptional polynomial. As-
sume that f and g are algebraically independent over K. Then Φ(x, y) itself
is an exceptional polynomial.

P r o o f. First, since Ψ (x, y) = Φ(f (x, y), g(x, y)) is absolutely irreducible,
so is Φ(x, y).

(
3) A polynomial is indecomposable if it is not a composition of two polynomials of
smaller degree.
(
4) Cassou-Nogu`es and Couveignes assume that both f and g are indecomposable.
But [16, assertion (2.38) on p. 142] implies that the assumption about g can be dropped.

282 Yu. F. Bilu and R. F. Tichy

Second, the ﬁeld K(u, v) of rational functions on the curve Φ(u, v) = 0 is
contained in the ﬁeld K(x, y) of rational functions on the curve Ψ (x, y) = 0,
the embedding being deﬁned by u ↦→ f (x, y) and v ↦→ g(x, y). By the L¨uroth
theorem, the curve Ψ (x, y) = 0 is of genus 0.
Third, since f (x, y) and g(x, y) are polynomials, the inﬁnite places of
the ﬁeld K(x, y) restrict to the inﬁnite places of the ﬁeld K(u, v). Since the
former ﬁeld has at most 2 inﬁnite places, so does the latter.

Proposition 9.2. Let q(x, y) = αx
2 + 2βxy + γy2 + δ ∈ K[x, y] be a
quadratic polynomial with αβγδ(β2 −αγ) ̸= 0. Let f (x), g(x) ∈ K[x] be non-
constant polynomials of degrees m and n, respectively, such that q(f (x), g(y))
is an exceptional polynomial. Then (m, n) = 1. Furthermore, deﬁne b =
δγ/(4(β2 − αγ)). Then for some linear polynomial λ(x) ∈ K[x] one of the
following options takes place.
(9.2.a) The degree m is even, b is a perfect square in K, and f (x) =√bDm(λ(x)
√a, 1) for some a ∈ K and a suitable choice of the
sign of √b.
(9.2.b) The degree m is odd and f (x) = √bDm(λ(x)
√b, 1).
We have similar options for g(x) with c = δα/(4(β2 − αγ)) instead of b,
and with another linear polynomial µ(x) instead of λ(x).

P r o o f. The plane curve q(f (x), g(y)) = 0 has 2 gcd(m, n) points at
inﬁnity, which implies that gcd(m, n) = 1.
Further, since q(f (x), g(y)) is exceptional, so is

γq(f (x), y) = (γy − βγyf (x))
2 − (β2 − αγ)(f (x)
2 − 4b),

as well as y2 − (β2 − αγ)(f (x)
2 − 4b). By Proposition 6.5, the polynomial
f (x)
2 − 4b has at most two roots of odd order. We complete the proof using
Corollary 5.4.

To formulate the main result of this section, we need to deﬁne one more
kind of pairs, which we call speciﬁc (
5). A speciﬁc pair over K is

(Dm(x, a
m/d), −Dn(x cos(π/d), an/d))

(or switched), where d = gcd(m, n) ≥ 3 and a, cos(2π/d) ∈ K. Notice that
−Dn(x cos(π/d), an/d) ∈ K[x] by (9).

Theorem 9.3. Let f (x), g(x) ∈ K[x] be such that f (x) − g(y) has an ex-
ceptional factor E(x, y). Then there exist a standard or speciﬁc pair (f1, g1)
over K, linear polynomials λ(x), µ(x) ∈ K[x], and a polynomial ϕ(x) ∈ K[x]
such that f = ϕ ◦ f1 ◦ λ and g = ϕ ◦ g1 ◦ µ. Also, E(x, y) is equal to
f1 ◦ λ(x) − g1 ◦ µ(y) times a constant if (f1, g1) is standard , and E(x, y)
divides f1 ◦ λ(x) − g1 ◦ µ(y) if (f1, g1) is speciﬁc.

(
5) This term has no intuitive meaning: speciﬁc pairs are neither “less standard” nor
“more speciﬁc” than standard pairs.

Diophantine equation f (x) = g(y) 283

P r o o f. All polynomials that occur in the proof have coeﬃcients in K
unless the contrary is stated explicitly.
Let f = f3 ◦ f2 and g = g3 ◦ g2 be the decompositions from Theorem 8.1
(we write f3 and g3 instead of f1 and g1). In particular,

(45) deg f3 = deg g3.

Then E(x, y) = q(f2(x), g2(y)), where q(x, y) is an absolutely irreducible
factor of f3(x) − g3(y).
It follows from (45) that the curve q(x, y) = 0 has exactly deg q points
at inﬁnity. Since q is exceptional (by Proposition 9.1), we have deg q ≤ 2.
Theorem 8.2 implies that f3 = ϕ1 ◦ f4 and g3 = ϕ1 ◦ g4, where either

(46) q(x, y) = f4(x) − g4(y),

or for some integer ν > 2 we have

(47) f4(x) = Dν(x + β, a), g4(x) = −Dν((αx + γ) cos(π/ν), a),

ν > 2, cos(2π/ν) ∈ K, q(x, y) | (f4(x) − g4(y)),

where a, α ∈ K ∗ and β, γ ∈ K. Put f5 = f4 ◦ f2 and g5 = g4 ◦ g2.
In the case (46) we have E(x, y) = f5(x) − g5(y). Since E(x, y) has d =
gcd(deg f5, deg g5) points at inﬁnity, we have d ≤ 2. Applying Theorem 6.1,
we conclude that f5 = ℓ ◦ f1 ◦ λ and g5 = ℓ ◦ g1 ◦ µ, where ℓ(x), λ(x), µ(x)
are linear polynomials and (f1, g1) is a standard pair over K.
Obviously, E(x, y) is equal to f1(λ(x)) − g1(µ(y)) times a constant.
Putting ϕ = ϕ1 ◦ ℓ, we complete the proof in the case (46).
Now assume (47). By (11), for some positive integer k we have q(x, y) =
qk(x + β, αy + γ), where

qk(x, y) = x
2 − 2xy cos(πk/ν) cos(π/ν) + y2 cos2(π/ν) − 4a sin
2(πk/ν).

Put f6 = f2 + β and g6 = αg2 + γ. Then E(x, y) = qk(f6(x), g6(y)) is an
exceptional polynomial, which, by Proposition 9.2, implies that

(48) gcd(m′, n′) = 1,

where m′ = deg f6 and n′ = deg g6. Without loss of generality, n′ is odd.
Furthermore, Proposition 9.2 implies that

g6(x) = (cos(π/ν))
−1√aDn′(µ1(x) cos(π/ν)
√a, 1),

and that either m′ is odd and

f6(x) = √aDm′(λ1(x)
√a, 1),

or m′ is even, a is a perfect square in K, and for some a
′ ∈ K ∗ and a suitable
choice of the sign of √a we have

f6(x) = √aDm′(λ1(x)
√a′, 1).

Here λ1(x) and µ1(x) are linear polynomials.

284 Yu. F. Bilu and R. F. Tichy

Putting m = m′ν and n = n′ν, we obtain

g5(x) = −Dν(g6(x) cos(π/ν), a)

= −(
√a)
−νDν((
√a)
−1g6(x) cos(π/ν), 1)

= −(
√a)
−νDν(Dn′(µ1(x)
√a cos(π/ν), 1), 1)

= −(
√a)
−νDn(µ1(x)
√a cos(π/ν), 1)

= { −a
−(ν+mn/ν)/2Dn(µ(x) cos(π/ν), am/ν) if m′ is odd,
−(
√a)
−ν(a
′)
−mn/(2ν)Dn(µ(x) cos(π/ν), (a
′)
m/ν) if m′ is even.

(Recall that √a ∈ K when m′ is even.) Here

µ(x) = { µ1(x)a
(1+m/ν)/2 if m′ is odd,
µ1(x)(a
′)
m/(2ν)√a if m′ is even.

A similar calculation shows that

f5(x) = { a
−(ν+mn/ν)/2Dm(λ(x), an/ν) if m′ is odd,
(
√a)
−ν(a
′)
−mn/(2ν)Dn(λ(x), (a
′)
n/ν) if m′ is even,

where
 λ(x) = { λ1(x)a
(1+n/ν)/2 if m′ is odd,
λ1(x)(a
′)
(1+n/ν)/2 if m′ is even.

Further, ν = d = gcd(m, n) by (48), which implies that d > 2 and cos(2π/d)
∈ K by (47). Thus, f5 = Af1 ◦ λ and g5 = Ag1 ◦ µ, where

A = { a
(ν+mn/ν)/2 if m′ is odd,
(
√a)
ν(a
′)
mn/(2ν) if m′ is even,

and (f1, g1) is a speciﬁc pair over K.
Finally, since q(x, y) | (f4(x) − g4(y)), the polynomial E(x, y) =
q(f2(x), g2(y)) divides f5(x) − g5(y) = A(f1(λ(x)) − g1(µ(y))). Putting
ϕ(x) = ϕ1(x/A), we complete the proof in the case (47) as well.

10. The Diophantine equation. Let R be a commutative integral do-
main with quotient ﬁeld K, and F (x, y) ∈ K[x, y]. We say that the equation
F (x, y) = 0 has inﬁnitely many solutions with a bounded R-denominator if
there exists a non-zero ∆ ∈ R such that F (x, y) = 0 has inﬁnitely many
solutions (x, y) ∈ K × K with ∆x, ∆y ∈ R.
In this section K is a number ﬁeld, and S a ﬁnite set of places of K
containing all Archimedean places. We denote by OS the ring of S-integers
of the ﬁeld K.
Recall the classical theorem of Siegel [30] (see also [23, 28]).

Theorem 10.1 (Siegel). Let F (x, y) ∈ K[x, y] be an absolutely irreducible
polynomial. If the equation F (x, y) = 0 has inﬁnitely many solutions with
a bounded OS-denominator , then the polynomial F (x, y) is exceptional , as
deﬁned at the beginning of Section 9.

Diophantine equation f (x) = g(y) 285

We need several simple auxiliary results.

Proposition 10.2. Let F (x, y) ∈ K[x, y] be irreducible over K but re-
ducible over K. Then the equation F (x, y) = 0 has at most ﬁnitely many
solutions (x, y) ∈ K × K.

P r o o f. This is well known (and very simple); see, for instance, [31,
beginning of Section 9.6].

Proposition 10.3. Let K be a totally real number ﬁeld , O its ring of
integers, and let F (x, y) ∈ K(x, y) have the following property: for any
embedding σ : K → R, the polynomial σF is semi-deﬁnite (see Subsec-
tion 3.2). Then the equation F (x, y) = 0 has only ﬁnitely many solutions
with a bounded O-denominator.

P r o o f. By Proposition 3.2(iii), there is a constant c = c(F ) such that
max(|σ(x)|, |σ(y)|) ≤ c(F ) for any (x, y) ∈ K 2 satisfying F (x, y) = 0 and
for any embedding σ : K → R.
Fix ∆ ∈ O. Let (x, y) ∈ K 2 be a solution of F (x, y) = 0 with ∆x, ∆y ∈
O. Then ∆x, ∆y are algebraic integers with all conjugates bounded. Hence
there are only ﬁnitely many possibilities for x and y. This completes the
proof.

Corollary 10.4. Let K be a totally real number ﬁeld , O its ring of
integers and a ∈ K ∗. Then we have the following.

(i) If d = gcd(m, n) is even then the equation

Dm(x, a
n/d) + Dn(y cos(π/d), am/d) = 0

has only ﬁnitely many solutions with a bounded O-denominator.
(ii) If d = gcd(m, n) is odd and the equation

Dm(x, a
n/d) + Dn(y, a
m/d) = 0

has inﬁnitely many solutions with a bounded O-denominator , then all of
them with ﬁnitely many exceptions satisfy

Dm/d(x, a
n/d) + Dn/d(y, a
m/d) = 0.

P r o o f. This follows from Propositions 3.3 and 10.3.

Now we are ready to prove the main result of this paper.

Theorem 10.5. Let K be number ﬁeld , S a ﬁnite set of places of K con-
taining all Archimedean places, and f (x), g(x) ∈ K[x]. Then the following
two assertions are equivalent.

(10.5.a) The equation f (x) = g(y) has inﬁnitely many solutions with a
bounded OS-denominator.

286 Yu. F. Bilu and R. F. Tichy

(10.5.b) We have f = ϕ◦f1 ◦λ and g = ϕ◦g1 ◦µ, where λ(x), µ(x) ∈ K[x]
are linear polynomials, ϕ(x) ∈ K[x], and (f1(x), g1(x)) is a stan-
dard or speciﬁc pair over K such that the equation f1(x) = g1(y)
has inﬁnitely many solutions with a bounded OS-denominator.

If K is totally real and S is the set of Archimedean places (in particular , if
K = Q and OS = Z) then the word “speciﬁc” in (10.5.b) may be skipped.

P r o o f. Only (10.5.a)⇒(10.5.b) is to be proved (the converse is obvious).
Thus, assume (10.5.a). Then there exists a K-irreducible factor E(x, y)
of f (x) − g(y) such that the equation E(x, y) = 0 has inﬁnitely many solu-
tions with a bounded OS-denominator. By Proposition 10.2, the polynomial
E(x, y) is absolutely irreducible. By Siegel’s theorem, E(x, y) is exceptional.
Now Theorem 9.3 implies that f = ϕ ◦ f1 ◦ λ and g = ϕ ◦ g1 ◦ µ, where ϕ,
f1, g1, λ and µ are as required.
Further, since E(x, y) divides f1 ◦λ(x)−g1 ◦µ(y), the equation f1 ◦λ(x) =
g1 ◦ µ(y) has inﬁnitely many solutions with a bounded OS-denominator.
Hence so does the equation f1(x) = g1(y).
Now assume that K is totally real, S the set of its Archimedean places,
and (f1, g1) a speciﬁc pair. That is,

f1(x) = Dm(x, a
n/d) and g1(x) = −Dn(x cos(π/d), am/d),

where d = gcd(m, n) ≥ 3 and a, cos(2π/d) ∈ K.
Since f1(x) = g1(y) has inﬁnitely many solutions with a bounded OS-
denominator, Corollary 10.4(i) implies that d is odd. Therefore cos(π/d) ∈
K. Now, f = ̃ϕ ◦ ̃f1 ◦ ̃λ and g = ̃ϕ ◦ ̃g1 ◦ ̃µ with

̃ϕ(x) = ϕ(Dd(εx, a
mn/d
2)),
̃f1(x) = Dm/d(x, a
n/d), ̃g1(x) = Dn/d(x, a
m/d),
̃λ(x) = ελ(x), ̃µ(x) = −εµ(x) cos(π/d),

where ε = (−1)
m. Notice that ( ̃f1, ̃g1) is a standard pair (of the third kind).
It remains to show that ̃f1(x) = ̃g1(y) has inﬁnitely many solutions with
a bounded OS-denominator. Since cos(π/d) ∈ K, the equation

f1(x) − g1(y/ cos(π/d)) = Dm(x, a
n/d) + Dn(x, a
m/d) = 0

has inﬁnitely many solutions with a bounded OS-denominator. By Corol-
lary 10.4(ii), so does the equation Dm/d(x, a
n/d) = −Dn/d(x, a
m/d). Since
either m/d or n/d is odd, the equation ̃f1(x) = ̃g1(y) has the same property.
The theorem is proved.

Theorem 1.1 is a particular case of Theorem 10.5.

Diophantine equation f (x) = g(y) 287

References

[1] R. M. A v a n z i and U. Z a n n i e r, Genus one curves deﬁned by separated variable
polynomials, Acta Arith., to appear.
[2] A. B a k e r, Bounds for solutions of superelliptic equations, Proc. Cambridge Philos.
Soc. 65 (1969), 439–444.
[3] F. B e u k e r s, T. N. S h o r e y and R. T i j d e m a n, Irreducibility of polynomials and
arithmetic progressions with equal product of terms, in: [21], pp. 11–26.
[4] Yu. B i l u, Integral points and Galois covers, Mat. Contemp. 14 (1998), 1–11.
[5] —, Quadratic factors of f (x) − g(y), Acta Arith. 90 (1999), 341–355.
[6] Yu. F. B i l u, B. B r i n d z a, ´A. P i n t´e r and R. F. T i c h y, On some diophantine
problems related to power sums and binomial coeﬃcients, in preparation.
[7] Yu. B i l u and G. H a n r o t, Solving superelliptic Diophantine equations by Baker’s
method, Compositio Math. 112 (1998), 273–312.
[8] Yu. F. B i l u, T. S t o l l and R. F. T i c h y, Diophantine equations for the Meixner
polynomials, in preparation.
[9] B. B r i n d z a and ´A. P i n t´e r, On the irreducibility of some polynomials in two
variables, Acta Arith. 82 (1997), 303–307.
[10] Y. B u g e a u d, Bounds for the solutions of superelliptic equations, Compositio Math.
107 (1997), 187–219.
[11] P. C a s s o u - N o g u`e s et J.-M. C o u v e i g n e s, Factorisations explicites de g(y)−h(z),
Acta Arith. 87 (1999), 291–317.
[12] H. D a v e n p o r t, D. J. L e w i s and A. S c h i n z e l, Equations of the form f (x) = g(y),
Quart. J. Math. Oxford Ser. (2) 12 (1961), 304–312.
[13] J.-H. E v e r t s e and J. H. S i l v e r m a n, Uniform bounds for the number of solutions
to Y n = f (X), Math. Proc. Cambridge Philos. Soc. 100 (1986), 237–248.
[14] W. F e i t, On symmetric balanced incomplete block designs with doubly transitive
automorphism groups, J. Combin. Theory Ser. A 14 (1973), 221–247.
[15] —, Some consequences of the classiﬁcation of ﬁnite simple groups, in: Proc. Sym-
pos. Pure Math. 37, Amer. Math. Soc., 1980, 175–181.
[16] M. F r i e d, The ﬁeld of deﬁnition of function ﬁelds and a problem in the reducibility
of polynomials in two variables, Illinois J. Math. 17 (1973), 128–146.
[17] —, Arithmetical properties of function ﬁelds (II). The generalized Schur problem,
Acta Arith. 25 (1973/74), 225–258.
[18] —, On a theorem of Ritt and related Diophantine problems, J. Reine Angew. Math.
264 (1974), 40–55.
[19] —, Exposition on an arithmetic-group theoretic connection via Riemann’s existence
theorem, in: Proc. Sympos. Pure Math. 37, Amer. Math. Soc., 1980, 571–601.
[20] —, Variables separated polynomials, the genus 0 problem, and moduli spaces, in:
[21], pp. 169–228.
[21] K. G y ˝o r y, H. I w a n i e c and J. U r b a n o w i c z (eds.), Number Theory in Progress
(Proc. Internat. Conf. in Number Theory in Honor of A. Schinzel, Zakopane,
1997), de Gruyter, 1999.
[22] P. K i r s c h e n h o f e r, A. P e t h ˝o and R. F. T i c h y, On analytical and Diophantine
properties of a family of counting polynomials, Acta Sci. Math. (Szeged) 65 (1999),
47–59.
[23] S. L a n g, Fundamentals of Diophantine Geometry, Springer, 1983.
[24] W. J. L e V e q u e, On the equation ym = f (x), Acta Arith. 9 (1964), 209–219.
[25] R. L i d l, G. L. M u l l e n and G. T u r n w a l d, Dickson Polynomials, Pitman Mono-
graphs Surveys Pure Appl. Math. 65, Longman Sci. Tech., 1993.

288 Yu. F. Bilu and R. F. Tichy

[26] J. F. R i t t, Prime and composite polynomials, Trans. Amer. Math. Soc. 23 (1922),
51–66.
[27] A. S c h i n z e l, Selected Topics on Polynomials, The Univ. of Michigan Press, Ann
Arbor, 1982.
[28] J.-P. S e r r e, Lectures on the Mordell–Weil Theorem, Aspects Math. E15, Vieweg,
Braunschweig, 1989.
[29] C. L. S i e g e l, The integer solutions of the equation y2 = axn + bx
n−1 + . . . + k,
J. London Math. Soc. 1 (1926), 66–68; also: Gesammelte Abhandlungen, Band 1,
207–208.
[30] —, ¨Uber einige Anwendungen Diophantischer Approximationen, Abh. Preuss. Akad.
Wiss. Phys.-Math. Kl., 1929, Nr. 1; also: Gesammelte Abhandlungen, Band 1,
209–266.
[31] V. G. S p r i n dˇz u k, Classical Diophantine Equations in Two Unknowns, Nauka,
Moscow, 1982 (in Russian); English transl.: Lecture Notes in Math. 1559, Springer,
1994.
[32] G. T u r n w a l d, On Schur’s conjecture, J. Austral. Math. Soc. 58 (1995), 312–357.
[33] H. A. T v e r b e r g, A study in irreducibility of polynomials, Ph.D. thesis, Dept. of
Math., Univ. of Bergen, 1968.
[34] P. M. V o u t i e r, On the number of S-integral solutions to Y m = f (X), Monatsh.
Math. 119 (1995), 125–139.

Mathematisches Institut
Universit¨at Basel
Rheinsprung 21
4051 Basel, Switzerland
E-mail: yuri@math.unibas.ch
 Institut f¨ur Mathematik (A)
Technische Universit¨at Graz
Steyrergasse 30
8010 Graz, Austria
E-mail: tichy@weyl.math.tu-graz.ac.at

Received on 17.12.1999 (3730)
