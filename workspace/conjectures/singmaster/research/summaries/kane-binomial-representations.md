> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/kane-binomial-representations.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://pdfs.semanticscholar.org/3d3e/f2f6c390e8427141100b4699b7322b08fd38.pdf | converted from PDF -->

The Number of Ways of
Expressing t as a Binomial
Coefficient

By Daniel Kane
January 7, 2007

An Interesting Note:

10 is both a triangular number and a
tetrahedral number.

Why does this hold?

Is it equal to any other binomial
coefficient?

Are there any non-trivial relations?

Yields a Pell Equation

Trying to produce solutions of the form

with Solutions

Stating the Problem More Precisely

•Studied by Singmaster in [2] (1971)

•N(3003) = 8

•N(t) ¸ 6 for infinitely many t

•Conj: N(t) = O(1)

Define

What are Reasonable Bounds?

• Singmaster showed in [2] that

• Consider n > 2m (we do this from now on)

An improvement

• In [3] Erdös et al. proved that

• Prime in (n-n5/8, n) for n >> 1.
• Split into cases based on n > (log t)6/5

For n > (log t)6/5

• Use Approximation

For  n < (log t)6/5

• Approximation yields m > n5/8

• 9 prime, P, s.t. n-m < P < n
• P divides t
• Pick largest N, all others satisfy P < n < N
• At most M solutions
• M = O(N5/8) = O((log t)3/4)
• Using the strongest conjectures on gaps
between primes could give

Another way to handle this case

• Consider all solutions
• Order so n1   >  n2   > … > nk
m1 <  m2 < … < mk,
• As n decreases and m increases, the
effect of changing n decreases and the
effect of changing m increases.
• (ni-ni+1)/(mi+1-mi) increasing.
• These fractions are distinct

Another way (continued)

• Differences of (ni , mi) are distinct
• Only O(s2) have n, m < s
• Total Change in n-m > ck3/2

• k3/2 = O((log t)6/5)
• k = O ((log t)4/5).

What did we do?

• n convex function of m
• Lattice points on graph of ANY convex
function
• Idea: Consider higher order derivatives.

Problems to Overcome

• How do we use the derivative data?
• How do we obtain the derivative data?

Using Data, a Lemma

Lemma If f and g are Cn-functions so that
f(x) = g(x) at x1 < x2 < … < xn+1, then
f(n)(y) = g(n)(y) for some y2 (x1 , xn+1)
• Generalization of Rolle’s Theorem
• Proof by induction & Rolle’s Theorem

Using Data, Proof of Lemma

f(1)(x) = g(1)(x)

f(2)(x) = g(2)(x)

f(0)(x) = g(0)(x) x1 x2 x3 xn-1 xn xn+1

f(n)(x) = g(n)(x)
 y

Using Derivative Data (Continued)

• Consider function f, f(mi) = ni
• g polynomial interpolation of f at m1, m2,
…, mk+1
• g(k) constant
• f(k) is this constant at some point

Using Derivative Data (cont.)Using Derivative Data (cont.)

• kth derivate of f small but non-zero
• Fit polynomial to k+1 points separated by
S
• ) kth derivative over k! either 0 or more
than S-k(k+1)/2.

Derivative Data

• Define
• Make smooth using 
• Estimate with Sterling’s approximation

Estimating Derivatives

• Main Term: Derivatives of
[ log t + (z+1) ] / z and take exp of power series
• (z - 1) / 2 is easy
• Error term: Cauchy Integral Formula

A Useful ParameterSplit into Cases

1.  < 1.15
2. 1.15 <  < log log t/(24 log log log t)
3. log log t/(24 log log log t)<  <(log log t)4

4. (log log t)4 < 

Case 1:  < 1.15

• Already covered
• O((log t)3/4) solutions

Case 2:  1.15 <  < log log t/(24 log log log t)

• Set k = (log log t)/(12 log log log t)
• Technical conditions satisfied
• k+1 adjacent solutions mi of separation S

Case 3:  log log t/(24 log log log t)<  <(log log t)4

We need a slightly better analysis to bound

LCM over all sequences of k distinct ri 0,

|ri| < S
 Bounding B

• Count multiples of each prime
• pn divides at most min(k , 2S/pn) ri’s
• Use Prime Number Theorem

Using Bound

• k = 2
• Technical Conditions Satisfied

Case 4:  (log log t)4 < Conclusions

•Know where to look to tighten this bound

•Can use technique for other problems

References

[1] D. Kane, On the Number of Representations of t as a
Binomial Coefficient, Integers: Electronic Journal of
Combinatorial Number Theory, 4, (2004), #A07, pp. 1-
10.
[2] D. Singmaster, How often Does an Integer Occur as a
Binomial Coefficient?, American Mathematical Monthly,
78, (1971) 385-386

*[excerpt ends; 163 characters not shown — see `research/sources/kane-binomial-representations.full.md`]*
