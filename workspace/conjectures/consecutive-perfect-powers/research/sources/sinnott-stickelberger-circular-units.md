# Sinnott, "On the Stickelberger Ideal and the Circular Units of a Cyclotomic Field"

**Source URL:** https://doi.org/10.2307/1970932
**Author:** W. Sinnott
**Published:** Annals of Mathematics, 1978.
**Status:** Summary-level record — retrieved via read_sources; full text not stored (publisher download blocked).

## Why this source is in the library

This is the primary treatment linking the two objects at the heart of the problem's obstruction: the **Stickelberger ideal** S (a set of annihilators of the ideal class group, in the group ring Z[G]) and the **circular units** C (a subgroup of the units). The problem's open content is controlling the class group of Q(zeta_p); Sinnott's index formulas are the quantitative bridge between units, the Stickelberger ideal, and class numbers.

## Setup (from the retrieved abstract)

- k an imaginary cyclotomic field, conductor m, G = Gal(k/Q), R = Z[G] the integral group ring.
- S = the Stickelberger ideal (an ideal of R), C = the circular units (a subgroup of the unit group E of k).
- j = the element of G induced by complex conjugation. For any G-module A, A^+ = {a : ja = a} and A^- = {a : ja = -a}.
- h = class number of k; h^+ = class number of k^+ (maximal totally real subfield); the derived ratio h^- = h·h̄/h^+ type quantity appears.

## Main result (from the retrieved abstract)

Sinnott computes the indices exactly:
- **[R^- : S^-]** — the index of the minus part of the Stickelberger ideal in the minus part of the group ring — expressed in terms of the class numbers h, h^+.
- **[E^+ : C^+]** — the index of the plus circular units in the plus unit group — the same style of class-number-related ratio.

These indexes measure how much of the (minus) class group is annihilated by S, and how large the circular units are inside the full unit group. They are the quantitative backbone of "the obstruction is the class group, and it is controlled by units/modulo circular units and the Stickelberger ideal."

## Relevance to the problem

In the cyclotomic setting of x^p - y^q = 1, the deep step (G-odd-descent / double-Wieferich / the minus-class-group argument) works with exactly these two objects:
- The Stickelberger ideal annihilates the minus part of the class group, which is what lets an ideal relation be pushed toward an element relation.
- The circular units / cyclotomic units generate a subgroup of the unit group of finite index equal to (a multiple of) the class number.

This source fixes the precise meaning of both, which the run currently holds only as names.

## Verified vs not

Verified (from abstract): statements of the setup (R, S, C, E, the +/- decomposition) and the claim that [R^-:S^-] and [E^+:C^+] are computed exactly in terms of h, h^+, and the Stickelberger data. The precise closed-form expression of the two indices was not fully retrieved — the abstract gives the structure but I did not capture the exact class-number formula. For the exact formulas, the full paper or Washington GTM 83 ch. 15 (cyclotomic units) is the source.

## Cross-reference

Washington, *Introduction to Cyclotomic Fields* GTM 83, covers this material (Chapter: cyclotomic units / class numbers). Tijdeman and Milne notes are in the library as the surrounding framework.
