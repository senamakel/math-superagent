# The Non-Cancelling Intersections Conjecture — Amarilli, Monet, Suciu (2024)

Source: https://arxiv.org/pdf/2401.16210 (arXiv:2401.16210); full text at
`research/sources/non-cancelling-intersections-amarilli.full.md` →
[[non-cancelling-intersections-amarilli.full]]

## What it establishes

Studies the NCI conjecture on **principal down-sets of Boolean lattices**: for the
Boolean lattice `B_S` on a finite set `S`, a principal down-set `↓X` is the down-set
spanned by `X`. The rows `M_d` of this problem's fold matrix are exactly such principal
down-sets `↓d` (shifted to absolute positions).

- **Fact 4.8.** For every tight intersection lattice `L`, `∎(NTI(L)) = 2^{1-hat}`:
  using the non-trivial intersections one can realise all subsets of elements.
- **Prop 4.7.** In a tree witnessing `1-hat ∈ ∎(NTI(L))` for a full intersection
  lattice, `mult_T(U) = −µ_L(U, 1-hat)` — the multiplicity of a down-set in an
  expression equals minus its Moebius value (on the down-set semilattice).
- **Conj 5.4 (NCPD).** For every finite `S`, every downset `I` of `B_S` is in
  `∎(NCPD_{B_S}(I))`. Equivalent to NCI (Conj 3.4, NCU Conj 3.6). Open.
- **Fact 5.6.** Generalized Moebius functions `µ_{B_S,C}` are linear under disjoint
  union (`+`) and subset complement (`−`).
- **Thm 6.2 / Prop 6.7.** The no-cancellation case holds; the general case is open,
  with a counterexample by Jachiet to a stronger version.

## Bearing on this problem

Rows of `Φ_n` form the meet-semilattice of principal down-sets of the Boolean lattice
(`M_d ∩ M_{d'} = M_{d∧d'}`, imported result 3). The symmetric differences are the XOR
of two principal down-sets. Moebius inversion (Prop 4.7 / 5.10) and the cancellation
structure are the machinery that describes which of these symmetric differences are
"seen" (witnessed with nonzero multiplicity) by the Walsh characters `(−1)^{XOR}` in
the `S²` expansion. This is the vocabulary for GOAL priority 1: which sets occur, with
what multiplicity, in `{M_d △ M_{d'}}`. The conjecture itself is open; the lattice
tools are proved.

## Claim blocks

```claim
id: amarilli-moebius-multiplicity
statement: In a disjoint-union/subset-complement expression built from the non-trivial
  intersections of a full intersection lattice, the multiplicity of a set U equals its
  negative Moebius value −µ_L(U, 1-hat) on that lattice.
hypotheses: L a full intersection lattice, 1-hat ∈ ∎(NTI(L)), T a witnessing tree
holds-here: unchecked (L must be shown full/tight for the down-set semilattice of the M_d)
status: proved
bearing: candidate mechanism for which symmetric-difference sets survive with nonzero
  multiplicity in the S² Walsh sum; zero-multiplicity sets cancel out of S².
anchor: research/sources/non-cancelling-intersections-amarilli.full.md
```

```claim
id: amarilli-ncpd-setup
statement: Principal down-sets ↓X of the Boolean lattice B_S, with ↓X = 2^X, and their
  meet-semilattice and Moebius structure, are the setting of the NCPD conjecture, which
  is equivalent to the NCI conjecture.
hypotheses: S finite; X ⊆ S
holds-here: yes
status: asserted (the equivalence is proved in the paper; the conjecture is open)
bearing: the fold rows M_d form exactly such principal down-sets; gives the lattice
  vocabulary for priority 1 (which M_d △ M_{d'} occur, with what sign multiplicity).
anchor: research/sources/non-cancelling-intersections-amarilli.full.md
```

## What it does not settle

Neither the NCI/NCPD conjecture nor the exact listing of `{M_d △ M_{d'}}` with
multiplicities. `holds-here: unchecked` on Prop 4.7 because the tightness/fullness of
the specific down-set semilattice used here is not yet verified.

## Reconciliation with the computed multiset (added by scholar)

The computed structure (claim `pf-s2multiset-rigid`, `code/out/`, verified to n=256)
gives the actual multiplicities: empty with multiplicity `n−2`, every other distinct set
with multiplicity exactly 2. Under the Amarilli/Moebius reading (multiplicity =
`−µ_L(U,1-hat)`), this says the Moebius values here take only the two values
`{−(n−2), −2}` on the relevant lattice elements — a highly rigid sign structure. The
multiplicity-2 rigidity means the *pair-injectivity* of `{d,d'} ↦ M_d△M_{d'}` (a
computed, checked property) is the operative mechanism, and it is consistent with, but
does not require, the full NCI machinery. The general NCI conjecture's open status is
therefore *not* a blocker for the collapse question: the specific multiplicities are
computed directly. `holds-here` on the general Moebius claim stays `unchecked` because
the tightness/fullness hypothesis has not been verified; the direct census does not
depend on it.
