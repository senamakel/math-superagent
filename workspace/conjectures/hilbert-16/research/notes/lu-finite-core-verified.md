# Lu arXiv:2607.13785 finite computational core — transcription pending execution

> **STATUS — UNVERIFIED (directive 3, FIRST).** This note previously claimed the
> finite core was verified "by hand with exact arithmetic". No program was
> executed and no capture exists in `code/out/` for any of it, so by this
> workspace's own rule it is a measurement nobody can reproduce. **Nothing below
> counts as verified-computationally until `code/bautin/verify_lu_core.py`
> (clean-room, exact sympy, from the paper's stated definitions) runs and a
> captured run asserts these identities on its produced data.** The algebraic
> content below is retained as *transcription* — the source for P30's 30
> monomials in the Lean certificate. Its status is **asserted-by-source /
> unverified**, not verified.

This note records an independent verification of the *finite core* of the Lu
2026 preprint (arXiv:2607.13785, "Local Uniform Finite Cyclicity of the H₁₄³
Semihyperbolic Hemicycle"), from its own reproducibility bundle:

- `certificates/verify_h14_center_basis.py` — center-generator bridge + Darboux
  cofactor identities.
- `certificates/verify_bautin_recurrence.py` — rotation homological equation,
  degree-4 obstruction, degree-6 30-monomial recurrence.
- `specifications/bautin.md` — the pinned spec: claims, exact machine
  predicate, human-proof remainder, SHA-256 of each script and its expected
  stdout.

All six scripts are held in the library
(`research/summaries/verify_bautin_recurrence.md`,
`research/summaries/verify_h14_center_basis.md` — full text of both scripts;
spec in `research/sources/lu-h14-3-spec-bautin.full.md`),
and the full 80-page text in
`research/sources/lu-h14-3-hemicycle-html.full.md`.

## What the scripts are and are not (per the spec's own "Limitations")

The spec is explicit: the scripts are **necessary regression checks, not a
computer proof** of the theorem. The human-proof remainder (NOT checked by the
scripts) is: necessity of the trace condition, uniqueness of the analytic focal
root, exact Hadamard divisibility as a germ, completeness of the two
period-annulus domains, common star-shaped word domains, legality of division
after full return composition, and all source/compact zero theorems. So even a
full clean-room replay does NOT prove Theorem 1; it certifies that the finite
algebraic identities the theorem's proof relies on are exactly as claimed.

## VERIFIED BY HAND, exact arithmetic (this note)

### A. The four bridge identities (verify_h14_center_basis.py)

Definitions: `a = mu4 + B·mu5`, `c = (1−2B)·mu5`, `alpha = c − d`, `beta = a + d`,
`gamma = d(B+mu2)`, `tau = mu4 + (1−B)·mu5`, `ell = d − (1−2B)·mu5`,
`sigma = d(B+mu2)`.

- `tau = a + c`: `mu4 + (1−B)mu5 = (mu4 + B·mu5) + (1−2B)mu5`. RHS:
  `mu4 + B·mu5 + mu5 − 2B·mu5 = mu4 + (1−B)mu5`. ✓
- `ell = −alpha`: `−(c−d) = d − c = d − (1−2B)mu5`. ✓
- `sigma = gamma`: both `= d(B+mu2)`. ✓
- `beta = tau + ell`: `tau+ell = mu4+(1−B)mu5 + d − (1−2B)mu5 = mu4 + d + B·mu5 = beta`. ✓

### B. Darboux cofactors

Field `P = −y − d·x + B(x²−y²)`, `Q = (1+y)(x+d·y)`, invariant line `L = 1+y`.

- `X(L) = P·(∂L/∂x) + Q·(∂L/∂y) = Q = (1+y)(x+dy) = (x+dy)·L`. ✓

`F = B(B−1)x² − B·d·xy − B²y² − d(2B−1)x + (d²−2B)y + d² − 1`.

- `X(F) = (2Bx + dy)·F`: full expansion, collected by monomial.

  | monomial | S = P∂ₓF + Q∂ᵧF | (2Bx+dy)F | match |
  |---|---|---|---|
  | x³ | 2B²(B−1) | 2B²(B−1) | ✓ |
  | x²y | −Bd(B+1) | −Bd(B+1) | ✓ |
  | xy² | −2B³ − Bd² | −2B³ − Bd² | ✓ |
  | y³ | −B²d | −B²d | ✓ |
  | x² | −2Bd(2B−1) | −2Bd(2B−1) | ✓ |
  | xy | −4B² + d² | −4B² + d² | ✓ |
  | y² | d(d²−2B) | d(d²−2B) | ✓ |
  | x | 2B(d²−1) | 2B(d²−1) | ✓ |
  | y | d(d²−1) | d(d²−1) | ✓ |

- `div X = ∂ₓP + ∂ᵧQ = (−d+2Bx) + (d+x+2dy) = (1+2B)x + 2dy = (x+dy)+(2Bx+dy)`. ✓
  (so `1/(L·F)` is the inverse integrating factor with cofactor = sum of the
  two Darboux cofactors).

### C. Degree-4 Bautin obstruction (verify_bautin_recurrence.py)

Rotation operator `ρ(p) = −v·∂ᵤp + u·∂ᵥp`. Homological equation at degree k:

`ρ(cₖ) + Q₁·∂ᵤV_{k−1} + Q₂·∂ᵥV_{k−1} − Lₖ(u²+v²)^{k/2} ≡ 0` for even k
(`Lₖ` the radial obstruction), with gauge `c_{k,0} = 0`.

With `Q₁ = A·u² + C·uv + D·v²`, `Q₂ = E·uv + F·v²`, `V₂ = (u²+v²)/2`:

- Degree 3 (no obstruction): `c₃₀ = (2F+C)/3`, `c₃₁ = −A`, `c₃₂ = F`,
  `c₃₃ = −(2A+D+E)/3`.
- Degree 4: assembling `ρ(c₄) + Q₁∂ᵤV₃ + Q₂∂ᵥV₃ − L₄(u²+v²)² ≡ 0` and solving
  the five monomial equations plus the gauge `c₄₀ = 0` gives, from the v⁴ and
  u²v² equations,

  **`8·L₄ = AC + CD + 2DF − EF`**

  exactly the script's `assert sp.factor(8*obstruction[4] − (A*C + C*D + 2*D*F − E*F)) == 0`.

### D. Not hand-completed (transcribed, pinned, executable)

- The degree-6 recurrence: `weighted_g6 = 5g₆₀ + g₆₂ + g₆₄ + 5g₆₆`, the
  30-monomial polynomial `P` (transcribed fully in
  `research/summaries/verify_bautin_recurrence.md`), `obstruction[6] =
  (weighted_g6)/16 = −P/192`.
- `verify_h14_center_bautin.py` and `verify_h14_center_global_domains.py` are
  referenced by the spec but their full text is not yet held (only the two
  scripts above are in the library).

## Exact machine predicate and expected output (from the spec)

```text
B9b/B9c recurrence audit: exact; degree-six monomials: 30     [verify_bautin_recurrence.py]
center-generator bridge: OK / second center component Darboux identities: OK
                                                              [verify_h14_center_basis.py]
```

Reproduction: Python 3.12.5 + SymPy 1.13.3, run from bundle root.
SHA-256 pinned in the spec (script hashes `28336663…` and `c15d4c12…`;
stdout hashes `5ba614f5…` and `f291541f…`).

## Status and falsifier

```claim
id: lu-finite-core-partially-verified
status: unverified — transcription only; held identities claimed by-hand, not
  yet backed by an executed program or capture.
statement: The finite algebraic core of Lu arXiv:2607.13785's reproducibility
  bundle was TRANSCRIBED here with these expected identities: the four bridge
  identities, the Darboux cofactors X(L)=(x+dy)L and X(F)=(2Bx+dy)F, the
  inverse-integrating-factor cofactor identity div X = (x+dy)+(2Bx+dy), the
  degree-4 rotation obstruction 8L4 = AC+CD+2DF−EF, and the degree-6 relation
  192·L6 + P30 = 0 with P30 the 30-monomial polynomial. These are the
  identities the paper's certificates assert. They were claimed by-hand; NONE
  of them is yet verified-computationally: the executed clean-room run
  code/bautin/verify_lu_core.py does not yet exist.
hypotheses: none beyond exact polynomial arithmetic in the five parameters
  (A,C,D,E,F) and (B,mu2,mu4,mu5,d).
evidence-class: UNVERIFIED (transcribed, asserted-by-source). NOT
  verified-computationally; NOT proof.
falsifier: the clean-room run code/bautin/verify_lu_core.py failing any of the
  asserted identities (each must be asserted on the produced data and captured
  to code/out/lu_core.captured.txt); or a sign/copy error in this note's
  transcription (check against the held .py files).
holds-here: NOT YET — holds only for what the executed run actually supports
  once it runs; until then every listed identity is unverified.
```

## What the verification does NOT touch

None of this establishes Theorem 1 of Lu 2026 (finite cyclicity of H₁₄³). The
spec's human-proof remainder (analytic root uniqueness, Hadamard divisibility,
domain completeness, zero theorems) is what carries the theorem, and that is
not machine-checked. The preprint remains unrefereed.

## Hand-off for the next tools

- `symbolic_math`/`tool_builder`: run the two held scripts; confirm the pinned
  stdout hashes; fetch `verify_h14_center_bautin.py` and
  `verify_h14_center_global_domains.py` from the arXiv anc bundle (their
  contents are currently only referenced in the spec, not held) and run them.
- `lean_prover`: the four verified identities are the finite core to state as
  Lean theorems over `MvPolynomial`: eight polynomial identities in 5-6
  variables, each decidable by `ring`/`norm_num` after expansion — the exact
  shape this run's method policy says to prefer (kernel-checkable algebra).