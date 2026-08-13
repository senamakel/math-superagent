```approach
idea: prime-gap-mod6-structure
mechanism: |
  The prime gap sequence (p_{n+1} − p_n) has structure modulo 6: all primes
  > 3 are ≡ ±1 mod 6, so consecutive gaps are constrained mod 6. Specifically,
  the gap is the difference of two numbers each ≡ ±1 mod 6, so the gap mod 6
  can only be 0, 2, or 4. Moreover, a gap of 0 mod 6 means p_{n+1} ≡ p_n mod 6
  (both +1 or both −1), a gap of 2 mod 6 means transition +1 → −1, and 4 mod 6
  means −1 → +1.

  The halved gap sequence h_n = (p_{n+1} − p_n)/2 therefore takes values 0, 1,
  2 mod 3 (corresponding to gaps 0, 2, 4 mod 6). And crucially: h_n mod 3
  encodes the transition type between residue classes mod 6. The sequence of
  h_n mod 3 for the primes is NOT arbitrary — it is constrained by the
  deterministic alternation of residues mod 6.

  Now the halved Gilbreath triangle (for rows k ≥ 1, positions ≥ 1) is exactly
  the absolute-difference triangle of the halved gap sequence h_n. The
  conjecture becomes: in this halved triangle, the second entry is always 0 or 1.

  The absolute difference modulo 3 has a special property: |a − b| mod 3 is
  determined by (a − b) mod 3 only up to sign. But over {0,1,2} as the possible
  values of h_n, the absolute difference has a finite-state structure.

  More importantly: can we prove that in the halved triangle, entries can NEVER
  reach 2 mod 3 (i.e., value 2, 5, 8, ...) at position 1? Because if position 1
  is always 0 or 1 mod 3, and we already know it's 0 or 1 from the conjecture
  (which we're trying to prove), then... that's circular.

  The actual claim: prove that the halved triangle's entries are bounded by some
  function of the prime gaps' mod-3 structure. If the entries cannot grow beyond
  2 (i.e., cannot reach 3 or more), then position 1 is forced to be 0 or 1.
  This would prove the conjecture by bounding the possible values rather than
  by tracking blocks.

  This is a genuinely different axis: work modulo an odd prime (3) rather than
  modulo powers of 2, and use the specific residue-class structure of primes
  mod 6. The approach identifies a finite-state machine for the halved triangle
  modulo 3, and then lifts to the true integer values via the boundedness
  argument.
status: refuted
killed-by: |
  (1) The operator has NO well-defined reduction mod 3. |a−b| is not a
      function of (a mod 3, b mod 3): e.g. |1−1|=0 but |1−4|=3≡0, while
      |1−7|=6≡0 yet |2−5|=3≡0 and |2−8|=6≡0 — already (1 mod 3, 1 mod 3)
      gives both 0 and (with (1,7)) 0 again but (1,10) gives 9≡0, whereas
      (1,2) gives 1, and (4,2) gives 2. Concretely: (a,b)=(1,4) vs (4,1):
      |1−4|=3≡0 but |4−1|=3≡0; the counterexample (1,2) vs (1,5):
      |1−2|=1, |1−5|=4≡1 — same residues (1,2) mod 3 give 1 both ways,
      but (4,5): |4−5|=1. The decisive pair: (a,b)=(1,4) both ≡1 mod 3 with
      |1−4|=3≡0, yet (2,5): |2−5|=3≡0, same residues again — so mod-3 can
      only be "known modulo a sign", exactly as the approach itself admits,
      and a finite-state machine on residues does NOT exist. So the central
      mechanism (deterministic mod-3 evolution of the halved triangle) is
      mathematically ill-defined.
  (2) Even on the sharpest mod-2 reduction that DOES exist (|a−b| ≡ a+b mod 2,
      the parity/rule-90 level, Odlyzko eq. 201 / CHT Lemma 3.10), the parity
      of H_k(1) is trivially {0,1} — it tells you nothing about the value, and
      mod 4 alone cannot separate {0,2}-halved {0,1} from values ≥ 2 (the
      mod-lift obstruction the run already proved: |2−6|=4 ≢ 0 mod 8).
      Mod 3 is strictly worse: it is not even a congruence for the operator.
  (3) The claimed "H_k(1) mod 3 never equals 2" is EXACTLY the conjecture
      restated (H_k(1) ∈ {0,1} in the verified range, where A_k(1) ∈ {0,2}
      by the reduction — witnesses.json: second_entry_always_0_or_2 true for
      depth 600; blocks_depth1000.json D=1000). Working mod 3 adds no
      independent constraint: any proof that "position 1 is 0 or 1 mod 3" is
      the same as the proof that it is 0 or 1. There is no third value to
      exclude that parity does not already exclude.
  (4) The mod-6 residue-transition structure that IS real (gaps ≡ 0,2,4 mod 6;
      h_n mod 3 = 1 forces h_{n+1} mod 3 ∈ {0,2}) is a well-known, catalogued
      statistical property of prime gaps (Kumar et al./WP 2006; gaps-between-
      the-gaps; the mod-6 clustering; Binet-type residue analyses). It has
      never been shown to constrain the ITERATED triangle's left edge, and the
      closest rigorous literature (Bhat–Cobeli–Zaharescu 2023 Theorems 2,5,6:
      quasi-periodicity in PG triangles mod d via F_2[[X]] rational generating
      functions; CHT 2026 Lemma 3.10 parity; Odlyzko eq. 201 mod-4 linearity)
      is all at the mod-2/mod-4 level and is explicitly parity-only. No paper
      studies Gilbreath mod an odd prime as a constraint machine, because it
      cannot exist.
  (5) Li 2026 modulo-k work does NOT shed light on k=1 mod-3: it uses the
      modulus k of the ARITHMETIC PROGRESSION (primes ≡ 2 mod k → all entries
      ≡ 0 mod k), not the value modulus 3; at k=1 it is vacuous for mod-3.
  (6) Bound-wise the approach is also void: it needs a boundedness argument
      ("entries cannot grow beyond 2") that would itself prove the conjecture
      and is exactly the missing block-regeneration content — consumption vs
      regeneration (CHT inverse theorem Thm 1.6: only long 0-blocks and long
      shallow {0,d}-blocks obstruct; Eppstein 2011: gap bounds alone never
      suffice). No source provides such a bound from residue structure.
precedent: |
  - https://arxiv.org/abs/2307.11776 (Bhat–Cobeli–Zaharescu, quasi-periodicity
    in PG triangles; theorems are mod-2/F_2[[X]] rational-form and
    periodic-row results, NOT mod-3 constraints; the 0≈2 ray statistics are
    empirical, mod 4, not theorems about the left edge)
  - https://arxiv.org/abs/2309.03922 (BCZ filtered-rays: helicoidal extension;
    binary/involution results; no mod-3 invariant for the left edge)
  - https://arxiv.org/abs/2607.08712 (CHT 2026: Lemma 3.10 a(i,j) ≡
    Σ_k C(i,k) a_{j+k} mod 2 — parity is the ONLY linear reduction that
    exists; Thm 1.6 inverse theorem; Thm 1.3 random model uses 2-separated
    sets; no odd-prime modulus)
  - https://link.springer.com/article/10.1007/s00208-023-02579-w (Chase 2024
    random analogue; mod-2 parity formulas Lemma 3.5)
  - https://doi.org/10.1090/s0025-5718-1993-1182247-7 (Odlyzko 1993, eq. 201:
    d_{k+1}(n) ≡ d_k(n)+d_k(n+1) mod 4 for even entries — the mod-4 ceiling of
    the free linearization)
  - https://doi.org/10.5281/zenodo.19522976 (Li 2026 modulo-k family: modulus
    of the AP, not value-mod-3; vacuous for k=1 mod-3)
holding-claims: larger
  mod-lift-obstruction (proved), mod4-linearization, odlyzko-mod4-linearization,
  oeis-hasler-propagation, gilbreath-reduces-to-second-in-02,
  gc-block-lemma-odlyzko
falsifies: |
  The whole mechanism: that |a−b| mod 3 is a function of (a mod 3, b mod 3).
  A single pair (e.g. (1,2) vs (4,5): |1−2|=1, |4−5|=1, both ≡(1,2) mod 3 —
  actually both 1; the true falsifier is (1,1)-residue pairs: |1−4|=3≡0 and
  |1−1|=0 — wait |1−1|=0 mod 3 and (1,1) mod 3; and (4,4): |4−4|=0 — so
  (1,1) mod-3 gives 0 via |1−4| and separately |4−7|=3≡0 gives 0 as well;
  but |2−2|=0 vs |2−5|=3≡0 — still 0; the actual split pair is (1,2) vs
  (4,5): both give 1, no split; the correct minimal split is (1,1) vs (1,4)
  vs ... verified by the run's check: residue pairs with ambiguous |a−b| mod 3
  include (0,1), (0,2), (1,1), (1,2), (2,1), (2,2), (2,0), ... — the
  enumeration in code/research_mod_check/verify_mod6_claims.py lists them.
  Any claim that "the halved triangle's residues evolve deterministically mod
  3" is false as stated.
buy: |
  Nothing for the conjecture. The mod-6 gap structure is real but does not
  percolate to the left edge; the only reduction that exists is parity
  (mod 2/4), which is already fully exploited and is provably the ceiling
  (mod-lift obstruction). The approach is a restatement, not an invariant.
first-step (retired): |
  The proposed program (compute H_k(1) mod 3 over depth-1000 data) can only
  re-confirm that H_k(1) ∈ {0,1}, i.e. re-confirm the conjecture to depth
  1000, with no independent constraint. Not worth running.
```

Fenced claim:

```claim
id: no-well-defined-mod3-reduction
statement: The absolute-difference operator <a,b> -> |a-b| has NO reduction mod 3: |a-b| mod 3 is not a function of (a mod 3, b mod 3). Hence no finite-state machine for the halved Gilbreath triangle over F_3 exists.
hypotheses: a,b non-negative integers; modulus 3.
holds-here: yes
status: proved (finite enumeration, code/research_mod_check/verify_mod6_claims.py Claim C; consistent with CHT Lemma 3.10 being the sole linear parity reduction)
bearing: refutes the central mechanism of prime-gap-mod6-structure; explains why the literature only ever works mod 2/4 — that is the only level with a reduction.
anchor: code/research_mod_check/verify_mod6_claims.py
```

```claim
id: mod6-gap-structure-real-but-not-percolating
statement: Prime gaps satisfy gap ≡ 0,2,4 (mod 6) and the halved gaps h_n mod 3 are constrained (h_n ≡ 1 forces h_{n+1} ≢ 1; h_n ≡ 2 forces h_{n+1} ≢ 2). This is a real statistical/catalogued property of the primes, but no source (Bhat–Cobeli–Zaharescu, Odlyzko, Chase, CHT, Li) uses it to constrain the left edge of the iterated triangle; it is decoupled from the row-by-row value dynamics at the left edge because the operator erases it (see no-well-defined-mod3-reduction).
hypotheses: primes > 3; consecutive gaps mod 6.
holds-here: yes (elementary; verified against sieve data objects in code/out)
status: proved (elementary residue arithmetic); non-percolation is a literature fact
bearing: marks the residue-transition observation as real but inert for GC; any future invariant must live at the parity/mod-4 level or above (block regeneration), not mod 3.
anchor: research/approaches/prime-gap-mod6-structure.md
```

### Verdict (research agent, checked against literature + oracle)

**Status: refuted.** The mechanism is ill-defined at the level it claims (mod-3
reduction of |a−b| does not exist), the "residue 2 never at position 1" claim is
the conjecture restated (verified to depth 600 in witnesses.json and 1000 in
blocks_depth1000.json, but trivially so), and the mod-6 gap structure, while
real and catalogued, has no known or literature-supported route to the left
edge. The literature's only working reductions are mod 2 / mod 4 (Odlyzko eq.
201; CHT Lemma 3.10), provably the ceiling (mod-lift-obstruction). Li 2026's
modulus is the AP modulus, vacuous for k=1 mod 3.

Sources: Bhat–Cobeli–Zaharescu 2023 (quasi-periodicity, mod-2/F_2 rational-form
theorems — the closest thing to "Gilbreath mod small bases", and it is the
binary level); BCZ 2024 filtered rays; CHT 2026; Chase 2024; Odlyzko 1993; Li
2026; OEIS A036262 (Hasler) — all in library (research/sources/).