# Approach: The modular method for the generalised Fermat equation

```approach
idea: Treat x^p - y^q = 1 as a generalised Fermat equation A x^p + B y^q = C z^r
       (here C = 1, r = 1, so z = 1) and apply the Darmon–Granville /
       Frey–Hellegouarch / Ribet–Wiles modular method: attach a Frey
       (elliptic or hyperelliptic) curve to a hypothetical solution, prove its
       mod-(p or q) Galois representation is irreducible and comes from a
       modular form, and derive a contradiction (or a strong constraint) from
       the level-lowering / modularity side.
mechanism: The standard machinery for A x^p + B y^q = C z^r attaches to a
       primitive solution a Frey curve whose conductor is controlled by the
       (small) primes dividing A B C, so its mod-l Galois representation arises
       from a modular form of a bounded level; level-lowering (Ribet) then
       forces the representation to match one of a finite, explicitly computable
       list of newforms, and the absence of such a newform (or its
       incompatibility with the Frey curve's ramification) rules the solution
       out. For Catalan the equation is x^p - y^q = 1, i.e. A = 1, B = -1,
       C = 1, r = 1 — the "signature" (p, q, 1) is a generalised Fermat
       signature with r = 1, so the usual three-term Fermat geometry degenerates
       (one term is a constant), which is exactly why the modular method has
       historically not been the route to Catalan. The value of the proposal is
       to make that *precise*: either the r = 1 signature still admits a usable
       Frey curve (a hyperelliptic Frey curve, or the q-th power as a twist),
       or the obstruction to the modular method is a *named, citable* fact —
       in which case recording it is itself the result that closes this line.
status: refuted
precedent: Darmon-Granville "On the equations z^m=F(x,y) and Ax^p+By^q=Cz^r" Proc. Camb. Phil. Soc. (BLMS) 27 (1995) https://doi.org/10.1112/blms/27.6.513 ; Billerey-Chen-Dieulefait-Freitas "On Darmon's program for the generalized Fermat equation I" https://doi.org/10.1515/crelle-2025-0014 ; Nguyen et al. "Asymptotic Fermat for signatures (r,r,p) using the modular approach" Res. Number Theory 2023 https://link.springer.com/article/10.1007/s40993-023-00474-6 ; Azon "Effective Darmon's program for the generalised Fermat equation" https://arxiv.org/abs/2504.01967
killed-by: The second term of the honest dichotomy closes: r = 1 is a named, citable obstruction. The modular method for generalised Fermat equations is set up for signatures (p,q,r) in the hyperbolic regime 1/p + 1/q + 1/r < 1, where Darmon-Granville prove finiteness and where a Frey curve/abelian variety has conductor controlled by the (prime divisors of) A,B,C and the small primes. For Catalan x^p - y^q = 1 normalised as Ax^p + By^q = Cz^r with r = 1, we have 1/p + 1/q + 1/r = 1/p + 1/q + 1 > 1: NOT hyperbolic, Darmon-Granville finiteness does not apply, and the entire modular literature (Darmon's program, Freitas-Siksek, Billerey-Chen-Dieulefait-Freitas 2025, Azon 2025) treats r >= 2 only. No Frey curve with conductor bounded in terms of ABC (here A=B=C=1) exists for the r=1 degeneration -- the conductor would depend on the free third term. Recording this is the result the file set out to produce: it closes the line.
research-note: This is a refute-on-evidence, not absence: the obstruction is precisely that 1/p+1/q+1/r > 1 for r=1, and that the generalised-Fermat modular framework (every source above) requires r >= 2. Do NOT re-propose the modular method for Catalan as a proof route; the r=1 degeneration is the named reason.
first-step: Reconstruct the Darmon–Granville framework for signature (p, q, r)
       with the equation normalised as A x^p + B y^q = C z^r, and determine the
       exact, citable answer to: *does the r = 1 case (one term constant) admit
       a non-trivial Frey curve with controlled conductor, or does the method
       degenerate?* Write the answer as a claim block with holds-here and the
       known solution's position.
```

## What this buys

A different *engine*. Every route the run currently holds (ideal factorisation,
class group, Stickelberger, double-Wieferich) is arithmetic in the cyclotomic
field. The modular method is arithmetic in a completely different place: the
theory of Galois representations and modular forms attached to elliptic curves.
It is the tool that actually settled Fermat's Last Theorem (Wiles) and has since
solved many generalised Fermat equations of signature (p, q, r) with r ≥ 2. The
reason Catalan was *not* settled this way is itself worth establishing exactly:
it is a boundary case of the framework, and knowing precisely why the standard
Frey curve fails for r = 1 is a genuine, citable, partial result — and the
natural next question (is there a hyperelliptic Frey curve for r = 1, or a
twist that restores a controlled conductor) is a concrete, checkable line.

## The known solution and where it sits

At `3^2 - 2^3 = 1`, `p = 2` is even. The modular method's level-lowering for a
Frey curve attached to a p-th power typically requires the exponent to be an
*odd prime* (to get the mod-p Galois representation with the right ramification),
so the known solution is **excluded by hypothesis** — but only *after* the
exponent-2 cases are proved separately, which is exactly the trap GOAL.md warns
about. The falsification oracle says: **any lemma claiming the modular method
rules out all solutions with p, q > 1 is false**, because it silently assumes
p, q odd prime. The honest statement must begin "for p, q distinct odd primes,
if a primitive solution exists, then ..." and the known solution is recorded as
excluded-by-hypothesis (p = 2 even), not as a genuine exception.

## Why it beats the standard alternative here

- The modular method turns the problem into a *finite* computation over a bounded
  level (the conductor is controlled by the constant coefficients A, B, C = 1),
  and the bound is structural — it does not grow with the problem's effective
  bound, so it is the opposite of "close the gap by computation".
- It produces a dichotomy that is itself a result: either the signature (p, q, 1)
  is solvable by the modular method (a new route to Catalan), or there is a
  named, citable obstruction that explains why the modular method cannot see
  this equation — closing the line honestly and redirecting the run.
- It is the one route with a track record of *proving no solution* for entire
  signatures, which is the exact shape of the target (a negative statement).

## What could kill it

1. **The r = 1 degeneration is real and fatal**: with one term constant, the
   standard Frey curve's conductor is not controlled by {p, q} alone but by the
   unknown x or y, so level-lowering gives no finite list to check. If this is
   the citable outcome, the line is closed as a *named dead end* — which is
   exactly what the approach is designed to find, and recording it prevents the
   run from walking into it.
2. A hyperelliptic Frey curve for r = 1 may exist but have a conductor whose
   level depends on x, y, putting the finite-list step out of reach.
3. The irreducibility of the mod-p representation (a hypothesis of the standard
   lemmas) may fail at the known solution or at the small primes that the
   equation forces (p | y, q | x from Cassels), and would need to be checked,
   not assumed.

## Cost

Determining the r = 1 answer is a literature/construction question (one focused
research task), not a computation. If a Frey curve exists, the finite newform
list for the bounded level is an explicit computation (modular forms databases),
again bounded and structural. The main risk is that the r = 1 case is a known
degeneration; in that case the deliverable is the *exact statement of why*, with
a source, and the line is closed with that reason.
