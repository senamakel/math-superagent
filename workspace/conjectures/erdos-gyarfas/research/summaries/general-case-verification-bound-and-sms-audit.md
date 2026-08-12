# General-case verification bound and the SMS n≤31 claim: exact statements, provenance, audit status

This note answers two questions for the Erdős–Gyárfás run:
(1) the exact statement and provenance of the strongest *general* (mixed, non-cubic)
lower bound on the order of a counterexample; and (2) whether the SMS repo's
`ArjunBalaji79/erdos-gyarfas-min-degree-3` claim (n≤31 ⇒ counterexample ≥ 32) has
been independently reproduced, audited, or peer-reviewed anywhere.

**Verdict in one line:** the strongest **published/peer-reviewed** general-case bound is
"any general counterexample has **more than 17 vertices**" (Royle & Markström, raw
searches n≤15 general / n≤29 cubic); the SMS repo's "≥32 vertices" is a **sole-author
preprint under submission, explicitly not independently reproduced or refereed** — the
only independent setups that corroborate any part of it reach at most n≤19 (≥20).

## (1) The exact strongest known general-case bound with its citation

**Published figure.** No counterexample to the Erdős–Gyárfás conjecture exists on
$\le 16$ vertices; any general (minimum-degree-≥3, non-regular allowed) counterexample
has **more than 17 vertices**, i.e. at least 18. This is the strongest *published*
general-case "order of a counterexample" statement.

**Provenance — what the primary sources actually report (two distinct raw magnitudes):**

- **Gordon Royle** (original "2^n conjecture" page, via Wayback): generated min-degree-3
  graphs with no edge between two degree->3 vertices and no 4-cycle using a modified
  McKay `makeg`, checked for 8-cycles; **all relevant graphs on fewer than 16 vertices
  (n ≤ 15) contain 8-cycles** — no counterexample. His relaxation note (allow a single
  degree-2 vertex) extends exclusion a little past 15 via a 1-connected construction.
- **Klas Markström** (Congressus Numerantium 171 (2004) 177–188, §4; "Extremal graphs
  for some problems on cycles in graphs"): confirms Royle's n<16 general search and then,
  in the cubic case, generated **all cubic graphs on fewer than 29 vertices** with
  Brinkmann's `minibaum`, checking for C4, C8, C16 — no counterexample. Smallest cubic
  graphs with no C4 and no C8 occur at n=24 (four; one planar = "Markström graph").

The **consolidated " >17 general / >30 cubic "** figure is the accepted summary of the
Royle + Markström searches, stated by multiple independent secondary sources:

- UCSD Erdős Problems page: "Royle and Markström showed through computer search that
  any counterexample contains more than 17 vertices, and moreover any cubic
  counterexample must contain more than 30 vertices"
  (https://mathweb.ucsd.edu/~erdosproblems/erdos/newproblems/PowerOfTwoCycles.html)
- Wikipedia "Erdős–Gyárfás conjecture"
  (https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Gy%C3%A1rf%C3%A1s_conjecture)
- Wolfram MathWorld "Markström Graph"
- Hegde–Sandeep–Shashank, arXiv:2410.22842 (abstract: "A potential counterexample would
  have at least 17 vertices; a cubic counterexample at least 30 vertices")
- Pirzada–Shah–Baskoro, EJGTA 10(1) (2022), https://doi.org/10.5614/ejgta.2022.10.1.24
  ("any counterexample must have at least 17 vertices, and any cubic counterexample at
  least 30").

**Provenance caveat (already in ROOT.md, restated precisely here):** exactly how the
published "17" follows from Royle's own stated "15" is **not documented** in the original
page. The honest reading is: raw primary searches reached n≤15 general / n≤29 cubic;
the ">17 total / >30 cubic" is the wide-cited consolidated figure. A single paper
stating exactly "17" is not identified; Markström's Congressus Numerantium 171 (2004)
is the closest single primary citation for the joint search. **Treat 15/29 as the raw
searched values and 17/30 as the published figures; state both.**

No peer-reviewed source was found that extends the **general** case beyond n=17.
The "bipartite counterexample has ≥30 vertices" bound (Nowbandegani–Esfandiari 2011,
via Hegde et al.) is for the restricted bipartite class, not general.

## (2) The SMS repo n≤31 claim — audit / reproduction / peer-review status

**What the claim is.** `ArjunBalaji79/erdos-gyarfas-min-degree-3` (sole author Arjun
Balaji, formerly at Columbia University, NY — the Zenodo preprint's affiliation
block reads "A. Balaji is with Columbia University", ORCID 0009-0005-1790-0034; the
GitHub profile lists Bangalore IN) uses SAT Modulo Symmetries (Kirchweger–Szeider SMS:
CaDiCaL + SMS canonicity propagator + Glasgow Subgraph Solver as a complete
forbidden-subgraph propagator) to decide, for each n = 17..31, whether a min-degree-≥3
graph with no C4/C8/C16 exists. **UNSAT at every n = 17..31** ⇒ every min-degree-≥3 graph
on ≤31 vertices has a power-of-two cycle ⇒ any general counterexample has **≥32
vertices**. Because general ⊇ cubic, this also covers the cubic case (≥30 → ≥32).
C32 needs 32 vertices, so n≤31 settles exactly the range where {4,8,16} are the only
admissible power-of-two lengths.

**Publication / peer-review status — NOT peer-reviewed as of the last source snapshot
(2026-07-04, Zenodo version v2).** Sources consulted in this library:

- Zenodo record 10.5281/zenodo.21190438, "Verifying the Erdős–Gyárfás Conjecture up to
  31 Vertices with SAT Modulo Symmetries", published July 4 2026, version v2,
  clearly marked **Preprint** / Open. Notes field: **"This work is under review at
  Learning on Graphs Conference 2026."** The deposited PDF is headed **"SUBMITTED TO
  IEEE ACCESS"**. (https://zenodo.org/records/21190438)
- The repository's own `verification.md`, `sms_results.md`, and README state the
  result is "Fresh computational result, **not yet independently reproduced or
  refereed**", with "a formal proof certificate (§7) as the remaining step toward a
  fully machine-checked claim."

So: as of the evidence gathered, there is **no accepted, peer-reviewed publication**
and **no independent third-party reproduction** of the ≥32 (n≤31) bound. The Zenodo DOI
is an archival preprint record, not peer review.

**What independent corroboration DOES exist (and how far it reaches):** nothing
independent reaches n≤31. The pieces, in decreasing strength:

1. **The repo's own CEGAR-SAT cross-check** (independent pure-Python solver, different
   solver library and symmetry handling): agrees with SMS as UNSAT through **n = 19**
   (bound ≥ 20). Not third-party — same author, second codebase.
2. **An informal independent exhaustive census** (MathOverflow question q/512914,
   ~2026-07) of all connected minimum-degree-3 graphs reporting the C4-or-C8-free count
   is 0 through n=19 (n=19: 22,816,929,306 graphs → 0) — **independent n≤19 agreement**
   (bound ≥ 20). This is a forum post, not peer-reviewed, and does not reach 31.
3. **nauty ground-truth anchor** (n=10, C4-only → 5, matches), **n≤16 published
   baseline reproduction** → 0, robustness across two cardinality encodings (sequential
   vs totalizer) at n∈{17,20,22,25} → 0, and a second symmetry-breaking ordering
   (colex) at n∈{17,20} → 0 (n=22,25 colex timed out at 55 min, inconclusive), plus
   positive controls (forbid only C4 → SAT at n=17,20,25,30). All **within the repo**,
   not third-party.

**Known gap / falsifier (why it is not yet machine-checkable end-to-end):** the SMS
`--lrat-output` UNSAT certificate cannot be validated by a generic checker (e.g.
drat-trim `lrat-check`) against the min-degree-3 CNF alone: the forbidden-C4/C8/C16
clauses are added by the Glasgow propagator during search and are **not RUP/RAT-derivable**
from the min-degree CNF (they remove valid min-degree-3 graphs). A referee-grade
end-to-end certificate needs the certified-SMS clause-logging machinery
(Kirchweger–Szeider et al.), which the repo lists as **future work**. Until that
lands, the UNSAT verdicts rest on trusting SMS + Glasgow + the min-degree encoding.
Falsifier: any min-degree-3 graph on n≤31 avoiding C4/C8/C16 (the repo's own
positive-control pipeline would surface it), or a genuine third-party reproduction
finding SAT at some n=17..31 — none exists.

**Internal off-by-one (flagged, not silently resolved — from github-sms-claim.md):** the
GitHub "About" description and `verification.md` headline say "every min-degree-3 graph
on **≤30** vertices" (bound ≥31), while the README body, `sms_results.md`, and the n=31
UNSAT row support "**≤31** / bound **≥32**". The stronger figure (≤31/≥32) is the one
the README, the results table, and the Zenodo abstract (which says "at most 31
vertices ... at least 32") actually support.

**SMS frontier reproducibility:** requires a Modal cloud account plus the SMS/Glasgow/
CaDiCaL builds; pinned commits are recorded but not checked out by the build script.
Local validation gates (nauty n=10, baseline n≤16, CEGAR n=17..19) run without Modal.
Not reproduced here.

## Bottom line for this run

- The safe, **published, source-backed** general bound remains **n ≥ 17** (raw searches
  to n≤15 general / n≤29 cubic, Royle & Markström; consolidated ">17/>30" in UCSD,
  Wikipedia, MathWorld, Hegde et al., Pirzada et al.). **No peer-reviewed source raises
  the general bound above 17.**
- The SMS **n≤31 / ≥32** result is the strongest *claimed* bound for BOTH the general
  and cubic cases, is the first SAT/SMS attack on the conjecture, but is **sole-author,
  preprint ("SUBMITTED TO IEEE ACCESS", "under review Learning on Graphs Conference
  2026"), not peer-reviewed, not independently reproduced, with no end-to-end
  machine-checkable certificate**. Any independent third-party setup corroborates at most
  n≤19 (≥20).
- Consequence for the run's verification thread (`threads/push-verification.md`): do
  NOT cite "≥32" as an established bound; cite it as `asserted-by-source` with the
  preprint DOI and the qualifications above. A genuine run-owned machine-checkable
  strengthening would either (a) reproduce part of the SMS range with an independent
  certified-SMS pipeline, or (b) push the general bound past 17 with a method produced
  and audited here.

```claim
id: EG-general-bound-published-17
statement: The strongest published/peer-reviewed lower bound on the order of a general (non-regular, δ≥3) counterexample to the Erdős–Gyárfás conjecture is 18: no counterexample exists on ≤16 vertices, so any general counterexample has more than 17 vertices. The raw primary searches reached n≤15 general (Royle) and n≤29 cubic (Markström); the consolidated ">17 total / >30 cubic" figure is the accepted published summary (UCSD Erdős Problems page, Wikipedia, MathWorld, Hegde–Sandeep–Shashank arXiv:2410.22842, Pirzada–Shah–Baskoro EJGTA 2022).
hypotheses: finite simple graph, δ(G)≥3, no cycle of length 2^k; the general (non-regular) case; n vertices.
holds-here: yes — this is exactly the run's verification-bound question for the general case.
status: sourced (published figure, independently restated by ≥4 secondary sources); exact provenance of "17" from Royle's "15" is not documented in the primary page — raw searched values are 15 general / 29 cubic.
bearing: Any claim that the general bound exceeds 17 must cite a source this run can audit; no peer-reviewed source does. The SMS "≥32" result is outside this claim (see EG-github-sms-n32).
anchor: research/summaries/general-case-verification-bound-and-sms-audit.md; research/ROOT.md; research/sources/arjunbalaji-zenodo-pdf.full.md
falsifier: a peer-reviewed computation that verifies a general min-degree-3 counterexample-free range strictly beyond n=16.
```

```claim
id: EG-sms-n31-not-peer-reviewed
statement: As of 2026-07-04 (Zenodo version v2), the ArjunBalaji79/erdos-gyarfas-min-degree-3 n≤31 / counterexample-≥32 result is NOT peer-reviewed, NOT published, and NOT independently reproduced: it is a sole-author preprint deposited as Zenodo DOI 10.5281/zenodo.21190438, the deposited PDF is headed "SUBMITTED TO IEEE ACCESS", the Zenodo notes say "under review at Learning on Graphs Conference 2026", and the repo's own verification.md states "not yet independently reproduced or refereed" with an end-to-end machine-checkable certificate (certified-SMS) listed as future work. Independent corroboration reaches only n≤19 (≥20): the repo's own CEGAR-SAT cross-check and an informal MathOverflow exhaustive census (n=19: 22,816,929,306 graphs → 0).
hypotheses: the SMS verification claim for general δ≥3 graphs on 17≤n≤31 vs C4/C8/C16.
holds-here: yes — this is the run's lead for a general-case verification bound past 17/15.
status: asserted-by-source (not refereed, not reproduced by any third party; corroborated independently only to n≤19).
bearing: The run must not treat "≥32" as an established bound. It is a strong but unvetted preprint lead; a legitimate machine-checkable strengthening would reproduce part of the range independently or push past 17 with an in-run audited method.
anchor: research/summaries/general-case-verification-bound-and-sms-audit.md; research/summaries/github-sms-claim.md; research/summaries/arjunbalaji-sms-verification.md; research/sources/arjunbalaji-zenodo-pdf.full.md
falsifier: (i) a peer-reviewed acceptance of the paper with the result intact; (ii) an independent third-party reproduction reaching n>19; (iii) the certified-SMS end-to-end certificate landing.
```

## Sources consulted / rejected

**Used:** Zenodo record 10.5281/zenodo.21190438 (+ its deposited PDF, fetched in full);
the SMS GitHub repo and its `sms_results.md`, `results.md`, `verification.md` (already in
library); UCSD Erdős Problems page; Wikipedia; Hegde et al. arXiv:2410.22842;
Pirzada–Shah–Baskoro EJGTA 2022; Hegde et al. abstract restating the 17/30 bounds;
Carr arXiv:2605.22844 (structure only, no new general bound).

**Rejected for this question:** Ghaffari–Mostaghim (Cayley graphs — restricted class);
Heckman–Krakovski (3-connected cubic planar — restricted class); Gao–Shan, Hu–Shen,
Hegde et al. P_k-free (restricted classes, no general order bound); Nowbandegani–
Esfandiari (bipartite ≥30 — restricted class); Sudakov–Verstraëte, Liu–Montgomery /
Montgomery cycles-expansion survey (asymptotic average-degree regime, not an order
bound on general counterexamples).
