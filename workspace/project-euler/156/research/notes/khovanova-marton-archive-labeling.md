# Khovanova & Marton, "Archive Labeling Sequences"

Primary source on disk: `research/sources/archive-labeling-arxiv-latest.full.md` (arXiv:2305.10357v2 [math.HO], 16 Feb 2024), `research/sources/archive-labeling-arxiv-v1.full.md` (v1, 25 Apr 2023), `research/sources/archive-labeling-amm-published.full.md` (published version, Amer. Math. Monthly 132(8) (2025) 780-787, DOI 10.1080/00029890.2025.2525050, source URL https://dspace.mit.edu/bitstream/handle/1721.1/163207/UAMM_A_2525050_O.pdf). Also a MathWorld news report (Oct 13 2004) of the underlying Google Labs Aptitude Test item: `research/sources/mathworld-google-aptitude.full.md`.

## What the paper establishes that this run needs

The problem PE156 is the base-10 single-digit instance of the "sticker/archive labeling" family that this paper studies. `f_d(x)` below is exactly Problem 156's `f(n,d)` for d=1..9 (it counts digit occurrences in the decimal spellings of 1..x; Problem 156 counts 0..n, and 0 contributes nothing to any d≠0, so the two agree).

### Closed form for the counting function (§7)

Count each decimal place k from the right separately. With x_k the k-th digit of x from the right and Y = floor(x/10^k)·10^(k-1):

- d>0, x_k < d: contribution Y
- d>0, x_k = d: Y + (x mod 10^(k-1)) + 1
- d>0, x_k > d: Y + 10^(k-1)

and f_d(x) = Σ_k c_d(x_k). This is the classical place-value identity: occurrences of digit d in [1,x] are computed per position in O(log₁₀ x) time.

### Finite search bound (Proposition 9.1)

For any digit d>0 in base b>d, the maximum possible value of a=(d,b) is b^b and all x with f_d(x,b)=x satisfy x ≤ d·b^b. In base 10: every solution of f(n,d)=n for d=1..9 satisfies n ≤ d·10^10.

Sketch: f_b(b^b) = b^b (so a solution exists at b^b); f_d(d·b^b) = d·b^b + 1, and every x in [d·b^b, (d+1)·b^b] has leading digit d so there are no solutions in that interval; then f_d((d+1)b^b) = (d+2)b^b and a base-b version of Lemma 5.1 pushes the count permanently ahead, so no solution can appear later. This is the provable bound that turns "find all fixed points of f(n,d)=n" into a finite search to d·10^10, without enumerating the whole range.

### Range-skipping search lemma (§7, Lemma 7.1)

If a≥(d) > x and f_d(y) < x for some y > x, then a≥(d) > y. Proof: f_d non-decreasing, so f_d(t) ≤ f_d(y) < x < t... wait, x < t ≤ y gives f_d(t) ≤ f_d(y) < x < t, so no equality in [x,y]. This lets the search jump over intervals where the function stays below the index. Used with an unbounded binary search (§7).

### Complement: bounds and counts

- A165617: number of solutions of f_1(x,b)=x; base 10 count is 83 (excluding n=0; A014778 includes it, so 84 with zero).
- A226238: largest x with f_1(x,10)=x, the concatenation of nine 1s then a 0 = 1,111,111,110 (which is exactly d·10^10 for d=1... no: 1,111,111,110 < 10^10? No — 1,111,111,110 is less than 10^10? 10^10 = 10,000,000,000, so 1,111,111,110 < 10^10? No: 10^10 = 10,000,000,000 and 1,111,111,110 has 10 digits starting with 1, so it is about 1.11×10^9, less than 10^10. Wait — 1,111,111,110 is ten digits (1,111,111,110 ≈ 1.11×10^9), while 10^10 = 10,000,000,000 is eleven digits. So 1,111,111,110 < 10^10? 1,111,111,110 < 10,000,000,000, yes. Hmm, but the bound is x ≤ d·10^10; for d=1 that is ≤ 10^10, and 1,111,111,110 < 10^10, so consistent. The record for d=1 is 1,111,111,110.)

Also: E_d (exact sequences) are periodic modulo 10^10 within ranges [r·10^10, (r+1)·10^10) for r < d (same number of solutions in each), which is why A130432(d) is divisible by d.

## OEIS sequence references established by the run

- A014778 (d=1 fixed points, 84 terms incl. 0; b-file on disk), A101639 (d=2, 13), A101640 (d=3, 35), A101641 (d=4, 47), A130427 (d=5, 4), A130428 (d=6, 71), A130429 (d=7, 48), A130430 (d=8, 343), A130431 (d=9, 8).
- A130432 = [84, 14, 36, 48, 5, 72, 49, 344, 9] = per-digit solution counts including n=0.
- A094798 = f(n,1) itself; partial sums of A268643; generating function g(x) = x/((1-x)(1-x^10)) + ((1-x^10)/(1-x))^2 g(x^10).
- A216398 is the per-digit sum s(d) sequence — **do not use** (that is the published answer to this contest problem; the run must derive it).

## Alternative analytic form (math.SE, crasic)

On disk: `research/sources/digit-count-analytical-math-se-archive.full.md` (via Wayback Machine of https://math.stackexchange.com/questions/47477). It gives f(d,n) = Σ_j (Σ_{i=0}^{r_j} (10^j δ_{i-1,d}) + r_j E(j) + δ_{r_j,d}(n[j:]+1)) with E(j)=j·10^(j-1) and n[j:] the number formed by the last j digits. This is an independent restatement of the same place-value identity, useful as a cross-check implementation.

```claim
id: km-prop91-bound
statement: For any digit d>0 in base b>d, every x with f_d(x,b)=x satisfies x ≤ d·b^b; in particular in base 10 all solutions of f(n,d)=n for d=1..9 have n ≤ d·10^10.
hypotheses: f_d(x,b) counts occurrences of digit d in the base-b spellings of 1..x; b>d; d≠0.
holds-here: holds. Problem 156's f(n,d) counts 0..n, and 0 contributes no occurrences of any d∈{1..9}, so f(n,d) = f_d(n,10). Bound n ≤ d·10^10 applies.
status: sourced (Khovanova & Marton, arXiv:2305.10357v2 Prop 9.1, on disk)
answers: identify-sticker-numbers-eeda
bearing: finite search bound; makes finding all fixed points a provably finite computation to d·10^10 with no enumeration of the interval.
anchor: research/sources/archive-labeling-arxiv-latest.full.md
```

```claim
id: place-value-closed-form
statement: For d>0, f_d(x) = Σ_k c_d(x_k) where c_d(x_k) = floor(x/10^k)·10^(k-1) if x_k<d; floor(x/10^k)·10^(k-1) + (x mod 10^(k-1)) + 1 if x_k=d; floor(x/10^k)·10^(k-1) + 10^(k-1) if x_k>d.
hypotheses: decimal representation, d > 0, x ≥ 0 (k summed over digit positions of x).
holds-here: holds. This is the standard place-value digit-count identity, usable directly as the O(log x) evaluation of f(n,d).
status: sourced (Khovanova & Marton §7; also GeeksforGeeks place-value article and LearnYard, on disk)
bearing: replaces per-n enumeration with O(#digits) evaluation per candidate; the core of solution.py.
anchor: research/sources/archive-labeling-arxiv-latest.full.md
```

```claim
id: km-lemma71-skip
statement: If a≥(d) > x and f_d(y) < x for some y > x, then a≥(d) > y. (f_d non-decreasing, so the whole interval [x,y] stays below the index.)
hypotheses: f_d non-decreasing (true for digit-count functions).
holds-here: holds for f(n,d), which is non-decreasing in n.
status: sourced (Khovanova & Marton Lemma 7.1)
bearing: lets the fixed-point search skip intervals; with the d·b^b bound it gives a complete, fast algorithm.
anchor: research/sources/archive-labeling-arxiv-latest.full.md
```