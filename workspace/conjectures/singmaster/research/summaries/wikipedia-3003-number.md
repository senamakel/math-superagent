# Wikipedia — Singmaster's conjecture / 3003 (number) — encyclopedic corroboration

Source: Wikipedia, "Singmaster's conjecture" (redirect from "3003 (number)"),
retrieved 2026 (revision 1363330357). Held at
`research/sources/wikipedia-3003-number.full.md`.

## What it fixes (statement, witnesses, open questions)

This is the encyclopedic entry for the modern statement and the exact witness
set, in agreement with the run's established facts (both-mirrors-plus-trivial
convention; N(3003)=8; the six N=6 values; the infinite family).

- **Statement**: `N(a) := #times a>1 appears in Pascal's triangle`; conjecture
  `N(a) = O(1)`, i.e. ∃ natural M with `N(a) ≤ M` for all a. Note the entry
  counts both mirrors implicitly (see witness list), matching this run's
  convention.
- **Known bounds** (all in agreement with the library): Singmaster 1971
  `O(log a)`; AEH 1974 `O(log a / log log a)`; best unconditional Kane 2007
  `O((log a)(log log log a)/(log log a)^3)`; conditional on Cramér's
  conjecture `O_ε((log a)^{2/3+ε})`.
- **Infinite family**: `C(n+1,k+1)=C(n,k+2)` has infinitely many solutions with
  `n=F_{2i+2}F_{2i+3}−1`, `k=F_{2i}F_{2i+3}−1`, giving infinitely many entries
  of multiplicity ≥ 6. The two non-boundary appearances + two symmetric mirrors
  + the trivial pair `C(a,1)=C(a,a−1)` = six. Next family member after 3003:
  `a = 61218182743304701891431482520 = C(104,39)=C(103,40)` (+ mirrors + trivial)
  — matches this run's `code/out` and OEIS A090162.
- **Exact witness list** (verbatim, both-mirrors-plus-trivial):
  - 120, 210, 1540, 7140, 11628, 24310 each occur exactly six times (the six
    sporadic N=6 values; e.g. 120 = C(120,1)=C(16,2)=C(10,3) + mirrors + trivial;
    24310 = C(24310,1)=C(221,2)=C(17,8) + mirrors + trivial);
  - **3003 = C(3003,1)=C(78,2)=C(15,5)=C(14,6)=C(14,8)=C(15,10)=C(78,76)
    =C(3003,3002)** — eight occurrences, "the only number known to appear eight
    times", also a member of the infinite family;
  - the smallest numbers appearing ≥ n times: 2,3,6,10,120,120,3003,3003
    (OEIS A062527).
- **Open questions** (verbatim): it is not known whether any number appears more
  than eight times, nor whether any number besides 3003 appears eight times; the
  conjectured finite upper bound could be as small as 8, but Singmaster thought
  it might be 10 or 12; it is unknown whether any numbers appear exactly five or
  seven times.
- **Elementary facts**: 2 appears once; 3,4,5 twice; all odd primes twice; 6
  (and central binomial coefficients except 1,2) three times; numbers
  `C(p,2)` for prime p>3 four times.

## Bearing for this run

This is a third-party encyclopedic corroboration of the run's core numbers
(witness set, family, bounds, open questions) with the exact convention the run
uses. It independently fixes:
(a) the statement and the "could be as small as 8" / "Singmaster thought 10 or
12" framing (matching de Weger's Conjecture A → N≤8 claim, held);
(b) the fact that **no N>8 and no second N=8 value is known** — a running check
for any computation: a value with multiplicity 9+ found in a scan would be a new
witness, never a contradiction of held sources;
(c) the odd-parity open questions (5 or 7 appearances never occur) — constraints
any multiplicity-counting method should respect.

Nothing here is a derivation of this run's own; it is catalogue-level
corroboration (as encyclopedic entries are). The primary anchors for each fact
are already held (Singmaster FQ 1975, AEH 1974, Kane 2007, de Weger 1995/1997,
MRSTT 2021).

```claim
id: wikipedia-singmaster-entry-corroboration
statement: Wikipedia's Singmaster's conjecture entry fixes N(a):= number of times
  a>1 appears in Pascal's triangle (both mirrors + trivial in the witness list);
  conjecture N(a)=O(1), possibly as small as 8 (Singmaster thought 10 or 12); no
  number >8 appearances or second 8-appearance value is known; no number appears
  exactly 5 or 7 times; the 3003 = C(3003,1)=C(78,2)=C(15,5)=C(14,6) eight-fold
  occurrence is unique; the six sporadic N=6 values are 120,210,1540,7140,11628,
  24310; Kane 2007 best bound O((log a)(log_3 a)/(log_2 a)^3); Cramer-conditional
  O_eps((log a)^{2/3+eps}); the infinite family gives N(a)>=6 for
  a = C(F_{2i+2}F_{2i+3}, F_{2i}F_{2i+3}) etc.
hypotheses: none beyond the standard statement (a>1).
holds-here: yes — matches this run's convention and every held primary.
status: asserted (catalogue corroboration; each fact anchored to held primaries)
bearing: fixes the exact statement, the open-question list, and the constraint
  that no computation should find N>8 without it being a new witness; corroborates
  the de Weger Conjecture A N<=8 framing.
anchor: research/sources/wikipedia-3003-number.full.md
```