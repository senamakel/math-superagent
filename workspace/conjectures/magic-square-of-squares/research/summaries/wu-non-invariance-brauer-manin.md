# Wu: Non-invariance of the Brauer-Manin obstruction for surfaces (arXiv:2103.01784)

Full text: `research/sources/wu-non-invariance-brauer-manin.full.md` (78.9 KB, complete paper at v3, 14 Apr 2021 — real PDF with body, proofs, appendix, not an abstract page).

## What the paper establishes

Two theorems, both assuming **Stoll's conjecture for curves over K** (Conjecture 3.0.1 = [Sto07, Conj. 9.1]: for any smooth projective geometrically connected curve C over a number field K, C(K) is dense in pr∞_K(C(A_K)^Br)). For any **nontrivial extension of number fields L/K**:

**Theorem 4.1.7** (negative answer to Question 1.2.1, weak approximation). There exists a smooth, projective, geometrically connected **surface X over K** such that
- X has a K-rational point and satisfies **weak approximation with Brauer-Manin obstruction off ∞_K** (i.e. off the archimedean places);
- X_L does **not** satisfy weak approximation with BM obstruction off T for **any** finite subset T ⊂ Ω_L.

**Theorem 4.2.9** (negative answer to Question 1.2.2, Hasse principle). There exists a smooth, projective, geometrically connected **surface X over K** such that
- X is a **counterexample to the Hasse principle** whose failure is **explained by the Brauer-Manin obstruction**;
- X_L is a counterexample to the Hasse principle but its failure **cannot be explained** by the Brauer-Manin obstruction.

Both are **unconditional** in the explicit examples K=Q, L=Q(i) (§5.2 for 4.1.7, §5.3 for 4.2.9): X is given by explicit equations in P²×P² (Thm 4.1.7) and P²×P¹×P¹ (Thm 4.2.9), built over the elliptic curve E: w1²w2 = w0³ − 16w2³, which has analytic rank 0 both over Q and as a quadratic twist E^(−1).

## Method

Construction idea (§1.3.3): find a curve C over K with C(K), C(L) both finite nonempty and C(K) ≠ C(L) (type I, Def. 3.0.3 — guaranteed by Lemma 3.0.4 under Stoll). Choose a dominant morphism γ: C → P¹ with γ(C(K)) = {∞}, γ(C(L)\C(K)) = {0}, étale over the discriminant locus R. Build a pencil over C whose fibres are prescribed curves C_∞ (above C(K)) and C_0 (above C(L)\C(K)), whose differing arithmetic forces the non-invariance.

## Implication for this run

Base-change non-invariance of the BM obstruction is a **proved (conditional) fact, with unconditional surface examples**, not a mere caution. Any Q(√3)-vanishing argument for the magic-square K3 surface must compute the relevant class explicitly; it can never be inferred from the mere existence of MSS over extension fields. But `holds-here: no` as a statement *about Bremner II's K3 S*: Wu's surfaces are generic pencils over an elliptic curve, not the magic-square surface, and the paper gives no method to evaluate BM on S.

## Claim block

```claim
id: wu-bm-noninvariance-under-base-change
statement: For any nontrivial extension L/K of number fields, assuming Stoll's conjecture for all curves over K (Conj. 3.0.1 = a curve C over K has C(K) dense in pr∞_K(C(A_K)^Br)), there exist smooth projective geometrically connected surfaces X over K of two kinds: (i) X has a K-rational point and satisfies weak approximation with Brauer-Manin obstruction off the archimedean places ∞_K, while X_L satisfies weak approximation with BM obstruction off NO finite subset T ⊂ Ω_L; (ii) X is a counterexample to the Hasse principle whose failure is explained by the BM obstruction, while X_L is a counterexample to the Hasse principle whose failure cannot be explained by the BM obstruction.
hypotheses: L/K nontrivial extension of number fields; Conjecture 3.0.1 (Stoll) holds over K; surfaces smooth projective geometrically connected. Unconditional for the explicit K=Q, L=Q(i) examples.
holds-here: no — Wu's surfaces are generic pencils over an elliptic curve, not Bremner II's magic-square K3 S; provides the base-change non-invariance caution and a certified-construction template, but transfers no theorem to S.
status: proved (conditional on Stoll's conjecture); unconditional in the Q/Q(i) examples
bearing: any Q(√3)-vanishing BM argument must compute the class explicitly, never infer it from extension-field MSS; non-invariance under base change is real and cannot be used as a blanket impossibility lever for the magic-square S.
anchor: research/summaries/wu-non-invariance-brauer-manin.md; source research/sources/wu-non-invariance-brauer-manin.full.md (arXiv:2103.01784v3), Theorems 4.1.7 and 4.2.9.
```

Note (replaces the earlier "only abstract on disk" memory): the full paper has been on disk since the original download; the task premise and the durable-memory entry claiming a 6.6KB abstract-only file are stale.
