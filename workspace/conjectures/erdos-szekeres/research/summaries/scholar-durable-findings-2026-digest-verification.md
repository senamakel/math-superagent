# Durable findings — verified this cycle (Cognee stand-in; memory server down)

The memory server's health check is not answering, so `remember_memory` would
accept-and-drop. Per the documented workspace convention these source-backed,
verified findings are stored here for a later pass to push to Cognee once the
server recovers. Each is verified against the primary full text on disk.

---

## F1 — Dumitru arXiv:2512.24061 encoding numbers (verified against paper body)

The 33-point ES(7) SAT instance: **578,336 variables** (5456 triple-orientation +
572,880 4-set selectors, 14 per 4-set) and **16,670,808 clauses** (9,493,440
reduced 5-point CC constraints + 2,905,320 4-set consistency + 4,272,048
no-convex-7-set, each of length 280). The 4-set convexity criterion (Proposition 1)
is exactly this run's `es35-four-criterion`. UNSAT certificates only for convex-
layer-anchored subfamilies; heavy-tailed runtimes (2.5e3–2.28e6 s); **ES(7)=33
remains open.** Soundness: a reduced (clause-omitting) relaxed UNSAT is a valid
certificate because omission only enlarges the admissible assignment set.
Claim `dumitru-es7` (asserted). Anchor: `research/sources/dumitru-notes-on-33-point-esz-arxiv2512.24061.full.md`.

## F2 — PointSAT arXiv:2607.02958 (verified against full text)

h(6,7)=24 (largest R² general-position set with no 6-hole or 7-gon has 23 points) —
**adjacent** hole/gon result, not ES(7). On the ES(7)-critical 32-point no-7-gon
problem: 2191 core-hrs, 200,000 abstract order-type solutions, **zero realizable
found** — evidence only, the abstract space was not exhausted; the 32-point case
has fewer flippable orientations (0.9% vs ≥1.2%) and mean 121.6 partial-realization
violations (vs ≤38), so added problem-specific difficulty. Consistent with SMQH
4-fold and Dumitru. A SAT upper bound must encode realizability (separate solver),
not added clauses — smallest unrealizable abstract order types have 9 points and
forbidding them needs O(n⁹) clauses. Claims `kph-h67-24`, `kph-32-no7gon-no-realizable-found`.
Anchor: `research/sources/krapivin-przybocki-heule - ... PointSAT HTML.full.md`.

## F3 — Koshelev–Koshka arXiv:2604.20120 (verified against HTML full text)

h(6,≥2)=17 and h(6,1)=18 (refines the ES(6)=17 boundary); explicit 17-point integer
set with no empty/1-interior hexagon = oracle checkpoint. **Linear subreduction**: fix
abscissae (x_i=i or exponential), feed the whole formula to SMT/Z3, orientation
determinants become linear-integer — the run's concrete realizability route for
ES(5)/ES(6) reproduction. Caveat (authors'): fixing x can in principle lose
realizations; empirical. Signotope 4-tuple one-sign-change axiom = 8 clauses per
4-set. Preprint, asserted-by-source. Claims `kk-linear-subreduction`, `kk-h61-h62`,
`kk-adjacent-not-esz7`. Anchor: `research/sources/koshelev-koshka-SAT-ASP-esz-linear-subreduction-arxiv2604.20120-html.full.md`.

## F4 — Baek–Balko decomposable stays asserted-by-source

`baek-balko-split` (ESsplit(k)=2^{k-2}+1) is proved-in-source (Lemma 10 upper bound
complete, Lemma 11 abstract lower bound complete; Lemma 9 & 12 "proof omitted").
`baek-balko-decomposable` (ES holds on decomposable sets, Theorem 8) is
**asserted-by-source** — the SoCG version says verbatim "The proof of Theorem 8 is
omitted", deferred to JCTA 2026. CONTEXT.md Established's "proved (SoCG 2025)" line
is **stale and must be corrected**; anything resting on decomposable-as-proved
rests on an unverified source claim. Recall check: durable memory agrees with the
claimed status. Anchor: `research/summaries/baek-balko-ES-conjecture-revisited-SoCG2025.pdf.md`.
