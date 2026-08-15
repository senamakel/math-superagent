# consecutive: perfect powers differing by 1

## Task A — oracle `solutions(limit)`
`perfect_powers(limit)` -> set of {X^e : X>=2, e>=2, X^e <= limit}, then
group consecutive: consecutive pairs (n, n+1) in sorted order, and also the
reverse (u = n+1, v = n) so that an output like (u**e2, v**e1) can mean
u^e2 - v^e1 = 1.  Two representations then always come from one unordered pair
{u,v}: one with (u^e2, v^e1) where bigger minus smaller = 1 (so u^e2 = v^e1 + 1),
one with (v^e1, u^e2) where v^e1 = u^e2 + 1. That double representation is
expected and harmless; we report BOTH so that every exact equality of the form
a^m - b^n = 1 appearing in the table is listed once.

Every entry a^m - b^n = 1 is recorded with (a, m, b, n):
  - a = y (the smaller base, whose power is the +1 side)
  - m = the exponent on the smaller base
  - b = x (the larger base)
  - n = the exponent on the larger base.
Each line of input_ints.txt:  a^m + 1 = b^n  (difference equals 1).

Output is one line per input integer: "1", "0+", "0", or "?".
"?" means the bound wrap wasn't finished in an earlier run and the number
needs a fresh bounded oracle that also checks x^m = y^n + 1 forms.  We now
handle both forms in one oracle, so treat '?' as solved here: both directions
are searched.
