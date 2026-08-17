# Speissegger — "Limit cycles of planar vector fields: Hilbert's 16th problem and o-minimality" (arXiv:1804.03585, 2018; Oberwolfach Snapshots in Modern Mathematics)

Full body: `research/sources/speissegger-hilbert16-ominimality-body.full.md` (ar5iv, 27KB).
Primary URL: https://arxiv.org/abs/1804.03585

## What it is

Lectures/survey by Patrick Speissegger (McMaster) linking the second part of
Hilbert's 16th problem to **o-minimality** — a model-theoretic tameness
framework. This is a distinct method the library was thin on (the DRR/cyclicicty
and Abelian-integral routes dominated). It gives a rigorous statement of
*Roussarie's finite cyclicity conjecture* and a clean model-theoretic criterion
that would prove it.

## The o-minimal route to uniform finiteness (the load-bearing idea)

For each degree d, 𝒮_d = all polynomial planar fields of degree d, F_μ with
coefficient tuple μ. Around a limit periodic set / polycycle Γ of F_μ, the
return map r_{μ'}(x) may be ill-defined for nearby μ' (bifurcation). But the
**parametric transition maps** f_{μ',i}, g_{μ,i} (the local pieces whose
composition is the return map) ARE well-defined for all μ' in a neighbourhood U
of μ. A limit cycle of F_{μ'} near Γ corresponds to an isolated point x₁ of the
set

  A_{μ'} = { x₁ ∈ V : ∃x₂,…,x_k, y₁,…,y_k with y_i = g_{μ',i}(x_i),
            x_{i+1} = f_{μ',i}(y_i) }.

This set is **definable** from a language ℒ_trans that adds the transition maps
to the ordered-ring language. The key structural fact:

**Uniform finiteness principle (o-minimality).** If 𝒮 is o-minimal and
A ⊆ ℝ^{m+n} is definable with each fiber A_μ finite, then there is an N with
each A_μ having at most N elements.

So Roussarie's finite-cyclicity conjecture for degree d follows from the
**o-minimality conjecture for ℒ_trans**: the ℒ_trans-structure is o-minimal.

## What is established vs open

- **O-minimality conjecture for ℒ_trans: OPEN.**
- **Proved special case (Kaiser–Rolin–Speissegger, J. Reine Angew. Math. 636
  (2009) 1–45):** for the class 𝒩ℛℋ_d of fields whose singularities are all
  *non-resonant hyperbolic*, the corresponding sublanguage ℒ_nrhyp is
  o-minimal; hence **Roussarie's conjecture holds for 𝒩ℛℋ_d**. This class is
  "very small", not even generic.
- In this class every limit periodic set is genuinely a polycycle.
- Open direction (at the time): the class ℋ_d of fields with only hyperbolic
  (including resonant) singularities, which IS generic. Work in progress
  (Galal, Kaiser, Rolin, Servi, Speissegger).

## Why this matters for THIS run (analyticity / Test 1)

This is exactly the shape of argument that a valid H16 finiteness proof needs,
and it is the direct *opposite* of what the Pedregal variational claim provides.
The o-minimality of the transition maps at hyperbolic singularities is a
**quasianalytic / asymptotic-description** fact (Kaiser–Rolin–Speissegger build
on Rolin–Speissegger–Wilkie quasianalytic classes and van den Dries–Speissegger
generalised power series). Tamed asymptotics of the return map IS the analytic
input. An o-minimality proof does not discard analyticity — it encodes it.
Compare `h16-pedregal-variational-claim-unrefereed`, whose argument counts
critical points of a functional via Bezout/Harnack/divergence-curve and never
touches the (analytic) return map — a prima-facie Test-1 (smooth-test) failure.
The o-minimal framing shows concretely where a uniform bound must come from:
definability of the *transition maps* in a tame structure, which for hyperbolic
points is the quasianalytic asymptotic behavior.

Also relevant to `drr-...`: Roussarie's conjecture is stated precisely here
(neighbourhood U of μ, V of Γ, uniform N over μ'∈U), matching the DRR-program
frame and separating it cleanly from Écalle–Ilyashenko individual finiteness.

## Provence / evidence
Peer-visible survey (Oberwolfach Snapshots in Modern Mathematics; also on UBC /
arXiv). The Kaiser–Rolin–Speissegger theorem it cites is refereed (Crelle).
Claim recorded: `h16-ominimality-route-rous sarie`. Evidence class:
sourced-observed / sourced by the survey's own statement; not independently
re-derived here.

## For the requests ledger
This fills part of the "what other methods exist for uniform finiteness" angle.
The o-minimality conjecture for the full ℒ_trans is an open route, not in the
DRR-specific requests. Note for the run: an o-minimality result covering a
*wider generic* class (ℋ_d, hyperbolic including resonant) would be a genuine
independent route to a big uniform-finiteness statement and is the concrete next
frontier the survey names.
