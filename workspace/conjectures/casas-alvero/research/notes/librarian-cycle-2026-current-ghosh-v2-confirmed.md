# Librarian cycle: library current through now; Ghosh stress-test confirmed against v2

<!-- librarian, this cycle -->

## Forward-sweep currency check (exa_search, 2026-09+)

Fresh search restricted to after the library's last confirmed full sweep
returns ONLY works already held:
- Ghosh v2 "Proof of the Casas-Alvero conjecture" (arXiv:2501.09272) — held.
- Fernández de las Heras 2013 "Three proofs of the Casas-Alvero conjecture"
  (arXiv:1306.5656) — held as `three-proofs-casas-alvero_2013`.
- Graf von Bothmer–Labs–Schicho–van de Woestijne 2007 — held.
- Castryck–Laterveer–Ounaïes 2012 — held.
- Lu 2017 — held.
- Schaub–Spivakovsky (set of bad primes / upper bound) — held.

**No new settled degree, no new counterexample, no new refereed partial
result.** The library is current through now.

## KEY verification: the Ghosh stress-test was made against v2, not a stale v1

The run's adversarial close-read of the claimed Ghosh proof lives in claim
`ghosh-char0-break-4-18` and `code/ghosh_charp/verify_break.py`
(1313/1313 exact checks, capture `code/out/ghosh_break.captured.txt`). v2 is
more than double v1 (15 KB → 30 KB, "Major revisions"), so it had to be
confirmed that the structures the close-read cites are in the **v2** text this
library holds.

Grep of `research/sources/ghosh2025_proof_html.full.md` (the v2 full text):
- **Proposition 4.3** at line 507 (the key injectivity lemma ι_{k,*}).
- **eq (4.18)** at line 561 (the degree-lowering isomorphism
  R_n/(F(1,j_1,n),…,F(n,j_n,n)) ≅ R_{n-1}/(Δ_{1n},…,Δ_{n-1,n}), which holds
  only when char ∤ n because the leading coefficient f(n,n,n) = −n is the unit).
- **f(n,j_n,n)** unit discussion at line 563 (Plücker relations,
  Δ_{in} = f(i,j_i,n)g(n,j_n,n) − f(n,j_n,n)g(i,j_i,n)).

**Conclusion:** the `ghosh-char0-break-4-18` finding — the char-0-only step
is the death of the unit −n exactly at the induction step d = n with char | n,
where the char-p witnesses x^{p+1}−x^p sit — is **against the current v2
claim**, not a withdrawn or superseded version. It stands.

## Status

- **CA remains open.** Smallest open degree 20. Ghosh claim is an unverified
  preprint (unrefereed, no community verdict on v2).
- Nothing new to fetch. Phase-1 test (ROOT status / minimal-counterexample /
  verification bound / restricted classes) is met. Further gathering only
  against a stated gap in REQUESTS.md — currently none.

## Recorded finding (memory server was down; stored here until Cognee recovers)

Same content as above; to be re-stored to Cognee once the memory endpoint
answers.
