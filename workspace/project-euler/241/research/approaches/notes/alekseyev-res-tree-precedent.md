# Precedent check: Alekseyev RES prime-wheel tree for hemiperfect (PE 241)

Question: does Alekseyev's 2026 RES tree-search method (arXiv:2601.17832v1, prime-wheel
pruning, Theorem 3.2/3.3) constitute a genuinely new direction for solving a·σ(n)=bn+c
at c=0, i.e. 2σ(n)=r·n (hemiperfect enumeration to 10^18)? Status: **modified** (method
grounded; the "port the existing solver" framing was wrong).

## Sources checked
- Paper: https://arxiv.org/abs/2601.17832 (full text read from PDF, `research/sources/alekseyev2601_pdf.full.md`).
- Implementation: https://github.com/maxale/multiplicative_functions — actual file list via
  https://api.github.com/repos/maxale/multiplicative_functions/contents/ — `sigma_linear_eq.sage`
  (read in full), `README.md`, `par_setup.sage`, `sigma_over_n_bound.sage`.

## (1) Does Alekseyev's implementation cover c=0 (multiply-perfect)? b odd / r odd?
- **Method**: paper states "although we do not exclude the case c=0 from consideration, it is
  rather special as it admits additional optimization techniques." So the *method* is stated to
  generalize to c=0, but the paper does not spell out those extra optimizations.
- **Released code (`res_solve_sigma_abc`)**: the c=0 branch is a stub. In `seed` generation:
  ```python
  if c==0 and a>=b:
      # a*sigma(n)=b*n, Prod (p^(k+1)-1)/(p-1)/p^k = b/a
      if a==b: sol.update( f_proc_w(1) )
      return sol
  ```
  This handles only the trivial `a==b → n=1` and returns **empty** for `a<b` with no tree
  descent. A commented-out line directly above it is the design note:
  `raise ValueError('c=0 is not well supported; use sigma_over_n_inverse.sage instead')` —
  i.e. the c=0 case was *delegated to a helper file that is NOT in the published repo*.
- For PE 241, (a,b,c)=(2,r,0) with r odd ≥3, so a=2<b=r: the c=0 block returns empty. The
  r-odd / b-odd "odd sigma" code paths (Section 3.3, Legendre-symbol squareness filters) run
  only within the nonzero-c tree branches, never for the PE241 c=0 case.
- **Verdict (1): NO.** The released solver does not cover c=0 with a<b, does not handle the
  odd-r hemiperfect equation, and a shipped `sigma_over_n_inverse.sage` does not exist (404).

## (2) Does his method already solve PE 241, making this equivalent to his solver?
- **No.** The paper's stated applications (Sections 5.1–5.3, Tables 1–2) are abundance/
  quasiperfect/almost-perfect, hyperperfect, and f-perfect numbers. Hemiperfect numbers, the
  OEIS A159907, and the 22 hemiperfects ≤10^18 appear nowhere. Since the released solver
  returns empty on c=0/a<b, it does not solve PE 241 either directly or as a pre-packaged case.
- Consequently the approach is *not* "use his existing solver": the c=0 specialization must be
  implemented from the paper's description. The paper itself withholds the c=0 optimizations.

## (3) Published application of the wheel to hemiperfects specifically?
- **None found.** Open-web and research-paper searches (hemiperfect + wheel/tree/lpf/Alekseyev/
  A159907, several phrasings) return no source applying Alekseyev's exact prime-wheel
  technique to hemiperfect numbers. The hemiperfect enumeration literature — Numericana hpn11/
  13/15/17 tables (Michon–Marcus), OEIS A159907/A088912, and the cirosantilli PE 241 solver —
  all use denominator-cancellation multiplicative DFS, not the wheel. So the wheel is a real
  refinement absent from the hemiperfect literature.

## What this means for the run
- The *method* is mathematically valid and Theorem 3.2/3.3 hypotheses hold for c=0 (the gcd/denominator
  reduction rules are the same that ground this run's DFS). So it qualifies as a grounded direction.
- But the file's original framing overclaimed twice: (i) it is **not** "fundamentally different"
  from this run's denominator-cancellation DFS — both are least-prime-factor trees over the
  divisor-sum equation via multiplicativity, so the wheel is an analytic *pruning refinement* of
  the same family, not a new topology; (ii) there is **no existing seam to port** — the released
  c=0 path is a stub.
- Real value: an independent verification route for the 22-value / 10^18 result (AGENTS rule 11,
  verify by a second route), not a replacement for the working DFS.

## Action
- approach status updated to `modified`; `precedent` filled with the above; `killed-by: none`
  (method valid, only the novelty/"port" framing was wrong).
