# Boyer, "A search for 3x3 magic squares having more than six square integers", 2004

[[boyer-square-of-squares-search-v2]]

Computational survey of problem (B) (magic square, maximise square entries). Documents the
six- and seven-square-entry landscape and the LS1 witness.

## Established statements

- Restates LaBar's problem and Gardner's $100 prize (1996).
- **Six square entries:** all sixteen Bremner configurations attainable (citing Bremner 2001).
  The smallest six-square magic square (magic sum 3×145):
  ```
  265  1²  13²
  7²  145  241
  11² 17²  5²
  ```
  (configuration 6.XV, centre 145 = 5·29). The two smallest with a square central cell are
  6.VII and 6.XIV, `889 697 17² / 5² 25² 35² / 31² 553 19²` etc.; squares of these two are
  similar by a Bremner correspondence.
- **Seven square entries:** up to symmetry there are eight ways to select seven entries
  (7.I–7.VII). No 7-square fully-magic example beyond Bremner's is known to the author.

## Implications for this run
- Six-square configurations all attainable ⇒ the obstruction is entirely in the seventh,
  eighth, ninth entries. This is exactly the run's "two realised + two half-realised AP
  differences" structure on the 7-square witness.
- LS1 repeatedly confirmed as the canonical 7-of-8-lines near-miss.

## Assessment
- Survey/compilation, no new proof. Valuable for the witness landscape and the six-square
  parametrisation examples; no impossibility content.

```claim
id: six-square-all-attainable
statement: All sixteen (up to symmetry) configurations of six square entries in a magic square
  are attainable with infinitely many examples; the smallest has magic sum 3·145 = 435.
hypotheses: six of nine entries are perfect squares
holds-here: yes
status: asserted (compiled from Bremner 2001)
bearing: the obstruction is purely in the 7th/8th/9th entries
anchor: research/sources/boyer-square-of-squares-search-v2.full.md
```
