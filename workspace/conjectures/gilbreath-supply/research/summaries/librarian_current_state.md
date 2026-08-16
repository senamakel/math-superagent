# Librarian current-state report — reopened pass

Reopen reason: the first pass closed claiming "equivalence to switch density is
the indicated answer"; a dedicated run refuted the collapse mechanism with an
explicit witness, so the run reopened to answer *whether any order-K (1<K≲n/2)
functional of the fold is controllable by an arithmetic input strictly weaker
than pointwise mod-4 switch density*.

## Library maturity assessment

Phase-1 is complete (`research/ROOT.md` meets its test: minimal-counterexample
structure, verification bounds, three settled restricted classes). The reopened
pass's scholar has already digested the higher-order (K>1) tier. Verified this
pass by reading the digests directly:

- **Lacasa et al. 2018 (arXiv:1802.08349)** — unconditional forbidden-block
  enumeration in the prime-gap sequence mod 6 at every order m>1, with the
  counting law |F(m)| = 3^m − 2^{m+1}. This is the strongest **unconditional**
  K>1 structure on the gap sequence. Digest: `summaries/lacasa_dynamical_prime_sequences.md`;
  the *negative projection transfer* (mod-6 structure destroyed by the mod-4
  parity projection) is recorded in `notes/lacasa_parity_projection_transfer.md`.
- **Wu 2019 (arXiv:1908.07095)** — the direct K>1 companion: length-k (k≥2)
  consecutive-prime residue-pattern frequencies are open at every order, only
  the constant patterns unconditional (Shiu/Maynard). Digest:
  `summaries/wu_nonuniform_residues_prime_sequences.md`. This is the precise
  form the parity barrier takes at every order — exactly the wall any K>1
  functional faces.

## Inventory (current, verified by grep this pass)

- **52 full texts** in `research/sources/`, each with its source URL on line 1
  (`<!-- source: … -->`). All search-reachable via `search_documents`.
  (One is a deliberate stub: `matomaki_radziwill_tao_averaged_chowla.full.md`,
  a "wrong download" pointer whose real paper is correctly filed as
  `matomaki_radziwill_tao_fourier_uniformity_averaged.full.md`. It exists only
  so nobody re-fetches the wrong arXiv ID.)
- **72 digests** in `research/summaries/`, carrying claim blocks that feed
  `research/CLAIMS.md`.

Tiers covered: (1) the parity barrier (ABGS 2011, Lau 2024, Lemke
Oliver–Soundararajan 2016, Granville–Martin, Rubinstein–Sarnak); (2) the
equal-residue side / door-3 refutation (Shiu-2000 expository full text, Maynard
2016, Banks–Freiberg–Turnage-Butterbaugh, Freiberg 2010); (3) the fold Φ —
Pascal-mod-2 / Rule-90 / Lucas-submask (Meštrović, Hofer, Bacher, Allouche &
Shallit I & II, Rampersad–Wiebe, Steinhaus triangles, Rowland, Szechtman); (4)
the Walsh/Krawtchouk/MacWilliams/Delsarte tier; (5) the ergodic / Lucas-mixing
tier (Pivato–Yassawi, Pivato, Takei); (6) direct prior work on the exact object
(Odlyzko 1993, Chase 2022) and the encyclopedic tier; (7) the higher-order K>1
tier (Lacasa, Wu) added this reopen.

## Gaps, restated

- The **only** open request, `walsh-spectral-subset-b904`, is a lower bound on
  wt(Φ_n x) for inputs not "complicated" in the five refuted senses. This is a
  *theorem to be found*, not a source: no published result states it, so there is
  nothing to download. It stays open as the load-bearing theorem gap.
- The Shiu-2000 "unsourced" gap recorded in the first-pass CONTEXT.md is
  **resolved**: the freely-available Ethan Yang expository full text
  (`sources/shiu_strings_expository.full.md`) states and proves the quantitative
  theorem, so the door-3 refutation is proved-status, not conditional-on-abstract.

## Housekeeping done this pass

- Described the two files that were `_(undescribed)_` in `code/lib/INDEX.md`:
  `direct_fold.py` (direct submask-XOR oracle: literal definition + subset-XOR
  zeta, the brute cross-check of s_sos) and `submasks.py` (down-set run
  decomposition backing the run-telescope identities).

## Bottom line

The library is complete for every live line of attack and the reopened K>1
territory. No source scarcer than the run's needs exists on the order-K
question — the surviving gap is a theorem (Walsh/subset-sum lower bound), not
literature. Further gathering happens only against a stated gap in
`REQUESTS.md`, per the terminus directive.
