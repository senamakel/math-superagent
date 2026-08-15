# Malyshev — maximum number of ones in a Boolean (mod 2) Pascal triangle

Directly relevant to this run's *proved* Rule-90 interior structure
(`rule90-interior-xor`): the halved `{0,2}` interior evolves by XOR = Pascal mod
2, so the density of 1s in that interior is exactly the type of quantity these
papers bound. This bounds how many times the left edge reads `2` during
erosion.

## The sharp bound (sourced

**F. M. Malyshev, "Boolean analogues of the Pascal triangle with maximal
possible number of ones", *Discrete Mathematics and Applications* 31(5)
(2021) 281–286 (eng. transl. of *Дискрет. Матем.* 33(4) 2021), doi
10.1515/dma-2021-0029**

Setting: a Boolean triangular array `T_s` of `s(s+1)/2` cells over `GF(2)`,
top row has `s` elements, each lower row is the XOR (sum mod 2) of adjacent
entries of the row above — exactly the Rule-90/Pascal-mod-2 structure this run
proved for the halved `{0,2}` block interior.

**Theorem.** The number `ξ` of ones satisfies

    ξ ≤ ⌈ s(s+1) / 3 ⌉,

and equality is attained **exactly** for triangles whose top row is the
Fibonacci sequence taken mod 2.

This is the sharp density bound on Rule-90 evolution of a halved block: at most
~2/3 of the interior cells can be 1 (edge = 2), and the extremal case is the
Fibonacci-mod-2 initial pattern (i.e., `11010110...`, which for the primes' own
halved gaps is *not* the case — the prime interior is much sparser in 2s).

## The distribution results (supporting)

- **F. M. Malyshev & E. V. Kutyreva, "On the distribution of the number of ones
  in a Boolean Pascal's triangle", *Discrete Math. Appl.* 16(3) (2006)
  261–268**, doi 10.1163/156939206777970435: for large `s` the count of ones
  concentrates near `k_s·s` for an unbounded threshold sequence `{k_i}`; any
  such triangle contains a near-maximal zero-triangle.
- **F. M. Malyshev, "Distribution of the extreme values of the number of ones
  in Boolean analogues of the Pascal triangle", *Discrete Math. Appl.* 27(3)
  (2017) 153–160**, doi 10.1515/dma-2017-0019: admissible counts below `k_i s`
  or above `s(s+1)/3 − (k_i s)/3` concentrate in small neighbourhoods depending
  only on `i` and on `s` modulo a modulus.

## Why it bears on this run

The halved interior of a leading `{0,2}` block is a Rule-90 (Pascal mod 2)
triangle. Malyshev's bound says the 1-density (edge-2 reads) is at most ~2/3 in
the *worst* case and the Fibonacci-mod-2 top row is the unique maximiser. Since
the run has independently proved the edge map of a block reads `2` at least
once in its life (`edge-interior-invertibility-sharpened`: e=0 ⟺ h=0), the
density question is about *how often* — which the (2,4)-event rate needs. This
is an upper-bound characterisation of the interior, not a regeneration proof:
it does not say anything about the boundary intruder or how many edge-2 reads
arrive *while* the intruder is 4.

```claim
id: malyshev-max-ones-boolean-pascal-bound
statement: In a Boolean (GF(2), XOR-add) Pascal triangle T_s with s(s+1)/2 cells, the number ξ of ones satisfies ξ ≤ ⌈s(s+1)/3⌉, with equality attained exactly for top rows that are the Fibonacci sequence mod 2. This bounds the density of 1s (edge-2 reads) in the halved Rule-90 interior of a {0,2} block.
hypotheses: XOR = Rule 90 = Pascal mod 2 structure of the halved {0,2} block interior (this run's proved rule90-interior-xor); T_s is any GF(2) Pascal triangle.
holds-here: yes — the interior of any {0,2} block satisfies exactly this XOR rule; the bound is an upper characterisation of interior 2-density.
status: sourced (Malyshev 2021, Discrete Math. Appl., quoted from published abstract); NOT independently verified by this run's program; the abstract is the full level of proof obtained.
bearing: bounds the frequency of edge-2 reads during erosion of a block from above (~≤ 2/3 worst case); it is interior structure only and says nothing about the boundary intruder, so it does not prove regeneration.
anchor: research/summaries/malyshev-maximal-ones-Boolean-pascal-triangle.md; doi 10.1515/dma-2021-0029
answers: how-dense-is-the-edge-2-read-set
```

## Status and provenance

- **Full text:** NOT held. Both the DMA 2021 English paper (doi 10.1515/dma-2021-0029)
  and the Math-Net.Ru Russian originals (10.4213/dm1606, dm1384) are scanned
  PDFs with no text layer and would not pass the converter; MMA/JSTOR not open.
  Recorded so nobody re-attempts.
- **Content:** sourced from the published abstracts (unambiguous theorem
  statements) via search. The theorem's exact statement `ξ ≤ ⌈s(s+1)/3⌉`,
  Fibonacci-mod-2 equality, is quoted verbatim from the abstract by two
  independent search hits.
- **Status of the claim:** this is a *catalogue-level sourced* fact about the
  Rule-90 interior, **not** verified by this run's program, and it is a
  characterisation of the interior only. It does not prove regeneration.
