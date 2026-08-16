# Approach: tropicalization / initial-ideal fan of the resultant ideal over ℤ

```approach
idea: Tropicalize the Casas-Alvero variety. Over ℤ the conditions are the resultants
       R_i = Res_x(f, H_i(f)) ∈ ℤ[a_1,…,a_{d−1}] (Hasse derivatives), and CA_d,0 is
       exactly V(R_1,…,R_{d−1}) = ∅ over ℚ̄. Work with the *global* polyhedral object:
       the Gröbner fan of the ideal I = (R_1,…,R_{d−1}) and the tropical prevariety
       Trop(V(I)) with respect to the trivial valuation on ℚ (equivalently: the
       initial ideals in_w(I) over all weight vectors w). By the Fundamental Theorem
       of Tropical Geometry, V(I) = ∅ over ℚ̄ iff every initial ideal in_w(I) is the
       unit ideal — a purely combinatorial emptiness certificate, not a Gröbner
       decision run at one order.
mechanism: This is NOT "Newton-polygon bookkeeping of f" (which the char-p test kills
       because it ignores the characteristic). The object here is the fan of the
       *ideal* of resultants, and the char-0/char-p distinction enters through the
       coefficients: reduction mod p changes the *support* of each R_i (a monomial of
       R_i whose integer coefficient is divisible by p disappears mod p), so the
       Newton polytopes — and hence the tropical variety — over ℚ and over 𝔽_p are
       different objects. The char-p witnesses x^{p+1}−x^p must live in a tropical
       cell of the 𝔽_p tropicalization whose existence depends on a monomial of some
       R_i that is divisible by p. So the char-p break is explicit and checkable:
       find the monomial(s) of R_i killed by p and the cell they create. If the
       empty-over-ℚ̄ certificate ever needs a monomial whose coefficient p divides,
       that is precisely where the argument stops being valid mod p.
first-step: For d = 4,5,6 compute the Newton polytope of each R_i over ℚ (sympy),
       then the tropical prevariety of (R_1,…,R_{d−1}) (initial ideals at a sample
       of weight vectors, or Singular 'tropical.lib'), and — for the bad primes of
       those d — the 𝔽_p support of each R_i, locating the monomials killed by p and
       the char-p witness's cell. Assert the guards through code/lib/casas_alvero.
charp-break: monomials of R_i with coefficients divisible by p; a certificate that
       survives reduction mod p would prove the false char-p statement and is refuted.
status: refuted
killed-by: (1) False premise — V(R_1,…,R_{d−1}) is not ∅: the pure power x^d
       (a_1 = … = a_{d−1} = 0) is a CA polynomial and lies in the variety; CA
       says V(I) = {0}, equivalently ht(I) = d−1 (Schaub–Spivakovsky,
       peer-reviewed J. Commut. Algebra 2025). The Fundamental Theorem's
       emptiness certificate therefore does not apply; the correct tropical
       statement is a dimension/height one (Trop(V(I)) zero-dimensional at the
       origin), strictly harder than the proposal assumes. (2) Infeasibility —
       the Gröbner fan dominates the single-Gröbner cost, and that cost already
       fails at d = 8 over ℚ (established computational-boundary), so the fan at
       d = 20 is out of reach by construction. (3) Redundancy — its one correct
       insight (reduction mod p kills monomials of R_i with p-divisible
       coefficients) is already established as resultant-monomials +
       bad-prime-criterion.
```
