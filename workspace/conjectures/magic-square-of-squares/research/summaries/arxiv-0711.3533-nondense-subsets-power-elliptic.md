# Viada, "Non-dense subsets of varieties in a power of an elliptic curve" (2007)

[[arxiv-0711.3533-nondense-subsets-power-elliptic]]

Source: Evelina Viada, "Non-dense subsets of varieties in a power of an elliptic
curve", arXiv:0711.3533 [math.NT] (2007; the numbering/date shown in arXiv
metadata appears as 2007). Full text:
`research/sources/arxiv-0711.3533-nondense-subsets-power-elliptic.full.md`
(81.9 KB from the ar5iv HTML rendering at
https://ar5iv.labs.arxiv.org/html/0711.3533; the PDF is at
https://arxiv.org/abs/0711.3533).

## What it establishes

Let E be an elliptic curve **without CM** defined over Q̄, and V ⊂ E^g a
**transverse d-dimensional** subvariety. The set of algebraic points of bounded
height that lie close (in a height-sense) to the union of all algebraic
subgroups of E^g of codimension d+1, translated by a point of a finite-rank
subgroup Γ ≤ E^g, is **non-Zariski-dense** in V. If Γ = 0, weak-transverse
suffices. The result is optimal w.r.t. the codimension of the algebraic
subgroups.

Method: an essentially optimal **effective version of the Bogomolov conjecture
for subvarieties of E^g** (proved in §3–6), combined with the David–Philippon /
Rémond explicit machinery; the paper's Theorem 6.2 cites Rémond [10] Thm 1.2,
and 6.3 cites Rémond [11], so Viada builds on (and refines) the same
David–Philippon–Rémond constant chain the run's `dp07-explicit-constant` lane
is chasing. The normalised-height lower bounds obtained are explicit in the
degree and ambient data.

## Bearing on this problem

This is a neighbouring effective-height result in E^g (the same shape of
subvariety ambient as the run's AP-in-x-coordinates configuration in E³,
though the run's variety is a *curve-in-E³* and Viada's is a *transverse
d-dim subvariety* with a codimension-relative subgroup-distance condition).
It corroborates that **effective, degree-dependent** minorations exist in this
setting (so the DP07 search lane is not empty), but it does not itself deliver
the DP07 constant specialised to the MSS AP configuration. Relevant — as
technique and as evidence that explicit E^g bounds are tractable — not
decisive.

## Claim block

```claim
id: viada-nondense-bounded-height-eg
statement: For E/Q̄ without CM and V ⊂ E^g transverse d-dimensional, the
  bounded-height algebraic points of V near the union of codimension-(d+1)
  algebraic subgroups translated by a finite-rank Γ are non-Zariski-dense
  (Γ=0: weak-transverse suffices); proved via an effective Bogomolov bound for
  subvarieties of E^g using David-Philippon/Rémond constants.
hypotheses: E without CM over Q̄; V transverse (weak-transverse if Γ=0)
holds-here: partial — same ambient E^g but the MSS AP subvariety is a curve,
  not a transverse d-dim variety; does not give the DP07 constant
status: proved-where-stated (primary text on disk)
bearing: evidence the effective E^g lane is tractable; context for
  dp07-explicit-constant; does not fill it
anchor: research/summaries/arxiv-0711.3533-nondense-subsets-power-elliptic.md
```