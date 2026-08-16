# The fold's image is the algebraic normal form of the window — Reed–Muller / algebraic-immunity route

```approach
idea: >
  Recast SUPPLY as a statement about the algebraic normal form (ANF) of the
  prime-gap window. Over F2 the submask-XOR map is the Möbius transform, which
  is self-inverse; the same map is the Reed–Muller transform, whose values are
  exactly the ANF coefficients of a Boolean function. Hence ν₂(n) = wt(Φ_n h)
  equals the number of nonzero ANF monomials of the Boolean function τ_n
  (the reversed ±1 gap-parity window) on ⌈log₂ n⌉ bits. SUPPLY says: the
  prime window has a linear number of ANF monomials (its Reed–Muller spectrum
  is spread), for every large n.

mechanism: >
  The identification is the known involution (claim supply-fold-submask-zeta-involution:
  T(d) = XOR_{s⊆d} τ[s] is the F2 zeta transform and is self-inverse), reread as
  coding theory: the coefficients of the algebraic normal form of a Boolean
  function f on k bits are exactly XOR_{s⊆d} f(s) (the Möbius/Reed–Muller
  transform). So ν₂(n) is the Hamming weight of the window's Reed–Muller
  spectrum. This changes the question from "is h complicated?" (the five closed
  doors, all refuted) to "is the window's ANF support large?", which is a
  question about the Reed–Muller code RM(k, k) and its dual via the MacWilliams
  transform, about algebraic immunity / annihilators, and about the
  uncertainty principle (Donoho–Stark is already a claim in this workspace:
  |supp f||supp f̂| ≥ |G|, with equality characterised by subgroup indicators).
  A putative counterexample (ν₂(n)/n → 0 on a set) places the windows in a
  coset of a low-weight Reed–Muller spectrum, an object with a known, rigid
  classification. The primes' arithmetic enters only as the (priced) hypothesis
  that the window's Reed–Muller spectrum is not concentrated — a spectral/
  valuation condition, not a complexity condition on h, so it does not reopen
  the closed family "h is complicated enough". Thue–Morse and all-ones are the
  two negative controls whose ANF support is sparse, exactly matching their
  measured sublinear ν₂.

status: refuted

killed-by: >
  The identity is real and is kept as a lemma (T(n,d) = a_d is the F2
  Moebius/Reed-Muller transform), but the *engine* the candidate mounted on it —
  Reed-Muller weight enumeration / MacWilliams on ANF support of a sliding window
  — is the open RM weight-spectrum problem (Carlet 2023/24), not an applicable
  bound. Research verdict: change of language, not of ground. The identity is
  absorbed as the eps_d = (-1)^{a_d} step inside the adopted line
  `fold-second-moment-krawtchouk`, whose engine is the Delsarte distance
  distribution / Krawtchouk transform of the row code — a problem the literature
  does support — rather than the RM weight spectrum. As a standalone route: refuted.

## Research verdict (grounding check)

**The reformulation is real, named, and reproduces the Scholze gate.** `a_d =
⊕_{x ⊆ d} g(x)` is exactly the F₂ Möbius / Zhegalkin transform computing the
algebraic normal form coefficient of a Boolean function — confirmed by the
cryptanalysis and coding literature (`b_(a1..an) = ⊕_{x_i ≤ a_i} f(x)`;
the F₂ Möbius transform is a self-inverse bijection between truth table and
ANF). The identity is one substitution `x = d−o` mapping submasks of `d`
bijectively: `T(n,d) = ⊕_{o⊆d} h[n−1−d+o] = a_d`. It reproduces
`supply-fold-submask-zeta-involution` in coding-theoretic language — the gate
(rule 4) passes.

**What it does NOT buy (payoff ungrounded on evidence, not absence).**
- The RM literature bounds *Hamming weight of codewords* (weight spectra of RM
  codes), tied to low algebraic *degree*. Our quantity — the number of nonzero
  ANF coefficients of an *arbitrary sliding window* — is neither low-degree nor
  function-weight; it is ANF-support size. No source found applies RM weight
  enumeration or MacWilliams to a sliding-window ANF-support lower bound.
- The RM weight spectrum is itself a hard open problem (Carlet 2023/2024 states
  this), so this hands the problem to a category that is not easier.
- No theorem found lower-bounds ANF-support of a general window without an input
  hypothesis; the routes that force it large are the five refuted "h is
  complicated enough" inputs. The identity is a change of *language*; the ground
  changes only if the window is shown to sit in a special RM-subcode coset —
  which is exactly the unproved arithmetic claim.

Sources: Springer *Probabilistic estimation of the algebraic degree of Boolean
functions*; arXiv:2004.11146 (Barbier–Cheballah–Le Bars, Möbius computation);
Carlet *Identifying codewords in general Reed–Muller codes* (DOI
10.3934/math.2024518); Carlet–Solé (DOI 10.1016/j.disc.2023.113568); Carlet
*RM(m−5,m)*. Claim ids on disk: `supply-fold-submask-zeta-involution`,
`donoho-stark-finite-abelian-product`, `meshulam-finite-abelian-divisor-bound`
(these uncertainty bounds point the same direction — their extremals are the
closed-door low-weight inputs).

SOURCES AND VERIFICATION CAVEAT (research pass): the identity `T(n,d) = a_d`
is a classical, sourced fact of Boolean-function theory (F₂ Möbius transform
computes ANF coefficients; Springer 10.1007/s12095-023-00660-4; arXiv:2004.11146;
hal-01178356), and it reproduces the already-checked claim
`supply-fold-submask-zeta-involution` by the substitution `x = d−o`. The on-disk
checker `code/out/anf_dictionary_check.py` (asserts `T(n,d)==a_d` for n=3..40
and all-ones ANF support 1) is WRITTEN but NOT YET EXECUTED — no execution tool
in the research role; `code/out/INDEX.md` flags it. So the identification is
held at sourced/dictionary level, not machine-verified. tool_builder must run
the checker (and the first-step's three-route computation) before candidate 1's
payoff is rested on.

SCHOLAR HAND-CHECK (n=4, this pass, no execution tool): for n=4, h=[h0,h1,h2,h3],
g=reversed=[h3,h2,h1,h0]. d=1: T=h2^h3, a_1=g0^g1=h3^h2 — match. d=2: T=h1^h3,
a_2=g0^g2=h3^h1 — match. d=3: T=h0^h1^h2^h3, a_3=g0^g1^g2^g3=h3^h2^h1^h0 —
match. All-ones negative control: all g_i=1, a_d = XOR of 2^{popcount(d)} ones
= 1 iff d=0 else 0, so ANF support = {0}, size 1 — matches nu2=O(1). Confirms
the identity on the smallest nontrivial case; the n=3..40 sweep is still un-run.

first-step: >
  Verify the ANF/Reed–Muller identification mechanically for n = 8..64: compute
  the Möbius transform of the window three independent ways (brute submask-XOR
  oracle, SOS transform, and direct ANF coefficient enumeration), confirm the
  three agree and equal the fold image; then print the ANF support sizes for the
  prime h, Thue–Morse, and all-ones windows, and confirm primes are spread while
  the two controls are sparse. This is the cheapest falsifier of the whole
  route: if the primes' ANF support is NOT spread at small n, the route is dead
  before any number theory is spent.
```
