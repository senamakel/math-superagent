# Han Yu, "Additive properties of numbers with restricted digits"

Source: arXiv:2004.05926 (2020), Algebra & Number Theory 15 (2021) 1283–1301. Full text: [[han-yu-2020-higher-dim-furstenberg-restricted-digits.full]].

## What it establishes

Let `B_b` = integers whose base-`b` expansion uses only digits `{0,1}`. For integers `a,b,c ≥ 3`, under mild (mutual non-degeneracy) conditions:

```
#((B_a + B_b) ∩ B_c ∩ [1,N]) = O(N^ε)   for every ε > 0.
```

So a **sum** of two restricted-digit sets is very thin (subpolynomial in N) against a third restricted-digit set. Verified in the full text: abstract at line 25–27 states exactly this estimate.

## Implication for this problem

- `B_3` is *exactly* the digit-`{0,1}` set `S` the Erdős problem concerns (`2^n` digit-2-free ⟺ `2^n ∈ B_3`).
- The theorem is about the *sum* `B_a + B_b` meeting `B_c`; it is a density/additive-transversality statement about where `B_3` sits additively.
- **It does not reach the powers of two.** `2^n` is a thin geometric sequence, not all of `B_3` nor a sum `B_a+B_b`. A density statement about the size of a set does not say which integers (in particular which `2^n`) lie in it. This is exactly the density-trap distinction in `problem.md`. Confirms rather than contradicts `BURRELL-YU-DENSITY-VS-THIN-SEQUENCE` and `naive-density-as-proof`.

## Status

Sourced; full text held. Background on additive structure of restricted-digit sets; does not contribute a proof step toward Erdős.

```claim
id: HAN-YU-2020-B3-SUM-THIN
statement: For a,b,c ≥ 3 (non-degenerate), #((B_a + B_b) ∩ B_c ∩ [1,N]) = O(N^ε) for every ε > 0, where B_b is the digit-{0,1} set in base b.
hypotheses: a,b,c ≥ 3 integer bases related non-degenerately.
holds-here: yes
status: asserted
bearing: an additive-thinness statement about restricted-digit sets; does NOT constrain which 2^n lie in B_3 = S, so it is background confirming the density-trap (a set-size statement is not a which-integers statement).
anchor: research/summaries/han-yu-2020-higher-dim-furstenberg-restricted-digits.md
```
