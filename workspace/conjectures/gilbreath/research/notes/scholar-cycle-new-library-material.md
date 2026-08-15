# Scholar cycle — new library material vs current beliefs

## The two genuinely-new sources this cycle, and what they establish

The researcher added **Malyshev 2021** and **Northshield 2010**, both on the
Rule-90 / Pascal-mod-2 structure of the halved `{0,2}` interior. Both already
carry replacing digests with claim blocks
(`malyshev-max-ones-boolean-pascal-bound`, `northshield-pascal-mod2-line-sums-gf`),
are logged in CLAIMS.md, and in Cognee. Neither filename hides unread text; each
has a verified note.

### Malyshev 2021 (Discrete Math. Appl. 31(5), doi 10.1515/dma-2021-0029)
**Establishes (sourced, catalogue-level; full text NOT held — scanned no-layer):**
in a Boolean (GF(2), XOR-add) Pascal triangle `T_s` with `s(s+1)/2` cells — the
exact rule-90 structure the run *proved* for the halved `{0,2}` interior
(`rule90-interior-xor`) — #ones `ξ ≤ ⌈s(s+1)/3⌉`, equality exactly for
Fibonacci-mod-2 top rows. **Bearing:** upper-bounds the edge-2-read density in
the interior (worst ~2/3; the primes' interior is far sparser, not the extremal).
Interior-frequency half of regeneration only; **does not** bound the boundary
intruder or prove regeneration. Hypotheses hold here: yes. Status: **asserted**.

### Northshield 2010 (Congressus Numerantium 200, hdl 20.500.12648/1110)
**Establishes (sourced; full text NOT held — bitstream blocked, sibling
paywalled):** mod-2 sums of binomials along lines `ai+bj=n` satisfy
`A(x)=P(x)·A(x²)`; the (1,1)-case is Gould's sequence (odd-count of row n of
Pascal mod 2), the (2,1)-case is Fibonacci. Algebraic form of the run's proved
rule-90 edge convolution `e_d = XOR_j [C(d,j) mod 2]·h[...]`. **Bearing:** lead
on the algebra of the edge-read pattern; interior only; does not prove
regeneration. Hypotheses hold here: yes. Status: **asserted**.

## The one scholarly move I made

Both new claims are `asserted` (sourced from abstracts, not machine-checked).
Malyshev's bound is exhaustively checkable for small s, so I wrote
`code/scholar/verify_malyshev_bound.py` to upgrade it to `checked`: it
enumerates all `2^s` top rows for s=1..14, computes the exact rule-90 ones-count,
compares max to `⌈s(s+1)/3⌉`, and checks the Fibonacci-mod-2 maximiser. **I
could not execute it** (scholar role has no shell tool), so the claim stays
`asserted`; the operator must run
`timeout 540 python3 code/scholar/verify_malyshev_bound.py | tee code/out/verify_malyshev_bound.captured.txt`.
This is a bounded small-instance check (method Rule 9), not a search.

## The two "unread" FULLPDFs are NOT unread (stale TASKS)

- **Granville 2026:** Lemma 5.4 **PROVED on the even domain**
  (`lemma54-re-derived-proof`), δ=0 case handled as normal closure (0→2 bounce),
  parity boundary located (over ALL integers the lemma is false — odd v stays
  odd; real prime diagonals are even, so prime case safe), `ν_2/n ≈ 0.42–0.52`
  measured. `li2023-not-bottleneck`: α ∈ {0.52,0.525} is immaterial once a
  positive-linear supply bound `ν_2 ≥ c·n` holds.
- **CHT 2026:** Theorem 1.6 verbatim, right-half column restriction `j ≥ N′`,
  hypotheses (i)–(iii), authors' p.8 difficulty assessment
  (`cht-theorem16-verbatim-fullpdf`). `holds-here: no`.

The **entire remaining open content of Route B** is the **supply-side linear
lower bound `ν_2(q_{n−1}) ≥ c·n, c>0`** (measured c≈0.5, unproved). Neither new
source touches it.

## Outstanding verification (cosmetic)
`code/out/verify_lemma54_v_le_gstar.py` (Link-A `v ≤ g*_n` via `|a−b| ≤ max`)
still has no captured output — `asserted` (elementary), not `checked`. Cosmetic:
the real-prime application measures `v_n` directly.

## Contradictions with recalled memory
**None.** Both new sources confirm the interior Rule-90 characterisation and add
only an upper-bound character of edge-2-read density; neither conflicts with any
established claim. They corroborate `edge-interior-invertibility-sharpened`
(edge reads 2 at least once in a block's life) — from the interior-frequency
side. No disagreement.

## Sources that do not help
Both new sources are leads on the interior-frequency half of regeneration, **not**
regeneration proofs: neither bounds the boundary intruder or the (2,4)-event
rate — the genuinely open target (REQUESTS.md regeneration row). Full texts are
unobtainable (recorded). Do not re-read for content.

## What the run still lacks
- A **proved** `ν_2 ≥ c·n` supply bound (the whole Route B target).
- A machine-verified Malyshev bound (operator must run the verifier).
- The Link-A `v ≤ g*_n` composition executed as `checked`.
