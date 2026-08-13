```approach
idea: Rule 90 cellular automaton with absorbing boundary — reframe the {0,2}
      region as a Rule 90 (XOR) CA and regeneration as boundary absorption
mechanism: >
  Within the {0,2} region, after halving (dividing by 2), the absolute-difference
  operator reduces to XOR: |a−b|/2 = (a/2) XOR (b/2) when a,b ∈ {0,2}. This is
  Wolfram's Rule 90, the additive linear cellular automaton; the whole {0,2}
  block of the Gilbreath triangle is a Rule-90 evolution from the initial
  bit-string A_1(2), A_1(3), ... (halved), with time = row depth.

  Regeneration is reframed as: the "intruder" values (≥4, halved to ≥2) at the
  boundary of the Rule-90 region get absorbed — reduced to {0,1} (i.e. {0,2}
  after doubling) — by the XOR dynamics. If the absorption time is bounded (a
  function of the intruder value, or uniformly), then regeneration is proved:
  the block only needs to be long enough to absorb the intruders at its edge.

status: refuted
killed-by: >
  (The within-{0,2} Rule-90 identification itself is REAL and grounded — that
  half survives; what is refuted is the approach's proposed mechanism, that a
  bounded boundary-absorption time yields regeneration.) The Rule-90
  identification is sourced — it is exactly the
  run's block-lemma apex result (a leading {0,2} block evolves by XOR/Sierpinski
  of its bit pattern), and CHT 2026 §1 note the same structure explicitly: the
  {0,d}-block with one nonzero entry produces "essentially the pattern of a
  Sierpinski triangle (or of Pascal's triangle modulo 2)". So the "within-{0,2}
  is Rule 90" half is grounded.

  But the ABSORBING-BOUNDARY mechanism with a bounded absorption time is
  exactly what the literature's obstructions refute for the general class:

  (1) CHT Theorem 1.6 isolates long shallow {0,d}-blocks (d>=2) as ONE OF THE
  ONLY TWO obstructions to decay, and Lemma 3.7(iii) proves a {0,d}-valued
  block stays {0,d}-valued in ALL descendants — i.e. an intruder stretch
  PROLONGED within a two-valued set does NOT decrease in magnitude. At the
  halved level an intruder value >=2 is precisely the d>=1 value CHT say can
  persist; there is no uniform absorption-time bound in general.

  (2) Eppstein 2011 builds 2-then-odds sequences with gaps <= f(n) whose right
  edge escapes to non-1 and re-enters 1 infinitely often — so the boundary
  "intruder" can be kept from being absorbed for arbitrarily long, at any block
  length. No B(f(v)) bounded absorption holds in the general class.

  (3) The mechanism's engine is the mod-4 linearization (addition mod 4 = the
  linear non-XOR extension), but that is exactly the parity-only content of CHT
  Lemma 3.10 / Odlyzko §2: it is a linear congruence that never fixes the exact
  {0,2} value (see mod4-pascal-invariant, which is refuted for the same
  reason). Rule 90 is linear over GF(2) and governs ONLY the {0,1} interior;
  once a value >=2 enters, the operator |a-b| is no longer XOR and leaves the
  linear CA regime — Rule-90 theory does not apply to the absorption step that
  regeneration needs.

  Whether the primes' boundary intruders are absorbed within a bounded time is
  EXACTLY the conjecture, not a corollary of Rule-90 dynamics. Nothing in the CA
  literature establishes uniform absorption for 2-then-odds, and Eppstein shows
  it is false in that class; primes can only differ by their special non-
  concentration (CHT two-separated-set hypothesis), which is unproved for
  primes.
precedent: >
  - https://arxiv.org/abs/2607.08712 (CHT §1 Sierpinski/{0,d} note; Lemma 3.7(iii)
    {0,d} propagates in all descendants; Theorem 1.6 long-{0,d}-block obstruction)
  - https://11011110.github.io/blog/2011/02/20/anti-gilbreath-sequences.html
    (Eppstein 2011, arbitrary-delay / infinite-escape of the right edge)
  - research/notes/block_lemma.md (this run's proved apex = Sierpinski/XOR of the
    block's bit pattern)
holding-claims: larger
  odlyzko-block-lemma-exact, odlyzko-mod4-linearization, mod-lift-obstruction,
  anti-gilbreath-construction
falsifies: >
  That a uniform bound B(v) exists on the number of rows to reduce any boundary
  value v>=4 to {0,2} when adjacent to a long-enough {0,2} block, for the class
  of 2-then-odds sequences. CHT Lemma 3.7(iii) (a {0,d} block never decreases)
  and Eppstein (arbitrary escape delay) together refute it.
buy: >
  The Rule-90 (Sierpinski/XOR) structure of the {0,2} interior is real and
  already captured by the proved block lemma. As a route to regeneration it buys
  nothing further: the needed absorption step is nonlinear and is exactly the
  open conjecture; the linear CA theory does not reach it.
first-step (retired): >
  Extracting boundary transitions from depth-1000 data and measuring absorption
  distance would produce only numerical evidence about depth 1000 — it cannot
  establish the uniform bounded-absorption lemma the approach needs, which CHT
  Lemma 3.7(iii) and Eppstein already show is false in the 2-then-odds class.
```

Fenced claim:

```claim
id: rule90-identification-real-absorption-refuted
statement: The {0,2} interior of a Gilbreath row evolves under the halved operator as XOR (= Wolfram Rule 90 = Pascal/Sierpinski mod 2) — this is proved here (block-lemma apex) and confirmed by CHT 2026 §1. But a uniform boundary-absorption bound reducing any intruder v>=4 to {0,2} in B(v) rows does not hold for the 2-then-odds class: CHT Lemma 3.7(iii) shows {0,d}-valued blocks persist in all descendants without decrease, and Eppstein 2011 builds small-gap sequences whose right edge escapes to non-1 and re-enters 1 infinitely often (arbitrary delay).
hypotheses: Gilbreath arrays of 2-then-odds sequences; primes the special case.
holds-here: yes (for the negative/uniform claim); the Rule-90 identification holds universally on {0,2} entries.
status: sourced (Rule-90 structure: this run proved + CHT confirm); the uniform-absorption bound refuted for the general class by CHT Lemma 3.7(iii) and Eppstein.
bearing: the within-block Rule-90 structure is real but regeneration happens AT the nonlinear boundary where Rule-90 does not apply; a bounded absorption time is exactly the unproved conjecture, not a CA corollary.
anchor: research/approaches/rule90-absorbing-boundary.md
```
