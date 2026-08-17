# Three-distance / factor-frequency structure — claims anchored to new sources

New sources this cycle (librarian):
- Alessandri & Berthé, "Three distance theorems and combinatorics on words",
  Enseign. Math. 44 (1998) — `research/sources/alessandri-berthe-three-distance-theorems.full.md`
- Berthé & Reutenauer, "On the Three-Distance Theorem", Math. Intelligencer 46
  (2024) — `research/sources/berthe-reutenauer-three-distance-intelligencer-2024.full.md`
- van Ravenstein, "The Three Gap Theorem (Steinhaus Conjecture)", J. Austral.
  Math. Soc. A 45 (1988) — `research/sources/van-ravenstein-three-gap-theorem-1988-hal.full.md`
- Berthé, "Fréquences des facteurs des suites sturmiennes", TCS 165 (1996) —
  `research/sources/berthe-frequences-facteurs-sturmiennes-1996.full.md`

These anchor the counting/structural side of directive 1 (the pair-correlation
route) and the slope-approximant threshold of directive 2 (the mechanical-word
route). Both were previously documented as "the exact closed form of A(d)
appears in no single paper" — the theory from which it follows is now on disk.

```claim
id: rotation-arc-factor-frequencies
statement: The k+1 points {-ma mod 1 : m = 0..k} cut the circle into k+1 arcs of
at most three different lengths, and if three lengths occur one is the sum of
the other two (three-distance theorem, Steinhaus/Sós/Surányi/Świerczkowski/
Slater/Halton). Dually, the gaps between successive visits {an} < beta take at
most three values (three-gap theorem). For a Sturmian sequence (coding of the
rotation, in particular PE1006's word of slope 1/phi^2 with the cut beta
matching the two-letter partition), the frequencies of the length-k factors take
at most three values, each realised by an explicitly counted number of factors
(Dekking for Fibonacci; Berthé 1996 for all Sturmian, via the word graph).
Berthé 1996 Théorème 1 makes it quantitative: for a Sturmian sequence of slope
alpha with m-points de Farey p1/q1 < alpha < p2/q2, the length-m factor
frequencies take only the three values { p2 - alpha q2, alpha q1 - p1,
alpha(q1 - q2) + p2 - p1 }, with multiplicities (m - q2 + 1), (m - q1 + 1),
(q1 + q2 - m - 1) respectively (so they sum to (q1+q2-1) - 2 + ... = the
special-factor count); in convergent notation the values are
(-1)^n(k p(n) + p(n-1) - alpha(k q(n) + q(n-1))), (-1)^n(alpha q(n) - p(n)),
and the third, for k q(n) + q(n-1) < m < (k+1)q(n) + q(n-1). These are the
exactly-three weights the arc/interval bookkeeping of directive 1 counts at
each lag.
hypotheses: alpha irrational (or rational with denominator > k); Sturmian
sequence = rotation coding with the partition [0,beta[, [beta,1[, beta in
{alpha, 1-alpha}.
holds-here: yes — the slope is a = F(n-2)/F(n) -> 1/phi^2 irrational; the k+1
arc-midpoint representatives of directive 2 and the lag structure of directive 1
are the same partition, so the "at most three lengths/values" structure is what
makes the autocorrelation counts A(d) a three-term closed form rather than a
distribution over many lengths.
status: sourced
anchor: research/sources/alessandri-berthe-three-distance-theorems.full.md
(three-distance thm p.1, three-gap p.2, Theorem 8);
research/sources/berthe-reutenauer-three-distance-intelligencer-2024.full.md
(Theorem 1, distance-encoding word);
research/sources/van-ravenstein-three-gap-theorem-1988-hal.full.md (Theorem 2,
first/last recurrence);
research/sources/berthe-frequences-facteurs-sturmiennes-1996.full.md (main
theorem, Dekking's case)
bearing: Supplies the named theory behind directive 1's verify-in-container
identity A(d) = max(0,m-t) + max(0,m-(N-t)): at each lag the pairs (j, j+d)
split into at most three gap classes, so the count is a sum of two clamped
linear terms instead of a histogram.
```

```claim
id: farey-slope-stabilisation
statement: Let p1/q1 < p2/q2 be consecutive m-points de Farey (Farey
neighbours of order m) and let alpha in ]p1/q1, p2/q2[. The length-m special
factors G_m and D_m (D_m = the expansive factor of the mechanical word of
slope alpha per Lemma 4; G_m its mirror image per Lemma 2 — these are the two
length-m factors with two one-sided extensions in the Rauzy word graph)
coincide exactly at m = q1 + q2 - 2: G_m = D_m iff m = q1 + q2 - 2 (Berthé
1996, Proposition 3, verbatim). In the Fibonacci case the Farey
neighbours of the convergent F(n-2)/F(n) are consecutive Fibonacci ratios,
giving q1 + q2 - 2 = F(n-1) + F(n-2) - 2 = F(n) - 2.
hypotheses: alpha between two consecutive Farey points p1/q1 < p2/q2.
holds-here: yes — directive 2 uses the rational slope a = F(n-2)/F(n) with
F(n) >> k; Proposition 3 says the factor set of the approximant coincides with
the Fibonacci word's factor set of length k exactly when k >= F(n) - 2, i.e.
the run's "F(n) >> k" margin is provably sufficient (and larger than the exact
threshold F(n)-2).
status: sourced
anchor: research/sources/berthe-frequences-facteurs-sturmiennes-1996.full.md
(Proposition 3)
bearing: Converts the run's empirical "word-length bound must be > 3k for
k=15" / "F(n) >> k" gate into a theorem: denominator F(n) needs only exceed
k + 2 for the factor set to be exactly the Fibonacci word's. It also justifies
the mechanical-word construction at k = 1..150 against the brute oracle.
```

```claim
id: distance-encoding-word-structure
statement: In the three-distance partition of [0,1] by {ialpha mod 1,
i = 0..n-1} U {1}, the leftmost interval is not the longest, and encoding the
successive interval lengths from left to right (leftmost -> a, longest -> b,
other -> c in the three-length case) produces a word which is the word encoding
of a circular symmetric discrete interval exchange; such words are exactly the
perfectly clustering Lyndon words (Berthé & Reutenauer 2024, Theorems 1, 3;
Ferenczi-Zamboni; Mantaci-Restivo-Sciortino for two letters).
hypotheses: n smaller than the smallest denominator of alpha when alpha is
rational; otherwise none (irrational alpha by compactness).
holds-here: yes — the run's arc partition uses rational alpha = F(n-2)/F(n)
with denominator F(n) > k, i.e. in the rational branch where the hypothesis
holds.
status: sourced
anchor: research/sources/berthe-reutenauer-three-distance-intelligencer-2024.full.md
(Theorem 1, Theorem 3; history: Sós/Surányi/Świerczkowski 1958, Slater, Halton)
bearing: Structural rigidity of the arc partition the solver iterates over
(the k+1 arc-midpoint intercepts in cyclic order); not directly load-bearing
for the arithmetic but fixes the ordering facts the mechanical-word
construction relies on.
```

```claim
id: dir1-domain-autocorrelation
statement: Directive 1's pair-correlation identity C(j,jp) = A(jp-j),
holds ONLY at k = F_n - 1 (k = 1, 2, 4, 7, 12, 20, 33, 54, 88, 143, ...), where
the k+1 factors are the F_n truncated cyclic rotations of a single standard
word. At general k (e.g. k=3, k=200, k=10^4) the identity is out of domain and
must NOT be weakened or rewritten to fit. For general k the correct replacement
is the arc version: C(j, j+d) equals the number of the k+1 partition
representatives lying in the arc A_j ∩ A_(j+d), where A_j = [frac(-(j+1)a),
frac(-ja)) has length a; the intersection is an arc whose LENGTH depends on d
alone (a - frac(-da) when frac(-da) < a, else a - (1 - frac(-da)) when that
< a, else empty), only its starting point depends on j — still a lattice-point
count that collapses. Phase 2 (telescoped v of directive 2) already passes at
k = 1..150 and is the load-bearing part; the remaining work is the
universal-Euclidean evaluation of the second moment.
hypotheses: the cyclic-autocorrelation form A(d) requires k = F_n - 1 (the k+1
factors are F_n rotations of one standard word); the arc-intersection form is
general in k.
holds-here: the primary route (directive 2, mechanical-word / telescoped
second moment) does not need Phase 3 at all and is valid for all k; directive 1
is a checkpoint at k = F_n - 1 only. The statement that k=3 / k=200 / k=10^4
are outside the identity's domain is consistent with directive 1's original
statement ("at k = F_n - 1 the k+1 factors are the F_n rotations").
status: asserted (steer directive 4; reproduction and any reliance are
tool_builder/solver tasks, not librarian work — the library records it so the
identity's domain is not forgotten)
anchor: config/directives (steering directive, Phase-3 note); the arc-length
account is the general-k arc-intersection count, recorded for the solver's
Phase-4 anchoring Psi(10^4)=16242174, Psi(10^6)=77578256 mod M.
bearing: Prevents the run from testing — and then "correcting" — the
autocorrelation identity outside its stated domain k = F_n - 1, which would be
a false negative. Re-tests of directive 1 must use only k = 1, 2, 4, 7, 12, 20,
33, 54, 88, 143, ...; the general-k lag collapse uses the arc-intersection
count whose length depends on the lag d alone.
```

The three-distance theorem itself is multiply anchored (Alessandri–Berthé;
Berthé–Reutenauer; van Ravenstein), and the "frequencies of factors take at
most 3 values" theorem is anchored in both Alessandri–Berthé (Theorem 8) and
Berthé 1996 (main theorem, with Dekking's Fibonacci case explicit).