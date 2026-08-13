# Subbarao–Warren (1966), *Unitary perfect numbers*

Full text: [[subbarao-warren-1966-unitary-perfect.full]] (Canad. Math. Bull. 9 (1966) 147–153; OCR is poor).

**Setup.** `σ*(N) = Π (p_i^{a_i} + 1)` over `p_i^{a_i} || N` is multiplicative; `N` is unitary perfect iff `σ*(N) = 2N`. First four found: `6, 60, 90, 87360` (the fifth, in the authors' footnote, was overlooked in an earlier abstract of one of them).

**Establishments relevant here.**
- The paper begins the parity argument: it is easy to see no odd UPN exists, and Lemma 1 handles `N = 2n`; Lemma 2 the case `3 | N` (this is the ancestor of the run's 2-adic budget identity, which is proved cleanly in `research/notes/parity-and-2-adic-budget.md`).
- **Theorem 4 (finiteness in fixed `ω`):** there are at most finitely many UPNs with a fixed number of distinct prime factors. This is the reason the finiteness question is at bottom a question about how many distinct primes can occur — the direct ancestor of the run's `|H_even| ≤ 4^N` prime-case reduction and Wall 1988's `ω(odd) ≥ 9`.

**Consequence for this run.** Theorem 4 is the historical grounding for "rarity in a fixed `ω` is plausible, but growth of `ω` is open" — exactly the dichotomy GOAL.md warns about (rarity ≠ finiteness). The paper's Conjecture (`n > 87360 ⇒ no more`) is the original Subbarao–Warren conjecture this run attacks.

**Hypotheses.** Results are for UPNs generally; the first-four enumeration is historical and consistent with the run's re-derived five witnesses (`code/out/known_five_verified.captured.txt`).

```claim
id: sw1966-finiteness-fixed-omega
statement: There are at most finitely many unitary perfect numbers with a fixed
  number of distinct prime factors.
hypotheses: sigma* multiplicative; N unitary perfect iff sigma*(N) = 2N
holds-here: yes - a sixth UPN, if it exists, therefore has arbitrarily large
  omega, tying growth of omega(odd) to the finiteness question
status: proved in source (Theorem 4); not re-derived here
bearing: justifies that the open question reduces to whether omega(odd) can
  grow; the run's a >= 8 and Wall 1988's omega(odd) >= 9 are steps in that
  direction but do not bound omega above
anchor: research/sources/subbarao-warren-1966-unitary-perfect.full.md
contradicts: (none)
answers: whether-finiteness-reduces-to-omega-growth
```
