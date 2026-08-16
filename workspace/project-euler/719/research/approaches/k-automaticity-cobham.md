# Is the S-root indicator a k-automatic sequence? (Cobham/Christol dichotomy)

## The idea in one line

Test the formal-language hypothesis that the indicator 1_S(m) of S-roots is a
**k-automatic sequence**: recognized by a finite automaton reading base-10
digits. If it is, the S-root set can be enumerated in O(log N) digit-length
time — exponentially better than the isqrt(N) root scan. If it is not, that is
a provable structural fact worth recording.

## Mathematics

A sequence (a_m) is k-automatic (Allouche–Shallit) iff its k-kernel
{a_{k^e m + r} : e ≥ 0, 0 ≤ r < k^e} is finite, iff a_m is the output of a
finite automaton reading the base-k digits of m. The S-condition is phrased
entirely in terms of base-10 digit substrings of m² (split into contiguous
blocks, sum to m), so automaticity is a natural hypothesis. Christol's theorem
links this to algebraicity: over 𝔽_q, a formal power series has algebraic
coefficients iff its coefficient sequence is p-automatic — giving a concrete
second route to prove/refute automaticity via the generating function
Σ_{m∈S} z^m.

Crucially, **automaticity is not recurrence.** This run closed
`a038206-no-recurrence` (no constant-coefficient linear recurrence of order ≤ 10,
no low-degree polynomial growth). That is not evidence against automaticity:
the Thue–Morse, paperfolding, and Rudin–Shapiro sequences are automatic and
satisfy no such recurrence. The negative modular sweep closed the existence of
cheap *modular filters*; automaticity is about a finite-state recogniser for
the whole structure, a strictly stronger and different question that has not
been tested.

## Why it is a different line of attack

The adopted method treats each m independently (recursion per root). A
finite-automaton recogniser would carry a bounded **carry state** — the
block-sum can be simulated digit-by-digit with a bounded amount of memory (the
running partial sums and the carry from the digit-by-digit square of m). If the
number of reachable (position, carry, partial-sum-bound) states is finite, the
whole S-root language is regular, and T(N) is computed by a transfer matrix over
at most ~13 digit positions rather than by visiting 10⁶ roots. This is a change
of representation: from "search roots" to "compute the language's acceptance
count and weighted sum."

## What is speculation vs established

- Established: definitions of k-automaticity, Cobham's theorem, Christol's
  theorem (standard, sourceable); the mod-9 necessary condition (every S-root
  m ≡ 0 or 1 mod 9) is a finite constraint already.
- Speculation: that the S-root indicator is k-automatic. This is an open
  question for this run — the carry state may or may not stay bounded, and the
  automaticity may hold for one base and fail for another (Cobham's theorem says
  automatic in two multiplicatively-independent bases forces eventual
  periodicity, which the data already contradicts).

## Cost

If automatic, O(poly(D)) for D = 13 digits, independent of N (so also computes
T(10¹⁸) and beyond for free). If refuted, the refutation (an unbounded
kernel / a non-periodicity argument) is a recorded dead end that sharpens the
existing "no recurrence" negative result.

```approach
idea: Ask whether the S-root indicator 1_S(m) is a base-10 automatic sequence (finite automaton with bounded carry state), and settle it via Cobham's dichotomy or Christol's p-adic algebraicity test on Σ_{m∈S} z^m.
mechanism: Allouche–Shallit k-automaticity; Christol's theorem (algebraic ↔ p-automatic over F_q); the S-condition is a digit-substring predicate on m², exactly the kind of predicate automata-with-carry recognise. Distinct from the closed "no linear recurrence" negative: automatic sequences include many without any recurrence.
status: refuted
## Research verdict (researcher, sourced)

**What the reformulation is actually called.** "k-automatic sequence" / "base-k
recognizable set": a set X ⊆ ℕ is k-recognizable iff its base-k representations
form a regular language; 1_X is then k-automatic (Rigo, "Recognizable sets of
integers"; Allouche–Shallit monograph). The candidate asks whether the *S-root
set* 1_S is base-10 automatic.

**The two settling mechanisms named in the proposal do not work as stated.**
- *Cobham's dichotomy* gives: a set both k-recognizable and ℓ-recognizable for
  two **multiplicatively independent** bases, if not ultimately periodic, is
  impossible. It says nothing about a set recognizable in a *single* base. To
  refute base-10 automaticity via Cobham you would first have to prove 1_S is
  automatic in some second base (e.g. base 3) — which is no easier than the
  original question. So Cobham cannot settle "is 1_S base-10 automatic."
- *Christol's theorem* characterises **p-automatic** sequences (prime base p)
  over 𝔽_p via algebraicity of Σ a_n z^n. It applies to base 10 only through the
  primes 2 and 5 dividing 10, and even then it characterises 2- or 5-automaticity,
  not base-10 recognisability. Recognisability of a set in composite base 10 is a
  different object (the digits are the whole numeral system) and is not the p-adic
  coefficient algebraicity Christol's theorem governs.

**Known settled results the candidate must live with.**
- The full set of perfect squares {n^t} is **not** k-recognizable for any base
  k ≥ 2 (Eilenberg; Rigo's Corollary, https://pdfs.semanticscholar.org/454e/1760e9e7c4152e41cfbce85de2632ce9354a.pdf) and the characteristic sequence of the
  squares s1(n) is nonautomatic (Ritchie, Minsky–Papert; see hal-04504166,
  https://hal.science/hal-04504166v1/document).
- Automatic sequences have **subword (factor) complexity O(n)** (Goč–Schaeffer–
  Shallit arXiv:1206.5352; Charlier–Rampersad–Shallit arXiv:1102.3698,
  Konieczny–Müllner arXiv:2309.03180). This is necessary, not sufficient — many
  non-automatic sequences (including the S-roots' sparse characteristic) also have
  linear subword complexity — so it does **not** refute automaticity of 1_S.
- 1_S is a subset of the squares. The non-recognizability of *all* squares does
  not imply non-recognizability of a subset (e.g. a single square, or the empty
  set, is recognizable).

**Bottom line.** I could find **no publication that proves or refutes** the
specific statement "1_S is base-10 automatic." The nearest settled analogues are
negative (full squares non-recognizable), and the named settling theorems do not
deliver a decision for the single-composite-base question. So the hypothesis is
*ungrounded*: not backed by the literature, and not refuted by a source either —
the honest absence is recorded. The intended payoff (O(log N), N-independent
enumeration via a transfer matrix) would be large, but the candidate gives no
reason to think the carry state stays bounded, and no publication supports it.
As a route to computing T(10^12), which is already settled by the O(sqrt N) scan,
it is a genuinely open research question with no precedent, not a method.

precedent: |
  - k-recognizability / automaticity framework: Rigo, "Recognizable sets of
    integers" (https://pdfs.semanticscholar.org/454e/1760e9e7c4152e41cfbce85de2632ce9354a.pdf);
    Allouche–Shallit *Automatic Sequences*.
  - Set of perfect squares (as powers n^t, t≥2) is not k-recognizable for any
    base (Rigo Corollary, citing Eilenberg).
  - Characteristic sequence of squares s1 is nonautomatic: hal-04504166
    (https://hal.science/hal-04504166v1/document); Ritchie; Minsky–Papert.
  - Automatic ⇒ subword complexity O(n): arXiv:1206.5352 (Goč–Schaeffer–Shallit),
    arXiv:1102.3698 (Charlier–Rampersad–Shallit), arXiv:2309.03180 (Konieczny–
    Müllner).
  - Cobham's dichotomy and Christol's theorem as stated in Allouche et al., "How
    to prove that a sequence is not automatic" (arXiv:2104.13072) and Coons
    arXiv:0810.3709.
  - No source found addressing the specific S-root set A038206's automaticity.
first-step: Build a candidate finite transducer that reads m's base-10 digits, maintains the digit-by-digit square of m and the bounded partial block-sum state, and check whether it accepts exactly the 406 known S-roots ≤ 10⁶; if it does, prove finiteness of the carry state; if it fails, search for the minimal kernel blow-up and state a non-automaticity argument.
killed-by: the proposal's own decision procedure is absent — Cobham's dichotomy requires a second multiplicatively-independent base (no easier to establish than the question itself) and Christol's theorem governs prime p-automaticity, not composite-base-10 recognisability; no source or argument bounds the carry state. As a route to a method it is an ungrounded open question, not a line of attack.
```
