# Approach: backward covering via the Stérin finite-state transducer

```approach
idea: Study the backward Collatz graph through regular predecessor languages and ask whether their union covers all positive binary strings.
mechanism: For T0(x)=x/2 and T1(x)=(3x+1)/2, Stérin proves that, for every x and fixed k, EPred_k(x)—binary representations of ancestors reaching x with exactly k uses of T1—is a regular language and gives an explicit regular expression. Stérin–Woods use finite-state transducers inside a Collatz cellular-automaton/base-conversion model. These theorems hold for fixed k. They do not state that the countable union over k stabilizes, is regular, or is recognized by one fixed 4-state reversible FST. The published constructions instead record k-dependent complexity growth, which is evidence against treating stabilization as automatic. Since regular languages are closed under finite union, not arbitrary countable union, finite-language inclusion becomes available only if stabilization is independently proved — and no source proves it.
status: refuted
killed-by: The load-bearing stabilization hypothesis (the composed transducers converge to a finite covering language) is not a theorem in the cited literature and is contradicted as an inference by the published k-dependent growth bounds (Stérin 2019/2020). A countable union of regular languages need not be regular, so the reduction to finite language inclusion fails without it. The fixed-k regularity is a real theorem but gives only bounded-odd-step coverage certificates, not a decision procedure for the full conjecture.
precedent: https://arxiv.org/abs/1907.00775 (Stérin 2019); https://doi.org/10.1007/978-3-030-61739-4_8 (Stérin 2020); https://doi.org/10.1007/978-3-030-61739-4_9 (Stérin–Woods 2020); claim ids: reformulation-power-of-2, everett-parity-vector-bijection
first-step: n/a — closed; the fixed-k regularity theorem is available as a bounded-coverage tool but the full-covering reduction has no supporting stabilization lemma.
```

## Literature assessment

**What it is called.** The relevant established terminology is *k-span predecessor sets*, *regular structure of predecessor sets in the Collatz graph*, and *finite-state-transducer/CQCA representation*. The 2019/2020 works prove regularity for each fixed budget k, not a uniform regular presentation of the full ancestor set.

**Precise theorem and hypotheses.** For every natural x and every fixed k, the binary language EPred_k(x) of ancestors reaching x with exactly k applications of T1 (and arbitrary T0 applications) is regular; Stérin supplies an explicit regular expression whose size depends strongly on k. Stérin–Woods prove a base-conversion result in their CQCA model and describe dual FST components. These statements apply to finite prefixes/budgets and to the specified encodings. They do not imply that ⋃_{k≥0}EPred_k(1)=N⁺ is a finite-state language.

The union equality itself is a tautological reformulation of Collatz, but proving it is the original problem. The proposed “stabilization” is an additional conjecture. Since regular languages are closed under finite union, not arbitrary countable union, finite-language inclusion becomes available only if stabilization is independently proved. The cited papers instead record k-dependent complexity, which is evidence against treating stabilization as automatic (not a formal disproof of stabilization).

**What it would buy.** Fixed-k automata give exact, non-statistical coverage certificates for bounded numbers or bounded odd-step budgets. A genuine stabilization theorem would be dramatic: it would reduce the full conjecture to finite automata inclusion. At present the approach is grounded only in its finite-budget component; the proposed full covering reduction remains open rather than literature-supported.
