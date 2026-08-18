# Patrício & Hartwig — the geometric-sum Euclidean recursion (academic anchor for G4)

```claim
id: geometric-sum-division-algorithm
statement: For the geometric sum G_n(x) = 1 + x + ... + x^{n-1}, Euclid's division
n = mq + r (0 <= r < m <= n) gives the recursion
G_{r+mq}(x) = x^r G_m(x^q) G_q(x) + G_r(x),
and for n = mq the special case G_{mq}(x) = G_m(x) G_q(x^m).
This is a published, non-competitive-programming statement of the geometric-weight
Euclidean split that the universal-Euclidean / OI-wiki merge-flip recursion rests on;
it shows the recursion is O(log) in n because after each nontrivial cycle the larger
Euclidean parameter strictly decreases, as in the ordinary Euclidean algorithm.
hypotheses: x an element of an (associative, unital) ring; the corner-sum/generalisation
holds even when x,c,y do not commute (Prop 2.4, eq (33)).
holds-here: true. PE1006's Psi(k) is the second moment of a 10^j-geometric floor sum
over k+1 reps; the geometric weight w = z^dR has exactly this G_n form, and the
universal-Euclidean monoid composes segments by the same mq+r split. The recursion is
the arithmetic engine behind the O(log) evaluation at k = 10^18.
status: sourced
bearing: Gives the final-step primitive (directive 2 / G4) a citable academic anchor
that is not a competitive-programming blog, part of the answer to the request
citable-name-treatment-0c91.
anchor: research/sources/patricio-hartwig-euclid-corner-sums.full.md
  (Patrício & Hartwig, "From Euclid to Corner Sums", Filomat 35(14) 2021, 4613-4636;
  Prop 2.4 eq (33)-(35); source URL http://elib.mi.sanu.ac.rs/files/journals/flmt/177/flmn177p4613-4636.pdf)
answers: citable-name-treatment-0c91
```

## What this adds to the library

- The request `citable-name-treatment-0c91` asked for *"a citable name/treatment of the
  universal Euclidean algorithm ... that evaluates sum floor-based geometric sums in
  O(log k)"*. The in-library sources were oi-wiki, cnblogs/fhq, LOJ138, AtCoder — all
  competitive-programming retellings.
- This is a **published, peer-reviewed** paper (Filomat 35:14, 2021) that extends
  Euclid's algorithm to geometric sums and corner sums, and its Proposition 2.4
  gives the geometric-sum division algorithm:
  `G_{r+mq}(x) = x^r G_m(x^q) G_q(x) + G_r(x)`.
- This is the same recursion the competitive-programming universal-Euclidean monoid
  implements (`solve` in the fhq source: `pow(b,(q-r-1)/p) + a + solve(...) + pow(b,cnt)`
  is exactly the Euclidean split-and-conquer on the geometric weights). The paper
  gives it a precise, citable statement and the O(log) convergence argument
  ("the larger Euclidean parameter strictly decreases, as in the ordinary Euclidean
  algorithm", Prop 2.4 ff).
- It does **not** carry the floor-moment tuple (S1, S2) explicitly — those come from
  the fhq/LOJ138/oi-wiki monoid. So the corner-sums paper is the *geometric-weight
  recursion* anchor; the *moment-carrying* monoid is still anchored by the
  competitive-programming sources + the run's own proven formula
  (claim `monoid-composition-formulas-verified`). Together they cover both halves of
  the request.

## The disconnect that remains (not the librarian's to solve)

The request's falsifies column — "if the Euclidean recursion required enumerating the
k+1 representatives or the k-1 floor terms (i.e. were not O(log) in k), G4 would be
refuted" — is not triggered by anything on disk. Both the published corner-sum
recursion (this paper, Prop 2.4) and the competitive-programming universal-Euclidean
sources are O(log) in k. The run's remaining work is executable (fix ueuclid.py S1/S2
compose), not a missing source.
