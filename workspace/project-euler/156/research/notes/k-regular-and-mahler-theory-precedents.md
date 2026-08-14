# Precedents for the 10-regular and Mahler generating-function approaches

The two proposed approaches (`research/approaches/regular-sequence-linear-representation.md`,
`research/approaches/mahler-generating-function.md`) were marked `precedent: _unchecked_` at
run start. This note pins their precedent to primary sources now on disk.

## The 1992 Allouche–Shallit paper itself is paywalled — recorded so nobody refetches

J.-P. Allouche and J. Shallit, "The ring of k-regular sequences", Theoret. Comput. Sci. 98
(1992) 163–197 (also STACS 1990, LNCS 415, 12–23) is behind Elsevier/Springer paywalls; a
legitimate free full text is not on the open web as of this cycle. **Do not re-search or
re-fetch it.** Its definitions and the three theorems this run needs are quoted verbatim in
two on-disk, freely-available primary sources:

- M. Coons, "Regular sequences and the joint spectral radius", arXiv:1511.07535
  (`research/sources/coons-regular-sequences-joint-spectral-radius.full.md`),
- D. Krenn and J. Shallit, "Decidability and k-regular sequences", arXiv:2005.09507v3,
  TCS 907 (2022) 34–44 (`research/sources/krenn-shallit-decidability-k-regular.full.md`).

## The three lemmas the regular-sequence approach needs, all quoteable from disk

**A–S Lemma 4.1 (linear representation).** Coons §1 states it in full: a sequence f is
k-regular iff there exist d×d matrices A_0..A_{k−1} and vectors v,w with
f(n) = w^T A_{i0}···A_{is} v, where (n)_k = i_s···i_0 is the base-k expansion of n.
Krenn–Shallit §1.4 restates it ([1, Theorem 2.2]) and gives a worked 2-regular example
(s2, the binary ones-count). This is the named theorem behind "a(n,d) = f(n,d) − n has a
finite matrix-product evaluator over the base-10 digits."

**A–S Theorem 3.1 (prefix-sum / summatory closure).** Krenn–Shallit, Theorem L proof:
"we construct g(m) = (p(...))² ... and f(n) = Σ_{0≤m<n} g(m). The sequence (f(n)) is
K-regular ... by [1, Theorem 3.1]." So the summatory of a k-regular sequence is k-regular —
the step that takes the per-number count c_d(n) to f(n,d) = Σ_{m≤n} c_d(m).

**A–S Theorem 6.1 (digit count is k-regular).** Krenn–Shallit Remark 1.1: "the number of
occurrences |z|_d of a digit d in the standard k-ary expansion z = (n)_k is a k-regular
sequence by [1, Theorem 6.1]", hence any polynomial in the per-digit counts is k-regular.

**A–S Theorem 2.10 (polynomial growth).** Krenn–Shallit §3.3: "for a k-regular sequence
with values in A there exists σ ≥ 0 such that f(n) ∈ O(n^σ); see [1, Theorem 2.10]." Coons
§1 states the same. This bounds f(n,d) and a(n,d) by n^σ — completes the theory, though
PE156's concrete bound comes from Khovanova–Marton Prop 9.1 (claim `G2-solution-bound`).

## The Mahler side, pinnings from this cycle

- **Mahler ⟺ regular-typological.** B. Adamczewski, J. P. Bell, D. Smertnig, "A height gap
  theorem for coefficients of Mahler functions", J. Eur. Math. Soc. 25 (2023) 2525–2571,
  arXiv:2003.03429 (`research/sources/abs-height-gap-mahler-regular.full.md`): a
  k-Mahler function is k-regular iff its coefficients have logarithmic Weil height O(log n);
  it is k-automatic iff the coefficients take finitely many values. This is the modern
  peer-reviewed statement of the Becker correspondence the Mahler approach cites.
  **Verified verbatim by the scholar this cycle** (Theorem 1.2, p.4): (a) k-automatic iff
  h(a_n) ∈ O(1) iff finite value set; (b) k-regular iff h(a_n) ∈ O(log n). Also Theorem 12.1:
  the growth class of a k-Mahler function is decidable. Summary:
  `research/summaries/abs-height-gap-mahler-regular.md`.
- **Stephan's divide-and-conquer g.f. classification.** R. Stephan, "Divide-and-conquer
  generating functions, Part I: Elementary sequences", arXiv:math/0307027
  (`research/sources/stephan-divide-and-conquer-generating-functions.full.md`): DC
  sequences (a_{2n} = f(a_n), a_{2n+1} = g(a_n)) have Mahlerian/DC ordinary generating
  functions; §2.4 gives the binary ones-count as an instance. Base-2 framing of the same
  phenomenon A094798 exhibits in base 10. Preprint, largely empirical — a structural lead,
  not a theorem to rest on.
- **Joint spectral radius.** Coons Theorem 1: for a k-regular sequence, log_k ρ(A_f) equals
  the growth exponent GrExp(f) = limsup log|f(n)|/log n. This is the machinery that makes
  the k-regular viewpoint quantitative; recorded for completeness, not needed by the solver.
  **Verified verbatim by the scholar this cycle** (Theorem 1 + proof, Propositions 4 & 6,
  Corollary 7, Appendix A). Summary: `research/summaries/coons-regular-sequences-joint-spectral-radius.md`.

## Scholar verification note (this cycle)

The three claims below (`as-linear-representation`, `as-digit-count-and-prefix-closure`,
`coons-growth-exponent-joint-spectral-radius`) are marked `holds-here: holds` in this
note and were **verified against the full texts on disk**: Coons arXiv:1511.07535
(linear-representation theorem quoted in §1; Theorem 1, Propositions 4/6, Corollary 7
verified) and Krenn–Shallit arXiv:2005.09507v3 (Remark 1.1, Theorem A, Theorem L proof,
§1.4, Proposition 3.5/3.6 verified; summaries written). The `abs-mahler-regular-height-ologn`
claim was verified against Adamczewski–Bell–Smertnig arXiv:2003.03429v2 Theorem 1.2.

```claim
id: as-linear-representation
statement: >
  A sequence f over a field K is k-regular iff there exist a positive integer d, matrices
  A_0,...,A_{k-1} in K^{d×d}, and vectors v, w in K^d such that
  f(n) = w^T A_{i0}···A_{is} v for every n, where (n)_k = i_s···i_0 is the base-k expansion
  of n (Allouche–Shallit [1, Lemma 4.1], stated in full in Coons arXiv:1511.07535 §1 and
  restated in Krenn–Shallit arXiv:2005.09507v3 §1.4 as [1, Theorem 2.2]).
hypotheses: >
  K a field of characteristic zero (fine over ℤ/ℚ for PE156); k ≥ 2 integer; f: Z≥0 → K.
holds-here: yes (k=10, d∈{1..9}: a(n,d) = f(n,d) − n is 10-regular over ℤ, giving a
  matrix-product evaluator over the base-10 digit string — a fourth, structurally
  independent evaluator, distinct from the place-value peel, MSD block sums, and
  digit-DP already implemented and verified this run)
status: checked (verified verbatim against Coons arXiv:1511.07535 §1 and
  Krenn–Shallit arXiv:2005.09507v3 §1.4 / [1, Theorem 2.2], full texts on disk)
bearing: >
  Precedent for the open approach `regular-sequence-linear-representation`; makes the
  proposed linear representation a named theorem rather than a guess.
anchor: research/sources/coons-regular-sequences-joint-spectral-radius.full.md
```

```claim
id: as-digit-count-and-prefix-closure
statement: >
  (i) For base k, the per-number digit-count |(n)_k|_d is a k-regular sequence
  (Allouche–Shallit [1, Theorem 6.1]). (ii) The summatory (prefix-sum) of any k-regular
  sequence is k-regular ([1, Theorem 3.1]). Hence c_d(n) and f(n,d) = Σ_{m≤n} c_d(m) are
  both 10-regular, and so is a(n,d) = f(n,d) − n (closure under sums).
hypotheses: k ≥ 2; d ∈ {0,...,k−1}; statements quoted in Krenn–Shallit arXiv:2005.09507v3
  (Remark 1.1 for (i), Theorem L proof for (ii)).
holds-here: yes (k=10, d∈{1..9}: c_d(10n+r) = c_d(n) + [r=d], so the 10-kernel is
  generated over ℤ by {c_d, 1} — the elementary proof of (i) for d≠0; (ii) is the
  summatory-closure step taking c_d(n) to f(n,d))
status: checked (verified verbatim against Krenn–Shallit arXiv:2005.09507v3
  Remark 1.1 and Theorem L proof, full text on disk)
bearing: >
  Justifies the claim in approach `regular-sequence-linear-representation` that a(n,d) is
  10-regular and hence has a finite linear representation.
anchor: research/sources/krenn-shallit-decidability-k-regular.full.md
```

```claim
id: abs-mahler-regular-height-ologn
statement: >
  A k-Mahler function is k-regular if and only if its coefficients have logarithmic Weil
  height O(log n); over a characteristic-zero ground field it is k-automatic if and only if
  its coefficients take finitely many values (Adamczewski–Bell–Smertnig, JEMS 25 (2023)
  2525–2571, arXiv:2003.03429).
hypotheses: >
  f(z) = Σ a_n z^n satisfies a linear k-Mahler functional equation; coefficients algebraic.
holds-here: yes (the digit-count generating function — A094798 instance
  g(x) = x/((1−x)(1−x^10)) + ((1−x^10)/(1−x))^2 g(x^10) — is 10-Mahler with integer
  coefficients, so height O(log n) is automatic; the theorem confirms the
  generating-function route is on classical ground)
status: checked (verified verbatim against Adamczewski–Bell–Smertnig
  arXiv:2003.03429v2 Theorem 1.2, full text on disk)
bearing: >
  Precedent for the open approach `mahler-generating-function`; pins the Mahler ⟺ regular
  correspondence to a named modern theorem with hypotheses.
anchor: research/sources/abs-height-gap-mahler-regular.full.md
```

```claim
id: coons-growth-exponent-joint-spectral-radius
statement: >
  For a (not eventually zero) k-regular sequence f over a characteristic-zero field, with
  A_f any set of k integer matrices associated to a basis of the K-span of the k-kernel,
  log_k ρ(A_f) = GrExp(f) := limsup_{n→∞, f(n)≠0} log|f(n)|/log n (Coons, arXiv:1511.07535,
  Theorem 1; holds with ℤ in place of K by the Noetherian-ring remark).
hypotheses: f k-regular over characteristic-zero K; A_f associated to a basis (not merely a
  spanning set) of ⟨Ker_k(f)⟩.
holds-here: yes (a(n,d) = f(n,d) − n is 10-regular over ℤ, so the theorem classifies
  its growth exactly via the joint spectral radius of the 10-kernel matrices;
  confirmatory theory only — PE156's search bound comes from Khovanova–Marton
  Prop 9.1, G2-solution-bound)
status: checked (verified verbatim against Coons arXiv:1511.07535 Theorem 1,
  Propositions 4 & 6, Corollary 7, full text on disk)
bearing: >
  Quantitative completion of the k-regular viewpoint; would let the matrix evaluator be
  certified for correctness-by-construction, and it is what makes the regular-sequence
  route a genuine alternate evaluation engine rather than arithmetic disguised.
anchor: research/sources/coons-regular-sequences-joint-spectral-radius.full.md
```

```claim
id: stephan-dc-generating-functions-classification
statement: >
  Divide-and-conquer sequences (a_{2n} = f(a_n,n), a_{2n+1} = g(a_n,n)) have ordinary
  generating functions satisfying Mahlerian homogeneous equations
  c_0(z)F(z)+c_1(z)F(z^2)+···+c_N(z)F(z^{2^N}) = 0, or DC-type equations with a right-hand
  side b(z). The paper exhibits explicit families (2.1)–(2.6) with attached recurrences;
  with α=1, c=0, d=1 the family (2.4) yields the binary ones-count e_1(n) (A000120) with
  g.f. 1/(1−z) Σ z^{2^k}/(1+z^{2^k}) (Stephan, arXiv:math/0307027, preprint).
hypotheses: base-2 recurrences; preprint asserts the catalog backed by computation to index
  100+, "formal proofs" left open.
holds-here: partial (it is base-2 framing of the same digit-count-generating-function
  phenomenon that A094798 exhibits in base 10; it describes the family but is not a
  theorem to rest the solve on)
status: sourced (arXiv preprint, on disk; cited by Adams-Watters–Ruskey JIS 2009, on disk)
bearing: >
  Confirms the generating-function reformulation of digit counts is a recognized subject
  (divide-and-conquer / Mahler type); background tier for approach `mahler-generating-function`.
anchor: research/sources/stephan-divide-and-conquer-generating-functions.full.md
```