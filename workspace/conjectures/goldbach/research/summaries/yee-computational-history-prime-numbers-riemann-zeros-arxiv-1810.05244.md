> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/yee-computational-history-prime-numbers-riemann-zeros-arxiv-1810.05244.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

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

*[excerpt ends; 75876 characters not shown — see `research/sources/yee-computational-history-prime-numbers-riemann-zeros-arxiv-1810.05244.full.md`]*
