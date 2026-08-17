# Samotij, "Entropy methods in combinatorics" (arXiv:2607.24414, 2026)

**Full text:** [[samotij-entropy-methods-combinatorics-2026.full]] · **Source URL:** https://arxiv.org/html/2607.24414

A selective survey by Wojciech Samotij (Tel Aviv) of entropy as a tool in extremal
and probabilistic combinatorics. Downloaded because it is cited by two of the
library's own sources (Yu dimension-free-bounds, Wakhare) and was not yet on disk.
It is a *pedagogical survey*, not a new result — its value is as a current-author
confirmation of the record and of the entropy-method framing.

## What §6 establishes (union-closed sets conjecture)

A concise, current (2026) restatement of the entropy method's history and record,
matching the library exactly:

- **Gilmer [43]** first proved an element in at least **1%** (one percent) of sets.
- The constant **(3−√5)/2 ≈ 0.38** was reached **independently by four groups**:
  [4] Alweiss–Huang–Sellke, [17] Chase–Lovett, [86] Pebody, [94] Sawin.
- **Two subsequent works** refined it further via Sawin's dependent-coupling
  suggestion: **[13] Cambie** (arXiv:2212.12500) and **[102] Yu** (Entropy 25(5):767,
  2023, where Yu presents it as ≈ 0.38234). The survey counts only these two as the
  follow-up improvements — **Liu's conditional ≈0.38271 is not among them**, which is
  independent confirmation that Liu remains outside the published/standard record.

Relevant to the run's **proved ceiling** claim `yu-gamma-hat-nonincreasing` /
`t̂_max = 0.3823455334`: the survey gives the constant as "(3−√5)/2 ≈ 38%" and the
two improvements "slightly improved", i.e. no 2026 source asserts a jump past
0.38234/0.3823455 in this standard survey.

## Theorem 6.1 (the heart, in survey form)

For `A,B` independent samples from a distribution over subsets of `[n]`: if
`H(A) > 0` and `max_i P(i ∈ A) < (3−√5)/2`, then `H(A∪B) > H(A)`. The proof sketch
reduces to: `Δ_i = E[h(p_i + q_i − p_i q_i) − h(p_i)] ≥ 0`; significance of the
barrier is that **(3−√5)/2 is the only nontrivial solution of `h(2p−p²) = h(p)`**,
and the key inequality `h(p²) ≥ ((√5+1)/2)·p·h(p)` (Boppana [9], arXiv:2301.09664).

## Claim blocks

```claim
id: samotij-confirms-uc-record-2026
statement: A 2026 survey (Samotij) credits the (3−√5)/2 constant to four independent
  groups (AHS, Chase–Lovett, Pebody, Sawin) and lists exactly two follow-up
  improvements via Sawin's dependent coupling: Cambie (arXiv:2212.12500) and Yu
  (Entropy 25(5):767, 2023, ≈0.38234). Liu's ≈0.38271 is not counted among them,
  confirming it is outside the standard published record.
hypotheses: currency of a survey author's enumeration, not a proof.
holds-here: yes — consistent with library's published-record claim (Yu 0.38234
  published; Cambie reached the same value independently as a preprint; Liu is
  conditional/unpublished).
status: asserted-by-source (survey enumeration).
bearing: settles/confirms the freshness of the published record and the "two
  follow-up works" count; no new constant or counterexample.
anchor: research/sources/samotij-entropy-methods-combinatorics-2026.full.md §6
```

```claim
id: samotij-barrier-characterization
statement: (3−√5)/2 is the only nontrivial solution of h(2p−p²) = h(p); the iid-OR
  entropy inequality reduces to h(p²) ≥ ((√5+1)/2)·p·h(p) (Boppana). Stated as the
  barrier's significance.
hypotheses: binary entropy h; the iid-OR setting of Theorem 6.1.
holds-here: yes — matches the library's `iid-barrier-exact` and `boppana-entropy-inequality`.
status: asserted-by-source (restatement in survey; the underlying result is proved
  in the library's Boppana source).
bearing: corroborates the barrier's exact characterization already held.
anchor: research/sources/samotij-entropy-methods-combinatorics-2026.full.md §6
```

## Bearing for this run

- Independent (2026, by a leading entropy-method author) confirmation that the
  published record stands: **Yu ≈ 0.38234** published, Cambie the independent
  preprint route to the same value, Liu conditional/unpublished.
- No new constant, no new class, no counterexample. The survey's non-UC sections
  (randomised chain rule, Shearer, Pinsker, Turán/entropy) do not touch the
  union-closed conjecture beyond §6.
- **Nothing here changes a number in CONTEXT.md or research/ROOT.md.** Its value is
  as a freshness/consistency anchor only.
