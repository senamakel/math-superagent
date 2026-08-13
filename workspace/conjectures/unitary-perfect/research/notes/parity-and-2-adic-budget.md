# Parity and the 2-adic budget

Two facts this run starts from rather than establishes. Both are elementary,
both are proved below, and both are checked against the five known unitary
perfect numbers. Re-deriving either is not a result.

Throughout, `σ*(n) = Π_{p^a || n} (p^a + 1)`, and `n` is unitary perfect iff
`σ*(n) = 2n`.

## Every unitary perfect number is even

This is Subbarao–Warren (1966). The proof is short enough that the workspace
should hold it rather than cite it.

Suppose `n` is odd and unitary perfect, with `ω = ω(n)` distinct prime factors.
Every prime power `p^a || n` has `p` odd, so `p^a + 1` is even. Hence
`2^ω | σ*(n) = 2n`. Since `n` is odd, `v2(2n) = 1`, so `ω ≤ 1`.

- `ω = 0` gives `n = 1`, and `σ*(1) = 1 ≠ 2`.
- `ω = 1` gives `n = p^a` and `σ*(n) = p^a + 1 = 2p^a`, so `p^a = 1`,
  contradicting `p^a > 1`.

So there is no odd unitary perfect number, and every unitary perfect number is
`n = 2^a · m` with `a ≥ 1` and `m` odd. ∎

## The 2-adic budget identity

Write `n = 2^a · Π_i p_i^{e_i}` with the `p_i` odd and distinct, `a ≥ 1`. Then

```
σ*(n) = (2^a + 1) · Π_i (p_i^{e_i} + 1)     and     2n = 2^{a+1} · Π_i p_i^{e_i}.
```

`2^a + 1` is odd and every `p_i^{e_i}` is odd, so taking `v2` of both sides of
`σ*(n) = 2n` gives

```
Σ_i v2(p_i^{e_i} + 1)  =  a + 1.
```

Each term on the left is at least 1, so immediately

```
ω(odd part of n)  ≤  a + 1,
```

with equality exactly when every odd component satisfies
`v2(p_i^{e_i} + 1) = 1`, i.e. `p_i^{e_i} ≡ 1 (mod 4)`.

This is the exact form of the constraint that arXiv:2605.20475 uses as its
"2-adic budget overshoot" filter: the power of 2 in `n` is not free, it is a
budget of exactly `a + 1` that the odd components must spend precisely, and each
component of the form `p^e ≡ 3 (mod 4)` spends at least 2 of it.

## Checked against the witness set

All five known unitary perfect numbers, from
`code/out/known_five_verified.captured.txt`:

| `n` | `a` | `ω(odd)` | `Σ v2(p^e+1)` | `a+1` | equality in `ω ≤ a+1` |
| --- | --- | --- | --- | --- | --- |
| 6 | 1 | 1 | 2 | 2 | no |
| 60 | 2 | 2 | 3 | 3 | no |
| 90 | 1 | 2 | 2 | 2 | **yes** |
| 87360 | 6 | 4 | 7 | 7 | no |
| 146361946186458562560000 | 18 | 11 | 19 | 19 | no |

The identity is exact in every case. Equality in the corollary holds for exactly
one of the five, `n = 90 = 2 · 3^2 · 5`, and it is precisely the one whose odd
components `3^2 = 9` and `5` are both `≡ 1 (mod 4)` — which is what the equality
condition predicts, not a coincidence to note.

```claim
id: unitary-perfect-2-adic-budget
statement: Every unitary perfect number is even (Subbarao-Warren 1966), and for
  n = 2^a * prod_i p_i^{e_i} unitary perfect with p_i odd and distinct, a >= 1,
  the identity sum_i v2(p_i^{e_i} + 1) = a + 1 holds exactly. Consequently
  omega(odd part of n) <= a + 1, with equality if and only if every odd unitary
  component satisfies p_i^{e_i} = 1 mod 4. Verified on all five known unitary
  perfect numbers 6, 60, 90, 87360 and 146361946186458562560000, where the
  identity is exact in every case and equality in the corollary holds for
  exactly n = 90, the unique one of the five whose odd components 9 and 5 are
  both 1 mod 4.
hypotheses: none beyond n unitary perfect; sigma* is the sum of unitary
  divisors, multiplicative with sigma*(p^a) = p^a + 1
holds-here: yes. Both parts are proved outright, not conditionally, and both
  are run against the full witness set rather than asserted
status: proved
bearing: fixes a >= 1 so the seed factor 2^a + 1 is always present, and makes
  the power of 2 an exact budget of a + 1 that the odd components must spend,
  each component that is 3 mod 4 spending at least 2. This is the elementary
  form of the 2-adic budget overshoot filter in arXiv:2605.20475. It bounds
  omega above by a + 1; the useful open direction is a lower bound on a in
  terms of omega, or the impossibility of a residue class of a
anchor: code/out/known_five_verified.captured.txt;
  research/notes/parity-and-2-adic-budget.md
source: operator-computation
```
