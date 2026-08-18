# Library cycle — Frougny Cobham/Bès anchor + Ostrowski/local-period side

## What this cycle added and why

The Cobham/Bès claim (`cobham-bes-frougny-multiplicatively-independent-
conversion`, which refutes the Zeckendorf automatic digit-DP route) cited
Frougny RAIRO-ITA 36 (2002) 143–157 as its PRIMARY anchor, but that paper was
**not on disk**. The rest of the run had been reasoning from the claim's
one-line statement without being able to read the source that fixes it. That
was exactly the "cited but absent" failure this role exists to prevent.

**Fixed.** Downloaded the author-hosted PDF:
`research/sources/frougny-mult-dep-linear-numeration-2002-irif.full.md`
(from https://www.irif.fr/~cf/publications/lucas.pdf, found via exa_search —
not an invented address).

### What the Frougny paper actually establishes (digest, full text on disk)

The abstract and theorems confirm the claim's content precisely:

- Two linear numeration systems whose characteristic polynomials are the
  minimal polynomials of (multiplicatively dependent) Pisot numbers β, γ have
  **conversion computable by a finite automaton**.
- **Theorem 2**: β, γ multiplicatively dependent Pisot numbers ⇒ conversion
  from the γ-system to the β-system is finite-automaton computable.
- **Corollary 1**: a set U-recognizable is γ-recognizable (automaton
  recognisability transfers between multiplicatively dependent Pisot bases).
- **Proposition 8**: there exists a linear recurrent sequence whose set of
  normal representations is NOT recognizable by a finite automaton — the
  boundary case showing automaton recognisability is genuinely restricted.
- Section on Bès's generalisation of Cobham's theorem (quoted in the intro:
  "The generalization of Cobham's Theorem by Bès is the following: let two
  linear numeration systems such that their characteristic polynomials are the
  minimal polynomials of two multiplicatively independent Pisot numbers…").

Since 10 = (10) and φ = (1+√5)/2 are multiplicatively independent Pisot
numbers, decimal and Zeckendorf/Fibonacci representations cannot be jointly
processed or converted by a finite automaton. This is the exact statement the
Cobham/Bès claim rests on, now readable from a source on disk.

## Frontier walk — Sturmian graphs → Ostrowski/local period side

Walked `citation_graph` on EFG+12 (Epifanio–Frougny–Gabriele–Mignosi–Shallit,
"Sturmian graphs and integer representations over numeration systems"). Two
citers were directly on the Ostrowski/local-period axis the directive-9
contiguous-window route and the mechanical floor-sum route touch:

1. **Schaeffer, "Ostrowski Numeration and the Local Period of Sturmian Words"**
   (arXiv:1210.2343) — downloaded:
   `research/sources/schaeffer-ostrowski-local-period-sturmian-2012.full.md`.
   Treats the local period p_x(n) of Sturmian words via Ostrowski numeration;
   reproduces the Mignosi–Restivo extremal local-period result and develops
   the Ostrowski representation of positions in a Sturmian word — the
   position/factor-index machinery.
2. **Frid, "Sturmian numeration systems and decompositions to palindromes"**
   (arXiv:1710.11553, EJC 71 (2018) 202–212) — downloaded:
   `research/sources/frid-sturmian-numeration-palindromes-2018.full.md`.
   Extends Ostrowski numeration systems to reflect the structure of
   characteristic Sturmian words; links representations to occurrences of
   factors/palindromes in the characteristic word. Relevant to the O(log)
   index/Ostrowski evaluation side.

The Hieronymi–Shallit "Decidability for Sturmian words" (arXiv:2102.08207)
citer is already on disk as `hieronymi-decidability-sturmian-words-ar5iv.full.md` — not re-downloaded.

## Morse–Hedlund 1940 — still a recorded gap

The frontier's top row (Symbolic Dynamics II, cited by 4 of our sources)
remains paywalled: JSTOR and MathSciNet require subscription; the Internet
Archive microfilm scan of AJM vol. 62 (1931–1961 scans) could not be resolved
to a stable direct URL this cycle. Its substance — factor complexity n+1 for
a Sturmian word, minimal complexity — is anchored redundantly on disk
(Lothaire C2, Berstel DLT'95/2007, Perrin–Restivo Theorem 1, Wikipedia
Fibonacci word). Kept as a recorded honest gap, not a search-budget sink.

## What could not be obtained (recorded)

- Chuan "Moments of conjugacy classes of binary words" (TCS 2003 — actually
  TCS 310 (2004) 273–285): ScienceDirect only, no free scan. The conjugate
  side is already anchored by Currie–Saari Cor 6 + Bugeaud–Reutenauer +
  Sivasankar–Rama Thm 7, so not a load-bearing gap.
- Berstel "Fibonacci Words — A Survey" remains a bibliographic-only record
  (no uncontaminated full text reachable); covered by the 2007 survey and
  Lothaire.
- Morse–Hedlund 1940 (above).

## Net effect for the run

- `cobham-bes-frougny-multiplicatively-independent-conversion` now points at a
  real file whose Theorem 2 / Corollary 1 / Prop 8 match its statement.
- The Ostrowski/local-period factor-index side of the mechanical floor-sum and
  contiguous-window routes has two new primary sources on disk.
