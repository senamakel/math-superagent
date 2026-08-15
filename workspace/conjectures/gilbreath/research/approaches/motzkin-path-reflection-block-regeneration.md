# Motzkin-path reflection block regeneration

```approach
idea: The leading {0,2} block, halved, is a {0,1} word whose adjacent
differences lie in {0,±1} — i.e. a Motzkin path. The (2,4)-regeneration
event is the first "2-step" that exits the Motzkin class, and the edge bit
is the path's endpoint height. Reframe regeneration as the exit/hitting
statistics of Motzkin paths and lower-bound the edge-hit (height-1) rate
with the André/Dvoretzky–Motzkin reflection principle and Motzkin–Catalan
enumeration.

mechanism: Halve the block: A_k(i) = 2·h_i with h_i ∈ {0,1} for i = 1..b_k.
Then h is a height function on the path graph with steps h_{i+1} − h_i ∈
{0,±1} — a Motzkin path starting at h_1. This is not a hypothesis; it is the
run's own established giant-jump characterization (a {0,2} block is exactly a
1-Lipschitz halved chain, claim in CONTEXT.md "Giant-jump mechanism"), so the
alphabet of the block object is bounded: {0,±1}. The step law (settled) says
the block erodes one cell per row. The intruder pair (x,y) = (2,4) is exactly
(edge height = 1, next step = +2): the Motzkin path's endpoint is at height 1
and the following position would leave the {0,±1} class by a jump of 2. Thus
each (2,4)-event is a *first exit* of a Motzkin excursion, and the conjecture
is the assertion that these exits recur fast enough that the recharge sum
Σ(j_i+1) never falls k−1 behind. The reflection principle (André; the
Dvoretzky–Motzkin cycle lemma) enumerates 1-Lipschitz words with a prescribed
endpoint among cyclic shifts; that is the right tool to turn "the block is a
Motzkin path" into a lower bound on how often the endpoint lands at height 1 —
the exact trigger needed for regeneration once the intruder has drained to 4.
This is NOT the refuted christoffel/balanced-word route (that object was the
gap word, with unbounded alphabet) and NOT lattice-path-enumeration of the
left column: the object here is the block itself, which is provably Motzkin.
The precise quantitative bound (how the reflection principle transfers to the
height-1 frequency of a fixed, non-random Motzkin word) is speculative and is
the thing to work out.

status: refuted
precedent: Motzkin-path / reflection-principle / cycle-lemma mathematics is
  real and precisely stated (the candidate's invented half is the transfer, and
  that half has NO precedent):
  - Dvoretzky–Motzkin cycle lemma: "A problem of arrangements", Duke Math. J.
    14 (1947) 305–313; modern statement + proof in Dershowitz–Zaks, "The Cycle
    Lemma and Some Applications", Eur. J. Combin. 11 (1990) 35–40
    (https://doi.org/10.1016/S0195-6698(13)80053-4): for a sequence of
    integers with total sum k > 0, EXACTLY k of its n cyclic rotations have all
    positive partial sums. Verified statement — it counts cyclic ROTATIONS of a
    fixed multiset, the enumerative input to ballot/lattice-path counts.
  - André reflection principle (ballot theorem) — the classical counting
    device; see the survey "A history and a survey of lattice path
    enumeration" (J. Statist. Plann. Inference 101 (2002) / Discrete Math),
    https://www.sciencedirect.com/science/article/abs/pii/S0378375810000315.
  - Motzkin paths and their enumeration by endpoint/height: "Bijective
    Recurrences for Motzkin paths" (Adv. Appl. Math. 27 (2001)),
    Prodinger "Peakless Motzkin paths of bounded height" (arXiv:2308.03080),
    "Counting lattice paths via a cycle lemma" (EPTCS 2011, cycle-lemma into
    Motzkin-Catalan-type counts).
  - NO source applies Motzkin-path enumeration, the reflection principle, or
    the cycle lemma to Gilbreath's conjecture or to {0,2}-block regeneration.
    Searches for "Motzkin Gilbreath", "lattice path Gilbreath block", "cycle
    lemma regeneration" returned only the Gilbreath-polynomials literature
    (Gatti 2023 MDPI), Chase's random analogue (Math. Ann.), and general
    lattice-path enumeration — none touches this object. Honest could-not-find
    on the application.
killed-by: The load-bearing transfer (reflection/cycle-lemma counts to the
  height-1 frequency of a FIXED non-random block) fails on three grounds:
  (1) The block as a halved {0,1} word is a 1-Lipschitz chain — genuinely the
  run's own characterization — but it is NOT a Motzkin path in the standard
  enumerative sense. A Motzkin path is an unbounded-height lattice path that
  starts at height 0, never goes below the axis, and (usually) returns to it;
  the standard counts (Motzkin numbers, peakless Motzkin, endpoint-at-height-h
  counts) run over ALL paths/rotations of a step multiset. The block's heights
  are confined to {0,1} (a height-1 strip), so it is the degenerate,
  zero-content Motzkin class, and the reflection/cycle-lemma machinery that
  gives interesting counts is precisely the part that assumes unbounded (or at
  least variable) height.
  (2) The Dvoretzky–Motzkin cycle lemma and André reflection are statements
  over cyclic ROTATIONS of a fixed multiset, chosen to give enumerations of
  lattice-path classes. The block is a SINGLE deterministic word that erodes
  by one cell per row; there is no enumeration over rotations, and no theorem
  gives the endpoint-height-1 frequency along a fixed word's erosion. The
  candidate itself flags this transfer as speculative — the literature check
  says no such theorem exists and no transfer argument is available.
  (3) Even a working height-1 bound could not close regeneration: a (2,4)-event
  needs BOTH edge = 2 (the block's endpoint height 1) AND intruder = 4. The
  intruder value is set by the tail A_k(b_k+1), which is OUTSIDE the block, so
  the Motzkin structure controls only the necessary half-condition. And the
  run has already PROVED (`edge-interior-invertibility`) that the block's
  interior pattern FULLY determines when the edge reads 2 (e=0 ⟺ h=0, with the
  edge-map invertible) — there is no leftover freedom for an enumeration to
  average over.
  What survives: the identification "halved block = 1-Lipschitz chain, steps
  in {0,±1}" is real, is the run's own established object, and is exactly the
  `lipschitz-excess-lyapunov` approach in this folder. The Motzkin-path LABEL
  is a genuine named object, but the block is a strip-1 degenerate case of it,
  so the label buys nothing that the 1-Lipschitz characterization (already
  recorded) does not.
first-step: (superseded — see killed-by) On the real rows
  (code/out/blocks_depth1000.json, code/out/witnesses.json), extract the
  halved block as a 1-Lipschitz chain for every live row and verify: (a) all
  steps ∈ {0,±1} (holds trivially by definition of a {0,2} block — this is the
  identification, not a hypothesis); (b) endpoint height equals the edge bit
  A_k(b_k)/2; (c) a (2,4)-event occurs precisely when endpoint height = 1 and
  the intruder = 4. The first two are the run's own proved reframings; the
  third is the half-condition gap named in killed-by (3). Do not spend a
  compute cycle on a reflection-principle bound — none exists for a fixed
  word, per killed-by (2).
```
