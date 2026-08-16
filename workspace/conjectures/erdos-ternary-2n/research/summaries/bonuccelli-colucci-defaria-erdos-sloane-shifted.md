# Bonuccelli, Colucci & de Faria, "On the Erdős-Sloane and Shifted Sloane Persistence Problems" — HELD IN FULL

Source: arXiv:2009.01114 (2020; J. Integer Seq. 23 (2020)). Full text:
`research/sources/bonuccelli-colucci-defaria-erdos-sloane-shifted.full.md`
(65 KB, PDF capture).

## What it studies

The Erdős–Sloane map `S*_b` (product of the *nonzero* digits of `n` in base b,
introduced by Erdős per Guy) and the t-shifted Sloane maps `S_{t,b}` (product of
digits shifted by t, from Wagstaff). It asks whether every n stabilizes under
iteration, whether persistence is bounded, and describes fixed points/cycles and
backward orbits.

## Key results

- **Theorem 5.** Assuming the de Faria–Tresser digit-equidistribution
  conjecture (Conjecture 1), the Erdős–Sloane maps `S*_3` and `S*_4` have
  integers of **arbitrarily large persistence**; assuming the uniform
  generalization (Conjecture 4), the same holds for `S*_b` for every `b ≥ 5`.
  So under the equidistribution conjecture, *unbounded* persistence — the
  opposite of the classical Sloane conjecture — holds for the Erdős–Sloane and
  shifted (t=1) variants.
- **Theorem 7.** `A_f = ℕ` for `t = 1, b ≥ 2` (every n stabilises under the
  shifted map), extending Wagstaff.
- **Theorem 8.** For `t=1, b=3` the cycles and backward orbits are described
  completely — the one fully-solved case.

## The direct bearing on the Erdős ternary conjecture

**Remark 3** states the key fact for this run, explicitly and from a primary
source:

> "Although Conjecture 1 seems very natural, even its simplest instances are
> not known to be true. For instance, it is not known whether the sequence
> (2^n) is asymptotically equidistributed in base 3. Indeed, even the old
> conjecture of Erdős that states that *all but finitely many terms of this
> sequence contain a digit two in its ternary expansion* is still open."

So: the digit-equidistribution framework is entirely **conditional** on
conjectures; even the simplest case (2^n in base 3) is unresolved; and Erdős's
digit-2 conjecture is confirmed as open by another independent primary source.
The persistence approach has not yielded an unconditional proof.

## Status

Primary source, held in full. Relevant to the run chiefly as (a) an independent
primary confirmation that the Erdős conjecture is still open, and (b) the
statement that the natural equidistribution route is conjectural and, if true,
would actually give *unbounded* persistence for the Erdős–Sloane map — a dead
end for proving boundedness-style obstruction, and a caution that the
equidistribution heuristic does not yield the specific digit-2 claim.

```claim
id: BONUCCELLI-DEFARIA-ERDOS-OPEN-STATUS
statement: The sequence 2^n is not known to be asymptotically equidistributed in
  base 3, and Erdős's conjecture that all but finitely many powers of 2 contain a
  digit 2 in ternary is still open (Remark 3). The de Faria-Tresser
  equidistribution conjecture is unproved even in its simplest instances.
hypotheses: none (status report).
holds-here: yes -- independent primary confirmation that the equidistribution
  route is conjectural and the Erdős digit-2 claim is open.
status: asserted-by-source (status report; the openness is the claim).
bearing: cautions the equidistribution line of attack -- it is conditional on an
  open conjecture and, per Thm 5, would give unbounded persistence for related
  maps rather than the specific obstruction the Erdős conjecture needs.
anchor: research/sources/bonuccelli-colucci-defaria-erdos-sloane-shifted.full.md
```
