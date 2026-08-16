# Scholar verification — entropy-frontier digests vs primary bodies

The library's six entropy-frontier papers were previously held as arXiv
abstract-page stubs; a repair pass re-fetched their real bodies and wrote
digests. This pass, the scholar re-derived each digest **against the primary
body on disk** and found all six faithful. What was checked, and the caveats:

## Verified faithful (digest matches body)

1. **Gilmer** (`gilmer-constant-lower-bound-2022.pdf.full.md`): Theorem 1
   `H(A∪B) ≥ 1.26·H(A)` under `Pr[i∈A] ≤ 0.01`; Theorem 2 (constant 0.01);
   Examples 1–2 product-Bernoulli crossover `H(A∪B)/H(A)=H(2p−p²)/H(p)`,
   =1 at p=(3−√5)/2, and Gilmer's own note that a stronger bound on Theorem 1
   cannot settle UC because `(3−√5)/2 < 1/2`.
2. **AHS** (`alweiss-huang-sellke-barrier-2022.html.full.md`): Theorem 1
   (two-point-mass minimizer), Theorem 2 + Claim 4 give constant `(3−√5)/2`
   as a "natural barrier for the method of Gilmer" — iid copies only.
3. **Chase–Lovett** (`chase-...-2022.html.full.md`, base still a stub):
   Theorem 1.3 (ψ−δ for (1−ε)-approx union-closed), Example 1.4 shows ψ is
   **optimal** for the approximate-iid relaxation.
4. **Pebody** (`pebody-...-2022.html.full.md`, base still a stub): Theorems
   1–2 (independent (3−√5)/2 proof); Lemma 3/4 discrete form
   `Σ p_i p_j H(v_i+v_j−v_i v_j) ≥ [H(2α−α²)/H(α)]·Σ p_i H(v_i)`.
5. **Boppana** (`boppana-...-2023.html.full.md`, base still a stub): elementary
   calculus proof of `h(x²) ≥ φ x h(x)`, φ=(√5+1)/2 golden ratio.
6. **Cambie** (`cambie-better-bounds-entropy-2022.pdf.full.md`): solves Sawin's
   Question 2 exactly; c≈0.3823455333667 at α≈0.0356069; Theorem 3.

## Cross-confirmation of the record value (two independent bodies)

Yu's own paper (`yu-dimension-free-bounds-2023.full.md`, line 149) cites
Cambie's interval `0.382345533366702 ≤ t̂_max ≤ 0.382345533366703` at
α≈0.03560698136437784; Cambie's body independently gives
`0.3823455333667034` and E[p]=0.3823455333667034. Two primary bodies agree.
Yu's certified point: Γ̂≥1.00000889 at (α=0.035, a≈0.3300622, β≈0.1560676),
independently reproduced by the run's `yu_crosscheck.py` to 2.937e-9.

## Caveats raised this pass

- **`pulaj-3set` status.** Claim `pulaj-3set` (FC(3,n)=⌊n/2⌋+1) is filed
  `evidence: proved`, but the only on-disk source is a **bibliographic record**
  (paper paywalled; content "reconstructed from companion notes"). It should be
  treated as **asserted-by-source**, not independently derivable, unless the
  real body is fetched or the run's Poonen-weight LP reproduces it. The
  corollary "a single 3-set is Non-FC" IS independently corroborated by
  Ellis–Ivan–Leader.
- **`cambie-0-38234-published-route`, `liu-conditionally-iid`, `ahs-published-ejc`**
  are `asserted-by-source`: Cambie/Liu are preprints, and Cambie's constant
  rests on a computer-verified minimization (Cambie himself notes it is
  "slightly less rigorous" than AHS).
- **Chase–Lovett / Pebody / Boppana**: the base `*.full.md` files are STILL
  abstract stubs; claims must point to the `.html.full.md` variant.

## Contradictions confirmed genuine

- **Morris Conjecture 3 vs Pulaj 2017**: genuine source-vs-source refutation,
  recorded both ways (`contradicts` edges in both directions). Known dead end;
  the run must not rely on Morris's Conjecture 3.
- **Ellis / Sawin vs Gilmer's Conjecture 1**: Gilmer's information-theoretic
  strengthening is FALSE (n=2 counterexample, verified by hand to −0.0468);
  ruled-out route to UC. The (3−√5)/2 barrier uses a different correct
  inequality, so no contradiction with AHS.
