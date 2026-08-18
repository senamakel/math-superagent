<!-- source: https://www.mathnet.ru/php/getFT.phtml?jrnid=rm&paperid=4718&what=fullteng&option_lang=eng | converted from PDF -->

Uspekhi Mat. Nauk 45:2 (1990), 143-200 Russian Math. Surveys 45:2 (1990), 129-203

Finiteness theorems for limit cycles

Yu.S. ll'yashenko

CONTENTS

Introduction 129
§1. Expansion of monodromy transformations of class 1 into terms with 137
incommensurable rates of decrease
§2. Function-theoretic properties of simple and sectorial cochains 159
§3. The Phragmen — Lindelof theorem for simple and sectorial cochains 173
§4. Superaccurate asymptotic series 183
Appendix I 197
Appendix II 199
Historical comments 201
References 202

Introduction

0.1. Formulation of results.
This is the first half of a two-part paper1^ containing the following results:

Theorem I. A polynomial vector field on the real plane has only finitely many
limit cycles.

Theorem II. An analytic vector field on a closed two-dimentional surface has
only finitely many limit cycles.

Theorem III. 4 singular point of an analytic vector field on the real plane has a
neighbourhood that is free from limit cycles.

It was shown by Poincare and Dulac [15] (see also [6]) that this theorem
follows from Theorem IV.

Theorem IV. An elementary compound cycle of an analytic vector field on a
two-dimensional surface has a neighbourhood that is free from limit cycles.

We recall that a compound cycle (also called polycycle) is a separatrix
polygon (a more detailed definition can be found in [6]). A compound cycle is
said to be elementary if all its points are elementary, that is, if they have at
least one non-zero eigenvalue.

(1)I plan to publish the second, far longer part in the form of a book.

130 Yu.S. Il'yashenko

Monodromy transformations of compound cycles are defined as for ordinary
cycles, only the transversals in the definition are replaced by semitransversals,
that is, semi-intervals that are transverse to the cycle (Fig. 1). It is convenient
to regard monodromy transformations as germs of maps (R + , 0) ->• (IR
+ , 0).

Fig. 1

Theorem V (identity theorem). A monodromy transformation of a compound
cycle of an analytic vector field that has countably many fixed points is the
identity.

Theorem IV is an obvious corollary of Theorem I. We shall give a proof
of Theorem I later: first, we prove it in a special case (see Theorem Β of §0.6)
and a general proof will be given in the second part.
In the Introduction we explain the ideas of the proof in both cases and
pass from differential equations to complex analysis.
All the main ideas used in the general case appear already in the first part
of the paper, which is technically far simpler than the second part.
Consequently the first part contains in a sense a digest of the proof of the
identity theorem in the general case. The division of the paper into two parts
should hopefully facilitate its understanding.

0.2. Outline of the proof.
In the proof of the identity theorem we first construct a set of germs of maps
(R+ , 0) -*• (R + , 0) containing monodromy transformations of compound
cycles of analytic vector fields as well as other maps. The germs of this new
set have the properties of expandability and extensibility. Expandability means
that each germ is assigned an asymptotic series containing information not
only about power asymptotic behaviour but also exponential asymptotic
behaviour. Such series are called superaccurate asymptotic series (SAAS) and
will be described in §§0.4 and 0.5. When this series is trivial (coincides with
the identity), the correction to the corresponding germ decays very rapidly as
χ -* 0. The terms of the series cannot oscillate, since the existence of finitely
many fixed points of a germ implies that the corresponding series is trivial.

Finiteness theorems for limit cycles 131

Extensibility means that the germ can be extended to a complex domain as
a map cochain, that is, a piecewise continuous map that is holomorphic
outside the discontinuity lines. Map cochains that originate from extensions
of monodromy transformations satisfy the Phragmen — Lindelof theorem,
which states that a correction to a germ that decreases extremely rapidly is
identically equal to zero. The triviality of an SAAS ensures automatically that
the correction decreases "extremely rapidly".
We have the following implication (Δν is a monodromy transformation of a
compound cycle γ, Δ γ is the SAAS for Δ γ, and Fix,» is the set of germs with
countably many fixed points):

Δ ν e Fix,*, 4Λ , = ^Α,- ι = 0.

An elementary compound cycle whose singular points are all hyperbolic
saddles is said to be hyperbolic, and elementary compound cycles that do not
satisfy this condition are non-hyperbolic. The outlined programme was carried
out in the hyperbolic case using ordinary instead of superaccurate asymptotic
series in [5]. In the general case one can use the analytic theory of normal
forms of resonant vector fields and maps to describe the monodromy
transformations.

0.3. Dulac's series and exponentially small corrections for monodromy
transformations.
The hyperbolic case. Dulac studied asymptotic series for monodromy
transformations which approximate the transformations up to an arbitrary
power.

Dulac's theorem. It is possible to choose a semitransversal to a compound cycle
of an analytic vector field and a chart on it in such a way that the corresponding
monodromy transformation is either flat, inverse to aflat transformation, or
semiregular. Semiregularity means that the germ can be expanded in Dulac's
asymptotic series
 oo
Δ7 = cxv' + S PJ (In x) xvi, vj / oo, Vj > 0,
ι
where c > 0 and Pj are polynomials (the arrow / denotes monotonic convergence).
Partial sums of Dulac's series approximate the monodromy transformation up to
an arbitrary power of x.

This theorem holds not only for analytic but also for smooth vector fields
with singular points of finite multiplicity. Hence this theorem cannot imply
the finiteness theorem. Only the following implication is obtained:
Δ γ e FIXQO =¥ Δ ν = id (see §23 of [15] and part 3 of the Introduction in [6]).
In the hyperbolic case, a monodromy transformation is uniquely determined
by its Dulac series. This was proved in [5]. This implies the identity theorem
and thus also Theorems I—IV for vector fields with non-degenerate singular
points.

132 Yu.S. IVyashenko

However, Dulac's series does not in general determine the monodromy
transformation. There is a compound cycle of an analytic vector field with
two degenerate elementary singular points whose monodromy transformation
differs from the identity by a non-zero flat component exp(— l/x) (see [5]).
It follows that ordinary asymptotic series are insufficient to determine the
monodromy transformations uniquely.

0.4. Superaccurate asymptotic series.
Consider a set Mi of germs of maps (K+ , 0) -» (R+ , 0). Each of these germs
can be expanded in an asymptotic series whose partial sums approximate the
germ up to an arbitrary power of x, for example, Dulac's series. Such series
will be called ordinary. However, it is desirable to expand the germs in series
with terms decreasing not only as powers but exponentially. This does not
appear to be possible at first sight: an arbitrary residual term of an ordinary
series is bounded by powers of χ and there seems no point in considering
exponentially decreasing terms.
This difficulty can be bypassed as follows. We introduce an intermediate
class of functions Mo; functions belonging to this class can be expanded in
ordinary series and are uniquely determined by them; hence the zero series
corresponds to a zero function. The germs of class Mi are then expanded in
terms of decreasing exponentials but the coefficients of such series are no
longer numbers but functions from Mo- A simple example of an SAAS has
the form

(*) Σ = a0 {χ) + 21 ctj {x) exp (— ν
;·/ζ), a}<=M 0, Vj/oo , ν,·>0 .

The series Σ is said to be asymptotic for a germ / if, given any ν > 0,
there is a partial sum of the series that approximates the germ on (R + , 0) to
within o(exp(—v/x)). All the information about the expansion of a germ /i n
an ordinary series is included in the free term of the superaccurate series: the
ordinary series for / and a 0 are identical.
We shall use a simple example to illustrate the application of superaccurate
series in the proof of the identity theorem. We make the additional assumption
that the class MQ {M\) includes the germs of the functions 0 and x, and the
germs of this class can be expanded in Dulac's series (in SAAS (*)) and are
uniquely determined by these expansions. We then have the following
theorem:

Theorem.
 ^ / = id.

< The theorem is proved along the same lines as Dulac's lemma (see [6]).
Assume that it is false, that is, there isan/eM j Π Fix*,,/ Φ id. Let (•) be
the SAAS for/. Assume first that a0 Φ id. This means that the corresponding
Dulac series is ά0—id Φ 0. Hence the germ OQ —id is equal to the principal

Finiteness theorems for limit cycles 133

term of its Dulac series multiplied by 1 + o(l); in particular, there is a v > 0
such that
 | a0 - id | > x\

The expandability of/ into an SAAS (*) implies that

I / - id | > | a0 - id | + ( | a, | exp (-v^x)) (1 + ο (1)) χ* (1 + ο (1)).

Hence /—id Φ 0 for small χ and therefore/^ Fix^,, which is a contradiction.
Now let a0 = id, / Φ id. The SAAS (*) then cannot be id, since otherwise
/ = id, because a germ from M\ is uniquely determined by its asymptotic
series. It follows from the definition of expandability that

/ - id = (a, exp (-V*) ) (1 + ο (1)).

Following the same line of reasoning again, we find that a\ Φ 0 for small x.
The other two factors in the expression for /— id are also non-zero in the
vicinity of zero. Hence /φ Fix,», which is a contradiction. t>

Remark. Monodromy transformations of compound cycles can be expanded
in asymptotic series not only in simple but also in composite exponential
functions
 exp ο (—ν exp ο .. . ο exp 1/x).

The number of exponentials in this superposition is a principal parameter η
and the identity theorem is proved by induction on n. We consider η = 1 in
the first part, and then arbitrary η in the second.
A monodromy transformation of an elementary compound cycle is a
composition of correspondence maps (see Figs. 1 and 2) (in Fig. 2, Γ + is the
inverse image semitransversal and Γ~ is the image semitransversal). Extensions
of these maps to the complex domain are different in the hyperbolic and non-
hyperbolic cases.
 Fig. 2

134 Yu.S. Il'yashenko

0.5. Correspondence maps for hyperbolic saddles. Almost regular germs.
Definition 1. A quadratic standard domain is an arbitrary domain of the form

φ (C
+ \ Κ), φ = ζ +
C>0 , K= { | ζ | >i?>.

Definition 2. An almost regular map is a holomorphic map from some
quadratic standard domain Ω to C which can be expanded in this domain in
an exponential Dulac series

oo
Σ = ν0ζ + <; + 3Ρ;(ζ)βχρ(-ν,·ζ) , v o >O , ΟΟ,/οο .

where Pj are real polynomials. Expandability means that, given any ν > 0,
there is a partial sum of the series that approximates the map to within
o(exp(—νξ)) in Ω.
Two almost regular maps are equivalent if they are equal on some quadratic
standard domain. The class of such equivalent maps is said to be an almost
regular germ.
The chart χ on the semitransversal (R+ , 0) is said to be natural; the chart
ξ = —In Λ: on (R + , oo) is logarithmic.

Theorem. A germ of a correspondence map for a hyperbolic sector of a non-
degenerate singular point of an analytic vector field on the plane expressed in the
logarithmic chart can be extended to an almost regular germ in the complex
domain.

This theorem strengthens the fundamental lemma of [5] and it was proved
by S.I. Trifonov at my request (see Appendix I).
We shall now describe correspondence maps of degenerate elementary
singular points using the results of [19], [17] and [7].

0.6. Correspondence maps for degenerate elementary singular points.
Normalizing cochains.
The correspondence maps in question can be expressed as products of three
factors, two of which are needed in the definition, to which we now proceed.
A germ of a holomorphic vector field at an isolated elementary singular point
is formally orbitally equivalent to the germ

z = zfc+1 (1 + az*)'
1
, w = —w.

Here k + 1 is the multiplicity of the singular point, and α is a constant that is
real if the original germ is real. The manifold z = 0 is contracting for the
formal normal form, and w = 0 is the central manifold. The correspondence
map from the semitransversal to the first manifold onto the semitransversal to
the second manifold (for brevity, we call this map TO the central manifold) is
denoted by Ast for a normalized system and has the form

Δβί (z) = exp (—iJhk,a (z)),

Finiteness theorems for limit cycles 135

where hkia(z) = kzk/(l—akzk In z). These factors introduce exponentially
small terms in the asymptotic expressions for monodromy transformations.
Given a germ of a real holomorphic vector field at an isolated degenerate
elementary singular point, there is always a one-dimensional holomorphic
invariant manifold that is contracting after a suitable change of time and, as a
rule, has no holomorphic central manifold. The contracting manifold
corresponds to the monodromy transformation

(**) /: z>- ζ - 2JUZ*+I + . . .

Here k has the same meaning as in the formal orbital normal form of a germ.
This transformation is formally equivalent to a shift during a time — 2ni along
the trajectories of the vector field υ(ζ) = zk+lj{\ +azk). The corresponding
normalizing formal series usually diverge, but represent asymptotic series for
normalizing cochains, which will be defined next.
A good k-partition of a punctured disc is a partition of the disc into 2k
equal sectors such that one of the boundary rays belongs to the real axis.

Theorem 1 (sectorial normalization theorem [2], [18]). For any germ (••) there
is a set of holomorphic functions said to be the normalizing cochain of the term
with the following properties:
1. There is a one-to-one correspondence between the functions of the set and
the sectors of a good k-partition of some disc with centre 0 and radius R.
2. Each function of the set can be extended biholomorphically to a sector Sj
with the same bisector and a greater radius, that is, with an arbitrary angle
a € (π/k, 2n/k) and the radius of the sector dependent on oe.
3. All the functions of the set have the same asymptotic Taylor series at zero
with identical linear part.
4. On the intersections of the corresponding sectors the functions of the set
differ by o(exp(—c/z*)) for some c > 0.
5. Each function of the set couples the germ (**) in the sector Sj with a time
shift —2ni along the trajectories of the field o(z).

There is a normalizing cochain whose correction decreases faster than the
correction of the germ (**), that is, the cochain id + o(z* +1), and it is unique.

Definition 1. The set of all normalizing cochains described in Theorem 1 and
in the subsequent supplementary remark is denoted by JV"S; the set of maps
corresponding to the sector adjoining (R+ , 0) from above will be denoted by

JV<& U (u corresponding to "upper").
The following result is also known, but since one can find it in [2], [18]
only by reading between the lines, we shall also present the proof.

Supplement (see Appendix II). A function of the set forming the normalizing
cochain can be extended holomorphically to a domain wider than the sector Sj.
In the case of the sector Su adjoining the positive semiaxis from above, this
domain in the logarithmic chart ζ = — hi ζ (ξ = —In χ), ξ = Re ζ, χ = Re z)

136 Yu.S. Il'yashenko

has the form k  lYl(£>, where

Π<Τ> = Φ εΠ , Π = {Ι > a, | η |

α = α (ε), ε π/2}, Φ ε = ζ + (1 - ε) ζ"*,
[Ο, 1).

A similar result holds also for the other functions of the set; the map of the
normalizing cochain corresponding to the sector S" will be denoted by F£onn·

Remark. Let us set Π ^ = Π*. The domains Π^ε) are ordered by inclusion:
Π ^ C Π ^ for ε < ε'. The domain Π ^ is called a generalized ε-neighbourhood
of the curvilinear semiaxis Π* (see Fig. 3).

π
 Fig. 3

We are now ready to describe the correspondence maps referred to in the
heading of this section.

Theorem 2 [14], [5]. A correspondence map TO the central manifold of a
degenerate elementary singular point of a real-analytic vector field
Δ : (R + , 0) -*• (R + , 0) is the restriction of the composition

Δ = g ο Δ 3ι ο Fnorm

to (K + , 0), where F Dorm is the normalizing map cochain (see Theorem 1 on
sectorial normalization) for the corresponding monodromy transformation, F^ 0Tm
is the map belonging to F aorm defined on the sector S" adjoining 1R
+ from above,
the map A st was defined at the beginning of this section, and the germ g is
holomorphic at zero.

Supplement (see Appendix II). The multiplier g'(0) is positive and the asymptotic
Taylor series for F^ or m is real.

The map F% 0Tm is said to be the main map of the set F aorm.

Remark. The composition Δ does not change on R + when the map FnOr m is
replaced by the map from F nor m corresponding to the sector adjacent to IR
+

from below and the germ g is replaced by another holomorphic germ. By
choosing the main map in the formulation of Theorem 2 we have simply fixed
one of the two symmetric alternatives, which is in itself asymmetric.

Finiteness theorems for limit cycles 137

The normalizing map cochains make it necessary to use functional cochains
in the investigation of monodromy transformations of compound cycles.
We shall denote the set of all germs described in Theorem 2 by TO and the
set of germs inverse to them by FROM; the set of all almost regular germs
will be denoted by •^
f· The following result yields the identity theorem.

Theorem A. A composition of germs belonging to the classes TO, Μ and
FROM either has no fixed points near zero or is the identity.

A general proof of this theorem will be given in the second part. Here we
prove only the following result:

Theorem B. Theorem A holds for compositions with alternating germs from the
classes TO and FROM.

Such compositions will be called compositions of class 1.
A composition containing equal numbers of maps from the classes TO and
FROM is said to be balanced. An unbalanced composition can have no fixed
points near zero (see [6], [14]). A different choice of a semitransversal leads to
a cyclic permutation of the correspondence maps. It follows that a
semitransversal can be chosen so that a balanced composition of class 1
contains as the first map from classes TO and FROM a map from TO and
the last map is a map from FROM. The set of all such compositions forms a
group denoted by G\. Let us set G° = Λ and G~x = Aff. It is obvious that
the group G\ is generated by germs from the set FROM ο Jl ο TO and M:

G1 = Gr (FROM ο Μ „ TO, Μ).

Theorem Β is equivalent to the following result.

Theorem B'. A germ from G\ either has no fixed points with the exception of
zero or is the identity.

This theorem will be proved in the rest of this paper.

§1. Expansion of monodromy transformations of class 1 into terms
with incommensurable rates of decrease

It is our main aim to prove that the correction of a germ of a monodromy
transformation of class 1 does not oscillate, which means that either it vanishes
identically or it is non-zero for small χ Φ 0. We shall expand the germs of
monodromy transformations into sums of terms belonging to different
Archimedean multiplicative classes, which distinguish the non-oscillatory germs
according to the rate of decrease. By definition two real germs are
multiplicatively Archimedean equivalent if a real non-zero power of one of the
germs majorizes the other and vice versa:

/ ~ g 4=¥ 3a, b e 03 \ 0: f > g, gb > /.

138 Yu.S. IVyashenko

For convenience we shall consider all the germs on (R + , oo) rather than
(R +, 0). For this purpose, we introduce the logarithmic chart ξ = —In χ,
which takes (R + , 0) to (R+ , oo).
Two complex germs are multiplicatively Archimedean equivalent if their
real parts are equivalent.
Decreasing germs from different Archimedean equivalence classes have by
definition incommensurable rates of decrease.

Examples. The germs at infinity of the functions 1/ln ξ, ξ" 1 , exp( —ξ),
exp(—exp ξ) are all pairwise inequivalent. We have ξ ~ ξ" 1 ; exp μξ ~ exp νξ
and exp ο μ exp ξ ~ exp ο ν exp ξ for any μ, ν ε R; and exp( — C\ exp μξ) ^
<+< exp( —C2 exp νξ) for any C\, C%  and μ Φ ν.
Monodromy transformations of class 1 can be expanded into terms
belonging to the Archimedean classes of germs at infinity of the functions
ξ, 2, exp( —ξ), and exp(—exp μξ), where μ > 0. Germs within the same
Archimedean class can have asymptotics that differ by Dulac series in the class
of exp( —ξ) and by superaccurate asymptotic series of class 1 (SAAS-1) in the
class of exp( —exp ξ) (such series will be defined later). Oscillations are
impossible because of the Phragmen — Lindelof theorem, proved in §3.

1.1. Transformation to the logarithmic chart.
The Table opposite lists some of the maps mentioned above expressed both in
the natural chart ζ and in the logarithmic chart ζ = — In z. We use the
notation χ = Re z, ξ = Re ζ and ξ = —hi χ (we always choose the branch
of the logarithm that is real on the positive semiaxis).
It will be particularly important to describe the normalizing cochains in the
logarithmic chart. They transform into so-called periodic map cochains, which
are invariant under a shift by 2ni and are defined in some right-hand half-
plane ξ ^ a (where a depends on the cochain).
Let F be a normalizing cochain. The cochain F = Ad(exp(—ζ))^ in the
logarithmic chart then has the following properties, which follow directly from
the sectorial normalization theorem together with the supplement.
1. F is a set of biholomorphic maps whose elements are in one-to-one
correspondence with the domains of a partition of the half-plane ξ ^ a into
horizontal half-strips by rays η = nj/k, j e Z; each map of the set is
biholomorphic in the corresponding half-strip.
2. Each map of the set can be extended biholomorphically to an
ε-neighbourhood of the corresponding half-strip (ε can be chosen arbitrarily
within the interval (0, n/2k)) for a suitable a depending on ε.
3. The map of the set corresponding to the half-strip that is adjacent to IR
from above is said to be the main map or main function of the set, and can be
extended to fc-'Π^, Π ^ = ΦεΠ, Π = {ξ > α, |η | < π/2}, Φε = ζ + (1 -ε)ζ~ 2,
where ε e [0, 1) is arbitrary.

Finiteness theorems for limit cycles 139

4. All the maps of F have a common asymptotic series

ζ +  Σα,· exp (-/ζ) , aj <ΞΞ R.

5. The difference coboundary 5 F of the cochain F formed by differences
of the functions of F corresponding to adjoining half-strips of the partition in
an ε-neighbourhood of the common boundary ray of the half-strips is bounded
from above by the same function

6F exp (—C exp kl·,), C > 0.

This is a uniform bound for all functions of the set; the constant C  depends
on the cochain.
We shall denote the class of all such cochains by ^

^S =  {F aom =  Ad (exp ( - ζ)) F n0Tm I F norm e rf"S}.

The map from F  nor m corresponding to the half-strip adjoining (R + , co) from
above is said to be the main map of this set. The set of all main maps for
^norm <Ξ ^%  will be denoted by

Map in the natural chart

Power:
ZrtC2V, C>0 , V>0 .

Standard flat
/o =  exp(—1/z).

Almost regular germ

Germ of class 5?·° (almost regular
with principal term z).

Germ / of a conformal map
(C, 0) - (C, 0) with an
identical principal part
(germ of class O 0).
 The same map in the logarithmic chart

Affine: (germ of the group Aff)
ζ ,_,. ν ζ — In c, ν >  0, In c e R.

Exponential ζ t->. exp ζ.

Germ / that can be expanded in a quadratic
standard domain (see §0.5) in an asymptotic
Dulac series real in R +

OO

0 <  Xj / OO.

The same expression as above but with α =  1
and β =  0.

Germ / of class Μ  with a representative that
is biholomorphic in some right-hand half-
plane ξ > a and can be expanded in a
convergent series

Πζ) =  ζ+Σ«ίβχρ(-/ζ),α ; ·ε ε

(where the coefficients aj are not necessarily real!).

140 Yu.S. IVyashenko

Conjugation by a standard flat germ goes over to conjugation by an
exponential; this operation is very important and occurs very frequently, and
we shall denote it by

A: f M. Ad (exp) /; A'1: f ~ Ad (In) /.

This concludes the discussion of the transformation to logarithmic charts.

1.2. The description of germs from the group G\ is first given in the
logarithmic chart and this continues the discussion from §0.6. We first remind
the reader of the standard notation.
For any two subsets si and Si of a group, we denote by Gr(.s/, Si) the
subgroup generated by these subsets and by siSi the set {ab\a e si, b e Si).
We put
 Ad (a) b — a'^ba,
Ad {si)SS = Gr (Ad (a)b\a^s/, h <= SS).

In other words, Ad(si)Si is the normal factor generated by the set Si in
Gr(.s/, Si).

Remark. Let Si be a normal factor in Gr(j/, 38); then clearly Gr(jj/, Si) = si Si.

The germ of a domain at infinity is a class of domains in C such that any
two of them coincide outside some compact set depending on the domains in
question.

Example. The set of all bounded sets on C represents the germ of the empty
set. The germ of (C + , oo) is represented (among others) by sets C+\k, where
k is an arbitrary disc |ξ| < R.
We now describe the maps of the class TO in the logarithmic chart. An
arbitrary map from TO is described in the natural chart by the theorem in §0.6;
after a suitable change of scale with a positive coefficient it is given by

Δ = g ο A sfo Fnorm |(R+, o)>

where g : (C, 0) -* (C, 0) is a germ of a holomorphic map with an identical
linear part; the other factors were described in §0.6. Using the examples
listed in the Table, we find that the map Δ has the following form in the
logarithmic chart:
 Δ = g ο exp οΤίχ,αΟ /"norm-

The germ h k,a is almost regular; we do not require any other information
about this germ. We shall denote by & the set of germs of maps
(C+ , oo) ->• (C+ , oo) that are obtained by going over to the logarithmic chart
from germs of holomorphic maps (C, 0) -»· (C, 0) with an identical affine
principal part (see row 6 of the Table):

X = {-In ο g ο exp (-ζ ) \g 6Ξ O0, g (0) = 0, g' (0) = 1}.

Finiteness theorems for limit cycles 141

We denote by S° the set of almost regular germs with an identical affine
principal part (see row 5 of the Table):

J?° = (?eJ ? \g= id +

Clearly, we have Μ = Aff ο ,9/°, where Aff = {αζ + β | α > 0, β 6 Κ}.

Remark. The corrections of germs from J?° decrease exponentially in a
suitable quadratic standard domain, because almost regular germs can be
expanded in asymptotic Dulac series in such domains. Finally, we shall
denote by J£JR the set of germs of maps whose restriction to (R+ , oo) acts as
a germ (R + , oo) -> (R+ , oo). The germs belonging to Jl.^ will be called real.
We have
 T0c( I = exp c Aff ο Μ* ° άψ") Π ^ R |<R+, <»)

We shall denote by Am the group generated by the first two factors from the
right, that is, J,Ou = Gr (gFu |?eJ?° , Fu e J^S*; there are gl e M,
a e Aff such that {Agx) agFu e JHU).
The germs from Am are holomorphic maps in a half-strip containing the
ray (R+ , oo). It is very important that such maps can be extended to suitable
quadratic standard domains as so-called simple functional cochains whose
structure is reminiscent of the normalizing cochains and which will be defined
in §1.4. The main property of such cochains is that they can be expanded in
Dulac asymptotic series in exponentials, and these series determine them
uniquely. We set

A0 = Gr (gF | g <= 3P, F e Jrfy, gFu

Hence
 TO C {Μ ο exp c Aff ο jo) η j£ R f('R+i ^,.

The superscript u at the vertical line indicates that a composition of the main
functions of the sets forming cochains from A0 should be restricted to (R+ , oo).
In what follows we shall write similar expressions without indicating the
restriction to the real axis, which will always be understood.
Consider the compositions
 FROM »j?oTO ,
FROM ο j? ο TO c Gr (4 Gr {M, J2), A\ Aff) f]

We set
 H° = Gr (M, J?°).

Then Gr (36, M) CZ Gr (H\ Aff).

Now let a = αζ + β, α > 0, β e R. We have

Aa = id + In α + In (1 + α" 1 β exp (— ζ)).

142 Yu.S. IVyashenko

Hence Aa s Μ <Z Gr(^° , Aff). We thus obtain

FROM .J?.TOcG r {AH0, Λ0, Aff) Π

The definition of the group on the right requires further clarification
(see below). We recall that

G
a CZ Gr (FROM .j?.TO , M).

Hence
 G1 a Gr (AH0, Λ°, Aff) f]

Comments. The elements of this group are defined a priori only as formal
compositions rather than pointwise maps. In fact, the germs of each of the
first two subgroups are not necessarily real on the real axis. However it turns
out that all the compositions from this group are defined in a neighbourhood
of a ray ξ ^ a; both the ray and the neighbourhood depend on the actual
composition. This follows from the additive expansion theorem (see §1.6),
which implies that the composition can be written as a sum of cochains such
that the domains of definition of their main functions contain a common
neighbourhood of a ray on the positive semiaxis. This concludes our
preliminary description of the germs from G\.

1.3. Heuristic ideas. Operations with functional cochains.
We have shown in §1.2 that each germ Δ e G\ can be expressed as a
composition of germs belonging to the classes Aff, A°, AH0. The corrections
of germs from class Aff and A° belong to the Archimedean classes of the
germs of ξ, 2 or exp( —ξ), respectively; germs of the class AH0 belong to the
Archimedean class of exp( —exp ξ) as shown in §1.5 below and illustrated by
the following example.

Example.

Λ (ζ + exp (-ζ) ) = ζ + In (1 + exp (-ζ ) exp (-exp ζ)) =

= ζ + Xaj exp (—/ζ) exp (—; exp ζ),

dj e 1R; the actual values of the coefficients a,- are irrelevant.
Before expanding a composition Δ 6 G\ into terms from different
Archimedean classes, it is convenient to collect groups of all factors with
corrections from the same Archimedean class. It follows from the Remark in
§1.1 that this leads to normal factors generated by a set of germs with rapidly
decreasing corrections in the group of germs whose corrections do not
decrease any faster. In particular, this leads to the groups Ad(Aff)t^e and
Ad(A°)AH°. To describe these groups, we need to introduce classes of map

cochains other (or wider) than j^ff. This will be accomplished in the next
section. Here we define operations with functional cochains or map cochains
which lead ultimately to new classes of functional cochains. We shall not

Finiteness theorems for limit cycles 143

describe this procedure step by step, but only define the required classes and
verify their group-theoretical properties. This programme constitutes a major
part of the present paper.

Definition 1. The sum of two cochains F and G corresponding to partitions Ξ'
and Ξ" is a cochain corresponding to the product of partitions: Ξ = Ξ' Π Ξ".
The domains of the partition Ξ are all the non-empty intersections of pairs of
domains from Ξ' and Ξ". Assume that domains D' and D" of Ξ' and Ξ"
correspond to functions / and g from F and G. Then the domain D = D' Π D"
of Ξ corresponds to the function f+g of F+G.
Other arithmetic operations with functional cochains are defined similarly.
A composition of map cochains is defined along the same lines: F ° G is
the set of compositions of maps belonging to F and G corresponding to
domains of partitions Ξ' and Ξ" with non-empty intersections. The definition
is meaningful if the corrections of maps from G do not exceed some positive ε
and the maps from F are defined in ε-neighbourhoods of the corresponding
domains.
If a functional cochain F corresponding to a partition Ξ^ is defined in a
domain Ω, and ρ is a biholomorphic map from Ω to Ω, then a cochain F ° ρ
can be defined in Ω which consists of functions Fj <> ρ, where Fj are functions
belonging to F. If Dj is a domain of the partition Ξ^ corresponding to a
function Fj, then the function Fj ο ρ corresponds to the domain p~](D Π ρΩ )
of a new partition denoted by a F * and corresponding to the cochain Fop
(for more detailed discussion, see Propositions 1 and 2 of §1.4).
It can now be seen that the conjugation of normalizing cochains by affine
germs generates map cochains corresponding to "dilated standard partitions",
that is, partitions into half-strips by the rays η = μπ_/ for any μ > 0.
Compositions of such map cochains corresponding to different μ lead to
products of several dilated standard partitions. This gives rise to the simple
cochains that will be defined below. Conjugation of germs of class AH0 by
simple map cochains gives rise to sectorial cochains. We shall now state the
exact definitions.

1.4. Simple and sectorial map cochains.
The cochains defined below will be considered in special domains. All the
normalizing cochains and almost regular germs are considered only in the
logarithmic chart.

Definition 1. A standard domain of class L is a domain that can be represented
in the form

Ω = Ste (C+\K), i> c = ^ + C-JL_ , C>0 , .£ = {|ζ|<Λ} .

We recall that we consider only the branch of the logarithmic function that is
real on the positive semiaxis (L refers to "logarithm").

144 Yu.S. nyashenko

Remark. Standard domains of class η > 1 arise in the investigation of
compositions of class η > 1 and will be defined in the second part. Standard
domains of class L have the following properties (which motivated our
definition).
The germ of a domain at infinity is a class of domains such that the
complements of any two domains of this class with respect to some compact
domain (depending on the domains in question) are the same.
1. The main function F " of a set F forming a normalizing cochain can be
extended to the germ of the domain (In Ω, oo) where Ω is an arbitrary domain
of class L. We have
 (In Ω, oo) = ((A^c) Π, oo),

A^
c = In (exp ζ + ϋζ'
1
 exp ζ) = ζ + In (1 + CC"
1
);

here Π = ||η | <-y- , ξ > a\. Hence

(In Ω, oo) c (ΠΪ\ oo) for any ε (Ξ [Ο, 1)

(for the definition of the half-strip Π ^ see §0.6 and also §1.2).
2. Property 1 implies that

(exp ΙΓ;
ε
\ oo) ID (Ω, oo)

for any ε e [0, 1) and any domain Ω of class L.
3. The correction of \|/
c increases on (R+
 , oo) less rapidly than any linear
germ.
These properties will be used in the proof of the Phragmen — Lindelof
theorem for simple and sectorial cochains defined later.
4. The relation |ζ| 1- ε
 = o(Re ζ) holds in a standard domain of class L
for an arbitrary ε > 0. The following two properties motivate the introduction
of the parameter C.
5. Given an arbitrary standard domain of class L, there is another standard
domain of class L whose points have distances from the boundary of the given
domain that are greater than or equal to any preassigned constant.
6. The intersection of any two standard domains of class L contains a
domain of class L.

Definition 2a. A standard partition Ξ
 s t is a partition of a domain in C by rays
η = Kj,j e Z. The strip η € [n(J—l), nj] will be denoted by Π;.
Let us modify the standard partition. We recall that

Let us set n. = ni°\ nmai n =

Finileness theorems for limit cycles 145

Definition 2b. A modified standard partition ΞΜ is the partition of a standard
domain Ω of class L into half-strips IL Π Ω, j e Z\{0; 1} together with the
half-strips n ma i n , n o \n ma i n (see Fig. 4). The set n ma ; n is called the main
domain of the modified standard partition. Its lower boundary is denoted by
i?o an d is called special. L
 * •"main

Fig. 4

Definition 3. Let ρ : Ω -* Ω be a diffeomorphism of domains of class L,
ρΩ C Ω, σ = ρ" 1. Let Ξ be a partition of Ω. We then have a partition
σ,Ξ of Ω that is the image of Ξ under the diffeomorphism σ with domains

(σ.Ξ), = σ (Β, Π Ρ Ω).

where Ξ; are domains belonging to Ξ. By definition the domain (σ,Ξ)7·
corresponds to Ξ7· under the diffeomorphism σ.

Definition 4. Let
 σ = (μ1? . . .

μι > μ2 > · · · > VN > 0

be a set of linear maps. A simple partition of type σ is the product of
partitions μ_,·. Ξ81:
 2
(R) = Π μ,·* Ξβί.

A modified simple partition of type (σ, k) is the product

t Ν
s
(it) = ΓΙ μ;*Ξ
Μ · Π μ,·*Ξ
8{.
ι k-fi
Definition 5. A generalized ε-neighbourhood of the main domain of a modified
standard partition is the set
 Π<ε> — ΤΤ<
ε) Ι Ι ΤΤ ε

146 Yu.S. IVyashenko

where Yl\ is the ε-neighbourhood of the half-strip Πι, Π ^ = φ εΠ (see the
reminder before Definition 2b or §0.6).
We use the symbol 3>
ε
 to denote the ε-neighbourhood of a set 2!. For
uniformity, we shall call all the ε-neighbourhoods of domains of a standard
partition, and also the domains of a modified standard partition with the
exception of the main domain, as well as the generalized ε-neighbourhood of
the main domain generalized Ε-neighbourhoods of domains of a standard or
modified standard partition. Moreover, a (σ, €)-neighbourhood or a generalized
ε-neighbourhood of a domain of a simple (modified simple) partition of type σ
(type (σ, k)) that is defined as the intersection of domains μ,-Ξ; with Ξ
7·
belonging to the standard (modified standard) partition will be defined as the
intersection of the images of generalized ε-neighbourhoods of these domains
under the diffeomorphisms μ
;- : ζ Η μ_,ζ.

Definition 6. A clothing cochain of a simple partition of type σ corresponding
to constants C, C" and ε is a set of functions mc,se defined in ε-neighbourhoods
of the boundary rays of the partition as follows. Given a boundary ray Jz? of
the partition Ξ of type σ = (μι, ..., μ^ν), we define

m
c, s? (ζ) = Σ C exp (— C exp μ^ξ),

where the summation is over the values of j for which JS? C μ;9Ξ 8ΐ, where
δ E
sl is the union of all the rays of the partition E
st. The clothing cochain of a
modified simple partition of type (σ, k) corresponding to constants C, C" and ε
is a set of functions considered in ε-neighbourhoods of the boundary rays and
defined in the same way as above.

Remarks. The latter cochain is not defined in the neighbourhood of all the
boundary lines of the modified simple partition. It is not defined in the
neighbourhood of images μ
7·^ο> y
 =
 1> •·•» N, of the special boundary line of
the modified standard partition; these images are not rays.
We are now ready to define one of the two main classes of functional
cochains that will be needed later: simple cochains.

Definition 7. A n ^.-simple cochain of type σ = (μι , ..., μ^) , μι > μ2 > ••·
... > μ/ντ > 0, is a functional cochain F defined in some standard domain of
class L and satisfying the following conditions:
1. The corresponding partition E
F
 is simple of type σ.
2. The functions of the set F can be extended holomorphically to
(σ, 8)-neighourhoods of the corresponding domains for some ε > 0 depending
only on F; this property is called the ε-extensibility of the cochain.
3. There is a v e R such that \F\ < exp νξ. If it is possible to choose a
ν < 0 in this estimate, then the cochain is said to be rapidly decreasing.
4. The modulus of the coboundary 8F is majorized by a clothing cochain
of E
F
 corresponding to some positive C, C" and ε in the domain of definition
of this cochain.
 Finiteness theorems for limit cycles 147

Definition 8. A simple cochain of type (σ, k), where σ is the same as in
Definition 7, is a functional cochain F defined in some standard domain of
class L and satisfying the following conditions:
1. The corresponding partition Ξ^ is a modified simple partition of type
(σ, k).
2.-4. The conditions 2—4 are repeated verbatim from Definition 7.

Remarks. 1. No estimate is imposed on the coboundary in the neighbourhoods
of images μ;·^Ό of the special boundary line of the modified standard partition.
2. An R-simple partition of type σ and the modified simple partition of
type (σ, k) coincide in the open upper half-plane.

Definition 9. A simple functional cochain of type σ = (μ], ..., μ^) is a set of
N+ 1 cochains consisting of an IR-simple cochain of type σ and of simple
cochains of type (σ, k) that coincide in the intersection of the open upper
half-plane with some standard domain of class L. These cochains are called
respectively the R-realization and the (σ, k) or k-realization of the simple
cochain F; they will be denoted by F^ and F^. The parameter Ν is said to
be the numerical type of the cochain F. If all the cochains of the set are
rapidly decreasing, then the set itself is called a rapidly decreasing cochain.

Examples. 1. A normalizing cochain written in the logarithmic chart is a
simple functional cochain. This follows from the results of §1.2.
2. An almost regular map determines a simple functional cochain with a
trivial (zero) coboundary. The same applies also to an arbitrary function that
is holomorphic and increases no faster than exp νξ, ν > 0, in a quadratic
standard domain or in a standard domain of class L (the former type of
domain includes the domains of the latter class).
We shall now define the other important class, namely sectorial cochains.
We recall our definition of the image of a partition under a diffeomorphism
(see Definition 3). We shall need partitions and domains that are obtained
from those described in Definitions 4 and 5 under the diffeomorphism exp.

Definition 10. Let Ξ be a simple partition of type

σ = (μ ΐ 5 . . ., μΝ), 1 > μ ι > . . . > μΝ > 0.

A sectorial partition of type σ = (exp ° μι, ..., exp ° μ^) is the image of Ξ
under the diffeomorphism exp; it is considered in standard domains of class L.
A modified sectorial partition of type (σ, k) is the image of a modified
simple partition of type (σ , k) under the diffeomorphism exp.
Α (σ, z)-neighbourhood or a generalized ε-neighbourhood of a domain of a
sectorial {modified sectorial) partition of type σ or (σ, k) is the image of a
(σ , e)-neighbourhood of a domain of a simple partition of type σ or (σ , k)
under the diffeomorphism exp upon intersection with the ε-neighbourhood of
the standard neighbourhood of class L in which the partition is considered.

148 Yu.S. IVyashenko

We further define an (exp, ^-neighbourhood of a ray i£ with vertex Ο to be
the sector with vertex 0, bisector if', and angle 2ε. A similar neighbourhood of
a ray of partition of a domain Ω is the intersection of the (exp, e)-neighbourhood
of the ray with the ε-neighbourhood of Ω.

Definition 11. A clothing cochain of a sectorial partition of type σ (or type
(σ, k)), σ = expo σ , σ = (μι, ..., μΝ) is the composition mc°ln, where mc
is the clothing cochain corresponding to a simple partition of type σ
(or (σ , k)); it is considered in the union of the (exp, 8)-neighbourhoods of
the partition rays for some ε > 0.
The clothing cochain of a sectorial partition can be described explicitly as
follows: the function me of the clothing cochain has the following form in
the (exp, 8)-neighbourhood of a boundary ray if:

mc.se (ζ) = ZC'exp(- C | ζ \μϊ\

where the summation is over the values of j for which ££ C exp ° μ/·9Ξβ1 for
partitions of type σ; if C exp ° μ; 9 ΞΜ for 1 ^ j ^ k and if C exp ° μ;·9 a s t
for k + 1 =ζ j < Ν in the case of partitions of type (σ, k).

Definition 12. a) An R-sectorial cochain of type

σ = (exp ο μ 1; . . ., exp ° μ Ν), 1 > μχ > . . . > μΝ > 0

is a functional cochain F defined on some standard domain of class L and
satisfying the following conditions:
1. The corresponding partition Ξ^ is sectorial of type σ.
2. The functions of the set F can be extended holomorphically to
(σ, 8)-neighbourhoods of the partition domains for some ε > 0 (this property
is called (σ, ^-extensibility or simply ε-extensibility of the cochain).
3. There is a v 6 R such that |F| < exp νξ. If we can choose ν < 0 in
this estimate, then the cochain is said to be rapidly decreasing.
4. The modulus of the coboundary bF is majorized by a clothing cochain
of Ξ^ corresponding to some positive C", C and ε in the domain of definition
of the cochain.
b) A sectorial cochain of type (σ, k) is defined similarly, only the
corresponding partition aF is sectorial of type (σ, k) and not of type σ.

Remark. An R-sectorial partition of type σ and a modified sectorial partition
of type (σ, k) in the open upper half-plane coincide. The following definition
is obtained when "simple cochains" are replaced in Definition 9 by "sectorial"
ones.

Definition 13. A sectorial functional cochain of type σ = (exp ° μι, ..., exp
is a set of the following N+ 1 cochains: an R-sectorial functional cochain of
type σ and sectorial cochains of type (σ, k), 1 ^ k < N, which coincide in
the intersection of the open upper half-plane with some standard domain of
class L. The cochains are called, respectively, the ^-realization and the (σ, k)-

Finiteness theorems for limit cycles 149

or k-realization of the sectorial cochain F and are denoted by F^ and /<*).
The parameter Ν is said to be the numerical type of the cochain. If all the
cochains of the set are rapidly decreasing, then the whole set is said to be a
rapidly decreasing cochain.
We need different realizations of the same cochain for the following reasons.
Firstly, they can be used to give precise meaning to the statement "for any
simple cochain F the superposition F°l n is a sectorial cochain", which can
then be proved.
Secondly, the Phragmen — Lindelof theorem holds for simple and sectorial
cochains (see §1.7 and §3); the proof requires that different realizations of the
same cochain be considered. Let us now state the exact definitions.

Definition 14. Let Ω and Ω be two standard domains of class L, and
ρ : Ω ->!l a biholomorphic immersion. Assume that F is a functional cochain
in Ω corresponding to a partition EF. Then Fo p is a functional cochain
corresponding to the partition σ+ΞΓ. Let Ξ7· be a domain of EF, and Fj the
corresponding function from F; then Fj ° ρ is a function from F ° ρ considered
in the domain (σ*Ξ),· (see Definition 3).
If F in Definition 14 is either simple or sectorial, Ω = Ω and Ω = Ω
are domains in the upper half-plane, and F ° ρ is the cochain in Ω + defined
above, then Fo ρ is said to be a simple or sectorial cochain of numerical type Ν
if this composition is the restriction to Ω + of each of the N+ 1 (identical in
the upper half-plane) realizations of some simple (sectorial) cochain.

Proposition 1. Let F be a simple cochain. Then Fo In is a sectorial cochain
which increases no faster than some power.

<\ Assume that F is a cochain of type σ = (μ], ..., μ^). We consider the
standard domain Ω of class 1 in which the cochain F is defined, and a domain
Ω of the same class such that In Ω C Ω. The domain Ω should be chosen
to satisfy an additional requirement that will be specified later. Let

Ω
+ = Ω Π {η > 0}, Ω+ = Ω Π {η > 0}.

We shall consider three cases. In each case, we choose appropriate
realizations of F to obtain a realization of Fo p.

Case 1: μΝ^ I. Let F be a (σ , ΛΟ-realization of F. The main domain of the
partition of type (σ , Ν) has the form μΛτΠπ13ίη and includes n ma j n ; here n mai n
is the main domain of a modified standard partition (see Definition 2b). The
domain exp n mai n contains a standard domain Ω of class L (see Property 2 of
domains of class L at the beginning of this section). It follows that F ° In can
be extended from the domain Ω Π {η > 0} in the upper half-plane to a
holomorphic function defined on the standard domain Ω. This holomorphic
function increases no faster than exp ο ν Re In ζ = |ζ| ν, and is thus a sectorial
cochain with a trivial coboundary (see Example 2 after Definition 9; a non-
existent partition (with an empty boundary) is both sectorial and simple).

150 Yu.S. Il'yashenko

The rates of increase of the composition in Cases 2 and 3 below are estimated
similarly and we shall not discuss this procedure in detail.

Case 2: μι ^ 1 > μ^. We take ko such that μ^ο ^ 1 > μ^+ι and show
that F ο In is a sectorial cochain of numerical type N—k0. For k = k0 we
consider a (σ, ^-realization F(k) of F. Again let n ma i n be the main domain
of a modified standard partition. Then (exp° [ij)Tlmiin D Ω for any./ < k.
Hence there are no partition lines in Ω for (exp ο μ;)ΞΜ with j < k. It follows
that the image of the partition of type (σ , k) regarded as a partition of Ω is
a sectorial partition of Ω of type

σ = (exp ο μ κ§+1, . . ., exp ο μΝ).

The composition F^ ο In is an R-sectorial cochain of type σ and numerical
type N—k0- All the conditions of Definition 12a can be easily verified.
Now let k0 < k < N, I = k—k0. We construct a (σ, /)-realization of
Fop. Let us consider a (σ , fc)-realization F^ of F. The composition F ^ <> In
is then a sectorial cochain of type (σ, /). Hence the set (F ^ ο In, ..., F ^ ° In)
is a sectorial cochain of type σ.

Case 3: 1 > μι. Let F
(JR) be the R-realization of F and F^ its (σ , fc)-realization.
The set (F^ ° In,..., F^N) ° In) is then a sectorial cochain of type

(*) σ = (exp ο μ 1 ; . . ., exp ο

Remark. Assume as before that F^ is the IR-realization of a simple cochain F.
Then FflR) ο In for μι > 1 is not in general a realization of a sectorial cochain.
In fact, on the ray (R+ , oo) (which is a partition ray for an R-realization) the
coboundary 3(F(R) ο In) is bounded from above by the clothing function

Ν _ χ
2 exp (—£|ζ| μ ' ); the first term decreases no faster, and for μι > 1 more
1
slowly, than exp( —Cξ). Meanwhile all the functions of the clothing cochains
defined above decrease faster than any exponential function exp(—νξ), ν > 0
(which plays a key role in the proof of the Phragmen — Lindelof theorem). It
follows that the coboundary for F<$) ο In does not satisfy the estimate imposed
in the condition 4 of Definition 12.

Proposition 2. Let F be a sectorial cochain of type (*), λ e (0, 1). Let
μ*λ~' ^ 1 > μ/Ε+ιλ""
1. The composition F<^ x is then a sectorial cochain of
type (exp ° μ^+ιλ" 1, ..., exp ο μ^λ" 1).

< The proof goes along the same lines as that of Proposition 1. t>

In conclusion, we shall state several additional definitions. R-simple and
IR-sectorial partitions of a domain that is symmetric about the real axis retain
this symmetry; the positive semiaxis includes a boundary ray of such partitions.
The restrictions to it of the functions of the set are a pair of functions on
(R+ , oo). This motivates the following definition:

Finiteness theorems for limit cycles 151

Definition 15. A functional cochain F is said to be weakly real if F(z) = F(z)
on (R + , oo). A simple (sectorial) cochain is weakly real if its R-realization is
weakly real.

Notation. We shall denote the set of all simple cochains by ^^reg, the set of
rapidly decreasing simple cochains by S^ieg, and those of weakly real and
rapidly decreasing weakly real cochains by f^Rre? and f??Rreg · Similar sets
for sectorial cochains are denoted by f%\ag, f9o™ g, f^Rreg and fi?jRreg·

Definition 16. A sectorial cochain satisfying the estimate \F\ < Cξ~ 5 for
some C > 0 is said to be weakly decreasing. The set of all such cochains is
denoted by f^ w (from weakly regular).
All these definitions concern only some of the properties of the functional
cochains of classes 0 and 1 defined below, so-called regularity. The other
fundamental property is expandability. This property is described for cochains
of class 1 in §1.5 below; for simple cochains we proceed to define it now.
A generalized Dulac series is a series

where Pj are polynomials. If the polynomials P} are real, the series is said to
be real.

Remark. Not all the ν in the generalized Dulac series are positive, but there
are only finitely many negative ones.

Definition 17. A simple functional cochain is said to be a cochain of class 0 if
it can be expanded in a generalized Dulac series. Expandibility means that
there is a standard domain of class L where, given any ν > 0, there is a
partial sum of the series that approximates simultaneously all the functions of
the set forming the cochain to within o(exp( — νξ)) uniformly with respect to
all functions. The set of all such cochains is denoted by f $°.
The set $Γ~Ί§\ of rapidly decreasing cochains of class 1 defined below
consists of rapidly decreasing sectorial cochains that can be expanded in
superaccurate asymptotic series, which will now be described.

1.5. Superaccurate asymptotic series and cochains of class 1.
The series and cochains defined below have a non-negative integral rank r,
and the definitions are formulated by induction on r. The exponents of the
superaccurate asymptotic series are independent of the rank, whereas the
coefficients depend on it.

Definition 1. The set El of the exponents of superaccurate asymptotic series of
class 1 is the set of sums of real quasipolynomials with exponents μ, 0 ^ μ =ξ Ι.
The quasipolynomial with μ = 1 has degree zero: this means that there is a
finite, possibly zero, limit ν = v(e) = lim —^—- on (R+ , oo). This limit is

called the principal index of the monomial with exponent e.

152 Yu.S. IVyashenko

The initial induction step is the definition of superaccurate series of rank 0
(r = 0).

Definition 2. The set CfC 1^0 of coefficients o/SAAS-(l, 0) {superaccurate
series of class 1 and rank 0) is the set of all simple functional cochains (not
necessarily weakly real). The SAAS-(1, 0) is a series of the form

Σ = 3 aj exp e^, e,· e Ε1, ν (e;) S» — oo, a} e •^
1>0 Ξ $φ.
i

Definition 3. A cochain is said to be expandable in SAAS-(1, 0) Σ if there is a
standard domain Ω of class L depending on the cochain such that for any
ν > 0 there is a partial sum Σ! of Σ which approximates the composition
F° exp in the domain In Ω to within o(exp(—ν exp ξ)):

| F — 2 X | = ο (exp (—ν exp ξ)) in the domain In Ω.

f Ψ-< ° (f %
x
l °) is defined to be the set of sectorial functional cochains that
are expandable in SAAS-(1, 0) with arbitrary (negative) principal exponents of
terms. The first set is the set of cochains of class 1, and the second set is the
set of rapidly decreasing cochains of class 1 and rank 0.

The induction step, that is, the transition from r to r + 1. Assume that we
have defined series of class SAAS-(1, r) and cochains of class &<&1'r. We
denote by ^C(s/\, ..., s/χ) the real linear hull of the sets s/i, ..

Definition 4.

We now define SAAS-(1, r+ 1) by the standard formula

Σ = Σα} exp e,·, e_, <Ξ Ε1, ν (e,·) - ^ — oo, as ι= 3Γ 1· r+1.

An SAAS-(1, r) Σ is said to be weakly real if all its partial sums Σι satisfy
Σ,(ζ) = Σ7?) on (R + , oo).
The set of all SAAS-(1, r) is denoted by &1·r, and that of all weakly real
SAAS-0, r) by «Jjr.

Definition 5. Expandability into an SAAS-(1, r) for any r is defined in the
same way as for r = 0 (see Definition 3).

The set tf^
1
'
r+1 of functional cochains of class 1 and rank r+ 1 an d th e set
&¥}+
 r + of rapidly decreasing functional cochains of class 1 and rank r+ 1 ar e
sets of sectorial functional cochains that are expandable into SAAS-(1, r+1)
with arbitrary (or with negative) principal exponents of terms. We denote by
Fefaf*1 the set of all weakly real cochains of class f« + r+1 .

Superaccurate series and functional cochains of class 1 are the series and
cochains of any rank (the subscript (+ ) indicates that the corresponding

Finiteness theorems for limit cycles 153

formulae hold both with the subscript + and without):

oo oo
<»R
 =
 U $R ' ^>R(+) = U
ο ο

Examples. 1. Let g e <9
0 be the germ of a holomorphic map (C, 0) -> (C, 0)
with a unit multiplier, and g its form in the logarithmic chart. Then

Ag - id e ^ ο exp.

< The germ g can be expanded in some half-plane ξ ^ α in a convergent
series
 g (ζ) = ζ + Σα
} exp (-/ζ).

We have

{Ag) (ζ) = In [exp ζ (1 + (exp (-ζ) ) Σα, exp (-/ exp ζ))] = ζ + In [1 +

+ exp (—ζ) Σα
} exp (—/ exp ζ)].

The function F = In I-] in the half-strip Π : ξ ^ α, Ι η I < π/2 can be
expanded in a convergent series of class SAAS-(1, 0). This function is equal
to Ag —ζ and is holomorphic in Π; hence F° In is holomorphic in C+
 \k,
where k is the disc |ζ| ^ exp a, and it decreases exponentially:

| F ο In | < C exp (-ξ/2).

This means that F ° In is a sectonal cochain with zero coboundary. \>

2. Let/ : (R+
 , oo) ->· (K+
 , oo) be an almost regular germ,/e » . Then
Af— ζ is a holomorphic function in Ω = C +
 \k for a large enough disc k, and
it is expandable in an SAAS-(1, 0) in Ω.
The proof follows that for Example 1.
Similarly AH
0
 d id + $%\ ο exp.

3. Two superaccurate asymptotic series can be equal even if the
corresponding exponents and coefficients of the terms are not equal (in contrast
to Dulac series). For example, the monomials aj exp ej,j = 1, 2, for

a
x = 1, .e x = —exp ζ + ζ and α2 = exp ζ, e2 = —exp ζ

are equal. It is possible to impose a normalization so that the exponents and
coefficients of terms are determined uniquely by the series; however, this is
difficult for series of class 1 and becomes quite impossible for series of an
arbitrary class, which will be defined in the second part. We shall therefore
adopt instead of an "algebraic" (term by term) definition of equality of
superaccurate series the following "analytic" definition.

154 Yu.S. ll'yashenko

Definition 6. An SAAS-l is equal to zero if, given any ν > 0, all but finitely
many of its partial sums are o(exp(—ν exp ξ)) on (K+ , oo). Two SAAS-1 are
equal if their difference is equal to zero.

1.6. Additive and multiplicative expansion theorems.

We define the following germ classes:

/° = Ad (Aff) .Ao;

we recall that

«io = Gr (gF, # <Ξ M\ F <= ^r% | there is a germ g l e O0: {AgJ Fu e *%) .

We set
 H1 = Ad (K+) (id + $%\ ο exp).
We have shown in Example 2 of §1.5 that AH0 C Hl. Moreover, we have
df C / · This together with (*) of §1.2 implies that

G1 d Gr (H1, J°, Aff).

We set
 G1 = Aff ο jo ο Η1.

The superscript indicates that we have completed the construction.

Multiplicative expansion theorem. G1 is a group containing G\.

We shall prove the identity theorem for germs from the group G1.

Remarks. 1. The first assertion of the multiplicative expansion theorem implies
the second one. Indeed, if C?
1 is a group, then G1 = GT(H\ J°, Aff) 3 d .
2. The multiplicative expansion theorem can be used to express monodromy
transformations of class 1 as compositions of germs whose (non-zero)
corrections belong to different Archimedean classes with the representatives ξ
or 2 for Aff, εχρ(-ξ ) for J°, and {exp(-exp μξ)|μ > 0} for Hl.

Additive expansion theorem. Let A be a monodromy transformation of class 1
or, more generally, A e G1. Then

Ν
(*) Δ = α + φ + Σ %
1

α <Ξ Aff, φ

if a = id, φ = 0, ψ 4 φ 0, then

In other words, φ in the expansion (*) is a simple rapidly decreasing weakly real
cochain; \|/y are sectorial rapidly decreasing cochains; and if the first two terms
in the sum give id, then the cochain ψι is weakly real.

Finiteness theorems for limit cycles 155

Remark. It follows from condition 3 of Definition 12 in §1.4 that in the
additive expansion theorem we have

| φ | -< exp (—εξ) on (R +, oo),

| ty) ο exp ο μ^ Ι -< exp (—ε exp μ>ξ) on (R+, oo)

for some ε > 0.
The proof of this theorem takes up a major part of this paper, see §§1.8
and 1.9 and §§2 and 4; it is used to deduce the identity theorem, which in
turn leads to the Phragmen — Lindelof theorem (§3).

The Phragmin - Lindelof theorem. A simple or sectorial cochain that decreases
on (R + , oo) faster than any exponential function is identically zero on K +.

The coboundary of a simple or sectorial cochain always decreases faster
than any exponential function. Hence if the main function of the set forming
an R-simple or R-sectorial cochain decreases on (R + , oo) faster than any
exponential function, then the other function corresponding to the partition
domain adjacent to R+ from below behaves similarly. For other realizations
on ((R
+ , oo) only one of the functions of the set is defined.

1.7. Derivation of the finiteness theorem from auxiliary results.
Let Δ e G1 Π Fix». Four cases may arise in the expansion (*) for Δ.

Case 1: α Φ id. The difference a—id is non-zero, and the other terms tend
to zero on (R + , oo). In this case Δ φ Fix».

Case 2: a = id and φ Φ 0 on (R + , oo). In this case, the Dulac series φ for
φ is non-zero, since otherwise it would follow from the definition of
expandability that the germ φ decreases on the real semiaxis faster than any
exponential function and it would be identically zero on (R + , oo) by virtue of
the Phragmen — Lindelof theorem. Each term of the non-zero Dulac series φ
is small compared with the preceding term (naturally, all the terms are non-
zero); let α ι be the first term of the series. Then α ι = Ρ(ζ) exp(—νζ), ν > 0
and Ρ is a real polynomial; φ = ai(l+c(l)), \|/y ο exp ο μ7- = α\θ{\). Hence
Δ-i d = α,(1 + ο(1)) Φ 0 on (R + , oo). We have again Δ φ Fix*,.

Case 3: a = id, φ = 0, and the germs \|/,· are not all zero; we can assume
without loss of generality that ψι Φ 0. In this case, the SAAS-1 for ψ] is
non-zero by the Phragmen — Lindelof theorem. Example 2 in §1.5 shows that
the terms of SAAS-1 cannot be ordered as easily as the terms of Dulac series.
We shall use the following theorem which will be proved in §4.

Theorem on the lower bound. Let Σ be a weakly real SAAS-X, ν the maximum
principal index of the terms ofL, and Σι a partial sum of the series. We then
have for an arbitrary ε > 0

Re Σ j > exp ((v — ε) exp %)) on (R+, oo).

156 Yu.S. Iiyashenko

Remark. A similar upper bound is quite obvious. Under the hypotheses of the
theorem, any partial sum of Σ has the following upper bound: for any ε > 0,

| Σ , | ^ex p ((ν +ε)βχ ρ ξ) on (R+, oo).

Corollary. Let ψ e f C
S$+ be a cochain that is expandable in an SAAS-X Σ
(see Definitions 3 and 5 in §1.5) and assume that Σ satisfies the hypotheses of
the theorem on the lower bound. Then for any ε > 0

Ret|) ο exp >- exp ((v — ε) exp 1) on (R+, oo).

We now return to the proof of the identity theorem. Since μ, > μ! for
j > 1 in the expansion (*) in §1.6, we obtain in (IR+, oo)
\m
1 2 ψ, ° exp ο μ_,· I -< exp (— exp (μχ + ε) ξ)
2
for any ε > 0 that is small enough. The corollary implies that

Re ψ! ο exp ° μι >- exp (—exp (μ! +y ) I)

on (K+ , oo). Hence we have on (R + , oo)

Re(A —id) = Re( > % ° ex P ° Κ?) Vex p (— exp ^ + -γ-jl) —

- exp ( - exp (μχ + ε) ξ) >- exp ( - exp (μ χ + -|-) ξ)

This means that Δ φ Fix,» also in this case.

Case 4. In the expansion (*) for Δ, a = id and φ = \|/y = 0. Then Δ = id.
This completes the proof of the identity theorem subject to the validity of the
preceding auxiliary theorems.
In the next section, we formulate lemmas required in the derivation of the
additive expansion theorem. These lemmas will be proved in §§2 and 4.

1.8. Group properties of map cochains.
The following lemmas are to a large extent motivated by the following
obvious idea: the functions exp( —ξ) and exp(—/(ξ)) belong to the same
multiplicative Archimedean class provided that the function / increases at
infinity no faster and no slower than a linear function; these functions belong
to different Archimedean classes if either / increases faster than any linear or
slower than any linear function. A shift (of an argument) signifies a change
of variables, often in the form ξ (->• ξ 4- ^(ξ), F = ο(ξ), which explains the
terminology. The lemmas are given names and are labelled by abbreviations
in parentheses for reference.

First lemma on shifts (LSI).
a) f$° ο Aff = fS°,
b) f^1 ο exp ο μ ο (id+ C + f&l) = fig1 « exp ° μ for an arbitrary C € Κ
and μ > 0.
 Finiteness theorems for limit cycles 157

For brevity, we use the notation

Κ = fW ο exp ο μ, μ > 0; fί = (J £* .

Second lemma on shifts (LS2).
a) The set id + fS" , η = 0, 1 « c/oied w«rfer compositions;

b) (id + f C?)-i = id + «, . η = 0,1;

c) ^°o(i d + r i
moreover for φ
 φ ο (id + f\) ci

d) let 0 < μ ^ v, r/zen

moreover for φεί ί

φ ο (id + fly) (Ζ φ + ^ίν ·

iVi/ femmi on ίΑί/is (LS3). Le? μ ^ v, then

ff +)ll ο (id + fU) C ^(+)μ-

The subscript ( + ) indicates that the formula holds both with the subscript
+ and without.

Fourth lemma on shifts (LS4).
a) jo C id + f<®&\
b) f1 ο jo c F 1 .

Lemma on conjugation.
a) Ad (Aff)(id + #X ) = id
b) Ad

and moreover if g e 0t and μ = lim g', then
(R+, « )

Ad (tf)(id + ^ ν ) C id + fly.y,

c) Ad (Z
0)/?1 = H 1.

Remarks. 1. The proofs of these lemmas are similar to the proofs of set
identities, that is, we establish that one well-defined set is included in another.
In spite of this simple scheme, the proofs are quite lengthy and technical.
However, it is the choice of correct definitions rather than the proofs which
presents the main difficulty (see §§1.4 and 1.5).
2. The lemma on conjugation has a simple proof, in contrast to the other
lemmas. It follows almost immediately from LSI and LS4 (see §4.6).
The lemmas of this section will be used to derive the multiplicative and
additive expansion theorems.

158 Yu.S. Il'yashenko

1.9. Proofs of the expansion theorems.
<\ Proof of the multiplicative expansion theorem. The theorem is equivalent to
the simultaneous validity of the following three assertions:

I. G'oG 1 = G
1 II . (G1)'1 = G
1 III . Gx C G1.

Proof of assertion I. We need to prove that

Aff ο jo c Η1 ο Aff ο jo ο Η1 = Aff ο jo ο Η1.

It is sufficient to show that
1°. Ad (Aff)tf
1 = H1,
2°. Ad (Aff)/
0 = J°,
3°. Ad (JO)H1 = fl1.
Assertion 1° follows directly from the result b) of the lemma on conjugation,
since Aff C ^-
Assertion 2° follows directly from the definition of J°.
Assertion 3° follows from the result c) of the lemma on conjugation.

Proof of assertion II. Clearly AfT 1 = Aff, (Ζ)" 1 = / , (Τ/1)"1 = Η1,
because they are all groups. Hence

(G
1)-
1 = Η1 ο jo ο Aff = G1.

Here the last equality follows from 1° — 3°.
Assertion III follows from the inclusion (see §1.6)

Gi C Gr (H\ jo, Aff)

and from I. This completes the proof of the multiplicative expansion
theorem. >

Proof of the additive expansion theorem. Let Δ e G
1 = Aff ο /* ο Η1. By a) of
LS4 we have
 J° d id $&
Clearly Aff c /° e Aff + f^+, Aff ο (id + f&) a Aff + fi+.

It then follows from LS2 and LS3 that (1 ) H1 C id + if^V) . Finally, LS2
implies that
 f <#& ο (id + fl) cz f%l+ + f I-

Hence

(1)
Only the inclusion (id + ^ l +)~ l C id + ^ + requires an explanation. It can be deduced
from LS2 b) provided we show that A~
l
(id + &r\.i<u C id + ^C+. We can prove that
exp ο (ln + J^ + ki ο In) = ζ exp J^ V C id + ^ifV. The last inclusion follows from a
simple completeness lemma, see §4.2.

Finiteness theorems for limit cycles 159

Finally,
 ψ; <Ξ fl^ = $%\ ο exp ο μ,·.

This is the expansion (*). It remains to verify that the cochain ψι in the
expression ψ ι = ψι ο exp ο μ, is weakly real if a = id and φ = 0.
Let R and / be operators from fS1 to f 'SJR defined as follows:

It is obvious that BA) and /ψ are weakly real cochains. A simple or sectorial
cochain ψ is weakly real if and only if its R-realization ψ^) satisfies

-βψ(Κ) = Ψ(Κ), H\\R) = 0 on (R+, oo).

We shall show that the germ ψι in the expansion (*) is weakly real for
α + φ = id. Let ψκκ) be the R-realization of the cochain ψι, and ψ" and ψί
the functions of the set ψκκ> corresponding to the sectors that are adjacent to
R + from above and from below. Then

Δ — id = ψ" ο exp ° μχ + ο (exp (—exp ο μ1 (1 + ε))).

Hence
 Im ψ? = ο (exp (-ξ 1+ε)).

The estimate for the coboundary of a sectorial cochain (condition 4 of
Definiton 12) indicates that a similar estimate holds also for Im ψί for a small
positive ε. Hence

for some ε > 0. It now follows from the Phragmen — Lindelof theorem that

This implies that ψΐ(|β) is a weakly real cochain.
This completes the proof of the additive expansion theorem.
To prove the identity theorem Β of §0.6, we still need to prove the lemmas
of §1.8, the Phragmen —Lindelof theorem of §1.6, and the theorem on the
lower bound of §1.7.

§2. Function-theoretic properties of simple and sectorial cochains

We shall now prove the "function-theoretic parts" of the lemmas in §1.8;
such formulations are obtained when P^1 is replaced in all the lemmas by
J^^ieg, that is, by taking sectorial cochains instead of cochains of class 1
(see Definition 13 of §1.4), thus retaining the requirement of regularity but

160 Yu.S. IVyashenko

dropping the condition of expandability in SAAS-1. Only the lemma on
conjugation will not be considered, since both regularity and expandability will
be proved simultaneously in §4.
To begin with, we shall discuss the simplest properties of functional cochains.

2.1. Differential algebras of cochains.
Definition 1. Two simple (sectorial) cochains are said to be equivalent if they
coincide in the intersection of some standard domain of class L with the upper
half-plane (see Definition 1 of §1.4). A class of equivalent simple (sectorial)
cochains is called a germ (at infinity, but this is often omitted) of a simple
(sectorial) cochain.

Lemma 1. Germs of simple functional cochains form a differential algebra.
The same applies also to germs of sectorial cochains. This means that the sums,
differences, products, and derivatives of simple (sectorial) cochains can be
extended from the intersection of a standard domain of class L with the upper
half-plane to the whole domain as simple (sectorial) cochains.

Let/an d g be germs of real functions on (R + , oo). The inequality/ -< g
means that there are representatives of the corresponding germs (denoted by
the same letter) satisfying the inequality / < g at all points. For a germ F of
a simple or sectorial cochain and a germ/of a function on (R + , oo), the
inequality \F\ •< / ° Re indicates that there are representatives of F and/suc h
that all the functions Fj of the set F satisfy the inequalities

| Fj | < / ο Re, where Re ζ = ξ.

Since simple and sectorial cochains admit several realizations, the operations
with such cochains require clarification. In fact, all the realizations of a single
cochain coincide in the upper half-plane. As a result, we define all the
operations for restrictions of simple and sectorial cochains to intersections of
standard domains of class L with the upper half-plane.

< The proof of Lemma 1 follows almost immediately from the definitions.
Let F\ and F2 be two simple (sectorial) cochains of types σι and σ2, and
F\ + F2 = F their sum in the upper half-plane (the difference and product can
be analysed along the same lines). We shall prove that F can be extended to
a simple (sectorial) cochain of type σ = O] U cs2. Let σι = (μι μ^),
σ2 = (vi, ..., ν Μ ) , σ = (λι, ..., λκ), Κ «ξ Μ+Ν, for simple cochains and

σ1 = (exp ο μ ΐ5 . . ., exp ° μΝ), σ2 = (exp ο v l t , . ., exp ο ν Μ ) ,
σ = (exp ο λ^ . . ., exp ο λ^), Κ <^ Μ + -Ν,

for sectorial cochains, where the numbers in each set decrease monotonically.
For any k, 1 < k ^ K, we construct a (σ, k) realization F(k) of F; the
R-realization is constructed similarly. We dioose fci and k^ so that
μ*, > λ* > μ*ι + 1, vkl > Xk > v^+i. Let F , = F i(kt) and F2 = F^ be,
respectively, k\- and /^-realizations of F\ and F2. We shall show that

Finiteness theorems for limit cycles 161

F = F 1 + F2IS a simple (sectorial) cochain of type (σ, k) (see Definitions 8
and 12b of §1.4); this is the required realization of F.
Let us verify all the conditons of Definitions 8 and 12b of §1.4. Let Ξι
and Ξ2 be the modified simple (sectorial) partitions of type (aj, k\) and (σ2, k2)
corresponding to F \ and F 2. Their product Ξ = Ξι · Ξ2 is then a modified
simple (sectorial) partition of type (σ, k).
By definition of the sum of cochains, the cochain F = F 1 + F 2 corresponds
to the partition Ξ; the ε-extensibility ((exp, e)-extensibility) of the sum and its
exponential upper bound follow from similar properties of the components.
This confirms conditions 1 — 3 of Definitions 8 and 12b for the cochain F.
We now only need to verify the estimate for the coboundary. The product
of partitions, whether simple or sectorial, corresponds to the sum of clothing
cochains (see (Definitions 6 and 11 of §1.4). We have

δ (Ρ, + Ft) = 6F1 + δΡ,.

It follows immediately that the coboundary of the sum is bounded from above
by the corresponding clothing cochain. This proves Lemma 1 for the sum of
simple and sectorial cochains. This proof can be repeated verbatim for the
difference.
Consider the product

Ι δ (W l < I Fi II δ^ 2 I + I ^2 I I δ*Ί Κ (exp νξΧτη
1 + m2).

Here m1 and m2 arejilothingjcochains of the partitions Ξι and Ξ 2 that majorize
the coboundaries hF\ and 5F2; \Fj\ < exp νξ, j = 1, 2.
But the product of a clothing cochain of a simple or a sectorial partition
with an exponential function is majorized by some other clothing cochain
corresponding to the same partition. For simple cochains this follows from
the inequality
 exp (νξ — C exp μξ) -< exp (—C exp μξ)

which holds for arbitrary ν > 0, μ > 0, 0 < C" < C; for sectorial cochains
it follows from the inequality

exp (νξ - C Ι ζ η < exp (- C | ζ |μ)

for arbitrary μ > 1, ν > 0, 0 < C < C.
This completes the proof of the lemma for the sum, the difference, and the
product.
The derivative of a simple or a sectorial cochain is again a cochain of the
same type but corresponding to a smaller value of ε (see condition 2 of
Definitions 8 and 12 in §1.4). This follows from the Cauchy inequality and
from the fact that the gap between (σ, e)-neighbourhoods of domains of
simple (sectorial) partitions for different values of ε is either separated from
zero or can be bounded from below by the function CZ,~3 for some C > 0.
This proves the lemma. >

162 Yu.S. IVyashenko

Lemma 2. The germs of cochains of class η for η = 0 and η = 1 form a
differential algebra.

We shall now prove this lemma completely for η = 0, and for part of the
proof for η = 1 we refer the reader to §4.1.

<\ We need to verify that the generalized Dulac series and SAAS-1 form
differential algebras. For Dulac series this is trivial. The set of SAAS-1 is
closed under addition and differentiation, which follows trivially from the
definitions of §1.5. The fact that this set is closed under multiplication will be
proved in §4.1.
Expandability in SAAS-1 is preserved under addition, subtraction,
multiplication, and differentiation; this can be verified by confirming that the
residual terms for the sum, product, and difference remain small. Such
estimates are standard and will not be carried out in detail. This completes
the proof of Lemma 2 for cochains of class 0 and 1. >

2.2. Completeness.
Let us choose a fixed standard domain Ω of class L. We consider the space
& of R-simple (or modified simple, R-sectorial, modified sectorial) cochains in
this domain with the following properties:
all the cochains corresponding to the same partition Ξ are ε-extensible
((exp, e)-extensible) with the same ε, and are bounded in magnitude from
above by a exp νξ with the same ν but the coefficient a depends on the cochain;
the coboundaries of the cochains are bounded from above by the same
clothing cochain m for the partition Ξ multiplied by a cochain-dependent
constant: j5F| < bpm.
For an (R-simple or modified simple partition, we consider the union of
ε-neighbourhoods of the partition rays and for an R-sectorial or modified
sectorial partition the union of sectors with angle 2ε whose bisectors are the
partition rays; we then take the intersection of the constructed half-strips and
sectors with Ω and denote it by 3Ξε.
Let us introduce a norm in !F:

|| F || = sup | F/exp νξ | + sup 16F/m \.

Lemma 3. The space & with the norm defined above is complete.

<\ This follows directly from a theorem of Weierstrass on the completeness of
the space of holomorphic functions with norm C. >

Corollary 1.
 exp F8& <Z 1 + f%?e
e, η = 0; 1.

< Let Fe &<*?£, η = 0, 1. We have expF — 1 =2F k /AI . The partial

sums of the latter series from a fundamental sequence in &. \>

Finiteness theorems for limit cycles 163

Corollary 2.
 In (1 + f Ο c f iQ, η = 0,1.

<] The proof is similar. >

2.3. The first lemma on shifts: a function-theoretic version (LSl reg).
a) $<&> ο Af f C f «° *
b) S^Sg ο exp ο μ ο (.#<> + <?) = £"$ £ ° exp ο μ
for any μ > 0 and C e R.
< These are two different versions of the same statement; this can be shown
if we formulate b) differently:

b') Let F be a sectorial cochain, id + h e 3t°, and in particular let h be a
holomorphic exponentially decreasing function in a domain of class L, C e R

(*) ρ = Ad (μ"1 ο ln)(id + C + h).

Then Fo p is again a sectorial cochain.

Assertion a) can be expressed as follows:

a') Let F be a simple cochain, ρ e Aff. Then F° ρ is again a simple
cochain.

The definition of cochain F ° ρ (Definition 14 of §1.4) motivates the
following proposition.

Proposition 1. Let Ω be a standard domain of class L, ρ e Aff or let ρ be
given by (*). Then there is a standard domain Ω of class L such that ρΩ C Ω.

<\ By Definition 1 of §1.4 the boundary of a standard domain of class L for
some C > 0 has the form

I - C | η | (In | η |Γ 2(1 + ο (1)) as | η | + oo.

It follows that the gap between two standard domains corresponding to
different values C\ and C2 of C is equal to

I C, - C, I Ι η I (In I η |)~2 (1 + 0 (1)).

This implies that Proposition 1 holds for ρ e Aff.
For ρ defined by (*) we have ρ = κζ + ο(ζί~ε) for some κ > 0, ε > 0 (see
Proposition 4 below). This completes the proof of Proposition 1. >
If the map ρ in a') and b') is linear and the cochains are R-simple or
R-sectorial, respectively, then the assertions become trivial, since simple
partitions remain simple under dilatations and sectorial partitions are
unchanged. Under real translations, simple partitions remain the same but
modified simple partitions are no longer of this type. This is due to the fact
that the main domain of a modified simple partition has the form μ

164 Yu.S. IVyashenko

where n ma j n is the main domain of a modified standard partition (see Fig. 4
and Definition 2b of §1.4) but this domain no longer has the same form after
a shift. However, it will be shown that special neighbourhoods of such domains
are included within one another as shown below. As a result, functions that
are holomorphic in a neighbourhood of the shifted domain can be studied in a
neighbourhood of the original domain. To formalize these ideas, we will need
the following definition.

Definition 1. Let Ξ be an arbitrary partition of a domain Ω belonging to one
of the following types: R-simple, R-sectorial, modified simple, and modified
sectorial; let σ be a biholomorphic map of Ω onto its image, σ = ρ" 1. Let
there be a δ > 0 such that in Ω: ρΩ C Ω any generalized δ-neighbourhood
0 (δ ) of a domain 2> of the partition Ξ is included in the image σ^ (2δ ) of the
generalized 25-neighbourhood of the same domain. The partition Ξ is then
said to be subordinate to the partition σ»Ξ of Ω.

Remark. Assume that the conditions of Definiton 1 are satisfied and that F is
an ε-extensible cochain corresponding to the partition Ξ. Then Fo ρ is a
δ-extensible cochain in Ω corresponding to the same partition for some δ > 0.
In order to verify the ε-extensibility of the cochain Fo ρ in a') and b'), we
shall prove the following propositions.

Proposition 2. A modified simple partition in some domain of class L is
subordinate to a partition obtained from the original partition after a shift by a
real constant.

<] The hypotheses of Definition 1 are clearly satisfied for the rectilinear
strips 2\ this follows from the fact that the shift is real. We thus need to
consider only the main domain of the partition (see Fig. 4) and show that for
any positive C and δ there are numbers a and a such that

(*•) φϊί C

where
 Π = {| > a, | η ! < κ/2}, Π = {ξ > α, | η | < π/2},

φ: ζ -* ζ + (1 - δ)ζ~\ ψ: ζ Μ- ζ + C + (1 - 2δ)ζ" 2.

The choice of a "large" value of a* is equivalent to choosing a domain Ω of
class L that is "right enough". Let us prove the inclusion (**). We set

(1 — δ) ζ' 2 = h, (id + h)-1 = id — X.

Then
 Ti = h ο (id - Τι) = (1 - δ)ζ-2 + Ο (ζ' 5) as ζ -*-οο.

The inclusion (•*) is equivalent to Π C Φ" 1 °ψΠ. Furthermore,

φ-ι ο ψ = ζ + C - δζ~2 + C^~3 + Ο (ζ"4).

Finiteness theorems for limit cycles 165

The exact value of C\ is not important; it is only essential that it is real.
This map is biholomorphic in the half-strip Π for large enough a and

| Im (φ"1 ο ψ) Π | | )η | =π/ 2 > π/2,

since —Im ζ~ 2 and Im ζ have the same sign and Im ζ~2||ηι=π/2 is of order
ξ~3, and Im ^ζ~ 3 || η |= π /2 is of order ξ~4; here we have used the fact that
C] is real. This proves the inclusion (**) and therefore also Proposition 2. >

Supplement to Proposition 2. Proposition 2 remains valid if the map ψ is
replaced by ψ = ψ + h with an exponentially decreasing correction h.

<\ The proof is repeated verbatim. t>

Proposition 3. Let ρ be the diffeomorphicm defined by (*), σ = ρ" 1, and Ξ an
arbitrary sectorial partition. Then in some standard domain of class L the
partition Ξ is subordinate to σ»Ξ.

The proof is based on the following result:

Proposition 4. There is an ε > 0 such that in (*) we have

ρ = κζ + ο (ζ1^), κ = exp μθ,

as ζ -*• οο in some domain of class L.

< By the definiton of p, there is a domain Ω of class L and a number ν > 0
such that in (*) we have
 \h\ = o (exp (-v|)) .

Then

ρ = A'1 (id + \iC + μΛ ο μ"
1) = κζ exp ο μΛ, ο μ"
1 ο 1η =

= κζ (1 + (μ + ο (i))h ο μ"* ο 1η).

But
 μομ-ΐο1η | = ο(βχ Ρ ο(-μ-ΐν1η|ζ|))=ο(|ζ|-*) , ε = -Κ- .

Hence ρ = κ ζ + ο (ζ1"6). >

Next we prove Proposition 3. For all the domains of a sectorial partition
with the exception of the main domain, the gap between the generalized δ- and
25-neighbourhoods increases linearly at infinity. This together with
Proposition 4 implies the inclusion required in Definition 1 for such
neighbourhoods. We claim that a similar inclusion holds also for the main
domain, which has the form exp ° ν(φΠ \J Πι) for some ν € (0, 1); here φ
and Π are the same as in the proof of Proposition 2 and Πι is the half-strip
η e [0, π], ξ ^ a. It is enough to show that there is a half-strip Π (see (**))

166 Yu.S. Il'yashenko

such that
 exp ο ν ο φΠ d ρ ° exp ο ν ο ·ψΠ,

where ρ is given by (•) and Π by (*•), and ψ: ζ Η ζ + (1-2δ)ζ~ 2. This
inclusion is equivalent to
 φΠ CZ {Ad (exp ο ν)ρ)
However,
 Ad (exp ° v)p = id + C -\- h,

where C = X^C, λ = μ-^ν, Ίι = λ~% ο λ;

(Ad (exp ο ν)ρ)ψ = ψ,

where ψ was defined in the supplement to Proposition 2. This supplement
now implies Proposition 3. >

Let us now prove the lemma LSl reg. The hypotheses 1 and 2 of
Definitions 7, 8 and 12 of §1.4 for the cochain F» ρ follow from Proposition 2
in the case of a') and from Proposition 3 for b'); we also use the remark
after Definition 1.
Let us verify the hypothesis 3. We need to prove the exponential estimate
for F ο p. By definition of simple and sectorial cochains, in some domain of
class L we have \F\ < exp νξ; for a rapidly decreasing F we have ν < 0.
If ρ = α(ζ + β) € Aff, then

| F ° ρ | < exp αν (ξ + β) < C exp ν'ξ, ν' = αν,

which confirms condition 3 of a'). If ρ is defined by (*), Proposition 4 and
property 4 of standard domains of class L imply that

| F ο ρ I < exp ν Re ρ = exp νξ (1 + ο (1)),

which also confirms condition 3 for b').
Next we verify condition 4 by estimating the coboundary. Assume that the
coboundary 5F is bounded by a clothing cochain m of the partition Ξ
corresponding to F. Then

|6(Fop) | = | (8F) ο p| < me ο p.

In a') we have ρ = α(ζ + β); me ο α is a clothing cochain for the partition
σ»Ξ, where σ = α" 1 ; we denote it by me- The composition /η<;ο(κ1+β) is
bounded above by a clothing cochain for the same partition σ,Ξ corresponding
to a different constant C" e (0, C). This follows from the inequality

exp (- C exp μ (ξ + β)) < C
x exp (—C exp μξ)

which holds for some C" e (0, Q and Cj > 0. We have thus verified all the
conditions of Definitions 7 and 8 of §1.4 and proved the assertion a').

Finiteness theorems for limit cycles 167

By Proposition 4 we have ρ = ζ(1 + ο(1)) in b'). Hence m c ° ρ is majorized
by a clothing cochain corresponding to the same partition as me- This follows
from the inequality

exp (-C | ζ (1 + ο (1)) \» < Cx exp (-C \ ζ |n)

which holds for some C e (0, Q and d > 0. We have verified all the
conditons of Definition 12 of §1.4 and proved b'), which completes the proof
of LSlreg. >

2.4. Function-theoretic version of the second lemma on shifts (LS2reg).
This lemma consists of four assertions LS2 re g a)—d), which are obtained from
the corresponding parts of LS2 in §1.8 if f%x and lfc6+ are replaced by
Jg and ?

LS2reg. a) Let F} ΕΞ f
r
6%
e, j = 1, 2, η = 0, 1; then

(id + Ft) ο (id + Ft) 6Ξ id + «e + g ;

b) (id + fO" 1 = id + F%%g, η = 0, 1;

c) te/ Fj e ^^°, F2 e f ^ieg, ίΛβη/or α«>; μ > 0

Ft ο (id + F 2 ο exp ο μ) — Fx <= f ^Sg ° exp ο μ;

d) fei Fj e f^ilg , ^2 e ^ieg , μ > v, iAen

F x ο exp ο μ ο (id + F 2 ο exp ο ν)] — Ft ο exp ° μ ΕΞ f'Sragoexpo ν.

< The assertion b) is proved along the same lines as a) but more simply, and
therefore we shall not state the proof of b) explicitly. The assertions a), c) and
d) are equivalent to the following statements:

a') Let F±, F2 e= f&+ or Flf F2 GE^ieg, Ρ = id and

(***) F^F^ip + FJ- Flt

then F ΕΞ f ^ or F <= P$£g, respectively;

c') let Fx S Ρβ°, F2 ΕΞ fSrtg, ρ = v"1 ° In, and /ei F be the cochain
defined by (*), then F ΕΞ &$&;

d') tei F l t ^ 2 <= f^eg, μ < ν, ρ = ζ\ λ = μν-1 < 1, and let F be

defined by (*), then F CZ f %%•

Reduction a') ==» a). We have

(id + FJ ο (id + F2) = id + Fx + F, + F,

where i 7 has the form (***) and ρ = id. The cochains Fi + F2 + F and F are
either both simple or both sectorial, since F\ and F 2 are of the same type.
We shall prove a'), b') and c') simultaneously. Let F be defined by (***).
We consider four cases.

168

Case

Case

Case
 1.

2.

3.
 Fx
F1

F! F,
 Ρ
' ae
 y«.S. Il'yashenko

= id.

Ξ f^r , ρ = id.

f ^reg, ρ = μ"1' In, μ > 0.

Case 4. Flt F2 <= ^«Sg , Ρ = ζ \ λ <= (0, 1).

We can prove a'), b') and c') by showing that F e= f&!J. in Case 1 and
F <= fiC g in Cases 2-4 . We note that a) is obtained if F2 in Case 2 is
assumed to be a rapidly decreasing rather than weakly decreasing sectorial
cochain.
In all four cases, we construct a domain of class L where F is defined, and
then confirm all the hypotheses of Definitions 7 — 9 and 12, 13 of §1.4. Let Ω
be the domain of definition of F\ (of class L) where the estimate \F\\ < exp νξ
holds for some ν e IR (condition 3 in the definition of simple and sectorial
cochains). We choose a domain Ω δ of class L for each δ > 0 such that
1° The cochain F2 is defined in Ω§ and satisfies the following inequalities
in this domain:
 I Ft | < 6, I F2 | < 6 Ι ζ Γ 8.

2° The domain Ω§ in Cases 1 and 2 or the domain ρΩδ in Cases 3 and 4
are contained in Ω together with their 26-neighbourhood. Both requirements
can be satisfied by virtue of property 5 of domains of class L (see the beginning
of §1.4 and the definitions of rapidly and weakly decreasing cochains). We
shall prove that the germ F defined by (*••) can be extended to Ωδ, provided
δ is small enough, as a simple cochain and in Cases 2 —4 as a sectorial cochain.
We consider all the cases at the same time.
Let Fj, j = 1, 2, be cochains of types σ,, σ = ρ" 1 . We shall prove that
the cochain F defined by (***) is of type α = σοΟ ] Uf2 · In Case 1, all
the functions of the set σ are dilatations: ζ »->· λζ, and in the remaining cases,
they are exponentials: ζ t-+ exp λζ. We shall order the maps in σ by
decreasing λ,·:

σ = (λχ, . . ., λκ), λχ > . . . > λ Α - > 0 in Case 1;
σ = (exp ο λχ, . . ., exp ο λ κ ) , 1 > λχ > . . . > λκ > 0 in Cases 2—4.

For each k such that 1 < k < Κ we construct a ^-realization F(k) of F; its
R-realization can be constructed similarly, and the corresponding procedure
will not be described. Let Ξ(^) be the fc-realization of the partition of type σ.
It is obtained as the product of partitions σ,Ξι and Ξ2, where Ξι and Ξ2 are
suitable realizations of the partitions Ξ^' and Ξ^
2 corresponding to F\ and F2-
In Case 1, the partitions Ξι and Ξ2 are constructed in the same way as in the
proof of Lemma 1 in §2.1. The construction in the remaining cases is similar.
Namely, let σ^,Ξ^
1 and Ξ^2 be partitions of type

σ ο σχ = (exp ο μχ, . . ., exp ο μ^), 1 > μ1 > . . . > μ^ > 0,
σ2 = (exp ο ν χ, . . ., exp ο νΜ), 1 > ν χ > . . . > νΜ > 0.

Finiteness theorems for limit cycles 169

Then

σ = σ ο O] l U σ2 = (exp ° λΐ5 . . ., exp ° λ κ ) , 1 > λχ > . . . > λκ > 0.

Let /ci and fc2 be such that μ^1 ^ λ*; > μ^,+ ι, v^2 ^ λ* > v^+i, and let
Ξι = Ξ ^ and Ξ 2 = S(fe be kr and /^-realizations of Ξ^
1 and Ξ^
2. Then
E(k) = σ.Ξ^Ξ 2. ^
Now let F\ = F(ki) and F2 = F^ be realizations of F] and F 2 corresponding
to the partitions Ξι and Ξ2. We shall show that F^) = F\ °(p + F2)—Fi
corresponds to Ξ ^ and is an ε-extensible cochain. Let U be any domain of
the partition Ξ ^ of Qg. This means that there are domains V and W belonging
to Ξ, and Ξ 2 such that U = W Π a.V, o.V = c(V Π ρΩδ).
Let /ι and f2 be functions from the sets F\ and F2 corresponding to V
and W. They can be extended holomorphically to generalized ε-neighbourhoods
Κ(ε) and W*-*) of V and W for some ε > 0. The gap between the domains
σ.Κ (ε ) and a.F (e/2 ) is greater than δ|ζ|~ 3 provided that δ is a small enough
number depending on ε. The compostion / = /ι ° (p +/2) is then defined in the
(σ, e/2)-neighbourhood of U and is a function of the set Fw. This proves
the ε/2-extensibility of the cochain F^ corresponding to Ξ ^ and confirms
conditions 1 and 2 of the definitions of simple and sectorial cochains.
We next verify condition 3 of these definitions, which means that we need
to estimate from above the modulus of F; we shall now show that there are
numbers C > 0 and κ > 0 such that

| F | < C exp (_κξ)

is satisfied in Ω$. By the hypothesis of the lemma, there are numbers ν e 1R
and λ > 0, C > 0 such that

\F1\<C exp νξ in Ω,
\F,\<C exp (-λξ) in Ω6.

Using the Cauchy inequality in the δ-neighbourhood of the domain Ωδ,
which is not closer to the boundary of Ω than δ by construction of Ωδ, we
find that there is a C" > 0 such that

\F[\< C" exp (νξ) in Q e.

In the domain Ω we have by Lagrange's theorem

(·*·) |F|<(ma x \F[o (p + eF2)\)\F2\.

θε[ο, ι]

The set (ρ + θ·Γ2)Ωδ is contained in the δ-neighbourhood of Ωδ. Hence

I F[ Ο (ρ + QF2)\ < C" exp (v (Re ρ + δ)).

We now have to consider the individual cases separately.

170 Yu.S. IVyashenko

Cases 1 and 2: ρ = id and the cochain Fj is assumed to be rapidly decreasing.
Then
 | F | < C" exp ( - | ν | (ξ + δ)){ Ft | < C exp (-κ|) '

for some C > 0 and κ > 0, since F2 is either rapidly or weakly decreasing.

Cases 3 and 4: ρ = μ" 1 ο In or ρ = ζ λ, λ < 1. In these cases, given any α
and any standard domain of class 1, we can choose a C such that

Re ρ < αξ

holds in this domain. We choose α so small that να — μ = —κ < 0. The
required estimate for \F\ then follows from (***).
We shall now verify condition 4 of the definitions of simple and sectorial
cochains by estimating the coboundary. Let i? be an arbitrary boundary ray
of the partition Ξ^ . There are two possibilities: if represents a boundary
ray either for both partitions σ.Ξ] and Ξ2 or for only one of them. The
second case is similar to the first, but simpler, since the functions of one of
the pairs/i,/2 or g\, g2 considered below coincide. Let us consider the first
case. Let fx and f2 be functions from F\ corresponding to the domains of Ξι
adjacent to .£? on the left and on the right; let g\ and g2 be similar functions
from F2 for the ray if; λ] =/ ι ° (p + gi), h2 =f2° (p + ik)- Then the inequality

- h21 < I (jx - ft) ο (ρ + gl) I + max I /2' ο (ρ + g l + θ (g2 - gl)) | . \gl - g2 \
ee[o 1]

holds in the (σ, £/2)-neighbourhood of <£ in the domain Ωδ provided that δ is
small enough. The difference h\—h2 belongs to 6F. Let m1 and m2 be
clothing cochains for Ξι and Ξ2. The above inequality then implies that

I 5F | < m1 ο (ρ + Ft) + C (exp (v Re ρ + 6))m2 < πι1 ο (ρ + F2) +

+ C (exp (v| + b))m\

The composition m1 ° ρ is a clothing cochain for the partition σ.Ξι; this was
discussed in detail for ρ = μ""
1 ο In in the proof of Proposition 1 of §1.4 and
the proof for ρ = ζ λ, λ < 1, is similar. The definition of clothing cochains
has been adapted to be used in such arguments. Furthermore, the composition
m1 ο (ρ + F2) is majorized by a clothing cochain corresponding to the same
partition as m1 ο ρ but to a different constant. This is obtained from the
following inequalities in the cases considered:

Case 1. exp (—C exp (μξ — δ)) -< exp (—C" exp μΐ).

Case 2. exp (-C (| ζ | - δ)>») -< exp (- C | ζ |n).

Case 3. exp (-C exp ο μν"1 » (In | ζ | - δ)) Κ exp (- C | ζ | λ), λ = μν"1.

Case 4. exp (-C (| ζ | - δ)»-) ^ exp {-C | ζ |λ).

Finiteness theorems for limit cycles 171

All these inequalities hold for some C e (0, C) which depends on δ.
The second term in the estimate for \5F\ is bounded from above by a
clothing cochain corresponding to the same partition as m 2 but to a different
constant. This follows for simple and sectorial cochains, respectively, from the
inequalities
 exp (—(exp μξ + ν ξ) -< exp (— C exp μξ),
exp (-C | ζ| μ + νξ) -< exp (-C | ζ |»).

This completes the estimate of the coboundary of F and thus also the proof of
LS2reg. >

2.5. Function-theoretic version of the third lemma on shifts (LS3reg).

Let F\ and F2 be rapidly decreasing sectorial cochains, μ ^ ν > 0. The equality

F ο ex p ο μ = F 1 <> ex p ο μ (id + F 2 ° ex p ο ν )

then defines a germ F of a rapidly decreasing sectorial cochain.
<\ In the case μ = ν, LS3reg follows from LS2reg a). Consider the case μ > v.
We set
 λ = μ-\ < 1.

By hypothesis,
 F = F x ο A'1 (id + μ"1 F 2 ο exp ο λ).

Furthermore,

A'1 (id + μ~
1/?;5 ° exp ° λ) = ζ. exp ° μ~^ 2 ο exp ° λ ο 1 η =

= ζ. exp ο μ" 1 ^ ° ζ χ •
By Corollary 1 of the completeness lemma in §2.2, there is a germ
such that
 exp ο μ-^ 2 = 1 + F 3.

By Lemma 1 of §2.1 the product C,x~ lF 3 = F 4 is again a rapidly decreasing
sectorial cochain. Hence

ζ exp c  μί\ , ο ζ^ = ζ eg·

By Proposition 2 of §1.4 the composition F s =  ί" 4οζ λ is again a sectorial
cochain. It decreases faster than any power in a standard domain of class L,
since so does exp( —ε Re η λ ) for any λ e (0, 1), ε > 0. Hence F 5 is a weakly
decreasing sectorial cochain. We have

= Γ ι ο ^ια -\- Γ  5), f j 6Ξ ir©regi ^ B S j-Btor·

By LS2 reg a'), we conclude that F is a rapidly decreasing sectorial cochain,
which completes the proof. [>

172 Yu.S. IVyashenko

2.6. Function-theoretic version of the fourth lemma on shifts (LS4 reg).

a) 7»c:id + r« R+ ;

b) f %U g ο exp ο μ ο /« = £<$£ε ο exp ο μ for any μ > 0.

< a) We recall that J° = Ad(Aff)^° (see §1.2),

Λο = Gr(gF, ge^jG^lagiE^.fl G Aff: (A gl)(agF u)

The set id+if<i(R+ represents a group under composition by LS2 a).
Moreover, Ad(Aff)(id + f^ + ) = id+f«R + by LSl re g a).
Hence it is sufficient to prove a) for the generating elements of J° belonging
to 0t° or Λτ$. But we have shown in Examples 1 and 2 of §1.4 that the
assertion a) holds for these elements. This proves the assertion a).
b) This assertion is equivalent to the following statement. Let F t e
id + F 2 e / , μ > 0. Then

F ^ F x ο Ad (μ"1 ο In) (id + F 2) <=

Remark. According to a), we have F 2 e f ^R". We shall prove a stronger

version of (*) .

Proposition 5. The formula () holds for any F 2 e $<@$.

< By LSl re g a ) . there is a germ F 3 e f ^ such that

Ad (μ"1) (id + F 2) = id + F 3.

The germ F 3 can be expanded in a Dulac series. Let us choose a partial
sum Σ of this series that approximates the germ so well that

id + ^ 3 = 2 ο (id + F t), F 4 e f«l , F t = ο (exp (-6|)) .

Then
 Ad (μ-Μη) (id + F t) = 4" 1 (id + F,) = Α^ΣοΑ'1 (id + F A).

But Σ ε ^° . Hence it follows from LSl re g b) that

Moreover,

A'
1 (id + F 4) = ζ expo^oln = ζ (1 + F 5°ln), F 6

The last equality follows from the completeness lemma. Here F$ ο hi is a
decreasing holomorphic function or a sectorial cochain (the first statement is a
special case of the second) by Proposition 1 of §1.4. In both cases,

ζί>1 η = ζο( θχρο(_6 In | ζ \ )) = ο (ζ"6)·

Finiteness theorems for limit cycles 173

Hence F 6 =  ^F$ ο In is a  weakly decreasing sectorial cochain. It now follows
from LS2reg a') that
 F = />((id + F
t) <= FtiSt,

which completes the proof. [>

§3. The Phragmon-Lindelof theorem for simple and sectorial cochains

This section contains the proof of the following theorem.

Theorem. Let F  be a  simple or a  sectorial cochain defined in a  standard domain
of class L  and decreasing faster than any exponential on (R
 +  , oo). Then F  = 0
on (fR
+
, oo).

The implication |f | <  εχρ(-νξ)Υ ν >  0  on (R +, oo) -* F  = 0  on
(R +, oo) is  called the Phragmen—Lindelof property of a  cochain F.
A similar result for a  sectorial cochain defined in a  sector with angle
smaller than π is  included in Proposition 3  of §3.4.
We begin with the classical Phragmen — Lindelof theorems. The last of
these theorems is  known to experts, but I  am not aware of any textbooks
including this theorem. For this reason, a  proof of this theorem will be given
here, particularly since it  represents a  model for the subsequent discussion.
This theorem was used in [5].

Heuristic ideas.
The proof of the Phragmen — Lindelof theorem employs different realizations of
the same cochain. A preliminary estimate (Propositions 1—3) is  proved for the
R-realization. Roughly speaking, this estimate claims that if the IR-realization
of a  cochain defined in a  standard domain of class L  decreases on (R +, oo)
faster than any exponential, then it  decreases on (R + , oo) nearly as fast as the
coboundary of the cochain. Next we narrow down the domain of definition
so that it  no longer contains the partition lines along which the coboundary
decreases slowest of all. For a  sectorial cochain F  of type

(*) σ  =  (expojij, . . . , θχρ°μ Ν  ), 1  >  μ χ >  . . . >  μ Ν  >  0

this construction has the following form. The number TV in the set σ, which
defines the partiton corresponding to the cochain, will be called the numerical
type of the cochain. We consider a  1-realization of the cochain denoted by
F
(i) in a  sector S  belonging to the domain (exp °  Hi)n main. The cochain F(\)
has a  different type σ(ΐ) in this sector:

σ ω =  (βχρ·μ 2, . . ., βχρ°μίν);

its coboundary decreases faster than the coboundary of the IR-realization of F.
The numerical type of the cochain F(i) on S  is  equal to N—l. The preliminary
estimate (Proposition 3) applied to the restriction of F^  to the aforementioned
sector claims that F w  decreases on (R +, oo) nearly as fast as the coboundary
δ^(!) on S. Proceeding by induction on the numerical type of the cochain,

174 Yu.S. IVyashenko

we find that the JV-realization F (N) of F decreases on (R + , oo) as fast as

exp( —(7|ζ| μ2Ϋ). But the main domain of the partition corresponding to F(Ao
contains a sector with greater angle than π μ Ν; the sector itself includes
(R +, co). The corresponding function of the set F^ is identically zero by
virtue of the classical Phragmen — Lindelof theorem.
We shall now begin a more detailed discussion.

3.1. Classical Phragmen-Lindelof theorems and their modifications.
A. The Phragmin-Lindelof theorem for an unbounded domain [11]. Let 2 be
a simply-connected domain on the Riemann sphere containing the point oo on its
boundary. Let f be a holomorphic function in 3) that is continuous in the
closure of 2 taken with respect to the ^-topology {not including the point oo)
and bounded. Then
 sup |/ | =  sup|/j.

This is a version of the maximum-modulus principle for holomorphic
functions.

B. The Phragmin-Lindelof theorem for two quadrants. Let f : C + -> C be a
holomorphic function bounded on the union of the imaginary axis and the positve
semiaxis which increases no faster than an exponential function of the modulus,
that is, there is a v > 0 such that |/(ζ)| < exp ν|ζ|. The function f is then
bounded and
 sup|/| = supj/|.

< We first prove that the function / satisfies the maximum-modulus principle
in each of the sectors Si and 5 2 , where S\ is the first and 52 the fourth
quadrant. We consider S\ and a family of barrier functions g e that are
holomorphic in 5 i and whose modulus in S\ is greater than ΟΊζ|1 + δ for some
C > 0 and δ > 0. For example, we take

ft (ζ) = exp ε (βζ)1+δ, β =  eW*.

For any positive ε the value of fjg& is bounded in S\, and it follows from
Theorem A that
 Pl//£e| p
s, es,

Taking the limit as ε ->· 0, we find that/i s bounded in S\. Similarly, /i s
bounded in 52 and hence also in C + . Using Theorem A again, we obtain
Theorem B. >

C. Corollary 1. If a holomorphic function / : C + ->C « bounded and
decreases on R + faster than any exponential exp(—νζ), ν > 0, then f = 0.

Finiteness theorems for limit cycles 175

<\ The function / exp λζ satisfies the hypotheses of Theorem Β for an
arbitrary λ > 0. Making use of the fact that |exp λζ| = 1 on 9C +, we
obtain
 ™ρ|/(ζ)|[βχρλζ|< 8 αρ|/| .

Assume that there is a point ζ such that Re ζ φ 0, /(ζ) Φ 0. Then
/(ζ) exp λζ -> οο as λ -+ οο, which is a contradiction. \>

Remark. The Phragmen — Lindelof theorem for cochains is proved along the
same lines as Corollary 1. The proofs of this corollary and of Theorem Β
were reported to us by E.A. Gorin.

Corollary 2. Theorem Β remains valid if the real semiaxis in its formulation is
replaced by a curve Γ connecting some point on 6C + with the point <x> on the
Riemann sphere and whose germ at infinity is contained within the sector Sa,
that is, [arg ζ| < α < π/2. The same applies to Corollary 1.

<] The proofs of Theorem Β and Corollary 1 are repeated almost verbatim. t>

Corollary 3. Corollary 2 remains valid if C + and 9C + are replaced by a
standard domain Ω of class L and its boundary 8Ω.

<] It follows from Property 3 of standard domains of class L (see §1.4) that
there is a conformal map ψ : C + -»· Ω of the form ψ(ζ) = ζ(1 +ο(1)). This
implies that the germ at infinity of the curve Γ = ψΚ + belongs to an
arbitrary sector Sa for α > 0. Hence fa ψ satisfies all the hypotheses of
Corollary 2. Corollary 2 then implies the validity of Corollary 3. >

Corollary 4. Let Ω be a subdomain of C containing a ray [R^, ξ > a, for some
a > 0, and let there be a conformal map ψ: Ω -*• C+, lim ψ (ζ) — °° which

takes the ray Ra into a curve Γ whose germ at infinity belongs to some sector
Sa, α € (0, π/2). Assume that a holomorphic function f: Ω -+ C increases no
faster than exp v|\|/| for some ν > 0, and let f be bounded on 9Ω and on R^\
Then f is bounded in Ω and
 |

Furthermore, if f decreases on IR^" faster than exp(—λ Re ψ) for any λ > 0,
then f = 0.

< Corollary 4 is proved by applying Corollary 2 to the function/ο ψ" 1 . >

3.2. Trivialization of a cocycle.
The first step on the way to proving the Phragmen — Lindelof theorem for
simple and sectorial functional cochains is to find for a given functional
cochain a "small" cochain with the same coboundary so that the difference
between the original cochain and this new cochain is a holomorphc function.

176 Yu.S. IVyashenko

Lemma 1. Let F be an ε-extensible \R-simple or U-sectorial functional cochain
defined in the ε-neighbourhood Ω ε of a domain Ω whose boundary contains the
point oo and which is included in some standard domain of class L; let aF'€

(EF) be the corresponding partition of Ω ε (of Ω). Assume that the modulus of the
coboundary is majorized by a clothing cochain m, and

m
o = supm, ^ mds = I <oo .

Then there is an ε-extensible functional cochain Φ in Ω such that

6F = 6Φ on dEF, max ) Φ |<Ce" 1 (m0 + 7),

where C is a constant depending on the type of the cochain F but not on F
itself.

< There is a natural orientation of the partition rays for EF'ε; this induces an
orientation of the coboundary clEF'E. In the formula for Φ below for
calculating the functions from the set 5F on a boundary line of EFrE we first
consider the domain to the left and then the one to the right of the line.
We set

It follows from Plemelj's theorem [10] that 5F = δΦ. Let us estimate |Φ(ζ)|
for ζ e Ω. Let F be an IR-simple cochain of type (μι, ..., μΝ), μι > ... > μ^ > 0,
or an R-sectorial cochain. In the first case, the generalized ε-neighbourhoods
of domains of EFl£ contain ordinary ε/μι-neighbourhoods and in the second
case ordinary ε-neighbourhoods.

1°. Let dist^, 8Ξ^ ε) > ε/C, where C = μι for a simple cochain and C = 1
for a sectorial cochain. Then |Φ(ζ)| < Cε~1/.

2°. Let dist^, QEF'e) < ε/C. Assume that ζ belongs to a domain D of EF.

Then the disc Κ with centre ζ and radius ε/C lies entirely in the
(σ, e)-neighbourhood of 2. In the formula for Φ we replace the integrals
over the "chords" (connected components of the intersection δΞρ·ε Π Κ) by
integrals over arcs of the circle dK with the same terminal points, which are
separated from ζ in Κ by the corresponding curvilinear chords. The integrals
over the arcs of dK are bounded above in modulus by the constant 27iC/no^,
and the integral over the rest of the contour by the constant CI/ε. Ths proves
the lemma. >

The cochain Φ in Lemma 1 is called the trivialization of the cocycle 8F.

Finiteness theorems for limit cycles 177

3.3. The maximum-modulus principle for functional cochains.
Lemma 2. Assume that under the hypotheses of Lemma 1 Ω is a standard
domain of class 1 and the functional cochain F increases no faster than exp νξ
in Ω and is bounded on 9Ω and on 1R
+. Then F is bounded in Ω and

sup | F | < sup | F | + 2&ΓΧ {m0 + /),

C, ε, m 0 and / have the same meaning as in Lemma 1.

< Let Φ be the trivialization of 5F defined in Lemma 1. Then F—Φ is a
holomorphic function in the standard domain Ω satisfying the hypotheses of
Corollary 2 of §3.1. By virtue of the corollary we obtain

sup I F — ΦI == sup | F — Φ ]
Ω 5Ω

Moreover,
 sup | F | < sup | F — Φ I + sup | Φ | < sup | F\ + 2 sup | Φ |.
Ω Ω Ω 3Ω Ω

The estimate of Lemma 1 for |Φ| implies the estimate in Lemma 2. >

We shall need an analogue of Lemma 2 for a sector.

Lemma 3. Under the hypotheses of Lemma 1 assume that Ω is a subdomain of
C satisfying the hypotheses of Corollary 4, for example an open sector containing
(IR
 + , oo). Let ψ : Ω -• C + be a conformal map. Assume that the ^.-sectorial
cochain F is defined in Ω and increases no faster than exp ν Re ψ for some
ν > 0 and is bounded on 3Ω and on (R + , oo). Then F is bounded on Ω and
satisfies the estimate of Lemma 2.

<J The proof of Lemma 2 can be repeated verbatim, except that Corollary 2 is
replaced by Corollary 4. >

3.4. Preliminary estimate for simple and sectorial functional cochains.
Proposition 1. Let F be a simple functional cochain ofU-type (μι, ..., μ^),
μι > μ2 > ... > μ,Λτ > 0. If F decreases on R+ faster than any exponential,
then given any sector Sa : |arg ζ| < α < π/2 and any δ > 0, there is a C > 0
such that the following inequality is satisfied for all ζ ε Sa:

| F (ζ) | < exp (-C exp μΓ
1 (1 - 6) ξ).

< We can assume without loss of generality that F is bounded. In fact,
according to Definitions 7 and 8 of §1.4 there is a v > 0 such that
|^(ζ)| < exp νξ. Then F exp(—νζ) is a bounded cochain satisfying the
hypotheses. Assume that \F\ < 1. Let F be defined in a standard domain Ω
of class L and let ψ : Ω -»· C + be a conformal map whose correction
increases more slowly than |ζ|; the existence of such a map follows from the
definition of a standard domain of class L (Property 3 in §1.4). For each
a > 0, we consider the domain Ωα = ψ"" 1 ^ , GJ" = {ξ > a). We apply the

178 Yu.S. Iiyashenko

maximum-modulus principle to the cochain i\, α = F exp λ (ψ (ζ) — a) in ΩΩ.
We need a preliminary upper bound for the maximum and the integral of the
corresponding clothing cochain. In the intersection of the (σ, e)-neighbourhood
of the boundary line of Ξ^ with the ε-neighbourhood of Ωβ we have

(*) Ι δί\, α (ζ) | < m (ζ) exp λ Re (ψ (ζ) - a),

m (ζ) < m (ζ) = Cx exp (—C2 exp μξ), μ = μι 1.

We shall show that Re ψ < ξ in Ω. In fact the inequality Re(\|i—id) < 0 is
satisfied everywhere on 3Ω. Moreover, |ψ — id| = ο(|ζ|). This implies that
Re(\|/ — id) < 0 by virtue of the well-known Phragmen — Lindelof theorem for
harmonic functions. Hence

(**) Ι δίλ. a (ζ) I < η (ζ) exp λ (ς - a).

Let Ω^ be the ε-neighbourhood of Ωα. We require an estimate for the
maximum modulus of the right-hand side of (**) and for the integral

(**•) 7(a) = ^ m exp λ (ξ — a)ds.

We can assume without loss of generality that Ω is contained in a quadratic
standard domain. Then the vertical line Re ζ = ξ in Ω intersects no more
than CZ,2 boundary lines of Ξ^, because this partition is the product of finitely
many dilated standard partitions. Since Re ψ < ς, we have Ω^ C C^_E and
hence
 7(a)< C ^ l"mexpl&  — a)

η—ε
Let us denote the integrand by m + . If m'+/m+ ^ —1 for ξ ^ α —ε, it is
easy to estimate I(a). Then

m+ (1) < m+ (a — ε) exp (a — ε — |) , / (a) < Cm+ (a — ε).

We have m'+/m+= 2ξ - 1 —C2 exp μξ + λ. The inequality m'+/m+ =ζ — 1 is
satisfied for all ξ ^ a — ε, provided that a is large enough, if we choose
λ = C2 exp μ(α—1). For such λ the functional cochain F^a satisfies the
hypotheses of Lemmas 1 and 2 with the following constants:

mB — in (a — ε), I = C (a — zfm (a — ε).

We have used the inequality exp( —λε) < 1; this factor is replaced by unity
in the upper bounds for the modulus and the integral of the clothing cochain.
By Lemma 2 we obtain everywhere in Ωα

(ζ) | < sup I F%, a I + 2CE"
1 (m0 + 7).

Finiteness theorems for limit cycles 179

But the quantities rrto and / for a fixed ε tend to zero as a ->• oo. We can
thus assume that the second term is less than 1. Moreover, we have
sup | Fx a | <* 1 irrespective of λ and a. Hence for ζ e Q a we have

| F (ζ) | < 2 exp (- λ Re (ψ (ζ) - α)), λ = C2 exp μ (α — 1).

Let us estimate F in the sector Sa : [arg ζ| < α < π/2. For each ζ e 5 α
with large enough ξ = Re ζ we take α = Re ψ(ζ) — 1. Then

| F (ζ) | < 2 exp (-C 2 exp μ (α - 1)).

But we have Re ψ = ξ(1 + ο(1)) in Sa. Hence for any δ there is a number ξ 0
depending on Sa such that the equality Re ψ(ζ) = a — 1 for ζ e Sa, ξ > ξο
implies that α —1 > (1 —δ)ξ. Finally we obtain

|/"(ζ ) | < exp (-C exp μ (1 - δ) ξ)

for ζ 6 5 β, Re ζ > ξ0, μ = μ,"
1. >

Corollary I. Functional cochains corresponding to an ^.-simple partition of
numerical type 1 have the Phragmen — Lindelof property.

< Let F be an R-simple cochain of type μι (which means that there are no
H2> ••·> ^N in Proposition 1). The function F" of the set F corresponding to
the main domain of the partition is holomorphic in the half-strip of width 3π/2
and decreases in this half-strip as the composite exponential function
exp(-C exp(l -δ)ξ). We have F" = 0 by virtue of the Phragmen - Lindelof
theorem. [>

Proposition 2. Let F be an R-sectorial cochain, that is, a regular functional
cochain of type (expo μι, ..., exp ο μ^), 1 > μ] > ... > μ^ > 0. If F
decreases on (R + , oo) faster than any exp(—νξ), ν > 0, then for any sector
Sa : [arg ζ[ < α < π/2 there is a number C depending on α such that the
inequality
 I F (ζ) | < exp (-C | ζ |n), μ = μ?,

is satisfied everywhere in Sa.

<\ Let ψ, Ω ο and i% o be chosen as in Proposition 1, and EF the R-sectorial
partition corresponding to F. The formulae (*) and (**) remain valid, except
that
 m = Cx exp (—C2 εχρομϊΜη) = Cx exp (—C2 | ζ \ )».

To estimate the integral I{a) by an integral over the real axis, we note that
there are finitely many partition lines of Ξ^, and therefore their slopes are
uniformly bounded. Moreover, |ζ| increases along each vertical line.

180 Yu.S. Il'yashenko

Hence

I (a)** J ίηβχρλ(ξ-α)ώ<<: ι ξ exp ο (—<72|ζ|ι» + λ (ξ -

We shall denote the integrand in the last integral by m+. If m'+/m+ <C — 1 for
ξ ^ α-ε , then /(α) < m+(a-e). We have m'+/m + = -Ο 2 μξ μ ~ 1 + λ. The
inequality m'+/m+ < — 1 is satisfied for all ξ > α —ε if we choose

λ = -γ C^a»-1 for large enough a. Following the same line of reasoning as

in the proof of Proposition 1, we obtain by Lemma 2

] F (ζ) | < 2 exp (- λ Re (ψ (ζ) - α)), λ = C o a^ ,

for some Q > 0. Let us estimate \F\ in Sa. For each ζ e S a we set

α (ζ) = Re ψ (ζ) \-. Since Re ψ(ζ) = ξ(1 + ο(1)), we find that α(ζ) > ξ/3 if

ξ is large enough. Hence

! F (ζ) | < 2 exp (-C o (α (ζ))^|/3) < exp (_C&*). >

Corollary 2. %1-sectorial cochains of numerical type 1 /zave //ie Phragmen —
Lindelof property.

<\ The proof follows easily from Proposition 2 and Corollary 3 of §3.1. We
carried out a similar argument in detail above. t>

To prove the Phragmen — Lindelof theorem for simple and sectorial cochains
of arbitrary numerical type, we require the following result.

Propositon 3. Let F be a sectorial cochain of type σ = (exp ° μι, ..., exp ο μ^)
1 > μι > ... > μΝ > 0, defined in the ε-neighbourhood of the sector

5(μ) = {ζ I arg ζ e (-πμ (1 - 6)/2, α (μ)), Ι ζ | > Λ},

ίημ(Ι-δ) for 0<μ<1/2 ,
1>μ> μι , «(μ) = { π(1 _ δ)/ 2 f0f 1/2<μ< ι .

Here δ > 0 and it is so small that μι < μ(1 —δ) and the angle γ of the sector
£(μ)
 ί 5 greater than πμ; otherwise δ and R are arbitrary positive numbers. Let

F decrease on (R + , oo) faster than exp (—Ctp), — < β < μι
1, for some C > 0.

Then there is a C > 0 such that

I F (I) | -< exp (-C'fM , I <= (R+, oo).

Remark. F decreases on (R + , oo) faster than a non-zero holomorphic function
in the sector S^y
 Finiteness theorems for limit cycles 181

<\ Let ψ be a conformal map 5(μ) -»C + ; we could easily write an explicit
expression for this map, but we need only the fact that

ψ (ζ) = (β*»ζ)
α + Ο (1), α = π/γ.

Here em is the rotation that takes the sector 5 (μ ) to a sector with the bisector
Κ +. We note that α < β since β > π/γ by hypothesis. Hence, the cochain
Fx<a = F exp(—λ(ψ(ζ)—ψ(α))) for any positive λ and a is bounded on R + .
Let us set 2>a = {Re ψ ^ Re \|/(a)}. We can assume without loss of generality
that F is bounded: |F | ^ 1. We have everywhere on d£>a

I exp λ (ψ (ζ) - ψ (α)) Ι = 1,

and on 5@%
 | exp λ (ψ (ζ) - ψ (α)) | < 1.

The coboundary hF\>a is bounded by

Ι WKa (ζ) | < m (ζ) exp λ (Re ψ (ζ) - Re ψ (α)) = m,.,a (ζ),

τη < m = Cj exp ( —C2 [ ξ |»
1), μ = μ^
1 > β > a.

Let us estimate the integral I (a) = ) mkyU. The function |ζ| μ for μ > 1

has a minimum value on each vertical line at the intersections with the real
axis. Hence |ζ[ν ^ ξν for ν > 0. Moreover, for some C > 0 we have

max Re ψ (ζ) < C!;a.

In fact the function Re ψ is continuous on the segment of the line Re ζ = 1
cut out by the sector 5(μ); moreover, Re ψ(ζ) is a homogeneous function of
degree α to within 0(1); it follows that the quotient Re ψ(ζ)/ξ
α is constant up
to <9(ξ~
α). Hence the above inequality is satisfied for large enough C. Finally,
we have
 ! δ FKa (ζ) | < Ct exp (-C&* + λ (Cj* - Re ψ (a))).

Repeating the same arguments as in the proof of Propostion 2, but employing
Lemma 3 instead of Lemma 2, we find that there are positive numbers C\ and
C2 so that the inequality

I F (ζ) | < 2 exp (- λ (C a | · - Re ψ (α)))

holds for λ = (7ια
μ~™, ζ e Da. If a = C& and C3 > 0 is small enough, then

ξ e 3>a and ψ(α)<'-7τ-£'ξα. Then for some C" > 0 we obtain

Li
 I F (ζ) | < exp (-C^) . >

182 Yu.S. Il'yashenko

3.5. Conclusion of the proof of the Phragmen-Lindelof theorem for simple and
sectorial cochains.
Theorem. Sectorial functional cochains defined in a standard domain of class L
have the Phragmen —Lindelof property. Moreover, a sectorial functional cochain
satisfying the hypotheses of Proposition 3 vanishes identically on fc +.

< Let F be a sectorial cochain of type σ = (exp ο μ1( ..., exp ο
1 > μι > ... > μΝ > 0. By Proposition 2 the cochain F decreases on R +

no slower than exp( —Ο|ζ| μΓ'). Let F^) be the fc-realization of F. The
restriction of F^ to
 3) = (ΘΧρ°μχ) nmain Π Ω

is a sectorial cochain of type σ(ΐ) = (exp ° μ2, ..., exp ° μ^); its numerical type
is N—l. For any δ > 0 there is a number R > 0 such that the domain 3)
contains the ε-neighbourhood of the sector 5(μ,) defined in Proposition 3. All
the hypotheses of Proposition 3 are satisfied for the restriction of Fw to this
ε-neighbourhood provided that δ is small enough; in particular, F^\^ is an
K-sectorial cochain. Hence Fm decreases on (IR+, oo) faster than
exp( — C | ζ Ιμϊ )· Proceeding by induction on k, we prove that the restriction of
the fc-realization F^y of F to the sector S^ky satisfies the hypotheses of
Proposition 3 for each k, 1 ^ k < N—l. Propostiion 3 applied to F\S^N_j
yields ?

The main function of the set F w is holomorphic in the sector S^y, the
angle of the sector is greater than πμ^, and therefore F|[R+ = 0 by virtue of the
classical Phragmen —Lindelof theorem. >

Theorem. Simple functional cochains have the Phragmen—Lindelof property.

<\ The proof follows from Proposition 1 and the preceding theorem. Let F
be a simple cochain o£ type (vj, v2, ..., v^), Vj > ... > v^ > 0. By
Proposition 1, for any δ > 0 we have

| F (1) | < exp (-C exp (1 - 6) vl*|).

Let F(i) be the 1-realization of F. We set ρ = 3vi In. Then F(i) ο ρ is a
sectorial cochain of type (exp ο μ2, ..., exp ο μ^), μ^· = vy/vj < 1, defined in
the domain p^Vill^ n which includes the sector £(μ) for μ = 1/3, an arbitrary
δ > 0, and R depending on δ. The previous estimate yields

Ι *ω°Ρ (S)l < exp (-C exp (1 - 6) vl 1 · ^ In 1) - exp (-C'fi*^)).

The cochain Fi ο ρ satisfies the hypotheses of Proposition 3 and the preceding
theorem implies that FJJR+ S 0. >

Finiteness theorems for limit cycles 183

§4. Superaccurate asymptotic series

We shall now complete the proof of the identity theorem for compositions
of correspondence maps of elementary singular points under the condition that
the maps TO the central manifold and FROM the central manifold alternate
in the composition (Theorem Β of the Introduction).
At the end of §4.1 we list all the lemmas and theorems that remain to be
proved in order to obtain the identity theorem. The Phragmen — Lindelof
theorem was proved in §3. The lemmas in §1.8 consist of two statements
each: one about regularity and the other about expandability of the cochains
in question. Regularity was proved in §2; we shall now prove expandability.
At the end we shall prove the theorem on the lower bound that was
formulated in §1.7.
We begin with the proofs of elementary properties of functional cochains of
classes 0 and 1.

4.1. Multiplication lemma.
Lemma 2 of §2.1 claims that germs of cochains of classes 0 and 1 form a
differential algebra. The lemma was proved at the end of §2.1 subject to a
lemma stating that JF^1 is closed under multiplication; this lemma will be
proved below. We shall require a somewhat stronger result.
We recall that by definition J 5 ^ = J^ 1 ° exp ° μ for any μ > 0. Since μ
is the operator of multiplication by μ, we can regard the notations J*
7} and
S'li, as synonymous.

Multiplication lemma (ML),
a) 1 ϊ

b) fl.f\,df\  for μ =ξ ν.

< a) According to the definition of cochains of class &\, there are two
assertions to be proved: regularity and expandability of the cochains on the
left-hand side.

Regularity:

We have && ° μ" 1 C ^ by LSl re g a) of §2.3. It follows from
Proposition 1 of §1.4 that the composition F<> In for any F e JF'tf0 is either a
holomorphic function that increases no faster than some power of [ζ| or a
sectorial cochain (the first statement is a special case of the second). Hence
&<$° ο μ" ' ο In C i^reg · By Lemma 1 of §2.1 we have ^^leg • PV^ C L
This proves the regularity.

Expandability:
 exp ο μ c ΡΨ- ° exp ο μ.

184 Yu.S. IVyashenko

By LSI a), this is equivalent to

§<®>.$%χ ο exp c fW ο exp

or for any Fi e &$>, F2 e &<€λ

F ο exp = Fx-F2o exp e f^1 ο exp.

We shall show that given any ν > 0 there is a partial sum Σ of a SAAS-1
that approximates F ο exp in the domain In Ω to within o(exp(—ν exp ξ));
here Ω is a standard domain of class L depending only on F and not on v.
We first write F2 ° exp in the form

F2 ο exp = Zi + R, R = ο (exp (—2v exp %)),

where Σι is a partial sum of an SAAS-1. By definition of simple cochains we
have |Fi| < exp μξ for some μ 6 03 in a standard domain of class 1. Hence

| F,R | = ο (exp(- v exp ξ))

in the domain In Ω. Next we prove that F\ · Σι is a partial sum of an SAAS-1.
We need to verify that F) after multiplication by Σι is "absorbed in the
coefficients" of this sum. This means that

This is equivalent to the statement

(*) Fvx\'I C Λ"1·r for any r e Z +.

We shall proceed by induction on r. The first step: r = 0. In this case we
have Xhr = Jf I> 0 = &<£> by Definition 2 of §1.5. The assertion (*) for
r = 0 now follows from Lemma 1 of §2.1.

Remark. The inclusion (*) for a fixed r implies that for the same r

(**) fS". f1^ r Cfl' r for any μ > 0.

The induction step. Assume that (*) holds for some r; we shall prove it for
r+ 1. The remark implies that (•·) holds for the same r. By Definition 4 of
§1.5, we obtain
 OC1'r+1 = X {$%\. f%l'r ο exp ο μ 10 < μ < 1).

By the induction hypothesis, we now have (*) for r+ 1 instead of r and
therefore also (**). This proves assertion a).
Assertion b) is equivalent to the following statement: let λ = μ~'ν < 1,
F] e &<#\ F 2 e &<€x. Then

The proof is similar to the proof of a) and we shall not go into such detail.

Finiteness theorems for limit cycles 185

Regularity. By Proposition 2 of §1.4, F\ ·> ζ λ is a sectorial cochain (or a
holomorphic function increasing no faster than an exponential function in a
standard domain of class L, that is, a sectorial cochain with a trivial
coboundary). We have F e ^^leg by Lemma 1 of §2.1.

Expandability. We can assume without loss of generality that F\ and Fi are
rapidly decreasing cochains, since otherwise we could multiply them by a
suitable decreasing exponential function. We shall show that for any p, q e Z+
and λ e (0, 1]

(***\ er1' Per1· 11—crx

The proof is by induction on r = ρ + q in the two cases λ < 1 and λ = 1.

Case 1: λ < 1. We shall show that the first factor is "absorbed in the
coefficients". The inclusion (•*•) can then be deduced as in the proof of a).

The initial step: r = 0. We have ρ = q = 0. We need to show that

This follows from the definition of Jf 1> 0 : Jf 1' 0 = &<^, the definition of
1 (see above), and the assertion a), which implies that

we recall that λ < 1, which is needed in the definition of X~'.

Induction step. Let (***) hold for p + q = /·. We shall prove it for ρ + q = r + 1.
It suffices to prove that

But this follows from the definitions of JT 1 ' * and JT 1 and the induction
hypothesis. The inclusion (***) for p + q = r+\ can now be deduced as in
the proof of a). W e have proved the lemma in Case 1.

Case 2: λ = 1.

Proposition 1. The set of partial sums of SAAS-l is closed under multiplication.

The assertion b) can be deduced from this proposition using standard
arguments as in the proof of the assertion a).

Proof of Proposition 1. We denote by Σ 1> Γ the set of partial sums of SAAS-l,

r, Σ 1 = U Σ 1 ·' . It is sufficient to prove the following inclusion for any

p, q e Z+:

(***•) Σι·ρ. Σ 1 · 9 d Σ 1 .

The proof is by induction on r = p + q.

186 Yu.S. IVyashenko

The initial step: r = 0. The set El of indices of SAAS-1 is closed under
addtion, and the set Jf1>0 of coefficients of SAAS-1, 0 is closed under
multiplication. We have jTh° = &<$° and &<€ • Ρ<0° C && by Lemma 2
of §2.1.
The induction step: assume that (••*•) holds for p + q = r. As usual, this
implies that
 fitff+v'CZfiv for μ<ν , p + q=r.

It follows that
 3Γ1·p' .X 1'q' c ΛΓΐ for p' + g '= r + l.

This completes the induction. >

We have thus proved not only the multiplication lemma but also Lemma 2
of §2.1, which states that the germs of cochains of class ^^ form a
differential algebra.

4.2. Completeness.
Lemma. Let φ be a function of one variable that is holomorphic in some
neighbourhood of zero. Then

φο0"- φ (0) C $W+, n = 0,1 .

< Let F e r C w = 0, 1. ^ = <p ο F - φ (0).
Then F e jF$£ g , which follows from Lemma 3 of §2.2. This proves the
regularity of F .
Next we prove the expandability of F for η = 1; the proof for η = 0 is
similar but simpler. Since F->•0asζ->ooi n some standard domain of class
L, we can choose a representative of F in the domain Ω of class L so that

φ ο F ο exp - <p(0) = J^S-lE-F' ο exp

3= 1
converges in In Ω. Any partial sum Ρ of this series is a polynomial in F and
belongs to the space &%*+ ° exp. Hence the sum Ρ may be approximated by
a partial sum Σ of SAAS-1 up to o(exp(—ν exp ξ)) for any ν > 0.
Moreover, Ρ approximates the sum of the preceding series up to o((F ο exp)N).
However, F is a rapidly decreasing cochain and this implies that the remainder
is o(exp(—Νε exp ξ)) for some ε > 0. Choosing Ν so that εΝ > ν, we find
that the cochain φ ο F—φ(0) is expandable. t>

Corollaries. 1. exp β f%l — 1 C fSl, η = 0, 1.

2. ln(l + r^+)C« , η = 0,1.

4.3. First lemma on shifts.
This lemma was formulated in §1.8. Assertion a) was proved in §2.3. We
now prove a stronger version of b).

Finiteness theorems for limit cycles 187

Proposition 1. For any μ > 0 and C e R

< This inclusion is equivalent to

ΡΨ ο A-1 (id + μϋ +

The equivalence follows from LSI a). The regularity (the inclusion of the left-
hand side in ^^leg) follows from Proposition 5 of §2.6 and the fact that shift
transforms into dilatation under logarithmic conjugation.
We now prove the expandability. Let Fx e J^ 1 , F2 e &<£% and let F be
a germ defined by
 F ο exp = F1 ο exp ° (id + C + Ft).

Proposition 2. Ε1 ° (id + C + ftf+) C E1 + f %%.

<\ The proposition follows from Taylor's formula, the multiplication lemma,
and completeness lemma of §4.2. >

For any ν > 0
 F1 ο exp = 2 -f R,

where Σ is a partial sum of SA.AS-1 and R is the remainder

R = ο (exp (—v exp ξ))

in a domain In Ω, where Ω is some standard domain of class L depending on F\.
Let F2 e J 5 "^ . We shall show that the partial sum and the remainder
withstand a change of variable ζ Η» ζ + C + F2, that is, they remain a partial
sum of SAAS-1 and a remainder.

Change of variable in the remainder.

R ο (id + C + F2) = ο (exp (-v exp (ξ + C + ο (1))) =

= ο (exp ((—νμ + 1) exp ξ)), where μ = exp C.

Change of variable in the partial sum of SAAS-1. It is enough to show that
Σ ο (id + C + F2) is a term of SAAS-1 under the condition that Σ = a exp e is
also a sum of a single term. We shall show by induction on the rank r that

(*) ^f 1 · τ ο (id + C + F2) c JT 1· r.

This will be used to show that

(··) PS1· r ο exp ο (id + C + Ft) d f "g1'r ο exp.

The initial step: r = 0. The formula (*) follows from LS2 a) for η = 0,
which was proved completely in §2.4. Hence there exist Fit F4 e

188 Yu.S. Il'yashenko

such that

(***) (a exp e) ο (id + C + F 2) = b exp {e1 + F 3) =

The equality 1 follows from Proposition 2, the equality 2 from Corollary 2 of
§4.2, and the equality 3 from the multiplication lemma. Hence

Σ1-0 β (id + C + f& +) d ΣΜ .

The change of variable in the remainder has already been discussed. Hence,
the change of variable ζ n · C, + C+F2, F 2 e ^"<if+ takes cochains that are
expandable in SAAS-1, 0 to cochains with the same property. This proves
(**) for r = 0.
The induction step. The formula (*) for r+l follows from the definition
of jfT1'r+1 (it is mentioned on p. 184) and the induction hypothesis, that is
from (**) for r. The formula (*) for r + 1 then implies the chain of equalities
(•**) for a e Jf 1>r+ 1 and this yields the inclusion (**) for r + 1 instead of r. >

4.4. Second lemma on shifts (LS2).
a) The set id + 5^+ , η = 0, 1, is closed under compositions;

b) (id + f «?)-i C id + f #?, η = 0,1 ;
c) f%° ο (id + £i) C .f ^° + .f Ϊ,

, moreover, if φ €Ξ f^ 0, then

φ ο (id + r J +) C φ + f\;

d) let μ ^ v, then

and, moreover, if φ ε= f μ,

φ ο (id + fi v ) C φ + fi v

The assertion a) of LS2 for η = 0 was proved completely in §2.4. For the
other assertions, we have proved the regularity (Jf\, ^ί μ , $f\v must be
replaced by F$£ g ° exp ° R +, ^^Jeg ° exp ° μ, ^^ g ° exp ο v). We still
need to prove the expandability (the exact formulation will be given below).
Assertion b) will be proved below. The assertion a) for η = 1 and c) and d)
will be proved simultaneously. They all follow from the next proposition.

Proposition 3. Let 0 < μ «5 ν, φ ε ^Γ«7° U &\, ψ e ^Vv · Then

< By definition we have either φ = F\ e i 2 ^ 0 or φ = F } ° exp ο μ, Fi e
ψ = F 2 ο exp ov,F 2 e ^^\. We need to prove that there is a germ F e
such that φ = F ° exp ° v. The regularity of F (that is, F e ^^ieg) was

Finiteness theorems for limit cycles 189

proved in §2.4. We now prove the expandability of F ° exp in SAAS-1. By
the definition of F we have

F ° exp = φ ο ν" 1 ο (id + F\ ° exp) — φ ο ν" 1, F2 = \F2·

If φ e gfg0, then φ ο v" 1 e &<{? by LSI. For (pe/Jw e have
φ ο ν" 1 e 2F\, λ = μν" 1 . In both cases we set φι = φ ° ν" 1 . Let us
expand F <> exp in a Taylor series

F ο exp = Σ + R,

where

and R is the remainder, which will be estimated below. We shall show that Σ
can be expanded in SAAS-1. It follows from Lemma 2 of §2.1 that
φ[η e F^ U &l for ally with λ < 1. By the multiplication lemma, all the
terms of Σ, and hence also Σ itself, belong to ^"if + ο exp.
Let us now estimate the remainder. By the definition of simple and sectorial
cochains, any cochain from ^ ^ \J &\ increases no faster than exp Cξ or
exp(C exp λξ) in Ω or λ" 1 hi Ω, where λ < 1; the standard domain Ω of
class L and the positive constant C depend on the cochain. We shall applyJhis
estimate to the derivative φ[Ν+1\ Moreover, the exponential estimate for F2

\Ft\< exp {-xl)

for some κ > 0 implies that we can choose representatives of F\ and F2 in Ω
in such a way that the composition

R = <ρ[Ν+1) ο (id + θν-^ 2 ο exp)

is defined for any θ e [0, 1] in the domain In Ω. This composition has an
upper bound:

I R I -< exp (C exp λ (ξ + ο (1))) -< exp (2C exp λ|) .

Estimating the remainder in the Taylor formula, we obtain

I R | < ( max fi)\F2° exp |* + 1 •< exp (2C exp λξ — χΝ exp ξ).
ee[o, ι]

We recall that λ < 1. If Ν is large enough, then the remainder decreases
faster than exp(—α exp ξ) for any preassigned α in the domain In Ω.
On the other hand, the cochain Σ is expandable in SAAS-1, which proves
Proposition 1. >

We can now complete the proof of LS2 by proving the assertion b):

(id + f «i)-1 = id + f %\.

190 Yu.S. ll'yashenko

< Let F, e &&+. We need to show that

The regularity, that is, F e J^^g , has been discussed in §2.4. It remains
to prove the expandability of F ο exp in SA AS-1.
We first prove that the equality

F ο exp = A (id + Fj)'1 — id

defines a germ F e 3P%>1+. Let us consider the composition

A (id + F-,) = id + In (1 + exp (— ζ) Fx ° exp) = id + Fx ο exp;

F ι e &<g\ by Corollary 1 of the completeness lemma in §4.2. We set

h = Fr ο exp, (id + h)'1 — id — 7ι, Τι = F « exp.

Then
 •h = h ° (id - Ji).

Let us consider the "successive approximations" to It :

h
0 = h, hi = h ο (id — h0), . . ., hn = h ° (id — hn-i).

By Proposition 1, each hn belongs to J^ V ° exp. In particular, they approach
the partial sums of SAAS-1 as required in the definition of expandability
(Definitions 3 and 5 of §1.5). ^
Let us estimate the difference h —hn; we shall show by induction on η that

I * - Κ | < Ι (1Ϊ (id + ο (1)))»« h ο (id + ο (1)) |.

The initial step:

I
 n - Κ I = i * - h I = \h ο (id - Τι) - h | < | h' ο (id + ο (1)) || R | =

= | h'o (id + ο (1)) || Λ ο (id + ο (1)) |.

The induction step:

I 7i — hn | = | h ο (id — ») - h ο (id - ha-i) | < I fc' ° (id + ο (1)) || Τι -

- h^i | < | Α' ο (id + ο (1)) r 1 . | Λ ο (id + ο (1)) |.

The last inequality follows from the induction hypothesis.
Using the definition of the set of rapidly decreasing cochains and the
lemma which states that this set is closed under differentiation, we find that
there is a κ > 0 such that

| h | < exp (—κ exp ξ), | h' | < exp (—κ exp ξ)

in the domain In Ω.
 Finiteness theorems for limit cycles 191

Hence for any natural number Ν in this domain we have

| Τι - hN | -< exp (- κ (Ν + 1) exp ξ).

The difference h —hN for sufficiently large Ν satisfies the estimate imposed on
the remainder of SAAS-1 in Definitions 3 and 5 of §1.5. This proves the
expandability of F ο exp = h and F e ^^l+.
Next we prove that F e ^^l+. We have

id + F ο exp = A (id + F^K

Hence

id + F = A-1 (id + F - exp) = exp ο (In ζ + F) = ζ exp F' = ζ + ζΨ,

where Fe 3F(€\ by Corollary 1 of the completeness lemma in §4.2.

The multiplication lemma implies that ζί ε &<$+; but ζF = F, which
completes the proof of b). t>

4.5. Third lemma on shifts (LS3).
Let μ > ν. Then
 fl ο (id + fiv) = §\.

< Let F\ e &<βλ, F2 e &% + , λ = μ~'ν. It is enough to prove that the germ
F ο exp defined by
F ο exp = Fx ο exp ο (id + F2 <> exp ο λ)

is expandable in SAAS-1 (the regularity of F was proved in §2). In turn, it is
sufficient to show that a partial sum of SAAS-1 remains a partial sum after
shift of the argument by a correction from &\\ with λ < 1, and the remainder
has practically the same upper bound as before the shift.
The estimate of the remainder is similar to that in the proof of LS2 and
will not be carried out in detail. Let us consider a partial sum of SAAS-1
consisting of a single term s. We shall show that

(*) s ο (id + F2 ο exp ο λ)

is again a term of SAAS-1. The lemma then follows.
Let
 s = a exp e, e €Ξ Ε\ α ΕΞ 3& p, F2 <ΞΞ f^i' q -

We shall prove (*) by induction on the sum of ranks r = p + q.
We first note that it follows from LS2 that for any ρ and q and an
arbitrary e e El there is a germ F3 e tF<€\ such that

e ο (id -f F2 ο exp ο λ) = e -f- F3 ° exp ο λ.

192 Yu.S. IVyashenko

The initial step: r = ρ = q = 0. Then a e ^<^°. By LS2 there is a
germ F
A e &<€x£ such that

a o (id + F2 ο exp ο λ) = α + F
t ° exp ο λ.

Then

(*•) (α exp e) ο (id + F
2 ° exp ο λ) =
 def
= (a + F
t ο exp ο λ), (exp ° F
s <> exp ο λ), exp e = b exp e.

By Corollary 1 of the completeness lemma and the multiplication lemma,
we have b e jf 1 · 1 .

Remark. The shift of argument considered above increases by one the rank of
the series to which the monomial belongs. This makes it necessary to introduce
series of non-zero rank in the proof of the identity theorem.

The induction step. Assume that (*) holds for a fixed r\ we shall prove it
for p + q = r + 1. By the induction hypothesis and the definition of Jf
]
·'' we
have
 χι, ν ο (id + f &; ' " exp ο λ) C W\

Hence there are a e Jf\ F
3 e &<g\ such that

(a exp e) ° (id -f- F
2 ° exp ο λ) = ά. (exp ο F
3 ° exp ο λ), exp e = b exp e.

By the multiplication lemma and the corollary to the completeness lemma
we find that b e Jf'. Hence b exp e is a term of SAAS-1, which completes
the proof of LS3. >

4.6. Fourth lemma on shifts and the lemma on conjugation.
Fourth lemma on shifts.
a) 7°<Zid+r#Rt ;
b) f ί μ ο 7° = ,f ϊ μ /or arcy μ > 0.

<\ Assertion a) was proved in §2.6. Assertion b) follows from a) and
Proposition 1 of §4.3. [>

Lemma on conjugation.
a) Ad (Aff) (id + fK) = id + ?K>
b) Ad (J?) H
1
 = H
1
,
and moreover if g e 8t and μ = lim g', then

Ad (g) (id + riv) c : id + 4μν;

c) Ad (7°) F 1
 = H
1
.
 Finiteness theorems for limit cycles 193

< a) Let α ε Aff, a = αζ + β, F e J^ . Then

Ad (a) (id + F) = of1» (a + F ° a) = a" 1 (a — β) + a -1 F ° a = id + a^F ° a.

By LSI a) we have α" 1 / " ο a e ^^°+, which proves the assertion a).
b) The first statement follows from the second by the definition of H1. Let

Β = μ ° ft. ft = id + C + Fx, id + f
1! €Ξ ^°.

We note that
 Ad (μ) (id + riv ) = id + ^μν ·

Almost regular germs form a group, and therefore

gi 1 == id-C-/' 1 . id-^fEE^ 0 , / ^

It is enough to show that for any F2 e &<$\. there is a germ F e ^^\ such
that
 Ad_(gx) (id + F2 ° exp ο v) = id + F ο exp ο ν.

By LS2 there is a germ F2 e &<€l+ such that

—P1 ο (id + F2 ο exp ο v) = —Fx -{- F3 ο exp ο ν.

Hence

Ad (gx) (id + F2o exp ο v) =

= (id — C — F1 + F2 ο exp ο ν -+- F3 ° exp ο ν) ο ^ = id -f f o exp ο ν,

where F e &<€\. The last equality follows from LSI b), and this completes
the proof of the assertion b). >

c) The proof is similar to the proof of b). By the definition of the group
Hl (see §1.6) we only need to show that for any F e J°

Ad (F) (id + Ρ8\ ο exp) C id + f<g\ ο exp.

By LS4 a) there is a germ Fx e 3^^°+ such that F"1 = id + Fi. Then

Ad (F) (id + flu) = (id + f} i d + F1 ο (id + f* ld) ο F 4 (id + F1 + ^ϊω)

= (F"1 + fi,„) ο F = id + r«i w ° ^ = id +

The equality 1 follows from LSI and the equality 2 from LS4. This
completes the proof of the lemma on conjugation. >

We have thus proved all the lemmas of §1.8. Hence the proofs of the
additive and multiplicative theorems on expansion in §1.9 become unconditional.
We still need to prove the theorem on the lower bound for partial sums of
SAAS-1 (see §1.7).

194 Yu.S. Il'yashenko

4.7. Theorem on the lower bound.
Let Σ be a weakly real SAAS-l, ν the highest principal exponent of terms of Σ,
and Σ] a partial sum of this series. Then for any ε > 0

Re Σ1 >- exp ((v — ε) exp ξ) on (R+, oo).

The theorem is proved by induction on the rank of Σ. We prove the
following statement at the same time.

Supplement. The argument of a partial sum of an arbitrary weakly real SAAS-l
tends to zero modulo π on (R + , oo).

We shall refer to the theorem on the lower bound together with the
supplement for series of rank r as LBr.

Fundamental lemma. Let Σ] be a partial sum of a weakly real SAAS-l whose
terms all have zero principal exponents. Then for any ε > 0 we have

(*) | Re Σ1 | >- exp (- ε exp ξ) on (R\ oo);

arg Σ χ -*• 0 (mod π) on (R+, oo).

The fundamental lemma for series of rank r will be denoted by FL r. We
shall prove this lemma by induction on r. First we formulate corollaries of it.

Corollary 1. LBr.

Before stating further corollaries, we shall introduce an ordering for
functions (R + , oo) -> C:

(**) /-< g-H- Re/-<Re £ on (R+, oo)

and for cochains:

(**·) F -<G^FU -< Gu.

We recall that F" is the function of F that is defined in the domain adjacent
to the ray (R + , oo) from above and includes this ray.

Examples. 1) The set of sums of real quasipolynomials is ordered by (**).
2) The set of functions that are expandable in distinct real Dulac series is
ordered by (**).
3) The set of weakly real simple cochains iF^R is ordered by (**).
The last statement follows from the Phragmen — Lindelof theorem, as a
result of which Dulac series for different (on R + ) simple cochains are different,
and from Example 2.

Corollary 2 of FL r. The set of weakly real sectorial cochains of rank r is
ordered by (***).
 μ>0

55 Γ+ 1
 Finiteness theorems for limit cycles 195

Corollary 3 ofFL,. The union [j ,f (ρ>,
Γ

μ antf ί/ie set xh r+ 1 are ordered bv {***).
>
For any α e ^55 Γ+1 , α ψ 0, //zere ύ α μ € (0, 1) such that on (R + , 00)

(***) I a I >- exp (—exp μξ)

arg a -*- 0 (mod π).

The implications FL r =Φ Corollary 1 ==> Corollary 2 =Φ Corollary 3 are
trivial and can be proved by the same arguments as in the proof of the
identity theorem in §1.7. We now only need to prove the fundamental lemma
to complete the proof of the theorem on the lower bound.

Proof of the fundamental lemma. The initial induction step is based on (***)
for the set wfe ° = f $|R (see Example 3).
The induction step is the deduction from the assertion (***) for ,%'jp r of the
fundamental lemma FL r, which implies (***) for /W^
r+1
, as we have shown.
Assume that (***) holds for an arbitrary a e Jf^''. Let

Ν
- ι = 2J "j ex P ej
1

be a partial sum of SAAS-1, r; e,· ε Ε1, aj e ,"//'$>'', v(ej) = 0. We shall prove
FLr by induction on the number of terms N.
The initial step: Ν - 1. In this case we have Σλ = αχ exp ej. The
coefficient αλ satisfies (***). Since Ime j = 0 on (R + , 00) and v(e]) = 0, we
find that Σι satisfies the conditions (*). This completes the initial step.
The induction step. Assume that the fundamental lemma holds for partial
sums of SAAS-1, r consisting of Ν terms; we shall prove it for sums consisting
of Ν + 1 terms. The proof is based on the following proposition.

Proposition 1. Let a\, a2 e X^r, ε 1 ; e2 ε Ε1. Then there is a limit

1= lim φ, φ = α2 exp ei/a1 exp ev
(R+. «>)

that can be either finite {and then real) or infinite.

<] By Corollary 3 we have

arg φ -> 0 (mod π) on (R +, 00).

We have also
 φ =

The set Sfcfc r forms a differential algebra by its definition and Lemma 2 of
§2.1. We have El C -^R r for any r. Hence the arguments of the numerator

196 Yu.S. Iiyashenko

and denominator of the fraction on the right-hand side tend to zero modulo π.
Moreover, Imfo — ei) = 0, that is, arg exp(e2 —ei) = 0. Hence

arg φ' -> 0 (mod π) on (R+, oo).

The behaviour of the arguments of φ and φ' indicates that Re φ is
monotonic in some neighbourhood of (R + , oo). Because arg φ ->• 0 (mod π),
we obtain the proposition. [>

Assume now that the first term of Σι is the "largest" term in the sense that
its quotients after division by the remaining terms tend to limits whose modulus
does not exceed 1. We set
 Σ 2 = Σ α Ι ατ exp et.

By Proposition 1 there is a limit I = lim Σ 2, | Ζ | < Λ
Γ + 1. We

consider separately the two cases / φ 0 and 1 = 0.

Case 1: Ι Φ 0. FL r now follows from the assertion proved in the initial
induction step.

Case 2: 1 = 0. In this case α\Σ2 is a partial sum of SAAS-1, r consisting of
Ν terms. By the induction hypothesis, (*) will hold if we replace Σ] by αιΣ2.
It follows from Corollary 3 for Ji'p ' (which enters in the "outer" induction
hypothesis for induction on r) that

arg (al) -*-0 (mod π) on (R+, °o).

Hence

(V ) arg Σ2-^ 0 (mod π) on (R+, 00).

The following inequality is satisfied for some ν > 0:

I «i I -< exp (νξ).

Hence for any ε > 0 we have

I Re Σ2 I >- κε, where κ ε (ξ) = exp (—ε exp ξ).

We now prove that (*) holds for Σ 2 instead of Σ ^ The second assertion
follows from (***) and the assumption that / = 0. Let us prove the first
assertion. It is enough to show that for any ε > 0

| Re Σ 2 | >-κ ε on (K+, 00).

This can be proved using only the following properties:

κε: κε -*-0, κ ε > 0, κ ε -> 0, κε < 0

and the estimate | Re Σ 2 | >- κ ε. We have
 S I Re 2; I =, I Re 2 2 (ξ) I.

Finiteness theorems for limit cycles 197

The last equality uses the following two facts: / = £2(00) = 0, and Re Σ2
does not change sign. Using the assertion proved in the initial step, we find
that Σ] = (α, exp ei)E 2 satisfies the first inequality of the system (•). This
completes the induction step and thus proves FL r.
We have proved the fundamental lemma for arbitrary r; this proves at the
same time the theorem on the lower bound and hence also the identity theorem
for compositions of class 1 (Theorem Β of the Introduction).

Appendix I

We now prove the lemma formulated in §0.5.

Lemma. The correspondence map of a saddle-type hyperbolic singular point of a
real analytic vector field is almost regular.

<\ By the definition of an almost regular germ, we need to prove that the
map in question written in the logarithmic chart (which was denoted by Δ in
[5] whereas we use the notation Δ ) has the following properties: a) it can be
extended biholomorphically to some quadratic standard domain Ω and b) it is
expandable in an asymptotic Dulac series in this domain. Assertion a)
(regularity) was proved in §3 of [5]. Assertion b) (expandability) can be
proved by a slight modification of the arguments employed in §3 of [5].
Dulac [15] showed that the vector field in question is orbitally analytically
equivalent to the field corresponding to the equation

ζ = ζ, w = —w (λ + zNw Nf (z, w))

for any natural number TV if the ratio — λ of the eigenvalues of the singular
point is irrational, and to the equation

(*) Ζ = Z, W = —w (λ + Ρ (U) + U N+1f (z, W))

for λ = m/n. Here u = zmw n is a resonance monomial, Ρ is a real polynomial
without a free term whose degree does not exceed N, and / is a function
holomorphic at zero., We can assume without loss of generality that |/ | in
the unit bidisc D = {\z\ ^ 1, Μ ^ 1} is less than any preassigned constant;
this can be achieved by a change of scale.
We shall prove the lemma for rational λ; the proof for an irrational value
is similar but simpler. By definition the correspondence map of the equation
(*) takes points of the transversal w = 1 to the transversal ζ = 1. We shall
need the following construction (see [5]). Let Ω be a quadratic standard
domain to which the map Δ can be extended biholomorphically, and let ζ =
ξ + i η e Ω be an arbitrary point. We denote by μ^ the curve with origin 0
and terminal point ζ consisting of two segments [0, ξ] and [ξ, ζ].
We set γ 0> ζ = εχρ(μζ — ζ) χ {0} (Fig. 5). The origin of the curve γ°· ζ is
&1 = (εχρ(-ζ), 0). Let & = (εχρ(-ζ), 1) and let γ ζ be an arc with origin 0>
that covers γ°' ζ on a solution of (•) and terminates at Q.

198 Yu.S. Il'yashenko

We set
 u = —n~ l In u = — (λ In ζ + In w).

It was shown in [5] that
 Δ(ζ ) = -I n u>(0),

•I (Q) = ;7 (.SP) + ο (1), ο (1) ->0 as ζ ->• σο in Ω.

By the definition of Ζ we have «(0») = ^λζ, 7i(Q) = Δ (ζ). Hence
Δ (ζ) = λζ + ο(1). We need to show that Δ (ζ) can be expanded in a Dulac
series in Ω. We consider a reduced system (*o), which is obtained from (*) for
/ = 0, and investigate the correspondence map Δ 0 for this system written in
the logarithmic chart; we then prove that the difference Δ — Δ 0 is small. The
function u on the trajectories of (*0) satisfies the factor equation
(*·) du
dtu
 = V V (tT) = ( ex P (—

Since P(0) = 0, we have V{u) = 0(1) exp(-w) . Let g'v be ^the
transformation of the phase flow of the field V during time t, and Δο the
correspondence map for the equation (*0) written in the logarithmic chart.
The time of motion along the arc γ<£ (the analogue of γ ζ for (*0)) is equal to
— In ζ = ζ. Hence

The solution φο of (**) with the initial condition φο(Ο) = λζ is holomorphic
in the disc |;| < C|ζj for any C > 0 and sufficiently large (ζ|. It follows that
the Taylor series for φο(ζ) = Δ 0(ζ),

converges. For / = ζ the series on the right-hand side changes into a
convergent Dulac series.
 Fig. 5

Finiteness theorems for limit cycles 199

Next we compare the maps Δ and Δ 0- For the complete system (*), on
the curve γ ζ lying in the bidisc Β (this was proved in [5]) we have

(***) ε = ν («) + R (t), | R | < | uN+1 }.

The function R is known if we know the curve γ ζ; we require only the estimate
for R (see above). Let φ be the solution of (***) with the initial condition
<p(0) = λζ. Then φ (ζ) = Δ (ζ). Let us estimate | φ(ζ) — Φο(ζ) I using Gronwall's
inequality. Let S be the length of the curve μζ; this is the curve traversed by
the time t while the phase point passes along the curve γ ζ; S < 2|ζ|. It was
shown in [5] that the solution cpj ζ assumes values in a disc Κ with centre cp(O)
and radius o(l) as ζ -> oo. Let us set L = max | V | = ο (j ζ]~
χ
)- From
Gronwall's inequality we obtain

Ι <P (D - Ψο (ζ) Κ max I R | exp LS =

= o (exp ( - (TV — 1) λ|)) = o-(exp (—νξ))

for any preassigned ν > 0 if TV is large enough. This proves the lemma. \>

Appendix II

In this appendix we shall prove two assertions from §0.6: a) the supplement
to the sectorial normalization theorem and b) the supplement to Theorem 2.

Proof of the supplement to the sectorial normalization theorem. We consider an
extension of the normalizing map from the sector S"; the rest of the proof is
similar, but will not be needed. We denote by S1 (I for lower) the sector that
is symmetrical to 5 " with respect to the real axis (Fig. 6);

Fig. 6

it is convenient to imagine that the sectors lie in different copies of the C-plane.
Let F" and Fl be the functions of F nor m that couple the map/ = z — 2nizk+ ] + ...
with the shift along the phase curves of the field o(-) = zk+1/(\ + azk) during
time — 2πζ or, equivalently, of the field — 2πίυ(ζ) = w(z) during time 1.

200 Yu.S. Il'yashenko

We denote this shift by g. The map F" can be extended biholomorphically
along the orbits of /using the equality Fu °. / = g ° F". We first discuss the
orbits of g, and for this purpose we describe the phase curves of iv. We shall
show that in a wedge of small radius containing a segment of the ray
L : arg ζ = — π/2/c, these phase curves touch L at 0, and the order of contact
is not less than k— 1/2 (we could take an arbitrary ε > 0 instead of 1/2). In

fact, we can verify that on the lines γ + = rexp i ( ^rz t r ' c " 1/2 ) tn e fi^d w

is directed into the wedge bounded by these lines. A simple estimate yields

arg ( * • j — arg w (ζ) = π + (ε + ο (1)) r*- 112. This confirms our claim about

the contact of phase curves of w and the arc L. Let ρ and f{p) be two points
in the sector S" Π Sl. We join these points by a curve Γ so that FT" is an
arc of a phase curve of w. The map F" can be extended biholomorphically to
the domain bounded by the lower radius of the sector S" and a portion of the

curve y: γ = LJ fnW = (F1)'1 \J gWFlT. This domain is shaded in Fig. 6.

The union on the right-hand side is a positive semitrajectory of the field w.
It touches L at 0, and the order of contact is not less than k— 1/2. The map
Fl can be expanded in an asymptotic Taylor series with an identical linear
part in the sector Sl containing this semitrajectory. It follows that the curve γ
touches the arc L at zero; the order of contact is not less than 1/2 (it is a
semicubical parabola touching the χ axis). On transition to the logarithmic
chart, this curve goes into a line that approaches the ray η = —π/2/: at a
rate exp( —ξ/2). This proves the supplement. [>

We shall prove that the derivative g'(0) in the asymptotic series for FnOrm in
the expression for the correspondence map of a degenerate elementary singular
point of a real vector field is real. Such a field withstands the involution of
complex conjugation in both variables. This means that a monodromy
transformation of a contracting manifold under conjugation ζ t-+ ζ in the image
and the inverse image goes into its inverse, since a loop around the singular
point on the holomorphic invariant manifold changes its orientation under
conjugation. The normalizing cochain described in the sectorial normalization
theorem is uniquely determined by the monodromy transformation. Together
with the monodromy transformation it couples the inverse map with the shift
during time 1 along the phase curves of the holomorphic vector field. The
cochain obtained from the normalizing cochain by the involution of complex
conjugation in the image and inverse image has the same property. From the
uniqueness of the normalizing cochain whose correction is of higher order of
smallness than that of the normalizing map it follows that this new cochain is
identical with the original one, which means that the original normalizing
cochain is weakly real in the sense of Definition 15 of §1.4. Hence the
corresponding asymptotic Taylor series, that is, the series for F^ or m in the

Finiteness theorems for limit cycles 201

formula Δ = joA lt « -Fnorm» is real. We recall that Ast = f0 ° hk,a,
/o = exp(— l/x), and hk-a can be expanded in a real Dulac series. Hence the
Dulac series for Δ] = hk,a ° f£otm is real. Let g'(0) = ν, ν = Ad(fo)v : ζ »->·
*-+ ζ/(1—ζ In ν), as in §1.1. We set g = vgu g\(0) = 1. The Dulac series for
/ο"1 ° Δ = (Ad(/0)(gi ° ν )) ο Δι is real because Δ is real. The Dulac series
for Ad(/0)gi is equal to χ (see [6] or [15]). Hence the Dulac series for ν is real
as the composition quotient of two real Dulac series. It follows that ν > 0. [>

Historical Comments

The finiteness problem has been regarded as solved for nearly 60 years. It
was treated in Dulac's memoir [15] in 1923 (which was translated into Russian
and published as a book in 1980). It appears that the first doubts about the
completeness of Dulac's proof were voiced by Dumortier: in a talk at the
Bourbaki Seminar Moussu [20] refers to a "private communication, 1977".
In 1981 Moussu sent letters to experts, enquiring whether they regard Dulac's
claim about the finiteness of the number of limit cycles as proved. Two
months previously, I discovered an error in Dulac's memoir (see [4]) and
pointed it out in my reply to Moussu's enquiry. A contemporary expose of
the main correct results of Dulac's memoir and an analysis of the error can be
found in an abbreviated version in [1], [4] and in detail in [6].
We note that the main obstacles that were surmounted in Dulac's memoir
were related to the local theory of differential equations, not analytic as could
have been assumed from the context, but infinitely smooth, and are linked to
the description of correspondence maps for hyperbolic sectors of elementary
singular points. The study of compositions of such maps leading to asymptotic
Dulac series was then fairly elementary. Monodromy transformations of
compound cycles with non-degenerate elementary singular points were studied
in the first part, and with arbitrary elementary singular points (including
degenerate ones) in the second part. Applications of the resolution of
singularities to the study of non-elementary compound cycles were discussed in
the third part; compound cycles consisting of a single singular point were
considered in the fourth part. The complexity of the last two parts was caused
by the fact that they rely on the theorem about resolution of singularities
which was proved only 45 years later (see [21]).
The detailed study of resolution of singularities of vector fields accomplished
by Dumortier in 1977 made the arguments of the last two parts of Dulac's
memoir quite commonplace; they were covered in a few lines in [6]. The
difficulties encountered in the first part of Dulac's memoir have been overcome
by going into the complex plane. Hence all the papers on the finiteness
problem that have been published in the last five years (see [13], [7], [16], [22])
deal more or less explicitly with the difficulties that have not been surmounted
in the second part of the memoir.

202 Yu.S. IVyashenko

Correspondence maps for degenerate elementary singular points have been
fully investigated from the point of view of their extension to a complex
domain in [7] and [17]. The only problem that still remained was the study of
compositions of such maps with almost regular maps. In order to avoid these
problems, we had to develop the formalism of "functional cochains" and
"superaccurate asymptotic series". The whole paper, including the second
part, is developed along the same lines, and the second part will use the same
ideas as the first but will be technically far more difficult.

Among earlier papers on the finiteness problem we should like to mention
in particular Bamon's papers [12] and [13], where the theorem was proved for
quadratic vector fields. A considerable part of the proof was also obtained
independently by Golitsyna [3] and Kotova [9]. They analysed several special
cases referring to the preprint [12].
 References

[I] V.I. Arnol'd and Yu.S. IFyashenko, Obyknovennye differentsial'nye uravneniya,
Dinamicheskie sistemy I, VINITI, Moscow 1985.
Translation: Dynamical systems I (Encyclopaedia of Math. Sciences), Springer -
Verlag, Heidelberg 1988. MR 89g:58060.
[2] S.M. Voronin, Analytic classification of germs of conformal maps (C, 0) -> (C, 0)
with identity linear part, Funktsional. Anal, i Prilozhen. 15:1 (1981), 1-17.
MR 82h:58008.
= Functional Anal. Appl. 15 (1981), 1-13.
[3] M.G. Golitsyna, Nesobstvennye slozhnye tsikly kvadratichnykh vektornykh polei na
ploskosti (Ideal compound cycles of quadratic vector fields on the plane), Gor'ki 1987.
[4] Yu.S. Il'yashenko, Singular points and limit cycles of differential equations on the
real and complex planes, Preprint Sci. Res. Comp. Centre, Pushchino 1982.
[5] , Limit cycles of polynomial vector fields with non-degenerate singular points
on the real plane, Funktsional. Anal, i Prilozhen. 18:3 (1984), 32-42.
MR 86a:34054.
= Functional Anal. Appl. 18 (1984), 199-209.
[6] , Dulac's memoir "On limit cycles" and related problems of the local theory of
differential equations, Uspekhi Mat. Nauk 40:6 (1985), 41-78. MR 87j:34052.
= Russian Math. Surveys 40:6 (1985), 1-49.
[7] , Separatrix lunes of analytic vector fields on the plane, Vestnik Moskov. Univ.
Ser. I Mat. Mekh. 1986, no. 4, 25-31. MR 88e: 34050.
= Moscow Univ. Math. Bull. 41:4 (1986), 28-35.
[8] , Finiteness theorems for limit cycles, Uspekhi Mat. Nauk 42:3 (1987), 223.
[9] A.Yu. Kotova, Ο teoreme konechnosti chisla predel'nykh tsiklov u kvadratichnyk sistem
(A theorem on the finiteness of the number of limit cycles of quadratic systems),
Gor'ki 1987.
[10] R. Courant, Geometrische funktionentheorie, Gottingen 1921.
Translation: Geometricheskaya teoriya funktsii kompleksnoi peremennoi, ONTI,
Moscow — Leningrad 1934.
[II] E.C. Titchmarsh, The theory of functions (2nd ed.), Oxford University Press, 1952.
Translation: Teoriya funktsii, GITTL, Moscow 1956.
[12] R. Bamon, Solution of Dulac's problem for quadratic vector fields, Preprint,
Universidad de Chile, 1985.

Finiteness theorems for limit cycles 203

[13] R. Bamon, Quadratic vector fields in the plane have a finite number of limit cycles,
Publ. Math. IHES No. 64 (1986), 111-142. M R 88(1:58095.
[14] , J.C. Martin-Rivas, and R. Moussu, Sur le probleme de Dulac, C.R. Acad.
Sci. 303 (1986), 737-739.
[15] H. Dulac, Sur ies cycles limites, Bull. Soc. Math. France 51 (1923), 45-188 .
Translation: Ο predel'nykh tsiklakh, Nauka, Moscow 1980. M R 82k:34031.
[16] J. Ecalle, J. Martinet, R. Moussu, and J.-P. Ramis, Non-accumulation de cycles
limites, C.R. Acad. Sci. 304 (1987), 375-378, 431-434.
[17] Yu.S. Il'yashenko, The finiteness problem for limit cycles of polynomial vector fields
on the plane, germs of saddle resonant vector fields and non-Hausdorff Riemann
surfaces, Lecture Notes in Math. 1060 (1984).
[18] B. Malgrange, Travaux d'Ecalle et de Martinet-Ramis sur les' systemes dynamiques,
Sem. Bourbaki, Vol. 1981/82, Asterisque No. 92-9 3 (1982), 59-73 . M R 84m:58023.
[19] J. Martinet and J.-P. Ramis, Problemes de modules pour des equations differentielles
non-lineaires du premier ordre, Publ. Math. IHES No. 55 (1982), 63-164.
MR 84k:34011.
[20] R. Moussu, Le probleme de la finitude du nombre de cycles limites (d'apres
Bamon R. et Il'yashenko Yu.S.), Sem. Bourbaki, Vol. 1985/86, Asterisque
No. 145-146 (1987), 89-101 . M R 88g:58159.
[21] A. Seidenberg, Reduction of singularities of differential equations Ady = Bdx, Amer.
J. Math. (1968), 248-269.
[22] J.Ch. Yoccoz, Non-accumulation de cycles limites, Sem. Bourbaki, Vol. 1987/88,
Asterisque No. 161-162 (1988), 87-103 . M R 90d:58127.

Translated by D. Mathon Moscow State University

Received by the Editors 26 September 1989
