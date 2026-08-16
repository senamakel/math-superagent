# Librarian cycle note — the one open gap, and why no download follows it

Status: **pause (NOTHING FURTHER)**. The library passes the phase-1 test
(ROOT.md: counterexample structure, verification ceilings, settled classes).
The subject is covered from all the directions the librarian brief names.

## The single genuinely open item, and its correct handling

The whole investigation now turns on two pure-F2/hypergeometric lemmas
(`G-threshold-asymptotic-zero`, `G-threshold-concentration`), both gated by one
elementary bound:

    for X ~ Hypergeometric(n, m, w):
        |E[(-1)^X]| <= max_j P[X=j] = O(1/sqrt(1 + Var X))

The run's own note (`research/notes/threshold_limit_open_lemma.md`) judges this
`NOT a missing source` — elementary, self-provable (log-concavity/unimodality +
local limit); the only thing to pin is the absolute constant C. A theorem_prover
or symbolic role derives it; no download is needed. `threshold-limit-hinges-on-
hypergeometric-mode-bound` records this in the claims ledger.

## Candidate surfaced by a sweep (search re-checked)

The canonical reference that would make the constant and the
hypergeometric-is-ultra-log-concave fact *cited* rather than self-proved:

- Saumard & Wellner (2014), *Log-concavity and strong log-concavity: a review*,
  Statistical Science 29(1). https://doi.org/10.1214/14-ss107
  - Variance-peak inequality for log-concave densities: f at the centre is
    tightly controlled by Var (1/12 · Var <= sup f^2 <= C · Var).
  - Hypergeometric is equal in distribution to a Bernoulli sum, hence ULC.

**Not downloaded.** Reasons, both operative rules in this workspace:
1. The run's note says the gap is self-provable; a source is not the fix, a
   theorem_prover is. Fetching would be spend with no information gain.
2. Search is frozen absolute (directive 30, pending the never-run Ratio-B
   N=160000 discriminator) and directive 49 closed pass 3 with no new lines.
   The new-source gate (name which unworked FRONTIER candidate answers and why)
   is not met: none answers — the gap is in-house theorem-proving.

## What a later role should do

- theorem_prover: derive `max_j P[X=j] <= C/sqrt(1+Var X)` for hypergeometric X
  and pin C (numerically verify n, m, w <= 40; the sharp corner n=6, m=3, w=2
  has |E|=0.2, max atom = 3/5 = 0.6).
- Only if that role explicitly wants the constant as a *cited* standard result
  (not self-derived) should it lift the freeze and fetch the Saumard-Wellner
  DOI above. Today it is a lead, not a claim.
