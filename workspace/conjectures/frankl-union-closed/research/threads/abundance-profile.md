# Abundance profile of a minimal counterexample

```thread
id: abundance-profile
question: What must the abundance profile (the exact integer vector of per-element
  membership counts) of a minimal counterexample to UC look like, and can the
  conditionally-iid coupling optimization (attack-coupling-half) constrain that
  profile enough to force an abundant element?
status: open
rests-on: ahs-barrier, liu-conditionally-iid, yu-record-0-38234, eil-small-sets
blocked-by: none
next: compute exact abundance profiles with the canonical oracle code/lib/uc.py;
  state one structural claim about a minimal counterexample's profile, then
  attack it (SAT for finite existence questions) before trusting it
```

## Why this direction

Started by operator directive: the counting sequence of union-closed families
(3, 13, 121, 4959, 2771103, … = OEIS A102896) is out of scope — a recurrence
for the count says nothing about whether an abundant element exists. The effort
belongs on the **abundance profile** instead: the exact integer vector
`(|{A∈F : x∈A}|)_{x∈[n]}`.

The profile is where the entropy-coupling bound lands: the coupling inequality
says that if every coordinate density is `< 1/2`, then `H(A∨B) > H(A)`, which
contradicts union-closure. So a candidate counterexample is exactly a profile
whose maximum density is `< 1/2`, and the live question is whether the
coupling-class inequality (Yu/Liu finite-dimensional optimization, being
implemented in task `attack-coupling-half`) excludes that profile.

## What would falsify it

A union-closed family whose maximum density is `< 1/2` and for which the
conditionally-iid coupling inequality is *satisfied* (i.e. the coupling bound
does not reach `1/2`) would show the profile is not constrained enough by this
coupling class alone — the extremal `μ` blocking `c=1/2` would then be the
deliverable barrier rather than UC.
