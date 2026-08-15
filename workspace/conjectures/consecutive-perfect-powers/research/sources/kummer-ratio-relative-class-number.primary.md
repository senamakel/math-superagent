# The Kummer ratio and the relative class number of prime cyclotomic fields (primary)

**Source URL:** https://arxiv.org/html/2402.13829
**Authors:** Neelam Kandhil, Alessandro Languasco, Pieter Moree, Sumaia Saad
Eddin, Alisa Sedunova, "The Kummer ratio of the relative class number for prime
cyclotomic fields", arXiv:2402.13829 (2024).
**Type:** freestanding research preprint (arXiv HTML).
**How obtained:** full-text readout via `read_sources` (server-side). The host
is blocked for direct `download_document`; only the server-side readout is
available. Nothing further is stored as a PDF.

## Why this source is in the library

The run's open content is the both-odd-prime case of `x^p - y^q = 1`, whose
obstruction is the class group of `Q(zeta_p)`. The open request
`exact-statement-mihailescu-bbf8` asks whether a hypothetical second solution
forces *cross-prime minus-class-number divisibility* `q | h^-(Q(ζ_p))` (and
mirror `p | h^-(Q(ζ_q))`). This source supplies the precise relationship between
divisibility of the full class number by `q` and divisibility of the *relative*
(minus) class number by `q` — Kummer's theorem — plus the Maillet-determinant
algorithm that computes `h_1(q)` exactly. It is the machinery for deciding
whether such cross-prime divisibility can be established, and at what cost. It
supplies **no** bound, exclusion, or answer for `x^p - y^q = 1` itself.

## Exact statements captured

**Definition (relative class number / first factor).** For an odd prime `q`
and `K = Q(ζ_q)`, `h_1(q) := h(q) / h^+(q)` where `h(q) = #Cl(K)` and
`h^+(q)` is the class number of the maximal real subfield `Q(ζ_q + ζ_q^{-1})`.
Kummer proved this is an integer. It is the same object this library calls
`h^-(Q(ζ_p))` — the relative / minus class number.

**Kummer's q-divisibility criterion.** `q | h(q)` if and only if
`q | h_1(q)`. (Kummer.) Since the run's cross-prime question is about a prime
`q` dividing the *minus* class number of `Q(ζ_p)` — a different prime `p` — this
criterion is for the case where the dividing prime equals the conductor, but the
underlying relationship (full class number modulo divisibility by a prime splits
onto the minus part) is the structural fact at play. Any claim that a dividing
prime forces non-triviality must be stated against it.

**Maillet determinant (Carlitz–Olson 1955).** For `n` coprime to `q`, let `n'`
be the least positive inverse of `n` mod `q`, and `A(n,q)` the least positive
residue of `n` mod `q`. Set `M_q = (A(m n', q))_{1 ≤ m, n ≤ (q-1)/2}` (a
`(q-1)/2 × (q-1)/2` matrix). Then

    det(M_q) = ± q^{(q-3)/2} · h_1(q).

This gives an exact-integer algorithm for `h_1(q)` — a genuinely different route
from the Bernoulli-product formula already in the library, so it can serve as an
independent oracle route for `h^-(Q(ζ_p))` in `code/`.

**Bounds on h_1(q).** Carlitz: `h_1(q) ≤ ((q-5)/4)!` for `q ≡ 1 (mod 4)`;
`h_1(q) ≤ ((q-7)/4)!·((q-3)/4)!` in general. Metsänkylä (1972):
`h_1(q) < 2q(q/24)^{(q-1)/4}`. Feng (1982):
`h_1(q) < 2q·q^{(q-1)/31.997158·...}`. Fung–Granville–Williams (1992) computed
`h_1(q)` exactly for `q < 3000` via determinants; Kummer computed by hand to
`q = 163` (with three arithmetic slips).

**Analytic class-number input.** With `G(q) := 2^q q^{(4π^2/q - 1/4)}` (as in the
paper), `R(q) := h_1(q)/G(q)` is the Kummer ratio and `r(q) = log R(q)`. The
paper's content is effective bounds on `R(q)` under hypotheses on Siegel zeros of
odd Dirichlet `L(s, χ)`, and an FFT algorithm computing `r(q)` (and hence
`h_1(q)`) with `O(q log q)` operations and `O(q)` memory.

## Relation to the known solution

The known solution `(x,p,y,q) = (3,2,2,3)` has `p = 2` even, so no odd-conductor
class-number machinery applies to it. This source never asserts existence or
non-existence of any solution; it only measures the class group. The falsifier
discipline is intact: nothing here implies "no solution exists."

## Status

- Sourced primary statements from an arXiv preprint; not yet re-derived
  in-workspace.
- The Maillet-determinant identity `det(M_q) = ± q^{(q-3)/2} h_1(q)` is a
  candidate **independent oracle route** for `h^-(Q(ζ_p))`, to be checked
  against the Bernoulli-product formula (claim `minus-class-number-formula`).
- **Verification status:** a direct integer check of `det(M_q) = ±q^((q-3)/2) h_1(q)`
  against the catalogued values `h^-(Q(ζ_q))` (OEIS A000927: q=3→1, 5→1, 7→1,
  11→1, 13→1, 17→1, 19→1, 23→3, 29→8, 31→9, 37→37, 41→121, 43→211) is
  **proposed but NOT yet run** in this librarian session (no execution tool was
  available here). The script `code/out/maillet_verify.py` encodes this check;
  it must be executed and its output read before the `maillet-determinant-equals-class-number`
  claim is promoted from `sourced` to `checked`. Until then report it as sourced only.

## Claims

```claim
id: kummer-q-divides-h-iff-q-divides-h1
statement: >
  For an odd prime q and K = Q(zeta_q), q | h(K) if and only if q | h_1(q),
  where h_1(q) = h(K)/h^+(K) is the relative (minus) class number. Equivalently,
  divisibility of the class number by the conductor q is detected by the minus
  part alone.
hypotheses: q an odd prime; h the class number of Q(zeta_q), h^+ the class
  number of the maximal real subfield, h_1 = h/h^+ the relative class number.
holds-here: >
  yes — the minus part of the class group of an odd-conductor cyclotomic field
  is exactly where q-divisibility is decided; this is the relationship the
  open request about cross-prime minus-class divisibility must be stated
  against. (Note it concerns the prime q equal to the conductor, whereas the
  run's cross-prime question concerns a different prime p dividing h^-(Q(zeta_q));)
  the criterion is the structural anchor, not the answer.
status: sourced (Kummer, as reported in arXiv:2402.13829).
anchor: research/sources/kummer-ratio-relative-class-number.primary.md
bearing: fixes where divisibility of a class number by its conductor's prime is
  decided — the minus part — which is the part computable; bounds any claim that
  a prime forces class-group non-triviality.
```

```claim
id: maillet-determinant-equals-class-number
statement: >
  For an odd prime q, with n' the least positive inverse of n modulo q and
  A(n,q) the least positive residue of n modulo q, the (q-1)/2 by (q-1)/2
  matrix M_q = (A(m n', q))_{1 <= m,n <= (q-1)/2} satisfies
  det(M_q) = +- q^((q-3)/2) * h_1(q), where h_1(q) is the relative class number
  of Q(zeta_q).
hypotheses: q an odd prime.
holds-here: yes — gives an exact-integer, determinant-based route to
  h^-(Q(zeta_p)) that is independent of the Bernoulli-product formula in the
  library; a candidate second route for the oracle (rule 11).
status: sourced (Carlitz–Olson 1955, as reported in arXiv:2402.13829); not yet
  re-derived in-workspace.
anchor: research/sources/kummer-ratio-relative-class-number.primary.md
bearing: an independent algorithm for the computable half of the obstruction;
  enables a second-route check of minus-class-number-formula.
```
