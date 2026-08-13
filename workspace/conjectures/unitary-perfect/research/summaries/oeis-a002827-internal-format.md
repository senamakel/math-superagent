> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/oeis-a002827-internal-format.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://oeis.org/A002827/internal | converted from HTML -->

A002827 - OEIS

[login][1]

The OEIS is supported by [the many generous donors to the OEIS Foundation][2].

[image: A002827 - OEIS] [3]

[A002827][4]

Unitary perfect numbers: numbers k such that usigma(k) - k = k.
(Formerly M4268 N1783)

47

%I M4268 N1783 #76 Jun 28 2026 15:47:49

%S 6,60,90,87360,146361946186458562560000

%N Unitary perfect numbers: numbers k such that usigma(k) - k = k.

%C d is a unitary divisor of k if gcd(d,k/d)=1; usigma(k) is their sum (A034448).

%C The prime factors of a unitary perfect number (A002827) are the Higgs primes (A057447). - _Paul Muljadi_, Oct 10 2005

%C It is not known if a(6) exists. - _N. J. A. Sloane_, Jul 27 2015

%C Frei proved that if there is a unitary perfect number that is not divisible by 3, then it is divisible by 2^m with m >= 144, it has at least 144 distinct odd prime factors, and it is larger than 10^440. - _Amiram Eldar_, Mar 05 2019

%C Conjecture: Subsequence of A083207 (Zumkeller numbers). Verified for all present terms. - _Ivan N. Ianakiev_, Jan 20 2020

%C All unitary perfect numbers are even (for a proof see the LeanGenius link). - _Peter Luschny_, Jun 05 2026

%D R. K. Guy, Unsolved Problems in Number Theory, Sect. B3.

%D F. Le Lionnais, Les Nombres Remarquables. Paris: Hermann, p. 59, 1983.

%D D. S. Mitrinovic et al., Handbook of Number Theory, Kluwer, Section III.45.1.

%D N. J. A. Sloane, A Handbook of Integer Sequences, Academic Press, 1973 (includes this sequence).

%D N. J. A. Sloane and Simon Plouffe, The Encyclopedia of Integer Sequences, Academic Press, 1995 (includes this sequence).

%D James J. Tattersall, Elementary Number Theory in Nine Chapters, Cambridge University Press, 1999, pages 147-148.

%H T. F. Bloom, <a href="https://www.erdosproblems.com/1052">Erdős Problem #1052</a>.

%H H. A. M. Frei, <a href="https://www.e-periodica.ch/digbib/view?pid=edm-001:1978:33#105">Über unitar perfekte Zahlen</a>, Elemente der Mathematik, Vol. 33, No. 4 (1978), pp. 95-96.

%H Takeshi Goto, <a href="http://doi.org/10.1216/rmjm/1194275935">Upper Bounds for Unitary Perfect Numbers and Unitary Harmonic Numbers</a>, Rocky Mountain Journal of Mathematics, Vol. 37, No. 5 (2007), pp. 1557-1576.

%H A. V. Lelechenko, <a href="http://taac.org.ua/files/a2014/proceedings/UA-2-Andrew%20Lelechenko-440.pdf">The Quest for the Generalized Perfect Numbers</a>, in Theoretical and Applied Aspects of Cybernetics, TAAC 2014, Kiev.

%H M. V. Subbarao, <a href="/A002827/a002827.pdf">Letter to N. J. A. Sloane, Feb 18 1974</a>

%H M. V. Subbarao, T. J. Cook, R. S. Newberry and J. M. Weber, <a href="http://www.math.ualberta.ca/~subbarao/documents/Subbarao_Cook_Newberry_Weber1972.pdf">On unitary perfect numbers</a>, Delta, 3 (No. 1, 1972), 22-26.

%H G. Villemin's Almanac of Numbers, <a href="http://villemin.gerard.free.fr/Wwwgvmm/Decompos/ParfUnit.htm">Nombres Unitairement Parfaits</a>

%H C. R. Wall, <a href="/A002827/a002827_1.pdf">Letter to P. Hagis, Jr., Jan 13 1972</a>

%H C. R. Wall, <a href="https://doi.org/10.4153/CMB-1975-021-9">The fifth unitary perfect number</a>, Canad. Math. Bull., 18 (1975), 115-122.

%H C. R. Wall, <a href="https://www.fq.math.ca/Scanned/25-4/wall1.pdf">On the largest odd component of a unitary perfect number</a>, Fib. Quart., 25 (1987), 312-316.

%H Robb J. Walters, <a href="https://leangenius.org/proof/erdos-1052">Erdős #1052: Unitary Perfect Numbers</a>, LeanGenius.

%H Eric Weisstein's World of Mathematics, <a href="https://mathworld.wolfram.com/UnitaryPerfectNumber.html">Unitary Perfect Number.</a>

%H Wikipedia, <a href="https://en.wikipedia.org/wiki/Unitary_perfect_number">Unitary perfect number</a>

%F If m is a term and omega(m) = A001221(m) = k, then m < 2^(2^k) (Goto, 2007). - _Amiram Eldar_, Jun 06 2020

%e 6 = 2 * 3.

%e 60 = 2^2 * 3 * 5.

%e 90 = 2 * 3^2 * 5.

%e 87360 = 2^6 * 3 * 5 * 7 * 13.


*[excerpt ends; 1633 characters not shown — see `research/sources/oeis-a002827-internal-format.full.md`]*
