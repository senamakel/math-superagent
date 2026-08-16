# Verdict: sawin-above-barrier / liu-0-38271 / yu-record-0-38234 vs ahs-gilmer-conj

```thread
id: contradiction-sawin-ahs
question: Do Sawin's dependent-coupling improvement and its evaluations (Yu, Liu)
  genuinely contradict the AHS/Gilmer constant (3−√5)/2, or is that value a
  barrier only to the iid-coupling class?
status: resolved
rests-on: ahs-barrier, ahs-gilmer-conj, pebody-optimization, chaSe-lovett
blocked-by: none
next: none — the iid/dependent coupling split is settled; do not re-flag these as
  contradictions
```

## Verdict: RESOLVED — not a genuine contradiction, a misread of what (3−√5)/2 bounds

All three flags (`sawin-above-barrier`, `liu-0-38271`, `yu-record-0-38234` each
"contradicting" `ahs-gilmer-conj`) are **misreads**. The AHS result and the
Gilmer conjecture it verifies are statements about the **iid twin-pair coupling
class only**; (3−√5)/2 is the ceiling of that specific class, and dependent
couplings (Sawin → Yu/Cambie → Liu) escape it by construction. No two of these
claims can both be load-bearing in the same sentence only if one insists that
(3−√5)/2 is a barrier to the *method* — which every relevant source explicitly
denies.

## Precise reasoning

**What AHS/Gilmer establish, precisely.** `ahs-gilmer-conj` verifies the explicit
one-variable inequality conjectured by Gilmer that yields (3−√5)/2. `ahs-barrier`
states the value as the maximum of E[H(X∪X')]/E[H(X)] over the min-densities,
which is "a barrier to the *iid-twin* form of Gilmer's method, not to the
conjecture" (`ahs-barrier`, bearing). Its twin case X, X' are i.i.d. copies.

`pebody-optimization` makes the class precise:
> "The best constant obtainable by the iid-OR entropy inequality (with an
> auxiliary variable S) is (3−√5)/2, found as the optimum of a
> conditional-entropy problem." (given iid coupling of (X,S), H(X|S) fixed,
> E(X) fixed)

So (3−√5)/2 is the **optimum over the iid coupling class**. It is not claimed
— by AHS, Pebody, or anyone here — to be a ceiling on the entropy method. AHS
itself: "(3−√5)/2 … is a barrier to the *iid-twin* form … not to the conjecture."

**What Sawin does.** `sawin-above-barrier`: "A dependent-coupling refinement of
Gilmer's method obtains a constant strictly greater than (3−√5)/2," using a
convex combination of the iid coupling and a max-entropy *dependent* coupling.
This is a **different coupling class**. That was the point: the iid ceiling is
escapable, so the method is not capped.

**What Yu and Liu do.** `yu-record-0-38234`: evaluates Sawin's *dependent-coupling
bound* (dimension-free optimization, bounded auxiliary cardinality) to ≈0.38234.
`liu-0-38271`: a *conditionally-iid coupling* (i.i.d. given an auxiliary S)
reaches ≈0.38271. Both are dependent-coupling refinements, both `follows-from:
sawin-above-barrier`.

**Why no contradiction.** Two statements can only contradict if they make claims
about the same object. AHS's (3−√5)/2 is an upper bound on the iid class; Yu/Liu
are lower bounds (constants achieved) in a strictly larger dependent-coupling
class. An upper bound on a subset and a lower bound on a superset are
simultaneously true. The "contradiction" arises only from reading (3−√5)/2 as
"the best the entropy method can ever do," which no source states. The same
misreading is explicitly warned against in `sawin-improved-lower-bound-2022.md`:
"the iid barrier is escapable," and "Any 'barrier theorem' this run proves must
be stated precisely about the class of couplings it covers."

## The record, confirmed

- **Yu ≈ 0.38234** — PUBLISHED, proved, and the current **published record**:
  Lei Yu, "Dimension-Free Bounds for the Union-Closed Sets Conjecture", Entropy
  2023, 25(5). This is the computable form of Sawin's dependent-coupling bound
  (`published-record-c`).
- **Liu ≈ 0.38271** — **conditional** (under numerically-verified hypotheses on
  a 9-d optimization's optimizer structure), **unpublished** (preprint
  arXiv:2306.08824; appeared at CISS 2024 conference, not a journal). Do not
  cite it as the record (`preprint-status-c`, `liu-0-38271`).
- Cambie (arXiv:2212.12500, ≈0.3823455) independently reaches the ~0.38234
  value via the same dependent-coupling method but is also a **preprint**
  (`preprint-status-c`); it is the second independent route to Yu's value.

Single number to beat in print: **0.38234…** (Yu, Entropy 2023).

## Action for the ledger

These three "contradictions" should be dropped from the contradictions list. The
only row that legitimately remains is the numeric one — `daswu-record-0-3823455`
vs `liu-0-38271` — which is not a contradiction either, just a record-vs-
conditional-claim status distinction (Yu/Cambie 0.38234 proved, Liu 0.38271
conditional). No `contradicts` edge should point from the dependent-coupling
values to `ahs-gilmer-conj` or `ahs-barrier`.
