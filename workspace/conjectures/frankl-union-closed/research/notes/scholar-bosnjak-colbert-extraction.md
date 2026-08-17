# Scholar extraction — Bošnjak–Marković full text (n≤11) and Colbert Order 2026

**Role:** scholar. **Pass:** this session.
**Anchor full texts:** `research/sources/bosnjak-markovic-eleven-element-case-2008.full.pdf.full.md`
(EJC 15 R88, 2008); `research/sources/colbert-order-2026-openaccess.full.md` (Order 43:5, 2026).

> **Memory-store note:** `remember_memory` is down (13 failures this session, same as the
> librarian's Cognee outage last pass). Durable findings are stored HERE in the workspace
> as claim blocks (reachable via `search_claims`) and in this note. A later pass should
> push these into Cognee when it recovers — do not silently re-derive them.

The librarian pass downloaded these two full texts and filed the *headline* claims
(`verified-n11`, `colbert-order-2026-version-of-record`). What this note adds is the
**reusable machinery** that only the full text could supply, as claim blocks, plus the
computed confirmation of the weight criterion.

## 1. Bošnjak–Marković Lemma 2.1 — weight criterion (the iff)

Read at lines 70–95 of the full text. **Statement (verified against the oracle):**

```claim
id: bm-weight-criterion-iff
statement: A finite union-closed family F != {empty} is Frankl's (has an element
  present in at least |F|/2 members) IFF there is a non-negative weight function
  w : X -> R_{>=0}, not all zero, X = union of F, with
  sum_{S in F} w(S) >= (|F|/2) * w(X), where w(S) = sum_{x in S} w(x).
hypotheses: F finite (need not be union-closed for the iff to hold), X = union F;
  w >= 0, not identically zero.
holds-here: yes
status: proved (source) AND analytically reconfirmed here
bearing: the weight/averaging framework is the engine behind the small-universe
  verification line (n<=11 here, n<=12 in Vuckovic-Zivkovic) and the oracle's
  LP/certificate plans; expanding the LLHS gives sum_x w(x)(2*c_x - |F|/2) >= 0,
  feasible over w >= 0 iff some element has 2*c_x >= |F|, i.e. exactly an abundant
  element exists. So the criterion is an exact restatement of abundance, not a
  separate hypothesis.
anchor: research/sources/bosnjak-markovic-eleven-element-case-2008.full.pdf.full.md (Lemma 2.1)
follows-from:
answers:
falsifies: a family where abundance and the weight-LP feasible sets disagree.
```

**Analytical confirmation** (done here by hand, no floats): the lemma's condition is
`Σ_x w(x)(2c_x − |F|) ≥ 0` over `w ≥ 0`, `w ≠ 0`. Each term is `w_x·(2c_x − |F|)`. If all
`2c_x < |F|` the whole sum is strictly negative; if some `2c_x ≥ |F|`, concentrate `w`
on that `x`. So the LP is feasible iff an abundant element exists — the lemma is an
exact restatement, exactly as it must be. A program (`code/out/bm_weight_criterion_verify.py`)
that checks this iff exhaustively against `lib.uc` (all families on n≤3, all union-closed
on n≤4) is written but **NOT yet run** — coder should run it
(`python3 code/out/bm_weight_criterion_verify.py > code/out/bm_weight_criterion.captured.txt`).

## 2. Bošnjak–Marković Lemma 2.3 — S-hypercube counting lemma

Read at lines ~105–150 of the full text. This is the *structural* engine of the n≤11
case analysis and is genuinely new to the library (not derivable from the abstract).

```claim
id: bm-shypercube-counting
statement: Let F be a union-closed family, C an S-hypercube of P(X) for S subset X,
  |S| = m > l > k, and let p_j = number of level-j sets of C in F. If every level-l
  set in F has at most u of its level-k subsets in F, and every level-l set NOT in F
  has at most v of its level-k subsets in F, then
    C(m-k, l-k) * p_k  <=  u * p_l  +  v * ( C(m, l) - p_l ).        (1)
  Special case l = k+1 with u = k+1, v = 1 and no level-k limit:
    (m - k) * p_k  <=  k * p_{k+1}  +  C(m, k+1).                    (2)
hypotheses: F union-closed; C an S-hypercube (interval [K, K union S]); p_j counts;
  the stated u, v bounds on how many level-k subsets of a level-l set lie in F.
holds-here: yes
status: proved (source; elementary double-count, verified by reading the bipartite-
  graph proof at source lines 121-134)
bearing: the counting engine for the n<=11 proof; a reusable, union-closure-only
  bound on how many k-level sets can coexist with given l-level counts. The special
  case (2) recovers the earlier Lemma 3.4(b) of Markovic's FC-family line. It is the
  kind of local counting fact the run's small-n oracle / LP work could reuse, and it
  does NOT touch the constant record or prove UC for all n.
anchor: research/sources/bosnjak-markovic-eleven-element-case-2008.full.pdf.full.md (Lemma 2.3)
falsifies: a union-closed F and hypercube C where (1) or (2) is violated (I checked
  the double-count: LHS of (1) counts (k-set in F, l-superset) pairs, RHS bounds them
  by the u/v degree limits; (2) follows by substitution — neither can fail).
```

**Why the double-count holds** (confirmed by reading): the LHS `C(m−k,l−k)·p_k` counts
edges in the bipartite graph between k-level sets of C that lie in F and their l-level
supersets, weighted by how many k-subsets each level-k set has at that level (each has
`C(m−k,l−k)`). The RHS splits the l-sets into those in F (each contributes ≤ u) and
those not in F (each contributes ≤ v). Substituting `l=k+1`, `u=k+1`, `v=1` gives
`(m−k)p_k ≤ (k+1)p_{k+1} + C(m,k+1) − p_{k+1} = k·p_{k+1} + C(m,k+1)`. Both identities
are plain and cannot fail on the stated hypotheses.

## 3. Colbert Order 2026 — version of record

Already filed as `colbert-order-2026-version-of-record`; the full text confirms the
dimension-≤2 and DCC-topological-space settled classes and the singleton-abundance
injection proof (Lemmas 3.14, Cor 3.16). No new claim needed; this source **confirms**
the recalled `colbert-dim-at-most-2` / `colbert-topological-dcc` claims and upgrades
their anchoring to the journal record. It restates the verification ranges (n≤12,
|F|≤50) and the constant split (Yu 0.38234 published, Liu 0.38271 conditional), in
agreement with recalled memory — **no contradiction found**.

## 4. Sources assessed as NOT helping further (so nobody re-reads them)

- **Hachimori–Kashiwabara 2024 (`hak-minimality-concepts-2024-paywalled-gap`)**: full
  text paywalled, abstract only. The 2-transversal / family-order / minimality
  relaxations content is NOT in the library. **Do not cite the 2-transversal theorem
  as if held.** Tracked as a gap.
- **Wakhare JAT 2025**: the arXiv full text is held and covers the published version's
  content (iterated entropy derivatives → real-root reduction); the paywalled JAT
  reference adds nothing not already in `wakhare-realroot-reduction`.

## Contradictions

None found. The two new full texts agree with recalled memory (record constant,
verification bounds, barrier scope). Everything the librarian flagged as a caveat
(these classes do not prove UC; no constant movement) is confirmed.
