# Miller 1970, "Periodic forests of stunted trees" — reference record (full text unobtainable)

**Bibliographic record for the primary source surfaced by the Rule-90 Wikipedia article and OEIS A396593.**

- **Citation:** J. C. P. Miller, "Periodic forests of stunted trees", *Philosophical Transactions of the Royal Society of London*, Series A, Mathematical and Physical Sciences, **266**(1172) (1970) 63–111. doi 10.1098/rsta.1970.0003.
- **Why the run wants it:** this is the 1970 peer-reviewed study connecting Rule 90 (the forward-difference / Pascal-mod-2 structure) to **Gilbreath's conjecture** via a forest-of-growing-trees metaphor — a primary simultaneous treatment of the run's *proved* interior claim (rule90-interior-xor). It is also the origin of the "triangular clearings" picture (a row of consecutive zeros being refilled from both ends — the consumption/regeneration story in metaphor).
- **Content (from ADS abstract + Wikipedia, not the primary text):** forests on a triangular lattice; a tree grows from each initial live cell, branching to the two nearest nodes at the next higher level, stunted where a rival branch competes; equivalent to Rule 90. Formal theory via generating functions / power series over GF(2)`φ(t)/f(t)` and a matrix formulation; base-periods vs row-periods from irreducible polynomials `f(t)`; enumerations of forests (base periods to 50); reflexive forests. Showed periodic initial conditions whose forests remain alive and whose triangular clearings stay bounded (used by Miller to design "tapestries"). The Gilbreath connection: a contiguous subsequence of {0,2} values in one row of the prime difference triangle determines the corresponding subsequence in the next row by Rule 90 (as recorded in Wikipedia and OEIS A396593).

## Why the full text could not be stored

- **Royal Society (royalsocietypublishing.org), both HTML and direct PDF endpoints:** HTTP 403 Forbidden for the downloader.
- **JSTOR (stable/73779):** returned only a JS "Client Challenge" bot-gate stub (305 bytes), no article text.
- No open-access mirror surfaced in searches. Recommended not to re-attempt these two endpoints.

## What is available instead

The Miller-1970 content this run needs is fully covered by held derived sources:
- `research/sources/wikipedia-rule-90.full.md` — the "Stunted trees and triangular clearings" section (Gilbreath/forward-difference/Rule-90 connection, the tree metaphor, Miller's periodic bounded-clearings result).
- `research/sources/oeis-A396593-run-length-of-second-entry.full.md` — cites Miller 1970 + Odlyzko 1993 and restates the {0,2}-Rule-90 expansion.
- The run's own proved `rule90-interior-xor` (research/notes/block_lemma.md) — the XOR/Sierpinski interior identification, independently derived and verified.

```claim
id: miller-1970-record
statement: Miller (1970) gives the forest-of-stunted-trees model equivalent to Rule 90 and connects it to Gilbreath's conjecture (forward difference triangle; a {0,2} subsequence in one row determines the next row's corresponding subsequence by Rule 90); develops GF(2) generating-function and matrix theory; proves periodic bounded-clearings configurations exist.
hypotheses: as reported second-hand (ADS abstract, Wikipedia, OEIS); primary text paywalled, not held.
holds-here: open (primary text not verified).
status: asserted-by-source (secondary records only).
bearing: the named 1970 primary treatment of the run's proved Rule-90 interior; full text unobtainable here.
anchor: research/summaries/miller-1970-periodic-forests-stunted-trees.md
```
