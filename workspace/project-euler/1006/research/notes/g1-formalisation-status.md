# G1 formalisation — what is proved, what is not

Node `G1-sturmian-factor-structure`.  File:
`code/lean/pe1006_psi_G1_sturmian_factor_structure-87f94deb.lean`.

The node's *full* claim — "k+1 distinct Fibonacci subwords of length k, equal
to the length-k factors of the infinite Fibonacci word" — is **not** yet
`formalised`: its count half ends in `sorry`.  Below, two claims that *are*
established by the kernel (the second is the statement's own oracle, computed),
each filed with an honest status.

```claim
id: g1-factor-chain-nested
statement: For S_n = S_0=0, S_1=01, S_{n+2}=S_{n+1}S_n, the length-k contiguous
      factor sets form a monotone nested chain: FactorSet(fibWord n, k) ⊆
      FactorSet(fibWord (n+1), k) for all n, k.  In particular FibSubwords k =
      ⋃_n FactorSet(fibWord n, k) is a monotone (increasing) union, so the
      object the count k+1 is asserted over is well-defined.
hypotheses: S_n defined as in PE1006; k, n any naturals (no k≥1 needed here).
holds-here: true — the factor of a prefix is a factor of the whole word, and
      S_n is a prefix of S_{n+1}.
status: formalised
formalisation: code/lean/pe1006_psi_G1_factor_chain-87f94deb.lean
      (factorSet_prefix_nest, factorSet_chain, factorSet_chain_any; kernel
      verdict: verified, axioms propext, Quot.sound — sorry-free)
bearing: fixes the nesting that underlies "the set of Fibonacci subwords" once
      the limit word is introduced; the shell of the node.
anchor: code/lean/pe1006_psi_G1_factor_chain-87f94deb.lean
```

```claim
id: g1-oracle-length3
statement: The length-3 Fibonacci subwords are exactly 001, 010, 100, 101 —
      i.e. the length-3 factor set of S_5 = 0100101001001 has card 4 = 3+1 and
      equals {001,010,100,101}.
hypotheses: S_5 = 0100101001001 (S_4++S_3 = 01001010 ++ 01001).
holds-here: true — matches problem.md's example exactly.
status: checked (computed by native_decide in the same file)
bearing: reproduces the statement's own worked oracle, so the formal FactorSet
      definition agrees with the problem's notion of distinct length-k subword.
anchor: code/lean/pe1006_psi_G1_sturmian_factor_structure-87f94deb.lean
```

The count theorem `fib_subword_count : (FibSubwords k).ncard = k+1` remains a
declared gap (Sturmian factor complexity), and the identification with the
infinite limit word is likewise gapped (aperiodicity / stabilisation).  See
`research/backward/g1-sturmian-factor-structure.md` for the decomposition.
