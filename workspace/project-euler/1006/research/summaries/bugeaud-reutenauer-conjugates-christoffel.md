# Bugeaud & Reutenauer — "On the conjugates of Christoffel words"

**Full text:** `research/sources/bugeaud-reutenauer-conjugates-christoffel-ar5iv.full.md`
(arXiv:2202.05486v5, 32 pp; published DMTCS vol. 27:3, #20, Nov 2025, DOI
10.46298/dmtcs.15140). URL:

- Full text (HTML): https://arxiv.org/html/2202.05486v5
- arXiv abs: https://arxiv.org/abs/2202.05486
- Journal: https://doi.org/10.46298/dmtcs.15140

## What this source establishes

A **Christoffel word** is the finite Sturmian word of rational slope — the word
whose conjugates are the rotations of a straight-line discretisation. Conjugates
are obtained by cyclically permuting the word.

The sentence this run needs, from the Introduction (repeated verbatim in the
full text):

> a word is a conjugate of a Christoffel word if and only if all its conjugates
> are factors of a Sturmian word; equivalently, this word (of length n say) is
> primitive and has exactly n−1 circular factors of length n−2
> (Lothaire 2002; Reutenauer 2019, Theorem 15.3.1).

**Why relevant to PE1006.** Directive 1's reduction is: at k = F_n − 1 the k+1
distinct length-k factors of the Fibonacci word are exactly the F_n rotations
(conjugates) of the truncated standard/Christoffel word. The quoted theorem is
the finite↔infinite bridge behind that: the finite conjugates' factor structure
coincides with the infinite Sturmian factor structure. It anchors the
identification of "the k+1 factors" with "the rotations of the standard word"
that underlies the cyclic-autocorrelation counting A(jp−j) in directive 1.

## What it additionally gives

- Parametrisation of the conjugates of Christoffel words by the integer
  Ostrowski numeration system (Theorem 7.3) — independent of the chosen
  Ostrowski representation. This generalises the Rauzy/de Luca–Mignosi
  standard-word constructions with Ostrowski numerals, the same representation
  used in the run's `hieronymi-decidability-sturmian-words` source and behind
  directive 1's "Euclidean/Ostrowski recursion on sum_d (a·d mod N) x^d".
- Borders/periods of conjugates: each finite Sturmian word has a nontrivial
  proper period except precisely the Christoffel words (Section 8).
- Sturmian graph / compact graph (Section 9, after Epifanio–Frougny–Gabriele–
  Mignosi–Shallit), embedded in the Stern–Brocot tree.

## What it does NOT give

- Not the specific closed form A(d) = max(0, m−t) + max(0, m−(N−t)) of
  directive 1. That cyclic pair-counting formula still has no dedicated source
  in the library; it is a rotation/balance count derivable from the standard
  word's balance structure, and remains to be verified in-container against the
  brute oracle rather than cited.
- Not a PE1006 answer. This is pure structural theory.

```claim
id: conjugate-christoffel-factor-sturmian
statement: A finite word w is a conjugate of a Christoffel word if and only if all
its conjugates (cyclic rotations) are factors of a Sturmian (infinite) word;
equivalently w is primitive and has exactly |w|-1 distinct circular factors of
length |w|-2. Hence for any n with Euler-Fibonacci index F(n) > k and k = F(n)-1,
the k+1 distinct length-k factors of the Fibonacci word (a characteristic
Sturmian word) are exactly the F(n) rotations of the standard/Christoffel word
truncated to k letters.
hypotheses: w a finite binary word; Christoffel/standard word of rational slope
with conjugate class the rotations; the surrounding infinite word Sturmian.
holds-here: yes — the run's directive-1 reduction, at k = F_n - 1, identifies the
k+1 factors with the rotations of the truncated standard word; this source is
the finite<->infinite bridge that supports it.
status: sourced
bearing: Anchors the finite/rotation side that directive 1's pair-correlation
reduction rests on (the k+1 factors = rotations of the standard word), and the
Ostrowski/standard-word parametrisation used in its O(log) recursion.
anchor: research/sources/bugeaud-reutenauer-conjugates-christoffel-ar5iv.full.md
(Introduction, the conjugation/factor bridge; Theorem 7.3; Section 9)
```

## Conclusion

This is a genuine strengthening of the finite/standard-word side of the library,
which was the thinnest axis. The primary (directive 2) mechanical-word route and
the universal-Euclidean primitive were already well anchored; this adds the
finite conjugate/rotation principle directive 1 rests on. The one load-bearing
formula still without a source (the autocorrelation A(d)) is a counting identity
to be checked against brute — it does not need a literature citation to be used,
only to be verified.
