# Torelli 2006, "Increasing integer sequences and Goldbach's conjecture" — full text

<!-- source: https://www.numdam.org/item/10.1051/ita:2006017.pdf | full text: sources/torelli-2006-increasing-integer-sequences-goldbach-pdf.full.md -->

Mauro Torelli (Univ. Milano), RAIRO-Theor. Inf. Appl. 40(2) (2006) 107–121,
doi 10.1051/ita:2006017. Full paper (Numdam PDF) now in the library. Surveys
increasing-integer-sequence (iis) classes (Goldbach, complete/practical, tournament,
MSF, sub-Fibonacci, permutation, addition-chain, binomial) with recurrences and
enumerations; Gilbreath sequences appear as one of the motivating classes.

## What it establishes (the parts that matter here)

- **Definition 3**: an iis is *Gilbreath* iff every leading entry of its iterated
  absolute-difference triangle is ≤ 1 (`a_{i,0} ≤ 1`; the ≤ 1 form removes the "2 is the
  only even prime" peculiarity — equivalently the run's reduction, stated in primoid
  coordinates). The primes' triangle: first element 1 each row.
- **Independence**: Gilbreath and Goldbach sequence classes are incomparable (example:
  1,2,3,6 is Goldbach not Gilbreath since a_3,0 = 2; 1,2,3,5,10,22,49 is Gilbreath not
  Goldbach). So GC and Goldbach are, in this framing, independent conjectures.
- **Theorem 2 (the load-bearing one for this run):** every prefix of the **primoids**
  (a_n with 2a_n+1 prime, i.e. the primes in disguise) is a *sub-permutation*:
  a_n ≤ a_{n−1} + ⌈n/2⌉, equivalently **p_{n+1} ≤ p_n + n for all n ≥ 1**, proved from
  Dusart's bounds with a computer check for the small range. This is a sharp, *proved*
  prime-gap bound: the n-th prime gap never exceeds the prime index.
- Theorem 5: a Goldbach sequence of length r has max ≥ (r+1 choose 2)+1-style lower
  bounds; enumerations tie many classes to OEIS sequences (binomial ↦ Catalan / central
  binomial; tournaments A002083; etc.).
- Conclusion's caution: "all the work concerning Gilbreath's conjecture ... is still to
  be done" — no theorem about GC itself.

## Bearing on this run

`p_{n+1} − p_n ≤ n` is the first *proven* bound available to the run on the width of the
prime-gap input feeding the {0,2} block. Combined with the block lemma (a length-N block
protects N+1 rows) it bounds how fast erosion can consume a block in terms of the prime
index; whether it can be turned into a regeneration statement is open. It also confirms
the "framework" angle: GC sits in a taxonomy of iis classes, none proved to contain the
primes in the relevant sense.

## Source status

Peer-reviewed journal (RAIRO-ITA, EDP Sciences; MSC 11Y55, 11P32, 05A15, 11B99),
open access at Numdam. Full PDF held. The bibliography (Guy §A10, Odlyzko 1993, Dusart,
Melfi, Richstein) is a useful checklist of the surrounding literature.