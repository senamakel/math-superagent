# Hieronymi, Ma, Oei, Schaeffer, Schulz & Shallit — Decidability of Sturmian words (LMCS 2024)

<!-- source: https://arxiv.org/pdf/2102.08207 | converted from PDF -->

Full text: `research/sources/hieronymi-decidability-sturmian-words-ar5iv.full.md`
(the 100KB PDF converted lossily; the abstract and statements below are the
reliable parts).

## What it claims

The paper proves that the **first-order theory of Sturmian words over Presburger
arithmetic is decidable**. Using a general adder recognizing addition in
**Ostrowski numeration systems** (Baranwal–Schaeffer–Shallit), it shows that the
first-order expansions of Presburger arithmetic by a single Sturmian word are
uniformly ω-automatic, and deduces the decidability of the theory of the class
of such structures. An implementation called **Pecan** automatically reproves
classical theorems about Sturmian words (e.g. balancedness, subword complexity)
in seconds and obtains new results about antisquares and antipalindromes in
characteristic Sturmian words.

## Key statements it carries

- Fact 1.1 (Hieronymi 2016): For a quadratic irrational α, the theory FO(R_α) is
  decidable.
- Fact 2.6–2.9: α-Ostrowski representation of natural numbers (unique
  representation, comparing via continued fractions) — the numeration system at
  the heart of directive 1's lag-sum recursion and of the mechanical-word /
  rotation structure.
- The ω-automatic/decision-procedure machinery (Pecan).

## Why it matters here (adjacent-problem / computational-attacks angle)

- It anchors **Ostrowski numeration** — the continued-fraction-based positional
  system in which the Fibonacci word's digit structure is automatic — which is
  the same number-system structure behind the solver's Euclidean/floor-sum
  reduction (directive 1's `(a·d mod N)` lag sums are an Ostrowski-style
  object).
- It is a legitimate *computational* approach to Sturmian-word properties, but
  it does **not** compute Ψ(k) itself; PE1006's Ψ(10^18) is a specific modular
  sum that needs the universal-Euclidean O(log) evaluation, not a decider.
- Also documents that the Fibonacci word is **Fibonacci-automatic** (an
  Ostrowski/Zeckendorf consequence), and that the bibliography's claimed Sturmian
  theory is fully standard.

Status: sourced; used as the adjacent computational/numeration-system reference,
not as the solving method. Its large full text is on disk but the claim-relevant
content is reproduced above.
