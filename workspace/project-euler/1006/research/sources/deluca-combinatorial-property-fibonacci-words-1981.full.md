<!-- source: https://www.mat.univie.ac.at/~slc/opapers/sc05deluca.pdf | A. de Luca, "A combinatorial property of the Fibonacci words", Information Processing Letters 12 (1981) 193-195 (Séminaire Lotharingien de Combinatoire reprint; OCR of a scan, partly garbled) -->

# A combinatorial property of the Fibonacci words — Aldo de Luca (1981)

Full text obtained (SLC scan, OCR-degraded). The two theorems are legible and
recorded below. This is the origin paper for the palindrome-factorisation
properties of finite Fibonacci words, later used by Wen–Wen, Cassaigne and
others.

## The results (decoded from the OCR)

Setup: A a finite alphabet, |A| ≥ 2, free monoid A*. The Fibonacci words are
defined inductively by

    f_1 = a,  f_2 = b,  f_{n+1} = f_n f_{n-1}   (n ≥ 1).

(Note: this is the *other* concatenation order than PE1006's S_{n+2} =
S_{n+1} S_n; the two conventions are mirror images.)

1. (Berstel, unpublished, used by de Luca) For n > 3, the Fibonacci word f_n
   has a **palindrome left factor of length |f_n| − 2**.

2. (de Luca) For all n ≥ 4, f_n is the **product of two uniquely determined
   palindrome words of lengths F(n−1) − 2 and F(n−2) + 2**, where F(n) is the
   n-th Fibonacci number (with the convention stated in the paper). Moreover
   for n > 4 the Fibonacci sequence is the *unique* sequence of words
   satisfying this property plus the requirements that each word contains at
   least two distinct letters and begins with the same letter ("b" in the
   paper's convention).

References cited in the paper: Knuth–Morris–Pratt (SIAM J. Comput. 6 (1977)
323–350); J.-P. Duval, *Contribution à la combinatoire du monoïde libre*,
Thèse d'État, Rouen 1980; J. Berstel, *Mots de Fibonacci*, Séminaire
d'Informatique Théorique 1980/81, Institut de Programmation, Paris VI.

## Relevance to PE1006

- The palindrome-factorisation of finite Fibonacci words is a structural fact
  about the very words whose limit is the run's f; it underlies factor
  structure results (e.g. the unique-special-factor/central-word theory used
  in the run's Rauzy-graph route).
- The paper is the citable source for "finite Fibonacci words have a palindrome
  prefix of length |f_n| − 2", which appears in the literature on factors of
  the Fibonacci word.
- It is a short note; the run's real workhorse sources remain the Lothaire
  chapter, Perrin–Restivo, and the factor-location papers already held.
