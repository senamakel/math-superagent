# Nathanson — "Arithmetic functions and fixed points of powers of permutations"

Source: https://arxiv.org/abs/2206.04021 (arXiv:2206.04021, v5, revised 7 Mar 2023).
Published: Archiv der Mathematik **120** (2023), 565–575; DOI 10.1007/s00013-023-01855-0.
Companion full text: `research/nathanson_fixed_points_powers.full.md` (this file holds only
the front-matter because the downloaded arXiv abs page carries no body; the
mathematical content below is taken from the abstract and the paper's stated
results as indexed by the search service).

## What the source establishes

For a permutation σ of a finite or countably infinite set X, let
F_X(σ^k) count the **fixed points of the k-th power of σ**. The whole sequence
k ↦ F_X(σ^k) determines the conjugacy class of σ.

The central identity (the paper's reconstruction tool) is:

> **F_X(σ^ℓ) = Σ_{k|ℓ} k · C(k)**,      where C(k) = number of k-cycles of σ.

Reason: an element is fixed by σ^ℓ iff it lies in a σ-cycle whose length divides ℓ;
a k-cycle contributes exactly k such fixed points, and contributes to every
multiple ℓ of k. The cycle-count vector C(k) is then recovered by Möbius
inversion, C(ℓ) = (1/ℓ) Σ_{d|ℓ} μ(ℓ/d) F(σ^d).

The paper also characterizes which arithmetic functions arise as fixed-point
counting functions of permutations, and when the sequence is periodic.

## Implications for the Q(n) problem

The factoradic/Lehmer rank of a permutation, and the run's gap-affine
inversion structure f_n(k)=A_n+(k−1)B_n, are already known (from
Campion-Loth et al. arXiv:2301.00898 and Pinsky–Schickentanz arXiv:2510.20654)
to depend on the conjugacy class through the number of fixed points a₁ = C(1)
and 2-cycles a₂ = C(2). This paper supplies a *third, independent* structural
fact: the correspondence between cycle counts C(k) and the fixed-point counts
of all powers σ^k, and a Möbius-inversion route to express any conjugacy-class
datum in terms of the fixed-point-of-powers function F(σ^k).

That matters because the conjugacy-class sums behind A_n and B_n are exactly
the quantities the run must weight by cycle type; expressing the a₁ / a₂
coefficients through fixed-point counts of powers gives an alternative,
character-free way to set up (or cross-check) those sums. It does NOT by
itself give a closed form for A_n, B_n — that remains the open step — but it
adds a second concrete machine (cycle-count ↔ fixed-points-of-powers) beside
the inversion-probability formulas already in the library, and it confirms the
centrality of the fixed-point parameter.

Note: the downloaded abs page contains only front matter; the identity above is
the paper's headline result as recorded by the search index, and the Möbius
inversion C(ℓ) = (1/ℓ)Σ_{d|ℓ}μ(ℓ/d)F(σ^d) is the standard reconstruction stated
in it. Cite it as the source for "fixed-point counts of powers determine cycle
structure."
