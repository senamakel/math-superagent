# Cobeli–Crasmaru–Zaharescu 2000, "A cellular automaton on a torus" — Thwaites's conjecture

<!-- source: http://emis.muni.cz/journals/PM/57f3/pm57f305.pdf | Portugaliae Math. 57(3) (2000) 311–323 -->
<!-- Replaces the placeholder digest. Full text at [[cobeli-crasmaru-zaharescu-2000-cellular-automaton-torus.full]] -->

## What it establishes

**Setting is CYCLIC (torus), not half-infinite.** Fix a length-d sequence
`(a_0..a_{d-1})`, extended periodically (`a_{k+d}=a_k`). The evolution is
`a'_k = |a_k − a_{k+1}|` with indices mod d. This is the same absolute-difference
operator as Gilbreath but **wrapped around a cycle of length d**, so every row
has exactly d cells and nothing escapes right — the fundamental difference from
the half-infinite triangle this run studies.

**Theorem 1 (Thwaites's conjecture, proved).** For any rational initial
sequence on a d-torus, iterating `|a_k−a_{k+1}|` mod d eventually reaches a cycle
whose entries all lie in `{0, r}` for some r>0; the cycle is the all-zero cycle
**(regardless of initial data) if and only if d is a power of 2.**

Mechanism: after rescaling, entries become {0,1}, where `|a−b| = a+b mod 2`
(addition in Z/2Z), i.e. the operator is XOR with the Pascal/`(1+X)` kernel. The
paper's Table 1 shows the d-th row is all zeros when `d=2^m`, and for d not a
power of 2 there exist sequences (e.g. `e_0=(1,0,...,0)`) whose rows at
power-of-2 depths are never all zero.

**Cycle-length structure for d not a power of 2.** Write `d = 2^k r`, r odd,
s = ord_r(2). Theorem 2: `2^k(2^s−1)` is a period of φ; for d an odd prime with
s even, `d(2^{s/2}−1)` is a period. **Corollary 3 (the period criterion):**
`k` is a period of `φ(x)=x·ρ(x)` (x is the {0,1}^d vector, ρ right-rotation,
· componentwise XOR) **iff the integers `ν_{k,d}(m)` have the same parity for all
m ∈ {1..d}**; these count the subsets R ⊂ R_k (R_k = powers 2^{l_i} mod d from the
binary digits of k) whose residues sum to m mod d. Theorem 3/Prop 1 give an
`O(s log k)` algorithm to compute φ^(k) by the base-2 decomposition (square-and-multiply
with rotations), which is the standard Rule-90 exponentiation-by-squaring.

## What it means for THIS run

- **It is NOT the collapse mechanism for the dyadic-periodicity-collapse thread.** The
  thread's collapse is about the *half-infinite* right diagonal with a *periodic halved-gap
  input h*; that mechanism is the run's proved `rule90-interior-xor` (periodic-window folds,
  claim `rule90-periodic-window-collapse`). Cobeli's Theorem 1 is the *cyclic* analogue and
  applies to the length d of the torus, not to a period of a half-infinite input. Do not cite
  it as the thread's collapse proof.
- **It independently confirms the "power of 2 is special" phenomenon in the F₂-Pascal-torus
  geometry.** The same `(1+X)`-XOR kernel that this run proved governs the halved `{0,2}`
  interior is exactly Cobeli's operator; the all-zero collapse at power-of-2 length is the
  torus reflection of the run's power-of-2-kernel-is-all-1 fact (`granville-lucas-kummer-sierpinski`).
- **It does not resolve the odd-factor growth half of the thread** (minimal period with an odd
  factor → ν₂ ~ c·n). Cobeli's cycle-length machinery is for the *length of cycles*, not the
  *density of ν₂ in the right diagonal*; nothing here explains why period-6 grows. Do not claim
  it does.
- **The parity criterion (Cor 3) is the clean primitive** the thread's "odd factor in the
  period breaks collapse" intuition would have to reconnect to: in the cyclic geometry a
  period collapses exactly when the subset-sum parities `ν_{k,d}(m)` agree. This is a cyclic
  statement; extending it to the half-infinite ν₂ ≥ c·n transfer is open and NOT in any source.

```claim
id: bcz2000-thwaites-cyclic-diff-collapse-power-of-2
statement: (Cobeli–Crasmaru–Zaharescu 2000, Portugaliae Math. 57(3):311–323) On a cyclic d-torus, iterating |a_k - a_{k+1}| mod d reaches the all-zero cycle for every initial rational sequence iff d is a power of 2 (Thm 1). For d = 2^k r (r odd, s = ord_r(2)), 2^k(2^s-1) is a period, and k is a period of phi(x)=x·rho(x) iff the subset-sum parities nu_{k,d}(m) have one common parity for all m (Cor 3).
hypotheses: cyclic (wrap-around) absolute-difference map on sequences of length d; entries rescaled to {0,1} where |a-b| = a+b mod 2 (the (1+X) XOR kernel).
holds-here: no (as a statement about the half-infinite Gilbreath triangle it is the wrong object); yes as the cyclic geometric analogue of the run's power-of-2-kernel fact.
status: proved in source (peer-reviewed)
bearing: independent confirmation that power-of-2 is special in the F2-Pascal absolute-difference geometry; provides the clean period-parity criterion (Cor 3) as the primitive the dyadic thread's odd-factor half would reconnect to. NOT the collapse mechanism for the half-infinite thread (that is rule90-interior-xor); does NOT explain odd-factor growth.
anchor: research/sources/cobeli-crasmaru-zaharescu-2000-cellular-automaton-torus.full.md
answers: does-any-held-source-cover-thwaites-cyclic-differences
```

> **No `follows-from` edge is drawn to rule90-interior-xor on purpose.** The
> two share the F2 (1+X) kernel but differ in boundary condition (cyclic torus
> vs half-infinite triangle), and Cobeli's Theorem 1 is an independent, source-proved
> result (Thwaites's conjecture), NOT a corollary of rule90-interior-xor.
> Dragging an entailment edge would mislead ENTAILMENT.md into treating it as derived.

## Status
- **This was an unfinished placeholder digest; now replaced.** No other held source covers
  Thwaites's conjecture / cyclic differences, so this closes the one genuinely undigested
  hold-out that bears on the live thread.
- Contradicts nothing in recalled memory: it is consistent with `rule90-interior-xor` (same
  kernel) and is explicitly the *cyclic* object, not the half-infinite one the thread is about.
