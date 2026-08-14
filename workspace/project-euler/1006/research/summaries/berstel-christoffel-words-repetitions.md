# Berstel–Lauve–Reutenauer–Saliola, "Combinatorics on Words: Christoffel Words and Repetitions in Words" (2008)

<!-- source: https://webpages.math.luc.edu/~lauve/papers/wordsbook.pdf -->

Complete mathematical text (book chapters 1–9: Christoffel words, Sturmian/standard words,
palindromization, primitive elements, Burrows–Wheeler, continued fractions, Stern–Brocot,
Markoff numbers, repetitions).

## What it establishes that bears on PE1006
- **Christoffel / standard / central words** and their characterizations (balanced words
  over {a,b}; slope b/a; palindromic +1-letter middle; the standard factorization into two
  Christoffel words, Thm 3.3 Borel–Laubie).
- **Lemma 2.7 (Cohn, de Luca–Mignosi)**: lower and upper Christoffel words of slope b/a are
  conjugates — the conjugate-class view of the length-k factors.
- **Theorem 3.3**: every Christoffel word has a unique factorization (u,v) into two
  Christoffel words — the substitution/reduction tree behind Fibonacci-index structure.
- Burrows–Wheeler and continued-fraction/Stern–Brocot connections (Ch. 6–7).
- Palindromization (Ch. 4): ψ(v) central words, central word = palindromic + possibly a
  middle letter; a proper Christoffel word is aψ(v)b.

## What it implies for this problem
This is a *surrounding-theory* reference. It does **not** give a closed form for Ψ(k) nor the
consecutive-factor lex-order rule (that is Perrin–Restivo). But it is the authoritative
statement of the Christoffel/standard-word apparatus behind the `factor-parameterization`
rung: it supports viewing the k+1 length-k Fibonacci factors as a conjugate class of a
Christoffel word plus a singular factor, and gives the standard-factorization recurrence that
any Fibonacci-index ("fib-index") recurrence must thread. `status: asserted` where I rely on
it rather than recompute.

## Full text
[[berstel-christoffel-words-repetitions.full]]

```claim
id: christoffel-conjugate-and-forest
statement: For coprime a,b the lower and upper Christoffel words of slope b/a are conjugates (Cohn, de Luca–Mignosi); every nontrivial Christoffel word has a unique standard factorization (u,v) into two Christoffel words (Borel–Laubie).
hypotheses: a,b coprime positive.
holds-here: yes — applies to the Fibonacci Christoffel/standard words (slope 1/phi^2, directive all-ones).
status: proved (in source)
bearing: structural backbone for parameterizing the k+1 factors and threading Fibonacci-index recurrences.
anchor: research/summaries/berstel-christoffel-words-repetitions.md
```
