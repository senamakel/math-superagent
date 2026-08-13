# Arithmetic Progressions on Conics — Ciss & Moody (J. Integer Seq., PMC5535277)

Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC5535277/ — Abdoul Aziz Ciss, Dustin Moody,
"Arithmetic Progressions on Conics", *Journal of Integer Sequences* 20 (2017), Article 17.1.8(?), 11 pp.
Full text: `research/sources/arithmetic-progressions-on-conics.full.md`.

## What it establishes

An AP on a curve means rational points whose **x-coordinates** form an AP (same convention as
Bremner). Results:

1. **Unit circle** x²+y²=1: there are infinitely many 3-term APs of rational points; a
   parametrisation includes infinitely many in the first quadrant. No 4-term AP exists? (Their
   §2 gives a 3-term construction through any rational point and a no-4-term/classification
   statement in the unit circle case.)
2. **Unit hyperbola** x²−y²=1: infinite families of 3-term APs.
3. **General conics ax²+cy²=1**: constructions of APs of length up to **8** — the longest
   known for conics; infinite families for some parameter values.

## Why it was downloaded

The Φ-quadruple question asks for an AP {q1−q2, q1, q1+q2} of **values** inside the image of
f(t) = sin(4 arctan t) = y-coordinate of a point on the unit circle. The conic literature
(APs of *points on* conics) is the closest classical relative but is a **different set-up**:
there the AP is in the x-coordinate of points *on* the conic; here the three values are
*y-coordinates at three different parameter values*, i.e. an AP inside the image of a fixed
rational map. Ciss–Moody's constructions therefore do **not** bound or construct APs in f(Q);
they confirm that AP-of-length-3 on the circle is abundant (a conic has infinitely many
rational points, so 3-term APs of points are plentiful — which morally explains why the
Φ-lifting must fail higher up: the additive relation among differences, not AP scarcity).

## Bearing on the run

Not a bound. Relevant only as the classical reference for "APs on the circle are easy",
which is consistent with the run's own finding that APs of squares are abundant
(`aps-of-squares-count-asymptotics`): scarcity of APs is not the obstruction; the four-
difference additive relation is. No claim block is taken from this paper.