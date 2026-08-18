<!-- source: https://fitforthem.unipa.it/rep:6533b823fe1ef96bd127f649 | record page; published: Theoretical Computer Science 82 (1991) 71-84, doi:10.1016/0304-3975(91)90172-x -->

# On the number of factors of Sturmian words — Filippo Mignosi (1991)

Status: **abstract/record page only**. Full text is paywalled (ScienceDirect,
doi:10.1016/0304-3975(91)90172-x); the Unipa repository page carries the
abstract and bibliographic record. Reported so nobody re-searches for a free
full text that is not there.

## The result (from the abstract, verbatim)

> We prove that for m ≥ 1, card(A_m) = 1 + Σ_{i=1}^{m} (m − i + 1) φ(i),
> where A_m is the set of factors of length m of all the Sturmian words and φ
> is the Euler function. This result was conjectured by Dulucq and
> Gouyou-Beauchamps (1987), who proved that this result implies that the
> language (∪_{m≥0} A_m)^c is inherently ambiguous. We also give a
> combinatorial version of the Riemann hypothesis.

## What this is and is not for PE1006

- **Not** the run's count. PE1006's F_k is the factor set of a *single*
  Sturmian word (the Fibonacci word), which has |F_k| = k + 1. Mignosi's A_m
  is the union of length-m factors over *all* Sturmian words — a different
  (larger) object, counted by the totient formula above.
- It is, however, the canonical reference for the **finite Sturmian language**
  (the set of all finite factors of Sturmian words), and it is cited in this
  role by Berstel's 2007 survey, Berthé 1996, Choffrut–Karhumäki 1997, and the
  Lothaire chapter already held. Having the record confirms the citation
  exists; the formula itself is cited in-library (e.g. in the Berstel 2007
  survey's bibliography).

## Related in-library holdings

- de Luca & Mignosi, "Some combinatorial properties of Sturmian words", TCS
  136 (1994) 361–385 — the companion paper (characterisations of finite
  Sturmian words); cited throughout the library but not itself held as a full
  text (paywalled).
- Berstel 2007 survey (`berstel-sturmian-episturmian-survey-2007.full.md`),
  Berthé 1996 (`berthe-frequences-facteurs-sturmiennes-1996.full.md`),
  Choffrut–Karhumäki 1997 (`choffrut-karhumaki-combinatorics-of-words-1997.full.md`)
  all cite and use the Mignosi enumeration.
