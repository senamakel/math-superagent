# Fibonacci-regular / linear-representation over the Zeckendorf base

```approach
idea: Show that the map k ↦ Ψ(k) is a Fibonacci-regular sequence (regular in the
  Zeckendorf/√5 numeration system), i.e. admits a finite linear representation:
  a finite set of matrices (one per digit of the Zeckendorf expansion of k) whose
  product, indexed by the Zeckendorf digits of k, computes Ψ(k). Then Ψ(10^18) is a
  fixed-size matrix product over the O(log 10^18) Zeckendorf digits of 10^18.
mechanism: The Fibonacci word f is Fibonacci-automatic (Mousavi–Schaeffer–Shallit 2015,
  "Decision algorithms for Fibonacci-automatic words", already in the library
  `sources/mousavi-schaeffer-shallit-fibonacci-automatic.full.md`). The substitution
  tree S_n = S_{n−1}S_{n−2} gives a recursive decomposition of the length-k factor set
  by the Zeckendorf representation of k, so the auxiliary data needed to evaluate Ψ(k)
  (the factor set, its values, their squares) evolves by a finite automaton reading the
  Zeckendorf digits of k. A "Fibonacci-regular" sequence in the sense of Allouche–Shallit
  then has a linear representation, giving Ψ(10^18) mod M by matrix products with exact
  arithmetic mod 101001001.
status: proposed
first-step: From the morphism 0→01, 1→0, derive by hand (or check against
  code/out/factors_k12.txt) a candidate state automaton that, reading the Zeckendorf
  digits of k, computes the k+1 factors' decimal values; verify a candidate linear
  representation reproduces Ψ(1..40) from code/out/psi_data_1_150.txt, then reduce
  10^18 to its Zeckendorf digits and matrix-multiply.
```

## Established vs speculation

- **Established (sourced, in library):** the Fibonacci word is Fibonacci-automatic
  (MSS 2015); regular sequences admit linear representations (Allouche–Shallit
  framework; the theory is standard, exact statements to be pulled from the library).
- **Speculation:** that Ψ(k) itself (or a fixed finite vector of auxiliary sequences
  including it) is Fibonacci-regular — i.e. the "no low-order constant-coefficient
  recurrence" obstacle (`PE1006-no-loworder-linear-recurrence`) is replaced by a
  *Zeckendorf-indexed* matrix system, which is exactly the structure Fibonacci-regular
  sequences have. This is the hypothesis research must check; it is compatible with
  the observed failure of ordinary linear recurrences and is not implied by it.

## Why different from the run

The run ruled out constant-coefficient linear recurrences in k and looked for a closed
form/state recurrence in the *word structure*. This approach changes the arithmetic of
the index: it evaluates Ψ over the Zeckendorf representation of k (Fibonacci base),
where the non-uniform, substitution-driven growth becomes a finite automaton / matrix
product. It is the automata-theoretic counterpart of the Ostrowski route, not a
variation of the lex-order enumeration.
