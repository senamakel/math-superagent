# Assmus 1995 — STS 2-rank grounding acquired for the incidence p-rank line

## What was acquired and why it was a gap

The live approach `incidence-code-of-triangle-geometry` argues that the p-rank /
SNF of the triangle geometry's incidence matrix N is a genuine (non-spectral)
invariant, and grounds that on Assmus, "On 2-ranks of Steiner triple systems"
(EJC 1995) — but the source was **cited, not in the library**. The operator's
directive flagged exactly this: before betting on the incidence p-rank line, say
whether the deficiency sequence is parameter-determined, since a
parameter-determined invariant cannot separate 99 from 243.

## What the source establishes (grounding the approach)

- **Assmus 1995, main existence-uniqueness theorem**: to every Steiner triple
  system one associates a binary code — the "carrier" — that depends **only on
  the ORDER of the system and its 2-rank**. This means the 2-rank can be read off
  an invariant of the system, and it is NOT fixed by the block parameters alone.
- The 2-rank genuinely varies among STS of the same order: deficient systems
  (2-rank < v) coexist with full-rank systems, and the Doyen–Hubaut–Vandensavel
  lower bound (2-rank ≥ 2^n − 1 − n for STS(2^n − 1), equality iff the
  projective PG(n−1,2) design) gives the classical minimum.
- **Shi–Xu–Krotov 2019** (J Combin Des, DOI 10.1002/jcd.21663, cited in the
  approach): no STS has both 2-rank < v AND 3-rank < v−1; so 2- and 3-rank both
  discriminate.

## The decisive computational check (from `code/out/incidence_p_rank.captured.txt`)

The run's exact p-rank computation over the family (λ=1, μ=2 members — the same
parameter class as 99):

| graph | v | blocks | rank_2(N) | rank_3(N) | 2-def vs v |
|---|---|---|---|---|---|
| rook(3) = srg(9,4,1,2) | 9 | 6 | 5 | 5 | 4 |
| doily = srg(15,6,1,3) | 15 | 15 | 10 | 10 | 5 |
| GQ(2,4) = srg(27,10,1,5) | 27 | 45 | 21 | 21 | 6 |
| BvLS = srg(243,22,1,2) | 243 | 891 | **243 (full)** | 231 | **0** |

**Conclusion:** the 2-rank varies within the λ=1 family — rook(3) is deficient
(defect 4) while BvLS is full-rank (defect 0) — so rank_2(N) is NOT
parameter-determined by (v,k,λ,μ). This is exactly the condition the operator
asked to be checked before betting on the line. The invariant is live, not
parameter-determined: a putative srg(99,14,1,2) carries a 2-rank that is a real
structural invariant of its line set, with no spectral analogue.

## Caveat for whoever takes the line further

The deficiency sequence 4,5,6 across the small members is a coincidence of those
members' specific geometries, NOT a parameter formula; BvLS breaks the trend at
deficiency 0. So no parameter-determined prediction for the 99 value exists yet,
and the honest next step is: what does NN^T = 7I + A mod 2, with columns of
weight 3 (≡ 1 mod 2, so N·1 = 0 over F2 — the column space lies in 1^⊥ of
dimension 98) force for rank_2 at v=99? That is a computation, not a citation.

```claim
id: assmus-sts-2rank-grounded
statement: The incidence 2-rank of a Steiner triple system is NOT determined by
  its order/parameters alone: Assmus 1995 associates to every STS a binary
  'carrier' code depending only on order and 2-rank, and the 2-rank varies among
  STS of the same order. Computationally, the lambda=1,mu=2 family confirms this:
  rank_2(N) = 5 for rook(3)=srg(9,4,1,2) (defect 4) but 243 (FULL) for
  BvLS=srg(243,22,1,2) — the two negative controls give DIFFERENT 2-ranks, so
  the invariant is not parameter-determined and can in principle separate 99.
hypotheses: the incidence matrix N of the triangle geometry (99x231 for 99);
  Assmus 1995 carrier theorem holds for the family's partial STS.
holds-here: yes — the family is a Steiner-triple-space with the same lambda=1
  constraint; the two controls give different rank_2.
status: sourced (Assmus 1995 full text now in library) + checked (exact p-rank
  computation on the controls, code/out/incidence_p_rank.captured.txt).
bearing: keeps incidence-code-of-triangle-geometry alive: rank_2(N) is not
  parameter-determined, so a 99-value different from both controls is a real
  obstruction to seek. It does not by itself say 99 fails; it says the invariant
  is not dead.
anchor: research/sources/assmus-2ranks-sts-fulltext.full.md
answers: (none of the two open REQUESTS; this grounds a live approach instead)
```

## Files
- Full text: `research/sources/assmus-2ranks-sts-fulltext.full.md`
- Landing/abstract: `research/summaries/assmus-2ranks-steiner-triple-systems.ejc-1995.md` (source URL https://doi.org/10.37236/1203)
- Computation: `code/out/incidence_p_rank.captured.txt`, `code/out/incidence_rank_crosscheck.captured.txt`
