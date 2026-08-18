# Librarian cycle — 2026-08-19/20: Glen–Justin survey + frontier resolution; lexicographic-order axis strengthened

## What this cycle did

1. **Verified library state against the requests ledger.** All five recorded
   `citable-*` requests carry `answers:` closures in claim notes on disk
   (requests-closed-recap.md); the rendered REQUESTS.md lag is cosmetic.

2. **Worked the top of the frontier.** Resolved previously anonymous OpenAlex
   rows to their primary papers and checked each against disk:
   - `W1586417893` = **Lothaire, *Algebraic Combinatorics on Words*** (Encyclopedia
     vol. 90) — held: Cambridge landing page (`lothaire-algebraic-combinatorics-words.full.md`)
     + full Sturmian chapter (`lothaire-sturmian-words-C2.full.md`).
   - `W1606152431` = **Wen–Wen, "Some properties of the singular words of the
     Fibonacci word"** (1994) — held (`wen-wen-singular-words-fibonacci-word-1994.full.md`).
   - `W2317201179` = **Morse–Hedlund, "Symbolic Dynamics II: Sturmian Trajectories"**
     (1940) — abstract held (`morse-hedlund-symbolic-dynamics-1938-ams-abstract.full.md`).
   - `W1853820275` = Berstel, "On the Index of Sturmian Words" (1999) — covered by
     held surveys (Cassaigne 2008, de Luca 1997, Glen thesis).
   - `W2006431506` = **Coven–Hedlund, "Sequences with minimal block growth II"**
     (1974) — the minimal-complexity/Sturmian-trajectories primary; complexity
     p(n)=n+1 anchored in-library by Lothaire C2, Perrin–Restivo, Wikipedia.
   - `W2090444071` = **Ostrowski 1922** — recorded paywalled, covered by
     Brown–Shiue/Pinner/Hieronymi–Terry.
   - `W1992715478` = de Luca–de Luca, "Palindromic prefixes and episturmian words"
     (2005) — covered by held surveys.
   - `W2035407289` = **Droubay–Pirillo, "Palindromes and Sturmian words"** (1999,
     120 cites) — paywalled; the key statement (Sturmian iff palindrome complexity
     h(n) = 1 + (n mod 2)) is carried in the newly downloaded Glen–Justin survey
     §6.2 and by Berstel 2007 survey held on disk.
   - `W2043646600` = **Mantaci–Restivo–Sciortino, "Burrows–Wheeler transform and
     Sturmian words"** (IPL 2003, 128 cites) — paywalled primary; its content
     (BWT of a standard Sturmian word; conjugates lexicographically ordered) is
     covered by the held Berstel 2007 survey §7 (read lines 910–1000) and by the
     held Dagstuhl Fici–Mantaci–Restivo–Romana–Rosone–Sciortino BWT survey
     (`fici-mantaci-restivo-romana-rosone-sciortino-bwt-combinatorics-words-dagstuhl.full.md`).

3. **Downloaded the missing standard survey.** **Glen & Justin, "Episturmian
   words: a survey"**, RAIRO-ITA 43 (2009) 403–442, arXiv:0801.1655 — the
   canonical modern survey of the Sturmian/episturmian theory axis:
   - `research/sources/glen-justin-episturmian-words-survey-2009-ar5iv.full.md`
     (152,849 bytes full text via ar5iv; URL recorded in-file).
   - Digest at `research/summaries/glen-justin-episturmian-words-survey-2009-ar5iv.md`.
   - The abstract-page-only first attempt (arxiv.org/abs/0801.1655) was replaced
     by the ar5iv full text; both filed, the full text is the usable one.

4. **Read the most relevant part for PE1006** — §7 "Balance & lexicographic
   order" (lines 733–930): lexicographic order on words; min(w|k)/max(w|k);
   Pirillo's Sturmian inequalities `as ≤ min(s) ≤ max(s) ≤ bs` (char. standard
   Sturmian, dating to Veerman mid-80s); Glen–Justin–Pirillo finite-word
   characterization (Theorem 7.5, Cor 7.7: finite word not Sturmian iff aua
   prefix of min(w) and bub prefix of max(w)); Lyndon/standard correspondence
   (Theorem 7.9: infinite Lyndon words in a standard subshift = a·s). **Why it
   matters here:** for equal-length binary strings the decimal value `val(x)` is
   exactly the lexicographic order on the factor set, so the Sturmian
   lexicographic structure is the ordering that Ψ(k)'s sum of squares lives in.
   The survey also fixes the vocabulary (min/max words, spins, directive words,
   episkew) for any future order-based attack on G4.

## Still not obtained (recorded, covered in-library)

- Chuan–Ho "Locating factors of the infinite Fibonacci word" (TCS 349, 2005) and
  "Factors of characteristic words: Location and decompositions" (TCS 411, 2010):
  paywalled; no open full text found. Content overlaps held Sivasankar–Rama Thm 7
  and Huang–Wen gap sequence; Zeckendorf-location formulas also reflected in
  Hieronymi–Terry and Shallit–Shan (held).
- Chuan "Moments of conjugacy classes of binary words" (TCS 310, 2004): paywalled;
  the Fibonacci Quarterly 2003 companion (same author, same moment framework) IS
  held (`chuan-moments-conjugacy-classes-fq2003.full.md`).
- Chuan "α-Words and factors of characteristic sequences" (Discrete Math. 177,
  1997): paywalled; covered by held FQ 2003 moments paper and Berstel 2007.
- Jenkinson–Zamboni "Characterisations of balanced words via orderings" (TCS 310,
  2004): paywalled; its order-characterization content is reflected in Glen–Justin
  §7 just downloaded.
- Droubay–Pirillo "Palindromes and Sturmian words" (TCS 223, 1999): paywalled;
  the h(n) = 1 + (n mod 2) characterization is stated in held sources
  (Berstel 2007, Glen–Justin §6.2).
- Mantaci–Restivo–Sciortino BWT-Sturmian (IPL 2003): paywalled; BWT-Sturmian
  content covered by held Berstel 2007 §7 and the held Dagstuhl BWT survey.

## Where the run stands

- Library: saturated on Sturmian complexity, factor structure, position theorems,
  singular/standard words, three-gap/floor-sum, universal-Euclidean moments, and
  now the lexicographic-order axis (Glen–Justin §7).
- The live gap G4 (fixed-dimensional O(log k) aggregation over k+1 intercepts)
  remains construction work, not a source gap: no published theorem states the
  joint second-moment collapse; the new survey's lexicographic material is
  background vocabulary for any order-based formulation, not the collapse itself.
- No further cycle work warranted: frontier worked to depth, open requests
  closed, primaries paywalled are covered by held equivalents.
