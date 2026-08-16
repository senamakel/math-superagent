# Almost k-union closed set systems

Raphael Yuster. arXiv:2302.12276v1 [math.CO], 2023. University of Haifa.

**Full text (read, intro + main results):** `research/sources/yuster-almost-k-union-closed-2023.html.full.md` (83KB)

## What it establishes (primary source, read)

This is the **origin paper of the k-union-closed attack line** that the live `attack-coupling-half` task builds on. It extends Gilmer's method and the Chase–Lovett result to *higher-order unions*.

**Definition (approximate k-union closed).** F ⊆ 2^[n], {∅}≠F is c-approximate k-union closed if for at least a c-fraction of the k-tuples A₁,…,A_k∈F we have ∪A_i ∈ F. Union-closed = k=2, c=1.

**Theorem 1.2 (Chase–Lovett, the k=2 case, restated).** A (1−ε)-approximate union-closed system (0≤ε<1/2) has an element in ψ−δ of its sets, ψ=(3−√5)/2, δ=2ε(1+log(1/ε)/log|F|). And ψ is *optimal*: there are such F (1−o_n(1) approximate) with every element in ≤ ψ+o_n(1) sets. **This is why (3−√5)/2 is the iid-entropy ceiling: it is the exact optimum for the approximate-union-closed relaxation.**

**ψ_k.** Unique real root of (1−x)^k − x in [0,1]; ψ₂ = (3−√5)/2.

**Theorem 1.6.** Conjecture 1.5 (the ψ_k version of Theorem 1.2 for k-unions) holds for k=3,4.

**Theorem 1.7.** Conjecture 1.5 holds with constant z_k in place of ψ_k, where z_k > ln k/(3k), 1/2 < z_k/ψ_k ≤ 1, and lim_{k→∞} z_k/ψ_k = log(1/φ)/log 2 ≈ 0.6943. So for large k the guaranteed element fraction is comparable to a constant × ψ_k.

**Proposition 1.4.** For every n there is a 1−o_n(1)-approximate k-union closed F whose every element is in ≤ ψ_k + o_n(1) sets. So ψ_k is (asymptotically) the right ceiling for this relaxation at order k.

**Core technical step.** Generalizes Boppana's binary-entropy inequality. For k=3,4 it is proved rigorously; for larger k the proof reduces to a **conjecture about roots of certain real polynomials** — the same real-rootedness program Wakhare (JMAA 2025) develops, and which Ho (arXiv:2601.19327) eventually proves for all real k via calculus (also in this library).

**Relation to Ho's α_k (documented tie-back).** Yuster's ψ_k (root of (1−x)^k = x) equals Ho's α_k/(1+α_k), where α_k is the unique positive root of x(1+x)^(k−1)=1. Both are the order-k "barrier" constant of the iid/approximate entropy method; α₂/(1+α₂) = ψ₂ = (3−√5)/2. (Script to verify: `code/out/yuster_psi_k_check.py`.)

```claim
id: yuster-psi-k-approx-optimal
statement: For the (1−ε)-approximate k-union-closed relaxation, ψ_k (unique root of (1−x)^k=x in [0,1]) is the asymptotically optimal ceiling: Theorem 1.6 proves the ψ−δ bound for k=3,4; Theorem 1.7 proves a z_k−δ bound (z_k>ln k/(3k), z_k→0.6943·ψ_k) for all k; Prop 1.4 gives matching upper constructions at ψ_k. ψ_2=(3−√5)/2 (Chase–Lovett).
hypotheses: F⊆2^[n], {∅}≠F, (1−ε)-approximate k-union closed, ε<1/2.
holds-here: true
status: proved
bearing: shows the (3−√5)/2 barrier is the k=2 member of the ψ_k family, and is optimal for the approximate relaxation; motivates k-union-closed attacks.
anchor: Yuster arXiv:2302.12276, Thms 1.2,1.6,1.7, Prop 1.4.
```

```claim
id: yuster-realroot-reduction
statement: The k-union-closed entropy inequality (Conjecture 1.5) reduces for general k to a conjecture about the real roots of explicit real polynomials; rigorously proved only for k≤4 in this paper (Wakhare/Ho subsequently settle the underlying entropy inequality for all real k).
hypotheses: k≥2.
holds-here: true
status: proved (as a reduction; root conjecture open here)
bearing: identifies the precise open technical step the attack must clear for general k; now partly bypassed by Ho's all-k calculus proof.
anchor: Yuster arXiv:2302.12276, §3 (Cor 3.7), §5.
```

## Why it matters for this run
- Directly behind `attack-coupling-half`: it is where the k-union-closed (order-k OR) attack and the ψ_k/α_k barrier family come from.
- Establishes that (3−√5)/2 is not merely "where Gilmer's inequality runs out" but the *optimal* constant for the approximate-union-closed relaxation (Chase–Lovett), which is the cleanest statement of what the iid method cannot cross.
- Together with Ho (all-k proof, Lean 4) and Wakhare (real-rootedness), this completes the picture: the entropy inequality at every order k is settled; what remains is UC itself at k=2, c=1.

## Notes
- ψ_k = α_k/(1+α_k) identity is documented (verify with `code/out/yuster_psi_k_check.py`); it links Yuster's framework to Ho's α_k formulation and confirms the family is one family, not two.
