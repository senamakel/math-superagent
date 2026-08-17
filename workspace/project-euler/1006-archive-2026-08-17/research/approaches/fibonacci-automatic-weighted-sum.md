# Approach: Fibonacci-automatic (Zeckendorf-automatic) weighted summation of Psi

```approach
idea: The Fibonacci word s_n is Fibonacci-automatic: there is a DFAO that outputs the n-th letter from the Zeckendorf (Fibonacci-base) representation of n. The k+1 distinct length-k factors are the windows at the k+1 "representative" starting positions, and those positions are themselves defined by a Fibonacci-regular predicate. Therefore the weighted double sum Psi(k) = sum over representatives n of (sum_{i<k} s_{n+i} 10^{k-1-i})^2 is the sum of a Fibonacci-regular function over a Fibonacci-regular index set; it is computable in O(log k) by the standard linear-representation summation method for automatic/regular sequences, with the powers of 10 carried as weights in a linear representation (exact integers, reduced mod M at the end).
mechanism: Fibonacci-automatic (a.k.a. Zeckendorf-automatic) sequences and their linear representations (Mousavi-Schaeffer-Shallit, "Decision algorithms for Fibonacci-automatic words"); summation of regular sequences via matrix products over the Zeckendorf digits of k; the weights 10^i are handled by a polynomial-weight linear representation, so the final number is exact and reduced mod 101001001 with exponent reduction mod ord_10(M).
status: proposed
precedent: unchecked
first-step: Implement the Zeckendorf automaton for s_n and check it reproduces the first ~1000 letters of the Fibonacci word against brute.py / the factor dump. Then formulate the predicate "n is a representative starting position for length-k factors" as a Zeckendorf automaton over (n,k) and verify against the k+1 distinct-window representatives already extractable from the factor matrix for k<=40; finally build the weighted linear representation whose summed value equals Psi(k) and confirm it reproduces Psi(1..40).
```

## Why this is a different setting

The two open threads both work in the *word combinatorics* setting (lex order, Christoffel
conjugates, column intervals). This approach moves the whole computation into the **formal
language / automatic sequences** setting: the infinite word is not a limit of morphisms but a
function `n -> s_n` computed by a finite automaton reading `n` in Zeckendorf base. Quantities
that are hard as Sturmian-word combinatorics become *matrix products over the digits of k*,
because automatic/regular sequences are closed under summation, and the running-sum / weighted-sum
machinery is a solved problem.

The no-small-recurrence finding (`PE1006-no-loworder-linear-recurrence`: Berlekamp-Massey
saturates, no C-finite recurrence of order <=40) does **not** rule this out: a Fibonacci-regular
sequence is generally *not* C-finite in `k` (it need only be finite-state over the Zeckendorf
representation), so the two diagnostics test different hypotheses. The automaton's state count is
bounded by the size of the morphism structure, not by `k`.

## What would kill it

If `Psi(k)` is *not* Fibonacci-regular — i.e. no finite automaton over Zeckendorf digits computes
it (with the `10^i` weights as a linear representation) — then the summation method returns no
finite linear representation and the approach fails. The check is constructive: build the
automaton from the `k<=40` data and see whether a finite state set closes; if states keep
proliferating with no bound, it is refuted.

## Relation to the Rauzy-graph approach

Both end in matrix products, but over different index sets: the Rauzy-graph approach iterates the
substitution on *graphs of factors* (dynamical systems), while this one iterates a finite
automaton on the *Zeckendorf digits of n and k* (formal language). They are independent
certificates and can cross-check the same final value.
