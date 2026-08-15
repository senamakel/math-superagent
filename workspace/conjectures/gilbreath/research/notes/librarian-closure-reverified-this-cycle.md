# Librarian closure — re-verified this cycle

**Role / source:** librarian, adversarial spot-check of the recorded closure.

The library was reported CLOSED (Directive 46; `librarian-closure-verified-2026.md`).
Rather than re-assert that from the note, this cycle verified it directly against
disk and the index.

## Checks performed (all on-disk, not recall)

1. **Canonical-reference tier present and searchable.** Confirmed in
   `research/sources/` and reachable via `search_documents`:
   - Odlyzko 1993 `odlyzko-1993-iterated-absolute-differences.full.md` +
     latex source (block lemma, exact constant)
   - Killgrove–Ralston 1959
   - Proth 1878 `proth-1878-ncm-vol4-googlebooks.full.md` (retraction recorded)
   - Chase 2024 (Math. Ann.), CHT 2026 (`chase-hunter-tao-2026-...FULLPDF`)
   - Granville 2026 `granville-2026-piercing-gilbreath-FULLPDF.full.md`
     (Lemma 5.4 / Theorem 5.5)
   - Banks–Ford–Tao 2023 (`maier-pomerance-2023-large-prime-gaps...`, filename is a
     misnomer, header records correct authors)
   - Chebyshev-bias / mod-4 pair sources: Ash–Beltis–Gross–Sinnott 2011,
     Rubinstein–Sarnak, Lemke Oliver–Soundararajan, Martin et al. 2024 survey
   - Encyclopedic tier: Wikipedia, MathWorld, Encyclopedia of Math, OEIS records
     (A000232, A036262, A080839, A089582, A347924)
   - Ducci primary sources: Glaser–Schöffl, Calkin–Stevens–Thomas, CZ 2011/2014,
     Caragiu–Zaharescu–Zaki, Chamberland
2. **Sole open REQUEST settled negative, with its note present.** The
   `g-supply-two-point-crux-settled.md` file exists on disk and carries the
   two-point argument (switch bit is a consecutive-pair statistic; GRH/Dirichlet
   one-point methods structurally blind; conditional Route B deliverable).
3. **Named MathOverflow fetch done.** `mathoverflow-...-thread.full.md` present.
4. **Frontier cited-by≥2 rows all held.** Matched against `research/sources/`
   (closure-verified-2026 note item 3 re-checked): Z-game, divisors/exponents
   game, Ducci-algebraic-numbers, Colonna record, Odlyzko itself, Killgrove–
   Ralston, Gatti, Torelli. Remaining are textbook/popularisation nodes.
5. **Notes on settlement and dead ends all present.** `g-supply-two-point-crux-settled`,
   `lemma54-descent-proof-repaired`, `step_law_proved`, `runcount-lemma-refuted`
   (via library-state), `no-deterministic-general-class-theorem`, `scholar-cycle-*`.

## Verdict

The closure holds on re-examination. NOTHING in the canonical tier, the frontier's
high-trust rows, or the settled REQUEST is missing. Per Directive 46, no
Gilbreath/Proth/Ducci re-fetch and no frontier re-sweep. A future librarian cycle
should act only if a NEW gap appears in `research/REQUESTS.md`.
