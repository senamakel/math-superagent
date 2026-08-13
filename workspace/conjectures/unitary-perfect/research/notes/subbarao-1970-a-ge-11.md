# Subbarao (1970) already proved a ≥ 11 — the run's a ≥ 8 is weaker and the a = 8 thread is closed

## What is established

**Claim.** Any unitary perfect number other than the five known ones satisfies
`a ≥ 11`, where `2^a || n` — i.e. `2^11 = 2048` divides any sixth example.

**Evidence class: sourced** (three primary texts in this library, all
attributing the result to Subbarao 1970, AMM 77 (1970) 389–390):

1. **Wall 1975 §2** (`research/sources/wall-1975-fifth-unitary-perfect-number-pdf.full.md`):
   verbatim, "Subbarao [1] has reported the impossibility of having A be 0, 3, 4,
   5, 7, 8, 9 or 10, and that if A = 1, then N = 6 or 90; if A = 2, then N = 60;
   if A = 6, then N = 87360. Thus we may restrict our attention here to A ≥ 11."
   Reference [1] of that paper is Subbarao, "Are There an Infinity of Unitary
   Perfect Numbers?", Amer. Math. Monthly 77 (1970) 389–90.

2. **Wall 1987 §2** (`research/sources/wall-1987-largest-odd-component.full.md`):
   verbatim, "Another lower bound, useful in many cases, is Subbarao's result
   [1] that a > 10 except for the first four unitary perfect numbers" and later
   "In light of Subbarao's results [1], we may assume that a > 10 from now on."
   Reference [1] again Subbarao 1970 AMM.

3. **Wall 1988** (`research/sources/wall-1988-nine-odd-components.full.md`,
   Introduction): "Subbarao and his co-workers [1] have shown that any new
   unitary perfect number N = 2^a m must have a > 10 and b > 6."

The 1966 paper (`research/sources/subbarao-warren-1966-cambridge-pdf.full.md`,
Theorem 2) already eliminated a = 3, 4, 5, 7 and classified a = 1, 2, 6; the
1970 AMM note is the source that closed a = 0, 8, 9, 10 as well (a = 10 is NOT
in the 1966 elimination — it is closed only in 1970).

## What this means for the run

- The run's headline lower bound `a ≥ 8` (from Wall 1988's ω(odd) ≥ 9 + the
  2-adic budget, `research/notes/lower-bound-on-a.md`) is **strictly weaker**
  than the 1970 literature bound `a ≥ 11`. The run's bound is not wrong — it
  is just not new, and it is not the best known.
- The thread `research/threads/a-ge-8-bound.md` (status: open, "kill a = 8")
  attacks a case Subbarao closed in 1970. **The thread should be closed as
  redundant**, not pursued. Its two proposed routes (Route A: H_even
  congruence a ≡ 2 mod 4; Route B: 257 = 2^8+1 is not 3-Higgs) are both
  subsumed by the 1970 elimination, which is unconditional (no H_even
  machinery needed).
- The genuinely open direction from GOAL.md is a **lower bound on a beyond
  11** in terms of ω, or impossibility of a residue class of a. Wall 1975
  (held) already pushed the working range to 11 ≤ a ≤ 38 for N < W
  (`N < W` requires `a < 38` since `(3/2)·2^38 > W`... more precisely the
  paper's inequality `2^A(1+2^A) d` argument), so the still-open seed range
  above the 1970 bound starts at a ≥ 11.

## Falsifier

A source showing Subbarao 1970 does **not** contain the a = 8 elimination
(would require reading the 2-page AMM note itself, which is paywalled — JSTOR
and T&F both 403'd this run). If the note contains only "a = 0, 3, 4, 5, 7
impossible" (matching the 1966 Theorem 2 list), the a ≥ 11 claim would drop to
a ≥ 8 and the a = 8 / a = 9 / a = 10 cases would be live. Two independent
Wall papers assert the fuller list, which is strong but not a substitute for
the note.

## 2026-08-13 update (librarian cycle 7)

- The U. Alberta author's publication list (`research/sources/subbarao-publications-ualberta.full.md`)
  confirms the note's shelf data (AMM 77(4):389–390) and carries a direct PDF
  link (`documents/1970Infinity.pdf`), but that PDF is **a JSTOR cover page
  only** (`https://www.jstor.org/stable/2316150`); the body is still not held.
  Summary: `research/summaries/subbarao-1970-infinity-unitary-perfect.md`.
- Claim `subbarao1970-a-ge-11` remains `asserted` (three Wall primaries +
  author bibliography), NOT promoted to checked. The note body is the one
  falsifier; REQUESTS row open.

## Witness check

All five known UPNs satisfy the claim vacuously or directly: {6, 60, 90,
87360} have a < 11 and are among the classified numbers; the fifth has a = 18
≥ 11. No witness refutes it.

```claim
id: subbarao1970-a-ge-11
statement: Any unitary perfect number other than the five known ones satisfies
  a >= 11, where 2^a || n. Equivalently 2^11 = 2048 divides any sixth example.
  The elimination of a = 0, 3, 4, 5, 7, 8, 9, 10 and the classification
  a = 1 -> {6, 90}, a = 2 -> {60}, a = 6 -> {87360} is attributed by three
  primary texts to Subbarao 1970, Amer. Math. Monthly 77 (1970) 389-390.
hypotheses: n is a unitary perfect number not among the five known; the
  attribution to Subbarao 1970 is via Wall 1975 Sec 2, Wall 1987 Sec 2, and
  Wall 1988 (all held full texts); the 1970 note itself is paywalled and not
  read. The 1966 paper (held) itself proves only a = 3,4,5,7 impossible and
  a = 1,2,6 classified; the a = 8, 9, 10 eliminations come via the Wall papers
holds-here: yes - any sixth UPN, the object this run targets
status: asserted
bearing: the run's headline lower bound a >= 8 (lower-bound-on-a.md) is weaker
  than 1970 literature. The thread a-ge-8-bound attacks the closed a = 8 case
  and is redundant. The open direction is a lower bound beyond 11 in terms of
  omega, or impossibility of a residue class of a
anchor: research/notes/subbarao-1970-a-ge-11.md;
  research/sources/wall-1975-fifth-unitary-perfect-number-pdf.full.md;
  research/sources/wall-1987-largest-odd-component.full.md;
  research/sources/wall-1988-nine-odd-components.full.md
contradicts: research/notes/lower-bound-on-a.md only in that a >= 8 there is
  presented as the frontier; it is not false, merely weaker
answers: lower-bound-on-a-beyond-11
```

## Recorded

This note supersedes the lower bound in `research/notes/lower-bound-on-a.md`
as the *best known*; that note's derivation (a ≥ 8 from Wall 1988 + budget)
remains correct as a self-contained proof but is not the literature frontier.
See also `research/notes/wall-1975-bounds-and-102-claim.md` for the
companion finding on search bounds.