# Biquadratic character of 2 over the divisors of 2^{2p}+1

```approach
idea: Re-encode the paper's mod-16 test — the one-way obstruction
  r ≡ 1 (mod 16) ⟹ r ∉ P_3 — as the biquadratic (quartic) residue
  character (2/r)_4 of 2 modulo the primitive prime divisors r of
  Φ_{4p}(2), and attack it with Gauss's quartic reciprocity in Z[i]
  applied to the factorization 2^{2p}+1 = (2^p+i)(2^p−i).

mechanism: For a primitive divisor r of Φ_{4p}(2), ord_r(2) = 4p. A
  generator argument (correct and elementary) gives the equivalence

      (2/r)_4 = 1  (2 is a fourth power mod r)  ⟺  16p | r−1  ⟺  v2(r−1) ≥ 4

  (write 2 = g^j with j/t odd and gcd(j/t, 4p) = 1 where t = (r−1)/4p;
  then 4 | j ⟺ 4 | t ⟺ 16p | r−1). The load-bearing fact is ONE-WAY:

      v2(r−1) ≥ 4 ⟹ r ∉ P_3   (the 3-Higgs exponent cap forbids v_q(r−1) > 3)

  The converse is FALSE: a prime r can have v2(r−1) ≤ 3 yet still be
  non-3-Higgs through an odd q | r−1 (paper's Lemma 20 witness
  343081 | 2^19066+1 has v2(343080) = 3 but is non-3-Higgs via the Pratt
  chain 343081 ≻ 953 ≻ 17). So the deliverable is: prove r ≡ 1 (mod 16)
  occurs, which certifies non-3-Higgs; do not claim a two-way
  characterization of P_3.

  Synthesis: 2^{2p}+1 = (2^p+i)(2^p−i) in Z[i]. A prime r ≡ 1 (mod 4)
  dividing 2^{2p}+1 has a unique Gaussian prime factor π | (2^p+i) (or
  |(2^p−i)); the quartic character (2/r)_4 = (2/π)_4 is computable by
  quartic reciprocity from the Gaussian factorization. The Aurifeuillean
  split 2^{2p}+1 = L_p·M_p separates the integer factors into two classes.

  **The key insight** (what no literature has): multiplicativity of the
  quartic character gives a divisor-transference product identity that
  BYPASSES factorization:

      Π_{π^e || 2^p+i} (2/π)_4^e  =  (2/(2^p+i))_4.

  The right side is evaluated in closed form by Gauss's supplementary law of
  quartic reciprocity applied to the Gaussian integer 2^p + i, as a function
  of p mod 16 alone. Each left factor (2/π)_4 = 1 ⟺ N(π) ≡ 1 (mod 16). So
  the product identity determines exactly how many prime divisors of Φ_{4p}(2)
  are ≡ 1 (mod 16), without factoring 2^p + i. This is a divisor-transference
  theorem in algebraic form — the paper's missing object.

  **What has been verified** (step 1, done): the equivalence (2/r)_4 = 1 ⟺
  r ≡ 1 (mod 16) holds on all 71 primitive divisors through p=61; the H_even
  p-slice {3,5,13,23,31,41,61} is reproduced exactly; heads (r≡1 mod 16)
  exist in all four residue classes mod 8 for non-H_even primes, and are
  absent for all seven H_even members — but no single mod-8 class forces a
  head (the per-class shortcut is refuted). The product formula is the only
  viable exact route.

status: adopted
first-step: (1) [done] Verify the generator equivalence on every primitive
  divisor for p ≤ 61: code/biquadratic_table.py + code/out/heven_gauss_61.captured.txt
  confirms (2/r)_4 = 1 ⟺ r ≡ 1 (mod 16) on all 71 primitive divisors, two
  independent ways (direct 4th-power test vs Cornacchia/quartic-reciprocity
  computation), with the H_even p-slice {3,5,13,23,31,41,61} reproduced exactly.
  (2) [the sharpened move] Exploit multiplicativity of the quartic character to
  obtain a divisor-transference product identity that BYPASSES factorization:

      Π_{π^e || 2^p+i} (2/π)_4^e  =  (2/(2^p+i))_4,

  and evaluate the right side in closed form via Gauss's supplementary law of
  quartic reciprocity applied to the (non-primary) Gaussian integer 2^p + i.
  Since each left factor satisfies (2/π)_4 = 1 ⟺ N(π) ≡ 1 (mod 16), the
  product identity is an exact, deterministic statement about how many divisors
  of Φ_{4p}(2) are ≡ 1 (mod 16), computable from p alone without factoring
  2^p + i. This is the divisor-transference theorem the paper says is missing,
  in algebraic rather than analytic form. First concrete computation: express
  (2/(2^p+i))_4 as a function of p mod 16 via the supplementary law, then
  reconcile it against the per-factor product in the p ≤ 61 table as a check.
  (3) [refuted shortcut, do not re-propose] The conjecture "for a fixed
  c = p mod 8, one of L_p, M_p necessarily has a divisor ≡ 1 (mod 16)" is
  FALSE: the computed table shows H_even members p = 3, 5, 13, 23, 31, 41, 61
  (all four classes mod 8) have zero such divisors, while heads occur in all
  four classes for non-members. A congruence-class theorem forcing a head does
  not exist; only the product formula (step 2) is a viable exact route.
```

## Corrections applied (from the literature check)

The original file carried three errors, all now fixed:

- **M1 — no longer conflates C29 with existence.** The file now states
  plainly that the deliverable is the (H1)-existence form for one mod-8
  class, weaker than Conjecture 29's proportional `c·ω` statement, and
  that this does not close C6 for the other mod-8 classes.
- **M2 — the iff is now one-way.** `(2/r)_4 = 1 ⟺ 16p | r−1` is retained
  (it is correct), but the chain to "3-Higgs" stops at the forward
  implication `v2(r−1) ≥ 4 ⟹ r ∉ P_3`, with the paper's own Lemma 20
  witness 343081 cited as the converse refutation.
- **M3 — no §6 misattribution.** The claim that the paper "names the
  algebraic factorization route as its own next step" is removed; the
  paper's §6 names no such step (it names BHV primitive-divisor bounds
  plus shifted-prime smoothness).

## Why this beat the others

| Candidate | Status | Reason |
| --- | --- | --- |
| `biquadratic-character-divisors` | **adopted** | Attacks the divisor-level gap — the paper's own named analytic target for (H1) — with named algebraic machinery (quartic reciprocity in Z[i]), no GRH, no Chebotarev, no density. The Aurifeuillean split is catalogued; the BHV primitive-divisor theorem is catalogued; the generator equivalence `(2/r)_4 = 1 ⟺ r ≡ 1 (mod 16)` is elementary. The gap is the divisor-transference theorem the paper says does not exist in the literature; quartic reciprocity is a concrete algebraic candidate for it. |
| `higgs-depth-bound` | refuted | 3-Higgs primes are infinite (OEIS A057447 b-file continues), so Pratt depth is unbounded; the paper's own m=2426 example has a fully 3-Higgs divisor P=25893760589 with nontrivial Pratt descent. The fallback reduces to thinness constraints the paper already makes via Ford's theorem, and thinness does not close (paper §5.3). |
| `p-adic-baker-obstruction` | refuted | Two fatal obstacles: (1) Iwasawa p-adic log diverges for every odd p_i ≠ ℓ (v_ℓ(1/p_i^{e_i}) = 0 < 1/(ℓ−1)); (2) Baker-type bounds apply to nonzero linear forms, but the form is identically zero by construction — it is the logarithm of the balance equation, a multiplicative dependence, not an inequality. |
| `archimedean-baker-sum-reciprocals` | refuted | Baker's theorem bounds nonzero linear forms; the proposed homogeneous form is identically zero (the log of the balance), so "0 = |Λ| > exp(−C···)" is a category error. The honest Archimedean route Σ 1/p_i^{e_i} ≈ log 2 gives lower bound m > exp(a/C) and upper bound log m ≤ 3(a+1)log(a+1), same asymptotic scale — no contradiction, as the file itself shows. |
