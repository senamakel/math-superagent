# Pattern-finder report — round 32: second-subconstituent nullity at μ=2

## What this round found

Completed interrupted work: the `pattern_subconstituent_spectrum*`,
`pattern_nullity_*`, `pattern_kernel_*`, `pattern_h_parameters*` files
(timestamps 07:19–07:47) had **no captures and no report**. This round
re-derived and verified them cleanly, and found one exact structural fact that
was not in the recorded catalogue (which covered triangles, coclique,
distance-2, pentagons, hexagons, induced-C4, p-rank/SNF, s-sharing — but not
this).

## Result: nullity of the second subconstituent is k/2 exactly at μ=2

Fix vertex 0 of an srg(v,k,λ,μ); H = induced graph on the m = v−k−1
non-neighbours of 0 (m = 84 at k=14). Each outer u has a **pair-label**
P_u = N(u)∩N(0), a 2-set (μ=2). For each **matched edge** {a,a′} of N(0)=7K₂
(λ=1 ⇒ N(0) is a matching):

    x^{a,a′}_u = [a ∈ P_u] − [a′ ∈ P_u].

Verified in exact integer arithmetic (two primes for the mod-p rank):
**H x^{a,a′} = 0 exactly**, and the k/2 = 7 vectors are linearly independent.

| graph | (v,k,λ,μ) | m | nullity(H) | k/2 | matched span = whole ker | non-matched all fail |
|---|---|---|---|---|---|---|
| rook(3) | (9,4,1,2) | 4 | 2 | 2 | ker degenerate | (kernel too small) |
| bvls | (243,22,1,2) | 220 | 11 | 11 | ✓ | 220/220 |
| doily | (15,6,1,3) | 8 | 0 | 3 | — | μ≠2: no 0-eig |
| GQ(2,4) | (27,10,1,5) | 16 | 0 | 5 | — | μ≠2: no 0-eig |

**Asserted only as verified-computed**: nullity(H) = k/2 at μ=2 on both
controls; the k/2 matched-pair vectors are in the kernel and linearly
independent on both; on bvls they span the whole kernel.

**Proven weaker claim** (from construction): nullity(H) ≥ k/2 for every
srg(v,k,1,2) — the k/2 matched-pair vectors are in the kernel, and they are
independent. This holds identically on rook and bvls and would hold on 99.

## Self-attack: the draft "closed-form proof" was over-claimed and retracted

An initial derivation asserted the SET identity A_w = A′_w (hence (Hx)_w=0 "by
case analysis") where A_w = {outer u: u~a, u~w}. The exact check
`pf_second_subconstituent_proof_check.py` shows on bvls that **A_w ≠ A′_w as
sets** on nearly every (matched-pair, outer-w) combination, while
**|A_w| = |A′_w| always** (values 1 or 2). So (Hx)_w=0 holds, but only the
cardinality equality is real — the set-equality proof does not exist, and the
note now states exactly that. Only the exact computation stands as evidence for
Hx=0.

## Status: conjecture, not separator

- The construction uses λ=1 (matching) and μ=2 (pair-labels are 2-sets) — it is
  **specific to the (λ=1, μ=2) subfamily**, which is exactly {rook(9), 99
  (open), bvls(243)}.
- nullity ≥ k/2 is parameter-determined (holds on both controls), so it has
  **no separating power** for srg(99,14,1,2).
- The sharp **equality** nullity(H) = k/2 is a **conjecture on 2 data points**
  (rook, bvls). There is no third μ=2 λ=1 test case in existence. If it held,
  the 84-vertex second subconstituent of a putative srg(99,14,1,2) would have
  zero-eigenvalue multiplicity exactly 7 (rank 77). This is a genuine 99-specific
  value, but it cannot currently be tested or derived; it is a weak line.

## Sequence tools

nullity sequence across the four λ=1 SRGs [2, 11, 0, 0] is a 4-point
distinct-parameter measurement (μ = 2,2,3,5), not an indexed family sequence:
the μ=3 and μ=5 members structurally cannot have the μ=2 kernel. The nullity
restricted to the μ=2 subfamily is [2, 11] — two points, no definable
extrapolation, no OEIS. No closed form, no recurrence, nothing to promote out of
the scratch. Consistent with the standing round-1–31 verdict: **no sequence on
disk separates srg(99,14,1,2) from its controls.**

## Verdict (round 32)

One new parameter-determined structural fact added to the catalogue (the μ=2
second-subconstituent kernel and nullity=k/2 on the controls), one over-claimed
"proof" caught and retracted, and a weak 2-point conjecture (nullity=k/2 for
any srg(v,k,1,2)) that would predict nullity 7 at 99 but has no test case.
Nothing with separating power. NOTHING FURTHER is being promoted; the sequence
line remains closed.

## Files
- `code/out/pf_second_subconstituent_nullity.py` (+ capture) — consolidated exact verification.
- `code/out/pf_second_subconstituent_matched_only.py` (+ capture) — matched vs non-matched.
- `code/out/pf_second_subconstituent_proof_check.py` (+ capture) — the set/cardinality check that refuted the draft proof.
- `research/notes/second-subconstituent-nullity-mu2.md` — the note (with retraction).
