# Claim — Fibonacci word is palindromically rich (Glen–Justin–Widmer–Zamboni)

Source: Amy Glen, Jacques Justin, Steve Widmer, Luca Q. Zamboni, "Palindromic
richness", European J. Combin. 29 (2008) 510–531, arXiv:0801.1656. Held in the
library at `research/sources/glen-justin-widmer-zamboni-palindromic-richness-ar5iv.full.md`
(ar5iv full text; URL recorded in-file).

```claim
id: fibonacci-word-palindromically-rich
statement: The Fibonacci word f (PE1006's S_n limit, fixed point of 0->01, 1->0)
is a rich (palindromically rich) infinite word: every length-k factor u of f
contains exactly |u|+1 = k+1 distinct palindromic factors (including the empty
word). Equivalently (Droubay–Justin–Pirillo), every prefix of every factor has
the property that its longest palindromic suffix occurs exactly once in it;
equivalently (Thm 2.14 of the source), every complete return to a palindromic
factor of f is itself a palindrome. More generally, every episturmian word is
rich (source, after Droubay–Justin–Pirillo 2001); Sturmian words are a subclass
of episturmian words; the Fibonacci word is Sturmian.
hypotheses: f the infinite Fibonacci word in the 0->01, 1->0 convention;
"palindromic factor" counts the empty word; richness means the maximal number
|w|+1 of distinct palindromic factors is attained for every factor w.
holds-here: yes — f is exactly PE1006's S_n limit (Sturmian, hence
episturmian, hence rich).
status: sourced
follows-from: Sturmian => episturmian => rich (Droubay–Justin–Pirillo,
Prop. 2.11 + Thm 2.14 of the source); the Fibonacci word's Sturmian identity
is anchored separately in the library (Lothaire C2, Perrin–Restivo).
bearing: Third independent characterisation of the factor set of f (palindromic
complexity), alongside factor complexity p(k)=k+1 and balance. Confirms the
structural picture of F_k but does NOT bear on the decimal second moment
Psi(k): no moment/weighted-sum statement over the factor set appears in this
paper. Relevant only as background corroboration for G4, not as an engine for
it.
anchor: research/sources/glen-justin-widmer-zamboni-palindromic-richness-ar5iv.full.md
(Def 2.2-2.3, Prop 2.11, Thm 2.14, Thm 5.2, Cor 5.6; lines 63-198, 173-184,
371-448)
```

## Corroboration

- The held Glen–Justin survey (`glen-justin-episturmian-words-survey-2009-ar5iv.full.md`)
  §6.2 reports the same palindromic-complexity statements; the primary now held
  gives full proofs.
- Held Berstel 2007 survey (§ on palindromic complexity) corroborates Sturmian
  = rich with palindrome complexity h(n) = 1 + (n mod 2).

## Boundary

Richness counts distinct *palindromic* factors; PE1006's Ψ(k) is a sum of
squares of decimal values over *all* length-k factors. The two counts coincide
only in that both are "k+1" for Sturmian words — a coincidence of complexity
values, not an identity of objects. Do not use this claim to move the sum of
squares onto palindromes.
