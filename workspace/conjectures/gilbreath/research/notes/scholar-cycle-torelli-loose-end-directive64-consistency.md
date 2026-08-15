# Scholar cycle — Directive-64 material consistent; one genuine loose end found

**Role / source:** scholar, adversarial re-digest of the `research/` library after
the research agent finished. The genuinely-new material this cycle is the three
items already filed in `scholar-cycle-new-material-directive64-measured.md`
(`dyadic-oddfactor-infimum-bounded`, `gap-size-hypotheses-do-not-separate`,
`switch-conservation-identity`). This cycle verified each against its captures,
the claims ledger, and durable memory; all three are consistent and correctly
filed. One genuine incompleteness surfaced that is not recorded anywhere: the
order-vs-marginal discriminator was never tested.

## The three new items — verified consistent, claim blocks present

1. **`dyadic-oddfactor-infimum-bounded`** (checked). Exact-int infima for
   P=3,5,7,9,15 (0.6471/0.5088/0.2667/0.3592/0.1143, argmin n<=114, residual
   nu2−c·n O(1) to n=24000, no late low past n=1000) confirm the dyadic
   dichotomy's odd-factor half numerically on the periodic families and do NOT
   refute the odd-factor converse by a plateau — but it stays CONJECTURED and
   does not close G-supply. The SCOPE OVER-REACH flag in the prior note stands:
   the measurement is exact periodic words (N₀=0, P<=15), strictly smaller than
   the eventually-periodic-with-preperiod case the proved collapse theorem
   handles; no measurement covers nonzero preperiod or unbounded P. In durable
   memory (stored this cycle).
2. **`gap-size-hypotheses-do-not-separate`** (checked). None of the three
   gap-size statistics separates the primes from the {2..20} families; where
   they differ the primes have the HEAVIER tail (max 86 vs 20), the wrong
   direction. Deaths are startup (k<=10). The data points to order/autocorr, not
   the marginal; primes satisfy the proved Torelli g_n<=n, iid {2..20} violates
   it in the death window. In durable memory (stored this cycle).
3. **`switch-conservation-identity`** (proved, pure counting):
   N_switch(x)+N_nonswitch(x)=pi(x)−1; G-supply is exactly equivalent to a
   below-density-1 UPPER bound on equal-residue pairs, which explains why the
   Ruzsa/Shiu/Martin LOWER bounds on the non-switch side give nothing. Already
   in durable memory (re-stored this cycle). Confirms
   `abgs-2011-s9-mod4-switch-limit-open`, reframes, does not close.

## The genuine loose end (not previously recorded anywhere)

**The order/autocorrelation discriminator was never tested.** The
`gap-hypothesis-separation-finding.md` note says "Corrective control in flight:
`torelli_conditioned_control.py`" — four controls: (1) {2..20} iid conditioned
on g_n<=n; (2) {2,4,6} same; (3) iid-with-replacement from the ACTUAL prime-gap
multiset (destroys only order, keeps the exact marginal); (4) same multiset
conditioned on g_n<=n. The prediction: if order is the discriminator, control
(3) dies while the primes live. **`code/gap_hyp/` holds only
`gap_hypothesis_separation.py` — the control was never written.** The note
describes it, durable memory describes it as "in flight", but there is no code,
no capture, and no result on disk; no task row tracks it. This is the one open
thread this cycle's material leaves dangling. It is directly relevant to the
successor of the dead `find-weakest-gap-variety-hypothesis` thread: the marginal
is closed (wrong direction), so the order half is the only place the sweep-death
question can still answer. Filed as scratch (durable memory this cycle).

## Sources that do not help (no re-read)

- The five prior scholar-cycle notes and the twelve librarian closure audits
  (cycles 3–12) all verify the same closed library; no re-digest warranted.
- The corpus holds no source that upper-bounds equal-residue consecutive-pair
  count below density 1 (which is exactly what G-supply needs); consistent with
  the named-open `abgs-2011-s9-mod4-switch-limit-open`. No contradiction with
  recalled memory in any of the three new items.

## What the run still lacks (unchanged, plus the loose end)

A proof or unconditional bound of `nu2 >= c*n` remains the entire open content
of Route B (the named-open two-point mod-4 switch-frequency hypothesis).
Everything else is proved, machine-checked, or a recorded refutation. The
working item this cycle adds: run the four-control order/marginal test
(`torelli_conditioned_control.py`) — the prediction is that killing only the
order (multiset resampling, control 3) restores the deaths while the primes
survive.

## Contradictions

None. All three new claims confirm rather than contradict recalled memory and
the existing ledger (which retains only the documented intended contradictions:
`odlyzko-block-lemma-asserted` vs `-exact`, `caldwell-proth-myth` vs retraction,
`g-supply-transfer` vs `-universal-refuted`, `rule90-periodic-window-collapse`
vs `-refuted`, `lemma54-lean...` vs stale thread text).
