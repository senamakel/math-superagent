# Lean formalisation report

`code/lean/fibonacci_position_theorem_contiguous_windows-af501dab.lean` passed `lean_check`.

The theorem is conditional: its proof invokes `FibonacciPosition.Cited.proposition_one`, attributed in the source to Sivasankar and Rama, arXiv:2207.04304, Proposition 1. The kernel checked the implication with no `sorry`; the cited proposition itself remains an axiom.

Binder correspondence:
- `n`, `k`: the source indices.
- `hn : 2 ≤ n`: source hypothesis `n >= 2`.
- `hk₁ : fibLen n ≤ k`: source hypothesis `F(n) ≤ k`.
- `hk₂ : k < fibLen (n + 1)`: source hypothesis `k < F(n+1)`.

The finite model defines `fibWord`, `fibLen`, contiguous finite factors, the union `fibonacciFactors`, left rotation, and the prescribed rotation-index union. `fibLen` is the formal `F` because it is the length of the recursively defined finite Fibonacci word.

Axioms reported by `#print axioms`: `propext`, `Classical.choice`, `Quot.sound`, and `FibonacciPosition.Cited.proposition_one`. Thus this should be recorded as `status: conditional`, not unconditional formalisation, despite the kernel verdict being verified for the implication.
