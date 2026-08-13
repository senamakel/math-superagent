# Bound on the HMS Theorem 1.1 effective constant C — the precise obstruction

**Question (TASKS.md blocking):** can an explicit numerical value be extracted for
the effective constant C in Harrison–Mudgal–Schmidt Theorem 1.1 (AP length ≤ C^(1+r)
on E/Q)? If not, record the exact dependency chain and the obstruction to computing a
number.

**Answer: No explicit value exists in any source on disk, for C or for any of its
three ingredients.** The paper's proof is *effective* (following it yields a number),
but the computation is not carried out anywhere, including in the three ingredient
sources. The obstruction is that two of the three ingredients have no numeric constant
stated anywhere the run can reach, and the third — the only genuinely explicit one — is
paywalled and not on disk.

Sources used (none fetched new): the full HMS text
`research/sources/harrison-mudgal-schmidt-sum-product-bremner-2026.html.full.md`
(§3.4 Theorem 3.7, §4 Lemma 4.3, §7), the DP07 acquisition record
`research/summaries/david-philippon-minorations-puissances-courbes-elliptiques-2007.md`,
and the DP07-adjacent tier on disk: Galateau 2016 habilitation, Viada 2007, Gao survey.

---

## The exact dependency chain for the elliptic-curve constant

Proof chain for Theorem 1.1 (verified against the §7 text):

```
Theorem 1.1  (AP/GP/consecutive-squares in E(Q)-coordinates, |A| ≤ C^(1+r))
  ⇐  Corollary 2.2   (proper GAP of rank k in 𝒞(Γ): |P| ≤ D(d)^(1+r))
      — proof of Theorem 1.1 sets G = E, H = 𝔾_a, 𝒞 = graph of (x,y)↦x,
        so the relevant degree is small and fixed (d = deg of the x-map)
  ⇐  Theorem 2.1   (𝒞₁(A)+⋯+𝒞_g(A) ≥ c(d,g)^(1+r)·|A|^g)
  ⇐  Theorem 4.2   (projection image ≥ c(g,deg 𝒱)^(1+r)·|A|^g)
      — via Prop 5.1 (𝒱_sum non-degenerate)
  ⇐  Lemma 4.3  +  Lemma 4.4 (Schwartz–Zippel)  +  Theorem 3.7
```

The three ingredient constants that enter C:

### 1. DP07 — David–Philippon `[11, Théorème 1.13]`
- **What it is:** the uniform Mordell–Lang bound with a *completely explicit* constant
  for subvarieties of self-products E^g of a single elliptic curve. HMS Theorem 3.7
  states it as: for any subgroup Γ ⊆ G^g(C) of rank r that is a finite-rank group,
  `|𝒱^co ∩ Γ| ≤ C(d,g)^(1+r)`, and "if G is an elliptic curve then this theorem
  follows **directly** from [11, Théorème 1.13]". It is the **sole**
  Diophantine-geometry input in the elliptic-curve case; nothing else (no Laurent, no
  ESS S-unit bounds) is needed for E, those serve the 𝔾_m case of Theorem 3.7 only.
- **Numeric value on disk: NONE.** HMS gives no expression. DP07 primary text is
  paywalled (OUP 403 on every route; no arXiv; not in HAL) — claim
  `dp07-primary-text-not-obtainable-this-cycle`, checked. The DP07-adjacent tier on
  disk (Galateau 2016, Viada 2007, Gao survey, GGK) *confirms* DP07 is the only
  explicit-constant uniform-ML result of this shape, but **none of them states the
  numeric constant** — each is survey/technique level. Per GGK/Gao it is the unique
  lane that could deliver a real number.
- **Where the number would come from:** Théorème 1.13 of rpm006, specialised to the
  correspondence 𝒞 = {(P, x(P))} ⊆ E × 𝔾_a (Example 3.5) — i.e. the subvariety giving
  AP-in-x-coordinates on E.

### 2. BZ — Bombieri–Zannier `[2, Lemma 2]`
- **What it is:** *not* the weak-PFR "BZ". In the §7 proof of Theorem 1.1 the
  constant is the subgroup-count bound of Bombieri–Zannier's "Heights of algebraic
  points on subvarieties of abelian varieties" (Ann. Sc. Norm. Super. Pisa 23, 1996).
  Used in **Lemma 4.3**: the algebraic subgroups H appearing in a maximal translate of
  a fibre 𝒱_Q belong to a *finite* set {H₁,…,H_ℓ} with `ℓ ≪_{g,deg(𝒱)} 1` — an
  effective bound on the *number* of possible subgroups, a function of the degree.
- **Numeric value on disk: NONE.** The BZ paper is not in the library, and HMS gives
  only the ≪_winding "ℓ ≪_{g,deg 𝒱} 1" (implicit constant, not exhibited).
- **Note on the earlier digest:** the prior claim text "C built from David–Philippon +
  PFR constants" was **corrected** in the summary — the §7 proof of Theorem 1.1 uses
  **no** weak-PFR. The 140/110 PFR constants (Lemmas 6.2–6.6) feed only the
  sum-product theorems 1.3/2.3, which are **not** in the Corollary 2.2 → Theorem 1.1
  chain. So "BZ = PFR constant" is wrong for this C; BZ = Bombieri–Zannier.

### 3. JS — Jones–Schmidt `[27]`
- **What it is:** the sub-Pfaffian complexity bound of Jones & Schmidt, "Pfaffian
  definitions of Weierstrass elliptic functions" (Math. Ann. 379, 2021). Used in
  **Lemma 4.3**: the graph of exp_G restricted to a fundamental domain is a
  sub-Pfaffian set "of complexity bounded by an **absolute (effectively computable)
  constant**", used to bound the complexity (hence degree) of the exceptional set
  Z^H. It is what makes the degrees in Lemma 4.3 effective rather than merely
  existential.
- **Numeric value on disk: NONE.** HMS calls it "absolute (effectively computable)" and
  never exhibits it; the JS paper is not in the library.

---

## Verdict per ingredient

| Ingredient | Source | Explicit numeric value on disk? | Status |
| --- | --- | --- | --- |
| DP07 constant (Thm 1.13) | David–Philippon IMRP 2007 | **No** — primary paywalled & unobtainable this cycle; survey tier confirms existence but gives no number | genuinely explicit in the original; not reachable |
| BZ constant (Lemma 2) | Bombieri–Zannier 1996 | **No** — HMS gives only "ℓ ≪ 1", implicit constant | effective in principle only |
| JS constant (Pfaffian complexity) | Jones–Schmidt 2021 | **No** — HMS says only "absolute (effectively computable)" | effective in principle only |

## Conclusion and precise obstruction

**The paper's proof IS effective, but the computation of C is not carried out — and
cannot be carried out from anything on disk.** To compute C one would need exactly
three numbers, and none is available:

1. **The DP07 constant** from Théorème 1.13 of rpm006, specialised to
   𝒞 = {(P, x(P))} ⊆ E × 𝔾_a (the AP-in-x-coordinates correspondence). This is the
   only ingredient with an actually-explicit constant in its source, and that source
   is paywalled — open request `dp07-explicit-constant-for-e3-ap`. **This is the
   binding obstruction.**
2. **The Bombieri–Zannier subgroup-count bound** ℓ = ℓ(g, deg 𝒱) from [2, Lemma 2] —
   an explicit function of degree; the BZ paper is not on disk and HMS does not exhibit it.
3. **The Jones–Schmidt absolute sub-Pfaffian complexity constant** from [27] — declared
   "absolute (effectively computable)" with no value.

The obstruction is therefore **not** that HMS's constant is inefficient in principle —
the proof produces a number. The obstruction is that the number is a function of three
sub-constants, one of which (DP07) lives in a paper this run cannot obtain, and the
other two (BZ, JS) are asserted effective without even being stated as explicit
expressions in the paper that uses them. Nothing on disk closes this; the claim below
records it.

Consequence for the MSS run (unchanged): the inequality C^(1+r) < 3 cannot be
evaluated. Even granting the DP07 constant were small, `C^(1+r) < 3` already requires
C < 3 for r=0 and C < √3 ≈ 1.733 for r ≥ 1, and every quantitative uniform-ML constant
in this chain is known to be far larger than either. The uniform-height approach
survives only as "an effective bound exists and is formally decidable"; the next lane
remains obtaining DP07's actually-explicit constant, not this paper.

```claim
id: hms-constant-nonextractable-on-disk
statement: No explicit numerical value for the HMS Theorem 1.1 effective constant C is
  present in any source on disk, nor for any of its three ingredients. The §7 proof of
  Theorem 1.1 composes exactly three Diophantine-geometric constants: (1) the
  David–Philippon uniform-Mordell–Lang constant from [11, Théorème 1.13], specialised to
  the x-coordinate correspondence {(P,x(P))} ⊆ E × G_a (the SOLE input for the
  elliptic-curve case); (2) the Bombieri–Zannier subgroup-count bound ℓ << 1 from
  [2, Lemma 2] (implicit constant); (3) the Jones–Schmidt absolute sub-Pfaffian
  complexity constant from [27] (stated only as 'absolute (effectively computable)').
  The weak-PFR constants (140, 110) are NOT in this chain — they feed only the
  sum-product theorems 1.3/2.3, correcting the earlier digest.
hypotheses: E/Q in Weierstrass form; C absolute, independent of a,b; proof chain
  Theorem 1.1 <= Corollary 2.2 <= Theorem 2.1 <= Theorem 4.2 <= Lemma 4.3 + Theorem 3.7
holds-here: yes — the MSS AP {a-b,a,a+b} of x(2Q_i) is an AP in X, so a putative MSS
  needs 3 <= C^(1+r(E_e)); the constant that would decide it is exactly this uncomputed C
status: checked (verified directly against the HMS full text §3.4/§4/§7; all three
  ingredient sources confirmed absent of numeric values on disk)
extractability: effective-in-principle, unexecuted — the proof yields a number, but no
  value is stated in HMS or in any source on disk
obstruction: DP07 primary text not obtainable this cycle (OUP paywall, claim
  dp07-primary-text-not-obtainable-this-cycle); BZ and JS are asserted effective by HMS
  without being given even as expressions; no value for any of the three exists in the
  library
what-three-numbers-needed:
  1. DP07 [11, Thm 1.13] constant for the x-coordinate correspondence in E^g
     (binding — that paper is paywalled),
  2. Bombieri–Zannier [2, Lemma 2] subgroup-count bound as a function of degree,
  3. Jones–Schmidt [27] absolute sub-Pfaffian complexity constant.
bearing: the task 'bound the HMS constant C' is answered in the negative; the run should
  record the dependency chain as the obstruction and keep open request
  dp07-explicit-constant-for-e3-ap as the only lane toward a number; C^(1+r) < 3 remains
  unevaluable
contradicts: hms-cor-2-2-gm-ap-bound-vacuous-at-length-3 (no — that claim concerns the
  Gm/Phi application, degree d=5, vacuity at length 3; the present claim concerns the
  elliptic/AP case and the extractability of the constant, not vacuity)
answers: hms-constant-bound (as 'no numeric value extractable'; precise obstruction
  recorded)
anchor: code/out/hms_constant_bound.md
```
