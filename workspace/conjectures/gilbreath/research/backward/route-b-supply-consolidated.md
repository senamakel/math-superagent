# Route B supply — the conditional theorem, consolidated

This skeleton does **not** restate the Granville reduction, and it does **not**
propose a fourth decomposition of the supply side. It records where the three
existing supply decompositions actually landed and states the single residual
gap in its sharp form (`ν₂ ≥ c·n` rather than `ν₂ > n^β`), so the ledger stops
offering open "reductions" that are in fact already closed or already refuted.

## What this file is a reduction OF and a reduction TO

The whole of Route B below the supply line is **discharged**:

- the `{0,2}` second-entry equivalence (`gilbreath-reduces-to-second-in-02`,
  `gilbreath-second-entry-equivalence`);
- the runway, Granville Lemma 5.4 (`lemma54-re-derived-proof`, proved on the
  even domain with the δ=0 absorption case handled as a closure case, not an
  exception; kernel-checked as `lemma54-descent-lean-formalised-even`; Link A
  `v ≤ g*_n` verified non-vacuously over 1181 columns, 0 violations,
  `lemma54-lean-and-linkA-current-verified`);
- the demand side (`gap-bounds-cannot-force-block-growth` / BHP 2001, sharpened
  to 0.52 by `li2023-short-interval-052`; immaterial once any linear supply
  bound holds, `li2023-not-bottleneck`).

So the goal reduces to **one** proposition: the supply lower bound `ν₂(q_n) ≥ c·n`.
That proposition is the named open problem `abgs-2011-s9-mod4-switch-limit-open`,
and the honest deliverable is the conditional theorem below.

## Why the three other supply skeletons do not further reduce it

- `supply-nu2-factorization` is **broken** by Shiu 2000: its load-bearing
  hypothesis `G-supply-nonconcentration` ("no constant run of length ≥ L" in the
  halved-gap bit string) is refuted — `shiu-2000-strings-of-congruent-primes`
  gives arbitrarily long runs of consecutive primes all ≡ a (mod 4), i.e.
  arbitrarily long all-0 runs of `h`. Weakening that hypothesis to "the long
  runs have sublinear total measure" is exactly the mod-4 switch density, i.e.
  exactly the single gap below — no combinatorial shortcut.
- `nu2-supply-mod4-transfer` is **broken** by the all-ones counterexample already
  recorded inside `supply-nu2-factorization.md`: a 2-then-odds sequence with
  every gap ≡ 2 mod 4 (`h = 1111…`, weight `w = n` maximal) fails at row 3 and
  has `ν₂ = 0`, so the transfer `ν₂ ≥ w/2` is **not** universal. Its fork lands
  on (b) — prime-specific — which is its own stated "not a reduction" case. The
  prime-specific `ν₂ ≥ w/2` is measured (min 0.689), not proved, and adds a
  second unproved prime statement rather than removing one.
- `nu2-supply-split`'s `G-supply-transfer` is the only genuinely open
  combinatorial question among them (does *success* force `ν₂ ≥ (2/3)w`?),
  but a positive answer would prove GC for the whole 2-then-odds class, which
  `anti-gilbreath-construction`/`colonna-deletion-left-edge-failure` rule out;
  its other gap is the same named-open density as below.

```skeleton
goal: Gilbreath's conjecture for the primes — A_k(0) = 1 for every k ≥ 1, equivalently every finite prime prefix q_1..q_n (n ≥ 2) is "successful" (the bottom single entry of its difference triangle is 1).
implies: |
  Work in right-diagonal coordinates δ(q_n) = (δ_0, ..., δ_{n-1}), δ_k(q_n) = A_k(n−k),
  so δ_{n−1}(q_n) = A_{n−1}(0) and "q_1..q_n succeeds" ⟺ δ_{n−1}(q_n) = 1.

  (0) EQUIVALENCE [discharged]  A_k(0)=1 for all k ⟺ A_k(1)∈{0,2} for all k
      (gilbreath-reduces-to-second-in-02, proved; gilbreath-second-entry-equivalence, Lean IFF).

  (1) RUNWAY [discharged]  q_1..q_{n−1} valid & successful ∧ g*_n ≤ 2ν₂(q_{n−1})+2 ⟹ q_1..q_n succeeds
      (lemma54-re-derived-proof, proved on the even domain; the δ=0 case is the absorption
      closure, not an exception; kernel-checked as lemma54-descent-lean-formalised-even;
      Link A v ≤ g*_n verified 1181 columns / 0 violations, lemma54-lean-and-linkA-current-verified).

  (2) DEMAND [discharged]  g*_n = max(g_2..g_n) < n^{0.525+ε} (BHP 2001), sharpened to
      n^{0.52+ε} (li2023-short-interval-052); the α ∈ {0.52, 0.525} choice is immaterial
      once a linear supply bound holds (li2023-not-bottleneck).

  (3) SUPPLY [SC-supply-nu2-linear, OPEN]  ν₂(q_n) ≥ c·n for a fixed c > 0 and all large n.

  COMBINE:  for large n, ν₂(q_{n−1}) ≥ c(n−1) > n^{0.52} ≥ g*_n, so the runway (1) turns
  "q_1..q_{n−1} successful" into "q_1..q_n successful"; strong induction on n from the
  verified base (the run's own depth 1000, or Odlyzko's 10^13 — verification-record-2026)
  gives every finite prefix successful, hence GC. By (0) this is the equivalent {0,2}
  second-entry statement.

  This is a CONDITIONAL theorem. Its sole hypothesis, (3), is the named open problem
  abgs-2011-s9-mod4-switch-limit-open in right-diagonal coordinates: it is NOT claimed to
  be provable unconditionally from anything the run holds (Shiu goes the wrong direction,
  Lau/Maynard are existence-only, ABGS §9 says no limit even exists).
status: sketched
rests-on: gilbreath-reduces-to-second-in-02, gilbreath-second-entry-equivalence, lemma54-re-derived-proof, lemma54-descent-lean-formalised-even, lemma54-lean-and-linkA-current-verified, gap-bounds-cannot-force-block-growth, li2023-short-interval-052, li2023-not-bottleneck, verification-record-2026, abgs-2011-s9-mod4-switch-limit-open
```

```gap
id: SC-supply-nu2-linear
lemma: For the prime sequence, the count ν₂(q_n) of 2s in the maximal {0,2} suffix of the right diagonal δ(q_n) satisfies ν₂(q_n) ≥ c·n for a fixed c > 0 and all sufficiently large n. (Sharp linear form of GN-supply-nu2-density; the n^{0.526} form is strictly weaker and is the same proposition.)
status: open
next: |
  This is the ENTIRE remaining content of Route B, and it is a named open problem, not a
  gap in the run's own argument. Two first moves, one theoretical and one computational:

  theorem_prover (the honest deliverable is the CONDITIONAL theorem, not an unconditional
  proof): prove "Hardy–Littlewood k-tuple conjecture ⟹ ν₂(q_n) = n/2 + O(√(n log n))".
  Under HL the halved-gap parity bit string h[j] = ((p_{j+2}−p_{j+1})/2) mod 2 is
  asymptotically unbiased with bounded pair correlations (los-2016-consecutive-pair-mod4-bias
  supplies the main term n/2 + bias; rubinstein-sarnak supplies the oscillation shape), and
  ν₂ is the weight of a fixed Rule-90 (Pascal-mod-2) fold of h (rule90-interior-xor), so a
  bounded-difference/Azuma concentration bound over the XOR folds gives the fluctuation.
  This is a corollary-level theorem under a named conjecture — a genuine partial result that
  reduces GC to one clean, well-studied hypothesis. It does NOT go through the refuted
  universal transfer ν₂ ≥ w/2; the fold map is applied to the prime bit string directly.

  tool_builder (sanity anchor, cheap): verify the random analogue — for i.i.d. unbiased
  h ∈ {0,1}^m, the weight of the same Φ-m fold equals m/2 + O(√(m log m)) with high
  probability — to pin the constant and the concentration rate the deterministic HL argument
  must reproduce. The real-prime ν₂ is already measured to n = 1e5
  (code/out/nu2_incremental_1e5.txt: max |ν₂ − n/2| = 624 at n = 78536, min ν₂/n = 0.4587,
  weakest implied exponent 0.7658 ≫ 0.525); extending to n = 1e6 only sharpens the constant,
  it does not change the target. Do not re-run the mod-4 transfer — it is prime-specific and
  refuted universally (see the note above and supply-nu2-factorization.md).

  STATUS HONESTY: an unconditional proof of ν₂ ≥ c·n is out of reach of the held library
  (shiu-2000-strings-of-congruent-primes proves arbitrarily long NON-switches, the wrong
  direction; lau-2024 existence-only; abgs-2011-s9-mod4-switch-limit-open: no limiting
  frequency exists). Report this gap as the hypothesis of a conditional theorem, never as
  "nearly closed".
thread: research/threads/regeneration.md
```
