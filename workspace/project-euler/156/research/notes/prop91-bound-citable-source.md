# Citable source for the bound x ≤ d·b^b (PE156 finite scan bound)

Question this answers: where, exactly, is the fact "for digit d > 0 in base b,
every x with f_d(x,b) = x satisfies x ≤ d·b^b" proved, with what hypotheses,
and does it transfer verbatim to f(n,d) counting occurrences in 0..n?

## The source (two citable versions of the same paper)

**Paper:** Tanya Khovanova and Gregory Marton, *Archive Labeling Sequences*.

1. **arXiv (has the proof):** arXiv:2305.10357v2 [math.HO], 16 Feb 2024,
   Section 9 "All Your Base", **Proposition 9.1** (proof included).
   URL: https://arxiv.org/html/2305.10357 — full text on disk:
   `research/sources/archive-labeling-arxiv-latest.full.md`.
2. **Published (states the bound, defers proof):** *Amer. Math. Monthly*
   132(8), 2025, 780–787, DOI 10.1080/00029890.2025.2525050, Section 4
   (before Table 3): "We can be more precise in claiming that the largest
   value in E_d is not more than d·10^10. We prove the claim for this and
   other bases in our accompanying paper." CC-BY copy:
   https://dspace.mit.edu/bitstream/handle/1721.1/163207/UAMM_A_2525050_O.pdf —
   full text on disk: `research/sources/archive-labeling-amm-published.full.md`.

## Exact statement (verbatim from the arXiv v2 text on disk)

> **Proposition 9.1.** For any digit d > 0 in base b > d the maximum possible
> value of a=(d, b) is b^b and all x such that f_d(x, b) = x must be
> ≤ d · b^b.

**Definition in force** (start of Section 9, verbatim): "we denote by
f_d(x, b) the number of times the sticker d is used in the writing of numbers
in the range [1, …, x] in base b." So:

- counting is **1-based**: the numbers written out are 1..x, not 0..x;
- d is a **single digit** with 1 ≤ d ≤ b−1 (digit symbols of base b), and
  the hypothesis is **b > d**;
- leading zeroes are not written (source of the d = 0 special case).

## Proof (as given in the paper)

1. f_b(b^b) = b^b, so a=(d, b) ≤ b^b. *(Caveat: the subscript "b" as
   typeset is odd — the digit b does not exist in base b; the base-10
   analogue is the digit b−1 = 9, and indeed Table 1 gives a=(9) = 10^10 =
   b^b. The bound itself does not depend on this witness line.)*
2. If x = d·b^b then f_d(x, b) = x + 1.
3. All numbers in [d·b^b, (d+1)·b^b] have d as their first digit, so no
   solution to f_d(x,b) = x lies in that range.
4. f_d((d+1)·b^b) = (d+2)·b^b.
5. A base-b version of Lemma 5.1 (any b^b consecutive numbers contain at
   least b^b occurrences of digit d) then shows no solution can appear among
   the next b^b numbers, and "by repeating this ad infinitum" f_d stays
   permanently ahead of its index. ∎

## Hypotheses

- b > 1 (Section 9 assumes b > 1; unary base is treated separately).
- d > 0, and b > d (i.e. d is a legitimate single digit of base b).
- f_d(x,b) counts digit-d occurrences in the base-b writings of **1..x**
  (no leading zeroes).

## Transfer to f(n,d) on 0..n — verbatim yes

The problem's f(n,d) counts digit d in the decimal writings of 0..n.
For d > 0, the number 0 contributes no occurrences (its only digit is 0 and
it has no leading zeroes), and every integer 1..n contributes the same digits
to both counts. Hence f(n,d) = f_d(n, 10) for all n ≥ 0 and d ∈ {1,…,9}.
Consequences:

- Every positive solution of f(n,d) = n is a solution of f_d(x,10) = x, so
  n ≤ d·10^10 for every positive solution.
- n = 0 is an extra solution of the 0-based problem (f(0,d) = 0) for every
  d, but 0 ≤ d·10^10 trivially. So the bound holds for the full solution set
  of the 0-based problem.
- Base 10, d ∈ {1,…,9}: every solution satisfies **n ≤ d·10^10**, e.g.
  d = 9 gives n ≤ 90,000,000,000. This is the finite scan bound for the
  PE156 solver (gap G2, `research/backward/fixed-point-enumeration.md`).

Nothing about the d = 0 case transfers: Theorem 5.2 proves a=(0) is not
well-defined in base 10 (no n with f_0(n) = n), and Prop 9.3 gives a separate
bound b^(b+3) when a=(0,b) exists.

## OEIS A226238 — what it actually is

A226238: a(n) = (n^n − n)/(n − 1) = Σ_{k=1}^{n−1} n^k. Written in base n it is
(n−1) ones followed by a 0. Per the paper (Section 9) this is the base-10
expression of the **largest** x with f_1(x, b) = x (sticker 1, base b);
for b = 10 it is 1,111,111,110 = the max of E_1 (Table 3, A014778).
So A226238 is the d = 1 companion sequence to Prop 9.1's bound
((b^b − b)/(b−1) ≤ b^b ≤ d·b^b), not the general-d bound itself. The general
bound is Proposition 9.1. (A165617 counts the number of solutions of
f_1(x,b)=x; A364972 lists bases where a=(0,b) does not exist.)

## Status

Verified by reading the full source text on disk (both the arXiv v2 HTML and
the AMM published PDF conversion). The bound's statement, hypotheses, and
proof are quoted verbatim above. Durable claims: `G2-solution-bound`,
`km-prop91-bound`.