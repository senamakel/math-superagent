# Scholar pass — library integrity verification

Date: this cycle. Independent re-check of the load-bearing claim blocks and
captures against their recorded numbers, since a claim a later run builds on is
only as good as the capture behind it. **Verdict: internally consistent; no
over-claim found among the load-bearing items checked.**

## What was checked (each against the actual stored capture / full text)

1. **Descent lemma core** (`code/out/descent_halved_verify.captured.txt`):
   12,582,900 (pattern,w) halved pairs, L=1..18, 0 violations of claims (1),(2),(3);
   even-unit cross-check 2,621,432 pairs, 0 violations; sharpness on all-1s for
   every L=1..18. Matches `lemma54-descent-proof-repaired.md` exactly.

2. **ν₂ table** (`code/out/nu2_granville_check.captured.txt`): n=50..3999,
   ν₂/n ∈ [0.42, 0.52], g* ≤ 2ν₂+2 held at 0 of 8 fails, factor ~26 over n^0.525
   at n=3999. Matches `granville-nu2-density-measured`.

3. **Link A / composition** (`code/out/verify_lemma54_v_le_gstar.captured.txt`):
   1181 real prime columns n=20..1200, 0 violations of v ≤ g*_n and of the Lemma
   5.4 hypothesis, max margin (2ν₂+2)/g*_n = 35.882. Matches the thread's record.

4. **ν₂/w transfer** (`code/out/reconcile_nu2w.captured.txt`): dense min ν₂/w =
   0.5152 at n=53 over n∈[50,3000]; sparse-set min 0.6885 at n=100; nu2 ≥ w/2 at
   every measured n. Matches `g-supply-transfer-measured` / `nu2w-minima-reconciled`.

5. **Block lemma constant 1**: verified directly against the Odlyzko 1993 LaTeX
   full text (§2, eq. 101, "d_k(1)=1 for K ≤ k ≤ N+K−1") and Table 2 (G(π(10^x))
   = 5,15,35,...,635). The re-derivation in `research/notes/block_lemma.md`
   (n+1 rows, diagonal-subtriangle argument) is consistent with the primary
   source. The `≈ n/2` figure is a genuine misremembering, correctly refuted.

6. **Two-point G-supply crux**: `research/notes/g-supply-two-point-crux-settled.md`
   is internally sound — the mod-4 switch count is two-point, so one-point
   PNT-in-AP/GRH/Dirichlet cannot bound it; the explicit countermodel (list all
   1-mod-4 primes then all 3-mod-4 primes) does impose zero lower bound from the
   marginals. ABGS 2011 §9 and LOS 2016 both correctly cited as conjectural.

## Memory consistency

recall_memory across the reduction, block lemma, regeneration, and supply-side
terms returns only content already mirrored on disk; nothing recalled contradicts
the stored captures. The graph-half of recall is currently unavailable (Cognee
triplet pipeline not built) — a recall *tooling* gap, not a content conflict.

## What this pass adds

A confirmation that the run's load-bearing claims are backed by captures that
reproduce their recorded numbers, so nothing in them needs re-deriving before
use. It does NOT change the mathematics: the open content remains exactly the
supply-side linear bound ν₂ ≥ c·n (named-open two-point mod-4 switch problem),
with Lemma 5.4's descent core proved and Lean-kernel-checked, and erosion
settled while regeneration is the open question.

## Caveat

I have no exec tool in this run, so "checked" above means cross-read of stored
captures against stored claims, not a fresh execution. The captures themselves
were produced by the run's own programs (recorded in each). The one genuinely
unrun verifier on disk is `code/scholar/verify_supply_transfer_independent.py`
(a third route into ν₂/w); it is redundant with the two already-agreeing captures.
