# Glen, Justin, Widmer & Zamboni, "Palindromic Richness"

**Primary.** Amy Glen, Jacques Justin, Steve Widmer, Luca Q. Zamboni,
*Palindromic richness*, European J. Combin. 29 (2008) 510–531,
doi:10.1016/j.ejc.2008.04.006. Full text via ar5iv from the arXiv preprint
0801.1656: `research/sources/glen-justin-widmer-zamboni-palindromic-richness-ar5iv.full.md`
(URL recorded in-file: https://ar5iv.labs.arxiv.org/html/0801.1656). 151
citations (OpenAlex). This is the primary that the held Glen–Justin survey
(`glen-justin-episturmian-words-survey-2009-ar5iv.full.md`, arXiv:0801.1655)
reports on; the survey and the primary are a pair, and until this download the
library held only the survey.

## What it establishes

**Rich words.** A finite word w is *rich* if it contains the maximum possible
number of distinct palindromic factors, namely |w|+1 (including the empty
word); equivalently every prefix of w has Property Ju (its longest palindromic
suffix occurs exactly once in the prefix) — this equivalence is the
Droubay–Justin–Pirillo theorem [13]. An infinite word is rich if all its
factors are. The same class was found independently by Ambrož–Frougny–
Masáková–Pelantová ("full words") and Brlek–Hamel–Nivat–Reutenauer.

- **Theorem 2.14**: an infinite word is rich iff every complete return to any
  palindromic factor is itself a palindrome.
- Episturmian words (hence Sturmian words, hence the Fibonacci word) are rich:
  any factor u of an episturmian word contains exactly |u|+1 distinct
  palindromic factors.
- **Theorem 5.2**: recurrent balanced rich infinite words are precisely the
  balanced episturmian words. Corollary 5.6: recurrent balanced rich words with
  mutually distinct letter frequencies are Sturmian or Fraenkel-type.
- Section 5 recalls: Sturmian words are precisely the aperiodic balanced
  infinite words on a 2-letter alphabet; in a balanced word the gaps between
  successive occurrences of any letter take values in {k, k+1}; any recurrent
  balanced infinite word over >2 letters is periodic.

## Bearing on PE1006

The Fibonacci word f (PE1006's S_n limit) is Sturmian, so it is rich: every
length-k factor of f contains exactly k+1 distinct palindromic factors, and all
complete returns to its palindromic factors are palindromes. This is a third,
independent characterisation axis (palindromic complexity) corroborating the
Sturmian identity of f that the run already anchors by factor complexity
(p(k)=k+1, Lothaire C2 / Perrin–Restivo / Morse–Hedlund) and by balance
(Sturmian = aperiodic balanced binary). It does **not** bear on the decimal
second moment Ψ(k): rich/palindromic structure is about *distinct palindromic
factors*, whereas Ψ sums squares of *decimal values of all factors*. No
moment/weighted-sum statement for the factor set appears anywhere in the paper.

## Relationship to the held library

- The Glen–Justin survey (0801.1655) is the survey version; this paper is the
  primary with full proofs.
- §6's P-morphisms (Hof–Knill–Simon) and §5's balance results connect to the
  held episturmian/morphism tier (Justin–Pirillo 2002, Berstel 2007).
- The palindromic-complexity axis is otherwise represented in-library only via
  survey statements (Glen–Justin survey §6.2, Berstel 2007); this is the first
  primary text held for it.

## Bibliographic notes for the frontier

The reference list (lines 979–1026 of the full text) cites the canonical
palindromic-complexity literature: Allouche–Baake–Cassaigne–Damanik (TCS 292,
2003), Brlek–Hamel–Nivat–Reutenauer (IJFCS 15, 2004), Baláži–Masáková–
Pelantová (TCS 380, 2007), Droubay–Justin–Pirillo (TCS 255, 2001), Justin–
Pirillo (TCS 276, 2002) — all already present in the frontier/library as
citations of held surveys; none is a new gap.
