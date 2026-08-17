# Harborth 1978, "Konvexe Fünfecke in ebenen Punktmengen" — attempted, article not yet obtained

**answers:** (none — this closes nothing; it records a genuine gap)

This cycle attempted to put the Harborth primary in the library, because the run's own
digests cite "g(5)=10 Harborth" (the exact value of the empty-pentagon number, an
ES-adjacent result) without holding the primary. The attempt failed twice; recorded
honestly so a later cycle does not repeat dead URLs:

- **Attempt 1** — `https://doi.org/10.5169/seals-32945` (E-Periodica DOI) returned
  the *table of contents* page of Elemente der Mathematik Band 33 (1978), not the
  article. Held at `research/sources/harborth-1978-konvexe-fuenfecke-in-ebenen-punktmengen.full.md`
  (324 lines). The TOC shows the article is "Konvexe Fünfecke in ebenen Punktmengen",
  Heft 5, page 116, PDF at the `cntmng` link for the issue.
- **Attempt 2** — `https://www.e-periodica.ch/cntmng?pid=edm-001%3A1978%3A33%3A%3A230`
  (the TOC's own PDF-link address pattern) returned a 158-byte "Redirecting" stub,
  no article text. The E-Periodica PDF endpoint needs browser context (cookie/session)
  this runtime's fetch does not carry; the downloader recorded duplicates under the
  `-in-ebenen-punktmengen` name rather than overwriting.

**What is and is not held therefore:**
- Held: the exact bibliographic pointer (journal, volume, year, page 116, Heft 5),
  enough to cite it; the fact that the paper exists where the digests said it does.
- NOT held: the article text. The g(5)=10 value remains **asserted-by-secondary-source**
  (Morris–Soltan survey and the run's digests), not verified against the primary.
  The claims ledger should keep that status; nothing in this run's load-bearing path
  currently depends on g(5) (it is recorded as ES-adjacent context), but if it ever
  becomes load-bearing it must be fetched from a different route (a library scan,
  the journal's alternate host, or a citing paper's full statement).

**Falsifier to record:** if a later fetch shows the value is not 10, or attributes
the empty-pentagon computation to a different author/year than Harborth 1978, the
secondary-source citations must be corrected. No such contradiction is known now.

Do not re-try the two URLs above; they are recorded dead for this runtime. The
frontier entry for the Harborth DOI (10.5169/seals-32945) already sits in the
library's own citation graph.