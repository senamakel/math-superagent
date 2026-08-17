# Phantom citation check: "Granville–Ramaré 1996 primitive prime divisor theorem"

**Finding (librarian, citation-integrity check).** The proposed approach
`research/approaches/zsigmondy-primitive-prime.md` rests its "primitive prime
divisor" engine on a citation that does not exist as stated:

> "Granville–Ramaré (1996, J. London Math. Soc. 54) proved that for
> n > max(k+1, 2k−3), the product n(n−1)…(n−k+1) has a prime divisor p that
> does NOT divide any product of k consecutive integers with a SMALLER starting
> value."

Checked against three independent witnesses:

1. **What Granville–Ramaré 1996 actually is:** "Explicit bounds on exponential
   sums and the scarcity of squarefree binomial coefficients", *Mathematika*
   43 (1996) 73–107. About squarefree binomial coefficients and exponential-sum
   bounds, not a primitive-prime-divisor theorem for consecutive-integer
   products. Journal (Mathematika, not JLMS) and volume (43, not 54) both wrong
   in the note's citation.
2. **Held sources contain no such theorem:** `grep Granville|Ramar` across
   `research/sources/` finds the name only in the article-list index and in
   Matveev's Kummer-condition text. The note claims the theorem is "held in the
   library (the recalled chunk from Number Theory in Progress Vol. 2)" — but
   the held NTIP source is **Vol. 1** (the de Gruyter preview), and it contains
   no Granville–Ramaré content. NTIP Vol. 2 is not on disk.
3. **[Search]** Granville–Ramaré 1996's real scope is squarefree/scarcity of
   binomial coefficients, corroborated by citing literature searches.

**Verdict.** The "Granville–Ramaré primitive prime divisor theorem for products
of consecutive integers" as stated in the approach note is a recalled citation
with no on-disk or real-world referent. The primitive-prime-divisor engine of
`zsigmondy-primitive-prime` is therefore **unsupported as written**. The
approach's separate Sylvester step is real and grounded:

- **Sylvester (1892) / Schur (1929):** a product of k consecutive integers
  each > k has a prime divisor > k.
- **Held, Laishram PhD thesis (Ch. 1)**, the actual refinements:
  - Laishram–Shorey Thm 1.2.1: for n > k, ω(Δ(n,k)) ≥ π(k) + ⌊¾π(k)⌋ − 1 + δ(k)
    with explicit exceptional pairs (list in (1.2.6));
  - Laishram–Shorey (Acta Arith 120 (2005) 199–211): P(Δ(n,k)) > 2k for
    n > max(k+13, (279/262)k) — the sharpest unconditional
    greatest-prime-divisor bound of the Sylvester–Schur type.

**What would falsify this finding:** a genuine Granville–Ramaré theorem on
primitive prime divisors of consecutive-integer products, with a citable
statement and location. Until one is produced, the approach's precedent must
cite Laishram–Shorey/Sylvester–Schur and state its primitive-prime engine only
for what is actually proved (Zsigmondy for a^n − b^n sequences; **not** for
falling-factorial blocks — Zsigmondy does not directly apply there, which is
precisely the gap the phantom citation was filling).