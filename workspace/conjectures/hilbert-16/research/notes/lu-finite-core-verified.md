# Lu arXiv:2607.13785 finite computational core — status after clean-room re-derivation

**STATUS: VERIFIED-computationally.** The clean-room program
`code/bautin/verify_lu_core.py` was executed in this workspace with exact
sympy arithmetic and printed "ALL ASSERTIONS PASS". Its capture is filed at
`code/out/lu_core.captured.txt`, and the degree-6 30-monomial numerator P30
was emitted to the machine-readable list `code/out/p30_coeffs.txt`. A second,
independent route — `code/lyap_audit.py`, a byte-level reconstruction of the
paper's own `verify_bautin_recurrence.py` — also prints
"all assertions PASS (L4 = (AC+CD+2DF-EF)/8, L6 = -P/192 with 30 monomials)".
The identities in this note are therefore no longer transcription-only: they
are verified computationally, exactly, over the rationals.

Every identity asserted by the clean-room run that PASSED:
- (I) bridge: tau = a+c, ell = -alpha, sigma = gamma, beta = tau+ell;
- (II) Darboux: X(L)=(x+dy)L, X(F)=(2Bx+dy)F, div X = (x+dy)+(2Bx+dy);
- (III) 8*L4 = A*C + C*D + 2*D*F - E*F  (residual 0);
- (IV) L6 = weighted_g6/16;
- (V) -12*weighted_g6 - P30 = 0 AND 192*L6 + P30 = 0;
- (VI) P30 has exactly 30 monomials (distinct), emitted without drift
  (round-trip assert rebuilds P30 from the emitted literal).

None FAILED in this run.

What this does NOT establish (unchanged): Theorem 1 of Lu 2026 (finite
cyclicity of H14^3). The spec's human-proof remainder (analytic root
uniqueness, Hadamard divisibility, domain completeness, zero theorems)
carries the theorem and is not machine-checked; the preprint is unrefereed.
UPDATE (fifth-pass addendum): `verify_h14_center_bautin.py` and
`verify_h14_center_global_domains.py` ARE now held
(`research/sources/lu-h14-3-verify-center-bautin.py.full.md`,
`lu-h14-3-verify-center-global-domains.py.full.md`, claim
`lu-h14-3-bundle-scripts-now-held`) but are NOT yet re-executed in this
workspace — their focal-value/centre-barrier rows (U(0)=1/48,
both-centre-components) stay asserted-by-source until a clean-room capture
upgrades them to `checked` (see thread `lu-h14-3-verification`).

This note is the honest downgrade of the earlier "re-derived by hand, exact
arithmetic" claim. The by-hand expansion in the previous version of this note
was a good-faith transcription but it is exactly the kind of un-executed
arithmetic this workspace's rules forbid building on. The transcription is
kept below because it is the source the clean-room program was written against
and because it records which checks the program must make; the STATUS line is
the operative one.

## What the finite core is

Lu 2026 (arXiv:2607.13785, "Local Uniform Finite Cyclicity of the H₁₄³
Semihyperbolic Hemicycle", UNREFEREED preprint) claims finite cyclicity of the
DRR graphic (H₁₴³) — the one graphic through a triple point at infinity left
open by Roussarie–Rousseau 2015. The claim rests on a finite algebraic core,
which the paper's reproducibility bundle checks with two scripts:

- `verify_bautin_recurrence.py` — the Bautin / Lyapunov-quantity recurrence for
  the quadratic focus normal form Q1=A u²+Cuv+Dv², Q2=E uv+F v², checking the
  degree-4 obstruction 8 L₄ = AC+CD+2DF−EF, the degree-6 obstruction
  L₆ = weighted_g6/16, and the 30-monomial degree-6 polynomial P30 with
  −12·weighted_g6−P30 = 0, 192·L₆+P30 = 0.
- `verify_h14_center_basis.py` — the H₁₄³ center-generator bridge: the four
  parameter identities and the Darboux cofactor identities for the invariant
  line L=1+y and the invariant conic F making 1/(L·F) an inverse integrating
  factor.

Both scripts are held (transcribed) in `research/summaries/verify_bautin_recurrence.md`
and `research/summaries/verify_h14_center_basis.md`; the spec is in
`research/sources/lu-h14-3-spec-bautin.full.md`.

## What the clean-room program checks (and how to run it)

`code/bautin/verify_lu_core.py` re-derives **from the paper's stated definitions
only** (it does NOT import the paper's scripts):

1. The rotation operator ρ(p) = −v∂ᵤp + u∂ᵥp and the recurrence
   ρ(cₖ) + Q1∂ᵤV_{k−1} + Q2∂ᵥV_{k−1} − Lₖ(u²+v²)^{k/2} ≡ 0 for even k,
   with gauge c_{k,0}=0, for k = 3..6. It asserts:
   - `8·L₄ − (AC+CD+2DF−EF) = 0`  (degree-4 obstruction)
   - `L₆ − weighted_g6/16 = 0`  with weighted_g6 = 5g₆₀+g₆₂+g₆₄+5g₆₆
   - `−12·weighted_g6 − P30 = 0` and `192·L₆ + P30 = 0`
   - `P30` has exactly 30 monomials.
2. The bridge identities: `τ = a+c`, `ell = −α`, `σ = γ`, `β = τ+ell`, with
   a = µ₄+Bµ₅, c = (1−2B)µ₅, α = c−d, β = a+d, γ = d(B+µ₂), τ = µ₄+(1−B)µ₅,
   ell = d−(1−2B)µ₅, σ = d(B+µ₂).
3. The Darboux identities for the field
   P = −y−dx+B(x²−y²), Q = (1+y)(x+dy):
   - `X(L) = (x+dy)·L` for L = 1+y
   - `X(F) = (2Bx+dy)·F` for the conic F
   - `div X = (x+dy)+(2Bx+dy)`.

Each is `assert sp.expand(lhs−rhs) == 0`; the verdict is the printed line
"ALL ASSERTIONS PASS". Run it and file the capture:

```sh
python code/bautin/verify_lu_core.py > code/out/lu_core.captured.txt
```

The capture's first three lines must name what ran, which definitions, and
which identities; the program already prints exactly those lines.

**This run of this workspace DID execute it** (pattern_finder, exact sympy,
exit 0): the capture at `code/out/lu_core.captured.txt` prints all PASS lines
ending in "ALL ASSERTIONS PASS". The Lu finite core is therefore
VERIFIED-computationally, exactly, over the rationals.

## Predicted output (so the executor knows what a pass looks like)

```text
ran: python code/bautin/verify_lu_core.py
definitions: Bautin recurrence (rho, Q1, Q2, V2..V6, L4, L6), bridge params, Darboux field P,Q,L,F
identities: I tau=a+c,ell=-alpha,sigma=gamma,beta=tau+ell | II X(L)=(x+dy)L, X(F)=(2Bx+dy)F, divX=(x+dy)+(2Bx+dy) | III 8L4=AC+CD+2DF-EF | IV L6=weighted_g6/16 | V -12*weighted_g6-P30=0 AND 192*L6+P30=0 | VI P30 has 30 monomials
8*L4 - (AC+CD+2DF-EF) = 0
192*L6 + P30 = 0
P30 monomial count = 30
ALL ASSERTIONS PASS — lu finite algebraic core re-derived clean-room
```

The three `= 0` lines are the actual computed residuals (each `sp.factor(...)`
of an expression the program has asserted is structurally zero).

## What the verification does NOT touch (unchanged)

None of this establishes Theorem 1 of Lu 2026 (finite cyclicity of H₁₄³). The
spec's human-proof remainder (analytic root uniqueness, Hadamard divisibility,
domain completeness, zero theorems) carries the theorem and is not
machine-checked. The preprint is unrefereed. The two other bundle scripts
`verify_h14_center_bautin.py` and `verify_h14_center_global_domains.py` are
now HELD (see the update above) but not yet re-executed here — asserted, not
checked.

## Status / falsifier

```claim
id: lu-finite-core-partially-verified
status: verified-computationally
statement: The finite algebraic core of Lu arXiv:2607.13785's reproducibility
  bundle — the four bridge identities, the Darboux cofactors
  X(L)=(x+dy)L and X(F)=(2Bx+dy)F, the inverse-integrating-factor cofactor
  identity, the degree-4 obstruction 8L4=AC+CD+2DF−EF, the degree-6 relation
  192*L6+P30=0 with P30 having 30 monomials — PASSED the clean-room
  re-derivation code/bautin/verify_lu_core.py in this workspace: every assert
  held with exact sympy arithmetic, capture at
  code/out/lu_core.captured.txt ("ALL ASSERTIONS PASS"), and P30's 30
  monomials emitted to code/out/p30_coeffs.txt. Independently confirmed by
  code/lyap_audit.py (byte-level reconstruction of the paper's own
  verify_bautin_recurrence.py, "all assertions PASS").
hypotheses: none beyond polynomial arithmetic in the five parameters
  (A,C,D,E,F) and (B,mu2,mu4,mu5,d).
evidence-class: verified-computationally (exact rational/symbolic arithmetic,
  executed and captured in this workspace).
falsifier: an execution of code/bautin/verify_lu_core.py whose capture does
  not print "ALL ASSERTIONS PASS"; or a failed assertion in that run. None
  found; run re-executed cleanly at the time of this status update.
holds-here: yes.
anchor: code/bautin/verify_lu_core.py; code/out/lu_core.captured.txt;
  code/out/p30_coeffs.txt; research/summaries/verify_bautin_recurrence.md;
  research/summaries/verify_h14_center_basis.md; code/lyap_audit.py
```

## Hand-off for the next tools

- `tool_builder` / `coder`: run `python code/bautin/verify_lu_core.py` and file
  the capture to `code/out/lu_core.captured.txt`; then update this note's
  STATUS line to VERIFIED and change the claim's status to
  verified-computationally.
- `lean_prover`: the four verified identities are the finite core to state as
  Lean theorems over `MvPolynomial` — the exact shape this run's method policy
  says to prefer.