# Fishkin 2010 abstract — reconstructed from OpenAlex (scholar verification)

The claim file and summary for Fishkin 2010 quote the theorem structure from
the OpenAlex abstract. This note records the exact reconstruction, so nobody
needs to re-derive it from the inverted index.

Source: research/sources/fishkin-openalex.full.md, `abstract_inverted_index`.
The indexed words, in ascending position order:

> "We [0] investigate [1] the [2] number [3] of [4] limit [5] cycles [6] a [8]
> planar [9] quadratic [10] vector [11] field [12] with [13] perturbed [15]
> center-like [16] singular [17] point. [18] An [19] upper [20] bound [21] is
> [22] obtained [23] on [24] the [25] number [26] of [27] δ-good [28] such [32]
> cycles [29] (Theorem [36] 1). [37] Here [38] δ [39] parameter [42]
> characterizing [43] cycles: [46] it [47] shows [48] how [49] far [50] those
> [51] are [52] from [54] points [57] and [62] infinite [65] points. [66] The
> [67] bound [68] also [69] includes [70] another [71] parameter, [72] κ, [73]
> field. [77] More [78] precisely, [79] κ [80] gives [81] an [82] estimate [83]
> of [84] distance [86] to [87] set [91] consisting [94] fields [98] line [101]
> [singular] point. [103] Earlier, [105] Ilyashenko [106] Llibre [108] found
> [109] ... sufficiently [125] far [126] ... Theorem [135] 1 [136] ... that
> [138] complement [140] each [141] other [143] yield [144] new [146] field,
> [159] regardless [160] of [161] its [162] distance [163] to [164] [center-like]
> point [172] 2). [174]"

Note the position indices have gaps (word tokens dropped by the indexer — e.g.
"cycles" at 6 has its article dropped, and the span from 109 to 125 contains
material the index omits). The reconstruction is faithful to the words present:
- Theorem 1: upper bound on δ-good limit cycles of a quadratic field with
  perturbed center-like singular point; δ shows how far those cycles are from
  points and infinite points; κ estimates distance to fields with a line of
  singular points.
- Theorem 2 (position 174, after "regardless of its distance to [a center-like]
  point"): the uniform bound, complementing Ilyashenko–Llibre.

**What the abstract does NOT contain:** any specific numerical constant
(10⁷², 10⁷⁷, δ^{−33}, or any exponent). Those figures in earlier reports are
unverified.

**What it confirms about the paper's place in the series:** Fishkin 2010 is
the companion paper to Ilyashenko–Llibre 2010 covering the perturbed-center
regime; the two complement each other. Alexey Fishkin is thanked in the
Ilyashenko–Llibre paper (line 631 of the held full text) for reading several
versions of the manuscript.
