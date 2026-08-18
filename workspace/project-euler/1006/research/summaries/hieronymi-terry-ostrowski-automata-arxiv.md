# Hieronymi–Terry — Ostrowski numeration systems, addition and finite automata (arXiv:1407.7000; Notre Dame J. Formal Logic)

<!-- source: https://arxiv.org/pdf/1407.7000 (PDF) and https://ar5iv.labs.arxiv.org/html/1407.7000 (HTML) | read 2026-08-19 -->

Full text: `[[hieronymi-terry-ostrowski-automata-arxiv.full]]` (ar5iv HTML, 70 KB) and `[[ostrowski-numeration-addition-finite-automata.pdf.full]]` (PDF conversion) — the same paper in two formats. `research/sources/hieronymi-terry-ostrowski-numeration-addition.full.md` is the publisher (Notre Dame J. Formal Logic) landing page only — use the arXiv files.

## What it establishes

An elementary **three-pass algorithm for addition in Ostrowski numeration systems** (Prop 2.1–Cor 2.8: Algorithms 1–3 normalize the digit representation of M+N so it satisfies the Ostrowski conditions), and the automata-theoretic consequences:

- **Theorem A**: when α is quadratic, addition in the Ostrowski numeration system based on α is **recognizable by a finite automaton**.
- **Theorem B** (Def 3.1–3.9, Thm 3.10): X ⊆ ℕⁿ is definable in (ℕ, +, V_α) — where V_α(x) = the smallest convergent denominator of α appearing with non-zero coefficient in the Ostrowski representation of x — iff the set of Ostrowski representations of elements of X is recognizable by a finite automaton. **Decidability of the theory of (ℕ,+,V_α) follows.**
- Lemma 3.8: the parity structure of the Ostrowski digits of n (all even-index digits ≤ 1 / odd digits = 0, etc.) characterizes membership in the even/odd sets U_e, U_o.

## Why it matters here

- **For the Fibonacci word**: α = 1/φ² is quadratic, so addition in the Fibonacci/Ostrowski numeration is finite-automaton-recognizable — the machinery behind the run's *automatic-digit-DP* idea. **But** (as the run already established via Cobham–Bès–Frougny, claim `cobham-bes-frougny-multiplicatively-independent-conversion`): automata over the Fibonacci numeration cannot convert to the base-10 weights Ψ(k) needs — 10 and φ are multiplicatively independent. So this paper supplies the *Ostrowski-side* recognizability and nothing on the decimal side: it does not unlock a base-10 automaton for Ψ.
- Corroborates the Ostrowski-representation machinery the run's `ostrowski-prefix-decomposition-characteristic` and the division-property/Fici factorization axis rest on.
- **Does NOT give Ψ(k)**: no decimal weighting, no squares, no joint-intercept aggregation. It is the numeration-system/automata reference, not a second-moment engine.

## Claims anchored here

Corroborates `ostrowski-prefix-decomposition-characteristic` and the Cobham-based refutation `pe1006-zeckendorf-automatic-digit-dp` (Fibonacci-side addition is automatic; the decimal-weight conversion is not). No new claim block.
