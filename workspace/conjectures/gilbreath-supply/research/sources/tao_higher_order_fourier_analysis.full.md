<!-- source: https://terrytao.wordpress.com/wp-content/uploads/2012/12/gsm-142-tao7-higher-book-05june2012.pdf | converted from PDF -->

Higher Order Fourier Analysis

Terence Tao

This is a preliminary version of the book Higher Order Fourier Analysis published by the American
Mathematical Society (AMS). This preliminary version is made available with the permission of the AMS
and may not be changed, edited, or reposted at any other website without explicit written permission
from the author and the AMS.

Author's preliminary version made available with permission of the publisher, the American Mathematical SocietyAuthor's preliminary version made available with permission of the publisher, the American Mathematical Society

To Garth Gaudry, who set me on the road;

To my family, for their constant support;

And to the readers of my blog, for their feedback and contributions.

Author's preliminary version made available with permission of the publisher, the American Mathematical SocietyAuthor's preliminary version made available with permission of the publisher, the American Mathematical Society

Contents

Preface ix

Acknowledgments x

Chapter 1. Higher order Fourier analysis 1

§1.1. Equidistribution of polynomial sequences in tori 2

§1.2. Roth’s theorem 26

§1.3. Linear patterns 45

§1.4. Equidistribution of polynomials over ﬁnite ﬁelds 59

§1.5. The inverse conjecture for the Gowers norm I. The ﬁnite ﬁeld
case 74

§1.6. The inverse conjecture for the Gowers norm II. The integer
case 92

§1.7. Linear equations in primes 109

Chapter 2. Related articles 129

§2.1. Ultralimit analysis and quantitative algebraic geometry 130

§2.2. Higher order Hilbert spaces 149

§2.3. The uncertainty principle 162

Bibliography 179

Index 185

vii

Author's preliminary version made available with permission of the publisher, the American Mathematical SocietyAuthor's preliminary version made available with permission of the publisher, the American Mathematical Society

Preface

Traditionally, Fourier analysis has been focused on the analysis of functions
in terms of linear phase functions such as the sequence \ ↦→ e(\) := e2πiαn.
In recent years, though, applications have arisen - particularly in connection
with problems involving linear patterns such as arithmetic progressions - in
which it has been necessary to go beyond the linear phases, replacing them
to higher order functions such as quadratic phases \ ↦→ e(\2). This has
given rise to the subject of quadratic Fourier analysis, and more generally
to higher order Fourier analysis.

The classical results of Weyl on the equidistribution of polynomials (and
their generalisations to other orbits on homogeneous spaces) can be inter-
preted through this perspective as foundational results in this subject. How-
ever, the modern theory of higher order Fourier analysis is very recent in-
deed (and still incomplete to some extent), beginning with the breakthrough
work of Gowers [Go1998], [Go2001] and also heavily inﬂuenced by paral-
lel work in ergodic theory, in particular the seminal work of Host and Kra
[HoKr2005]. This area was also quickly seen to have much in common with
areas of theoretical computer science related to polynomiality testing, and in
joint work with Ben Green and Tamar Ziegler [GrTa2010], [GrTa2008c],
[GrTaZi2010b], applications of this theory were given to asymptotics for
various linear patterns in the prime numbers.

There are already several surveys or texts in the literature (e.g. [Gr2007],
[Kr2006], [Kr2007], [Ho2006], [Ta2007], [TaVu2006]) that seek to cover
some aspects of these developments. In this text (based on a topics graduate
course I taught in the spring of 2010), I attempt to give a broad tour of this
nascent ﬁeld. This text is not intended to directly substitute for the core
papers in the subject (many of which are quite technical and lengthy), but

ix

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

x Preface

focuses instead on basic foundational and preparatory material, and on the
simplest illustrative examples of key results, and should thus hopefully serve
as a companion to the existing literature on the subject. In accordance with
this complementary intention of this text, we also present certain approaches
to the material that is not explicitly present in the literature, such as the
abstract approach to Gowers-type norms (Section 2.2) or the ultraﬁlter ap-
proach to equidistribution (Section 1.1.3).

There is however one important omission in this text that should be
pointed out. In order to keep the material here focused, self-contained,
and of a reasonable length (in particular, of a length that can be mostly
covered in a single graduate course), I have focused on the combinatorial
aspects of higher order Fourier analysis, and only very brieﬂy touched upon
the equally signiﬁcant ergodic theory side of the subject. In particular, the
breakthrough work of Host and Kra [HoKr∈005], establishing an ergodic-
theoretic precursor to the inverse conjecture for the Gowers norms, is not
discussed in detail here; nor is the very recent work of Szegedy [Sz∈009],
[Sz∈009⌊], [ Sz∈0∞0], [ Sz∈0∞0⌊] and Camarena-Szegedy [CaSz∈0∞0] in
which the Host-Kra machinery is adapted to the combinatorial setting.
However, some of the foundational material for these papers, such as the
ultralimit approach to equidistribution and structural decomposition, or the
analysis of parallelopipeds on nilmanifolds, is covered in this text.

This text presumes a graduate-level familiarity with basic real analysis
and measure theory, such as is covered in [Ta∈0∞∞], [Ta∈0∞0], particularly
with regard to the “soft” or “qualitative” side of the subject.

The core of the text is Chapter 1, which comprise the main lecture
material. The material in Chapter 2 is optional to these lectures, except for
the ultraﬁlter material in Section 2.1 which would be needed to some extent
in order to facilitate the ultralimit analysis in Chapter 1. However, it is
possible to omit the portions of the text involving ultraﬁlters and still be able
to cover most of the material (though from a narrower set of perspectives).

A⌋∥\owled}me\ts

I am greatly indebted to my students of the course on which this text was
based, as well as many further commenters on my blog, including Sungjin
Kim, William Meyerson, Joel Moreira, Thomas Sauvaget, Siming Tu, and
Mads Sørensen. These comments, as well as the original lecture notes for
this course, can be viewed online at
terrytao.wordpress.com/category/teaching/254b-higher-order-fourier-analysis/

Thanks also to Ben Green for suggestions. The author is supported by
a grant from the MacArthur Foundation, by NSF grant DMS-0649473, and
by the NSF Waterman award.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

Chapter 1

Higher order Fourier
analysis
 ∞

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

2 1. Higher order Fourier analysis

∞.∞. Equ⟩d⟩str⟩⌊ut⟩o\ o{ √oly\om⟩al seque\⌋es ⟩\ tor⟩

(Linear) Four⟩er a\alys⟩scan be viewed as a tool to study an arbitrary func-
tion f on (say) the integers Z, by looking at how such a function correlates
with l⟩\ear √⟨asessuch as n 7! e(˘n), where e(x) := e2πix is the funda-
mental character, and ˘ 2 R is a frequency. These correlations control a
number of expressions relating to f , such as the expected behaviour of f on
arithmetic progressions n; n + r; n + 2r of length three.

In this text we will be studying higher-order correlations, such as the
correlation of f with quadratic phases such as n 7! e(˘n2), as these will
control the expected behaviour of f on more complex patterns, such as
arithmetic progressions n; n + r; n + 2r; n + 3r of length four. In order to do
this, we must ﬁrst understand the behaviour of e§√o\e\t⟩al sumssuch as

N∑

n=1e(ﬀn2):

Such sums are closely related to the d⟩str⟩⌊ut⟩o\of expressions such as
ﬀn2 mod 1 in the unit circle T := R=Z, asn varies from 1 to N . More
generally, one is interested in the distribution of polynomials P : Zd ! T
of one or more variables taking values in a torus T; for instance, one might
be interested in the distribution of the quadruplet (ﬀn2; ﬀ(n + r)2; ﬀ(n +
2r)2; ﬀ(n + 3r)2) as n; r both vary from 1 to N . Roughly speaking, once we
understand these types of distributions, then the general machinery of qua-
dratic Fourier analysis will then allow us to understand the distribution of
the quadruplet (f (n); f (n + r); f (n + 2r); f (n + 3r)) for more general classes
of functions f ; this can lead for instance to an understanding of the distri-
bution of arithmetic progressions of length 4 in the primes, if f is somehow
related to the primes.

More generally, to ﬁnd arithmetic progressions such as n; n + r; n +
2r; n + 3r in a set A, it would suﬃce to understand the equidistribution of
the quadruplet1 (1A(n); 1A(n + r); 1A(n + 2r); 1A(n + 3r)) in f0; 1g4 as n and
r vary. This is the starting point for the fundamental connection between
⌋om⌊⟩\ator⟩⌋s(and more speciﬁcally, the task of ﬁnding patterns inside sets)
and dy\am⟩⌋s (and more speciﬁcally, the theory of equidistribution and
recurrence in measure-preserving dynamical systems, which is a subﬁeld of
er}od⟩⌋ t⟨eory). This connection was explored in the previous monograph
[Ta2009]; it will also be important in this text (particularly as a source of
motivation), but the primary focus will be on ﬁnitary, and Fourier-based,
methods.

1Here 1A is the indicator function of A, deﬁned by setting 1A(n) equal to 1 whenn ∈ A and
equal to zero otherwise.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.1. Equidistribution in tori 3

The theory of equidistribution of polynomial orbits was developed in
the linear case by Dirichlet and Kronecker, and in the polynomial case by
Weyl. There are two regimes of interest; the (qualitative) asym√tot⟩⌋ re}⟩me
in which the scale parameter N is sent to inﬁnity, and the (quantitative)
s⟩\}le-s⌋ale re}⟩mein which N is kept ﬁxed (but large). Traditionally, it is
the asymptotic regime which is studied, which connects the subject to other
asymptotic ﬁelds of mathematics, such as dynamical systems and ergodic
theory. However, for many applications (such as the study of the primes), it
is the single-scale regime which is of greater importance. The two regimes
are not directly equivalent, but are closely related: the single-scale theory
can be usually used to derive analogous results in the asymptotic regime,
and conversely the arguments in the asymptotic regime can serve as a sim-
pliﬁed model to show the way to proceed in the single-scale regime. The
analogy between the two can be made tighter by introducing the (qualita-
tive) ultral⟩m⟩t re}⟩me, which is formally equivalent to the single-scale regime
(except for the fact that explicitly quantitative bounds are abandoned in the
ultralimit), but resembles the asymptotic regime quite closely.

For the ﬁnitary portion of the text, we will be using asym√tot⟩⌋ \otat⟩o\:
X ˝ Y , Y ˛ X , or X = O(Y ) denotes the bound jX j ˇ CY for some
absolute constant C , and if we need C to depend on additional parameters
then we will indicate this by subscripts, e.g. X ˝ d Y means that jX j ˇ C dY
for some C d depending only on d. In the ultralimit theory we will use an
analogue of asymptotic notation, which we will review later in this section.

1.1.1. Asymptotic equidistribution theory. Before we look at the single-
scale equidistribution theory (both in its ﬁnitary form, and its ultralimit
form), we will ﬁrst study the slightly simpler, and much more classical,
asym√tot⟩⌋ equidistribution theory.

Suppose we have a sequence of points §(1)∅ §(2)∅ §(3)∅ : : :in a compact
metric space X . For any ﬁnite N > 0, we can deﬁne the probability measure

N := E n2[N ]◦x(n)

which is the average of the D⟩ra⌋ √o⟩\t masseson each of the points §(1)∅ : : : ∅ §(N),
where we use E n2[N ] as shorthand for 1
N ∑N
n/1 (with [N] := f1∅ : : : ∅ Ng).
Asym√tot⟩⌋ equ⟩d⟩str⟩⌊ut⟩o\ t⟨eoryis concerned with the limiting behaviour
of these probability measures N in the limit N ! 1, for various sequences
§(1)∅ §(2)∅ : : :of interest. In particular, we say that the sequence § : N ! X
is asym√tot⟩⌋ally equ⟩d⟩str⟩⌊utedon N with respect to a reference Borel √ro⌊-
a⌊⟩l⟩ty measure on X if the N converge in the vague topology to , or in
other words that

(1.1) E n2[N ]{(§(\)) = ∫

X { dN ! ∫

X { d

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

4 1. Higher order Fourier analysis

for all continuous scalar-valued functions { ∈ C (X ). Note (from the Riesz
representation theorem) that any sequence is asymptotically equidistributed
with respect to at most one Borel probability measure .

It is also useful to have a slightly stronger notion of equidistribution: we
say that a sequence § : N → X is totally asymptotically equidistributedif
it is asymptotically equidistributed on every inﬁnite arithmetic progression,
i.e. that the sequence \ ↦→ §(q\ + r) is asymptotically equidistributed for
all integers q≥ 1 and r≥ 0.

A doubly inﬁnite sequence (§(\)) n2Z , indexed by the integers rather
than the natural numbers, is said to be asymptotically equidistributed rela-
tive to if both halves2 of the sequence §(1)∅ §(2)∅ §(3)∅ : : :and §(−1)∅ §(−2)∅ §(−3)∅ : : :
are asymptotically equidistributed relative to . Similarly, one can deﬁne
the notion of a doubly inﬁnite sequence being totally asymptotically equidis-
tributed relative to .

Example 1.1.1. If X = {0∅1}, and §(\) := 1 whenever 2 2j ≤ \ < 22j〉

for some natural number | and §(\) := 0 otherwise, show that the sequence
§ is not asymptotically equidistributed with respect to any measure. Thus
we see that asymptotic equidistribution requires all scales to behave “the
same” in the limit.

Exercise 1.1.1.If § : N → X is a sequence into a compact metric space
X , and  is a probability measure on X , show that § is asymptotically
equidistributed with respect to  if and only if one has

lim
N !1 1
N |{1 ≤ \ ≤ N : § (\) ∈ U }| = (U)

for all open sets U in X whose boundary @U has measure zero. (Hint: for
the “only if” part, use Urysohn’s lemma. For the “if” part, reduce (1.1) to
functions { taking values between 0 and 1, and observe that almost all of
the level sets {y ∈ X : {(y ) < t} have a boundary of measure zero.) What
happens if the requirement that @U have measure zero is omitted?

Exercise 1.1.2.Let § be a sequence in a compact metric space X which is
equidistributed relative to some probability measure . Show that for any
open set U in X with (U) > 0, the set {\ ∈ N : §(\) ∈ U } is inﬁnite, and
furthermore has positive lower density in the sense that

lim inf
N !1 1
N |{1 ≤ \ ≤ N : §(\) ∈ U }| > 0:

In particular, if the support of  is equal to X , show that the set {§(\) :
\ ∈ N} is dense in X .

2This omits x() entirely, but it is easy to see that any individual element of the sequen̂e
has no im√ât on the asym√totî equidistribution.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.1. Equidistribution in tori 5

E§er⌋⟩se ∞.∞.3.Let § : N ! X be a sequence into a compact metric space
X which is equidistributed relative to some probability measure . Let
': R ! R be a compactly supported, piecewise continuous function with
only ﬁnitely many pieces. Show that for any { 2 C (X ) one has

lim
N !1 1
N
 X

n2N '(\=N){(§ (\)) =  Z

X { d
  Z 1

 '(t)dt


and for any open U whose boundary has measure zero, one has

lim
N !1 1
N
 X

n2N:x(n)2U
'(\=N) = (U)  Z 1

 '(t)dt
 :

In this section, X will be a torus (i.e. a compact connected abelian Lie
group), which from the theory of Lie groups is isomorphic to the standard
torus T d, where d is the dimension of the torus. This torus is then equipped
with Haar measure, which is the unique Borel probability measure on the
torus which is translation-invariant. One can identify the standard torus T d

with the standard fundamental domain [0∅1)d, in which case the Haar mea-
sure is equated with the usual Lebesgue measure. We shall call a sequence
§ ∅ §2∅ : : :in T d (asymptotically) equidistributedif it is (asymptotically)
equidistributed with respect to Haar measure.

We have a simple criterion for when a sequence is asymptotically equidis-
tributed, that reduces the problem to that of estimating exponential sums:

Pro√os⟩t⟩o\ ∞.∞.∈(Weyl equidistribution criterion).Let§ : N ! T d.
Then§ is asymptotically equidistributed if and only if

(1.2) lim
N !1 E n2⋃N]e(∥ ∆§(\)) = 0

for all∥ 2 Zdnf0g, where e(y ) := e2πiy. Here we use the dot product

(∥∅ : : : ∅ ∥d) ∆(§ ∅ : : : ∅ §d) := ∥§ + ∆ ∆ ∆+ ∥d§ d

which mapsZd  T d to T.

Proo{.The “only if” part is immediate from (1.1). For the “if” part, we
see from (1.2) that (1.1) holds whenever { is a plane wave {(y ) := e(∥ ∆y )
for some ∥ 2 Zd (checking the ∥ = 0 case separately), and thus by linearity
whenever { is a trigonometric polynomial. But by Fourier analysis (or from
the Stone-Weierstrass theorem), the trigonometric polynomials are dense
in C (T d) in the uniform topology. The claim now follows from a standard
limiting argument. 

As one consequence of this proposition, one can reduce multidimensional
equidistribution to single-dimensional equidistribution:

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

6 1. Higher order Fourier analysis

Corollary ∞.∞.3.Letx : N ω T d. T⟨e\x ⟩s asym√tot⟩⌋ally equ⟩d⟩str⟩⌊uted
⟩\ T d ⟩{ a\d o\ly ⟩{, {or ea⌋⟨k 2 Zdnf0g, t⟨e seque\⌋en 7ω k  x(n) ⟩s
asym√tot⟩⌋ally equ⟩d⟩str⟩⌊uted ⟩\T.

E§er⌋⟩se ∞.∞.4.Show that a sequence x : N ω T d is totally asymptotically
equidistributed if and only if one has

(1.3) lim
N !1 E n2[N ]e(k  x(n))e(ﬀn) = 0

for all k 2 Zdnf0g and all rational ﬀ.

This quickly gives a test for equidistribution for linear sequences, some-
times known as the equ⟩d⟩str⟩⌊ut⟩o\ t⟨eorem:

E§er⌋⟩se ∞.∞.5.Let ﬀ; ﬁ 2 T d. By using the geometric series formula, show
that the following are equivalent:

(i) The sequence n 7ωnﬀ + ﬁ is asymptotically equidistributed on N.

(ii) The sequence n 7ωnﬀ + ﬁ is totally asymptotically equidistributed
on N.

(iii) The sequence n 7ωnﬀ + ﬁ is totally asymptotically equidistributed
on Z.

(iv) ﬀ is ⟩rrat⟩o\al, in the sense thatk  ﬀ 6= 0 for any non-zerok 2 Zd.

Remar∥ ∞.∞.4.One can view Exercise 1.1.5 as an assertion that a linear
sequence xn will equidistribute itself unless there is an “obvious” algebraic
obstruction to it doing so, such as k  xn being constant for some non-zero
k. This theme of algebraic obstructions being the “only” obstructions to
uniform distribution will be present throughout the text.

Exercise 1.1.5 shows that linear sequences with irrational shift ﬀ are
equidistributed. At the other extreme, if ﬀ is rat⟩o\alin the sense that
mﬀ = 0 for some positive integer m, then the sequence n 7ω nﬀ + ﬁ is
clearly periodic of period m, and deﬁnitely not equidistributed.

In the one-dimensional case d = 1, these are the only two possibili-
ties. But in higher dimensions, one can have a mixture of the two ex-
tremes, that exhibits irrational behaviour in some directions and periodic
behaviour in others. Consider for instance the two-dimensional sequence
n 7ω (p 2n; 1
2 n) mod Z2. The ﬁrst coordinate is totally asymptotically
equidistributed in T, while the second coordinate is periodic; the shift
(p 2; 1
2 ) is neither irrational nor rational, but is a mixture of both. As such,
we see that the two-dimensional sequence is equidistributed with respect to
Haar measure on the group T  ( 1
2 Z=Z).

This phenomenon generalises:

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.1. Equidistribution in tori 7

Pro√os⟩t⟩o\ ∞.∞.5(Equidistribution for abelian linear sequences).LetT
⌊e a torus, a\d letx(n) := nﬀ + ﬁ {or some ﬀ; ﬁ 2 T. T⟨e\ t⟨ere e§⟩sts
a de⌋om√os⟩t⟩o\ x = x0 + x00, w⟨erex0(n) := nﬀ0 ⟩s totally asym√tot⟩⌋ally
equ⟩d⟩str⟩⌊uted o\Z ⟩\ a su⌊torusT0 o{ T (w⟩t⟨ﬀ0 2 T0, o{ ⌋ourse), a\d
x00(n) = nﬀ00+ ﬁ ⟩s √er⟩od⟩⌋ (or equ⟩vale\tly, t⟨atﬀ002 T ⟩s rat⟩o\al).

Proo{.We induct on the dimension d of the torus T. The claim is vacuous
for d = 0, so suppose that d  1 and that the claim has already been proven
for tori of smaller dimension. Without loss of generality we may identify T
with T d.

If ﬀ is irrational, then we are done by Exercise 1.1.5, so we may assume
that ﬀ is not irrational; thus k  ﬀ = 0 for some non-zero k 2 Zd. We then
write k = mk0, where m is a positive integer and k0 2 Zd is ⟩rredu⌋⟩⌊le(i.e.
k0 is not a proper multiple of any other element of Zd); thus k0 ﬀ is rational.
We may thus write ﬀ = ﬀ1 + ﬀ2, where ﬀ2 is rational, and k0 ﬀ1 = 0. Thus,
we can split x = x1 + x2, where x1(n) := nﬀ1 and x2(n) := nﬀ2 + ﬁ. Clearly
x2 is periodic, while x1 takes values in the subtorus T1 := fy 2 T: k0 y = 0g
of T. The claim now follows by applying the induction hypothesis to T1
(and noting that the sum of two periodic sequences is again periodic). 

As a corollary of the above proposition, we see that any linear sequence
n 7ω nﬀ + ﬁ in a torus T is equidistributed in some union of ﬁnite cosets
of a subtorus T0. It is easy to see that this torus T is uniquely determined
by ﬀ, although there is a slight ambiguity in the decomposition x = x0+ x00

because one can add or subtract a periodic linear sequence taking values in
T from x0 and add it to x00(or vice versa).

Having discussed the linear case, we now consider the more general sit-
uation of √oly\om⟩al sequences in tori. To get from the linear case to the
polynomial case, the fundamental tool is

Lemma ∞.∞.̸(van der Corput inequality).Leta1; a2; : : : ⌊e a seque\⌋e o{
⌋om√le§ \um⌊ers o{ ma}\⟩tude at most1. T⟨e\ {or every1  H  N , we
⟨ave
 jE n2[N ]anj ˝   E h2[H ]jE n2[N ]an+hanj
 1=2+ 1
H 1=2 + H 1=2

N 1=2:

Proo{.For each h 2 [H ], we have

E n2[N ]an = E n2[N ]an+h+ O  H
N
 

and hence on averaging

E n2[N ]an = E n2[N ]E h2[H ]an+h+ O  H
N
  :

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

8 1. Higher order Fourier analysis

Applying Cauchy-Schwarz, we conclude

E \2[N ]a\ ˝ (E \2[N ]jE ⟨2[H ]a\+⟨ j
2)
1=2 + H
N :

We expand out the left-hand side as

E \2[N ]a\ ˝ (E ⟨∅⟨ 02[H ]E \2[N ]a\+⟨ a\+⟨ 0)
1=2 + H
N :

The diagonal contribution h = h0 is O(1=H). By symmetry, the oﬀ-diagonal
contribution can be dominated by the contribution when h > h 0. Making
the change of variables n 7! n   h0, h 7! h + h0 (accepting a further error of
O(H 1=2=N1=2)), we obtain the claim. 

Corollary ∞.∞.↦(van der Corput lemma).Letx : N ! T d be such that the
derivative sequence@⟨ x : n 7! x(n +h)  x(n) is asymptotically equidistributed
onN for all positive integersh. Thenx \ is asymptotically equidistributed
onN. Similarly withN replaced byZ.

Proo{.We just prove the claim for N, as the claim for Z is analogous (and
can in any case be deduced from the N case.)

By Proposition 1.1.2, we need to show that for each non-zero k 2 Zd ,
the exponential sum jE \2[N ]e(k  x(n))j
goes to zero as N ! 1. Fix an H > 0. By Lemma 1.1.6, this expression is
bounded by

˝ (E ⟨2[H ]jE \2[N ]e(k  (x(n + h)   x(n)))j)1=2 + 1
H 1=2 + H 1=2

N 1=2:

On the other hand, for each ﬁxed positive integer h, we have from hypothesis
and Proposition 1.1.2 that jE \2[N ]e(k  (x(n + h)   x(n)))j goes to zero as
N ! 1. Taking limit superior as N ! 1, we conclude that

lim sup
N !1 jE \2[N ]e(k  x(n))j ˝ 1
H 1=2:

Since H is arbitrary, the claim follows. 

Remar∥ ∞.∞.8.There is another famous lemma by van der Corput con-
cerning oscillatory integrals, but it is not directly related to the material
discussed here.

Corollary 1.1.7 has the following immediate corollary:

Corollary ∞.∞.9(Weyl equidistribution theorem for polynomials).Lets 
1 be an integer, and letP (n) = ﬀs ns +    + ﬀ0 be a polynomial of degrees
with ﬀ0; : : : ; ﬀs 2 T d . Ifﬀs is irrational, thenn 7! P (n) is asymptotically
equidistributed onZ.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.1. Equidistribution in tori 9

Proo{.We induct on s. For s = 1 this follows from Exercise 1.1.5. Now
suppose that s > 1, and that the claim has already been proven for smaller
values of s. For any positive integer ⟨, we observe that P(\ + ⟨) Γ P(\)
is a polynomial of degree s Γ 1 in \ with leading coeﬃcient s⟨ s\ s 1 . As
s is irrational, s⟨ s is irrational also, and so by the induction hypothesis,
P(\ + ⟨) Γ P(\) is asymptotically equidistributed. The claim now follows
from Corollary 1.1.7. 

E§er⌋⟩se ∞.∞.̸.Let P(\) = s\ s + ∆ ∆ ∆+ 0 be a polynomial of degree s in
T d. Show that the following are equivalent:

(i) P is asymptotically equidistributed on N.

(ii) P is totally asymptotically equidistributed on N.

(iii) P is totally asymptotically equidistributed on Z.

(iv) There does not exist a non-zero ∥ 2 Zd such that ∥ ∆1 = ∆ ∆ ∆=
∥ ∆s = 0.

(Hint: it is convenient to ﬁrst use Corollary 1.1.3 to reduce to the one-
dimensional case.)

This gives a polynomial variant of the equidistribution theorem:

E§er⌋⟩se ∞.∞.↦(Equidistribution theorem for abelian polynomial sequences).
Let T be a torus, and let P be a polynomial map from Z to T of some degree
s  0. Show that there exists a decomposition P = P 0 + P 00, where P 0∅ P00

are polynomials of degree s, P 0 is totally asymptotically equidistributed in
a subtorus T 0 of T on Z, and P 00is periodic (or equivalently, that all non-
constant coeﬃcients of P 00are rational).

In particular, we see that polynomial sequences in a torus are equidis-
tributed with respect to a ﬁnite combination of Haar measures of cosets of
a subtorus. Note that this ﬁnite combination can have multiplicity; for in-
stance, when considering the polynomial map \ 7! (p 2\∅ 1
3\ 2) mod Z2, it
is not hard to see that this map is equidistributed with respect to 1=3 times
the Haar probability measure on (T)  f 0 mod Zg, plus 2=3 times the Haar
probability measure on (T)  f 1
3 mod Zg.

Exercise 1.1.7 gives a satisfactory description of the asymptotic equidis-
tribution of arbitrary polynomial sequences in tori. We give just one example
of how such a description can be useful:

E§er⌋⟩se ∞.∞.8(Recurrence).Let T be a torus, let P be a polynomial map
from Z to T , and let \ 0 be an integer. Show that there exists a sequence \ j
of positive integers going to inﬁnity such that P(\ j) ! P(\ 0).

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

10 1. Higher order Fourier analysis

We discussed recurrence for one-dimensional sequences § : \ ↦→ §(\).
It is also of interest to establish an analogous theory for multi-dimensional
sequences, as follows.

Deﬁnition 1.1.10. A multidimensional sequence § : Zm → X is asymptot-
ically equidistributed relative to a probability measure  if, for every con-
tinuous, compactly supported function ': R m → R and every function
{ ∈ C (X ), one has

1
N m X

n2∫ m '(\=N){(§(\)) →  Z

∫ m '
  Z

X { d


as N → ∞. The sequence is totally asymptotically equidistributed relative
to  if the sequence \ ↦→ § (q\+ r) is asymptotically equidistributed relative
to  for all positive integers qand all r∈ Zm.

Exercise 1.1.9. Show that this deﬁnition of equidistribution on Zm co-
incides with the preceding deﬁnition of equidistribution on Z in the one-
dimensional case m = 1.

Exercise 1.1.10 (Multidimensional Weyl equidistribution criterion). Let
§ : Zm → Td be a multidimensional sequence. Show that § is asymptotically
equidistributed if and only if

(1.4) lim
N ω1 1
N m X

n2∫ m:n/N2B e(∥ · §(\)) = 0

for all ∥ ∈ Zd\{0} and all rectangular boxes B in R m. Then show that § is
totally asymptotically equidistributed if and only if

(1.5) lim
N ω1 1
N m X

n2∫ m:n/N2B e(∥ · §(\))e( · \) = 0

for all ∥ ∈ Zd\{0}, all rectangular boxes B in R m, and all rational  ∈ Qm.

Exercise 1.1.11. Let 1∅ : : : ∅ m∅ ∈ Td, and let § : Zm → Td be the linear
sequence §(\ 1∅ : : : ∅ \m) := \ 11 + · · · + \ mm + . Show that the following
are equivalent:

(i) The sequence § is asymptotically equidistributed on Zm.

(ii) The sequence § is totally asymptotically equidistributed on Zm.

(iii) We have (∥ · 1∅ : : : ∅ ∥· m) ̸= 0 for any non-zero ∥ ∈ Zd.

Exercise 1.1.12 (Multidimensional van der Corput lemma). Let § : Zm →
Td be such that the sequence @h§ : \ ↦→ § (\ + ⟨) − §(\) is asymptotically
equidistributed on Zm for all ⟨ outside of a hyperplane in R m. Show that
§ is asymptotically equidistributed on Zm.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.1. Equidistribution in tori 11

E§er⌋⟩se ∞.∞.∞3.Let

P(\ 1∅ : : : ∅ \m) := X

i1,...,im 0:i 1+)))+im s i1,...,im \ i1
1 : : : \
im
m

be a polynomial map from Zm to T d of degree s, where i1,...,im 2 T d are
coeﬃcients. Show that the following are equivalent:

(i) P is asymptotically equidistributed on Zm.

(ii) P is totally asymptotically equidistributed on Zm.

(iii) There does not exist a non-zero ∥ 2 Zd such that ∥  i1,...,im = 0
for all (⟩1∅ : : : ∅ ⟩m) 6= 0.

E§er⌋⟩se ∞.∞.∞4(Equidistribution for abelian multidimensional polynomial
sequences).Let T be a torus, and let P be a polynomial map from Zm to
T of some degree s  0. Show that there exists a decomposition P = P +
P , where P ∅ Pare polynomials of degree s, P is totally asymptotically
equidistributed in a subtorus T of T on Zm, and P is periodic with respect
to some ﬁnite index sublattice of Zm (or equivalently, that all non-constant
coeﬃcients of P are rational).

We give just one application of this multidimensional theory, that gives a
hint as to why the theory of equidistribution of polynomials may be relevant:

E§er⌋⟩se ∞.∞.∞5.Let T be a torus, let P be a polynomial map from Z
to T , let " > 0, and let ∥  1. Show that there exists positive integers
a∅ r 1 such that P(a)∅ P(a+ r)∅ : : : ∅ P(a+ (∥   1)r) all lie within " of each
other. (Hint: consider the polynomial map from Z2 to T k that maps (a∅ r)
to (P(a)∅ : : : ∅ P(a+ (∥   1)r)). One can also use the one-dimensional theory
by freezing a and only looking at the equidistribution in r.)

∞.∞.∈. S⟩\}le-s⌋ale equ⟩d⟩str⟩⌊ut⟩o\ t⟨eory.We now turn from the as-
ymptotic equidistribution theory to the equidistribution theory at a single
scale N. Thus, instead of analysing the qualitative distribution of inﬁnite
sequence § : N ω X , we consider instead the quantitative distribution of
a ﬁnite sequence § : [N] ω X , where N is a (large) natural number and
[N] := f1∅ : : : ∅ Ng. To make everything quantitative, we will replace the
notion of a continuous function by that of a Lipschitz function. Recall that
the (inhomogeneous) Lipschitz norm k{kLip of a function { : X ω R on a
metric space X = (X∅ d) is deﬁned by the formula

k{kLip := sup
x2X j{(§)j + sup
x,y2X :x6=y

j{(§)   {(y )j
d(§∅ y ) :

We also deﬁne the homogeneous Lipschitz seminorm

k{k ˙Lip := sup
x,y2X :x6=y

j{(§)   {(y )j
d(§∅ y ) :

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

12 1. Higher order Fourier analysis

De\⟩t⟩o\ ∞.∞.∞∞.Let X = (X∅ d) be a compact metric space, let ◦ > 0,
let  be a probability measure on X . A ﬁnite sequence § : [N] ! X is said
to be ◦-equidistributedrelative to  if one has

(1.6) jE n2[N ]{(§(\)) Γ ∫

X { dj ˇ ◦k{kLip

for all Lipschitz functions { : X ! R.

We say that the sequence § 1∅ : : : ∅ §N 2 X is totally ◦-equidistributed
relative to  if one has

jE n2P {(§(\)) Γ ∫

X { dj ˇ ◦k{kLip

for all Lipschitz functions { : X ! R and all arithmetic progressions P in
[N] of length at least ◦N.

In this section, we will only apply this concept to the torus T d with
the Haar measure  and the metric inherited from the Euclidean metric.
However, in subsequent sections we will also consider equidistribution in
other spaces, most notably on nilmanifolds.

E§er⌋⟩se ∞.∞.∞̸.Let §(1)∅ §(2)∅ §(3)∅ : : :be a sequence in a metric space
X = (X∅ d), and let  be a probability measure on X . Show that the
sequence §(1)∅ §(2)∅ : : :is asymptotically equidistributed relative to  if
and only if, for every ◦ > 0, §(1)∅ : : : ∅ §(N) is ◦-equidistributed relative
to  whenever N is suﬃciently large depending on ◦, or equivalently if
§(1)∅ : : : ∅ §(N) is ◦(N)-equidistributed relative to  for all N > 0, where
◦(N) ! 0 as N ! 1. (Hint. You will need the Arzela-Ascoli theorem.)

Similarly, show that §(1)∅ §(2)∅ : : :is totally asymptotically equidistributed
relative to  if and only if, for every ◦ > 0, §(1)∅ : : : ∅ §(N) is totally ◦-
equidistributed relative to  whenever N is suﬃciently large depending on
◦, or equivalently if §(1)∅ : : : ∅ §(N) is totally ◦(N)-equidistributed relative
to  for all N > 0, where ◦(N) ! 0 as N ! 1.

Remar∥ ∞.∞.∞∈.More succinctly, (total) asymptotic equidistribution of
§(1)∅ §(2)∅ : : :is equivalent to (total) o N !1 (1)-equidistribution of § (1)∅ : : : ∅ §(N)
as N ! 1, where o n!1 (1) denotes a quantity that goes to zero as N ! 1.
Thus we see that asymptotic notation such as o n!1 (1) can eﬃciently con-
ceal a surprisingly large number of quantiﬁers.

E§er⌋⟩se ∞.∞.∞↦.Let N0 be a large integer, and let § (\) := \=N0 mod 1 be
a sequence in the standard torus T = R=Z with Haar measure. Show that
whenever N is a positive multiple of N0, then the sequence § (1)∅ : : : ∅ §(N)
is O(1=N0)-equidistributed. What happens if N is not a multiple of N0?

If furthermore N  N 2
0 , show that §(1)∅ : : : ∅ §(N) is O(1=
p N0)-equidistributed.
Why is a condition such as N  N 2
0 necessary?

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.1. Equidistribution in tori 13

Note that the above exercise does not specify the exact relationship
between ◦ and N when one is given an asymptotically equidistributed se-
quence §(1)∅ §(2)∅ : : :; this relationship is the additional piece of information
provided by single-scale equidistribution that is not present in asymptotic
equidistribution.

It turns out that much of the asymptotic equidistribution theory has
a counterpart for single-scale equidistribution. We begin with the Weyl
criterion.

Pro√os⟩t⟩o\ ∞.∞.∞3(Single-scale Weyl equidistribution criterion).Let § 1∅ §2∅ : : : ∅ §N
be a sequence inT d, and let 0 < ◦ < 1.

(i) If § 1∅ : : : ∅ §N is ◦-equidistributed, and∥ 2 Zdnf0g has magnitude
j∥j  ◦ c , then one has

jE n2[N ]e(∥  § n )j ˝ d ◦
c

if ⌋ > 0 is a small enough absolute constant.

(ii) Conversely, if§ 1∅ : : : ∅ §N is not ◦-equidistributed, then there exists
∥ 2 Zdnf0g with magnitudej∥j ˝ d ◦ C d, such that

jE n2[N ]e(∥  § n )j ˛d ◦
Cd

for some C d depending ond.

Proo{.The ﬁrst claim is immediate as the function § 7! e(∥  §) has mean
zero and Lipschitz constant Od(j∥j), so we turn to the second claim. By
hypothesis, (1.6) fails for some Lipschitz {. We may subtract oﬀ the mean
and assume that R

T d{ = 0; we can then normalise the Lipschitz norm to be
one; thus we now have jE n2[N ]{(§ n )j > ◦:

We introduce a summation parameter R 2 N, and consider the Fejer partial
Fourier series FR {(§) := X

k 2Z d
m R (∥) ˆ{(∥)e(∥  §)

where ˆ{(∥) are the Fourier coeﬃcients

ˆ{(∥) := Z

T d
{(§ )e( ∥  §) d§

and m R is the Fourier multiplier

m R (∥1∅ : : : ∅ ∥d) :=
 dY

j /1
  1   j∥j j
R
 
 +:

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

14 1. Higher order Fourier analysis

Standard Fourier analysis shows that we have the convolution representation

FR{(§ ) = Z

T d {(y )K R(§   y )

where K R is the Fej´er kernel

K R(§ 1∅ : : : ∅ §d ) :=
 dY

| /1
 1
R
  sin(≈R§| )
sin(≈§| )
  2 :

Using the kernel bounds Z

T d K R = 1

and
 jKR(§)j ˝ d
 dY

| /1 R(1 + Rk§| kT )
(2 ∅

where k§kT is the distance from § to the nearest integer, and the Lipschitz
nature of {, we see that
 FR{(§) = {(§) + Od (1=R):

Thus, if we choose R to be a suﬃciently small multiple of 1=◦ (depending
on d), one has jE\2[N ]FR{(§ \ )j ˛ ◦

and thus by the pigeonhole principle (and the trivial bound ˆ{(∥) = O(1)
and ˆ{(0) = 0) we have
 jE\2[N ]e(∥  § \ )j ˛d ◦
Od (1)

for some non-zero ∥ of magnitude j∥j ˝ d ◦(O d (1), and the claim follows. 

There is an analogue for total equidistribution:

Exercise 1.1.18.Let § 1∅ §2∅ : : : ∅ §N be a sequence in Td , and let 0 < ◦ < 1.

(i) If § 1∅ : : : ∅ §N is totally ◦-equidistributed, ∥ 2 Zd nf0g has magnitude
j∥j  ◦(⌋ d , and a is a rational of height at most ◦(⌋ d , then one has

jE\2[N ]e(∥  § \ )e(a\)j ˝ d ◦
⌋d

if ⌋d > 0 is a small enough constant depending only on d.

(ii) Conversely, if § 1∅ : : : ∅ §N is \ot totally ◦-equidistributed, then there
exists ∥ 2 Zd nf0g with magnitude j∥j ˝ d ◦(C d , and a rational a of
height Od (◦(C d ), such that

jE\2[N ]e(∥  § \ )e(a\)j ˛d ◦
C d

for some C d depending on d.

This gives a version of Exercise 1.1.5:

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.1. Equidistribution in tori 15

E§er⌋⟩se ∞.∞.∞9.Let ∅ 2 T d, let N  1, and let 0 < ◦ < 1. Suppose that
the linear sequence (\ + )N
n=1 is not totally ◦-equidistributed. Show that
there exists a non-zero ∥ 2 Zd with j∥j ˝ d ◦ O d (1) such that k∥ ∆kT ˝ d
◦ O d (1)=N.

Next, we give an analogue of Corollary 1.1.7:

E§er⌋⟩se ∞.∞.∈0(Single-scale van der Corput lemma).Let § 1∅ §2∅ : : : ∅ §N 2
T d be a sequence which is not totally ◦-equidistributed for some 0 < ◦ ˇ 1=2.
Let 1 ˇ H ˇ ◦ C d N for some suﬃciently large C d depending only on d.
Then there exists at least ◦Cd H integers ⟨ 2 [ΓH∅ H] such that the sequence
(§ n+h Γ § n)N
n=1 is not totally ◦Cd -equidistributed (where we extend § n by
zero outside of f1∅ : : : ∅ Ng). (Hint:apply Lemma 1.1.6.)

Just as in the asymptotic setting, we can use the van der Corput lemma
to extend the linear equidistribution theory to polynomial sequences. To
get satisfactory results, though, we will need an additional input, namely
the following classical lemma, essentially due to Vinogradov:

Lemma ∞.∞.∞4.Let 2 T, 0 < " < 1=100,100" < ◦ < 1, andN  100=◦.
Suppose thatk\kT ˇ " for at least◦N values of \ 2 [ΓN∅ N]. Then there
exists a positive integerq= O(1=◦) such thatkqkT ˝ εq
δN .

The key point here is that one starts with many multiples of  being
somewhat close (O(")) to an integer, but concludes that there is a single
multiple of  which is very close (O("=N), ignoring factors of ◦) to an
integer.

Proo{.By the pigeonhole principle, we can ﬁnd two distinct integers \∅ \0 2
[ΓN∅ N] with j\ Γ \ 0j ˝ 1=◦ such that k\kT∅k\0kT ˇ ". Setting q :=
j\0Γ \j, we thus have kqkT ˇ 2". We may assume that q6= 0 since we
are done otherwise. Since N  100=◦, we have N=q 10 (say).

Now partition [ΓN∅ N] into qarithmetic progressions f\q + r: ΓN=q+
O(1) ˇ \ ˇ N=q+ O(1)g for some r = 0∅ : : : ∅ qΓ 1. By the pigeonhole
principle, there must exist an rfor which the set

fΓN=q+ O(1) ˇ \ ˇ N=q+ O(1) : k(\q+ r)kT ˇ "g

has cardinality at least ◦N=q. On the other hand, since kqkT ˇ 2" ˇ
0:02, we see that this set consists of intervals of length at most 2"=kqkT,
punctuated by gaps of length at least 0:9=kqkT (say). Since the gaps are
at least 0:45="times as large as the intervals, we see that if two or more
these intervals appear in the set, then the cardinality of the set is at most
100"N=q < ◦N=q, a contradiction. Thus at most one interval appears in the
set, which implies that 2"=kqkT  ◦N=q, and the claim follows. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

16 1. Higher order Fourier analysis

Remar∥ ∞.∞.∞5.The numerical constants can of course be improved, but
this is not our focus here.

E§er⌋⟩se ∞.∞.∈∞.Let P : Z ! T d be a polynomial sequence P(\) := s\ s+
∆ ∆ ∆+0, let N  1, and let 0 < ◦ < 1. Suppose that the polynomial sequence
P is not totally ◦-equidistributed on [N]. Show that there exists a non-zero
∥ 2 Zd with j∥j ˝ d,s ◦ O d,s (1) such that k∥ ∆skT ˝ d,s ◦ O d,s (1)=Ns. (Hint:
Induct on s starting with Exercise 1.1.19 for the base case, and then using
Exercise 1.1.20 and Lemma 1.1.14 to continue the induction.)

Note the N s denominator; the higher-degree coeﬃcients of a polynomial
need to be very rational in order not to cause equidistribution.

The above exercise only controls the top degree coeﬃcient, but we can
in fact control all coeﬃcients this way:

Lemma ∞.∞.∞̸.With the hypotheses of Exercise 1.1.21, we can in fact
nd a non-zero∥ 2 Zd with j∥j ˝ d,s ◦ O d,s (1) such thatk∥ ∆ikT ˝ d,s
◦ O d,s (1)=Ni for all⟩ = 0∅ : : : ∅ s.

Proo{.We shall just establish the one-dimensional case d = 1, as the general
dimensional case then follows from Exercise 1.1.18.

The case s ˇ 1 follows from Exercise 1.1.19, so assume inductively that
s > 1 and that the claim has already been proven for smaller values of
s. We allow all implied constants to depend on s. From Exercise 1.1.21,
we already can ﬁnd a positive ∥ with ∥ = O(◦ O (1)) such that k∥skT ˝
◦ O (1)=Ns. We now partition [N] into arithmetic progressions of spacing ∥
and length N 0 ˘ ◦CN for some suﬃciently large C ; then by the pigeonhole
principle, we see that P fails to be totally ˛ ◦O(1)-equidistributed on one
of these progressions. But on one such progression (which can be identiﬁed
with [N 0]) the degree s component of P is essentially constant (up to errors
much smaller than ◦) if C is large enough; if one then applies the induction
hypothesis to the remaining portion of P on this progression, we can obtain
the claim. 

This gives us the following analogue of Exercise 1.1.7. We say that a
subtorus T of some dimension d 0 of a standard torus T d has complexity
at most M if there exists an invertible linear transformation L 2 SLd(Z)
with integer coeﬃcients (which can thus be viewed as a homeomorphism
of T d that maps T to the standard torus T d′  f0g d d ′ ), and such that all
coeﬃcients have magnitude at most M.

E§er⌋⟩se ∞.∞.∈∈.Show that every subtorus (i.e. compact connected Lie
subgroup) T of T d has ﬁnite complexity. (Hint:Let V be the Lie algebra
of T , then identify V with a subspace of Rd and T with V =(V “ Zd). Show

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.1. Equidistribution in tori 17

that V ∩ Zd is a full rank sublattice of V , and is thus generated by dim(V )
independent generators.)

Proposition 1.1.17 (Single-scale equidistribution theorem for abelian poly-
nomial sequences). Let P be a polynomial map from Z to Td of some degree
s ≥ 0, and let F : R + → R + be an increasing function. Then there exists
an integer 1 ≤ M ≤ OF,s,d(1) and a decomposition

P = Psmth + Pequi + Prat

into polynomials of degree s, where

(i) (Psmth is smooth) The ⟩th coeﬃcient i,smth of Psmth has size O(M=Ni).
In particular, on the interval [N], Psmth is Lipschitz with homoge-
neous norm Os,d(M=N).

(ii) (Pequi is equidistributed) There exists a subtorus T of Td of com-
plexity at most M and some dimension d 0, such that Pequi takes
values in T and is totally 1=F(M)-equidistributed on [N] in this
torus (after identifying this torus with Td using an invertible lin-
ear transformation of complexity at most M).

(iii) (Prat is rational) The coeﬃcients i,rat of Prat are such that qi,rat =
0 for some 1 ≤ q≤ M and all 0 ≤ ⟩ ≤ s. In particular, qPrat = 0
and Prat is periodic with period q.

If furthermore F is of polynomial growth, and more precisely F(M) ≤ KMA

for some A∅ K ≥ 1, then one can take M ≪A,s,d K OA,s,d(1).

Example 1.1.18. Consider the linear ﬂow P(\) := (√2\∅( 1
2+ 1
N )\) mod Z2

in T2 on [N]. This ﬂow can be decomposed into a smooth ﬂow Psmth(\) :=
(0∅ 1
N \) mod Z2 with a homogeneous Lipschitz norm of O(1=N), an equidis-
tributed ﬂow Pequi(\) := ( √2\∅0) mod Z2 which will be ◦-equidistributed
on the subtorus T1 × {0} for a reasonably small ◦ (in fact one can take ◦ as
small as N  c for some small absolute constant ⌋ > 0), and a rational ﬂow
Prat(\) := (0 ∅1
2\) mod Z2, which is periodic with period 2. This example
illustrates how all three components of this decomposition arise naturally in
the single-scale case.

Remark 1.1.19. Comparing this result with the asymptotically equidis-
tributed analogue in Example 1.1.7, we notice several diﬀerences. Firstly,
we now have the smooth component Psmth, which did not previously make
an appearance (except implicitly, as the constant term in P 0). Secondly,
the equidistribution of the component Pequi is not inﬁnite, but is the next
best thing, namely it is given by an arbitrary function F of the quantity M,
which controls the other components of the decomposition.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

18 1. Higher order Fourier analysis

Proo{.The case s = 0 is trivial, so suppose inductively that s  1, and that
the claim has already been proven for lower degrees. Then for ﬁxed degree,
the case d = 0 is vacuously true, so we make a further inductive assumption
d  1 and the claim has already been proven for smaller dimensions (keeping
s ﬁxed).

If P is already totally 1=F(1)-equidistributed then we are done (setting
Pequi = P and Psmth = Prat = 0 and M = 1), so suppose that this is not
the case. Applying Exercise 1.1.21, we conclude that there is some non-zero
∥ 2 Zd with j∥j ˝ d;s F(1)Od;s (1)such that

k∥ ∆ikT ˝ d;s F(1)
Od;s (1)=N
i

for all ⟩ = 0∅ : : : ∅ s. We split ∥ = m∥ where ∥is irreducible and m is a posi-
tive integer. We can therefore split i = i;smth + i;rat + 
i where i;smth =
O(F(1)Od;s (1)=Ni), qi = 0 for some positive integer q= Od;s (F(1)Od;s (1)),
and ∥∆
i = 0. This then gives a decomposition P = Psmth + P + Prat,
with P taking values in the subtorus f§ 2 T d : ∥∆§ = 0g, which can be
identiﬁed with T d(1 after an invertible linear transformation with integer
coeﬃcients of size Od;s (F(1)Od;s (1)). If one applies the induction hypothesis
to P (with F replaced by a suitably larger function F) one then obtains
the claim.

The ﬁnal claim about polynomial bounds can be veriﬁed by a closer
inspection of the argument (noting that all intermediate steps are polyno-
mially quantitative, and that the length of the induction is bounded by
Od;s (1)). 

Remar∥ ∞.∞.∈0.It is instructive to see how this smooth-equidistributed-
rational decomposition evolves as N increases. Roughly speaking, the torus
T that the Pequi component is equidistributed on is stable at most scales,
but there will be a ﬁnite number of times in which a “growth spurt” oc-
curs and T jumps up in dimension. For instance, consider the linear ﬂow
P(\) := ( \=N0∅ \=N2
0 ) mod Z2 on the two-dimensional torus. At scales
N ˝ N0 (and with F ﬁxed, and N0 assumed to be suﬃciently large de-
pending on F), P consists entirely of the smooth component. But as N
increases past N0, the ﬁrst component of P no longer qualiﬁes as smooth,
and becomes equidistributed instead; thus in the range N0 ˝ N ˝ N 2
0 , we
have Psmth(\) = (0∅ \=N2
0 ) mod Z2 and Pequi(\) = (\=N0∅0) mod Z2 (with
Prat remaining trivial), with the torus T increasing from the trivial torus
f0g 2 to T 1  f0g. A second transition occurs when N exceeds N 2
0 , at which
point Pequi encompasses all of P. Evolving things in a somewhat diﬀerent
direction, if one then increases F so that F(1) is much larger than N 2
0 , then
P will now entirely consist of a rational component Prat. These sorts of
dynamics are not directly seen if one only looks at the asymptotic theory,

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.1. Equidistribution in tori 19

which roughly speaking is concerned with the limit after taking N → ∞, and
then taking a second limit by making the growth function F go to inﬁnity.

There is a multidimensional version of Proposition 1.1.17, but we will
not describe it here; see [GrTa2011] for a statement (and also see the next
section for the ultralimit counterpart of this statement).

Remark 1.1.21. These single-scale abelian equidistribution theorems are a
special case of a more general single-scale nilpotentequidistribution theorem,
which will play an important role in later aspects of the theory, and which
was the main result of the aforementioned paper of Ben Green and myself.

As an example of this theorem in action, we give a single-scale strength-
ening of Exercise 1.1.8 (and Exercise 1.1.15):

Exercise 1.1.23 (Recurrence). Let P be a polynomial map from Z to T d

of degree s, and let N ≥ 1 be an integer. Show that for every " > 0 and
N > 1, and every integer \ 0 ∈ [N], we have

|{\ ∈ [N] : ∥P(\) − P(\ 0)∥ ≤ "}| ≫d;s "
Od,s (1)N:

Exercise 1.1.24(Multiple recurrence). With the notation of Exercise 1.1.23,
establish that

|{r∈[−N∅ N] : ∥P(\ 0 + |r) − P(\ 0)∥ ≤ " for | = 0∅1∅ : : : ∅ ∥− 1}|

≫d;s;k "
Od,s,k (1)N

for any ∥ ≥ 1.

Exercise 1.1.25(Syndeticity). A set of integers is syndeticif it has bounded
gaps (or equivalently, if a ﬁnite number of translates of this set can cover
all of Z). Let P : Z → T d be a polynomial and let " > 0. Show that
the set {\ ∈ Z: ∥P(\) − P(\ 0)∥ ≤ "} is syndetic. (Hint: ﬁrst reduce to
the case when P is (totally) asymptotically equidistributed. Then, if N is
large enough, show (by inspection of the proof of Exercise 1.1.21) that the
translates P(· + \ 0) are "-equidistributed on [N] uniformly for all \ ∈ Z,
for any ﬁxed " > 0. Note how the asymptotic theory and the single-scale
theory need to work together to obtain this result.)

1.1.3. Ultralimit equidistribution theory. The single-scale theory was
somewhat more complicated than the asymptotic theory, in part because
one had to juggle parameters such as N∅ ◦, and (for the equidistribution
theorems) F as well. However, one can clean up this theory somewhat
(especially if one does not wish to quantify the dependence of bounds on
the equidistribution parameter ◦) by using an ultralimit, which causes the ◦

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

20 1. Higher order Fourier analysis

and F parameters to disappear, at the cost of converting the ﬁnitary theory
to an inﬁnitary one. Ultralimit analysis is discussed in Section 2.1; we give
a quick review here.

We ﬁrst ﬁx a \o\-√r⟩\⌋⟩√al ultralter1 2 NnN (see Section 2.1 for a
deﬁnition of a non-principal ultraﬁlter). A property P pertaining to a natu-
ral number  is said to hold {or all su◦⌋⟩e\tly ⌋lose to 1 if the set of  for
which P holds lies in the ultraﬁlter 1 . Two sequences (§  )2N ∅(y  )2N
of objects are equ⟩vale\tif one has §  = y  for all  suﬃciently close to
1 , and we deﬁne the ultral⟩m⟩tlim!   §  to be the equivalence class of
all sequences equivalent to (§  )2N , with the convention that § is identiﬁed
with its own ultralimit lim!   §  . Given any sequence X  of sets, the
ultra√rodu⌋t
Q
!  X  is the space of all ultralimits lim!   §  , where
§  2 X  for all  suﬃciently close to 1 . The ultraproduct Q
!  X of
a single set X is the ultra√owerof X and is denoted X .

Ultralimits of real numbers (i.e. elements of R ) will be called l⟩m⟩t real
\um⌊ers; similarly one deﬁnes limit natural numbers, limit complex num-
bers, etc. Ordinary numbers will be called sta\dardnumbers to distinguish
them from limit numbers, thus for instance a limit real number is an ul-
tralimit of standard real numbers. All the usual arithmetic operations and
relations on standard numbers are inherited by their limit analogues; for in-
stance, a limit real number lim!   §  is larger than another lim!  y
if one has §  > y  for all  suﬃciently close to 1 . The axioms of a
non-principal ultraﬁlter ensure that these relations and operations on limit
numbers obey the same axioms as their standard counterparts
3.

Ultraproducts of sets will be called l⟩m⟩t sets; they are roughly analogous
to “elementary sets” in measure theory. Ultraproducts of ﬁnite sets will be
called l⟩m⟩t \⟩te sets. Thus, for instance, ifN = lim!   N is a limit
natural number, then [N] = Q
!  [N ] is a limit ﬁnite set, and can be
identiﬁed with the set of limit natural numbers between 1 and N.

Remark 1.1.22. In the language of \o\sta\dard a\alys⟩s, limit numbers
and limit sets are known as \o\sta\dard \um⌊ersand ⟩\ter\al setsrespec-
tively. We will however use the language of ultralimit analysis rather than
nonstandard analysis in order to emphasise the fact that limit objects are
the ultralimits of standard objects; see Section 2.1 for further discussion of
this perspective.

3The formalisation of this principle is  Los's t⟨eorem, which roughly speaking asserts that
any rst-order sentence which is true for standard objects, is also true for their limit counterparts.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.1. Equidistribution in tori 21

Given a sequence of functions {: X  ! Y, we can form the ultralimit
lim! 1 {: lim! 1 X  ! lim! 1 Y by the formula

( lim
! 1 {) θ lim
! 1 §

 := lim
! 1 {(§ );

one easily veriﬁes that this is a well-deﬁned function between the two ultra-
products. We refer to ultralimits of functions as limit functions; they are
roughly analogous to “simple functions” in measurable theory. We identify
every standard function { : X ! Y with its ultralimit lim! 1 { :  X !  Y ,
which extends the original function {.

Now we introduce limit asymptotic notation, which is deliberately chosen
to be similar (though not identical) to ordinary asymptotic notation. Given
two limit numbers X∅ Y, we write X ˝ Y , Y ˛ X , or X = O(Y ) if we
have jX j ˇ CY for some standard C > 0. We also write X = o(Y ) if we
have jX j ˇ ⌋Y for every standard ⌋ > 0; thus for any limit numbers X∅ Y
with Y > 0, exactly one of jX j ˛ Y and X = o(Y ) is true. A limit real
is said to be bounded if it is of the form O(1), and inβnitesimalif it is of
the form o(1); similarly for limit complex numbers. Note that the bounded
limit reals are a subring of the limit reals, and the inﬁnitesimal limit reals
are an ideal of the bounded limit reals.

Exer̂ise ..26(Relation between limit asymptotic notation and ordinary
asymptotic notation).Let X = lim! 1 X  and Y = lim! 1 Y be two
limit numbers.

(i) Show that X ˝ Y if and only if there exists a standard C > 0 such
that jXj ˇ CY  for all  suﬃciently close to 0.

(ii) Show that X = o(Y ) if and only if, for every standard " > 0, one
has jXj ˇ "Y for all  suﬃciently close to 0.

Exer̂ise ..27.Show that every bounded limit real number § has a
unique decomposition § = st(§) + ( § Γ st(§)), where st(§ ) is a standard
real (called the standard partof § ) and § Γ st(§) is inﬁnitesimal.

We now give the analogue of single-scale equidistribution in the ultra-
limit setting.

De∣nition ..23(Ultralimit equidistribution).Let X = (X∅ d) be a stan-
dard compact metric space, let N be an unbounded limit natural number,
and let § : [N] !  X be a limit function. We say that § is equidistributed
with respect to a (standard) Borel probability measure  on X if one has

stE \2[N ]{(§(\)) = Z

X { d

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

22 1. Higher order Fourier analysis

for all standard continuous functions { ∈ C (X ). Here, we deﬁne the expec-
tation of a limit function in the obvious limit manner, thus

En2[N ]{(§(\)) = lim
α! α1 En2[N  ]{(§ α(\))

if N = limα! α1 Nα and § = limα! α1 § α.

We say that § is totally equidistributedrelative to  if the sequence
\ ↦→ §(q\ + r) is equidistributed on [N=q] for every standard q > 0 and
r∈ Z (extending § arbitrarily outside [N] if necessary).

Remark 1.1.24. One could just as easily replace the space of continuous
functions by any dense subclass in the uniform topology, such as the space
of Lipschitz functions.

The ultralimit notion of equidistribution is closely related to that of
both asymptotic equidistribution and single-scale equidistribution, as the
following exercises indicate:

Exercise 1.1.28 (Asymptotic equidistribution vs. ultralimit equidistribu-
tion). Let § : N → X be a sequence into a standard compact metric space
(which can then be extended from a map from  N to  X as usual), let  be
a Borel probability measure on X . Show that § is asymptotically equidis-
tributed on N with respect to  if and only if § is equidistributed on [N]
for every unbounded natural number N and every choice of non-principal
ultraﬁlter 1 .

Exercise 1.1.29 (Single-scale equidistribution vs. ultralimit equidistribu-
tion). For every  ∈ N, let Nα be a natural number that goes to inﬁnity as
 → ∞, let § α : [Nα] → X be a map to a standard compact metric space.
Let  be a Borel probability measure on X . Write N := limα!α 1 Nα and
§ := limα! α1 § α for the ultralimits. Show that § is equidistributed with
respect to  if and only if, for every standard ◦ > 0, § α is ◦-equidistributed
with respect to  for all  suﬃciently close to 1 .

In view of these correspondences, it is thus not surprising that one has
ultralimit analogues of the asymptotic and single-scale theory. These ana-
logues tend to be logically equivalentto the single-scale counterparts (once
one concedes all quantitative bounds), but are formally similar(though not
identical) to the asymptotic counterparts, thus providing a bridge between
the two theories, which we can summarise by the following three statements:

(i) Asymptotic theory is analogous to ultralimit theory (in particular,
the statements and proofs are formally similar);

(ii) ultralimit theory is logically equivalent to qualitative ﬁnitary the-
ory; and

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.1. Equidistribution in tori 23

(iii) quantitative ﬁnitary theory is a strengthening of qualitative ﬁnitary
theory.

For instance, here is the ultralimit version of the Weyl criterion:

E§er⌋⟩se ∞.∞.30(Ultralimit Weyl equidistribution criterion).Let § : [N] !
Td be a limit function for some unbounded N and standard d. Then § is
equidistributed if and only if

(1.7) E n2[N ]e(∥ ∆§(\)) = o(1)

for all standard ∥ 2 Zdnf0g. Hint. mimic the proof of Proposition 1.1.2.

E§er⌋⟩se ∞.∞.3∞.Use Exercise 1.1.30 to recover a weak version of Propo-
sition 1.1.13, in which the quantities ◦cd, ◦Cdare replaced by (ineﬀective)
functions of ◦ that decay to zero as ◦ ! 0. Conversely, use this weak version
to recover Exercise 1.1.30. (Hint. Similar arguments appear in Section 2.1.)

E§er⌋⟩se ∞.∞.3∈.With the notation of Exercise 1.1.30, show that § is to-
tally equidistributed if and only if

E n2[N ]e(∥ ∆§(\))e(⊆\) = o(1)

for all standard ∥ 2 Zdnf0g and standard rational ⊆.

E§er⌋⟩se ∞.∞.33.With the notation of Exercise 1.1.30, show that § is
equidistributed in T d on [N] if and only if ∥ ∆§ is equidistributed in T
on [N] for every non-zero standard ∥ 2 Zd.

Now we establish the ultralimit version of the linear equidistribution
criterion:

E§er⌋⟩se ∞.∞.34.Let ∅ 2 T d, and let N be an unbounded integer.
Show that the following are equivalent:

(i) The sequence \ 7! \ +  is equidistributed on [N].

(ii) The sequence \ 7! \ +  is totally equidistributed on [N].

(iii)  is irrational to scale1=N, in the sense that ∥ ∆ 6=O(1=N) for
any non-zero standard ∥ 2 Zd.

Note that in the ultralimit setting, assertions such as ∥ ∆ 6=O(1=N)
make perfectly rigorous sense (it means that j∥∆j  C=N for every standard
C ), but when using ﬁnitary asymptotic big-O notation

Next, we establish the analogue of the van der Corput lemma:

E§er⌋⟩se ∞.∞.35(van der Corput lemma, ultralimit version).Let N be an
unbounded integer, and let § : [N] ! T d be a limit sequence. Let H = o(N )
be unbounded, and suppose that the derivative sequence @h§ : \ 7! §(\ +

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

24 1. Higher order Fourier analysis

⟨) − §(\) is equidistributed on [ N] for ≫ H values of ⟨ ∈ [H] (extending
§ by arbitrarily outside of [N]). Show that § is equidistributed on [N].
Similarly “equidistributed” replaced by “totally equidistributed”.

Here is the analogue of the Vinogradov lemma:

Exercise 1.1.36 (Vinogradov lemma, ultralimit version). Let  ∈ ∗T, N
be unbounded, and " > 0 be inﬁnitesimal. Suppose that ∥\∥T ≤ " for
≫ N values of \ ∈ [−N∅ N]. Show that there exists a positive standard
integer qsuch that ∥q∥T ≪ "=N.

These two lemmas allow us to establish the ultralimit polynomial equidis-
tribution theory:

Exercise 1.1.37. Let P : ∗ Z → ∗Td be a polynomial sequence P(\) :=
s \ s + · · · + 0 with s∅ d standard, and 0∅ : : : ∅ s ∈ ∗Td. Let N be an
unbounded natural number. Suppose that P is not totally equidistributed
on [N]. Show that there exists a non-zero standard ∥ ∈ Zd with ∥∥ · s ∥T ≪
N  s .

Exercise 1.1.38. With the hypotheses of Exercise 1.1.37, show in fact that
there exists a non-zero standard ∥ ∈ Zd such that ∥∥ · i∥T ≪ N  i for all
⟩ = 0∅ : : : ∅ s.

Exercise 1.1.39 (Ultralimit equidistribution theorem for abelian polyno-
mial sequences). Let P be a polynomial map from ∗Z to ∗Td of some stan-
dard degree s ≥ 0. Let N be an unbounded natural number. Then there
exists a decomposition
 P = Psmth + Pequi + Prat

into polynomials of degree s, where

(i) (Psmth is smooth) The ⟩th coeﬃcient i;smth of Psmth has size O(N  i ).
In particular, on the interval [N], Psmth is Lipschitz with homoge-
neous norm O(1=N).

(ii) (Pequi is equidistributed) There exists a standard subtorus T of Td,
such that Pequi takes values in T and is totally equidistributed on
[N] in this torus.

(iii) (Prat is rational) The coeﬃcients i;rat of Prat are standard rational
elements of Td. In particular, there is a standard positive integer
qsuch that qPrat = 0 and Prat is periodic with period q.

Exercise 1.1.40. Show that the torus T is uniquely determined by P, and
decomposition P = Psmth + Pequi + Prat in Exercise 1.1.39 is unique up to
expressions taking values in T (i.e. if one is given another decomposition

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.1. Equidistribution in tori 25

P = P 0
smth + P 0
equi∅ P0
rat, then Pi and P 0
i diﬀer by expressions taking values
in T ).

Exercise 1.1.41 (Recurrence). Let P be a polynomial map from Z to T d

of some standard degree s, and let N be an unbounded natural number.
Show that for every standard " > 0 and every \ 0 2 N, we have

jf\ 2 [N] : kP(\)   P(\ 0)k  "gj ˛N

and more generally

jfr2 [ N∅ N ] : kP(\ 0 + |r)   P(\ 0)k  " for | = 0∅1∅ : : : ∅ ∥  1gj ˛N

for any standard ∥.

As before, there are also multidimensional analogues of this theory. We
shall just state the main results without proof:

Deﬁnition 1.1.25 (Multidimensional equidistribution). Let X be a stan-
dard compact metric space, let N be an unbounded limit natural number,
let m  1 be standard, and let § : [N]m ! X be a limit function. We
say that § is equidistributedwith respect to a (standard) Borel probability
measure  on X if one has

stE n∈[N ]m 1B(\=N){(§(\)) = mes(Ω) Z

X { d

for every standard box B ˆ [0∅1]m and for all standard continuous functions
{ 2 C (X ).

We say that § is totally equidistributedrelative to  if the sequence
\ 7! §(q\ + r) is equidistributed on [N=q]d for every standard q >0 and
r2 Z m (extending § arbitrarily outside [N] if necessary).

Remark 1.1.26. One can replace the indicators 1B by many other classes,
such as indicators of standard convex sets, or standard open sets whose
boundary has measure zero, or continuous or Lipschitz functions.

Theorem 1.1.27 (Multidimensional ultralimit equidistribution theorem for
abelian polynomial sequences). Let m∅ d∅ s  0 be standard integers, and let
P be a polynomial map fromZ m to T d of degrees. LetN be an unbounded
natural number. Then there exists a decomposition

P = Psmth + Pequi + Prat

into polynomials of degrees, where

(i) (Psmth is smooth) The⟩th coeδcient i,smth ofPsmth has sizeO(N −|i| )
for every multi-index⟩ = (⟩1∅ : : : ∅ ⟩m). In particular, on the interval
[N], Psmth is Lipschitz with homogeneous normO(1=N).

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

26 1. Higher order Fourier analysis

(ii) (Pequi ⟩s equ⟩d⟩str⟩⌊uted) T⟨ere e§⟩sts a sta\dard su⌊torusT o{ T d,
su⌋⟨ t⟨atPequi ta∥es values ⟩\T a\d ⟩s totally equ⟩d⟩str⟩⌊uted o\
[N]m ⟩\ t⟨⟩s torus.

(iii) (Prat ⟩s rat⟩o\al) T⟨e ⌋oe◦⌋⟩e\tsi;rat o{ Prat are sta\dard rat⟩o\al
eleme\ts o{ T d. I\ √art⟩⌋ular, t⟨ere ⟩s a sta\dard √os⟩t⟩ve ⟩\te}er
qsu⌋⟨ t⟨atqPrat = 0 a\d Prat ⟩s √er⟩od⟩⌋ w⟩t⟨ √er⟩odq.

Proof. This is implicitly in [GrTa2011]; the result is phrased using the
language of single-scale equidistribution, but this easily implies the ultralimit
version. 

1.2. Roth's theorem

We now give a basic application of Fourier analysis to the problem of count-
ing additive patterns in sets, namely the following famous theorem of Roth
[Ro1953 ]:

Theorem 1.2.1 (Roth’s theorem). LetA ⌊e a su⌊set o{ t⟨e ⟩\te}ersZ w⟨ose
u√√er de\s⟩ty
 ◦(A) := lim sup
N )
 jA\ [ N∅ N ]j
2N + 1
⟩s √os⟩t⟩ve. T⟨e\A ⌋o\ta⟩\s ⟩\\⟩tely ma\y ar⟩t⟨met⟩⌋ √ro}ress⟩o\sa∅ a+
r∅ a+ 2ro{ le\}t⟨ t⟨ree, w⟩t⟨a 2 Z a\d r >0.

This is the ﬁrst non-trivial case of Szemered⟩'s t⟨eorem[Sz1975], which
is the same assertion but with length three arithmetic progressions replaced
by progressions of length ∥ for any ∥.

As it turns out, one can prove Roth’s theorem by an application of linear
Fourier analysis - by comparing the set A (or more precisely, the indicator
function 1A of that set, or of pieces of that set) against linear characters
\ 7ωe(\) for various frequencies  2 R=Z. There are two extreme cases to
consider (which are model examples of a more general dichotomy between
structure and randomness, as discussed in [Ta2008]). One is when A is
aligned up almost completely with one of these linear characters, for instance
by being a Bo⟨r setof the form

f\ 2 Z : k\  ⊆kR=Z < "g

or more generally of the form

f\ 2 Z : \ 2 U g

for some multi-dimensional frequency  2 T d and some open set U . In
this case, arithmetic progressions can be located using the equidistribution
theory from Section 1.1. At the other extreme, one has Four⟩er-u\⟩{ormor
Four⟩er-√seudora\dom sets, whose correlation with any linear character is

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.2. Roth’s theorem 27

negligible. In this case, arithmetic progressions can be produced in abun-
dance via a Fourier-analytic calculation.

To handle the general case, one must somehow synthesise together the
argument that deals with the structured case with the argument that deals
with the random case. There are several known ways to do this, but they
can be basically classiﬁed into two general methods, namely the de\s⟩ty
⟩\⌋reme\t ar}ume\t(or L1 increment argument) and the e\er}y ⟩\⌋reme\t
ar}ume\t(or L2 increment argument).

The idea behind the density increment argument is to introduce a di-
chotomy: either the object A being studied is pseudorandom (in which case
one is done), or else one can use the theory of the structured objects to lo-
cate a sub-object of signiﬁcantly higher “density” than the original object.
As the density cannot exceed one, one should thus be done after a ﬁnite
number of iterations of this dichotomy. This argument was introduced by
Roth in his original proof [Ro1953 ] of the above theorem.

The idea behind the energy increment argument is instead to decompose
the original object A into two pieces (and, sometimes, a small additional er-
ror term): a stru⌋tured ⌋om√o\e\tthat captures all the structured objects
that have signiﬁcant correlation with A, and a √seudora\dom ⌋om√o\e\t
which has no signiﬁcant correlation with any structured object. This de-
composition usually proceeds by trying to maximise the “energy” (or L2

norm) of the structured component, or dually by trying to minimise the en-
ergy of the residual between the original object and the structured object.
This argument appears for instance in the proof of the Szemered⟩ re}ular-
⟩ty lemma [Sz1978] (which, not coincidentally, can also be used to prove
Roth’s theorem), and is also implicit in the ergodic theory approach to such
problems (through the machinery of conditional expectation relative to a
factor, which is a type of orthogonal projection, the existence of which is
usually established via an energy increment argument). However, one can
also deploy the energy increment argument in the Fourier analytic setting,
to give an alternate Fourier-analytic proof of Roth’s theorem that diﬀers in
some ways from the density increment proof.

In this section we give both two Fourier-analytic proofs of Roth’s theo-
rem, one proceeding via the density increment argument, and the other by
the energy increment argument. As it turns out, both of these arguments
extend to establish Szemer´edi’s theorem, and more generally in counting
other types of patterns, but this is non-trivial (requiring some sort of ⟩\-
verse ⌋o\|e⌋turefor the Gowers uniformity norms in both cases); we will
discuss this further in later sections.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

28 1. Higher order Fourier analysis

∞.∈.∞. T⟨e de\s⟩ty ⟩\⌋reme\t ar}ume\t.We begin with the density
increment argument. We ﬁrst rephrase Roth’s theorem in a ﬁnitary form:

T⟨eorem ∞.∈.∈(Roth’s theorem, again).For everyﬃ > 0, t⟨ere e§⟩sts a\
N0 = N0(ﬃ) > 0, su⌋⟨ t⟨at {or everyN  N0, a\d everyA ˆ [N ] w⟩t⟨
jAj  ﬃN,A ⌋o\ta⟩\s a\ ar⟩t⟨met⟩⌋ √ro}ress⟩o\ o{ le\}t⟨ t⟨ree.

E§er⌋⟩se ∞.∈.∞.Show that Theorem 1.2.1 and Theorem 1.2.2 are equiva-
lent.

We prove Theorem 1.2.2 by a downward induction on the density pa-
rameter ﬃ. Let P(ﬃ) denote the proposition that Theorem 1.2.2 holds for
that value of ﬃ(i.e. for suﬃciently large N and all A ˆ [N ] with jAj  ﬃN,
A contains an arithmetic progression of length three). Our objective is to
show that P(ﬃ) holds for all ﬃ > 0.

Clearly, P(ﬃ) is (vacuously) true for ﬃ > 1 (and trivially true for ﬃ 1).
It is also monotone in the sense that if P(ﬃ) holds for some ﬃ, then P(ﬃ0)
holds for all ﬃ0 > ﬃ. To downwardly induct on ﬃ, we will prove the following
dichotomy:

Pro√os⟩t⟩o\ ∞.∈.3(Lack of progressions implies density increment).Let
ﬃ > 0, letN ⌊e su◦⌋⟩e\tly lar}e de√e\d⟩\} o\ﬃ, a\d letA ˆ [N ] ⌊e su⌋⟨
t⟨atjAj  ﬃN. T⟨e\ o\e o{ t⟨e {ollow⟩\} ⟨olds:

(i) A ⌋o\ta⟩\s a\ ar⟩t⟨met⟩⌋ √ro}ress⟩o\ o{ le\}t⟨ t⟨ree∅ or

(ii) t⟨ere e§⟩sts a su⌊√ro}ress⟩o\P o{ [N ] o{ le\}t⟨ at leastN 0 su⌋⟨
t⟨atjA \ Pj  (ﬃ+ c(ﬃ))jPj, w⟨ereN 0 = N 0(N ) }oes to ⟩\\⟩ty as
N ! 1, a\d c(ﬃ) > 0 ⟩s ⌊ou\ded away {rom zero w⟨e\ever ﬃ⟩s
⌊ou\ded away {rom zero.

Let us see why Proposition 1.2.3 implies Theorem 1.2.2. It is slightly
more convenient to use a “well-ordering principle” argument rather than an
induction argument, though unsurprisingly the two approaches turn out to
be equivalent. Let ﬃ be the inﬁmum of all ﬃfor which P(ﬃ) holds, thus
0 ˇ ﬃ ˇ 1. If ﬃ = 0 then we are done, so suppose that ﬃ is non-zero.
Then for any ” > 0, P(ﬃ   ”) is false, thus there exist arbitrarily large N
and A ˆ [N ] with jAj  (ﬃ   ”)N with no progressions of length three. By
Proposition 1.2.3, we can thus ﬁnd a subprogression P of N of length at
least N 0 with jA \ Pj  (ﬃ   ” + c(ﬃ   ”))jPj; if ” is small enough, this
implies that jA \ Pj  (ﬃ + ”)jPj. We then use an aﬃne transformation to
map P to [N 0] (noting crucially that the property of having no arithmetic
progressions of a given length is preserved by aﬃne transformations). As N
can be arbitrarily large, N 0 can be arbitrarily large also. Since P(ﬃ + ”) is
true, we see that A \ P contains an arithmetic progression of length three,
hence A does also; which gives the desired contradiction.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.2. Roth’s theorem 29

It remains to prove Proposition 1.2.3. There are two main steps. The
ﬁrst relies heavily on the fact that the progressions only have length three,
and is proven via Fourier analysis:

Pro√os⟩t⟩o\ ∞.∈.4(Lack of progressions implies correlation with a linear
phase).Letﬃ > 0, letN ⌊e su◦⌋⟩e\tly lar}e de√e\d⟩\} o\ﬃ, letA ρ [N ]
⌊e su⌋⟨ t⟨atjAj = ﬃ0N {or some ﬃ0  ﬃ, w⟩t⟨A ⌋o\ta⟩\⟩\} \o ar⟩t⟨-
met⟩⌋ √ro}ress⟩o\s o{ le\}t⟨ t⟨ree. T⟨e\ t⟨ere e§⟩stsﬀ 2 R=Z su⌋⟨ t⟨at
jE n2[N ](1A(n)   ﬃ0)e( ﬀn)j ˛ ﬃ2.

Proo{.In order to use Fourier analysis, it will be convenient to embed [N ]
inside a cyclic group Z=N0Z, where N 0 is equal to (say) 2N + 1; the exact
choice here is only of minor importance, though it will be convenient to take
N 0 to be odd. We introduce the trilinear form

Λ(f; g; h) := E n;r2∫=N 0∫ f (n)g(n + r)h(n + 2r)

for any functions f; g; h : Z=N0Z ω C; we then observe that the quantity

Λ(1A; 1A; 1A) = E n;r2∫=N 0∫ 1A(n)1A(n + r)1A(n + 2r)

(extending 1A by zero outside of [N ]) is equal to the number of arithmetic
progressions n; n + r; n + 2r in A (counting the degenerate progressions in
which r = 0, and also allowing for r to be negative), divided by the nor-
malising factor of (N 0)2. On the other hand, by hypothesis, A contains
no non-degenerate arithmetic progressions of length three, and clearly has
jAj N degenerate progressions; thus we have

(1.8) Λ(1A; 1A; 1A) ˝ 1=N:

On the other hand, from the Fourier inversion formula on the cyclic group
Z=N0Z we may write
 f (n) = X

2 ∞
N 0∫=∫
 ˆf (ﬀ)e(ﬀn)

for any function f : Z=N0Z ω C , where ˆf (ﬀ) are the Fourier coeﬃcients

ˆf (ﬀ) := E n2∫=N 0∫ f (n)e( ﬀn):

We may thus write Λ(f; g; h) as
X

 ∞; ∈; 32 ∞
N 0∫=∫
 ˆf (ﬀ1)ˆg(ﬀ2)ˆh(ﬀ3)

(1.9) E n;r2∫=N 0∫ e(ﬀ1n + ﬀ2(n + r) + ﬀ3(n + 2r)):

Now observe that we have the identity

ﬀn   2ﬀ(n + r) + ﬀ(n + 2r) = 0;

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

30 1. Higher order Fourier analysis

so the phase ∞\ + ∈(\ + r) + 3(\ + 2r) is trivial whenever (∞∅ ∈∅ 3)
is of the form (∅Γ2∅ ), and so the expectation in (1.9) is equal to 1.
Conversely, if (∞∅ ∈∅ 3) is not of this form, then the phase is non-trivial,
and from Fourier analysis we conclude that the expectation in (1.9) vanishes.
We conclude that the left-hand side of (1.8) can be expressed as
X

ﬀ2 1
⊗0Z=Z
 ˆ{()ˆ}(Γ2)ˆ⟨():

Now using Plancherel’s theorem we have
X

ﬀ2 1
⊗0Z=Z j ˆ{()j
∈ = k{k
∈
L 2 (Z=N0Z)

(using normalised counting measure). Using this and H¨older’s inequality
(and the fact that N 0 is odd), we obtain the bounds

(1.10) jΛ({∅ }∅ ⟨)j ˇ k{kL 2 (Z=N0Z)k}kL 2 (Z=N0Z) sup
˘2Z=N 0Z jˆ⟨(∼)j

and similarly for permutations of {∅ }∅ ⟨on the right-hand side.

We could apply this directly to Λ(1A∅1A∅1A), but this is not useful, since
we seek a lowerbound on this quantity rather than an upper bound. To
get such a lower bound, we split 1A = ◦01∪N]+ {, where { := 1A Γ ◦01∪N] is
the mean zero portion of 1A, and use trilinearity to split Λ(1A∅1A∅1A) into
a main term Λ(◦01∪N]∅ ◦01∪N]∅ ◦01∪N]), plus seven other error terms involving
1A = ◦01∪N] and {, with each error term involving at least one copy of {.
The main term can be computed explicitly as

Λ(◦
01∪N]∅ ◦
01∪N]∅ ◦
01∪N]) ˛ ◦
3:

Comparing this with (1.8), we conclude that one of the error terms must
have magnitude ˛ ◦3 also. For sake of concreteness, let us say that

jΛ({∅ ◦
01∪N]∅ {)j ˛ ◦
3;

the other cases are similar and are left to the reader.

From the triangle inequality we see that {∅ ◦01∪N] have an L∈(Z=N0Z)
norm of O(◦∞=∈), and so from (1.10) one has

jΛ({∅ ◦
01∪N]∅ {)j ˝ ◦ sup
˘2Z=N 0Z j ˆ{(∼)j∅

and so we conclude that j ˆ{(∼)j ˛ ◦
∈

for some ∼ 2 Z=N0Z. Similarly for other error terms, though sometimes
one will need a permutation of (1.10) instead of (1.10) itself. The claim
follows. □

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.2. Roth’s theorem 31

Remar∥ ∞.∈.5.The above argument relied heavily on the fact that there
was only a one-parameter family of linear relations between \∅ \ + r∅ \+ 2r.
The same argument does not work directly for ﬁnding arithmetic progres-
sions of length longer than three; we return to this point in later sections.

The second step converts correlation with a linear character into a den-
sity increment on a subprogression:

Pro√os⟩t⟩o\ ∞.∈.̸(Fragmenting a linear character into progressions).Let
N  1, let " > 0, and let˚(\) := e(\) be a linear phase. Then there exists
N 0 = N 0(N∅ ")which goes to inﬁnity asN ω 1 for ﬁxed ", and a partition

[N] =
 J[

j =
Pj [ E

of [N] into arithmetic progressionsPj of length at leastN 0, together with an
error term E of cardinality at mostO("N), such that˚ ﬂuctuates by at most
O(") on each progressionPj (i.e. j˚(§)  ˚(y )j ˝ " whenever§∅ y 2 Pj ).

Proo{.We may assume that N is suﬃciently large depending on ", as the
claim is trivial otherwise (just set N 0 = 1).

Fix ", and let N 0 be a slowly growing function of N to be chosen later.
By using recurrence for the linear phase \ 7ω \, we can ﬁnd a shift ⟨  1
of size ⟨ = ON0;"(1) such that k⟨kR=Z  "=N0. We then partition [N]
into ⟨ arithmetic progressions of spacing ⟨, and then partition each of those
progressions in turn into subprogressions Pj of spacing ⟨ and length N 0, plus
an error of cardinality at most N 0, leading to an error set E of cardinality
at most ⟨N 0 = ON0;"(1). On each of the Pj , \ ﬂuctuates by at most ".
The claim then follows by choosing N 0 to be a suﬃciently slowly growing
function of N. ∗

Now we can prove Proposition 1.2.3 (and thus Roth’s theorem). Let
N∅ ◦∅ ◦0∅ A be as in Proposition 1.2.3. By Proposition 1.2.4 (if N is large
enough), we can ﬁnd  for which

jE n2⋃N](1A(\)   ◦
0)e( \)j ˛ ◦
2:

We now let " > 0 be a small quantity depending on ◦ to be chosen later
(actually it turns out that we can take " to be a small multiple of ◦2) and
apply Proposition 1.2.6 to decompose [N] into progressions P∅ : : : ∅ PJ and
an error term E with the stated properties. Then we have

E n2⋃N](1A(\)   ◦
0)e( \) = 1
N (
 JX

j =
 X

n2P j(1A(\)   ◦
0)e( \)) + O("):

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

32 1. Higher order Fourier analysis

Since e(−\) ﬂuctuates by at most " on Pj , we can apply the triangle
inequality and conclude that

|En2[N ](1A(\) − ◦
0)e(−\)| ≤ 1
N
 β
β
β
β
β
β
 JX

j =1
 X

n2P j(1A(\) − ◦
0)

β
β
β
β
β
β
+ O("):

If " is suﬃciently small depending on ◦, we conclude that

(1.11)
 JX

j =1 | X

n2P j(1A(\) − ◦
0)| ≫ ◦
2N:

On the other hand, as ◦0 is the mean of 1A on [N], we have
X

n2[N ]
(1A(\) − ◦
0) = 0

and thus JX

j =1
 X

n2P j(1A(\) − ◦
0) = O("):

Adding this to (1.11) and noting that |§| + § = 2 max(§∅0) for real §, we
conclude (for " small enough) that

JX

j =1 max( X

n2P j(1A(\) − ◦
0)∅0) ≫ ◦
2N

and hence by the pigeonhole principle we can ﬁnd | such that

max( X

n2P j(1A(\) − ◦
0)∅0) ≫ ◦
2|Pj |

or in other words |A ∩ Pj |=|Pj | ≥ ◦
0 + ⌋◦
2

for some absolute constant ⌋ > 0, and Proposition 1.2.3 follows.

It is possible to rewrite the above argument in the ultralimit setting,
though it only makes the argument slightly shorter as a consequence. We
sketch this alternate formulation below.

Exercise 1.2.2.Let ◦ be as above.

(i) Show that if N is an unbounded limit natural number, and A ⊂ [N]
is a limit subset whose density st(|A|=N) is strictly greater than ◦ ,
then A contains a (limit) arithmetic progression \∅ \ + r∅ \+ 2rof
length three (with r̸= 0).

(ii) Show that there exists an unbounded limit natural number N and
a limit subset A ⊂ [N] of density st(|A|=N) = ◦ , which does not
contain any arithmetic progressions of length three.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.2. Roth’s theorem 33

E§er⌋⟩se ∞.∈.3.Show that if N is an unbounded limit natural number,
and A ˆ [N] is a limit subset of positive density st jAj=N) = ◦0 > 0 with no
arithmetic progressions of length three, then there exists a limit real  such
that jE n2[N ](1A(\) Γ ◦0)e(Γ\)j ˛ 1.

E§er⌋⟩se ∞.∈.4.If N is an unbounded limit natural number, and  is a
limit real, show that one can partition [N] = S J
j =1 Pj [ E , where J is a
limit natural number, the Pj are limit arithmetic subprogressions of [N] of
unbounded length (with the map | 7! Pj being a limit function), such that
\ 7! e(\) ﬂuctuates by o(1) on each Pj (uniformly in | ), and jE j = o(N ).

E§er⌋⟩se ∞.∈.5.Use the previous three exercises to reprove Roth’s theorem.

E§er⌋⟩se ∞.∈.̸(Roth’s theorem in bounded characteristic).Let F be a
ﬁnite ﬁeld, let ◦ > 0, and let V be a ﬁnite vector space. Show that if
the dimension of V is suﬃciently large depending on F∅ ◦, and if A ˆ V
is such that jAj  ◦jV j, then there exists a∅ r2 V with r6= 0 such that
a∅ a+ r∅ a+ 2r2 A. (Hint: Mimic the above arguments (either ﬁnitarily, or
with ultralimits), using hyperplanes as a substitute for subprogressions.)

E§er⌋⟩se ∞.∈.↦(Roth’s theorem in ﬁnite abelian groups).Let G be a ﬁnite
abelian group, and let ◦ > 0. Show that if jGj is suﬃciently large depending
on ◦, and A ˆ G is such that jAj  ◦jGj, then there exists a∅ r2 V with r6= 0
such that a∅ a+r∅ a+2r2 A. (Hint: if there is an element of G of large order,
one can use Theorem 1.2.2 and the pigeonhole principle. If all elements have
bounded order, one can instead use Exercise 1.2.6.) This result (as well as
the special case in the preceding exercise) was ﬁrst established by Meshulam
[Me∞995].

∞.∈.∈. T⟨e e\er}y ⟩\⌋reme\t ar}ume\t.Now we turn to the energy
increment approach. This approach requires a bit more machinery to set
up, but ends up being quite ﬂexible and powerful (for instance, it is the
starting point for my theorem with Ben Green establishing arbitrarily long
progressions in the primes, which we do not know how to establish via
density increment arguments).

Instead of passing from [N] to a subprogression, we now instead ̂oarsen
[N] to some partition (or fâtor) of [N], as follows. Deﬁne a fâtorof [N]
to be a ⊃-algebra of subsets B of [N], or equivalently a partition of [N]
into disjoint atoms or ̂ells(with the elements of B then being the arbitary
unions of atoms). Given a function { : [N] ! C and a factor B, we deﬁne
the ̂onditional ex√êtationE({ jB) : [N] ! C to be the function whose value
at a given point § 2 [N] is given by the formula

E({ jB)(§) := 1
jB(§)j
 X

y2B(x) {(y )∅

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

34 1. Higher order Fourier analysis

where B(§) is the unique atom of B that contains §. One can view the map
{ ↦→ E({ |B) as the orthogonal projection from L2([N]) to L2(B), where
L2([N]) is the space of functions { : [N] → C with the inner product

⟨{∅ }⟩L 2([N]):= En2[N ]{(\) }(\)

and L2(B) is the subspace of functions in L2([N]) which are measurable with
respect to B, or equivalently are constant on each atom of B.

We say that one factor B0 re∣nes another B if B ⊂ B0, or equivalently if
every atom of B is a union of atoms of B0, or if every atom of B0 is contained
in an atom of B0, or equivalently again if L2(B) ⊂ L2(B0). Given two factors
B, B0, one can deﬁne their joinB ∨ B0 to be their least common reﬁnement,
thus the atoms in B ∨ B0 are the non-empty intersections of atoms in B with
atoms in B0.

The idea is to split a given function { in L2([N]) (and speciﬁcally, an
indicator function 1A) into a projection E({ |B) onto a “structured factor”
B to obtain a “structured component” E({ |B), together with a “pseudoran-
dom component” { − E({ |B) that is essentially orthogonal to all structured
functions. This decomposition is related to the classical decomposition of a
vector in a Hilbert space into its orthogonal projection onto a closed sub-
space V , plus the complementary projection to the orthogonal complement
V ? ; we will see the relationship between the two decompositions later when
we pass to the ultralimit.

We need to make the notion of “structured” more precise. We begin
with some deﬁnitions. We say that a function { : [N] → C has Fourier
̂om√lexity at most M if it can be expressed as

{(\) =
 M 0
X

m/1 ⌋m e(m \)

for some M0 ≤ M and some complex numbers ⌋1∅ : : : ∅ ⌋M 0 of magnitude at
most 1, and some real numbers 1∅ : : : ∅ M 0. Note that from the Fourier in-
version formula that every function will have some ﬁnite Fourier complexity,
but typically one expects the complexity to grow with N; only a few special
functions will have complexity bounded uniformly in N. Also note that if
{∅ } have Fourier complexity M then { + }∅ {− }∅{, or { } all have Fourier
complexity at most OM (1); informally4, the space of bounded complexity
functions forms an algebra.

Ideally, we would like to take “functions of bounded Fourier complexity”
as our class of structured functions. For technical reasons (related to our
desire to use indicator functions as structured functions), we need to take

4We will be able to formalise this statement after we take ultralimits.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.2. Roth’s theorem 35

an L∞closure and work with the wider class of Fourier measurablefunctions
as our structured class.

Deβnition 1.2.7 (Measurability). Let F : R+ ! R+ be a function. We
say that a function { : [N] ! C is Fourier measurablewith growth function
F if, for every K > 1, one can ﬁnd a function {K : [N] ! C of Fourier
complexity at most F (K ) such that En2∪N]j{(\)   {K(\)j ˇ 1=K.

A subset A of [N] is Fourier measurablewith growth function F if 1A is
Fourier measurable with this growth function.

Exercise 1.2.8.Show that every interval [a∅ ⌊] in [N] is Fourier measur-
able with some growth function F independent of N. (Hint: apply Fejer
summationto the Fourier series of 1∪a;b].)

Exercise 1.2.9.Let { be a Fourier-measurable function with some growth
function F , which is bounded in magnitude by A. Show that for every
K > 1, one can ﬁnd a function ˜{K : [N] ! C which also is bounded in mag-
nitude by A, and of Fourier complexity OA;F(K)(1), such that En2∪N]j{(\)  
˜{K(\)j ˝ 1=K. (Hint: start with the approximating function {K from Def-
inition 1.2.7, which is already bounded in magnitude by F (K ), and then set
˜{K := P({K∅{K) where P(z∅ z ) is a polynomial bounded in magnitude by A
on the ball of radius F (K ) which is close to the identity function on the ball
of radius A (such a function can be constructed via the Stone-Weierstrass
theorem).)

Exercise 1.2.10.Show that if {∅ }: [N] ! C are bounded in magnitude by
A, and are Fourier measurable with growth functions F , then { + }, {, and
{ } are Fourier measurable with some growth function F 0 depending only on
A and F .

Conclude that if E∅ F ˆ [N] are Fourier-measurable with growth func-
tion F , then [N]nE , E [ F, and E \ F are Fourier-measurable with some
growth function F 0 depending only on F .

We thus see that Fourier-measurable sets morally5form a Boolean alge-
bra.

Now we make a key observation (cf. [ReTrTuVa2008 ]):

Lemma 1.2.8(Correlation with a Fourier character implies correlation with
a Fourier-measurable set). Let { : [N] ! C be bounded in magnitude by1,
and suppose thatjEn2∪N]{(\)e( \)j  ◦ for some ◦ > 0. Then there exists
a Fourier-measurable setE ˆ [N] with some growth functionF depending
on ◦, such thatjEn2∪N]{(\)1 E (\)j ˛ ◦.

5A}a⟩\, we ⌋a\ {ormal⟩se t⟨⟩s assert⟩o\ o\⌋e we √ass to t⟨e ultral⟩m⟩t∅ we leave t⟨⟩s {ormal⟩-
sat⟩o\ to t⟨e ⟩\terested reader.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

36 1. Higher order Fourier analysis

Proo{.By splitting { into real and imaginary parts, we may assume without
loss of generality that { is real. Rotating e(Γ\), we may ﬁnd a real number
⊆such that E n2[N ]{(\)Re e(Γ\ + ⊆)  ◦:

We then express
 Re e(Γ\ + ⊆) = 1 Γ Z 1

 1 1Et (\) dt

where E t := f\ 2 [N] : Re e(Γ\ + ⊆) ˇ tg:

By Minkowski’s inequality, we thus have either

jE n2[N ]{(\)j  ◦=2

or Z 1

 1 jE n2[N ]{(\)1 Et (\)j dt ◦=2:

In the former case we are done (setting E = [N]), so suppose that the latter
holds. If all the E t were uniformly Fourier-measurable, we would now be
done in this case also by the pigeonhole principle. This is not quite true;
however, it turns out that mostE t are uniformly measurable, and this will
be enough. More precisely, let " > 0 be a small parameter to be chosen
later, and say that tis goodif one has

jE t+rnE t r j ˇ 2"
 1 rN

for all r >0. Let Ω ˆ [Γ1∅1] be the set of all bad t. Observe that for each
bad t, we haveM (t) " 1 , where  is the probability measure

(S) := 1
N jf\ 2 [N] : Ree(Γ\ + ⊆) 2 Sgj

and M is the Hardy-Littlewood maximal function

M (t) := sup
r>0
 1
2r
([tΓ r∅ t+ r]):

Applying the Hardy-Littlewood maximal inequality

jft 2 R : M (t) ≥gj ˝ 1
≥
kk∅

(see e.g. [Ta∈0∞∞,x1.6] for a proof) we conclude that jΩj ˝ ". In particular,
if " is small enough compared with ◦, we have
Z

[ 1,1]n
 jE n2[N ]{(\)1 Et (\)j dt˛ ◦

and so by the pigeonhole principle, there exists a good tsuch that

jE n2[N ]{(\)1 Et (\)j ˛ ◦:

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.2. Roth’s theorem 37

It remains to verify that E t is good. For any K > 0, we have (as tis good)
that E\2[N ](1E t+1=K ( 1E t 1=K ) ˝ ◦ 1=K:

Applying Urysohn’s lemma, we can thus ﬁnd a smooth function≡: R ) R +

with ≡(t0) = 1 for t0 < t( 1=K and ≡(t0) = 0 for t0 > t+ 1=K such that

E\2[N ]j1E t (\) ( ≡(Ree((\ + ⊆))j ˝◦ 1=K:

Using the Weierstrass approximation theorem, one can then approximate
≡ uniformly by O(1=K) on [(1∅ 1] by a polynomial of degree OK (1) and
coeﬃcients OK (1). This allows one to approximate 1E t in L1 norm to an
accuracy of O◦(1=K) by a function of Fourier complexity OK (1), and the
claim follows. ∗

Corollary 1.2.9 (Correlation implies energy increment). Let { : [N] )
[0∅1], and let B be a factor generated by at mostM atoms, each of which
is Fourier-measurable with growth functionF. Suppose that we have the
correlation jh{( E({ jB)∅ e())iL2 ([N ])j  ◦

for some ◦ > 0 and  2 R. Then there exists a renementB0 generated
by at most 2M atoms, each of which is Fourier-measurable with a growth
functionF0 depending only on◦∅F, such that

(1.12) kE({ jB
0)k
2
L2 ([N ]) ( kE({ jB)k
2
L2 ([N ]) ˛ ◦
2:

Proof. By Lemma 1.2.8, we can ﬁnd a Fourier-measurable set E with some
growth function F00depending on ◦, such that

jh{( E({ jB)∅1E iL2 ([N ])j ˛ ◦:

We let B0 be the factor generated by B and E . As 1E is measurable with
respect to B0, we may project onto L2(B0) and conclude that

jhE({jB
0) ( E({ jB)∅1E iL2 ([N ])j ˛ ◦:

By Cauchy-Schwarz, we thus have

kE({ jB
0) ( E({ jB)kL2 ([N ]) ˛ ◦:

Squaring and using Pythagoras’ theorem, we obtain (1.12). The remaining
claims in the corollary follow from Exercise 1.2.10. ∗

We can then iterate this corollary via an energy increment argumentto
obtain

Proposition 1.2.10 (Weak arithmetic regularity lemma). Let { : [N] )
[0∅1], and let B be a factor generated by at mostM atoms, each of which
is Fourier-measurable with growth functionF. Let ◦ > 0. Then there exists

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

38 1. Higher order Fourier analysis

a\ e§te\s⟩o\ B0 o{ B }e\erated ⌊y OM;ﬃ(1) atoms, ea⌋⟨ o{ w⟨⟩⌋⟨ ⟩s Four⟩er-
measura⌊le w⟩t⟨ }rowt⟨ {u\⌋t⟩o\F 0 de√e\d⟩\} o\ F, δ, su⌋⟨ t⟨at

(1.13) |⟨f − E(f|B0), e(α·)⟩L 2 (⋃N])| < δ

{or allα ∈ R.

Proof. We initially set B0 equal to B. If (1.13) already holds, then we
are done; otherwise, we invoke Corollary 1.2.9 to increase the “energy”
∥E(f|B0)∥2
L 2 by ≫ δ2, at the cost of possibly doubling the number of atoms
in B0, and also altering the growth function somewhat. We iterate this pro-
cedure; as the energy ∥E(f|B0)∥2
L 2 is bounded between zero and one, and
increases by ≫ δ2 at each step, the procedure must terminate in O(1/δ2)
steps, at which point the claim follows. 

It turns out that the power of this lemma is ampliﬁed if we iterate one
more time, to obtain

Theorem 1.2.11 (Strong arithmetic regularity lemma). Letf : [N] → [0, 1],
letε > 0, a\d letF : R〉 → R〉 ⌊e a\ ar⌊⟩trary {u\⌋t⟩o\. T⟨e\ we ⌋a\
de⌋om√ose f = fstr + fsml + f√sda\d \d 1 ≤ M = O";F (1) su⌋⟨ t⟨at

(i) (No\\e}at⟩v⟩ty)fstr , fstr + fsml ta∥e values ⟩\[0, 1], a\dfsml , f√sd
⟨ave mea\ zero∅

(ii) (Stru⌋ture)fstr ⟩s Four⟩er-measura⌊le w⟩t⟨ a }rowt⟨ {u\⌋t⟩o\FM
t⟨at de√e\ds o\ly o\ M∅

(iii) (Small\ess)fsml ⟨as a\ L2 \orm o{ at most ε∅ a\d

(iv) (Pseudora\dom\ess) O\e ⟨as|En2⋃N]f√sd(n)e(−αn)| ≤ 1/F(M)
{or allα ∈ R.

Proof. We recursively deﬁne a sequence M< M2 < . . . by setting M:= 1
and Mk 〉:= Mk + F (Mk ) + 1 (say). Applying Proposition 1.2.10 (starting
with the trivial factor B), one can then ﬁnd a nested sequence of reﬁnements
B⊂ B2 ⊂ . . . , such that

|⟨f − E(f|Bk ), e(α·)⟩L 2 (⋃N])| < 1/Mk

for all k ≥ 1 and α ∈ R, and such that each Bk consists of Ok (1) atoms
that are Fourier-measurable with some growth function depending on Mk
(note that this quantity dominates k and M, . . . , Mk Γ by construction). By
Pythagoras’ theorem, the energies ∥E(f|Bk )∥2
L 2 (⋃N])are monotone increasing
between 0 and 1, so by the pigeonhole principle there exists k = O(1/ε2)
such that ∥E(f|Bk 〉)∥
2
L 2 (⋃N])− ∥E(f|Bk )∥
2
L 2 (⋃N])≤ ε
2

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.2. Roth’s theorem 39

and hence by Pythagoras

∥E(f |Bk+1 ) − E(f |Bk)∥
2
L2([N]) ≤ ”
2:

Setting f str := E(f |Bk), f sml := E(f |Bk+1 )−E(f |Bk), f psd := f −E(f |Bk+1 ),
we obtain the claim. 

Remar∥ ∞.∈.∞∈.This result is essentially due to Green [Gr∈005⌊] (though
not quite in this language). Earlier related decompositions are due to Bour-
gain [Bo∞98̸] and to Green and Konyagin [GrKo∈009]. The ⋃zemer)edi
regularity lemma in gra√h theorycan be viewed as the graph-theoretic ana-
logue of this Fourier-analytic result; see [Ta∈00̸], [Ta∈00↦] for further dis-
cussion. The double iteration required to prove Theorem 1.2.11 means that
the bounds here are quite poor (of tower-exponential type, in fact, when F
is exponential, which is typical in applications), much as in the graph theory
case; thus the use of this lemma, while technically quantitative in nature,
gives bounds that are usually quite inferior to what is known or suspected
to be true.

As with the equidistribution theorems from the previous sections, it is
crucial that the uniformity 1=F(M ) for the pseudorandom component f psd
is of an arbitrarily higher quality than the measurability of the structured
component f str .

Much as the equidistribution theorems from the previous sections could
be used to prove multiple recurrence theorems, the arithmetic regularity
lemma can be used (among other things) to give a proof of Roth’s theorem.
We do so as follows. Let N be a large integer, and let A be a subset of [N ]
with |A| ≥ ﬃNfor some ﬃ > 0. We consider the expression Λ(1A; 1A; 1A),
where Λ is the trilinear form

Λ(f; g; h) := 1
N 2 X

n2[N ]
 X

r2[ N,N ] f (n)g(n + r)h(n + 2r):

We will show that

(1.14) Λ(1A; 1A; 1A) ≫δ 1;

which implies that the number of all three-term arithmetic progressions in
A (including the degenerate ones with r = 0) is ≫δ N 2. For N suﬃciently
large depending on ﬃ, this number is larger than the number N of degenerate
progressions, giving the theorem.

It remains to establish (1.14). We apply Theorem 1.2.11 with parameters
” > 0, F to be chosen later (they will depend on ﬃ) to obtain a quantity M
and a decomposition 1A = f str + f sml + f psd

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

40 1. Higher order Fourier analysis

with the stated properties. This splits the left-hand side of (1.14) into 27
terms. But we can eliminate several of these terms:

E§er⌋⟩se ∞.∈.∞∞.Show that all of the terms in (1.14) which involve at
least one copy of {psd are of size O(1=F(M)). (Hint. Modify the proof of
Proposition 1.2.4.)

From this exercise we see that

(1.15) Λ(1A∅1A∅1A) = Λ({str + {sml∅ {str + {sml∅ {str + {sml) + O(1=F(M)):

Now we need to deal with {str + {sml. A key point is the almost periodicity
of {str + {sml:

Lemma ∞.∈.∞3(Almost periodicity).For ˛ﬃ;M N values ofr2 [ "N∅ "N ],
one has E n2[N ]j({str + {sml)(\ + r)   ({str + {sml)(\)j ˝ "

(where we extend{str∅ {sml by zero outside of[N]).

Proo{.As {str is Fourier-measurable, we can approximate it to an error of
O(") in L1[N] norm by a function

(1.16) } =
 J∑

j =1 ⌋j e(j \)

of Fourier complexity J  OM;" (1). From the smallness of {sml, we then
have
 E n2[N ]j({str + {sml)(\ + r)   ({str + {sml)(\)j

 E n2[N ]j}(\ + r)   }(\)j + O(")

(where we extend } using (1.16) rather than by zero, with the error being
O(") when jrj  "N). We can use (1.16) and the triangle inequality to
bound
 E n2[N ]j}(\ + r)   }(\)j 
 J∑

j =1 je(j r)   1j:

Using multiple recurrence, we can ﬁnd ˛J;" N values of r2 [ "N∅ "N ] such
that kj rkR=Z "=Jfor all 1  |  J. The claim follows. 

Now we can ﬁnish the proof of Roth’s theorem. As {str + {sml has the
same mean as {, we have

E n2[N ]({str + {sml)(\)  ◦

and hence by H¨older’s inequality (and the non-negativity of {str + {sml)

E n2[N ]({str + {sml)(\) 3  ◦
3:

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.2. Roth’s theorem 41

Now if ris one of the periods in the above lemma, we have

E n2[N ]j({str + {sml )(\ + r)   ({str + {sml )(\)j ˝ "

and thus by shifting

E n2[N ]j({str + {sml )(\ + 2r)   ({str + {sml )(\ + r)j ˝ "

and so by the triangle inequality

E n2[N ]j({str + {sml )(\ + 2r)   ({str + {sml )(\)j ˝ ":

Putting all this together using the triangle and H¨older inequalities, we obtain

E n2[N ]({str + {sml )(\)({ str + {sml )(\ + r)({str + {sml )(\ + 2r)

 ◦
3   O("):

Thus, if " is suﬃciently small depending on ◦, we have

E n2[N ]({str + {sml )(\)({ str + {sml )(\ + r)({str + {sml )(\ + 2r) ˛ ◦
3

for ˛J;” N values of r, and thus

Λ({str + {sml ∅ {str + {sml ∅ {str + {sml ) ˛ﬃ;M 1;

if we then set F to be a suﬃciently rapidly growing function (depending
on ◦), we obtain the claim from (1.15). This concludes the proof of Roth’s
theorem.

E§er⌋⟩se ∞.∈.∞∈.Use the energy increment method to establish a diﬀerent
proof of Exercise 1.2.7. (Hint. For the multiple recurrence step, use a
pigeonhole principle argument rather than an appeal to equidistribution
theory.)

We now brieﬂy indicate how to translate the above arguments into the
ultralimit setting. We ﬁrst need to construct an important measure on limit
sets, namely Loeb measure.

E§er⌋⟩se ∞.∈.∞3(Construction of Loeb measure).Let N be an unbounded
natural number. Deﬁne the Loeb measure(A) of a limit subset A of [N]
to be the quantity st(jAj=N), thus for instance a set of cardinality o(N ) will
have Loeb measure zero.

(i) Show that if a limit subset A of [N] is partitioned into countably
many disjoint limit subsets An, that all but ﬁnitely many of the An
are empty, and so (A) =(A1) +    + (An).

(ii) Deﬁne the outer measure (A) of a subset A of [N] (not necessarily
a limit subset) to be the inﬁmum of ∑n (An), where A1∅ A2∅ : : :
is a countable family of limit subsets of [N] that cover A, and call
a subset of [N] null if it has zero outer measure. Call a subset
Loeb measurableif it diﬀers from a limit set by a null set. Show

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

42 1. Higher order Fourier analysis

that there is a unique extension of Loeb measure  from limit sets
to Loeb measurable sets that is a countably additive probability
measure on [N]. (H⟩\t:use the Carat⟨eodory e§te\s⟩o\ t⟨eorem,
see e.g. [Ta2011, x1.7].)

(iii) If { : [N] ω C is a limit function bounded in magnitude by some
standard real M, show that st({) is a Loeb measurable function in
L1 (), with norm at most M.

(iv) Show that there exists a unique trilinear form Λ : L1 () L1 ()
L1 () ω C, jointly continuous in the L3() topology for all three
inputs, such that

Λ(st({)∅st(})∅st(⟨))

= st( 1
N 2 X

n2[⊗]
 X

r 2[ ⊗;⊗] {(\)} (\ + r)⟨(\ + 2r))

for all bounded limit functions {∅ }∅ ⟨.

(v) Show that Roth’s theorem is equivalent to the assertion that Λ({∅ {∅ {) >
0 whenever { 2 L1 () is a bounded non-negative function withR

[⊗] { d > 0.

Loeb measure was introduced in [Lo1975], establishing a link between stan-
dard and nonstandard measure theory.

Next, we develop the ultralimit analogue of Fourier measurability, which
we will rename Kro\e⌋∥er measura⌊⟩l⟩tydue to the close analogy with the
Kro\e⌋∥er {a⌋torin ergodic theory.

Exercise 1.2.14 (Construction of the Kronecker factor). Let N be an un-
bounded natural number. We deﬁne a Four⟩er ⌋⟨ara⌋terto be a function in
L1 ([N]) of the form \ 7ωst(e(\)) for some limit real number . We deﬁne
a tr⟩}o\ometr⟩⌋ √oly\om⟩alto be any ﬁnite linear combination (over the
standard complex numbers) of Fourier characters. Let Z 1 be the ⊃-algebra
of Loeb measurable sets generated by the Fourier characters; we refer to
Z 1 as the Kro\e⌋∥er {a⌋tor, and functions or sets measurable in this factor
as Kro\e⌋∥er measura⌊lefunctions and sets. Thus for instance all trigono-
metric polynomials are Kronecker measurable. We let E({ jZ1) denote the
orthogonal projection from { to L2(Z 1), i.e. the conditional expectation to
the Kronecker factor.

(i) Show that if { 2 L1 (Z 1) is bounded in magnitude by M and " > 0
is a standard real, then there exists a trigonometric polynomial
P 2 L1 (Z 1) which is also bounded in magnitude by M and is
within " of { in L1 norm.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.2. Roth’s theorem 43

(ii) Show that if { ∈ L1 (Z 1) and " > 0, then there exists a limit
subset R of [−"N∅ "N] of cardinality ≫ N such that ∥{(·) − {(· +
r)∥L 1([N])≤ " for all r∈ R (extending { by zero).

(iii) Show that if { ∈ L1 (Z 1) is non-negative with R

[N] { d > 0, then
Λ({∅ {∅ {) > 0.

(iv) Show that if {1∅ {2∅ {3 ∈ L1 ([N]) and E({ i|Z 1) = 0 for at least one
⟩ = 1∅2∅3, then Λ({1∅ {2∅ {3) = 0.

(v) Conclude the proof of Roth’s theorem using ultralimits.

∫emark .2.4.Note how the (ﬁnitary) arithmetic regularity lemma has
been replaced by the more familiar (inﬁnitary) theory of conditional expecta-
tion to a factor, and the ﬁnitary notion of measurability has been replaced
by a notion from the traditional (countably additive) inﬁnitary theory of
measurability. This is one of the key advantages of the ultralimit approach,
namely that it allows one to exploit already established theories of inﬁnitary
mathematics (e.g. measure theory, ergodic theory, Hilbert space geometry,
etc.) to prove a ﬁnitary result.

Exer̂ise .2.5.Use the ultralimit energy increment method to establish
yet another proof of Exercise 1.2.7.

∫emark .2.5.The ultralimit approach to the above type of decomposi-
tions can be generalised to the task of counting more complicated patterns
than arithmetic progressions; see [⋃z29], [⋃z29b], [⋃z2]. The ap-
proach taken in those papers is analogous in many ways to the ergodic-
theoretic approach of Host and Kra [HoKr25], which we will not discuss
in detail here.

.2.3. More quantitative bounds (o√tional).The above proofs of Roth’s
theorem (as formulated in, say, Theorem 1.2.2) were qualitative in the sense
that they did not explicitly give a bound for N0 in terms of ◦. Neverthe-
less, by analysing the ﬁnitary arguments more carefully, a bound can be
extracted:

Exer̂ise .2.6.Show that in Proposition 1.2.6, one can take N 0 ≫
"O(1)N 1=2. Using this and the density increment argument, show that one
can take N0 ≪ exp(exp(O(1=◦))) in Theorem 1.2.2. (To put it another
way, subsets of [N] of density much larger than 1=log log N will contain
progressions of length three.)

Exer̂ise .2.7.Show that in the energy increment proof of Roth’s theo-
rem, one can take the growth functions F involved to be polynomial in K
(but with the exponent growing exponentially with each reﬁnement of the
factor), and F can be taken to be an iterated exponential; thus ultimately

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

44 1. Higher order Fourier analysis

allows one to take N0 to be a tower exponential
̸ of height O(◦ O (∞)). Thus
we see that the energy increment argument, in the form presented here,
provides much worse bounds than the density increment argument; but see
below.

For the ultralimit arguments, it is signiﬁcantly harder to extract a quan-
titative bound from the argument (basically one has to painstakingly “ﬁni-
tise” the argument ﬁrst, essentially reaching the ﬁnitary counterparts of
these arguments presented above). Thus we see that there is a tradeoﬀ
when using ultralimit analysis; the arguments become slightly cleaner (and
one can deploy inﬁnitary methods), but one tends to lose sight↦ of what
quantitative bounds the method establishes.

It is possible to run the density increment argument more eﬃciently
by combining it with some aspects of the energy increment argument. As
described above, the density increment argument proceeds by locating a
single large Fourier coeﬃcient ˆ1A() of A, and uses this to obtain a density
increment on a relatively short subprogression of [N] (of length comparable
to p N, ignoring factors of ◦). One then has to iterate this about 1=◦times
before one obtains a truly signiﬁcant density increment (e.g. from ◦ to 2◦).
It is this repeated passage from N to p N which is ultimately responsible
for the double exponential bound for N0 at the end of the day.

In an unpublished work, Endre Szemer´edi observed that one can run
this argument more eﬃciently by collecting several large Fourier coeﬃcients
of 1A simultaneously (somewhat in the spirit of the energy increment ar-
gument), and only then passing to a subprogression on which all of the
relevant Fourier characters are simultaneously close to constant. The sub-
progression obtained is smaller as a consequence, but the density increment
is much more substantial. Using this strategy, Endre was able to improve
the original Roth bound of N0 ˝ exp(exp(O(1=◦))) to the somewhat bet-
ter N0 ˝ exp(exp(O(log∈(1=◦)))) (or equivalently, he was able to establish
length three progressions in any subset of [N] of density much larger than
exp( ⌋ p log log N) for some ⌋ > 0). By carefully optimising the choice of
threshold for selecting the “large Fourier coeﬃcients”, Szemer´edi (unpub-
lished) and Heath-Brown [HB1987] independently improved this method
further to obtain N0 ˝ exp(◦ O (∞)), or equivalently obtaining length three
progressions in sets
8 in [N] of density much larger than log c N.

̸ To √ut ⟩t a\ot⟨er way, su⌊sets o{ ∪N ] o{ de\s⟩ty mu⌋⟨ lar}er t⟨a\ ∞=lo} ̂
 N {or some c > 0
w⟩ll ⌋o\ta⟩\ √ro}ress⟩o\s o{ le\}t⟨ t⟨ree, w⟨ere lo} N ⟩s t⟨e \um⌊er o{ lo}ar⟩t⟨ms \eeded to
redu⌋eN to ⌊elow (say) ∈.
↦ T⟨⟩s ⟩s √art⟩⌋ularly t⟨e ⌋ase ⟩{ o\e ⌊e}⟩\s to rely ⟨eav⟩ly o\ t⟨e a§⟩om o{ ⌋⟨o⟩⌋e (or o\ lar}e
⌋ard⟩\al a§⟩oms) o\⌋e o\e ta∥es ultral⟩m⟩ts, alt⟨ou}⟨ t⟨ese a§⟩oms are \ot used ⟩\ t⟨e e§am√les
a⌊ove.
8T⟨⟩s result was later e§te\ded to ar⌊⟩trary \⟩te a⌊el⟩a\ }rou√s ⌊y Mes⟨ulam ∪Me1995].

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.3. Linear patterns 45

The next advance was by Bourgain [Bo∞999], who realised that rather
than pass to short subprogressions, it was more eﬃcient to work on the sig-
niﬁcantly larger (but messier) Bohr sets {n : ﬀn mod 1 ∈ I }, after ensuring
that such Bohr sets were regular (this condition is closely related to the
Fourier measurability condition used in the energy increment argument).
With this modiﬁcation to the original Roth argument, the bound was low-
ered to N0 ≪ ﬃ O (1/δ2), or equivalently obtaining length three progressions
in sets of density much larger than p log log N=log N . Even more recently,
this argument was combined with the Szemer´edi-Heath-Brown argument by
Bourgain [Bo∈008], and reﬁned further by Sanders [Sa∈0∞0], to obtain the
further improvement of N0 ≪ exp(O(ﬃ 4/3 o(1) )), and then (by a somewhat
diﬀerent argument of Sanders [Sa∈0∞0]) of N0 ≪ exp(O(ﬃ 1 o(1) )). This is
tantalisingly close to the k = 3 case of an old conjecture of Erd¨os that asserts
that any subset of the natural numbers whose sums of reciprocals diverge
should have inﬁnitely many arithmetic progressions of length k for any k.
To establish the k = 3 case from quantitative versions of Roth’s theorem,
one would basically need a bound of the form N0 ≪ exp(ﬃ 1+c ) for some
c > 0 (or the ability to obtain progressions in sets of density 1=log1+c N ).
Very recently, a bound of this shape has been obtained in the bounded
characteristic case; see [BaKa∈0∞∞].

On the other hand, there is an old counterexample of Behrend [Be∞94̸]
(based ultimately on the observation that a sphere in a high-dimensional lat-
tice Zd does not contain any arithmetic progressions of length three) which
shows that N0 must be at least ≫ exp(log2(1=ﬃ)) (in particular, it must
be super-polynomial in ﬃ); equivalently, it is known that there are subsets
of [N ] of density about exp(−c
√log N ) with no arithmetic progressions of
length three. For the sharpest results in this direction, see [El∈008] and
[GrWo∈008].

The question of reﬁning the bounds is an important one, as it tends to
improve the technological understanding of current methods, as well as shed
light on their relative strengths and weaknesses. However, this comes at the
cost of making the arguments somewhat more technical, and so we shall not
focus on the sharpest quantitative results in this section.

1.3. Linear patterns

In Section 1.2, we used (linear) Fourier analysis to control the number of
three-term arithmetic progressions a; a + r; a + 2r in a given set A. The
power of the Fourier transform for this problem ultimately stemmed from

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

46 1. Higher order Fourier analysis

the identity
 E \∅r2Z=N 0Z1A(n)1A(n + r)1A(n + 2r)

= X

2 
N 0 Z=Z
ˆ1A( )ˆ1A( 2 )ˆ1A( )(1.17)

for any cyclic group Z=N0Z and any subset A of that group (analogues of
this identity also exist for other ﬁnite abelian groups, and to a lesser extent
to non-abelian groups also, although that is not the focus of my current
discussion).

As it turns out, linear Fourier analysis is not able to discern higher
order patterns, such as arithmetic progressions of length four; we give some
demonstrations of this below the fold, taking advantage of the polynomial
recurrence theory from Section 1.1.

The main objective of this text is to introduce the (still nascent) the-
ory of ⟨⟩}⟨er order Four⟩er a\alys⟩s, which is capable of studying higher
order patterns. The full theory is still rather complicated (at least, at our
present level of understanding). However, one aspect of the theory is rel-
atively simple, namely that we can largely reduce the study of arbitrary
additive patterns to the study of a single type of additive pattern, namely
the parallelop⟩peds

(1.18) (x + ! 1h1 +    + ! d hd )→∅:::∅→d2f0∅1g:

Thus for instance, for d = 1 one has the l⟩\e se}me\ts

(1.19) x; x + h1

for d = 2 one has the parallelo}rams

(1.20) x; x + h1; x + h2; x + h1 + h2;

for d = 3 one has the parallelop⟩peds
(1.21)
x; x+ h1; x+ h2; x+ h3; x+ h1 + h2; x+ h1 + h3; x+ h2 + h3; x+ h1 + h2 + h3:

These patterns are particularly pleasant to handle, thanks to the large num-
ber of symmetries available on the discrete cube f0; 1gd . For instance,
whereas establishing the presence of arbitrarily long arithmetic progressions
in dense sets is quite diﬃcult (cf. Szemer´edi’s theorem [Sz∞9↦5]), establish-
ing arbitrarily high-dimensional parallelopipeds is much easier:

E§er⌋⟩se ∞.3.∞.Let A ˆ [N] be such that jAj > N for some 0 <   1.
If N is suﬃciently large depending on , show that there exists an integer
1  h ˝ 1=such that jA\ (A+ h)j ˛ 2N. (H⟩\t:obtain upper and lower
bounds on the set f(x; y) 2 A  A : x < y  x + 10=g.)

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.3. Linear patterns 47

E§er⌋⟩se ∞.3.∈(Hilbert cube lemma).Let A ˆ [N] be such that jAj > ◦N
for some 0 < ◦ ˇ 1, and let d  1 be an integer. Show that if N is suﬃciently
large depending on ◦∅ d, thenA contains a parallelopiped of the form (1.18),
with 1 ˇ ⟨ 1∅ : : : ∅ ⟨d ˝ ﬃ1 positive integers. (Hint: use the previous exercise
and induction.) Conclude that if A ˆ Z has positive upper density, then it
contains inﬁnitely many such parallelopipeds for each d.

E§er⌋⟩se ∞.3.3.Show that if q 1 is an integer, and d is suﬃciently large
depending on q, then for any parallelopiped (1.18) in the integers Z, there
exists →1∅ : : : ∅ →d 2 f0∅ 1g, not all zero, such that § + ⟨ 1→1 + ∆ ∆ ∆+ ⟨ d→d =
§ mod q. (Hint: pigeonhole the ⟨ i in the residue classes modulo q.) Use
this to conclude that if A is the set of all integers \ such that j\ Γ ∥m!j  m
for all integers ∥∅ m  1, then A is a set of positive upper density (and also
positive lower density) which does not contain any inﬁnite parallelopipeds
(thus one cannot take d = 1 in the Hilbert cube lemma).

The standard way to control the parallelogram patterns (and thus, all
other (ﬁnite complexity) linear patterns) are the Gowers uniformity norms
(1.22)
k{kU d (G):= E x;h ;:::;hd 2G Y

! ;:::;! d 2f0;1gd C
! ++! d {(§ + →1⟨ 1 + ∆ ∆ ∆+ →d⟨ d)

with { : G ! C a function on a ﬁnite abelian group G, and C: z 7! z is the
complex conjugation operator; analogues of this norm also exist for group-
like objects such as the progression [N], and also for measure-preserving
systems (where they are known as the Gowers-Host-Kra uniformity semi-
norms, see [HoKr∈005] for more discussion). In this section we will focus
on the basic properties of these norms; the deepest fact about them, known
as the inverse conjecturefor these norms, will be discussed in later sections.

∞.3.∞. L⟩\ear Four⟩er a\alys⟩s does \ot ⌋o\trol le\}t⟨ {our √ro-
}ress⟩o\s.Let A ˆ Z=NZ be a subset of a cyclic group Z=NZ with density
jAj = ◦N; we think of 0 < ◦ ˇ 1 as being ﬁxed, and N as being very large
or going oﬀ to inﬁnity.

For each ∥  1, consider the number

(1.23) f(\∅ r) 2 Z=NZ  Z=NZ : \∅ \ + r∅ : : : ∅ \+ (∥ Γ 1)r2 Ag

of ∥-term arithmetic progressions in A (including degenerate progressions).
Heuristically, this expression should typically be close to ◦k N 2. Since there
are N 2 pairs (\∅ r) and we would expect each pair to have a ◦k “probability”
that \∅ \+r∅ : : : ∅ \+(∥ Γ 1)rsimultaneously lie in A. Indeed, using standard
probabilistic tools such as Cherno 's inequality, it is not diﬃcult to justify
this heuristic with probability asymptotically close to 1 in the case that A
is a randomly chosen set of the given density.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

48 1. Higher order Fourier analysis

Let’s see how this heuristic holds up for small values of ∥. For ∥ = 0∅1∅2,
this prediction is exactly accurate (with no error term) for any set A with
cardinality ◦N; no randomness hypothesis of any sort is required. For ∥ = 3,
we see from (1.17) and the observation that ˆ1A(0) = ◦ that (1.23) is given
by the formula
 N 2
 0

@ ◦
3 + X

∼2Z=N Z:∼6=0
ˆ1A(∼)
2ˆ1A( 2∼ )

1

A :

Let us informally say that A is Fourier-√seudorandomif one has

sup
∼2Z=N Z:∼6=0
jˆ1A(∼)j = o(1)

where o(1) is a quantity that goes to zero as N ω 1. Then from applying
Plancherel’s formula and Cauchy-Schwarz as in the previous sections, we see
that the number of three-term arithmetic progressions is

N 2(◦
3 + o(1)):

Thus we see that the Fourier-pseudorandomness hypothesis allows us to
count three-term arithmetic progressions almost exactly.

On the other hand, without the Fourier-pseudorandomness hypothesis,
the count (1.23) can be signiﬁcantly diﬀerent from ◦3N 2. For instance, if A
is an interval A = [◦N], then it is not hard to see that (1.23) is comparable
to ◦2N 2 rather than ◦3N 2; the point is that with a set as structured as an
interval, once \ and \ + rlie in A, there is already a very strong chance
that \ + 2rlies in A also. In the other direction, a construction of Behrend
(mentioned in the previous sections) shows the quantity (1.23) can in fact
dip below ◦C N 2 for any ﬁxed C (and in fact one can be as small as ◦
⌋ log 1
N 2

for some absolute constant ⌋ > 0).

Now we consider the ∥ = 4 case of (1.23), which counts four-term pro-
gressions. Here, it turns out that Fourier-pseudorandomness is insuﬃcient;
it is possible for the quantity (1.23) to be signiﬁcantly larger or smaller than
◦4N 2 even if A is pseudorandom, as was observed by Gowers [Go∞99∀] (with
a closely related observation in the context of ergodic theory by Furstenberg
[Fu∞99′]).

E§erc⟩se ∞.3.4.Let  be an irrational real number, let 0 < ◦ < 1, and let
A := f\ 2 [N] : 0  f\ 2g  ◦g. Show that A is Fourier-pseudorandom
(keeping  and ◦ ﬁxed and letting N ω 1). ( Hint: One can use Exercise
1.1.21 to show that sums of the form E \2[N ]e(∥\2)e(∼\) cannot be large.)

E§erc⟩se ∞.3.5.Continuing the previous exercise, show that the expression
(1.23) for ∥ = 4 is equal to (⌋◦3 + o(1))N 2 as N ω 1, for some absolute
constant ⌋ > 0, if ◦ > 0 is suﬃciently small. (Hint: ﬁrst show, using

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.3. Linear patterns 49

the machinery in Section 1.1, that the two-dimensional sequence (\∅ r) ↦→
(\2∅ (\ + r)2∅ (\ + 2r)2∅ (\ + 3r)2) mod Z4 is asymptotically equidis-
tributed in the torus {(§ 1∅ §2∅ §3∅ §4) ∈ T 4 : § 1 − 3§ 2 + 3§ 3 − § 4 = 0}.)

The above exercises show that a Fourier-pseudorandom set can have
a four-term progression count (1.23) signiﬁcantly larger than ◦4N. One
can also make the count signiﬁcantly smaller than ◦4N (an observation of
Gowers, discussed at [Wo]), but this requires more work.

Exercise 1.3.6.Let 0 < ◦ < 1. Show that there exists a function { : T 2 →
[0∅1] with R

T {(§∅ y ) dy = ◦ for all § ∈ T, such that the expression

(1.24) Z

V {(§ 1∅ y 1) : : : {(§ 4∅ y 4)

is strictly less than ◦4, where V ≤ (T 2)4 is the subspace of quadruplets
((§ 1∅ y 1)∅ : : : ∅(§ 4∅ y 4)) such that § 1∅ : : : ∅ §4 is in arithmetic progression (i.e.
§ i = § + ⟩rfor some §∅ r∈ T) and the y 1∅ : : : ∅ y4 obey the constraint

y 1 − 3y 2 + 3y 3 − y 4 = 0:

(Hint: Take { of the form

{(§∅ y ) := ◦ + "({1(§ ) cos(2≈y ) + {3(§) cos(6 ≈y ))

where " > 0 is a small number, and {1∅ {3 are carefully chosen to make the
"2 term in (1.24) negative.)

Exercise 1.3.7.Show that there exists an absolute constant ⌋ > 0 such
that for all suﬃciently small ◦ > 0 and suﬃciently large N (depending on
◦) and a set A ⊂ [N] with |A| ≥ ◦N, such that (1.23) with ∥ = 4 is less
than ◦4+cN 2. (Hint: take ◦ ∼ 2 m for some m ≥ 1, and let A be a random
subset of [N] with each element \ of [N] lying in A with an independent
probability of mY

j=1 {(j\ mod 1∅ j\ 2 mod 1)∅

where { is the function in the previous exercise (with ◦ = 1=2), and1∅ : : : ∅ m
are real numbers which are linearly independent over Z modulo 1.)

1.3.2. The 100% case. Now we consider the question of counting more
general linear (or aﬃne) patterns than arithmetic progressions. A reasonably
general setting is to count patterns of the form

Ψ(~§) := (  1(~§)∅ : : : ∅  t(~§))

in a subset A of a ﬁnite abelian group G (e.g. a cyclic group G = Z=NZ),
where ~§ = (§ 1∅ : : : ∅ §d) ∈ G d, and the  1∅ : : : ∅  t : G d → G are aﬃne-linear

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

50 1. Higher order Fourier analysis

forms
  ⟩(§ 1∅ : : : ∅ §d ) = ⌋⟩ +
 dX

| =1 ⌋⟩∅|§ |

for some ﬁxed integers ⌋⟩∅ ⌋⟩∅| 2 Z. To avoid degeneracies, we will assume
that all the  ⟩ are surjective (or equilently, that the ⌋⟩∅1∅ : : : ∅ ⌋⟩∅d do not have
a common factor that divides the order of G). This count would then be
given by jGj d ΛΨ(1A∅ : : : ∅1A)

where ΛΨ is the d-linear form

ΛΨ({1∅ : : : ∅ {d ) := E~§2G d{1( 1(~§)) : : : {t( t(~§)):

For instance, the task of counting arithmetic progressions \∅ \ + r∅ : : : ∅ \+
(∥   1)rcorresponds to the case d = 2∅ t= ∥, and  ⟩(§ 1∅ §2) := § 1 +(⟩  1)§ 2.

We have the trivial bound

(1.25) jΛΨ({1∅ : : : ∅ {t)j ˇ k{ 1kL1 (G) : : :k{tkL1 (G)

where k{ kL1 (G) := sup
§2G j{(§)j:

Remark 1.3.1. One can replace the L1 norm on {⟩ in (1.25) with an L√i
norm for various values of √1∅ : : : ∅ √t. The set of all admissible √1∅ : : : ∅ √tis de-
scribed by the Brascamp-Lieb inequality, see for instance [BeCaChTa2008]
for further discussion. We will not need these variants of (1.25).

Improving this trivial bound turns out to be a key step in the theory
of counting general linear patterns. In particular, it turns out that for any
" > 0, one usually has

jΛΨ({1∅ : : : ∅ {t)j < "k{1kL1 (G) : : :k{tkL1 (G)

except when {1∅ : : : ∅ {t take a very special form (or at least correlate with
functions of a very special form, such as linear or higher order characters).

To reiterate: the key to the subject is to understand the inverse problem
of characterising those functions {1∅ : : : ∅ {d for which one has

jΛΨ({1∅ : : : ∅ {t)j  "k{1kL1 (G) : : :k{tkL1 (G) :

This problem is of most interest (and the most diﬃcult) in the “1% world”
when " is small (e.g. " = 0:01), but it is also instructive to consider the
simpler cases of the “99% world” when " is very close to one (e.g. " = 0:99),
or the “100% world” when " is exactly equal to one. In these model cases
one can use additional techniques (error-correction and similar techniques
(often of a theoretical computer science ﬂavour) in the 99% world, or exact
algebraic manipulation in the 100% world) to understand this expression.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.3. Linear patterns 51

Let us thus begin with analysing the 100% situation. Speciﬁcally, we
assume that we are given functions {∞∅ : : : ∅ {t 2 L1 (G) with

jΛ	({∞∅ : : : ∅ {t)j = k{∞kL1 (G): : :k{tkL1 (G)

and wish to classify the functions {∞∅ : : : ∅ {t as best we can. We will normalise
all the norms on the right-hand side to be one, thus j{i(§)j  1 for all § 2 G
and ⟩ = 1∅ : : : ∅ t, and

(1.26) jΛ	({∞∅ : : : ∅ {t)j = 1:

By the triangle inequality, we conclude that

Λ	(j{∞j∅ : : : ∅j{tj)  1:

On the other hand, we have the crude bound

Λ	(j{∞j∅ : : : ∅j{tj)  1:

Thus equality occurs, which (by the surjectivity hypothesis on all the  i)
shows that j{i(§)j = 1 for all § 2 G and ⟩ = 1∅ : : : ∅ t. Thus we may write
{i(§) = e(˚i(§)) for some phase functions ˚i : G ω R=Z. We then have

Λ	({∞∅ : : : ∅ {t) = E~x2G de(
 tX

i=∞˚i( i(~§)))

and so from (1.26) one has the equation

(1.27)
 tX

i=∞˚i( i(~§)) = ⌋

for all ~§ 2 G d and some constant ⌋.

So the problem now reduces to the algebraic problem of solving func-
tional equations such as (1.27). To illustrate this type of problem, let us
consider a simple case when d = 2∅ t= 3 and

 ∞(§∅ y ) = §;  ∈(§∅ y ) = y ;  3(§∅ y ) = § + y

in which case we are trying to understand solutions ˚∞∅ ˚∈∅ ˚3: G ω R=Zto
the functional equation

(1.28) ˚∞(§) + ˚∈(y ) + ˚3(§ + y ) = ⌋:

This equation involves three unknown functions ˚∞∅ ˚∈∅ ˚3. But we can elim-
inate two of the functions by taking discrete derivatives. To motivate this
idea, let us temporarily assume that G is the real line R rather than a
ﬁnite group, and that the functions ˚∞∅ ˚∈∅ ˚3 are smooth. If we then ap-
ply the partial derivative operator @x to the above functional equation, one
eliminates ˚∈ and obtains
 ˚
0
∞(§) + ˚
0
3(§ + y ) = 0;

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

52 1. Higher order Fourier analysis

applying @y then eliminates ˚1 and leaves us with

˚
00
3(§ + y ) = 0∅

thus ˚00
3 vanishes identically; we can integrate this twice to conclude that ˚3
is a linear function of its input,

˚3(§ ) = a3§ + ⌊3

for some constants a3∅ ⌊3 2 R. A similar argument (using the partial deriva-
tive operator @§   @y to eliminate ˚3, or by applying change of variables such
as (§∅ z ) := (§∅ § + y )) shows that ˚1(§) = a1§ + ⌊1 and ˚2(§ ) = a2§ + ⌊2
for some additional constants a1∅ ⌊1∅ a2∅ ⌊2. Finally, by returning to (1.28)
and comparing coeﬃcients we obtain the additional compatibility condition
a3 =  a 1 =  a 2, which one then easily veriﬁes to completely describe all
possible solutions to this equation in the case of smooth functions on R.

Returning now to the discrete world, we mimic the continuous operation
of a partial derivative by introducing diﬀerence operators

@⟨ ˚(§) := ˚(§ + ⟨)   ˚(§)

for ⟨ 2 G. If we diﬀerence (1.28) in the § variable by an arbitrary shift
⟨ 2 G by replacing § by § + ⟨ and then subtracting, we eliminate ˚2 and
obtain (@⟨ ˚1)(§) + (@⟨ ˚3)(§ + y ) = 0;
if we then diﬀerence in the y variable by a second arbitrary shift ∥ 2 G, one
obtains (@∥ @⟨ ˚3)(§ + y ) = 0
for all §∅ y∅ ⟨∅ ∥ 2 G; in particular, @∥ @⟨ ˚3  0 for all ∥∅ ⟨ 2 G. Such
functions are aﬃne-linear:

Exercise 1.3.8. Let ˚: G ! R=Z be a function. Show that @∥ @⟨ ˚ = 0 if
and only if one has ˚(§) = a(§) + ⌊ for some ⌊ 2 G and some homomor-
phism a: G ! R=Z. Conclude that the solutions to (1.28) are given by the
form ˚⟩(§) = a⟩(§) + ⌊⟩, where ⌊1∅ ⌊2∅ ⌊3 2 G and a1∅ a2∅ a3 : G ! R=Z are
homomorphisms with a1 =  a 2 =  a 3.

Having solved the functional equation (1.28), let us now look at an equa-
tion related to four term arithmetic progressions, namely

(1.29) ˚1(§) + ˚2(§ + y ) + ˚3(§ + 2y ) + ˚4(§ + 3y ) = ⌋

for all §∅ y 2 G, some constant ⌋ 2 G, and some functions ˚1∅ ˚2∅ ˚3∅ ˚4 : G !
R=Z. We will try to isolate ˚4 by using discrete derivatives as before to
eliminate the other functions. Firstly, we diﬀerentiate in the y direction by
an arbitrary shift ⟨ 2 G, leading to

(@⟨ ˚2)(§ + y ) + (@2⟨ ˚3)(§ + 2y ) + (@3⟨ ˚4)(§ + 3y ) = 0:

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.3. Linear patterns 53

In preparation for then eliminating ˚∈, we shift § backwards by y , obtaining

(@h˚∈)(§) + (@∈h˚3)(§ + y ) + (@3h˚4)(§ + 2y ) = 0:

Diﬀerentiating in the y direction by another arbitrary shift ∥ 2 G, we obtain

(@k@∈h˚3)(§ + y ) + (@∈k@3h˚4)(§ + 2y ) = 0:

We shift § backwards by y again:

(@k@∈h˚3)(§) + (@∈k@3h˚4)(§ + y ) = 0:

One ﬁnal diﬀerentiation in y by an arbitrary shift l2 G gives

(@l@∈k@3h˚4)(§ + y ) = 0:

For simplicity, we now make the assumption that the order jGj of G is not
divisible by either 2 or 3, so that the homomorphisms ∥ 7ω 2∥ and ⟨ 7ω 3⟨
are automorphisms of G. We conclude that

(1.30) @l@k@h˚4 0

for all l∅ ∥∅ ⟨. Such functions will be calledquadratic functions from G to
R=Z, thus ˚4 is quadratic. A similar argument shows that ˚∞∅ ˚∈∅ ˚3 are
quadratic.

Just as (aﬃne-)linear functions can be completely described in terms of
homomorphisms, quadratic functions can be described in terms of bilinear
forms, as long as one avoids the characteristic 2 case:

Exercise 1.3.9. Let G be a ﬁnite abelian group with jGj not divisible
by 2. Show that a map ˚: G ω R=Z is quadratic if and only one has a
representation of the form

˚(§) = B (§∅ §) + L(§) + ⌋

where ⌋ 2 R=Z, L : G ω R=Z is a homomorphism, and B : G  G ω
R=Z is a symmetric bihomomorphism (i.e. B (§∅ y ) = B (y∅ § ), and B is
a homomorphism in each of §∅ y individually (holding the other variable
ﬁxed)). (Hint: Heuristically, one should set B (⟨∅ ∥) := ∞
∈@h@k˚(§), but there
is a diﬃculty because the operation of dividing by ∞
∈ is not well-deﬁned on
R=Z. It is, however, well-deﬁned on jGjt⟨ roots of unity, thanks to jGj not
being divisible by two. Once B has been constructed, subtract it oﬀ and use
Exercise 1.3.8.) What goes wrong when jGj is divisible by 2?

Exercise 1.3.10. Show that when jGj is not divisible by 2∅3, that the
complete solution to (1.29) is given by

˚i(§) = B i(§∅ §) + Li(§) + ⌋i

for ⟩ = 1∅2∅3∅4, ⌋i 2 R=Z, homomorphisms Li : G ω R=Z, and symmetric
bihomomorphisms B i : G  G ω R=Z with B ∈ =  3B ∞∅ B3 = 3B ∞∅ B4 =
 B ∞and L∞+ L∈ + L3 + L4= L∈ + 2L3 + 3L4= 0.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

54 1. Higher order Fourier analysis

E§er⌋⟩se ∞.3.∞∞.Obtain a complete solution to the functional equation
(1.29) in the case when |G| is allowed to be divisible by 2 or 3. (This is an
open-ended and surprisingly tricky exercise; it of course depends on what
one is willing to call a “solution” to the problem. Use your own judgement.)

E§er⌋⟩se ∞.3.∞∈.Call a map ˚: G → R=Za polynomial of degree≤ d if
one has @h 1 : : : @h d+1 ˚(x) = 0 for allx; h; : : : ; hd〉 ∈ G. Show that if k ≥ 1
and ˚; : : : ; ˚k obey the functional equation

˚(x) + ˚2(x + y) + · · · + ˚k (x + (k − 1)y) = c

and |G| is not divisible by any integer between 2 and k − 1, then ˚; : : : ; ˚k
are polynomials of degree ≤ k − 2.

We are now ready to turn to the general case of solving equations of
the form (1.27). We relied on two main tricks to solve these equations:
diﬀerentiation, and change of variables. When solving an equation such as
(1.29), we alternated these two tricks in turn. To handle the general case,
it is more convenient to rearrange the argument by doing all the change of
variables in advance. For instance, another way to solve (1.29) is to ﬁrst
make the (non-injective) change of variables

(x; y) := (b+ 2c + 3d;−a − b− c − d)

for arbitrary a; b; c; d∈ G, so that

(x; x + y; x+ 2y; x+ 3y) = (b+ 2c+ 3d;−a + c+ 2d;−2a − b+ d;−3a − 2b− c)

and (1.29) becomes
(1.31)
˚(b+ 2c+ 3d) + ˚2(−a + c+ 2d) + ˚3(−2a − b+ d) + ˚4(−3a − 2b− c) = const

for all a; b; c; d∈ G. The point of performing this change of variables is that
while the ˚4 term (for instance) involves all the three variables a; b; c, the
remaining terms only depend on two of the a; b; cat a time. If we now pick
h; k; l ∈ G arbitrarily, and then diﬀerentiate in the a; b; c variables by the
shifts h; k; l respectively, then we eliminate the ˚; ˚2; ˚3 terms and arrive
at (@ l @ 2k @ 3h ˚4)(−3a − 2b− c) = 0
which soon places us back at (1.30) (assuming as before that |G| is not
divisible by 2 or 3).

Now we can do the general case, once we put in place a deﬁnition (from
[GrTa∈0∞0]):

De\⟩t⟩o\ ∞.3.∈(Cauchy-Schwarz complexity).A system   ; : : : ;   t : Gd →
G of aﬃne-linear forms (with linear coeﬃcients in Z) have Cauchy-Schwarz
complexity at mosts if, for every 1 ≤ i ≤ t, one can partition [t]\{i} into
s + 1 classes (some of which may be empty), such that   i does not lie in

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.3. Linear patterns 55

the aﬃne-linear span (over Q) of the forms in any of these classes. The
Cau⌋⟨y-S⌋⟨warz ⌋om√le§⟩ty of a system is deﬁned to be the least such s
with this property, or 1 if no such s exists.

The adjective “Cauchy-Schwarz” (introduced by Gowers and Wolf [GoWo∈0∞0])
may be puzzling at present, but will be motivated later.

This is a somewhat strange deﬁnition to come to grips with at ﬁrst, so
we illustrate it with some examples. The system of forms x; y; x + y is of
complexity 1; given any form here, such as y, one can partition the remaining
forms into two classes, namely fxg and fx + yg, such that y is not in the
aﬃne-linear span of either. On the other hand, as y is in the aﬃne linear
span of fx; x + yg, the Cauchy-Schwarz complexity is not zero.

E§er⌋⟩se ∞.3.∞3.Show that for any k  2, the system of forms x; x +
y; : : : ; x+ (k   1)y has complexity k   2.

E§er⌋⟩se ∞.3.∞4.Show that a system of non-constant forms has ﬁnite
Cauchy-Schwarz complexity if and only if no form is an aﬃne-linear combi-
nation of another.

There is an equivalent way to formulate the notion of Cauchy-Schwarz
complexity, in the spirit of the change of variables mentioned earlier. Deﬁne
the ⌋⟨ara⌋ter⟩st⟩⌋of a ﬁnite abelian group G to be the least order of a
non-identity element.

Pro√os⟩t⟩o\ ∞.3.3(Equivalent formulation of Cauchy-Schwarz complex-
ity).Let  1; : : : ;   t : Gd ω G ⌊e a system o{ a◦\e-l⟩\ear {orms. Su√√ose
t⟨at t⟨e ⌋⟨ara⌋ter⟩st⟩⌋ o{G ⟩s su◦⌋⟩e\tly lar}e de√e\d⟩\} o\ t⟨e ⌋oe◦⌋⟩e\ts
o{   1; : : : ;   t. T⟨e\  1; : : : ;   t ⟨as Cau⌋⟨y-S⌋⟨warz ⌋om√le§⟩ty at mosts ⟩{
a\d o\ly ⟩{, {or ea⌋⟨1  i  t, o\e ⌋a\ \d a l⟩\ear ⌋⟨a\}e o{ var⟩a⌊les~x =
Li(y1; : : : ; ys+1 ; z1; : : : ; zm) overQ su⌋⟨ t⟨at t⟨e {orm˙  i(Li(y1; : : : ; ys+1 ; z1; : : : ; zm))
⟨as \o\-zero y1; : : : ; ys+1 ⌋oe◦⌋⟩e\ts, ⌊ut all t⟨e ot⟨er {orms˙  j (Li(y1; : : : ; ys+1 ; z1; : : : ; zm))
w⟩t⟨j 6=i ⟨ave at least o\e va\⟩s⟨⟩\}y1; : : : ; ys+1 ⌋oe◦⌋⟩e\t, a\d ˙  i : Qd ω
Q ⟩s t⟨e l⟩\ear {orm ⟩\du⌋ed ⌊y t⟨e ⟩\te}er ⌋oe◦⌋⟩e\ts o{  i.

Proo{.To show the “only if” part, observe that if 1  i  t and Li is as
above, then we can partition the   j , j 6=i into s + 1 classes depending on
which yk coeﬃcient vanishes for k = 1; : : : ; s + 1 (breaking ties arbitrarily),
and then   i is not representable as an aﬃne-linear combination of the forms
from any of these classes (here we use the large characteristic hypothesis).
Conversely, suppose   1; : : : ;   t has Cauchy-Schwarz complexity at most s,
and let 1  i  s. We can then partition the j 6=i into s + 1 classes
A1; : : : ;As+1 , such that   i cannot be expressed as an aﬃne-linear combina-
tion of the   j from Ak for any 1  k  s + 1. By duality, one can then ﬁnd

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

56 1. Higher order Fourier analysis

vectors v∥ 2 Qd for each 1 ˇ ∥ ˇ s + 1 such that ˙ ⟩ does not annihilate v∥ ,
but all the ˙ | from A∥ do. If we then set

L⟩(y 1∅ : : : ∅ ys+1 ∅ z 1∅ : : : ∅ zd ) := (z 1∅ : : : ∅ zd ) + y 1v1 + ∆ ∆ ∆+ y s+1 vs+1

then we obtain the claim. 

Exercise 1.3.15.Let  1∅ : : : ∅  t: G d ! G be a system of aﬃne-linear forms
with Cauchy-Schwarz complexity at most s, and suppose that the equation
(1.27) holds for some ﬁnite abelian group G and some ˚1∅ : : : ∅ ˚t: G !
R=Z. Suppose also that the characteristic ofG is suﬃciently large depending
on the coeﬃcients of  1∅ : : : ∅  t. Conclude that all of the ˚1∅ : : : ∅ ˚t are
polynomials of degree ˇ t.

It turns out that this result is not quite best possible. Deﬁne the true
complexityof a system of aﬃne-linear forms  1∅ : : : ∅  t: G d ! G to be the
largest s such that the powers ˙ s
1∅ : : : ∅˙ s
t : Qd ! Q are linearly independent
over Q.

Exercise 1.3.16.Show that the true complexity is always less than or equal
to the Cauchy-Schwarz complexity, and give an example to show that strict
inequality can occur. Also, show that the true complexity is ﬁnite if and
only if the Cauchy-Schwarz complexity is ﬁnite.

Exercise 1.3.17.Show that Exercise 1.3.15 continues to hold if Cauchy-
Schwarz complexity is replaced by true complexity. (Hint. ﬁrst understand
the cyclic case G = Z=NZ, and use Exercise 1.3.15 to reduce to the case
when all the ˚⟩ are polynomials of bounded degree. The main point is to
use a “Lefschetz principle” to lift statements in Z=NZ to a characteristic
zero ﬁeld such as Q.) Show that the true complexity cannot be replaced by
any smaller quantity.

See [GoWo2010] for further discussion of the relationship between Cauchy-
Schwarz complexity and true complexity.

1.3.3. The Gowers uniformity norms. In the previous section, we saw
that equality in the trivial inequality (1.25) only occurred when the functions
{1∅ : : : ∅ {t were of the form {⟩ = e(˚⟩) for some polynomials ˚⟩ of degree at
most s, where s was the true complexity (or Cauchy-Schwarz complexity) of
the system  1∅ : : : ∅  t. Another way of phrasing this latter fact is that one
has the identity ∆⟨  : : :∆⟨ s〉{⟩(§) = 1

for all ⟨ 1∅ : : : ∅ ⟨s+1 ∅ § 2 G, where ∆ ⟨ is the multiplicative derivative

∆⟨ {(§) := {(§ + ⟨) {(§ ):

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.3. Linear patterns 57

This phenomenon extends beyond the “100% world” of exact equalities.
For any { : G → C and d ≥ 1, we deﬁne the Gowers uniformity norm
∥{∥U d(G)by the formula

(1.32) ∥{∥U d(G):= (Eh ;:::;hd;x2G ∆h  : : :∆h d{(§)) 1=2d;

note that this is equivalent to (1.22). Using the identity

Eh;x 2G ∆h {(§) = |Ex2G {(§)| 2

we easily verify that the expectation in the deﬁnition of (1.32) is a non-
negative real. We also have the recursive formula

(1.33) ∥{∥U d(G):= (Eh2G ∥∆h {∥2d 
U d  (G))
1=2d

for all d ≥ 1.

The U 1 norm essentially just the mean:

(1.34) ∥{∥U (G)= |Ex2G {(§ )|:

As such, it is actually a seminormrather than a norm.

The U 2 norm can be computed in terms of the Fourier transform:

Exercise 1.3.18 (Fourier representation of U 2). Deﬁne the Pontryagin dual
ˆG of a ﬁnite abelian group G to be the space of all homomorphisms ∼: G →
R=Z. For each function { : G → C, deﬁne the Fourier transform ˆ{ : ˆG → C
by the formula ˆ{(∼) := Ex2G {(§ )e(−∼(§)). Establish the identity

∥{∥U 2(G)= ∥ ˆ{∥` 4(^G):= (X

˘2 ^G | ˆ{(∼)|
4)
1=4:

In particular, the U 2 norm is a genuine norm (thanks to the norm prop-
erties of `4(G), and the injectivity of the Fourier transform).

For the higher Gowers norms, there is not nearly as nice a formula known
in terms of things like the Fourier transform, and it is not immediately obvi-
ous that these are indeed norms. But this can be established by introducing
the more general Gowers inner product

⟨({! )! 2f0;1gd⟩U d(G):= Ex;h ;:::;hd2G Y

! ;:::;! d2f0;1gd

C! ++! d{! ;:::;! d(§ + →1⟨ 1 + · · · + →d⟨ d)

for any 2d-tuple ({! )! 2f0;1gd of functions {! : G → C, thus in particular

⟨({)! 2f0;1gd⟩U d(G)= ∥{∥
2d
U d(G):

The relationship between the Gowers inner product and the Gowers unifor-
mity norm is analogous to that between a Hilbert space inner product and

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

58 1. Higher order Fourier analysis

the Hilbert space norm. In particular, we have the following analogue of the
Cauchy-Schwarz inequality:

E§er⌋⟩se ∞.3.∞9(Cauchy-Schwarz-Gowers inequality).For any tuple ({! )! 2f0;1g d
of functions {! : G ω C, use the Cauchy-Schwarz inequality to show that

jh({! )! 2f0;1g diUd(G)j  ∏

j =0;1 jh({ˇ i;j (! ))! 2f0;1g diUd(G)j
1=2

for all 1  ⟩  d, where for | = 0∅1 and → 2 f 0∅1gd, ≈i;j (→) 2 f 0∅1gd

is formed from → by replacing the ⟩th coordinate with | . Iterate this to
conclude that
 jh({! )! 2f0;1g diUd(G)j  ∏

! 2f0;1g d k{! kUd(G):

Then use this to conclude the monotonicity formula

k{kUd(G)  k{ kUd+1(G)
for all d  1, and the triangle inequality

k{ + }kUd(G)  k{ kUd(G) + k}kUd(G)
for all {∅ }: G ω C. ( Hint: For the latter inequality, raise both sides to the
power 2d and expand the left-hand side.) Conclude in particular that the
U d(G) norms are indeed norms for all d  2.

The Gowers uniformity norms can be viewed as a quantitative measure
of how well a given function behaves like a polynomial. One piece of evidence
in this direction is:

E§er⌋⟩se ∞.3.∈0(Inverse conjecture for the Gowers norm, 100% case).
Let { : G ω C be such that k{kL∞ (G) = 1, and let s  0. Show that
k{kUs +1(G)  1, with equality if and only if { = e(˚) for some polynomial
˚: G ω R=Zof degree at most s.

The problem of classifying smaller values of k{kUs+1(G) is signiﬁcantly
more diﬃcult, and will be discussed in later sections.

E§er⌋⟩se ∞.3.∈∞(Polynomial phase invariance).If { : G ω C is a func-
tion and ˚: G ω R=Z is a polynomial of degree at most s, show that
ke(˚){kUs+1(G) = k{kUs+1(G). Conclude in particular that

sup
˚ jE x2G e(˚(§)){(§)j  k{kUs+1(G)

where ˚ ranges over polynomials of degree at most s.

The main utility for the Gowers norms in this subject comes from the
fact that they control many other expressions of interest. Here is a basic
example:

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.4. Equidistribution in ﬁnite ﬁelds 59

E§er⌋⟩se ∞.3.∈∈.Let { : G ! C be a function, and for each 1 ˇ ⟩ ˇ
s + 1, let }i : G s+1 ! C be a function bounded in magnitude by 1 which
is independent of the ⟩th coordinate of G s+1 . Let a1∅ : : : ∅ as+1 be non-zero
integers, and suppose that the characteristic of G exceeds the magnitude of
any of the ai. Show that

jE x1,...,xs+1 2G{(a1§ 1 + ∆ ∆ ∆+ as+1 § s+1 )
 s+1Y

i=1 }i(§ 1∅ : : : ∅ §s+1 )j

ˇ k{ kU s+1 (G):
Hint: induct on s and use (1.33) and the Cauchy-Schwarz inequality.

This gives us an analogue of Exercise 1.3.15:

E§er⌋⟩se ∞.3.∈3(Generalised von Neumann inequality).Let Ψ = ( 1∅ : : : ∅  t)
be a collection of aﬃne-linear forms  i : G d ! G with Cauchy-Schwarz com-
plexity s. If the characteristic of G is suﬃciently large depending on the
linear coeﬃcients of  1∅ : : : ∅  t, show that one has the bound

jΛ	 ({1∅ : : : ∅ {t)j ˇ inf
1it k{ikU s+1 (G)

whenever {1∅ : : : ∅ {t : G ! C are bounded in magnitude by one.

Conclude in particular that if A is a subset of G with jAj = ◦jGj, then

Λ	 (1A∅ : : : ∅1A) = ◦
t + Ot(k1A Γ ◦kU s+1 (G)):

From the above inequality, we see that if A has some positive den-
sity ◦ > 0 but has much fewer than ◦tN d=2 (say) patterns of the form
 1(~§)∅ : : : ∅  t(~§) with ~§ 2 G d, then we have

k1A Γ ◦kU s+1 (G) ˛t,δ 1:

This is the initial motivation for studying inverse theoremsfor the Gowers
norms, which give necessary conditions for a (bounded) function to have
large U s+1 (G) norm. This will be a focus of subsequent sections.

∞.4. Equ⟩d⟩str⟩but⟩o\ o{ poly\om⟩als over \⟩te elds

In the previous sections, we have focused mostly on the equidistribution or
linear patterns on a subset of the integers Z, and in particular on intervals
[N]. The integers are of course a very important domain to study in addi-
tive combinatorics; but there are also other fundamental model examples of
domains to study. One of these is that of a vector space V over a ﬁnite ﬁeld
F = Fp of prime order. Such domains are of interest in computer science
(particularly when √= 2) and also in number theory; but they also serve as
an important simpliﬁed dyadic modelfor the integers. See [Ta∈008, x1.6]
or [Gr∈005a] for further discussion of this point.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

60 1. Higher order Fourier analysis

The additive combinatorics of the integers Z, and of vector spaces V
over ﬁnite ﬁelds, are analogous, but not quite identical. For instance, the
analogue of an arithmetic progression in Z is a subspace of V . In many cases,
the ﬁnite ﬁeld theory is a little bit simpler than the integer theory; for in-
stance, subspaces are closed under addition, whereas arithmetic progressions
are only “almost” closed9 under addition in various senses. However, there
are some ways in which the integers are better behaved. For instance, be-
cause the integers can be generated by a single generator, a homomorphism
from Z to some other group G can be described by a single group element
}: \ 7ω }n . However, to specify a homomorphism from a vector space V
to G one would need to specify one group element for each dimension of
V . Thus we see that there is a tradeoﬀ when passing from Z (or [N]) to a
vector space model; one gains a bounded torsion property, at the expense10

of conceding the bounded generation property.

The starting point for this text (Section 1.1) was the study of equidis-
tribution of polynomials P : Z ω R=Z from the integers to the unit cir-
cle. We now turn to the parallel theory of equidistribution of polynomials
P : V ω R=Z from vector spaces over ﬁnite ﬁelds to the unit circle. Ac-
tually, for simplicity we will mostly focus on the classicalcase, when the
polynomials in fact take values in the √th roots of unity (where √ is the
characteristic of the ﬁeld F = Fp). As it turns out, the non-classical case
is also of importance (particularly in low characteristic), but the theory is
more diﬃcult; see [Ta∈009, x1.12] for some further discussion.

∞.4.∞. Poly\om⟩als: ⌊as⟩⌋ t⟨eory.Throughout this section, V will be a
ﬁnite-dimensional vector space over a ﬁnite ﬁeld F = Fp of prime order √.

Recall from Section 1.3 that a function P : V ω R=Z is a function is a
polynomial of degree at mostd if

@h 1 : : : @h d+1P(§) = 0

for all §∅ ⟨ 1∅ : : : ∅ ⟨d+1 2 V , where @h P(§) := P(§ + ⟨)   P(§). As mentioned
in previous sections, this is equivalent to the assertion that the Gowers
uniformity norm ke(P)kU d+1(V ) = 1. The space of polynomials of degree
at most d will be denoted Polyd (V ω R=Z); it is clearly an additive
group. Note that a polynomial of degree zero is the same thing as a constant
function, thus Poly0 (V ω R=Z) R=Z.

An important special case of polynomials are the classical polynomials,
which take values in F (which we identify with the √th roots of unity in

9For instance, [N ] is closed under addition approximately half of the time.
10Of course, if one wants to deal with arbitrarily large domains, one has to concede one or the
other; the only additive groups that have both bounded torsion and boundedly many generators,
are bounded.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.4. Equidistribution in ﬁnite ﬁelds 61

R=Z in the obvious manner); the space of such polynomials of degree at
most d will be denoted Polyˇd (V ! F); this is clearly a vector space over
F. The classical polynomials have a familiar description, once we use a basis
to identify V with Fn:

E§er⌋⟩se ∞.4.∞.Let P : Fn ! F be a function, and d  0 be an integer.
Show that P is a (classical) polynomial of degree at most d if and only if
one has a representation of the form

P(§ 1∅ : : : ∅ §n) := X

i,...,in0:i +∆∆∆+inˇd ⌋i,...,in§ i
1 : : : §
in
n

for some coeﬃcients ⌋i,...,in 2 F. Furthermore, show that we can restrict
the exponents ⟩1∅ : : : ∅ ⟩n to lie in the range f0∅ : : : ∅ √  1g, and that once one
does so, the representation is unique. (Hint: First establish the d = 1 case,
which can be done for instance by a dimension counting argument, and then
induct on dimension.)

E§er⌋⟩se ∞.4.∈.Show that the cardinality of Polyˇd (V ! F) is at most

√(
d〉dim(V)
d ), with equality if and only if d < √.

Now we study more general polynomials. A basic fact here is that mul-
tiplying a polynomial by the characteristic √lowers the degree:

Lemma ∞.4.∞.If P 2 Polyˇd (V ! R=Z), then√P2 Polyˇmax(dΓp+1,0) (V !
R=Z).

Proo{.Without loss of generality we may take d  √  1; an easy induction
on d then shows it suﬃces to verify the base case d = √  1. Our task is now
to show that √Pis constant, or equivalently that √∆eP = 0 for all e 2 V .

Fix e. The operator 1 + ∆e represents a shift by e. Since √e= 0, we
conclude that (1 + ∆e)pP = P. On the other hand, as P has degree at most
√  1, ∆p
eP = 0, and so
 ((1 + ∆e)
p   1   ∆p
e)P = 0:

Using the binomial formula, we can factorise the left-hand side as

(1 + √  1
2 ∆e +    + ∆pΓ2
e )(√∆eP) = 0:

The ﬁrst factor can be inverted by Neumann series since ∆e acts nilpotently
on polynomials. We conclude that √∆eP = 0 as required. ∗

E§er⌋⟩se ∞.4.3.Establish the identity
11

√(T
j   1) = ( 1) pΓ1 (T j   1)(T   1)(T 2   1) : : :(T pΓ1   1)

mod T p   1

11We thank Andrew Granville for showings us this argument.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

62 1. Higher order Fourier analysis

for an indeterminate T and any integer | , by testing on √t⟨ roots of unity.
Use this to give an alternate proof of Lemma 1.4.1.

This classiﬁes all polynomials in the high characteristic case √ > d:

Corollary 1.4.2. If √ > d, thenPolyˇd (V ω R=Z) = Polyˇd (V ω F) +
(R=Z). In other words, every polynomial of degree at mostd is the sum of
a classical polynomial and a constant.

The situation is more complicated in the low characteristic case √ d, in
which non-classical polynomials can occur (polynomials that are not simply
a classical polynomial up to constants). For instance, consider the function
P : F∈ ω R=Z deﬁned by P(0) = 0 and P(1) = 1=4. One easily veriﬁes that
this is a (non-classical) quadratic (i.e. a polynomial of degree at most 2),
but is clearly not a shifted version of a classical polynomial since its range
is not a shift of the second roots f0∅1=2g mod 1 of unity.

Exercise 1.4.4. Let P : F∈ ω R=Z be a function. Show that P is a poly-
nomial of degree at most d if and only if the range of P is a translate of the
(2d)t⟨ roots of unity (i.e. 2dP is constant).

For further discussion of non-classical polynomials, see [Ta2009, x1.12].
Henceforth we shall avoid this technical issue by restricting to the high
characteristic case √ > d(or equivalently, the low degree case d < √).

1.4.2. Equidistribution. Let us now consider the equidistribution theory
of a classical polynomial P : V ω F, where we think of F as being a ﬁxed
ﬁeld (in particular, √= O(1)), and the dimension of V as being very large; V
will play the role here that the interval [N] played in Section 1.1. This the-
ory is classical for linear and quadratic polynomials. The general theory was
studied ﬁrst in [GrTa2009] in the high characteristic case √ > d, and ex-
tended to the low characteristic case in [KaLo2008]; see also [HaSh2010],
[HaLo2010] for some recent reﬁnements. An analogous theory surely exists
for the non-classical case, although this is not currently in the literature.

The situation here is simpler because a classical polynomial can only
take √ values, so that in the equidistributed case one expects each value
to be obtained about jVj=√times. Inspired by this, let us call a classical
polynomial P ◦-equidistributedif one has

jf§ 2 V : P(§) = ag   jV j=√j ◦jVj

for all a 2 F.

Exercise 1.4.5. Show that this is equivalent to the notion of ◦-equidistribution
given in Section 1.1, if one gives F the metric induced from R=Z, and if one
is willing to modify ◦ by a multiplicative factor depending on √in the equiv-
alences.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.4. Equidistribution in ﬁnite ﬁelds 63

Before we study equidistribution in earnest, we ﬁrst give a classical es-
timate.

E§er⌋⟩se ∞.4.̸(Chevalley-Warning theorem).Let V be a ﬁnite dimensional
space, and let P : V ! F be a classical polynomial of degree less than
(√Γ 1) dim(V ). Show that P x2V P(§) = 0. ( Hint. Identify V with Fn for
some \ and apply Exercise 1.4.1. Use the fact that P x2F § i = 0 for all
1 ˇ ⟩ < √Γ 1, which can be deduced by using a change of variables § 7! ⌊§.)
If furthermore P has degree less than dim(V ), conclude that for every a 2 F,
that jf§ 2 V : P(§) = agj is a multiple of √. (Hint. Apply Fermat’s little
theorem to the quantity (P Γ a)p 1 .) In particular, if § 0 2 V , then there
exists at least one further § 2 V such that P(§) = P(§ 0).

If P has degree at most d and § 0 2 V , obtain the recurrence inequality

jf§ 2 V : P(§) = P(§ 0)gj ˛p;d jV j:

(Hint. normalise § 0 = 0, then average the previous claim over all subspaces
of V of a certain dimension.)

The above exercise goes some way towards establishing equidistribution,
by showing that every element in the image of P is attained a fairly large
number of times. But additional techniques will be needed (together with
additional hypotheses on P) in order to obtain full equidistribution. It will
be convenient to work in the ultralimit setting. Deﬁne a limit classical poly-
nomialP : V ! F on a limit ﬁnite-dimensional vector space V = Q ﬀ! ﬀ1 Vﬀ
of degree at most d to be an ultralimit of classical polynomials Pﬀ : Vﬀ ! F
of degree at most d (we keep F and d ﬁxed independently of ). We say
that a limit classical polynomial P is equidistributedif one has

jf§ 2 V : P(§) = agj = jV j=√+ o(jV j)

for all a 2 F, where the cardinalities here are of course limit cardinalities.

E§er⌋⟩se ∞.4.↦.Let V be a limit ﬁnite-dimensional vector space. Show that
a limit function P : V ! F is a limit classical polynomial of degree at most
d if and only if it is a classical polynomial of degree at most d (observing
here that every limit vector space is automatically a vector space).

E§er⌋⟩se ∞.4.8.Let P = limﬀ!ﬀ 1 Pﬀ be a limit classical polynomial.
Show that P is equidistributed if and only if, for every ◦ > 0, Pﬀ is ◦-
equidistributed for  suﬃciently close to 1 .

E§er⌋⟩se ∞.4.9.Let P : V ! F be a limit classical polynomial which is
linear (i.e. of degree at most 1). Show that P is equidistributed if and only
if P is non-constant.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

64 1. Higher order Fourier analysis

There is an analogue of the Weyl equidistribution criterion in this setting.
Call a limit function P : V → F biased if |Ex2V e(P (§))| ≫ 1, and unbiased
if Ex2V e(P (§)) = o(1), where we identify P(§ ) ∈ F with an element of R=Z.

Exercise 1.4.10 (Weyl equidistribution criterion). Let P : V → F be a
limit function. Show that P is equidistributed if and only if ∥P is unbiased
for all non-zero ∥ ∈ F.

Thus to understand the equidistribution of polynomials, it suﬃces to un-
derstand the size of exponential sums Ex2V e(P (§)). For linear polynomials,
this is an easy application of Fourier analysis:

Exercise 1.4.11. Let P : V → F be a polynomial of degree at most 1.
Show that |Ex2V e(P (§))| equals 1 if P is constant, and equals 0 if P is not
constant. (Note that this is completely consistent with the previous two
exercises.)

Next, we turn attention to the quadratic case. Here, we can use the
Weyl diﬀerencing trick, which we phrase as an identity

(1.35) |Ex2V {(§)| 2 = Eh2V Ex2V ∆h {(§)

for any ﬁnite vector space V and function { : V → C, where ∆h {(§) :=
{(§ + ⟨) {(§ ) is the multiplicative derivative. Taking ultralimits, we see that
the identity also holds for limit functions on limit ﬁnite dimensional vector
spaces. In particular, we have

(1.36) |Ex2V e(P (§))| 2 = Eh2V Ex2V e(@h P(§))

for any limit function P : V → F on a limit ﬁnite dimensional space.

If P is quadratic, then @h P is linear. Applying (1.4.11), we conclude
that if P is biased, then @h P must be constant for ≫ |V | values of ⟨ ∈ V .

On the other hand, by using the cocycle identity

@h+kP(§) = @h P(§ + ∥) + @k P(§)

we see that the set of ⟨ ∈ V for which @h P is constant is a limit subspace
of W. On that subspace, P is then linear; passing to a codimension one
subspace W 0 of W, P is then constant on W 0. As @h P is linear for every
⟨, P is then linear on each coset ⟨ + W 0 of W 0. As |W 0| ≫ |V |, there are
only a bounded number of such cosets; thus P is piecewise linear, and thus
piecewise constant on slightly smaller cosets. Intersecting all the subspaces
together, we can thus ﬁnd another limit subspace U with |U | ≫ |V | such
that P is constant on each coset of U . To put it another way, if we view U
as the intersection of a bounded number of kernels of linear homomorphism
L1∅ : : : ∅ Ld : V → F (where d = O(1) is the codimension of U ), then P

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.4. Equidistribution in ﬁnite ﬁelds 65

is constant on every simultaneous level set of L∞∅ : : : ∅ Ld, and can thus be
expressed as a function F(L∞∅ : : : ∅ Ld) of these linear polynomials.

More generally, let us say that a limit classical polynomial P of degree
 d is low rank if it can be expressed as P = F(Q∞∅ : : : ∅ Qd) where Q∞∅ : : : ∅ Qd
are a bounded number of polynomials of degree  d   1. We can summarise
the above discussion (and also Exercise 1.4.11) as follows:

Proposition 1.4.3. Let d  2, and let P : V ω F be a limit classical
polynomial. If P is biased, then P is low rank.

In particular, from the Weyl criterion, we see that if P is not equidis-
tributed, then P is of low rank.

Of course, the claim fails if the low rank hypothesis is dropped. For
instance, consider a limit classical quadratic Q = L∞L∈ that is the product
of two linearly independent linear polynomials L∞∅ L∈. Then Q attains each
non-zero value with a density of (√  1)=√∈ rather than 1=√(and attains 0
with a density of (2√  1)=√∈ rather than 1=√).

Exercise 1.4.12. Suppose that the characteristic √ of F is greater than
2, and suppose that P : Fn ω F is a quadratic polynomial of the form
P(§ ) = § TM § + ⌊T§ + ⌋, where ⌋ 2 F, ⌊ 2 Fn, M is a symmetric \  \
matrix with coeﬃcients in F, and § T is the transpose of §. Show that
jEx2V e(P (§))j  √ r= ∈, where r is the rank of M. Furthermore, if ⌊ is
orthogonal to the kernel of M, show that equality is attained, and otherwise
Ex2V e(P (§)) vanishes.

What happens in the even characteristic case (assuming now that M is
not symmetric)?

Exercise 1.4.13 (Van der Corput lemma). Let P : V ω F be a limit func-
tion on a limit ﬁnite dimensional vector space V , and suppose that there
exists a limit subset H of V which is sparse in the sense that jHj = o(jV j),
and such that @hP is equidistributed for all ⟨ 2 V nH. Show that P itself is
equidistributed. Use this to give an alternate proof of 1.4.3.

Exercise 1.4.14 (Space of polynomials is discrete). Let P : V ω F be a
polynomial of degree at most d such that Ex2V je(P(§))   ⌋j < 2 d+∞ for
some constant ⌋ 2 S∞. Show that P is constant. (Hint: induct on d.)
Conclude that if P∅ Qare two distinct polynomials of degree at most d, that
ke(P)   e(Q)kL2(V)˛ 1.

The fact that high rank polynomials are equidistributed extends to
higher degrees also:

Theorem 1.4.4. Let P : V ω F be a limit classical polynomial. If P is
biased, then P is low rank.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

66 1. Higher order Fourier analysis

I\ √art⟩⌋ular, {rom t⟨e Weyl ⌋r⟩ter⟩o\, we see t⟨at ⟩{P ⟩s \ot equ⟩d⟩s-
tr⟩⌊uted, t⟨e\P ⟩s o{ low ra\∥.

In the high characteristic case √ > d, this claim was obtained in [GrTa2009];
the generalisation to the low characteristic case √ d was carried out in
[KaLo2008]. The statement is phrased in the language of ultraﬁlters, but
it has an equivalent ﬁnitary analogue:

Exercise 1.4.15. Show that Theorem 1.4.4 is equivalent to the claim that
for every d  1 and ◦ > 0, and every classical polynomial P : V ω F of de-
gree at most d on a ﬁnite-dimensional vector space with jEx2V e(P (§))j  ◦,
that P can be expressed as a function of at most Oﬃ;d(1) classical polynomials
of degree at most d   1.

The proof of Theorem 1.4.4 is a little lengthy. It splits up into two pieces.
We say that a limit function P : V ω F (not necessarily a polynomial) is
o{ order< d if it can be expressed as a function of a bounded number
of polynomials of degree less than d. Our task is thus to show that every
polynomial of degree d which is biased, is of order < d . We ﬁrst get within an
epsilon of this goal, using an argument of Bogdanov and Viola [BoVi2010]:

Lemma 1.4.5 (Bogdanov-Viola lemma). LetP : V ω F ⌊e a l⟩m⟩t √oly\o-
m⟩al o{ de}reed w⟨⟩⌋⟨ ⟩s ⌊⟩ased, a\d let" > 0 ⌊e sta\dard. T⟨e\ o\e ⌋a\
\d a l⟩m⟩t {u\⌋t⟩o\Q: V ω F o{ order< d su⌋⟨ t⟨atjf§ 2 V : P(§) 6=
Q(§)gj  "jVj.

Proof. Let ≤ > 0 be a small standard number (depending on ") to be
chosen later, let M be a large standard integer (depending on "∅ ≤) to be
chosen later, and let ⟨ 1∅ : : : ∅ ⟨M be chosen uniformly at random from V . An
application of the second moment method (which we leave as an exercise)
shows that if M is large enough, then with probability at least 1   ", one
has jEm2M e(P (§ + ⟨ m ))   Ex2V e(P (§))j  ≤
for at least (1   ")jVj choices of §. We can rearrange this as

je(P(§ ))   1
◦ Em2M e( @ h m P(§))j  ≤=◦

where ◦ := jEx2V e(P (§))j; note from hypothesis that ◦ ˛ 1. If we let F(§)
be the nearest √th root of unity to 1
ﬃEm2M e( @ h m P(§ )), then (if ≤ is small
enough) we conclude that e(P (§)) = F(§) for at least (1   ")jVj choices of
§. On the other hand, F is clearly of order < d , and the claim follows. 

Exercise 1.4.16. Establish the claim left as an exercise in the above proof.

To conclude the proof of Theorem 1.4.4 from Lemma 1.4.5, it thus suﬃces
to show

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.4. Equidistribution in ﬁnite ﬁelds 67

Pro√os⟩t⟩o\ ∞.4.̸(Rigidity).Let P : V ω F ⌊e a l⟩m⟩t √oly\om⟩al o{
de}reed w⟨⟩⌋⟨ ⟩s equal to a l⟩m⟩t {u\⌋t⟩o\Q: V ω F o{ order< d o\ at
least1   ” o{ V, w⟨ere” > 0 ⟩s sta\dard. I{” ⟩s su◦⌋⟩e\tly small w⟩t⟨
res√e⌋t tod, t⟨e\P ⟩s also o{ order< d .

This proposition is somewhat tricky to prove, even in the high character-
istic case p > d. We ﬁx d < p and assume inductively that the proposition
(and hence) Theorem 1.4.4 has been demonstrated for all smaller values of
d.
 The main idea here is to start with the “noisy polynomial” Q, and per-
form some sort of “error correction” on Q to recover P; the key is then to
show that this error correction procedure preserves the property of being
order < d . From Exercise 1.4.14 we know that ⟩\ √r⟩\⌋⟩√le, this error cor-
rection is possible if ” is small enough; but in order to preserve the order
< d property we need a more explicit error correction algorithm which is
tractable for analysis. This is provided by the following lemma.

Lemma ∞.4.↦(Error correction of polynomials).LetP : V ω F ⌊e a (l⟩m⟩t)
⌋lass⟩⌋al √oly\om⟩al o{ de}ree at mostd, a\d letQ: V ω F ⌊e a (l⟩m⟩t) {u\⌋-
t⟩o\ w⟨⟩⌋⟨ a}rees w⟩t⟨P at least1   ” o{ t⟨e t⟩me {or some”  2 d 2 . T⟨e\
{or everyx 2 V,P(x) ⟩s equal to t⟨e most ⌋ommo\ value (⟩.e. t⟨e mode) o{
∑
! 2f0;1g d+1 nf0g ( 1) j! j 1 Q(x + ! 1h1 +    + ! d+1hd+1) as h1; : : : ; hd+1 vary
⟩\ V.

Proo{.As P is a polynomial of degree at most d, one has

@h1 : : : @hd+1 P(x) = 0

for all x; h1; : : : ; hd+12 V. We rearrange this as

P(x) = ∑

! 2f0;1g d+1 nf 0g( 1) j! j  1P(x + ! 1h1 +    + ! d+1hd+1):

We conclude that

(1.37) P(x) = ∑

! 2f0;1g d+1 nf0g ( 1) j! j 1 Q(x + ! 1h1 +    + ! d+1hd+1! d+1)

holds unless P and Q diﬀer at x + h1! 1 +    + hd+1! d+1 for some ! 2
f0; 1gd+1nf0g.

On the other hand, if x is ﬁxed and h1; : : : ; hd+1 are chosen indepen-
dently and uniformly at random from V, then for each ! 2 f0; 1gd+1nf0g,
x + h1! 1 +    + hd+1! d+1 is also uniformly distributed in V, and so the
probability that P and Q diﬀer at x + h1! 1 +    + hd+1! d+1 is at most
2 d 2 . Applying the union bound for the 2d+1  1 < 2d+1 values of ! under
consideration, we conclude that (1.37) happens more than half the time, and
the claim follows. ∗

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

68 1. Higher order Fourier analysis

Note that the above argument in fact shows that the mode is attained
for at least 1 − 2d+1 ε of the choices of h1, . . . , hd+1 .

In view of this lemma, the goal is now to show that if Q is of order
< d and is suﬃciently close to a polynomial of degree d, then the mode ofP →2f0∅1gd〉nf0g(−1)j→j 1 Q(x + ω1h1 + · · · + ωd+1 hd+1 ) is also of order < d.

By hypothesis, we have Q = F (R1, . . . , Rm ) for some standard m and
some polynomials R1, . . . , Rm of degree d − 1. To motivate the general
argument, let us ﬁrst work in an easy model case, in which the R1, . . . , Rm
are polynomials of degree d − 1 that are linearly independent modulo low
rank (i.e. order < d − 2) errors, i.e. no non-trivial linear combination of
R1, . . . , Rm over F is of low rank. This is not the most general case, but is
somewhat simpler and will serve to illustrate the main ideas.

The linear independence, combined with the inductive hypothesis, im-
plies that any non-trivial linear combination of R1, . . . , Rm is unbiased.
From this and Fourier analysis, we see that ⃗R := (R1, . . . , Rm ) is jointly
equidistributed, thus in particular we have

(1.38) |Sr| = (p
 m + o(1))|V |

for all r ∈ Fm , where Sr:= {x ∈ V : ⃗R(x) = r}.

In fact, we have a much stronger equidistribution property than this;
not only do we understand the distribution of ⃗R(x) for a single x, but more
generally we can control the distribution of an entire parallelopiped

⃗R
[D ](x, h1, . . . , hD ) := ( ⃗R(x + ω1h1 + · · · + ωD hD ))→∅:::∅→D 2f0∅1g

for any standard integer D ≥ 0. Because all the components ⃗R are poly-
nomials of degree d − 1, the quantity ⃗R[D ](x, h1, . . . , hD ) is constrained to
the space Σ[D ], deﬁned as the subspace of (Fm )2D consisting of all tuples
r = (r→)→2f0∅1gD obeying the constraints
12

X

→2F (−1)
j→jr→ = 0

for all faces F ⊂ {0, 1}D of dimension d, where |ω| := ω1 + · · · + ωD is the
sign of ω.

Proposition 1.4.8.⃗R[D ] is equidistributed inΣ[D ], thus

|{(x, h1, . . . , hD ) ∈ V d+1 : ⃗R
[D ](x, h1, . . . , hD ) = r}|

=  1
|Σ[D ]| + o(1)
´ |V |d+1

12These constraints are of course vacuous if D < d.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.4. Equidistribution in ﬁnite ﬁelds 69

{or allr2 Σ[D]. Furt⟨ermore, we ⟨ave t⟨e re\ed ⌊ou\d

jf(⟨ 1∅ : : : ∅ ⟨D ) 2 V d : ~R
[D](§∅ ⟨ 1∅ : : : ∅ ⟨D ) = rgj

=  √m

jΣ[D]j + o(1)  jV j
d

{or allr2 Σ[D] a\d all§ 2 Sr0 .

∑roof.It suﬃces to prove the second claim. Fix § and r= (r! )! 2f0;1gD
From the deﬁnition of Σ[D], we see that ris uniquely determined by the
component r0 and r<d := (r! )! 2f0;1gD .0<j! j<d . It will thus suﬃce to show
that
 jf(§∅ ⟨ 1∅ : : : ∅ ⟨D ) 2 V d : ~R
[D]
<d (§∅ ⟨ 1∅ : : : ∅ ⟨D ) = r<d gj

=  √m

jΣ[D]j + o(1)  jV j
d

for all r<d 2 (Fm )f! 2f0;1gD .0<j! j<dg , where

~R
[D]
<d (§∅ ⟨ 1∅ : : : ∅ ⟨D ) :=

( ~R(§ + →1⟨ 1 + ∆ ∆ ∆+ →D ⟨ D ))! 2f0;1gD .0<j! j<d :

By Fourier analysis, it suﬃces to show that

E h 1 ;:::;hD 2V e  ∼∆~R
[D]
<d (§∅ ⟨ 1∅ : : : ∅ ⟨D )
 = o(1)

for any non-zero ∼ 2 (Fm )f! 2f0;1gD .0<j! j<dg . In other words, we need to
show that
(1.39)

E h 1 ;:::;hD 2V e
 0

@ X

! 2f0;1gD .j! j<d ∼! ∆~R(§ + →1⟨ 1 + ∆ ∆ ∆+ →D ⟨ D )

1

A = o(1)

whenever the ∼! 2 Fm for →2 f 0∅1gD ∅0 < j→j < d are not all zero.

Let →0 be such that ∼! 0 6= 0, and such thatj→j is as large as possible; let
us write d 0 := j→0j, so that 0 ˇ d 0 < d . Without loss of generality we may
take →0 = (1∅ : : : ∅1∅0∅ : : : ∅0). Suppose (1.39) failed, then by the pigeonhole
principle one can ﬁnd ⟨ d′ +1∅ : : : ∅ ⟨D such that

jE h 1 ;:::;hd′ 2V e( X

! 2f0;1gD .j! j<d ∼! ∆~R(§ + →1⟨ 1 + ∆ ∆ ∆+ →D ⟨ D ))j ˛ 1:

We write the left-hand side as

jE h 1 ;:::;hd′ 2V e(∼! 0 ∆~R(§ + ⟨ 1 + ∆ ∆ ∆+ ⟨ d′ ))
 d′
Y

j /1 {j (⟨ 1∅ : : : ∅ ⟨d′ )j

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

70 1. Higher order Fourier analysis

where {| are bounded limit functions depending on §∅ ⟨ d 0+1∅ : : : ∅ ⟨D that are
independent of ⟨ | .

We can eliminate each {| term in turn by the Cauchy-Schwarz argument
used in Section 1.3, and conclude that

ke(∼→0  ~R)kU d0(V)˛ 1∅

and thus by the monotonicity of Gowers norms

ke(∼→0  ~R)kU dΓ1 (V)˛ 1∅

or in other words that the degree d   1 polynomial (§∅ ⟨ 1∅ : : : ∅ ⟨d(1 ) 7!
@⟨ 1 : : : @⟨ dΓ1 (∼→0  ~R)(§) is biased. By the induction hypothesis, this polyno-
mial must be low rank.

At this point we crucially exploit the high characteristic hypothesis by
noting the Taylor expansion formula

P(y ) = 1
(d   1)! @
d(1
y P(y ) + low rank errors:

The high characteristic is necessary here to invert (d   1)!. We conclude that
∼→0  ~R is of low rank, but this contradicts the hypothesis on the R1∅ : : : ∅ Rm
and the non-zero nature of ∼→0 , and the claim follows. 

Let § 2 V and r= (r→)→2f0∅1gD 2 Σ[D]. From the above proposition we
have an equidistribution result for a cube pinned at §:

jf(⟨ 1∅ : : : ∅ ⟨D ) 2 V D :§ + →1⟨ 1 +    + →D ⟨ D 2 Srω
for all →2 f 0∅1gD gj

=  √m

jΣ[D]j + o(1)  jV j
D :

(1.40)

In fact, we can do a bit better than this, and obtain equidistribution even
after ﬁxing a second vertex:

E§erc⟩se ∞.4.∞↦(Equidistribution of doubly pinned cubes).Let (r→)→2f0∅1gD 2
Σ[D], let § 2 Sr0 , let →2 f0∅ 1gD nf0g. Then for all but o(jV j) elements y
of Srω 0 , one has

(1.41) jf(⟨ 1∅ : : : ∅ ⟨D ) 2 V D : § + →1⟨ 1 +    + →D ⟨ D 2 Srω

for all →2 f 0∅1gD ; § + →

1⟨ 1 +    + →

D ⟨ D = y gj

= ( √m

jΣ[D]j + o(1))jV j
D (1 :

(Hint:One can proceed by applying Proposition 1.4.8 with D replaced by
a larger dimension, such as 2D; details can be found in [GrTa∈′′9].)

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.4. Equidistribution in ﬁnite ﬁelds 71

We can now establish Proposition 1.4.6 in the case where the R∞∅ : : : ∅ Rm
are independent modulo low rank errors. Let r0 2 Fm and § 2 Sr0 . It will
suﬃce to show that P(§) does not depend on § as long as § stays inside r0 .

Call an atom Sr good if P and Q agree for at least 1  p " of the elements
of Sr ; by Markov’s inequality (and (1.38)) we see that at least 1   p " + o(1)
of the atoms are good. From this and an easy counting argument we can
ﬁnd an element r= (r! )! 2f0;∞gd in Σ∪d]with the speciﬁed value of r0 , such
that r! is good for every f0∅1gdnf0g.

Fix r. Now consider all the pinned cubes (§+⟨ ∞→∞+  +⟨ d→d)! 1;:::;! d2f0;∞gd
with § + ⟨ ∞→∞+    + ⟨ d→d 2 Srω for all →2 f 0∅1gdnf0g. By (1.40), the num-
ber of such cubes is ( pm

j±[d]j + o(1))jV jd. On the other hand, by Proposition
1.4.17, the total number of such cubes for which

P(§ + ⟨ ∞→∞+    + ⟨ d→d) 6=Q(§ + ⟨ ∞→∞+    + ⟨ d→d)

for some → 2 f0∅1gdnf0g is o(jV jd(∞). We conclude that there exists a
pinned cube for which

P(§ + ⟨ ∞→∞+    + ⟨ d→d) = Q(§ + ⟨ ∞→∞+    + ⟨ d→d)

for all →2 f0∅1gdnf0g, and in particular (1.37) holds. However, as Q is
constant on each of the Sr , we see that the right-hand side of (1.37) does
not depend on § , and so the left-hand side does also.

This completes the proof of Proposition 1.4.6 in the independent case.
In the general case, one reduces to a (slight generalisation of) this case by
the following regularity lemma:

Lemma 1.4.9 (Regularity lemma). Let R∞∅ : : : ∅ Rm be a bounded number
of limit classical polynomials of degree d   1. Then there exists a limit
classical bounded number of polynomialsSd0;∞∅ : : : ∅ Sd0;md0 of degree d for
each 1  d  d   1, such that eachR∞∅ : : : ∅ Rm is a function of theSd0;i for
1  d  d and 1  ⟩  m d0, and such that for eachd , the Sd0;∞∅ : : : ∅ Sd0;md0
are independent modulo low rank polynomials of degreed .

Proof. We induct on d. The claim is vacuously true for d = 1, so suppose
that d > 1 and that the claim has already been proven for d   1.

Let Polyd(∞ be the space of limit classical polynomials of degree 
d   1, and let Poly0
d(∞ be the subspace of low rank limit classical poly-
nomials. Working in the quotient space Polyd(∞ =Poly0
d(∞, we see that
R∞∅ : : : ∅ Rm generates a ﬁnite-dimensional space here, which thus has a ba-
sis Sd(∞;∞∅ : : : ∅ Sd(∞;md 1 mod Poly0
d(∞, thus Sd(∞;∞∅ : : : ∅ Sd(∞;md 1 are lin-
early independent modulo low rank polynomials of degree d   1, and the
R∞∅ : : : ∅ Rm are linear combinations of the Sd(∞;∞∅ : : : ∅ Sd(∞;md 1 plus combi-
nations of some additional polynomials R
∞∅ : : : ∅ R
m0 of degree d  2. Applying

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

72 1. Higher order Fourier analysis

the induction hypothesis to those additional polynomials, one obtains the
claim. ∗

E§er⌋⟩se ∞.4.∞8.Show that the polynomials S := (Sd0,i)1d 0d 1;1im d0
appearing in the above lemma are equidistributed in the sense that

jfx2 V : S(x) = sgj=
   1

p
P d
d0/1 md0 + o(1)

!
 jVj

for any s = (sd0,i)1d 0d 1;1im d0 with sd0,i 2 F.

Applying the above lemma, one can express any order < d function Q
in the form Q = F((Sd0,i)1d 0d 1;1im d0). It is then possible to modify
the previous arguments to obtain Proposition 1.4.6; see [GrTa∈009] for
more details. (We phrase the arguments in a ﬁnitary setting rather than a
nonstandard one, but the two approaches are equivalent; see Section 2.1 for
more discussion.)

It is possible to modify the above arguments to handle the low char-
acteristic case, but due to the lack of a good Taylor expansion, one has
to regularise the derivatives of the polynomials, as well as the polynomials
themselves; see [KaLo∈008] for details.

∞.4.3. A\alyt⟩⌋ ra\∥.Deﬁne the rank rankd 1 (P) of a degree d (limit)
classical polynomial P to be the least number m of degree  d   1 (limit)
classical polynomials R1; : : : ; Rm such that P is a function of R1; : : : ; Rm.
Theorem 1.4.3 tells us that P is equidistributed whenever the rank is un-
bounded. However, the proof was rather involved. There is a more elemen-
tary approach to equidistribution to Gowers and Wolf [GoWo∈0∞0⌊] which
replaces the rank by a diﬀerent object, called analytic rank , and which can
serve as a simpler substitute for the concept of rank in some applications.

De\⟩t⟩o\ ∞.4.∞0(Analytic rank).The analytic rank arankd 1 (P) of a
(limit) classical polynomial P : V ω F of degree  d is deﬁned to be the
quantity
 arankd(P) :=   logp E x,h1,...,hd2V e(@h1 : : : @hdP(x))

=  2 d logp ke(P)kU d(V ):

From the properties of the Gowers norms we see that this quantity is
non-negative, is zero if and only if P is a polynomial of degree < d , and is
ﬁnite (or limit ﬁnite) for d > 2. (For d = 1, the analytic rank is inﬁnite if P
is non-constant and zero if P is constant.)

E§er⌋⟩se ∞.4.∞9.Show that if p > 2 and P is a (limit) classical polynomial
of degree 2, then rank1(P) = arank1(P).

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.4. Equidistribution in ﬁnite ﬁelds 73

E§er⌋⟩se ∞.4.∈0.Show that if the analytic rank arankdΓ1 (P ) of a limit
classical polynomial P of degree d is unbounded, then P is equidistributed.

E§er⌋⟩se ∞.4.∈∞.Suppose we are in the high characteristic case p > d.
Using Theorem 1.4.3, show that a limit classical polynomial has bounded
analytic rank if and only if it has bounded rank. (Hint: One direction
follows from the preceding exercise. For the other direction, use the Taylor
formula P (x) = 1
dω@d
§ P (x).) This is a special case of the inverse conjecture
for the Gowers norms, which we will discuss in more detail in later sections.

Conclude the following ﬁnitary version: if P : V ω F is a classical poly-
nomial of degree d on a ﬁnite-dimensoinal vector space V, and arankdΓ1 (P ) 
M , then rankdΓ1 (P ) ˝ M∅√∅d1; conversely, if rankdΓ1 (P )  M , then arankdΓ1 (P ) ˝ M∅√∅d
1.

E§er⌋⟩se ∞.4.∈∈.Show that if P is a (limit) classical polynomial of degree
d, then rankdΓ1 (P ) = rankdΓ1 (cP) and arankdΓ1 (P ) = arankdΓ1 (cP) for
all c 2 Fn0, and rankdΓ1 (P + Q) = rankdΓ1 (P ) and arankdΓ1 (P + Q) =
arankdΓ1 (P ) for all (limit) classical polynomials Q of degree  d   1.

It is clear that the rank obeys the triangle inequality rankdΓ1 (P + Q) 
rankdΓ1 (P ) + rankdΓ1 (Q) for all (limit) classical polynomials of degree  d.
There is an analogue for analytic rank:

Pro√os⟩t⟩o\ ∞.4.∞∞(Quasi-triangle inequality for analytic rank).[GoWo∈0∞0⌊]
Let P; Q: V ω F be (limit) classical polynomials of degree d. Then
arankdΓ1 (P + Q)  2d (arankdΓ1 (P ) + arankdΓ1 (Q)).

Proo{.Let T1(h1; : : : ; hd ) be the d-linear form

T1(h1; : : : ; hd ) := @⟨  : : : @⟨ dP (x)

(note that the right-hand side is independent of x); similarly deﬁne

T2(h1; : : : ; hd ) := @⟨  : : : @⟨ dP (x)

By deﬁnition, we have

E ⟨ ∅:::∅⟨d2V e(T1(h1; : : : ; hd )) = p
Γ arankd  (P)

and E ⟨ ∅:::∅⟨d2V e(T2(h1; : : : ; hd )) = p
Γ arankd  (Q)

and thus
 E ⟨ ∅:::∅⟨d∅⟨0
∅:::∅⟨0
d2V e(T1(h1; : : : ; hd ) + T2(h0
1; : : : ; h
0
d ))

= p
Γ arankd  (P)Γarankd  (Q):
We make the substitution h0
| = h| + k| . Using the multilinearity of T2, we
can write the left-hand side as

E ∥∅:::∅∥d2V E ⟨ ∅:::∅⟨d2V e((T1 + T2)(h1; : : : ; hd ))

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

74 1. Higher order Fourier analysis

dY

| =1 f| (h1, . . . , hd , k1, . . . , kd )

where the f| are functions bounded in magnitude by 1 that are independent
of the h| variable. Eliminating all these factors by Cauchy-Schwarz as in
Section 1.3, we can bound the above expression by

(E ⟨ 0
1∅:::∅⟨0
d ∅⟨1
1∅:::∅⟨1
d 2V e( X

→2f0∅1gd( 1) j→j(T1 + T2)(h
→1
1 , . . . , h
→d
d )j
1=2d

which using the substitution h⟩ := h1
⟩   h0
⟩ and the multilinearity of T1 + T2
simpliﬁes to (E ⟨ 1∅:::∅⟨d 2V e((T1 + T2)(h1, . . . , hd ))j
1=2d

which by deﬁnition of analytic rank is

p
( arankd 1 (P +Q)=2d ,

and the claim follows. ∗

1.5. The inverse conjecture for the Gowers norm I. The
nite eld case

In Section 1.3, we saw that the number of additive patterns in a given set
was (in principle, at least) controlled by the Gowers uniformity norms of
functions associated to that set.

Such norms can be deﬁned on any ﬁnite additive group (and also on
some other types of domains, though we will not discuss this point here).
In particular, they can be deﬁned on the ﬁnite-dimensional vector spaces V
over a ﬁnite ﬁeld F.

In this case, the Gowers norms Ud+1 (V ) are closely tied to the space
Polyd (V ω R /Z) of polynomials of degree at most d. Indeed, as noted
in Exercise 1.4.20, a function f : V ω C of L (V ) norm 1 has Ud+1 (V )
norm equal to 1 if and only if f = e(φ) for some φ 2 Polyd (V ω R /Z);
thus polynomials solve the “100% inverse problem” for the trivial inequality
kfkU d+1 (V )  kfkL1 (V ). They are also a crucial component of the solution
to the “99% inverse problem” and “1% inverse problem”. For the former,
we will soon show:

Proposition 1.5.1 (99% inverse theorem for Ud+1 (V )). Let f : V ω C be
such that kfkL1 (V ) and kfkU d+1 (V )  1   ε for some ε > 0. Then there
exists φ 2 Polyd (V ω R /Z) such that kf   e(φ)kL1(V ) = Od∅F(ε⌋), where
c = cd > 0 is a constant depending only on d.

Thus, for the Gowers norm to be almost completely saturated, one must
be very close to a polynomial. The converse assertion is easily established:

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.5. Inverse conjecture over ﬁnite ﬁelds 75

E§er⌋⟩se ∞.5.∞(Converse to 99% inverse theorem for U d+1(V )).If k{ kL1 (V)ˇ
1 and k{  e(˚)k L1 (V)ˇ " for some ˚2 Polyd (V ! R=Z), thenkF kUd+1(V)
1   Od;F("c), where ⌋ = ⌋d > 0 is a constant depending only on d.

In the 1% world, one no longer expects to be close to a polynomial.
Instead, one expects to correlatewith a polynomial. Indeed, one has

Lemma ∞.5.∈(Converse to the 1% inverse theorem for U d+1(V )).I{{ : V !
C a\d ˚ 2 Polyd (V ! R=Z) are suc⟨ t⟨atjh{∅ e(˚)iL2 (V)j  ", w⟨ere
h{∅ }i L2 (V):= E x2G{(§) }(§), t⟨e\k{ kUd+1(V) ".

Proo{.From the deﬁnition (1.34) of the U 1 norm, the monotonicity of the
Gowers norms (Exercise 1.3.19), and the polynomial phase modulation in-
variance of the Gowers norms (Exercise 1.3.21), one has

jh{∅ e(˚)ij = k{ e( ˚)k U1 (V)
ˇ k { e( ˚)k Ud+1(V)
= k{ kUd+1(V)
and the claim follows. 

It is a diﬃcult but known fact that Lemma 1.5.2 can be reversed:

T⟨eorem ∞.5.3(1% inverse theorem for U d+1(V )).Suppose t⟨atchar(F) >
d  0. I{{ : V ! C ⟩s suc⟨ t⟨atk{ kL1 (V)ˇ 1 a\d k{ kUd+1(V) ", t⟨e\
t⟨ere e§⟩sts˚2 Polyd (V ! R=Z) suc⟨ t⟨atjh{∅ e(˚)iL2 (V)j ˛ ”;d;F 1.

This result is sometimes referred to as the ⟩\verse co\|ecture {or t⟨e
Gowers \orm(in high, but bounded, characteristic). For small d, the claim
is easy:

E§er⌋⟩se ∞.5.∈.Verify the cases d = 0∅1 of this theorem. (H⟩\t:to verify
the d = 1 case, use the Fourier-analytic identities k{ kU2 (V)= (
P
 ˘2 ^V j ˆ{(∼)j4)1=4

and k{ kL2 (V)= (P
 ˘2 ^V j ˆ{(∼)j2)1=2, where ˆV is the space of all homomor-

phisms ∼: § 7! ∼ § from V to R=Z, and ˆ{(∼) := E x2V {(§)e( ∼  §) are the
Fourier coeﬃcients of {.)

This conjecture for larger values of d are more diﬃcult to establish.
The d = 2 case of the theorem was established in [GrTa∈008]; the low
characteristic case char(F) = d = 2 was independently and simultaneously
established in [Sa∈00↦]. The cases d > 2 in the high characteristic case
was established in two stages, ﬁrstly using a modiﬁcation of the Furstenberg
correspondence principle in [TaZ⟩∈0∞0], and then using a modiﬁcation of
the methods of Host-Kra [HoKr∈005] and Ziegler [ Z⟩∈00↦] to solve that
counterpart, as done in [BeTaZ⟩∈0∞0 ]; an alternate proof was also obtained

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

76 1. Higher order Fourier analysis

in [Sz∈0∞0⌋]. Finally, the low characteristic case was recently achieved in
[TaZ⟩∈0∞∞].

In the high characteristic case, we saw from Section 1.4 that one could
replace the space of non-classical polynomials Poly≤d(V ! R/Z) in the
above conjecture with the essentially equivalent space of classical polyno-
mials Poly≤d(V ! F). However, as we shall see below, this turns out not
to be the case in certain low characteristic cases (a fact ﬁrst observed in
[LoMeSa∈008], [ GrTa∈009]), for instance if char( F) = 2 and d  3; this
is ultimately due to the existence in those cases of non-classical polynomials
which exhibit no signiﬁcant correlation with classical polynomials of equal
or lesser degree. This distinction between classical and non-classical poly-
nomials appears to be a rather non-trivial obstruction to understanding the
low characteristic setting; it may be necessary to obtain a more complete
theory of non-classical polynomials in order to fully settle this issue.

The inverse conjecture has a number of consequences. For instance, it
can be used to establish the analogue of Szemer´edi’s theorem in this setting:

T⟨eorem ∞.5.4(Szemer´edi’s theorem for ﬁnite ﬁelds).Let F = Fp be
a ﬁnite ﬁeld, letδ > 0, and letA ˆ Fn be such thatjAj  δjFnj. If
n is suciently large depending onp, δ, thenA contains an (ane) line
fx, x + r, . . . , x+ (p   1)rg for somex, r 2 Fn withr 6= 0.

‘

E§er⌋⟩se ∞.5.3.Use Theorem 1.5.4 to establish the following generalisation:
with the notation as above, if k  1 and n is suﬃciently large depending on
p, δ, then A contains an aﬃne k-dimensional subspace.

We will prove this theorem in two diﬀerent ways, one using a density
increment method, and the other using an energy increment method. We
discuss some other applications below the fold.

∞.5.∞. T⟨e99% ⟩\verse t⟨eorem.We now prove Proposition 1.5.1. Re-
sults of this type for general d appear in [AlKaKrL⟩Ro∈003] (see also
[SuTrVa∞999] for a precursor result); thed = 1 case was treated previously
in [BlLuRu∞993]. The argument here is taken from [TaZ⟩∈0∞0], and has
a certain “cohomological” ﬂavour (comparing cocycles with coboundaries,
determining when a closed form is exact, etc.). Indeed, the inverse theory
can be viewed as a sort of “additive combinatorics cohomology”.

Let F, V, d, f, εbe as in the theorem. We let all implied constants depend
on d, F. We use the symbol c to denote various positive constants depending
only on d. We may assume ε is suﬃciently small depending on d, F, as the
claim is trivial otherwise.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.5. Inverse conjecture over ﬁnite ﬁelds 77

The case d = 0 is easy, so we assume inductively that d ≥ 1 and that
the claim has been already proven for d − 1.

The ﬁrst thing to do is to make { unit magnitude. One easily veriﬁes
the crude bound ∥{∥
2d+1
Ud+1 (V) ≤ ∥{∥L1 (V)

and thus ∥{∥L1 (V) ≥ 1 − O("):

Since |{| ≤ 1 pointwise, we conclude that

Ex2V1 − |{(§)| = O("):

As such, { diﬀers from a function ˜{ of unit magnitude by O(") in L1 norm.
By replacing { with ˜{ and using the triangle inequality for the Gowers norm
(changing " and worsening the constant ⌋ in Proposition 1.5.1 if necessary),
we may assume without loss of generality that |{| = 1 throughout, thus
{ = e( ) for some  : V → R=Z.

Since ∥{∥
2d+1
Ud+1 (V) = Eh2V∥e(@h )∥
2d
Ud (V)
we see from Markov’s inequality that

∥e(@h )∥Ud (V) ≥ 1 − O("
c)

for all ⟨ in a subset H of V of density 1 − O("c). Applying the inductive
hypothesis, we see that for each such ⟨, we can ﬁnd a polynomial ˚h ∈
Polyd(1 (V → R=Z) such that

∥e(@h ) − e(˚h)∥L1 (V) = O("
c):

Now let ⟨∅ ∥ ∈ H. Using the cocycle identity

e(@h+k ) = e(@h˚)T
he(@k˚)

where T h is the shift operator T h{(§) := {(§ + ⟨), we see using H¨older’s
inequality that
 ∥e(@h+k ) − e(˚hT h˚k)∥L1 (V) = O("
c):

On the other hand, ˚hT h˚k is a polynomial of order d. Also, since H is so
dense, every element lof V has at least one representation of the form l= ⟨ +
∥ for some ⟨∅ ∥ ∈ H (indeed, out of all |V | possible representations l= ⟨ + ∥,
⟨ or ∥ can fall outside of H for at most O("c|V |) of these representations).
We conclude that for every l∈ V there exists a polynomial ˚
l ∈ Polyd (V →
R=Z) such that

(1.42) ∥e(@l ) − e(˚

l)∥L1 (V) = O("
c):

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

78 1. Higher order Fourier analysis

The new polynomial ˚0
l supercedes the old one ˚l; to reﬂect this, we abuse
notation and write ˚l for ˚0
l. Applying the cocycle equation again, we see
that

(1.43) ke(˚h+k )   e(˚hT h˚k)kL1(V) = O("
c)

for all ⟨∅ ∥ 2 V . Applying the rigidity of polynomials (Exercise 1.4.6), we
conclude that ˚h+k = ˚hT h˚k + ⌋h;k
for some constant ⌋h;k 2 R=Z. From (1.43) we in fact have⌋h;k = O("c) for
all ⟨∅ ∥ 2 V .

The expression ⌋h;k is known as a 2-̂oboundary(see [Ta2009, x1.13]
for more discussion). To eliminate it, we use the ﬁnite characteristic to
discretise the problem as follows. First, we use the cocycle identity

p−1Y

j =0 e(T jh @h ) = 1

where √is the characteristic of the ﬁeld. Using (1.42), we conclude that

k
 p−1Y

j =0 e(T jh ˚h)   1kL1(V) = O("
c):

On the other hand, T jh ˚h takes values in some coset of a ﬁnite subgroup C
of R=Z (depending only on √∅ d), by Lemma 1.4.1. We conclude that this
coset must be a shift of C by O("c). Since ˚h itself takes values in some
coset of a ﬁnite subgroup, we conclude that there is a ﬁnite subgroup C 0

(depending only on √∅ d) such that each ˚h takes values in a shift of C 0 by
O("c).

Next, we note that we have the freedom to shift each ˚h by O("c) (ad-
justing ⌋h;k accordingly) without signiﬁcantly aﬀecting any of the properties
already established. Doing so, we can thus ensure that all the ˚h take val-
ues in C 0 itself, which forces ⌋h;k to do so also. But since ⌋h;k = O("c), we
conclude that ⌋h;k = 0 for all ⟨∅ ∥, thus ˚h is a perfect cocycle:

˚h+k = ˚hT h˚k:

We may thus integrate ˚h and write ˚h = @hΦ, where Φ(§) := ˚x(0). Thus
@hΦ is a polynomial of degree d   1 for each ⟨, thus Φ itself is a polynomial
of degree d. From (1.42) one has

Ex∈V e(@h(   Φ)) = 1 + O("
c)

for all ⟨ 2 V ; averaging in V we conclude that

jEx∈V e(   Φ)j
2 = 1 + O("
c)

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.5. Inverse conjecture over ﬁnite ﬁelds 79

and thus
 ∥e( ) − e(Φ)∥L1 (V) = O("
c)

and Proposition 1.5.1 follows.

One consequence of Proposition 1.5.1 is that the property of being a
classical polynomial of a ﬁxed degree d is locally testable, which is a notion
of interest in theoretical computer science. More precisely, suppose one is
given a large ﬁnite vector space V and two functions ˚1∅ ˚2 : V → F. One
is told that one of the functions ˚1∅ ˚2 is a classical polynomial of degree at
most d, while the other is quite far from being such a classical polynomial,
in the sense that every polynomial of degree at most d will diﬀer with that
polynomial on at least " of the values in V . The task is then to decide with
a high degree of conﬁdence which of the functions is a polynomial and which
one is not, without inspecting too many of the values of ˚1 or ˚2.

This can be done as follows. Pick §∅ ⟨ 1∅ : : : ∅ ⟨d+1 ∈ V at random, and
test whether the identities
 @h1 : : : @hd+1˚1(§) = 0

and
 @h1 : : : @hd+1˚2(§) = 0

hold; note that one only has to inspect ˚1∅ ˚2 at 2d+1 values in V for this.
If one of these identities fails, then that function must not be polynomial,
and so one has successfully decided which of the functions is polynomials.
We claim that the probability that the identity fails for the non-polynomial
function is at least ◦ for some ◦ ≫d;F "Od;F(1), and so if one iterates this
test Oﬃ(1) times, one will be able to successfully solve the problem with
probability arbitrarily close to 1.

To verify the claim, suppose for contradiction that the identity only
failed at most ◦ of the time for the non-polynomial (say it is ˚2); then
∥e(˚2)∥Ud+1(V) ≥ 1 − O(◦), and thus by Proposition 1.5.1, ˚2 is very close
in L1 norm to a polynomial; rounding that polynomial to a root of unity we
thus see that ˚2 agrees with high accuracy to a classical polynomial, which
leads to a contradiction if ◦ is chosen suitably.

1.5.2. A partial counterexample in low characteristic. We now show
a distinction between classical polynomials and non-classical polynomials
that causes the inverse conjecture to fail in low characteristic if one insists
on using classical polynomials. For simplicity we restrict attention to the
characteristic two case F = F2. We will use an argument of Alon and
Beigel [AlBe2001], reproduced in [GrTa2009]. A diﬀerent argument (with
stronger bounds) appeared independently in [LoMeSa2008].

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

80 1. Higher order Fourier analysis

We work in a standard vector space V = Fn, with standard basis
e1∅ : : : ∅ en and coordinates § 1∅ : : : ∅ §n. Among all the classical polynomials
on this space are the symmetric polynomials

Sm := X

1i <<i mn § i : : : §im∅

which play a special role.

E§er⌋⟩se ∞.5.4.Let L : V ! N be the digit summation function L :=
#f1  ⟩  \ : § i = 1g. Show that

Sm =  L
m
  mod 2:

Establish Lucas’ theorem 13
 Sm = S2j : : : S2jr

where m = 2j  +    + 2j r , | 1 >    > | r is the binary expansion of m. Show
that S2j is the 2j binary coeﬃcient of L, and conclude that Sm is a function
of L mod 2j .

We deﬁne an an aﬃne coordinate subspace to be a translate of a subspace
of V generated by some subset of the standard basis vectors e1∅ : : : ∅ en. To
put it another way, an aﬃne coordinate subspace is created by freezing some
of the coordinates, but letting some other coordinates be arbitrary.

Of course, not all classical polynomials come from symmetric polyno-
mials. However, thanks to an application of Ramsey’s theorem observed in
[AlBe∈00∞], this is true on coordinate subspaces:

Lemma ∞.5.5(Ramsey’s theorem for polynomials).Let P : Fn ! F be
a polynomial of degree at most d. Then one can partition Fn into aﬃne
coordinate subspaces of dimension W at least →d(\), where →d(\) ! 1 as
\ ! 1 for ﬁxed d, such that on each such subspace W, P is equal to a
linear combination of the symmetric polynomials S0∅ S1∅ : : : ∅ Sd.

Proo{.We induct on d. The claim is trivial for d = 0, so suppose that
d  1 and the claim has already been proven for smaller d. The degree d
term Pd of P can be written as

Pd = X

fi ;:::;idg2E § i : : : §id

where E is a d-uniform hypergraph on f1∅ : : : ∅ \g, i.e. a collection of d-
element subsets of f1∅ : : : ∅ \g. Applying Ramsey’s theorem for hypergraphs

13These results are closely related to the well-known fact thatPascal's tr⟩a\}lemodulo 2
takes the form of an inβniteS⟩erp⟩\s∥⟩ }as∥et.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.5. Inverse conjecture over ﬁnite ﬁelds 81

(see e.g. [GrRoS√∞980] or [Ta∈009, §2.6]), one can ﬁnd a subcollection
j 1; : : : ; jm of indices with m ≥ ! d(n) such that E either has no edges in
{j 1; : : : ; jm }, or else contains all the edges in {j 1; : : : ; jm }. We then foliate
Fn into the aﬃne subspaces formed by translating the coordinate subspace
generated by ej 1 ; : : : ; ej m . By construction, we see that on each such sub-
space, P is equal to either 0 or Sd plus a polynomial of degree d − 1. The
claim then follows by applying the induction hypothesis (and noting that the
linear span of S0; : : : ; Sd(1 on an aﬃne coordinate subspace is equivariant
with respect to translation of that subspace). 

Because of this, if one wants to concoct a function which is almost or-
thogonal to all polynomials of degree at most d, it will suﬃce to build a func-
tion which is almost orthogonal to the symmetric polynomials S0; : : : ; Sd on
all aﬃne coordinate subspaces of moderately large size. Pursuing this idea,
we are led to

Pro√os⟩t⟩o\ ∞.5.̸(Counterexample to classical inverse conjecture).Let
d ≥ 1, and let f : Fn
2 → S 1 be the functionf := e(L=2d), where L is as in
Exercise 1.5.4. ThenL=2d mod 1 is a non-classical polynomial of degree at
most d, and so ∥f ∥U d+1 (Fn
2 )= 1; but one has

⟨f; e (˚)⟩L 2(Fn
2 )= on),d (1)

uniformly for all classical polynomials˚of degree less than2d(1 , where
on),d (1) is bounded in magnitude by a quantity that goes to zero asn → ∞
for each xedd.

Proo{.We ﬁrst prove the polynomiality of L=2d mod 1. Let x ↦→ |x| be the
obvious map from F2 to {0; 1}, thus

L =
 nX

i/1 |xi|:

By linearity, it will suﬃce to show that each function |xi| mod 2d is a poly-
nomial of degree at most d. But one easily veriﬁes that for any h ∈ Fn
2 ,
@h |xi| is equal to zero when hi = 0 and equal to 1 − 2|xi| when hi = 1.
Iterating this observation d times, we obtain the claim.

Now let ˚be a classical polynomial of degree less than 2d(1 . By Lemma
1.5.5, we can partition Fn
2 into aﬃne coordinate subspaces W of dimension
at least ! d(n) such that ˚is a linear combination of S0; : : : ; S2d 1 (1 on each
such subspace. By the pigeonhole principle, we thus can ﬁnd such a W such
that
 |⟨f; e (˚)⟩L 2(Fn
2 )| ≤ |⟨f; e (˚)⟩L 2(W)|:

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

82 1. Higher order Fourier analysis

On the other hand, from Exercise 1.5.4, the function ˚ on W depends only
on L mod 2dΓ1 . Now, as dim(W) ! 1, the function L mod 2d (which is es-
sentially the distribution function of a simple random walk of length dim(V )
on Z=2d Z) becomes equidistributed; in particular, for any a 2 Z=2d Z, the
function { will take the values e(a=2d ) and  e(a=2 d ) with asymptotically
equal frequency on W, whilst ˚ remains unchanged. As such we see that
jh{∅ e(˚)iL2 (W)j ! 0 as dim(W) ! 1, and thus as \ ! 1, and the claim
follows. 

Exercise 1.5.5. With the same setup as the previous proposition, show that
ke(S2d 1 =2)kU d+1(Fn
2 )˛ 1, but that he(S2d 1 =2)∅ e(˚)iL2 (Fn
2 )= o \!1,d (1)
for all classical polynomials ˚ of degree less than 2dΓ1 .

1.5.3. The 1% inverse theorem: sketches of a proof. The proof of
Theorem 1.5.3 is rather diﬃcult once d  2; even the d = 2 case is not
particularly easy. However, the arguments still have the same cohomological
ﬂavour encountered in the 99% theory. We will not give full proofs of this
theorem here, but indicate some of the main ideas.

We begin by discussing (quite non-rigorously) the signiﬁcantly simpler
(but still non-trivial) d = 2 case, under the assumption of odd characteris-
tic, in which case we can use the arguments from [Go1998], [GrTa2008].
Unsurprisingly, we will take advantage of the d = 1 case of the theorem as
an induction hypothesis.

Let V = F\ for some ﬁeld F of characteristic greater than 2, and {
be a function with k{ kL1 (V)ˇ 1 and k{ kU 3 (V)˛ 1. We would like to
show that { correlates with a quadratic phase function e(˚) (due to the
characteristic hypothesis, we may take ˚ to be classical), in the sense that
jh{∅ e(˚)iL2 (V)j ˛ 1.

We expand k{ k8
U 3 (V)as E⟨2V k∆⟨ {k4
U 2 (V). By the pigeonhole principle,
we conclude that k∆⟨ {kU 2 (V)˛ 1

for “many” ⟨ 2 V , where by “many” we mean “a proportion of ˛ 1”.
Applying the U 2 inverse theorem, we conclude that for many ⟨, that there
exists a linear polynomial ˚⟨ : V ! F (which we may as well take to be
classical) such that jh∆⟨ {∅ e(˚⟨ )i L2 (V)j ˛ 1:

This should be compared with the 99% theory. There, we were able to
force ∆⟨ { close to e(˚⟨ ) for most ⟨; here, we only have the weaker statement
that ∆⟨ { correlateswith e(˚⟨ ) for many (not most) ⟨. Still, we will keep
going. In the 99% theory, we were able to assume { had magnitude 1, which
made the cocycle equation ∆⟨+∥{ = (∆⟨ {)T ⟨ ∆∥ { available; this then forced

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.5. Inverse conjecture over ﬁnite ﬁelds 83

an approximate cocycle equation ˚⟨+∥ π ˚⟨ + T ⟨ ˚∥ for most ⟨∅ ∥ (indeed,
we were able to use this trick to upgrade “most” to “all”).

This doesn’t quite work in the 1% case. Firstly, { need not have mag-
nitude exactly equal to 1. This is not a terribly serious problem, but the
more important diﬃculty is that correlation, unlike the property of being
close, is not transitive or multiplicative: just because ∆⟨ { correlates with
e(˚⟨ ), and T ⟨ ∆∥ { correlates with T ⟨ e(˚∥ ), one cannot then conclude that
∆⟨+∥ { = (∆⟨ {)T ⟨ ∆∥ { correlates with e(˚⟨ )T ⟨ e(˚∥ ); and even if one had
this, and if ∆⟨+∥ { correlated with e(˚⟨+∥ ), one could not conclude that
e(˚⟨+∥ ) correlated with e(˚⟨ )T ⟨ e(˚∥ ).

Despite all these obstacles, it is still possible to extract something re-
sembling a cocycle equation for the ˚⟨ , by means of the Cauchy-Schwarz
inequality. Indeed, we have the following remarkable observation of Gowers
[Go1998]:

Lemma 1.5.7. Let V be a ﬁnite additive group, and let{ : V ω C be a
function, bounded by1. LetH ρ V be a subset withjHj ˛ j V j, and suppose
that for each⟨ 2 H, suppose that we have a function˜⟨ : V ω C bounded
by1, such that
 jh∆⟨ {∅ ˜⟨ iL2 (V )j ˛ 1

uniformly in⟨. Then there exist˛ jV j3 quadruples⟨ 1∅ ⟨2∅ ⟨3∅ ⟨4 2 H with
⟨ 1 + ⟨ 2 = ⟨ 3 + ⟨ 4 such that

jE§2V ˜⟨ 1 (§)˜⟨ 2 (§ + ⟨ 1   ⟨ 4)˜⟨ 3 (§) ˜⟨ 4 (§ + ⟨ 1   ⟨ 4)j ˛ 1

uniformly among the quadruples.

We shall refer to quadruples (⟨ 1∅ ⟨2∅ ⟨3∅ ⟨4) obeying the relation ⟨ 1+⟨ 2 =
⟨ 3 + ⟨ 4 as additive quadruples.

Proof. We extend ˜⟨ to be zero when ⟨ lies outside of H. Then we have

jE⟨2V ⊆⟨ h∆⟨ {∅ ˜⟨ iL2 (V )j ˛ 1

and some complex numbers ⊆⟨ bounded in magnitude by one. We rearrange
this as
 jE§∅y 2V {(y ){(§ )⊆y (§ ˜y (§ (§)j ˛ 1:

Using Cauchy-Schwarz in § and y to eliminate the { variables, we conclude
that
 jE§∅y∅§ 0∅y 02V ⊆y (§ ⊆y (§ 0⊆y 0(§ ⊆y (§ ˜y (§ (§)

˜y (§ 0(§ )˜y 0(§ (§)˜y 0(§ 0(§ )j ˛ 1:

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

84 1. Higher order Fourier analysis

Setting (⟨ ∞∅ ⟨∈∅ ⟨3∅ ⟨4) to be the additive quadruple (y Γ §∅ y 0Γ § 0∅ y 0Γ §∅ y Γ § 0)
we obtain

jEh1 +h 2 =h 3 +h 4 ⊆h1 ⊆h2 ⊆h3 ⊆h4
E x2V ˜h1 (§)˜h2 (§ + ⟨ ∞Γ ⟨ 4)˜h3 (§) ˜h4 (§ + ⟨ ∞Γ ⟨ 4)j ˛ 1

and the claim follows (note that for the quadruples obeying the stated lower
bound, ⟨ ∞∅ ⟨∈∅ ⟨3∅ ⟨4 must lie in H). 

Applying this lemma to our current situation, we ﬁnd many additive
quadruples (⟨ ∞∅ ⟨∈∅ ⟨3∅ ⟨4) for which

jEx2V e(˚h1 (§) + ˚h2 (§ + ⟨ ∞Γ ⟨ 4) Γ ˚h3 (§) Γ ˚h4 (§ + ⟨ ∞Γ ⟨ 4))j ˛ 1:

In particular, by the equidistribution theory in Section 1.4, the polynomial
˚h1 + ˚h2 Γ ˚h3 Γ ˚h4 is low rank.

The above discussion is valid in any value of d  2, but is particularly
simple when d = 2, as the ˚h are now linear, and so ˚h1 + ˚h2 Γ ˚h3 Γ ˚h4
is now constant. Writing˚h(§) = ∼h ∆§ + ⊆h for some ∼h 2 V using the
standard dot product on V , and some (irrelevant) constant term ⊆h 2 F, we
conclude that

(1.44) ∼h1 + ∼h2 = ∼h3 + ∼h4
for many additive quadruples ⟨ ∞∅ ⟨∈∅ ⟨3∅ ⟨4.

We now have to solve an additive combinatorics problem, namely to
classify the functions ⟨ 7! ∼h from V to V which are “1% aﬃne linear”
in the sense that the property (1.44) holds for many additive quadruples;
equivalently, the graph f(⟨∅ ∼h) : ⟨ 2 Hg in V  V has high “additive
energy”, deﬁned as the number of additive quadruples that it contains. An
obvious example of a function with this property is an aﬃne-linear function
∼h = M ⟨ + ∼0 , where M: V ! V is a linear transformation and ∼0 2 V . As
it turns out, this is essentially the only example:

Proposition 1.5.8 (Balog-Szemer´edi-Gowers-Freiman theorem for vector
spaces). LetH ˆ V , and let⟨ 7! ∼h be a map fromH toV such that(1.44)
holds for˛ jV j3 additive quadruples inH. Then there exists an aδne
function⟨ 7! M ⟨ + ∼0 such that∼h = M ⟨ + ∼0 for˛ jV j values of ⟨ inH.

This proposition is a consequence of standard results in additive com-
binatorics, in particular the Balog-Szemer´edi-Gowers lemma and Freiman’s
theorem for vector spaces; see [TaVu2006 , x11.3] for further discussion.
The proof is elementary but a little lengthy and would take us too far aﬁeld,
so we simply assume this proposition for now and keep going. We conclude
that

(1.45) jEx2V ∆h{(§)e(M ⟨ ∆§)e(∼0 ∆§)j ˛ 1

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.5. Inverse conjecture over ﬁnite ﬁelds 85

for many ⟨ ∈ V .

The most diﬃcult term to deal with here is the quadratic term M ⟨ · §.
To deal with this term, suppose temporarily that M is symmetric, thus
M ⟨ · § = M §· ⟨. Then (since we are in odd characteristic) we can integrate
M ⟨ · § as
 M ⟨ · § = @h
  1
2 M § · § ´ − 1
2 M ⟨ · ⟨

and thus

|Ex2V {(§ + ⟨)e( 1
2 M(§ + ⟨) · (§ + ⟨)) {(§ )e(− 1
2 M § · § )e(∼· § )| ≫ 1

for many ⟨ ∈ H. Taking L2 norms in ⟨, we conclude that the U 2 inner
product between two copies of {(§)e( 
2M §·§) and two copies of {(§)e( 
2M §·
§)e(−∼· §). Applying the U 2 Cauchy-Schwarz-Gowers inequality, followed
by the U 2 inverse theorem, we conclude that {(§)e( 
2M §· § ) correlates with
e(˚) for some linear phase, and thus { itself correlates with e( ) for some
quadratic phase.

This argument also works (with minor modiﬁcation) when M is virtually
symmetric, in the sense that there exist a bounded index subspace ofV such
that the restriction of the form M ⟨ · § to V is symmetric, by foliating into
cosets of that subspace; we omit the details. On the other hand, if M is
not virtually symmetric, there is no obvious way to “integrate” the phase
e(M ⟨· §) to eliminate it as above. (Indeed, in order for M ⟨· § to be “exact”
in the sense that it is the “derivative” of something (modulo lower order
terms), e.g. M ⟨ · § ≈ @hΦ for some Φ, it must ﬁrst be “closed” in the sense
that @k(M ⟨·§) ≈ @h(M ∥·§) in some sense, since we have @h@k = @k@h; thus
we again see the emergence of cohomological concepts in the background.)

To establish the required symmetry on M, we return to Gowers’ argu-
ment from Lemma 1.5.7, and tweak it slightly. We start with (1.45) and
rewrite it as |Ex2V {(§ + ⟨){ 0(§)e(M ⟨ · §)| ≫ 1

where { 0(§) := {(§)e(∼· §). We square-average this in ⟨ to obtain

|Ex,y,h2V {(§ + ⟨){ 0(§ ){(y + ⟨) { 0(y )e(M ⟨ · (§ − y ))| ≫ 1:

Now we make the somewhat unusual substitution z = § + y + ⟨ to obtain

|Ex,y,z2V {(z − y ){ 0(§) {(z − §) { 0(y )e(M(z − § − y ) · (§ − y ))| ≫ 1:

Thus there exists z such that

|Ex,y2V {(z − y ){ 0(§ ){(z − §) { 0(y )e(M(z − § − y ) · (§ − y ))| ≫ 1:

We collect all terms that depend only on § (and z ) or only on y (and z ) to
obtain |Ex,y2V {z,(§){ z,2(y )e(M § · y − M y · §)| ≫ 1

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

86 1. Higher order Fourier analysis

for some bounded functions {z∅ 1∅ {z∅ 2. Eliminating these functions by two
applications of Cauchy-Schwarz, we obtain

jE§∅y∅§ 0∅y 02V e(M(§   § 0)  (y   y 0)   M(y   y 0)  (§   § 0))j ˛ 1

or, on making the change of variables a := §   § 0∅ ⌊:= y   y 0,

jEa∅⌊2V e(M a ⌊   M ⌊ a)j ˛ 1:

Using equidistribution theory, this means that the quadratic form (a∅ ⌊)7ω
M a ⌊  M ⌊ a is low rank, which easily implies that M is virtually symmetric.

Remark 1.5.9. In [Sa2007] a variant of this argument was introduced
to deal with the even characterisstic case. The key new idea is to split
the matrix of M into its diagonal component, plus the component that
vanishes on the diagonal. The latter component can made (virtually) (anti-
)symmetric and thus expressible U + U T where U is an upper-triangular
matrix; this allows for an integration as before, using U §  § in place of
1
2 M § §. In characteristic two, the diagonal contribution to M § § is linear
in § and can be easily handled by passing to a codimension one subspace.
See [Sa2007] for details.

Now we turn to the general d case. In principle, the above argument
should still work, say for d = 3. The main sticking point is that instead of
dealing with a vector-valued function ⟨ 7ω∼⟨ that is approximately linear in
the sense that (1.44) holds for many additive quadruples, in the d = 3 case
one is now faced with a matrix-valuedfunction ⟨ 7ω M⟨ with the property
that M⟨ 1 + M⟨ 2 = M⟨ 3 + M⟨ 4 + L⟨ 1∅⟨2∅⟨3∅⟨4
for many additive quadruples ⟨ 1∅ ⟨2∅ ⟨3∅ ⟨4, where the matrix L⟨ 1∅⟨2∅⟨3∅⟨4 has
bounded rank. With our current level of additive combinatorics technology,
we are not able to deal properly with this bounded rank error (the main
diﬃculty being that the set of low rank matrices has no good “doubling”
properties). Because of this obstruction, no generalisation of the above
arguments to higher d has been found.

There is however another approach, based ultimately on the ergodic the-
ory work of Host-Kra [HoKr2005] and of Ziegler [Zi2007], that can handle
the general d case, which was worked out in [TaZi2010, BeTaZi2010]. It
turns out that it is convenient to phrase these arguments in the language
of ergodic theory. However, in order not to have to introduce too much
additional material, we will describe the arguments here in the case d = 3
without explicitly using ergodic theory notation. To do this, though, we will
have to sacriﬁce a lot of rigour and only work with some illustrative special
cases rather than the general case, and also use somewhat vague terminology
(e.g. “general position” or “low rank”).

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.5. Inverse conjecture over ﬁnite ﬁelds 87

To simplify things further, we will establish the U 3 inverse theorem
only for a special type of function, namely a quartic phase∞4e(˚), where
˚: V ! F is a classical polynomial of degree 4. The claim to show then
is that if ke(˚)kU 3(V)˛ 1, then e(˚) correlates with a cubic phase. In the
high characteristic case √ >4, this result can be handled by equidistribution
theory. Indeed, since

ke(˚)k
8
U 3(V)= Ex;h 1;h 2;h 3;h 4 e(@h 1 @h 2 @h 3 @h 4 ˚(§))∅

that theory tells us that the quartic polynomial (§∅ ⟨ ∞∅ ⟨∈∅ ⟨3∅ ⟨4) 7! @h 1 @h 2 @h 3 @h 4 ˚(§)
is low rank. On the other hand, in high characteristic one has the Taylor
expansion
 ˚(§) = 1
4! @x @x @x @x ˚(0) +Q(§)

for some cubic function Q (as can be seen for instance by decomposing into
monomials). From this we easily conclude that ˚ itself has low rank (i.e.
it is a function of boundedly many cubic (or lower degree) polynomials), at
which point it is easy to see from Fourier analysis that e(˚) will correlate
with the exponential of a polynomial of degree at most 3.

Now we present a diﬀerent argument that relies slightly less on the quar-
tic nature of ˚; it is a substantially more diﬃcult argument, and we will skip
some steps here to simplify the exposition, but the argument happens to ex-
tend to more general situations. As ke(˚)kU 3 ˛ 1, we have k∆h e(˚)kU 2 ˛ 1
for many ⟨, thus by the inverse U ∈ theorem, ∆h e(˚) = e(@h ˚) correlates with
a quadratic phase. Using equidistribution theory, we conclude that the cubic
polynomial @h ˚ is low rank.

At present, the low rank property for @h ˚ is only true for many ⟨. But
from the cocycle identity

(1.46) @h+k ˚= @h ˚+ T h @k ˚∅

we see that if @h ˚ and @k ˚ are both low rank, then so is @h+k ˚; thus the
property of @h ˚being low rank is in some sense preserved by addition. Using
this and a bit of additive combinatorics, one can conclude that @h ˚ is low
rank for all ⟨ in a bounded index subspace of V ; restricting to that subspace,
we will now assume that @h ˚ is low rank for all ⟨ 2 V . Thus we have

@h ˚= Fh ( ~Qh )

where ~Qh is some bounded collection of quadratic polynomials for each ⟨,
and Fh is some function. To simplify the discussion, let us pretend that ~Qh

∞4A }ood e§am√le to ∥ee√ ⟩\ m⟩\d ⟩s t⟨e symmetr⟩⌋ √oly\om⟩al √⟨ase e(S2=∈) {rom Se⌋t⟩o\
∞.5.∈, t⟨ou}⟨ o\e ⟨as to ta∥e some ⌋are w⟩t⟨ t⟨⟩s e§am√le due to t⟨e low ⌋⟨ara⌋ter⟩st⟩⌋.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

88 1. Higher order Fourier analysis

in fact consists of just a single quadratic Q⟨ , plus some linear polynomials
~L⟨ , thus

(1.47) @⟨ ˚= F⟨ (Q⟨ ∅~L⟨ )

There are two extreme cases to consider, depending on how Q⟨ depends
on ⟨. Consider ﬁrst a “core” case when Q⟨ = Q is independent of ⟨. Thus

(1.48) @⟨ ˚= F⟨ (Q∅~L⟨ )

If Q is low rank, then we can absorb it into the L⟨ factors, so suppose instead
that Q is high rank, and thus equidistributed even after ﬁxing the values of
L⟨ .
 The function @⟨ ˚ is cubic, and Q is a high rank quadratic. Because
of this, the function F0(Q∅ L⟨ ) must be at most linear in the Q variable;
this can be established by another application of equidistribution theory,
see [GrTa2009, x8]. Thus one can factorise

@⟨ ˚= QF0
⟨ (L⟨ ) + F00
⟨ (L⟨ )

for some functions F0
⟨ ∅ F00
⟨ . In fact, as @⟨ ˚ is cubic, F0
⟨ must be linear, while
F00
⟨ is cubic.

By comparing the Q coeﬃcients F00
⟨ (L⟨ ) in the cocycle equation (1.46),
we see that the function ⊂⟨ := F00
⟨ (L⟨ ) is itself a cocycle:

⊂⟨+∥ = ⊂⟨ + T ⟨ ⊂∥ :

As a consequence, we have ⊂⟨ = @⟨ R for some function R: V ! R=Z. Since
⊂⟨ is linear, R is quadratic; thus we have

(1.49) @⟨ ˚= Q@⟨ R + F00
⟨ (L⟨ ):

With a high characteristic assumption √ >2, one can ensure R is classical.
We will assume that R is high rank, as this is the most diﬃcult case.

Suppose ﬁrst that Q = R. In high characteristic, one can then integrate
Q@⟨ Q by expressing this as @⟨ ( 1
2Q2) plus lower order terms, thus @⟨ (˚  1
2Q2)
is an order 1 function in the sense that it is a function of a bounded number of
linear functions. In particular, e(@⟨ (˚  1
2Q2)) has a large U 2 norm for all ⟨,
which implies that e(˚  1
2Q2) has a large U 3 norm, and thus correlates with
a quadratic phase. Since e( 1
2Q2) can be decomposed by Fourier analysis into
a linear combination of quadratic phases, we conclude that e(˚) correlates
with a quadratic phase and one is thus done in this case.

Now consider the other extreme, in which Q and R lie in general position.
Then, if we diﬀerentiate (1.49) in ∥, we obtain one has

@∥ @⟨ ˚= @∥ Q@⟨ R + Q@∥ @⟨ R + @∥ Q(@∥ @⟨ R) + @∥ F00
⟨ (L⟨ )∅

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.5. Inverse conjecture over ﬁnite ﬁelds 89

and then anti-symmetrising in ∥∅ ⟨ one has

0 = @∥ Q@⟨ R Γ @⟨ Q@∥ R + (@∥ Q Γ @⟨ Q)@∥ @⟨ R + @∥ F00
⟨ (L⟨ ) Γ @⟨ F00
∥ (L⟨ ):

If Q and R are unrelated, then the linear forms @∥ Q∅ @∥ R will typically be
in general position with respect to each other and with L⟨ , and similarly
@⟨ Q∅ @⟨ R will be in general position with respect to each other and with
L∥ . From this, one can show that the above equation is not satisﬁable
generically, because the mixed terms @∥ Q@⟨ RΓ @⟨ Q@∥ R cannot be cancelled
by the simpler terms in the above expression.

An interpolation of the above two arguments can handle the case in
which Q⟨ does not depend on ⟨. Now we consider the other extreme, in
which Q⟨ varies in ⟨, so that Q⟨ and Q∥ are in general position for generic
⟨∅ ∥, and similarly
15 for Q⟨ and Q⟨+∥ , or for Q∥ and Q⟨+∥ .

To analyse this situation, we return to the cocycle equation (1.46), which
currently reads

(1.50) F⟨+∥ (Q⟨+∥ ∅~L⟨+∥ ) = F⟨ (Q⟨ ∅~L⟨ ) + T ⟨ F∥ (Q∥ ∅~L∥ ):

Because any two of Q⟨+∥ ∅ Q⟨ ∅ Q∥ can be assumed to be in general position,
one can show using equidistribution theory that the above equation can only
be satisﬁed when the F⟨ are linear in the Q⟨ variable, thus

@⟨ ˚= Q⟨ F0
⟨ (~L⟨ ) + F00
⟨ (~L⟨ )

much as before. Furthermore, the coeﬃcients F0
⟨ (~L⟨ ) must now be (essen-
tially) constant in ⟨ in order to obtain (1.50). Absorbing this constant into
the deﬁnition of Q⟨ , we now have

@⟨ ˚= Q⟨ + F00
⟨ (~L⟨ ):

We will once again pretend that ~L⟨ is just a single linear form L⟨ . Again
we consider two extremes. If L⟨ = L is independent of ⟨, then by passing
to a bounded index subspace (the level set of L) we now see that @⟨ ˚ is
quadratic, hence ˚ is cubic, and we are done. Now suppose instead that
L⟨ varies in ⟨, so that L⟨ ∅ L∥ are in general position for generic ⟨∅ ∥. We
look at the cocycle equation again, which now tells us that F00
⟨ (~L⟨ ) obeys
the quasicocyclecondition

Q⟨∅∥ + F00
⟨+∥ (~L⟨+∥ ) = F00
⟨ (~L⟨ ) + T ⟨ F00
∥ (~L∥ )

where Q⟨∅∥ := Q⟨+∥ Γ Q⟨ Γ T ⟨ Q∥ is a quadratic polynomial. With any two
of L⟨ ∅ L∥ ∅ L⟨+∥ in general position, one can then conclude (using equidis-
tribution theory) that F00
⟨ ∅ F00
∥ ∅ F00
⟨+∥ are quadratic polynomials. Thus @⟨ ˚

15Note though that we cannot simultaneously assume that Qh ∅ Qk ∅ Qh〉k are in general
position; indeed, Qh might vary linearly in ⟨, and indeed we expect this to be the basic behaviour
of Qh here, as was observed in the preceding argument.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

90 1. Higher order Fourier analysis

is quadratic, and ˚ is cubic as before. This completes the heuristic discus-
sion of various extreme model cases; the general case is handled by a rather
complicated combination of all of these special case methods, and is best
performed
∞̸ in the framework of ergodic theory; see [BeTaZi2010 ]. The
various functional equations for these vertical derivatives were ﬁrst intro-
duced by Conze and Lesigne [CoLe1984].

1.5.4. Consequences of the inverse conjecture for the Gowers norm.
We now discuss brieﬂy some of the consequences of the inverse conjecture for
the Gowers norm, beginning with Szemer´edi’s theorem in vector ﬁelds (The-
orem 1.5.4). We will use the density increment method17. Let A ˆ V = Fn

be a set of density at least ◦ containing no lines. This implies that the
√-linear form

Λ(1A∅ : : : ∅1A) := Ex;r2F n1A(§) : : :1A(§ + (√  1)r)

has size o(1). On the other hand, as this pattern has complexity √  2, we
see from Section 1.3 that one has the bound

jΛ({0 ∅ : : : ∅ {p ∞ )j ˇ sup
0j p ∞ k{j kUp 1 (V)

whenever {0 ∅ : : : ∅ {p ∞ are bounded in magnitude by 1. Splitting 1A = ◦ +
(1A   ◦), we conclude that

Λ(1A∅ : : : ∅1A) = ◦
p + Op(k1A   ◦kUp 1 (V))

and thus (for \ large enough)

k1A   ◦kUp 1 (V)˛ p;1:

Applying Theorem 1.5.3, we ﬁnd that there exists a polynomial ˚ of degree
at most √  2 such that
 jh1A   ◦∅ e(˚)ij ˛p;1:

To proceed we need the following analogue of Proposition 1.2.6:

Exercise 1.5.6 (Fragmenting a polynomial into subspaces). Let ˚: Fn ! F
be a classical polynomial of degree d < √. Show that one can partition V
into aﬃne subspaces W of dimension at least \ 0(\∅ d∅ √), where \ 0 ! 1 as
\ ! 1 for ﬁxed d∅ √, such that˚ is constant on each W. (H⟩\t:Induct
on d, and use Exercise 1.4.6 repeatedly to ﬁnd a good initial partition into
subspaces on which ˚ has degree at most d   1.)

Exercise 1.5.7. Use the previous exercise to complete the proof of Theorem
1.5.4. (H⟩\t:mimic the density increment argument from Section 1.2.)

∞̸⟩\ √art⟩⌋ular, t⟨e ⟩dea o{ e§tra⌋t⟩\} out t⟨e ⌋oe◦⌋⟩e\t o{ a ∥ey √oly\om⟩al, su⌋⟨ as t⟨e
⌋oe◦⌋⟩e\t F 0
h(Lh) o{Q, ⟩s ⌊est ⌋a√tured ⌊y t⟨e er}od⟩⌋ t⟨eory ⌋o\⌋e√t o{vertical diαerentiation.
A}a⟩\, see ∪BeTa∫i2] {or deta⟩ls.
17 A\ e\er}y ⟩\⌋reme\t ar}ume\t ⟩s also √oss⟩⌊le, ⌊ut ⟩s more ⌋om√l⟩⌋ated∅ see ∪GrTa2b].

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.5. Inverse conjecture over ﬁnite ﬁelds 91

By using the inverse theorem as a substitute for Lemma 1.2.8, one ob-
tains the following regularity lemma, analogous to Theorem 1.2.11:

T⟨eorem ∞.5.∞0(Strong arithmetic regularity lemma).Su√√ose t⟨atchar(F) =
p > d  0. Letf : V ω [0; 1], let” > 0, a\d letF : R+ ω R+ ⌊e a\ ar-
⌊⟩trary {u\⌋t⟩o\. T⟨e\ we ⌋a\ de⌋om√osef = f str + f sml + f psd a\d \d
1  M = O";F;d;p(1) su⌋⟨ t⟨at

(i) (No\\e}at⟩v⟩ty)f str ; f str + f sml ta∥e values ⟩\[0; 1], a\df sml ; f psd
⟨ave mea\ zero∅

(ii) (Stru⌋ture)f str ⟩s a {u\⌋t⟩o\ o{M ⌋lass⟩⌋al √oly\om⟩als o{ de}ree
at mostd∅

(iii) (Small\ess)f sml ⟨as a\ L2(V) \orm o{ at most ”∅ a\d

(iv) (Pseudora\dom\ess) O\e ⟨askf psd kUd〉(V)  1=F(M ) {or allﬀ 2
R.

For a proof, see [Ta∈00↦]. The argument is similar to that appear-
ing in Theorem 1.2.11, but the discrete nature of polynomials in bounded
characteristic allows one to avoid a number of technical issues regarding
measurability.

This theorem can then be used for a variety of applications in additive
combinatorics. For instance, it gives the following variant of a result of
Bergelson, Host, and Kra [BeHoKa∈005 ]:

Pro√os⟩t⟩o\ ∞.5.∞∞.Letp > 4  k, letF = Fp, a\d letA ρ Fn w⟩t⟨
jAj ﬃjFnj, a\d let” > 0. T⟨e\ {or˛ ;";pjFnj values o{h 2 Fn, o\e ⟨as

jfx 2 Fn : x; x + h; : : : ; x + (k   1)h 2 Agj  (ﬃ
k   ”)jF
nj:

Roughly speaking, the idea is to apply the regularity lemma to f := 1A,
discard the contribution of the f sml and f psd errors, and then control the
structured component using the equidistribution theory from Section 1.4. A
proof of this result can be found in [Gr∈00↦]; see also [GrTa∈0∞0⌊] for an
analogous result in Z=NZ. Curiously, the claim fails when 4 is replaced by
any larger number; this is essentially an observation of Ruzsa that appears
in the appendix of [BeHoKa∈005 ].

The above regularity lemma (or more precisely, a close relative of this
lemma) was also used in [GoWo∈0∞0⌊]:

T⟨eorem ∞.5.∞∈(Gowers-Wolf theorem).[GoWo∈0∞0⌊] LetΨ = (  1; : : : ;   t)
⌊e a ⌋olle⌋t⟩o\ o{ l⟩\ear {orms w⟩t⟨ ⟩\te}er ⌋oe◦⌋⟩e\ts, w⟩t⟨ \o two {orms
⌊e⟩\} l⟩\early de√e\de\t. LetF ⟨ave su◦⌋⟩e\tly lar}e ⌋⟨ara⌋ter⟩st⟩⌋, a\d
su√√ose t⟨atf 1; : : : ; f t : Fn ω C are {u\⌋t⟩o\s ⌊ou\ded ⟩\ ma}\⟩tude ⌊y1
su⌋⟨ t⟨at jΛ	 (f 1; : : : ; f t)j  ﬃ

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

92 1. Higher order Fourier analysis

w⟨ereΛ	 was t⟨e {orm de\ed ⟩\ Se⌋t⟩o\ ∞.3. T⟨e\ {or ea⌋⟨1 ˇ i ˇ t t⟨ere
e§⟩sts a ⌋lass⟩⌋al √oly\om⟩alφi o{ de}ree at mostd su⌋⟨ t⟨at

jhfi, e(φi)i L 2(Fn )j ˛d;	;ﬃ1,

w⟨ered ⟩s t⟨e true ⌋om√le§⟩ty o{ t⟨e systemΨ as de\ed ⟩\ Se⌋t⟩o\ ∞.3.
T⟨⟩s d ⟩s ⌊est √oss⟩⌊le.

1.6. The inverse conjecture for the Gowers norm II. The
integer case

In Section 1.5, we saw that the Gowers uniformity norms on vector spaces
Fn were controlled by classical polynomial phases e(φ).

Now we study the analogous situation on cyclic groups Z/NZ. Here,
there is an unexpected surprise: the polynomial phases (classical or other-
wise) are no longer suﬃcient to control the Gowers norms Us+∞(Z/NZ) once
s exceeds 1. To resolve this problem, one must enlarge the space of poly-
nomials to a larger class. It turns out that there are at least three closely
related options for this class: the lo⌋al √oly\om⟩als, the ⌊ra⌋∥et √oly\om⟩als,
and the \⟩lseque\⌋es. Each of the three classes has its own strengths and
weaknesses, but in my opinion the nilsequences seem to be the most natural
class, due to the rich algebraic and dynamical structure coming from the
nilpotent Lie group undergirding such sequences. For reasons of space we
shall focus primarily on the nilsequence viewpoint here.

Traditionally, nilsequences have been deﬁned in terms of linear orbits
n 7! gn x on nilmanifolds G/Γ; however, in recent years it has been realised
that it is convenient for technical reasons (particularly for the quantitative
“single-scale” theory) to generalise this setup to that of √oly\om⟩al orbits
n 7! g(n)Γ, and this is the perspective we will take here.

A polynomial phase n 7! e(φ(n)) on a ﬁnite abelian group H is formed
by starting with a polynomial φ: H ! R/Z to the unit circle, and then
composing it with the exponential function e: R/Z ! C. To create a
nilsequence n 7! F (g(n)Γ), we generalise this construction by starting with
a polynomial gΓ : H ! G/Γ into a \⟩lma\⟩{old G/Γ, and then composing
this with a Lipschitz
∞8function F : G/Γ ! C. These classes of sequences
certainly include the polynomial phases, but are somewhat more general;
for instance, they almost
∞9include ⌊ra⌋∥et √oly\om⟩alphases such as n 7!
e(bαncβn).

∞8T⟨e L⟩√s⌋⟨⟩tz re}ular⟩ty ⌋lass ⟩s ⌋o\ve\⟩e\t {or m⟩\or te⌋⟨\⟩⌋al reaso\s, ⌊ut o\e ⌋ould also
use ot⟨er re}ular⟩ty ⌋lasses ⟨ere ⟩{ des⟩red.
∞9T⟨e ∩almost" ⟨ere ⟩s ⌊e⌋ause t⟨e releva\t {u\⌋t⟩o\sF :G=−→ C ⟩\volved are o\ly √⟩e⌋e-
w⟩se L⟩√s⌋⟨⟩tz rat⟨er t⟨a\ L⟩√s⌋⟨⟩tz, ⌊ut t⟨⟩s ⟩s √r⟩mar⟩ly a te⌋⟨\⟩⌋al ⟩ssue a\d o\e s⟨ould v⟩ew
⌊ra⌋∥et √oly\om⟩al √⟨ases as ∩morally" ⌊e⟩\} \⟩lseque\⌋es.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.6. Inverse conjecture over the integers 93

In this section we set out the basic theory for these nilsequences, in-
cluding their equidistribution theory (which generalises the equidistribution
theory of polynomial ﬂows on tori from Section 1.1) and show that they
are indeed obstructions to the Gowers norm being small. This leads to the
⟩\verse ⌋o\|e⌋ture {or t⟨e Gowers \ormsthat shows that the Gowers norms
on cyclic groups are indeed controlled by these sequences.

∞.̸.∞. Ge\eral t⟨eory o{ √oly\om⟩al ma√s.In previous sections, we
deﬁned the notion of a (non-classical) polynomial map ˚of degree at most
d between two additive groups H; G, to be a map ˚: H ω G obeying the
identity @h 1 : : : @h d+1 ˚(x) = 0

for all x; h; : : : ; hd〉 2 H , where @h ˚(x) :=˚(x+ h)   ˚(x) is the additive
discrete derivative operator.

There is another way to view this concept. For any k; d  0, deﬁne
the Host-Kra }rou√HK
k (H;  d) of H of dimension k and degree d to be
the subgroup of H f;gd consisting of all tuples (x! )! 2f;gk obeying the
constraints X

! 2F ( 1) j! jx! = 0

for all faces F of the unit cube f0; 1gk of dimension at least d + 1, where
j(! ; : : : ; ! k )j := ! +    + ! k . (These constraints are of course trivial if
k  d.) A r-dimensional face of the unit cube f0; 1gk is of course formed by
freezing k   r of the coordinates to a ﬁxed value in f0; 1g, and letting the
remaining r coordinates vary freely in f0; 1g.

Thus for instance HK
2(H;  1) is (essentially) space of parallelograms
(x; x + h; x + k; x + h + k) in H 4, while HK2(H;  0) is the diagonal group
f(x; x; x; x) : x 2 H 4g, and HK
2(H;  2) is all of H 4.

E§er⌋⟩se ∞.̸.∞.Let ˚: H ω G be a map between additive groups, and let
k > d  0. Show that ˚is a (non-classical) polynomial of degree at most d if
it maps HK
k (H;  1) to HK
k (G;  d), i.e. that (˚(x! ))! 2f;gk 2 HK
k (G; 
d) whenever (x! )! 2f;gk 2 HKk (H;  1).

It turns out (somewhat remarkably) that these notions can be satisfac-
torily generalised to non-abelian setting, this was ﬁrst observed by Leib-
man [Le∞998, Le∈00∈]. The (now multiplicative) groupsH; G need to be
equipped with an additional structure, namely that of a ltrat⟩o\.

De\⟩t⟩o\ ∞.̸.∞(Filtration).A ltrat⟩o\on a multiplicative group G is a
family (Gi )1
i= of subgroups of G obeying the nesting property

G  G  G  : : :

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

94 1. Higher order Fourier analysis

and the ﬁltration property
 [G ≥i ∅ G≥j ] ρ G ≥i+j

for all ⟩∅ |  0, where [H∅ K] is the group generated by f[⟨∅ ∥] : ⟨ 2 H∅ ∥ 2
K g, where [⟨∅ ∥] := ⟨∥⟨ −1∥−1 is the commutator of ⟨ and ∥. We will refer
to the pair G • = (G∅ (G ≥i )∞
i=0 ) as a ﬁltered group. We say that an element }
of G has degree ⟩ if it belongs to G ≥i , thus for instance a degree  ⟩ and
degree  | element will commute modulo  ⟩ + | errors.

In practice we usually have G ≥0 = G. As such, we see that [ G∅ G ≥j ] ρ
G ≥j for all | , and so all the G ≥j are normal subgroups of G.

Exercise 1.6.2.Deﬁne the lower central series

G = G 0 = G 1  G 2  : : :

of a group G by setting G 0∅ G1 := G and G i+1 := [G∅ G i] for ⟩  1. Show
that the lower central series (G j )∞
j =0 is a ﬁltration of G. Furthermore, show
that the lower central series is the minimal ﬁltration that starts at G, in the
sense that if (G 0
≥j )∞
j =0 is any other ﬁltration with G 0
≥0 = G, then G 0
≥j ˙ G ≥j
for all | .

Example 1.6.2. If G is an abelian group, and d  0, we deﬁne the degree
d ﬁltration (G∅  d) on G by setting G ≥i := G if ⟩  d and G ≥i = fidg for
⟩ > d.

Example 1.6.3. If G • = (G∅ (G ≥i )∞
i=0 ) is a ﬁltered group, and ∥  0, we
deﬁne the shifted ﬁltered group G +k
• := (G∅ (G ≥i+k )∞
i=0 ); this is clearly again
a ﬁltered group.

Deβnition 1.6.4 (Host-Kra groups). Let G • = (G∅ (G ≥i )∞
i=0 ) be a ﬁltered
group, and let ∥  0 be an integer. The Host-Kra groupHKk(G •) is the
subgroup of G {0;1} k generated by the elements }F with F an arbitrary face
in f0∅1gk and } an element of G ≥k−dim(F ), where }F is the element of G {0;1} k

whose coordinate at →is equal to } when →2 F and equal to fidg otherwise.

From construction we see that the Host-Kra group is symmetric with
respect to the symmetry group Sk n (Z=2Z)k of the unit cube f0∅1gk. We
will use these symmetries implicitly in the sequel without further comment.

Example 1.6.5.Let us parameterise an element of G {0;1} 2 as (}00∅ }01∅ }10∅ }11).
Then HK
2(G) is generated by elements of the form ( }0∅ }0∅ }0∅ }0) for }0 2
G ≥0, (id∅id∅ }1∅ }1) and (id∅ }1∅id∅ }1), and (id∅id∅id∅ }2) for }0 2 G ≥0∅ }1 2
G ≥1∅ }2 2 G ≥2. (This does not cover all the possible faces of f0∅1g2, but
it is easy to see that the remaining faces are redundant.) In other words,
HK
2(G) consists of all group elements of the form ( }0∅ }0}1∅ }0}0
1∅ }0}1}0
1}2),
where }0 2 G ≥0, }1∅ }0
1 2 G ≥1, and }2 2 G ≥2. This example is generalised
in the exercise below.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.6. Inverse conjecture over the integers 95

E§er⌋⟩se ∞.̸.3.Deﬁne a lower {a⌋eto be a face of a discrete cube f0, 1gk

in which all the frozen coeﬃcients are equal to 0. Let us order the lower
faces as F1, . . . , F2k (1 in such a way that i  j whenever Fi is a subface of
Fj . Let G be a ﬁltered group. Show that every element of HK
k (G) has a
unique representation of the form Q2k  ∞
i=0 (gi)Fi , where gi 2 Gk (dim(F i ) and
the product is taken from left to right (say).

E§er⌋⟩se ∞.̸.4.If G is an abelian group, show that the group HK
k (G, ˇ d)
deﬁned in Deﬁnition 1.6.4 agrees with the group deﬁned at the beginning of
this section for additive groups (after transcribing the former to multiplica-
tive notation).

E§er⌋⟩se ∞.̸.5.Let G be a ﬁltered group. Let F be an r-dimensional face
of f0, 1gk . Identifying F with f0, 1gr in an obvious manner, we then obtain
a restriction homomorphism from Gf0;1gk with GF  Gf0;1gr . Show that the
restriction of any element of HKk (G) to Gf0;1gr then lies in HK
r (G).

E§er⌋⟩se ∞.̸.̸.Let G be a ﬁltered group, let k  0 and l  1 be integers,
and let g = (g! )! 2f0;1gk and h = (h! )! 2f0;1gk be elements of Gf0;1gk . Let

f = (f! )! 2f0;1gk +l be the element of Gf0;1gk +l deﬁned by setting f! k ;! l for
ωk 2 f0, 1gk , ωl 2 f0, 1gl to equal g! k for ωl 6= (1, . . . ,1), and equal to
g! k h! k otherwise. Show that f 2 HKk +l(G) if and only if g 2 HKk (G)
and h 2 HKk (G+l
 ), where G+l
 is deﬁned in Example 1.6.3. (H⟩\t:use
Exercises 1.6.3, 1.6.5.)

E§er⌋⟩se ∞.̸.↦.Let G be a ﬁltered group, let k  1, and let g = (g! )! 2f0;1gk
be an element of Gf0;1gk . We deﬁne the der⟩vat⟩ve@1g 2 Gf0;1gk  ∞ in the
ﬁrst variable to be the tuple (g!;1 g(1
!;0 )! 2f0;1gk  ∞ . Show that g 2 HKk (G) if
and only if the restriction of g to f0, 1gk (1 lies in HKk (1 (G) and @1g lies
in HKk (G+1
 ), where G+1
 is deﬁned in Example 1.6.3.

Remar∥ ∞.̸.̸.The the Host-Kra groups of a ﬁltered group in fact form
a ⌋u⌊⟩⌋ ⌋om√le§, a concept used in topology; but we will not pursue this
connection here.

In analogy with Exercise 1.6.1, we can now deﬁne the general notion of
a polynomial map:

De\⟩t⟩o\ ∞.̸.↦.A map φ: H ! G between two ﬁltered groups H, G is
said to be √oly\om⟩al if it maps HKk (H) to HKk (G) for each k  0. The
space of all such maps is denoted Poly(H ! G).

Since HKk (H), HK
k (G) are groups, we immediately obtain
20

20From our choice of deﬁnitions, this theorem is a triviality, but the theorem is less trivial
when using an alternate but non-trivially equivalent deﬁnition of a polynomial, which we will give

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

96 1. Higher order Fourier analysis

T⟨eorem ∞.̸.8(Lazard-Leibman theorem).Poly(Hω G ) forms a group
under pointwise multiplication.

In a similar spirit, we have

T⟨eorem ∞.̸.9 (Filtered groups and polynomial maps form a category).
If ˚: H ω G and  : G ω K are polynomial maps between ﬁltered groups
H∅ G∅ K, then  δ ˚: H ω K is also a polynomial map.

We can also give some basic examples of polynomial maps. Any constant
map from H to G taking values in G 0 is polynomial, as is any map ˚: H ω
G which is a ﬁltered homomorphism in the sense that it is a homomorphism
from Hi to G i for any ⟩  0.

Now we turn to an alternate deﬁnition of a polynomial map. For any ⟨ 2
H and any map ˚: H ω G Deﬁne the multiplicative derivative ∆h˚: H ω G
by the formula ∆h˚(§) := ˚(⟨§)˚(§) Γ1 .

T⟨eorem ∞.̸.∞0(Alternate description of polynomials).Let ˚: H ω G be
a map between two ﬁltered groups H∅ G. Then ˚ is polynomial if and only
if, for any ⟩1∅ : : : ∅ ⟩m  0, § 2 H0 , and ⟨ j 2 Hi j for | = 1∅ : : : ∅ m, one
has ∆h1 : : :∆hm ˚(§) 2 G i 1+∆∆∆+im .

In particular, from Exercise 1.6.1, we see that a non-classical polynomial
of degree d from one additive group H to another G is the same thing as a
polynomial map from (H∅ 1) to (G∅  d). More generally, a ˚ map from
(H∅ 1) to a ﬁltered group G  is polynomial if and only if

∆h1 : : :∆hi˚(§) 2 G i

for all ⟩  0 and §∅ ⟨ 1∅ : : : ∅ ⟨i 2 H.

Proo{.We ﬁrst prove the “only if” direction. It is clear (by using 0-
dimensional cubes) that a polynomial map must map H0 to G 0 . To
obtain the remaining cases, it suﬃces by induction on m to show that if ˚
is polynomial from H to G , and ⟨ 2 Hi for some ⟩  0, then ∆h˚ is
polynomial from H to G +i
 . But this is easily seen from Exercise 1.6.7.

Now we establish the “if” direction. We need to show that ˚ maps
HKk(H) to HK
k(G ) for each ∥. We establish this by induction on ∥. The
case ∥ = 0 is trivial, so suppose that ∥  1 and that the claim has already
been estabilshed for all smaller values of ∥.

Let ⟨ 2 HKk(H). We split Hf0,1g k as Hf0,1g k  1  Hf0,1g k  1 . From Ex-
ercise 1.6.7 we see that we can write ⟨ = (⟨ 0∅ ⟨1⟨ 0) where ⟨ 0 2 HKkΓ1 (H)

shortly. Lazard [La∞954] gave a version of this theorem whenH was the integers andG was a
nilpotent Lie group; the general problem of multiplying polynomial sequences was considered by
Leibman [Le∞99∀].

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.6. Inverse conjecture over the integers 97

and ⟨ ∞ 2 HKk ∞ (H+∞
 ), thus ˚(⟨) = (˚(⟨0 )∅ ˚(⟨ ∞⟨ 0 )) (extending ˚ to act
on Hf0,∞g k  or Hf0,∞g k in the obvious manner). By induction hypothe-
sis, ˚(⟨0 ) 2 HK
k ∞ (G ), so by Exercise 1.6.7, it suﬃces to show that
˚(⟨∞⟨ 0 )˚ ∞ (⟨ 0 ) 2 HKk ∞ (G +∞
 ).

By telescoping series, it suﬃces to establish this when ⟨ ∞= ⟨ F for some
face F of some dimension r in f0∅ 1gk ∞ and some ⟨ 2 Hk  r , as these
elements generate HKk ∞ (H+∞
 ). But then ˚(⟨∞⟨ 0 )˚ ∞ (⟨ 0 ) vanishes outside
of F and is equal to ∆h˚(⟨0 ) on F, so by Exercise 1.6.6 it will suﬃce to
show that ∆h˚(⟨0
0 ) 2 HKr(G +k  r
 ), where ⟨ 0
0 is ⟨ 0 restricted to F (which
one then identiﬁes with f0∅ 1gr). But by the induction hypothesis, ∆h˚
maps HK
r(H) to HKr(H+k  r
 ), and the claim then follows from Exercise
1.6.5. 

Exercise 1.6.8. Let ⟩∞∅ : : : ∅ ⟩k  0 be integers. If G  is a ﬁltered group,
deﬁne HK
(i,...,ik )(G ) to be the subgroup of G f0,∞g k generated by the ele-
ments }F , where F ranges over all faces of f0∅ 1gk and } 2 G i j ++i j r ,
where 1 ˇ | ∞ < ∆ ∆ ∆< | r ˇ ∥ are the coordinates of F that are frozen.
This generalises the Host-Kra groups HKk(G ), which correspond to the
case ⟩∞= ∆ ∆ ∆= ⟩k = 1. Show that if ˚ is a polynomial map from H to G ,
then ˚ maps HK(i,...,ik )(H) to HK
(i,...,ik )(G ).

Exercise 1.6.9. Suppose that ˚: H ! G is a non-classical polynomial of
degree ˇ d from one additive group to another. Show that ˚is a polynomial
map from (H∅ˇ m) to (G∅ ˇ dm) for every m  1. Conclude in particular
that the composition of a non-classical polynomial of degree ˇ d and a non-
classical polynomial of degree ˇ d 0 is a non-classical polynomial of degree
ˇ dd 0.

Exercise 1.6.10. Let ˚∞: H ! G ∞, ˚∈: H ! G ∈ be non-classical polynomi-
als of degrees ˇ d ∞, ˇ d ∈ respectively between additive groups H∅ G∞∅ G∈, and
let B : G ∞G ∈ ! G be a bihomomorphism to another additive group (i.e. B
is a homomorphism in each variable separately). Show that B (˚∞∅ ˚∈) : H !
G is a non-classical polynomial of degree ˇ d ∞+ d ∈.

1.6.2. Nilsequences. We now specialise the above theory of polynomial
maps ˚: H ! G to the case when H is just the integers Z = (Z∅ˇ 1)
(viewed additively) and G is a nilpotent group. Recall that a group G is
\⟩lpote\tof step at most s if the (s + 1)t⟨ group G s+∞ in the lower central
series vanishes; thus for instance a group is nilpotent of step at most 1 if and
only if it is abelian. Analogously, let us call a ﬁltered group G  \⟩lpote\t
of degree at most s if G s+∞ vanishes. Note that if G 0 = G and G  is
nilpotent of degree at most s, then G is nilpotent of step at most s. On the
other hand, the degree of a ﬁltered group can exceed the step; for instance,
given an additive group G and an integer d  1, (G∅ ˇ d) has degree d but

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

98 1. Higher order Fourier analysis

step 1. The step is the traditional measure of nilpotency for groups, but the
degree seems to be a more suitable measure in the ﬁltered group category.

We refer to sequences } : Z ! G which are polynomial maps from (Z∅ˇ
1) to G  as polynomial sequences adapted to G  . The space of all such
sequences is denoted Poly(Z ! G); by the machinery of the previous section,
this is a multiplicative group. These sequences can be described explicitly:

E§er⌋⟩se ∞.̸.∞∞.Let s  0 be an integer, and let G  be a ﬁltered group
which is nilpotent of degree s. Show that a sequence } : Z ! G is a polyno-
mial sequence if and only if one has

(1.51) }(\) = }0}(n
)
1 }(
n
2)
2 : : : }
(
n
s )
s

for all \ 2 Z and some }i 2 G i for ⟩ = 0∅ : : : ∅ s, where   n
i := n(n 1):::(n i+1)
i! .
Furthermore, show that the }i are unique. We refer to the }0∅ : : : ∅ }s as the
Taylor coeﬃcients of } at the origin.

E§er⌋⟩se ∞.̸.∞∈.In a degree 2 nilpotent group G, establish the formula

}n⟨ n = (}⟨) n[}∅ ⟨]
  (
n
2)

for all }∅ ⟨ 2 G and \ 2 Z. This is the ﬁrst non-trivial case of the Hall-
Petresco formula, a discrete analogue of the Baker-Campbell-Hausdorﬀ for-
mula that expresses the polynomial sequence \ 7! }n⟨ n explicitly in the
form (1.51).

Deﬁne a nilpotent ﬁltered Lie group of degree ˇ s to be a nilpotent
ﬁltered group of degree ˇ s, in which G = G 0 and all of the G i are con-
nected, simply connected ﬁnite-dimensional Lie groups. A model example
here is the Heisenberg group, which is the degree 2 nilpotent ﬁltered Lie
group
 G = G 0 = G 1 :=
 0

@1 R R
0 1 R
0 0 1
 1

A

(i.e. the group of upper-triangular unipotent matrices with arbitrary real
entries in the upper triangular positions) with

G 2 :=
 0

@1 0 R
0 1 0
0 0 1
 1

A

and G i trivial for ⟩ > 2 (so in this case, G i is also the lower central series).

E§er⌋⟩se ∞.̸.∞3.Show that a sequence

}(\) =
 0

@1 §(\) y (\)
0 1 z (\)
0 0 1
 1

A

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.6. Inverse conjecture over the integers 99

from Z to the Heisenberg group G is a polynomial sequence if and only if
§∅ z are linear polynomials and z is a quadratic polynomial.

It is a standard fact in the theory of Lie groups that a connected, simply
connected nilpotent Lie group G is topologically equivalent to its Lie algebra
g, with the homeomorphism given by the exponential map exp : g ω G
(or its inverse, the logarithm function log : G ω g. Indeed, the Baker-
Campbell-Hausdorﬀ formula lets one use the nilpotent Lie algebra g to build
a connected, simply connected Lie group with that Lie algebra, which is
then necessarily isomorphic to G. One can thus classify ﬁltered nilpotent
Lie groups in terms of ﬁltered nilpotent Lie algebras, i.e. a nilpotent Lie
algebras g = g0 together with a nested family of sub-Lie algebras

g0  g1      gs+1 = f0g

with the inclusions [gi∅gj] ρ gi+j (in which the bracket is now the Lie bracket
rather than the commutator). One can describe such ﬁltered nilpotent Lie
algebras even more precisely using Mal'̂ev bases; see [Ma∞949], [Le∈005].
For instance, in the case of the Heisenberg group, one has

g = g0 = g1 :=
 0

@ 0 R R
0 0 R
0 0 0
 1

A

and
 g2 :=
 0

@ 0 0 R
0 0 0
0 0 0
 1

A :

From the ﬁltration property, we see that for ⟩  0, each G i+1 is a normal
closed subgroup of G i , and for ⟩  1, the quotient group G i+1 =Gi is
connected, simply connected abelian Lie group (with Lie algebra gi+1 =gi ),
and is thus isomorphic to a vector space (with the additive group law).
Related to this, one can view G = G 0 as a group extension of the quotient
group G=G s (with the degree s   1 ﬁltration (G i =Gs )) by the central
vector space G s . Thus one can view degree s ﬁltered nilpotent groups as an
s-fold iterated tower of central extensions by ﬁnite-dimensional vector spaces
starting from a point; for instance, the Heisenberg group is an extension of
R2 by R.

We thus see that nilpotent ﬁltered Lie groups are generalisations of vec-
tor spaces (which correspond to the degree 1 case). We now turn to ﬁltered
nilmanifolds, which are generalisations of tori. A degree s ﬁltered nilman-
ifold G=Γ = (G=Γ∅ G∅Γ) is a ﬁltered degree s nilpotent Lie group G ,
together with a discrete subgroup Γ of G, such that all the subgroups G i
in the ﬁltration are rationalrelative to Γ, which means that the subgroup
Γi := Γ \ G i is a cocompact subgroup of G i (i.e. the quotient space

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

100 1. Higher order Fourier analysis

G ≥i =Γ≥i is cocompact, or equivalently one can write G ≥i = Γ≥i  K ≥i for
some compact subset K ≥i of G ≥i . Note that the subgroups Γ≥i give Γ the
structure of a degree s ﬁltered nilpotent group Γ•.

Exercise 1.6.14. Let G := R 2 and Γ := Z 2, and let  2 R . Show that the
subgroup f(§∅ §) : § 2 Rg of G is rational relative to Γ if and only if  is
a rational number; this may help explain the terminology “rational”.

By hypothesis, the quotient space G=Γ = G ≥0=Γ≥0 is a smooth compact
manifold. The space G ≥s =Γ≥s is a compact connected abelian Lie group, and
is thus a torus; the degree s ﬁltered nilmanifold G=Γ can then be viewed as
a principal torus bundle over the degree s   1 ﬁltered nilmanifold G=(G ≥s Γ)
with G ≥s =Γ≥s as the structure group; thus one can view degree s ﬁltered
nilmanifolds as an s-fold iterated tower of torus extensions starting from a
point. For instance, the Heisenberg nilmanifold

G=Γ :=
 


1 R R
0 1 R
0 0 1
 

 =



1 Z Z
0 1 Z
0 0 1
 



is an extension of the two-dimensional torus R 2=Z2 by the circle R =Z.

Every torus of some dimension d can be viewed as a unit cube [0∅1]d

with opposite faces glued together; up to measure zero sets, the cube then
serves as a fundamental domain for the nilmanifold. Nilmanifolds can be
viewed the same way, but the gluing can be somewhat “twisted”:

Exercise 1.6.15. Let G=Γ be the Heisenberg nilmanifold. If we abbreviate

[§∅ y∅ z ] :=
 


1 § y
0 1 z
0 0 1


 Γ 2 G=Γ

for all §∅ y∅ z 2 R , show that for almost all §∅ y∅ z , that [§∅ y∅ z ] has exactly
one representation of the form [a∅ ⌊∅ ⌋] witha∅ ⌊∅ ⌋2 [0∅1], which is given by
the identity [§∅ y∅ z ] = [f§ g∅fy   §bz cg∅fz g]

where b§c is the greatest integer part of §, and f§g := §   b §c 2 [0∅1) is
the fractional part function. Conclude that G=Γ is topologically equivalent
to the unit cube [0∅1]3 quotiented by the identiﬁcations

(0∅ y∅ z ) ξ (1∅ y∅ z )

(§∅0∅ z ) ξ (§∅1∅ z )

(§∅ y∅ 0) ξ (§∅fy   §g∅1)

between opposite faces.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.6. Inverse conjecture over the integers 101

Note that by using the projection (§∅ y∅ z ) ↦→ (§∅ z ), we can view the
Heisenberg nilmanifold G=Γ as a twisted circle bundle over (R=Z)2, with
the ﬁbers being isomorphic to the unit circle R=Z. Show that G=Γ is not
homeomorphic to (R=Z)3. (Hint: show that there are some non-trivial
homotopies between loops that force the fundamental group of G=Γ to be
smaller than Z3.)

The logarithm log(Γ) of the discrete cocompact subgroup Γ can be shown
to be a lattice of the Lie algebra g. After a change of basis, one can thus
view the latter algebra as a standard vector space R d and the lattice as
Zd. Denoting the standard generators of the lattice (and the standard basis
of R d) as e1∅ : : : ∅ ed, we then see that the Lie bracket [ei∅ ej] of two such
generators must be an integer combination of more generators:

[ei∅ ej] =
 d∑

k/1 ⌋ijkek:

The structure constants ⌋ijk describe completely the Lie group structure of
G and Γ. The rational subgroups G l can also be described by picking some
generators for log(Γi ), which are integer combinations of the e1∅ : : : ∅ ed. We
say that the ﬁltered nilmanifold has complexity at most M if the dimension
and degree is at most M, and the structure constants and coeﬃcients of the
generators also have magnitude at most M. This is an admittedly artiﬁcial
deﬁnition, but for quantitative applications it is necessary to have some
means to quantify the complexity of a nilmanifold.

A polynomial orbit in a ﬁltered nilmanifold G=Γ is a map O : Z → G=Γ
of the form O(\) := }(\)Γ, where } : Z → G is a polynomial sequence. For
instance, any linear orbit O(\) = }n§ , where § ∈ G=Γ and } ∈ G, is a
polynomial orbit.

Exercise 1.6.16. For any ∅ ∈ R, show that the sequence

\ ↦→ [{−\}∅{\⌊\⌋}∅{\}]

(using the notation from Exercise 1.6.15) is a polynomial sequence in the
Heisenberg nilmanifold.

With the above example, we see the emergence of bracket polynomials
when representing polynomial orbits in a fundamental domain. Indeed, one
can view the entire machinery of orbits in nilmanifolds as a means of eﬃ-
ciently capturing such polynomials in an algebraically tractable framework
(namely, that of polynomial sequences in nilpotent groups). The piecewise
continuous nature of the bracket polynomials is then ultimately tied to the
twisted gluing needed to identify the fundamental domain with the nilman-
ifold.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

102 1. Higher order Fourier analysis

Finally, we can deﬁne the notion of a (basic Lipschitz) nilsequence of
degree ≤ s. This is a sequence  : Z → C of the form  (\) := F(O(\)),
where O : Z → G=Γ is a polynomial orbit in a ﬁltered nilmanifold of degree
≤ s, and F : G=Γ → C is a Lipschitz21 function. We say that the nilsequence
has complexity at most M if the ﬁltered nilmanifold has complexity at most
M, and the (inhomogeneous Lipschitz norm) of F is also at most M.

A basic example of a degree ≤ s nilsequence is a polynomial phase
\ ↦→ e(P (\)), where P : Z → R=Zis a polynomial of degree ≤ s. A bit more
generally, \ ↦→ F(P(\)) is a degree ≤ s sequence, whenever F : R=Z → C
is a Lipschitz function. In view of Exercises 1.6.15, 1.6.16, we also see that

(1.52) \ ↦→ e(\⌊\⌋) ({\}) ({\})

or more generally
 \ ↦→ F(\⌊\⌋) ({\}) ({\})

are also degree ≤ 2 nilsequences, where  : [0∅1] → C is a Lipschitz function
that vanishes near 0 and 1. The  ({\}) factor is not needed (as there is
no twisting in the § coordinate in Exercise 1.6.15), but the  ({\}) factor
is (unfortunately) necessary, as otherwise one encounters the discontinuity
inherent in the ⌊\⌋ term (and one would merely have a piecewise Lipschitz
nilsequence rather than a genuinely Lipschitz nilsequence). Because of this
discontinuity, bracket polynomial phases \ ↦→ e(\⌊\⌋) cannot quite be
viewed as Lipschitz nilsequences, but from a heuristic viewpoint it is often
helpful to pretend as if bracket polynomial phases are model instances of
nilsequences.

The only degree ≤ 0 nilsequences are the constants. The degree ≤ 1
nilsequences are essentially the quasiperiodic functions:

Exercise 1.6.17. Show that a degree ≤ 1 nilsequence of complexity M is
Fourier-measurable with growth function FM depending only on M, where
Fourier measurability was deﬁned in Section 1.2.

Exercise 1.6.18. Show that the class of nilsequences of degree ≤ s does
not change if we drop the condition G = G 0 , or if we add the additional
condition G = G 1 .

Remark 1.6.11. The space of nilsequences is also unchanged if one insists
that the polynomial orbit be linear, and that the ﬁltration be the lower cen-
tral series ﬁltration; and this is in fact the original deﬁnition of a nilsequence.
The proof of this equivalence is a little tricky, though: see [GrTaZi2010b].

21One needs a metric onG=  to deβne the Lipschitz constant, but this can be done for
instance by using a basise; : : : ; ed of   to identify G=  with a fundamental domain [0;1]d, and
using this to construct some (artiβcial) metric onG= . The details of such a construction will
not be important here.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.6. Inverse conjecture over the integers 103

∞.̸.3. Co\\e⌋t⟩o\ w⟩t⟨ t⟨e Gowers \orms.We deﬁne the Gowers
norm ∥f ∥U d [N] of a function f : [N ] → C by the formula

∥f ∥U d [N] := ∥f ∥U d (Z/N Z)=∥1[N]∥U d (Z/N Z)
where N 0is any integer greater than (d+1)N , [N ] is embedded inside Z=N0Z,
and f is extended by zero outside of [N ]. It is easy to see that this deﬁnition
is independent of the choice of N 0. Note also that the normalisation factor
∥1[N]∥U d (Z/N Z) is comparable to 1 when d is ﬁxed and N 0 is comparable to
N .
 One of the main reasons why nilsequences are relevant to the theory of
the Gowers norms is that they are an obstruction to that norm being small.
More precisely, we have

T⟨eorem ∞.̸.∞∈(Converse to the inverse conjecture for the Gowers norms).
Let f : [N ] → C be such that∥f ∥L [N] ≤ 1 and |⟨f;   ⟩L∈([N])| ≥ ﬃfor some
degree ≤ s nilsequence of complexity at mostM . Then ∥f ∥U s+∞[N] ≫s,δ,M 1.

We now prove this theorem, using an argument from [GrTaZ⟩∈009]. It
is convenient to introduce a few more notions. Deﬁne a vertical character
of a degree ≤ s ﬁltered nilmanifold G=Γ to be a continuous homomorphism
 : Gs → R=Z that annihilates Γs , or equivalently an element of the
Pontryagin dual \Gs =Γs of the torus Gs =Γs . A function F : G=Γ→ C
is said to have vertical frequency if F obeys the equation

F(gsx) = e( (gs))F(x)

for all gs ∈ Gs and x ∈ G=Γ. A degree≤ s nilsequence is said to have
a vertical frequencyif it can be represented in the form n ↦→ F(O(n)) for
some Lipschitz F with a vertical frequency.

For instance, a polynomial phase n ↦→ e(P(n)), where P : Z → R=Z
is a polynomial of degree ≤ s, is a degree ≤ s nilsequence with a vertical
frequency. Any nilsequence of degree ≤ s − 1 is trivially a nilsequence
of degree ≤ s with a vertical frequency of 0. Finally, observe that the
space of degree ≤ s nilsequences with a vertical frequency is closed under
multiplication and complex conjugation.

E§er⌋⟩se ∞.̸.∞9.Show that a degree ≤ 1 nilsequence with a vertical fre-
quency necessarily takes the form   (n) = ce(ﬀn) for some c ∈ C and ﬀ ∈ R
(and conversely, all such sequences are degree ≤ 1 nilsequences with a ver-
tical frequency). Thus, up to constants, degree ≤ 1 nilsequences with a
vertical frequency are the same as Fourier characters.

A basic fact (generalising the invertibility of the Fourier transform in the
degree ≤ 1 case) is that the nilsequences with vertical frequency generate
all the other nilsequences:

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

104 1. Higher order Fourier analysis

E§er⌋⟩se ∞.̸.∈0.Show that any degree ≤ s nilsequence can be approxi-
mated to arbitrary accuracy in the uniform norm by a linear combination
of nilsequences with a vertical frequency. (Hint. use the Stone-Weierstrass
theorem.)

More quantitatively, show that a degree ≤ s nilsequence of complex-
ity ≤ M can be approximated uniformly to error ” by a sum of OM;";s (1)
nilsequences, each with a representation with a vertical frequency that is
of complexity OM;";s (1). (Hint. this can be deduced from the qualitative
result by a compactness argument using the Arzela-Ascoli theorem.)

A derivative ∆h e(P(n)) of a polynomial phase is a polynomial phase of
one lower degree. There is an analogous fact for nilsequences with a vertical
frequency:

Lemma ∞.̸.∞3(Diﬀerentiating nilsequences with a vertical frequency).Let
s ≥ 1, and let  be a degree≤ s nilsequence with a vertical frequency. Then
for anyh ∈ Z, ∆h   is a degree≤ s − 1 nilsequence. Furthermore, if  has
complexity≤ M (with a vertical frequency representation), then∆h   has
complexityOM;s (1).

Proo{.We just prove the ﬁrst claim, as the second claim follows by reﬁning
the argument.

We write   = F(g(n)Γ) for some polynomial sequence g: Z → G=Γ and
some Lipschitz function F with a vertical frequency. We then express

∆h   (n) = ˜F(˜g(n)(Γ × Γ))

where ˜F : G × G=(Γ× Γ) → C is the function

˜F(x; y) := F(x)F(y)

and ˜g: Z → G × G is the sequence

˜g(n) := (g(n); @h g(n)g(n)):

Now we give a ﬁltration on G × G by setting

(G × G)j := Gj ×Gj +1 Gj

for j ≥ 0, where Gj ×Gj +1 Gj is the subgroup of Gj ×Gj +1 Gj gen-
erated by Gj +1 × Gj +1 and the diagonal group Gj := {(gj ; gj ) : gj ∈
Gj . One easily veriﬁes that this is a ﬁltration on G × G. The sequences
(g(n); g(n)) and (id; @h g(n)) are both polynomial with respect to this ﬁl-
tration, and hence by the Lazard-Leibman theorem (Theorem 1.6.8), ˜g is
polynomial also.

Next, we use the hypothesis that F has a vertical frequency to conclude
that F is invariant with respect to the action of the diagonal group Gs =

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.6. Inverse conjecture over the integers 105

(G × G) s . If we then deﬁne G  to be the Lie group G  := (G × G) 0 =Gs
with ﬁltration G j := (G × G) j =Gs , then G  is a degree ≤ s − 1 ﬁltered
nilpotent Lie group; setting Γ := (Γ × Γ) ∩ G  , we conclude that G  =Γ

is a degree ≤ s − 1 nilmanifold and

∆h (\) = F (} (\)Γ  )

where F ∅ } are the projections of ˜F ∅˜} from G × G to G  . The claim
follows. 

We now prove Theorem 1.6.12 by induction on s. The claim is trivial for
s = 0, so we assume that s ≥ 1 and that the claim has already been proven
for smaller values of s.

Let {∅ ◦∅  be as in Theorem 1.6.12. From Exercise 1.6.20 we see (after
modifying ◦∅ M) that we may assume that  has a vertical frequency. Next,
we use the identity

|En2∫/N ∫ 0{(\)  (\)| 2 = Eh2∫/N 0∫ En2∫/N 0∫ ∆h{(\) ∆h (\)

(extending { by zero outside of [N], and extending  arbitrarily) to conclude
that |En2[N ]∆h{(\) ∆h (\)| ≫ δ 1
for ≫ N values of ⟨ ∈ [−N∅ N]. By induction hypothesis and Lemma 1.6.13,
we conclude that ∥∆h{∥U s [N] ≫δ,M 1
for ≫ N values of ⟨ ∈ [−N∅ N]. Using the identity

∥{∥2s+∞
U s+∞(∫/N 0∫) = Eh2∫/N 0∫ ∥∆h{∥2s
U s (∫/N 0∫)
we close the induction and obtain the claim.

In the other direction, we have the following recent result:

Theorem 1.6.14 (Inverse conjecture for the Gowers norms on Z). [GrTaZi2010b]
Let{ : [N] → C be such that∥{∥L1 [N] ≤ 1 and∥{∥U s+∞[N] ≥ ◦. Then
|⟨{∅  ⟩L∈([N])| ≫s,δ 1 for some degree≤ s nilsequence of complexityOs,δ(1).

An extensive heuristic discussion of how this conjecture is proven can
be found in [GrTaZi2010]; for the purposes of this text, we shall simply
accept this theorem as a black box. For a discussion of the history of the
conjecture, including the cases s ≤ 3, see [GrTaZi2009]. An alternate proof
to Theorem 1.6.14 was recently also established in [CaSz2010], [Sz2010b].
These methods are based on the proof of an analogous ergodic-theory result
to Theorem 1.6.14, namely the description of the characteristic factors for
the Gowers-Host-Kra seminorms in [HoKr2005], which we will not discuss
here, except to say that one of the main ideas is to construct, and then study,
spaces analogous to the Host-Kra groups HK
k(G) and Host-Kra nilmanifolds

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

106 1. Higher order Fourier analysis

HK∥ (G)=HK
∥ (Γ) associated to an arbitrary function { on a (limit-ﬁnite)
interval [N] (or of a function { on an ergodic measure-preserving system).

Exercise 1.6.21 (99% inverse theorem).

(i) (Straightening an approximately linear function) Let "∅ ≤ >0. Let
∼: [ N∅ N ] ω R=Zbe a function such that j∼(a+⌊)  ∼(a)  ∼(⌊)j 
≤ for all but "N2 of all a∅ ⌊2 [ N∅ N ] with a + ⌊ 2 [ N∅ N ]. If "
is suﬃciently small, show that there exists an aﬃne linear function
\ 7ω \ +  with ∅ 2 R=Z such that j∼(\)   \   j ˝ " ≤ for
all but ◦(")N values of \ 2 [ N∅ N ], where ◦(") ω 0 as " ω 0.
(Hint: One can take ≤ to be small. First ﬁnd a way to lift ∼in a
nice manner from R=Z to R.)

(ii) Let { : [N] ω C be such that k{kL1 [N ]  1 and k{kU s+1 [N ]  1   ".
Show that there exists a polynomial P : Z ω R=Z of degree  s
such that k{   e(P )kL2([N ])  ◦, where ◦ = ◦s (") ω 0 as " ω 0
(holding s ﬁxed). Hint: Adapt the argument of the analogous
ﬁnite ﬁeld statement. One cannot exploit the discrete nature of
polynomials any more; and so one must use the preceding part of
the exercise as a substitute.

The inverse conjecture for the Gowers norms, when combined with the
equidistribution theory for nilsequences that we will turn to next, has a
number of consequences, analogous to the consequences for the ﬁnite ﬁeld
analogues of these facts; see [GrTa2010b] for further discussion.

1.6.4. Equidistribution of nilsequences. In the subject of higher order
Fourier analysis, and in particular in the proof of the inverse conjecture for
the Gowers norms, as well as in several of the applications of this conjecture,
it will be of importance to be able to compute statistics of nilsequences  ,
such as their averages E\2[N ] (\) for a large integer N; this generalises
the computation of exponential sums such as E\2[N ]e(P (\)) that occurred
in Section 1.1. This is closely related to the equidistribution of polynomial
orbits O : Z ω G=Γ in nilmanifolds. Note that as G=Γ is a compact quotient
of a locally compact group G, it comes endowed with a unique left-invariant
Haar measure G=  (which is isomorphic to the Lebesgue measure on a
fundamental domain [0∅1]d of that nilmanifold). By default, when we talk
about equidistribution in a nilmanifold, we mean with respect to the Haar
measure; thus O is asymptotically equidistributed if and only if

lim
N !1 E\2[N ]F(O(\)) = 0

for all Lipschitz F : G=Γ ω C. One can also describe single-scale equidis-
tribution (and non-standard equidistribution) in a similar fashion, but for
sake of discussion let us restrict attention to the simpler and more classical

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.6. Inverse conjecture over the integers 107

situation of asymptotic equidistribution here (although it is the single-scale
equidistribution theory which is ultimately relevant to questions relating to
the Gowers norms).

When studying equidistribution of polynomial sequences in a torus T d , a
key tool was the van der Corput lemma(Lemma 1.1.6). This lemma asserted
that if a sequence x: Z ! T d is such that all derivatives @⟨ x: Z ! T d with
h 6= 0 are asymptotically equidistributed, thenx itself is also asymptotically
equidistributed.

The notion of a derivative requires the ability to perform subtraction
on the range space T d : @⟨ x(n + h)   @⟨ x(n). When working in a higher
degree nilmanifold G/Γ, which is not a torus, we do not have a notion of
subtraction. However, such manifolds are still torus bundles with torus
T := Gs /Γs . This gives a weaker notion of subtraction, namely the
map π : G/Γ  G/Γ ! (G/Γ  G/Γ)/T  , where T  is the diagonal action
gs : (x, y) 7! (gs x, gs y) of the torus T on the product space G/Γ G/Γ. This
leads to a generalisation of the van der Corput lemma:

Lemma ∞.̸.∞5(Relative van der Corput lemma).Let x: Z ! G/Γ be a
sequence in a degreeˇ s nilmanifold for somes  1. Suppose that the
projection of x to the degreeˇ s   1 ﬁltered nilmanifoldG/Gs Γ is asymp-
totically equidistributed, and suppose also that for each non-zeroh 2 Z, the
sequence @⟨ x: n 7! π(x(n + h), x(n)) is asymptotically equidistributed with
respect to someT-invariant measure µ⟨ on (G/Γ  G/Γ)/T  . Then x is
asymptotically equidistributed inG/Γ.

Proo{.It suﬃces to show that, for each Lipschitz function F : G/Γ ! C ,
that
 lim
\!1 E \2[N ]F (x(n)) = ∫

G=  F dµG=  .

By Exercise 1.6.20, we may assume that F has a vertical frequency. If this
vertical frequency is non-zero, then F descends to a function on the degree
ˇ s   1 ﬁltered nilmanifold G/Gs Γ, and the claim then follows from the
equidistribution hypothesis on this space. So suppose instead that F has
a non-zero vertical frequency. By vertically rotating F (and using the Gs -
invariance of µG=  we conclude that ∫
G=  F µG=  = 0. Applying the van der
Corput inequality (Lemma 1.1.6), we now see that it suﬃces to show that

lim
\!1 E \2[N ]F (x(n + h))F (x(n)) = 0

for each non-zero h. The function (x, y) ! F (x)F (y) on G/Γ  G/Γ is
T  -invariant (because of the vertical frequency hypothesis) and so descends

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

108 1. Higher order Fourier analysis

to a function ˜F on (G=Γ × G=Γ)=T∆. We thus have

lim
n!1 En2[N ]F(§(\ + ⟨)) F(§(\)) = Z

(G/ΓG/Γ)/T ) ˜F dh:

The function ˜F has a non-zero vertical frequency with respect to the residual
action of T (or more precisely, of (T × T)=T∆, which is isomorphic to T).
As h is invariant with respect to this action, the integral thus vanishes, as
required. 

This gives a useful criterion for equidistribution of polynomial orbits.
Deﬁne a horizontal characterto be a continuous homomorphism ≡ from G
to R=Z that annihilates Γ (or equivalently, an element of the Pontryagin
dual of the horizontal torusG=([G∅ G]Γ)). This is easily seen to be a torus.
Let ≈i : G i → Ti be the projection map.

Theorem 1.6.16 (Leibman equidistribution criterion). Let O : \ ↦→ }(\)Γ
be a polynomial orbit on a degree≤ s ltered nilmanifoldG=Γ. Suppose that
G = G 0 = G 1 . Then O is asymptotically equidistributed inG=Γ if and
only if ≡◦ } is non-constant for each non-trivial horizontal character.

This theorem was ﬁrst established by Leibman[Le2005] (by a slightly
diﬀerent method), and also follows from the above van der Corput lemma
and some tedious additional computations; see [GrTa2011] for details. For
linear orbits, this result was established in [Pa1970], [Gr1961]. Using this
criterion (together with more quantitative analogues for single-scale equidis-
tribution), one can develop equidistribution decompositions that generalise
those in Section 1.1. Again, the details are technical and we will refer to
[GrTa2011] for details. We give a special case of Theorem 1.6.16 as an
exercise:

Exercise 1.6.22. Use Lemma 1.6.15 to show that if ∅ are two real num-
bers that are linearly independent modulo 1 over the integers, then the
polynomial orbit
 \ ↦→
 0

@ 1 \ 0
0 1 \
0 0 1
 1

A Γ

is asymptotically equidistributed in the Heisenberg nilmanifold G=Γ; note
that this is a special case of Theorem 1.6.16. Conclude that the map \ ↦→
\⌊\⌋ mod 1 is asymptotically equidistributed in the unit circle.

One application of this equidistribution theory is to show that bracket
polynomial objects such as (1.52) have a negligible correlation with any gen-
uinely quadratic phase \ ↦→ e(\2 + \ + ) (or more generally, with any

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.7. Linear equations in primes 109

genuinely polynomial phase of bounded degree); this result was ﬁrst estab-
lished in [Ha∞993]. On the other hand, from Theorem 1.6.12 we know that
(1.52) has a large U 3[N] norm. This shows that even when s = 2, one cannot
invert the Gowers norm purely using polynomial phases. This observation
ﬁrst appeared in [Go∞998] (with a related observation in [ FuW⟩∞99̸]).

E§er⌋⟩se ∞.̸.∈3.Let the notation be as in Exercise 1.6.22. Show that

lim
n!1 E n2[N ]e(\b\c   \
2   ◦\) = 0

for any ∅ ◦2 R. (Hint: You can either apply Theorem 1.6.16, or go back
to Lemma 1.6.15.)

.7. Linear equations in √rimes

In this section, we discuss one of the motivating applications of the theory
developed thus far, namely to count solutions to linear equations in primes
P = f2∅3∅5∅7∅ : : :g (or in dense subsets A of primes P). Unfortunately,
the most famous linear equations in primes: the twin prime equation √2  
√1 = 2 and the even Goldbach equation √1 + √2 = N - remain out of
reach of this technology (because the relevant aﬃne linear forms involved
are commensurate, and thus have inﬁnite complexity with respect to the
Gowers norms), but most other systems of equations, in particular that of
arithmetic progressions √i = \ + ⟩rfor ⟩ = 0∅ : : : ∅ ∥  1 (or equivalently,
√i + √i+2 = 2√i+1 for ⟩ = 0∅ : : : ∅ ∥  2) , as well as the odd Goldbach equation
√1 + √2 + √3 = N, are tractable.

To illustrate the main ideas, we will focus on the following result of
Green [Gr∈005]:

T⟨eorem ∞.↦.∞(Roth’s theorem in the primes).[Gr∈005] Let A ˆ P be
a subset of primes whose upper densitylim supN !1 jA \ [N]j=jP \[N]j is
positive. ThenA contains inβnitely many arithmetic progressions of length
three.

This should be compared with Roth’s theorem in the integers (Section
1.2), which is the same statement but with the primes P replaced by the
integers Z (or natural numbers N). Indeed, Roth’s theorem for the primes is
proven by transferringRoth’s theorem for the integers to the prime setting;
the latter theorem is used as a “black box”. The key diﬃculty here in
performing this transference is that the primes have zero density inside the
integers; indeed, from the prime number theorem we have jP \ [N]j = (1 +
o(1)) N
log N = o(N ).

There are a number of generalisations of this transference technique. In
[GrTa∈008⌊], the above theorem was extended to progressions of longer
length (thus transferring Szemer´edi’s theorem to the primes). In a series

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

110 1. Higher order Fourier analysis

of papers [GrTa∈0∞0, GrTa∈0∞∞, GrTa∈008⌋, GrTaZ⟩∈0∞0⌊], related
methods are also used to obtain an asymptotic for the number of solutions
in the primes to any system of linear equations of bounded complexity. This
latter result uses the full power of higher order Fourier analysis, in particular
relying heavily on the inverse conjecture for the Gowers norms; in contrast,
Roth’s theorem and Szemer´edi’s theorem in the primes are “softer” results
that do not need this conjecture.

To transfer results from the integers to the primes, there are three basic
steps:

(i) A general transference principle, that transfers certain types of ad-
ditive combinatorial results from dense subsets of the integers to
dense subsets of a suitably “pseudorandom set” of integers (or more
precisely, to the integers weighted by a suitably “pseudorandom
measure”);

(ii) An application of sieve theory to show that the primes (or more
precisely, an aﬃne modiﬁcation of the primes) lie inside a suitably
pseudorandom set of integers (or more precisely, have signiﬁcant
mass with respect to a suitably pseudorandom measure).

(iii) If one is seeking asymptotics for patterns in the primes, and not
simply lower bounds, one also needs to control correlations between
the primes (or proxies for the primes, such as the M¨obius function)
with various objects that arise from higher order Fourier analysis,
such as nilsequences.

The former step can be accomplished∈∈ in a number of ways. For pro-
gressions of length three (and more generally, for controlling linear patterns
of complexity at most one), transference can be accomplished by Fourier-
analytic methods. For more complicated patterns, one can use techniques
inspired by ergodic theory; more recently, simpliﬁed and more eﬃcient meth-
ods based on duality (the Hahn-Banach theorem) have also been used. No
number theory is used in this step.

The second step is accomplished by fairly standard sieve theory methods
(e.g. the Selberg sieve, or the slight variants of this sieve used by Goldston-
Yıldırım-Pintz [GoY⟩P⟩∈008]). Remarkably, very little of the formidable
apparatus of modern analytic number theory is needed for this step; for
instance, the only fact about the Riemann zeta function that is truly needed
is that it has a simple pole at s = 1, and no knowledge of L-functions is
needed.

∈∈I\ t⟨e ⌋ase o{ tra\s{ere\⌋e togenuinely ra\dom sets, rat⟨er t⟨a\ √seudora\dom sets,
s⟩m⟩lar ⟩deas a√√eared earl⟩er ⟩\ t⟨e }ra√⟨ t⟨eory sett⟩\}∅ see ∪KoLuRo1996].

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.7. Linear equations in primes 111

The third step does draw more signiﬁcantly on analytic number theory
techniques and results (most notably, the method of Vinogradov to compute
oscillatory sums over the primes, and also the Siegel-Walﬁsz theorem that
gives a good error term on the prime number theorem in arithemtic pro-
gressions). As these techniques are somewhat orthogonal to the main topic
of this text, we shall only touch brieﬂy on this aspect of the transference
strategy.

∞.↦.∞. Tra\s{ere\⌋e.The transference principle is not a single theorem,
but is instead a family of related results with a common purpose, namely to
show that a suﬃciently pseudorandom set, measure, or probability distribu-
tion will be “indistinguishable” from the whole set (or the uniform measure
or probability distribution) in certain statistical senses. A key tool in this
regard is a de\se model t⟨eorem that allows one to a√√ro§⟩mateor model any
set or function that is dense with respect to a pseudorandom measure, by a
set or function which is dense with respect to the uniform measure. It turns
out that one can do this as long as the approximation is made with respect
to a suﬃciently wea∥ topology; for the applications to counting arithmetic
patterns, it turns out that the topology given by the Gowers norms is the
right one to use. The somewhat complicated nature of these norms, though,
does make the veriﬁcation of the required pseudorandomness properties to
be slightly tricky.

We illustrate these themes with Roth’s theorem, though the general
strategy applies to several other results in additive combinatorics. We begin
with Roth’s theorem in a cyclic group Z=NZ, which we phrase as follows:

T⟨eorem ∞.↦.∈(Roth’s theorem in Z=NZ).LetN ⌊e odd. I{f : Z=NZ ω
R ⟩s a {u\⌋t⟩o\ o⌊ey⟩\} t⟨e √o⟩\tw⟩se ⌊ou\d0  f  1 a\d t⟨e lower ⌊ou\d
E n2Z=N Zf (n)  ﬃ > 0, t⟨e\ o\e ⟨asΛ(f; f; f )  c(ﬃ) {or some c(ﬃ) > 0,
w⟨ereΛ(f; g; h) := E n;r 2Z=N Zf (n)g(n + r)h(n + 2r).

We assume this theorem as a “black box”, in that we will not care as
to how this theorem is proven. As noted in previous sections, this theorem
easily implies the existence of non-trivial arithmetic progressions of length
three in any subset A of [N=3] (say) with jAj  ﬃN, as long as N is suf-
ﬁciently large depending on ﬃ, as it provides a non-trivial lower bound on
Λ(1A; 1A; 1A).

Now we generalise the above theorem. We view N as an (odd) parameter
going oﬀ to inﬁnity, and use oN !1 (1) to denote any quantity that goes to
zero as N ω 1. We deﬁne a measure(or more precisely, a we⟩}⟨t {u\⌋t⟩o\)
to be a non-negative function : Z=NZ ω R〉 depending on N , such that
E n2⋃N](n) = 1 + oN !1 (1), thus  is basically the density function of a
probability distribution on Z=NZ. We say that  is Rot⟨-√seudora\domif

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

112 1. Higher order Fourier analysis

for every ◦ > 0 (independent of N) there exists ⌋(◦) > 0 such that one has
the lower bound
 Λ({∅ {∅ {)  ⌋(◦) + o N ω1;◦ (1)

whenever { : Z=NZ ! R is a function obeying the pointwise bound 0 ˇ { ˇ
and the lower bound E\2Z=N Z{  ◦, and o N ω1;◦ (1) goes to zero as N !
1 for any ﬁxed ◦. Thus, Roth’s theorem asserts that the uniform measure 1
is Roth-pseudorandom. Observe that if  is Roth-pseudorandom, then any
subset A of [N=3] whose weighted density(A) := E\2Z=N Z1A(\)(\) is at
least ◦ will contain a non-trivial arithmetic progression of length three, if
N is suﬃciently large depending on ◦, as we once again obtain a non-trivial
lower bound on Λ(1A∅1A∅1A) in this case. Thus it is of interest to establish
Roth-pseudorandomness for a wide class of measures.

Exercise 1.7.1. Show that if  is Roth-pseudorandom, and ≡ is another
measure which is “uniformly absolutely continuous” with respect to in the
sense that one has the bound ≡(A) ˇ {((A)) + o N ω1 (1) all A ˆ Z=NZ
and some function { : R+ ! R+ with {(§) ! 0 as § ! 0, then ≡ is also
Roth-pseudorandom.

In view of the above exercise, the case of measures that are absolutely
continuous with respect to the uniform distribution is uninteresting: the
important case is instead when ≡ is “singular” with respect to the uniform
measure, in the sense that it is concentrated on a set of density o N ω1 (1)
with respect to uniform measure, as this will allow us to detect progressions
of length three in sparse sets.

A model example to keep in mind of a candidate for a Roth-pseudorandom
measure is a random sparse measure of some small density 0 < √˝ 1, in
which each (\) is an independent random variable that equals 1 =√with
probability √and 0 otherwise. The case √= 1=log N can be thought of as
a crude model for the primes (cf. Cram´er’s random model for the primes).

Recall that the form Λ({∅ }∅ ⟨) is controlled by theU 2 norm in the sense
that one has the inequality

jΛ({∅ }∅ ⟨)j ˇ k{kU 2(Z=NZ)

whenever {∅ }∅ ⟨: Z=NZ ! C are bounded in magnitude by 1, and similarly
for permutations. Actually one has the slightly more precise inequality

jΛ({∅ }∅ ⟨)j ˇ k{ku2(Z=NZ)

where
 k{ku2(Z=NZ) := sup
∼2Z=N Z j ˆ{(∼)j

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.7. Linear equations in primes 113

as can easily be seen from the identity

(1.53) Λ({∅ }∅ ⟨) = X

˘2Z=N Z
 ˆ{(∼)ˆ}( 2∼ )ˆ⟨(∼)∅

H¨older’s inequality, and the Plancherel identity.

This suggests a strategy to establish the Roth-pseudorandomness of a
measure by showing that functions { dominated that measure can be approx-
imated in u2 norm by functions dominated instead by the uniform measure
1. Indeed, we have

Lemma .7.3(Criterion for Roth-pseudorandomness).Suppose we have a
measure with the following properties:

(i) (Control byu2) For any{∅ }∅ ⟨: ∫=N∫ ! ∫ with the pointwise
bound j{j∅j}j∅j⟨j  + 1, one hasjΛ({∅ }∅ ⟨)j (k{ku2 (Z=NZ)) +
o N ω1 (1), where : ∫ + ! ∫ + is a function with(§) ! 0 as
§ ! 0, and similarly for permutations.

(ii) (Approximation inu2) For any{ : ∫=N∫ ! ∫ with the pointwise
bound 0  {  , and any" > 0, there exists} : ∫=N∫ ! ∫
with the pointwise bound0  }  1 + o nω1,” (1) such thatk{  
}ku2 (Z=NZ) " + o nω1,” (1).

Then is Roth-pseudorandom.

∑roof.Let { : ∫=N∫ ! C be such that 0  {  and E n2Z=N Z {  ◦. Let
" > 0 be a small number to be chosen later. We then use the decomposition
to split { = } + ({   }) with the above stated properties. Since

jEn2Z=N Z {(\)   }(\)j  k{   }ku2 (Z=NZ) " + o nω1,” (1)

we have from the triangle inequality that

E n2Z=N Z }(\)  ◦   "   o nω1,” (1)

and in particular E n2Z=N Z }(\)  ◦=2

for N large enough. Similarly we have 0  }  2 (say) for N large enough.
From Roth’s theorem we conclude that

Λ(}∅ }∅ }) ˛ ⌋(◦=4)

for N large enough. On the other hand, by the ﬁrst hypothesis, the other
seven terms in

Λ({∅ {∅ {) = Λ(} + ({   })∅ }+ ({   })∅ }+ ({   }))

are O((O(")) for N large enough. If " is suﬃciently small depending on ◦,
we obtain the claim. ∗

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

114 1. Higher order Fourier analysis

Note that this argument in fact gives a value of ⌋(◦) that is essentially
the same as ⌋(◦). Also, we see that the u2 norm here could be replaced by
the U 2 norm, or indeed by any other quantity which is strong enough for
the control hypothesis to hold, and also weak enough for the approximation
property to hold.

So now we need to ﬁnd some conditions on that will allow us to obtain
both the control and approximation properties. We begin with the control
property. One way to accomplish this is via a restriction estimate:

Lemma 1.7.4 (Restriction estimate implies control). Let  be a measure.
Suppose there exists an exponent 2 < q <3 such that one has the restriction
estimate

(1.54) k ˆ{k`q (∫=N ∫)  C

whenever { : Z=NZ ! C obeys the pointwise bound j{j  , where C is
independent of \. Then  enjoys the control in u2 property from Lemma
1.7.3.

Proof. From Plancherel’s theorem, we see that (1.54) already holds if we
have j{j  1, so by the triangle inequality it also holds (with a slightly
diﬀerent value of C ) if j{j  + 1.

Now suppose that j{j∅j}j∅j⟨j  +1. From (1.53) and H¨older’s inequality
one has

jΛ({∅ }∅ ⟨)j  k{k
q 2
`q (∫=N ∫) k ˆ{k
3 q
`1 (∫=N ∫) k}k`q (∫=N ∫) k⟨k`q (∫=N ∫)

and thus by (1.54) jΛ({∅ }∅ ⟨)j C qk{k
3 q
u∈(∫=N ∫)
and the claim follows. 

Exercise 1.7.2.Show that the estimate (1.54) for q 2 can only hold when
 is bounded uniformly in N; this explains the presence of the hypothesis
q >2 in the above condition.

Exercise 1.7.3.Show that the estimate (1.54) is equivalent to the estimate

E\2∫=N ∫ j X

∼2∫=N ∫ }(∼)e(∼\§=N)j(\)  C k}k`q 0(∫=N ∫)

for all } : Z=NZ ! C, where q0 := q=(q  1) is the dual exponent to q.
Informally, this asserts that a Fourier series with `q0 coeﬃcients can be “re-
stricted” to the support of  in an uniformly absolutely integrable manner
(relative to ). Historically, this is the origin of the term “restriction theo-
rem” (in the context where Z=NZ is replaced with a Euclidean space such
as R\ , and  is surface measure on a manifold such as the sphere S\ 1 ).
See for instance [Ta2003].

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.7. Linear equations in primes 115

Now we turn to the approximation property. The approximation } to
{ needs to be close in u∈ norm, i.e. the Fourier coeﬃcients need to be
uniformly close. One attempt to accomplish this is hard thresholding: one
simply discards all Fourier coeﬃcients in the Fourier expansion

{(\) = X

˘2Z=N Z
 ˆ{(∼)e(§∼=N)

of { that are too small, thus setting } equal to something like

}(\) = X

˘2Z=N Z:j^f (˘)j"
ˆ{(∼)e(§∼=N):

The main problem with this choice is that there is no guarantee that the
non-negativity of { will transfer over to the non-negativity of }; also, there
is no particular reason why } would be bounded.

But a small modiﬁcation of this idea does work, as follows. Let S :=
f∼2 Z=NZ : jˆ{(∼)j  "gdenote the large Fourier coeﬃcients of {. The
function } proposed above can be viewed as a convolution {  K , where
K (\) := P ˘2S e(§∼=N) and {  K (\) := Em2Z=N Z{(m)K (\ ( m). The
inability to get good pointwise bounds on {  K can be traced back to the
oscillatory nature of the convolution kernel K (which can be viewed as a
generalised Dirichlet kernel).

But experience with Fourier analysis tells us that the behaviour of such
convolutions improves if one replaces the Dirichlet-type kernels with some-
thing more like a Fej´er type kernel instead. With that in mind, we try

}(\) := Em 1 ;m 2 2B {(\ + m ∞( m ∈)

where B is the Bohr set

B := f\2 Z=NZ : je(\∼=N) ( 1j  " for all ∼2 Sg:

Clearly, if { is non-negative, then } is also. Now we look at upper bounds
on }. Clearly }(\)  Em 1 ;m 2 2B (\ + m ∞( m ∈)

so by Fourier expansion

k}kL ∞ (Z=NZ) X

˘2Z=N Z jEm2B e(∼B)j
∈jˆ(∼)j:

Let us make the Fourier-pseudorandomness assumption

(1.55) sup
˘6=0jˆ(∼)j= o N !1 (1):

Evaluating the ∼= 0 term on the RHS separately, we conclude

k}kL ∞ (Z=NZ) 1 + o N !1 ( X

˘2Z=N Z jEm2B e(∼B)j
∈):

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

116 1. Higher order Fourier analysis

By Plancherel’s theorem we have
X

∼2Z=N Z jEm2B e(ξB)j
2 = jBj/N.

From the Kronecker approximation theorem we have

jBj/N ˛ (ε/10)
jSj

(say). Finally, if we assume (1.54) we have jSj ˝ εΓq. Putting this all
together we obtain the pointwise bound

g ˇ 1 + oN !1;q∅" (1).

Finally, we see how g approximates f. From Fourier analysis one has

ˆg(ξ) = ˆf(ξ)jEm2B e(ξB)j
2

and so kf   gku2(Z=NZ)= sup
∼2Z=N Z j ˆf(ξ)j(1   jE m2B e(ξB)j
2).

The frequencies ξ that lie outside ξ give a contribution of at most ε by the
deﬁnition of S, so we look now at the terms where ξ 2 S. From the deﬁnition
of B and the triangle inequality we have

jEm2B e(ξB)   1j ˇ ε

in such cases, while from the measure nature of ν we have

j ˆf(ξ)j ˇ E\2Z=N Zν(n) = 1 + oN !1 (1).

Putting this all together, we obtain

kf   gku2(Z=NZ)˝ ε + oN !1 (1).

To summarise, we have the following result, which essentially appears in
[GrTa2006]:

Theorem 1.7.5 (Criterion for Roth-pseudorandomness). Let ν be a mea-
sure obeying the Fourier-pseudorandomness assumption(1.55) and the re-
striction estimate(1.54) for some2 < q < 3. Thenν is Roth-pseudorandom.

This turns out to be a fairly tractable criterion for establishing the Roth-
pseudorandomness of various measures, which in turn can be used to detect
progressions of length three (and related patterns) on various sparse sets,
such as the primes; see the next section.

The above arguments to establish Roth-pseudorandomness relied heavily
on linear Fourier analysis. Now we give an alternate approach that avoids
Fourier analysis entirely; it is less eﬃcient and a bit messier, but will extend
in a fairly straightforward (but notationally intensive) manner to higher
order patterns. To do this, we replace the u2 norm in Lemma 1.7.3 with

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.7. Linear equations in primes 117

the U ∈ norm, so we now have to verify a control by U ∈ hypothesis and an
approximation by U ∈ hypothesis.

We begin with the control by U ∈ hypothesis. Instead of Fourier analysis,
we will rely solely on the Cauchy-Schwarz inequality, using a weighted ver-
sion of the arguments from Section 1.3 that ﬁrst appeared in [GrTa2008b].
We wish to control the expression

Λ({∅ }∅ ⟨) =En,r2Z/N Z{(\)} (\ + r)⟨(\ + 2r)

where {∅ }∅ ⟨are bounded in magnitude by + 1. For simplicity we will just
assume that {∅ }∅ ⟨are bounded in magnitude by ; the more general case
is similar but a little bit messier. For brevity we will also omit the domain
Z=NZ in the averages, and also abbreviate o N !1 (1) as o(1). We make the
change of variables (\∅ r) = (⌊ + 2⌋∅ a   ⌊   ⌋) to write this expression as

Ea,b,c{(⌊ + 2⌋)}(a   ⌋)⟨( 2a   ⌊)

the point being that each term involves only two of the three variables a∅ ⌊∅ ⌋.

We can pointwise bound ⟨ by  and estimate the above expression in
magnitude by Ea,bjEc{(⌊ + 2⌋)}(a   ⌋)j( 2a   ⌊):

Since E= 1 + o(1), we can use Cauchy-Schwarz and bound this by

(1 + o(1))(E a,bjEc{(⌊ + 2⌋)}(a   ⌋)j
∈( 2a   ⌊))
∞/∈

which we rewrite as

(1 + o(1)) (Ea,b,c,c0{(⌊ + 2⌋){(⌊ + 2⌋
0)}(a   ⌋)}(a   ⌋
0)( 2a   ⌊)
)∞/∈
:

We now bound } by , to obtain

(1 + o(1)) (Ea,c,c0(a   ⌋)(a   ⌋
0)jEb{(⌊ + 2⌋){(⌊ + 2⌋
0)( 2a   ⌊)j
)∞/∈
:

If we make the hypothesis

(1.56) Ea,c,c0(a   ⌋)(a   ⌋
0) = 1 + o(1)

(which is a variant of (1.55), as can be seen by expanding out using Fourier
analysis), followed by Cauchy-Schwarz, we can bound this by

(1 + o(1)) (Ea,c,c0(a   ⌋)(a   ⌋
0)jEb{(⌊ + 2⌋){(⌊ + 2⌋
0)( 2a   ⌊)j
∈)∞/4
:

We expand this out as

(1 + o(1))jE a,b,b0,c,c0{(⌊ + 2⌋){(⌊
0 + 2⌋){(⌊ + 2⌋
0){(⌊
0 + 2⌋
0)F(⌊∅ ⌊
0∅ ⌋∅ ⌋
0)j
∞/4:

where
 F(⌊∅ ⌊
0∅ ⌋∅ ⌋
0) := Ea(a   ⌋)(a   ⌋
0)( 2a   ⌊)( 2a   ⌊
0):

If the F factor could be replaced by 1, then the expression inside the absolute
values would just be k{k4
U 2 (Z/NZ), which is what we wanted. Applying the

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

118 1. Higher order Fourier analysis

triangle inequality and bounding { by , we can thus bound the previous
expression by

≪ Γ
∥{∥U 2 (Z/N Z) + E a,b,b0,c,c0(⌊ + 2⌋)(⌊
0+ 2⌋)(⌊ + 2⌋
0)(⌊
0+ 2⌋
0)|F(⌊∅ ⌊
0∅ ⌋∅ ⌋
0) − 1|
∆1/4 :

If we make the hypotheses

(1.57) E a,b,b0,c,c0(⌊+2⌋)(⌊
0+2⌋)(⌊+2⌋
0)(⌊
0+2⌋
0)F(⌊∅ ⌊
0∅ ⌋∅ ⌋
0)i = 1+o(1)

for ⟩ = 0∅1∅2, then another application of Cauchy-Schwarz gives

E a,b,b0,c,c0(⌊ + 2⌋)(⌊
0+ 2⌋)(⌊ + 2⌋
0)(⌊
0+ 2⌋
0)|F(⌊∅ ⌊
0∅ ⌋∅ ⌋
0) − 1| = o(1)

and so we have obtained the control in U 2 hypothesis (at least for {, and
assuming boundedness by and +1 assuming the conditions (1.56), (1.57)).
We refer to such conditions (involving the product of evaluated at distinct
linear forms on the left-hand side, and a 1 + o(1) on the right-hand side) as
l⟩\ear {orms co\d⟩t⟩o\s. Generalising to the case of functions bounded by
+ 1, and permuting {∅ }∅ ⟨, we can soon obtain the following result (stated
somewhat informally):

Lemma .7.6(Generalised von Neumann theorem).I{ obeys a certa⟩\
\⟩te l⟩st o{ l⟩\ear {orms co\d⟩t⟩o\s, t⟨e\ t⟨e co\trol byU 2 ⟨ypot⟨es⟩s ⟩\
Lemma ∞.↦.3 ⟨olds.

Now we turn to the approximation in U 2 property. It is possible to es-
tablish this approximation property by an energy increment method, anal-
ogous to the energy increment proof of Roth’s theorem in Section 1.2; see
[GrTa26] for details. However, this argument turns out to be rather
complicated. We give here a simpler approach based on duality (and more
precisely, the Hahn-Banach theorem) that yields the same result, due inde-
pendently to Gowers [Go2] and to Reingold-Trevisan-Tulsiani-Vadhan
[∫eTrTuVa28]. This approach also has the beneﬁt of giving somewhat
sharper quantitative reﬁnements.

The ﬁrst task is to represent the U 2 norm in a dual formulation. The
starting point is that the expression

∥{∥4
U 2 (Z/N Z) = E n,a,b{(\){ (\ + a){(\ + ⌊){(\ + a + ⌊)

whenever { : ∫=N∫ → ∫ , can be rewritten as

∥{∥4
U 2 (Z/N Z) = ⟨{∅D{⟩L2 (Z/N Z)

where the dual {u\ct⟩o\D{ = D2{ : ∫=N∫ → ∫ is deﬁned by

D{(\) := E a,b{(\ + a){(\ + ⌊){(\ + a + ⌊):

Deﬁne a bas⟩c a\t⟩-u\⟩{orm {u\ct⟩o\to be any function of the form DF,
where F : ∫=N∫ → ∫ obeys the pointwise bound |F| ≤ + 1. To obtain
the approximation property, it thus suﬃces to show that for every " > 0, for

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.7. Linear equations in primes 119

N suﬃciently large depending on ", and any { : Z=NZ ! R with 0 ˇ { ˇ ,
one can decompose { = {1 + {2 where 0 ˇ {1 ˇ 1 and jh{2∅DFij ˇ "4 for
all basic anti-uniform functions DF. Indeed, if one sets F := {2, the latter
bound gives k{2k4
U 2(Z=NZ)ˇ "4, and the desired decomposition follows.

In order to apply the Hahn-Banach theorem properly, it is convenient
to symmetrise and convexify the space of basic anti-uniform functions. De-
ﬁne an averaged anti-uniform fun̂tionto be any convex combination of
basic anti-uniform functions and their negations, and denote the space of
all such averaged anti-uniform functions as B . Thus B is a compact convex
symmetric subset of the ﬁnite-dimensional real vector space L2(Z=NZ) that
contains a neighbourhood of the origin; equivalently, it deﬁnes a norm on
L2(Z=NZ). Our task is then to show (for ﬁxed " and large N) that for any
{ 2 Z=NZ ! R with 0 ˇ { ˇ + 1, the sets

U := f({ 1∅ {2) 2 L
2(Z=NZ) “ L
2(Z=NZ) : {1 + {2 = {g

and

V := f({ 1∅ {2) 2 L
2(Z=NZ)“L 2(Z=NZ) : 0 ˇ {1 ˇ 1; h{2∅ ˚i ˇ "
4 for all ˚2 B g

have non-empty intersection.

The point of phrasing things this way is that U and V are both closed
convex subsets of the ﬁnite-dimensional vector space L2(Z=NZ)“ L2(Z=NZ),
and so the Hahn-Banâh theoremis applicable23. Indeed, suppose that there
was some { for which U and V were disjoint. Then, by the Hahn-Banach
theorem, there must exist some linear functional

({1∅ {2) 7! h{1∅ ˚1i L 2(Z=NZ)+ h{2∅ ˚2i L 2(Z=NZ)

which separates the two sets, in the sense that

h{1∅ ˚1i L 2(Z=NZ)+ h{2∅ ˚2i L 2(Z=NZ)> ⌋

for all ({1∅ {2) 2 U , and

h{1∅ ˚1i L 2(Z=NZ)+ h{2∅ ˚2i L 2(Z=NZ)ˇ ⌋

for all ({1∅ {2) 2 V , where ⌋ is a real number.

From the form of U , we see that we must have ˚1 = ˚2. In partic-
ular, we may normalise ˚ = ˚1 = ˚2 to be on the boundary of B . As
all ﬁnite-dimensional spaces are reﬂexive, we see in that case that h{2∅ ˚i
can be as large as "4 on V , and independently h{1∅ ˚i can be as large as
E n2Z=N Z max(˚∅0). We conclude that

E n2Z=N Z max(˚∅0) + "
4 ˇ E n2Z=N Z{ ˚:

23One could also use closely related results, such as theFarkas lemma. see [Ta2008 , x1.16]
for more discussion.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

120 1. Higher order Fourier analysis

As 0 ≤ { ≤ , we see that { ˚≤ max(˚∅0), and thus

En2Z/N Z(− 1) max(˚∅0) ≥ "
4:

We now make the hypothesis that the dual function D(+ 1) of + 1 is
uniformly bounded:

(1.58) D(+ 1) ≤ C:

We remark that the linear forms condition (which we have not speciﬁed
explicitly) will give this bound with C = D(1 + 1) + o(1) = 2 22 1 + o(1).

Since ˚ is a convex combination of functions of the form ±DF and
|F| ≤ + 1, this implies that ˚ is bounded uniformly as well: |˚| ≤ C .
Applying the Weierstrass approximation theorem to the function max(§∅0)
for |§| ≤ C (and noting that the L1 norm of − 1 is O(1)) we conclude that
there exists a polynomial P : R → R (depending only on " and C ) such that

En2Z/N Z(− 1)P(˚)≥ "
4=2

(say). Breaking P into monomials, and using the pigeonhole principle, we
conclude that there exists a non-negative integer ∥ = Oε,C(1) such that

|En2Z/N Z(− 1)˚
k| ≫ε,C 1;

since ˚ was a convex combination of functions of the form ±DF, we thus
conclude that there exist F1∅ : : : ∅ Fk with |F1|∅ : : : ∅|Fk| ≤ + 1 such that

|En2Z/N Z(− 1)(DF1) : : :(DFk)| ≫ε,C 1:

We shall contradict this by at, making the hypothesis that

(1.59) En2Z/N Z(− 1)(DF1) : : :(DFk) = o N !1,k (1)

for all ∥ ≥ 1 and all F1∅ : : : ∅ Fk bounded in magnitude by + 1.

We summarise this discussion as follows:

Theorem 1.7.7 (Dense model theorem). If (1.58), (1.59) hold, then the
approximation inU 2 hypothesis in Lemma 1.7.3 holds.

There is nothing too special about the U 2 norm here; one could work
with higher Gowers norms, or indeed with any other norm for which one has
a reasonably explicit description of the dual.

The abstract version of theorem was ﬁrst (implicitly) proven in [GrTa2008b],
and made more explicit [TaZi2008]. The methods there were diﬀerent (and
somewhat more complicated). To prove approximation, the basic idea was
to write } = E({ |B) for some carefully chosen ⊃-algebra B (built out of dual
functions that correlated with things like the residual { − E({ |B)). This au-
tomatically gave the non-negativity of }; the upper bound on } came from
the bound E({ |B) ≤ E(|B), with the latter expression then being bounded
by the Weierstrass approximation theorem and (1.59).

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.7. Linear equations in primes 121

To summarise, in order to establish the Roth-pseudorandomness of a
measure , we have at least two options. The ﬁrst (which relies on Fourier
analysis, and is thus largely restricted to complexity 1 problems) is to estab-
lish the Fourier pseudorandomness bound (1.55) and the restriction estimate
(1.54). The other (which does not require Fourier analysis) is to establish a
ﬁnite number of linear forms conditions, as well as the estimate (1.59).

Next, we informally sketch how one can deduce (1.59) from a ﬁnite
number of linear forms conditions, as well as a crude estimate

(1.60) = O(N o(1) )

and a condition known as the correlation condition. At the cost of oversim-
plifying slightly, we express this condition as the assertion that

(1.61) E \2Z=N Z(\ + ⟨ 1) : : : (\ + ⟨ ∥ ) ˝ ∥ 1

whenever ⟨ 1∅ : : : ∅ ⟨∥ 2 Z=NZ are distinct, thus the ∥-point correlation func-
tion of  is bounded for each ∥. For the number-theoretic applications, one
needs to replace the 1 on the right-hand side by a more complicated expres-
sion, but we will defer this technicality to the exercises. We remark that for
each ﬁxed ∥, the correlation condition would be implied by the linear forms
condition, but it is important that we can make ∥ arbitrarily large.

For simplicity of notation we assume that the F| are bounded in mag-
nitude by  rather than by + 1. We begin by expanding out (1.59) as

jE\∅⟨ 1;1∅:::∅⟨2;k ((\) ( 1)
 ∥Y

| =1 F| (\ + ⟨ 1∅|)F| (\ + ⟨ 2∅|)F| (\ + ⟨ 1∅| + ⟨ 2∅|)j:

Shifting ⟨ ⟩∅| by ⟨ ⟩ for some ⟨ 1∅ ⟨2 and re-averaging, we can rewrite this as

jE⟨ 1;1∅:::∅⟨2;k E \∅⟨ 1∅⟨2((\) ( 1)F~⟨ 1(\ + ⟨ 1)F~⟨ 2(\ + ⟨ 2)F~⟨ 1+~⟨ 2(\ + ⟨ 1 + ⟨ 2)j

where ~⟨ ⟩ := (⟨ ⟩∅1∅ : : : ∅ ⟨⟩∅∥) for ⟩ = 1∅2 and

F(v1∅:::∅vk )(\) :=
 ∥Y

| =1 F| (\ + v| ):

The inner expectation is the Gowers inner product of ( 1, F~⟨ 1, F~⟨ 2, and
F~⟨ 1+⟨ 2. Using the linear forms condition we may assume that

k( 1kU 2(Z=NZ) = o(1)

and so it will suﬃce by the Cauchy-Schwarz-Gowers inequality, followed by
the H¨older inequality, to show that

E ⟨ 1;1∅:::∅⟨2;k F~⟨ 1k
4
U 2(Z=NZ) ˝ K 1

and similarly for ~⟨ 2 and ~⟨ 1 + ~⟨ 2.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

122 1. Higher order Fourier analysis

We just prove the claim for ~⟨ ∞, as the other two cases are similar. We
expand the left-hand side as

jEn;a;b;h 1;:::;hk
 k∏

j =∞
Fj (\ + ⟨ j )Fj (\ + ⟨ j + a)Fj (\ + ⟨ j + ⌊)Fj (\ + ⟨ j + a + ⌊)j

which we can upper bound by

jEn;a;b;h 1;:::;hk
 k∏

j =∞
(\ + ⟨ j )(\ + ⟨ j + a)(\ + ⟨ j + ⌊)(\ + ⟨ j + a + ⌊)j

We can factorise this as

Ea;bjEn (\)(\ + a)(\ + ⌊)(\ + a + ⌊)j
k :

Using (1.61), we see that the inner expectation is Ok (1) as long as 0∅ a∅ ⌊∅ a+⌊
are distinct; in all other cases they are O(N o(∞)), by (1.60). Combining these
two cases we obtain the claim.

Exercise 1.7.4.Show that (1.59) also follows from a ﬁnite number of linear
forms conditions and (1.61), if the Fj are only assumed to be bounded in
magnitude by  + 1 rather than , and the right-hand side of (1.61) is
weakened to ∑
∞i<j m ≪(⟨ i Γ ⟨ j ), where ≪: Z=NZ ! R+ is a function
obeying the moment bounds En2Z=N Z ≪(\) q ˝ q 1 for each q 1.

The above machinery was geared to getting Roth-type lower bounds on
Λ({∅ {∅ {); but it also can be used to give more precise asymptotics:

Exercise 1.7.5.Suppose that obeys the hypotheses of Lemma 1.7.3 (with
the u∈ norm). Let { : Z=NZ ! R obey the pointwise bound 0 ˇ { ˇ 1
and has mean En2Z=N Z {(\) = ◦; suppose also that one has the pseudo-
randomness bound sup˘2Z=N Zn0 j ˆ{(∼)j = o N ω1 (1). Show that Λ({∅ {∅ {) =
◦3 + o N ω1 (1).

Exercise 1.7.6.Repeat the previous exercise, but with the u∈ norm re-
placed by the U ∈ norm.

Informally, the above exercises show that if one wants to obtain asymp-
totics for three-term progressions in a set A which has positive relative
density with respect to a Roth-pseudorandom measure, then it suﬃces to
obtain a non-trivial bound on the exponential sums ∑
n2A e(∼\) for non-zero
frequencies ∼.

For longer progressions, one uses higher-order Gowers norms, and a sim-
ilar argument (using the inverse conjecture for the Gowers norms) shows
(roughly speaking) that to obtain asymptotics for ∥-term progressions (or
more generally, linear patterns of complexity ∥ Γ 1) in a U k  ∞ -pseudorandom
measure (by which we mean that the analogue of Lemma 1.7.3 for the U k  ∞

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.7. Linear equations in primes 123

norm holds) then it suﬃces to obtain a non-trivial bound on sums of the
form P \2A F (g(n)Γ) for k  2-step nilsequences F (g(n)Γ). See [GrTa2010]
for further discussion.

1.7.2. A brief discussion of sieve theory. In order to apply the above
theory to ﬁnd patterns in the primes, we need to build a measure ν with
respect to which the primes have a positive density, and for which one can
verify conditions such as the Fourier pseudorandomness condition (1.55),
the restriction estimate (1.54), linear forms conditions, and the correlation
condition (1.61).

There is an initial problem with this, namely that the primes themselves
are not uniformly distributed with respect to small moduli. For instance, all
primes are coprime to two (with one exception). In contrast, any measure ν
obeying the Fourier pseudorandomness condition (1.55) (which is implied by
the condition kν   1kU 2 = o(1), which would follow in turn from the linear
forms condition), must be evenly distributed in both odd and even residue
classes up to o(1) errors; this forces the density of the primes in ν to be at
most 1/2 + o(1). A similar argument using all the prime moduli less than
some parameter w shows in fact that the density of primes in ν is at mostQ √<w(1   
√) + oN !1;w (1). Since P √ 
√ diverges to +1, Q √(1   
√) diverges
to zero, and so we see that the primes cannot in fact have a positive density
with respect to any pseudorandom measure.

This diﬃculty can be overcome by a simple aﬃne change of variables
known as the W-trick, where we replace the primesP = f2, 3, 5, . . .g by the
modiﬁed set PW∅⌊ := fn 2 N : W n + b 2 Pg , where W := Q √<wp is the
product of all the primes less than w, and 1 ˇ b < W is a residue class
coprime to W. In practice, w (and W) are slowly growing functions of N,
e.g. one could take w = log log log N. By the pigeonhole principle, for any
given N and W there will exist a b for which PW∅⌊ is large (of cardinality
˛ N
˚(W) logN , where φ(W) is the number of residue classes coprime to W);
indeed, thanks to the prime number theorem in arithmetic progressions, any
such b would work (e.g. one can take b = 1). Note that every arithmetic
progression in PW∅⌊ is associated to a corresponding arithmetic progression
in P. Thus, for the task of locating arithmetic progressions at least, we
may as well work with PW∅⌊; a similar claim also holds for more complicated
tasks, such as counting the number of linear patterns in P, though one now
has to work with several residue classes at once. The point of passing from
P to PW∅⌊ is that the latter set no longer has any particular bias to favour or
disfavour any residue class with modulus less than w; there are still biases
at higher moduli, but as long as w goes to inﬁnity with N, the eﬀect of such
biases will end up being negligible (ultimately contributing o(1) terms to
things like the linear forms condition).

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

124 1. Higher order Fourier analysis

To simplify the exposition a bit, though, let us ignore the W-trick and
pretend that we are working with the primes themselves rather than the
aﬃne-shifted primes. We will also ignore the technical distinctions between
the interval [N] and the cyclic group Z=NZ.

The most natural candidate for the measure is the von Mangoldt func-
tion Λ : N ω R+, deﬁned by setting Λ(\) := log √when \ = √j is a prime
√ or a power of a prime, and Λ(\) = 0 otherwise. One hint as to the
signiﬁcance of this function is provided by the identity

log \ = X

djn Λ(d)

for all natural numbers \, which can be viewed as a generating function of
the fundamental theorem of arithmetic.

The prime number theorem tells us that Λ is indeed a measure: E n2[N]Λ(\) =
1 + o(1). And the primes have full density with respect to this function:
E n2[N]1∑(\)Λ(\) = 1 + o(1). Furthermore, the von Mangoldt function has
good Fourier pseudorandomness properties (after applying the W-trick),
thanks to the classical techniques of Hardy-Littlewood and Vinogradov. In-
deed, to control exponential sums such as E n2[N]Λ(\)e(∼\) for some ∼2 R,
one can use tools such as the Siegel-Walﬁsz theorem (a quantitative version
of the prime number theorem in arithmetic progressions) to control such
sums in the “major arc” case when ∼is close to a rational of small height,
while in the “minor arc” case when ∼behaves irrationally, one can use the
standard identity

(1.62) Λ(\) = X

djn (d) log \
d ∅

where  is the M obius function 24, to re-express such a sum in terms of
expressions roughly of the form
X

d;m (d) log me(∼dm )

where we are intentionally vague as to what range the d∅ m parameters are
being summed over. The idea is then to eliminate the  factor by tools
such as the triangle inequality or the Cauchy-Schwarz inequality, leading to
expressions such as X

d jX

m log me(∼dm )j;

the point is that the inner sum does not contain any number-theoretic factors
such as Λ or , but is still oscillatory (at least if ∼is suﬃciently irrational),

24The M obius function  is deﬁned by setting (n) := ( (1) k when n is the product of k
distinct primes for some k  0, and (n) = 0 otherwise.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.7. Linear equations in primes 125

and so one can extract useful cancellation from here. Actually, the situation
is more complicated than this, because there are regions of the range of (d∅ m)
for which this method provides insuﬃcient cancellation, in which case one
has to rearrange the sum further using more arithmetic identities such as
(1.62) (for instance, using a truncated version of (1.62) known as Vau}⟨a\'s
⟩de\t⟩ty). We will not discuss this further here, but any advanced analytic
number theory text (e.g. [IwKo2004]) will cover this material.

Unfortunately, while the Fourier-pseudorandomness of Λ is well-understood,
the linear forms and correlation conditions are essentially equivalent to (and
in fact slightly harder than) the original problem of obtaining asymptotics
for linear patterns in primes, and so using Λ for the pseudorandom measure
would result in a circular argument. Furthermore, correlations such as

En2[N ]Λ(\)Λ(\ + 2)

(which essentially counts the number of twin primes up to N) are notoriously
diﬃcult to compute. For instance, if one tries to expand the above sum using
(1.62), one ends up with expressions such as

X

d,dˇN (d)(d
0) X

nˇN :djn,djn+2log \
d log \ + 2
d 0 :

By the Chinese remainder theorem, the two residue conditions dj\ and
d 0j\ + 2 can be combined to a single residue condition for \ modulo the
least common multiple l⌋m(d∅ d0) of d and d 0. If d and d 0 are both small,
e.g. d∅ d0  N 1/10, then this least common multiple is much less than N,
and in such a case one can compute the inner sum very precisely; as it turns
out, the main term in this estimate is multiplicative in d∅ d0, which allows
the outer sum to be estimated using the techniques of multiplicative number
theory (and in particular, using the theory of the Riemann zeta function).
Unfortunately, for the bulk of the above sum, d and d 0 are instead compara-
ble to N, and the least common multiple is typically of size N 2, and then it
becomes extraordinarily diﬃcult to estimate the inner sum (and hence the
entire sum).

However, if we tru\⌋atethe divisor sum (1.62) to restrict d to a range
such as d  N 1/10, then the situation improves substantially. This leads to
expressions such as

(1.63) (\) := 1
log R
 0

@ X

djn;d<R (d) log R
d
 1

A
 2

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

126 1. Higher order Fourier analysis

or more generally

(1.64) (\) := log R
0

@ X

djn (d)
⊆ log d
log R

∞

A
 2

for some cutoﬀ function  , where R is a small power25 of N; the expression
(1.63) corresponds to the case  (§ ) := max(1   §∅0). The presence of the
square is to ensure that  is non-negative, and the presence of the 1
log R is a
normalisation factor to ensure that has mean close to 1. Such expressions
were essentially introduced to Selberg (as part of what is now known as the
Selberg sieve), although the sieve weight factors  ( log d
log R ) are usually mod-
iﬁed slightly for the Selberg sieve (see [GrTa26] for further discussion).
The correlation properties of the particular expression (1.63) were studied
intensively by Goldston and Yıldırım (see e.g. [Go∏i∑i28]), and have
particularly sharp estimates, although for applications discussed here, one
can work instead with a smoother choice of cutoﬀ  , which makes the re-
quired correlation estimates on  easier to prove (but with slightly worse
bounds). Indeed, the required linear forms and correlation conditions can
be veriﬁed for (1.64) (or more precisely, a variant of in which the W-trick
is applied) by a moderately lengthy, but elementary and straightforward cal-
culation, based ultimately on the Chinese remainder theorem, an analysis
of the local problem (working mod qfor small q), and the fundamental fact
that the Riemann zeta function (s) is approximately equal to 1=(s  1) for
s close to 1. See for instance [Ta24] for more discussion.

If one uses (1.63), then we see that (\) is equal to log R when \ is
any prime larger than R; if log R is comparable to log N, we thus see (from
the prime number theorem) that the primes in [N] do indeed have positive
density relative to . This is then enough to be able to invoke the transfer-
ence principle and extend results such as Szemer´edi’s theorem to the primes,
establishing in particular that the primes contain arbitrarily long arithmetic
progressions; see [GrTa28b] for details.

To use the Fourier-analytic approach, it turns out to be convenient to
replace the above measures  by a slight variant which looks more compli-
cated in the spatial domain, but is easier to manipulate in the frequency
domain. More speciﬁcally, the expression (1.63) or (1.64) is replaced with a
variant such as

:= log R
0

@ X

djn;dR (d) d
˚(d)
 X

qR=d;(q;d)=1
 1
˚(q)
 ∞

A
 2

25The exact power of N that one sets R equal to will depend on the complexity of the linear
forms and correlation conditions one needs. For counting progressions of length three, for instance,
one can take R = N 1=10.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

1.7. Linear equations in primes 127

where ˚(d) is the Euler totient function (the number of integers from 1 to d
that are coprime to d). Some standard multiplicative number theory shows
that the weights d
˚(d) P qˇR=d;(q∅d)=1 1
˚(q) are approximately equal to log R
d
in some sense. With such a representation, it turns out that the Fourier
coeﬃcients of  can be computed more or less explicitly, and is essentially
supported on those frequencies of the form a=qwith q  R2. This makes
it easy to verify the required Fourier-pseudorandomness hypothesis (1.55)
(once one applies the W-trick). As for the restriction estimate (1.54), the
ﬁrst step is to use Exercise (1.7.3) and the Cauchy-Schwarz inequality to
reduce matters to showing an estimate of the shape

E\ jX

∼ }(∼)e(∼\§=N)j
2(\) ˝ k} k`q 0:

The right-hand side can be rearranged to be of the shape
X

∼∅∼0 }(∼)}(∼0)ˆ(∼  ∼
0):

It is then possible to use the good pointwise control on the Fourier transform
ˆ of  (in particular, the fact that it “decays” quite rapidly away from the
major arcs) to get a good restriction estimate. See [GrTa2006] for further
discussion.

As discussed in the previous section, to get asymptotics for patterns in
the primes we also need to control exponential sums such as
X

√ˇN e(∼√)

and more generally (for higher complexity patterns)
X

√ˇN F(}(√)Γ)

for various nilsequences \ 7! F(}(\)Γ). Again, it is convenient to use the von
Mangoldt function Λ as a proxy for the primes, thus leading to expressions
such as X

\ˇN Λ(\)F (}(\)Γ):

Actually, for technical reasons it is convenient to use identities such as (1.62)
to replace this type of expression with expressions such as
X

\ˇN (\)F(}(\)Γ)∅

because the M¨obius function  enjoys better boundedness and equidistri-
bution properties than Λ. (For instance, Λ strongly favours odd numbers
over even numbers, whereas the M¨obius function has no preference.) It

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

128 1. Higher order Fourier analysis

turns out that these expressions can be controlled by a generalisation of the
method of Vinogradov used to compute exponential sums over primes, using
the equidistribution theory of nilsequences as a substitute for the classical
theory of exponential sums over integers. See [GrTa∈008⌋] for details.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

Chapter 2

Related articles
 ∞∈9

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

130 2. Related articles

∈.∞. Ultral⟩m⟩t a\alys⟩s a\d qua\t⟩tat⟩ve al}e⌊ra⟩⌋ }eometry

There is a close relationship between ﬁnitary (or “hard”, or “quantita-
tive”) analysis, and inﬁnitary (or “soft”, or “qualitative”) analysis; see e.g.
[Ta∈008, x1.3, 1.5] or [Ta∈0∞0⌊, x2.11]. One way to connect the two types
of analysis is via compactness arguments(and more speciﬁcally, contradic-
tion and compactnessarguments); such arguments can convert qualitative
properties (such as continuity) to quantitative properties (such as bounded),
basically because of the fundamental fact that continuous functions on a
compact space are bounded (or the closely related fact that sequentially
continuous functions on a sequentially compact space are bounded).

A key stage in any such compactness argument is the following: one has
a sequence X n of “quantitative” or “ﬁnitary” objects or spaces, and one has
to somehow end up with a “qualitative” or “inﬁnitary” limit object X or
limit space. One common way to achieve this is to embed everything inside
some universal space and then use some weak compactness property of that
space, such as the Banach-Alaoglu theorem(or its sequential counterpart;
see [Ta∈0∞0, x1.8]). This is for instance the idea behind the Furstenberg
correspondence principlerelating ergodic theory to combinatorics; see for
instance [Ta∈009, x2.10] for further discussion.

However, there is a slightly diﬀerent approach, which I will call ultralimit
analysis, which proceeds via the machinery ofultraβltersand ultraproducts;
typically, the limit objects X one constructs are now the ultraproducts (or
ultralimits) of the original objects X  . There are two main facts that make
ultralimit analysis powerful. The ﬁrst is that one can take ultralimits of
arbitrarysequences of objects, as opposed to more traditional tools such as
metric completions, which only allow one to take limits of Cauchy sequences
of objects. The second fact is  Los's theorem, which tells us thatX is an
elementary limitof the X  (i.e. every sentence in ﬁrst-order logic which
is true for the X  for ﬀ large enough, is true for X ). This existence of
elementary limits is a manifestation of the compactness theoremin logic; see
[Ta∈0∞0⌊, x1.4] for more discussion. So we see that compactness methods
and ultraﬁlter methods are closely intertwined
1.

Ultralimit analysis is very closely related to nonstandard analysis; see
[Ta∈008, x1.5] for further discussion. We will expand upon this connection
later in this section. Roughly speaking, the relationship between ultralimit
analysis and nonstandard analysis is analogous to the relationship between
measure theory and probability theory.

1See also [Ta2,x1.8] for a related connection between ultraβlters and compactness.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

2.1. Ultralimit analysis 131

To illustrate how ultralimit analysis is actually used in practice, we will
take here a qualitative inﬁnitary theory - in this case, basic algebraic geom-
etry - and apply ultralimit analysis to then deduce a quantitative version
of this theory, in which the complexity of the various algebraic sets and
varieties that appear as outputs are controlled uniformly by the complexity
of the inputs. The point of this exercise is to show how ultralimit analy-
sis allows for a relatively painless conversion back and forth between the
quantitative and qualitative worlds, though in some cases the quantitative
translation of a qualitative result (or vice versa) may be somewhat unex-
pected. In a recent paper [BrGrTa∈0∞0], ultralimit analysis was used to
reduce the messiness of various quantitative arguments by replacing them
with a qualitative setting in which the theory becomes signiﬁcantly cleaner.

For sake of completeness, we will also reprove some earlier instances of
the correspondence principle via ultralimit analysis, namely the deduction
of the quantitative Gromov theorem from the qualitative one, and of Sze-
mer´edi’s theorem from the Furstenberg recurrence theorem, to illustrate how
close the two techniques are to each other.

∈.∞.∞. Ultral⟩m⟩t a\alys⟩s.In order to perform ultralimit analysis, we
need to prepare the scene by deciding on three things in advance:

(i) The sta\dard u\⟩verseU of standard objects and spaces.

(ii) A distinction between ord⟩\ary o⌊|e⌋ts, and s√a⌋es.

(iii) A choice of \o\-√r⟩\⌋⟩√al ultralterα1 2 βNnN.

We now discuss each of these three preparatory ingredients in turn.

We assume that we have a sta\dard u\⟩verseor su√erstru⌋tureU which
contains all the “standard” sets, objects, and structures that we ordinarily
care about, such as the natural numbers, the real numbers, the power set of
real numbers, the power set of the power set of real numbers, and so forth.
For technical reasons, we have to limit the size of this universe by requiring
that it be a set, rather than a class; thus (by Russell's √arado§), not all
sets will be standard (e.g. U itself will not be a standard set). However,
in many areas of mathematics (particularly those of a “ﬁnitary” or at most
“countable” ﬂavour, or those based on ﬁnite-dimensional spaces such as
Rd), the type of objects considered in a ﬁeld of mathematics can often be
contained inside a single set U. For instance, the class of all groups is too
large to be a set. But in practice, one is only interested in, say, groups with
an at most countable number of generators, and if one then enumerates
these generators and considers their relations, one can identify each such
group (up to isomorphism) to one in some ﬁxed set of model groups. One
can then take U to be the collection of these groups, and the various objects
one can form from these groups (e.g. power sets, maps from one group to

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

132 2. Related articles

another, etc.). Thus, in practice, the requirement that we limit the scope of
objects to care about is not a signiﬁcant limitation∈.

It is important to note that while we primarily ⌋areabout objects in-
side the standard universe U, we allow ourselves to use objects outside the
standard universe (but still inside the ambient set theory) whenever it is
convenient to do so. The situation is analogous to that of using complex
analysis to solve real analysis problems; one may only care about state-
ments that have to do with real numbers, but sometimes it is convenient to
introduce complex numbers within the √roo{sof such statements3.

We will also assume that there is a distinction between two types of
objects in this universe: s√a⌋es, which are sets that can contain other objects,
and ord⟩\ary o⌊|e⌋ts, which are all the objects that are not spaces. Thus, for
instance, a group element would typically be considered an ordinary object,
whereas a group itself would be a space that group elements can live in. It is
also convenient to view functions f : X ! Y between two spaces as itself a
type of ordinary object (namely, an element of a space Hom(X, Y ) of maps
from X to Y ). The precise concept of what constitutes a space, and what
constitutes an ordinary object, is somewhat hard to formalise, but the basic
rule of thumb to decide whether an object X should be a space or not is to
ask whether mathematical phrases such as x 2 X, f : X ! Y , or A ˆ X
are likely to make useful sense. If so, then X is a space; otherwise, X is an
ordinary object.

Examples of spaces include sets, groups, rings, ﬁelds, graphs, vector
spaces, topological spaces, metric spaces, function spaces, measure spaces,
dynamical systems, and operator algebras. Examples of ordinary objects
include points, numbers, functions, matrices, strings, and equations.

Remark 2.1.1. Note that in some cases, a single object may seem to be
both an ordinary object and a space, but one can often separate the two
roles that this object is playing by making a suﬃciently ﬁne distinction.
For instance, in Euclidean geometry, a line ℓ in is both an ordinary object
(it is one of the primitive concepts in that geometry), but it can also be
viewed as a space of points. In such cases, it becomes useful to distinguish
between the a⌊stra⌋t l⟩\eℓ, which is the primitive object, and its real⟩sat⟩o\
ℓ[R ] as a space of points in the Euclidean plane. This type of distinction
is quite common in algebraic geometry, thus, for instance, the imaginary
circle C := f(x, y ) : x∈ + y∈ = Γ1g has an empty realisation C[R ] = ; in
the real plane R ∈, but has a non-trivial realisation C[C ] in the complex

∈I{ o\e does \ot wa\t to l⟩m⟩t o\e's s⌋o√e ⟩\ t⟨⟩s {as⟨⟩o\, o\e ⌋a\ √ro⌋eed ⟩\stead us⟩\} t⟨e
ma⌋⟨⟩\ery o{ Grothendieck universes.
3More }e\erally, t⟨e tr⟩⌋∥ o{ √ass⟩\} to somecompletionU o{ o\e's or⟩}⟩\al stru⌋tureU ⟩\
order to more eas⟩ly √er{orm ⌋erta⟩\ mat⟨emat⟩⌋al ar}ume\ts ⟩s a ⌋ommo\ t⟨eme t⟨rou}⟨out
moder\ mat⟨emat⟩⌋s.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

2.1. Ultralimit analysis 133

plane C ∈ (or over ﬁnite ﬁelds), and so we do not consider C (as an abstract
algebraic variety) to be empty. Similarly, given a function f , we distinguish
between the function f itself (as an abstract object) and the graph f [X ] :=
f(x; f (x)) : x 2 X g of that function over some given domain X .

We also ﬁx a nonprincipal ultraﬁlter ﬀ1 on the natural numbers. Recall
that this is a collection of subsets of N with the following properties:

(i) No ﬁnite set lies in ﬀ1 .

(ii) If A ρ N is in ﬀ1 , then any subset of N containing A is in ﬀ1 .

(iii) If A; B lie in ﬀ1 , then A \ B also lies in ﬀ1 .

(iv) If A ρ N, then exactly one of A and NnA lies in ﬀ1 .

Given a property P(ﬀ) which may be true or false for each natural
number ﬀ, we say that P is true for ﬀ suﬃciently close to ﬀ1 if the set
fﬀ 2 N : P(ﬀ) holdsg lies in ﬀ1 . The existence of a non-principal ultraﬁlter
ﬀ1 is guaranteed by the ultraﬁlter lemma, which can be proven using the
axiom of choice (or equivalently, by using Zorn’s lemma).

Remar∥ ∈.∞.∈.One can view ﬀ1 as a point in the Stone- ˇCech compacti-
ﬁcation (see [Ta∈0∞0, x1.8]), in which case “for ﬀ suﬃciently close to ﬀ1 ”
acquires the familiar topological meaning “for all ﬀ in a neighbourhood of
ﬀ1 ”.

We can use this ultraﬁlter to take limits of standard objects and spaces.
Indeed, given any two sequences (xα)α2⊗, (yα)α2⊗ of standard ordinary
objects, we say that such sequences are equivalent if we have xα = yα for all
ﬀ suﬃciently close to ﬀ1 . We then deﬁne the ultralimit limα!α 1 xα of a
sequence (xα)α2⊗ to be the equivalence class of (xα)α2⊗ (in the space U⊗

of all sequences in the universe). In other words, we have

lim
α! α1 xα = lim
α!α 1 yα

if and only if xα = yα for all ﬀ suﬃciently close to ﬀ1 .

The ultralimit limα!α 1 xα lies outside the standard universe U, but is
still constructible as an object in the ambient set theory (because U was
assumed to be a set). Note that we do not need xα to be well-deﬁned for all
ﬀ for the limit (xα)α2⊗ to make sense; it is enough that xα is well-deﬁned
for all ﬀ suﬃciently close to ﬀ1 .

If x = limα! α1 xα, we refer to the sequence xα of ordinary objects as
a model for the limit x. Thus, any two models for the same limit object x
will agree in a suﬃciently small neighbourhood of ﬀ1 .

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

134 2. Related articles

Similarly, given a sequence of standard spaces (X )2N , one can form
4

the ultralimit(or ultraproduct) lim! 1 X , deﬁned as the collection of all
ultralimits lim! 1 §  of sequences § , where §  2 X  for all  2 N (or for
all  suﬃciently close to 1 ). Again, this space will lie outside the standard
universe, but is still a set. If X = lim! 1 X , we refer to the sequence X
of spaces as a modelfor X .

As a special case of an ultralimit, given a single space X , its ultralimit
lim! 1 X is known as the ultrapowerof X and will be denoted X .

Remark 2.1.3.One can view X as a type of completionof X , much as
the reals are the metric completionof the rationals. Indeed, just as the reals
encompass all limits lim\!1 § \ of Cauchy sequences § 1∅ §2∅ : : :in the ratio-
nals, up to equivalence, the ultrapower X encompass all limits of arbitrary
sequences in X , up to agreement suﬃciently close to 1 . The ability
5 to
take limits of arbitrary sequences, and not merely Cauchy sequences or con-
vergent sequences, is the underlying source of power of ultralimit analysis.

Of course, we embed the rationals into the reals by identifying each
rational § with its limit lim\!1 §. In a similar spirit, we identify every
standard ordinary object § with its ultralimit lim! 1 §. In particular, a
standard space X is now identiﬁed with a subspace of X . When X is ﬁnite,
it is easy to see that this embedding of X to X is surjective; but for inﬁnite
X , the ultrapower is signiﬁcantly larger than X itself.

Remark 2.1.4.One could collect the ultralimits of all the ordinary objects
and spaces in the standard universe U and form a new structure, the non-
standard universeU1 , which one can view as a completionof the standard
universe, in much the same way that the reals are a completion of the ra-
tionals. However, we will not have to explicitly deal with this nonstandard
universe and will not discuss it again in this post.

In nonstandard analysis, an ultralimit of standard ordinary object in a
given class is referred to as (or more precisely, models) a nonstandardobject
in that class. To emphasise the slightly diﬀerent philosophy of ultralimit
analysis, however, I would like to call these objects limit objectsin that
class instead. Thus, for instance:

(i) An ultralimit \ = lim! 1 \  of standard natural numbers is a
limit natural number(or a nonstandard natural number, or an el-
ement of N);

4This will not conﬂict with the notion of ultralimits for ordinary objects, so long as one
always takes care to keep spaces and ordinary objects separate.
5This ability ultimately arises from the universal nature of the Stone- ˇCech compactiﬁcation
N, as well as the discrete nature of N, which makes all sequences \ 7! § n continuous.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

2.1. Ultralimit analysis 135

(ii) An ultralimit § = lim! 1 §  of standard real numbers is a limit
real number (or a nonstandard real number, or a hyperreal, or an
element of R);

(iii) An ultralimit ˚ = lim! 1 ˚ of standard functions ˚: X  ω
Y between two sets X ∅ Y is a limit function (also known as an
internal function, or a nonstandard function);

(iv) An ultralimit ˚ = lim! 1 ˚ of standard continuous functions
˚: X  ω Y between two topological spaces X ∅ Y is a limit con-
tinuous function (or internal continuous function, or nonstandard
continuous function);

(v) etc.

Clearly, all standard ordinary objects are limit objects of the same class,
but not conversely.

Similarly, ultralimits of spaces in a given class will be referred to limit
spaces in that class (in nonstandard analysis, they would be called nonstan-
dard spaces or internal spaces instead). For instance:

(i) An ultralimit X = lim! 1 X  of standard sets is a limit set (or
internal set, or nonstandard set);

(ii) An ultralimit G = lim! 1 G  of standard groups is a limit group
(or internal group, or nonstandard group);

(iii) An ultralimit (X∅B∅ ) = lim! 1 (X ∅B∅ ) of standard mea-
sure spaces is a limit measure space (or internal measure space, or
nonstandard measure space);

(iv) etc.

Note that ﬁnite standard spaces will also be limit spaces of the same class,
but inﬁnite standard spaces will not. For instance, Z is a standard group,
but is not a limit group, basically because it does not contain limit integers
such as lim! 1 . However, Z is contained in the limit group Z. The
relationship between standard spaces and limit spaces is analogous to that
between incomplete spaces and complete spaces in various ﬁelds of mathe-
matics (e.g. in metric space theory or ﬁeld theory).

Any operation or result involving ﬁnitely many standard objects, spaces,
and ﬁrst-order quantiﬁers carries over to their nonstandard or limit coun-
terparts (the formal statement of this is  Los’s theorem). For instance, the
addition operation on standard natural numbers gives an addition operation
on limit natural numbers, deﬁned by the formula

lim
! 1 \  + lim
! 1 m  := lim
! 1 (\  + m ):

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

136 2. Related articles

It is easy to see that this is a well-deﬁned operation on the limit natural
numbers ∗N, and that the usual properties of addition (e.g. the associative
and commutative laws) carry over to this limit (much as how the associa-
tivity and commutativity of addition on the rationals automatically implies
the same laws of arithmetic for the reals). Similarly, we can deﬁne the other
arithmetic and order relations on limit numbers: for instance we have

lim
ﬀ→ ﬀ1 nﬀ  lim
ﬀ→ﬀ 1 mﬀ

if and only if nﬀ  mﬀ for all ﬀ suﬃciently close to ﬀ0, and similarly deﬁne
; >; < , etc. Note from the deﬁnition of an ultraﬁlter that we still have the
usual order trichotomy: given any two limit numbers n; m, exactly one of
n < m, n = m, and n > m is true.

E§am√le ∈.∞.5.The limit natural number ! := limﬀ→ ﬀ1 ﬀ is larger than
all standard natural numbers, but ! 2 = limﬀ→ﬀ 1 ﬀ2 is even larger still.

The following two exercises should give some intuition of how  Los’s the-
orem is proved, and what it could be useful for:

E§er⌋⟩se ∈.∞.∞.Show that the following two formulations of Goldbâh's
̂onjêtureare equivalent:

(i) Every even natural number greater than two is the sum of two
primes.

(ii) Every even limit natural number greater than two is the sum of
two prime limit natural numbers.

Here, we deﬁne a limit natural number n to be even if we have n = 2m for
some limit natural number m, and a limit natural number n to be √rime if
it is greater than 1 but cannot be written as the product of two limit natural
numbers greater than 1.

E§er⌋⟩se ∈.∞.∈.Let kﬀ be a sequence of algebraically closed ﬁelds. Show
that the ultralimit k := limﬀ→ﬀ 1 kﬀ is also an algebraically closed ﬁeld. In
other words, every limit algebraically closed ﬁeld is an algebraically closed
ﬁeld.

Given an ultralimit ˚:= limﬀ→ﬀ 1 ˚ﬀ of functions ˚ﬀ : X ﬀ ! Yﬀ, we can
view ˚as a function from the limit space X := Q
ﬀ→ﬀ 1 X ﬀ to the limit
space Y := Q
ﬀ→ﬀ 1 Yﬀ by the formula

˚( lim
ﬀ→ ﬀ1 x ﬀ) := lim
ﬀ→ﬀ 1 ˚ﬀ(x ﬀ):

Again, it is easy to check that this is well-deﬁned. Thus every limit function
from a limit space X to a limit space Y is a function from X to Y, but the
converse is not true in general.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

2.1. Ultralimit analysis 137

One can easily show that limit sets behave well with respect to ﬁnitely
many boolean operations; for instance, the intersection of two limit sets
X = lim! 1 X  and Y = lim! 1 Y is another limit set, namely X \ Y =
lim! 1 X \ Y. However, we caution that the same is not necessarily true
for inﬁnite boolean operations; the countable union or intersection of limit
sets need not be a limit set. (For instance, each individual standard integer
in Z is a limit set, but their union Z is not.) Indeed, there is an analogy
between the limit subsets of a limit set, and the clopen (simultaneously
closed and open) subsets of a topological space (or the constructible setsin
an algebraic variety).

By the same type of arguments used to show Exercise 2.1.2, one can
check that every limit group is a group (albeit one that usually lies outside
the standard universe U), every limit ring is a ring, every limit ﬁeld is a
ﬁeld, etc.

The situation with vector spaces is a little more interesting. The ul-
traproduct V = lim! 1 V of a collection of standard vector spaces V
over R is a vector space over the larger ﬁeld R, because the various scalar
multiplication operations  : R  V ! V over the standard reals become
a scalar multiplication operation  : R  V ! V over the limit reals. Of
course, as the standard reals R are a subﬁeld of the limit reals R, V is also
a vector space over the standard reals R; but when viewed this way, the
properties of the V are not automatically inherited by V . For instance, if
each of the V are d-dimensional over R for some ﬁxed ﬁnite d, then V is
d-dimensional over the limit reals R, but is inﬁnite dimensional over the
reals R.

Now let A = lim! 1 A be a limit ﬁnite set, i.e. a limit of ﬁnite sets
A. Every ﬁnite set is a limit ﬁnite set, but not conversely; for instance,
lim! 1 f1∅ : : : ∅ g is a limit ﬁnite set which has inﬁnite cardinality. On
the other hand, because every ﬁnite set A has a cardinality jAj 2 N
which is a standard natural number, we can assign to every limit ﬁnite
set A = lim! 1 A a limit cardinalityjAj 2 N which is a limit natural
number, by the formula
 j lim
! 1 Aj := lim
! 1 jAj:

This limit cardinality inherits all of the ﬁrst-order properties of ordinary
cardinality. For instance, we have the inclusion-exclusion formula

jA [ B j + jA \ B j = jAj + jB j

for any two limit ﬁnite sets; this follows from the inclusion-exclusion formula
for standard ﬁnite sets by an easy limiting argument.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

138 2. Related articles

It is not hard to show that lim→1 A is ﬁnite if and only if the jAj
are bounded for α suﬃciently close to α∞. Thus, we see that one feature
of passage to ultralimits is that it converts the term “bounded” to “ﬁnite”,
while the term “ﬁnite” becomes “limit ﬁnite”. This makes ultralimit analysis
useful for deducing facts about bounded quantities from facts about ﬁnite
quantities. We give some examples of this in the next section.

In a similar vein, an ultralimit (X, d) = lim→1 (X, d) of stan-
dard metric spaces (X, d) yields a limit metric space, thus for instance
d: X  X ! ∗R is now a metric taking values in the limit reals. Now,
if the spaces (X, d) were uniformly bounded, then the limit space (X, d)
would be bounded by some (standard) real diameter. From the Bolzano-
Weierstrass theoremwe see that every bounded limit real number x has a
unique standard partst(x) which diﬀers from x by an inﬁnitesimal, i.e. a
limit real number of the form lim→1 x where x converges to zero in the
classical sense. As a consequence, the standard part st(d) of the limit metric
function d: X  X ! ∗R is a genuine metric function st(d) : X  X ! R.
The resulting metric space (X, st(d)) is often referred to as an ultralimit
of the original metric spaces (X, d), although strictly speaking this con-
ﬂicts slightly with the notation here, because we consider (X, d) to be the
ultralimit instead.

2.1.2. Application. quantitative algebraic geometry. As a sample
application of the above machinery, we shall use ultraﬁlter analysis to quickly
deduce some quantitative (but not explicitly eﬀective) algebraic geometry
results from their more well-known qualitative counterparts. Signiﬁcantly
stronger results than the ones given here can be provided by the ﬁeld of
eective algebraic geometry, but that theory is somewhat more complicated
than the classical qualitative theory, and the point to stress here is that one
can obtain a “cheap” version of this eﬀective algebraic geometry from the
qualitative theory by a straightforward ultraﬁlter argument. There does not
seem to be a comparably easy way to get such ineﬀective quantitative results
without the use of ultraﬁlters or closely related tools (e.g. nonstandard
analysis or elementary limits).

We begin by recalling a basic deﬁnition:

Deβnition 2.1.6 (Algebraic set). An (aﬃne) algebraic set over an alge-
braically closed ﬁeld k is a subset of k\ , where n is a positive integer, of the
form

(2.1) fx 2 k
\ : P(x) =    = Pm (x) = 0g

where P, . . . , Pm : k\ ! k are a ﬁnite collection of polynomials.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

2.1. Ultralimit analysis 139

Now we turn to the quantitative theory, in which we try to control the
⌋om√le§⟩ty of various objects. Let us say that an algebraic set in ∥n has
⌋om√le§⟩ty at most M if \  M, and one can express the set in the form
(2.1) where m  M, and each of the polynomials P1∅ : : : ∅ Pm has degree at
most M. We can then ask the question of to what extent one can make
the above qualitative algebraic statements quantitative. For instance, it is
known that a dimension 0 algebraic set is ﬁnite; but can we bound ⟨ow ﬁnite
it is in terms of the complexity M of that set? We are particularly interested
in obtaining bounds here which are uniform in the underlying ﬁeld ∥.

One way to do so is to open up an algebraic geometry textbook and care-
fully go through the √roo{sof all the relevant qualitative facts, and carefully
track the dependence on the complexity. For instance, one could bound the
cardinality of a dimension 0 algebraic set using Bezout's t⟨eorem. But here,
we will use ultralimit analysis to obtain such quantitative analogues “for
free” from their qualitative counterparts. The catch, though, is that the
bounds we obtain are ⟩\ee⌋t⟩ve; they use the qualitative facts as a “black
box”, and one would have to go through the proof of these facts in order to
extract anything better.

To begin the application of ultraﬁlter analysis, we use the following
simple lemma.

Lemma 2.1.7 (Ultralimits of bounded complexity algebraic sets are alge-
braic). Let\ ⌊e a d⟩me\s⟩o\. Su√√ose we ⟨ave a seque\⌋e o{ al}e⌊ra⟩⌋ sets
Aﬀ ρ ∥n
ﬀ over al}e⌊ra⟩⌋ally ⌋losed elds∥ﬀ, w⟨ose ⌋om√le§⟩ty ⟩s ⌊ou\ded ⌊y
a qua\t⟩tyM w⟨⟩⌋⟨ ⟩s u\⟩{orm ⟩\. T⟨e\ ⟩{ we set∥ := limﬀω ﬀ ∥ﬀ a\d
A := limﬀωﬀ  Aﬀ, t⟨e\∥ ⟩s a\ al}e⌊ra⟩⌋ally ⌋losed eld a\dA ρ ∥n ⟩s a\
al}e⌊ra⟩⌋ set (also o{ ⌋om√le§⟩ty at mostM).

Co\versely, every al}e⌊ra⟩⌋ set ⟩\∥n ⟩s t⟨e ultral⟩m⟩t o{ al}e⌊ra⟩⌋ sets ⟩\
∥n
ﬀ o{ ⌊ou\ded ⌋om√le§⟩ty.

Proof. The fact that ∥ is algebraically closed comes from Exercise 2.1.2.
Now we look at the algebraic sets Aﬀ. By adding dummy polynomials if
necessary, we can write

Aﬀ = f§ 2 ∥n
ﬀ : Pﬀ;1 (§) =    = Pﬀ;M (§) = 0 g

where the Pﬀ;1 ∅ : : : ∅ Pﬀ;M : ∥n
ﬀ ω ∥ﬀ of degree at most M.

We can then take ultralimits of the Pﬀ;i to create polynomials P1∅ : : : ∅ PM : ∥n ω
∥ of degree at most M. One easily veriﬁes on taking ultralimits that

A = f§ 2 ∥n : P1(§) =    = PM (§ ) = 0g

and the ﬁrst claim follows. The converse claim is proven similarly. 

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

140 2. Related articles

Ultralimits preserve a number of key algebraic concepts (basically be-
cause such concepts are deﬁnable in ﬁrst-order logic). We ﬁrst illustrate
this with the algebraic geometry concept of d⟩me\s⟩o\. It is known that
every non-empty algebraic set V in ∥n has a d⟩me\s⟩o\ dim(V ), which is an
integer between 0 and \, with the convention that the empty set has dimen-
sion  1. There are many ways to deﬁne this dimension, but one way is to
proceed by induction on the dimension \ as follows. A non-empty algebraic
subset of ∥0 has dimension 0. Now if \  1, we say that an algebraic set V
has dimension d for some 0  d  \ if the following statements hold:

(i) For all but ﬁnitely many t2 ∥, the slice Vt := f§ 2 ∥n 1 : (§∅ t)2
V g either all have dimension d   1, or are all empty.

(ii) For the remaining t2 ∥, the slice Vt has dimension at most d. If
the generic slices Vt were all empty, then one of the exceptional Vt
has to have dimension exactly d.

Informally, A has dimension d iﬀ a generic slice of A has dimension d   1.

It is a non-trivial fact to show that every algebraic set in ∥n does indeed
have a well-deﬁned dimension between  1 and \.

Now we see how dimension behaves under ultralimits.

Lemma 2.1.8 (Continuity of dimension). Su√√ose t⟨atAﬀ ρ ∥n
ﬀ are al-
}e⌊ra⟩⌋ sets over var⟩ous al}e⌊ra⟩⌋ally ⌋losed elds∥ﬀ o{ u\⟩{ormly ⌊ou\ded
⌋om√le§⟩ty, a\d letA := limﬀ! ﬀ Aﬀ ⌊e t⟨e l⟩m⟩t⟩\} al}e⌊ra⟩⌋ set }⟩ve\ ⌊y
Lemma ∈.∞.↦. T⟨e\dim(A) = limﬀ!ﬀ  dim(Aﬀ). I\ ot⟨er words, we ⟨ave
dim(A) = dim(Aﬀ) {or all su◦⌋⟩e\tly ⌋lose to 1 .

Proof. One could obtain this directly from  Los's t⟨eorem, but it is instruc-
tive to do this from ﬁrst principles.

We induct on dimension \. The case \ = 0 is trivial, so suppose that
\  1 and the claim has already been shown for \   1. Write d for the
dimension of A. If d =  1, then A is empty and so Aﬀ must be empty for
all  suﬃciently close to 1 , so suppose that d  0. By the construction
of dimension, the slice At all have dimension d   1 (or are all empty) for all
but ﬁnitely many values t1∅ : : : ∅ tr of t2 ∥. Let us assume that these generic
slices At all have dimension d   1; the other case is treated similarly and is left
to the reader. As ∥ is the ultralimit of the ∥ﬀ, we can write ti = limﬀ! ﬀ tﬀ;i
for each 1  ⟩  r. We claim that for  suﬃciently close to 1 , the slices
(Aﬀ)tα have dimension d   1 whenever tﬀ 6=tﬀ;1 ∅ : : : ∅ tﬀ;r . Indeed, suppose
that this were not the case. Carefully negating the quantiﬁers (and using
the ultraﬁlter property), we see that for  suﬃciently close to 1 , we can
ﬁnd tﬀ 6=tﬀ;1 ∅ : : : ∅ tﬀ;r such that (Aﬀ)tα has dimension diﬀerent from d   1.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

2.1. Ultralimit analysis 141

Taking ultralimits and writing t:= lim! 1 t, we see from the induction
hypothesis that At has dimension diﬀerent from d   1, contradiction.

We have shown that for  suﬃciently close to 1 , all but ﬁnitely many
slices of A have dimension d   1, and thus by the deﬁnition of dimension,
A has dimension d, and the claim follows. 

We can use this to deduce quantitative algebraic geometry results from
qualitative analogues. For instance, from the deﬁnition of dimension we
have

Lemma 2.1.9 (Qualitative Bezout-type theorem). Every dimension 0 al-
gebraî variety is ∣nite.

Using ultraﬁlter analysis, we immediately obtain the following quantita-
tive analogue:

Lemma 2.1.10 (Quantitative Bezout-type theorem). Let A ˆ ∥\ be an
algebraî set of dimension0 and ̂om√lexity at mostM over a ∣eld∥. Then
the ̂ardinalityA is bounded by a quantityC M de√ending only onM (in
√artîular, it is inde√endent of∥).

Proof. By passing to the algebraic closure, we may assume that ∥ is alge-
braically closed.

Suppose this were not the case. Carefully negating the quantiﬁers (and
using the axiom of choice), we may ﬁnd a sequence A ˆ ∥\
 of dimension 0
algebraic sets and uniformly bounded complexity over algebraically closed
ﬁelds ∥, such that jAj ! 1 as  ! 1. We pass to an ultralimit to
obtain a limit algebraic set A := lim! 1 A, which by Lemma 2.1.8 has
dimension 0, and is thus ﬁnite by Lemma 2.1.9. But then this forces A
to be bounded for  suﬃciently close to 1 (indeed we have jAj = jAj in
such a neighbourhood), contradiction. 

Remark 2.1.11. Note that this proof gives absolutely no bound on C M
in terms of M! One can get such a bound by using more eﬀective tools,
such as the actual Bezout theorem, but this requires more actual knowledge
of how the qualitative algebraic results are proved. If one only knows the
qualitative results as a black box, then the ineﬀective quantitative result is
the best one can do.

Now we give another illustration of the method. The following funda-
mental result in algebraic geometry is known:

Lemma 2.1.12(Qualitative Noetherian condition). There does not exist an
in∣nite dêreasing sequen̂e of algebraî sets in a ane s√âe∥\ , in whîh
eâh set is a √ro√er subset of the √revious one.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

142 2. Related articles

Using ultralimit analysis, one can convert this qualitative result into an
ostensibly stronger quantitative version:

Lemma ∈.∞.∞3(Quantitative Noetherian condition).LetF : N ω N ⌊e
a {u\⌋t⟩o\. LetA1 ) A2 )    ) AR ⌊e a seque\⌋e o{ √ro√erly \ested
al}e⌊ra⟩⌋ sets ⟩\kn {or some al}e⌊ra⟩⌋ally ⌋losed eldk, su⌋⟨ t⟨at ea⌋⟨
Ai ⟨as ⌋om√le§⟩ty at most F(i). T⟨e\ R ⟩s ⌊ou\ded ⌊y CF {or some CF
de√e\d⟩\} o\ly o\ F (⟩\ √art⟩⌋ular, ⟩t ⟩s ⟩\de√e\de\t o{k).

Remar∥ ∈.∞.∞4.Specialising to the case when F is a constant M , we see
that there is an upper bound on proper nested sequences of algebraic sets of
bounded complexity; but the statement is more powerful than this because
we allow F to be non-constant. Note that one can easily use this strong form
of the quantitative Noetherian condition to recover Lemma 2.1.12 (why?),
but if one only knew Lemma 2.1.13 in the constant case F = M then this
does not obviously recover Lemma 2.1.12.

Proo{.Note that n is bounded by F(1), so it will suﬃce to prove this claim
for a ﬁxed n.

Fix n. Suppose the claim failed. Carefully negating all the quantiﬁers
(and using the axiom of choice), we see that there exists an F, a sequence kα
of algebraically closed ﬁelds, a sequence Rα going to inﬁnity, and sequences

Aα,1 )    ) Aα,R

of properly nested algebraic sets in kn
α, with each Aα,i having complexity at
most F(i).

We take an ultralimit of everything that depends on ﬀ, creating an
algebraically closed ﬁeld k = limαω α1 kα, and an inﬁnite sequence6

A1 ) A2 ) : : :

of properly nested algebraic sets in kn. But this contradicts Lemma 2.1.12.
∗

Again, this argument gives absolutely no clue as to how CF is going to
depend on F.

Let us give one last illustration of the ultralimit analysis method, which
contains an additional subtlety. Deﬁne an al}e⌊ra⟩⌋ var⟩etyto be an alge-
braic set which is ⟩rredu⌋⟩⌊le, which means that it cannot be expressed as
the union of two proper subalgebraic sets. This notation is stable under
ultralimits:

6In fact, we could continue this sequence into a limit sequence up to the unbounded limit
number lim  ! 1 R , but we will not need this overspill here.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

2.1. Ultralimit analysis 143

Lemma ∈.∞.∞5(Continuity of irreducibility).Su√√ose t⟨atAα ˆ kn
α are
al}e⌊ra⟩⌋ sets over var⟩ous al}e⌊ra⟩⌋ally ⌋losed eldskα o{ u\⟩{ormly ⌊ou\ded
⌋om√le§⟩ty, a\d letA := limα!α 1 Aα ⌊e t⟨e l⟩m⟩t⟩\} al}e⌊ra⟩⌋ set }⟩ve\ ⌊y
Lemma ∈.∞.↦. T⟨e\A ⟩s a\ al}e⌊ra⟩⌋ var⟩ety ⟩{ a\d o\ly ⟩{Aα ⟩s a\ al}e⌊ra⟩⌋
var⟩ety {or allﬀ su◦⌋⟩e\tly ⌋lose to ﬀ1 .

However, this lemma is somewhat harder to prove than previous ones,
because the notion of irreducibility is not quite a ﬁrst order statement. The
following exercises show the limit of what one can do without using some
serious algebraic geometry:

E§er⌋⟩se ∈.∞.3.Let the notation and assumptions be as in Lemma 2.1.15.
Show that if A is \ot an algebraic variety, then Aα is a not algebraic variety
for all ﬀ suﬃciently close to ﬀ1 .

E§er⌋⟩se ∈.∞.4.Let the notation and assumptions be as in Lemma 2.1.15.
Call an algebraic set M -⟩rredu⌋⟩⌊leif it cannot be expressed as the union
of two proper algebraic sets of complexity at most M . Show that if A ⟩s
an algebraic variety, then for every M  1, Aα is M -irreducible for all ﬀ
suﬃciently close to ﬀ1 .

These exercises are not quite strong enough to give Lemma 2.1.15, be-
cause M -irreducibility is a weaker concept than irreducibility. However, one
can do better by applying some further facts in algebraic geometry. Given
an algebraic set A of dimension d  0 in an aﬃne space kn, one can assign
a de}reedeg(A), which is a positive integer such that jA \ Vj = deg(A) for
}e\er⟩⌋n   d-dimensional aﬃne subspaces of kn, which means that V be-
longs to the a◦\e Grassma\\⟩a\ Gr of n  d-dimensional aﬃne subspaces of
kn, after removing an algebraic subset of Gr of dimension strictly less than
that of Gr. It is a standard fact of algebraic geometry that every algebraic
set can be assigned a degree. Somewhat less trivially, the degree controls
the complexity:

T⟨eorem ∈.∞.∞̸(Degree controls complexity).LetA ⌊e a\ al}e⌊ra⟩⌋ va-
r⟩ety o{ kn o{ de}ree D. T⟨e\ A ⟨as ⌋om√le§⟩ty at most Cn,D {or some
⌋o\sta\tsn; D de√e\d⟩\} o\ly o\ n; D.

Proo{.It7 suﬃces to show that A can be cut out by polynomials of degree
D, since the space of polynomials of degree D that vanish on A is a vector
space of dimension bounded only by n and D.

Let A have dimension d. We pick a generic aﬃne subspace V of kn of
dimension n   d   2, and consider the cone C(V; A) formed by taking all

7We thank Jordan Ellenberg and nia ⊗twinowska for this argument, whîh goes bâk to
⋃Mu1970].

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

144 2. Related articles

the union of all the lines joining a point in V to a point in A. This is an
algebraic image of V × A × R and is thus generically an algebraic set of
dimension \ − 1, i.e. a hypersurface. Furthermore, as A has degree D, it is
not hard to see that C (V∅ A) has degreeD as well. Since a hypersurface is
necessarily cut out by a single polynomial, this polynomial must have degree
D.
 To ﬁnish the claim, it suﬃces to show that the intersection of the C (V∅ A)
as V varies is exactly A. Clearly, this intersection contains A. Now let √
be any point not in A. The cone of A over √can be viewed as an algebraic
subset of the projective space P n 1 of dimension d; meanwhile, the cone of
a generic subspace V of dimension \ − d − 2 is a generic subspace of P n 1 of
the same dimension. Thus, for generic V , these two cones do not intersect,
and thus √lies outside C (V∅ A), and the claim follows. 

Remark 2.1.17. There is a stronger theorem that asserts that if the degree
of a ŝheme in ∥n is bounded, then the complexity of that scheme is bounded
as well. The main diﬀerence between a variety and a scheme here is that
for a scheme, we not only specify the set of points cut out by the scheme,
but also the ideal of functions that we want to think of as vanishing on that
set. This theorem is signiﬁcantly more diﬃcult than the above result; see
[Kl1971, Corollary 6.11].

Given this theorem, we can now prove Lemma 2.1.15.

Proof. In view of Exercise 2.1.3, it suﬃces to show that if A is irreducible,
then the Aα are irreducible for  suﬃciently close to 0.

The algebraic set A has some dimension d and degree D, thus |A ∩ V | =
D for generic aﬃne \ − d-dimensional subspaces V of ∥n. Undoing the
limit using Lemma 2.1.7 and Lemma 2.1.8 (adapted to the Grassmannian
Gr rather than to aﬃne space), we see that for  suﬃciently close to 0,
|Aα ∩ Vα| = D for generic aﬃne \ − d-dimensional subspaces Vα of ∥n
α. In
other words, Aα has degree D, and thus by Theorem 2.1.16, any algebraic
variety of Aα of the same dimension d as Aα will have complexity bounded by
C n,D uniformly in . Let B α be a d-dimensional algebraic subvariety of Aα,
and let B be the ultralimit of the B α. Then by Lemma 2.1.7, Lemma 2.1.8
and the uniform complexity bound, B is a d-dimensional algebraic subset of
A, and thus must equal all of A by irreducibility of A. But this implies that
B α = Aα for all  suﬃciently close to 0, and the claim follows. 

We give a sample application of this result. From the Noetherian con-
dition we easily obtain

Lemma 2.1.18 (Qualitative decomposition into varieties). Every algebraî
set ̂an be ex√ressed as a union of ∣nitely many algebraî varieties.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

2.1. Ultralimit analysis 145

Using ultralimit analysis, we can make this quantitative:

Lemma ∈.∞.∞9(Quantitative decomposition into varieties).LetA ρ kn ⌊e
a\ al}e⌊ra⟩⌋ set o{ ⌋om√le§⟩ty at mostM over a\ al}e⌊ra⟩⌋ally ⌋losed eld
k. T⟨e\A ⌋a\ ⌊e e§√ressed as t⟨e u\⟩o\ o{ at mostCM al}e⌊ra⟩⌋ var⟩et⟩es
o{ ⌋om√le§⟩ty at mostCM , w⟨ereCM de√e\ds o\ly o\ M .

Proo{.As n is bounded by M , it suﬃces to prove the claim for a ﬁxed n.

Fix n and M . Suppose the claim failed. Carefully negating all the quan-
tiﬁers (and using the axiom of choice), we see that there exists a sequence
Aﬀ ρ kn
ﬀ of uniformly bounded complexity, such that Aﬀ cannot be ex-
pressed as the union of at most ﬀ algebraic varieties of complexity at most
ﬀ. Now we pass to an ultralimit, obtaining a limit algebraic set A ρ kn .
As discussed earlier, A is an algebraic set over an algebraically closed ﬁeld
and is thus expressible as the union of a ﬁnite number of algebraic varieties
A1; : : : ; Am . By Lemma 2.1.7 and Lemma 2.1.15, each Ai is an ultralimit of
algebraic varieties Aﬀ;i of bounded complexity. The claim follows. 

∈.∞.3. A√√l⟩⌋at⟩o\: Qua\t⟩tat⟩ve Gromov t⟨eorem.As a further il-
lustration of ultralimit analysis, we now establish the correspondence prin-
ciple between ﬁnitary and inﬁntary forms of the following famous theorem
of Gromov [Gr∞98∞]:

T⟨eorem ∈.∞.∈0(Qualitative Gromov theorem).Every \⟩tely }e\erated
}rou√ o{ √oly\om⟩al }rowt⟨ ⟩s v⟩rtually \⟩l√ote\t.

Let us now make the observation (already observed in [Gr∞98∞]) that
this theorem implies (and is in fact equivalent to) a quantitative version:

T⟨eorem ∈.∞.∈∞(Quantitative Gromov theorem).For everyC; d t⟨ere e§-
⟩stsR su⌋⟨ t⟨at ⟩{G ⟩s }e\erated ⌊y a \⟩te setS w⟩t⟨ t⟨e }rowt⟨ ⌋o\d⟩t⟩o\
jBS (r)j  Crd {or all1  r  R, t⟨e\G ⟩s v⟩rtually \⟩l√ote\t, a\d {urt⟨er-
more ⟩t ⟨as a \⟩l√ote\t su⌊}rou√ o{ ste√ a\d ⟩\de§ at mostMC;d {or some
MC;d de√e\d⟩\} o\ly o\ C; d. HereBS (r) ⟩s t⟨e ⌊all o{ rad⟩usr }e\erated
⌊y t⟨e set S.

Proo{.We use ultralimit analysis. Suppose this theorem failed. Carefully
negating the quantiﬁers, we ﬁnd that there exists C; d, as well as a sequence
Gﬀ of groups generated by a ﬁnite set Sﬀ such that jBS  (r)j  Crd for all
1  r  ﬀ, and such that Gﬀ does not contain any nilpotent subgroup of
step and index at most ﬀ.

Now we take ultralimits, setting G := limﬀω ﬀ1 Gﬀ and S := limﬀω ﬀ1 Sﬀ.
As the Sﬀ have cardinality uniformly bounded (by Cr1), S is ﬁnite. The set
S need not generate G, but it certainly generates some subgroup hSi of this
group. Since jBS  (r)j  Crd for all ﬀ and all 1  r  ﬀ, we see on taking

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

146 2. Related articles

ultralimits that |B S (r)| ≤ Crd for all r. Thus ⟨S⟩ is of polynomial growth,
and is thus virtually nilpotent.

Now we need to undo the ultralimit, but this requires a certain amount
of preparation. We know that ⟨S⟩ contains a ﬁnite index nilpotent subgroup
G 0. As ⟨S⟩ is ﬁnitely generated, the ﬁnite index subgroup G 0 is also
8. Let
S0 be a set of generators for G 0. Since G 0 is nilpotent of some step s, all
commutators of S0 of length at least s + 1 vanish.

Writing S0 as an ultralimit of S0
ﬀ, we see that the S0
ﬀ are ﬁnite subsets
of G ﬀ which generate some subgroup G 0
ﬀ. Since all commutators of S0 of
length at least s + 1 vanish, the same is true for S0
ﬀ for  close enough to
1 , and so G 0
ﬀ is nilpotent for such  with step bounded uniformly in .

Finally, if we let R be large enough that B S (R) intersects every coset of
G 0, then we can cover B S (R+1) by a product of B S (R) and some elements of
G 0 (which are of course ﬁnite products of elements in S0 and their inverses).
Undoing the ultralimit, we see that for  suﬃciently close to 1 , we can
cover B S (R + 1) by the product of B S (R) and some elements of G 0
ﬀ.
Iterating this we see that we can cover all of G ﬀ by B S (R) times G 0
ﬀ, and
so G 0
ﬀ has ﬁnite index bounded uniformly in . But this contradicts the
construction of G ﬀ. 

∫emark 2..22.As usual, the argument gives no eﬀective bound on MC;d.
Obtaining such an eﬀective bound is in fact rather non-trivial; see [⋃h29]
for further discussion.

2..4. √√lîation: Furstenberg ̂orres√onden̂e √rin̂i√le.Let me
now redo another application of the correspondence principle via ultralimit
analysis. We will begin with the following famous result of Furstenberg
[Fu977]:

Theorem 2..23(Furstenberg recurrence theorem).Let(X∅B∅ ∅ T) be a
measure-preserving system, and letA ⊂ X have positive measure. Let∥ ≥ 1.
Then there existsr >0 such thatA ∩ T r A ∩ · · · ∩ T (k 1) r A is non-empty.

We then use this theorem and ultralimit analysis to derive the following
well-known result of Szemer´edi [⋃z975]:

Theorem 2..24(Szemer´edi’s theorem).Every set of integers of positive
upper density contains arbitrarily long arithmetic progressions.

8Here is a quick proof of this claim: for R large enough, BS (R) will intersect every coset
of G0. As a consequence, one can describe the action of hSi on the ﬁnite set hSi=G0 using only
knowledge of BS (2R + 1) \ G0. In particular, BS (2R + 1) \ G0 generates a ﬁnite index subgroup.
Increasing R, the index of this subgroup is non-increasing, and thus must eventually stabilise. At
that point, we generate all of G0.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

2.1. Ultralimit analysis 147

Proo{.Suppose this were not the case. Then there exists ∥  1 and a set
A of positive upper density with no progressions of length ∥. Unpacking the
deﬁnition of positive upper density, this means that there exists ◦ > 0 and
a sequence Nα ! 1 such that

jA “ [ΓN α∅ Nα]j  ◦j[ΓNα∅ Nα]j

for all . We pass to an ultralimit, introducing the limit natural number
N := limα! α1 Nα and using the ultrapower  A = limα!α 1 A (note that A
is a space, not an ordinary object). Then we have

j
 A “ [ΓN∅ N]j  ◦j[ΓN∅ N]j

where the cardinalities are in the limit sense. Note also that  A has no
progressins of length ∥.

Consider the space of all boolean combinations of shifts  A + rof  A,
where rranges over (standard) integers, thus for instance

(
 A + 3) “ (
 A + 5)n(
 A Γ 7)

would be such a set. We call such sets deβnable sets. We give each such
deﬁnable set B a limit measure

(B) := jB “ [ΓN∅ N]j=[ΓN∅ N]:

This measure takes values in the limit interval  [0∅1] and is clearly a ﬁnitely
additive probability measure. It is also nearly translation invariant in the
sense that (B + ∥) = (B) + o(1)

for any standard integer ∥, where o(1) is an inβnitesimal(i.e. a limit real
number which is smaller in magnitude than any positive standard real num-
ber). In particular, the standard part st() ofis a ﬁnitely additive standard
probability measure. Note from construction that st()(A) ◦.

Now we convert this ﬁnitely additive measure into a countably additive
one. Let 2∫ be the set of all subsets B of the integers. This is a compact
metrisable space, which we endow with the Borel ⊃-algebra B and the stan-
dard shift T : B 7! B + 1. The Borel ⊃-algebra is generated by the clopen
sets in this space, which are boolean combinations of T rE , where E is the
basic cylinder setE := fB 2 2∫ : 0 2 B g. Each clopen set can be assigned a
deﬁnable set in  Z by mapping T rE to  A+rand then extending by boolean
combinations. The ﬁnitely additive probability measure st() on deﬁnable
sets then pulls back to a ﬁnitely additive probability measure  on clopen
sets in 2∫ . Applying the Caratheodory extension theorem(see e.g. [Ta∈0∞∞,
x1.7]), taking advantage of the compactness of 2∫ , we can extend this ﬁnitely
additive measure to a countably additive Borel probability measure.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

148 2. Related articles

By construction, (E ) ≥ ◦ > 0. Applying Theorem 2.1.23, we can ﬁnd
r >0 such that E ∩ T r E ∩ · · · ∩ T (k 1) r E is non-empty. This implies that
 A ∩ ( A + r) ∩ · · · ∩ ( A + (∥ − 1)r) is non-empty, and so  A contains an
arithmetic progression of length ∥, a contradiction. 

Remark 2.1.25. The above argument is nearly identical to the usual proof
of the correspondence principle, which uses ∑rokhorov's theorem (see e.g.
[Ta2010, §1.10]) instead of ultraﬁlters. The measure constructed above is
essentially the Loeb measure [Lo1975] for the ultraproduct.

2.1.5. Relationship with nonstandard analysis. Ultralimit analysis is
extremely close to, but subtly diﬀerent from, nonstandard analysis, because
of a shift of emphasis and philosophy. The relationship can be illustrated
by the following table of analogies:
Digits Strings of digits Numbers
Symbols Strings of symbols Sentences
Set theory Finite von Neumann ordinals Peano arithmetic
Rational numbers Q Q Real numbers R
Real analysis Analysis on R Complex analysis
R R2 Euclidean plane geometry
R Coordinate chart atlases Manifolds
R Matrices Linear transformations
Algebra Sheaves of rings Schemes
Deterministic theory Measure theory Probability theory
Probability theory Von Neumann algebras Noncommutative prob. theory
Classical mechanics Hilbert space mechanics Quantum mechanics
Finitary analysis Asymptotic analysis Inﬁnitary analysis
Combinatorics Correspondence principle Ergodic theory
Quantitative analysis Compactness arguments Qualitative analysis
Standard analysis Ultralimit analysis Nonstandard analysis

Here R is the algebraic completion of the reals, but Q is the metric
completion of the rationals.

In the ﬁrst column one has a “base” theory or concept, which implic-
itly carries with it a certain ontology and way of thinking, regarding what
objects one really cares to study, and what objects really “exist” in some
mathematical sense. In the second column one has a fancier theory than
the base theory (typically a “limiting case”, a “generalisation”, or a “com-
pletion” of the base theory), but one which still shares a close relationship
with the base theory, in particular largely retaining the ontological and con-
ceptual mindset of that theory. In the third column one has a new theory,
which is modeledby the theories in the middle column, but which is not
tied to that model, or to the implicit ontology and viewpoint carried by

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

2.2. Higher order Hilbert spaces 149

that model. For instance, one ⌋a\ think of a complex number as an element
of the algebraic completion of the reals, but one does not ⟨ave to, and in-
deed in many parts of complex analysis or complex geometry one wants to
ignore the role of the reals as much as possible. Similarly for other rows of
the above table. See for instance [Ta∈0∞∞⌊, x1.1] for further discussion of
the distinction between measure theory and probability theory.

Remar∥ ∈.∞.∉.The relationship between the second and third columns
of the above table is also known as the ma√-terr⟩tory relat⟩o\.

Returning to ultralimit analysis, this is a type of analysis which still
shares close ties with its base theory, standard analysis, in that all the ob-
jects one considers are either standard objects, or ultralimits of such objects
(and similarly for all the spaces one considers). But more importantly, one
continues to t⟨⟩\∥ o{ nonstandard objects as being ultralimits of standard
objects, rather than having an existence which is largely independent of the
concept of base theory of standard analysis. This perspective is reversed in
nonstandard analysis: one views the nonstandard universe as existing in its
own right, and the fact that the standard universe can be embedded inside it
is a secondary feature (albeit one which is absolutely essential if one is to use
nonstandard analysis in any nontrivial manner to say something new about
standard analysis). In nonstandard analysis, ultraﬁlters are viewed as one
tool in which one can construct the nonstandard universe from the standard
one, but their role in the subject is otherwise minimised. In contrast, the
ultraﬁlter α1 plays a prominent role in ultralimit analysis.

In my opinion, none of the three columns here are inherently “better”
than the other two; but they do work together quite well. In particular, the
middle column serves as a very useful bridge to carry results back and forth
between the worlds of the left and right columns.

2.2. Higher order Hilbert spaces

Recall that a (complex, semi-deﬁnite) ⟩\\er √rodu⌋t s√a⌋eis a complex vec-
tor space V equipped with a sesquilinear form h,i : V  V ! C which is
conjugate symmetric, in the sense that hw, vi = hv, wi for all v, w 2 V , and
non-negative in the sense that hv, vi  0 for all v 2 V . By inspecting the
non-negativity of hv+ w, v+ wi for complex numbers  2 C, one obtains
the Cau⌋⟨y-S⌋⟨warz ⟩\equal⟩ty

jhv, wij ˇ jhv, vij1=2jhw, wij1=2;

if one then deﬁnes kvk := jhv, vij1=2, one then quickly concludes the tr⟩a\}le
⟩\equal⟩ty kv + wk ˇ k vk + kwk

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

150 2. Related articles

which then soon implies that ∥∥ is a sem⟩-\orm
9 on V . If we make the
additional assumption that the inner product ⟨, ⟩ is positive deﬁnite, i.e.
that ⟨v, v⟩ > 0 whenever v is non-zero, then this semi-norm becomes a norm.
If V is complete with respect to the metric d(v, w) := ∥v − w∥ induced by
this norm, then V is called a H⟩l⌊ert s√a⌋e.

The above material is extremely standard, and can be found in any
graduate real analysis text (e.g. [Ta2010, §1.6]). But what is perhaps
less well known (except inside the ﬁelds of additive combinatorics and er-
godic theory) is that the above theory of classical Hilbert spaces is just
the ﬁrst case of a hierarchy of ⟨⟩}⟨er order H⟩l⌊ert s√a⌋es, in which the
binary inner product f, g ↦→ ⟨f, g⟩ is replaced with a 2d-ary inner product
(f! )! 2f0;1g d↦→ ⟨(f! )! 2f0;1g d⟩ that obeys an appropriate generalisation of the
conjugate symmetry, sesquilinearity, and positive semi-deﬁniteness axioms.
Such inner products then obey a higher order Cauchy-Schwarz inequality,
known as the Cau⌋⟨y-S⌋⟨warz-Gowersinequality, and then also obey a tri-
angle inequality and become semi-norms (or norms, if the inner product was
non-degenerate). Examples of such norms and spaces include the Gowers
u\⟩{orm⟩ty \orms ∥∥Ud(G), the Gowers ⌊o§ \orms ∥∥ d(X1 X d), and the
Gowers-Host-Kra sem⟩\orms∥∥Ud(X); a more elementary example are the

family of Lebesgue spaces L2d
(X) when the exponent is a power of two.
They play a central role in modern additive combinatorics and to certain
aspects of ergodic theory, particularly those relating to Szemer´edi’s theorem
(or its ergodic counterpart, the Furstenberg multiple recurrence theorem);
they also arise in the regularity theory of hypergraphs (which is not unre-
lated to the other two topics).

A simple example to keep in mind here is the order two Hilbert space
L4(X) on a measure space X = (X, B, µ), where the inner product takes the
form
 ⟨f00, f01, f10, f11⟩L4 (X) := Z

X f00(x)f01(x)f10(x)f11(x) dµ(x).

In this section we will set out the abstract theory of such higher or-
der Hilbert spaces; this is drawn from the more concrete work of Gowers
[Go2001] and Host-Kra [HoKr2005], but this material is actually quite
abstract, and is not particularly tied to any explicit choice of norm so long
as a certain axioms are satisﬁed. In applications, one can (and probably

9A semi-normon a vector space V is a map v 7ω kvk from V to the non-negative reals
[0; +1) which obeys the triangle inequality kv + wk  k vk + kwk and the homogeneity relation
kcvk = jcjkvk for all v; w 2 V and c 2 C. A normis a semi-norm with the additional property
that kvk > 0 for all non-zero v.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

2.2. Higher order Hilbert spaces 151

should) work in the concrete setting, but we will record the abstract ax-
iomatic approach here, as this does not appear to be explicitly in the liter-
ature elsewhere.

∈.∈.∞. De\⟩t⟩o\ o{ a ⟨⟩}⟨er order H⟩l⌊ert s√a⌋e.Let V∅ W be com-
plex vector spaces. Then one can form the (algebraic) tensor productV
 W,
which can be deﬁned as the vector space spanned by formal tensor products
v
 w, subject to the constraint10 that the tensor product is bilinear (i.e.
that v
 (w1 +w2) = (v
 w1)+(v
 w2), v
 ⌋w = ⌋(v
 w), and similarly with
the roles of v and w reversed). More generally, one can deﬁne the tensor
product N ω2
 Vω of any ﬁnite family of complex vector spaces Vω.

Given a complex vector space V , one can deﬁne its complex conjugate
11

V to be the set of formal conjugates fv: v2 V g of vectors in V , with the
vector space operations given by
 0 := 0

v+ w := v+ w

⌋v:= ⌋v:

The map v7ω vis then an antilinear isomorphism from V to V . We adopt
the convention that v = v, thus v 7ω v is also an antilinear isomorphism
from V to V .

For inductive reasons, it is convenient to use ﬁnite sets A of labels,
rather than natural numbers d, to index the order of the systems we will
be studying. In any case, the cardinality jAjof the set of labels will be the
most important feature of this set.

Given a complex vector space V and a ﬁnite set A of labels, we form the
tensor cube V [A] to be
 V [A] := O

ω2f0,1gA C
jωjV∅

where C is the conjugation map V 7ω V , and j→j := P i2A →i when → =
(→i)i2A; thus for instance12 V [fg]= V , V [f1g] V
 V is spanned by tensor
products v0
 v1 with v0∅ v1 2 V , V [f1,2g] V
 V
 V
 V is spanned by
tensor products v00
 v01
 v10
 v11 with v00∅ v01∅ v10∅ v11 2 V , and so forth.

10More formally, one would quotient out by the subspace generated by elements such as
v
 (w1 + w2 ) ( (v
 w1 ) ( (v
 w2 ) or v
 cw ( c(v
 w) to create the tensor product.
11One can work with real higher order Hilbert spaces instead of complex ones, in which case
the conjugation symbols can be completely ignored.
12It would be better to order the four factors v00 , v01 , v10 , v11 in a square pattern, rather
than linearly as is done here, but we have used the inferior linear ordering here for typographical
reasons.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

152 2. Related articles

Given any ﬁnite set A of labels and any ⟩ ∈ A, one can form an identiﬁ-
cation V [A] ≡ V [Anf ig] ⊗ V [Anfig]

by identifying a tensor product N ω2f0,1g A Cjωjvω in V [A] with
0

@ O

ω2f0,1g Ani Cjωjv(ω,0)
1

A ⊗
 0

@ O

ω2f0,1g Ani Cjωjv(ω,1)
1

A

where, for →0 ∈ {0∅1}Ani and →i ∈ {0∅1}, (→0∅ →i) denotes the element of
{0∅1}A that agrees with →0 on A\⟩ and equals →i on ⟩. We refer to this
identiﬁcation as ⊗i, thus

⊗i : V [Anf ig] ⊗ V [Anf ig] → V [A]

is an isomorphism, and one can deﬁne the ⟩th tensor product v⊗i w ∈ V [A]

of two elements v∅ w∈ V [Anf ig]. Thus for instance, if v = v0 ⊗ v1 and
w = w0 ⊗ w1 are elements of V [f1g] , then

v⊗2 w = v0 ⊗ v1 ⊗ w0 ⊗ w1

using the linear ordering conventions used earlier. If we instead view v∅ w
as elements of V [f2g] rather than V [f1g] , then

v⊗1 w = v0 ⊗ w0 ⊗ v1 ⊗ w1:

A (semi-)deﬁnite inner product ⟨∅⟩ on a complex vector space V can be
viewed as a linear functional ⟨⟩ : V ⊗ V → C on V [f1g] = V ⊗ V obeying
a conjugation symmetry and positive (semi-)deﬁniteness property, deﬁned
on tensor products v⊗ w as ⟨v⊗ w⟩ := ⟨v∅ w⟩. With this notation, the
conjugation symmetry axiom becomes

⟨w ⊗ v⟩ := ⟨v⊗ w⟩

and the positive semi-deﬁniteness property becomes

⟨v⊗ v⟩ ≥ 0

with equality iﬀ v= 0 in the deﬁnite case.

Now we can deﬁne a higher order inner product space.

Denition 2.2.1(Higher order inner product space). Let A be a ﬁnite set
of labels. A (semi-denite) inner product space of orderA is a complex
vector space V , together with a linear functional ⟨⟩A : V [A] → C that obeys
the following axiom:

• (Splitting axiom) For every ⟩ ∈ A, ⟨⟩A is a semi-deﬁnite classical
inner product ⟨⟩Anfig on V [Anf ig] ⊗ V [Anfig] , which we identify with
V [A] using ⊗i as mentioned above.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

2.2. Higher order Hilbert spaces 153

We say that the inner product space is √os⟩t⟩ve de\⟩teif one has∞3h
N ! 2f0;∞gA Cj! jv i A >
0 whenever v 2 V is non-zero.

For instance, if  is the empty set, then an inner product space of order 
is just a complex vector space V equipped with a linear functional v 7! hv i A
from V to C (which one could interpret as an expectation or a trace, if one
wished). If  is a singleton set, then an inner product space of order  is
the same thing as a classical inner product space.

If  = f1;2g, then an inner product space of order  is a complex vector
space V equipped with a linear functional hiA : V Ω V Ω V Ω V, which in
particular gives rise to a quartisesquilinear (!) form

(v 00 ; v0∞; v∞0; v∞∞) 7! hv 00 Ω v 0∞ Ω v ∞0 Ω v ∞∞i A

which is a classical inner product in two diﬀerent ways, thus for instance we
have hv 00 Ω v 0∞ Ω v ∞0 Ω v ∞∞i A = hv 00 Ω v 0∞; v∞0 Ω v ∞∞i f∈g

for v 00 ; v0∞; v∞0; v∞∞2 V and some classical inner product h;i f∈g on V∪f∈g],
and similarly

hv 00 Ω v 0∞ Ω v ∞0 Ω v ∞∞i A = hv 00 Ω v ∞0; v0∞ Ω v ∞∞i f∞g

for some classical inner product h;i f∞g on V∪f∞g].

2.2.2. Examples.Let us now give the three major (and inter-related)
examples of inner product spaces of higher order: the Gowers u\⟩{orm⟩ty
s√a⌋es, that arise in additive combinatorics; theGowers ⌊o§ s√a⌋es, which
arise in hypergraph regularity theory, and the Gowers-Host-Kra s√a⌋es,
which arise in ergodic theory. We also remark on the much simpler example
of the Lebesgue spaces of dyadic exponent.

The ﬁrst example is the family of Gowers u\⟩{orm⟩ty s√a⌋esUA(G),
which we will deﬁne for simplicity on a ﬁnite additive group G (one can
also deﬁne this norm more generally on ﬁnite subsets of abelian groups, and
probably also nilpotent groups, but we will not do so here). Here  is a
ﬁnite set of labels; in applications one usually sets  := f1; : : : ; dg, in which
case one abbreviates Uf∞;:::;dg(G) asUd(G). The spaceUA(G) is the space
of all functions f: G! C, and so UA(G)∪A]can be canonically identiﬁed
with the space of functions F: Gf0;∞gA ! C. To make UA(G) into an inner
product space of order , we deﬁne

hFi A := Ex2G [A] F(x )

∞3Note {rom t⟨e s√l⟩tt⟩\} a§⟩om t⟨at o\e already ⟨as t⟨e \o\-str⟩⌋t ⟩\equal⟩ty. But t⟨e
√os⟩t⟩ve de\⟩te\ess √ro√erty ⟩s wea∥er t⟨a\ t⟨e assert⟩o\ t⟨at ea⌋⟨ o{ t⟨e ⌋lass⟩⌋al ⟩\\er √rodu⌋ts
are t⟨emselves \o\-de}e\erate.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

154 2. Related articles

where G ∪A]is the subgroup of G f0;∞gA consisting of the parallelopipeds

G ∪A]:= f(§ + X

i2A →i⟨ i)! 2f0;∞gA : § 2 G∅ ⟨ i 2 G for all ⟩ 2 Ag:

This is clearly a linear functional. To verify the splitting axiom, one observes
the identity
 hF0
 i F∞iA = E hj 2G for j 2Anfig E x;hi 2G

F0 ((§ + X

j 2Anfig →j ⟨ j )! 2f0;∞gAnfig )

F∞((§ + ⟨ i + X

j 2Anfig →j ⟨ j )! 2f0;∞gAnfig )

for any ⟩ 2 A and F0 ∅ F∞ 2 U A(G) ∪Anfig]. The right-hand side is then a
semi-deﬁnite classical inner product on U A(G) ∪Anfig]; the semi-deﬁniteness
becomes more apparent if one makes the substitution (§∅ y ) := (§∅ § + ⟨ i).

Specialising to tensor products, we obtain the Gowers inner product

h
 ! 2f0;∞gA C
j! j{! iA = E x2G;h i 2G8i2A Y

! 2f0;∞gA C
j! j{! (§ +
 AX

i=∞→i⟨ i):

Thus, for instance, when A = f1∅2g,

h{00
 {0∞
 {∞0
 {∞∞iA

= E x;h∞;h∈2G {00 (§) {∞0(§ + ⟨ ∈){∞0(§ + ⟨ ∞){∞∞(§ + ⟨ ∞+ ⟨ ∈):

The second example is the family of the (incomplete) Gowers box spaces
 A \ L1 (X ), deﬁned on a Cartesian product X := Q i2A X i of a family
X i = (X i∅Bi∅ i) of measure spaces indexed by a ﬁnite set A. To avoid
some minor technicalities regarding absolute integrability, we assume that
all the measure spaces have ﬁnite measure (the theory also works in the
⊃-ﬁnite case, but we will not discuss this here). This space is the space of
all bounded measurable functions { 2 L1 (X ) (here, for technical reasons,
it is best not to quotient out by almost everywhere equivalence until later in
the theory). The tensor power L1 (X )∪A]can thus be identiﬁed with a sub-
space of L1 (X f0;∞gA ) (roughly speaking, this is the subspace of “elementary
functions”). We can then deﬁne an inner product of order A by the formula

hFi = Z

X
 Z

X F(((§ ! i ;i)i2A )! 2f0;∞gA ) d(§0 )d(§∞)

for all F 2 L1 (X )∪A]ˆ L1 (X f0;∞gA ), where § 0 = (§ 0;i )i2A and § ∞ =
(§ 0;i )i2A are integrated using product measure  := Q i2A i.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

2.2. Higher order Hilbert spaces 155

The veriﬁcation of the splitting property is analogous to that for the
Gowers uniformity spaces. Indeed, there is the identity

⟨F0 ⊗i F1⟩A = Z

X (i)
 Z

X (i)
 Z

Xi
 Z

Xi

F0  (§ ω
j ,j)j2Anfig∅ §0,i
 ω2Anfig

F1  (§ ω
j ,j)j2Anfig∅ §1,i
 ω2Anfig

di(§ 0,i)di(§ 1,i)d
(i)(§ (i)
0 )d
(i)(§ (i)
1 )

for all ⟩ ∈ A and F0∅ F1 ∈ L1 (X )[Anfig] ⊂ L1 (X f0,1gAnfig
), where X (i) :=
Q j2Anfig X j, (i) := Q j2Anfig j, and § (i)
a = (§ a,j)j2Anfig for a = 0∅1. From
this formula one can verify the inner product property without much trouble
(the main diﬃculty here is simply in unpacking all the notation).

The third example is that of the (incomplete) Gowers-Host-Kra spaces
U A ∩ L1 (X ). Here, X = (X∅B∅ ) is a probability space with an invertible
measure-preserving shift T , which of course induces a measure-preserving
action \ ↦→ T n of the integers Z on X . (One can replace the integers in
the discussion that follows by more general nilpotent amenable groups, but
we will stick to integer actions for simplicity.) It is often convenient to also
assume that the measure  is ergodic, though this is not strictly required
to deﬁne the semi-norms. The space here is L1 (X ); the power L1 (X )[A]

is then a subspace of L1 (X f0,1gA ). One can deﬁne the Host-Kra measure
[A] on X [A] for any ﬁnite A by the following recursive procedure. Firstly,
when A is empty, then [A] is just . If instead A is non-empty, then pick
an element ⟩ ∈ A and view X [A] as the Cartesian product of X [Anfig] with
itself. The shift T acts on X , and thus acts diagonally on X [Anfig] by acting
on each component separately. It is not hard to show inductively from the
construction that we are about to give that [Anfig] is invariant with respect
to this diagonal shift, which we will call T [Anfig]. The product ⊃-algebra
B[Anfig] has an invariant factor (B[Anfig])T [Anfig]with respect to this shift.
We then deﬁne [A] to be the relative product of [Anfig] with itself relative
to this invariant factor. One can show that this deﬁnition is independent of
the choice of ⟩, and that the form

⟨F⟩A := Z

X [A] F d
[A]

is an inner product of order A; see [HoKr∈′′5] for details.

A ﬁnal (and signiﬁcantly simpler) example of a inner product space
of order A is the Lebesgue space L2jAj
(X ) on some measure space X =

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

156 2. Related articles

(X∅B∅ ), with inner product

⟨F⟩A := Z

X F((§∅ : : : ∅ §)) d(§)

where § ↦→ (§∅ : : : ∅ §) is the diagonal embedding from X to X [A] ≡ X 2jAj .
For tensor products, this inner product takes the form

⟨ O

! 2f0;1gA Cj! j{! ⟩A = Z

X
 Y

! 2f0;1gA Cj! j{! d∅

thus for instance when A = {1∅2},

⟨{00 ⊗ {01 ⊗ {10 ⊗ {11⟩A = Z

X {00{01{10{11 d:

We leave it as an exercise to the reader to show L2jAj (X ) is indeed an inner
product space of order A. This example is (the completion of) the Gowers-
Host-Kra space in the case when the shift T is trivial.

We also remark that given an inner product space (V∅⟨⟩A) of some order
A, given some subset B of A, and given a ﬁxed vector v in V , one can
deﬁne a weighted inner product space (V∅⟨⟩B;v ) of order B by the formula

⟨F⟩B;v := ⟨F ⊗ O

! 2f0;1gA nf0;1gB Cj! jv ⟩A

for all F ∈ V [B], where {0∅1}B is embedded in {0∅1}A by extension by
zero and the tensor product on the right-hand side is deﬁned in the obvious
manner. One can check that this is indeed a weighted inner product space.
This is a generalisation of the classical fact that every vector v in an inner
product space V naturally deﬁnes a linear functional w ↦→ ⟨w∅ v ⟩ on V . In
the case of the Gowers uniformity spaces with v := 1, this construction
takes U A(G) to U B (G); similarly for the Gowers box spaces.

2.2.3. Basic theory.Let V be an inner product space of order A for some
ﬁnite non-empty A. The splitting axiom tells us that

⟨F0 ⊗i F1⟩A = ⟨F0∅ F1⟩Anfig

for all ⟩ ∈ A, F0∅ F1 ∈ V [Anfig], and some inner product ⟨∅⟩ on X [Anfig]. In
particular one has
 ⟨F ⊗i F⟩A ≥ 0

for all F ∈ V [Anfig], as well as the classical Cauchy-Schwarz inequality

|⟨F0 ⊗i F1⟩A| ≤ |⟨F0 ⊗i F0⟩A|
1=2|⟨F1 ⊗i F1⟩A|1=2:

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

2.2. Higher order Hilbert spaces 157

If we specialise this inequality to the tensor products

Fa := O

→02f0∅1g Anfi g C
j→0jva∅→0

for various va∅→0 2 V , one concludes that

jh O

→2f0∅1g A C
j→jv→iAj  Y

a2f0∅1g jh O

→2f0∅1g A C
j→jva∅→0iAj
1=2

where we write →= (→⟩∅ →0) for some →⟩ 2 f0∅1gand →0 2 f0∅1gAnf ⟩g. If we
iterate this inequality once for each ⟩ 2 A, we obtain the Cauchy-Schwarz-
Gowers inequality
 jh O

→2f0∅1g A C
j→jv→iAj  Y

→2f0∅1g A kv→kA

where kvkA := jh O

→2f0∅1g A C
j→jviAj
1=2jAj :

The quantity kvkA is clearly non-negative and homogeneous. We also have
the Gowers triangle inequality

kv0 + v1kA  k v0kA + kv1kA∅

which makes kkA a semi-norm (and in fact a norm, if the inner product
space was positive deﬁnite). To see this inequality, we ﬁrst raise both sides
to the power 2jAj:
 kv0 + v1k
2jAj
A  (kv0kA + kv1kA)2jAj :

The left-hand side can be expanded as

jh O

→2f0∅1g A C
j→j(v0 + v1)iAj

which after expanding out using linearity and the triangle inequality, can be
bounded by X

2f0∅1g f0,1g A jh O

→2f0∅1g A C
j→jvω iAj

which by the Cauchy-Schwarz-Gowers inequality can be bounded in turn by
X

2f0∅1g f0,1g A
 Y

→2f0∅1g A kvω kA

which can then be factored into (kv0kA + kv1kA)2jAj as required.

Note that when A is a singleton set, the above argument collapses to
the usual derivation of the triangle inequality from the classical Cauchy-
Schwarz inequality. It is also instructive to see how this collapses to one

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

158 2. Related articles

of the standard proofs of the triangle inequality for L∈k (X ) using a large
number of applications of the Cauchy-Schwarz inequality.

In analogy with classical Hilbert spaces, one can deﬁne a Hilbert space
of orderA to be an inner product space V of order A which is both positive
deﬁnite and complete, so that the norm kk A gives V the structure of a
Banach space. A typical example is U ∈(G) for a ﬁnite abelian G, which is
the space of all functions { : G ! C with the norm

k{ kU2(G)= k ˆ{k` 4(^G)

where ˆG is the Pontraygin dual of G (i.e. the space of homomorphisms
∼: § 7! ∼ § from G to R=Z) and ˆ{(∼) := Ex2G{(§)e( ∼  §) is the Fourier
transform. Thus we see that `4( ˆG) is a Hilbert space of order 2. More
generally, L∈k (X ) for any measure space X and any ∥  0 can be viewed as
a Hilbert space of order ∥.

The Gowers norms U d(G) and Gowers-Host-Kra norms U d(X ) coincide
in the model case when X = G = Z=NZ is a cyclic group with uniform
measure and the standard shift T : § 7! § + 1. Also, the Gowers norms
U d(G) can be viewed as a special case of the box norms via the identity

k{ kUd (G):= k{ ﬃsk  d (Gd )

where s : G d ! G is the summation operation s(§ ∞∅ : : : ∅ §d) := § ∞+    + § d.

Just as classical inner product spaces can be made positive deﬁnite by
quotienting out the norm zero elements, and then made into a classical
Hilbert space by metric completion, inner product spaces of any order can
also be made positive deﬁnite and completed. One can apply this procedure
for instance to obtain the completed Gowers box spaces  A(X ) and the
completed Gowers-Host-Kra spaces U A(X ) (which become L∈|A| (X ) when
the shift T is trivial). These spaces are related, but not equal, to their
Lebesgue counterparts Lp(X ); for instance for the Gowers-Host-Kra spaces
in the ergodic setting, a repeated application of Young’s inequality reveals
the inequalities
 k{ kUA (X)ˇ k{ kL2|A| =(|A|〉)(X)ˇ k{ kL∞ (X)∅

and so U A(X ) contains a (quotient) of L∈|A| =(jAj+∞)(X ).

The null space of the Gowers-Host-Kra norm U A(X ) in L1 (X ) in the
ergodic case is quite interesting; it turns out to be the space L1 (Z <jAj)? of
bounded measurable functions { whose conditional expectation E({jZ <jAj
on the characteristic factorZ <jAj of order jAj  1 of X vanishes; in particular,
L1 (Z <jAj) becomes a dense subspace of U A(X ), embedded injectively. It is
a highly non-trivial and useful result, ﬁrst obtained in [HoKr2005],bthat

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

2.2. Higher order Hilbert spaces 159

Z<jAj is the inverse limit of all nilsystem factors of step at most |A| − 1; this
is the ergodic counterpart of the inverse conjecture for the Gowers norms.

2.2.4. The category of higher order inner product spaces. The
higher order Hilbert spaces L1(X), L2(X), L4(X), L8(X), . . . are related to
each other via H¨older’s inequality; the pointwise product of two L4 functions
is in L2, the product of two L8 functions is in L4, and so forth. Furthermore,
the inner products on all of these spaces are can be connected to each other
via the pointwise product.

We can generalise this concept, giving the class of inner product spaces
(of arbitrary orders) the structure of a category.

Deﬁnition 2.2.2. Let B ⊆ A be ﬁnite sets, and let VB = (VB , ⟨⟩B ), VA =
(VA, ⟨⟩A) be inner product spaces of order B, A respectively. An isometry φ
from VA to VB is a linear map

φ: ⊗

→2f0∅1g AnB Cj→jVA → VB

which preserves the inner product in the sense that
〈 ⊗

→2f0∅1g A Cj→jv→

〉

A

=
 〈 ⊗

→02f0∅1g B Cj→0jφ( ⊗

→002f0∅1g AnB Cj→00jv(→0∅→00))
〉

B
 ,

where ω0, ω00→ (ω0, ω00) is the obvious concatenation map from {0, 1}B ×
{0, 1}AnB to {0, 1}A.

Given an isometry φ from VA to VB , and an isometry   from VB to VC
for some C ⊂ B ⊂ A, one can form the composition

  ◦ φ: ⊗

→2f0∅1g AnC Cj→jVA → VC

by the formula

  ◦ φ
 

 ⊗

→2f0∅1g AnC Cj→jv→





:=
 

 ⊗

→02f0∅1g BnC Cj→0jφ
 

 ⊗

→002f0∅1g AnB Cj→00jv(→0∅→00)









and extending by linearity; one can verify that this continues to be an isom-
etry, and that the class of inner product spaces of arbitrary order together
with isomorphisms form a category.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

160 2. Related articles

When A = B is a singleton set, the above concept collapses to the
classical notion of an isometry for inner product spaces. Of course, one could
specialise to the subcategory of higher order Hilbert spaces if desired. The
inner product on a higher order inner product space can now be interpreted
as an isometry from that space to the space C (viewed as an inner product
space of order ;), and is the unique such isometry; in the language of category
theory, this space C becomes the terminal objectof the category.

A model example of an isometry is the sesquilinear product map {∅ }7!
{}, which is an isometry from L2d(X ) to L2d  (X ) for any d  1. For the
Gowers-Host-Kra norms, the map {∅ }7! { Ω } is an isometry from U d(X [k])
to U d 1 (X [k+1]) for any d  2 and ∥  0.

To see analogous isometries for the Gowers uniformity norms, one has
to generalise these norms to the “non-ergodic” setting when one does not
average the shift parameter ⟨ over the entire group G, but on a subgroup
H. Speciﬁcally, for ﬁnite additive groups H ˇ G and functions {ω: G ! C
with →2 f 0∅1gA, deﬁne the local Gowers inner product

hΩω2f0,1g A C
jωj{ωi UA (G,H) = E x2G,h i 2H 8i2A Y

ω2f0,1g A C
jωj{ω(§ +
 AX

i=1 →i⟨ i):

By foliating G into cosets of H, one can express this local Gowers inner
product as an amalgam of the ordinary Gowers inner product and a Lebesgue
inner product. For instance, one has the identity

k{kUA (G,H) =
 ′

@ X

y 2G/Hk{(∆+ y )k
2jAj
UA (H)
∞

A
1/2jAj
 :

We deﬁne the inner product space U A(G∅ H) to be the space of functions
from G to C with the above inner product. Given any | 2 A, we can then
create an isometry ∆ = ∆j from U A(G∅ H) to U Anfjg(G H∅ H) by deﬁning
14

∆({∅ {
0)(§∅ ⟨) := {(§ + ⟨) { 0(§):

One can obtain analogous isometries for the Gowers box norms after
similarly generalising to “non-ergodic” settings; we leave this as an exercise
to the interested reader.

Actually, the “derivative maps” from inner product spaces VA of order A
to those of order Anf| g can be constructed abstractly. Indeed, one can view
VA Ω VA as an inner product space of order Anf| g with the inner product

14This isometry does not ostensibly depend on j, except through the labels of the inner
product of the target space UAnfj g (G  H, H) of the isometry.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

2.2. Higher order Hilbert spaces 161

deﬁned on tensor products by
* O

→02f0∅1gAnfj g C
j→0j(v →0∅0
 v →0∅1)

+
 Anf| g

:=
 * O

(→0∅→j )2f0∅1gA C
j(→0∅→j )jv →0∅→j
 +
 A

and then the map v; w 7ω v
 w is an isometry. One can iterate this con-
struction and obtain a cubic complex of inner product spaces

VB := O

→2f0∅1gAnB C
j→jVA

of order B for each B ρ , together with a commuting system of derivative
isometries ∆ from VB to VB nf| g for each j 2 B ρ .

Conversely, one can use cubic complexes to build higher order inner
product spaces:

Proposition 2.2.3. Let be a nite set. For eachB ρ , suppose that we
have a vector spaceVB equipped with af0;1gB -sesquilinear form

hiB : O

→2f0∅1gB C
j→jVB ω C

and suppose that for eachj 2 B one has a sesquilinear product

∆B ω B nf| g : VB
 VB ω VB nf| g

obeying the compatibility conditions
* O

→2f0∅1gB C
j→jv →

+
 B

=
 * O

→02f0∅1gB nfj g ∆B ω B nf| g(v (→0∅0); v(→0∅1))

+
 B nf| g

whenever v → 2 VB for all) 2 f 0;1gB . Suppose also that the formhif| g is
a classical inner product onVf| g for every j 2 . Then for eachB ρ ,
VB is an inner product space of orderj, and the maps∆B ω B nf| g become
isometries.

This proposition is established by an easy induction on the cardinality of
B. Note that we do not require the derivative maps ∆B ω B nf| g to commute
with each other, although this is almost always the case in applications.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

162 2. Related articles

∈.3. T⟨e u\⌋erta⟩\ty √r⟩\⌋⟩√le

A recurring theme in mathematics is that of dual⟩ty: a mathematical object
X can either be described ⟩\ter\ally(or in √⟨ys⟩⌋al s√a⌋e, orlo⌋ally), by
describing what X physically consists of (or what kind of maps exist ⟩\to
X ), or e§ter\ally(or in {reque\⌋y s√a⌋e, or}lo⌊ally), by describing what
X globally interacts or resonates with (or what kind of maps exist out o{
X ). These two fundamentally opposed perspectives on the object X are
often dual to each other in various ways: performing an operation on X
may transform it one way in physical space, but in a dual way in frequency
space, with the frequency space description often being a “inversion” of
the physical space description. In several important cases, one is fortunate
enough to have some sort of {u\dame\tal t⟨eoremconnecting the internal
and external perspectives. Here are some (closely inter-related) examples of
this perspective:

(i) Vector space duality A vector space V over a ﬁeld F can be
described either by the set of vectors inside V, or dually by the set of
linear functionals  : V ! F from V to the ﬁeld F (or equivalently,
the set of vectors inside the dual space V ). (If one is working in
the category of topological vector spaces, one would work instead
with continuous linear functionals; and so forth.) A fundamental
connection between the two is given by the Ha⟨\-Ba\a⌋⟨ t⟨eorem
(and its relatives); see e.g. [Ta2010, x1.5].

(ii) Vector subspace duality In a similar spirit, a subspace W of
V can be described either by listing a basis or a spanning set, or
dually by a list of linear functionals that cut out that subspace
(i.e. a spanning set for the orthogonal complement W? := f 2
V : (w) = 0 for all w 2 Wg). Again, the Hahn-Banach theorem
provides a fundamental connection between the two perspectives.

(iii) Convex duality More generally, a (closed, bounded) convex body
K in a vector space V can be described either by listing a set of
(extreme) points whose convex hull is K, or else by listing a set of
(irreducible) linear inequalities that cut out K. The fundamental
connection between the two is given by the Far∥as lemma; see
[Ta2008, x1.16] for further discussion.

(iv) Ideal-variety duality In a slightly diﬀerent direction, an algebraic
variety V in an aﬃne space An can be viewed either “in physical
space” or “internally” as a collection of points in V, or else “in
frequency space” or “externally” as a collection of polynomials on
An whose simultaneous zero locus cuts out V. The fundamental

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

2.3. The uncertainty principle 163

connection between the two perspectives is given by the \ullstelle\-
satz, which then leads to many of the basic fundamental theorems
in classical algebraic geometry; see [Ta∈008, x1.15] for further dis-
cussion.

(v) H⟩l⌊ert s√a⌋e dual⟩ty An element v in a Hilbert space H can
either be thought of in physical space as a ve⌋torin that space,
or in momentum space as a ⌋ove⌋torw 7! hv, wi on that space.
The fundamental connection between the two is given by the R⟩esz
re√rese\tat⟩o\ t⟨eorem {or H⟩l⌊ert s√a⌋es; see [Ta∈0∞0, x1.15] for
further discussion.

(vi) Sema\t⟩⌋-sy\ta⌋t⟩⌋ dual⟩ty Much more generally still, a math-
ematical theory can either be described ⟩\ter\allyor sy\ta⌋t⟩⌋ally
via its axioms and theorems, or e§ter\allyor sema\t⟩⌋ally via its
models. The fundamental connection between the two perspectives
is given by the G odel ⌋om√lete\ess t⟨eorem ; see [Ta∈0∞0⌊, x1.4]
for further discussion.

(vii) I\tr⟩\s⟩⌋-e§tr⟩\s⟩⌋ dual⟩tyA (Riemannian) manifold M can ei-
ther be viewed intrinsically (using only concepts that do not require
an ambient space, such as the Lev⟩-C⟩v⟩ta ⌋o\\e⌋t⟩o\), or extrinsi-
cally, for instance as the level set of some deﬁning function in an
ambient space. Some important connections between the two per-
spectives includes the Nas⟨ em⌊edd⟩\} t⟨eorem and the t⟨eorema
e}re}⟩um.

(viii) Grou√ dual⟩ty A group G can be described either via √rese\ta-
t⟩o\s (lists of generators, together with relations between them) or
re√rese\tat⟩o\s(realisations of that group in some more concrete
group of transformations). A fundamental connection between the
two is Cayley's t⟨eorem. Unfortunately, in general it is diﬃcult
to build upon this connection (except in special cases, such as the
abelian case), and one cannot always pass eﬀortlessly from one per-
spective to the other.

(ix) Po\trya}⟩\ }rou√ dual⟩ty A (locally compact Hausdorﬀ) a⌊el⟩a\
group G can be described either by listing its elements g 2 G, or
by listing the ⌋⟨ara⌋ters˜: G ! R/Z (i.e. continuous homomor-
phisms from G to the unit circle, or equivalently elements of ˆG).
The connection between the two is the focus of a⌊stra⌋t ⟨armo\⟩⌋
a\alys⟩s; see [Ta∈0∞0, x1.12] for further discussion.

(x) Po\trya}⟩\ su⌊}rou√ dual⟩ty A subgroup H of a locally com-
pact abelian group G can be described either by generators in H,
or generators in the orthogonal complement H? := fξ 2 ˆG : ξ ∆h =

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

164 2. Related articles

0 for all ⟨ ∈ H}. One of the fundamental connections between the
two is the Poisson summation formula.

(xi) Fourier duality A (suﬃciently nice) function { : G → C on a
locally compact abelian group G (equipped with a Haar measure
) can either be described in physical space (by its values {(§ ) at
each element § of G) or in frequency space (by the values ˆ{(∼) =R

G {(§)e(−∼·§) d(§) at elements ∼of the Pontryagin dual ˆG). The
fundamental connection between the two is the Fourier inversion
formula.

(xii) The uncertainty principle The behaviour of a function { at
physical scales above (resp. below) a certain scale R is almost
completely controlled by the behaviour of its Fourier transform ˆ{
at frequency scales below (resp. above) the dual scale 1=R and
vice versa, thanks to various mathematical manifestations15 of the
uncertainty principle.

(xiii) Stone/Gelfand duality A (locally compact Hausdorﬀ) topolog-
ical space X can be viewed in physical space (as a collection of
points), or dually, via the C  algebra C (X ) of continuous complex-
valued functions on that space, or (in the case when X is compact
and totally disconnected) via the boolean algebra of clopen sets (or
equivalently, the idempotents of C (X )). The fundamental connec-
tion between the two is given by the Stone representation theorem
(see [Ta2010, §2.3]) or the (commutative) Gelfand-Naimark theo-
rem (see [Ta2010, §1.10]).

In this section we will discuss one particular manifestation of duality,
namely the uncertainty principlethat describes the dual relationship be-
tween physical space and frequency space. There are various concrete for-
malisations of this principle, most famously the Heisenberg uncertainty prin-
ciple and the Hardy uncertainty principle(see [Ta2010, §2.6]) - but in many
situations, it is the heuristic formulation of the principle that is more useful
and insightful than any particular rigorous theorem that attempts to capture
that principle. Unfortunately, it is a bit tricky to formulate this heuristic
in a succinct way that covers all the various applications of that principle;
the Heisenberg inequality ∆§ · ∆∼& 1 is a good start, but it only captures
a portion of what the principle tells us. Consider for instance the following
(deliberately vague) statements, each of which can be viewed (heuristically,
at least) as a manifestation of the uncertainty principle:

15The Poisson summation formula can also be viewed as a variant of this principle, using
subgroups instead of scales.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

2.3. The uncertainty principle 165

(i) A function which is band-limited (restricted to low frequencies) is
featureless and smooth at ﬁne scales, but can be oscillatory (i.e.
containing plenty of cancellation) at coarse scales. Conversely, a
function which is smooth at ﬁne scales will be almost entirely re-
stricted to low frequencies.

(ii) A function which is restricted to high frequencies is oscillatory at
ﬁne scales, but is negligible at coarse scales. Conversely, a function
which is oscillatory at ﬁne scales will be almost entirely restricted
to high frequencies.

(iii) Projecting a function to low frequencies corresponds to averaging
out (or spreading out) that function at ﬁne scales, leaving only the
coarse scale behaviour.

(iv) Projecting a frequency to high frequencies corresponds to remov-
ing the averaged coarse scale behaviour, leaving only the ﬁne scale
oscillation.

(v) The number of degrees of freedom of a function is bounded by the
product of its spatial uncertainty and its frequency uncertainty (or
more generally, by the volume of the phase space uncertainty). In
particular, there are not enough degrees of freedom for a non-trivial
function to be simulatenously localised to both very ﬁne scales and
very low frequencies.

(vi) To control the coarse scale (or global) averaged behaviour of a func-
tion, one essentially only needs to know the low frequency compo-
nents of the function (and vice versa).

(vii) To control the ﬁne scale (or local) oscillation of a function, one only
needs to know the high frequency components of the function (and
vice versa).

(viii) Localising a function to a region of physical space will cause its
Fourier transform (or inverse Fourier transform) to resemble a plane
wave on every dual region of frequency space.

(ix) Averaging a function along certain spatial directions or at certain
scales will cause the Fourier transform to become localised to the
dual directions and scales. The smoother the averaging, the sharper
the localisation.

(x) The smoother a function is, the more rapidly decreasing its Fourier
transform (or inverse Fourier transform) is (and vice versa).

(xi) If a function is smooth or almost constant in certain directions
or at certain scales, then its Fourier transform (or inverse Fourier
transform) will decay away from the dual directions or beyond the
dual scales.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

166 2. Related articles

(xii) If a function has a singularity spanning certain directions or certain
scales, then its Fourier transform (or inverse Fourier transform) will
decay slowly along the dual directions or within the dual scales.

(xiii) Localisation operations in position approximately commute with
localisation operations in frequency so long as the product of the
spatial uncertainty and the frequency uncertainty is signiﬁcantly
larger than one.

(xiv) In the high frequency (or large scale) limit, position and frequency
asymptotically behave like a pair of classical observables, and par-
tial diﬀerential equations asymptotically behave like classical ordi-
nary diﬀerential equations. At lower frequencies (or ﬁner scales),
the former becomes a “quantum mechanical perturbation” of the
latter, with the strength of the quantum eﬀects increasing as one
moves to increasingly lower frequencies and ﬁner spatial scales.

(xv) Etc., etc.

(xvi) Almost all of the above statements generalise to other locally com-
pact abelian groups than R or R\ , in which the concept of a direc-
tion or scale is replaced by that of a subgroup or an approximate
subgroup
16.

All of the above (closely related) assertions can be viewed as being in-
stances of “the uncertainty principle”, but it seems diﬃcult to combine them
all into a single uniﬁed assertion, even at the heuristic level; they seem to be
better arranged as a cloud of tightly interconnected assertions, each of which
is reinforced by several of the others. The famous inequality ∆x  ∆˘ & 1 is
at the centre of this cloud, but is by no means the only aspect of it.

The uncertainty principle (as interpreted in the above broad sense) is one
of the most fundamental principles in harmonic analysis (and more speciﬁ-
cally, to the subﬁeld of time-frequency analysis), second only to the Fourier
inversion formula (and more generally, Plancherel's theorem) in importance;
understanding this principle is a key piece of intuition in the subject that
one has to internalise before one can really get to grips with this subject
(and also with closely related subjects, such as semi-classical analysis and
microlocal analysis). Like many fundamental results in mathematics, the
principle is not actually that diﬃcult to understand, once one sees how it
works; and when one needs to use it rigorously, it is usually not too diﬃcult
to improvise a suitable formalisation of the principle for the occasion. But,
given how vague this principle is, it is diﬃcult to present this principle in a

16In particular, as we will see below, the Poisson summation formula can be viewed as another
manifestation of the uncertainty principle.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

2.3. The uncertainty principle 167

traditional “theorem-proof-remark” manner. Here, we will give a set of in-
terrelated discussions about this principle rather than a linear development
of the theory, as this seemed to more closely align with the nature of this
principle.

The uncertainty principle gien here is associated only to classical (or
l⟩\ear) Fourier analysis. In principle, there should be uncertainty principles
for quadratic or higher order Fourier analysis, but we will not pursue such
questions here.

∈.3.∞. A\ ⟩\{ormal {ou\dat⟩o\ {or t⟨e u\⌋erta⟩\ty √r⟩\⌋⟩√le.Many
of the manifestations of the uncertainty principle can be heuristically derived
from the following informal heuristic:

Heur⟩st⟩⌋ ∈.3.∞(Phase heuristic).I{ t⟨e √⟨ase˚(x)o{ a ⌋om√le§ e§√o-
\e\t⟩ale2ˇi˚(x)u⌋tuates ⌊y less t⟨a\1 {orx ⟩\ some \⟩⌋e doma⟩\ Ω (e.}.
a ⌋o\ve§ set, or more }e\erally a\ a√√ro§⟩mate su⌊}rou√), t⟨e\ t⟨e √⟨ase
e2ˇi˚(x)⌊e⟨aves as ⟩{ ⟩t were ⌋o\sta\t o\Ω. I{ ⟩\stead t⟨e √⟨ase u⌋tuates
⌊y mu⌋⟨ more t⟨a\ 1, t⟨e\e2ˇi˚(x)s⟨ould os⌋⟩llate a\d e§⟨⟩⌊⟩t s⟩}\⟩⌋a\t
⌋a\⌋ellat⟩o\. T⟨e more t⟨e √⟨ase u⌋tuates, t⟨e more os⌋⟩llat⟩o\ a\d ⌋a\-
⌋ellat⟩o\ ⌊e⌋omes √rese\t.

For instance, according to this heuristic, on an interval [ R; R ] in the
real line, the linear phase x 7! e2ˇi˘x at a given frequency ˘ 2 R behaves like
a constant when j˘j ˝ 1=R, but oscillates signiﬁcantly when j˘j ˛ 1=R. This
is visually plausible if one graphs the real and imaginary parts cos(2ˇi˘x),
sin(2ˇi˘x). For now, we will take this principle as axiomatic, without further
justiﬁcation, and without further elaboration as to what vague terms such
as “behaves as if” or ˝ mean.

Remar∥ ∈.3.∈.The above heuristic can also be viewed as the informal
foundation for the √r⟩\⌋⟩√le o{ stat⟩o\ary √⟨ase. This is not coincidental,
but will not be the focus of the discussion here.

Let’s give a few examples to illustrate how this heuristic informally im-
plies some versions of the uncertainty principle. Suppose for instance that
a function f : R ! C is supported in an interval [ R; R ]. Now consider the
Fourier transform
17

ˆf (˘) := Z

∫ e
 2ˇix˘ f (x) dx = Z R

 R e
 2ˇix˘ f (x) dx:

We assume that the function is nice enough (e.g. absolutely integrable will
certainly suﬃce) that one can deﬁne the Fourier transform without diﬃculty.

17Other normalisations of the Fourier transform are also used in the literature, but the precise
choice of normalisation does not signiβcantly aαect the discussion here.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

168 2. Related articles

If |∼| ≪ 1=R, then the phase §∼ ﬂuctuates by less than 1 on the domain
§ ∈ [−R∅ R], and so the phase here is essentially constant by the above
heuristic; in particular, we expect the Fourier transform ˆ{(∼) to not vary
much in this interval. More generally, if we consider frequencies ∼ in an
interval |∼−∼0| ≪ 1=Rfor a ﬁxed ∼0, then on separating e 2ˇix˘ as e 2ˇix˘ 0 ×
e 2ˇix(˘  ˘ 0), the latter phase §(∼− ∼0) is essentially constant by the above
heuristic, and so we expect ˆ{(∼) to not vary much in this interval either.
Thus ˆ{(∼) is close to constant at scales much ﬁner than 1=R, just as the
uncertainty principle predicts.

A similar heuristic calculation using the Fourier inversion formula

{(§ ) = Z

∫ e2ˇix˘ ˆ{(∼) d∼

shows that if the Fourier transform ˆ{(∼) is restricted to an interval [−N∅ N],
then the function { should behave roughly like a constant at scales ≪ 1=N.
A bit more generally, if the Fourier transform is restricted to an interval [∼0−
N∅ ∼0+N], then by separating e2ˇix˘ as e2ˇix 0˘0 e2ˇi(x x 0)˘e2ˇix 0(˘ ˘ 0)e2ˇi(x x 0)(˘ ˘ 0)

and discarding the last phase when |§ − § 0| ≪ 1=N, we see that the function
{ behaves like a constant multiple of the plane wave § ↦→ e2ˇix˘ 0 on each
interval {§ : |§ − § 0| ≪ 1=N} (but it could be a diﬀerent constant multiple
on each such interval).

The same type of heuristic computation can be carried through in higher
dimensions. For instance, if a function { : Rn → C has Fourier transform
supported in some symmetric convex body Ω, then one expects { itself to
behave like a constant on any translate § 0+⌋Ω of a small multiple 0 < ⌋ ≪ 1
of the polar body
Ω
 := {§ ∈ R
n : |§ · ∼| ≤ 1 for all ∼∈ Ω}

of Ω.

An important special case where the above heuristics are in fact exactly
rigorous is when one does not work with approximate subgroupssuch as
intervals [−R∅ R] or convex bodies Ω, but rather with subgroups H of the
ambient (locally compact abelian) group G that is serving as physical space.
Here, of course, we need the general Fourier transform

ˆ{(∼) := Z

G e 2ˇi˘ x {(§) dG(§)∅

where G is a Haar measure on the locally compact abelian group G, where
∼: § ↦→ ∼· § is a continuous homomorphism from G to R=Z(and is thus an
element of the Pontryagin dual group ˆG), with Fourier transform given by

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

2.3. The uncertainty principle 169

the inversion formula
 {(§) = Z
ˆG e2πiξx ˆ{(∼)d ˆG(∼)

wheere ˆG is the dual Haar measure on ˆG (see e.g. my lecture notes for
further discussion of this general theory). If { is supported on a subgroup
H of G (this may require { to be a measure rather than a function, if H is a
measure zero subgroup of G), we conclude 18 (rigorously!) that ˆ{ is constant
along cosets of the orthgonal complement
ˆH := f∼ 2 ˆG : ∼ § = 0 for all § 2 Hg:

For instance, a measure { on R that is supported on Z will have a Fourier
transform ˆ{ that is constant along the Z direction, as Z is its own orthogonal
complement. This is a basic component of the Poisson summation formula.

Remark 2.3.3. Of course, in Euclidean domains such as R or Rn, basic
sets such as the intervals [ R∅ R ] are not actual subgroups, but are only
a√√roximate subgrou√s(roughly speaking, this means that they are closed
under addition a “reasonable fraction of the time”; for a precise deﬁnition,
see [TaVu2006 ]. However, there are dyadî modelsof Euclidean domains
(cf. [Ta2008, x1.6]), such as the ﬁeld F(( 1
t )) of formal Laurent series in
a variable 1
t over a ﬁnite ﬁeld F, in which the analogues of such intervals
arein fact actual subgroups, which allows for a very precise and rigorous
formalisation of many of the heuristics given here in that setting.

One can view an interval such as [ 1=R∅ 1=R] as being an approximate
orthogonal complement to the interval [ R∅ R ], and more generally the polar
body Ω as an approximate orthogonal complement to Ω. Conversely, the
uncertainty principle ∆§  ∆∼ ˛ 1 when specialised to subgroups H of a
ﬁnite abelian group G becomes the equality

jHj  jH ? j = jGj

and when specialised to subspaces V of a Euclidean space Rn becomes

dim(V ) + dim(V ? ) = dim(Rn):

We saw above that a function { that was restricted to a region Ω would
necessarily have a Fourier transform ˆ{ that was essentially constant on trans-
lates of (small multiples of) the dual region Ω . This implication can be
partially reversed. For instance, suppose that ˆ{ behaved like a constant at
all scales ˝ N. Then if one inspects the Fourier inversion formula

{(§) = Z

R ˆ{(∼)e2πixξ d∼

18This is assuming that f is a function or a measure. If f is merely a distribution, the
situation is more complicated.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

170 2. Related articles

we note that if |§| ≫ 1=N, then e2πixξ oscillates at scales ≪ N by the above
heuristic, and so {(§) should be negligible when |§| ≫ 1=N.

The above heuristic computations can be made rigorous in a number of
ways. One basic method is to exploit the fundamental fact that the Fourier
transform intertwines multiplication and convolution, thus19

[{ ∗ } = ˆ{ ˆ}

and c{ } = ˆ{ ∗ ˆ}

and similarly for the inverse Fourier transform. For instance, if a function
{ has Fourier transform supported on [−N∅ N], then we have

ˆ{ = ˆ{  N

where  N (§) :=  (§=N) and  is a smooth and compactly supported (or
rapidly decreasing) cutoﬀ function
20 that equals 1 on the interval [−1∅1].

Inverting the Fourier transform, we obtain the reproducing formula

{ = { ∗ ˇ N

where ˇ N is the inverse Fourier transform of  N . One can compute that

ˇ N (§) = N ˇ (N § )

and thus

(2.2) {(§) = Z

∫ {(§ + y
N ) ˇ (y ) dy:

If one chose  to be smooth and compactly supported (or at the very least,
a Schwartz function), ˇ will be in the Schwartz class. As such, (2.2) can
be viewed as an assertion that the value of the band-limited function { at
any given point § is essentially an average of its values at nearby points
§ + y
N for y = O(1). This formula can already be used to give many rigorous
instantiations of the uncertainty principle.

Remark 2.3.4.Another basic method to formalise the above heuristics,
particularly with regard to “oscillation causes cancellation”, is to use inte-
gration by parts.

19Here, the convolution  is with respect to either the Haar measure µG on the physical
space G, or the Haar measure µ ^G on the frequency space ˆG, as indicated by context.
20There is a lot of freedom here in what cutoﬀ function to pick, but in practice, “all bump
functions are usually equivalent”; unless one is optimising constants, needs a very speciﬁc and
delicate cancellation, or if one really, really needs a explicit formula, one usually does not have
to think too hard regarding what speciﬁc cutoﬀ to use, though smooth and well localised cutoﬀs
often tend to be superior to rough or slowly decaying cutoﬀs.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

2.3. The uncertainty principle 171

∈.3.∈. Pro|e⌋t⟩o\s.The restriction 1∪ΓN,N](X )f := f 1∪ΓN,N] of a func-
tion f : R ! C to an interval [ N; N ] is just the orthogonal projection (in
the Hilbert space L∈(R)) of f to the space of functions that are spatially
supported in [ N; N ]. Taking Fourier transforms (which, by Plancherel’s
theorem, preserves the Hilbert space L∈(R)), we see that the Fourier restric-
tion 1∪ΓN,N](D )f of f , deﬁned as

\1∪ΓN,N](D )f := ˆf 1∪ΓN,N]

is the orthogonal projection of f to those functions with Fourier support
in [ N; N ]. As discussed above, such functions are (heuristically) those
functions which are essentially constant at scales ˝ 1=N. As such, these
projection operators should behave like averaging operators at this scale.
This turns out not to be that accurate of a heuristic if one uses the sharp
cutoﬀs 1∪ΓN,N](though this does work perfectly in the dyadic model setting),
but if one replaces the sharp cutoﬀs by smoother ones, then this heuristic
can be justiﬁed by using convolutions as in the previous section; this leads
to Littlewood-∑aley theory, a cornerstone of the harmonic analysis of func-
tion spaces such as Sobolev spaces, and which are particularly important in
partial diﬀerential equations; see for instance [Ta∈00̸⌊, Appendix A] for
further discussion.

One can view the restriction operator 1∪ΓN,N](X ) as the spectral pro-
jection of the position operator Xf (x) := xf (x) to the interval [ N; N ];
in a similar vein, one can view 1∪ΓN,N](D ) as a spectral projection of the
diﬀerentiation operator Df (x) := ∞
∈πi d
dx f (x).

As before, one can work with other sets than intervals here. For instance,
restricting a function f : G ! C to a subgroup H causes the Fourier trans-
form ˆf to be averaged along the dual group ˆH . In particular, restricting
a function f : R ! C to the integers (and renormalising it to become the
measure P n2Z f (n)ﬃn) causes the Fourier transform ˆf : R ! C to become
summed over the dual group Z? = Z to become the function P m2Z ˆf ( +m).
In particular, the zero Fourier coeﬃcient of P n2Z f (n)ﬃn is P m2Z ˆf (m),
leading to the Poisson summation formula

X

n2Z f (n) = X

m2Z ˆf (m):

More generally, one has
 X

n2R Z f (n) = 1
R
 X

m2 ∞
R Z
 ˆf (m)

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

172 2. Related articles

for any R > 0, which can be viewed as a one-parameter family of identities
interpolating between the inversion formula

{(0) = Z

R ˆ{(∼) d∼

on one hand, and the forward Fourier transform formula
Z

R {(§) d§ = ˆ{(0)

on the other.

The duality ∆§  ∆∼˛ 1 between the position variable § and the fre-
quency variable ∼(or equivalently, between the position operator X and the
diﬀerentiation operator D) can be generalised to contexts in which the two
dual variables haved a diﬀerent “physical” interpretation than position and
frequency. One basic example of this is the duality ∆t ∆E ˛ 1 between a
time variable tand an energy variable E in quantum mechanics. Consider
a time-dependent Schr¨odinger equation

(2.3) ⟩@t = H ;  (0) =  0

for some Hermitian (and time-independent) spatial operator H on some
arbitrary domain (which does not need to be a Euclidean space Rn , or
even a group), where we have normalised away for now the role of Planck’s
constant ~. If the underlying spatial space L2(R) has an orthonormal basis
of eigenvector solutions to the time-independent Schr¨odinger equation

Huk = E k uk

then the solution to (2.3) is formally given by the formula

 = e itH  0 = X

k e iE k th 0∅ uk iuk :

We thus see that the coeﬃcients h 0∅ uk i (or more precisely, the eigenvectors
h 0∅ uk iuk ) can be viewed as the Fourier coeﬃcients of  in time, with the
energies E k playing the role of the frequency vector. Taking traces, one
(formally) sees a similar Fourier relationship between the trace function
tr(e itH ) and the spectrum E 1 < E 2 < E 3 < : : ::

(2.4) tr(e itH ) = X

k e iE k t:

As a consequence, the heuristics of the uncertainty principle carry through
here. Just as the behaviour of a function { at scales ˝ T largely controls the
spectral behaviour of ˆ{ at scales ˛ 1=T, one can use the evolution operator
e itH of the Schr¨odinger equation up to times jtj T to understand the

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

2.3. The uncertainty principle 173

spectrum E ∞< E ∈ < E 3 < : : :of H at scales ˛ 1=T. For instance, from
(2.4) we (formally) see that

tr(
Z

R ≡(t=T)eitE0 e(itH dt) =T X

k ˆ≡
θ E k Γ E 0
2≈=T
 

for any test function ≡ and any energy level E 0 . Roughly speaking, this
formula tells us that the number of eigenvalues in an interval of size O(1=T)
can be more or less controlled by the Schr¨odinger operators up to time T .

A similar analysis also holds for the solution operator

u(t) = cos(t
p Γ∆)u0 + sin(t
p Γ∆)
p Γ∆ u∞

for the wave equation
 @
∈
t u Γ ∆u = 0

on an arbitrary spatial Riemannian manifold M (which we will take to
be compact in order to have discrete spectrum). If we write ≥k for the
eigenvalues of p Γ∆ (so the Laplace-Beltrami operator ∆ has eigenvalues
Γ≥∈
k), then a similar analysis to the above shows that knowledge of the
solution to the wave equation up to time T gives (at least in principle)
knowledge of the spectrum averaged to at the scale 1=T or above.

From the ﬁnite speed of propagation property of the wave equation
(which has been normalised so that the speed of light ⌋ is equal to 1), one
only needs to know the geometry of the manifold M up to distance scales T
in order to understand the wave operator up to times T . In particular, if T
is less than the injectivity radius of M, then the topology and global geom-
etry of M is largely irrelevant, and the manifold more or less behaves like (a
suitably normalised version of) Euclidean space. As a consequence, one can
borrow Euclidean space techniques (such as the spatial Fourier transform)
to control the spectrum at coarse scales ˛ 1, leading in particular to the
Weyl law for the distribution of eigenvalues on this manifold; see for in-
stance [So1993] for a rigorous discussion. It is a signiﬁcant challenge to go
signiﬁcantly below this scale and understand the ﬁner structure of the spec-
trum; by the uncertainty principle, this task is largely equivalent to that of
understanding the wave equation on long time scales T ˛ 1, and the global
geometry of the manifold M (and in particular, the dynamical properties of
the geodesic ﬂow) must then inevitably play a more dominant role.

Another important uncertainty principle duality relationship is that be-
tween the (imaginary parts of the) zeroes ⊂ of the Riemann zeta function
(s) and the logarithms log √of the primes. Starting from the fundamental

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

174 2. Related articles

Euler product formula
 (s) = Y

p (1   √
 s )
 1

and using rigorous versions of the heuristic factorisation

(s) π Y

ˆ (s   ⊂)

one can soon derive explicit formulae connecting zeroes and primes, such as
X

ˆ
 1
s   ⊂ π   X

p log √e
 s logp

(see e.g. [Ta2010b, x1.8] for more discussion). Using such formulae, one
can relate the zeroes of the zeta function in the strip fIm(⊂)  T g with
the distribution of the log-primes at scales ˛ 1=T. For instance, knowing
that there are no zeroes on the line segment f1 + ⟩t: jtj T g is basically
equivalent to a partial prime number theorem ≈(§) = (1+ O( 1
T )) x
logx ; letting
T ω 1, we see that the full prime number theorem is equivalent to the
absence of zeroes on the entire line f1 + ⟩t: t2 Rg. More generally, there
is a fairly well-understood dictionary between the distribution of zeroes and
the distribution of primes, which is explored in just about any advanced text
in analytic number theory.

2.3.3. Phase space and the semi-classical limit. The above heuris-
tic description of Fourier projections such as 1[ N;N ](§) suggest that a
Fourier projection 1J (D) will approximately commute with a spatial projec-
tion 1I (X ) whenever I, J are intervals that obey the Heisenberg inequality
jIjjJj ˛ 1. Again, this heuristic is not quite accurate if one uses sharp
cutoﬀs (except in the dyadic model), but becomes quite valid if one uses
smooth cutoﬀs. As such, one can morally talk about phase space projec-
tions 1I J (X∅ D) π 1I (X )1J (D) π 1J (D)1I (X ) to rectangles I  J in phase
space, so long as these rectangles are large enough not to be in violation of
the uncertainty principle.

Heuristically, 1I J (X∅ D) is an orthogonal projection to the space21 of
functions that are localised to I in physical space and to J in frequency
space. One can approximately compute the dimension of this not-quite-
vector-space by computing the trace of the projection. Recalling that the
trace of an integral operator T { (§) := R

∫ K (§∅ y ){(y ) dy is given by tr T =

21This is morally a vector space, but unfortunately this is not rigorous due to the inability to
perfectly localise in both physical space and frequency space simultaneously, thanks to the Hardy
uncertainty principle.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

2.3. The uncertainty principle 175

R

R K(x; x), a short computation reveals that the trace of 1I (X )1J (D) is
Z

I ˇ1J (0) dx = jI jjJ j:

Thus we conclude that the phase space region I  J contains approximately
jI jjJj degrees of freedom in it, which can be viewed as a “macroscopic”
version of the uncertainty principle.

More generally, the number of degrees of freedom contained in a large
region Ω ˆ R  R of phase space is proportional to its area. Among other
things, this can be used to justify the Weyl law for the distribution of eigen-
values of various operators. For instance, if H is the Schr¨odinger operator

H =  ⃗ 2 d2

dx2 + V(x) = ⃗2D2 + V(X );

where ⃗ > 0 is a small constant (which physically can be interpreted as
Planck’s constant), and V is a conﬁning potential (to ensure discreteness
of the spectrum), then the spectral projection 1⋃ 1,E ](H ), when spectrally
projected to energy levels below a given threshold E, is morally like a phase
space projection to the region Ω := f(˘; x ) : ⃗2˘2+ V(x) ˇ Eg. As such, the
number of eigenvalues of H less than E should roughly equal the area of Ω,
particularly when ⃗ is small (so that Ω becomes large, and the uncertainty
principle no longer dominates); note that if V is a conﬁning potential (such
as the harmonic potential V(x) = jxj2) then Ω will have ﬁnite area. Such
heuristics can be justiﬁed by the machinery of semi-classical analysisand
the pseudo-diﬀerential calculus, which we will not detail here.

The correspondence principlein quantum mechanics asserts that in the
limit ⃗ ! 0, quantum mechanics asymptotically converges (in some suitable
sense) to classical mechanics. There are several ways to make this principle
precise. One can work in a dual formulation, using algebras of observables
rather than dealing with physical states directly, in which case the point is
that the non-commutative operator algebras of quantum observables con-
verge in various operator topologies to the commutative operator algebras
of classical observables in the limit ⃗ ! 0. This is the most common way
that the correspondence principle is formulated; but one can also work di-
rectly using states. We illustrate this with the time-dependent Schr¨odinger
equation

(2.5) i⃗@t  =   ⃗2

2m @xx  + V(x)

with a potential V, where m > 0 is a ﬁxed constant (representing mass) and
⃗ > 0 is a small constant, or equivalently

i⃗@t  = ⊆ P2

2m + V(X )

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

176 2. Related articles

where X is the position operator X{ (§) := §{ (§ ) and P is the momentum
operator P {(§) := −⟩~ d
dx {(§) (thus P = ⟩~D ). The classical counterpart to
this equation is Newton’s second law

F = ma;

where a = d2x
dt2 and F = −@xV (§); introducing the momentum √:= mv =
m dx
dt , one can rewrite Newton’s second law as Hamilton’s equations of motion

(2.6) @t√= −@xV (§); @t§ = 1
m √:

We now indicate (heuristically, at least) how (2.5) converges to (2.6) as
~ → 0. According to de Broglie’s law √= 2≈~∼ , the momentum √should
be proportional to the frequency ∼. Accordingly, consider a wave function
 that at time tis concentrated near position § 0(t) and momentum√0(t),
and thus near frequency √0(t)=(2≈~); heuristically one can view  as having
the shape
  (t∅ §) = A (
t∅
§ − § 0(t)
r
 ) eip0(t)x/~eiθ(t)/~

where ⊆(t) is some phase,ris some spatial scale (between 1 and ~) and A
is some amplitude function. Informally, we have X ≈ § 0(t) andP ≈ √0(t)
for  .

Before we analyse the equation (2.5), we ﬁrst look at some simpler equa-
tions. First, we look at ⟩~@ t = E
where E is a real scalar constant. Then the evolution of this equation is
given by a simple phase rotation:

 (t∅ §) = e iEt/~  (0∅ §):

This phase rotation does not change the location § 0(t) or momentum√0(t)
of the wave: @t§ 0(t) = 0; @t√0(t) = 0:
Next, we look at the transport equation

⟩~@ t = −⟩~v@ x

where v∈ R is another constant This evolution is given by translation:

 (t∅ §) =  (0∅ § − vt);

the position § 0(t) of this evolution moves at the constant speed of v, but
the momentum is unchanged:

@t§ 0(t) =v; @t√0(t) = 0:

Combining the two, we see that an equation of the form

⟩~@ t = E  − ⟩~v (@x − ⟩√0(t)=~)

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

2.3. The uncertainty principle 177

would also transport the position § 0 at a constant speed of v, without chang-
ing the momentum. Next, we consider the modulation equation

⟩~@ t = F §

where F 2 R is yet another constant. This equation is solved by the formula

 (t∅ §) = eitF x/~  (0∅ §);

this phase modulation does not change the position § 0 (t), but steadily in-
creases the momentum √0 (t) at a rate ofF:

@t§ 0 (t) = 0; @t√0 (t) =F:

Finally, we combine all these equations together, looking at the combined
equation
 ⟩~@ t = E    ⟩~v (@x   ⟩√0 (t)=~) + F(§   § 0 (t)) :

Heuristically at least, the position § 0 (t) and momentum√0 (t) of solutions
to this equation should evolve according to the law

(2.7) @t§ 0 (t) =v; @t√0 (t) =F:

Remark 2.3.5. One can make the above discussion more rigorous by using
the metaplectic representation.

The above analysis was for v∅ Fconstant, but as all statements here are
instantaneous and ﬁrst-order in time, it also applies for time-dependent v∅ F.

Now we return to the Schr¨odinger equation (2.5). If   is localised in
space close to § 0 (t), then by Taylor expansion we may linearise the V (§)
component as V (§) = V (§ 0 (t)) + (§  § 0 (t))@xV (§):

Similarly, if  is localised in momentum close to √0 (t), then in frequency it
is localised close to √0 (t)=(2≈~), so that @x ˇ ⟩√0 (t)=~, and so we have a
Taylor expansion

@xx ˇ (⟩√0 (t)=~)∈ + 2(⟩√0 (t)=~) (@x   (⟩√0 (t)=~)) :

These Taylor expansions become increasingly accurate in the limit ~ ! 0,
assuming suitable localisation in both space and momentum. Inserting these
approximations and simplifying, one arrives at

@t = E (t)
⟩~    √0 (t)
m (@x   (⟩√0 (t)=~))    ⟩
~ (§   § 0 (t))@xV (§ 0 (t))

where E (t) := p(t)2
∈m + V (§ 0 (t)) is the classical energy of the state. Using
the heuristics (2.7) we are led to (2.6) as desired.

More generally, a Schr¨odinger equation

⟩~@ t = H(X∅ P)

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

178 2. Related articles

where P := −⟩~ d
dx is the momentum operator, and being vague about ex-
actly what a function H(X∅ P) of two non-commuting operators X∅ P means,
can be (heuristically) approximately Taylor expanded as

⟩~@ t = H(§ 0(t)∅ √0(t))

+ @H
@√
H(§ 0(t)∅ √0(t))(P− √0(t))

+ @H
@§ H(§ 0(t)∅ √0(t))(X − § 0(t))

and (2.7) leads us to the Hamilton equations of motion

@t§(t) = @H
@√
; @t√(t) =− @H
@§ :

It turns out that these heuristic computations can be made completely rig-
orous in the semi-classical limit ~ → 0, by using the machinery of pseudo-
dierential calculus, but we will not detail this here.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

Bibliography

[AlBe2001] N. Alon, R. Beigel, Lower ⌊ou\ds {or a√√ro§⟩mat⟩o\s ⌊y low de}ree √oly\om⟩als
overZm , Proc. of the 16th Annual IEEE Conference on Computational Complexity
(CCC), IEEE, 2001, pp. 184-187.

[AlKaKrLiRo2003] N. Alon, T. Kaufman, M. Krivelevich, S. Litsyn, D. Ron, Test⟩\} low-
de}ree √oly\om⟩als over GF(∈), Approximation, randomization, and combinatorial
optimization, 188199, Lecture Notes in Comput. Sci., 2764, Springer, Berlin, 2003.

[BaKa2011] M. Bateman, N. Katz, New Bou\ds o\ ⌋a√ sets, preprint. arXiv.1101.5851

[Be1946] F. A. Behrend, O\ sets o{ ⟩\te}ers w⟨⟩⌋⟨ ⌋o\ta⟩\ \o t⟨ree terms ⟩\ ar⟩t⟨met⟩⌋al
√ro}ress⟩o\, Proc. Nat. Acad. Sci. U. S. A. 3∈ (1946), 331-332.

[BeCaChTa2008] J. Bennett, Jonathan; A. Carbery, M. Christ, T. Tao, T⟨e Bras⌋am√-
L⟩e⌊ ⟩\equal⟩t⟩es: \⟩te\ess, stru⌋ture a\d e§tremals, Geom. Funct. Anal. ∞↦ (2008),
no. 5, 1343-1415.

[BeHoKa2005] V. Bergelson, B. Host and B. Kra, Mult⟩√le re⌋urre\⌋e a\d \⟩lseque\⌋es,
with an appendix by Imre Ruzsa, Invent. Math. ∞̸0 (2005), no. 2, 261{303.

[BeTaZi2010] V. Bergelson, T. Tao, T. Ziegler, A\ ⟩\verse t⟨eorem {or t⟨e u\⟩{orm⟩ty
sem⟩\orms asso⌋⟩ated w⟩t⟨ t⟨e a⌋t⟩o\ o{Fp, Geom. Funct. Anal. ∞9(2010), no. 6,
1539-1596.

[BlLuRu1993] M. Blum, M. Luby, R. Rubinfeld, Sel{-test⟩\}/⌋orre⌋t⟩\} w⟩t⟨ a√√l⟩⌋at⟩o\s
to \umer⟩⌋al √ro⌊lems, Proceedings of the 22nd Annual ACM Symposium on Theory
of Computing (Baltimore, MD, 1990). J. Comput. System Sci. 4↦ (1993), no. 3, 549-
595.

[BoVi2010] A. Bogdanov, E. Viola, Pseudora\dom ⌊⟩ts {or √oly\om⟩als, SIAM J. Comput.
39 (2010), no. 6, 2464-2486.

[Bo1986] J. Bourgain, A Szemered⟩ ty√e t⟨eorem {or sets o{ √os⟩t⟩ve de\s⟩ty ⟩\Rk , Israel
J. Math. 54(1986), no. 3, 307-316.

[Bo1999] J. Bourgain, O\ tr⟩√les ⟩\ ar⟩t⟨met⟩⌋ √ro}ress⟩o\, Geom. Funct. Anal. 9 (1999),
no. 5, 968-984.

[Bo2008] J. Bourgain, Rot⟨'s t⟨eorem o\ √ro}ress⟩o\s rev⟩s⟩ted, J. Anal. Math. ∞04(2008),
155{192.
 179

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

180 Bibliography

∪BrGrTa∈0∞0] E. Breu⟩llard, B. Gree\, T. Tao,A√√ro§⟩mate su⌊}rou√s o{ l⟩\ear }rou√s,
Geom. Fu\⌋t. A\al.21 (∈0∞∞), \o. 4, ↦↦4-8∞9.

∪CaSz∈0∞0] O. Camare\a, B. Sze}edy,N⟩ls√a⌋es, \⟩lma\⟩{olds a\d t⟨e⟩r mor√⟨⟩sms,
√re√r⟩\t.arXiv.1009.3825

∪CoLe∞984] J.-P. Co\ze, E. Les⟩}\e,T⟨eoremes er}od⟩ques √our des mesures d⟩a}o\ales,
Bull. So⌋. Mat⟨. Fra\⌋e112 (∞984), ∞43{∞↦5.

∪El∈008] M. El∥⟩\,A\ Im√roved Co\stru⌋t⟩o\ o{ Pro}ress⟩o\-Free Sets, Israel J. Mat⟨.
184 (∈0∞∞), 93-∞∈8.

∪Fu∞9↦↦] H. Furste\⌊er},Er}od⟩⌋ ⌊e⟨av⟩or o{ d⟩a}o\al measures a\d a t⟨eorem o{ Sze-
mered⟩ o\ ar⟩t⟨met⟩⌋ √ro}ress⟩o\s, J. A\alyse Mat⟨.31 (∞9↦↦), ∈04{∈5̸.

∪Fu∞990] H. Furste\⌊er},No\⌋o\ve\t⟩o\al er}od⟩⌋ avera}es, T⟨e le}a⌋y o{ Jo⟨\ vo\ Neu-
ma\\ (Hem√stead, NY, ∞988), 43-5̸, Pro⌋. Sym√os. Pure Mat⟨., 50, Amer. Mat⟨.
So⌋., Prov⟩de\⌋e, RI, ∞990.

∪FuW⟩∞99̸] H. Furste\⌊er}, B. We⟩ss,A mea\ er}od⟩⌋ t⟨eorem {or
∞=N
P N
n= f (T
n x)g(T
n 2 x). Co\ver}e\⌋e ⟩\ er}od⟩⌋ t⟨eory a\d √ro⌊a⌊⟩l⟩ty (Colum-
⌊us, OH, ∞993), ∞93-∈∈↦, O⟨⟩o State U\⟩v. Mat⟨. Res. I\st. Pu⌊l., 5 de Gruyter,
Berl⟩\, ∞99̸.

∪GoY⟩P⟩∈008] D. Goldsto\, J. P⟩\tz, C. Yldrm,Pr⟩mes ⟩\ Tu√les II, A⌋ta Mat⟨.204
(∈0∞0), \o. ∞, ∞4↦.

∪Go∞998] W. T. Gowers,A \ew √roo{ o{ Szemered⟩'s t⟨eorem {or ar⟩t⟨met⟩⌋ √ro}ress⟩o\s
o{ le\}t⟨ {our, Geom. Fu\⌋t. A\al.8 (∞998), \o. 3, 5∈9-55∞.

∪Go∈00∞] W. T. Gowers,A \ew √roo{ o{ Szemered⟩'s t⟨eorem, Geom. Fu\⌋t. A\al.11
(∈00∞), \o. 3, 4̸5-588.

∪Go∈0∞0] W. T. Gowers,De⌋om√os⟩t⟩o\s, a√√ro§⟩mate stru⌋ture, tra\s{ere\⌋e, a\d t⟨e
Ha⟨\-Ba\a⌋⟨ t⟨eorem, Bull. Lo\d. Mat⟨. So⌋.42 (∈0∞0), \o. 4, 5↦3-̸0̸.

∪GoWo∈0∞0] W. T. Gowers, J. Wol{,T⟨e true ⌋om√le§⟩ty o{ a system o{ l⟩\ear equat⟩o\s,
Pro⌋. Lo\d. Mat⟨. So⌋. (3)100 (∈0∞0), \o. ∞, ∞55-∞↦̸.

∪GoWo∈0∞0⌊] W. T. Gowers, J. Wol{,L⟩\ear {orms a\d ⟨⟩}⟨er-de}ree u\⟩{orm⟩ty {or {u\⌋-
t⟩o\s o\ F
n
p , Geom. Fu\⌋t. A\al.21 (∈0∞∞), \o. ∞, 3̸-̸9.

∪GrRoS√∞980] R. Gra⟨am, B. Rot⟨s⌋⟨⟩ld, J.H. S√e\⌋er, Ramsey T⟨eory,Jo⟨\ W⟩ley a\d
So\s, NY (∞980).

∪Gr∈005] B. Gree\,Rot⟨'s t⟨eorem ⟩\ t⟨e √r⟩mes, A\\als o{ Mat⟨.161 (∈005), \o. 3,
∞̸09{∞̸3̸.

∪Gr∈005⌊] B. Gree\,A Szemered⟩-ty√e re}ular⟩ty lemma ⟩\ a⌊el⟩a\ }rou√s, w⟩t⟨ a√√l⟩⌋a-
t⟩o\s, Geom. Fu\⌋t. A\al.15 (∈005), \o. ∈, 340-3↦̸.

∪Gr∈005a] B. Gree\,F⟩\⟩te eld models ⟩\ add⟩t⟩ve ⌋om⌊⟩\ator⟩⌋s, Surveys ⟩\ ⌋om⌊⟩\a-
tor⟩⌋s ∈005, ∞∈↦, Lo\do\ Mat⟨. So⌋. Le⌋ture Note Ser., 3∈↦, Cam⌊r⟩d}e U\⟩v. Press,
Cam⌊r⟩d}e, ∈005.

∪Gr∈00↦] B. Gree\,Mo\treal le⌋ture \otes o\ quadrat⟩⌋ Four⟩er a\alys⟩s, Add⟩t⟩ve Com-
⌊⟩\ator⟩⌋s (Mo\treal ∈00̸, ed. Gra\v⟩lle et al.), CRM Pro⌋eed⟩\}s vol. 43, ̸9{∞0∈,
AMS ∈00↦.

∪GrKo∈009] B. Gree\, S. Ko\ya}⟩\,O\ t⟨e L⟩ttlewood √ro⌊lem modulo a √r⟩me, Ca\ad.
J. Mat⟨.61 (∈009), \o. ∞, ∞4∞-∞̸4.

∪GrTa∈00̸] B. Gree\, T. Tao,Restr⟩⌋t⟩o\ t⟨eory o{ t⟨e Sel⌊er} s⟩eve, w⟩t⟨ a√√l⟩⌋at⟩o\s, J.
T⟨. Nom⌊res Bordeau§18 (∈00̸), ∞3↦-∞↦∈

∪GrTa∈008] B. Gree\, T. Tao,A\ ⟩\verse t⟨eorem {or t⟨e GowersU3(G)\orm, Pro⌋.
Ed⟩\⌊. Mat⟨. So⌋. (∈)51 (∈008), \o. ∞, ↦3-∞53.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

Bibliography 181

∪GrTa∈008⌊] B. Gree\, T. Tao,T⟨e √r⟩mes ⌋o\ta⟩\ ar⌊⟩trar⟩ly lo\} ar⟩t⟨met⟩⌋ √ro}res-
s⟩o\s, A\\als o{ Mat⟨.167 (∈008), 48∞{54↦.

∪GrTa∈008⌋] B. Gree\, T. Tao,T⟨e M o⌊⟩us {u\⌋t⟩o\ ⟩s stro\}ly ort⟨o}o\al to \⟩lseque\⌋es,
√re√r⟩\t.arxiv.0807.1736

∪GrTa∈009] B. Gree\, T. Tao,T⟨e d⟩str⟩⌊ut⟩o\ o{ √oly\om⟩als over \⟩te elds, w⟩t⟨ a√-
√l⟩⌋at⟩o\s to t⟨e Gowers \orms, Co\tr⟩⌊. D⟩s⌋rete Mat⟨.4 (∈009), \o. ∈, ∞-3̸.

∪GrTa∈0∞0] B. Gree\, T. Tao,L⟩\ear equat⟩o\s ⟩\ √r⟩mes, A\\als o{ Mat⟨.171 (∈0∞0),
∞↦53{∞850.

∪GrTa∈0∞0⌊] B. Gree\, T. Tao,A\ ar⟩t⟨met⟩⌋ re}ular⟩ty lemma, a\ asso⌋⟩ated ⌋ou\t⟩\}
lemma, a\d a√√l⟩⌋at⟩o\s, A\ Irre}ular M⟩\d: Szemered⟩ ⟩s ↦0, Bolya⟩ So⌋⟩ety Mat⟨e-
mat⟩⌋al Stud⟩es, ∈0∞0.

∪GrTa∈0∞∞] B. Gree\, T. Tao,T⟨e qua\t⟩tat⟩ve ⌊e⟨av⟩our o{ √oly\om⟩al or⌊⟩ts o\ \⟩lma\-
⟩{olds, √re√r⟩\t.arXiv.0709.3562

∪GrTaZ⟩∈009] B. Gree\, T. Tao, T. Z⟩e}ler,A\ ⟩\verse t⟨eorem {or t⟨e GowersU4∪N]
\orm, √re√r⟩\t.arXiv.0911.5681

∪GrTaZ⟩∈0∞0] B. Gree\, T. Tao, T. Z⟩e}ler,A\ ⟩\verse t⟨eorem {or t⟨e GowersUs+1 ∪N]-
\orm (A\\ou\⌋eme\t), Ele⌋tro\. Res. A\\ou\⌋. Mat⟨. S⌋⟩.18 (∈0∞∞), ̸9-90.

∪GrTaZ⟩∈0∞0⌊] B. Gree\, T. Tao, T. Z⟩e}ler,A\ ⟩\verse t⟨eorem {or t⟨e GowersUs+1 ∪N]-
\orm, √re√r⟩\t.arXiv.1009.3998

∪GrWo∈008] B. Gree\, J. Wol{,A \ote o\ El∥⟩\'s ⟩m√roveme\t o{ Be⟨re\d's ⌋o\stru⌋t⟩o\,
Add⟩t⟩ve \um⌊er t⟨eory, ∞4∞∞44, S√r⟩\}er, New Yor∥, ∈0∞0.

∪Gr∞9̸∞] L. W. Gree\,S√e⌋tra o{ \⟩lows,Bull. Amer. Mat⟨. So⌋.67 (∞9̸∞) 4∞4{4∞5.

∪Gr∞98∞] M. Gromov,Grou√s o{ √oly\om⟩al }rowt⟨ a\d e§√a\d⟩\} ma√s, I\st. Hautes
Etudes S⌋⟩. Pu⌊l. Mat⟨. No.53 (∞98∞), 53{↦3.

∪Ha∞993] I. J. Hala\d,U\⟩{orm d⟩str⟩⌊ut⟩o\ o{ }e\eral⟩zed √oly\om⟩als, J. Num⌊er T⟨eory
45 (∞993), 3∈↦{3̸̸.

∪HaS⟨∈0∞0] E. Haramaty, A. S⟨√⟩l∥a,O\ t⟨e stru⌋ture o{ ⌋u⌊⟩⌋ a\d quart⟩⌋ √oly\om⟩-
als, STOC'∞0Pro⌋eed⟩\}s o{ t⟨e ∈0∞0 ACM I\ter\at⟩o\al Sym√os⟩um o\ T⟨eory o{
Com√ut⟩\}, 33∞340, ACM, New Yor∥, ∈0∞0.

∪HaLo∈0∞0] H. Hatam⟩, S. Lovett,H⟩}⟨er-order Four⟩er a\alys⟩s o{F
n
p a\d t⟨e ⌋om√le§⟩ty
o{ systems o{ l⟩\ear {orms, Geom. Fu\⌋t. A\al.21 (∈0∞∞), \o. ̸, ∞33∞-∞35↦.

∪HB∞98↦] D. R. Heat⟨-Brow\,I\te}er sets ⌋o\ta⟩\⟩\} \o ar⟩t⟨met⟩⌋ √ro}ress⟩o\s, J. Lo\-
do\ Mat⟨. So⌋. (∈)35 (∞98↦), \o. 3, 385-394.

∪Ho∈00̸] B. Host,Pro}ress⟩o\s ar⟩t⟨met⟩ques da\s les \om⌊res √rem⟩ers (d'a√res B.
Gree\ et T. Tao)Sem⟩\a⟩re Bour⌊a∥⟩. Vol. ∈004/∈005. Astr⟩sque No. 30↦ (∈00̸),
E§√. No. 944, v⟩⟩⟩, ∈∈9-∈4̸.

∪HoKr∈005] B. Host, B. Kra,No\⌋o\ve\t⟩o\al er}od⟩⌋ avera}es a\d \⟩lma\⟩{olds, A\\. o{
Mat⟨. (∈)161 (∈005), \o. ∞, 39↦-488.

∪IwKo∈004] H. Iwa\⟩e⌋, E. Kowals∥⟩, A\alyt⟩⌋ \um⌊er t⟨eory. Amer⟩⌋a\ Mat⟨emat⟩⌋al
So⌋⟩ety Colloqu⟩um Pu⌊l⟩⌋at⟩o\s, 53. Amer⟩⌋a\ Mat⟨emat⟩⌋al So⌋⟩ety, Prov⟩de\⌋e,
RI, ∈004.

∪KaLo∈008] T. Kau{ma\, S. Lovett,Worst Case to Avera}e Case Redu⌋t⟩o\s {or Poly\o-
m⟩als, FOCS (∈008) ∞̸̸{∞↦5.

∪Kl∞9↦∞] S. L. Kle⟩ma\,Les t⟨eor⊆emes de \⟩tude √our le {o\⌋teur de P⟩⌋ard, ⟩\T⟨eor⟩e
des ⟩\terse⌋t⟩o\s et t⟨eor⊆eme de R⟩ema\\-Ro⌋⟨(SGA̸), e§√ose XIII, √√.̸∞̸{̸̸̸.
LNM ∈∈5, S√r⟩\}er-Verla}, Berl⟩\-New Yor∥, ∞9↦∞.

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

182 Bibliography

∪KoLuRo∞99̸] Y. Ko⟨aya∥awa, T. Lu⌋zsa∥, V. R odl,Ar⟩t⟨met⟩⌋ √ro}ress⟩o\s o{ le\}t⟨
t⟨ree ⟩\ su⌊sets o{ a ra\dom set, A⌋ta Ar⟩t⟨.75 (∞99̸), \o. ∈, ∞33{∞̸3.
∪Kr∈00̸] B. Kra,From ⌋om⌊⟩\ator⟩⌋s to er}od⟩⌋ t⟨eory a\d ⌊a⌋∥ a}a⟩\, I\ter\at⟩o\al Co\-
}ress o{ Mat⟨emat⟩⌋⟩a\s. Vol. III, 5↦↦̸, Eur. Mat⟨. So⌋., Zr⟩⌋⟨, ∈00̸.
∪Kr∈00↦] B. Kra,Er}od⟩⌋ met⟨ods ⟩\ add⟩t⟩ve ⌋om⌊⟩\ator⟩⌋s, Add⟩t⟩ve ⌋om⌊⟩\ator⟩⌋s, ∞03-
∞43, CRM Pro⌋. Le⌋ture Notes, 43, Amer. Mat⟨. So⌋., Prov⟩de\⌋e, RI, ∈00↦.
∪La∞954] M. Lazard,Sur les }rou√es \⟩l√ote\ts et les a\\eau§ de L⟩e, A\\. S⌋⟩. E⌋ole
Norm. Su√. (3)71 (∞954), ∞0∞-∞90
∪Le∞998] A. Le⟩⌊ma\,Poly\om⟩al seque\⌋es ⟩\ }rou√s, Jour\al o{ Al}e⌊ra ∈0∞ (∞998),
∞89{∈0̸.
∪Le∈00∈] A. Le⟩⌊ma\,Poly\om⟩al ma√√⟩\}s o{ }rou√s,Israel J. Mat⟨.129 (∈00∈), ∈9{̸0.
∪Le∈005] A. Le⟩⌊ma\,Po⟩\tw⟩se ⌋o\ver}e\⌋e o{ er}od⟩⌋ avera}es o{ √oly\om⟩al seque\⌋es
o{ tra\slat⟩o\s o\ a \⟩lma\⟩{old, Er}od⟩⌋ T⟨eory a\d Dy\am⟩⌋al Systems 25 (∈005),
\o. ∞, ∈0∞{∈∞3.
∪Lo∞9↦5] P. A. Loe⌊,Co\vers⟩o\ {rom \o\sta\dard to sta\dard measure s√a⌋es a\d a√-
√l⟩⌋at⟩o\s ⟩\ √ro⌊a⌊⟩l⟩ty t⟨eory, Tra\s. Amer. Mat⟨. So⌋.211 (∞9↦5), √√. ∞∞3{∞∈∈.
∪LoMeSa∈008] S. Lovett, R. Mes⟨ulam, A. Samorod\⟩ts∥y,I\verse ⌋o\|e⌋ture {or t⟨e Gow-
ers \orm ⟩s {alse, STOC'08, 54↦-55̸, ACM, New Yor∥, ∈008.
∪Ma∞949] A. Mal'⌋ev,O\ a ⌋lass o{ ⟨omo}e\eous s√a⌋es , Izvest⟩ya A∥ad. Nau∥ SSSR, Ser
Mat.13 (∞949), 9{3∈.
∪Me∞995] R. Mes⟨ulam,O\ su⌊sets o{ \⟩te a⌊el⟩a\ }rou√s w⟩t⟨ \o 3-term ar⟩t⟨met⟩⌋
√ro}ress⟩o\s, J. Com⌊⟩\. T⟨eory Ser. A71 (∞995), \o. ∞, ∞̸8-∞↦∈.
∪Mu∞9↦0] D. Mum{ord,Var⟩et⟩es de\ed ⌊y quadrat⟩⌋ equat⟩o\s, ∞9↦0 Quest⟩o\s o\ Al}e-
⌊ra⟩⌋ Var⟩et⟩es (C.I.M.E., III C⟩⌋lo, Vare\\a, ∞9̸9) √√. ∈9{∞00 Ed⟩z⟩o\⟩ Cremo\ese,
Rome.
∪Pa∞9↦0] W. Parry,Dy\am⟩⌋al systems o\ \⟩lma\⟩{olds, Bull. Lo\do\ Mat⟨. So⌋.2 (∞9↦0)
3↦{40.
∪ReTrTuVa∈008] O. Re⟩\}old, L. Trev⟩sa\, M. Tuls⟩a\⟩, S. Vad⟨a\,New Proo{s o{ t⟨e
Gree\-Tao-Z⟩e}ler De\se Model T⟨eorem: A\ E§√os⟩t⟩o\, √re√r⟩\t.arXiv.0806.0381
∪Ro∞953] K.F. Rot⟨,O\ ⌋erta⟩\ sets o{ ⟩\te}ers, J. Lo\do\ Mat⟨. So⌋.28 (∞953), ∈45-∈5∈.
∪Sa∈00↦] A. Samorod\⟩ts∥y,Low-de}ree tests at lar}e d⟩sta\⌋es, STOC'0↦Pro⌋eed⟩\}s o{
t⟨e 39t⟨ A\\ual ACM Sym√os⟩um o\ T⟨eory o{ Com√ut⟩\}, 50̸5∞5, ACM, New
Yor∥, ∈00↦.
∪Sa∈0∞0] T. Sa\ders,O\ ⌋erta⟩\ ot⟨er sets o{ ⟩\te}ers, J. A\al. Mat⟨., to a√√ear,
arX⟩v:∞00↦.5444, ∈0∞0.
∪Sa∈0∞0] T. Sa\ders,O\ Rot⟨'s t⟨eorem o\ √ro}ress⟩o\s, √re√r⟩\t.
∪S⟨∈009] Y. S⟨alom, T. Tao,A \⟩tary vers⟩o\ o{ Gromov's √oly\om⟩al }rowt⟨ t⟨eorem,
Geom. Fu\⌋t. A\al. ∈0 (∈0∞0), \o. ̸, ∞50∈-∞54↦.
∪So∞993] C. So}}e, Four⟩er ⟩\te}rals ⟩\ ⌋lass⟩⌋al a\alys⟩s. Cam⌊r⟩d}e Tra⌋ts ⟩\ Mat⟨emat-
⟩⌋s, ∞05. Cam⌊r⟩d}e U\⟩vers⟩ty Press, Cam⌊r⟩d}e, ∞993.
∪SuTrVa∞999] M. Suda\, L. Trev⟩sa\, S. Vad⟨a\,Pseudora\dom }e\erators w⟩t⟨out t⟨e
XOR lemma, A\\ual ACM Sym√os⟩um o\ T⟨eory o{ Com√ut⟩\} (Atla\ta, GA, ∞999),
53↦54̸ (ele⌋tro\⟩⌋), ACM, New Yor∥, ∞999.
∪Sz∈009] B. Sze}edy, H⟩}⟨er order Four⟩er a\alys⟩s as a\ al}e⌊ra⟩⌋ t⟨eory I, √re√r⟩\t.
arXiv.0903.0897
∪Sz∈009⌊] B. Sze}edy, H⟩}⟨er order Four⟩er a\alys⟩s as a\ al}e⌊ra⟩⌋ t⟨eory II, √re√r⟩\t.
arXiv.0911.1157

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

Bibliography 183

∪Sz∈0∞0] B. Sze}edy,H⟩}⟨er order Four⟩er a\alys⟩s as a\ al}e⌊ra⟩⌋ t⟨eory III, √re√r⟩\t.
arXiv:1001.4282

∪Sz∈0∞0⌊] B. Sze}edy,Gowers \orms, re}ular⟩zat⟩o\ a\d l⟩m⟩ts o{ {u\⌋t⟩o\s o\ a⌊el⟩a\
}rou√s, √re√r⟩\t.arXiv:1010.6211

∪Sz∈0∞0⌋] B. Sze}edy,Stru⌋ture o{ \⟩te \⟩ls√a⌋es a\d ⟩\verse t⟨eorems {or t⟨e Gowers
\orms ⟩\ ⌊ou\ded e§√o\e\t }rou√s, √re√r⟩\t.arXiv:1011.1057

∪Sz∞9↦5] E. Szemered⟩,O\ sets o{ ⟩\te}ers ⌋o\ta⟩\⟩\} \ok eleme\ts ⟩\ ar⟩t⟨met⟩⌋ √ro-
}ress⟩o\, A⌋ta Ar⟩t⟨.27 (∞9↦5), ∈99{345.

∪Sz∞9↦8] E. Szemered⟩,Re}ular √art⟩t⟩o\s o{ }ra√⟨s, ⟩\ ∩Pro⌊lemes Com⌊⟩\ato⟩res et
T⟨eor⟩e des Gra√⟨es, Pro⌋. Colloque I\ter. CNRS," (Bermo\d, Four\⟩er, Las Ver}\as,
Sotteau, eds.), CNRS Par⟩s, ∞9↦8, 399{40∞.

∪Ta∈003] T. Tao,Re⌋e\t √ro}ress o\ t⟨e Restr⟩⌋t⟩o\ ⌋o\|e⌋ture, √re√r⟩\t.math.CA/0311181

∪Ta∈004] T. Tao,A remar∥ o\ Goldsto\-Yldrm ⌋orrelat⟩o\ est⟩mates, u\√u⌊l⟩s⟨ed.
www.math.ucla.edu/˘tao/preprints/Expository/gy-corr.dvi

∪Ta∈00̸] T. Tao,Szemered⟩'s re}ular⟩ty lemma rev⟩s⟩ted, Co\tr⟩⌊. D⟩s⌋rete Mat⟨.1 (∈00̸),
\o. ∞, 8-∈8.

∪Ta∈00̸⌊] T. Tao, No\l⟩\ear d⟩s√ers⟩ve equat⟩o\s: lo⌋al a\d }lo⌊al a\alys⟩s, CBMS re-
}⟩o\al ser⟩es ⟩\ mat⟨emat⟩⌋s, ∈00̸.

∪Ta∈00↦] T. Tao,Stru⌋ture a\d ra\dom\ess ⟩\ ⌋om⌊⟩\ator⟩⌋s, Pro⌋eed⟩\}s o{ t⟨e 48t⟨
a\\ual sym√os⟩um o\ Fou\dat⟩o\s o{ Com√uter S⌋⟩e\⌋e (FOCS) ∈00↦, 3{∞8.

∪Ta∈008] T. Tao, Stru⌋ture a\d Ra\dom\ess, Amer⟩⌋a\ Mat⟨emat⟩⌋al So⌋⟩ety, ∈008.

∪Ta∈009] T. Tao, Po⟩\⌋are's le}a⌋⟩es, Vol. I., Amer⟩⌋a\ Mat⟨emat⟩⌋al So⌋⟩ety, ∈009.

∪Ta∈0∞0] T. Tao, A\ e√s⟩lo\ o{ room, Vol. I., Graduate Stud⟩es ⟩\ Mat⟨emat⟩⌋s, ∞∞↦.
Amer⟩⌋a\ Mat⟨emat⟩⌋al So⌋⟩ety, Prov⟩de\⌋e, RI, ∈0∞0.

∪Ta∈0∞0⌊] T. Tao, A\ e√s⟩lo\ o{ room, Vol. II., Amer⟩⌋a\ Mat⟨emat⟩⌋al So⌋⟩ety, ∈0∞0.

∪Ta∈0∞∞] T. Tao, A\ ⟩\trodu⌋t⟩o\ to measure t⟨eory, Amer⟩⌋a\ Mat⟨emat⟩⌋al So⌋⟩ety,
∈0∞∞.

∪Ta∈0∞∞⌊] T. Tao, To√⟩⌋s ⟩\ ra\dom matr⟩§ t⟨eory, Amer⟩⌋a\ Mat⟨emat⟩⌋al So⌋⟩ety, ∈0∞∞.

∪TaVu∈00̸] T. Tao, V. Vu, Add⟩t⟩ve ⌋om⌊⟩\ator⟩⌋s. Cam⌊r⟩d}e Stud⟩es ⟩\ Adva\⌋ed
Mat⟨emat⟩⌋s, ∞05. Cam⌊r⟩d}e U\⟩vers⟩ty Press, Cam⌊r⟩d}e, ∈00̸.

∪TaZ⟩∈008] T. Tao, T. Z⟩e}ler,T⟨e √r⟩mes ⌋o\ta⟩\ ar⌊⟩trar⟩ly lo\} √oly\om⟩al √ro}ress⟩o\s,
A⌋ta Mat⟨.201 (∈008), ∈∞3-305.

∪TaZ⟩∈0∞0] T. Tao, T. Z⟩e}ler,T⟨e ⟩\verse ⌋o\|e⌋ture {or t⟨e Gowers \orm over \⟩te
elds v⟩a t⟨e ⌋orres√o\de\⌋e √r⟩\⌋⟩√le, A\al. PDE3 (∈0∞0), \o. ∞, ∞-∈0.

∪TaZ⟩∈0∞∞] T. Tao, T. Z⟩e}ler,T⟨e ⟩\verse ⌋o\|e⌋ture {or t⟨e Gowers \orm over \⟩te
elds ⟩\ low ⌋⟨ara⌋ter⟩st⟩⌋, √re√r⟩\t.arXiv:1101.1469

∪Wo] J. Wol{,T⟨e m⟩\⟩mum \um⌊er o{ mo\o⌋⟨romat⟩⌋ 4-term √ro}ress⟩o\s,
www.juliawolf.org/research/preprints/talk280509.pdf

∪Z⟩∈00↦] T. Z⟩e}ler,U\⟩versal ⌋⟨ara⌋ter⟩st⟩⌋ {a⌋tors a\d Furste\⌊er} avera}es, J. Amer.
Mat⟨. So⌋. ∈0 (∈00↦), \o. ∞, 53-9↦.

Author's preliminary version made available with permission of the publisher, the American Mathematical SocietyAuthor's preliminary version made available with permission of the publisher, the American Mathematical Society

Index

2-coboundary, 78
99% inverse theorem for the Gowers
norms, 74
W -trick, 123
◦-equidistribution, 12
 Los’s theorem, 20

additive cohomology, 76
additive quadruple, 83
algebraic set, 138
algebraic variety, 142
almost periodicity, 40
analytic rank, 72
arithmetic regularity lemma (strong),
38
arithmetic regularity lemma (weak), 38
asymptotic equidistribution, 3, 10
asymptotic notation, 3
asymptotic notation (ultralimit
analysis), 21
atom, 33

Balog-Szemer´edi-Gowers-Freiman
theorem, 84
Bezout’s theorem, 141
bias, 64
Bogdanov-Viola lemma, 66
Bohr set, 115
bounded (ultralimit analysis), 21
bracket polynomial, 101

Cauchy-Schwarz complexity, 55
Cauchy-Schwarz inequality, 149
 Cauchy-Schwarz-Gowers inequality, 58,
157
characteristic, 55
Chevalley-Warning theorem, 63
classical polynomial, 61
cocycle, 77
complex conjugation, 151
complexity of a nilmanifold, 101
complexity of a nilsequence, 102
complexity of an algebraic set, 139
conditional expectation, 33
continuity of dimension, 140
continuity of irreducibility, 143
converse inverse theorem for the Gowers
norms, 75
correlation condition, 121
correspondence principle, 175

de Broglie’s law, 176
degree, 94
dense model theorem, 111, 120
density increment argument, 28
diﬀerentiation of nilsequences, 104
dimension, 140
Dirac measure, 3

energy increment argument, 33
equidistribution, 62
Equidistribution (abelian linear
sequences), 7
Equidistribution (abelian
multidimensional polynomial
sequences), 11
 ∞85

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

186 Index

Equ⟩d⟩str⟩⌊ut⟩o\ (a⌊el⟩a\ √oly\om⟩al
seque\⌋es), 9, ∞↦, ∈4
equ⟩d⟩str⟩⌊ut⟩o\ (ultral⟩m⟩t a\alys⟩s), ∈∈
equ⟩d⟩str⟩⌊ut⟩o\ t⟨eorem, ̸
error ⌋orre⌋t⟩o\ o{ √oly\om⟩als, ̸↦
e§√o\e\t⟩al sum, ∈

{a⌋tor, 33
Fe|er summat⟩o\, ∞3
ltered }rou√, 94
ltrat⟩o\, 93
Four⟩er measura⌊⟩l⟩ty, 35
Four⟩er √seudora\dom\ess, 48
{ra}me\tat⟩o\, 3∞

}e\eral⟩sed vo\ Neuma\\ ⟩\equal⟩ty, 59
}e\eral⟩sed vo\ Neuma\\ t⟨eorem, ∞∞8
Gowers ⌊o§ s√a⌋e, ∞54
Gowers ⟩\\er √rodu⌋t, 5↦, ∞54
Gowers tr⟩a\}le ⟩\equal⟩ty, ∞5↦
Gowers u\⟩{orm⟩ty \orm, 4↦, 5↦, ∞53
Gowers' Cau⌋⟨y-S⌋⟨warz ar}ume\t, 83
Gowers-Host-Kra sem⟩\orm, ∞55
Gowers-Wol{ t⟨eorem, 9∈
Gromov's t⟨eorem, ∞45
}rowt⟨ s√urt, ∞9

Haar measure, 5
Hall-Petres⌋o {ormula, 98
Ham⟩lto\'s equat⟩o\ o{ mot⟩o\, ∞↦̸
Hardy-L⟩ttlewood ma§⟩mal ⟩\equal⟩ty,
3̸
He⟩se\⌊er} }rou√, 98
He⟩se\⌊er} \⟩lma\⟩{old, ∞00
H⟩}⟨er order ⟩\\er √rodu⌋t s√a⌋e., ∞53
H⟩l⌊ert ⌋u⌊e lemma, 4↦
H⟩l⌊ert s√a⌋e, ∞50
⟨or⟩zo\tal ⌋⟨ara⌋ter, ∞08
⟨or⟩zo\tal torus, ∞08
Host-Kra }rou√, 93, 94
Host-Kra measure, ∞55
⟨y√erreal, ∞35

⟩\d⟩⌋ator {u\⌋t⟩o\, ∈
⟩\\⟩tes⟩mal, ∈∞, ∞38
⟩\\er √rodu⌋t s√a⌋e, ∞49
⟩\verse ⌋o\|e⌋ture {or t⟨e Gowers \orm,
58, ∞05
⟩\verse ⌋o\|e⌋ture {or t⟨e Gowers
u\⟩{orm⟩ty \orms, ↦5
⟩rrat⟩o\al, ̸

|o⟩\, 34
 Kro\e⌋∥er {a⌋tor, 4∈
Kro\e⌋∥er measura⌊⟩l⟩ty, 4∈

Lazard-Le⟩⌊ma\ t⟨eorem, 9̸
L⟩e⌊ma\ equ⟩d⟩str⟩⌊ut⟩o\ ⌋r⟩ter⟩o\, ∞08
l⟩m⟩t \⟩te set, ∈0
l⟩m⟩t {u\⌋t⟩o\, ∈∞
l⟩m⟩t \um⌊er, ∈0
l⟩m⟩t o⌊|e⌋t, ∞34
l⟩m⟩t set, ∈0
l⟩\ear {orms ⌋o\d⟩t⟩o\s, ∞∞8
l⟩\ear √⟨ase, ∈
L⟩√s⌋⟨⟩tz \orm, ∞∞
L⟩ttlewood-Paley t⟨eory, ∞↦∞
lo⌋al Gowers ⟩\\er √rodu⌋t, ∞̸0
lo⌋al testa⌊⟩l⟩ty, ↦9
Loe⌊ measure, 4∞
low ra\∥, ̸5
lower ⌋e\tral ser⟩es, 94
lower {a⌋e, 95
Lu⌋as' t⟨eorem, 80

Mal'⌋ev ⌊as⟩s, 99
mult⟩√le re⌋urre\⌋e, ∞9

Newto\'s se⌋o\d law, ∞↦̸
\⟩l√ote\t, 98
Noet⟨er⟩a\ ⌋o\d⟩t⟩o\, ∞4∈
\o\√r⟩\⌋⟩√al ultralter, ∞33
\orm, ∞50

√⟨ase ⟨eur⟩st⟩⌋, ∞̸↦
√olyar ⌊ody, ∞̸8
√oly\om⟩al, 54, ̸0
√oly\om⟩al or⌊⟩t, ∞0∞
√oly\om⟩al √⟨ase ⟩\var⟩a\⌋e, 58
√oly\om⟩al re⌋urre\⌋e, 9
√oly\om⟩al seque\⌋e, 98
Po\trya}⟩\ dual, 5↦

Ramsey's t⟨eorem, 80
re⌋urre\⌋e, ∞9
re\eme\t, 34
re}ular⟩ty lemma {or √oly\om⟩als, ↦∞
relat⟩ve va\ der Cor√ut lemma, ∞0↦
re√rodu⌋⟩\} {ormula, ∞↦0
restr⟩⌋t⟩o\ est⟩mate, ∞∞4
r⟩}⟩d⟩ty, ̸↦
Rot⟨'s t⟨eorem, ∉, 33, ∞∞∞
Rot⟨'s t⟨eorem ⟩\ t⟨e √r⟩mes, ∞09
Rot⟨-√seudora\dom, ∞∞∈

S⌋⟨r od⟩\}er equat⟩o\, ∞↦∈, ∞↦5

Author's preliminary version made available with permission of the publisher, the American Mathematical Society

Index 187

sem⟩-\orm, ∞50
s√l⟩tt⟩\} a§⟩om, ∞53
sta\dard, ∈0
sta\dard √art, ∈∞, ∞38
sta\dard u\⟩verse, ∞3∞
stro\} ar⟩t⟨met⟩⌋ re}ular⟩ty lemma, 9∞
stru⌋ture a\d ra\dom\ess, 34
su√erstru⌋ture, ∞3∞
symmetr⟩⌋ √oly\om⟩al, 80
sy\det⟩⌋⟩ty, ∞9

Taylor ⌋oe◦⌋⟩e\t, 98
te\sor √rodu⌋t, ∞5∞
total asym√tot⟩⌋ equ⟩d⟩str⟩⌊ut⟩o\, 4, ∞0
total equ⟩d⟩str⟩⌊ut⟩o\ (ultral⟩m⟩t
a\alys⟩s), ∈∈
tra\s{ere\⌋e, ∞09
tr⟩a\}le ⟩\equal⟩ty, ∞49

ultral⟩m⟩t, ∈0, ∈∞, ∞34
ultra√ower, ∈0, ∞34
ultra√rodu⌋t, ∈0, ∞34

va\ der Cor√ut ⟩\equal⟩ty, ↦
va\ der Cor√ut lemma, 8, ∞∞, ∈4, ̸5
vert⟩⌋al ⌋⟨ara⌋ter, ∞03
vert⟩⌋al {reque\⌋y, ∞03
V⟩\o}radov lemma, ∞5, ∈4
vo\ Ma\}oldt {u\⌋t⟩o\, ∞∈4

we⟩}⟨t {u\⌋t⟩o\, ∞∞∈
Weyl ⌋r⟩ter⟩o\, ∞3
Weyl equ⟩d⟩str⟩⌊ut⟩o\ ⌋r⟩ter⟩o\, 5, ∞0,
∞3, ∈3, ̸4
Weyl equ⟩d⟩str⟩⌊ut⟩o\ t⟨eorem, 9
Weyl law, ∞↦3

Author's preliminary version made available with permission of the publisher, the American Mathematical Society
