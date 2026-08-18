# Mourtada–Moussu 1997: Dulac maps are 1-Pfaffian iff analytically normalisable

```claim
id: mourtada-moussu-1997-dulac-pfaffian-iff-normalisable
statement: (MM 1997, Bull. SMF 125:1-13, full text held.) A germ of reduced analytic 1-form ω = 0 in (R²,0) with a col-sector (saddle sector) S, with characteristic number λ > 0 (Siegel domain, 1-jet j¹ω = λ y dx + x dy), has an analytic integrating factor if and only if its Dulac map d_{ω,S} is 1-pfaffien (i.e. its graph is the germ at 0 of an integral curve of an analytic equation η = 0 with algebraically isolated singularity at 0 ∈ R²). Equivalently (Proposition 0, citing Ecalle/Martinet–Ramis/Mattei–Moussu): (i) ω = 0 has a convergent normal form; (ii) the iterator H (resp. K) is convergent; (iii) ω = 0 has an analytic integrating factor. The normal form is one of three types: Type I hyperbolic non-resonant (λ ∈ R⁺∖Q), Type II hyperbolic resonant (λ = p/q), Type III semi-hyperbolic (λ = 0, one analytic separatrix + one formal). Propositions 1+2: for Types I,II the asymptotic expansion d converges ⇔ ω analytically normalisable ⇔ d is 1-pfaffienne.
hypotheses: reduced analytic 1-form in the Siegel domain with a col-sector; the Dulac map is evaluated on transverse analytic sections close to 0.
holds-here: yes, for the individual passage germs; the open DRR graphics are reduced (their blow-up vertices have 1-jets of this form after desingularisation, Seidenberg).
status: asserted-by-source (full text read and held; not independently re-derived)
falsifier: A reduced analytic non-normalisable form whose Dulac map is nevertheless 1-pfaffienne would refute the theorem (no such example is known; the paper's proof is a bidirectional argument over the three normal-form types).
sources: https://doi.org/10.24033/bsmf.2297
anchors: research/sources/mourtada-moussu-dulac-pfaffiennes.pdf.full.md lines 30-330 (Résumé, Introduction, §1.1-1.4, Propositions 0-2)
```

## What this means for the adopted synthesis

The MM theorem is a **two-edged** result for the adopted approach
`compensator-pfaffian-mourtada-moussu-synthesis`:

1. **Positive edge (locates analyticity):** the equivalence
   `1-Pfaffian ⇔ analytically normalisable` is the exact step where a
   smooth-but-not-analytic field would fail. A C^∞ field whose Dulac map is not
   analytically normalisable has a non-1-Pfaffian Dulac map, so a purely
   smooth zero-bound could not proceed through the Khovanskii/Pfaffian route.
   This is the Test-1 location, stated as a cited theorem rather than a guess.

2. **Negative edge (bounds the method):** the paper's own conclusion is
   "le champ d'application de cette théorie aux problèmes de cycles limites est
   assez limité. Il doit être réservé à l'étude de « cas génériques »."
   The full Dulac maps of the open non-hyperbolic graphics are NOT 1-Pfaffian
   (they are not analytically normalisable — that is precisely why they remain
   open after the integrable/elementary closures). Therefore the synthesis must
   use the RSZ/RR Theorem 2.3 **normal-form decomposition** D = leading + φ_A,
   where only the leading part (powers + compensator) is Khovanskii-Pfaffian,
   and φ_A is handled by DIR derivation-division. The strong claim "the whole
   Dulac map is Pfaffian" is refuted by MM; the refined claim "the leading
   normal-form part is Pfaffian of fixed format, remainder by DIR" is the live
   form, and its own falsifier (per-passage exponent growth in the four-map
   composition) is stated in the approach file.

## Distinctness of two Pfaffian notions (do not conflate)

- **Mourtada–Moussu 1-pfaffien** (strong): the graph of the *whole* Dulac map
  lies on one analytic curve with isolated singularity. This is equivalent to
  analytic normalisability and fails for the open graphics.
- **Khovanskii Pfaffian chain** (weak): a *triangular* system dfᵢ/dx = Pᵢ(x,f₀,…,fᵢ)
  on an open box. This is what the RSZ leading term satisfies (powers +
  compensator), with format fixed over the parameter stratum.
