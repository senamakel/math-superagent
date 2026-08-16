# g_run_telescope_verify — negative control + corrected claim (directive 26)

## What ran

`code/gfold/g_run_telescope_verify.py` re-run at full scale (`--trials 30`,
`d` up to 2^14), now with the directive-26 failing negative control appended.

Capture: `code/out/g_run_telescope_verify_negctrl_full.captured.txt`
(exit 0). The streamed pipeline ran one row at a time, no materialization.

## What the positive checks establish

- **C1** down-set run structure `↓d = ∪ [m·2^g, (m+1)·2^g − 1]`, g = ν₂(d+1),
  run length 2^g, run count 2^(popcount(d)−g): all **16385** values d=0..16384
  pass by brute submask enumeration.
- **C2** telescoping identity `XOR_{o∈[u,v]} h[pos+o] = [r_{pos+u} ≠ r_{pos+v+1}]`
  on the real prime-residue h (`r = q_j mod 4`): **52275** brute (element
  enumeration) + **1654885** prefix-XOR (algebraic) (d,pos) pairs, ALL PASS.
- **C2 random**: 30 random h = **1568250** brute + **49646550** prefix pairs,
  ALL PASS.

## The negative control (directive 26) — the point of this capture

The positive identity holds because `h[j] = [r_{j+1} ≠ r_j]` for a **two-valued**
boundary r: XOR over an interval is the parity of flips, and two-valuedness is
what makes odd flips ⇔ differing endpoints. That two-valued hypothesis is
load-bearing, so a run that ONLY ever passes cannot distinguish "identity true"
from "predicate true by construction".

**Control:** perturb to a **three-valued** boundary `r = q_j mod 3`. Parity of
flips no longer determines endpoint difference (`0→1→2` is two flips with
different endpoints). Result:

```
brute: d=0..1024 x 21 positions = 620067 pairs, MISMATCHES = 438 (expected
nonzero; the 2-valued hypothesis is load-bearing)
first mismatch d=1 pos=0 run=0-1 xor=0 tel=1
```

Mismatches = **438, nonzero** — the identity genuinely breaks when the
two-valued hypothesis is removed. This is the check that the 2-valued `q_j mod 4`
result is not vacuous: it relies on an actual arithmetic hypothesis (residues
take exactly two values), and removing it produces a measurable failure. The
`q_j mod 2` and `q_j mod 4` prime boundaries both sit in the 2-valued class, so
the positive result is specific to that class and not true by construction.

## Corrected claim block

```claim
id: g-run-telescope-verified
statement: For every d ≥ 0 the digital down-set ↓d partitions into maximal
  consecutive-integer runs, g = ν₂(d+1): each run length exactly 2^g, run count
  exactly 2^(popcount d − g), each run a block [m·2^g, (m+1)·2^g − 1]; and for
  any {0,1} string h with two-valued boundary r (h[j]=[r_{j+1}≠r_j]; prime
  case r = q_j mod 4) any run [u,v] telescopes:
  XOR_{o∈[u,v]} h[pos+o] = [r_{pos+u} ≠ r_{pos+v+1}].
hypotheses: C1 checked for d = 0..16384 by brute submask enumeration (16385
  values). C2 checked on the real prime-residue h: 52275 brute + 1654885
  prefix-XOR (d,pos) pairs; and on 30 random h: 1568250 brute + 49646550
  prefix pairs — all PASS. The two-valued boundary is load-bearing: replacing
  it by a three-valued boundary (r = q_j mod 3) produces 438 mismatches over
  620067 pairs (negative control), so the identity is not true by construction.
holds-here: SCHEME-scoped — the run-structure/telescoping facts hold for
  d = 0..16384 on the prime and random two-valued h as enumerated above. The
  identity is algebraic (associativity of XOR over an interval, parity of
  flips) and holds for ANY two-valued boundary by the same argument; only the
  finite verification range is d = 0..16384.
status: checked (machine-verified, exact F2 arithmetic, two routes agree: brute
  element enumeration + prefix-XOR difference; negative control fails with a
  nonzero count as required).
bearing: this is the reduction step grounding the adopted dyadic-gap-correlation
  approach — it expresses a submask-XOR (down-set) fold cell as an interval
  parity under the two-valued prime-residue boundary. It buys nothing, by
  itself, for wt(Φ_n h) ≥ c·n: it reorganises the fold into the run/telescope
  form but does not bound its weight. Whether the telescoped form lets a
  weaker arithmetic input (below positive mod-4 switch density) force linear
  weight remains exactly the open question of GOAL priority 2.
anchor: code/out/g_run_telescope_verify_negctrl_full.captured.txt
```

## Status

Measurement/verification, not a proof of SUPPLY. All positive checks pass; the
negative control fails with a stated nonzero count, which is what makes the
pass meaningful.
