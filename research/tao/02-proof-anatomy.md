# The anatomy of a Tao proof

Eleven solved problems, dissected for the *sequence of moves* that produced the
solution rather than the mathematics of the solution itself. Each entry uses a fixed
six-field schema so the file is parseable:

- **(a) As posed** — statement, who, when.
- **(b) Reframing** — the change of target that unlocked it.
- **(c) Imported machinery** — what, and from which adjacent field.
- **(d) Computed / verified** — numerics, certificates, formalisation.
- **(e) Program length and ladder** — years elapsed, prior partial and no-go results.
- **(f) Transferable move** — a firing rule, with a trigger and a safety check.

Three findings deserve to be read before the entries, because they invert the
folklore:

1. **Polymath8 is the cautionary case, not the triumphant one.** Thirteen months of
   collaborative optimisation drove the prime gap from 70,000,000 to 4,680. Maynard
   then reached 600 independently while *discarding* the Zhang/Polymath8a
   equidistribution machinery entirely, needing only classical Bombieri–Vinogradov.
   The winning branch was not the one the effort went into. An agent that budgets by
   "progress per unit effort on the current branch" would have starved the branch
   that won.
2. **Greenfeld–Tao's no-go results were navigational, not consolation.** Their 2021
   rigidity result ("the swapping property") proved that a one-tile Wang encoding
   *cannot* work. That is what sent them to the Sudoku encoding that did. A no-go is
   a search-space pruning operation, and should be scored as progress.
3. **The sunflower lemma shows a simplification cascade as a first-class research
   mode.** ALWZ (Aug 2019) → Rao's noiseless-coding rewrite (Sep 2019) → Tao's
   entropy rewrite (Jul 2020) → Bell–Chueluecha–Warnke's better bound (Sep 2020),
   plus a sideways transplant where Frankston–Kahn–Narayanan–Park carried the
   *spread lemma* onto Kahn–Kalai. Rewriting someone else's proof in a cleaner
   formalism is not exposition; it is what produced the next bound.

**Provenance note.** Entries 1–9 rest on sourced web research (arXiv, terrytao.wordpress.com,
Quanta, Polymath wiki), with URLs below. Entries 10–11 touch material at or past the
assistant's knowledge cutoff; claims there that were not verified against a live source
are marked **[UNVERIFIED]** and should be checked before being relied on.

---

## Index

| # | Result | Year | Dominant move | Target weakened? | Machine-verified? |
|---|---|---|---|---|---|
| 1 | Green–Tao (primes contain APs) | 2004/08 | Transfer through a majorant | No | No |
| 2 | Erdős discrepancy | 2015/16 | Route via a stronger conjecture, then weaken the input | Input, not output | Partially (SAT, C=2 only) |
| 3 | Collatz, almost all orbits | 2019/22 | Weaken target twice + change the measure | Yes, twice | No |
| 4 | Averaged Navier–Stokes blowup | 2014/16 | Prove a barrier about the method class | Target abandoned | No |
| 5 | Sendov, high degree | 2020/22 | Asymptotic-only, accept ineffectivity | Yes | No |
| 6 | Polynomial Freiman–Ruzsa | 2023/25 | Change the size functional (entropy) | No | Yes (Lean 4, 3 weeks) |
| 7 | Bounded prime gaps | 2013/14 | Parameterise into an optimisation problem | Yes (from twin primes) | Yes (tuple search, variational) |
| 8 | Sunflower lemma | 2019/20 | Re-derive in a cleaner formalism | No | Classical case only (Isabelle) |
| 9 | Periodic tiling counterexample | 2022/24 | Build the counterexample as a machine | No (refutation) | No |
| 10 | Tao–Ziegler / inverse Gowers | 2006–12 | Discharge the hypotheses of a conditional theorem | No | No |
| 11 | Equational Theories Project | 2024–25 | Mechanise an exhaustive search | N/A (new target) | Yes (Lean 4 + ATP) |

---

## 1. Green–Tao: the primes contain arbitrarily long arithmetic progressions

**(a)** That the primes contain arbitrarily long APs descends from the Erdős–Turán
program (their 1936 paper on APs in dense sets was motivated by the primes). Erdős's
stronger conjecture — any set with divergent reciprocal sum contains arbitrarily long
APs — is still open. arXiv math/0404188 (8 Apr 2004); *Annals* 167 (2008) 481–547.

**(b)** The primes have density zero, so Szemerédi does not apply. Rather than attack
that, they changed the target to *finding a pseudorandom majorant*: prove a **relative**
Szemerédi theorem for any measure ν satisfying a linear forms condition and a
correlation condition, then place the primes inside a set of almost primes where they
have positive *relative* density (~1/k). Density zero becomes density 1/k by changing
the ambient measure, not the set.

**(c)** Szemerédi's theorem (1975) as a black box, from combinatorics; the
Furstenberg (1977) ergodic and Gowers (1998–2001) Fourier proofs shaped the uniformity-norm
framework; the Goldston–Yıldırım sieve from analytic number theory — imported from the
*small prime gaps* program, a different problem entirely. The paper is filed under both
Number Theory and Dynamical Systems.

**(d)** Nothing load-bearing. The theorem is purely existential and exhibits no AP.
Records (AP-23 in 2004 through AP-27 by PrimeGrid in 2019) are downstream and independent.

**(e)** ~68 years from Erdős–Turán. Ladder: van der Corput 1939 (3-term APs);
Heath-Brown 1981 (4-term with one almost-prime); Green 2005 (*Roth's theorem in the
primes*, the k=3 case of the transference idea, one year ahead of the general result).
Six arXiv versions and a four-year referee gap. Simplified afterwards by Conlon–Fox–Zhao
(arXiv:1403.2957), who removed the correlation condition entirely.

**(f) MOVE — transfer through a majorant.** *Trigger:* the target set is too sparse for
a known theorem about dense sets. *Action:* do not attack sparsity; search for a
tractable superset in which the target has positive relative density, then prove the
known theorem relative to that superset's measure. *Check:* the majorant must satisfy
explicitly stated pseudorandomness conditions, and those conditions must be verifiable
for the actual superset — the sieve estimate is the real work, not the transference.

## 2. Erdős discrepancy problem

**(a)** Erdős, c. 1932: is there a ±1 sequence f and a constant C with
|Σ_{j≤k} f(jd)| ≤ C for all d, k? $500 prize. Open ~83 years.

**(b)** Two hops. *Hop 1* (Polymath5, Jan 2010): a Fourier-analytic reduction from the
general bounded-discrepancy hypothesis to a statement about **completely multiplicative**
functions. *Hop 2* (Sept 2015): route through the **Elliott conjecture**, used *as an
inverse theorem* — a bad multiplicative function is forced to correlate with a modulated
Dirichlet character, then killed by a variant of Borwein–Choi–Coons. This proved EDP
*conditionally* on 11 Sep 2015. The unconditional step, one week later, came from
**weakening the input**: a *logarithmically averaged* Elliott conjecture, weaker than the
one assumed, which the same argument accepts. The credit for the Elliott route belongs to
a Polymath5 participant, Uwe Stroinski.

**(c)** Multiplicative/"pretentious" number theory (Granville–Soundararajan);
Matomäki–Radziwiłł on multiplicative functions in short intervals — breakthroughs that did
not exist during Polymath5; and from **information theory** the new **entropy decrement
argument**, which Tao explicitly built by analogy with the density-increment and
energy-increment arguments around Szemerédi's theorem.

**(d)** Konev–Lisitsa (arXiv:1402.2184, Feb 2014) SAT-encoded the C=2 case: a maximal
sequence of length **1160** with discrepancy 2, and no sequence of length **1161**. The
DRUP unsatisfiability certificate was ~**13 GB**, larger than Wikipedia at the time and
not humanly checkable. Prior search had reached only 1124. This settled C=2 and nothing else.

**(e)** Polymath5 opened 19 Jan 2010 with the three-step program already sketched, ran
through 2010, was revived in Sept 2012, and **stalled without solving it**. SAT (2014)
handled one value of C. The solve came 11 Sep → 18 Sep 2015; arXiv:1509.05363; published
as *Discrete Analysis* 2016:1, the journal's inaugural paper. Note the shape: the
collaborative phase produced the reduction that the eventual solo proof used, five years
later, once external tools (Matomäki–Radziwiłł) existed.

**(f) MOVE — weaken the hypothesis, not the conclusion.** *Trigger:* you have a proof
conditional on conjecture X, and X is out of reach. *Action:* audit which consequences of
X the proof actually consumes, and try to prove only those — typically an averaged,
logarithmic, or low-moment version. *Check:* re-run the whole derivation against the
weakened X; "the argument adapts without difficulty" must be verified, not assumed.
*Corollary rule:* a stalled collaboration that produced a reduction is not a failure;
re-attempt it whenever a new external tool lands.

## 3. Almost all Collatz orbits attain almost bounded values

**(a)** The 3x+1 map, Lothar Collatz c. 1937: does every orbit reach 1? Lagarias:
"This is a really dangerous problem. People become obsessed with it and it really is
impossible."

**(b)** Three simultaneous changes, all explicit. *All* → *almost all*. *Bounded* →
*almost bounded* (Col_min(N) < f(N) for **any** f → ∞, e.g. four-fold iterated log).
And, the load-bearing one, *natural density* → **logarithmic density**. The reason for
the third is mechanical: the uniform measure on [1,x] is not transported by Collatz
dynamics to anything like the uniform measure on [1,x^θ], so local results cannot be
iterated; logarithmic density is approximately invariant, so they can. Tao's stated
analogy is Bourgain's invariant-measure method for nonlinear Schrödinger. The trigger was
social — an anonymous blog commenter suggested trying "almost all".

**(c)** PDE almost-sure local-to-global wellposedness and invariant measures (Bourgain);
**probability** — Syracuse random variables, total-variation stabilisation, renewal
processes, a 2D random walk avoiding triangles; **Fourier analysis** — a decay estimate
obtained from an *averaged* Riesz product after conditioning, not a plain one; 3-adic
analysis.

**(d)** Not central. Backdrop: Barina 2020 verified all N up to 2⁶⁸ on a single GPU
(2.2×10¹¹ 128-bit numbers/sec).

**(e)** ~82 years. Ladder, every rung a *natural*-density statement with a polynomial
ceiling: Terras 1976 (Col_min(N) < N); Everett 1977; Allouche 1979 (θ > 0.869); Korec
1994 (θ > 0.7924, the record for 25 years); Krasikov–Lagarias 2003. Tao trades natural
for logarithmic density and gets an essentially arbitrary sub-polynomial ceiling — a
strictly incomparable statement, not a better exponent. **He had written the no-go
himself in 2011**: any proof of full Collatz must use transcendence theory or create
exponential separation between powers of 2 and 3. The 2019 paper sidesteps its author's
own barrier by not proving the conjecture.

**(f) MOVE — change the measure to one the dynamics preserves.** *Trigger:* you have a
local result that resists iteration into a global one. *Action:* check whether the failure
is that your measure is not (approximately) invariant under the map; if so, search for one
that is, and restate the theorem in it. *Check:* the new measure must still make the
conclusion meaningful — logarithmic density is weaker than natural density, and saying so
is part of the result. *Companion rule:* when a barrier you believe blocks target T,
enumerate the weakenings of T that the barrier does not cover.

## 4. Finite-time blowup for an averaged 3D Navier–Stokes equation

**(a)** Global regularity for 3D incompressible Navier–Stokes; Clay Millennium Problem
(2000). Write it as ∂_t u = Δu + B(u,u), where ⟨B(u,u),u⟩ = 0 *is* the energy identity.
arXiv:1402.0290 (3 Feb 2014); *JAMS* 29 (2016) 601–674.

**(b)** Abandon the equation. Replace B by an **averaged** B̃ — averaged over spatial
rotations and order-zero Fourier multipliers — chosen so ⟨B̃(u,u),u⟩ = 0 still holds, then
construct a smooth finite-time-blowup solution for B̃. Because those operations are
bounded on essentially all relevant function spaces, B̃ obeys almost every upper-bound
estimate B does. So any proof phrased purely in terms of such estimates plus the energy
identity would apply verbatim to B̃ and prove something false. Tao: "it is not possible to
establish global regularity by any 'abstract' approach which only uses upper bound
function space estimates on the nonlinear part of the equation, combined with the energy
identity." The output is a theorem about a *class of methods*.

**(c)** Dyadic shell ODE models from Katz–Pavlović. The conceptual import is **computer
architecture**: the blowup mechanism is "a von Neumann machine … that, after some time
delay, manages to suddenly create a replica of itself at a finer scale." Each copy is
(1+ε₀) times smaller and (1+ε₀)^{5/2} times faster; the geometric series converges, hence
finite-time blowup. Tao's speculation — "if one could somehow create enough 'logic gates'
out of ideal fluid, one could presumably build a sort of 'fluid computer', at which point
the task … reduces to a software engineering exercise rather than a PDE problem."

**(d)** None.

**(e)** Seven years of deliberately building the barrier. 2007: *Why global regularity for
Navier–Stokes is hard* — the supercriticality diagnosis, with an explicit enumeration of
what any successful method must do. 2007: arXiv:0710.1604, quantitative formulation. 2009:
global regularity for a *logarithmically supercritical* hyperdissipative NSE — the
positive-direction probe measuring exactly how far past criticality energy methods reach.
2014: the barrier as a theorem. 2016: an Euler-type vorticity-form blowup fixing the
missing vorticity equation, with the honest caveats (Type II not Type I; no Hamiltonian
structure). Tao in 2014: "I don't expect this program to come to fruition any time in the
next five years." **Downstream:** Cardona–Miranda–Peralta-Salas–Presas built Turing-complete
stationary Euler flows on the 3-sphere (arXiv:2012.12828; *PNAS* 2021) — via **contact
geometry**, not PDE. The speculation seeded a programme in a different community.

**(f) MOVE — prove the barrier when you cannot prove the theorem.** *Trigger:* repeated
attempts on T fail, and you can characterise what your attempts have in common (e.g. "only
uses estimate class E plus conserved quantity Q"). *Action:* construct a perturbed problem
T′ that satisfies every property in that characterisation but is false, and prove T′ false.
*Check:* the perturbation must genuinely preserve *all* the exploited properties — the
value of the barrier is exactly the size of the class it kills, and an unfaithful
perturbation kills nothing. *Corollary:* a barrier is a positive result; record it as
pruning, and log which future attempts it forbids.

## 5. Sendov's conjecture for sufficiently high degree polynomials

**(a)** Blagovest Sendov, 1959 (long misattributed to Iliev): if a complex polynomial of
degree n ≥ 2 has all zeros in the closed unit disk, then for each zero λ₀ there is a zero
of f′ within distance 1 of λ₀. arXiv:2012.04125 (8 Dec 2020); *Acta Mathematica* 229 (2022)
347–392.

**(b)** Do not prove the conjecture; prove there exists an absolute n₀ such that it holds
for all n ≥ n₀. "All degrees" → "all large degrees" buys an asymptotic regime where
compactness applies. The price is paid openly: the proof is compactness-and-contradiction
(assume counterexamples with n → ∞, extract limits by repeated subsequence extraction), so
it is **ineffective** — no explicit n₀ falls out, and Tao says any quantitative substitute
would give an n₀ "certainly much larger than 9."

**(c)** **Probability and potential theory into complex analysis.** Zeros of f and f′
become random variables; the tools are logarithmic potentials, Stieltjes transforms,
balayage, Grace's theorem, unique continuation for harmonic functions, and the
"cheap nonstandard analysis" compactness formalism familiar from PDE. The limiting identity
has a Brownian reading: two Brownian motions started at the two limit laws exit the unit
disk with the same distribution.

**(d)** No numerics of consequence. Two regimes handled separately (zero near the origin;
zero near the boundary), each closed by a contradiction — an argument-principle winding
number in one, incompatible Fourier-mode conditions in the other.

**(e)** 61 years. The prior ladder is *degree-by-degree verification*, which is the point:
n < 6 (Meir–Sharma 1969), n < 7 (Brown 1991), n < 8 (Borcea 1996), n < 9 (Brown–Xiang
1999) — thirty years to advance four degrees. Structural cases covered other ranges
(Gauss–Lucas at a=0; Bojanov 2011; Chalebgwa 2020; Kasmalkar 2014). Tao's move attacks
from the opposite end of the same axis, leaving a finite but astronomically large gap in
the middle. **[UNVERIFIED]** Wikipedia reportedly now records a claimed full proof of
Sendov (5 Aug 2026, Lech Mazur, with GPT-5.6 Pro assistance); an earlier claimed proof
preprint (arXiv:2210.08720) also exists. Neither was verified here.

**(f) MOVE — attack the parameter axis from the opposite end.** *Trigger:* a conjecture
indexed by n where verification proceeds n = 1, 2, 3, … and has stalled. *Action:* try to
prove it for all sufficiently large n instead, using compactness in the n → ∞ limit.
*Check:* state the ineffectivity plainly, and do not claim the conjecture — the residual
gap may be unclosable in practice. *Note:* success here converts an infinite open problem
into a finite (if enormous) computation, which is a genuine change of kind.

## 6. Polynomial Freiman–Ruzsa (Marton's conjecture)

**(a)** Freiman (1960s) on sets with small sumset; **Katalin Marton** (d. 2019)
formulated the polynomial-bound variant, published on her behalf by Ruzsa in 1999. Proved:
if A ⊆ F₂ⁿ with |A+A| ≤ K|A|, then A is covered by at most 2K¹² cosets of a subspace H with
|H| ≤ |A|. Gowers–Green–Manners–Tao, arXiv:2311.05762 (9 Nov 2023); *Annals* 201 (2025).

**(b)** **Measure sets by entropy, not cardinality.** Work with random variables and the
entropic Ruzsa distance d(X;X) := H(X₁+X₂) − H(X). The engine is a *fibring inequality*:
for a homomorphism π, the doubling of the data is at least the doubling of its image plus
the conditional doubling of the fibres — which drives d down geometrically to an endgame
where characteristic-2 independence closes it. The entropy idea was **Gowers' from ~20
years earlier**, resurrected in June 2023. Tao: "At some point we realized that these old
ideas from Tim from 20 years ago were actually more likely to work than the ones we were
trying."

**(c)** Information theory into additive combinatorics.

**(d)** The formalisation is the story. Launched **13 Nov 2023, four days after the
preprint**; declared complete **5 Dec 2023** — three weeks; **~25 volunteer contributors**,
several of whom the maintainers had never met; **Tao wrote about 5% of the Lean himself**.
Coordination ran on Patrick Massot's **Blueprint**: a human-readable proof skeleton with a
colour-coded dependency graph (green = formalised, blue = ready to formalise) linked to the
Lean, running within ~48 hours of launch. Tao on why this scales: "my fellow repository
maintainers and I have already approved several pull requests from contributors that had
not previously met, as the code was verified to be correct." Formal verification removes
*trust* as a prerequisite for mass collaboration. By-product: a Shannon entropy inequality
library now upstreaming into Mathlib. On AI: Copilot's inline suggestions were sometimes
"almost correct," but Lean's own `exact?` search was more effective.

**(e)** ~24 years from Marton's formulation. Prior bounds were exponential; **Sanders 2012**
gave a quasi-polynomial Bogolyubov–Ruzsa lemma (exp(log^{3+ε} K) cosets), the record until
2023 — and, notably, good enough to lower the field's sense of urgency without resolving
anything. Sequels came fast: bounded-torsion groups (Apr 2024), Liao's exponent improvement
to 11, then 9 in the repo.

**(f) MOVE — replace the size functional with one that has a chain rule.** *Trigger:* an
induction on a combinatorial quantity (cardinality, count) that resists because the
quantity does not decompose along maps. *Action:* find an information-theoretic or
analytic surrogate with a decomposition identity, restate the conjecture in it, and induct
there. *Check:* the surrogate statement must imply the original — the translation back is a
proof obligation, not a formality. *Companion rule:* when a proof is finished, formalising
it is a parallelisable task with near-zero coordination cost, because the verifier replaces
peer trust. Budget three weeks and twenty strangers, not two years and a co-author.

## 7. Bounded gaps between primes: Zhang, Polymath8, Maynard

**(a)** Twin primes: liminf(p_{n+1} − p_n) = 2. The tractable target came from
Goldston–Pintz–Yıldırım (2005): any exponent of distribution θ > 1/2 in Bombieri–Vinogradov
gives bounded gaps outright. Granville, on the near-miss: "We could have done this seven
years ago if we hadn't been so sure we couldn't do it!" **Zhang**, announced 13–14 May 2013,
*Annals* 179 (2014): gaps < 7×10⁷.

**(b)** Three successive reframings. *Zhang:* do not prove Elliott–Halberstam; prove a
weakened version restricted to **smooth squarefree moduli**, which suffices for GPY.
*Polymath8:* the whole argument is numerically parameterised in (ϖ, δ, k₀, H), so the
result becomes an **optimisation problem** — and, being modular, splits into six components
worked in parallel. *Maynard:* replace GPY's one-variable sieve weight with a
**multi-variable** one, scoring each number individually rather than the tuple collectively,
converting the problem into a calculus-of-variations problem over a simplex. Tao's own
statement of the sting: Maynard's arguments "avoid using the difficult partial results …
established by Zhang and then refined by Polymath8; instead, the main input is the classical
Bombieri–Vinogradov theorem."

**(c)** Zhang: Kloosterman sums, Weil/Deligne bounds, the Heath-Brown identity.
Polymath8a: ℓ-adic **trace functions** and the Graham–Ringrose method, brought in bodily by
their practitioners (Fouvry, Kowalski, Michel, Nelson) — algebraic geometry over finite
fields walking in as people, not citations. Polymath8b: **quadratic programming and Krylov
iteration** from numerical analysis.

**(d)** Two computational subprojects, and here computation *is* the endgame.
*Narrow admissible tuples:* Zhang, Hensley–Richards, Schinzel and greedy sieves, iterated
merging (~5% narrower than previous constructions), plus local optimisations; Engelsma's
pre-existing private database was opened to the project; Sutherland ran a public submission
database that auto-converted a new k into a new H. *The variational problem:* M_k bracketed
numerically (1.845 ≤ M₄ ≤ 1.848; 3.95608 ≤ M₅₉ ≤ 4.148), with M_k > 4 the threshold that
matters. The final k=50 / H=246 record was a **two-week computation** by Pace Nielsen.

**(e)** ~13 months, 37 blog threads, 20–50 comments a day at peak, a wiki, a shared Dropbox.
The ladder: 70,000,000 (14 May 2013) → 59,874,594 → 13,008,612 → **Polymath8a launches 4 Jun**
→ 388,284 → 11,123 → 5,414 → **4,680 (27 Jul, 8a endpoint)** → **600 (19 Nov, Maynard,
independently)** → 576 → 330 → 270 → **246 (14 Apr 2014)**. Conditional: 12 under EH, 6 under
GEH — and 6 is the barrier for sieve methods, so the method's own ceiling was reached and
identified. Tao on the pace: "Just ten minutes of effort … there was a chance to push the
bound down … and claim, however briefly, the 'world record'." Sutherland on the cost:
"The participants really have to be comfortable with making mistakes in a forum that is
both public and permanent." Kowalski: without the format, "we would never have dared to make
such a technical improvement public."

**(f) MOVE — parameterise, then optimise; but fund the orthogonal branch.**
*Trigger:* a proof whose conclusion is a number determined by several independent technical
inputs. *Action:* expose the parameters, split the argument into modules with a published
interface between them, and let each module improve independently; maintain a live
leaderboard so improvements compose automatically. *Check — the important one:* monotone
improvement on a fixed architecture has a ceiling, and a *structurally different* attack may
leapfrog the entire ladder from a weaker starting point. Reserve budget for the branch that
is not currently winning. Concretely: an agent measuring "progress per unit effort" on the
Zhang branch would have deprioritised exactly the sieve redesign that won.

## 8. The sunflower lemma, and simplification as a research mode

**(a)** A sunflower with r petals: sets A₁…A_r sharing a core A₀ with pairwise disjoint
petals A_i∖A₀. **Erdős–Rado**, 1960: any k!(r−1)^k + 1 sets of size k contain an r-sunflower;
conjectured C(r)^k suffices. Erdős offered **$1,000** for r = 3. Open 59 years.

**(b)** ALWZ (Alweiss–Lovett–Wu–Zhang, arXiv:1908.08483, 22 Aug 2019; *Annals* 194 (2021))
improved the bound to about (log w)^w, proving it for a *robust* notion of sunflower for
which their bound is sharp to lower-order terms. The shared engine is the **spread lemma**:
a random set **A** is R-spread if P(S ⊂ **A**) ≤ R^{−|S|} for all S. Then the cascade.
**Rao** (Sep 2019) replaced ALWZ's probabilistic random-restriction argument with an explicit
**Shannon noiseless coding** construction. **Tao** (20 Jul 2020) rewrote Rao once more:
"Rao's argument used the Shannon noiseless coding theorem. It turns out that the argument
can be arranged in the very slightly different language of Shannon entropy" — prefix codes
and code-length accounting become conditional entropy and the chain rule. His stated payoff
is precise and mechanical: "One nice advantage of the entropy formalism over the
combinatorial one is that the analogue of this instance of the Cauchy–Schwarz inequality
automatically becomes an equality."

**(c)** Information theory into extremal set theory — twice, by two different routes
(coding theorem, then entropy).

**(d)** No search or formalisation of ALWZ. The *classical* Erdős–Rado lemma is formalised
in Isabelle/HOL (René Thiemann, Archive of Formal Proofs, Feb 2021).

**(e)** Thirteen months for the whole cascade, against 59 years of near-stasis: Kostochka
1997 was essentially the only significant improvement in 37 years, and Naslund–Sawin 2017
attacked sunflower-*free* sets with the slice-rank polynomial method from the cap-set
breakthrough — an adjacent-field import that did *not* crack the main conjecture. After
ALWZ: Rao (Sep 2019) → Tao (Jul 2020) → **Bell–Chueluecha–Warnke** (Sep 2020), whose
(Cp log k)^k drops the log p and is the current best. Sideways:
**Frankston–Kahn–Narayanan–Park** (Oct 2019) repurposed the spread machinery to prove the
fractional Kahn–Kalai expectation-threshold conjecture, and **Park–Pham** (2022) then proved
full Kahn–Kalai in five pages with the spread lemma falling out as a corollary.

**(f) MOVE — re-derive a fresh proof in a cleaner category, then look sideways.**
*Trigger:* a new result whose argument is ad hoc, or phrased in a formalism with slack
(explicit constructions, encodings, case analysis). *Action:* identify the formalism in
which its key inequality becomes an *identity*, and rewrite. Then extract the reusable
lemma from the middle of the proof and test it against unrelated open problems.
*Check:* the rewrite must reproduce or improve the bound, not merely restate it — and
scoring should credit the extracted lemma, since here the spread lemma outlived the
sunflower application that produced it.

## 9. Greenfeld–Tao: a counterexample to the periodic tiling conjecture

**(a)** If a finite F ⊂ Zᵈ tiles Zᵈ by translations, must it also tile periodically?
Stated explicitly by Lagarias–Wang (1996), implicit in Grünbaum–Shephard's *Tilings and
Patterns* (1987). Known true for d=1 (Newman 1977), R¹ (Lagarias–Wang), **Z²**
(Bhattacharya 2020, by ergodic theory), R² for topological disks (Kenyon 1992), and convex
tiles in all dimensions. arXiv:2211.15847 (29 Nov 2022); *Annals* 200 (2024) 301–363.

**(b)** Three chained encodings turning tiling into programming. (1) *One equation → a
system:* stack many tiling equations into one over a larger group, creating "a 'tiling
language', in which each sentence … expresses a different type of constraint." (2) *Tiling
language → functional equations:* the vertical line test — A ⊕ ({0}×H) = G×H says exactly
that A is the graph of a function — converts set constraints into constraints on functions.
(3) *Functional equations → a Sudoku puzzle:* target a non-periodic p-adically structured
function (last nonzero base-p digit) and build a board where every non-vertical line must
exhibit 2-adic behaviour. Their vocabulary for the encoding — "expressible" and "weakly
expressible" properties — is explicitly analogous to Π⁰₀ and Σ⁰₁ in the arithmetic
hierarchy. Tao on programming with tiles: weakly expressible properties "allow us to easily
construct quite complicated weakly expressible properties out of a 'library' of simple
weakly expressible properties, much as a complex computer program can be constructed out of
simple library routines."

**(c)** Computability theory (the domino problem, Wang tiles, Berger 1966), model theory,
p-adic valuation arithmetic, and commutative algebra (Frobenius in F_p[Zᵈ], powering the
dilation lemma). Ergodic theory and Fourier analysis were tried and **abandoned**: "Our
investigations also originally used ergodic-theoretic and Fourier-analytic techniques, but
we ultimately found combinatorial methods to be more effective."

**(d)** **Nothing was computed.** No machine search, no code, no formal verification. The
group and hence the dimension are "in principle explicitly computable, but we have not
attempted to optimize the size of these objects"; the blowup is exponential because one must
conjunct exponentially many expressible properties. The informal figure reported is ~2^(100^100).
Open Question 10.1 asks for the smallest d.

**(e)** ~26–35 years, with **two published no-go results as navigation**. *Oct 2020,
structure of translational tilings:* a new combinatorial proof of Bhattacharya, plus the
first crack — an 8-element F ⊂ Z² with a level-4 tiling that is not weakly periodic.
*Aug 2021, undecidable tilings with two tiles:* the decisive no-go, the "swapping property",
a rigidity result proving that matching constraints **cannot** be encoded with a single
Wang-style tile. Tao stated the obstruction at the time: "we were forced to introduce a
second tile … This appears to be an inherent feature of the method, since we found a partial
rigidity result … that obstructs this encoding strategy." That result is what sent them to
Sudoku. Then announcement (18 Sep 2022) and full paper (29 Nov 2022) — during which the
encoding prime itself changed, from p = 53 to a 2-group, because "we were not able to make
these two types of functions 'talk' to each other." Follow-ups: undecidability of
translational monotilings (Sep 2023, using primes 53 and 59), and variants (May 2025).

**(f) MOVE — build the counterexample as a machine.** *Trigger:* a conjecture asserting
that every solution of some constraint system is structured/periodic, where the constraint
system is expressive. *Action:* establish that the constraint language can encode boolean
logic and a counter, assemble a library of reusable encodable properties, then *program* an
aperiodic object. *Check:* verify the language is genuinely closed under the composition
operations you need — the failure mode is two sub-languages that cannot talk to each other,
which happened here and forced a redesign. *Corollary — the important rule:* when an
encoding attempt fails, try to prove a **rigidity theorem** explaining why. A theorem saying
"this encoding is impossible" tells you which encoding to try next; an unexplained failure
tells you nothing.

## 10. Tao–Ziegler and the inverse conjecture for the Gowers norms

**(a)** Green–Tao, *Linear equations in primes* (2006; *Annals* 2010), established
Hardy–Littlewood-type asymptotics for systems of linear equations in the primes — but
**conditionally**, on two named conjectures: MN(s) (Möbius orthogonality to nilsequences)
and GI(s) (the inverse conjecture for the Gowers uniformity norms, asserting that a function
with large U^{s+1} norm correlates with a nilsequence of step s).

**(b)** The reframing is organisational rather than mathematical: *isolate the obstructions
as named, standalone conjectures, prove the main theorem conditionally on them, publish, and
then discharge them one at a time*. This converts one intractable problem into a public
dependency graph with an explicit critical path. GI(s) was then proved by Green–Tao–Ziegler
(arXiv:1009.3998; *Annals* 2012), MN(s) by Green–Tao, at which point the 2006 theorem became
unconditional retroactively. A parallel strand extended the Green–Tao transference machine
itself rather than the primes: *The primes contain arbitrarily long polynomial progressions*
(Tao–Ziegler, arXiv:math/0610050; *Acta Math.* 2008) replaced arithmetic progressions with
polynomial ones, reusing the majorant apparatus on a harder configuration.

**(c)** Ergodic theory — the Host–Kra/Ziegler structure theory of characteristic factors,
where nilsystems appear as the universal objects, imported into finitary additive
combinatorics. Ziegler's presence on both papers is the mechanism: the adjacent field
arrived as a collaborator. Also nilmanifolds and equidistribution on them (Lie theory).
A low-characteristic finite-field analogue was handled separately, where the naive form of
the conjecture is **false** and required repair.

**(d)** No significant computation or formalisation.

**(e)** ~6 years from conditional statement to unconditional, across a chain of papers, with
the finite-field cases and the low-characteristic correction as intermediate rungs.
**[UNVERIFIED — arXiv identifiers, dates and journal details in this entry are from memory
and were not confirmed against a live source; verify before citing.]**

**(f) MOVE — publish conditionally on named obstructions.** *Trigger:* a proof that runs to
completion except for one or more clearly statable gaps. *Action:* do not wait. Name each
gap as a standalone conjecture with a precise statement, publish the main theorem
conditionally, and treat the named conjectures as an explicit work queue.
*Check:* each named conjecture must be *self-contained* — statable and attackable without
the parent proof — or it is a restatement of the difficulty rather than a decomposition of
it. *Payoff:* the conditional theorem is citable immediately, other people can attack the
sub-conjectures, and discharging one upgrades every downstream result at once.

## 11. The Equational Theories Project

**(a)** For magmas (a set with one binary operation), consider the finite list of equational
laws of bounded complexity — **4694** of them, up to symmetry — and ask, for every ordered
pair, whether one law implies the other. That is roughly **22 million** implication
questions, essentially none of which any individual would pose alone. Launched by Tao in
**September 2024** as an open, Lean-4-backed collaboration; repository and blueprint at
teorth/equational_theories.

**(b)** The reframing is the choice of target itself: instead of picking one hard question,
pick a **complete, mechanically enumerable universe** of easy-to-state questions and resolve
*all* of them. This makes the work massively parallel, makes partial progress measurable as
a percentage, lets automated tools handle the bulk, and concentrates human attention on the
residue that resists. The interesting mathematics is then defined *after the fact* as
whatever the machines could not close.

**(c)** Automated theorem provers and SMT solvers (Vampire, Z3, Prover9), finite model
builders (Mace4) for counterexamples, term-rewriting/equality-saturation engines, custom
high-performance search code, and Lean 4 with Blueprint as the integration and trust layer —
the same coordination stack proven out by PFR one year earlier. **[UNVERIFIED: the specific
tool roster.]**

**(d)** Verification is the whole point: every implication and every refutation lands as a
checked Lean proof rather than a claim. The overwhelming majority of the ~22 million pairs
fell to automation; a small residue of genuinely hard implications required human insight
and bespoke constructions. **[UNVERIFIED: exact resolved/unresolved counts, contributor
count, completion date, and the arXiv identifier of the resulting paper.]**

**(e)** Months, not years, for a problem with no prior literature — because the problem was
*constructed to be* attackable at scale. The relevant prior result is not mathematical but
infrastructural: PFR (entry 6) demonstrated that a Blueprint-plus-Lean repository lets
strangers contribute verified work without trust. **[UNVERIFIED: 2025 completion details.]**

**Related and also [UNVERIFIED]:** during 2025 Tao worked with AI systems on mathematical
discovery (a collaboration involving AlphaEvolve is reported) and engaged with the Erdős
Problems database, where several long-open problems were reportedly resolved or located in
the literature with AI assistance. Details, attributions, and which problems were genuinely
*solved* versus *found already solved* were not verified here and should be checked directly.

**(f) MOVE — mechanise an exhaustive universe, then mine the residue.** *Trigger:* a class
of questions that is finitely enumerable, uniformly statable, and individually shallow.
*Action:* enumerate the whole class, throw every automated prover and model-builder at it,
require machine-checked output, and publish the frontier of unresolved cases as the live
work queue. *Check:* the residue is the deliverable — an exhaustive search that resolves
100% by machine has found no mathematics, and one that resolves 10% has chosen the wrong
class. Tune the complexity bound so the machines clear most of it and the remainder is
small enough for humans. *Second check:* machine-checked output is what permits contribution
without review capacity; without a verifier, this move does not scale.

---

## Move catalogue

The (f) rules, deduplicated and grouped. These are the file's actual output.

**A. Weaken the target — deliberately, and along a named axis.**
- A1. Weaken the *quantifier*: all → almost all (3).
- A2. Weaken the *conclusion*: bounded → almost bounded, exact → asymptotic (3, 5).
- A3. Weaken the *parameter range*: all n → all large n, accepting ineffectivity (5).
- A4. Weaken the *hypothesis* instead of the conclusion: find the averaged or logarithmic
  version of the conjecture your proof actually consumes (2).
- A5. Weaken the *ambient problem*: prove it for a perturbed equation that keeps every
  property your method exploits (4).
- *Meta-rule:* before attacking T, enumerate its weakenings and check which known barriers
  each escapes. Tao's 2011 Collatz no-go blocks the full conjecture and not the
  almost-all version, and he wrote both.

**B. Change the measuring apparatus.**
- B1. Change the *measure* to one the dynamics preserves, so local results iterate (3).
- B2. Change the *ambient measure* so a sparse set becomes dense, then apply a density
  theorem relatively (1).
- B3. Change the *size functional* to one with a chain rule — entropy for cardinality (6, 8).

**C. Import from an adjacent field, preferably as a person.**
- C1. Named imports observed: ergodic theory → combinatorics (1, 10); information theory →
  additive combinatorics and extremal set theory (2, 6, 8); probability and potential theory
  → complex analysis (5); PDE invariant-measure methods → number theory (3); computer
  architecture and computability → PDE and tiling (4, 9); numerical optimisation →
  analytic number theory (7); contact geometry → fluids (4, downstream).
- C2. The reliable transport mechanism is *collaboration*, not citation. Ziegler on the
  Gowers-norm papers, Fouvry–Kowalski–Michel–Nelson bringing trace functions into
  Polymath8, Miranda's group taking the fluid computer into contact geometry.
- C3. Old discarded ideas are an adjacent field too. PFR ran on Gowers' entropy approach
  from twenty years earlier. Search the abandoned-attempts literature, including the
  collaborators' own.

**D. Prove the barrier.**
- D1. When attempts fail, characterise what they share, then construct an object satisfying
  that characterisation for which the theorem is false (4).
- D2. When an encoding fails, prove a rigidity theorem saying why — it names the next
  encoding to try (9).
- D3. Score a no-go as progress. It prunes, and here it navigated.
- D4. Probe the boundary from the positive side too: the 2009 log-supercritical regularity
  result measured exactly how far energy methods reach (4).

**E. Construct, don't just seek.**
- E1. Show the constraint language encodes boolean logic plus a counter, build a library of
  reusable encodable properties, then program the counterexample (9).
- E2. Verify closure under composition first; disconnected sub-languages are the failure mode.
- E3. Accept grotesque parameters. The tiling dimension is unoptimised and enormous, and
  existence was the point.

**F. Decompose and publish partially.**
- F1. Name the gaps as standalone conjectures and publish conditionally; discharge them
  later, upgrading everything downstream at once (10).
- F2. Modularise into components with a published interface so they improve in parallel (7).
- F3. Expose numeric parameters and maintain a live leaderboard so gains compose (7).
- F4. **Fund the orthogonal branch.** Monotone improvement on a fixed architecture has a
  ceiling; a structurally different attack can leapfrog the whole ladder from a weaker
  start. This is Polymath8's real lesson (7).

**G. Rewrite and mine other people's proofs.**
- G1. Find the formalism where the key inequality becomes an identity, and rewrite (8).
- G2. Extract the reusable lemma from the middle and test it on unrelated problems — the
  spread lemma outlived its sunflower application (8).
- G3. Expect a cascade: each rewrite exposes slack for the next. Four steps in thirteen
  months (8).

**H. Mechanise, and make the machine's output checkable.**
- H1. Enumerate an exhaustive universe of shallow questions, automate the bulk, and treat
  the residue as the deliverable (11).
- H2. Machine-checked output removes trust as a prerequisite, which is what lets strangers
  contribute (6, 11).
- H3. Formalising a finished proof is parallelisable at near-zero coordination cost: three
  weeks, ~25 strangers, 5% of the code from the author (6).
- H4. Computation settles *instances*, not conjectures. The 13 GB SAT certificate resolved
  one value of C and did not generalise (2).

---

## Ladder statistics

How long each program ran and how many rungs preceded the result. This is the table to
consult when budgeting a run.

| Result | Problem open | Tao's own program | Prior partial results | Preceded by an explicit no-go? |
|---|---|---|---|---|
| Green–Tao | ~68 yr | ~2 yr | 3 (van der Corput, Heath-Brown, Green 2005) | No |
| Erdős discrepancy | ~83 yr | 5.5 yr (Polymath5 → solve) | 3 (Polymath5 reduction, SAT C=2, Matomäki–Radziwiłł) | No |
| Collatz | ~82 yr | 8 yr (2011 no-go → 2019) | 5 (Terras, Everett, Allouche, Korec, Krasikov–Lagarias) | **Yes — his own** |
| Navier–Stokes barrier | 14 yr (Clay) | 7 yr (2007 → 2014) | 3 (2007 diagnosis, 2007 quantitative, 2009 positive probe) | Was itself the no-go |
| Sendov | 61 yr | ~1 yr | 8 (4 degree checks, 4 structural ranges) | No |
| PFR | ~24 yr | ~5 mo (Jun–Nov 2023) | 2 (Ruzsa/Freiman exponential, Sanders 2012) | No |
| Prime gaps | ~100 yr | 13 mo | ~20 recorded bound improvements | Yes (GEH sieve barrier at 6) |
| Sunflower | 59 yr | ~1 mo (exposition) | 2 in 59 yr (Kostochka, Naslund–Sawin) | No |
| Periodic tiling | 26–35 yr | ~2 yr | 2 papers, both no-gos | **Yes — two, navigational** |
| Inverse Gowers | ~4 yr conditional | ~6 yr | chain of conditional papers | No |
| Equational Theories | new | months | infrastructural (PFR) | No |

Readings for an automated agent:

- **Median prior-partial-result count is 3.** A frontier with fewer than three established
  weaker statements is early; a frontier with twenty (prime gaps) is an optimisation
  problem, and the winning move there was to leave the ladder.
- **Two of eleven were preceded by an explicit no-go, and one *was* the no-go.** Both
  navigational cases (Collatz, tiling) had the barrier written by the same author who later
  went around it. Barriers are worth generating on your own frontier, not just reading.
- **Program length has no relation to problem age.** An 83-year-old problem took 5.5 years;
  a 59-year-old one took a month of rewriting. Age predicts nothing about tractability;
  the arrival of an external tool (Matomäki–Radziwiłł, ALWZ) predicts a great deal.
- **Computation was decisive in exactly one case (prime gaps) and decorative in most.**
  Where it mattered it was the endgame of an already-parameterised problem. Reaching for
  a computation before the problem is parameterised is the error to avoid.
- **The two fastest results reused someone else's fresh output** — Tao's sunflower rewrite
  (11 months after ALWZ) and PFR's revival of Gowers' 20-year-old entropy idea. Monitoring
  adjacent output beats attacking a cold frontier.

---

## Sources

**1. Green–Tao.** arxiv.org/abs/math/0404188 · en.wikipedia.org/wiki/Green%E2%80%93Tao_theorem ·
arxiv.org/abs/1403.2957 (Conlon–Fox–Zhao)

**2. Erdős discrepancy.** terrytao.wordpress.com/2015/09/11/the-erdos-discrepancy-problem-via-the-elliott-conjecture/ ·
terrytao.wordpress.com/2015/09/18/the-logarithmically-averaged-chowla-and-elliott-conjectures-for-two-point-correlations-the-erdos-discrepancy-problem/ ·
arxiv.org/abs/1509.05363 · arxiv.org/abs/1402.2184 (Konev–Lisitsa) ·
gowers.wordpress.com/2015/09/20/edp28-problem-solved-by-terence-tao/ ·
michaelnielsen.org/polymath/index.php?title=The_Erd%C5%91s_discrepancy_problem

**3. Collatz.** terrytao.wordpress.com/2019/09/10/almost-all-collatz-orbits-attain-almost-bounded-values/ ·
arxiv.org/abs/1909.03562 · terrytao.wordpress.com/2011/08/25/the-collatz-conjecture-littlewood-offord-theory-and-powers-of-2-and-3/ ·
quantamagazine.org/mathematician-terence-tao-and-the-collatz-conjecture-20191211/ ·
link.springer.com/article/10.1007/s11227-020-03368-x (Barina)

**4. Navier–Stokes.** arxiv.org/abs/1402.0290 ·
terrytao.wordpress.com/2014/02/04/finite-time-blowup-for-an-averaged-three-dimensional-navier-stokes-equation/ ·
terrytao.wordpress.com/2007/03/18/why-global-regularity-for-navier-stokes-is-hard/ ·
arxiv.org/abs/0906.3070 · terrytao.wordpress.com/2016/02/01/finite-time-blowup-for-an-euler-type-equation-in-vorticity-stream-form/ ·
quantamagazine.org/a-fluid-new-path-in-grand-math-challenge-20140224/ ·
arxiv.org/abs/2012.12828 · pnas.org/doi/10.1073/pnas.2026818118

**5. Sendov.** arxiv.org/abs/2012.04125 ·
terrytao.wordpress.com/2020/12/08/sendovs-conjecture-for-sufficiently-high-degree-polynomials/ ·
projecteuclid.org/journals/acta-mathematica/volume-229/issue-2/ ·
en.wikipedia.org/wiki/Sendov's_conjecture

**6. PFR.** arxiv.org/abs/2311.05762 · terrytao.wordpress.com/2023/11/13/on-a-conjecture-of-marton/ ·
terrytao.wordpress.com/2023/11/18/formalizing-the-proof-of-pfr-in-lean4-using-blueprint-a-short-tour/ ·
github.com/teorth/pfr · teorth.github.io/pfr/blueprint · mathstodon.xyz/@tao/111526765350663641 ·
quantamagazine.org/a-team-of-math-proves-a-critical-link-between-addition-and-sets-20231206/ ·
theoryofcomputing.org/articles/gs006/gs006.pdf (Sanders, via Lovett)

**7. Prime gaps.** annals.math.princeton.edu (Zhang) · arxiv.org/abs/1402.0811 (Polymath8a) ·
arxiv.org/abs/1407.4897 (Polymath8b) · arxiv.org/pdf/1409.8361 (retrospective) ·
terrytao.wordpress.com/2013/11/19/polymath8b-bounded-intervals-with-many-primes-after-maynard/ ·
terrytao.wordpress.com/2014/06/19/polymath8-wrapping-up/ ·
michaelnielsen.org/polymath/index.php?title=Timeline_of_prime_gap_bounds ·
michaelnielsen.org/polymath/index.php?title=Finding_narrow_admissible_tuples ·
quantamagazine.org/mathematicians-team-up-on-twin-primes-conjecture-20131119/

**8. Sunflower.** arxiv.org/abs/1908.08483 (ALWZ) · arxiv.org/abs/1909.04774 (Rao) ·
terrytao.wordpress.com/2020/07/20/the-sunflower-lemma-via-shannon-entropy/ ·
arxiv.org/abs/2009.09327 (Bell–Chueluecha–Warnke) · arxiv.org/abs/1910.13433 (FKNP) ·
arxiv.org/pdf/2203.17207 (Park–Pham) · isa-afp.org/entries/Sunflowers.html ·
quantamagazine.org/mathematicians-begin-to-tame-wild-sunflower-problem-20191021/

**9. Periodic tiling.** arxiv.org/abs/2211.15847 · arxiv.org/abs/2209.08451 ·
arxiv.org/abs/2010.03254 · arxiv.org/abs/2108.07902 ·
terrytao.wordpress.com/2022/09/19/a-counterexample-to-the-periodic-tiling-conjecture/ ·
terrytao.wordpress.com/2022/11/29/a-counterexample-to-the-periodic-tiling-conjecture/ ·
terrytao.wordpress.com/2021/08/19/undecidable-translational-tilings-with-only-two-tiles-or-one-nonabelian-tile/ ·
terrytao.wordpress.com/2020/10/08/the-structure-of-translational-tilings-in-zd/ ·
quantamagazine.org/nasty-geometry-breaks-decades-old-tiling-conjecture-20221215/

**10–11. [UNVERIFIED]** Green–Tao *Linear equations in primes*; Green–Tao–Ziegler inverse
conjecture; Tao–Ziegler polynomial progressions; teorth/equational_theories and its
blueprint; 2025 AlphaEvolve and Erdős-problems-database activity. Identifiers and dates in
these two entries were not confirmed against live sources during this pass.
