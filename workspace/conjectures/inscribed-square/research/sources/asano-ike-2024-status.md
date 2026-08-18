# Asano–Ike 2024 — current status check (as of this run, ~August 2026)

**Paper:** Tomohiro Asano, Yuichi Ike, "The rectifiable rectangular peg problem," arXiv:2412.21057 [math.SG], first posted 2024-12-30.
**URL:** https://arxiv.org/abs/2412.21057 · https://doi.org/10.48550/arxiv.2412.21057

## Bottom line

- **Status: arXiv preprint only — NOT published, NOT peer-reviewed, NOT retracted.**
- **Revised: yes — currently at v3** (5 Jan 2026). v2 fixed "an error in Section 5"; v3 is a general revision ("v3: Revised").
- **Not superseded:** it remains the strongest known positive result for the square peg problem (every rectifiable Jordan curve inscribes a θ-rectangle for all θ ∈ (0,π), hence a square at θ = π/2).
- **No counterexample to the Toeplitz conjecture is claimed anywhere in the sources checked; the conjecture remains open** for general (non-rectifiable) continuous Jordan curves.

## Evidence, source by source

### 1. arXiv listing (authoritative for version history) — checked live
- arXiv API record for id 2412.21057 (`http://export.arxiv.org/api/query?id_list=2412.21057`): title, abstract, and:
  - `2024-12-30T16:18:37Z` first submission
  - **v3** current, dated **2026-01-05T11:13:26Z**
  - comment field: *"30 pages, v3: Revised. v2: An error in Section 5 fixed. Many typos fixed"*
- The downloaded full text itself is dated "January 6, 2026" and carries "arXiv:2412.21057v3 [math.SG] 5 Jan 2026" on page 1, confirming the workspace copy is the current v3.
- What Section 5 is: "Jordan curves" — 5.1 proof of the main theorem, 5.2 rectifiable curves (Corollary 5.9), 5.3 locally monotone curves (Corollary 5.12). The v2 error fix is therefore inside the proof that rectifiable curves satisfy Theorem 1.1's hypotheses.

### 2. OpenAlex record — checked live
- API record `https://openalex.org/W4405957718` (DOI 10.48550/arxiv.2412.21057):
  - `"type":"preprint"`, `"is_published":false`, `"is_accepted":false`, `"is_retracted":false`
  - sole `primary_location` is the arXiv repository; no journal source, no volume/issue/pages
  - `"cited_by_count":0` (OpenAlex counts zero citations as of the record's last update, 2026-08-06)
  - funding: JSPS CREST and KAKENHI (21K13801), JST CREST JPMJCR24Q1

### 3. Google Scholar — reached, no record
- `https://scholar.google.com/scholar?q=%22The+rectifiable+rectangular+peg+problem%22` returned (in Arabic localization) *"your search — 'The rectifiable rectangular peg problem' — did not match any article"*.
- Interpretation: no journal-published version is indexed under this title in Scholar (Scholar indexes arXiv preprints under their title, so the absence of even an arXiv hit is a Scholar indexing quirk, but it is certainly not evidence of a journal version). No journal DOI or citation record was found.

### 4. Citation graph — no one has built on it yet
- `citation_graph` on 2412.21057: OpenAlex holds **0 citing works** (and an incomplete reference list). Nobody has published a follow-up that cites it, so there is no published confirmation, correction, or supersession by citation.
- The most closely related newer work (Greene–Lobb 2026, arXiv:2604.17116, "Jordan curves inscribe a positive measure of rectangles"; Barber 2026, arXiv:2604.27717, isosceles trapezoids) cites Asano–Ike's theorem as background ("every rectifiable or locally monotone curve inscribes every rectangle") but neither cites it in a way that validates or refutes it — both are themselves 2026 preprints, and both address rectangle/trapezoid problems, not the full square conjecture.

## 2025–2026 developments on the full Toeplitz conjecture

### The continuous Legendrian lift question (Asano–Ike Theorem 1.1's hypothesis) — still open
- Theorem 1.1 (verbatim from v3, §1.1): Let c : S¹ → R² be a Jordan curve such that there is a sequence of smooth Jordan curves cₙ → c in C⁰ with the primitives fₙ of (cₙ∘e)∗λ converging uniformly on compact subsets to a continuous f. Then c inscribes a θ-rectangle for any θ ∈ (0,π). *"A Jordan curve satisfying the conditions in Theorem 1.1 might be said to admit a continuous Legendrian lift."*
- The paper proves rectifiable curves (Cor 5.9) and locally monotone curves (Cor 5.12) admit such a lift.
- **No source found (arXiv, journal, or preprint) proves or disproves that every Jordan curve admits a continuous Legendrian lift.** This remains the sharp open question separating the solved class (rectifiable) from the general case. The 2025 arXiv listing for "square peg" contains no paper on this; the only nearby item is Asano–Ike–Kuo–Li, "C⁰-rigidity of Legendrians and coisotropics via sheaf quantization" (arXiv:2510.01746, Oct 2025), which is about C⁰-rigidity of Legendrians under contact homeomorphisms, not about existence of lifts of Jordan curves — it does not settle the question.

### New proof attempts of the full conjecture since Asano–Ike — one series found, self-published, unvalidated
- **Yoshiki Ueoka, Zenodo preprint series (2025–2026), claiming a degree-theoretic proof for all C⁰ Jordan curves:**
  - "A Complete Proof of the C⁰ Toeplitz Conjecture: An Approach via the Concept of Permanence and Degree Theory" — https://doi.org/10.5281/zenodo.17554802 (2025-11-08)
  - "A Fully Rigorous Degree-Theoretic Proof of the Square Peg Problem for C⁰ Jordan Curves" — https://doi.org/10.5281/zenodo.17655388 (2025-11-20)
  - "The Proof of the Inscribed Square Problem using Topological Degree" — https://doi.org/10.5281/zenodo.17847990 (2025-12-08)
  - "On the existence of squares inscribed in arbitrary C⁰ Jordan closed curves in the plane" — https://doi.org/10.5281/zenodo.18243635 (dated 2025-01-14 in metadata)
  - Plus a Medium article by the same author (2026-01-14) advertising the claim.
- **Status: NOT peer-reviewed, NOT published in any journal, NOT cited (0 citations), no independent validation or published critique found.** The author is an independent researcher. Multiple overlapping preprints with slightly different titles and "priority claims"/"proof skeleton" language, plus the explicit admission in one that "local formalization can be added along the reference chain," are hallmarks of an unvetted claim. **Do not treat as established.** The central claim — that the standard degree argument can be pushed from C¹ to C⁰ with a uniform positive boundary margin — is precisely the step every serious treatment (Matschke 2014 survey; Tao 2017; problem.md §"Where the general case breaks") identifies as the unsolved core, and no expert has endorsed Ueoka's resolution of it. This run's GOAL.md explicitly requires treating any such claim as unproven until peer-reviewed and widely accepted.

### Other 2025–2026 items on arXiv (from the live API query `all:"square peg"`, sorted by date)
- Chambers, "On the square peg problem," Discrete Comput. Geom. 73 (2025) 1144–1153, DOI 10.1007/s00454-025-00720-x — already in library. Stability: curves C⁰-close to a C² curve inscribe a square of positive side length. Does not cover general continuous curves.
- Naseri Sadr, "A Table Theorem for Surfaces with Odd Euler Characteristic" (arXiv:2412.01977v2, Mar 2025) — uses the smooth square-peg result to prove table-type theorems; not a new square-peg proof.
- Hugelmeyer, "A Solution to the Periodic Square Peg Problem" (arXiv:2407.20412) — periodic variant, 2024, in library.
- Greene–Lobb 2024 works (2404.05179, 2407.07798), Tao 2017, Rifford 2021, Matschke 2009/2022, CDM — all pre-2025 or already in library.
- **No arXiv paper from 2025–2026 claims a full proof of the conjecture** (the only full-proof claim found is Ueoka's Zenodo series).

## Counterexample claims — none found

- No source checked (Matschke's survey and its 2014/2022 extensions, Tao 2017, Greene–Lobb, Asano–Ike, Wikipedia's current entry, MathOverflow threads, the 2025–2026 arXiv listing, the deep-research synthesis) claims or establishes a Jordan curve with no inscribed square.
- The only "counterexample" language in the literature is about **weaker/related statements**: Matschke's Figure 2 (a Jordan curve with no inscribed square lying entirely *inside* — the square need not be inside), and Matschke's *topological counterexample for a regular octahedron on metric 2-spheres* (a different problem). Neither is a counterexample to Toeplitz's conjecture.
- Wikipedia (checked 2026-02-02 revision): "No general counterexample is known; the problem remains open in full generality."

## What could not be checked (network limits)

- **MathSciNet / zbMATH** (subscription) were not reachable through the available tools — no independent confirmation of whether a journal submission is in progress. This is a genuine residual gap: an accepted-but-not-yet-indexed journal version, or a submission under review, would not appear in arXiv/OpenAlex/Scholar. All three checked sources agree the paper is a preprint as of the check.
- **The actual content of Ueoka's proofs** was not read in full (only abstracts and search summaries). A claim of a complete proof of a 115-year-old conjecture made on a non-peer-reviewed platform should be treated as unverified until an expert reads it; recording the claim's existence is not endorsing it.
- Scholar returned only an Arabic-localized empty result — the page loaded, but gave no citation counts.

## Recommendations for the library

- The claim `asano-ike-2024-rectifiable-square` should be updated: status remains "asserted-by-source (arXiv preprint)", now at **v3 (5 Jan 2026)** with the Section-5 error fixed in v2; still no journal version as of ~Aug 2026.
- The claim `asano-ike-2024-legendrian-lift-gap` stands: the continuous Legendrian lift question is open; Ueoka's Zenodo claim does not address it (it is a different method) and is unvalidated.
- Add a new note flagging the Ueoka Zenodo series as an unvalidated full-proof claim that the run should NOT treat as established, with the URLs above.

## Key URLs

- arXiv abs: https://arxiv.org/abs/2412.21057
- arXiv API record (version history): http://export.arxiv.org/api/query?id_list=2412.21057
- DOI: https://doi.org/10.48550/arxiv.2412.21057
- OpenAlex: https://openalex.org/W4405957718
- Google Scholar search (no record): https://scholar.google.com/scholar?q=%22The+rectifiable+rectangular+peg+problem%22
- Ueoka Zenodo preprints: https://doi.org/10.5281/zenodo.17554802 · https://doi.org/10.5281/zenodo.17655388 · https://doi.org/10.5281/zenodo.17847990 · https://doi.org/10.5281/zenodo.18243635
- Asano–Ike–Kuo–Li 2025 (C⁰-rigidity of Legendrians; related but does not settle the lift question): https://arxiv.org/abs/2510.01746
- Greene–Lobb 2026 (positive measure of rectangles; cites AI as background): https://doi.org/10.48550/arxiv.2604.17116
- Barber 2026 (isosceles trapezoids; cites AI as background): https://doi.org/10.48550/arxiv.2604.27717
