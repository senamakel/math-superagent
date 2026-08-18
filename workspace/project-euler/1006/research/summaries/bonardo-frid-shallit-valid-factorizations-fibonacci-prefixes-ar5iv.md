# Bonardo, Frid & Shallit — The number of valid factorizations of Fibonacci prefixes

<!-- source: https://ar5iv.labs.arxiv.org/html/1806.09534 (arXiv:1806.09534; DOI 10.1016/j.tcs.2018.12.016) | full text at research/sources/bonardo-frid-shallit-valid-factorizations-fibonacci-prefixes-ar5iv.full.md -->

**Pierre Bonardo, Anna E. Frid, Jeffrey Shallit** (2019). Theoretical Computer Science 775:68–75. (Aix-Marseille / Waterloo.)

## What it establishes

- **Objects.** f the Fibonacci word (fixed point of μ: a→ab, b→a), f_n the finite Fibonacci words, and V(n) the number of *valid representations* (factorizations) of the length-n prefix f(0..n] into a (not necessarily strictly) decreasing sequence of standard Fibonacci words f_i.
- **Theorem 1 (main).** If f[n]=a then V(n) = ⌈n/φ²⌉, equivalently V(n) = (# of occurrences of b in f(0..n]) + 1. If f[n]=b then V(n) = ⌈n/φ³⌉, equivalently V(n) = (# of occurrences of aa in f(0..n]) + 1. So V(n) is the shuffle of the ceilings of two linear functions of n.
- **Context (Lemma 1, §2).** Fibonacci (Zeckendorf) representations: every N has canonical form [k_n…k_0]_F with k_{i+1}−k_i ≥ 2; the word language of canonical representations is the regular expression ε + 1(0+01)*. The morphism μ sends f(0..[k_n…k_0]_F] to f(0..[k_n…k_0 0]_F] (shift in the Fibonacci numeration). Confirms the Fibonacci word is Sturmian of slope 1/φ² with f[n] = a iff {n/φ²} < 1−1/φ² (Example 2.1.24 of Lothaire [3]).
- **§4 (Fibonacci-regular representation).** V(n) is Fibonacci-regular (Theorem 2), i.e. computable by a finite automaton on the Zeckendorf representation of n.

## Why it matters for PE1006

This is the frontier's top research row (cited-by 16) that the run previously had only a 110-byte failed-download stub for. Its Lemma 1 / Zeckendorf-prefix machinery is exactly the Ostrowski/Zeckendorf structure the run's mechanical-word and position-theorem work uses; its V(n) (counting factorizations into standard Fibonacci words) is a Fibonacci-regular sequence with an explicit ceil-of-linear closed form — a model for the kind of exact closed form the run seeks for Ψ. It does NOT give Ψ(k) itself.

## Status

Full text on disk, read and verified. Summary written by librarian (the automatic digest is superseded).
