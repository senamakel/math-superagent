# Attack on G-threshold-shadow

## Hand-found counterexample (n=4, d=1, a=2)

The lemma claims:
  A |-> |O_{<=d}(A)| = |{x in O : |N(x) cap A| <= d}|, over A subset E, |A| = a,
  is maximised by a Hamming ball (initial segment of simplicial/colex order).

Take n=4, d=1, a=2, A = {0000, 1111} (both even weight; NOT an initial segment:
1111 is the weight-4 maximal element).

- Adjacent to 0000: the 4 weight-1 vertices {1000,0100,0010,0001}.
- Adjacent to 1111: the 4 weight-3 vertices {0111,1011,1101,1110}.
- These 8 are exactly O, with no odd vertex in both lists => every odd vertex
  has exactly 1 neighbour in A => |O_{<=1}(A)| = 8 = |O|, the global maximum.

Every simplicial/colex initial segment of E of size 2 = {0000} u {one weight-2
vertex w}; w has 2 weight-1 neighbours, both adjacent to 0000, so exactly 2 odd
vertices have 2 neighbours => |O_{<=1}(initial segment)| = 6.

Thus A beats every ball: 8 > 6. The claim "ball is extremal for |O_{<=d}|" is
FALSE as stated.

## Why it is not n=3
In n=3, even vertices are {000,011,101,110}; the antipode of 0000 is 1111 which
is ODD in n=3, so the antipodal-even pair does not exist there. n=4 is minimal.

## Bearing on the skeleton
G2 supplies the extremal U_d(a) needed for the contrapositive G1 + G3. If the
ball is not the true maximiser, the ball value under-estimates the true max
|O_{<=d}(A)|, so a bound U_d(a) computed at the ball is not a valid upper bound.
Concretely at n=4,d=1,a=2: |O_{<=1}(A)| = 8 > 2^{n-1} - a = 6, so the G1
inequality |O_{<=d}(A)| <= 2^{n-1} - a FAILS for this non-ball A even though it
holds for every ball. The extremal family for the threshold shadow is NOT a
ball; it is an antipodally-split / distributed family.
