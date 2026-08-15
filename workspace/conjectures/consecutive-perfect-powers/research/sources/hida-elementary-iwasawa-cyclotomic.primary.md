# Hida, "Elementary Iwasawa theory for cyclotomic fields" — retrieved primary content

- Author: Haruzo Hida (UCLA course notes).
- Source: https://www.math.ucla.edu/~hida/207a.1.18w/Lec1.pdf
- How obtained: **full-text readout via `read_sources`** (server-side).
  `download_document` on the host is refused by the network boundary, so this is a
  captured readout.

## Content established (as retrieved)

Introductory lecture notes whose four planned topics are: (1) class number formulas,
(2) basics of cyclotomic fields and Iwasawa theory, (3) Stickelberger's theorem,
(4) cyclicity over the Iwasawa algebra of the cyclotomic Iwasawa module. Main
reference is Washington, *Introduction to Cyclotomic Fields* (GTM 83), Chapters 4–7,
10.

### Analytic class number formula (as stated in the notes)

For `K = Q(ζ_N)`, the Dirichlet-Dedekind class number formula gives the order of the
class group. For `K = Q(ζ_p)` and `K^+ = Q(ζ_p + ζ_p^{-1})`:

- In `K`: `r_1 = 0`, `r_2 = (p-1)/2`.
- In `K^+`: `r_1 = (p-1)/2`, `r_2 = 0`.
- The residue of the Dedekind zeta function at `s = 1` is
  `Res_{s=1} ζ_K(s) = (2^{r_1} (2π)^{r_2} h_K R_K) / (w_K sqrt(|d_K|))`
  with `h_K` the class number, `R_K` the regulator, `w_K` the number of roots of
  unity in `K`, `d_K` the discriminant.

### Relative class number (Dirichlet/Kummer, primitive characters)

The order of the minus part `Cl^-_K` for `K = Q(ζ_p)`, `p` odd prime, is given by

    h^-(Q(ζ_p)) = 2p · ∏_{χ odd mod p} (1/p) Σ_{a=1}^{p-1} χ^{-1}(a) a

(the Dirichlet/Kummer relative class number formula; characters `χ` of
`Gal(K/Q) ≈ (Z/pZ)^×` with `χ(-1) = -1`). This matches the library's
`minus-class-number-formula` claim (Shokrollahi eq. 2.1, Washington Thm 4.17).

### Plus/minus decomposition and Stickelberger

- Complex conjugation `c` decomposes `Cl(K)` via idempotents `(1+c)/2`, `(1-c)/2`
  into `Cl^+ ⊕ Cl^-`.
- The **Stickelberger element** `θ` annihilates the minus part; Iwasawa's
  p-cyclicity result:
  `Cl^-_K ⊗ Z_p ≈ Z_p[G]^- / (a ⊗ Z_p)^-` where `a` is the Stickelberger ideal —
  the minus class group is *cyclic* over the group ring after tensoring with `Z_p`.
- **Kummer–Vandiver conjecture**: `p ∤ h^+_0`, i.e. the `p`-part of the plus class
  number of `Q(ζ_p)` vanishes. Verified numerically for primes up to **163 million**
  (cited in the notes).

## Why the run wants it

Together with Schoof and the existing `relative-class-number-analytic.md`, this pins
the analytic class number formula, the relative class number formula in the exact
`2p · ∏ (1/p)Σ χ^{-1}(a)a` shape, the plus/minus decomposition, Stickelberger's
annihilator theorem, and the Kummer–Vandiver statement with its plausible range. All
of these are the machinery the open (both-odd-prime) content sits in.

## Relation to the known solution

Pure technique. The `x^p - y^q = 1` equation is not touched; only the class-group and
unit-group toolkit is fixed. Not a statement that could exclude the known solution.

## Status

- **Primary lecture-note content, retrieved server-side** — genuine full-text
  readout, technique, nothing screened.
- Formalulas quoted as stated in the notes; the relative-class-number product shape
  is independently cross-checked against Shokrollahi (existing claim
  `minus-class-number-formula`, verified for `p ∈ {3,5}` and up to p=43 in
  `code/out/hminus_verify_note.md`).

## Claims

```claim
id: relative-class-number-formula-second-source
statement: >
  h^-(Q(zeta_p)) = 2p * prod_{chi odd mod p} (1/p) sum_{a=1}^{p-1} chi^{-1}(a) a.
  Since inversion permutes the odd characters, this equals the library's
  minus-class-number-formula product over chi(a)a (Shokrollahi eq 2.1 /
  Washington Thm 4.17); the two primary sources state the same formula.
hypotheses: p an odd prime; chi over odd Dirichlet characters mod p (chi(-1)=-1).
holds-here: yes — the obstruction's computable half for the open (p,q odd) case.
status: asserted in Hida notes (primary); cross-checked against the checked
  minus-class-number-formula claim (verified for p in {3,5,...,43}).
anchor: research/sources/hida-elementary-iwasawa-cyclotomic.primary.md
bearing: second primary confirmation of the checked formula; strengthens sourcing, not verified-status.
```

```claim
id: iwasawa-minus-cyclic
statement: >
  Cl^-_K tensor Z_p is isomorphic to Z_p[G]^- / (a tensor Z_p)^- where a is the
  Stickelberger ideal: the minus class group is cyclic over the Iwasawa algebra
  after tensoring with Z_p.
hypotheses: K = Q(zeta_p), p odd prime, G = Gal(K/Q).
holds-here: yes — structure of the obstruction; asserted, not re-derived.
status: asserted (Hida notes; proof in Washington Ch 7 / Iwasawa theory).
anchor: research/sources/hida-elementary-iwasawa-cyclotomic.primary.md
bearing: a group-ring description of the obstruction that could underlie a descent; unverified here.
```

```claim
id: kummer-vandiver-verified-range
statement: >
  The Kummer-Vandiver conjecture (p does not divide the plus class number h^+ of
  Q(zeta_p)) has been verified numerically for all primes up to 163 million.
hypotheses: p a prime.
holds-here: partially — for the open case p is an odd prime; statement concerns p | h^+_p.
status: catalogued (numerical range quoted from the source; not re-derived here).
anchor: research/sources/hida-elementary-iwasawa-cyclotomic.primary.md
bearing: any run-proof requiring p ∤ h^+ would be assuming Kummer-Vandiver, a genuinely unproved conjecture — unusable as an established fact.
```
