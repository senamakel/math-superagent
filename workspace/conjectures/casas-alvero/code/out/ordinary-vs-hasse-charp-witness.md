# Hasse recheck of the `f(X^p)` clause in `charp-witness-xpp1-xp`

What was attacked: the clause of claim `charp-witness-xpp1-xp`
(`research/summaries/grafvonbothmer2007_infinitely_many.md`) that reads

> f(X^p) without constant term also works since all derivatives vanish.

The first part of the claim (x^{p+1} − x^p is CA, not a pure power) is checked
already (oracle guard 3, `code/out/oracle_guard.captured.txt`). The second
clause is **ordinary-derivative vacuity**: over F_p, d/dx f(X^p) =
p X^{p−1} f′(X^p) ≡ 0, so every ordinary derivative vanishes and
gcd(f, f^(i)) = f is trivially non-constant. The published char-p literature
uses the **Hasse** derivative H_i(f) = Σ_j C(j,i) c_j X^{j−i} (Castryck et al.
2012 Def 1; Schaub–Spivakovsky; see `research/threads/hasse-vs-ordinary.md`),
which does not vanish where the ordinary one does. This note records whether
the clause survives under Hasse.

## Method and programs

- `code/hasse_charp/recheck_xpp1_xp_hasse.py` — the requested program. Exact
  sympy over GF(p); decides with the canonical oracle `lib.casas_alvero.is_ca`
  (ordinary), `is_ca_hasse` (Hasse), `is_pure_power`, and explicit
  `H_i` via `lib.casasalvero.hasse_derivative`. Guards at entry:
  `is_ca((x−1)^3, 0)`, `is_ca(x^3−x, 0)`, and `is_ca_hasse(x^{p+1}−x^p, p)` for
  p = 2, 3, 5 — all asserted before any measured output.
- `code/hasse_charp/crosscheck_hasse_independent.py` — **independent second
  route**: hand-rolled F_p ring and Euclid gcd, closed-form Hasse coefficient
  C(j,i) mod p, no sympy and no `lib` imports at all. 56/56 checks agree with
  the oracle route (verdict tables below).

Output captured at `code/out/ordinary-vs-hasse-charp-witness.captured.txt`.
All arithmetic exact; no floats anywhere.

## Results

### (A) the genuine Hasse witness: x^{p+1} − x^p, p ∈ {2,3,5,7}

| p | deg | is_ca | is_ca_hasse | is_pure_power | nonzero H_i |
| --- | --- | --- | --- | --- | --- |
| 2 | 3 | True | True | False | [1, 2] |
| 3 | 4 | True | True | False | [1, 3] |
| 5 | 6 | True | True | False | [1, 5] |
| 7 | 8 | True | True | False | [1, 7] |

Both hypothesis formulations hold and the polynomial is not a pure power:
this is the genuine char-p witness under **both** conventions.

### (B1) g = x^{mp}, m = 1..3 (monomial f(X^p), f(0) = 0)

| p | m | deg | is_ca | is_ca_hasse | is_pure_power | H_1 | H_2 | H_p | all H_i vanish? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 1 | 2 | True | True | True | ≡ 0 | — | — | **yes** |
| 2 | 2 | 4 | True | True | True | ≡ 0 | ≡ 0 | ≡ 0 | **yes** |
| 2 | 3 | 6 | True | True | True | ≡ 0 | **x⁴** | x⁴ | **no** (H₂, H₄) |
| 3 | 1 | 3 | True | True | True | ≡ 0 | ≡ 0 | — | **yes** |
| 3 | 2 | 6 | True | True | True | ≡ 0 | ≡ 0 | **−x³** | **no** (H₃) |
| 3 | 3 | 9 | True | True | True | ≡ 0 | ≡ 0 | ≡ 0 | **yes** |
| 5 | 1 | 5 | True | True | True | ≡ 0 | ≡ 0 | — | **yes** |
| 5 | 2 | 10 | True | True | True | ≡ 0 | ≡ 0 | **2x⁵** | **no** (H₅) |
| 5 | 3 | 15 | True | True | True | ≡ 0 | ≡ 0 | **−2x¹⁰** | **no** (H₅, H₁₀) |
| 7 | 1 | 7 | True | True | True | ≡ 0 | ≡ 0 | — | **yes** |
| 7 | 2 | 14 | True | True | True | ≡ 0 | ≡ 0 | **2x⁷** | **no** (H₇) |
| 7 | 3 | 21 | True | True | True | ≡ 0 | ≡ 0 | **3x¹⁴** | **no** (H₇, H₁₄) |

(`—` = index out of range, deg < i+1.) By Lucas' theorem H_i(x^{mp}) =
C(mp,i) x^{mp−i} is nonzero iff p | i and p ∤ C(m, i/p): the "all derivatives
vanish" clause is **false in general** under Hasse — H₂(x⁶) = x⁴ ≠ 0 over F₂.
The hypothesis still holds for monomials, but only because gcd(x^{mp}, H_i)
always contains the factor x, not by vacuity.

### (B2) g = x^p + x^{2p} (f(Y) = Y + Y², f(0) = 0)

| p | deg | is_ca | is_ca_hasse | is_pure_power | H_1 | H_p | first failing i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 4 | True | **False** | False | ≡ 0 | 1 | **2** |
| 3 | 6 | True | **False** | False | ≡ 0 | −x³+1 | **3** |
| 5 | 10 | True | **False** | False | ≡ 0 | 2x⁵+1 | **5** |
| 7 | 14 | True | **False** | False | ≡ 0 | 2x⁷+1 | **7** |

H_p(x^p + x^{2p}) = C(2p,p) x^p + 1 = 2x^p + 1, which shares no root with
g = x^p(1 + x^p): gcd is constant, hypothesis fails at i = p for every prime.
Boundary check: with c₁ = 0 the polynomial reduces to the monomial x^{2p}
(Hasse-CA), with c₁ = 2 it fails for p = 3, 5, 7 (and passes for p = 2, where
2 ≡ 0 mod 2 — consistent, since the polynomial *is* the monomial there). So
Hasse-CA holds iff c₁ ≡ 0 mod p.

H_1(g) ≡ 0 in every row of both tables: the **first** derivative is vacuous
in both formulations (C(j,1) = j ≡ 0 mod p for j ∈ {p, 2p, mp}); what fails to
transfer is the *all* in "all derivatives vanish".

## Verdict

The clause "f(X^p) without constant term also works since all derivatives
vanish" is **ordinary-derivative vacuity and does not survive the Hasse
formulation**:

1. The Hasse derivatives of f(X^p) do **not** all vanish (H₂(x⁶) = x⁴ over
   F₂; H_p(x^{2p}) = 2x^p, etc.). Only H₁ ≡ 0 generically.
2. f(X^p) without constant term is **not Hasse-CA in general**: the two-term
   example x^p + x^{2p} fails the Hasse hypothesis at i = p for every prime
   p ∈ {2,3,5,7} (and for c₁ ≠ 0).
3. The only Hasse sense in which a *monomial* f(X^p) "works" is as a
   monomial: gcd(x^{mp}, H_i) ∋ x for every i — a root-sharing accident, not
   vacuity. Monomials are pure powers (x−0)^{mp} anyway, so they are not
   counterexamples.

```claim
id: charp-witness-xpp1-xp-hasse-recheck
statement: The clause "f(X^p) without constant term also works since all
  derivatives vanish" in claim charp-witness-xpp1-xp is ORDINARY-derivative
  vacuity and does not survive the Hasse formulation (H_i(f) = sum_j C(j,i) c_j
  x^{j-i}, the published char-p convention). For primes p in {2,3,5,7}: (i)
  the Hasse derivatives of g = f(X^p), f(0)=0, do NOT all vanish in general —
  H_2(x^{6}) = x^4 over F_2, H_p(x^{2p}) = 2 x^p over F_p — only H_1 is
  identically 0 (C(j,1) = j ≡ 0 mod p for j = mp); (ii) the two-term example
  g = x^p + x^{2p} (f(Y) = Y + Y^2) is NOT Hasse-CA: is_ca_hasse = False for
  every p in {2,3,5,7}, first failing index i = p (H_p = 2 x^p + 1, gcd with g
  constant), while is_ca (ordinary) = True vacuously; Hasse-CA holds for
  c_1 x^p + c_2 x^{2p} iff c_1 ≡ 0 mod p; (iii) monomial g = x^{mp} (m=1..3)
  is Hasse-CA for all tested (p,m) but only because gcd(x^{mp}, H_i) contains
  the factor x — a monomial root-sharing accident, not vacuity — and x^{mp} is
  a pure power (x-0)^{mp}, so no counterexample arises there. The genuine
  char-p witness remains x^{p+1} - x^p, which is Hasse-CA and not a pure power
  (checked again here for p = 2,3,5,7).
hypotheses: char K = p > 0, primes p in {2,3,5,7}, g = f(X^p) with f(0) = 0,
  degree <= 21
holds-here: yes
status: checked (two independent exact routes agree: canonical sympy oracle
  lib.casas_alvero.is_ca_hasse + lib.casasalvero.hasse_derivative, and a
  hand-rolled F_p Euclid-gcd implementation with no sympy/lib imports;
  56/56 cross-checks pass; captured
  code/out/ordinary-vs-hasse-charp-witness.captured.txt)
anchor: code/hasse_charp/recheck_xpp1_xp_hasse.py,
  code/hasse_charp/crosscheck_hasse_independent.py
falsifies: a (p, g) with p in {2,3,5,7}, g = f(X^p), f(0) = 0, where
  is_ca_hasse disagrees between the two routes, or where H_i(g) ≡ 0 for all
  i in 1..deg-1 for some g = x^p + x^{2p}.
```

Consequence for the source claim: `charp-witness-xpp1-xp` is correct in its
substantive part (x^{p+1} − x^p is a genuine char-p counterexample, and it
remains so under Hasse) but its "f(X^p) without constant term also works"
clause must be read as ordinary-derivative-only. Any later argument that uses
the clause as a Hasse witness, or that imports the vacuity "all derivatives
vanish" into a Hasse-convention statement, is unsupported — the correct Hasse
witness family is x^{p+1} − x^p (and its relatives such as x^{2p+1} − x^{2p}
in the class x^{mp}(x − 1) shape, cf. nonzero-H list for x^{p+1} − x^p), not
an arbitrary f(X^p).
