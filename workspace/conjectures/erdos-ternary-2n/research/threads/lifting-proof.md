```thread
question: Is the 2-to-1 lifting of A_k provable via LTE, giving |A_k| = 2^(k-1) unconditionally?
status: dead — PROVED unconditionally (ternary-lifting-theorem)
rests-on: ternary-sieve-count-doubles, SIEVE-EXACT, SAYE-2, SAYE-3
blocked-by: none — the theorem was proved, not blocked; superseded by the Lean
  formalisation and DH-1 × Lagarias directions
result: The theorem is proved via the three-lemma argument in code/out/lifting_theorem.md.
  |A_k| = 2^(k-1) for all k. The sieve never closes.
next: superseded by Lean formalisation (lean-formalization) and DH-1 × Lagarias (dh1-gap)
```

# Proving the 2-to-1 lifting

## The claim to prove

`A_k = { r mod 2·3^(k-1) : low k ternary digits of 2^r mod 3^k avoid 2 }`.

Data (`code/out/sieve_Ak.captured.txt`, `code/out/sieve_cannot_close.md`,
and the librarian's own derivation in `research/threads/sieve-dynamics.md`):
`|A_k| = 2^(k-1)` for every k = 1..26, computed by lifting. **Directive: k=26
used 333s and 2.1 GiB; no more sieving by materialising A_k as a set.** Each
class in `A_k` lifts to three candidates in `A_{k+1}`, and exactly two survive.

## The bijective-structure derivation (librarian, elementary)

`2` has order `φ(3^k) = 2·3^(k-1)` mod 3^k (primitive root — LAG-1, SAYE-2).
So `Φ_k : r mod 2·3^(k-1) ↦ 2^r mod 3^k` is a bijection onto `(Z/3^k)^×`.
`S_k = { low k digits in {0,1} }`; power residues are units, and a unit's low
digit is 1 (never 0), so the attainable patterns are: low digit 1, other k−1
digits each in {0,1} — exactly `2^(k-1)` patterns. Bijection gives
`|A_k| = 2^(k-1)` exactly. Drop the newest digit: each class has exactly two
preimages (append 0 or 1 to the pattern), both units, both hit by a unique
exponent — so the extension map `A_{k+1} → A_k` is exactly 2-to-1.

This is a *proof* of the count once `Φ_k` bijectivity is formalised (it
depends only on the primitive-root order, which is proved in LAG-1/SAYE-2). It
does not need the LTE quotient c at all.

## The alternative LTE sketch (from the operator; needs the c-check)

Adding `j·2·3^(k-2)` multiplies `2^r` by `(2^{2·3^(k-2)})^j`. If
`v_3(2^{2·3^(k-2)} - 1) = k-1` with quotient c ≢ 0 (mod 3), then the three
lifts give upper digits {d, d+c, d+2c} mod 3, exactly one equal to 2 — so
exactly two survive. This is a second, independent route to the same theorem
(LTE on base 4, whose order mod 3^k is 3^(k-1)).

## What must be checked before this is "proved"

1. `v_3(2^{2·3^(k-2)} - 1) = k-1` exactly (LTE on base 4) — for k = 2..12 it is
   machine-verifiable; the run should do it.
2. The quotient `c = (2^{2·3^(k-2)} - 1)/3^(k-1)` satisfies `c ≢ 0 (mod 3)`.
3. The digit-shift step: carry analysis into the top digit — write it down
   carefully.
4. Whether the bijection proof (which is immediate and doesn't need LTE) and
   the LTE proof agree — they should; cross-check.

## Status

- Data: checked, exact, k = 1..26 (operator; `code/out/sieve_lift.captured.txt`).
- Bijection derivation: **completed proof**, no LTE needed. The map
  `Φ_k : r mod 2·3^(k-1) ↦ 2^r mod 3^k` is a bijection onto the units (2 is a
  primitive root mod 3^k, order φ(3^k), LAG-1/SAYE-2). Units' low digit is 1,
  so the attainable length-k {0,1} patterns are those with low digit 1:
  exactly 2^(k-1). Each length-k pattern extends to length k+1 in exactly two
  ways (new digit ∈ {0,1}), both units, both hit by a unique exponent — so
  `A_{k+1} → A_k` is exactly 2-to-1 and surjective. This is complete and needs
  no carry analysis.
- LTE mechanism: the formula `2^{2·3^(k-2)} = 4^{3^(k-2)} ≡ 1 + c·3^(k-1)
  (mod 3^k)`, c ≢ 0 mod 3, follows from LTE (v_3(4^t − 1) = 1 + v_3(t) at
  t = 3^(k-2)), so conditions 1–2 hold by theorem. Condition 3 (carry into the
  k-th digit when adding c·3^(k-1)·x to x) is **not automatic** and is exactly
  why the bijection proof is preferred: it avoids the carry issue entirely.
  Recorded as a fragile alternative, not the mechanism.