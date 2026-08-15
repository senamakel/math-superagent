# Sinnott, "On the Stickelberger Ideal and the Circular Units of a Cyclotomic Field"

- Source: W. Sinnott, *Annals of Mathematics* **108** (1978).
- URL: https://doi.org/10.2307/1970932
- Abstract and content retrieved via `read_sources` on 10.2307/1970932
  (server-side). **Full text NOT obtained** (network boundary blocks publisher
  hosts). The summary below records what the abstract and readout established.

## What the source establishes

For an imaginary cyclotomic field `k` (conductor `m`, `k = Q(ζ_m)`) with
maximal real subfield `k+`, let `G = Gal(k/Q)`, `R = Z[G]`, `h` the class number
of `k`, `h+` the class number of `k+`, and `h- = h/h+`. Two objects: the
Stickelberger ideal `S` of `R`, and the circular (cyclotomic) units `C` of `k`.
Complex conjugation `j` splits each Z[G]-module into `+` and `-` parts.

The paper's main result (from abstract):
- **[R- : S-] = h-** on the minus part: the Stickelberger ideal, tensored where
  needed, has index exactly the minus class number `h-` (up to the stated
  computable factors). This is the link between the Stickelberger/cyclotomic-unit
  machinery and the minus class group.
- **[E+ : C+]**, the index of the circular units in the full unit group on the
  plus (totally real) part, is computed in terms of `h`, `h+`, and unit data.

The minus-part index identity `[Z[G]- : S_G-] = h_p-`
for `k = Q(ζ_p)` is Iwasawa's result (Iwasawa, "A Class Number Formula for
Cyclotomic Fields", *Ann. Math.* **76** (1962), DOI 10.2307/1970270), which
Sinnott's framework extends.

## Why the run wants it

This is the machinery named by the skeletons' hard gap: `G-odd-descent` /
`odd-prime-contradiction` rest on the minus class group of `Q(ζ_p)` via the
Stickelberger ideal and cyclotomic units, and the problem framing says the
obstruction for `x^p − y^q = 1` with both exponents odd is exactly the failure
of these ideals to be principal. This source fixes the definition and the
index relation that would convert an ideal relation into an element relation.

## Status

- **Technique reference, not a claim about `x^p − y^q = 1`.** Records the
  minus-class-number/Stickelberger index identity. Sourced from the abstract;
  full proof text not obtained. The exact index relation used by the descent
  step must be confirmed against the primary text before a claim block is cut
  from it.
