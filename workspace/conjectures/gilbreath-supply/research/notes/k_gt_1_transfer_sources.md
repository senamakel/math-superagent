# K>1 transfer — what the new sources establish for the reopened pass

This pass's territory (GOAL.md): is there a functional of the fold, sensitive to correlation
order `1 < K ≲ n/2`, controllable by an arithmetic input **strictly weaker than pointwise
mod-4 switch density**? The library's K>1 corner was thin. Two new primary sources now cover it.

## 1. Lacasa, Luque, Gómez, Miramontes (arXiv:1802.08349) — unconditional forbidden blocks, but mod 6

- Prime gap sequence mod 6 (symbols {0,2,4}): a block of m consecutive gap residues is forbidden
  iff some prime r is "ticked" by all partial sums. Exact counts |A(m)|=2^{m+1} admissible,
  |F(m)|=3^m−2^{m+1} forbidden; first (4,4) at m=2; h(0)=log 2 < log 3. **Unconditional**
  (divisibility of integers). This is the strongest unconditional K>1 structure on the gaps.
- Primes mod k (k=3,4,6): no forbidden patterns, but a **monotone-decreasing Rényi spectrum** —
  length-m blocks (m>1) occur non-equiprobably; a real higher-order pattern not reproduced by any
  null model. Frequencies conditional on Hardy–Littlewood.

**Transfer = NEGATIVE (parity projection).** The fold reads the mod-4 gap-**parity** string
`h[j]=(g_j/2) mod 2`. Since `g=6a+c` ⇒ `h = (3a+c/2) mod 2 = (a mod 2) ⊕ (c/2 mod 2)`, with `a`
free, the parity bit carries **no mod-6 information**: every parity block is realisable from both
an admissible and a forbidden mod-6 block. Hand-verified at m=2 ((4,4) → all four parity blocks).
General-m statement recorded as conjecture, mechanical check queued
(`code/librarian/lacasa_projection_check.py`). **The unconditional mod-6 forbidden structure does
not survive to the fold's parity input.**

## 2. Wu (arXiv:1908.07095) — length-k pattern frequencies, the parity barrier at every order

- For length-k ≥ 2 patterns of consecutive primes mod q, `π(x;q,a)` is **not known to tend to
  infinity** for non-constant a. Only constant patterns are unconditional: Shiu (π→∞), Maynard
  (π > Cπ(x) — verified against the library's Maynard source, Thm 3.3). Observed non-uniformity:
  mod 10, x=10^8, π((1,1))≈4.62e6 vs π((9,1))≈7.99e6 vs naive 6.25e6.
- Theorems (conditional) control the lower-order terms of the LOS pair-bias asymptotic and let it
  be truncated at arbitrary order n.

**Consequence.** The parity barrier is not a K=1 artifact. At *every* pattern length k ≥ 2, only
the equal-residue (constant-pattern) side is unconditional, and that is the **zero-run / no-switch**
direction — the wrong direction for SUPPLY, which needs switches.

## Synthesis for the reopened pass

The two new sources bracket the K>1 question from opposite sides and neither supplies the sought
input:

- The only **unconditional** K>1 structure on the prime gaps (Lacasa's forbidden blocks, mod 6)
  is destroyed by the mod-4 parity projection the fold applies. So it cannot drive a K>1 functional
  of `wt(Φ_n h)`.
- The K>1 structure that **would** survive to the fold's input (length-k mod-4/parity patterns, Wu)
  is exactly the conjectural, L-function-inaccessible, parity-barred part — no theorem, and the
  unconditional side of it is the zero-direction.

**Open (unchanged):** whether any K>1 functional of the fold, on the actual prime parity string h,
is controllable by an input strictly weaker than pointwise mod-4 switch density. These sources
close the two *naive* suppliers of such an input (unconditional mod-6 forbidden blocks; unconditional
length-k patterns). The remaining hope is a fold-structural (Lucas/kernel/second-moment) input, which
is the territory already mapped as open in `research/REQUESTS.md` (`walsh-spectral-subset-b904`).

## Claims filed
- `lacasa-forbidden-gap-blocks-unconditional` (proved; mod-6)
- `wu-length-k-pattern-frequencies-open` (asserted barrier; Shiu/Maynard parts proved)
- `lacasa-mod6-forbidden-blocks-parity-invisible` (proved for ALL m by per-coordinate
  bijection; claim block in `lacasa_parity_projection_transfer.md`)

## Mechanical check (optional confirmation, NOT a gate)
The general-m projection statement is PROVED for all m by a per-coordinate bijection (each
parity bit h_j = (a_j mod 2) xor (c_j/2 mod 2) reaches both values for every class, coordinates
independent), so it does not need a run before being cited. `code/scholar/lacasa_parity_projection_check.py`
is a confirmation for m=1..6 (abstract + real-prime data), not the evidence. Do not re-derive
the result as if it were open; a run would only be a cross-check, not a gate.
