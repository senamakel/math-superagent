# H_even, 3-Higgs primes, and the reduction — sourced structure

Everything in this note is sourced or directly checked, not guessed. The
anchors are the full texts under `research/sources/`. The claim blocks below
are the run's working ledger entries.

## The 3-Higgs primes (OEIS A057447)

`p` is **3-Higgs** iff `p - 1` divides the cube of the product of smaller
3-Higgs primes, with each prime factor of `p - 1` occurring to exponent at
most 3. Equivalently (Maciejewski §1.1): every prime factor of `p - 1` is
itself 3-Higgs and has `v_q(p-1) <= 3`.

The sequence: 2, 3, 5, 7, 11, 13, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
67, 71, 73, 79, 83, 89, 101, 107, 109, 127, 131, 139, 149, 151, 157, ...
(OEIS A057447).

Every prime divisor of a unitary perfect number is 3-Higgs
(OEIS A002827 comment, attributed to Paul Muljadi, 2005; and Maciejewski).

## The set H and H_even

```
H      = { m >= 1 : every prime factor of 2^m + 1 is 3-Higgs }
H_even = H ∩ 2Z
```

The open conjecture (Maciejewski Conjecture 6): **H_even is finite**. This is
equivalent to the Subbarao–Warren finiteness question, after the paper's
bounded-box reduction.

## What is rigorously established (from Maciejewski 2026)

- Theorem 8: `H_even ∩ [2,1200] = {2, 6, 10, 18, 26, 30, 46, 62, 82, 122}`.
- Proposition 5: `H_even ⊆ {m ≡ 2 (mod 4)}`. Every element is `2 mod 4`.
- Proposition 4 (structural lemma): if `m = 2k ∈ H_even`, `k` odd, then
  - every prime factor of `k` is 3-Higgs,
  - `v_q(k) <= 3` for every prime `q | k` ("Higgs-cubefree"),
  - `2d ∈ H_even` for every odd divisor `d | k`.
- Theorem 7 (prime-case reduction): `H_even` is finite **iff** the prime
  branch `H_even^prime = {m = 2p : p odd prime, 2p ∈ H_even}` is finite, and
  `|H_even| <= 4^|H_even^prime|`.
- Theorem 21 (thinness): `#{m ≤ X : m ∈ H} << X^(1-η)` for an absolute
  `η > 0`, and `Σ_{m∈H} 1/m < ∞`. **Rigorous but insufficient**: the bound is
  exponential at the primitive-divisor height.
- Theorems 9–19 + Lemma 20 give the finite frontier:
  `|H_even ∩ [2,50000]| ≤ 272` (rigorous), `|H_even ∩ [2,40000]| ≤ 201`.

## The prime branch and the analytic target

For `m = 2p`, `p` odd prime, `2p ∈ H_even` means every prime divisor of
`2^(2p)+1` is 3-Higgs. The Aurifeuillean split

```
2^(2p)+1 = (2^p - 2^((p+1)/2) + 1)(2^p + 2^((p+1)/2) + 1) = L_p · M_p
```

gives two ≈half-length special-form integers. The open candidates (e.g.
`m ∈ {2426, 2602, ...}`) are each blocked by an unfactored composite cofactor
of `L_p` or `M_p`.

The divisor-level target: for `r | Φ_{4p}(2)` a primitive divisor,
`ord_r(2) = 4p`, so `r ≡ 1 (mod 4p)` and `(r-1)/(4p) ∈ S_3^(≤3)` is
*necessary* for `r` to be 3-Higgs. The log-mass identity:

```
log(2^(2p)+1) = log 5 + log Φ_{4p}(2) ~ 2p log 2
```

forces the primitive divisors to carry total log-mass `≫ p`, while Ford-type
reciprocal-mass bounds only control `Σ 1/r << 1/p`. The gap is exponential.
(Conjectures 23–26, 29, and Theorem 30 in Maciejewski §5.3.)

## OEIS lookup miss — a finding

The verified members of H_even (`2, 6, 10, 18, 26, 30, 46, 62, 82, 122`) do
**not** match any OEIS sequence. So no catalogued closed form exists; the
structure has to come from the problem. Recorded so nobody re-searches.

## Checked claims

```claim
id: heven-verified-members
statement: H_even ∩ [2,1200] = {2, 6, 10, 18, 26, 30, 46, 62, 82, 122}, so
  H_even has exactly these ten verified elements through 1200 and no verified
  element in (122, 1200].
hypotheses: Maciejewski's factor cache and APR-CL verification transcript for
  Theorem 8 are correct
holds-here: yes, as sourced from the paper's Theorem 8 with its proof sketch; not
  independently recomputed in this run
status: asserted
bearing: the only confirmed H_even members below 1200; the search for any 2p
  candidate must pass through these or be a partial-cofactor unknown
falsifier: a verified member of H_even in (122,1200] would refute Theorem 8
anchor: research/sources/maciejewski-bounded-box-subbarao-warren.full.md
source: arXiv:2605.20475 Theorem 8
```

```claim
id: heven-two-mod-four
statement: H_even ⊆ {m ≡ 2 (mod 4)}. Every even m in H is 2 mod 4, i.e.
  v2(m) = 1. In particular m = 2k with k odd.
hypotheses: the Lucas refinement of Fermat-prime structure (v2(q-1) ≤ 3 for
  3-Higgs q, and q | F_k ⇒ v2(q-1) = k+2 ≥ 4 for k ≥ 2)
holds-here: yes, sourced from the paper's Proposition 5, proved there
status: catalogued
bearing: kills the m ≡ 0 (mod 4) branch of H_even outright; finiteness reduces
  to m = 2p (Theorem 7), while composite members exist (k = 9, 15 verified)
  and are inherited from unresolved prime divisors via Proposition 4(3)
falsifier: an m divisible by 4 with all prime factors of 2^m+1 3-Higgs
anchor: research/sources/maciejewski-bounded-box-subbarao-warren.full.md
source: arXiv:2605.20475 Proposition 5
```

```claim
id: heven-prime-case-reduction
statement: H_even is finite iff the set {m = 2p : p odd prime, 2p ∈ H_even}
  is finite, and |H_even| <= 4^|H_even^prime|.
hypotheses: Proposition 4 (Zsigmondy + Higgs-cubefree structure)
holds-here: yes, sourced from the paper's Theorem 7, proved there
status: asserted-by-source (rigorous in the paper)
bearing: closes the UPN branch if and only if the 2p prime branch closes. That
  is the exact bottleneck the run should attack.
falsifier: infinite H_even with finite prime branch would refute; or a
  counterexample to the structural lemma
anchor: research/sources/maciejewski-bounded-box-subbarao-warren.full.md
source: arXiv:2605.20475 Theorem 7
```

```claim
id: heven-thinness-not-finiteness
statement: #{m ≤ X : m ∈ H} << X^(1-η) for an absolute η > 0, and
  Σ_{m∈H} 1/m < ∞. This is power-saving thinness but does NOT imply
  finiteness; on the prime branch the relevant bound is exponential at the
  primitive-divisor height x = 2^(2k).
hypotheses: Ford's theorem on downward-closed prime sets (arXiv:1212.3498)
  with p0 = 17 the smallest omitted 3-Higgs prime
holds-here: yes, sourced from the paper's Theorem 21 and Ford's paper
status: asserted-by-source (rigorous in the paper)
bearing: rarity is not finiteness — the run must say which one it is
  producing; any result stated as "rarity" does not close the conjecture
falsifier: a proof that the counting bound is not power-saving, or evidence
  that P_3 contains all primes
anchor: research/sources/ford-pratt-trees-missing-primes-2014.full.md;
  research/sources/maciejewski-bounded-box-subbarao-warren.full.md
source: arXiv:2605.20475 Theorem 21; arXiv:1212.3498 Theorem 1
```

```claim
id: heven-frontier-50000
statement: |H_even ∩ [2,40000]| ≤ 201 and |H_even ∩ [2,50000]| ≤ 272,
  rigorous. No verified element in (122, 50000].
hypotheses: the paper's factor cache, APR-CL transcripts, Lemma 20 deep-Pratt
  closures (six large APR-CL-verified prime divisors), and Theorems 8–19
holds-here: yes, as sourced; not independently reproduced in this run
status: asserted-by-source (rigorous in the paper)
bearing: the verified frontier of H_even; the run's computations should
  reproduce part of it before trusting anything past it
falsifier: an independent computation finding a new verified H_even element
  or a bug in the paper's certificate
anchor: research/sources/maciejewski-bounded-box-subbarao-warren.full.md
source: arXiv:2605.20475 Theorems 8–19 and Lemma 20
```

```claim
id: aurifeuillean-split
statement: For odd prime p, 2^(2p)+1 = L_p · M_p with
  L_p = 2^p - 2^((p+1)/2) + 1, M_p = 2^p + 2^((p+1)/2) + 1; both are
  integer-coefficient quartics in a power of 2, each ≈ half the bit length.
hypotheses: Aurifeuillean identity for b^n + 1, n odd
holds-here: yes, sourced from the paper's equation (2) and the worked
  m = 2426 example, which matches the Cunningham Project table
status: checked
bearing: the open candidates are special-form SNFS targets after the split;
  a factoring campaign would target L_p and M_p separately
falsifier: a failed modular check of L_p·M_p = 2^(2p)+1
anchor: research/sources/maciejewski-bounded-box-subbarao-warren.full.md
source: arXiv:2605.20475 §5.2
```

## Gap status

- Frei 1978 full text not yet in the library (only OEIS-sourced statement of
  his result). The result itself is load-bearing for the 3 ∤ n question.
- Wall 1975 (fifth UPN) full text not in the library; the fifth UPN's
  structure is carried by OEIS, Wikipedia, Wall 1987/1988, and Maciejewski.
- The OEIS A002827 entry records Frei's theorem: a UPN not divisible by 3 has
  2^m | n with m ≥ 144, at least 144 distinct odd prime factors, and
  n > 10^440. Source for that claim: OEIS comment (Amiram Eldar, Mar 05 2019),
  which cites Frei 1978. **Not yet verified against the primary text.** which cites Frei 1978. **Not yet verified against the primary text.**