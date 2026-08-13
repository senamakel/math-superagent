# Library cycle summary — binary-digit thread grounding and near-collision completeness

## What this cycle added

1. **Blokhuis–Brouwer–de Weger 2017 preprint** ("Binomial collisions and near
   collisions", aeb.win.tue.nl/preprints/binomcoll.pdf) — the preprint form of
   the held INTEGERS A64 paper, with the full sieve algorithm, the complete
   d=1 near-collision table (20 entries), and seven infinite families of near
   collisions. Full text:
   `research/sources/brouwer-binomial-collisions-near.full.md`; summary:
   `research/summaries/brouwer-binomial-collisions-near.md`.
   - Confirms the collision list: 3003 = C(78,2)=C(15,5)=C(14,6); six sporadic
     (120, 210, 1540, 7140, 11628, 24310); the infinite Lind/Singmaster/Tovey
     family. Same parametrization as the run's family (verified by substitution;
     runnable checker `code/librarian_check_family_forms.py` NOT yet executed).
   - Theorem 2.2: no unknown collisions for the solved (k,l) pairs, for
     (m,l)=(n-1,k+1),(n-1,k+2),(n-2,k+1), for n ≤ 10^6, and value ≤ 10^60.
   - The `A(k,p)` polynomial-image sieve (image size ≈(1-e^-1)p odd k,
     ≈(1-e^-1/2)p even k) is a reusable elementary tool; feeds the
     binary-digit/Lucas attack line.

2. **Rowland 2017 survey** ("Binomial coefficients, valuations, and words",
   ericrowland.github.io) — the base-p digital machinery: Kummer, Lucas,
   Glaisher 1899 (2^{popcount(n)} odd entries per row), Fine 1947, Rowland's
   matrix theorem (exact polynomial for the nonzero-mod-p^α count).
   Full text: `research/sources/rowland-binomial-valuations-words.full.md`.
   **Finding for the binary-digit thread:** this entire literature counts how
   many coefficients are odd / nonzero mod p^α, NOT how often one integer value
   recurs across rows. The thread's stated gap (odd-triangle *value*
   multiplicity) survives the literature search; the n ≤ 2^18 odd-triangle scan
   probes genuinely unstudied territory. Recorded in
   `research/threads/binary-digit.md`.

3. **Lane 2023** (arXiv:2309.12942) — explicit error term on the
   Barat–Grabner equidistribution of residues mod p across the first n rows.
   Adjacent distributional benchmark: for p=2 vacuous (one nonzero residue), so
   it does not touch the odd-value multiplicity question; useful for general-p
   partial-statistics analogues.

4. **Near-collision completeness cross-check:** Katsipis 2019 (already held)
   resolves the remaining d=1 cases (6,3),(3,6),(8,2), completing the
   Blokhuis–Brouwer–de Weger d=1 conjecture. GRKTU 2019 (held) solves
   C(n,k)=C(m,l)+d for d ∈ [-3,3] on the eight solved pairs.

## Status

- No open REQUESTS file exists in this session's toolset; requests would come
  through the summaries/claims machinery.
- The nearest open thread is `binary-digit`; its first computational step
  (odd-triangle scan to 2^18) remains unrun and is now confirmed to be
  exploring unstudied territory.
- Singmaster 1971 (AMM 78) remains unobtained (paywalled); its content is
  attested by held primaries (FQ 1975, AEH 1974, GRKTU 2020).
- Tian 2025 (MDPI) remains 403-blocked; recorded in
  `research/summaries/claimed-resolutions-2025-2026-caution.md`.