<!-- source: https://www.ams.org/journals/bull/1990-23-01/S0273-0979-1990-15899-9/S0273-0979-1990-15899-9.pdf | converted from PDF -->

BULLETIN (New Series) OF THE
AMERICAN MATHEMATICAL SOCIETY
Volume 23, Number 1, July 1990

OLD AND NEW CONJECTURED
DIOPHANTINE INEQUALITIES

SERGE LANG *

The original meaning of diophantine problems is to find all so-
lutions of equations in integers or rational numbers, and to give a
bound for these solutions. One may expand the domain of coef-
ficients and solutions to include algebraic integers, algebraic num-
bers, polynomials, rational functions, or algebraic functions. In
the case of polynomial solutions, one tries to bound their degrees.
Inequalities concerning the size of solutions of diophantine prob-
lems are called diophantine inequalities.
During the past few years, new insights have been gained in old
problems combined with new ones, and great coherence has been
achieved in understanding a number of diophantine inequalities.
Some of these results, notably the first section, can be formulated
in very simple terms, almost at the level of high school algebra.

Received by the editors July 24, 1989.
1980 Mathematics Subject Classification (1985 Revision). Primary 11D41,
11D75, 11G05, 11G30.
* Supported by NSF grant, but...: In 1981 the Yale administration turned down
the NSF grant to me as principal investigator because I would not sign effort re-
ports. (However the math dept. at Yale passed a resolution to return all effort
reports unsigned to the administration, and the Yale administration did nothing
about other people's grants.) I was without a grant for 4 years. Then I reapplied
for some items (such as travel expenses) in 1985, via someone else's grant, but I
have not reapplied for summer salary support since 1981, and have therefore been
without such support since. The fact that I am listed by the NSF as being "sup-
ported" by the NSF has given rise to misunderstandings concerning the nature of
the support I received this last decade, whence it is important to specify the nature
of such support. In addition, I find that the shortage of funds affecting the NSF
makes it impossible for them to fulfill properly their funding role by following past
policies on the allocation of funds. Over the last few years I have found that on
the whole, for each person getting a grant, there are several others equally qualified
who have been dropped, thus causing chaos in the granting process, and serious
misinterpretations as to its implications by university administrators. It is demor-
alizing for the younger generation of mathematicians when getting a grant becomes
a crap-shoot, particularly when university administrators often interpret not having
NSF support as making someone unsuitable for tenuring or promoting. As a result
of all these factors (plus renewed bureaucratic pressures), I have decided not to
apply for any further NSF support in any form whatsoever starting next year.

©1990 American Mathematical Society
0273-0979/90 $1.00+ $.25 per page
37

38  SERGE LANG

I shall give a survey starting with these formulations, and ending
with more sophisticated applications to elliptic curves. But I have
made an attempt to have this article readable by a fairly broad
audience by giving basic definitions, and limiting myself to the
rational numbers whenever possible.

1. The abc conjecture. This conjecture evolved from the insights
of Mason [Ma], Frey [Fr], Szpiro, and others. Mason started one
recent trend of thoughts by discovering an entirely new relation
among polynomials, in a very original work, as follows. Let f(t)
be a polynomial with coefficients in an algebraically closed field of
characteristic 0. We define

n0(f) = number of distinct zeros of ƒ .

Thus nQ(f) counts the zeros of ƒ by giving each of them multi-
plicity one.

Mason's theorem. Let a(t), b(t), c(t) be relatively prime polyno-
mials such that a + b = c. Then

maxdeg{<z, b, c} ^ nQ(abc) - 1.

In the statement of Mason's theorem, observe that it does not
matter whether we assume a, b, c relatively prime in pairs, or
without common prime factor for a, b, c. These two possible
assumptions are equivalent by the equation a + b = c. Also the
statement is symmetric in a, b, c and we could have rewritten
the equation in the form a + b + c = 0.
Mason's theorem is a theorem, not a conjecture, and can be
proved as follows. Dividing by c, and letting ƒ = a/c, g = b/c,
we have  ƒ+<?= !
where ƒ, g are rational functions. Differentiating we get
which we rewrite as

so that  b = g^ f If
a f g'I g '
If J? is a rational function, R{t) = \[{t - p^f' with qteZ, then

R>/R = Y_?L-

OLD AND NEW CONJECTURED DIOPHANTINE INEQUALITIES 39

and the multiplicities disappear. Suppose

a(t) = n('-"/) m ' > b{t) = Uit-PjP , c(t) = U(t-yJk.

Then  b_ = //ƒ = El^-Eiz ^

8/8 2^ ?-£ ~ 2^ t-yk

A common denominator for f j ƒ and g'/S" *
s gi ye n by the prod-
uct
 tfo = II('- a i>II('-^)II('-7*) '
whose degree is n0(abc). Observe that N0//f and N0g'/g are
both polynomials of degrees at most n0(abc) - 1. From the rela-
tion
 Û #0*7 *
and the fact that a, b are assumed relatively prime we deduce the
inequality in Mason's theorem.
As an application let us prove Fermat's theorem for polyno-
mials. Thus let x(t), y(t), z(t) be relatively prime polynomials
such that one of them has degree ^ 1, and such that

x(t)
n+y(t)
n = z(t)\

We want to prove that n ^ 2 . By Mason's theorem, we get

degjt(0" ^ degx(f) + deg}/(0 + degz(r) - 1

and similarly replacing x by y and z on the left-hand side.
Adding, we find

n(degx + degy + degz) < 3(degx-fdegy H-degz) - 3.

This yields a contradiction if n ^ 3 .
Influenced by Mason's theorem, and considerations of Szpiro
and Frey which we shall describe below, Masser and Oesterle for-
mulated the abc conjecture for integers as follows. Let A: be a
non-zero integer. Define the radical of k to be

P\k
i.e. the product of the distinct primes dividing k. There is a
classical analogy between polynomials and integers. Under that
analogy, nQ of a polynomial corresponds to log NQ of an integer.
Thus for polynomials we had an inequality formulated additively,

40  SERGE LANG

whereas for integers we formulate the corresponding inequality
multiplicatively. Note that if x, y are nonzero integers, then

N0(xy)<N0(x)N0(y),

and if x, y are relatively prime, then

N0(xy) = N0(x)N0(y).

The abc conjecture. Given e > 0 there exists a
number C(e) having the following property. For
any nonzero relatively prime integers a, b, c such
that a + b = c we have

max(|a|, \b\, \c\) ^ C{e)N0{abc)
l+
e.

Unlike the polynomial case, it is necessary to have the e in
the formulation of the conjecture, and the constant C(e) on the
right-hand side. To simplify notation in dealing with the possible
presence of such constants, if A, B are positive functions, we
write

to mean that there exists a constant C > 0 such that A ^ CB.
Thus A < B means that A = 0(B) in the big oh notation. We
write

to mean A = O(B) and B = 0(A). In case the functions A, B
depend on a parameter e, the constant C also depends on e.
The conjecture implies that many prime factors of abc occur
to the first power, and that if some primes occur to high powers,
then they have to be compensated by "large" primes, or many
primes, occurring to the first power. Readers interested in seeing
immediately the application to the Fermât problem and similar
problems should skip the following remarks, having to do with the
equation 2
n ± 1 = k. For n large, the abc conjecture would
state that k is divisible by large primes to the first power or many
primes to the first power. This phenomenon can be seen on the
tables of [BLSTW]. The simplest examples showing the need for
the constant C(e) in the abc conjecture were communicated to
me by Wojtek Jastrzebowski and Dan Spielman as follows. We
want to show that there is no constant C > 0 such that

max(|a|, |&|, \c\) <: CNQ(abc).

OLD AND NEW CONJECTURED DIOPHANTINE INEQUALITIES 41

Writing 3 = 1 + 2, we find by induction that

2"|(3 2W-1).

We consider the relations an + bn= cn given by

2"
3 - 1 = c .
n
Then

so there is no constant C such that cn ^ 3CN0(cn). Other ex-
amples can be constructed similarly since the role of 3 and 2 can
be played by other integers: instead of 2 we use a prime p, and
instead of 3 we use an integer = 1 mod p .
In line with these examples, we now show that the abc conjec-
ture implies a classical conjecture:

There are infinitely many primes p such that

2
p~
l ï 1 mod/? 2.

We follow Silverman [Si]. First a remark. Let S be the set of
primes such that  2
P~ ^ 1 mod p .
We claim that if n is a positive integer, and p is a prime such
that 2
n = 1 mod p but 2
n ^ 1 mod p
2, then p is in S. Indeed,
let d be the period of 2 in the multiplicative group (Z/pZ)* of
units in Z/pZ, which has order p - 1. Then d divides p - 1 and
also divides n. Furthermore 2
n = 1 mod p but 2
n ^ 1 mod p
2

implies 2 ^ 1 mod p
2 . Hence 2
p~
l ^ 1 mod p
2, as one sees by
writing p - 1 = dm, with m prime to /?, and 2 —\-\-pk with
/: prime to /?. Then

2
P~ = 1 +pmk ^ 1 modp ,

so /? is in 5 as claimed.
Now suppose that 5 is finite. Write
2" " ! = W
where ww is the product of primes in S, and all primes dividing
vn are not in S. Then un is bounded. If p\vn then by the claim,
p
2 divides 2
n - 1, so p
2 divides vn. By the abc conjecture
applied to the equation
 (2"-l ) + l =2
n

42  SERGE LANG

we conclude that
 _ / 1/2, l+e ^ (l+£)/2
Un
Vn « («W ) < *>i
whence vw is bounded, a contradiction.
Actually, in line with Lang-Trotter conjectures, the probability
that 2
p~
l = 1 + pk(modp
2) with a fixed residue class k modp
should be 0(1//?), so the number of primes p ^ x such that
2
p~
l = 1 mod p 2 should be
 O(loglogx).

Thus most primes should have the property that 2
P~ ^ 1 mod p .
We now pass to the application of the abc conjecture to var-
ious diophantine equations. In the case of polynomials, we got
an explicit bound for the degree of Fermat's equation satisfied by
polynomials which are not all constant. Since there is an unknown
constant C(e) floating around in the abc conjecture, we shall get
only an unknown bound for the classical case of Fermat's equation
over the integers. Thus we define the asymptotic Fermât problem
to state that there exists an integer nx such that for all n^nx the
equation  n , n n
x + y = z
has only a trivial solution in integers, that is with one of x, y, z
equal to 0. Of course, for the asymptotic Fermât problem as well
as the ordinary one, we may and do assume that x, y, z are rel-
atively prime.

The abc conjecture implies the asymptotic Fermât problem.

Indeed, suppose x
n + y
n = z
n with x, y, z relatively prime.
By the abc conjecture, we have

\x I < \xyz\

\y I < \xyA

Taking the product yields

z | < \xyz\ .

\xyz\
n < \xyz\
 +e,

whence for \xyz\ > 1 we get n bounded. The extent to which the
abc conjecture is proved with an explicit constant C(e) (or say

OLD AND NEW CONJECTURED DIOPHANTINE INEQUALITIES 43

C(l) to fix ideas) yields the corresponding explicit determination
of the bound for n in the application.
We shall now see how the abc conjecture implies other conjec-
tures by Hall, Szpiro, and Lang- Waldschmidt,

Hall's original conjecture is that if u,v are rela-
tively
then
tively prime nonzero integers such that u - v ^ 0

, 3 2, ^ , ,1/2—e
\U - V I > \U\
Note that Hall's conjecture describes how small \u
3 - v
2\ can be,
and the answer is not too small, as described by the right-hand
side. Furthermore, if \u
3 - v
2\ is small, then \u
3\ X v
2 so
M X \u\
3^
2. The Hall conjecture can also be interpreted as
giving a bound for integral relatively prime solutions of

2 3
v = u + b with integral b.
Then we find  |w|<|è| 2+e .

More generally, as in Lang-Waldschmidt [La3], p. 212, let us fix
nonzero integers A, B and let u, v, k, m, n be variable, with
u, v relatively prime and mn > m + n . Put

Au
m + Bv
n = k.

By the abc conjecture, we get
 ,1+e
\u\
m < \uvN0(k)\
l

\v\
n < \uvNQ(k)\
1+e

If, say, \Au
m\ <: \Bv
n\ then \u\ < \v\
n/m . We substitute this
estimate for u to get an inequality entirely in terms of v , namely

We first bring all powers of v to the left-hand side. We have
n mn - (m + n)
n- 1 - m m

actually the original conjecture does not make the assumption that u, v are
3 2
relatively prime, only that u -v ^ 0 . The original conjecture also follows from
the abc conjecture by extracting a common factor, and using the same method as
that indicated below. We make the relatively prime assumption to avoid secondary
technical complications, and we leave the proof in general to the reader.

44  SERGE LANG

We let the reader take care of the extra e, so we obtain

(1) \v\<£N0(k)
m(l+e)/{mn-
{m+n)) and then also

\u\ « Aro(fc)»(i+«)/(«».-(«+»))

because the situation is symmetric in u and v . Again by the abc
conjecture, we have
 \k\<£\uvN0(k)\
l+e,

so using the estimate for \uv\ coming from the product of the
inequalities in ( 1 ) we find

(2) |*| « Aro(yt)"»'(
1^)/('"»-(m+M))_

The Hall conjecture concerning u -v = k is a special case of
(1), after we replace NQ(k) with \k\, because #0(fc) ^ |/c|.
Again take m = 3 , « = 2 and take ^4 = 4, B = -27 . In this
case, we write D instead of k, and we find for

D = 4u
3 - 21v
2

that

(3) \u\ < N0(D)
2+e and \v\ <& N0(D)
Ue.

These inequalities are supposed to hold at first for u, v relatively
prime. Suppose we allow u, v to have some bounded common
factor, say d. Write
u - ud and v = t/d

with i/ , v relatively prime. Then

D = 4d
3u
3-21d
2v'
2.

Now we can apply inequalities (1) with A = 4d and B = -21 d ,
and we find the same inequalities (3), with the constant implicit in
the sign < depending also on d, or on some fixed bound for such
a common factor. Under these circumstances, we call inequalities
(3) the generalized Szpiro conjecture.
The original Szpiro conjecture was stated for what is called a
"minimal discriminant" D. We shall discuss the notion of a min-
imal discriminant in §4, when we go further into the theory of
elliptic curves. Szpiro's inequality was stated in the form

\D\<£N(D)
6+\

OLD AND NEW CONJECTURED DIOPHANTINE INEQUALITIES 45

where N(D) is a more subtle invariant which is commonly used
in the literature, namely the conductor. But for our purposes, it
is sufficient and much easier to use the radical NQ(D), since the
conductor is harder to define, and its subtleties are irrelevant for
what we are doing.
Note that the generalized Szpiro conjecture actually bounds \u\,
\v\ and not just \D\ itself in terms of the right power of NQ(D).
The point of D is that it occurs as the discriminant of an elliptic
curve. The recent trend of thoughts in the direction we are dis-
cussing was started by Frey [Fr], who associated with each solution
of a + b = c the elliptic curve

2
y =x(x-a)(x + b)9
which we call the Frey curve. The discriminant of the right-hand
side is the product of the differences of the roots squared, and so

D = {abc)
1.

We make a translation
 K b - a
Ç = x + —

to get rid of the x2-term, so that our equation can be rewritten

y =t -y2ç-y3>

where y2, y3 are homogeneous in a, b of appropriate weight. The
discriminant does not change because the roots of the polynomial
in Ç are translations of the roots of the polynomial in x . Then

D = 4yl-21y].

The translation with (b - a)/3 introduces a small denominator.
One may avoid this denominator by using the curve

y = x(x - 3a)(x + 3b),

so that y2, y3 then come out to be integers, and one can apply the
generalized Szpiro conjecture to the discriminant, which then has
an extra factor
 D = 3\abcf = Ay\-21y\.

The Szpiro conjecture implies asymptotic Fermât.

Indeed, suppose that

a = u , b = v , and c = w

46  SERGE LANG

with relatively prime u, v, w . Then

4y2 - 27y3 = 3 (uvw)
 n,

and we get a bound on n from the Szpiro conjecture

|D|«JV0(Z>)6+\

Of course any exponent would do, e.g. \D\ < N0(D)
m for asymp-
totic Fermât.
We have already seen that the abc conjecture implies general-
ized Szpiro.

Conversely, generalized Szpiro implies abc.

Indeed, the correspondence

(a,b)+->(y2,yj

is invertible, and has the "right" weight. A simple algebraic ma-
nipulation left to the reader shows that the generalized Szpiro esti-
mates on y2, y3 imply the desired estimates on \a\, \b\. (I found
this manipulation a good assignment for my undergraduate algebra
class.)
From the equivalence between abc and generalized Szpiro, one
can use the examples given at the beginning to show that the ep-
silon is needed in the Szpiro conjecture.
Hall made his conjecture in 1971, actually without the epsilon
so it had to be adjusted later. The final setting of the proofs in the
simple abc context which we gave above had to await Mason and
the abc conjecture a decade later.
Let us return to the polynomial case and Mason's theorem. The
proofs that the abc conjecture implies the other conjectures apply
as well in this case, so the analog use of Hall, Szpiro and Lang-
Waldschmidt are also proved in the polynomial case. Actually, it
had already been conjectured in [BCHS] that if ƒ , g are non-zero
polynomials such that f - g
2 ^ 0 then

deg(/(0 3 -^(0 2 )^^deg/( 0 + l .

This (and its analogue for higher degrees) was proved by Daven-
port [Dav] in 1965, but we now see it as a consequence of Ma-
son's theorem. Both in the case of Hall's conjecture for integers
and Davenport's theorem, the point is to determine what lower
bound can occur in a difference between a cube and a square, in
the simplest case. The result for polynomials is particularly clear

OLD AND NEW CONJECTURED DIOPHANTINE INEQUALITIES 47

since, unlike the case of integers, there is no extraneous undeter-
mined constant C(e) floating around, and there is even +1 on
the right-hand side.
The polynomial case as in Davenport and the Hall conjecture
for integers are of course not independent. Examples in the poly-
nomial case parametrize cases with integers when we substitute
integers for the variable. Examples are given in [BCHS], one of
them due to Birch being:

f(t) = t
6
 + 4t
4+l0t
2
 + 6 and g(t) = t
9+ 6t
7+ 2U
5+ 35t
3+ & t,

whence  degree(/(03 - g{tf) = \ deg ƒ + 1.
This example shows that Davenport's inequality is best possible,
because the degree attains the lowest possible value permissible
under his theorem. Substituting large integral values of t = 2
mod 4 gives examples of similarly low values for x 3 - y
2. A
fairly general construction is given by Danilov [Dan]. See also
the discussion of similar questions relevant to the size of integral
points on elliptic curves in [La2], for instance Conjecture 5.
For those who know the theory of function fields in one variable,
it is clear that the <z&c-property can also be formulated in that
case, and can also be proved in that case. In fact, historically it
was done that way as in [Ma3]. However, we are interested in
algebraic number fields, so we shall now go to the next level of
exposition and discuss heights of points in number fields.
So far we have proved the implications and equivalences relating
three corners of the following diagram.

Fermât «** - Generalized Szpiro

Vojta *»» abc

Our purpose is to fill in the Vojta corner, and show how the con-
jectures follow from the Vojta conjecture. One of the crucial points

48  SERGE LANG

here is that we cannot stay within the realm of rational numbers,
we must look at algebraic numbers. It will be seen how diophantine
properties of a family of curves over the rational numbers depends
on the diophantine properties of a single curve but uniformly for
solutions in finite extensions of the rationals of bounded degree.
We want to estimate how big solutions of diophantine equations
can be. What does "big" mean? Let x = c/d be a rational number
expressed in lowest form with relatively prime integers c, d. We
define the height of x to be

h(x) = logmax(|c|, \d\).

Similarly, if P = (x0, ... , xM) is a point in projective space with
integer coordinates x- which are relatively prime, then we define
the height  h(P) = logmax|x.|.

The abc conjecture thus bounds the height of the point (a, b, c),
with relatively prime integers a, b, c which can be seen as repre-
senting a point in projective 2-space.
The next two sections which carry out the above program are
independent of the final three sections which give applications of
the abc conjecture to elliptic curves, via the Szpiro conjecture.
The reader may therefore read these in any order.

Remark for those who know or want to find out about modular curves. I don't
want to discuss modular curves here, I want to confine the discussion to diophan-
tine inequalities. But for those interested, it may be useful to make the following
comments, for which we assume that the reader will either know the required def-
initions or look them up elsewhere.
Frey started the recent train of thoughts concerning Fermât and elliptic curves
by pointing out that the elliptic curve associated with a solution of Fermât would
have remarkable properties which should contradict the Taniyama-Shimura con-
jecture that all elliptic curves over the rational are "modular" [Fr]. Frey's idea was
to show that the elliptic curve then could not exist, whence Fermât follows. There
were serious difficulties in realizing this idea. Serre [Se] pointed out that one needed
apparently more than the Taniyama-Shimura conjecture, for instance another con-
jecture which he had made, concerning the modularity of Galois representations
over the rationals. Then Ribet [Ri] proved enough of the Serre conjecture in the
modular case to show that the Taniyama-Shimura conjecture suffices for the Fer-
mât application. We do not go into this modular aspect here. On the contrary, in
the present discussion, we are pointing in a different direction, namely the direc-
tion of diophantine analysis and diophantine inequalities. The Szpiro conjecture
can be viewed as lying just in the middle, and is susceptible of being handled or
proved in either direction. Thus the abc conjecture has a modular interpretation
via the generalized Szpiro conjecture to which it is equivalent. I must also point
out that the modular route to Fermât via Ribet-Serre-Taniyama-Shimura would
prove Fermât unconditionally. The route via the diophantine inequalities depends

OLD AND NEW CONJECTURED DIOPHANTINE INEQUALITIES 49

2. The height for algebraic points. In this section we discuss alge-
braic numbers, and we describe how to define the height for points
with algebraic coordinates, which will be used in §3. After that we
return to the rational numbers, but we shall use p-adic numbers
also.
Let F be a number field, i.e. a finite extension of the rational
numbers Q. Then F has a family of absolute values, p-adic and
archimedean (at infinity, as one says). We shall now describe these
absolute values.
For each prime p there is the p-adic absolute value on Q, de-
fined on a rational number a = p
rc/d with (c, d) = 1, p \ cd,
by
 \a\p = l/P-
This /7-adic absolute value has a finite number of extensions to
F, which are called p-adic also. Let v be one of these, extending
^ on Q . Let Fv be the completion of F at v . Then Fv is a
finite extension of the field of p-adic numbers Qp . The absolute
value on Q^ extends uniquely to Fv . Each v is induced by an
imbedding of F into the algebraic closure of Qp :

and v is induced by the absolute value on Q* . Conversely, given
such an imbedding a : F —• Q^ we let va be the induced absolute
value.
The rational numbers also have the ordinary absolute value, ex-
tending to the real numbers, and denoted by v^ . An extension
of v^ to F is said to be at infinity, and there is a finite number
of such extension. Let v extend r; to F. Then v is induced
oo
by an imbedding

of F into the complex numbers. Thus the situations at infinity and
at the ordinary primes are entirely similar. In each case, imbed-
dings of F into Q^ which differ by an isomorphism of Fv over
Qv give rise to the same absolute value on F, and conversely. In
the case of absolute values at infinity, a pair of complex conju-
gate imbeddings of F into C corresponds to an extension of the
ordinary absolute value from Q to F .

on the constants in the estimates for these inequalities, and will be as effective as
these constants can be made to be effective.

50  SERGE LANG

Now consider a point P = (x0, ... , xn) in projective space P
w ,
with coordinates in F so x- e F and not all Xj = 0. We define
the height of P by the formula

h(
p) = j]p7QjS^ , :QJlogmax|xy|v

where [F : Q] denotes the degree of the extension, and where
the sum is taken over all the above described absolute values v
on F. The Artin-Whaples product formula (sum formula in our
case) asserts that for a e F, a ^ 0 we have
5X:Q„]logH, = 0,

V
and so the height indeed depends only on the point in projec-
tive space. An elementary property of the absolute values implies
that the height is independent of the field F in which the coordi-
nates xQ, ... , xn lie: this is the reason for the normalizing factor
l/[F : Q] in front of the formula defining the height.
Note that if F = Q and x0, ... , xn are relatively prime inte-
gers, then  h(P) = logmax|.x-|,

where the absolute value here is the ordinary one on the rational
numbers.
We shall need another notion of algebraic number theory. The
field F has a subring R, the ring of algebraic integers which are
those elements of F satisfying an equation

Tn+an_Jn-1 + --- + a0 = 0

whose coefficients aQ, ... , an_x lie in the ordinary integers Z .
This ring R has a basis {wl, ... , wN} over Z , where N = [F : Q].

If aj (7 = 1,... , N) ranges over all imbeddings of F into C,
then the logarithmic discriminant d(F) is defined by

d(F)=^±Q] log| detail 2

= log | discriminant of F over Q|.

It is easy to prove that if F{, F2 are number fields, then

d{FxF2)^d{Fx) + d{F2).

Also if Fx C F2 then d(Fx) <: d(F2).

OLD AND NEW CONJECTURED DIOPHANTINE INEQUALITIES 51

Given a point P in projective space, we let

d(P) = d(F(P)).

Furthermore, the discriminant of the field F(P) is insensitive to
the higher power of primes dividing the coordinates of the point.

EXAMPLE. Suppose x = ax^n where a is a positive integer. Let

v. vr

be the factorization with v. > 1 and with distinct primes px,
... , pr. Then  logA
7
0(a) = ^log/7 / .

Furthermore  Q(a )cQ(p 1 / ,...,/> / ) .

If a is a root of an = p , then the discriminant is the norm of
na
n~~
l, so the discriminant is bounded by n
np
n~
l. Hence

n - 1
d(Q(oc)) <; log H + log/?.

We apply this estimate to each prime dividing a to get

d(Q(x))^rlogn + ^logN0(a).

REMARK. For N0(a) -» oo we have

r = o(logN0(a)).

Indeed, if r is bounded this is trivial. If r is unbounded, then
/?! "Pr > r\, so our assertion follows from Sterling's formula that
r\ > re~r.
So far we have dealt with notions of algebraic number theory.
We now pass to the height in the context of algebraic geometry, in
the case of curves. We must assume that the reader is acquainted
with the basic notion of an algebraic curve, imbeddable in projec-
tive space. Such a curve X will always be assumed irreducible.
It is defined by a system of homogeneous polynomial equations
when it is so imbedded, and is said to be defined over F if the co-
efficients of these equations lie in F . A divisor on X is a formal
linear combination of points, with integer coefficients. The degree
of a divisor is defined to be the sum of these coefficients. The
curve X is covered by affine pieces, and a typical affine piece may
be defined by one equation f(x, y) = 0, for instance. A point will
usually be taken with coordinates x, y which lie in some number

52  SERGE LANG

field, i.e. we deal mostly with algebraic points. The set of points
with coordinates in a field E is denote by X(E). Then X(C) is
the set of complex points, and if the curve is nonsingular, then
X(C) is a compact Riemann surface. The genus g of X may be
defined as the genus of this surface, but there are also algebraic
definitions. For instance, if X is defined by one homogeneous
irreducible equation  ^oJ,J 2 ) = 0

in the projective plane, if X is nonsingular, and H has degree d,
then the genus of X is (d - \)(d - 2)/2.
The genus is also equal to the dimension of the space of regular
differential forms. Say over the complex numbers, let ydx be
a meromorphic differential form on X where y, x are rational
functions on X. Let P be a complex point. Let t be a local
uniformizing parameter at P. We write

ydx=y{t)-jjdt,

where y, x are expressible as power series in t. Then we define

dx
ordpydx = order of the power series y(t)-jj .

We can associate a divisor to the differential form ydx by letting

(ydx) - y ^ ordp(ydx)(P).

p
Then the degree of this form satisfies

deg{ydx) = ] P ordp(ydx) = 2g - 2.

p
If ƒ is a rational function on X, then one can also associate a
divisor ( ƒ ) to ƒ , namely at the point P we define ordp ƒ = order
of the power series ƒ (t), in terms of the local parameter t. Then
deg( ƒ) = 0 (which corresponds to the product formula). A divisor
is said to be rationally equivalent to 0 if it is the divisor of a rational
function. Equivalence among divisors will always refer to rational
equivalence in what follows. In light of the relation deg(ƒ) = 0
we see that the degree function is defined on equivalence classes.
The class of divisors of rational differential forms is called the
canonical class.
Let X be a projective nonsingular curve defined over a number
field. To each divisor D on X one can associate a function, the

OLD AND NEW CONJECTURED DIOPHANTINE INEQUALITIES 53

height,  hD:X(Q*)-+R
from the set of algebraic points into the reals, satisfying the follow-
ing properties, and uniquely determined by them modulo bounded
functions:
1. D »-• hD is well defined mod 0(1) on the ra-
tional equivalence class of D and is a homomor-
phism, i.e. is additive in D.
2. If D is a hyperplane section in a projective
imbedding, then hD(P) is the height of a point P
in that projective imbedding.
The uniqueness follows because given a divisor D there exists two
projective imbeddings of X with hyperplane sections H{ and H2
respectively such that D is equivalent to Hx - H2 (this is a basic
lemma of algebraic geometry).

3. The Vojta conjecture. The conjectures expressed by Vojta [Vo]
are basic to the subject. I give here only one of the conjectures
having to do with curves.

Vojta conjecture Let X be a projective nonsingular
curve defined over a number field. Let K be the
canonical class of X. Then given e > 0,

hK(P)£(l+e)d(P) + Oe(l) forPeX(Q
a).

In the first place, observe that for a curve of genus ^ 2, the
Vojta conjecture immediately implies that the set of rational points
X(F) is finite (Mordell conjecture—Faltings theorem). Indeed, in
that case d(P) is constant, so the height of such points is bounded,
and it is easy to show that there is only a finite number of points
of bounded degree and bounded height.
We shall now see how the Vojta conjecture implies asymptotic
Fermât and also implies the abc conjecture. Note that we shall
use the Vojta conjecture only for points P of bounded degree over
F as in [Vo], Appendix ABC p. 84.
Suppose we want to prove Vojta implies asymptotic Fermât. Let

Xn:x +y =z

be the Fermât curve and consider X4 which has genus 3. For
a hypersurface of degree d in P m the canonical class is that of
(d - (m + 1)))//, where H is a hyperplane. So for Xn in P2 the

54  SERGE LANG

canonical class is that of (n - 3)H, and for X4 the canonical class
is  K = H.

Let u
n + v
n = w
n in relatively prime integers. Associate the
point  n / \ / H/4 n/4 n/4s „
P = (x, y , z) — (u :v : w ) onI 4 .

From the definition of the height, it is immediate that
Yl

h(P) = — logmax(|w|, \v\, |^|) .

By Vojta's conjecture we get

-logmax|w|, |v|, |it;| < logA^0(wfi(;) + 0(1),

which gives a bound for n .
Similarly to prove the abc conjecture from Vojta, suppose
a + b — c. Fix n . Associate the point
P = (a ' :b ' :c ' ) onI n .
Since Kn- {n- 3)H we get by Vojta's conjecture

M^ ) = ^logmax(M , \b\, \c\) < (l+e{)loèN0(abc) + On(l).

This IS the log of the abc inequality. We let n —• oo with
e = e{ + 4/n or whatever.

We shall conclude with sections on elliptic curves, showing how
the abc conjecture implies diophantine properties of such curves
over number fields.

4. Elliptic curves and minimal equations. An elliptic curve for our
purposes will be a curve which can be represented by an equation
in Weierstrass form
 y
2 = x
3 - y2x - y3,

with coefficients y2, y3 in some field F . Let A denote the curve.
The set of points with coordinates x, y e F together with the
point at infinity is denoted by A(F), and is a group. As before,
we shall take F to be mostly a subfield of the complex numbers,
in which case A(F) is a subgroup of A(C). Over C, the curve is
parametrized by the Weierstrass functions

z^(p(z), \p\z)),

OLD AND NEW CONJECTURED DIOPHANTINE INEQUALITIES 55

giving an analytic isomorphism C/A—• A(C) where A is a lattice.
The lattice points go to the point at infinity under this parametri-
zation. The addition formula for the p-function defines the group
law on A(C), and this addition formula is given by rational func-
tions on the coordinates (x,y), with coefficients in Q , which is
why A(F) is a subgroup.
As before we have the discriminants

4y2
3 - 27y
2
3 = D and A = 16D.

For any number c/ 0 we can change the elliptic curve by an
isomorphism, which under the Weierstrass parametrization maps
z H-» cz. Then the representation of this isomorphism on the
equation has the effect:

1- 2 / - 3
xy-+x = c x, y^y =c y ,

y2^y2 = c"\, y3 ^ y3 = c~6y3,

so that the isomorphic curve satisfies the equation
y =x -y2x -y3.

Suppose the elliptic curve is defined over Q, that is y2, y3 G Q.
By an appropriate such isomorphism, we can make y2, y3 e Z.
Suppose p is a prime such that p
4 divides y2 and p
6 divides y3.
Then we can change the elliptic curve by an isomorphism, letting
y2 »-• p~
4y2 and y3 »-• P~
6y3- After having done so repeatedly
until no further possible, we obtain what is a minimal model for
the curve over Z , and then A is called a minimal discriminant.

REMARK. The minimal discriminant is defined up to a factor of
± 1, and is an invariant of an isomorphism class of elliptic curves
over Q . We have slightly over simplified the situation in two ways.
First by tying ourselves down to the Weierstrass model, we don't
quite get the "right" notion for this minimal discriminant, because
of the primes 2 and 3. One has to give a more general equation,
first studied by Deuring, and carried out systematically in more
recent times by Neron and Tate. Also to be absolutely correct, to
take care of the primes 2 and 3, we really should consider a more
general form of the Weierstrass model, namely:

2 3 2
y +a{xy + a3y = x +a2x +a4x + a6.
One can obtain a minimal model, i.e. one with minimal discrimi-
nant, just as in the standard case of the Weierstrass equation. The

56  SERGE LANG

following statements refer to such a model, but the reader may
think of p ^ 2, 3 and of the usual Weierstrass equation without
harm.
The discussion of isomorphisms above contained the essential
aspects of the minimal discriminant. Furthermore, by dealing over
the rationals, we avoid all the problems which come from non-
unique factorization in number fields, and the existence of a non-
trivial group of units in the ring of integers of the number field.
A reader acquainted with elementary algebraic number theory will
then see that in case of a nontrivial ideal class group, there is no
unique minimal model of the curve with minimal discriminant,
but there is a finite number of models, with relatively minimal
discriminants. These are secondary considerations for what we
are doing here, where we want to see clearly the effect of the abc
conjecture on the diophantine aspects of the curve. These essential
aspects are all present for curves over the rationals.
We shall want to apply the Szpiro conjecture, but we must take
into account that y2, y3 may not be relatively prime. We still want
to see that for a minimal model, we have |A| < N0(A)
S for some
s independent of A. Indeed, by the minimality assumption, if
p
m is a common factor of y2, y3 then m ^ 5. Therefore, if
d = (y2 > ^3) is the greatest common divisor, then

d^N0(d)
5.

By factoring out a common factor, canceling, and small algebraic
manipulations, it is easy to see that for a minimal equation, by the
abc conjecture we have

|A| « N0(A?
+Ed
4

and therefore  |A| « N0(A)
S

for some low integer s which we may call the Szpiro exponent.
Without loss of generality, we may then assume that

|A| ^ N0(A)
S

except for a finite number of A, and so except for a finite number
of elliptic curves. We shall omit these exceptional curves, and
assume in the sequel that |A| < N0{k)
s.

5. The Szpiro conjecture and torsion points. Let F be a num-
ber field, that is a finite extension of the rational numbers. The

OLD AND NEW CONJECTURED DIOPHANTINE INEQUALITIES 57

Mordell-Weil theorem asserts that the group of rational points
A(F) is finitely generated. (Mordell originally proved the theorem
over the rationals.) It is a major problem to describe the order
of the torsion group and the rank of A(F). We are here con-
cerned with the torsion group, which is finite by the Mordell-Weil
theorem. A standard conjecture states:

Given the number field F, there exists a positive
number C such that for every elliptic curve A de-
fined over F, the order of the torsion group A(F)tor
is bounded by C.
Over the rational numbers, this was proved in a very strong form
by Mazur [Maz], who showed that the order of the torsion group is
bounded by 16. For this purpose, Mazur developed a whole theory
on modular curves. Here we are concerned with a statement which
is weaker in the sense that no specific bound like 16, is given,
but stronger in that we want the statement for any number field.
Results for number fields have been obtained by Kubert [Ku]. In
this section, we show that the abc conjecture for number fields
implies the uniform boundedness of torsion as stated above by an
argument due to Frey which he wrote me in 1986.
For simplicity, we shall work over the rational numbers. A
reader acquainted with the basic properties of elliptic curves and
number fields will immediately see that the arguments generalize.
As usual we define the isomorphism invariant

7 = 3 4 y2/A.

REMARK. The primes which divide the denominator of j play
a special role. These primes must also divide A, but the converse
need not hold. We shall have to use a relatively deep fact:

If there exists a rational point in A(Q) of prime
order n > 5, then y2 and y3 are relatively prime
except for small powers of 2 and 3, and also pos-
sibly n itself
This fact is hard to prove, and we make some comments for those
somewhat acquainted with elliptic curves, or those who may wish
to pursue this matter further. Let p be a prime ^ 5. One may
reduce the minimal equation of an elliptic curve mod p . Then
the reduced equation defines a possibly reducible curve, called the
fiber. The group law on the original elliptic curve reduces to a
group law on the set of nonsingular points on the fiber, giving

58  SERGE LANG

rise to the theory of the Néron model. Cf. [Ne], the last section
on elliptic curves, and the last table, as well as Artin's exposition
(somewhat sketchy) of Néron models [Ar], especially Proposition
1.15. Now suppose that j is /7-integral. If p is not a common
factor of y2 and y3 then we say that the elliptic curve is semistable
at p . If p is a common factor, then the curve reduces mod p to
y
2 = x
3. Let us look at the curve over the p-adic field Qp . By
the theory of Néron models, it can be shown that the nonsingular
part of the fiber is an algebraic group, which contains the additive
group as a subgroup of index at most 4, and that the kernel of
reduction is a p-adic Lie group, which does not contain points
of finite order. From this structure, we conclude that the curve
is semistable at p when there exists a rational point of prime
order n > 5, except possibly when p = n, because all points
on the additive group in characteristic p have order p. For a
generalization and examples, see Lenstra-Oort [L-O], especially §3
for examples of large p-torsion /?-adically.
Admitting the above fact, we see that except possibly for 2, 3,
and n, the primes dividing the denominator of j are precisely
the primes dividing A.
To prove a theorem about torsion points over the rationals, we
must have a model for them which will contain enough algebraic
information, even though it may involve some analysis. The clas-
sical parametrization C/A -» -4(C) by the Weierstrass functions is
not good enough for this purpose. However, we may take the lat-
tice to have a Z-basis {T, 1} where r is in the upper half plane:
Im(r) > 0. Then we put
 q=q = e
Inix

We can then also represent A(C) as a quotient of the multiplicative
group as follows. We have the Fourier series expansion, power
series in q, in all standard texts, including [Lai] and [La3]:

(2m) y2 = —

( 27n )
 y 3 = ^ 3
 0 0
 M3 »
n
n q
n-\ 00
 M5^w
n q .1 + 504£fA_

OLD AND NEW CONJECTURED DIOPHANTINE INEQUALITIES 59

oo
(2rc/ri2A=^n(1-^)24

j = 1 + 744+ 196884tf+ •••

and for a variable t eC* :

t m. oo n

mez I1 - 9 0
We get an analytic isomorphism

C7ff Z ^(C ) by f ~ (*(*), y(0).

The power series expansions for X(t) and Y(t) have essentially
integral coefficients, and as Tate remarked in the late fifties, they
can be used to parametrize an elliptic curve in the p-adic domain,
where they converge provided that

\q\ < 1 or equivalently p divides the denominator of j .

This elliptic curve, called the Tate curve, is isomorphic to the given
curve over a quadratic extension. For simplicity, we shall argue as
if this isomorphism is over Qp itself.
As with the complex numbers, the absolute value on Q extends
uniquely to the algebraic closure Q^ and to the completion of the
algebraic closure, which we denote by Cp, and which plays the
role of C.
In the p-adic field, using the notation u — v to mean that u/v
is a /7-adic unit, we see that

j and A ~ q.
Q
Except for the primes 2 and 3, y2 and y3 are then p-adic units.
Tate normalizes the equation and the power series further to get
rid of denominators involving 2 and 3 completely, but we don't go
into this here.
Thus t H-> (X(t), Y(t)) gives a homomorphism

C*p-+A(Cp) inducing Q
m
p^A(Qp)

from the multiplicative group of the field to the group of points of
A in the field. The kernel is the infinite cyclic group q . Similarly,

60  SERGE LANG

if F is a finite extension of Q in C we have a parametrization
F* /q
z —• A(F). We then obtain a model for the torsion points
of A in A(C ) . The points of order n are parametrized by the
group generated by  q , Cn mod q

where # ^ is any one of the nth roots of q, well defined modulo
an nth root of unity; and Çn is a primitive «th root of unity.
We shall first prove that there is only a finite number of primes
n such that an elliptic curve over Q has a rational point of order
n, by showing that the minimal discriminants of such curves are
divisible by only a finite number of primes.
Suppose that the elliptic curve A over the rationals has a point
P e A(Q) of order precisely n with n prime. For each prime
number p dividing the denominator of j , and thus dividing A,
1 In
this point is represented by q ' or Çn. If P corresponds to
q
{/n , since P e A(Qp) it follows that q
l/n eQp,so p
n\q = qA .
Suppose on the other hand that P corresponds to Çn for some
primitive nth root of unity. Let (P) be the cyclic group generated
by P, and let  B = A/(P)
be the quotient elliptic curve, which is then also defined over Q.
Then we have the minimal discriminants AA and AB , and the two
parameters qA and qB coming from the Tate parametrization p-
adically. In the present case, we claim that qB = q
n
A . Indeed, the
system here works just as in the case of a lattice. The map raising
to the nth power gives an isomorphism

C;/(q,QZc;
n/(q
n) = C*p/(q
n).

Thus the "period" group of C*p/(q, Çn) is generated by q
n , in
case P corresponds to Çn . (See the Remark below.) Therefore
qB = qA. It follows that in this case, p
n\qB . Hence in both cases,

p
n divides qAqB.

In terms of the minimal discriminants, this implies that

p
n divides AAAB.

But it is known that AA and AB are divisible by the same primes.
By the Szpiro conjecture applied to AA and AB separately, we get

|A^Afi| « N0(AjN0(AB)
s = N0(A)
2s.

OLD AND NEW CONJECTURED DIOPHANTINE INEQUALITIES 61

If px, .. . , pr are the primes dividing A and ^ n, 2 , 3 , then we
get
 (Pl'-Pr) <(Pi'-Pr) " ,

which gives a bound on « as effective as the constant in Szpiro's
conjecture, unless there are no primes p{, .. . , pr. But in that
case, A is divisible only by n (or 2 and 3). Then for n > 5 , the
curve has good reduction modulo 5, say, and reduction mod 5
induces an isomorphism on the points of order n, which is im-
possible for n sufficiently large since the cardinality of A(¥s) is
bounded.
It follows that the discriminants of minimal models are divisible
by only a finite number of primes. By what we saw at the end of
§4, this implies that there is only a finite number of values AA for
minimal models A . It remains to be shown that for fixed A the
equation
 A = 4y
3
2-21y
2
3

has only a finite number of solutions y2, y3 giving minimal mod-
els. This is a known theorem, but for our purposes we can deduce
it from the Szpiro conjecture. Indeed, the powers of primes occur-
ring as common factors of y2, y3 are bounded by the minimality
condition. Hence the g.c.d. of y2, y3 is bounded for all elliptic
curves with minimal equation over Q . By the generalized Szpiro
conjecture, it follows that \y2\ and |y3| are also bounded, thus
proving the desired implication.

REMARK. Concerning the assertion made that qB = q
n
A when
B = A/(P) and P corresponds to the nth roots of unity, the
reader should think first in terms of the complex case. Suppose
the lattice of the elliptic curve is [r, 1] (i.e. the group generated
by T , 1 over Z) , so A(C) « C/[r, 1]. Let P correspond to l/n .
Then
 A(C)/(P)nC/[T9 1//I]«C/[/IT , 1],

where the second isomorphism is induced by multiplication
n : C —• C . Exponentiating, we see in the complex case that the
" q " corresponding to A/(P) is e2ninx. Now the reader must ac-
cept that essentially the same theory of parametrization holds in
the p-adic domain, so the argument works the same way, as given
in the above proof.

62  SERGE LANG

The same method should prove a more general conjecture as
follows.
Let F be a number field. There exists a positive
number C having the following property. If A is
an elliptic curve over F, without complex multipli-
cation, and if there exists a cyclic subgroup of order
n, invariant under the Galois group over F, then
n<C.
The cyclic subgroup is generated by one point P of order n,
and the hypothesis means that the extension F(P) is Galois, with
group G such that for a G G we have

with some element x(
a) € (Z/nZ)*. Thus x gives a representa-
tion of G as a subgroup of (Z/wZ)*. If n is a prime number,
then in particular, the order of G is prime to n .
To follow the same pattern of proof, one needs to start with
semistability. Assume for the moment that the curve is semistable,
and let F = Q for simplicity as before. As before, we then get
that a prime dividing AA also divides the denominator of j .
In the first step of the proof, supposing that P corresponds
to q
l'
n under the Tate parametrization, we note that either the
polynomial X
n - q is irreducible over Qp or it has a root in Qp ,
by an elementary criterion of field theory. Therefore, if q is not
an nth power in Q then

Qp(<i
l/n) = Qp(P)

has degree n over Qp . Since the Galois group has order prime to
n, this cannot happen and therefore q is an nth power in Qp .
Thus we are in the same situation as before, and exactly the same
arguments using the Szpiro conjecture show that n is bounded.
However, under the weaker hypothesis of the Galois invariant
cyclic subgroup instead of a rational point of sufficiently high or-
der, it is not clear how to reduce the general case to the semistable
case, so at this time, the above arguments apply only to the family
of semistable curves.

6. The height on elliptic curves. Let A be an elliptic curve over
the rationals again, and let A^ be its minimal discriminant. We
let y
2 = x 3 - y2x - y3 be a minimal equation, with integer coeffi-
cients. A fundamental problem is to estimate the absolute values

OLD AND NEW CONJECTURED DIOPHANTINE INEQUALITIES 63

ofx,y as function of y2 and y3 for integral solutions in Z ,
and to estimate the height h(x(P)) for rational solutions. Since
A(Q) is finitely generated, A(Q) modulo its torsion group is a free
abelian group, finitely generated. It is a problem to give an upper
bound for the heights of free generators for this group. For conjec-
tures see [La2]. The height h(x(P)) has a great deal of structure.
On the group A(Q) modulo torsion, according to a fundamental
theorem of Néron-Tate, there exists a positive definite quadratic
form
 hA:A(Q)/A(Q)tor^R

such that
 hA{P) = \h{x{P)) + 0{\).

In the next section we shall formulate a fundamental conjecture
about this height. Here, we describe a number of basic properties
which allow us to compute it, and which will be used to deal with
that conjecture.
In the preceding section, we used certain explicit formulas
parametrizing the functions (y2, y3, A, j , x, y). We now need
similar formulas to express the height. It turns out that the height
can be given as a sum
 V

where Xv is a function (the Néron function) given by an analytic
expression on A(QV) for each absolute value v. We shall now
describe these functions. As a matter of notation, for any absolute
value v , we define
 v(a) = -log\a\v.

For instance, if v is p-adic, then v(p
m) = m log/?, so v(a) is
the order m of a at p , times a normalizing factor log/7 which is
used to get global formulas putting all the absolute values together.
As a approaches 0 we want the p-adic order to approach oo, and
similarly for an absolute value at infinity.
The height hA is a quadratic form, but the local functions kv
cannot be quadratic: there has to be some extraneous term ap-
pearing in the quadratic relations locally, and only after taking the
sum over all v does this term disappear. For elliptic curves, a

64  SERGE LANG

neat characterization for the Néron functions was given by Tate
as follows.
Let F be a p-adic field, or the complex numbers.
Let A be an elliptic curve defined over F. There
exists a unique function Àv: A(F) - {0} —• R sat-
isfying the following conditions:
(i) Àv is continuous and bounded outside every
neighborhood ofO.
(ii) Let z be a local uniformizingparameter at
0. Then there exists a bounded continuous
function a on an open neighborhood of 0
such that for all P in that neighborhood,
p zfi 0, we have

Xv(P) = v{z(P)) + a(P).

(iii) For all P, Q e A(F) such that P,Q,
P±Q^0 we have
kv(P + Q)+kv(P-Q)

= 2kv{P) + 2kv(Q) + v(x(P) - x(Q)) - £t/(A).

Without the last two terms, the third relation would be the relation
defining a quadratic function. The final constant involving v(A)
is a conveniently normalized term. When applying the relation of
(iii) globally, the sum over all v of the last two terms will vanish by
the product formula, when x(P), x(Q), are rational numbers, say;
so summing over all v yields a quadratic function on the group
of rational points. It is not difficult to show that this function is
the quadratic height.
We shall now give explicit formulas due to Tate for the Néron
functions Àv in order to be able to estimate the height from below
later. In each case, it is not difficult to verify that the formulas we
give satisfy the desired quadratic relation. The other conditions (i)
and (ii) simply express that the Néron function has a logarithmic
singularity at the origin, and these conditions are also immediately
verified in each case. We shall omit the verification.

v = voo.
In dealing with torsion points on elliptic curves, we have already
remarked that we have a complex analytic isomorphism

C/[T91]->A(C)
where x lies in the upper half plane, and [T, 1] is the lattice

OLD AND NEW CONJECTURED DIOPHANTINE INEQUALITIES 65

generated by r , 1 over Z . We can change T by any element of
SL2(Z), and in particular, we can take T to be in the standard
fundamental domain for SL2(Z). If we let

2nix

Q = Qx = e

then
(*) Imr ^ \\f}> and so \qx\ ^ e~
n .
We let u — uxx + u2 e C (ux, u2 e R), and we let

2niu

be a variable in C*. We let
 oo
g0(t) = g0(q, t) = (I - t)*[[(l - qnt){\ - q"lt).
n=\
Then we have a functional equation for g0 , namely

g0(qt) = -r" 1 g0(t) = g0(t~
l).

Let B2 be the second Bernoulli polynomial,

B 2(r) = T
2 -T+\.

We define the Néron function

Av(u, T) = \B2{ux)v{q) + v(^0(flrM)) = \B2{ux)v{q) + v(g0(t)).

Immediately from the functional equation, we see that Àv(u, r) is
even in u, that is
 kv(-u, r)=Av(u, T).

The term involving B2 serves the purpose of making the function
as we have defined it periodic, with periods 1, r . This can be ver-
ified directly and simply from the functional equation for g0 . The
function kv is real analytic, except for a logarithmic singularity at
the lattice points, as one sees directly from its definition.

Proposition 6.1. For v = v^ there exists a con-
stant C^ > 0 having the following property. Let
Imr > A/3/2 and let \ux\ ^ 1/6. Then

Proof. By the periodicity and the fact that Xv(u, T) is even in u,
we can normalize a representative for a point by the condition

(**) 0 ^ u{ ^ \ whence |<?
1/2| ^ \qu\ ^ 1 and \q
l,2/qu\£l.

66  SERGE LANG

In that case, we conclude that the Néron function has the value

Av(w,T) = -^B 2 (M 1 )log|«|-log|l-?J-0(l) ,

and it is easy to compute an explicit value for 0(1), independent
of u and r . Namely, for n ^ 1, we have estimates

• n , ^ —nn\/3/2

and
 i n, , , n-1/2 1/2, ,^ , w-1/2 , ^ -(«-1/2)TTV / 3/ 2
\Q lQu\ = \Q Q /4U\ = \Q \^
e

These inequalities show that the term -0(1 ) is independent of u
and T. In addition, the choice of \ux\ ^ 1/6 was made so that
B2(«j) ^ 0, and hence the term -B2{ux)\o%\q\ is actually ^ 0
since \q\ < 1. Finally \qu\ < 1, so

log|l -qu\ ^log2 .

The uniform lower bound of Proposition 6.1 for Xv(u, T) follows
at once from these estimates.

We have an analytic isomorphism

C/[r, \]^A{C)byu~Pu.

We also write u = u(P). The function kv(u, T) being periodic in
u, we use it to define the ^-component of the height, namely for
a rational point P corresponding to u we let

kv{P)=kv{u(P),T).

Proposition 6.1 can be restated in part by saying that if P is suffi-
ciently close to the origin, then kv (P) has a uniform lower bound
as in Proposition 6.1.
We shall apply this to multiples of an arbitrary point P which
lie close to the origin, thus giving us a lower bound for the com-
ponent of the height at infinity.

Proposition 6.2. Let C^ be the constant of Propo-
sition 6.1. Let A be an elliptic curve over Q, and
let P e A(Q). Given an integer M ^ 1, there
exists an integer b satisfying

\<b<±6M

such that for v = voo we have

Xv{mbP)^-C00 forl<:m<:M.

OLD AND NEW CONJECTURED DIOPHANTINE INEQUALITIES 67

Proof. We get a homomorphism A(Q) —• R/Z by mapping

Q^ux{Q) modZ .

Let n be a suitably large integer. Partition R/Z into « small
intervals of length \/n . The multiples of the point P given by

0,P , 2P, ... , >?P

map to n + 1 elements of R/Z . Hence there exist integers
0 ^ n{ < n2 ^ n such that fljjP and « 2JP lie in the same small
interval. Let b = n2- n{. Then 0 < b ^ n and £P lies in the
small interval containing the origin. Then

\^{bP)\^\

and therefore
 \ux(mbP)\< — for 1 <m<M.

Thus if we let n - 6M we get \ux(mbP)\ ^ 1/6, and we can
apply Proposition 6.1 to conclude the proof.
Next we deal with the absolute values associated with prime
numbers, and we have to distinguish cases, depending on whether
j is /7-integral or not.

v = v for p prime, and j is p -integral.
Given a prime p, one may reduce the minimal equation of an
elliptic curve mod p . Then the reduced equation defines a possi-
bly reducible curve, called the fiber. The group law on the original
elliptic curve reduces to a group law on the set of nonsingular
points on the fiber.

Proposition 6.3. Let v - vp . Then for all points
P whose reduction mod p is nonsingular on the
fiber, the Néron function is defined by

XV{P) = imax{0 , \og\x(P)\v} + ^(A ) > ^(A) .

This proposition is proved essentially by brute force, cf. for
instance Theorem 4.4 and Theorem 6.1 of [La3, Chapter III] for
the standard Weierstrass equation.
The following result is crucial to know how far a point is from
having singular reduction on the fiber.

68  SERGE LANG

Proposition 6.4. Assume that we are dealing with a
minimal model, and that j is p-integral Then
(i) For every point P e A(F) the point 12P has
nonsingular reduction on the fiber.
(ii) Furthermore, Xv(l2mP) ^ l/12t>(A) for all
positive integers m.

Proof. The proof of the first statement is by computation, using
the Néron-Kodaira classification of all possible cases of degener-
acy which can occur. See Néron's last chapter on elliptic curves
([Ne], the final table), and for more recent insights, Tate's algo-
rithm [Ta2]. It is a very tedious matter. To replace such compu-
tations by theoretical arguments takes very heavy machinery. The
second statement follows by applying Theorem 6.3.
For our purposes the factor 12 is not important, all that matters
is that there is some universal integer which can be used to multiply
a point and land it into the nonsingular part of the fiber.

v — vp with p prime, and j is not /^-integral.
Finally we must give a description of the Néron function for v
when p divides the denominator of j , i.e. j is not p-integral.
This case is a p-adic analogue of the case over the complex num-
bers, with essentially the same formulas. We deal here with the
Tate curve as in §4.
Let Cp be the completion of the algebraic closure of Qp and
let t be a variable in C*. Define

oo
g0(t) = (l-t)Y[(l-q
nt)(l-q
n/t).

The functional equation was formal, and so we have again

g0(Qt) = g0(t~
l) = -t~
lg0(t)9

valid for all teCp. Define
 v(q) oràpq

Proposition 6.5. Let p divide the denominator of

j . Let Pt be the image of t in A(Cp) under the
Tate parametrization. Then

OLD AND NEW CONJECTURED DIOPHANTINE INEQUALITIES 69

Thus we see the analogy with the complex case. From the func-
tional equation of g0 we conclude again that kv(Pt) is periodic
with period q, and so is defined on the elliptic curve.
Now let F be a finite extension of Qp in Cp, and suppose
q e F*. For every t e F* we can find a representative mod q
z

which we denote by tp, and which is uniquely determined by the
condition
 0 < u{t) < 1 or equivalently \q\v < \t\v ^ 1.

For such a representative we see from the formula for gQ that
v(g0(tp)) ^ 0. It is therefore convenient to define the periodic
function
 B: R/Z -+ R by B(w) = B2(w) if 0 < u <; 1,

and B is extended by periodicity to all of R. One can also write

B(u) = {u}
2-{u} + ±

where {u} is the fractional part of u, and we obtain:

Proposition 6.6. Let p divide the denominator of

j , and v = vp. Then

Xv(P)>\*(u{tp))v{q).

Just as Proposition 6.4 gave us a simple criterion to get a nice
formula for the height of points whose reduction is nonsingular on
the fiber, we can formulate a similar criterion which we can apply
to Proposition 6.6. Indeed, if u(tp) = 0 then we get the simple
inequality  lv(P)^±2v(q) = ±2v(A)

just as in Proposition 6.3. Suppose however that P is an arbitrary
point in ^(Q^). Let
b = ovdp(q) = ordp(A).

Then from the definitions, tp eq
Z, and therefore tbp is a /7-adic
unit, and so u(tbP) = 0. Combining the two cases of Proposition
6.4 and 6.6, we find:

Proposition 6.7. Given a positive integer n0 there
exists an integer b > 0 having the following prop-
erty. For all elliptic curves A over Q, and non-
torsion rational point P e A(Q), if v = vp is such

70  SERGE LANG

that j is p-integral or ordp(A) < n0 then

Xv(bP)>±v(A).

7. The Szpiro conjecture implies the minimal height conjecture. Let
A be an elliptic curve defined over Q, and let hA be the Néron-
Tate height. In [Lai] I conjectured that this height satisfies a min-
imum condition as follows. We let AA be the minimal discrimi-
nant.  There exists constants CQ and CQ > 0 such that
for all elliptic curves A over Q and a non-torsion
point P e A(Q), we have

hA(P)^CQloë\AA\-C'Q.

Note that given an integer A ^ 0 there is only a finite number
of elliptic curves A over Q whose minimal discriminant is A.
Consequently we really did not need to mention the constant CL
in the stated inequality, because for log|AJ sufficiently large, the
right-hand side is ^ CQ log |AJ for some CQ > 0, and by picking
log | AA | sufficiently large, we are omitting only a finite number of
values of hA(P). Hence by shrinking the constant CQ suitably,
we obtain the stated inequality without a CQ .
On the other hand in [La2] I also conjectured an upper bound
for the height of suitable free generators of A(Q)/A(Q)t0T, and I
showed that the two conjectures are not independent: the lower
bound conjecture is used to motivate the upper bound conjecture,
and to carry out certain steps in trying to prove it. The essential
point is as follows. Let ( , ) be the symmetric bilinear form giving
rise to the quadratic form hA . Then from L-series considerations,
conjecturally one gets a bound for the determinant det(P/, P.)
of a basis for A(Q) mod torsion. It is possible to construct a
basis {Px, ... , Pr} which is "almost" orthogonalized. "Almost"
is because we are over Z , not over R. For a precise definition,
see [La2] or [La3]. We order the points by ascending height, so

hA{p{)^---<hA{pr).
Then we get a conjectural upper bound for the product

hA{Px)---hA{Pr)-
In order to get an upper bound for hA(Pr) itself, we can then
divide by the first r - 1 terms, and this is where one needs a lower
bound for hA(Px).

OLD AND NEW CONJECTURED DIOPHANTINE INEQUALITIES 71

It occurred to Marc Hindry and to me independently that the
Szpiro conjecture should imply this minimum, and the implication
was proved by Hindry-Silverman [H-S]. I shall describe their proof
in this section.
In the first place, Silverman [S] had proved my conjecture in
the case of integral y-invariant, and so the problem was how to
expand his arguments so that they could apply to the non-integral
case.
As before, we let s be the Szpiro exponent, so that we have

|A| ^ N0(A)
5

except for a finite number of elliptic curves, which we disregard.
We always take the elliptic curve in minimal form, so A is the
minimal discriminant.
For the subsequent proof, it will be convenient to decompose
the minimal discriminant into a product. We let

A = AtA2

where:

A j is the product of the prime powers which occur with an
exponent < 2s
A2 is the product of those prime powers which occur with an
exponent ^ 2s.
Then

(*) loglAJ^loglAI.
 1 lis
This follows immediately from the inequality NQ(A2) ^ A2 , the
inequality
 |A| ^ N0(Af < lA/jy^) ^ |A,r|A2|1/2,

and by substituting A2 = A/Aj on the right-hand side.
The primes dividing A2 are the ones which caused trouble in
extending Silverman's proof. To cancel their negative contribution
to the height, due to a term with the Bernoulli function, Hindry-
Silverman use an averaging process, based on a simple inequality of
analysis, which we extract here. As in the previous section, we let
B be the periodic function obtain from the Bernoulli polynomial
B 2 .

72  SERGE LANG

Lemma 7.1. For all u e R/Z and all positive inte-
gers M we have

M / \ i

m=\
 x '

Proof. We have the Fourier expansion

n / s 1 v - ^ 1 Ininu

But also

M
. /M+l \ /M+l \ M+l , ™ \

Therefore
M  / \
S('-STT) B <'"" )

M oo
1 1V1 OO / \ *
V^ V^ / 1 ^ \ A / Ininmu , —Ininmu^

1 2

^ - — because £(2) = n /6

as desired.
Hindry and Silverman place the lemma in the context of an
inequality for Fourier transforms by Blanksby-Montgomery
[B-M]. The lemma and its proof also fall under the pattern used by
Elkies in estimating Green's functions on Riemannian manifolds,
cf. [La4], Chapter VI, Theorem 6.1.
All that will be used of Lemma 7.1 is that a linear combination
of B(mu) with suitable positive coefficients is uniformly bounded
from below, and the sum of the coefficients tends to infinity. The
specific form of the coefficients is not important for the applica-
tions we shall make.
We now give the proof of the minimal height conjecture assum-
ing the Szpiro conjecture. First, by taking nQ = 2s (for instance),
we can apply Theorem 6.7. Since for all points P e A(Q) we have
hA(bP) = b\(P),

OLD AND NEW CONJECTURED DIOPHANTINE INEQUALITIES 73

it suffices to prove the lower bound for the height of points P
which satisfy the inequality

for all v = v such that p\A{. From now on, we assume that
the point P has this property. We pick M sufficiently large as
a function of s. For instance, M = 4s suffices, as will become
apparent from the following arguments. We let

M M
 M

c^ — l - , ^ . « whence I P c_ = — and C%£ = V* cmm ,
1 " MTÏ
 whence
 5Z
 c
m = y
 and C
M = E
 c
»
m=l m=l
We select b as in Proposition 6.2. Then
M
CMb
2hA(P) = J2^b
2hA(P)

M M
= E cmhA(mbP) = E E cJ-vWP).
m=\ v m=l
We shall give a lower bound for the ^-contribution Yl
 c
mK(
mbP)
for each v . We partition the absolute values v into four sets:

v = v with p f A ;
v =vp with p|Aj ;
v =vp with /?|A2 .
We note that for every non-zero integer d we have trivially
Y,vp(d) = \og\d\.

P\d
\ï v = voo then using Proposition 6.2 and the è of that proposi-
tion, we conclude that the ^-contribution is ^ -MC^ .\îv = vp
with p \ A, then the ^-contribution is ^ 0 by Proposition 6.3.
Therefore by Proposition 6.6 and Lemma 7.1 for p|A2, and Propo-
sition 6.7 for p\A{, we get

CMb
2hA(P) > -MC^ + ^ y loglA.I - ^log|A 2 |

= "
MC°°+4fcMl0g|A|~À
l0g|A|

using (*) and the trivial fact that |A2| < |A|. We may now pick
for instance M = 4s . Then the right-hand side is

= ~ 45C°°
 + 2i l0g|A| '
which concludes the proof.

74  SERGE LANG

REFERENCES

[Ar] M. ARTIN, Néron models, Arithmetic Geometry (G. Cornell and J. Silver-
man, eds.), Springer-Verlag, Berlin and New York, 1986, pp. 213-230.

[BCHS] B. BIRCH, S. CHOWLA, M. HALL, AND A. SCHINZEL, On the difference
x
3 - y1 , Norske Vid. Selsk. Forrh., 38 (1965), pp. 65-69.

[B-M] P. BLANKSBY AND H. MONTGOMERY, Algebraic integers near the unit
circle, Acta Arith., 18 (1971), pp. 355-369.

[BLSTW] J. BRILLHART, D . H. LEHMER, J. L. SELFRIDGE, B. TUCKERMAN AND S.
S. WAGSTAFF, JR., Factorization of bn±1,6 = 2, 3 , 5 , 6 , 7 , 10, 11
up to high powers, Contemporary Mathematics Vol. 22, AMS, 1983.

[Dan] L. V. DANILOV, The diophantine equation x - y = k and Hall's
conjecture, Mat. Zametki., 32 No. 3 (1982), pp. 273-275.

[Dav] H. DAVENPORT, On f3(t) - g
2{t), K. Norske Vid. Selsk. Forrh. (Trond-
heim), 38(1965), pp. 86-87.
[Frl] G. FREY, Links between stable elliptic curves and certain diophantine
equations, Annales Universitatis Saraviensis, Series Mathematicae, 1
(1986), pp. 1-40.

[Fr2] , Links between elliptic curves and solutions of A — B — C , J.
Indian Math. Soc,, 51 (1987), pp. 117-145.

[Ha] M. HALL, The diophantine equation x -y = k , Computers in Number
Theory (A. O. L. Atkin and B. J. Birch, eds.), Academic Press, London,
1971, pp. 173-198.
[H-S] M. HINDRY AND J. SILVERMAN, The canonical height and integral points
on elliptic curves, Invent. Math., 93 (1988), pp. 419-450.
[Kul] D. KUBERT, Universal bounds on the torsion of elliptic curves, Proc. Lon-
don Math. Soc, vol. XXXIII (1976), pp. 193-237.
[Ku2] , Universal bounds on the torsion of elliptic curves, Compositio
Math., 38(1979), pp. 121-128.
[La 1 ] S. LANG, Elliptic functions, Addison-Wesley, 1973, reprinted by Springer-
Verlag, Berlin and New York, 1987.
[La2] , Conjectured diophantine estimates on elliptic curves, Arithmetic
and Geometry, Volume dedicated to Shafarevich, Vol. I, edited by M.
Artin and J. Tate, Birkhauser, 1983, pp. 155-171.

[La3] , Elliptic Curves: Diophantine Analysis, Springer-Verlag, Berlin and
New York, 1978, pp. 212-213.
[La4] , Introduction to Arakelov Theory, Springer-Verlag, Berlin and New
York, 1988.
[L-O] H. LENSTRA AND F. OORT, Abelian varieties having purely additive re-
duction, J. Pure and Applied Algebra, 36 (1985), pp. 281-198.
[Ma 1 ] R. C. MASON, Equations over function fields, Springer Lecture Notes 1068
(1984, 149-157), in Number Theory, proceedings of the Noordwijk-
erhout, 1983.
[Ma2] , Diophantine equations over function fields, London Math. Soc.
Lecture Note Series, vol. 96, Cambridge University Press, United
Kingdom, 1984.

OLD AND NEW CONJECTURED DIOPHANTINE INEQUALITIES 75

[Ma3] , The hyperelliptic equation over function fields, Math. Proc. Cam-
bridge Philos. Soc, 93 (1983), pp. 219-230.
[Maz] B. MAZUR, Modular curves and the Eisenstein ideal, Inst. Hautes Études
Sci. Publ. Math. (1978).
[Ne] A. NÉRON, Modèles minimaux des variétés abéliènnes sur les corps lo-
caux et globaux, Inst. Hautes Études Sci. Publ. Math., 21 (1964),
pp. 361-482.
[Ri] K. RIBET, On modular representations of Gal(Q/Q) arising from mod-
ular forms (to appear).
[Se] J. P. SERRE, Sur les représentations modulaires de degré 2 de Gal(Q/Q),
Duke Math. J., 54 (1987), pp. 179-230.
[Si] J. SILVERMAN, Lower bound for the canonical height on elliptic curves,
Duke Math. J., 48 (1981), pp. 633-648.
[Tal] J. TATE, The arithmetic of elliptic curves, Invent. Math., 23 (1974),
pp. 179-206.
[Ta2] , Algorithm for determining the type of a singular fiber in an el-
liptic pencil, Modular Functions in One Variable IV, Lecture Notes
in Math., vol. 476, Springer-Verlag, Berlin and New York, (Antwerp
Conference).
[Ve] P. VOJTA, Diophantine approximations and value distribution theory,
Lecture Notes in Math., vol. 1239, Springer-Verlag, Berlin and New
York, 1987.

DEPARTMENT OF MATHEMATICS, YALE UNIVERSITY, NEW HAVEN, CONNECTI-
CUT 06520
