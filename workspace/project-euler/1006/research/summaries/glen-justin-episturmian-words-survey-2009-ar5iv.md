# Glen & Justin — Episturmian words: a survey (2009)

**Source:** Glen & Justin, *Episturmian words: a survey*, RAIRO-ITA 43 (2009)
403–442; arXiv:0801.1655, full text via ar5iv at
`research/sources/glen-justin-episturmian-words-survey-2009-ar5iv.full.md`
(152 KB). This replaces the abstract-page-only download
(`glen-justin-episturmian-words-survey-2009.full.md` — do not cite that one).

## What it establishes

Canonical modern survey of Sturmian/episturmian combinatorics. Statements
bearing on PE1006:

- **Factor complexity (Thm 6.1).** A k-strict episturmian word has complexity
  (k−1)·n+1 for all n; the Sturmian n+1 (the run's
  `fibonacci-sturmian-complexity`) is the k=2 case. Consistent.
- **Palindromes (§6.2).** Episturmian words are *rich*: every length-n factor
  contains exactly n+1 distinct palindromes; palindromic complexity is 1
  palindrome per even length, one per centre per odd length (Thm 6.2).
- **Critical exponent (§6.3, Ex 6.10).** Fibonacci word (directive (ab)^ω):
  critical exponent 2+φ (Mignosi–Pirillo); k-bonacci: 2+1/(φ_k−1).
  Cross-check only — already in-library (Mousavi–Schaeffer–Shallit Thm 3.24).
- **Return words (§6.5).** Sturmian iff every factor has exactly 2 return
  words (Vuillon); episturmian Thm 6.13 gives explicit returns f⁻¹μ(x)f.
- **Lexicographic order (§7, the new substance).** min(w|k)/max(w|k) limit to
  min(w), max(w). *Sturmian inequalities* (Pirillo 2003; Veerman mid-80s): for
  standard Sturmian s on {a<b}, as ≤ min(s) ≤ max(s) ≤ bs (7.1),
  characterising standard Sturmian. Finite-word characterisation (Thm 7.5,
  Cor 7.7): w on {a,b} is **not** Sturmian iff ∃u with aua prefix of min(w)
  and bub prefix of max(w). Infinite Lyndon words in a standard subshift are
  exactly a·s (Thm 7.9).

## Why it matters here

For fixed-length binary strings val(x) is strictly monotone in lexicographic
order, so the factor set's lex structure (min/max factor, Lyndon conjugate) is
the order Ψ's sum of squares lives in. Vocabulary for any order-based G4
formulation; corroborates Christoffel/Lyndon conjugacy facts already claimed
(`bwt-standard-sturmian-characterization`). Does **not** collapse the
joint-intercept second moment — no theorem here aggregates decimal-weight
moments over the k+1 factors.

```claim
id: glen-justin-sturmian-lexicographic-inequality
statement: For a standard Sturmian word s on {a<b}, the lexicographic
extremal-factor limits satisfy as <= min(s) <= max(s) <= bs (Pirillo/Veerman,
(7.1)); and a finite word w on {a,b} is not Sturmian iff there is a finite u
with aua a prefix of min(w) and bub a prefix of max(w) (Glen-Justin-Pirillo,
Cor 7.7).
hypotheses: binary alphabet with order a<b; Sturmian = standard (characteristic)
word; min/max over the factor set of each length, limits taken.
holds-here: yes — PE1006's word is standard Sturmian (slope 1/phi^2), and its
k+1 length-k factors are totally ordered by val = lex order for fixed k.
status: asserted (survey statement, original proofs in [62, 93, 94])
bearing: Fixes the lexicographic structure of the factor set that Psi(k) sums
over; background vocabulary for any order-based attack on G4, not the collapse
itself.
anchor: research/sources/glen-justin-episturmian-words-survey-2009-ar5iv.full.md
(Thm 7.5, Cor 7.7 lines 815-868; inequality (7.1) lines 789-814)
```

## Boundaries

- Survey tier: statements cite primaries, most paywalled; treat as asserted.
- The two-letter Sturmian results apply here; the k-letter episturmian
  material (Arnoux–Rauzy, episkew, Fraenkel) does not help PE1006 directly.
- Cross-checks confirmed against held claims: complexity n+1, critical
  exponent 2+φ, exactly 2 return words per factor, richness.
