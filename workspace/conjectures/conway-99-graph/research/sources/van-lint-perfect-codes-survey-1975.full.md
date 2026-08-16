<!-- source: https://projecteuclid.org/journals/rocky-mountain-journal-of-mathematics/volume-5/issue-2/A-survey-of-perfect-codes/10.1216/rmj-1975-5-2-199.pdf | converted from PDF -->

ROCKY MOUNTAIN
JOURNAL O F MATHEMATICS
Volume 5, Number 2, Spring 1975

A SURVEY OF PERFECT CODES

J. H . VAN LINT

1. Introduction. In recent years there has been a lot of interest in
so-called "perfect codes". Originally a topic in the theory of error-
correcting codes, there are now connections to group theory, com-
binatorial configurations, covering problems and even diophantine
number theory. As the results are spread over many fields and journals
and since many of them are quite recent there has been a lot of duplica-
tion and more is to b e expected. For this reason it seems worthwhile
to write a survey of what is known (to this author) at the moment.
To introduce the subject and for further use in this survey w e need a
number of concepts from the theory of error-correcting codes which w e
now introduce briefly.
Consider a set F of q distinct symbols. W e shall call this set the
alphabet. By J?(n) : = F n we denote the set of all n-tuples from F,
i.e.

(1.1) ,#<»> : = {(au 02, ' ' *, an) \ a, G F, i = 1,2, • • -, n}.

In many cases we shall impose some algebraic structure, e.g., F will
be a ring and tR{n) an F-module. If F is the field GF(q) w e can con-
sider <s/?
(n) as an n-dimensional vector-space over F. W e write
a : = (ah a2, * * *, an) and use the words vector or word to denote the
n-tuples from Ji{n) (n is called the block length or word length). W e
also introduce a metric d in cR
{n). In coding theory the most familiar
metric is Hamming-distance defined by

(1.2) d(x, y) : = the number of indices ifor which x{ ^ t/j.

In many cases one of the symbols of F is denoted by 0 (zero). We then
define the weight w(a) of a word a by

(1.3) w(a) : = the number of indices ifor which a^ j£ 0.

Note that if 0 : = (0,0, • • -, 0) then w(a) = d(a, 0).
If x G J?
in) and e è 0 is an integer we define the sphere S(x, e) with
center x and radius e by

(1.4) S(x, e):={y£^») | d{x, y) ^ e}.

Received by the editors November 16, 1972.

Copyright © 1975 Rocky Mountain Mathematics Consortium
199

200  J. H. VAN LINT

Clearly

(1.5) |S(x,e)|= tOiq-iy.
i=0

Any subset C of *#<"> is called a code. If F = GF(q) and <^<
n> is the
n-dimensional vector-space over F then C is called a linear code (or
(n, fc)-code) if C is a fc-dimensional linear subspace of cR
{n\ A slightly
weaker concept is a group code. This name is used if <s/?
(n) is an addi-
tive group an d C a subgroup. A code C is an e-error-correcting code
if

(1.6) V xE C VyGC [(* ^ y) => d(x, y) ^ 2 e + 1] ,

i.e.,

(1.7) VxGC VyGC [(x ^ y) =* S(x, e) fi % , e) = 0] .

If for such an ^-error-correcting code C th e union of these spheres is
*/?<">, i.e.,

(1.8) <*<»>= U S(%,e)
xG C

then the code is called perfect. In this case there is, for every y G <^?
(n),
a unique xE C with d(x, y) = e.
In th e following w e shall make use of some terminology from th e
theory of linear codes which we now introduce. If C is a linear code
of dimension fc and xl7 x2,* * •, x& form a basis of C then th e matrix G
with row-vectors x1? x2, * ' ',xk is called a generator matrix of C. A
generator matrix H of the orthogonal complement C of C in ^?(ri) is
called a parity-check matrix of C. The orthogonal complement itself
is called the dual code of C. Clearly we have

(1.9) C = {a G </?<»> | a = (bl9 b2i • • -, bk) G  %b{ G F, i = 1,2 , • • -, fc}

an d

(1.10) C = {aG^|atf T =0} .

The error-correcting properties of a code do not change if we apply
a permutation n of th e places to ^?(n), e.g., ir(ai, a2, • * *, an) =
(an, an_i, * * ",fli). Th e resulting codes are called equivalent codes.
Sometimes th e definition of equivalence is extended by also allowing
a permutation of the symbols of F; (this will in general destroy
linearity).
The main purpose of this survey is to discuss the connection of per-
fect codes to several other problems and to show how the problem of

A SURVEY OF PERFECT CODES  201

the existence of such perfect codes was completely solved in the case
where F is a finite field. First, however, we wish to show how the
concept of perfect code, as introduced above, can be generalized in
several directions and how some analogous problems can be formu-
lated.
Let (^?, d) be a metric space (d the distance function) and e > 0.
A subset CC^i s called a perfect e-code if Jt is the disjoint union of
the spheres of radius e (as in (1.8)) around the points of C. In this
formulation we have a sphere-packing problem of a special nature.
A rather natural generalization of the Hamming metric is the Lee-
metric defined as follows when F is the ring of integers mod q:

n
(1.11) WL(x) : = J ) niin{Xb q ~ *i}>
i = l

where the sum is taken in Z, and

(1.12) d L{x,y): = W L(x-y).

Very little is known about perfect codes with this metric. (See § 8.)
A more complicated way to generalize perfect codes is the following.
Start with n alphabets Fh F2, • • -, F n and let *R : = Fl X F 2 X • • • X
Fn. Define Hamming metric as in (1.2). Again, we can study perfect
codes in Ji. (See § 8.)
If J?
in) is n-dimensional vector-space over GF(q) and C C */?
(n) is
a perfect e-error-correcting code, then by (1.8) we have <^?
(n) =
S(0, e) © C, a direct sum. We can now generalize the problem by
varying the set S. If, e.g., we take S to include all vectors of weight
= e and also some of the vectors of weight e + 1 then any solution
C is called a quasi-perfect code. This class of codes contains codes
which are called nearly perfect. These will be treated in § 8.
The geometrical problems of packing spheres in cR
in\ resp. covering
<s/?
(n) with spheres meet in the case of perfect packings (coverings).
Therefore it is to be expected that some results concerning perfect
codes originate from the study of covering problems. Typical examples
are perfect single-error-correcting codes which turned up several
times in connection with the following group theory problem (Taussky
and Todd [65] ). Let G be an abelian group with base elements
gi» g2> ' ' ' gn> all of order q. Let S be the set of all powers of the base
elements, i.e., S = {g? \ i = 1,2, • • -, n; 0 S a < q}. Let if be a subset
of G such that every element g of G can be written as g = hs with
h Çz H, s G S. This is called a group covering. Taussky and Todd
asked for the minimal number of elements in such a set H and whether
H could be a subgroup. (See § 2.)

202  J. H. VAN LINT

This survey is organized as follows. In § 2 we discuss perfect
single-error-correcting codes. In section 3 we discuss the two known
nontrivial perfect ^-error-correcting codes with e ^ 2. These are
known as the Golay codes. We shall illustrate their connection with
combinatorial theory and group theory. More connections between
perfect codes and combinatorial theory will be discussed in § 4. The
interesting properties of the known perfect codes have stimulated the
search for more such codes. The obvious thing to do is to consider
the necessary condition for the existence of such codes which follows
from (1.8) by counting the number of elements on both sides. This
leads to a number theoretic problem. The condition, known as the
sphere-packing condition, is treated in § 5. A deeper theorem yield-
ing a necessary condition for the existence of perfect codes is known
as Lloyd's theorem. This is discussed in § 6. In the past few years an
extensive study of the combined necessary conditions has led to a
proof that all perfect codes over alphabets which are finite fields are
known. We summarize the methods in § 7. Finally, in § 8, we shall
discuss the generalizations mentioned earlier in this introduction.

2. Perfect single-error-correcting codes. Perfect single-error-cor-
recting codes (s.e.c. codes) have been constructed for every field
alphabet GF(qf). They are known as Hamming codes (sometimes H-G
codes, the G for Golay who contributed to the development of the
idea first used by Hamming [28] ). The codes have been rediscovered
a number of times, e.g., as a solution of the problem of Taussky and
Todd mentioned in the introduction (see later in this section). We
mention the references Cocke [15], Golay [24], Losey [45], Mac Wil-
liams [47], Mauldon [49], Zaremba [72], [73].
Hamming codes are defined as follows. Let the ?n-dimensional
vector-space J?
{m) over GF(q) be interpreted as a model of the affine
geometry AG(m, q). There are n : = (q
m — l)/(g — 1) lines through
the origin 0. On each of these we choose one non-zero vector. We
take these vectors as columns of a matrix H (m rows, n columns). Con-
sider H as the parity-check matrix of a linear code C in */?
(n) (cf. (1.1),
(1.10)). Since a linear combination of less than three columns of H
is zero only if the coefficients are zero, the non-zero words of C all
have weight ^ 3. Hence C is an s.e.c. code ((1.6) holds with e = 1). C
is a subspace of J?
{n) with dimension n — m. By (1.5) we have S(x, 1) =
q
m for xGC. Therefore we find from (1.6) that |U xGCS(x,l)| =
qn-mqm _ ^n - |^(n)|? [e^ (U ) holds and hence C is perfect! (For
a generalization of this idea see § 8.)
The special case q = 2 is particularly elegant. We can choose the

A SURVEY OF PERFECT CODES  203

columns of H to be the binary representations of the integers 1, 2, * • -, n.
If c is a vector in the Hamming code, i.e., cH
T = 0, and c' is ob-
tained from c by changing the j-th coordinate of c (a single error)
then c'H
T is the binary representation ofj (the place where the error
occurs).

DEFINITION (2.1). If Ai denotes the number of code words of weight
i in a code C then A(z) : — ^f^o A ^ is called the weight enumerator
ofC.

If C is a perfect s.e.c. code of length n over an alphabet of q symbols
(q not necessarily a prime power) then

(2.2) ^
+ n(q — 1)[1 + (qr — l)z] <»-i>/*(l - z)(»«i-i)+iy<i}.

This result is obtained by a straightforward counting argument (Peter-
son [53] p. 68; van Lint [41] p. 89).
Before looking at the problem of the existence of perfect s.e.c. codes
in the case that | F | is not a power of a prime we give an alternate
description of Hamming codes, valid if q is a power of a prime, n =
(q
m — l)l(q — 1) and (n, q — 1) = (m, q — 1) = 1. To do this we
introduce the concept of a cyclic code which will turn up again later.
A linear code C is called cyclic if

(2.3) (ao9ai9 ' • *,a n-i)
 e C <=^>(an.l,a0,ai, • • *,an_2) €E C.

If R denotes the ring of polynomials with coefficients in GF(q), i.e.,
R: = (GF(q)[x], +, ) and S is the ideal generated by x
n — 1, i.e.,
S : = (({x
n — 1}), + , ), then the residue class ring Rmod S is repre-
sented by the polynomials OQ + axx + • • • + a^i*" - 1 of degree
< n. As an additive group R mod S is isomorphic to J?
(n) and a cyclic
code C corresponds to an ideal in Rmod S (cf. Peterson [53] p. 137;
Berlekamp [12] p. 129; van Lint [41] p. 42). Now let a be a primi-
tive element in GF(gm). Then ß = a
q~
l is a primitive n-th root of
unity in GF(q
m). The minimal polynomial (over GF(q)) ofß, which we
call g(x), has degree â m. In R mod S the polynomial g(x) generates
an ideal which corresponds to a cyclic code C of dimension è n — m.
If we represent l,/3,/32, • • *,/3n_ 1 as vectors (with m coordinates) over
GF(q) and take these vectors as columns of a matrix H then aH
T = 0,
where a: = (a0, fli, * * ",ön-i), means the same thing as Oo + fl^
+ • • • + an^xa
n~
l = 0, i.e., g(x) divides a0 + Ö^X + • • • + an_Yx
n~
l

and hence a G C. It is easily seen that the code C is equivalent to a

204  J. H. VAN LINT

Hamming code as described earlier in this section. We remark that if
(n, q — 1) ^ 1, Hamming codes can be described in a similar way by
replacing x
n — 1 by x
n — c; c suitably chosen in GF(q).
There are no examples known of perfect s.e.c. codes in the case
where | F | is not a power of a prime (except of course the trivial
example n= 1 and C any one-element subset of F). From (1.1),
(1.5), (1.8) it is obvious that

(2.4) 1 + n(q - 1) | q
n

is a necessary condition for the existence of a perfect s.e.c. code of
word length n over an alphabet of q symbols. (We remark that if
q = p
a, p prime then (2.4) implies that 1 + n(q — 1) is a power of
q (cf. van Lint [41] p. 87). If n = q + 1 then (2.4) is satisfied. The
first case to be studied then is q = 6, n = 7. Strangely enough, this is
the only case for which it has been shown that there is no perfect s.e.c.
code (cf. Golomb and Posner [25] ). The curious exception is a conse-
quence of the nonexistence of two orthogonal Latin squares of order 6.
We return to this fact later in this section. If (2.4) holds and n = 1
(mod q) then all the coefficients in (2.2) are integers which means that
no nonexistence theorem is to be expected from that direction.
If any such perfect codes exist they will be hard to construct. This
is a consequence of a theorem of B. Lindström [37] which states that
if n = q + 1, q is not a power of a prime, and C is a perfect s.e.c. code
over an alphabet of q symbols, then C is not a group code! This was
generalized by H. W. Lenstra Jr. [35] to:

THEOREM (2.5). Let G{ (1 ^ i ^ n) be a group with underlying set
F. Suppose there exists a subgroup C C H" =i G{ such that the under-
lying set of C is a perfect e-error correcting code of block length n
over F, with e < n. Then q is a power of a prime p and each G{ is
abelian of type (p, p, • • *, p).

In 1962 Ju. L. Vasil'ev produced nonlinear perfect s.e.c. codes.
Later his construction was generalized. References are Lindström
[37], Schönheim [58], Vasil'ev [69]. The results are combined in:

THEOREM (2.6). If q is a power of a prime, n = (q m+ 1 — l)/(q — 1),
where m e 3 if q = 2 and m § 2 if q ^ 3, then there exists a perfect
single-error-correcting code of length n over GF(q) which is not
equivalent to a linear code.

In (2.6) equivalence includes permutation of the symbols of the
alphabet. This concludes the discussion on construction and existence
of perfect s.e.c. codes. We are left with

A SURVEY OF PERFECT CODES  205

PROBLEM (2.7). Are there any perfect single-error-correcting codes
over an alphabet F for which \F\is not a power of a prime?

It is worthwhile tc give a brief look at some interesting results con-
nected with perfect s.e.c. codes discussed in a paper by Golomb and
Posner [25]. Let us consider once again a Hamming code C of
length n = q + 1 over GF(qr). The dual C of this code has dimen-
sion 2, i.e., C 1 consists of q
2 words of length q + 1. If, for a : =
(<*!, 02, ' ' -, an) and b : = (bl9 b2, ' ' -, b„), (a f 6), a, = b, and
aj = foj (i / j) then a and fo are both orthogonal to a word of weight
2. Since there are no words of weight 2 in C it follows that any 2
words a and b in C have distance = n — 1 = g. If we make a
list of the q
2 words of C 1 (q
2 rows, q + 1 columns) then in any 2
columns of this list every pair (i,j) occurs once. Such a combina-
torial object is called an orthogonal array OA(q, q + 1) (cf. Hall [27] ).
It is well known that the existence of such an array is equivalent to
the existence of a projective plane of order q. Now in this discussion
we have assumed linearity of C but there is some reason to conjecture
that the existence of a perfect s.e.c. code of length n = q + 1 is as
hard to show as the existence of a projective plane of order q. For
many other interesting connections between combinatorial theory and
perfect codes we refer to the original paper (Golomb and Posner
[25] ).
In a football pool one wishes to forecast the outcome (win, lose or
draw) of n football matches. To win second prize one must have
n — 1 correct results. The question is what is the most efficient way
of making a number of forecasts such that, no matter what the outcome
of the matches, at least one of the forecasts will have ^ n — 1 correct
results. If n = (3m — l)/2 there is a solution with 3 n ~ m forecasts and
this solution is provided by the Hamming code of length n over GF(3).
It was this problem which led Taussky and Todd to their group theory
problem mentioned in § 1. Further references: Stanton [62], John-
son [84].
Another amusing (old) problem connected to the Hamming code
over GF(3) is the penny-weighing problem: Given a balance which
can be used to determine whether two weights are equal, or which is
heavier, and given a certain quantity of pennies, of which at most one
may be heavier or lighter than the standard weight, it is asked to
determine what paired assemblies of pennies should have their weight
compared with each other, in order to find, with a minimum number
of operations, which penny, if any, is too heavy or too light. It is also
required that the weighing program be completely predetermined,
and thus not affected by the results of the successive weighings. By

206  J. H. VAN LINT

now the connection to perfect codes should be obvious to the reader.
For details we refer to Assmus and Mattson [10], Golay [24], van
Lint [38].

3. The Golay codes. Obvious and trivial examples of perfect ^-error-
correcting codes with e > 1 are

(3.1) n arbitrary, q arbitrary, e = n,C consists of one word;

(3.2) n odd, q = 2, i.e., F : = {0,1}, C consists of the zero
word and the all-one word. In this case e = (n — l)/2.
The code is known as the repetition code.

The codes (3.1) and (3.2) are called trivial perfect codes. We exclude
them from further discussion. There are two known non-trivial per-
fect e-error-correcting codes with e > 1. In this section we discuss
representations and properties of these codes which have been shown
to be unique (cf. (3.5)). The codes were first discussed by Golay [22].
Here we introduce them as quadratic-residue codes (cf. Berlekamp
[12] p. 352; van Lint [41] p. 79). We refer to the introduction of
cyclic codes in § 2 of this survey.

DEFINITION (3.3). Over GF(2) we have

x
23 - 1 = (x - l)(x
il + x 9 +x 7 + x6 + xHx+l )

• (x
11 + x
10 + x6 + r 5 + xHx 2 +l )

= (x - l)gò(*)gi(z).

The polynomial go(*) generates a (23,12) cyclic code called the binary
Golay code.

DEFINITION (3.4). Over GF(3) we have

x ll -l = (x- l)(x5 + x
4 - x
3 + x
2 - l)(x
5 - x
3 + x
2 - x - 1)

= (* - l)go(*)gi(*).

The polynomial go(s) generates an (11,6) cyclic code called the ternary
Golay code.

There are several ways of showing that the minimum distance of the
binary Golay code is 7 and that the minimum distance of the ternary
Golay code is 5 (cf., e.g., van Lint [41] ). For both codes (1.8) then
follows by counting (cf. (1.5)). Hence the binary Golay code is a per-
fect 3-error-correcting code over GF(2) and the ternary Golay code is
a perfect 2-error-correcting code over GF(3).
In the following theorem we call two codes equivalent if one is
obtained from the other by a monomial transformation on the vector
space cR
{n\ i.e., a linear mapping defined by a matrix DP where D is

A SURVEY OF PERFECT CODES  207

a diagonal matrix and F a permutation matrix. The following theorem
is due to V. Pless [54] (see Comment (9.1)!):

THEOREM (3.5).
(i) Every perfect 2-error-correcting code of word length 11 over
GF(3) is equivalent to the ternary Golay code, (assuming linearity),
(ii) every perfect terror-correcting code of word length 23 over
GF(2) is equivalent to the binary Golay code, (assuming linearity).

In fact more is proved in the paper. For codes with the parameters
of the Golay codes a number of properties are shown to be equivalent.
One of these is the property of being perfect, another is equivalence
with a Golay code. The proof depends on the following property that
both of the Golay codes have. If C is an (n, k) code we call C + the
extended code if C + C <s/?
(n+1> is obtained by adding an extra coor-
dinate to the words of C, which coordinate is a fixed linear combina-
tion of the remaining coordinates. Then C + is an (n + 1, k) code.
The most common extension is obtained by requiring that in the ex-
tended code every word is orthogonal to (1,1, • • •, 1). Then it can be
shown that the following is true.

THEOREM (3.6). The extended Golay codes are self-dual if the
original codes are suitably represented, (cf. van Lint [41], Pless
[54]).

This property was used by Goethals [20] to construct a simple
decoding algorithm for the binary Golay code. For other decoding
methods see Assmus and Mattson [10], Chien [14].
The following representations of the two Golay codes are often
useful. For details we refer to Karlin [33], van Lint [41]. Let
Cn be the circulant matrix of size 11 with first row (11011100010) and
let C5 be the circulant matrix of size 5 with first row (01—1—11) .

11 •• 1

Il2 Cll  , G 2 : =

are generator matrices of the two Golay codes.
A particularly simple description of the binary Golay code was
given by R. Turyn, cf. réf. [7]. Let H be the (8,4) code obtained
by extending the (7,4) Hamming code. Numbering the positions from
1 to 8 we obtain the code W by applying the permutation (1,7) (2,6)
(3, 5) to the positions. Then

V:= {(a+ c,b + c,a+b+ c)\aGH,bGH,cGH'}

208  J. H. VAN LINT

is a (24,12) linear code over GF(2). By showing that this code has
minimum distance 8 it follows from (3.5) that V is the extended binary
Golay code. For details we refer to van Lint [41] p. 100.
For the sake of completeness we give the weight enumerators of the
Golay codes. Obviously the fact that the codes are perfect is enough
information to calculate these weight enumerators. Several other
methods are faster. The weight enumerator of the binary Golay code
is:

(3.6)
1 + 253 z
7 + 506 z
8 + 1288 z
n + 1288 z
12 + 506 z
15 + 253 z
lG + z
23;

the weight enumerator of the ternary Golay code is

(3.7) 1 + 132 z
5 + 132 z
6 + 330 z
8 + 110 z
9 + 24 z
li.

Recently Goethals [20] obtained a. new non-linear code, having
256 code words of length 16 at mutual distance at least 6 by consider-
ing a subset of the binary Golay code and dropping 8 coordinates.
He showed that dropping one more coordinate gives a code equivalent
to the Nordstrom-Robinson code (Nordstrom and Robinson [51] ).
Preparata [56] gave a method of extending a class of nonlinear 2-
error-correcting codes which, when applied to the Nordstrom-
Robinson code, produces the binary Golay code. This is Goethals'
result obtained from the other direction. Other results obtained by
considering a subset of the positions in the Golay codes will be men-
tioned in the next section.
Many interesting groups can be described by considering auto-
morphism groups of certain combinatorial configurations, i.e., per-
mutation groups on the elements of such a configuration which leave
the configuration invariant. As an example one can consider a code
and permute the coordinate places as we did in the definition
of equivalence in § 1. Those permutations which leave the code
invariant (as a subset of J?
in)) form the automorphism group of the
code. It was shown by Assmus and Mattson [4] that the auto-
morphism groups of the extended Golay codes are the Mathieu groups
M24 and M12, (cf. also Berlekamp [12] p. 395; Paige [52]). The
groups Mn, A^22> M23 appear as the automorphism groups of special
tactical configurations called Steiner systems (see § 4) obtained from
the Golay codes. Recent discoveries of new simple groups on the one
hand and the connection between the Mathieu groups and the Golay
codes on the other explain the interest of group theorists in the search
for new perfect codes. The results to be discussed in § 7 were a dis-
appointment for them. (Additional reference: Todd [93] ).

A SURVEY OF PERFECT CODES  209

4. Perfect codes and combinatorial theory. There are several con-
nections between perfect codes and combinatorial theory. Most of
these are applications in which error-correcting properties of the codes
are not important but where the structure of the codes leads to interest-
ing results. We mentioned a few of these results in § 2 (Golomb and
Posner [25] ).

DEFINITION (4.1). A tactical configuration of type k; t — d — n
(also called a t-design) is a collection !£> of d-subsets of an n-set S
such that every f-subset of S is contained in exactly À distinct mem-
bers of 2 \ To avoid trivial configurations one usually demands
0 < t < d < n.

For the special case t = 2 the tactical configuration is called a
balanced incomplete block design. In the case A. = 1 the tactical con-
figuration is called a Steiner system of type (t, d,n). The following
theorem illustrates the connection with perfect codes. We state the
result only for binary codes. By adding the assumption of linearity
it can be generalized to other alphabets (Assmus and Mattson [5] ).

THEOREM (4.2). Let V be a binary perfect e-error-correcting code of
block length n and assume 0 €E V. Then the collection *h of (2e + 1)
subsets D of {1, 2, • • •, n}for which there is a codeword in V with its
nonzero coordinates in the positions of D is a Steiner system of type
(e + 1, 2e + 1, n).

For a proof see van Lint [41] p. 95. A simple counting argument
then leads to the following theorem.

THEOREM (4.3). If a binary perfect e-error-correcting code of block
length n exists then the numbers

(.;T-\)/(^ +I--*)-*-<»••••••

are all integers.

This theorem has been used to show the non-existence of certain
perfect codes. Now that the results of § 7 are known the theorem has
lost its importance. Another theorem of the type of (4.2) is

THEOREM (4.4). The codewords of weight 8 {interpreted as subsets of
{1,2, • • *,24}) in the extended binary Golay code form a Steiner
system of type (5, 8,24).

Goethals [20] derived several block designs from this Steiner
system. For extensive treatment of this type of application of perfect
codes cf. Assmus and Mattson [5], [6], [8], [9]; Paige [52]. The

210  J. H. VAN LINT

results of Assmus and Mattson were generalized to semilinear codes
by J. Schönheim [59]. For a connection between tactical configura-
tions and nearly perfect codes see § 8.
An interesting application of the ternary Golay code to graph theory
is given in Berlekamp, van Lint and Seidel [ 13]. The paper is con-
cerned with strongly regular graphs in which every adjacent pair of
vertices is in exactly one triangle an d every non-adjacent pair of
vertices is in exactly one quadrangle. If n is the number of vertices of
such a graph then one can show that n must be one of the integers 9,
99, 243, 6273 o r 494019. The example for n = 9 is easily found. Fo r
n = 243 the ternary Golay code provided an example in the following
way. The columns of the 5 by 11 parity check matrix H  of the ternary
Golay code are considered as points x{ (i = 1, 2, • • -, 11) in 5-dimen-
sional vector space over GF(3). The vertices of the graph are 0,
±xh (i = 1,2, •••,11), an d ±xi±xj,i^j, (i,j = 1, 2, • • -, 11).
If the difference of two vertices is ± xfe they are called adjacent. It
is easy to check that this graph has the required properties. For the
other 3 values of n the problem is still open.

5. The sphere-packing condition. An obvious necessary condition
for the existence of a perfect ^-error-correcting code of word length
n over an alphabet of q symbols (if q is a power of a prime p we write
q = p
a) is obtained from (1.5) and (1.8) in the same way as (2.4). Th e
condition is

(5.1) S (ï)(q-iy\q»

t= 0

and it is known as the sphere-packing-condition. If q = p a it follows
from (5.1) that

(5.2) E  (ï)(q-iy=q
k-
i= 0

By expanding the power of (q — 1) we find

(5.3) ± i-iy^oct'j1) =(-i)y.

A counting argument of the same type as was used to derive (5.1)
is th e following. Consider a perfect e-error-correcting code an d
assume without loss of generality that 0 is in the code. All the other
words of the code have weight a t least 2e + 1. Hence each word of
weight e + 1 is at distance e from exactly one codeword of weight

A SURVEY OF PERFECT CODES  211

le + 1. Hence the number A2e+l (cf. (2.1)) is [(A)/(% +1)] (9 - l)
e + l

Hence

THEOREM (5.4). A necessary condition for the existence of a perfect
e-error-correcting code of block length n over an alphabet of q
symbols is that
 [(A)/(2ee+1)](9 - l) ê + 1

is an integer.

Note that q = 2 yields the case h = 0 in (4.3).
Extensive computer searches have been made to find solutions of
(5.2) with e > 1. The ranges that were covered were:
(a) e = 2, q odd, 3 g q â 125, 3 g fc ^ 40000 (Cohen [16] ),
(b) e ^ 20, 9 = 2, n ^ 2 7 0 (McAndrew [50] ),
(c) & g 1000, 9 ^ 100, n ^ 1000 (van Lint [38] ).
Excluding the parameters of trivial codes the computer searches
yielded only the parameters of the Golay codes and 9 = 2, e = 2,
n = 90. The last set is excluded by (4.3).
The first papers on nonexistence of perfect codes all started with the
equation (5.2). The theorems are of two different types which we now
discuss briefly. The first method is due to Shapiro and Slotnick [61].
They observed that if q = 2 and e is odd, then the left-hand side of
(5.2) can be written as (n + l)Re(n)le\, where Re(n) is a polynomial
of degree e — 1 with integer coefficients. Therefore (5.2) implies that
n + 1 = 2
lb, where b \e\, and substitution in Re(n) yields an equa-
tion for £ and b. It follows that the possible values of n are in a finite
set. This had also been observed by Golay [23]. The method of
Shapiro and Slotnick was also applied by Leont'ev [36]. By a modifi-
cation of this same method and using only hand computation Johnson
[31] showed there are no nontrivial binary perfect ^-error-correct-
ing codes for 5 = e =i 29, e odd. This was extended to e ^ 39, e odd
by James, Stanton and Cowan [30].
The other early nonexistence theorems all concern e = 2. For that
case (5.2) can be interpreted as a quadratic equation in n. For this
equation to have a solution in integers it is necessary that the diophan-
tine equation x
2 — (q
2 — 6q + 1) = 8q
k has a solution in integers.
This diophantine equation can be treated by considering a suitable
algebraic extension of Q or using continued fraction methods. The
following cases were settled:
(a) g = 5, Engelman [19]
(b) q =? 5 (and 9 = 6, assuming linearity), Cohen [16]
(c) 7 ^ 9 g 9,Alter [1], [2].

212  J. H. VAN LINT

In each case no unknown solutions to (5.2) were found. Although as
far as perfect codes are concerned the problem has been settled, the
purely number-theoretic problem of finding all solutions of (5.2)
remains open. (cf. also Alter [3] ).

6. Lloyd's theorem. A necessary condition for the existence of a
perfect binary code, deeper than (5.2), was found by Lloyd [44].
This theorem was generalized by F. J. MacWilliams [46] and recast
by A. M. Gleason (cf. Assmus and Mattson [5] ). Below we shall sketch
a proof for the case q = p
a (p prime) as given in van Lint [41].
Recently it was shown by Delsarte [17] and Lenstra [35] that the
theorem holds for all q. A polynomial which plays a role in the
theorem has been shown by Delsarte to be connected with a sequence
of orthogonal polynomials defined by Kravcuk in 1929 (cf. Szegö
[64] ).
Before formulating Lloyd's theorem we introduce the Kravcuk
polynomials. We assume n is fixed.

DEFINITION (6.1). The Kravcuk polynomial Pk(x) of degree k is
defined by

Pk(x) : = 2 (-W9 - IM P ( H ) > ° = * =
 n>
j=0
where
 x = x(x - 1) • • • (x - j + 1)
{jh fi

The Kravcuk polynomials are connected to the MacWilliams trans-
form for the weight enumerator of a code and its dual (cf. Berlekamp
[ 12] 16.2) in the following way:
If A(x,y) : = Sil o A^-'the n

B(x, y): = A(y-x,y+(q- l)x) = f BkxY~h

where Bk = 5^=0 AiPk(i). The polynomials Pk(x) satisfy the ortho-
gonality conditions

(6.2) Ë (! ) (9 - W<)P.( 0 = ( " )9n(9 - D r 8- O^i^n ,

i=0

where 8rs is the Kronecker symbol. (For further relations see Delsarte

[17])-
 A SURVEY OF PERFECT CODES  213

DEFINITION (6.3). Lloyd's polynomial Qe(x) is defined by

k=0

The polynomial Qe(x) has degree e and can be written as

(6.5) Qe{x) = i (-i)r;1) cziiiq - !)*-'>

or

(6.6) <?,(*) =(-1)« ± (-lyqKY) Ctj
1).

Then we have

THEOREM (6.7). If a perfect e-error-correcting code of block length
n over an alphabet ofq symbols exists, then Qe(x) has e distinct integral
zeros among 1, 2, • • -, n.

Essentially the theorem depends on a counting argument. No struc-
ture of the alphabet is necessary and the perfect code need not be
linear. The proof we sketch is for the case q = p
a in which case we
can take GF(q) for our alphabet. This allows us to make certain
simplifications but these are not essential (cf. Lenstra [35] ).
Let (2C> ©> *) be the group ring of <^?
(n) over Q where we use 0
and S to distingusih formal addition from vector addition in J?
(n)-
The set 2f is

In the following we identify any subset CC^? (n ) with the element
S cEc
 c of 5f • If C is a perfect ^-error-correcting code and Se : =
S(0,e)(cf.(1.4))then

(6.8) Se* C = <#<»>.

If Vi : = (1,1, • • -, 1,0,0, • • ',0)G J?
in) is the vector for which the
first i coordinates are 1 and the other coordinates are 0, then Q : =
{c + Vi | c GE C} is also a perfect code and Ci has minimum weight
i (0 ^ i ^ e). The elements C0, Q , • *, Ce are linearly independent
over Ç). Let G be the group of all monomial transformations of ^?
(n.
}

Then the mapping T defined by

214  J . H . VAN LINT

(6.9) TCg «**):= -£ r la,5>(* )

is a homomorphism of % into the (n + 1)-dimensional subspace

*:={!* ( S x)|oftGÇ } .

A straightforward calculation shows that Se(A) : = Se * A defines a
linear transformation of 3C and that the e linearly independent ele-
ments Q — C0 (i = 1, 2, • • -, e) satisfy Se(Q — C0) = 0. Hence the
kernel K of Se has dimension at least e. For the next step of the proof
let X be any non-trivial character on (GF(qf), +) . Then it is not hard
to show that if we define X„ : <R(n) -» C
 x by X„(x) : = X((x, u)) and
extend this in the obvious way to a linear functional on 2f, then the
functionals X{ : = XVi span the space of all linear functionals on 2f.
A direct calculation shows that Xw(Se) = Qe(w) for ti; = 0,1, • • •, n.
Since Xw(Se)Xw(A) = 0 for all A in K and the Xw are linearly inde-
pendent there must be at least (and therefore exactly) e integral
values of w for which Qe(w) vanishes. Since Qe(0) ^ 0 this proves
the theorem.
We mention that these zeros of Qe are exactly the weights of the
words in the dual of the perfect code in case this code is linear. For
this and details of the proof we refer to van Lint [41]. Lenstra's
proof for arbitrary q follows the same pattern, replacing characters by
suitable homomorphisms, etc. (also see Delsarte [78], [79] ).
The original proof in Lloyd [44] reduced the counting argument
to a differential equation. The necessary condition for the existence
of a binary perfect e-error-correcting code then amounted to the van-
ishing of e of the coefficients of (1 + x)
e(l — x)
n~
1~
e, expanded as a
polynomial. Roos [57] proved the same formulation of Lloyd's
theorem for q = p in a purely algebraic way. The proof also depends
on the idea of averaging over all translations of the code which is the
basis of the proof we have sketched.

7. Nonexistence theorems. Although Lloyd [44] treated a few
examples in his paper he did not use his theorem to prove the non-
existence of classes of perfect codes and the theorem remained un-
used for several years. Johnson [31] used Lloyd's theorem to give
an alternate proof for the cases q = 2, e = 2 or 3 which had been
settled by number theory methods (see § 5). In retrospect it is remark-
able to see how simple the general treatment of e = 2 and e = 3,
with no restriction on q, turned out to be. The proof for e = 2 (van
Lint [39] ) uses the sphere-packing condition and Lloyd's theorem

A SURVEY OF PERFECT CODES  215

and the simple observation that Qe(0) is the left-hand side of (5.2),
(cf. (6.5)). With this information on the product of the zeros of the
quadratic polynomial Ç>2{x) it took only one page to show that there
are no perfect 2-error-correcting codes with q = p
a > 3, n > 2. The
proof that the Golay code is the only nontrivial perfect 3-error-
correcting code was even simpler. Two consecutive integers were
found for which Q3(x) had different signs!
The method used for e = 2 depended on solving the quadratic
equation Q2(x) = 0. Of course this method did not look promising
for e > 3. In fact only e = 4 looked feasible. The first nonexistence
proof for the case q = 2, e = 4 was (unnecessarily) extremely compli-
cated. In this proof (van Lint [42] ) the equation Q4(x) = 0 was
solved explicitly. Lloyd's theorem then led to the condition that
(n — 1) ± (3n — 7 ± V6n 2 - 30n + 40) m is an even integer for all
four choices of signs. The resulting set of diophantine equations was
treated by using a method which had just been developed by Baker
and Davenport [11]. This involved two hours computing time on
ATLAS I. Although this was interesting as a second application of
this method of Baker and Davenport this author soon realized that
instead of using only Lloyd's theorem as he had done, the proof for
e = 4 should also have exploited the connection between (5.2) and
(6.5) as was done for e = 2 and e = 3. For e = 4 this connection
implies that Ç^O) is a power of 2 and since the product of the zeros
of Q4{x) is 3Q4(0)/2 three of the zeros of Q4(x) are powers of 2. This
observation led to a proof in a few lines (van Lint [38] ) that there
are no non trivial binary perfect 4-error-correcting codes.
At this point the idea which would lead to the proof that all perfect
codes over finite fields are known had been born. The idea, men-
tioned above in the case q = 2, e = 4 was generalized by this author
(van Lint [43] ) to all q and p > e. Simultaneously Tietäväinen [66]
observed that the method used by van Lint [39] for e = 2 and
e = 3 could be generalized to e = 4, i.e., the restriction q = 2 which
we used above is unnecessary.
Actually the whole idea of the nonexistence proofs is extremely
simple. We have already remarked that Qe(0) is equal to the left-
hand side of (5.2) and hence a power of q. By calculating the first
two coefficients of Qe(x), we then know the sum and the product of
the zeros of this polynomial:

(7,, , | + %+ .. . + ;f,= '("-^-'>  + ife±i),
q *

(7.2) xxx2 • ' * xe = e\q
k~
e.

216  J. H. VAN LINT

Using the alternating character of the expression (6.5) a lower bound
for the zeros of Qe(x) can be obtained. Combined with a relatively
simple divisibility argument this was sufficient to prove the following
theorem.

THEOREM (7.3). If e ^ 3, q = p
a
y p > e then there is no nontrivial
perfect e-error-correcting code over GF(q).

For details we refer to van Lint [41], [43]. This method also
works for p < e if p^e. For fixed e the theorem leaves only a finite
number of values of p to be considered. These can all be treated by
exactly the same method (and a little more care) as was shown in van
Lint [40] fore = 5,6 and 7.
To complete the nonexistence theorems a refinement was neces-
sary. This was provided by Tietäväinen [67], [68]. The first new
trick is an elegant application of a refined arithmetic-geometric mean
inequality to (7.1) and (7.2). The second is the observation that (7.2)
implies that for p â ey there is at least one pair of zeros xi9 Xj with
XilXj = p
v, which is not difficult to prove. Finally small values of
n are excluded by the Elias bound (cf. Berlekamp [12] ch. 13).
These ideas combined with a skillful treatment of several inequalities
led to the following theorem:

THEOREM (7.4). If e ^ 4, q = p
a, p ^ e then there is no nontrivial
perfect e-error-correcting code over GF(q).

For details we refer to Tietäväinen [68]. Clearly (7.3) and (7.4)
completely settle the problem of the existence of perfect codes over
finite fields. In §6 we mentioned that Lenstra [35] had shown
Lloyd's theorem to be true for all q. The reason this has not led to
new nonexistence theorems yet is the fact that if q is not a power of
a prime then (5.2) must be replaced by (5.1) and (7.2) is no longer as
useful. (See Comments (9.2) and (9.3)!)

8. Generalizations. In § 1 we introduced the Lee-metric (1.11, 1.12)
(cf. Lee [34] ). For this metric one can again study perfect codes and
ask the same questions which have been treated for the Hamming
metric. Very little is known about perfect codes for this metric. We
mention:

THEOREM (8.1). For any given t, there exists a perfect t-Lee-error-
correcting code of block length n = 2 over the alphabet of integers
mod q = 2t
2 + 2t + 1 (cf. Berlekamp [12], ch. 13).

Golomb and Welch [26] conjectured that for t > 1, n > 2 and
q > 3 there are no perfect Lee-error-correcting codes. They treated

A SURVEY OF PERFECT CODES  217

a number of special cases (namely n = 3, t = 2, and n > 2, t > tn) but
essentially the problem is still completely open.
Clearly the sphere-packing condition for the Lee metric is obtained
in the same way as (5.1) namely by calculating |S(0, e)\ for the Lee
metric. The result is

(8.2) S2'(î)(|)| 9 » (t^(q-l)l2)
t=0

where t is the number of errors. In § 5 we saw that the sphere-
packing bound alone has led to only a few nonexistence theorems. In
fact it was only the combination with Lloyd's theorem which led to
success. So we have

PROBLEM (8.3). Is there an analog of Lloyd's theorem for perfect
codes in the Lee metric? (See Comment (9.4)!)

The problem of sphere-packing with no gaps using a metric which
is a combination of the Hamming and Lee metrics also occurs in a
paper by S. K. Stein [63]. His results are similar to those of Golomb
and Welch. (Also see Stein [90], [91] ).
Herzog and Schonheim [29] have generalized the idea on which
Hamming codes are based to construct perfect codes for J? : = Fx X
F2 X • • • X F n where each Ft is a field and Hamming metric is de-
fined as in (1.2). Let the abelian group G be the union of n subgroups
Gi, G2, • • •, Gn which pairwise have only the zero element of G in
common. Then (xi9 x2, ' * •, xn)—> *i + *2 + * * * +
 xn *
s a homo-
morphism of <R : = Gl X G2 X • • • X Gn into G. The kernel of this
homomorphism is a group code in <R. It is easily seen that this code is
single-error-correcting. This is the idea used in § 2 where AG(ra, q)
was written as the union of all lines through the origin. Herzog and
Schonheim give an example of a perfect code in GF(4) X GF(2) X
GF(2) X GF(2) X GF(2), namely

(0,0,0,0,0) (1,0,1,1,0)

08,1,1,0,0) («,0,1,0,1)

(a,l,0,l,0 ) (A 0,0,1,1)

(1,1,0,0,1) (0,1,1,1,1),

where {0,1, o,ß} = GF(4). We remark that in this example each
element of GF(4) is followed by a complementary pair of words of a
Hadamard code (cf. Peterson [53], § 5.7 and also [83], [86] ).

218  J. H. VAN LINT

Let S*(0, e) be a subset of Ji
(n) with

(8.5) S(0, e) C S*(0, e) C S*(0, e + 1)

(where inclusions are strict). If an e-error-correcting code C has the
property

(8.6) *#<»>= U (x+S*(0, 4 a disjoint union,

then the code C is called quasiperfect. This generalizes (1.8). Such
codes can be obtained, e.g., by dropping certain coordinates from all
words of a Hamming code. There are very many quasiperfect codes.
Apparently (8.6) is so much less restrictive than (1.8) that the result-
ing codes do not have such interesting properties. For a number of
results we refer to Peterson [53], Wagner [70], [71], [94].
Recently Goethals and Snover [21] introduced the concept of
nearly perfect code. Johnson [32] proved that for a binary code
C of length n and minimum distance 2e + 1 the following bound for
the number of codewords holds

(8.7)|C|{Ì(ì)+ r-^(e)(—-[—])}^*
n-

Note that for a binary perfect code we have (e + 1) \(n — e) by (4.3)
and that equality holds in (8.7) (cf. (5.1), (5.2)). Now any code for
which equality holds in (8.7) is called nearly perfect. This includes
the perfect codes and the shortened Hamming codes and also the
Preparata 2-error-correcting codes (Preparata [55] ). Many of the
properties of perfect codes discussed in this survey were generalized
to nearly perfect codes by Goethals and Snover, e.g., theorem (4.2),
(5.2) and Lloyd's theorem. We mention one example of such a gen-
eralization of (4.2).

THEOREM (8.8). In any nearly perfect e-error-correcting code of
length n, the codevectors at distance d = 2e + 1 from a given co-
devector determine an e-design with parameters [(n — e)l(e + 1)] ;
(e9d,n). (cf. (4.1)).

The generalization of Lloyd's theorem is

THEOREM (8.9). If a nearly perfect binary e-error-correcting code
of block length n, with n + 1 ^p 0 (mod e + 1), exists, then

e- w + [(„-ny(g+i)]^^>-g-'W>

has e + 1 distinct integral zeros among 1,2, • • -, n.

A SURVEY OF PERFECT CODES  219

Of course this raises:

PROBLEM (8.10). Generalize (7.3) and (7.4) to nearly perfect codes.

The combinatorial theorems of which (8.8) is an example combined
with the conjecture that there is no nontrivial 6-design justify the con-
jecture that all the nearly perfect codes are known. Similar results to
those of Goethals and Snover were found independently by Semakov,
Zinovjev and Zaitzev [60] in a paper on uniformly packed codes,
a special type of quasiperfect codes. (See Comment (9.5)!)
In § 6 we mentioned that the e distinct integral zeros of Qe(x) in the
case of a linear perfect code are exactly the distinct nonzero weights
occurring in the dual code. This led Delsarte [18] to a generaliza-
tion of the duals of perfect codes by considering codes with e distinct
nonzero weights satisfying equality in a certain bound on the number
of codewords. Besides the duals of perfect codes he found other
examples. The most interesting fact from our point of view is that a
generalization of Lloyd's theorem again holds. (See Comment (9.6)!)
It seems that in this area of combinatorics many more interesting
results are to be expected. It is the hope of this author that the
present survey will prevent unnecessary duplication of research and
enable the interested readers to work on those problems which are
open at this moment.

9. Comments (added in proof). In accordance with the last sen-
tence of § 8 we add some comments on papers which appeared since
the manuscript of this survey was submitted. We have added 23
references to the original list. Some of these are older papers of which
this author was not aware. For drawing his attention to these papers
and for several helpful suggestions concerning small changes in the
survey the author wishes to thank many of the persons mentioned in
the references.

COMMENT (9.1). In Theorem (3.5) linearity of the codes is assumed.
In the meantime it has been shown by Snover [89] and by Delsarte
and Goethals [80] that Theorem (3.5) holds even if linearity is not
assumed.

COMMENT (9.2). Shortly after Tietäväinen, a proof very similar to
his proof was found independently by V. A. Zinov'ev and V. K. Leont'ev
[85], [95], [96].

COMMENT (9.3). Recently Tietäväinen [92] produced a non-
existence proof for perfect codes which is much shorter than his
original proof. He excludes q = 2. In van Lint [87] it is shown that

220  J. H. VAN LINT

a slight modification makes the proof valid for q = 2. This paper also
includes some information on the nonexistence of perfect codes when
q is not a prime power.

COMMENT (9.4). The answer to Problem (8.3) is yes. A proof was
recently provided by L. A. Bassalygo [74].

COMMENT (9.5). The original idea of uniformly packed codes has
been generalized even further; cf. Bassalygo, Zaitzev and Zinov'ev
[75]. Recently Goethals and van Tilborg have found a number of
interesting sequences of uniformly packed codes. Their paper is in
preparation. Also see van Lint [ 87].

COMMENT (9.6). A very interesting generalization of perfect codes
in R(n) is the concept of a perfect code in a graph as defined by
Biggs [76], [77]. Also see Heden [82], Hammond and Smith
[88]. A general theory containing nearly all the concepts treated
in this survey is the theory of association schemes in coding theory.
This was developed by Delsarte [78], [79]. Both of these papers
are highly recommended to those readers who wish to gain more in-
sight into the theory of perfect codes.

REFERENCES

1. R. Alter, On the Nonexistence of Close-Packed Double Hamming-Error -
Correcting Codes on q = 7 Symbols, J. Comp. Syst. Sci. 2 (1968), 169-176.
2. , On the Nonexistence of Perfect Double Hamming-Error-Correcting
Codes onq = Sandq = 9 Symbols, Inf. and Control 13 (1968), 619-627.
3. , On a Diophantine Equation Related to Perfect Codes, Math, of
Comp. 25 (1971), 621-624.
4. E. F. Assmus Jr. and H. F. Mattson, Perfect Codes and the Mathieu Groups,
Archiv d. Math. 17 (1966), 121-135.
5. , Cyclic Codes, Report AFCRL-66-348 of the Applied Research Lab-
oratory of Sylvania Electronic Systems, Waltham, Mass. (1966).
6. , On the number of Inequivalent Steiner Triple Systems, J. Comb.
Theory 1 (1966), 301-305.
7. , A simple construction of the binary Golay code, Report AFCRL-67-
0365 of the Applied Research Laboratory of Sylvania Electronic Systems, part
VI (1967).
8. , On Tactical Configurations and Error-Correcting Codes, J. Comb.
Theory 2 (1967), 243-257.
9. , New 5-Designs, J. Comb. Theory 6 (1969), 122-151.
10. , Algebraic Theory of Codes II, Report AFCRL-69-0461 of the
Applied Research Laboratory of Sylvania Electronic Systems (1969).
11. A. Baker and H. Davenport, The equations 3x
2 — 2 = y
2 and Sx
2 — 7 = z
2,
Quart. J. of Math. 20 (1968), 129-137.

A SURVEY OF PERFECT CODES  221

12. E. R. Berlekamp, Algebraic Coding Theory, McGraw-Hill Book Comp.,
New York (1968).
13. E. R. Berlekamp, J. H. van Lint and J. J. Seidel, A strongly regular graph
derived from the perfect ternary Golay Code, in J. N. Sri vasta va (ed.), A Survey of
Combinatorial Theory, North Holland Pubi. Comp., Amsterdam (1973).
14. R. T. Chien, On Golay s perfect codes and step by step decoding, IEEE
Trans. Inform. Theory IT 12 (1966), 403-404.
15. J. Cocke, Lossless symbol coding with nonprimes, IEEE Trans. Inform.
Theory, 5 (1959), 33-34.
16. E. L. Cohen, A Note on Perfect Double Error-Correcting Codes on q Sym-
bols, Inf. and Control 7 (1964), 381-384.
17. P. Delsarte, Linear programming associated with coding theory, Report
R 182 of MBLE Research Laboratory, Bruxelles, Belgium (1971).
18. , Four fundamental parameters of a code, Report R 184 of MBLE
Research Laboratory, Bruxelles, Belgium (1972).
19. C. Engelman, On Close-Packed Double Error-Correcting Codes on P Sym-
bols, IRE Trans-Inform. Theory 7 (1961), 51-52.
20. J.-M. Goethals, On the Golay Perfect Binary Code, J. Comb. Theory 11
(1971), 178-186.
21. J.-M. Goethals and S. L. Snover, Nearly Perfect Binary Codes, Discrete
Math. 3 (1972), 65-88.
22. M. J. E. Golay, Notes on Digital Coding, Proc. IRE 37 (1949), 657.
23. , Binary Coding, IEEE Trans. Inform. Theory IT 4 (1954), 23-28.
24. , Notes on the Penny-Weighing Problem, Lossless Symbol Coding
with Nonprimes, etc., IEEE Trans. Inform. Theory, IT 4 (1958), 103-109.
25. S. W. Golomb and E. C. Posner, Rook Domains, Latin Squares, Affine
Planes, and Error-Correcting Codes, IEEE Trans. Inform. Theory IT 10 (1964),
196-208.
26. S. W. Golomb and L. R. Welch, Algebraic Coding and the Lee Metric,
p. 175-194 of H. B. Mann, Error-Correcting Codes, John Wiley & Sons, Inc.,
New York (1968).
27. M. Hall Jr., Combinatorial Theory, Blaisdell Publishing Company, Waltham,
Mass. (1967).
28. R. W. Hamming, Error-Detecting and Error-Correcting Codes, Bell System
Tech. J. 29 (1950), 147-160.
29. M. Herzog and J. Schonheim, Linear and Nonlinear Single-Error-Correcting
Perfect Mixed Codes, Inf. and Control 18 (1971), 364-368.
30. L. O. James, R. G. Stanton and D. D. Cowan, A Problem in Coding Theory,
Proc. Louisiana Conf. on Combinatorics, Graph Theory and Computing (1970),
167-179 (Louisiana State Univ., Baton Rouge, Lo.).
31. S. M. Johnson, On Perfect Error-Correcting Codes, Memorandum RM-
3403-PR of the Rand Corporation, Santa Monica, Cal. (1962).
32. , A New Upper bound for Error-Correcting Codes, IEEE Trans.
Inform. Theory, IT 8 (1962), 203-207.
33. M. Karlin, New Binary Coding Results by Circulants, IEEE Trans. Inform.
Theory IT 15 (1969), 81-92.
34. C. Y. Lee, Some Properties of Nonbinary Error-Correcting Codes, IEEE
Trans. Inform. Theory IT 4 (1958), 77-82.
35. H. W. Lenstra Jr., Two theorems on perfect codes, Discrete Math. 3 (1972),
125-132.

222  J . H. VAN LINT

36. V. K. Leont'ev, On a Problem of Close-Packed Codes (in Russian), Diskret.
Analiz 2 (1964) 56-58.
37. B. Lindström, On group and nongroup perfect codes in q symbols, Math.
Scand. 25 (1969), 149-158.
38. J. H. van Lint, 1967-1969 Report of the Discrete Mathematics group, Re-
port 69-WSK-04 of the Technological University, Eindhoven, Netherlands (1969).
39. , On the Nonexistence of Perfect 2- and 2-Hamming-Error-Correcting
Codes over GF(q), Inf. and Control 16 (1970), 396-401.
40. , On the Nonexistence of Perfect 5-, 6- and 7- Hamming-Error-Cor-
recting Codes over GF(q), Report 70-WSK-06 of the Technological University,
Eindhoven, Netherlands (1970).
41. , Coding Theory, Springer Verlag, Berlin-Heidelberg, New York (1971).
42. , On the Nonexistence of Certain Perfect Codes, Computers in Number
Theory 277-282, Academic Press, London and New York (1971).
43. , Nonexistence Theorems for Perfect Error-Correcting-Codes, Com-
puters in Algebra and Number Theory 89-95, SIAM-AMS Proceedings IV (1971).
44. S. P. Lloyd, Binary Block Coding, Bell System Tech. J. 36 (1957), 517-535.
45. G. Losey, Note on a Theorem of Zaremba, J. Comb. Theory 6 (1969), 208 -
209.
46. F. J. MacWilliams, Ph. D. Dissertation, Harvard University (1961).
47. , An Historical Survey, p. 3-13 of H. B. Mann, Error-Correcting Codes,
John Wiley & Sons, Inc., New York (1968).
48. H. B. Mann, Error-Correcting Codes, John Wiley & Sons, Inc., New York
(1968).
49. J. G. Mauldon, Covering Theorems for Groups, Quart. J. Math. 1 (1950),
284-287.
50. M. H. McAndrew, An Algorithm for Solving a Polynomic Congruence and
its Application to Error-Correcting Codes, Math, of Comp. 19 (1965), 68-72.
51. A. W. Nordstrom and J. P. Robinson, An Optimum Nonlinear Code, Inform,
and Control 11 (1967), 613-616.
52. L. J. Paige, A Note on the Mathieu Groups, Can. J. Math. 9 (1956), 15-18.
53. W. W. Peterson, Error-Correcting Codes, The M. I. T. Press, Cambridge,
Mass. (1961).
54. V. Pless, On the uniqueness of the Golay codes, J. Comb. Theory 5 (1968),
215-228.
55. F. P. Preparata, A Class of Optimum Nonlinear Double-Error-Correcting
Codes, Inform, and Control 13 (1968), 378-400.
56. , A new look at the Golay (23, 12) code, IEEE Trans. Inform. Theory
IT 16 (1970), 510-511.
57. J. E. Roos, An Algebraic Study of Group and Nongroup Error-Correcting
Codes, Inform, and Control 8 (1965), 195-214.
58. J. Schönheim, On linear and nonlinear single-error-correcting q-nary per-
fect codes, Inf. and Control 12 (1968), 23-26.
59. , Semilinear Codes and some Combinatorial Applications of Them,
Inf. and Control 15 (1969), 61-66.
60. N. V. Semakov, N. A. Zinovjev and G. V. Zaitzev, Uniformly Packed Codes
(in Russian), Problemy Peredachi Informatsii 7 (1971), 38-50.
61. H. S. Shapiro and D. S. Slotnick, On the Mathematical Theory of Error-
Correcting Codes, IBM J. Res. Develop. 3 (1959), 25-34.
62. R. G. Stanton, Covering theorems in groups (or: How to win at football
pools), Recent Progress in Combinatorics (Proc. Third Waterloo Conf. on Combina-

A SURVEY OF PERFECT CODES  223

tories) 37-45, Academic Press, New York (1969).
63. S. K. Stein, Factoring by Subsets, Pac. J. Math. 22 (1967), 523-541.
64. G. Szegö, Orthogonal Polynomials, Am. Math. Soc. Coll. Pubi. 23 (1959).
65. O. Taussky and J. Todd, Covering Theorems for Groups, Ann. Soc. Polon.
Math. 2 (1948), 303-305.
66. A. Tietäväinen, On the Nonexistence of Perfect 4-Hamming-Error-Correct-
ing Codes, Ann. Ac. Sci. Fennicae Ser. A. I (1970), 485.
67. —— , On the Nonexistence of Perfect Codes over Finite Fields, SIAM J.
Appi. Math. 24 (1973), 88-96.
68. A. Tietäväinen and A. Perko, There are No Unknown Perfect Binary Codes,
Ann. Univ. Turku, Ser. A. I (1971), 148.
69. Ju. L. Vasil'ev, On nongroup close-packed codes (in Russian), Probi. Kib-
ernet 8 (1962), 337-339, translated in Probleme der Kybernetik 8 (1965), 375-378.
70. T. J. Wagner, A Search Technique for Quasi-Perfect Codes, Inf. and Con-
trol 9 (1966), 94-99.
71. 9 A Remark Concerning the Existence of Binary Quasi-Perfect Codes,
IEEE Trans. Inform. Theory IT 12 (1966), 401.
72. S. K. Zaremba, A Covering Theorem for Abelian Groups, J. London Math.
Soc. 26 (1950), 71-72.
73. , Covering problems concerning Abelian Groups, J. London Math Soc.
27 (1952), 242-246.
74. L. A. Bassalygo, A Necessary condition for the Existence of Perfect Codes
in the Lee Metric (in Russian), Matematicheski Zametki 15 (1974), 313-320.
75. L. A. Bassalygo, G. V. Zaitzev, N. A. Zinov'ev, On Uniformly Packed
Codes (in Russian), Problemy Peredachi Informatsii (1974), 9-14.
76. N. L. Biggs, Perfect Codes in Graphs, J. Comb. Theory B 15 (1973),
289-296.
77. , Perfect Codes and Distance Transitive Graphs, in Combinatorics,
Proc. of the Third British Comb. Conf., Aberystwyth 1973, London Math. Soc.
Lecture Notes 13 (F. P. McDonough and V. C. Mavron, eds.).
78. P. Delsarte, An Algebraic Approach to the Association Schemes of
Coding Theory, Philips Res. Repts. Suppl. 10 (1973).
79. , The Association Schemes of Coding Theory, p. 139-157 in Com-
binatorics (M. Hall and J. H. van Lint, eds.), Mathematical Centre Tracts 55,
Amsterdam, 1974.
80. P. Delsarte and J.-M. Goethals, Unrestricted Codes with the Golay
Parameters are Unique, Report R 238, M.B.L.E. Research Laboratory, Brussels,
1973.
81. S. W. Golomb and L. R. Welch, Perfect Codes in the Lee Metric and
the Packing of Polyominoes, SIAM J. Appi. Math. 18 (1970), 302-317.
82. O. Heden, Perfect Codes in Antipodal Distance-Transitiv e Graphs, Math.
Institute of the Univ. of Stockholm preprint (1974).
83. M. Herzog and J. Schönheim, Group Partition, Factorization and the
Vector Covering Problem, Can. Math. Bull. 15 (1972), 207-214.
84. S. M. Johnson, A New Lower Bound for Coverings by Rook Domains,
Utilitas Math. 1 (1972), 121-140.
85. V. K. Leont'ev, On the Existence of Densely Packed Codes (in Rus-
sian), Problemy Kibernet. 15 (1965), 253-257.
86. B. Lindström, Group Partitions and Mixed Perfect Codes, Can. Math.
Bull, (to appear).
87. J. H. van Lint, Recent Results on Perfect Codes and Related Topics,

224  J. H. VAN LINT

p. 158-178 in Combinatorics (M. Hall and J. H. van Lint, eds.) Mathematical
Centre Tracts 55, Amsterdam, 1974.
88. D. H. Smith and P. Hammond, Perfect Codes in the Graphs 0^, J. Comb.
Theory (to appear).
89. S. L. Snover, The Uniqueness of the Nordstrom-Robinson and the Golay
Binary Codes, thesis, Michigan State Univ., 1973.
90. S. K. Stein, A Symmetric Star Body that Tiles but not as a Lattice, Proc.
Am. Math. Soc. 36 (1972), 543-548.
91. , Algebraic Tiling, Am. Math. Monthly 81 (1974), 445-462.
92. A. Tietäväinen, A Short Proof for the Nonexistence of Unknown Perfect
Codes over GF(q), q > 2, Ann. Acad. Sci. Fennicae A 580 (1974).
93. J. A. Todd, A Representation of the Mathieu Group M24 as a Collinea-
tion Group, Ann. di Mat. (IV) 71 (1966), 199-238.
94. T. J. Wagner, Some Additional Quasi-Perfect Codes, Inf. and Control
10 (1967), 334.
95. V. A. Zinov'ev and V. K. Leont'ev, On Perfect Codes (in Russian), Prob-
lemy Peredachi Informatsii 8 (1972), 26-35.
96. , A Theorem on the Nonexistence of Perfect Codes over Finite
Fields (in Russian), Probiemy Peredachii Informatsii (to appear).

TECHNICAL UNIVERSITY EINDHOVEN, EINDHOVEN, NETHERLANDS
