# An Explicit Solution to the Chessboard Pebbling Problem — abstract/digest (arXiv:1009.5731)

<!-- source: https://arxiv.org/abs/1009.5731 -->

Full content is summarised in research/L2.0/pebbling_knessl_pdf.md (the PDF
text), which this abstract page anchors. This paper by Qiang Zhen and Charles
Knessl (Math.CO, 12 pp) gives *exact* contour-integral expressions for the
number of reachable chessboard-pebbling configurations G(k) and the two-
parameter sequence G(k,m), then derives asymptotics in several regimes. It
builds directly on CGMO (AMM 102 (1995)) and Knessl (Math. Comput. Modelling
47 (2008)), and its G(k,m) recurrence is the one OEIS A007902 encodes.

Key facts (details in the PDF note):
- Exact: Theorem 2.1 (contour formula), Corollary 2.1 (G(k)).
- Recurrence: eqs (2.1)-(2.3); G(k)=G(k,0).
- Asymptotics: G(k) ~ c*·a^k, a = 1/z_* ≈ 2.321642199494…, c* ≈ 0.12268707…;
  z_* ≈ 0.430729593137930 is the unique root |z_*|<1/2 of S(z)=0.
- This is the 2D amoeba/A007902 count; the 3D generalisation is Eriksson's
  folded-polyominoid theory (see research/L2.0/pebbling_ejc_survey.md).

URL: https://arxiv.org/abs/1009.5731 ; PDF: https://arxiv.org/pdf/1009.5731
DOI: https://doi.org/10.48550/arXiv.1009.5731
