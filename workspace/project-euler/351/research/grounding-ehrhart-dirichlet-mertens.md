# Grounding of the three proposed PE-351 approaches

All three candidates in `research/approaches/` were taken to the literature and
grounded. Status: **grounded** for each (precedent filled, no refutation found).

## 1. `ehrhart-mobius-hexagon` — Ehrhart theory + Möbius inversion

**What it is called:** Ehrhart theory for lattice polygons (Ehrhart 1959/62;
Beck–Robins, *Counting Lattice Points in Polytopes* §3). The hexagon
{|x|,|y|,|x+y|≤n} is a lattice polygon; its Ehrhart polynomial counts points
in the dilate tP.

**The collapse is exact** (previously marked speculative). With
L_P(t) = 3t²+3t+1:

    P(n) = 1 + Σ_{d≤n} μ(d)(L_P(⌊n/d⌋) − 1)
         = 1 + 3 Σ_d μ(d)⌊n/d⌋(⌊n/d⌋+1)
         = 1 + 6Φ(n)            [summatory-totient-mobius-identity]
    H(n) = L_P(n) − P(n) = 3n²+3n−6Φ(n). ✓

The only non-trivial ingredient, the summatory-totient Möbius identity
Φ(n) = (1/2)Σ_d μ(d)⌊n/d⌋(⌊n/d⌋+1), is a sourced ledger claim. Every theorem
invoked has hypotheses that hold: the hexagon is a lattice polygon, tP is the
order-t orchard, and primitive-point splitting (visible iff gcd=1) is the
Baake–Grimm–Warrington/Martin theory already in the library.

**Buy:** a new *derivation* of the closed form; grounding in Ehrhart/visible-
point theory. Not a faster computation — it collapses to the same Φ(n).

## 2. `dirichlet-hyperbola-gauss-2-3` — Gauss recursion, Θ(n^{2/3})

**What it is called:** the fast-prefix-sums / Dirichlet-hyperbola method
("Dujiao sieve" in CP circles). The recursion Φ(n)=n(n+1)/2 − Σ_{d=2..n}Φ(⌊n/d⌋)
is exact (Gauss identity rearranged), visits O(√n) distinct floor quotients,
and with a φ/Φ prefix up to n^{2/3} gives Θ(n^{2/3}) time, Θ(n^{1/2}) space.

**Sources:** Kulkov, Codeforces blog entry 117635 (general framework, claims
all-floor-quotient prefix sums in O(n^{2/3})); Brown arXiv:2506.07386
(Θ(n^{2/3}) totient sum). Chai Wah Wu's A063985 recursion (`totient-sum-fast-
recursion`) is the same floor-grouped recursion for the cototient partial sums.

**Buy:** a genuinely second, independent sublinear route to Φ(10^8)/H(10^8),
different object (summatory Φ) and different complexity class than the φ-sieve.

## 3. `mertens-first-lehman-rivat` — Mertens first, Θ(n^{2/3})–Θ(n^{3/5})

**What it is called:** Mertens-first / Meissel–Lehmer / Deléglise–Rivat method.
Distinct intermediate object: the Möbius summatory M, not Φ.

**Ingredients (all sourced ledger claims + primary papers):**
- Lehman identity (Deléglise & Rivat 1996, Exp. Math. 5(4):291–295,
  DOI 10.1080/10586458.1996.10504594) → `lehman-mertens-identity`.
- DR recursion → `mertens-recursion`, O(x^{2/3}) time.
- Mertens-first totient formula (Brown arXiv:2506.07386) → `mertens-first-totient-formula`.
- Helfgott–Thompson O(x^{3/5}) improvement (Res. Number Theory 9(1):6 2023,
  DOI 10.1007/s40993-022-00408-8) → `heath-brown-mobius-identity`.
- DR 1998 (Computing ψ(x), DOI 10.1090/S0025-5718-98-00977-6) independent
  lineage confirmation for the Meissel–Lehmer family.

**Buy:** a third independent sublinear route to the same final answer, with a
well-developed analytic lineage.

## Caveats (refute-on-evidence, not absence)

- No published PE-351 answer or solution was sought (that would invalidate the
  run); the grounding is about the *named theory* each candidate invokes being
  genuine, standard, with hypotheses that hold, and in two cases already
  implemented in the cited literature.
- Why I did NOT mark any as refuted: each candidate's core theorem is
  textbook, each was found in multiple independent sources, and each reduces to
  the already-known closed form H(n)=3n²+3n−6Φ(n). Refutation would require a
  source showing one of the routes is invalid here — none was found.

## Files updated

- `research/approaches/ehrhart-mobius-hexagon.md` → grounded
- `research/approaches/dirichlet-hyperbola-gauss-2-3.md` → grounded
- `research/approaches/mertens-first-lehman-rivat.md` → grounded
- Cogeene memory updated with the grounding verdict.
