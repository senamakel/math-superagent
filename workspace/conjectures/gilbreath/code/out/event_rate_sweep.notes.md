# Event-rate sweep over the 2-then-odds class: step law universal, regeneration fails on most random sequences

Run: `timeout 540 python3 code/event_rate/event_rate_sweep.py` → `code/out/event_rate_sweep.captured.txt`
Analysis: `python3 code/event_rate/analyze_sweep.py` → `code/out/event_rate_sweep_analysis.captured.txt`
Stats: `code/out/event_rate_stats.jsonl` (persisted before reporting)

## What was measured

1154 sequences in the general Gilbreath-like class `A_0 = (2, 3, 3 + cumsum(even gaps))`
(gaps i.i.d. per family: `{2}` consecutive; `{2,4}`; skewed `{2,4,6}`;
skewed `{2,4,6,8,10}`; uniform `{2..6}`, `{2..10}`, `{2..20}`, `{2..50}`, `{2..100}`;
geometric with p = 0.5, 0.25, 0.125, 0.0625; each family with and without the first gap
forced to 2 — the primes have first gap 2), across 3 batches:
sweep D=600/W=200k ×48 seeds, deep D=1200/W=400k ×10 seeds, long D=4000/W=2M ×4 seeds.
26 workers of 28 CPUs, wall 278.4 s, all row arithmetic exact int64, two rows held at a time.

## Results

**1. Step law and recharge identity: universal.** Over all 1154 sequences,
46,528 eligible rows, 20,013 (2,4)-regeneration events, the step law
(`b_{k+1} ≥ b_k ⟺ (e,c) = (2,4)`, else `b_{k+1} = b_k − 1`) and the recharge
identity fail **zero** times — same exact accounting as the prime rows
(depth 1000). The step law is a theorem for all nonneg sequences and holds
as measured.

**2. Regeneration is NOT generic in the random class: 852/1154 (73.8%)
sequences hit `b_k = 0` before their batch depth; all deaths occur within the
first 10 rows, 89.7% within the first 3.** The block is destroyed in the
startup transient (rows 1–3) or not at all: no sequence in the class that
survived row 10 ever died out to 4000 rows of the long batch. Long-run
regeneration failure was not observed; the class failure is a startup effect.

**3. `first gap = 2` is the single decisive (and sufficient for the small-gap
families) startup condition.** Forcing the first gap to 2 converts every
family with support ⊆ {2,4} (consecutive: 0/48 × 3 batches died, f2-rand24:
0/48) from majority-`rand24` death (62%, k ≤ 1) to 100% survival over the full
batch depth — even for the long D=4000 batch. f2-skew246 death drops 65%→29%
(sweep). The primes have first gap 2, so the prime row starts with the
regenerative `(2,4)` event.

**4. Healthy-class regeneration: exact local (2,4) mechanism with
`rho_live ≥ 0.318`, `min_b ≥ 1` (240 non-degenerate survivors), i.e.
regeneration events never let the block length fall below 1 in these
sequences, matching the prime rows (min b = 2).**

**5. Oracle:** 4 independent numpy-vs-pure-Python cross-checks all match on
events, eligible, min_b, first_b0, step/recharge failures, densities.
`witnesses.json` prime row: 60 regeneration events (block data).

## What this settles, exactly (bounded claims)

- Proved-not-refuted: the step law + recharge identity (the bookkeeping that
  reduces the conjecture to an event-rate inequality) hold on every one of the
  1154 random sequences measured — same as on the primes.
- Verified-numerically (not proved): "first gap 2 + small gap support ⟹ never
  reaches b=0" to depth 600–4000, family-dependent, seeds ≤ 48.
- Verified-numerically: any sequence in this class surviving 10 rows survives
  the full batch (852 died, all k ≤ 10; 302 survived all to batch depth).
- **What it does NOT say:** nothing about all k for the primes. In particular
  it gives no regeneration-rate lower bound for infinitely many rows, so it
  does not resolve the open question (`k` with `b_k = 0`).

## Note against the general-class strategy

The directive/GOAL.md hopes for "2 followed by odd numbers with gaps bounded
by g" as a settled class; this sweep shows that class **fails** unless the
first gap is 2 (and even with it, uniform{2..20}/geometric-p=0.25 die
immediately — the primes' gap profile 2,2,4,2,4,2,4,6,2,... is far from
uniform). Eppstein's anti-Gilbreath construction already refuted the
bounded-gap class; the data localises the failure to the startup rows and to
the first gap in particular. A general-class theorem must include the "first
gap = 2" hypothesis and something like the small-support skew; that is the
carved-down class this run's data supports. The primes satisfy both.

```claim
id: event-rate-sweep-step-law-universal
statement: Over 1154 random 2-then-odds sequences (D up to 4000, W up to 2e6; gap families consecutive/{2,4}/skew{2,4,6}/skew{2,4,6,8,10}/uniform{2..2g}/geometric, with and without first gap forced to 2), the step law (b_{k+1} >= b_k iff (e_k,c_k) = (2,4), else b_{k+1} = b_k - 1) and the recharge identity fail zero times (46528 eligible rows, 20013 events).
hypotheses: A_0 = (2,3,3+cumsum(even gaps)); b_k = leading {0,2} length; measurement stops at the first row with b_k = 0 (or batch depth); numpy int64 exact.
holds-here: yes (the primes are in the class with first gap 2)
status: computed and checked, step-law validity for all nonneg sequences is proved elsewhere (code/event_rate/event_rate_sweep.py docstring; matching evidence on prime rows to depth 1000)
anchor: code/out/event_rate_sweep.captured.txt
```

```claim
id: event-rate-sweep-regeneration-not-generic
statement: In the random 2-then-odds class, 852/1154 (73.8%) sequences reach b_k = 0 within their batch depth, all deaths within the first 10 rows and 89.7% within the first 3; sequences surviving row 10 survived the full batch (up to D=4000). Forcing the first gap to 2 turns the {2,4}-support families from majority-death (62% for rand24, k<=1) to 100%-survival (0/48 per batch, all three batches incl. D=4000); death fractions grow monotonically with gap-support width.
hypotheses: same class as event-rate-sweep-step-law-universal; survival = never hitting b_k = 0 up to batch depth (600/1200/4000); 48/10/4 seeds per family per batch.
holds-here: no — the primes (first gap 2, small skewed gaps) sit in the surviving minority; the class as a whole refutes the naive bounded-gap generalisation
status: computed and checked (bounds above); not proved
anchor: code/out/event_rate_sweep_analysis.captured.txt
```

```claim
id: first-gap-2-startup-sufficiency-supported
statement: For the 2-then-odds class with gap support {2,4} (consecutive and rand24), forcing gap[0] = 2 gives 0 sequences reaching b_k = 0 among 62 measured (48 sweep + 10 deep + 4 long) to depth up to 4000, versus 62% deaths at k <= 1 without it; within the class, all observed b_k = 0 deaths happen in the first 10 rows.
hypotheses: families consecutive and rand24, seeds as above, widths W = 2e5..2e6.
holds-here: yes for the primes (first gap is 2, gaps are small and skewed), but the statement's scope is the measured class, not any theorem for all k
status: computed and checked (bound: depth 4000, 62 seeds); unproved
anchor: code/out/event_rate_sweep_analysis.captured.txt
```