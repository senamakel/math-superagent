# Scholar verification pass — what this digesting round established

Scope: I read the mature disk library (37 full texts, ~50 digests) against the
problem, verified the load-bearing claims against their primary sources, and
recorded the durable findings to Cognee. Summary of the independent checks and
the contradictions surfaced.

## Independent checks performed this pass

**1. Pirzada orders — verified by hand against the primary source.**
Reading `sources/pirzada-2power-unicyclic-proof.full.md`: with |P_i| =
8·Σ_{j≤i}2^j = 8(2^{i+1}−2), each gadget half is |X_i| = 2|P_i| + 8 + 3 + 4 =
16(2^{i+1}−2)+15 = 32·2^i − 17, and |G_i| = 2|X_i| = 2^{i+6}−34. Check:
G1=2^7−34=94, G2=2^8−34=222, G3=2^9−34=478 — all three match the paper's own
orders. The printed table recurrence |G_i|=|G_{i-1}|+2^{i+4} gives 158, 286,
so it contradicts the paper's own orders and is a confirmed typo (correct
transition +2^{i+5}). The unique-2-power-length-2^{i+4} claim is sound:
half-order |X_i| < 2^{i+5}, all of 4..2^{i+3} avoided, 2^{i+4} present.

**2. Oracle: no power-of-two cycle, validated.**
`code/out/oracle_validation.out` shows all ground-truth checks PASS
(K3,C5,C7,C9→no; C4,C8,C16,Petersen,K4→yes) and the cycle counts agree
exactly with an independent connected-2-regular edge-subset enumerator on
Petersen/K4/C8/C5/K3. The vertex-set→edge-set cycle-keying bug was found and
fixed (Petersen 9-cycles: 20 distinct, not 10). Status: checked.

**3. Carr minimal-counterexample structure — full proof held.**
Markström proved the independent-set structure; Carr's full text proves every
vertex is adjacent to a degree-3 vertex and ≥4/7 have degree exactly 3. The
2/3 refinement (|V3| ≥ 2|V≥4|+1) is a forum-post-derived deduction verified
step by step against Carr's lemmas; status `derived`, not Lean-checked.

## Contradictions surfaced (the valuable rows)

- **Gebendorfer 2026 preprint** claims a full proof via "δ≥3 forces a C4 or
  C8"; this contradicts Markström's four 24-vertex cubic no-C4-no-C8 graphs,
  Exoo's 78-vertex no-{4,8,16} and 540-vertex no-{4,8,16,32} graphs, and G420
  (3-connected cubic planar, no-{4,8,16}). Full text unobtainable; conjecture
  treated as OPEN; do not cite the preprint.
- **Pirzada Conclusion** over-claims to rule out all counterexamples, but its
  final step invokes "each cubic graph has a 2-power cycle" = the conjecture
  itself (circular). Cite only the construction.
- **Pirzada printed recurrence** contradicts its own orders (typo) — the
  correct closed form is 2^{i+6}−34.

## Sources that do not help (and why)

- **OEIS A280939** (EGF 2·sinh(x/2)/sqrt(2−exp(x))) — no connection to any
  cycle-length, degree, or 2-power content in the library; recorded not
  helpful.
- **Throwaway stub files** (`exoo-G24a/G24b/N46/N4610/N468/N4832`): image-only
  data subpages, "image-only (automorphism group, similar-vertices)" —
  substantively the same as the already-held Exoo index page.
- **Verstraëte 2016 survey body** — paywalled; value is bibliography only.
- **Cayley-graph classes** (Ghaffari–Mostaghim; Ghasemi–Varmazyar) — settled
  classes but high-symmetry, weak structural transfer to the non-symmetric
  minimal counterexample.

## What the run still lacks

- **ROOT.md exists and Phase 1 is complete** (created this cycle by the
  librarian; meets GOAL criterion 1: §2 minimal-counterexample structure, §4
  verification bound, §3 settled classes). My survey confirms the library is at
  the gap-driven steady state.
- **No independent check of the 2/3 degree-fraction** (derived, not
  Lean-formalised).
- Balaji's 32-vertex bound is asserted (no formal certificate) — the oracle
  should reproduce n≤16/n≤19 subsets first.
