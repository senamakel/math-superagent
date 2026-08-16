# Stephan, "Aperiodicity and subword complexity in the binary expansion of powers of three"

Source: arXiv:2607.14774 (2026). Full text: [[stephan-2026-aperiodicity-subword-complexity-binary-3n.full]].

## What it establishes

Two results on the *binary* digits of `3^m` (the mirror of this run's `2^n`-in-ternary).

**Theorem A.** For every fixed period `p`, the number of positions at which the binary expansion of `3^m` breaks `p`-periodicity grows like `B_p(3^m) = Θ(log m / log log m)`, so `B_p(3^m) → ∞`; equivalently, no window of the expansion deeper than a fixed power of `log m` is `p`-periodic. Method: effective Baker–Wüstholz lower bounds on linear forms in logarithms (periodic-run estimate via a periodic remainder identity, Lemma 2.3, plus non-degeneracy, Lemma 2.5).

**Theorem B.** The finite binary word of the low-order digits of `3^m` meets the Morse–Hedlund floor: its subword complexity satisfies `p_{3^m}(n) ≥ n+1` for every length `n`, once `m` is large enough. Method: a quantitative finite form of Morse–Hedlund (Lemma 4.1), in the spirit of Carpi–de Luca.

## Implication for this problem

- This is the **dual** of the Erdős problem: the binary digits of `3^m` vs. the ternary digits of `2^n`. It shows powers of one base carry proven aperiodicity/complexity in another base's digits — structural support that digit sequences of `2^n` are "complex", but the paper proves nothing about the ternary digit-avoidance of `2^n` itself.
- `holds-here: no` — the object studied is `3^m` mod 2-adic structure, not `2^n` mod 3. It does not reach the middle ternary digits of `2^n` that this run needs.
- The Morse–Hedlund/aperiodicity machinery (Theorem B) is suggestive for a symbolic-invariant attack — if the ternary digit string of `2^n` were eventually periodic in some statistic that `S` violates, aperiodicity would force the obstruction — but no such bridge is present in this source.

## Status

Sourced; full text held. Structural analogy/background for the symbolic-invariant and complexity lines, not a tool that reaches the Erdős obstruction. Consistent with the dispersion literature (`STEWART-DIGITAL-SUM-POWERS`, `DIMITROV-HOWE-26-ONES`); no contradiction with recalled memory.

```claim
id: STEPHAN-APERIODICITY-SUBWORD
statement: For fixed period p, the binary expansion of 3^m breaks p-periodicity at order B_p(3^m) = Θ(log m/log log m) → ∞ (no deeper-than-poly-log window is p-periodic); and for large m the low-order binary digit word of 3^m has subword complexity ≥ n+1 (Morse-Hedlund floor).
hypotheses: m large; p fixed; 3^m written in base 2.
holds-here: no
status: asserted
bearing: the dual (binary of 3^m) of this run's problem; proves aperiodicity/complexity of powers-of-one-base in another base's digits but says nothing about the ternary digit-2-avoidance of 2^n or its middle digits.
anchor: research/summaries/stephan-2026-aperiodicity-subword-complexity-binary-3n.md
```
