# Thread: root-difference-coloring — char-p collapse mechanism resolved

```thread
question: Where does the root-difference-coloring collapse step break in
      characteristic p, and is that the whole of the admissibility test?
status: open
rests-on: root-difference-identity (proved char-free,
      research/notes/root-difference-identity-verified.md),
      gvb-coefficient-descent-charp (this note),
      hasse-vs-ordinary (dead), polstra-convex-hull-theorem,
      macintyre-goncaroff-bounds (research/summaries/macintyre1949...
      .md) -- the analytic bounds on the Abel-Goncharoff G_n that the
      char-0-only collapse step would ultimately be measured against
next: The char-p break is now NAMED at the pivot level (coefficient descent,
      stops where the first pivot (d choose d-1) = d is not 0 mod p, i.e. the
      witness degree d = p+1). What remains open is the CHAR-0-only ingredient
      to collapse the degrees between the p^k grid — the convex-hull /
      Gauss-Lucas propagation — and whether it can be made to force collapse
      at d = p+1. Test the descent pivot boundary against the bad-prime lists
      (binomial criterion, n=3,4,5 calibrated in badprimes-criterion-n5.md),
      and confirm (d choose i) ≡ 0 mod p for all 1<=i<=d-1 at d=p^k with
      code/scholar/descent_check.py (written, awaiting execution).
```

## Findings

0b. **The two-shared-roots stratum has a structural source (scholar, Kostov 2020).**
   Kostov's higher-order-discriminant factorisation
   Res(D~_m, ∂D~_m/∂a_k, a_k) = A_{m,k} B_{m,k} C_{m,k}² says C_{m,k}=0 is the
   closure of the parameter set where P and P^(m) share TWO distinct roots
   (`kostov-higher-order-discriminant-two-shared-roots`). The run's R_i =
   Res(f, H_i f) are the same resultant family (up to the Hasse unit 1/i! in
   char 0), so this gives an independent, sourced description of the
   shared-root-multiplicity stratum the collapse step must rule out in char 0 —
   and it is irreducible and quasi-homogeneous with weight(a_j)=j, so any
   collapse argument in the weighted (centroid-pinning) normalisation is
   consistent with it. Char-0 (C[a]) only; no char-p content.

0. **The named char-p break is NOT (only) per-color Hasse vacuity — confirmed
   by a fully NON-vacuous char-p refutation at n=6, p=7 (this run, refuter).**
   f = x^6 − x^2 over F_7: p = 7 > n = 6, so no binomial coefficient C(6,i)
   vanishes and every Hasse derivative H_1=6x^5+5x, H_2=x^4−1, H_3=6x^3,
   H_4=x^2, H_5=6x is nonzero; the pinned-centroid descent break p|n−1 also
   does not occur (7 ∤ 5). Yet f has three F_7-roots {0(mult 2),1,6}, is not a
   pure power, and shares a root with each H_i. `find_counterexample` on
   code/refute/ca_deg6_char7.p returns **refuted** (model matches the hand
   tables entry-for-entry; 7 is the 3rd published degree-6 bad prime, Castryck
   2012 Table 1). So the char-0 collapse step must fail at n=6,p=7 for a reason
   OTHER than derivative degeneracy — the missing char-0-only ingredient
   (Gauss-Lucas / convex-hull propagation) alone carries the obstruction, and
   any collapse-step argument must survive THIS witness (all H_i ≠ 0), not just
   x^{p+1}−x^p. → code/out/refute_deg6_char7.md (claim deg6-char7-nonvacuous-refuted)

1. **The identity holds and is a tautology, char-free** (already recorded in
   `root-difference-identity-verified.md`): `H_i(f)(x) = e_{n-i}(x-beta_*)`,
   `R_i = prod_beta H_i(f)(beta)`, valid over any commutative ring.

2. **The char-p collapse is NOT absent — it is coefficient descent.**
   Graf von Bothmer et al 2007 (Props 2.5, 2.6, Lemma 2.4) prove X_{p^k}(Fbar_p)
   and X_{2p^k}(Fbar_p) are empty: since `(d choose i) ≡ 0 mod p` for all
   `1<=i<=d-1` when `d = p^k`, `P_{d-1} = a_1` forces `a_1=0`, then `P_{d-2}=a_2`
   forces `a_2=0`, ... and the descent collapses all coefficients to 0.

3. **The break is the first pivot `(d choose d-1) = d ≡ 0 mod p`.** At the
   witness degree `d = p+1`, `(p+1 choose p) = p+1 ≢ 0 mod p`, so the descent
   never starts and `x^{p+1} - x^p` survives. This corrects the earlier claim
   that "the convex-hull propagation has no F_p analogue" — the F_p collapse
   exists and is coefficient descent; the char-0-only piece is confined to the
   convex-hull/Gauss-Lucas propagation between the p^k grid.

4. **Remaining open gap (unchanged in substance):** the char-0 collapse at
   `d = p+1` — forcing all roots to coincide via the convex-hull propagation
   that has no F_p analogue. This is the conjecture to establish for small n
   (5, 6) before any claim to n=20. The char-p break is now named at the tuple
   level; that is what GOAL.md's admissibility test requires.

## Blocked-by / next-step

- Resolve `code/scholar/descent_check.py` (confirm the binomial-descent
  hypothesis at p^k). Then test the pivot boundary `p | (d choose d-1)` against
  the bad-prime lists to confirm the correspondence "p ∤ d ⇒ witnesses exist"
  holds at the small degrees where the bad lists are known, and mark the
  approximation `p^k`/`2p^k` grid vs `p+1` gap.
