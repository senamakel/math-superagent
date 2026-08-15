<!-- source: https://arxiv.org/pdf/2309.08729 | converted from PDF -->

arXiv:2309.08729v3  [math.NT]  11 Dec 2024
AN ANNOTATED BIBLIOGRAPHY FOR
COMPARATIVE PRIME NUMBER THEORY

GREG MARTIN, PU JUSTIN SCARFY YANG, ARAM BAHRINI, PRAJEET BAJPAI,
K ¨UBRA BENL˙I, JENNA DOWNEY, YUAN YUAN LI, XIAOXUAN LIANG,
AMIR PARVARDI, REGINALD SIMPSON, ETHAN PATRICK WHITE, AND CHI HOI YIP

Abstract. The goal of this annotated bibliography is to record every publication on the topic of comparative
prime number theory together with a summary of its results. We use a uniﬁed system of notation for the
quantities being studied and for the hypotheses under which results are obtained.

1. Introduction

Comparative prime number theory is the study of number-theoretic quantities, such as functions
that count primes with particular properties, and how they compare to one another. It certainly
includes (but is not limited to) “prime number races”, which examine inequalities between the
counting functions of primes in arithmetic progressions to the same modulus; indeed, Chebyshev
observing the apparent preponderance of primes of the form 4k + 3 over those of the form 4k + 1
was the historical beginning of comparative prime number theory. Studying inequalities between
two functions can be rephrased as studying the sign of their diﬀerence, and so the methods of
comparative prime number theory also extend to studying the sign (and changes of sign) of other
number-theoretic quantities that are less directly related to prime-counting functions.
The phrase “comparative prime number theory” goes back at least as far as the title of a long
sequence of papers of Knapowski and Tur´an, beginning with [71]. That paper begins with a list of
several questions that can be interpreted as an attempt to deﬁne the scope of the ﬁeld, as does the
ﬁrst paper [84] in a sequel series by the same authors. Other surveys of these topics include papers
by Kaczorowski [221] and by Ford and Konyagin [232], as well as an expository introduction to the
ﬁeld by Granville and the ﬁrst author [250].
This being said, there is no ironclad deﬁnition of what is and is not comparative prime number
theory. Most quantities in this ﬁeld have “explicit formulas” that express them as sums of oscillatory
functions indexed by the zeros of L-functions of some type (including the Riemann zeta-function).
As such, suitably normalized versions of these quantities are expected to have limiting (logarithmic)
distribution functions, which are measures that record the frequencies with which the normalized
quantities take values in various intervals in the limit (“continuous histograms” of their values).
In our view, the existence of such a limiting distribution is one of the main criteria for deciding
whether a topic does or does not belong to the ﬁeld of comparative prime number theory.
The purpose of this annotated bibliography is to provide a single exhaustive resource that lists
every publication in the ﬁeld of comparative prime number theory, and provides a summary of the
results of each publication included. Like any human endeavour, the fulﬁllment of that goal will
be imperfect. More speciﬁcally, we have aimed for completeness for all publications through 2023,
as well as an incomplete list of sources from 2024.
The publications in comparative prime number theory over the 170 years of its existence have
understandably used a wide variety of notations for the same objects. Another purpose of this
work is to propose a uniﬁed system of notation for referring to the functions and quantities that are
the main objects of study in comparative prime number theory, as well as uniform terminology for
the assumptions on zeros of L-functions that arise repeatedly when trying to prove theorems about
these quantities. In particular, in our summaries of each publication, we have translated the results
into this modern uniﬁed notation whenever possible, rather than preserving the notation used by

2010 Mathematics Subject Classiﬁcation. 11N13 (11Y35).
 1

2 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

the authors. In this respect, this work is more of a scientiﬁc resource than a historical document,
although of course we hope it has some utility in the latter role (and we have included authors’
exact words on a few occasions, particularly when problems or conjectures were ﬁrst proposed).
Section 2 is therefore a long section presenting this system of notation for elementary functions,
prime counting functions and other summatory functions of number-theoretic quantities, their er-
ror terms (both normalized and unnormalized), weighted and averaged versions of these quantities,
analogues of these quantities over number ﬁelds and function ﬁelds, functions that count the num-
ber of sign changes of these quantities, and (natural and logarithmic) limiting densities and limiting
distribution functions. Section 3, beginning on page 9, describes objects and theorems that fre-
quently arise in this ﬁeld, such as Dirichlet characters and L-functions, Landau’s theorem, explicit
formulas, the power-sum method, k-functions, and various hypotheses on the zeros of L-functions.
Section 4, beginning on page 12, enumerates the types of questions that comparative number theory
studies about the quantities from Section 2. The annotated bibliography proper begins on page 14.
The origin of this manuscript was a literature survey project by the ﬁrst two authors in 2012;
since then, the other authors have contributed signiﬁcantly and have greatly expanded the extent
of this bibliography and the accompanying material.

2. Notation related to number theory and real analysis

We use N to denote the set of positive integers, and similarly Z, R, and C to denote the sets of
integers, real numbers, and complex numbers, respectively. We reserve the letter p to denote prime
numbers, and sums and products such as ∑p and ∏p|q are restricted to prime values of p.
We use the following standard conventions regarding magnitudes of complex-valued functions f
and g, real-valued functions h, and nonnegative real-valued functions r and s (of a complex or real
argument z):
• f (z) ≪ s(z) (due to Vinogradov) means that there exists a constant C > 0 such that
|f (z)| ≤ Cs(z) for all values of z under consideration;
• O(s(z)) (due to Bachmann) represents an unspeciﬁed function f (z) with the property that
f (z) ≪ s(z);
• r(z) ≍ s(z) (due to Hardy) means that both r(z) ≪ s(z) and s(z) ≪ r(z) are true;
• f (z) ∼ g(z) (also due to Hardy) means that lim f (z)/g(z) = 1, where the location of the
limit is taken from context (often as z → ∞ through real numbers);
• f (z) = o(s(z)) (due to Landau) means that lim f (z)/s(z) = 0;
• f (z) = Ω(s(z)) (due to Hardy and Littlewood) is the negation of f (z) = o(s(z)), or equiva-
lently the statement lim sup |f (z)|/s(z) > 0;
• h(z) = Ω+(s(z)) and h(z) = Ω−(s(z)) (due in this form to Landau) mean, respectively, that
lim sup h(z)/s(z) > 0 and lim inf h(z)/s(z) < 0, either of which implies h(z) = Ω(s(z));
• h(z) = Ω±(s(z)) means that both h(z) = Ω+(s(z)) and h(z) = Ω−(s(z)) are true.

2.1. Elementary functions. As is standard in number theory, we use φ(n) to denote the Euler
totient function, which is the number of reduced residue classes modulo n. We use ω(n) to denote
the number of distinct prime factors of n and Ω(n) to denote the number of prime factors of n
counted with multiplicity. We let µ(n) and Λ(n) denote the M¨obius and von Mangoldt functions,
respectively:

µ(n) =
 {
(−1)ω(n), if n is squarefree,
0, otherwise; Λ(n) =
 {
log p, if n = pr for some r ∈ N,
0, otherwise.

We use (a, q) as a shorthand for gcd(a, q). For any (a, q) = 1, we deﬁne

cq(a) = #{b (mod q) : b2 ≡ a (mod q)}

to be the number of “square roots” of a modulo q. For brevity we write cq = cq(1), which is also
the number of real Dirichlet characters (mod q), or equivalently the index [(Z/qZ)× : ((Z/qZ)×)2];
it turns out that cq = 2ω(q)+η where η ∈ {−1, 0, 1} depends upon the power of 2 dividing n. For
(a, q) = 1, it is the case that cq(a) equals cq if a is a square (mod q) and 0 otherwise. (Many sources

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 3

deﬁne c(q, a) to be cq(a) − 1, which is more convenient for some purposes and less convenient for
others.)
We deﬁne two closely related logarithmic integrals

li(x) = lim
ε→0+
 ( ∫ 1−ε

0
 dt
log t + ∫ x

1+ε
 dt
log t
 ) =
 K∑

k=1
 (k − 1)!x
(log x)k + OK
 ( x
(log x)K+1
 )

Li(x) = ∫ x

2
 dt
log t = li(x) − li(2) ≈ li(x) − 1.04516378.

2.2. Prime counting functions. We use the standard notation for the prime counting functions

π(x) = #{p ≤ x} = ∑

p≤x 1

Π(x) = ∑

n≤x
 Λ(n)
log n = ∑

pk≤x
 1
k =
 ∞∑

k=1
 π(x1/k)
k

θ(x) = ∑

p≤x log p

ψ(x) = ∑

n≤x Λ(n) = ∑

pk≤x log p = ∑

p≤x
 ⌊ log x
log p
 ⌋ log p =
 ∞∑

k=1
 θ(x1/k)
k .

We may replace the cutoﬀ variable x with any set S of real numbers, so that for example

ψ(S) = ∑

n∈S Λ(n) and Π
((0, x]
) = Π(x) and θ(
(x, y]
) = θ(y) − θ(x).

All of these functions have analogues for prime powers restricted to arithmetic progressions:

π(x; q, a) = #{p ≤ x : p ≡ a (mod q)} = ∑

p≤x
p≡a (mod q)
 1

Π(x; q, a) = ∑

n≤x
n≡a (mod q)
 Λ(n)
log n = ∑

pk≤x
pk≡a (mod q)
 1
k

θ(x; q, a) = ∑

p≤x
p≡a (mod q)
 log p

ψ(x; q, a) = ∑

n≤x
n≡a (mod q)
 Λ(n) = ∑

pk≤x
pk≡a (mod q)
 log p.

These counting functions are interesting only in the case (a, q) = 1, a restriction that we will usually
not state explicitly. Here too we may replace the ﬁrst argument with a set, so that for example
π(S; q, a) = #{p ∈ S : p ≡ a (mod q)}.
When the third argument is a set rather than an integer, the function counts prime powers that
are congruent modulo q to any element of that set; for example, θ(x; q, {1, 2}) = θ(x; q, 1)+θ(x; q, 2).
In this context, R and N always refer to the quadratic residues and nonresidues, respectively, among
the reduced residues modulo q, so that for example

π(x; q, R) = #{p ≤ x : p is a quadratic residue (mod q)}

π(x; q, N ) = #{p ≤ x : p is a quadratic nonresidue (mod q)}.

Note that R contains φ(q)/cq residue classes (mod q) and N contains the other φ(q)(1 − 1/cq)
residue classes. We use A = N ∪ R to refer to the set of all reduced residue classes.

4 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

When these prime counting functions for arithmetic progressions appear with four arguments
instead of three, the function is the diﬀerence of the counts for the two indicated arithmetic pro-
gressions; for example, ψ(x; q, a, 1) = ψ(x; q, a) − ψ(x; q, 1). (Warning: some authors use ∆ for
diﬀerences of this type, but we give a diﬀerent meaning to ∆ below in Section 2.4.) When these
ﬁnal two arguments are sets, we make the convention that the two counting functions being sub-
tracted are individually normalized by the number of distinct reduced residue classes in each set;
for example,
 θ(x; 7, {1, 2}, {3, 4, 5}) = 1
2 θ(x; 7, {1, 2}) − 1
3 θ(x; 7, {3, 4, 5})

Π(x; q, N , R) = 1
φ(q) − cq Π(x; q, N ) − 1
cq Π(x; q, R).(2.1)

(This convention is consistent with the four-argument notation when the last two arguments are
single integers, although these is some dissonance between this convention and the three-argument
notation when the last argument is a set, since that function is not normalized in this way.) There is
no need for the notation to admit the possibility of two diﬀerent moduli, since such a diﬀerence can
always be written using residue classes of the least common multiple of the moduli: for example,

π(x; 8, 1) − π(x; 5, 2) = 4π(x; 40, {1, 9, 17, 33}, {7, 17, 27, 37}
) = 3π(x; 40, {1, 9, 33}, {7, 27, 37}).

The residue class 1 (mod q) is special in some ways, and it is thus helpful to deﬁne the notation

π(x; q, 1, max) = π(x; q, 1)− max
a∈(Z/qZ)×
a̸≡1 (mod q)
 π(x; q, a), π(x; q, 1, min) = π(x; q, 1)− min
a∈(Z/qZ)×
a̸≡1 (mod q)
 π(x; q, a),

and similarly for other prime counting functions.

2.3. Prime ideal classes. For any number ﬁeld K (ﬁnite extension of Q), we say that α ∈ K is
totally positive if α maps to a positive real number under all embeddings of K in C. We call ideals a
and b of a number ﬁeld K congruent modulo another ideal f ⊂ K if both a and b are coprime to
f and there exist totally positive algebraic integers α and β in K with α ≡ β ≡ 1 (mod f) such
that αa = βb. The equivalence classes of ideals modulo f form a group under ideal multiplication,
with the principal ideal class K0 as its identity element. For a character χ of this group, we abuse
notation slightly by deﬁning χ(a) on ideals a directly: if a is coprime to f then we set χ(a) = χ([a]),
where [a] is the ideal class (mod f) containing a, and if a is not coprime to f then we set χ(a) = 0.
We can now deﬁne the Hecke–Landau zeta-function ζ(s, χ) to be the Dirichlet series

ζ(s, χ) = ∑

a
 χ(a)
Na
s ,

Finally, for an ideal class K, we deﬁne prime ideal counting functions such as

π(x, K) = ∑

Np≤x
p∈K
p prime ideal
 1, ψ(x, K) = ∑

Npm≤x
pm∈K
p prime ideal
 log Np.

2.4. Error terms for prime counting functions. These prime counting functions have well-
known main terms, and it is useful to have a standard notation to refer to the error terms obtained
by subtracting these main terms, as well as normalized versions of such error terms. We use ∆ to
denote error terms for the standard prime counting functions:

∆ψ(x) = ψ(x) − x, ∆θ(x) = θ(x) − x, ∆Π(x) = Π(x) − li(x), ∆π(x) = π(x) − li(x).

(In this document’s article summaries, we will use the above normalizations even when an article
subtracts a slightly diﬀerent main term: we do not distinguish here between li(x) and Li(x) and∑2≤n≤x 1/ log n, for example.) We also use E for normalized versions of these error terms:

Eψ(x) = ∆ψ(x)
√
x , Eθ(x) = ∆θ(x)
√x , EΠ(x) = ∆Π(x)
√x/ log x , Eπ(x) = ∆π(x)
√x/ log x .

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 5

While there is not a formula for starting with a general function f and determining the correct
denominator to use when deﬁning Ef , the normalization factor chosen is the one for which the
resulting E function is expected to have a limiting logarithmic distribution.
It’s not uncommon to integrate these error terms: for a function f such as π, Π, θ, or ψ, we
deﬁne A
f
0 (x) = ∆f (x) and, for m ≥ 1,

A
f
m(x) = ∫ x

0 A
f
m−1(t) dt.

(Again, we ignore the fact that some articles might use a diﬀerent lower endpoint for such in-
tegrals.) This operation has a predictable eﬀect on summatory functions and explicit formulas:
for example, A
ψ
m(x) = ∑n≤x(Λ(n) − 1)(x − n)m/m! has an explicit formula containing terms of
the form xρ+m/ρ(ρ + 1) · · · (ρ + m). For repeated integration of the absolute error, we also deﬁne
A
f
|0|(x) = |Af (x)| and, for m ≥ 1,
 A
f
|m|(x) = ∫ x

0 A
f
|m−1|(t) dt.

There are similar logarithmic integration operators: we deﬁne A
f
0 (x) = ∆f (x) and, for m ≥ 1,

A
f
m(x) = ∫ x

0 A
f
m−1(t) dt
t .

This operation also predictably aﬀects summatory functions and explicit formulas: for example,
A
ψ
m(x) = ∑n≤x(Λ(n) − 1)(log x
n )m has an explicit formula containing terms of the form xρ/ρm+1.

We also use the notation A
f
|m|(x) for repeated logarithmic integration of the absolute error.
When we count primes in arithmetic progressions, the error terms ∆ include a factor of φ(q) for
simplicity: for example,

∆ψ(x; q, a) = φ(q)ψ(x; q, a) − x and ∆π(x; q, a) = φ(q)π(x; q, a) − li(x).

The normalized error terms E are then derived from these ∆ as before: for example,

Eψ(x; q, a) = ∆ψ(x; q, a)
√x and Eπ(x; q, a) = ∆π(x; q, a)
√
x/ log x .

It is convenient at times to use a prime counting function itself as the main term, and such error
terms are denoted by the symbol ˚∆: for example,

˚∆ψ(x; q, a) = φ(q)ψ(x; q, a) − ψ(x) and ˚∆π(x; q, a) = φ(q)π(x; q, a) − π(x).

(Typically this modiﬁcation results in the same explicit formula with the principal character re-
moved.) The corresponding normalized error terms are denoted by ˚E: for example,

˚Eψ(x; q, a) = ˚∆ψ(x; q, a)
√x and ˚Eπ(x; q, a) = ˚∆π(x; q, a)
√
x/ log x .

We extend our convention regarding counting functions in arithmetic progressions: for example,

∆ψ(x; q, a, b) = ∆ψ(x; q, a) − ∆ψ(x; q, b) and Eπ(x; q, a, b) = Eπ(x; q, a) − Eπ(x; q, b).

Note that functions of the ﬁrst type are almost redundant, since (for example) ∆ψ(x; q, a, b) =
φ(q)ψ(x; q, a, b) exactly. (And recall that some authors use ∆ to mean this diﬀerence function
without the factor φ(q).) However, there will be situations where each notation is useful to us;
furthermore, this new use of ∆ already follows from existing notational conventions.
It can also be convenient to deﬁne this notation for the function ψ(x, χ) = ∑n≤x Λ(n)χ(n), for
any Dirichlet character χ (see Section 3.1), in the following way:

∆ψ(x, χ) = ψ(x, χ) −
 {
x, if χ = χ0,
0, if χ ̸= χ0, Eψ(x, χ) = ∆ψ(x, χ)
√x .

6 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

All of the functions in this section so far have been real-valued (except for the last paragraph
where the functions are potentially complex-valued); in the context of primes in arithmetic pro-
gressions, it is often helpful to consider vector-valued functions. We use subscripts to indicate the
modulus and residue classes—for example,

πq;a1,...,ar (x) = (π(x; q, a1), . . . , π(x; q, ar)
) and ˚Eψ
q;a1,...,ar (x) = ( ˚Eψ(x; q, a1), . . . , ˚Eψ(x; q, ar)
).

2.5. Weighted versions of prime counting functions. It is common to vary these prime count-
ing functions by attaching a weight to each term in the sum, changing for example ∑n≤x Λ(n) to
∑n≤x Λ(n)g(n). We use the following consistent notation for the most common of these variants.
As is standard, the subscript 0, as in the example ψ0(x) = 1
2 (ψ(x−) + ψ(x+)
), represents a
modiﬁcation of a function’s value at a jump discontinuity to equal the average of the left- and
right-hand limits.
The subscript r represents weighting by a reciprocal factor (often resulting in a “Mertens sum”);
for example,
 πr(x) = ∑

p≤x
 1
p , θr(x) = ∑

p≤x
 log p
p , and ψr(x; q, a) = ∑

n≤x
n≡a (mod q)
 Λ(n)
n .

If we wish to modify one of these Mertens sums at its jump discontinuities as above, we concatenate
the two subscripts: for example, πr0(x) = 1
2 (πr(x−)+πr(x+)
). Indeed all of our previous notational
variants can apply to these sums as well—for example,

∆πr (x) = πr(x) − (log log x + B) and Eπr (x) = √x log x · ∆πr (x)

for the appropriate constant B.
The subscript e represents weighting by an exponentially decaying function of x rather than
cutting oﬀ abruptly at x; for example,

πe(x) = ∑

p e
−p/x and ψe(x; q, a) = ∑

n≥1
n≡a (mod q)
 Λ(n)e
−n/x.

In terms of their asymptotics, these exponentially weighted sums usually act like their abrupt-cutoﬀ
versions; for example, πe(x) has a similar size to π(x). However, their oscillations are typically
damped, often resulting in rather diﬀerent properties when comparing two such functions to each
other (such as the exponentially weighted version having a bias for one sign while the unweighted
version exhibits oscillations of sign).
The subscript l represents weighting by a certain exponential factor with a squared logarithm,
scaled by a second parameter r: for example,

πl(x, r) = ∑

p e
− 1
r (log p
x )2 and ψl(x, r; q, a) = ∑

n≥1
n≡a (mod q)
 Λ(n)e
− 1
r (log n
x )2.

In asymptotic terms, this weighting is similar to restricting the range of summation to approxi-
mately [e−√rx, e
√rx]; again, the oscillatory nature of the weighted sum can be rather diﬀerent.
When the weight function is a Dirichlet character χ (see Section 3.1), we follow the tradition of
putting χ as an extra argument rather than a subscript; for example,

θ(x, χ) = ∑

p≤x χ(p) log p.

2.6. Summatory functions. Certain summatory functions of multiplicative functions have been
analyzed using the techniques of comparative prime number theory. Two notable examples are the
sums of the M¨obius and Liouville functions, which are denoted by

M (x) = ∑

n≤x µ(n) and L(x) = ∑

n≤x(−1)
Ω(n),

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 7

respectively. (The Liouville function is typically denoted by λ(n) = (−1)Ω(n), but we avoid that
notation herein to free the symbol λ for other uses.) Two conjectures that motivated substan-
tial work in comparative prime number theory are the “Mertens conjecture”, the assertion that
|M (x)| < √x, and the “P´olya problem”, the assertion that L(x) ≤ 0. (The latter assertion is often
mistakenly named “P´olya’s conjecture”, but P´olya only posed and studied the problem rather than
making a deﬁnitive conjecture and indeed probably found it unlikely to be true.) Both assertions
have been disproved (in [181] and [51], respectively), although research continues into the distribu-
tion of these two functions. The weak Mertens conjecture, namely the assertion that M (x) ≪ √x,
is still unresolved, although it was shown in [35] to be incompatible with the pair of conjectures
RH and LI (see Section 3.6).
The notational conventions from the previous sections are used for weighted versions of these
summary functions as well; for example,

M (x; q, a) = ∑

n≤x
n≡a (mod q)
 µ(n) and Lr(x) = ∑

n≤x
 (−1)Ω(n)

n ;

the conjecture that the latter is always nonnegative (often attributed to Tur´an, though again he only
studied the problem rather than asserting a conjecture) was also disproved in [51]. We also deﬁne the
notation ∆M (x) = M (x) and ∆L(x) = L(x) and ∆Lr (x) = Lr(x); while unproﬁtable on their own,
these deﬁnitions allow us to employ the notation for repeated averaging described in Section 2.4,
as well as the notation EM (x) = M (x)/
√x and EL(x) = L(x)/
√x and ELr (x) = Lr(x)
√x.
We also introduce some standard notation for k-free numbers, which are numbers not divisible
by the kth power of any prime, so that squarefree numbers are the case k = 2. Let Qk(x) denote
the number of k-free integers up to x, and deﬁne ∆Qk(x) = Qk(x) − x/ζ(k). For integers k ≥ 2, the
generalized M¨obius function µk(n) is deﬁned to be µk(n) = (−1)Ω(n) if n is k-free and µk(n) = 0
otherwise. Note that these functions interpolate between µ2(n) = µ(n) and limk→∞ µk(n) =
(−1)Ω(n). These quantities are related by the identity Qk(x) = ∑n≤x µ2
k(n).
Another summatory function studied using techniques that overlap with those of comparative
prime number theory is

D(x) = ∑

n≤x τ (n), where τ (n) = #{d : d | n} = ∑

d|n 1.

It was ﬁrst proven by Dirichlet (see [16] for a discussion of the history) that

D(x) = x log x + (2C0 − 1)x + O(
√x),

where C0 is Euler’s constant. The study of the error term ∆D(x) = D(x) − x log x − (2C0 − 1)x is
intertwined with comparative prime number theory, and one early result by Hardy [16] demonstrates
that the techniques of comparative prime theory are often applicable to the study of this error term.

2.7. Counting sign changes. We use the letter W generally to denote the function that counts
the number of sign changes of another function on an interval. To be pedantic, if h is a function
from (1, ∞) to R, then we deﬁne

W (h; T ) = max {n ≥ 0 : there exist 1 < t0 < t1 < · · · < tn < T

with h(tj−1)h(tj ) < 0 for all 1 ≤ j ≤ n}
.

(One could quibble over whether taking the value 0 counts as a sign change regardless of its
neighboring values; the results in this subject tend not to require this loophole.) We can demand
large oscillations to go along with our sign changes by adding a function as an additional argument:

W (
h; T ; S(t)
) = max {
n ≥ 0 : there exist 1 < t0 < t1 < · · · < tn < T

with h(tj−1)h(tj ) < 0 for all 1 ≤ j ≤ n and |h(tj)| > S(tj) for all 0 ≤ j ≤ n}
.

Given functions f and g from (1, ∞) to R, we further deﬁne W (f, g; T ) = W (f − g; T ) to be
the counting function of sign changes of the diﬀerence f (x) − g(x). Certain special cases of this

8 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

notation deserve a shorthand notation: we deﬁne W π(T ) = W (π, li; T ) and W Π(T ) = W (Π, li; T ),
and also W θ(T ) = W (θ, x; T ) and W ψ(T ) = W (ψ, x; T ) where x denotes the identity function. (As
before, we do not distinguish in our summaries between li(x) and Li(x) and ∑2≤n≤x 1/ log n in this
context.) The bare notation W (T ) is a further shorthand for W π(T ).
In addition, given a positive integer q and distinct reduced residues a and b (mod q), we deﬁne
W ψ
q;a,b(T ) = W (
ψ(x; q, a), ψ(x; q, b); T ), and similarly with ψ replaced by θ, Π, or π; we further
shorten W π
q;a,b(T ) to Wq;a,b(T ). We may add a function as an additional argument as above to
indicate large oscillations, as in Wq;a,b(T ; S(t)) for example; similarly, we may replace single residue
classes with sets of residue classes, as in Wq;N ,R(T ).

2.8. Densities. The natural density of a set S of positive real numbers is

d(S) = lim
x→∞ meas ({0 < t ≤ x : t ∈ S}
)

x = lim
x→∞ 1
x
 ∫

0<t<x
t∈S
 dt,

where “meas” denotes Lebesgue measure on R. On the other hand, the logarithmic density of a
set S ⊂ (1, ∞) is
 δ(S) = lim
x→∞ 1
log x
 ∫

1<t<x
t∈S
 dt
t .

An easy change of variables shows that the logarithmic density of S equals the natural density of
the set log S = {log t : t ∈ S}. Moreover, a partial summation argument shows that if the natural
density d(S) exists, then the logarithmic density δ(S) also exists and has the same value. However,
there are sets whose natural density does not exist but whose logarithmic density does exist; for
example, the union (over k ∈ N) of the intervals [102k−1, 102k) has logarithmic density equal to 1
2
but does not have a natural density.
We will use many variants of this logarithmic density notation. If f1, . . . , fr are functions from
(1, ∞) to R, then we deﬁne the shorthand notation

δ(f1, f2, . . . , fr) = δ({x > 1 : f1(x) > f2(x) > · · · > fr(x)}
).

For example, δ(li, π) is the logarithmic density of the set of real numbers x > 1 for which li(x) >
π(x). Certain special cases of this notation can be even further abbreviated. For example, let q be
a positive integer, and let a1, . . . , ar be distinct reduced residues (mod q). Then we deﬁne

δq;a1,...,ar = δ(π(x; q, a1), . . . , π(x; q, ar)
) = δ({x > 1 : π(x; q, a1) > · · · > π(x; q, ar)}
).

We also deﬁne

δq;N ,R = δ(π(x; q, N ), π(x; q, R)
) = δ({x > 1 : π(x; q, N ) > π(x; q, R)}
)

and similarly for δq;R,N (these deﬁnitions are sensible when q has primitive roots).
Finally, we deﬁne the upper and lower logarithmic densities of S (which always exist) as

δ(S) = lim sup
x→∞ 1
log x
 ∫

1<t<x
t∈S
 dt
t , δ(S) = lim inf
x→∞ 1
log x
 ∫

1<t<x
t∈S
 dt
t ,

so that δ(S) exists if and only if δ(S) = δ(S). This notation propagates through our shorthand
notations as well; for instance, δq;N ,R = δ({x > 1 : π(x; q, N ) > π(x; q, R)}
).

2.9. Limiting distributions and density functions. Given a function h : [0, ∞) → R, the
limiting (or asymptotic) cumulative distribution function of h is the nondecreasing function

lim
T →∞ meas{t ∈ [0, T ] : h(t) ≤ a}
T = lim
T →∞

( 1
T
 ∫

0≤t≤T
h(t)≤a
 dt)

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 9

if the limit exists (except at jump discontinuities, of which there are only a countable number). More
common in comparative prime number theory is the limiting logarithmic cumulative distribution
function, with the analogous deﬁnition

κ
h(α) = lim
U →∞ 1
log U
 ( ∫

1≤u≤U
h(u)≤α
 du
u
 ),

which equivalently is the cumulative distribution function of h(et). There is a corresponding limiting
logarithmic density µh, which is the measure satisfying

µh((α, β]
) = ∫ β

α κ
h(x) dx

for any real numbers α < β. It has the property that for any bounded continuous function f (x),

lim
U →∞ 1
log U
 (∫ U

1 f (
h(u)
) du
u
 ) = ∫
R f (x) dµh(x),

and the continuity assumption can be omitted if µh is absolutely continuous with respect to
Lebesgue measure. These logarithmic densities are probability measures and thus can be viewed as
the densities of random variables. Vector-valued functions have analogous logarithmic cumulative
distribution functions and logarithmic densities on Rr.

3. Notation related to complex analysis

As is usual in analytic number theory, we often use s = σ + it to denote a complex variable and
its real and imaginary parts; its argument will be denoted by arg(s), so that s = |s|ei arg s. If ρ is a
nontrivial zero of a Dirichlet (or other) L-function, including the Riemann zeta-function, we write
ρ = β + iγ to refer to its real and imaginary parts.

3.1. Dirichlet characters and Dirichlet L-functions. As usual, a Dirichlet character with
modulus q is a completely multiplicative function on Z with period q whose support is the set of
integers coprime to q. We call characters real, complex, quadratic, (im)primitive, and induced with
their standard meanings; the conductor of a character χ is the modulus of the primitive character
χ∗ that induces it.
We use χ0 to denote the principal character (the modulus being understood from context). When
D ̸= 1 is a fundamental discriminant, we let χD denote the associated quadratic character, which
is a primitive character of conductor |D| that is even if D > 0 and odd if D < 0. When q is prime,
we use the shorthand χ±q to mean χq if q ≡ 1 (mod 4) and χ−q if q ≡ 3 (mod 4). On the other
hand, by χ1 we mean a hypothetical quadratic character with an exceptional zero β1.
Every Dirichlet character gives rise to a Dirichlet L-function L(s, χ) = ∑∞
n=1 χ(n)n−s. Like the
Riemann zeta-function (which is the special case q = 1 and χ = χ0), Dirichlet L-functions have
inﬁnitely many nontrivial zeros ρ = β + iγ in the critical strip 0 < β < 1. These zeros are counted
by the function N (T, χ) = #{ρ : L(ρ, χ) = 0, 0 < β < 1, |γ| ≤ T }.
Note the slight dissonance with the traditional notation

N (T ) = #{ρ : ζ(ρ) = 0, 0 < β < 1, 0 ≤ γ ≤ T }

which counts only nontrivial zeros of ζ(s) in the upper half-plane: this suﬃces for ζ(s) due to the
Schwarz reﬂection principle, but Dirichlet L-functions do not all possess that symmetry.
Sums over zeros of Dirichlet L-functions (of the type that arise in explicit formulas, for example)
often do not converge absolutely, and therefore we adopt the standing convention that sums over
nontrivial zeros are limits of their symmetric truncations:
∑

ρ f (ρ) = lim
T →∞
 ∑

L(ρ,χ)=0
0<β<1
|γ|≤T
 f (ρ).

10 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

3.2. Landau’s theorem. For a real-valued function A(x), deﬁne

g(s) = ∫ ∞

1
 A(x)
xs dx

Typically there will be a real number σ0 such that this integral converges when σ > σ0 and diverges
when σ < σ0. Landau proved that if A(x) is eventually positive or eventually negative, then g(s)
has a singularity at s = σ0 (that is, g(s) must have a rightmost singularity on the real axis).
The contrapositive of this theorem is a useful tool in comparative prime number theory: Suppose
that g(s) has no singularities on the subray {σ ∈ R : σ > σ1} of the real axis (that is, g(s) is analytic
on a neighborhood of that ray), but g(s) is not analytic in the half-plane {s ∈ C : σ > σ1}. Then
A(x) has arbitrarily large sign changes.

3.3. Explicit formulas. As mentioned earlier, one of the deﬁning characteristics of comparative
prime number theory is the presence of an “explicit formula”. There is no precise deﬁnition of
that term, but typically an explicit formula contains a sum over the (nontrivial) zeros of some
L-function. The prototypical example is the explicit formula

ψ0(x) = x − ∑

ρ
 xρ

ρ − log 2π − 1
2 log (1 − 1
x2
 )

for the Chebyshev function ψ(x) modiﬁed at its jump discontinuities; the fact that this is an exact
equality for all x > 1 is one of the most beautiful statements in analytic number theory.
Explicit formulas for prime-counting functions yield explicit formulas for their normalized error
terms; for example, assuming the generalized Riemann hypothesis,

Eθ(x; q, a, b) = cq(b) − cq(a) − ∑

χ (mod q)
 (
χ(a) − χ(b)
) ∑

γ∈R
L(1/2+iγ,χ)=0
 xiγ

1
2 + iγ + Oq(x−1/6).

This formula is helpful for studying when Eθ(x; q, a, b) > 0, or equivalently when θ(x; q, a) >
θ(x; q, b). Note that each summand in the inner sum oscillates around a circle of ﬁxed radius
(one that decreases as γ increases); while this inner sum is not literally bounded, it is bounded
on average over x and possesses a limiting logarithmic distribution. Therefore Eθ(x; q, a, b) has a
limiting logarithmic distribution with mean cq(b) − cq(a), the sign of which depends on whether a
and b are quadratic residues or nonresidues modulo q.

3.4. The power-sum method. A great deal of early progress in comparative prime number
theory, particularly the unconditional results, relied on the study of linear combinations of powers
of complex numbers, namely sums of the shape

sv =
 n∑

j=1 bjzv
j .

Lower bounds for such sums were systematically developed by Tur´an and S´os. While there are
many variants of these lower bounds that have been obtained, they can be grouped into two main
categories.
The “ﬁrst main theorem” is a type of result that applies when the zj are large. For example,
suppose that z1, . . . , zn are distinct complex numbers with |zn| ≥ 1 for all n. For any nonnegative
integer m, there exists an integer m + 1 ≤ v ≤ m + n such that

|sv| ≥ ( n
A(m + n)
 )n|s0|,

where A is an absolute constant.
The “second main theorem” is a type of result that applies when the zj are small. For exam-
ple, suppose that z1, . . . , zn are distinct complex numbers with 1 ≥ |z1| ≥ · · · ≥ |zn|. For any

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 11

nonnegative integer m, there exists an integer m + 1 ≤ v ≤ m + n such that

|sv| ≥ ( n
B(m + n)
 )n min
1≤j≤n
 ∣
∣
∣
∣
 j∑

n=1 bn
∣
∣
∣
∣,

where B is an absolute constant.
Instead of restricting the candidate exponents v to an interval of exactly n consecutive integers, we
may allow candidates from a longer range of exponents. For example, in the “second main theorem”
(so that 1 ≥ |z1| ≥ · · · ≥ |zn|), let m ≥ N ≥ n; then there exists an integer m + 1 ≤ v ≤ m + N
such that
 |sv| ≥ ( N
Bm
 )N min
1≤j≤n
 ∣
∣
∣
∣
 j∑

n=1 bn
∣
∣
∣
∣.

For the “second main theorem”, one can also obtain better conclusions by adding an “argument
restriction”, that is, the assumption that each | arg zj| ≥ ε for some ﬁxed ε > 0. Stronger results
can also be obtained by assuming that each bj is a nonnegative real number, and strengthened
further by restricting to the special case b1 = · · · = bn = 1.
Note that these results show that some sv is large in modulus but gives no information about
its argument. Tur´an (somewhat unhelpfully) calls these results “two-sided” theorems. There exist
analogous results where the lower bound applies not just to |sv| but to ℜsv or −ℜsv; Tur´an calls
such results “one-sided” theorems.

3.5. k-functions. A great deal of the work of Kaczorowski involves certain functions called k-
functions, which are superﬁcially similar to sums that appear in explicit formulas for ψ(x, χ). For
ℑz > 0, deﬁne
 k(z, χ) = ∑

γ>0 e
ρz and K(z, χ) = ∑

γ>0
 eρz

ρ ,

where the sums are over zeros of L(s, χ) in the upper half-plane.
These functions can be regarded as having their domain equal to M, the Riemann surface for
log z; every point on the surface can be uniquely written as reia where r > 0 and a ∈ R. Let zc

denote the natural extension of complex conjugation to M, namely (reia)c = re−ia; also let z∗

denote an extension of multiplication by −1 to M, namely (reia)∗ = rei(a−π).
Certain functions appear frequently in connection to k-functions: deﬁne

D(z, χ) = − ∑

β>0
L(β,χ)=0
 e
βz + 1
e2z − 1
 




e3z + e2z − 1, if χ = χ0,
ez, if χ ̸= χ0 and χ(−1) = 1,
e2z, if χ(−1) = −1.

Further deﬁne
 F (x, χ) = lim
y→0+
 (K(x + iy, χ) + K(x + iy, χ)
)

and
 R1(x) = 1
2 log(1 − e
−2x), R−1(x) = 1
2 log ex − 1
ex + 1 .

Certain constants also appear frequently: deﬁne

B(χ) = ∑

β>0
L(β,χ)=0
 1
β − C0
2 − 1
2 log π
q + F (0, χ) −
 




1, if χ = χ0,
0, if χ ̸= χ0 and χ(−1) = 1,
log 2, if χ(−1) = −1

(note that B(χ) is not the same as a constant of the same name related to the Hadamard product
expansion of L(s, χ)) and C(χ) = B(χ) + C0 + log 2π
q .

12 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

3.6. Hypotheses on zeros. It is extremely diﬃcult to obtain unconditional results in compara-
tive prime number theory, particularly where limiting logarithmic distributions and densities are
concerned. Certain assumptions on the zeros of Dirichlet L-functions therefore arise repeatedly
in this subject. The most famous of these is the generalized Riemann hypothesis (GRH), some-
times called the Riemann–Piltz conjecture, which asserts that all nontrivial zeros of all Dirichlet
L-functions have real part equal to 1
2 . We use σ0-GRH to denote the weaker (but still currently
inaccessible) assertion that L(σ + it, χ) does not vanish when σ > σ0, so that 1-GRH is trivial and
1
2 -GRH is the same as the full GRH.
Given a nonempty set X of Dirichlet L-functions (or, abusing notation slightly, Dirichlet char-
acters), we let Θ(X) denote the supremum of the real parts of their zeros, that is, the smallest
real number such that Θ(X)-GRH holds. We use the abbreviation Θ(q) when X is the set of all
Dirichlet characters modulo q, as well as Θ(χ) when X consists of the single Dirichlet character χ.
The assertion that some Dirichlet L-function in X has a zero with real part exactly equal to Θ(X)
is abbreviated SA for “supremum attained” (and sometimes referred to as “Ingham’s condition”).
We may write SA(X) to emphasize that we are considering a speciﬁc set of Dirichlet L-functions,
but the set is often inferred from context (this remark applies similarly to the remainder of the
notation in this section). We note that GRH implies SA but that Θ(X) = 1 is inconsistent with SA.
Regarding the vertical distributions of the zeros, we use HC to denote the “Haselgrove condition”
that no Dirichlet character (in the set under discussion) vanishes on the segment 0 < σ < 1 of the
real axis. Such a real zero would create a non-oscillatory term in relevant explicit formulas, one
that could result in an unexpected source of bias. By continuity, HC implies that there exists a
positive constant Ek such that these L(s, χ) are nonzero on the rectangle {0 < σ < 1, |t| ≤ Ek};
we write HC(Ek) if we need to refer to this parameter.
The notation GRH(H) (sometimes called the “ﬁnite Riemann–Piltz” conjecture) denotes the
generalized Riemann hypothesis “up to height H”, namely the statement that if ρ is a nontrivial
zero of L(s, χ) with |γ| ≤ H, then β = 1
2 . Note that HC(Ek) implies GRH(H) if Ek ≥ H; on the
other hand, GRH(H) gives no constraint at all upon zeros on the critical line. We therefore use
the notation GRH(H, Ek) to denote the combination of GRH(H) and HC(Ek), the latter of which
constrains only the zeros on the critical line when Ek < H. Note also that GRH(0) is almost the
same as HC, except that GRH(0) allows for the possibility of a zero at s = 1
2 .
The arithmetic nature of the imaginary parts (ordinates) of zeros of L(s, χ) is also signiﬁcant
in comparative prime number theory. We write LI (sometimes called GSH for the “grand simplic-
ity hypothesis”) to denote the “linear independence” assertion that the multiset of nonnegative
ordinates of zeros of the relevant Dirichlet L-functions is linearly independent over the rational
numbers. In particular, LI implies that all zeros are simple and that L( 1
2 , χ) ̸= 0. We use LI(σ)
to denote the corresponding linear independence conjecture restricted to the zeros with real parts
greater than or equal to σ.
For the Riemann zeta-function, the Riemann hypothesis (RH) is the assertion that all nontrivial
zeros of ζ(s) have real part equal to 1
2 . Almost all of the other notation above would be used in
the same form when referring to ζ(s), although Θ({ζ(s)}) is abbreviated simply to Θ. These same
abbreviations are also used for analogous hypotheses on zeros of other L-functions that should be
clear from context.
 4. Types of questions

Given two functions f, g : (1, ∞) → R that are asymptotic to each other, such as π(x) and li(x)
or π(x; 4, 1) and π(x; 4, 3), the questions that comparative prime number theory tends to ask about
the pair of functions are:

(1) Are there arbitrarily large values of x for which f (x) > g(x), and arbitrarily large values
of x for which g(x) < f (x)? In other words, does the diﬀerence f (x) − g(x) change signs
inﬁnitely often? (These are not quite mathematically identical because of the possibility of
plentiful or carefully arranged ties f (x) = g(x), so implicit in this question is asking whether

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 13

such ties are rare.) The other alternative is that one of the functions exceeds the other for
all suﬃciently large x.
(2) How large and positive can the diﬀerence f (x) − g(x) get? How large and negative can it
get?
(3) More generally, what is the distribution of values of f (x) − g(x)? Is it possible that some
suitably normalized version of this diﬀerence, such as (f (x) − g(x))/
√x, actually has a
limiting distribution or a limiting logarithmic distribution?
(4) How often does the diﬀerence f (x) − g(x) change sign? How many sign changes are there
in (1, X) as a function of X? How close can we take Y = Y (X) to X to ensure that there
is always a sign change in [X, Y ]?
(5) What is the natural density of the set of real numbers x > 1 for which f (x) > g(x)? What
is its logarithmic density δ(f, g)? (Typically we believe that the natural densities of such
sets do not exist in prime number races, but that their logarithmic densities do exist.)
(6) Given a family of races, such as π(x; q, N ) versus π(x; q, R): how do answers to the above
questions, such as δq;N ,R, depend upon the member of the family (q in this case)? Do the
distributions of the members of the family tend to some limit, such as a normal distribution?
Some of the above questions have analogues for several functions f1, . . . , fr : (1, ∞) → R considered
together:
(7) Are there arbitrarily large values of x for which f1(x) > · · · > fr(x)? Does this remain true
no matter how we permute the fj?
(8) More generally, what is the distribution of values of the vector (f1(x), . . . , fr(x)
) ∈ Rr? Is
it possible that some suitably normalized version of this diﬀerence actually has a limiting
distribution or a limiting logarithmic distribution?
(9) What is the natural density of the set of real numbers x > 1 for which f1(x) > · · · >
fr(x)? What is its logarithmic density δ(f1, . . . , fr)? (As before, we believe that the natural
densities of such sets do not exist in prime number races, but that their logarithmic densities
do exist.)
(10) Given a family of such r-way races, how do answers to the above questions depend upon
the member of the family? Do the distributions of the members of the family tend to some
limit, such as a multivariate normal distribution?
The articles [71] and [84] by Knapowski and Tur´an present organized schema for problems in
comparative prime number theory, as do surveys of these topics by Kaczorowski [221] and by Ford
and Konyagin [232], although several of the questions listed above had not yet been investigated
suﬃciently deeply to make some of their lists.

Acknowledgments

We gratefully thank Devang Agarwal, Alexandre Bailleul, Michael Coons, Alia Hamieh, Elchin
Hasanalizade, Daniel R. Johnston, Farid Jokar, Florent Jouve, Shin-ya Koyama, LATEX Stack Ex-
change user “moewe”, Michael J. Mossinghoﬀ, Nathan Ng, and Alan Xiang for their contributions
to this manuscript. We also thank the anonymous referees for their thorough readings and de-
tailed suggestions for corrections and improvements. Many authors’ research was supported by the
Natural Science and Engineering Research Council of Canada.

Chronological bibliography

The annotated bibliography begins here, with all of the sources cited and summarized listed in
chronological order; items in this chronological list are labeled by their number alone, such as [123].
Following the annotated bibliography is a second list, in alphabetical order by author, of the same
set of sources but without annotations; items in this alphabetical list have been given labels that
are numbers following the letter “A” (for “alphabetical”), such as [A45], to distinguish them from
the labels in the main list. Each entry in the second bibliography links to its corresponding entry
and annotation in the ﬁrst bibliography.

14 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

Our goal has been to describe the results using a single system of notation, both to avoid the
need to deﬁne notation in individual annotations and to propose a uniﬁed notation for current and
future practitioners of comparative prime number theory. Any notation in a summary that is not
deﬁned there can be found or deduced from the detailed material in Sections 2–3.

[1] Chebyshev, P., Lettre de M. le professeur Tch´ebychev a M. Fuss, sur un nouveau th´eor`eme relatif
aux nombres premiers contenus dans la formes 4n + 1 et 4n + 3, French, Bull. de la Classe phys.
math. de l’Acad. Imp. des Sciences St. Petersburg 11 (1853), 208.

The author remarks for the ﬁrst time that there appear to be more primes of the form 4n + 3 than
4n + 1, in that their counting functions “diﬀer notably in their second terms” (original French:
“diﬀ`erent notablement entre elles par leurs seconds termes”). Several assertions are made (without
proof): that Eπ(x; 4, 3, 1) takes values arbitrarily close to 1; that πe(x, χ−4) → −∞ as x → ∞;
and that if f (x) is a decreasing function with limx→∞ x
1/2f (x) ̸= 0, then the series ∑
p χ−4(p)f (p)
diverges.

[2] Piltz, A., ¨Uber die H¨auﬁgkeit der Primzahlen in arithmetischen Progressionen und ¨uber verwandte
Gesetze, German, Habilitationsschrift, Friedrich–Schiller–Universit¨at Jena (1884).

Several authors cite this habilitation thesis as the ﬁrst appearance of GRH, the generalized Riemann
hypothesis for Dirichlet L-functions (“Riemann–Piltz conjecture”). On page 25 the author writes,
“Wie in der Einleitung erw¨ahnt wurde, hatte Riemann die Vermuthung, dass diese Verschwindung-
stellen was die Funktion ζ(s) betriﬀt, sich s¨ammtlich durch die Form 1/2 + αi wo α reell ist, bringen
lassen. Dieser Satz gilt nicht nur f¨ur die Funktion ζ(s) sondern auch f¨ur die ζ(s, ν).”

[3] Phragm´en, P., Sur le logarithme int´egral et la fonction f (x) de Riemann, French, ¨Ofversigt af Kongl.
Vetenskaps–Akademiens F¨ohandlingar. 48 (1891), 599–616.

The author establishes a general proposition (similar to the eventual “Landau’s theorem”) capable
of establishing that particular functions change sign for arbitrarily large arguments. From this
proposition, the author shows that Π(x) − (li(x) − log 2) changes sign inﬁnitely often, as do the
diﬀerences ψ(x) − (x − log π
2 ) and Π
∗
r(x) − (log log x + C0) and ψr(x) − (log x − C0). Also, each of
the diﬀerences Πr(x; 4, 1) − ( 1
2 Li(x) − 1
2 log log x
log 2 − log 2) and Πr(x; 4, 3) − ( 1
2 Li(x) − 1
2 log log x
log 2 ) and
Πr(x; 4, 1, 3) + log 2 changes signs inﬁnitely often. Finally, the author establishes the assertion of
Chebyshev that 1 is a limit point of the function Eπ(x; 4, 3, 1).

This article cites [1].

[4] Mertens, F., ¨Uber eine zahlentheoretische Funktion, German, Sitzungsberichte Akad. Wien 106
(1897), 761–830.

The author publishes a table of the values of µ(n) and M (n) for n ≤ 10,000, using the formula
∑⌊
√n⌋
d=1 (
µ(d)⌊ n
d ⌋ + M ( n
d )
) = ⌊√
n⌋M (⌊√
n⌋) + 1 to check the output. Based on the table, the author
conjectures that |M (x)| < √
x for all x > 1. Using the formula ψ(x) = − ∑
n≤x µ(n)⌊ x
n ⌋ log n, the
author shows that M (x) ≪ √x would imply ∆
ψ(x) ≪ x
3/4 log x and ∆
Π(x) ≪ x
3/4 as well as RH,
and that M (x) ≪ √
x/(log x)
1+δ for some δ > 0 would imply that ζ(s) has no nontrivial zeros.

[5] Sterneck, R. D. von, Empirische Untersuchung ¨uber den Verlauf der zahlentheoretischen Funktion
σ(n) = ∑x=n
x=1 µ(x) im Intervalle von 0 bis 150000, German, Sitzungsberichte Akad. Wiss. Wien IIa
106 (1897), 835–1024.

The author provides a table of values for M (x). From the table, the author observes that |M (n)| <
1
2 √
n for 201 ≤ n ≤ 150,000, and conjectures that |M (x)| < √
x for all x > 1. The author also
compares M (x) with a random walk at the squarefree numbers, commenting that the corresponding

expectation of the absolute value of the random walk, namely √ 12
π2 √x ≈ 1.10266√
x, exceeds even
the maximal values of |M (x)| from the table.

This article cites [4].

[6] Sterneck, R. D. von, Bemerkung ¨uber die Summierung einiger zahlen-theoretischen Functionen,
Monatsh. Math. Phys. 9 (1898), no. 1, 43–45, MR1546543.

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 15

Using elementary methods, the author shows that |M (x)| < x/9 + 8 and |L(x)| < x/9 + √
x/2 + 7
for all x > 0.

[7] Sterneck, R. D. von, Empirische Untersuchung ¨uber den Verlauf der zahlentheoretischen Funktion
σ(n) = ∑x=n
x=1 µ(x) im Intervalle von 150000 bis 500000, German, Sitzungsberichte Kais. Akad.
Wissensch. Wien IIa 110 (1901), 1053–1102.

The author veriﬁes that |M (n)| < 1
2 √n for 201 ≤ n ≤ 500,000.

This article cites [5].

[8] Schmidt, E., ¨Uber die Anzahl der Primzahlen unter gegebener Grenze, German, Math. Ann. 57
(1903), no. 2, 195–204, MR1511206.

The author shows that ∆
Π(x) = Ω±(x
Θ−ε) for every ε > 0, and that both EΠ(x) > 1
29 and
EΠ(x) < − 1
29 occur inﬁnitely often. He also shows the same results with Π(x) in the deﬁnitions
of ∆
Π and EΠ replaced by π(x) + 1
2 Li(
√x).

[9] Stieltjes, T. J., Correspondance d’Hermite et de Stieltjes, French, Gauthier–Villars, Imprimeur–
Libraire, Paris, 1905, xxi+pp. 1–477.

In Lettre 79 (starting on page 160), the author states the conjectural bound |M (x)| ≤ √
x.

[10] Landau, E., ¨Uber einen Satz von Tschebyschef, German, Math. Ann. 61 (1906), no. 4, 527–550,
MR1511360.

Phragm´en [3] proved Chebyshev’s claim that 1 is a limit point of the function Eπ(x; 4, 3, 1), using
the theory of functions of complex arguments. The author of this article gives a simpler proof based
on the theory of Dirichlet series.

This article cites [8].

[11] Landau, E., Handbuch der Lehre von der Verteilung der Primzahlen. 2 B¨ande, German, Leipzig und
Berlin, B. G. Teubner, 1909, xviii+pp. 1–564, ix+pp. 565–961.

In Sections 199 and 200, the author generalizes his proof from [10], showing that (cq(b)− cq(a))/φ(q)
is a limit point of the function Eπ(x; q, a, b). He also shows that if c > √
1/4 + γ2
1 , where γ1 ≈ 14.1347
is the smallest ordinate of a nontrivial zero of ζ(s), then both EΠ(x) > 1
c and EΠ(x) < − 1
c
occur inﬁnitely often, as well as the same result with Π(x) in the deﬁnition of EΠ replaced by
π(x) + 1
2 Li(
√
x).

[12] Sterneck, R. D. von, Die zahlentheoretische Funktion σ(n) bis zur Grenze 5000000, German, Sitzungs-
berichte Kais. Akad. Wissensch. Wien IIa 121 (1912), 1083–1096.

The author calculates 16 selected values of M (n) with 600,000 ≤ n ≤ 5,000,000 and veriﬁes they
all satisfy |M (n)| ≤ 1
2 √
n. The computation uses the following formula, which is a reﬁned version
of a formula of Mertens [4]: for j = 1, 2, 3, 4, if n exceeds the product of the ﬁrst j primes, then
∑⌊
√n⌋
d=1 µ(d)ωj (n/d) + ∑d′ M (n/d) = ωj(
⌊√
n⌋)
M (
⌊√
n⌋)
, where ωj(x) is the number of positive
integers ≤ x that are not divisible by any of the ﬁrst j primes, and d
′ runs over all such numbers
≤ g. The author claims that the bound |M (n)| ≤ 1
2 √n for all n > 200 represents an unproved but
extremely probable number theoretic law, and thus RH could be also regarded as correct with a
high degree of probability (original German: “|M (n)| ≤ 1
2 √
n zwar ein unbewiesenes, aber ausseror-
dentlich wahrscheinliches zahlentheoretisches Gesetz darstellt, und somit auch die Riemann’sche
Vermutung mit einem hohen Grad von Wahrscheinlichkeit als richtig angesehen werden kann”).

This article cites [4, 5, 7].

[13] Sterneck, R. D. von, Neue empirische Daten ¨uber die zahlentheoretische Funktion σ(n), German,
Proc. 5th International Congress of Mathematicians 1 (1913), 341–343.

This is a summary of the previous three articles of the author.

This article cites [4, 5, 7, 12].

[14] Littlewood, J. E., Sur la distribution des nombres premiers, French, Comptes Rendus de l’Acad.
Sci. Paris 158 (1914), 1869–1872.

16 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

Assuming RH, the author shows that

∆
ψ(x) = Ω±(√
x log log log x
)

∆
π(x) = Ω±
( √
x log log log x
log x
 )
.

It follows that the conjectured inequality π(x) < Li(x) (“pr´esum´ee par divers auteurs pour des
raisons empiriques”) cannot hold for all values of x.

This article cites [11].

[15] Hardy, G. H. and Littlewood, J. E., On an assertion of Tchebychef, Proc. London Math. Soc. (2)
14 (1915), xv–xvi.

A letter of Chebyshev asserts that limx→∞ πe(x) = −∞. The authors verify the conjecture assuming
GRH for L(s, χ−4). Using a formula of Cahen and Mellin and an application of Cauchy’s theorem,
the authors show that −πe(x) ≫ √
x/ log x.

[16] Hardy, G. H., On Dirichlet’s divisor problem, Proc. London Math. Soc. (2) 15 (1916), 1–25,
MR1576550.

This article begins with a short background on the history of the Dirichlet divisor problem and states
the best bounds for ∆
D(x) available at the time, namely Voronoi’s result ∆
D(x) ≪ x
1/3 log x. The
author then proves that ∆
D(x) = Ω±(x
1/4). He draws a direct comparison to Schmidt’s proof [8]
that ∆
Π(x) = Ω±(
√
x/ log x), and to a simpliﬁed version of Schmidt’s proof by Landau [11]; he
states that his proof for ∆
D does not “diﬀer in principle” from Landau’s proof for ∆
Π, and for the
sake of comparison provides a simpliﬁed form of the proof that ∆
ψ(x) = Ω±(
√
x) based on Landau’s
methods.

The article then discusses various generalizations of the problem. The ﬁrst generalization discussed,
due to Piltz, concerns the same problem for Dk(x) = ∑n≤x τk(n), where τk(n) denotes the number
of ways n can be decomposed into k ordered factors: Hardy asserts that the methods in this article
can show that ∆
Dk (x) = Ω±(x
(k−1)/(2k)). The second generalization concerns R(x) = ∑
n≤x r(n),
where r(n) counts the number of ways n can be represented as the sum of two squares: Hardy
likewise asserts that ∆
R(x) = Ω±(x
1/4). Finally, the article concludes with a discussion of an
explicit formula for D(x), ﬁrst found by Voronoi, and some alternative proof methods and their
comparative advantages and disadvantages.

This article cites [11, 14].

[17] Hardy, G. H. and Littlewood, J. E., Contributions to the theory of the Riemann zeta-function and
the theory of the distribution of primes, Acta Math. 41 (1916), no. 1, 119–196, MR1555148.

This article contains full proofs of several results that had been announced by (at least one of) the
authors in the few years prior.

In Section 2.2, the authors obtain an explicit formula for the exponentially weighted sum ψe(x) −
1/(e1/x − 1) = ∑∞
n=1(Λ(n) − 1)e−n/x; furthermore, assuming RH, they show that this expression is
both ≪ √
x and Ω±(
√x). From the latter they deduce that ∆
ψ(x) = Ω±(
√
x). In Section 2.3, they
consider the function ∑p≥3(−1)
(p+1)/2e−p/x = −πe(x, χ−4). Assuming GRH for L(s, χ−4), they
prove that πe(x, χ−4) → −∞ as x → ∞, which is one way of justifying Chebyshev’s observation
that there are more primes congruent to 3 (mod 4) than to 1 (mod 4).

In Section 5, the authors provide a full proof of “Littlewood’s theorem” (announced in [14]) on
irregularities in the distribution of primes: they prove that

∆
π(x) = Ω±
( √x
log x log log log x
),

which in particular refutes the conjecture that π(x) < li(x) for all x > 1.

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 17

Their proof, which begins with the assumption of RH thanks to prior work of Landau [11, Sections
201–3], uses homogeneous Diophantine approximation for the imaginary parts of the zeros of ζ(s).
They assert that it can be shown in a similar way that ψ(x, χ−4) = Ω±(
√
x log log log x) and

π(x; 4, 3, 1) = Ω±
( √
x
log x log log log x
)
;

these results are actually dissonant with Chebyshev’s observations. (As a side remark, this is also
the article in which appears the proof of the asymptotic formula for the second moment of ζ(s) on
the critical line.)

This article cites [8, 11, 14, 15].

[18] Landau, E., ¨Uber einige ¨altere Vermutungen und Behauptungen in der Primzahltheorie, German,
Math. Z. 1 (1918), no. 2-3, 1–24, MR1544293.

Chebyshev asserted that πe(x, χ−4) → −∞ as x → ∞; the author shows that this assertion implies
GRH for L(s, χ−4). Assuming this GRH, he shows that π(x; 4, 3, 1) ≪ √
x log x. Assuming the
original assertion of Chebyshev, he proves that ∑p χ−4(p)f (p) converges whenever f (p) is strictly
decreasing and satisﬁes f (p) ≪ x
−1/2−δ for some δ > 0.

The author also examines the series
L′(s, χD)
L(s, χD) = − ∑

p
 χD(p) log p
ps − χD(p) ,

the identity originally valid for ℜs > 1; he shows that this series diverges at s = 1
2 , disproving a
conjecture of Lerch. Finally, the author shows that ∑∞
n=1 µ(n)/√
n diverges, disproving a conjecture
of Stieltjes, and also shows that M (x) = Ω(
√
x).

This article cites [1].

[19] Landau, E., ¨Uber einige ¨altere Vermutungen und Behauptungen in der Primzahltheorie, German,
Math. Z. 1 (1918), no. 2-3, 213–219, MR1544293.

The author gives a simpliﬁed proof of the result of Hardy and Littlewood [17, Section 2.3] that GRH
for L(s, χ−4) implies Chebyshev’s assertion πe(x, χ−4) → −∞ as x → ∞.

[20] P´olya, G., Verschiedene Bemerkungen zur Zahlentheorie, German, Jahresbericht der deutschen
Math.–Vereinigung 28 (1919), 31–40.

In Section III, the author empirically observes that L(n) ≤ 0 for 2 ≤ n ≤ 1500, with equality
only for n ∈ {2, 4, 6, 10, 16, 26, 40, 96, 586}; he explains some of these equalities as resulting from
imaginary quadratic ﬁelds Q(
√
−p) with class number 1. The author also notes that RH would
follow from the assertion that L(n) ≤ 0 for all large n. However, he does not formulate this as a
conjecture, saying only: “Ich teile diese Beobachtung mit, um evtl. weitere numerische Untersuchung
zu veranlassen. Der Bewies von [L(n) ≤ 0], sogar nur f¨ur hinreichend grosses n, w¨urde den Beweis
der Riemannschen Vermutung nach sich ziehen. . . .”.

This article cites [11].

[21] Cram´er, H., Ein Mittelwertsatz in der Primzahltheorie, German, Math. Z. 12 (1922), no. 1, 147–153,
MR1544509.

Under RH, the author shows that

lim
x→∞ 1
log x
 ∫ x

2
 ( ∆
ψ(t)
t
 )2 dt = ∑

ρ
 ∣
∣
∣
∣ nρ
ρ
 ∣
∣
∣
∣

2 ,

where nρ is the multiplicity of the zero ρ. It follows that Aψ
1 (x) ≪ x
3/2 (and the same for Aθ
1(x))
and thus that Aπ
1 (x) ≪ x
3/2/ log x (and the same for AΠ
1 (x)).

This article cites [11, 17].

[22] Littlewood, J. E., Mathematical Notes: 3; on a Theorem Concerning the Distribution of Prime
Numbers, J. London Math. Soc. 2 (1927), no. 1, 41–45, MR1574052.

18 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

The author shows that ∆
ψ(x) = Ω±(
√
x). The main idea is to examine the recursive sequence
of integrals Aψ
n (x); since x
−1Aψ
n(x) is an average of Aψ
n−1(x), it suﬃces to prove that Aψ
n(x) =
Ω±(x
n+ 1
2 ) when n is suﬃciently large.

This article cites [11].

[23] P´olya, G., ¨Uber das Vorzeichen des Restgliedes im Primzahltheorie, German, G¨ott. Nachr. (1930),
19–27.

The author proves that lim supT →∞ W ψ(T )/ log T ≥ γ1/π, where γ1 ≈ 14.1347 is the smallest
ordinate of a nontrivial zero of ζ(s). Indeed, γ1 can be replaced by the minimum positive ordinate of
the zeros of ζ(s) having maximal real part, or ∞ if no such zero exists. It was known for a long while
that this article contained an error that could be mended; the corrected version ﬁnally appeared
as [109].

This article cites [3, 8].

[24] Evelyn, C. J. A. and Linfoot, E. H., On a problem in the additive theory of numbers, Ann. of Math.
(2) 32 (1931), no. 2, 261–270, MR1502996.

Using Landau’s theorem, the authors show that ∆
Qk (x) = Ω±(x
1/2k).

This article cites [11].

[25] P´olya, G., On polar singularities of power series and of Dirichlet series, Proc. London Math. Soc.
(2) 33 (1931), no. 2, 85–101, MR1576856.

Let ω(u) be a real-valued function and set Φ(s) = ∫ ∞
1 ω(u)u−s du. If the number of sign changes
W ω(x) is O(log x), then a rightmost singularity σ + it of Φ(s) (that is, a singularity with σ maximal)
exists and satisﬁes 0 ≤ t ≤ lim supx→∞ πW ω(x)/ log x. This result generalizes Landau’s theorem,
which is the case W ω(x) ≪ 1.

[26] Ingham, A. E., The distribution of prime numbers, Cambridge Tracts in Mathematics and Mathe-
matical Physics. 30. London: Cambridge University Press, 1932, 114 pp.

In Chapter III of this book (Further Theory of ζ(s). Applications), the author shows how information
on the zero-free region of ζ(s) leads to improved estimates for ∆
ψ(x). Let η(t) be a real-valued
decreasing function deﬁned on t ≥ 0 satisfying 0 ≤ η(t) ≤ 1
2 and 1/η(t) = O(log t), and suppose
that η′(t) is continuous and η′(t) = o(1). If ζ(s) has no zeros in the region {σ > 1 − η(|t|)}, then for
any α ∈ (0, 1) we have ∆
ψ(x) ≪ x exp
(
− 1
2 αω(x)
), where ω(x) = mint≥1(
η(t) log x + log t)
.

Chapter V (Irregularities of Distribution) gathers known results on comparative prime number
theory from the literature. The author also outlines the proof of

π(x; 4, 3, 1) = Ω±
( √
x
log x log log log x
)
,

which was asserted by Hardy and Littlewood [17].

This book cites [3, 10, 11, 14, 17–19, 21–23].

[27] Skewes, S., On the Diﬀerence π(x) − li (x) (I), J. London Math. Soc. 8 (1933), no. 4, 277–283,
MR1573970.

This article shows, assuming RH, that π(x) > li(x) for some x < 1010
1034 . Littlewood [14, 17] proved
the existence of such an x by considering the function F (ξiη) = ∑
γ>0 e−γ(ξ+iη)/γ for 0 ≤ ξ ≤ 1
and η ≥ 1, which is relevant since the explicit formula yields −2ℑF (i log x) = Eψ(x) + O(1). Using
the Dirichlet box principle, Littlewood showed that ℑF (ξ + iη) has large values (on the order of
log log η) of either prescribed sign, with ξ tending to 0, and then used a modiﬁed form of the
Phragm´en–Lindel¨of principle to show that an equally large value of −ℑF (iη) must be attained.

The Phragm´en–Lindel¨of principle, that the maximum of an analytic function deﬁned on a semi-
inﬁnite strip (with suitable growth conditions) must occur on the boundary of the strip, is only
an existence result; the author strengthens the result to give quantitative bounds on when an
approximation to an interior value is attained on the boundary of the strip. In this way he is able
to make Littlewood’s result explicit (although the details are not included), which was not clearly
possible beforehand.

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 19

(Estimates of the smallest x such that π(x) > li(x) have since been called “Skewes numbers”. For
comparison, the best estimates today are about 1.4 × 10316.)

This article cites [26].

[28] Jessen, B. and Wintner, A., Distribution functions and the Riemann zeta function, Trans. Amer.
Math. Soc. 38 (1935), no. 1, 48–88, MR1501802.

This article contains a systematic study of inﬁnite convolutions of distribution functions (densities)
on Rk, and consequently of inﬁnite sums of independent random variables, via their Fourier trans-
forms; they give criteria for when these convolutions converge and when the result is singular or
absolutely continuous. They analyze distributions of functions on convex closed curves in R2. The
results are applied to the limiting distribution functions of almost-periodic functions of multiple
types. As an application, the authors derive results on the limiting distributions of log ζ(σ + it) and
ζ(σ + it) for 1
2 < σ ≤ 1 (the case σ > 1 being simpler).

[29] Wintner, A., On the asymptotic distribution of the remainder term of the prime-number theorem,
Amer. J. Math. 57 (1935), no. 3, 534–538, MR1507933.

Assuming RH, the author investigates the tail ∑|ρ|>T x
iγ/ρ of the sum appearing in the explicit
formula for ψ(x), showing that its mean-square average tends to 0 as T → ∞. This implies that the
full sum converges (and represents, in the Besicovitch sense, the function of which it is the “Fourier
series”) and has a logarithmic distribution function. The author also mentions the potential relevance
of LI to whether this distribution function can be constant on intervals.

This article cites [28].

[30] Ingham, A. E., A note on the distribution of primes, Acta Arith. 1 (1936), 201–211.

This article gives another proof of an explicit version of Littlewood’s theorem [17] and establishes
the following stronger result: Assuming SA for ζ(s), there exists an absolute constant A > 1 such
that, for all x > 1, the interval (x, Ax) contains a sign change of π(x) − Li(x). The author highlights
his use of Fej´er kernels in the proof, in contrast with the Poisson kernel used by Skewes [27].

This article cites [17, 23, 27].

[31] Littlewood, J. E., Mathematical Notes (12): An Inequality for a Sum of Cosines, J. London Math.
Soc. 12 (1937), no. 3, 217–221, MR1575079.

This short note is mathematically concerned with the maximum values of trigonometric polynomials.
The author reveals that his motivation was to establish an explicit upper bound for the ﬁrst sign
change of ∆
π(x) without assuming RH. Ultimately, the author claims to have found alternative
means for ﬁnding such an upper bound.

This note cites [27].

[32] Wintner, A., Asymptotic distributions and inﬁnite convolutions, Lecture notes distributed by the
Institute for Advanced Study (Princeton) (1938).

The chapter titles are: 1. Distribution functions; 2. Integrals and convolutions; 3. Moments of dis-
tribution functions; 4. Fourier transforms; 5. Inﬁnite convolutions; 6. Smoothness criteria for dis-
tribution functions; 7. Convergence criteria for inﬁnite convolutions; 8. Asymptotic distributions;
9. The Riemann zeta-function; 10. Poisson convolutions; 11. Convolutions and the theory of proba-
bility; 12. Bernoulli convolutions; 13. Almost periodic functions with linearly independent exponents;
14. Symmetric distribution functions in k dimensions; 15. Two-dimensional convolutions and the
Riemann zeta-function; 16. The addition of convex curves.

These notes cite [28, 29].

[33] Gupta, H., On a table of values of L(n), Proc. Indian Acad. Sci., Sect. A. 12 (1940), 407–409,
MR0003644.

Regarding P´olya’s problem, the author veriﬁes that L(n) ≤ 0 for 2 ≤ n ≤ 20,000. The author also
conjectures that L(x) ≪ √x based on the computation.

This article cites [20].

20 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

[34] Wintner, A., On the distribution function of the remainder term of the prime number theorem,
Amer. J. Math. 63 (1941), 233–248, MR0004255.

This article investigates the normalized remainder term EΨ(x) by establishing the existence of its
limiting logarithmic cumulative distribution function. Assuming RH, the author proves that the
spectrum of this limiting distribution is unbounded both above and below, which implies the same
for EΨ(x). He also gives an estimate for all of the moments of this limiting distribution, in an eﬀort
to determine whether these moments uniquely determine the given distribution.

The techniques involved in the proof come primarily from the application of the theory of almost-
periodic functions (of both the uniform and Besicovitch varieties) to the sum over the nontrivial
zeros in the fundamental explicit formula.

This article cites [26, 28, 29].

[35] Ingham, A. E., On two conjectures in the theory of numbers, Amer. J. Math. 64 (1942), 313–319,
MR0006202.

The author probes conjectured bounds for the summatory functions M (x) and L(x). He proves
that the truth, for suﬃciently large x, of any one of the inequalities M (x) < Kx
1/2, M (x) >
−Kx
1/2, L(x) < Kx
1/2, or L(x) > −Kx
1/2 (where K is a constant) would imply not only RH and
the simplicity of the zeros of ζ(s) (as was “well known”), but also the falsity of LI. Of this last
assumption, the author writes: “It would be easy to relax this hypothesis a little, but there seems
no obvious way of replacing it by anything essentially easier to verify.” Indeed, he shows that if
there are only ﬁnitely many rational linear relations among the positive imaginary parts of these
zeros, then EM (x) and EL(x) would be unbounded both above and below, contrary to existing
conjectures.

The method of the proof is similar to Littlewood’s disproof of the conjecture π(x) < li(x) in [17],
including a reliance on trigonometric polynomials involving the zeros of ζ(s), except that Dirich-
let’s theorem on homogeneous Diophantine approximation is replaced by Kronecker’s theorem on
inhomogeneous Diophantine approximation. For the proof, the author establishes two main results,
one concerning Laplace transforms of real trigonometric polynomials, and the other establishing the
divergence (assuming RH) of the two residue series ∑γ>0 1/ρζ′(ρ) and ∑
γ>0 ζ(2ρ)/ρζ′(ρ).

This article cites [4, 5, 7, 9, 13, 20, 33].

[36] Tietze, H., Einige Tabellen zur Verteilung der Primzahlen auf Untergruppen der teilerfremden Restk-
lassen nach gegebenem Modul, German, Abh. Bayer. Akad. Wiss. Math.-Nat. Abt. (N.F.) 1944
(1944), no. 55, 31, MR0017310.

The author provides tables of φ(q)π(x; q, A, Γ) for various moduli q (with a particular focus on q =
262, the smallest even modulus for which 3, 5, 7, 11, 13 are all quadratic residues) and various sets Γ
of residue classes, often subgroups of A.

[37] Tur´an, P., On some approximative Dirichlet-polynomials in the theory of the zeta-function of Rie-
mann, Danske Vid. Selsk. Mat.-Fys. Medd. 24 (1948), no. 17, 36, MR27305.

The author shows that if there exists a positive constant K such that Lr(x) > −K/√
x for suﬃciently
large x, then RH holds. The author also reports that Lr(x) ≥ 0 for x ≤ 1,000. While people often
refer to the statement that Lr(x) is never negative as “Tur´an’s conjecture”, that claim is never
made in this article.

This article cites [20, 23, 33].

[38] Wintner, A., A note on Mertens’ hypothesis, Rev. Ci. (Lima) 50 (1948), 181–184, MR29414.

The author shows that M (x) ≪ √
x is equivalent to ∑n≤x µ(n)
√n ≪ 1; the forward direction follows
from partial summation, while the converse uses a Tauberian theorem due to Riesz.

[39] Tur´an, P., On the remainder-term of the prime-number formula. II, English, with Russian summary,
Acta Math. Acad. Sci. Hungar. 1 (1950), 155–166, MR0049219.

The author shows that if ∆
π(x) ≪ x exp(
−a(log x)
1/(1+β)) for some constants a > 0 and 0 < β < 1,
then there exists a constant b > 0 such that ζ(s) does not vanish in the domain σ > 1 − b/log
β |t|;

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 21

this is the converse of a special case of a theorem of Ingham. The main tool of the proof is a version
of the “second main theorem” of the power-sum method (the statement in the article seems to
contain the typo max |zj| ≥ 1 instead of max |zj| ≤ 1) for longer ranges of the exponent.

This article cites [26].

[40] Tur´an, P., On the remainder-term of the prime-number formula. I, English, with Russian summary,
Acta Math. Acad. Sci. Hungar. 1 (1950), 48–63, MR0043121.

This article investigates lower bounds for |∆
ψ(x)| and |∆
π(x)|, speciﬁcally to answer Littlewood’s
call [31] to replace Landau’s theorem, which depends upon the smallest half-plane containing all
the zeros of ζ(s), by an estimation that depends only upon one single zero ρ0 = β0 + iγ0 of ζ(s).
The author shows, using a version of his “ﬁrst main theorem”, that when T is suﬃciently large in
terms of ρ0,
 max
1≤x≤T |∆
ψ(x)| > T β0

|ρ0|(10 log T )/ log log T exp (
− c log T log log log T
log log T
 ) ,

where c is a positive constant depending on ρ0.

This article cites [8, 14, 17, 23, 30, 31, 46, 65].

[41] Fawaz, A. Y., The explicit formula for L0(x), Proc. London Math. Soc. (3) 1 (1951), 86–103,
MR43841.

Assuming RH and the simplicity of the zeros of ζ(s), the author records the identity

L0(x) = √
x
ζ( 1
2 ) + ∑

ρ
 ζ(2ρ)
ρζ′(ρ) x
ρ + 1
2πi
 ∫ 1/4+i∞

1/4−i∞
 ζ(2s)
sζ(s) x
s ds.

By a more delicate argument, he establishes the more explicit series representation

1
2πi
 ∫ 1/4+i∞

1/4−i∞
 ζ(2s)
sζ(s) x
s ds = 2
 ∞∑

n=1
 q(n)λ(n)
n (
C(
√nx) + S(
√
nx)
)
,

where q(n) is the largest integer whose square divides n, and C(t) and S(t) are the normalized
Fresnel integrals, which both tend to 1
2 as t → ∞. With these identities, the author indicates a
possible approach to resolving P´olya’s problem in the negative.

This article cites [11, 20, 30, 35].

[42] Titchmarsh, E. C., The Theory of the Riemann Zeta-Function, Oxford, at the Clarendon Press,
1951, pp. vi+346, MR0046485.

This is the ﬁrst edition of [186].

[43] Fawaz, A. Y., On an unsolved problem in the analytic theory of numbers, Quart. J. Math. Oxford
Ser. (2) 3 (1952), 282–295, MR51857.

This article is a continuation of the author’s previous work [41]. Deﬁning

I(x) = 1
2πi
 ∫ a+i∞

a−i∞
 ζ(2s)
sζ(s) x
s ds

for any a ∈ (0, 1
2 ), the author proves that

lim inf
x→∞ EL(x) = − lim sup
x→0+ I(x)
√
x and lim sup
x→∞ EL(x) = − lim inf
x→0+ I(x)
√x ,

which suggests an alternative approach to studying L(x).

This article cites [20, 26, 30, 33, 35, 41, 42].

[44] Landau, E., Handbuch der Lehre von der Verteilung der Primzahlen. 2 B¨ande, German, 2d ed; With
an appendix by Paul T. Bateman, Chelsea Publishing Co., New York, 1953, xviii+pp. 1–564, ix+pp.
565–1001, MR0068565.

This is the second edition of [11].

22 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

[45] Tur´an, P., Eine neue Methode in der Analysis und deren Anwendungen, German, Akad´emiai Kiad´o,
Budapest, 1953, 196 pp., MR0060548.

This book contains a coherent exposition of the power-sum method which is also referred as “Tur`an’s
method”. Many applications of the method are given, including a result that derives zero-free regions
from bounds for Eψ(x) and improved zero-density results.

[46] Skewes, S., On the diﬀerence π(x)−li x. II, Proc. London Math. Soc. (3) 5 (1955), 48–70, MR0067145.

This article provides an unconditional explicit estimate for a sign change of the diﬀerence ∆
π(x):

if we deﬁne X1 = ee
e7.703 and X2 = e4X 30
1 < ee
ee7.705 < 1010
10103 , then the author shows that there
exists some x < X2 such that π(x) > li(x). The author divides the proof into two cases, ﬁrst when RH
is “nearly true” and then the contrary case. More speciﬁcally, he deﬁnes a hypothesis (H) (the “nearly
true” case) as follows: Every zero ρ = β + iγ for which |γ| < X 3
1 satisﬁes β − 1
2 ≤ X −3
1 log−2 X1.

For the case where (H) holds, the author modiﬁes Ingham’s technique from [30], which assumed
RH but improved the estimation of ∆
ψ0 (x) by showing that zeros with γ large relative to x do not
contribute meaningfully to the sum. Ultimately the author’s argument boils down to estimation
of the sum ∑0<γ<500 sin γω
γ (
1 − γ
500 )
; Dirichlet’s box principle is used again, in conjunction with
estimates of the values of the 269 zeros of ζ(s) with 0 < γ < 500.

For the contrary case, which the author calls (NH), he remarks that it no longer suﬃces to work
ﬁrst with ψ(x) and then pass to π(x) with standard partial summation techniques. Instead, he
works directly from the explicit formula for ∆
Π0(x), introducing a smoothing factor to amplify
the contribution from the hypothesized (H)-violating zero. Throughout, the author uses explicit
estimates for sums over nontrivial zeros of ζ(s), such as |N (T + h) − N (T )| < 1
2π (h + 1.77) log T + 8.7
for 7.1 < h < T
2 .

This article cites [14, 26, 27, 30].

[47] S´os, V. T. and Tur´an, P., On some new theorems in the theory of Diophantine approximations,
English, with Russian summary, Acta Math. Acad. Sci. Hungar. 6 (1955), 241–255, MR0077579.

The authors give bounds for the valid constants A and B appearing in the ﬁrst and second main
theorems of the power-sum method. It is known that A = 2e is valid in the ﬁrst main theorem, and
the authors show that A = 4
π is too small. They also show that B = 2e1+4/e is valid in the second
main theorem (improving the previous B = 24e2) while B = 1.321 is not; they mention that the
improvement in the upper bound leads to improved constants in a zero-density theorem for ζ(s) and
in the maximal gap between primes. The authors also refer to a “third main theorem”, in which the
normalized lower bound for the power-sum is independent of the bj rather than of the zj.

This article cites [45].

[48] Leech, J., Note on the distribution of prime numbers, J. London Math. Soc. 32 (1957), 56–58,
MR0083001.

The author uses the EDSAC at Cambridge to compute π(x; 4, 1) and π(x; 4, 3) for x up to 3×106. He
discovers that π(x; 4, 1) > π(x; 4, 3) at x = 26,861, for which π(x; 4, 1) = 1,473 and π(x; 4, 3) = 1,472.
The other values of x above 26,863 for which π(x; 4, 1) > π(x; 4, 3) are between 616,000 and 634,000;
the greatest diﬀerence found is at x = 623,681, for which π(x; 4, 1) = 25,444 and π(x; 4, 3) = 25,436.

The author notes that πi(x) = 2π(x; 4, 1) + π(
√x; 4, 3) + 1, the number of Gaussian primes with
norm at most x (up to associates, and for x ≥ 2), is consequently large near this latter range as
well; the most extreme value found is at x = 617,537, for which πi(x) = 50,509 ≈ li(x) + 19.5.

When examining the explicit formula for π(x; 4, 3, 1) at x = 620,000, the author found that the
ﬁrst 20 pairs of zeros of L(s, χ−4), whose imaginary parts ranged from ±6.020948 to ±49.723129,
included 16 pairs that give negative contributions to the explicit formula, while subsequent zeros
gave more or less random contributions.

This article cites [26, 27].

[49] Prachar, K., Primzahlverteilung, German, Springer-Verlag, Berlin-G¨ottingen-Heidelberg, 1957, x+415
pp. MR0087685.

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 23

The contents of this book are divided into the following ten main chapters, plus an Appendix
that provides additional background on topics such as partial summation and the Γ-function. The
chapters are: I. Elementary results; II. Sieve methods; III. The prime number theorem; IV. Primes
in an arithmetical progression; V. Diﬀerent applications; VI. The Goldbach problem; VII. Function
theoretic properties of the L-functions. Explicit formulae and their applications; VIII. Trigonometric
sums; IX. Theorems on the density of zeros of the L-functions and their application in prime number
theory; X. The smallest prime in an arithmetical progression.

[50] Bateman, P. T. and Grosswald, E., On a theorem of Erd¨os and Szekeres, Illinois J. Math. 2 (1958),
88–98, MR95804.

Let N (x) be the number of squarefull numbers up to x, and let the corresponding error term be
∆
N (x) = N (x) − (
ζ( 3
2 )x
1/2/ζ(3) + ζ( 2
3 )x
1/3/ζ(2)
)
. In this article, the authors show that if ρ is any
zero of the Riemann zeta function such that ζ( ρ
2 ) ̸= 0 and ζ( ρ
3 ) ̸= 0, then ∆
N (x) = Ω±(x
ℜ(ρ)/6).

This article cites [11, 24, 42].

[51] Haselgrove, C. B., A disproof of a conjecture of P´olya, Mathematika 5 (1958), 141–145, MR0104638.

Following Ingham’s method [35], the author resolves P´olya’s problem in the negative by showing
that a truncated version of the explicit formula for EL(x), using zeros of ζ(s) up to height 1,000, is
positive at x = e831.847; while this does not rigorously establish that EL(e831.847) is itself positive,
the truncated value is a lower bound for lim supx→∞ EL(x). Similarly, the author resolves Tur´an’s
problem in the negative by showing that the analogous truncation of the explicit formula for ELr (x)
is negative at x = e853.853. The computations were carried out on an EDSAC I and a Mark I.

This article cites [4, 20, 35, 37].

[52] Knapowski, S., On prime numbers in an arithmetical progression, Acta Arith. 4 (1958), 57–70,
MR0096622.

This article begins by recalling that ∆
π(x; q, 1) ≪ε x
θ+ε implies ∆
π(x; q, a) ≪ε x
θ+ε for all (a, q) =
1. The author establishes an explicit inequality relating the two, namely that

max
x≤T |∆
π(x; q, a)| ≤ T δ(T ) exp ( (1 + q−1) log T
√log log T
 )
( max
x≤T |∆
π(x; q, 1)| + φ(q)
√T )
.

Here δ(T ) = ε(
√T )−ε( exp(
√log log T )
)
, where ε(H) is the largest real part of the zeros of ζ(s) up to
height H; in particular, δ(T ) is eventually identically 0 assuming SA, and δ(T ) → 0 unconditionally.
The author derives this result from the analogous result for ∆
ψ(x; q, a), which does not contain the
term φ(q)
√T ; he remarks upon a similar result for ∆
Π(x; q, a) assuming SA.

This article cites [11, 45].

[53] Knapowski, S., On the M¨obius function, Acta Arith. 4 (1958), 209–216, MR0096630.

The author proves that the assumption ∫ T
1 (M (x)/x)
2 dx ≪ log T , which is stronger than the
Mertens conjecture and is known to imply both RH and the simplicity of the zeros of ζ(s), also
implies that M (x) = Ω(
x
1/2 exp(−log x/√
log log x)
)
.

This article cites [45].

[54] Wintner, A., On the λ-variant of Mertens’ µ-hypothesis, Amer. J. Math. 80 (1958), 639–642,
MR98723.

The author considers an analogue of the weak Mertens conjecture for the summatory function of the
Liouville function. The author shows that L(x) ≪ √x is equivalent to ∑n≤x λ(n)/√
n = c log x + O(1),
where c = 1/ζ(1/2) < 0. The proof follows the similar lines as of the author’s earlier work [38].

This article cites [35, 38].

[55] Knapowski, S., On the mean values of certain functions in prime number theory, English, with Rus-
sian summary, Acta Math. Acad. Sci. Hungar. 10 (1959), 375–390. (unbound insert), MR0111722.

24 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

The author continues his work in [53] by considering lower bounds for the logarithmic averages
A
ψ
|1|(x) and A
M
|1|(x). The author shows that if ρ0 = β0 + iγ0 is a zero of ζ(s), then

A
ψ
|1|(x) > x
β0 exp (
−14 log x
√
log log x
 )

when x is suﬃciently large in terms of |ρ0|. He also shows that the conjectured upper bound
A
M
|1|(x) ≪ √
x actually implies the lower bound

A
M
|1|(x) > √
x exp (
− log x
√
log log x
 )

when x is suﬃciently large.

This article cites [40, 44, 45, 47, 53].

[56] Shanks, D., Quadratic residues and the distribution of primes, Math. Tables Aids Comput. 13
(1959), 272–284, MR0108470.

The author investigates Chebyshev’s assertion that there are more primes of the form 4m − 1
than of the form 4m + 1. Deﬁne τ (n) = π(n; 4, 3, 1)
√
n/π(n) (which is asymptotically equivalent
to π(n; 4, 3, 1) log n/√
n but is easier to manipulate numerically). Upon computing π(n; 4, 3, 1) for
values of n up to 3 million, he analyzes the values τ (1,000k) for 1 ≤ k ≤ 2,000, noting that their
histogram is “roughly normal with a mean of (nearly) 1”. The author conjectures that

lim
x→∞ 1
x
 ∑

n≤x τ (n) = lim
x→∞ 1
x
 ∑

n≤x
 π(x; 4, 3, 1)
√
n
π(n) = 1,

and notes that weaker versions of the conjecture—namely, that the above limit holds under GRH
for L(s, χ−4), or that the above limit either equals 1 or fails to exist—are also open. (He can show,
under GRH, that the mean value inside the limit is positive and bounded away from 0 for suﬃciently
large x.)

Next, the author discusses the distribution of primes in the residue classes modulo 8, 10, and 12. Both
from examining the collected data and from combinatorial reasoning involving the multiplicative
groups of those moduli, he concludes that the quadratic residues are the ones with a smaller number
of primes (on average). For the speciﬁc modulus 4, he outlines an argument, based on combinatorial
reasoning with the quantities #{n ≤ x : Ω(n) = a, n ≡ ±1 (mod 4)}, that shows that the mean value
of τ (n) should be 1. Indeed, he remarks that the generalization of this mean value to the integers
with a prime factors (counted with multiplicity) predicts that it is the residue class (−1)
a (mod 4)
that should have more such integers; in other words, the bias switches according to the parity of
the number of prime factors. A related remark is that there is a bias towards integers for which
(−1)
Ω(n)χ−4(n) equals 1 over those for which it equals −1.

This article ends with a discussion of how similar arguments to those laid out in this article could
be used to analyze the relationship between π(x) and li(x).

This article cites [1, 3, 10, 17, 27, 44, 48].

[57] Tur´an, P., Nachtrag zu meiner Abhandlung “On some approximative Dirichlet polynomials in the
theory of zeta-function of Riemann”, Acta Math. Acad. Sci. Hungar. 10 (1959), 277–298 (unbound
insert), MR115977.

The main topic of this article is the connection between RH and zeros of partial sums of the
series for ζ(s). Herein, however, the author mentions that the assertion that Lr(x) is nonnegative
(eventually or even always) has been called “Tur´an’s conjecture”, but that he never made such a
claim even implicitly. The exact quote, in which “1” refers to [37] and “(3.2)” refers to the inequality
Lr(x) ≥ 0, is: “Merkw¨urdigerweise bezeichnetendie an 1 anschließenden Arbeiten schlechthin (3.2)
als ,,Tur insche Vermutung“, sogar f¨ur n ≥ 1 behauptet. (3.2) kommt in 1 nirgends vor, f¨ur n ≥ 1
nicht einmal implizite behauptet.”

This article cites [10, 37, 42, 51].

[58] Knapowski, S., Contributions to the theory of the distribution of prime numbers in arithmetical
progressions. I, Acta Arith. 6 (1960/1961), 415–434, MR0125822.

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 25

Assuming GRH(q7), the author shows that
∫ T

T exp(−(log T )3/4)
 |∆
ψ(x; q, a)|
x dx > φ(q)T 1/2 exp (
− 2 log T
log log T
 )

when T is suﬃciently large in terms of q, which in particular implies an Ω-result for ∆
ψ(x; q, a).
Unconditionally the right-hand side can be replaced by T 1/4.

This article cites [45, 49, 52].

[59] Lehman, R. S., On Liouville’s function, Math. Comp. 14 (1960), 311–320, MR0120198.

The author describes computations leading to an explicit counterexample to P´olya’s problem, show-
ing that L(906,180,359) = 1 is a small value for which the inequality fails. In order to speed up the
computation for L(x), which was performed on an IBM 704 at Berkeley, the author uses (a slightly
more complicated version of) the recursive formula

L(x) = ∑

m≤x/m µ(m)
⌊√ x
m
 ⌋ − ∑

k<v λ(k)
(⌊ x
km
 ⌋ − ⌊ x
mv
 ⌋) − ∑

x/w<l≤x/v L( x
l
 ) ∑

m|l
m≤x/w
 µ(m).

The author uses a conditional truncated explicit formula for a weighted variant of L(eu) to identify
promising candidates for positive values of L(x).

This article cites [12, 20, 26, 35, 41, 43, 51].

[60] Lehmer, D. H. and Selberg, S., A sum involving the function of M¨obius, Acta Arith. 6 (1960), 111–
114, MR115965.

Using Landau’s Theorem, the authors show that AMr
1 (x) − K changes signs inﬁnitely often for any
constant K. Numerical calculations show that the ﬁrst 56 sign changes of AMr
1 (x) − 2 are nearly in
a geometric progression, and a heuristic explanation of this phenomenon is derived from the explicit
formula AMr
1 (x) − 2 = − ∑ x
ρ/ρ(1 − ρ)ζ′(ρ).

[61] Sta´s, W., ¨Uber die Umkehrung eines Satzes von Ingham, German, Acta Arith. 6 (1960/1961), 435–
446, MR0146153.

Ingham [26] showed that any precise information on the zero-free region of ζ(s) would lead to a
correspondingly precise estimate on ∆
ψ(x). The author uses the power-sum method to obtain a
partial converse of this theorem. As an illustration, the author shows that ∆
ψ(x) ≪ x/(log x)
1/10

would imply that ζ(s) ̸= 0 in the region σ > 1 − 1
400 (log t)t−20 when t is suﬃciently large.

This article cites [26, 45].

[62] Knapowski, S., Contributions to the theory of the distribution of prime numbers in arithmetical
progressions. II, Acta Arith 7 (1961/1962), 325–335, MR0142520.

Assuming GRH(q7), the author shows that
∫ T

T exp(−(log T )3/4)
 |ψ(x; q, a1, a2)|
x dx > T 1/2 exp (
− 2 log T
log log T
 )

when T is suﬃciently large in terms of q, and the analogous result with ψ replaced by Π. (Uncon-
ditionally the right-hand side can be replaced by T 1/4.) If both a1 and a2 are nonsquares (mod q),
then the same result holds for π as well.

This article cites [49, 58].

[63] Knapowski, S., Mean-value estimations for the M¨obius function. I, Acta Arith. 7 (1961), 121–130,
MR0133287.

Supposing that A
M
|1|(T ) < aT 1/2 for T ≥ 1, the author exhibits a constant H(a) such that
∫ T

T /H(a)
 |M (x)|
x dx > T 1/2

H(a) .

for T ≥ H(a), reﬁning a theorem from [55] by following an idea due to Ingham in a letter to Tur´an.
The author also states another theorem which is proved later in [64].

26 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

This article cites [53, 55, 64].

[64] Knapowski, S., Mean-value estimations for the M¨obius function. II, Acta Arith. 7 (1961), 337–343,
MR0142500.

This article presents a proof of the theorem which was announced in [63]: When T is suﬃciently
large, RH(ω) implies that for T ≤ exp(ω10).
∫ T

T exp(−100 log T
log log T log log log T )
 |M (x)|
x dx > T 1/2 exp
(
−12 log T
log log T log log log T )
.

This article cites [45, 58, 63].

[65] Knapowski, S., On sign-changes in the remainder-term in the prime-number formula, J. London
Math. Soc. 36 (1961), 451–460, MR0133309.

The author shows that if ρ0 = β0 + iγ0 is any zero of ζ(s), then for T suﬃciently large in terms
of γ0,
 ∆
ψ(t) = Ω±
(
tβ0 exp ( −15 log t
√log log t
 ))
,

and the same for ∆
Π(t) (which implies an Ω−-result, though not an Ω+-result, for ∆
π(t)). A slightly
more precise version of this result implies that lim inf T →∞ W ψ(T )/ log log T ≥ 1/ log 2.

This article cites [30, 40, 46].

[66] Knapowski, S., On sign-changes of the diﬀerence π(x) − li x, Acta Arith. 7 (1961/1962), 107–119,
MR0133308.

This article is concerned with explicit lower bounds for the number W (T ) of sign changes of the func-
tion li(x)−π(x). Previously, Ingham [30] had shown, assuming SA, that lim inf T →∞ W (T )/log T > 0,
while the author [65] had proved unconditionally that lim inf T →∞ W (T )/log log T > 0. Skewes [46]

famously found that W (
ee
ee7.705 ) ≥ 1.

In this article, the author shows unconditionally that W (T ) ≥ e−35 log log log log T for T ≥ ee
ee35

(the author did not try to optimize these constants). Similar to [46], the proof is divided into
two cases, ﬁrst when RH is “nearly true” and then the contrary case. More speciﬁcally, setting
X = 7√
log log T , the author deﬁnes a hypothesis (C) (the “nearly true” case) as follows: Every zero
ρ = β +iγ for which |γ| ≤ X 3 satisﬁes β − 1
2 ≤ 2/(3X 3 log X). The author then proves the inequality
above ﬁrst assuming (C) and then again assuming its negation (NC).

This article cites [14, 26, 46, 65].

[67] Knapowski, S. and Sta´s, W., A note on a theorem of Hardy and Littlewood, Acta Arith. 7 (1961/1962),
161–166, MR0131410.

The authors examine the function ∆
ψe (x) = ∑∞
n=1(Λ(n) − 1)e−n/x. They prove, unconditionally
and eﬀectively, that
 max
1≤y≤x |∆
ψe (y)| > x
1/2 exp (
− 4 log x log log log x
log log x
 )

when x is suﬃciently large. The main tool of the proof is a version of the second main theorem of
the power-sum method.

This article cites [17, 45, 58].

[68] Tur´an, P., On some further one-sided theorems of new type in the theory of Diophantine approx-
imations, English, with Russian summary, Acta Math. Acad. Sci. Hungar. 12 (1961), 455–468,
MR0132728.

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 27

The author establishes a “one-sided” version of the second main theorem of the power-sum method
with an argument restriction. Let m be a nonnegative integer and choose 0 < α ≤ π
2 , and suppose
that z1, . . . , zn are complex numbers satisfying 1 = |z1| ≥ |z2| ≥ · · · ≥ |zn| and | arg(zj)| > α, and
that b1, . . . , bn are complex numbers with min1≤µ≤n ℜ ∑µ
j=1 bj > 0. Then there exists an integer
m + 1 ≤ v ≤ m + n(3 + π
α ) such that

ℜ
 n∑

j=1 bjzv
j ≥ 1
2n + 1
 ( n
24e3(m + n(3 + π
α ))
 )2n min
1≤µ≤n ℜ
 µ∑

j=1 bj,

with the analogous result for −ℜ ∑n
j=1 bjzv
j .

This article cites [45].

[69] Knapowski, S., Contributions to the theory of the distribution of prime numbers in arithmetical
progressions. III, Acta Arith 8 (1962/1963), 97–105, MR0142521.

Assuming GRH(q7), the author shows that
∫ T

T exp(−(log T )3/4)
 |π(x; q, a1, a2)|
x dx > T 1/2 exp (
− 7 log T
log log T
 )
;

unlike in his earlier work, one no longer needs to assume that a1 and a2 are nonsquares.

This article cites [45, 49, 58, 62].

[70] Knapowski, S., On oscillations of certain means formed from the M¨obius series. I, Acta Arith. 8
(1962/1963), 311–320, MR0155802.

Assuming RH(H) (but with no assumptions on the simplicity of zeros of ζ(s)), the author shows
that
 max
1≤x≤T M (x) > √
T exp (
− 15 log T log log log T
log log T
 )

for T ≤ eH10 , and similarly for −M (x); in the same range he deduces that W (M, T ) ≫ log T .

This article cites [53, 55, 63, 65, 68, 73].

[71] Knapowski, S. and Tur´an, P., Comparative prime-number theory. I. Introduction, Acta Math. Acad.
Sci. Hungar. 13 (1962), 299–314, MR0146156.

The authors start by introducing ten problems of interest in “comparative prime-number theory” to
the modulus k, the ﬁrst seven concerning the sign changes and extreme values of π(x; k, ℓ1, ℓ2)
and the natural density of the solutions to π(x; k, ℓ1, ℓ2) > 0. The eighth problem, which the
authors call the “race-problem of Shanks–R´enyi” (which is perhaps the ﬁrst time R´enyi’s name
was linked to comparative prime number theory) is whether there are arbitrarily large solutions
x to π(x; k, ℓ1) < · · · < π(x; k, ℓφ(k)); the last two problems concern the simultaneous inequalities
π(x; k, ℓj) > 1
φ(k) li(x).

The authors allude to variants of these ten problems generated by replacing π(x; k, ℓ) by πe(x; k, ℓ)
(and, where needed, Li(x) by ∫ ∞
2 e
−t/x
log t dt), and further vary these problems by replacing π with
ψ or Π. They are aware that such problems could be further varied (“. . . the analogous problems
concerning the distribution of primes in binary quadratic forms with ﬁxed discriminant or of the
prime ideals of a ﬁxed ﬁeld in various idealclasses”).

In Section 4, the authors discuss how some of the problems involving ψ(x; k, ℓ) can be conditionally
solved using Landau’s theorem (and hence unconditionally for moduli dividing 24). In Section 5,
the authors discuss the results they have so far concerning the problems involving π(x; k, ℓ), and in
Section 8, they brieﬂy discuss what is known about prime number races modulo 4. Throughout the
rest of this article, the authors introduce the results that will be proved in the next seven articles
of the series.

This article cites [1, 3, 17, 23, 30, 46, 56].

[72] Knapowski, S. and Tur´an, P., Comparative prime-number theory. II. Comparison of the progressions
≡ 1 mod k and ≡ l mod k, l ̸≡ 1 mod k, Acta Math. Acad. Sci. Hungar. 13 (1962), 315–342,
MR0146157.

28 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

This article focuses on the race between the residue class 1 (mod k) and other residue classes
ℓ ̸≡ 1 (mod k), for a ﬁxed modulus k for which HC holds.

Fix a character χ (mod k) such that χ(ℓ) ̸= 1, and let ρ0 = β0 + iγ0 be a zero of L(s, χ). The
authors prove that for T large enough,

max
T 1/3≤x≤T ψ(x; k, 1, ℓ) > T β0 exp (
−41 log T log log log T
log log T
 )

max
T 1/3≤x≤T Π(x; k, 1, ℓ) > T β0 exp (
−41 log T log log log T
log log T
 )

and symmetric results for the minimum. As one might expect, the oscillations obtained for π(x; k, 1, ℓ)
are worse, but the authors do prove

max
exp(log1/130
3 T )≤x≤T
 ( log x
√
x
 ) π(x; k, 1, ℓ) > 1
100 log log log log log T

and the symmetric result for the minimum. Each of these results yields lower bounds on the corre-
sponding number of sign changes, although for π(x; k, 1, ℓ) the bound is very low—improving this
bound is addressed directly in [73]. The authors’ methods can also compare primes congruent to
1 (mod k) to the average number of primes in other residue classes (mod k):

max
exp(log1/130
3 T )≤x≤T
 ( log x
√
x
 ) (
π(x; k, 1) − 1
φ(k) − 1
 ∑

(ℓ,k)=1
ℓ̸=1
 π(x; k, ℓ)
) > 1
100 log5 T

and the symmetric result for the minimum.

The proofs follow from the application of the power-sum method for bounding exponential sums.
Siegel’s theorem on the existence of zeros in certain rectangles, coupled with the veriﬁcation of HC
for certain moduli up to 24, give for these moduli the ﬁrst unconditional results about the size of
the ﬂuctuations of the above functions and the number of their sign changes.

This article cites [14, 17, 30, 46, 65].

[73] Knapowski, S. and Tur´an, P., Comparative prime-number theory. III. Continuation of the study
of comparison of the progressions ≡ 1 mod k and ≡ l mod k, Acta Math. Acad. Sci. Hungar. 13
(1962), 343–364, MR0146158.

The authors continue their comparison of π(x; k, ℓ) and π(x; k, 1), where ℓ ̸≡ 1 (mod k) and (ℓ, k) =
1, assuming HC for the modulus k. They show that Wk;ℓ,1(T ) > k−c log log log log T for suﬃciently
large T , where c is an absolute eﬀective constant. The proof technique involves Dirichlet’s box
principle and bounds obtained on Π(x; k, ℓ, 1) in [72].

When ℓ is a quadratic residue (mod k), they also show that if ρ0 = β0 + iγ0 is a zero of L(s, χ) for
some character χ such that χ(ℓ) ̸= 1, then for suﬃciently large T ,

max
T 1/3≤x≤T π(x; k, ℓ, 1) > T β0 exp (
−42 log T log log log T
log log T
 ) ,

and a similar statement holds for the minimum; consequently, for such k and ℓ, the inequality
Wk;ℓ,1(T ) > 1
log 3 log log T + O(1) holds for suﬃciently large T . The proof involves the power-sum
method for bounds on exponential sums.

The authors remark that both theorems hold as well for W (
∆
π(x; k, 1); T ) and W (˚∆
π(x; k, 1); T )
.

This article cites [17, 27, 30, 71, 72].

[74] Rosser, J. B. and Schoenfeld, L., Approximate formulas for some functions of prime numbers, Illinois
J. Math. 6 (1962), 64–94, MR0137689.

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 29

Sprinkled among the many explicit inequalities for prime counting functions are a few comments
directly related to comparative prime number theory, particularly on pages 72–73. The authors
point out that it is unknown whether n/φ(n) ≥ eC0 log log n inﬁnitely often, where C0 is Euler’s
constant. They also speculate as to the existence of counterexamples to the inequalities

log log x + B < ∑

p≤x
 1
p < log log x + B + 2
√
x log x

log x + E < ∑

p≤x
 log p
p < log x + E + 2.06123
√x

eC0 log x < ∏

p≤x
 p
p − 1 < eC0( log x + 2
√
x
 ),

where the constant B is the unique real number with the property that the diﬀerences among the
expressions on the ﬁrst line tends to 0, and similarly with E and the second line.

[75] Knapowski, S. and Tur´an, P., Comparative prime-number theory. IV. Paradigma to the general case,
k = 8 and 5, Acta Math. Acad. Sci. Hungar. 14 (1963), 31–42, MR0146159.

The authors apply techniques from earlier in this series of articles to the modulus k = 8, when
ℓ1, ℓ2 ∈ {3, 5, 7} are distinct quadratic nonresidues. They show that

max
T 1/3≤x≤T π(x; 8, ℓ1, ℓ2) > √
T exp (
−23 log T log log log T
log log T
 ) ,

and similarly for Π(x; 8, ℓ1, ℓ2) and ψ(x; 8, ℓ1, ℓ2). Since ℓ1 and ℓ2 can be interchanged, this re-
sult implies the inequality W8;ℓ1,ℓ2(T ) > 1
log 3 log log T + O(1), and similarly for W Π
8;ℓ1,ℓ2(T ) and

W ψ
8;ℓ1,ℓ2(T ).

In the third section, the authors remark on the modulus k = 5. The case (ℓ1, ℓ2) = (ℓ, 1) has already
been handled earlier in this series; the authors mention that the case (ℓ1, ℓ2) = (2, 3), where both
are quadratic nonresidues, can be handled in a similar way to the k = 8 cases treated in this article.
The remaining cases have ℓ1 = 4, a quadratic residue not equal to 1 (mod 5), and ℓ2 ∈ {2, 3}, and
these cases yield “an unpleasant (or pleasant?) surprise”: the authors cannot establish sign changes
for π(x; 5, 4, 2) and π(x; 5, 4, 3) even assuming GRH (although the methods do work for the Π and
ψ versions, a situation the authors discuss further in the later articles of this series).

This article cites [71–73].

[76] Knapowski, S. and Tur´an, P., Comparative prime-number theory. V. Some theorems concerning the
general case, Acta Math. Acad. Sci. Hungar. 14 (1963), 43–63, MR0146160.

Under the assumption of a “ﬁnite Riemann–Piltz conjecture” GRH(H, Ek), the authors establish
the following result for any distinct reduced residues ℓ1, ℓ2 (mod k) and for T suﬃciently large
(explicitly quantiﬁed in the article):

max
T 1/3≤x≤T Π(x; k, ℓ1, ℓ2) > √
T exp (
−44 log T log log log T
log log T
 )
,

and the same with Π replaced by ψ. A central element to their proof is the estimation of the integral

J(T ) = − 1
2πi
 ∫ 2+i∞

2−i∞
 ( ey1s

s
 )v (ω0Lv0
1 )
s

sv0+1 · 1
φ(k)
 ( ∑

χ (mod k)
χ(ℓ1)̸=χ(ℓ2)
 (χ(ℓ1) − χ(ℓ2)) L′

L (s, χ)
) ds

= 1
(v + v0)!
 ∫ Y1

1 Π(x; k, ℓ1, ℓ2) d
dx
 (( log Y1
x
 )v+v0 log x

)
 dx.

Their approach involves an application of the power-sum method similar to what appears in the
previous articles of the series. The authors note that their main theorem gives similar bounds on
∆
Π(x; k, ℓ)/φ(k) and ∆
ψ(x; k, ℓ)/φ(k). In particular, this result implies the lower bounds W Π
k;ℓ1,ℓ2(T ) >

1
log 3 log log T + O(1) and W ψ
k;ℓ1,ℓ2(T ) > 1
log 3 log log T + O(1).

This article cites [58, 71–73, 75].

30 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

[77] Knapowski, S. and Tur´an, P., Comparative prime-number theory. VI. Continuation of the general
case, Acta Math. Acad. Sci. Hungar. 14 (1963), 65–78, MR0146161.

Under the assumption of a “ﬁnite Riemann–Piltz conjecture” GRH(H, Ek), the authors establish
the following result in the case that ℓ1 and ℓ2 are either both quadratic residues or both quadratic
nonresidues (mod k): when T is suﬃciently large in terms of k (the authors give an explicit lower
bound), the inequalities

max
T 1/3≤x≤T π(x, k, ℓ1, ℓ2) > √
T exp (
−44 log T log log log T
log log T
 )

min
T 1/3≤x≤T π(x, k, ℓ1, ℓ2) < −√
T exp (
−44 log T log log log T
log log T
 )

hold. As usual, this result implies the lower bound Wk;ℓ1,ℓ2(T ) > 1
log 3 log log T + O(1). The authors
rely on multiple lemmas from their use of the power-sum method in previous articles of this series.

This article cites [72, 73, 76].

[78] Knapowski, S. and Tur´an, P., Comparative prime-number theory. VII. The problem of sign-changes
in the general case, Acta Math. Acad. Sci. Hungar 14 (1963), 241–250, MR0156826.

This article gives a general conditional proof that ψ(x; k, ℓ1, ℓ2) changes sign inﬁnitely often. The
authors show, assuming HC(Ek) for the modulus k for some constant 0 < Ek ≤ 1, that there exists
a positive constant c such that ψ(x; k, ℓ1, ℓ2) changes sign in every interval of the form ω ≤ x ≤
exp(2√
ω) as long as ω ≥ max {
ekc , e2/E3
k }
.
This result immediately implies results for the ﬁrst sign change of ψ(x; k, ℓ1, ℓ2) and for its number
of sign changes.

This article cites [71–73, 76, 77].

[79] Knapowski, S. and Tur´an, P., Comparative prime-number theory. VIII. Chebyshev’s problem for
k = 8, Acta Math. Acad. Sci. Hungar 14 (1963), 251–268, MR0156827.

Hardy–Littlewood and Landau had already shown that the assertion limx→∞ πe(x; 4, 1, 3) = −∞
is equivalent to GRH for L(s, χ−4). In this article the authors obtain an analogous equivalence
concerning the races between 1 and a nonsquare (mod 8): slightly modifying the arguments for
the (mod 4) case, they show that the assertion limx→∞ θe(x; 8, 1, ℓ) = −∞ for all ℓ ̸≡ 1 (mod 8) is
equivalent to GRH for the three nonprincipal Dirichlet L-functions (mod 8), and the same for the
assertion limx→∞ πe(x; 8, 1, ℓ) = −∞.

They further show that the race between two nonsquares switches inﬁnitely often—more precisely,
for ℓ1 ̸≡ ℓ2 ̸≡ 1 (mod 8), they unconditionally show that when T is large enough,

max
T 1/3≤x≤T θe(x; 8, ℓ1, ℓ2) > √
T exp (−22 log T log log log T
log log T
 ) .

They indicate that this result is “deeper”, and in particular that they cannot yet replace θe with
πe in this result.

The proofs rely on the power-sum method, as well as some explicit numerical data for the low-lying
zeros of the L-functions (mod 8).

This article cites [17–19].

[80] Neubauer, G., Eine empirische Untersuchung zur Mertensschen Funktion, German, Numer. Math.
5 (1963), 1–13, MR155787.

The author conducts an empirical study on the function M (n), disproving two conjectures. The
ﬁrst conjecture, by von Sterneck [12, 13] asserts that |M (n)| ≤ 1
2 √
n for n > 200, but the author
ﬁnds that n = 7,760,000,000 is a counterexample. The second conjecture, by Miller, asserts that∑n≤x M (n) < 0 for x ≥ 3, but the author shows that it ﬁrst fails at x = 21,067. The author also
points out some errors in the values of M (n) listed in [7, 12, 13].

This article cites [5, 7, 12, 13].

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 31

[81] Ingham, A. E., The distribution of prime numbers, Cambridge Tracts in Mathematics and Mathe-
matical Physics, No. 30, Stechert-Hafner, Inc., New York, 1964, pp. v+114, MR0184920.

This is a reprint of [26].

[82] K´atai, I., Eine Bemerkung zur “Comparative prime-number theory I-VIII” von S. Knapowski und
P. Tur´an, German, Ann. Univ. Sci. Budapest. E¨otv¨os Sect. Math. 7 (1964), 33–40, MR0176967.

Let ℓ1 and ℓ2 be distinct reduced residues (mod k). Assuming HC, the author proves that

lim sup
x→∞ ψ(x, k, ℓ1, ℓ2)
√
x > 0

(and hence the corresponding statement for lim inf). When ℓ1 and ℓ2 are either both quadratic
residues or both quadratic nonresidues, it follows that

lim sup
x→∞ π(x, k, ℓ1, ℓ2)
√
x/log x > 0,

(and the corresponding statement for lim inf). The proof uses an idea of Littlewood, namely to
estimate the iterated integrals An(x) = ∫ x
2 An−1(u) du where A0(x) = ψ(x; k, ℓ1, ℓ2) + O(log x) is
the explicit sum over zeros of Dirichlet L-functions (mod k).

Assuming GRH, the author can make the above statements quantitative and localized to intervals
of the form (x0, ax0), thus obtaining the lower bounds W ψ
k;ℓ1,ℓ2(T ) ≫ log T and (under the same

assumption on ℓ1 and ℓ2) the same estimate for W ψ
k;ℓ1,ℓ2(T ) ≫ log T .

This article cites [10, 22, 71–73, 75–79].

[83] Knapowski, S., On oscillations of certain means formed from the M¨obius series. II, Acta Arith. 10
(1964), 377–386, MR0172856.

The author investigates oscillations of the Mertens sum M (x) over intervals. Assuming RH, the
author shows that for all T > 1,

max
I⊂[T e−6(log T )5/6 ,T e6(log T )5/6 ] M (I) > T 1/2e−(log T )3/4

and the symmetric result for the minimum; indeed, only the assumption RH(H) is needed to establish
these oscillations for T ≤ eH6 . The author also establishes oscillations of the same size for the
absolute logarithmic average A
M
|1|(
[T e−6(log T )5/6, T e6(log T )5/6 ])
.

This article cites [70, 73, 85].

[84] Knapowski, S. and Tur´an, P., Further developments in the comparative prime-number theory. I,
Acta Arith. 9 (1964), 23–40, MR0162771.

The ﬁrst two sections oﬀer a short summary of comparative prime number theory up to 1964. The
authors classify the subject into 48 separate problems over 12 categories (and additional variants
on these), which is of interest to those interested in the history of the ﬁeld. They then move on to
prove results about “strongly localized accumulation problems”.

Most generally, assuming HC for the modulus k, they show that if T is suﬃciently large in terms of
k, then for any (ℓ, k) = 1 with ℓ ̸≡ 1 (mod k),

max
I ψ(
I; k, ℓ, 1) > √
T e− log11/12 T and min
I ψ(
I; k, ℓ, 1) < −√
T e− log11/12 T ,

where the maximum and minimum are taken over all subintervals I of [
T e− log11/12 T , T ]
. The central
argument involves the evaluation of the integral

1
2πi
 ∫ eAs( eBs − e−Bs

2Bs
 )r( 1
φ(k)
 ∑

χ (mod k) χ(ℓ) L′

L (s, χ)
) ds

for positive constants A and B.

This article cites [1, 17–19, 45, 65, 71–73, 75–79].

[85] Knapowski, S. and Tur´an, P., Further developments in the comparative prime-number theory. II. A
modiﬁcation of Chebyshev’s assertion, Acta Arith. 10 (1964), 293–313, MR0174538.

32 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

The authors establish several theorems, all assuming HC(Ek) with Ek ≪ √
log k/k; most of their
results concern the function θl(x, r; k, ℓ1, ℓ2) where r = r(x, k) satisﬁes log k
Ek ≪ r ≤ log x. Their
most general result (Theorem VI) is that for any quadratic nonresidue ℓ1 (mod k) and quadratic
residue ℓ2 (mod k), if L(s, χ) satisﬁes GRH for all characters χ (mod k) such that χ(ℓ1) ̸= χ(ℓ2),
then θl(x, r; k, ℓ1, ℓ2) ≫ √
x for x suﬃciently large.

They also establish the following result. Let ℓ be a quadratic nonresidue (mod k), and suppose
that there exists a character χ (mod k) with χ(ℓ) ̸= 1 such that L(s, χ) has a zero ρ0 = β0 + iγ0
with β0 > 1
2 . Then for all T (suﬃciently large in terms of k and ρ0), there exist subintervals
I± of [T e−5 log20/21 T , T e5 log20/21 T ] such that π(I+; k, ℓ, 1) > T β0 exp (
−(2 + γ2
0 )(log T )
5/7) and
π(I−; k, ℓ, 1) < −T β0 exp (
−(2 + γ2
0 )(log T )
5/7)
. They deduce this theorem from an analogous theo-
rem involving θl(x, r; k, ℓ, 1), which serves as a sort of inverse to Theorem VI.

Together, these results imply, given a quadratic nonresidue ℓ (mod k), that limx→∞ θl(x, r; k, ℓ, 1) =
+∞ holds if and only if L(s, χ) satisﬁes GRH for all characters χ (mod k) with χ(ℓ) ̸= 1. It follows
that limx→∞ θl(x, r; k, ℓ, 1) = +∞ holds for all quadratic nonresidues (mod k) if and only if L(s, χ)
satisﬁes GRH for every nonprincipal character χ (mod k).

The authors also make some remarks about races between residue classes to diﬀerent moduli, showing
for example how the race between π(x; 3, 1) and π(x; 4, 1) reduces to a race between residue classes
modulo 12, to which their results apply.

This article cites [1, 17, 18, 45, 65, 72, 75, 79].

[86] Makai, E., On a minimum problem. II, Acta Math. Acad. Sci. Hungar. 15 (1964), 63–66, MR0159791.

The author shows that the constant B in the second main theorem of the power-sum method cannot
be taken smaller than 4e.

This article cites [47].

[87] Sta´s, W., Some remarks on a series of Ramanujan, Acta Arith. 10 (1964/1965), 359–368, MR0177957.

Assuming RH, the author shows that

max
T 1−ε≤x≤T
 ∣
∣
∣
∣
 ∞∑

n=1
 µ(n)
n e−(x/n)2∣
∣
∣
∣ ≥ T −1/2−ε

when T is suﬃciently large in terms of ε.

This article cites [85].

[88] Tur´an, P., On a comparative theory of primes, in: Proc. Fourth All-Union Math. Congr (Leningrad,
1961) (Russian), Vol. II, Izdat. “Nauka”, Leningrad, 1964, pp. 137–142, MR0229595.

The author states some results whose detailed proofs later appeared in the series [71] with Knapowski.
First, the interval [T 1/3, T ] contains a sign change of ψ(x; 4, 3, 1) when T is large, while Eπ(x; 4, 3, 1) =
Ω±(log log log log log x). Analogous results hold for the moduli q = 3 and q = 6. For q = 8, when
ℓ = 3, 5, 7 the analogues hold for π(x; 8, ℓ, 1), while when ℓ1, ℓ2 ̸= 1 are distinct then π(x; 8, ℓ1, ℓ2) =
Ω±(
√
xe−log x/√log log x) for values x in all large intervals [T 1/3, T ], and similarly for πe(x; 8, ℓ1, ℓ2).
When ℓ ∈ {3, 5, 7}, he shows that limx→∞ πe(x; 8, ℓ, 1) = ∞ if and only GRH(χ) holds for all
χ (mod 8) with χ(ℓ) ̸= 1. The analogues hold for q = 5 (with the understanding that the distinction
between 1 and 3, 5, 7 (mod 8) becomes the distinction between quadratic residues and nonresidues
(mod 5)), with the exception that the Ω-result for πe(x; 5, 4, 1) requires that no L(s, χ) (mod 5)
vanishes in the region σ > 1 − (log log t)
−1/3.

[89] Grosswald, E., On some generalizations of theorems by Landau and P´olya, Israel J. Math. 3 (1965),
211–220, MR0198145.

The author generalizes theorems of Landau [10] and P´olya [23] on the relationship between sign
changes of a real-valued function and singularities of the corresponding Mellin transform; the main
results allow for logarithmic-type singularities as well as poles. The article asserts that its Theorem 6
follows from its Theorem 2, but it is remarked in [183] that this implication is invalid.

This article cites [8, 10, 14, 23].

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 33

[90] K´atai, I., The Ω-estimation of the arithmetic mean of the M¨obius function, Hungarian, Magyar Tud.
Akad. Mat. Fiz. Oszt. K¨ozl. 15 (1965), 15–18, MR0231801.

Assuming RH(T ), the author proves that M (x) = Ω±(T x
1/2e−c(log log x)2) for some c > 0. Analo-
gously, assuming RH(B) for any given B > 105, the author proves that M (x) = Ω±(x
1/2−δe−c(log log x)2),
where δ ≪ (log log B)/ log B.

This article cites [42, 53, 63].

[91] Knapowski, S. and Tur´an, P., Further developments in the comparative prime-number theory. III,
Acta Arith. 11 (1965), 115–127, MR0180539.

This article concerns the weighted function θl(x, r; k, ℓ, 1), for a modulus k satisfying HC and a
quadratic residue ℓ ̸≡ 1 (mod k). Let β0 be the real part of any zero of an L(s, χ) where χ (mod k)
a character such that χ(ℓ) ̸= 1. The authors exhibit extreme values of θl(x, r; k, ℓ, 1) where x is
near T and r is near (log T )
2/3; more precisely, there exists a positive constant c such that for
T suﬃciently large, there exist x1, x2 ∈ (T e−(log T )5/6, T e(log T )11/15 ) such that for suitable r1, r2 ∈
[(2 log T )
2/3, (2 log T )
2/3 + (2 log T )
2/5],

θl(x1, r1; k, ℓ, 1) > T β0e−c(log T )5/6 and θl(x2, r2; k, ℓ, 1) < −T β0e−c(log T )5/6.

The authors then state that using the methods of their prior article [85], it follows that for T
suﬃciently large, there exist closed subintervals I, J ⊆ [T e−(log T )6/7, T e(log T )6/7] such that one has
the “strongly localized accumulations”

π(I; k, ℓ, 1) > √
T e−c(log T )5/6 and π(J; k, ℓ, 1) < −√
T e−c(log T )5/6.

This article cites [1, 17–19, 45, 72, 79, 85].

[92] Knapowski, S. and Tur´an, P., Further developments in the comparative prime-number theory. IV,
Acta Arith. 11 (1965), 147-161; ibid. 11 (1965), 147–161, MR0182616.

Let ℓ1 and ℓ2 be quadratic nonresidues modulo a suﬃciently large modulus k. Let η be suﬃciently
small in terms of k, and suppose that the Dirichlet L-functions (mod k) satisfy GRH(2/√
η, Ek)
for suitable Ek. Then, when T is suﬃciently large in terms of k and η, there exist x+ and x−
in the interval [T 1−√
η, T elog
3/4 T ], and η1 and η2 in the interval [2η log T, 2η log T + √
log T ], such
that θl(x+, v+; k, ℓ1, ℓ2) > T 1/2−4
√
η and θl(x−, v−; k, ℓ1, ℓ2) < −T 1/2−4
√
η. Furthermore, under the
same assumptions, there exist subintervals I+, I− of [T 1−4
√
η, T 1+4
√
η] such that π(I+; k, ℓ1, ℓ2) >
T 1/2−5
√
η and π(I−; k, ℓ1, ℓ2) < −T 1/2−5
√
η.

This article cites [45, 73, 76, 85].

[93] Knapowski, S. and Tur´an, P., Further developments in the comparative prime-number theory. V,
Acta Arith. 11 (1965), 147-161; ibid. 11 (1965), 193–202, MR0182616.

This short article is distinct among the second series by Knapowski and Tur´an, in that, rather
than making use of “one-sided theorems” of the power-sum method, it uses a diﬀerent, “two-sided”
theorem to obtain its results: If m > 0 and z1, . . . , zn ∈ C nondecreasing in absolute value with
|z1| = 1, then for any b1, . . . , bn ∈ C, there exists an integer ν such that m ≤ ν ≤ m + n and
∣
∣
∣
∣
 n∑

j=1 bjzj
∣
∣
∣
∣ ≥ 1
2n
 ( n
8e(m + n)
 )n min
1≤k≤n
 ∣
∣
∣
∣
 k∑

j=1 bj
∣
∣
∣
∣.

In addition to the use of the “two-sided” theorem above, the authors use a modiﬁed idea attributed
to Kreisel involving a sequence of integrals.

The main result of this article is a single theorem, for residues ℓ ̸≡ 1 (mod k) for suﬃciently large
moduli k, under the assumption that there exists 0 < δ < 1
10 such that no function L(s, χ) with
χ(ℓ) ̸= 1 vanishes in the closed disk |s − 1| ≤ 1
2 + 4δ. (This assumption is stronger than HC(2√δ)
but weaker than HC( 1
2 + 4δ).) For any suﬃciently large T , the interval I = [T, e(log T )2(log log T )3 ]
contains x1, x2 such that

ψ(x1; k, 1, ℓ) ≥ x
1/2−4δ
1 and ψ(x2; k, 1, ℓ) ≤ −x
1/2−4δ
1 .

34 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

The authors compare their result to [72, Theorem 1.1], which uses more conventional methods and
yields a more localized sign change.

This article cites [66, 68, 72].

[94] Knapowski, S. and Tur´an, P., On an assertion of ˇCebyˇsev, J. Analyse Math. 14 (1965), 267–274,
MR0177963.

The authors begin by remarking on some variants of the result of Hardy–Littlewood–Landau [17–
19] that Chebyshev’s assertion, namely that limx→∞ πe(x; 4, 1, 3) = −∞, is equivalent to GRH
for L(s, χ−4). The same methods would show the “Abelian preponderance-relations” that the limit
limx→∞ πe(x; 3, 1, 2) = −∞ if and only if GRH holds for L(s, χ−3), while limx→∞ πe(x; 8, 1, ℓ) = −∞
for all ℓ ∈ {3, 5, 7} if and only if GRH holds for all nonprincipal Dirichlet L-functions (mod 8), and
(“mutatis mutandis”) limx→∞ πe(x; 12, 1, ℓ) = −∞ for all ℓ ∈ {5, 7, 11} if and only if GRH holds
for all nonprincipal Dirichlet L-functions (mod 12). All of these results, they point out, hold with
πe replaced by θe.

For the modulus k = 8, in the case where ℓ1, ℓ2 ∈ {3, 5, 7} are distinct quadratic nonresidues, the
authors had shown [79] that

max
T 1/3≤x≤T θe(x; 8, ℓ1, ℓ2) > √
T exp (−22 log T log log log T
log log T
 ) ;

however, they point out that the method failed to yield the analogous result for the “properly
ˇCebyˇsev” function πe. In this article, the authors do establish analogous large oscillations (without
identifying the signs of those oscillations) in the form

max
T 1/3≤x≤T |πe(x; 8, ℓ1, ℓ2)| ≥ √T exp (
−23 log T log log log T
log log T
 )

for any distinct reduced residues ℓ1, ℓ2 (mod 8), as well as the analogous statement for πe(x; 4, 1, 3).
The additional technical tool is a result (then unpublished) of Szeg˝o that derives estimates for∑n
j=1 bje−jy log j from estimates for ∑n
j=1 bje−jy.

This article cites [1, 17–19, 79].

[95] K´atai, I., Omega-type investigations in prime number theory, Hungarian, with English summary,
Magyar Tud. Akad. Mat. Fiz. Oszt. K¨ozl. 16 (1966), 369–396, MR0241374.

The author summarizes many oscillation results from his earlier work, most unconditional and
some assuming HC, for functions including M (x), Mr(x), Me(x), ψ(x; k, ℓ1, ℓ2) and π(x; k, ℓ1, ℓ2),
ψe(x; k, ℓ1, ℓ2), and ∑∞
n=1 µ(n)
n e−(x/n)2, as well as functions involving the distribution of k-free in-
tegers. An example that typiﬁes the strengths of the results is

max
T <x<T 7+4
√
3 M (x) = Ω±(
√
x) and max
T <x<T 1+ε M (x) = Ω±(x
Θ−ε).

This article cites [10, 14, 17, 19, 22, 31, 42, 46, 49, 53, 62, 70–73, 75–79, 83, 87].

[96] Knapowski, S. and Tur´an, P., Further developments in the comparative prime-number theory. VI.
Accumulation theorems for residue-classes representing quadratic residues mod k, Acta Arith. 12
(1966), 85–96, MR0200250.

The authors consider a “modiﬁed Abelian means” race between two quadratic residues ℓ1, ℓ2 (mod k),
under the assumption GRH( 3√
η , Ek) for suitable constants η and Ek. Their main result is that there

exist x ∈ [T 1−√
η, T log T ] and ν ∼ 2η log T such that

θl(x, ν; k, ℓ1, ℓ2) > T 1/2−2
√
η

(and thus the symmetric result for a large negative value). A corollary is the existence of an interval
I ⊂ [T 1−4
√
η, T 1+4
√
η] such that
 π(I; k, ℓ1, ℓ2) > T 1/2−3
√
η.

The authors obtain similar bounds for two quadratic nonresidues in [92], but emphasize that they
have not been able to extend the results to races where ℓ1 ̸≡ 1 (mod k) is a quadratic residue and
ℓ2 is a quadratic nonresidue. They employ the power-sum method for exponential sums.

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 35

This article cites [73, 85, 91, 92].

[97] Lehman, R. S., On the diﬀerence π(x) − li(x), Acta Arith. 11 (1966), 397–410, MR0202686.

The author shows that π(x) > li(x) for some x < 1.65 × 101,165; more precisely, he shows that there
is an interval of length 10500 between 1.53 × 101,165 and 1.65 × 101,165 on which π(x) > li(x). The
computations, involving the zeros of ζ(s) up to height 12,000, were performed on an IBM 7090 at
Berkeley.

This article cites [46, 66].

[98] Stark, H. M., On the asymptotic density of the k-free integers, Proc. Amer. Math. Soc. 17 (1966),
1211–1214, MR199161.

Evelyn and Linfoot [24] showed that ∆
Qk (x) = Ω±(x
1/2k). Following Ingham’s method [35], the
author makes their result eﬀective by showing that

lim inf
x→∞ ∆
Qk (x)/x
1/2k < −Ck and lim sup
x→∞ ∆
Qk (x)/x
1/2k > Ck;

here Ck = 2(1 − γ1
γ2 )
∣
∣ζ( ρ1
k )/ρ1ζ′(ρ1)
∣
∣, where ρj = 1
2 + iγj (j = 1, 2) are the ﬁrst two zeros of ζ(s)
above the real axis.

This article cites [24, 35].

[99] Grosswald, E., Oscillation theorems of arithmetical functions, Trans. Amer. Math. Soc. 126 (1967),
1–28, MR0202685.

The author reproduces known oscillation theorems for ∆
ψ(x), ∆
Π(x), and ∆
π(x) with proofs based
on extended versions of Landau’s theorem [10]. The results on the number of sign changes of ψ(q; a, b)
can be compared with ones in [71–73, 75, 77]. Moreover, under a suitable assumption weaker than
HC on the triples (q, a, b) the author proves that the diﬀerence π(x; q, a, b) changes sign inﬁnitely
often for q = 43, 47, 163, noting that the cases when q = 4 was proved by Hardy and Littlewood [17]
and the cases when q = 3, 5, 8 were proved by Knapowski and Tur´an [75]. It has been noted [183,
page 2] that some of the implications used in this article to derive some of the theorems from the
others may not be valid.

This article cites [1, 8, 10, 14, 23, 30, 45, 51, 71–73, 75–79, 84, 89, 94].

[100] K´atai, I., Comparative theory of prime numbers, Russian, Acta Math. Acad. Sci. Hungar 18 (1967),
133–149, MR0207665.

The author establishes various theorems on bounds for various arithmetic functions using the ideas
of Rodosski˘ı. These results include bounds related to M (x) and ψ(x; q, a, b) and ψr(x; q, a), as well
as estimates related to prime races modulo 8.

This article cites [49, 75–79, 87].

[101] K´atai, I., On investigations in the comparative prime number theory, Acta Math. Acad. Sci. Hungar.
18 (1967), 379–391, MR0218318.

The author establishes an oscillation theorem of Landau type for Dirichlet integrals with a nonreal
pole of arbitrary multiplicity, with the additional feature that the oscillations can be localized to
explicit intervals of the form [T, T K]. From this, he deduces many unconditional number-theoretical
results. For example, all of the following oscillations can be found in all suﬃciently large intervals
of the form [T, T 7+4
√
3]:

• M (x) = Ω±(
√
x), and the same for M (x, χ−4) and M (x; 4, 1) and M (x; 4, 3) and Me(x)
• Mr(x) = Ω±(1/√
x), and the same for ∑∞
n=1 µ(n)
n e−(x/n)2

• for any k ≥ 2, ∆
Qk (x) = Ω±(x
1/2k), and similarly for the sum of e−n/x over all k-free numbers
• ψ(x; 8, ℓ1, ℓ2) = Ω±(x
1/2) and, if ℓ1, ℓ2 ̸≡ 1 (mod 8), then π(x; 8, ℓ1, ℓ2) = Ω±(x
1/2)/ log x

Furthermore, by considering separately the cases where RH or GRH is true or false, the author ﬁnds
all the following oscillations in intervals of the form [T, T 1+ε] for any ﬁxed ε > 0:

• M (x) = Ω±(x
Θ−ε), and similarly for the other functions in the previous list

36 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

• under HC, ψ(x; k, ℓ1, ℓ2) = Ω±(x
Θ(k)−ε), and the same for ψe(x; k, ℓ1, ℓ2) (indeed, a hypothesis
slightly weaker than HC is required, in that real zeros of diﬀerent L-functions could cancel each
other out)

These last theorems imply qualitative improvements on the number of sign changes of their respec-
tive functions: for example, W (M, T )/ log log T → ∞ and, under HC, W ψ
k,ℓ1,ℓ2(T )/ log log T → ∞.

This article cites [10, 17, 71–73, 75–79].

[102] K´atai, I., On oscillations of number-theoretic functions, Acta Arith. 13 (1967/1968), 107–122,
MR0219496.

Assuming RH(H), the author shows that maxT κ≤x≤T M (x) ≫ √
x for T suﬃciently large in terms
of H and for an explicit κ = κ(H) that increases to 1 as H → ∞ (and similarly with M (x) replaced
by −M (x)). All constants are eﬀectively computable; for example, the value κ = 0.36 follows from
Rosser and Schoenfeld’s calculations of zeros of ζ(s). The author proves analogous results for several
weighted versions of M (x), such as

S(x) =
 ∞∑

n=1
 µ(n)
n e−(x/n)2 =
 ∞∑

k=1
 (−x
2)
k

k!ζ(2k + 1) ,

and also establishes lower bounds of magnitude T κ/2 for various averages of M (x) and its variants.

This article cites [17, 53, 62, 70, 87, 90, 101],

[103] Ryan, J. T., One more “many-more” assertion, Amer. Math. Monthly 74 (1967), no. 1, 19–24,
MR0207632.

Let πa(x; m, b) = #{n ≤ x : n ≡ b (mod m), Ω(n) = a}. Via combinatorial reasoning, the author
conjectures that πa(x; m, b)/πa(x; 1, 1) is asymptotically

1
φ(m) − (−1)
a+1(
1 − 1
cm
 )
x
−1/2 if b is a quadratic residue,

1
φ(m) + (−1)
a+1

cm x
−1/2 if b is a quadratic nonresidue.

The author provides some numerical evidence supporting the conjecture.

This article cites [3, 10, 44, 56].

[104] Cohen, A. M. and Mayhew, M. J. E., On the diﬀerence π(x) − li(x), Proc. London Math. Soc. (3)
18 (1968), 691–713, MR0233781.

Using an unpublished manuscript of Turing as a starting point, and using computations of zeros of
ζ(s) by Haselgrove, the authors show that π(x) − li(x) > 0 for some x ≤ 1010
529.7.

This article cites [97].

[105] Good, I. J. and Churchhouse, R. F., The Riemann hypothesis and pseudorandom features of the
M¨obius sequence, Math. Comp. 22 (1968), 857–861, MR240062.

The authors describe a random model for partial sums of µ(n) over short intervals and conjec-
ture that when h is large, the limiting distribution of M (x) − M (x − h) is normal with mean
0 and variance 6h/π2. Based on the law of the iterated logarithm, they also conjecture that
lim supx→∞ M (x)/√
x log log x = √
12/π.

This article cites [14, 26, 42, 51, 80].

[106] K´atai, I., On oscillation of the number of primes in an arithmetical progression. Acta Sci. Math.
(Szeged) 29 (1968), 271–282, MR0233782.

For the moduli q ∈ {3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 19, 24}, and on every suﬃciently large interval of the
form x ∈ [T, T 7+4
√
3], the author shows that ˚∆
π(x; q, a) = Ω±(
√x/ log x) for all quadratic non-
residues a, and also that π(x; q, a, b) = Ω±(
√
x/ log x) when a and b are both quadratic residues
or both quadratic nonresidues; the same results hold for the exponentially weighted functions
˚∆
π
e (x; q, a) and πe(x; q, a, b).

This article cites [14, 46, 49, 65, 79, 94, 97].

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 37

[107] Spira, R., Zeros of sections of the zeta function. II, Math. Comp. 22 (1968), 163–173, MR228456.

Haselgrove [51] resolved P´olya’s problem in the negative; in this article, the author provides numer-
ical evidence that conﬁrms Haselgrove’s computations. The author does a similar computation for
the Mertens function, showing that

lim inf
x→∞ EM (x) < −0.6027 and lim sup
x→∞ EM (x) > 0.5355.

The calculations were performed on an IBM 7040 at the University of Tennessee Computing Center.

This article cites [37, 51, 59, 74].

[108] Knapowski, S. and Tur´an, P., ¨Uber einige Fragen der vergleichenden Primzahltheorie, German
(1969), 157–171, MR0272729.

The authors prove that for all suﬃciently large T , there exist positive reals x < y ≤ T such that
θ(
(x, y]; 4, 3, 1) > √
y. The authors also prove an analogous bound for θ((x, y]; 4, 1, 3)
.

This article cites [1, 10, 14, 17–19, 68, 72, 84, 85].

[109] P´olya, G., ¨Uber das Vorzeichen des Restgliedes im Primzahlsatz, German (1969), 233–244, MR0263757.

This is a corrected version of the author’s earlier article [23].

[110] Steinig, J., The changes of sign of certain arithmetical error-terms, Comment. Math. Helv. 44
(1969), 385–400, MR0257003.

The author ﬁlls a gap in the proof of a reﬁnement of Landau’s theorem by P´olya and applies it to
summatory functions of arithmetic functions whose associated Dirichlet series have functional equa-
tions, obtaining lower bounds for the number of sign changes of the real and imaginary parts of the
corresponding error terms. Particular applications include the divisor function d(n), Ramanujan’s
function τ (n), and the number of representations of n as the sum of k squares (whose associated
Dirichlet series is the Epstein zeta-function ζk(s)).

This article cites [10].

[111] Saﬀari, B., Sur la fausset´e de la conjecture de Mertens. (With discussion.) French, C. R. Acad. Sci.
Paris S´er. A-B 271 (1970), A1097–A1101, MR280447.

The author investigates the connection between the Mertens conjecture and a ﬁnite version of LI,
using a method similar to that of Ingham [35]. Let γ1 < γ2 < · · · denote the positive ordinates
of the nontrivial zeros of ζ(s). Let P (h) be the statement that there are no nontrivial linear re-
lations ∑h
k=1 akγk ̸= 0 with ∑h
k=1 |ah| ≤ h, a ﬁnite and computationally veriﬁable assertion. The
author shows that P (28000) would imply lim supx→∞ |M (x)|/√
x > 1.179, which disproves Mertens
conjecture.

This article cites [4, 5, 7, 9, 13, 35, 80, 112].

[112] Bateman, P. T., Brown, J. W., Hall, R. S., Kloss, K. E., and Stemmler, R. M., Linear relations
connecting the imaginary parts of the zeros of the zeta function (1971), 11–19, MR0330069.

This article strengthens a result of Ingham [35] in a way that allows for computational exploration.
Deﬁne a sum ∑N
n=1 cnγn, where γ1, γ2, . . . are the positive ordinates of the nontrivial zeros of ζ(s),
to be of type (B) if each cn ∈ {−2, −1, 0, 1, 2} with at most one |cn| equal to 2. The authors show
that if at most ﬁnitely many sums of type (B) equal zero, then

lim sup
x→∞ x
−1/2L(x) = ∞, lim inf
x→∞ x
−1/2L(x) = −∞,

lim sup
x→∞ x
−1/2M (x) = ∞, lim inf
x→∞ x
−1/2M (x) = −∞.

Tables of data are given for the smallest sums of type (B) for N = 1, . . . , 20, as well as of type (A)
sums where only cn ∈ {−1, 0, 1} are allowed.

This article cites [26, 35].

[113] Stanis law Knapowski (19. V. 1931–28. IX. 1967), Colloq. Math. 23 (1971), 309–310, MR0300853.

This article is a short biography of Stanis law Knapowski’s life.

38 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

[114] Stark, H. M., A problem in comparative prime number theory, Acta Arith. 18 (1971), 311–320,
MR0289452.

This article gives a Tauberian theorem of Landau type (with a proof sketch and a reference to an
unpublished manuscript of the author) and uses it to show that

lim sup
x→∞
 (
Eπ(x; k, a) − Eπ(x; q, b)
) ≥ cq(b) − ck(a)

+ ∑

χ (mod q)
χ̸=χ0
 ∑

|γ|<T
 χ(b)
ρ
 (
1 − γ
T
 )
e(ρ−1/2)u − ∑

χ (mod k)
χ̸=χ0
 ∑

|γ|<T
 χ(a)
ρ
 (
1 − γ
T
 )
e(ρ−1/2)u

for any T > 0 and any u ∈ R, under the assumption of GRH(0) for nonprincipal L-functions
modulo k and q. In particular, the lim sup is positive if either a is a nonsquare (mod k) or b is a
square (mod q) (these are the cases for which cq(b) − ck(a) ≥ 0). Under the same assumption, the
author further proves

lim sup
x→∞
 (
Eπ(x; k, a) − Eπ(x; q, b)
) ≥ cq(b) − ck(a)

+ ∑

χ (mod q)
χ̸=χ0
 ∑

|γ|<T
 χ(b)
ρ e(ρ−1/2)u − ∑

χ (mod k)
χ̸=χ0
 ∑

|γ|<T
 χ(a)
ρ e(ρ−1/2)u

for any T > 0 and any u ̸= 0. Finally, when u < 0 the author obtains an exact formula for this
right-hand side as T → ∞, a version that implies that the lim sup is inﬁnite if a ≡ 1 (mod k) or
b ≡ 1 (mod q) but not both. The author also uses this exact formula and some shrewd explicit
computation to show for the ﬁrst time that π(x; 5, 4, 2) = Ω+(
√x/ log x).

This article cites [35, 71–73, 75–79].

[115] Tur´an, P., Commemoration on Stanis law Knapowski, Colloq. Math. 23 (1971), 310–318, MR0300854.

The author recalls theorems from Knapowski’s work after he died in a car accident at age 36.

This article cites [52, 62, 63, 69, 71–73].

[116] Diamond, H. G., Two oscillation theorems (1972), 113–118. Lecture Notes in Math., Vol. 251,
MR0332684.

The author presents two variants of oscillation theorems analogous to those of Ingham in [35]. Let
F (s) = ∫ ∞
0 e−suf (u) du denote the Laplace transform of the measurable function f : [0, ∞) → R.
We suppose that the integral deﬁning F (s) converges for ℜ(s) > 0, and that F (s) can be continued
as a meromorphic function to a neighborhood of the imaginary axis; suppose further that all the
poles of F (s) on the imaginary axis are simple. Let T be the set of positive real numbers t such that
it is a pole of F (s), and let at be the residue of F (s) at s = it; furthermore, let a0 be the residue
(possibly 0) of F (s) at s = 0.

The author deﬁnes a subset W ⊂ T to be “weakly independent of order N ” if the only way to ﬁnd
integers |nt| ≤ N (t ∈ W ) such that ∑
t∈W ntt ∈ T is to choose one nt equal to 1 and the rest equal
to 0. Given such a weakly independent subset W ⊂ T of order N , the author proves that

lim
x→∞ ess sup
u≥x f (u) ≥ a0 + 2N
N + 1
 ∑

j∈J |aj|

lim
x→∞ ess inf
u≥x f (u) ≤ a0 − 2N
N + 1
 ∑

j∈J |aj|

(where these essential supremum and inﬁmum denote the supremum/inﬁmum when we may ignore
a set of inputs of measure 0); equivalently, if 2N
N +1 ∑
j∈J |aj| > |a0| then f (x) has arbitrarily large
sign changes. (The author gives a slight strengthening of this theorem as well.)

This article cites [35, 51, 59, 89, 99, 111, 112].

[117] Grosswald, E., Oscillation theorems, in: The theory of arithmetic functions (Proc. Conf., Western
Michigan Univ., Kalamazoo, Mich., 1971), Lecture Notes in Math., Vol. 251, Springer, Berlin, 1972,
141–168, MR0332685.

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 39

This article improves results due to Grosswald [99] that relied on an extended Landau’s theorem
and a theorem of Diamond [116]. Say that a ﬁnite set of real numbers is k-independent if there are
no nontrivial vanishing linear combinations of that set with integer coeﬃcients bounded by k in
absolute value. The author shows that the veriﬁcation of the 5-independence of the (ordinates of
the) ﬁrst 30 zeros of ζ is suﬃcient to show that π(x) − li(x) changes sign inﬁnitely often. Similarly,
the veriﬁcation of the 13-independence of the ﬁrst 75 zeros is suﬃcient to disprove the Mertens
conjecture, and the veriﬁcation of the 16-independence of the ﬁrst 13 zeros is suﬃcient to prove
that L(x) and Lr(x) change sign inﬁnitely often. Moreover, for integers q, q′ with φ(q) = φ(q′), the
author investigates the sign changes of π(x; q, a) − π(x; q′, a′). In particular, the author shows that
π(x; p, a, a′) changes sign inﬁnitely often for all primes p ≤ 19 and all appropriate a, a′.

This article cites [14, 17, 35, 51, 71, 99, 111, 112, 114, 116].

[118] Knapowski, S. and Tur´an, P., Further developments in the comparative prime number theory. VII,
Acta Arith. 21 (1972), 193–201, MR0302585.

The authors show that for large enough T , there exist numbers U1, U2, U3, U4 with

log log log T ≤ U2 exp (
− log15/16 U2) ≤ U1 < U2 ≤ T

log log log T ≤ U4 exp (
− log15/16 U4) ≤ U3 < U4 ≤ T

such that θ([U1, U2]; 4, 1, 3) > √
U2 and θ([U3, U4]; 4, 1, 3) < −√
U4. In particular, there exist consec-
utive primes pn and pn+1, both congruent to 1 (mod 4), satisfying log log log T ≤ pn < pn+1 ≤ T .

This article cites [45, 72, 85].

[119] Shanks, D. and Lal, M., Bateman’s constants reconsidered and the distribution of cubic residues,
Math. Comp. 26 (1972), 265–285, MR0302590.

Set αa(p) = 3 if a is a cubic residue modulo p and αa(p) = 0 otherwise, and deﬁne ka = ∏
p∤a(p −
αa(p))/(p − 1), a conditionally convergent constant relevant to the conjectured asymptotic formula
for the number of prime values of n3 + a. The authors describe their computations of k2 and k3
accurate to six decimal places. Further heuristics invoke the race between those primes for which a
is a cubic residue and those for which it is not, which is a Chebotarev density theorem race for the
extension Q( 3√
a, e2πi/3)/Q.

[120] Dancs, S. and Tur´an, P., Investigations in the powersum theory. I, Ann. Univ. Sci. Budapest. E¨otv¨os
Sect. Math. 16 (1973), 47–52 (1974), MR0352012.

Spurred by unpublished work of Knapowski, the authors establish the following more ﬂexible version
of the second main theorem of the power-sum method. In addition to the usual condition 1 = |z1| ≥
|z2| ≥ · · · ≥ |zn|, let m ≥ 0 be an integer, choose δ1 and δ2 with m
m+n ≤ δ2 ≤ δ1 ≤ 1, and choose
indices ℓ1 and ℓ2 such that |zℓ1| ≥ δ1 and |zℓ2| ≤ δ2 (or ℓ2 = n if no such zℓ2 exists). Then

max
m+1≤v≤m+n
 ∣
∣
∣
∣
 n∑

j=1 bjzv
j
 ∣
∣
∣
∣ ≥ 2( δ1 − δ2
8e
 )n min
ℓ1≤j≤ℓ2 |b1 + · · · + bj|.

This article cites [45].

[121] Jurkat, W. B., On the Mertens conjecture and related general Ω-theorems (1973), 147–158, MR0352026.

Deﬁne C = 2 + ∑∞
n=1 (−1)
n(2π)
2n/n(2n)!ζ(2n + 1) ≈ −.505. The author proves unconditionally
that lim supx→∞ EM (x) > 1 + C and lim inf x→∞ EM (x) < C; in particular, the latter inequality
disproves the conjecture of von Sterneck [7] that |M (x)| ≤ 1
2 √
x. The main tool is a general oscillation
result for almost periodic functions in the distributional sense (combined with Landau’s theorem
to reduce to the RH case). The author’s general theorems recover Ω-results proved by Hardy and
Littlewood for ∆
ψ(x) and ∆
D(x).

This article cites [7, 14, 16, 26, 27, 30, 35, 42, 80, 112, 116].

[122] Brent, R. P., Irregularities in the distribution of primes and twin primes, Math. Comp. 29 (1975),
Collection of articles dedicated to Derrick Henry Lehmer on the occasion of his seventieth birthday,
43–56, MR0369287.

40 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

The author reports on extensive calculations of π(x) and of the counting function for twin primes.
He suggests from these computations that Eπ(x) has a limiting distribution with mean −1 and
standard deviation approximately 0.21 (which diﬀers by less than 3% from the true value under RH
and LI). He veriﬁes that π(x) ≤ li(x) for x ≤ 8 × 1010, and predicts from the observed distribution
above that π(x) ≤ li(x) for x up to at least 10100. Shanks [56] conjectured that 1
x ∫ x
0 Eπ(t) dt tends
to −1; the author suggests from his computations that this conjecture is false but that its logarithmic
counterpart limx→∞ 1
log x ∫ x
1 Eπ(t) dt
t = −1 should be true.

The author also shows that the error term in the counting function of twin primes does not exceed
2.3x
1/2/ log x in absolute value for x ≤ 8 × 1010. He also gives the heuristic estimate 1.9021604 ± 5 ×
10−7 for Brun’s constant ∑( 1
q + 1
q+2 ) (where the sum is over twin primes q), although no rigorous
upper bound is given.

This article cites [14, 17, 26, 46, 56, 97].

[123] Diamond, H. G., Changes of sign of π(x) − li(x), Enseignement Math. (2) 21 (1975), no. 1, 1–14,
MR0376566.

The author gives a new proof that π(x)−li(x) changes sign inﬁnitely often, without using an explicit
formula for prime-counting functions but instead establishing a Tauberian theorem of Wiener–
Ikehara type. The author believes that the arguments could be extended to gain the extra factor of
log log log x in the oscillations found by Littlewood.

This article cites [35, 74].

[124] Ellison, W. J., Les nombres premiers, French, En collaboration avec Michel Mend`es France; Publi-
cations de l’Institut de Math´ematique de l’Universit´e de Nancago, No. IX; Actualit´es Scientiﬁques
et Industrielles, No. 1366, Hermann, Paris, 1975, pp. xiv+442, MR0417077.

Chapter 6 of the book is on irregularities in the distribution of prime counting functions. Complete
proofs of classical oscillation results on ∆
ψ(x) and ∆
Π(x) are presented in Section 6.2. The Mertens
conjecture and P´olya problem and their connections with Ingham’s method [35] are discussed in
Section 6.3. In Section 6.4, the author discusses the disproof of a conjecture of Shanks [56], which is
a precise version of Chebyshev’s bias on the prime races between 1 (mod 4) primes and 3 (mod 4)
primes. In the notes section of the same chapter, the author discusses the diﬀerence between ∆
π(x)
and its analogue in the setting of Gaussian primes, as well as sign changes of arithmetic functions.

This chapter cites [1, 4, 10, 14, 17, 27, 35, 46, 48, 51, 56, 59, 66, 71–77, 80, 97, 99, 104, 110, 111].

[125] Jurkat, W. and Peyerimhoﬀ, A., A constructive approach to Kronecker approximations and its ap-
plication to the Mertens conjecture, J. Reine Angew. Math. 286(287) (1976), 322–340, MR429789.

Similar to the ﬁrst author’s work [121], the authors reduce the problem of improving the bounds on
lim sup EM (x) and lim inf EM (x) to ﬁnding a reasonably good solution to an inhomogenous Dio-
phantine approximation problem. Their new constructive algorithm leads to the following improved
bounds related to the Mertens conjecture:

lim inf
x→∞ EM (x) < −0.638 and lim sup
x→∞ EM (x) > 0.779.

The authors remark that the smallest counterexample to the Mertens conjecture is likely to be at
least exp(4.16 × 1014).

This article cites [4, 5, 7, 12, 13, 35, 42, 80, 107, 112, 116, 121].

[126] Knapowski, S. and Tur´an, P., On the sign changes of (π(x) − li x). I, in: Topics in number theory
(Proc. Colloq., Debrecen, 1974), North-Holland, Amsterdam, 1976, 153–169. Colloq. Math. Soc.
J´anos Bolyai, Vol. 13, MR0439771.

The authors prove that W π(T ) = Ω((log T )
1/4(log log T )
−4) (a slightly weaker result is claimed). In
light of Ingham’s stronger result [30] assuming SA, it suﬃces to assume that RH is false. Given any
zero ρ = β + iγ of ζ(s) with β > 1
2 , the authors show that for x ∈ [Y, Y exp((log Y )
3/4(log log Y )
4)]
one has ∆
Π(x) = Ω±(Y β exp(−√
log Y )) when Y is suﬃciently large in terms of ρ. The authors make
special mention of their application of a “two-sided” power-sum theorem to get a strong “one-sided”
result.

This article cites [8, 14, 17, 23, 27, 30, 31, 46, 65, 74, 93, 97].

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 41

[127] Knapowski, S. and Tur´an, P., On the sign changes of (π(x) − li x). II, Monatsh. Math. 82 (1976),
no. 2, 163–175, MR0439772.

Following ideas of Littlewood, Ingham, and Skewes, the authors show unconditionally that W (Y ) ≫
log log log Y for suﬃciently large Y , where the implied constants are eﬀective.

The proof itself is divided into two cases. First, supposing the existence of an RH-violating zero
β + iγ of ζ(s) such that β ≥ 1
2 + 2 log
−1/5 Y and 0 < γ ≤ log1/5 Y , the authors establish the much
stronger lower bound
 V1(Y ) > 1
2
 ( log Y

2 log5/6 Y
 )1/5 > 1
4 log1/30 Y.

The second case, where there is no such zero, is more technical and relies as usual upon Dirichlet’s
box principle.

This article cites [14, 17, 23, 26, 30, 46, 66, 126].

[128] Levinson, N., On the number of sign changes of π(x) − li x, in: Topics in number theory (Proc.
Colloq., Debrecen, 1974), North-Holland, Amsterdam, 1976, 171–177. Colloq. Math. Soc. J´anos
Bolyai, Vol. 13, MR0439774.

Assuming that SA is false, the author shows that lim supT →∞ W π(T )/ log T = ∞. The author
adapts a Landau-type argument of P´olya [23, 109] to treat functions with logarithmic singularities.

This article cites [23, 30, 65, 66, 109, 126].

[129] Pintz, J., Bemerkungen zur Arbeit: “On the sign changes of (π(x) − li x). II” (Monatsh. Math.
82 (1976), no. 2, 163–175) von S. Knapowski und P. Tur´an, German, Monatsh. Math. 82 (1976),
no. 3, 199–206, MR0439773.

The author shows that there exists c > 0 such that W (T ) ≫ (log log T )
c when T is suﬃciently
large. Indeed, this is a special case of a more general result that establishes many large oscilla-
tions of ∆(x): let D be suﬃciently large and set µ = D/ log log log log T . Then there are at least
exp (
(log log log T )
1−µ) sign changes of ∆(x) up to T , with oscillations as large as

∆(x) > ( 1
2 − 3 log D
D
 )
µ · √
x log log log x
log x

(and the negative analogue), which, when D is so large that µ ≫ 1, provides oscillations as large as
those established by Littlewood.

This article cites [14, 30, 46, 127].

[130] Sta´s, W. and Wiertelak, K., Further applications of Tur´an’s methods to the distribution of prime
ideals in ideal classes (mod f ), Acta Arith. 31 (1976), no. 2, 153–165, MR0429797.

Let K1, K2 be ideal classes (mod f) in a number ﬁeld. In this article, the authors use the second main
theorem of the power-sum method to bound ψ(x, K1) − ψ(x, K2) given a zero-free region for Hecke–
Landau zeta functions of relevant Hecke characters χ, and establish a converse as well: Let γ1 be the
supremum of numbers γ for which ψ(x, K1) − ψ(x, K2) ≪ xe−a(log x)γ for some positive constant a,
and let γ2 be the inﬁmum of numbers γ for which ∏
χ(K1)̸=χ(K2) ζ(s, χ) does not vanish in the region
σ > 1 − b/(log |t|)
γ for some positive constant b. The authors prove that γ1 = 1/(1 + γ2).

This article cites [26, 45, 49, 61].

[131] Bays, C. and Hudson, R. H., The segmented sieve of Eratosthenes and primes in arithmetic progres-
sions to 1012, Nordisk Tidskr. Informationsbehandling (BIT) 17 (1977), no. 2, 121–127, MR0447090.

The authors describe in detail a reﬁnement of the segmented sieve of Eratosthenes, which they call
the dual sieve, designed to lower the execution time. As an illustration, they record the number of
primes in the eight reduced residue classes modulo 24 (from which one can calculate the number of
primes in residue classes modulo any divisor of 24) up to 1011, 2 × 1011, . . . , 1012. From their table,
one easily observes that π(x; 24, 1) is consistently smaller than any other π(x; 24, a) by an amount
that is very roughly 1
2 π(
√x).

42 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

[132] Hooley, C., On the Barban-Davenport-Halberstam theorem. VII, J. London Math. Soc. (2) 16 (1977),
no. 1, 1–8, MR0506080.

Assuming GRH and LI, the author shows that Eψ(x; q, a)/√φ(q) log q has a limiting logarithmic
distribution function (depending only on q and not a), as well as the central limit theorem that these
functions tend to the standard normal distribution as q → ∞. The proof proceeds by writing the
characteristic function of this distribution as a product of Bessel functions. The same result holds
for Eθ(x; q, a)/√
φ(q) log q, except that the mean of the limiting logarithmic distribution depends
on whether a is a quadratic residue (mod q).

This article cites [34].

[133] Hudson, R. H. and Bays, C., The mean behavior of primes in arithmetic progressions, J. Reine
Angew. Math. 296 (1977), 80–99, MR0460261.

The goal of this article is to ﬁnd an elementary explanation (not involving complex analysis) for
biases in prime number races. They argue from the Meissel-type formula

π(x; q, a) = Φ(x, x
1/3; q, a)+π(x
1/3; q, a) − ∑

x1/3<p≤x1/2

p∤q
 π( x
p ; q, ap−1)

+ ∑

x1/3<p≤x1/2

p∤q
 π(p; q, ap−1) − ∑

b (mod q)
b
2≡a (mod q)
 π(
(x
1/3, x
1/2]; q, b)
,

where Φ(x, y; q, a) denotes the number of integers in (1, x] congruent to a (mod q) that are free of
prime factors up to y. They identify the ﬁnal term as a persistent bias against quadratic residues a,
and support their interpretation with numerical evidence.

The authors reﬁne the above formula to reduce the occurrences of x
1/3 to x
1/4, thus introducing
contributions from products of three primes; while observable in the numerical data, these contribu-
tions seem to be less signiﬁcant for large x. From their analysis they make some heuristic predictions,
in particular that
 Aπ
1 (x; q, N ) − (cq − 1)Aπ
1 (x; q, R) ∼ 1
2
 x∑

n=1 π(n1/2).

This article cites [1, 3, 17, 18, 44, 48, 56, 71–73, 75–79, 81, 84, 85, 91–94, 96, 114, 119, 131, 138].

[134] Knapowski, S. and Tur´an, P., On prime numbers ≡ 1 resp. 3 (mod 4), in: Number theory and
algebra, Academic Press, New York, 1977, pp. 157–165, MR0466043.

The authors show, with pν denoting the νth prime, that when T is suﬃciently large,
∑

pν ≤T
pν ≡pν+1≡1 (mod 4)
 1 > logB T

for some eﬀective constant B. The fact that the left-hand side tends to ∞ follows from Littlewood’s
oscillation theorem for primes (mod 4), but no quantitative rate of growth had been established.
The proof uses their result from [118], as well as Ingham’s application of Fej´er kernels as in [30]. The
authors note the open problem about the existence of inﬁnitely many triples of consecutive primes
congruent to 1 (mod 4). They also guess that the four possibilities for the pair of congruence classes
(pν, pν+1) (mod 4) are not equally likely.

This article cites [26, 85, 118].

[135] Pintz, J., On the remainder term of the prime number formula. III. Sign changes of π(x) − lix,
Studia Sci. Math. Hungar. 12 (1977), no. 3-4, 345–369 (1980), MR607089.

This article establishes new results on the number of sign changes of π(x) − li(x). In particular it
proves the eﬀective result W (T ) ≫ √
log T / log log T and corresponding results for W Π(T ), W θ(T ),
and W ψ(T ) with the same lower bound. Moreover, it establishes that there is necessarily a sign
change in the interval [T, T exp(63√
log T log log T )] for T large enough in each of these cases, al-
though the lower bound on such T is eﬀectively computable only in the Π(x) and ψ(x) versions.

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 43

Under RH, Ingham’s result from 1936 gives in fact a stronger localization theorem. The author here
uses the power-sum method, and in particular a result of S´os–Tur´an, to achieve a result under the
assumption that RH fails. Ingham’s idea to use Fej´er kernels is also applied to prove the eﬀective
lower bound on W (T ) in the absence of an eﬀective localization result.

This article cites [14, 23, 30, 46, 65, 66, 126, 127, 129].

[136] Pintz, J., On the sign changes of π(x) − li(x), in: Journ´ees Arithm´etiques de Caen (Univ. Caen,
Caen, 1976), Soc. Math. France, Paris, 1977, 255–265. Ast´erisque No. 41–42, MR0447151.

The author begins with a thorough summary of results on sign changes of ∆
π(x) and related
problems; he then announces, without proof, several new results of this type. He claims that for
T suﬃciently large, unconditionally, W (T ) ≫ √
log T / log log T , and that there exists c > 0 such
that every interval of the form [T c, T ] contains a sign change of ∆
π(x); ineﬀectively one can narrow
these intervals to the form [T e−√
log T log log T , T ]. Even if one restricts to “big sign changes”, where
∆
π(x) = Ω±(
√
x log log log x/ log x), the author asserts that the number of such sign changes up
to T is ≫ √
log T e−√
log log T eﬀectively and ≫ √log T /(log log T )
2 ineﬀectively; these sign changes
can be localized as well, and the latter inequality even holds for large sign changes of the average of
∆
π(x) over intervals of length x/ log log x. The author further asserts that analogous theorems can
be proved for the other prime counting functions, as well as for π(x; 4, 1, 3) and some other class of
prime races.

This article cites [14, 30, 46, 71–73, 75–79, 126, 127, 129].

[137] Bays, C. and Hudson, R. H., Details of the ﬁrst region of integers x with π3,2(x) < π3,1(x), Math.
Comp. 32 (1978), no. 142, 571–576, MR0476616.

The authors determine that x = 608,981,813,029 is the smallest x such that π(x; 3, 2, 1) = −1. A
faster version of a previous program of theirs (which had run up to 2.5 × 1011) was used to ﬁnd this
sign change. The authors provide graphs of π(x; 3, 2, 1) near this ﬁrst sign change; they highlight
that π(x; 3, 2, 1) becomes negative at two separate regions near the sign change, before taking on
values shortly after that are much more positive. The authors observe that neither π(x; 3, 2, 1) nor
π(x; 4, 3, 1) becomes very negative near the occurrence of its ﬁrst negative values; in attempts to
determine a smaller Skewes number, consequently, they recommend evaluation of ∆
π(x) in regular
intervals in order to not miss a “shallow” sign change.

This article cites [1, 14, 26, 48, 56, 84, 97, 138, 141].

[138] Bays, C. and Hudson, R. H., On the ﬂuctuations of Littlewood for primes of the form 4n ± 1, Math.
Comp. 32 (1978), no. 141, 281–286, MR0476615.

The authors describe the sixth “axis crossing region” (a term they deﬁne rigorously) for π(x; 4, 3, 1),
in which there are 4.1 × 108 consecutive integers satisfying π(n; 4, 3, 1) < 0. From their ﬁndings of
surprisingly large axis crossing regions, the authors suggest that the number of integers n ≤ x
with π(n; 4, 3, 1) < 0 might be Ω(x/ log x), while still respecting the conjecture that this counting
function is o(x).

This article cites [1, 14, 17, 18, 25, 44, 48, 56, 73, 78, 81, 84, 85, 133].

[139] Bays, C. and Hudson, R. H., The appearance of tens of billions of integers x with π24,13(x) < π24,1(x)
in the vicinity of 1012, J. Reine Angew. Math. 299/300 (1978), 234–237, MR0472726.

The authors describe their empirical observation that π(x; 24, 13, 1) < 0 for about a third of the
integers between 0.978 × 1012 and 1.094 × 1012. They assert the expectation that the set of such
real numbers x has density 0.

This article cites [44, 56, 72, 84, 85, 131, 133, 137, 138].

[140] Pintz, J., On the remainder term of the prime number formula. IV. Sign changes of π(x) − lix,
Studia Sci. Math. Hungar. 13 (1978), no. 1-2, 29–42 (1981), MR630377.

This article establishes lower bounds for the number of sign changes for the error terms of classical
prime-counting functions. The main theorem of this article states that for f = π, Π, θ, or ψ, there

44 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

exists an absolute constant Y (f ) such that for Y > Y (f ),

W f (Y ) > 1
1011 log Y
(log log Y )3 .

Interestingly, Y (Π) and Y (ψ) are eﬀectively computable in the author’s proof, whereas Y (π) and
Y (θ) are ineﬀective constants.

This article cites [14, 30, 46, 65, 66, 126, 127, 129, 135].

[141] Bays, C. and Hudson, R. H., Numerical and graphical description of all axis crossing regions for
the moduli 4 and 8 which occur before 1012, Internat. J. Math. Math. Sci. 2 (1979), no. 1, 111–119,
MR529694.

The authors of this article determine by computation the locations where π(x; 4, 3, 1) < 0, and
where π(x; 8, a, 1) < 0 for any a ∈ {3, 5, 7}, for x up to 1012. For x < 109, a check was made at every
prime; for 109 ≤ x ≤ 1012, a check was made every 107 integers, with additional checks in between
if π(x; q, a, b) was found to be near zero. They then organize these locations into “axis-crossing
regions” (ACRs) [m, n], where π(m; q, a, 1) = π(n; q, a, 1) = −1 and π(x; q, a, 1) ≥ 0 for all x outside
an ACR, with m at least twice as large as the upper bound for the previous ACR.

For q = 4, they ﬁnd six distinct ACRs under 1012. For (q, a) = (8, 5), they ﬁnd two ACRs under
1012 and ﬁnd no ACRs for (q, a) = (8, 3) or (q, a) = (8, 7). They compare their computations to
earlier published results from Leech [48], Shanks [56], and an unpublished communication from
Lehmer (dated October 29, 1975). While their results overlap with Leech and Shanks for q = 4 for
x ≤ 3 · 106, they ﬁnd that their new information contradicts a prior characterization of the ACRs as
mostly consisting of sparse, tiny intervals. For example, one ACR below x < 2 · 1010 contains 5 · 108

integers where π(x; 4, 3, 1) < 0; another ACR between 37 · 109 and 39 · 109 contains 1.2 · 109 integers
with π(x; 8, 5, 1) < 0. Consequently, they argue that for large x, such regions may be more typical
than sign-changes being sparse, isolated points.

This article cites [1, 14, 48, 56, 72, 73, 131, 138].

[142] Besenfelder, H.-J., ¨Uber eine Vermutung von Tschebyschef. I, German, J. Reine Angew. Math.
307/308 (1979), 411–417, MR534235.

Using an existing explicit formula for general Mellin-transform pairs, the author shows that

2√
πy ∑

0<σ<1
L(σ+iγ,χ−4)=0
 ey(σ−1/2+iγ)2 = log 4
π − 2
 ∞∑

n=1
 Λ(n)χ−4(n)
√n e−(log n)2/4y

− C0 + 2 ∫ ∞

0
 e−x2/4y+x/2 − 1
1 − e2x dx.

From this identity, he proves unconditionally that

lim
x→∞
 ∑

p χ−4(p) log p
√p e−(log2 p)/x = −∞.

(Note: the author, Hans–Joachim Besenfelder, soon changed his last name to Bentz and began to
publish under that name.)

This article cites [1, 17, 18, 85].

[143] Riele, H. J. J. te, Computations concerning the conjecture of Mertens, J. Reine Angew. Math.
311(312) (1979), 356–360, MR549977.

The author introduces some modiﬁcations of the method of Jurkat and Peyerimhoﬀ [125] and proves
that lim inf
x→∞ EM (x) < −0.843 and lim sup
x→∞ EM (x) > 0.860.

The calculation took several hundred CPU-hours on a CDC Cyber 73/173 system.

This article cites [4, 107, 112, 125].

[144] Bentz, H.-J. and Pintz, J., Quadratic residues and the distribution of prime numbers, Monatsh.
Math. 90 (1980), no. 2, 91–100, MR595317.

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 45

The ﬁrst section of this article oﬀers a short, conventional history of prime number races, speciﬁcally
citing Shanks’s computational work and heuristics from [56] as motivation for its results. Let ℓ1 be
a quadratic residue (mod q) and ℓ2 a quadratic nonresidue (mod q). Suppose that Dirichlet L-
functions (mod q) satisfying the condition that all zeros β + iγ satisfy the inequality β2 − γ2 ≤ 1
4
(a “bowtie” assumption). Then for 0 ≤ α < 1/2,
∑

p≡ℓ1 (mod q)
 log p
pα e−(log p)2/x − ∑

p≡ℓ2 (mod q)
 log p
pα e−(log p)2/x ∼ cq
φ(q) √
πx · e x
4 ( 1
2 −α)2 ,

and in particular tends to inﬁnity. By computations of Spira, this result is unconditional for q ≤ 24.

This article cites [1, 17–19, 48, 56, 71–73, 75–79, 84, 85, 91–93, 96, 142, 146, 162].

[145] Bentz, H.-J. and Pintz, J., ¨Uber eine Verallgemeinerung des Tschebyschef-Problems, German, Math.
Z. 174 (1980), no. 1, 35–41, MR591612.

Chebyshev conjectured that limx→∞ πe(x, χ−4) = −∞, which is equivalent [17–19] to GRH for
L(s, χ−4). Knapowski and Tur´an showed that these assertions are further equivalent to limx→∞ θl(x, r, χ−4) =
−∞. In this article, the authors establish a related implication: Let χ be a quadratic character
(mod q). Suppose that all nonreal zeros ρ = β + iγ of L(s, χ) satisfy β2 − γ2 < 1/4, a property
implied by GRH( √3
2 ). Then for 0 ≤ α < 1/2 they prove that

lim
x→∞
 ∑

p χ(p) log p
pα · exp
(
− log2 p
x
 ) = −∞.

This article cites [1, 17, 49, 56, 85, 92, 142, 144, 146].

[146] Besenfelder, H.-J., ¨Uber eine Vermutung von Tschebyschef. II, German, J. Reine Angew. Math. 313
(1980), 52–58, MR552462.

The author proves unconditionally that for all 0 ≤ α ≤ 1
2 ,

lim
x→∞
 ∑

p
 χ−4(p) log p
pα e−(log
2 p)/x = −∞,

using an explicit formula similar to the one in his prior work [142].

This article cites [1, 17–19, 78, 85, 113, 115, 142].

[147] Gallagher, P. X., Some consequences of the Riemann hypothesis, Acta Arith. 37 (1980), 339–343,
MR598886.

Under RH, the author proves that Eψ(x) ≪ (log log x)
2 except on a set of ﬁnite measure, and that
for any function f (x) tending to inﬁnity, Eψ(x) ≪ f (x) except on a set of density 0; the proofs are
similar to showing that Eψ(x) has a limiting logarithmic distribution. The method also provides
short proofs of Cram´er’s conditional estimates [21] ∫ X
1 Eψ(x)
2 dx ≪ X and ∫ X
1 Eψ(x)
2 dx
x ∼ C log X
(for an explicit constant C), as well as of Selberg’s conditional result on the normal density of primes
in short intervals.

This article cites [21].

[148] Hudson, R. H., A common combinatorial principle underlies Riemann’s formula, the Chebyshev
phenomenon, and other subtle eﬀects in comparative prime number theory. I, J. Reine Angew.
Math. 313 (1980), 133–150, MR552467.

The author outlines a combinatorial principle that seeks to explain various eﬀects and biases
in comparative prime number theory. He highlights Riemann’s original explicit formula π(x) ∼
li(x) − 1
2 li(x
1/2) − 1
3 li(x
1/3) + · · · and connects it to Chebyshev’s observation, which can be seen as
approximating π(x; 4, 3, 1) by half the number of prime squares. Arguing from a generalization of an
exact formula of Meissel, the author deduces, in the example of primes (mod 4), that an “excess” in
the number of integers of the form pq, where p and q are prime, in the class 1 (mod 4) must result
in a corresponding “deﬁciency” in the number of primes of exactly this magnitude, that is, half the
number of prime squares. A combinatorial observation gives a reason for such an excess: in counting
integers that are the product of two primes from a set, products of distinct primes are counted twice
(as pq and qp), while the prime squares are not. The author then provides similar arguments for

46 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

why cubic and higher order eﬀects should exist. Along with describing the combinatorial principle
in generality, he provides details of some numerical investigations into these eﬀects.

This article cites [1, 14, 56, 84, 85, 114].

[149] Monach, W. R., Numerical Investigation of Several Problems in Number Theory, Thesis (Ph.D.)–
University of Michigan), ProQuest LLC, Ann Arbor, MI, 1980, 180 pp., MR2631002.

In Chapter 2 of this thesis, assuming RH and LI, the author shows that the limiting logarithmic
distribution of Eψ is equal to the distribution function of the random variable ∑γ>0 2 sin(2πθγ)/|ρ|,
where the θγ are independent random variables uniformly distributed in [0, 1). The remainder of the
chapter describes methods of computing bounds on this distribution function on the interval [−1, 1]
(a table of values is included, as are the programs used to generate said table) and determining an
asymptotic formula for its derivative.

This article cites [28, 51, 74].

[150] Montgomery, H. L., The zeta function and prime numbers, in: Proceedings of the Queen’s Number
Theory Conference, 1979 (Kingston, Ont., 1979), vol. 54, Queen’s Papers in Pure and Appl. Math.
Queen’s Univ., Kingston, Ont., 1980, pp. 1–31, MR634679.

Section 3 of this article examines random variables of the form X = ∑∞
k=1 rk sin(2πθk) for {rk} a
decreasing ℓ2 sequence, where the θk are independently uniformly distributed on R/Z. The author
establishes, for any integer K ≥ 1, the bounds

P (
X ≥ 2
 K∑

k=1 rk
) ≤ exp
 (
− 3
4
 ( K∑

k=1 rk
)2( ∞∑

k=K+1 r2
k
)−1)

P (
X ≥ 1
2
 K∑

k=1 rk
) ≥ 1
240 exp
 (
−100( K∑

k=1 rk
)2( ∞∑

k=K+1 r2
k
)−1)
 ;

in addition, if δ is suﬃciently small and ∑
k : rk>δ(rk − δ) ≥ V , then

P (X ≥ V ) ≥ 1
2 exp (
− 1
2
 ∑

k : rk>δ log π2rk
2δ
 )
.

These results can be applied to the limiting logarithmic distribution function of Eψ(x), which
(assuming RH and LI) is the same as the distribution of the random variable Y = ∑
γ>0 2
|ρ| sin(2πθρ).
In particular, the second result implies that there exist constants 0 < c1 < c2 such that

exp (
−c2√
ve√
2πv) ≤ P (Y > v) ≤ exp (
−c1√
ve√
2πv)
,

which suggests the conjecture lim sup
x→∞ Eψ(x)
(log log log x)2 = 1
2π and lim inf
x→∞ Eψ(x)
(log log log x)2 = − 1
2π .

[151] Pintz, J., On the remainder term of the prime number formula. I. On a problem of Littlewood, Acta
Arith. 36 (1980), no. 4, 341–365, MR585891.

This article contains explicit oscillation results under the assumption that RH is false. Suppose that
ρ0 = β0 + iγ0 is a nontrivial zero of ζ(s). Let 0 < ε ≤ 0.02, and set A = 40,000ε−2 log γ0. Then for
H suﬃciently large in terms of ρ0, there exist x+ and x− in the interval [H, H A] such that

∆
π(x+) > (1 − ε) x
β0
+
|ρ0| log x+ and ∆
π(x−) < −(1 − ε) x
β0
−
|ρ0| log x− ,

and the same for ∆
Π(x); similarly, the result holds without the factor log x in the denominator for
∆
ψ(x) and ∆
θ(x). In all these theorems, if in addition β0 > 1
2 + ε and γ0 is suﬃciently large in
terms of ε, then by replacing the factor (1 − ε)/|ρ0| by the smaller 1/γ1+ε
0 , the localization can be
improved to the interval [H, H 1+ε]. Consequently, W f (T )/ log log T tends to inﬁnity for each of the
four functions f ∈ {π, Π, θ, ψ} (the case where RH is true having been handled by Ingham [30]).

This article cites [14, 30, 71–73, 75–79, 84, 85, 91–93, 126, 150].

[152] Pintz, J., On the remainder term of the prime number formula. II. On a theorem of Ingham, Acta
Arith. 37 (1980), 209–220, MR598876.

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 47

This article investigates the connection between the zero free region of ζ(s) and the size of the
remainder term in the prime number theorem. Let η : [1, ∞) → (0, 1
2 ] be a continuous, decreas-
ing function, and suppose that ζ(s) does not vanish when σ > 1 − η(|t|). If we deﬁne ω(x) =
mint≥1(η(t) log x + log t), then for any 0 < ε < 1,

∆
ψ(x) ≪ε x/e(1−ε)ω(x),

and the same is true for ∆
θ(x) and ∆
Π(x) and ∆
π(x). This is an improvement of a result of
Ingham [26, Theorem 22], which had a factor of 1
2 in the exponent (and additional conditions
upon η). In particular, when combined with a 1960/61 theorem of Sta´s, this result provides a
nearly lossless relationship between zero-free regions for ζ(s) and error terms in the prime number
theorem. It follows that an Ω-theorem for any of the four error terms given above actually implies
Ω±-theorems, of the same order of magnitude up to an ε in the exponent, for all four error terms,
an implication that seems extremely diﬃcult to prove directly.

This article cites [14, 26, 71–73, 75–79, 84, 85, 91–93, 126, 150].

[153] Pintz, J., On the remainder term of the prime number formula. V. Eﬀective mean value theorems,
Studia Sci. Math. Hungar. 15 (1980), no. 1-3, 215–223, MR681441.

For any of the functions f ∈ {π, Π, θ, ψ}, the author establishes lower bounds for the integrated
absolute error term Af
|1|(x). The main theorem of this article states that if β0 + iγ0 is a zero of

the Riemann zeta function, then Af
|1|(Y )/Y ≥ Y β0e−2
√log Y (log log Y )2 when Y is suﬃciently large in
terms of γ0. The author sketches a modiﬁcation of the proof that yields the stronger lower bound
Af
|1|(Y )/Y ≥ Y β0e−18(log Y )1/3(log log Y )4/3.

This article cites [21, 31, 40, 55, 58, 124, 135, 140, 151, 152, 154].

[154] Pintz, J., On the remainder term of the prime number formula. VI. Ineﬀective mean value theorems,
Studia Sci. Math. Hungar. 15 (1980), no. 1-3, 225–230, MR681442.

This article concerns the absolute averages A|1| of various standard error terms for prime counting
functions. When Y is suﬃciently large (ineﬀectively), the author proves that

Aπ
|1|(Y ) > 0.62 Y 3/2

log Y , AΠ
|1|(Y ) > 9 · 10−5 Y 3/2

log Y ,

Aθ
|1|(Y ) > 0.62Y 3/2, Aψ
|1|(Y ) > 10−4Y 3/2.

Thanks to work of Cram´er [21], if RH is true then these bounds are best possible up to the leading
constants (and even those constants are not too far oﬀ). Under RH, the author can improve some of
these constants and also better localize the implied large values of the error terms; indeed, the lower
bounds for the A|1| are derived from the existence of large oscillations of the error terms, rather
than the other way around.

This article cites [21, 30, 153].

[155] Pintz, J., Oscillatory properties of M (x) = ∑n≤x µ(n). II, Studia Sci. Math. Hungar. 15 (1980),
no. 4, 491–496, MR688630.

The author shows that M (x) changes sign in the interval [Y exp(−3 log
3/2
2 Y ), Y ] for all suﬃciently
large Y , which improves the main result in [160]. The proof uses upper and lower bounds for an
integral of the form ∫ w
v |M (x)|x
−1−θ dx, where θ is the maximal real part of the zeros of ζ(s) for
|t| ≲ log Y .

This article cites [11, 49, 70, 100, 102, 140, 160, 163].

[156] Tanaka, M., A numerical investigation on cumulative sum of the Liouville function, Tokyo J. Math.
3 (1980), no. 1, 187–189, MR584557.

This article reports on the sign changes of L(x) for x ≤ 109. In particular, the author shows that
906,150,256 is the smallest integer n ≥ 2 such that L(n) > 0.

This article cites [35, 59].

[157] Tanaka, M., On the M¨obius and allied functions, Tokyo J. Math. 3 (1980), no. 2, 215–218, MR605090.

48 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

Deﬁne Bk = ζ ( k
2 ) /ζ ( 1
2 ) ζ(k) if k ≥ 3 is odd and Bk = 1/ζ ( 1
2 ) ζ ( k
2 ) if k ≥ 4 is even. The author
shows that ∑n≤x µk(x) − Bk√
x = Ω±(
√
x) for each k ≥ 3, generalizing classical oscillation results
for M (x) (which is the case k = 2) and L(x) (which is the case k → ∞).

This article cites [35, 44].

[158] Anderson, R. J. and Stark, H. M., Oscillation theorems, in: Analytic number theory (Philadelphia,
Pa., 1980), vol. 899, Lecture Notes in Math. Springer, Berlin-New York, 1981, 79–106, MR654520.

The authors disprove several conjectures using a theorem of Landau and the locations of zeros of
ζ(s). The authors also show that for conjectures of a certain type (such as von Sterneck’s conjec-
ture [12, 13] |M (x)| < 1
2 √
x for x > 200 and P´olya’s problem [20] L(x) ≤ 0 for x ≥ 2), a single
counterexample implies inﬁnitely many counterexamples. In particular, using the known counterex-
amples from Neubauer [80] that EM (x) > 0.557 for x = 7.76 × 109, and from Lehman [59] that
EL(x) > 0.023 for x = 9.064 × 108, the authors conclude that lim supx→∞ EM (x) > 0.557 and
lim supx→∞ EL(x) > 0.023.

This article cites [35, 41, 43, 51, 59, 80, 89, 111, 112, 114, 117, 121, 123, 143].

[159] Chen, W. W. L., On the error term of the prime number theorem and the diﬀerence between the
number of primes in the residue classes modulo 4, J. London Math. Soc. (2) 23 (1981), no. 1, 24–40,
MR602236.

It was conjectured in [56] that ∑
n≤x Eπ(n) ∼ x and ∑
n≤x Eπ(n; 4, 3, 1) ∼ x; in this article the
author disproves these conjectures. Deﬁning the function R(x) = ∑n≤x Eψ(n) he shows that R(x) =
Ω±(x
1/2+Θ−ε) for every ε > 0, which can be improved to R(x) = Ω±(x
1/2+Θ) under SA. The same
results hold for P (x) − x in place of R(x), where P (x) = − ∑
n≤x Eπ(n). In these theorems, the
author notes that ψ(n) and π(n) can also be replaced by ψ(n; 4, 1, 3) and π(n; 4, 1, 3).

This article cites [56].

[160] Pintz, J., On the sign changes of M (x) = ∑n≤x µ(n), Analysis 1 (1981), no. 3, 191–195, MR660714.

Assuming RH(T ), the author shows that M (x) changes sign in the interval [Y 1−1/(T −2), Y 1+1/(T −2)]
for every suﬃciently large Y . Consequently, using Brent’s veriﬁcation of RH for the ﬁrst 7 ·107 zeros
of ζ(s), the author concludes that M (x) changes sign in every interval of the form [Y 1−10
−7 , Y ] for
all suﬃciently large Y , which improves the main result in [102].

This article cites [70, 83, 100, 102].

[161] Bentz, H.-J., Discrepancies in the distribution of prime numbers, J. Number Theory 15 (1982),
no. 2, 252–274, MR675189.

For 0 ≤ α < 1
2 , the author shows unconditionally that
∑

p χ−4(p) log p
pα e−(log x)2/p ∼ − √
πx
2 ex(1−2α)2/16;

when α = 1
2 , the right-hand side must be replaced by 1
4 √
πx. Both results remain valid if χ−4 is
replaced by χ−3. These results can be interpreted as comparing (in a speciﬁc way) the residue class
1 to the other reduced residue class modulo 4 or 3. Analogously, when α = 1
2 , the author establishes
the same result when comparing 1 (mod 8) to another reduced residue class (mod 8); if two reduced
residue classes (mod 8) are compared, the resulting expression is bounded. The author asserts that
the required hypotheses on zeros of relevant Dirichlet L-functions is that they do not vanish in the
“bowtie” {s : σ > 0, 0 < |t| < |σ − 1
2 |}. The author also presents some numerical data concerning
the prime number race (mod 3).

This article cites [17–19, 26, 48, 56, 71–73, 75–79, 84, 85, 91–93, 96, 118, 133, 142, 144, 146].

[162] Bentz, H.-J. and Pintz, J., ¨Uber das Tschebyschef-Problem, German, Resultate Math. 5 (1982),
no. 1, 1–5, MR662791.

The authors give a shorter proof that lim
x→∞
 ∑

p χ−4(p) log p · exp (− log
2 p
x
 ) = −∞.

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 49

This article cites [1, 17–19, 56, 85, 142, 146].

[163] Pintz, J., Oscillatory properties of M (x) = ∑n≤x µ(n). I, Acta Arith. 42 (1982), no. 1, 49–55,
MR678996.

This article is concerned with oscillations in the Mertens sum. The natural diﬃculty of this problem
comes from the fact that the explicit formula for M (x) contains terms of the form x
ρ/ρζ′(ρ), which
are more diﬃcult to handle than the terms x
ρ/ρ appearing in the explicit formula for ∆
ψ(x). The
author proves that if ρ0 = β0 + iγ0 is a zero of ζ(s), then for Y > e|γ0|+4,

1
Y
 ∫ Y

Y /(100 log Y ) |M (x)| dx > 1
6|ρ0|3 Y β0 and max
x≤Y |M (x)| ≥ 1
6|ρ0|3 Y β0.

Consequently, using the ﬁrst zeta zero 1
2 + iγ1 with γ1 ≈ 14.1347,

max
Y /(100 log Y )≤x≤Y |M (x)| ≥ 1
17,000
 √Y

for Y ≥ 2; the constant 1/17,000 can be improved but not enough to disprove the Mertens conjecture.

This article cites [40, 101].

[164] Sta´s, W., On sign-changes in the remainder term of the prime ideal formula, Funct. Approx. Com-
ment. Math. 13 (1982), 159–166, MR817334.

The author proves an analogue of a result of Knapowski [65] for the error term of the prime ideal
theorem. More precisely he shows that for a number ﬁeld K whose Dedekind zeta function ζK (s)
satisﬁes HC, and an arbitrary zero ρ0 = β0 + iγ0 of ζK,

∆
ψ(T, K) = Ω±
(
T β0 exp
(
−15 log T
√
log log T
 ))
.

The author also gives a lower bound on the number of sign changes of ∆
ψ(T, K).

This article cites [45, 65, 68, 85, 151].

[165] Bays, C. and Hudson, R. H., The cyclic behavior of primes in the arithmetic progressions modulo
11, J. Reine Angew. Math. 339 (1983), 215–220, MR686708.

The authors plot the ten functions Aπ
1 (x, 11, a) (1 ≤ a ≤ 10) for x up to 2 · 109 and note some
surprising phenomena. First, the residue class a such that Aπ
1 (x, 11, a) is in last place among the ten
functions cycles over the quadratic residues in the order 9, 92, 93, 94, 95 with only minor deviations.
Second, when a is the residue class in last place, there is a strong tendency for 11 − a to be the
residue class in ﬁrst place. The authors say that this second tendency remains pronounced for prime
moduli up to 47, and speculate as to whether further averaging might enhance the ﬁrst phenomenon
for larger moduli.

This article cites [56, 84, 85, 91, 133].

[166] Kolesnik, G. and Straus, E. G., On the sum of powers of complex numbers, in: Studies in pure
mathematics, Birkh¨auser, Basel, 1983, 427–442, MR820241.

The authors examine the second main theorem of the power-sum method, obtaining the constant
B = 4e which is best possible by [86]. When m ≤ n they also give the larger lower bound

|sv| ≥ n!(2m + n)!
2n(2m + 2n)!√
2m + 2n + 1 min
1≤j≤n |b1 + · · · + bj|.

This article cites [47, 86].

[167] Pintz, J., On the distribution of square-free numbers, J. London Math. Soc. (2) 28 (1983), no. 3,
401–405, MR724708.

The author shows AQk
|1| (x) ≫ Y 1/2k for each k ≥ 2 using an unexpectedly simple argument, with
eﬀective estimates whose dependence on k is explicit. These results signiﬁcantly strengthen work of
Evelyn–Linfoot [24] and K´atai [102].

This article cites [24, 102].

50 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

[168] Pintz, J., Oscillatory properties of the remainder term of the prime number formula, in: Studies in
pure mathematics, Birkh¨auser, Basel, 1983, pp. 551–560, MR820251.

The author establishes two theorems that improve and simplify prior work of Tur´an and of Ingham.
The ﬁrst theorem states that if ζ(β0 + iγ0) = 0, then for T suﬃciently large in terms of γ0, there
exists an x ∈ [T 1/4, T ] for which |∆
ψ(x)| ≫γ0 x
β1 (with an explicit dependence on γ0). The second
theorem assumes that ζ(s) ̸= 0 in a region of the shape σ ≥ 1 − η(t) where η is continuous and
decreasing, and, deﬁning ω(x) = mint≥0(η(t) log x + log t), concludes that ∆
ψ(x) = Ω(x/e54ω(x)).
The main tool is the power-sum estimate of S´os and Tur´an. Near-optimal improvements (by the
author) of these two results appeared slightly earlier [151, 152].

This article cites [3, 26, 39, 40, 47, 151, 152].

[169] Robin, G., Sur l’ordre maximum de la fonction somme des diviseurs, French, in: Seminar on number
theory, Paris 1981–82 (Paris, 1981/1982), vol. 38, Progr. Math. Birkh¨auser Boston, Boston, MA,
1983, 233–244, MR729173.

The author investigates the function σ(n)
n and proves that RH is true if and only if σ(n)
n < eC0 log log n
when n is suﬃciently large. If (Ck) is the sequence of colossally abundant numbers, the author further
shows that (σ(Ck)/Ck log log Ck) has inﬁnitely many local extrema. Finally, the author shows that
if RH is false, then both ∆
πr (x) and ∏
p≤x(1 − 1
p ) − 1/eC0 log x change signs inﬁnitely often.

This article cites [74, 99, 124].

[170] Kaczorowski, J., On sign-changes in the remainder-term of the prime-number formula. I, Acta Arith.
44 (1984), no. 4, 365–377, MR777013.

This article establishes a lower bound on the growth of the number of sign changes of ∆
ψ(x) and
∆
Π(x). Speciﬁcally, the author proves that W ψ(T ) ≥ γ1
4π log T (and the same for W Π(x)) when T
is suﬃciently large (eﬀectively), where γ1 ≈ 14.1347 is the smallest ordinate of a nontrivial zero
of ζ(s). The key technique is to bound W ψ(T ) below by W (
A
ψ
n ; T )
, the number of sign changes
of repeated logarithmic integrals of ∆
ψ(x); using the fact that the second-lowest nontrivial zero of
ζ(s) has imaginary part exceeding 15, the author derives an explicit formula for W (
A
ψ
n ; T ) when
n ≍ log T is suitably chosen.

This article cites [8, 14, 17, 23, 26, 27, 30, 46, 65, 66, 97, 126–129, 135, 140].

[171] Pintz, J., On the partial sums of the M¨obius function, in: Topics in classical number theory, Vol.
I, II (Budapest, 1981), vol. 34, Colloq. Math. Soc. J´anos Bolyai, North-Holland, Amsterdam, 1984,
1229–1250, MR781183.

The author investigates sign changes of M (x) using lower bounds for AM
|1|(Y ). He shows that if
ζ(ρ0) = 0, then AM
|1|(Y ) > Y 1+β0/6|ρ0|3 for Y > e|γ0|+4, an eﬀective improvement of an ineﬀec-
tive inequality of K´atai that provides the ﬁrst eﬀective disproof for the Mertens conjecture when
RH is false. The author further concludes that M (x) changes sign in every interval of the form
[Y exp(−3 log
3/2
2 Y ), Y ] when Y is suﬃciently large.

This article cites [4, 9, 11, 35, 53, 63, 64, 90, 95].

[172] Pintz, J., On the remainder term of the prime number formula and the zeros of Riemann’s zeta-
function, in: Number theory, Noordwijkerhout 1983 (Noordwijkerhout, 1983), vol. 1068, Lecture
Notes in Math. Springer, Berlin, 1984, pp. 186–197, MR756094.

This article is primarily a summary of the results to be proved in the series [151–155, 160] by the
author. The main functions of interest are S(x) = max0≤u≤x |∆
ψ(u)| and Aψ
|1|(x) = ∫ x
0 |∆
ψ(u)| du.

The following theorem is proved: Deﬁne ω(x) = log x
Z(x) , where Z(x) = maxρ xβ
|γ| . Then

log x
S(x) ∼ log x
2

Aψ
|1|(x) ∼ ω(x).

In particular, this implies that S(x) and 1
x Aψ
|1|(x) are close in value, that is, the mean and maximum
of |∆
ψ(u)| are close. The proof uses a zero-density theorem of Carlson (for the upper bounds) and
the power-sum method (for the lower bounds).

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 51

This article cites [14, 26, 46, 55, 61, 65, 66, 126, 127, 151–155, 160, 170].

[173] Pintz, J., Oscillatory properties of M (x) = ∑n≤x µ(n). III, Acta Arith. 43 (1984), no. 2, 105–113,
MR736725.

By reﬁning the proof method in his previous work [155], the author proves that if ρ0 = β0 + iγ0 is
a zero of ζ(s), then when Y is suﬃciently large in terms of γ0,

max
x∈[Y exp(−5(log log Y )5/2),Y ] M (x)
xβ0 > 1
48|ρ0|3 , min
x∈[Y exp(−5(log log Y )5/2),Y ] M (x)
xβ0 < − 1
48|ρ0|3 .

This article cites [70, 90, 100, 102, 140, 155, 163].

[174] Pintz, J. and Salerno, S., Irregularities in the distribution of primes in arithmetic progressions. II,
Arch. Math. (Basel) 43 (1984), no. 4, 351–357, MR802311.

The authors elaborate on their work in [176] to handle prime number races where a bias is present.
Again assuming a ﬁnite Riemann–Piltz conjecture, they show that when Y is suﬃciently large,

1
Y
 ∫ Y

Y 1−7/λ |π(x; q, ℓ1, ℓ2)| dx ≥ √
Y exp (− 9 log Y
λ − c3qλ(log log Y )
2) ,

(and the same for θ in place of π) for any λ satisfying
√
log Y
√q log log Y < λ < c2 log Y

q (log log Y )
2 .

They ﬁrst deal with the case when both ℓ1 and ℓ2 are quadratic residues (mod q), using an explicit
formula involving zeros of both L(s, χ) and L(2s, χ). In the remaining case when ℓ1 is a residue and
ℓ2 is a nonresidue, there is an additional term corresponding to the pole of L(2s, χ0) at s = 1
2 .

This article cites [58, 62, 69, 176].

[175] Pintz, J. and Salerno, S., On the comparative theory of primes, Ann. Scuola Norm. Sup. Pisa Cl.
Sci. (4) 11 (1984), no. 2, 245–260, MR764945.

The authors obtain new estimates on ψ(x; q, ℓ1, ℓ2) for arbitrary residues ℓ1, ℓ2. Assuming GRH(cq2 log6 q, E(q)),
the authors prove that for Y suﬃciently large, there exists

x ∈
 [

Y exp
 (
− cq
√
E(q) (log Y )
1/2(log log Y )
3/2)
 , Y
 ]

such that
 ψ(x; q, ℓ1, ℓ2) > √Y exp
 (
− cq
√
E(q) (log Y )
1/2(log log Y )
3/2)
 .

This is an improvement over the work of Knapowski and Tur´an both in the localization and in the
lower bound. The authors improve the power-sum bounds used by Knapowski and Tur´an to prove
their results.

This article cites [11, 71–73, 75–79, 89].

[176] Pintz, J. and Salerno, S., Irregularities in the distribution of primes in arithmetic progressions. I,
Arch. Math. (Basel) 42 (1984), no. 5, 439–447, MR756697.

Assuming a ﬁnite Riemann–Piltz conjecture, the authors show that when Y is suﬃciently large,
∫ Y

Y 1−7/λ ψ(x; q, ℓ1, ℓ2) dx
x ≫ √
Y exp (
− 2 log Y
λ − c3qλ log2 Y )

(and the same for Π in place of ψ) for any λ satisfying
√
log Y
√q log log Y < λ < c2 log Y
q(log log Y )2 .

Essentially any such choice of λ improves upon analogous results of Knapowski [58, 62, 69]. The proof
also works for ψ replaced by θ or π, but only if ℓ1 and ℓ2 are both quadratic nonresidues (mod q).

This article cites [58, 62, 69, 92, 182].

52 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

[177] Tur´an, P., On a new method of analysis and its applications, Pure and Applied Mathematics (New
York), John Wiley & Sons, Inc., New York, 1984, pp. xvi+584, MR749389.

This is a comprehensive work on the power-sum method, completed with the assistance of G. Hal´asz
and J. Pintz and including a foreword by V. T. S´os. The ﬁrst part of the book introduces the method,
while the second and larger part discusses a wide range of applications. Chapters 48–56 are directly
related to comparative prime number theory.

[178] Ellison, W. and Ellison, F., Prime numbers, A Wiley-Interscience Publication, John Wiley & Sons,
Inc., New York; Hermann, Paris, 1985, pp. xii+417, MR814687.

This book is an English translation of [124].

[179] Hudson, R. H., Averaging eﬀects on irregularities in the distribution of primes in arithmetic pro-
gressions, Math. Comp. 44 (1985), no. 170, 561–571, MR777286.

The author presents data on Eπ(x; 6, 5, 1) for x ≤ 2.5 · 1011. He proves (acknowledging A. Schinzel’s
help) that limx→∞ Eπ(x; 6, 5, 1) ̸= 1, and gives a heuristic argument that limx→∞ EAπ
m (x; 6, 5, 1) ̸= 1
for every m ∈ N. On the other hand, he shows that limm→∞ lim supx→∞ EAπ
m (x; 6, 5, 1) = 1 and
similarly for lim inf x→∞.

This article cites [84, 85, 91–94, 124].

[180] Kaczorowski, J., On sign-changes in the remainder-term of the prime-number formula. II, Acta
Arith. 45 (1985), no. 1, 65–74, MR791085.

The author proves unconditionally that W π(T ) ≫ log T , though with an ineﬀective constant, and
the same for W θ(T ). He also proves unconditionally that lim inf T →∞ W ψ(T )/log T ≥ γ(Θ)/π, where
γ(Θ) is the smallest γ > 0 such that ζ(Θ + iγ) = 0 (or γ(Θ) = ∞ if Θ is not attained); this improves
a result of P´olya [23], which had lim sup in place of lim inf. He remarks that if RH is false, then
the proof of this latter result can be extended to W θ(T ) and (with a bit more diﬃculty) to W Π(T )
and W π(T ). As in a previous article, the proofs of both theorems make use of the iterated averages
A
f
n(x).

This article cites [14, 17, 23, 30, 65, 66, 126–129, 170].

[181] Odlyzko, A. M. and Riele, H. J. J. te, Disproof of the Mertens conjecture, J. Reine Angew. Math.
357 (1985), 138–160, MR783538.

The authors disprove the Mertens conjecture by showing that

lim inf
x→∞ EM (x) < −1.009 and lim sup
x→∞ EM (x) > 1.06.

The method, based upon work of Ingham, is to ﬁnd values of hK(y) = ∑ρ k(γ) e
iγy
ρζ′(ρ) that are large
in absolute value, using the kernel k(t) = g(t/T ) with T = 2,515.286 . . . the height of the 2,000th
zero of ζ(s), where
 g(t) =
 {(1 − |t|) cos(πt) + π−1 sin(π|t|), |t| ≤ 1
0, |t| ≥ 1.

The key development is the algorithm due to Lenstra, Lenstra, and Lov´asz for ﬁnding short vec-
tors in lattices, which reduces the computation time needed to ﬁnd an appropriate inhomogeneous
Diophantine approximation. The authors begin with a summary of past work on the conjecture
and conclude with remarks on future work towards ﬁnding explicit counterexamples to Mertens
conjecture, discussing limitations of their method.

This article cites [5, 7, 12, 13, 35, 42, 51, 59, 105, 111, 112, 121, 125, 143, 158, 173].

[182] Pintz, J. and Salerno, S., Accumulation theorems for primes in arithmetic progressions, Acta Math.
Hungar. 46 (1985), no. 1-2, 151–172, MR819064.

Assuming HC(Eq) and GRH(D) with D ≥ D0 = c0q2 log6 q and λ ≥ 20D0, the authors show that
when T is suﬃciently large, there exists some k and some x near T such that

ψl(x, 4k; q, a, b) > √
x exp
(
− LD2

λ2 − cq2

Eq λ log3 L)
.

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 53

The main tool in the proof is a “one-sided” version of the second main theorem of the power-sum
method. When both a and b are quadratic residues or nonresidues, the same result holds with ψl
replaced by θl.

This article cites [1, 11, 49, 84, 85, 91, 92].

[183] Kaczorowski, J. and Pintz, J., Oscillatory properties of arithmetical functions. I, Acta Math. Hungar.
48 (1986), no. 1-2, 173–185, MR858395.

The authors improve upon and extend results of Landau [10], P´olya [23], and Grosswald [89].
Given a Dirichlet integral F (s) = ∫ ∞
x0 f (x)x
−s−1 dx converging on a right half-plane {σ > θ},
with a continuation to a larger half-plane except for perhaps countably many poles or logarith-
mic singularities (in a precise sense), the authors show that lim inf T →∞ W (f,T )
log T ≥ γ
π where γ =
inf{|t| : F (s) is not regular at θ + it}. This result implies ≫ log T sign changes of the functions
M (x) and ∆
Qk (x), as well as of ψ(x; q, ℓ1, ℓ2) assuming HC. For a slightly more restricted class of
functions, the authors prove an eﬀective version of a similar result, again guaranteeing ≫ log T sign
changes (essentially using a single singularity of F (s)) but now with eﬀective constants.

This article cites [10, 23, 76, 77, 89, 99, 101, 128, 155, 170, 180].

[184] Pintz, J. and Salerno, S., Some consequences of the general Riemann hypothesis in the comparative
theory of primes, J. Number Theory 23 (1986), no. 2, 183–194, MR845900.

The authors establish the eﬀective results maxY 7/8≤x≤Y Eψ(x; q, a1, a2) > e−qc1 and maxB2(Y )≤x≤Y Eψ(x; q, a1, a2) ≫
(log Y )
−qc2 , where B2(Y ) ≫ Y (log Y )
−qc3 , as well as the same statements where ψ is replaced by θ,
Π, or π. Furthermore, the authors show that W ψ(Y ) ≫q (log Y )/ log log Y with explicit constants,
and similarly with ψ replaced by Π or, if a1 and a2 are both quadratic residues or both quadratic
nonresidues modulo q, with θ or π.

This article cites [71–73, 75–79, 175, 176].

[185] Robin, G., Irr´egularit´es dans la distribution des nombres premiers dans les progressions arithm´etiques,
French, Ann. Fac. Sci. Toulouse Math. (5) 8 (1986), no. 2, 159–173, MR928842.

This article examines, assuming HC, the asymptotic behavior of the weighted average P(x) =
∑n≤x ˚∆(n; k, ℓ)n−α logβ n where α and β are ﬁxed real numbers. If GRH is false, then P(x) ≪
1 + x
1−α+Θk logβ−1 x and P(x) = Ω±(x
1−α+Θk−ε); under the additional assumption of SA, we have
P(x) = Ω±(x
1−α+Θk logβ−1 x) (which is thus best possible for α < 1 + Θk).

If GRH is true, the behavior depends more signiﬁcantly upon α and β. When α > 3
2 , we have
P(x) ≪ 1. When α = 3
2 , we have P(x) ≪ 1 if β < 0, and P(x) = (1 − ck(ℓ)) log log x + O(1) if β = 0,
and P(x) = (1 − ck(ℓ))(log x)
β/β + O((log x)
β−1 log log x) if β > 0. Finally, when α < 3
2 , we have
P(x) ≪ x
3/2−α logβ−1 x. This theorem disproves Shanks’s conjecture ∑
n≤x π(n; 4, 3, 1)n1/2/π(n) ∼
x, as well as corresponding conjectures for other moduli. Moreover, it shows that Brent’s conjecture∑n≤x π(n; 4, 3, 1)/n1/2π(n) ∼ log x is equivalent to GRH.

Again assuming GRH and α < 3
2 , the author asserts that for certain moduli including 3, 4, 5, 6, 7, 8,
9, 10, 12, there exists a constant αk,ℓ such that for α > αk,ℓ, when x is suﬃciently large then P(x) < 0
if ℓ is a quadratic residue and P(x) > 0 if ℓ is a quadratic nonresidue. (It seems that this result
actually holds for all moduli k ≥ 3.) On the other hand, for some moduli including 23, 43, 67, 163,
there exists a constant α
′
k,ℓ such that for α < α
′
k,ℓ, we have P(x) = Ω±(x
3/2−α logβ−1 x).

This article cites [17–19, 48, 56, 71–73, 75–79, 84, 85, 91–93, 96, 114, 118, 122, 124, 144, 158, 159,
161].

[186] Titchmarsh, E. C., The theory of the Riemann zeta-function, Second, Edited and with a preface by
D. R. Heath-Brown, The Clarendon Press, Oxford University Press, New York, 1986, pp. x+412,
MR0882550.

This book is the second edition of the classical and comprehensive treatise on the theory of the
Riemann zeta-function, now with a large number of chapter-end notes by Heath-Brown. Chapter XII
contains the asymptotic formula for the error term in the divisor problem and relevant upper bounds
and oscillation results. Chapter XIV contains an explicit formula for M (x) and its upper bounds
and oscillations, as well as a connection between its mean-square average and the simplicity of zeros

54 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

of ζ(s); in the chapter-end notes, it is noted that the Mertens conjecture has been disproved and
Tur´an’s problem has been resolved in the negative.

This article cites [35, 51, 125, 181].

[187] Kaczorowski, J., On sign-changes in the remainder-term of the prime-number formula. III, Acta
Arith. 48 (1987), no. 4, 347–371, MR927376.

This article examines W (∆
ψ
e ; T ), the number of sign changes of ∆
ψ
e (x) = ∑∞
n=1(Λ(n)−1)e−n/x in the
interval [0, T ]. The author ﬁrst proves that SA (which he calls “Ingham’s condition”) is equivalent
to the assertion that W (
∆
ψ
e ; [T, eT ]) ≪ 1 uniformly for T > 0, which is further equivalent to
each of lim supT →∞ W (∆
ψ
e ; T ) < ∞ and lim inf T →∞ W (∆
ψ
e ; T ) < ∞. Assuming SA and LI(Θ), the
author proves that W (∆
ψ
e ; T ) ∼ κ log T as T → ∞, for a constant κ (given by an explicit integral)
depending on the zeros of ζ(s) on the line σ = Θ. Finally, assuming RH, the author proves that
W (∆
ψ
e ; T ) = γ1
π log T +O(1), where γ1 ≈ 14.1347 is the smallest ordinate of a nontrivial zero of ζ(s),
and indeed that these sign changes are extremely regularly spaced and correspond to oscillations
that are ≫ √
x. These results support the author’s conjecture that W (∆
ψ
e ; T ) ∼ c log T as T → ∞.

This article cites [17, 30, 67, 170, 180].

[188] Kaczorowski, J. and Pintz, J., Oscillatory properties of arithmetical functions. II, Acta Math. Hun-
gar. 49 (1987), no. 3-4, 441–453, MR891057.

The authors extend their earlier results to obtain ≫ log T sign changes for functions such as
∆
Π(x; q, a), ∆
π(x; q, a) where a is a quadratic nonresidue, ∆
Π(x; q, a, b) where a ̸≡ b (mod q), and
so on. They also similarly obtain sign changes (in relatively short intervals) for the error term in
the asymptotic formula for the counting function of irreducible elements in the ring of integers OK
of a number ﬁeld K, assuming the Dedekind zeta function of the Hilbert class ﬁeld of K does not
vanish on the interval [1/2, 1) and has at least one simple zero in the half-plane σ > 1/2.

This article cites [30, 170, 180, 183].

[189] Pintz, J., An eﬀective disproof of the Mertens conjecture, Ast´erisque (1987), no. 147-148, 325–333,
346, MR891440.

The disproof of the Mertens conjecture by Odlyzko and te Riele [181] does not provide any eﬀective
counterexample. In this article, the author shows that there exists x < exp(3.21 · 1064), such that
|M (x)| > √x.

This article cites [4, 35, 125, 181].

[190] Riele, H. J. J. te, On the sign of the diﬀerence π(x) − li(x), Math. Comp. 48 (1987), no. 177, 323–
328, MR866118.

The author shows that π(x) > li(x) for some 6.62 × 10370 ≤ x ≤ 6.69 × 10370, thereby improving
the previous best estimate, 1.65 × 101165, for Skewes’s number found by Lehman [97]. Using an
explicit formula for Eπ(eu) averaged by a Gaussian kernel, Lehman had found three candidates for
x near which π(x) > li(x), namely e727.952, e853.853, and e2,682.977. Lehman showed that e2,682.977

produced an actual example; using the zeros of ζ(s) up to height 5 × 104, found on a CYBER
205 supercomputer located at the Academic Computer Centre Amsterdam, the author shows that
e853.853 produces an actual example. The author speculates that zeros up to height 4 × 105 would
be required to determine whether there is an actual example around e727.952.

This article cites [14, 46, 97].

[191] Balasubramanian, R., Ramachandra, K., and Subbarao, M. V., On the error function in the asymp-
totic formula for the counting function of k-full numbers, Acta Arith. 50 (1988), no. 2, 107–118,
MR945261.

For k ≥ 2, let Nk(x) be the number of k-full numbers up to x, which is known to admit an
asymptotic formula of the form Nk(x) = ∑
k≤j≤2k−1 bjx
1/j + ∆k(x). In this article, the authors
show that ∆2(x) = Ω(x
1/10), while ∆k(x) = Ω(x
1/2(k+r)) for k ≥ 3 where r is the smallest positive
integer such that r(r − 1) ≥ 2k. Their method was to establish a lower bound on a weighted average
of |∆k(x)|.

This article cites [42, 50].

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 55

[192] Fujii, A., Some generalizations of Chebyshev’s conjecture, Proc. Japan Acad. Ser. A Math. Sci. 64
(1988), no. 7, 260–263, MR974088.

The author shows if 0 < α ≤ 4, then the statement limx→∞ ∑p χ−4(p)e−(p/x)α = −∞ is equivalent
to GRH for L(s, χ−4), generalizing earlier results for α = 1. Further, the author deﬁnes ξ(x, k) by
Γ(s)
k = ∫ ∞
0 x
s−1ξ(x, k) dx and shows the statement limx→∞ ∑
p χ−4(p) log p · ξ(p/x, 2) = −∞ is
also equivalent to GRH for L(s, χ−4). The author conjectures that the ﬁrst equivalence holds for
any α > 0 and the second (without the factor log p) for any integer k ≥ 1. He also remarks that
the method can be used for other weight functions involving exponentials and Bessel functions,
including Knapowski–Tur´an’s function e− log
2(p/x).

This article cites [18, 19, 144].

[193] Kaczorowski, J., On sign-changes in the remainder-term of the prime-number formula. IV, Acta
Arith. 50 (1988), no. 1, 15–21, MR945273.

The author proves, when Θ > 1
2 , that for any ε > 0 we have maxT ≤x≤(1+ε)T |∆
ψ
e (x)| ≫ε T Θ−ε. In
light of the author’s previous results [187] that assumed RH, it follows that unconditionally (but
ineﬀectively), maxT ≤x≤(1+ε)T |∆
ψ
e (x)| ≫ε √
T . The author also deduces that W ψ
e (T ) = o(log2 T ),
and sketches a construction (of a “barrier”) showing that this result cannot be improved without
further information on the zeros of ζ(s).

This article cites [45, 58, 67, 170, 180, 187].

[194] Kaczorowski, J. and Sta´s, W., On the number of sign changes in the remainder-term of the prime-
ideal theorem, Colloq. Math. 56 (1988), no. 1, 185–197, MR980524.

The author shows that if K is a number ﬁeld such that HC holds for ζK (s), then for any 0 < ε < 1
one has W ψK (T ) ≥ (1 − ε) γK
π log T when T is suﬃciently large in terms of K and ε. The assumption
of no real zeros can be removed if the contribution from the real zeros is subtracted from EψK (x).

This article cites [30, 68, 164, 170].

[195] Kaczorowski, J. and Sta´s, W., On the number of sign-changes in the remainder-term of the prime-
ideal theorem, Discuss. Math. 9 (1988), 83–102 (1989), MR1042465.

This article is identical to [194].

[196] Gonek, S. M., On negative moments of the Riemann zeta-function, Mathematika 36 (1989), no. 1,
71–88, MR1014202.

The author provides arguments supporting Hejhal’s conjecture [197] that
∑

0<γ≤T
 1
|ζ′(ρ)|2k ≍ T (log T )
(k−1)2

for k > 0, and suggests that the conjecture could be extended to k ≤ 0. Assuming RH and the
simplicity of all zeros of ζ(s), the author shows that
∑

0<γ≤T
 1
|ζ′(ρ)|2 ≫ T

and conjectures that ∑

0<γ≤T
 1
|ζ′(ρ)|2 ∼ 3
π3 T.

This article cites [186, 197].

[197] Hejhal, D. A., On the distribution of log |ζ′( 1
2 + it)|, in: Number theory, trace formulas and discrete
groups (Oslo, 1987), Academic Press, Boston, MA, 1989, pp. 343–370, MR993326.

Studying the value distribution of log |ζ′( 1
2 + it)|, the author conjectures that for k > 0,
∑

0<γ≤T
 1
|ζ′(ρ)|2k ≍ T (log T )
(k−1)2,

56 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

which would imply that ∑
0<γ≤T 1/|ρζ′(ρ)| diverges; the author conjectures that ∑
0<γ≤T 1/|ρζ′(ρ)|2k

converges if and only if k > 1
2 .

This article cites [42].

[198] Szyd lo, B., ¨Uber Vorzeichenwechsel einiger arithmetischer Funktionen. I, German, Math. Ann. 283
(1989), 139–149, MR0973808.

This article concerns eﬀective results of the type W (f ; X) ≥ c log X for X ≥ X0, using a modiﬁcation
of Kaczorowski’s method with a more general averaging operator x
−d−k ∫ x
0 f (ξ)ξd+k−1 dξ.

This article cites [14, 170, 180, 183, 199].

[199] Szyd lo, B., ¨Uber Vorzeichenwechsel einiger arithmetischer Funktionen. II, German, Math. Ann. 283
(1989), 151–163, MR0973808.

The author uses his results from [198] to give explicit lower bounds for the number of sign changes of
∆
ψ(X). He shows unconditionally that W ψ(X) ≥ 0.013 log X when X ≥ 102250, the proof requiring
minimal computation, as well as the similar results W ψ(X) ≥ 0.994 γ1
π log X for X ≥ exp(198,594)
and W ψ(X) ≥ 0.99999997 γ1
π log X for X ≥ exp(9 × 1014); here γ1 ≈ 14.1347 is the smallest ordinate
of a nontrivial zero of ζ(s). Assuming RH(H) for some H ≥ 501.5, he further shows that W ψ(X) ≥
(1 − 3
H ) γ1
π log X when X ≥ exp(0.09 max{4400, H}).

This article cites [170, 180, 183, 198].

[200] Szyd lo, B., ¨Uber Vorzeichenwechsel einiger arithmetischer Funktionen. III, German, Monatsh. Math.
108 (1989), 325–336, MR1029966.

The author generalizes his results [198, 199] on the number of sign changes in W ψ(x) to algebraic
number ﬁelds. Let K be an algebraic number ﬁeld of degree n and d the absolute value of its
discriminant. In this article, he extends previous work [194] by giving eﬀective lower bounds for
the function W ψK (X) which counts the sign changes of ∑
Npr ≤x log Np − x. Assume GRH(H, 0) for
the Dedekind zeta function ζK. When H and X are suﬃciently large (in a precise way given with
eﬀective constants), the author shows that W ψK (X) ≥ (1 − 10
H ) γK
π log X, where γK is the positive
imaginary part of the nontrivial zero of ζK closest to the real axis.

This article cites [170, 180, 183, 188, 194, 198, 199].

[201] Kaczorowski, J., The k-functions in multiplicative number theory. I. On complex explicit formulae,
Acta Arith. 56 (1990), no. 3, 195–211, MR1083000.

This is the ﬁrst in a series of articles on the “k-functions” k(z, χ) and K(z, χ) and certain limiting
values F (x, χ) of the latter (see Section 3.5 of this annotated bibliography for deﬁnitions). In Sec-
tion 3, the author proves that k(z, χ) can be analytically continued to a meromorphic function on
the Riemann surface M for log z, and indeed that

k(z, χ) − 1
2πi ez

ez − 1 log z

is meromorphic and single-valued on C. Indeed, the author ﬁnds all of the singularities of k(z, χ)
on M (all simple poles) and their residues. He also establishes the functional equations

k(z, χ) + ezk(z∗, χ) = D(z, χ), k(z, χ) + k(zc, χ) = ezD(−z, χ).

In Section 4, the author establishes explicit formulas for ψ0(x, χ) and ψ0r(x, χ), stated in the forms

F (x, χ) + ∑

β>0
L(β,χ)=0
 eβx

β = −ψ0(ex, χ) − Rχ(−1)(x) + B(χ) +
 



ex, if χ = χ0,
−x, if χ ̸= χ0 and χ(−1) = 1,
0, if χ(−1) = −1

for x > 0, and

F (x, χ) + ∑

β>0
L(β,χ)=0
 eβx

β = ψ0r(e|x|, χ) + R−χ(−1)(|x|) + C(χ) +
 



ex, if χ = χ0,
x, if χ ̸= χ0 and χ(−1) = 1,
0, if χ(−1) = −1

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 57

for x < 0. The author then shows that the left-hand side is equal to the series ∑ρ eρx/ρ as in the
classical explicit formulas for the right-hand sides.

This article cites [26].

[202] Kaczorowski, J., The k-functions in multiplicative number theory. II. Uniform distribution of zeta
zeros, Acta Arith. 56 (1990), no. 3, 213–224, MR1083001.

Let 0 < γ1 ≤ γ2 ≤ · · · denote the imaginary parts of nontrivial zeros of L(s, χ) in the upper
half plane. In this article Kaczorowski deﬁnes a positive Toeplitz matrix A = (ank) by ank =
e−γk γn
k (∑∞
h=1 e−γhγn
h )
−1 (for n, k ≥ 1), and proves that for any nonzero real x, the sequence
(xγn)
∞
n=1 is A-uniformly distributed (mod 1); the known result that the xγn are uniformly distributed
(mod 1) (in the sense of Weyl) follows as a corollary.

This article cites [201].

[203] Bartz, K. M., On some complex explicit formulae connected with the M¨obius function. I, II, Acta
Arith. 57 (1991), no. 4, 283–293, 295–305, MR1109990.

Assuming RH and the simplicity of the zeros of ζ(s), Titchmarsh showed that

M0(x) = ∑

ρ
 x
ρ

ρζ′(ρ) − 2 −
 ∞∑

n=1
 (−1)
n(2π/x)
2n

(2n)!nζ(2n + 1) .

In Part I, the author investigates the function m(z) = ∑
ℑρ>0 eρz/ζ′(ρ) (still assuming the simplicity
of the zeros). He shows that m(z) is a holomorphic function for ℑz > 0 that has an analytic
continuation to a meromorphic function on C satisfying the functional equation

m(z) + m(z) = −2
 ∞∑

n=1
 µ(n)
n cos ( 2π
n e−z)
.

Using analytic properties of m(z), he establishes Titchmarsh’s formula for M0(x) without assuming
RH.

This article cites [26, 42, 181, 201].

[204] Fujii, A., An additive problem of prime numbers. III, Proc. Japan Acad. Ser. A Math. Sci. 67 (1991),
no. 8, 278–283, MR1137928.

Motivated by Goldbach’s conjecture, the author proves that under RH,
∑

a,b≥1
a+b≤x
 Λ(a)Λ(b) = x
2

2 − 4x
3/2G(x) + O((x log x)
4/3) with G(x) = ℜ ∑

γ>0
 x
iγ

( 1
2 + iγ)( 3
2 + iγ) ,

where γ runs over the ordinates of the nontrivial zeros of ζ(s) in the upper half-plane. Follow-
ing the approach of Odlyzko and te Riele [181], the author shows that lim sup G(x) > 0.012 and
lim inf G(x) < −0.012 based on the ﬁrst 70 zeros.

This article cites [22, 42, 49, 81, 158, 181].

[205] Kaczorowski, J., The k-functions in multiplicative number theory. III. Uniform distribution of zeta
zeros; discrepancy, Acta Arith. 57 (1991), no. 3, 199–210, MR1105605.

Continuing the previous article in this series, the author deﬁnes an “A-discrepancy”

D∗
n(x) = sup
0≤t≤1
 ∣
∣
∣
∣

( ∑

k≥1
{xγk}<t
 e−γk γn
k
 )∕( ∞∑

k=1 e−γk γn
k
 ) − t∣
∣
∣
∣.

He shows that D∗
n(x) ≪ (log log n/ log n)
2/3 for every real number x ̸= 0. Under a certain A-variant
of zero-density theorems for Dirichlet L-functions, he proves that D∗
n(x) ≪ 1/ log n and conjectures
that D∗
n(x) ∼ α(x)/ log n for some constant α(x).

This article cites [202].

[206] Kaczorowski, J., The k-functions in multiplicative number theory. IV. On a method of A. E. Ingham,
Acta Arith. 57 (1991), no. 3, 231–244, MR1105608.

58 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

Using k-functions, the author proves an oscillation theorem for a speciﬁc class of almost periodic
functions, generalizing results of Ingham. He then applies the theorem to prime counting functions:
for instance, he shows that for every positive constant A > 0, there exists a number c > 1 such
that for all x > 1, we have sup Eψ(x) ≥ A and inf Eψ(x) ≤ −A on the interval (x, cx). The author
observes that Ingham’s refutation of the weak Mertens conjecture under RH and LI can be adapted
to give the analogous results for Eπ(x; q, a) and Eπ(x; q, a, b); he reproves these results, assuming
GRH but replacing LI by a condition on the intersection of the appropriate inﬁnite subtorus and
the diagonal subtorus. Finally, the author establishes an interesting connection between the range
of Eψ(x; q, a) and the range of x
1/2∆
ψ
r (x; q, a−1).

This article cites [30, 35, 51, 112, 114, 116, 121, 158, 181, 201].

[207] Kaczorowski, J., The k-functions in multiplicative number theory. V. Changes of sign of some arith-
metical error terms, Acta Arith. 59 (1991), no. 1, 37–58, MR1133236.

Assuming GRH and HC, the author shows that

lim inf
T →∞ W ψ
q,a(T )
log T ≥ γ0
π + κ,

where γ0 is the lowest “uncancelled” zero of Dirichlet L-functions modulo q—more precisely, the
minimal γ > 0 such that 1
2 + iγ is a pole of ∑χ (mod q) χ(a) L′
L (s, χ)—and where κ = κ(q, a) is a
nonnegative number, deﬁned as the density of zeros of a certain linear combination of K-functions.
When q = a = 1, this result implies that

lim inf
T →∞ W ψ(T )
log T ≥ γ1
π + 10−250,

where γ1 = 14.1347 . . . is the smallest ordinate of a nontrivial zero of ζ(s); this result breaks the
barrier γ1
π that had been achieved in prior results.

This article cites [170, 180, 183, 187, 188, 201, 206].

[208] Pintz, J., On an assertion of Riemann concerning the distribution of prime numbers, Acta Math.
Hungar. 58 (1991), no. 3-4, 383–387, MR1153492.

The author shows that a weighted version of ∆
Π(x) is negative on the average. More precisely, it is
shown that there are explicitly calculable positive absolute constants c1 and c2 such that if y > c1,
then ∫ ∞

1 ∆
Π(x) exp(
− log2 x
y
 ) dx < − c2
y exp ( 9y
16
 )
.

This article cites [8, 14, 26, 49, 65, 126, 140].

[209] Heath-Brown, D. R., The distribution and moments of the error term in the Dirichlet divisor prob-
lem, Acta Arith. 60 (1992), no. 4, 389–415, MR1159354.

Let a1(x), a2(x), . . . be continuous real-valued functions of period 1, and let η1, η2, . . . be nonzero
constants such that limN →∞ lim supT →∞ 1
T ∫ T
0 min{1, |F (x) − ∑n≤N an(ηnx)|} dx = 0; the author

shows that the mean value 1
T ∫ T
0 p(F (t)) dt converges to a limit as T → ∞ for every continuous,
integrable, piecewise diﬀerentiable function p for which ˆp is also integrable. Under further hypotheses,
including the linear independence of the ηj over Q, the author shows that F (x) has a limiting
distribution function. When such a limiting distribution function exists, the author establishes a
necessary condition for certain normalized moments of F (x) to converge in the limit. The author
applies these theorems when F (x) is the error term in: the classical divisor problem, the circle
problem, the Piltz divisor problem for τ3, or the second moment for ζ(s) on the critical line. An
important lemma is the evaluation, for continuous functions b1(t), . . . , bk(t) of period 1 from R to
C, of limT →∞ 1
T ∫ T
0 b1(η1t) . . . bk(ηkt) dt.

This article cites [21, 186].

[210] Kaczorowski, J., A contribution to the Shanks-R´enyi race problem, Quart. J. Math. Oxford Ser. (2)
44 (1993), no. 176, 451–458, MR1251926.

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 59

The author shows, assuming GRH, that there are inﬁnitely many integers m such that π(m; q, 1)
is larger than any other π(m; q, a), as well as inﬁnitely many integers such that π(m; q, 1) is the
smallest. Indeed, the sets of such integers have positive lower density, even if a stronger inequality
is demanded: the author proves that for any positive real number u, there exist constants c > 1 and
b > 0 such that for every T ≥ 1,

#
{T ≤ m ≤ cT : Eπ(m; q, 1) − max
a̸≡1 (mod q) Eπ(m; q, a) ≥ u} ≥ bT,

and similarly for Eψ; and the same result holds with ≥ u replaced by ≤ −u. The author uses
his k-functions that appeared in prior work, as well as an examination of the boundary values of
Dirichlet series.

The author formulates the following “Strong Race Hypothesis”: for every permutation of the set
{a1, a2, . . . , aφ(q)} of reduced residue classes modulo q, the set of integers m such that

π(m; q, a1) < π(m; q, a2) < · · · < π(m; q, aφ(q))

has positive lower density.

This article cites [56, 71, 201, 206].

[211] Sankaranarayanan, A., On the sign changes in the remainder term of an asymptotic formula for the
number of squarefree numbers, Arch. Math. (Basel) 60 (1993), no. 1, 51–57, MR1193094.

Using a method of Kaczorowski [170], the author shows that the number of sign changes of ∆
Q2 (x)
for 2 ≤ x ≤ T is ≫ log T with an eﬀective constant. The author claims the analogous result for
∆
Qk (with the implicit constant depending on k) for all 2 ≤ k ≤ 108.

This article cites [170, 188, 193, 198–200].

[212] Kaczorowski, J., Results on the distribution of primes, J. Reine Angew. Math. 446 (1994), 89–113,
MR1256149.

The author uses k-functions to prove several results. Assuming RH, he shows that the set {m ∈
N : Eπ(x) > u} has positive lower density for any u ∈ R, and similarly with Eπ(x) replaced by
−Eπ(x), Eψ(x), −Eψ(x); assuming GRH, Eπ(x) may be further replaced by Eπ(x; q, 1, max) and
−Eπ(x; q, 1, min) and their counterparts with ψ. Unconditionally he gives analogous weaker density
statements such as #{m ≤ M : Eπ(x) > u} = Ω(M 1−ε). All these results are ineﬀective, but the
author provides eﬀective counterparts such as lim inf N →∞ ∑N
k=1 2−k#{2k ≤ m < 2k+1 : Eπ(x) >
u} > 0.

This article cites [10, 14, 30, 49, 56, 71, 137, 138, 201, 206, 210, 212, 218].

[213] Montgomery, H. L., Ten lectures on the interface between analytic number theory and harmonic
analysis, vol. 84, CBMS Regional Conference Series in Mathematics, Published for the Conference
Board of the Mathematical Sciences, Washington, DC; by the American Mathematical Society,
Providence, RI, 1994, pp. xiv+220, MR1297543.

In Chapter 5 the author gives proofs of the ﬁrst and second main theorems of the power-sum method
using duality, and improves the ﬁrst main theorem for longer ranges of v to max1≤v≤N 2 |sv| ≫
|s0|/N . The author also deduces Fabry’s gap theorem from the ﬁrst main theorem, and gives im-
proved lower bounds for the speciﬁc cases where all the coeﬃcients bj are all nonnegative or all
equal to 1.

This chapter cites [31, 65, 66, 166, 177].

[214] Motohashi, Y., The binary additive divisor problem, Ann. Sci. ´Ecole Norm. Sup. (4) 27 (1994), no. 5,
529–572, MR1296556.

Given a positive integer k, the additive divisor problem concerns the asymptotic behavior of Sk(x) =∑n≤x τ (n)τ (n + k). It is known that there is a quadratic polynomial Pk(t) such that Sk(x) ∼
xPk(log x). The author shows that Sk(x)−xPk(log x) = Ω(
√
x) via Kloosterman sums and Kuznetsov’s
trace formulas.

[215] Rubinstein, M. and Sarnak, P., Chebyshev’s bias, Experiment. Math. 3 (1994), no. 3, 173–197,
MR1329368.

60 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

This is the article that really placed in central roles the logarithmic limiting distributions and
logarithmic densities of prime number races.

Assuming GRH: the authors show that

Eq;a1,...,ar (x) = log x
√x
 (
φ(q)π(x; q, a1) − π(x), . . . , φ(q)π(x; q, ar) − π(x)
)

has a limiting logarithmic distribution µq;a1,...,ar on Rr. They give an exponential upper bound for
the “tail” of µq;a1,...,ar (that is, the mass assigned to the exterior of a large ball), as well as a doubly
exponential lower bound for the portion of that tail lying in certain speciﬁc orthants. They note the
analogous results for the race between π(x) and Li(x), as well as for the race between π(x; q, N ) and
π(x; q, R); in these two-way races, it follows that δ(π, Li), δ(Li, π), δq;R,N , and δq;N,R are strictly
positive.

Assuming GRH and LI: they give the formula for the Fourier transform of µq;a1,...,ar . From it they
deduce that the densities δq;a1,...,ar exist and are strictly positive. They characterize the races (all
with r ≤ 3) for which µq;a1,...,ar is symmetric under all permutations of the coordinates. They
show that δq;a1,...,ar tends to 1/r! as q tends to inﬁnity, and establish a central limit theorem
for Eq;N,R(x)/√log q. They also compute δ(Li, π), and δq;N,R for q ∈ {3, 4, 5, 7, 11, 13}, to several
decimal places.

This article cites [14, 26, 27, 32, 34, 48, 56, 71, 132, 137, 190, 209].

[216] Szyd lo, B., On oscillations in the additive divisor problem. I, Acta Arith. 66 (1994), no. 1, 63–69,
MR1262653.

For a positive integer k, let Ek(x) be the error term for the asymptotic formula of ∑
n≤x τ (n)τ (n+k)
related to the additive divisor problem. Using Landau’s theorem, the author shows that Ek(x) =
Ω±(
√
x), improving a result of Motohashi [214].

This article cites [158, 186, 214].

[217] Kaczorowski, J., On the distribution of primes (mod 4), Analysis 15 (1995), no. 2, 159–171, MR1344249.

The author examines upper and lower natural densities in the prime number race modulo 4. As-
suming GRH for L(s, χ−4), he proves that d
∗(4; 1, 3) ≥ 0.04054045 and d
∗(4; 3, 1) ≥ 0.99998936,
and that d∗(4; 1, 3) < 0.0000106 and d∗(4; 3, 1) < 0.9594595.

This article cites [10, 14, 30, 49, 56, 71, 138, 201, 206, 210, 212, 218].

[218] Kaczorowski, J., On the Shanks-R´enyi race problem mod 5, J. Number Theory 50 (1995), no. 1,
106–118, MR1310738.

Assuming GRH, the author shows that for any permutation (a1, a2, a3, a4) of (1, 2, 3, 4), there exist
constants b > 0 and c0 > 1 such that

#
{T ≤ x ≤ c0T : ψ(x; 5, a1) > ψ(x; 5, a2) >ψ(x; 5, a3) > ψ(x; 5, a4),

min
1≤j≤3 (
ψ(x; 5, aj, aj+1)
) ≥ b√
x} ≫ T.

The proof is another application of the author’s theory of k-functions and involves explicit calcula-
tions using the Dirichlet L-functions (mod 5) and exponential sums corresponding to each permu-
tation.

This article cites [71, 201, 210].

[219] Kaczorowski, J., On the Shanks-R´enyi race problem, Acta Arith. 74 (1996), no. 1, 31–46, MR1367576.

The author’s earlier result [210] implies that there exists a permutation {σj} of the reduced residue
classes (mod q) that begins with 1 such that the set of x for which the π(x; q, σj ) are in the given order
has positive lower density. In this article, he provides a method for computing explicit permutations
with this property. As an application, he gives permutations for each prime modulus ≤ 29 that satisfy
these conditions and therefore provably occur with positive lower density; for example, modulo 13
he provides the permutation (1, 7, 8, 9, 2, 6, 12, 10, 11, 5, 3, 4) with this property. Similar results apply
to permutations with 1 in last place, and to the functions ψ(x; q, σj ).

This article cites [71, 201, 206, 210, 212, 218].

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 61

[220] Stechkin, S. B. and Popov, A. Y., Asymptotic distribution of prime numbers in the mean, Uspekhi
Mat. Nauk 51 (1996), no. 6(312), 21–88, MR1440155.

The authors prove that when x suﬃciently large,
∫ 2x

x |∆
ψ(u)| du ≥ x
3/2

200 and ∫ 2x

x |∆
π(u)| du ≥ x
3/2

log x ,

and also that there exists a constant A > 1 such that
∫ Ax

x max{0, ∆
ψ(u)} du ≥ x
3/2 and ∫ Ax

x min{0, ∆
ψ(u)} du ≤ −x
3/2.

Assuming RH, these latter inequalities hold with A = 212. If RH is false, however, then the con-
stant A (as well as the constant implied by “suﬃciently large”) is ineﬀective.

This article cites [8, 21].

[221] Kaczorowski, J., Boundary values of Dirichlet series and the distribution of primes, in: European
Congress of Mathematics, Vol. I (Budapest, 1996), vol. 168, Progr. Math. Birkh¨auser, Basel, 1998,
237–254, MR1645811.

From the Math Review by M. Jutila: “Various aspects and problems as well as the history of
comparative prime number theory are surveyed, including recent important work by the author
[using K-functions]. The central topic is the comparative study of the frequency of primes in diﬀerent
arithmetic progressions. The article ends with a list of open problems and an extensive bibliography
with 30 references.”

This article cites [18, 19, 34, 71, 74, 84, 132, 138, 150, 170, 180, 181, 183, 187, 188, 193, 201, 206,
207, 209, 210, 212, 215, 217, 218].

[222] Gonek, S., The second moment of the reciprocal of the Riemann zeta function and its derivative,
1999, url: https://www.slmath.org/workshops/101/schedules/25626.

This web page contains a recording and notes from the talk where the author announced the

conjecture that ∑

0<γ≤T
 1
|ζ′(ρ)|2 ∼ 3
π3 T .

[223] Bays, C. and Hudson, R. H., Zeroes of Dirichlet L-functions and irregularities in the distribution of
primes, Math. Comp. 69 (2000), no. 230, 861–866, MR1651741.

The authors describe computations of both π(x; 4, 3, 1) for values of x past 1012, as well as its
estimate using a truncated explicit formula with 12,000 zeros of L(s, χ−4) for values of x up to
101,000. The estimate duplicates the true distribution with satisfying accuracy, rediscovers all known
axis-crossing regions, and ﬁnds probable new axis-crossing regions. The method extends to other
diﬀerences such as ∆
π(x) and π(x; q, N , R).

This article cites [48, 56, 131, 137, 141, 215, 218, 223].

[224] Bays, C. and Hudson, R. H., A new bound for the smallest x with π(x) > li(x), Math. Comp. 69
(2000), no. 231, 1285–1296, MR1752093.

Using Lehman’s theorem [97] together with the ﬁrst 106 zeros of ζ(s) (supplied by Odlyzko), the
authors show that there exist many integers x in the range [exp(727.95209 − .002), exp(727.95209 +
.002)] for which π(x) > li(x). (This corresponds to the interval [1.3954272×10316, 1.4010201×10316),
although the authors claim that the interval is [1.398201×10316, 1.398244×10316].) They also report
on computations approximating π(x) − li(x) for x up to about 4 × 1012370 (the signiﬁcance being
that the 20th region with many solutions to π(x) > li(x) is probably around this number) that
support the conditional result of Rubinstein and Sarnak that δ(li, π) ≈ 0.99999974.

This article cites [14, 26, 27, 46, 97, 190, 215, 223, 229].

[225] Feuerverger, A. and Martin, G., Biases in the Shanks-R´enyi prime number race, Experiment. Math.
9 (2000), no. 4, 535–570, MR1806291.

62 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

Assuming GRH and LI, the authors establish a general formula for δq;a1,...,ar as a linear combination
of principal values of integrals of dimensions up to r − 1. As an example, they numerically compute
all possible race densities when q ∈ {5, 8, 12} (including the full four-way races), all densities for
two- and three-way races when q ∈ {7, 9}, and all two-way race densities when q = 11. They
also list some families of symmetries among these densities, as well as some families of provable
inequalities for three-way race densities. The authors conjecture that “two-ties” conﬁgurations are
possible in the following sense: for any 1 ≤ i, j, k, ℓ ≤ r, there exist arbitrarily large x such that
π(x; q, ai) = π(x; q, aj ) and π(x; q, ak) = π(x; q, aℓ) (even if the relative sizes of all r contestants are
prescribed); they further conjecture that analogous “three-ties” conﬁgurations occur only ﬁnitely
often. They also make some speculative conjectures about “bias factors” and “order equivalences”
to introduce the idea of comparing densities to one another; they also describe the question of
the possible asymptotic sizes of δq;a1,...,ar if r is a function of q. Finally, they remark that their
techniques also resolve a question of Knapowski and Tur´an [71] about simultaneous solutions to
∆
π(x; q, aj ) > 0.

This article cites [14, 56, 71, 165, 215, 219].

[226] Narkiewicz, W., The development of prime number theory, Springer Monographs in Mathematics,
Springer-Verlag, Berlin, 2000, pp. xii+448, MR1756780.

Section 6.6 is devoted to the sign of the diﬀerence π(x) − li(x). The author sketches the proof of
Littlewood’s theorem and gives a detailed survey of results about W (T ) and W ψ(T ).

This article cites [8, 14, 23, 27, 30, 46, 65, 66, 97, 106, 126–128, 135, 136, 190].

[227] Ng, N., Limiting Distributions and Zeros of Artin L-Functions, Thesis (Ph.D.)–University of British
Columbia, 2000, url: http://www.cs.uleth.ca/~nathanng/RESEARCH/phd.thesis.pdf.

In Section 2 of this thesis, the author gives examples of Artin L-functions for which LI is false. In
Section 5.1, the author derives (under GRH) an explicit formula for log x√
x ( |G|
|C| πC (x) − πK (x)
) as
x → ∞, where L/K is a normal extension of number ﬁelds, G = Gal(L/K) and C is a conjugacy
class of G, and πK(x) = #{p ⊂ OK : Np ≤ x} and πC (x) = #{p ⊂ OK : Np ≤ x, σp = C} where σp
is the Frobenius. Using the explicit formula, the author obtains analogues of Chebyshev’s bias in
Galois groups. In Section 6.1, an explicit formula is given for log x√
x π(x, a1, a2), where a1 and a2 are
ideal classes of a number ﬁeld K. This formula is used to prove analogues of Chebyshev’s bias for
primes in ideal classes. In Chapter 7, the author conditionally establishes the existence of a limiting
distribution for EM (x) and conjectures that its maximal order is (log log log x)
5/4.

This article cites [21, 35, 51, 112, 147, 150, 181, 186, 209, 215, 225, 229].

[228] Puchta, J.-C., On large oscillations of the remainder of the prime number theorems, Acta Math.
Hungar. 87 (2000), no. 3, 213–227, MR1761276.

Assuming GRH, the author shows that Eψ(x; q, 1, min) = Ω+(log log log x) and Eψ(x; q, 1, max) =
Ω−(log log log x) where all constants are eﬀective. In particular, the q = 1 case gives an eﬀective
version of the classical result of Littlewood [14]. One tool is an evaluation of the moments of Eψχ(u)
for Dirichlet characters χ: the author shows that 1
y ∫ y
0 Eψχ(u)
k du
u → (−1)
k ∑γ1+···+γk=0 1/ρ1 · · · ρk,
where the sum runs over k-tuples of nontrivial zeros of L(s, χ).

This article cites [14, 34, 201, 202, 205, 206, 210, 218].

[229] Bays, C., Ford, K., Hudson, R. H., and Rubinstein, M., Zeros of Dirichlet L-functions near the real
axis and Chebyshev’s bias, J. Number Theory 87 (2001), no. 1, 54–76, MR1816036.

This article is concerned with estimating the densities δq,N ,R, in particular by using the fact that the
truncated explicit formula is an almost-periodic function whose largest “quasi-period” is dictated by
its lowest zero. The authors present data supporting the fact that these densities depends strongly
on the location of the ﬁrst few zeros of L(s, χ±q) and the size of the ﬁrst zero. Plots of E(x; q, N , R)
for all primes q with h(−q) = 1 are provided, and the diﬃculty of accurately estimating the densities
from such data is pointed out. The authors note that the Chowla–Selberg formula implies that if
Q(
√
−q) is an imaginary quadratic ﬁeld with class number 1 then L(s, χ−q) has a relatively low-lying
zero; they also analyze the connection between low-lying zeros and class numbers 3 and 5.

This article cites [1, 14, 48, 56, 71, 137, 141, 148, 210, 215, 218, 223].

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 63

[230] Ford, K. and Hudson, R. H., Sign changes in πq,a(x) − πq,b(x), Acta Arith. 100 (2001), no. 4, 297–
314, MR1862054.

The authors generalize Lehman’s method [97] to arithmetic progressions, enabling them to give new
results on the location of negative values of π(x; q, b, 1) for moduli q | 24. They show that each
π(x; 8, b, 1) is negative for some x < 5 · 1019, each π(x; 12, b, 1) is negative for some x < 1084, and
each π(x; 24, b, 1) is negative for some x < 10253. Further, if GRH(630,000) holds for L(s, χ−4), then
π(x; 4, 1, 3) > √
x/ log x for some x ≈ 8 · 1034,171.

This article cites [27, 44, 46, 48, 56, 74, 75, 97, 131, 137, 139, 210, 212, 215, 219, 224, 229].

[231] Ruzsa, I. Z., Consecutive primes modulo 4, Indag. Math. (N.S.) 12 (2001), no. 4, 489–503, MR1908877.

The author proves that the number of pairs of consecutive primes up to x that are both congruent
to 1 (mod 4) is ≫ x log log x/ log2 x, improving a result of Shiu. A generalization holds where the
single residue class 1 (mod 4) is replaced by an arbitrary set of reduced residue classes modulo q of
size φ(q)/2. The proof uses Maier’s method.

This article cites [134, 213].

[232] Ford, K. and Konyagin, S., Chebyshev’s conjecture and the prime number race, in: IV International
Conference “Modern Problems of Number Theory and its Applications”: Current Problems, Part
II (Russian) (Tula, 2001), Mosk. Gos. Univ. im. Lomonosova, Mekh.-Mat. Fak., Moscow, 2002,
pp. 67–91, MR1985941.

This article describes nine families of problems that are central to the study of comparative prime
number theory. The ﬁrst eight are taken from or inspired by the problems listed by Knapowski
and Tur´an in [71]; the ninth problem, entitled “Union-problems”, examines the distribution of
1
#A π(x; q, A) − 1
#B π(x; q, B). Throughout the rest of the article, the authors provide an overview of
what is already known about the ﬁrst seven problems.

This article cites [1, 10, 14, 17–19, 27, 32, 34, 35, 46, 48, 56, 71–73, 75–79, 82, 84, 85, 91–93, 96, 97,
99, 112, 114, 116–118, 131, 132, 138, 139, 141, 148, 150, 190, 201, 206, 210, 215, 218, 219, 223, 225,
229, 230, 233, 235, 238].

[233] Ford, K. and Konyagin, S., The prime number race and zeros of L-functions oﬀ the critical line,
Duke Math. J. 113 (2002), no. 2, 313–330, MR1909220.

This article introduces the term “barrier” for a hypothetical conﬁguration of zeros of Dirichlet
L-functions that causes some ordering of a set of π(x; q, aj ) not to occur for x suﬃciently large.
The authors show (through several complementary constructions) that for every three-way prime
number races, there is a ﬁnite barrier that prevents at least one of the six possible orderings from
occurring for large x; moreover, the zeros in these barriers can be arbitrarily close to the critical
line and arbitrarily far from the real axis. While most of their constructions of barriers involve zeros
with linearly dependent ordinates, the authors construct in the ﬁnal section a barrier with linearly
independent ordinates.

This article cites [1, 14, 56, 71–73, 75–79, 84, 85, 91–93, 96, 137, 210, 215, 218, 219].

[234] Lau, Y.-K., On the existence of limiting distributions of some number-theoretic error terms, J.
Number Theory 94 (2002), no. 2, 359–374, MR1916279.

This article investigates the limiting distribution of almost periodic functions. The author proves
the existence of the limiting distribution of a class of functions which are bounded and can be
approximated by periodic functions in L1-norm. By using the quantitative version of the continuity
theorem, the author is able to investigate the rate of convergence of some cases. Compared to Heath-
Brown’s work [209] on distribution of the error term in the Dirichlet divisor problem, the result here
is more general and requires weaker hypotheses.

This article cites [209, 215].

[235] Martin, G., Asymmetries in the Shanks-R´enyi prime number race, in: Number theory for the mil-
lennium, II (Urbana, IL, 2000), A K Peters, Natick, MA, 2002, pp. 403–415, MR1956261.

The author begins with the known values (assuming GRH and LI), for q = 8 and q = 12, of δq;a,1
where a ̸≡ 1 (mod q) and of δq;a,b,c where {a, b, c} is a permutation of the three nonidentity elements

64 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

of (Z/qZ)
×. He investigates how one could have predicted the relative sizes of these densities using
the values and conductors of the nonprincipal Dirichlet characters (mod q), by arguing by analogy
with independent random variables with variances of diﬀerent sizes.

The author also comments on the equality of a family of variant deﬁnitions of the logarithmic density
of a set of positive real numbers, as well as some conjectures on the rarity of ties π(x; q, a) = π(x; q, b).

This article cites [48, 137, 141, 148, 215, 225].

[236] Balanzario, E. P. and Hern´andez, S., On the number of large oscillations of some arithmetical power
series, Arch. Math. (Basel) 81 (2003), no. 3, 285–290, MR2013259.

Fix distinct integers a ≥ 0 and b ≥ 1 and a real number 0 < θ < 1
2b , and deﬁne

h(x) =
 ∞∑

n=1 ℓ(n)e−n/x − Γ(1/a)
aζ(b/a) x
1/a, where ζ(as)
ζ(bs) =
 ∞∑

n=1
 ℓ(n)
ns .

(When a = 0, the second term in the deﬁnition of h is omitted.) Special cases include ℓ(n) = ζ(0)µ(n)
when (a, b) = (0, 1) and ℓ(n) = (−1)
Ω(n) when (a, b) = (2, 1). Assuming that the zeros of ζ(s), up
to a height depending on θ and b, are simple and lie on the critical line, the authors show that
W (h; T ; tθ) ≫ log T . For example, in the special cases mentioned above, the authors verify the
assumption up to height 105 to deduce oscillations of size t0.278.

This article cites [170, 211].

[237] Ford, K. and Konyagin, S., The prime number race and zeros of L-functions oﬀ the critical line. II,
Bonner Math. Schriften 360 (2003), 40, MR2075622.

The authors continue to explore “barriers” for various statements in comparative prime number
theory. In this article they make the distinction between the barrier itself, which is a multiset
of complex numbers, and the consequences to orderings of prime-counting functions (or functions
that are suﬃciently close to such) that would follow from the L(s, χ) having their rightmost zeros
precisely at the elements of the barrier. After establishing some lemmas on values of trigonometric
polynomials, the authors prove several results concerning whether or not bounded (or ﬁnite) barriers
exist for various races of the form π(x; q, 1) against many other π(x; q, a). They show that if every
two-way race from a set of r functions π(x; q, aj ) changes leaders inﬁnitely often, then the total
number of r-way orderings is at least r(r − 1)/2 + 1; they investigate whether barriers can exist that
limit the number of orderings to this minimal value (“extremal barriers”), and construct barriers
that do force at most r(r − 1) orderings.

This article cites [14, 71–73, 75–79, 84, 85, 91–93, 96, 201, 210, 232, 233].

[238] Kaczorowski, J. and Ramar´e, O., Almost periodicity of some error terms in prime number theory,
Acta Arith. 106 (2003), no. 3, 277–297, MR1957110.

This article investigates, assuming GRH, the distribution of values of a large class of functions of
arithmetic signiﬁcance (related to the Selberg class) using boundary values of k-functions. They
establish an explicit formula for the appropriate functions as well as almost periodicity in the L2

sense of Stepanov and the existence of a limiting logarithmic density.

This article cites [201, 206, 215, 217, 221].

[239] Leboeuf, P., Prime correlations and ﬂuctuations, Ann. Henri Poincar´e 4 (2003), no. suppl. 2, S727–
S752, MR2037293.

In Section 4, the author heuristically computes higher moments of Eπ(x) from the explicit formula,
determining that the third moment should be asymptotic to − 3√x ∑γ>0( 1
4 + γ2)
−2; while this
vanishes in the limit as x → ∞, it demonstrates an asymmetry for ﬁnite x. The author also calculates
the limiting fourth moment and notes that it diﬀers from that of the Gaussian approximation.
In addition, the author shows that there are persistent correlations between values of Eπ(x) at
arguments separated by up to x
γ1 , where γ1 ≈ 14.1347 is the smallest ordinate of a nontrivial zero
of ζ(s). These observations are supported by numerical calculations.

This article cites [97, 215, 223].

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 65

[240] Del´eglise, M., Dusart, P., and Roblot, X.-F., Counting primes in residue classes, Math. Comp. 73
(2004), no. 247, 1565–1575, MR2047102.

Extending a well-known method of Meissel for computing π(x), the authors give an algorithm for
computing π(x; q, a) in time O(x
2/3/ log
2 x). They use this algorithm to compute π(x; 4, 1) and
π(x; 4, 3) for x = 10j, 2 · 10j, . . . , 9 · 10j for each 10 ≤ j ≤ 19. In particular, a new region where
π(x; 4, 3) < π(x; 4, 1) is discovered near x = 1018.

This article cites [14, 48, 81, 138, 215, 225, 229].

[241] Kotnik, T. and Lune, J. van de, On the order of the Mertens function, Experiment. Math. 13 (2004),
no. 4, 473–481, MR2118272.

The authors use the ﬁrst million zeros of ζ(s) to approximate EM (x) for x ≤ 1010
10. Based on the
data, the authors conjecture that EM (x) = Ω±(
√
log log log x), with the data suggesting approxi-
mately the constant 1
2 for each sign. In particular, the authors propose that earlier conjectures [105,
111, 243] on the extreme values of EM (x) do not hold.

This article cites [4, 14, 105, 111, 181, 189, 243].

[242] Moree, P., Chebyshev’s bias for composite numbers with restricted prime divisors, Math. Comp. 73
(2004), no. 245, 425–449, MR2034131.

Deﬁne N (x; q, a) to be the number of integers up to x all of whose prime factors are congruent to
a (mod q). The author shows that min{N (x; 3, 2), N (x; 4, 3)} ≥ max{N (x; 3, 1), N (x; 4, 1)} for all
x ≥ 1, using the fact that N (x; q, a) is the summatory function of a multiplicative function whose
values on primes alone has summatory function π(x; q, a); consequently, biases in the distribution of
small primes in residue classes modulo q can be magniﬁed into complete biases among the N (x; q, a).
Indeed, Wirsing’s method is already enough to establish such inequalities for suﬃciently large x;
the author develops eﬀective versions of Wirsing’s method to conclude the same for all x ≥ 1.

This article cites [1, 14, 74, 84, 137, 215, 221, 226, 230].

[243] Ng, N., The distribution of the summatory function of the M¨obius function, Proc. London Math.
Soc. (3) 89 (2004), no. 2, 361–389, MR2078705.

This article contains several results on the Mertens sum M (x), all conditional on both RH and the
estimate ∑0<γ≤T 1/|ζ′(ρ)|2 ≪ T . The author shows that M (x) ≪ x
1/2(log x)
3/2, and furthermore
that M (x) ≪ x
1/2(log log x)
3/2 except on a set of ﬁnite logarithmic measure. He also proves that
∫ X

1
 ( M (x)
x
 )2 dx ∼ log X · ∑

γ>0
 2
|ρζ′(ρ)|2 ,

which in particular implies the “weak Mertens conjecture” ∫ Y
2 (M (x)/x)
2 dx ≪ log Y . Under the
additional assumption of LI, he shows that EM (x) has a limiting logarithmic distribution whose
Fourier transform can be written down explicitly. Partly building on unpublished work by Gonek,
the author conjectures that EM (x) = Ω±(
(log log log x)
5/4)
.

This article cites [21, 26, 35, 51, 112, 150, 181, 196, 197, 209, 215, 227].

[244] Schlage–Puchta, J.-C., Sign changes of π(x, q, 1) − π(x, q, a), Acta Math. Hungar. 102 (2004), no. 4,
305–320, MR2040112.

This article examines the race between π(x; q, 1) and π(x; q, max) = maxa̸≡1 (mod q) π(x; q, a). Set
C = exp
(
max{q, e1,260}170 + e18cq )
. Assuming GRH, the author proves that W (
π(x; q, 1, max); T ) >
(log T )/C −1, and in particular that there exists x < eC such that π(x; q, 1, max) > 0. The analogous
results are proved for the race between π(x) and li(x), with C = exp(e16.7).

This article cites [27, 30, 97, 135, 140, 190, 210, 218, 228].

[245] Karatsuba, A. A., Behavior of the function R1(x) and of its mean value, Russian, Dokl. Akad. Nauk
404 (2005), no. 4, 439–442, MR2256805.

Let R1(x) = π(x) − li(x) + 1
2 li(
√
x). The author follows Kaczorowski’s method in [170, 180] to show
that W (R1, T ) ≫ log T and W (
∫ x
0 R1(t) dt, T ) ≫ log T .

66 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

This article cites [170, 180, 246].

[246] Karatsuba, A. A., On the approximation of π(x), Russian, Chebyshevskii Sb. 5 (2005), no. 4(12),
5–20, MR2169423.

Let R1(x) = π(x) − li(x) + 1
2 li(
√x), and recursively deﬁne

Rj+1(x) = ∫ x

2 Rj(t) dt = − x
j+ 1
2
log x
 ∑

γ
 x 1
2 +iγ

( 1
2 + iγ) · · · (j + 1
2 + iγ) + O( x
j+ 1
2

log2 x
 )

for each j ≥ 1. Ingham [26] conjectured that π(x) is better approximated by li(x) − 1
2 li(
√
x) than by
li(x). Under RH, the author validates this conjecture by showing that each of the functions Rj(x)
changes signs inﬁnitely often, in contrast to Aπ
1 (x) < − 3
5 x
3/2/ log x + O(x
3/2/ log
2 x).

This article cites [26].

[247] Karatsuba, A. A., On the number of sign changes of the function R1(x) and its mean values, Russian,
Chebyshevskii Sb. 6 (2005), no. 2(14), 163–183, MR2262605.

Let R1(x) = π(x) − li(x) + 1
2 li(
√
x) and Rj+1(x) = ∫ x
2 Rj(t) dt for j ≥ 1. The author generalizes his
earlier article [245] to show that for W (Rj , T ) ≫ log T for all positive integers j.

This article cites [170, 180, 198, 199, 246].

[248] Radziejewski, M., On the distribution of algebraic numbers with prescribed factorization properties,
Acta Arith. 116 (2005), no. 2, 153–171, MR2110393.

Given any number ﬁeld K and any subgroup Γ of the narrow class group of K, there is a notion of
irreducibility of ideals in Γ; the corresponding factorization into irreducibles can be nonunique, and
indeed the lengths of such factorizations can also be nonunique. The author examines the counting
functions of ideals in Γ whose set of factorization lengths has cardinality lying in a prescribed
interval, or (alternatively) contains one of a prescribed set of positive integers. The author obtains
oscillation results for the corresponding error terms of the form Ω(x
1/2−ε), as well as lower bounds
of size log X for the number of sign changes up to X.

This article cites [188, 249].

[249] Radziejewski, M., Oscillations of error terms associated with certain arithmetical functions, Monatsh.
Math. 144 (2005), no. 2, 113–130, MR2123959.

Kaczorowski and Pintz [188] considered functions of a real variable whose Mellin transforms had
singularities of the form (s − ρ)
wP (log(s − ρ)) for some w ∈ C. The author extends this class of
functions to those with singularities that are linear combinations of this type, showing that such
functions (suitably normalized) have oscillations of the form Ω(x
1/2−ε), as well as lower bounds of
size log X for the number of sign changes up to X. The motivation was to address error terms of
counting functions corresponding to certain ideal factorization problems in number ﬁelds [248], and
the author provides an application to counting the number of ideals in a subgroup of the narrow
class group all of whose restricted factorizations have the same length.

This article cites [10, 17, 23, 30, 89, 102, 128, 183, 188, 212].

[250] Granville, A. and Martin, G., Prime number races, Amer. Math. Monthly 113 (2006), no. 1, 1–33,
MR2202918.

The authors present an accessible survey of prime number races, explicit formulas for π(x) and
π(x; q, a), the biases caused by squares of primes, and limiting distributions and densities. The ﬁnal
section describes unpublished research of G. Davidoﬀ (in connection with an REU group), including
the theorem that Wq;N ,R(T ) is unbounded for any prime modulus q, assuming only that L(s, χ±q)
has no real zero in the interval [Θ(χ±q), 1].

This article cites [14, 34, 56, 71–73, 75–79, 114, 137, 148, 186, 215, 217, 219, 224, 225, 227, 229, 233,
235, 237, 255].

[251] Kotnik, T. and Riele, H. te, The Mertens conjecture revisited, in: Algorithmic number theory,
vol. 4076, Lecture Notes in Comput. Sci. Springer, Berlin, 2006, pp. 156–167, MR2282922.

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 67

Based on the work of Odlyzko and te Riele [181], a reﬁned version of the LLL algorithm, and
improved precision for zeros of ζ function, the authors show that

lim inf
x→∞ EM (x) < −1.229 and lim sup
x→∞ EM (x) > 1.218.

Using a similar idea, the authors show that a counterexample to the Mertens conjecture occurs
before exp(1.59 × 1040), improving Pintz’s result [189]. The authors also provide new numerical
evidence to support the conjecture M (x) = Ω±(
√
x log log log x) made in [241].

This article cites [4, 35, 42, 105, 111, 112, 121, 125, 143, 181, 189, 241, 243].

[252] Montgomery, H. L. and Vorhauer, U. M. A., Changes of sign of the error term in the prime number
theorem, Funct. Approx. Comment. Math. 35 (2006), 235–247, MR2271616.

The authors show that ∆
ψ(x) takes values of both signs in every interval [x, 19x] for x ≥ 1 (where
the 19 is best possible), and takes values of both signs in every interval [x, 2.02x] when x is suﬃciently
large.

This article cites [14, 22, 23, 30, 170, 207].

[253] Kaczorowski, J., Results on the M¨obius function, J. Lond. Math. Soc. (2) 75 (2007), no. 2, 509–521,
MR2340242.

The author shows that
∞∑

n=1 µ(n) (cos ( x
n
 ) − 1) = Ω±(x
1/2 log log log x),

which comes tantalizingly close to the assertion that EM (x) = Ω±(log log log x). The proof uses an
explicit formula for a relative of k(z), namely

m(z) = 1
2πi
 ∫

C
 ezs

ζ(s) ds

where C is the boundary of a half strip enclosing the part of the critical strip lying in the upper half
plane.

This article cites [35, 181, 186, 189, 203, 206, 241, 243, 254].

[254] Kaczorowski, J. and Wiertelak, K., Ω-estimates for a class of arithmetic error terms, Math. Proc.
Cambridge Philos. Soc. 142 (2007), no. 3, 385–394, MR2329690.

The authors consider a general class of functions of the form F (z) = ∑∞
n=1 aneiωnz on the upper-half
plane, whose boundary values P (x) = limy→0+ ℜF (x + iy) exist for suﬃciently large x. If certain
growth conditions are satisﬁed, they establish oscillation results for P (x). Applying their result to
K(z)e−z/2 recovers Littlewood’s theorem ∆
ψ(x) = Ω±(x 1
2 log log log x), and similar consequences
hold for ∆
ψ(x; q, 1) and ψ(x; q, 1, a). As another application, the authors establish that the error
term in the asymptotic formula for ∑n≤x 2ω(n) is Ω±(
x
1/4(log log x)
1/2/(log log log x)
3/2)
. (As an
aside, in this variant of the divisor problem, obtaining even ≪ x
1/2−δ for the error term requires RH.)

This article cites [14, 201, 206, 221].

[255] Sarnak, P., Letter to Barry Mazur on ‘Chebyshev’s bias’ for τ (p), 2007, url: http://web.math.princeton.edu/sarna

Let λ(p) = τ (p)/p11/2 denote the normalized pth Fourier coeﬃcient of the Ramanujan function ∆(z),
a holomorphic cusp form of weight 12. Under various assumptions (functional equation, RH, LI) for
the symmetric power L-functions associated to ∆(z), the author proves the existence of a limiting
logarithmic distribution for the cumulative sum x
−1/2 log x·∑p≤x λ(p). This distribution has mean 1
but inﬁnite variance, so that even though there is a bias towards being positive, the set of such x
has logarithmic density 1
2 . The author provides a similar analysis for x
−1/2 log x · ∑
p≤x aE(p)/√
p,
where aE(p) are the coeﬃcients of the weight-2 cusp form attached to an elliptic curve E/Q; here
the mean is 1 − 2r(E) where r(E) is the rank of E. Here the variance is (conjecturally) ﬁnite, and
so the logarithmic density of the set of x for which ∑
p≤x aE(p)/√
p > 0 is strictly between 1
2 and 1
when r(E) = 0, but strictly between 0 and 1
2 when r(E) ≥ 1. The author makes analogous remarks
about the symmetric powers of these elliptic curve L-functions, where the ﬁniteness of the variance
corresponds to whether E has complex multiplication.

68 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

This letter cites [215].

[256] Borwein, P., Ferguson, R., and Mossinghoﬀ, M. J., Sign changes in sums of the Liouville function,
Math. Comp. 77 (2008), no. 263, 1681–1694, MR2398787.

The authors develop reﬁned algorithms for computing the sums L(x) and Lr(x). They show that the
smallest positive integer n for which Lr(n) < 0 (that is, the ﬁrst witness to the negative resolution
of Tur´an’s problem) is 72,185,376,951,205; they also describe the many sign changes of Lr(x) among
the subsequent integers, and suggest that its next sign change occurs near 1.16 · 1019. Similar results
are obtained for L(n), including a new region of sign changes starting at 351,100,332,278,253; their
calculation allows them to conclude that L(n) > 0.061867√
n inﬁnitely often.

This article [33, 35, 37, 51, 59, 156, 158].

[257] Cha, B., Chebyshev’s bias in function ﬁelds, Compos. Math. 144 (2008), no. 6, 1351–1374, MR2474313.

The author adapts the arguments of Rubinstein and Sarnak [215] to the function ﬁeld setting,
establishing (under the appropriate generalization of LI) the existence of limiting distributions and
their symmetries, a bias towards quadratic nonresidues in two-way races, and central limit theorems.
The author also provides some examples where LI is violated and the expected biases are overridden,
as well as an example where LI can actually be veriﬁed.

This article cites [1, 215, 250].

[258] Kotnik, T., The prime-counting function and its analytic approximations: π(x) and its approxima-
tions, Adv. Comput. Math. 29 (2008), no. 1, 55–70, MR2420864.

The author shows that π(x) < li(x) for 2 ≤ x ≤ 1014, improving unpublished work of Odlyzko
showing that π(x) < li(x) for x ≤ 1.59 × 1013. The rigorous computation used an Eratosthenes
sieve for π(x) and Ramanujan’s formula li(x) = √
x ∑∞
n=1 an logn x + log log x + C0, truncated at
n = 75 and linearly interpolated when x > 1010. Based on the data set, the author conjectures that
|∆
π(x)| < √
x and − 2
5 x
3/2 < Aπ
1 (x) < 0 for x > 2. The program for computation and storage of
the data was written in Delphi 6.0 and run on a PC with a 2.4 GHz Intel Pentium 4 processor and
512 MB of RAM.

This article cites [14, 26, 46, 74, 97, 122, 190, 224].

[259] Kowalski, E., The large sieve, monodromy, and zeta functions of algebraic curves. II. Independence
of the zeros, Int. Math. Res. Not. IMRN (2008), Art. ID rnn 091, 57, MR2439552.

The author initiates the study of analogues of LI over function ﬁelds. When C is a smooth genus-g
projective curve deﬁned over a ﬁnite ﬁeld Fq, its zeta function can be expressed as P (q−s)/(1 −
q−s)(1 − q1−s) where P (x) is a polynomial of degree 2g. RH over function ﬁelds (proved by Weil)
implies that the zeros of P (x) can be written as α1 = √
qeiθ1 , . . . , α2g = √qeiθ2g . The curve C is
said to satisfy LI if the set {θj : 0 ≤ θj ≤ π} ∪ {π} is linearly independent over Q.

The author focuses on a special family of hyperelliptic curves. Let f ∈ Z[x] be a squarefree monic
polynomial of degree 2g, and let p be an odd prime not dividing the discriminant of f . Consider
curves Ct : y2 = f (x)(x − t) parameterized by t ∈ Fq, where Fq is a ﬁnite extension of Fp. The
author shows that the number of t ∈ Fq with f (t) ̸= 0 in Fq such that LI fails for Ct is ≪
q1−1/(4g2+2g+4) log q, where the implicit constant depends only on g; in particular, most curves in
such a family satisfy LI. The author proves a similar result for the (multiset) union of the zeros of
the zeta functions associated to a k-tuple of curves in this family: the corresponding upper bound for
failures of LI among these k-tuples is shown to be ≪ ckqk−1/(29kg2 ) log q, where c > 1 is a constant
depending only on g and the implicit constant depends only on g. The author also indicates that the
connection between LI and Chebyshev’s bias in this function ﬁeld setting is parallel to the classical
prime number race setting. In particular, when C1, C2 are algebraic curves (smooth, projective,
geometrically connected) with common genus g ≥ 1 deﬁned over Fq such that the union of the zeros
of their zeta functions satisﬁes LI, the author shows that there is no bias among the race between
#C1(Fqn ) and #C2(Fqn ) as n → ∞.

This article cites [35, 215, 243].

[260] Mazur, B., Finding meaning in error terms, Bull. Amer. Math. Soc. (N.S.) 45 (2008), no. 2, 185–
228, MR2383303.

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 69

The author describes two manifestations of the Sato–Tate distribution for error terms and discusses
biases in sign in each case. The ﬁrst such situation arises when counting the number of representa-
tions of primes p as the sum of 24 squares, which is also the Fourier coeﬃcient of a modular form
of level 4 and weight 12 (where the Sato–Tate distribution is still a conjecture). In Section 1.8, the
author gives a graph showing a positive bias in the error term for this number of representations.
The second situation arises when counting points on elliptic curves modulo p (where the Sato–Tate
distribution is a theorem). In Section 2.3, the author provides graphs showing biases in sign in the
error terms for four (non-CM) elliptic curves: the rank-0 curve y2 + y = x
3 − x
2 exhibits a positive
bias, the rank-1 curve 31A (as labeled in Stein’s tables) exhibits a negative bias, and the rank-2
curve 389A and the rank-3 curve 5077A exhibit stronger negative biases. The author attributes
the letter [255] from Sarnak, shaped by conversations with Granville, that describes the conjectured
limiting logarithmic distributions associated with the normalized error terms in both problems: both
of them have nonzero means (in the case of elliptic curves the mean is 1 − 2 rank(E)) but inﬁnite
variances, which suggests that all these error terms should be positive and negative with logarithmic
density 1
2 .

This article cites [215, 250].

[261] Diamond, H. G. and Pintz, J., Oscillation of Mertens’ product formula, J. Th´eor. Nombres Bordeaux
21 (2009), no. 3, 523–533, MR2605532.

The authors show that − ∑
p≤x log(1 − 1
p ) − log log x − C0 = Ω±(1/(
√
x log x)), which implies that
∏
p≤x(1 − 1
p )
−1 − eC0 log x changes sign inﬁnitely often. If RH is false, the result is a consequence
of Landau’s theorem. If RH is true, the authors ﬁrst show that
∫ x

1
 dΠ(t)
t − ∫ x

1
 1 − t−1

t log t dt = Ω±
( log log log x
√
x log x
 )

and then use Littlewood’s [14] result on the sign changes of ∆
π(x) and Cram´er’s bound ∆
Eψ
1 (x) ≪ x.
The authors include a second proof in the RH case using a variant of the Wiener–Ikehara method
due to Ingham [35].

This article cites [14, 35, 41, 43, 74, 123].

[262] Kaczorowski, J., On the distribution of irreducible algebraic integers, Monatsh. Math. 156 (2009),
no. 1, 47–71, MR2470105.

Given a number ﬁeld K, the author studies the oscillations of the error term EK (x) for the counting
function of irreducible elements of K (up to units). Let ζKH (s) denote the Dedekind zeta function
of the Hilbert class ﬁeld of K, and let ρ denote a nontrivial zero of ζKH . The author introduces a
complicated integer-valued quantity m∗(ρ, K) related to the multiplicity of ρ; under the assumption
that some m∗(ρ, K) is nonzero, he proves that EK (x) = Ω±(√
x(log log x)
D(K)−1/ log x
)
, where
D(K) is the Davenport constant of the class group of K. As a result, when K has class number 2,
we unconditionally have EK(x) = Ω±(√
x log log x/ log x)
; when the class number is an odd prime p,
we have EK (x) = Ω±(
√x(log log x)
p−1/ log x) provided that ζKH (s) has at least one nontrivial zero
of multiplicity not divisible by p. All of these oscillations have logarithmic frequency. Assuming RH
for ζKH (s), the author sketches a proof of HK(x) ≪ √
x(log x)
D(K)+1.

This article cites [14, 180, 186, 188, 238, 254, 263].

[263] Kaczorowski, J. and Wiertelak, K., Oscillations of a given size of some arithmetic error terms,
Trans. Amer. Math. Soc. 361 (2009), no. 9, 5023–5039, MR2506435.

The authors use a combination of methods from [170, 180, 183, 254] to prove that

W (
Eψ(T ); T ; log log H(T )
) ≫ (log T )/H(T )

for suﬃciently large T , where H(T ) is a function with 1 ≪ H(T ) < log T . Letting H(T ) =
exp((log log T )
c) with a small c > 0, this theorem recovers the classical result of Littlewood that
∆
ψ(x) = Ω±(
√
x log log log x). They show the analogous bound for Eπ(T ; q, a, 1) assuming HC for
Dirichlet L-functions. The authors also investigate the summatory function D2(x) = ∑
n≤x 2ω(n).
Assuming that all the simple zeros ρ = 1/2 + iγ of ζ(s) on the critical line satisfy ζ′(ρ) ≫ |γ|−O(1),

70 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

they show that

W (
D2(T ); T ; T 1/4(log H(T ))
1/2(log log H(T ))
−3/2) ≫ (log T )/H(T )

for any function 1 ≪ H(T ) ≤ log T .

This article cites [14, 170, 180, 183, 186, 187, 193, 201, 206, 252, 254].

[264] Sneed, J. P., Prime and quasi-prime number races, Thesis (Ph.D.)–University of Illinois at Urbana-
Champaign, ProQuest LLC, Ann Arbor, MI, 2009, 83 pp., MR2753165.

In Chapter 2, the author veriﬁes HC for moduli q ≤ 100 and shows that all (two-way) prime
number races for such moduli have inﬁnitely many lead changes. In Chapter 3, the author explores
semiprime races, which concern the functions π2(x; q, ℓ) = #{p1p2 ≤ x : p1p2 ≡ ℓ (mod q)} and
E2(x; q, ℓ1, ℓ2) = (
π2(x; q, ℓ1)−π2(x; q, ℓ2)
) log x/√
x log log x. Assuming GRH and LI, he proves that
E2(x; 4, 3, 1) has mean − 1
2 (negative, unlike E(x; 4, 3, 1)) and takes negative values with logarithmic
density ≈ 0.894280.

This article cites [1, 10, 14, 34, 35, 48, 72, 82, 99, 114, 116, 125, 131, 215, 230, 232, 250].

[265] Cha, B. and Kim, S., Biases in the prime number race of function ﬁelds, J. Number Theory 130
(2010), no. 4, 1048–1055, MR2600420.

The authors derive a formula, in the function ﬁeld setting, for the logarithmic densities of races
among the counting functions of irreducible polynomials of degree up to X in residue classes. The
proofs follow [215] closely, although the authors introduce a smoothing function on the Fourier
side to overcome the problem that the Fourier transforms decay slowly due to the ﬁniteness of the
number of zeros of the relevant L-functions.

This article cites [215, 225, 250, 257].

[266] Chao, K. F. and Plymen, R., A new bound for the smallest x with π(x) > li(x), Int. J. Number
Theory 6 (2010), no. 3, 681–690, MR2652902.

The authors modify Lehman’s theorem [97] by improving the bound on θ1(x) = 2 log x
3 ( π(x)
x log x − 1)
using an inequality of Panaitopol. Together with 2 × 106 zeros of ζ(s) (supplied by Odlyzko), they
show that there exist at least 10154 consecutive integers x in the range [1.3978965×10316, 1.398344×
10316] for which π(x) > li(x).

This article cites [14, 27, 46, 74, 97, 190, 224, 258].

[267] Ford, K. and Sneed, J., Chebyshev’s bias for products of two primes, Experiment. Math. 19 (2010),
no. 4, 385–398, MR2778652.

The authors examine Chebyshev’s bias for integers which are the product of two primes. Let
π2(x; q, a) denote the number of integers n up to x such that n ≡ a (mod q) and Ω(n) = 2.

Assume GRH for Dirichlet L-functions modulo q and also that the zeros of L(s, χ) are simple
for each nonprincipal character χ (mod q). If f (x1, . . . , xr) is the logarithmic density function
of (
E(x; q, a1, b1), . . . , E(x; q, ar, br)
)
, the authors show that the logarithmic density function of(
E2(x; q, a1, b1), . . . , E2(x; q, ar, br)
) is

f ( cq(b1) − cq(a1)
2 − x1, . . . , cq(br) − cq(ar)
2 − xr
) .

Consequently, assuming both GRH and LI for modulus q, the authors show that δ2(
π2(x; q, a), π2(x; q, b)
)

exists, and equals 1
2 if a and b are both quadratic residues or both quadratic nonresidues (mod q).
Otherwise, if a is a quadratic nonresidue and b is a quadratic residue, then

1 − δq;a1,a2 < δ2(
π2(x; q, a), π2(x; q, b)
) < 1
2 .

This article cites [1, 14, 48, 71, 215, 232, 250, 264, 281].

[268] Kaczorowski, J., Ω-estimates related to irreducible algebraic integers, Math. Nachr. 283 (2010),
no. 9, 1291–1303, MR2730494.

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 71

The author continues his examination of EK(x) from [262], under the assumption that no entire
function from the Selberg class vanishes at s = 1 (which follows from Selberg’s orthonormality
conjecture). He shows that this assumption implies that at least one of the quantities m∗(ρ, K)
from his previous work is nonzero, and therefore that this nonvanishing assumption implies that
EK(x) = Ω±(√
x(log log x)
D(K)−1/ log x)
, where D(K) is the Davenport constant of the class group
of K. He also shows unconditionally that EK (x) = Ω±(
√x/(log x)
OK (1)). All these oscillations have
logarithmic frequency.

This article cites [170, 180, 188, 262, 263].

[269] Kaczorowski, J. and Wiertelak, K., Oscillations of the remainder term related to the Euler totient
function, J. Number Theory 130 (2010), no. 12, 2683–2700, MR2684490.

The authors study the oscillations of f (x) = ∑
n≤x φ(n) − 3
π2 x
2, the best known result being
f (x) = Ω±(x
√log log x) due to Montgomery. The authors show that f (x) = f AR(x)+f AN (x), where
the arithmetic part f AR(x) = ∑∞
n=1 µ(n)
n { x
n } and the analytic part f AN (x) = − ∫ x
0 f AR(t) dt
t =
1
2 ∑∞
n=1 µ(n){ x
n }2 + 1
2 . They establish Montgomery-type oscillations for f AR(x) and similar func-
tions, including examples arising from coeﬃcients of newforms. The analytic part f AN (x) has an
explicit formula (thus is o(x) unconditionally in particular) and is interesting in its own right, and
the authors establish Littlewood-type oscillations for it.

This article cites [170, 180, 183, 254, 262, 263, 268, 270].

[270] Kaczorowski, J. and Wiertelak, K., Smoothing arithmetic error terms: the case of the Euler φ
function, Math. Nachr. 283 (2010), no. 11, 1637–1645, MR2759800.

The authors observe that the order of magnitude of arithmetic error terms is often uninﬂuenced
by smoothing; for example, ∆
ψ(x) = Ω±(
√x log log log x) unconditionally and ∆
ψ(x) ≪ √
x(log x)
2

on RH, while A
ψ
1 (x) = Ω±(
√
x) unconditionally and A
ψ
1 (x) = O(
√x) on RH. If we deﬁne f (x) =
∑n≤x φ(n) − 3
π2 x
2, then Walﬁsz showed that f (x) ≪ x(log x)
2/3(log log x)
4/3 and Montgomery
showed that f (x) = Ω±(x
√log log x). In contrast, the authors show that A
f
1 (x) = Ω±(
√x log log log x)
unconditionally and A
f
1 (x) ≤ √x exp (
O(log x/ log log x)
) on RH.

This article cites [14, 170, 180, 183, 201, 206, 254, 262, 263, 268].

[271] Saouter, Y. and Demichel, P., A sharp region where π(x) − li(x) is positive, Math. Comp. 79 (2010),
no. 272, 2395–2405, MR2684372.

The authors improve the error term for the function I(ω, η) in Lehman’s theorem [97], which
allows them to conclude that there are more than 6.09 × 10150 successive integers in the vicin-
ity of exp(727.951335792) ≈ 1.397166707819 × 10316 such that π(x) > li(x). They show that
π(x) − li(x) > 9.1472 × 10149 for some x ∈ [1.39715131 × 10316, 1.39718211 × 10316]; assuming
RH, they show that π(x) − li(x) > 1.7503 × 10148 for some x in the smaller interval [1.3971619476 ×
10316, 1.3971714624 × 10316].

This article cites [74, 97, 148, 190, 224, 266].

[272] Brent, R. P. and Lune, J. van de, A note on P´olya’s observation concerning Liouville’s function, in:
Herman J. J. te Riele Liber Amicorum, CWI, 2011, pp. 92–97, url: https://arxiv.org/abs/1112.4911.

By ﬁnding an exact formula in terms of Jacobi’s theta function, the authors prove that

∞∑

n=1
 (−1)
Ω(n)

eπn/x + 1 = −
 √
2 − 1
2 √x + 1
2 + ON (x
−N )

as x → ∞ for every positive integer N , which they interpret as a bias of (−1)
Ω(n) towards negative
values.

This article cites [20, 35, 51, 59, 156, 181, 215, 241, 251, 256, 283].

[273] Cha, B. and Im, B.-H., Chebyshev’s bias in Galois extensions of global function ﬁelds, J. Number
Theory 131 (2011), no. 10, 1875–1886, MR2811555.

72 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

The authors study Chebyshev’s bias in a ﬁnite Galois extension F of a global function ﬁeld K.
Let πC (N ) be the number of prime elements in K of degree N whose Frobenius lies in C. Fol-
lowing the strategy of Rubinstein and Sarnak [215], the authors study the limiting distribution of
X
qX/2 ∑X
N =1 |G|
|C| (
πc(N ) − π(N )
). The authors show that when F/K is geometric and satisﬁes LI,
there is a bias towards conjugacy class of the Galois group containing fewer square elements, as in
the number ﬁeld case. The authors give a complete description of the prime element race in the case
of scalar ﬁeld extensions of K.

This article cites [215, 225, 250, 257, 259, 265].

[274] Fiorilli, D., Irr´egularit´es dans la distribution des nombres premiers et des suites plus g´en´erales dans
les progressions arithm´etiques, French, Thesis (Ph.D.)–Universit´e de Montr´eal, ProQuest LLC, Ann
Arbor, MI, 2011, 261 pp., MR3103752.

Chapter 2 of this thesis is the article [281]. A result in the introduction explains why the method
of [170] is not capable of producing more sign changes in the π-vs.-li race: the author shows that if

ψk(x) = 1
k!
 ∑

n≤x Λ(n)
( log x
n )k = x − ∑

ρ
 x
ρ

ρk+1 +
 k∑

j=0
 ak−j
j! (log x)
j

is the k-fold logarithmic average of ψ(x), then W (ψk; T ) = γ1
2π log T + Ok(1) for k ≥ 5, where
γ1 ≈ 14.1347 is the smallest ordinate of a nontrivial zero of ζ(s). The phenomenon is that the
repeated averaging washes out all of the small-scale sign changes expected for ψ(x) itself.

[275] Stoll, D. A. and Demichel, P., The impact of ζ(s) complex zeros on π(x) for x < 1010
13, Math.
Comp. 80 (2011), no. 276, 2381–2394, MR2813366.

The authors analyze Eπ(x) for x < 1010
13 using the ﬁrst 2 × 1011 nontrivial zeros of ζ(s). Based
on numerical computation, the authors suggest that there may exist an x near 1.397162914 × 10316

such that π(x) > li(x). The authors also conjecture that |Eπ(x)| < 1
e (log log log x + e + 1).

This article cites [14, 26, 27, 46, 74, 97, 122, 215, 224, 258, 266, 271].

[276] Kunik, M. and Lucht, L. G., Power series with the von Mangoldt function, Funct. Approx. Comment.
Math. 47 (2012), no. part 1, 15–33, MR2987108.

The authors investigate the series F (w) = ∑∞
n=1 Λ(n)
n wn for |w| ≤ 1. The authors use a more
convenient direct method compared to that of Hardy and Littlewood in [17] to derive the explicit
formulas for the series ∑ Λ(n)e−nz = 1/z + (cosh(z) − 1) log z + T (z) − ∑
ρ Γ(ρ)z−ρ and for F (e−z);
in particular the authors obtain a closed form for the entire function T (z). The main result re-
veals logarithmic singularities of F (e2πit) at the reduced rational numbers t = a
q with squarefree
denominator q ∈ N.

This article cites [17].

[277] Lamzouri, Y., Large deviations of the limiting distribution in the Shanks–R´enyi prime number race,
Math. Proc. Cambridge Philos. Soc. 153 (2012), no. 1, 147–166, MR2943671.

The author reﬁnes tail estimates for the distribution µq;a1,...,ar given by Rubinstein and Sarnak [215].
From the Math Review by D. R. Heath-Brown, with slight changes in notation: “Deﬁne

σ(q) = (
2 ∑

χ (mod q)
χ̸=χ0
 ∑

γ>0
 1
1/4 + γ2
 )1/2,

with γ running over ordinates of zeros of L(s, χ). . . . It is proved here that if 0 < λ ≤ √
log log q
then
 µq;a1,...,ar (
∥t∥2 > λσ(q)
) = (2π)
−r/2 ∫
∥t∥2>λ exp
(
− 1
2 ∥t∥2) dt + Or(
(log q)
−2)
.

. . . For large V it is shown that

exp
(
−c1 V 2

φ(q) log q
 ) ≪q µq;a1,...,ar (
∥t∥2 > V ) ≪q exp
(
−c2 V 2

φ(q) log q
 )

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 73

for (φ(q) log q)
1/2 ≪ V ≤ Aφ(q) log q, with constants c1, c2 depending only on r and A. For even
larger V the paper gives further results, showing that there are transitions in the behaviour, occur-
ring around V = φ(q) log q and V = φ(q) log2 q.”

This article cites [71–73, 76–79, 149, 150, 210, 215, 219, 281].

[278] Lamzouri, Y., The Shanks-R´enyi prime number race with many contestants, Math. Res. Lett. 19
(2012), no. 3, 649–666, MR2998146.

The author examines the order of magnitude of the density δq;a1,...,ar when the number of con-
testants r tends to inﬁnity as q → ∞. Assuming GRH and LI, he shows that δq;a1,...,ar = 1
r! (1 +
O( r2
log q )) when r ≤ √
log q, while δq;a1,...,ar = exp(−r log r + r + O(log r + r2
log q )) when √
log q ≪
r ≤ (1 − ε) log q/ log log q. For larger r, he provides the upper bound δq;a1,...,ar ≪ε q−1+2ε for
(1 − ε) log q/ log log q ≤ r ≤ φ(q).

This article cites [14, 71–73, 76–79, 133, 165, 210, 212, 215, 219, 225, 233, 235, 237, 277, 281].

[279] Milinovich, M. B. and Ng, N., A note on a conjecture of Gonek, Funct. Approx. Comment. Math.
46 (2012), 177–187, MR2931664.

Assuming RH and the simplicity of all zeros of ζ(s), the authors show that
∑

0<γ≤T
 1
|ζ′(ρ)|2 ≥ ( 3
2π3 − o(1)
)T.

This article cites [35, 51, 98, 181, 186, 222, 243].

[280] Mossinghoﬀ, M. J. and Trudgian, T. S., Between the problems of P´olya and Tur´an, J. Aust. Math.
Soc. 93 (2012), no. 1–2, 157–171, MR3062002.

For α ∈ [0, 1], deﬁne Lα(x) = ∑

n≤x(−1)
Ω(n)/nα. The authors generalize classical results of P´olya
and Tur´an by proving that RH is equivalent to the estimate Lα(x) ≪α,ε x
1/2−α+ε for all ε > 0, the
equivalence being for any (hence all) α ∈ [0, 1]. Modifying the function slightly by deﬁning

Lα(x) = Lα(x) −
 



0, if 0 ≤ α < 1
2 ,
log x/2ζ( 1
2 ), if α = 1
2 ,
ζ(2α)/ζ(α), if 1
2 < α ≤ 1,

they also show that the assertion, for any c ∈ R, that Lα(x) − cx
1/2−α has constant sign implies
that all the zeros of ζ(s) are simple but is incompatible with LI, even with ﬁnitely many exceptions.
(The assertion that L1/2(x) − c itself has constant sign is shown to imply that all zeros of ζ(s)
have multiplicity at most 2, but is not known to be inconsistent with LI.) The authors state the
problem of showing that Lα(x) has inﬁnitely many sign changes, which is known only for α = 0 and
α = 1 [51], and also of showing that L1/2(x) ≤ 0 for x suﬃciently large, perhaps x ≥ 17.

This article cites [35, 37, 51, 59, 156, 186, 215, 256].

[281] Fiorilli, D. and Martin, G., Inequities in the Shanks-R´enyi prime number race: an asymptotic formula
for the densities, J. Reine Angew. Math. 676 (2013), 121–212, MR3028758.

Assuming GRH and LI, the authors establish an asymptotic series for δq;a,b whose error term can
be taken to be any negative power of q. The ﬁrst asymptotic formula given by this series, in the
case where a is a quadratic nonresidue and b is a quadratic residue (mod q), is

δq;a,b = 1
2 + ρ(q)
√
2πV (q; a, b) + Oε(q−3/2+ε),

where V (q; a, b) = ∑χ (mod q) |χ(b) − χ(a)|2 ∑
ρ 1/( 1
4 + γ2) and ρ(q) is the number of square roots
of 1 (mod q). The authors give a closed form for V (q; a, b) in terms of arithmetic properties of its
arguments, which allow them to compare various values of δq;a,b; for example, for ﬁxed a ̸= −1, they
show (always assuming GRH and LI) that when q is suﬃciently large, δq;−1,1 < δq;a,1 whenever −1
and a are both quadratic nonresidues (mod q). Explicit bounds for the error terms in this formula
allow the authors to calculate the list of all 117 two-way prime number races (up to symmetries)
for which δq;a,b > 0.9, the largest of which is δ24,5,1 ≈ 0.999988.

74 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

This article cites [56, 74, 132, 165, 215, 225, 229].

[282] Ford, K., Lamzouri, Y., and Konyagin, S., The prime number race and zeros of Dirichlet L-functions
oﬀ the critical line: Part III, Q. J. Math. 64 (2013), no. 4, 1091–1098, MR3151605.

The authors construct “barriers” for two-way prime number races, including π(x)− li(x). They show
that a certain hypothetical conﬁguration of zeros of L(s, χ) would imply that {x ≥ 2 : π(x; q, b) >
π(x; q, a)} has asymptotic density 0. Furthermore, they show that a certain hypothetical conﬁgura-
tion of the zeros of ζ(s) would imply that {x ≥ 2 : π(x) > li(x)} has asymptotic density 0, while a
related conﬁguration would result in the same set having asymptotic density 1.

This article cites [14, 71–73, 75–79, 84, 85, 91–93, 96, 118, 210, 212, 215, 232, 233, 237, 250, 264].

[283] Humphries, P., The distribution of weighted sums of the Liouville function and P´olya’s conjecture,
J. Number Theory 133 (2013), no. 2, 545–582, MR2994374.

The author gives an excellent review of the history and known results concerning the weighted
Liouville summatory function Lα(x) = ∑
n≤x λ(n)/nα. Deﬁne δα to be the logarithmic density of
the set of positive real numbers x such that Lα(x) ≤ 0. Assuming RH and LI and the estimate∑
0<γ<T |ζ′(ρ)|−2 ≪ T , the author shows when 0 ≤ α < 1
2 that 1
2 ≤ δα < 1, so that in particular,
Lα(x) changes sign inﬁnitely often. The author additionally shows under the same hypotheses that
limα→1/2− δα = 1. Moreover, the author proves (without needing the hypothesis LI) that δ1/2 = 1,
lending some credence to the conjecture that L1/2(x) ≤ 0 for x ≥ 17.

This article cites [20, 35, 41, 51, 54, 112, 150, 156, 158, 196, 197, 215, 225, 227, 243, 256, 280, 284,
328].

[284] Lamzouri, Y., Prime number races with three or more competitors, Math. Ann. 356 (2013), no. 3,
1117–1162, MR3063909.

Assuming GRH and LI, the author describes phenomena that occur for multi-way prime number
races that are not present in two-way races. When r ≥ 3, the author shows that ∣
∣δq;a1,...,ar − 1
r! ∣
∣ =
Ω(1/ log q), in contrast to the r = 2 case [281] where ∣
∣δq;a1,a2 − 1
2 ∣
∣ ≪ q−1/2+o(1). The author
also shows that when q is suﬃciently large in terms of r, there are always r squares a1, . . . , ar
modulo q for which δq;a1,...,ar ̸= 1
r! (and similarly r nonsquares). The method of proof is to study
the approximation of the characteristic function ˆµq;a1,...,ar by that of a multivariate Gaussian, paying
particular attention to secondary main terms that arise.

This article cites [71–73, 75–79, 131, 165, 210, 212, 215, 219, 225, 233, 250, 278, 281].

[285] Myerscough, C., Application of an accurate remainder term in the calculation of residue class dis-
tributions, 2013, url: https://arxiv.org/abs/1301.1434.

The author studies the family Pµ(t) of density functions of the sum of random variables
∑

χ |χ(a) − χ(b)| ∑

γ>µ
 2ℜZγ
√
1/4 + γ2

where Zγ are independent random variables, uniformly distributed on the unit circle, indexed by
the ordinates of zeros of L(s, χ); the motivation is that P0(t) has the same distribution as the prime
number race measure µq;a,b. The author discovers that when t is small, the behaviour of Pµ(t)
approaches the normal distribution over a wider and wider range of t/σµ as µ increases, while when
t is large, Pµ(t) decays signiﬁcantly faster than a normal distribution.

To explicitly evaluate Pµ(t), the author compares the methods of the steepest descent (to third
order), numerical convolution methods, and the Rubinstein–Sarnak method, and notes that there
is an agreement to within 0.001% for 1 ≤ t ≤ 1.2 (and similar observations for other ranges of t).
The author points out that Rubinstein–Sarnak is the best way to obtain results which are much
larger than the absolute accuracy of computation, while the steepest descent method is desirable
for extreme deviations, and the convolution method is valuable for some intermediate ranges.

This article cites [14, 26, 97, 149, 215, 223–225, 229, 235, 239, 277, 281, 290].

[286] Petrushov, O. A., Asymptotic estimates of functions based on the behavior of their Laplace trans-
forms near singular points, Math. Notes 93 (2013), no. 5–6, 906–916, MR3206041.

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 75

The author establishes results on the limit supremum and inﬁmum of a real continuous function
ν(t) under assumptions on the behavior of the Laplace transform ∫ ∞
0 e−st dν(t) near its singular
point. As a corollary, the author obtains results on the limiting behavior of the function Ma(x) =∑n<x µ(n)n−a for 0 ≤ a ≤ 1
2 in terms of functions related to 1/ζ(s).

This article cites [181].

[287] Akbary, A., Ng, N., and Shahabi, M., Limiting distributions of the classical error terms of prime
number theory, Q. J. Math. 65 (2014), no. 3, 743–780, MR3261965.

The authors establish a suﬃcient condition for when general functions of the form

ℜ ∑

λn≤X rneiλny + E(y, X)

(or vector-valued analogues) are B2-almost-periodic and therefore possess limiting distributions.
They apply this theorem, assuming the appropriate RH, to (logarithmically scaled versions of)
functions such as: ∑n≤x Λ(n)an(π) for automorphic L-functions L(s, χ); the Mertens and Liouville
functions M (x) and L(x), analogues of these for arithmetic progressions, and interpolations between
these and Mr(x) and Lr(x); and (on the further assumption that Artin L-functions are entire) for
prime counting functions in Chebotarev conjugacy classes. They provide further conclusions if the
linear independence of the λn is also assumed.

This article cites [21, 28, 29, 32, 51, 147, 156, 181, 196, 197, 209, 215, 225, 227, 243, 256, 279, 281,
283, 284, 289, 290].

[288] Chaubey, S., Lanius, M., and Zaharescu, A., Irrational factor races, Proc. Indian Acad. Sci. Math.
Sci. 124 (2014), no. 4, 471–479, MR3306734.

Atanassov deﬁned the “irrational factor” of the number n = pr1
1 · · · prk
k to be I(n) = p1/r1
1 · · · p1/rk
k .
The authors establish an asymptotic formula for the summatory function of I(n) over a reduced
residue class. They then use a Landau-type argument to show that the race between the summatory
functions of I(n) over integers that are 1 (mod 3) and integers that are 2 (mod 3) has inﬁnitely
many lead changes; they remark that a theorem from [263] shows that the number of sign changes
in [1, T ] is ≫ log T when T is suﬃciently large.

This article cites [10, 14, 71, 183, 263].

[289] Fiorilli, D., Elliptic curves of unbounded rank and Chebyshev’s bias, Int. Math. Res. Not. IMRN
(2014), no. 18, 4997–5024, MR3264673.

The author extends the results from [255] on “elliptic curve prime number races”, the races between
primes for which the number of points on a given elliptic curve over Fp is greater or less than
p + 1. Assuming GRH and LI for L-functions of elliptic curves, the author establishes an equivalence
between two phenomena. The ﬁrst phenomenon is unbounded analytic ranks for elliptic curves—
more precisely, the conjecture that lim supNE→∞ ran(E)/√
log(NE) = ∞ where NE is the conductor
of E. The second phenomenon is the existence of arbitrarily biased elliptic curve prime races, that
is, races for which the logarithmic density of the set {t : S(t) = − ∑
p≤t app−1/2 ≥ 0} is arbitrarily
close to 1. When showing that the ﬁrst phenomenon implies the second, LI can be weakened to the
hypothesis that the nonreal zeros of L-functions of any elliptic curve have multiplicities bounded
by a universal constant. When showing that the second phenomenon implies the ﬁrst, only LI is
required, and in fact the author shows that the existence of arbitrarily biased races under LI would
imply GRH for an inﬁnite family of L(s, E).

This article cites [14, 215, 227, 228, 250, 255, 260, 281, 287].

[290] Fiorilli, D., Highly biased prime number races, Algebra Number Theory 8 (2014), no. 7, 1733–1767,
MR3272280.

It is known, assuming GRH and LI, that δ(p; N, R) tends to 1
2 as the prime modulus p tends to
inﬁnity. In contrast, the author shows that the analogous density δ(q; N, R) takes a set of values that
is dense in ( 1
2 , 1), under the same two assumptions (although LI can be weakened to a mild bound
on the multiplicities of zeros of L(s, χ)), with large biases corresponding to highly composite moduli
in a quantitative sense (including a conjecture for the asymptotic size of the analogues of Skewes’s

76 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

number for these races). The author proves similar results for fairly general linear combinations of
reduced residue classes.

This article cites [17–19, 27, 149, 150, 215, 217, 224, 225, 227–229, 243, 250, 277, 281, 285, 287].

[291] Humphries, P., On the Mertens conjecture for elliptic curves over ﬁnite ﬁelds, Bull. Aust. Math.
Soc. 89 (2014), no. 1, 19–32, MR3163001.

The author gives a necessary and suﬃcient condition for an elliptic curve over a ﬁnite ﬁeld to satisfy
the function ﬁeld analogue of the Mertens conjecture lim supX→∞ |ME/Fq (X)|/qX/2 ≤ 1 (as studied
by the author in [292]), in terms of the order of the ﬁnite ﬁeld and the trace of the Frobenius
endomorphism acting on the curve. Moreover, the author shows if the Mertens conjecture holds for
a given elliptic curve, then in fact lim supX→∞ |ME/Fq (X)|/qX/2 = 1.

This article cites [4, 35, 112, 181, 251, 295, 308].

[292] Humphries, P., On the Mertens conjecture for function ﬁelds, Int. J. Number Theory 10 (2014),
no. 2, 341–361, MR3189983.

Cha [308] introduced the Mertens function MC/Fq (X) of a smooth projective curve deﬁned over a
ﬁnite ﬁeld, and showed under LI that EMC/Fq (X) is bounded where EMC/Fq (X) = MC/Fq (X)/qX/2.
Thus, a natural analogue of the Mertens conjecture for function ﬁelds would be

lim sup
X→∞ |EMC/Fq (X)| ≤ 1.

For ﬁxed q and g, let H2g+1,qn denote the set of hyperelliptic curves y2 = f (x) over Fqn arising
from squarefree monic polynomials in Fqn [x] of degree 2g + 1. The author shows that as n → ∞,
almost all curves in H2g+1,qn satisfy lim supX→∞ |EMC/Fqn (X)| > 1, while for any β > 1, a positive
proportion of curves in H2g+1,qn satisfy lim supX→∞ |EMC/Fqn (X)| ≤ β.

This article cites [4, 13, 35, 112, 181, 243, 251, 259, 291, 295, 308].

[293] Radziejewski, M., Oscillatory properties of real functions with weakly bounded Mellin transform, Q.
J. Math. 65 (2014), no. 1, 249–266, MR3179660.

The author summarizes many existing Landau-type oscillation theorems, and establishes a new
oscillation theorem for functions whose Mellin transforms satisfy certain growth conditions (weaker
than usual) and have certain singularities (more general than usual). As an application, he shows
that the counting function of numbers that can be written as the sum of two squares has oscillations
of size x
1/2(log x)
−3/2−ε; he generalizes this result to ∑n≤x( 1
4 r(n))
z , where r(n) is the number of
representations of n as the sum of two squares, for generic z (but not z = 1).

This article cites [3, 10, 71, 75, 79, 183, 188, 248, 249, 262, 268].

[294] Saouter, Y. and Riele, H. te, Improved results on the Mertens conjecture, Math. Comp. 83 (2014),
no. 285, 421–433, MR3120597.

The authors reﬁne Pintz’s eﬀective disproof [189] of the Mertens conjecture and show that |M (x)| >
1.0088√
x for some x < exp(1.004×1033). The authors also discuss possibilities for obtaining smaller
counterexamples.

This article cites [4, 181, 189, 251, 253, 271].

[295] Best, D. G. and Trudgian, T. S., Linear relations of zeroes of the zeta-function, Math. Comp. 84
(2015), no. 294, 2047–2058, MR3335903.

Using the method of Grosswald [117], the authors prove that

lim inf
x→∞ EM (x) < −1.6383 and lim sup
x→∞ EM (x) > 1.6383.

The proof uses a reﬁned variant of the LLL-algorithm and a kernel function used by Odlyzko and
te Riele [181], as well as several techniques for speeding up the computation.

In the appendix of the article, the authors list new lower bounds on m for the “m-dependence”
of the ﬁrst n positive ordinates of nontrivial zeros of ζ(s), for n ≤ 500. This numerical evidence,
combined with Grosswald’s theorem, provides new proofs that Eπ(x), L(x), and Lr(x) change signs
inﬁnitely often.

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 77

This article cites [35, 51, 112, 116, 117, 125, 158, 181, 251].

[296] B¨uthe, J., On the ﬁrst sign change in Mertens’ theorem, Acta Arith. 171 (2015), no. 2, 183–195,
MR3414306.

Rosser and Schoenfeld [74] observed that ∆
πr (x) ≥ 0 for 1 ≤ x ≤ 108. The author proves that
there exists an x0 ≈ 1.91 × 10215 such that ∆
πr (x) < 0 for x ∈ [x0 − 6 × 10103, x0]. The proof is
an adaptation of a method of Lehman [97] that improved upon Skewes’s number, though with a
diﬀerent choice of kernel function.

This article cites [27, 74, 97, 169, 300].

[297] Fiorilli, D., The distribution of the variance of primes in arithmetic progressions, Int. Math. Res.
Not. IMRN (2015), no. 12, 4421–4448, MR3356760.

The author studies the “variance” of primes in arithmetic progressions

V (x; q) = ∑

(a,q)=1
 ∣
∣
∣
∣ψ(x; q, a) − ψ(x; χ0)
φ(q)
 ∣
∣
∣
∣
2

that was ﬁrst examined by Hooley and is known to be asymptotic to x log q in certain ranges
of q. The author conjectures that V (x; q) ∼ x log q uniformly for (log log x)
1+δ ≤ q ≤ x for any ﬁxed
δ > 0, a much wider range than previously anticipated. The conjecture arises from the computation,
assuming GRH and LI, of the limiting logarithmic distribution of V (x; q) for a given q and studying
its large deviations.

This article cites [34, 132, 149, 150, 215, 225, 227, 235, 243, 259, 277, 278, 281, 284, 289, 290].

[298] Kisilevsky, H. and Rubinstein, M. O., Chebotarev sets, Acta Arith. 171 (2015), no. 2, 97–124,
MR3414302.

Let Podd = {2, 5, 11, 17, 23, 31, . . .} be the set consisting of every other prime (the odd-index primes).
In this article, the authors show that Podd cannot be written as a ﬁnite union of sets of the form
{p : p ≡ a (mod q)}, even up to ﬁnitely many exceptions. More generally, call a set P of prime ideals
of a number ﬁeld K a Chebotarev set if there are ﬁnitely many ﬁnite Galois extensions Li/K and
conjugacy classes Ci such that the symmetric diﬀerence of the sets P and ⋃
i{p ⊂ K : σp(Li/K) =
Ci} is ﬁnite. Using explicit formulas, the authors show that if P is a Chebotarev set of density
β ∈ Q with 0 < β < 1 (and P (x) counts the number of elements of P of norm up to x), then
∆P (x) = P (x) − βπK(x) = Ω(x
1/2/ log x). In particular, Podd is not a Chebotarev set (hence not a
ﬁnite union of sets of primes in residue classes), since the counting function Podd(x) = 1
2 π(x)+ O(1).

This article cites [26, 215].

[299] Lay, J., Sign changes in Mertens’ ﬁrst and second theorems, 2015, url: https://arxiv.org/abs/1505.03589.

The author shows that the functions Eθ
r (x) and Eπ
r (x) change sign inﬁnitely often. Under RH, fol-
lowing a similar proof used by Diamond and Pintz [261], the author shows Eθ
r (x) = Ω±( log log log x
)

and the same for Eπ
r (x). Similar to the work of Lamzouri [304], assuming RH and LI, the author
proves that both the logarithmic densities of {x > 1 : Eθ
r (x) > 0} and {x > 1 : Eπ
r (x) > 0} equal
δ(li, π) ≈ 0.99999974.

This article cites [26, 34, 74, 215, 261, 287, 304].

[300] Saouter, Y., Trudgian, T., and Demichel, P., A still sharper region where π(x) − li(x) is positive,
Math. Comp. 84 (2015), no. 295, 2433–2446, MR3356033.

The authors incorporate both theoretical and computational improvements to show that there are
more than 7.17×10152 consecutive integers in the interval [1.397165243588×10316, 1.397167149324×
10316] for which π(x) > li(x).

This article cites [14, 97, 258, 271].

[301] Bhowmik, G., Ramar´e, O., and Schlage–Puchta, J.-C., Tauberian oscillation theorems and the dis-
tribution of Goldbach numbers, English, with English and French summaries, J. Th´eor. Nombres
Bordeaux 28 (2016), no. 2, 291–299, MR3509711.

78 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

The authors establish an eﬀective version of Landau’s theorem for Dirichlet integrals, which they
apply to the function Gk(n) = ∑

n1+···+nk=n Λ(n1) · · · Λ(nk) counting the weighted number of rep-
resentations of n as the sum of k primes. Further deﬁning

∆k(x) = ∑

n≤x Gk(n) − x
k

k! + k ∑

ρ
 x
ρ+k−1

ρ(ρ + 1) · · · (ρ + k − 1) ,

they show under RH that ∆2(n) = Ω±(x) and, for particular constants ck, that ∆k(n) − ckx
k−1 =
Ω±(x
k−1) for k ≥ 3.

This article cites [71, 244].

[302] Cha, B., Fiorilli, D., and Jouve, F., Prime number races for elliptic curves over function ﬁelds, Ann.
Sci. ´Ec. Norm. Sup´er. (4) 49 (2016), no. 5, 1239–1277, MR3581815.

The authors describe the prime number race for elliptic curves over the function ﬁeld of a proper,
smooth, and geometrically connected curve over a ﬁnite ﬁeld. Let E/K be a family of elliptic curves
of unbounded conductor for which L(E/K, T ) satisﬁes LI (which can be conﬁrmed in some cases) and
such that rank(E/K) = o(
√NE/K) as NE/K → ∞. Then, the random variable √
q−1
√q XE/√
NE/K
converges in distribution to the standard Gaussian as NE/K → ∞. As a consequence, δ(E) (the
proportion of those x for which more primes up to x have positive trace of Frobenius ap(E) than
negative) tends to 1
2 .

Moreover, the authors also study the behavior of the function TE(X) = −Xq−X/2 ∑deg(v)≤X 2 cos θv
associated to the elliptic curves of Ulmer’s family of elliptic curves over Fq[t]. They discuss the cases
of extreme bias and moderate bias for Ulmer’s family. Moreover, through proving a central limit
theorem, the authors shows that δ(Ef ) − 1
2 = Ω( 1√d ) for quadratic twists Ef .

This article cites [215, 255, 257, 260, 281, 287, 289, 290].

[303] Dummit, D., Granville, A., and Kisilevsky, B., Big biases amongst products of two primes, Mathe-
matika 62 (2016), no. 2, 502–507, MR3521338.

This article establishes permanent, relatively large biases in races involving products of two primes.
The authors show that if χ is a quadratic character (mod d), then

#{pq ≤ x : χ(p) = χ(q) = −1}
#{pq ≤ x : (pq, d) = 1} = 1 − ( ∑

p
 χ(p)
p + o(1)
) 1
log log x ,

and the same statement with both minus signs changed to plus signs. In particular, the race between
integers pq with χ(p) = χ(q) = −1 and those with χ(p) = χ(q) = 1 has a bias in favor of the sign
of (and proportional to) ∑
p χ(p)/p.

For example, ∑p χ5(p)/p ≈ −1.008, and correspondingly integers pq with both p and q qua-
dratic nonresidues (mod 5) are 41.6% more numerous up to 107 than random chance would sug-
gest. The authors conjecture that there exists d ≤ x such that the right-hand side is as large as
1 + log log log x/log log x. They also note that the same proof gives a bias for the ratio
∑

p≤x
χ(p)=1
 1
p
 ∕ ∑

p≤x
χ(p)=−1
 1
p = 1 + (
2 ∑

p
 χ(p)
p + o(1)
) 1
log log x ,

giving a permanent bias involving only primes (in contrast to the unweighted race between π(x; d, R)
and π(x; d, N )); the proof also generalizes to products of k primes with prescribed quadratic char-
acter values (for ﬁxed k). They remark on the possibility of counting pq ≤ x where p and q are
restricted to prescribed but arbitrary residue classes.

This article cites [267].

[304] Lamzouri, Y., A bias in Mertens’ product formula, Int. J. Number Theory 12 (2016), no. 1, 97–109,
MR3455269.

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 79

Let M be the set of real numbers x > 1 such that ∏
p≤x(1 − 1/p)
−1 > eC0 log x. Assuming RH, the
author proves that both M and its complement have positive lower logarithmic density. Further
assuming LI, the author shows that the logarithmic density of M equals δ(li, π) ≈ 0.99999974. The
author also conjectures that

lim sup
x→∞
 (( ∏

p≤x
 (
1 − 1
p
 )−1 − eC0 log x
)∕ (log log log x)
2
√x
 ) = eC0

2π

and the symmetric result for the lim inf.

This article cites [14, 74, 149, 150, 215, 250, 261, 282], as well as an earlier draft of this annotated
bibliography.

[305] Lemke Oliver, R. J. and Soundararajan, K., Unexpected biases in the distribution of consecutive
primes, Proc. Natl. Acad. Sci. USA 113 (2016), no. 31, E4446–E4454, MR3624386.

Given a tuple a = (a1, . . . , ar) of reduced residues modulo q, let

π(x; q, a) = #{pn ≤ x : pn+i−1 ≡ ai (mod q) for each 1 ≤ i ≤ r}

count the occurrences of the pattern of residues deﬁned by a. The authors observe (among other
things) that repeated residues appear less frequently than changing ones; for example, for x0 = p108 ,
we have π(x0; 10, (1, 3)) = 7,429,438 but π(x0; 10, (1, 1)) = 4,623,042. The authors conjecture that
all patterns occur equally often in the limit, but that lower order terms create predictable biases; in
contrast to prime number races and their inﬁnity of sign changes, some of these inequalities should
always hold, such as π(x; 3, (1, −1)) > π(x; 3, (1, 1)) for x ≥ 5. The authors provide numerical
evidence for their conjectures, as well as heuristic justiﬁcation related to the Hardy–Littlewood
prime k-tuples conjecture.

This article cites [134, 215, 250, 303].

[306] Platt, D. J. and Trudgian, T. S., On the ﬁrst sign change of θ(x) − x, Math. Comp. 85 (2016),
no. 299, 1539–1547, MR3454375.

The authors compute that ∆
θ(x) < 0 for 0 ≤ x ≤ 1.39×1017. By partial summation, this implies that
∆
π(x) < 0 for 2 < x ≤ 1.39 × 1017. The authors also prove that there exists x ≈ 1.3971623 × 10316

for which ∆
θ(x) > 0.

This article cites [14, 26, 46, 97, 224, 252, 258, 300].

[307] Riele, H. J. J. te, The Mertens conjecture, in: The legacy of Bernhard Riemann after one hundred
and ﬁfty years. Vol. II, vol. 35.2, Adv. Lect. Math. (ALM), Int. Press, Somerville, MA, 2016, pp. 703–
718, MR3525909.

This article is a survey of the history of the Mertens conjecture and related computations. The author
summarizes methods and techniques for disproving the Mertens conjecture and more generally for
estimating lim inf EM(x) and lim sup EM(x).

This article cites [4, 5, 7, 9, 12, 13, 35, 42, 59, 80, 107, 112, 117, 125, 143, 181, 189, 241, 251, 294,
295].

[308] Cha, B., The summatory function of the M¨obius function in function ﬁelds, Acta Arith. 179 (2017),
no. 4, 375–395, MR3684399.

The author investigates an analogue of the Mertens sum for function ﬁelds. Let C be a nonsingular
projective curve deﬁned over a ﬁnite ﬁeld Fq of characteristic p > 2. The author deﬁnes the M¨obius
function µC/Fq (D) of C/Fq for all eﬀective divisors D of C to be

µC/Fq (D) =
 




1, if D = 0,
0, if a prime divisor divides D with order at least 2,
(−1)
t, if D is a sum of t distinct prime divisors.

80 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

Let cµ(N ) = ∑deg(D)=N µC/Fq (D) and MC/Fq (X) = ∑
deg D≤X µC/Fq (D). The author justiﬁes these
new deﬁnitions by showing that the Dirichlet series Zµ(u) associated with µC/Fq (D) for a divisor D
is closely related to the the zeta function ZC/Fq (u) associated with the curve C:

1
ZC/Fq (u) = Zµ(u) = ∑

D≥0
 µC/Fq (D)
N Ds =
 ∞∑

N =0 cµ(N )uN ,

where u = q−s and N D is the absolute norm of D, so that MC/Fq (X) = ∑N ≤X cµ(N ). By working
with the coeﬃcients, the author shows that MC/Fq (X) ≪ X 2g−1qX/2.

Let γ1 = √qeiθ1, . . . , γ2g = √
qeiθ2g be the inverse zeros of ZC/Fq (u), where g is the genus of C. The
curve C is said to satisfy LI if the set {θj : 0 ≤ θj ≤ π} ∪ {π} is linearly independent over Q. The
author shows that LI implies

D(C/Fq) = lim sup
X→∞
 |MC/Fq (X)|
qX/2 =
 2g∑

j=1
 ∣
∣
∣
∣
∣ γj
Z ′
C/Fq (γ−1
j ) γj
γj − 1
 ∣
∣
∣
∣
∣ < ∞,

while D(C/Fq) = ∞ if there is a zero with multiple order. The author also shows that a family
of hyperelliptic curves satisfy LI and computes the geometric average of D(C/Fq) over this family
using an equidistribution theorem due to Deligne.

This article cites [4, 35, 181, 215, 243, 257, 259, 273, 292].

[309] Hough, P., A lower bound for biases amongst products of two primes, Res. Number Theory 3 (2017),
Art. 19, 11, MR3692499.

The author establishes a stronger version of a conjecture from [303] on the biases between products
of two primes, by showing that suﬃciently large x, there are at least exp (
(C − ε)
√
log x
) integers
d ≤ exp(C√
log x) such that

#{pq ≤ x : χd(p) = χd(q) = −1}
1
4 #{pq ≤ x : (pq, d) = 1} ≥ 1 + log log log x + O(1)
log log x ,

and similarly with “ ≥ 1 + · · · ” replaced by “ ≤ 1 − · · · ” and/or with −1 replaced by 1 on the
left-hand side. The author also shows that GRH implies that these oscillations are best possible.
The proof uses a result of Granville and Soundararajan on extremal values of L(1, χ).

This article cites [250, 281, 303].

[310] Meng, X., The distribution of k-free numbers and the derivative of the Riemann zeta-function, Math.
Proc. Cambridge Philos. Soc. 162 (2017), no. 2, 293–317, MR3604916.

Assuming RH, this article connects the normalized error term EQk (x) = (Qk(x) − x/ζ(k))/x
1/2k

for the distribution of k-free numbers with the sum J−1(T ) = ∑0<γ≤T |ζ′(ρ)|−2 over nontrivial
zeros of ζ(s). The author ﬁrst shows that J−1(T ) ≪ε T 1+ε holding for all ε > 0 is equivalent to
∫ X
1 EQk (x)
2 dx
x ≪k log X holding for all k ≥ 2. If in fact J−1(T ) ≪ε T 1+ε for all ε > 0, the author
proves that for each k ≥ 2,

lim
X→∞ 1
log X
 ∫ X

1 EQk (x)
2 dx
x = ∑

γ>0
 2|ζ(ρ/k)|2

|ρζ′(ρ)|2

and EQk (x) has a limiting logarithmic distribution. The author establishes analogous results for
M (x). Assuming (RH still and) the assumption J−1(T ) ≪ T 2−δ for any ﬁxed δ > 0, he establishes a
weaker version of Mertens conjecture, namely ∫ X
2 (M (x)/x)
2 dx ≪ log X, and proves that M (x) ≪
x
1/2(log log x)
3/2 except on a set of ﬁnite logarithmic measure. He also shows that

lim
X→∞ 1
log X
 ∫ X

1 EM (x)
2 dx
x = ∑

γ>0
 2
|ρζ′(ρ)|2

and EM (x) has a limiting logarithmic distribution.

This article cites [24, 186, 196, 197, 243, 287].

[311] Mossinghoﬀ, M. J. and Trudgian, T. S., The Liouville function and the Riemann hypothesis, in:
Exploring the Riemann zeta function, Springer, Cham, 2017, pp. 201–221, MR3700043.

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 81

The authors show that

lim inf
x→∞ EL(x) < −2.3723 and lim sup
x→∞ EL(x) > 1.0028

lim inf
x→∞ ELr (x) < −1.0028 and lim sup
x→∞ ELr (x) > 2.3723.

They further deﬁne Lα(x) = ∑n≤x λ(n)n−α for all α ∈ (0, 1), and show that Lα(x) changes signs
inﬁnitely often for each α ∈ (0, 0.29714 . . .), while Lα(x) − ζ(2α)/ζ(α) changes signs inﬁnitely often
for each α ∈ (0.70285, . . . , 1). The theoretical and computational reasoning employed is similar
to [295].

This article cites [9, 35, 37, 51, 59, 99, 112, 116, 117, 125, 156, 158, 181, 256, 283, 287, 295].

[312] B¨uthe, J., An analytic method for bounding ψ(x), Math. Comp. 87 (2018), no. 312, 1991–2009,
MR3787399.

The author presents a fast analytic algorithm for computing approximate values of ψ(x) on intervals
of the shape [x, Lx] for ﬁxed L > 1. As an application, the author shows that ∆
π(x) < 0 for 2 ≤ x ≤
1019, improving the best known lower bound for the Skewes number by Platt and Trudgian [306].
The calculations took about 1,200 hours on a 2.27 GHz Intel Xeon X7560 CPU.

This article cites [74, 275, 306].

[313] Harper, A. J. and Lamzouri, Y., Orderings of weakly correlated random variables, and prime num-
ber races with many contestants, Probab. Theory Related Fields 170 (2018), no. 3-4, 961–1010,
MR3773805.

The authors investigate, assuming GRH and LI, the asymptotic behavior of δq;a1,...,an when the num-
ber of competitors n grows as a function of the modulus q. They show that if n ≤ log q/(log log q)
4

then δq;a1,...,an ∼ 1
n! , resolving an unpublished conjecture by Ford and Lamzouri and strengthening
results of Rubinstein and Sarnak [215] and Lamzouri [284]. They prove that this is not necessarily
true for larger n, as predicted by Feuerverger and Martin [225]: when φ(q)
ε ≤ n ≤ φ(q) one has
lim inf q→∞ n!δq;a1,...,an < 1.

They further discuss the ﬁrst k leaders in a prime number race: for each integer 1 ≤ k ≤ n, they
deﬁne δk(q; a1, . . . , an) to be the logarithmic density of the set of real numbers x ≥ 2 such that

π(x; q, a1) > π(x; q, a2) > · · · > π(x; q, ak) > max
k+1≤j≤n π(x; q, aj).

They show that if 2 ≤ n ≤ φ(q)
1/32 then δ1(q; a1, . . . , an) ∼ 1
n , and that the analogous result
δk(q; a1, . . . , an) ∼ (n−k)!
n! holds for k(log k)
10 ≤ (log q)/ log n but not for n ≥ φ(q)
ε.

In addition to using the circle method to control the average size of correlations in prime number
races, the authors develop sophisticated probabilistic tools including an exchangeable pairs version
of Stein’s method and variants of “normal comparison” lemmas of Slepian.

This article cites [14, 71–73, 75, 76, 78, 79, 210, 212, 213, 215, 219, 225, 233, 250, 278, 281, 282,
284, 290, 328], as well as an earlier draft of this annotated bibliography.

[314] Hurst, G., Computations of the Mertens function and improved bounds on the Mertens conjecture,
Math. Comp. 87 (2018), no. 310, 1013–1028, MR3739227.

The author extends Odlyzko and te Riele’s disproof of Mertens conjecture [181] by obtaining stronger
bounds using more modern algorithms and computers. In particular the author proves that

lim inf
x→∞ EM (x) < −1.837625 and lim sup
x→∞ EM (x) > 1.826054.

The author computes M (x) for x ≤ 1016 and for x = 254, . . . , 273. The algorithm operates in
logspace, lowering the amount of storage required during computations. The author notes that
cache misses were a signiﬁcant source of increased computing time for larger values of M (x); they
suggest that a future algorithm could further reduce cache size by storing M¨obius values in two bits,
rather than bytes.

This article cites [35, 42, 99, 181, 241, 243, 295].

[315] Meng, X., Chebyshev’s bias for products of k primes, Algebra Number Theory 12 (2018), no. 2,
305–341, MR3803705.

82 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

Deﬁne πk(x; q, a) = #{n ≤ x : n ≡ a (mod q), ω(n) = k}, and deﬁne Nk(x; q, a) to be the analogous
function with ω(n) replaced by Ω(n); deﬁne πk(x; q, a, b) = πk(x; q, a) − πk(x; q, b) and similarly
for Nk(x; q, a, b). Assuming GRH and the simplicity of the zeros of L(s, χ), the author establishes
asymptotic formulas relating πk(x; q, a, b) and Nk(x; q, a, b) to N1(x; q, a, b) = π(x; q, a, b). Further
assuming LI, the author establishes the existence of the logarithmic densities δ(πk(x; q, a, b)) and
δ(Nk(x; q, a, b)) (including computations of several such), characterizes when these densities are less
than or greater than 1
2 , and demonstrates how the distances from such densities to 1
2 decrease as
functions of k.

This article cites [1, 14, 44, 48, 71, 148, 186, 215, 232, 250, 267, 281, 284].

[316] Meng, X., Large bias for integers with prime factors in arithmetic progressions, Mathematika 64
(2018), no. 1, 237–252, MR3778223.

Given k ≥ 2 and a multiset {a1, . . . , ak} of reduced residues modulo q, the author determines an
asymptotic formula for the number of squarefree integers up to x that can be written as p1p2 · · · pk
with each pj ≡ aj (mod q), with an explicit second-order term of relative size 1/ log log x compared
to the main term. In particular, certain such multisets are biased over others, and those biases are
eventually permanent. The constants in this second-order term are closely related to the constants
in Mertens sum for primes in arithmetic progressions, which are heavily inﬂuenced by the least
prime appearing. The author’s results are given both for ﬁxed k and with k growing like a constant
multiple of log log x.

This article cites [242, 267, 303, 315].

[317] Schlage–Puchta, J.-C., Oscillations of the error term in the prime number theorem, Acta Math.
Hungar. 156 (2018), no. 2, 303–308, MR3871592.

Using the power-sum method and Pintz’s technique of kernel functions, the author improves Pintz’s
result [168] on localized oscillations of ∆
ψ. The main result is that if 0 < ε < 1
e , and ρ0 = σ0 + iγ0
is a zero of ζ(s) with σ0 ≥ 1
2 + ε and γ0 > 8.31/ε, then for each T suﬃciently large (depending
explicitly on γ0 and ε), there exists x ∈ [T, T 1+ε] such that |∆
ψ(x)| ≫ x
σ0 /γ1+ε
0 .

This article cites [31, 40, 166, 168, 177].

[318] Ford, K., Harper, A. J., and Lamzouri, Y., Extreme biases in prime number races with many con-
testants, Math. Ann. 374 (2019), no. 1-2, 517–551, MR3961320.

The authors show that prime race densities δq;a1,...,ar can have size signiﬁcantly diﬀerent from 1
r!
when r is suﬃciently large in terms of q. More precisely, they show that there exists η > 0 and
a1, . . . , ar (mod q) such that

δq;a1,...,ar ≤ exp (
− η min{n, φ(q)
1/50}
log q
 ) 1
r! ,

and an analogous lower bound for large values without the negative sign on the right-hand side.
They derive this result from a similar result concerning the density of real numbers x such that
π(x; q, a1) > · · · > π(x; q, ak) are the k largest of the r prime counting functions while simultaneously
π(x; q, ak+1) < · · · < π(x; q, a2k) are the k smallest. The authors exploit the fact that certain
E(x; q, aj) are known to have large correlations of size Ω−(1/ log q); they also develop a comparison
theorem to multivariate normal distributions with a relative rather than absolute error.

This article cites [132, 215, 225, 232, 237, 250, 278, 281, 284, 290, 313], as well as an earlier draft of
this annotated bibliography.

[319] Humphries, P., Shekatkar, S. M., and Wong, T. A., Biases in prime factorizations and Liouville func-
tions for arithmetic progressions, J. Th´eor. Nombres Bordeaux 31 (2019), no. 1, 1–25, MR3996180.

Given a set S of integers, deﬁne ΩS(n) = #{p | n : p ∈ S}. The authors study ΣS(x) = ∑
n≤x(−1)
ΩS (n)

when S is a union of residue classes modulo q. If S is the complete set of reduced residue classes
(mod q) then ΣS(x) is similar to L(x); if q is prime and S is the set of quadratic nonresidues (mod q),
then ΣS(x) is similar to ∑
n≤x( n
q ) except that (−1)
ΩS(n) takes nonzero values at multiples of q as
well.
 ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 83

The authors show that the general behavior of ΣS(x) is more predictable than these special cases: if S
is the union of r reduced residue classes (mod q) with r /∈ {φ(q), φ(q)
2 }, then ΣS(x) ∼ b0x/(log x)
2−2r/ϕ(q)

for some explicit constant b0 that has the same sign as φ(q)
2 − r. If r = φ(q)
2 , then still ΣS(x) = o(x)
provided that S is not a set of the form {n : χ(n) = −1} for some quadratic Dirichlet character
χ (mod q). Finally, suppose that S = {n : χ(n) ̸= −1} for some quadratic χ (mod q). Assuming
GRH, LI, and ∑
0<γ≤T |L′(ρ, χq)|−2 ≪ T θ for some 1 < θ < 3 − √
3, the authors show that the
logarithmic density δ of {x > 0 : ΣS(x) ≥ 0} exists and satisﬁes 1
2 ≤ δ < 1.

This article cites [20, 35, 51, 256, 283, 287, 295, 310, 316].

[320] Lamzouri, Y. and Martin, B., On the race between primes with an odd versus an even sum of the
last k binary digits, Funct. Approx. Comment. Math. 61 (2019), no. 1, 7–25, MR4012359.

Let A and B be disjoint sets of reduced residue classes modulo q with #A = #B. If A and B
contain the same number of quadratic residues, the authors prove that HC implies π(x; q, A, B) =
Ω±(
√
x/ log x). Under GRH and LI, the authors show that δq;A,B = 1
2 if A and B contain the same
number of quadratic residues while δq;A,B < 1
2 if A contains more quadratic residues than B.

Using these results, the authors study the oscillation and the limiting logarithmic distribution of the
function Sk(x) = ∑p≤x(−1)
sk(p), where sk(p) is the sum of the last k binary digits of p (note S2(x) =
π(x; 4, 3, 1) − 1 recovers Chebyshev’s bias [1]). The ﬁrst result above implies that Sk(x) changes sign
inﬁnitely often for all k ≥ 2, while the second result above implies that δ({x : Sk(x) > 0}) = 1
2 for
k ≥ 4. (In both cases the assumptions refer to Dirichlet L-functions modulo 2k.) The authors further
compute that δ({x : S3(x) > 0}) = δ({x : π(x; 8, 3) + π(x; 8, 5) > π(x; 8, 1) + π(x; 8, 7)}) ≈ 0.9822
using the approach of Rubinstein–Sarnak [215].

This article cites [17, 72, 106, 210, 215, 232, 282].

[321] Lichtman, J. D., Martin, G., and Pomerance, C., Primes in prime number races, Proc. Amer. Math.
Soc. 147 (2019), no. 9, 3743–3757.

Assuming GRH and LI, the authors show that the set of primes q for which π(q) > li(q) has a well-
deﬁned logarithmic relative density in the set of all primes, whose value equals δ(π, li) (approximately
2.6 · 10−7). The same is true of the set of primes q such that eC0 log q > ∏
p≤q(1 − 1/p)
−1, and the
set of primes q such that 1/ log q > ∑
p≥q 1/p log p. The methods apply to discrete subsets of R that
are well-distributed in almost all short intervals (such as the integers themselves).

This article cites [14, 215, 224, 281, 287, 304, 312, 325].

[322] Mahatab, K. and Mukhopadhyay, A., Measure-theoretic aspects of oscillations of error terms, Acta
Arith. 187 (2019), no. 3, 201–217, MR3902795.

The authors prove a quantitative version of Landau’s theorem on oscillations of the error term
∆(x) appearing in the asymptotic formula for a summatory function, provided that the Mellin
transform A(s) = ∫ ∞
1 ∆(x)/x
s+1 dx satisﬁes certain analytic properties. More precisely, if A(s) has
a singularity at σ0+it0 for some t0 ̸= 0 and has no real singularity for σ ≥ σ0, then Landau’s theorem
gives ∆(x) = Ω±(x
σ0 ). Under additional assumptions on A(s), the authors obtain oscillation results
for the Lebesgue measure of sets of the form {x ∈ [T, 2T ] : ∆(x) > λx
σ0 } and {x ∈ [T, 2T ] : ∆(x) <
−λx
σ0 }. In particular, for the Mertens sum, the authors deduce unconditionally that the Lebesgue
measure of the set {
x ∈ [T, 2T ] : EM (x) > |ρ1ζ′(ρ1)|−1 − o(1)
} is Ω(T 1−ε) for each ε > 0, where
ρ1 = 1
2 + iγ1 is a nontrivial zero of ζ(s) closest to the real axis.

This article cites [10, 17, 35, 158, 301].

[323] Platt, D. and Trudgian, T., Fujii’s development on Chebyshev’s conjecture, Int. J. Number Theory
15 (2019), no. 3, 639–644, MR3925757.

The authors show that GRH for L(s, χ−4) is equivalent, for any 0 < α < 20.40442, to

lim
x→∞
 ∑

p χ−4(p)e−(x/n)α = −∞;

they show also that the given method cannot be extended to α < 20.40443.

This article cites [17, 18, 97, 192, 215, 232, 312].

84 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

[324] Alkan, E., Biased behavior of weighted Mertens sums, Int. J. Number Theory 16 (2020), no. 3,
547–577, MR4079395.

The author considers weighted Mertens sums restricted to integers that are products of primes from
a set of primes P with #P(x) = π(x) + O(x/(log x)
3+α) for some α > 0. Under this condition, it is
shown that there exists a δ = δ(P) > 0 such that given σ ∈ (1, 1 + δ),
∑

n≤x
p|n =⇒ p∈P
ω(n)≡1 (mod 2)
 µ(n)(log n)
2

nσ < 0

holds when x is suﬃciently large in terms of σ. The author also studies inequalities of the shape
∑

n≤x
p|n =⇒ p∈P
ω(n)≡1 (mod 2)
 µ(n)(log n)
k

nσ < 0

for all k ∈ N. Finally, the author states the conjecture that for any k ∈ N and σ ≥ 1,
∑

n≤x
ω(n)≡1 (mod 2)
 |µ(n)|(log n)
k

nσ < ∑

n≤x
ω(n)≡0 (mod 2)
 |µ(n)|(log n)
k

nσ

when x is suﬃciently large.

This article cites [4, 35, 60, 181, 233, 241, 243, 250, 251, 288, 294, 304, 307].

[325] Devin, L., Chebyshev’s bias for analytic L-functions, Math. Proc. Cambridge Philos. Soc. 169 (2020),
no. 1, 103–140, MR4120786.

The author extends the study of prime number races to counting functions with explicit formulas
associated to general L-functions from the Selberg class, including Dirichlet L-functions and Hasse–
Weil L-functions. She unconditionally proves the existence of a limiting logarithmic distribution for
these counting functions, and establishes properties of the limiting distribution (such as absolute
continuity) under much weaker conditions than GRH and LI.

This article cites [215, 233, 250, 260, 287].

[326] Devin, L., Limiting properties of the distribution of primes in an arbitrarily large number of residue
classes, Canad. Math. Bull. 63 (2020), no. 4, 837–849, MR4176773.

The author extends her earlier weakening of the LI assumption to the setting of prime number races
with many contestants. Assuming GRH but only weakened versions of the LI assumption, she shows
the existence of logarithmic densities associated to r-way prime number races. Her methods apply
equally well to the number ﬁeld and function ﬁeld settings (in the latter case, GRH is no longer a
hypothesis). An erratum appeared in the same journal in 2021 (MR4352666).

This article cites [215, 232, 238, 250, 257, 259, 265, 273, 287, 302, 315, 321, 325, 328].

[327] Lemke Oliver, R. J. and Soundararajan, K., The distribution of consecutive prime biases and sums
of sawtooth random variables, Math. Proc. Cambridge Philos. Soc. 168 (2020), no. 1, 149–169,
MR4043824.

The authors continue their study of biases in the patterns of consecutive primes (mod q). Their
conjectures in [305] contained a tertiary main term with complicated constants c2(q, a) whose dis-
tribution was not easily understood. In this article, they connect these constants with both the
discrete Fourier transform of Dedekind sums and the error term R(x) = ∑n≤x φ(n) − 3
π2 x
2. They
show that q−1c2(q, (a, b)) has a continuous limiting distribution as q → ∞ (connected to that of
the related Dedekind sums), and that x
−1R(x) has a limiting distribution with doubly exponential
decay.

This article cites [213, 305].

[328] Martin, G. and Ng, N., Inclusive prime number races, Trans. Amer. Math. Soc. 373 (2020), no. 5,
3561–3607, MR4082248.

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 85

The authors investigate, under GRH, how to weaken the LI assumption in earlier results. Say that a
zero 1
2 +iγ of some Dirichlet L-function (mod q) with γ ≥ 0 is “self-suﬃcient” if it cannot be written
as a rational linear combination of other such zeros (so that LI is true if and only if all such zeros
are self-suﬃcient). The authors show that a certain ﬁnite number of self-suﬃcient zeros is enough
for the logarithmic limiting distributions of Eπ(x; q, a1, . . . , ar) to exist (in which case the r-way
race is “weakly inclusive”). If the sum of reciprocals of ordinates of self-suﬃcient zeros is suﬃciently
large in terms of q, the authors show that all logarithmic densities δq;a1,...,ar exist and are positive
(the race is “inclusive”); if that reciprocal sum diverges, then the distribution of Eπ(x; q, a1, . . . , ar)
assigns mass to every open set in Rr (the race is “strongly inclusive”). These last two properties
are stronger than an r-way race being “exhaustive”, which indicates that all r! possible orderings
occur for arbitrarily large x.

This article cites [32, 35, 82, 114, 116, 117, 206, 210, 215, 237, 250, 264, 281–283, 287, 325].

[329] Meng, X., Number of prime factors over arithmetic progressions, Q. J. Math. 71 (2020), no. 1,
97–121, MR4077187.

Assuming GRH and LI, the author proves that both ∑n≤x ω(n)χ−4(n) < 0 and ∑
n≤x Ω(n)χ−4(n) >
0 on sets of logarithmic density 1. This result gives a conditional conﬁrmation of a conjecture of
G. Martin.

This article cites [1, 196, 197, 215, 287, 310, 315, 316].

[330] Mossinghoﬀ, M. J. and Trudgian, T. S., A tale of two omegas, in: 75 years of mathematics of
computation, vol. 754, Contemp. Math. Amer. Math. Soc., [Providence], RI, 2020, pp. 343–364,
MR4132130.

Let H(x) = ∑
n≤x(−1)
ω(n). The authors prove that H(x) > 1.7√
x and H(x) < −1.7√
x inﬁnitely
often, complementing existing results on oscillations for L(x). The proof is very similar to that of
the follow-up paper [337].

This article cites [4, 20, 35, 51, 59, 99, 112, 116, 117, 125, 158, 181, 186, 215, 243, 256, 280, 283,
295, 311, 314].

[331] Plymen, R., The Great Prime Number Race, vol. 92, Student Mathematical Library, American
Mathematical Society, Providence, RI, 2020, p. 138, MR4249594.

Chapter 6 provides a comprehensive overview of the methods used to study the oscillations of
π(x) − li(x). Chapter 7 outlines known results on the logarithmic density of the race between π(x)
and li(x), as well as upper bounds for the Skewes number.

This book cites [14, 26, 27, 46, 97, 186, 190, 215, 224, 266, 271, 275, 321].

[332] Porritt, S., Character sums over products of prime polynomials, 2020, url: https://arxiv.org/abs/2003.12002.

The author proves asymptotic formulas for character sums over degree-n monic polynomials in Fq[t]
with a ﬁxed number of prime factors k (counted with multiplicity). This type of asymptotic formula
was previously considered in [336], where the results held when k = o(
√
log n). The author extends
the range of uniformity to 1 ≤ k ≤ q1/2−ε log n for any ε > 0 when the character is complex, and to
1 ≤ k ≤ (log n)
2/3 when the character is real.

This article cites [215, 250, 267, 315, 336].

[333] Alkan, E., Variations on criteria of P´olya and Tur´an for the Riemann hypothesis, J. Number Theory
225 (2021), 90–124, MR4231545.

Inspired by the Mertens conjecture, P´olya’s problem, and Tur´an’s problem and their connections
with RH, the author explores the connection between weaker versions of RH and the bias of certain
weighted sums involving the M¨obius function and the Liouville function. Given a set P of primes,
the author deﬁnes the “restricted M¨obius function” µP (n) = µ(n) if all prime factors of n are in P
and µP (n) = 0 otherwise. Let 1
2 ≤ σ0 < 1, and let P be a set of primes that omits ≪ x
σ0 primes
up to x. The author shows, for each κ ∈ {0, 1, 2}, that σ0-RH is equivalent to the statement that
the partial sum ∑n≤x µP (n)(log n)
κ/nα is eventually negative for all σ0 < α < 1. An analogous
statement is also proved for the restricted Liouville function.

This article cites [35, 51, 57, 280, 311, 324, 330, 352].

86 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

[334] Bailleul, A., Chebyshev’s bias in dihedral and generalized quaternion Galois groups, Algebra Number
Theory 15 (2021), no. 4, 999–1041, MR4265352.

This article studies a generalization of Chebyshev’s bias to the Chebotarev density theorem, which
was ﬁrst investigated by Ng [227]. Namely, if L/K is a Galois extension of number ﬁelds and C is
a conjugacy class of Gal(L/K), then πC (x) denotes the number of unramiﬁed prime ideals p of K
with norm N (p) ≤ x and whose Artin symbol ( p
L/K ) equals C. For any two conjugacy classes C1
and C2 of Gal(L/K), a “Chebotarev race” measures the logarithmic density of values x such that
πC1(x)/#C1 > πC2 (x)/#C2. Fiorilli and Jouve [363] have shown that some Chebotarev races are
extremely biased (in that the logarithmic density is close to 1) and the author continues this study
in a new context.

Using class ﬁeld theory constructions and results on root numbers of quaternion extensions, the
author analyzes Chebyshev’s bias in certain families of number ﬁeld extensions with Galois groups
of 2-power order, namely dihedral or generalized quaternion. Conditional on GRH and variants of
LI, he performs an analysis in two diﬀerent aspects: the “horizontal aspect” (ﬁxed Galois group) and
the “vertical aspect” (high-degree towers of 2-power order). Each direction reveals an interesting
connection between the central zeros of Artin L-functions and the bias of the Chebotarev race; this
relationship is a key novelty of the article.

This article cites [1, 34, 71, 84, 210, 215, 217, 227, 257, 273, 278, 281, 284, 313, 315, 318, 325, 328,
342, 363].

[335] Devin, L., Discrepancies in the distribution of Gaussian primes, 2021, url: https://arxiv.org/abs/2105.02492.

Every p ≡ 1 (mod 4) can be written uniquely as p = a2 + 4b2 with positive integers a, b. The
author formulates two conjectures concerning counting functions related to the distribution of these
numbers a and 2b. First, she conjectures that the function ∑p≤x, p≡1 (mod 4) sign(a − 2b) is negative
for a set of logarithmic density strictly between 1
2 and 1, and thus there is a bias towards the
even square being larger than the odd square in such representations. Second, she conjectures that∑p≤x, p≡1 (mod 4) χ−4(a) is eventually always positive, so that there is a complete bias towards
the positive odd number in such representations being 1 (mod 4) rather than 3 (mod 4). Both
conjectures rely on her extension of existing results to cover counting functions that are governed
by a sum of inﬁnitely many L-functions (such as Hecke L-functions).

This article cites [34, 215, 238, 255, 287, 289, 290, 302, 325], as well as an earlier draft of this
annotated bibliography.

[336] Devin, L. and Meng, X., Chebyshev’s bias for products of irreducible polynomials, Adv. Math. 392
(2021), Paper No. 108040, 45, MR4316675.

The authors study the counting function of polynomials in Fq[t] in sets of invertible residue classes
modulo a ﬁxed polynomial that have k irreducible factors (these can be counted either with or
without multiplicity). They prove asymptotic formulas for the normalized diﬀerences of two such
counting functions in terms of the zeros of the relevant L-functions; these asymptotic formulas
are valid for k almost as large as √
log X where X bounds the degree of the polynomials being
counted. In the important special case where the sets of residue classes are the quadratic residues
and nonresidues, the formulas simplify and the sign of the bias analyzed: assuming LI, the bias is
towards quadratic residues when we count irreducible factors without multiplicity, while the bias
depends on the parity of k when we count them with multiplicity. Finally, the authors use the fact
that some L-functions vanish at the critical point q−1/2 to show that there exist completely biased
and unbiased races, contrary to what is expected in the number ﬁeld setting.

This article cites [215, 232, 242, 257, 259, 267, 281, 287, 290, 302, 315, 316, 326, 328].

[337] Mossinghoﬀ, M. J., Oliveira e Silva, T., and Trudgian, T. S., The distribution of k-free numbers,
Math. Comp. 90 (2021), no. 328, 907–929, MR4194167.

For each k ≥ 2, set
 Ck = min{
lim sup
x→∞ ∆
Qk (x)
x1/2k , ∣
∣
∣
∣lim inf
x→∞ ∆
Qk (x)
x1/2k
 ∣
∣
∣
∣
}
.

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 87

The authors show that Ck > 3 for 2 ≤ k ≤ 5 and Ck > 2 for 6 ≤ k ≤ 10, and that Ck > 0.74969
for all suﬃciently large k, improving previously known lower bounds on Ck signiﬁcantly. The proof
is based on a variant of Ingham’s method developed by Anderson and Stark [158]. To achieve that,
the authors establish weak linear dependence relations among a subset of ordinates of ζ via the LLL
algorithm. The massive computation required approximately 5 core-years.

This article cites [24, 35, 98, 125, 158, 167, 186, 243, 280, 295, 310, 311, 330].

[338] Mossinghoﬀ, M. J. and Trudgian, T. S., Oscillations in weighted arithmetic sums, Int. J. Number
Theory 17 (2021), no. 7, 1697–1716, MR4295379.

The authors continue to investigate oscillations in weighted sums of arithmetic functions involv-
ing (−1)
Ω(n) and (−1)
ω(n) as in their previous papers [280, 311, 330]. For 0 ≤ α ≤ 1, let Hα(x) =∑n≤x(−1)
ω(n)/nα. Deﬁne Hα(x) = Hα(x) when 0 ≤ α ≤ 1
2 and Hα(x) = Hα(x)−∑n≥1(−1)
ω(n)/nα

when 1
2 < α ≤ 1, and set EHα (x) = Hα(x)x
α−1/2. The authors prove that lim inf EHα(x) ≤ −1.7
and lim sup EHα (x) ≥ 1.7, generalizing the oscillation result concerning H0(x) from [330]. The
authors also establish analogous results for the summatory function Sα(x) = ∑
n≤x(−1)
n−Ω(n)/nα.

This article cites [20, 35, 51, 59, 99, 112, 116, 117, 125, 158, 256, 280, 283, 295, 311, 314, 330, 337].

[339] Shchebetov, A., Chebyshev’s bias visualizer, 2021, url: http://math101.guru/en/downloads-2/repository/.

This website contains the downloadable application “Chebyshev’s bias visualizer”, which permits
graphical exploration of prime number races with many parameters customizable by the user. The
author has explored several races for larger values of x than previously and, in particular, discovered
the ﬁrst region where π(x; 12, 5, 1) < 0 (starting at 25,726,067,172,577) and the ﬁrst region where
π(x; 12, 7, 1) < 0 (starting at 27,489,101,529,529).

[340] Aymone, M., A note on prime number races and zero free regions for L functions, Int. J. Number
Theory 18 (2022), no. 1, 1–8, MR4369787.

The author observes that GRH for L(s, χ−4) would imply that ∑
p≤x χ−4(p)p−σ would be eventually
negative when σ → 1/2+. He investigates the connection between the sign changes of the weighted
prime number races associated to a real nonprincipal Dirichlet character χ and the zero-free region of
the corresponding L-function L(s, χ), proving that there exists 0 ≤ σ < 1 such that ∑p≤x χ(p)p−σ

has only ﬁnitely many sign changes if and only if there exists ε > 0 such that L(s, χ) ̸= 0 in the
half plane σ > 1 − ε.

This article cites [186, 250, 313].

[341] Bailleul, A., Explicit Kronecker–Weyl theorems and applications to prime number races, Res. Num-
ber Theory 8 (2022), no. 3, Paper No. 43, 34, MR4447414.

The author proves general versions of Kronecker–Weyl theorems, both in the discrete and continuous
settings and with no linear independence assumption, where the sets on which the equidistribution
is guaranteed are explicitly constructed. The article consists of many applications of these explicit
theorems, including suﬃcient conditions for lower bounds for the lower densities in certain Cheb-
otarev races. The applications are given in a more general setting for random variables, where the
densities are bounded by probabilities of certain explicitly given events. As a concrete application,
in the last part of the article, the author studies densities for prime divisor races in geometric Galois
extensions of function ﬁelds of one variable over ﬁnite ﬁelds, including the cases for which the LI
hypothesis fails to hold.

This article cites [215, 227, 238, 257, 273, 287, 302, 325, 326, 328, 336, 363].

[342] Fiorilli, D. and Jouve, F., Unconditional Chebyshev biases in number ﬁelds, J. ´Ec. polytech. Math.
9 (2022), 671–679, MR4400872.

If L/K is a Galois extension of number ﬁelds and C is a conjugacy class in Gal(L/K), then
π(x; C, L/K) denotes the number of unramiﬁed prime ideals p of K with norm N (p) ≤ x whose
Frobenius conjugacy class Frobp equals C. For two conjugacy classes C1, C2, let δL/K;C1,C2 be
the logarithmic density of the set {
x ≥ 1 : 1
#C1 π(x; C1, L/K) > 1
#C2 π(x; C2, L/K)
}
. The authors
unconditionally show that there are inﬁnitely many Galois extensions L/K and conjugacy classes
C1, C2 such that δL/K;C1,C2 = 1.

88 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

This article cites [1, 215, 217, 227, 363].

[343] Hathi, S. and Lee, E. S., Mertens’ third theorem for number ﬁelds: a new proof, Cram´er’s inequality,
oscillations, and bias, 2022, url: https://arxiv.org/abs/2112.02166.

The authors establish number ﬁeld analogues of existing results on Mertens sums. Given a number
ﬁeld K, let ∆
MK (x) = ∏N (p)≤x(1 − 1/N (p))
−1 − eC0κK log x for an appropriate constant κK. The
authors show that if there exists a non-real rightmost zero σK of ζK(s), then ∆
MK (x) changes sign
inﬁnitely often, generalizing the case K = Q which was shown in [261]. Assuming GRH, they show
that the lower logarithmic densities δ(∆
MK , 0) and δ(0, ∆
MK ) are both positive, generalizing results
in [304]. They provide numerics for these logarithmic densities for the two cases K = Q(
√
5) and
K = Q(
√
13). They also show that δ(∆
MK , 0) → 1
2 for quadratic ﬁelds K as the discriminant of K
tends to inﬁnity.

This article cites [14, 21, 74, 97, 215, 261, 287, 304].

[344] Heap, W., Li, J., and Zhao, J., Lower bounds for discrete negative moments of the Riemann zeta
function, Algebra Number Theory 16 (2022), no. 7, 1589–1625, MR4496076.

Under the assumption of RH and the simplicity of all zeros of ζ(s), the authors show that
∑

0≤γ≤T
 1
|ζ′(ρ)|2k ≫ T (log T )
(k−1)2

for all rational numbers k ≥ 0; this lower bound is of the expected order of magnitude when
0 < k < 3/2.

This article cites [35, 181, 186, 196, 197, 243, 279, 283, 310].

[345] Kim, J., Prime running functions, Exp. Math. 31 (2022), no. 4, 1291–1313, MR4516258.

From the Math Review by S. S. Wagstaﬀ, Jr.: “This article introduces a new type of prime counting
statistic. The prime running function Φ(x; d, a) counts the number of integers n ≤ x for which
the largest prime p ≤ n satisﬁes p ≡ a (mod d). In other words, Φ(x; d, a) counts the primes
p ≡ a (mod d), each weighted by the length of the gap from p to the next larger prime (in any
residue class). The author conjectures that

Φ(x; d, a) = x
φ(d) + R(d; a) x
log x + o
( x
log x
 )
,

as x → ∞, where R(d; a) is a (nonzero) ‘bias’ constant. A modiﬁed Cram´er probabilistic model . . .
is rigorously analyzed. It predicts the functional form displayed above for Φ(x; d, a), including the
bias. Experimental evidence also supports this shape, at least for small values of d. For example,
computation suggests that R(5; a) is about −0.07, −0.22, 0.21, 0.09 for a = 1, 2, 3, 4, respectively. It
is conjectured that R(d; −a) = −R(d; a).”

This article cites [1, 14, 17, 71, 215, 218, 221, 225, 250, 290, 305].

[346] Koyama, S.-y. and Kurokawa, N., Chebyshev’s bias for Ramanujan’s τ -function via the deep Riemann
hypothesis, Proc. Japan Acad. Ser. A Math. Sci. 98 (2022), no. 6, 35–39, MR4432981.

Given a sequence M (p) of r × r unitary matrices indexed by primes, deﬁne

L(s, M ) = ∏

p det(
1 − M (p)p−s)−1

for ℜ(s) > 1. Assume that L(s, M ) has an analytic continuation to an entire function and that
L( 1
2 , M ) ̸= 0. The Deep Riemann Hypothesis (DRH) in this context is the assumption that the
Euler product deﬁning L(s, M ) converges for s = 1
2 and limx→∞ ∏
p det(1 − M (p)p−1/2)
−1 =
2δ(M)/2L( 1
2 , M ) where δ(M ) is the order of the pole of L(s, M 2) at s = 1. Assuming DRH for
L(s, M ), the authors show that

lim
x→∞
 ∑
p≤x tr(M (p))/p1/2

log log x = − δ(M )
2 .

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 89

Let τ (n) denote Ramanujan’s τ -function and let L(s, ∆) = ∑∞
n=1 τ (n)n−s, so that L(s+ 11
2 , ∆) is an
example of such an L(s, M ). Assuming DRH for L(s+ 11
2 , ∆), the authors show that ∑p≤x τ (p)/p6 ∼
1
2 log log x, and consequently the natural density of A = {x > 0 : ∑
p≤x τ (p)/p6 > 0} equals 1.

This article cites [14, 215, 217, 255, 351, 359].

[347] Lin, J. and Martin, G., Densities in certain three-way prime number races, Canad. J. Math. 74
(2022), no. 1, 232–265, MR4379402.

Assuming GRH and LI, the authors establish an asymptotic formula for δq;a1,a2,a3 in the case when
a2
1 ≡ a2
2 ≡ a2
3 (mod q), with a power savings in q in the error term; the main term, which is the
arctangent of a speciﬁed algebraic function of the quantities b(χ) = ∑L(ρ,χ)=0 1/|ρ|2, arises as an
orthant probability for a multivariate normal random variable. The congruence hypothesis allows
for an atypical normalization of the Eπ(x; q, aj) for which any given χ (mod q) appears in at most
one of the three such expressions, allowing one to model the error terms by independent random
variables. The authors propose that to minimize their error terms, asymptotic formulas for δq;a1,...,ar
always be phrased in terms of orthant probabilities.

This article cites [215, 235, 278, 281, 284, 313].

[348] Morrill, T., Platt, D., and Trudgian, T., Sign changes in the prime number theorem, Ramanujan J.
57 (2022), no. 1, 165–173, MR4360480.

The authors show that
 lim inf
T →∞ W ψ(T )
log T ≥ γ1
π + 1.867 · 10−30,

improving the best known bound given by Kaczorowski [207]; the result is achieved by following
Kaczorowski’s method with some theoretical and computational improvements.

This article cites [97, 109, 170, 180, 201, 207, 252, 306].

[349] Mossinghoﬀ, M. J. and Trudgian, T. S., Oscillations in the Goldbach conjecture, J. Th´eor. Nombres
Bordeaux 34 (2022), no. 1, 295–307, MR4450618.

Fujii [204] studied the function G(x) = ℜ ∑γ>0 x
iγ /( 1
2 + iγ)( 3
2 + iγ) and its connection to Gold-
bach’s conjecture. In this article, the authors show that lim sup G(x) > 0.021030 and lim inf G(x) <
−0.022978 under RH, improving Fujii’s result. Moreover, they show lim sup G(x) > 0.022978 under
the extra assumption that the ordinates of the ﬁrst 106 zeros of ζ(s) in the upper half-plane are
linearly independent over Q. They also show that |G(x)| < 0.023059 for all x > 0. The SageMath
computations used in the proof required approximately 24 core-days.

This article cites [97, 181, 204, 301, 314, 338].

[350] Sedrati, Y., Inequities in the Shanks–Renyi prime number race over function ﬁelds, Mathematika
68 (2022), no. 3, 840–895, MR4449835.

The author extends results for classical prime number races [225, 284] to the function ﬁeld setting.
Given a prime power q and a monic polynomial m ∈ Fq[T ], the function πq(a, m, N ) counts the
number of irreducible polynomials P ∈ Fq[T ] of degree N such that P ≡ a (mod m). Let δm;a1,...,ar
be the density of integers X such that ∑X
N =1 πq(a1, m, N ) > · · · > ∑X
N =1 πq(ar, m, N ). Assuming
LI, the author establishes an asymptotic formula for δm;a1,...,ar as the degree of m tends to inﬁnity.
The author further shows that races with three or more competitors behave diﬀerently than two-way
races in the sense that δm;a1,a2 − 1
2 ≪ q(−1/2+o(1)) deg m while |δm;a1,...,ar − 1
r! | = Ω(1/ deg m) when
r ≥ 3. When a1, . . . , ar have bounded degree, the author provides a simple criterion for δm;a1,...,ar to
exhibit an extreme bias, and proves (still assuming LI) that when r ≥ 3, there are always unbiased
races involving only quadratic residues or only quadratic residues when deg m is large enough. The
author concludes by giving a few examples of races where LI is actually false.

This article cites [14, 215, 225, 232, 250, 257, 265, 273, 281, 284, 302, 315, 326, 334].

[351] Aoki, M. and Koyama, S.-y., Chebyshev’s bias against splitting and principal primes in global ﬁelds,
J. Number Theory 245 (2023), 233–262, MR4517481.

90 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

The authors show that ∑

p≤x
p≡3 (mod 4)
 1
p1/2 − ∑

p≤x
p≡1 (mod 4)
 1
p1/2 ∼ 1
2 log log x

under the Deep Riemann Hypothesis for Dirichlet L-functions, which is the assumption that for all
nonprincipal Dirichlet characters χ and all s with ℜ(s) = 1
2 ,

lim
x→∞

(
(log x)
m ∏

p≤x
 (
1 − χ(p)
ps
 )−1) = L(m)(s, χ)
eC0mm! ×
 {√
2, if χ2 = χ0 and s = 1
2 ,
1, otherwise,

where m denotes the order of vanishing of L(s, χ) at s = 1
2 . Further, they show parallel results for
the biases in number ﬁelds and their ﬁnite abelian extensions under the assumption of an analogous
Deep Riemann Hypothesis. The authors also provide numerical data to support their conditional
results. The authors note that the Deep Riemann Hypothesis for general L-functions is due to
Kurokawa.

This article cites [14, 71, 215, 217, 255, 257, 287, 289, 325, 334, 340, 346, 358, 359].

[352] Axler, C., New estimates for some integrals of functions deﬁned over primes, Funct. Approx. Com-
ment. Math. 68 (2023), no. 2, 207–229, MR4603776.

The author provides quantitative reﬁnements of several results proved by Johnston [357]. The author
proves that RH is equivalent to

− x
3/2

log x < ∫ x

2 ∆
π(t) dt < (
− 2
3 + λ0
) x
3/2

log x
when x is suﬃciently large, where λ0 ≈ 0.0461. Moreover,

C − D
log3 x < ∫ x

2
 ∆
π(t)
t2 dt < C + D
log3 x < 0

holds when x is suﬃciently large, where C ≈ −0.62759 and D = 0.0100757. Analogous results for ∆
θ

are also discussed.

This article cites [11, 14, 44, 49, 74, 170, 208, 312, 357].

[353] Fiorilli, D. and Martin, G., Disproving Hooley’s conjecture, J. Eur. Math. Soc. (JEMS) 25 (2023),
no. 12, 4791–4812, MR4662302.

Deﬁne G(x; q) = ∑(a,q)=1(
∆
θ(x; q, a)/φ(q)
)2. When q is ﬁxed, results of the form E(x, χ) =
Ω(log log log x) imply that G(x; q) ̸≪ x log q; such oscillation results were proved by Littlewood [14]
for certain characters, and extended by G. Davidoﬀ (unpublished) to all real nonprincipal charac-
ters. Hooley conjectured that G(x; q) ≪ x log q as soon as q tends to inﬁnity with x. In this article,
the authors disprove this conjecture. While the basic approach using Diophantine approximation
and the explicit formula is the same as in earlier results, the need to have estimates that are uniform
in q requires signiﬁcant technical attention.

This article cites [14, 132, 168, 183, 215, 281, 297, 317].

[354] Gao, P. and Zhao, L., Lower bounds for negative moments of ζ′(ρ), Mathematika 69 (2023), no. 4,
1081–1103, MR4627909.

Assuming RH and the simplicity of all zeros of ζ(s), the authors prove that
∑

0≤γ≤T
 1
|ζ′(ρ)|2k ≫ T (log T )
(k−1)2

for all real numbers k ≥ 0; the lower bound is of the expected order of magnitude when 0 < k < 3/2.
This result generalizes the work of Heap, Li, and Zhao [344] who gave the same bound for rational k.

This article cites [186, 196, 197, 243, 279, 344].

[355] Gorodetsky, O., Sums of two squares are strongly biased towards quadratic residues, Algebra Number
Theory 17 (2023), no. 3, 775–804, MR4578006.

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 91

Throughout, let q be a positive integer, and let a and b be distinct reduced residue classes (mod q)
with a ≡ b ≡ 1 (mod (4, q)). Let S denote the set of positive integers that can be written as a sum of
two squares. Assuming GRH for both L(s, χ) and L(s, χχ−4) for all Dirichlet characters modulo q,
the author gives a suﬃcient condition for the diﬀerence #
{n ≤ x : n ∈ S, n ≡ a (mod q)} > #
{n ≤
x : n ∈ S, n ≡ b (mod q)
} to have (natural) density 1. In particular, this is the case when a is
a quadratic residue and b is a quadratic nonresidue (mod q) and L(s, χ)L(s, χχ−4) ̸= 0 for some
χ (mod q) with χ(b) = −1.

The author also improves the work of Meng [329], related to a conjecture of Martin, by proving
results assuming only GRH. The author shows that ∑
n≤x ω(n)χ−4(n) < 0 on a set of natural
density 1, and more generally that if ∑χ (mod q), χ2=χ0 (χ(a) − χ(b))L( 1
2 , χ) > 0 then
∑

m≤n
m≡a (mod q)
 ω(m) < ∑

m≤n
m≡b (mod q)
 ω(m) and ∑

m≤n
m≡a (mod q)
 Ω(m) > ∑

m≤n
m≡b (mod q)
 Ω(m)

on a set of density 1.

This article cites [14, 71, 215, 217, 227, 242, 257, 267, 289, 290, 293, 295, 302, 303, 315, 325, 329,
332, 334–336, 342].

[356] Hu, D., Kaneko, I., Martin, S., and Schildkraut, C., On a Mertens-type conjecture for number ﬁelds,
2023, url: https://arxiv.org/abs/2109.06665.

Let µK(n) be the M¨obius function deﬁned over ideals of a number ﬁeld K, and deﬁne EMK (x) =
x
−1/2 ∑N (a)≤x µK(a). The authors formulate a “na¨ıve Mertens-type conjecture over K” as the
assertion −1 ≤ lim inf EMK (x) ≤ lim sup EMK (x) ≤ 1. With this formulation, the authors prove
that if K ̸= Q(
√
−3), Q(
√
5) is a quadratic extension of Q, then the na¨ıve Mertens-type conjecture
over K is false; they provide a generalization for extensions of Q of higher degree. Moreover, they
generalize Ng’s result [243] to abelian number ﬁelds K by showing, assuming both GRH for the
Dedekind zeta function ζK(s) and an estimate
∑

0≤γK ≤T
ζK (1/2+iγK )=0
 1
|ζ′
K (1/2 + iγK)|2 ≪α T 1+α

for some α < 2 − √
3, that EMK (x) possesses a limiting logarithmic distribution.

This article cites [4, 112, 121, 125, 181, 186, 215, 227, 243, 283, 287, 292, 295, 314].

[357] Johnston, D. R., On the average value of π(t) − li(t), Canad. Math. Bull. 66 (2023), no. 1, 185–195,
MR4552509.

The author shows that ∫ x
2 ∆
Π(t)/t2 dt < 0 for all x > 2, strengthening a result of Pintz [208], and
proves the same inequality with ∆
Π replaced by any of ∆
π, ∆
ψ, or ∆
θ. The author also shows that
RH is equivalent to ∫ x
2 ∆
π(t) dt < 0 for all x > 2, and proves the same statement for ∆
θ(t).

This article cites [8, 14, 74, 81, 170, 215, 224, 250, 283, 296, 300, 304, 306, 312, 360].

[358] Kaneko, I. and Koyama, S.-y., A new aspect of Chebyshev’s bias for elliptic curves over function
ﬁelds, Proc. Amer. Math. Soc. 151 (2023), no. 12, 5059–5068, MR4648908.

The authors prove an analogue of Chebyshev biases for non-constant elliptic curves E over function
ﬁelds K with positive characteristic. When v is a ﬁnite place of K, let qv be the cardinality of the
residue ﬁeld kv, and let Ev be the kv-reduction of E. Deﬁne

av(E) =
 



qv + 1 − #Ev(kv), if E has good reduction at v,
1, if E has split multiplicative reduction at v,
−1, if E has non-split multiplicative reduction at v,
0, if E has additive reduction at v.

They prove that ∑
qv ≤x av(E)/qv = ( 1
2 − rank(E)
) log log x + O(1). In particular, if rank(E) = 0
then there exists a bias towards av(E) being positive, while if rank(E) is positive then there exists
a bias towards av(E) being negative. The proof is based on the convergence of the Euler product
at the center, which follows from the Deep Riemann Hypothesis over function ﬁelds.

92 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

This article cites [14, 71, 215, 217, 255, 287, 302, 325, 346, 351, 359].

[359] Kaneko, I., Koyama, S.-y., and Kurokawa, N., Towards the Deep Riemann Hypothesis for GLn, 2023,
url: https://arxiv.org/abs/2206.02612.

This article is a survey on the Deep Riemann Hypothesis and its applications. The authors state
a version of the conjecture for Artin L-functions, and prove that if the global ﬁeld over which the
Artin L-function is deﬁned has positive characteristic, then the reformulated conjecture holds. A
similar conjecture and result are introduced for nontrivial cuspidal automorphic representations
deﬁned over a global number ﬁeld K.

This article cites [14, 71, 215, 217, 255, 325, 346, 351, 358].

[360] Martin, G., Mossinghoﬀ, M., and Trudgian, T., Fake mu’s, Proc. Amer. Math. Soc. 151 (2023),
no. 8, 3229–3244, MR4591762.

The authors investigate comparative number theoretic results for a family of arithmetic functions
called “fake µ’s”, which are multiplicative functions f (n) such that f (pr) ∈ {−1, 0, 1} depends
only on r and not p; fake µ’s include many commonly studied functions such as µ(n), µ2(n),
(−1)
ω(n), and µk(n). Generalizing a technique of Tanaka [157], the authors show that if f (n) is
a fake µ with f (p) = −1 and f (p2) = 1 for all primes p, then its summatory function F (x) satisﬁes
F (x) − b√
x = Ω±(
√x), where b is twice the residue at 1
2 of the Dirichlet series corresponding
to f (n). The authors also determine the minimum and maximum of the above constant b and show
that both extreme values can be achieved by particular fake µ’s.

This article cites [4, 20, 35, 51, 59, 156, 157, 181, 186, 191, 215, 225, 243, 256, 280, 283, 310, 311,
314, 319, 324, 330, 333, 337, 338].

[361] Bailleul, A., Devin, L., Keliher, D., and Li, W., Exceptional biases in counting primes over function
ﬁelds, J. Lond. Math. Soc. (2) 109 (2024), no. 3, Paper No. e12876, 32, MR4709829.

The authors explore the likelihood of LI failing for the zeta functions of hyperelliptic curves over
ﬁnite ﬁelds, and discuss the implications to the distributions of irreducible polynomials over ﬁnite
ﬁelds that are square or nonsquare residues modulo a ﬁxed polynomial f . Let Hd(Fq) be the family
of monic squarefree polynomials of degree d deﬁned over Fq. One can associate each f ∈ Hd(Fq) to
the hyperelliptic curve Cf : y2 = f (x) with genus g = ⌊ 1
2 (d − 1)⌋. The authors prove that among
the zeta functions of all the curves Cf associated to f ∈ Hd(Fq), the density of those that fail LI is
≪ q−1/(4g2+2g+4)(log q)
1−δ, where the implicit constant depends on g and the characteristic p of Fq,
and δ ≤ 1 is a constant depending on g that satisﬁes δ → 1
8g as g → ∞. This result extends work of
Kowalski [259] to hyperelliptic curves associated with the full family of squarefree polynomials. The
authors also show that if p ≥ 5, then the corresponding upper bound can be signiﬁcantly improved
to ≪ p/q when g = 1, and ≪p q−1/12 log q when g = 2.

The authors then study the function

Eπ(n; f, R, N ) = n
qn/2 ∑

deg(h)=n
h irreducible
 χf (h),

where f ∈ Hd(Fq) and χf is the unique primitive quadratic character modulo f . Note that
Eπ(n; f, R, N ) measures the bias of the race among degree-n irreducible polynomials in Fq[x] that
are square residues modulo f versus nonsquare residues modulo f . If LI holds for the zeta function
of Cf , the authors show that Eπ(n; f, R, N ) is biased toward negative values and has inﬁnitely many
sign changes. The authors then study how likely Eπ(n; f, R, N ) behaves diﬀerently by introducing
three types of exceptional bias. Roughly speaking, they say Eπ(n; f, R, N ) has complete bias if
Eπ(n; f, R, N ) < 0 for almost all n, has lower term bias if Eπ(n; f, R, N ) is very close to 0 for a
positive proportion of n, and has a reversed bias if Eπ(n; f, R, N ) > 0 for more than half of the n. In
each of the three types of exceptional bias, they give an upper bound on the density of f ∈ Hd(Fq)
such that Eπ(n; f, R, N ) exhibits the bias, which signiﬁcantly improves the above mentioned upper
bound on the density where LI fails for Cf ; they also construct a family of examples exhibiting each
bias.

This article cites [215, 232, 233, 237, 250, 257, 259, 273, 281, 282, 302, 328, 334, 336, 341, 342, 350].

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 93

[362] Bui, H. M., Florea, A., and Milinovich, M. B., Negative discrete moments of the derivative of the
Riemann zeta-function, Bull. Lond. Math. Soc. 56 (2024), no. 8, 2680–2703, MR4795352.

Assuming RH, the authors establish the upper bound

∑

γ∈F
T <γ≤2T
 1
|ζ′(ρ)|2k ≪δ,ε
 {T 1+δ, if 2k(1 + ε) ≤ 1,
T k+1/2+δ, if 2k(1 + ε) > 1

for any positive numbers δ and ε, where

F = {γ : ζ( 1
2 + iγ) = 0, |γ − γ′| ≫ 1/ log T for any γ′ ̸= γ such that ζ( 1
2 + iγ′) = 0}
.

This upper bound is stronger than the corresponding upper bound for the sum over all ordinates
γ ∈ (T, 2T ] that would be implied by the weak Mertens conjecture.

This article cites [186].

[363] Fiorilli, D. and Jouve, F., Distribution of Frobenius elements in families of Galois extensions, J.
Inst. Math. Jussieu 23 (2024), no. 3, 1169–1258, MR4742716.

For a class function t on G = Gal(L/K), the authors consider the Frobenius counting function

π(x; L/K, t) = ∑

p⊂OK
Np≤x
 t(Frobp)

and study the “normalized Chebotarev error term”

E(x; L/K, t) = x
−Θ log x · (π(x; L/K, t) − ̂t(1)Li(x)),

where Θ is the supremum of real parts of zeros of certain Artin L-functions of L/Q relevant to t.
They show that this error admits a limiting logarithmic distribution, and they compute its mean,
along with unconditional and conditional bounds on its variance. They also prove improved bounds
on the error term of the Chebotarev density theorem assuming GRH and Artin’s conjecture. They
further consider the logarithmic densities δ(L/K; t) of the set of values of x for which E(x; L/K, t)
is positive, giving criteria for when the density is close to 1 or 1
2 , indicating a bias or lack thereof.
Finally, these ideas are applied to the class function tC1,C2 = |G|
|C1| 1C1 − |G|
|C2| 1C2 for special families
of extensions (Sn, dihedral, radical, abelian, and Hilbert class ﬁelds of quadratic extensions), giving
asymptotic bounds for the densities in each case.

This article cites [14, 34, 71–73, 149, 215, 217, 218, 227, 228, 250, 255, 257, 260, 267, 273, 277, 281,
287, 289, 290, 302, 303, 305, 315, 325, 328, 334, 336, 337] and this bibliography.

[364] Grze´skowiak, M., Kaczorowski, J., Pa´nkowski,  L., and Radziejewski, M., On the sign changes of
ψ(x) − x, 2024, url: https://arxiv.org/abs/2408.10399.

The authors show that
 lim inf
T →∞ W ψ(T )
log T ≥ γ1
π + 1
60 ,

improving the previous best bound given by Morrill, Platt, and Trudgian [348]; the result is achieved
by following the method of Kaczorowski [207] with some theoretical and computational improve-
ments.

This article cites [29, 30, 97, 109, 170, 180, 207, 221, 348].

[365] Hamieh, A., Kadiri, H., Martin, G., and Ng, N., Comparative prime number theory problem list,
2024, url: https://arxiv.org/abs/2407.03530.

This list of problems was collected from participants at the Comparative Prime Number Theory
Symposium held at the University of British Columbia (Vancouver, Canada) from June 17–21, 2024.

This problem list cites [6, 56, 74, 165, 180, 207, 215, 225, 227, 235, 257, 279, 281, 284, 290, 296, 299,
300, 312, 314, 325, 334, 338, 343, 344, 348, 351, 354, 357, 362, 363] and this bibliography.

[366] Hayani, M., On the inﬂuence of the Galois group structure on the Chebyshev bias in number ﬁelds,
2024, url: https://arxiv.org/abs/2404.06804.

94 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

Let k be a number ﬁeld and let G be a ﬁnite group, considered as a subgroup of its group of
permutations S(G). Let L/k be a Galois extension with Galois group S(G), and let K = LG be
the ﬁxed ﬁeld of G. Then, for all a, b ∈ G of the same order, with respective conjugacy classes Ca
and Cb, the author shows that either π(x; L/K; Ca)/#Ca = π(x; L/K; Cb)/#Cb identically, or
one of π(x; L/K; Ca)/#Ca > π(x; L/K; Cb)/#Cb and π(x; L/K; Ca)/#Ca < π(x; L/K; Cb)/#Cb
holds for all suﬃciently large x. The author shows that the ﬁrst case (no bias) holds for G = Q8
being the 8-element quaternion group and a, b two elements of the same order, and that the second
case (extreme bias for a) holds for G = Q8 × Z/4Z with a = (1, 2) and b = (−1, 0). Moreover,
in the case k = Q when there is an extreme bias, assuming GRH for ζL(s) the author gives a
formula, in terms of invariants of the ﬁeld extension and a, b for the threshold A that the inequality
π(x; L/K; Ca)/#Ca > π(x; L/K; Cb)/#Cb holds for all x ≥ A. The article contains several concrete
examples on how these biases are aﬀected by the structure of ﬁeld extensions.

This article cites [1, 215, 217, 227, 325, 334, 342, 363].

[367] Sheth, A., Euler products at the centre and applications to Chebyshev’s bias, 2024, url: https://arxiv.org/abs/2405.0

Let π be an irreducible cuspidal automorphic representation of GLn(AQ) (where AQ denotes the
adele ring of Q) with associated L-function

L(s, π) = ∏

p L(s, πp) = ∏

p
 n∏

j=1
(
1 − αj,pp−s)−1,

where L(s, πp) are local factors deﬁned by polynomials characterized by {αj,p}, the eigenvalues
attached to the semisimple conjugacy class associated to πp in GLn(C). The Ramanujan–Petersson
Conjecture asserts that |α1,p| = · · · = |αn,p| = 1 for any p at which πp is unramiﬁed.

In this article, assuming analytic continuation and GRH for L(s, π) and the Ramanujan–Petersson
Conjecture, the author shows that for x outside a set of ﬁnite logarithmic measure,

(log x)
m ∏

p≤x
 n∏

j=1
(
1 − αj,pp−1/2)−1 ∼ 2ν(π)/2

emγm! L(m)( 1
2 , π)

for a particular integer ν(π), where m is the order of vanishing of L(s, π) at s = 1
2 . This result
conditionally conﬁrms the Deep Riemann Hypothesis for GLn formulated in [359]. As a result, the
author shows that under the same assumptions, there is a constant cπ such that for x outside a set
of ﬁnite logarithmic measure,
∑

p≤x
 α1,p + · · · + αn,p
√
p = ( R(π)
2 − m) log log x + cπ + o(1)

for a particular integer R(π).

This article cites [71, 147, 150, 215, 217, 255, 260, 325, 346, 351, 358].

Alphabetic bibliography

[A1] Akbary, A., Ng, N., and Shahabi, M., Limiting distributions of the classical error terms of prime
number theory, Q. J. Math. 65 (2014), no. 3, 743–780, MR3261965. Numerical entry: [287]
[A2] Alkan, E., Biased behavior of weighted Mertens sums, Int. J. Number Theory 16 (2020), no. 3,
547–577, MR4079395. Numerical entry: [324]
[A3] Alkan, E., Variations on criteria of P´olya and Tur´an for the Riemann hypothesis, J. Number Theory
225 (2021), 90–124, MR4231545. Numerical entry: [333]
[A4] Anderson, R. J. and Stark, H. M., Oscillation theorems, in: Analytic number theory (Philadelphia,
Pa., 1980), vol. 899, Lecture Notes in Math. Springer, Berlin-New York, 1981, 79–106, MR654520.
Numerical entry: [158]
[A5] Aoki, M. and Koyama, S.-y., Chebyshev’s bias against splitting and principal primes in global ﬁelds,
J. Number Theory 245 (2023), 233–262, MR4517481. Numerical entry: [351]
[A6] Axler, C., New estimates for some integrals of functions deﬁned over primes, Funct. Approx. Com-
ment. Math. 68 (2023), no. 2, 207–229, MR4603776. Numerical entry: [352]
[A7] Aymone, M., A note on prime number races and zero free regions for L functions, Int. J. Number
Theory 18 (2022), no. 1, 1–8, MR4369787. Numerical entry: [340]

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 95

[A8] Bailleul, A., Chebyshev’s bias in dihedral and generalized quaternion Galois groups, Algebra Number
Theory 15 (2021), no. 4, 999–1041, MR4265352. Numerical entry: [334]
[A9] Bailleul, A., Explicit Kronecker–Weyl theorems and applications to prime number races, Res. Num-
ber Theory 8 (2022), no. 3, Paper No. 43, 34, MR4447414. Numerical entry: [341]
[A10] Bailleul, A., Devin, L., Keliher, D., and Li, W., Exceptional biases in counting primes over function
ﬁelds, J. Lond. Math. Soc. (2) 109 (2024), no. 3, Paper No. e12876, 32, MR4709829. Numerical
entry: [361]
[A11] Balanzario, E. P. and Hern´andez, S., On the number of large oscillations of some arithmetical power
series, Arch. Math. (Basel) 81 (2003), no. 3, 285–290, MR2013259. Numerical entry: [236]
[A12] Balasubramanian, R., Ramachandra, K., and Subbarao, M. V., On the error function in the asymp-
totic formula for the counting function of k-full numbers, Acta Arith. 50 (1988), no. 2, 107–118,
MR945261. Numerical entry: [191]
[A13] Bartz, K. M., On some complex explicit formulae connected with the M¨obius function. I, II, Acta
Arith. 57 (1991), no. 4, 283–293, 295–305, MR1109990. Numerical entry: [203]
[A14] Bateman, P. T., Brown, J. W., Hall, R. S., Kloss, K. E., and Stemmler, R. M., Linear relations con-
necting the imaginary parts of the zeros of the zeta function (1971), 11–19, MR0330069. Numerical
entry: [112]
[A15] Bateman, P. T. and Grosswald, E., On a theorem of Erd¨os and Szekeres, Illinois J. Math. 2 (1958),
88–98, MR95804. Numerical entry: [50]
[A16] Bays, C., Ford, K., Hudson, R. H., and Rubinstein, M., Zeros of Dirichlet L-functions near the
real axis and Chebyshev’s bias, J. Number Theory 87 (2001), no. 1, 54–76, MR1816036. Numerical
entry: [229]
[A17] Bays, C. and Hudson, R. H., The segmented sieve of Eratosthenes and primes in arithmetic progres-
sions to 1012, Nordisk Tidskr. Informationsbehandling (BIT) 17 (1977), no. 2, 121–127, MR0447090.
Numerical entry: [131]
[A18] Bays, C. and Hudson, R. H., Details of the ﬁrst region of integers x with π3,2(x) < π3,1(x), Math.
Comp. 32 (1978), no. 142, 571–576, MR0476616. Numerical entry: [137]
[A19] Bays, C. and Hudson, R. H., Numerical and graphical description of all axis crossing regions for
the moduli 4 and 8 which occur before 1012, Internat. J. Math. Math. Sci. 2 (1979), no. 1, 111–119,
MR529694. Numerical entry: [141]
[A20] Bays, C. and Hudson, R. H., Zeroes of Dirichlet L-functions and irregularities in the distribution of
primes, Math. Comp. 69 (2000), no. 230, 861–866, MR1651741. Numerical entry: [223]
[A21] Bays, C. and Hudson, R. H., On the ﬂuctuations of Littlewood for primes of the form 4n ± 1, Math.
Comp. 32 (1978), no. 141, 281–286, MR0476615. Numerical entry: [138]
[A22] Bays, C. and Hudson, R. H., The appearance of tens of billions of integers x with π24,13(x) < π24,1(x)
in the vicinity of 1012, J. Reine Angew. Math. 299/300 (1978), 234–237, MR0472726. Numerical
entry: [139]
[A23] Bays, C. and Hudson, R. H., The cyclic behavior of primes in the arithmetic progressions modulo
11, J. Reine Angew. Math. 339 (1983), 215–220, MR686708. Numerical entry: [165]
[A24] Bays, C. and Hudson, R. H., A new bound for the smallest x with π(x) > li(x), Math. Comp. 69
(2000), no. 231, 1285–1296, MR1752093. Numerical entry: [224]
[A25] Bentz, H.-J., Discrepancies in the distribution of prime numbers, J. Number Theory 15 (1982),
no. 2, 252–274, MR675189. Numerical entry: [161]
[A26] Bentz, H.-J. and Pintz, J., Quadratic residues and the distribution of prime numbers, Monatsh.
Math. 90 (1980), no. 2, 91–100, MR595317. Numerical entry: [144]

[A27] Bentz, H.-J. and Pintz, J., ¨Uber das Tschebyschef-Problem, German, Resultate Math. 5 (1982),
no. 1, 1–5, MR662791. Numerical entry: [162]

[A28] Bentz, H.-J. and Pintz, J., ¨Uber eine Verallgemeinerung des Tschebyschef-Problems, German, Math.
Z. 174 (1980), no. 1, 35–41, MR591612. Numerical entry: [145]

[A29] Besenfelder, H.-J., ¨Uber eine Vermutung von Tschebyschef. I, German, J. Reine Angew. Math.
307/308 (1979), 411–417, MR534235. Numerical entry: [142]

96 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

[A30] Besenfelder, H.-J., ¨Uber eine Vermutung von Tschebyschef. II, German, J. Reine Angew. Math. 313
(1980), 52–58, MR552462. Numerical entry: [146]
[A31] Best, D. G. and Trudgian, T. S., Linear relations of zeroes of the zeta-function, Math. Comp. 84
(2015), no. 294, 2047–2058, MR3335903. Numerical entry: [295]
[A32] Bhowmik, G., Ramar´e, O., and Schlage–Puchta, J.-C., Tauberian oscillation theorems and the dis-
tribution of Goldbach numbers, English, with English and French summaries, J. Th´eor. Nombres
Bordeaux 28 (2016), no. 2, 291–299, MR3509711. Numerical entry: [301]
[A33] Borwein, P., Ferguson, R., and Mossinghoﬀ, M. J., Sign changes in sums of the Liouville function,
Math. Comp. 77 (2008), no. 263, 1681–1694, MR2398787. Numerical entry: [256]
[A34] Brent, R. P. and Lune, J. van de, A note on P´olya’s observation concerning Liouville’s function, in:
Herman J. J. te Riele Liber Amicorum, CWI, 2011, pp. 92–97, url: https://arxiv.org/abs/1112.4911.
Numerical entry: [272]
[A35] Brent, R. P., Irregularities in the distribution of primes and twin primes, Math. Comp. 29 (1975),
Collection of articles dedicated to Derrick Henry Lehmer on the occasion of his seventieth birthday,
43–56, MR0369287. Numerical entry: [122]
[A36] Bui, H. M., Florea, A., and Milinovich, M. B., Negative discrete moments of the derivative of the
Riemann zeta-function, Bull. Lond. Math. Soc. 56 (2024), no. 8, 2680–2703, MR4795352. Numerical
entry: [362]
[A37] B¨uthe, J., On the ﬁrst sign change in Mertens’ theorem, Acta Arith. 171 (2015), no. 2, 183–195,
MR3414306. Numerical entry: [296]
[A38] B¨uthe, J., An analytic method for bounding ψ(x), Math. Comp. 87 (2018), no. 312, 1991–2009,
MR3787399. Numerical entry: [312]
[A39] Cha, B. and Im, B.-H., Chebyshev’s bias in Galois extensions of global function ﬁelds, J. Number
Theory 131 (2011), no. 10, 1875–1886, MR2811555. Numerical entry: [273]
[A40] Cha, B., Fiorilli, D., and Jouve, F., Prime number races for elliptic curves over function ﬁelds, Ann.
Sci. ´Ec. Norm. Sup´er. (4) 49 (2016), no. 5, 1239–1277, MR3581815. Numerical entry: [302]
[A41] Cha, B., Chebyshev’s bias in function ﬁelds, Compos. Math. 144 (2008), no. 6, 1351–1374, MR2474313.
Numerical entry: [257]
[A42] Cha, B., The summatory function of the M¨obius function in function ﬁelds, Acta Arith. 179 (2017),
no. 4, 375–395, MR3684399. Numerical entry: [308]
[A43] Cha, B. and Kim, S., Biases in the prime number race of function ﬁelds, J. Number Theory 130
(2010), no. 4, 1048–1055, MR2600420. Numerical entry: [265]
[A44] Chao, K. F. and Plymen, R., A new bound for the smallest x with π(x) > li(x), Int. J. Number
Theory 6 (2010), no. 3, 681–690, MR2652902. Numerical entry: [266]
[A45] Chaubey, S., Lanius, M., and Zaharescu, A., Irrational factor races, Proc. Indian Acad. Sci. Math.
Sci. 124 (2014), no. 4, 471–479, MR3306734. Numerical entry: [288]
[A46] Chebyshev, P., Lettre de M. le professeur Tch´ebychev a M. Fuss, sur un nouveau th´eor`eme relatif
aux nombres premiers contenus dans la formes 4n + 1 et 4n + 3, French, Bull. de la Classe phys.
math. de l’Acad. Imp. des Sciences St. Petersburg 11 (1853), 208. Numerical entry: [1]
[A47] Chen, W. W. L., On the error term of the prime number theorem and the diﬀerence between the
number of primes in the residue classes modulo 4, J. London Math. Soc. (2) 23 (1981), no. 1, 24–40,
MR602236. Numerical entry: [159]
[A48] Cohen, A. M. and Mayhew, M. J. E., On the diﬀerence π(x) − li(x), Proc. London Math. Soc. (3)
18 (1968), 691–713, MR0233781. Numerical entry: [104]
[A49] Cram´er, H., Ein Mittelwertsatz in der Primzahltheorie, German, Math. Z. 12 (1922), no. 1, 147–153,
MR1544509. Numerical entry: [21]
[A50] Dancs, S. and Tur´an, P., Investigations in the powersum theory. I, Ann. Univ. Sci. Budapest. E¨otv¨os
Sect. Math. 16 (1973), 47–52 (1974), MR0352012. Numerical entry: [120]
[A51] Del´eglise, M., Dusart, P., and Roblot, X.-F., Counting primes in residue classes, Math. Comp. 73
(2004), no. 247, 1565–1575, MR2047102. Numerical entry: [240]
[A52] Devin, L., Chebyshev’s bias for analytic L-functions, Math. Proc. Cambridge Philos. Soc. 169 (2020),
no. 1, 103–140, MR4120786. Numerical entry: [325]

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 97

[A53] Devin, L., Limiting properties of the distribution of primes in an arbitrarily large number of residue
classes, Canad. Math. Bull. 63 (2020), no. 4, 837–849, MR4176773. Numerical entry: [326]
[A54] Devin, L., Discrepancies in the distribution of Gaussian primes, 2021, url: https://arxiv.org/abs/2105.02492.
Numerical entry: [335]
[A55] Devin, L. and Meng, X., Chebyshev’s bias for products of irreducible polynomials, Adv. Math. 392
(2021), Paper No. 108040, 45, MR4316675. Numerical entry: [336]
[A56] Diamond, H. G., Two oscillation theorems (1972), 113–118. Lecture Notes in Math., Vol. 251,
MR0332684. Numerical entry: [116]
[A57] Diamond, H. G. and Pintz, J., Oscillation of Mertens’ product formula, J. Th´eor. Nombres Bordeaux
21 (2009), no. 3, 523–533, MR2605532. Numerical entry: [261]
[A58] Diamond, H. G., Changes of sign of π(x) − li(x), Enseignement Math. (2) 21 (1975), no. 1, 1–14,
MR0376566. Numerical entry: [123]
[A59] Dummit, D., Granville, A., and Kisilevsky, B., Big biases amongst products of two primes, Mathe-
matika 62 (2016), no. 2, 502–507, MR3521338. Numerical entry: [303]
[A60] Ellison, W. and Ellison, F., Prime numbers, A Wiley-Interscience Publication, John Wiley & Sons,
Inc., New York; Hermann, Paris, 1985, pp. xii+417, MR814687. Numerical entry: [178]
[A61] Ellison, W. J., Les nombres premiers, French, En collaboration avec Michel Mend`es France; Publi-
cations de l’Institut de Math´ematique de l’Universit´e de Nancago, No. IX; Actualit´es Scientiﬁques
et Industrielles, No. 1366, Hermann, Paris, 1975, pp. xiv+442, MR0417077. Numerical entry: [124]
[A62] Evelyn, C. J. A. and Linfoot, E. H., On a problem in the additive theory of numbers, Ann. of Math.
(2) 32 (1931), no. 2, 261–270, MR1502996. Numerical entry: [24]
[A63] Fawaz, A. Y., The explicit formula for L0(x), Proc. London Math. Soc. (3) 1 (1951), 86–103,
MR43841. Numerical entry: [41]
[A64] Fawaz, A. Y., On an unsolved problem in the analytic theory of numbers, Quart. J. Math. Oxford
Ser. (2) 3 (1952), 282–295, MR51857. Numerical entry: [43]
[A65] Feuerverger, A. and Martin, G., Biases in the Shanks-R´enyi prime number race, Experiment. Math.
9 (2000), no. 4, 535–570, MR1806291. Numerical entry: [225]
[A66] Fiorilli, D., Irr´egularit´es dans la distribution des nombres premiers et des suites plus g´en´erales dans
les progressions arithm´etiques, French, Thesis (Ph.D.)–Universit´e de Montr´eal, ProQuest LLC, Ann
Arbor, MI, 2011, 261 pp., MR3103752. Numerical entry: [274]
[A67] Fiorilli, D., Elliptic curves of unbounded rank and Chebyshev’s bias, Int. Math. Res. Not. IMRN
(2014), no. 18, 4997–5024, MR3264673. Numerical entry: [289]
[A68] Fiorilli, D., Highly biased prime number races, Algebra Number Theory 8 (2014), no. 7, 1733–1767,
MR3272280. Numerical entry: [290]
[A69] Fiorilli, D., The distribution of the variance of primes in arithmetic progressions, Int. Math. Res.
Not. IMRN (2015), no. 12, 4421–4448, MR3356760. Numerical entry: [297]
[A70] Fiorilli, D. and Martin, G., Inequities in the Shanks-R´enyi prime number race: an asymptotic formula
for the densities, J. Reine Angew. Math. 676 (2013), 121–212, MR3028758. Numerical entry: [281]

[A71] Fiorilli, D. and Jouve, F., Unconditional Chebyshev biases in number ﬁelds, J. ´Ec. polytech. Math.
9 (2022), 671–679, MR4400872. Numerical entry: [342]
[A72] Fiorilli, D. and Jouve, F., Distribution of Frobenius elements in families of Galois extensions, J.
Inst. Math. Jussieu 23 (2024), no. 3, 1169–1258, MR4742716. Numerical entry: [363]
[A73] Fiorilli, D. and Martin, G., Disproving Hooley’s conjecture, J. Eur. Math. Soc. (JEMS) 25 (2023),
no. 12, 4791–4812, MR4662302. Numerical entry: [353]
[A74] Ford, K. and Konyagin, S., Chebyshev’s conjecture and the prime number race, in: IV International
Conference “Modern Problems of Number Theory and its Applications”: Current Problems, Part
II (Russian) (Tula, 2001), Mosk. Gos. Univ. im. Lomonosova, Mekh.-Mat. Fak., Moscow, 2002,
pp. 67–91, MR1985941. Numerical entry: [232]
[A75] Ford, K. and Konyagin, S., The prime number race and zeros of L-functions oﬀ the critical line,
Duke Math. J. 113 (2002), no. 2, 313–330, MR1909220. Numerical entry: [233]
[A76] Ford, K. and Konyagin, S., The prime number race and zeros of L-functions oﬀ the critical line. II,
Bonner Math. Schriften 360 (2003), 40, MR2075622. Numerical entry: [237]

98 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

[A77] Ford, K., Lamzouri, Y., and Konyagin, S., The prime number race and zeros of Dirichlet L-functions
oﬀ the critical line: Part III, Q. J. Math. 64 (2013), no. 4, 1091–1098, MR3151605. Numerical
entry: [282]
[A78] Ford, K. and Sneed, J., Chebyshev’s bias for products of two primes, Experiment. Math. 19 (2010),
no. 4, 385–398, MR2778652. Numerical entry: [267]
[A79] Ford, K., Harper, A. J., and Lamzouri, Y., Extreme biases in prime number races with many con-
testants, Math. Ann. 374 (2019), no. 1-2, 517–551, MR3961320. Numerical entry: [318]
[A80] Ford, K. and Hudson, R. H., Sign changes in πq,a(x) − πq,b(x), Acta Arith. 100 (2001), no. 4, 297–
314, MR1862054. Numerical entry: [230]
[A81] Fujii, A., Some generalizations of Chebyshev’s conjecture, Proc. Japan Acad. Ser. A Math. Sci. 64
(1988), no. 7, 260–263, MR974088. Numerical entry: [192]
[A82] Fujii, A., An additive problem of prime numbers. III, Proc. Japan Acad. Ser. A Math. Sci. 67 (1991),
no. 8, 278–283, MR1137928. Numerical entry: [204]
[A83] Gallagher, P. X., Some consequences of the Riemann hypothesis, Acta Arith. 37 (1980), 339–343,
MR598886. Numerical entry: [147]
[A84] Gao, P. and Zhao, L., Lower bounds for negative moments of ζ′(ρ), Mathematika 69 (2023), no. 4,
1081–1103, MR4627909. Numerical entry: [354]
[A85] Gonek, S., The second moment of the reciprocal of the Riemann zeta function and its derivative,
1999, url: https://www.slmath.org/workshops/101/schedules/25626. Numerical entry: [222]
[A86] Gonek, S. M., On negative moments of the Riemann zeta-function, Mathematika 36 (1989), no. 1,
71–88, MR1014202. Numerical entry: [196]
[A87] Good, I. J. and Churchhouse, R. F., The Riemann hypothesis and pseudorandom features of the
M¨obius sequence, Math. Comp. 22 (1968), 857–861, MR240062. Numerical entry: [105]
[A88] Gorodetsky, O., Sums of two squares are strongly biased towards quadratic residues, Algebra Number
Theory 17 (2023), no. 3, 775–804, MR4578006. Numerical entry: [355]
[A89] Granville, A. and Martin, G., Prime number races, Amer. Math. Monthly 113 (2006), no. 1, 1–33,
MR2202918. Numerical entry: [250]
[A90] Grosswald, E., On some generalizations of theorems by Landau and P´olya, Israel J. Math. 3 (1965),
211–220, MR0198145. Numerical entry: [89]
[A91] Grosswald, E., Oscillation theorems of arithmetical functions, Trans. Amer. Math. Soc. 126 (1967),
1–28, MR0202685. Numerical entry: [99]
[A92] Grosswald, E., Oscillation theorems, in: The theory of arithmetic functions (Proc. Conf., Western
Michigan Univ., Kalamazoo, Mich., 1971), Lecture Notes in Math., Vol. 251, Springer, Berlin, 1972,
141–168, MR0332685. Numerical entry: [117]
[A93] Grze´skowiak, M., Kaczorowski, J., Pa´nkowski,  L., and Radziejewski, M., On the sign changes of
ψ(x) − x, 2024, url: https://arxiv.org/abs/2408.10399. Numerical entry: [364]
[A94] Gupta, H., On a table of values of L(n), Proc. Indian Acad. Sci., Sect. A. 12 (1940), 407–409,
MR0003644. Numerical entry: [33]
[A95] Hamieh, A., Kadiri, H., Martin, G., and Ng, N., Comparative prime number theory problem list,
2024, url: https://arxiv.org/abs/2407.03530. Numerical entry: [365]
[A96] Hardy, G. H., On Dirichlet’s divisor problem, Proc. London Math. Soc. (2) 15 (1916), 1–25,
MR1576550. Numerical entry: [16]
[A97] Hardy, G. H. and Littlewood, J. E., On an assertion of Tchebychef, Proc. London Math. Soc. (2)
14 (1915), xv–xvi. Numerical entry: [15]
[A98] Hardy, G. H. and Littlewood, J. E., Contributions to the theory of the Riemann zeta-function and the
theory of the distribution of primes, Acta Math. 41 (1916), no. 1, 119–196, MR1555148. Numerical
entry: [17]
[A99] Harper, A. J. and Lamzouri, Y., Orderings of weakly correlated random variables, and prime num-
ber races with many contestants, Probab. Theory Related Fields 170 (2018), no. 3-4, 961–1010,
MR3773805. Numerical entry: [313]
[A100] Haselgrove, C. B., A disproof of a conjecture of P´olya, Mathematika 5 (1958), 141–145, MR0104638.
Numerical entry: [51]

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 99

[A101] Hathi, S. and Lee, E. S., Mertens’ third theorem for number ﬁelds: a new proof, Cram´er’s inequality,
oscillations, and bias, 2022, url: https://arxiv.org/abs/2112.02166. Numerical entry: [343]
[A102] Hayani, M., On the inﬂuence of the Galois group structure on the Chebyshev bias in number ﬁelds,
2024, url: https://arxiv.org/abs/2404.06804. Numerical entry: [366]
[A103] Heap, W., Li, J., and Zhao, J., Lower bounds for discrete negative moments of the Riemann zeta
function, Algebra Number Theory 16 (2022), no. 7, 1589–1625, MR4496076. Numerical entry: [344]
[A104] Heath-Brown, D. R., The distribution and moments of the error term in the Dirichlet divisor prob-
lem, Acta Arith. 60 (1992), no. 4, 389–415, MR1159354. Numerical entry: [209]
[A105] Hejhal, D. A., On the distribution of log |ζ′( 1
2 + it)|, in: Number theory, trace formulas and dis-
crete groups (Oslo, 1987), Academic Press, Boston, MA, 1989, pp. 343–370, MR993326. Numerical
entry: [197]
[A106] Hooley, C., On the Barban-Davenport-Halberstam theorem. VII, J. London Math. Soc. (2) 16 (1977),
no. 1, 1–8, MR0506080. Numerical entry: [132]
[A107] Hough, P., A lower bound for biases amongst products of two primes, Res. Number Theory 3 (2017),
Art. 19, 11, MR3692499. Numerical entry: [309]
[A108] Hu, D., Kaneko, I., Martin, S., and Schildkraut, C., On a Mertens-type conjecture for number ﬁelds,
2023, url: https://arxiv.org/abs/2109.06665. Numerical entry: [356]
[A109] Hudson, R. H., A common combinatorial principle underlies Riemann’s formula, the Chebyshev
phenomenon, and other subtle eﬀects in comparative prime number theory. I, J. Reine Angew.
Math. 313 (1980), 133–150, MR552467. Numerical entry: [148]
[A110] Hudson, R. H., Averaging eﬀects on irregularities in the distribution of primes in arithmetic pro-
gressions, Math. Comp. 44 (1985), no. 170, 561–571, MR777286. Numerical entry: [179]
[A111] Hudson, R. H. and Bays, C., The mean behavior of primes in arithmetic progressions, J. Reine
Angew. Math. 296 (1977), 80–99, MR0460261. Numerical entry: [133]
[A112] Humphries, P., The distribution of weighted sums of the Liouville function and P´olya’s conjecture,
J. Number Theory 133 (2013), no. 2, 545–582, MR2994374. Numerical entry: [283]
[A113] Humphries, P., On the Mertens conjecture for elliptic curves over ﬁnite ﬁelds, Bull. Aust. Math.
Soc. 89 (2014), no. 1, 19–32, MR3163001. Numerical entry: [291]
[A114] Humphries, P., On the Mertens conjecture for function ﬁelds, Int. J. Number Theory 10 (2014),
no. 2, 341–361, MR3189983. Numerical entry: [292]
[A115] Humphries, P., Shekatkar, S. M., and Wong, T. A., Biases in prime factorizations and Liouville func-
tions for arithmetic progressions, J. Th´eor. Nombres Bordeaux 31 (2019), no. 1, 1–25, MR3996180.
Numerical entry: [319]
[A116] Hurst, G., Computations of the Mertens function and improved bounds on the Mertens conjecture,
Math. Comp. 87 (2018), no. 310, 1013–1028, MR3739227. Numerical entry: [314]
[A117] Ingham, A. E., The distribution of prime numbers, Cambridge Tracts in Mathematics and Mathe-
matical Physics. 30. London: Cambridge University Press, 1932, 114 pp.. Numerical entry: [26]
[A118] Ingham, A. E., A note on the distribution of primes, Acta Arith. 1 (1936), 201–211. Numerical
entry: [30]
[A119] Ingham, A. E., On two conjectures in the theory of numbers, Amer. J. Math. 64 (1942), 313–319,
MR0006202. Numerical entry: [35]
[A120] Ingham, A. E., The distribution of prime numbers, Cambridge Tracts in Mathematics and Mathe-
matical Physics, No. 30, Stechert-Hafner, Inc., New York, 1964, pp. v+114, MR0184920. Numerical
entry: [81]
[A121] Jessen, B. and Wintner, A., Distribution functions and the Riemann zeta function, Trans. Amer.
Math. Soc. 38 (1935), no. 1, 48–88, MR1501802. Numerical entry: [28]
[A122] Johnston, D. R., On the average value of π(t) − li(t), Canad. Math. Bull. 66 (2023), no. 1, 185–195,
MR4552509. Numerical entry: [357]
[A123] Jurkat, W. and Peyerimhoﬀ, A., A constructive approach to Kronecker approximations and its ap-
plication to the Mertens conjecture, J. Reine Angew. Math. 286(287) (1976), 322–340, MR429789.
Numerical entry: [125]

100 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

[A124] Jurkat, W. B., On the Mertens conjecture and related general Ω-theorems (1973), 147–158, MR0352026.
Numerical entry: [121]
[A125] Kaczorowski, J., On sign-changes in the remainder-term of the prime-number formula. I, Acta Arith.
44 (1984), no. 4, 365–377, MR777013. Numerical entry: [170]
[A126] Kaczorowski, J., On sign-changes in the remainder-term of the prime-number formula. II, Acta
Arith. 45 (1985), no. 1, 65–74, MR791085. Numerical entry: [180]
[A127] Kaczorowski, J., On sign-changes in the remainder-term of the prime-number formula. III, Acta
Arith. 48 (1987), no. 4, 347–371, MR927376. Numerical entry: [187]
[A128] Kaczorowski, J., On sign-changes in the remainder-term of the prime-number formula. IV, Acta
Arith. 50 (1988), no. 1, 15–21, MR945273. Numerical entry: [193]
[A129] Kaczorowski, J., The k-functions in multiplicative number theory. I. On complex explicit formulae,
Acta Arith. 56 (1990), no. 3, 195–211, MR1083000. Numerical entry: [201]
[A130] Kaczorowski, J., The k-functions in multiplicative number theory. II. Uniform distribution of zeta
zeros, Acta Arith. 56 (1990), no. 3, 213–224, MR1083001. Numerical entry: [202]
[A131] Kaczorowski, J., The k-functions in multiplicative number theory. III. Uniform distribution of zeta
zeros; discrepancy, Acta Arith. 57 (1991), no. 3, 199–210, MR1105605. Numerical entry: [205]
[A132] Kaczorowski, J., The k-functions in multiplicative number theory. IV. On a method of A. E. Ingham,
Acta Arith. 57 (1991), no. 3, 231–244, MR1105608. Numerical entry: [206]
[A133] Kaczorowski, J., The k-functions in multiplicative number theory. V. Changes of sign of some arith-
metical error terms, Acta Arith. 59 (1991), no. 1, 37–58, MR1133236. Numerical entry: [207]
[A134] Kaczorowski, J., A contribution to the Shanks-R´enyi race problem, Quart. J. Math. Oxford Ser. (2)
44 (1993), no. 176, 451–458, MR1251926. Numerical entry: [210]
[A135] Kaczorowski, J., On the Shanks-R´enyi race problem, Acta Arith. 74 (1996), no. 1, 31–46, MR1367576.
Numerical entry: [219]
[A136] Kaczorowski, J. and Pintz, J., Oscillatory properties of arithmetical functions. I, Acta Math. Hungar.
48 (1986), no. 1-2, 173–185, MR858395. Numerical entry: [183]
[A137] Kaczorowski, J. and Pintz, J., Oscillatory properties of arithmetical functions. II, Acta Math. Hun-
gar. 49 (1987), no. 3-4, 441–453, MR891057. Numerical entry: [188]
[A138] Kaczorowski, J. and Sta´s, W., On the number of sign changes in the remainder-term of the prime-
ideal theorem, Colloq. Math. 56 (1988), no. 1, 185–197, MR980524. Numerical entry: [194]
[A139] Kaczorowski, J., Results on the distribution of primes, J. Reine Angew. Math. 446 (1994), 89–113,
MR1256149. Numerical entry: [212]
[A140] Kaczorowski, J., On the distribution of primes (mod 4), Analysis 15 (1995), no. 2, 159–171, MR1344249.
Numerical entry: [217]
[A141] Kaczorowski, J., On the Shanks-R´enyi race problem mod 5, J. Number Theory 50 (1995), no. 1,
106–118, MR1310738. Numerical entry: [218]
[A142] Kaczorowski, J., Boundary values of Dirichlet series and the distribution of primes, in: European
Congress of Mathematics, Vol. I (Budapest, 1996), vol. 168, Progr. Math. Birkh¨auser, Basel, 1998,
237–254, MR1645811. Numerical entry: [221]
[A143] Kaczorowski, J., Results on the M¨obius function, J. Lond. Math. Soc. (2) 75 (2007), no. 2, 509–521,
MR2340242. Numerical entry: [253]
[A144] Kaczorowski, J., On the distribution of irreducible algebraic integers, Monatsh. Math. 156 (2009),
no. 1, 47–71, MR2470105. Numerical entry: [262]
[A145] Kaczorowski, J., Ω-estimates related to irreducible algebraic integers, Math. Nachr. 283 (2010),
no. 9, 1291–1303, MR2730494. Numerical entry: [268]
[A146] Kaczorowski, J. and Ramar´e, O., Almost periodicity of some error terms in prime number theory,
Acta Arith. 106 (2003), no. 3, 277–297, MR1957110. Numerical entry: [238]
[A147] Kaczorowski, J. and Sta´s, W., On the number of sign-changes in the remainder-term of the prime-
ideal theorem, Discuss. Math. 9 (1988), 83–102 (1989), MR1042465. Numerical entry: [195]
[A148] Kaczorowski, J. and Wiertelak, K., Ω-estimates for a class of arithmetic error terms, Math. Proc.
Cambridge Philos. Soc. 142 (2007), no. 3, 385–394, MR2329690. Numerical entry: [254]

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 101

[A149] Kaczorowski, J. and Wiertelak, K., Oscillations of a given size of some arithmetic error terms,
Trans. Amer. Math. Soc. 361 (2009), no. 9, 5023–5039, MR2506435. Numerical entry: [263]
[A150] Kaczorowski, J. and Wiertelak, K., Oscillations of the remainder term related to the Euler totient
function, J. Number Theory 130 (2010), no. 12, 2683–2700, MR2684490. Numerical entry: [269]
[A151] Kaczorowski, J. and Wiertelak, K., Smoothing arithmetic error terms: the case of the Euler φ
function, Math. Nachr. 283 (2010), no. 11, 1637–1645, MR2759800. Numerical entry: [270]
[A152] Kaneko, I. and Koyama, S.-y., A new aspect of Chebyshev’s bias for elliptic curves over function
ﬁelds, Proc. Amer. Math. Soc. 151 (2023), no. 12, 5059–5068, MR4648908. Numerical entry: [358]
[A153] Kaneko, I., Koyama, S.-y., and Kurokawa, N., Towards the Deep Riemann Hypothesis for GLn, 2023,
url: https://arxiv.org/abs/2206.02612. Numerical entry: [359]
[A154] Karatsuba, A. A., Behavior of the function R1(x) and of its mean value, Russian, Dokl. Akad. Nauk
404 (2005), no. 4, 439–442, MR2256805. Numerical entry: [245]
[A155] Karatsuba, A. A., On the approximation of π(x), Russian, Chebyshevskii Sb. 5 (2005), no. 4(12),
5–20, MR2169423. Numerical entry: [246]
[A156] Karatsuba, A. A., On the number of sign changes of the function R1(x) and its mean values, Russian,
Chebyshevskii Sb. 6 (2005), no. 2(14), 163–183, MR2262605. Numerical entry: [247]
[A157] K´atai, I., Eine Bemerkung zur “Comparative prime-number theory I-VIII” von S. Knapowski und
P. Tur´an, German, Ann. Univ. Sci. Budapest. E¨otv¨os Sect. Math. 7 (1964), 33–40, MR0176967.
Numerical entry: [82]
[A158] K´atai, I., Comparative theory of prime numbers, Russian, Acta Math. Acad. Sci. Hungar 18 (1967),
133–149, MR0207665. Numerical entry: [100]
[A159] K´atai, I., On investigations in the comparative prime number theory, Acta Math. Acad. Sci. Hungar.
18 (1967), 379–391, MR0218318. Numerical entry: [101]
[A160] K´atai, I., On oscillations of number-theoretic functions, Acta Arith. 13 (1967/1968), 107–122,
MR0219496. Numerical entry: [102]
[A161] K´atai, I., On oscillation of the number of primes in an arithmetical progression. Acta Sci. Math.
(Szeged) 29 (1968), 271–282, MR0233782. Numerical entry: [106]
[A162] K´atai, I., The Ω-estimation of the arithmetic mean of the M¨obius function, Hungarian, Magyar Tud.
Akad. Mat. Fiz. Oszt. K¨ozl. 15 (1965), 15–18, MR0231801. Numerical entry: [90]
[A163] K´atai, I., Omega-type investigations in prime number theory, Hungarian, with English summary,
Magyar Tud. Akad. Mat. Fiz. Oszt. K¨ozl. 16 (1966), 369–396, MR0241374. Numerical entry: [95]
[A164] Kim, J., Prime running functions, Exp. Math. 31 (2022), no. 4, 1291–1313, MR4516258. Numerical
entry: [345]
[A165] Kisilevsky, H. and Rubinstein, M. O., Chebotarev sets, Acta Arith. 171 (2015), no. 2, 97–124,
MR3414302. Numerical entry: [298]
[A166] Knapowski, S., On prime numbers in an arithmetical progression, Acta Arith. 4 (1958), 57–70,
MR0096622. Numerical entry: [52]
[A167] Knapowski, S., On the M¨obius function, Acta Arith. 4 (1958), 209–216, MR0096630. Numerical
entry: [53]
[A168] Knapowski, S., On the mean values of certain functions in prime number theory, English, with Rus-
sian summary, Acta Math. Acad. Sci. Hungar. 10 (1959), 375–390. (unbound insert), MR0111722.
Numerical entry: [55]
[A169] Knapowski, S., Contributions to the theory of the distribution of prime numbers in arithmetical
progressions. I, Acta Arith. 6 (1960/1961), 415–434, MR0125822. Numerical entry: [58]
[A170] Knapowski, S., Contributions to the theory of the distribution of prime numbers in arithmetical
progressions. II, Acta Arith 7 (1961/1962), 325–335, MR0142520. Numerical entry: [62]
[A171] Knapowski, S., Mean-value estimations for the M¨obius function. I, Acta Arith. 7 (1961), 121–130,
MR0133287. Numerical entry: [63]
[A172] Knapowski, S., Mean-value estimations for the M¨obius function. II, Acta Arith. 7 (1961), 337–343,
MR0142500. Numerical entry: [64]
[A173] Knapowski, S., On sign-changes in the remainder-term in the prime-number formula, J. London
Math. Soc. 36 (1961), 451–460, MR0133309. Numerical entry: [65]

102 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

[A174] Knapowski, S., On sign-changes of the diﬀerence π(x) − li x, Acta Arith. 7 (1961/1962), 107–119,
MR0133308. Numerical entry: [66]
[A175] Knapowski, S., Contributions to the theory of the distribution of prime numbers in arithmetical
progressions. III, Acta Arith 8 (1962/1963), 97–105, MR0142521. Numerical entry: [69]
[A176] Knapowski, S., On oscillations of certain means formed from the M¨obius series. I, Acta Arith. 8
(1962/1963), 311–320, MR0155802. Numerical entry: [70]
[A177] Knapowski, S., On oscillations of certain means formed from the M¨obius series. II, Acta Arith. 10
(1964), 377–386, MR0172856. Numerical entry: [83]
[A178] Knapowski, S. and Sta´s, W., A note on a theorem of Hardy and Littlewood, Acta Arith. 7 (1961/1962),
161–166, MR0131410. Numerical entry: [67]
[A179] Knapowski, S. and Tur´an, P., Comparative prime-number theory. I. Introduction, Acta Math. Acad.
Sci. Hungar. 13 (1962), 299–314, MR0146156. Numerical entry: [71]
[A180] Knapowski, S. and Tur´an, P., Comparative prime-number theory. II. Comparison of the progressions
≡ 1 mod k and ≡ l mod k, l ̸≡ 1 mod k, Acta Math. Acad. Sci. Hungar. 13 (1962), 315–342,
MR0146157. Numerical entry: [72]
[A181] Knapowski, S. and Tur´an, P., Comparative prime-number theory. III. Continuation of the study
of comparison of the progressions ≡ 1 mod k and ≡ l mod k, Acta Math. Acad. Sci. Hungar. 13
(1962), 343–364, MR0146158. Numerical entry: [73]
[A182] Knapowski, S. and Tur´an, P., Comparative prime-number theory. IV. Paradigma to the general case,
k = 8 and 5, Acta Math. Acad. Sci. Hungar. 14 (1963), 31–42, MR0146159. Numerical entry: [75]
[A183] Knapowski, S. and Tur´an, P., Comparative prime-number theory. V. Some theorems concerning the
general case, Acta Math. Acad. Sci. Hungar. 14 (1963), 43–63, MR0146160. Numerical entry: [76]
[A184] Knapowski, S. and Tur´an, P., Comparative prime-number theory. VI. Continuation of the general
case, Acta Math. Acad. Sci. Hungar. 14 (1963), 65–78, MR0146161. Numerical entry: [77]
[A185] Knapowski, S. and Tur´an, P., Comparative prime-number theory. VII. The problem of sign-changes
in the general case, Acta Math. Acad. Sci. Hungar 14 (1963), 241–250, MR0156826. Numerical
entry: [78]
[A186] Knapowski, S. and Tur´an, P., Comparative prime-number theory. VIII. Chebyshev’s problem for
k = 8, Acta Math. Acad. Sci. Hungar 14 (1963), 251–268, MR0156827. Numerical entry: [79]
[A187] Knapowski, S. and Tur´an, P., Further developments in the comparative prime-number theory. I,
Acta Arith. 9 (1964), 23–40, MR0162771. Numerical entry: [84]
[A188] Knapowski, S. and Tur´an, P., Further developments in the comparative prime-number theory. II.
A modiﬁcation of Chebyshev’s assertion, Acta Arith. 10 (1964), 293–313, MR0174538. Numerical
entry: [85]
[A189] Knapowski, S. and Tur´an, P., Further developments in the comparative prime-number theory. III,
Acta Arith. 11 (1965), 115–127, MR0180539. Numerical entry: [91]
[A190] Knapowski, S. and Tur´an, P., Further developments in the comparative prime-number theory. IV,
Acta Arith. 11 (1965), 147-161; ibid. 11 (1965), 147–161, MR0182616. Numerical entry: [92]
[A191] Knapowski, S. and Tur´an, P., Further developments in the comparative prime-number theory. V,
Acta Arith. 11 (1965), 147-161; ibid. 11 (1965), 193–202, MR0182616. Numerical entry: [93]
[A192] Knapowski, S. and Tur´an, P., On an assertion of ˇCebyˇsev, J. Analyse Math. 14 (1965), 267–274,
MR0177963. Numerical entry: [94]
[A193] Knapowski, S. and Tur´an, P., Further developments in the comparative prime-number theory. VI.
Accumulation theorems for residue-classes representing quadratic residues mod k, Acta Arith. 12
(1966), 85–96, MR0200250. Numerical entry: [96]

[A194] Knapowski, S. and Tur´an, P., ¨Uber einige Fragen der vergleichenden Primzahltheorie, German
(1969), 157–171, MR0272729. Numerical entry: [108]
[A195] Knapowski, S. and Tur´an, P., Further developments in the comparative prime number theory. VII,
Acta Arith. 21 (1972), 193–201, MR0302585. Numerical entry: [118]
[A196] Knapowski, S. and Tur´an, P., On the sign changes of (π(x) − li x). I, in: Topics in number theory
(Proc. Colloq., Debrecen, 1974), North-Holland, Amsterdam, 1976, 153–169. Colloq. Math. Soc.
J´anos Bolyai, Vol. 13, MR0439771. Numerical entry: [126]

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 103

[A197] Knapowski, S. and Tur´an, P., On the sign changes of (π(x) − li x). II, Monatsh. Math. 82 (1976),
no. 2, 163–175, MR0439772. Numerical entry: [127]
[A198] Knapowski, S. and Tur´an, P., On prime numbers ≡ 1 resp. 3 (mod 4), in: Number theory and
algebra, Academic Press, New York, 1977, pp. 157–165, MR0466043. Numerical entry: [134]
[A199] Kolesnik, G. and Straus, E. G., On the sum of powers of complex numbers, in: Studies in pure
mathematics, Birkh¨auser, Basel, 1983, 427–442, MR820241. Numerical entry: [166]
[A200] Kotnik, T., The prime-counting function and its analytic approximations: π(x) and its approxima-
tions, Adv. Comput. Math. 29 (2008), no. 1, 55–70, MR2420864. Numerical entry: [258]
[A201] Kotnik, T. and Lune, J. van de, On the order of the Mertens function, Experiment. Math. 13 (2004),
no. 4, 473–481, MR2118272. Numerical entry: [241]
[A202] Kotnik, T. and Riele, H. te, The Mertens conjecture revisited, in: Algorithmic number theory,
vol. 4076, Lecture Notes in Comput. Sci. Springer, Berlin, 2006, pp. 156–167, MR2282922. Numerical
entry: [251]
[A203] Kowalski, E., The large sieve, monodromy, and zeta functions of algebraic curves. II. Independence
of the zeros, Int. Math. Res. Not. IMRN (2008), Art. ID rnn 091, 57, MR2439552. Numerical
entry: [259]
[A204] Koyama, S.-y. and Kurokawa, N., Chebyshev’s bias for Ramanujan’s τ -function via the deep Riemann
hypothesis, Proc. Japan Acad. Ser. A Math. Sci. 98 (2022), no. 6, 35–39, MR4432981. Numerical
entry: [346]
[A205] Kunik, M. and Lucht, L. G., Power series with the von Mangoldt function, Funct. Approx. Comment.
Math. 47 (2012), no. part 1, 15–33, MR2987108. Numerical entry: [276]
[A206] Lamzouri, Y., Large deviations of the limiting distribution in the Shanks–R´enyi prime number race,
Math. Proc. Cambridge Philos. Soc. 153 (2012), no. 1, 147–166, MR2943671. Numerical entry: [277]
[A207] Lamzouri, Y., The Shanks-R´enyi prime number race with many contestants, Math. Res. Lett. 19
(2012), no. 3, 649–666, MR2998146. Numerical entry: [278]
[A208] Lamzouri, Y., Prime number races with three or more competitors, Math. Ann. 356 (2013), no. 3,
1117–1162, MR3063909. Numerical entry: [284]
[A209] Lamzouri, Y., A bias in Mertens’ product formula, Int. J. Number Theory 12 (2016), no. 1, 97–109,
MR3455269. Numerical entry: [304]
[A210] Lamzouri, Y. and Martin, B., On the race between primes with an odd versus an even sum of the last
k binary digits, Funct. Approx. Comment. Math. 61 (2019), no. 1, 7–25, MR4012359. Numerical
entry: [320]

[A211] Landau, E., ¨Uber einen Satz von Tschebyschef, German, Math. Ann. 61 (1906), no. 4, 527–550,
MR1511360. Numerical entry: [10]
[A212] Landau, E., Handbuch der Lehre von der Verteilung der Primzahlen. 2 B¨ande, German, Leipzig und
Berlin, B. G. Teubner, 1909, xviii+pp. 1–564, ix+pp. 565–961. Numerical entry: [11]

[A213] Landau, E., ¨Uber einige ¨altere Vermutungen und Behauptungen in der Primzahltheorie, German,
Math. Z. 1 (1918), no. 2-3, 1–24, MR1544293. Numerical entry: [18]

[A214] Landau, E., ¨Uber einige ¨altere Vermutungen und Behauptungen in der Primzahltheorie, German,
Math. Z. 1 (1918), no. 2-3, 213–219, MR1544293. Numerical entry: [19]
[A215] Landau, E., Handbuch der Lehre von der Verteilung der Primzahlen. 2 B¨ande, German, 2d ed; With
an appendix by Paul T. Bateman, Chelsea Publishing Co., New York, 1953, xviii+pp. 1–564, ix+pp.
565–1001, MR0068565. Numerical entry: [44]
[A216] Lau, Y.-K., On the existence of limiting distributions of some number-theoretic error terms, J.
Number Theory 94 (2002), no. 2, 359–374, MR1916279. Numerical entry: [234]
[A217] Lay, J., Sign changes in Mertens’ ﬁrst and second theorems, 2015, url: https://arxiv.org/abs/1505.03589.
Numerical entry: [299]
[A218] Leboeuf, P., Prime correlations and ﬂuctuations, Ann. Henri Poincar´e 4 (2003), no. suppl. 2, S727–
S752, MR2037293. Numerical entry: [239]
[A219] Leech, J., Note on the distribution of prime numbers, J. London Math. Soc. 32 (1957), 56–58,
MR0083001. Numerical entry: [48]

104 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

[A220] Lehman, R. S., On the diﬀerence π(x) − li(x), Acta Arith. 11 (1966), 397–410, MR0202686. Nu-
merical entry: [97]
[A221] Lehman, R. S., On Liouville’s function, Math. Comp. 14 (1960), 311–320, MR0120198. Numerical
entry: [59]
[A222] Lehmer, D. H. and Selberg, S., A sum involving the function of M¨obius, Acta Arith. 6 (1960), 111–
114, MR115965. Numerical entry: [60]
[A223] Lemke Oliver, R. J. and Soundararajan, K., Unexpected biases in the distribution of consecutive
primes, Proc. Natl. Acad. Sci. USA 113 (2016), no. 31, E4446–E4454, MR3624386. Numerical
entry: [305]
[A224] Lemke Oliver, R. J. and Soundararajan, K., The distribution of consecutive prime biases and sums
of sawtooth random variables, Math. Proc. Cambridge Philos. Soc. 168 (2020), no. 1, 149–169,
MR4043824. Numerical entry: [327]
[A225] Levinson, N., On the number of sign changes of π(x) − li x, in: Topics in number theory (Proc.
Colloq., Debrecen, 1974), North-Holland, Amsterdam, 1976, 171–177. Colloq. Math. Soc. J´anos
Bolyai, Vol. 13, MR0439774. Numerical entry: [128]
[A226] Lichtman, J. D., Martin, G., and Pomerance, C., Primes in prime number races, Proc. Amer. Math.
Soc. 147 (2019), no. 9, 3743–3757. Numerical entry: [321]
[A227] Lin, J. and Martin, G., Densities in certain three-way prime number races, Canad. J. Math. 74
(2022), no. 1, 232–265, MR4379402. Numerical entry: [347]
[A228] Littlewood, J. E., Sur la distribution des nombres premiers, French, Comptes Rendus de l’Acad.
Sci. Paris 158 (1914), 1869–1872. Numerical entry: [14]
[A229] Littlewood, J. E., Mathematical Notes: 3; on a Theorem Concerning the Distribution of Prime
Numbers, J. London Math. Soc. 2 (1927), no. 1, 41–45, MR1574052. Numerical entry: [22]
[A230] Littlewood, J. E., Mathematical Notes (12): An Inequality for a Sum of Cosines, J. London Math.
Soc. 12 (1937), no. 3, 217–221, MR1575079. Numerical entry: [31]
[A231] Mahatab, K. and Mukhopadhyay, A., Measure-theoretic aspects of oscillations of error terms, Acta
Arith. 187 (2019), no. 3, 201–217, MR3902795. Numerical entry: [322]
[A232] Makai, E., On a minimum problem. II, Acta Math. Acad. Sci. Hungar. 15 (1964), 63–66, MR0159791.
Numerical entry: [86]
[A233] Martin, G., Asymmetries in the Shanks-R´enyi prime number race, in: Number theory for the millen-
nium, II (Urbana, IL, 2000), A K Peters, Natick, MA, 2002, pp. 403–415, MR1956261. Numerical
entry: [235]
[A234] Martin, G., Mossinghoﬀ, M., and Trudgian, T., Fake mu’s, Proc. Amer. Math. Soc. 151 (2023),
no. 8, 3229–3244, MR4591762. Numerical entry: [360]
[A235] Martin, G. and Ng, N., Inclusive prime number races, Trans. Amer. Math. Soc. 373 (2020), no. 5,
3561–3607, MR4082248. Numerical entry: [328]
[A236] Mazur, B., Finding meaning in error terms, Bull. Amer. Math. Soc. (N.S.) 45 (2008), no. 2, 185–
228, MR2383303. Numerical entry: [260]
[A237] Meng, X., The distribution of k-free numbers and the derivative of the Riemann zeta-function, Math.
Proc. Cambridge Philos. Soc. 162 (2017), no. 2, 293–317, MR3604916. Numerical entry: [310]
[A238] Meng, X., Chebyshev’s bias for products of k primes, Algebra Number Theory 12 (2018), no. 2,
305–341, MR3803705. Numerical entry: [315]
[A239] Meng, X., Large bias for integers with prime factors in arithmetic progressions, Mathematika 64
(2018), no. 1, 237–252, MR3778223. Numerical entry: [316]
[A240] Meng, X., Number of prime factors over arithmetic progressions, Q. J. Math. 71 (2020), no. 1,
97–121, MR4077187. Numerical entry: [329]

[A241] Mertens, F., ¨Uber eine zahlentheoretische Funktion, German, Sitzungsberichte Akad. Wien 106
(1897), 761–830. Numerical entry: [4]
[A242] Milinovich, M. B. and Ng, N., A note on a conjecture of Gonek, Funct. Approx. Comment. Math.
46 (2012), 177–187, MR2931664. Numerical entry: [279]

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 105

[A243] Monach, W. R., Numerical Investigation of Several Problems in Number Theory, Thesis (Ph.D.)–
University of Michigan), ProQuest LLC, Ann Arbor, MI, 1980, 180 pp., MR2631002. Numerical
entry: [149]
[A244] Montgomery, H. L., The zeta function and prime numbers, in: Proceedings of the Queen’s Number
Theory Conference, 1979 (Kingston, Ont., 1979), vol. 54, Queen’s Papers in Pure and Appl. Math.
Queen’s Univ., Kingston, Ont., 1980, pp. 1–31, MR634679. Numerical entry: [150]
[A245] Montgomery, H. L., Ten lectures on the interface between analytic number theory and harmonic
analysis, vol. 84, CBMS Regional Conference Series in Mathematics, Published for the Conference
Board of the Mathematical Sciences, Washington, DC; by the American Mathematical Society,
Providence, RI, 1994, pp. xiv+220, MR1297543. Numerical entry: [213]
[A246] Montgomery, H. L. and Vorhauer, U. M. A., Changes of sign of the error term in the prime number
theorem, Funct. Approx. Comment. Math. 35 (2006), 235–247, MR2271616. Numerical entry: [252]
[A247] Moree, P., Chebyshev’s bias for composite numbers with restricted prime divisors, Math. Comp. 73
(2004), no. 245, 425–449, MR2034131. Numerical entry: [242]
[A248] Morrill, T., Platt, D., and Trudgian, T., Sign changes in the prime number theorem, Ramanujan J.
57 (2022), no. 1, 165–173, MR4360480. Numerical entry: [348]
[A249] Mossinghoﬀ, M. J., Oliveira e Silva, T., and Trudgian, T. S., The distribution of k-free numbers,
Math. Comp. 90 (2021), no. 328, 907–929, MR4194167. Numerical entry: [337]
[A250] Mossinghoﬀ, M. J. and Trudgian, T. S., Between the problems of P´olya and Tur´an, J. Aust. Math.
Soc. 93 (2012), no. 1–2, 157–171, MR3062002. Numerical entry: [280]
[A251] Mossinghoﬀ, M. J. and Trudgian, T. S., The Liouville function and the Riemann hypothesis, in:
Exploring the Riemann zeta function, Springer, Cham, 2017, pp. 201–221, MR3700043. Numerical
entry: [311]
[A252] Mossinghoﬀ, M. J. and Trudgian, T. S., A tale of two omegas, in: 75 years of mathematics of
computation, vol. 754, Contemp. Math. Amer. Math. Soc., [Providence], RI, 2020, pp. 343–364,
MR4132130. Numerical entry: [330]
[A253] Mossinghoﬀ, M. J. and Trudgian, T. S., Oscillations in weighted arithmetic sums, Int. J. Number
Theory 17 (2021), no. 7, 1697–1716, MR4295379. Numerical entry: [338]
[A254] Mossinghoﬀ, M. J. and Trudgian, T. S., Oscillations in the Goldbach conjecture, J. Th´eor. Nombres
Bordeaux 34 (2022), no. 1, 295–307, MR4450618. Numerical entry: [349]

[A255] Motohashi, Y., The binary additive divisor problem, Ann. Sci. ´Ecole Norm. Sup. (4) 27 (1994), no. 5,
529–572, MR1296556. Numerical entry: [214]
[A256] Myerscough, C., Application of an accurate remainder term in the calculation of residue class dis-
tributions, 2013, url: https://arxiv.org/abs/1301.1434. Numerical entry: [285]
[A257] Narkiewicz, W., The development of prime number theory, Springer Monographs in Mathematics,
Springer-Verlag, Berlin, 2000, pp. xii+448, MR1756780. Numerical entry: [226]
[A258] Neubauer, G., Eine empirische Untersuchung zur Mertensschen Funktion, German, Numer. Math.
5 (1963), 1–13, MR155787. Numerical entry: [80]
[A259] Ng, N., Limiting Distributions and Zeros of Artin L-Functions, Thesis (Ph.D.)–University of British
Columbia, 2000, url: http://www.cs.uleth.ca/~nathanng/RESEARCH/phd.thesis.pdf. Numer-
ical entry: [227]
[A260] Ng, N., The distribution of the summatory function of the M¨obius function, Proc. London Math.
Soc. (3) 89 (2004), no. 2, 361–389, MR2078705. Numerical entry: [243]
[A261] Odlyzko, A. M. and Riele, H. J. J. te, Disproof of the Mertens conjecture, J. Reine Angew. Math.
357 (1985), 138–160, MR783538. Numerical entry: [181]
[A262] Petrushov, O. A., Asymptotic estimates of functions based on the behavior of their Laplace trans-
forms near singular points, Math. Notes 93 (2013), no. 5–6, 906–916, MR3206041. Numerical en-
try: [286]

[A263] Phragm´en, P., Sur le logarithme int´egral et la fonction f (x) de Riemann, French, ¨Ofversigt af Kongl.
Vetenskaps–Akademiens F¨ohandlingar. 48 (1891), 599–616. Numerical entry: [3]

106 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

[A264] Piltz, A., ¨Uber die H¨auﬁgkeit der Primzahlen in arithmetischen Progressionen und ¨uber verwandte
Gesetze, German, Habilitationsschrift, Friedrich–Schiller–Universit¨at Jena (1884). Numerical en-
try: [2]
[A265] Pintz, J., Bemerkungen zur Arbeit: “On the sign changes of (π(x) − li x). II” (Monatsh. Math.
82 (1976), no. 2, 163–175) von S. Knapowski und P. Tur´an, German, Monatsh. Math. 82 (1976),
no. 3, 199–206, MR0439773. Numerical entry: [129]
[A266] Pintz, J., On the remainder term of the prime number formula. III. Sign changes of π(x) − lix,
Studia Sci. Math. Hungar. 12 (1977), no. 3-4, 345–369 (1980), MR607089. Numerical entry: [135]
[A267] Pintz, J., On the sign changes of π(x) − li(x), in: Journ´ees Arithm´etiques de Caen (Univ. Caen,
Caen, 1976), Soc. Math. France, Paris, 1977, 255–265. Ast´erisque No. 41–42, MR0447151. Numerical
entry: [136]
[A268] Pintz, J., On the remainder term of the prime number formula. IV. Sign changes of π(x) − lix,
Studia Sci. Math. Hungar. 13 (1978), no. 1-2, 29–42 (1981), MR630377. Numerical entry: [140]
[A269] Pintz, J., On the remainder term of the prime number formula. I. On a problem of Littlewood, Acta
Arith. 36 (1980), no. 4, 341–365, MR585891. Numerical entry: [151]
[A270] Pintz, J., On the remainder term of the prime number formula. II. On a theorem of Ingham, Acta
Arith. 37 (1980), 209–220, MR598876. Numerical entry: [152]
[A271] Pintz, J., On the remainder term of the prime number formula. V. Eﬀective mean value theorems,
Studia Sci. Math. Hungar. 15 (1980), no. 1-3, 215–223, MR681441. Numerical entry: [153]
[A272] Pintz, J., On the remainder term of the prime number formula. VI. Ineﬀective mean value theorems,
Studia Sci. Math. Hungar. 15 (1980), no. 1-3, 225–230, MR681442. Numerical entry: [154]
[A273] Pintz, J., Oscillatory properties of M (x) = ∑n≤x µ(n). II, Studia Sci. Math. Hungar. 15 (1980),
no. 4, 491–496, MR688630. Numerical entry: [155]
[A274] Pintz, J., On the sign changes of M (x) = ∑n≤x µ(n), Analysis 1 (1981), no. 3, 191–195, MR660714.
Numerical entry: [160]
[A275] Pintz, J., Oscillatory properties of M (x) = ∑n≤x µ(n). I, Acta Arith. 42 (1982), no. 1, 49–55,
MR678996. Numerical entry: [163]
[A276] Pintz, J., On the distribution of square-free numbers, J. London Math. Soc. (2) 28 (1983), no. 3,
401–405, MR724708. Numerical entry: [167]
[A277] Pintz, J., Oscillatory properties of the remainder term of the prime number formula, in: Studies in
pure mathematics, Birkh¨auser, Basel, 1983, pp. 551–560, MR820251. Numerical entry: [168]
[A278] Pintz, J., On the partial sums of the M¨obius function, in: Topics in classical number theory, Vol.
I, II (Budapest, 1981), vol. 34, Colloq. Math. Soc. J´anos Bolyai, North-Holland, Amsterdam, 1984,
1229–1250, MR781183. Numerical entry: [171]
[A279] Pintz, J., On the remainder term of the prime number formula and the zeros of Riemann’s zeta-
function, in: Number theory, Noordwijkerhout 1983 (Noordwijkerhout, 1983), vol. 1068, Lecture
Notes in Math. Springer, Berlin, 1984, pp. 186–197, MR756094. Numerical entry: [172]
[A280] Pintz, J., Oscillatory properties of M (x) = ∑n≤x µ(n). III, Acta Arith. 43 (1984), no. 2, 105–113,
MR736725. Numerical entry: [173]
[A281] Pintz, J., An eﬀective disproof of the Mertens conjecture, Ast´erisque (1987), no. 147-148, 325–333,
346, MR891440. Numerical entry: [189]
[A282] Pintz, J., On an assertion of Riemann concerning the distribution of prime numbers, Acta Math.
Hungar. 58 (1991), no. 3-4, 383–387, MR1153492. Numerical entry: [208]
[A283] Pintz, J. and Salerno, S., Irregularities in the distribution of primes in arithmetic progressions. II,
Arch. Math. (Basel) 43 (1984), no. 4, 351–357, MR802311. Numerical entry: [174]
[A284] Pintz, J. and Salerno, S., On the comparative theory of primes, Ann. Scuola Norm. Sup. Pisa Cl.
Sci. (4) 11 (1984), no. 2, 245–260, MR764945. Numerical entry: [175]
[A285] Pintz, J. and Salerno, S., Accumulation theorems for primes in arithmetic progressions, Acta Math.
Hungar. 46 (1985), no. 1-2, 151–172, MR819064. Numerical entry: [182]
[A286] Pintz, J. and Salerno, S., Some consequences of the general Riemann hypothesis in the comparative
theory of primes, J. Number Theory 23 (1986), no. 2, 183–194, MR845900. Numerical entry: [184]

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 107

[A287] Pintz, J. and Salerno, S., Irregularities in the distribution of primes in arithmetic progressions. I,
Arch. Math. (Basel) 42 (1984), no. 5, 439–447, MR756697. Numerical entry: [176]
[A288] Platt, D. J. and Trudgian, T. S., On the ﬁrst sign change of θ(x) − x, Math. Comp. 85 (2016),
no. 299, 1539–1547, MR3454375. Numerical entry: [306]
[A289] Platt, D. and Trudgian, T., Fujii’s development on Chebyshev’s conjecture, Int. J. Number Theory
15 (2019), no. 3, 639–644, MR3925757. Numerical entry: [323]
[A290] Plymen, R., The Great Prime Number Race, vol. 92, Student Mathematical Library, American
Mathematical Society, Providence, RI, 2020, p. 138, MR4249594. Numerical entry: [331]
[A291] P´olya, G., Verschiedene Bemerkungen zur Zahlentheorie, German, Jahresbericht der deutschen
Math.–Vereinigung 28 (1919), 31–40. Numerical entry: [20]

[A292] P´olya, G., ¨Uber das Vorzeichen des Restgliedes im Primzahltheorie, German, G¨ott. Nachr. (1930),
19–27. Numerical entry: [23]
[A293] P´olya, G., On polar singularities of power series and of Dirichlet series, Proc. London Math. Soc.
(2) 33 (1931), no. 2, 85–101, MR1576856. Numerical entry: [25]

[A294] P´olya, G., ¨Uber das Vorzeichen des Restgliedes im Primzahlsatz, German (1969), 233–244, MR0263757.
Numerical entry: [109]
[A295] Porritt, S., Character sums over products of prime polynomials, 2020, url: https://arxiv.org/abs/2003.12002.
Numerical entry: [332]
[A296] Prachar, K., Primzahlverteilung, German, Springer-Verlag, Berlin-G¨ottingen-Heidelberg, 1957, x+415
pp. MR0087685. Numerical entry: [49]
[A297] Puchta, J.-C., On large oscillations of the remainder of the prime number theorems, Acta Math.
Hungar. 87 (2000), no. 3, 213–227, MR1761276. Numerical entry: [228]
[A298] Radziejewski, M., On the distribution of algebraic numbers with prescribed factorization properties,
Acta Arith. 116 (2005), no. 2, 153–171, MR2110393. Numerical entry: [248]
[A299] Radziejewski, M., Oscillations of error terms associated with certain arithmetical functions, Monatsh.
Math. 144 (2005), no. 2, 113–130, MR2123959. Numerical entry: [249]
[A300] Radziejewski, M., Oscillatory properties of real functions with weakly bounded Mellin transform, Q.
J. Math. 65 (2014), no. 1, 249–266, MR3179660. Numerical entry: [293]
[A301] Riele, H. J. J. te, Computations concerning the conjecture of Mertens, J. Reine Angew. Math.
311(312) (1979), 356–360, MR549977. Numerical entry: [143]
[A302] Riele, H. J. J. te, On the sign of the diﬀerence π(x) − li(x), Math. Comp. 48 (1987), no. 177, 323–
328, MR866118. Numerical entry: [190]
[A303] Riele, H. J. J. te, The Mertens conjecture, in: The legacy of Bernhard Riemann after one hundred
and ﬁfty years. Vol. II, vol. 35.2, Adv. Lect. Math. (ALM), Int. Press, Somerville, MA, 2016, pp. 703–
718, MR3525909. Numerical entry: [307]
[A304] Robin, G., Sur l’ordre maximum de la fonction somme des diviseurs, French, in: Seminar on number
theory, Paris 1981–82 (Paris, 1981/1982), vol. 38, Progr. Math. Birkh¨auser Boston, Boston, MA,
1983, 233–244, MR729173. Numerical entry: [169]
[A305] Robin, G., Irr´egularit´es dans la distribution des nombres premiers dans les progressions arithm´etiques,
French, Ann. Fac. Sci. Toulouse Math. (5) 8 (1986), no. 2, 159–173, MR928842. Numerical en-
try: [185]
[A306] Rosser, J. B. and Schoenfeld, L., Approximate formulas for some functions of prime numbers, Illinois
J. Math. 6 (1962), 64–94, MR0137689. Numerical entry: [74]
[A307] Rubinstein, M. and Sarnak, P., Chebyshev’s bias, Experiment. Math. 3 (1994), no. 3, 173–197,
MR1329368. Numerical entry: [215]
[A308] Ruzsa, I. Z., Consecutive primes modulo 4, Indag. Math. (N.S.) 12 (2001), no. 4, 489–503, MR1908877.
Numerical entry: [231]
[A309] Ryan, J. T., One more “many-more” assertion, Amer. Math. Monthly 74 (1967), no. 1, 19–24,
MR0207632. Numerical entry: [103]
[A310] Saﬀari, B., Sur la fausset´e de la conjecture de Mertens. (With discussion.) French, C. R. Acad. Sci.
Paris S´er. A-B 271 (1970), A1097–A1101, MR280447. Numerical entry: [111]

108 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

[A311] Sankaranarayanan, A., On the sign changes in the remainder term of an asymptotic formula for the
number of squarefree numbers, Arch. Math. (Basel) 60 (1993), no. 1, 51–57, MR1193094. Numerical
entry: [211]
[A312] Saouter, Y. and Demichel, P., A sharp region where π(x) − li(x) is positive, Math. Comp. 79 (2010),
no. 272, 2395–2405, MR2684372. Numerical entry: [271]
[A313] Saouter, Y. and Riele, H. te, Improved results on the Mertens conjecture, Math. Comp. 83 (2014),
no. 285, 421–433, MR3120597. Numerical entry: [294]
[A314] Saouter, Y., Trudgian, T., and Demichel, P., A still sharper region where π(x) − li(x) is positive,
Math. Comp. 84 (2015), no. 295, 2433–2446, MR3356033. Numerical entry: [300]
[A315] Sarnak, P., Letter to Barry Mazur on ‘Chebyshev’s bias’ for τ (p), 2007, url: http://web.math.princeton.edu/sarna
Numerical entry: [255]
[A316] Schlage–Puchta, J.-C., Sign changes of π(x, q, 1) − π(x, q, a), Acta Math. Hungar. 102 (2004), no. 4,
305–320, MR2040112. Numerical entry: [244]
[A317] Schlage–Puchta, J.-C., Oscillations of the error term in the prime number theorem, Acta Math.
Hungar. 156 (2018), no. 2, 303–308, MR3871592. Numerical entry: [317]

[A318] Schmidt, E., ¨Uber die Anzahl der Primzahlen unter gegebener Grenze, German, Math. Ann. 57
(1903), no. 2, 195–204, MR1511206. Numerical entry: [8]
[A319] Sedrati, Y., Inequities in the Shanks–Renyi prime number race over function ﬁelds, Mathematika
68 (2022), no. 3, 840–895, MR4449835. Numerical entry: [350]
[A320] Shanks, D., Quadratic residues and the distribution of primes, Math. Tables Aids Comput. 13
(1959), 272–284, MR0108470. Numerical entry: [56]
[A321] Shanks, D. and Lal, M., Bateman’s constants reconsidered and the distribution of cubic residues,
Math. Comp. 26 (1972), 265–285, MR0302590. Numerical entry: [119]
[A322] Shchebetov, A., Chebyshev’s bias visualizer, 2021, url: http://math101.guru/en/downloads-2/repository/.
Numerical entry: [339]
[A323] Sheth, A., Euler products at the centre and applications to Chebyshev’s bias, 2024, url: https://arxiv.org/abs/2405.0
Numerical entry: [367]
[A324] Skewes, S., On the Diﬀerence π(x) − li (x) (I), J. London Math. Soc. 8 (1933), no. 4, 277–283,
MR1573970. Numerical entry: [27]
[A325] Skewes, S., On the diﬀerence π(x)−li x. II, Proc. London Math. Soc. (3) 5 (1955), 48–70, MR0067145.
Numerical entry: [46]
[A326] Sneed, J. P., Prime and quasi-prime number races, Thesis (Ph.D.)–University of Illinois at Urbana-
Champaign, ProQuest LLC, Ann Arbor, MI, 2009, 83 pp., MR2753165. Numerical entry: [264]
[A327] S´os, V. T. and Tur´an, P., On some new theorems in the theory of Diophantine approximations,
English, with Russian summary, Acta Math. Acad. Sci. Hungar. 6 (1955), 241–255, MR0077579.
Numerical entry: [47]
[A328] Spira, R., Zeros of sections of the zeta function. II, Math. Comp. 22 (1968), 163–173, MR228456.
Numerical entry: [107]
[A329] Stanis law Knapowski (19. V. 1931–28. IX. 1967), Colloq. Math. 23 (1971), 309–310, MR0300853.
Numerical entry: [113]
[A330] Stark, H. M., On the asymptotic density of the k-free integers, Proc. Amer. Math. Soc. 17 (1966),
1211–1214, MR199161. Numerical entry: [98]
[A331] Stark, H. M., A problem in comparative prime number theory, Acta Arith. 18 (1971), 311–320,
MR0289452. Numerical entry: [114]

[A332] Sta´s, W., ¨Uber die Umkehrung eines Satzes von Ingham, German, Acta Arith. 6 (1960/1961), 435–
446, MR0146153. Numerical entry: [61]
[A333] Sta´s, W., Some remarks on a series of Ramanujan, Acta Arith. 10 (1964/1965), 359–368, MR0177957.
Numerical entry: [87]
[A334] Sta´s, W. and Wiertelak, K., Further applications of Tur´an’s methods to the distribution of prime
ideals in ideal classes (mod f ), Acta Arith. 31 (1976), no. 2, 153–165, MR0429797. Numerical
entry: [130]

ANNOTATED BIBLIOGRAPHY FOR COMPARATIVE PRIME NUMBER THEORY 109

[A335] Sta´s, W., On sign-changes in the remainder term of the prime ideal formula, Funct. Approx. Com-
ment. Math. 13 (1982), 159–166, MR817334. Numerical entry: [164]
[A336] Stechkin, S. B. and Popov, A. Y., Asymptotic distribution of prime numbers in the mean, Uspekhi
Mat. Nauk 51 (1996), no. 6(312), 21–88, MR1440155. Numerical entry: [220]
[A337] Steinig, J., The changes of sign of certain arithmetical error-terms, Comment. Math. Helv. 44
(1969), 385–400, MR0257003. Numerical entry: [110]
[A338] Sterneck, R. D. von, Empirische Untersuchung ¨uber den Verlauf der zahlentheoretischen Funktion
σ(n) = ∑x=n
x=1 µ(x) im Intervalle von 0 bis 150000, German, Sitzungsberichte Akad. Wiss. Wien IIa
106 (1897), 835–1024. Numerical entry: [5]
[A339] Sterneck, R. D. von, Bemerkung ¨uber die Summierung einiger zahlen-theoretischen Functionen,
Monatsh. Math. Phys. 9 (1898), no. 1, 43–45, MR1546543. Numerical entry: [6]
[A340] Sterneck, R. D. von, Empirische Untersuchung ¨uber den Verlauf der zahlentheoretischen Funktion
σ(n) = ∑x=n
x=1 µ(x) im Intervalle von 150000 bis 500000, German, Sitzungsberichte Kais. Akad.
Wissensch. Wien IIa 110 (1901), 1053–1102. Numerical entry: [7]
[A341] Sterneck, R. D. von, Die zahlentheoretische Funktion σ(n) bis zur Grenze 5000000, German, Sitzungs-
berichte Kais. Akad. Wissensch. Wien IIa 121 (1912), 1083–1096. Numerical entry: [12]
[A342] Sterneck, R. D. von, Neue empirische Daten ¨uber die zahlentheoretische Funktion σ(n), German,
Proc. 5th International Congress of Mathematicians 1 (1913), 341–343. Numerical entry: [13]
[A343] Stieltjes, T. J., Correspondance d’Hermite et de Stieltjes, French, Gauthier–Villars, Imprimeur–
Libraire, Paris, 1905, xxi+pp. 1–477. Numerical entry: [9]

[A344] Stoll, D. A. and Demichel, P., The impact of ζ(s) complex zeros on π(x) for x < 1010
13, Math.
Comp. 80 (2011), no. 276, 2381–2394, MR2813366. Numerical entry: [275]

[A345] Szyd lo, B., ¨Uber Vorzeichenwechsel einiger arithmetischer Funktionen. I, German, Math. Ann. 283
(1989), 139–149, MR0973808. Numerical entry: [198]

[A346] Szyd lo, B., ¨Uber Vorzeichenwechsel einiger arithmetischer Funktionen. II, German, Math. Ann. 283
(1989), 151–163, MR0973808. Numerical entry: [199]

[A347] Szyd lo, B., ¨Uber Vorzeichenwechsel einiger arithmetischer Funktionen. III, German, Monatsh. Math.
108 (1989), 325–336, MR1029966. Numerical entry: [200]
[A348] Szyd lo, B., On oscillations in the additive divisor problem. I, Acta Arith. 66 (1994), no. 1, 63–69,
MR1262653. Numerical entry: [216]
[A349] Tanaka, M., A numerical investigation on cumulative sum of the Liouville function, Tokyo J. Math.
3 (1980), no. 1, 187–189, MR584557. Numerical entry: [156]
[A350] Tanaka, M., On the M¨obius and allied functions, Tokyo J. Math. 3 (1980), no. 2, 215–218, MR605090.
Numerical entry: [157]
[A351] Tietze, H., Einige Tabellen zur Verteilung der Primzahlen auf Untergruppen der teilerfremden Restk-
lassen nach gegebenem Modul, German, Abh. Bayer. Akad. Wiss. Math.-Nat. Abt. (N.F.) 1944
(1944), no. 55, 31, MR0017310. Numerical entry: [36]
[A352] Titchmarsh, E. C., The Theory of the Riemann Zeta-Function, Oxford, at the Clarendon Press,
1951, pp. vi+346, MR0046485. Numerical entry: [42]
[A353] Titchmarsh, E. C., The theory of the Riemann zeta-function, Second, Edited and with a preface by
D. R. Heath-Brown, The Clarendon Press, Oxford University Press, New York, 1986, pp. x+412,
MR0882550. Numerical entry: [186]
[A354] Tur´an, P., On the remainder-term of the prime-number formula. II, English, with Russian summary,
Acta Math. Acad. Sci. Hungar. 1 (1950), 155–166, MR0049219. Numerical entry: [39]
[A355] Tur´an, P., Nachtrag zu meiner Abhandlung “On some approximative Dirichlet polynomials in the
theory of zeta-function of Riemann”, Acta Math. Acad. Sci. Hungar. 10 (1959), 277–298 (unbound
insert), MR115977. Numerical entry: [57]
[A356] Tur´an, P., On some further one-sided theorems of new type in the theory of Diophantine approx-
imations, English, with Russian summary, Acta Math. Acad. Sci. Hungar. 12 (1961), 455–468,
MR0132728. Numerical entry: [68]

110 MARTIN, YANG, BAHRINI, BAJPAI, BENL˙I, DOWNEY, LI, LIANG, PARVARDI, SIMPSON, WHITE, AND YIP

[A357] Tur´an, P., On a comparative theory of primes, in: Proc. Fourth All-Union Math. Congr (Leningrad,
1961) (Russian), Vol. II, Izdat. “Nauka”, Leningrad, 1964, pp. 137–142, MR0229595. Numerical
entry: [88]
[A358] Tur´an, P., On some approximative Dirichlet-polynomials in the theory of the zeta-function of Rie-
mann, Danske Vid. Selsk. Mat.-Fys. Medd. 24 (1948), no. 17, 36, MR27305. Numerical entry: [37]
[A359] Tur´an, P., On the remainder-term of the prime-number formula. I, English, with Russian summary,
Acta Math. Acad. Sci. Hungar. 1 (1950), 48–63, MR0043121. Numerical entry: [40]
[A360] Tur´an, P., Eine neue Methode in der Analysis und deren Anwendungen, German, Akad´emiai Kiad´o,
Budapest, 1953, 196 pp., MR0060548. Numerical entry: [45]
[A361] Tur´an, P., Commemoration on Stanis law Knapowski, Colloq. Math. 23 (1971), 310–318, MR0300854.
Numerical entry: [115]
[A362] Tur´an, P., On a new method of analysis and its applications, Pure and Applied Mathematics (New
York), John Wiley & Sons, Inc., New York, 1984, pp. xvi+584, MR749389. Numerical entry: [177]
[A363] Wintner, A., On the asymptotic distribution of the remainder term of the prime-number theorem,
Amer. J. Math. 57 (1935), no. 3, 534–538, MR1507933. Numerical entry: [29]
[A364] Wintner, A., Asymptotic distributions and inﬁnite convolutions, Lecture notes distributed by the
Institute for Advanced Study (Princeton) (1938). Numerical entry: [32]
[A365] Wintner, A., On the distribution function of the remainder term of the prime number theorem,
Amer. J. Math. 63 (1941), 233–248, MR0004255. Numerical entry: [34]
[A366] Wintner, A., A note on Mertens’ hypothesis, Rev. Ci. (Lima) 50 (1948), 181–184, MR29414. Nu-
merical entry: [38]
[A367] Wintner, A., On the λ-variant of Mertens’ µ-hypothesis, Amer. J. Math. 80 (1958), 639–642,
MR98723. Numerical entry: [54]

University of British Columbia, Department of Mathematics, Room 121, 1984 Mathematics Road, Vancouver,
BC Canada V6T 1Z2
Email address: gerg@math.ubc.ca
