# Cassaigne, "On extremal properties of the Fibonacci word" (RAIRO ITA 42, 2008)

<!-- source: https://www.numdam.org/item/10.1051/ita:2008003.pdf -->

Surveys quantitative properties (repetition exponent, recurrence, palindromes) for which the
Fibonacci word is extremal.

## What it establishes (relevant to PE1006)
- The Fibonacci word f is the fixed point of the substitution a->ab, b->a; |φⁿ(a)| = F_{n+2}.
- Repetition/indices: Theorem 2.1–2.4 (critical exponent / index ind(u) bounds for Sturmian
  words); Theorem 2.8 (Fibonacci word is maximal for a related quantity among non-periodic
  words); recurrence results (Thm 3.3, ρ*(u)=ind*(u) for Sturmian).
- Palindromic content of the Thue–Morse word (Prop 6.3: total lower palindrome density 20/19).

## What it implies for this problem
**Does not help the core computation.** It is about repetition exponents, recurrence
functions, and palindromes — none of which enter Ψ(k) = sum of squares of the integer values
of the length-k factors. It confirms background facts (lengths |S_n|=F_{n+2}; f is a standard
Sturmian word of slope 2−φ = 1/φ²) but contributes no factor-set structure or sum formula.
Not load-bearing; referenced for the slope/length identification only. `status: background`.
