# Source-library repair: the entropy frontier is now primary-sourced

The six papers the run's "current best constant" claim rests on were held only
as ~6KB arXiv **abstract-page stubs** (title + abstract + ArXiv chrome), not
paper bodies. This was the failure flagged in the previous-attempt lesson
("saved `.full.md` files are only arXiv abstract pages"). This pass re-fetched
each from the full-text `/html/` and `/pdf/` URLs its own abstract page links,
exactly as the lesson instructed.

## What was upgraded (stub → full body)

| Source | Where the body lives NOW | What it now establishes |
| --- | --- | --- |
| Gilmer, arXiv:2211.09055 | `gilmer-...-2022.full.md` (33.9KB) + `gilmer-...-2022.pdf.full.md` (21.1KB) | The original 0.01 constant bound: Theorem 1 (`H(A∪B) ≥ 1.26·H(A)` under `Pr[i∈A] ≤ 0.01`), Theorem 2 (0.01 constant for UC). Examples 1–2 give the product-Bernoulli crossover `H(A∪B)/H(A) = H(2p−p²)/H(p)`, < 1 for p < (3−√5)/2, = 1 at p=(3−√5)/2. |
| Alweiss–Huang–Sellke, arXiv:2211.11731 | `alweiss-...-2022.full.md` (37.8KB) + `alweiss-...-2022.html.full.md` (36.6KB) | The `(3−√5)/2` bound, explicitly "a natural barrier for the method of Gilmer"; minimizer reduces to two point masses; `φH(x²) ≥ xH(x)` tight at x ∈ {φ,1}; φ* = φ (Claims 3–4). |
| Chase–Lovett, arXiv:2211.11689 | **only** `chase-...-2022.html.full.md` (12.6KB); base `.full.md` is still the abstract stub | Verifies Gilmer's `(3−√5)/2` conjecture; extends to `(1−o(1))`-approximate union-closed with `ψ − o(1)`, ψ=(3−√5)/2; **ψ is optimal** for the approximate relaxation (Example 1.4). |
| Pebody, arXiv:2211.13139 | **only** `pebody-...-2022.html.full.md` (19.1KB); base `.full.md` is still the abstract stub | Independent `(3−√5)/2` bound (Theorems 1–2); Lemma 3/4 gives the discrete form `Σ p_i p_j H(w_i w_j) ≥ H(β²)/H(β) Σ p_i H(w_i)`. |
| Boppana, arXiv:2301.09664 | **only** `boppana-...-2023.html.full.md` (7.4KB); base `.full.md` is still the abstract stub | Simple calculus proof of `h(x²) ≥ φ·x·h(x)` (golden ratio φ=(√5+1)/2); the inequality AHS/CL/Pebody/Sawin all rely on. |
| Cambie, arXiv:2212.12500 | `cambie-...-2022.full.md` (66.0KB) + `cambie-...-2022.pdf.full.md` (44.7KB) | Solves Sawin's Question 2 exactly; dependent-samples improvement over (3−√5)/2 to c ≈ 0.3823455 (Theorem 3); critical distributions reduce to support ≤ 3. |

## IMPORTANT: which files are real bodies

- **Chase–Lovett, Pebody, Boppana**: their base `*.full.md` files are STILL the
  arXiv **abstract pages** (233/232/234 lines of arXiv chrome). The real bodies
  exist ONLY in the `.html.full.md` variants. Any claim citing these must point
  to the `.html.full.md`, not the base stub.
- **Gilmer, AHS, Cambie**: both the base `.full.md` and the new `.html`/`.pdf`
  variants are real bodies (duplicate formats of the same paper).
- **Yu, Liu, Sawin**: real bodies (all variants).

## Already genuine (checked, not touched)

- Yu (arXiv:2212.00658): `yu-...-2023.full.md` + `.html.full.md` — real body; ≈0.38234 record.
- Liu (arXiv:2306.08824): `liu-...-2023.full.md` + `.html.full.md` — real body; ≈0.38271 improvement.
- Sawin (arXiv:2211.11504): `sawin-...-2022.html.full.md` (41KB) + base — real body.

## Value of this repair

`research/ROOT.md` and the ledger's record claims cite these six papers as
sources. Before this pass, opening the cited `.full.md` would show only an
abstract — the "record" was sourced but the bibliography was not reproducible.
Now the specific statements confirm:
- `(3−√5)/2` is the **iid-entropy barrier**, not the record (AHS: "natural
  barrier for the method of Gilmer"); Chase–Lovett prove it is OPTIMAL for the
  approximate-iid relaxation; dependent couplings (Sawin/Cambie/Yu/Liu) escape it.
- The golden-ratio inequality `h(x²) ≥ φ x h(x)` is the one-variable spine of the
  barrier, with Boppana's simple proof.
- Yu ≈ 0.38234 stands as the strongest peer-reviewed record (Entropy 2023).

Summaries for all six upgraded bodies: `research/summaries/*.{pdf,html}.md`.
All bodies are indexed (search_documents reaches them).
