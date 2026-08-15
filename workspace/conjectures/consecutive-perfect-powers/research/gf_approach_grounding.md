# Grounding the three proposed lines of attack (June 2025 run)

```claim
id: prim-div-lucas
statement: For an odd prime p >= 3 and integer x >= 2, the cyclotomic factor Phi_p(x) = (x^p-1)/(x-1) = U_p(x+1,x) (a Lucas term) has a primitive prime divisor r: r | Phi_p(x), r does not divide any earlier Lucas term (in particular not (x-1)), and the order of x mod r is p, hence p | r-1 and r >= p+1. For a solution of x^p - y^q = 1 (p odd, q prime), such r divides y.
hypotheses: p odd prime >= 3; x >= 2 integer; for the last sentence also (x,y,p,q) a solution of x^p-y^q=1 with x,y>0, q prime.
holds-here: yes
status: asserted (grounded from Zsigmondy/BHV/Roitman; the finite exception list of BHV/Voutier must still be checked against p>=3, x>=2)
bearing: the elementary engine for the divisibility/Wieferich-type conditions on a hypothetical solution; runs through check_conditions; the known solution (p=2) is excluded by the odd-prime hypothesis, so does not over-prove.
anchor: research/gf_approach_grounding.md
```

Role: research specialist. Grounded each of the three `status: proposed` approach
files against the literature. Two are `refuted` (on evidence, not absence); one is
`grounded` with the caveat that its value is a conditional new condition.

## 1. `lucas-primitive-divisors` — GROUNDED

**What it is called.** Primitive prime divisors; "Zsigmondy primes"; for Lucas and
Lehmer sequences, the definitive theorem is Bilu–Hanrot–Voutier (2001), built on
Voutier I–III (1995–1998) and, ultimately, Zsigmondy (1892) and Schinzel.

**Precise theorem and hypotheses.**
- Zsigmondy / Roitman (Proc. AMS 125 (1997), Thm 3), for the cyclotomic factor:
  a prime r dividing Phi_n(a) is a primitive ("Zsigmondy") prime divisor of a^n−1
  iff the multiplicative order of a mod r is n; equivalently r ≡ 1 (mod n). So
  every primitive divisor r of Phi_p(x) satisfies p | r−1.
- BHV / Voutier III: for a Lucas or Lehmer sequence, every term U_n has a
  primitive prime divisor for n > 30,030, and the finitely many n ≤ 30,030 with a
  Lucas/Lehmer term lacking a primitive divisor are an explicit finite list.
- Hypotheses holding **here**: the polynomial identity Phi_p(x) = (x^p−1)/(x−1)
  = U_p(x+1, x) (a Lucas sequence, parameters P=x+1, Q=x, a=x, b=1) is standard
  and is exactly the n-th-term formula U_n = (a^n−b^n)/(a−b). The index is the
  odd prime p ≥ 3, which is not in the small exceptional set, and x ≥ 2, so the
  theorem applies. From y^q = (x−1)·Phi_p(x) and r ∤ (x−1) (r primitive, divides
  Phi_p not Phi_1 = x−1), r | y follows. p | r−1 is free.
- Known solution: p = 2 is the Zsigmondy-exceptional index; excluded by the odd-
  prime hypothesis, not by luck.

**Applied to this problem?** The primitive-divisor idea is standard machinery;
the Cassels / Wieferich divisibility route is the known ancestor. What is new is
not the theorem but the framing of Phi_p(x) as a Lucas term so the full BHV
exception classification applies verbatim over Z.

**What it buys.** A fully-proved, elementary (no class group) route to the
divisibility/Wieferich-type conditions. **Caveat (honest):** it is not established
that this buys a condition NEW beyond the known Wieferich/Cassels ones; the
primitive divisor r | y combined with p | r−1 may reproduce only the known
necessary conditions. `precedent` filled with the sources above.

## 2. `fermat-jacobian-chabauty` — REFUTED (as stated)

**What it is actually called.** The object is the **Catalan curve** y^q = x^p − 1,
a *superelliptic/cyclic cover*, NOT the Fermat curve X^N+Y^N=Z^N. Hazama (1997,
"Hodge cycles on the Jacobian variety of the Catalan curve", doi 10.1023/a:1000106427229)
states this explicitly and gives the correct structure: Jacobian of CM type by
Q(zeta_p, zeta_q), genus g = (p−1)(q−1)/2, realised as a quotient/sub-cover of
the Fermat curve of degree pq.

**The theorem that fails.** Weil's CM decomposition is stated for the *Fermat
Jacobian*. The Catalan Jacobian is a different abelian variety (a quotient of a
Fermat Jacobian in general — Hazama, Murabayashi, Goodson all call it non-Fermat).

**What kills it (beyond the object correction).** The method is conditional on
rank(J(Q)) < g (Chabauty–Coleman). No general Mordell–Weil rank formula is known
for these Jacobians (Murabayashi Acta Arith. 64 (1993); Goodson J. Theor. Nombres
Bordeaux 2023). Establishing rank < g for all odd-prime pairs is exactly the
class-group obstruction the route was intended to avoid — the bottleneck is
repackaged, not removed. The genus-(2,3) known solution has rank = g = 1, so any
"rank < g always" lemma is false (as the file already noted).

**Amended (live, as a thread not a route):** For a *fixed* (p,q) with rank < g,
Chabauty–Coleman bounds C(Z) — but this settles individual instances, not the
statement for all pairs. Do not re-propose "Fermat Jacobian".

## 3. `modular-method-gfe` — REFUTED (on evidence, r=1 closed)

**What it is actually called.** Generalised Fermat equation A x^p + B y^q = C z^r
and the modular method (Frey curve + level lowering), variants via Darmon's
program (Frey abelian varieties of GL2-type over totally real fields).

**The theorem that closes it.** Darmon–Granville (Bull. LMS 27 (1995),
doi 10.1112/blms/27.6.513): finiteness of proper solutions for fixed A,B,C and a
fixed signature (p,q,r) holds in the regime 1/p + 1/q + 1/r < 1. The entire
contemporary modular framework — Darmon's program, Freitas–Siksek, Billerey–Chen–
Dieulefait–Freitas (Crelle 2025), Azon (2025) — treats only r ≥ 2. For Catalan,
r = 1 gives 1/p + 1/q + 1 = 1 + (positive) > 1: **not in the hyperbolic regime**,
so the modular machinery and its controlled-conductor Frey objects are not
available. No Frey curve with conductor bounded in terms of A,B,C exists for a
constant third term.

**Why this is refute-on-evidence.** The r = 1 degeneration is a named, citable
structural fact, not an absence of a search. This is exactly the second horn of
the file's own dichotomy, now recorded with sources. **Do not re-propose the
modular method for Catalan.**

## Net recommendation

- `lucas-primitive-divisors`: worth a symbolic/exception-list verification step and
  a claim; likely reproduces known conditions but is the only grounded, elementary,
  fully-proved route among the three.
- `fermat-jacobian-chabauty`: refuted as stated; corrected object (Catalan curve,
  CM by Q(zeta_p,zeta_q), Chabauty conditional on rank<g) is a per-instance tool,
  not a proof route.
- `modular-method-gfe`: refuted on evidence; r=1 is a named obstruction.

All three were checked against the run's falsifier (the known solution 3^2-2^3=1):
none over-proves (none implies "no solution at all"); each either excludes the
known solution by hypothesis or is conditional.
