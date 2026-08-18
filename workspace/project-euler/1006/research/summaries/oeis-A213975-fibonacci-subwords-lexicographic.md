# OEIS A213975 — subwords of the Fibonacci word A003842 in lexicographic order

```claim
id: oeis-A213975-lexicographic-subwords
statement: A213975 lists the factors (subwords) of the Fibonacci word A003842
(1->12, 2->1 substitution: 12112121112...), one length at a time, in
lexicographic order; it is a catalogue, not a theorem source. The entry
restates that A003842 is Sturmian with exactly n+1 length-n factors, and its
FORMULA section gives an O(n^2) recursive construction of the length-n factor
list (extend by both letters only when u is the reverse of a prefix of the
Fibonacci word, else extend uniquely avoiding the forbidden words 22 and 111).
hypotheses: A003842 convention (1<->2 on the problem's alphabet, i.e. the
digit-complement of PE1006's S over letters {1,2}).
holds-here: no — the problem's S is A003849's complement (0=2, 1=1); factor
SETS are invariant but the numeric decimal values are not, so the lexicographic
list does not directly give Psi(k) terms. As a catalogue it also cannot give
the O(log) structure Psi(10^18) needs.
status: catalogued
bearing: none for the computation; confirms the Sturmian k+1 count for the
complement word only. The CROSSREFS document the exact Chuan-Ho locating-factors
paper (TCS 349 (2005) 429-442), which the library holds via the Sivasankar-
Rama/Lemma-2 position theorem.
anchor: research/sources/oeis-A213975-fibonacci-subwords-lexicographic.full.md
```

## What the source actually establishes

- A213975 = list of factors of the Fibonacci word **A003842** (the substitution
  1→12, 2→1 limit `12112121112...`), grouped by length and **lexicographically
  ordered**. It is a catalogue entry (OEIS), so its evidence is a
  computed/enumerated list, not an argument.
- The comment repeats the standard fact: A003842 is Sturmian, so exactly n+1
  factors of length n.
- The FORMULA gives a recursive construction of the length-n+1 list from the
  length-n list: each u in S(n) has a unique extension ux except when u is the
  **reverse of a prefix of the Fibonacci word** (then both u0 and u1 occur);
  x is chosen to avoid the two forbidden words 22 and 111. This is the
  right-special factor structure of the Sturmian word in catalogue form.
- Cross-references: Chuan–Ho "Locating factors of the infinite Fibonacci
  word" (TCS 349 (2005) 429–442) — the location/position source the library
  holds via the Sivasankar–Rama position theorem — plus Currie–Saari least
  periods, Lothaire ch. 2, Mignosi–Restivo–Sciortino forbidden factors, and
  the Wen–Wen singular words paper.

## Convention trap (why it does not directly help)

A003842 uses letters {1,2}; PE1006's S is A003849 (0,1 word, slope 1/φ²).
The digit complement 0↔1 (equivalently 2↔1) maps the factor sets onto each
other, so the *count* k+1 is the same, but the *decimal values* of the factors
— and hence Ψ(k) — change under complement. So this catalogue cannot be used
to read off the problem's Ψ(k) terms, and as a computed list it has no
bearing on the O(log) evaluation at k=10^18 either.

## Bearing

Confirmed as **peripheral**: like A344953 and the other OEIS rows, it does not
help the computation. Its only value is bibliographic — the Chuan–Ho 2005
reference for the locating-factors content already held in-library.