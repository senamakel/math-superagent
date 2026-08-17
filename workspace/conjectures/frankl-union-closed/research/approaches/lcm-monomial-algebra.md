```approach
idea: Commutative-algebra reformulation. Under the monomial bijection A ↦ x^A =
  ∏_{i∈A} x_i, a union-closed family F (with ∅, V ∈ F) is exactly a set of
  monomials in k[x_1,…,x_n] containing 1 and closed under lcm — a
  sub-join-semilattice of the divisibility lattice that is closed upward under
  duals. Attach to F the monomial ideal I_F it generates and its Alexander dual,
  and read abundance off the Hilbert series / the minimal free resolution. The
  named theorem is Gasharov–Peeva–Welker: the minimal free resolution (Betti
  numbers, Hilbert series) of a monomial ideal is a function of its lcm-lattice
  — here exactly the family's ∪-structure — together with Alexander duality
  (Miller–Sturmfels). The distinctive point against the already-adopted Möbius
  semigroup algebra C[L,∨]: that approach works in the *semigroup algebra of the
  lattice* and its orthogonal idempotents; this one works in the *quotient ring
  k[x]/I_F and its free resolution / Hilbert function*, a different algebra whose
  invariants have never been tied to the abundance ≥ 1/2 question.

mechanism: δ(i) = #{A ∈ F : i ∈ A} is the number of monomials of F divisible by
  x_i, so the abundance vector is a derivative of the monomial-count
  (Hilbert) generating function. On the other hand the lcm-closure means the
  "primitive"/minimal monomials of I_F (join-irreducibles of the lcm-lattice)
  generate the whole resolution, and GPW pins the Betti numbers to that
  lcm-lattice. A counterexample (all δ(i) < m/2, m = |F|) is a statement that
  every variable divides fewer than half the monomials of an lcm-closed set —
  equivalently that the *Alexander-dual* complex has every vertex in more than
  half of ... , a parity/shifting condition topological rather than
  moment/entropy. The hope: an exact algebra identity (Hilbert-series or Betti
  inequality forced by lcm-closure) that forces max_i δ(i) ≥ m/2, of a kind the
  adopted Möbius semigroup algebra does not see because it never moves to the
  quotient ring/resolution. Marked speculative: the honest, checkable content is
  whether any algebraic invariant of I_F distinguishes the abundant variable.

status: proposed

first-step: With the canonical oracle, for each union-closed family on n ≤ 5
  (∅,V ∈ F), (1) write I_F and its Alexander dual I_F^∨; (2) compute the Hilbert
  series and the full Betti table of k[x]/I_F (or the minimal free resolution as
  a chain complex) by exact Gröbner/linear algebra (sympy for n ≤ 4, degree
  reverse-lex); (3) record whether max_i δ(i) − m/2 and each variable's
  divisibility count appears as a Hilbert-series coefficient or Betti number of
  a dual object, and test the three negative controls (2^[n] must give every
  δ(i) = m/2 exactly; a non-union-closed family breaks lcm-closure so I_F's
  resolution is NOT pinned by the same lcm-lattice; finiteness via m ≤ 2^n). If
  no algebraic invariant tracks abundance for n ≤ 5, say so — that is itself a
  negative result bounding this route.
```
