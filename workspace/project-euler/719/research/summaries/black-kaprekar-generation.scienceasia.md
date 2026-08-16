# Black — Some Properties of the Kaprekar Numbers and a Means of Generation

Source: https://www.scienceasia.org/2001.27.n2/v27_133_136.pdf
(DOI 10.2306/scienceasia1513-1874.2001.27.133; `research/sources/black-kaprekar-generation.scienceasia.full.md`).
Colin G Black, ScienceAsia 27 (2001) 133–136.

**Definition used (n-Kaprekar).** k is an *n*-Kaprekar number when k = q + r and
k² = q·10^n + r with k,q,r positive integers, q > 0, 0 < r < 10^n (for k > 1).
This is exactly the **two-block** split of k² (left part of digit length ≤ n,
right part of length n). Not the general 2+-block S-number rule.

**What it establishes.**
- **Theorem 1:** k is n-Kaprekar ⇒ k² ≡ k (mod 10^n − 1).
- **Corollary:** k is n-Kaprekar ⇒ k² ≡ k (mod 9); combined with (mod 9)
  arithmetic this forces k ≡ 0 or 1 (mod 9) for any Kaprekar number.
- **Theorem 2:** for t ≡ k (mod 9), k is n-Kaprekar only if t ∈ {0, 1}.
- **Theorem 3:** q is always even; r is odd when k is odd, even when k is even.
- Gives a constructive generation scheme (via q, r from a formula in k and n)
  for the two-block Kaprekar numbers up to any bound.

**Bearing on PE 719.** Reinforces the two-block theory (same residue-class-9
observation Iannucci and the OEIS A038206 comment use for S-roots) but the
method is restricted to exactly-two-block splits. The S-number rule allows
2+ blocks, so this is not a route to T(10¹²); the digit-partition recursion
over arbitrary block counts is still required. Supplementary, confirming the
mod-9 filter (roots m ≡ 0 or 1 mod 9) that the backward ladder uses as a
necessary (not sufficient) filter.

**Does not settle** the general multi-block problem or the numeric answer.
