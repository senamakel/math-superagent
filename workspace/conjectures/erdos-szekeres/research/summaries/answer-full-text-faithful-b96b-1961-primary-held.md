# Request `full-text-faithful-b96b` — answered by held 1961 primary

**answers: full-text-faithful-b96b**

The request asked for the full text or a faithful reproduction of Erdős–Szekeres
1960/'61 "On some extremum problems in elementary geometry" — the canonical lower-bound
construction of 2^{n-2} points with no convex n-gon. That is already in the library:

- **Held full text:** `research/sources/erdos-szekeres-1961-on-some-extremum-problems-elementary-geometry-renyi.pdf.full.md`
  (473 lines), source URL https://renyi.hu/~p_erdos/1960-09.pdf (in the leading
  comment). This is the Rényi Institute's hosted scan of the primary.
- **What it establishes** (read directly from the held text):
  - Line ~23: "we shall construct a set of 2^{n−2} points which contains no convex
    n-gon. Thus 2^{n−2} ≤ f₀(n) < ..." — the lower bound is explicitly the paper's
    construction.
  - Lines ~154–200: the full construction. Let (the formula for the number of points
    in S_k, k = 1..n−1) with S_{k+1} built from S_k by a translation/offset scheme;
    S = ∪_k S_k has Σ_k C(n−2,k−1) = 2^{n−2} points, and the slope argument shows
    "every convex polygon in S has less than n sides": any line connecting S_i and
    S_ℓ (1 ≤ i < ℓ ≤ n−1) has slope strictly between the bounds that prevent a
    convex n-gon from forming across blocks.
  - This is exactly the primary treatment the request wanted: the construction,
    the size identity, and the emptiness argument are all in the held scan.
- **Bearing this closes:** the run's lower-bound arm (build the 2^{n-2}-point
  construction at n=5,6,7 with exact coordinates) can work from this primary plus
  the already-verified `es_construct` realization on disk; the "we lack the original
  construction details" worry is resolved — the details are held and read.
- **Status:** request answered from held material. The 1961 journal pagination
  (Ann. Univ. Sci. Budapest. Eötvös Sect. Math. 3-4 (1961) 53–62) is the canonical
  citation; the Rényi PDF is the same paper.