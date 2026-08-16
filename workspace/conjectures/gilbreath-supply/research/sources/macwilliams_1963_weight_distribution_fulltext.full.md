<!-- source: https://user.eng.umd.edu/~abarg/ECC/macwilliams1963.pdf | converted from PDF -->

A Theorem on the Distribution of Weights
in a Systematic Codet

By JESSIE MACWILLIAMS

(Manuscript received September 4, 1962)

A systematic code of word length n is a subspace of the vector space of all
possible rows of n symbols chosen from a finite field. The weight of a vector
is the number of its nonzero coordinates; clearly any given code contains a
certain finite number of vectors of each weight from zero to n. This set of
integers is called the spectrum of the code, and very little is known about it,
although it appears to be important both mathematically and as a practical
means of evaluating the error-detecting properties of the code.
In this paper it is shown that the spectrum of a systematic code deter-
mines uniquely the spectrum. of its dual code (the orthogonal vector space).
In fact the two sets of integers are related by a system of linear equations.
Consequently there is a set of conditions which m1lst be satisfied by the
weights which actually occur in a systematic code. If there is enough other
information about the code, it is possible to use this result to calculate its
spectrum.

In most systems of error correction by binary or multiple level codes
the minimum distance between two code words is an important parame-
ter. (The distance between two code words is the number of coordinate
places in which they differ.) Much attention has been given to devising
codes which have an assigned minimum distance.
The weight of a code word is its distance from the origin. The distance
between two code words is the weight of the vector obtained by sub-
tracting one from the other, coordinate by coordinate. If the code words
form a vector space, this vector is itself a member of the code. Such codes
are called systematic codes. The set of integers specifying the weight of
each code word is then exactly the same collection of numbers as the set
of integers specifying the distance between each pair of code words.

t This paper formed part of a thesis presented to the Department of Mathe-
matics, Harvard University, in partial fulfillment of the requirements for the
degree of Doctor of Philosophy.
 79

80 THE BELL SYSTEM TECHNICAL JOURNAL, JANUARY 1963

Thus it is customary to talk about weight properties rather than distance
properties of systematic codes.
In many cases, practically all that is known explicitly about the
distribution of weights in a code is that the weight hasa certain minimum
value. Recent studies have shown that it would be useful (e.g., in the
study of real life channels) to have more information. We would like to
be able to answer questions of the following sort:

i. Given a method (implemented or theoretical) for constructing a
systematic code, how many elements of each weight will be obtained?
(It is a safe assumption that nobody will want to write out the code
vectors and count them.)

ii. Given a set, Ul , U2, ..• , Us , of positive integers, is it possible to
construct a systematic code with elements of these weights only?

In theory there exists a method of answering these questions.1 •
2 •
3 Un-
fortunately this method is quite difficult to apply. The purpose of this
paper is to give a different method which is in some ways more useful.
We show that the spectrum of a systematic code determines uniquely
the spectrum of the dual code (the orthogonal vector space). In fact,
the two sets of integers are related by a system of linear equations. Our
main theorem shows how to obtain this system of equations.
In Section I we give definitions and statements of the main theorem
and of some corollaries. Section II contains proofs of these theorems.
Section III describes how the results of Section I may be applied.

I. DEFINITIONS, NOTATION AND A STATEMENT OF THE MAIN THEOREM

Let F be a finite field of q elements; q is a prime power. Let Fn denote
the direct sum of n copies of F. F" is the set of all possible row vectors
of length n, in which each coordinate is an element of F. Addition of two
vectors is defined coordinate by coordinate, under the rules prevailing
inFo
F" is a vector space of dimension novel' F. Choose a basis consisting
of the n vectors
 El = (1,0,0, ,0)

E2 = (0, 1,0, ,0)

En = (0,0,0, ... , 1).

An element U of F" is then expressed uniquely as

WEIGHTS IN A SYSTEMATIC CODE 81

n
U = LUi E i,
i=l Ui E F.

We write U = (Ul, U2, .•• , Un).
The weight of U is defined to be the number of Ui which actually ap-
pear in this sum - i.e., the number of nonzero coordinates in the vector
u. An alphabet is any subspace of F" j a vector belonging to the alphabet
a is called a letter of a. It may happen that every letter of a has zero as
the jth coordinate - this case is not excluded.
The scalar product of two vectors,

11. n
U = L UiEi, IJ = L ViEi ,
i-l i-l Ui, Vi E F,

is u*v = Li~l UiVi, where the multiplication and addition are carried out
in F. If F is the field of two elements 0, 1, for example, the scalar product
of (1, 1, 0) with itself is 1·1 + 1·1 = O.
Two vectors u, v are orthogonal if their scalar product is zero. In the
example above, (1, 1,0) is orthogonal to itself.
The orthogonal complement of an alphabet a is the set of all vectors
of F" which are orthogonal to every vector of a. It is clear that these
vectors also form an alphabet, say CB, which is called the dual alphabet
of a. If 11: is the dimension of a, the dimension of CB is m = n - k.
The main result of this paper is as follows (the proof is given in Section
II) :
Let a be an alphabet of dimension k, and CB the dual alphabet of di-
mension m. Let Ai , B, denote the number of letters of weight i in a, CB
respectively. Of course, Ao = Bo = 1. Set v = q - 1. Let z be an in-
determinate.
Theorem1: The quantitiesdefined above are related by theequation

n n
L Ai( l + 'Yz) n- i( l - Z)i = l L Bii.
i=O i=O

Remarks:
i. The formula above is symmetric in the sense that, setting (1 - z) /
(1 +,¥z) = Z, we obtain by straightforward algebra

n n
L B i(l + ,¥z)n-i(l - Z)i = qm L Aiz i •
i=O ic=O

ii. Theorem 1 is a statement about equivalent elassesj'" it is still
true if a, CB are replaced by equivalent alphabets.
An alphabet a is said to be decomposable,':' with respect to the basis

82 THE BELL SYSTEM TECHNICAL JOURNAL, JANUARY 1963

El, E2, ••• , En of F", if it is the direct sum of two alphabetsai, ~,
whereat containsn columns of zeros and~ occupies these columns only.
For example, thealphabet
 0 0 0 0
1 1 0 0
0 0 1 1
1 1 1 1

is decomposable,with

0 0 0 0 0 0 0 0
a1 = 1 1 0 0 a2 = 0 1 1.0

In general, al is a k1-dimensional alphabetin E'" and ~ a /C2-dimen-
sional alphabetin F n2, with nl + ~ = n, k) + /C2 = k, k1 ~ nl, k2 ~ n2.
The dualalphabetof a decomposablealphabetis also decomposable;
in fact 03 = 031 + 032 , where O3i is the dual alphabetof ai in F"! i =
1, 2. (The example above is self-dual.)
CaroUa1"y 1.1: If a is decomposable, say a = al + a2, the equation

n
~ A i ( 1 + ,¥z)n-i(1 - Z)i = l ~ Bii

-ill!!!!!!lO

is reducible in the obvious sense;the factors arethe equationspertain-
ing to ai, (B. in F n " i = 1, 2.
For the example above we have

[(1 + Z)4 + (1 - Z)2]2 = 2\1 + Z2)2.

Carolla1"y 1.2: A necessary condition forthe existence of an alphabet
containingletters of weights Wi , i = 1, 2, '" , s, and no other, isthat
there exists a set of integersai, i = 1, 2, '" , s, suchthatthe expres-
sion .
(1 + ,¥z)n+ '¥ ~ a.(l + ,¥z)n-w'(1 _ z)W',
;=1

when expanded in powers ofz, takes the form

n
qk + '¥l ~ {3;Z"
i-I

where the {3i are positive integers.
Unfortunately,this condition is not sufficient. For example,

(1 + Z)8+ 7(1 + Z)6(l - Z)2 + 7(1 + z)2(1 - Z)6+ (1 - Z)8

= 2\1 + 7z
2 + 7z
6 + i),

WEIGHTS IN A SYSTEMATIC CODE 83

but it is not possible to construct a binary alphabet containing 7 letters
of weight 2 and no letters of weight 4.
IfAl = A 2 = ... = A 2; = 0, every vector of weight ~j in F" appears
as a coset leader for a, and conversely. Another way of saying this is
that, for all pairs of distinct letters a, a', of a and any i ~ j, the set of
vectors at distance i from a is disjoint from the set of vectors at distance
i from a'. In this case we can enumerate these vectors by weights as
follows:
Let i., denote the number of vectors of weight 8 in F" which are at
distance i from some letter of a. Write
 n
(1 + 'Yz)n-;(l - z); = L'lt(i,j)z;
i-O

Corollary 1.3: If a contains no letter of weight < 2j + 1, then

n n
Lf.,ix· = L B;'lt(i,j)(l + 'Yx)n-'(l - x)i.
B-1 i=O

The proofs of corollaries 1.1 to 1.3 are given in Section II.

II. PROOFS

If a is an alphabet of F" and (B the orthogonal complement of a, the
weights of the letters of (B are, of course, uniquely determined by the
letters of A. However, a much stronger statement can be made: the set
of integers specifying the number of letters of each weight in (B is related
by a system of linear equations to the set of integers similarly defined for
G.. This section will consist of proofs of this statement and of some of
its consequences.
Two proofs are given. The first is short and easy; the second is longer
and more sophisticated. However, it incidentally produces a more gen-
eral result and gives some insight into what is going on.
We make the following conventions for notation: a shall be a k-di-
mensional alphabet in F" j (B shall be the orthogonal complement of a
of dimension m = n - kj'Y shall denote the quantity q - 1. Ai, B,
denote the number of letters of weight i in a, (B respectively. The bi-

nomial coefficient (:) is understood to be zero if 8 > r.

Let lO1, lO2, ••• , lOn be the usual basis of F n • Let 8 = (81,82, ••• , 8.)
be a set of p different indices, 1 ~ 8; ~ n, and let t = (t1 , ~, ••• , tn-.)
be the complementary set of indices. Denote by F:, Ft-· the spaces
generated by lO8 1 , ••• , lO•• and lOll' ••• , lOln_•• Clearly, F:, rt:: are
orthogonal complements in E", Let IH Istand for the number of vectors
in a space H.

84 THE BELL SYSTEM TECHNICAL JOURNAL, JANUARY 1963

Lemma 2.0: Ian F t n
- v I = r: Iill n F'-I.

Proof: The orthogonal complement of a n F tn-vis the smallest space
containing ill and F.-. This is the lattice theoretic union of ill and F:,
which we write ill U F:. Then
IillUF'-I· Ian FIn-vI = qn = qm+k.

The number of vectors in ill U F'- is qmqvIIill n F'-I.
Hence

or Ian Ft-VI = l-v Iill n F'-I.

Denote by {( EsI, ••• , Es.), a} a pair consisting of II basis vectors of
F" and a vector a of a which is orthogonal to each of ESI , ••• , Es••
Lemma2.1:
i. For a fixed set of indicesSI, ••• , s, the number of pairs

{(EsI, ••• ,Es,), aj is Ian Ft- V I.

ii. The total number of such pairs for aUchoices of II distinct basis
. "n A (n- i)vectors ~8 £."i=D ill'

Proof:
i. F tn- v consists of exactly those vectors of E" which are orthogonal
to ESI , ••• , Esv ; hence a n Ft- V consists of exactly those vectors of a
which are orthogonal to ESI , '" , Es••
ii. If a E a is of weight i, then a is orthogonal to n - i of the vectors
er , "', En. A set of II vectors may be chosen from these n - i in
(n~i) ways. Hence the total number of pairs

{(ES1' "', lOs.), a} is :t Ai (n - i).
i=O J1

Let Ls indicate summation over all possible choices of 11 indices
81, ... , 8.; similarly, Lt denotes summation over all the comple-
mentary sets t1 , ••• , tn-v' Lemma 2.1 is equivalent to
L Ia n Ft-'I = t Ai (n- i).
t i=O II

WEIGHTS IN A SYSTEMATIC CODE 85

Replace G. by CB, P by n - P and s by t. The same argument then gives

:E ICB n F: I = t e. (n- i).

8 ;=0 n - v

Lemma2.2

Proof: For a fixed set s (which determines, of course, a fixed set t)
we have by 2.0

Thus :E I G. nF/-vI = qk-v:EICB nF'-I,
I 8

which, by 2.1 is the same thing as
t Ai (n- i) = r:t B; (n- i).
;=0 v ;=0 n - v

The equation of 2.2 holds for p = 0, 1, ... , n - 1. This is, in fact,
one form of the promised set of linear equations between the quantities
A;, B;.
We now give the second proof.
Let 9 be a finite Abelian group. A character x of 9 is a homomorphism
of 9 into the multiplicative group of complex numbers of absolute value
1. The characters of 9 form a group g* which is isomorphic to g, there
being in general no canonical isomorphism. t
If G. is a subgroup of g, the characters such that x(a) = 1 for all a of

G. form a subgroup CB* of g*. CB* is precisely the character group of 9
modG..
Suppose now that 9 is the additive group of a finite field. g* is just a
multiplicative copy of g, and the characters can be labeled by the ele-
ments of 9 in a symmetric way; that is, if r, s, ... are elements of 9
we have
 x.(s) = x.(r) = x(r, s).

If 9 is the additive group of a prime field of order q, we take r, s etc.

t For prime fields, the proof can be given without mentioning the word charac-
ter. The presentation here is an uneasy compromise with conscience - we wish
to indicate possible extensions to nonprime fields without doing too much work.

86 THE BELL SYSTEM TECHNICAL JOURNAL, JANUARY 1963

to be the integers mod q,and set x(r, s) = t B where t is a primitive qth
root of unity.
We have from the general theory of characters

x(r, 0) = x(O, s) = 1,
,.
:E x(r, s) = -1
r=l if s ~ O.

Let EI, E2, ••• , En be the fixed basis of F", and U = (UI, U2, '" , Un)
the coordinates of a vector of E" with respect to this basis. The char-
acter group of F" is, of course, a multiplicative copy of E",We label the
characters by elements of F" as follows:

n

Let a be a subspace of E", The characters such that l/tb(a) = 1 for all
a of ('t form a subgroup <B* of the character group. <B* is exactly the
character group of Fn moda. The elements b which label these charac-
ters form a subspace <B of E",isomorphic to F"mod a. In our notation,
the equation l/t(a, b) = 1 holds for all a of a and all b of <B, and given
either ('t or <B, the other is uniquely] determined by this condition.
Lemma2.3: Let a, <B be related as above. Then

i. L:l/t(v, a) = l if v E <B.
aell

ii. :E l/t(v, a) = 0 if v ~ <B.
aell

Proof: Part i is obvious, since by definition l/t(v, a) = 1 if v E B. For
ii we observe that for a E a, l/t(v, a) = l/ta(V) is a character of F" mod<B.
If v denotes a coset of F" mod<B, La.ll l/ta(V) = 0 for v ~ <B. Now
l/ta(V) = l/ta(V) for any v in Vj hence
:E l/t(v, a) = :E l/ta(V) = 0 if v ~ <B.
a ea 4t(l

Lemma2.4: If F is a primefield, then ('t, (B are related as in 2.3 if and
onlyif they areorthogonal complements.
Proof: l/t(a, b) = t'Ea;b;where t is a primitive qth root of unity. Hence
l/t(a, b) = 1 implies that a is orthogonal to b. Since ('t is isomorphic to
E" mod<B the dimensions of a, <B add up to n. Thus <B is the orthogonal
complement of ('t.

t That is, if F is a prime field. Otherwise we must fix the basis of F over its
prime field before we claim uniqueness.

WEIGHTS IN A SYSTEMATIC CODE 87

Let f( i, s) denote a function of the integers i, s with values in a ring
R. The values of f( i, s) may be added and multiplied, and these opera-
tions obey the two distributive laws. f(i, Vi) denotes the same function
of i and the ith coordinate of v.
Lemma 2.5:
 n n 'Y
L Ilr«. Vi) = IT Lf(i, r),
11 4! pft i-I i==-l r!!!!!!!!O

Proof: If n = 1 the statement is

'Y 'Y
Lf(l, s) = Lf(l, r ),
8-0 r=O

which is obvious. Assume the truth of the lemma for F n
- 1•
Let F,", 0 ~ r ~ 'Y, denote the set of vectors of F" which have last
coordinate r. Clearly the F; n are a partition of F",Then

"y 11-1 "'(
= L f(n, r) IT L f(i, r) (by induction)
r-=O i=-l r=O

" 'Y
= II L f(i, r),
i-I r=O

Let z(r) be a set of (commuting) indeterminates, r = 0, 1, "', 'Y. To
each vector V = (Vl, V2, ••• , VII) of F"associate a monomial 11;:'1 Z(Vi).
The monomial associated with V describes how many times each field
element appears as a component of v. Let R be the ring of polynomials
in z(O), z(l), ... , z('Y) over the complex numbers. Let U = (Ul , U2 , ••• ,Un)
be a fixed vector of F".
Lemma2.6:

Proof: Set fU, Vj) = X(Uj , vlII)z(Vj), which is in R. Then

II
1f;(u, v)z(V 1)Z("2) ••• Z(l''') = II f<i,Vj).

j~l

By 2.5,

88 THE BELL SYSTEM TECHNICAL JOURNAL, JANUARY 1963

Lemma2.7: Let ex, (B be orthogonal complementsin F", as usual. Then

Proof:We evaluate the quantity

F(u, v) = L:: L:: x(u, v)z(V 1)Z(V2) ••• Z<vn)

U e a v E Fn

in two ways, which give the two sides of the equation.
By 2.6
 n 'Y
F(u, v) = L:: II L X(Uj, r)i
r).

U E (1 j~l rClO

Also
 F(u, v)

By 2.4 and 2.3

Hence
 L:: Z(Vl)Z(V2) ••• z(v n) L:: 1/;(u, v).
v E Fn U E a

F( u, v) = q" L Z<Vj)iV2) ••• z(v,,).
v • <ll

Theorem2.8: Let ex be a k-dimensionalalphabet of F", and(B the ortho-
gonalcomplementof dimension m= n - k, Let A" B, denote the numoe»
of letters of weighti in eL, ill. Then

n n
L::A,(1 +'Yz)n-'(1-z)' = q" LBizi.

i-O i=O
l

z ifr~O
Proof:In 2.7 set z(r) = 1 if r = O.

If Uj = 0, X(Uj, 1') is 1and L::J=o x(Uj, r)z(r) becomes (1 + 'Yz).

If Uj ~ 0 L::J-l X(Uj, 1') is -1, and L;=o x(Uj, 1')Z(r) becomes (1 - z).

WEIGHTS IN A SYSTEMATIC CODE 89

Let IU Idenote the number of nonzero Uj •

Then IT'}..1 L;-o x( Uj , r)ir ) goes into (1 + -yz)n-I ul (1 - z) lui;
IU Iis of course the weight of U = (U1, U2, ••• , Un), so that the left-
hand side of 2.7 becomes

n
L .1;(1 + -yz)n-i(l - z);.
i=O

The right-hand side of 2.7 is clearly

n
k"'B i
q L.. «,
i=O

which proves the theorem.
Innumerable sets of linear equations between the quantities Ai, B;
may be obtained from theorem 2.8. The following two are sometimes
useful.
Lemma2.9: For p = 0, 1, ... , n,

i.

(Theseere theequationsof 2.2.)

ii. t Ai (i) = r: t (_I)iB.--yv-i (n - i).
i=v P i=O n - P

i. is obtained by setting (1 + -yz)/(l - z) = 1 + y,
ii. by setting (1 - z)/(1 + -yz) = 1 + y. The algebraic details are
easy to verify.
This process is reversible, i.e., (i) or (ii) imply 2.8: Before exploring
the consequences of theorem 2.8, we give a different specialization of 2.7.
Theorem.2.10: Let B,m be the number ofletters of <B which contains
coordinatesequal to1. Let .10.be the number oflettersU in G. of weights [or
which Li:'1 Uj = O. Let Ala be the number ofletters U in G. of weights for
which Li::'1 Uj ;;6 O. (Clearly A, = .10.+ Ala).
Then
 II
L B,(l)z' = (.10, - Ala/-y)(z - 1)'(z + -y)n-,.
,-0

Proof: In 2.7 set
 (r) lzz = 1
 if r = 1

if r ;;6 1.

90 THE BELL SYSTEM TECHNICAL JOURNAL, JANUARY 1963

Then
 n
l L Z(V 1)Z(V2) ••• i Vn ) becomes qk L B.(J)z·,

p e <B 8-0
., .,
L X(Ui, r)z(r) becomes X(Ui, I)z + L X(Ui, r) - X(Ui, 1)
r=O r=O .,

= X(Ui, I)(z -1) + Lx(ui,r)
r-O
= IX(Ui' I)(z - 1)
lz+ 'Y
 ifui~O
ifui=O

n .,
II L X (~ti, 1')Z(r) becomes
i=:ol r-O

Now if U is a letter of A, so are also the letters 2u, ... , 'YU, and these
have the same weight as u. We sum first over these letters
., .,
L ITX (SUi, 1) = L X(S~~ti, 1)
8=1 8=:11
 if ~Ui ~ 0

if~ui=O

The sum of

over all letters in (t, of the same weight as U is thus

(A Ol ul - (A11u1h»(z+ 'Y)n-Iul(z - 1) l u1,

Hence the left-hand side of 2.7 becomes

n
L (Ao. - (Alsh» (z + 'Y) n-8(z - 1)".
8=0

We return now to the consequences of theorem 2.8. As remarked in
the proof of 2.10, if (t, contains a letter u, it contains also the letters
2u, ... , 'Yu; that is, the number of letters of weight i in G. is divisible
by'Y for i > O. We have then
Lemma2.11: A necessaryconditionfor theexistenceof an alphabetcon-
taining lettersof weightsWi , i = 1, 2, "', s, and noother, is theexistence
of a set ofintegersai , i = 1,2, ... , s, such that theexpression

WEIGHTS IN A SYSTEMATIC CODE

•
(1 + 'Yz)n + 'Y L IXi(l + 'Yz)n-w'(l - Z)W',
;-1 .

when expanded in powers of z, takes theform

n
l + 'Yl L {3ii,
i=1
 91

where the {3i are positive integers.
It has been pointed out before that this condition is not sufficient.
Suppose now that a = a1+ a2 is a decomposable alphabet. a; is a
k;-dimensional alphabet in F'", j = 1, 2, with orthogonal alphabet B;.
k1 + k2 = le, and nl + ~ = n. Let AP', A.'2l and BP', B/2l be the
number of letters of weight i in a1, a2 , (B1 , (B2 .
Lemma 2.12:
 n
L Ai(l + 'Yz)n-i(l - z/
i=O

= [f: A.'1l(l + 'Yz)n1-i(1 - Z)iJ [~ A.'2l(1 + 'Yz)nz-i(l - Z)iJ
,=0 1=0

= t [llf:B.'llZiJ [lz ~ B.'2lziJ .
• =0 .=0 .=0

Proof: The number of letters of weight s in (Bl + (B2 is
L B,,(l)Bp(2l,
"+p=.

which is the coefficient of z· in L~~o BPli L~:'oB.' 2li. Similarly,
L A" (1lA p (2l
"+p=.

is the coefficient of (1 + 'Yz)n-"(1 - z)" in
[f:A/1l(1 + 'Yz)n1-i(1 - Z)iJ [~A/2l(l+ 'Yz)nz-i(l_ z)iJ.
1=0 1=0

We define the coset leader of a coset of a in F" to be an element of
least weight in the coset. The weight of a coset is defined to be the
weight of its coset leader.
If Ai = 0 for i = 1, 2, ... , 2e every vector of weight ~ e in F" ap-
pears as a coset leader for a and conversely. Another way of saying this
is: for all pairs of distinct letters a, a' of a, the set of vectors at distance
i ~ e from a is disjoint from the set of vectors at distance i from a'.
Let ct', C2(i), ... , c.(i) be the cosets of A of weight i; we assume that

92 THE BELL SYSTEM TECHNICAL JOURNAL, JANUARY 1963

v = '1"(:), i.e., that all vectors of weight i appear as coset leaders. Let
f." be the number of vectors of weight s contained in the set-theoretic
•
union U c/'). The polynomial L~=o f.,ix' is called the enumerator (by
i=l
weight) of this set of vectors. We propose to show that theorem 2.8 gives
a convenient expression for this enumerator. We need the following
preliminary lemma.
Lemma2.13: Let u be a fixed vector of weighti. Let d. t be the numberof
vectors of weights which are at distance tfrom u. Then

n n
L L d.1xV = (1 +'Yxy)n-i[x+ y + ('1' - l)xy)'.
.=0 1=0

Proof: Suppose first that u = (Ul, U2, ••. , u,) is a vector of weight
i in F": We show that under these circumstances

i i
L L d. t = [x + y + ('1' - l)xy]i.
• =0 t=O
This is obvious for i = 1; we suppose it true for i-I. Let v = (VI, V2 ,
... , Vi-I) be a vector of weight s distant t from (Ul, U2, ... , Ui-J) in
r:'. From v we obtain:
i. One vector (VI, V2, , V,-l, 0), weight s, distant t + 1 from u.
ii. One vector (VI, V2, , Vi-I, Ui) weight s + 1 distant t from u.
iii. '1' - 1 vectors (VI, V2, ... , Vi-I, Vi) Vi ~ 0, Vi ~ u, which have
weight s + 1, and are distant t + 1 from u.
Hence the enumerator for i is obtained by multiplying that for i-I
by [x + y + ('1' - 1 )xy], and the lemma is proved for n = i.
We now apply induction to n - i. Let U be a vector of weight i in
F", and u' a vector of weight i in F n- 1 obtained from u by omitting one
zero coordinate. Let v' be a vector of F n- 1 which has weight e and is
distant t from u'. From v' we obtain in F n

i. One vector of weight s, distant t from u, by adding a zero coordinate
to o',
ii. '1' vectors of weight s + 1, distant t + 1 from u, by adding a non-
zero coordinate to o',
This corresponds to multiplication by (1 +'Yxy). Hence the lemma is
proved.
Lemma2.11(-: Suppose that Ai = 0, i = 1, 2, ... , 2e, and take t ~ e.
Then the enumerator,LZ-o/.,tx',of vectors in cosets of weight t of F"
mod (j, is the coefficient ofyt in

n
L A,(1 +'Yxy)n-i(x+ y + ('1' - l)xy)i.
,=0
 WEIGHTS IN A SYSTEMATIC CODE 93

Proof: The cosets of weight t in F" modG. are disjoint, and contain all
vectors of F" which are at distance t from some letter of G..
Set (1 + 'Yz)n-i(1 - Z)i = L~=o 'lr(i, n, r)zr. Let ill, B, have their
usual meaning. Assume the conditions of 2.14.
Lemma2.15:t

n n
qm Lf.. tx• = L s.e«, n, t)(1 + 'Yx)n-i(1 - x)'
3=0 i=O

Proof: Set
 z = x + y + ('Y - l)xy
1 + 'Yxy ,
then

1 + 'YZ = (l + 'YX)(l + 'YY)
(1 + 'YXY) ,

Make this substitution in the equation
 (l-x)(l-y)
1-z= .
1 + 'Yxy

n n
L B i(1 + 'Yz)n-i(1 - z) = qm L Aizi

i-O i~O
we obtain
..
L B i(1 + 'Yx)n-i(l - x)i(1 + 'Yy)"-i(1 _ y)i
i==O ..
= qm L Ai(l + 'Yxy)n-i(x+ y + ('Y - l)xy)i.
i=O

Equating coefficients of yt gives us

n n
L Bi'I!(i, n, l)(1 + 'Yx)n-i(1 - X)i = qm Lf.. tx•
i=O .=0

III. APPLICATIONS

The easiest application of theorem 1 is to a generalized Hamming
alphabet, that is, a close-packed I-error correcting alphabet over a field
of q elements. Such an alphabet exists for n = (qm - 1)f'Y, all m > 1.
3

The dual alphabet is of dimension m, and contains (qm - I) letters
of weight «".The spectrum of a generalized Hamming alphabet is
thus given by the expansion of
(l + 'Yz)n + (qm - 1)(1 + 'Yz)n-u(1 - z) u

where n = (qm - 1)f'Y, u = «:
t A similar formula (q = 2) is found by Lloyd! for close-packed codes which
are not assumed to be group codes.

94 THE BELL SYSTEM TECHNICAL JOURNAL, JANUARY 1963

TABLE I - DISTRIBUTION OF WEIGHTS IN THE Two GOLAY CODES
The first table is for the 3-error-correcting (23,12) alphabet over Z2 ,the second
for the 2-error-correcting (11, 6) alphabet over Z3 . In both cases, i stands for
weight, Bi for the number of letters of weight i in the dual alphabet, A, for the
number of letters of this weight in the Golay alphabet.

i B, A,

0 1 1
7 0 23X11
8 23 X 22 23 X 22
11 0 23 X 56
12 23 X 56 23 X 56
15 0 23 X 22
16 23 X 11 23X11
23 0 1

i Bi A,

0 1 1
5 0 2 X 66
6 2 X 66 2 X 66
8 0 2 X 165
9 2 X 55 2 X 55
11 0 2 X 12

Theorem 1 may, in fact, be used to calculate the number of letters of
each weight in any close-packed code. The results for the two Golay"
codes are given in Table I.
Anything which is known about the structure of an alphabet or its
dual may be used with theorem 1 to limit the number of possible weight
distributions. Such items of information are a very diversified character,
and no general method has been developed. However, the results ob-
tained by hand calculation indicated that it is probably worthwhile to
make a systematic computer study of the known classes of alphabets.

ACKNOWLEDGMENTS

The author would like to thank her friends and associates for their
consistently helpful suggestions; and is especially indebted to H. E.
Elliott for the elegant proof of lemma 2.5 and to J. B. Kruskal for
theorem 2.10. The criticisms and suggestions of Professor A. M.
Gleason of Harvard University produced new and better proofs of
practically every other theorem in this paper.

REFERENCES

1. Slepian, D., A Class of Binary Signaling Alphabets, B.S.T.J., 35, January, 1956,
pp. 203-234.
2. Bose, R. C., and Kuebler, R. R., Jr., A Geometry of Binary Sequences Asso-
ciated with Group Alphabets in Information Theory, Ann. Math. Stat. 31,
1960, p. 113.
3. MacWilliams, F. J., Error-correcting Codes for Multiple-Level Transmission,
B.S.T.J., 40, January, 1961, pp. 281-308.
4. Slepian, D., Some Further Theory of Group Codes, B.S.T.J., 39, September,
1960, pp. ]219-1252.
5. Llovd, S. P .. Binarv Block Codine:. B.S.T.J.. 36. March. 1957. PP. 517-535.
