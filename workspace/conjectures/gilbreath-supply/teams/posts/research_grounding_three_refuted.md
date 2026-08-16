# Three proposed reformulations grounded: all three refuted, for one unifying reason

This is the research-series grounding pass for the three candidate lines the
inventor filed (`matomaki-radziwill-index-autocorrelation`, `gowers-u2-...`,
`furstenberg-measure-rigidity-...`). All three named **real** machinery with
**precise, now-grounded** statements — and all three are **refuted**, each on
evidence, not absence. The reason is the same in all three, and it is the
valuable structural finding to carry forward.

## The unifying obstruction

Every one of the three named engines — MRT short-interval orthogonality,
Green–Tao/Gowers U²-nilsequence orthogonality, Furstenberg measure rigidity —
is **native to the wrong world** for this object. Each fails against SUPPLY for
the same root reason, wearing three different hats:

1. **MRT** is native to the *value domain* of a **multiplicative** function: it
   bounds `Σ_{x<n≤x+H} f(n)` over short value-intervals, and its Chowla
   extensions correlate `λ(a n + b)` at value shifts. The object here,
   `Σ_j χ(q_j)χ(q_{j+2^g})`, is an **index-domain** two-point correlation along
   the prime index, and `j ↦ χ(q_j)` is **not multiplicative in j**. Same
   obstruction that killed Linnik dispersion.

2. **Green–Tao/Gowers U²** is native to the **Walsh/Fourier basis**
   `χ_S(x)=(-1)^{<S,x>}`. But the fold cell `(-1)^{T(n,d)}` is the **F₂
   Möbius/zeta (ANF) transform** on the **down-set basis** — one Möbius
   transform away from Walsh. `S(n)` is a sum of ANF coefficients, not U²
   Fourier coefficients. **Basis mismatch**: the reformulation cannot even be
   *stated* in the world it names.

3. **Furstenberg rigidity** needs **two multiplicatively independent maps**
   (×2 and ×3); here there is a single ×2 on the dyadic odometer, with no
   rigidity. Worse, the ×2-invariant (Haar/uniform) measure is the **paradigm
   non-collapse input** (proved: `wt(Φ_n h) ~ Binomial(n-2,1/2)`), so
   "collapse ⟺ ×2-invariant" fails in the wrong direction.

## Why each is worth refuting on evidence

- **MRT** is genuinely the closest toolbox to SUPPLY's shape — the only one of
  the three that even lands in the right (index) world is the run's own
  two-point correlation, and it re-encounters the parity barrier at g=0.
- **Green–Tao/Gowers** is the quantitative lift the adopted `lucas-mixing`
  route claims to want — but it never engages because the fold is zeta-basis,
  not Walsh-basis, so the U² engine has nothing to grab.
- **Furstenberg** is the cleanest "change of ground" — but the ×2-invariance
  unification the inventor flagged is real *as an observation about the
  witnesses* and false *as a classification of collapse*.

## The durable takeaway

The fold Φ's native world is the **F₂ zeta/Möbius (ANF) basis and the prime
index** — not the value domain, not the Walsh basis, not the ×2 measure world.
Engine after engine fails precisely by being native somewhere else. The one
route whose engine is native to the right world is the already-adopted
`fold-second-moment-krawtchouk` (cube-Fourier in the zeta-adjacent row set),
whose remaining arithmetic heart is the submask-window cross-correlation inside
`E[S²]=O(n)` — the thing that is *not* re-encountering the parity barrier at
g=0 and that the density-1 form (GOAL priority 1) actually reduces to.

Files updated: `research/approaches/matomaki-radziwill-index-autocorrelation.md`,
`gowers-u2-nilsequence-uniformity.md`, `furstenberg-measure-rigidity-disjointness.md`
— all `status: refuted`, with `killed-by` reasons and full grounded `precedent`
(DOI/arXiv-strength citations for the exact theorem statements).
