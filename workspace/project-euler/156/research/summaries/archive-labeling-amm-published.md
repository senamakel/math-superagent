# Khovanova & Marton, "Archive Labeling Sequences" — published AMM version

**Source:** https://dspace.mit.edu/bitstream/handle/1721.1/163207/UAMM_A_2525050_O.pdf (CC-BY; DOI 10.1080/00029890.2025.2525050; Amer. Math. Monthly 132(8), 2025, 780–787). Full text: `research/sources/archive-labeling-amm-published.full.md`.

This is the **published** version of the paper that governs PE156. The full proof of the base-b bound is in the arXiv v2 companion (`research/sources/archive-labeling-arxiv-latest.full.md`, Prop 9.1); the AMM paper *states* the bound and defers the proof to the arXiv companion [4].

## What this version establishes that the run needs

- **Definition.** fd(x) = number of times digit d is written in the whole numbers 0..x (Section 2). For d ∈ {1..9} this is exactly Problem 156's f(n,d). f1(x) is OEIS A094798.
- **The "exactly" sequences Ed(d) are bounded by d·10^10** (Section 4, before Table 3): "We can be more precise in claiming that the largest value in Ed is not more than d·10^10. We prove the claim for this and other bases in our accompanying paper [4]." Proof: see `claim km-prop91-bound`/`G2-solution-bound` (arXiv Prop 9.1).
- **Actual largest solutions** (Table 3, for checking the run's own answers): d=1: 1 111 111 110; d=2: 10 535 000 000; d=3: 20 500 000 000; d=4: 30 500 000 000; d=5: 40 000 000 000; d=6: 59 628 399 995; d=7: 69 971 736 170; d=8: 79 998 399 997; d=9: 80 000 000 000.
- **Number of terms per digit** (Table 2, A-numbers): d=1: A014778 (83 terms, positive; 84 counting 0); d=2: A101639 (13); d=3: A101640 (35); d=4: A101641 (47); d=5: A130427 (4); d=6: A130428 (71); d=7: A130429 (48); d=8: A130430 (343); d=9: A130431 (8). A130432 = counts including n=0 = [84,14,36,48,5,72,49,344,9].
- **The digit-count closed form** (Section 7, eq. (1)): count digit d per decimal place k from the right; with Y = floor(x/10^k)·10^(k−1):
  - d>0, x_k<d: contribution Y
  - d>0, x_k=d: Y + (x mod 10^(k−1)) + 1
  - d>0, x_k>d: Y + 10^(k−1)
  d=0 needs separate leading-zero adjustment (not needed for PE156).
- **Skip lemma for search** (Section 7, Lemma 9 = arXiv Lemma 7.1): if a≥(d) > x and fd(y) < x for some y > x, then a≥(d) > y. Used with an unbounded binary search over "safeleft" ranges.
- **Zero case** (Section 5): a=(0) is not well-defined (no n with f0(n)=n); Theorem 8 + proof.
- **Periodicity** (Section 4): solutions repeat modulo 10^10 in each range [r·10^10, (r+1)·10^10) for r < d, which is why A130432(d) is divisible by d.

## Implications for PE156

- The run needs Σ s(d) for d=1..9, where s(d) = Σ of all n with f(n,d)=n. This paper's Table 2 says the total solution count is 84+14+36+48+5+72+49+344+9 = 661 (including 0). The bound n ≤ d·10^10 makes the search finite; the closed form (Section 7) makes each f(n,d) evaluation O(digits); the skip lemma makes the search fast.

## Caveat / do-not-use

- A216398 is the per-digit sum s(d) sequence — the published **answer** to this contest problem. Do not download or read it; the run must derive s(d).