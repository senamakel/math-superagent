# Librarian cycle — state-of-the-art probe; only gap is the JCTA 2026 decomposable-set proof

<!-- source: deep_research + exa_search + citation_graph + download_document probes, this cycle -->

## What this cycle did

1. **Audited** the reference library against disk (not recall): every canonical
   source in `research/sources/` resolves to a real file; ROOT.md meets GOAL.md
   criterion 1 (structure of minimal counterexample, verification bound,
   restricted classes); the three REQUESTS rows are answered by held full texts
   (a derivation-render artifact, not a gap).

2. **Probed the current state of the art** (deep_research across 2024-09 onward)
   specifically for anything the held sources do NOT already cover. The state of
   the exact conjecture is unchanged through 2025-2026:
   - ES(n)=2^{n-2}+1 is still **open for n≥7**; ES(7)=33 unproven.
   - No new primary settles or improves the exact value.
   - The best upper bound remains Holmsen–Mojarrad–Pach–Tardos
     2^{n+O(√(n log n))} (held); asymptotic, not bearing on the exact constant.
   - No 2025–2026 paper closes a gap in the exact conjecture.

3. **Triaged the three genuinely new 2025–2026 leads** the probe surfaced, and
   rejected all three as acquisitions against the exact conjecture:
   - **Baek & Balko, JCTA 2026** (DOI 10.1016/j.jcta.2026.106195) — the *journal
     version* of the SoCG 2025 paper the library already holds in full. Same
     result set. **Not a new acquisition** — except for one pointed exception
     below.
   - **Furukawa 2025**, *Big convex polytopes or rich hyperplanes* (arXiv:2501.03645)
     — higher-dimensional analogue ES_d(l,n); adjacent problem, no reduction to
     the planar exact conjecture. Drift guard: rejected.
   - **Blake–Felsner–Hämäläinen–Witkowski 2025**, *ES for convex permutations and
     orthogonally convex point sets* — a *different* function N_o(n)
     (orthogonally convex subsets / convex subpermutations), NOT ES(n). Drift
     guard: rejected.

## The one live gap this cycle confirms

The held SoCG 2025 full text of Baek & Balko says **"The proof of Theorem 8 is
omitted"** for the decomposable-set theorem (the strongest restricted-class
result: the ES conjecture holds for all decomposable sets). The digest
(`baek-balko-ES-conjecture-revisited-SoCG2025.pdf.md`) marks claim
`baek-balko-decomposable` as **asserted-by-source**, pending the JCTA 2026
journal version which is supposed to carry the full proof.

Probe outcome this cycle:
- ScienceDirect JCTA 2026 version is **403-confirmed unobtainable** in open
  access (`download_document` failed: 403 Forbidden on the article PII).
- **No arXiv preprint** of the journal-complete version exists as of this cycle.
  Jineon Baek's arXiv papers are arXiv:2206.04260 (ETV, held) and arXiv:2411.19826
  (Gerver sofa, unrelated). Nothing new posted.
- author/conference portals (DROPS, BGU, researchr, Starfos) all carry only the
  SoCG 2025 short version, which is the one already held.

So the referenced upgrade (hold the full decomposable-set proof) is **recorded
as a new REQUESTS row** for a future run with subscription access or after the
authors post the journal version to arXiv. It is the only precisely-identified
acquisition that remains.

## NOTHING ELSE to acquire

Every other angle — canonical tier, surveys, every upper bound, lower-bound
realizability, exact values and computation, SAT/order-type/chirotope
foundations, restricted classes, adjacent problems, formalisation arm — is
covered by a held primary or faithful digest. The library remains phase-1
complete. Further acquisition resumes only against a stated gap, and the only
such gap at the end of this cycle is the JCTA 2026 decomposable-set proof above.
