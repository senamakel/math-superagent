<!-- source: https://arxiv.org/pdf/1810.05244 | converted from PDF -->

A COMPUTATIONAL HISTORY OF PRIME NUMBERS AND
RIEMANN ZEROS

PIETER MOREE, IZABELA PETRYKIEWICZ, AND ALISA SEDUNOVA

Abstract. We give an informal survey of the historical development of computations
related to prime number distribution and zeros of the Riemann zeta function
1.

The fundamental quantity in the study of prime numbers
2 is the prime counting func-
tion π(x), which counts the number of primes not exceeding x; in mathematical notation
we have
 π(x) = ∑

p≤x 1.

The ﬁrst mathematicians to investigate the growth of π(x) had of course to start with
collecting data. They did this by painfully setting up tables of consecutive prime numbers,
e.g., Kr¨uger in 1746 and Vega in 1797 (primes up to 100 000 and 400 031 respectively).
The most celebrated of these prime table computers was Gauss. In 1791, when he was 14
years old, he noticed that as one gets to larger and larger numbers the primes thin out,
but that locally their distribution appears to be quite erratic. He based himself on a prime
number table contained in a booklet with tables of logarithms he had received as a prize,
and went on to conjecture that the “probability that an arbitrary integer n is actually a
prime number should equal 1/ log n”. Thus Gauss conjectured that

π(x) ≈ ∑

2≤n≤x
 1
log n ≈ Li(x),

with
 Li(x) = ∫ x

2
 dt
log t,

the logarithmic integral3. Since by partial integration it is easily seen that Li(x) ∼
x/ log x, the conjecture of Gauss implies that asymptotically

π(x) ∼ x
log x,

2010 Mathematics Subject Classiﬁcation. 11N37, 11Y60.
1Caution! The authors are non-experts.
2We follow the tradition to denote a prime number by the letter p.
3An ever recurring theme in analytic number theory is approximating a sum by an integral (Section 1).
1arXiv:1810.05244v1  [math.NT]  11 Oct 2018
2 P. MOREE, I. PETRYKIEWICZ, AND A. SEDUNOVA

a conjecture that was proved much later, in 1896, by Hadamard
4 and de la Vall´ee-Poussin5

independently. This asymptotic for π(x) is called the Prime Number Theorem (PNT).
Gauss kept a life long interest in primes and what he did was to count primes in blocks
of 1 000 (a Chiliade). As he wrote in a letter to Bessel, he would use an idle quarter of
hour here and there to deal with a further block. By the end of his life he would extend the
tables up to 3 000 000. After Gauss, number theorists kept extending the existing prime
number tables. Thus in 1856 Crelle6 published a table of primes up to 6 000 000, and a few
years later Dase
7 extended this to 9 000 000. The most impressive feat in this regard is due
to Kulik
8, who spent 20 years preparing a factor table of the numbers coprime to 30 up to
1 000 330 200 (he did so in eight manuscript volumes, totalling 4 212 pages).
The holy grail in computational prime number theory is to ﬁnd sharp estimates of π(x).
These estimates should be in terms of elementary functions.
An early attempt is by Legendre
9, who claimed (1808) that x/(log x − 1.0836) should
approximate π(x) well. We now know that this is a reasonable estimate (the estimate
x/(log x − 1) is actually better). A much more recent and rigorous example is provided by
the estimates x
log x
 (
1 + 1
2 log x
 ) < π(x) < x
log x
(1 + 3
2 log x
), x ≥ 59.

due to Rosser and Schoenfeld [62]. Some further examples can be found in Section 8.2.
The reason why sharp estimates of π(x) and of related prime counting functions are so
important is that many problems in number theory use them as input. There are plenty of
number theoretical problems where one comes to a solution only on assuming that a sharp
estimate for π(x) is available, an estimate we cannot currently prove, but which we could
if we knew that the Riemann Hypothesis (RH) holds true (we will come back to this
shortly). Under RH it can be shown that for every x > 2 657 we have

|π(x) − Li(x)| < 1
8π √x log x. (1)

This is a sharp inequality as the estimate π(x) = Li(x) + O(
√x/ log x) does not hold
[67]. The latter result says that the primes do behave irregularly to some extent. The
importance of the RH is that if true it would imply that we can very well approximate

4Jacques Salomon Hadamard (1865 Versailles, France – 1963 in Paris, France), French mathematician,
professor at the University of Bordeaux, Coll`ege de France, ´Ecole Polytechnique and ´Ecole Centrale.
5Charles Jean Gustave Nicolas Baron de la Vall´ee-Poussin (1866 Leuven, Belgium – 1962 Leuven,
Belgium), Belgian mathematician, professor at Catholic University of Leuven, Coll`ege de France and
Sorbonne.
6August Leopold Crelle (1780 Eichwerder, Germany – 1855 Berlin, Germany), German mathematician,
founder of Journal f¨ur die reine und angewandte Mathematik.
7Johann Martin Zacharias Dase (1824 Hamburg, Germany – 1861 Hamburg, Germany), German arith-
metician, having great calculating skills, but little mathematical knowledge.
8Jakob Philipp Kulik (1793 Lemberg, Austrian Empire – 1863 Prague, Bohemia), Polish-Austrian math-
ematician, professor at the Charles University of Prague.
9Adrien-Marie Legendre (1752 Paris, France – 1833 Paris, France), French mathematician and author
of an inﬂuential number theory book.

PRIME NUMBERS AND RIEMANN ZEROS 3

π(x) by the simple function Li(x), which makes proving results involving primes in general
much easier.
The sharpest estimates to date for π(x) are obtained by using properties of the so-called
Riemann zeta function, deﬁned by

ζ(s) =
 ∞∑

n=1
 1
ns , (2)

with s a complex number having real part Res > 1, see [60]10. The function converges
for all complex numbers s such that Res > 1. In 1859 a renowned G¨ottingen professor,
Riemann
11, published “ ¨Uber die Anzahl der Primzahlen unter einer gegebenen Gr¨osse”.
This paper
12 is without doubt the most important paper ever written in analytic number
theory; indeed it is foundational as Riemann makes essential use of s being a complex
variable, whereas a century earlier Euler13 only considered ζ(s) for real values of s14. That
Riemann considered his zeta function as an analytic function comes as no surprise as the
development of complex analysis was one of his central preoccupations. He brought the
study of π(x) to a completely new level, but actually proved little as the tool he used,
complex function theory, did not have on a ﬁrm theoretical foundation at the time. It took
about 40 years and a lot of preliminary work, mainly by Cahen, Halphen and Phragm´en
(see, e.g., [51] for more details), before the PNT could be ﬁnally proved using methods of
complex function theory. A tremendous amount of work was carried out by Landau
15, who
went meticulously through all earlier relevant work on this subject, checked its correctness,
simpliﬁed it16 and wrote a standard work on prime number theory in 1909 [44, 45]
17. He
himself proved many important results as well, such as the prime ideal theorem (see Section
9.2).
A lot of eﬀort was put into proving results about prime numbers without using com-
plex analysis. The most celebrated results were obtained by Selberg18 (and, more or less,
independently) by Erd˝os. They based themselves on the identity, now called Selberg’s

10The imaginary part of s will be denoted by Ims.
11Georg Friedrich Bernhard Riemann (1826 Breselenz, Hanover – 1866 Selasca, Italy), German mathe-
matician, student of Gauss, professor at G¨ottingen University.
12This only 9-pages-long paper, it is the only published work of Riemann on number theory.
13Leonhard Euler (1707 Basel, Switzerland – 1783 St. Petersburg, Russian Empire), extremely proliﬁc
Swiss mathematician, student of Johann Bernoulli.
14For more on Euler’s work on ζ, see Ayoub [1].
15Edmund Georg Hermann Landau (1877 Berlin, Germany – 1938 Berlin, Germany), German mathe-
matician, student of Frobenius, professor at G¨ottingen University.
16He gave a much simpler proof of the PNT, for example.
17H. Montgomary and R. Vaughan, both non-Germans, studying the original German version, were
surprised to learn about a very strong mathematician called Verfasser they had never heard of (Verfasser
means author...).
18Atle Selberg (1917 Langesund, Norway – 2007 Princeton, the US), Norwegian mathematician, profes-
sor at Princeton University, recipient of the Fields Medal (1950) and the Abel Prize (2002).

4 P. MOREE, I. PETRYKIEWICZ, AND A. SEDUNOVA

symmetry formula,
∑

p≤x log2 p + ∑

p,q≤x log p · log q = 2x log x + O(x),

and used it to obtain an elementary proof of the PNT. Until 1950 it was widely believed
(e.g., by Landau) that no such elementary proof could be developed and so this result
greatly impressed the contemporaries. Later Selberg extended this combinatorial technique
to show the PNT for primes in arithmetic progression, see [68]. For a nice survey see
Diamond [18]. Unfortunately, the high hopes placed in new insights coming from ﬁnding
an elementary proof of PNT were thwarted.
The level of insight that Riemann had reached was ﬁnally surpassed by Hardy and
Littlewood in the 1920’s. As far as his zeta function is concerned, Riemann was certainly
more than half a century ahead of his time!
Using partial integration it is easy to deduce that for Res > 0 an analytic continuation
of ζ(s) is given by
 ζ(s) = s
s − 1 − s ∫ ∞

1
 t − ⌊t⌋
t1+s dt, (3)

with ⌊t⌋ being the ﬂoor function. Another analytic continuation is obtained on noting that
for Res > 1 we have
 (1 − 2
1−s)ζ(s) =
 ∞∑

n=1(−1)
nn
−s. (4)

Since the right hand side actually converges for Res > 0, the identity furnishes an analytic
continuation for all Res > 0.
In his paper, Riemann showed that the zeta function actually has an analytic continua-
tion to the whole complex plane, except for a simple pole at s = 1, and that it vanishes at
all negative even integers. The trivial zeros of ζ(s) are the ones at negative even integers,
the non-trivial zeros come from complex numbers s = σ + it with 0 ≤ σ ≤ 1. The zeta
function satisﬁes the functional equation

Γ (s/2) π−s/2ζ(s) = Γ ((1 − s)/2) π(s−1)/2ζ(1 − s), (5)

where Γ(z) = ∫ ∞
0 t
z−1e
−tdt for Rez > 0 denotes the Gamma function (a continuous
extension of the factorial function
19). This function is never equal to zero, and is holo-
morphic everywhere except at the points 0, −1, −2, . . . , where it has simple poles.
It turns out that Γ(s/2)π−s/2ζ(s) has a simple pole at both s = 0 and s = 1. This
suggests that we should multiply it by s(s − 1). In this way we obtain the Riemann
ξ-function. It is an entire function whose zeros ρ are the non-trivial zeros of ζ(s). Note
that we can rewrite (5) as ξ(s) = ξ(1 − s).

19If n is a non negative integer, then, e.g., Γ(n + 1) = n!. For this reason some authors write Γ(z + 1)
instead of Γ(z).
 PRIME NUMBERS AND RIEMANN ZEROS 5

We have the following Hadamard factorisation of ξ:

ξ(s) = s(s − 1)Γ(s/2)π−s/2ζ(s) = ξ(0) ∏

ρ (1 − s/ρ) es/ρ,

where here (and in the sequel) the zeros ρ are counted with their own multiplicities, e.g.,
a double zero is counted twice.
Riemann gave two beautiful proofs of the functional equation; one is related to the theory
of modular forms and makes use of the transformation property Ω(x) = x−1/2Ω(x−1), valid
for all positive x, with
 Ω(x) =
 ∞∑

n=−∞ e−n2πx,

while the second proof uses the integral representation (18) from Section 4. Note that if ρ is
a non-trivial zero, then so is 1 − ρ by the functional equation. Moreover, since ζ(s) = ζ(s),
we deduce that ρ and 1 − ρ are also zeros. Thus the zeros are symmetrically arranged
about the half line (also called the critical line) given by Res = 1/2 and also about the
real axis. Therefore we often only calculate the zeros in the upper half plane. Riemann
shows that the non-trivial zeros lie in the critical strip20, the strip 0 ≤ Res ≤ 1, and,
furthermore, are not real. Moreover, he wrote that probably all its non-trivial zeros lie
on the half line and continues: “Certainly one would wish for a stricter proof here; I have
meanwhile temporarily put aside the search for this after some ﬂeeting futile attempts,
as it appears unnecessary for the next objective of my investigation.”
21 The Riemann
Hypothesis states that all non-trivial zeros (the zeros in the critical strip) of the zeta
function are on the half line. We call the zeros of ζ(s) on the half line critical zeros. If
in the rectangle deﬁned by 0 ≤ Res ≤ 1 and 0 ≤ Ims ≤ T there are only critical zeros, we
say that RH up to height T holds true.
Solving RH is one of the famous 23 problems posed by Hilbert at the 1900 International
Congress of Mathematicians in Paris. These problems held their fascination and inﬂuence
on the developments through the twentieth century [17]. Resolving RH is one of seven
Millennium Prize Problems that were stated by the Clay Mathematics Institute in 2000.
A correct solution to any of the problems results in a 1 000 000 dollar prize being awarded
by this institute [8]. Many mathematicians regard RH as the biggest open problem in all
of mathematics.
The behaviour of ζ(s) in the critical strip is very closely related to the distributional
properties of the primes. The uniqueness of prime factorization ﬁnds its analytic counter-
part in the identity
 ζ(s) = ∏

p (1 − p−s)
−1, Res > 1, (6)

20In this strip formula (2) for ζ(s) does not apply, but formula (3) and (4) do.
21Hiervon w¨are allerdings ein strenger Beweis zu w¨unschen; ich habe indess die Aufsuchung desselben
nach einigen ﬂ¨uchtigen vergeblichen Versuchen vorl¨auﬁg bei Seite gelassen, da er f¨ur den n¨achsten Zweck
meiner Untersuchung entbehrlich schien. [60] Translation: David R. Wilkins.

6 P. MOREE, I. PETRYKIEWICZ, AND A. SEDUNOVA

x π(x) Li(x) − π(x) R(x) − π(x)
10
8 5 761 455 754 97
10
9 50 847 534 1 701 −79
1010 455 052 511 3 104 −1 828
1011 4 118 054 813 11 588 −2 318
1012 37 607 912 018 38 263 −1 476
1013 346 065 536 839 108 971 −5 773
1014 3 204 941 750 802 314 890 −19 200
1015 29 844 570 422 667 1 052 619 73 218
1016 279 238 341 033 925 3 214 632 327 052
1017 2 623 557 157 654 233 7 956 589 −598 255
1018 24 739 954 287 740 860 21 949 555 −3 501 366
Table 1. The values of π(x) compared with values of Li(x) and R(x).

which was established by Euler for real s. Indeed, to become an inhabitant of the Zeta Zoo
(Section 9.2) an analytic function f (s) needs to have a factorization of the form ∏
p fp(s).
A formula of this type is now called an Euler product.
Thus the fact that ζ(s) tends to inﬁnity if one approaches s = 1 from the right over the
real axis
22 ensures by (6) that there are inﬁnitely many primes p. This was discovered in
1737 by Euler who established the stronger result that ∑

p p−1 is unbounded
23. It turns out
that, in order to prove the PNT, it is enough to show that there are no zeros on the line
Res = 1. The connection between the non-trivial zeros and the prime numbers is actually
much closer than this. Indeed, it can be shown that

π(x) = R(x) − ∑

ρ R(xρ), (7)

where the sum is over all the non-trivial zeros ρ (counted with multiplicities) and

R(x) =
 ∞∑

n=1
 µ(n)
n Li(x1/n) (8)

denotes the Riemann function and µ the M¨obius function (see Section 8.4). Using
Gram’s (1893) quickly converging power series

R(x) = 1 +
 ∞∑

n=1
 1
nζ(n + 1) (log x)
n

n! ,

the Riemann function is computable. Two further expressions for R(x) were found by
Ramanujan. He independently discovered the importance of R(x) (around 1910) and
developed a prime number theory that, as Hardy phrased it, was ”what the theory might
be if the zeta-function had no complex zeros”.

22Indeed, the Riemann zeta function has a simple pole with residue 1 at s = 1.
23Gauss in 1796 conjectured, and Mertens proved in 1874 the stronger result that ∑
p≤x p−1 = log log x+
C + o(1), with C a constant.
 PRIME NUMBERS AND RIEMANN ZEROS 7

It turns out that, from a theoretical perspective, it is better to work with certain
weighted prime counting functions rather than with π(x) (that is, each prime p is counted
with a weight w(p)). The most well-known of these are ϑ(x) = ∑

p≤x log p and ψ(x) =
∑

pm≤x log p, where the sums are taken over all primes, respectively all prime powers less
than x. The ﬁrst function is known as the Chebyshev ϑ-function, the second one as the
Chebyshev ψ-function
24. One often sees the ψ-function deﬁned as ψ(x) = ∑
n≤x Λ(n),
where Λ(n), the von Mangoldt function, equals log p if n is a power of a prime p and
zero otherwise. This function is more natural than it appears at ﬁrst sight, since logarith-
mic diﬀerentiation of the Euler identity (6) yields −ζ ′/ζ(s) = ∑∞
n=1 Λ(n)n
−s for Res > 1.
The quotient ζ ′/ζ has simple poles in the zeros of ζ and plays an important role in prime
number theory.
The complicated explicit formula (7) for π(x) takes a much easier form for ψ(x). This
result is called the “explicit formula” and due to von Mangoldt25. He showed in 1895 that
for x > 1 and x not a prime power we have

ψ(x) = x − ∑

ζ(ρ)=0
 xρ

ρ − ζ ′(0)
ζ(0) , (9)

where the sum on the right-hand side is over all zeros (also the trivial ones!) of the Riemann
zeta function. The explicit von Mangoldt formula was vastly generalized by Andr´e Weil.
His explicit formula works for a large class of test functions. The summation over the
roots involves the test function and this then equals a sum over the primes involving the
Fourier transform of the test function. On choosing a suitable test function (depending on
the problem one studies), Weil’s explicit formula has actually become an important tool
in computational prime number theory.
Note that |xρ| = xReρ and consideration of the explicit formula suggests that lim sup Reρ
determines the error term. Due to the existence of critical zeros, the minimum possible
value of the latter quantity is a half. We have lim sup Reρ = 1/2 if and only if the RH
holds true26.
Note that if the ∑ 1/|ρ| were to be bounded, with ρ ranging over all critical zeros, then
it would follow from (9) that on RH we have ψ(x) = x + O(
√x). However, this sum does
not converge, but a slightly weaker result is true, namely
∑

Ims≤T
 xρ

|ρ| = O(xα log2 T ),

with α any number such that there are no zeros ρ with Reρ > α. Using the latter approx-
imation with α = 1/2 it can be shown that the RH is equivalent with

ψ(x) = x + O(x1/2 log2 x). (10)

24It is easy to see that ψ(x) is the logarithm of the least common multiple of the integers 1, 2, . . . , [x].
25Hans Carl Friedrich von Mangoldt (1854 Weimar, Duchy of Saxe-Weimar-Eisenach – 1925 Danzig-
Langfuhr, Free City of Danzig), German mathematician, student of Kummer and Weierstrass, professor
at Hanover University and Technical University of Aachen.
26Recall that if ρ is a zero, so is 1 − ρ.

8 P. MOREE, I. PETRYKIEWICZ, AND A. SEDUNOVA

By the same argument it can be unconditionally shown that ψ(x) = x + O(xκ log2 x) with
κ = lim sup Reρ.
The analogue of (10) for π(x) is due to von Koch, who showed in 1901 that the RH is
equivalent to the formula

π(x) = Li(x) + O(E(x)), E(x) = x1/2 log x. (11)

As in the error term in (10), the 1/2 in the error term E is directly related to the half line:
if we would have a zero oﬀ the half line, it always has a related zero s0 having Res0 > 1/2
and the estimate (11) with E(x) = xRes0−ε is false. Indeed, more generally, the larger the
area inside the critical strip where we can show there are no zeros, the smaller we can take
E(x) in (11). Quite a bit of computational work was done on determining an explicit zero
free region that is as large as possible, e.g., Kadiri [39] showed that

Res ≥ 1 − 1
R0|Ims|, |Ims| ≥ 2, R0 = 5.69693,

is a zero free region. Already in 1899 de la Vall´ee-Poussin had established the above
result with diﬀerent constants. He showed that his zero free region leads to E(x) =
exp (−c√log x), with some positive constant c. It implies that for every ﬁxed r > 1 we
have E(x) = x(log x)−r. This function is far from behaving like √x. Indeed, it would be
an astounding result if somebody could prove that E(x) = xα, for some α < 1. Despite
great eﬀort by many number theorists, the above result of de la Vall´ee-Poussin has not
been much improved.
As we have seen a prime number heuristic that works well is to assume that n is a prime
with probability 1/ log n. Riemann’s research leads one to replace this by a more accurate
heuristic, namely that the average value of Λ(n) equals 1. This leads us to expect that,
e.g., ψ(x) ∼ x, which is the PNT in a diﬀerent guise
27. Indeed, by elementary arguments
it can be shown that the assertions

π(x) ∼ x
log x , ϑ(x) ∼ x, ψ(x) ∼ x,

are all equivalent and so are three diﬀerent guises of the PNT.
More interesting is to consider Π(x) = ∑
n≤x Λ(n)/ log n. Here our heuristic suggests
that
 Π(x) =
 ∞∑

k=1
 π(x1/k)
k ≈ ∑

n≤x
 1
log n ≈ Li(x). (12)

By M¨obius inversion we obtain from this the heuristic π(x) ≈ R(x), with R(x) the Rie-
mann function. This approximation is excellent, as shown in Table 1.
From the papers Riemann left us, it transpires that his computational skills were amaz-
ing and that he (being a perfectionist) kept a lot of his ﬁndings up his sleeve
28. In a
letter to Weierstrass from 1859 Riemann mentioned that he discovered new expansions

27Recall that ψ(x) = ∑

n≤x Λ(n).
28Unfortunately a lot of his notes were burnt after his death by his housekeeper. A true treasure trove
that went up in cinders!
 PRIME NUMBERS AND RIEMANN ZEROS 9

n zero n zero n zero
1 14.1347 6 37.5862 11 52.9703
2 21.0220 7 40.9187 12 56.4462
3 25.0109 8 43.3271 13 59.3470
4 30.4249 9 48.0052 14 60.8318
5 32.9351 10 49.7738 15 65.1125
Table 2. The ﬁrst ﬁfteen zeros of ζ rounded to four decimal places.

for ζ. At the turn of the 20th century many people tried to ﬁnd these expansions in the
unpublished notes of Riemann in the G¨ottingen library. Meanwhile in England, Hardy
29

in the early 1920’s, together with his lifelong collaborator Littlewood,
30 found “an approx-
imate functional equation” [28, 29]. However, a librarian in G¨ottingen discovered that
this approximate formula was already known to Riemann. Moreover, whereas Hardy and
Littlewood had determined the dominating term only, Riemann had a method to estimate
the remainder term. In 1926, while in G¨ottingen, Bessel-Hagen31 discovered a previously
unknown approximate formula in Riemann’s notes. Siegel
32 then analysed the notes with
these two approximate formulas, working out the details,
33 and in 1932 published them.
One of these is now known as the Riemann-Siegel formula. This formula is still used
in calculating the zeros of the Riemann zeta function, see Section 4 for more details.
Over time mathematicians calculated non-trivial zeros in the hope of disproving the
Riemann Hypothesis (like Turing) or to ﬁnd evidence for it. At present, more than 100
billion zeros have been veriﬁed to be critical; for example, Gourdon in 2004 veriﬁed that
the ﬁrst 1013 zeros are critical (see [23]); moreover, Odlyzko calculated 10 billion zeros near
10
22 and showed that they all are critical, [52]. The ﬁrst ﬁfteen zeros are listed in Table 2.
The number of non-trivial zeros computed by the various dramatis personae can be found
in Table 4.
The problem of calculating non-trivial zeros can be divided into three challenges. First
of all given s ̸= 1, one wants to be able to compute ζ(s) with prescribed precision. Secondly
one wants to locate the critical zeros, the zeros on the half line, up to a prescribed height
T . Finally, one wants to show that RH holds true up to a prescribed height T . The latter
challenge necessitates being able to calculate the total number of zeros in the critical strip

29Godfrey Harold Hardy (1877 Cranleigh, England – 1947 Cambridge, England), English mathemati-
cian, professor at the University of Cambridge.
30John Edensor Littlewood (1885 Rochester, England – 1977 Cambridge, England), British mathemati-
cian, professor at the University of Cambridge.
31Erich Paul Werner Bessel-Hagen (1898 Berlin, German Empire – 1946 Bonn, Germany), German
mathematician, student of Carath´eodory, professor at the University of Bonn.
32Carl Ludwig Siegel (1896 Berlin, German Empire – 1981 G¨ottingen, West Germany), German math-
ematician, student of Landau, professor at the University of Frankfurt and G¨ottingen.
33Diese Gr¨unde machten eine freie Bearbeitung des Riemannschen Fragmentes notwendig, wie sie im
folgenden ausgef¨uhrt werden soll. [69]

10 P. MOREE, I. PETRYKIEWICZ, AND A. SEDUNOVA

up to height T and comparing this with the number of critical zeros found.
These three challenges are addressed in the following sections.

1. Euler-Maclaurin formula

The ﬁrst important result on computing non-trivial zeros dates back to 1903, when
Gram
34 published a paper with a list of approximate values of 15 non-trivial zeros and the
proof that RH is true up to height 50 [24]. He used the Euler-Maclaurin summation
formula, a method originating in the 18th century to evaluate sums, which describes how
good an approximation of a sum is obtained by replacing it by the corresponding integral
[77, Chapter 4]. A few years before the publication of his paper, he tried a more elaborate
method to compute non-trivial zeros; however, he gave up due to the sheer complexity of
the calculations hoping that someone else would discover a better way35. Nobody managed
to obtain the desired results and after 8 years Gram resumed the work on the numerical
estimations of non-trivial zeros. He tried a ”na¨ıve approach”, which, to his surprise, worked
well
36. Gram applied the Euler-Maclaurin summation formula to ∑∞
j=n j−s and, evaluating
it at s = 1/2 + it, obtained the (exact), but not absolutely converging, series expansion

ζ(s) =
 n−1∑

j=1 j−s + n−s

2 + n1−s

s − 1 +
 ∞∑

k=1 Rk,n(s), (13)

with
 Rk,n(s) = B2k
(2k)! n
1−s−2k 2k−2∏

j=0 (s + j),

where Bk denotes the k-th Bernoulli number37. In order to approximate ζ(s) one chooses
an appropriate m, computes the Rk,n terms up to this m and estimates the remainder by
∣
∣
∣
∣
∣
 ∞∑

k=m+1 Rk,n(s)

∣
∣
∣
∣
∣ < ∣
∣
∣
∣ s + 2m + 1
Res + 2m + 1 Rm+1,n(s)∣
∣
∣
∣ .

Gram observed that, in order to calculate any zero with 0 < Ims < 50 to 7 decimal
places, we can take n = 20. In general, the number n of terms needed to be calculated in
(13) in order to obtain an estimation of ζ(s) up to reasonable precision grows linearly with

34Jørgen Pedersen Gram (1850 Nustrup, Denmark – 1916 Copenhagen, Denmark), Danish mathemati-
cian, actuary.
35Ces diﬃcult´es m’ayant paru insummontables `a moins de calculs immenses, j’abandonnai ces recherches
en esp´erant qu’un autre trouverait quelque m´ethode pouvant servir soit au calcul des coeﬃcients de ξ(t)
soit au calcul direct des racines α. Mais, autant que je sache, aucune m´ethode de ce genre n’a encore ´et´e
publi´ee. [24]
36N´eamoins l’automne dernier je me suis d´ecid´e `a faire cet essai, et j’ai ´et´e frapp´e de la facilit´e avec
laquelle il a r´eussi. [24]
37Bernoulli numbers can be deﬁned recursively: B0 = 1 and Bm = − ∑m−1
k=0 (m
k ) Bk
m−k+1 , or as coeﬃcients
of the generating exponential function x
ex−1 = ∑∞
n=0 Bnxn

n! .

PRIME NUMBERS AND RIEMANN ZEROS 11

Ims. Later Backlund38 provided good bounds for the size of the estimation error for this
method in terms of n, m and s.
This approach is simple and the computational work is proportional to Ims. However,
in practice, it is only eﬃcient to evaluate zeros with small imaginary part. In Sections 4,
5 and 6 we will present more eﬃcient algorithms to approximate ζ(s).

2. Gram test

Now that we are able to compute ζ(s) with arbitrary precision, the next challenge is to
locate Riemann’s zeros. Consider the Hardy Z-function
39

Z(t) = eiθ(t)ζ ( 1
2 + it
) , (14)

where
 θ(t) = Im log Γ ( it
2 − 3
4
 ) − t
2 log π. (15)

(Recall that Γ denotes the Gamma function.) The function Z(t) is a real-valued function
and Z(t) = 0 if and only if ζ ( 1
2 + it) = 0. Thus we can detect critical zeros by ﬁnding
intervals where Z changes sign and then applying Newton’s method. In particular, we
can compute θ(t) and ζ ( 1
2 + it) and then look at the sign change. On using well-known
asymptotic estimates for the Γ-function we ﬁnd the asymptotic formula

θ(t) = t
2 log ( t
2πe
) − π
8 + 1
48t + O ( 1
t3
 ) .

Alternatively, we could consider Reζ and Imζ separately. We ﬁrst observe that ζ (1/2 + it) =
Z(t) cos θ(t) − iZ(t) sin θ(t). Then we note that Imζ changes sign if either Z(t) or sin θ(t)
changes sign. The function θ(t) is increasing for t ≥ 10, therefore between consecutive zeros
of sin θ(t) there is exactly one zero of cos θ(t) and so cos θ(t) changes sign. It follows that,
if Reζ(1/2 + it) = Z(t) cos θ(t) is positive at two consecutive zeros z1 < z2 of sin θ(t), then
Z must change sign in the interval I = [1/2 + iz1, 1/2 + iz2] and hence there is a zero of Z
(and hence a critical zero) in the interval I. Thus it is important to locate those t for which
sin θ(t) = 0. These points are called Gram points. To be precise, the n-th Gram point
gn is deﬁned as the unique solution to θ(gn) = nπ, gn ≥ 10. We conclude that, as long as
ζ (1/2 + ign) > 0, there is at least one critical zero in the interval (1/2 + ign−1, 1/2 + ign).
Checking if ζ (1/2 + ign) > 0 at a Gram point gn is called the Gram test.
In 1925 Hutchinson
40 [35], using Gram point computations, showed that RH holds up
to height T = 300. He found two empty Gram intervals, but since the neighbouring Gram
interval in each case contained two zeros, he could overcome this defect.

38Ralf Josef Backlund (1888 Pietarsaari, Finland – 1949 Helsinki, Finland), Finnish mathematician,
actuary, student of Lindel¨of; shortly after obtaining his PhD, he quit academia to work for an insurance
company; he was one of the founders of the Actuarial Society of Finland.
39The ﬁrst to work with this function was Riemann, not Hardy.
40John Irwin Hutchinson (1867 Bangor, the US – 1935), American mathematician, student of Bolza,
professor at Cornell University.

12 P. MOREE, I. PETRYKIEWICZ, AND A. SEDUNOVA

3. Total number of zeros up to a given height

Suppose that we have localized the zeros on the half line for all 0 < |Im(s)| < T . We
would like to prove the RH up to height T . Already Gram showed that

log ξ ( 1
2 + it) = log ξ ( 1
2
 ) − t
2 ∑

Reγ>0 γ−2 − t
4

2
 ∑

Reγ>0 γ−4 − . . . ,

where the sum is over the zeros ρ of ξ written in the form 1/2 + iγ. From this identity
he could evaluate ∑
Reγ>0 γ−2n very precisely. Since ∑
Reγ>0 γ−2n is dominated by the ﬁrst
few terms, he compared the estimated term ∑ γ−10 to the ﬁnite sum evaluated for the the
15 zeros found on the critical line. He then concluded that RH holds up to height T = 50.
For more zeros the calculations became too involved.
Let N (T ) and N0(T ) denote the number of zeros, respectively critical zeros, of ζ(s) with
0 < Ims < T counted with multiplicities. Von Mangoldt (1905) showed that

N (T ) = T
2π log T
2πe + O(log T ). (16)

Put
 S(T ) = 1
π Im ∫

Cε
 ζ ′(s)
ζ(s) ds, (17)

where Cε is the path
41 consisting of the segment from 1 + ε to 1 + ε + iT and that from
1 + ε + iT to 1/2 + iT . Backlund, basing himself on Riemann’s ideas, showed in 1912 that

N (T ) = θ(T )
π + 1 + S(T ).

Moreover, if Reζ is not zero on Cε, then N (T ) is the nearest integer to θ(T )/π + 1, i.e.

|S(T )| ≤ 1
2 .

Backlund [2, 3] himself proved that N (200) = 79 and, using Gram’s approach, showed that
all these zeros lie on the half line. Hutchinson also used this method to show that there
are no more zeros with 0 < Im(s) < 300 other than the ones he found. The problem with
the approach of Backlund is to ﬁnd a T such that Reζ is non-zero on C. This is a diﬃcult
task. Even worse is the fact that S(T ) can get arbitrarily large, so that inﬁnitely often one
will pick a T for which |S(T )| > 1/2. For these two reasons, nowadays a better method
developed by Turing half a century later is used (see Section 5).
We note that the above approach to verify the RH numerically up to a certain height
will fail if zeta has zeros that are not simple. It is conjectured that actually the Riemann
zeta function has only simple zeros. The reader might regard this as wishful thinking,
but Random Matrix Theory, in particular Montgomery’s pair correlation conjecture, see
Section 9.4, strongly suggests that all the zeros are simple. It is also a numerical observation
that the critical zeros ‘repel’ each other.
We would like to conclude this section by recalling some major results involving N (T ),

41It is only a quarter rectangle and this is related to the four fold symmetry of the zeta roots.

PRIME NUMBERS AND RIEMANN ZEROS 13

see Karatsuba [40, Chapter 2] for an introduction. Hardy [26] was the ﬁrst to show that
there are inﬁnitely many critical zeros. Even more, in 1921 he showed with Littlewood
that N0(T ) ≥ c1T with c1 a positive constant and T ≥ 15. In 1942 Selberg showed that
a positive fraction of all non-trivial zeros are critical, that is that N0(T ) ≥ c2N (T ) with
c2 > 0. Selberg’s ideas lead to a tiny value of c2 of about 7 · 10
−8 (as was worked out by S.
Min in his PhD thesis). In the mid 1970’s Levinson
42 caused a sensation by showing that
one can take c2 = 0.3474. It was later improved to 0.4088 by Conrey [9], 0.4105 by Bui,
Conrey and Young [7], and 0.4128 by Feng [22].

4. Riemann-Siegel formula

In 1932 Siegel [69] published the results on the Riemann zeta function found in the notes
of Riemann stored in the archives of the G¨ottingen University Library. The following
identity was discovered by Riemann. We start by showing the validity of the integral
representation
 ζ(s) = Γ(−s)
2πi
 ∫ +∞

−∞
 (−x)
s

ex − 1 dx
x , (18)

where the contour integral starts at +∞ and descends along the real axis, circulates 0 in
the positive direction and returns to +∞ up to the real axis. We can then evaluate the
integral in (18) in two ways: ﬁrstly by using the trivial identity

e
−N x

ex − 1 =
 ∞∑

n=N +1 e
−nx,

and secondly by changing the contour and applying the Cauchy residue theorem. We set
Res = 1/2 and arrive at

Z(t) = 2 ∑

n2<t/(2π)
 1
n1/2 cos(θ(t) − t log n) + R(t),

where Z(t) and θ(t) were deﬁned in (14) and (15) respectively.
The idea of the Riemann-Siegel method43 is to bound the remainder term R(t). In order
to determine the roots of the zeta function, we again use the function Z. Riemann, using
the saddle point method, found that

R(t) = (−1)
⌊√t/(2π)⌋−1 ( t
2π
 )−1/4 ( m∑

j=0 Cjt
−j/2 + Rm(t)),

with
 C0 = F (δ), C1 = −F (3)(δ)
23 · 3 , C2 = F (2)(δ)
24 + F (6)(δ)
27 · 32 ,

42Norman Levinson (1912 Lynn, the US – 1975 Boston, the US), American mathematician, professor
at MIT.
43For a derivation and more details see, e.g., [21, Chapter 7].

14 P. MOREE, I. PETRYKIEWICZ, AND A. SEDUNOVA

etc., and
 F (x) = cos (x2 + 3π/8)
cos (√
2πx
) , δ = √
t +
 (⌊√ t
2π
 ⌋
 + 1
2
 ) √
2π.

The error term Rm(t) satisﬁes the estimate Rm(t) = O(t
−(2m+3)/4). Explicitly estimating
the error term Rm(t) is unfortunately quite diﬃcult. Titchmarsh
44, a former student of
Hardy, proved in 1935 [72] that if t > 250π, then

|R0(t)| ≤ 3
2
 ( t
2π
 )−3/4

and used this estimate to verify RH up to height 390.

5. Turing’s method

After Siegel’s publication in 1932 of the Riemann-Siegel formula, Titchmarsh obtained
a grant for large scale computation of the non-trivial zeros. Making use of this formula,
tabulating machines and “computers” (as the mostly female operators of such machines
were called in those days), Titchmarsh established that the 1 041 non-trivial zeros up to
height 1 468 are all critical. Turing45, who from his student days onwards was interested
in the zeros of the Riemann zeta function, became interested in extending Titchmarsh’s
results. In his ﬁrst paper on this topic [74], he considered the Riemann-Siegel method,
but improved the estimate of Titchmarsh’s remainder term in such a way that it gives
satisfactory results for 30 < Ims < 1 000. However, the paper was rather technical, and,
within some years, better estimates were obtained. Turing designed and even started to
build a special purpose analog computer46 in order to verify the RH in the range 0 <
Ims < 6 000. The outbreak of the Second World War prevented him from completing the
construction of the machine. However, his attempts to build such a machine had set his
mind in motion about building computers and helped him later to build faster his famous
Bombes in order to break the Enigma Code. One can thus argue that many people thank
their lives to the critical zeros!
After the Second World War Turing returned to the problem of computing non-trivial
zeros. In his second paper on the zeros of ζ, he attempted to calculate the zeros of the
Riemann zeta function for large Ims, that is, for 1 414 < Ims < 1 540, in order to ﬁnd a
counterexample. He writes: The calculations were done in an optimistic hope that a zero
would be found oﬀ the critical line, and the calculations were directed more towards ﬁnding
such zeros than proving that none existed [75]. During this attempt to disprove the RH
he developed what is now called Turing’s method, a method to estimate the number of
non-trivial zeros up to a given height, which is still used today. In order to describe the
method, we need to go back to 1914, when Littlewood showed that, assuming the RH, the

44Edward Charles Titchmarsh (1899 Newbury, England – 1963 Oxford, England), British mathemati-
cian, student of Hardy, professor at the University of Oxford.
45Alan Mathison Turing (1912 London, England – 1954 Wilmslow, England), British pioneering com-
puter scientist, mathematician, student of Church.
46The blueprint of the machine is available at http://www.turingarchive.org/browse.php/C/2.

PRIME NUMBERS AND RIEMANN ZEROS 15

Algorithm Euler-Maclaurin Riemann-Siegel Odlyzko-Sch¨onhage
A O(N 2+ε) O(N 3/2+ε) O(N 1+ε)
B O(x2/3+ε) O(x3/5+ε) O(x1/2+ε)
C O(xε) O(xε) O(x1/4+ε)
Table 3. Comparison of diﬀerent algorithms.
A: Number of operations needed to verify the RH for the ﬁrst N zeros;
B: Number of operations needed to compute π(x);
C: Number of bits of storage needed to compute π(x).

diﬀerence π(x) − Li(x) changes sign inﬁnitely often(see also Section 8.3), thus extending
a result of Erhard Schmidt who had proved it, assuming the RH was false [47]. Turing
managed to exploit the result of Littlewood in order to average the value of

S(t) = N (t) − (θ(t)
π + 1)

over [0, T ]. He showed that S(t) tends to zero as t tends to inﬁnity. In particular, he
proved that, for h > 0 and T > 168π,
∣
∣
∣
∣
∫ T +h

T S(t)dt
∣
∣
∣
∣ ≤ 2.3 + 0.128 log T + h
2π .

If we calculate S(t) using the observed number of zeros N ′(t) instead of N (t) and we
missed k zeros, i.e., N ′(t) < N (t), then we would get that S(t) → −k, which eventually
contradicts the above estimate. What the method amounts to is the following. In order to
verify RH up to height T , one has to ﬁnd enough critical zeros up to height T + O(log T ).
For more details on Turing’s work on this subject, see for example [4], [13, 265–279].

6. Odlyzko-Sch¨onhage method

In 1988 Odlyzko
47 and Sch¨onhage
48 developed a diﬀerent approach to evaluate the Rie-
mann zeta function. In [53] they observed that the problem of evaluating sums of the form
∑M
k=1 dkk−it at an evenly spaced set of t’s can be transformed into a problem of evaluat-
ing a rational function of the form ∑n
k=1 ak(z − bk)
−1 at all n-th roots of unity using the
fast Fourier transform. The algorithm they designed rapidly evaluates such functions at
multiple values. In particular, they showed that, for any positive constants δ, σ, c1, there
exists an eﬀectively computable constant c2 and an algorithm which, for any T, computes
ζ(σ+it), T ≤ t ≤ T +T 1/2 to T −c1 precision in less than c2T δ operations (addition, subtrac-
tion, multiplication, division). The algorithm has no advantage over the Riemann-Siegel
method when a single value is evaluated, but it signiﬁcantly improves the veriﬁcation time
of the RH for the ﬁrst N zeros as shown in Table 3.

47Andrew Michael Odlyzko (1949 Tarn´ow, Poland), Polish-American mathematician, student of Stark,
professor at the University of Minnesota.
48Arnold Sch¨onhage (1934 Lockhausen, the Free State of Lippe), German mathematician, computer
scientist, student of Hoheisel, professor at the University of Bonn, the University of T¨ubingen and the
University of Konstanz.

16 P. MOREE, I. PETRYKIEWICZ, AND A. SEDUNOVA

Year Number of computed zeros Author
1859 ≥ 2 Riemann
1903 15 Gram
1914 79 Backlund
1925 138 Hutchinson
1935 1 041 Titchmarsh
1953 1 104 Turing
1956 25 000 Lehmer
1966 250 000 Lehman
1968 3 500 000 Rosser, Yohe, Schoenfeld
1979 81 000 001 Brent
1982 200 000 001 Brent, van de Lune, te Riele, Winter
1983 300 000 001 van de Lune, te Riele
1986 1 500 000 001 van de Lune, te Riele, Winter
2004 900 000 000 000 Wedeniwski
2004 10 000 000 000 000 Demichel, Gourdon
Table 4. Record history of calculating critical zeros.

7. A brief history of non-trivial zeros calculations

Riemann seems to have computed only a few non-trivial zeros. He certainly found zeros
at approximately 1/2 + i14.1386 and at 1/2 + i25.31, and very likely computed more. He
derived and tried to use the wonderful identity
∑

Imρ>0
 ( 1
ρ + 1
1 − ρ
 ) = 1 + γ
2 − log π
2 − log 2 = 0.02309570896612103381 . . .

to prove that the root at 14.1 is the ﬁrst root
49. The latter identity can be used to infer
that Reρ > 10 for the ﬁrst non-trivial zero. The decimals Riemann gave for the two roots
are slightly oﬀ, but the 20 decimals above he computed correctly!
In the earlier sections we reported about the computations and innovations due to Gram,
Backlund, Hutchinson, Titchmarsh and Turing. After Turing computers with every in-
creasing performance played a major role. At the beginning of the 21st century, large
scale computations were performed. Between 2001 and 2005 the project ZetaGrid, led by
Wedeniewski, was established. It involved distributed computation of the non-trivial ze-
ros. It ran on more than 10 000 computers in over 70 countries and was based on software
developed by van de Lune, te Riele and Winter [76] who after years of work eventually
computed the ﬁrst 1.5 · 10
9 Riemann zeros. More than 9 · 10
11 ﬁrst zeros were veriﬁed to lie
on the critical line. In 2004 Demichel and Gourdon, [23], performed the calculation of the
zeros using the Odlyzko-Sch¨onhage method to verify that the ﬁrst 10
13 lie on the critical
line. The calculation was not repeated though. Unfortunately, neither of the results was
published in a mathematical journal.
The above history is summarized in Table 4.

49The identity can be derived using the Hadamard factorization for ξ. Here γ denotes Euler’s constant.

PRIME NUMBERS AND RIEMANN ZEROS 17

8. Applications

In this section we give some applications of being able to determine many non-trivial
zeros with high precision, e.g., the determination of π(x) for very large x. The three
subsections that follow are about prime number inequalities; the ﬁrst one about inequalities
that hold true, and the other two about famous inequalities conjectured in the 19th century
that turn out to be too good to be true. The ﬁnal subsection is about the ternary Goldbach
conjecture, which was recently resolved using very extensive zero calculations of Dirichlet50

L-functions (that behave like ζ(s) in many respects).

8.1. The exact value of π(x). The record values for which π(x) has been exactly com-
puted are a good indicator for the progress in computational prime number theory. The
obvious way of computing π(x) is, of course, by counting all primes p ≤ x. For large
values of x this is quite ineﬃcient. In 1871 Meissel devised an ingenious method of com-
puting π(x) without computing all primes p ≤ x. This method requires only the knowl-
edge of the primes p ≤ √x, as well as the values of π(y) for some values of y ≤ x2/3.
In 1885 Meissel determined π(10
9) (albeit not quite accurately). The algorithm was
steadily improved and, e.g., in 2007 Oliveira e Silva used it to compute π(10
23). As-
suming RH in 2010 B¨uthe, Franke, Jost and Kleinjung announced a value of π(10
24).
Very recently by a diﬀerent method Platt [57], based on an explicit formula of Riemann
for the quantity on the left hand side of (12), managed to show unconditionally that
π(10
24) = 18 435 599 767 349 200 867 866, in agreement with the value of B¨uthe et al. This
computation rests on the ﬁrst 69 778 732 700 critical zeros computed with 25 decimal ac-
curacy. For the values of π(10
k) with 8 ≤ k ≤ 18 the reader is referred to Table 1.

8.2. Explicit prime number bounds. One of the most often quoted papers in compu-
tational number theory is the one by Rosser and Schoenfeld [62]. In this paper, among
other things, they prove the explicit bounds of π(x) that we mentioned in the introduction.
The importance of this paper is that their proof was based on verifying the RH up to a
certain height. Then using the fact that the ﬁrst 3 502 500 zeros of ζ lie on the critical
line, the authors together with Yohe found explicit bounds for the ϑ-function [63]. Let pn
denote the nth prime. Rosser and Schoenfeld obtained the estimates

n(log n + log log n − 3/2) < pn < n(log n + log log n − 1/2),

valid for every n ≥ 21. From this we deduce that pn > n log n for every n ≥ 1, a result
that had been obtained already in 1939 by Rosser [61]. Note that Table 1 suggests that
π(x) ≥ [x/ log x] for all x large enough. Indeed, Rosser and Schoenfeld in 1962 using
a delicate analysis established the truth of this inequality for x ≥ 17. Meanwhile most
explicit estimates of Rosser and Schoenfeld have been sharpened, e.g., by Dusart who
exploited the veriﬁcation of the RH for the ﬁrst 1.5 · 10
9 zeros [20].

50Johann Peter Gustav Lejeune Dirichlet, German mathematician (1805–1859), who gave his name to
the Dirichlet series; the Dirichlet theorem on primes in arithmetic progressions precedes by almost 70 years
the prime number theorem. He was the advisor of Bernhard Riemann.

18 P. MOREE, I. PETRYKIEWICZ, AND A. SEDUNOVA

A recent result from B¨uthe shows explicitly the connection between a partial RH and a
sharp prime number estimate. He proved that if the RH holds true up to height T , then
the estimate (1) holds true for all x satisfying 4.92x/ log x ≤ T .

8.3. Comparison of π(x) with Li(x). From Riemann’s formulae (7) and (8) it follows
that
 π(x) = Li(x) − Li(
√x)
2 − ∑

ρ Li(xρ) + W (x),

where W (x) relatively to the three earlier summands is of lower order. Riemann’s writings
suggest (he was rather vague about it) that he thought that the inequality

π(x) < Li(x) (19)

is always satisﬁed. Gauss and Goldschmidt had established the validity up to x = 10
5.
Today we know that it even holds up to x = 1014, cf. also Table 1. However, in 1914
Littlewood proved the spectacular result that the diﬀerence π(x) − Li(x) changes sign
inﬁnitely often. In the mid-1930s Ingham showed that this result follows from knowledge
of some initial non-trivial zeros51. His proof was both simpler and more explicit than
Littlewood’s, but also more computational. Let x0 be the smallest integer for which π(x0) >
Li(x0). Skewes showed that

x0 < 10
101034 (1933, on RH), x0 < 10
1010964 (1955, unconditionally).

For a long time these bounds of Skewes were considered to be the largest “naturally”
occurring numbers in mathematics.
Using tables of non-trivial zeros accurate to 28 digits for the ﬁrst 15 000 zeros and to
14 digits for the next 35 000 zeros, te Riele showed that (19) is false for at least 10 180
successive integers in [6.627·10
370, 6.687·10
370]. He made use of an earlier result of Lehman,
which allows one to put bounds on π(x) − Li(x), assuming that we have found all non-
trivial zeros to height T , and that RH is checked up to height T [46]. Lehman himself had
obtained x0 < 10
1166 using this result.
We now know that once (19) holds the wait until the inequality is reversed grows again,
on average, as a function of the starting x. Thus we should perhaps not be surprised that
the average of χ(t) with χ(t) = 1 if π(t) < Li(t) and χ(t) = 0 otherwise, does not exist.
However, under various plausible conjectures the density

δ = lim
x→∞ 1
log x
 ∫ x

1
 χ(t)
t dt

does exist and satisﬁes δ = 0.99999973 . . . (see [65]). This conjecturally quantiﬁes the
dominance of Li(x) over π(x). The strong bias towards Li(x) is an example of an interesting
phenomenon that is called Chebyshev’s bias (see Section 9.2).

51Subsequently, Turing whose initial interest was in improving the results of Skewes, turned his interest
to computing non-trivial zeros.

PRIME NUMBERS AND RIEMANN ZEROS 19

8.4. The Mertens conjecture. The Mertens function M (x) denotes the diﬀerence
between the number of squarefree integers n ≤ x having an even number of prime factors
and those having an odd number of prime factors. More formally, we have

M (x) = ∑

n≤x µ(n),

where µ(n) = 0 if a square exceeding one divides n and µ(n) = (−1)
m with m be-
ing the number of diﬀerent prime factors of n otherwise. The function µ is called the
M¨obius
52 function and outside number theory arises very frequently in combinatorial
counting (inclusion-exclusion). It is not diﬃcult to show that

1
ζ(s) =
 ∞∑

n=1
 µ(n)
ns = s ∫ ∞

1
 M (t)
t1+s dt,

from which one can infer that the RH is equivalent with |M (t)| = O(t1/2+ε). The PNT
is equivalent to M (x) = o(x). Most number theorists envision the Mertens function as
something like a random walk, with the ±1 contributions from µ to M (x) being close to a
random coin ﬂip. It is known by the probability theory that for the summatory function
w(x) = ∑

n≤x wn, with wn = ±1, randomly and independently, we have

lim sup
x→∞ w(x)
√
(x/2) log log x = 1.

This suggests that if µ is ”suﬃciently” random, then the ratio M (x)/
√x is expected to be
unbounded.
On the basis of numerical work Stieltjes53 in 1885
54 and independently Mertens
55 in 1897
[48], conjectured that |M (x)| < √x, a conjecture that is now known as the Mertens con-
jecture. Daublebsky von Sterneck56, earlier had made the stronger claim that |M (x)| <√x/2 for x > 200. That conjecture was disproved in 1963 by Neubauer. We now know
that 7 725 038 629 is the minimal integer > 200 for which the Daublebsky von Sterneck
bound does not hold. In 1983 Odlyzko and te Riele [54] caused a sensation by disproving
the Mertens conjecture. They showed that

lim sup
x→∞ M (x)
√x > 1.06, lim inf
x→∞ M (x)
√
x < −1.009,

52August Ferdinand M¨obius (1790 Schulpforta, Saxony – 1868 Leipzig, Germany), German mathemati-
cian and astronomer, student of Gauss and Pfaﬀ, professor at the University of Leipzig.
53Thomas Joannes Stieltjes (1856 Zwolle, the Netherlands – 1894 Toulouse, France), Dutch mathemati-
cian, professor at Toulouse University.
54In a letter to Hermite published only in 1905.
55Franz Carl Joseph Mertens (1840 Schroda, Prussia – 1927 in Vienna, Austria), Polish-German math-
ematician, student of Kummer and Kronecker, professor at Jagiellonian University in Cracow and the
University of Vienna.
56 Robert Daublebsky von Sterneck (1871 Vienna, Austria–1928 Graz,Austria), a student of F. Mertens.
He was born into a celebrated family belonging to the nobility. Later in life he was poor and only used
Sterneck as a last name.

20 P. MOREE, I. PETRYKIEWICZ, AND A. SEDUNOVA

without actually giving a speciﬁc integer x0 with |M (x0)| ≥ √x0. Later Kotnik and te
Riele [43] using very extensive computer calculations showed that there is an x0 < e
1.59·1040

for which the Mertens conjecture fails.
The ﬁrst step in disproving the Mertens conjecture is to ﬁnd the analogue of (9) for
M (x)/
√x. Assuming RH and that all critical zeros are simple this can be done. It
involves a sum having terms of the form e
iγy/(ρζ ′(ρ)), where ρ = 1/2 + iγ, x = e
y. Next,
one ﬁnds an upper bound for the error made on cutting this formula at a given height
T up to which one has veriﬁed RH numerically and computed the zeros with suﬃcient
numerical precision. In order to obtain the desired result, one needs to verify RH and the
simplicity of the zeros up to a height large enough. Secondly, we want each of the terms
to be close to its maximum, which happens when γy is close to an even integer. The latter
leads to a problem in simultaneous Diophantine approximation. Now the key factor that
allowed Odlyzko and te Riele to progress beyond earlier failed attempts to disprove the
Mertens conjecture, was using the at the time recently developed Lenstra-Lenstra-Lov´asz
algorithm, or LLL-algorithm for short. With the use of this new algorithm less extensive
computing was needed to reach rather stronger results than before. Indeed only the ﬁrst
2 000 non-trivial zeros calculated with circa 100 signiﬁcant decimal places, were used in
the disproof.

8.5. The ternary Goldbach conjecture. The Goldbach conjecture (formulated in
1742 in a letter to Euler) states that every even number exceeding 2 can be represented as
a sum of two primes. This is a very famous conjecture that remains unsolved. A weaker
variant is the ternary Goldbach conjecture, also known as odd or weak Goldbach
conjecture. It says that every odd number greater than 7 can be expressed as the sum of
three odd primes.
Hardy and Littlewood showed in 1923 that on GRH
57, the odd Goldbach conjecture
is true for all suﬃciently large odd numbers. In 1937, Vinogradov [78] established this
result unconditionally. Vinogradov used the circle method, which involves both minor
and major arc estimates. His student Borozdkin in his PhD thesis (unpublished), made
the suﬃciently large explicit, yielding a huge number eee41.96 and further published a re-
sult with the smaller bound e
e16.038, see [5]. In 1997, Deshouillers, Eﬃnger, te Riele and
Zinoviev published a result showing that GRH implies Goldbach’s weak conjecture [16].
This required checking all integers ≤ 10
20 as for all larger integers they could establish the
result by theoretical means. Without GRH it was known in 2002 that the 10
20 has to be
replaced by 101347. In 2012 and 2013, Helfgott released a series of preprints improving the
major and minor arc estimates suﬃciently to unconditionally prove the weak Goldbach
conjecture (see [31], [32], [33] and [34]). Helfgott made use of a result of Platt [58] who
had rigorously veriﬁed, using interval arithmetic, the RH for all Dirichlet L-functions for
modulus q ≤ 400 000 up to height around 108/q. The binary Goldbach conjecture is nu-
merically veriﬁed up to 4 · 10
18 by Oliveira e Silva, Herzog and Pardi [55].
The Goldbach conjecture is also studied in the ﬁeld of additive number theory, where

57Grand Riemann Hypothesis, see Section 9.2.

PRIME NUMBERS AND RIEMANN ZEROS 21

one considers a special set A (primes, squares, etc.) and then wonders what the sumset
A+A = {a+b : a, b ∈ A} looks like (similarly, with A+A+A, etc.). For a nice introduction
to additive number theory see the book by Tao and Vu [71].

9. Major recent developments

In this section we discuss some major more recent developments related to the Riemann
zeta function.

9.1. Complex analytic number theory. Riemann’s paper and, in its wake, the proof of
the PNT were a major achievement of 19th century mathematics and gave rise to complex
analytic number theory.
A function f from the natural numbers to the complex numbers is called an arithmetic
function. An important subclass are the multiplicative functions that satisfy f (1) = 1
and f (mn) = f (m)f (n) for arbitrary coprime natural numbers m and n (the M¨obius
function is an example of a multiplicative function). The behaviour of arithmetic functions
is usually very erratic. For that reason it makes sense to investigate related quantities that
show more regular behaviour, for example the summatory function ∑

n≤x f (n). The zeta
function reﬂex leads one to consider F (s) = ∑∞
n=1 f (n)n−s, which is called a Dirichlet
series. Using the Perron integral and assuming that F (s) converges absolutely for some
Res > σ one then ﬁnds that ∑

n≤x f (n) = ∫ c+i∞

c−i∞ F (s)xs

s ds,

with c > σ arbitrary and tries to estimate the integral. For this it is particularly important
to be able to shift the line of integration as far as possible to the left. Here it becomes
relevant to have an analytic continuation of F (s). The more one knows about F (s) the
more information one can deduce about f . However, often F (s) is not so well-behaved
and one tries to consider a closely related function f ∗ instead, with the property that its
Dirichlet series F ∗(s) behaves in a nicer way
58. The results one obtains in this way about
f ∗ one tries to relate back to f .
The attentive reader sees of course immediately that this whole approach is patterned
on Riemann’s 1859 paper.

9.2. The Zeta Zoo. The study of the Riemann zeta-function has proved so extraordinarily
successful in deepening our understanding of the primes, that it has become standard in
number theory to try to associate zeta type functions to arithmetic structures (some kind
of Pavlov reﬂex). Indeed, these days there is an enormous zoo of zeta functions. The
alpha animal in the Zeta Zoo was and still is zeta. It codiﬁes the behaviour of the integers
and their atomic constituents: the primes. An important species of zeta functions are the
Dirichlet L–functions. These were introduced by Dirichlet in order to understand the
behaviour of primes in arithmetic progression. Like zeta, they satisfy a product expansion,
a functional equation and it is conjectured that their zeros are also on the half line. The

58E.g., ∑ p
−s is not nicely behaved, but ∑ Λ(n)n−s is.

22 P. MOREE, I. PETRYKIEWICZ, AND A. SEDUNOVA

latter hypothesis is called the Extended Riemann Hypothesis (ERH). Again a lot of
computational number theory was done to verify RH for individual Dirichlet L–series 59 up
to a certain height and this was used to derive explicit bounds for π(x; d, a), with a and d
being coprime integers. These computations played an important role in the recent proof
of the ternary Goldbach conjecture by Helfgott (see Section 8.5). De la Vall´ee Poussin
(1897) proved that every of the arithmetic progressions a(mod d) with 1 ≤ a < d and a
and d coprime (of which there are ϕ(d)) gets asymptotically its fair share of the primes,
i.e., that asymptotically
 π(x; d, a) ∼ π(x)
ϕ(d).

In 1837 Dirichlet in a ground breaking paper (where he introduced characters in number
theory) had proved a weaker version of this result. Although the primes are asymptotically
equidistributed, they have some positive bias towards progressions modulo d where a is a
non-square modulo d. This was noted in 1853 by Chebyshev and is now known as Cheby-
shev’s bias. E.g., Bays and Hudson found in 1979 that 608 981 813 029 is the smallest
prime for which π(x; 3, 2) > π(x; 3, 1). For a nice introduction to this phenomenon see
Granville and Martin [25]. As in the π(x) versus Li(x) problem, under various assump-
tions there is a computable logarithmic measure for how often π(x; d, a1) > π(x; d, a2).
Another important class of zeta functions are the Dedekind zeta functions. This is
the analogue of the Riemann zeta function for a number ﬁeld and can be treated by similar
methods. E.g., Landau in 1903 showed the prime ideal theorem, stating that in a given
number ﬁeld the number of prime ideals of norm ≤ x grows asymptotically as x/ log x.
The hypothesis that every Dedekind zeta function has its non-trivial zeros on the critical
line is called the Grand Riemann Hypothesis (GRH).
The reader might wonder about a more stringent deﬁnition of a zeta function. Here is
what Selberg, with a life time of experience with zeta functions, thought about this.
A zeta function F (s) is a function of a complex variable s that satisﬁes the following
properties.

(1) Dirichlet series: for Res > 1, one can write F (s) = ∑∞
n=1 ann−s.
(2) Ramanujan hypothesis: the growth of the coeﬃcients an has to be modest, in
essence like that of the divisor function ∑

d|n 1.
(3) Analytic continuation: F (s) extends to a meromorphic function.
(4) Functional equation: there is ”a connection” between F (s) and F (1 − s).
(5) Euler product
60 one should be able to write F (s) = ∏
p Fp(s).

9.3. Correlation of pairs of non-trivial zeros. So far we exclusively focused on ﬁnd-
ing and counting non-trivial zeros. A reﬁnement is to ask about the distribution of the
zeros, e.g., how are the diﬀerences between (consecutive) zeros distributed? Here the ﬁrst

59A profound database can be found at http://www.lmfdb.org/.
60Patterned after Euler’s product formula (6).

PRIME NUMBERS AND RIEMANN ZEROS 23

theoretical work is due to Montgomery61 [50]. He assumed the RH and wrote the zeros as
1/2 + iγi with 0 < γ1 ≤ γ2 ≤ . . . To account for the increase of the density of the zeros as
one goes up the critical strip and rescales them as

γi = γi log(γi/(2πe))
2π .

By the asymptotic (16) for N (T ) it then follows that the mean spacing between two rescaled
consecutive zeros is 1. The pair correlation conjecture of Montgomery states that, with
0 ≤ α < β, we have, as M tends to inﬁnity,

1
M |{1 ≤ i < j ≤ M : γj − γi ∈ [α, β)}| ∼ ∫ β

α
 (1 − (sin(πt)
πt
 )2)dt.

The integrand here is small when t is close to zero, suggesting that the non-trivial zeros
repel each other. Montgomery proved a smoothened version of his conjecture and used it
to show that on the RH more than two thirds of the non-trivial zeros are simple.
Odlyzko numerically tested both this conjecture and the RH, beginning in the late 1980s.
In the 1990s this led to monumental computations where billions of zeros were computed
high up the critical strip. For a graphical demonstration of the computations, see Figure 1.

9.4. Random matrix theory. In 1972 Montgomery discussed his pair correlation con-
jecture with the physicist Dyson
62. Dyson immediately saw that the statistical distribution
found by Montgomery appeared to be the same as the pair correlation distribution for the
eigenvalues of a random Hermitian matrix that he had discovered a decade earlier.
Random matrix theory (RMT) was proposed by the physicist Eugene Wigner
63 in
1951 to describe nuclear physics. The quantum mechanics of a heavy nucleus is complex
and not well understood. Wigner made the bold conjecture that the statistics of the energy
levels can be captured by random matrices.
RMT turns out to be a powerful tool in making conjectures involving the Riemann zeta
and related functions. These conjectures lie typically way beyond the reach of current
theoretical tools. Since this is the case, doing numerical checks on the conjectures is very
important. These checks are often very computationally intensive.
As a very important example let us consider the problem of determining the even mo-
ments of the Riemann zeta function on the half line. We deﬁne

Ik(T ) = 1
T
 ∫ T

0 |ζ(1/2 + it)|
2kdt.

Progress on determining the moments was slow. Hardy and Littlewood [27] determined in
1916 the asymptotic behaviour of I1(T ). Ingham [36] improved this in 1926 in two ways,

61Hugh Lowell Montgomery (1944 Muncie, the US), American mathematician, student of Davenport,
professor at Michigan University.
62Freeman John Dyson (1923 Crowthorne, England), American physicist, professor at Princeton
University.
63Eugene Paul Wigner (1902 Budapest, Hungary – 1995 Princeton, the US), Hungarian-American
physicist and mathematician, Laureate of the Nobel Prize in Physics (1963).

24 P. MOREE, I. PETRYKIEWICZ, AND A. SEDUNOVA

normalized spacingdensity
0.0 0.5 1.0 1.5 2.0 2.5 3.00.00.20.40.60.81.01.2
Figure 1. Odlyzko’s pair correlation plot for 2 · 10
8 non-trivial zeros near
the 1023th zero. In the displayed interval, the data agrees with the pair
correlation conjecture to within about 0.002.

calculating the full asymptotic expansion when k = 1 and determining the leading term
for k = 2 (the lower-order terms for k = 2 were determined by Heath-Brown [30] in 1979).

PRIME NUMBERS AND RIEMANN ZEROS 25

It was conjectured for general k that

Ik(T ) ∼ f (k)a(k)
k2! T (log T )k2,

with a(k) a certain inﬁnite product over all primes and f (k) an integer. Hard grinding
analytic number theory led to the conjecture that f (3) = 42 [11] and f (4) = 24024 [12].
Progress beyond this seemed very challenging. Using RMT and modelling the zeros up to
height T with N by N matrices with N around log(T /2π), Keating and Snaith came with
a conjectural integer value for f (k) for all k. Their conjecture is consistent with all earlier
results and the conjectural values of f (3) and f (4) derived using hardcore analytic number
theory. Extensive numerical work corroborates the Keating and Snaith conjecture.
The RMT method oﬀers a dictionary that allows one to translate number theoretical
problems into random matrix problems that usually can be solved. However, there is no
proof whatsoever that the dictionary always works. As long as this is the case, computa-
tional number theoretical work will play a very important role. The work of Odlyzko [52]
on the zeros near 1022 is of enormous importance here, as the Riemann zeta function starts
showing “its true face” only for very large values of T .
The RMT method also works in the setting of function ﬁelds. These share many
similarities with the number ﬁeld setting, but often are easier to deal with. E.g., for them
the Riemann Hypothesis is proved! In this setting Katz and Sarnak actually managed to
prove various important results suggested by the RMT dictionary (published in their book
[41] and surveyed in [42]).
The quest for an explanation of the RMT connection is ongoing and has led to ac-
tive research at the intersection of number theory, mathematical physics, probability and
statistics.
 10. Words of warning

We hope that we have whetted the appetite of the reader to do computations in analytic
number theory him or herself. A word of warning is, however, not amiss. Asymptotic esti-
mates in analytic number theory often involve repeated logarithms. These are very diﬃcult
to detect by numerical computation. Thus a function that grows, e.g., like log log log x,
looks on a computer like a bounded function. For this reason it is highly dangerous to
make conjectures based on numerics alone (e.g., the Mertens conjecture), without some
theoretical and heuristic considerations supporting the truth of the conjecture.

11. Further reading

Nice popular introductions to prime number theory are Sabbagh [66] and du Sautoy [19].
Halfway between a popular and more mathematical treatment is an interesting collection of
prime number records and results modelled after the Guiness book of records [59]. For more
mathematical introductions see, e.g., [10, 15, 21, 37, 56]. In the book of Edwards64 there is
a detailed explanation of the method used by Gram, Backlund and Hutchinson to compute

64Warning: Edwards writes Γ(s + 1) instead of Γ(s).

26 P. MOREE, I. PETRYKIEWICZ, AND A. SEDUNOVA

the smallest 300 non-trivial zeros. More advanced books are Ivi´c [38] and Titchmarsh
[73]. The contribution of Hejhal and Odlyzko [13, 265–279] on the work of Turing on
the Riemann zeta function is very informative. Snaith [70] wrote a nice overview of the
connections between L-functions and random matrix theory, focusing on the example of
the Riemann zeta function. A very readable conference proceedings on this matter is [49].
Rubinstein’s beautiful article [64, pp. 633–679] also discusses RMT, but with main focus
on the inﬂuence of Riemann.
This survey owes a lot to the book of Narkiewicz [51] on the development of prime
number theory that provides a nice mix of mathematical ideas and historical material.
Also the book of Crandall and Pomerance [14] on computational prime number theory
turned out to be quite helpful.
Finally, in tune with the dictum of Edwards ”that one should read the masters and
beware of secondary sources”65, we would like to point out [6], which has many articles by
the Riemann zeta masters.
 12. Acknowledgement

The authors are enormously grateful to Alexandru Ciolan for his TEXnical assistance and
his excellent proofreading of the many earlier versions. Also they thank Alex Weisse for his
TEXnical assistance. Special thanks are due to Jan B¨uthe, Andreas Decker, Tomoko Kita-
gawa (alias Kate Kattegat), W ladys law Narkiewicz, Olivier Ramar´e, Michael Rubinstein,
Kannan Soundararajan, Caroline Turnage-Butterbaugh and Tim Trudgian.

References

[1] R. Ayoub. Euler and the zeta function. Amer. Math. Monthly, 81:1067–1086, 1974.
[2] R. J. Backlund. Einige numerische Rechnungen die Nullprodukte der Riemannschen ζ-Funktion be-
treﬀend. ¨Ofv. Finska Vet. Soc. Frh., 54(3):1–7, 1912.
[3] R. J. Backlund. Sur les z´eros de la fonction ζ(s) de Riemann. Comp. Rend. Acad. Sci., 158:1979–1981,
1914.
[4] A. R. Booker. Turing and the Riemann Hypothesis. Notices Amer. Math. Soc., 53(10):1208–1211,
2006.
[5] K. G. Borodzkin. On the problem of i. m. vinogradovs constant (in russian). Proc. Third All-Union
Math. Conf, 1, 1956.
[6] P. Borwein, S. Choi, B. Rooney, and A. Weirathmueller, editors. The Riemann hypothesis. CMS Books
in Mathematics/Ouvrages de Math´ematiques de la SMC. Springer, New York, 2008. A resource for
the aﬃcionado and virtuoso alike.
[7] H. M. Bui, B. Conrey, and M. P. Young. More than 41% of the zeros of the zeta function are on the
critical line. Acta Arith., 150(1):35–64, 2011.
[8] J. Carlson, A. Jaﬀe, and A. Wiles, editors. The Millennium Prize Problems. Clay Mathematics Insti-
tute, Cambridge, MA; American Mathematical Society, Providence, RI, 2006.
[9] J. B. Conrey. More than two ﬁfths of the zeros of the Riemann zeta function are on the critical line.
J. Reine Angew. Math., 399:1–26, 1989.
[10] J. B. Conrey. The Riemann Hypothesis. Notices Amer. Math. Soc., 50(3):341–353, 2003.
[11] J. B. Conrey and A. Ghosh. A conjecture for the sixth power moment of the Riemann zeta-function.
Internat. Math. Res. Notices, (15):775–780, 1998.

65Such as the present survey written by non-masters.

PRIME NUMBERS AND RIEMANN ZEROS 27

[12] J. B. Conrey and S. M. Gonek. High moments of the Riemann zeta-function. Duke Math. J.,
107(3):577–604, 2001.
[13] S. Cooper and J. van Leeuwen. Alan Turing: His Work and Impact. Elsevier Science, 2013.
[14] R. Crandall and C. Pomerance. Prime numbers. Springer, New York, second edition, 2005. A compu-
tational perspective.
[15] H. Davenport. Multiplicative number theory, volume 74 of Graduate Texts in Mathematics. Springer-
Verlag, New York, third edition, 2000. Revised and with a preface by Hugh L. Montgomery.
[16] J.-M. Deshouillers, G. Eﬃnger, H. te Riele, and D. Zinoviev. A complete Vinogradov 3-primes theorem
under the Riemann hypothesis. Electron. Res. Announc. Amer. Math. Soc., 3:99–104, 1997.
[17] K. Devlin. The millennium problems. Basic Books, New York, 2002. The seven greatest unsolved
mathematical puzzles of our time.
[18] H. G. Diamond. Elementary methods in the study of the distribution of prime numbers. Bull. Amer.
Math. Soc. (N.S.), 7(3):553–589, 1982.
[19] M. du Sautoy. The Music of the Primes: Searching to Solve the Greatest Mystery in Mathematics.
Fourth Estate, 2003.
[20] P. Dusart. In´egalit´es explicites pour ψ(X), θ(X), π(X) et les nombres premiers. C. R. Math. Acad.
Sci. Soc. R. Can., 21(2):53–59, 1999.
[21] H. Edwards. Riemann’s Zeta Function. Dover books on mathematics. Dover Publications, Mineola,
New York, 2001.
[22] S. Feng. Zeros of the Riemann zeta function on the critical line. J. Number Theory, 132(4):511–542,
2012.
[23] X. Gourdon. The 10
13 ﬁrst zeros of the Riemann Zeta function, and zeros computa-
tion at very large height. http://numbers.computation.free.fr/Constants/Miscellaneous/
zetazeros1e13-1e24.pdf, 2004.
[24] J.-P. Gram. Note sur les z´eros de la fonction ζ(s) de Riemann. Acta Math., 27(1):289–304, December
1903.
[25] A. Granville and G. Martin. Prime number races. Gac. R. Soc. Mat. Esp., 8(1):197–240, 2005. With
appendices by Giuliana Davidoﬀ and Michael Guy.
[26] G. H. Hardy. Sur les z´eros de la fonction ζ(s) de Riemann. Comp. Rend. Acad. Sci., 158:1012–1014,
1914.
[27] G. H. Hardy and J. E. Littlewood. Contributions to the theory of the Riemann zeta-function and the
theory of the distribution of primes. Acta Math., 41(1):119–196, 1916.
[28] G. H. Hardy and J. E. Littlewood. The zeros of the Riemann’s Zeta-Function on the critical line.
Math. Zeitschrift, 10:283–317, 1921.
[29] G. H. Hardy and J. E. Littlewood. The approximate functional equation in the theory of the zeta-
function, with applications to the divisor problems of Dirichlet and Piltz. Proc. London Math. Soc.,
21(2):39–74, 1922.
[30] D. R. Heath-Brown. The fourth power moment of the Riemann zeta function. Proc. London Math.
Soc. (3), 38(3):385–422, 1979.
[31] H. A. Helfgott. Major arcs for goldbachs problem. Preprint. Available at arXiv:1203.5712.
[32] H. A. Helfgott. Minor arcs for goldbachs problem. Preprint. Available at arXiv:1205.5252.
[33] H. A. Helfgott. The ternary goldbach conjecture is true. Preprint. Available at arXiv:1312.7748.
[34] H. A. Helfgott. La conjecture de Goldbach ternaire. Gaz. Math., (140):5–18, 2014. Translated by
Margaret Bilu, revised by the author.
[35] J. I. Hutchinson. On the roots of the Riemann zeta function. Trans. Amer. Math. Soc., 27:49–60,
1925.
[36] A. E. Ingham. Mean-Value Theorems in the Theory of the Riemann Zeta-Function. Proc. London
Math. Soc., S2-27(1):273, 1928.
[37] A. E. Ingham. The distribution of prime numbers. Cambridge Mathematical Library. Cambridge
University Press, Cambridge, 1990. Reprint of the 1932 original, With a foreword by R. C. Vaughan.

28 P. MOREE, I. PETRYKIEWICZ, AND A. SEDUNOVA

[38] A. Ivi´c. The Riemann zeta-function. A Wiley-Interscience Publication. John Wiley & Sons, Inc., New
York, 1985. The theory of the Riemann zeta-function with applications.
[39] H. Kadiri. Une r´egion explicite sans z´eros pour la fonction ζ de Riemann. Acta Arith., 117(4):303–339,
2005.
[40] A. A. Karatsuba. Complex analysis in number theory. CRC Press, Boca Raton, FL, 1995.
[41] N. M. Katz and P. Sarnak. Random matrices, Frobenius eigenvalues, and monodromy, volume 45
of American Mathematical Society Colloquium Publications. American Mathematical Society, Provi-
dence, RI, 1999.
[42] N. M. Katz and P. Sarnak. Zeroes of zeta functions and symmetry. Bull. Amer. Math. Soc. (N.S.),
36(1):1–26, 1999.
[43] T. Kotnik and H. te Riele. The Mertens conjecture revisited. In Algorithmic number theory, volume
4076 of Lecture Notes in Comput. Sci., pages 156–167. Springer, Berlin, 2006.
[44] E. Landau. Handbuch der Lehre von der Verteilung der Primzahlen. 2 B¨ande. Leipzig B.G. Teubner,
1909.
[45] E. Landau. Handbuch der Lehre von der Verteilung der Primzahlen. 2 B¨ande. Chelsea Publishing
Co., New York, 1953. 2d ed, With an appendix by Paul T. Bateman.
[46] R. S. Lehman. On the diﬀerence π(x) − li(x). Acta Arith., 11:397–410, 1966.
[47] J. E. Littlewood. Sur la distribution des nombres premiers. Comp. Rend. Acad. Sci., 158:1869–1872,
1914.
[48] F. Mertens. ¨Uber eine zahlentheoretische Funktion. Sitzungsberichte Akademie Wissenschaftlicher
Wien Mathematik-Naturlich IIa, 106:761–830, 1897.
[49] F. Mezzadri and N. C. Snaith, editors. Recent perspectives in random matrix theory and number
theory, volume 322 of London Mathematical Society Lecture Note Series. Cambridge University Press,
Cambridge, 2005.
[50] H. L. Montgomery. The pair correlation of zeros of the zeta function. In Analytic number theory (Proc.
Sympos. Pure Math., Vol. XXIV, St. Louis Univ., St. Louis, Mo., 1972), pages 181–193. Amer. Math.
Soc., Providence, R.I., 1973.
[51] W. Narkiewicz. The development of prime number theory. Springer Monographs in Mathematics.
Springer-Verlag, Berlin, 2000. From Euclid to Hardy and Littlewood.
[52] A. M. Odlyzko. The 1022-nd zero of the Riemann zeta function. In Dynamical, spectral, and arithmetic
zeta functions (San Antonio, TX, 1999), volume 290 of Contemp. Math., pages 139–144. Amer. Math.
Soc., Providence, RI, 2001.
[53] A. M. Odlyzko and A. Sch¨onhage. Fast algorithms for multiple evaluations of the Riemann zeta
function. Trans. Amer. Math. Soc., 309(2):797–809, 1988.
[54] A. M. Odlyzko and H. J. J. te Riele. Disproof of the Mertens conjecture. J. Reine Angew. Math.,
357:138–160, 1985.
[55] T. Oliveira e Silva, S. Herzog, and S. Pardi. Empirical veriﬁcation of the even Goldbach conjecture
and computation of prime gaps up to 4 · 1018. Math. Comp., 83(288):2033–2060, 2014.
[56] S. J. Patterson. An introduction to the theory of the Riemann zeta-function, volume 14 of Cambridge
Studies in Advanced Mathematics. Cambridge University Press, Cambridge, 1988.
[57] D. J. Platt. Computing π(x) analytically. Math. Comp., 84(293):1521–1535, 2015.
[58] D. J. Platt. Numerical computations concerning the GRH. Math. Comp., 85(302):3009–3027, 2016.
[59] P. Ribenboim. The new book of prime number records. Springer-Verlag, New York, 1996.
[60] B. Riemann. ¨Uber die Anzahl der Primzahlen unter einer gegebenen Gr¨osse. Monatsberichte der
Berliner Akademie, pages 671–680, November 1859.
[61] J. B. Rosser. The n-th prime is greater than n log n. Proc. London Math. Soc., 45(2):21–44, 1939.
[62] J. B. Rosser and L. Schoenfeld. Approximate formulas for some functions of prime numbers. Illinois
J. Math., 6:64–94, 1962.
 PRIME NUMBERS AND RIEMANN ZEROS 29

[63] J. B. Rosser, J. M. Yohe, and L. Schoenfeld. Rigorous computation and the zeros of the Riemann zeta-
function. (With discussion). In Information Processing 68 (Proc. IFIP Congress, Edinburgh, 1968),
Vol. 1: Mathematics, Software, pages 70–76. North-Holland, Amsterdam, 1969.
[64] M. Rubinstein. Riemann’s inﬂuence in number theory from a computational and experimental per-
spective. In The legacy of Bernhard Riemann after one hundred and ﬁfty years. Vol. II, volume 35 of
Adv. Lect. Math. (ALM), pages 633–679. Int. Press, Somerville, MA, 2016.
[65] M. Rubinstein and P. Sarnak. Chebyshev’s bias. Experiment. Math., 3(3):173–197, 1994.
[66] K. Sabbagh. Dr. Riemann’s Zeros. Atlantic books, 2003. The theory of the Riemann zeta-function
with applications.
[67] E. Schmidt. ¨Uber die Anzahl der Primzahlen unter gegebener Grenze. Math. Ann., 57(2):195–204,
1903.
[68] A. Selberg. An elementary proof of the prime-number theorem for arithmetic progressions. Canadian
J. Math., 2:66–78, 1950.
[69] C. L. Siegel. ¨Uber Riemanns Nachlass zur analytischen Zahlentheorie. Quellen und Studien zur
Geschichte der Math. Astr. Phys., 2:45–80, 1932.
[70] N. C. Snaith. Riemann zeros and random matrix theory. Milan J. Math., 78(1):135–152, 2010.
[71] T. Tao and V. H. Vu. Additive combinatorics, volume 105 of Cambridge Studies in Advanced Mathe-
matics. Cambridge University Press, Cambridge, 2010. Paperback edition [of MR2289012].
[72] E. C. Titchmarsh. The zeros of the Riemann zeta-function. Proc. Roy. Soc. London, 151:234–255,
1935.
[73] E. C. Titchmarsh. The theory of the Riemann zeta-function. The Clarendon Press, Oxford University
Press, New York, second edition, 1986. Edited and with a preface by D. R. Heath-Brown.
[74] A. M. Turing. A method for the calculation of the zeta-function. Proc. London Math. Soc., 48 (2):180–
197, 1945.
[75] A. M. Turing. Some calculations of the Riemann zeta-function. Proc. London Math. Soc., 3 (3):99–117,
1953.
[76] J. van de Lune, H. J. J. te Riele, and D. T. Winter. On the zeros of the Riemann zeta function in the
critical strip. IV. Math. Comp., 46(174):667–681, 1986.
[77] V. S. Varadarajan. Euler through time: a new look at old themes. American Mathematical Society,
Providence, RI, 2006.
[78] I. M. Vinogradov. Representation of an odd number as a sum of three primes. Dokl. Akad. Nauk.
SSR, 15:291–294, 1937.

(P. Moree, A. Sedunova) Max-Planck-Institut f¨ur Mathematik, Vivatsgasse 7, D-53111
Bonn, Germany.
E-mail address: moree@mpim-bonn.mpg.de
E-mail address: alisa.sedunova@phystech.edu

(I. Petrykiewicz)
E-mail address: ipetrykiewicz@gmail.com
