# Granville 2026 "Piercing Gilbreath's Conjecture" (arXiv:2607.04166, cs.CR) — full PDF read

<!-- source: https://arxiv.org/abs/2607.04166 | abstract page: sources/granville-2026-piercing-gilbreath-arxiv.full.md | full PDF: sources/granville-2026-piercing-gilbreath-FULLPDF.full.md -->

## Correction to the earlier dismissal

The earlier summary dismissed this paper from its arXiv `/abs/` landing page alone
(6.8 KB: title, categories, submission history, no statements), recording
`granville-2026-piercing-gilbreath-not-load-bearing` as `asserted`. The actual PDF
(2,732 lines, 70 theorem/lemma/proposition/proof occurrences) has now been read
(full text: `research/sources/granville-2026-piercing-gilbreath-FULLPDF.full.md`; note:
`research/notes/granville-2607-04166-actually-read.md`). **The paper is still not a
peer-reviewed proof, but it contains two statements worth keeping and one proof gap
worth measuring.** The blanket "no result this run can use" was wrong.

Author is Vincent Granville (data-science/fintech, **not** Andrew Granville the number
theorist), self-published via BondingAI.io, cs.CR. Standard of proof uneven — e.g.
Theorem 2.5's "proof" is `"Take kappa_0=0 and the theorem is proved!"` — so Lemma 5.4
below must be re-derived, not adopted.

## What is usable

Notation is the *right diagonal*: `delta_0(q_n)=q_n`, `delta_1(q_n)=g_n=q_n−q_{n−1}`,
`delta_k(q_n)=|delta_{k−1}(q_n)−delta_{k−1}(q_{n−1})|` — the run's triangle read along
the diagonal through `q_n` (`delta_k(q_n)=A_k[n−k]`). The "0-2 cycle" is the maximal
`{0,2}` suffix of that diagonal; `nu_2(q_n)` counts the 2s in it.

- **Lemma 5.4 (p.16).** If `q_1..q_{n−1}` is valid & successful, then `q_1..q_n`
  succeeds provided `g*_n <= 2·nu_2(q_{n−1}) + 2`, where `g*_n = max(g_2,...,g_n)`
  (record gap). Stated as an iff on a refined quantity `v_n`, weakened to the `g*_n`
  bound. **This is the run's own budget inequality `Σ(j_i+1) ≥ k−2` in different
  coordinates**: descent supply (`2·nu_2`) against record-gap demand, and the demand
  side is the *prime gap* — the side where the literature lives.
- **Theorem 5.5 (p.16).** If `g*_n < n^α` and `nu_2(q_{n−1}) > n^β` with `β>α`, then
  for large `n` success at `q_{n−1}` transfers to `q_n`. The demand side
  `α = 0.525` is **unconditional for primes** (Baker–Harman–Pintz 2001, cited
  correctly). **The whole remaining content is a lower bound on `nu_2`** — which
  Granville does not prove (he offers `β=0.99` by his own Conjecture 5.1 and a
  `nu_2 ~ n/2` heuristic).

## Measured here (operator, exact arithmetic, primes < 3e6)

`code/out/nu2_granville_check.captured.txt` (and an independent re-verifier
`code/verify_nu2_claim.py`, second route, written for this session):

- `nu_2/n` sits in [0.42, 0.52] for n ∈ {50,100,200,400,800,1600,3200,3999} — the
  `n/2` density, not merely `n^β` for any `β>0.525`. At n=3999 the theorem needs
  `nu_2 > 78`; the true value is 2048 (a factor of 26 of slack).
- **Lemma 5.4's hypothesis `g*_n ≤ 2·nu_2+2` holds at every sampled n** with two
  orders of margin (record gap 72 against budget 4098 at n=3999).

## The proof gap — machine-checked

`code/out/lemma54_iff_check.captured.txt` (Killer: lemma54_iff_check.py, n=20..2500):
Granville's Lemma 5.4 proof **discards the case "some `delta_{k−1}(q_n)=0` inside the
gray block"** with a hand-wave. On the real primes this discarded case occurs in
**100% (2480/2480) of rows**. Yet the lemma's *statement* still holds everywhere:
the iff `(v_n ≤ 2·nu_2+2 ⟺ success)` has **0 violations** and the weakened
sufficiency `(g*_n ≤ 2·nu_2+2 ⟹ success)` has **0 violations** across all 2,480
rows. So the statement is true numerically, but Granville's proof is incomplete —
it skips the case that is universal. The lemma must be re-derived with the δ=0 case
handled, before anything cites it.

## Bottom line

**Do not cite the paper as a proof** (Theorem 5.5 is conditional on Granville's own
unproved Conjecture 5.1, and Lemma 5.4's proof is incomplete — it discards a
universal case; see the separate note `research/notes/lemma54-discarded-case-is-universal.md`
and its claim `lemma54-discarded-case-universal`). **Do keep the reduction.** Lemma 5.4
restates the run's recharge budget inequality with the *prime gap* on the demand side,
and Theorem 5.5 turns the whole problem into a density bound on `nu_2` (2s in a
diagonal), which empirically holds with huge margin (`nu_2 ~ n/2` vs the needed
`n^0.525`). The `g*_n` demand side is unconditional via Baker–Harman–Pintz. This is a
genuine reduction worth recording, not a crank to discard.
