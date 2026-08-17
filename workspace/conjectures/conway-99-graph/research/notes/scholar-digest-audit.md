# Scholar digest audit — the library is faithful, and one 99-specific lever remains unchecked

<!-- source: scholar role audit of research/sources + research/summaries, this run -->

## Verdict

The library is complete, CLOSED, and internally consistent: 49 full texts in
`research/sources/`, one digest apiece in `research/summaries/`, 104 claims in
`derived/CLAIMS.md`, all requested gaps answered. The scholar has read the
load-bearing digests **against their full texts** and confirms each is faithful:
no digest misrepresents its source on any statement the run leans on. This
note records that audit and the one thing that emerged: a genuinely 99-specific
forbidden/forced configuration candidate that remains `asserted`, never verified.

## Digests verified faithful against their full texts

1. **Makhnev 1988 (primary Russian, mathnet.ru paperid=4220).** Condition (*)
   [any two triangles joined by ≥2 edges are joined by exactly 3 edges] IS
   Reimbayev's n3=0. Thm 1: under (*), a λ=1 SRG is μ≤3 or (27,10,1,5). Thm 2:
   no srg(99,14,1,2)/(115,18,1,3) satisfies (*), via a forced srg(33,12,1,6)
   subobject that is itself parameter-INFEASIBLE by multiplicity integrality
   (g numerator 2k+(v-1)(λ−μ) = −136, not divisible by √Δ=7; verified in
   `code/out/check_srg33_12_1_6.captured.txt`). Oracle gate passed: BOTH
   controls rook(3), bvls satisfy (*) with n3=0 (μ=2≤3 absorbs them in Thm 1).
   Contrapositively any putative (99,14,1,2) has n3≥1 (constraint). This is the
   verified backbone of the n3 lever.

2. **Reimbayev hexagon bound (arXiv:2409.10620) and order-6 counts
   (arXiv:2508.03377).** n12 ≥ (1/12)nk(k−2)(2k²−21k+53), attained iff n3=0;
   identity n12 = formula + n3 verified exactly on both controls with n3=0.
   The 62 order-6 counts do NOT arithmetically force n3≥1 at 99 (all admit
   n3=0, residue n3≡0 mod 3, admissible interval [0,4158] at k=14). So order-6
   counting alone cannot separate 99 from the n3=0 controls; n3 is the crux,
   and n3=0 is only Reimbayev's conjecture.

3. **Brouwer–Neumaier 1988 μ=2/PLS dichotomy** does not bite 99: λ(λ+3)/2 = 2,
   k=14≥2, so neither the grid nor the PQ branch is triggered. Claim
   `bn-88-mu2-structure` (formerly `unchecked`) is faithful to the source.

4. **k=14 nonexistence templates.** Wilbrink–Brouwer (57,14,1,4) and
   Shpectorov–Zhao (85,14,3,2) are faithfully digested; both share the 7K₂
   local structure and neither decides 99, but each is a transferable template
   that the run's n3/k14-l1-local threads already cite.

5. **Automorphism bounds** (Makhnev–Minakova |G| | 2·3³·7·11; Cesarz–Woldar
   7||G|⇒Z₇, 2||G|⇒|G||6, computer-free; Crnković–Maksimović no Z6/S3/Z9/E9;
   Behbahani–Lam primes {2,3}, order-3 fixed-point-free) — all sourced and none
   relies on the (refuted on bvls) fixed-set-is-coclique lemma (claim
   `audit-fixed-set-lemma-no-source-uses-it`).

## The one thing that emerged — a 99-specific separator, still asserted

**Keramatipour Theorem 3.4.2 / claim `keramatipour-no-paley9-pattern-99`**
asserts: a putative srg(99,14,1,2) CANNOT follow the Paley(9) pattern
(Definition 12: for every vertex v and matched pair of N(v)-edges, the
9-vertex induced subgraph is Paley(9)); the proof forces two vertices to share
three neighbours.

The control-side is now **verified** by this run: the pattern is CONFIRMED
present on BOTH existing members — rook(3)=srg(9,4,1,2) (9 configurations) and
bvls=srg(243,22,1,2) (13365 configurations), exact check
(`code/out/paley9_pattern_check_fixed.captured.txt`, new claim
`keramatipour-paley9-pattern-holds-on-controls`, checked).

**Why this is a genuine k=14 separator (not refuted on arrival):** the theorem's
proof explicitly uses the k=14 vertex budget — "name vertex 0's neighbours 1 to
14, 2i−1 adjacent to 2i" — and builds 7 parallel triangles through the 7 edges
of the matching. rook(3) has k=4 (only 2 matching edges, the 9-vertex pattern
is the whole graph, no budget to force a contradicting triangle) and bvls has
k=22 (more than 14 neighbours, so the "14 named neighbours" forcing does not
close). So the contradiction is plausibly absent exactly where the two
controls live. **But the proof is an informal case analysis in an unrefereed
MPhil thesis and has NOT been independently verified.** It is the one
load-bearing `asserted` claim in the library that is a candidate 99-specific
forbidden configuration — the exact shape the run's deliverable asks for.

## What remains genuinely open (for the run to attack)

- Whether Keramatipour Thm 3.4.2 is sound — i.e. whether the full Paley(9)-pattern
  really is forbidden at (99,14,1,2) while holding on rook(3) and bvls. This is a
  finite local-forcing question within the 7K₂/μ=2 geometry, checkable by the
  oracle against both controls, and is the crispest 99-vs-family separator the
  library currently holds unverified.
- The n3 lever itself: n3≥1 is a constraint, not existence; n3=0 (Makhnev's
  route) is only Reimbayev's conjecture.
- Triviality of Aut(99) and existence itself.

## Note on durable memory

Cognee is degraded per directive 20 (recall returns little; `remember_memory`
fails on a health-check timeout, 4 attempts). Durable knowledge lives on
disk — `derived/CLAIMS.md`, this note, the summaries — and is complete. Nothing
durable is lost by the memory outage.
