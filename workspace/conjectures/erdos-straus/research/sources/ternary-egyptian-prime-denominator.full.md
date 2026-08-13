<!-- source: https://link.springer.com/article/10.1007/s40993-022-00339-4 | converted from HTML -->

Ternary Egyptian fractions with prime denominator | Research in Number Theory | Springer Nature Link

Skip to main content

# Ternary Egyptian fractions with prime denominator

- Research
- [Open access][1]
- Published: 26 June 2022

- Volume 8, article number 41 ( 2022)
- Cite this article

You have full access to this [open access][1] article

[Download PDF][2]

[Save article][3]

[View saved research][4]

[Research in Number Theory][5] [Aims and scope][6] [Submit manuscript][7]

Ternary Egyptian fractions with prime denominator

[Download PDF][2]

## Abstract

For a prime number *p*, let \(A_3(p)= | \{ m \in \mathbb {N}: \exists m_1,m_2,m_3 \in \mathbb {N}, \frac{m}{p}=\frac{1}{m_1}+\frac{1}{m_2}+\frac{1}{m_3} \} |\). In 2019 Luca and Pappalardi proved that \(x (\log x)^3 \ll \sum _{p \le x} A_{3}(p) \ll x (\log x)^5\). We improve the upper bound, showing \(\sum _{p \le x} A_{3}(p) \ll x (\log x)^3 (\log \log x)^2\).

### Similar content being viewed by others

### [Egyptian fractions of bounded length][8]

Article 22 January 2024

### [On sum of prime factors of composite positive integers][9]

Article 22 February 2021

### [A quantitative bound on Furstenberg–Sárközy patterns with shifted prime power common differences in primes][10]

Article Open access 15 October 2024

### Explore related subjects

Discover the latest articles, books and news in related subjects, suggested using machine learning.

- [Algebra][11]
- [Arithmetic and Logic Structures][12]
- [Computational Number Theory][13]
- [Mathematics][14]
- [Number Theory][15]
- [Sequences, Series, Summability][16]
- [Analytical Techniques in Number Theory][17]

## 1 Introduction

An *Egyptian fraction*is a representation of a rational number as a sum of reciprocals of distinct integers. A ternary Egyptian fraction is such a sum that consists of exactly three summands. More precisely, it is a representation of a rational number \(\frac{m}{n}\) as the sum \(\frac{m}{n} = \frac{1}{m_1} + \frac{1}{m_2} + \frac{1}{m_3}\), for some distinct integers \(m_1, m_2, m_3\).

Questions regarding Egyptian fractions are amongst the most ancient problems in mathematics. Throughout history many mathematicians have studied this topic, gaining popularity in recent times thanks to Erdős who presented and solved various problems concerning Egyptian fractions (for more details, see, e.g. [[3][18]]). Probably one of the most famous amongst them is a conjecture by Erdős and Straus, stating that for any \(n \ge 2\), the rational number \(\frac{4}{n}\) has a representation as a ternary Egyptian fraction, that is, that the Diophantic equation

$$\begin{aligned}\frac{4}{n} = \frac{1}{x} + \frac{1}{y} + \frac{1}{z} \end{aligned}$$

has at least one solution. This conjecture is still open.

In this paper we consider ternary Egyptian fractions for which the denominator is a prime number, and we are interested in bounding the number of those, for all primes in a certain range. As usual, for two functions \(f, g : {\mathbb {N}} \rightarrow {\mathbb {R}}\), by \(f(x) \ll g(x)\) we mean that there exists a constant \(c > 0\) and a natural number \(N \in {\mathbb {N}}\), such that for any \(n \ge N\) we have \(f(n) \le c \cdot g(n)\). Throughout the paper, *p*always designates a prime number.

Let \(A_3(p)= \left| \left\{ m \in {\mathbb {N}}: \exists m_1,m_2,m_3 \in {\mathbb {N}}, \frac{m}{p}=\frac{1}{m_1}+\frac{1}{m_2}+\frac{1}{m_3} \right\} \right| \). Luca and Pappalardi [[5][19]] proved the following.

### Theorem 1.1

$$\begin{aligned}x (\log x)^3 \ll \sum _{p \le x} A_{3}(p) \ll x (\log x)^5. \end{aligned}$$

Our main result in this paper closes the gap between the upper and the lower bounds up to a factor of polyloglog.

### Theorem 1.2

$$\begin{aligned} x (\log x)^3 \ll \sum _{p \le x} A_{3}(p) \ll x (\log x)^3 (\log \log x)^2. \end{aligned}$$

(1)

Throughout the paper, \(\log \) always stands for the logarithm function in base 2.

## 2 Proof idea

The proof of our main theorem follows the lines of the proof of Theorem [1.1][20] by Luca and Pappalardi [[5][19]]. Our contribution is the improved upper bound in Lemma [2.3][21], which is our main lemma. The proof of Lemma [2.3][21] is based on two ingredients. The first one is an application of the Brun–Titchmarsh inequality (Theorem [3.1][22]). The second ingredient is Proposition [3.4][23], which is a strengthened version of Proposition [3.3][24] for the certain range of parameters which fits our needs.

The next lemma describes a well-known classification of solutions for ternary Egyptian fractions with a prime denominator. It appears in Mordell’s book [[6][25]], for example, as well as in other texts. A proof can be found, e.g., in [[5][19]].

### Lemma 2.1

If \(\frac{m}{p}=\frac{1}{m_1}+\frac{1}{m_2}+\frac{1}{m_3}\), where \(m_1, m_2, m_3\) are positive integers and \(\gcd (m,p)=1\), then either \(m \in \{ 1,2,3 \}\) or there exist positive integers *a*, *b*, *c*, *u*such that \(\gcd (a,b)=1\), \(c | a+b\) and one of the following holds:

-

either (Type I)

$$\begin{aligned}m = \frac{p + (a+b)/c}{abu}, \end{aligned}$$

-

or (Type II)

$$\begin{aligned}m = \frac{1 + p(a+b)/c}{abu}. \end{aligned}$$

Given Lemma [2.1][26], we denote by \(A_{3, I}(p)\) and by \(A_{3, II}(p)\) the number of those \(m\in {\mathbb {N}}\) for which \(\frac{m}{p}\) is of type I and of type II, respectively. Given the lower bound of Theorem [1.1][20], we can already rule out the case where \(m \in \{1,2,3 \}\) or \(\gcd (m,p) > 1\), as it contributes *O*(*x*) to the sum below. Hence,

$$\begin{aligned} \sum _{p\le x} A_3(p) \ll \sum _{p\le x} A_{3,I}(p) + \sum _{p\le x} A_{3,II}(p). \end{aligned}$$

In [[5][19]], they deduce Theorem [1.1][20] from the following lemma.

### Lemma 2.2

We have \(x (\log x)^3 \ll \sum _{p \le x} A_{3,I}(p) \ll x (\log x)^3\) and \(\sum _{p \le x} A_{3,II}(p) \ll x (\log x)^5\).

We improve the upper bound on the sum of solutions of type II in Lemma [2.2][27].

### Lemma 2.3

We have

$$\begin{aligned} \sum _{p \le x} A_{3,II}(p) \ll x (\log x)^3 (\log \log x)^2. \end{aligned}$$

Theorem [1.2][28] then follows immediately from Lemma [2.3][21]. The rest of the paper is dedicated to proving Lemma [2.3][21].

## 3 Proof of Lemma [2.3][21]

We use two classical number theory inequalities. The first one is the Brun–Titchmarsh inequality (Theorem 6.6 in [[4][29]]). Let \(\pi (x;q,a)\) denote the number of primes *p*congruent to *a*modulo *q*satisfying \(p \le x\). Recall that \(\phi \) is the Euler totient function.

### Theorem 3.1

For all \(q < x\) we have

$$\begin{aligned} \pi (x;q,a) \le \frac{2x}{\phi (q) \log (x/q)}. \end{aligned}$$

The second inequality we use is the known bound on the sum of characters by Burgess [[1][30]].

### Theorem 3.2

Let \(\chi \) be a Dirichlet character modulo *q*. Let \(r \ge 1\), \(H \ge 1\) be fixed integers, and fix \(\varepsilon > 0\). Then if either *q*is square-free or \(r=2\) we have

$$\begin{aligned} \sum _{N \le n \le N+H} \chi (n) \ll _{r, \varepsilon } H^{1-\frac{1}{r+1}} q^{\frac{1}{4r} + \varepsilon }. \end{aligned}$$

Recall that \(\tau (n) {:}{=}\sum _{d|n} 1\) is the number of distinct divisors *d*of *n*. Elsholtz and Tao proved the following (Proposition 1.4 from [[2][31]]).

### Proposition 3.3

For any \(A,B > 1\), and any positive integer \(k \le (AB)^{O(1)}\), we have

$$\begin{aligned} \sum _{a \le A} \sum _{b \le B} \tau (kab^2+1) \ll AB \log (A+B) \log (1+k). \end{aligned}$$

For our proof we need a refined version of Proposition [3.3][24], which holds for a more restricted range of *k*.

### Proposition 3.4

For any \(A,B > 1\) and \(p < \frac{5}{3}\), and any positive integer \(k \le A^p\), we have

$$\begin{aligned} \sum _{a \le A} \sum _{b \le B} \tau (kab^2+1) \ll _p AB \log (A+B). \end{aligned}$$

(2)

The tighter upper bound of Proposition [3.4][23] is one of the main ingredients in our improved upper bound in Lemma [2.3][21]. Note that Proposition [3.4][23] can probably be proved for a larger range than \(k \le A^p\) for \(p < \frac{5}{3}\), but since in our proof we use Proposition [3.4][23] only for \(p=1\), we have not made any effort in this direction.

### Proof

The proof follows the same lines as of the proof of Proposition [3.3][24] by Elsholtz and Tao [[2][31]]. For the case \(A \ge B\) it was already shown in [[2][31]] that ( [2][32]) holds. For the case where \(A \le B\), using the same argument as in their proof, it is sufficient to show that

$$\begin{aligned} \left| \sum _{\begin{array}{c} q \le B, \\ (q,2k)=1 \end{array}} \sum _{\begin{array}{c} a \le A, \\ (a,2q)=1 \end{array}} \left( \frac{-ka}{q} \right) \frac{\log \left( \frac{B}{q} \right) }{q} \right| \ll _p A \log B, \end{aligned}$$

where by \(\left( \frac{a}{q} \right) \) we mean the Jacobi symbol. Moreover, the contribution of \(q > kA\) has been shown by Elsholtz and Tao to be at most \(A\log B\).

It is left to consider the contribution of \(q \le kA\), for which we obtain a stronger upper bound, using Theorem [3.2][33] for \(r=2\), and \(k \le A^p\). Thus, we have

$$\begin{aligned} \left| \sum _{\begin{array}{c} a \le A, \\ (a,2q)=1 \end{array}} \left( \frac{-ka}{q} \right) \right| \ll _{\varepsilon } A^{\frac{2}{3}}q^{\frac{1}{8}+\varepsilon } \end{aligned}$$

Hence,

$$\begin{aligned} \left| \sum _{\begin{array}{c} q \le kA, \\ (q,2k)=1 \end{array}} \sum _{\begin{array}{c} a \le A, \\ (a,2q)=1 \end{array}} \left( \frac{-ka}{q} \right) \frac{\log \left( \frac{B}{q} \right) }{q} \right|&\ll _{\varepsilon } \sum _{q \le kA} A^{\frac{2}{3}}q^{\frac{1}{8}-1+\varepsilon } \log B\\&\ll _{\varepsilon } A^{\frac{2}{3}}(kA)^{\frac{1}{8}+\varepsilon } \log B \\&\ll _{\varepsilon } A^{\frac{2}{3}+\frac{p+1}{8}+\varepsilon (p+1)} \log B, \end{aligned}$$

Taking \(\varepsilon > 0\) small enough proves the statement. \(\square \)

We are now ready to prove our main lemma.

### Proof of Lemma 2.3

In fact, we prove something slightly stronger. We bound the number of tuples (*m*, *p*, *a*, *b*, *c*, *u*) of Type II satisfying Lemma [2.1][26], which we denote by \({\mathcal {T}}(x)\). This gives an upper bound on the number of pairs (*m*, *p*) of type II,

$$\begin{aligned} \sum _{p \le x} A_{3,II}(p) \le {\mathcal {T}}(x). \end{aligned}$$

(3)

For each pair (*m*, *p*) of type II we can write \(p = \frac{baum - 1}{(a+b)/c}\). By setting \(t = (a+b)/c\) and substituting \(b = ct-a\), we get

$$\begin{aligned} p = \frac{(ct-a)aum - 1}{t} = caum - \frac{a^2um+1}{t}. \end{aligned}$$

Furthermore, note that \(aum \le 4x\). Indeed, assuming without loss of generality that \(a \le b\), we get that

$$\begin{aligned} m = \frac{1+pt}{a(ct-a)u} \le \frac{2pt}{a(ct/2)u} = \frac{4p}{acu}, \end{aligned}$$

giving \(aum \le \frac{4p}{c} \le 4x\). For the sake of simplicity, as \(aum \ll x\), we might as well assume \(aum \le x\). Moreover, by symmetry, we can assume \(u \le m\). We have \(\tau (a^2um+1)\) possibilities for *t*, and once *a*, *u*, *m*and *t*have been fixed, there are only \(\pi (x;aum,-(a^2um + 1)/t)\) possibilities for *p*. Hence, the number of tuples (*m*, *p*, *a*, *b*, *c*, *u*) is at most

$$\begin{aligned} {\mathcal {T}}(x) \le \sum _{aum \le x}\sum _{t | a^2um +1} \pi \left( x; aum, -\frac{a^2um + 1}{t} \right) . \end{aligned}$$

(4)

Considering both ( [3][34]) and ( [4][35]), we now focus on bounding from above the right-hand side of ( [4][35]).

By the Brun–Titchmarsh inequality (Theorem [3.1][22]), we have \(\pi (x; aum, d) \ll \frac{x}{\phi (aum)\log (x/aum)}\) for all *d*. Moreover, considering also the trivial bound \(\pi (x; aum, d) \ll \frac{x}{aum}\), we actually get \(\pi (x; aum, d) \ll \frac{x}{\phi (aum) \log (2+x/aum)}\), which is useful for those values of *aum*which are very close to *x*. Using this last inequality and the classical inequality \(\phi (n) \gg \frac{n}{\log \log n}\), we have

$$\begin{aligned} \sum _{aum \le x}\sum _{t | a^2um +1} \pi \left( x; aum, -\frac{a^2um + 1}{t} \right)&\ll \sum _{aum \le x} \sum _{t|a^2um+1} \frac{x}{\phi (aum) \log (2+x/aum)} \\&\ll \sum _{aum \le x} \tau (a^2um+1)\frac{x}{\phi (aum) \log (2+x/aum)} \\&\ll \sum _{aum \le x} \tau (a^2um+1)\frac{x}{aum} \frac{\log \log aum}{\log (2+x/aum)}. \end{aligned}$$

It suffices to show that the following holds for any \(N \le x\),

$$\begin{aligned} \sum _{N/2 \le aum \le N} \frac{\tau (a^2um+1)}{aum} \ll (\log x)^3. \end{aligned}$$

(5)

Indeed, summing ( [5][36]) over all \(N = 2^i\) for \(i \le \log x\) gives

$$\begin{aligned} \sum _{p \le x} A_{3,II}(p) \ll x (\log x)^3 \sum _{i=1}^{\log x} \frac{\log i}{1+\log x -i} \ll x (\log x)^3 (\log \log x)^2, \end{aligned}$$

proving the lemma.

Hence, it is left to prove ( [5][36]). We have

$$\begin{aligned} \sum _{N/2 \le aum \le N} \frac{\tau (a^2um+1)}{aum} \ll \sum _{A,U,M} \sum _{U \le u \le 2U} \sum _{A \le a \le 2A} \sum _{M \le m \le 2M} \frac{\tau (a^2um+1)}{aum}, \end{aligned}$$

where the first sum on the right-hand-side is going over all dyadic triplets \((A,U,M) = (2^i, 2^j, 2^h)\) for which the set \(\left\{ aum ~:~ A\le a\le 2A, \, U\le u \le 2U, \, M\le m \le 2M \right\} \) has a non-empty intersection with the interval [*N*/2, *N*].

By Proposition [3.4][23], since \(U \le M\), we have

$$\begin{aligned} \sum _{U \le u \le 2U} \sum _{A \le a \le 2A} \sum _{M \le m \le 2M} \tau (a^2um+1) \ll AUM \log x. \end{aligned}$$

Since in this range of summation we have \(aum \ge AUM\), we get

$$\begin{aligned} \sum _{U \le u \le 2U} \sum _{A \le a \le 2A} \sum _{M \le m \le 2M} \frac{\tau (a^2um+1)}{aum} \ll \log x. \end{aligned}$$

(6)

For every \(N \le x\) there are \(O((\log x)^2)\) dyadic triplets (*A*, *U*, *M*) for which the set \(\{ aum: A \le a \le 2A, \, U \le u \le 2U, \, M \le m \le 2M \}\) has a non-empty intersection with [*N*/2, *N*]. Considering ( [6][37]) we then get

$$\begin{aligned} \sum _{N/2 \le aum \le N} \frac{\tau (a^2um+1)}{aum} \ll (\log x)^3, \end{aligned}$$

proving ( [5][36]), as desired. \(\square \)

## 4 Concluding remarks

We believe that the correct order is the lower bound \(x(\log x)^3\). As mentioned at the beginning of the proof of Lemma [2.3][21], we actually count tuples (*m*, *p*, *a*, *b*, *c*, *u*) rather than pairs (*m*, *p*). A more direct count of the number of pairs (*m*, *p*) could possibly yield the desired order of \(x(\log x)^3\).

## Data availability

Data sharing not applicable to this article as no datasets were generated or analysed during the current study.

## References

1.

Burgess, D.A.: On character sums and l-series. II. Proc. Lond. Math. Soc. **3**(1), 524–536 (1963)

[Article][38] [MathSciNet][39] [Google Scholar][40]

2.

Elsholtz, C., Tao, T.: Counting the number of solutions to the Erdös–Straus equation on unit fractions. J. Aust. Math. Soc. **94**, 50–105 (2013)

[Article][41] [MathSciNet][42] [Google Scholar][43]

3.

Guy, R.: Unsolved Problems in Number Theory, 2nd edn. Springer, Nw York (1994)

[Book][44] [Google Scholar][45]

4.

Iwaniec, H., Kowalski, E.: Analytic number theory. Am. Math. Soc. Colloq. Public. **53**, 159 (2004)

[MathSciNet][46] [MATH][47] [Google Scholar][48]

5.

Luca, F., Pappalardi, F.: On ternary Egyptian fractions with prime denominator. Res. Number Theory **5**(4), 1–14 (2019)

[Article][49] [MathSciNet][50] [Google Scholar][51]

6.

Mordell, L.J.: Diophantine Equations. Academic Press, Cambridge (1969)

[MATH][52] [Google Scholar][53]

[Download references][54]

## Acknowledgements

The authors would like to thank their PhD supervisor Professor Béla Bollobás for his valuable comments.

In a previous version of this paper we proved an upper bound of \(x (\log x)^3 (\log \log x)^3\). We would like to thank Matteo Bordignon, Christian Elsholtz, Bryce Kerr and Timothy Trudgian for pointing out to us that using the Burgess bound instead of the Pólya-Vinogradov inequality enables us to prove Proposition [3.4][23] in its current more general version, and consequently removes one \(\log \log x\) factor in Lemma [2.3][21]. The authors would also like to thank the anonymous referee for further comments.

## Author information

### Authors and Affiliations

1.

Department of Pure Mathematics and Mathematical Statistics (DPMMS), University of Cambridge, Wilberforce Road, Cambridge, CB3 0WA, UK

Adva Mond & Julien Portier

Authors

1. Adva Mond

[View author publications][55]

Search author on: [PubMed][56] [Google Scholar][57]

2. Julien Portier

[View author publications][58]

Search author on: [PubMed][59] [Google Scholar][60]

### Corresponding author

Correspondence to [Julien Portier][61].

## Additional information

### Publisher's Note

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## Rights and permissions

**Open Access**This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit [http://creativecommons.org/licenses/by/4.0/][62].

[Reprints and permissions][63]

## About this article

[image: Check for updates. Verify currency and authenticity via CrossMark] [64]

### Cite this article

Mond, A., Portier, J. Ternary Egyptian fractions with prime denominator. *Res. number theory***8**, 41 (2022). https://doi.org/10.1007/s40993-022-00339-4

[Download citation][65]

-

Received: 07 February 2022

-

Accepted: 20 May 2022

-

Published: 26 June 2022

-

Version of record: 26 June 2022

-

DOI: https://doi.org/10.1007/s40993-022-00339-4

### Share this article

Anyone you share the following link with will be able to read this content:

Get shareable link

Sorry, a shareable link is not currently available for this article.

Copy shareable link to clipboard

Provided by the Springer Nature SharedIt content-sharing initiative

### Keywords

- [Egyptian fractions][66]
- [Analytic number theory][67]
- [Counting problems][68]


## Links

[1]: https://www.springernature.com/gp/open-science/about/the-fundamentals-of-open-access-and-open-research
[2]: /content/pdf/10.1007/s40993-022-00339-4.pdf
[3]: /article/10.1007/s40993-022-00339-4/save-research?_csrf=EsUw9q0E7ZVUEFxLyfnPltbY-wPwdlHY
[4]: /saved-research
[5]: /journal/40993
[6]: /journal/40993/aims-and-scope
[7]: https://www.editorialmanager.com/rntb
[8]: https://link.springer.com/10.1007/s40993-023-00504-3?fromPaywallRec=false
[9]: https://link.springer.com/10.1007/s11139-020-00370-y?fromPaywallRec=false
[10]: https://link.springer.com/10.1007/s00208-024-03015-3?fromPaywallRec=false
[11]: /subjects/algebra
[12]: /subjects/arithmetic-and-logic-structures
[13]: /subjects/computational-number-theory
[14]: /subjects/mathematics
[15]: /subjects/number-theory
[16]: /subjects/sequences-series-summability
[17]: /subjects/analytical-techniques-in-number-theory
[18]: /article/10.1007/s40993-022-00339-4#ref-CR3
[19]: /article/10.1007/s40993-022-00339-4#ref-CR5
[20]: /article/10.1007/s40993-022-00339-4#FPar1
[21]: /article/10.1007/s40993-022-00339-4#FPar5
[22]: /article/10.1007/s40993-022-00339-4#FPar6
[23]: /article/10.1007/s40993-022-00339-4#FPar9
[24]: /article/10.1007/s40993-022-00339-4#FPar8
[25]: /article/10.1007/s40993-022-00339-4#ref-CR6
[26]: /article/10.1007/s40993-022-00339-4#FPar3
[27]: /article/10.1007/s40993-022-00339-4#FPar4
[28]: /article/10.1007/s40993-022-00339-4#FPar2
[29]: /article/10.1007/s40993-022-00339-4#ref-CR4
[30]: /article/10.1007/s40993-022-00339-4#ref-CR1
[31]: /article/10.1007/s40993-022-00339-4#ref-CR2
[32]: /article/10.1007/s40993-022-00339-4#Equ2
[33]: /article/10.1007/s40993-022-00339-4#FPar7
[34]: /article/10.1007/s40993-022-00339-4#Equ3
[35]: /article/10.1007/s40993-022-00339-4#Equ4
[36]: /article/10.1007/s40993-022-00339-4#Equ5
[37]: /article/10.1007/s40993-022-00339-4#Equ6
[38]: https://doi.org/10.1112%2Fplms%2Fs3-13.1.524
[39]: http://www.ams.org/mathscinet-getitem?mr=148626
[40]: http://scholar.google.com/scholar_lookup?amp;title=On%20character%20sums%20and%20l-series.%20II&amp;journal=Proc.%20Lond.%20Math.%20Soc.&amp;doi=10.1112%2Fplms%2Fs3-13.1.524&amp;volume=3&amp;issue=1&amp;pages=524-536&amp;publication_year=1963&amp;author=Burgess%2CDA
[41]: https://doi.org/10.1017%2FS1446788712000468
[42]: http://www.ams.org/mathscinet-getitem?mr=3101397
[43]: http://scholar.google.com/scholar_lookup?amp;title=Counting%20the%20number%20of%20solutions%20to%20the%20Erd%C3%B6s%E2%80%93Straus%20equation%20on%20unit%20fractions&amp;journal=J.%20Aust.%20Math.%20Soc.&amp;doi=10.1017%2FS1446788712000468&amp;volume=94&amp;pages=50-105&amp;publication_year=2013&amp;author=Elsholtz%2CC&amp;author=Tao%2CT
[44]: https://link.springer.com/doi/10.1007/978-1-4899-3585-4
[45]: http://scholar.google.com/scholar_lookup?amp;title=Unsolved%20Problems%20in%20Number%20Theory&amp;doi=10.1007%2F978-1-4899-3585-4&amp;publication_year=1994&amp;author=Guy%2CR
[46]: http://www.ams.org/mathscinet-getitem?mr=2061214
[47]: http://www.emis.de/MATH-item?1059.11001
[48]: http://scholar.google.com/scholar_lookup?amp;title=Analytic%20number%20theory&amp;journal=Am.%20Math.%20Soc.%20Colloq.%20Public.&amp;volume=53&amp;publication_year=2004&amp;author=Iwaniec%2CH&amp;author=Kowalski%2CE
[49]: https://link.springer.com/doi/10.1007/s40993-019-0172-z
[50]: http://www.ams.org/mathscinet-getitem?mr=4030240
[51]: http://scholar.google.com/scholar_lookup?amp;title=On%20ternary%20Egyptian%20fractions%20with%20prime%20denominator&amp;journal=Res.%20Number%20Theory&amp;doi=10.1007%2Fs40993-019-0172-z&amp;volume=5&amp;issue=4&amp;pages=1-14&amp;publication_year=2019&amp;author=Luca%2CF&amp;author=Pappalardi%2CF
[52]: http://www.emis.de/MATH-item?0188.34503
[53]: http://scholar.google.com/scholar_lookup?amp;title=Diophantine%20Equations&amp;publication_year=1969&amp;author=Mordell%2CLJ
[54]: https://citation-needed.springer.com/v2/references/10.1007/s40993-022-00339-4?format=refman&amp;flavour=references
[55]: /search?sortBy=newestFirst&amp;contributor=Adva%20Mond
[56]: https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&amp;term=Adva%20Mond
[57]: https://scholar.google.co.uk/scholar?as_q=&amp;num=10&amp;btnG=Search+Scholar&amp;as_epq=&amp;as_oq=&amp;as_eq=&amp;as_occt=any&amp;as_sauthors=%22Adva%20Mond%22&amp;as_publication=&amp;as_ylo=&amp;as_yhi=&amp;as_allsubj=all&amp;hl=en
[58]: /search?sortBy=newestFirst&amp;contributor=Julien%20Portier
[59]: https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&amp;term=Julien%20Portier
[60]: https://scholar.google.co.uk/scholar?as_q=&amp;num=10&amp;btnG=Search+Scholar&amp;as_epq=&amp;as_oq=&amp;as_eq=&amp;as_occt=any&amp;as_sauthors=%22Julien%20Portier%22&amp;as_publication=&amp;as_ylo=&amp;as_yhi=&amp;as_allsubj=all&amp;hl=en
[61]: mailto:jp899@cam.ac.uk
[62]: http://creativecommons.org/licenses/by/4.0/
[63]: https://s100.copyright.com/AppDispatchServlet?title=Ternary%20Egyptian%20fractions%20with%20prime%20denominator&amp;author=Adva%20Mond%20et%20al&amp;contentID=10.1007%2Fs40993-022-00339-4&amp;copyright=The%20Author%28s%29&amp;publication=2522-0160&amp;publicationDate=2022-06-26&amp;publisherName=SpringerNature&amp;orderBeanReset=true&amp;oa=CC%20BY
[64]: https://crossmark.crossref.org/dialog/?doi=10.1007/s40993-022-00339-4
[65]: https://citation-needed.springer.com/v2/references/10.1007/s40993-022-00339-4?format=refman&amp;flavour=citation
[66]: /search?query=Egyptian%20fractions&amp;facet-discipline=#34;Mathematics&#34;
[67]: /search?query=Analytic%20number%20theory&amp;facet-discipline=#34;Mathematics&#34;
[68]: /search?query=Counting%20problems&amp;facet-discipline=#34;Mathematics&#34;
