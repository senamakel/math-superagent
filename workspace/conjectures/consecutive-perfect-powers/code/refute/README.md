# Refute — adversarial checks

Counterexample and independent-verification attempts against this run's claims.

- `hminus_exact_check.py` — independent exact (sympy algebraic, no floats)
  verification of the minus-class-number formula `h^-(Q(zeta_p)) = 2p *
  prod_{chi odd} (-1/2 B_{1,chi})`, cross-checking the two float-based "routes"
  the board flagged as not independent.
