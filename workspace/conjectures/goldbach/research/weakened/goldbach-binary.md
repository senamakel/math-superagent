# Ladder of weakened versions — binary Goldbach

The full-strength goal and the difficulties that make it hard, then the goal
with one difficulty switched off at a time, weakest (most conveniences assumed)
first. A rung is `settled` only when the run has established it; a rung that
was attacked and failed stays on the ladder with the reason.

The difficulties are named from what the sources actually say, not from the
topic:

- **D-every** — the conjecture is a statement about *every* even n. The
  literature reaches only density / almost-all results: the exceptional set
  E(X) ≪ X^{1−δ}. Best **published** δ = 0.121 (Lu 2010, E(X) < X^{0.879});
  best **claimed** δ = 0.28 (Pintz 2018 preprint, E(X) < X^{0.72}); sharpest
  preprint claim δ = 0.3 (Zhao 2025, E(X) = O(X^{7/10})); all constants
  ineffective. (Pintz's announced δ = 1/3 of 2004, recorded in Kumchev–Tolev
  §1 eq. (1.6), was superseded by his own 2018 X^{0.72}.) Under GRH,
  E(X) ≪ X^{1/2+ε} (Hardy–Littlewood 1924; Pintz 2018 §1, eq. (1.2)). A
  density result is not a proof; this is the obstruction that separates the
  two.
- **D-parity** — the parity problem in sieve theory: sieves can reach
  "at most two prime factors" (Chen's theorem) but cannot conclude "prime." A
  proven structural limitation of sieve methods themselves, not a gap waiting
  on a cleverer sieve (problem.md; Friedlander–Iwaniec 2023).
- **D-minorarc** — uncontrolled minor-arc error in the binary circle method:
  the minor-arc error is not controllable for all n, only for almost all n,
  which is why the circle method yields density results and not a proof
  (problem.md; Helfgott's ternary proof works precisely because three summands
  smooth the minor arcs).
- **D-threshold** — the "sufficiently large" threshold is astronomically
  ineffective. Chen's theorem as classically stated gives no effective
  threshold; the best effective version (Bordignon–Johnston–Starichkova 2022,
  Thm 3) requires n > exp(exp(32.7)) ≈ 10^{10^{14}}, and the unconditional
  "prime + at most e^{29.3} primes" version (Thm 5) is what covers the gap
  below it. The conjecture is open in the entire interval
  (4×10^{18}, exp(exp(32.7))).
- **D-bridge** — no algebraic identity bridges multiplicative primality and the
  additive equation p+q=n; the structural reason the above all fail.

```ladder
goal: Every even integer n > 2 is the sum of two primes (binary/strong Goldbach).
difficulties: D-every, D-parity, D-minorarc, D-threshold, D-bridge
status: open
```

---

```rung
id: R-verified-range
statement: Every even integer n with 4 ≤ n ≤ 4×10^18 is the sum of two primes.
off: D-every, D-parity, D-minorarc, D-threshold, D-bridge
stance: settled
merge: This is not a weakening the run produced; it is the published
  computational verification of Oliveira e Silva, Herzog and Pardi (2014),
  verified to 4×10^18 and double-checked to 4×10^17 (research/sources/
  oliveira-e-silva-...). It switches off every difficulty by fiat: the range
  is finite, so "every n" is a finite check; sieves and the circle method are
  not invoked; the threshold is the verification bound itself; no bridge is
  needed because primality is tested directly. The next move up is to push this
  bound, which is a computational rung (see R-push-verification), not a
  theoretical one. Recorded as settled so the run does not re-prove it.
```

---

```rung
id: R-push-verification
statement: Every even integer n with 4 ≤ n ≤ B is the sum of two primes, for
  some explicit B > 4×10^18 stated by the run.
off: D-every, D-parity, D-minorarc, D-threshold, D-bridge
stance: open
merge: Same difficulty profile as R-verified-range — a finite range, checked
  directly — but with the bound pushed past the literature's 4×10^18. The
  forward loop attacks this with tool_builder's exact checker (a segmented
  sieve plus Goldbach-partition search, reproducing the Oliveira e Silva
  method) and reproduces 4×10^18 before trusting anything beyond it. This is a
  real, reportable result (GOAL.md completion criterion 2: a lower
  verification bound pushed past the record) and it is the rung an attempt
  could settle today. Turning the next difficulty on means leaving the finite
  range: the first theoretical rung is R-density-delta.
```

---

```rung
id: R-density-delta
statement: There exists an absolute δ > 0 such that the number E(X) of even
  integers n ≤ X not representable as a sum of two primes satisfies
  E(X) ≪ X^{1−δ}.
off: D-every
stance: settled
merge: This is the Montgomery–Vaughan (1975) exceptional-set theorem, with the
  best published exponent δ = 0.121 (Lu 2010, E(X) < X^{0.879}); Pintz 2018
  (preprint) claims δ = 0.28 (E < X^{0.72}), Zhao 2025 (preprint) claims
  δ = 0.3 (E = O(X^{7/10})), all ineffective. It switches off only D-every: it
  is an almost-all statement, not an every-n statement, and every other
  difficulty (parity, minor arcs, threshold, bridge) is still live in its
  proof. It is recorded settled because the run's library establishes it, not
  because the run proved it. The next move up is to improve δ itself
  (R-sharpen-delta), which is the genuinely attackable theoretical rung.
```

---

```rung
id: R-sharpen-delta
statement: The exceptional-set bound E(X) ≪ X^{1−δ} holds with some explicit
  δ > 1/3, improving on Pintz's 2004 exponent.
off: D-every
stance: open
merge: Same difficulty profile as R-density-delta (still almost-all, so
  D-every off; everything else live) but asks for a genuine improvement to the
  known exponent. GOAL.md names this explicitly as a real reportable result
  (criterion 2: a better δ in the Montgomery–Vaughan exponent). The forward
  loop attacks it through the circle method's minor-arc estimates — this is
  where D-minorarc starts to bite, because any improvement to δ requires
  tighter minor-arc control than the current literature has. The merge to the
  next rung is: keep the improved minor-arc control and ask whether it can be
  made uniform in n, which is R-conditional-grh.
```

---

```rung
id: R-conditional-grh
statement: Assuming the Generalized Riemann Hypothesis, E(X) ≪ X^{1/2+ε} for
  every ε > 0; equivalently, under GRH, all but O(X^{1/2+ε}) even n ≤ X are a
  sum of two primes.
off: D-every
stance: settled
merge: This is the Hardy–Littlewood (1924) conditional estimate, still the best
  conditional result on GRH (Pintz 2018, §1 eq. (1.2); Goldston's
  log-power refinement is the only improvement). Recorded settled from the
  library. It switches off only D-every and is conditional on GRH, so it is
  weaker than R-density-delta in the sense of resting on an unproved
  hypothesis. The interesting merge is not upward to a stronger density result
  but sideways: under GRH, can the *unconditional* "every n" be reached for
  some restricted class? That is R-restricted-class. The new Bhowmik–Grimmelt
  survey (research/summaries/pintz-exceptional-set-goldbach-problem-survey-explicit-major-arcs-arxiv-2607.27282.md)
  gives a fully explicit major-arc formula usable here.
```

---

```rung
id: R-restricted-class
statement: There exists a non-trivial arithmetic-progression or
  multiplicative-constraint class C of even integers, stated exactly, such that
  every n in C is the sum of two primes (with the class and the proof's
  hypotheses both explicit).
off: D-every
stance: open
merge: This switches off D-every *for the class C only* — it is an every-n
  statement, but over a restricted set rather than all even n. It is the
  highest-value result the run can aim for (GOAL.md criterion 1). The
  obstruction that bites here is D-parity: any sieve-based proof for a class
  hits the parity problem the moment it tries to conclude "prime" rather than
  "prime or semiprime," so the class must be chosen so that the parity barrier
  is genuinely evaded (e.g. a class where a bilinear-form / Type I/II
  decomposition gives an asymptotic, not just upper/lower bounds). New sources
  this cycle give almost-all restricted-class results: Salmensuu 2022 (both
  summands in APs mod r, r ≤ N^(1/2), three layers of "almost all"),
  Cumberbatch 2024 (digit-restricted sets, power saving in |A(X)|), Akeno 2026
  (level of distribution 1/6 for Goldbach primes). None is an every-n statement
  for its class; each is a density result inside a restricted class. The merge
  to the next rung is to enlarge C toward all even n, which is where
  D-minorarc and D-bridge re-enter.
```

---

```rung
id: R-chen-effective
statement: Every even integer n > exp(exp(32.7)) is the sum of a prime and a
  number with at most two prime factors (effective Chen theorem, with the
  threshold made explicit).
off: D-threshold
stance: settled
merge: This is Bordignon–Johnston–Starichkova (2022), Thm 3, with the
  effective threshold exp(exp(32.7)) and the square-free refinement of
  Corollary 4. It switches off D-threshold (the threshold is now explicit)
  but leaves D-parity fully on: the second summand is "prime or semiprime,"
  not "prime." Recorded settled from the library. The merge upward is the
  obstruction itself: to reach "prime" from "prime or semiprime" one must
  break D-parity, which no known technique does. This rung is on the ladder
  precisely to mark where the parity barrier sits.
```

---

```rung
id: R-chen-all-n
statement: Every even integer n ≥ 4 is the sum of a prime and a number with at
  most e^{29.3} prime factors.
off: D-threshold
stance: settled
merge: Bordignon–Johnston–Starichkova (2022), Thm 5 — the effective
  Rényi-type result covering the gap below the Chen threshold, at the cost of
  allowing up to e^{29.3} prime factors in the second summand. Switches off
  D-threshold (all n ≥ 4) but leaves D-parity on in an extreme form: the
  second summand is far from prime. Recorded settled from the library. The
  merge is to reduce the number of allowed prime factors toward 1, which is
  the same parity barrier as R-chen-effective, approached from below.
```

---

```rung
id: R-siegel-zero-implies-goldbach
statement: If a real Siegel zero exists for a primitive quadratic character
  χ (mod q) (in the precise sense of Matomäki–Merikoski Cor. 1.2), then a
  weak form of the Goldbach asymptotic holds for even h ≡ 0 (mod q) in
  [q^{10}, q^{η^{99/100}}], and in particular L(s, χ) has no exceptional zero
  in that range.
off: D-every, D-bridge
stance: open
merge: This is Matomäki–Merikoski (2022), Cor. 1.2 — a conditional link
  between Siegel zeros and Goldbach: a weak Goldbach-type lower bound on the
  weighted representation sum rules out an exceptional zero. It switches off
  D-every (it is an asymptotic for a range of h, not every n) and D-bridge
  (the Siegel zero, if it exists, *is* the bridge between the multiplicative
  and additive sides). The obstruction that bites is that the implication runs
  the wrong way for a proof of Goldbach: it says "Goldbach ⇒ no Siegel zero,"
  not "Siegel zero ⇒ Goldbach for every n." The merge is to ask whether the
  contrapositive can be sharpened into a positive density statement, which
  re-enters D-every and D-minorarc.
```

---

```rung
id: R-minimal-counterexample
statement: Any minimal counterexample n (the least even n > 2 not a sum of two
  primes) satisfies an explicit finite list of necessary conditions — e.g.
  n > 4×10^18, n ≡ 0 (mod 2), n not in any settled restricted class C, and
  n − p composite for every prime p < n (so n lies in the "exceptional set" at
  its own scale).
off: D-parity, D-minorarc, D-bridge
stance: open
merge: A structural / reduction rung (GOAL.md criterion 4): it does not prove
  the conjecture, it constrains where a counterexample can live. It switches
  off D-parity, D-minorarc and D-bridge by not attempting to count
  representations — it only records necessary conditions a counterexample must
  satisfy, drawing on R-verified-range (n > 4×10^18) and any settled
  R-restricted-class. The obstruction that bites is D-every itself: the
  conditions are necessary but not sufficient, so they cannot rule out a
  counterexample, only narrow where it would be. The merge is to add a
  condition strong enough that the narrowed set is empty, which is exactly
  what no known technique does.
```

---

The rung to attack next is **R-push-verification**: it is the weakest rung an
attempt can settle today (a finite range, checked directly, with the bound
pushed past 4×10^18), it is the rung the run's own computation can produce, and
it is a genuine reportable result under GOAL.md criterion 2.

The difficulty I expect to actually bite is **D-parity**. The rung that is
most informative about where the real obstruction lives is **R-chen-effective**:
it is settled, but it is settled at "prime or semiprime," and the single step
from there to "prime" is the parity barrier, which is the difficulty the whole
ladder is climbing toward and the one no rung above it has switched off.
