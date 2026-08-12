# Morgenstern, "Some extended searches", 2013 (multimagie.com)

[[morgenstern-extended-searches-2013]]

The run's key **computational bound** on four-AP / equal-step configurations.

## Established statements

The near-MSS construction needs several 3-term APs of squares with a prescribed common
difference `d`. Morgenstern exhaustively enumerated:
- **Three APs with equal `d`, all odd entries**: complete enumeration to `d ≤ 2.4×10¹⁹`,
  partial beyond; found **3809** instances, of which all but the following were eliminated
  because two scale factors shared a prime or a scale factor was a multiple of an `8k+3` prime:
  - `d = 71831760`: two sets of three APs;
  - `d = 2.75×10¹⁵`: one set (three APs).
- **Three *primitive* APs with equal `d`**: only **5** instances total, the largest at
  `d = 3.31×10¹⁵`; **none beyond** that up to `d = 6.4×10²²`.

## Implications for this run
- A true MSS needs **four** centre APs with differences `u, v, u+v, u−v`, a stronger
  condition than three equal-`d` APs. Morgenstern shows three equal-`d` primitive APs die out
  by `d ≈ 3.3×10¹⁵`. So any MSS with centre `e²` would force four of these linked patterns;
  the bound localises the non-existence region to `d` far beyond this run's reach.
- The `8k+3`-prime elimination and "two scale factors share a prime ⇒ dead" are the exact
  sieve rules an impossibility argument can reuse (they are consistent with Morgenstern's
  Thm 5/6 elementary results).

## Assessment
- This is the run's documented computational boundary (CONTEXT.md "Numbers" section relies on
  it). Confirmed here as stated.

```claim
id: three-primitive-equal-d-bound
statement: Up to d = 6.4×10²² there are only five configurations of three primitive 3-square
  APs all with the same difference d, the largest at d = 3.31×10¹⁵.
hypotheses: three APs of squares, primitive, equal difference d, all odd entries
holds-here: yes (bound is exhaustive, stated in the source)
status: catalogued
bearing: the literature's real search boundary; the four-AP MSS condition is stronger
anchor: research/sources/morgenstern-extended-searches-2013.full.md
```
