# Run-length signed representation + Zsigmondy/LTE valuation invariant

```approach
idea: Encode a digit-{0,1} power of 2 by its *runs* of 1s. A run of length r at
  position s contributes 3^s(3^r - 1)/2, so 2^{n+1} = sum_j (3^{s_j+r_j} - 3^{s_j}),
  a signed {+1,-1}-coefficient sum of *distinct* powers of 3 with a pairing.
  Take v_2 of both sides; LTE and Zsigmondy (primitive divisors of 3^r-1) force a
  2-adic cancellation tree over the run multiset. A *middle-digit invariant*.
mechanism: v_2(RHS) is achieved only through a chain of cancellations among
  minimal-valuation terms; v_2(LHS) = n+1. The conjecture becomes: the forced
  cancellation condition has exactly the three witness run multisets.
status: refuted
killed-by: Two independent fatal defects, both verified by exact hand arithmetic
  (see research/candidate-precedent-handcheck.md):
   (1) The v_2 identity carries NO digit information. For ANY integer m with
       ternary runs {(s_j,r_j)}, m = sum_j 3^{s_j}(3^{r_j}-1)/2, so
       2m = sum_j (3^{s_j+r_j}-3^{s_j}) is an IDENTITY -- the definition of 2m
       in run form. Setting m=2^n gives v_2(RHS) = v_2(2^{n+1}) = n+1 for every n,
       digit-free or not. There is no digit-{0,1} hypothesis anywhere in the
       valuation line: the same runs-and-valuations identity holds if any of the
       runs are replaced by a different integer with the same run lengths. The
       'invariant' is vacuous.
   (2) The stated witness decomposition is miscomputed. 2^8=256=100111_3 has
       positions 0,1,2 all equal to 1 -- ONE run of length 3 at s=0, plus a
       length-1 run at s=5: {(0,3),(5,1)}, NOT {(0,2),(2,1),(5,1)}. The file's
       centerpiece '8 + 18 + 486 = 512' splits a contiguous run and is built on
       that error. The correct identity is 3^0(3^3-1)/2 + 3^5(3^1-1)/2 = 256.
precedent:
  - "LTE (Lifting-the-Exponent): v_2(3^r-1) = 1 (r odd), 2+v_2(r) (r even). A
     standard, re-derivable identity -- but it applies to 3^r-1 for every r
     regardless of digits, so it constrains run LENGTHS only, never positions,
     and is satisfied by arbitrarily many run multisets."
  - "Zsigmondy / Bang-Zsigmondy: 3^r-1 has a primitive prime divisor for all
     r>1 except r=6. Also constrains lengths only, never offsets s_j; the
     primitive divisors are irrelevant to which of the three digit-{0,1} patterns
     occurs."
  - "Zsigmondy generalisations (Avci 2020 arXiv:2011.06136; backward orbits
     ScienceDirect S0022314X22002451) are about existence/absence of primitive
     divisors in Lucas-type sequences -- a length-side phenomenon with no
     position content."
```

## Verdict

**Refuted, on evidence.** Two independent kills, both exact and hand-checked:

1. **Vacuity.** The core identity `2^{n+1} = Σ(3^{s_j+r_j}−3^{s_j})` is true for
   *every* integer `m` written in run form, not only digit-{0,1} powers; setting
   `m=2^n` turns `v_2(LHS)=n+1` into a tautology. A run-and-valuation identity
   that holds for arbitrary integers cannot be a symbolic invariant distinguishing
   digit-{0,1} powers — it never uses the digit hypothesis. This is the same trap
   as the density trap: a true statement about all integers that says nothing
   about the thin sequence.
2. **Miscomputed witness.** The motivating `n=8` decomposition is wrong: `256 =
   100111_3` has a single run `111` at positions 0,1,2, not two runs `11,1`.
   The `8+18+486` chain does not equal the run decomposition of `256`; the correct
   run contribution is `13 + 243`. And under the correct decomposition the
   "cancellation tree" reduces to a tautology, so nothing survives to be a
   conjecture.

Because the invariant is vacuous, there is **no middle-digit constraint** to
recover from it; the residue-class-count task (`verify-2adic-constraint-family`)
that it claimed to refine is similarly a pure-2-adic additive partition with no
digit-{0,1} content beyond the already-proved `|A_k|=2^{k-1}` counting. Every
claimed obstruction must also pass the falsification oracle `n=0,2,8`; a vacuous
invariant passes it trivially, which is precisely the sign it is not an
obstruction.
