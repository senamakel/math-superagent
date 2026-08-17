# Librarian cycle — state-of-the-art recency check; library stands complete

## What this cycle did

A recency and completeness pass (no acquisition), against the steering rule that
gathering proceeds only against a stated gap in `research/REQUESTS.md`. Since
the last librarian verification cycle, live searches resolved every current
directly-relevant result to a text already on disk.

## Verified current (all in `research/sources/`, read first via summaries)

1. **Dumitru, arXiv:2512.24061 (Dec 2025), *Notes on the 33-point ES problem*** —
   the most recent direct attack on ES(7). SAT encoding on triple-orientation
   variables + 4-set convexity criterion + convex-layer anchoring; UNSAT only
   for anchored subfamilies; ES(7)=33 remains open; heavy-tailed runtime.
   Held: `sources/dumitru-notes-on-33-point-esz-arxiv2512.24061.full.md`.
   Live search and OpenAlex both resolve 2512.24061 to exactly this text — no
   mis-assignment.
2. **Baek–Balko SoCG 2025** (10.4230/lipics.socg.2025.13) — split k-gon
   threshold, decomposable sets, ordered-3-uniform generalization fails. Held
   (both the correct full text and the PDF conversion).
3. **Damásdi–Dong–Scheucher–Zeng saturation** — SoCG 2024 / EJC 2025 (same
   result): sat_g(n) ≤ (7/8)·2^{n-2}, ES construction saturated. Held.
4. **Koshelev–Koshka arXiv:2604.20120** (Apr 2026) and **Krapivin–Przybocki–
   Heule PointSAT** — adjacent ES-type values (hnc(4,0;4,0)=26; H(6)∩H(7)
   avoidance=23), not ES(7). Held.

So the current state of the art on the planar convex-position conjecture through
Dec 2025 is fully held; no newer direct ES(7) result exists in live search.

## Citation-graph check (both newest primaries)

OpenAlex holds **no connected works** for either 2512.24061 (Dumitru) or
10.4230/lipics.socg.2025.13 (Baek–Balko) — the records are too new to carry
reference/citation connectivity, so the graph walk returned no new leads. Not a
library gap; a data-completeness artifact of OpenAlex.

## Surfaced but not acquired (adjacent, drift-guarded)

- **Mubayi–Suk, "The ES problem and an induced Ramsey question"** (Math. Proc.
  Camb. Phil. Soc., 2019; DOI 10.1112/s0025579319000135) — concerns the
  *higher-dimensional* convex-polytope analogue ES_d (d≥3) and an induced-Ramsey
  hypergraph parameter g_k(n). Adjacent to the planar ES(n) conjecture; holds no
  information that bears on ES(n)=2^{n-2}+1. Per GOAL.md's drift guard and the
  REQUESTS steering rule, not acquired.

## Decision

**NOTHING FURTHER** to acquire. The reference library stands complete against the
current state of the art: canonical tier (ES 1935, ES 1961, Morris–Soltan survey),
all published upper bounds with exact error terms, exact values ES(3..6) with the
method that settled each, the lower-bound construction and its realizability, the
full computational/SAT/order-type landscape through Dec 2025, restricted classes
(Baek–Balko decomposable/split, Károlyi–Tóth forbidden order types, Damásdi et
al. saturation), counterexample constructions, and the Lean/Mathlib formalisation
arm. All requests answered by held primaries. Next valuable work is run-side
(the queued gsplit Phase-2 provenance re-capture), not librarian acquisition.
