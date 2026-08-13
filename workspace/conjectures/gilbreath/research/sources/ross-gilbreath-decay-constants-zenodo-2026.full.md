<!-- source: https://zenodo.org/records/21326026/files/Empirical_Structure_of_the_Gilbreath_Decay_Constants.pdf | converted from PDF -->

Empirical Structure of the Gilbreath Decay Constants

Michael M. Ross
Independent Researcher
michaelmross@cantab.net

July 2026

Abstract

Chase, Hunter, and Tao introduced a stationary continuous Gilbreath model in which the
top row consists of independent standard exponential variables and ci := E a(i, j) denotes the
expected entry at depth i. They proved ∑

i≤n ci ≥ log(n + e), computed c0, . . . , c3 exactly, and
could not prove that (ci) is bounded. This note reports a Monte Carlo study to depth 8192,
anchored by new exact rational values of c4, c5, and c6. The principal empirical law is

ci ≈ C λs2(i)

i ,

where s2(i) is the binary digit sum and the effective λ drifts slowly through approximately
1.14–1.20 in the sampled windows. The conjectural 1/i behavior thus becomes visible after
conditioning on digit-sum classes, while pooled data decay more slowly and display a pronounced
dyadic sawtooth; at extreme digit sums the modulation saturates below its geometric extrapola-
tion. Complementary finite-depth experiments indicate a polynomial-versus-exponential growth
transition for continuous uniform data, a full-row relaxation law of order G
0.63–G
0.66, and a spike
survival distance asymptotic to its amplitude. These findings quantify the decay mechanism of
the Gilbreath array that lies beyond the elementary parity wave.

1 Introduction

Given a sequence a1, a2, . . ., its Gilbreath array is defined recursively by

a(0, j) = aj, a(i + 1, j) = |a(i, j) − a(i, j + 1)|. (1)

For the prime sequence, Gilbreath’s conjecture asserts that the left edge equals 1 at every positive
depth. There are two distinct mechanisms in that statement. If a sequence begins with 2 and is
followed by odd integers, parity alone forces every subsequent leading entry to be odd. It does not
force that entry to be 1. The latter behavior requires the array to reach and sustain the closed
{0, 2} regime, in which a leading 1 remains pinned. This distinction is developed in the companion
note [3].
The present paper concerns the quantitative question behind that second mechanism: how
rapidly do typical amplitudes in an absolute-difference array decay? Chase, Hunter, and Tao (CHT)
study the continuous stationary model in which the aj are independent exponential random variables
of mean one [2]. Translation invariance in j gives

E a(i, j) = ci, (2)

1

where ci depends only on the depth. They prove

n∑

i=0 ci ≥ log(n + e), (3)

so exponential decay is impossible. They tentatively suggest that 1/i may be the maximal plausible
rate, but note that the available theory does not even establish that (ci) is bounded [2, Remark 1.5].
The experiments below reveal a more structured version of the 1/i picture. The binary digit sum

s2(i) := the number of ones in the binary expansion of i

modulates the leading order. This is natural: CHT already point to Lucas’ theorem and the fact
that row i of Pascal’s triangle has 2s2(i) odd entries. The new numerical claim is that this parity
statistic enters approximately geometrically.

All asymptotic-looking statements in this note, except the exact low-depth values and identities
explicitly derived below, are empirical. The figures are intended to identify theorem-shaped targets,
not to substitute for proofs.

2 Exact low-depth anchors

The constants ci are rational. Writing ar = sbr, where s = ∑i+1
r=1 ar and (b1, . . . , bi+1) is uniform on
the standard simplex, homogeneity gives

ci = (i + 1)E b(i, 1). (4)

On each region where the signs of all intermediate differences are fixed, b(i, 1) is a linear form.
Partitioning the simplex into these rational sign cones therefore reduces ci to a finite sum of rational
polytope volumes and first moments.
CHT record c0, c1, c2, c3. Exact sign-cone computations in the present study extend the table by
three values: c4 = 778959731701
1447295850000 = 0.5382173463 . . . , (5)

c5 = 14008668886481596262550223816901
25320304994525128311856832700000 = 0.5532582996 . . . , (6)

and c6 = 0.448388672133 . . ., whose reduced fraction has a 150-digit denominator and is deposited
with the supplementary data. Each value is certified by an exact partition-of-unity identity (the
cone volumes sum to exactly 1), by reproduction of CHT’s c2 = 7/9 and c3 = 227/288 in the same
pipeline, and by agreement with independent Monte Carlo estimates within one standard error at
2 × 108–5 × 108 samples. Table ?? summarizes the low-depth values.
CHT already observed that monotonicity fails at c2 < c3. The exact continuation shows the
failure is systematic: the weave c3 > c4 < c5 > c6 tracks the digit-sum column of Table ??. The
arithmetic also grows rapidly more complicated: the largest primes dividing the denominators of c4,
c5, c6 are 17, 47, and 331 respectively, and in the sign-cone decomposition every pattern is feasible
through depth four while the first infeasible cones appear at depth five. Both trends are consistent
with the absence of a simple closed form.
 2

Table 1: Low-depth Gilbreath decay constants and binary digit sums. All values through c6 are exact; the
longest rational representations are given in (5)–(6) and the data supplement.

i decimal value s2(i)

2 0.7777777778 = 7/9 1

3 0.7881944444 = 227/288 2

4 0.538217346302 1

5 0.553258299594 2

6 0.448388672133 2

3 A digit-sum-modulated decay law

3.1 The first-order model

The main simulation used 768 independent pyramids of width 8192. For each depth, all available
horizontal entries were averaged, and the exact constants through depth six were superimposed as
checks. Figure 1 compares the resulting ci with

̂ci = Cλs2(i)

i . (7)

Across broad interior windows, the geometric modulation is striking: points with the same value of
s2(i) form nearly parallel 1/i strands, and ratios between adjacent digit-sum classes are approximately
constant. The effective fitted parameter is not stable at the present depths; representative windows
give values near 1.14, 1.20, and 1.17. Accordingly, (7) should be read as a one-term empirical law
with slowly varying coefficients, not as a fitted asymptotic formula with an identified constant.

Empirical observation 1 (Conditional 1/i behavior). Within a fixed binary digit-sum class, the
data are consistent with ci decreasing proportionally to 1/i across successive dyadic scales. The
visible failure of a single smooth C/i curve is largely a consequence of the changing distribution of
s2(i).

This is a refinement, rather than a literal confirmation, of a pointwise ci ≍ 1/i law. The factor
λs2(i) can grow with i, so no uniform constant multiple of 1/i is suggested by the data.

3.2 Dyadic averaging

The digit law predicts a specific difference between conditional and pooled slopes. If i is uniform in
the dyadic block [2m, 2m+1), then
 s2(i) d
= 1 + Bin(m, 1/2),

and therefore
 E λ
s2(i) = λ ( 1 + λ
2
 )m . (8)

Since i ≍ 2m, the block-averaged form of (7) is of order

i
−1+α(λ), α(λ) := log2
 ( 1 + λ
2
 ) . (9)

3

Figure 1: Monte Carlo estimates of ci through depth 8192 (red), the digit-sum model Cλs2(i)/i with a
deep-window estimate λ = 1.17 (green), and the pure 1/i envelope (dotted). Open circles mark exact
low-depth values. The flare near 2
13 is partly genuine binary structure and partly a loss of effective sample
size.

For λ between 1.14 and 1.20, one obtains α ≈ 0.098–0.138, hence a pooled exponent around −0.90
to −0.86 before accounting for scale drift and within-class skew. Binary averaging thus explains a
substantial part of the shallower slope seen in an undifferentiated log–log fit, though not, at the
present fitted values of λ, all of it; this residual is one reason not to overstate the one-parameter
model.

3.3 The terminal digit-sum crescendo

The sharp flare near the right edge of Figure 1 has two sources. The first is real. Integers just
below 213 = 8192 have unusually many binary ones, culminating in s2(8191) = 13, so (7) predicts
a dyadic crescendo, and the measured values follow it: ici rises from roughly 4.5 early in the last
octave to about 33 at its extreme edge. The second source is statistical. At depth i, a pyramid
of width N supplies only N − i horizontal entries, correlated over a range that grows with i; the
measured relative standard error rises from about 2.3% near i = 1000 to 25% at i = 8191. The final
one percent of depths should therefore not be used to estimate λ without a dedicated boundary
correction.
There is nevertheless a systematic effect beyond the noise. Near the crest, the data fall below
the geometric extrapolation: the data/model ratio decreases from about 0.95 near i = 7200 to
roughly 0.80–0.55 over the final high-digit-sum range. If the modulation is written more generally as
ci ≈ C g(s2(i))/i, then log g(k) appears concave for extreme k: the digit-sum modulation saturates
rather than remaining perfectly geometric.
 4

4 Finite-depth growth thresholds

Following Chase’s random analogue of Gilbreath’s conjecture [1], CHT prove an almost-sure Gilbreath
result for broad independent integer-valued models whose entries are eventually bounded by δn, for
sufficiently small δ, and show that a general statement fails at the exponential scale 2n+1 [2]. They
explicitly describe the gap between linear and exponential growth as difficult to narrow.
To probe a natural one-parameter family, we generated independent continuous variables

aj ∼ Unif[0, R(j)] (10)

for several rate functions R, and measured

pn(R) := P(a(n − 1, 1) > 1
). (11)

This is a finite-depth amplitude test, not a direct instance of the integer-valued theorem. The results
are shown in Figure 2. Every tested linear or polynomial rate trends downward or turns downward
by the largest sampled depths; even R(j) = j4 falls from a near-saturated failure probability. By
contrast, the tested exponential rates, including 2j/64, rise decisively.

Figure 2: Finite-depth failure probabilities for continuous uniform input aj ∼ Unif[0, R(j)]. Error bars are
binomial standard errors from 150–400 trials per point. In the tested family, polynomial rates decay or
turn downward, while exponential rates grow.

Open question 1 (Uniform-family threshold). For the continuous uniform family (10), does
pn(R) → 0 for every polynomial R, while some or every exponential rate R(j) = 2εj remains
supercritical? If so, how does this family-specific threshold coexist with the potentially lower worst-
case threshold in the general CHT framework?

The experiment does not refute a linear worst-case threshold. It indicates only that continuous
uniform data appear much more contractive than the most adversarial distributions allowed by a
general theorem.
 5

5 Transient decay and propagation

The constants ci average over stationary exponential input. A complementary way to inspect the
mechanism is to inject bounded disturbances and measure how long or how far they survive. Figure 3
summarizes three such experiments.

Figure 3: Three transient diagnostics. Left: the measured full-row grind-down time is a power law in the
gap bound G, with fitted exponent 0.66 in this run and 0.63–0.66 across runs. Center: a spike of size
G = 512 in a diverse {2, 4, 6} background loses approximately one unit of wall amplitude per column of
separation. Right: the measured survival distance satisfies d∗(G)/G → 1 over the sampled range; error
bars use 12–20 independent backgrounds.

First, for random even top rows with entries bounded by G, the full-row grind-down time τ is
not logarithmic. The data fit
 τ (G) ≍ G
β, β ≈ 0.63–0.66. (12)

The visual dynamics are geometric at first but end in a long linear “chipping” phase, which dominates
the stopping time.
Second, place a single spike of amplitude G at distance d from the left wall in a diverse small-gap
sea. For G = 512, the disturbance arriving at the wall decreases almost linearly with slope −1 and
vanishes near d = G. Repeating across amplitudes gives

d
∗(G) ≈ G, (13)

with observed ratios d∗(G)/G progressing through approximately

0.79, 0.85, 0.93, 0.96, 0.98, 0.99.

This slope-one law is the cleanest candidate for a direct theorem among the transient experiments.
The background matters. Constant residue-class seas can conserve a disturbance: sets of the
form {0, d} are closed under absolute differencing, and constant-mod-4 environments can preserve
residue defects that a diverse sea absorbs. This is consistent with both the parity discussion in [3]
and the CHT inverse theorem, which isolates long zero blocks and long shallow {0, d}-valued blocks
as the deterministic obstructions to collapse [2].

6 Interpretation and open problems

The data support the following hierarchy.
 6

1. First order: after conditioning on binary digit sum, the decay is approximately 1/i.

2. Arithmetic modulation: the conditional scale grows approximately as λs2(i), explaining the
non-monotone sawtooth and much of the discrepancy between conditional and pooled slopes.

3. Second order: λ drifts with scale, the high-digit-sum tail saturates, and the terminal region
suffers severe loss of effective sample size.

4. Dynamical scale: bounded disturbances exhibit power-law relaxation and approximately
unit-speed attenuation toward the wall.

A useful first theorem would not need to identify an asymptotic constant. It would already be
significant to prove a digit-sensitive comparison such as

ci ≤ A Bs2(i)

i (14)

for absolute constants A and B, or to establish an averaged version over dyadic blocks. Even a
rigorous explanation of why neighboring digit-sum classes have asymptotically stable ratios would
turn the observed Pascal-parity connection into a quantitative theorem.
A second target is the propagation law (13). In a sufficiently mixing bounded background, one
may ask whether a spike of amplitude G can influence the wall only from distance at most G + O(1),
and whether examples attain G − O(1). Such a statement would give a precise metric version of the
light-cone intuition already present in the spacetime formalism of CHT.
Finally, none of the present averages removes the deterministic obstruction relevant to primes.
The parity wave guarantees only oddness at the left edge; the event “equal to one” requires the
suppression of rigid zero and two-valued structures. The empirical decay constants explain why
random arrays are expected to grind down, but Gilbreath’s conjecture asks whether the actual
prime-gap array always avoids the exceptional arrangements. That remains a separate arithmetic
problem.

Data and reproducibility note

Figure 1 uses 768 Monte Carlo pyramids of width 8192. Figure 2 uses 150–400 trials per point
and a continuous-uniform model throughout. In Figure 3, the full-row fit is based on 60 trials
per displayed mean, and the safe-distance error bars use 12–20 independent backgrounds. The
generating code, exact rational certificates through c6 (including the volume identities), and
the raw data files are deposited with the archival version of this manuscript. Code and full
reproducibility details are available at https://github.com/michaelmross/Gilbreath, archived
at DOI 10.5281/zenodo.21536390.

Acknowledgments

The author thanks Claude (Anthropic) and ChatGPT for assistance with exposition and computation.

References

[1] Z. Chase, A random analogue of Gilbreath’s conjecture, Mathematische Annalen 388 (2024), 2611–2625.

7

[2] Z. Chase, Z. Hunter, and T. Tao, Gilbreath’s conjecture: a Cram´er random model and a deterministic
analysis, arXiv:2607.08712, 2026.

[3] M. M. Ross, Is Gilbreath’s conjecture garden-variety numerology? What the parity argument proves, and
what remains open, michaelmross.github.io/gilbreath-parity-note.html.

[4] T. Tao, Gilbreath decay constants, interactive web application, https://teorth.github.io/tao-web/
apps/gilbreath-cn.html (accessed July 20, 2026).

8
