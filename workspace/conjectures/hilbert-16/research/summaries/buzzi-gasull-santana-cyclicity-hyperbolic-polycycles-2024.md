# Buzzi–Gasull–Santana 2024 — cyclicity of hyperbolic polycycles

Full text: [[buzzi-gasull-santana-cyclicity-hyperbolic-polycycles-2024.html.full]] (arXiv:2407.20721, math.DS, 2024).

## What the source establishes (held full text)

**Framework.** Γⁿ a hyperbolic polycycle: n (not necessarily distinct) hyperbolic
saddles p₁,…,pₙ with hyperbolicity ratios rᵢ = |λᵢˢ|/λᵢᵘ and graphic number
r(Γⁿ) = ∏ rᵢ. Cherkas: r(Γⁿ)≠1 ⇒ Γⁿ has well-defined stability (r>1 stable,
r<1 unstable), i.e. Γⁿ is *simple*. Cyclicity Cycl(X, 𝒳, Γⁿ) ≥ k means: for
every ε>0 there is Y_ε ∈ 𝒳 arbitrarily close to X with at least k limit cycles
γⱼ(ε) at Hausdorff distance < ε from Γⁿ.

**Main result (Theorem 1).** Let 𝒳 be 𝔛^∞ (smooth fields, Whitney strong
topology) or 𝒫^r (polynomial fields of any degree, Whitney weak C^r topology),
r ≥ 1. If X ∈ 𝒳 has a hyperbolic polycycle Γⁿ, then
**Cycl(X, 𝒳, Γⁿ) ≥ Δ(Γⁿ)**,
where Δ(Γⁿ) = max over permutations σ of #{i : (R_{i,σ}−1)(R_{i−1,σ}−1) < 0}
with R_{i,σ} = ∏ⱼ₌₁ⁱ r_{σ(j)}. So Δ(Γⁿ) counts how many times the sign of
(r-partial-product − 1) can be made to alternate by reordering the saddles.
0 ≤ Δ ≤ n; Δ = 0 iff all rᵢ = 1.

**Method.** Break Γⁿ into sub-polycycles Γ^{n−1}, Γ^{n−2}, … by expelling saddles
one at a time; each stability flip (opposite stabilities of Γ^{n₀} and
Γ^{n₀−1}, guaranteed by (r(Γ^{n₀})−1)(r(Γ^{n₀−1})−1) < 0) yields ≥ 1 limit cycle
of odd multiplicity by Poincaré–Bendixson. The technical core is regularity
(continuity and differentiability in initial conditions and parameters) of the
return maps, obtained from Marín–Villadelprat's asymptotic expansion of the
Dulac map (JDE 2020/2021/2024, refs [18],[19],[21]).

**Context it records (valuable for this run):**
- Mourtada: n=1, cyclicity ≤ 1 if r₁ ≠ 1 (Andronov–Leontovich); n=2, cyclicity
  ≤ 2 if (r₁−1)(r₂−1) ≠ 0, = 2 if (r₁−1)(r₂−1) < 0; n∈{3,4} generic results,
  incl. generic families with cyclicity **5** for n=4. Published sources:
  Mourtada Ann. Inst. Fourier 41 (1991) (finiteness algorithm), JDE 113 (1994)
  (two-vertex polycycles), Ann. Fac. Sci. Toulouse 3 (1994) (three-vertex).
- Dukov (Sb. Math. 214 (2023)): n ≥ 2 generic ⇒ any limit cycle from Γⁿ by a
  finite-dimensional perturbation has multiplicity ≤ n.
- Non-generic: Han–Zhu give Γ¹ with cyclicity ≥ 5 (polynomial deg 8) and Γ²
  with cyclicity ≥ 12 (deg 11); Tian–Han higher for n=2.
- Polynomial case (X ∈ 𝒫^r) is "totally new": any prescribed list of
  hyperbolicity ratios is realisable by a polynomial field of the same degree
  n (Prop 9); can bifurcate n limit cycles from Γⁿ with polynomial
  perturbation, preserving derivative control on any compact — but NOT yet with
  perturbation degree equal to that of X (open).

## What it lets this run conclude

- **Hyperbolic polycycles are finitely cyclic (already known via Mourtada) and
  now have explicit lower bounds** Δ(Γⁿ) uniform in the family. The method to
  prove a *lower* bound on cyclicity is the model "break polycycles, count
  stability flips" — a finite combinatorial count in the hyperbolicity ratios.
- For **quadratic fields the hyperbolicity ratios are restricted** (quadratic
  saddles), which is exactly the DRR setting: the hemicycle closures
  (Marín–Villadelprat 2025) already give cyclicity 2 for the D-system class.
- The open DRR graphics are the *non-hyperbolic* ones (nilpotent, degenerate,
  semi-hyperbolic) — this paper supports that separation by showing the
  hyperbolic side is a settled, explicit theory.
- The Dulac-map regularity basis (MV 2020/21/24) is the instrument this run's
  displacement-function expansion needs; the QAS 2025 paper applies it to
  persistent polycycles with explicit return-map leading terms.

## Claim

```claim
id: h16-hyperbolic-polycycle-cyclicity-lower-bound-bgs2024
status: asserted
statement: Buzzi-Gasull-Santana (2024), "On the cyclicity of hyperbolic
  polycycles", arXiv:2407.20721, Theorem 1: if X is a C^∞ planar field (or a
  polynomial field) with a hyperbolic polycycle Gamma^n (n hyperbolic saddles,
  hyperbolicity ratios r_1..r_n), then Cycl(X, Xclass, Gamma^n) >= Delta(Gamma^n)
  where Delta(Gamma^n) = max over permutations sigma of #{i :
  (R_{i,sigma}-1)(R_{i-1,sigma}-1) < 0}, R_{i,sigma} = prod_{j<=i} r_{sigma(j)}.
  The bound is achieved by expelling saddles one by one, one limit cycle per
  stability flip. Polynomial case new: any list of ratios realizable by a
  polynomial field of degree n; lower bound attained by polynomial perturbation
  (generally of higher degree than X — the equal-degree requirement is open).
hypotheses: planar C^infty vector field X (or polynomial, P^r topology) with a
  hyperbolic polycycle Gamma^n; saddles possibly non-distinct; hyperbolicity
  ratios positive reals; cyclicity inside the family Xclass (Whitney strong C^infty
  or weak C^r on polynomials).
evidence-class: sourced (arXiv full text held,
  research/sources/buzzi-gasull-santana-cyclicity-hyperbolic-polycycles-2024.html.full.md).
falsifier: an error in the regularity argument for the return maps along the
  breaking steps (rests on Marin-Villadelprat Dulac-map asymptotics); or a
  hyperbolic polycycle with Delta(Gamma^n) stability flips but fewer than
  Delta bifurcating limit cycles in a full neighbourhood of X — no such
  counterexample known.
holds-here: yes for the hyperbolic classes of the DRR program and for the
  run's lower-bound instrument; the open DRR graphics are non-hyperbolic, so
  this does NOT close them — it sharpens why the hyperbolic side is done.
anchor: research/sources/buzzi-gasull-santana-cyclicity-hyperbolic-polycycles-2024.html.full.md
follows-from: h16-dulac-finiteness-theorem, drr-1994-citation-anchor
```

## Frontier additions

References [18],[19],[21] (Marín–Villadelprat Dulac-map trilogy, JDE
2020/2021/2024), [23],[25],[26] (Mourtada hyperbolic-polycycle finiteness),
[29] (Roussarie book), [11] (Han–Wu–Bi 2004 n-vertex polycycles) are now
frontier leads; **Mourtada Ann. Inst. Fourier 41 (1991) is the primary source
for "hyperbolic polycycles are finitely cyclic" and is open access on Numdam** —
high value for the DRR hyperbolic-classes row.