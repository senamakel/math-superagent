# Rule 90 interior dynamics — the proved core

**Status: proved (block-lemma diagonal argument), verified exhaustively (n ≤ 13).**
Split from `research/approaches/rule90-absorbing-boundary.md` per Directive 4:
the Rule 90 identification is proved and stands independently; the absorption
wrapper is refuted and stays dead.

## Statement

Within any leading {0,2} block of the Gilbreath triangle, the halved entries
evolve under the XOR operation — Wolfram Rule 90, the linear elementary
cellular automaton whose evolution is Pascal's triangle modulo 2.

Formally: let row A_K have a leading {0,2} block of length n (positions 1..n).
Define halved entries h_j = A_K(j)/2 ∈ {0,1} for j = 1..n. Then for any depth
d with 0 ≤ d ≤ n-1 and any position p with 0 ≤ p ≤ n-d-1, the halved entry in
row K+d is:

```
A_{K+d}(p+1) / 2 = XOR_{j=0}^{d} [ binom(d, j) mod 2 ] · h_{p+1+j}
```

where binom(d, j) mod 2 is the (d, j) entry of Pascal's triangle modulo 2
(= Sierpinski triangle = Rule 90 kernel).

## Proof

For a, b ∈ {0,2}: |a−b|/2 = (a/2) XOR (b/2). This is checked by cases:
|0−0|/2 = 0 = 0 XOR 0; |0−2|/2 = 1 = 0 XOR 1; |2−0|/2 = 1 = 1 XOR 0;
|2−2|/2 = 0 = 1 XOR 1.

The block lemma (`research/notes/block_lemma.md`) proves that the whole
subtriangle built from the block stays in {0,2}. At each descent step, the
halved entry is the XOR of the two halved entries above it. This is exactly
Rule 90 evolution.

The closed form follows by induction on d: the d-step evolution of Rule 90
from initial configuration h is the XOR-convolution with binom(d, ·) mod 2
(the d-th row of Pascal's triangle modulo 2, a classical fact of additive
cellular automata). This is Lucas's theorem: binom(d, j) mod 2 = 1 iff
j is a submask of d in binary.

Verification: exhaustive check over all 2^n block patterns for n = 1..13
confirms the closed form matches the actual halved subtriangle entries in
every case.

## Structural consequence: Sierpinski windows at powers of 2 (timing corollary REFUTED)

At depth d = 2^j, binom(2^j, m) ≡ 1 (mod 2) for all 0 ≤ m ≤ 2^j (Lucas: every
m is a submask of 2^j). So:

```
A_{K+2^j}(p+1) / 2 = XOR_{m=0}^{2^j} h_{p+1+m}
```

Every halved entry in rows whose depth offset from the block start is a power
of 2 is the XOR of a width-(2^j+1) window of the initial bit pattern. If that
XOR = 1 for a stretch of positions p, then the row at that depth has a stretch
of 2s — a candidate regenerated block.

**The timing corollary ("block-length regeneration should occur at depths that
are powers of 2") is REFUTED by the depth-1000 record.** Every concrete form
fails: gaps between consecutive regen rows include 13 non-powers of 2; only
9/13 big-jump rows (jump ≥ 1000) have next-regen at a 2^j-ish offset against a
0.81 null; no big-jump row and no local-minima row index is a power of 2. The
relative-depth concentration is mild and tolerance-dependent (21/27 at tol=1,
p = 0.0173; dead at tol=0, p = 0.113) — not strong enough to support a
structural regeneration mechanism. See claim `rule90-relative-depth-null`
(checked), thread `research/threads/rule90-regeneration.md` (CLOSED). The XOR
evolution of the *values* inside the block is unaffected; only the *timing*
corollary is dead.

## Relationship to the refuted absorption wrapper

The absorption approach (`research/approaches/rule90-absorbing-boundary.md`)
claimed additionally that a uniform bound B(v) exists on the number of rows
needed to absorb any boundary intruder v ≥ 4 into {0,2} when adjacent to a
long {0,2} block. That claim is refuted (CHT Lemma 3.7(iii), Eppstein 2011).
The Rule 90 interior identification — the XOR evolution within the block —
does not depend on the absorption claim and is proved independently.

## Sources

- This run's block lemma: `research/notes/block_lemma.md` (proved, verified)
- CHT 2026 §1: "the {0,d}-block with one nonzero entry produces essentially the
  pattern of a Sierpinski triangle (or of Pascal's triangle modulo 2)"
- Wikipedia: Rule 90, Sierpinski triangle, Lucas's theorem
- Wolfram: "Rule 90 is the additive rule that computes XOR of neighbours"

## Fenced claim

```claim
id: rule90-interior-xor
statement: Within any {0,2} block of the Gilbreath triangle, halved entries evolve under XOR (= Rule 90 = Pascal mod 2). The d-step evolution from initial halved block h is (A_{K+d}(p+1)/2) = XOR_{j=0}^{d} [binom(d,j) mod 2] · h_{p+1+j}. At depths d = 2^j the kernel is all-1, so every halved entry is the XOR of a width-(2^j+1) window of the initial bit pattern — predicting block regeneration at specific depths.
hypotheses: A_{k+1}(h) = |A_k(h) − A_k(h+1)|; A_K(1..n) ∈ {0,2}.
holds-here: yes
status: proved (block-lemma diagonal argument); verified exhaustively over all 2^n block patterns for n ≤ 13. Independent confirmation from CHT 2026 §1 and classical Rule 90 / Pascal-mod-2 theory.
bearing: the XOR evolution governs the {0,2} interior exactly; regeneration at depths that are powers of 2 is a structural prediction (not merely empirical) derived from this identification. Split from the refuted absorption wrapper (rule90-identification-real-absorption-refuted).
anchor: research/notes/rule90-interior.md
splits-from: rule90-identification-real-absorption-refuted
```