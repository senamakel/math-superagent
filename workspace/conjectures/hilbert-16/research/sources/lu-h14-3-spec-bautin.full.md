<!-- source: https://arxiv.org/src/2607.13785v2/anc/h14_3_reproducibility/specifications/bautin.md | converted from plain text -->

# Center and Bautin Certificate

## Claim and manuscript locators

- Claims: `lem:h14-center-bautin-ideal` and `lem:center-word-domains`.
- Manuscript: Theorem `thm:part-ii-center-ideal` and Appendix
  `app:center-bautin`.
- Scripts: `certificates/verify_h14_center_basis.py`,
  `verify_bautin_recurrence.py`, `verify_h14_center_bautin.py`, and
  `verify_h14_center_global_domains.py`, all under
  `certificates/`.

## Finite mathematical alphabet or recurrence

The focal calculation uses homogeneous polynomials through degree six in the
five normalized coefficients `(A,C,D,E,F)`. At each degree the rotation
homological equation determines the correction coefficients; an even degree
leaves one radial obstruction. The finite recurrence gives
`8 L1 = AC + CD + 2 DF - EF` and a degree-six numerator with 30 monomials.

The parameter-side alphabet consists of `(tau, ell, a, t_c, B)`, with
`t_c = B + m`, the two center slices `a = 0` and `t_c = 0`, and the two global
center-domain certificates: the reversible first integral and the quadratic
inverse integrating factor.

## Physical exhaustiveness

The human proof derives the trace-zero reduction, shows that the first focal
obstruction has a unique local root, proves exact divisibility on both slices,
and proves that the two resulting branches are centers. It then identifies the
maximal physical section intervals using the reversible barrier and the
quadratic invariant conic. These domain facts are required before full-word
Hadamard division and are not outputs of symbolic simplification.

## Exact machine predicate

The four scripts check:

1. the bridge between `(alpha,beta,gamma)` and `(tau,ell,d(B+m))`;
2. the two Darboux cofactor identities on the quadratic center component;
3. the degree-four obstruction and degree-six angular-average recurrence;
4. equality of the expanded 30-monomial polynomial with the recurrence;
5. vanishing of the degree-six obstruction on both center components and the
   coefficient `U(0) = 1/48` after the first obstruction;
6. the reversible first-integral Lie derivative, extra critical point, and
   source-minus-saddle barrier identity;
7. the quadratic inverse integrating factor, extra critical point, gate
   determinant, and invariant-conic restriction.

## Human proof remainder

The scripts do not prove necessity of the trace condition, uniqueness of the
analytic focal root, exact Hadamard divisibility as a germ, completeness of
the two period-annulus domains, common star-shaped word domains, legality of
division after full return composition, or any source/compact zero theorem.

## Representative encoded example

`verify_bautin_recurrence.py` constructs the homogeneous correction of degree
four, fixes the gauge `c_(4,0)=0`, and checks that its radial obstruction obeys
`8 L1 = AC + CD + 2 DF - EF`. This is a direct encoding of the representative
calculation in Appendix `app:center-bautin`. The later 30-term equality checks
the same recurrence at degree six; it does not replace the slice-divisibility
argument.

## Reproduction commands

Run from the extracted bundle root:

```bash
python certificates/verify_h14_center_basis.py
python certificates/verify_bautin_recurrence.py
python certificates/verify_h14_center_bautin.py
python certificates/verify_h14_center_global_domains.py
```

Runtime for the clean-room replay: CPython 3.12.5 and SymPy 1.13.3.

## Expected outputs

The first script prints the two `OK` lines for the generator bridge and
Darboux identities. The second prints:

```text
B9b/B9c recurrence audit: exact; degree-six monomials: 30
```

The third prints the exact `L1` formula, `30` numerator terms, vanishing on
both components, `a*(B + m)/48 + O(eps^3)`, and `U(0) = 1/48`. The fourth
prints `OK` for the reversible Lie derivative and barrier, the quadratic
inverse integrating factor, and the displayed critical-point, determinant,
and invariant-conic formulas.

## SHA-256

| Script | Script SHA-256 | Canonical stdout SHA-256 |
|---|---|---|
| `certificates/verify_h14_center_basis.py` | `c15d4c1270b02b0fa6537d84efdbd9046c37841db9e0b7847cefd96c6f4eacbf` | `f291541f01d0c15cdfdb50ebad52017c6a8080234593f78759930d10aff7907e` |
| `verify_bautin_recurrence.py` | `2833666390b40d239dc2ef961b40a0e607751c9e433c7dd254924a73a3e661ae` | `5ba614f53d5c80aecd7a8c27d615194f62f13d7f2a05edafbc0d16cb972dfb8d` |
| `verify_h14_center_bautin.py` | `6c22eb5f2584cf49198a1ad5e9fe8c3a5a92ec23ce95a41c3723f8dd5d8c4cd0` | `10a3ff15b46d9236485fd207ad1bd440c8f6c80504a2f0ef340970219fb2ac1a` |
| `verify_h14_center_global_domains.py` | `37b5a823fa44ba4340088e4beaf2e3fb5b2a63806c00872f287c01deba88ab18` | `e7df44d9e2eee845c23923a4d217a15f454e14a43d5f82746d4eb3e29001cd21` |

## Limitations

Successful symbolic identities are necessary regression checks, not a
computer proof of center-domain topology or of the theorem. The scripts do
not search for additional center components outside the proved local graph,
do not validate a finite-smooth normalizer, and do not authorize division on
an arbitrary germ. The locked clean-room replay is provided in `reproduce/`.
