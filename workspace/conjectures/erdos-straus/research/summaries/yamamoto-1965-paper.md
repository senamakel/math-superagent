# Yamamoto, "On the Diophantine Equation 4/n = 1/x + 1/y + 1/z" (1965) — bibliographic record

Source: https://www.jstage.jst.go.jp/article/kyushumfs/19/1/19_1_37/_article/-char/en (J-STAGE, open access)
Bibliographic record: Mem. Fac. Sci. Kyushu Univ. Ser. A 19(1) (1965) 37–47. DOI: 10.2206/kyushumfs.19.37. Received 1964-12-20, available on J-STAGE since 2008-12-05. Author: Koichi Yamamoto.

## Status: citation fixed, text unobtained

The landing page (this download) is a bibliographic record only. The full-text PDF (`/_pdf/-char/en`) is a **scanned PDF with no text layer** — the downloader refused it. So the library now holds the *canonical citation* for Yamamoto 1965 but not the article's content.

**What is known about the content from the library's other sources (secondary, sourced):**
- Elsholtz–Tao and Salez both cite Yamamoto 1965 as the origin of the **Type I / Type II solution classification** for 4/p: Type I = n divides exactly one of x,y,z; Type II = n divides exactly two. (Elsholtz–Tao §1: "for odd prime p, every solution is Type I or Type II, and f(p) = 3 f_I(p) + 3 f_II(p)".)
- The Elsholtz–Tao verification-history table credits Yamamoto with the numerical bound **10^7 (1964)**.
- Wikipedia's "Nonexistence of identities" section's square-obstruction (no polynomial identity when r is a quadratic residue mod p) is attributed to Mordell's book, which in turn reports Rosati/Yamamoto parametrisations (per the Salez footnote recorded in `research/notes/mordell-book.md`).

## Implication

The run does **not** need Yamamoto's original text: the Type I/II definitions and the 10^7 bound are already stated with primary citations in the two Elsholtz–Tao copies on disk. What the run does need — the *exact* statement of why no standard identity covers the squares — is in Elsholtz–Tao Prop 1.6 (to be extracted) and in Eppstein's modular conditions (now summarized). Do not re-attempt the Yamamoto PDF; record the citation fixed.

```claim
id: yamamoto-1965-type12-origin
statement: Yamamoto 1965 (Mem. Fac. Sci. Kyushu Univ. Ser. A 19, 37–47) is the origin of the Type I / Type II classification of solutions of 4/p and of the numerical verification to 10^7; the article is open-access on J-STAGE (DOI 10.2206/kyushumfs.19.37) but its PDF is a no-text-layer scan, so the library holds the citation, not the text.
hypotheses: historical attribution; the classification and 10^7 bound are asserted by Elsholtz–Tao (primary for the statement) and cross-confirmed by Salez and Wikipedia.
holds-here: true — the run's type I/II vocabulary comes from here.
status: asserted-by-source (Elsholtz–Tao §1 and Table 1); citation fixed from J-STAGE.
bearing: fixes the standard Type I/II terminology the entire literature (this library included) uses; nothing about the run's construction depends on reading Yamamoto's own proofs, since Elsholtz–Tao restates the classification.
anchor: research/sources/yamamoto-1965-paper.full.md
```