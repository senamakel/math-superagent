# Bugeaud & Reutenauer — "On the conjugates of Christoffel words" (arXiv full text)

**Full text:** `research/sources/bugeaud-reutenauer-conjugates-christoffel-ar5iv.full.md`
(arXiv:2202.05486v5 HTML, 133 KB). Journal: DMTCS 27:3 #20 (2025),
DOI 10.46298/dmtcs.15140. This is the verbose arXiv version of the same paper
whose record page is `bugeaud-reutenauer-conjugates-christoffel-2025.md`.

**The run's real summary of this source** (with the claim block) is at
`research/summaries/bugeaud-reutenauer-conjugates-christoffel.md` — read that,
not this file. In brief:

- **Finite↔infinite bridge (load-bearing for directive 1):** *a word is a
  conjugate of a Christoffel word if and only if all its conjugates (cyclic
  rotations) are factors of a Sturmian word; equivalently it is primitive and
  has exactly |w|−1 circular factors of length |w|−2* (Lothaire 2002;
  Reutenauer 2019, Thm 15.3.1). This anchors the run's claim
  `conjugate-christoffel-factor-sturmian`: at k = F_n − 1 the k+1 length-k
  factors of the Fibonacci word are the F_n rotations of the truncated
  standard/Christoffel word.
- Conjugates of Christoffel words are parametrised by the integer Ostrowski
  numeration system (Thm 7.3), generalising Rauzy / de Luca–Mignosi standard
  words — the same Ostrowski axis as the run's hieronymi source and directive
  1's O(log) recursion.
- Borders/periods of conjugates: each finite Sturmian word has a nontrivial
  proper period except precisely the Christoffel words (Section 8).
- **Not in this paper:** the cyclic-autocorrelation closed form
  A(d) = max(0, m−t) + max(0, m−(N−t)) of directive 1; that remains a
  verify-in-container identity, not a cite.