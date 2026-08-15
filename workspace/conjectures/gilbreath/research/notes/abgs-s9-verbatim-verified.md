# ABGS 2011 §9 verified verbatim against the full text

**Scholar, 2026.** The run's single most load-bearing claim — the one the whole
Route B conditional deliverable rests on — is `abgs-2011-s9-mod4-switch-limit-open`,
filed as `asserted` (taken on the source's word). This note records that it has
now been **verified against the full text** (`research/sources/ash-beltis-gross-sinnott-2011-successive-prime-residue-pairs.full.md`).

## What the full text actually says (§9, "Further Open Questions")

- "**To the best of our knowledge, Problem 1.1 is wide open, and cannot be
  treated using L-functions, unlike the case of Dirichlet's theorem.**" (from
  the Introduction — stronger than the §9 wording, and the structural fact
  behind the run's two-point settlement).
- §9 asks verbatim whether for any a, d, a′, d′ (all coprime-compatible) the
  ratio `N(a,d,m,x)/N(a′,d′,m,x) → 1` as x→∞. On the data: "the terms appear to
  be getting closer together, but of course **we cannot tell whether they are
  tending toward a limiting ratio of 1**."
- §9 states: "It seems quite possible that N(1,4,4,x) > N(1,2,4,x) for almost
  all values of x" — the Chebyshev-bias-style second-order excess in the
  switch direction, which is exactly the direction G-supply needs.

So the claim block's quoted sentence is **verbatim accurate**, and the deeper
claim it files that "no unconditional positive-density lower bound on the
switch count exists" is the librarian's two-point synthesis (held in
`research/notes/g-supply-two-point-crux-settled.md`), now reinforced by the
paper's own "cannot be treated using L-functions."

## m=4 data (§7) — connects to G-supply

The m=4 pair counts over p ∈ [10^3, 10^6]:

| pair | residue meaning | count |
| --- | --- | --- |
| (1,1) | non-switch | 16574 |
| (3,3) | non-switch | 16715 |
| (1,3) | switch (gap≡2 mod 4) | 22521 |
| (3,1) | switch | 22520 |

Switch total 45041 vs non-switch 33289, ratio ≈ **1.354** — the switch pairs
are the more frequent two at finite x, i.e. ν₂-ish density above n/2. This is
consistent with (not a proof of) the run's measured ν₂/n ≈ 0.49–0.52 and the
`g-supply-transfer-measured` claim (w/n ≈ 0.60). Also consistent with the m=16
"broken diagonal" power-of-2 independence (Prop 4.1): the switch pairs (1,3),
(3,1) are equal to ~1 part in 1000 (22521 vs 22520), confirming the
residue-independence of the switch frequency at m=4.

## Status

- Existing claim `abgs-2011-s9-mod4-switch-limit-open`: **confirmed against the
  primary text**. The `stated` wording is verbatim; the open-question status is
  factual; the "no unconditional linear bound" bearing follows from the
  two-point crux, not from the quote alone.
- What this does NOT do: it does not prove the open lower bound `ν₂ ≥ c·n`.
  It confirms that the bound is open and that the source names it so.

```claim
id: abgs-s9-verbatim-verified
statement: The quote "we cannot tell whether they are tending toward a limiting ratio of 1" (ABGS 2011 §9) is verbatim in the full text; the paper states in the Introduction that Problem 1.1 (asymptotics of N(a,d,m,x)) "is wide open, and cannot be treated using L-functions"; at m=4 the switch pairs (1,3),(3,1) occur 45041 times vs 33289 non-switch over p in [1e3,1e6] (ratio ~1.354), i.e. the switch count exceeds the non-switch count at finite scale, consistent with the run's measured nu2/n ~ 0.5.
hypotheses: primes; N(a,d,m,x) = #{p<q<x : p≡a, q≡a+d (mod m)}.
holds-here: yes
status: checked  (verbatim quote + numeric m=4 counts from the source's own tables; the "no unconditional bound" bearing is the two-point synthesis elsewhere)
bearing: upgrades the run's load-bearing claim from "asserted on the source's word" to "verified against the primary text"; reinforces the two-point crux that Route B cannot be made unconditional by PNT-in-AP/GRH/Dirichlet.
anchor: research/sources/ash-beltis-gross-sinnott-2011-successive-prime-residue-pairs.full.md
answers: abgs-2011-s9-mod4-switch-limit-open (verbatim confirmation)
```
