# Sourced claims — PE1006 governing theory (corrected)

Each claim below is backed by a source in `research/sources/` (full text, with its
URL in the first line). A claim's `anchor` names that source. Status `sourced`
means a standard theorem found in the library; `checked` means verified in-container
against the brute oracle (see `code/out/`).

**Correction recorded (contradicts steering directive 2's literal slope):** the
problem's word is the characteristic Sturmian word of slope α = 1/φ² = (3−√5)/2
≈ 0.381966 (Perrin–Restivo Example 2: "The Fibonacci word is the characteristic
word of slope α = 2/(3+√5)"), which equals (3−√5)/2. Directive 2 says to take
"slope a = F(n-1)/F(n)"; under any Fibonacci convention the ratio of
*consecutive* Fibonacci numbers tends to 1/φ ≈ 0.618, which is the ones-density
of the *complement* word (zeros ↔ ones). With exact rational arithmetic at k=3,
slope 55/89 ≈ 0.618 generates the factor set {010, 011, 101, 110} ≠ the
problem's {001, 010, 100, 101}; slope 34/89 ≈ 0.382 = F(n-2)/F(n) generates
exactly {001, 010, 100, 101}. The correction: use F(n-2)/F(n) (consecutive
Fibonacci numbers two apart), i.e. α = 1/φ². See
`research/summaries/perrin-restivo-note-sturmian-words.md` and
`code/out/check_slope.py` (verification script for tool_builder).

---

```claim
id: governing-sturmian
statement: The infinite Fibonacci word S = 0100101001001... (the limit of the
problem's S_n = S_{n-1} S_{n-2}, S_0=0, S_1=01) is the characteristic word
c_α of slope α = 2/(3+sqrt(5)) = (3-sqrt(5))/2 = 1/phi^2, phi = (1+sqrt(5))/2.
Its digit at position n >= 0 is c_α(n) = floor((n+2)α) - floor((n+1)α), i.e. it
is the lower mechanical word s_{α,0} = 0·c_α shifted by one letter
(s_{α,0}(n) = floor((n+1)α) - floor(nα)). Equivalently (Wikipedia convention)
digit n >= 1 is 2 + floor(n·phi) - floor((n+1)·phi).
hypotheses: S is the limit of the substitution 0 -> 01, 1 -> 0 applied to 0;
slope α = 1/phi^2 is irrational.
holds-here: yes — this is exactly the word whose length-k substrings the problem
calls Fibonacci subwords (verified: the problem's S_4 = 01001010 is the length-8
prefix; factor set at k=3 matches the problem oracle).
status: sourced
anchor: research/sources/perrin-restivo-note-sturmian-words.full.md (Example 2,
"The Fibonacci word is the characteristic word of slope α = 2/(3+sqrt(5))");
research/sources/perrin-sturmian-words-lecture2-mechanical.full.md;
research/sources/wikipedia-fibonacci-word.full.md
bearing: Fixes the object under study as the characteristic Sturmian word of
slope 1/phi^2, opening the mechanical-word and factor-complexity theorems.
answers: citable-statement-theorem-039a
```

```claim
id: governing-factor-complexity
statement: A Sturmian word has exactly k+1 distinct factors (contiguous
substrings) of length k for every k >= 1 (Morse–Hedlund minimal complexity;
Perrin–Restivo Theorem 1: s is Sturmian iff mechanical of irrational slope, and
the definition: exactly n+1 factors of length n). Hence the infinite Fibonacci
word has exactly k+1 distinct length-k substrings — precisely the problem's
"interestingly, for each positive integer k, there are only k+1 different
Fibonacci subwords of length k".
hypotheses: binary word, Sturmian (irrational mechanical / balanced and
aperiodic).
holds-here: yes — the problem asserts the k+1 count; the theorem is the
standard explanation and the brute oracle confirms count = k+1 for k=1..20.
status: sourced (confirmable in-container via code/out/PE1006-verification.md)
anchor: research/sources/perrin-restivo-note-sturmian-words.full.md (Theorem 1,
definition in Section 2); research/sources/perrin-sturmian-words-lecture2-mechanical.full.md
(Morse–Hedlund 1940 equivalence); research/sources/fibonacci-word-2d-factor-complexity-ar5iv.full.md
(Proposition 4)
bearing: Confirms the object set: exactly k+1 distinct subwords per length,
so Psi(k) is a sum of squares over k+1 decimals.
answers: citable-statement-theorem-039a
```

```claim
id: mechanical-word-digit-rule
statement: Let α in (0,1) and s_{α,ρ}(n) = floor((n+1)α + ρ) - floor(nα + ρ),
n >= 0 (lower mechanical word with slope α, intercept ρ). All mechanical words
of one slope have the same factor set (Perrin Lecture 2, Proposition). The k+1
distinct length-k factors of the Fibonacci word (slope α = 1/phi^2) are exactly
the k+1 words (s_{α,ρ_j}(0), ..., s_{α,ρ_j}(k-1)) where ρ_j runs over the
midpoints of the k+1 arcs of the circle R/Z cut at the k+1 points
{m·(-α) mod 1 : m = 0..k}. In exact integer arithmetic α may be replaced by
the rational F(n-2)/F(n) (A000045 convention), provided the denominator F(n) is
large enough that the k+1 cut points are distinct and in the same cyclic order
(k < F(n) is necessary; the exact threshold is the run's k=1..150 vs brute gate).
hypotheses: α irrational (or rational approximant with denominator > k);
arc-midpoint intercepts distinct (true for irrational α; needs denominator > k
for the rational approximant).
holds-here: yes with the corrected slope F(n-2)/F(n) -> 1/phi^2; the literal
steer-directive slope F(n-1)/F(n) -> 1/phi fails (see contradiction block
below). Verified in-container at k=1..100 (exact rational arithmetic).
status: sourced (construction from Perrin Lecture 2 interval correspondence
I_w and same-slope-same-factors proposition); VERIFIED in-container with exact
rational arithmetic: the construction with slope F(n-2)/F(n) reproduces the
brute factor set (and count k+1) for every k = 1..100 (note
research/notes/mechanical-slope-correction.md, programs /tmp/mech3.py..mech6.py,
/tmp/bridge.py, prior cycle); k=3 oracle match also hand-checked in this
digest (34/89 -> {001,010,100,101}). The literal directive slope F(n-1)/F(n)
fails (produces 11, absent from the Fibonacci word; k=3 gives {010,011,101,110}).
follows-from: governing-factor-complexity, governing-sturmian
anchor: research/sources/perrin-sturmian-words-lecture2-mechanical.full.md
(rotation coding, interval I_w, same-slope-same-factors);
research/sources/perrin-restivo-note-sturmian-words.full.md (digit formula,
characteristic word)
bearing: Reduces the object set to k+1 mechanical-word representatives with an
arithmetic digit formula — this is what makes Psi(10^18) tractable at all.
```

```claim
id: steer-d2-literal-slope
statement: Steering directive 2 instructs the run to model the k+1 factors as a
mechanical word of "slope a = F(n-1)/F(n)" for F(n) >> k.
hypotheses: F is a Fibonacci sequence in any standard convention.
holds-here: no — under every standard convention F(n-1)/F(n) -> 1/phi ~ 0.618,
which is the ones-density of the complement word, not of S. Exact arithmetic at
k=3 with 55/89 yields factors {010,011,101,110}, not the problem's
{001,010,100,101}. The corrected slope is F(n-2)/F(n) -> 1/phi^2 ~ 0.382.
status: asserted (steer input); refuted as stated by the k=3 exact check
contradicts: mechanical-word-digit-rule
bearing: Do not implement the directive's literal slope; use F(n-2)/F(n).
```

```claim
id: governing-universal-euclidean
statement: The universal Euclidean algorithm (monoid generalisation of AtCoder
floor_sum, "Chtholly's algorithm") evaluates sums of the form
sum_{i=0}^{n-1} x^i * floor((a*i+b)/c), and the tuple
(count, sum x^i, sum x^i floor, sum x^i floor^2), in O(log(max{a,c})) time via
the merge-and-flip recursion F(a,b,c,n,U,R) = (b>=c: U^{b/c} F(a, b%c, c, n, U, R);
a>=c: F(a%c, b, c, n, U, U^{a/c} R); else with m=floor((a n+b)/c): m=0 -> R^n,
m>0 -> R^{(c-b-1)/a} U F(c, (c-b-1)%a, a, m-1, R, U) R^{n - floor((c m - b -1)/a)}).
hypotheses: a,b,c,n >= 0 integers, c > 0; x a unit in the ring (mod M =
101001001, x = 10^{-1}, exists since gcd(10, M) = 1); carried quantities linear
in the floor argument (monoid closure).
holds-here: yes — directive 2's Psi(k) is the second moment of a linearly
(geometrically) weighted floor sum, within monoid closure.
status: sourced
anchor: research/sources/oi-wiki-universal-euclidean-floor-sum.full.md;
research/sources/universal-euclidean-geometric-weight-fhq.full.md;
research/sources/loj138-universal-euclidean-floor-moments.full.md;
research/sources/atcoder-math-hpp-v151.full.md (floor_sum)
bearing: This is the O(log) primitive that makes Psi(10^18) mod M computable
without enumerating ~10^18 terms.
answers: citable-name-treatment-0c91, citable-precise-statement-600d, citable-precise-statement-d2e7
```

---

Notes on coverage:

- Answers request `citable-statement-theorem-039a` (Sturmian / factor complexity
  k+1): `governing-sturmian` + `governing-factor-complexity`.
- Answers requests `citable-precise-statement-600d`, `citable-precise-statement-d2e7`,
  `citable-name-treatment-0c91` (universal Euclidean / geometric-weight floor_sum):
  `governing-universal-euclidean`.
- **Contradiction on disk:** `steer-d2-literal-slope` (holds-here: no) vs
  `mechanical-word-digit-rule` (holds-here: yes, corrected slope). This is the
  most valuable finding of this digest: a wrong slope at k=10^18 would swap
  every digit, giving a completely different Psi.