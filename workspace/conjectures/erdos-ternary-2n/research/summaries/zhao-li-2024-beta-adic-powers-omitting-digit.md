<!-- source: https://arxiv.org/pdf/2405.06220 | Zhao & Li, "On β-adic expansions of powers of algebraic integers omitting a digit" (2024) -->

# Zhao & Li, "On β-adic expansions of powers of algebraic integers omitting a digit"

Source: arXiv:2405.06220 (May 2024). Full text: `research/sources/zhao-li-2024-beta-adic-powers-omitting-digit.full.md`.

## What it establishes

Let `α, β` be relatively prime algebraic integers in a number field `K`. The paper bounds the number of `n ∈ {1,…,N}` for which the β-adic expansion of `α^n` **omits a given digit**, when all prime-ideal factors of `(β)` are unramified with integer-prime norms.

**Theorem 1.8 / abstract version.** Under those hypotheses,
```
#{ n ≤ N : β-adic expansion of α^n omits a fixed digit } ≤ C1 · N^σ(β),
σ(β) = log(|N(β)| − 1) / log|N(β)|,
```
with `C1` depending only on `β`.

**Corollary 1.9 (the Erdős-relevant case).** For coprime rational integers `p, q` and any digit `b ∈ {0,…,q−1}`:
```
M_b(p, q, N) := #{ n ≤ N : base-q expansion of p^n omits the digit b } ≤ C · N^(log(q−1)/log q).
```
For the Erdős case `p = 2, q = 3, b = 2`: `(log 2)/(log 3) ≈ 0.63092`, so
```
#{ n ≤ N : (2^n)_3 omits the digit 2 } ≤ C · N^(0.63092).
```
This is **exactly the Narkiewicz (1980) bound**, re-derived here by a modern, elementary number-field method (canonical number systems, p-adic valuation, subsequence splitting via Lemma 3.2–3.4). The exponent `log 2/log 3` is the same as Narkiewicz's.

## Method (why it works)

`(β) = p_1^{e_1}…p_h^{e_h}` unramified with `N(p_i)=q_i` integer primes. The sequence `α^n` splits into subsequences along which `G_l(x) = α^l (α^u)^x` behaves p-adically like a polynomial, and for each digit-omission there is a quantitative bound on how many `x` can keep `G_l(x)` in the omitted-digit residue class. The canonical-number-system (CNS) hypothesis guarantees a clean digit expansion. The exponent `σ(β)` comes from `log(|N(β)|−1)/log|N(β)|`.

## Relevance to this run

- **Fills the library's Narkiewicz gap with a primary, modern, elementary source.** The recalled `N(X) ≤ 1.62·X^(log_3 2)` from CONTEXT.md is corroborated in form: exponent `log 2/log 3 ≈ 0.63092` (this paper's constant `C` is not stated as 1.62; the exact constant from Narkiewicz's original should be attributed separately). The bound is `# {n ≤ N : (2^n)_3 omits 2} ≤ C·N^(log_3 2)`, sublinear in `N` but **not** tending to a constant — it is consistent with (indeed, allows) the belief that the count grows slowly rather than being finite. This is the "counting obstruction" at the *upper-counting* level: these bounds do **not** prove finiteness of digit-omitting `n`, which is why Erdős's conjecture (finiteness = `{0,2,8}`) remains open even given this bound.
- The exponent `log 2/log 3` is exactly the Hausdorff dimension of the digit-`{0,1}` Cantor set — the count bound reflects that dimension. This ties the counting line to the fractal/dimension line.
- Confirms the three witnesses are not contradicted: `2^0, 2^2, 2^8` are allowed as the small-`n` cases.

## Status

Sourced (arXiv preprint 2024, and the same group's JNT-adjacent line; peer-review status of this exact preprint unverified). The Corollary 1.9 statement with `σ = log(q−1)/log q` and the p=2,q=3,b=2 case `N^(0.63092)` are quotable. This **corroborates** the recalled Narkiewicz bound but is a distinct, elementary derivation; attribute the `1.62` constant to Narkiewicz's original, not this paper.

```claim
id: ZHAO-LI-NARKIEWICZ-BOUND
statement: For coprime rational p, q and digit b in {0..q-1}, the number of
  n <= N whose base-q expansion of p^n omits b is <= C · N^(log(q-1)/log q).
  For p=2, q=3, b=2: #{ n <= N : (2^n)_3 omits 2 } <= C · N^(0.63092).
hypotheses: (β) has only unramified prime-ideal factors with integer-prime
  norms; α coprime to β. Holds for p=2, q=3 in Q.
holds-here: yes — this is the counting bound on digit-2-free exponents; exponent
  log_3 2 = 0.63092 matches Narkiewicz.
status: sourced (arXiv:2405.06220, 2024); constant C not stated as 1.62 — that
  constant belongs to Narkiewicz's original bound.
bearing: sublinear-in-N upper bound on how many n omit the digit 2; does NOT
  prove finiteness (count may still grow slowly), which is why Erdős's
  conjecture stays open. Exponent equals dim of digit-{0,1} Cantor set.
anchor: research/summaries/zhao-li-2024-beta-adic-powers-omitting-digit.md
answers: narkiewicz-count-primary (fill this by also getting Narkiewicz's exact 1.62)
```
