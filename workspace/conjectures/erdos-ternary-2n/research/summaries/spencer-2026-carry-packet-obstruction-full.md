# Spencer, "A Carry-Packet Obstruction for Powers of Two with Ternary Digits in {0,1}"

Source: Zenodo record https://zenodo.org/records/20355936 (v1, 23 May 2026), author Michael Spencer.
Full text: `research/sources/spencer-2026-carry-packet-obstruction-full.full.md`.
**Status: a claimed proof of Erdős's conjecture, not peer-reviewed (Zenodo preprint, 0 citations). Assessed here as UNSOUND at its completeness step.**

## What it claims

A complete proof that the only powers of two whose base-3 expansion uses only digits
`0,1` are `1, 4, 256` — i.e. it claims to *prove* the very conjecture this run is asked
to attack. It works on the run's own directed line (a symbolic carry invariant on
`x ↦ 4x` / `x ↦ 2x` in base 3), which is exactly why the run must hold and assess it.

**Structure.**
1. Parity reduction: odd powers of 2 end in ternary digit 2, so a nontrivial candidate
   is `2^k = 4^e`.
2. Rail equivalence: `R_e = (4^e−1)/3`, and `4^e = 3R_e+1` appends a final ternary 1, so
   `4^e ∈ A ⇔ R_e ∈ A` (A = digit-{0,1} words).
3. Carry mechanism: `4m = m + 3m`, i.e. quadrupling = ternary self-overlap with a
   one-place-left shift. A digit 2 appears when two unresolved contributions collide.
4. Lemma 6.1 (length-3 local carry law): among 3-digit ternary words, those whose
   quadruple has no digit 2 are exactly `000, 001, 010, 021, 100, 101, 210`.
5. Conclude the only "primitive isolated artifacts" are (up to ternary scaling) the
   singleton `1` and the collapse `21`; the word `101` is a separated composite `1+3²`.
6. Reduced-cofactor invariant: `core_{2,3}(N) = N/(2^{ν₂N}3^{ν₃N})` is preserved by
   triadic scaling; carries a non-dyadic cofactor (5 for `101`-type, 7 for `21`-type).
7. The only "anchored" packet that is both carry-admissible and dyadically pure is
   `2101_3 = 64`, giving `64·4 = 256 = 100111_3`.
8. Non-repetition: a separated reuse has value `64(1+3^s)`; Lemma 9.1 shows `1+3^s` is
   not a power of 2 for `s ≥ 2`. Only `s=1` (ratio 1:3, required by quadrupling) works.
9. **Theorem 12.1:** if `q` is a power of 2 and `4q ∈ A`, then `q = 1` or `q = 64`.
10. **Theorem 13.1:** the powers of two in A are exactly `1, 4, 256`.

## What checks and what does not

**Arithmetic examples all verify by hand.** `2101_3 = 54+9+1 = 64`; `64·4 = 256 =
100111_3`; `100111_3·4 = 1024 = 1101221_3` (729+243+27+18+6+1), which contains a 2;
`101_3·4 = 40 = 1111_3`; `10101_3·4 = 364 = 111111_3`; `021_3·4 = 28 = 1001_3`;
`210_3·4 = 84 = 10010_3`. **Lemma 9.1 is correct:** for even `s ≥ 2`, `3^s ≡ 1 (mod 8)`
so `1+3^s ≡ 2 (mod 8)` and `> 2` ⇒ not a power of 2; for odd `s > 1`, `1+3^s = 4·(odd>1)`
has a non-dyadic odd factor.

**The completeness step of Theorem 12.1 is unsound.** The proof reduces the whole
question to a *length-3 local* classification (Lemma 6.1), then asserts — without an
induction — that *every* carry-compatible structure of arbitrary length decomposes into
isolated copies of the primitive artifacts `1` and `21` (up to scaling). But:

- Lemma 6.1 classifies only 3-digit words. A word of arbitrary length whose quadruple is
  digit-{0,1}-clean is not a concatenation of independent 3-digit blocks, because carries
  propagate *across* block boundaries.
- The paper itself concedes this: **Remark 6.3** says the block `20` is "not an
  independent artifact" but "only a carry-propagation segment inside a larger coupled
  packet." That is precisely to say carries couple blocks. Yet no argument controls all
  coupling configurations of arbitrary length.
- The canonical packet `2101_3 = 64` is itself a *coupling* of primitive segments that the
  length-3 primitive classification does not generate — it is found by inspection, not by
  the exhaustion. So the exhaustion at length 3 cannot rule out *other* longer couplings
  that also multiply through cleanly. There is no argument that `2101_3` is the only
  length-4-or-longer clean coupling.

In short: Theorem 12.1 is, in its content, essentially the conjecture restricted to the
quadrupling step (it says the only `q` a power of 2 with `4q` digit-{0,1}-clean are
`1, 64` — which, given the conjecture is true, is consistent with all data and proves
nothing until the classification is complete). The classification is the whole difficulty,
and it is asserted, not proved.

## Assessment

A **dead end to record, not a route to adopt**: the claimed proof does not establish the
conjecture. Its individual invariants (reduced cofactor, separation cofactor) are sound and
reusable, but the central "exhaustive classification of primitive carry packets" is carried
out only at length 3 and extended to all lengths by assertion. This is the same class of
error GOAL.md warns about — a small-case correctness presented as a global theorem.

The three witnesses `n = 0, 2, 8` are all consistent with this construction (1 = the
trivial packet, 4 = singleton `11_3`, 256 = `64·4`), so the falsification oracle
(force a 2 at n=8, or not) does NOT refute it — the failure is a missing induction, not a
wrong witness. That makes it harder to catch and exactly why it is worth recording.

```claim
id: SPENCER-CARRY-PACKET-UNSOUND
statement: Spencer 2026 claims to prove Erdos's conjecture (powers of 2 in base 3
  with digits {0,1} are exactly 1, 4, 256) by a carry-packet admissibility
  obstruction. The individual invariants (core_{2,3} reduced cofactor preserved by
  3-scaling; 1+3^s not a power of 2 for s>=2) are correct, but the proof is
  UNSOUND: Theorem 12.1 rests on classifying primitive carry packets exhaustively
  at length 3 (Lemma 6.1) and asserting without an induction that arbitrary-length
  clean words decompose into isolated copies thereof, while carries couple across
  block boundaries (its own Remark 6.3). The canonical packet 2101_3=64 is itself a
  coupling not generated by the primitive exhaustion, so other longer couplings are
  not ruled out. The classification is the whole difficulty and is asserted.
hypotheses: none that rescue the argument -- the completeness step is missing.
holds-here: yes -- the analysis of the proof being unsound at its completeness
  step is this-run verified against the full text (the claim IS the assessment of
  Spencer, not a theorem he states).
status: checked -- the arithmetic of the preprint re-verified independently in
  THIS run, hand first and then MACHINE-EXECUTED (code/out/spencer_verify.py,
  capture code/out/spencer_verify.captured.txt, EXIT_CODE=0, ALL PASS): Lemma
  6.1 list complete over all 27 three-digit words and each quadruple; Lemma 9.1
  (no s in [2,40] with 1+3^s a power of 2) by mod-8 even / odd-factor odd; all
  example quadruples and reduced cofactors core(101_3=10)=5 (01-type) and
  core(21_3=7)=7 (21-type) confirm, preserved under 3-scaling; canonical packet
  2101_3=64 and 256=100111_3 confirm (100111_3*4 = 1101221_3 contains a 2).
  The completeness gap of Thm 12.1 is real and is the
  assessment: the length-3 exhaustion does not generate the 4-digit canonical
  packet 2101_3=64 (found by inspection), and Remark 6.3 concedes carries couple
  across block boundaries, so longer couplings are not ruled out. Oracle
  n=0,2,8 all consistent -- the failure is NOT caught by the witness check, it is
  a missing induction.
bearing: a freshly-surfaced claimed proof on this run's exact directed line that
  must NOT be trusted or re-derived blindly. Its reduced-cofactor and
  separation-cofactor lemmas are reusable, but the packet-classification route to a
  proof requires the induction the preprint lacks. Predecessor: Zenodo 18111949
  (Dec 2025) is the same author's earlier carry-exclusion attempt on the same claim.
anchor: code/out/spencer_verify.captured.txt (program code/out/spencer_verify.py,
  EXIT_CODE=0, run this attempt); claim note code/out/spencer_verify_claim.md
```
