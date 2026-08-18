<!-- source: https://arxiv.org/pdf/1711.09253v1 | converted from PDF -->

Erland Samuel Bring’s
“Transformation of Algebraic Equations”

Alexander Chen1, Yang-Hui He
2 & John McKay3

1 Westminster School
alexander.chen@westminster.org.uk

2 Merton College, University of Oxford, OX14JD, UK;
Department of Mathematics, City, University of London, EC1V 0HB, UK;
School of Physics, NanKai University, Tianjin, 300071, P.R. China
hey@maths.ox.ac.uk

3 Department of Mathematics and Statistics,
Concordia University, 1455 de Maisonneuve Blvd. West,
Montreal, Quebec, H3G 1M8, Canada
mckay@encs.concordia.ca

Abstract

We translate Erland Samuel Bring’s treatise Meletemata quædam Mathematica circa
Transformationem Æquationum Algebraicarum (“Some Selected Mathematics on the
Transformation of Algebraic Equations”) written as his Promotionschrift at the Univer-
sity of Lund in 1786, from its Latin into English, with modern mathematical notation.
Bring (1736 - 98) made important contributions to algebraic equations and obtained
the canonical form x5 + px + q = 0 for quintics before Jerrard, Ruﬃni and Abel. In due
course, he realized the signiﬁcance of the projective curve which now bears his name:
the complete intersection of the homogeneous polynomials of degrees 1, 2, 3 in P4, i.e.,{ 4∑

i=0 zi = 4∑

i=0 z2
i = 4∑

i=0 z3
i = 0
} ∈ C[z0, . . . , z4].

1arXiv:1711.09253v1  [math.HO]  25 Nov 2017
Introduction and Translators’ Notes

Within the illustrious history surrounding the Quintic Problem (q. v. [Har, Kle, Ber, DM]), it
is unavoidable that many tales should be eclipsed by the ultimate triumph and heart-breaking
tragedy of Evariste Galois. Dead more than a decade before Galois was born, Erland Samuel
Bring (1736-98), late Professor of History at the University of Lund, certainly provided one
such biography (cf. e.g.,[Mac]). Having read law, philosophy and history and subsequently
practised in the ﬁrst and lectured in the latter two, our polymath’s true passion lay in
mathematics. Though with volumes in history and mathematics ranging from geometry,
astronomy and commentaries on Euler, the magnum opus of Bring came in the form of his
Promotionschrift in application for his professorship in mathematics – when already professor
of history – at the University of Lund, then the Royal Academy of Queen Carolina, in 1786.

The great Sylvester begins [Syl] his treatise on Hamilton’s numbers [Ham] with the words
(as will be seen shortly, the dedication page of the thesis is by Somelius):

In the year 1786 Erland Samuel Bring, Professor at the University of Lund in
Sweden, showed how by an extension of the method of Tschirnhausen it was
possible to deprive the general algebraical equation of the 5th degree of three of
its terms without solving an equation higher than the 3rd degree. By a well-
understood, however singular, academical ﬁction, this discovery was ascribed by
him to one of his own pupils, a certain Sven Gustaf Sommelius, and embodied in
a thesis humbly submitted to himself for approval by that pupil as a preliminary
to his obtaining his degree of Doctor of Philosophy in the University.

It is thus remarkable that our humble professor of history has managed to bring the general
quintic to the trinomial form x5 + px + q = 0 (1)

by solving a set of no higher than cubics whose analytic resolution are standard even for his
time, using so-called Tschirnhaus transformations which date to the late 17th century. The
achievement, together with the thesis, was sadly much forgotten until later independently
rediscovered by the Irish mathematician G. Jerrard, after the works of Abel – which Jerrard
did not believe - showing the insolubility of the quintic by radicals. The simple expression
(1) is now called the Bring-Jerrard form of the quintic. A history (including some parts of
Bring’s thesis in the original, p45, cit. ibid.) was given by the Reverend R. Harley [Har] on
this reduction.
 2

It is amusing that Bring writes as the last sentence of §III, for the general m-th degree
polynomial that

. . . in genere ad eliminandum terminum M:tum requiri ut resolvatur æquatio M:tæ
dignitatis, credo de reliquo quemcunque facile perspicere, unum tantummodo ter-
minum ob eandem rationem, cujus supra mota mentio est, exterminari posse;
adeo ut si ita sit, ut Algebraistæ aliquando in spem venerint quamlibet æqua-
tionem ope transformationis a terminis suis intermedii liberatam resolvendi, fan-
tendum omnino est, hujus exspectationi in hunc usque diem minime respondisse
eventum nec unquam responsurum, quominus aliam transformandi methodum ac
quæ hucusque obtinuit, olim adhibere contingat.

(“ in general in order to remove the Mth term as required, an equation of degree M needs to
be resolved. I believe, with regards to the remaining cases, anyone can easily discover that
only one coeﬃcient can be removed, by the same reasoning that has been mentioned already.
If this is true, Algebrists ﬁnally will come to hope that any sort of equation, freed by the
power of transformations, can be resolved by its coeﬃcients, and it must be acknowledged
wholly that another method of transformation other than this one has not obtained this to
this day, but an expectation of this sort does not mean that an answer will never be found.”)
A forgiveable statement for the 18th century!

Yet Bring’s optimism (beginning of §.IV) remains sound advice to all generations of
mathematicians:

Quamvis autem nihil fere ex iis, quæ ad Mathesin pertinent, intactum atque
intentatum reliquerint amabilis hujus scientiæ plusquam indefessi amantes atque
cultores, ea tamen Algebræ particula, . . .

(However, no method belonging to the study of Mathematics should have been left behind,
untried and extended, from this lovable science by its untiring lovers and worshippers, and
this area of Algebra in particular, . . . )

The wider signiﬁcance of the Bring-Jerrard form was appreciated much later in the works
of Hermite [Her] on elliptic functions and Klein’s celebrated lectures [Kle] on the icosahedron
(q.v. an account especially in relation to Bring’s curve in [Nas]; cf. citeBN,edge,weber). The
key is that in reducing the general quintic

x5 + ax4 + bx3 + cx2 + dx + e = 0 (2)

3

into the form of (1), the ﬁve complex roots zi=0,...,4, by Viet`e, must be such that

0 = a = ∑

0≤i≤4 zi , 0 = b = ∑

0≤i<j≤4 zizj , 0 = c = ∑

0≤i<j<k≤4 zizjzk . (3)

Since symmetric polynomials in zi can be written interchangeably into the basis of elementary
ones as above, or into sum of powers. The above can be recast into

4∑

i=0 zi =
 4∑

i=0 z2
i =
 4∑

i=0 z3
i = 0 . (4)

Klein’s realization is that (4) itself deﬁnes a complex algebraic curve, of genus 4, as a complete
intersection in P4 with homogeneous coordinates [z0 : . . . : z4]. This curve, which he dubbed
Bring’s curve in honour of our protagonist, can be thought of as a moduli space of Bring-
Jerrard quintics. It has symmetry group S5, the largest possible for a genus 4 curve.

More recently, the deep connection between Bring’s curve to the icosahedron has been
exploited in the context of dessins d’enfants [SS], sporadic groups and generalized Moonshine
[HM], as well as the E8 Lie group and modular groups [Ga, Ya]. With this resurgence of
interest it is therefore expedient to present, for the ﬁrst time in other than the original Latin,
the entirety of Bring’s inﬂuential thesis, which hopefully is of interest to mathematicians and
historians alike.

Translaters’ Synopsis of the Thesis

I: A reminder of how the quadratic can be solved using linear substitutions;

II: A similar treatment for the cubic;

III: How one might attack the general equation of the m-th degree;

IV: On real and complex condition of roots in solving the cubic;

V: A general strategy for eliminating terms in the cubic;

VI: Following the strategy of §. V, construct the speciﬁc elimination problem of removing
the terms of degree 1 and 2;

VII: Similar treatment as §. VI for the quartic;

VIII: Further removal of the terms of degrees 3 and 4 in the quartic;

4

IX: Diﬃculties in removing three terms in the quartic;

X: Setting up subsidiaries for the quintic;

XI: Finally putting the quinitc into Bring-Jerrard form.

Notes

In translating the Latin, a few points may be of interest to the reader:

• Dignitatis: The word for “degree” of the polynomial is “dignitatis”, also, of course,
meaning “dignity”;

• &c, or “etc”, is taken as “. . .” in equations;

• Greek is used only once in the thesis, §III., p6, ωζ εν παρoδω, meaning “in passing”
or “just generally”.

• Q. E .F. : “quod erat faciendum” (that which was to be done) used for the end of a
construction, as opposed to the perhaps more familiar Q. E. D. for “demonstrandum”
used at the end of a proof; Indeed, one also has “quad est absurdum” - though not
abbreviated - for proofs by contradiction;

• Quartic equations are referred to as “æquationæ biquadraticæ”;

• “S:æ R:æ M:tis” is short for “Serenissimæ Reginæ Majestatis”, used for the Swedish
Queen (we thank Mr. Julian Reid, archivist of Merton College, Oxford for this insight);

• Terminus: The word for “term” in the polynomial is “terminus”, it is also used to
mean the coeﬃcient of a term;

• “Variable” corresponds to “littera”, thus, e.g., “littera z” means “the variable z”;

• Various words such as “real”, “complex”, “root” are their obvious counterparts “realis”,
“imaginaria”, “radicus”;

• When referring to variables, e.g., “the value of z”, a Greek insertion is made as “valor
τ ων z” (most of the time τ ων is shortened to τ 8) as τ ων is Greek for “of”.

Now, without further ado, we present, in English and modern notation, the thesis of Bring.

5

References

[Ber] M. G. Belardinelli, “R´esolution Analytique des Equations Algebraiques Generales,”
M´emorial des Sciences Mathematiques, Fascicule 145, Paris, Gauthier-Villars, 1960.
[BN] H. Braden, T. Northover, “Bring’s curve: its period matrix and the vector of Riemann
constants”, SIGMA Symmetry Integrability Geom. Methods Appl. 8 (2012)
[DM] P. Doyle & C. McMullen, “Solving the quintic by iteration”, Acta Math., 163 (1989),
151-180.
[Edg] W. L. Edge, “Bring’s curve”, J. of LMS, 18 (3): 539 - 545, (1978).
–, “Tritangent Planes of Brings Curve”, J. LMS. (1981) 23 (2): 215 - 222
[Ga] Skip Garibaldi, “E8, the most exceptional group,” Bull. AMS 53 (2016) no.4, 643 - 671.
[Ham] The Hamilton numbers, cf. OEIS http://oeis.org/A000905.
[Har] Rev. R. Harley, “A contribution to the history of the problem of the reduction of the
general equation of the ﬁfth degree to a trinomial form,” The Quarterly J. of Pure and
Applied Maths, V6 (1863-1864), p38.
[Her] C. Hermite, “Sur la r´esolution de l´equation du cinqui`eme degr´e,” Comp. Rend. Math.
Acad. Sci. Paris, 46:508 - 515, 1858.
[HM] Y. H. He and J. McKay, “Sporadic and Exceptional,” arXiv:1505.06742 [math.AG].
[Kle] F. Klein, “Vorlesungen ¨uber das Ikosaeder und die Auﬂ¨osung der Gleichungen vom
f¨unften Grade,” Leipzig, Teubner, 1884.
Trans. G. G. Morrice, “Lectures on the Icosahedron and the solution of Equations of
the Fifth Degree,” Dover, NY 1956, https://ia800207.us.archive.org/11/items/
cu31924059413439/cu31924059413439.pdf
[Mac] The reader is referred to “Erland Samuel Bring” at the MacTutor, http://
www-history.mcs.st-and.ac.uk/Biographies/Bring.html
[Nas] O. Nash, “On Klein’s Icosahedral Solution of the Quintic”, arXiv:1308.0955.
[SS] D. Singerman, R. I. Syddall, “The Riemann Surface of a Uniform Dessin”, Beitr¨age zur
Algebra und Geometrie V. 44 (2003), No. 2, 413 - 430.
[Syl] J. J. Sylvester and J. Hammond, “On Hamilton’s Numbers”, Phil. Trans. of Royal Soc,
London, 1887, pp285-312 & 1888, pp65-71.
[Web] Matthias Weber, “Keplers small stellated dodecahedron as a Riemann surface”, Pa-
ciﬁc J. Maths, Vol. 220 (2005), No. 1, 167-182. http://www.indiana.edu/~minimal/
research/kepler.pdf
[Ya] Lei Yang, “Modular curves, invariant theory and E8”, arXiv:1704.01735.

6

Some Selected Mathematics on the
Transformation of Algebraic Equations

which by the great consent of of the Faculty of Philosophy in the Royal Academy of Queen
Carolina, Dr. Erland Samuel Bring (Regius and Ordinary Professor of History) modestly
presented by Sven Gustaf Sommelius (under the stipend of the King and of Palmcreutz of
Lund) to the erudite examinations of the public, on the 15th day of December, 1786.

Dedication

To a man of great faith, of Her Most Serene Majesty, the noblest Lord Sven Lagerbring,
Doctor of Civil and Canon Law, (most digniﬁed counsellor of the Queen’s Council, Celebrated
Professor of History in the Queen Carolina Academy, most merited member of the Royal
Academy, most venerated senior member of the Carolina Academy, my dearest master and
uncle like an indulgent parent);

To a man of great faith, of Her Most Serene Majesty, the noblest Lord Charles A. Hal-
lenborg (Counsellor in the Council in the King’s Dicastry of Bero, of great gravitas);

To a noble man and generous Lord Magnus Hallenborg (Celebrated accessory in the
King’s Dicastry of Junicopen, of great justice).

To a most noble and capable man Lord Adolf Hallenborg, the most noble Centurian of
the Cavalry in her Royal Legion of South Scania; To the Maecenians and most excellent
patrons

I need neither to anxiously question the Maecenians nor appeal to doubting Patrons,
under whose guardianship this Academic specimen was produced, as long as I and many
others are allowed to pay our respects and adorations to you, most noble men, the most
bold Maecenians and Patrons. Although it is truly most excellent, with regard to praises of
you, to favour those more scholarly ones, with whose delights and pleasures you are truly
considered; however this preference, shared by others as well as myself, I will honour with a
silent loyalty, since there are currently other aspects which I wish to address more.

For I ought to remember publicly, lest I seem or be an ignorant child, the house of your

7

people, in particular your forefathers, so many of whom were benefactors and so unusually
magnanimous with favours, which are used by Parents/Founders for sermons/discussions.
Therefore I put this on record, which is worth as much to me as a beloved memory, because
it stimulates an emotion of loyalty to you, Maecenians and Great Patrons, and I decided to
make testament to it with a deferential dedication. Therefore, I eagerly beseech and implore
you to allow your most honourable name to be inscribed in this work, and more importantly,
and again I beg you because I owe the fortunes of my beginning to your coming, that you
allow this since it is ordained by destiny, and so it is also necessary for me to give back this
account of my studies.

Not only do you allow me to oﬀer these ﬁrst fruits of labour but you have no issue also
with your client oﬀering to praise your accustomed benevolence, which comes second in no
way out of duty. For if, as is your custom, you should act kindly, and give to your indebted
servant new pledges of grace, then I will have the accomplishment which to me serves as
the greatest joy. As for the rest, I pay my utmost respects to divine will, for the immense
generosity of you, Maecenians and most revered Patrons, for the entire course of happiness,
and for all the prosperity which hopefully will endure ﬂourishing for as long as possible.
Wherever I shall be, I am forever devoted to Your Most Noble Name.

Your most devoted follower,

Sven Gust. Sommelius.

§I.

Within Algebra, nothing is more greatly desired than the ability to resolve any equation
into its roots. However, although in the pursuit of this matter Mathematical attempts have
progressed, a general method of solving quintic equations so far has not been accomplished,
unless approximations are suﬃcient, and this goal remains sought after through the darkest
nights. Among diﬀerent methods, which have been called in reinforcement to remove this
diﬃculty, there is one which is not at all unfavourable, in which a proposed equation is
transformed into another, whose solutions are easier to ﬁnd.

As an example, assume that the quadratic equation, A, which is to be solved is:

A : z2 + mz + n = 0 . (5)

8

Certainly, nothing is easier than the creation of another Equation B, in which we introduce
a new unknown quantity y, which satisﬁes, z = y − a. For if the value of y − a is substituted
into Equation A, then by this method, Equation A is changed into an equation of this form:

B : y2 − y(−2a + m) + (a2 − ma + n) = 0 . (6)

Having made this transformation, I believe it is apparent to anyone that a solution can be
found for Equation B with very little diﬃculty. When I assumed that z = y − a as I pleased,
we have control over the letter a, so nothing else is necessary than to deﬁne a in such a
way so that the second coeﬃcient becomes zero, and that is when −2a + m = 0 or a = m
2
Therefore, having substituted in this value for a, Equation B becomes

y2 + m
2

4 − m2

2 + n = 0 or y2 = m2

4 − n . (7)

In this equation, since we have made it so that the second coeﬃcient disappears, which
in equations of this sort is the only intermediary coeﬃcient, by no means will it be hard to
ﬁnd a suitable solution, since it is necessary that:

y = ±
√m2

4 − n = ±1
2
 √
m2 − 4n. (8)

Henceforth, the solution of Equation A, once rearranged, surfaces, since: z = y − a = y − m
2
and so z = −m
2 ± 1
2
√m2 − 4n. Q.E.F. (9)

This solution to equation A is the same for all quadratic equations, and is well-known and
appears in Algebra books, although in a diﬀerent way. However, it is clear from this example,
not merely what to transform equations means, but also that this can truly resolve equations
with great success.
 §II.

Indeed it is certainly possible to ﬁnd well-known transformations in all equations with degree
of this sort. Truly it is evident, since we only have control over one letter, only one coeﬃcient
by this method can be eliminated. Let us assume that our proposed cubic equation is:

A: z3 + mz2 + nz + p = 0 (10)

into which we substitute z = y − a and so is transformed into

B: y3 + y2(−3a + m) + y(3a2 − 2ma + n) + (−a3 + ma
2 − na + p) = 0 . (11)

9

Certainly, in this new equation, the removal of either the second or third coeﬃcients is easy,
just as we want: in fact, apart from a very rare case, these coeﬃcients cannot both be
reduced at the same time. Because in order to reduce the second coeﬃcient, −3a + m = 0,
that is, a = m
3 . However, to reduce the third coeﬃcient, we need 3a2 − 2ma + n = 0, or
a = m
3 ± 1
3√
m2 − 3n.

The solution for a, if we were to set a = m
3 is very diﬀerent from the result if we set a
as a = m
3 ± 1
3√m2 − 3n, and both results cannot be reached together unless in this case, in
which m
3 = m
3 ± 1
3
 3√
m2 − 3n, and in which case m
2 − 3n = 0, or n = m2
3 . If therefore we use
this equation z3 + mz2 + m2
3 z + p = 0, without doubt, taking z = y − m
3 it is transformed
into
 y3 + y2(−m + m) + y(m
2

3 − 2m
2

3 + m
2

3 ) + (−m3

27 + m
3

9 − m3

9 + p) = 0 (12)

or y3 − m3
27 + p = 0, and in this equation not only the second but also the third coeﬃcient
is reduced. However, this case, in which a locus of this kind is possible, is rare to such an
extent that when a general method is made to reduce the coeﬃcients, it is not useful for all
others that also come under the same category of cubics.

Therefore from the above-mentioned determined values, while one substitution removes
more than the other, after one of two has been removed, that term does not remain in the
ﬁnite equation, in which the other term can be resolved with a solution which is very clearly
achievable, and so generally only one term of the transformed equation can be removed.
Because when it is as such, a cubic equation can not be resolved up until now through the
removal of both intermediate terms. However it cannot be denied that getting rid of the
second term provides great ease for solving equations, and that from the written algebra, we
reach an adequate solution.
 §III.

Just as with the quadratic and cubic equations, it is not doubted that in other equations,
transformations can be made in such a way. By way of example, let us create this general
equation: A: zα + mzα−1 + nzα−2 + pzα−3 + qzα−4 + . . . = 0 , (13)

10

in which we assume z = y − a. This will become, with the agreement of anyone who is
accustomed to the study of limits in mathematics:

B: yα + yα−1(−αa
1 + m) + yα−2 (
a2(α(α − 1)
1 · 2 ) + a−m(α − 1)
1 + n
) +

+ yα−3 (
a3(−α(α − 1)(α − 2)
1 · 2 · 3 ) + a2(+m(α − 1)(α − 2)
1 · 2 ) + a(−n(α − 2)
1 )
) +

+ yα−4 (
a4(+α(α − 1)(α − 2)(α − 3)
1 · 2 · 3 · 4 ) + a3(−m(α − 1)(α − 2)(α − 3)
1 · 2 · 3 ) +

+a2(+n(α − 2)(α − 3)
1 · 2 ) + a(−p(α − 3)
1 ) + q) + . . . = 0 .
 (14)

In this equation B, which is more easily observed in this way, for the second term to be
removed, −αa + m = 0 is substituted in, and also, so that the third term also disappears,
a2( α(α−1)
1·2 ) − a(m(α − 1)) + n = 0. Thus in order to remove the fourth coeﬃcient as required,
the substitution is:

a3 ( −α(α − 1)(α − 2)
1 · 2 · 3
 ) + a2 ( m(α − 1)(α − 2)
1 · 2
 ) − a(n(α − 2)) + p = 0 (15)

and in general in order to remove the Mth term as required, an equation of degree M needs
to be resolved. I believe, with regards to the remaining cases, anyone can easily discover that
only one coeﬃcient can be removed, by the same reasoning that has been mentioned already.
If this is true, Algebrists ﬁnally will come to hope that any sort of equation, freed by the
power of transformations, can be resolved by its coeﬃcients, and it must be acknowledged
wholly that another method of transformation other than this one has not obtained this to
this day, and an expectation of this sort does not mean that an answer will never be found.

§IV.

What we have discussed up to this point about the transformation of equations is not new,
and generally nothing that Algebra in its youngest form, while still wailing in its cradle,
cannot have taught. However, no method belonging to the study of Mathematics should
have been left behind, untried and extended, from this lovable science by its untiring lovers
and worshippers, and this area of Algebra, which deals with transformations of equations,
lay unused innocently, doubtless as if forgotten, as Mathematicians will have believed, and
until now do believe, that a means by which an equation of the third degree and having two
or more coeﬃcients can be solved is certainly impossible using a transformation of this sort.
Indeed either by thinking or otherwise not thinking about this matter, they all wanted to
deter the future generations, and they added a demonstration, which is this; They said:

11

Let us create a contradiction; let us assume for example that this cubic equation

A: z3 + mz2 + nz + p = 0, (16)

can be transformed into another purer cubic equation

B: y3 + a = 0, (17)

in which both intermediary terms are removed. Therefore the value of z in
equation A can be deduced by knowing the value of y in equation B. Since however
out of the roots of Equation B only one is real, the other two must be complex;
and for Equation A because it holds, due to a lack of loss of generality, such that
all cubic equations of this sort adheres to it, and, without doubt, sometimes A
is deﬁned by exclusively real roots, which obviously can happen, with the result
that a root of equation A, although it is real, nevertheless is determined by a
root of equation B, even though it is complex. This says, in eﬀect, that one root,
which is real, must be determined by another, which is complex, which creates
the contradiction.

We concede with both hands that equation A, which must be kept without loss of gen-
erality, can have roots such that they are all real, nor is it denied that equation B can only
boast one real root, with the other two always producing the mathematical impossibility.
Regarding the possibility of all three roots being real, it is not an easy task. However in the
equation B: y3 + a = 0, one root is always y + 3√
a = 0 which is real. In order to obtain the
other two roots, equation B is divided by the already discovered root, which results in

y2 − y 3√a + 3√a2 = 0 . (18)

Thus, out of the remaining two roots, one is y − 1
2 3√
a + 1
2
 3√
−3 3√a2 = 0, and the other is

y − 1
2 3√a − 1
2
 3√−3 3√a2 = 0, both of which are complex. Thus far, in the currently examined
demonstration, there has certainly been no lack of mathematical rigour.

When however, it is put forward that it is not possible for a real quantity to be determined
by a complex one, this is certainly very general and this phrase determined by something
is certainly not without suspicion of error. It is ambiguous and it can be deﬁned without
doubt such that it can be said non-absurdly that a complex value sometimes can determine
a real quantity. If however, this deﬁnition of this phrase is taken to be true here, in order to
say that a real quantity is reﬁned from parts, of which one or the other can sometimes be
complex, then this explanation cannot be doubted, but we come upon in this way a notion

12

that is diﬃcult to understand, which according to the basis of the contradiction cannot
be done. Anyone who has delved into the preceding maths or even only common Algebra
cannot be unaccustomed to this sort of matter. Let us create, for example, the cubic equation
z3 + mz + p = 0, which by Cardano’s formula can be solved into its roots, one of which is
this:
 z − 3
√ q
2 +
 √ q2

4 + p3

27 − 3
√ q
2 −
 √ q2

4 + p3

27 . (19)

If it happens that q2

4 + p3

27 is negative, which must happen in some cases, we know √ q2
4 + p3
27
becomes complex, and, here, z is the sum of two complex numbers and, the entire argument
relies on z being a real quantity. A contradiction of this sort, without doubt, cannot be dealt

with in another way than the establishing of the complex numbers, which is 3
√
 q
2 + √ q2
4 + p3
27

which is balanced by the other imaginary part which is 3
√
 q
2 − √ q2
4 + p3
27 with the result that

one cancels out the other. There are no exceptions, in which a similar annihilation does not
occur, so the value of z in A, although real, nevertheless can be determined from the complex
y values in equation B. By the truth of this sought-after demonstration, all contrary assault
collapses, such as the demonstration that was supported for a long time more by judgement
rather than calculations on the authority of those prestigious mathematicians. Thanks to
these ingeniously beautiful eﬀorts to understand the stars in the sky and its sublime ﬂight,
never again will this argument be undeservedly overlooked. Certainly if anyone should still
remain anxious, we believe they will be placated once they entrust in transformations, which
will be used for the abolishment of several terms in any equation.

§V.

These results, which were quoted above, apply to all transformations, provided there exists:

1. A proposed equation A to be solved, which will be transformed.

2. An equation B, which will be created, which contains not only an unknown quantity of
equation A, but also a certain new unknown quality, such that the relationship between
these two values is deﬁned by the characteristics of equation B. This equation is called
the subsidiary or intermediary equation, since in fact without it a transformation is
impossible anyway.
 13

3. A certain algebraic operation, often very diﬃcult, although always possible, by which
the unknown quantity which is common to equations A and B is removed.

Having performed this operation, another equation C appears from the extermination, which
tends to be called the transformed equation, containing the unknown quantity introduced in
equation B, which has the same maximum degree as the other unknown quantity in equation
A. In order to further clarify this process, let us repeat it using one of many previously stated
examples.

1. The equation A: z3 + mz2 + nz + p = 0 is proposed, and is to be transformed;

2. This equation B: z + a − y = 0 acts as the subsidiary;

3. The letter z is removed from equations A and B, and this transformed equation appears:

C: y3 + (−3a + m)y2 + (3a2 − 2ma + n)y − a3 + na2 − na + p = 0 . (20)

Having considered this, I believe none of the mathematicians can deny that this transforma-
tion, described above, and everything else described since the beginning of this dissertation,
applies for all cubics. We ought to add that we accept, furthermore, to have considered
another Subsidiary equation to be applied, which is of a single degree. From this, it happens
that we can only control the value of one letter, and thereby only one term from the equa-
tion can be removed. Truly, from what I have said of this process, nothing at all impedes a
subsidiary equation from having two or higher degree and we will see transformations that
happen because of this fact, in which two of more terms can be exterminated from any
general equation.
 §VI.

1. The equation which is to be transformed is proposed to be:

A: z3 + mz2 + nz + p = 0, (21)

2. This is the subsidiary equation:

B: z2 + bz + a + y = 0, (22)

14

3. Following the elimination of z from these two equations, this transformed equation
appears

C: y3 + (−mb + m
2 − 2n + 3a)y2+

+ (nb2 + (−mn + 3p)b + n
2 − 2mp − 2mba + (2m
2 − 4n)a + 3a2)y−

− pb3 + mpb2 − npb + p2 + nb2a + (−mn + 3p)ba+

+ (n2 − 2mp)a + (m
2 − 2n)a2 − mba2 + a3 = 0 .
 (23)

In this equation, the two letters a and b are deﬁned however we please, and actually they
interact with this equation in such contrasting manners, that they by no means have just
the power of a single letter. It is not possible for us to eliminate both the intermediary terms
without the use of this trick, which is:

1. D: − mb + m2 − 2n + 3a = 0 ,

2. E: nb2 + (−mn + 3p)b + n2 − 2mp − 2mba + (2m
2 − 4n)a + 3a2 = 0 . (24)

From equation D, it follows that a = mb−m2+2n
3 . This value of a is substituted into equation
E in the place of the same letter a, which results in:

b2 + −7mn + 9p + 2m3

3n − m2 b + −n
2 − 6mp − m
4 + 4m
2n
3n − m2 = 0 . (25)

The value of this letter b will easily be known, since in order to obtain its value, nothing
is needed bar the resolution of a quadratic equation. However, having found out the value
of b, it is not possible to ignore what a becomes. Furthermore, it follows that, in whatever
way letters a and b should be determined, the transformed equation C loses both of its
intermediary terms. Q. E. F .

Therefore in this way, equation C becomes pure, and is easily resolved. With the known
value of y now, the value of z is easily found, after the resolution of the quadratic equation B.
What is very easily understood in this way is that cancelling of one impossible (imaginary)
term by another can happen, as seen in Chapter 4. There are two imaginary roots in
equation C, after both intermediary terms disappear, from which the two roots of equation
A are derived, even though they are real. In fact, this dependent state cannot be reached
unless by using Equation B; however, as long as this equation is simple, that is of a single
degree, it does not seem to be something which an imaginary root of equation C can remove.

If however a quadratic equation becomes the intermediary of which both roots can be
imaginary, the whole process of explanation becomes very satisfactory. For the imaginary
root of the pure equation C can be balanced by the imaginary number, which can be among

15

of the roots of equation B, such that with the complex numbers having been removed one
by the other, nothing can stop all the roots of equation A being real and thus generalize for
the rest of the cases.
 §VII.

From the cubic equations that were transformed to our liking, we are allowed to set forth
unobstructed to similarly transform quartic equations by using the quadratic equation. Thus
this equation is proposed: A: z4 + nz2 + pz + q = 0 , (26)

in which the second term is removed, which is necessary in case the matter is pressured by
greater diﬃculties. If the second term were to be present, it would certainly not be worth
removing it. The subsidiary equation is:

B: z2 + bz + a + y = 0 . (27)

Following the removal of the letter z, this equation becomes:

C: y4 + (4a − 2n)y3 + (6a2 − 6na + nb2 + 3pb + n2 + 2q)y2+

+ (4a3 − 6na2 + (2n
2 + 4q)a + 6pab + 2nb2 − npb + 2nq + p2 − pb3 − 4qb
2)y+

+ a4 − 2na3 + (n2 + 2q)a2 + 3pba2 + nb2a2 − (2nq + 2p3)a−

− pnba − 4qb
2a − pb3a + qb
4 + nqb
2 − qbp + q2 = 0 .
 (28)

In this equation, the second and third terms can be removed very easily, if we set:

1. 4a − 2n = 0 or a = n
2 and

2. nb2 + 3pb + n2 + 2q − 3n2
2 = 0.

In truth, the removal of the 2nd and 4th terms seems much more fruitful, since by this, the
quartic equation is transformed into a quadratic and is resolved very easily. Regarding the
easier solution of the aforementioned matter, we set this substitution which has featured
previously, which was how we removed the 2nd and 3rd terms. Let this be the proposed
equation: A: z4 + pz + q = 0 . (29)

16

As before, let the subsidiary equation be:

B: z2 + bz + a + y = 0 . (30)

After we substitute out the value of z we will have:

C: y4 + 4ay3 + (6a2 + 3pb + 2q)y2 + (4a3 + 4qa + 6abp + p2 − pb3 − 4qb
2)y

+a4 + 2qa
2 + 3pba2 + p2a − 4qb
2a − pba3 + qb
4 − qpb + q2 = 0 . (31)

In this equation if we set a = 0 then it is necessary that:

D: − pb3 − 4qb
2 + p2 = 0 , (32)

in order to remove the 2nd and 4th terms; which is done so that the quartic equation C
formally becomes quadratic as desired. Therefore, the value of b is discovered with the
easy resolution of the cubic equation D, and the value of y is then discovered through the
completion of the resolution of the quadratic equation C, and moreover, the value of z, which
is then itself plucked out of the darkness, cannot be unknown once the quadratic equation
B is resolved. Q.E.F.

§VIII.

If you were to want to remove the third and fourth terms, we would run into a diﬃculty
that at ﬁrst glance is neither light nor trivial, and which we ought to treat very carefully; At
ﬁrst we may fear that we will ﬁnd diﬃculties in transforming equations of higher degree in
many places, and that these will be hindrances to removing the third, fourth and remaining
terms. Naturally, in order to simultaneously remove the third and fourth terms of the quartic
equation, it is required that:

1. 6a2 + 3pb + 2q = 0 or b = −6a2−2q
3p ,

2. 4a3 + 4qa + 6pba − pb3 − 4qb
2 + p2 = 0,

from which when either a or b are removed, a certain equation is set out, in which the other
of these letters is of a higher degree than z or the other unknown values in the proposed
equation, thus in order to solve an equation of a lower degree, we need to solve one of higher
degree, so bad becomes worse.
 17

Nevertheless, although this diﬃculty will be present in other equations, it is certain that
it can be removed easily in this present occasion. For if at ﬁrst the second and third terms
are removed from the proposed quartic equation, which we have seen to be possible, then
a reciprocal transformation is made, and no Mathematician can deny that in this way a
quartic equation deprived of its 3rd and 4th terms appears, Q.E.F.

About the remaining, so that anyone can see very clearly, all equations of any degree can
be transformed using an intermediary quadratic equation into another, in which since either
the second or the third term is removed, given the possibility of solving a quadratic equation,
or the 4th term, given the possibility of the solution of a cubic equation, and thus from now
on, in a way I believe nobody can doubt, that in general thanks to this transformation more
than two terms can be removed at the same time.

§IX.

Therefore, so that we can remove three terms in a certain equation, anyone can see that it is
necessary for the intermediary equation to have at least degree 3. Let the proposed quartic
equation be: A: z4 + pz + q = 0 (33)

and the subsidiary equation be:

B: z3 + cz2 + bz + a + y = 0 (34)

after the substitution of the letter z we will have:

C: y4 + (4a − 3p)y3 + (6a2 − 9pa + 3pbc + 4qb + 2qc
2 + 3p2)y2+

+ (4a
3 − 9ba2 + 6p2a + 4qc
2a + 6pbca + 8qba−

− pbc3 − 4qcb
2 − 3p2cb − 5pqb + 4q2c + p2c3 + pqc
2 − p3)y+

+ a4 − 3pa3 + 3p2a2 + 2qc
2a2 + 4qba
2 + 3pbca2 + pqc
2a−

− 3p2bca − p3a + p2c3a − 4qb
2ca + 4q2ca − 5pqba−

− pb3a + qb
4 + 3pqcb
2 + 2q2b2 − pqbc3 − 4q2c2b + p2qb + q2c4 − pq2c + q3 = 0 .

(35)

18

In order to remove all three intermediary terms of this equation C, after duly carried out
calculations, none cannot see that it is required that:

1. a = 3p
4 , (36)

2. E: 24pbc + 16qc
2 + 32qb − 3p2 = 0 , (37)

3. F: − 2pb3 − 8qb
2c + 2p2c3 − 3p2bc + 4pqc
2 − 6pqb + 8q2c + p3 = 0 . (38)

And if we remove b from equations E and F, this equation comes out:

G: (243p5 − 5 · 16
3pq3)c6 + (7 · 24
3p4q − 8 · 16
3q4)c5+

+ 540 · 24
2p3q2c4 + (180 · 24p6 + 500 · 32
2p2q3)c3+

+ (945 · 16p5q + 400 · 32
2pq4)c2 + (15 · 32 · 36q2p4 + 4 · 32
3q5)c+

+ 7 · 32
2p3q3 − 27p7 = 0 .
 (39)

This equation G is of the sixth degree. It is certainly true that b can be evaluated with the
cancellation of the letter c in equations E and F. But in fact in this case we do not get an
equation of smaller degree. It can perhaps be thought that it is not only an equation of sixth
degree is present, but actually, under its structure lies an equation of smaller degree, since
it is scarcely understood how an expression for the roots of a quartic equation can reveal an
expression for roots of a sixth degree equation.

Whatever it is, it seems necessary to solve an equation of the sixth degree in order to
remove all the intermediary terms in a quartic equation. This is the same diﬃculty that
we encountered earlier in §. 8, whose solution however is not suﬃcient as a remedy, and in
whose place an extension of this idea will be used. We will see however that this diﬃculty
in removing three terms of a certain equation is not always irrefutable.

§X.

Let the proposed equation be:
 A: z5 + pz2 + qz + r = 0 , (40)

in which the second and third terms are to be removed. Let the subsidiary equation be:

B: z4 + dz3 + cz2 + bz + a + y = 0 (41)

19

Cancelling out the letter z gives:

C: y5 + (−3pd − 4q + 5a)y4+

+ (3pbc + 4qbd + 5rb + 2qc
2 + 5rcd − 3p2c + 6q2 − 4pr + 5pqd + +3p2d2 − 12pda−

− 16qa + 10a2)y3+

+ (−pb3 − 4qb
2c − 5rb2d + 3p2b2 + 9pbca + 12qbda − 5rbc2 − 3p2bcd + 2pqbc − 5pqbd
2+

+ 15rba + (pr − 8q2)bd − (11rq − 3p3)b + 6qc
2a + 15rcda + p2c3 + pqc
2d+

+ (8rp − 4q2)c2 − 9p2ca + 18q2a + (4q2 − 7pr)cd2 − (2qr + 3p3)cd − 12pra+

+ 15pqda + (2q2q + 5r2)c − (p3 + 3rq)d3 + 9p2d2a − (qp2 + 5r2)d2−

− (pq2 + rp2)d − 18pda2 + p4 − 4q3 + 8rpq + 10a
3 − 24qa
2)y2 + . . . = 0 .
 (42)

In this equation C, the 5th and 6th terms are overlooked, since they are not yet needed. But
in order to remove the second, third and fourth term, it is necessary that:

1.D: a − 3pd + 4q
5 = 0; (43)

2.E: 15pbc + 20qbd + 25rb + 10qc
2 + 25rcd − 15p2c − 3p2d
2 − 23pqd − 2q2 − 20rp = 0 ;
(44)

3. The coeﬃcient of the 4th term must also be zero,

the equation for which we call F.

If in equation F, we set the value of a equal to 3pd+4q
5 , it is trivial to see that the letters b,
c and d by this substitution are not raised to a higher degree than before. When however,
from equations E and F, either b or c or d are cancelled, this cannot create anything but
an equation of sixth degree, which perhaps is not of another form, nor can be changed to
a smaller degree by any method. Nevertheless, a tentative hope is exhibited of solving this
great diﬃculty.
 §XI.

If in equation E, being nothing other than the third term of Equation C, instead of a takes
the value of 3pd+4q
5 , and we set

b = αd + ζ, and also c = d + γ . (45)

20

This equation E is turned into this equation:

G: [(15p + 20q)α − 3p2 + 10q + 25r]d2+

[(15pα + 20q + 25r)γ + (15p + 20q)ζ + 25rα − 15p2 − 23pq]d+

+ 10qy2 + (15pζ − 15p2)γ + 25rζ − 2q2 − 2rp = 0
 (46)

If we set
 α = 3p2 − 10q − 25r
15p + 20q (47)

and
 ζ = −15pαγ − 25rα − 20qγ − 25rγ + 15p2 + 23pq
15p + 20q (48)

then 10qγ2 + (−15p2 + 15pζ)γ + 25rζ − 2q2 − 2rp = 0 . (49)

Anyone can see that in order to ﬁnd the values of ζ and γ it is not necessary to solve any
other equation other than the quadratic one. Therefore, having revealed by this very easy
method the values of α, ζ and γ and after substituting these in their place in equation G, this
equation G is completely reduced, with one term removing another, such that in equation C
the third term is also removed.

Having ﬁnished this, we substitute into the 4th term of the same equation C in the place
of a the same value of 3pd+4q
5 and in the place of b the same value of αd + ζ and also in
the place of c the same value d + γ; of course the letters α,ζ and γ are determined in the
same way that they were be deﬁned before, and we are now looking to remove the additional
fourth term from the equation, in which d is the only unknown. However, the maximum
degree of d cannot surpass three, so that it is accessible by the resolution of a cubic equation,
whose value should then be compatible with the removal of the fourth term in equation C.

Since therefore, by the deﬁnition of a the second term will be removed, and by the
deﬁnitions of b, c, α, ζ and γ the third term will be removed and by the deﬁnition of d the
fourth term will be removed, it is true that in this way, the three aforementioned intermediary
terms in any equation of 5th degree can be removed. Q.E.F.

In truth, the long extent of this matter and the reason of time forbid all from pursuing
this for merit. For the essence of the solution, you can investigate at leisure the nature of
the resolution of the cubic and quartic equations, which, by the work of transformations, we
saw can become comparable to the rule of Cardano, which concerns greatly these methods.

At present, this will be suﬃcient and is why we document this little piece of work for
acceptance. FINEM

21
