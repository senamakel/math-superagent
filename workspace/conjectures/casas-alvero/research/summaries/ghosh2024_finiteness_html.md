# Ghosh, *A finiteness result towards the CA conjecture* (arXiv:2402.18717, v3 2025)

Full text: [[ghosh2024_finiteness_html.full]]

The most structurally advanced source the run holds, and directly on the run's scheme-theoretic axis. Builds on the `Graf-von-Bothmer` weighted-projective-Z-scheme reformulation and proves a clean 2-dimensional bound on the counterexample variety in **every** characteristic.

## The arithmetic Casas-Alvero scheme

The `d`-th arithmetic Casas-Alvero scheme is `X_d ⊂ P_Z(1,2,…,d−1)`, cut out by the vanishings of `Res_X(P,P_i)` for all `1≤i<deg P`. CA in degree d over char-0 is equivalent to `X_d` having the "expected" 1-dimensional / empty structure; Conjecture CA (for fixed degree) ⇔ the projective variety of CA polynomials is 1-dimensional.

## Main theorems (verified in §4–6)

```claim
id: ghosh-dim-bound
statement: For n≥3 and any algebraically closed field K (any characteristic),
  dim ∩_{i=1}^{n−1} X_n^i(K) ≤ 2. Concretely the scheme of shift-equivalence classes
  of CA polynomials is at most 2-dimensional in every characteristic.
hypotheses: K algebraically closed, any characteristic, n≥3
holds-here: yes
status: accepted-at-AJM (peer-reviewed acceptance for the finiteness/dimension bound;
  the proof was flagged & fixed after Schaub–Spivakovsky pointed out a gap in an
  earlier version — see acknowledgement §1.3)
bearing: Regardless of the unproved status, this is the strongest *established-in-principle*
  structural bound on counterexample varieties. It shows CA(degree n) reduces to
  "the 1-dimensional piece is empty." Not being char-specific, it CANNOT be the whole
  proof (CA is false in char p) — consistent with CA being open.
anchor: research/sources/ghosh2024_finiteness_html.full.md (Theorem A = 5.6, §5)
falsifies: a held counterexample of dimension >2, or a peer-review refutation.
```

```claim
id: ghosh-finiteness
statement: X_n is a finite Z-scheme of dimension ≤1 for all n≥3, hence affine; the
  arithmetic CA scheme has finitely many K-rational points over any field K. Concretely,
  for each n there are at most finitely many counterexamples to CA in degree n up to
  affine transformations, over any field of any characteristic.
hypotheses: n≥3, any field
holds-here: yes
status: accepted-at-AJM (Corollary 5.7, 5.8, 5.11), peer-reviewed acceptance
bearing: The run should not hunt an infinite family of counterexamples; there are only
  finitely many per degree. A dimension-0/empty proof for a given n is the whole of CA_n.
anchor: research/sources/ghosh2024_finiteness_html.full.md (Thm B=5.7, Cor C=5.8)
falsifies: an infinite family of counterexamples of a fixed degree over some field.
```

```claim
id: ghosh-complete-intersection
statement: The intermediate arithmetic CA schemes X_n[j] (1≤j≤n−1, with X_n[n−1]=X_n)
  have K-points forming an almost complete intersection over any algebraically closed K;
  CA in degree n over char-0 is equivalent to X_n being a complete intersection. Moreover
  j_C(n) ≥ q(n)−1 where q(n) = largest number ≤ n of the form p^k or 2p^k (Theorem E).
hypotheses: K alg. closed; char-0 for the j_C result
holds-here: yes
status: asserted-by-source (Theorem E = Cor 6.8, §6)
bearing: Gives the run a concrete measure of how far a degree is from forcing collapse:
  the largest j for which the intermediate scheme is a complete intersection. Degree 20
  (q(20)=16) has j_C(20) ≥ 15. Recovering/refining this is a real partial target.
anchor: research/sources/ghosh2024_finiteness_html.full.md (§6)
falsifies: a peer-review refutation or a computation showing a larger j for some n.
```

## What it does not settle
The theorems leave the final "1-dimensional piece is empty" step unproved — that is CA. The 2-dim bound holds in all characteristics, so by itself it cannot rule out the char-p counterexamples; the characteristic-0 content must live in a further step the paper does not supply. **This is exactly the void the run's own scheme argument would have to fill.** The finiteness result (dim-bound, finiteness, complete-intersection) is now **peer-reviewed, accepted for publication in the American Journal of Mathematics** (2026, per Hopkins Press list and the author's UW page) — separating it clearly from the full claimed proof (arXiv:2501.09272), which remains an unverified 0-citation preprint and is NOT accepted anywhere.
