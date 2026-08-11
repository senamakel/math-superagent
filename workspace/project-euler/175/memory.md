# Working memory

## Problem

Project Euler-style problem (presented in `/workspace/problem.html`; this setup
labels the objective "problem 175").

- $f(0)=1$; for $n\ge 1$, $f(n)$ = number of ways to write $n$ as a sum of
  powers of $2$ with no power occurring more than twice.
- Worked facts (oracle, from the statement, unverified independently so far):
  - $f(10)=5$ with the five listed decompositions.
  - Smallest $n$ with $f(n)/f(n-1)=13/17$ is $241$; binary $11110001$;
    Shortened Binary Expansion (run lengths from MSB) is `4,3,1`.
- Target: SBE of the smallest $n$ with
  $f(n)/f(n-1)=123456789/987654321$, output as comma-separated integers, no
  whitespace.

## Established results

- Phase 1 (extraction) complete: verbatim statement written to
  `/workspace/problem_statement.md` (verified against raw HTML of
  `/workspace/problem.html`).
- Output format, verbatim: "Give your answer as comma separated integers,
  without any whitespaces." (e.g., `4,3,1` for the sample n=241).

## Failed approaches

(none)

## Open questions

- Method to compute the smallest $n$ (do not iterate to the bound; the SBE is
  expected to be short — a recursive/CF-like construction of the ratio
  $f(n)/f(n-1)$ is the likely route). Not to be pursued until the oracle cases
  are reproduced.

Source document: `/workspace/problem.html` (local, no external sources used).