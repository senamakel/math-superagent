# Wikipedia — "Hasse derivative"

Source URL: https://en.wikipedia.org/wiki/Hasse_derivative
Full text: `research/sources/wikipedia_hasse-derivative.full.md`.

## What it establishes

The Hasse derivative `D^k f` of a polynomial `f = Σ a_n x^n`:
`D^k f = Σ C(n,k) a_n x^{n−k}`, defined **without the k! factor**. Key
properties: it is char-free (never identically zero in positive
characteristic, unlike the ordinary derivative); in characteristic 0,
`D^k f = f^{(k)}/k!`; the Taylor expansion `f(x+t) = Σ_k D^k f(x) t^k`; the
chain rule analogue; the relationship to the formal derivative over `ℤ[x]`.

## Bearing on the run

- This is the precise object that resolves the run's `hasse-vs-ordinary`
  contradiction (claim `bad-prime-lists-hasse-formulation`): the published
  bad-prime lists (Castryck et al. 2012 Def 1; Schaub–Spivakovsky) use Hasse
  derivatives. In char p the ordinary derivative vanishes for i ≥ p, so the
  ordinary hypothesis degenerates; the Hasse formulation is the correct one.
- The run's oracle keeps both (`is_ca` ordinary and `is_ca_hasse`); they agree
  in char 0 and for p ≥ n. This entry is the reference for the definition in
  the library.

Claim status: reference-level definition (textbook algebra fact; matches the
definitions used in the held Graf-von-Bothmer and Castryck et al. texts).