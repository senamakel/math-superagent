# Weakened ladder for x^p - y^q = 1 (consecutive perfect powers)

The declared difficulties are specific obstructions, not topics. The `off` field
of every rung is a subset of these exact names.

- `odd-prime-both` — both exponents are odd primes, so `x^p - y^q` has no
  factorisation over `Z` or `Z[i]`; the elementary method of the bottom rungs is
  gone and the argument must live in `Z[zeta_p]`.
- `nonprincipal-ideals` — the class-group obstruction: in `Z[zeta_p]` the
  equation forces an *ideal* factorisation, and lifting it to an *element*
  relation requires the relevant ideals to be principal; they need not be.
- `unbounded-exponents` — `p, q` range over all odd primes, so the field
  `Q(zeta_p)` itself varies with `p`; no single fixed ring contains the argument.
- `independent-pq` — **both** `p` and `q` are arbitrary, unrelated odd primes, so
  the double-Wieferich-type relations linking them must be excluded with no
  fixed small prime as a handle. Off once either exponent is fixed to a concrete
  prime or a concrete pair.
- `unconditional-class-number` — the relevant class number (on Mihailescu's
  route, the minus part `h^-` of the cyclotomic field) must be controlled by a
  proved bound, not GRH or Cohen–Lenstra heuristics.
- `astronomical-bound` — the effective bound from linear forms in logarithms is
  far beyond any computable search, so a rung with unbounded exponents cannot be
  settled by enumeration and must be settled structurally.

```ladder
goal: determine all integer solutions of x^p - y^q = 1 with x,y>0 and p,q>1; the conjecture is that (x,p,y,q)=(3,2,2,3) is the only one
difficulties: odd-prime-both, nonprincipal-ideals, unbounded-exponents, independent-pq, unconditional-class-number, astronomical-bound
status: open
```

```rung
id: R-cat-x2y3
statement: all integer solutions of x^2 - y^3 = 1 with x,y>0; claim exactly (x,y)=(3,2)
off: odd-prime-both, nonprincipal-ideals, unbounded-exponents, independent-pq, unconditional-class-number, astronomical-bound
stance: open
merge: (x-1)(x+1)=y^3 over Z with gcd(x-1,x+1) | 2 splits into two cases, both forced to cubes. The same two-case argument is uniform in the odd exponent, so promote to x^2 - y^q = 1 (R-cat-x2yq) at no new cost.
```

```rung
id: R-cat-x2yq
statement: all integer solutions of x^2 - y^q = 1 with x,y>0 and q an odd prime; claim exactly (3,2,2,3)
off: odd-prime-both, nonprincipal-ideals, unbounded-exponents, independent-pq, unconditional-class-number
stance: open
merge: q runs over all odd primes but the factorisation stays in Q, so the method is uniform (unbounded-exponents off). To reach the mirror x^p - y^2 = 1 the factorisation moves into Z[i]: x^p = (y+i)(y-i) with gcd(y+i,y-i) | 2i. Only new ingredient: Z[i] is Euclidean (class number 1).
```

```rung
id: R-cat-xpy2
statement: all integer solutions of x^p - y^2 = 1 with x,y>0 and p an odd prime; claim none
off: odd-prime-both, nonprincipal-ideals, unbounded-exponents, independent-pq, unconditional-class-number
stance: open
merge: now both exponents become odd primes and factorisation over Z/Z[i] disappears: odd-prime-both and unbounded-exponents turn on together, forcing the move into Z[zeta_p]. First rung where both rings are UFDs: the fixed pair x^3 - y^5 = 1 (R-cat-35), with h(zeta_3)=h(zeta_5)=1 so nonprincipal-ideals stays off.
```

```rung
id: R-cat-35
statement: all integer solutions of x^3 - y^5 = 1 with x,y>0; claim none
off: nonprincipal-ideals, unbounded-exponents, independent-pq, unconditional-class-number, astronomical-bound
stance: open
merge: turn nonprincipal-ideals back on at a fixed pair where one cyclotomic ring is not a UFD: the first is p=23, h^-(Q(zeta_23))=3. The step to watch is exactly the ideal-to-element lift the bottom rungs got for free; at (p,q)=(23,·) that is where the argument first fails.
```

```rung
id: R-cat-fixed
statement: for a fixed pair (p,q) of odd primes, all integer solutions of x^p - y^q = 1 with x,y>0; claim none for any odd-prime pair
off: unbounded-exponents, unconditional-class-number, astronomical-bound, independent-pq
stance: open
merge: let one exponent vary: x^3 - y^q = 1 with q an arbitrary odd prime turns unbounded-exponents back on (Q(zeta_q) varies with q) and unconditional-class-number with it, while p stays fixed; that is the shape of the known partial results and the next real rung.
```

```rung
id: R-cat-x3yq
statement: all integer solutions of x^3 - y^q = 1 with x,y>0 and q an odd prime; claim none
off: independent-pq
stance: open
merge: drop the fixed exponent 3 and let both p,q be arbitrary odd primes; the two things still switched off are the double-Wieferich exclusion (independent-pq) and the unconditional h^- bound. That is the full goal.
```

```rung
id: R-cat-full
statement: all integer solutions of x^p - y^q = 1 with x,y>0 and p,q odd primes; claim exactly (3,2,2,3) overall
off:
stance: open
merge: this is the goal itself, every difficulty on. Reaching it from R-cat-x3yq needs (a) the double-Wieferich exclusion with both exponents free, and (b) an unconditional (non-GRH) bound on the relevant class number. These are the two ingredients problem.md names as the heart of the open content; neither is sourced in this run yet.
```
