# Eliahou 1993 — exact cycle-length formula (primary statement via catalog)

<!-- src: S. Eliahou, "The 3x+1 problem: new lower bounds on nontrivial cycle lengths", Discrete Math. 118 (1993) 45–56, DOI 10.1016/0012-365X(93)90052-U; exact statement via MaRDI/zbMATH catalog entry (portal.mardi4nfdi.de/wiki/Item:Q685592) and UNIGE archive abstract (archive-ouverte.unige.ch/unige:12087) -->

Full text: **not held** (Elsevier paywall). The UNIGE record is at
`research/summaries/eliahou-cycle-lengths.md`; the exact theorem statement is
captured here from the MaRDI catalog entry (which reproduces the zbMATH
review's statement of the paper).

## What the source establishes

**Theorem (Eliahou 1993).** For the map T with T(n) = n/2 if n is even and
T(n) = (3n+1)/2 if n is odd, any **non-trivial cycle Ω** of T with
**Min Ω > 2^40** satisfies

    Card Ω = 301,994·a + 17,087,915·b + 85,137,581·c

where a, b, c are nonnegative integers, **b > 0**, and **ac = 0** (at most one
of a, c is nonzero).

The smallest admissible values for Card Ω are therefore 17,087,915;
17,389,909; 17,691,903; ...

**Method:** classical continued fractions giving a sharp **one-sided**
Diophantine approximation of log₂(3).

**The abstract (UNIGE):** "any nontrivial cyclic orbit under iteration of T
must contain at least 17 087 915 elements."

## What it implies for this run

- The hypothesis Min Ω > 2^40 is **satisfied** by any non-trivial cycle under
  the Barina verification bound (all n < 2^71 verified, so a non-trivial
  cycle would have minimum > 2^71 > 2^40). Hence the formula applies
  unconditionally to any non-trivial cycle consistent with current
  verification.
- The 10,439,860,591 period bound in `lagarias-W2` is the version of this
  formula combined with the then-verification bound; Barina's
  355,504,839,929 (`barina-cycle-length-355b`) is the current version.
- The one-sided Diophantine approximation of log₂(3) is the same lever as the
  `zudilin-mu-8616` irrationality measure — the two sources are the two sides
  of the same coin.

## Claims

```claim
id: eliahou-cycle-formula-exact
statement: For the map T (T(n)=n/2 even, T(n)=(3n+1)/2 odd), any non-trivial cycle Ω with Min Ω > 2^40 satisfies Card Ω = 301994·a + 17087915·b + 85137581·c for nonnegative integers a,b,c with b > 0 and ac = 0; the smallest admissible cycle lengths are 17,087,915; 17,389,909; 17,691,903; ... (Eliahou 1993).
hypotheses: Ω is a non-trivial cycle of T; Min Ω > 2^40
holds-here: yes — Barina's verification bound 2^71 implies any non-trivial cycle has Min Ω > 2^40, so the formula applies
status: asserted
bearing: the exact cycle-length formula behind lagarias-W2 and barina-cycle-length-355b
anchor: research/summaries/eliahou-cycle-lengths.md
```

```claim
id: eliahou-method-one-sided-cf
statement: Eliahou's proof uses classical continued fractions to obtain a sharp one-sided Diophantine approximation of log_2(3) (Eliahou 1993, via MaRDI/zbMATH review).
hypotheses: none
holds-here: yes — identifies the method that converts cycle shapes into cycle-length bounds
status: asserted
bearing: the Diophantine-approximation lever, dual to zudilin-mu-8616
anchor: research/summaries/eliahou-cycle-lengths.md
```
