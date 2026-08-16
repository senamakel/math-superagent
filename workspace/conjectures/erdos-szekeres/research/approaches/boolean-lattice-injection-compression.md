```approach
idea: Points inject into the Boolean lattice B_{n-2}; prove it by compression (LYM/Sperner/Kleitman)
mechanism: The ES construction is literally the Boolean lattice realized geometrically: point ↔ subset S ⊆ [n−2], block i = the C(n-2,i) subsets of size i, arranged so convex position corresponds to a chain/flag. So ES(n) ≤ 2^{n-2}+1 is exactly the statement "every no-convex-n-gon set injects into B_{n-2}", and the conjecture is that B_{n-2} is the unique extremal object. The mechanism: assign each point p a full profile Prof(p) ⊆ [n−2] — the set of intermediate sizes ℓ at which p sits atop a cup/cap staircase — and prove Prof is injective, with two points sharing a profile exactly a convex n-gon. The classical cups/caps proof keeps only the cardinality pair (cup, cap), whose count ≈ 4^n is provably lossy (ms-cups-caps-tight); keeping the full subset profile is the information that recovers the 2^{n-2} constant. The proof machine is compression/shifting: if Prof is monotone under a suitable order, a monotone injection into the subset lattice subject to the chain condition forces N ≤ 2^{n-2} by the LYM/Sperner inequality applied to the induced flag. Speculative core: the profile map is monotone and the collision condition is exactly "convex n-gon" — this is the claim to attack first.
status: refuted
killed-by: The stated "close with LYM/Sperner" step cannot deliver the bound, and the "B_{n-2} is the unique extremal object" premise is false.
precedent: >
  (a) The premise that B_{n-2} is the UNIQUE extremal object is contradicted by the
  literature: there are many non-isomorphic 2^{n-2}-point no-convex-n-gon constructions.
  Baek & Balko, "The Erdős–Szekeres Conjecture Revisited" (SoCG 2025,
  doi:10.4230/lipics.socg.2025.13) prove the ES conjecture for DECOMPOSABLE sets and give a
  general blow-up method generating "new constructions ... generalizing all previously known
  constructions" of 2^{n-2}-point no-k-gon sets (incl. Horton-type and Valtr-type), showing
  the extremal family is a broad class, not the single Boolean-lattice object. Damásdi–Dong–
  Scheucher–Zeng (SoCG 2024, doi:10.4230/lipics.socg.2024.46: "Saturation results around the
  Erdős–Szekeres problem") also construct distinct saturated sets at (7/8)·2^{n-2} and confirm
  the ES construction is saturated — the extremal/pre-extremal sets are not unique. Károlyi–
  Tóth (DCG 2012, doi:10.1007/s00454-012-9424-6) build recursive "twin" order types with
  controlled convex-position properties, further non-isomorphic examples. So "conjecture =
  B_{n-2} unique extremal" is not supported; the object is a rich family.
  (b) The proof mechanism "close with LYM/Sperner" cannot yield 2^{n-2} as stated. Sperner's
  theorem bounds an ANTICHAIN in B_{n-2} by C(n−2, ⌊(n−2)/2⌋) ≈ 2^{n-2}/√(n−2), and the k-Sperner /
  chain versions give larger-than-2^{n-2} bounds — none of the LYM/Sperner/Kleitman
  inequalities produce a family bound of exactly |B_{n-2}| = 2^{n-2}. (For reference: Sperner
  1928; Erdős 1945 k-Sperner; the chains/antichain extremal literature e.g. Patkós
  doi:10.37236/4644, Das–Gan–Sudakov doi:10.1017/s0963548314000273.) So if the run wants the
  full 2^{n-2}, the bound MUST come from the injectivity Prof(p) being a genuine bijection
  onto B_{n-2}, NOT from a Sperner/LYM inequality on top of injectivity — the compression step
  as written would only give a smaller antichain-sized bound, which is the WRONG direction
  (it would contradict the 2^{n-2} lower bound). The Bowden–Kapron–Tardos "happy ending"
  partial-injection idea for the weaker 2^{n+O(√(n log n))} bound exists in spirit (the Suk
  argument assigns labels/partial orders), but no exact injectivity proof is published.
first-step: Define Prof(p) precisely as { ℓ : p is the apex of an ℓ-cup-tower and an (n−ℓ)-cap-tower } (or the staircase analogue via the 4-point criterion); compute Prof on the ES construction (target: bijection onto B_{n-2}) and on small extremal sets via the oracle; then hunt the smallest two-point set that shares a profile without a convex n-gon — the monotonicity/collision claim is falsified the moment such a pair exists. REDIRECT: because the uniqueness premise is false and Sperner cannot give 2^{n-2}, the only surviving version is "Prof is an injective bijection onto B_{n-2}" used as a polarization/antichain-decomposition tool — check it against the Baek–Balko non-decomposable examples first, which may already break injectivity.
```

## Literature report — Boolean-lattice injection / compression

**What the reformulation is called.** The ES construction as the Boolean lattice realized
geometrically; "profile" / flag / chain condition; compression via LYM/Sperner/Kleitman.
This is the *extremal-set (poset) theory* reformulation: identify points with subsets and
try to bound the family size by a subset-lattice extremal result.

**Precise statements / premises found.**
- *Sperner (1928):* a family of subsets of [n] with no inclusion (antichain) has size ≤
  C(n, ⌊n/2⌋) ≈ 2^n/√n. *Erdős (1945):* a family with no (k+1)-chain has size = the sum of
  the k largest binomial coefficients — ≥ 2^{n-2}, not a route down to it. *Kleitman / LYM:**
  various. None of these yields a strict ≤ 2^{n-2} family bound = |B_{n-2}|; in fact the
  k-Sperner bounds are ≥ 2^{n-2}. So the compression step as written would produce the wrong
  inequality (too small, contradicting the 2^{n-2} lower bound) or too large. The bound must
  be the injectivity itself (a genuine bijection onto B_{n-2}), not a Sperner/LYM cap.
- *Uniqueness is false.* Baek–Balko (SoCG 2025, doi:10.4230/lipics.socg.2025.13): blow-up
  constructions give a broad family of 2^{n-2}-point no-k-gon sets, generalizing Horton/Valtr;
  the ES conjecture holds for decomposable sets but the extremal family is not the single
  Boolean lattice. Damásdi–Dong–Scheucher–Zeng (SoCG 2024): distinct saturated sets.
  Károlyi–Tóth (2012): recursive twin order types. So "B_{n-2} is the unique extremal" is not
  supported.

**Has anyone applied this to THIS problem?** The Suk argument and its refinements assign
partial orders / labels to points and count via cups/caps in a way that is morally "each
point carries a small amount of structural info," reaching 2^{n+O(√(n log n))} — but no
published proof forces an exact injective embedding into B_{n-2} and closes the conjecture.
No exact-injectivity (polarization) proof is in the literature.

**What it would buy.** If Prof were an injective map into B_{n-2}, then |set| ≤ 2^{n-2}
follows immediately — exactly the conjecture. That is a clean target. But (a) the map as
defined (apex of cup/cap towers of all intermediate sizes) is not established to be
injective, is not established to be monotone, and is contradicted-in-spirit by the
non-uniqueness of extremal sets; (b) the compression step adds nothing (Sperner cannot
deliver the bound) and misstates the mechanism.

**Verdict: refuted as stated** — the uniqueness premise is false and the LYM/Sperner
closing step is in the wrong direction. The only surviving fragment is the exact-injectivity
claim itself, which the run should test against the Baek–Balko non-decomposable examples
first; if a non-decomposable 2^{n-2}-point no-k-gon set breaks injectivity, the whole
approach is closed.
