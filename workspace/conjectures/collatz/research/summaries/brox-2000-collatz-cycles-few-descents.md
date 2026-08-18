# Brox 2000 — Collatz cycles with few descents

<!-- source: https://matwbn.icm.edu.pl/ksiazki/aa/aa92/aa9229.pdf (Acta Arith. 92(2) (2000), 181–188). Full text held: ICM scan with text layer, 14650 bytes. -->

**T. Brox, 2000. Primary text held.** (This replaces the earlier placeholder
failure record — the ICM scan succeeded.)

## What it establishes

Work in terms of T₁ on odd integers, defined by 2^{k(x)}T₁(x) = 3x+1 (x odd),
k(x) ≥ 1 the 2-adic multiplicity of 3x+1. A "Collatz cycle" Γ = (x₁,…,x_n) is
a cycle of T₁ (equivalently the odd elements of a 3x+1 cycle); k = Σk(x) is
the period of the corresponding 3x+1 cycle; x is **descending** if k(x) ≥ 2;
δ(Γ) = number of descending elements.

- **Theorem 1.1**: the number of Collatz cycles with δ(Γ) < 2 log|Γ| is
  finite.
- **Corollary 1.2**: for each fixed ν ≥ 1, the number of Collatz cycles with
  δ(Γ) ≤ ν is finite. (Note: Steiner's theorem is exactly the case ν = 1 —
  the only positive Collatz cycle with δ = 1 is the fixed point 1.)
- **Lemma 2.2**: if {k_i} generates a Collatz cycle then k = k₁+…+k_n ≤ 2n
  (from 2^k = Π(3 + 1/x_{i−1}) ≤ 4^n); in particular, for each n, only
  finitely many Collatz cycles with |Γ| = n.
- Method: cycle existence ⇔ M = 2^k − 3^n divides a periodic sequence
  F_i = φ_{n−1}(k_{i+1},…,k_{i+n−1}) (Lemma 2.1); reformulation in terms of
  the descents (h_j, n_j) with ψ-functions (Lemma 3.1); the H-sequence
  minimum bound (4.1) combined with the Baker–Feldman effective lower bound
  |k log 2 − n log 3| > max(k,n)^{−C₀} gives the finiteness. Extended to
  3x+d maps in Remark 4.1.

## Why it matters for this run

This is the primary behind the previously-held `brox-finitely-many-cycles`
claim (which was asserted via Chamberland's survey). The primary statement
uses δ(Γ) = number of descending elements, i.e. elements with k(x) ≥ 2 —
NOT the σ₁ mod-4 count in the Chamberland-derived claim. The claims ledger
should prefer this primary statement. Note the subtlety: Corollary 1.2's
finiteness for δ ≤ ν is what Simons–de Weger's m-cycle finiteness and
Hercher's m ≥ 92 build on — this paper is the modern rigorous form of
Steiner's old theorem.

```claim
id: brox-finite-cycles-few-descents
statement: There are only finitely many Collatz cycles Γ with δ(Γ) < 2 log|Γ|, where δ(Γ) is the number of descending elements (odd x with 2-adic multiplicity k(x) ≥ 2 of 3x+1); consequently finitely many with δ(Γ) ≤ ν for each fixed ν ≥ 1. In particular (Lemma 2.2) finitely many Collatz cycles of each period n (k = Σk(x) ≤ 2n).
hypotheses: T₁ the odd-only accelerated map, 2^{k(x)}T₁(x) = 3x+1; Collatz cycle = cycle of T₁.
holds-here: true.
evidence: proved in source (Brox 2000, Thm 1.1, Cor 1.2, Lemma 2.2), read in full text from the ICM scan.
status: proved (in source; not yet Lean-formalised here)
falsifies: an infinite family of Collatz cycles with δ(Γ) < 2 log|Γ|, or two cycles with the same period n.
```
