# Coven & Nitecki, "On the Genesis of Symbolic Dynamics as We Know It" (arXiv:math/0611322) — verdict

Source: https://arxiv.org/pdf/math/0611322
Full text: [[coven-nitecki-genesis-symbolic-dynamics.full]]

## What this source is

A **historical** paper tracing the beginnings of symbolic dynamics: it argues
that neither Hadamard's 1898 paper nor the Morse–Hedlund papers of 1938/1940
present the modern abstract point of view, and places the start in Hedlund's
1944 "Sturmian minimal sets", supported by a 1941 Hedlund–Morse letter. Its
primary content is a reading of the history (Hadamard geodesic coding, Morse &
Hedlund's shift/Sturmian trajectory work, the topology programme).

## What it establishes that bears on PE1006

Only one thing, and it is historical rather than load-bearing:

- It reproduces the original **Morse–Hedlund 1940 definition** of Sturmian
  trajectories: two-symbol trajectories in which any two maximal blocks of
  consecutive appearances of a symbol differ in length by at most one — i.e.
  the **balance condition** that is one of the three equivalent modern
  definitions of a Sturmian word. It motivates the name via the Sturm
  Separation Theorem.

This is a primary/historical anchor for the *definition* underlying the run's
`governing-sturmian` and `governing-factor-complexity` claims.

## What it does NOT establish

- It does **not** state the factor-complexity theorem p(k) = k+1 for Sturmian
  words (that stays anchored to Perrin–Restivo / Berstel DLT'95 / Lothaire C2),
  nor any mechanical-word/floor-sum fact, nor anything about Ψ(k), decimal
  readings, or the modulus.

## Verdict

**Marginal help; does not change the run.** It is a historical source and
adds no theorem the run lacks. The balance-condition definition it reproduces
is already established in-container (brute oracle k=1..20 factor count k+1
is the *consequence*, not the definition). Keep as a citation of record for
the Sturmian definition; do not treat it as evidence for any computation.

## Claims anchored here

None new. Corroborates the governing-sturmian claim's underlying definition
(Sturmian = balanced + non-periodic) but adds no statement.
