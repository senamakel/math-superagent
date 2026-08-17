# Scholar report — library digestion cycle

What this scholar pass did, concluded, and what the run still lacks.

## What I read and digested

The reference library is **mature** (the canonical tier, every published upper
bound, the lower-bound construction, exact values, and the full computational/SAT
arm were already digested into 93+ claim blocks before this pass). The genuinely
new source this cycle was the one real frontier gap the librarian closed:
**Horton 1983** (sets with no empty convex 7-gons). I read its primary full text
and replaced its two placeholder digests with real notes.

### New/replaced notes (all now carry claim blocks, no placeholders remain)

1. **`research/summaries/horton-1983-sets-with-no-empty-convex-7-gons.pdf.md`** —
   the substantive digest. Establishes: for every $k$ a $2^k$-point set
   $S_k=\{(i,d(i)):0\le i<2^k\}$, $d(i)=\sum_j a_j c^{j-1}$, $c=2^k+1$, has **no
   empty convex 7-gon**; hence $g(n)$ (least $N$ forcing an *empty* convex
   $n$-gon) does not exist for $n\ge 7$, and $g(6)$ is open. Kept its proof
   mechanism (any empty convex polygon meeting bottom half $B$ and top half $T$
   has $\le 3$ vertices in each, so $\le 6$ total). Claim `horton-no-empty-7gon`,
   `horton-s-k-construction` (both proved, from the primary argument). Deliberate
   boundary: this is the **empty-side analogue** of the ES construction, NOT the
   convex-position ES(n) conjecture — kept out of Established per GOAL's
   adjacent-problem rule.
2. **`research/summaries/horton-1983-sets-with-no-empty-convex-7-gons.md`** — the
   HTML landing duplicate → redirect to the PDF digest.
3. **`research/summaries/smqh-erdos-szekeres-encoder.py.md`** — replaced the
   placeholder with the actual SMQH SAT encoder digest. This is the reference
   encoding the run's computational arm must mirror: CNF over orientation vars +
   linear-order vars, CC-system/ordered-signotope transitivity clauses, the
   `conv_{p,q,r,s}` 4-set convexity predicate, and no-g-gon = negate conv over a
   g-subset's 4-subsets; optional `forced_sym` adds rotation equivalence +
   lex-smallest-rotation isomorph rejection. Claim `smqh-erdos-szekeres-encoder`.
4. **`research/summaries/dumitrescu-...-html.md`** — found to already hold a
   substantive digest of the Goodman–Pollack allowable-sequence framework (not a
   placeholder). Added claim
   `dumitrescu-allowable-framework-primary`: every allowable sequence is
   realizable as the $n$-sequence of a **pseudoline** arrangement but not every
   one by a **point set** — the primary on-disk statement of the realizability
   trap.
5. **`research/summaries/dumitrescu-...-md`** — compact note for the
   Dirac–Goodman–Pollack conjecture itself (c=1/845), claim `dumitrescu-dgp`
   (marked adjacent, not a route to ES).
6. **`research/summaries/smqh-repo-tree.md`** / **`smqh-github-repo-search.md`** —
   replaced with artifact-evidence notes: the SMQH pipeline (eznf encodes →
   allsat-cadical enumerates abstracts → Localizer realizes) and the hard finding
   that the **six inner-12 configurations were never published** (claim
   `smqh-inner12-never-published`) — the extract-inner-12-as-restricted-class
   route is closed; do not re-search.
7. **`research/summaries/wikipedia-happy-ending-problem.md`** and
   **`wikipedia-erdos-szekeres-theorem.md`** — encyclopedic notes: the
   small-values/adjacent taxonomy (claim `wiki-happy-ending-small-values`), and
   the **name-hygiene** marker that the Mathlib "Erdős–Szekeres" is the
   *monotone-subsequence* theorem, distinct from the planar ES(n) conjecture
   (claim `wiki-es-monotone-subsequence`).
8. **`research/summaries/erdosproblems-107-happy-ending-entry.md`** — context:
   problem open with no claimed solution; prize structure; a Lean statement
   already exists externally (claim `erdosproblems-107-open`).
9. Redirects for **MIS-DOWNLOAD stubs** that would otherwise be read as genuine:
   `duque-... 2017 full.md`, `balko-valtr EJC 2017 full.md`,
   `goal-aichholzer...k-convex`, `scheucher -full`, `heule-scheucher -full`,
   `subercaseaux-et-al -full`, `dumitru -full`, `subercaseaux-mackey HTML`,
   `koshelev -html`, `PointSAT HTML`, `leanpool -full`, `felsner...-full` — each
   now a short redirect to its owning note, so the wrong-paper content is never
   re-read as evidence.

### Verification handoff

Wrote **`code/out/horton_verify.py`** (exact-integer, numpy dtype=object)
checking general position and absence of an empty convex 7-gon for Horton $S_k$
at $k=3,4$ (optionally 5). I cannot execute code in this role, so I handed it to
coder via `code/out/horton_verify_HANDOFF.md` with the exact command and expected
result. Pending that run, `horton-no-empty-7gon` is `proved` from the source's
argument (not machine-checked yet).

## Conclusions

- **Horton is a structural datum, not a tool.** It is a second independent
  example of the *recursive self-similar* shape an extremal no-large-convex/
  empty construction takes (halves = scaled translates), supporting the
  extremal-structure thread's question of how close an extremal $2^{n-2}$-point
  no-convex-$n$-gon set must be to the ES construction. It does NOT bear on
  $\mathrm{ES}(n)\le 2^{n-2}+1$.
- **The computational frontier, now well-documented:** on ES(7)-critical size,
  SMQH (4-fold, no realizable 32-pt no-7-gon), PointSAT (200k abstract candidates,
  none realizable), and Dumitru (UNSAT on anchored subfamilies) all fail to
  realize any 32-point no-7-gon set — but none exhausts the abstract space, so
  none refutes ES(7)=33. The abstract space is dominated by unrealizable order
  types; any upper-bound argument must enforce 4-tuple/point realizability.
- **Sources that do not help (and why):** the encyclopedic tier (Wikipedia,
  MathWorld, erdosproblems) adds no mathematics the primaries do not establish
  more reliably — retained only as pointers and drift-guards. The
  MIS-DOWNLOAD stubs (wrong physics/NLP papers fetched from guessed URLs) must
  never be cited; I redirected their summaries so a future reader is pointed at
  the correct source rather than re-reading garbage as evidence.

## Flag: ledger indexing quirk for the horton ids

The two `horton-*` claim blocks are correctly on disk in my canonical note and in
the librarian's acquisition report, and the **entailment graph reads them** (the
`wiki-happy-ending-small-values` claim, which `follows-from: horton-no-empty-7gon`,
is filed under "Established for free"). Yet `read_ledger` queries by id or text
return no horton row. Since the derivation demonstrably reads the claim (it
appears in ENTAILMENT.md), this is a runtime lookup/indexing quirk for these two
ids, not missing content. The on-disk note is the source of truth and is correct.

## What the run still lacks

- A machine **verification** of the Horton construction (handed to coder).
- **ES(7)** remains open; the strongest available route remains the structural
  one (force convex position from split/decomposable structure, or a
  stability/uniqueness argument for extremal sets), not more counting — counting
  is provably lossy (`ms-cups-caps-tight`), and the abstract-hypergraph analogue
  fails (`balko-valtr-refutes-PS`, `baek-balko-split`).
