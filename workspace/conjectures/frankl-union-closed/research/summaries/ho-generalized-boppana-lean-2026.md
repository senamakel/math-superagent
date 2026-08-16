# A generalization of Boppana's entropy inequality

Boon Suan Ho. arXiv:2601.19327v1 [math.CO], 27 Jan 2026. National University of Singapore. 4 pages, CC BY 4.0. Note: analysis assisted by GPT-5.2 pro; formalized in Lean 4, code at https://github.com/boonsuan/entropy-inequality.

**Full text (read):** `research/sources/ho-generalized-boppana-lean-2026.html.full.md`

## What it establishes (primary source, read in full)

**Theorem 1.** Let k > 1 be real. Then α_k·h(xᵏ) ≥ x^(k−1)·h(x) for 0 ≤ x ≤ 1, where 0 < α_k < 1 is the unique positive solution to x(1+x)^(k−1) = 1, and equality holds iff x = 0, 1/(1+α_k), or 1.

Boppana's inequality (h(x²) ≥ φx·h(x), φ = (1+√5)/2) is exactly the k=2 case. This was conjectured by Yuster for integer k≥2 (who proved k=2, as the known AHS/Sawin bound, and k=3,4); Yuster–Yashfe proved 5 ≤ k ≤ 20; Wakhare investigated real k. Ho proves it for all real k > 1.

**Corollary 1 (Yuster's Conjecture 1.5), the UC analogue.** Let k ≥ 2 integer, 0 ≤ c ≤ 1. A finite set system F is c-approximate k-union-closed if for at least a c-fraction of the k-tuples A₁,…,A_k ∈ F, ∪A_i ∈ F. If {∅} ≠ F ⊆ 2^[n] is (1−ε)-approximate k-union-closed with 0 ≤ ε < 1/2, then some element lies in α_k/(1+α_k) − δ fraction of sets, where δ = (kε + 2εlog(1/ε)/log|F|)^(1/(k−1)).

For k=2 this recovers the approximate-union-closed bound with α₂/(1+α₂) = (3−√5)/2 — the iid-entropy barrier, now seen as the k=2 case of this family. (Verified: α₂ solves x(1+x)=1, x = 1/φ ≈ 0.6180, and α₂/(1+α₂) = 0.6180/1.6180 = 0.381966 = (3−√5)/2.)

## Proof method (the structural fact this run should reuse)

Define q(x) = x^(k−1)h(x)/h(xᵏ) on (0,1), extend to q(0)=q(1)=1/k. Goal q(x) ≤ α_k. Show q'(x)=0 iff x = 1/(1+α_k). The key reduction: q'(x)=0 reduces (via h'(x)=log(1−x)−log x, and xh'(x)=h(x)+log(1−x)) to U(x)=U(xᵏ) where U(x) = log(x)·log(1−x)/h(x). Since U(x)=U(1−x) and U is strictly decreasing on (0,1/2], U(x)=U(xᵏ) forces xᵏ = 1−x, hence x = 1/(1+α_k). Uniqueness of the critical point, with q(1/(1+α_k))=α_k > 1/k = q(0)=q(1), gives the result (Lemma 3, a local-max argument).

**Why it matters for this run:** This is the same attack line as the live `attack-coupling-half` task. It (a) proves the generalized entropy inequality for *all real k > 1*, which is what a k-union-closed (not just 2-union-closed) attack needs; (b) confirms the barrier (3−√5)/2 is the k=2 member of this exact family α_k/(1+α_k); (c) provides a Lean 4 formalization (github.com/boonsuan/entropy-inequality) that lean_prover can lift. Yuan/Yuster-style generalization is a candidate route past the k=2 iid barrier.

```claim
id: ho-generalized-boppana-k
statement: For real k > 1, α_k·h(x^k) ≥ x^(k−1)·h(x) for 0≤x≤1, where α_k is the unique positive solution of x(1+x)^(k−1)=1; equality iff x ∈ {0, 1/(1+α_k), 1}. Boppana's inequality is the k=2 case.
hypotheses: k real > 1; h binary entropy.
holds-here: true
status: proved
bearing: generalizes the engine of the iid-entropy barrier to all k>1; the barrier (3−√5)/2 = α_2/(1+α_2) is the k=2 member of this family; targets a k-union-closed attack.
anchor: Ho arXiv:2601.19327, Theorem 1; full text in sources.
formalisation: Lean 4, github.com/boonsuan/entropy-inequality
```

```claim
id: ho-approx-k-union-closed
statement: A (1−ε)-approximate k-union-closed system (ε<1/2) has an element in α_k/(1+α_k) − δ of its sets, δ=(kε+2εlog(1/ε)/log|F|)^(1/(k−1)). For k=2 this is the approximate-union-closed (3−√5)/2 bound (Chase–Lovett).
hypotheses: F finite, {∅}≠F⊆2^[n], (1−ε)-approximate k-union-closed, 0≤ε<1/2.
holds-here: true
status: proved
bearing: generalizes Chase–Lovett's approximate-UC bound to k-union-closed; shows (3−√5)/2 is the k=2 case, and larger k need different constants.
anchor: Ho arXiv:2601.19327, Corollary 1.
```

## Notes
- k=2 tie-back verified numerically (α₂=1/φ, α₂/(1+α₂)=(3−√5)/2 ≈ 0.381966), matching the library's established `ahs-barrier`.
- The paper acknowledges LLM assistance (GPT) in some steps; the Lean 4 formalization is the independent mechanical check, per this workspace's rule that numerics/heuristics are not proof.
