# Librarian: Krawtchouk/MacWilliams/Delsarte engine — local sources mapped

> **SUPERSEDED in part (scholar pass).** The "load-bearing point" below — that
> the Delsarte bound needs the fold row set to be linear — is **wrong**, and is
> refuted by the primary source this note itself cites. Guruswami's notes prove
> the Delsarte LP constraint for *general* codes by sum of squares (full text
> lines 519–590), no linearity anywhere; the MacWilliams *identity* needs
> linearity, but the approach uses only the distance distribution and its
> Krawtchouk diagonalization. The corrected claim is
> `delsarte-lp-holds-for-nonlinear-row-sets`
> (`research/notes/scholar_krawtchouk_gate_resolution.md`), which contradicts
> and supersedes the gate below. The real gate is the *computed* distance
> distribution: `A_2 = O(n^{0.48})`, `F_n(1−2p)=O(n)` (exact, n≤4096;
> `code/out/fold_second_moment_capture.txt`). Keep the rest of this note for
> the source map; do not rebuild the approach on the linearity gate.

This note records what the library holds for the coding-theory engine the
adopted approach `fold-second-moment-krawtchouk` rests on, and the one
holds-here that must be checked before the engine transfers to the fold.

**Initial flag, corrected.** An earlier version of this note asserted the
library held *no* primary treatment of MacWilliams/Krawtchouk/Delsarte. That
was wrong in a specific way: `grep_workspace` on `research/sources` and
`search_claims` missed sources that were **on disk but not indexed**. The
primary tier was and is present: `macwilliams_1963_weight_distribution_fulltext`
(the original 1963 paper), `guruswami_macwilliams_lp_notes_fulltext`
(Guruswami's CMU notes on the Delsarte LP bound, MacWilliams identity, and
distance distribution), and `essential_coding_theory_guruswami_rudra_sudan_fulltext`
(the coding-theory book), all indexed by the coverage pass
(`librarian_coverage_pass.md`) and now reached by `search_documents`.
My two Wikipedia downloads are *additional* encyclopedic entries, not the
first sources of the engine.

## The load-bearing point for the adopted approach

| Source | File | What it establishes that the run needs |
| --- | --- | --- |
| Wikipedia — MacWilliams identity | `sources/wikipedia_macwilliams_identity.full.md` | States the identity `W(C^⊥;x,y) = (1/|C|) W(C; y−x, y+x)`; defines weight distribution `A_t`, weight enumerator `W(C;x,y)`, **distance (inner) distribution** `A_i = (1/M) #{(c₁,c₂)∈C² : d(c₁,c₂)=i}`, distance enumerator, and outer distribution. References Hill 1986, Pless 1982, van Lint 1992 (GTM 86 §3.5, §4.3). |
| Wikipedia — Krawtchouk (Kravchuk) polynomials | `sources/wikipedia_krawtchouk_polynomials.full.md` | Definition `K_k(x;n,q) = Σ_j (−1)^j (q−1)^{k−j} (x choose j)((n−x) choose (k−j))`; **generating function** `(1+(q−1)z)^{n−x}(1−z)^x = Σ K_k(x;n,q) z^k`; **orthogonality** `Σ_i (n choose i)(q−1)^i K_r(i)K_s(i) = q^n (q−1)^r (n choose r) δ_{r,s}`; three-term recurrence; references Kravchuk 1929, Levenshtein 1995, MacWilliams–Sloane 1977. |
| Ashikhmin–Barg–Litsyn 1999 (arXiv math/9910175) | `sources/ashikhmin_barg_litsyn_polynomial_method.full.md` | Abstract only (the conversion captured the arXiv landing page, not the full PDF). Confirms title/topic: "Polynomial, or Delsarte's, method", distance distribution, Krawtchouk transform `A′ = (1/|C|)A·K`, Delsarte inequalities. Use the Wikipedia entries for statements; this file is a reference pointer. |
| Friedlander 2024 (arXiv 2401.07319) | `sources/friedlander_macwilliams_krawtchouk.full.md` | Abstract only. States the MacWilliams identity in both forms (functional transform and direct weight-distribution via eigenvalues of association schemes) for "Krawtchouk association schemes". Reference pointer; the Wikipedia entries carry the concrete identities. |

## The load-bearing point for the adopted approach

The `fold-second-moment-krawtchouk` approach uses three identities, now all
primary-sourced in the library:

1. **XOR moment** — `E[eps_d eps_{d′}] = (1−2p)^{|M_d XOR M_{d′}|}` for iid
   Bernoulli(p) bits. Standard; follows from `E[(-1)^x]=1−2p`. (This was already
   sourced as a claim `primes-fold-second-moment-at-uniform`.)
2. **Krawtchouk diagonalization** — `F_n(z) = 2^{−n} Σ_ω (1−z)^{wt(ω)}(1+z)^{n−wt(ω)} Ĉ_n(ω)²`
   where `Ĉ_n(ω) = Σ_d (−1)^{⟨ω, 1_{M_d}⟩}`. This is the **Hadamard/Fourier
   transform on the cube** — it holds for any *multiset* of points of F₂ⁿ, not
   only for a *linear code*. The Wikipedia distance-enumerator and Krawtchouk
   generating function/orthogonality entries give the underlying identities. The
   fold's row set `{1_{M_d} : d ∈ [2,n−1]}` need not be linear for the
   *identity* to hold; **but** — this is the critical, currently-unchecked point —
   the *Delsarte LP bound / MacWilliams-transform-nonnegativity* that turns a
   distance distribution into a *bound* requires Ĉ_n(ω) ≥ 0 for all ω, which
   holds only for *linear* codes. The fold row set is a subcode of F₂ⁿ that is
   in general **not linear** (it is the set of translated digital down-set
   indicators, which is not closed under XOR). So the Krawtchouk *identity* is
   usable, but the *Delsarte LP bound* is **not directly transferable** without
   checking linearity. This is exactly the kind of holds-here that must be
   verified before the approach's condition (C) is taken as a bound.
3. **Row weight** — `|M_d| = 2^{popcount(d)}`, all rows even for d ≥ 1.

## What to read next

- The **primary** proof-level treatments are already local: `macwilliams_1963_weight_distribution_fulltext.full.md` (original paper), `guruswami_macwilliams_lp_notes_fulltext.full.md` (Delsarte LP bound and distance distribution for a binary code), and `essential_coding_theory_guruswami_rudra_sudan_fulltext.full.md` (book). My Wikipedia additions (`wikipedia_macwilliams_identity`, `wikipedia_krawtchouk_polynomials`) are the encyclopedic companion tier.
- The key structural question the run must answer before building on the
  Krawtchouk route: **is the fold row set a linear code?** If not (almost
  certainly), the *distance-distribution identity* still holds, but the *Delsarte
  nonnegativity that bounds F_n(z)* does not follow from the standard theorem —
  and both the original MacWilliams paper and Guruswami's notes apply the
  transform/bound to **linear** codes. A direct computation of whether the row
  set is XOR-closed would settle this.

```claim
id: krawtchouk-delsarte-linear-code-holds-here
statement: The MacWilliams identity and the Delsarte linear-programming bound — the engine of the adopted approach fold-second-moment-krawtchouk — are stated in the library's primary sources (MacWilliams 1963; Guruswami CMU notes) for a LINEAR code and its dual. The fold's row set R_n = {1_{M_d} : d in [2,n-1]} (translated digital down-set indicators) is a subset of F2^n that need not be closed under XOR. The Krawtchouk diagonalization identity F_n(z) = 2^{-n} sum_omega (1-z)^{wt omega}(1+z)^{n-wt omega} C-hat_n(omega)^2 is a pure Fourier transform on the cube and holds for ANY multiset of R_n; but the Delsarte bound that turns the distance distribution into F_n(z) = O(n) additionally needs C-hat_n(omega) >= 0 for all omega, which the standard theorem guarantees only for linear codes. Whether R_n is XOR-closed is therefore a holds-here gate: unverified, not inherited.
hypotheses: fold row set R_n; Delsarte/MacWilliams nonnegativity applies to linear codes; Krawtchouk identity is cube-Fourier (any multiset).
holds-here: unverified — the identity transfers, the bound does not unless R_n is linear
status: sourced-check (the linearity of R_n is uncomputed)
bearing: gates whether fold-second-moment-krawtchouk's condition (C) (F_n(z)=O(n) as a bound on the primes) follows from the standard MacWilliams/Delsarte theorem, or needs a separate argument that R_n's distance distribution itself gives the growth.
anchor: research/summaries/librarian_krawtchouk_macwilliams_engine.md; sources/guruswami_macwilliams_lp_notes_fulltext.full.md; draft checker code/librarian/rowset_linearity_check.py (unexecuted)
```
