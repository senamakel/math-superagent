# G2 — formalisation status of the mechanical-word factor representation

Node `pe1006-psi/G2-mechanical-word-representation`, formalised in
`code/lean/pe1006_psi_G2_mechanical_word_representation-1f79c34f.lean`.

## Statement as formalised (**corrected slope**)

The literal node text "slope a = F(n-1)/F(n)" was refuted by the run's refuter
(`code/refute/G2-slope-refutation.md`): F(n-1)/F(n) → 1/phi is the slope of the
*complement* word and produces factors containing `11`, which never occur in
the Fibonacci word.  The corrected slope is `fib(n)/fib(n+2)` — the continued
fraction convergents to `1/phi^2 = (3-sqrt5)/2` (the characteristic Sturmian
slope of the Fibonacci word) — with hypothesis `k < fib(n+2)` (the run's
"F(n) > k" under `|S_n| = fib(n+2)`).  Every implementation
(`code/mech/mech_psi.py`, `Problem1006.lean mechSlope`, `check_slope.py`)
uses this corrected slope and verifies it for k = 1..100.

Binder-by-binder in Lean (`PE1006G2`):

- `slope n := fib n / fib (n+2)` — the rational slope, `a`.
- `intercept n m := -m·a` — the cut points `frac(-m·a)` of the node.
- `mechDigit a x j := ⌊x+(j+1)a⌋ - ⌊x+ja⌋` — `digit_j(x)`, `j = 0..k-1`.
- `mechWord n k m : Fin k → ℤ` — the mechanical word of intercept `m`, length `k`.
- `mechFactorSet n k = {w | ∃ m ≤ k, w = mechWord n k m}` — the k+1 words.
- `FactorSet k` — the length-k factors of the infinite Fibonacci word.
- `mech_reproduces_factors k n (h : k < fib (n+2)) : mechFactorSet n k = FactorSet k`
  — the node's main identity, **gapped**.
- `mech_set_card k n (h : k < fib (n+2)) : (mechFactorSet n k).ncard = k + 1`
  — the count half, **gapped**.

## What the kernel proved (sorry-free shell): `status: formalised`

`lean_check` on the shell file
`code/lean/pe1006_psi_G2_mech_shell-1f79c34f.lean` (companion of the node
file, which keeps the gapped deep identity) **passes** — `outcome: verified`,
no `sorry`, no cited axioms; the four declarations depend only on `propext`,
`Classical.choice`, `Quot.sound`:

- `slope_mem_Icc n : 0 ≤ slope n ∧ slope n ≤ 1`
- `mechDigit_nonneg a x j (ha0 : 0 ≤ a) : 0 ≤ mechDigit a x j`
- `mechDigit_succ_le a x j (ha0 : 0 ≤ a) (ha1 : a ≤ 1) : mechDigit a x j ≤ 1`
- `mechWord_binary n k m j (hj : j < k) : 0 ≤ mechWord n k m ⟨j,hj⟩ ∧ mechWord n k m ⟨j,hj⟩ ≤ 1`

Together these pin down the *object* the node quantifies over: the slope is in
`[0,1]`, every intercept is an exact rational (`ℚ`), every `floor` is an exact
integer (`Int.floor`), and every digit is in `{0,1}` — the node's exactness
remark ("every quantity is rational with denominator F(n)^2 or better, and
floor is exact-integer, checkable exactly not in floating point") holds by
construction over `ℚ` with no floats anywhere.

## The deep identity — NOT formalised (gap)

`mech_reproduces_factors` and `mech_set_card` are the Sturmian rotational-factor
theorem.  Mathlib has no Sturmian-words library, so this is recorded under
`namespace Cited` as an axiom with its sources (Lothaire/Berstel Ch. 2 §2.1.1
p. 89 Morse–Hedlund; Perrin–Restivo Thm 1: all mechanical words of one slope
share their factor sets), and the two theorems end in `sorry`.  `lean_check`
reports them as depending on `sorryAx` and `PE1006G2.Cited.mechanical_factors`
— they are **not** formalised and no claim below marks them so.

An exact-terminal oracle check (kernel-computed, `native_decide`) reproduces
the refutation table's corrected digit row: for `a = 2/5` the digits
`0,0,1` give the factor `001`.

## What would discharge the gap

A proof that the length-k factors of the characteristic Sturmian word of slope
α are exactly the k+1 mechanical words of slope α with intercepts `-m·a`
(whenever the rational approximant `a` has denominator `q > k`).  That is a
standard result in Sturmian-word theory (Berstel's Proposition: all mechanical
words of one slope share their factor set; the factors of slope-α mechanical
words are exactly the shorter mechanical words).  It needs a Sturmian-word
development in Mathlib that does not exist here; a first move would be to
formalise the three equivalent definitions of Sturmian words
(`code/lean/Lib/sturmian_three_equivalent_definitions.lean` already sketches
them under `Cited`) and bridge the finite-`S_n` family to the limit word.

```claim
id: g2-mech-shell-exact-binary
statement: For the corrected slope a = fib(n)/fib(n+2), every digit
  digit_j(x) = floor(x+(j+1)a) - floor(x+ja) of a mechanical word of intercept
  x = -m·a lies in {0,1}, the slope lies in [0,1], and the whole construction
  is carried out in the exact fields ℚ/ℤ (floor is Int.floor, never float).
  Hence the node's exactness remark holds, and the k+1 mechanical words are
  honest binary words of length k (before even asserting they equal the factors).
hypotheses: k,n,m,j ∈ ℕ with j < k; a = fib(n)/fib(n+2).
holds-here: yes — this is the corrected slope verified against the factor set
  for k = 1..100 in code/mech/mech_psi.py.
status: formalised
formalisation: code/lean/pe1006_psi_G2_mech_shell-1f79c34f.lean
bearing: pins down the object the node's deep identity quantifies over — the
  exact, binary mechanical word construction — so the remaining gap is purely
  the Sturmian factor identity.
anchor: research/notes/g2-formalisation-status.md
```

```gap
id: g2-mech-reproduces-factors
lemma: For every n with k < fib(n+2), mechFactorSet n k = FactorSet k — the
  k+1 mechanical words (exact, binary by g2-mech-shell-exact-binary) are
  exactly the length-k factors of the infinite Fibonacci word.
status: open
next: formalise Sturmian-word basics (three equivalent definitions; all
  mechanical words of one slope share factor sets; factor set of slope-α =
  shorter mechanical words) and bridge the finite S_n family to the limit.
  Source: Berstel, Recent Results on Sturmian Words Thm 1.1/2.1; Perrin–Restivo
  Thm 1.
```

```gap
id: g2-mech-set-card
lemma: For every n with k < fib(n+2), (mechFactorSet n k).ncard = k + 1 — the
  k+1 mechanical words are distinct, matching the k+1 distinct factors.
status: open
next: follows from the factor identity and the Sturmian factor-complexity
  count p(k) = k+1 (Lothaire Ch. 2 §2.1.1, Morse–Hedlund); prove either the
  count directly or via g2-mech-reproduces-factors + fib_subword_count (G1).
```
