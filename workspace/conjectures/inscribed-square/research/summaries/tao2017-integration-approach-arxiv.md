# Tao 2017 — An integration approach to the Toeplitz square peg problem

**Source:** Terence Tao, "An integration approach to the Toeplitz square peg problem," Forum of Mathematics, Sigma 5 (2017), e30. DOI: 10.1017/fms.2017.23. arXiv:1611.07441. Full text at [[research/sources/tao2017-integration-approach-arxiv.full.md]].

## What it establishes

**Theorem 1.2 (two Lipschitz graphs, small constant).** Let [t₀,t₁] be an interval and f, g : [t₀,t₁] → R be (1−ε)-Lipschitz functions for some ε > 0, with f(t₀) = g(t₀), f(t₁) = g(t₁), and f(t) < g(t) for all t₀ < t < t₁. Then the Jordan curve Graph_f([t₀,t₁]) ∪ Graph_g([t₀,t₁]) inscribes a square.

The two-graphs class is *not* locally monotone in general: oscillation at the endpoints can be unbounded, so Stromquist's theorem does not directly apply. The method introduces a "conserved integral of motion" built from the signed area ∫_γ y dx under a rectifiable curve (Lemma 3.4: this area equals −|Ω|, the negative Lebesgue measure of the bounded region, hence is nonzero for a simple anticlockwise rectifiable curve).

**The shrinkout obstruction (stated precisely).** The regularity hypotheses in all homological approaches are needed to rule out *arbitrarily small* inscribed or almost-inscribed squares; on rough curves a limiting argument can lose the square to a point. Tao's integrals are designed to be insensitive to small squares.

**Open variants (not solved here):**
- **Conjecture 4.1 (Periodic square peg problem):** for σ₁, σ₂ : R/LZ → Cyl_L simple curves homologous to Graph_{0,L}, disjoint, the union inscribes a square. Tao (2017) reported it open even for piecewise-linear curves. **UPDATE (resolved):** Hugelmeyer, "A Solution to the Periodic Square Peg Problem" (arXiv:2407.20412, 2024) resolves it — full text now in the library (`research/sources/hugelmeyer-2024-periodic-square-peg.full.md`), verified: Theorem 1 (injective continuous f, g : ℝ→ℝ² with f(x+1)=f(x)+(0,1), g(x+1)=g(x)+(0,1), disjoint images ⇒ im(f)∪im(g) contains the four corners of a plane square) is Tao's Conjecture 4.1 with L=1 (general L by scaling). The claim `tao2017-periodic-variant-open` is superseded. **This does NOT settle Toeplitz**: the periodic variant is a separate problem; Tao's Proposition 4.7 gives that Toeplitz (Conjecture 1.1) implies the "no infinitesimal squares" special case Conjecture 4.6, not conversely.
- Conjecture 4.6 (special case with no infinitesimal squares) and Proposition 4.7: Conjecture 1.1 (Toeplitz) implies Conjecture 4.6; so the periodic problem is a *reformulation family*: a proof of the periodic conjecture would settle Toeplitz.
- Lemma 4.3: disjoint graphs of C-Lipschitz functions with C < tan(3π/8) = 1+√2 do not inscribe infinitesimal squares — the 1+√2 threshold appears here first in Tao.

## Why it matters here

- The two-graphs class is one of ROOT.md's three restricted classes; Rifford 2021 and Greene–Lobb 2024 extend it to Lipschitz = 1 and < 1+√2 respectively.
- The periodic reformulation (Conjecture 4.1) and the "no infinitesimal squares" special case are the cleanest published statement of what a shrinkout-free argument must prove.
- Lemma 4.3 shows the 1+√2 threshold has an elementary geometric source — useful for a Lean formalization of the nondegeneracy step.

## Claims

```claim
id: tao2017-two-lipschitz-graphs
statement: If f, g : [t0, t1] → R agree at endpoints, f(t) < g(t) on the interior, and both have Lipschitz constant < 1, then the Jordan curve formed by the union of their graphs inscribes a square.
status: asserted-by-source
evidence: Tao 2017, Theorem 1.2 (Forum Math. Sigma 5, e30)
holds-here: yes — one of the three restricted classes ROOT.md names; the curve need not be locally monotone
falsifies: a pair of (1−ε)-Lipschitz functions agreeing at endpoints with no inscribed square
anchor: research/sources/tao2017-integration-approach-arxiv.full.md
```

```claim
id: tao2017-shrinkout-difficulty
statement: The obstruction to extending homological proofs to rough curves is that inscribed or almost-inscribed squares may be arbitrarily small, so limiting arguments can lose the square (shrinkout); Tao's integrals are designed to be insensitive to small squares.
status: asserted-by-source
evidence: Tao 2017, Introduction and §4 (the periodic variant, insensitive to small squares)
holds-here: yes — this is failure point 3 of problem.md, named precisely
falsifies: a homological proof for rough curves that does not control square size at any scale
anchor: research/sources/tao2017-integration-approach-arxiv.full.md
```

```claim
id: tao2017-periodic-variant-resolved
statement: The periodic variant of the square peg problem (two disjoint periodic curves in the cylinder inscribing a square, insensitive to small squares) — open per Tao 2017 Conjecture 4.1 — is RESOLVED by Hugelmeyer 2024 (arXiv:2407.20412): injective continuous f, g : ℝ→ℝ² with f(x+1)=f(x)+(0,1), g(x+1)=g(x)+(0,1), disjoint images, admit four points in im(f)∪im(g) forming a plane square. This does NOT settle Toeplitz: the periodic problem is a separate statement.
status: asserted-by-source (Hugelmeyer 2024, arXiv preprint, full text in library)
evidence: Hugelmeyer 2024, Theorem 1; matches Tao 2017 Conjecture 4.1 (L=1; general L by scaling)
holds-here: yes — resolves the periodic variant; does not transfer to the plain Jordan-curve case
falsifies: a pair of disjoint periodic curves without an inscribed square; or a published error in the Floer computation
anchor: research/sources/hugelmeyer-2024-periodic-square-peg.full.md
```

```claim
id: tao2017-periodic-variant-open
statement: The periodic variant of the square peg problem (a periodic curve in the cylinder inscribing a square, insensitive to small squares) is open even for piecewise-linear curves.
status: superseded (Tao 2017 statement; resolved by Hugelmeyer 2024 — see tao2017-periodic-variant-resolved)
evidence: Tao 2017, Conjecture 4.1 (as of 2017)
holds-here: no longer — Hugelmeyer 2024 resolves it
falsifies: n/a (historical claim only)
contradicts: resolved by hugelmeyer2024-periodic-square-peg
anchor: research/sources/tao2017-integration-approach-arxiv.full.md
```
