# Yolcu–Aaronson–Heule 2023 — automated approach via string rewriting

<!-- src: Yolcu, Aaronson & Heule, "An Automated Approach to the Collatz Conjecture", arXiv:2105.14697, J. Automated Reasoning 2023 -->

Full text: `research/sources/yolcu-aaronson-heule-2023-automated-collatz.full.md`

## What the source establishes

An automated-deduction attack on Collatz via **termination of string rewriting
systems** (SRS). This is a *failed approach* source: it establishes
equivalences and impossibility results for the method, not the conjecture.

**Main results:**
1. **Equivalence theorem:** a rewriting system simulating the Collatz function
   on strings corresponding to **mixed binary-ternary representations** of
   positive integers is constructed, and termination of that rewriting system
   is **equivalent** to the Collatz conjecture. This is a reformulation, not a
   proof — it shows the conjecture can be attacked as a termination problem.
2. **Impossibility result:** a previously studied rewriting system (Zantema)
   that simulates Collatz using **unary representations** admits **no
   termination proof via natural matrix interpretations**, even with the
   dependency-pair transformation. So that particular automated route is
   closed.
3. **Automated weakenings proved:** a minimal termination prover using
   natural/arctic matrix interpretations finds automated proofs of
   **nontrivial weakenings** of the Collatz conjecture. (The full text was
   examined; the specific weakened statements and bounds are in the paper's
   later sections — the standard tools AProVE/Matchbox could not prove some
   of these, requiring arctic matrix interpretations.)
4. **SAT-solver observation:** the phase-saving heuristic used by default in
   modern SAT solvers degrades CDCL performance on formulas encoding the
   existence of matrix interpretations; negative branching improves it. (A
   practical note for this run's own SAT usage.)

## What it implies for this run

This is the computational/automated-deduction flank of the literature: Collatz
⇔ termination of an SRS over mixed binary-ternary strings; natural matrix
interpretations provably cannot do Zantema's unary system; arctic
interpretations can prove weakenings. The impossibility result is the record
of a closed direction — do not propose natural matrix interpretations for
Collatz termination again.

## Claims

```claim
id: yah-rewriting-equivalence
statement: There is a string rewriting system over mixed binary-ternary representations of positive integers whose termination is equivalent to the Collatz conjecture (Yolcu–Aaronson–Heule 2023).
hypotheses: the specific SRS constructed in the paper
holds-here: yes
status: proved
bearing: reformulates Collatz as a termination problem; the automated-deduction flank
anchor: research/summaries/yolcu-aaronson-heule-2023-automated-collatz.md
```

```claim
id: yah-no-natural-matrix-interp
statement: Zantema's unary-representation rewriting system simulating the Collatz function admits no termination proof via natural matrix interpretations, even with the dependency-pair transformation (Yolcu–Aaronson–Heule 2023).
hypotheses: natural matrix interpretations, unary representation, with/without dependency pairs
holds-here: yes — closes a specific automated route
status: proved
bearing: closed direction: do not propose natural matrix interpretations for Collatz termination
anchor: research/summaries/yolcu-aaronson-heule-2023-automated-collatz.md
```

```claim
id: yah-weakenings-automated
statement: A minimal termination prover using natural/arctic matrix interpretations automatically proves nontrivial weakenings of the Collatz conjecture (Yolcu–Aaronson–Heule 2023); the full Collatz conjecture is not proved.
hypotheses: the specific weakened variants defined in the paper
holds-here: yes — as evidence of what automated methods can reach
status: asserted
bearing: marks the frontier of the automated-deduction approach; the conjecture itself remains open
anchor: research/summaries/yolcu-aaronson-heule-2023-automated-collatz.md
```
