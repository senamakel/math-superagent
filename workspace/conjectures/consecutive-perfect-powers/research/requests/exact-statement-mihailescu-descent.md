# Request `exact-statement-mihailescu-bbf8` — the descent step: what is screened, what the run's own arithmetic shows

## Request, restated

Does Mihailescu's 2002 descent step in the proof of Catalan's conjecture produce
**cross-prime minus-class-number divisibility** `q | h^-(Q(ζ_p))` (and mirror
`p | h^-(Q(ζ_q))`) as a forced consequence of a hypothetical solution of
`x^p - y^q = 1` (p, q distinct odd primes) satisfying `p | y`, `q | x` and the
double-Wieferich congruences? Or is the real mechanism different — same-prime
p-part padding via a direct factor, or a genuinely different obstruction?

## Screening: the exact published descent step is not reachable in this run

Every search query aimed at the published proof's final step was withheld by the
run's evidence policy:

> "...screens sources that would supply a published answer to the problem in
> `problem.md`... Do not rephrase the query to get around it, and do not try
> another route to the same source."

That screen is on-grade here: **the exact descent step of Mihailescu's 2002
proof IS the published answer to the run's problem.** `problem.md` asks for the
proof that `(3,2,2,3)` is the only solution; Mihailescu's final step is that
proof's load-bearing clause. The primary sources (Mihailescu 2002/2003;
Schoof's book *Catalan's Conjecture*; Bourbaki) and citation-graph routes to them
are therefore all closed off by the policy. **I cannot, from sources, produce the
citable exact statement the request asks for.** What would settle it is a
primary-source read of the descent step, which this run's boundary forbids.

What I can and should do with the run's own tools: (a) state precisely what is
screened; (b) test the *specific, checkable sub-claim* the request names — the
cross-prime divisibility `q | h^-(Q(ζ_p))` — against the exact, workspace-computed
class numbers at the double-Wieferich pairs that the conditional theorem leaves
alive; and (c) reason from the held technique tier about which mechanism the data
supports. (b) is a genuine, non-screened contribution.

## The decisive computed datum

The run already computed the minus class numbers and the double-Wieferich pairs
exactly (`code/out/pattern_dw_structure.captured.txt`,
`code/out/pattern_sequences.captured.txt`). The double-Wieferich pairs below
200000 (the only exponent pairs the conditional non-Wieferich theorem does NOT
exclude) are exactly:

```
(83, 4871)      minimal; 83 is REGULAR (83 ∤ B_{2k} for 2 ≤ 2k ≤ 80)
(2903, 18787)   smaller member irregular (2903 | B_2386)
(911, 318917)   known pair; smaller member irregular (911 | B_60)
```

For the minimal pair, the descent field's minus class number:

```
h^-(Q(ζ_83)) = 838216959 = 3 · 279405653      (exact)
  83   | h^-(83)    ?  False
  4871 | h^-(83)    ?  False
```

Hand-check (independent of the captured output): 838216959 / 3 = 279405653 exact
(digit sum 51); 4871·172000+4871·83 = 837812000+404293 = 838216293, remainder
666 ≠ 0, so 4871 ∤; 83·3366333 = 279405639, remainder 14 ≠ 0, so 83 ∤. Confirmed.

**At the minimal double-Wieferich pair (83, 4871) — the first exponent pair a
hypothetical odd-prime solution would have to be — `Cl^-(Q(ζ_83))` has order
coprime to BOTH exponents 83 and 4871, and 83 itself is regular.**

## What this does and does not establish about the request's question

### It does NOT refute the cross-prime forcing claim `solution ⇒ q | h^-(Q(ζ_p))`

That claim is one-way: a *solution* forces the divisibility. (83,4871) is a
double-Wieferich pair, a superset of the possible exponent pairs (solution ⇒
double-Wieferich), but it is not itself a solution. So `4871 ∤ h^-(83)` does not
touch the forcing claim's truth. It only says (83,4871) is not a solution *to
that forced relation* — which is exactly what a sieve wants.

### What it DOES establish — two precise, sourced-by-computation facts

**Fact 1 — the cross-prime condition, if true, has teeth at the first survivor.**
If the descent genuinely forced `q | h^-(Q(ζ_p))` and `p | h^-(Q(ζ_q))`, then the
minimal double-Wieferich pair (83,4871) would be excluded by it (4871 ∤ h^-(83)).
So the cross-prime sieve is *not vacuous*: it kills the very first pair the
Wieferich sieve leaves standing. This is the favourable case for the approach
note `minus-classnumber-crossprime-bernoulli.md` — but is NOT evidence the forcing
is true.

**Fact 2 — the same-prime minus-class-group torsion mechanism is DEAD at this
pair.** The run's own note states the consequence plainly: at (83,4871), 83 is
regular and `Cl^-(Q(ζ_83))` is coprime to both exponents, so "an ideal-to-element
lift here would have to cross no p-torsion in Cl^-". A descent whose obstruction
is the p-part (or q-part) of `Cl^-(Q(ζ_p))` **cannot be** the mechanism — the
relevant torsion is absent. This refutes (for this pair) the "same-prime p-part
torsion of the minus class group" reading of the descent, in favour of the
request's third alternative: **a genuinely different obstruction** (plus-part /
unit-group index / the direct-factor structure that survives coprime-minus-class
groups).

## The honest answer to "is cross-prime `q | h^-(Q(ζ_p))` a published consequence?"

**Cannot be confirmed from sources in this run** — the primary statement is
screened, and no retrieved source asserts it. It is a *reconstruction/candidate*,
not a sourced consequence.

**Scepticism (structural, not sourced).** The one-place implication cannot be
falsified by computation, but the *form* is suspect on the run's own arithmetic:
cross-prime divisibility of h^- is an accidental Bernoulli-product coincidence
(e.g. it happens at (p,q)=(23,3) — h^-(23)=3 — but (23,3) is not double-Wieferich),
and it does NOT follow from being a double-Wieferich pair (it fails at the minimal
one). A genuine descent mechanism would be expected to generalize across the
surviving pairs, not to single out the minimal one. That is evidence the real
mechanism is NOT captured by a bare `q | h^-(Q(ζ_p))` Bernoulli test.

## What would settle the request (recorded, not retrievable here)

A primary-source statement of the descent step's relation to the minus class
group — the Stickelberger/cyclotomic-unit relation it actually uses, and whether
the relevant prime is the same exponent prime (p-adic in Q(ζ_p)) or the opposite
cross prime. Screened. Recorded as an open request; the run's own arithmetic
bounds where the obstruction can and cannot live.

## Claims

```claim
id: dw83-hminus-coprime-both-exponents
statement: >
  For the minimal double-Wieferich odd-prime pair (83,4871): h^-(Q(ζ_83)) =
  838216959 = 3·279405653 (exact), and neither 83 nor 4871 divides h^-(Q(ζ_83)).
  Also 83 divides no even Bernoulli numerator B_{2k}, 2 ≤ 2k ≤ 80 (83 regular).
hypotheses: (p,q) a double-Wieferich pair; h^- of Q(ζ_p) from the Bernoulli
  character product.
holds-here: yes — (83,4871) is the minimal double-Wieferich pair, i.e. the first
  pair the conditional non-Wieferich theorem does not exclude.
status: checked — exact integer arithmetic (pattern_dw_structure.captured.txt);
  the factorisation 3·279405653 and the non-divisibility by 83 and 4871 were
  re-verified by hand here.
anchor: code/out/pattern_dw_structure.captured.txt
bearing: bounds the descent: the obstruction to an ideal-to-element lift at
  (83,4871) is NOT p- or q-torsion of Cl^-(Q(ζ_83)), since that group is coprime
  to both exponents.
```

```claim
id: crossprime-q-hminus-not-sourced
statement: >
  The claim that a hypothetical solution x^p-y^q=1 (p,q distinct odd primes
  forcing p|x, q|y, double-Wieferich) forces cross-prime divisibility
  q | h^-(Q(ζ_p)) and p | h^-(Q(ζ_q)) is NOT a published consequence that this
  run can cite: the primary descent-step source is screened by the evidence
  policy, and no retrieved source asserts it. It is a candidate/reconstruction.
  It is also NOT a consequence of the double-Wieferich condition alone, since it
  fails at the minimal double-Wieferich pair (83,4871): 4871 ∤ h^-(Q(ζ_83)).
answers: exact-statement-mihailescu-bbf8
hypotheses: the cross-prime forcing hypothesis under evaluation.
holds-here: n/a — this claim reports the sourcing failure and the computed
  counterexample to "double-Wieferich ⇒ cross-prime h^- divisibility".
status: asserted (sourced-negative: screening + exact computation); not proved.
anchor: research/approaches/minus-classnumber-crossprime-bernoulli.md;
  code/out/pattern_dw_structure.captured.txt
bearing: the cross-prime Bernoulli sieve is a candidate necessary condition on a
  HYPOTHETICAL solution, not an established forced consequence; the workspace
  must not promote it to a proof step.
```

```claim
id: same-prime-minus-torsion-absent-at-83-4871
statement: >
  At the minimal double-Wieferich pair (83,4871), Cl^-(Q(ζ_83)) has no torsion at
  either 83 or 4871 (h^-(83) = 838216959 coprime to both), and 83 is regular.
  Therefore a descent whose obstruction is the same-prime p-part of Cl^-(Q(ζ_p))
  cannot be the mechanism at this pair; the obstruction (if any) lies in the
  plus part, the unit-group index, or a direct-factor structure that survives a
  minus class group coprime to both exponents.
hypotheses: (p,q)=(83,4871), the minimal double-Wieferich pair.
holds-here: yes — this is exactly the first surviving exponent pair.
status: checked (exact arithmetic); the 'cannot be the mechanism' is a justified
  inference for THIS pair, not a theorem for all pairs.
anchor: code/out/pattern_dw_structure.captured.txt
bearing: refutes (at this pair) the 'same-prime minus-class-group torsion'
  reading of the descent, in favour of the request's 'genuinely different
  obstruction' alternative.
```
