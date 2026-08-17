# Yakubovich, *Towards the Casas-Alvero conjecture* (arXiv:1504.00274v2, 14 Aug 2015)

Source URL: https://repositorio-aberto.up.pt/bitstream/10216/90434/2/171243.pdf
(arXiv:1504.00274v2 [math.CA]; repository mirror of the University of Porto.)
Full text: `research/sources/towards-casas-alvero_porto.full.md`.

## Relationship to the held v1

The library already holds **v1** of the same paper at
`research/sources/yakubovich2025_validity-casas-alvero.full.md`
(`yakubovich2025_validity-casas-alvero.pdf`), which the run previously
summarised as "Yakubovich, *The validity of the Casas-Alvero conjecture*
(2015, arXiv:1504.00274)". The two are the **same work, versions 1 and 2** —
v1 dated 1 Apr 2015, v2 dated 14 Aug 2015, titled *Towards the Casas-Alvero
conjecture*. The v2 is the later, final version (the one the author's later
papers and the published J. Classical Analysis record cite). **Both version
full texts are now held.** Prefer the v2 text (this file) for statements;
the v1 text is retained for the version record.

## What this paper establishes

A real- and complex-analysis contribution to the CA problem, in the
Abel–Gontcharoff interpolation-polynomial tradition. Claims (all as stated in
the paper; this is a claimed-proof-family item, not a settled result):

- **Proposition 1.** A polynomial with only real roots, degree n≥2, is trivial
  iff its (n−2)-nd derivative has a double root.
- **Proposition 2.** A possible non-trivial f of degree n≥6 with only real
  roots, sharing a root with its (n−2)-nd and (n−1)-st derivatives, has at
  least **five distinct roots**.
- **Proposition 3.** Under the same conditions with n≥7 and distinct
  multiplicities of the (n−2)-nd derivative roots, at least **six distinct
  roots**.
- **Proposition 4.** CA holds iff it holds for common roots lying in the unit
  circle (homogeneity reduction, from shift/homogeneity (5)).
- **Proposition 5.** A possible non-trivial CA-polynomial with only real zeros
  has at least 5 distinct roots.
- **Proposition 6.** A non-trivial f of degree n≥2 with k distinct roots,
  sharing root λ₁ with its (n−1)-st derivative, must contain at least one root
  outside the disk D_μ = {z : |z−λ₁−1| ≤ μ}, μ∈(0,1).
- Determinantal representation of the Levinson/Gontcharoff polynomials
  (upper-Hessenberg form, Lemma 1); a sharper-than-Goncharov bound on
  |G_n(z,z₀,…,z_{n−1})|; Sz.-Nagy type identities; a generalisation of the
  Schoenberg-conjectured Rolle analogue.

## Bearing on the run

- Real-rooted restrictions: the ≥5-distinct-roots statement for real-rooted CA
  polynomials (Prop 5) aligns with the held Laterveer–Ounaïes ≥5 bound
  (which needs no real-root hypothesis) — corroborating, not superseding.
- The unit-circle reduction (Prop 4) is a distinct normalisation worth knowing
  against the run's centroid/traceless normalisations.
- The paper is in the **claimed-proof family** (the abstract reports
  "necessary and sufficient conditions for triviality"); the run's status note
  (`research/notes/casas-alvero-status.md` line ~292) already lists
  arXiv:1504.00274 (2015, preprint) as an unverified/claimed item. **Nothing
  here changes the standing status: CA open.**

## Caveats

- Prop 1's "iff" is a strong claim; it is asserted in this preprint and not
  independently checked here. It is corroborated in spirit by the real-root
  analysis in Chellali 2015 (held) and Polstra 2012 (held), but the exact
  statement should be treated as asserted-by-source unless verified.
- The v1 vs v2 naming discrepancy was real: the run's earlier summary used the
  v1 title. Both are now held and cross-linked.

Claim block (id: yakubovich-2015-towards-1504.00274v2):
See the reconciliation note `research/notes/yakubovich-1504-00274-v1-v2.md`
for the version record; this file's propositions are asserted-by-source
(preprint), corroborated at the ≥5-distinct-roots point by the held
Laterveer–Ounaïes primary.

```claim
id: yakubovich-2015-towards-1504-00274v2
statement: Yakubovich, "Towards the Casas-Alvero conjecture"
  (arXiv:1504.00274v2, 14 Aug 2015, via Univ. of Porto repository) — real-
  rooted/analysis constraints on CA polynomials: (Prop 1) a real-rooted degree-
  n≥2 polynomial is trivial iff its (n-2)-nd derivative has a double root;
  (Prop 2) a real-rooted degree-n≥6 polynomial sharing roots with its (n-2)-nd
  and (n-1)-st derivatives has at least 5 distinct roots; (Prop 3) same with
  n≥7 and distinct multiplicities gives at least 6; (Prop 4) CA holds iff it
  holds for common roots on the unit circle; (Prop 6) a non-trivial degree-n
  polynomial sharing root λ1 with its (n-1)-st derivative has a root outside
  the disk D_μ={|z-λ1-1|≤μ}, μ∈(0,1). Plus determinantal (upper-Hessenberg)
  representation of the Levinson/Gontcharoff polynomials and a
  sharper-than-Goncharov bound.
hypotheses: char 0 (complex coefficients); real-rooted restrictions where
  stated; Abel-Gontcharoff interpolation framework
holds-here: yes, where the ≥5-distinct-roots real-rooted statement is
  corroborated by the held Laterveer-Ounaïes 2012 primary (which needs no
  real-root hypothesis)
status: asserted-by-source (preprint in the claimed-proof family; the v2 is
  the definitive version of the already-held arXiv:1504.00274v1); nothing
  here changes CA's standing status of open
anchor: research/sources/towards-casas-alvero_porto.full.md
falsifies: an independent check showing one of Props 1-6 is false as stated,
  or a peer-reviewed record showing the paper's full-CA implications were
  rejected for cause
```