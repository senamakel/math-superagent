# Reduce to prime exponents, then split on the exponent-2 cases

```skeleton
goal: x^p - y^q = 1 with x,y>0, p,q>1 has (x,p,y,q)=(3,2,2,3) as its only solution.
implies: Take any solution (x,p,y,q). Write p=a·p', q=b·q' with p',q' prime. By G-prime-reduction, (x^a,p',y^b,q') is a solution, and since 3 and 2 are not perfect powers, (x,p,y,q)=(3,2,2,3) iff (x^a,p',y^b,q')=(3,2,2,3). Split on the prime exponents: (i) p'=2 — G-exp2-a forces (x^a,2,y^b,q')=(3,2,2,3), hence the original equals (3,2,2,3); (ii) q'=2 — G-exp2-b says x^{p'}-(y^b)^2=1 has no solution for any prime p', contradiction; (iii) p',q' both odd primes — G-odd-prime says no solution, contradiction. These three exhaust all cases, so every solution is (3,2,2,3).
status: sketched
rests-on: none (research/CLAIMS.md is empty; every lemma below is open)
```

```gap
id: G-prime-reduction
lemma: If (x,p,y,q) solves x^p - y^q = 1 with x,y>0, p,q>1, and p=a·p', q=b·q' with p',q' prime, then (x^a,p',y^b,q') also solves it; moreover (x,p,y,q)=(3,2,2,3) iff (x^a,p',y^b,q')=(3,2,2,3). In particular the conjecture reduces to prime exponents.
status: open
next: theorem_prover — formalise in Lean 4/Mathlib: (x^a)^{p'}=x^p, the "3 and 2 are not perfect powers" uniqueness step, and the iff. Report #print axioms. This is the one-line reduction every downstream argument assumes, and it must be airtight before G-odd-prime is even considered.
```

```gap
id: G-exp2-a
lemma: x^2 - y^q = 1 with x,y>0 and q prime has the unique solution (x,y,q)=(3,2,3).
status: open
next: theorem_prover — prove by factorising y^q=(x-1)(x+1) in Z; gcd(x-1,x+1)∈{1,2}, split on parity of x. The known solution (3,2,3) is exactly this q=3, x=3 case, so the lemma must return it, not exclude it. Classical (Lebesgue); redo in full here.
```

```gap
id: G-exp2-b
lemma: x^p - y^2 = 1 with x,y>0 and p prime has no solutions.
status: open
next: theorem_prover — prove in Z[i]: x^p=(y+i)(y-i) with gcd(y+i,y-i) a unit times a power of (1+i); deduce y+i=u(a+bi)^p and compare imaginary parts via the binomial theorem to contradict odd p; p=2 is difference of squares. The known solution (3,2,2,3) has y-exponent 3, so it sits outside this case and nothing is excluded.
```

```gap
id: G-odd-prime
lemma: x^p - y^q = 1 has no solution with p,q odd primes.
status: open
next: this is the open content; it is decomposed in research/backward/both-odd-primes.md. First concrete move there: G-Cassels (p|y, q|x), handed to theorem_prover with the Cassels 1960 source fetched by the librarian.
```
