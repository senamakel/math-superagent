> **Encyclopedic context — the problem's standing and prizes.**

# Erdős Problem #107 (erdosproblems.com)

> **Source:** `https://www.erdosproblems.com/107` (full text at `research/sources/erdosproblems-107-happy-ending-entry.full.md`). **Encyclopedic context only.**

## What it establishes

- **Open problem, no claimed solution.** The site ("Falsifiable: open, but could
  be disproved with a finite counterexample") lists ES(n)=2^{n-2}+1 as **open with
  zero claimed proofs**. This is current (page last edited 11 Apr 2026).
- **The prize.** Erdős's own $500 for a proof, only $100 for a disproof; Graham
  adds $1000 for a proof. (The Erdős-prize amount is a fact about the problem's
  standing, not its mathematics — noted in problem.md.)
- **Bound recap** (consistent with primaries): $2^{n-2}+1 \le f(n) \le
  \binom{2n-4}{n-2}+1$; several improvements all of form $4^{(1+o(1))n}$; Suk
  $2^{(1+o(1))n}$; current best HMPT $2^{n+O(\sqrt{n\log n})}$.
- **Formalized statement exists** (DeepMind formal-conjectures #107 `.lean`),
  relevant to GOAL criterion 7 — the statement is already formalized in Lean by
  an external project.

## Bearing

Confirms (a) the problem remains open with no claimed solution, (b) the prize
structure, and (c) that a Lean formal statement of f(n)=2^{n-2}+1 already exists
externally (so the run's own Lean file must improve on / differ from it — e.g. by
formalizing supporting lemmas rather than only the statement). Context only; every
mathematical statement here is primary-backed in the library.

```claim
id: erdosproblems-107-open
statement: (encyclopedic) Erdős-Szekeres ES(n)=2^{n-2}+1 is open with no claimed solution (as of Apr 2026); Erdős offers $500 (proof) / $100 (disproof), Graham $1000 (proof); a Lean formal statement of the conjecture exists in google-deepmind/formal-conjectures #107.
hypotheses: none.
holds-here: N/A — context on the problem's standing and its external formalisation.
status: catalogued (encyclopedic; open-status page).
bearing: the run's Lean arm can build on the external formalisation of the statement rather than restate it from scratch; confirms the prize/standing facts.
anchor: research/summaries/erdosproblems-107-happy-ending-entry.md
```
