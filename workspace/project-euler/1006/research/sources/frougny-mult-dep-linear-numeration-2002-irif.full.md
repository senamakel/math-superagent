<!-- source: https://www.irif.fr/~cf/publications/lucas.pdf | converted from PDF -->

On multiplicatively dependent
linear numeration systems,
and periodic points

shristiane vrougny

1 L.I.A.F.A.
Case 7014, 2 place Jussieu, 75251 Paris Cedex 05, France
Christiane.Frougny@liafa.jussieu.fr
2 Universit«e Paris 8

Abstract. Two linear numeration systems, with characteristic polyno-
mial equal to the minimal polynomial of two Pisot numbers β and γ
respectively, such that β and γ are multiplicatively dependent, are con-
sidered. It is shown that the conversion between one system and the
other one is computable by a ﬁnite automaton. We also deﬁne a se-
quence of integers which is equal to the number of periodic points of a
soﬁc dynamical system associated with some Parry number.

1 Introduction

This work is about the conversion of integers represented in two diEerent
numeration systemsT linked in a certain sense[ Recall that the conversion
between base d and base b is computable by a ﬁnite automatonT but that
conversion between base c and base b is not[ More generallyT two numbers
pu a and qu a are said to be multiplicatively dependent if there exist
positive integers k and P such that pk m qr[ q set of natural numbers
is said to be p-recognizable if the set of representations in base p of its
elements is recognizable by a ﬁnite automaton[ r˝uchi has shown that the
set {qn | n ≥ ]} is pWrecognizable only if p and q are multiplicatively
dependent integers [e][ yn contrastT the famous theorem of sobham [g]
states that the only sets of natural numbers that are both pW and qW
recognizableT when p and q are two multiplicatively independent integers
u aT are unions of arithmetic progressionsT and thus are kWrecognizable
for any integer ku a[ Several generalizations of sobham’s Theorem have
been givenT see for instance [beT a]T fT agT h][ yn particular this result has
been extended by r`es [d] to nonWstandard numeration systems[
The most popular nonWstandard numeration system is probably the
vibonacci numeration system[ Recall that every nonWnegative integer can

be represented as a sum of vibonacci numbersT which can be chosen nonW
consecutive[ yt is also possible to represent an integer as a sum of ˜ucas
numbers[ Since vibonacci and ˜ucas numbers satisfy the same recurrence
relationT the question of the conversion between ˜ucas representations
and vibonacci representations is very natural[ yn [bb] and [bc]T the relation
between the vibonacci sequence and the ˜ucas sequence is examined from
another point of view[ q sequence of nonWnegative integers OvnPn≥0 is said
to be exactly realizable if there exists a dynamical system OSℓ QPT where
S is a compact metric space and Q j S → S is an homeomorphismT for
which for all n ≥ aT vn is the number of periodic points of period nT that
isT vn mH{s ∈ S | QnOsPm s}b

The authors give a necessary and suFcient condition for a sequence to be
exactly realizable in certain cases[ yn particularT they prove that amongst
the sequences satisfying the vibonacci recurrence un m un−1 S un−2T the
unique Oup to scalar multiplesP exactly realizable sequence is the one of
˜ucas numbersT and the dynamical system is the golden mean shiftT that
is to sayT the set of biWinﬁnite sequences on the alphabet {]ℓ a} such that
a a is always followed by a ][
q linear numeration system is deﬁned by an increasing sequence of
integers satisfying a linear recurrence relation[ The generalization of the
sobham’s Theorem by r`es [d] is the following one j let two linear nuW
meration systems such that their characteristic polynomials are the miniW
mal polynomials of two multiplicatively independent Pisot numbers1k the
only sets of natural numbers such that their representations in these two
systems are recognizable by a ﬁnite automaton are unions of arithmetic
progressions[
vrom the result of r`es follows that the conversion between two linear
numeration systems U and Y linked to two multiplicatively independent
Pisot numbers cannot be realized by a ﬁnite automaton[ yn this paperT we
prove that the conversion between two linear numeration systems U and
Y such that their characteristic polynomials are the minimal polynomials
of two multiplicatively dependent Pisot numbers is computable by a ﬁnite
automaton[ This implies that a set of integers which is U Wrecognizable is
then also Y Wrecognizable[ Note that in [f] it is proved that if U and V are
two linear numeration systems with the same characteristic polynomial
which is the minimal polynomial of a Pisot numberT then a U Wrecognizable
set is also V Wrecognizable[

1 A Pisot number is an algebraic integer such that its algebraic conjugates are strictly
less than 1 in modulus. The golden mean and the natural numbers are Pisot numbers.

b

The paper is organized as follows[ virst we recall several results which
will be of use in this paper[ yn particularT the normalization in a linear
numeration system consists in converting a representation on a “big” alW
phabet onto the soWcalled normal representationT obtained by a greedy
algorithm[ xere the system U is ﬁxed[ yt is shown in [ae] thatT basicallyT
when the sequence U is linked to a Pisot numberT like the vibonacci numW
bers are linked to the golden meanT then normalization is computable by
a ﬁnite automaton on any alphabet of digits[ yn the present work we ﬁrst
construct a ﬁnite automaton realizing the conversion from ˜ucas repreW
sentations to vibonacci representations[ Then we consider two sequences
of integers U and V [ yf the elements of V can be linearly expressed Owith
rational coeFcientsP in those of U T and if the normalization in the system
U is computable by a ﬁnite automatonT then so it is for the conversion
from V Wrepresentations to U Wrepresentations[ vrom this result we deduce
that if U and V have for characteristic polynomial the same minimal
polynomial of a Pisot numberT with diEerent initial conditionsT then the
conversion from V Wrepresentations to U Wrepresentations is computable by
a ﬁnite automaton[
Next we introduce two diEerent linear numeration systems associated
with a Pisot number R of degree m[ The ﬁrst oneT UtT is deﬁned from
the point of view of the symbolic dynamical system deﬁned by R[ We call
it Fibonacci-likeT because when R is equal to the golden meanT it is the
vibonacci numeration system[ The second oneT VtT is deﬁned from the
algebraic properties of R[ More preciselyT for n ≥ aT the nWth term of Vt
is vn m Rn S Rn
2 S ··· S Rn
mT where R2T [ [ [ T Rm are the algebraic conjugates
of R[ We call it Lucas-likeT because when R is equal to the golden meanT
it is the ˜ucas numeration system[ The conversion from Vt to Ut Oor any
sequence with characteristic polynomial equal to the minimal polynomial
of RP is shown to be computable by a ﬁnite automaton[
Then we consider two linear numeration systemsT U and Y T such that
their characteristic polynomial is equal to the minimal polynomial of a
Pisot number RT or S respectivelyT where R and S are multiplicatively
dependent[ Then the conversion from Y to U is shown to be computable
by a ﬁnite automaton OTheorem bP[
The ˜ucasWlike sequence Vt plays a central role in the proof of TheoW
rem b[ yn factT it is also closely related to the number of periodic points
of the symbolic dynamical system St associated with R[ xere we do not
need the assumption that R is a Pisot number[ q Parry number is a real
number R such that the betaWexpansion of a Osee Section b[dP is evenW
tually periodic or ﬁnite[ Such numbers are usually called beta-numbers

c

after Parry [ba][ Note that a Pisot number is a Parry number [b][ vrom
now on R is a Parry numberT and the vibonacciWlike sequence and the
˜ucasWlike sequence are deﬁned as in the Pisot case[ yf the symbolic dyW
namical system St associated with R is of ﬁnite typeT that is to say if the
betaWexpansion of a is ﬁniteT then the sequence Vt is exactly realized by
St[ This is no more the case when the symbolic dynamical system associW
ated with R is not of ﬁnite typeT but is soﬁcT i.e. the betaWexpansion of a
is inﬁnite eventually periodic[ We deﬁne a sequence Rt which is exactly
realized by St in the soﬁc case[ yt is shown that the set of greedy repreW
sentations of the natural numbers in the linear numeration system deﬁned
by Rt is not recognizable by a ﬁnite automatonT and consequently the
conversion between Rt and Vt cannot be realized by a ﬁnite automatonT
even if R is a Pisot number[
Section i is devoted to the quadratic case study as an example for the
general case[ We end this paper by exploring the connection between the
˜ucasWlike sequence Vt and the base RWrepresentations for the case where
R is a Pisot quadratic unit[ Note that in [ad] we have proved that the
conversion from UtWrepresentations to folded RWrepresentations is comW
putable by a ﬁnite automatonT and in [af]T that this is possible only if R
is a quadratic Pisot unit[
Part of this work has been presented in [ac][

2 Preliminaries

2.1 Words

qn alphabet x is a ﬁnite set[ q ﬁnite sequence of elements of x is called
a wordT and the set of words on x is the free monoid x∗[ The empty
word is denoted by T[ The set of inﬁnite sequences or inﬁnite words on x
is denoted by xN[ ˜et v be a nonWempty word of x∗T denote by vn the
concatenation of v to itself n timesT and by vv the inﬁnite concatenation
vvv ··· [ qn inﬁnite word of the form uvv is said to be eventually periodic[
q factor of a Oﬁnite or inﬁniteP word w is a ﬁnite word f such that
w m uf v[

2.2 U -representations

The deﬁnitions recalled below and related results can be found in the
survey [b]T shap[ g][ We consider a generalization of the usual notion of
numeration systemT which yields a representation of the natural numbers[

d

The base is replaced by an inﬁnite increasing sequence of integers[ The
basic example is the wellWknown vibonacci numeration system[
˜et U mOunPn≥0 be a strictly increasing sequence of integers with
u0 m a[ q U Wrepresentation of a nonWnegative integer N is a ﬁnite sequence
of integers OdiPk≥i≥0 such that N m ∑k
i=0 diuib Such a representation will
be written ON PU m dk ··· d0T most signiﬁcant digit ﬁrst[
qmong all possible U Wrepresentations of a given nonWnegative integer
N one is distinguished and called the normal U -representation of N k it
is also called the greedy representationT since it can be obtained by the
following greedy algorithm [aa]j given integers m and p let us denote
by qOmℓ pP and rOmℓ pP the quotient and the remainder of the uuclidean
division of m by p[ ˜et k ≥ ] such that uk ≤ N s uk+1 and let dk m
qONℓ ukP and rk m rONℓ ukPT andT for i m k − aT [ [ [ T ]T di m qOri+1ℓuiP and
ri m rOri+1ℓuiP[ Then N m dkuk S···Sd0u0[ The normal U Wrepresentation
of N is denoted by ⟨N ⟩U [ The normal U Wrepresentation of ] is the empty
word T[ The set of greedy or normal U Wrepresentations of all the nonW
negative integers is denoted by GOU P[ yn this workT we consider only the
case where the sequence U is linearly recurrent[ Then the numeration
system associated with U is said to be a linear numeration system[ The
digits of a normal U Wrepresentation are contained in a canonical ﬁnite
alphabet xU associated with U [
˜et D be a ﬁnite alphabet of integers and let w m dk ··· d0 be a word
of D∗[ tenote by UU OwP the numerical value of w in the system U T that
isT UU OwPm ∑k
i=0 diui[ The normalization in the system U on D∗ is the
partial function VU,D∗ j D∗ → x∗
U that maps a word w of D∗ such that
N m UU OwP is nonWnegative onto the normal U Wrepresentation of N [
˜et U and V be two sequences of integersT and let D be a ﬁnite
alphabet of integers[ The conversion from the numeration system V to
the numeration system U on D∗ is the partial function W j D∗ → x∗
U that
maps a V Wrepresentation dk ··· d0 in D∗ of a nonWnegative integer N m∑k
i=0 divi onto the normal U Wrepresentation of N [ yn fact the alphabet D
plays no peculiar roleT and we will simply speak of the conversion from V
to U [

2.3 Beta-expansions

We now consider numeration systems where the base is a real number
R u a[ Representations of real numbers in such systems were introduced
by R´enyi [bd] under the name of beta-expansions[ ˜et the base R u a
be a real number[ virst let x be a real number in the interval []ℓ a][ q
representation in base R of x is an inﬁnite sequence of integers OxiPi≥1 such

e

that x m ∑
i≥1 xiR−i[ q particular betaWrepresentationT called the beta-
expansionT can be computed by the “greedy algorithm” j denote by ⌊y⌋
and {y} the integer part and the fractional part of a number y[ Set r0 m x
and let for i ≥ aT xi m ⌊Rri−1⌋T ri m {Rri−1}[ Then x m ∑i≥1 xiR−iT
where the xi’s are elements of the canonical alphabet xt m {]ℓ b b b ℓ ⌊R⌋}
if R is not an integerT or xt m {]ℓ b b b ℓ R − a} if R is an integer[ The
betaWexpansion of x is denoted by dtOxP[
˜et D be a ﬁnite alphabet of integers[ The normalization in base R
on DN is the partial function Vt,DN j DN → xN
t that maps a word OxiPi≥1
of DN such that x m ∑i≥1 xiR−i ∈ []ℓ a[ onto the RWexpansion of x[
SecondlyT we consider a real number x greater than a[ There exists
k ∈ N such that Rk ≤ xs Rk+1[ xence ] ≤ xcRk+1 s aT thus it is enough
to represent numbers from the interval []ℓ a]T since by shifting we will get
the representation of any positive real number[ q RWrepresentation of an
x m ∑k≤i≤−∞ xiRi will be denoted by OxPt m xk ··· x0.x−1x−2 ··· [
yf a representation ends in inﬁnitely many zerosT like v]vT the ending
zeros are omitted and the representation is said to be ﬁnite[
q Pisot number is an algebraic integer such that its algebraic conjuW
gates are strictly less than a in modulus[ yt is known that if R is a Pisot
number then dtOaP is ﬁnite or inﬁnite eventually periodic [b][

2.4 Symbolic dynamical systems

The reader may consult [ai] for more details on these topics[ ˜et x be
a ﬁnite alphabetT recall that xN is endowed with the product topology
and the shift Q deﬁned by QOOxiPi≥1P m Oxi+1Pi≥1[ yt is a compact metric
space and Q is a homeomorphism[ q symbolic dynamical system is a closed
shiftWinvariant subset of xN[ yt is said to be a system of ﬁnite type if it is
deﬁned by the interdiction of a ﬁnite set of factors[ yt is said to be soﬁc
if the set of its ﬁnite factors is recognizable by a ﬁnite automaton[ Note
that a system of ﬁnite type is soﬁc[ The same notions can be deﬁned for
biWinﬁnite sequences and subsets of xZ[
tenote by Dt the set of RWexpansions of numbers of []ℓ a[[ The closure
of Dt in xN
t is a symbolic dynamical systemT called the beta-shift St[ The
following results are knownj the betaWshift is of ﬁnite type if and only if
if the RWexpansion of aT dtOaPT is ﬁniteT and the betaWshift is soﬁc if and
only if dtOaP is eventually periodic [b][
ry abuseT we will keep the same name of betaWshift for the set of biW
inﬁnite sequences such that each right tail is in the oneWsided betaWshift[
We denote by PernOStP the number of periodic elements of period n under
the shift of St [
 f

vollowing [bbT bc] we say that a sequence of nonWnegative integers V m
OvnPn≥0 is exactly realizable if there exists a betaWshift St such that for
every n ≥ aT vn m PernOStP[

2.5 Automata

We refer the reader to [i][ qn automaton over xT A mOQℓ xℓ Eℓ Iℓ T PT is a
directed graph labelled by elements of x[ The set of verticesT traditionally
called statesT is denoted by QT I ⊂ Q is the set of initial statesT T ⊂ Q
is the set of terminal states and E ⊂ Q × x × Q is the set of labelled
edges[ yf Opℓ aℓ qP ∈ ET we denote p a
−→ q[ The automaton is ﬁnite if Q is
ﬁnite[ q subset H of x∗ is said to be recognizable by a ﬁnite automaton
if there exists a ﬁnite automaton A such that H is equal to the set of
labels of paths starting in an initial state and ending in a terminal state[
q 2-tape automaton with input alphabet x and output alphabet y is an
automaton over the nonWfree monoid x∗ × y∗ j A mOQℓ x∗ × y∗ℓ Eℓ Iℓ T P
is a directed graph the edges of which are labelled by elements of x∗ ×y∗[
The automaton is ﬁnite if Q and E are ﬁnite[ The ﬁnite bWtape automata
are also known as transducers[ q relation R of x∗ × y∗ is said to be
computable by a ﬁnite automaton if there exists a ﬁnite bWtape automaton
A such that R is equal to the set of labels of paths starting in an initial
state and ending in a terminal state[ q function is computable by a ﬁnite
automaton if its graph is computable by a ﬁnite bWtape automaton[ These
deﬁnitions extend to relations Oand functionsP of inﬁnite words as followsj
a relation R of inﬁnite words is computable by a ﬁnite automaton if there
exists a ﬁnite bWtape automaton such that R is equal to the set of labels of
inﬁnite paths starting in an initial state and going inﬁnitely often through
a terminal state[ Recall that the set of relations computable by a ﬁnite
automaton is closed under composition and inverse[

2.6 Previous results

yn this work we will make use of the following results[ ˜et U be a linearly
recurrent sequence of integers such that its characteristic polynomial is
exactly the minimal polynomial of a Pisot number[ Then the set GOU P
of normal U Wrepresentations of nonWnegative integers is recognizable by
a ﬁnite automatonT andT for every alphabet of positive or negative inteW
gers DT normalization VU,D∗ is computable by a ﬁnite automaton [ae][
Normalization in base RT when R is a Pisot numberT is computable by
a ﬁnite automaton on any alphabet D [ab][ qddition and multiplication
by a ﬁxed positive integer constant are particular cases of normalizationT

g

and thus are computable by a ﬁnite automatonT in the system U and in
base R[ These results on normalization do not extend to the case that R
is a Parry number which is not a Pisot number[

3 Fibonacci and Lucas

˜et us recall that the Fibonacci numeration system is deﬁned by the
sequence F of vibonacci numbers

F m {aℓ bℓ cℓ eℓ hℓ acℓ b b b}b

The canonical alphabet is xF m {]ℓ a} and the set of normal representaW
tions is equal to GOF P m a{]ℓ a}∗ \{]ℓ a}∗aa{]ℓ a}∗ ∪ T[ Words containing
a factor aa are forbidden[
The Lucas numeration system is deﬁned by the sequence L of ˜ucas
numbers L m {aℓ cℓ dℓ gℓ aaℓ ahℓ b b b}b

The canonical alphabet is xL m {]ℓ aℓ b} and the set of normal represenW
tations is equal to GOLPm GOF P∪OGOF P\TP{]b}∪{b}[ We give in Table a
below the normal vibonacci and ˜ucas representations of the ﬁrst natural
numbers[
 N Fibonacci Lucas
1 1 1
2 10 2
3 100 10
4 101 100
5 1000 101
6 1001 102
7 1010 1000
8 10000 1001
9 10001 1002
10 10010 1010
11 10100 10000

Table 1. Normal Fibonacci and Lucas representations of the 11 ﬁrst integers

The vibonacci and the ˜ucas sequences both have for characteristic
polynomial P OXPm X2 − X − ab

h

The root u a of P is denoted by XT the golden meanT and its algebraic
conjugate by X′[ Since X S X′ m aT for coherence of notations with the
general caseT we denote F mOFnPn≥0 and L mOLnPn≥1[ Recall that
for every n ≥ aT Ln m Xn S X′n[ The associated dynamical system is
the golden mean shiftT which is the set of biWinﬁnite sequences on {]ℓ a}
having no factor aa[
qlthough the following result is a consequence of the more general
one below OTheorem aPT we give here a direct construction[

Proposition 1. The conversion from a Lucas representation of an inte-
ger to the normal Fibonacci representation of that integer is computable
by a ﬁnite automaton.

Proof. virstT for every n ≥ cT we get Ln m Fn−1 SFn−3[ Take N a positive
integer and a LWrepresentation ON PL m dk ··· d1T where the di’s are in an
alphabet y ⊇ {]ℓ aℓ b}T and k ≥ d[ Then N m dkLk S ··· S d1L1T thus
N m dkFk−1 S dk−1Fk−2 SOdk−2 S dkPFk−3 S ··· SOd3 S d5PF2 SOd2 S
d4PF1SOd1Sd2Sd3PF0T hence the word dkdk−1Odk−2SdkP ··· Od3Sd5POd2S
d4POd1 S d2 S d3P is a vibonacci representation of N on a certain ﬁnite
alphabet of digits D[
The conversion from a word of the form dk ··· d1 in y∗T where k ≥ dT
onto a word of the form dkdk−1Odk−2SdkP ··· Od3Sd5POd2Sd4POd1Sd2Sd3P
on D∗ is computable by a ﬁnite automaton A mOQℓ y × zℓ Eℓ {T}ℓ {t}Pj
the set of states is Q m {T} ∪ y ∪ Oy × yP ∪ {t} where {t} is the unique
terminal state[ The initial state is T[ vor each d in yT there is an edge

T d/d
→ db vor each d and c in yT there is an edge d c/c
→ Odℓ cPb vor each

Odℓ cP ∈ y × y and a in yT there is an edge Odℓ cP a/a+d
→ Ocℓ aPb vor each

Odℓ cP ∈ y × y and a in yT there is a terminal edge Odℓ cP a/a+c+d
→ tb Words
of length less than d are handled directly[
Then it is enough to normalize in the vibonacci system on D∗T and it
is known that this is realizable by a ﬁnite automatonT see Section b[f[ ⊓⊔

On vigure a we give an automaton realizing the conversion from norW
mal ˜ucas representations to vibonacci representations on {]ℓ aℓ b}∗O{T}∪
{c}P[ States of the form Odℓ cP are denoted by dc[ Note that this automaton
is not deterministic on inputs[ Since we are dealing with normal ˜ucas
representationsT the automaton has less states than the one constructed
in the proof of Proposition a above[ To decrease the complexity of the
drawingT we introduce more than one terminal state[ Terminal states are
indicated by an outgoing arrow[ The result must be normalized afterW
wards[
 i

ε 1 10 00

01
 0/0

1/1

2/2
 0/0 0/1

0/1
 2/3
 2/2

0/1

1/1
1/20/0

Fig. 1. Conversion from normal Lucas representations to Fibonacci representations

4 A technical result

We now consider two linearly recurrent sequences U mOunPn≥0 and V m
OvnPn≥0 of positive integers[ The result below is the generalization of
Proposition a[

Proposition 2. If there exist r rational constants Yi’s for a ≤ i ≤ r and
K ≥ ] such that for every n ≥ K, vn m Y1un+r−1 S ··· S Yrun, and if
the normalization in the system U is computable by a ﬁnite automaton on
any alphabet, then the conversion from a V -representation of an integer
to the normal U -representation of that integer is computable by a ﬁnite
automaton.

Proof. One can assume that the Yi’s are all of the form picq where the
pi’s belong to Z and q belongs to NT q ̸m ][ ˜et N be a positive integer
and consider a V Wrepresentation ON PV m bj ··· b0T where the bi’s are in
an alphabet of digits y ⊇ xV [ Then qN m bjqvj S ··· S b0qv0[ Since
for n ≥ KT qvn m p1un+r−1 S ··· S prunT and v0T v1T [ [ [ T vK−1 can
be expressed in the system U T we get that qN is of the form qN m
dj+r−1uj+r−1 S ··· S d0u0[ Since each digit diT for ] ≤ i ≤ j S r − aT is
a linear combination of qT p1T [ [ [ T prT the bi’s and the coeFcients of the
U Wrepresentation of the ﬁrst terms v0T v1T [ [ [ T vK−1T we get that di is an
element of a ﬁnite alphabet of digits D ⊃ xU [ ry assumptionT VU,D∗ is
computable by a ﬁnite automaton[ yt remains to show that the function
which maps VU,D∗Odj+r−1 ··· d0Pms qN uU onto s N uU is computable
by a ﬁnite automatonT and this is due to the fact that it is the inverse

a]

of the multiplication by the natural qT which is computable by a ﬁnite
automaton in the system U T see Section b[f[ ⊓⊔

5 Common characteristic polynomial

The vibonacci and the ˜ucas numeration systems are examples of diEerW
ent numeration systems having the same characteristic polynomialT but
diEerent initial conditions[

Theorem 1. Let P be the minimal polynomial of a Pisot number of
degree m. Let U and V be two sequences with common characteristic
polynomial P and diqerent initial conditions. The conversion from a V -
representation of a positive integer to the normal U -representation of that
integer is computable by a ﬁnite automaton.

Proof. Since the polynomial P is the minimal polynomial of a Pisot numW
berT normalization in the system U is computable by a ﬁnite automaW
ton on any alphabet Osee Section b[fP[ On the other handT the family
{unℓun+1ℓ b b b ℓ un+m−1 | n ≥ ]} is freeT because the annihilator polyW
nomial is the minimal polynomial[ Since U and V have the same charW
acteristic polynomialT it is known from standard results of linear algeW
bra that there exist rational constants Yi such thatT for each n ≥ ]T
vn m Y1un+m−1 S ··· S Ymun[ The result follows then from Proposition b[
⊓⊔

6 Two numeration systems associated with a Parry
number

˜et R be a Parry numberT i.e. the RWexpansion of a is ﬁnite or eventually
periodic[ We deﬁne two numeration systems associated with R[

6.1 Fibonacci-like numeration system

virst suppose that the RWexpansion of a is ﬁniteT dtOaP m t1 ··· tN [q
linear recurrent sequence Ut mOunPn≥0 is canonically associated with R
as follows un m t1un−1 S ··· S tN un−N for n ≥ N

u0 maℓ and for a ≤ i ≤ N − aℓui m t1ui−1 S ··· S tiu0 Sab

The characteristic polynomial of Ut is thus

KOXPm XN − t1X N −1 − · · · − tN b

aa

Suppose now that the RWexpansion of a is inﬁnite eventually periodicT

dtOaP m t1 ··· tN OtN +1 ··· tN +pP
v

with N and p minimal[ The sequence Ut mOunPn≥0 is the following one

un m t1un−1 S ··· S tN +pun−N −p S un−p − t1un−p−1 − · · · − tN un−N −p

for n ≥ N S pT

u0 maℓ and for a ≤ i ≤ N S p − aℓui m t1ui−1 S ··· S tiu0 Sab

The characteristic polynomial of Ut is now

KOXPm XN +p −
 N +p∑

i=1 tiX N +p−i − X N S
 N∑

i=1 tiX N −ib

Note that in general KOXP may be reducible[ Since KOXP is deﬁned from
the betaWexpansion of aT we will say that it is the beta-polynomial of R[
The system Ut is said to be the canonical numeration system assoW
ciated with R[ yn [c] it is shown that the set of normal representations
of the integers GOUt P is exactly the set of ﬁnite factors of the betaWshift
St[ The numeration system Ut is the natural one from the point of view
of symbolic dynamical systems[ The set GOUtP is recognized by a ﬁnite
automatonT see Section h[

6.2 Lucas-like numeration system

Now we introduce another linear recurrent sequence Vt mOvnPn≥0 assoW
ciated with R a Parry number of degree m as follows[ tenote by R1 m RT
R2T [ [ [ T Rm the roots of the minimal polynomial P OXPm Xm −a1X m−1 −
··· am of R[ Set

v0 maℓ and for n ≥ aℓvn m Rn
1 S ··· S Rn
mb

Then the characteristic polynomial of Vt is equal to P OXP[ The set GOVtP
is recognized by a ﬁnite automatonT [ae][

qs an example let us take R m X the golden mean[ Then Uw is the set
of vibonacci numbersT and Vw is the set of ˜ucas numbers Ofor n ≥ aP[ yf R
is an integerT then the two systems Ut and Vt are the sameT the standard
RWary numeration system[
 ab

6.3 Conversion in the Pisot case

Now we suppose that R is a Pisot number[

Proposition 3. Let R be a Pisot number such that its beta-polynomial
KOXP is equal to its minimal polynomial. Let U be any linear sequence
with characteristic polynomial equal to KOXP xin particular Uty. The con-
version from the linear numeration system Vt to the linear numeration
system U xand converselyy is computable by a ﬁnite automaton.

Proof. yt comes from the fact that U and Vt have the same characteristic
polynomialT which is the minimal polynomial of a Pisot number[ Thus
normalization in both systems is computable by a ﬁnite automaton on
any alphabetT and the result follows by Theorem a[ ⊓⊔

7 Multiplicatively dependent numeration systems

virst recall that if R is a Pisot number of degree m thenT for any positive
integer kT Rk is a Pisot number of degree m Osee [a]P[ Two Pisot numbers
R and S are said to be multiplicatively dependent if there exist two positive
integers k and P such that Rk m Sr[ Then R and S have the same degree
m[

Theorem 2. Let R and S be two multiplicatively dependent Pisot num-
bers. Let U and Y be two linear sequences with characteristic polynomial
equal to the minimal polynomial of R and S respectively. Then the con-
version from the Y -numeration system to the U -numeration system is
computable by a ﬁnite automaton.

Proof. Set Z m Rk m Sr[ qs aboveT let Vt mOvnPn≥0 with v0 m a and
vn m Rn
1 S ··· S Rn
m for n ≥ a[ The conjugates of Z are of the form
Zi m Rk
i T for b ≤ i ≤ m[ Set W mOwnPn≥0 with wn m Zn
1 S ··· S
Zn
m for n ≥ a[ Then W is the ˜ucasWlike numeration system associW
ated with Z[ NowT for n ≥ aT wn m vkn[ Thus any W Wrepresentation
of an integer N of the form ON PW m dk ··· d0 gives a VtWrepresentation
ON PVβ m dk]k−1dk−1]k−1 ··· d1]k−1d0T and thus the conversion from W W
representations to ˜ucasWlike VtWrepresentations is computable by a ﬁnite
automaton[ The same is true for the conversion from W Wrepresentations
to VxWrepresentations[ ry Proposition c the conversion from Y to VxT and
that from Vt to U are computable by a ﬁnite automatonT and the result
follows[ ⊓⊔

ac

q set S of natural numbers is said to be U -recognizable if the set
{snuU | n ∈ S} of normal U Wrepresentations of the elements of S is
recognizable by a ﬁnite automaton[ The following result is an immediate
consequence of Theorem b[

Corollary 1. Let R and S be two multiplicatively dependent Pisot num-
bers. Let U and Y be two linear sequences with characteristic polynomial
equal to the minimal polynomial of R and S respectively. Then a set which
is U -recognizable is Y -recognizable as well.

8 Periodic points

˜et R be a Parry number[ The betaWshift St is soﬁcT i.e. the set of its
ﬁnite factors is recognizable by a ﬁnite automatonT and periodic points
of St are periodic biWinﬁnite words that are labels of biWinﬁnite paths in
the automaton that recognizes it[
The determination of the number of periodic points of the betaWshift
St is importantT because the entropy of St is equal to

hOStP m lim
n→∞ a
n log PernOStP m log R

see [aiT Th[ d[c[f][
Note thatT for any prime qT PerqOStP ≡ Per1OStP mod qT see [bc][
yn the sequelT we assume that the minimal polynomial P OXP of R
and its betaWpolynomial KOXP are identicalT of degree m[ qs aboveT let
Vt mOvnPn≥0 with vn m Rn S Rn
2 S ··· S Rn
m for n ≥ a[

8.1 The ﬁnite type case

yf dtOaP m t1 ··· tN T then St is a system of ﬁnite type[ We construct an
automaton At which recognizes the set of factors of St[ There are N
states q1T [ [ [ T qN [ vor each iTa ≤ i s Nℓ there is an edge labelled ti from
qi to qi+1[ vor a ≤ i ≤ N T there are edges labelled by ]T aT [ [ [ T ti − a
from qi to q1[ The adjacency matrix of At is the companion matrix M of
KOXPT deﬁned byT for a ≤ i ≤ N
M [iℓ a] m ti
M [iℓ i S a] m a

and other entries equal to ][
 ad

Proposition 4. Let R be a Parry number such that dtOaP m t1 ··· tN .
Then for n ≥ a, vn m trace OM nP m PernOStP.

Proof. Since M is the adjacency matrix of a system of ﬁnite typeT the
number of periodic points of period n in St is equal to trace OM nPT see for
instance [ai][ On the other handT since M is the companion matrix of the
minimal polynomial of RT we have that trace OMnPm Rn
1 S ··· S Rn
N m vn
for n ≥ a[ ⊓⊔

Corollary 2. When dtOaP is ﬁnite, the Lucas-like sequence Vt is exactly
realized by the beta-shift St.

8.2 The inﬁnite soﬁc case

This is the case when dtOaP m t1 ··· tN OtN +1 ··· tN +pPv[ We construct an
automaton At which recognizes the set of factors of St[ There are N S p
states q1T [ [ [ T qN +p[ vor each iTa ≤ i s N S pℓ there is an edge labelled
ti from qi to qi+1[ There is an edge labelled tN +p from qN +p to qN +1[ vor
a ≤ i ≤ N S pT there are edges labelled by ]T aT [ [ [ T ti − a from qi to q1[
The adjacency matrix of At is the matrix M deﬁned by for a ≤ i ≤ N S p

M [iℓ a] m ti
M [iℓ i S a] m a for i ̸m N S p

M [N S pℓ N S a] m a

and other entries equal to ][

Proposition 5. Let R be a Parry number such that

dtOaP m t1 ··· tN OtN +1 ··· tN +pP
vb

Then for n ≥ a, vn m trace OM nP.

Proof. Remark that M is not the companion matrix of P OXP[ The comW
panion matrix z is in that case the following one

z[iℓ a] m ti for a ≤ i ≤ p − a

z[pℓ a] m tp Sa

z[iℓ a] m ti − ti−p for p Sa ≤ i ≤ N S p

z[iℓ i S a] m a for a ≤ i ≤ N S p

and other entries equal to ][ ry a straightforward computationT it is
possible to show that the matrices M and z are similar[ More preciselyT

ae

there exists a matrix Z such that M m Z−1zZT where Z is deﬁned byT
for a ≤ iℓ j ≤ N S p

Z[iℓ j] m a if i ≡ j mod p and i ≥ j

m ] otherwise

Therefore trace OM nP m trace OznPm Rn
1 S ··· S Rn
N +p m vn for n ≥ a[ ⊓⊔

sontrarily to what happens in the case where the system is of ﬁnite
typeT in the soﬁc case diEerent loops in the automaton At may have the
same labelT see Section i[b for the quadratic case[ So PernOStP is not equal
to vn[

Proposition 6. Let R a Parry number such that

dtOaP m t1 ··· tN OtN +1 ··· tN +pP
vb

Then for n ≥ a,
 PernOStPm vn − p if p divides n

PernOStPm vn otherwiseb

Proof. Recall that dtOaP is strictly greater in the lexicographic order slex
than the shifted sequences QiOdtOaPP for iu aT [ba][
virstT suppose that for each iTa ≤ i ≤ pT tN +i st1[ Then in the automaW
ton At there are two loops with label tN +1 ··· tN +pT one starting from
state q1 and the other one from state qN +1[
SecondT suppose that there exists a ≤ isp maximum such that t1 ··· ti m
tN +1 ··· tN +i m w[ Then necessarily tN +i+1 sti+1[ Thus there is a path

q1 w
−→ qi+1 tN +i+1
−→ q1

and since tN +i+2 ··· tN +p slex t1 ··· tp−i−1T there is a loop with label
tN +i+2 ··· tN +p from q1[ Thus there are two loops with label tN +1 ··· tN +p[
So there are p times two loops with same labelT a circular permutation of
the word tN +1 ··· tN +p[ Thus when counting the periodic biWinﬁnite words
in the automaton that are labels of loopsT we must remove p of them each
time the period is a multiple of p[ ⊓⊔

Corollary 3. The sequence Rt mOrnPn≥1 deﬁned by r0 ma, and for
n ≥ a, rn m vn − p if p divides n and rn m vn otherwise, is exactly
realized by the soﬁc beta-shift St.
 af

Proposition 7. The sequence Rt is a linear recurrent sequence, of char-
acteristic polynomial OXp − aPKOXP.

Proof. ˜et us rewrite the minimal polynomial of R as KOXPm XN +p −
a1X N +p−1 − · · · − aN +p[ xenceT for n ≥ N S p S aT

vn m a1vn−1 S ··· S aN +pvn−N −pb

Suppose that p does not divide n[ Then

rn m vn m ∑

1≤i≤N +p
p̸ |n−i
 airn−i S ∑

1≤i≤N +p
p|n−i
 aiOrn−i S pPb

Thus rn m ∑

1≤i≤N +p airn−i S ∑

1≤i≤N +p
p|n−i
 pb OaP

Similarly rn−p m ∑

1≤i≤N +p airn−p−i S ∑

1≤i≤N +p
p|n−p−i
 pb

ThereforeT since the two last sums in rn and rn−p respectively are equalT

rn mO ∑

1≤i≤N +p airn−iPS rn−p − ∑

1≤i≤N +p airn−p−ib

yf p divides n then

rn m −p S ∑

1≤i≤N +p airn−i S ∑

1≤i≤N +p
p|n−i
 p ObP

and the result follows as above[ xence the characteristic polynomial of
Rt is equal to OXp − aPKOXP[ ⊓⊔

Proposition 8. The set GORtP of normal Rt-representations of the nat-
ural numbers is not recognizable by a ﬁnite automaton.

Proof. Suppose that GORtP is recognizable by a ﬁnite automaton[ Then
the set H m {⟨rn − a⟩Rβ | n ≥ a}

of words of GORtP that are maximal for the lexicographic order is recogW
nizable by a ﬁnite automaton as wellT see [bf][ yt is also knownT by [ah]T

ag

that the normal RtWrepresentation of rn − aT for n large enoughT beW
gins with a preﬁx of the form t1 ··· tN OtN +1 ··· tN +pPj for some inteW
ger jT because R is the dominant root of the characteristic polynomial
JOXP m OXp − aPKOXP of RtT and dtOaP m t1 ··· tN OtN +1 ··· tN +pPv[
tenote by K′OXP the opposite of the reciprocal polynomial of KOXPT
K ′OXPm −aS t1X S ··· S tp−1X p−1 SOtp S aPXp SOtp+1 − t1PXp+1 S
··· SOtN +p − tN PXN +pb SimilarlyT let J ′OXPm K′OXP − XpK ′OXP[
ry a direct computationT one getsT for each j ≥ a

J ′OXP S bXpJ ′OXPS ··· SOj S aPXpj J ′OXPm

K ′OXPS XpK ′OXPS ··· S XpjK ′OXP − Oj S aPXp(j+1)K ′OXP OcP

We introduce a notationj if w m w0 ··· wn is a wordT ℓOwPm w0 S w1X S
··· S wnX n is the polynomial associated with w Owith increasing powersP[
The signed digit −d is denoted by ¯d[ We then getT for each j ≥ a

K ′OXPS XpK ′OXPS ··· S XpjK ′OXPm

ℓO¯at1 ··· tN OtN +1 ··· tN +pP
j+1PS X p(j+1)ℓOa ¯t1 ··· ¯tN P OdP

Case 1[ p ≥ N S a[
vrom uq[ OcP and OdP follows thatT for n m N SpOj SbPSPT with a ≤ P ≤ pT
rn − a has a RtWrepresentation of the form

Orn − aPRβ m t1 ··· tN OtN +1 ··· tN +pP
jw(n)

where w(n) is a word of length bp S PT corresponding to the polynomial

W (n)OXPm tN +1 S tN +2X S ··· tN +pX p−1

S X p−N −1 − t1X p−N − · · · − tN X p−1

− Oj S aPXp−N −1K ′OXP − X2p+r−1b OeP

The diEerence between W (N +p(j+3)+r) and W (N +p(j+2)+r) is equal to
−X p−N −1K ′OXP[ The word associated with −Xp−N −1K ′OXP is of the
form s m]p−N −1a ¯t1 ··· tp−1O−tp − aPOt1 − tp+1P ··· OtN − tN +pP]rT and the
value of s in the system Rt is equal to URβ OsPm rN +p+r − t1rN +p+r−1 −
··· − tp−1rN +r+1 − Otp S aPrN +r SOt1 − tp+1PrN +r−1 S ··· SOtN − tN +pPrr[
Suppose that N S p S P is not divisible by p[ vrom uq[ OaP follows that
URβ OsP is equal to the positive constant

zOPPm ∑

1≤i≤N +p
p|N +r−i
 pb

ah

vor a ≤ P ≤ p ﬁxed such that N S p S P is not divisible by pT let IOPPm
{n ∈ N | n m N S pOj S bP S Pℓ j ≥ a}[ ˜et aOnPm URβ Ow(n)P[ The family
OaOnPPn∈I(r) is thus strictly increasing[ Remember that the length |w(n)|
is equal to bp S P[
yf aOnP sr2p+rT then the normal RtWrepresentation of rn − a is of the
form ⟨rn − a⟩Rβ m t1 ··· tN OtN +1 ··· tN +pPjz(n) where z(n) is a word of
length bp S PT equal to the normal RtWrepresentation of w(n)T preﬁxed by
an adequate number of ]’s[
yf aOnP ≥ bp S PT then let h be the smallest positive integer such that
URβ OOtN +1 ··· tN +pPhw(n)P srp(h+2)+r[ Then

⟨rn − a⟩Rβ m t1 ··· tN OtN +1 ··· tN +pP
j−hz(n)

where z(n) is a word of length pOh S bP S P that is the normal RtW
representation of OtN +1 ··· tN +pPhw(n)[ vrom this follows that the set
{⟨rn − a⟩Rβ | n ∈ IOPP} is not recognizable by a ﬁnite automatonT and so
it is for the set H itself[

Case 2[ psN S a[
˜et k be the smallest integer ≥ b such that N Sa ≤ kp[ Then from uq[ OcP
and OdP follows thatT for n m N S pOj S bP S PT with a ≤ P ≤ pT rn − a has
a RtWrepresentation of the form

Orn − aPRβ m t1 ··· tN OtN +1 ··· tN +pP
j+1−kw(n)

where w(n) is a word of length pOkSaPSPT corresponding to the polynomial

W (n)OXP m OtN +1 S tN +2X S ··· tN +pX p−1POa S X S ··· S XkP

S X kOXp−N −1 − t1X p−N − · · · − tN X p−1P

− Oj S aPK′OXPXpk−N −1 − X p(k+1)+r−1b OfP

With the same reasoning as in sase aT we show that H is not recogW
nizable by a ﬁnite automaton[ ⊓⊔

9 Example : the quadratic case

xere we are interested only in the case where the root R u a of the
polynomial P OXPm X2 − aX − bT with a and b in ZT is a Parry numberT
which is the case only if a ≥ b ≥ aT or if a ≥ c and −a Sb ≤ b ≤−a[
Note that R is in fact a Pisot number[ We denote the conjugate of R by
R′T |R′| s a[
 ai

9.1 The ﬁnite type case

Suppose that a ≥ b ≥ a[ Then the RWexpansion of a is dtOaP m abT and
the canonical alphabet is xt m {]ℓ b b b ℓ a}[ vorbidden words are those
containing a factor in the ﬁnite set I m {abℓ aOb S aPℓ b b b ℓ aa}T hence the
dynamical system St associated with R is of ﬁnite type[ yt is the set of
biWinﬁnite sequences in the automaton described in vigure b[

1 2

0, . . . , a ! 1 a

0, . . . , b ! 1

Fig. 2. Automaton in the ﬁnite type case

The matrix M of St is
 M m ( a a
b ]
 )

The vibonacciWlike sequence Ut is deﬁned by un m aun−1 S bun−2 for
n ≥ bT with u0 m a and u1 m a S a[
The ˜ucasWlike sequence Vt is deﬁned by vn m avn−1Sbvn−2 for n ≥ cT
with v0 m aT v1 m R S R′ m a and v2 m R2 S R′2 m a2 Sbb[ yn the special
case in which a m b m a OvibonacciPT this deﬁnition gives v0 m v1 m aT
which is not allowedT since the sequence must be stricly increasing[ This
case has been handled in Section c[
Note thatT for n ≥ a

vn m a − bb
a − b Sa un S ba Sbb − ab
a − b Sa un−1b

The sequence Vt is exactly realizable[ yt is proved in [bc] that if a
and b are in NT if b m a2 Sdb is not a squareT and if a and a2 Sbb are
relatively primeT then a sequence V satisfying the polynomial P is exactly
realizable if and only if v2
v1 m a2+2b
a [
b]

9.2 The inﬁnite soﬁc case

Suppose that a ≥ c and −aSb ≤ b ≤−a[ Then dtOaP m Oa−aPOaSb−aPv

and the canonical alphabet is xt m {]ℓ b b b ℓ a − a}[ The dynamical system
St associated with R is soﬁc j it is the set of biWinﬁnite sequences in the
automaton described in vigure c[ q word is forbidden if and only if it
contains a factor in the set I m {Oa − aPOa S b − aPnd | a S b ≤ d ≤
a − aℓn ≥ ]}T which is recognizable by a ﬁnite automaton[

1 2

0, . . . , a ! 2 a ! 1

0, . . . , a + b ! 2

a + b ! 1

Fig. 3. Automaton in the soﬁc case

The matrix M of St is

M m ( a − aa
a S b − aa
 )

The companion matrix of R is
 z m ( a a
b ]
 )

The vibonacciWlike sequence Ut is deﬁned by un m aun−1 S bun−2 for
n ≥ bT with u0 m a and u1 m a[
The ˜ucasWlike sequence Vt is deﬁned by vn m avn−1Sbvn−2 for n ≥ cT
with v0 m aT v1 m R S R′ m a and v2 m R2 S R′2 m a2 Sbb[
Note thatT for n ≥ a we have

vn mbun − aun−1b

We have thatT for n ≥ aT PernOStPm vn − aT since there are two
diEerent loops labelled by Oa S b − aP in the automaton of vigure cT one
from state a and the other one from state bT because ] sa S b − a ≤ a − b[
The sequence Rt mOrnPn≥0 deﬁned by

rn mOa S aPrn−1 SOb − aPrn−2 − brn−3

ba

for n ≥ cT and r0 m aT r1 m a − aT r2 m a2 Sbb − a and r3 m a3 Scab − aT
exactly realizes the betaWshift[

Example 1. Take a m c and b m −a[ Then R m 3+
√5
2 T dtOaP m bavT and
Ut m {aℓ cℓ hℓ baℓ eeℓ addℓ cggℓ b b b} is the sequence of vibonacci numbers
of even indexk Vt m {aℓ cℓ gℓ ahℓ dgℓ abcℓ cbbℓ b b b} is the sequence of ˜ucas
numbers of even index n for n ≥ a[ The sequence which exactly realizes
St is Rt m {aℓ bℓ fℓ agℓ dfℓ abbℓ cbaℓ b b b}[ The set H m {⟨rn − a⟩Rβ | n ≥ a}
is equal to H m {aℓ baℓ bb]ℓ babaℓ bab]]ℓ baab]aℓ baaaba]ℓ baaaabaaℓ
baaaaabb]ℓ baaaaab]]]ℓ b b b}[ □

10 Quadratic Pisot units

xere R is a quadratic Pisot unitT that is to say the root u a of the
polynomial P OXPm X2 − aX − aT with a ≥ aT or of the polynomial
P OXPm X2 − aX S aT with a ≥ c[ yn that case there are nice properties
connecting the numeration in the systems Ut and Vt and in base R[ yt
is known thatT when R is a quadratic Pisot unitT every positive integer
has a ﬁnite RWexpansion [ae]T the conversion from UtWrepresentations to
RWrepresentations folded around the radix point is computable by a ﬁnite
automaton [ad]T and this property is characteristic of quadratic Pisot
units [af][
qs an exampleT we give in Table b the XWexpansions of the ﬁrst inteW
gers[
 N ϕ-expansions
1 1.
2 10.01
3 100.01
4 101.01
5 1000.1001
6 1010.0001
7 10000.0001
8 10001.0001
9 10010.0101
10 10100.0101
11 10101.0101

Table 2. ϕ-expansions of the 11 ﬁrst integers

We now make the link with the ˜ucasWlike numeration Vt[

bb

10.1 Case β2 = aβ +1

virst suppose that a ≥ b[ The following result is a simple consequence of
the fact that for n ≥ aT vn m Rn S R′n and that R′ m −R−1[

Lemma 1. Let y be a ﬁnite alphabet of digits containing xVβ . If ON PVβ m
dk ··· d0, with di ∈ y, then ON Pt m dk ··· d0. ¯d1d2 ¯d3 ··· O−aPkdk.

Note that the digits in ON Pt are elements of the alphabet ˜y m {dℓ ¯d | d ∈
y}[ Then the RWexpansion of N is obtained by using the normalization
Vt, ˜BN Owhich is computable by a ﬁnite automatonP[

Now we treat the case a m a[ The connection between ˜ucas repreW
sentations and representations in base the golden mean X is the following
one[

Lemma 2. Let y be a ﬁnite alphabet of digits containing xL. If ON PL m
dk ··· d1, with di ∈ y, then ON Pw m dk ··· d1]. ¯d1d2 ··· O−aPkdk.

qs aboveT the XWexpansion of N is obtained by using the normalization
Vw, ˜BN[

10.2 Case β2 = aβ ! 1

Then dtOaP m Oa − aPOa − bPv[
The following lemma is just a consequence of the fact that for n ≥ aT
vn m Rn S R′n and that R′ m R−1[

Lemma 3. Let y be a ﬁnite alphabet of digits containing xVβ . If ON PVβ m
dk ··· d0, with di ∈ y, then ON Pt m dk ··· d0.d1 ··· dk.

Proposition 9. If dk ··· d0 is the normal Vt-representation of N then
dk ··· d0.d1 ··· dk is the R-expansion of N .

Proof. Note that GOVtPm {w ∈ GOUtP | w ̸m w′Oa − aPOa − bPnℓn ≥
a}[ NowT it is enough to show that if w m dk ··· d0 is in GOVtPT then
dk ··· d1d0d1 ··· dk contains no factor in I m {Oa−aPOa−bPnOa−aP | n ≥ ]}[
virstT w has no factor in I since GOVtP ⊂ GOUtP[ SecondT d0d1 ··· dk has
no factor in I eitherT because I is symmetrical[ ThirdT suppose that g m
dk ··· d1d0d1 ··· dk is of the form g m g′Oa − aPOa − bPj Oa − bPn−jOa − aPg′′T
with w m g′Oa − aPOa − bPj[ Then wc∈ GOVtPT a contradiction[ ⊓⊔

bc

References

1. M.-J. Bertin, A. Decomps-Guilloux, M. Grandet-Hugot, M. Pathiaux-Delefosse,
J.- P. Schreiber, Pisot and Salem numbers, Birkh˝auser, 1992.
2. A. Bertrand, D«eveloppements en base de Pisot et r«epartition modulo 1. C.R.Acad.
Sc., Paris 285 (1977), 419—421.
3. A. Bertrand-Mathis, Comment «ecrire les nombres entiers dans une base qui n’est
pas enti‘ere. Acta Math. Acad. Sci. Hungar. 54 (1989), 237—241.
4. A. B‘es, An extension of the Cobham-Sem‹enov Theorem. Journal of Symbolic Logic
65 (2000), 201—211.
5. J. R. B˝uchi, Weak second-order arithmetic and ﬁnite automata. Z. Math. Logik
Grundlagen Math. 6 (1960), 66—92.
6. V. Bruy‘ere and G. Hansel, Bertrand numeration systems and recognizability. The-
oret. Comp. Sci. 181 (1997), 17—43.
7. A. Cobham, On the base-dependence of sets of numbers recognizable by ﬁnite
automata. Math. Systems Theory 3 (1969), 186—192.
8. F. Durand, A generalization of Cobham’s Theorem. Theory of Computing Systems
31 (1998), 169—185.
9. S. Eilenberg, Automata, Languages and Machines, vol. A, Academic Press, 1974.
10. S. Fabre, Une g«en«eralisation du th«eor‘eme de Cobham. Acta Arithm. 67 (1994),
197—208.
11. A.S. Fraenkel, Systems of numeration. Amer. Math. Monthly 92(2) (1985), 105—
114.
12. Ch. Frougny, Representation of numbers and ﬁnite automata. Math. Systems The-
ory 25 (1992), 37—60.
13. Ch. Frougny, Conversion between two multiplicatively dependent linear numera-
tion systems. In Proceedings of LATIN 02, Lectures Notes in Computer Science
2286 (2002), 64—75.
14. Ch. Frougny and J. Sakarovitch, Automatic conversion from Fibonacci represen-
tation to representation in base ϕ, and a generalization. Internat. J. Algebra
Comput. 9 (1999), 351—384.
15. Ch. Frougny and B. Solomyak, On Representation of Integers in Linear Numer-
ation Systems, In Ergodic theory of Z
d-Actions, edited by M. Pollicott and K.
Schmidt, London Mathematical Society Lecture Note Series 228 (1996), Cam-
bridge University Press, 345—368.
16. Ch. Frougny and B. Solomyak, On the context-freeness of the θ-expansions of the
integers. Internat. J. Algebra Comput. 9 (1999), 347—350.
17. G. Hansel, Syst‘emes de num«eration ind«ependants et synd«eticit«e. Theoret. Comp.
Sci. 204 (1998), 119—130.
18. M. Hollander, Greedy numeration systems and regularity. Theory of Computing
Systems 31 (1998), 111—133.
19. D. Lind and B. Marcus, An Introduction to Symbolic Dynamics, Cambridge Uni-
versity Press, 1995.
20. M. Lothaire, Algebraic Combinatorics on Words, Cambridge University Press,
2002.
21. W. Parry, On the β-expansions of real numbers. Acta Math. Acad. Sci. Hungar.
11 (1960), 401—416.
22. Y. Puri and T. Ward, A dynamical property unique to the Lucas sequence. Fi-
bonacci Quartely 39 (2001), 398—402.

bd

23. Y. Puri and T. Ward, Arithmetic and growth of periodic orbits. J. of Integer
Sequences 4 (2001), Article 01.2.1.
24. A. R«enyi, Representations for real numbers and their ergodic properties. Acta
Math. Acad. Sci. Hungar. 8 (1957), 477—493.
25. A. L . Sem‹enov, The Presburger nature of predicates that are regular in two num-
ber systems. Siberian Math. J. 18 (1977), 289—299.
26. J. Shallit, Numeration systems, linear recurrences, and regular sets. Inform. Com-
put. 113 (1994), 331—347.
 be
