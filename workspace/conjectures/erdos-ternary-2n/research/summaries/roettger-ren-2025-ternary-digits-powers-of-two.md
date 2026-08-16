# Roettger & Ren, "Ternary Digits of Powers of Two" (2025)

Source: arXiv:2511.03861 (5 Nov 2025), math.NT. Full text:
`research/sources/roettger-ren-2025-ternary-digits-powers-of-two.html.full.md`
(abstract page also held at `...ternary-digits-powers-of-two.full.md`).

## What it is

A **computational-evidence + reformulation** paper, not a proof of Erdős. It lays out
a tower of conjectures from strongest to weakest and gives numerical evidence
(n ≤ 10^6) for the strongest, none of which is settled.

## The conjecture tower (Section 1) — useful for locating Erdős in the landscape

For `f_d(n) = c_d(n)/l(n)`, the frequency of digit `d ∈ {0,1,2}` in the ternary
expansion of `2^n` (length `l(n) = ⌈n·log_3 2⌉`):

- **C1 (strongest):** each `f_d(n) → 1/3` as `n → ∞` (uniform distribution in the limit).
- **C2:** each `f_d(n)` has a nonzero limit.
- **C3:** each `f_d(n)` is bounded below by a nonzero constant for large `n`.
- **C4 (Erdős):** every `2^n`, `n > 8`, has a ternary digit 2.

So Erdős's conjecture is the *weakest* in a natural hierarchy; Terry Tao's remark
quoted that even C4 is "still a fair distance beyond what one can do with current
technology". Lagarias [7] is cited as the main results reference.

**Lemma 1 (provable):** if C1 holds then the *aggregate* frequency
`F_d(N) = (Σ_n c_d(n))/(Σ_n l(n)) → 1/3`. (Weighted average argument.) So Eq. (1),
the aggregate limit, is a strictly weaker conjecture than C1.

## Computational evidence (Section 2, verified range n ≤ 10^6)

- Aggregate digit frequencies `F_d(N)` and length-2 and length-3 string frequencies,
  plus variance/standard-deviation and non-aggregate digit tallies (consecutive exponents).
- Reports results "supporting uniform distribution in the limit" over `1 ≤ n ≤ 10^6`
  (2h51m47s of compute). **This is numerical evidence for C1, not a proof; it says
  nothing about a specific counterexample to C4.**

## Theorems proved in the paper (Sections 3–4) — conditional, background

These are the only *proved* statements, and none reaches Erdős:

- **Theorem 1 (Benford's Law for ternary digits):** proved; leading-digit behaviour.
- **Theorem 2 (Average count in leading digits):** proved.
- **Theorem 3 (Uniform distribution of frequency in leading digits):** proved from
  uniform distribution mod 1 of `n·log_3 2` — but only *on average over n*,
  again not per-n.
- **Theorem 4 (Baker 1975, very special case) + Corollary 1:** a linear-forms-in-
  logarithms consequence. Like Benford, applies to leading digits / averages, not to a
  single `2^n`.

The paper is explicit that Benford's Law and Baker's Theorem "neither prove nor
disprove" C1–C4.

## Normality of log_3(2) (Section 5)

`α = log_3(2) ≈ 0.63093`; unknown whether normal to base 3. Computational evidence
from the first 10^6 ternary digits of `α` supports it. **Non-connection note:** the
paper gives a heuristic that conjectures about the ternary digits of `α` do NOT seem
to imply conjectures about the ternary digits of `2^n` (and vice versa) — despite
`α` appearing in the length formula.

## Relevance to this run

- Gives the **standard conjecture hierarchy** C1–C4, fixing where Erdős (C4) sits
  relative to uniform-distribution (C1) and Benford/Baker results. Good for ROOT's
  "state the structure" and for the CONTEXT contradiction note that uniform/aggregate
  results do not reach a per-`n` counterexample.
- **Verification bound here: n ≤ 10^6** — far weaker than Saye's `2·3^45 ≈ 5.9×10^21`.
  This run's own oracle bound is `[1,1000]` (finite_check) and `k ≤ 26` (sieve);
  keep all three separate.
- Section 6 connects to **Selfridge's integer-complexity conjecture** — a sibling
  open problem (adds an adjacent-problem angle the library lacked).

```claim
id: ROETTGER-REN-CONJECTURE-TOWER
statement: The ternary-digit uniform-distribution statements for 2^n form the
  tower C1 (f_d(n)->1/3) ⊃ C2 (nonzero limit) ⊃ C3 (nonzero lower bound) ⊃ C4
  (Erdős: n>8 => a digit 2). Lemma 1: C1 => aggregate F_d(N)->1/3. Benford's Law
  and Baker's Theorem apply only to leading digits / averages and neither prove
  nor disprove C1-C4.
hypotheses: none beyond the definitions; Section 3-4 theorems rely on
  equidistribution mod 1 of n·log_3 2 and Baker's theorem.
holds-here: yes (definitions and tower are standard; the tower is a reformulation
  that locates Erdős as the weakest of four uniform-distribution conjectures).
status: asserted-by-source (theorems proved in the paper; computational evidence
  is numerical, not a proof).
bearing: background — clarifies that per-n results (needed for C4) are strictly
  stronger than the aggregate/Benford/Baker/equidistribution results, all of which
  are average or leading-digit statements. Consonant with the density trap in
  GOAL.md.
anchor: research/sources/roettger-ren-2025-ternary-digits-powers-of-two.html.full.md
falsifies: any attempt to derive Erdős (C4) from Benford's Law, Baker's Theorem,
  or aggregate digit-frequency results — the paper makes the non-implication
  explicit.
```
