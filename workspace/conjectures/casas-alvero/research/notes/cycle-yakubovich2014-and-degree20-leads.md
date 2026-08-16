# Library cycle report: Yakubovich 2014 survey held; two degree-20 dissertation leads blocked

## What is now held (primary source, full text)

**Yakubovich, *Polynomial problems of the Casas-Alvero type*, J. Classical Analysis 4(2) (2014) 103–120.**
Downloaded full text: `research/sources/yakubovich2014_casas-alvero-type-survey.full.md`
(summary: `research/summaries/yakubovich2014_casas-alvero-type-survey.md`).
Landing page `doi:10.7153/jca-04-07` held only an abstract stub; the real PDF is at
`http://files.ele-math.com/articles/jca-04-07.pdf` (open access).

Four claim blocks written from it, all in the claims ledger (search_claims → `y2014-*`):
- `y2014-ab-goncharoff-ca-representation` — CA reduces by scaling to common roots in the unit circle (Prop 1).
- `y2014-real-rooted-ca-holds` — CA holds for real-rooted polynomials; real-rooted counterexample (if any) has ≥5 distinct zeros (Prop 2, Cor 11).
- `y2014-sz-nagy-root-derivative-identity` — Sz.-Nagy identities (Lemma 1) and the necessary inequalities (44),(46),(47) any real-rooted counterexample must satisfy (Props 3–5).
- `y2014-trivial-iff-double-root-n-2` — real-rooted degree-n≥2 is trivial iff its (n−2)-nd derivative has a double root (Cor 1).

This is the source closest to the run's adopted `root-difference-coloring` thread: it supplies the
Abel–Gontcharoff form, the Sz.-Nagy identities, and the unit-circle reduction that thread's
verification script exercises. The full text lets the thread check its own identity verification
against a published derivation (see THREADS.md → root-difference-coloring).

## Leads found but NOT yet held (could not be downloaded this cycle)

### Chávez Martínez 2018 (degree-20 fixed-roots) — ***lead only, not established***
Yemile del Socorro Chávez Martínez, *La Conjetura de Casas-Alvero para un número fijo de raíces*,
PhD thesis, Univ. de Cantabria, 2018 (dirs. Laureano González-Vega, Luis Felipe Tabera).
Handles `hdl.handle.net/10902/15246` and `repositorio.unican.es/xmlui/handle/10902/15246` both block
direct download (tool error). Per the repository's own abstract and the Dialnet synthesis (which I have
NOT downloaded as a source), it claims:
- CA holds in degree 20 for polynomials with exactly 4, 5, or 6 distinct roots, via a
  Gröbner-basis-of-the-last-k-derivatives strategy;
- 627 multiplicity partitions of degree 20 enumerated, 45 trivial, 302 of 627 confirmed;
- CA holds for 2 and 3 distinct roots in char 0 generally;
- it corrects the statement (and proof) of one theorem from earlier literature ([6]);
- a tropical example where CA holds classically but fails tropically.

**Status: LEAD.** None of the above is asserted by a held source; it comes from the repository's own
abstract and a synthesis tool. The existing claim `settled-classes` and `at-least-five-distinct-roots`
do NOT yet include it. Do not cite it as established until the full PDF is held. The gap is recorded in
Cognee (memory id 8103727796861295815) and in the frontier.

### Frutos Marín 2013 (arithmetic perspectives) — lead
Rosa María de Frutos Marín, *Perspectivas aritméticas para la Conjetura de Casas-Alvero*, PhD thesis,
Univ. de Valladolid, 2013 (dir. Antonio Campillo). The bitstream `uvadoc.uva.es/bitstream/10324/3602/1/TESIS367-130927.pdf`
is named in the repository but direct download fails. Abstract (held only as search result) claims:
CA is equivalent to a purely arithmetic problem (a discriminant per degree n whose non-vanishing is
equivalent to CA for that degree), plus a modular/p-prime formulation (7 weighted projective schemes),
an "expansion principle" (p effective for n ⇒ CA for all degrees n·p^ℓ), and truth for many n with ≤3
prime divisors. Not yet a held source.

## What this means for the run
The `root-difference-coloring` thread now has its primary analytical source in the library. The
degree-20 frontier gained two candidate restricter results (fixed small number of distinct roots ⇒ CA,
and ≤3-prime-divisor degrees), but neither is yet citable from a held source — both are leads for a
later cycle to fetch via a different route (Dialnet, director's page, or the published version).
