# Shared context

**Problem in one line.** Erdős (1979): for `n > 8`, the base-3 expansion of `2^n`
contains a digit `2`; the only digit-2-free powers are `2^0=1`, `2^2=4=11_3`,
`2^8=256=100111_3`. Believed true, open since 1979. This workspace was cleared and
restarted deliberately: nothing in it is inherited, every claim starts unverified.
`GOAL.md` and `problem.md` are the authority; the deliverable is a partial result
(symbolic invariant, middle-digit constraint, subclass proof, sourced bound), not
the conjecture.

**Route this run is directed down.** 3-adic dynamics + a *symbolic invariant*
preserved by `x↦2x` on `Z_3` that the digit-`{0,1}` set `S` violates — not a bigger
sieve. The sieve is an instrument for the dynamics, never the deliverable.

## Established

**Caveat that governs this whole section.** The workspace ledger `CLAMS.md` is
empty (`search_claims` reports "No claims recorded yet"); `code/` has no programs
and `code/out/` has no captures. Everything below is **recalled from Cognee
durable memory of prior sessions of this same project**
(`conjectures_erdos_ternary_2n`) and corroborated here only by cheap hand
arithmetic. It is prior-work, not this-run-verified. The run must re-derive the
blocked items below (build the oracle, re-prove) before building on them.

- **SIEVE-EXACT — `|A_k| = 2^(k-1)` exactly for all k≥1** (proved by bijection in a
  prior session). `A_k = { r mod 2·3^(k-1) : low k ternary digits of 2^r mod 3^k
  avoid 2 }`. Proof: 2 is a primitive root mod `3^k` (order `φ(3^k)=2·3^(k-1)`),
  so `Φ_k: r ↦ 2^r mod 3^k` bijects the period onto the units; a unit's digit
  pattern avoids 2 iff low digit is 1 and the other k-1 digits are in {0,1} —
  exactly `2^(k-1)` patterns. Each class lifts to exactly 2 of 3 children; no
  class ever dies, none collide. **Hand check here: k=1 gives `A_1={0}`, |A_1|=1 =
  2^0` ✓.**
- **CONSEQUENCE — the modular sieve can NEVER close by counting** (proved). `|A_k|`
  grows like `2^k` while density `(1/2)(2/3)^(k-1) → 0`. A proof must show only
  finitely many *paths* survive, not that the count decays. Reframing: the orbit
  of 1 under `×2` in `Z_3^×` (closure = all of `Z_3^×`) meets the Cantor set `S`
  (digits in {0,1}) in exactly `{1,4,256}`.
- **Oracle verified** (prior session): `digit_free(1)=True, (4)=True, (256)=True`;
  `digit_free(2)=(8)=(32)=False` (`32=1012_3`, `64=2101_3` contain a 2). Witnesses
  `n=0,2,8` digit-free at every k=1..40.
- **Order facts** (verified k=1..40): order of 2 mod `3^k` = `2·3^(k-1)`;
  `v_3(2^(2·3^(k-2))-1) = k-1`, so `2^(2·3^(k-2)) ≡ 1 + 3^(k-1) mod 3^k` (LTE,
  c=1).

## Ruled out

- **Sieve-as-proof** — closed, with the reason: `|A_k|=2^(k-1)`, so counting
  residue classes never kills the digit-2-free set at any finite 3-adic precision.
  This is the starting obstruction in `problem.md`; the run must get past it, and
  re-sieving to larger k after it is not progress.
- **Density trap** — "density of digit-2-free integers → 0" is true and irrelevant;
  it says nothing about the thin sequence `2^n`. Never recorded as a proof.
- **Probabilistic heuristic** `(2/3)^k` — explains why the conjecture is believed;
  proves nothing. Never recorded as a proof.

## Numbers

- `|A_k| = 2^(k-1)`: 1, 2, 4, 8, …, verified to k=26 in prior sessions (direct
  sieve to k=12, lift-count to k=11, order/LTE/witnesses to k=40).
- Literal count of `2`s in `2^n` base 3 (OEIS A260683, sourced): starts
  `0,1,0,2,1,1,1,2,0,4,2,4,…` — value 0 exactly at n=0,2,8.
- Verification bounds in the library (sourced, NOT reproduced here): Gupta 1978
  `n<4374`; Vardi 1991 `n≤2·3^20≈7·10^9`; Saye 2022 `n≤2·3^45≈5.9·10^21`
  (digit-2 AND digit-0 conjectures; Θ(2^K) recursive trailing-digit construction,
  not Θ(3^K) naive).

## Recalled

Marked recalled from Cognee; hypotheses are this exact problem so they hold, but
each needs a primary source re-fetched in this workspace.

- **Narkiewicz (1980):** `#{n≤X : (2^n)_3 omits 2} ≤ 1.62·X^(log_3 2)`, `log_3 2 ≈
  0.63092`. Method: 2 primitive mod `3^k`, only `2^(k-1)` of `2·3^(k-1)` residues
  omit 2. Source noted: Lagarias math/0512006.
- **Dimitrov–Howe (2021, arXiv:2105.06440; Rocky Mountain J. Math):** outside
  `{0,2,8}`, base-3 expansion of `2^x` contains a digit 2 **or ≥ 26 ones**. So any
  counterexample must have `≥26` ones and zero 2s. Residual open case exactly
  "≥26 ones and no 2s". Improving the 26 is the DH-frontier, needing their
  nested-moduli/determinate-power-lifting method handled for larger sums of
  distinct powers of 3.
- **Kaneko–Stoll (2018):** patterns of 0/1 digits are abundant in the exponent
  set — powers of 2 with prescribed ternary trailing patterns exist in a positive
  proportion of n. Shows digit-0/1 patterns alone never run out; reinforces that
  the kill must come from middle/high coupling.
- **Middle digits (Lagarias 2009 §1.6):** combining real top-digit and 3-adic
  bottom-digit control to reach the ~`log_3 2 · n` middle digits is **open**;
  whether high and low digits are "uncorrelated" in a quantifiable way is
  unresolved. The low digits are what the sieve reaches, the high digits what size
  arguments reach; nobody touches the middle. This is the target.

## Contradictions

- **`|A_k| = 2^k` vs `2^(k-1)` — memory disagrees with itself.** A passing earlier
  memory reports the raw oracle giving `2^k` (1,2,4,…,128 at k=8) and calls that
  "the counting obstruction `|A_k|` grows like `2^k`"; the later durable SIEVE-EXACT
  record proves `2^(k-1)`. Hand check at k=1 (only r=0 works) forces `2^(k-1)`, so
  `2^k` is the wrong earlier value. Worth one cheap re-verification in this run;
  record the resolution rather than re-opening it.
- Saye's "n≤2·3^45" and Dimitrov–Howe's "≥26 ones" are both from recalled memory;
  treat as sourced-but-needs-primary until re-fetched. Neither is this-run-verified.

## Gaps

- **Rebuild the oracle in THIS workspace** (per GOAL.md): `digit_free(m)` exact;
  `sieve(k)` working mod `3^k` only, never materialising `2^n`; falsification
  oracle = every claimed obstruction must pass `n=0,2,8`. Verify digit_free by hand
  on the three witnesses + a known-`2` value before trusting it.
- **Re-prove `|A_k|=2^(k-1)` here** (stated cheap-and-once in GOAL.md), then move
  past it.
- **The middle-digit coupling** is the live open piece: a symbolic invariant,
  weight/carry/transducer statistic on the base-2→base-3 conversion, or an
  automaton-invariance argument that the {0,1}-digit set `S` violates but `x↦2x`
  preserves — checked against n=0,2,8. Improving DH's 26, or any middle-digit
  constraint, also counts.
- No primary source is yet downloaded in this workspace except Saye-2022 (full text
  present) — fetch-and-digest Dimitrov–Howe, Narkiewicz, Kaneko–Stoll, Lagarias as
  claims are built on them.
