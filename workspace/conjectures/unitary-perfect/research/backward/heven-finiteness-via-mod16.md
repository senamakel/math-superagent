# Skeleton: finiteness of H_even via the mod-16 divisor route

The goal here is **Conjecture 6** of Maciejewski (arXiv:2605.20475): the set

```
H_even = { even m : every prime divisor of 2^m + 1 is 3-Higgs }
```

is finite. This is the single remaining branch after the in-box impostor
elimination (Theorem 2 / Corollary 3), and it closes the Subbarao–Warren
reduction **within the bounded box B at max a = 10000** — not the full
unitary-perfect-number conjecture, which the paper explicitly leaves open.
Everything below is scoped to that.

```skeleton
goal: Conjecture 6 (Maciejewski arXiv:2605.20475) — H_even = {even m : every
  prime divisor of 2^m+1 is 3-Higgs} is finite.
implies: Take any odd prime p with 2p ∈ H_even^prime = {2q : q odd prime,
  2q ∈ H_even}. By hb-prop4-structural, p ∈ P_3 (p is 3-Higgs, and it is the
  single prime factor of the odd part k = p). For p ≥ p0, G-H2 gives
  ω(Φ_{4p}(2)) ≥ C·log p, so G-H1 applies: some prime divisor r | Φ_{4p}(2)
  satisfies r ≡ 1 (mod 16). Since r is an odd prime, v2(r−1) ≥ 4 > 3; by the
  one-way implication in hb-defs-3higgs-heven, r ∉ P_3. Hence 2^{2p}+1 has a
  non-3-Higgs prime divisor, so 2p ∉ H_even — contradiction. Therefore
  H_even^prime ⊆ {2p : p odd prime, p < p0} is finite, and by
  heven-prime-case-reduction (|H_even| ≤ 4^|H_even^prime|), H_even is finite.
  (This is exactly the proof of the paper's Theorem 30; hb-thm30-conditional
  packages the implication (H1)∧(H2) ⇒ H_even finite, so the two open gaps
  below are the paper's (H1) and (H2) verbatim.)
status: live
rests-on: heven-prime-case-reduction, heven-two-mod-four, hb-prop4-structural,
  hb-thm30-conditional, hb-defs-3higgs-heven, bhv-primitive-divisor-theorem
```

### Maciejewski structural results — taken from the paper, not independently proved or checked here

These four reductions are Maciejewski's Theorems 7, Proposition 5, Proposition 4,
and the conditional form of Theorem 30. The run has **read them from the paper**
and catalogued them; **none is proved or checked independently here**. The
skeleton is therefore **conditional**: finiteness of H_even reduces to (H1) and
(H2) **given** the Maciejewski structural results. A conditional reduction is a
real result; claiming these as discharged without independent verification is
not. Evidence class for all four: `asserted` (from `heven-prime-case-reduction`,
`heven-two-mod-four`, `hb-prop4-structural`) or `asserted` (from
`hb-thm30-conditional`).

```gap
id: G-prime-case-reduction
lemma: H_even is finite iff H_even^prime = {2p : p odd prime, 2p ∈ H_even} is
  finite, and |H_even| ≤ 4^|H_even^prime|. (Maciejewski Theorem 7.)
status: conditional-on-paper
evidence: asserted (heven-prime-case-reduction, catalogued from paper-extraction.md)
```

```gap
id: G-mod4-restriction
lemma: H_even ⊆ {m ≡ 2 (mod 4)}; equivalently every m ∈ H_even has v2(m) = 1.
  (Maciejewski Proposition 5.)
status: conditional-on-paper
evidence: catalogued (heven-two-mod-four, heven-and-3-higgs-structure.md)
```

```gap
id: G-higgs-cubefree-structure
lemma: If m = 2k ∈ H_even with k odd, then every prime q | k is 3-Higgs with
  v_q(k) ≤ 3. In particular, on the prime branch k = p, membership 2p ∈ H_even
  forces p ∈ P_3. (Maciejewski Proposition 4.)
status: conditional-on-paper
evidence: catalogued (hb-prop4-structural, paper-extraction.md)
```

```gap
id: G-conditional-finiteness
lemma: If (H1) and (H2) hold, then H_even is finite. (Maciejewski Theorem 30.)
status: conditional-on-paper
evidence: asserted (hb-thm30-conditional, paper-extraction.md; unchecked)
```

### The two open gaps — these are what the run must attack

Given the Maciejewski structural results above, finiteness of H_even reduces
exactly to (H1) and (H2). These are the paper's own open conjuncts.

```gap
id: G-H1-divisor-mod16-existence
lemma: (H1) There exists an effective constant C > 0 such that for every odd
  prime p with ω(Φ_{4p}(2)) ≥ C·log p, at least one prime divisor r | Φ_{4p}(2)
  satisfies r ≡ 1 (mod 16).
status: open
next: tool_builder: for each odd prime p in a stated range (start 1213 ≤ p ≤ 2000,
  split L_p·M_p via the Aurifeuillean split `aurifeuillean-split`), partially
  factor Φ_{4p}(2) = L_p·M_p to a stated factor bound, record the count ω (exact
  only where fully factored) and the number of prime divisors r ≡ 1 (mod 16);
  then test the (H1) predicate for a fixed C (e.g. C = 1): report the smallest p
  with ω ≥ C·log p but zero r ≡ 1 (mod 16) divisors, or "none found up to bound"
  with what was left unfactored. Bounded: timeout 540, state range + unfactored
  cofactors. NOTE: hb-thm30-h1-not-chebotarev records that this is NOT derivable
  from effective Chebotarev even under GRH — it is a divisor-transference
  statement about one fixed integer.
```

```gap
id: G-H2-omega-log-growth
lemma: (H2) There exists an effective threshold p0 and the constant C from (H1)
  such that for every prime p ≥ p0, ω(Φ_{4p}(2)) ≥ C·log p.
status: open
next: tool_builder + theorem_prover. (a) Compute ω(Φ_{4p}(2)) exactly for odd
  primes p up to a bound where L_p·M_p fully factors (measure the feasible bound
  first), and check ω ≥ C·log p for a fixed C, reporting the smallest p that
  fails or "none up to bound". (b) Hand the theorem_prover the extraction:
  does the Stewart/Hong radical lower bound (hong-stewart-nonprimitive-bound:
  rad(2^{2p}+1) ≫ 2^{2p}/(non-primitive part), non-primitive part O(log(4p)))
  convert into ω(Φ_{4p}(2)) ≥ C·log p, using that every prime divisor r of
  Φ_{4p}(2) satisfies r ≡ 1 (mod 4p), hence r ≥ 4p+1? This is the "Stewart
  program" target the paper isolates for (H2); it is a stated open conjunct.
```

## Alternative single-lemma routes (not decomposed further here)

The paper names three divisor-level statements, each of which alone closes
Conjecture 6 and would collapse this skeleton to one gap:

- **Conjecture 29** (`hb-c29-divisor-mod16`): proportional mod-16 statement
  `#{r | Φ_{4p}(2) : r ≡ 1 (mod 16)} ≥ c·ω(Φ_{4p}(2))` with `ω → ∞` — stronger
  than (H1), and subsumes the ω-growth conjunct. **One-way** implication
  `r ≡ 1 (mod 16) ⟹ r ∉ P_3` is what makes it close C6; the converse is false.
- **Conjecture 23** (`hb-c23-hybrid-semigroup`): no prime r with
  `ord_r(2) = 4k` and `(r−1)/(4k) ∈ S_3^{(≤3)}` for large k.
- **Conjecture 24** (`hb-c24-semigroup-logmass`): the primitive log-mass bound.

A proof of any one of these is a direct discharge of the goal; the two-gap
Theorem 30 decomposition above is kept because (H1) and (H2) separate two
different difficulties (divisor-transference vs. radical/ω growth) and match the
paper's own named theorem exactly.
