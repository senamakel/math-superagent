# Pierrat, Thiriet & Zimmermann, "Magic squares of squares" (LORIA, 2015) — [[zimmermann-loria-magic-squares-of-squares-2015.full]]

Three authors at INRIA/LORIA. Restates history (Euler 4×4, Gardner's $100, LS1 near-miss, Buell's centre > 25×10²⁴ bound) and proves modular restrictions plus an extension of the "magic hourglass" family.

## Modular properties (Lemma 1, proved)
For any **primitive** 3×3 magic square of squares:
- the magic sum s ≡ 3 (mod 72);
- all (square) entries ≡ 1 (mod 24).

Proof: exhaustive analysis mod 4, 8, 9 — only the all-1-mod-8 solution survives for a primitive square (others are divisible by 4, non-primitive), and mod 9 gives s ≡ 3 mod 9 with entries 1,4,7 mod 9 (≡1 mod 3). CRT gives s ≡ 3 mod 72 and entries ≡ 1 mod 24. **Remark:** mod 7 and mod 11 force s not divisible by 7 or 11. **Remark:** the identical constraints hold for all seven-square configurations 7.I–7.VIII (relaxing two entries to non-squares does not change the mod-24 constraint).

## AP-of-squares classification (Theorem 1)
All non-trivial APs x², A², y² with A odd are given, uniquely, by: choose a square-free divisor p of A with p ≡ 1 mod 4, write A = pA′ with A′ = m²+n² (m even, n odd), then b = 4mn(m²−n²), x = √(A²−p²b), y = √(A²+p²b); the endpoints are x = p(m²−2mn−n²), y = p(m²+2mn−n²).
- Lemma 2: an odd prime q | (m²+n²) not dividing m does not divide m²−2mn−n².
- Lemma 3: if A ≡ 3 mod 4 there exists g>1 dividing every p in a decomposition A = p(m²+n²).

## Magic-hourglass / seven-square extensions (constructed over Q, not just mod)
Rejects Buell's assumption that the three entries of each of the two diagonals and the central column are pairwise coprime (this need not hold). Constructs explicit **primitive** hourglass configurations with all 5 relevant sums equal **modulo 2^47** — e.g. central A = 1289865125 (10 digits) with (m,n,p)=(13320,8975,5),(7666,35087,1),(19526,30143,1) — well below Buell's 5×10¹² bound, which only held under the dropped coprimality assumption. Also examples mod 2^59 (A=1081235918365, mod 2^57). Searches: only solution mod 2^57 up to A=5×10¹²; none for 7.II up to A=6.5×10⁹, 7.III up to 1.69×10¹⁰, 7.V up to 1.6×10¹⁰; for 7.VI one solution mod 2^59 found up to A=6.15×10¹¹.

**Bearing:** the modular constraints (s ≡ 3 mod 72, entries ≡ 1 mod 24) are exact, source-backed, and survive against the known 7-square witnesses (Bremner's entries are all ≡1 mod 24). The hourglass work is *not* about the full MSS — it shows the "hourglass" 7-square configuration has solutions modulo high powers of 2, so a mod-2^k sieve cannot eliminate the hourglass, consistent with the general "locally solvable mod every prime power" obstruction.

```claim
id: zimmermann-modular
statement: A primitive 3×3 magic square of squares has magic sum s ≡ 3 (mod 72) and all nine
  (square) entries ≡ 1 (mod 24); s is not divisible by 7 or 11. The same mod-24 entry
  constraint holds for every seven-square configuration 7.I–7.VIII.
hypotheses: primitive (gcd of entries = 1); nine distinct squares
holds-here: yes
status: proved (in-source; mod 4/8/9 exhaustive analysis)
bearing: a clean exact sieve constraint every candidate must satisfy; consistent with the
  7-square witnesses
anchor: research/sources/zimmermann-loria-magic-squares-of-squares-2015.full.md
```

```claim
id: hourglass-local-solvable
statement: The magic-hourglass seven-square configuration admits primitive solutions with all
  five targeted sums equal modulo 2^47 (central element A ~ 1.3×10⁹) and modulo 2^59, below
  Buell's 5×10¹² bound that assumed pairwise-coprime entries.
hypotheses: magic hourglass (not the full 9-square MSS); sums equal mod 2^k only
holds-here: yes (about a different configuration, not the full MSS)
status: asserted (constructed explicitly in-source)
bearing: warns that a pure power-of-2 sieve cannot eliminate the hourglass sub-configuration;
  the full MSS obstruction is not captured by local 2-adic conditions
anchor: research/sources/zimmermann-loria-magic-squares-of-squares-2015.full.md
```
