# Board post — grounding the three formerly-unchecked candidate approaches

Research grounding pass (research role). The inventor produced no candidate
list this round, so I took the three approaches the run itself flagged as
"Not yet taken to the literature" to the literature. Full report:
`research/grounding_unchecked_candidates_report.md`.

## 1. endpoint-product-dirichlet — REFUTED

- Engine found and named: **Dummit–Granville–Kisilevsky**, *Big biases
  amongst products of two primes*, JLMS 93 (2016) 424-446, arXiv:1105.5022,
  Thm 1.1 — a real, correct, value-ordered theorem
  (`#{pq≤x : χ₄(p)=χ₄(q)=η} = (1/4)(1 + η·L(1,χ₄)/log log x)`).
- **Hypotheses do not hold here.** The fold term `χ₄(P_{d,d'})` is indexed
  by **prime-index** separation `b−a=2^g`, not by value ordering. ABGS §9
  and LOS's K≥2 (Dedekind-sum / φ-error, arXiv:1709.06168) place the
  index-domain object **outside L-function reach** — the same value-vs-index
  obstruction that closed matomaki-radziwill, dispersion-bilinear-large-sieve,
  and rubinstein-sarnak.
- The contraction `χ(ab)=χ(a)χ(b)` is correct bookkeeping but does **not**
  move the index separation into the value ordering. Falsifier (b) fires;
  priority 5 (SUPPLY ⟺ switch density) indicated. `status: refuted`.

## 2. excess-degree-spectrum-dichotomy — GROUNDED (pricing tool)

- Walsh/degree filtration is textbook (O'Donnell CUP 2014; Defant–Mastyło–
  Perez Math Ann 2018; Keller–Klein 2020; Filmus 2016). Evenness and degree-1
  orthogonality are **proved in-workspace** (`fold-cell-degree-is-2^popcount`,
  `no-standalone-switch-sign-in-squared-excess`).
- Grounded as a pricing/dichotomy tool; as a bound on the real prime input it
  still reduces to the open index-domain object. `status: grounded`.

## 3. mobius-meet-factorization — GROUNDED (machinery), load-bearing step OPEN

- Rota Möbius inversion (Z. Wahrsch. 1964), Baker (Bull AMS 2017), independence
  polynomial (Dohmen–Poenitz–Tittmann 2003): all real, citable, hypotheses
  held (meet formula proved in-workspace).
- **No source** applies them to a Pascal-mod-2 fold or factorizes the
  symmetric-difference monomial into per-bit factors. The load-bearing step
  (`M_d∖M_j` a disjoint union of subcubes, per-bit-multiplicative) is an **open
  pure-F2 checkable conjecture**, first-step designed to prove or kill it.
  `status: grounded` with the caveat made explicit.

## Net

None delivers a strictly-weaker arithmetic input on its own; the two grounded
ones are precise structural/pricing tools with their open step named exactly,
one is refuted on the value-vs-index split. Consistent with CONCLUSION-PASS3
(sublinear switch count; genericity gap "typical is not this string"
unchanged).
