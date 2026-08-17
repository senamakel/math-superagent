# Combine the held minimal-counterexample constraints — verdict

<!-- regenerator-trigger -->

What ran: `python3 code/out/combine_constraints.py` (exit 0), capture
`code/out/combine_constraints.captured.txt`. Oracle: `lib.uc.decide_union_closed`,
`lib.uc.abundance`, `lib.uc.abundant_elements` — exact integer counts, no floats.
Range: n=1..4 exhaustive — ALL nonempty subfamilies of [n], i.e. 2^(2^n) − 1
each (65,535 at n=4; 65,808 families total). UC guard A102896 = 3,13,121,4959
and empty-free guard 1,6,60,2479 both PASS. Abundance convention: 2*c >= m
(≥ half).

The five held constraints are ESTABLISHED claims in the store, cited not
re-derived: (A) `kpt-thm5-counterexample-corollary` (proved; empty-free), (B)
`karpas-large-families` (proved), (C) `verified-m-small` (proved; n_ground ≥ 13,
m ≥ 51), (D) `no-degree-1-element-in-minimal-counterexample`
(verified-computational n≤4), (E) `rarest-count-floor` (proved for ALL families,
union-closure-free) and its tightness `gnm-envelope-rarest-floor-tight`.

```claim
id: cc-no-abundance-without-closure-on-4
statement: Over ALL 32,767 nonempty empty-free subfamilies of [4] there exist
  exactly 74 NON-union-closed families satisfying the arithmetic
  counterexample constraints (A) n_max >= 2*k_min + 1, (D) no degree-1 element
  (every present element occurs in >= 2 sets), (B) m < 2^{n_ground-1}, with NO
  abundant element (2*c_x < m for every element x) — distribution by
  (n_ground,m): (4,5):13, (4,7):61; canonical witness
  F = {{a},{ab},{c},{d},{bcd}} (masks 1,3,4,8,14; m=5, n_ground=4, k_min=1,
  n_max=3, counts (2,2,2,2), abundant []), oracle-confirmed not union-closed
  ({a} u {c} missing). Hence the held arithmetic constraints (A),(B),(D) MINUS
  union-closure do NOT force abundance: union-closure is the hypothesis doing
  the work, and the claim "these constraints force abundance" is FALSE on [4].
  Joint consistency: (A)&(D) are satisfied by 1,823 empty-free UNION-CLOSED
  families on [4] that are NOT counterexamples (example {{ab},{c},{abc}},
  masks 3,4,7, counts (2,2,2,0), abundant [0,1,2]), so the constraints neither
  force a contradiction nor force a counterexample. Pure-count minimum: the
  smallest n_ground admitting ANY family with n_ground present elements,
  m < 2^{n_ground-1} and no abundant element is n_ground=3 ({{a},{b},{c}},
  m=3 < 4, counts (1,1,1)); none exists at n_ground<=2 (m<2^{n-1} forces m=1
  there, and one set makes every present element abundant).
hypotheses: F a family (set of bitmasks) of subsets of [4] in the empty-free
  convention (0 not in F); k_min = min set size, n_max = max set size over the
  members, n_ground = |union F|, m = |F|; abundance = 2*c >= m (>= half);
  (E)-floor = m - 2^{n_ground-1}. Constraints (A),(B),(D) come from the held
  claims kpt-thm5-counterexample-corollary / karpas-large-families /
  no-degree-1-element-in-minimal-counterexample and are taken as arithmetic
  conditions only here; union-closure is NOT imposed on the hunted families.
  The pure-count minimum does NOT assume empty-free (an empty-containing
  witness {empty,{a},{b,c}}, masks 0,1,6, also attains n_ground=3: m=3 < 4,
  counts (1,1,1), no abundant).
holds-here: yes (unconditionally — exhaustive enumeration, 0 exceptions)
status: verified-computational, EXHAUSTIVE on [4] (all 2^16 subfamilies through
  the canonical oracle lib.uc). Ceiling: the same hunt on n_ground=5 means
  2^32 subfamilies (the enumeration ceiling) and is NOT pushed — the [4]
  verdict already settles the claim (a witness EXISTS), and a larger run would
  only add witness statistics, not change the boolean outcome.
bearing: the negative control for the combined-constraint claim: the arithmetic
  envelope (A),(B),(D) is not sufficient — union-closure is indispensable (as
  expected from GOAL.md control #2 "union-closure must be used"). It also
  confirms the vacuity observation: (E) is vacuous exactly on the
  counterexample regime. Over all 65,808 families on n=1..4, 25,695 lie in the
  Karpas regime (B), and 0 of them have (E)-floor m - 2^{n_ground-1} >= 0 —
  (B) forces the floor negative, so the rarest-count-floor lower bound does
  all its work only where counterexamples cannot live. No UC family on n<=4 is
  a counterexample (0 found), consistent with the verified floor and
  Bosnjak-Markovic n<=11. Next step worth a larger run: the UC-side
  extrapolation of (D) to n=5 (2,771,103 UC families per A102896, reachable by
  the existing g_nm cascade), extending the no-degree-1 verified floor.
anchor: code/out/combine_constraints.py, code/out/combine_constraints.captured.txt,
  code/out/combine_constraints_crosscheck.py (independent second route:
  combinations-based enumeration, oracle still lib.uc; re-derived the 74
  witnesses, the (n_ground,m) distribution, the canonical witness, the
  pure-count minimum n_ground=3 — including the empty-containing witness
  {empty,{a},{b,c}} masks 0,1,6 with m=3 < 4, counts (1,1,1) — and the
  (E)-vacuity 0/25695; CROSSCHECK PASS)
follows-from: kpt-thm5-counterexample-corollary, karpas-large-families,
  verified-m-small, no-degree-1-element-in-minimal-counterexample,
  rarest-count-floor
```

## The combined structural claim, stated once

A counterexample F to union-closed sets (empty-free convention, k = k_min, N =
n_max, n = n_ground, m = |F|) must satisfy, simultaneously:

- (A) N >= 2k + 1 — ratio of largest to smallest member set at least 2 (KPT Thm 5(3) corollary),
- (B) m < 2^{n−1} — the Karpas small-family regime,
- (C) m >= 4n − 1 with n >= 13, in particular m >= 51 (Roberts–Simpson / Hu; the Živković–Vučković n≥13 floor),
- (D) every element in at least 2 sets (no degree-1),
- (E) count_x >= m − 2^{n−1} for all x — **vacuous under (B)**, since (B) makes the floor negative; numerically: 0 of 25,695 families in the (B) regime have floor ≥ 0.

The hunt attacks the claim "these five constraints force abundance". Verdict: on
[4], the arithmetic part (A),(B),(D) alone admits 74 abundant-free
non-union-closed families, so the constraints do not force abundance without
closure; and no UC family on n≤4 is a counterexample, so union-closure is
precisely the hypothesis that closes the gap on the verified floor. This does
not prove UC (and nothing here claims it); it locates where union-closure must
do its work.

## One-line statement of what a larger run would settle

Pushing the NON-UC hunt to n_ground=5 (2^32 subfamilies = enumeration ceiling)
would add witness statistics only — the [4] verdict already settles the claim
(a witness exists, so the constraints minus closure do not force abundance);
the ceiling worth pushing is the UC-side no-degree-1 floor to n=5 (2,771,103
UC families, reachable by the existing cascade).

## Booleans (all exact, from the capture)

| question | outcome |
| --- | --- |
| UC guard A102896 (3,13,121,4959) | PASS |
| empty-free UC guard (1,6,60,2479) | PASS |
| oracle guards (powerset 1/2, singleton, antichain) | PASS |
| UC counterexample on n≤4 | 0 (UC holds there) |
| (E) violated over all 65,808 families | 0 (matches proved claim) |
| (B)-regime families with (E)-floor ≥ 0 | 0 — (E) is vacuous on the counterexample regime |
| non-UC witnesses to the hunt on [4] | 74 (of 32,767 empty-free) |
| (A)&(D) jointly satisfied by UC non-counterexamples on [4] | 1,823 (example given) |
| pure-count min n_ground (m<2^{n−1}, no abundant) | 3 (witness {{a},{b},{c}}) |

## Operational note

Constraint (C) (m >= 4n − 1, n >= 13) is recorded as vacuous on n<=4 — it
needs n_ground >= 13, unreachable here; its consistency with (A),(B),(D) is
therefore not exercised on [4], which is stated rather than hidden. The claims
ledger is not writeable by this role; the claim block above, with the
`<!-- regenerator-trigger -->` marker, is how the runtime files it (filed:
the claim is present in `derived/CLAIMS.md` and `search_claims`).

Cognee memory was unhealthy when this pass finished: `remember_memory` and
`note_scratch` were both rejected ("the memory server cannot index right
now ... would be accepted and dropped"). The executed result therefore lives
in this file, in `code/out/combine_constraints.captured.txt`, and in
`derived/CLAIMS.md` — NOT in Cognee. A later run that queries memory for
"combined counterexample constraints / cc-no-abundance-without-closure-on-4"
and finds nothing should read this note and the capture rather than
re-deriving (same failure mode and remedy as constraint_delim_claims.md).