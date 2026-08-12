> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/multiply_perfect_numbers_page_oeis_pdf.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://oeis.org/A091443/a091443.pdf | converted from PDF -->

6/4/2020 Multiply Perfect Numbers

wwwhomes.uni-bielefeld.de/achim/mpn.html 1/6

The Multiply Perfect Numbers Page

Introduction

Let o(n) be the number theoretic function which denotes the sum of all divisors of a natural number n. If o(n) is an integral multiply of n, then n is denoted as a multiply
perfect number or k-fold perfect number (also called multiperfect number or pluperfect number). Call o(n)/n abundancy (also called index or multiplicity) of n. A
multiply perfect number is called proper if its abundancy is > 2. For example consider the divisors of the number 120:
1+2+3+4+5+6+8+10+12+15+20+24+30+40+60+120=o(120)=o(2^3*3*5)=o(2^3)*o(3)*o(5)=(1+2+4+8)*(1+3)*(1+5)=15*4*6=360=3*120.
Hence 120 is a 3-fold perfect number.

Status

Abundancy Count When last number was discovered Which was last? Are all discovered? Estimated total number

1 1 - - yes and proved 1

2 50 2017-12-26 18.4889706 no, there are inﬁnitely many ∞

3 6 <= 1643 3.2049844 yes 6

4 36 <= 1929 4.3351682 yes 36

5 65 <= 1990 5.1744360 yes 65

6 245 1993-05-?? 5.6720844 yes 245

7 516 1994-01-09 5.9403364 almost surely yes ~ 515

8 1135 2017-05-20 6.3396518 probably yes ~ 1140

9 2095 2013-01-10 7.2802453 no ~ 2200

10 1164 2013-01-03 7.2933919 no ~ 4500

11 1 2001-03-13 8.3870050 no ~ 10000

In column "Which was last?" the identiﬁer ln(ln(MPN)) is given for those which were verﬁed by me. I checked these numbers only for those MPNs reported before 2017-
05-23.
We have a total of 5311+3 (of which 5263 have an abundancy > 2) known and claimed MPNs until 2018-01-07.
It is extremly probable, that all proper MPNs with abundancy <= 7 are discovered.

Data

Richard Schroeppel's archive of 2094 MPNs built 1995-12-13 .
The collection of 5311 MPNs from 2014-01-01(gziped to 918 kB) sorted by abundancy and magnitude. It is grown out of Rich's database --- thanks ---, and transformed into
a new format, such that each multiply perfect number allocates one line with all its additional informations in the form:
M|ln_ln|rich_id,deep|dpf,tpf|date|name|number|comment

| is a separator character between the ﬁelds and is not allowed inside any ﬁeld. Except of the last ﬁeld, comment, all other ﬁelds are obligatory, but they can be empty,
e.g. if the discovery date or person is unknown.
M indicates the abundancy of the number as a lower case letter, such that the letters a,b,c,d,... correspond to the abundancies 1,2,3,4, ... .
ln_ln gives the decimal value of logeloge of the number and is rounded to 7 decimal places after the period. This serves now as a unique identiﬁer to each number,
also.
rich_id is Rich's unique identiﬁer for this number which encodes the abundancy appended by the exponents of at most the three primes 2,3,5. These exponents are
encoded alternatingly in a 26-base system made up of the letters a-z und a 10-base system made up of the digits 0-9. The letter @ is used if a prime exponent is zero.
In the case that this identiﬁer is still ambigious, it is appended by a lower case letter which serves as a counter.
R. Sorli likes to avoid this further counter and recommends to use not only the primes 2,3,5, but as less as further necessary for unequivocality using Rich's scheme of
alternatingly letters and digits for encoding the corresponding exponents (at most up to and including 23 is sufﬁcient until now).
deep indicates the minimal number of successive primes (starting with 2) whose exponents must be given to reconstruct the MPN straight forward (without knowing
its abundancy).
dpf indicates the number of different prime factors.
tpf indicates the number of total prime factors.
date gives the year of the ﬁrst (or independent) discovery in the form YYYY-MM-DD as long as month and day (and year) is known.
name gives the name of the discoverer. Like in the date ﬁeld, multiple independent discoveries are separated by commas.

*[excerpt ends; 17180 characters not shown — see `research/sources/multiply_perfect_numbers_page_oeis_pdf.full.md`]*
