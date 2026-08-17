# Pattern-finder report — round 16: catalogue re-check (unchanged) + clean-design intersection histogram

## What I checked and why

Since round 15 (clean super-simple 2-(22,4,2) existence) the only new on-disk
facts are research notes (scholar pass 7, refuter report) — no new
sequence-bearing artifact. Before concluding NOTHING FURTHER, I re-derived the
entire family-count catalogue independently from closed forms and re-verified
the one genuinely new object (the clean design), so the "exhausted" verdict is
itself grounded in this round's fresh run rather than inherited.

## Finding 1 — the catalogue is unchanged (checked, exact)

Fresh derivation of all nine family sequences over the feasible index set
`u ∈ {1,3,4,10,31}` (k = u²+u+2, a = 2u+1 | 63, v = 1+k²/2):

| sequence | values |
|---|---|
| triangles | [6, 231, 891, 117096, 81842481] |
| pentagons | [0, 33264, 384912, 1669320576, 96451036488576] |
| hexagon base (n3=0 term) | [6, 209286, 4980690, 146767540920, ...] |
| outer blocks | [0, 140, 660, 110880, 81348960] |
| distance-2 | [4, 84, 220, 6160, 493024] |
| coclique bound | [3, 22, 45, 561, 15408] |
| n3 cap | [18, 4158, 26730, 19320840, 121781611728] |
| m_r | [4, 54, 132, 3280, 250914] |
| m_s | [4, 44, 110, 2992, 243104] |

Reference cross-checks against the standing values: **ALL PASS**. First/second
differences are non-zero and non-constant for every sequence, so none is a
low-order polynomial; as established in rounds 1–15, each is a u³/u⁴ quartic
governed by the sparse `a|63` index arithmetic, and no constant-coefficient
linear recurrence fits. None separates 99 from the controls 9 and 243 — the
standing conclusion is unchanged.

## Finding 2 — clean design re-verified; new exact structural fact

The clean (super-simple) 2-(22,4,2) certificate is re-verified this round by
independent exact counting: 77 distinct blocks, every point in exactly 14
blocks, every pair in exactly 2, max triple overlap 1 (**super-simple PASS**);
`RE-VERIFY = True`.

**New this round** — the block-pair **intersection histogram** of the clean
design, previously not tabulated:

```
{0: 1155, 1: 1540, 2: 231}
```

Consistency identities (all exact):
- 1155+1540+231 = 2926 = C(77,2) ✓
- 1·1540 + 2·231 = 2002 = 22·C(14,2) ✓ (double-count block-pairs ∩ point-pairs)
- blocks·4 = 308 = Σ point degrees ✓

This histogram is **distinct from the defective Q1 design** of round 14, which
was `{0:1149, 1:1558, 2:213, 3:6}` (6 block-pairs sharing a triple = 6 direct
mu=2 violations). The clean design has **no** λ₃=3 intersection (no two blocks
share a triple), the super-simplicity condition. That is the exact sense in
which the clean design is the mu=2-violation-free member the graph lift needs.

## Status

- Both findings are **checked** (fresh exact integer run this round), not
  conjectures.
- Finding 2 extends the round-15 existence certificate with its intersection
  histogram — a finite structural fact, **not a sequence**, and it does not open
  a new lever: it merely quantifies that the clean design is mu=2-clean at the
  design level. The lift to a full 99-vertex graph (interlocking of the 77
  outside vertices) remains the open global question, which sequence tools
  cannot touch.

## First-falsifying term

None. The catalogue and the design facts are finitary exact computations over
fixed sets, not fitted patterns; there is no extrapolating sequence to break.

## After this round

The sequence line remains genuinely exhausted (rounds 1–16). The only
99-specific quantities that separate 99 from rook(3) and BvLS are unchanged:
the **coclique bound 22** and the forced **n3≥3**. The next structural steps
are construction/search lines (the full graph lift; the k=14 local triangle
geometry; the multiplicity 3-rank bracket (5,231)), not regularity mining.
NOTHING FURTHER is available from the sequence tools.

## Files

- `code/out/pf_catalogue_recheck_round16.py` — the fresh re-derivation + design re-verify.
- This report.
