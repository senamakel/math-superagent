# Catalogue of all known binomial collisions, and the ineffectivity source

Anchored to MRSTT (arXiv:2106.03335, full text `research/sources/mrstt-fulltext.full.md`),
which collects the state of the art as of 2021. This is the strongest single
statement of "what a uniform bound must be consistent with".

## All known non-trivial collisions (MRSTT Remark 1.4)

We restrict to `2 <= k <= n/2, 2 <= l <= m/2, k < l` in `C(n,k) = C(m,l)`. The
only known solutions are:

1. **(16,2) = (10,3)**: `C(16,2) = C(10,3) = 120`
2. **(56,2) = (22,3)**: `C(56,2) = C(22,3) = 1540`
3. **(120,2) = (36,3)**: `C(120,2) = C(36,3) = 7140`
4. **(21,2) = (10,4)**: `C(21,2) = C(10,4) = 210`
5. **(153,2) = (19,5)**: `C(153,2) = C(19,5) = 11628`
6. **(221,2) = (17,8)**: `C(221,2) = C(17,8) = 24310`
7. **(78,2) = (15,5) = (14,6)**: the 3003 triple (3040 under row notation)
8. The infinite Fibonacci family: `C(F_{2i+2}F_{2i+3}, F_{2i}F_{2i+3}) =
   C(F_{2i+2}F_{2i+3}-1, F_{2i}F_{2i+3}+1)` for i = 1, 2, ... (Lind, Singmaster,
   Tovey). First few `(n,k)` pairs: (15,5)=(14,6) [3003], (104,39)=(103,40)
   [61218182743304701891431482520], ...

**de Weger's Conjecture**: these generate all non-trivial collisions. This would
imply `N(a) <= 8` (with `N(3003)=8` and `N(a)=6` for all other family member, via
the two interior solutions + mirrors + trivial pair). It would imply Singmaster.

VERIFIED against this run's oracle `code/out/witnesses.json` (exact integer
arithmetic, scan over `a <= 10^7`): every one-off collision above reproduces
exactly as a nontrivial pair, and 3003 reproduces as the triple
(78,2),(15,5),(14,6) with N=8. So these entries are `verified-numerically`, not
merely sourced. (The giant j=2 Fibonacci value 61218182743304701891431482520 is
> 10^7 so outside the oracle scan, but independently held in Singmaster 1975 and
A098565.)

## The ineffectivity obstruction, with its exact source

MRSTT Remark 1.5 states: the number of solutions to `C(n,m) = C(n',m')` for fixed
`2 <= m < m'` has been shown (via **Siegel's theorem on integral points**) to be
**finite**, in **[4] = Beukers, Shorey, Tijdeman**, "Irreducibility of polynomials
and arithmetic progressions with equal products of terms", in *Number theory in
progress, Vol. 1 (Zakopane-Kościelisko, 1997)*, pp. 11–26, de Gruyter, Berlin 1999.
(Also [16] Kiss treats `(x,p)=(y,2)` for odd prime p.)

The crucial sentence (verbatim): *"This implies that there are no collisions in
the regime `2 <= m <= w(n)` if `w` is a function of `n` that goes to infinity
sufficiently slowly... **Unfortunately, due to the reliance on Siegel's theorem,
the function `w` given by these arguments is completely ineffective.**"*

This is the primary-source anchor for the run's central obstruction:
**finiteness per fixed `(k1,k2)` is ineffective, so it yields no bound uniform
in the pair.** It is the same "finiteness is not a bound" trap as Faltings.

## What else Remark 1.5 establishes about the boundary

After Theorem 1.3 (interior, ≤2 per half / ≤4 total), the conjecture reduces
without loss of generality to the boundary region
`2 <= m <= exp(log^{2/3+eps} n)`, equivalently
`2 <= m <= (log t)/(log_2 t)^{3/2 - eps}`. This is precisely where
Beukers–Shorey–Tijdeman (per-pair finiteness) applies but is ineffective, and
where de Weger's conjecture predicts at most one solution for large t.

## Gap recorded

The BST paper itself ([4], 1999) is in a paywalled de Gruyter proceedings volume
and was not freely downloadable. The run holds its exact statement *as quoted by
MRSTT's full text* (fixed-pair finiteness via Siegel, ineffective), but not the
paper's own text. This is an acceptable secondary-anchor (the obstruction is
independently re-derivable from Siegel plus MRSTT's quote), but if a primary copy
becomes available (e.g. via an author page or an open archive), secure it.

Evidence class: sourced (MRSTT full text read and quoted).
