# Pirzada, Shah & Baskoro, "On 2-power unicyclic cubic graphs", EJGTA 10(1) (2022) 24

[[research/sources/pirzada-shah-baskoro-2-power-unicyclic-cubic.full.md]] · source URL: https://doi.org/10.5614/ejgta.2022.10.1.24

## What it establishes

Constructs an **infinite family of 2-power-unicyclic cubic graphs**: cubic graphs containing **exactly one** cycle whose length is a power of two (a "2-power cycle"). The constructions have even order n=2^s and their single 2-power cycle has length 2^k < s; all other cycle lengths are non-power-of-two.

The author's framing claim — "the only 2-power cycle in a cubic graph cannot be removed, implying there does not exist a counterexample to the Erdős–Gyárfás conjecture" — is a loose/overbroad phrasing. The legitimate content is narrower: each constructed member does satisfy EG (it has its single 2-power cycle), and this particular construction method cannot produce a counterexample. It does **not** prove the conjecture. Treat the advertised "does not exist a counterexample" as a statement about this family only, not the general conjecture — the abstract is aspirational, the construction is the real result.

## Why it matters

- With Bensmail's result (arbitrarily large cubic graphs whose only 2-power cycles have length 4 only or 8 only), the construction landscape is now clear: you can make large cubic graphs whose power-of-two cycles are *sparse and short*, but no one has made one with *none*. This is exactly the tension at the heart of the conjecture — the obstruction is keeping ALL powers of two out simultaneously.
- Corroborates the run's structural picture: a minimal counterexample, if it exists, must have power-of-two cycles *almost but not quite* forced across its cycle spectrum.

**Claim block** (fenced for CLAIMS.md):

```claim
id: EG-pirzada-2-power-unicyclic-family
statement: There exists an infinite family of simple cubic graphs each containing exactly one cycle whose length is a power of two (order 2^s, that one cycle of length 2^k < s).
hypotheses: cubic simple graphs; construction given in paper.
holds-here: shows power-of-two cycles can be made arbitrarily sparse (down to one) among the cycle lengths of cubic graphs, yet still present — so the obstruction is forcing all powers out at once, not finding any.
status: asserted-by-source (construction; proof of existence not re-verified here)
bearing: bounds what a would-be counterexample construction must achieve: keep every 2^k out, while existing constructions only thin the set down to one.
anchor: research/summaries/pirzada-shah-baskoro-2-power-unicyclic-cubic.md
```
