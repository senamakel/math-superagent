# DELETED — wrong arXiv download (librarian, this pass)

This file records a wrong download so nobody repeats it.

- **Intended:** Beni Yoshida, *Information storage capacity of discrete spin systems*,
  Annals of Physics 338 (2013) 134–166; arXiv preprint.
- **What I fetched by guess:** `research/sources/yoshida_information_storage_fractal_codes.full.md`
  from `https://arxiv.org/pdf/1304.6104` (and the auto-generated digest at
  `research/summaries/yoshida_information_storage_fractal_codes.md`).
- **What it actually is:** arXiv:1304.6104 is Kevin Heng, *Why Does Nature Form Exoplanets Easily?*
  — an exoplanets article, unrelated to this problem.

**Lesson (matches the Project Euler failure mode the instructions warn about):** I inferred the
arXiv number from the submission date, but the correct ID had the same *December* date in a
different year's series. Guessing an arXiv ID stores the wrong paper silently. The fix is the
arXiv API title query, which returns the authoritative ID: **arXiv:1111.3275** (v3, dated
2012-12-24), API-confirmed via `export.arxiv.org/api/query` on 2026-08-16. The correct
download is at `https://arxiv.org/pdf/1111.3275`.

The wrong `1304.6104` full-text and digest were deleted. The correct download is filed next to
this note as `yoshida_information_storage_fractal_codes.full.md` / `.md` (overwritten).
