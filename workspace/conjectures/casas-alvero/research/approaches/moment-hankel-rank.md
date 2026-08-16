# Approach: moment / Hankel rank (refuted)

Proposed: re-read the shared-root conditions as linear constraints on the power
sums of the roots, and "pure power" as "rank-1 Hankel matrix" (Pólya/Kronecker:
Hankel rank = number of distinct roots; Curto–Fialkow flat extension in the PSD
setting). CA becomes "the disjunctions force rank H = 1".

```approach
idea: Truncated moment problem / Hankel operator. For monic f with distinct
      roots β_1,…,β_r of multiplicities m_1,…,m_r, the Hankel matrix
      H = [s_{a+b}]_{0 ≤ a,b ≤ r−1} built from the power sums s_k = Σ_j m_j β_j^k
      has rank exactly r (Pólya/Kronecker; flat extension, Curto–Fialkow).
      Hence "f is a pure power" ⟺ rank H = 1 ⟺ (s_0,…,s_{2n−2}) is a geometric
      progression n·c^k. CA becomes the claim that the n−1 shared-root
      conditions force rank H = 1.
mechanism: H_i(f)(β_j) = 0 is, via the owned root-difference identity,
      e_{n−i}(β_j−β_*) = 0 — a linear relation among power sums via Newton
      identities. CA hypothesis is a disjunction of such equations per i; the
      question is whether the disjunctions force rank H = 1.
      Char-p break: in char p the middle colours are vacuous (Lucas:
      H_i(x^{p+1}−x^p) = 0 for 2 ≤ i ≤ p−1), so the moment constraints
      disappear and rank 1 is no longer forced — the 2-root witness has a
      rank-2 moment matrix unconstrained by the vacuous colours.
status: refuted
killed-by: (1) NOT a new object. The "moment matrix of the root measure" is the
      power-sum matrix, which is equivalent to the elementary-symmetric
      (root-difference) content the run already owns: Newton's identities give
      a bijection between the power sums s_k and the elementary symmetric
      functions e_k, and the owned identity H_i(f)(β_j) = e_{n−i}(β_j−β_*) IS
      the symmetric-function form of the same data. The published CA literature
      already works in exactly this language: Laterveer–Ounaïes
      (arXiv:1204.0450, Lemma 2) use Newton formulas on the power sums σ_m(l)
      of the roots of the derivatives, and Castryck–Laterveer–Ounaïes
      (arXiv:1208.5404, Theorem 2, §3) organise the degree-(p+1) counterexample
      constraints around a Hankel-type determinant Δ_f (eq. 2) that must vanish
      mod p. So the "different matrix from every one the run owns" premise of
      the proposal is false — it is the adopted root-difference-coloring in
      moment-matrix disguise.
      (2) The bridge "CA ⟺ rank H = 1" is exactly CA restated: rank H = 1 ⟺ f
      is a pure power (that is the classical direction, true), so "the
      disjunctions force rank 1" is nothing but "the shared-root conditions
      force f to be a pure power". No reduction.
      The char-p break claim is correct and survives: over F_p the witness
      x^{p+1}−x^p has two distinct roots {0,1}, so its moment matrix has rank 2,
      and the Lucas-vacuous middle Hasse derivatives impose no link between the
      two roots. But a correct char-p break does not save a reformulation whose
      only load-bearing step is the conjecture itself.
first-step: superseded — the moment/Hankel content is absorbed into
      root-difference-coloring (Newton ⇔ elementary-symmetric). What could be
      kept is Castryck's Δ_f determinant (eq. 2 of arXiv:1208.5404) as a
      bookkeeping refinement of the type/colour constraints, not a new matrix.
precedent: laterveer-ounaies-2012, (Newton, power, sums, σ_m(l), =, central,
      tool);, castryck-2012, (Hankel-type, Δ_f, determinant, eq., 2,, Theorem,
      2,, already, organizes, degree-(p+1), counterexample, constraints);
      polya-kronecker / curto-fialkow, (the, classical, Hankel-rank,
      =, #atoms, fact,, true, but, standard);, newton-identities,
      (power-sum, ⇔, elementary-symmetric, bijection)., No, source, proves,
      that, the, CA, disjunctions, force, rank, H, =, 1.
```
