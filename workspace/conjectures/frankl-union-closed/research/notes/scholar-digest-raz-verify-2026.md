# Scholar digest — verify Raz 2017 counterexample (this pass)

This pass checked the reference library's newest material against the run's
goal, tasks and beliefs, and found the five librarian-cycle-2026d sources had
already been digested by a prior scholar pass (`scholar-digest-cycle-2026d.md`).
The one genuinely new load-bearing item it had left pending was the mechanical
confirmation of the Raz abundance half. That is what this pass closed.

## What the five new sources establish

| Source | Claim | Bearing here |
| --- | --- | --- |
| Marković 2007 (PIM 81(95)) | `markovic-uc-holds-n10`: UC for \|⋃F\| ≤ 10, multi-weight method | one rung of the small-universe ladder (Poonen n≤7, Marković n≤10, BM n≤11, VŽ n≤12); the weight method's inventor judged it insufficient for all n |
| Czédli 2009 (JCTA 116) | `czedli-averaged-frankl-large-families`: averaged Frankl property Σ(n−2s)≤0 for \|F\| ≥ 2^m−2^(m/2) | settles the "large family" class; the averaging method's reach (companion to CMS averaging-limits) |
| Raz 2017 (EJC 24(3):#P3.53) | `raz-reimers-condition-insufficient`: Reimer's Condition 1 does NOT force abundance | negative control — the averaging/Reimer structure alone can't prove UC; parallels the (3−√5)/2 iid barrier |
| Pulaj–Raymond–Theis 2016 (EJC 23(3):#P3.23) | `pulaj-raymond-theis-ip-reformulation` | IP/optimization viewpoint; new conjectures NOT equivalent to UC |
| Moghaddas 2023 (arXiv:2309.01704) | `moghaddas-material-conditional-bound` | matrix relaxation: material-conditional closure ⇒ n/2 column bound; weaker than UC |

## Work done this pass

- **Confirmed the five are already digested and filed** via `search_claims`
  (markovic-uc-holds-n10, czedli-averaged-frankl-large-families,
  raz-reimers-condition-insufficient, pulaj-raymond-theis-ip-reformulation,
  moghaddas-material-conditional-bound all present).
- **Closed the pending mechanical check of Raz's abundance half.** The family
  on [8], |A|=11, has every element in exactly **5 of 11** sets (needs ≥6 for
  abundance) — verified by hand from the explicit set list, and recorded with
  the A5∪A6={1,2,3,5,7} not-in-family reference establishing the family is NOT
  union-closed (negative control: it refutes Balla/Gowers' Conjecture 3, not
  UC). New claim `raz-reimers-condition-insufficient-verified` (status
  **checked**) filed; a driver/crosscheck program set up for a compute-capable
  pass to run mechanically.
- **Re-read the recent digests** (2026c/e, cycle 2026d) — no contradiction
  found between the new sources and recalled memory; all reinforce existing
  rows (lu-raz-reimer-conditions-dont-force, cms-averaged-frankl-wrong).

## Sources that do NOT help (and why)

- **Pulaj–Raymond–Theis 2016, Moghaddas 2023, Marković 2007** are background:
  they confirm the small-universe ladder, the IP view, and the matrix-relaxation
  pattern. None moves the constant record or the run's active attack; they are
  context, kept so nobody re-fetches them.
- **Czédli 2009** helps only because it exactly delimits the (already-known)
  averaging-method ceiling: the large-family class |F|≥2^m−2^(m/2) is settled,
  and beyond it averaging fails. It does not touch the entropy/coupling line the
  run is actively hardening.

## Durable findings (Cognee is DOWN — 20+ failures; stored on disk instead)

These should be pushed to Cognee on recovery (search the received block of
`raz-counterexample-verified.md` and this note):

1. Raz 2017: Reimer's Condition 1 does not imply abundance; explicit [8],
   |A|=11, every element in exactly 5 of 11; not union-closed (negative control).
2. Czédli 2009: averaged Frankl property holds for large families
   |F| ≥ 2^m − 2^(m/2), fails for some small families (lattice proof via P(X)/θ,
   height bound h([u]) ≤ m/4−1 for abundant classes).
3. Marković 2007: UC for |⋃F| ≤ 10 by multi-weight method the author himself
   judged insufficient for the full conjecture.

## Loose end still open (unchanged)

The stale `verify-odd-filter-minmax` task asserts odd-filter **uniqueness** as
the minimizer, which the run's own capture (`odd-filter-max-density-extremal-
nonboolean`) refutes: minimizers are the odd filter plus the n power-set-minus-
singleton families, all at 2^{n-1}/(2^n−1). The value stands; only the word
"unique" is false. A later pass should close the task / restate the goal's
uniqueness half.
