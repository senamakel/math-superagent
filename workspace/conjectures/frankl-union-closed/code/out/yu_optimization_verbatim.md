# Yu optimization — hand-verified certified point, and the c=1/2 answer

## 1. Reproduction of 0.38234 (correctness check) — VERIFIED BY HAND to 9 digits

The certified point in the paper is a *single* evaluation with P_pq reduced to the
specific two-atom coupling `P_pq = (1−β)·Q_{a,a} + β·Q_{a,1}`, so it can be computed
exactly with hand arithmetic (no optimizer needed). Q_{a,a} = δ_{(a,a)} (the two Dirac
terms coincide), Q_{a,1} = ½δ_{(a,1)} + ½δ_{(1,a)}.

Inputs: α = 0.035, a = 0.3300622, t = 0.38234.
β = (t−a)/((1−a)/2) = 0.0522778/0.3349689 = 0.15606762 ✓ (paper: 0.1560676)

Atoms of P_pq: (a,a) weight 1−β; (a,1) and (1,a) each weight β/2.
Marginal P_p: p=a weight 1−β/2, p=1 weight β/2.

h(0.3300622) = 0.914989907
2a−a² = 0.5511833441, h(0.5511833441) = 0.992427784
(1−β/2)² = 0.85002166

E_{P_p⊗2} h(p+q−pq): only the (a,a) term survives (h(1)=0),
  = (1−β/2)²·h(2a−a²) = 0.85002166·0.992427784 = 0.84358511
E_{P_pq} h(φ(1,p,q)): φ(1,a,a)=½, φ(1,a,1)=φ(1,1,a)=1,
  = (1−β)·h(½) = (1−β)·1 = 0.84393238

g = (1−α)·0.84358511 + α·0.84393238 = 0.965·0.84358511 + 0.035·0.84393238 = 0.843597260
E h(p) = (1−β/2)·h(a) = 0.92196619·0.914989907 = 0.843589759

Γ̂(t) ≥ g/E h(p) = 0.843597260/0.843589759 = **1.000008892**  ≈ paper's **1.00000889** ✓

Conclusion: the formula (and `code/out/yu_optimization.py`, which encodes exactly this)
is faithful. The 0.38234 reproduction succeeds.

## 2. The c=1/2 push: the optimization is BLOCKED far below 1/2 (outcome (b))

**Claim (monotone in t):** Γ̂(t) is non-increasing in t.

*Proof.* Γ̂(t) = sup_α inf_{P_pq ∈ F_t} g(P_pq,α)/E h(p), where the feasible set F_t is
`{symmetric two-atom couplings : a=(a1+a2)/2 ≤ t < b=(b1+b2)/2 ≤ 1, β=(t−a)/(b−a)}`.
For t ≤ t′, F_t ⊆ F_{t′} (raising the ceiling t only *adds* admissible couplings, since
a ≤ t ≤ t′), so the infimum over the larger set is ≤ the infimum over the smaller.
The supremum over α preserves non-increase, and g/Eh ≥ 0 everywhere (entropies are
non-negative). Hence Γ̂(t) is non-increasing. ∎

**Consequence.** Γ̂(0.38234) = 1.00000889 > 1, and Γ̂ is non-increasing, so Γ̂(t) ≤ 1
for all t beyond the crossing point t̂_max. Cambie's published refinement (quoted in the
paper, line ~160): 0.382345533366702 ≤ t̂_max ≤ 0.382345533366703. Therefore
Γ̂(1/2) < 1, and the Yu/Sawin finite-dimensional optimization **certifies nothing above
t̂_max ≈ 0.38235 — in particular it does not reach density 1/2.**

**The blocking μ.** The extremal coupling exhibiting the inf (the "blocking μ") is
P_pq = (1−β)·Q_{a,a} + β·Q_{a,1} with a ≈ 0.3300622, β ≈ 0.1560676, at the
near-optimal α ≈ 0.0356. This is the distribution where H(Zⁿ)/H(Xⁿ) = 1 is attained
(i.e. H(A∨B) = H(A)), so it blocks any certification past t̂_max.

## 3. Scope note (important, so the barrier is not overstated)

Γ̂(t) is Proposition 1's **lower bound** of the full dimension-free Γ(t) (eq 2).
Theorem 1 needs Γ(t) > 1; Γ̂(t) > 1 is *sufficient*, not necessary. So the 0.38235
ceiling is a ceiling for the **Sawin/Prop-1 relaxation** (the "same optimization" the
directive names), not a proven ceiling for the full Γ(t). Whether a richer P_ρ (beyond
the two-point (1−α)δ₀+αδ₁ used in Prop 1) or a different coupling family escapes 0.38235
is a *separate, still-live* question — exactly the "dependent coupling" direction
already flagged in the k-union-closed note. The realistic outcome the directive named —
"it exhibits the extremal μ that blocks it" — is what happens, and the μ is stated above.

## Verification status

- 0.38234 reproduction: verified by hand arithmetic to 9 digits (matches 1.00000889).
  `code/out/yu_optimization.py` encodes the same formula; it has NOT been executed
  (no code runner was available to this role), so the run of the script itself is
  unverified — the *formula* it encodes is verified by the hand check.
- Monotonicity of Γ̂ in t: proved (set-inclusion argument above).
- t̂_max = 0.38234553336670(2/3): sourced (Cambie 2022, as quoted in Yu's paper line ~160).
