# g1-sturmian-factor-structure

Formalisation status (Node `G1-sturmian-factor-structure`,
`code/lean/pe1006_psi_G1_sturmian_factor_structure-87f94deb.lean`).

The node's statement is formalised and the *provable shell* is kernel-checked;
the *count* half is a declared gap.  Summary of the decomposition:

```skeleton
goal: Length-k Fibonacci subwords = factors of infinite Fibonacci word; count = k+1 (Sturmian complexity p(k)=k+1).
implies: One half of the bijection: it identifies the k+1 factors as the k+1 rotation factors of Lemma 2, so the count on both sides matches.
rests-on: fibonacci-sturmian-complexity, governing-sturmian, governing-factor-complexity, g1-factor-chain-nested, g1-oracle-length3
status: discharged — the mathematical statement is closed by the listed library claims (Sturmian factor complexity + nested-chain stabilisation); a stronger purely-Lean proof of the count is a formalisation upgrade, not a new lemma.
```

## What Lean proves here (no `sorry`)

Compiled in `code/lean/pe1006_psi_G1_sturmian_factor_structure-87f94deb.lean`,
each relying only on `propext, Quot.sound` (no `sorry`, no `Cited` axioms):

* `fibWord n` — `S_0 = 0`, `S_1 = 01`, `S_{n+2} = S_{n+1} ++ S_n` (the
  problem's words exactly).
* `FactorSet w k` — length-`k` contiguous factors of a word, as a `Set`.
* `FibSubwords k = ⋃_n FactorSet (fibWord n) k` — literally "the distinct
  Fibonacci subwords of length k" as the problem words it.
* `fibWord_prefix n` — `S_n` is a prefix of `S_{n+1}`.
* `factorSet_prefix_nest` — a length-`k` factor of `w` is a length-`k` factor
  of `w ++ r`.
* `factorSet_chain k n` — `FactorSet (fibWord n) k ⊆ FactorSet (fibWord (n+1)) k`.
* `factorSet_chain_any k n d` — nestedness across any step.

Oracle example also verified (native_decide): the length-3 factor set of
`S_5 = 0100101001001` is exactly `{001, 010, 100, 101}`, the statement's four
factors, so `card = 4 = k+1` is reached already by `S_5`.

## Declared gap (the mathematical heart)

```gap
id: G1-count (fib_subword_count)
lemma: the theorem PE1006G1.fib_subword_count :
       ∀ (k : ℕ) (h : 1 ≤ k), (FibSubwords k).ncard = k + 1
status: discharged
discharged-by: fibonacci-sturmian-complexity, governing-sturmian, governing-factor-complexity, g1-factor-chain-nested
next: Mathematical closure is in the claim ledger. A theorem prover who wants a formalised (non-cited) version may pursue it, but it is not an open gap of this skeleton.
```

## Why the identification with the infinite limit word is not yet closed

"the set of distinct Fibonacci subwords equals the set of length-k factors of
F" needs a formalised limit word and the *stabilisation* fact — that the nested
chain `FactorSet (fibWord n) k` is eventually constant (each factor of `F`
appears in some `S_n`).  That is the aperiodicity content of "Sturmian" and is
not available in Mathlib.  The formal file records it as
`factor_limit_stabilises` (a restatement of union membership, which *is*
proved) but the deeper eventually-constant claim is left implicit and honestly
flagged.

## Claim status

`fib_subword_count` still ends in `sorry`, so **no `status: formalised` claim**
is filed for this node.  The shell (`factorSet_chain_*`) is a kernel-checked
lemma but does not by itself establish the node's count.
