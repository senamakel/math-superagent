# Northshield — Sums across Pascal's triangle modulo 2

"Sums across Pascal's triangle modulo 2", *Congressus Numerantium* 200 (2010),
35 pp (Sam Northshield, SUNY Plattsburgh). Item record held (DSpace, both the
old handle 1951/69939 and the moved handle 20.500.12648/1110); the full-text
PDF bitstream (196.71 KB) exists at the repository but the bitstream endpoint
did not pass through the converter (returned a DSpace stub, no text). No other
open full text found (the journal-article sibling *Integrating across Pascal's
triangle*, J. Math. Anal. Appl. 374(2) 385–393, 2011, is paywalled).

## Abstract-level content (sourced)

The paper studies sums of binomial coefficients `C(i+j, i)` modulo 2 over
lines `a·i + b·j = n` in Pascal's triangle. Key cases:

- **(1,1) case** `(i+j=n)`: gives Gould's sequence `g(n) = Σ_{i+j=n} C(i+j,i) mod 2`,
  characterisable via binary representations of `n`.
- **(2,1) case** `(i+2j=n)`: gives `F_{n+1} ~ C·φ^n` (Fibonacci) via
  hyperbinary representations of `n`.
- **(3,1) case**: generating function `A(x) = (1+x+x³)A(x²)` and a recursion,
  with a combinatorial interpretation in terms of "3,1-hyperbinary"
  representations of `n`.
- Generalisation to modulo 3 along lines, with generating functions
  `T(x)` and recurrences `q_m(x)`.

The central technique is the functional equation `A(x) = P(x)·A(x²)` for
mod-2 binomial sums — the algebraic (generating-function) form of the Rule-90 /
Pascal-mod-2 structure this run proved for the halved `{0,2}` interior.

## Why it was flagged / bears on the run

This run's durable memory named Northshield's generating-function machinery as
the algebraic analogue of the Rule-90 edge convolution
`e_d = XOR_j [C(d,j) mod 2]·h[...]` (the halved edge of a block under
erosion). The `(1,1)`-case Gould-sequence result is exactly the count of odd
binomial coefficients in row `n` of Pascal's triangle mod 2 — the pattern of
edge-2 reads over `n` steps of erosion. So it is a lead on the interior
frequency half of regeneration, not a regeneration proof.

```claim
id: northshield-pascal-mod2-line-sums-gf
statement: Sums of binomial coefficients C(i+j,i) mod 2 along lines ai+bj=n satisfy functional equations A(x)=P(x)·A(x²); the (1,1) case is Gould's sequence (count of odd entries in row n of Pascal's triangle mod 2) and the (2,1) case is the Fibonacci sequence. This is the algebraic form of the Rule-90 edge convolution.
hypotheses: mod-2 binomial sums; Gould's sequence counts the pattern of edge-2 reads over n erosion steps of a halved {0,2} block.
holds-here: yes — the halved interior is Pascal mod 2, so the edge-read pattern over n steps is exactly the (1,1)-case Gould sequence.
status: sourced (Northshield 2010, Congressus Numerantium 200, item record + abstract); full text not obtained (bitstream blocked/paywalled); NOT verified by this run's program.
bearing: a lead on the algebra of the Rule-90 edge pattern; interior structure only, does not prove regeneration.
anchor: research/summaries/northshield-sums-across-pascals-triangle-mod2.md; hdl 20.500.12648/1110
answers: what-algebra-governs-the-edge-read-pattern
```

## Status and provenance

- **Full text:** NOT held (bitstream download blocked by converter; journal
  sibling paywalled). Recorded so nobody re-attempts the repository bitstream.
- **Content:** sourced from the item record and the paper's own abstract via
  search; the exact functional-equation technique is confirmed by the search
  extract and by Northshield's own citation in the J. Math. Anal. Appl. 2011
  follow-on.
- **Status of the claim:** this is a *catalogue-level sourced* fact about the
  Rule-90 interior and its edge-read pattern; **not** verified by this run's
  program; does not prove regeneration.
