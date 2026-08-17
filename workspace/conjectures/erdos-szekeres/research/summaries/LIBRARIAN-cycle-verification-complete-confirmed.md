# Librarian cycle — library verified complete (independent re-audit)

<!-- role: librarian; this cycle did NO new downloads, for reasons given below -->

## Verdict in one line

The reference library already meets the phase-1 exit test and every standing
REQUEST row is answered by a genuine primary full text on disk. This cycle
re-audited that conclusion independently (list_workspace, grep, search_claims,
read_ledger, source read) rather than taking the prior two completeness audits
on faith, and it holds.

## What was verified this cycle

1. **Canonical tier all held, with URLs inside the files.** Re-listed
   `research/sources/` (70+ full-text files). Every result ROOT.md and CLAIMS.md
   attribute has an `anchor:` to a concrete file on disk. Key primaries confirmed
   present:
   - Erdős–Szekeres 1935 (Compositio): `sources/erdos-szekeres - A combinatorial problem in geometry - Compositio 1935 full.full.md` (numdam).
   - Erdős–Szekeres 1960/61 lower-bound construction:
     `sources/erdos-szekeres-1961-...-renyi.pdf.full.md` (https://renyi.hu/~p_erdos/1960-09.pdf).
   - Szekeres–Peters 2006 (ES(6)=17): `sources/peters-szekeres-17-point-esz-ANZIAM-2006.full.md` (Cambridge PDF).
   - Suk 2017 (`sources/suk-...-arxiv1604.08657.full.md`), Holmsen–Mojarrad–Pach–Tardos,
     Baek–Balko SoCG 2025, Norin–Yuditsky, Vlachos, Mojarrad–Vlachos, Tóth–Valtr,
     Chung–Graham, Kleitman–Pachter, Morris–Soltan survey.
   - SAT/orientation family: Balko–Valtr ENDM 2015, Scheucher, Dumitru ES(7),
     SMQH, PointSAT, Koshelev–Koshka, Heule–Scheucher, Subercaseaux ITP, Felsner–Weil
     signotopes, Goodman–Pollack–Sturmfels, Bergold–Felsner–Scheucher, Wikipedia CC-system.
   - Restricted classes: Damásdi et al. (saturation), Károlyi–Tóth (forbidden
     order types), Pór–Valtr (partitioned), Bárány–Valtr (positive fraction),
     Baek–Balko (split/decomposable), Horton 1983 (empty 7-gons, adjacent).

2. **Request rows answered on disk.** Three request ids exist
   (`balko-valtr-attack-baa4`, `open-access-full-1e6e`, `full-text-faithful-b96b`)
   and each is answered by a claim block carrying `answers: <id>` inside a held
   summary. Grep confirms the `answers:` tags resolve to real files. The rows
   still *render* open in `derived/REQUESTS.md` — this is the documented
   re-derivation-state artifact, not a library gap (see
   `summaries/LIBRARIAN-audit-requests-answered-derivation-artifact.md`). The
   primary content backing each is on disk and citable.

3. **Search_claims confirms the claims ledger is populated and anchored.** For
   the Balko–Valtr / Baek–Balko / realizability cluster, every returned claim
   carried a `Check it at:` path naming a held file. No claim is stranded on
   recall.

## Why no new downloads this cycle

- The steering rule in force (recorded in CONTEXT.md) is that gathering proceeds
  only against a stated gap in `research/REQUESTS.md`. There is no open gap with
  an un-answered need: all three request rows are answered by held primaries.
- The only canonical item ever flagged as not-in-library is Knuth's *Axioms and
  Hulls* book itself (paywalled). Its content (CC-system axioms) is already
  covered in the held Wikipedia-cc-system + Felsner + Dumitru + Bergold sources.
  Not worth a Springer paywall fetch.
- Pach–Solymosi k-convex chapter exists only as a MIS-DOWNLOAD stub; the IWOCA-2019
  version of the same content is held (`balko-bhore-...-IWOCA2019.full.md`), and it
  is a drift-guarded adjacent problem.
- Erdős–Tuza–Valtr 1996 "Ramsey-remainder" primary is paywalled/unobtainable in
  open access (recorded); its content is faithfully restated in held Baek
  (arXiv:2206.04260, Thm 1.5) and Balko–Valtr.

Downloading anything here would be busywork: it would either duplicate a held
primary or pull a paywalled page whose content is already faithfully held.

## Net

Library is complete at the fidelity this run requires. ROOT.md meets GOAL.md
criterion 1; the oracle foundation (4-point criterion + es_construct + 1961
primary) is held; every claim traces to a file; every request row is answered
by a primary on disk. The next valuable work is the run's own
oracle/computation (a run-side task, not librarian acquisition), and the
head-of-queue items in the tasks ledger already point there.
