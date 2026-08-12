# Couch–Daniel–Wright — Classes of cubic graphs containing cycles of integer-power lengths

Source: http://ajc.maths.uq.edu.au/pdf/79/ajc_v79_p100.pdf
Published: Australasian J. Combinatorics 79(1) (2021) 100–105 (open access)
Full text: `research/sources/couch-daniel-wright-integer-power-lengths.full.md`

## What it is

A short open-access paper (P. J. Couch, B. D. Daniel, W. Paul Wright, Lamar University)
attacking **Caro's weaker question**: does every graph with δ≥3 contain a cycle whose
length is an integer power `a^k` (a≥2, k≥2) — a relaxation of the power-of-two
conjecture. It does NOT settle the power-of-two conjecture; it settles Caro's question
for several restricted classes.

## Key established results

1. **Theorem 1 / The main interval trick.** Using a number-theoretic lemma of Paz
   (Lemma 1): for n beyond ~286, there is an integer power `a^m` in `[n, 3n/2)`. So a
   cycle of length `n` whose neighborhood produces all lengths `[2n,3n]` yields a cycle
   of integer-power length. Combined with a triangle-contraction reduction, this shows:
2. **Corollary 1**: every **claw-free graph with δ≥3 contains a cycle of length a^k**
   (integer power, a≥2, k≥2).
3. **Corollary 2**: every claw-free graph with δ≥2, Δ=3, and at most two degree-2
   vertices contains such a cycle.
4. **Corollary 3 / Theorem 2 / Theorem 3**: extending to graphs where the set of
   centers of induced claws is independent, and to **almost claw-free** graphs with δ≥3.

## Direct relevance to the run

- **Confirms the power-of-two conjecture does NOT follow from Caro's integer-power
  question** — the integer-power result for claw-free graphs is strictly weaker than
  the power-of-two conjecture for claw-free graphs. The claw-free power-of-two case
  (Nowbandegani et al.) is a separate, still-open restriction.
- Cites and locates **Shauger's other paper [11]**: "Claw-free, cubic graphs of low
  genus have a cycle whose length is a power of two", Congr. Numer. 159 (2002) 119–126.
  This is an additional primary result in the run's family that is NOT yet in the
  library (conference proceedings, no open PDF found yet). Listed for a future request.
- Confirms the standard references: Daniel–Shauger 2001 (planar claw-free), Shauger
  1998 (K1,m-free), Heckman–Krakovski (3-connected cubic planar), Bensmail (q-power
  constructions), Verstraëte (unavoidable cycle lengths).

## Status

Peer-reviewed, open access (AJC, CC BY-ND 4.0). Read in full here. It is an *adjacent*
result (Caro's integer-power question), not a step toward the power-of-two conjecture;
record for completeness and because it pins down the claw-free integer-power class.

```claim
id: EG-clawfree-integer-power-cycle
statement: Every claw-free graph with δ≥3 contains a cycle whose length is a^k for some integers a≥2, k≥2 (Caro's integer-power question, not the power-of-two conjecture).
hypotheses: claw-free, δ≥3.
holds-here: yes — a settled adjacent class; weaker than the power-of-two conjecture for claw-free graphs, which remains open.
status: proved (Australas. J. Combin. 79 (2021) 100–105)
bearing: Separates Caro's weaker question from the EG power-of-two conjecture; a run looking for a claw-free power-of-two result must not cite this as settling it.
anchor: research/sources/couch-daniel-wright-integer-power-lengths.full.md
```
