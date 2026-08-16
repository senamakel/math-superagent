# 2-regular / automaton generating-function reformulation of the diagonal

```approach
idea: The diagonal cells T(n,d) = s_d(n−1−d) (the submask XOR, one per row) form
      a 2-regular sequence, by Lucas' theorem on binomial sums mod 2
      (Rampersad–Wiebe, arXiv:2309.04012). Represent wt(Φ_n h) = Σ_d T(n,d) as a
      linear representation / finite automaton, and attack the weight through
      the automaton's structure rather than through a search over n.
mechanism: 2-regularity means T(n,d) is computed by a finite automaton reading
      the base-2 digits of n and d. Then ν₂(n) = Σ_d T(n,d) is a count of
      accepting states along row n of that automaton, so SUPPLY's bound becomes
      a statement about the automaton's finite kernel and the digit structure
      of n. The prime string h enters only as the coefficients of the
      automaton's states.
status: refuted
precedent:
  - "Rampersad & Wiebe, Sums of products of binomial coefficients mod 2 and
     2-regular sequences, arXiv:2309.04012: run-length transforms of
     linear-recurrence sequences are 2-regular, Walnut-decidable; Thm 20 gives
     an exact 0/1 characterization of one binomial-product mod-2 sum (1 iff
     every run of 1s in [n]₂ has length divisible by m)."
     https://arxiv.org/abs/2309.04012
  - "Coons, (Non)Automaticity of number-theoretic functions, arXiv:0810.3709:
     the prime indicator χ_P(n) is NOT k-automatic for any k ≥ 2."
     https://arxiv.org/abs/0810.3709
  - "Hartmanis & Shank, On the Recognition of Primes by Automata (1968): neither
     the primes nor any infinite subset is accepted by a finite (or pushdown)
     automaton."  https://doi.org/10.1145/321466.321470
  - "Dubbe, The automaticity of the set of primes, arXiv:2409.04314: the primes'
     recognition automaticity is within a hair of the maximal ~x (not O(1)), so
     the primes are far from automatic."  https://arxiv.org/abs/2409.04314
  - claim: rw-not-the-submask-xor-fold (asserted) —
     research/summaries/rampersad_wiebe_2regular_fulltext.md
killed-by: the fold matrix entries are 2-automatic, but ν₂(n) = wt(Φ_n h) is
      the sum over d of a submask-XOR of the prime gap-parity coefficients h.
      Whether that sum is a 2-regular sequence in n is a statement about a
      generating function with NON-automatic (prime-derived) coefficients; the
      2-regularity the automaton route needs would make ν₂(n) a finite-state
      function of n, which the non-automaticity of the prime-driven input does
      not support and which, as Rampersad–Wiebe's own digest states
      (rw-not-the-submask-xor-fold), the paper does NOT establish — it treats
      run-length transforms of linear-recurrence sequences, not the submask-XOR
      fold against an arbitrary coefficient string.
      Concretely: Rampersad–Wiebe's T(n) is a *scalar* run-length product of a
      fixed recurrence; SUPPLY's T(n,d) is a *vector family in d* folded against
      h. The 2-regularity engine (Lucas, Walnut) applies only to the former. So
      the automaton machinery is real but does not reach wt(Φ_n h) for the
      primes; there is no evidence ν₂(n) is 2-regular in n, and the
      non-automaticity of the primes (Hartmanis–Shank 1968, Coons 2008, Dubbe
      2024) is positive reason it is not.
open-step: a genuine 2-regular representation of the fold *with h as free
      coefficients* would be a new object; but even then the primes' coefficients
      are non-automatic, so the automaton would not be finite-state over n alone.
first-step: (closed) the on-disk digest already corrected the premise
      (rw-not-the-submask-xor-fold); no executable step advances this candidate
      toward SUPPLY without first resolving whether wt(Φ_n h) is a finite-state
      function of n, which the non-automaticity of the primes argues against.
```

## Why it is distinct

This is the *algebraic / automaton* route: it turns the fold into a finite-state
generating function whose accepting-state count is exactly ν₂(n), replacing a
per-n combinatorial sum with a single algebraic object.

## Literature verdict (research specialist, 2026-02)

- Rampersad–Wiebe is real and 2-regularity of run-length transforms is proved,
  but the on-disk digest's own correction (rw-not-the-submask-xor-fold) is
  decisive: the paper's sums are over k of *products* C(·)C(n,k), not XORs over
  submasks of a fixed d against a non-recurrence coefficient string, and its
  T(n) is a scalar, not SUPPLY's vector-in-d fold. It hands over the Lucas /
  Walnut *engine* but no theorem about wt(Φ_n h).
- The fatal structural input is non-automaticity of the primes. Hartmanis–
  Shank 1968 and Coons 2008 (and the automaticity quantifications of Dubbe
  2024) prove the prime-derived coefficient string is not k-automatic. A
  finite-automaton-in-n description of ν₂(n) = wt(Φ_n h) would express an
  infinite computation of a non-automatic input by a finite automaton, which
  these results make untenable. The automaton machinery is **grounded** as a
  tool; the *route to SUPPLY* is **refuted**.
- Honest caveat: I did not find a paper that attacks the specific
  submask-XOR-with-prime-coefficients weight directly; the refutation combines
  Rampersad–Wiebe's non-coverage with the primes'-non-automaticity, both
  sourced, to show the automaton route cannot reach ν₂(n) for the primes. A
  subtlety: T(n,d) may still be automatic jointly in (n,d) even though h is
  not, because h is a *parameter* — but then the automaton is not finite over n
  alone, which is precisely the form the lower bound wt ≥ c·n would need. That
  is the honest boundary of the refutation.
