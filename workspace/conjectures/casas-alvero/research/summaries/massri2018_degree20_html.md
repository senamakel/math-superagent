# Massri — "The Casas-Alvero conjecture for three recycled roots in degree 20" (arXiv:1806.09561v6, 2023)

Full text held at `research/sources/massri2018_degree20_html.full.md` (arXiv HTML v6, 25 Aug 2023).
Source URL: https://arxiv.org/html/1806.09561v6. arXiv:1806.09561 (v1 25 Jun 2018; v2, v3, v5 withdrawn; v4 2021; v6 2023 is the current version).

## What the paper establishes

The paper works with Abel–Gontcharoff polynomials G(x; y_0, …, y_{n−1}): the unique degree-n polynomial with prescribed "derivative values" at nodes (G^{(i)}(y_i) = 0-type conditions), which every polynomial can be written against in normal form f = G(x; y_0, …, y_{n−1}). Three results:

1. **Finiteness (Section 5, Prop 5.x/6.1).** The number of possible counterexamples in normal form of degree p^r + p^s or p^r + 2p^s (p prime, r,s positive integers) is finite. (Introduction states it as: finite number of possible counterexamples in normal form of degrees p^s(p^r+1) or p^s(p^r+2), p prime, r,s ≥ 0.)

2. **Algebraic coefficients (Section 6).** A possible counterexample in normal form of degree p^r + 1 has algebraic coefficients (in Q̄[x]).

3. **No three recycled roots in degree 20 (Section 7, Theorem 7.10).** There is no CA-polynomial of degree 20 with three recycled roots. "Recycled roots" = the y_i in the Abel–Gontcharoff normal form taking values in {0, 1, y} (three distinct values, roots recycled across derivative levels). Proof: brute-force check of all 3^17 cases (i from 0 to 3^17−1 in base 3, mapping digits to y_k ∈ {0,1,y}), each tested by whether res(f_i(1), f_i(y)) = 0; done in <48 h on a 4 GHz/4 GB personal computer.

## Supporting results in Section 7 (all stated with proofs)

- **Theorem 7.9:** There is no CA-polynomial of degree 20 with a root of multiplicity ≥ 11, and none of degree 24 with a root of multiplicity ≥ 15. (Proved by reduction mod p: degree 20 over F_5, degree 24 over F_7; the radical of ⟨f(1), res(f,N_5 f), res(f,N_10 f), res(f,N_15 f)⟩ (resp. N_7, N_14, N_21) has finitely many solutions, none with the forced coincidence.)

```claim
id: massri-no-mult-11-degree20
statement: There is no CA-polynomial of degree 20 with a root of multiplicity >= 11, and
  none of degree 24 with a root of multiplicity >= 15 (Massri, arXiv:1806.09561v6, Theorem
  7.9). Proof: reduction mod p (deg 20 over F_5, deg 24 over F_7); the radical of
  <f(1), res(f,N_5 f), res(f,N_10 f), res(f,N_15 f)> (resp. N_7,N_14,N_21) has finitely
  many solutions, none with the forced coincidence. A multiplicity upper bound on a
  minimal counterexample in the smallest open degree.
hypotheses: char 0 (bound on char-0 CA polynomials); degree 20 or 24; N_i f the
  Abel-Gontcharoff/Hasse normal-form derivatives
holds-here: yes — a direct constraint on a minimal counterexample in the smallest open
  degree 20, strengthening the Laterveer-Ounaies "root of multiplicity >= N-2 => pure
  power" (N-2 = 18; Massri pushes the no-CA bound to 11 for N=20)
status: asserted-by-source (stated with proof sketch in the full text; not independently
  re-verified by this run)
bearing: any root of a degree-20 counterexample has multiplicity at most 10; a structural
  constraint usable by the scheme/elimination route
anchor: research/sources/massri2018_degree20_html.full.md, Theorem 7.9
falsifies: a degree-20 CA polynomial (not a pure power) with a root of multiplicity >= 11,
  or a degree-24 one with multiplicity >= 15
```
- **Remark 7.4:** For n=20, p=19, all 2^17 cases of |G(1;0,0,c_2,…,c_{n−2},1)| = 1/p were checked: 6680 possible CA-polynomials with ≥2 distinct roots, reduced to 3125 after excluding y_4=y_16=1, y_5=y_10=1, y_10=y_15=1; the 4 most computationally intensive cases are systems with 16 equations in 15 variables.
- **Remark 7.6:** For n=20, p=19, the minimum m = min |G(1;0,0,c_2,…,c_{n−2},1)| over c_i ∈ {0,1} equals 5; hence any CA-polynomial of degree 20 has a common root of absolute value > (1/p)^5 = 19^−5. Same for n=24, p=23.
- **Proposition 7.7 (p-adic bound):** If f (degree n, ≥2 distinct roots) has a prime q, a set S, and a root λ with |C(n,i)|_q < 1 for all i ∈ S and f^(i)(λ) = 0 for all i ∉ S, then f is not a CA-polynomial. Proof: normalize, evaluate at 1, get −1 = Σ_{i∈S} C(n,i) b_i with |b_i|_q ≤ 1, contradiction by ultrametric inequality.
- **Remark 7.8:** For n=20 this rules out CA-polynomials G(x;y_0,…,y_19) with y_1=y_19, y_4=y_16, or y_5=y_10=y_15.

## Relationship to the run's claims

- Directly establishes claim `massri-degree20-no-3-recycled` (degree 20 has no counterexamples with three recycled roots) and `massri-finiteness-psums` (finiteness of counterexamples in normal form of degree p^r+p^s, p^r+2p^s) — both currently in CLAIMS.md as asserted-by-source, now backed by this full text.
- The Introduction confirms: "the first open case is n = 20", "the conjecture is known to be false in positive characteristic", and that the conjecture has been proved for degrees p^e, 2p^e, 3p^e, 4p^e, 5p^e for infinitely many primes p (citing [15,5,7,9]). This corroborates claims `smallest-open-degree`, `charp-false`, `5p-bad-primes-chellali`.
- Theorem 7.9 (no root of multiplicity ≥ 11 in a degree-20 CA polynomial) is a multiplicity-bound constraint on a minimal counterexample, in the same family as claim `at-least-five-distinct-roots` (Laterveer–Ounaïes) and the Laterveer–Ounaïes multiplicity-N−2 result. Note the interplay: Laterveer–Ounaïes say a root of multiplicity ≥ N−2 forces a pure power; Massri's 11 bound for N=20 is stronger than N−2 = 18 in this range, and is a different mechanism (p-adic + resultant over F_5).
- The Abel–Gontcharoff normal form and the p-adic Proposition 7.7 are directly relevant to the run's adopted root-difference-coloring approach (which uses the Abel–Gontcharoff / root-difference factorization H_i(f)(x) = e_{n−i}(x−β_1,…,x−β_n)); see thread root-difference-coloring.

## Caveats

- v6 (2023) is a major re-expansion after three withdrawals (v2, v3, v5); the run treats its claims as asserted-by-source (computational for Theorem 7.10 — a 3^17-case exhaustive check, not a proof in the traditional sense; exact in the sense of exact resultant computations), not as independently verified here. The 3^17 = 129,140,163-case check is reported by the author, not reproduced by this run.
- Theorem 7.9's "no multiplicity ≥ 11 root in degree 20" and Remark 7.6's "root of abs value > 19^−5" are stated with proofs in the text and could be re-verified by the run's oracle.
