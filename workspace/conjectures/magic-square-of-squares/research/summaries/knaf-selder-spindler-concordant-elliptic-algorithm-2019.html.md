> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/knaf-selder-spindler-concordant-elliptic-algorithm-2019.html.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/html/1907.02148 | converted from HTML -->

## What is in it

- An Algorithm to Find Rational Points on Elliptic Curves Related to the Concordant Form…
  - 1 Introduction
  - 2 General background
    - 2.1 Elliptic curves
      - 2.1.1 General notions
      - 2.1.2 Elliptic curves corresponding to concordant forms
    - 2.2 Quadratic Forms
      - 2.2.1 Solvability criterion
      - 2.2.2 Parametrization of quadratic forms
      - 2.2.3 Pairs of quadrics with separated variables
    - 2.3 Two-descent
      - 2.3.1 General theory
      - 2.3.2 Reducing the number of possibilities
      - 2.3.3 Notations
  - 3 Examples for the two-descent
    - 3.1 General strategy
    - 3.2 General data
    - 3.3 Examples
      - 3.3.1 Congruent prime numbers
      - 3.3.2 Congruent numbers which are twice a prime number
- …


## What it claims

It is well known that the determination of the Mordell-Weil group of an elliptic curve is a difficult problem. Apart from the torsion subgroup, which can be calculated rather easily using the Lutz-Nagell-Theorem ([11], [16], cf. [20], [21]) and for which very good general information is given by Mazur’s Theorem (cf. [12]), obtaining information on the rational points of a rationally defined elliptic curve is hard. Even if the elliptic curve is explicitly given, both the calculation of the rank of the Mordell-Weil group and the determination of explicit solutions (generators of this group) are difficult problems. A famous example due to Zagier (cf. [25]; also see [9], p.5, Fig. 1.3), which illustrates the problems, is the task of explicitly showing that n = 157 n=157 is a congruent number by determining the sides of a rational triangle with area 157 157, which consist of fractions with more than 25 25 decimal places in both the numerator and the denominator. As a byproduct of these calculations one easily obtains nontrivial rational solutions of the equation y 2 = x ⁡ ( x − 157) ​ (…

## Statements it makes

Lemma: Consider the projective quadric Q = { ( x 0, x 1, x 2) ∈ ℙ 2 | F ( X 0, X 1, X 2) Q=\{(x_{0},x_{1},x_{2})\in\mathbb{P}^{2}\,|\,F(X_{0},X_{1},X_{2}) = 0 } =0\} where F ⁡ ( X 0, X 1, X 2) = a 00 ​ X 0 2 + a 01 ​ X 0 ​ X 1 + a 11 ​ X 1 2 + a 22 ​ X 2 2 F(X_{0},X_{1},X_{2})=a_{00}X_{0}^{2}+a_{01}X_{0}X_{1}+a_{11}X_{1}^{2}+a_{22}X_{2}^{2}. The set of all points ( x 0, x 1, x 2) ∈ Q (x_{0},x_{1},x_{2})\in Q with x 2 ≠ 0 x_{2}\not=0 can be parametrized by the rational mapping Φ: ℙ 1 → Q \varPhi:\mathbb{P}^{1}\rightarrow Q given by Φ ⁡ ( ξ 0, ξ 1) = ( φ 0 ​ ( ξ 0, ξ 1), φ 1 ​ ( ξ 0, ξ 1), φ 2 ​ ( ξ 0, ξ 1))…

Lemma: Let Q 1, Q 2 Q_{1},Q_{2} be two quadratic forms as above, let ( x 0, x 1, x 2) (x_{0},x_{1},x_{2}) be a point on Q 1 Q_{1} and let

Corollary: If the two quadrics Q 1 Q_{1} and Q 2 Q_{2} are diagonal (i.e., if a 01 = b 01 = 0 a_{01}=b_{01}=0) and if one of the coordinates x 0 x_{0} or x 1 x_{1} of the fixed point is zero, then the substituted form of Q 2 Q_{2} is biquadratic in ( ξ 0, ξ 1) (\xi_{0},\xi_{1}).

*[digest of a 118858 character source; every section, statement, and proof in full at `research/sources/knaf-selder-spindler-concordant-elliptic-algorithm-2019.html.full.md`]*
