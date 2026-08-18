# Masáková–Pelantová: Powers of factors and recurrence function characterizing Sturmian words (arXiv:0809.0603)

<!-- source: https://ar5iv.labs.arxiv.org/html/0809.0603 | downloaded 2026-08-19 -->

Full text: `research/sources/masakova-pelantova-powers-factors-recurrence-sturmian-ar5iv.full.md`
(also: https://arxiv.org/abs/0809.0603)

## What it establishes

Z. Masáková and E. Pelantová relate the index of an infinite aperiodic word to its recurrence
function to give another characterization of Sturmian words, and give a new proof of the theorem
describing the index of a Sturmian word in terms of the continued fraction expansion of its slope
(originally proved independently by Carpi–de Luca and Damanik–Lenz).

**Theorem 1.1:** A uniformly recurrent infinite word u is Sturmian iff there exist infinitely many
factors w of u such that R(|w|) = |w| · ind(w) + 1, where R is the recurrence function and ind(w)
the maximal rational exponent of a power of w occurring in u.

The paper opens with the standard historical attribution: Sturmian words first appeared in
Morse–Hedlund 1938 [17], and Morse–Hedlund [18] already characterized them via the balance
property. The Fibonacci word is noted as the most prominent Sturmian word.

## Why it matters here

- The **recurrence function** R(n) of the Fibonacci word (minimal window length containing every
  factor of length n) is the object behind the run's first-occurrence-window picture
  (`fibonacci-first-occurrence-window-bound`, Cassaigne's Φ+1 bound): this paper is the clean
  modern reference for R(n) of Sturmian words and its continued-fraction description.
- It also confirms the Morse–Hedlund attribution chain for Sturmian words and the balance property
  — the historical anchor for the whole Sturmian factor-complexity framework.
- It does **not** give the decimal second-moment formula; it fixes the window/recurrence structure.

## Claims anchored here

Corroborates `fibonacci-first-occurrence-window-bound` and the Sturmian-factor framework. No new
claim block needed.
