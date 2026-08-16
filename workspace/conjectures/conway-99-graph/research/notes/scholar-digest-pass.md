# Scholar digest pass — what was added this run

The reference library was already well-built by the librarian. This scholar
pass verified the digests against the full texts, replaced the placeholder
digests that were still boilerplate, added the missing claim blocks, stored
durable findings in Cognee, and wrote the canonical oracle.

## Summaries rewritten (were placeholder "digest only" boilerplate)

- `research/summaries/reimbayev-hexagon-bound-srg-lambda1-mu2.md` — abstract
  only in library; records the hexagon lower bound as a lead but flaggable as
  unusable without the paper body. **Important:** the "full text" downloaded
  for this arXiv paper is only its landing page, not the paper.
- `research/summaries/reimbayev-subgraphs-order-six-srg-l1-mu2.md` — same
  caveat (order-six subgraph classification, list not in library).
- `research/summaries/keramatipour-sat-conway99.md` — SAT attack; abstract
  says solvers cannot handle the problem in reasonable time; adds no reportable
  boundary, confirms enumeration is the wrong method.
- `research/summaries/zehavi-oliveira-not-conway-99.md` — solvable *variant*,
  NOT the actual problem; boundary caution only.
- `research/summaries/automorph-putative-conway-99-graph.md` — Cesarz–Woldar
  2025 findings with claim block `aut-cw-2025`.
- `research/summaries/crnkovic-maksimovic-composite-automorphism.md` — claim
  block `aut-cm-2020` (no Z6/S3/Z9/E9).
- `research/summaries/makhnev-2013-local-subgraphs-srg-99.md` — paywalled,
  body absent; mostly unusable.
- `research/summaries/van-lint-perfect-codes-survey-1975.md` — five-member list
  + BvLS construction; claim block `five-member-list-vanlint1975`.

## Verified against full texts

- Brouwer–Neumaier 1988 full text confirmed: theorem k >= lambda(lambda+3)/2,
  corollary (mu=2, k < lambda(lambda+3)/2 => partial quadrangle, (lambda+1)|k),
  row 99 in its own table marked `?` open with spectrum 3^54,-4^44.
- Brouwer web tables: row 9 `! 9 4 1 2 | 1 4 | -2 4 Paley(9)`; row 195 of
  51-100 `? | 99 | 14 | 1 | 2 | 3 54 | -4 44` — the 2-graph* note and open
  status confirmed.
- `research/sources/index.full.md` is a DUPLICATE of the Brouwer–Neumaier
  Springer landing page (same DOI 10.1007/BF02122552); the real full text is
  `brouwer-neumaier-1988-combinatorica.full.md`. Flagged so nobody reads it
  again expecting something new.

## Claim blocks added (now in research/CLAIMS.md)

- `aut-cw-2025` (Cesarz–Woldar: 7||G| => Z7, 2||G| => |G||6, computer-free)
- `aut-cm-2020` (Crnkovic–Maksimović: no Z6/S3/Z9/E9)
- `five-member-list-vanlint1975` (family is exactly five members; BvLS exists)

## Durable memory (Cognee)

Stored source-backed findings: the five-member family / 33 excluded by
integrality; the automorphism bounds; the mu=2 dichotomy does not bite 99; the
controls 9 and 243 exist; (99,14,1,2) open; local structure 7K2. NOTE: the
`remember_memory` writes returned IDs, but `recall_memory` returns a Cognee 404
("No data found"), so recall is currently unavailable in this box — the writes
landed but the index is not serving them. A later run should re-check recall.

## Canonical oracle — code/lib/srg.py (NEW)

Wrote the single canonical oracle so no script decides srg membership inline:
`is_srg(A, v, k, lambda, mu)` using exact integer common-neighbour counting
(A @ A) off the 0/1 matrix — no floating-point spectrum as a decision.
Exposes `rook(3)` (srg(9,4,1,2)), `bvls_graph()` (243-vertex coset graph from
the ternary Golay 5x11 parity-check H, srg(243,22,1,2)), and
`random_regular_14_99()` (negative control). `__main__` is a self-check that
tool_builder/coder MUST run and record before anything trusts it (scholar has
no execution tool this run, so is_srg is marked UNVERIFIED until that self-check
lands under code/out/).

## Not done (no tool in this run) — hand to orchestrator/tool_builder

1. **Run and record the oracle self-check** (`python code/lib/srg.py`): expect
   rook(3) True, rook(4) False, bvls True (243,22,1,2), random 99 True-fails.
   Redirect output to code/out/oracle-selfcheck.txt. This is TASKS.md's first
   open row (ledger write needed — I have no record_entry tool).
2. Independently build the BvLS graph a second way (e.g. Cayley-graph/abelian
   construction per Wikipedia) to cross-verify bvls_graph(), not just self-check.
3. Expose save/load of the adjacency matrix (GOAL: oracle must read a matrix
   off disk). Current is_srg takes an in-memory matrix.
4. Then attack one structural claim (phase 3), run against rook(3) and bvls.

Note on TASKS.md: it is derived from the `tasks` ledger; filling it requires
`record_entry`/`close_entry`, which are not in my tool set. The proposed rows
are above.
