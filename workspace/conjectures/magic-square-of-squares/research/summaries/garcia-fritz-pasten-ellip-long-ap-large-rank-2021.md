# Garcia-Fritz & Pastén, "Elliptic curves with long arithmetic progressions have large rank", IMRN 2021

[[garcia-fritz-pasten-ellip-long-ap-large-rank-2021]]
Full text: `research/sources/garcia-fritz-pasten-ellip-long-ap-large-rank-2021.full.md`
arXiv:1910.14485v1 [math.NT], 31 Oct 2019. **This IS the genuine paper** (formerly
wrong-fetched as 1807.06084; the file has been overwritten with the correct text —
the previous "WRONG FETCH" note is obsolete). IMRN 2021(10):7394–7432.

## The verbatim central theorem (Section 6.1, Theorem 6.1)

> "Let j0 ∈ Q^alg and let d ≥ 2 be an integer. There is an effectively computable
> constant κ(j0,d) depending only on j0 and d such that the following holds:
> Let E be an elliptic curve over Q^alg with j-invariant equal to j0. Let g ∈ k(E)
> be a non-constant rational function on E of degree d defined over Q^alg. Let
> Γ ⊆ E(Q^alg) be a subgroup of finite rank. Suppose that for a positive integer N
> there is a sequence P1,…,PN of points in Γ such that no Pj is a pole of g, and
> the sequence g(P1),…,g(PN) ∈ Q^alg is a non-trivial arithmetic progression. Then
> **1 + rank Γ > κ(j0,d) · log N.**"

**Hypothesis check for this problem.** The theorem requires the AP to be of the
values **g(P_j) of points P_j that themselves lie in a finite-rank subgroup Γ**.
For the MSS: the three x-values a−b, a, a+b are x-coordinates of the **doubled**
points 2Q₀, 2Q₁, 2Q₂ ∈ 2E(Q). Take P_j = 2Q_j. Then P_j ∈ 2E(Q) ⊆ E(Q), and
2E(Q) has finite index in E(Q) (index = #E(Q)/2E(Q) ≤ #Sel₂(E) < ∞), so
rank(2E(Q)) = rank(E(Q)) =: r. With g = x (degree 2), the values
g(2Q_j) = x(2Q_j) = a−b, a, a+b form a non-trivial AP (b ≠ 0). **So the exact
hypotheses hold with Γ = 2E(Q), the AP-points being the doubled points
themselves.** Doubling is NO obstruction: an AP of doubled-point x-coordinates
*is* an AP of x(P) for points P = 2Q ∈ Γ = 2E(Q).

**Bearing.** Theorem 6.1 (11/§) gives N ≤ C(j0,2)^(1+r), i.e. the AP-3 length is
consistent for any r ≥ 0 as long as C ≥ 3^(1/(r+1)). Its j0-dependence was
removed by Gao–Ge–Kühne uniform Mordell–Lang, giving Theorem 1.8 in the 2026
note: **absolute C** with length ≤ C^(r+1) for ALL E/Q of rank r (unconditional,
over any number field). The Robertson curve E_c has j varying with c, so the
absolute-C version is the one needed. Constraint: needs C^(1+r) < 3 for
non-existence; C is ineffective, so no numeric contradiction is extractable.

**What it does NOT settle**: the value of C (Remond/GGK constants not explicit);
whether rank(E_c) for c = e² is bounded. These are the surviving gaps.

```claim
id: gfp-2021-theorem-6-1-doubled-points-in-scope
statement: The Garcia-Fritz-Pasten AP-length bound (Thm 6.1: N <= C^(1+rank Γ),
  and its j-independent Theorem 1.8/2026 form) applies verbatim to the MSS
  configuration, whose AP is x(2Q_0), x(2Q_1), x(2Q_2) = a-b, a, a+b of DOUBLED
  points: take P_j = 2Q_j in the finite-index (hence same-rank) subgroup
  2E(Q) ⊆ E(Q); then g(P_j) = x(2Q_j) form the AP, so the hypothesis "P_j in
  finite-rank Γ, g(P_j) in AP" holds with Γ = 2E(Q), g = x-coordinate (deg 2).
hypotheses: Robertson reduction holds (a-b, a, a+b = x(2Q_j), Q_j in E(Q), on
  E: y^2 = x(x^2 - c^2)); 2E(Q) finite index (Mordell-Weil + finite Selmer); AP
  non-trivial (b != 0, distinct entries)
holds-here: yes
status: checked (verbatim Thm 6.1 arXiv:1910.14485, and 2026-note Thm 1.8)
bearing: dissolves the doubled-point applicability blocker (exact-reduction-magic-507c):
  uniform-height-bound-elliptic-ap is usable as-is on the geometry; the ONLY surviving
  obstruction is ineffectiveness of C (cannot get C^(1+r) < 3), plus unbounded rank of E_c.
anchor: research/sources/garcia-fritz-pasten-ellip-long-ap-large-rank-2021.full.md (Thm 6.1, Sec 6.1) + garcia-fritz-pasten-bremner-uniformity-2026.full.md (Thm 1.8)
answers: exact-reduction-magic-507c
contradicts: garcia-fritz-pasten-ellip-long-ap-large-rank-2021 WRONG-FETCH note (outdated; file is now the genuine paper)
```

## Source
Garcia-Fritz, N. and Pasten, H. "Elliptic curves with long arithmetic progressions
have large rank." IMRN 2021(10):7394–7432. arXiv:1910.14485.
