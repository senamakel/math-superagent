# Cassou-Noguès–Płoski 2012 — Invariants of plane curve singularities and Newton diagrams

Source: P. Cassou-Noguès, A. Płoski, "Invariants of plane curve singularities
and Newton diagrams", arXiv:1207.1600 (2012). Primary; full text held at
`research/sources/cassou-nogues-ploski-invariants-plane-curve-singularities-2012.full.md`.

## What it establishes (per the primary abstract and structure)

- For a reduced plane curve singularity over an algebraically closed field, the
  three local invariants — **Milnor number μ, delta invariant δ, number of
  branches r** — obey the **Milnor formula `2δ = μ + r − 1`**.
- δ, μ, r admit explicit computation from the **Newton diagram** / Newton
  transformation / Puiseux parametrization; δ is the count of double points
  acquired in a resolution (the "number of double points" the genus formula
  subtracts from the arithmetic genus).
- The paper develops an elementary intersection-theoretic framework for these
  invariants (planar versions of classical nondegenerate-singularity results,
  Jung's lemma on discriminants, invariance under coordinate changes).

## Bearing for this run

- This is the **tool reference for the pending `G-delta-invariant` task** in
  `research/BACKWARD.md`: proving that the total delta invariant of the
  singularities of the projective closure of `C(x,m)=C(y,n)` equals
  `δ(m,n) = ((m-1)(n-1) − 1 + gcd(m,n))/2` (equivalently g = p_a − δ with
  p_a = (m-1)(n-1)), which would promote the run's genus closed form from
  checked to proved. The singular points live at the common vanishing of the
  two falling factorials and at infinity; each is a multi-branch point whose δ
  can be summed via the Milnor formula once the branches (Puiseux series at
  each point) are known.
- Not a result about Singmaster per se — a supporting primary for the genus
  derivation thread.

```claim
id: cassou-nogues-ploski-delta-newton
statement: Cassou-Nogues-Ploski 2012 (arXiv:1207.1600, primary held): for a
  reduced plane curve singularity, delta invariant delta, Milnor number mu and
  branch number r satisfy 2*delta = mu + r - 1, and delta, mu, r are
  computable from the Newton diagram / Puiseux parametrization; delta is the
  number of double points acquired in a resolution.
hypotheses: plane curve, algebraically closed field, reduced (multi-branch
  allowed) singularity.
holds-here: yes - the singularities of the projective closure of C(x,m)=C(y,n)
  are multi-branch points (common falling-factorial zeros plus infinity) whose
  delta the genus closed-form proof must sum.
status: sourced (primary held; not re-derived here)
bearing: tool reference for the live G-delta-invariant task in BACKWARD.md
  (prove delta(m,n) = ((m-1)(n-1)-1+gcd(m,n))/2 for the binomial curves).
anchor: research/summaries/cassou-nogues-ploski-invariants-plane-curve-singularities-2012.md
```