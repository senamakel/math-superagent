> **Name-hygiene marker — a DIFFERENT theorem with the same name.**

# Wikipedia — Erdős–Szekeres theorem (monotone subsequence)

> **Source:** `https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Szekeres_theorem` (full text at `research/sources/wikipedia-erdos-szekeres-theorem.full.md`). **Encyclopedic context only.**

## What it establishes and why it is NOT the ES conjecture

The **Erdős–Szekeres theorem** (in the formulation Wikipedia's page is about) is the
**monotone-subsequence** result: any sequence of $(r-1)(s-1)+1$ distinct reals
contains a monotonically increasing subsequence of length $r$ or a monotonically
decreasing one of length $s$. It appeared in the *same 1935 paper* as the Happy
Ending problem, and is proved by pigeonhole / Dilworth / Robinson–Schensted.

**This is a different theorem from the convex-polygon Erdős–Szekeres conjecture
($\mathrm{ES}(n)=2^{n-2}+1$) that this run attacks.** Both share the names
"Erdős–Szekeres"; the monotone-subsequence one is the one already in Mathlib
(`Mathlib`'s ErdosSzekeres file), which GOAL warns must not be mistaken for
novelty. The geometric/order-type form is the cups-and-caps / monotone-path
statement the run actually works over (see [[cups-caps-is-N3-monotone-path]]).

## Bearing

A hard name-hygiene boundary. Any Lean formalization or theorem statement this run
writes must say *planar convex-position* explicitly, or it will be read as the
(already-in-Mathlib) monotone-subsequence theorem. This page is a fast illustration
of the boundary but contributes nothing to the mathematics.

```claim
id: wiki-es-monotone-subsequence
statement: (encyclopedic) The Erdos-Szekeres theorem in its sequence form: any (r-1)(s-1)+1 distinct reals contain an increasing length-r or decreasing length-s subsequence. This is the monotone-subsequence theorem, DISTINCT from the convex-polygon conjecture ES(n)=2^{n-2}+1; the former is already in Mathlib.
hypotheses: none beyond distinct real numbers.
holds-here: N/A — a name-hygiene marker, not a tool for the ES(n) conjecture.
status: catalogued (encyclopedic; well-known result, primary elsewhere).
bearing: keeps the run from claiming the Mathlib monotone-subsequence theorem as novelty; the run's formal statement must say planar convex-position explicitly.
anchor: research/summaries/wikipedia-erdos-szekeres-theorem.md
```
