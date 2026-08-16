# Mathlib's `erdos_szekeres` is the monotone-subsequence theorem, NOT the convex-polygon conjecture

Source: https://leanprover-community.github.io/mathlib_docs/wiedijk_100_theorems/ascending_descending_sequences.html
Full text: [[mathlib-erdos-szekeres-monotone-subsequence-full]]
Verified: downloaded and read this run.

## What it establishes

`theorem erdos_szekeres {r s n : ℕ} {f : fin n → α} (hn : r * s < n) (hf : fn.injective f) :
  (∃ t : finset (fin n), r < t.card ∧ strict_mono_on f t) ∨
  (∃ t : finset (fin n), s < t.card ∧ strict_anti_on f t)`

This is Theorem 73 of the Wiedijk 100 Theorems list, formalised in `mathlib-archive/wiedijk_100_theorems/ascending_descending_sequences.lean` (synchronised with mathlib4). It proves: a sequence of more than r·s distinct values contains an increasing subsequence longer than r or a decreasing subsequence longer than s — the (r−1)(s−1)+1 Erdős–Szekeres **monotone-subsequence** theorem. Proof by labelling each element with the pair (longest increasing subseq ending there, longest decreasing subseq ending there); the pairs are unique so >r·s elements force a long monotone subsequence.

## Implication for this run (GOAL 5 — Lean formalisation)

This is EXACTLY the name collision problem.md warns about. `Mathlib.Combinatorics.Pigeonhole`-adjacent / any `ErdosSzekeres` name in Lean refers to the *monotone-subsequence* result, NOT the convex-polygon conjecture ES(n)=2^{n-2}+1 that this run targets. The two share a name and neither implies the other.

Consequences:
- A Lean goal file must NOT import this as if it were the convex-polygon fact. The formal statement of ES(n) (general position, convex position, the worst-case quantifier order) must be written from scratch.
- This file is still a useful *model*: it shows the idiomatic way Lean states an Erdős–Szekeres-style extremal theorem (finset subset, cardinality bound, monotonicity predicate) — a template for how to state convex position.
- The actual cups-and-caps geometry argument is NOT in this file. That is a separate formalisation effort. (LeanPool has an `ErdosTuzaValtr/Main/CapCup.lean` — a cup/cap dichotomy, but for the monotone-subsequence setting, not the planar convex-polygon one; see that summary.)

```claim
id: mathlib-esz-is-monotone-subsequence
statement: In Lean/Mathlib, the theorem named `erdos_szekeres` (mathlib-archive/wiedijk_100_theorems/ascending_descending_sequences.lean, Theorem 73 of the 100-Theorems list) is the monotone-subsequence result: (r−1)(s−1)+1, i.e. r·s < n forces a strictly-monotone- or strictly-antitone-on-a-finset subsequence of length > r resp. > s. It is NOT the convex-polygon conjecture ES(n)=2^{n-2}+1.
hypotheses: f : fin n → α injective, α a linear order, r*s < n.
holds-here: yes
status: checked (directly read the Mathlib source file this run — the file's own content confirms the monotone-subsequence statement)
bearing: GOAL 5 — this run's Lean formalisation of ES(n) must be written from scratch and must not cite this file as the convex-polygon result.
anchor: research/summaries/mathlib-erdos-szekeres-monotone-subsequence.md
```
