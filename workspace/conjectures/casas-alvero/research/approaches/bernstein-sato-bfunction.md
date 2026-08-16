# Bernstein–Sato b-function as the multiplicity multiset invariant (refuted)

```approach
idea: For univariate f with root multiplicities m_1,…,m_r the Bernstein–Sato
       polynomial is b_f(s) = ∏_j ∏_{k=1}^{m_j}(s + k/m_j), so b_f IS the
       multiplicity multiset and "pure power" ⟺ b_f(s) = ∏_{k=1}^n(s+k/n). The
       CA hypothesis is to become constraints on the local/ideal b-functions of
       (f, f^{(i)}) that force the multiset to {n}.
mechanism: b_f records multiplicities; ideal b-functions of (f, f^{(i)}) detect
       common roots; aggregating over i is conjectured to force collapse.
status: refuted
killed-by: no load-bearing inference. b_f records only the multiplicity
       multiset — an invariant CA's hypothesis does not directly constrain
       (CA constrains which roots are SHARED with derivatives, not the
       multiplicities of f's roots). The bridge, "the ideal b-functions of
       (f, f^{(i)}) aggregate to force the multiset to {n}", has no known
       theorem behind it and no proposed mechanism; the proposal itself admits
       the factorization "is not known". The one-variable ideal (f, f^{(i)}) is
       a zero-dimensional complete intersection whose b-function is a standard
       local object attached to the shared-root set — there is no known
       aggregation relation over i = 1..n−1. A reformulation whose only
       established content (b_f = multiplicity data) is already fully known, and
       whose entire force is a conjecture about a conjecture, is not an attack.
precedent: _unchecked_
charp-break: Bernstein–Sato theory does not exist in char p (stated; the break is
       structural, which is the one part of the proposal that was right, but a
       clean char-p break does not rescue an inference that is absent in char 0).
```

## Why it closed

The char-0-only nature of the object was genuinely attractive: every admissible
CA argument must use characteristic 0 somewhere, and Bernstein–Sato theory is
about as characteristic-0 as an object gets. But the proposal confuses *having
a char-0 invariant* with *having an inference*:

- **`b_f` is the answer, not the engine.** It equals the multiplicity multiset
  exactly. The CA hypothesis does not speak to the multiplicity multiset of `f`
  directly; it speaks to which of `f`'s roots are also roots of `f^{(i)}`. So
  the reformulation starts from data the hypothesis never mentions and needs a
  new bridge to reach the hypothesis at all.
- **The bridge is unsupported.** No source, classical or modern, gives a
  factorization or divisibility relation between `b_f` and the ideal
  b-functions of `(f, f^{(i)})` that would collapse the multiset under the
  shared-root conditions. The proposal's own "Status of the parts" says the
  aggregation "is not already known". A load-bearing bet that is *entirely*
  speculative, with no named theorem whose hypotheses it instantiates, is not
  adoptable — it is a restatement plus a wish.
- **First step is a survey, not an attack.** "Source the exact statement of
  ideal b-functions" is phase-1 gathering; it would confirm the classical parts
  (which are not in doubt) and leave the actual bet untouched.

The correct move, if the multiplicity multiset is wanted, is the run's existing
and sourced handle on multiplicities (Laterveer–Ounaïes multiplicity constraints;
Polstra convex-hull), not a D-module invariant that adds no constraint on top of
them.
