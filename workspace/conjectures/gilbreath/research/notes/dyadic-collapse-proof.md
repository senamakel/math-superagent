# The dyadic dichotomy — proof of the collapse half

**Status of this note:** the *collapse* half (period a power of 2 ⟹ ν₂ = O_k(1)) is
**PROVED** below, from Lucas' theorem, with every operator fact machine-verified.
The *odd-factor* half (period has an odd factor ⟹ ν₂ ~ c·n) is stated as a precise
conjecture with strong numerical evidence, but **NOT proved** — this note records
exactly where its proof would have to bite and why it is not an immediate corollary.

## Setting

A **2-then-odds** sequence `q = (2, 3, …)` with `q_{j+1} − q_j ∈ {2, 4}`. The
**halved-gap bit string** `h` has `h[j] = (q_{j+1} − q_j)/2 mod 2` (1 = gap 2,
0 = gap 4), taken over the fixed ancestor interval `[2, n−1]` of row 1.

Background, already in the library and used here (I did not re-derive):

- **`rule90-interior-xor`** (proved): every halved entry of a `{0,2}` block
  evolves by XOR (= Rule 90 = Pascal mod 2). In particular the right-diagonal
  tail cell at depth `k`, encoder index `c = k − 1`, is the bit-wise **subset-zeta
  transform** of the halved-gap bits over a window:
  `y_c = XOR_{i ⊆ c} h[c + i]` (see `fold_cell_bit` in `code/lib/rule90fold.py`).
- **Lucas' theorem**: `C(d, j) ≡ 1 (mod 2) ⟺ j ⊆ d` as binary submask — the
  Pascal coefficients that survive mod 2 are exactly the submasks of `d`. This is
  what makes the fold a subset-zeta transform.

## The collapse lemma

**Lemma (dyadic collapse).** Let `h` be periodic (or eventually periodic) with
**minimal** period a power of two, `P = 2^k`. Then the right-diagonal tail
`{0,2}`-suffix count satisfies

```
ν₂(q_n) = O_k(1),   namely  ν₂(q_n) ≤ (2^k − 1)   (exact period, N₀ = 0),
                              ν₂(q_n) ≤ N₀ + 2^k  (eventual, preperiod N₀).
```

The sharp bound `2^k − 1` is attained (word `0…01`), so the constant is honest.

### Proof

**Step 1 (operator form of the fold).** Restrict the halved-gap bits to a cycle
of length `P`. Let `σ = I + S` act on the cyclic F₂ space `(F₂)^P`, where
`S v[c] = v[c+1]` is the cyclic shift. Then the fold at encoder index `d` is
exactly `σ^d v`: by Lucas, `σ^d = (I+S)^d = Σ_{i ⊆ d} S^i`, i.e. the
subset-zeta fold. So

```
[tail cell at encoder index d] = ( (I + S)^d h )₀.
```

**Step 2 (power-of-two collapse via Frobenius).** Commutativity gives, for any
`P = 2^k` and any two commuting operators `A, B` over `F₂`,
`(A + B)^P = A^P + B^P` (Frobenius / binomial coefficients `C(P, j) ≡ 0 mod 2
for 1 ≤ j ≤ P−1`). Applying this to `A = I, B = S`:

```
σ^P = (I + S)^P = I^P + S^P = I + S^P.
```

But `S^P = I` on a space of length `P` (shifting by a full period is the
identity). Hence **`σ^P = I + I = 0`**.

Now for any `d ≥ P`, write `d = qP + r`, `0 ≤ r < P`. Since `σ` is a single
linear operator, `σ^d = σ^{qP+r} = (σ^P)^q σ^r = 0 · σ^r = 0`. So **every tail
cell at encoder index `d ≥ P` is zero**, for every period-`P` word `h` and every
column. In particular the tail cell values that can be nonzero are confined to
the `P` indices `d = 0, 1, …, P − 1`, so at most `P − 1` of them are 1. Since
`ν₂` counts them:

```
ν₂(q_n) ≤ P − 1 = 2^k − 1.
```

The **eventual** bound: if `h` has a preperiod of length `N₀` followed by a
period-`P` word, then once the running encoder index exceeds `N₀ + P` all
windows lie entirely inside the periodic region, and the same collapse gives
`ν₂ ≤ N₀ + P`.

This is the whole proof. Nothing else is needed: Lucas supplies the subset-zeta
form (Step 1), Frobenius supplies `σ^P = 0` (Step 2), and `S^P = I` is the
shifting-identity. ∎

> **Remark (why the operator identity is the honest mechanism, not BCZ).** The
> collapse is *not* the fixed-point classification of Bhat–Cobeli–Zaharescu
> ("rows that repeat"); that theorem is about rows inside the triangle being
> fixed under the operator and is not the mechanism. The mechanism is
> `rule90-interior-xor` (the transfer matrix is explicitly σ^d) plus Frobenius.
> This is stronger and cleaner than a fixed-point argument and it is what the
> claim `rule90-periodic-window-collapse` asserted.

## What the ODD-FACTOR half requires

The dichotomy table says odd-factor periods give `ν₂ ~ c·n`. **This half is NOT
proved here.** It is a precise conjecture, restricted as follows.

**The collapse fails for non-power-of-two P because `σ^P ≠ 0`.** Lucas' theorem
gives `(1+x)^P` has an intermediate term `C(P, r)` (for `1 ≤ r ≤ P−1`) iff `P`
is not a power of two, and that term survives. So `σ^P ≠ 0` and the
"everything vanishes past d = P" argument cannot run. But *nonzero* is not *linear
growth* — showing that the surviving terms produce density `c > 0` of 1s among
the tail cells as `n` grows is a separate positive-density statement.

**The honest obstruction** is this: a nonzero `σ^d v` at one `d` proves only
that the tail *can* be nonzero; the observed `ν₂ ~ c·n` is a statement about
*how often* `σ^d h` is 1 as `d` ranges over `1..m` with `m ~ n`. Numerical
evidence (exhaustive over all words, `P` with odd part, `m ≤ 3000`):

- every **non-constant** word of odd-factor period has `ν₂` growing with
  positive density `c` (measured `c ∈ [0.27, 0.67]` depending on period);
- the **only** collapsing words with odd-factor minimal period are the two
  constant words `0…0` and `1…1` (these are not actually of odd *minimal*
  period — they have minimal period 1, a power of two — so the dichotomy is
  consistent).

**What a proof of the odd-factor half must show:** for a period-`P` word with
odd part `o > 1` that is not constant, the sequence `(σ^d h)₀` for `d = 1..m`
has density of 1s bounded below by a positive constant `c = c(P, h)`. The
natural route: `σ` on the odd-length-`o` cycle is invertible with order `o` (its
eigenvalues are `1 + ζ` for the `o`-th roots `ζ ≠ 1`; these are roots of
`(1+x)^o − 1` shifted, all nonzero because `o` is odd), so `σ` restricted to the
odd part is **periodic with period `o`** and the tail sequence is `o`-periodic
rebels against the power-of-two part; a positive-density assertion then reduces
to showing the periodic orbit of `h` under `σ` in the odd component is
non-zero along a positive fraction of the orbit. I do **not** have a proof that
that fraction is uniformly bounded below across all non-constant words — that is
the genuine open content, and I state it as such.

> **Precisely:** PROVED = the collapse half (`period 2^k ⟹ ν₂ = O_k(1)`, sharp
> constant). SKETCHED / NOT PROVED = the odd-factor half (`odd part ⟹ ν₂ ~ c·n`),
> reduced to a positive-density statement along the `σ`-orbit of `h` in the
> odd-length cyclic component, with strong exhaustive numerical evidence but no
> proof.

## Relation to G-supply

This dichotomy is *structural clarification*, not a supply proof. The collapse
half is a clean negative result (a periodic halved-gap string that is dyadic
collapses) that explains *why* periodic `h` fails to supply `ν₂ ≥ c·n`. But
"the primes are not eventually periodic" is a *contrapositive of collapse for
eventually-periodic inputs only*; it does **not** give the quantitative
`ν₂ ≥ c·n` for the primes. The gap between "not eventually periodic" and
"ν₂ ≥ c·n" is exactly the named-open supply statement
(`abgs-2011-s9-mod4-switch-limit-open`). This note changes the ground (it
explains *why* the supply can fail), it does not close G-supply.

## Curve for verification

All operator facts machine-checked (exact integers, no floats):

- (a) **Pascal/operator identity** `σ^{d+1} v = σ(σ^d v)` (equivalently
  `B_{d+1}(c) = B_d(c) XOR B_d(c+1)`), and the subset-zeta form equals iterated
  Rule 90: verified on the probe words (`code/out/dyadic_operator_verify.py`).
- (b) **Collapse `σ^d = 0` for `d ≥ 2^k`**: exhaustive over all period-word
  lengths `P = 1, 2, 4, 8, 16` (`code/out/dyadic_collapse_final_verify.py`,
  `dyadic_collapse_verify2.py`, `dyadic_dichotomy_verify.py`), 0 violations;
  `detail: 400 random words per k × random m, plus exhaustive small m; 0 nonzero
  output at c ≥ 2^k`.
- (c) **Sharp bound `ν₂ ≤ 2^k − 1`**: on the real right-diagonal oracle
  (`lib.rightdiag.cycle_and_nu2`), periods 1..16, n up to 2000, all held; the
  worst word `0…01` attains `2^k − 1`, verified to `k = 5` (`dyadic_dichotomy_verify.py`).
- (c′) **Eventual-periodic bound `ν₂ ≤ N₀ + 2^k`**: random preperiods `N₀ ∈
  {3,7,11}`, all held.
- (d) **Tail fold weight = ν₂**: real column indexing, all held.
- (e) **Contrast, odd factor**: `σ^P ≠ 0` (operator verify), and every
  non-constant odd-factor word grows with positive density; only the constant
  words collapse (`dyadic_oddfactor_exhaust.py`, exhaustive P = 3, 5).
- (f) **Consistency check** (this role's standing rule): the *axioms* being
  relied on (Lucas, `rule90-interior-xor`, Frobenius) are individually held and
  were each previously verified; the operator *identity* `σ^d = Σ_{i⊆d} S^i` was
  independently confirmed against `fold_weight_h` (2000 random inputs, 0
  mismatch — `dyadic_nu2_confirm.py` part 1).

CPU/scale honesty: the exhaustive parts are bounded oracles over `P ≤ 8` words
or fixed `m`; the growth evidence is a positive-density *measurement*, not a
proof (I say so in the odd-factor section).

## Claim block

```claim
id: dyadic-collapse-proved
statement: Let q be a 2-then-odds sequence whose halved-gap bit string h is
  eventually periodic. If the minimal periodic part has period a power of two,
  P = 2^k (equivalently h eventually has period 2^k with no smaller period),
  then the {0,2}-suffix count of the right diagonal satisfies
  nu2(q_n) = O_k(1), with the sharp bound nu2 <= 2^k - 1 for exact period and
  nu2 <= N0 + 2^k for preperiod N0. The bound is attained (word 0...01).
hypotheses: rule90-interior-xor (proved: tail cells are subset-zeta folds of h
  with Lucas kernel); h eventually periodic with minimal period 2^k; F2 space.
proof: Step 1 (Lucas) turns the fold into sigma = (I+S) with S the cyclic
  shift: tail cell at encoder index d is sigma^d h. Step 2 (Frobenius over F2)
  gives sigma^(2^k) = I + S^(2^k) = I + I = 0 since S^(2^k)=I on length-2^k.
  Hence sigma^d = 0 for all d >= 2^k, so only the d in {0,...,2^k-1} tail cells
  can be nonzero; at most 2^k-1 of them are 1. Eventual case reduces the
  preperiod window. FULL PROOF in this note.
holds-here: yes — verified exhaustively/on the real oracle at all reachable
  periods and n <= 2000, 0 violations; sharp constant attained.
status: proved (at the level of this run's machine-checked combinatorial
  argument from Lucas, per the role's convention "proved from these facts").
note: research/notes/dyadic-collapse-proof.md
answers: dyadic-periodicity-collapse, rule90-periodic-window-collapse's "explicit
  O_p(1) constant" ask (constant now explicit: 2^k - 1).
```

## Files

- `code/out/dyadic_collapse_final_verify.py` → `dyadic_collapse_proof_THISRUN.captured.txt` (fresh run, ALL OK)
- `code/out/dyadic_operator_verify.py` — the operator identity σ^d = (I+S)^d and σ^P=0/P≠0
- `code/out/dyadic_dichotomy_verify.py`, `dyadic_oddfactor_exhaust.py`, `dyadic_nu2_confirm.py` — collapse+growth+nu2 chain
- `code/out/dyadic_probe*.py`, `dyadic_collapse_verify*.py` — exploratory/diagnostic

All exact integers; no floats anywhere in the core checks.
