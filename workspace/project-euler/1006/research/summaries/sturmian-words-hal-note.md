# Perrin & Restivo, "A note on Sturmian words" (TCS 429, 2012)

<!-- source: https://hal.science/hal-00828351/file/noteSturmianWords.pdf -->

Authoritative structural source for PE1006. Alphabet `A = {a,b}` (problem: `a=0, b=1`).

## Definitions used
- A word is **Sturmian** if it has exactly `n+1` factors of length `n` for all `n >= 1`.
  A finite word is Sturmian if it is a factor of an infinite Sturmian word.
- The **Fibonacci word**: fixed point `s` of the morphism `a -> ab, b -> a`;
  `s = abaababaabaab...`. The finite words `u_n = f^{n+1}(b)` (n >= -1) are the
  Fibonacci words with `u_n = u_{n-1}u_{n-2}`. In the problem's alphabet this is the
  sequence 0, 01, 010, 01001, ... The **slope** of the Fibonacci word is
  `α = 2/(3+√5) = (3-√5)/2 = 1/φ²` (Eq. "Example 2": continued fraction `[0,2,1,1,...]`).
- **Sturmian set** = set of all factors of a Sturmian word.
- A Sturmian set is **balanced**: two equal-length factors differ in number of `b`s by <= 1.
- **Right special** factor of length n: `wa, wb` both factors; exactly one per length.

## Theorem 2 (the structural theorem that drives enumeration) — Section 3
  Let `F` be a Sturmian set. Two words `u, v` of `F` of the same length are **consecutive
  in lexicographic order** iff
  `u = r·a·b·s, v = r·b·a·s`  or  `u = r·a, v = r·b`
  (for some words `r, s`; `r` is then the right-special principal prefix).
  Consequence (Corollary 3): the word following a non-maximal factor `u` is computed from
  its longest right-special prefix `r`: if `u = ra` next is `rb`; if `u = rabs` next is `rbas`.
  Proposition 5: generating all `n+1` length-n factors in lex order takes O(n²) time (linear
  in the size `n(n+1)` of the output).

## Proposition 3 (right border) — Section 4
  Ordered lexicographically, the last letters of the length-n factors, taken cyclically,
  form `b^p a^q` up to conjugacy (two changes total). Equivalently each column of the
  n×(n+1) factor matrix is `a* b*` up to cyclic shift. Related to Burrows–Wheeler transform
  and standard words (Theorem 3: `T(w)=b^p a^q` with p,q coprime iff w is a conjugate of a
  standard word). For the Fibonacci word length-8 example: conjugates of `abaababa` plus the
  singular factor `babaabab`.

## Explicit material given for the Fibonacci word
- `Characteristic(u,v,n)` integer algorithm generating the characteristic prefix (Example 11:
  `Characteristic(13,5,11) = a b a a b a b a a b a`).
- Table 1: all 11 length-10 factors of the Fibonacci word (primary concrete check target).
- Table 3: all 9 length-8 factors.

## What it lets this run do
- Confirms the governing object is the Sturmian factor set of slope 1/φ².
- Gives the lex-order consecutive-factor rule, which is the clean description of the
  k+1-factor set and the structural ingredient behind any exact recurrence for Ψ(k).
- Provides the full length-8 and length-10 factor lists to validate a brute oracle and any
  parameterization.

## What it does NOT settle (for the computation)
- Enumeration via Next/Sturm is O(n²) in length — **infeasible at k = 10^18**. This source
  gives the *structure* (lex order, consecutive pairs), not an O(log k) evaluation of the
  sum of squares. The closed form for Ψ(k) is not in this paper; it uses Theorem 2 as input.

## Full text
[[sturmian-words-hal-note.full]]

```claim
id: PR-consecutive-factors-lex
statement: In a Sturmian set F, two equal-length factors u,v are consecutive in lex order iff u=r·ab·s and v=r·ba·s, or u=r·a and v=r·b; the next factor after u is rbas (if u=rabs) or rb (if u=ra), r the longest right-special prefix.
hypotheses: F is a Sturmian set (factor set of a Sturmian word); u,v in F of equal length.
holds-here: yes — F here is the Fibonacci Sturmian set (slope 1/phi^2).
status: proved (in source)
bearing: classifies/orders the k+1 length-k factors; structural basis for a recurrence on Psi(k).
anchor: research/summaries/sturmian-words-hal-note.md
answers: precise-sourced-statement-c1ec
```

```claim
id: PerrinRestivo-len8-len10-lists
statement: The Fibonacci Sturmian set's length-8 factors are the 8 conjugates of abaababa plus the singular factor babaabab (9 total); its 11 length-10 factors are listed in the paper's Table 1.
hypotheses: Fibonacci word slope 2/(3+sqrt5).
holds-here: yes — decimal-digit check targets for a brute oracle.
status: asserted in source (worked examples); VERIFIED independently by scholar against the run's brute oracle via the Cassaigne-Fici-Sciortino-Zamboni Christoffel array A_{5,3} (hal-01829144): the 8 length-8 factors with Parikh (5,3) match the oracle exactly and the singular 10100101 is confirmed as "the other factor of length 8". Length-8 count 9 and structure verified; length-10 count 11 matches oracle.
bearing: concrete oracle values to reproduce the brute program against (made a checked two-way verification).
anchor: research/summaries/sturmian-words-hal-note.md
```
