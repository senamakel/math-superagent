# Fici, Mantaci, Restivo, Romana, Rosone, Sciortino — "BWT and Combinatorics on Words" (Dagstuhl festschrift for Manzini, OASIcs 131, 2025)

Full text: `research/sources/fici-mantaci-restivo-romana-rosone-sciortino-bwt-combinatorics-words-dagstuhl.full.md`
(URL: https://drops.dagstuhl.de/storage/01oasics/oasics-vol131-manzinis-festschrift/OASIcs.Manzini.1/OASIcs.Manzini.1.pdf;
DOI 10.4230/OASIcs.Manzini.1; 77 KB converted, 1550 lines.)

## What it establishes

A modern survey of the Burrows-Wheeler transform (BWT) under the combinatorial point of view —
the connection to Sturmian/standard/Christoffel words, BWT runs as a repetitiveness measure, and
sensitivity to morphisms. It is the accessible replacement for the paywalled/404'd original
Mantaci–Restivo–Sciortino 2003 IPL paper ("Burrows-Wheeler transform and Sturmian words", which the
survey cites as [53]).

- **BWT definition** (Section 2): bwt(w) lexicographically sorts all cyclic rotations of w and takes
  the last character of each sorted rotation. Clustering effect: identical characters group when they
  share contexts; r(w) = number of BWT runs (maximal runs of identical chars in bwt(w)) is a
  repetitiveness measure.
- **Mantaci et al. [53] result**: the BWT can be used to characterize **standard Sturmian words**.
  Binary words with minimum r (r = 2, the alphabet size) are exactly the standard Sturmian words:
  the BWT produces total clustering of all occurrences of each character. (This is the "extremal
  case" of the clustering effect for binary alphabets, Section 5.)
- **Perfectly clustering words** (Section 5): words whose BWT produces lexicographically decreasing
  maximal runs; the first combinatorial characterization was established only recently [43].
- **Standard Sturmian words** (Section 3, definition): a Sturmian word is standard if every prefix is
  left special (and therefore the only left special factor of that length). Directive-sequence
  construction: s_0 = b, s_1 = a, s_{n+1} = s_n^{d_n} s_{n-1}, with d_1 ≥ 0, d_i > 0. **The Fibonacci
  infinite word is standard Sturmian with directive sequence d_i = 1 for every i; its standard
  sequence is the Fibonacci words f_0 = b, f_1 = a, f_n = f_{n-1} f_{n-2}.**
- **Christoffel words** (Section 3): a binary word is a Christoffel word iff it is the lexicographically
  minimal (Lyndon) conjugate of a standard word (standard words are always primitive).
- **Left-special characterization of Sturmian**: an infinite binary word is Sturmian iff it has exactly
  one left special factor of length n for each n ≥ 0 (equivalently one right special factor) — cited
  to [48]. This matches claim `fibonacci-unique-special-factor-reverse` (the unique right-special factor
  of the Fibonacci word is the reverse of the length-n prefix).
- **Morphism sensitivity** (Section 6): injective binary morphisms always increase or preserve the BWT
  run count r; the Sturmian morphisms are the only ones that preserve it.

## Relevance to PE1006

- Confirms from a different, modern source that the Fibonacci word is the standard Sturmian word of
  directive sequence all-1s, with the finite standard words being exactly the S_n of the problem
  (f_n = f_{n-1} f_{n-2}).
- The left/right-special characterization (exactly one special factor per length) is the same
  special-factor structure Cassaigne's Prop 3.1 quantifies for the Fibonacci word (s(n) = p(n+1) − p(n) = 1),
  and that the run's adopted Rauzy/right-special-extension route uses.
- The BWT/rotation viewpoint (lex-sorted conjugates of standard words) is the same orbit
  structure the run's Christoffel-conjugacy approach used (k rotations of one Christoffel word +
  one singular factor); this survey is the modern reference for the perfectly-clustering / Christoffel
  conjugacy facts behind that approach.

## Claim block

```claim
id: bwt-standard-sturmian-characterization
statement: The BWT characterizes standard Sturmian words: a binary word has the minimum possible
number of BWT runs (total clustering of each character) iff it is a standard Sturmian word
(Mantaci–Restivo–Sciortino, cited as [53] in this survey). Equivalently, an infinite binary word is
Sturmian iff it has exactly one left special factor of length n for each n >= 0. The Fibonacci word
is the standard Sturmian word with directive sequence d_i = 1 for all i, whose standard words are
f_0 = b, f_1 = a, f_n = f_{n-1} f_{n-2} — exactly the S_n of PE1006 (up to the 0/1 complement
convention). A Christoffel word is the lexicographically minimal (Lyndon) conjugate of a standard word.
hypotheses: binary alphabet, standard (lexicographic) order; BWT of finite words; Sturmian = balanced
aperiodic binary word.
holds-here: yes — PE1006's S_n are the standard Fibonacci words; the factor set of each length is the
set of conjugates (rotations) of the standard word plus the singular factor, matching the run's
christoffel-conjugacy approach.
status: sourced
bearing: Modern accessible source (CC-BY open access) for the standard-Sturmian/Christoffel structure
of the Fibonacci word and its rotations; replaces the paywalled original Mantaci–Restivo–Sciortino
2003 IPL paper as the in-library anchor for the BWT/conjugacy axis.
anchor: research/sources/fici-mantaci-restivo-romana-rosone-sciortino-bwt-combinatorics-words-dagstuhl.full.md
  (Sections 3 and 5; lines 95, 139-141, 225-250)
```

## Acquisition notes

- The DIMACS workshop PDF (http://dimacs.rutgers.edu/Workshops/BWT/bwt10.pdf) is 404; the Dagstuhl
  festschrift chapter is the accessible modern survey of the same Mantaci–Restivo–Sciortino line and is
  CC-BY open access.
- The original Mantaci–Restivo–Sciortino 2003 IPL article remains paywalled at Elsevier; its statement
  is captured here via the survey's citation.
