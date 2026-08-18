# Asano–Ike 2024 — status check (v3, still a preprint) — scholar verdict

**Source:** Tomohiro Asano, Yuichi Ike, "The rectifiable rectangular peg
problem," arXiv:2412.21057 [math.SG]. Status check performed live ~Aug 2026
([[research/sources/asano-ike-2024-status.md]]; full text v3 at
[[research/sources/asano-ike-2024-rectifiable-rectangular-peg.full.md]]).

**Bottom line: the paper is an arXiv preprint, currently v3 (5 Jan 2026), NOT
peer-reviewed, NOT published, NOT retracted, NOT superseded.** v2 fixed "an
error in Section 5" (the rectifiable-case proof); v3 is a general revision. The
workspace's full text is the current v3 (page 1 dated 5 Jan 2026). OpenAlex:
type preprint, is_published false, is_retracted false, 0 citations. Scholar:
no journal record. **Consequence for the run: `asano-ike-2024-rectifiable-
square` and its family stay `asserted-by-source`, not `proved`; a
retraction/correction would falsify them.** This is already reflected in the
ledger's statuses — no change needed, but the version number is now pinned (v3)
and the Section-5 error history is known.

**What it establishes beyond the paper itself (this check's own findings):**

1. **The continuous Legendrian lift question is still open.** No source found
   proves or disproves that every Jordan curve admits one. Asano–Ike–Kuo–Li
   2025 (arXiv:2510.01746) is about C⁰-rigidity of Legendrians/coisotropics
   under contact homeomorphisms — related machinery, does not settle existence
   of lifts of Jordan curves. The frontier (thesis `legendrian-lift-frontier`,
   ladder R4) stands.

2. **The only full-proof claim found in 2025–26 is unvalidated:** Yoshiki
   Ueoka's Zenodo preprint series (5 items, 2025-11 through 2026-01, DOIs
   10.5281/zenodo.17554802 …18243635) claiming a degree-theoretic proof for all
   C⁰ Jordan curves. Not peer-reviewed, 0 citations, no expert endorsement,
   overlapping titles/"priority" language, one admits "local formalization can
   be added along the reference chain." **Do not treat as established.** The
   claim — pushing the degree argument from C¹ to C⁰ with a uniform positive
   boundary margin — is exactly the step every serious treatment (Matschke 2014,
   Tao 2017, problem.md §"Where the general case breaks") identifies as the
   unsolved core.

3. **No counterexample claims exist anywhere checked** (arXiv, OpenAlex,
   Scholar, Wikipedia 2026-02-02 revision: "No general counterexample is
   known; the problem remains open in full generality"). Matschke's "no square
   inside" example and the octahedron topological counterexample are weaker/
   different statements, not counterexamples to Toeplitz.

4. **Residual gap (honest):** MathSciNet/zbMATH were unreachable; an
   accepted-but-not-yet-indexed journal version, or a submission under review,
   would not show in arXiv/OpenAlex/Scholar. The check is as strong as those
   three sources allow, not stronger.

```claim
id: asano-ike-2024-v3-preprint-status
statement: Asano–Ike 2024 (arXiv:2412.21057) is, as of Aug 2026, an unreviewed arXiv preprint at v3 (5 Jan 2026; v2 fixed an error in Section 5); OpenAlex records type=preprint, is_published=false, is_retracted=false, 0 citations; no journal version is indexed. All in-library claims resting on it are asserted-by-source.
status: checked (live status check against arXiv API, OpenAlex, Scholar, citation graph)
evidence: arXiv API id_list=2412.21057; OpenAlex W4405957718; Scholar search; research/sources/asano-ike-2024-status.md
holds-here: yes — pins the evidence status of asano-ike-2024-rectifiable-square and the whole family
falsifies: discovery of a peer-reviewed version, or a retraction
anchor: research/sources/asano-ike-2024-status.md
```

```claim
id: ueoka-2025-full-proof-unvalidated
statement: Yoshiki Ueoka's Zenodo series (2025–26, five preprints) claims a degree-theoretic proof of the square peg problem for all C⁰ Jordan curves; it is not peer-reviewed, not cited, has no expert endorsement, and its central step (degree argument from C¹ to C⁰ with uniform positive boundary margin) is exactly the step the literature identifies as unsolved. It must not be treated as established.
status: catalogued (existence recorded; content not read in full)
evidence: Zenodo DOIs 10.5281/zenodo.17554802, .17655388, .17847990, .18243635; asano-ike-2024-status.md
holds-here: yes — prevents the run from treating an unvalidated full-proof claim as a resolution
falsifies: expert verification or peer-reviewed publication of the proof; a published critique confirming its correctness
anchor: research/sources/asano-ike-2024-status.md
```
