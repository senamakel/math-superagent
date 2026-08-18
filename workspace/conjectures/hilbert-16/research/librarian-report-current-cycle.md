# Librarian cycle report — finiteness-theorem primary texts, DRR ledger re-confirmed

## What was added this pass (both primary, verified by first lines)

1. **Ilyashenko 1990, "Finiteness theorems for limit cycles"** (Russian Math.
   Surveys 45:2, 129-203; UMN 45:2, 143-200) — NEW full text.
   - File: `research/sources/ilyashenko-1990-finiteness-theorems-rms-primary.full.md`
     (3.4 MB PDF source → 163 KB Markdown, 3863 lines).
   - URL: `https://www.mathnet.ru/php/getFT.phtml?jrnid=rm&paperid=4718&what=fullteng&option_lang=eng`
     — **mathnet paperid `rm4718`** (found via a citation URL `mathnet.ru/rus/rm4718`,
     NOT guessed; a guessed `rm4668` fetched Rozanova's PDE paper instead and was
     neutralised — see the wrong-fetch record below).
   - Content (verified from first 40 lines): Theorems I-IV — (I) polynomial planar
     fields have finitely many limit cycles; (II) analytic fields on closed
     2-surfaces have finitely many; (III) a neighbourhood of a singular point free
     of limit cycles; (IV) elementary compound cycles have a limit-cycle-free
     neighbourhood. §1 expansion of monodromy transformations into terms with
     incommensurable rates of decrease; §2 functional cochains (simple and
     sectorial); §3 Phragmén–Lindelöf for cochains; §4 superaccurate asymptotic
     series. This is the **canonical survey of the Dulac finiteness theorem and
     its proof structure** — the Ilyashenko side of the Écalle-side frontier row
     (Écalle 1992 book), and the 19-citation frontier target
     `10.1070/rm1990v045n02abeh002335` now held.
   - Why it matters here: the finiteness theorem is the pointwise side of the
     H16.2 uniformity gap; its proof structure (cochains, Phragmén–Lindelöf,
     superaccurate series) is exactly where the run's `dulac-cochain-stokes-consistency`
     approach lives, and where Yeung 2024 claims a gap. Now the primary text is on
     disk for the scholar to check those claims against.

2. **Ilyashenko 2016, "Finiteness theorems for limit cycles: a digest of the
   revised proof"** (Izvestiya: Mathematics 80:1, 50-112, part 1 of 2) — full text
   now held.
   - Files: `research/sources/ilyashenko-2016-digest-revised-proof-fulltext.full.md`
     (763 KB PDF → 155 KB Markdown; digest at
     `research/summaries/ilyashenko-2016-digest-revised-proof-fulltext.md`).
   - URL: `https://www.mathnet.ru/php/getFT.phtml?jrnid=im&paperid=8352&what=fullteng&option_lang=eng`
     — paperid `im8352` (from the held abstract page's getFT link, not guessed).
   - Content (digest verified): Theorems 0.1-0.12 — finiteness for polynomial
     fields and analytic fields on closed surfaces; non-accumulation theorem for
     elementary polycycles; identity theorem (countably many fixed points ⇒
     monodromy is identity); asymptotics theorem; almost-regular germs extend to
     quadratic domains; Phragmén–Lindelöf for almost-regular germs; sectorial
     normalization; correspondence maps TO/FROM a centre manifold of a degenerate
     elementary point; monodromy as a finite composition of almost-regular maps
     and TO/FROM maps. This is Ilyashenko's **revised-proof digest**, directly
     relevant to the `dulac-cochain-stokes-consistency` thread and to checking
     Yeung's claimed gap.
   - Part 2 (the series' second paper) was NOT fetched: its mathnet paperid is
     not derivable by guessing (im8353 is a 404) and no citation URL for it is
     held. Recorded as a gap, not guessed again.

## Wrong-fetch record (kept as a lesson, neutralised as a source)

`research/sources/ilyashenko-1990-finiteness-theorems-rms-fulltext.full.md` was
created by a **guessed** mathnet paperid (`rm4668`) and contains **O. S.
Rozanova's PDE paper** (Communications of the Moscow Mathematical Society), not
Ilyashenko. It has been overwritten with a WRONG-FETCH header pointing to the
correct file, and the incident is recorded at
`research/findings/wrong-fetch-rozanova-mislabeled-ilyashenko-1990.md`. Lesson:
**never guess a mathnet paperid**; get it from a citation URL that carries
`mathnet.ru/rus/rmNNNN`, then verify the first lines of the landing text against
the expected title.

## DRR ledger — re-confirmed, not changed

No new closure of any open DRR graphic appeared in this pass's searches (bounded
to 2026): the held picture stands — ≥89/121 fully closed by 2015 (88 RSZ +
(I^1_14) RR), (I^1_6b),(H^3_13),(DI_2b) boundary-sets-only, (H^3_14) open with
Lu arXiv:2607.13785 (v2, 17 Jul 2026, unrefereed) the sole claim, 11 degenerate
graphics open per Shan 2013. The two open requests
(`complete-current-ledger-cb3d`, `dumortier-roussarie-rousseau-9c4f`) remain
unfillable from a single public source — no consolidated post-2020 ledger exists
and DRR 1994's raw catalogue is paywalled. Re-confirmed via the Fishkin search
that the field has moved on (Marín–Villadelprat hemicycles; the 2024-2026
surveys) without closing the DRR rows.

## Fishkin — constants still unverified

The AMS PDF for Fishkin 2010 (Trans. Moscow Math. Soc. 71,
DOI 10.1090/s0077-1554-2010-00181-1) was rate-limited three times (HTTP 429).
The search-result abstract quotes the constants (σ = exp(-10^73 κ - 2δ - 33),
bound exp(exp(10^72 κ - 2δ - 33))) but that is still recall-level; the claim
`fishkin-perturbed-center-quadratic-bound` remains abstract-level only. The
thread `restricted-h2-bounds` stays open; the next attempt should use the
mathnet mirror of the Russian original (Trudy Moskov. Mat. Obshch. 71, 2010)
rather than ams.org.

## Requests ledger — status

- `complete-current-ledger-cb3d` / `dumortier-rousseau-rousseau-9c4f` (DRR
  ledger): still open; unfillable from one source, triangulated instead.
- Gasull–Santana structural-status comparison: answered by held claims
  (`h16-gasull-santana-2024-structural-status`); no new fetch needed.
- Best special-family Abelian-integral bound: answered by held sources
  (BD linear-in-m, BNY double-exponential, FTV2013 Chebyshev ECT, Gavrilov 2001);
  no new fetch needed.

## Memory

`remember_memory` was attempted for both new holdings; the Cognee service
failed (health check timeout) on every call this pass, so the durable record of
this cycle is this report + the source files themselves. When memory recovers,
store: (a) Ilyashenko 1990 RMS 45:2 full text held at
`research/sources/ilyashenko-1990-finiteness-theorems-rms-primary.full.md`
(mathnet rm4718); (b) Ilyashenko 2016 digest part 1 full text held at
`research/sources/ilyashenko-2016-digest-revised-proof-fulltext.full.md`
(mathnet im8352); (c) the mathnet paperid lesson.
