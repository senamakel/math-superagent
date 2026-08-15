# Scholar digest-pass report — source library review

Scope: this scholar session re-read the principal load-bearing sources in
`research/sources/` and checked their fidelity against what the run needs. This
session has **no execution tool**, so it added no verified computation; its
role was to confirm the library is correctly digested, flag what is still
unverified, and state which sources help and which do not.

## Confirmed load-bearing claims (personally re-read, anchored correctly)

| Source (anchor) | Establishes | Status |
| --- | --- | --- |
| Conrad factorize.pdf | Z[zeta_p]=O_K; (p)=(1-zeta_p)^(p-1); P=(1-zeta_p) principal, e=p-1, f=1 | asserted |
| Schoof realcyc.pdf | 0->Cl+->Cl->Cl-->0; h=h+·h-; h~+|h+; plus not known p>=71 | asserted (paper proves the divisibility) |
| relative-class-number-analytic + stickelberger-cyclotomic-units | h^-(Q(zeta_p))=2p·prod_{chi odd}(-1/2 B_{1,chi}); Stickelberger ideal annihilates Cl; [Z[G]^-:s^-]=h^-; [E+:C+]=h^+ up to pow 2 | asserted |
| MIT 18.785 | zeta_K(s)=prod L(s,chi); analytic class number formula | asserted |
| Evertse Ch5 | Baker 1975 |Lambda|>(eB)^(-C); multiplicative coroll. 5.3 | asserted |
| Klazar Thue | finiteness for irreducible homogeneous deg>=3; does NOT apply to varying-exponent x^p-y^q=1 | asserted |
| Pillai tier | Bennett at-most-two (2001), at-most-one inequality (2008); c_0(3,2)=13; (3,2,1) two-solution exception | asserted |

All are standard facts asserted by their sources; none supplies the answer to
`x^p - y^q = 1` (correctly screened by the evidence policy).

## Fidelity corrections / flags from this pass

1. **`zeta-p-ring-of-integers-and-ramification` is still `asserted`** — the
   foundational claim of the both-odd cyclotomic approach has not been
   re-derived in-workspace. An exact check (3 direct consequences: Norm(1-zeta_p)=p,
   prod(1-zeta^j)=p, Phi_p(X)≡(X-1)^(p-1) mod p) was **written** at
   `code/scholar_oracle/verify_ramification.py` but **NOT run** (no execution
   tool). tool_builder/coder must run it before any both-odd lemma treats the
   ramification as verified-numerically. Do not attribute a pass to this session.

2. The hminus "two independent routes" concern raised earlier (verify_claims.py
   vs hminus_exact.py sharing the same Bernoulli product and hardcoded table) is
   **resolved**: the PARI/GP `bnfinit` class-number ratio route
   (hminus_pari.gp) is genuinely independent (never evaluates the Bernoulli
   product), 13/13 values match for p=3..43. Verified from the captured output
   `code/out/hminus_pari.captured.txt`.

3. The valuation identity `v_p(x^p-1)=1+v_p(x-1)` **requires hypothesis
   `p | (x-1)`** (LTE congruence), not `p ∤ x`; the latter is false (p=3,x=2).
   This correction is already in the library and RECONFIRMED here — do not build
   a Cassels/divisibility lemma on the `p∤x` form.

## Sources that do not help further (read once, not again)

- `keune-number-fields.md`, `washington-*.md`: catalogues/metadata; ring
  structure already covered by Nguyen/Milne/Conrad.
- `tijdeman-linear-forms-survey.md`: technique-only; the exact effective bound
  for this equation is not needed to make the "cannot compute" argument.
- `conrad-cyclotomic-extensions.about.md`, `conrad-unit-theorem.about.md`:
  background Galois/unit-rank facts, no load-bearing step beyond what is already
  claimed.
- `columbia-cyclotomic-class-groups.primary.md`: duplicate of the canonical
  `columbia-ant-cyclotomic-and-class-numbers.primary.md`; pointer only, delete on
  cleanup (as PROVENANCE already notes).

## What the run still lacks (unchanged by this session)

- The in-workspace **proof** of Cassels divisibility `p|y, q|x` (the valuation
  machinery is `checked`, the ideal-power/unit argument is not).
- The double-Wieferich congruences re-derived from Cassels (currently
  reconstructed/heuristic; screened as answer-adjacent).
- The proofs of the two exponent-2 cases in full (Z and Z[i]); both numerically
  verified to 10^8 but `proved` only for x^2-y^3=1.
- The both-odd class-group descent (G-odd-descent) — the only step with no
  cheap move in any source.
