# Tasks

Priority follows operator directive 2: the ledger is asserted-heavy (32
asserted / 3 checked) and two anchors are not real sources. **Stop adding
claims; convert the existing ones.**

## Done (prior cycles)

Oracle (`code/oracle.py`), parallel self-check, witness cross-check (12/12),
small brute sweep n≤200, and the corrected n≡3 (mod 4) + even-case identities —
all captured and recorded. See `research/CLAIMS.md` and `code/out/`.

## 1. Source integrity (operator directive 2) — done this cycle

- [x] Tombstone Yamamoto 1965: the `.full.md` file is the J-STAGE landing page
      only; the `_pdf/-char/en` URL was re-fetched and refused (scanned, no
      text layer). Tombstone in `research/summaries/yamamoto-1965-paper.md`;
      do not cite Yamamoto as a read source.
- [x] Demote `yamamoto-1965-type12-origin` to asserted-never-read in
      `research/CLAIMS.md`.
- [x] Annotate `mathworld-egyptian-context` as orientation-only (encyclopedia
      entry, not a load-bearing anchor).

## 2. Convert identity-family claims (asserted → checked)

Each asserted identity family must get, in a claim block: the exact identity in
k, a symbolic proof that `4/n(k) − 1/x − 1/y − 1/z ≡ 0` (`is_identity`), and a
separate proof of positivity and integrality for ALL k in the stated class — not
a test on small k. A family tested on k=0..4999 without an identity proof is
`checked`, never `proved`.

- [ ] The eight classical covering identities (2 mod 3; 3 mod 4; 5 mod 8;
      2/3 mod 5; 3/5/6 mod 7): write each exact (n,x,y,z) identity, prove it
      symbolically in k, and prove integrality+positivity from the stated
      modulus. Currently `is_identity`-checked in `code/out/commands.log` but
      still `asserted` in the ledger — promote to checked claim rows.
- [ ] The corrected n≡3 (mod 4) family and the even case: already checked
      k=0..4999; restate as proved identities with integrality/positivity for
      all k.
- [ ] `prime-reduction` and `reduction-mod24`: prove the scaling lift
      `4/n = 1/x+1/y+1/z ⇒ 4/(nm) = 1/(mx)+1/(my)+1/(mz)` in exact arithmetic
      and promote both to `checked`.
- [ ] Label each family NEW vs REDISCOVERY against
      `research/sources/elsholtz-sums-of-k-unit-fractions.full.md` — name the
      known shape each identity instantiates and say whether anything here is
      genuinely new.

## 3. Only after the ledger is converted

- [ ] Return to ansatz-space search over the six open classes
      {1,121,169,289,361,529} mod 840, engaging Schinzel Thm 1 (no ℤ[k]
      polynomial identity over a quadratic-residue class); a new family must
      leave that shape.
