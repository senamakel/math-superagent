# Novelty check — block-transfer classification for PE156 (f_d(x)=x)

**Question asked.** Is the following classification theorem already named/known in the
literature, and is there a closed form for S0(d), or is it still enumerated?

**Theorem (this run, proven and verified).** For 1 ≤ d ≤ 9 and 0 ≤ k ≤ d−1, the map
x ↦ k·10^10 + x is a bijection from the solutions of f_d(x)=x with x < 10^10 onto the
solutions in block k, because f_d(k·10^m + x) − f_d(x) = k·m·10^(m−1) for 0 ≤ x < 10^m and
k < d. Consequence: s(d) = d·Σ_{x∈S0} x + (d(d−1)/2)·10^10·|S0|, where S0 is the solution
set in [0, 10^10).

## Verdict

**The block-transfer / self-similarity statement is NOT novel — it is stated, with an
explanation, in Khovanova & Marton, "Archive Labeling Sequences", and the rest of the
theorem (the equal-block-count consequence) is an immediate corollary already drawn in the
paper.** What is novel in this run's contribution is narrower: the general-m residue
identity, the derived closed-form sum formula s(d), and the systematic verification —
none of which appear in K&M or anywhere else found.

## (1) Is the block-transfer stated in Khovanova–Marton arXiv:2305.10357 (on disk) or elsewhere?

**Yes.** It is stated in the arXiv v2 (section 4, right after Table 2) — the same section
that introduces the E_d sequences:

> "However, if we did start at zero, and thus add 1 to the last column, we see a neat
> pattern: the result is divisible by d. This hides an even more interesting fact: the
> actual values of E_d are periodic modulo 10^10, while being bounded by d·10^10; the
> latter fact is proven in Proposition 9.1. To explain periodicity, we observe that for
> 0 ≤ x < (d−1)10^10, we have f_d(x+10^10) = f_d(x) + 10^10. It follows that the numbers x
> and x+10^10 are either both members of the sequence E(d) or both non-members. Thus the
> number of the solutions to the equation f_d(x)=x in the range [0, …, 10^10−1] is the
> same as in the range [r10^10, …, (r+1)10^10−1], when r < d. Hence, we have d ranges with
> the same number of solutions, which explains the divisibility of A130432(d) by d."

This is exactly the "block-transfer with m=10, k=1": the shift by 10^10 maps solutions to
solutions (and non-solutions to non-solutions), so the blocks [r·10^10, (r+1)·10^10) for
r < d each contain a translate of the seed set [0, 10^10). Combined with Prop 9.1
(n ≤ d·10^10, which the arXiv proves in §9 and the AMM states in §4), the d-block
decomposition follows — the bijection is a one-line reading, though the AMM/arXiv do not
write the "bijection" word and do not give the derived sum formula.

**The published version** (Amer. Math. Monthly 132(8) (2025) 780–787,
DOI 10.1080/00029890.2025.2525050; CC-BY copy on disk at
`research/sources/archive-labeling-amm-published.full.md`) contains the same passage in
Section 4, with an added explanation ("This is due to the fact that only the last ten
digits contribute to the count, because if the number has 11 digits, then the first digit
is less than d. In addition, the last ten digits go through all possible 10-digit strings
when the number changes from x+1 to x+10^10. Thus the count of the number of digits d
increases exactly by 10^10.").

**The arXiv v1** (`research/sources/archive-labeling-arxiv-v1.full.md`) does **not**
contain the periodicity paragraph — v1 Section 4 stops at the A130432 divisibility remark
without explaining it. The paragraph was added in v2 (16 Feb 2024) and carried into the
published AMM.

**Also on disk (catalogue structure only):** OEIS A130432's terms (counts) and the
divisibility comment; the A014778 entry records Wasserman's run-structure comment for
d=1 (six runs of ten, ten pairs, four isolated) and the finiteness proof.

**Elsewhere.** Multiple web searches (research paper category and open web) found no other
named statement of the block structure, the shift identity, or the seed-set reduction.
The only nearby hits are:
- Morrow, "A digit function with infinitely many 1-cycles", Math. Gazette 86 (2002) —
  a digit-sum dynamics piece, different function, no block structure.
- Stewart (Can. J. Math., 1960), Adams-Watters–Ruskey (JIS 2009), Stephan
  (math/0307027), Allouche–Shallit k-regular theory, Adamczewski–Bell–Smertnig —
  the digit-count generating-function / regular-sequence family, all on disk; none
  discuss fixed points of f_d(x)=x or the block decomposition.

## What K&M do NOT state (the genuinely new parts of this run's contribution)

1. **The general-m residue identity** f_d(k·10^m + x) − f_d(x) = k·m·10^(m−1) for
   0 ≤ x < 10^m, k < d. The paper gives only the m=10, k=1 case, and only in words
   ("the last ten digits go through all possible 10-digit strings").
2. **The closed-form sum** s(d) = d·Σ_{x∈S0} x + (d(d−1)/2)·10^10·|S0|. K&M list Table 3
   (maxima) and A130432 (counts) but never the per-digit sums or a sum formula. (The
   per-digit sums s(1..9) are the PE156 answer and appear only as OEIS A216398, which
   this run deliberately does not read — see `research/notes/oeis-catalogue-pe156.md`.)
3. **The verification** that the block-0 seed sets per digit are
   |S0| = [84,7,12,12,1,12,7,43,1] and ΣS0 = [22786974071, 1868991481, 4215999875,
   5499999885, 0, 105783999905, 58131008510, 409040935919, 0] (OEIS lookup misses
   recorded earlier).

## (2) Is there a known way to get S0(d) itself in closed form, or is it still enumerated?

**Still enumerated, as far as this check can establish — and S0(d) shows no known closed
form.** Evidence:

- **OEIS lookup misses (this run).** The block-0 count sequence N0(d) = [84,7,12,12,1,12,7,43,1]
  and the block-0 sum data are **not** OEIS-catalogued (`research/notes/pattern-findings-block-structure.md`
  records both misses; no closed form, recurrence, or generating function surfaced).
- **K&M** enumerate E_d computationally (their §7 algorithm, unbounded binary search) and
  do not give a closed form for the seed set or for the counts.
- **No analytic form found.** Searches for "closed form" / "seed set" / explicit
  formulas for the solutions of f_d(x)=x in [0, 10^10) returned nothing published.
  The d=1 set has a partially described shape (six runs of ten, ten pairs, four isolated
  numbers — OEIS A014778 comment) but that is descriptive, not a closed form, and it is
  specific to d=1.
- **Structural reason (run's own analysis).** The seeds are exactly the solutions of
  f(n,d)=n below 10^10; they are not digit-arithmetic objects of any fixed pattern, and
  the run's sequence tools found no linear recurrence of order ≤ 12 for N0(d). So S0(d)
  is best described as an **enumerated object** (finite, computable by the jump iterator
  in ~86k f-evaluations per digit), not a closed-form one.

## Sources (on disk unless noted)

- Khovanova & Marton, Archive Labeling Sequences, arXiv:2305.10357v2 [math.HO], 16 Feb
  2024 — **§4 periodicity passage** (`research/sources/archive-labeling-arxiv-latest.full.md`);
  **Prop 9.1 bound**; §7 algorithm. https://arxiv.org/abs/2305.10357 (html v2
  https://arxiv.org/html/2305.10357v2)
- Khovanova & Marton, Archive Labeling Sequences, Amer. Math. Monthly 132(8) (2025)
  780–787, DOI 10.1080/00029890.2025.2525050 — same §4 passage
  (`research/sources/archive-labeling-amm-published.full.md`, from MIT DSpace
  https://dspace.mit.edu/bitstream/handle/1721.1/163207/UAMM_A_2525050_O.pdf)
- arXiv v1 (25 Apr 2023) — periodicity paragraph absent
  (`research/sources/archive-labeling-arxiv-v1.full.md`); https://arxiv.org/pdf/2305.10357v1
- OEIS A014778/A130432 comments (`research/sources/oeis-A014778-main.full.md`,
  `research/sources/oeis-search-fixed-points.full.md`); https://oeis.org/A014778
- Run's own analysis: `research/notes/pattern-findings-block-structure.md`,
  `research/approaches/block-transfer-classification.md`,
  `research/notes/oeis-catalogue-pe156.md`
- Morrow, A digit function with infinitely many 1-cycles, Math. Gazette 86(505) (2002),
  DOI 10.2307/3621591 — unrelated digit function, kept as a "considered and rejected" lead.
- Exa searches this cycle and prior citation-status record:
  `research/notes/km-citation-and-corroboration-map.md` (ADS 0 citations as of last check).

## Bottom line

- The block-transfer/self-similarity classification is **already published in
  Khovanova–Marton** (both arXiv v2 §4 and AMM 2025 §4), where the one-step m=10 shift
  identity, the membership equivalence, and the equal-block-count consequence are stated
  explicitly. The run's theorem is therefore **not novel as a theorem**; it is a
  re-derivation and generalization of K&M's periodicity remark.
- The **novel** ingredients are the general-m identity (k·m·10^(m−1)), the closed-form
  s(d) expression for the sums, and the verification data (N0, S0 per digit). None of
  these was found anywhere in the literature.
- S0(d) has **no known closed form** and is still an enumerated object; the literature
  and OEIS give no formula, and the run's own sequence-tool misses support that.