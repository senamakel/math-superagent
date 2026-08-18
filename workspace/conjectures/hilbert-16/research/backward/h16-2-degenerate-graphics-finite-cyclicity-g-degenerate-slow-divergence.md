# h16-2-degenerate-graphics-finite-cyclicity-g-degenerate-slow-divergence

```skeleton
goal: On the desingularized charts of the family blow-up at the contact point of a normal-form family, the displacement map's derivative is C∞ contact-equivalent to a development whose leading term is the slow divergence integral; wherever that integral is not identically zero, the displacement has at most B zeros with B read off the SDI (DR 2009 Thm 3.1 shape: ≤3 DF1a generic, ≤5 DF2a center, ≤1 under sign conditions). For DI2a concretely: the SDI of family (2.8) on the strip-of-hyperbolas stratum is computed explicitly, its zeros bound the limit cycles on the generic strata, and the strata where it vanishes identically are identified — that list is exactly the input to G-degenerate-pstar-and-center. This is where the zero count is actually obtained: a generic invocation of 'slow divergence machinery' with no computed integral bounds nothing.
implies: bounds the displacement's zeros on the desingularized generic strata — the bulk of the parameter box
next: tool_builder + symbolic_math, today: port the DR 2009 §4 family blow-up (4.1) computation — charts, center manifold (4.5), the SDI — from the DF1a/DF2a family (3.1) to the DI2a family (2.8), exact in sympy over Q; validate the port by reproducing the DF1a/DF2a SDI first (live check against held text DR 2009 §4), capture to code/out/di2a_slow_divergence.captured.txt, and report the vanishing strata explicitly.
status: open
```
