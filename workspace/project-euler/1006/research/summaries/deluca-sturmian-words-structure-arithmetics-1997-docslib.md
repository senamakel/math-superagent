# de Luca, "Sturmian words: structure, combinatorics, and their arithmetics" (TCS 183, 1997) — docslib duplicate

Source: https://docslib.org/doc/3630572/sturmian-words-structure-combinatorics-and-their-arithmetics
(DOI 10.1016/S0304-3975(96)00310-6)
Full text: [[deluca-sturmian-words-structure-arithmetics-1997-docslib.full]]

## This file is a duplicate of an already-digested note

The fully digested note lives at `research/summaries/deluca-sturmian-words-structure-arithmetics-1997.md`
(intro + abstract converted from the same source; full body could not be
obtained — the DocsLib mirror converted only abstract + Introduction).
This docslib-named file is the same source and carries no additional body
text (the numbered sections did not convert).

## What de Luca 1997 establishes (summary, see the note for the claim block)

- Fibonacci word = the canonical Sturmian word; Sturmian = binary, non
  ultimately periodic, minimal subword complexity p(n) = n+1 — the fact behind
  PE1006's "only k+1 distinct Fibonacci subwords" (`standard-sturmian-PER-farey-construction`,
  `governing-factor-complexity`).
- Geometric (lattice-cut) definition: factor set depends only on slope, not
  intercept.
- Standard Sturmian words via partial-quotient recursion s_{n+1} = s_n^{q_n-1} s_{n-1}
  — the "doubled standard word / rotations at k=F_n−1" construction of directive 1.
- PER set = words with two coprime periods p,q, |w| = p+q−2; Farey correspondence
  PER ↔ irreducible p/q; A_n suffixes = right-special factors.

## Verdict

**Already covered.** No new statement beyond the de Luca 1997 note already
filed and the Berstel DLT'95 / 2007, Lothaire C2, Perrin–Restivo texts on
disk. Claim `standard-sturmian-PER-farey-construction` is anchored to the
non-docslib note. Nothing here is new; do not re-read this file.

## Claims anchored here

None (see the sibling note `deluca-sturmian-words-structure-arithmetics-1997.md`).
