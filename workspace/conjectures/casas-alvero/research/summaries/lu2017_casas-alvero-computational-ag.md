# Lu, *Casas-Alvero conjecture in computational algebraic geometry* (2017, arXiv:1707.04754)

<!-- source: https://arxiv.org/pdf/1707.04754 | preprint -->

## What this source is

A 2017 preprint by Zhipeng Lu claiming a proof of CA via computational
algebraic geometry: parameterized derivatives, Combinatorial Nullstellensatz,
Noether normalization, regular sequences, and dimension counts over ℂ and over
finite fields.

## What it claims

- **Theorem 1.1**: dim_C CA_n = 1 for all n ≥ 1 (the variety of CA polynomials
  is 1-dimensional — this is the *equivalent reformulation* of CA itself: CA
  says the CA variety is the 1-dimensional locus of pure powers (x−a)^n, so
  dimension-1 alone is not the conjecture, but the paper claims more).
- Theorem 1.2/1.3: for f = ∏(x−x_i) with the derivative-polynomials
  f^(j)(x_i) as polynomials in the root coordinates x_1,…,x_n (K = ℂ or
  char(K) large ≫ n!), the variety Z(f^(1)(x_{i1}),…,f^(n−1)(x_{i_{n-1}}))
  has dimension 1.
- **Proposition 2.3**: CA holds for n iff for large primes p ≫ n, over F_p the
  variety Z(f^(1)(x_{i1}),…,f^(n−1)(x_{i_{n-1}})) has size p, "for any branch".
- Proposition 4.1–4.5: over F_p, |V(J)| = p iff |V(J)| < p^2, and (Prop 4.5)
  for each k there is m_k with x_k^{m_k} ∈ LM(J), J = ⟨H_1,…,H_{n−1}⟩,
  H_i(x_i) the derivative-polynomials.

## Status — claimed proof, suspect char-p relation

This is another entry in the claimed-proof family (Battiston withdrawn,
Fernández de las Heras unpublished, Yakubovich unpublished, Ghosh unverified,
Lu 2017 preprint). Crucially for this run it appears to **fall directly into
the char-p trap**: Proposition 2.3 reduces the char-0 conjecture to a count
over F_p of size p, and §4 proves those F_p statements. Since **CA is false in
char p** (x^{p+1}−x^p etc.), any argument whose core is a char-p computation
must be stating a false or vacuous char-p theorem, or its reduction step
(2.3) is where the char-0-only content hides. The natural reading: the "size p"
over F_p corresponds to the pure-power branch, and the char-p counterexamples
live in other branches — so the claim that dimension/size counts *prove* the
conjecture needs the missing step that rules those branches out, which the
paper does not appear to supply.

**Char-p test**: run Prop 2.3's counting claim for n = p+1 against the known
char-p counterexamples — the count of F_p-points must NOT be p for those
branches if the claim is to be consistent.

## Bearing

- Documents another claimed proof whose char-0-only step is not located
  (per GOAL.md's test: an argument that also proves the char-p statement is
  refuted). Lu's Prop 2.3 is exactly the kind of "reduction to large-prime
  counting" that the char-p counterexamples are designed to break.
- The regular-sequence / dimension-1 machinery is a known dead-end-adjacent
  technique for CA; it does not by itself separate char 0 from char p.

## Status labels

- Claimed proof: **asserted-by-source (preprint), unverified, suspect**.
- Its char-p reduction (Prop 2.3): **unverified here; flagged for the oracle
  test** — not established by this run.