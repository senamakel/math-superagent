# Scholar session report — library digestion for COLLAPSE

## What I did

1. **Read the full workspace context** (GOAL, problem, CONTEXT, FRONTIER,
   REQUESTS, THREADS, the backward/weakened ladders) and every source summary.
2. **Replaced the three remaining template digests** with real summaries that
   either establish facts or say plainly that they do not help, each with a
   fenced `claim` block:
   - `run-length-transform-binomial-mod2-integers` (Wu, INTEGERS 2022): Thm 1
     submask criterion is definitional; **warned that the paper's "run length
     transform" is on the binary index and is NOT this problem's runs inside
     M_d** (a common-source confusion worth flagging).
   - `bacher-chapman-symmetric-pascal-matrices-modp`: established the Thue-Morse
     determinant/char-poly of the *symmetric* Pascal matrix `P(n)=C(i+j,i)`;
     marked `holds-here: no` because `P(n)` is a **different matrix** from
     `Φ_n` — a caution that "Pascal matrix" in the literature usually means a
     different object.
   - `mathonet-rigo-stipulanti-zenaidi` and the Wu 2-regular companion:
     weak bearing (p-automatic vocabulary, odious/evil); the run-length objects
     differ from this problem's M_d runs.
3. **Reconciled an apparent contradiction** in the run: the backward goal
   `collapse-by-evenness` is marked *discharged* (S² is a polynomial in
   adjacent-pair XOR characters, "order 1"), yet the captured G-witness data
   shows S² is *not* constant on lag-1 C_K-fibers and has minimal order
   K*≈n/2. Resolution: these are two different notions of "correlation order"
   — the evenness proof's objects (adjacent XOR *pattern*) are far finer than
   the pinned C_K lag-count *histogram*. Both are consistent; the problem's
   pinned decision object (DEFINITION-OF-CK.md) is the C_K one, so the witness
   data is the operative reading. Recorded as claim-block note and in memory.
4. **Collected the computed results** (which live in code/out) into claim
   blocks with `status: checked`:
   - `pf-s2multiset-rigid`: the multiset {M_d△M_{d'}} is empty×n-2 + every
     other set×2, distinct count = 1+C(n-2,2), verified to n=256, with an
     **independent second route** (bitset vs frozenset census, ALL CHECKS
     PASSED) and broken-run_count negative control. This **answers the open
     request** `reference-that-establishes-5a15` on the *counting* side.
   - `g-witness-order` / `g-witness-intermediate`: no witness at full pair
     order (K=n-1) for n≤16; witnesses exist for K<K*; negative control fires.
   - `g-evenness-collapse`: ker={0,all-ones}, S even under complement.
5. **Catalogued code/out/** — described 20+ previously-undescribed computation
   files and refreshed the index, including flagging `witness_hunt_n20.txt` as
   an EMPTY (failed) capture and several scripts whose outputs are NOT captured
   (pf_kstar_extend, pf_kstar_n17_18, witness_anatomy has an undefined-variable
   bug) so nobody cites them as run-backed.
6. **Stored durable findings in Cognee** (success messages): the multiset
   structure, the witness/no-witness data, the evenness fact, the
   adjacent-XOR vs count-histogram reconciliation, and the submask/Walsh
   framework.

## What I concluded

- The open request "which sets occur, with multiplicity" is **answered on the
  counting side**: rigid empty×n-2 / nonempty×2, verified n≤256 by two routes.
- Because the multiplicity is uniformly 2, the S² Walsh expansion has **no
  multiplicity redundancy** — any collapse must come from *algebraic* relations
  among the (n−2)² characters, not from multiplicity cancellation.
- The witness search found **no counterexample at full pair order for n≤16**
  (K=n−1 fiber is S²-constant), but the minimal order K*(n)≈n/2 suggests the
  collapse (if it holds) is at order ~n/2, not a bounded order.
- **Sources do not establish collapse.** The library gives the framework
  (submask/Lucas, Walsh basis, Moebius inversion, run structure, distance
  enumerator) and the counting half, but no source states whether S² factors
  through short-range correlations. That remains the open crux; the computed
  data is the run's own evidence.

## What the run still lacks

1. A **proof** of `pf-s2multiset-rigid` (the multiplicity-2 / injectivity
   regularity) — verified to n=256, proven nowhere. The down-set/translate
   structure is the likely route.
2. A **proof** of the COLLAPSE itself (that S² factors through short-range
   correlations at some order), or a full refutation witness at unbounded n.
   The n≤16 census finds no full-order witness but the order tracks n/2.
3. **Captured output** for pf_kstar_extend / pf_kstar_n17_18 /
   pf_verify_witness / verify_g_witness (scripts exist, outputs not captured) —
   the definitive K*(n) sequence beyond the n≤16 g_witness_fiber capture is
   not on disk.
4. `amarilli-moebius-multiplicity`'s `holds-here` remains `unchecked` (the
   tightness/fullness of the specific down-set semilattice unverified) — but
   the direct census does not depend on it.

## Sources that do NOT help (and why)

- **Barbé CA paper** — not obtained; the file under its name is a wrong
  download (Painlevé VI quantum algebra). Do not cite.
- **Wolfram 1984** — landing page capture, no content. Do not read again.
- **Rains–Sloane self-dual codes** — different object (code weight enumerators,
  not this S² index multiset). Do not re-open.
- **Fine 1947** — jstor unobtainable; substance already in the Rowland note.
- **Bacher–Chapman** — different matrix (`holds-here: no`); kept only as a
  cautionary note about the "Pascal matrix" name.
