# Librarian cycle report

Cycle focus: the library is mature and phase 1 is complete (ROOT.md states the
structure of a minimal counterexample, the verification bound, and three+
settled restricted classes). Per the steering, further gathering happens only
against a stated gap. The one genuinely thin, load-bearing angle this cycle was
the **allowable-sequence thread's unsourced framework primitives** — the thread
that is the live frontier (steer 12) was running on a circular-sequence
definition that was flagged `gp80-not-held-circular-sequence-unsourced` /
`staircase-convexity-unsourced` on disk, with no primary on disk.

## Acquired this cycle

**Dumitrescu, "The Dirac–Goodman–Pollack Conjecture", arXiv:2204.06101 (2022, v3).**
- Full text: `research/sources/dumitrescu-Dirac-Goodman-Pollack-conjecture-arxiv2204.06101-html.full.md`
  (48 KB, fetched from the arXiv HTML rendering; the `/abs` fetch returned only
  metadata, so I downloaded the `html/2204.06101v3` full text).
- Summary: `research/summaries/dumitrescu-Dirac-Goodman-Pollack-conjecture-arxiv2204.06101-html.md`
  (replaces the auto-digest).
- Why it matters: it is a clean primary statement of the **Goodman–Pollack
  allowable/circular-sequence framework** the active thread operates on — the
  circular sequence from rotating a line's projection order, the half-period from
  identity to reversal, the non-overlapping-adjacent-subsequence reversal rule,
  local sequences Λ_i, and wiring-diagram realization. Critically it states the
  realizability bind as a cited primary: **not every allowable sequence is
  realizable by a point set, but every one is realizable by a pseudoline
  arrangement**. That is exactly the `hm-allowable-realizability-etr-complete`
  bind the thread must respect — now on disk instead of recalled.
- Durable finding recorded in Cognee (`remember_memory`).

## Sought but not obtained (recorded, not gaps re-opened)

- **Goodman–Pollack 1980**, "On the combinatorial classification of nondegenerate
  configurations in the plane" (JCTA 29:220–235): paywalled at Elsevier
  (DOI 10.1016/0097-3165(80)90011-4); the MaRDI portal confirms bibliographic
  details only, no PDF. The definitional content it carried is now held via
  Dumitrescu's primary restatement, so this is a record, not a live gap.
- **Goodman–Pollack 1993 survey chapter** (Springer): paywalled at
  link.springer.com; full text not reachable without subscription.
- **AMS Notices retrospective** (2024): 403 Forbidden on download.

## Request posted — declined, correctly

`request_research` for the extreme-in-projection/staircase-convexity criterion was
refused because the library already carries 8 claims bearing on it. That refusal
is correct: the extreme-in-projection characterization is elementary and has been
machine-verified against `lib/es_geom` by the thread itself (agrees on all
|S|≥4 subsets, only the trivial 3-subset triangle artefact), and the
`gsplit-enum-completeness` and `g-cupcap-verified` claims back the sequential /
cup-cap routes. Chasing the paywalled GP primaries for this one elementary point
would be gold-plating; the substance is held. The `staircase-convexity-unsourced`
flag stands as an honest label — the definition is now sourced (Dumitrescu), the
machine check is done, but the literal "contiguous staircase of reversals"
characterization for realizable point sets remains asserted-by-run, not
proved-by-source.

## Nothing further (next cycle)

Phase 1 does not need more gathering. The frontier's top targets are either
already in the library (struck-through) or paywalled (GP80/93, AMS). The next
cycle's highest-value move would be to answer one of the run's genuinely open
computational gaps (e.g. reproducing ES(6)=17/ES(5)=9 with this run's own
encoder, per tasks) — but that is tool_builder's/scholar's work, not the
library's, and there is no stated library gap left to fill this cycle.
