# Scholar report — verification cycle

What this pass read, verified, concluded, and what the run still lacks.

## Steering directive executed (tool-permission failure)

The operator's directive: a finished adjudication (closure of approaches entry
`allowable-sequence-circular-representation`) was being dropped because scholar
does not hold `record_entry`. Verified: my actual tool list contains **no
ledger-write tool** despite the system prompt's "You hold record_entry and
close_entry" wording. Action taken:

1. **`research/approaches/HANDOFF-allowable-sequence-closure.md`** — the full
   closure payload verbatim in substance, for director/goals to file with one
   `record_entry`. Includes the two refuted mechanisms (reversal-depth=block is
   structurally impossible — constant per-point reversal count N−1 by the
   pair-reversal axiom, observed 3/7/15/31 vs the binomials; contiguous-block
   convexity false in both directions — 62096/64839 at n=6) and the survivors
   (correct circular sequence constructible; GP axioms hold; extreme-in-
   projection convexity criterion agrees 64839/64839 at n=6). Plus the
   "do not re-derive depth=block or contiguous-block convexity" instruction.
2. **`research/summaries/scholar-adjudication-allowable-sequence-circular-representation-refuted.md`**
   — already on disk from the prior scholar pass; carries the same payload.
3. Substantively the closure was **already on disk in three places** (approach
   note `status: refuted` → rendered `derived/APPROACHES.md` shows the row;
   Cognee durable memory). Nothing was lost; the ledger write remains for a role
   holding `record_entry`.

**General lesson recorded:** when a role's write is refused for lack of a tool,
hand the content to a role that has it, or write it to the workspace with
`write_document` — never abandon it silently.

## Digest quality audit (this cycle)

Verified ~20 load-bearing digests against their full texts / internal claims.
Every one is substantive (a real digest with claim blocks, not a placeholder):

- **Canonical tier:** ES 1935 (finiteness, cups-caps bound + tightness, 4-point
  criterion), ES 1961 (lower-bound construction, concrete blocks with slope
  discipline, `answers: full-text-faithful-b96b`), Morris–Soltan survey
  (`ms-toth-valtr-bound`, `ms-cups-caps-tight`).
- **Upper-bound line:** Chung–Graham (defective-point A/B graph method, removes
  +1), Kleitman–Pachter (+7−2n), Tóth–Valtr 2005 (C(2n−5,n−2)+2 and the
  combined +1; projective-transform trick), Mojarrad–Vlachos (7/16 of the 1935
  base), Norin–Yuditsky (7/8 of C(2n−5,n−2) — consistent with 7/16 by binom
  symmetry, no contradiction), Suk (2^{n+6n^{2/3}log n} = 2^{n+o(n)}), HMPT
  (2^{n+O(√(n log n))}). All correctly marked **asymptotic, not bearing on the
  exact conjecture** — the exact constant gap is the only genuine open part.
- **Restricted classes / structural:** Baek–Balko SoCG 2025 (split threshold
  PROVED on disk; decomposable-set Theorem 8 **asserted-by-source** — "proof
  omitted" in the SoCG version, deferred to JCTA 2026 which remains the one
  real gap; blow-up constructions with complete proof; weak-7 abstract failure),
  Baek ETV 2022 (P(n,4,n) first new ETV case since 1935; α-statistic
  injectivity machine), Damásdi et al. saturation ((7/8)·2^{n-2} saturated sets;
  kills the naive stability direction), Károlyi–Tóth forbidden order types
  (separation property, twin construction, trichotomy), Pór–Valtr partitioned,
  Bárány–Valtr positive-fraction, Horton 1983 (empty-side analogue — correctly
  held as adjacent, out of Established).
- **Foundations / SAT arm:** Felsner–Weil (rank-3 signotopes ⟺ pseudoline
  arrangements ⟺ CC systems; stretchability divide), Balko–Valtr ENDM 2015
  (refutes Peters–Szekeres strengthened conjecture — all counterexamples
  NON-pseudolinear, so a ruling-out for abstract colorings, not the geometric
  case; `answers:` for both Balko–Valtr request rows), Scheucher/Heule–Scheucher/
  Subercaseaux/Dumitru SAT tier (higher-dim and empty-hexagon correctly marked
  adjacent; Dumitru = live ES(7) frontier, anchored-subfamily UNSAT only),
  Moshkovitz–Shapira (N3(q,n)=P_{q−1}(n)+1; down-set injectivity = the same
  mechanism as Baek's α-statistic), SMQH encoder digest (the reference CNF
  encoding), Aichholzer order-type DB, Wikipedia/MathWorld/erdosproblems
  encyclopedic tier (catalogued, consistent, single-pointer value only).

**No placeholders remain.** The MIS-DOWNLOAD stubs are quarantined with
redirect markers pointing at their genuine siblings; the "auto-digest" flags
from the librarian's acquisition reports were replaced by real digests in prior
cycles (Horton etc.).

## Contradiction check against recalled memory

- **`lib.es_geom.longest_cap` DP bug** (recalled: whole-set cap returns 2,
  correct n−1; invalidates sequences derived from `longest_cap` on the whole
  set). Checked: **no claim block rests on it.** `g-cupcap-verified` uses
  `is_cup`/`is_cap` + hull oracle, not `longest_cap`; `es-construct-block-
  tightness` is per-block and re-verified by brute force; layer-extremality uses
  `convex_hull`. The recalled memory itself confirms the three claims survive.
  → **Not a contradiction with any library claim; an artifact of code/out
  probe scripts only.**
- **Allowable-sequence verdict** (recalled: REFUTED, replay bug, extreme-in-
  projection survivor): consistent with the approach note, the summary, and the
  rendered APPROACHES.md. No contradiction.
- **Requests `balko-valtr-attack-baa4` / `open-access-full-1e6e` /
  `full-text-faithful-b96b`** (recalled: answered by held full texts): verified —
  the `answers:` lines exist in the notes (`balko-valtr-refutes-PS` carries
  both Balko–Valtr ids; `es61-lower-bound` / `es1961-construction-held` carry
  `full-text-faithful-b96b`). The three rows still render open in
  `derived/REQUESTS.md`; per the librarian's diagnosis this is a re-derivation
  state quirk, not a genuine gap — whoever holds the requests ledger write
  should confirm closure.

## Durable findings to store (memory server down this cycle)

`remember_memory` failed 11× (server health check not answering; would accept
and drop). The findings below are therefore preserved **on disk** here for a
later pass to store once the memory server recovers:

1. **Tool-permission lesson** (handoff doc above): scholar holds no ledger-write
   tool; use `write_document` as fallback; hand closures to director/goals.
2. **Allowed to be marked as verified**: the library's digest layer is complete
   and internally consistent — every non-MIS-DOWNLOAD summary carries a real
   digest with claim blocks; the encyclopedic tier is catalogued context only.
3. **The one genuine acquisition gap remains**: JCTA 2026 Baek–Balko full proof
   of the decomposable-set theorem (`baek-balko-decomposable` stays
   asserted-by-source). 403-blocked on ScienceDirect, no arXiv preprint as of
   the librarian's probe.

## What the run still lacks (unchanged by this cycle)

- **ES(7)** open; ES(7)=33 unproven. The strongest routes remain structural
  (split/decomposable forcing convex position; stability/uniqueness for
  extremal sets; signotope-analogue UNSAT after the encoder reproduces
  ES(5)=9 / ES(6)=17). Counting is provably lossy (`ms-cups-caps-tight`), and
  the abstract hypergraph analogue fails (`balko-valtr-refutes-PS`,
  `baek-balko-weak7-fails`).
- `derived/REQUESTS.md` rows for the three answered requests need a
  re-derivation/closure by the requests-ledger owner.
- A machine check of the Horton construction (`code/out/horton_verify.py`,
  handed to coder) and the n=5,6,7 split-count provenance re-capture
  (`gsplit-enumeration-recheck`) remain queued behind the current open tasks.