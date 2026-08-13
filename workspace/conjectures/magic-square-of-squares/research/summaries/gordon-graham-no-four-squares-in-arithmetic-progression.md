# Gordon–Graham, "There are no four squares in arithmetic progression"

[[gordon-graham-no-four-squares-in-arithmetic-progression]]

Source: T. Gordon, R. Graham, "There are no four squares in arithmetic progression",
The Fibonacci Quarterly 53.1 (2015), 3–8,
https://www.fq.math.ca/Papers1/53-1/GordonGraham09012014.pdf .
Full text at `research/sources/gordon-graham-no-four-squares-in-arithmetic-progression.full.md`.

## What it establishes

A **descent** proof of Fermat's classical no-four-squares-in-AP result, strengthened to a
cleaner statement. It also — usefully for this run — surveys the panoply of existing proofs
and singles out a **persistently incorrect proof** to avoid.

**Theorem 2.1.** There are no Pythagorean triples of the forms `(a,b,c)` and `(a,2b,d)`
simultaneously.

**Corollary 2.2.** If `p⁴ − p²q² + q⁴ = r²` with `p,q` positive integers, then `p = q`.

**Theorem 2.3.** The product of four distinct positive integers that form an arithmetic
progression cannot be a perfect square: there are no positive integers `a, d, x` with
`a(a+d)(a+2d)(a+3d) = x²`.

**Corollary 2.4.** There are no four distinct squares that form an arithmetic progression.

**Corollary 2.5.** If `a² + b²` is a square, then `a² + 4ab + b²` is not a square.

## Bearing on the 3×3 MSS

- Corollary 2.5 is directly relevant: it says that out of any Pythagorean pair `(a,b)`
  (i.e. any single realised centre AP-difference endpoint), the "next" form
  `a²+4ab+b²` cannot be a square. This is exactly the kind of structural constraint on
  consecutive AP-differences through a common centre that a descent on the `Φ` additive
  quadruple would use.
- Theorem 2.3's form `∏(a+id) = x²` is the product form of the no-4-square-AP statement;
  the descent gives a template for how a non-existence proof here must be a genuine
  descent (produce a strictly smaller solution), not a modular sieve — which this run has
  already shown is insufficient (`phi-padic-no-obstruction`, checked).
- The paper's careful takedown of an incorrect proof mirrors this run's own audit
  discipline (the `ferreira-1506-06621-refuted` failure mode — substituting a root back
  into the equation it solved).

```claim
id: no-four-squares-in-ap-descent
statement: The product of four distinct positive integers in arithmetic progression is
  never a square (Gordon–Graham Thm 2.3); hence no four distinct squares form an AP.
  Corollary 2.5: if a²+b² is a square then a²+4ab+b² is not.
hypotheses: distinct positive integers; a,d>0.
holds-here: yes — a classical model of the descent the run's Φ/triple and four-AP
  arguments would need; it does not by itself settle the 3×3 case (which needs a common
  middle square in four linked 3-APs, not four terms of one AP).
status: proved (Gordon–Graham, infinite descent)
bearing: structural constraint on AP-difference forms through a shared square centre;
  survey of the (varied, some incorrect) proofs of the n=4 case.
anchor: research/summaries/gordon-graham-no-four-squares-in-arithmetic-progression.md
```

## Falsifier

A quadruple of distinct positive integers `a(a+d)(a+2d)(a+3d)=x²` would falsify
Theorem 2.3; none exists (the descent yields a strictly smaller one, a contradiction).
The incorrect-proof caution: several published "proofs" of Corollary 2.4 make exactly the
root-substitution error this run audits for.
