# Pattern-finder report — round 10: c7 proved from λ=1 (upgrades from asserted to derived); induced-C4 family sequence

## What changed since round 9

Round 9 closed the flag on the incidence-code p-rank sequences (these are
control values spanning two families, not a parameter-uniform sequence). The
run's catalogue of parameter-determined family counts (rounds 3–8) was
complete. Two things were **not** on disk as sequences, and one claim was
recorded as merely *asserted* when it is in fact *provable from λ=1*:

1. **c7** (`c7-4vertex-mu2-common-neighbour-nonadjacent`) sat in `research/CLAIMS.md`
   as "asserted by the source, not proved there and not checked here"
   (status `asserted`). This round proves it from λ=1 and checks it on every
   known λ=1 member.
2. **The induced-C4 count as a family sequence** was never tabulated
   (`code/out/count_induced_C4.py`'s own docstring says "rounds 1-8 never
   tabulated an induced-C4 count as a family sequence"). This round derives and
   checks it.

## Finding 1 — c7 is a THEOREM of λ=1 (upgraded from asserted to proved)

**Claim:** in any `srg(v,k,1,2)` (in particular a hypothetical `srg(99,14,1,2)`),
the two common neighbours of any non-adjacent pair are non-adjacent to each other.

**Proof (derived here, no external citation needed):** take a non-adjacent pair
`{u,v}` and two common neighbours `a,b`. If `a~b`, then edge `ab` belongs to
triangle `abu` and to triangle `abv`. These are two *distinct* triangles sharing
the edge `ab` (they differ in their third vertex, `u` vs `v`). But λ=1 says every
edge lies in a **unique** triangle. Contradiction. Hence no two common neighbours
of a non-adjacent pair are adjacent. QED.

This is the same content as Sims' alpha=beta=0 criterion that the source cites,
but stated here as a self-contained λ=1 argument. It holds for the **whole
family**, so it is a proof, not a two-control check.

**Checked exactly on all four known λ=1 members** (`code/out/induced_C4_proof_check.py`,
exact integer adjacency, `is_srg` entry guard on each):

| graph | (v,k,μ) | nonedge pairs | common-neigh pairs that are adjacent (c7 violations) |
|---|---|---|---|
| rook(3) | (9,4,2) | 18 | 0 |
| doily | (15,6,3) | 60 | 0 |
| GQ(2,4) | (27,10,5) | 216 | 0 |
| BvLS | (243,22,2) | 26730 | 0 |

## Finding 2 — induced-C4 count: family sequence (NEW) and its closed form

For a `λ=1` graph, every non-adjacent pair's common neighbours are pairwise
non-adjacent (Finding 1), so **every** unordered pair of common neighbours gives
one induced 4-cycle:

```
induced C4  =  C(μ,2) · #nonedges      for every λ=1 SRG.
```

In the **μ=2 family** (`k∈{4,14,22,112,994}`, `v=1+k²/2`) specifically:

```
induced C4  =  #nonedges  =  v·k(k−2)/4  =  v(v−1−k)/2 .
```

**Family sequence** `[18, 4158, 26730, 19320840, 121781611728]`
(checked: rook 18, BvLS 26730). This is **identical** to the n3-cap family of
report 6 (`v·k(k−2)/4`) — of course, since both reduce to nonedges.

Sequence tools over the 5 terms: `analyze_sequence` — not a low-degree
polynomial, every term divisible by 18, residues mod 2 period 1;
`find_linear_recurrence(order ≤ 4)` — **no constant-coefficient linear
recurrence**, matching every other family count (all quartic-in-`u` from
`k=u²+u+2`); OEIS: not catalogued (a miss recorded so nobody re-searches).
`induced_C4_family.py` verifies the parametric identity `#nonedges = v·k(k−2)/4`
on all five feasible members symbolically.

## Status

- **Finding 1 (c7 theorem):** a **proof** (derived from λ=1); the four-member
  check is corroboration, all exact. Cannot be falsified by any member of the
  λ=1 family — it inherits from the definition. It is inert for separating 99
  (both controls satisfy it, as round-1/`4vertex-condition-lead` established),
  but it is now a *derived* theorem rather than an asserted source fact, which
  hardens the session's foundation for any argument that uses c7 (e.g. forcing
  a non-adjacent pair of common neighbours, diamond-freeness).
- **Finding 2 (induced-C4):** a **derivation** verified on all four known λ=1
  members. Like every family count it is parameter-determined and holds on the
  controls — it does **not** separate 99.

## Bearing on the open problem

Induced-C4 is the one count that round 4's K4−e argument gestured at (both are
4-vertex counts) and — like K4−e (identically 0) — it is degenerate as a 99-lever:
it is exactly `#nonedges`, fully parameter-determined, and equal on the μ=2
controls. The genuinely useful output of this round is the **c7 upgrade**:
it converts a source-asserted structural fact the run relies on into a proved
λ=1 theorem, so future 99 arguments built on "common neighbours of a nonedge are
nonadjacent" rest on a derivation, not a citation.

The standing separation levers are unchanged: the **22-coclique** value (report 3,
parameter-specific, distinct from controls' 3 and 45) and the **n3≥1/≥3** forced
case (Makhnev conditional, reports 2/6).

## Files

- `code/out/induced_C4_proof_check.py` — c7 + induced-C4 exact check on all four λ=1 members.
- `code/out/count_induced_C4.py`, `code/out/induced_C4_family.py` — direct C4 counts and parametric identity.
- This report (`code/out/pattern_finder_report10.md`).
