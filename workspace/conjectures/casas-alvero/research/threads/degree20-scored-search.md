# Thread: degree-20 scored search — score distribution across construction families

```thread
question: Across genuinely different degree-20 construction families (binomials,
      trinomials, root-multiset, f=(x-r)^m g, cyclotomic/Chebyshev), what is the
      distribution of the first-failing derivative index j, and is the plateau at
      score 18 a binomial-family fact or a general degree-20 obstruction?
status: open
rests-on: binomial-plateau-finding (to be recorded, directive 11), laterveer-ounaies
      minimal-counterexample constraints (sourced)
next: Record the binomial plateau mechanism as a binomial-only fact; then diversify
      constructions (directive 11 step 1) and report first-failing j across
      families (step 2); guard: any non-binomial score 19 is a scorer bug (step 3).
```

## Findings

1. **The binomial plateau is a one-index mechanism.** For f = x^20 - c*x^k, every
   derivative j = k+1..19 is a scalar monomial times x^(20-j), so it shares root 0
   with f; the ONLY failing derivative is j = k itself. Hence score = 18 = 19 - 1
   and the binding constraint is always the single index j = k. This is a fact
   about BINOMIALS, not about degree-20 polynomials in general. (Directive 11; to
   be recorded as a claim with a falsifier, task record-binomial-plateau-finding.)

2. **The scorer's rejection path is untested by the live population.** 21 scored
   binomial candidates, 0 rejected. The 6-case smoke test exercises the rejection
   paths, but no live candidate did — so the scorer's power to constrain the
   population is not yet demonstrated (task scorer-rejection-check).

## Remaining

The first-failing-j distribution across families is the deliverable. If every
family fails at a structurally analogous index, that is the obstruction statement
and the closest this search gets to the conjecture. The search must change the
CONSTRUCTION, not the exponent — a population that is one family re-parameterised
is not a search.
