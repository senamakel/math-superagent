# Claim G2 — finite search bound for f(n,d)=n

Fills request `identify-sticker-numbers-eeda`: the "sticker numbers / exactly
numbers" paper is **Khovanova & Marton, "Archive Labeling Sequences"**,
arXiv:2305.10357v2 [math.HO] (16 Feb 2024), published in *Amer. Math. Monthly*
132(8) (2025) 780–787, DOI 10.1080/00029890.2025.2525050. A CC-BY copy of the
published version is held at MIT DSpace (hdl.handle.net/1721.1/163207).

```claim
id: G2-solution-bound
statement: >
  For any base b > 1 and digit d > 0 with b > d, every x such that
  fd(x,b) = x satisfies x ≤ d·b^b, where fd(x,b) counts the occurrences of the
  digit d in the base-b writings of the numbers 1..x.  For base b = 10 and
  d in {1,...,9}: every n ≥ 0 with f(n,d) = n satisfies n ≤ d·10^10, where
  f(n,d) is the problem's count of digit d in the decimal writings of 0..n.
hypotheses: >
  (i) d > 0 and b > d (here b = 10, d in {1..9}: both hold).
  (ii) The paper counts occurrences in 1..x, the problem in 0..n.  These agree
  for every d > 0 because 0 has no nonzero decimal digits; hence the bound
  transfers verbatim to f(n,d).  (The paper's sequence Ed is defined on
  positive integers; our solution set additionally contains 0, which is below
  the bound and does not affect it.)
  (iii) The bound is finite because fd(x) grows superlinearly in x: in
  numbers below 10^k there are k·10^(k-1) occurrences of each nonzero digit,
  so fd(x) ≥ (1/10)·(#digits of 1..x), which exceeds x beyond some point.
holds-here: yes
status: proved (source: Proposition 9.1, with proof; the base-10 bound is also
  stated in the published AMM paper, Section 4, "[the largest value in Ed] is
  not more than d·10^10", with Table 3 listing the actual maxima).
bearing: >
  Discharges gap G2 of research/backward/fixed-point-enumeration.md: the
  solution set S_d = {n : f(n,d)=n} lies inside [0, d·10^10], so a search that
  never passes d·10^10 and evaluates f exactly is provably complete without
  enumerating numbers up to the answer.  This is the finite bound that makes
  the PE156 solver exact.
answers: identify-sticker-numbers-eeda
anchor: >
  https://arxiv.org/html/2305.10357 (v2, Section 9, Proposition 9.1, with
  proof); published version https://dspace.mit.edu/bitstream/handle/1721.1/163207/UAMM_A_2525050_O.pdf
  (Section 4 bound statement, Table 3); DOI 10.1080/00029890.2025.2525050.
```