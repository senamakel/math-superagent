# Buell, "A search for a magic hourglass", 1999/2004

[[buell-search-for-magic-hourglass-1999]]

**Status: no readable full text on disk, and this was re-confirmed this cycle.**
The paper exists only as the PDF at `http://www.multimagie.com/Buell.pdf` (101 Kb;
also listed on the MULTIMAGIE "Magic squares of squares" page ref [12]). No arXiv
version exists, and no other host was found. The PDF's text layer is corrupt —
both a direct fetch and a Wayback Machine snapshot
(`https://web.archive.org/web/2019id_/http://www.multimagie.com/Buell.pdf`)
return the same mojibake (broken DVI-to-PDF byte soup, no recoverable body).
This is a **permanent acquisition failure, not a transient one**: the corrupt
bytes are identical on both hosts, so the file itself is bad, not the route.
Do not re-fetch it. The paper's content is known through citations in Bremner II
(2001), Zimmermann–Loria (2015), and Michaud-Rodgers (2019), all on disk.

## What the citations establish (secondary-sourced)
- **Buell's hourglass bound.** Duncan Buell "A search for a magic hourglass"
  (preprint cited in Bremner 2001, Zimmermann 2015) showed by a careful search
  that there is **no seven-square magic-square "hourglass" configuration whose
  central element is less than `25×10²⁴`**. This is the origin of the
  frequently-quoted "centre > 25×10²⁴" bound. Bremner II 2001 states it
  verbatim: "no seven-square magic square corresponding to the 'hour-glass'
  configuration in which the central element of the square is less than
  25·10²⁴." Method per Boyer (`boyer-square-of-squares-search-v2`): hourglass =
  configuration 7.I; Buell studied it in 1998; a line through the centre with
  two squares around it is an integer solution of x² + y² = 2C, and the search
  parametrises the required pairs/triples of such lines.
- **Zimmermann–Loria's correction.** Buell assumed that in each pair of
  diagonals and the central column the three entries are **coprime**.
  Zimmermann–Loria show this assumption does not necessarily hold, and
  (relaxing it) find hourglass solutions with central element only ~10 digits
  congruent mod `2⁴⁷`, i.e. far below Buell's bound. So **Buell's `25×10²⁴`
  applies only under his coprimality hypothesis** and does not rule out
  hourglasses in general.
- **Verification by re-search.** Morgenstern (June 2014, "Three new searches for
  a magic hourglass", `morgenstern-hourglass-searches-2014`) re-ran the same
  formulas with pairs instead of triples (strictly wider range than Buell, since
  `m²+n² = r²+s² = (u²+v²)t` with non-square t) and again found no solutions —
  his Search 3 "serves as a verification that the Buell search cor[rectly]
  found no solutions".

## Implications for this run
- When the run (or CONTEXT.md) quotes "centre > 25×10²⁴", it must be attributed
  precisely: Buell proved it for the **hourglass configuration** (7 squares:
  two diagonals + central column), **not** for the full 3×3 MSS, and **only
  under a coprimality assumption that Zimmermann–Loria relaxed**. The full-MSS
  centre has no comparable proven bound. Michaud-Rodgers cites the bound for
  the full problem ("central element > 25×10²⁴, so probably not"), which is a
  mis-attribution the run must not copy.
- This is a standing instance of "an impossibility lemma restated too broadly
  is false".

## Assessment
- **Canonical correction recorded.** The `25×10²⁴` hourglass bound is real but
  narrow (hourglass + coprime); do not reuse as a general MSS centre bound.
- The claim block below is `asserted` (secondary-sourced) and must stay that
  way; the primary text is unobtainable in readable form.

```claim
id: buell-hourglass-25e24-coprime
statement: Buell's search shows no 7-square magic hourglass with centre < 25×10²⁴,
  under a coprimality assumption on the diagonal/column triples; Zimmermann-Loria
  relax that assumption and find much smaller (10-digit) hourglass solutions
  mod 2^47; Morgenstern's 2014 pair-based re-search (wider range) found none.
hypotheses: hourglass configuration (two diagonals + central column, 7 squares);
  Buell: the triples in each line coprime
holds-here: for the hourglass only; NOT a general MSS centre bound
status: asserted (secondary-sourced; primary PDF text layer corrupt at all hosts)
bearing: corrects the run's centre-bound quotation; a caution against
  over-broad impossibility lemmas
anchor: research/summaries/bremner-on-squares-of-squares-II-2001.md,
  research/summaries/zimmermann-loria-magic-squares-of-squares-2015.md
```

```claim
id: buell-fulltext-corrupt-unobtainable
statement: Buell's "A search for a magic hourglass" PDF (multimagie.com/Buell.pdf)
  has a corrupt text layer; identical mojibake from the original and from the
  Wayback Machine. No arXiv version or alternate host exists. Full text is not
  obtainable; all knowledge of the paper is via Bremner II 2001, Boyer 2004,
  Zimmermann-Loria 2015, and Morgenstern 2014.
hypotheses: —
holds-here: yes
status: checked (two independent fetch routes, both corrupt)
bearing: stops future re-fetch attempts; forces the 25×10²⁴ claim to stay
  secondary-sourced
anchor: research/summaries/buell-search-for-magic-hourglass-1999.md
```