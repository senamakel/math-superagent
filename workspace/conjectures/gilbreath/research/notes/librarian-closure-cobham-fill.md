# Librarian closure — re-verified this cycle (with a real fill)

**Role / source:** librarian, adversarial spot-check of the recorded closure, and
one genuine fill.

## What was checked (all on-disk, not recall)

The canonical tier, frontier cited-by≥2 rows, the settled REQUEST, and the named
fetch were re-verified against `research/sources/` (as in
`librarian-closure-reverified-this-cycle.md`). The closure held there: Odlyzko
1993, Killgrove–Ralston 1959, Proth 1878 (retraction), Chase 2024 / CHT 2026,
Granville 2026 (Lemma 5.4 / Thm 5.5), Banks–Ford–Tao 2023, the Chebyshev-bias /
mod-4 pair corpus, the encyclopedic/OEIS tier, and the Ducci primary sources are
all present and digested.

## The genuine gap found and filled this cycle: Cobham's theorem

While re-verifying the two *adopted* approaches
`christol-cobham-fold-inverse-automaticity` and `dyadic-linear-complexity-supply`
(which rest the automatic-subclass lemma of the live `dyadic-periodicity-collapse`
thread on Christol's **and** Cobham's theorems), a `search_documents` /
`search_claims` / memory sweep returned **nothing for Cobham**. Christol was
grounded (Kedlaya 2008; Adamczewski–Bostan–Caruso 2023); Cobham was not — the run
was citing it from recall. This is exactly the failure the librarian exists to
prevent.

**Filled.** Downloaded and digested Krebs, "A more reasonable proof of Cobham's
theorem", arXiv:1801.06704 (a short proof paper, so a clean canonical statement
and proof chain; original Cobham 1969 = Math. Systems Theory 3:186–192):

- Full text: `research/sources/cobham-theorem-krebs-proof-statement.full.md`
- Summary: `research/summaries/cobham-theorem-krebs-proof-statement.md`
- Claim: `research/notes/cobham-theorem-grounded.md` → `cobham-theorem-grounded`
  (status: sourced-statement)

**Theorem (verbatim):** if a sequence is both a-automatic and b-automatic for
multiplicatively independent a,b ≥ 2, then it is ultimately periodic;
equivalently a set is both a-recognizable and b-recognizable iff ultimately
periodic.

**Scope discipline carried forward (matches what the approach already records):**
Cobham alone does NOT force rigidity on a single-base 2-automatic string —
Thue–Morse (2-automatic, aperiodic) and period-3 (2-automatic, non-rigid, ν₂ ~
0.647n) are the two witnesses — so the dyadic dichotomy rests on the σ = I+S
spectral structure, not on Cobham. This fill does **not** close G-supply.

## Second check: 2-adic complexity

The approaches' "2-adic complexity / 2-adic rigidity" is the run's **own** σ =
I+S spectral invariant (the subset-zeta density), NOT the cryptographic
FCSR/2-adic-span notion of Klapper–Goresky. No gap: the term is this run's
defined quantity, not an external theorem the run was leaning on unread.

## Verdict

The library was closed except for one genuine, named, load-bearing gap, which is
now filled and recorded. Nothing further to fetch this cycle. Per Directive 46,
no Gilbreath/Proth/Ducci re-fetch and no frontier re-sweep; a future librarian
cycle should act only if a NEW gap appears in `research/REQUESTS.md`.
