<!-- source: https://www.math.umd.edu/~laskow/713/Spring17/juliarobinson.pdf | converted from PDF -->

THE JOURNAL or SYMBOLIC LOGIC
Volume 14, Number 2, June 1949

DEFINABILITY AND DECISION PROBLEMS IN ARITHMETIC

JULIA ROBINSON

Introduction. In this paper, we are concerned with the arithmetical defin-
ability of certain notions of integers and rationals in terms of other notions.
The results derived will be applied to obtain a negative solution of corresponding
decision problems.1

In Section 1, we show that addition of positive integers can be defined arith-
metically in terms of multiplication and the unary operation of successor <S
(where Sa = a + 1). Also, it is shown that both addition and multiplication
can be defined arithmetically in terms of successor and the relation of divisibil-
ity | (where x\y means x divides y). Thus the elementary theory of integers
with S and • (or &and |) as the only primitive notions, which may seem rather
narrow, is sufficient to express every idea or result which can be expressed in
elementary number theory, i.e., the arithmetic of integers with + and •. An
axiomatic problem concerning the system of positive integers with S and • is
discussed in Section 2.
In Section 3, we show that the notion of an integer can be defined arithmeti-
cally in terms of the notion of a rational number and the operations of + and •
on rationals. Hence the arithmetic of rationals is adequate for the formulation
of all problems of elementary number theory.
Since the solution of the decision problem is known to be negative for ele-
mentary number theory, it follows from our results that the solution of the de-
cision problem is negative for any of the related theories mentioned above.
As a further consequence, we see that the solution of the decision problem for
the arithmetical theory of arbitrary fields is also negative. These problems will
be discussed in Section 4.
The way in which we use the terms "arithmetic," "arithmetical or elementary
theory," and "arithmetical definability" calls for some comments. For example,
by the arithmetic (or elementary theory) of integers, we mean that part of the
general theory of integers which can be developed without using any notions of
a set-theoretical nature; that is, the part of the theory which can be formalized
within the lower predicate calculus. Thus in formulating statements of the
arithmetic of integers, we use only variables representing arbitrary integers;
logical constants of the lower predicate calculus: A (and), v (or), ~ (not), —•
(if, then), <-» (if and only if), A (for every), V (there exists), = (equals); and
mathematical constants denoting individual integers such as 0 and 1, relations
between integers such as < , and operations on integers such as + and • .
The notion of arithmetical definability will be explained by means of examples.

Received September 28, 1948.
1 This paper was submitted as a dissertation in partial fulfillment of the requirements
for the degree of Doctor of Philosophy at the University of California. I wish to express
my appreciation for the many helpful suggestions of Professor Alfred Tarski, under whose
direction the thesis was written. I am particularly indebted for his assistance in preparing
Section 4.  98

use, available at https:/www.cambridge.org/core/terms. https://doi.org/10.2307/2266510
Downloaded from https:/www.cambridge.org/core. University of Maryland - University Libraries, on 06 Apr 2017 at 13:15:42, subject to the Cambridge Core terms of

DEFINABILITY AND DECISION PROBLEMS IN ARITHMETIC 9 9

By saying for instance that addition of positive integers is arithmetically de-
finable in terms of • and S, we mean that there is a formula <j>  with the following
properties:
(i) <t>  is a formula of the elementary theory of positive integers with S and • as
the only mathematical constants (thus <f>  contains only variables representing
positive integers, the logical constants listed above and the mathematical
constants S and •)•
(ii) </> contains three distinct free variables say x, y and z?
(iii) (j>  is satisfied by those and only those ordered triples of integers (x, y, z)
for which x + y = z? A formula <j>  with this property may be referred to as a
defining formula for + in terms of • and S. As we shall see in Section 1 such
a defining formula actually exists, in fact we can take for <f>  the formula

S(x-z)-S(yz) = S(z-z-S(x-y)).

To give another example, the formula

(1) M x = y -\- y

of the elementary theory of positive integers is satisfied by those and only those
positive integers x which are even. Hence this formula shows that the notion
of an even integer is arithmetically definable in terms of addition. Now con-
sider the formula

(2) A  ([2«Q  A A (y«A  •-» y + 2«Q)] -* *«G).
Q

This formula differs from (1) in that besides variables representing positive
integers, it also contains a bound variable representing sets of integers; and in
addition to logical constants of the lower predicate calculus it also contains the
symbol « denoting the membership relation. On the other hand (2) like (1)
contains only one free variable x and is satisfied by those and only those positve
integers which are even. If we knew only (2) without knowing (1), we could
just say that the notion of an even integer is recursively definable (or recursively
arithmetically definable) in terms of addition.
In this example, the explicit arithmetical definition is the simplest and most
natural one; in other cases, set-theoretical or in particular recursive definitions
may be easy while an explicit arithmetical definition is either impossible or hard
to find.
The problem of the axiomatic foundation of the discussion will be disregarded
in Sections 1 and 3. Thus when stating that a formula is a theorem, we do not
try to derive this formula from any axioms but merely to show that it is true in
the intuitive sense and can be so recognized by mathematicians. It will be

' No attempt is made in this paper to present the metamathematical fragments of the
discussion in a rigorous, formal way or to carry through a sharp distinction between meta-
mathematical and mathematical notions. In particular, quotation marks are omitted
in most cases since we believe no confusion will arise from this negligence.
3 For a precise formal definition of the notion of satisfaction and truth, see Tarski [10].

use, available at https:/www.cambridge.org/core/terms. https://doi.org/10.2307/2266510
Downloaded from https:/www.cambridge.org/core. University of Maryland - University Libraries, on 06 Apr 2017 at 13:15:42, subject to the Cambridge Core terms of

100  JULIA ROBINSON

seen that the question of axiomatization will play a rather restricted r61e even
in the results established in Section 4.

1. Problems of definability in the arithmetic of integers. In developing the
arithmetic of positive integers, we usually consider addition and multiplication
as fundamental operations. It is known that a great variety of other arith-
metical notions are (explicitly) arithmetically definable in terms of these opera-
tions. The problem arises whether one of these operations is definable in terms
of the other. Consider first the problem of defining • in terms of + . It is
obvious that • can be denned recursively in terms of + ; we first define 1 as the
positive integer which is not the sum of two positive integers and then use
the familiar recursive definition of multiplication.
The situation changes if we are interested in the arithmetical definability of
multiplication in terms of addition. From a result of Presburger [8], we can
easily obtain a detailed description of all relations between integers and opera-
tions on integers which can be defined arithmetically in terms of + ; and we do
not find • among them. It is easily seen that + is not definable in terms of •
in any sense of the word definable. For the system of positive integers has auto-
morphisms with respect to multiplication which permute the primes in an
arbitrary way, so that sum is certainly not preserved. This method of proof is
due to Padoa [7].
Among the notions which are arithmetically definable in terms of addition,
we find the relation < in terms of which the successor operation is arithmetically
definable. Conversely, + can be defined in terms of < and < in terms of S
by means of recursive definitions. However by an argument exactly analogous
to that referred to above to show that • is not arithmetically definable in terms
of + , it can be shown that + is not arithmetically definable in terms of < and
that < , hence also + , is not arithmetically definable in terms of S.
4,

We can now ask the question whether addition is arithmetically definable
in terms of one of these weaker notions combined with multiplication. In this
connection we obtain:

THEOREM 1.1. Addition of positive integers is arithmetically definable in terms
of multiplication and the successor operation as well as in terms of multiplication
and the relation of less-than.
Proof. It is easily seen that for any three positive integers, we have a + b =
c if and only if a, b, and c satisfy the following formula:

(1) S(a-c)-S(b-c) = S[(c-c)-S(a-b)].

To verify this, write formula (1) using ordinary mathematical notation:

(1 + ac) (1 + be) = 1 + c* (1 + ab).

Multiplying out and cancelling terms appearing on both sides of the equation,
we have (a + b)c = c
2. Since c is a positive number, this is true if and only if
a + b = c.
From this argument it follows at once that + is arithmetically definable in

4 This follows from the results discussed in Hilbert-Bernays [6], vol. I, pp. 234-264.

use, available at https:/www.cambridge.org/core/terms. https://doi.org/10.2307/2266510
Downloaded from https:/www.cambridge.org/core. University of Maryland - University Libraries, on 06 Apr 2017 at 13:15:42, subject to the Cambridge Core terms of

DEFINABILITY AND DECISION PROBLEMS IN ARITHMETIC  101

terms of • and S. We now notice that (1) can be given the following equiva-
lent form:

V [S(a-b) = x A S(a-c) = y A S(b-c) = z A S([C-C]-X) = yz\.

This clearly remains valid if we eliminate the symbol S by replacing each par-
tial formula of the form
 Su = v
by  U < V A f\ ~( M < W A w < V).
w

In this way, we see that + is arithmetically definable in terms of • and < .
We can now try to improve the results obtained in Theorem 1.1 by replacing
multiplication by weaker notions. In the first place, we have in mind the re-
lation of divisibility. This relation is of course arithmetically definable in terms
of multiplication while it seems very likely that • is not arithmetically definable
in terms of |. It can be shown however that • can be defined set-theoretically
in terms of |. As an improvement of Theorem 1.1, we now obtain:
TFEOREM 1.2. Addition and multi-plication of positive integers are arithmeti-
cally definable in terms of the successor operation and the relation of divisibility.
Proof. It is clearly sufficient to show that • is arithmetically definable in
terms of | and S. We shall express the fact that two integers a and b are
relatively prime by a A. b and denote the least common multiple of two numbers
a and b by aob. Then the following equivalence holds in the arithmetic of posi-
tive integers:

(2) a • b = c *-* J\ (a\x A&|XAC|Z) V yy \[a±x^b±y^c±x^
x x.y.m

cij/Aiiy A m\S(aox) A m\S(boy)] —>

V [m\u A Su = cO(xOy)]}.
u
Suppose first that a-b — c and that x, y and m satisfy the conditions

aJ_£A&j_yAcJ_xAc_L.2/AxJLi/ A m|,s( aox) A m\S(bOy).

We must show that if a and b are not both 1, then

V[m|wA Su = (a-b)o(xOy)].
u

Now because of the conditions of relative primeness, we can replace the symbol o
by • throughout. Hence we must check that m\(ax + 1) and m\(by + 1) implies
that m\(abxy — 1). Writing this out in terms of congruences, we have
ox ss — 1 (mod TO) and by = — 1 (mod TO) implies abxy = + 1 (mod TO),
which certainly holds.
Conversely, suppose the right side of (2) holds and show that a-b = c. Notice
first that c = 1 implies a = b = 1, for otherwise we may take x, y, and TO all
equal to 1 and obtain that there exists a u such that Su = 1, which is impossible.

use, available at https:/www.cambridge.org/core/terms. https://doi.org/10.2307/2266510
Downloaded from https:/www.cambridge.org/core. University of Maryland - University Libraries, on 06 Apr 2017 at 13:15:42, subject to the Cambridge Core terms of

102  JULIA ROBINSON

Hence consider the case when c is different from 1. Let m be prime to a and b.
Choose x and y prime to a, b, and c and to each other and such that

ax 5= — 1 (mod m),

by = — 1 (mod m).

This is possible since x and y are only restricted to belonging to certain residue
classes mod m which are prime to m. Now since m\ S(aOx) and m\ S(bOy) and
the right side of (2) holds, it follows that there is a u satisfying m\u A SU =
co(xOy) or in terms of congruences cxy = + 1 (mod m). Hence c = ab for
arbitrarily large values of m and thus c = ab.
The relation _L and the operation o are both arithmetically definable in terms of
divisibility. In fact, the following equivalences can be used as definitions:

a±b *-* / \ (x\a A x\b —* / \ x\y)

X V
and
 c = aob «-» y\ (o|x A &|x <-> c|x).

Hence we can eliminate the symbols _L and o from (2) and obtain a defining formula
for • in terms of S and |.
We might also try to improve Theorem 1.2 by replacing divisibility by the
relation of relative primeness. However I have not been able to determine
whether • is arithmetically definable in terms of ± and S or even in terms of _L
and + .
It is easy to see that Theorem 1.1 can be extended to the arithmetic of arbi-
trary (not only positive) integers and furthermore to the arithmetic of arbitrary
integral domains with unity, i.e., for every integral domain addition can be
defined arithmetically in terms of multiplication and the successor operation <S
with Sa = a + l.6 The definition of + in terms of • and S used in the proof of
Theorem 1.1 can easily be modified in order to make it apply to arbitrary inte-
gers or to the elements of arbitrary integral domains.
On the other hand, I have been unable to extend Theorem 1.2 to arbitrary
integers; the difficulty in this case reduces to that of defining the notion of a
positive integer in terms of | and S.

2. An axiomatic problem regarding the arithmetic of positive integers.
Whenever addition and multiplication can be defined in terms of other notions
of the arithmetic of positive integers, it is clearly possible to formulate an axiom
system for arithmetic involving these other notions as the only primitive ones.
This can be done in a mechanical way by simply eliminating + and • from any
of the familiar axiom systems involving only these two notions. The axioms
thus obtained are usually complicated and artificial, and the problem of finding
a simple and elegant axiom system of the kind desired may present considerable
difficulty. We shall consider here only one problem of this kind.

6 This improves an analogous result for the theory of abstract fields recently published
by B. A. Bernstein [1].

use, available at https:/www.cambridge.org/core/terms. https://doi.org/10.2307/2266510
Downloaded from https:/www.cambridge.org/core. University of Maryland - University Libraries, on 06 Apr 2017 at 13:15:42, subject to the Cambridge Core terms of

DEFINABILITY AND DECISION PROBLEMS IN ARITHMETIC 103

We start here with the familiar axiom system due to Peano. It contains four
primitive notions 1, S, •, and + and consists of the following axioms:

Al.

A2.

A3.

A4.

A5.

A6.

A7.
 A ~Sa = 1
a
A (Sa = Sb -> a = b)

(9(1) A A [9(a) -» 9(Sa)])
a
A a + 1 = Sa
a
A a + Sb = S(a + b)
a, 6
/\0' 1 = a
a
A a- Sb = (a-b) + a.
 -» A 9(a)
a

a.b

Here the induction principle A3 is an axiom-schema, that is an infinite system
of axioms. It is understood that the symbol 9(a) may be replaced by any
arithmetical formula containing just one free variable a, if suitable replacements
of 9(1) and 9(Sa) are also made.6

We put the induction principle in this form if we decide to formalize the
arithmetic of positive integers entirely within the lower predicate calculus.
If on the other hand we want to use set theory in developing the arithmetic of
positive integers, we replace the axiom-schema A3 by the following axiom:

A3'. A ([1 « A
 A A (« « A -» Sa e fi)] -» A a « Q).
a
In such a case, we can also replace A4—A7 by explicit set-theoretical defini-
tions of + and • .
By our Theorem 1.1, it follows that the symbol + may be eliminated from
Peano's axioms. This can be done mechanically by transforming A4, A5, and
A7 with the help of the formula defining + in terms of <S and • in the proof of
Theorem 1.1. We thus obtained the formulations:

A4'. /\S(a-Sa)-S(l-Sa) = S([Sa- Sa]- Sa)
a

AS'. /\[S(a-c)'S(b-c) = S[(c-e)-S(a-b)]-*

S(a-Sc)-S(Sb-Sc) = S([Sc- Sc]- S(a- Sb))]

AT. A S[(a-b)-(a-Sb)]-S[a-(a-Sb)] = S([(a-Sb)-(a-Sb)]-S[(a-b)-a]).
a.b

• We could consider a more general axiom schema in which 9(a) could be replaced by
any arithmetical formula containing in addition to a also other free variables b, c, ••-
(in which case the whole schema would have to be preceded by the quantifiers A&,e,...).
It is shown in Hilbert-Bernays [61, vol. I, p. 343, that this more general form of the induction
principle is actually no stronger than A3.

use, available at https:/www.cambridge.org/core/terms. https://doi.org/10.2307/2266510
Downloaded from https:/www.cambridge.org/core. University of Maryland - University Libraries, on 06 Apr 2017 at 13:15:42, subject to the Cambridge Core terms of

104  JULIA ROBINSON

In view of the character of the defining formula which is used, we have to add
one more axiom to guarantee the operational character of addition, i.e., the
uniqueness of the result of addition. This new axiom is:

A8. A {[S(a-c)-S(b-c) = S ([c-c]-S(a-b))

S(a-d)-S(b-d) = S([d-d]-S(a-b))]-*c = d).

A moment's reflection suffices to see that the axiom system consisting of Al
-A3, A4', A5', A6, AT, and A8 is equivalent to the original axiom system (when
supplemented by the definition of + in terms of • and S) and is adequate for the
development of the arithmetic of positive integers within the lower predicate
calculus. We shall refer to this axiom system as System ©; and shall use the
symbol ©' to denote the axiom system obtained from @ by replacing A3 by A3'.
We do not know whether the axioms of © or ©' are mutually independent.
We now want to consider another simpler axiom system with the same mathe-
matical constants as @ and which is also possibly an adequate basis for the de-
velopment of the arithmetic of positive integers. This system consists of the
old axioms Al, A2, A3, A6 and the following three new axioms:

A4". /\a-b = b-a
a,b

A5". A a-(b-c) = (a-b)-c
a,b,c

A7". A Sa-S(a-b) = S(a-S(b-Sa)).
a, 6

A4" and A5" are of course well-known consequences of the Peano axioms.
Axiom A7" is unfamiliar, but expresses the simple identity

(1 + a) (1 + ab) = 1 + a (1 + b (1 + a)).

The new axiom system will be referred to as System X; and by X' we shall
denote the system obtained from X by replacing A3 by A3'. We are interested
in whether Systems <S and X are equivalent (mutually derivable) and whether
consequently £ can actually serve as a basis for the arithmetic of integers.
The question can be answered affirmatively if we replace © and X by ©' and X'
and permit outselves to use set-theoretical devices in derivations. In fact, we
have:

THEOREM 2.1. Systems ©' and X' are equivalent.
Proof. The derivation of the axioms of X' from those of @' presents no diffi-
culty. By defining addition in an appropriate way, we can easily derive from
<£' all of Peano's axioms and hence we can obtain the axioms of X' by means of
the ordinary recursive procedure.
To derive the axioms of ©' from those of X' we proceed in the following way.
Since Al, A2, and A3' (i.e., "proper" Peano axioms) are available in X', we
introduce ordinary addition and multiplication by means of the usual recursive
definitions. Then we show by induction that the multiplication operation thus
defined satisfies the remaining axioms of ©'. The only thing that we do not
yet know is whether this recursive multiplication coincides with the operation •

use, available at https:/www.cambridge.org/core/terms. https://doi.org/10.2307/2266510
Downloaded from https:/www.cambridge.org/core. University of Maryland - University Libraries, on 06 Apr 2017 at 13:15:42, subject to the Cambridge Core terms of

DEFINABILITY AND DECISION PROBLEMS IN ARITHMETIC 10 5

of the axioms of X'. Hence the proof will be completed if we establish the fol-
lowing:
LEMMA. The only binary operation • defined on the positive integers and satisfy-
ing the following formulas for all positive integers
(i) o-l = a
(ii) ab = ba
(iii) a-(b-c) = (a-b)-c
(iv) Sa-S(a-b) = S(a-S(b-Sa))
is ordinary multiplication.
Proof. Let X denote ordinary multiplication, that is multiplication intro-
duced recursively. We need to show that for every a and b, ab = a X b.
We proceed by induction. Clearly o-l = l-o = o=lXo . Suppose that it
has been shown that m-n = m X n for m ^ a and for all n. We need to show
that Sa-n = Sa X n for all n. Let 01 be the set of all n such that Sa-n =
Sa X n.
We show first that the inductive hypothesis together with (i)-(iv) implies
that if b ( 01 then S(a Xb) e 91. Using the inductive hypothesis, we have from
(iv) that
 Sa-b = Sa X b -» Sa-S(a X b) = S(a X S(b X 5a)).

But since X also satisfies (iv), we have

Sa X S(a X b) = S(a X 5(6 X 5a)).

Therefore,
 Sa-b = SaXi»- * Sa- S(a X 6) = Sa X 5(a X 6),

and if 61 91 then 5(a X b)« 91.
Next we shall show that if m g a and 6 € 91, then m X 6 e 9l. Suppose
Sa-6 = Sa X t, then

So-(TO X 6) = Sa-(m-b) = (Sa-6)-m = ( & X i) X m = & X (m X 6).

Hence if b e iV, m X b t 01. Here we used (ii) and (iii) as well as the inductive
hypothesis.
Also for m ^ a, if TO X 6 « 01, then b t 91. Suppose TO ^ a and Sa- (m X b)
= SaX (mX b). Then

(Sa-b) X m = Sa-b-m = Sa-(m X b) = Sa X (TO X 6) = (5a X 6) X m.

Now using the cancellation law for ordinary multiplication we have 5a -b =
Sa X b. Therefore if m ^ a and m X b t 91 then b t 91.
We are now ready to show by induction in b that b t 9l. Suppose that for
all b < n, b e 9l, and show that n t 01. It is sufficient to consider n > 1, since
Sa-1 = Sa X 1 = 5a by (i).
CASE I. n and a relatively prime. Then there are r and s such that

S(a Xr) = nXs*r<n*s^a.

By the inductive hypothesis r e 01 since r < n. Hence S(a X r) t 01, that is
n X s t 91. But s g a, so n e 01.

use, available at https:/www.cambridge.org/core/terms. https://doi.org/10.2307/2266510
Downloaded from https:/www.cambridge.org/core. University of Maryland - University Libraries, on 06 Apr 2017 at 13:15:42, subject to the Cambridge Core terms of

106  JULIA EOBINSON

CASE II. n and a have a common factor k > 1. Say n = k X t with A; 5? a
and < < n. Hence by the inductive hypothesis, t « 91, and since A; ^ a this
implies A; X <« 91. But A; X t is just n, so n« 91.
We have just shown that ab = a X b for every o and 6. In the proof, we
have used various theorems from elementary number theory but these can all
be derived from Peano's axioms. The proof of our lemma and hence also of
Theorem 2.1 is thus complete.
We now return to the problem of equivalence of © and X on the basis of the
lower predicate calculus. This problem seems to be more difficult and is still
open. As in the proof of Theorem 2.1 we can easily deduce the axioms of X
from those of ©. Going in the opposite direction, we can easily derive A4'
and A7' from the axioms of X. However I have not been able to derive from
X either A5' or A8. In fact, I have not even been able to show that either the
cancellation law

(1) A (°" c = b-c—*a = b)
a,b,e

or all true equalities of the form

(2) a-fi - y

where a, 0, and y stand for arbitrary constant terms of the form 1, SI, SSI,
• • • are derivable from the axioms of Systems X. The only result which we know
in this connection is that all equalities (2) become derivable if we enrich X by
including the cancellation law (1). This can be shown by analyzing the proof
of Theorem 2.1, more specifically the lemma formulated there.

3. Problems of definability in the arithmetic of rationals. Given any state-
ment of the arithmetic of rational numbers with + and •, an equivalent state-
ment of integral arithmetic with the same fundamental operations can be found
by replacing each rational variable by the ratio of two integer variables, clear-
ing of fractions, and adjoining the condition that the denominators are not zero.
It is much less simple to determine whether with every statement of the arith-
metic of integers we can correlate an equivalent statement in the arithmetic
of rationals and whether consequently the arithmetic of rationals is adequate to
express all problems of elementary number theory.
The answer to this question is an affirmative one. To show this, it clearly
suffices to prove that the notion of an integer is (explicitly) arithmetically
definable in the arithmetic of rationals in terms of the operations + and •.
In establishing this result, we need not refrain from using any known theorem
concerning integers or rationals since, as was stated in the introduction, we are
disregarding here the problem of axiomatic foundations of our discussion. In
order to make the argument more easily readable, we shall use in it besides
the variables capital A, B, C, • • • representing arbitrary rationals also small
a, b, c, • • • which are assumed to be integers.

THEOEEM 3.1. (i) For a rational number N to be an integer it is necessary and
sufficient that it satisfy the following formula

use, available at https:/www.cambridge.org/core/terms. https://doi.org/10.2307/2266510
Downloaded from https:/www.cambridge.org/core. University of Maryland - University Libraries, on 06 Apr 2017 at 13:15:42, subject to the Cambridge Core terms of

DEFINABILITY AND DECISION PROBLEMS IN ARITHMETIC 107

A ({ ( V 2 + BZ
2 = X2 + A F
2) A / \ [( V 2 + ABM
2 + BZ
2

A..B X.Y.Z  M X,Y,Z

= X2 + A F
2) — ( V 2 + AB(ilf + l)2 + BZ
2 = X2 + A F
2)]}
x,r,z

— ( V 2 + ABW
2 + BZ
2 = X2 + AF2 )) .
x,r,z

(ii) Hence the notion of an integer and that of a positive integer is arithmetically
definable in terms of the notion of a rational and the operations of addition and
multiplication on rationals.
Proof, (i) Let 0(A, B, K) stand for

V 2 + ABK
2- + BZ
2 = X2 + AY
2.

x.r.z

Then we can rewrite the formula given in (i) as follows:
(1) A \(fKA, B, 0) A A [*(A, B, M) -><*>( A, B, M + 1)]) -»*(A, B,N)\.
A.S M
It may be noticed that our formula is closely related to the formula

A {[0tC?AA(Af eQ-+M + ltO)]-+NeQ\,
Q

which defines the notion of a non-negative integer set-theoretically.
We first show that any given integer N satisfies (1). In fact, suppose A and
B satisfy the hypothesis of (1),

(2) *{A, B, 0) A A [*(A, B, M) - 0(A, B, M + 1)].
M
If now N is a positive integer, then by induction it satisfies the conclusion of
(1), i.e., <f>(A, B, N). On the other hand, since N occurs in <j>(A,  B, N) only to
an even power, it is clear that
4>(A,B,-N)^<t,(A,B,N).

Thus if N is any integer and A and B satisfy (2), then #(A, B, N) holds; in
other words, N satisfies (1).
It is much harder to show that every rational number N which satisfies (1)
is an integer. We shall need several lemmas. The first two are special cases
of a general theorem of Hasse [5] which gives necessary and sufficient conditions
for rational representation of a rational number by a given quadratic form in
any number of variables.
7 The symbol (k/p) is the familiar Legendre symbol
giving the quadratic character of A; (mod p).

LEMMA 1. If p is a prime = 3 (mod 4) then X
2 + F
2 — pZ
2 represents  a non-
zero rational number M, if and only if M is not of the form

p-k-S
2 with (k/p) = 1

or k- S
2 with k = p (mod 8).

7 A forthcoming book by Gordon Pall, The arithmetical theory of quadratic forms,
will give an elementary account of the theory.

use, available at https:/www.cambridge.org/core/terms. https://doi.org/10.2307/2266510
Downloaded from https:/www.cambridge.org/core. University of Maryland - University Libraries, on 06 Apr 2017 at 13:15:42, subject to the Cambridge Core terms of

108  JULIA ROBINSON

LEMMA 2. / / p and q are odd primes with p = 1 (mod 4) and (q/p) = — 1,
then X2 + qY2 — pZ2 represents a non-zero rational number M if and only if M
is not of the form
 p-k-S
2 with (k/p) = - 1

or q-k-S2 with (k/q) = — 1.

LEMMA 3. If p is a prime = 3 (mod 4) then

2 + pM2 + pZ2 = X2 + Y2

has a solution for X, Y, and Z if and only if the denominator of M in lowest terms
is odd and prime to p.
Proof. Let M = n/d in lowest terms. Put m = 2d
2 + pn2. It is sufficient to
determine when m can be represented rationally by the form X2 + Y2 — pZ2.
Suppose that d is odd and prime to p. Then m is prime to p, so m is not of the
form p-k-S
2. Also m = 1, 2 (mod 4), so it is not of the form k- S2 with k = p
(mod 8) since p = 3 (mod 4). Hence by Lemma 1, m can be represented.
Suppose p\d and put d = pr. Then m = p-k where k = 2pr
2 + n2 is prime
to p, since we assumed that n/d is in lowest terms, so (k/p) = (n
2/p) = 1.
Thus, m is of the form p-k-S
2 with (k/p) = 1. Therefore by Lemma 1, TO is
not represented by X
2 + Y2 — pZ2.
Suppose 2\d and put d = 2s. Then m = 8s2 + pn2. But n is odd, so TO = p
(mod 8) and hence is not represented by the forms X2 + Y2 — pZ2.
LEMMA 4. If p and q are odd primes with p = 1 (mod 4) and such that (q/p)
= — 1, then
 2 + pqM2 + pZ2 = X2 + qY1

has a solution for X, Y, Z if and only if the denominator of M in lowest terms is
prime to p and q.
Proof. Let M = n/d in lowest terms and put TO = 2d
2 + pqn
2. It is sufficient
to check that TO is represented by the form X2 + qY2 — pZ2 if and only if d is
prime to p and q.
Suppose that d is prime to p and q, then TO is also prime to p and q. Hence
by Lemma 2, TO is represented by the form X2 + q Y
2 — pZ2.
Suppose that p\d and put d = pr, then TO = p-k where k = 2pr
2 + qn2.
Since qn
2 is prime to p, the quadratic character (k/p) = (qn
2/p) = (q/p) - — 1.
Hence TO is not represented by X2 + gF2 — pZ
2.
Similarly, suppose q\d and put d = qs. Then TO = gfc where k = 2gr
2 +
pn
2 and (k/q) = (pn
2/q) = (p/q) = (g/p) = —1 . Hence TO is not represented
by the given form.
LEMMA 5. / / p is a prime = 1 (mod 4), there is an odd prime q such that
(q/p) = -1 .
Proof. Let s be any non-residue of p. Then either s or s + p is odd and an
odd non-residue of p must have an odd prime factor which is also a non-residue
of p. Let this be q.
We are now ready to proceed with the proof of (i). We wish to show that if
N satisfies (1), then iV is an integer.

use, available at https:/www.cambridge.org/core/terms. https://doi.org/10.2307/2266510
Downloaded from https:/www.cambridge.org/core. University of Maryland - University Libraries, on 06 Apr 2017 at 13:15:42, subject to the Cambridge Core terms of

DEFINABILITY AND DECISION PROBLEMS IN ARITHMETIC 109

Consider first the case when A — 1 and B = p where p is any prime = 3
(mod 4). Lemma 3 states that 0(1, p, M) if and only if the denominator of M
in lowest terms is not divisible by 2 or p. Hence A = 1 and B = p satisfy (2)
since M and M + 1 have the same denominator and the denominator of 0
in lowest terms is ±1 . Therefore, if N satisfies (1), we must have 0(1, p, N).
Hence the denominator of N is not divisible by 2 or p. But this holds for any
prime s 3 (mod 4), hence the denominator of N is not divisible by 2 or by any
prime = 3 (mod 4).
Next let p be any prime = 1 (mod 4). Choose q by Lemma 5 to be an odd
prime such that (q/p) = — 1. Then, Lemma 4 states that 0(g, p, M) if and
only if the denominator of M in lowest terms is not divisible by p or q. Hence,
as before, A = q and B = p satisfy the condition (2) so that if N satisfies (1)
we must have <j>(q, p, N). Hence the denominator of N in lowest terms is not
divisible by any prime = 1 (mod 4).
Combining these results, we see that the denominator of N is not divisible by
any prime, and therefore must be ±1 . Hence N is an integer.
(ii) From the formula stated in (i) we can easily eliminate the symbols 1 and
2 and replace X2 by X X (cf. the proof of the second part of Theorem 1.1).
Hence the definability of integers in terms of the notion of a rational and the
operations of addition and multiplication follows at once.
To extend this result to the notion of a positive integer it is sufficient to recall
that the latter notion is definable in terms of that of an arbitrary integer and the
operations + and •; in fact, using the symbolic expression Int(A) to express
the fact that A is an arbitrary integer, the following formula holds if and only
if A is a positive integer:

Int(A) A~ 4 = 0 A V A = X
2 + F 2 + Z2 + W8.
X.K.Z.JT

Another defining formula with fewer quantifiers which may serve the same
purpose was suggested by R. M. Robinson:

Int(A) A ~ A = 0 A V [Int(X) A ~X = 0 A (A = X s v X2 = 1 + A Y%

As an obvious consequence of Theorem 3.1, we obtain:
THEOREM 3.2. Let n be any fixed positive integer and let R be an n-ary relation
between rational numbers. Let R' be the relation which holds between 2n integers,
Pi, P2, • • • , Pn ; qi, •• • , qnif and only if qi j± 0, • • • , qn y& 0, and R holds
between p\/q\, • • • , pn/qn • Then R is arithmetically definable in terms of +
and • on rationals if (and only if) R' is arithmetically definable in terms of + and •
on integers.
This consequence of our discussion is interesting because of a result of Godel
[4] which shows that the variety of relations between integers (and operations
on integers) which are arithmetically definable in terms of addition and multi-
plication of integers is very great. For instance from Theorem 3.2 and Godel's
result, we can conclude that the relation which holds between three rationals
A, B, and N if and only if N is a positive integer and A — B
N is definable in the
arithmetic of rationals.

use, available at https:/www.cambridge.org/core/terms. https://doi.org/10.2307/2266510
Downloaded from https:/www.cambridge.org/core. University of Maryland - University Libraries, on 06 Apr 2017 at 13:15:42, subject to the Cambridge Core terms of

110  JULIA ROBINSON

4. Applications  to the  decision problem  in arithmetic. From  the results
obtained in Sections 1 and 3 various consequences can be derived concerning the
decision problem in the arithmetic of integers and rationals. In deriving these
consequences, we make use of some unpublished results of Tarski and Mostowski.
Hence we start with a brief account of these results.
The following remarks apply to mathematical theories which are assumed to
be formalized within the lower predicate calculus (with identity and without
variable predicates). We assume that in all these theories the same logical
symbols, the same logical axioms and axiom-schemata, and the same rules of
inference are used. Thus two such theories differ from each other only by the
range of their variables, their specific mathematical constants (primitive sym-
bols) and their specific mathematical axioms.
In each theory, we define in the usual way what we understand by a formula;
in particular, all axioms turn out to be formulas and any application of rules of
inference to given formulas yields a new formula. A formula which can be
obtained from logical and mathematical axioms by applying rules of inference
is referred to as a provable formula. A theory X is called consistent if not every
formula in it is provable; this amounts to saying that no two formulas one of
which is the negation of the other are both provable.
A theory X' is called an extension of the theory X if every provable formula in
X is also provable in X'. A set of formulas is called decidable if a method exists
which permits us in each particular case to decide in a finite number of steps if a
given formula belongs to the set;
8 otherwise, it is called undecidable. A theory
is decidable if the set of its provable formulas is decidable. A theory X is
said to be essentially undecidable
9 if it is consistent and if no consistent theory
X' which is an extension of X is decidable.
As an example of the theories discussed, we may consider the arithmetic of
positive integers with + and • as the only mathematical constants; however, for
our purpose it is convenient to introduce in this theory the symbol Pos to denote
the notion of a positive integer. The mathematical axioms are essentially
Peano's axioms listed in Section 2. We modify them slightly in order to elimi-
nate the symbols S and 1; in formulating these axioms, we use the symbolic
expression
 6U(c) (to mean c = 1) as an abbreviation of the formula

POS(C)A A [Pos(a;)A Pos(y) —> ~(x + y = c)].
*.»

The resulting axioms are:

Bl. V ^(c )

C

B2. A ([Pos(a)A POS(6)A <5U(C)A a + c = b + c]->a = b)
a.b.c

B3. A {[Pos(a)A POS(6)A 611(c)] - • a + (b + c) = (a + b) + c)
a,b,c

8 Using more technical terminology, a set of formulas is decidable if the set of integers
correlated with the formulas is general recursive.
• This notion was introduced by Tarski.

use, available at https:/www.cambridge.org/core/terms. https://doi.org/10.2307/2266510
Downloaded from https:/www.cambridge.org/core. University of Maryland - University Libraries, on 06 Apr 2017 at 13:15:42, subject to the Cambridge Core terms of

DEFINABILITY AND DECISION PROBLEMS IN ARITHMETIC 111

B4. A [{Pos(a) A 6U(c)j -> a-c = a]
a.c
B5. A {[Pos(a) A Pos(6)A qi(c)] -» a-(6 + c) = (a-6) + a}
a.b.c
B6. A {[^(c)
 A
 S'WA A ([Pos(a)A g>(a)] -> 9(a + c))]

-»A(Pos(o)-»9»(o))} .
a
We shall call the theory based on these axioms ty. The same remarks that were
made in Section 2 about A6 apply to the induction principle B6.
It was shown by Church [2] using essentially the method of Godel [4] that the
theory
 s$ based upon the above axioms is undecidable. Rosser [9] showed that
this theory is even essentially undecidable.
It is well known that the following formulas are provable in Theory fy:

B7. A [(Pos(o) A Pos(6) A Pos(c) A a + c = 6 + c)-» a = 6]
a,b,c

B8. A [(Pos(a) A Pos(6)) -*a + b = b + a]
a, b

B9. A [(Pos(o) A p0s(6) A POS(C)) -» a + (b + c) = (a + b) + c]
a,b,c
BIO. A [(Pos(a) A Pos(6) A ~ a = b) -+ V (Pos(c) A[ a = 6 + cv 6 = a + c])]
a,b c
Bll . A [(Pos(o) A Pos(6) A Pos(c)) -» a-(b + c) = (a-6) + (a-c)].
a,b,e
It is also clear that if we replace B2, B3, and B5 by B7-B11 in the axiom system
of the theory ^ we obtain an equivalent axiom system. Hence the results of
Church and Rosser previously mentioned apply equally well to the new axiom
system. In this connection, however, Mostowski and Tarski have recently
obtained a stronger result:
I. The theory '$' with primitive mathematical terms +, -, and Pos and with the
mathematical axioms Bl, B4, B7-B11 is essentially undecidable.
The method of proof is similar to that used by earlier authors.
As is easily seen, an important difference between fy and fy' is that ^J' does
not have the induction principle and hence has only a finite number of mathe-
matical axioms. In consequence, as we shall see, Theorem I has a much wider
range of applications than the older results in this direction, i.e., it enables us to
establish the undecidability of a much greater variety of mathematical theories.
The applications of Theorem I are based on the following general method
developed by Tarski. Let Xi be a theory (of the type considered) with the
(specific) mathematical constants Oi, • • • , 0„ and £ 2 be another theory with
the mathematical constants Qi, • • • , Qm. We shall speak of a possible defini-
tion of one of the symbols 0,- in terms of Q x, • • • , Qm . To fix the idea, assume
for example that Oi is the symbol for a binary operation. Then by a possible
definition of Oi in terms of Qi, • • • , Qm we understand any equivalence of the
form
 A [oO*fc = c  «-*• <f>]
a, h e

use, available at https:/www.cambridge.org/core/terms. https://doi.org/10.2307/2266510
Downloaded from https:/www.cambridge.org/core. University of Maryland - University Libraries, on 06 Apr 2017 at 13:15:42, subject to the Cambridge Core terms of

112  JULIA ROBINSON

where <t> stands for any formula containing only three free variables a, b, and c
and containing no mathematical constants other than Qi, • • • , Qm . We now
say that Theory Xi is consistently interpretable in Theory £ 2 if there is a con-
sistent theory X satisfying the following conditions: (i) X is an extension of
both Xi and X2, i.e., both Ox, • • • , On and Qi, • • • , Qm are mathematical con-
stants of X and all axioms of both Xi and Xt are axioms (or at least provable
formulas) of X. (ii) For each of the symbols 0< (i = 1, • • • , n) which does not
occur in the sequence Qi, • • • , Qm , there is an axiom (or provable formula) in
X which is a possible definition of 0< in terms Qi, • • • , Qm.
Using this terminology Tarski stated the following general principle:
II. If a theory Xi has only a finite number of mathematical axioms and is es-
sentially undecidable, then every theory Xz in which Xi is consistently interpretable
is undecidable (although not necessarily essentially undecidable).
By applying II to two theories Xi and X2 with the same mathematical con-
stants, we obtain the following formulation:
III. Let Xi and X2 be two theories with the same mathematical constants. If
Xi has only a finite number of mathematical axioms and is essentially undecidable,
and if the theory X which has the same mathematical constants as Xi and X2 and
whose axiom system is the union of those of Xi and X2 is consistent, then X% is un-
decidable.
From I—III various general results regarding the decision problem have been
derived. Thus, I and III imply at once the following corollary:
IV. Every theory X with mathematical symbols Pos, + , and • is undecidable
provided only that all the axioms of X are true formulas of the, arithmetic of positive
integers; or at least that all the axioms of X are compatible with those of Theory
fy' of Theorem I (i.e., the theory based on the union of the two axiom systems is con-
sistent).
This result comprehends two particular cases which are known from the litera-
ture: the case when all true sentences are regarded as axioms of X; and the case
when X has no mathematical axioms at all, so that X reduces to a purely logical
theory whose undecidability amounts to the undecidability of the lower predi-
cate calculus which was established by Church [3].
By using II instead of III, Theorem IV can be extended to the arithmetic of
arbitrary integers. Since among the true formulas of the arithmetic of arbi-
trary integers involving + and •, we find those which serve as postulates defining
the notion of an abstract ring, this result implies the following interesting corol-
lary:
V. The general (arithmetical) theory of abstract rings is undecidable.
Finally, by means of I and II Tarski has established the undecidability of the
general theories of lattices and groups.
New theorems in this domain can be obtained by combining I—III with the
results of the earlier sections of this paper. In fact we obtain:
THEOREM 4.1. Every theory X whose mathematical constants are Pos (or Int),
S, and • is undecidable provided only that the axioms are true formulas in the arith-
metic of positive integers (or of arbitrary integers). The result (in its application

use, available at https:/www.cambridge.org/core/terms. https://doi.org/10.2307/2266510
Downloaded from https:/www.cambridge.org/core. University of Maryland - University Libraries, on 06 Apr 2017 at 13:15:42, subject to the Cambridge Core terms of

DEFINABILITY AND DECISION PROBLEMS IN ARITHMETIC 113

to positive integers) remains valid if the multiplication symbol ; is replaced by the
divisibility symbol |.
10

THEOREM 4.2. Every theory X whose mathematical constants are Rt (to denote
the notion of a rational number), +  , and • is undeeidable provided only that the axioms
of X are true formulas in the arithmetic of rationals.
The proofs of these two theorems are entirely analogous. We want to out-
line briefly the proof 4.2 in order to clarify the use of I—III.
Given the theories ty of Theorem I and the theory X satisfying the hypothesis
of 4.2, we construct a new theory X' in the following way. The mathematical
constants of X' are Rt, Pos, + , and •. The axiom system of X' consists: (i) of
all axioms of ty' listed in I; (ii) of all axioms of X; and (iii) of an equivalence
which is a possible definition of Pos in terms of Rt, + , and • and which results
from Theorem 3.1. The theory X' thus obtained is obviously consistent since
all its axioms are true formulas in the arithmetic of rational numbers. Hence
according to the definition of consistent interpretability, ty' is consistently
interpretable in X; and therefore, by I and II, X is undeeidable.
It may be noticed that the symbol + in 4.2 can be replaced by <S; for the ad-
dition of rationals, like that of integers, is definable in terms of S and
Since among the formulas involving + and • which are true in the arithmetic
of rationals, we find those which are used as postulates to define the notion of an
abstract field, we obtain as a particular case of 4.2:
THEOREM 4.3. The general (arithmetical) theory of abstract fields is undeeid-
able.11' n

It should be emphasized that the general theory of abstract fields is by no
means essentially undeeidable, for extensions of this theory are known which are
decidable. In fact, as it was stated by Tarski [11], the arithmetical theory of
real closed fields and that of algebraically closed fields (thus in particular the
arithmetic of algebraic numbers, real algebraic numbers, real numbers, and that
of complex numbers with + and •) are decidable. Hence many further prob-
lems are suggested which are still open.
In particular, we can ask whether the arithmetical theory of various algebraic
extensions of the field of rational numbers are decidable. This applies to both
finite and infinite extensions.
A specially interesting case, in view of its application to the decision problem
for geometry, is that of the field of all constructible numbers, i.e., numbers
which can be obtained from 1 by means of rational operations and extracting
square roots.
We can also look for purely mathematical characterization of those fields

10 The problem of the undecidability of the system of integers with multiplication and
less-than was proposed by Mostowski.
11 The decision problem for fields was proposed by Tarski.
12 Using the results formulated in theorems 4.1-4.3, Tarski has recently shown that the
general (arithmetical) theory of modular lattices and that of projective geometry are also
undeeidable. This improves his earlier result regarding the undecidability of the general
lattice theory.

use, available at https:/www.cambridge.org/core/terms. https://doi.org/10.2307/2266510
Downloaded from https:/www.cambridge.org/core. University of Maryland - University Libraries, on 06 Apr 2017 at 13:15:42, subject to the Cambridge Core terms of

114  JULIA ROBINSON

whose theory is decidable or undecidable. Regarding those fields with char-
acteristic 0, parallel problems arise if, instead of fields whose theories are un-
decidable, we consider those in which the notion of an integer is arithmetically
definable. We do not know at present whether these two series of problems are
equivalent; if the notion of integer is arithmetically definable in a field then the
arithmetical theory of this field is undecidable, but the problem of whether the
converse holds (for fields of characteristic zero) is still open.

REFERENCES

[I] BERNSTEIN, B . A., Weak definitions  of a  field, Duke mathematical journal,  vol. 14
(1947), pp. 475-482.
[2] CHURCH, ALONZO, An  unsolvable problem  of elementary number theory, American
journal of mathematics,  vol. 58(1936), pp. 345-363.
[3] CHURCH, ALONZO, A note on the Entscheidungsproblem, thi s  JOURNAL, vol. 1(1936),
pp. 40-il , 101-102.
[4] GODEL, KURT, Vber formal unentscheidbare Satze  der Principia Mathematica  und
verwandter Systeme  I, Monatshefte fiir Mathematik  und  Physik,  vol. 38(1931), pp. 173-
198.
[5] HASSE, H., Vber die Darstellbarkeit von Zahlen durch quadralische Formen  im  K6rper
der rationalen Zahlen, Journal fiir  die reine und  angewandte Mathematik,  vol. 152 (1923),
pp. 129-148.
[6] HILBERT, D. , and BERNAYS, P. , Grundlagen der Mathematik.
[7] PADOA, A.,Vnnouveau systeme irreductible de postulatspour Valgebre, Comptes rendus
du 2-e Congres International  des Mathimaliciens, 1902,  pp. 249-256.
[8] PRESBUROER, M., Vber die Vollstandigkeit eines gewissen Systems  der Arithmetik,
Comptes rendus  du I  Congris des Pays Slaves, Warsaw 1929.
[9] ROSSER, B. , Extensions  of some theorems  of Gddel and  Church, this  JOURNAL, vol.
1(1936), pp. 87-91.
[10] TARSKI, A., Der Wahrheilsbegriff  in den  formalisierten Sprachen, Studia philoso-
Phica, vol. 1(1935), pp. 261-405.
[II] TARSKI, A., New  investigations on the  completeness of deductive theories (abstract),
this JOURNAL, vol. 4(1939), p . 176. [Added in proof: A detailed account has since
appeared in A . TARSKI, A  decision method  for elementary algebra  and geometry. Project
RAND , publication R-109, August 1948.]

UNIVERSITY OF CALIFORNIA

use, available at https:/www.cambridge.org/core/terms. https://doi.org/10.2307/2266510
Downloaded from https:/www.cambridge.org/core. University of Maryland - University Libraries, on 06 Apr 2017 at 13:15:42, subject to the Cambridge Core terms of
