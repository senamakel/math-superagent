# de Luca, "Sturmian words: structure, combinatorics, and their arithmetics" (TCS 183, 1997) — summary

Source: https://docslib.org/doc/3630572/sturmian-words-structure-combinatorics-and-their-arithmetics
(DOI 10.1016/S0304-3975(96)00310-6; Theoretical Computer Science 183 (1997) 45–82)
Full text: `research/sources/deluca-sturmian-words-structure-arithmetics-1997-docslib.full.md`
**Honest limitation:** only the abstract and full Introduction converted from the DocsLib mirror;
the numbered body sections did not. The library's Berstel DLT'95 / 2007 surveys and Lothaire C2
chapter carry the corresponding proofs in full. What this source adds is the *program* and
definitions that structurally tie the run's finite-word side together.

## What it establishes that bears on PE1006

- **The Fibonacci word as the canonical Sturmian word.** "The most famous Sturmian word is the
  Fibonacci word f which is the limit of the sequence {f_n}, f_0=b, f_1=a, f_{n+1}=f_n f_{n-1}."
  (Note: de Luca swaps the alphabet, a↔1, so his a↔1, b↔0 relative to PE1006's S_n; the
  structure is identical.) Sturmian words are "binary infinite words which are not ultimately
  periodic and of minimal subword complexity", hence exactly p(n)=n+1 factors of each length —
  the statement behind PE1006's "only k+1 distinct Fibonacci subwords".
- **Geometric definition.** A Sturmian word = the intersection codings of a lattice: horizontal
  crossing ↦ b, vertical ↦ a, corner ↦ ab/ba, of a semi-line of irrational slope. The set of
  finite subwords depends only on the slope, not the intercept — *the* reason the k+1 length-k
  factors form a fixed set.
- **Standard Sturmian words via partial quotient sequence.** Given q_0>0, q_i>0, define
  s_0=b, s_1=a, s_{n+1}=s_n^{q_n-1}s_{n-1}. The limit s is a standard Sturmian word; every
  standard Sturmian word arises so. This is the literal "doubled standard word / rotations at
  k=F_n−1" construction directive 1 uses.
- **The PER set.** PER = words w with two coprime periods p,q, |w| = p+q−2. Theorem (de Luca &
  Mignosi 1994): the finite standard Sturmian words satisfy Stand = {a,b} ∪ PER{ab,ba}. PER is
  the "kernel" of the standard Sturmian words. Palindrome left-closure (−):
  w∈PER ⟹ (aw)^(−), (bw)^(−) ∈ PER; PER is the smallest such set over {ε}.
- **Farey correspondence.** There is a natural bijection PER ↔ {irreducible p/q, p<q} via
  ||w|| = p/q (p=minimal period, q with |w|=p+q−2). For each n, A_n = {w∈PER : ||w||=p/q,
  q≤n+1, p+q−2≥n} is a biprefix code; the set of its length-n suffixes coincides with the
  right-special factors SR(n) of length n, and A_n is the left-palindrome closure of SR(n).
  **This is the standard-word side of the run's factor structure** (the k+1 factors at
  k=F_n−1 are the F_n rotations of the standard word q_n, i.e. elements of PER).

## Relation to the run

- Confirms (with the on-disk Berstel DLT'95 / 2007, Lothaire C2, Perrin–Restivo) that the
  problem's factor set is governed by one irrational slope, 1/φ².
- The PER / Farey-correspondence machinery is the theoretical home of directive 1's "at
  k=F_n−1 the k+1 factors are rotations of the standard word" and of the new contiguous-window
  reformulation (k+1 contiguous windows of the doubled standard word q_n q_n).

## Frontier / citations added

14 citations added to `derived/FRONTIER.md` (Dekking substitution-invariant Sturmian words,
O'Bryant Sturmian permutations, Berstel–Séébold morphic Sturmian words, the Christoffel-words
book, the *-Sturmian words paper, return-words characterization, etc.).
