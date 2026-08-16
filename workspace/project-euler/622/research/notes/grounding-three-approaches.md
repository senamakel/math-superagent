# Grounding the three proposed approaches in the literature

Research role report. Each proposed reformulation taken to the literature; per
candidate: what it is called, the precise theorem it relies on and whether its
hypotheses hold here, precedent, and what it buys. Status set on each approach
file. Arithmetic underpinning was already machine-checked and recorded in the
claim library (three independent programs: solution.py, verify_answer.py,
pattern_verify.py — claim `pe622-answer-order-sixty`); a fresh verification
program is filed at `code/pe622/research_verify.py` for tool_builder to run.

## 1. Zsigmondy primitive-prime-divisor classification — GROUNDED

**What it is called.** Zsigmondy's theorem (1892), independently Birkhoff &
Vandiver; the "primitive prime divisor" / "Zsigmondy prime" theorem. The
order-classification it drives (primes of 2^n−1 partition by ord_p(2)) is the
standard cyclotomic-polynomial structure: 2^n−1 = ∏_{d|n} Φ_d(2), and p is a
primitive (order-n) prime divisor of 2^n−1 iff p | Φ_n(2), i.e. ord_p(2)=n.

**Precise statement + hypotheses.** (Avci, arXiv:2011.06136, downloaded
`research/sources/avci-large-zsigmondy-primes.full.md`; clean form in
Huppert–Blackburn via the Cambridge conjugacy-classes paper, Thm 2.4):
For coprime positive integers a > b and n ≥ 2, a^n − b^n has a primitive prime
divisor p (p | a^n−b^n but p ∤ a^k−b^k for all 1 ≤ k < n) **except** for
(a,b,n) = (2,1,6) and, for n=2, a+b a power of 2. For a=2, b=1: the sole
exception is n=6 (2^6−1 = 63 = 3²·7, no primitive divisor), plus n=2
(a−b=1→2^2−1=3, primitive divisor exists). All other n ≥ 2 have a primitive
prime divisor.

**Hypotheses hold here.** We need n = 60 (each d | 60). 60 ≠ 6, so every Φ_d(2),
d | 60, d ≥ 2 has a primitive prime divisor — each order class of the 11 primes
{3,5,7,11,13,31,41,61,151,331,1321} of 2^60−1 is nonempty, matching the recorded
orders {2,4,3,10,12,5,20,60,15,30,60}. The inventor's "order-6 class empty"
check is exactly Zsigmondy's (2,1,6) exception: 2^6−1=63=3²·7 has no order-6
prime. Since Φ_6(2) divides 2^60−1 but contributes no prime of order 6, the
lcm=60 condition is unaffected — sound.

**Wieferich lift.** ord_{p^a}(2) = ord_p(2)·p^{a−1} when p is not Wieferich
(p^{ord_p(2)} ≢ 1 mod p²). This is claim `wieferich-lift-order` in the library
(proof: Packard Cor 4.2, Chappelon Thm 3.6 — both held under
`research/sources/`). Kiriu–Mejía (arXiv:2201.02751) give the general form
ord_{p^e}(2) = p^{e−e0}·ord_p(2) with e0 the largest exponent with
ord_{p^{e0}}(2)=ord_p(2); since v_p(2^{ord_p(2)}−1)=1 for all 11 primes
(machine-checked, none is Wieferich — the known base-2 Wieferich primes 1093,
3511 do not divide 2^60−1), equality holds for every a. Hypotheses (odd prime p,
gcd(2,p)=1) hold.

**What it buys.** ord_m(2) = lcm_i ord_{p_i^{a_i}}(2) (claim
`order-lcm-over-prime-powers`, proved, sourced to Naor Thm 6.1.32 + Chappelon
Prop 5) turns "ord_m(2)=60" into the local condition lcm_i(d_p·p^{a−1}) = 60
over the 11 primes with exponents a ≤ v_p(2^60−1) (a ≤ 2 for p=3,5, else a ≤ 1).
This gives an explicit classification of the 4456 moduli and a multiplicative
(Euler-product-like) formula for S(60), genuinely orthogonal to the skeleton's
inclusion-exclusion over the modulus's divisors. Cautions: (i) Zsigmondy is
supporting, not load-bearing — the classification's arithmetic works from the
order data alone, so Zsigmondy guarantees the full range of orders rather than
computing anything; (ii) the "Euler-factor decoupling" write-up is the only
speculative part and should be derived explicitly, but the underlying
local/global lcm splitting is standard. status: **grounded**.

## 2. Kernel-verified divisor recursion — GROUNDED (mathematics), kernel budget open

**What it is called.** This is not a named theorem — it is the certificate
pattern plus the standard CRT decomposition. The mathematics it rests on: the
divisor lattice of m = ∏ p_i^{a_i} is the product of exponent-chains
([0,a_i] per prime), so counting/summing divisors with a predicate is a
structural product recursion; the order-60 predicate decouples per prime power
via the CRT order-lcm (claim `order-lcm-crt-sourceable`, sourced to TCD Thm 5.4
+ Naor Ex 6.1.20) and order-divisibility (claim `order-divisibility-conrad`,
Conrad Thm 2.1).

**Precise statement.** ord_{n1·n2}(a) = lcm(ord_{n1}(a), ord_{n2}(a)) for
gcd(n1,n2)=1 (finitely many factors), and ord_m(2) | d ⟺ m | 2^d−1. Hypotheses
(gcd(2,m)=1, i.e. m odd) hold here — the witten criterion is exactly
"m | 2^60−1 and m ∤ 2^{12}−1, 2^{20}−1, 2^{30}−1" as in the skeleton's G-ord
criterion. The recursion correctly enumerates {m : ord_m(2)=60} because the
divisor set of a factored number is a Cartesian product of chains (finitely
many primes ⇒ finite recursion depth 11; τ(2^60−1)=4608 leaves).

**Precedent.** The CRT/lcm order decomposition that makes the recursion correct
is standard and already in the library as proven, sourced claims. Nobody in the
library has applied it in Lean; the feasible question is whether Mathlib's
kernel unfolds an 11-deep, 4608-leaf recursion inside the lean_check timeout
without native_decide. That is an engineering/engine-budget question, not a
literature question, so the literature neither supports nor refutes feasibility
— it is honestly untested. The mathematics is grounded; the kernel-unfold budget
is the open risk the file already names. status: **grounded** (mathematics),
with the explicit caveat that the speculative part is not answerable from the
literature and must be tested in Lean.

## 3. Möbius inversion on the exponent lattice — GROUNDED

**What it is called.** Möbius inversion (Rota's poset Möbius inversion in
finitary arithmetic form). The application — extract "exact order k" from
"order divides d" over d | k — is the canonical Möbius-inversion/convolution
trick (element counts by order; see the "how many integers have order n"
literature, e.g. the cycle-counting and Jordan-totient-generalisation papers;
Moree's distribution work uses the same inclusion-exclusion over orders).

**Precise statement.** For arithmetic F, f: F(n)=Σ_{d|n}f(d) for all n ⟺
f(n)=Σ_{d|n}μ(n/d)F(d). Applied via ord_m(2)|d ⟺ m|2^d−1 (Conrad Thm 2.1):
C(k)=Σ_{d|k}μ(k/d)(τ(2^d−1)−1) and S(k)=Σ_{d|k}μ(k/d)(σ(2^d−1)−1). Hypotheses
(m odd, gcd(2,m)=1) hold. This is claim `mobius-inversion-sourceable`, already
proved and sourced (Stanford Möbius-inversion notes + Conrad), and
machine-verified for k=1..60 in `code/pe622/verify_answer.py`.

**What it buys / proximity.** True for all k (general-parameter, stronger than
the skeleton's {12,20,30} coincidence); at k=60 a signed sum of eight σ-values.
Honest caveat confirmed by the literature: it is the same number-theoretic
family as the skeleton's divisor-lattice weighting (both are a divisor-lattice
convolution), so it is not orthogonal to the skeleton — but it is a valid,
fully-general, independently-verifiable route. status: **grounded** (and the
flagged proximity is accurate).

## Claim

```claim
id: zsigmondy-primitive-prime-divisor
statement: For coprime positive integers a > b and n >= 2, a^n - b^n has a
  primitive prime divisor p (p | a^n - b^n, p not dividing a^k - b^k for all
  1 <= k < n) except when (a,b,n) = (2,1,6), and for n = 2 when a + b is a
  power of 2. For a=2,b=1 the single exception is n=6; consequently each
  cyclotomic factor Phi_d(2), d >= 2, d != 6, has a prime p with ord_p(2) = d,
  so each order class {p : ord_p(2) = d} among the primes of 2^60-1 is
  nonempty for every d | 60, d != 1 (the d=6 class is exactly Zsigmondy's
  exception: 2^6-1 = 63 = 3^2*7 has no order-6 prime).
hypotheses: gcd(a,b) = 1; a,b,n as stated; the order-class application needs
  the classification of primes of 2^n-1 by ord_p(2) (p | Phi_d(2) iff
  ord_p(2) = d).
holds-here: yes (60 != 6, so every phi_d(2), d | 60, has a primitive divisor).
bearing: certifies each primitive-order class {p : ord_p(2)=d}, d | 60, is
  nonempty, and confirms the order-6 class is empty (Zsigmondy exception) —
  the justification that the lcm=60 prime-power classification is complete.
status: sourced
anchor: Avci arXiv:2011.06136 (Zsigmondy + large-Zsigmondy statement);
  Cambridge conjugacy-classes paper Thm 2.4 (Zsigmondy prime existence);
  Schinzel, Proc. Camb. Phil. Soc. (primitive prime factors of a^n-b^n).
```

## Sources

- Avci, "Large Zsigmondy Primes", arXiv:2011.06136 —
  https://arxiv.org/pdf/2011.06136 (downloaded; Zsigmondy statement)
- Schinzel, "On primitive prime factors of a^n−b^n", Proc. Camb. Phil. Soc. —
  https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/abs/on-primitive-prime-factors-of-anbn/FF4F8CB4D5BEDD2854151670559F36C6
- Cambridge, "Prime divisors and the number of conjugacy classes…", Zsigmondy
  Thm 2.4 — https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/prime-divisors-and-the-number-of-conjugacy-classes-of-finite-groups/79A16F6CD21CA87BDF4B5E578387FC1F
- Kiriu–Mejía, "Some notes about power residues modulo prime", arXiv:2201.02751
  (order lift ord_{p^e}(2)=p^{e−e0}ord_p(2)) —
  https://arxiv.org/abs/2201.02751
- Library claims (proved, sourced): `order-lcm-over-prime-powers`/CRT (Naor
  Thm 6.1.32, Chappelon Prop 5), `wieferich-lift-order` (Packard Cor 4.2,
  Chappelon Thm 3.6), `order-divisibility-conrad` (Conrad Thm 2.1),
  `mobius-inversion-sourceable` (Stanford notes + Conrad), `pe622-answer`,
  `outshuffle-order-equals-ord` (Diaconis–Graham–Kantor Lemma 1).
- Stanford Möbius inversion: crypto.stanford.edu/pbc/notes/numbertheory/mobius.html
- Conrad, "Orders of units in modular arithmetic":
  kconrad.math.uconn.edu/blurbs/ugradnumthy/ordersmodm.pdf
