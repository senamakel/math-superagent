# Scholar cycle — Malyshev 2021 & Northshield 2010: digest confirmed, consistency check, verification gap

**What this cycle establishes.** The two genuinely-new sources the research
agent added this pass — Malyshev 2021 ("Boolean analogues of the Pascal triangle
with maximal possible number of ones", Discrete Math. Appl. 31(5), doi
10.1515/dma-2021-0029) and Northshield 2010 ("Sums across Pascal's triangle
modulo 2", Congressus Numerantium 200, hdl 20.500.12648/1110) — are both already
digested and correctly filed in `research/notes/scholar-cycle-new-library-material.md`
with claim blocks (`malyshev-max-ones-boolean-pascal-bound`,
`northshield-pascal-mod2-line-sums-gf`), indexed in CLAIMS.md, and in Cognee.
I re-read both summaries and the sheet note; neither has drifted.

## What each actually establishes (and what it implies here)

**Malyshev 2021.** Theorem (quoted from published abstract): in a Boolean
(GF(2), XOR-add = Rule-90/Pascal-mod-2) triangular array of `s(s+1)/2` cells,
the number of ones `ξ ≤ ⌈s(s+1)/3⌉`, with equality *exactly* for top rows that
are the Fibonacci sequence mod 2. **Bearing here:** the halved `{0,2}` interior
of a Gilbreath row is precisely such a triangle (this run's proved
`rule90-interior-xor`), so this is a sharp *upper* bound on the density of 1s =
edge-2 reads during erosion: worst case ~2/3. The primes' interior is far
sparser. **It does NOT prove regeneration**: it bounds how often the edge reads
2, but regeneration needs those reads to land *while the intruder is 4* — a
boundary condition Malyshev's interior statement says nothing about.

**Northshield 2010.** Mod-2 sums of binomials along lines `ai+bj=n` satisfy
`A(x)=P(x)·A(x²)`; the (1,1) case is Gould's sequence (count of odd entries in
row n of Pascal mod 2), the (2,1) case is Fibonacci. **Bearing here:** the
algebraic (generating-function) form of this run's proved Rule-90 edge
convolution `e_d = XOR_j [C(d,j) mod 2]·h[...]`. Interior/algebra only; does not
prove regeneration. Both full texts unobtainable (no text layer / DSpace stub /
paywalled) — recorded, do not re-attempt.

## Consistency check (hand, small s) — Malyshev bound not garbled at small s

I verified the quoted bound `ξ ≤ ⌈s(s+1)/3⌉` and its Fibonacci-mod-2 equality
achiever on the first five sizes by hand (Fibonacci mod 2 top row = 1,1,0,1,1,0,…):

| s | cells | Fib-mod-2 ξ | bound ⌈s(s+1)/3⌉ | equality |
|---|---|---|---|---|
| 1 | 1 | 1 | 1 | ✓ |
| 2 | 3 | 2 | 2 | ✓ |
| 3 | 6 | 4 | 4 | ✓ |
| 4 | 10 | 7 | 7 | ✓ |
| 5 | 15 | 10 | 10 | ✓ |

Non-Fibonacci offenders (all-ones top s=3,5; alternating 1,0,1,0,1) stay strictly
below the bound. **This is a consistency check only** — it confirms the quoted
statement is not a garbled transcription at small s, not a proof. Claim stays
`status: asserted` (abstract-sourced), which is the honest level.

## The verification gap (operator action, if any)

`code/scholar/verify_malyshev_bound.py` (enumerates all 2^s top rows for s=1..14,
compares max ξ to the bound, checks the Fib-mod-2 maximiser) was written but not
executed — the scholar role has no shell tool. **Operator should run**
`timeout 540 python3 code/scholar/verify_malyshev_bound.py | tee code/out/verify_malyshev_bound.captured.txt`
to upgrade the claim to `checked`. This is a bounded small-instance check (all
top rows to s=14), not a search, and does not approach anything the bound in the
problem statement is meant to defeat.

## Contradictions with recalled memory

**None.** Both sources corroborate `rule90-interior-xor` and
`edge-interior-invertibility-sharpened` (the edge reads 2 at least once per block
life) from the interior-frequency side. Malyshev's *upper* bound on edge-2 reads
is consistent with — not opposed by — the run's *existence* result (edge reads 2
at least once). Neither source touches the genuinely open target (the two-point
mod-4 switch-correlation lower bound that is the entire remaining content of
Route B / G-supply).

## Sources that do not help further

Both are interior-frequency leads on regeneration, not regeneration proofs, and
neither full text is obtainable. Do not re-read for content; the digests are
complete and final.
