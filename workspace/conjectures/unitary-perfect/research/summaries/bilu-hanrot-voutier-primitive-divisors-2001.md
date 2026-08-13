# Bilu–Hanrot–Voutier (2001), *Existence of primitive divisors of Lucas and Lehmer numbers*

Full text: [[bilu-hanrot-voutier-primitive-divisors-2001.full]] (INRIA RR-3792; the PDF OCR is almost entirely garbled — unusable as text. Only the front matter and citation survive legibly).

**What this source establishes.** The paper proves the *Primitive Divisor Theorem*: for `n > 30` (and the small exceptional `n` catalogued), the `n`-th term `u_n` of a Lucas sequence (and a Lehmer sequence) has a primitive prime divisor — a prime dividing `u_n` that divides no earlier `u_k`. In particular every `2^m + 1` (equivalently every cyclotomic value `Φ_n(2)`) with `n` in the covered range has a primitive prime divisor.

**Why this run holds it load-bearing.** Maciejewski's Proposition 4 (the Higgs-cubefree structural lemma) uses exactly this: for `m = 2k ∈ H_even`, Zsigmondy (of which BHV is the effective modern form) gives a primitive divisor `r` of `2^{2k}+1` with `ord_r(2) = 4k`, so `4k | r − 1`; then `r` being 3-Higgs forces `v_q(r−1) ≤ 3`, giving `v_q(k) ≤ 3` and the divisor-closure `2d ∈ H_even`. It is also what the paper's Conjecture 23 cites for `k ≥ 4`. The run's `heven-prime-case-reduction` and `heven-thinness` claims rest on it.

**Hypotheses checked.** The theorem's hypotheses (Lucas/Lehmer sequence, `n` large) hold here: `Φ_{4p}(2)` is a cyclotomic value whose primitive divisor has order exactly `4p`. Effective, non-conditional (unlike GRH).

**Caution.** Because the captured OCR is unusable, I could not re-verify the exact `n > 30` threshold or the exceptional-case list from the text. The claim is therefore recorded at `status: asserted` on the strength that Zsigmondy's theorem is classical and well-established, not from a readable derivation in this file.

```claim
id: bhv-primitive-divisor-theorem
statement: For Lucas/Lehmer sequences, u_n has a primitive prime divisor for
  all sufficiently large n (all n > some bound; n = 30 and a catalogue of
  small exceptions). Applied to 2^n + 1, every cyclotomic value Phi_n(2) has a
  primitive prime divisor r with ord_r(2) = n.
hypotheses: n in the covered (large) range; primitive divisor means it divides
  no earlier term
holds-here: yes for Phi_{4p}(2) with p large (the H_even prime branch), and for
  every 2^(2k)+1 in Prop 4
status: asserted
bearing: underpins Maciejewski Prop 4 (Higgs-cubefree structure of H_even) and
  Conjecture 23; without it the geometric control of ord_r(2) = 4k fails
anchor: research/sources/maciejewski-bounded-box-subbarao-warren.full.md
contradicts: (none)
answers: whether-primitive-divisor-of-Phi4p-2-exists
```
