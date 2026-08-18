# Bautin (1952), "On the number of limit cycles...", Mat. Sb. 30(72):1, 181-196

<!-- source: https://www.mathnet.ru/php/getFT.phtml?jrnid=sm&paperid=5421&what=fullt&option_lang=eng | Russian full text. Full text: [[bautin-1952-full.pdf.full]]. Claim `h16-bautin-1952-m2equals3-primary`. -->

## What it establishes — the literature boundary M(2) = 3 (Primary source!)

**Theorem.** The maximum number of small-amplitude limit cycles that can appear
from a focus/center equilibrium state of a quadratic system as the coefficients
vary (over ALL coefficient variations) is **3**. A quadratic system (A2) with 3
limit cycles is exhibited.

Note the careful statement: this is the *local* problem — small-amplitude cycles
around a single focus/center under all coefficient changes — NOT the global
H(2) (4 cycles via Shi/Chen-Wang are a *global* bound from separate nests). The
distinction is load-bearing for GOAL step 4.

## The exact machinery (needed to reproduce M(2)=3)

- §1: precise definition of **cyclicity of order k** of the equilibrium:
  (a) there is an ε₀-neighbourhood of the coefficient point and a δ₀-neighbourhood
  of (0,0) containing no system with >k limit cycles in the δ₀-neighbourhood;
  (b) for any smaller ε<ε₀, δ<δ₀, there is a system within ε of the point with
  exactly k limit cycles in the δ-neighbourhood. Conditions: `a₁₀b₀₁−a₀₁b₁₀ > 0`
  and `a₁₀+b₀₁ = 0`.
- §2: reduction under
  `(a₁₀−b₀₁)²+4a₁₀b₀₁ < 0` to the **canonical focus form (II)** in the six
  coefficients λ₁,…,λ₅, where `λ₁=λ₄=λ₅=0` is exactly the center condition
  (P_x+Q_y=0). This is the origin of the run's "five-coefficient chart ring".
- §3: passage to polar coordinates; the radial equation (III) is expanded in
  powers of ρ — the Lyapunov quantities.

This is precisely the machine the run's oracle (GOAL step 4) must reproduce
exactly over Q before trusting anything past it.

## Hypotheses / holds here

Quadratic systems, small-amplitude cycles about a single focus/center. **Holds
here: yes** — this is the boundary the run reproduces before trusting any
Bautin-ideal computation past M(2)=3.

**Evidence class: sourced** (PRIMARY full text now held from mathnet's
full-text PDF; previously recorded as "not openly downloadable").

## Falsifier

A quadratic system with 4 small-amplitude cycles from a single focus would
contradict M(2)=3. None known; M(2)=3 is the standard accepted boundary.

## Bearing / implication

- The six-coefficient canonical focus form and the λ-centre condition are the
  exact chart the run's `verify_lu_core` / Bautin-recurrence Lean files use —
  and the warning from the claim ledger: this chart ring is NOT the full
  six-parameter family, and its L8∉⟨L4,L6⟩ etc. membership facts must not be
  quoted as M(2)=3 evidence either way.
- Reproducing Bautin's M(2)=3 exactly (Lyapunov quantities over Q + the ideal
  they generate) is the declared feasibility-boundary task.
