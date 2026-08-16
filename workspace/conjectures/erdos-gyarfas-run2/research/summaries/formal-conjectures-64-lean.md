# Formal Conjectures 64 — existing Lean statement

Source: google-deepmind/formal-conjectures, ErdosProblems/64.lean. Full text
held; [[formal-conjectures-64-lean]].

## What it establishes

An existing Lean 4 formalisation of the conjecture (Erdős Problem 64) using
Mathlib's SimpleGraph/Walk/IsCycle:

```
(G : SimpleGraph V) [Fintype V] [DecidableRel G.Adj]
→ G.minDegree ≥ 3 → ∃ k ≥ 2, ∃ v, ∃ c : G.Walk v v, c.IsCycle ∧ c.length = 2^k
```

The theorem is stated with `sorry` (unproved), and `𝓝` no context yet. The
k ≥ 2 convention is explicit (so length 4, 8, …; excludes the vacuous 1, 2).

## For this problem

This is the canonical formal statement the run's Lean 4 file should reproduce
or adapt (GOAL.md criterion 4). The formalisation reflects the k ≥ 2
convention already. It is an *existing* statement with `sorry` — the run can
formalise it without `sorry` as a deliverable, and formalise any lemma it
proves.

```claim
id: lean-formal-statement
statement: The conjecture has an existing Lean 4 formalisation (minDegree ≥ 3 → ∃ k ≥ 2, cycle of length 2^k) with the theorem stated as a sorry.
hypotheses: SimpleGraph V, Fintype, DecidableRel, G.minDegree ≥ 3
holds-here: yes — the reference formal target
status: sourced (existing formalisation, unproved)
bearing: gives the formal skeleton and the k ≥ 2 convention the Lean deliverable must use
anchor: research/sources/formal-conjectures-64-lean.full.md
```
