# The fold's second moment as an analytic trace: Bessel–Nevanlinna counting

```approach
idea: >
  Attach a two-variable generating function to the fold's second moment,
  G(x,y) = sum_{n>=0} sum_{d,d'} z^{|M_d △ M_{d'}|} x^d y^{d'}, using the
  proved meet formula |M_d △ M_{d'}| = 2^pc(d)+2^pc(d')-2^{pc(d∧d')+1}.
  The double sum over (d,d') has a closed form as an infinite product over
  the bit positions (the meet-and-join semilattice is a product of Boolean
  lattices). The number of (d,d') pairs in [2,n-1]^2 with symmetric
  difference exactly k is then the coefficient of a modular form or a
  theta-type function whose growth is a classical analytic fact. The open
  arithmetic input E[S(n)^2]=O(n) becomes a statement about the boundary
  values of this generating function, priced by the Bessel/Nevanlinna
  structure of the counting function of the meet lattice.
mechanism: >
  Named machinery: generating functions / theta series over the Boolean
  meet-semilattice, and the classical theory of the counting function
  (Hardy–Ramanujan / Nevanlinna for meromorphic boundary). The identity to
  be exploited is exact and already proved: the meet formula
  (downset-row-intersection-meet-formula) makes the double sum factor over
  bits. This is a different object from the refuted
  fold-second-moment-krawtchouk (which diagonalizes via Krawtchouk on the
  row code) and from the unchecked mobius-meet-factorization (which factors
  the monomial over M_d △ M_{d'}; here we factor the COUNTING function over
  the (d,d') index lattice, a pure function of n with no primes).
status: proposed
first-step: >
  symbolic_math + tool_builder, exact arithmetic. (1) Derive the closed
  form of the double sum F_n(z) = sum_{d,d'} z^{|M_d △ M_{d'}|} as a
  product over bits using the meet formula, and verify it against direct
  enumeration for n <= 64. (2) Identify the growth of F_n(z) near z=1 (the
  second moment threshold) from the product form. (3) Determine the
  analytic class (rational in z for fixed n? a theta-type function in n?)
  and state what boundary asymptotics it implies for E[S(n)^2]. FALSIFIER:
  if the product form does not match direct enumeration, the meet formula
  fails to factor the counting function and the route dies.
falsifies: >
  (a) product form mismatches enumeration; (b) the counting function has no
  closed analytic boundary form (no Bessel/Nevanlinna structure); (c) the
  boundary asymptotics give only the already-known O(n) fair-model bound
  and add no pricing of the prime input.
```
