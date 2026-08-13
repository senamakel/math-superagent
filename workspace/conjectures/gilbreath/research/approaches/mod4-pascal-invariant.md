```approach
idea: The mod-4 Pascal linearization as an invariant machine — reframe the conjecture as a statement about the Sierpinski-gasket dot product of the prime gap sequence
mechanism: >
  Odlyzko's mod-4 linearization (d_{k+1}(n) ≡ d_k(n) + d_k(n+1) (mod 4) wherever
  d_k(n) is even) is already established (sourced, Odlyzko 1993 §2 eq.201, CHT
  Lemma 3.10). Iterating, d_k(1)/2 (mod 2) = Σ_{j=0}^{k-1} binom(k-1, j) ·
  (d_1(2+j)/2) (mod 2) — the parity of the halved second entry is the dot
  product of the (k-1)-st row of Pascal's triangle mod 2 (Sierpinski gasket)
  with the halved initial gaps. The conjecture A_k(1) ∈ {0,2} then becomes:
  for every k ≥ 1 this dot product is 0 or 1 (halved), which would require
  lifting the mod-2 parity to the actual value, tracking mod 2^t for t ≥ 1.

  The full invariant: work mod 2^t for t ≥ 1, lifting the Pascal iteration via
  the Lucas/Kummer structure for higher powers, obtaining d_k(1) =
  Σ binom(k-1, j) · d_1(2+j) with signs from the absolute-value operator's
  branch choice — the sign pattern being itself a function of the Pascal
  structure.

status: refuted
killed-by: >
  The free linearization does NOT lift to mod 2^t. Since |a−b| = a+b − 2·min(a,b),
  the congruence |a−b| ≡ a+b (mod 2^t) holds iff 2·min(a,b) ≡ 0 (mod 2^t), i.e.
  iff the smaller entry is divisible by 2^{t−1}. Mod 4 (t=2) it always holds
  (min of two evens is even); mod 8 (t=3) it fails: |2−6| = 4 ≢ 0 (mod 8) while
  2+6 = 8 ≡ 0 (mod 8). So mod 4 is the ceiling of the free lift, and mod 4
  conflates 0 with 4 and 2 with 6 — exactly the failure values the conjecture
  must exclude. The free congruence level therefore cannot certify A_k(1) ∈
  {0,2}. CHT (Lemma 3.10) confirm the mod-2 parity formula is the clean level
  and explicitly state they "will not use Lemma 3.10 directly" — it rules out
  long 0-blocks and {0,d}-blocks for even d but "does not easily reduce the
  likelihood of long {0,d}-valued blocks for odd d", and it gives only parity,
  never the exact {0,2} value. The sign/branch structure the candidate flags as
  "the real work" is exactly the obstruction, and no source resolves it.
precedent: >
  - https://arxiv.org/abs/2607.08712 (CHT Lemma 3.10 parity formula; §4 Remark
    4.5 exponential threshold; the paper does not use Lemma 3.10 to control
    {0,2}/value, only parity)
  - https://www-users.cse.umn.edu/~odlyzko/doc/arch/gilbreath.conj.tex (Odlyzko
    1993 §2, mod-4 linearization, its eq. 201 origin)
holding-claims: larger
  mod4-linearization, odlyzko-mod4-linearization (the mod-2/4 side is real)
falsifies: >
  That iterating the Sierpinski dot product mod 2^t, t ≥ 3, recovers the full
  halved value d_k(1)/2. The a=2,b=6 counterexample shows the mod-8 lift fails,
  so any invariant machine resting on mod-2^t (t≥3) freedom is void.
buy: >
  Nothing for the conjecture as stated: parity of d_k(1)/2 is trivially 0 or 1
  (it is always one of them), and mod 4 cannot separate {0,2} from {4,6,...}.
  The approach would need a completely separate argument for the exact value.
first-step (retired): >
  The proposed program (compute d_k(1)/2 both ways and study the Sierpinski
  autocorrelation) would only re-confirm parity; it cannot reach the value.
  Not worth running.
```

Fenced claim:

```claim
id: mod-lift-obstruction
statement: The absolute-difference operator <a,b> -> |a-b| satisfies |a-b| = a+b - 2min(a,b), so the congruence |a-b| ≡ a+b (mod 2^t) holds iff min(a,b) ≡ 0 (mod 2^(t-1)). It holds for all even a,b mod 4, but fails mod 8 (|2-6|=4 ≢ 0 mod 8). Hence mod 4 is the ceiling of the free linearization, and mod 4 conflates the value 0 with 4 and 2 with 6 — so no free mod-2^t Pascal/invariant machine can certify A_k(1) ∈ {0,2}.
hypotheses: a,b even non-negative integers; iterated absolute differences d_k(n).
holds-here: yes
status: proved (elementary algebra, hand-verified; consistent with CHT Lemma 3.10 being parity-only)
bearing: refutes the central lift of the mod4-pascal-invariant approach; the {0,2}-value beyond parity is not reachable by the free congruence, which is why the value question is genuinely separate.
anchor: research/approaches/mod4-pascal-invariant.md
```
