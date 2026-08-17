# Librarian acquisition report — this cycle: Horton 1983 closed; ETV-1996 / Károlyi–Solymosi-2005 registered

## Newly acquired (full primary text)

| Source | File | URL | What it establishes |
|---|---|---|---|
| **Horton 1983**, "Sets with No Empty Convex 7-Gons", Canad. Math. Bull. 26(4) (1983) 482–484 | `sources/horton-1983-sets-with-no-empty-convex-7-gons.pdf.full.md` (+ auto digest) | https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0E7C17D71D9FA4A08B265441FBEB32D7/S0008439500065176a.pdf/sets-with-no-empty-convex-7-gons.pdf | The primary statement and construction of the empty-hexagon-adjacent failure: for every k, a 2^k-point set S_k = {(i, d(i)) : 0 ≤ i < 2^k} with the binary-functional d(i) = Σ a_j c^{j-1}, c = 2^k+1, whose every empty convex polygon has ≤ 6 vertices — so g(n) (least N forcing an *empty* convex n-gon) does not exist for all n ≥ 7. This is the empty-side analogue of the ES construction and the reason empty-7-gons and beyond drop out of the ES story. Cited by 4 held sources (Morris–Soltan, Tóth–Valtr, Károlyi–Tóth, Wikipedia/Rosta); previously absent. Claims `horton-no-empty-7gon`, `horton-s-k-construction` (below). Also adds citation-lead rows (Valtr, Nešetřil–Valtr, Caro's generalized-ES bound) to FRONTIER. |

## Closed / registered this cycle

- **Empty-7-gon primary now held** (frontier row, cited twice). Previously only secondary restatements (Morris–Soltan's analytic rendition and Valtr's recursive "Horton set"); the original 1983 note is now in the library with the concrete binary-functional construction.
- **Requests-ledger state**: requests `balko-valtr-attack-baa4`, `open-access-full-1e6e`, `full-text-faithful-b96b` each carry `answers:` claim blocks in the held summaries (`balko-valtr-A-SAT-attack-on-ES-ENDM2015.md`, `erdos-szekeres-1961-construction-concrete.md`) but still render open in `derived/REQUESTS.md` — a re-derivation-state issue, not a library gap. The primary content backing each is physically in `research/sources/`.

## Documented-but-not-held (record; alternate or none held)

- **Erdős–Tuza–Valtr 1996, "Ramsey-remainder", European J. Combin. 17(6):519–532 (DOI 10.1006/eujc.1996.0045).** The canonical primary for the ETV enumeration conjecture (N(n,a,b) = Σ C(n-2,i)) the run treats as "the ETV reformulation." Not held: only Baek's arXiv treatment (`ETV-on-the-Erdos-Tuza-Valtr-Conjecture.full.md`, arXiv:2206.04260) states it, attributing the equivalence Thm 1.5 to [5] = this paper. Elsevier/paywalled; no open copy located this cycle. **Not a live block** — the run's ETV arm reads Baek (held, full proof of P(n,4,n)). Flag only if a precise statement of the 1996 enumeration form is needed beyond Baek's restatement.
- **Károlyi–Solymosi 2005, "Erdős–Szekeres theorem with forbidden order types", JCTA 113:455–465 (DOI 10.1016/j.jcta.2005.04.006).** The ancestor of the held Károlyi–Tóth 2012 restricted-class result (F_T(n) machinery). ScienceDirect 403 (confirmed again this cycle). Its non-explicit F_T(n) > 2^{n−2} and the explicit examples 𝒫 (pentagon+center) are restated in the held 2012 paper — not a live gap, but the 2005 paper itself is not in the library.

## Files on disk (all under research/)

- `research/sources/horton-1983-sets-with-no-empty-convex-7-gons.pdf.full.md` (full text, URL in leading comment)
- `research/sources/horton-1983-sets-with-no-empty-convex-7-gons.full.md` (Cambridge landing-page HTML — metadata only, keep as pointer)
- auto digests under `research/summaries/` (scholar to replace with ≤1000-token summaries)

## Claim blocks (for CLAIMS.md)

```claim
id: horton-no-empty-7gon
statement: For every k there is a 2^k-point general-position set with no empty convex 7-gon; hence g(n) — the least N such that every N points contain an empty convex n-gon — does not exist for any n ≥ 7. (g(3)=3, g(4)=5, g(5)=10 by Harborth; g(6) open.)
hypotheses: planar point sets in general position; empty n-gon = convex n-gon with no other point of the set inside.
holds-here: true and primary; this is the empty-side analogue of the ES lower-bound construction and the reason the run must keep "empty-hexagon/empty-7-gon" strictly separate from the convex-position ES(n) conjecture.
status: proved (primary, Horton 1983, full text in library).
bearing: adjacent-problem guard. The ES(n) conjecture is about convex-position (not empty) n-gons; its lower bound construction (1961) is a different object from Horton's 1983 construction. Do not conflate.
anchor: research/sources/horton-1983-sets-with-no-empty-convex-7-gons.pdf.full.md
```

```claim
id: horton-s-k-construction
statement: The Horton construction is S_k = {(i, d(i)) : i = 0,…,2^k−1}, d(i) = Σ_{j=1}^k a_j c^{j−1} with c = 2^k+1 and (a_1…a_k) the fixed-width binary expansion of i. Its trefoil symmetries (L/R/B/T scaled translates; 180° rotation T↔B; all B below / all T above any join of the other half) force any empty convex polygon to meet each half in ≤ 3 points, hence have ≤ 6 vertices.
hypotheses: as above; c large enough that (g) holds.
holds-here: true, this is the concrete dual object to the ES 1961 construction; both are recursive/self-similar "no large convex/empty" witnesses built from a functional sequence.
status: proved (primary, Horton 1983).
bearing: gives an exact-arithmetic testable sequence (binary functional) the run can realize and verify emptiness-of-7-gon with its oracle, mirroring how it verifies the ES construction's convex-n-gon emptiness.
anchor: research/sources/horton-1983-sets-with-no-empty-convex-7-gons.pdf.full.md
```

## Scholar handoff

Auto digests for the two Horton files should be replaced by scholar summaries under 1000 tokens. The claim blocks above carry the essential statements already.
